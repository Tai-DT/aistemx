import { useState, useEffect, lazy, Suspense } from 'react';
import { Navbar, type TabType } from './components/Navbar';
import { HeroShowcase } from './components/HeroShowcase';
import { MarketingHome } from './features/MarketingHome';
import { StudentAuthModal } from './components/StudentAuthModal';
import { AistemXLogo } from './components/AistemXLogo';
import { Heart, Lock, Loader2, Sparkles } from 'lucide-react';

// Code-splitting các tab học thuật và quản trị giúp tải nhanh và tối ưu tài nguyên
const LessonsTab = lazy(() => import('./features/LessonsTab').then((m) => ({ default: m.LessonsTab })));
const FormulasTab = lazy(() => import('./features/FormulasTab').then((m) => ({ default: m.FormulasTab })));
const PracticeTab = lazy(() => import('./features/PracticeTab').then((m) => ({ default: m.PracticeTab })));
const ExamsTab = lazy(() => import('./features/ExamsTab').then((m) => ({ default: m.ExamsTab })));
const ScholarshipTab = lazy(() => import('./features/ScholarshipTab').then((m) => ({ default: m.ScholarshipTab })));
const FlashcardsTab = lazy(() => import('./features/FlashcardsTab').then((m) => ({ default: m.FlashcardsTab })));
const AnalyticsTab = lazy(() => import('./features/AnalyticsTab').then((m) => ({ default: m.AnalyticsTab })));
const AdminLogin = lazy(() => import('./features/admin/AdminLogin').then((m) => ({ default: m.AdminLogin })));
const AdminDashboard = lazy(() => import('./features/admin/AdminDashboard').then((m) => ({ default: m.AdminDashboard })));
const AiTutorModal = lazy(() => import('./components/AiTutorModal').then((m) => ({ default: m.AiTutorModal })));

function TabLoadingFallback() {
  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        minHeight: '360px',
        gap: '14px',
        color: 'var(--text-secondary)',
        padding: '40px 20px',
      }}
    >
      <Loader2 size={36} className="animate-spin" color="var(--accent-primary)" />
      <span style={{ fontSize: '0.95rem', fontWeight: 500, color: 'var(--text-secondary)' }}>
        Đang tải phân hệ học thuật...
      </span>
    </div>
  );
}

