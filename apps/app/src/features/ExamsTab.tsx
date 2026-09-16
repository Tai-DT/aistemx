import { useState, useEffect } from 'react';
import { api, type Problem } from '../services/api';
import { MathView } from '../components/MathView';
import {
  Clock,
  CheckCircle2,
  XCircle,
  ArrowRight,
  Sparkles,
  ChevronLeft,
} from 'lucide-react';
import confetti from 'canvas-confetti';

interface Exam {
  id: string;
  name: string;
  provider: string;
  subject: string;
  level?: string;
  overview?: string;
  sample_problems?: Problem[];
}

export const ExamsTab = () => {
  const [exams, setExams] = useState<Exam[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeExam, setActiveExam] = useState<Exam | null>(null);
  const [examSession, setExamSession] = useState<{
    problems: Problem[];
    answers: Record<string, string>;
    timeLeftSeconds: number;
    submitted: boolean;
    score: number;
  } | null>(null);

  useEffect(() => {
    const fetchExams = async () => {
      setLoading(true);
      try {
        const data = await api.getExams();
        setExams(data.exams || []);
      } catch (e) {
        console.error('Lỗi tải danh sách đề thi:', e);
      } finally {
        setLoading(false);
      }
    };
    fetchExams();
  }, []);

  // Timer countdown
  useEffect(() => {
    if (!examSession || examSession.submitted || examSession.timeLeftSeconds <= 0) return;

    const timer = setInterval(() => {
      setExamSession((prev) => {
        if (!prev) return null;
        if (prev.timeLeftSeconds <= 1) {
          clearInterval(timer);
          // Auto submit
          handleAutoSubmit(prev);
          return { ...prev, timeLeftSeconds: 0 };
        }
        return { ...prev, timeLeftSeconds: prev.timeLeftSeconds - 1 };
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [examSession?.submitted, examSession?.timeLeftSeconds]);

  const handleStartExam = async (exam: Exam) => {
    setLoading(true);
    try {
      const detail = await api.getExamDetail(exam.id);
      setActiveExam(detail);
      const problems = detail.sample_problems || [];
      const durationSeconds = 45 * 60; // 45 phút tiêu chuẩn

      setExamSession({
        problems,
        answers: {},
        timeLeftSeconds: durationSeconds,
        submitted: false,
        score: 0,
      });
    } catch (e) {
      console.error('Lỗi bắt đầu kỳ thi:', e);
    } finally {
      setLoading(false);
    }
  };

  const handleSelectAnswer = (problemId: string, choiceKey: string) => {
    if (!examSession || examSession.submitted) return;
    setExamSession((prev) => {
      if (!prev) return null;
      return {
        ...prev,
        answers: { ...prev.answers, [problemId]: choiceKey },
      };
    });
  };

  const calculateScore = (session: typeof examSession) => {
    if (!session || session.problems.length === 0) return 0;
    let correctCount = 0;
    session.problems.forEach((p) => {
      const userAns = session.answers[p.id];
      if (userAns && userAns.toUpperCase() === p.answer.trim().toUpperCase()) {
        correctCount++;
      }
    });
    return Math.round((correctCount / session.problems.length) * 100);
  };

  const handleSubmitExam = () => {
    if (!examSession) return;
    const finalScore = calculateScore(examSession);
    setExamSession((prev) => (prev ? { ...prev, submitted: true, score: finalScore } : null));

    if (finalScore >= 80) {
      confetti({ particleCount: 80, spread: 80 });
    }
  };

  const handleAutoSubmit = (currentSession: NonNullable<typeof examSession>) => {
    const finalScore = calculateScore(currentSession);
    setExamSession({ ...currentSession, submitted: true, score: finalScore });
  };

  const formatTime = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  // NẾU ĐANG TRONG PHÒNG THI
  if (examSession && activeExam) {
    const correctCount = examSession.problems.filter(
      (p) => examSession.answers[p.id]?.toUpperCase() === p.answer.trim().toUpperCase()
    ).length;

    return (
      <div className="tab-container animate-fade-in" style={{ paddingBottom: '60px' }}>
        {/* Sticky Exam Top Bar */}
        <div
          className="glass-panel"
          style={{
            position: 'sticky',
            top: '80px',
            zIndex: 90,
            padding: '16px 24px',
            marginBottom: '24px',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            flexWrap: 'wrap',
            gap: '16px',
            borderBottom: '2px solid var(--accent-primary)',
          }}
        >
          <div>
            <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
              <span className="badge badge-indigo">{activeExam.provider}</span>
              <span className="badge badge-emerald">{activeExam.subject.toUpperCase()}</span>
            </div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 800, margin: '4px 0 0' }}>{activeExam.name}</h3>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
            {/* Countdown Clock */}
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                padding: '8px 16px',
                borderRadius: 'var(--radius-full)',
                background: examSession.timeLeftSeconds < 300 ? 'rgba(244, 63, 94, 0.15)' : 'rgba(99, 102, 241, 0.15)',
                border: `1px solid ${examSession.timeLeftSeconds < 300 ? '#f43f5e' : 'var(--accent-primary)'}`,
                color: examSession.timeLeftSeconds < 300 ? '#f43f5e' : '#a5b4fc',
                fontSize: '1.1rem',
                fontWeight: 800,
                fontFamily: 'var(--font-mono)',
              }}
            >
              <Clock size={18} />
              <span>{formatTime(examSession.timeLeftSeconds)}</span>
            </div>

            {!examSession.submitted ? (
              <button className="btn btn-primary" onClick={handleSubmitExam}>
                <span>Nộp Bài Thi</span>
              </button>
            ) : (
              <button
                className="btn btn-secondary"
                onClick={() => {
                  setExamSession(null);
                  setActiveExam(null);
                }}
              >
                <ChevronLeft size={16} />
                <span>Rời Phòng Thi</span>
              </button>
            )}
          </div>
        </div>

        {/* Exam Results Score Card */}
        {examSession.submitted && (
          <div
            className="glass-panel animate-scale-up"
            style={{
              padding: '28px',
              marginBottom: '28px',
              textAlign: 'center',
              border: '1px solid rgba(16, 185, 129, 0.3)',
              background: 'radial-gradient(ellipse at center, rgba(16, 185, 129, 0.1) 0%, rgba(10, 13, 20, 0.9) 70%)',
            }}
          >
            <h2 style={{ fontSize: '1.8rem', fontWeight: 800, marginBottom: '6px' }}>Kết Quả Thi Thử</h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '20px' }}>
              Bài thi: <strong>{activeExam.name}</strong>
            </p>

            <div style={{ display: 'flex', justifyContent: 'center', gap: '30px', flexWrap: 'wrap', marginBottom: '20px' }}>
              <div>
                <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>ĐIỂM SỐ</div>
                <div style={{ fontSize: '2.5rem', fontWeight: 900, color: examSession.score >= 80 ? '#10b981' : '#f59e0b' }}>
                  {examSession.score} / 100
                </div>
              </div>

              <div>
                <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>SỐ CÂU ĐÚNG</div>
                <div style={{ fontSize: '2.5rem', fontWeight: 900, color: '#f8fafc' }}>
                  {correctCount} / {examSession.problems.length}
                </div>
              </div>

              <div>
                <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>XẾP HẠNG</div>
                <div style={{ fontSize: '2.5rem', fontWeight: 900, color: '#06b6d4' }}>
                  {examSession.score >= 85 ? 'Xuất Sắc' : examSession.score >= 65 ? 'Đạt Chuẩn' : 'Cần Cố Gắng'}
                </div>
              </div>
            </div>

            <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)' }}>
              Hãy xem lại phân tích lời giải chi tiết và các bẫy sai lầm của từng câu ở bên dưới.
            </p>
          </div>
        )}

        {/* Questions List */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {examSession.problems.map((p, idx) => {
            const userChoice = examSession.answers[p.id];
            const isCorrect = userChoice?.toUpperCase() === p.answer.trim().toUpperCase();

            return (
              <div
                key={p.id}
                className="glass-panel"
                style={{
                  padding: '24px',
                  borderLeft: examSession.submitted
                    ? isCorrect
                      ? '4px solid #10b981'
                      : '4px solid #f43f5e'
                    : '4px solid var(--border-subtle)',
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '14px' }}>
                  <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                    <span className="badge badge-indigo">Câu {idx + 1}</span>
                    <span className="badge badge-amber">Độ khó: {p.difficulty || 2}/5</span>
                  </div>

                  {examSession.submitted && (
                    <div>
                      {isCorrect ? (
                        <span className="badge badge-emerald">
                          <CheckCircle2 size={13} /> Đúng (+1 câu)
                        </span>
                      ) : (
                        <span className="badge badge-rose">
                          <XCircle size={13} /> Sai (Đáp án: {p.answer})
                        </span>
                      )}
                    </div>
                  )}
                </div>

                <div style={{ fontSize: '1.05rem', lineHeight: 1.6, marginBottom: '18px' }}>
                  <MathView content={p.statement_vi} />
                </div>

                {/* Multiple Choices */}
                {p.choices && (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                    {p.choices.map((c) => {
                      const isSelected = userChoice === c.key;
                      const isKeyCorrect = c.key.toUpperCase() === p.answer.trim().toUpperCase();

                      let btnStyle: React.CSSProperties = {
                        display: 'flex',
                        alignItems: 'center',
                        gap: '12px',
                        padding: '12px 16px',
                        borderRadius: 'var(--radius-md)',
                        background: 'rgba(255, 255, 255, 0.03)',
                        border: '1px solid var(--border-subtle)',
                        cursor: examSession.submitted ? 'default' : 'pointer',
                        textAlign: 'left',
                      };

                      if (examSession.submitted) {
                        if (isKeyCorrect) {
                          btnStyle = { ...btnStyle, background: 'rgba(16, 185, 129, 0.15)', border: '1px solid #10b981' };
                        } else if (isSelected && !isKeyCorrect) {
                          btnStyle = { ...btnStyle, background: 'rgba(244, 63, 94, 0.15)', border: '1px solid #f43f5e' };
                        }
                      } else if (isSelected) {
                        btnStyle = { ...btnStyle, background: 'rgba(99, 102, 241, 0.15)', border: '1px solid var(--accent-primary)' };
                      }

                      return (
                        <div key={c.key}>
                          <div
                            style={btnStyle}
                            onClick={() => handleSelectAnswer(p.id, c.key)}
                            className={!examSession.submitted ? 'choice-hover' : ''}
                          >
                            <div
                              style={{
                                width: '28px',
                                height: '28px',
                                borderRadius: '50%',
                                background: isSelected ? 'var(--accent-primary)' : 'rgba(255, 255, 255, 0.1)',
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                fontWeight: 700,
                                fontSize: '0.85rem',
                              }}
                            >
                              {c.key}
                            </div>
                            <div style={{ flex: 1 }}>
                              <MathView content={c.text} />
                            </div>
                          </div>

                          {/* Show Why Wrong Distractor if Incorrect */}
                          {examSession.submitted && isSelected && !isKeyCorrect && c.why_wrong && (
                            <div
                              style={{
                                marginTop: '6px',
                                marginLeft: '40px',
                                padding: '8px 12px',
                                borderRadius: 'var(--radius-sm)',
                                background: 'rgba(244, 63, 94, 0.08)',
                                borderLeft: '3px solid #f43f5e',
                                fontSize: '0.84rem',
                                color: '#fda4af',
                              }}
                            >
                              ⚠️ <strong>Bẫy lý thuyết:</strong> {c.why_wrong}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    );
  }

  // DANH SÁCH 41 KỲ THI CHUẨN HOÁ
  return (
    <div className="tab-container animate-fade-in">
      {/* Header */}
      <div className="glass-panel" style={{ padding: '24px', marginBottom: '24px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <h2 style={{ fontSize: '1.5rem', display: 'flex', alignItems: 'center', gap: '10px' }}>
              <Clock style={{ color: '#f59e0b' }} />
              <span>Phòng Thi Thử</span>
            </h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.88rem', marginTop: '4px' }}>
              Luyện đề thi thử có bấm giờ: AP Calculus, SAT, THPT Quốc Gia và Olympic.
            </p>
          </div>
          <div className="badge badge-amber">
            <Sparkles size={14} />
            <span>Thi thử bấm giờ</span>
          </div>
        </div>
      </div>

      {/* Grid of Exams */}
      {loading ? (
        <div style={{ textAlign: 'center', padding: '60px 0', color: 'var(--text-muted)' }}>
          Đang nạp danh sách 41 kỳ thi chuẩn...
        </div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(340px, 1fr))', gap: '20px' }}>
          {exams.map((exam) => (
            <div
              key={exam.id}
              className="glass-card"
              style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}
            >
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '12px' }}>
                  <span className="badge badge-indigo">{exam.provider}</span>
                  <span className="badge badge-cyan">{exam.subject.toUpperCase()}</span>
                </div>

                <h3 style={{ fontSize: '1.25rem', fontWeight: 800, lineHeight: 1.3, marginBottom: '8px' }}>
                  {exam.name}
                </h3>

                <p style={{ fontSize: '0.86rem', color: 'var(--text-secondary)', lineHeight: 1.5, marginBottom: '16px' }}>
                  {exam.overview?.slice(0, 180)}...
                </p>
              </div>

              <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: '14px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', fontSize: '0.82rem', color: 'var(--text-muted)' }}>
                  <span>⏱️ Thời gian: 45 phút</span>
                  <span>📝 20-25 câu hỏi</span>
                </div>

                <button
                  className="btn btn-primary"
                  style={{ width: '100%', fontSize: '0.88rem' }}
                  onClick={() => handleStartExam(exam)}
                >
                  <Clock size={16} />
                  <span>Vào Phòng Thi Thử Ngay</span>
                  <ArrowRight size={14} />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
