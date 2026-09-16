import { useState, type FC } from 'react';
import { api } from '../services/api';
import { X, LogIn, UserPlus, Lock, Mail, User, Sparkles } from 'lucide-react';

interface StudentAuthModalProps {
  initialMode?: 'login' | 'register';
  onClose: () => void;
  onSuccess: (user: any, token: string) => void;
}

export const StudentAuthModal: FC<StudentAuthModalProps> = ({
  initialMode = 'login',
  onClose,
  onSuccess,
}) => {
  const [mode, setMode] = useState<'login' | 'register'>(initialMode);
  const [usernameOrEmail, setUsernameOrEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFillDemo = () => {
    setUsernameOrEmail('hocsinh@aistem.edu.vn');
    setPassword('123456');
    setError(null);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      if (mode === 'login') {
        if (!usernameOrEmail.trim() || !password.trim()) {
          throw new Error('Vui lòng nhập đầy đủ tên đăng nhập/email và mật khẩu.');
        }
        const data = await api.loginStudent(usernameOrEmail.trim(), password);
        onSuccess(data.user, data.token);
      } else {
        if (!username.trim() || !email.trim() || !password.trim()) {
          throw new Error('Vui lòng điền đầy đủ các thông tin bắt buộc.');
        }
        const data = await api.registerStudent(
          username.trim(),
          email.trim(),
          password,
          fullName.trim() || username.trim()
        );
        onSuccess(data.user, data.token);
      }
    } catch (err: any) {
      console.error('Lỗi xác thực:', err);
      setError(err?.message || 'Có lỗi xảy ra, vui lòng thử lại.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        zIndex: 250,
        background: 'rgba(15, 23, 42, 0.45)',
        backdropFilter: 'blur(16px)',
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
          maxWidth: '460px',
          padding: '32px',
          borderRadius: 'var(--radius-lg)',
          boxShadow: '0 20px 40px -10px rgba(15, 23, 42, 0.15)',
          position: 'relative',
          border: '1px solid #cbd5e1',
          background: '#ffffff',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Close Button */}
        <button
          className="btn btn-secondary"
          style={{ position: 'absolute', right: '16px', top: '16px', padding: '6px', borderRadius: '50%' }}
          onClick={onClose}
        >
          <X size={18} />
        </button>

        {/* Modal Header */}
        <div style={{ textAlign: 'center', marginBottom: '24px' }}>
          <div
            style={{
              width: '52px',
              height: '52px',
              borderRadius: '16px',
              background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              margin: '0 auto 12px',
              boxShadow: '0 4px 16px rgba(2, 132, 199, 0.3)',
            }}
          >
            {mode === 'login' ? <LogIn size={26} color="#fff" /> : <UserPlus size={26} color="#fff" />}
          </div>

          <h3 style={{ fontSize: '1.45rem', fontWeight: 800, color: '#0f172a', marginBottom: '4px' }}>
            {mode === 'login' ? 'Đăng Nhập Học Viên' : 'Đăng Ký Tài Khoản Học'}
          </h3>
          <p style={{ color: '#475569', fontSize: '0.86rem', margin: 0 }}>
            {mode === 'login'
              ? 'Bắt đầu lộ trình học cá nhân hóa & lưu tiến độ của bạn'
              : 'Tham gia nền tảng tự học STEM từ gốc rễ hoàn toàn miễn phí'}
          </p>
        </div>

        {/* Quick Demo Fill for Login */}
        {mode === 'login' && (
          <div
            style={{
              padding: '10px 14px',
              borderRadius: 'var(--radius-md)',
              background: '#f0f9ff',
              border: '1px solid #bae6fd',
              marginBottom: '20px',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
            }}
          >
            <div style={{ fontSize: '0.8rem', color: '#475569' }}>
              <span style={{ color: '#0284c7', fontWeight: 700 }}>Tài khoản học sinh mẫu:</span>
              <div>hocsinh@aistem.edu.vn / 123456</div>
            </div>
            <button
              type="button"
              className="btn btn-secondary"
              style={{ fontSize: '0.78rem', padding: '4px 10px', color: '#0284c7', background: '#ffffff', border: '1px solid #bae6fd' }}
              onClick={handleFillDemo}
            >
              <Sparkles size={13} style={{ marginRight: '4px' }} />
              Dùng Thử Ngay
            </button>
          </div>
        )}

        {/* Error Alert */}
        {error && (
          <div
            style={{
              padding: '10px 14px',
              borderRadius: 'var(--radius-sm)',
              background: 'rgba(239, 68, 68, 0.1)',
              border: '1px solid rgba(239, 68, 68, 0.3)',
              color: '#f87171',
              fontSize: '0.84rem',
              marginBottom: '16px',
            }}
          >
            {error}
          </div>
        )}

        {/* Form */}
        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
          {mode === 'login' ? (
            <>
              <div>
                <label style={{ fontSize: '0.84rem', fontWeight: 600, color: 'var(--text-secondary)', display: 'block', marginBottom: '6px' }}>
                  Email hoặc Tên Đăng Nhập
                </label>
                <div style={{ position: 'relative' }}>
                  <Mail
                    size={16}
                    style={{
                      position: 'absolute',
                      left: '12px',
                      top: '50%',
                      transform: 'translateY(-50%)',
                      color: 'var(--text-muted)',
                    }}
                  />
                  <input
                    type="text"
                    required
                    placeholder="VD: hocsinh@aistem.edu.vn"
                    value={usernameOrEmail}
                    onChange={(e) => setUsernameOrEmail(e.target.value)}
                    className="input-field"
                    style={{ paddingLeft: '38px', fontSize: '0.9rem' }}
                  />
                </div>
              </div>

              <div>
                <label style={{ fontSize: '0.84rem', fontWeight: 600, color: 'var(--text-secondary)', display: 'block', marginBottom: '6px' }}>
                  Mật Khẩu
                </label>
                <div style={{ position: 'relative' }}>
                  <Lock
                    size={16}
                    style={{
                      position: 'absolute',
                      left: '12px',
                      top: '50%',
                      transform: 'translateY(-50%)',
                      color: 'var(--text-muted)',
                    }}
                  />
                  <input
                    type="password"
                    required
                    placeholder="••••••••"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="input-field"
                    style={{ paddingLeft: '38px', fontSize: '0.9rem' }}
                  />
                </div>
              </div>
            </>
          ) : (
            <>
              <div>
                <label style={{ fontSize: '0.84rem', fontWeight: 600, color: 'var(--text-secondary)', display: 'block', marginBottom: '6px' }}>
                  Họ và Tên Học Viên
                </label>
                <div style={{ position: 'relative' }}>
                  <User
                    size={16}
                    style={{
                      position: 'absolute',
                      left: '12px',
                      top: '50%',
                      transform: 'translateY(-50%)',
                      color: 'var(--text-muted)',
                    }}
                  />
                  <input
                    type="text"
                    placeholder="VD: Nguyễn Minh Anh"
                    value={fullName}
                    onChange={(e) => setFullName(e.target.value)}
                    className="input-field"
                    style={{ paddingLeft: '38px', fontSize: '0.9rem' }}
                  />
                </div>
              </div>

              <div>
                <label style={{ fontSize: '0.84rem', fontWeight: 600, color: 'var(--text-secondary)', display: 'block', marginBottom: '6px' }}>
                  Tên Đăng Nhập (viết liền, không dấu)
                </label>
                <div style={{ position: 'relative' }}>
                  <User
                    size={16}
                    style={{
                      position: 'absolute',
                      left: '12px',
                      top: '50%',
                      transform: 'translateY(-50%)',
                      color: 'var(--text-muted)',
                    }}
                  />
                  <input
                    type="text"
                    required
                    placeholder="VD: minhanh_stem"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    className="input-field"
                    style={{ paddingLeft: '38px', fontSize: '0.9rem' }}
                  />
                </div>
              </div>

              <div>
                <label style={{ fontSize: '0.84rem', fontWeight: 600, color: 'var(--text-secondary)', display: 'block', marginBottom: '6px' }}>
                  Địa Chỉ Email
                </label>
                <div style={{ position: 'relative' }}>
                  <Mail
                    size={16}
                    style={{
                      position: 'absolute',
                      left: '12px',
                      top: '50%',
                      transform: 'translateY(-50%)',
                      color: 'var(--text-muted)',
                    }}
                  />
                  <input
                    type="email"
                    required
                    placeholder="minhanh@gmail.com"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="input-field"
                    style={{ paddingLeft: '38px', fontSize: '0.9rem' }}
                  />
                </div>
              </div>

              <div>
                <label style={{ fontSize: '0.84rem', fontWeight: 600, color: 'var(--text-secondary)', display: 'block', marginBottom: '6px' }}>
                  Mật Khẩu (tối thiểu 6 ký tự)
                </label>
                <div style={{ position: 'relative' }}>
                  <Lock
                    size={16}
                    style={{
                      position: 'absolute',
                      left: '12px',
                      top: '50%',
                      transform: 'translateY(-50%)',
                      color: 'var(--text-muted)',
                    }}
                  />
                  <input
                    type="password"
                    required
                    placeholder="••••••••"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="input-field"
                    style={{ paddingLeft: '38px', fontSize: '0.9rem' }}
                  />
                </div>
              </div>
            </>
          )}

          <button
            type="submit"
            className="btn btn-primary"
            style={{ padding: '12px', fontSize: '0.95rem', fontWeight: 700, marginTop: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px' }}
            disabled={loading}
          >
            {loading ? (
              <span>Đang xử lý...</span>
            ) : mode === 'login' ? (
              <>
                <LogIn size={16} />
                <span>Đăng Nhập Vào Học</span>
              </>
            ) : (
              <>
                <UserPlus size={16} />
                <span>Hoàn Tất Đăng Ký</span>
              </>
            )}
          </button>
        </form>

        {/* Switch Mode Footer */}
        <div style={{ textAlign: 'center', marginTop: '20px', fontSize: '0.85rem', color: '#475569' }}>
          {mode === 'login' ? (
            <span>
              Chưa có tài khoản?{' '}
              <button
                type="button"
                style={{ background: 'none', border: 'none', color: '#0284c7', fontWeight: 700, cursor: 'pointer', padding: 0 }}
                onClick={() => {
                  setMode('register');
                  setError(null);
                }}
              >
                Đăng ký miễn phí
              </button>
            </span>
          ) : (
            <span>
              Đã có tài khoản?{' '}
              <button
                type="button"
                style={{ background: 'none', border: 'none', color: '#0284c7', fontWeight: 700, cursor: 'pointer', padding: 0 }}
                onClick={() => {
                  setMode('login');
                  setError(null);
                }}
              >
                Đăng nhập ngay
              </button>
            </span>
          )}
        </div>
      </div>
    </div>
  );
};
