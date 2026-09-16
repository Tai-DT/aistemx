import { useState, useEffect, useMemo, useRef, type FC } from 'react';
import { createPortal } from 'react-dom';
import { api } from '../../services/api';
import { MathView } from '../../components/MathView';
import { InteractiveFormulaDemo } from '../../components/InteractiveFormulaDemo';
import {
  X,
  BookOpen,
  Target,
  Sparkles,
  Bot,
  GitFork,
  ArrowRight,
  Clock,
  AlertTriangle,
  CheckCircle2,
  FileText,
  Lightbulb,
  FlaskConical,
  Video,
  ExternalLink,
  PlayCircle,
} from 'lucide-react';

interface LessonModalProps {
  lessonId: string;
  onClose: () => void;
  onSelectFormula?: (fid: string) => void;
  onSelectLesson?: (lid: string) => void;
}

type LessonModalTab = 'simulation' | 'theory' | 'exercises' | 'video' | 'ai';

export const LessonModal: FC<LessonModalProps> = ({ lessonId, onClose, onSelectFormula, onSelectLesson }) => {
  const [activeLessonId, setActiveLessonId] = useState(lessonId);
  const [lesson, setLesson] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [selectedFormulaIndex, setSelectedFormulaIndex] = useState(0);
  const [aiExplanation, setAiExplanation] = useState<string | null>(null);
  const [aiLoading, setAiLoading] = useState(false);
  const [activeTab, setActiveTab] = useState<LessonModalTab>('simulation');
  const [activeEmbeddedVideo, setActiveEmbeddedVideo] = useState<{ id: string; title: string; author: string; badge: string; desc: string } | null>(null);

  const scrollContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    setActiveLessonId(lessonId);
    setSelectedFormulaIndex(0);
    setActiveTab('simulation');
    setActiveEmbeddedVideo(null);
  }, [lessonId]);

  useEffect(() => {
    let isCancelled = false;
    const fetchDetail = async () => {
      setLoading(true);
      setAiExplanation(null);
      try {
        const data = await api.getLessonDetail(activeLessonId);
        if (!isCancelled) {
          setLesson(data);
          // Nếu bài này không có công thức hay mô phỏng, tự chuyển sang tab lý thuyết
          if (!data.formula_details || data.formula_details.length === 0) {
            setActiveTab('theory');
          } else {
            setActiveTab('simulation');
          }
        }
      } catch (e) {
        console.error('Lỗi nạp bài học:', e);
      } finally {
        if (!isCancelled) {
          setLoading(false);
        }
      }
    };
    fetchDetail();
    return () => {
      isCancelled = true;
    };
  }, [activeLessonId]);

  // Cuộn lên đỉnh mỗi khi chuyển tab hoặc đổi bài
  useEffect(() => {
    if (scrollContainerRef.current) {
      scrollContainerRef.current.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }, [activeTab, activeLessonId]);

  const handleSwitchLesson = (newId: string) => {
    setActiveLessonId(newId);
    if (onSelectLesson) onSelectLesson(newId);
  };

  const isElementary = Boolean(
    lesson?.level === 'tieu-hoc' ||
    lesson?.id?.includes('tieu-hoc') ||
    (Array.isArray(lesson?.grades) && lesson.grades.some((g: number) => g <= 5)) ||
    (Array.isArray(lesson?.tags) && lesson.tags.some((t: string) => ['lop1', 'lop2', 'lop3', 'lop4', 'lop5', 'tieu-hoc'].includes(t.toLowerCase())))
  );

  const handleAskAI = async () => {
    if (!lesson) return;
    setAiLoading(true);
    try {
      const audience = isElementary ? 'Học sinh Tiểu học Lớp 5 (10 tuổi)' : 'học sinh THCS & THPT';
      const examplesText = lesson.worked_examples && lesson.worked_examples.length > 0
        ? lesson.worked_examples.map((ex: any, i: number) => `Bài tập ${i + 1}: ${ex.problem}\nLời giải: ${ex.solution}`).join('\n\n')
        : '';
      const fullContext = [
        lesson.title_vi,
        lesson.content,
        examplesText ? `BÀI TẬP VÍ DỤ TRONG BÀI:\n${examplesText}` : '',
        lesson.key_concepts?.map((c: any) => `${c.term_vi}: ${c.definition}`).join('; '),
      ].filter(Boolean).join('\n\n');

      const res = await api.explainWithAI(
        lesson.title_vi,
        fullContext,
        audience
      );
      setAiExplanation(res.ai_explanation);
    } catch (e) {
      console.error('Lỗi gọi gia sư AI:', e);
    } finally {
      setAiLoading(false);
    }
  };

  useEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = 'hidden';
    return () => {
      document.body.style.overflow = originalStyle;
    };
  }, []);

  const hasSimulations = Boolean(lesson?.formula_details && lesson.formula_details.length > 0);
  const hasExercises = Boolean(lesson?.worked_examples && lesson.worked_examples.length > 0);

  // Danh sách video bài giảng chất lượng cao được nhúng xem trực tiếp
  const curatedVideos = useMemo(() => {
    if (!lesson) return [];
    const title = (lesson.title_vi || '').toLowerCase();
    const topic = (lesson.unit || '').toLowerCase();
    const subj = lesson.subject || 'math';
    const list: Array<{ id: string; title: string; author: string; badge: string; desc: string }> = [];

    // 1. TOÁN HỌC
    if (subj === 'math') {
      if (title.includes('tích phân') || topic.includes('tích phân') || title.includes('đạo hàm')) {
        list.push({
          id: 'WUvTyaaNkzM',
          title: 'Essence of Calculus: Bản chất đạo hàm & tích phân trực quan',
          author: '3Blue1Brown Vietsub',
          badge: 'Đồ họa 3D kinh điển',
          desc: 'Trực quan hóa hình học từng bước tại sao vi phân và tích phân lại gắn liền mật thiết.',
        });
        list.push({
          id: 'rfG8ce4nNh0',
          title: 'Integration and the Fundamental Theorem of Calculus: Tích phân hình học',
          author: '3Blue1Brown',
          badge: 'Bản chất toán học',
          desc: 'Hiểu cội nguồn của tích phân từ phép chia nhỏ vô hạn các dải diện tích Riemann.',
        });
      } else if (title.includes('ma trận') || title.includes('vector') || title.includes('hệ phương trình')) {
        list.push({
          id: 'fNk_zzaMoSs',
          title: 'Essence of Linear Algebra: Bản chất Đại số tuyến tính & Vector',
          author: '3Blue1Brown',
          badge: 'Đồ họa không gian',
          desc: 'Quan sát sự biến đổi không gian, phép quay và phép co giãn của ma trận.',
        });
      } else if (title.includes('hình học') || title.includes('pytago') || isElementary) {
        list.push({
          id: 'YompsDlEdtc',
          title: 'Chứng minh định lý Pytago & Hình học phẳng trực quan',
          author: 'Math Antics',
          badge: 'Trực quan sinh động',
          desc: 'Minh họa ghép hình và ý nghĩa thực tế của diện tích hình phẳng.',
        });
      } else {
        list.push({
          id: 'WUvTyaaNkzM',
          title: 'Tư duy toán học trực quan: Bản chất hình học & công thức',
          author: '3Blue1Brown',
          badge: 'Khoa học trực quan',
          desc: 'Học cách tư duy hình học hóa mọi bài toán để hiểu sâu và nhớ lâu.',
        });
      }
    }

    // 2. VẬT LÝ
    if (subj === 'physics') {
      if (title.includes('newton') || title.includes('động lực') || title.includes('chuyển động')) {
        list.push({
          id: 'kKKM8Y-u7ds',
          title: '3 Định luật Newton về chuyển động & Bản chất của Lực',
          author: 'CrashCourse Physics',
          badge: 'Thực nghiệm & Hoạt hình',
          desc: 'Quán tính, F = ma và Định luật III tương tác lực với ví dụ đời thực.',
        });
        list.push({
          id: 'bHIhgxav9LY',
          title: 'Thí nghiệm trọng lực & Thả rơi tự do trong buồng chân không NASA',
          author: 'Veritasium & BBC',
          badge: 'Thí nghiệm thực tế',
          desc: 'Quả lông vũ và quả cầu bi rơi cùng một vận tốc trong môi trường không có không khí.',
        });
      } else if (title.includes('sóng') || title.includes('dao động') || title.includes('con lắc')) {
        list.push({
          id: 'T2bN_Y8W_tY',
          title: 'Sóng cơ, Giao thoa sóng và Dao động điều hòa trực quan',
          author: 'CrashCourse Physics',
          badge: 'Mô phỏng sóng',
          desc: 'Minh họa bước sóng, tần số và hiện tượng cộng hưởng thực tế.',
        });
      } else {
        list.push({
          id: 'ZM8ECpB9650',
          title: 'Bản chất Điện trường, Hiệu điện thế & Định luật Ohm',
          author: 'CrashCourse Physics',
          badge: 'Vật lý căn bản',
          desc: 'Dòng chảy electron và các mạch điện cơ bản được mô phỏng trực quan.',
        });
      }
    }

    // 3. HÓA HỌC
    if (subj === 'chemistry') {
      if (title.includes('cân bằng') || title.includes('tốc độ')) {
        list.push({
          id: 'vERIUmgpD3Y',
          title: 'Cân bằng hóa học & Nguyên lý dịch chuyển Le Chatelier',
          author: 'CrashCourse Chemistry',
          badge: 'Mô phỏng phân tử',
          desc: 'Cách áp suất, nhiệt độ và nồng độ làm dịch chuyển cân bằng phản ứng thuận nghịch.',
        });
      } else if (title.includes('hữu cơ') || title.includes('este') || title.includes('lipit')) {
        list.push({
          id: 'mAjrnZ-znkY',
          title: 'Hóa học hữu cơ: Cấu tạo phân tử Carbon & Nhóm chức',
          author: 'Khan Academy Organic',
          badge: 'Cấu trúc 3D',
          desc: 'Cơ chế phản ứng este hóa và chuỗi biến hóa hợp chất hữu cơ.',
        });
      } else {
        list.push({
          id: 'FSyAehMdpyI',
          title: 'Bảng tuần hoàn các nguyên tố hóa học & Cấu hình electron',
          author: 'CrashCourse Chemistry',
          badge: 'Mô hình nguyên tử',
          desc: 'Quy luật biến thiên bán kính, độ âm điện và tính chất hóa học các nhóm A.',
        });
      }
    }

    // 4. SINH HỌC
    if (subj === 'biology') {
      if (title.includes('mendel') || title.includes('di truyền') || title.includes('lai')) {
        list.push({
          id: 'i-0rSv6oxSY',
          title: 'Monohybrids and the Punnett Square: Lai một cặp tính trạng & Khung Punnett',
          author: 'Amoeba Sisters',
          badge: 'Trực quan di truyền',
          desc: 'Phép lai một cặp tính trạng của Menđen với chuột lang, alen trội và lặn.',
        });
        list.push({
          id: 'Mehz7tCxjSE',
          title: 'How Mendel pea plants helped us understand genetics (Thí nghiệm Đậu Hà Lan)',
          author: 'TED-Ed Khoa Học',
          badge: 'Hoạt hình TED-Ed',
          desc: 'Gregor Mendel và lịch sử khám phá các quy luật di truyền nền tảng của nhân loại.',
        });
        list.push({
          id: '8m6hHRlKwxY',
          title: 'DNA, Chromosomes, Genes, and Traits: Bản chất Gen và Di truyền',
          author: 'Amoeba Sisters',
          badge: 'Hoạt hình trực quan',
          desc: 'Cơ chế ADN mang thông tin di truyền và hình thành tính trạng cơ thể.',
        });
      } else if (title.includes('quang hợp') || title.includes('hô hấp') || title.includes('thực vật')) {
        list.push({
          id: 'g78utcLQrJ4',
          title: 'Quang hợp ở thực vật: Pha sáng & Chu trình Calvin',
          author: 'Khan Academy Biology',
          badge: 'Sinh học phân tử',
          desc: 'Lục lạp biến đổi quang năng ánh sáng mặt trời thành năng lượng hóa học glucose.',
        });
        list.push({
          id: 'sQK3Yr4Sc_k',
          title: 'Photosynthesis: Crash Course Biology',
          author: 'CrashCourse Biology',
          badge: 'Khoa học trực quan',
          desc: 'Chi tiết chuỗi vận chuyển electron quang hợp và chuyển hóa năng lượng ATP.',
        });
      } else {
        list.push({
          id: 'L0k-enzoeOM',
          title: 'Quá trình phân bào: Nguyên phân & Giảm phân trực quan',
          author: 'CrashCourse Biology',
          badge: 'Sinh học tế bào',
          desc: 'Quan sát các nhiễm sắc thể co xoắn, xếp hàng ở mặt phẳng xích đạo và phân li.',
        });
        list.push({
          id: '8m6hHRlKwxY',
          title: 'DNA, Nhiễm sắc thể & Cấu trúc di truyền học',
          author: 'Amoeba Sisters',
          badge: 'Khoa học cơ bản',
          desc: 'Mô tả trực quan mối liên hệ giữa ADN, gen và nhiễm sắc thể trong nhân tế bào.',
        });
      }
    }

    // Mặc định luôn có ít nhất 1 video trực quan
    if (list.length === 0) {
      list.push({
        id: 'WUvTyaaNkzM',
        title: `Bài giảng trực quan chủ đề: ${lesson.title_vi}`,
        author: 'AISTEM Educational Network',
        badge: 'Bài giảng chuẩn',
        desc: 'Mô phỏng hiện tượng khoa học và phân tích chi tiết ứng dụng thực tế.',
      });
    }

    return list;
  }, [lesson, isElementary]);

  // Video đang được chọn phát
  const currentVideo = activeEmbeddedVideo || curatedVideos[0];

  return createPortal(
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        width: '100vw',
        height: '100vh',
        zIndex: 9999,
        background: 'rgba(15, 23, 42, 0.65)',
        backdropFilter: 'blur(8px)',
        WebkitBackdropFilter: 'blur(8px)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '16px',
      }}
      onClick={onClose}
    >
      <div
        ref={scrollContainerRef}
        className="glass-panel animate-scale-up"
        style={{
          width: '100%',
          maxWidth: '960px',
          maxHeight: '94vh',
          overflowY: 'auto',
          padding: '24px 28px',
          borderRadius: 'var(--radius-lg)',
          background: '#ffffff',
          border: '1px solid #bae6fd',
          boxShadow: '0 20px 45px -10px rgba(15, 23, 42, 0.2)',
          position: 'relative',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Nút đóng nổi góc phải */}
        <button
          className="btn btn-secondary"
          style={{
            position: 'absolute',
            right: '18px',
            top: '18px',
            padding: '6px',
            borderRadius: '50%',
            zIndex: 10,
            background: '#f8fafc',
          }}
          onClick={onClose}
          title="Đóng bài học"
        >
          <X size={18} />
        </button>

        {loading ? (
          <div style={{ textAlign: 'center', padding: '70px 0', color: 'var(--text-muted)' }}>
            <div style={{ fontSize: '1.8rem', marginBottom: '12px' }}>🧪</div>
            <p style={{ fontSize: '0.95rem' }}>Đang mở phòng học thí nghiệm trực quan...</p>
          </div>
        ) : lesson ? (
          <div>
            {/* Header thông tin bài học gọn gàng */}
            <div style={{ marginBottom: '16px', paddingRight: '46px' }}>
              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '8px', alignItems: 'center' }}>
                <span className="badge badge-indigo" style={{ fontWeight: 700 }}>
                  {lesson.subject === 'math'
                    ? 'Toán Học'
                    : lesson.subject === 'physics'
                    ? 'Vật Lí'
                    : lesson.subject === 'chemistry'
                    ? 'Hoá Học'
                    : lesson.subject === 'biology'
                    ? 'Sinh Học'
                    : (lesson.subject || '').toUpperCase()}
                </span>
                {lesson.level && <span className="badge badge-emerald">{lesson.level.toUpperCase()}</span>}
                {lesson.grades && lesson.grades.length > 0 && (
                  <span className="badge badge-cyan">Lớp {lesson.grades.join(', ')}</span>
                )}
                {lesson.duration_minutes && (
                  <span
                    className="badge"
                    style={{ background: '#e0f2fe', color: '#0369a1', border: '1px solid #bae6fd' }}
                  >
                    <Clock size={12} style={{ marginRight: '4px' }} />
                    {lesson.duration_minutes} phút
                  </span>
                )}
                {lesson.unit && (
                  <span style={{ fontSize: '0.82rem', color: '#64748b', fontWeight: 600 }}>
                    • {lesson.unit}
                  </span>
                )}
              </div>

              <h2 style={{ fontSize: '1.45rem', fontWeight: 800, lineHeight: 1.3, marginBottom: '4px', color: '#0f172a' }}>
                {lesson.title_vi}
              </h2>
              {lesson.title_en && (
                <div style={{ fontSize: '0.88rem', color: '#64748b', fontStyle: 'italic' }}>
                  {lesson.title_en}
                </div>
              )}
            </div>

            {/* BANNER PHƯƠNG PHÁP SƯ PHẠM LỚP 5 / TIỂU HỌC */}
            {isElementary && (
              <div
                style={{
                  padding: '12px 16px',
                  borderRadius: 'var(--radius-md)',
                  background: 'linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%)',
                  border: '1px solid #86efac',
                  marginBottom: '16px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '12px',
                  boxShadow: '0 2px 6px rgba(22, 101, 52, 0.04)',
                }}
              >
                <div style={{ fontSize: '26px', lineHeight: 1 }}>🌱</div>
                <div>
                  <div style={{ fontWeight: 700, fontSize: '0.9rem', color: '#166534', display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <span>Góc Sư Phạm Lớp 5: Diễn Giải Bằng Trực Quan & Đời Thường</span>
                    <span style={{ background: '#16a34a', color: '#ffffff', fontSize: '0.7rem', padding: '1px 6px', borderRadius: '8px' }}>
                      Chuẩn lứa tuổi 10 tuổi
                    </span>
                  </div>
                  <div style={{ fontSize: '0.82rem', color: '#15803d', marginTop: '2px' }}>
                    Bài học được thiết kế bằng xe đạp, bạn Thỏ, chiếc bánh pizza và các khối hình Lego 1cm³ — không dùng thuật ngữ hay công thức trừu tượng người lớn!
                  </div>
                </div>
              </div>
            )}

            {/* THANH TAB ĐIỀU HƯỚNG TRỰC QUAN NGAY TRÊN ĐẦU */}
            <div
              style={{
                display: 'flex',
                gap: '8px',
                borderBottom: '2px solid #e2e8f0',
                paddingBottom: '8px',
                marginBottom: '20px',
                flexWrap: 'wrap',
              }}
            >
              <button
                className={`btn ${activeTab === 'simulation' ? 'btn-primary' : 'btn-secondary'}`}
                style={{
                  fontSize: '0.86rem',
                  padding: '8px 16px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  borderRadius: 'var(--radius-md)',
                  fontWeight: 600,
                }}
                onClick={() => setActiveTab('simulation')}
              >
                <FlaskConical size={16} />
                <span>Mô Phỏng Trực Quan & Công Thức</span>
                {hasSimulations && (
                  <span
                    style={{
                      background: activeTab === 'simulation' ? 'rgba(255,255,255,0.25)' : '#e0f2fe',
                      color: activeTab === 'simulation' ? '#ffffff' : '#0369a1',
                      padding: '1px 6px',
                      borderRadius: '10px',
                      fontSize: '0.72rem',
                    }}
                  >
                    {lesson.formula_details.length}
                  </span>
                )}
              </button>

              <button
                className={`btn ${activeTab === 'theory' ? 'btn-primary' : 'btn-secondary'}`}
                style={{
                  fontSize: '0.86rem',
                  padding: '8px 16px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  borderRadius: 'var(--radius-md)',
                  fontWeight: 600,
                }}
                onClick={() => setActiveTab('theory')}
              >
                <BookOpen size={16} />
                <span>Bài Giảng & Khái Niệm</span>
              </button>

              <button
                className={`btn ${activeTab === 'exercises' ? 'btn-primary' : 'btn-secondary'}`}
                style={{
                  fontSize: '0.86rem',
                  padding: '8px 16px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  borderRadius: 'var(--radius-md)',
                  fontWeight: 600,
                }}
                onClick={() => setActiveTab('exercises')}
              >
                <Lightbulb size={16} />
                <span>Bài Tập Mẫu Hướng Dẫn</span>
                {hasExercises && (
                  <span
                    style={{
                      background: activeTab === 'exercises' ? 'rgba(255,255,255,0.25)' : '#fef3c7',
                      color: activeTab === 'exercises' ? '#ffffff' : '#b45309',
                      padding: '1px 6px',
                      borderRadius: '10px',
                      fontSize: '0.72rem',
                    }}
                  >
                    {lesson.worked_examples.length}
                  </span>
                )}
              </button>

              <button
                className={`btn ${activeTab === 'video' ? 'btn-primary' : 'btn-secondary'}`}
                style={{
                  fontSize: '0.86rem',
                  padding: '8px 16px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  borderRadius: 'var(--radius-md)',
                  fontWeight: 600,
                  background: activeTab === 'video' ? '#dc2626' : undefined,
                  borderColor: activeTab === 'video' ? '#b91c1c' : undefined,
                }}
                onClick={() => setActiveTab('video')}
              >
                <Video size={16} />
                <span>Video Bài Học</span>
                <span
                  style={{
                    background: activeTab === 'video' ? 'rgba(255,255,255,0.25)' : '#fee2e2',
                    color: activeTab === 'video' ? '#ffffff' : '#b91c1c',
                    padding: '1px 6px',
                    borderRadius: '10px',
                    fontSize: '0.72rem',
                  }}
                >
                  YouTube
                </span>
              </button>

              <button
                className={`btn ${activeTab === 'ai' ? 'btn-primary' : 'btn-secondary'}`}
                style={{
                  fontSize: '0.86rem',
                  padding: '8px 16px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  borderRadius: 'var(--radius-md)',
                  fontWeight: 600,
                  marginLeft: 'auto',
                }}
                onClick={() => setActiveTab('ai')}
              >
                <Bot size={16} />
                <span>Gia Sư AI & Tiên Quyết</span>
              </button>
            </div>

            {/* ================= TAB 1: MÔ PHỎNG TRỰC QUAN & CÔNG THỨC (MỞ NGAY TRƯỚC MẮT) ================= */}
            {activeTab === 'simulation' && (
              <div className="animate-fade-in">
                {lesson.formula_details && lesson.formula_details.length > 0 ? (() => {
                  const activeFormula = lesson.formula_details[selectedFormulaIndex] || lesson.formula_details[0];
                  return (
                    <div>
                      {/* Chọn công thức nếu bài có nhiều hơn 1 công thức */}
                      {lesson.formula_details.length > 1 && (
                        <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '14px', alignItems: 'center' }}>
                          <span style={{ fontSize: '0.82rem', fontWeight: 600, color: '#64748b' }}>
                            Chọn công thức:
                          </span>
                          {lesson.formula_details.map((f: any, idx: number) => (
                            <button
                              key={f.id || idx}
                              className={`btn ${selectedFormulaIndex === idx ? 'btn-primary' : 'btn-secondary'}`}
                              style={{
                                padding: '5px 12px',
                                fontSize: '0.8rem',
                                borderRadius: 'var(--radius-full)',
                              }}
                              onClick={() => setSelectedFormulaIndex(idx)}
                            >
                              <span>#{idx + 1} {f.name_vi || f.name}</span>
                            </button>
                          ))}
                        </div>
                      )}

                      {/* Khung công thức & mô phỏng tương tác */}
                      <div
                        style={{
                          padding: '18px 20px',
                          borderRadius: 'var(--radius-md)',
                          background: '#ffffff',
                          border: '1px solid #bae6fd',
                          boxShadow: '0 2px 8px rgba(2, 132, 199, 0.06)',
                          marginBottom: '20px',
                        }}
                      >
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', marginBottom: '12px' }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <FlaskConical size={20} color="#0284c7" />
                            <span style={{ fontWeight: 800, fontSize: '1.08rem', color: '#0f172a' }}>
                              {activeFormula.name_vi || activeFormula.name}
                            </span>
                          </div>

                          {activeFormula.id && (
                            <span
                              className="badge badge-indigo"
                              style={{ cursor: 'pointer', fontSize: '0.74rem' }}
                              onClick={() => onSelectFormula && onSelectFormula(activeFormula.id)}
                              title="Xem chi tiết công thức trong từ điển"
                            >
                              Mã: {activeFormula.id}
                            </span>
                          )}
                        </div>

                        {/* LaTeX Block hiển thị phương trình cốt lõi */}
                        {activeFormula.latex && (
                          <div
                            style={{
                              padding: '14px',
                              background: '#f8fafc',
                              borderRadius: 'var(--radius-sm)',
                              border: '1px solid #e2e8f0',
                              textAlign: 'center',
                              fontSize: '1.2rem',
                              marginBottom: '16px',
                              overflowX: 'auto',
                            }}
                          >
                            <MathView latex={activeFormula.latex} block />
                          </div>
                        )}

                        {/* Interactive Visual Simulation Component */}
                        <InteractiveFormulaDemo formula={activeFormula} />
                      </div>

                      {/* Tóm tắt nhanh khái niệm liên quan */}
                      {lesson.key_concepts && lesson.key_concepts.length > 0 && (
                        <div
                          style={{
                            padding: '14px 18px',
                            background: '#f0f9ff',
                            border: '1px solid #bae6fd',
                            borderRadius: 'var(--radius-md)',
                          }}
                        >
                          <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#0369a1', marginBottom: '6px' }}>
                            💡 Khái niệm cần nhớ khi tương tác mô phỏng:
                          </div>
                          <div style={{ fontSize: '0.88rem', color: '#0f172a', lineHeight: 1.5 }}>
                            <strong>{lesson.key_concepts[0].term_vi}:</strong>{' '}
                            {lesson.key_concepts[0].definition}
                          </div>
                        </div>
                      )}
                    </div>
                  );
                })() : (
                  <div style={{ textAlign: 'center', padding: '40px 20px', background: '#f8fafc', borderRadius: 'var(--radius-md)', border: '1px dashed #cbd5e1' }}>
                    <BookOpen size={40} color="#94a3b8" style={{ margin: '0 auto 10px' }} />
                    <h4 style={{ fontSize: '1rem', color: '#334155', marginBottom: '6px' }}>
                      Bài học tập trung vào tư duy lý thuyết & phương pháp suy luận
                    </h4>
                    <p style={{ fontSize: '0.86rem', color: '#64748b', marginBottom: '14px' }}>
                      Mời bạn chuyển sang tab "Bài Giảng & Khái Niệm" để xem đầy đủ nội dung chi tiết.
                    </p>
                    <button
                      className="btn btn-primary"
                      style={{ fontSize: '0.84rem' }}
                      onClick={() => setActiveTab('theory')}
                    >
                      Xem Bài Giảng Ngay
                    </button>
                  </div>
                )}
              </div>
            )}

            {/* ================= TAB 2: BÀI GIẢNG & KHÁI NIỆM ================= */}
            {activeTab === 'theory' && (
              <div className="animate-fade-in">
                {/* Mục tiêu năng lực */}
                {lesson.objectives && lesson.objectives.length > 0 && (
                  <div
                    style={{
                      padding: '16px 20px',
                      borderRadius: 'var(--radius-md)',
                      background: '#f8fafc',
                      border: '1px solid #e2e8f0',
                      marginBottom: '20px',
                    }}
                  >
                    <h4 style={{ fontSize: '0.96rem', fontWeight: 700, color: '#0369a1', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <Target size={16} />
                      <span>Mục Tiêu Năng Lực Cần Đạt</span>
                    </h4>
                    <ul style={{ paddingLeft: '20px', display: 'flex', flexDirection: 'column', gap: '6px', fontSize: '0.9rem', margin: 0 }}>
                      {lesson.objectives.map((obj: string, idx: number) => (
                        <li key={idx} style={{ color: '#1e293b', lineHeight: 1.55 }}>
                          {obj}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Khái niệm cốt lõi */}
                {lesson.key_concepts && lesson.key_concepts.length > 0 && (
                  <div style={{ marginBottom: '22px' }}>
                    <h4 style={{ fontSize: '1.02rem', fontWeight: 700, color: '#0f172a', marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <Sparkles size={18} color="#0284c7" />
                      <span>Khái Niệm & Định Luật Cốt Lõi</span>
                    </h4>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                      {lesson.key_concepts.map((concept: any, cIdx: number) => (
                        <div
                          key={cIdx}
                          style={{
                            padding: '12px 16px',
                            borderRadius: 'var(--radius-md)',
                            background: '#ffffff',
                            border: '1px solid #e2e8f0',
                            boxShadow: '0 1px 3px rgba(15, 23, 42, 0.03)',
                          }}
                        >
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
                            <span style={{ fontWeight: 700, fontSize: '0.94rem', color: '#0369a1' }}>
                              {concept.term_vi}
                            </span>
                            {concept.term_en && (
                              <span style={{ fontSize: '0.8rem', color: '#64748b' }}>
                                ({concept.term_en})
                              </span>
                            )}
                          </div>
                          <div style={{ fontSize: '0.9rem', lineHeight: 1.6, color: '#1e293b' }}>
                            <MathView content={concept.definition} />
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Nội dung bài giảng toàn văn */}
                {lesson.content && (
                  <div style={{ marginBottom: '20px' }}>
                    <h4 style={{ fontSize: '1.02rem', fontWeight: 700, color: '#0f172a', marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <FileText size={18} color="#059669" />
                      <span>Nội Dung Lý Thuyết Chi Tiết</span>
                    </h4>
                    <div
                      style={{
                        padding: '20px 24px',
                        borderRadius: 'var(--radius-md)',
                        background: '#ffffff',
                        border: '1px solid #e2e8f0',
                        lineHeight: 1.7,
                        fontSize: '0.95rem',
                        color: '#1e293b',
                        whiteSpace: 'pre-line',
                        boxShadow: '0 1px 3px rgba(15, 23, 42, 0.03)',
                      }}
                    >
                      <MathView content={lesson.content} />
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* ================= TAB 3: BÀI TẬP MẪU & LỜI GIẢI ================= */}
            {activeTab === 'exercises' && (
              <div className="animate-fade-in">
                {lesson.worked_examples && lesson.worked_examples.length > 0 ? (
                  <div style={{ marginBottom: '24px' }}>
                    <h4 style={{ fontSize: '1.02rem', fontWeight: 700, color: '#0f172a', marginBottom: '14px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <Lightbulb size={18} color="#d97706" />
                      <span>Bài Tập Mẫu Có Hướng Dẫn Từng Bước ({lesson.worked_examples.length})</span>
                    </h4>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
                      {lesson.worked_examples.map((ex: any, exIdx: number) => (
                        <div
                          key={exIdx}
                          style={{
                            padding: '18px 20px',
                            borderRadius: 'var(--radius-md)',
                            background: '#ffffff',
                            border: '1px solid #fed7aa',
                            boxShadow: '0 2px 6px rgba(217, 119, 6, 0.05)',
                          }}
                        >
                          <div style={{ fontSize: '0.92rem', fontWeight: 700, color: '#9a3412', marginBottom: '8px' }}>
                            Ví dụ {exIdx + 1}:
                          </div>
                          <div style={{ fontSize: '0.94rem', lineHeight: 1.6, marginBottom: '12px', color: '#1e293b' }}>
                            <MathView content={ex.problem} />
                          </div>

                          <div
                            style={{
                              padding: '12px 14px',
                              borderRadius: 'var(--radius-sm)',
                              background: '#fffbeb',
                              border: '1px solid #fde68a',
                              fontSize: '0.9rem',
                              lineHeight: 1.65,
                              color: '#78350f',
                              whiteSpace: 'pre-line',
                              marginBottom: '10px',
                            }}
                          >
                            <div style={{ fontWeight: 700, marginBottom: '4px', color: '#92400e' }}>
                              Lời giải chi tiết:
                            </div>
                            <MathView content={ex.solution} />
                          </div>

                          {ex.answer && (
                            <div style={{ fontSize: '0.88rem', fontWeight: 700, color: '#059669', display: 'flex', alignItems: 'center', gap: '6px' }}>
                              <CheckCircle2 size={16} />
                              <span>Đáp số: <MathView content={ex.answer} /></span>
                            </div>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                ) : (
                  <div style={{ textAlign: 'center', padding: '30px', color: '#64748b' }}>
                    Chưa có bài tập mẫu cho phần này. Hãy xem phần Mô Phỏng Trực Quan.
                  </div>
                )}

                {/* Các lỗi sai thường gặp */}
                {lesson.common_mistakes && lesson.common_mistakes.length > 0 && (
                  <div
                    style={{
                      padding: '16px 20px',
                      borderRadius: 'var(--radius-md)',
                      background: '#fef2f2',
                      border: '1px solid #fecaca',
                      marginBottom: '20px',
                    }}
                  >
                    <h4 style={{ fontSize: '0.96rem', fontWeight: 700, color: '#b91c1c', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <AlertTriangle size={16} />
                      <span>Các Lỗi Sai Thường Gặp Cần Tránh</span>
                    </h4>
                    <ul style={{ paddingLeft: '20px', display: 'flex', flexDirection: 'column', gap: '6px', fontSize: '0.9rem', margin: 0 }}>
                      {lesson.common_mistakes.map((mistake: string, mIdx: number) => (
                        <li key={mIdx} style={{ color: '#991b1b', lineHeight: 1.55 }}>
                          {mistake}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            )}

            {/* ================= TAB 4: VIDEO BÀI HỌC TRỰC QUAN & YOUTUBE ================= */}
            {activeTab === 'video' && (
              <div className="animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                {/* Banner giới thiệu video */}
                <div
                  style={{
                    padding: '16px 20px',
                    borderRadius: 'var(--radius-md)',
                    background: 'linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%)',
                    border: '1px solid #fecaca',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    flexWrap: 'wrap',
                    gap: '12px',
                    boxShadow: '0 2px 8px rgba(220, 38, 38, 0.05)',
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                    <div style={{ background: '#dc2626', color: '#ffffff', borderRadius: '50%', width: '42px', height: '42px', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                      <PlayCircle size={24} />
                    </div>
                    <div>
                      <div style={{ fontWeight: 800, fontSize: '1rem', color: '#991b1b' }}>
                        Xem Video Bài Học Trực Tiếp Trong Ứng Dụng
                      </div>
                      <div style={{ fontSize: '0.84rem', color: '#b91c1c', marginTop: '2px' }}>
                        Video phát ngay trong cửa sổ học tập, không cần rời khỏi trang web.
                      </div>
                    </div>
                  </div>

                  <span className="badge" style={{ background: '#ffffff', color: '#dc2626', border: '1px solid #fca5a5', fontWeight: 700, fontSize: '0.78rem' }}>
                    📺 Đang phát: {currentVideo.author}
                  </span>
                </div>

                {/* KHUNG NHÚNG VIDEO YOUTUBE PHÁT TRỰC TIẾP TRONG ỨNG DỤNG */}
                <div
                  style={{
                    borderRadius: 'var(--radius-md)',
                    overflow: 'hidden',
                    background: '#0f172a',
                    border: '1px solid #334155',
                    boxShadow: '0 4px 16px rgba(0, 0, 0, 0.2)',
                  }}
                >
                  <div style={{ padding: '12px 18px', background: '#1e293b', borderBottom: '1px solid #334155', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: '#f8fafc', fontSize: '0.9rem', fontWeight: 700 }}>
                      <Video size={17} color="#ef4444" />
                      <span>{currentVideo.title}</span>
                    </div>
                    <span style={{ fontSize: '0.74rem', background: '#334155', color: '#cbd5e1', padding: '2px 8px', borderRadius: '4px' }}>
                      {currentVideo.badge}
                    </span>
                  </div>

                  {/* Video Player Iframe chuẩn YouTube Embed không bị chặn */}
                  <div style={{ position: 'relative', width: '100%', paddingTop: '56.25%', background: '#000000' }}>
                    <iframe
                      key={currentVideo.id}
                      style={{
                        position: 'absolute',
                        top: 0,
                        left: 0,
                        width: '100%',
                        height: '100%',
                        border: 'none',
                      }}
                      src={`https://www.youtube.com/embed/${currentVideo.id}?autoplay=0&rel=0&modestbranding=1`}
                      title={currentVideo.title}
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowFullScreen
                    />
                  </div>

                  <div style={{ padding: '12px 18px', background: '#0f172a', color: '#94a3b8', fontSize: '0.82rem', lineHeight: 1.5, borderTop: '1px solid #1e293b' }}>
                    📖 <strong>Tóm tắt nội dung video:</strong> {currentVideo.desc}
                  </div>
                </div>

                {/* DANH SÁCH CÁC VIDEO ĐƯỢC CHỌN LỌC ĐỂ CHUYỂN BÀI 1-CLICK (KHÔNG MỞ TAB MỚI) */}
                <div
                  style={{
                    padding: '18px 20px',
                    borderRadius: 'var(--radius-md)',
                    background: '#ffffff',
                    border: '1px solid #e2e8f0',
                    boxShadow: '0 2px 8px rgba(15, 23, 42, 0.04)',
                  }}
                >
                  <div style={{ fontWeight: 700, fontSize: '0.94rem', color: '#0f172a', marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <Sparkles size={16} color="#dc2626" />
                    <span>Chọn Video Khác Cho Chủ Đề Này (Bấm Để Phát Ngay Trên Khung):</span>
                  </div>

                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: '12px' }}>
                    {curatedVideos.map((vid: { id: string; title: string; author: string; badge: string; desc: string }) => {
                      const isSelected = currentVideo.id === vid.id;
                      return (
                        <button
                          key={vid.id}
                          type="button"
                          onClick={() => setActiveEmbeddedVideo(vid)}
                          className="glass-card"
                          style={{
                            padding: '14px 16px',
                            textAlign: 'left',
                            display: 'flex',
                            flexDirection: 'column',
                            justifyContent: 'space-between',
                            border: isSelected ? '2px solid #dc2626' : '1px solid #e2e8f0',
                            background: isSelected ? '#fef2f2' : '#ffffff',
                            cursor: 'pointer',
                            borderRadius: 'var(--radius-sm)',
                            boxShadow: isSelected ? '0 0 0 1px #dc2626' : undefined,
                            transition: 'all 0.2s ease',
                          }}
                        >
                          <div>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                              <span style={{ fontSize: '0.72rem', fontWeight: 700, color: isSelected ? '#dc2626' : '#64748b', background: isSelected ? '#fee2e2' : '#f1f5f9', padding: '2px 6px', borderRadius: '4px' }}>
                                {vid.badge}
                              </span>
                              {isSelected && (
                                <span style={{ fontSize: '0.72rem', fontWeight: 700, color: '#dc2626' }}>
                                  ▶ Đang phát
                                </span>
                              )}
                            </div>
                            <div style={{ fontWeight: 700, fontSize: '0.88rem', color: isSelected ? '#991b1b' : '#0f172a', marginBottom: '4px', lineHeight: 1.35 }}>
                              {vid.title}
                            </div>
                            <div style={{ fontSize: '0.78rem', color: '#64748b', lineHeight: 1.45 }}>
                              Kênh: <strong>{vid.author}</strong>
                            </div>
                          </div>
                          <div style={{ marginTop: '10px', fontSize: '0.76rem', fontWeight: 600, color: isSelected ? '#dc2626' : '#2563eb' }}>
                            {isSelected ? 'Đang phát ở khung trên' : 'Bấm để phát video này →'}
                          </div>
                        </button>
                      );
                    })}
                  </div>
                </div>

                {/* Nút tìm thêm trên YouTube (tùy chọn dự phòng) */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 16px', background: '#f8fafc', borderRadius: 'var(--radius-sm)', border: '1px solid #e2e8f0', fontSize: '0.82rem', color: '#64748b' }}>
                  <span>Nếu muốn tìm kiếm thêm hàng nghìn video mở rộng ngoài thư viện chọn lọc:</span>
                  <a
                    href={`https://www.youtube.com/results?search_query=${encodeURIComponent(`${lesson.title_vi} ${lesson.subject || ''}`)}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{ color: '#dc2626', fontWeight: 700, textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '4px' }}
                  >
                    <span>Mở danh sách tìm kiếm YouTube</span>
                    <ExternalLink size={12} />
                  </a>
                </div>
              </div>
            )}

            {/* ================= TAB 5: GIA SƯ AI & TIÊN QUYẾT ================= */}
            {activeTab === 'ai' && (
              <div className="animate-fade-in">
                {/* Gia sư AI */}
                <div
                  style={{
                    padding: '18px 20px',
                    borderRadius: 'var(--radius-md)',
                    background: '#faf5ff',
                    border: '1px solid #e9d5ff',
                    marginBottom: '22px',
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px', marginBottom: '10px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <Bot size={20} color="#7e22ce" />
                      <span style={{ fontWeight: 700, fontSize: '0.95rem', color: '#6b21a8' }}>
                        Gia Sư AI AISTEM: Hướng Dẫn Tư Duy Chuyên Sâu
                      </span>
                    </div>

                    <button
                      className="btn btn-secondary"
                      style={{ fontSize: '0.8rem', padding: '6px 12px', background: '#ffffff' }}
                      onClick={handleAskAI}
                      disabled={aiLoading}
                    >
                      <Sparkles size={14} color="#7e22ce" />
                      <span>{aiLoading ? 'Đang phân tích...' : 'Hỏi Gia Sư AI Về Bài Này'}</span>
                    </button>
                  </div>

                  {aiExplanation ? (
                    <div
                      style={{
                        marginTop: '12px',
                        padding: '14px 16px',
                        borderRadius: 'var(--radius-sm)',
                        background: '#ffffff',
                        border: '1px solid #d8b4fe',
                        fontSize: '0.92rem',
                        lineHeight: 1.65,
                        whiteSpace: 'pre-line',
                        color: '#1e293b',
                      }}
                      className="animate-fade-in"
                    >
                      <MathView content={aiExplanation} />
                    </div>
                  ) : (
                    <p style={{ fontSize: '0.84rem', color: '#581c87', margin: 0 }}>
                      Bấm nút để AI phân tích mối liên kết thực nghiệm, mẹo nhớ nhanh và ứng dụng giải bài thi của bài học.
                    </p>
                  )}
                </div>

                {/* Chuỗi liên kết tiên quyết & mở khóa */}
                <div
                  style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
                    gap: '14px',
                  }}
                >
                  {/* Cần học trước */}
                  <div
                    style={{
                      padding: '14px 16px',
                      borderRadius: 'var(--radius-md)',
                      background: '#fffbeb',
                      border: '1px solid #fde68a',
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                      <GitFork size={16} color="#d97706" />
                      <span style={{ fontWeight: 700, fontSize: '0.88rem', color: '#b45309' }}>
                        Kiến Thức Gốc Cần Nắm Trước {lesson.prerequisite_details?.length ? `(${lesson.prerequisite_details.length})` : ''}
                      </span>
                    </div>
                    {lesson.prerequisite_details && lesson.prerequisite_details.length > 0 ? (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                        {lesson.prerequisite_details.map((prereq: any) => (
                          <button
                            key={prereq.id}
                            className="btn btn-secondary"
                            style={{
                              textAlign: 'left',
                              justifyContent: 'flex-start',
                              padding: '6px 10px',
                              fontSize: '0.82rem',
                              borderRadius: 'var(--radius-sm)',
                              border: '1px solid #fde68a',
                              background: '#ffffff',
                              color: '#b45309',
                            }}
                            onClick={() => handleSwitchLesson(prereq.id)}
                            title={`Học trước: ${prereq.title_vi}`}
                          >
                            <span>← {prereq.title_vi}</span>
                          </button>
                        ))}
                      </div>
                    ) : (
                      <p style={{ fontSize: '0.82rem', color: '#78350f', margin: 0 }}>
                        🌱 Đây là bài học nền tảng gốc rễ.
                      </p>
                    )}
                  </div>

                  {/* Mở khóa tiếp theo */}
                  <div
                    style={{
                      padding: '14px 16px',
                      borderRadius: 'var(--radius-md)',
                      background: '#f0fdf4',
                      border: '1px solid #bbf7d0',
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                      <ArrowRight size={16} color="#059669" />
                      <span style={{ fontWeight: 700, fontSize: '0.88rem', color: '#047857' }}>
                        Mở Khóa Các Bài Tiếp Theo {lesson.next_lessons?.length ? `(${lesson.next_lessons.length})` : ''}
                      </span>
                    </div>
                    {lesson.next_lessons && lesson.next_lessons.length > 0 ? (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                        {lesson.next_lessons.map((nextL: any) => (
                          <button
                            key={nextL.id}
                            className="btn btn-secondary"
                            style={{
                              textAlign: 'left',
                              justifyContent: 'flex-start',
                              padding: '6px 10px',
                              fontSize: '0.82rem',
                              borderRadius: 'var(--radius-sm)',
                              border: '1px solid #bbf7d0',
                              background: '#ffffff',
                              color: '#047857',
                            }}
                            onClick={() => handleSwitchLesson(nextL.id)}
                            title={`Bài tiếp theo: ${nextL.title_vi}`}
                          >
                            <span>→ {nextL.title_vi}</span>
                          </button>
                        ))}
                      </div>
                    ) : (
                      <p style={{ fontSize: '0.82rem', color: '#064e3b', margin: 0 }}>
                        🎯 Đây là bài học chuyên sâu đỉnh cao của chuyên đề.
                      </p>
                    )}
                  </div>
                </div>
              </div>
            )}
          </div>
        ) : null}
      </div>
    </div>,
    document.body
  );
};
