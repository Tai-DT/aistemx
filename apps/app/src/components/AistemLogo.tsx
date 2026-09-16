import { type FC } from 'react';

interface AistemLogoProps {
  variant?: 'mark' | 'full' | 'squircle';
  size?: number;
  className?: string;
  showTagline?: boolean;
}

export const AistemLogo: FC<AistemLogoProps> = ({
  variant = 'mark',
  size = 40,
  className = '',
  showTagline = true,
}) => {
  const isSquircle = variant === 'squircle';

  const markSvg = (
    <svg
      width={size}
      height={size}
      viewBox="0 0 100 100"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      style={{ display: 'block', flexShrink: 0 }}
      aria-label="AISTEM — Biểu tượng Khởi nguồn từ Nước H2O, Toán học, Vật lý và Sinh học"
    >
      <defs>
        {/* H2O Water & Physics Wave Gradient */}
        <linearGradient id="h2o-water-grad" x1="20%" y1="0%" x2="80%" y2="100%">
          <stop offset="0%" stopColor="#38bdf8" />
          <stop offset="50%" stopColor="#0ea5e9" />
          <stop offset="100%" stopColor="#0284c7" />
        </linearGradient>

        {/* Biology DNA & Chlorophyll Life Gradient */}
        <linearGradient id="h2o-bio-grad" x1="0%" y1="100%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="#059669" />
          <stop offset="50%" stopColor="#10b981" />
          <stop offset="100%" stopColor="#34d399" />
        </linearGradient>

        {/* Sunlight & Energy Gradient */}
        <linearGradient id="h2o-sun-grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#fef08a" />
          <stop offset="50%" stopColor="#f59e0b" />
          <stop offset="100%" stopColor="#d97706" />
        </linearGradient>

        {/* Deep Ocean Abyssal Squircle Background */}
        <linearGradient id="h2o-ocean-bg" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#0c1f38" />
          <stop offset="50%" stopColor="#071322" />
          <stop offset="100%" stopColor="#030811" />
        </linearGradient>

        {/* Water Fluid Glow Filter */}
        <filter id="h2o-glow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="2.5" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
      </defs>

      {/* Optional iOS Squircle Container */}
      {isSquircle && (
        <>
          <rect
            x="2"
            y="2"
            width="96"
            height="96"
            rx="24"
            fill="url(#h2o-ocean-bg)"
            stroke="rgba(14, 165, 233, 0.35)"
            strokeWidth="1.5"
          />
          {/* Subtle Caustic Ocean Light */}
          <circle cx="50" cy="30" r="30" fill="rgba(14, 165, 233, 0.18)" filter="url(#h2o-glow)" />
        </>
      )}

      <g filter="url(#h2o-glow)">
        {/* 1. VẬT LÝ — Các vòng sóng lan truyền (Harmonic Wave Ripples λ = v/f) */}
        <path
          d="M20 68 A32 32 0 0 0 80 68"
          stroke="url(#h2o-water-grad)"
          strokeWidth="1.8"
          strokeLinecap="round"
          strokeDasharray="2 3"
          opacity="0.5"
        />
        <path
          d="M14 68 A38 38 0 0 0 86 68"
          stroke="url(#h2o-water-grad)"
          strokeWidth="1.4"
          strokeLinecap="round"
          opacity="0.35"
        />

        {/* 2. TOÁN HỌC & NƯỚC — Giọt nước theo đường xoắn ốc Fibonacci (Golden Ratio Water Droplet) */}
        <path
          d="M50 14 C50 14, 25 46, 25 66 A25 25 0 0 0 75 66 C75 46, 50 14, 50 14 Z"
          stroke="url(#h2o-water-grad)"
          strokeWidth="3.4"
          strokeLinecap="round"
          strokeLinejoin="round"
          fill="rgba(14, 165, 233, 0.08)"
        />

        {/* Đường xoắn Fibonacci nội tại (Toán học giải tích dòng chảy) */}
        <path
          d="M50 18 C38 36, 32 50, 36 65 C40 80, 60 78, 64 68 C68 58, 56 50, 48 56 C44 60, 46 66, 50 66"
          stroke="url(#h2o-water-grad)"
          strokeWidth="1.6"
          strokeLinecap="round"
          opacity="0.55"
        />

        {/* 3. HÓA HỌC & VẬT LÝ — Cấu trúc phân tử NƯỚC H2O (Góc liên kết 104.5°) */}
        {/* Liên kết Hydro-Oxy trái */}
        <line x1="50" y1="46" x2="40" y2="57" stroke="url(#h2o-water-grad)" strokeWidth="2.8" strokeLinecap="round" />
        {/* Liên kết Hydro-Oxy phải */}
        <line x1="50" y1="46" x2="60" y2="57" stroke="url(#h2o-water-grad)" strokeWidth="2.8" strokeLinecap="round" />
        
        {/* Nguyên tử O (Oxygen) ở tâm */}
        <circle cx="50" cy="45" r="5" fill="#38bdf8" stroke="#0284c7" strokeWidth="1.5" />
        <circle cx="48.5" cy="43.5" r="1.5" fill="#ffffff" opacity="0.8" />

        {/* Nguyên tử H1 (Hydrogen) bên trái */}
        <circle cx="39" cy="58" r="3.6" fill="#7dd3fc" stroke="#0284c7" strokeWidth="1.2" />

        {/* Nguyên tử H2 (Hydrogen) bên phải */}
        <circle cx="61" cy="58" r="3.6" fill="#7dd3fc" stroke="#0284c7" strokeWidth="1.2" />

        {/* 4. SINH HỌC — Chuỗi xoắn kép DNA & Mầm lá xanh (Sự sống khởi sinh từ Nước) */}
        {/* Trục chuỗi xoắn DNA vươn lên từ đáy giọt nước */}
        <path
          d="M45 74 Q50 68 55 64 Q50 60 45 56"
          stroke="url(#h2o-bio-grad)"
          strokeWidth="2.2"
          strokeLinecap="round"
        />
        <path
          d="M55 74 Q50 68 45 64 Q50 60 55 56"
          stroke="url(#h2o-bio-grad)"
          strokeWidth="2.2"
          strokeLinecap="round"
        />
        {/* Bậc thang liên kết base DNA */}
        <line x1="47" y1="71" x2="53" y2="71" stroke="url(#h2o-bio-grad)" strokeWidth="1.4" opacity="0.8" />
        <line x1="46" y1="64" x2="54" y2="64" stroke="url(#h2o-bio-grad)" strokeWidth="1.4" opacity="0.8" />

        {/* Mầm lá quang hợp (Chlorophyll leaf) nảy sinh từ giọt nước */}
        <path
          d="M56 62 C63 60, 68 54, 66 48 C60 49, 56 56, 56 62 Z"
          fill="url(#h2o-bio-grad)"
          opacity="0.95"
        />
        <path
          d="M44 66 C38 64, 34 58, 36 53 C41 54, 44 60, 44 66 Z"
          fill="url(#h2o-bio-grad)"
          opacity="0.85"
        />

        {/* 5. NĂNG LƯỢNG MẶT TRỜI / QUANG HỢP — Tia sáng hội tụ đỉnh giọt nước */}
        <path
          d="M50 8 L51.5 12 L55.5 13.5 L51.5 15 L50 19 L48.5 15 L44.5 13.5 L48.5 12 Z"
          fill="url(#h2o-sun-grad)"
        />
      </g>
    </svg>
  );

  if (variant === 'mark' || variant === 'squircle') {
    return markSvg;
  }

  // Full Horizontal Brand Lockup
  return (
    <div
      className={`aistem-brand-lockup ${className}`}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: `${Math.max(8, Math.round(size * 0.26))}px`,
        userSelect: 'none',
        cursor: 'pointer',
      }}
    >
      <div
        style={{
          width: `${size}px`,
          height: `${size}px`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          position: 'relative',
        }}
      >
        {markSvg}
      </div>

      <div>
        <div
          style={{
            fontSize: `${Math.max(16, Math.round(size * 0.52))}px`,
            fontWeight: 800,
            letterSpacing: '-0.035em',
            lineHeight: 1.1,
            display: 'flex',
            alignItems: 'center',
            gap: '5px',
          }}
        >
          <span
            style={{
              background: 'linear-gradient(135deg, #0369a1 0%, #0284c7 45%, #059669 100%)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
            }}
          >
            AISTEM
          </span>
          <span
            style={{
              fontSize: `${Math.max(9, Math.round(size * 0.22))}px`,
              fontWeight: 700,
              padding: '2px 6px',
              borderRadius: '6px',
              background: '#e0f2fe',
              border: '1px solid #bae6fd',
              color: '#0369a1',
              letterSpacing: '0.04em',
              textTransform: 'uppercase',
            }}
          >
            H₂O • STEM
          </span>
        </div>

        {showTagline && (
          <div
            style={{
              fontSize: `${Math.max(9, Math.round(size * 0.22))}px`,
              color: '#475569',
              fontWeight: 600,
              letterSpacing: '0.05em',
              marginTop: '1px',
              textTransform: 'uppercase',
            }}
          >
            VẬT LÝ • TOÁN HỌC • SINH HỌC TỰ NHIÊN
          </div>
        )}
      </div>
    </div>
  );
};
