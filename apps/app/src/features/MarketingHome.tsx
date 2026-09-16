import { useState, type FC } from 'react';
import {
  Sparkles,
  ArrowRight,
  Gift,
  Star,
  Users,
  Lock,
  Compass,
  Trophy,
  Atom,
  ChevronRight,
  FileText,
  Waves,
  Dna,
  GraduationCap,
  Shield,
  Award,
  BookOpen,
} from 'lucide-react';
import { LeadGenModal } from '../components/LeadGenModal';
import { InteractiveStemSimulation } from '../components/InteractiveStemSimulation';

interface MarketingHomeProps {
  onOpenAuth: (mode: 'login' | 'register') => void;
  onPreviewLesson?: (lessonId: string) => void;
}

export const MarketingHome: FC<MarketingHomeProps> = ({ onOpenAuth }) => {
  const [showLeadModal, setShowLeadModal] = useState(false);

  const pillars = [
    {
      icon: Atom,
      color: '#0ea5e9',
      domain: 'Hóa Học & Nước H₂O',
      title: 'Dung Môi Vạn Năng & Liên Kết Phân Tử',
      desc: 'Hiểu cặn kẽ góc liên kết 104.5°, liên kết Hydro, sức căng bề mặt và vai trò dung môi quyết định mọi phản ứng hóa học tự nhiên.',
      highlight: 'H₂O • Cân Bằng Hóa Học • Động Học Phản Ứng',
    },
    {
      icon: Waves,
      color: '#38bdf8',
      domain: 'Vật Lý Tự Nhiên',
      title: 'Sóng Cơ, Cơ Học & Năng Lượng Vũ Trụ',
      desc: 'Từ sóng nước lan truyền λ = v/f, dao động điều hòa đến thuyết lượng tử photon E = hf và động lực học chất lưu thời gian thực.',
      highlight: 'Cơ Học • Sóng Giao Thoa • Nhiệt Động Lực Học',
    },
    {
      icon: Compass,
      color: '#06b6d4',
      domain: 'Toán Học Thuần Túy',
      title: 'Giải Tích, Tỷ Lệ Vàng & Hình Học Tự Nhiên',
      desc: 'Khám phá chuỗi Fibonacci trong xoáy nước, đạo hàm vi tích phân mô tả dòng chảy và ma trận tri thức liên kết không khoảng trống.',
      highlight: 'Vi Tích Phân • Tỷ Lệ Vàng Φ • Ma Trận DAG',
    },
    {
      icon: Dna,
      color: '#10b981',
      domain: 'Sinh Học Phân Tử',
      title: 'Chuỗi Xoắn DNA & Mầm Sống Quang Hợp',
      desc: 'Sự sống nảy nở từ đại dương nguyên thủy: mã di truyền xoắn kép DNA, cơ chế tế bào và phản ứng quang hợp chuyển hóa ánh sáng.',
      highlight: 'Di Truyền DNA • Tế Bào Học • Sinh Thái Học',
    },
  ];

  const demoLessons = [
    {
      id: 'math-physics-derivative',
      subject: 'Toán Học & Vật Lý',
      title: 'Đạo Hàm: Bản Chất Hình Học & Tốc Độ Lan Truyền Sóng Nước',
      duration: '25 phút',
      level: 'Cốt Lõi Vững Vàng',
      formula: 'v(t) = s\'(t) = lim[Δt→0] (Δs/Δt)',
      summary: 'Tại sao vi tích phân là ngôn ngữ duy nhất mô tả trọn vẹn sự biến thiên liên tục của vũ trụ và động lực học chất lưu.',
    },
    {
      id: 'chemistry-h2o-structure',
      subject: 'Hóa Học & Vật Lý Phân Tử',
      title: 'Cấu Trúc Phân Tử Nước H₂O: Góc Liên Kết 104.5° & Tính Phân Cực',
      duration: '30 phút',
      level: 'Chuyên Đề Trọng Tâm',
      formula: '2H₂ + O₂ → 2H₂O (ΔH = -571.6 kJ/mol)',
      summary: 'Khám phá lai hóa sp3 bất đối xứng của Oxy và mạng lưới liên kết hydro kiến tạo nên toàn bộ sự sống trên Trái Đất.',
    },
    {
      id: 'biology-dna-transcription',
      subject: 'Sinh Học & Hóa Sinh',
      title: 'Cơ Chế Phiên Mã DNA & Phản Ứng Quang Hợp Trong Dung Môi Nước',
      duration: '28 phút',
      level: 'Nâng Cao & Olympic',
      formula: '6CO₂ + 6H₂O + hv → C₆H₁₂O₆ + 6O₂',
      summary: 'Hành trình từ chuỗi xoắn kép Watson-Crick đến phân giải phân tử nước tạo oxy nuôi dưỡng khí quyển hành tinh.',
    },
  ];

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '64px', paddingBottom: '60px' }}>
      {/* 1. HERO BANNER */}
      <section
        className="glass-panel"
        style={{
          padding: '56px 36px',
          borderRadius: 'var(--radius-xl)',
          position: 'relative',
          overflow: 'hidden',
          background: 'radial-gradient(ellipse at 50% 0%, rgba(224, 242, 254, 0.75) 0%, #ffffff 80%)',
          border: '1px solid #cbd5e1',
          boxShadow: '0 12px 36px -8px rgba(15, 23, 42, 0.08)',
        }}
      >
        <div style={{ maxWidth: '960px', margin: '0 auto', textAlign: 'center', position: 'relative', zIndex: 2 }}>
          {/* Nature STEM Origin Tag */}
          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '8px',
              padding: '6px 18px',
              borderRadius: 'var(--radius-full)',
              background: '#e0f2fe',
              border: '1px solid #bae6fd',
              color: '#0369a1',
              fontSize: '0.84rem',
              fontWeight: 700,
              letterSpacing: '0.04em',
              marginBottom: '20px',
            }}
          >
            <GraduationCap size={16} color="#0284c7" />
            <span>CHUẨN HỌC ĐƯỜNG & OLYMPIAD • TOÁN - LÝ - HOÁ - SINH • TRÍ TUỆ NHÂN TẠO</span>
          </div>

          {/* Heading */}
          <h1
            style={{
              fontSize: 'clamp(2.1rem, 4.5vw, 3.4rem)',
              fontWeight: 800,
              letterSpacing: '-0.03em',
              lineHeight: 1.18,
              marginBottom: '20px',
            }}
          >
            AISTEM X — Hệ Tri Thức Khoa Học & AI Toàn Diện (aistemx.com)
            <br />
            <span className="gradient-text">Ươm Mầm Tài Năng • Chinh Phục Học Bổng Quốc Tế</span>
          </h1>

          {/* Subtitle */}
          <p
            style={{
              fontSize: 'clamp(1rem, 1.8vw, 1.15rem)',
              color: 'var(--text-secondary)',
              lineHeight: 1.65,
              maxWidth: '820px',
              margin: '0 auto 36px',
            }}
          >
            Nền tảng học thuật chuẩn mực dành cho học sinh, giáo viên và nhà trường: Kết nối <strong>5,272 công thức</strong>, 
            <strong> 1,018 bài giảng liên môn</strong> và <strong>4,351 bài toán kiểm định SymPy CAS</strong> cùng Gia sư AI tư duy bản chất, 
            nói không với học vẹt.
          </p>

          {/* Primary CTAs */}
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '14px',
              flexWrap: 'wrap',
            }}
          >
            <button
              className="btn btn-primary"
              style={{
                padding: '14px 30px',
                fontSize: '1.02rem',
                fontWeight: 700,
                borderRadius: 'var(--radius-md)',
                boxShadow: '0 8px 24px -4px rgba(14, 165, 233, 0.5)',
              }}
              onClick={() => onOpenAuth('login')}
            >
              <span>Đăng Nhập Vào Học Ngay</span>
              <ArrowRight size={18} />
            </button>

            <button
              className="btn btn-secondary"
              style={{
                padding: '14px 26px',
                fontSize: '0.98rem',
                fontWeight: 600,
                borderRadius: 'var(--radius-md)',
                border: '1px solid rgba(255, 255, 255, 0.15)',
              }}
              onClick={() => onOpenAuth('register')}
            >
              <span>Tạo Tài Khoản Học Viên</span>
            </button>

            <button
              className="btn btn-secondary"
              style={{
                padding: '14px 22px',
                fontSize: '0.92rem',
                borderRadius: 'var(--radius-md)',
                color: '#f59e0b',
                background: 'rgba(245, 158, 11, 0.08)',
                border: '1px solid rgba(245, 158, 11, 0.25)',
              }}
              onClick={() => setShowLeadModal(true)}
            >
              <Gift size={16} />
              <span>Nhận Cẩm Nang Học Bổng PDF</span>
            </button>
          </div>

          {/* Social Proof */}
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '28px',
              flexWrap: 'wrap',
              marginTop: '44px',
              paddingTop: '28px',
              borderTop: '1px solid #e2e8f0',
              color: '#475569',
              fontSize: '0.86rem',
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <Users size={16} color="#0284c7" />
              <span><strong>12,500+</strong> học viên tin cậy</span>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <Star size={16} color="#d97706" fill="#d97706" />
              <span><strong>98.4%</strong> đạt mục tiêu điểm số</span>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <Trophy size={16} color="#059669" />
              <span><strong>45+</strong> học bổng toàn phần quốc tế</span>
            </div>
          </div>
        </div>
      </section>

      {/* 2. AISTEM X ACADEMIC CREST & SCHOOL PHILOSOPHY */}
      <section
        className="glass-panel"
        style={{
          padding: '40px 32px',
          borderRadius: 'var(--radius-xl)',
          background: 'linear-gradient(135deg, #f8fafc 0%, #ffffff 50%, #eff6ff 100%)',
          border: '1px solid #bfdbfe',
          boxShadow: '0 10px 30px -5px rgba(29, 78, 216, 0.08)',
        }}
      >
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))',
            gap: '36px',
            alignItems: 'center',
          }}
        >
          {/* Visual Crest Card */}
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '24px',
              background: '#ffffff',
              borderRadius: 'var(--radius-lg)',
              border: '1px solid #e2e8f0',
              boxShadow: '0 8px 24px rgba(15, 23, 42, 0.06)',
              textAlign: 'center',
            }}
          >
            <div
              style={{
                position: 'relative',
                width: '100%',
                maxWidth: '280px',
                aspectRatio: '1/1',
                borderRadius: '20px',
                overflow: 'hidden',
                boxShadow: '0 12px 28px rgba(30, 58, 138, 0.15)',
                marginBottom: '16px',
              }}
            >
              <img
                src="/logo.svg"
                alt="AISTEM X — Biểu Tượng Khoa Học & AI Quốc Tế"
                style={{
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                  display: 'block',
                }}
              />
            </div>

            <div
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '6px',
                padding: '4px 12px',
                borderRadius: 'var(--radius-full)',
                background: '#eff6ff',
                border: '1px solid #bfdbfe',
                fontSize: '0.78rem',
                color: '#1d4ed8',
                fontWeight: 700,
                letterSpacing: '0.04em',
                textTransform: 'uppercase',
                marginBottom: '6px',
              }}
            >
              <Award size={14} color="#1d4ed8" />
              <span>Huy Hiệu Học Thuật Danh Giá</span>
            </div>

            <h3 style={{ fontSize: '1.25rem', fontWeight: 800, margin: '4px 0 6px', color: '#0f172a' }}>
              Biểu Tượng Tri Thức AISTEM X
            </h3>
            <p style={{ fontSize: '0.84rem', color: '#64748b', lineHeight: 1.5, margin: 0 }}>
              Giao thoa giữa chữ X công nghệ tương lai, 4 trụ cột liên môn Toán-Lý-Hoá-Sinh, ngọn đuốc sáng tạo và lõi hạt nhân trí tuệ AI.
            </p>
          </div>

          {/* School Philosophy Details */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
            <div>
              <div
                style={{
                  fontSize: '0.8rem',
                  color: '#2563eb',
                  fontWeight: 700,
                  textTransform: 'uppercase',
                  letterSpacing: '0.06em',
                  marginBottom: '6px',
                }}
              >
                Tiêu Chuẩn Thiết Kế Cho Môi Trường Học Đường
              </div>
              <h2 style={{ fontSize: '1.75rem', fontWeight: 800, color: '#0f172a', margin: '0 0 10px' }}>
                Tại Sao AISTEM X Phù Hợp Cho Học Sinh & Nhà Trường?
              </h2>
              <p style={{ fontSize: '0.92rem', color: '#475569', lineHeight: 1.6, margin: 0 }}>
                AISTEM X được kiến tạo để mang lại một môi trường học thuật trong sáng, uy tín và chuẩn mực, đáp ứng đầy đủ yêu cầu giảng dạy tại trường và bồi dưỡng chuyên sâu.
              </p>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '14px' }}>
              <div style={{ padding: '14px', borderRadius: 'var(--radius-md)', background: '#ffffff', border: '1px solid #e2e8f0' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#1d4ed8', fontWeight: 700, fontSize: '0.92rem', marginBottom: '4px' }}>
                  <BookOpen size={16} />
                  <span>Chuẩn Khung Quốc Gia & Quốc Tế</span>
                </div>
                <p style={{ fontSize: '0.82rem', color: '#64748b', margin: 0, lineHeight: 1.5 }}>
                  Bám sát chương trình GDPT 2018 và tương thích hoàn toàn với các chuẩn thi chuyên, AP, IB, SAT và Olympic KHTN.
                </p>
              </div>

              <div style={{ padding: '14px', borderRadius: 'var(--radius-md)', background: '#ffffff', border: '1px solid #e2e8f0' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#059669', fontWeight: 700, fontSize: '0.92rem', marginBottom: '4px' }}>
                  <Shield size={16} />
                  <span>Kiểm Định CAS Tuyệt Đối 100%</span>
                </div>
                <p style={{ fontSize: '0.82rem', color: '#64748b', margin: 0, lineHeight: 1.5 }}>
                  Toàn bộ 4,351 bài toán và công thức đều được kiểm tra tự động qua SymPy CAS Engine, loại bỏ hoàn toàn sai số.
                </p>
              </div>

              <div style={{ padding: '14px', borderRadius: 'var(--radius-md)', background: '#ffffff', border: '1px solid #e2e8f0' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#0284c7', fontWeight: 700, fontSize: '0.92rem', marginBottom: '4px' }}>
                  <Sparkles size={16} />
                  <span>Gia Sư AI Phương Pháp Socratic</span>
                </div>
                <p style={{ fontSize: '0.82rem', color: '#64748b', margin: 0, lineHeight: 1.5 }}>
                  AI không giải hộ bài tập mà đặt câu hỏi gợi mở, hướng dẫn từng bước tư duy giúp học sinh làm chủ bản chất.
                </p>
              </div>

              <div style={{ padding: '14px', borderRadius: 'var(--radius-md)', background: '#ffffff', border: '1px solid #e2e8f0' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#d97706', fontWeight: 700, fontSize: '0.92rem', marginBottom: '4px' }}>
                  <GraduationCap size={16} />
                  <span>Định Hướng Học Bổng Toàn Cầu</span>
                </div>
                <p style={{ fontSize: '0.82rem', color: '#64748b', margin: 0, lineHeight: 1.5 }}>
                  Tích hợp hồ sơ năng lực STEM, chứng chỉ học tập và 25 cẩm nang học bổng toàn phần Ivy League, Oxford, NUS.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 3. INTERACTIVE STEM SIMULATION LABORATORY */}
      <section>
        <div style={{ textAlign: 'center', marginBottom: '24px' }}>
          <div style={{ fontSize: '0.8rem', color: '#38bdf8', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.06em', marginBottom: '4px' }}>
            Trực Quan Hóa Tương Tác
          </div>
          <h2 style={{ fontSize: '1.75rem', fontWeight: 800, margin: 0 }}>
            Khám Phá Phòng Thí Nghiệm <span className="gradient-text">STEM Trực Quan</span>
          </h2>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.92rem', marginTop: '6px' }}>
            Tương tác trực tiếp với phân tử nước H₂O, sóng vật lý, đường xoắn ốc Fibonacci và chuỗi xoắn kép DNA ngay dưới đây:
          </p>
        </div>

        <InteractiveStemSimulation />
      </section>

      {/* 4. FOUR NATURAL STEM PILLARS */}
      <section>
        <div style={{ textAlign: 'center', marginBottom: '36px' }}>
          <div style={{ fontSize: '0.8rem', color: '#10b981', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.06em', marginBottom: '4px' }}>
            Tứ Trụ Tri Thức Tự Nhiên
          </div>
          <h2 style={{ fontSize: '1.8rem', fontWeight: 800, marginBottom: '8px' }}>
            Học Thuật Liên Môn: Gắn Kết 4 Lĩnh Vực Khoa Học Cốt Lõi
          </h2>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem', maxWidth: '720px', margin: '0 auto' }}>
            Thay vì học rời rạc từng môn, AISTEM X kết nối kiến thức theo chu trình tự nhiên giúp học sinh hiểu sâu và vận dụng giải quyết các bài toán quốc tế phức tạp.
          </p>
        </div>

        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
            gap: '20px',
          }}
        >
          {pillars.map((p, idx) => {
            const Icon = p.icon;
            return (
              <div
                key={idx}
                className="glass-panel"
                style={{
                  padding: '24px',
                  borderRadius: 'var(--radius-lg)',
                  border: '1px solid var(--border-subtle)',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '12px',
                  transition: 'transform 0.2s ease, border-color 0.2s ease',
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                  <div
                    style={{
                      width: '44px',
                      height: '44px',
                      borderRadius: '12px',
                      background: `${p.color}12`,
                      border: `1px solid ${p.color}30`,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                    }}
                  >
                    <Icon size={22} color={p.color} />
                  </div>
                  <span style={{ fontSize: '0.75rem', fontWeight: 700, color: p.color, background: `${p.color}12`, padding: '3px 8px', borderRadius: 'var(--radius-sm)' }}>
                    {p.domain}
                  </span>
                </div>

                <h3 style={{ fontSize: '1.12rem', fontWeight: 700, margin: 0, color: '#0f172a' }}>
                  {p.title}
                </h3>

                <p style={{ fontSize: '0.88rem', color: '#475569', lineHeight: 1.6, margin: 0, flex: 1 }}>
                  {p.desc}
                </p>

                <div
                  style={{
                    paddingTop: '12px',
                    borderTop: '1px solid #f1f5f9',
                    fontSize: '0.78rem',
                    color: '#0284c7',
                    fontWeight: 600,
                  }}
                >
                  🌱 {p.highlight}
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* 4. DEMO LESSON & REAL STEM PROBLEMS PREVIEW */}
      <section
        className="glass-panel"
        style={{
          padding: '36px 32px',
          borderRadius: 'var(--radius-xl)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
        }}
      >
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'flex-end',
            flexWrap: 'wrap',
            gap: '16px',
            marginBottom: '28px',
          }}
        >
          <div>
            <div
              style={{
                fontSize: '0.78rem',
                color: '#38bdf8',
                fontWeight: 700,
                textTransform: 'uppercase',
                letterSpacing: '0.05em',
                marginBottom: '4px',
              }}
            >
              Xem Trước Nội Dung Học
            </div>
            <h2 style={{ fontSize: '1.6rem', fontWeight: 800, margin: 0 }}>
              Một Vài Bài Học Mẫu Tiêu Biểu
            </h2>
          </div>

          <button
            className="btn btn-secondary"
            style={{ fontSize: '0.88rem', padding: '8px 16px' }}
            onClick={() => onOpenAuth('login')}
          >
            <span>Mở khóa toàn bộ 250+ bài học</span>
            <ChevronRight size={16} />
          </button>
        </div>

        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
            gap: '20px',
          }}
        >
          {demoLessons.map((item) => (
            <div
              key={item.id}
              style={{
                padding: '22px',
                borderRadius: 'var(--radius-md)',
                background: '#f8fafc',
                border: '1px solid #e2e8f0',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                gap: '14px',
                boxShadow: '0 1px 3px rgba(15, 23, 42, 0.04)',
              }}
            >
              <div>
                <div
                  style={{
                    display: 'inline-block',
                    fontSize: '0.75rem',
                    fontWeight: 600,
                    color: '#0284c7',
                    background: '#e0f2fe',
                    padding: '3px 8px',
                    borderRadius: 'var(--radius-sm)',
                    marginBottom: '10px',
                  }}
                >
                  {item.subject}
                </div>
                <h4 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#0f172a', marginBottom: '8px', lineHeight: 1.4 }}>
                  {item.title}
                </h4>

                <div
                  style={{
                    padding: '6px 10px',
                    borderRadius: '6px',
                    background: '#f1f5f9',
                    border: '1px solid #e2e8f0',
                    fontSize: '0.78rem',
                    fontFamily: 'JetBrains Mono, monospace',
                    color: '#0369a1',
                    marginBottom: '10px',
                  }}
                >
                  {item.formula}
                </div>

                <p style={{ fontSize: '0.84rem', color: '#475569', lineHeight: 1.55, margin: 0 }}>
                  {item.summary}
                </p>
              </div>

              <div
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  paddingTop: '12px',
                  borderTop: '1px solid #e2e8f0',
                  fontSize: '0.78rem',
                  color: '#64748b',
                }}
              >
                <span>⏱️ {item.duration}</span>
                <button
                  className="btn btn-secondary"
                  style={{ fontSize: '0.78rem', padding: '5px 10px', gap: '4px', color: '#0284c7' }}
                  onClick={() => onOpenAuth('login')}
                >
                  <Lock size={12} />
                  <span>Đăng nhập để học</span>
                </button>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* 5. GLOBAL SCHOLARSHIPS & PRESTIGIOUS OLYMPIAD PREP */}
      <section
        style={{
          borderRadius: 'var(--radius-xl)',
          padding: '40px 32px',
          background: 'linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%)',
          border: '1px solid #fde68a',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '24px',
          boxShadow: '0 8px 24px -4px rgba(217, 119, 6, 0.1)',
        }}
      >
        <div style={{ maxWidth: '640px' }}>
          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              fontSize: '0.78rem',
              fontWeight: 700,
              color: '#b45309',
              background: '#fef3c7',
              border: '1px solid #fde68a',
              padding: '4px 10px',
              borderRadius: 'var(--radius-full)',
              marginBottom: '10px',
            }}
          >
            <Gift size={13} color="#b45309" />
            <span>CẨM NANG HỌC BỔNG STEM TOÀN CẦU</span>
          </div>
          <h3 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#78350f', marginBottom: '8px' }}>
            Chiến Lược Nộp Đơn Vào MIT, Harvard, NUS & VinUni
          </h3>
          <p style={{ fontSize: '0.9rem', color: '#92400e', lineHeight: 1.6, margin: 0 }}>
            Tài liệu độc quyền tổng hợp cấu trúc bài luận cá nhân định hướng STEM, phương pháp xây dựng dự án nghiên cứu khoa học từ thực nghiệm nước & môi trường, cùng kinh nghiệm phỏng vấn học bổng toàn phần.
          </p>
        </div>

        <button
          className="btn btn-primary"
          style={{
            padding: '12px 24px',
            fontSize: '0.95rem',
            fontWeight: 700,
            background: 'linear-gradient(135deg, #d97706 0%, #b45309 100%)',
            border: 'none',
            color: '#ffffff',
            display: 'inline-flex',
            alignItems: 'center',
            gap: '8px',
          }}
          onClick={() => setShowLeadModal(true)}
        >
          <FileText size={16} />
          <span>Nhận Cẩm Nang Qua Email</span>
        </button>
      </section>

      {/* 6. BOTTOM CALL TO ACTION */}
      <section style={{ textAlign: 'center', maxWidth: '720px', margin: '0 auto' }}>
        <h3 style={{ fontSize: '1.75rem', fontWeight: 800, marginBottom: '12px' }}>
          Sẵn Sàng Khám Phá Khoa Học Thực Thụ?
        </h3>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem', marginBottom: '24px', lineHeight: 1.6 }}>
          Đăng nhập ngay để bắt đầu lộ trình học từ gốc rễ, rèn luyện tư duy thực nghiệm và mở khóa toàn bộ kho bài học, công thức tương tác và đề thi thử chuẩn quốc tế.
        </p>
        <button
          className="btn btn-primary"
          style={{ padding: '14px 34px', fontSize: '1.05rem', fontWeight: 700 }}
          onClick={() => onOpenAuth('login')}
        >
          <Sparkles size={18} style={{ marginRight: '6px' }} />
          <span>Đăng Nhập Vào Khóa Học</span>
        </button>
      </section>

      {/* Lead Generation Modal */}
      {showLeadModal && <LeadGenModal onClose={() => setShowLeadModal(false)} />}
    </div>
  );
};
