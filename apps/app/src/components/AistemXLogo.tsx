import { type FC } from 'react';

interface AistemXLogoProps {
  variant?: 'mark' | 'full' | 'squircle';
  size?: number;
  className?: string;
  showTagline?: boolean;
}

export const AistemXLogo: FC<AistemXLogoProps> = ({
  variant = 'full',
  size = 40,
  className = '',
  showTagline = true,
}) => {
  const isSquircle = variant === 'squircle';

  const markSvg = (
    <svg
      width={size}
      height={size}
      viewBox="0 0 120 120"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      style={{ display: 'block', flexShrink: 0 }}
      aria-label="AISTEM X — Nền tảng Khoa học & AI STEM Quốc tế"
    >
      <defs>
        {/* Beam 1: AI & Math Logic (Royal Blue -> Electric Cyan) */}
        <linearGradient id="ax-beam-blue" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#1e3a8a" />
          <stop offset="30%" stopColor="#2563eb" />
          <stop offset="70%" stopColor="#0284c7" />
          <stop offset="100%" stopColor="#38bdf8" />
        </linearGradient>

        {/* Beam 2: Life Science & Energy (Emerald Green -> Aurora Teal) */}
        <linearGradient id="ax-beam-emerald" x1="100%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stopColor="#065f46" />
          <stop offset="35%" stopColor="#059669" />
          <stop offset="75%" stopColor="#10b981" />
          <stop offset="100%" stopColor="#34d399" />
        </linearGradient>

        {/* Core Quantum Spark (Gold -> Sun Amber) */}
        <linearGradient id="ax-spark" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#fef08a" />
          <stop offset="40%" stopColor="#f59e0b" />
          <stop offset="100%" stopColor="#d97706" />
        </linearGradient>

        {/* Orbit Path Gradient */}
        <linearGradient id="ax-orbit" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#38bdf8" stopOpacity="0.8" />
          <stop offset="50%" stopColor="#818cf8" stopOpacity="0.4" />
          <stop offset="100%" stopColor="#34d399" stopOpacity="0.8" />
        </linearGradient>

        {/* Dark Obsidian Squircle Canvas */}
        <linearGradient id="ax-squircle-bg" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#0b1329" />
          <stop offset="50%" stopColor="#0f172a" />
          <stop offset="100%" stopColor="#020617" />
        </linearGradient>

        {/* Glow Filter */}
        <filter id="ax-glow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="2.5" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
      </defs>

      {/* --- SQUIRCLE BACKGROUND (For App Icon & Favicon) --- */}
      {isSquircle && (
        <g>
          <rect
            x="4"
            y="4"
            width="112"
            height="112"
            rx="28"
            fill="url(#ax-squircle-bg)"
            stroke="#0284c7"
            strokeWidth="1.8"
            strokeOpacity="0.4"
          />
          {/* Ambient Specular Highlight */}
          <circle cx="60" cy="60" r="38" fill="#0284c7" fillOpacity="0.12" filter="url(#ax-glow)" />
        </g>
      )}

      {/* --- SCIENCE ORBITAL ELLIPSE (Vật Lý & Thiên Văn Học) --- */}
      <g opacity={isSquircle ? 0.95 : 0.85}>
        <ellipse
          cx="60"
          cy="60"
          rx="48"
          ry="17"
          transform="rotate(-28 60 60)"
          stroke="url(#ax-orbit)"
          strokeWidth="2.2"
          strokeDasharray="4 2"
          strokeLinecap="round"
        />
        {/* Orbital Quantum Nodes (Electron / Particle) */}
        <circle cx="21" cy="40" r="3.2" fill="#38bdf8" filter="url(#ax-glow)" />
        <circle cx="99" cy="80" r="3.2" fill="#34d399" filter="url(#ax-glow)" />
      </g>

      {/* --- ICONIC FUTURISTIC 'X' ARCHITECTURE --- */}
      <g filter="url(#ax-glow)">
        {/* Main Beam 1 (Top-Left to Bottom-Right): Logic, Mathematics & AI */}
        <path
          d="M26 24 L38 20 L94 96 L82 100 Z"
          fill="url(#ax-beam-blue)"
          stroke={isSquircle ? '#38bdf8' : 'none'}
          strokeWidth="0.5"
        />

        {/* Main Beam 2 (Top-Right to Bottom-Left): Life Sciences & Chemistry */}
        <path
          d="M94 24 L82 20 L26 96 L38 100 Z"
          fill="url(#ax-beam-emerald)"
          stroke={isSquircle ? '#34d399' : 'none'}
          strokeWidth="0.5"
        />

        {/* Overlapping Quantum Nexus Intersect */}
        <path
          d="M52 52 L68 52 L60 68 Z"
          fill="url(#ax-beam-blue)"
          opacity="0.85"
        />

        {/* Central Brilliant AI Core Spark (Bản chất Trí tuệ Nhân tạo & Sáng tạo) */}
        <path
          d="M60 49 L62.8 57.2 L71 60 L62.8 62.8 L60 71 L57.2 62.8 L49 60 L57.2 57.2 Z"
          fill="url(#ax-spark)"
        />
        <circle cx="60" cy="60" r="2.2" fill="#ffffff" />
      </g>
    </svg>
  );

  if (variant === 'mark' || variant === 'squircle') {
    return markSvg;
  }

  // Full Horizontal Brand Lockup
  return (
    <div
      className={`aistemx-brand-lockup ${className}`}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: `${Math.max(8, Math.round(size * 0.28))}px`,
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
            fontSize: `${Math.max(17, Math.round(size * 0.54))}px`,
            fontWeight: 800,
            letterSpacing: '-0.035em',
            lineHeight: 1.1,
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
            fontFamily: "'Outfit', var(--font-sans)",
          }}
        >
          <span
            style={{
              color: '#0f172a',
              fontWeight: 800,
            }}
          >
            AISTEM
          </span>
          <span
            style={{
              background: 'linear-gradient(135deg, #0284c7 0%, #6366f1 60%, #10b981 100%)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              fontWeight: 900,
              fontSize: `${Math.max(20, Math.round(size * 0.62))}px`,
              marginLeft: '-1px',
            }}
          >
            X
          </span>
          <span
            style={{
              fontSize: `${Math.max(9, Math.round(size * 0.2))}px`,
              fontWeight: 700,
              padding: '2px 6px',
              borderRadius: '6px',
              background: '#e0f2fe',
              border: '1px solid #bae6fd',
              color: '#0369a1',
              letterSpacing: '0.04em',
              textTransform: 'uppercase',
              marginLeft: '3px',
            }}
          >
            .COM
          </span>
        </div>

        {showTagline && (
          <div
            style={{
              fontSize: `${Math.max(9, Math.round(size * 0.2))}px`,
              color: '#64748b',
              fontWeight: 600,
              letterSpacing: '0.04em',
              marginTop: '2px',
              textTransform: 'uppercase',
            }}
          >
            KHOA HỌC • TOÁN HỌC • TRÍ TUỆ NHÂN TẠO
          </div>
        )}
      </div>
    </div>
  );
};
