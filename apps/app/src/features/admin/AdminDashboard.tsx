import { useState, useEffect } from 'react';
import { api } from '../../services/api';
import {
  Users,
  CheckCircle2,
  XCircle,
  Search,
  LogOut,
  ArrowLeft,
  GraduationCap,
  BarChart3,
  BookOpen,
  X,
  Flame,
} from 'lucide-react';

interface AdminDashboardProps {
  onLogout: () => void;
  onExit: () => void;
}

export const AdminDashboard = ({ onLogout, onExit }: AdminDashboardProps) => {
  const [activeTab, setActiveTab] = useState<'overview' | 'learners'>('overview');
  const [overview, setOverview] = useState<any>(null);
  const [learners, setLearners] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedLearnerId, setSelectedLearnerId] = useState<string | null>(null);
  const [learnerDetail, setLearnerDetail] = useState<any>(null);
  const [detailLoading, setDetailLoading] = useState(false);

  const loadData = async () => {
    setLoading(true);
    try {
      const [ov, lr] = await Promise.all([
        api.getAdminOverview(),
        api.getAdminLearners(searchQuery),
      ]);
      setOverview(ov);
      setLearners(lr.learners || []);
    } catch (e) {
      console.error('Lỗi tải dữ liệu admin:', e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, [searchQuery]);

  const handleOpenDetail = async (lid: string) => {
    setSelectedLearnerId(lid);
    setDetailLoading(true);
    try {
      const detail = await api.getAdminLearnerDetail(lid);
      setLearnerDetail(detail);
    } catch (e) {
      console.error('Lỗi tải chi tiết học viên:', e);
    } finally {
      setDetailLoading(false);
    }
  };

  return (
    <div className="tab-container animate-fade-in" style={{ paddingBottom: '80px' }}>
      {/* Admin Executive Header */}
      <div
        className="glass-panel"
        style={{
          padding: '20px 24px',
          marginBottom: '24px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '16px',
          borderLeft: '4px solid var(--accent-primary)',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
          <div
            style={{
              width: '44px',
              height: '44px',
              borderRadius: '12px',
              background: 'linear-gradient(135deg, #6366f1 0%, #06b6d4 100%)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              boxShadow: '0 0 15px rgba(99, 102, 241, 0.4)',
            }}
          >
            <BarChart3 size={24} color="#fff" />
          </div>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <h2 style={{ fontSize: '1.4rem', fontWeight: 800, margin: 0 }}>
                Hệ Thống Quản Trị & Theo Dõi Học Viên
              </h2>
              <span className="badge badge-indigo">Admin Executive</span>
            </div>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.82rem', margin: 0 }}>
              Cơ sở hạ tầng giám sát năng lực thực tế học sinh và tiến độ săn học bổng quốc tế
            </p>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <button
            className="btn btn-secondary"
            style={{ fontSize: '0.85rem', padding: '8px 14px' }}
            onClick={onExit}
          >
            <ArrowLeft size={16} />
            <span>Về Trang Học Tập</span>
          </button>

          <button
            className="btn btn-secondary"
            style={{ fontSize: '0.85rem', padding: '8px 14px', color: '#fda4af' }}
            onClick={onLogout}
          >
            <LogOut size={16} />
            <span>Đăng Xuất</span>
          </button>
        </div>
      </div>

      {/* Admin Navigation Pills */}
      <div style={{ display: 'flex', gap: '10px', marginBottom: '24px' }}>
        <button
          className={`btn ${activeTab === 'overview' ? 'btn-primary' : 'btn-secondary'}`}
          onClick={() => setActiveTab('overview')}
        >
          <BarChart3 size={16} />
          <span>Tổng Quan Đào Tạo & Lỗ Hổng Kiến Thức</span>
        </button>

        <button
          className={`btn ${activeTab === 'learners' ? 'btn-primary' : 'btn-secondary'}`}
          onClick={() => setActiveTab('learners')}
        >
          <Users size={16} />
          <span>Danh Sách & Đánh Giá Học Viên ({learners.length})</span>
        </button>
      </div>

      {/* TAB 1: OVERVIEW */}
      {activeTab === 'overview' && (
        <div>
          {/* Top KPI Cards */}
          <div
            style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
              gap: '16px',
              marginBottom: '28px',
            }}
          >
            <div className="glass-card">
              <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-muted)', marginBottom: '8px' }}>
                <span style={{ fontSize: '0.85rem' }}>Tổng Số Học Sinh</span>
                <Users size={18} color="#6366f1" />
              </div>
              <div style={{ fontSize: '2rem', fontWeight: 800 }}>{overview?.total_learners || 0}</div>
              <div style={{ fontSize: '0.78rem', color: '#10b981', marginTop: '4px' }}>Học sinh đang theo dõi</div>
            </div>

            <div className="glass-card">
              <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-muted)', marginBottom: '8px' }}>
                <span style={{ fontSize: '0.85rem' }}>Tổng Lượt Làm Bài</span>
                <CheckCircle2 size={18} color="#10b981" />
              </div>
              <div style={{ fontSize: '2rem', fontWeight: 800 }}>{overview?.total_attempts || 0}</div>
              <div style={{ fontSize: '0.78rem', color: '#10b981', marginTop: '4px' }}>Lưu trữ trên PostgreSQL</div>
            </div>

            <div className="glass-card">
              <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-muted)', marginBottom: '8px' }}>
                <span style={{ fontSize: '0.85rem' }}>Tỷ Lệ Đúng Trung Bình</span>
                <Flame size={18} color="#06b6d4" />
              </div>
              <div style={{ fontSize: '2rem', fontWeight: 800, color: '#06b6d4' }}>
                {overview?.avg_accuracy || 0}%
              </div>
              <div style={{ fontSize: '0.78rem', color: 'var(--text-secondary)', marginTop: '4px' }}>Toàn bộ 4 môn STEM</div>
            </div>

            <div className="glass-card">
              <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-muted)', marginBottom: '8px' }}>
                <span style={{ fontSize: '0.85rem' }}>Ứng Viên Săn Học Bổng</span>
                <GraduationCap size={18} color="#f59e0b" />
              </div>
              <div style={{ fontSize: '2rem', fontWeight: 800, color: '#f59e0b' }}>
                {overview?.scholarship_candidates || 0}
              </div>
              <div style={{ fontSize: '0.78rem', color: '#f59e0b', marginTop: '4px' }}>Đã hoàn tất đánh giá hồ sơ</div>
            </div>
          </div>

          {/* Critical Knowledge Gaps (Most failed problems) */}
          <div className="glass-panel" style={{ padding: '24px' }}>
            <h3 style={{ fontSize: '1.2rem', marginBottom: '6px', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <XCircle color="#f43f5e" size={20} />
              <span>Báo Cáo Điểm Nóng: Top Bài Toán Học Sinh Sai Nhiều Nhất</span>
            </h3>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.88rem', marginBottom: '20px' }}>
              Thống kê giúp giáo viên phát hiện ngay các lỗ hổng lý thuyết hoặc bẫy tư duy học sinh đang mắc phải
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {overview?.difficult_problems?.map((item: any, idx: number) => (
                <div
                  key={idx}
                  style={{
                    padding: '16px',
                    borderRadius: 'var(--radius-md)',
                    background: 'rgba(244, 63, 94, 0.05)',
                    border: '1px solid rgba(244, 63, 94, 0.2)',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    flexWrap: 'wrap',
                    gap: '12px',
                  }}
                >
                  <div style={{ flex: 1, minWidth: '240px' }}>
                    <div style={{ display: 'flex', gap: '8px', alignItems: 'center', marginBottom: '6px' }}>
                      <span className="badge badge-rose">Top #{idx + 1} Thất Bại</span>
                      <span className="badge badge-indigo">{item.subject.toUpperCase()}</span>
                      <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Mã: {item.problem_id}</span>
                    </div>
                    <div style={{ fontSize: '0.92rem', color: 'var(--text-primary)', lineHeight: 1.5 }}>
                      {item.statement}
                    </div>
                  </div>

                  <div style={{ textAlign: 'right', minWidth: '140px' }}>
                    <div style={{ fontSize: '1.4rem', fontWeight: 800, color: '#f43f5e' }}>
                      {item.failure_rate}%
                    </div>
                    <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                      Sai {item.wrong_attempts} / {item.total_attempts} lượt
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: LEARNERS DIRECTORY */}
      {activeTab === 'learners' && (
        <div className="glass-panel" style={{ padding: '24px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px', marginBottom: '20px' }}>
            <div>
              <h3 style={{ fontSize: '1.25rem' }}>Danh Sách & Năng Lực Học Viên</h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem' }}>
                Nhấp vào từng học sinh để xem chi tiết năng lực từng môn và phân tích hồ sơ học bổng
              </p>
            </div>

            <div style={{ position: 'relative', minWidth: '280px' }}>
              <Search
                size={16}
                style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }}
              />
              <input
                type="text"
                placeholder="Tìm học sinh theo tên, trường, email..."
                className="input-field"
                style={{ paddingLeft: '36px', fontSize: '0.88rem' }}
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
            </div>
          </div>

          {loading ? (
            <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
              Đang tải danh sách học sinh...
            </div>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.88rem' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-secondary)', borderBottom: '1px solid var(--border-subtle)', textAlign: 'left' }}>
                    <th style={{ padding: '12px 14px' }}>Học Sinh</th>
                    <th style={{ padding: '12px 14px' }}>Trường & Lớp</th>
                    <th style={{ padding: '12px 14px' }}>Mục Tiêu Du Học</th>
                    <th style={{ padding: '12px 14px', textAlign: 'center' }}>Số Bài Đã Làm</th>
                    <th style={{ padding: '12px 14px', textAlign: 'center' }}>Tỷ Lệ Đúng</th>
                    <th style={{ padding: '12px 14px' }}>Học Bổng</th>
                    <th style={{ padding: '12px 14px', textAlign: 'right' }}>Thao Tác</th>
                  </tr>
                </thead>
                <tbody>
                  {learners.map((l) => (
                    <tr
                      key={l.id}
                      style={{
                        borderBottom: '1px solid var(--border-subtle)',
                        cursor: 'pointer',
                        transition: 'background var(--transition-fast)',
                      }}
                      className="hover-row"
                      onClick={() => handleOpenDetail(l.id)}
                    >
                      <td style={{ padding: '12px 14px' }}>
                        <div style={{ fontWeight: 600, color: '#fff' }}>{l.name}</div>
                        <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>{l.email}</div>
                      </td>
                      <td style={{ padding: '12px 14px' }}>
                        <div>{l.school}</div>
                        <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>Lớp {l.grade || 12}</div>
                      </td>
                      <td style={{ padding: '12px 14px', color: '#a5b4fc' }}>
                        {l.target_major || 'STEM / Computer Science'}
                      </td>
                      <td style={{ padding: '12px 14px', textAlign: 'center', fontWeight: 700 }}>
                        {l.total_attempts}
                      </td>
                      <td style={{ padding: '12px 14px', textAlign: 'center' }}>
                        <span
                          className={`badge ${
                            l.accuracy_rate >= 80
                              ? 'badge-emerald'
                              : l.accuracy_rate >= 60
                              ? 'badge-amber'
                              : 'badge-rose'
                          }`}
                        >
                          {l.accuracy_rate}%
                        </span>
                      </td>
                      <td style={{ padding: '12px 14px' }}>
                        {l.scholarship_tier ? (
                          <span className="badge badge-cyan" style={{ fontSize: '0.72rem' }}>
                            {l.scholarship_tier_name?.split(':')[0] || 'Tier Evaluated'} ({l.scholarship_score}đ)
                          </span>
                        ) : (
                          <span style={{ color: 'var(--text-muted)', fontSize: '0.78rem' }}>Chưa nộp hồ sơ</span>
                        )}
                      </td>
                      <td style={{ padding: '12px 14px', textAlign: 'right' }}>
                        <button
                          className="btn btn-secondary"
                          style={{ padding: '5px 10px', fontSize: '0.78rem' }}
                          onClick={(e) => {
                            e.stopPropagation();
                            handleOpenDetail(l.id);
                          }}
                        >
                          Xem Đánh Giá
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}

      {/* LEARNER DETAIL DRAWER / MODAL */}
      {selectedLearnerId && (
        <div
          style={{
            position: 'fixed',
            inset: 0,
            zIndex: 300,
            background: 'rgba(5, 7, 11, 0.82)',
            backdropFilter: 'blur(16px)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '20px',
          }}
          onClick={() => setSelectedLearnerId(null)}
        >
          <div
            className="glass-panel animate-scale-up"
            style={{
              width: '100%',
              maxWidth: '840px',
              maxHeight: '90vh',
              overflowY: 'auto',
              padding: '28px',
              borderRadius: 'var(--radius-lg)',
              boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.7)',
            }}
            onClick={(e) => e.stopPropagation()}
          >
            {detailLoading ? (
              <div style={{ textAlign: 'center', padding: '60px 0', color: 'var(--text-secondary)' }}>
                Đang nạp hồ sơ chi tiết học viên...
              </div>
            ) : learnerDetail ? (
              <div>
                {/* Header */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '20px' }}>
                  <div>
                    <span className="badge badge-indigo" style={{ marginBottom: '8px' }}>
                      Lớp {learnerDetail.learner.grade} • {learnerDetail.learner.school}
                    </span>
                    <h3 style={{ fontSize: '1.5rem', fontWeight: 800 }}>{learnerDetail.learner.name}</h3>
                    <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                      {learnerDetail.learner.email} • Nguyện vọng: {learnerDetail.learner.target_major}
                    </div>
                  </div>

                  <button
                    className="btn btn-secondary"
                    style={{ padding: '8px', borderRadius: '50%' }}
                    onClick={() => setSelectedLearnerId(null)}
                  >
                    <X size={20} />
                  </button>
                </div>

                {/* Subject Competency Bars */}
                <div style={{ marginBottom: '24px' }}>
                  <h4 style={{ fontSize: '1rem', fontWeight: 600, marginBottom: '14px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <BarChart3 size={18} color="#6366f1" />
                    <span>Năng Lực Giải Quyết Vấn Đề Theo Môn Học</span>
                  </h4>

                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '12px' }}>
                    {[
                      { key: 'math', name: 'Toán Học', color: '#6366f1' },
                      { key: 'physics', name: 'Vật Lí', color: '#06b6d4' },
                      { key: 'chemistry', name: 'Hoá Học', color: '#10b981' },
                      { key: 'biology', name: 'Sinh Học', color: '#ec4899' },
                    ].map((subj) => {
                      const st = learnerDetail.subject_stats?.[subj.key] || { attempted: 0, correct: 0, accuracy: 0 };
                      return (
                        <div
                          key={subj.key}
                          style={{
                            padding: '14px',
                            borderRadius: 'var(--radius-md)',
                            background: 'rgba(255, 255, 255, 0.03)',
                            border: '1px solid var(--border-subtle)',
                          }}
                        >
                          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: '6px' }}>
                            <span style={{ fontWeight: 600 }}>{subj.name}</span>
                            <span style={{ color: subj.color, fontWeight: 700 }}>{st.accuracy}%</span>
                          </div>
                          <div style={{ height: '6px', background: 'rgba(255, 255, 255, 0.1)', borderRadius: '3px', overflow: 'hidden' }}>
                            <div style={{ height: '100%', width: `${st.accuracy}%`, background: subj.color, borderRadius: '3px' }} />
                          </div>
                          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '6px' }}>
                            Đúng {st.correct} / {st.attempted} câu
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>

                {/* Scholarship Profile Evaluation */}
                {learnerDetail.scholarship_evaluation && (
                  <div
                    style={{
                      padding: '18px',
                      borderRadius: 'var(--radius-md)',
                      background: 'rgba(245, 158, 11, 0.06)',
                      border: '1px solid rgba(245, 158, 11, 0.25)',
                      marginBottom: '24px',
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                      <h4 style={{ fontSize: '1rem', fontWeight: 700, color: '#f59e0b', display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <GraduationCap size={18} />
                        <span>Đánh Giá Hồ Sơ Săn Học Bổng Toàn Cầu</span>
                      </h4>
                      <span className="badge badge-amber" style={{ fontSize: '0.85rem' }}>
                        {learnerDetail.scholarship_evaluation.tier_name}
                      </span>
                    </div>

                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: '10px', fontSize: '0.86rem', marginBottom: '12px' }}>
                      <div>GPA: <strong>{learnerDetail.scholarship_evaluation.gpa}</strong></div>
                      <div>SAT: <strong>{learnerDetail.scholarship_evaluation.sat}</strong></div>
                      <div>IELTS: <strong>{learnerDetail.scholarship_evaluation.ielts}</strong></div>
                      <div>Điểm Hồ Sơ: <strong style={{ color: '#10b981' }}>{learnerDetail.scholarship_evaluation.total_score} / 100</strong></div>
                    </div>

                    {learnerDetail.scholarship_evaluation.gap_analysis && (
                      <div style={{ fontSize: '0.84rem', color: '#fcd34d' }}>
                        <strong>Lỗ hổng & Chiến lược bổ sung:</strong>
                        <ul style={{ paddingLeft: '18px', marginTop: '4px' }}>
                          {learnerDetail.scholarship_evaluation.gap_analysis.map((g: string, i: number) => (
                            <li key={i}>{g}</li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </div>
                )}

                {/* Recent Quiz Attempts Log */}
                <div>
                  <h4 style={{ fontSize: '1rem', fontWeight: 600, marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <BookOpen size={18} color="#06b6d4" />
                    <span>Lịch Sử 20 Lần Giải Bài Gần Nhất</span>
                  </h4>

                  <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '240px', overflowY: 'auto' }}>
                    {learnerDetail.attempts_history?.map((att: any, aIdx: number) => (
                      <div
                        key={aIdx}
                        style={{
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center',
                          padding: '10px 14px',
                          borderRadius: 'var(--radius-sm)',
                          background: att.correct ? 'rgba(16, 185, 129, 0.05)' : 'rgba(244, 63, 94, 0.05)',
                          border: `1px solid ${att.correct ? 'rgba(16, 185, 129, 0.2)' : 'rgba(244, 63, 94, 0.2)'}`,
                          fontSize: '0.85rem',
                        }}
                      >
                        <div style={{ flex: 1, paddingRight: '12px' }}>
                          <span className="badge badge-indigo" style={{ fontSize: '0.7rem', marginRight: '8px' }}>
                            {att.subject.toUpperCase()}
                          </span>
                          <span>{att.statement}</span>
                        </div>

                        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                          <div>
                            Học sinh chọn: <strong>{att.user_answer}</strong>
                          </div>
                          {att.correct ? (
                            <CheckCircle2 size={18} color="#10b981" />
                          ) : (
                            <XCircle size={18} color="#f43f5e" />
                          )}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            ) : null}
          </div>
        </div>
      )}
    </div>
  );
};
