import { useState, type FC } from 'react';
import { createPortal } from 'react-dom';
import type { Formula } from '../../services/api';
import { MathView } from '../../components/MathView';
import { InteractiveFormulaDemo } from '../../components/InteractiveFormulaDemo';
import { X, Copy, Check, BookOpen, Sparkles } from 'lucide-react';

interface FormulaModalProps {
  formula: Formula;
  onClose: () => void;
}

export const FormulaModal: FC<FormulaModalProps> = ({ formula, onClose }) => {
  const [copied, setCopied] = useState(false);

  const handleCopyLatex = () => {
    if (formula.latex) {
      navigator.clipboard.writeText(formula.latex);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  return createPortal(
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        width: '100vw',
        height: '100vh',
        zIndex: 9999,
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
          maxWidth: '780px',
          maxHeight: '92vh',
          overflowY: 'auto',
          padding: '30px 28px',
          borderRadius: 'var(--radius-lg)',
          background: '#ffffff',
          border: '1px solid #bae6fd',
          boxShadow: '0 20px 40px -10px rgba(15, 23, 42, 0.15)',
          position: 'relative',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '16px', marginBottom: '20px' }}>
          <div>
            <div style={{ display: 'flex', gap: '8px', marginBottom: '8px', flexWrap: 'wrap', alignItems: 'center' }}>
              <span className="badge badge-indigo">
                {formula.subject === 'math'
                  ? 'Toán Học'
                  : formula.subject === 'physics'
                  ? 'Vật Lí'
                  : formula.subject === 'chemistry'
                  ? 'Hoá Học'
                  : formula.subject === 'biology'
                  ? 'Sinh Học'
                  : (formula.subject || '').toUpperCase()}
              </span>
              {formula.level && <span className="badge badge-emerald">Lớp {formula.level}</span>}
              {formula.id && <span style={{ fontSize: '0.76rem', color: 'var(--text-muted)' }}>#{formula.id}</span>}
            </div>
            <h3 style={{ fontSize: '1.5rem', fontWeight: 800, lineHeight: 1.3, color: '#0f172a' }}>
              {formula.name_vi || formula.name}
            </h3>
            {formula.name_en && (
              <div style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', fontStyle: 'italic', marginTop: '2px' }}>
                {formula.name_en}
              </div>
            )}
          </div>
          <button
            className="btn btn-secondary"
            style={{ padding: '8px', borderRadius: '50%' }}
            onClick={onClose}
            aria-label="Đóng"
          >
            <X size={20} />
          </button>
        </div>

        {/* Big LaTeX Equation Display */}
        <div
          style={{
            padding: '24px 20px',
            background: '#f8fafc',
            borderRadius: 'var(--radius-md)',
            border: '1px solid #e2e8f0',
            textAlign: 'center',
            marginBottom: '20px',
            overflowX: 'auto',
          }}
        >
          <div style={{ fontSize: '1.4rem', color: 'var(--text-primary)' }}>
            <MathView latex={formula.latex} block />
          </div>

          <div style={{ display: 'flex', justifyContent: 'center', gap: '10px', marginTop: '16px' }}>
            <button
              className="btn btn-secondary"
              style={{ fontSize: '0.8rem', padding: '6px 14px' }}
              onClick={handleCopyLatex}
            >
              {copied ? <Check size={14} color="#059669" /> : <Copy size={14} />}
              <span>{copied ? 'Đã chép mã LaTeX!' : 'Sao chép mã LaTeX'}</span>
            </button>
          </div>
        </div>

        {/* Interactive Visual Simulation */}
        <div style={{ marginBottom: '24px' }}>
          <InteractiveFormulaDemo formula={formula} />
        </div>

        {/* Description / Explanation */}
        {(formula.description || formula.description_vi) && (
          <div style={{ marginBottom: '22px' }}>
            <h4 style={{ fontSize: '0.98rem', fontWeight: 700, color: '#0f172a', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '6px' }}>
              <BookOpen size={16} color="#0284c7" />
              <span>Ý nghĩa và Bản chất Khoa học</span>
            </h4>
            <p style={{ color: 'var(--text-primary)', lineHeight: 1.65, fontSize: '0.92rem' }}>
              {formula.description || formula.description_vi}
            </p>
          </div>
        )}

        {/* Variables Breakdown Table */}
        {formula.variables && Object.keys(formula.variables).length > 0 && (
          <div style={{ marginBottom: '24px' }}>
            <h4 style={{ fontSize: '0.98rem', fontWeight: 700, color: '#0f172a', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
              <Sparkles size={16} color="#059669" />
              <span>Đại Lượng & Đơn Vị Đo Chuẩn SI</span>
            </h4>
            <div style={{ border: '1px solid #e2e8f0', borderRadius: 'var(--radius-md)', overflow: 'hidden' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.88rem' }}>
                <thead>
                  <tr style={{ background: '#f1f5f9', borderBottom: '1px solid #e2e8f0', textAlign: 'left' }}>
                    <th style={{ padding: '10px 14px', width: '25%', color: '#334155' }}>Ký hiệu</th>
                    <th style={{ padding: '10px 14px', width: '50%', color: '#334155' }}>Tên đại lượng</th>
                    <th style={{ padding: '10px 14px', width: '25%', color: '#334155' }}>Đơn vị SI</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(formula.variables).map(([key, val], idx) => {
                    const info: { name?: string; unit?: string } =
                      typeof val === 'object' && val !== null ? (val as { name?: string; unit?: string }) : { name: String(val), unit: '' };
                    return (
                      <tr key={key} style={{ borderBottom: idx < Object.keys(formula.variables!).length - 1 ? '1px solid #f1f5f9' : 'none', background: idx % 2 === 0 ? '#ffffff' : '#f8fafc' }}>
                        <td style={{ padding: '10px 14px', fontFamily: 'monospace', color: '#0284c7', fontWeight: 700 }}>
                          <MathView latex={key} />
                        </td>
                        <td style={{ padding: '10px 14px', color: '#1e293b' }}>{info.name || key}</td>
                        <td style={{ padding: '10px 14px', color: 'var(--text-secondary)', fontWeight: 500 }}>{info.unit || '—'}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>
    </div>,
    document.body
  );
};
