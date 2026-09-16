import { useState, type FC } from 'react';
import { BookOpen, ShieldCheck, GraduationCap, Brain, Menu, X, Clock, Library, LogIn, LogOut, User, Sparkles } from 'lucide-react';
import { AistemXLogo } from './AistemXLogo';

export type TabType = 'formulas' | 'lessons' | 'practice' | 'exams' | 'scholarship' | 'flashcards' | 'analytics';

interface NavbarProps {
  activeTab: TabType;
  onTabChange: (tab: TabType) => void;
  pgHealthy?: boolean;
  studentUser?: any;
  onOpenStudentAuth?: (mode: 'login' | 'register') => void;
  onLogoutStudent?: () => void;
  onLogoClick?: () => void;
}

export const Navbar: FC<NavbarProps> = ({
  activeTab,
  onTabChange,
  studentUser,
  onOpenStudentAuth,
  onLogoutStudent,
  onLogoClick,
}) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navItems = [
    { id: 'lessons' as TabType, label: 'Bài Học', icon: Library },
    { id: 'formulas' as TabType, label: 'Công Thức', icon: BookOpen },
    { id: 'practice' as TabType, label: 'Luyện Bài', icon: ShieldCheck },
    { id: 'exams' as TabType, label: 'Thi Thử', icon: Clock },
    { id: 'scholarship' as TabType, label: 'Học Bổng', icon: GraduationCap },
    { id: 'flashcards' as TabType, label: 'Ghi Nhớ', icon: Brain },
  ];

  const handleSelectTab = (tab: TabType) => {
    onTabChange(tab);
    setMobileMenuOpen(false);
  };

  return (
    <header
      style={{
        position: 'sticky',
        top: 0,
        zIndex: 100,
        background: 'rgba(255, 255, 255, 0.94)',
        backdropFilter: 'blur(20px)',
        WebkitBackdropFilter: 'blur(20px)',
        borderBottom: '1px solid var(--border-subtle)',
        boxShadow: '0 1px 4px rgba(15, 23, 42, 0.05)',
        padding: '0 20px',
      }}
    >
      <div
        style={{
          maxWidth: '1360px',
          margin: '0 auto',
          height: '70px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          gap: '16px',
        }}
      >
        {/* Brand Logo */}
        <div
          onClick={() => {
            if (onLogoClick) onLogoClick();
            else handleSelectTab('lessons');
          }}
          title="AISTEM X — Hệ Tri Thức & AI Khoa Học Toàn Diện (aistemx.com)"
        >
          <AistemXLogo variant="full" size={38} />
        </div>

        {/* Desktop Navigation */}
        {studentUser ? (
          <nav
            style={{ display: 'flex', alignItems: 'center', gap: '6px' }}
            className="desktop-nav-bar"
          >
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = activeTab === item.id;
              return (
                <button
                  key={item.id}
                  className={`btn ${isActive ? 'btn-primary' : 'btn-secondary'}`}
                  style={{
                    fontSize: '0.88rem',
                    padding: '8px 14px',
                    borderRadius: 'var(--radius-md)',
                    position: 'relative',
                  }}
                  onClick={() => handleSelectTab(item.id)}
                >
                  <Icon size={16} />
                  <span>{item.label}</span>
                </button>
              );
            })}
          </nav>
        ) : (
          <div className="desktop-nav-bar" style={{ display: 'flex', alignItems: 'center', gap: '20px', color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
            <span style={{ color: '#1d4ed8', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '6px' }}>
              <Sparkles size={15} color="#1d4ed8" />
              Cổng Học Thuật & Săn Học Bổng Toàn Diện
            </span>
          </div>
        )}

        {/* User Actions / Auth */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          {studentUser ? (
            <>
              {/* Learner Info Badge */}
              <div
                style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '8px',
                  padding: '6px 14px',
                  borderRadius: 'var(--radius-full)',
                  background: '#e0f2fe',
                  border: '1px solid #bae6fd',
                  fontSize: '0.84rem',
                  color: '#0369a1',
                  fontWeight: 600,
                }}
              >
                <div
                  style={{
                    width: '24px',
                    height: '24px',
                    borderRadius: '50%',
                    background: 'linear-gradient(135deg, #818cf8 0%, #38bdf8 100%)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    color: '#fff',
                    fontSize: '0.72rem',
                    fontWeight: 700,
                  }}
                >
                  <User size={13} />
                </div>
                <span>{studentUser.full_name || studentUser.username || 'Học Viên'}</span>
              </div>

              {/* Logout Button */}
              {onLogoutStudent && (
                <button
                  className="btn btn-secondary"
                  style={{
                    padding: '8px 12px',
                    fontSize: '0.82rem',
                    color: '#94a3b8',
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: '6px',
                  }}
                  onClick={onLogoutStudent}
                  title="Đăng xuất khỏi tài khoản học viên"
                >
                  <LogOut size={15} />
                  <span className="desktop-nav-bar">Đăng Xuất</span>
                </button>
              )}
            </>
          ) : (
            <>
              {/* Guest CTA Buttons */}
              <button
                className="btn btn-secondary"
                style={{
                  fontSize: '0.88rem',
                  padding: '8px 16px',
                  borderRadius: 'var(--radius-md)',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '6px',
                }}
                onClick={() => onOpenStudentAuth && onOpenStudentAuth('login')}
              >
                <LogIn size={15} />
                <span>Đăng Nhập</span>
              </button>

              <button
                className="btn btn-primary"
                style={{
                  fontSize: '0.88rem',
                  padding: '8px 18px',
                  borderRadius: 'var(--radius-md)',
                  fontWeight: 700,
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '6px',
                }}
                onClick={() => onOpenStudentAuth && onOpenStudentAuth('register')}
              >
                <span>Bắt Đầu Học</span>
              </button>
            </>
          )}

          {studentUser && (
            <button
              className="btn btn-secondary mobile-menu-toggle"
              style={{ padding: '8px', display: 'none' }}
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              aria-label="Toggle navigation menu"
            >
              {mobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
            </button>
          )}
        </div>
      </div>

      {/* Mobile Drawer (Only for authenticated student) */}
      {studentUser && mobileMenuOpen && (
        <div
          style={{
            padding: '16px',
            borderTop: '1px solid var(--border-subtle)',
            background: 'var(--bg-secondary)',
            display: 'flex',
            flexDirection: 'column',
            gap: '8px',
          }}
          className="mobile-drawer"
        >
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                className={`btn ${isActive ? 'btn-primary' : 'btn-secondary'}`}
                style={{
                  width: '100%',
                  justifyContent: 'flex-start',
                  padding: '12px 16px',
                }}
                onClick={() => handleSelectTab(item.id)}
              >
                <Icon size={18} />
                <span style={{ flex: 1, textAlign: 'left' }}>{item.label}</span>
              </button>
            );
          })}
        </div>
      )}
    </header>
  );
};
