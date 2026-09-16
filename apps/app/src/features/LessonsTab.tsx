import { useState, useEffect, useCallback, useMemo } from 'react';
import { api, type LearningRoadmap } from '../services/api';
import { Pagination } from '../components/Pagination';
import { LessonModal } from './lessons/LessonModal';
import {
  BookOpen,
  Search,
  Sparkles,
  Eye,
  GitFork,
  Clock,
  Compass,
  Layers,
  Calendar,
  CheckCircle2,
  ChevronRight,
  Target,
  Video,
} from 'lucide-react';

export const LessonsTab = () => {
  // Navigation & View Mode
  const [activeTab, setActiveTab] = useState<'matrix' | 'roadmap'>('matrix');

  // Matrix View State
  const [lessons, setLessons] = useState<any[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(true);
  const [subject, setSubject] = useState<string>('');
  const [level, setLevel] = useState<string>('');
  const [grade, setGrade] = useState<string>('');
  const [query, setQuery] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [selectedLessonId, setSelectedLessonId] = useState<string | null>(null);
  const pageSize = 24;

  // Roadmap View State
  const [goalQuery, setGoalQuery] = useState('tích phân');
  const [maxLessons, setMaxLessons] = useState(15);
  const [sessionMinutes, setSessionMinutes] = useState(60);
  const [roadmapData, setRoadmapData] = useState<LearningRoadmap | null>(null);
  const [roadmapLoading, setRoadmapLoading] = useState(false);
  const [roadmapError, setRoadmapError] = useState<string | null>(null);
  const [roadmapViewType, setRoadmapViewType] = useState<'milestones' | 'sessions'>('milestones');

  const loadLessons = useCallback(
    async (pageToLoad = 1) => {
      setLoading(true);
      try {
        const data = await api.getLessons({
          subject: subject || undefined,
          level: level || undefined,
          grade: grade ? Number(grade) : undefined,
          page: pageToLoad,
          page_size: pageSize,
        });
        setLessons(data.lessons || []);
        setTotal(data.total || 0);
        setCurrentPage(pageToLoad);
      } catch (e) {
        console.error('Lỗi tải bài học:', e);
      } finally {
        setLoading(false);
      }
    },
    [subject, level, grade]
  );

  useEffect(() => {
    loadLessons(1);
  }, [subject, level, grade]);

  // Sinh lộ trình học từ gốc
  const handleGenerateRoadmap = async (targetGoal?: string) => {
    const goalToRun = targetGoal || goalQuery;
    if (!goalToRun.trim()) return;
    setRoadmapLoading(true);
    setRoadmapError(null);
    try {
      const data = await api.generateRoadmap({
        goal: goalToRun.trim(),
        max_lessons: maxLessons,
        minutes_per_session: sessionMinutes,
        practice_per_lesson: 2,
      });
      setRoadmapData(data);
      setActiveTab('roadmap');
    } catch (e: any) {
      console.error('Lỗi sinh lộ trình:', e);
      setRoadmapError(e?.message || 'Không thể tạo lộ trình cho mục tiêu này. Vui lòng thử từ khóa cụ thể hơn.');
    } finally {
      setRoadmapLoading(false);
    }
  };

  const subjectPills = [
    { id: '', label: 'Tất cả môn' },
    { id: 'math', label: 'Toán Học' },
    { id: 'physics', label: 'Vật Lí' },
    { id: 'chemistry', label: 'Hoá Học' },
    { id: 'biology', label: 'Sinh Học' },
  ];

  const popularGoals = [
    { label: 'Tích Phân & Ứng Dụng', goal: 'tích phân', subject: 'math' },
    { label: 'Đạo Hàm & Tiếp Tuyến', goal: 'đạo hàm', subject: 'math' },
    { label: 'Định Luật Newton & Động Lực Học', goal: 'định luật newton', subject: 'physics' },
    { label: 'Dao Động Cơ & Sóng Cơ', goal: 'dao động cơ', subject: 'physics' },
    { label: 'Cân Bằng Hoá Học & pH', goal: 'cân bằng hoá học', subject: 'chemistry' },
    { label: 'Este & Lipit', goal: 'este', subject: 'chemistry' },
    { label: 'Quy Luật Di Truyền Mendel', goal: 'di truyền mendel', subject: 'biology' },
    { label: 'Quang Hợp & Hô Hấp', goal: 'quang hợp', subject: 'biology' },
  ];

  const filteredLessons = query.trim()
    ? lessons.filter(
        (l) =>
          l.title_vi?.toLowerCase().includes(query.toLowerCase()) ||
          l.title_en?.toLowerCase().includes(query.toLowerCase()) ||
          l.unit?.toLowerCase().includes(query.toLowerCase())
      )
    : lessons;

  // Group lessons by unit
  const groupedUnits = useMemo(() => {
    const map = new Map<string, any[]>();
    for (const l of filteredLessons) {
      const unitKey = l.unit || 'Chuyên Đề Trọng Tâm';
      if (!map.has(unitKey)) {
        map.set(unitKey, []);
      }
      map.get(unitKey)!.push(l);
    }
    // Sắp xếp bài theo thứ tự sư phạm order
    for (const items of map.values()) {
      items.sort((a, b) => (a.order ?? 999) - (b.order ?? 999));
    }
    return Array.from(map.entries());
  }, [filteredLessons]);

  const totalPages = Math.ceil(total / pageSize);

  return (
    <div className="tab-container animate-fade-in">
      {/* Top Banner & Mode Toggle */}
      <div className="glass-panel" style={{ padding: '24px', marginBottom: '24px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px', marginBottom: '20px' }}>
          <div>
            <h2 style={{ fontSize: '1.5rem', display: 'flex', alignItems: 'center', gap: '10px' }}>
              <Compass style={{ color: '#6366f1' }} />
              <span>Bài Học & Lộ Trình</span>
            </h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.88rem', marginTop: '4px' }}>
              Học theo chuyên đề bài bản hoặc nhập mục tiêu để có lộ trình từng bước từ dễ đến nâng cao.
            </p>
          </div>
          
          {/* Mode Switcher Buttons */}
          <div style={{ display: 'flex', gap: '8px', background: 'rgba(255, 255, 255, 0.04)', padding: '4px', borderRadius: 'var(--radius-md)' }}>
            <button
              className={`btn ${activeTab === 'matrix' ? 'btn-primary' : 'btn-secondary'}`}
              style={{ padding: '8px 16px', fontSize: '0.86rem', display: 'flex', alignItems: 'center', gap: '6px' }}
              onClick={() => setActiveTab('matrix')}
            >
              <Layers size={15} />
              <span>Theo Chuyên Đề</span>
            </button>
            <button
              className={`btn ${activeTab === 'roadmap' ? 'btn-primary' : 'btn-secondary'}`}
              style={{ padding: '8px 16px', fontSize: '0.86rem', display: 'flex', alignItems: 'center', gap: '6px' }}
              onClick={() => {
                setActiveTab('roadmap');
                if (!roadmapData) handleGenerateRoadmap();
              }}
            >
              <GitFork size={15} />
              <span>Lộ Trình Tự Động</span>
            </button>
          </div>
        </div>

        {/* ================= MODE 1: MA TRẬN CHƯƠNG MỤC ================= */}
        {activeTab === 'matrix' && (
          <div className="animate-fade-in">
            {/* Subject Pills */}
            <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '16px' }}>
              {subjectPills.map((pill) => (
                <button
                  key={pill.id}
                  className={`btn ${subject === pill.id ? 'btn-primary' : 'btn-secondary'}`}
                  style={{
                    fontSize: '0.85rem',
                    padding: '6px 14px',
                    borderRadius: 'var(--radius-full)',
                  }}
                  onClick={() => {
                    setSubject(pill.id);
                    setCurrentPage(1);
                  }}
                >
                  {pill.label}
                </button>
              ))}
            </div>

            {/* Filter Bar */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '12px' }}>
              <div style={{ position: 'relative', gridColumn: 'span 2' }}>
                <Search
                  size={18}
                  style={{
                    position: 'absolute',
                    left: '14px',
                    top: '50%',
                    transform: 'translateY(-50%)',
                    color: 'var(--text-muted)',
                  }}
                />
                <input
                  type="text"
                  placeholder="Tìm theo chủ đề, tiêu đề (ví dụ: Tích phân, Mendel, Điện trường, Este...)"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  className="input-field"
                  style={{ paddingLeft: '40px' }}
                />
              </div>

              <select
                value={level}
                onChange={(e) => {
                  setLevel(e.target.value);
                  setCurrentPage(1);
                }}
                className="input-field"
                style={{ cursor: 'pointer' }}
              >
                <option value="">Tất cả cấp học</option>
                <option value="tieu-hoc">Tiểu học (Lớp 1 - 5)</option>
                <option value="thcs">THCS (Lớp 6 - 9)</option>
                <option value="thpt">THPT (Lớp 10 - 12)</option>
                <option value="dai-hoc">Đại học / AP / Olympic</option>
              </select>

              <select
                value={grade}
                onChange={(e) => {
                  setGrade(e.target.value);
                  setCurrentPage(1);
                }}
                className="input-field"
                style={{ cursor: 'pointer' }}
              >
                <option value="">Tất cả khối lớp</option>
                <option value="1">Lớp 1</option>
                <option value="2">Lớp 2</option>
                <option value="3">Lớp 3</option>
                <option value="4">Lớp 4</option>
                <option value="5">Lớp 5</option>
                <option value="6">Lớp 6</option>
                <option value="7">Lớp 7</option>
                <option value="8">Lớp 8</option>
                <option value="9">Lớp 9</option>
                <option value="10">Lớp 10</option>
                <option value="11">Lớp 11</option>
                <option value="12">Lớp 12</option>
              </select>
            </div>
          </div>
        )}

        {/* ================= MODE 2: BỘ SINH LỘ TRÌNH HỌC TỪ GỐC ================= */}
        {activeTab === 'roadmap' && (
          <div className="animate-fade-in">
            <div style={{ marginBottom: '14px' }}>
              <label style={{ fontSize: '0.88rem', fontWeight: 600, color: 'var(--text-secondary)', display: 'block', marginBottom: '8px' }}>
                Bạn muốn học hoặc ôn luyện chủ đề nào?
              </label>
              <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
                <div style={{ position: 'relative', flex: '1 1 320px' }}>
                  <Target
                    size={18}
                    style={{
                      position: 'absolute',
                      left: '14px',
                      top: '50%',
                      transform: 'translateY(-50%)',
                      color: '#a855f7',
                    }}
                  />
                  <input
                    type="text"
                    value={goalQuery}
                    onChange={(e) => setGoalQuery(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleGenerateRoadmap()}
                    placeholder="VD: tích phân, đạo hàm, định luật newton, este, di truyền..."
                    className="input-field"
                    style={{ paddingLeft: '42px', fontSize: '0.95rem' }}
                  />
                </div>

                <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                  <select
                    value={maxLessons}
                    onChange={(e) => setMaxLessons(Number(e.target.value))}
                    className="input-field"
                    style={{ width: '130px', cursor: 'pointer', fontSize: '0.85rem' }}
                    title="Số bài học tối đa"
                  >
                    <option value={10}>Tối đa 10 bài</option>
                    <option value={15}>Tối đa 15 bài</option>
                    <option value={25}>Tối đa 25 bài</option>
                    <option value={40}>Tối đa 40 bài</option>
                  </select>

                  <select
                    value={sessionMinutes}
                    onChange={(e) => setSessionMinutes(Number(e.target.value))}
                    className="input-field"
                    style={{ width: '130px', cursor: 'pointer', fontSize: '0.85rem' }}
                    title="Thời lượng mỗi buổi học"
                  >
                    <option value={45}>45 phút / buổi</option>
                    <option value={60}>60 phút / buổi</option>
                    <option value={90}>90 phút / buổi</option>
                  </select>

                  <button
                    className="btn btn-primary"
                    style={{ padding: '10px 20px', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '8px' }}
                    onClick={() => handleGenerateRoadmap()}
                    disabled={roadmapLoading}
                  >
                    <Sparkles size={16} />
                    <span>{roadmapLoading ? 'Đang tạo lộ trình...' : 'Tạo Lộ Trình'}</span>
                  </button>
                </div>
              </div>
            </div>

            {/* Popular Goals */}
            <div>
              <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', marginBottom: '6px' }}>
                Mục tiêu phổ biến gợi ý nhanh:
              </div>
              <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                {popularGoals.map((item, idx) => (
                  <button
                    key={idx}
                    className="btn btn-secondary"
                    style={{
                      fontSize: '0.78rem',
                      padding: '4px 10px',
                      borderRadius: 'var(--radius-full)',
                      background: goalQuery.toLowerCase() === item.goal.toLowerCase() ? 'rgba(99, 102, 241, 0.25)' : undefined,
                      borderColor: goalQuery.toLowerCase() === item.goal.toLowerCase() ? '#6366f1' : undefined,
                    }}
                    onClick={() => {
                      setGoalQuery(item.goal);
                      handleGenerateRoadmap(item.goal);
                    }}
                  >
                    <span>{item.label}</span>
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>

      {/* ================= BODY RENDERING ================= */}

      {/* VIEW 1: MATRIX OF CURRICULUM */}
      {activeTab === 'matrix' && (
        <>
          {loading ? (
            <div
              style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))',
                gap: '20px',
              }}
            >
              {Array.from({ length: 6 }).map((_, i) => (
                <div key={i} className="glass-card" style={{ height: '180px', opacity: 0.5, animation: 'pulse 1.5s infinite' }} />
              ))}
            </div>
          ) : filteredLessons.length === 0 ? (
            <div className="glass-panel" style={{ padding: '60px 20px', textAlign: 'center' }}>
              <BookOpen size={48} style={{ color: 'var(--text-muted)', margin: '0 auto 16px' }} />
              <h3 style={{ fontSize: '1.2rem', marginBottom: '8px' }}>Không tìm thấy bài học nào phù hợp</h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
                Hãy thử tìm bằng từ khoá khác hoặc điều chỉnh bộ lọc môn học / khối lớp.
              </p>
            </div>
          ) : (
            <div id="curriculum-grid" style={{ display: 'flex', flexDirection: 'column', gap: '28px' }}>
              {groupedUnits.map(([unitTitle, unitLessons]) => (
                <div key={unitTitle} className="glass-panel" style={{ padding: '20px 24px' }}>
                  {/* Unit Section Header */}
                  <div
                    style={{
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                      borderBottom: '1px solid var(--border-subtle)',
                      paddingBottom: '12px',
                      marginBottom: '16px',
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                      <Layers size={18} color="#0284c7" />
                      <h3 style={{ fontSize: '1.15rem', fontWeight: 700, color: 'var(--text-primary)' }}>
                        {unitTitle}
                      </h3>
                    </div>
                    <span className="badge badge-indigo" style={{ fontSize: '0.78rem' }}>
                      {unitLessons.length} bài học tuần tự
                    </span>
                  </div>

                  {/* Lessons Grid in this Unit */}
                  <div
                    style={{
                      display: 'grid',
                      gridTemplateColumns: 'repeat(auto-fill, minmax(310px, 1fr))',
                      gap: '16px',
                    }}
                  >
                    {unitLessons.map((lesson) => (
                      <div
                        key={lesson.id}
                        className="glass-card"
                        style={{
                          display: 'flex',
                          flexDirection: 'column',
                          justifyContent: 'space-between',
                          cursor: 'pointer',
                          position: 'relative',
                          border: '1px solid var(--border-subtle)',
                          transition: 'transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease',
                        }}
                        onClick={() => setSelectedLessonId(lesson.id)}
                      >
                        <div>
                          {/* Top Badges */}
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
                            <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
                              <span
                                className={`badge ${
                                  lesson.subject === 'math'
                                    ? 'badge-indigo'
                                    : lesson.subject === 'physics'
                                    ? 'badge-cyan'
                                    : lesson.subject === 'chemistry'
                                    ? 'badge-emerald'
                                    : 'badge-rose'
                                }`}
                                style={{ fontSize: '0.72rem' }}
                              >
                                {lesson.subject === 'math'
                                  ? 'Toán'
                                  : lesson.subject === 'physics'
                                  ? 'Vật Lí'
                                  : lesson.subject === 'chemistry'
                                  ? 'Hoá Học'
                                  : lesson.subject === 'biology'
                                  ? 'Sinh Học'
                                  : lesson.subject}
                              </span>

                              {lesson.order != null && (
                                <span className="badge badge-amber" style={{ fontSize: '0.7rem' }}>
                                  Bài {lesson.order}
                                </span>
                              )}
                            </div>

                            {lesson.grades && lesson.grades.length > 0 && (
                              <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>
                                Lớp {lesson.grades.join(', ')}
                              </span>
                            )}
                          </div>

                          {/* Title */}
                          <h4
                            style={{
                              fontSize: '1rem',
                              fontWeight: 700,
                              lineHeight: 1.4,
                              marginBottom: '6px',
                              color: 'var(--text-primary)',
                            }}
                          >
                            {lesson.title_vi}
                          </h4>

                          {lesson.title_en && (
                            <div style={{ fontSize: '0.78rem', color: 'var(--text-secondary)', fontStyle: 'italic', marginBottom: '12px' }}>
                              {lesson.title_en}
                            </div>
                          )}

                          {/* Prerequisites Indicator */}
                          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.75rem', marginBottom: '12px' }}>
                            <GitFork size={12} color={lesson.prerequisites?.length ? '#d97706' : '#16a34a'} />
                            {lesson.prerequisites?.length > 0 ? (
                              <span style={{ color: '#b45309', fontWeight: 600 }}>
                                Cần {lesson.prerequisites.length} bài tiên quyết
                              </span>
                            ) : (
                              <span style={{ color: '#15803d', fontWeight: 600 }}>Bài học nền tảng gốc rễ</span>
                            )}
                          </div>
                        </div>

                        {/* Bottom Actions */}
                        <div
                          style={{
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'space-between',
                            paddingTop: '10px',
                            borderTop: '1px solid var(--border-subtle)',
                          }}
                        >
                          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                            <Clock size={12} />
                            {lesson.duration_minutes || 45}p
                          </span>

                          <div style={{ display: 'flex', gap: '6px' }}>
                            <button
                              className="btn btn-secondary"
                              style={{ padding: '4px 10px', fontSize: '0.75rem', color: '#a5b4fc' }}
                              onClick={(e) => {
                                e.stopPropagation();
                                setSelectedLessonId(lesson.id);
                              }}
                            >
                              <Eye size={13} />
                              <span>Học</span>
                            </button>

                            <button
                              className="btn btn-secondary"
                              style={{ padding: '4px 8px', fontSize: '0.75rem', color: '#c084fc' }}
                              title="Dựng lộ trình học xuất phát từ bài này"
                              onClick={(e) => {
                                e.stopPropagation();
                                setGoalQuery(lesson.id);
                                handleGenerateRoadmap(lesson.id);
                              }}
                            >
                              <GitFork size={13} />
                              <span>Lộ Trình</span>
                            </button>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              ))}

              {/* Pagination */}
              <Pagination
                currentPage={currentPage}
                totalPages={totalPages}
                onPageChange={(page) => loadLessons(page)}
                totalItems={total}
                pageSize={pageSize}
              />
            </div>
          )}
        </>
      )}

      {/* VIEW 2: ROADMAP GENERATOR (DAG) */}
      {activeTab === 'roadmap' && (
        <div className="animate-fade-in">
          {roadmapLoading ? (
            <div className="glass-panel" style={{ padding: '50px 20px', textAlign: 'center' }}>
              <div style={{ display: 'inline-block', marginBottom: '16px' }}>
                <Sparkles size={36} className="animate-spin" color="#6366f1" />
              </div>
              <h3 style={{ fontSize: '1.2rem', marginBottom: '8px' }}>
                Đang Chuẩn Bị Lộ Trình Học Cho Bạn...
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.88rem', maxWidth: '520px', margin: '0 auto' }}>
                Hệ thống đang lựa chọn các bài học nền tảng và sắp xếp thứ tự dễ tiếp thu nhất cho chủ đề &ldquo;{goalQuery}&rdquo;.
              </p>
            </div>
          ) : roadmapError ? (
            <div className="glass-panel" style={{ padding: '40px 20px', textAlign: 'center', borderColor: 'rgba(239, 68, 68, 0.4)' }}>
              <p style={{ color: '#f87171', marginBottom: '12px' }}>{roadmapError}</p>
              <button className="btn btn-primary" onClick={() => handleGenerateRoadmap('tích phân')}>
                Thử lại với mục tiêu mẫu: &ldquo;Tích phân&rdquo;
              </button>
            </div>
          ) : roadmapData ? (
            <div>
              {/* Summary Dashboard Header */}
              <div
                className="glass-panel"
                style={{
                  padding: '20px 24px',
                  marginBottom: '20px',
                  background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(168, 85, 247, 0.08))',
                  border: '1px solid rgba(99, 102, 241, 0.3)',
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px', marginBottom: '16px' }}>
                  <div>
                    <span className="badge badge-indigo" style={{ marginBottom: '6px' }}>
                      Lộ Trình Học Từng Bước
                    </span>
                    <h3 style={{ fontSize: '1.3rem', fontWeight: 800 }}>
                      Mục Tiêu: &ldquo;{roadmapData.goal}&rdquo;
                    </h3>
                  </div>

                  <div style={{ display: 'flex', gap: '8px' }}>
                    <button
                      className={`btn ${roadmapViewType === 'milestones' ? 'btn-primary' : 'btn-secondary'}`}
                      style={{ fontSize: '0.8rem', padding: '6px 14px' }}
                      onClick={() => setRoadmapViewType('milestones')}
                    >
                      <Layers size={14} style={{ marginRight: '4px' }} />
                      Chặng Học ({roadmapData.milestones.length})
                    </button>
                    <button
                      className={`btn ${roadmapViewType === 'sessions' ? 'btn-primary' : 'btn-secondary'}`}
                      style={{ fontSize: '0.8rem', padding: '6px 14px' }}
                      onClick={() => setRoadmapViewType('sessions')}
                    >
                      <Calendar size={14} style={{ marginRight: '4px' }} />
                      Buổi Học ({roadmapData.sessions.length})
                    </button>
                  </div>
                </div>

                {/* KPI Metrics */}
                <div
                  style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))',
                    gap: '12px',
                    marginBottom: '16px',
                  }}
                >
                  <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border-subtle)', padding: '12px', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                    <div style={{ fontSize: '1.4rem', fontWeight: 800, color: '#0369a1' }}>
                      ~{roadmapData.total_hours ?? (roadmapData.total_minutes / 60).toFixed(1)}h
                    </div>
                    <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>Thời lượng học</div>
                  </div>

                  <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border-subtle)', padding: '12px', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                    <div style={{ fontSize: '1.4rem', fontWeight: 800, color: '#047857' }}>
                      {roadmapData.lesson_count || roadmapData.milestones.length}
                    </div>
                    <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>Bài học lý thuyết</div>
                  </div>

                  <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border-subtle)', padding: '12px', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                    <div style={{ fontSize: '1.4rem', fontWeight: 800, color: '#b45309' }}>
                      {roadmapData.practice_count}
                    </div>
                    <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>Bài tập rèn luyện</div>
                  </div>

                  <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border-subtle)', padding: '12px', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                    <div style={{ fontSize: '1.4rem', fontWeight: 800, color: '#7e22ce' }}>
                      {roadmapData.sessions.length}
                    </div>
                    <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>Buổi học phân bổ</div>
                  </div>
                </div>

                {/* Explanations from engine */}
                {roadmapData.warnings && roadmapData.warnings.length > 0 && (
                  <div
                    style={{
                      padding: '10px 14px',
                      borderRadius: 'var(--radius-sm)',
                      background: 'rgba(0, 0, 0, 0.3)',
                      borderLeft: '3px solid #6366f1',
                      fontSize: '0.84rem',
                      lineHeight: 1.5,
                      color: 'var(--text-secondary)',
                    }}
                  >
                    {roadmapData.warnings.map((w, idx) => (
                      <div key={idx} style={{ marginBottom: idx < roadmapData.warnings.length - 1 ? '4px' : 0 }}>
                        💡 {w}
                      </div>
                    ))}
                  </div>
                )}
              </div>

              {/* VIEW SUB-MODE: MILESTONES TIMELINE */}
              {roadmapViewType === 'milestones' && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                  {roadmapData.milestones.map((milestone) => {
                    const isTarget = milestone.lesson.reason?.includes('bài đích');
                    const isRoot = milestone.prerequisites_met.length === 0 && milestone.order <= 2;
                    return (
                      <div
                        key={milestone.lesson.id}
                        className="glass-card"
                        style={{
                          display: 'flex',
                          gap: '18px',
                          padding: '18px 22px',
                          border: isTarget
                            ? '1px solid rgba(236, 72, 153, 0.5)'
                            : isRoot
                            ? '1px solid rgba(74, 222, 128, 0.4)'
                            : '1px solid rgba(255, 255, 255, 0.08)',
                          background: isTarget
                            ? 'rgba(236, 72, 153, 0.04)'
                            : isRoot
                            ? 'rgba(74, 222, 128, 0.03)'
                            : undefined,
                        }}
                      >
                        {/* Step Order Badge */}
                        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                          <div
                            style={{
                              width: '36px',
                              height: '36px',
                              borderRadius: '50%',
                              background: isTarget
                                ? '#ec4899'
                                : isRoot
                                ? '#22c55e'
                                : '#6366f1',
                              color: '#fff',
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              fontWeight: 800,
                              fontSize: '0.95rem',
                            }}
                          >
                            {milestone.order}
                          </div>
                          {milestone.order < roadmapData.milestones.length && (
                            <div style={{ width: '2px', flex: 1, background: 'rgba(255, 255, 255, 0.1)', marginTop: '8px' }} />
                          )}
                        </div>

                        {/* Step Details */}
                        <div style={{ flex: 1 }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', marginBottom: '8px' }}>
                            <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
                              <span
                                className={`badge ${
                                  isTarget
                                    ? 'badge-rose'
                                    : isRoot
                                    ? 'badge-emerald'
                                    : 'badge-indigo'
                                }`}
                                style={{ fontSize: '0.72rem' }}
                              >
                                {isTarget
                                  ? '🎯 Hoàn thành mục tiêu'
                                  : isRoot
                                  ? '🌱 Bắt đầu từ đây (Nền tảng)'
                                  : '🔗 Kiến thức bổ trợ'}
                              </span>

                              {milestone.unit && (
                                <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                                  • {milestone.unit}
                                </span>
                              )}
                            </div>

                            <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                              <Clock size={12} />
                              {milestone.lesson.minutes || 45} phút lý thuyết
                            </span>
                          </div>

                          <h4 style={{ fontSize: '1.15rem', fontWeight: 700, marginBottom: '6px', color: 'var(--text-primary)' }}>
                            {milestone.lesson.title}
                          </h4>

                          <p style={{ fontSize: '0.84rem', color: 'var(--text-secondary)', marginBottom: '12px' }}>
                            <strong>Mục đích học:</strong> {milestone.lesson.reason}
                          </p>

                          {/* Attached Practice Problems */}
                          {milestone.practice && milestone.practice.length > 0 && (
                            <div
                              style={{
                                padding: '10px 12px',
                                borderRadius: 'var(--radius-sm)',
                                background: 'var(--bg-card)',
                                border: '1px solid var(--border-subtle)',
                                marginBottom: '12px',
                              }}
                            >
                              <div style={{ fontSize: '0.78rem', fontWeight: 600, color: '#b45309', marginBottom: '6px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                                <CheckCircle2 size={13} />
                                <span>Bài tập rèn luyện ngay ({milestone.practice.length} câu):</span>
                              </div>
                              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                                {milestone.practice.map((prob) => (
                                  <div
                                    key={prob.id}
                                    style={{
                                      fontSize: '0.8rem',
                                      color: 'var(--text-secondary)',
                                      display: 'flex',
                                      alignItems: 'center',
                                      gap: '6px',
                                    }}
                                  >
                                    <ChevronRight size={12} color="var(--text-muted)" />
                                    <span style={{ flex: 1 }}>{prob.title}</span>
                                    <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>
                                      (~{prob.minutes || 5}p)
                                    </span>
                                  </div>
                                ))}
                              </div>
                            </div>
                          )}

                          {/* Action Buttons */}
                          <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                            <button
                              className="btn btn-primary"
                              style={{ fontSize: '0.82rem', padding: '6px 14px' }}
                              onClick={() => setSelectedLessonId(milestone.lesson.id)}
                            >
                              <Eye size={14} style={{ marginRight: '6px' }} />
                              <span>Học Bài Này</span>
                            </button>

                            <a
                              href={`https://www.youtube.com/results?search_query=${encodeURIComponent(`bài giảng ${milestone.lesson.title}`)}`}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="btn btn-secondary"
                              style={{
                                fontSize: '0.82rem',
                                padding: '6px 12px',
                                textDecoration: 'none',
                                color: '#ef4444',
                                borderColor: 'rgba(239, 68, 68, 0.3)',
                                background: 'rgba(239, 68, 68, 0.05)',
                              }}
                              title="Xem video giảng bài này trên YouTube"
                            >
                              <Video size={14} style={{ marginRight: '6px' }} />
                              <span>Xem Video Bài Học</span>
                            </a>
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}

              {/* VIEW SUB-MODE: STUDY SESSIONS */}
              {roadmapViewType === 'sessions' && (
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '16px' }}>
                  {roadmapData.sessions.map((session) => (
                    <div
                      key={session.index}
                      className="glass-card"
                      style={{
                        padding: '18px 20px',
                        display: 'flex',
                        flexDirection: 'column',
                        justifyContent: 'space-between',
                      }}
                    >
                      <div>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                          <span className="badge badge-indigo" style={{ fontSize: '0.82rem', fontWeight: 700 }}>
                            Buổi {session.index}
                          </span>
                          <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                            <Clock size={12} />
                            {session.minutes} phút
                          </span>
                        </div>

                        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginBottom: '16px' }}>
                          {session.items.map((item, itemIdx) => (
                            <div
                              key={itemIdx}
                              style={{
                                padding: '8px 10px',
                                borderRadius: 'var(--radius-sm)',
                                background: item.kind === 'lesson' ? 'rgba(99, 102, 241, 0.08)' : 'rgba(234, 179, 8, 0.06)',
                                border: `1px solid ${item.kind === 'lesson' ? 'rgba(99, 102, 241, 0.2)' : 'rgba(234, 179, 8, 0.2)'}`,
                                fontSize: '0.82rem',
                              }}
                            >
                              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2px' }}>
                                <span
                                  style={{
                                    fontWeight: 600,
                                    color: item.kind === 'lesson' ? '#a5b4fc' : '#fde047',
                                    fontSize: '0.72rem',
                                  }}
                                >
                                  {item.kind === 'lesson' ? '📖 BÀI HỌC' : '✏️ BÀI TẬP'}
                                </span>
                                <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>
                                  {item.minutes}p
                                </span>
                              </div>
                              <div style={{ color: 'var(--text-primary)', lineHeight: 1.4 }}>
                                {item.title}
                              </div>
                            </div>
                          ))}
                        </div>
                      </div>

                      <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', textAlign: 'right' }}>
                        Hoàn thành trong {session.minutes} phút
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          ) : null}
        </div>
      )}

      {/* Lesson Detail & AI Tutor Modal */}
      {selectedLessonId && (
        <LessonModal
          lessonId={selectedLessonId}
          onClose={() => setSelectedLessonId(null)}
          onSelectLesson={(newId) => setSelectedLessonId(newId)}
        />
      )}
    </div>
  );
};
