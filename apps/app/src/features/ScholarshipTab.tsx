import { useState, useEffect } from 'react';
import { api, type Scholarship, type ReadinessScore, type STARFeedback } from '../services/api';
import { GraduationCap, Award, MessageSquare, AlertTriangle, ExternalLink, Sparkles, Send } from 'lucide-react';
import confetti from 'canvas-confetti';

export const ScholarshipTab = () => {

  const [subTab, setSubTab] = useState<'directory' | 'readiness' | 'interview'>('directory');
  const [scholarships, setScholarships] = useState<Scholarship[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCountry, setSelectedCountry] = useState('');

  // Form Đánh giá Hồ sơ (Readiness)
  const [gpa, setGpa] = useState<number>(3.85);
  const [sat, setSat] = useState<number>(1520);
  const [ielts, setIelts] = useState<number>(8.0);
  const [awardLevel, setAwardLevel] = useState<string>('national_first');
  const [hasSpikeProject, setHasSpikeProject] = useState<boolean>(true);
  const [researchPapers, setResearchPapers] = useState<number>(1);
  const [readinessResult, setReadinessResult] = useState<ReadinessScore | null>(null);
  const [evaluating, setEvaluating] = useState(false);

  // Form Luyện Phỏng Vấn STAR
  const [questions, setQuestions] = useState<Array<{ id: string; question_vi: string; focus_area: string }>>([]);
  const [selectedQuestion, setSelectedQuestion] = useState<string>('');
  const [interviewAnswer, setInterviewAnswer] = useState<string>('');
  const [starFeedback, setStarFeedback] = useState<STARFeedback | null>(null);
  const [interviewEvaluating, setInterviewEvaluating] = useState(false);

  useEffect(() => {
    const initData = async () => {
      setLoading(true);
      try {
        const schData = await api.getScholarships();
        setScholarships(schData.scholarships || []);

        const qData = await api.getInterviewQuestions();
        const qList = qData.questions || [];
        setQuestions(qList);
        if (qList.length > 0) setSelectedQuestion(qList[0].id);
      } catch (e) {
        console.error(e);
      } finally {
        setLoading(false);
      }
    };
    initData();
  }, []);

  const handleEvaluateReadiness = async (e: React.FormEvent) => {
    e.preventDefault();
    setEvaluating(true);
    try {
      const awards = awardLevel ? [awardLevel] : [];
      const spikes = hasSpikeProject ? ['founder_open_source_stem_ai'] : [];
      const res = await api.evaluateReadiness({
        gpa,
        sat,
        ielts,
        stem_awards: awards,
        spike_projects: spikes,
        research_papers: researchPapers,
        leadership_roles: ['lead_stem_club'],
        essay_readiness: 85,
      });
      setReadinessResult(res);

      if (res.total_score >= 80) {
        confetti({ particleCount: 70, spread: 80 });
      }
    } catch (e) {
      console.error(e);
    } finally {
      setEvaluating(false);
    }
  };

  const handleEvaluateInterview = async () => {
    if (!selectedQuestion || !interviewAnswer.trim()) return;
    setInterviewEvaluating(true);
    try {
      const res = await api.evaluateInterviewAnswer(selectedQuestion, interviewAnswer);
      setStarFeedback(res);
      if (res.overall_score >= 80) {
        confetti({ particleCount: 60, spread: 70 });
      }
    } catch (e) {
      console.error(e);
    } finally {
      setInterviewEvaluating(false);
    }
  };

  return (
    <div className="tab-container animate-fade-in">
      {/* Sub-tab Navigation */}
      <div style={{ display: 'flex', gap: '10px', marginBottom: '24px', flexWrap: 'wrap' }}>
        <button
          className={`btn ${subTab === 'directory' ? 'btn-primary' : 'btn-secondary'}`}
          onClick={() => setSubTab('directory')}
        >
          <GraduationCap size={16} />
          <span>Danh Sách Học Bổng</span>
        </button>
        <button
          className={`btn ${subTab === 'readiness' ? 'btn-primary' : 'btn-secondary'}`}
          onClick={() => setSubTab('readiness')}
        >
          <Award size={16} />
          <span>Đánh Giá Hồ Sơ</span>
        </button>
        <button
          className={`btn ${subTab === 'interview' ? 'btn-primary' : 'btn-secondary'}`}
          onClick={() => setSubTab('interview')}
        >
          <MessageSquare size={16} />
          <span>Luyện Phỏng Vấn</span>
        </button>
      </div>

      {/* SubTab 1: Directory */}
      {subTab === 'directory' && (
        <div>
          <div className="glass-panel" style={{ padding: '24px', marginBottom: '20px' }}>
            <h3 style={{ fontSize: '1.4rem', marginBottom: '6px' }}>Học Bổng Toàn Phần & Danh Giá</h3>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '16px' }}>
              Khám phá các chương trình học bổng uy tín: Mỹ, Anh, Đức, Nhật Bản, Singapore, Việt Nam...
            </p>

            {/* Country Filters & Search */}
            <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '14px' }}>
              {['', 'Mỹ', 'Vương quốc Anh', 'Đức', 'Nhật Bản', 'Hàn Quốc', 'Singapore', 'Pháp', 'Thụy Điển', 'Việt Nam'].map((c) => (
                <button
                  key={c}
                  className={`btn ${selectedCountry === c ? 'btn-primary' : 'btn-secondary'}`}
                  style={{ fontSize: '0.82rem', padding: '5px 12px', borderRadius: 'var(--radius-full)' }}
                  onClick={() => setSelectedCountry(c)}
                >
                  {c === '' ? 'Tất cả quốc gia' : c}
                </button>
              ))}
            </div>

            <input
              type="text"
              placeholder="Tìm học bổng theo tên trường, đơn vị tài trợ, từ khoá..."
              className="input-field"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>

          {loading ? (
            <div style={{ textAlign: 'center', padding: '60px 0', color: 'var(--text-secondary)' }}>
              <div className="pulse-glow" style={{ width: '40px', height: '40px', borderRadius: '50%', background: 'var(--accent-primary)', margin: '0 auto 16px' }} />
              <p>Đang nạp 25 chương trình học bổng toàn cầu...</p>
            </div>
          ) : (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(350px, 1fr))', gap: '16px' }}>
              {scholarships
                .filter((s) => {
                  if (selectedCountry && s.country !== selectedCountry) return false;
                  if (searchQuery.trim()) {
                    const q = searchQuery.toLowerCase();
                    return (
                      s.name.toLowerCase().includes(q) ||
                      s.provider.toLowerCase().includes(q) ||
                      s.overview.toLowerCase().includes(q) ||
                      s.country.toLowerCase().includes(q)
                    );
                  }
                  return true;
                })
                .map((s) => (
                <div key={s.id} className="glass-card" style={{ display: 'flex', flexDirection: 'column' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '12px' }}>
                    <span className="badge badge-indigo">{s.country}</span>
                    <span className="badge badge-emerald">{s.coverage}</span>
                  </div>


                <h4 style={{ fontSize: '1.2rem', marginBottom: '6px', color: 'var(--text-primary)' }}>{s.name}</h4>
                <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '16px' }}>{s.provider}</p>

                <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border-subtle)', padding: '12px', borderRadius: 'var(--radius-sm)', marginBottom: '16px', fontSize: '0.86rem', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px' }}>
                  <div><strong>Giá trị:</strong> <span style={{ color: '#059669', fontWeight: 700 }}>${s.financial_value_usd.toLocaleString()}/năm</span></div>
                  <div><strong>GPA tối thiểu:</strong> {s.gpa_min}/4.0</div>
                  <div><strong>SAT yêu cầu:</strong> {s.sat_min > 0 ? `${s.sat_min}+` : 'Tuỳ chọn'}</div>
                  <div><strong>IELTS:</strong> {s.ielts_min}+</div>
                </div>

                <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: '16px', flex: 1 }}>
                  {s.overview}
                </p>

                <a
                  href={s.official_url}
                  target="_blank"
                  rel="noreferrer"
                  className="btn btn-secondary"
                  style={{ width: '100%', fontSize: '0.85rem' }}
                >
                  <span>Website Chính Thức</span>
                  <ExternalLink size={14} />
                </a>
              </div>
            ))}
          </div>
        )}
      </div>
    )}



      {/* SubTab 2: Readiness Calculator */}
      {subTab === 'readiness' && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: '24px' }}>
          {/* Form */}
          <div className="glass-panel" style={{ padding: '28px' }}>
            <h3 style={{ fontSize: '1.35rem', marginBottom: '18px', display: 'flex', alignItems: 'center', gap: '10px' }}>
              <Award style={{ color: 'var(--accent-warning)' }} />
              <span>Nhập Thông Tin Ứng Viên</span>
            </h3>

            <form onSubmit={handleEvaluateReadiness} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                  Điểm GPA THPT (Thang 4.0): <strong style={{ color: 'var(--text-primary)' }}>{gpa}</strong>
                </label>
                <input
                  type="range"
                  min="3.0"
                  max="4.0"
                  step="0.05"
                  value={gpa}
                  onChange={(e) => setGpa(parseFloat(e.target.value))}
                  style={{ width: '100%', accentColor: '#0284c7' }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                  Điểm SAT (400 - 1600): <strong style={{ color: 'var(--text-primary)' }}>{sat}</strong>
                </label>
                <input
                  type="range"
                  min="1200"
                  max="1600"
                  step="10"
                  value={sat}
                  onChange={(e) => setSat(parseInt(e.target.value))}
                  style={{ width: '100%', accentColor: '#0284c7' }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                  Điểm IELTS: <strong style={{ color: 'var(--text-primary)' }}>{ielts}</strong>
                </label>
                <input
                  type="range"
                  min="6.0"
                  max="9.0"
                  step="0.5"
                  value={ielts}
                  onChange={(e) => setIelts(parseFloat(e.target.value))}
                  style={{ width: '100%', accentColor: '#0284c7' }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                  Giải Thưởng Học Thuật STEM Cao Nhất:
                </label>
                <select
                  value={awardLevel}
                  onChange={(e) => setAwardLevel(e.target.value)}
                  className="input-field"
                >
                  <option value="international_gold">Huy Chương Vàng Quốc Tế (IMO, IPhO, IChO, IBO)</option>
                  <option value="international_bronze">Huy Chương Bạc / Đồng Quốc Tế</option>
                  <option value="national_first">Giải Nhất / Nhì Quốc Gia (HSG QG / ISEF)</option>
                  <option value="national_third">Giải Ba / Khuyến Khích Quốc Gia</option>
                  <option value="provincial_first">Giải Nhất Tỉnh / Thành Phố</option>
                  <option value="">Không có giải chính thức</option>
                </select>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <input
                  type="checkbox"
                  id="spikeCheck"
                  checked={hasSpikeProject}
                  onChange={(e) => setHasSpikeProject(e.target.checked)}
                  style={{ width: '18px', height: '18px' }}
                />
                <label htmlFor="spikeCheck" style={{ fontSize: '0.9rem', color: 'var(--text-primary)', cursor: 'pointer' }}>
                  Có Dự Án Trọng Tâm Đột Phá (Spike Profile / Nghiên Cứu Độc Lập)
                </label>
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                  Số Lượng Bài Báo Nghiên Cứu Khoa Học (Scopus / Hội Thảo):
                </label>
                <input
                  type="number"
                  min="0"
                  max="10"
                  value={researchPapers}
                  onChange={(e) => setResearchPapers(parseInt(e.target.value) || 0)}
                  className="input-field"
                />
              </div>

              <button type="submit" className="btn btn-primary" style={{ marginTop: '10px' }} disabled={evaluating}>
                <Sparkles size={16} />
                <span>{evaluating ? 'Đang phân tích hồ sơ...' : 'Đánh Giá Độ Sẵn Sàng (Evaluate)'}</span>
              </button>
            </form>
          </div>

          {/* Result Card */}
          <div className="glass-panel" style={{ padding: '28px' }}>
            {readinessResult ? (
              <div className="animate-fade-in">
                <div style={{ textAlign: 'center', marginBottom: '24px' }}>
                  <span className="badge badge-amber" style={{ fontSize: '0.85rem' }}>{readinessResult.tier}</span>
                  <h2 style={{ fontSize: '3.2rem', color: '#f59e0b', margin: '8px 0' }}>{readinessResult.total_score}</h2>
                  <p style={{ color: 'var(--text-secondary)', fontSize: '1.05rem', fontWeight: 600 }}>{readinessResult.tier_name}</p>
                </div>

                {/* Score Breakdown Bars */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '24px' }}>
                  <div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: '4px' }}>
                      <span>Học Thuật (GPA, SAT, IELTS)</span>
                      <strong>{readinessResult.breakdown.academics}/25</strong>
                    </div>
                    <div style={{ background: 'rgba(255,255,255,0.08)', borderRadius: '4px', height: '8px', overflow: 'hidden' }}>
                      <div style={{ width: `${(readinessResult.breakdown.academics / 25) * 100}%`, background: '#6366f1', height: '100%' }} />
                    </div>
                  </div>

                  <div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: '4px' }}>
                      <span>Giải Thưởng STEM</span>
                      <strong>{readinessResult.breakdown.stem_awards}/25</strong>
                    </div>
                    <div style={{ background: 'rgba(255,255,255,0.08)', borderRadius: '4px', height: '8px', overflow: 'hidden' }}>
                      <div style={{ width: `${(readinessResult.breakdown.stem_awards / 25) * 100}%`, background: '#10b981', height: '100%' }} />
                    </div>
                  </div>

                  <div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: '4px' }}>
                      <span>Hồ Sơ Đột Phá (Spike Profile)</span>
                      <strong>{readinessResult.breakdown.spike_profile}/25</strong>
                    </div>
                    <div style={{ background: 'rgba(255,255,255,0.08)', borderRadius: '4px', height: '8px', overflow: 'hidden' }}>
                      <div style={{ width: `${(readinessResult.breakdown.spike_profile / 25) * 100}%`, background: '#f59e0b', height: '100%' }} />
                    </div>
                  </div>

                  <div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: '4px' }}>
                      <span>Bài Luận & Thư Giới Thiệu</span>
                      <strong>{readinessResult.breakdown.essays_and_lors}/25</strong>
                    </div>
                    <div style={{ background: 'rgba(255,255,255,0.08)', borderRadius: '4px', height: '8px', overflow: 'hidden' }}>
                      <div style={{ width: `${(readinessResult.breakdown.essays_and_lors / 25) * 100}%`, background: '#06b6d4', height: '100%' }} />
                    </div>
                  </div>
                </div>

                {/* Gap Checklist */}
                {readinessResult.gap_analysis && readinessResult.gap_analysis.length > 0 && (
                  <div style={{ background: 'rgba(245, 158, 11, 0.08)', border: '1px solid rgba(245, 158, 11, 0.2)', padding: '16px', borderRadius: 'var(--radius-md)' }}>
                    <h5 style={{ color: '#f59e0b', display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '8px' }}>
                      <AlertTriangle size={16} /> Danh Mục Cần Cải Thiện (Gap Analysis):
                    </h5>
                    <ul style={{ paddingLeft: '18px', fontSize: '0.88rem', color: 'var(--text-primary)', display: 'flex', flexDirection: 'column', gap: '4px' }}>
                      {readinessResult.gap_analysis.map((gap, i) => (
                        <li key={i}>{gap}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ) : (
              <div style={{ textAlign: 'center', padding: '60px 20px', color: 'var(--text-muted)' }}>
                <Award size={48} style={{ margin: '0 auto 16px', opacity: 0.3 }} />
                <p>Nhập thông số học thuật bên trái và bấm Đánh Giá để xem phân tầng hồ sơ và danh mục khuyến nghị.</p>
              </div>
            )}
          </div>
        </div>
      )}

      {/* SubTab 3: STAR Interview Simulator */}
      {subTab === 'interview' && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: '24px' }}>
          {/* Question & Answer Panel */}
          <div className="glass-panel" style={{ padding: '28px' }}>
            <h3 style={{ fontSize: '1.35rem', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '10px' }}>
              <MessageSquare style={{ color: 'var(--accent-primary)' }} />
              <span>Phòng Phỏng Vấn Học Bổng Chuẩn STAR</span>
            </h3>

            <div style={{ marginBottom: '16px' }}>
              <label style={{ display: 'block', fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                Chọn Câu Hỏi Phỏng Vấn:
              </label>
              <select
                value={selectedQuestion}
                onChange={(e) => setSelectedQuestion(e.target.value)}
                className="input-field"
              >
                {questions.map((q) => (
                  <option key={q.id} value={q.id}>
                    [{q.focus_area}] {q.question_vi}
                  </option>
                ))}
              </select>
            </div>

            <div style={{ marginBottom: '16px' }}>
              <label style={{ display: 'block', fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                Nội Dung Câu Trả Lời Của Bạn (Khuyến khích cấu trúc theo S - T - A - R):
              </label>
              <textarea
                rows={8}
                value={interviewAnswer}
                onChange={(e) => setInterviewAnswer(e.target.value)}
                placeholder="Ví dụ: Trong một dự án nghiên cứu thuật toán tại trường (Situation), nhóm tôi gặp phải bài toán tối ưu hoá độ trễ dưới 50ms (Task). Tôi đã đề xuất cấu trúc dữ liệu mới và tái lập trình bằng C++ (Action), kết quả đạt độ trễ 28ms và dự án giành giải Nhất toàn trường (Result)..."
                className="input-field"
                style={{ resize: 'vertical' }}
              />
            </div>

            <button
              onClick={handleEvaluateInterview}
              disabled={interviewEvaluating || !interviewAnswer.trim()}
              className="btn btn-primary"
              style={{ width: '100%' }}
            >
              <Send size={16} />
              <span>{interviewEvaluating ? 'AI Đang Phân Tích STAR...' : 'Chấm Điểm Phỏng Vấn Tức Thì'}</span>
            </button>
          </div>

          {/* AI Feedback Panel */}
          <div className="glass-panel" style={{ padding: '28px' }}>
            {starFeedback ? (
              <div className="animate-fade-in">
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
                  <div>
                    <span className="badge badge-emerald">Đánh Giá Phản Xạ STAR</span>
                    <h2 style={{ fontSize: '2.8rem', color: '#10b981', margin: '6px 0' }}>{starFeedback.overall_score}/100</h2>
                  </div>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px' }}>
                    <div style={{ padding: '8px 12px', borderRadius: '8px', background: starFeedback.components_found.situation ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)', fontSize: '0.82rem', fontWeight: 600 }}>
                      S (Tình huống): {starFeedback.scores.situation}/25
                    </div>
                    <div style={{ padding: '8px 12px', borderRadius: '8px', background: starFeedback.components_found.task ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)', fontSize: '0.82rem', fontWeight: 600 }}>
                      T (Nhiệm vụ): {starFeedback.scores.task}/25
                    </div>
                    <div style={{ padding: '8px 12px', borderRadius: '8px', background: starFeedback.components_found.action ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)', fontSize: '0.82rem', fontWeight: 600 }}>
                      A (Hành động): {starFeedback.scores.action}/25
                    </div>
                    <div style={{ padding: '8px 12px', borderRadius: '8px', background: starFeedback.components_found.result ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)', fontSize: '0.82rem', fontWeight: 600 }}>
                      R (Kết quả): {starFeedback.scores.result}/25
                    </div>
                  </div>
                </div>

                {starFeedback.actionable_advice && starFeedback.actionable_advice.length > 0 && (
                  <div style={{ background: 'rgba(99, 102, 241, 0.08)', border: '1px solid rgba(99, 102, 241, 0.2)', padding: '16px', borderRadius: 'var(--radius-md)' }}>
                    <h5 style={{ color: 'var(--text-accent)', marginBottom: '8px' }}>Lời Khuyên Nâng Cao Điểm Số:</h5>
                    <ul style={{ paddingLeft: '18px', fontSize: '0.9rem', color: 'var(--text-primary)', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                      {starFeedback.actionable_advice.map((adv, i) => (
                        <li key={i}>{adv}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ) : (
              <div style={{ textAlign: 'center', padding: '60px 20px', color: 'var(--text-muted)' }}>
                <MessageSquare size={48} style={{ margin: '0 auto 16px', opacity: 0.3 }} />
                <p>Chọn câu hỏi và viết câu trả lời theo phương pháp STAR bên trái để nhận phản hồi từ bộ máy phân tích.</p>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
