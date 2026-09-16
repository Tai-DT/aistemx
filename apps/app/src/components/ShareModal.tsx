import { useState, type FC } from 'react';
import { X, Share2, Copy, Check, MessageSquare, Globe, Send } from 'lucide-react';

interface ShareModalProps {
  onClose: () => void;
  title?: string;
  url?: string;
}

export const ShareModal: FC<ShareModalProps> = ({
  onClose,
  title = 'AISTEM — Nền Tảng Học Thuật STEM & Săn Học Bổng Toàn Cầu',
  url = typeof window !== 'undefined' ? window.location.href : 'https://aistem.edu.vn',
}) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(url);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const shareFacebook = () => {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`, '_blank');
  };

  const shareTwitter = () => {
    const text = `Khám phá ${title} với 5,272 công thức, 4,351 bài toán CAS và 25 học bổng quốc tế!`;
    window.open(`https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`, '_blank');
  };

  const shareZalo = () => {
    window.open(`https://sp.zalo.me/share_inline?url=${encodeURIComponent(url)}`, '_blank');
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
          maxWidth: '460px',
          padding: '28px 24px',
          borderRadius: 'var(--radius-lg)',
          background: '#ffffff',
          border: '1px solid #e2e8f0',
          boxShadow: '0 20px 40px -10px rgba(15, 23, 42, 0.15)',
          position: 'relative',
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

        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '16px' }}>
          <div
            style={{
              width: '40px',
              height: '40px',
              borderRadius: '12px',
              background: 'linear-gradient(135deg, #06b6d4 0%, #6366f1 100%)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            <Share2 size={20} color="#fff" />
          </div>
          <div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 700 }}>Chia Sẻ Với Bạn Bè</h3>
            <p style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
              Lan tỏa tài liệu học tập chuẩn quốc tế tới cộng đồng
            </p>
          </div>
        </div>

        {/* Social Share Buttons */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px', marginBottom: '20px' }}>
          <button
            className="btn btn-secondary"
            style={{ display: 'flex', flexDirection: 'column', gap: '6px', padding: '14px 10px', fontSize: '0.8rem' }}
            onClick={shareFacebook}
          >
            <Globe size={22} color="#1877f2" />
            <span>Facebook</span>
          </button>

          <button
            className="btn btn-secondary"
            style={{ display: 'flex', flexDirection: 'column', gap: '6px', padding: '14px 10px', fontSize: '0.8rem' }}
            onClick={shareZalo}
          >
            <MessageSquare size={22} color="#0068ff" />
            <span>Zalo</span>
          </button>

          <button
            className="btn btn-secondary"
            style={{ display: 'flex', flexDirection: 'column', gap: '6px', padding: '14px 10px', fontSize: '0.8rem' }}
            onClick={shareTwitter}
          >
            <Send size={22} color="#06b6d4" />
            <span>X / Telegram</span>
          </button>
        </div>

        {/* Copy Link Bar */}
        <div>
          <label style={{ display: 'block', fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '6px' }}>
            Hoặc sao chép liên kết trực tiếp:
          </label>
          <div style={{ display: 'flex', gap: '8px' }}>
            <input
              type="text"
              readOnly
              value={url}
              className="input-field"
              style={{ fontSize: '0.85rem', padding: '10px 12px' }}
            />
            <button className="btn btn-primary" onClick={handleCopy} style={{ flexShrink: 0 }}>
              {copied ? <Check size={16} /> : <Copy size={16} />}
              <span>{copied ? 'Đã Chép' : 'Chép Link'}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
