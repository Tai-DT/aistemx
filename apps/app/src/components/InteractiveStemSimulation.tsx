import { useState, useEffect, useRef, type FC } from 'react';
import { Waves, Atom, Dna, Compass, Play, Pause, RotateCcw } from 'lucide-react';

export type StemMode = 'water' | 'physics' | 'math' | 'biology';

export const InteractiveStemSimulation: FC = () => {
  const [activeMode, setActiveMode] = useState<StemMode>('water');
  const [isRunning, setIsRunning] = useState(true);
  
  // Simulation parameters
  const [paramValue, setParamValue] = useState(50); // General dynamic parameter (e.g. Temperature, Wave freq, Spiral growth)
  
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const animFrameId = useRef<number | null>(null);
  const timeRef = useRef<number>(0);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let width = (canvas.width = canvas.parentElement?.clientWidth || 600);
    let height = (canvas.height = 360);

    const handleResize = () => {
      if (!canvas || !canvas.parentElement) return;
      width = canvas.width = canvas.parentElement.clientWidth;
      height = canvas.height = 360;
    };
    window.addEventListener('resize', handleResize);

    const render = () => {
      if (isRunning) {
        timeRef.current += 0.03;
      }
      const t = timeRef.current;

      ctx.clearRect(0, 0, width, height);

      // Clean pristine light laboratory aquatic background
      const bgGrad = ctx.createRadialGradient(width / 2, height / 2, 20, width / 2, height / 2, width / 1.5);
      bgGrad.addColorStop(0, '#ffffff');
      bgGrad.addColorStop(1, '#f0f9ff');
      ctx.fillStyle = bgGrad;
      ctx.fillRect(0, 0, width, height);

      const cx = width / 2;
      const cy = height / 2;

      // MODE 1: NƯỚC & HÓA HỌC (H2O Molecule & Hydrogen Bonds)
      if (activeMode === 'water') {
        const temp = paramValue; // Temperature in Celsius: 0 (Ice) to 100 (Steam)
        const agitation = (temp / 100) * 12;

        // Subtle water grid / caustics
        ctx.strokeStyle = 'rgba(14, 165, 233, 0.08)';
        ctx.lineWidth = 1;
        for (let x = 0; x < width; x += 40) {
          ctx.beginPath();
          ctx.moveTo(x, 0);
          ctx.lineTo(x, height);
          ctx.stroke();
        }
        for (let y = 0; y < height; y += 40) {
          ctx.beginPath();
          ctx.moveTo(0, y);
          ctx.lineTo(width, y);
          ctx.stroke();
        }

        // Draw multiple ambient H2O molecules in background
        const moleculeCount = 6;
        for (let i = 0; i < moleculeCount; i++) {
          const angle = (i * Math.PI * 2) / moleculeCount + t * 0.2;
          const dist = 110 + Math.sin(t + i) * 15;
          const mx = cx + Math.cos(angle) * dist + (Math.random() - 0.5) * agitation * 0.3;
          const my = cy + Math.sin(angle) * dist + (Math.random() - 0.5) * agitation * 0.3;

          // Connecting dotted hydrogen bond
          ctx.beginPath();
          ctx.setLineDash([4, 4]);
          ctx.strokeStyle = 'rgba(56, 189, 248, 0.25)';
          ctx.lineWidth = 1.5;
          ctx.moveTo(cx, cy);
          ctx.lineTo(mx, my);
          ctx.stroke();
          ctx.setLineDash([]);

          // Mini H2O
          ctx.fillStyle = '#0284c7';
          ctx.beginPath();
          ctx.arc(mx, my, 8, 0, Math.PI * 2);
          ctx.fill();

          // Mini H atoms
          const h1x = mx - 10;
          const h1y = my + 7;
          const h2x = mx + 10;
          const h2y = my + 7;

          ctx.fillStyle = '#7dd3fc';
          ctx.beginPath();
          ctx.arc(h1x, h1y, 4, 0, Math.PI * 2);
          ctx.arc(h2x, h2y, 4, 0, Math.PI * 2);
          ctx.fill();
        }

        // Central Master H2O Molecule
        const oPulse = 28 + Math.sin(t * 2) * 2;
        const bondAngle = (104.5 * Math.PI) / 180; // 104.5 degrees
        const bondLength = 65;

        const h1x = cx - Math.sin(bondAngle / 2) * bondLength;
        const h1y = cy + Math.cos(bondAngle / 2) * bondLength + Math.sin(t * 3) * (agitation * 0.5);
        const h2x = cx + Math.sin(bondAngle / 2) * bondLength;
        const h2y = cy + Math.cos(bondAngle / 2) * bondLength + Math.cos(t * 3) * (agitation * 0.5);

        // Covalent Bonds with glowing gradient
        const bondGrad1 = ctx.createLinearGradient(cx, cy, h1x, h1y);
        bondGrad1.addColorStop(0, '#38bdf8');
        bondGrad1.addColorStop(1, '#bae6fd');
        ctx.beginPath();
        ctx.strokeStyle = bondGrad1;
        ctx.lineWidth = 6;
        ctx.lineCap = 'round';
        ctx.moveTo(cx, cy);
        ctx.lineTo(h1x, h1y);
        ctx.stroke();

        const bondGrad2 = ctx.createLinearGradient(cx, cy, h2x, h2y);
        bondGrad2.addColorStop(0, '#38bdf8');
        bondGrad2.addColorStop(1, '#bae6fd');
        ctx.beginPath();
        ctx.strokeStyle = bondGrad2;
        ctx.lineWidth = 6;
        ctx.lineCap = 'round';
        ctx.moveTo(cx, cy);
        ctx.lineTo(h2x, h2y);
        ctx.stroke();

        // Arc displaying 104.5°
        ctx.beginPath();
        ctx.arc(cx, cy, 32, Math.PI / 2 - bondAngle / 2, Math.PI / 2 + bondAngle / 2);
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = '#fde68a';
        ctx.font = '12px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('104.5°', cx, cy + 46);

        // Oxygen Nucleus (O)
        const oGrad = ctx.createRadialGradient(cx - 8, cy - 8, 4, cx, cy, oPulse);
        oGrad.addColorStop(0, '#7dd3fc');
        oGrad.addColorStop(0.6, '#0284c7');
        oGrad.addColorStop(1, '#0369a1');
        ctx.fillStyle = oGrad;
        ctx.beginPath();
        ctx.arc(cx, cy, oPulse, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 18px Outfit, sans-serif';
        ctx.textBaseline = 'middle';
        ctx.fillText('O', cx, cy);

        // Hydrogen Nuclei (H)
        [ [h1x, h1y], [h2x, h2y] ].forEach(([hx, hy]) => {
          const hGrad = ctx.createRadialGradient(hx - 4, hy - 4, 2, hx, hy, 16);
          hGrad.addColorStop(0, '#ffffff');
          hGrad.addColorStop(0.5, '#38bdf8');
          hGrad.addColorStop(1, '#0284c7');
          ctx.fillStyle = hGrad;
          ctx.beginPath();
          ctx.arc(hx, hy, 16, 0, Math.PI * 2);
          ctx.fill();

          ctx.fillStyle = '#ffffff';
          ctx.font = 'bold 14px Outfit, sans-serif';
          ctx.fillText('H', hx, hy);
        });

        // Legend tag in canvas
        ctx.textAlign = 'left';
        ctx.textBaseline = 'top';
        ctx.fillStyle = '#0284c7';
        ctx.font = '700 13px JetBrains Mono, monospace';
        ctx.fillText(`H₂O (Dung môi sự sống) • T = ${temp}°C`, 20, 20);
        ctx.fillStyle = '#475569';
        ctx.font = '12px Inter, sans-serif';
        ctx.fillText('Góc liên kết cộng hóa trị phân cực 104.5° & mạng lưới liên kết Hydro', 20, 40);
      }

      // MODE 2: VẬT LÝ — Sóng Cơ & Giao Thoa Nước (Wave Mechanics)
      else if (activeMode === 'physics') {
        const freq = (paramValue / 100) * 4 + 1; // Frequency

        // Dual Wave Sources (Interference Experiment: Thí nghiệm giao thoa 2 nguồn sóng nước S1, S2)
        const s1x = cx - 90;
        const s2x = cx + 90;
        const sy = cy;

        // Wave lines
        const rings = 14;
        for (let r = 1; r <= rings; r++) {
          const radius = ((r * 18 + t * freq * 15) % (rings * 18));
          const alpha = Math.max(0, 1 - radius / (rings * 18));

          // Wave from S1
          ctx.beginPath();
          ctx.arc(s1x, sy, radius, 0, Math.PI * 2);
          ctx.strokeStyle = `rgba(14, 165, 233, ${alpha * 0.4})`;
          ctx.lineWidth = 2;
          ctx.stroke();

          // Wave from S2
          ctx.beginPath();
          ctx.arc(s2x, sy, radius, 0, Math.PI * 2);
          ctx.strokeStyle = `rgba(16, 185, 129, ${alpha * 0.4})`;
          ctx.lineWidth = 2;
          ctx.stroke();
        }

        // Source pins
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(s1x, sy, 7, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#10b981';
        ctx.beginPath();
        ctx.arc(s2x, sy, 7, 0, Math.PI * 2);
        ctx.fill();

        // Wave equation sinusoidal trace at bottom
        ctx.beginPath();
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2.5;
        const waveY = height - 50;
        for (let x = 40; x < width - 40; x++) {
          const y = waveY + Math.sin((x * 0.04) - t * freq * 2) * 22;
          if (x === 40) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();

        ctx.textAlign = 'left';
        ctx.textBaseline = 'top';
        ctx.fillStyle = '#0284c7';
        ctx.font = '700 13px JetBrains Mono, monospace';
        ctx.fillText(`VẬT LÝ SÓNG: ψ(r, t) = 2A cos(πΔd/λ) • f = ${freq.toFixed(1)} Hz`, 20, 20);
        ctx.fillStyle = '#475569';
        ctx.font = '12px Inter, sans-serif';
        ctx.fillText('Giao thoa sóng nước 2 nguồn kết hợp S₁ & S₂ (Cực đại giao thoa: d₂ - d₁ = kλ)', 20, 40);
      }

      // MODE 3: TOÁN HỌC — Fibonacci Spiral & Tỷ Lệ Vàng
      else if (activeMode === 'math') {
        const phi = 1.6180339887;
        const scale = 0.5 + (paramValue / 100) * 0.8;

        // Draw Fibonacci squares & logarithmic golden spiral
        ctx.save();
        ctx.translate(cx - 30, cy + 20);
        ctx.scale(scale, scale);

        ctx.strokeStyle = 'rgba(56, 189, 248, 0.35)';
        ctx.lineWidth = 1.5;

        // Draw Spiral Curve
        ctx.beginPath();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3.5;
        for (let a = 0; a < Math.PI * 7; a += 0.05) {
          const r = 2.2 * Math.pow(phi, (2 * a) / Math.PI);
          const px = r * Math.cos(a + t * 0.3);
          const py = r * Math.sin(a + t * 0.3);
          if (a === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();

        ctx.restore();

        ctx.textAlign = 'left';
        ctx.textBaseline = 'top';
        ctx.fillStyle = '#0284c7';
        ctx.font = '700 13px JetBrains Mono, monospace';
        ctx.fillText('TOÁN HỌC: Xoắn Ốc Hoàng Gia Fibonacci • Φ = 1.618033...', 20, 20);
        ctx.fillStyle = '#475569';
        ctx.font = '12px Inter, sans-serif';
        ctx.fillText('Quy luật tỷ lệ vàng trong hình học giọt nước, bão nhiệt đới và dải ngân hà', 20, 40);
      }

      // MODE 4: SINH HỌC — Chuỗi Xoắn Kép DNA & Diệp Lục
      else if (activeMode === 'biology') {
        const dnaLength = 20;
        const spacing = 14;
        const amplitude = 55;

        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        const startX = cx - (dnaLength * spacing) / 2;

        for (let i = 0; i < dnaLength; i++) {
          const x = startX + i * spacing;
          const wavePhase = (i * 0.35) - t * 1.5;
          const y1 = cy + Math.sin(wavePhase) * amplitude;
          const y2 = cy - Math.sin(wavePhase) * amplitude;

          // Rung rơ kết nối cặp Base (A-T hoặc G-C)
          const isAT = i % 2 === 0;
          ctx.beginPath();
          ctx.strokeStyle = isAT ? 'rgba(56, 189, 248, 0.45)' : 'rgba(16, 185, 129, 0.45)';
          ctx.lineWidth = 3;
          ctx.moveTo(x, y1);
          ctx.lineTo(x, y2);
          ctx.stroke();

          // Nucleotide beads
          ctx.fillStyle = '#0ea5e9'; // Strand 1
          ctx.beginPath();
          ctx.arc(x, y1, 6, 0, Math.PI * 2);
          ctx.fill();

          ctx.fillStyle = '#10b981'; // Strand 2
          ctx.beginPath();
          ctx.arc(x, y2, 6, 0, Math.PI * 2);
          ctx.fill();
        }

        ctx.textAlign = 'left';
        ctx.textBaseline = 'top';
        ctx.fillStyle = '#059669';
        ctx.font = '700 13px JetBrains Mono, monospace';
        ctx.fillText('SINH HỌC: Chuỗi Xoắn Kép DNA (Watson & Crick) & Dung Môi Nước', 20, 20);
        ctx.fillStyle = '#475569';
        ctx.font = '12px Inter, sans-serif';
        ctx.fillText('Quang hợp tự nhiên: 6CO₂ + 6H₂O + Ánh Sáng → C₆H₁₂O₆ + 6O₂', 20, 40);
      }

      animFrameId.current = requestAnimationFrame(render);
    };

    animFrameId.current = requestAnimationFrame(render);

    return () => {
      if (animFrameId.current) cancelAnimationFrame(animFrameId.current);
      window.removeEventListener('resize', handleResize);
    };
  }, [activeMode, isRunning, paramValue]);

  return (
    <div
      className="glass-panel"
      style={{
        borderRadius: 'var(--radius-xl)',
        border: '1px solid #e2e8f0',
        overflow: 'hidden',
        background: '#ffffff',
        boxShadow: '0 8px 30px -4px rgba(15, 23, 42, 0.08)',
      }}
    >
      {/* Simulation Header & Mode Tabs */}
      <div
        style={{
          padding: '16px 20px',
          borderBottom: '1px solid #e2e8f0',
          background: '#f8fafc',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '12px',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <div
            style={{
              width: '10px',
              height: '10px',
              borderRadius: '50%',
              background: '#059669',
              boxShadow: '0 0 8px #059669',
            }}
          />
          <span style={{ fontSize: '0.9rem', fontWeight: 700, color: '#0f172a' }}>
            Phòng Thí Nghiệm Mô Phỏng Khoa Học Trực Quan
          </span>
        </div>

        {/* 4 STEM Field Switchers */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
          <button
            className={`btn ${activeMode === 'water' ? 'btn-primary' : 'btn-secondary'}`}
            style={{ fontSize: '0.8rem', padding: '6px 12px', gap: '5px' }}
            onClick={() => setActiveMode('water')}
          >
            <Atom size={14} />
            <span>1. Nước (H₂O)</span>
          </button>

          <button
            className={`btn ${activeMode === 'physics' ? 'btn-primary' : 'btn-secondary'}`}
            style={{ fontSize: '0.8rem', padding: '6px 12px', gap: '5px' }}
            onClick={() => setActiveMode('physics')}
          >
            <Waves size={14} />
            <span>2. Vật Lý (Sóng)</span>
          </button>

          <button
            className={`btn ${activeMode === 'math' ? 'btn-primary' : 'btn-secondary'}`}
            style={{ fontSize: '0.8rem', padding: '6px 12px', gap: '5px' }}
            onClick={() => setActiveMode('math')}
          >
            <Compass size={14} />
            <span>3. Toán (Fibonacci)</span>
          </button>

          <button
            className={`btn ${activeMode === 'biology' ? 'btn-primary' : 'btn-secondary'}`}
            style={{ fontSize: '0.8rem', padding: '6px 12px', gap: '5px' }}
            onClick={() => setActiveMode('biology')}
          >
            <Dna size={14} />
            <span>4. Sinh Học (DNA)</span>
          </button>
        </div>
      </div>

      {/* Canvas Display */}
      <div style={{ position: 'relative', width: '100%', height: '360px', overflow: 'hidden' }}>
        <canvas ref={canvasRef} style={{ width: '100%', height: '100%', display: 'block' }} />
      </div>

      {/* Interactive Controls Bar */}
      <div
        style={{
          padding: '14px 20px',
          borderTop: '1px solid #e2e8f0',
          background: '#f8fafc',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '16px',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px', flex: 1, minWidth: '240px' }}>
          <span style={{ fontSize: '0.8rem', color: '#475569', fontWeight: 600 }}>
            {activeMode === 'water' && 'Nhiệt độ (T°C):'}
            {activeMode === 'physics' && 'Tần số sóng (f):'}
            {activeMode === 'math' && 'Hệ số phóng đại (Scale):'}
            {activeMode === 'biology' && 'Tốc độ phiên mã (Rate):'}
          </span>
          <input
            type="range"
            min="10"
            max="100"
            value={paramValue}
            onChange={(e) => setParamValue(Number(e.target.value))}
            style={{
              flex: 1,
              maxWidth: '220px',
              accentColor: '#0284c7',
              cursor: 'pointer',
            }}
          />
          <span style={{ fontSize: '0.82rem', color: '#0284c7', fontWeight: 700, minWidth: '40px' }}>
            {paramValue}
          </span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <button
            className="btn btn-secondary"
            style={{ fontSize: '0.8rem', padding: '6px 12px', gap: '4px' }}
            onClick={() => setIsRunning(!isRunning)}
          >
            {isRunning ? <Pause size={14} /> : <Play size={14} />}
            <span>{isRunning ? 'Tạm Dừng' : 'Tiếp Tục'}</span>
          </button>

          <button
            className="btn btn-secondary"
            style={{ fontSize: '0.8rem', padding: '6px 12px', gap: '4px' }}
            onClick={() => {
              setParamValue(50);
              timeRef.current = 0;
            }}
          >
            <RotateCcw size={14} />
            <span>Đặt Lại</span>
          </button>
        </div>
      </div>
    </div>
  );
};