export function App() {
  const [activeTab, setActiveTab] = useState<TabType>('lessons');

  // Quản lý trạng thái học sinh đăng nhập
  const [studentUser, setStudentUser] = useState<any>(() => {
    try {
      const saved = localStorage.getItem('aistem_student_user');
      return saved ? JSON.parse(saved) : null;
    } catch {
      return null;
    }
  });

  const [authModalOpen, setAuthModalOpen] = useState(false);
  const [authModalMode, setAuthModalMode] = useState<'login' | 'register'>('login');
  const [aiTutorOpen, setAiTutorOpen] = useState(false);

  const handleOpenAuth = (mode: 'login' | 'register' = 'login') => {
    setAuthModalMode(mode);
    setAuthModalOpen(true);
  };

  const handleStudentAuthSuccess = (user: any, token: string) => {
    try {
      localStorage.setItem('aistem_student_user', JSON.stringify(user));
      if (token) localStorage.setItem('aistem_student_token', token);
    } catch {
      // ignore
    }
    setStudentUser(user);
    setAuthModalOpen(false);
  };

  const handleStudentLogout = () => {
    localStorage.removeItem('aistem_student_user');
    localStorage.removeItem('aistem_student_token');
    setStudentUser(null);
  };

  // Quản lý route Admin (/admin hoặc #admin)
  const [isAdminRoute, setIsAdminRoute] = useState<boolean>(() => {
    return (
      window.location.pathname.startsWith('/admin') ||
      window.location.hash === '#admin' ||
      window.location.hash === '#/admin'
    );
  });

  const [adminUser, setAdminUser] = useState<any>(() => {
    try {
      const saved = localStorage.getItem('aistem_admin_auth');
      return saved ? JSON.parse(saved) : null;
    } catch {
      return null;
    }
  });

  useEffect(() => {
    const handleUrlChange = () => {
      const isAdm =
        window.location.pathname.startsWith('/admin') ||
        window.location.hash === '#admin' ||
        window.location.hash === '#/admin';
      setIsAdminRoute(isAdm);
    };

    window.addEventListener('popstate', handleUrlChange);
    window.addEventListener('hashchange', handleUrlChange);
    return () => {
      window.removeEventListener('popstate', handleUrlChange);
      window.removeEventListener('hashchange', handleUrlChange);
    };
  }, []);

  const navigateToAdmin = () => {
    setIsAdminRoute(true);
    window.history.pushState(null, '', '/admin');
  };

  const exitAdmin = () => {
    setIsAdminRoute(false);
    window.history.pushState(null, '', '/');
  };

  const handleLogout = () => {
    localStorage.removeItem('aistem_admin_auth');
    setAdminUser(null);
    exitAdmin();
  };

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Nếu đang ở cổng Admin */}
      {isAdminRoute ? (
        <main
          style={{
            flex: 1,
            maxWidth: '1360px',
            width: '100%',
            margin: '0 auto',
            padding: '24px 20px',
          }}
        >
          <Suspense fallback={<TabLoadingFallback />}>
            {adminUser ? (
              <AdminDashboard onLogout={handleLogout} onExit={exitAdmin} />
            ) : (
              <AdminLogin onSuccess={(user) => setAdminUser(user)} onCancel={exitAdmin} />
            )}
          </Suspense>
        </main>
      ) : (
        /* Giao diện Học sinh (Chưa đăng nhập -> Marketing Landing, Đã đăng nhập -> Dashboard Khóa Học) */
        <>
          {/* Top Navbar */}
          <Navbar
            activeTab={activeTab}
            onTabChange={setActiveTab}
            pgHealthy={true}
            studentUser={studentUser}
            onOpenStudentAuth={handleOpenAuth}
            onLogoutStudent={handleStudentLogout}
            onLogoClick={() => {
              if (studentUser) setActiveTab('lessons');
            }}
          />

          {/* Nội dung chính */}
          <main
            style={{
              flex: 1,
              maxWidth: '1360px',
              width: '100%',
              margin: '0 auto',
              padding: '28px 20px 80px',
            }}
          >
            {!studentUser ? (
              /* Khi chưa đăng nhập: Hiển thị Landing Marketing & Giới thiệu khóa học, nút Đăng nhập / Đăng ký */
              <MarketingHome onOpenAuth={handleOpenAuth} />
            ) : (
              /* Khi đã đăng nhập: Mở toàn bộ hệ sinh thái học tập & thi cử */
              <Suspense fallback={<TabLoadingFallback />}>
                {/* Banner giới thiệu nhẹ nhàng (chỉ hiển thị ở tab Bài học và có thể đóng) */}
                {activeTab === 'lessons' && <HeroShowcase onNavigateTab={setActiveTab} />}

                {/* Các phân hệ học tập & khảo thí */}
                {activeTab === 'lessons' && <LessonsTab />}
                {activeTab === 'formulas' && <FormulasTab />}
                {activeTab === 'practice' && <PracticeTab />}
                {activeTab === 'exams' && <ExamsTab />}
                {activeTab === 'scholarship' && <ScholarshipTab />}
                {activeTab === 'flashcards' && <FlashcardsTab />}
                {activeTab === 'analytics' && <AnalyticsTab />}
              </Suspense>
            )}
          </main>

          {/* Modal Đăng Nhập / Đăng Ký Học Viên */}
          {authModalOpen && (
            <StudentAuthModal
              initialMode={authModalMode}
              onClose={() => setAuthModalOpen(false)}
              onSuccess={handleStudentAuthSuccess}
            />
          )}
        </>
      )}

      {/* Footer chung với nút truy cập kín đáo cho Admin ở góc */}
      <footer
        style={{
          borderTop: '1px solid var(--border-subtle)',
          background: 'rgba(255, 255, 255, 0.95)',
          padding: '20px',
          marginTop: 'auto',
        }}
      >
        <div
          style={{
            maxWidth: '1360px',
            margin: '0 auto',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            flexWrap: 'wrap',
            gap: '16px',
            fontSize: '0.85rem',
            color: 'var(--text-secondary)',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <AistemXLogo variant="mark" size={24} />
            <span>
              <strong>AISTEM X</strong> — Hệ Tri Thức & AI Khoa Học Toàn Diện (aistemx.com)
            </span>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
            <span>Thiết kế tinh gọn cho học sinh & sinh viên STEM</span>
            <Heart size={13} color="#f43f5e" fill="#f43f5e" />
          </div>

          {/* Các chỉ số và Lối vào Admin kín đáo */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
            <span>PostgreSQL 16 (:5434)</span>
            <span>FastAPI CAS (:8000)</span>

            {/* Nút vào admin kín đáo ở footer */}
            {!isAdminRoute && (
              <button
                onClick={navigateToAdmin}
                style={{
                  background: 'none',
                  border: 'none',
                  color: 'var(--text-muted)',
                  fontSize: '0.78rem',
                  cursor: 'pointer',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '4px',
                  padding: '4px 8px',
                  borderRadius: 'var(--radius-sm)',
                  transition: 'color var(--transition-fast)',
                }}
                className="admin-discrete-btn"
                title="Cổng Đăng Nhập Quản Trị Viên (Hoặc truy cập tên_miền/admin)"
              >
                <Lock size={12} />
                <span>Quản Trị</span>
              </button>
            )}
          </div>
        </div>
      </footer>

      {/* Nút nổi Trợ Lý Gia Sư AI STEM (Cloudflare Workers AI) */}
      {!isAdminRoute && (
        <button
          type="button"
          onClick={() => setAiTutorOpen(true)}
          style={{
            position: 'fixed',
            bottom: '26px',
            right: '26px',
            zIndex: 850,
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            padding: '12px 18px',
            borderRadius: 'var(--radius-full)',
            background: 'linear-gradient(135deg, #0284c7, #6366f1)',
            color: '#ffffff',
            border: 'none',
            boxShadow: '0 8px 24px rgba(2, 132, 199, 0.4), 0 2px 6px rgba(0, 0, 0, 0.1)',
            cursor: 'pointer',
            fontWeight: 700,
            fontSize: '0.9rem',
            transition: 'all var(--transition-smooth)',
          }}
          className="pulse-glow"
          title="Mở Trợ lý Gia sư AI STEM (Hỏi đáp, giải bài & chứng minh)"
        >
          <Sparkles size={18} />
          <span>Gia Sư AI AISTEM X</span>
        </button>
      )}

      {/* Cửa sổ tương tác Gia sư AI */}
      {aiTutorOpen && (
        <Suspense fallback={null}>
          <AiTutorModal isOpen={aiTutorOpen} onClose={() => setAiTutorOpen(false)} />
        </Suspense>
      )}
    </div>
  );
}

export default App;
