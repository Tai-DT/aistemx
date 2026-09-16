import { useState, useEffect, type FC } from 'react';
import { Gift, Share2, ArrowRight, BookOpen, ShieldCheck, X } from 'lucide-react';
import { LeadGenModal } from './LeadGenModal';
import { ShareModal } from './ShareModal';

interface HeroShowcaseProps {
  onNavigateTab: (tab: any) => void;
}

export const HeroShowcase: FC<HeroShowcaseProps> = ({ onNavigateTab }) => {
  const [showLeadModal, setShowLeadModal] = useState(false);
  const [showShareModal, setShowShareModal] = useState(false);
  const [dismissed, setDismissed] = useState<boolean>(() => {
    try {
      return localStorage.getItem('aistem_hero_dismissed') === 'true';
    } catch {
      return false;
    }
  });

  const handleDismiss = () => {
    setDismissed(true);
    try {
      localStorage.setItem('aistem_hero_dismissed', 'true');
    } catch {
      // ignore
    }
  };

  useEffect(() => {
    // Allows user to restore banner if needed via event
    const handleReset = () => setDismissed(false);
    window.addEventListener('aistem_reset_hero', handleReset);
    return () => window.removeEventListener('aistem_reset_hero', handleReset);
  }, []);

  if (dismissed) {
    return (
      <>
        {showLeadModal && <LeadGenModal onClose={() => setShowLeadModal(false)} />}
        {showShareModal && <ShareModal onClose={() => setShowShareModal(false)} />}
      </>
    );
  }

  return (
    <>
      <div
        className="glass-panel animate-fade-in"
        style={{
          marginBottom: '20px',
          padding: '22px 26px',
          position: 'relative',
          borderRadius: 'var(--radius-lg)',
          background: 'linear-gradient(135deg, #f0f9ff 0%, #ffffff 60%, #ecfdf5 100%)',
          border: '1px solid #bae6fd',
          boxShadow: '0 4px 20px -2px rgba(15, 23, 42, 0.05)',
        }}
      >
        {/* Dismiss Button */}
        <button
          onClick={handleDismiss}
          style={{
            position: 'absolute',
            right: '14px',
            top: '14px',
            background: 'none',
            border: 'none',
            color: 'var(--text-muted)',
            cursor: 'pointer',
            padding: '4px',
            borderRadius: '50%',
          }}
          title="Thu gọn bảng chào mừng"
          aria-label="Thu gọn bảng chào mừng"
        >
          <X size={16} />
        </button>

        <div style={{ maxWidth: '820px' }}>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', marginBottom: '8px' }}>
            <span
              style={{
                fontSize: '0.75rem',
                fontWeight: 700,
                color: '#0369a1',
                background: '#e0f2fe',
                border: '1px solid #bae6fd',
                padding: '3px 10px',
                borderRadius: 'var(--radius-full)',
              }}
            >
              🌊 Khởi Nguồn Từ Nước H₂O • Vật Lý • Toán Học • Sinh Học
            </span>
          </div>

          <h2
            style={{
              fontSize: '1.5rem',
              fontWeight: 800,
              lineHeight: 1.3,
              marginBottom: '6px',
              color: '#0f172a',
            }}
          >
            Học STEM Từ Bản Chất Tự Nhiên — <span className="gradient-text">Từng Bước Vững Vàng</span>
          </h2>

          <p
            style={{
              color: 'var(--text-secondary)',
              fontSize: '0.9rem',
              lineHeight: 1.55,
              marginBottom: '16px',
              maxWidth: '720px',
            }}
          >
            Mọi quy luật khoa học đều liên kết chặt chẽ: từ cấu trúc phân tử nước H₂O, phương trình sóng cơ học, tỷ lệ vàng Fibonacci đến chuỗi xoắn kép DNA. Chọn chuyên đề để hệ thống tự động chỉ rõ kiến thức nền tảng cần nắm trước.
          </p>

          {/* Clean Action Buttons */}
          <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'center' }}>
            <button
              className="btn btn-primary"
              style={{ fontSize: '0.85rem', padding: '8px 16px', display: 'flex', alignItems: 'center', gap: '6px' }}
              onClick={() => {
                onNavigateTab('lessons');
                setTimeout(() => {
                  document.getElementById('curriculum-grid')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }, 80);
              }}
            >
              <BookOpen size={15} />
              <span>Xem Lộ Trình Bài Học</span>
              <ArrowRight size={13} />
            </button>

            <button
              className="btn btn-secondary"
              style={{ fontSize: '0.85rem', padding: '8px 16px', display: 'flex', alignItems: 'center', gap: '6px' }}
              onClick={() => onNavigateTab('practice')}
            >
              <ShieldCheck size={15} color="#06b6d4" />
              <span>Luyện Bài Tập</span>
            </button>

            <div style={{ marginLeft: 'auto', display: 'flex', gap: '8px' }}>
              <button
                className="btn btn-secondary"
                style={{ fontSize: '0.8rem', padding: '6px 12px', border: '1px solid rgba(245, 158, 11, 0.3)' }}
                onClick={() => setShowLeadModal(true)}
                title="Nhận cẩm nang tóm tắt công thức miễn phí"
              >
                <Gift size={14} color="#f59e0b" style={{ marginRight: '4px' }} />
                <span style={{ color: '#d97706', fontWeight: 600 }}>Cẩm Nang PDF</span>
              </button>

              <button
                className="btn btn-secondary"
                style={{ fontSize: '0.8rem', padding: '6px 12px' }}
                onClick={() => setShowShareModal(true)}
                title="Chia sẻ với bạn bè"
              >
                <Share2 size={14} style={{ marginRight: '4px' }} />
                <span>Chia Sẻ</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      {showLeadModal && <LeadGenModal onClose={() => setShowLeadModal(false)} />}
      {showShareModal && <ShareModal onClose={() => setShowShareModal(false)} />}
    </>
  );
};
