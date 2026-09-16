import { useState, type FC } from 'react';
import { api } from '../../services/api';
import { ShieldCheck, Lock, User, AlertCircle, ArrowLeft } from 'lucide-react';

interface AdminLoginProps {
  onSuccess: (user: any) => void;
  onCancel: () => void;
}

export const AdminLogin: FC<AdminLoginProps> = ({ onSuccess, onCancel }) => {
  const [username, setUsername] = useState('admin@aistem.edu.vn');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!password.trim()) {
      setError('Vui lòng nhập mật khẩu quản trị.');
      return;
    }

    setLoading(true);
    setError('');
    try {
      const res = await api.loginAdmin(username, password);
      localStorage.setItem('aistem_admin_auth', JSON.stringify(res.user));
      onSuccess(res.user);
    } catch (err: any) {
      setError(err.message || 'Mật khẩu quản trị không chính xác.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        minHeight: '80vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '20px',
      }}
      className="animate-fade-in"
    >
      <div
        className="glass-panel"
        style={{
          width: '100%',
          maxWidth: '440px',
          padding: '36px 30px',
          borderRadius: 'var(--radius-lg)',
          boxShadow: '0 20px 50px rgba(0, 0, 0, 0.6)',
          border: '1px solid rgba(99, 102, 241, 0.3)',
        }}
      >
        <div style={{ textAlign: 'center', marginBottom: '28px' }}>
          <div
            style={{
              width: '56px',
              height: '56px',
              borderRadius: '16px',
              background: 'linear-gradient(135deg, #6366f1 0%, #06b6d4 100%)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              margin: '0 auto 16px',
              boxShadow: '0 0 24px rgba(99, 102, 241, 0.5)',
            }}
          >
            <ShieldCheck size={32} color="#fff" />
          </div>
          <h2 style={{ fontSize: '1.45rem', fontWeight: 800, color: '#fff' }}>Cổng Quản Trị AISTEM</h2>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginTop: '4px' }}>
            Khu vực bảo mật dành cho Ban Quản trị & Đào tạo
          </p>
        </div>

        {error && (
          <div
            style={{
              padding: '12px 14px',
              borderRadius: 'var(--radius-md)',
              background: 'rgba(244, 63, 94, 0.12)',
              border: '1px solid rgba(244, 63, 94, 0.3)',
              color: '#fda4af',
              fontSize: '0.85rem',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              marginBottom: '20px',
            }}
          >
            <AlertCircle size={16} style={{ flexShrink: 0 }} />
            <span>{error}</span>
          </div>
        )}

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.82rem', color: 'var(--text-secondary)', marginBottom: '6px' }}>
              Tài khoản quản trị viên:
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
                className="input-field"
                style={{ paddingLeft: '38px', fontSize: '0.9rem' }}
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="admin@aistem.edu.vn"
                required
              />
            </div>
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.82rem', color: 'var(--text-secondary)', marginBottom: '6px' }}>
              Mật khẩu truy cập:
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
                className="input-field"
                style={{ paddingLeft: '38px', fontSize: '0.9rem' }}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Nhập mật khẩu..."
                required
                autoFocus
              />
            </div>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '6px' }}>
              Gợi ý mặc định: <code>admin2026</code> hoặc <code>aistem2026</code>
            </div>
          </div>

          <button
            type="submit"
            className="btn btn-primary"
            style={{ width: '100%', padding: '12px', marginTop: '10px' }}
            disabled={loading}
          >
            {loading ? 'Đang xác thực...' : 'Đăng Nhập Quản Trị'}
          </button>

          <button
            type="button"
            className="btn btn-secondary"
            style={{ width: '100%', padding: '10px', fontSize: '0.85rem' }}
            onClick={onCancel}
          >
            <ArrowLeft size={16} />
            <span>Quay lại trang học sinh</span>
          </button>
        </form>
      </div>
    </div>
  );
};
