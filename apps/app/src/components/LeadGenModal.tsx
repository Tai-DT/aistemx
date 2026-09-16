import { useState, type FC } from 'react';
import { X, Gift, Send, CheckCircle2, Download } from 'lucide-react';
import confetti from 'canvas-confetti';

interface LeadGenModalProps {
  onClose: () => void;
}

export const LeadGenModal: FC<LeadGenModalProps> = ({ onClose }) => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [school, setSchool] = useState('');
  const [target, setTarget] = useState('hoc-bong-ivy-league');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim() || !email.trim()) return;

    // Save lead to local storage
    try {
      const existing = JSON.parse(localStorage.getItem('aistem_leads') || '[]');
      existing.push({ name, email, phone, school, target, createdAt: new Date().toISOString() });
      localStorage.setItem('aistem_leads', JSON.stringify(existing));
    } catch {
      // ignore
    }

    setSubmitted(true);
    confetti({ particleCount: 70, spread: 80 });
  };

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        zIndex: 300,
        background: 'rgba(15, 23, 42, 0.45)',
        backdropFilter: 'blur(8px)',
        WebkitBackdropFilter: 'blur(8px)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '20px',
      }}
      onClick={onClose}
    >
      <div
        className="glass-panel animate-scale-up"
        style={{
          width: '100%',
          maxWidth: '520px',
          padding: '32px 28px',
          borderRadius: 'var(--radius-lg)',
          background: '#ffffff',
          boxShadow: '0 20px 40px -10px rgba(15, 23, 42, 0.15)',
          position: 'relative',
          border: '1px solid #bae6fd',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        <button
          className="btn btn-secondary"
          style={{ position: 'absolute', right: '16px', top: '16px', padding: '6px', borderRadius: '50%' }}
          onClick={onClose}
        >
          <X size={18} />
        </button>

        {submitted ? (
          <div style={{ textAlign: 'center', padding: '20px 10px' }}>
            <div
              style={{
                width: '60px',
                height: '60px',
                borderRadius: '50%',
                background: 'rgba(16, 185, 129, 0.15)',
                color: '#10b981',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                margin: '0 auto 16px',
                border: '1px solid rgba(16, 185, 129, 0.3)',
              }}
            >
              <CheckCircle2 size={32} />
            </div>

            <h3 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text-primary)', marginBottom: '8px' }}>
              Đăng Ký Nhận Cẩm Nang Thành Công!
            </h3>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', lineHeight: 1.6, marginBottom: '24px' }}>
              Bộ tài liệu <strong>Cẩm Nang 10,682 Công Thức STEM & Bản Đồ Săn Học Bổng Quốc Tế</strong> đã được kích hoạt. Ban Cố Vấn AISTEM X sẽ gửi tài liệu và phân tích lộ trình qua email của bạn: <strong>{email}</strong>.
            </p>

            <a
              href="/data/catalog_summary.json"
              download="AISTEMX_Formula_Handbook_Summary.json"
              className="btn btn-primary"
              style={{ width: '100%', padding: '12px', fontSize: '0.95rem' }}
            >
              <Download size={18} />
              <span>Tải Bản Tóm Tắt PDF / JSON Ngay</span>
            </a>
          </div>
        ) : (
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '16px' }}>
              <div
                style={{
                  width: '42px',
                  height: '42px',
                  borderRadius: '12px',
                  background: 'linear-gradient(135deg, #f59e0b 0%, #ef4444 100%)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                }}
              >
                <Gift size={22} color="#fff" />
              </div>
              <div>
                <h3 style={{ fontSize: '1.25rem', fontWeight: 800, lineHeight: 1.2 }}>
                  Nhận Cẩm Nang STEM Miễn Phí
                </h3>
                <div style={{ fontSize: '0.78rem', color: '#d97706', fontWeight: 600 }}>
                  TẶNG 5,272 CÔNG THỨC & LỘ TRÌNH HỌC BỔNG TOÀN PHẦN
                </div>
              </div>
            </div>

            <p style={{ fontSize: '0.86rem', color: 'var(--text-secondary)', lineHeight: 1.5, marginBottom: '18px' }}>
              Điền thông tin để nhận miễn phí bộ tài liệu chuẩn quốc tế độc quyền từ AISTEM X và nhận tư vấn chiến lược xét tuyển đại học top đầu:
            </p>

            <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                  Họ và tên của bạn: *
                </label>
                <input
                  type="text"
                  required
                  placeholder="Ví dụ: Nguyễn Văn An"
                  className="input-field"
                  style={{ fontSize: '0.88rem', padding: '10px 14px' }}
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                />
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                    Email nhận tài liệu: *
                  </label>
                  <input
                    type="email"
                    required
                    placeholder="email@domain.com"
                    className="input-field"
                    style={{ fontSize: '0.88rem', padding: '10px 14px' }}
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                    Số điện thoại / Zalo:
                  </label>
                  <input
                    type="tel"
                    placeholder="0912..."
                    className="input-field"
                    style={{ fontSize: '0.88rem', padding: '10px 14px' }}
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                  />
                </div>
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                  Trường THPT / Đại học hiện tại:
                </label>
                <input
                  type="text"
                  placeholder="Ví dụ: THPT Chuyên KHTN, Chuyên Amsterdam..."
                  className="input-field"
                  style={{ fontSize: '0.88rem', padding: '10px 14px' }}
                  value={school}
                  onChange={(e) => setSchool(e.target.value)}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                  Mục tiêu trọng tâm:
                </label>
                <select
                  className="input-field"
                  style={{ fontSize: '0.88rem', padding: '10px 14px', cursor: 'pointer' }}
                  value={target}
                  onChange={(e) => setTarget(e.target.value)}
                >
                  <option value="hoc-bong-ivy-league">Săn học bổng Mỹ / Ivy League & Top 30 National</option>
                  <option value="hoc-bong-chau-au">Học bổng Đức (DAAD), Anh (Oxbridge), Pháp, Thụy Điển</option>
                  <option value="hoc-bong-chau-a">Học bổng MEXT Nhật Bản, KGSP Hàn Quốc, Singa/NUS Singapore</option>
                  <option value="dai-hoc-top-vn">Thi Olympic & Tốt nghiệp THPT vào ĐH Bách Khoa, Y Dược, Ngoại Thương</option>
                </select>
              </div>

              <button
                type="submit"
                className="btn btn-primary"
                style={{ width: '100%', padding: '12px', marginTop: '6px' }}
              >
                <Send size={16} />
                <span>Gửi Thông Tin & Nhận Cẩm Nang PDF Ngay</span>
              </button>
            </form>
          </div>
        )}
      </div>
    </div>
  );
};
