import { useState, useEffect, useCallback } from 'react';
import { api, type Formula } from '../services/api';
import { MathView } from '../components/MathView';
import { Pagination } from '../components/Pagination';
import { FormulaModal } from './formulas/FormulaModal';
import { Search, BookOpen, Sparkles, Copy, Check, Eye } from 'lucide-react';

export const FormulasTab = () => {
  const [formulas, setFormulas] = useState<Formula[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(true);
  const [subject, setSubject] = useState<string>('');
  const [level, setLevel] = useState<string>('');
  const [query, setQuery] = useState('');
  const [illusFilter, setIllusFilter] = useState<'all' | 'has_illus' | 'no_illus'>('all');
  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 24;

  const [selectedFormula, setSelectedFormula] = useState<Formula | null>(null);
  const [copiedId, setCopiedId] = useState<string | null>(null);

  const loadFormulas = useCallback(async (pageToLoad = 1) => {
    setLoading(true);
    try {
      const data = await api.getFormulas({
        subject: subject || undefined,
        level: level || undefined,
        q: query.trim() || undefined,
        has_illustration: illusFilter === 'has_illus' ? true : illusFilter === 'no_illus' ? false : undefined,
        page: pageToLoad,
        page_size: pageSize,
      });
      setFormulas(data.formulas || []);
      setTotal(data.total || 0);
      setCurrentPage(pageToLoad);
    } catch (e) {
      console.error('Lỗi nạp công thức:', e);
    } finally {
      setLoading(false);
    }
  }, [subject, level, query, illusFilter]);

  useEffect(() => {
    loadFormulas(1);
  }, [subject, level, illusFilter]);

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    loadFormulas(1);
  };

  const handleCopyLatex = (e: React.MouseEvent, f: Formula) => {
    e.stopPropagation();
    if (f.latex) {
      navigator.clipboard.writeText(f.latex);
      setCopiedId(f.id);
      setTimeout(() => setCopiedId(null), 2000);
    }
  };

  const handleOpenDetail = async (f: Formula) => {
    try {
      // Fetch full formula detail with vars, description, usage
      const res = await fetch(`/api/formulas/${f.id}`);
      if (res.ok) {
        const full = await res.json();
        setSelectedFormula(full);
        return;
      }
    } catch {
      // fallback
    }
    setSelectedFormula(f);
  };

  const subjectPills = [
    { id: '', label: 'Tất cả môn' },
    { id: 'math', label: 'Toán Học', color: '#6366f1' },
    { id: 'physics', label: 'Vật Lí', color: '#06b6d4' },
    { id: 'chemistry', label: 'Hoá Học', color: '#10b981' },
    { id: 'biology', label: 'Sinh Học', color: '#ec4899' },
  ];

  const totalPages = Math.ceil(total / pageSize);

  return (
    <div className="tab-container animate-fade-in">
      {/* Header & Filter Bar */}
      <div className="glass-panel" style={{ padding: '24px', marginBottom: '24px' }}>
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            flexWrap: 'wrap',
            gap: '16px',
            marginBottom: '20px',
          }}
        >
          <div>
            <h2 style={{ fontSize: '1.5rem', display: 'flex', alignItems: 'center', gap: '10px' }}>
              <BookOpen style={{ color: '#6366f1' }} />
              <span>Sổ Tay Công Thức</span>
            </h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.88rem', marginTop: '4px' }}>
              Tra cứu nhanh công thức Toán, Lí, Hoá, Sinh kèm máy tính biến số tương tác.
            </p>
          </div>
          <div className="badge badge-indigo">
            <Sparkles size={14} />
            <span>Tra cứu & tính toán</span>
          </div>
        </div>

        {/* Quick Subject Tabs */}
        <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '16px' }}>
          {subjectPills.map((pill) => (
            <button
              key={pill.id}
              className={`btn ${subject === pill.id ? 'btn-primary' : 'btn-secondary'}`}
              style={{
                fontSize: '0.85rem',
                padding: '6px 14px',
                borderRadius: 'var(--radius-full)',
              }}
              onClick={() => {
                setSubject(pill.id);
                setCurrentPage(1);
              }}
            >
              {pill.label}
            </button>
          ))}
        </div>

        {/* Search & Filters */}
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
            gap: '12px',
          }}
        >
          <form onSubmit={handleSearchSubmit} style={{ display: 'flex', gap: '8px', gridColumn: 'span 2' }}>
            <div style={{ position: 'relative', flex: 1 }}>
              <Search
                size={18}
                style={{
                  position: 'absolute',
                  left: '14px',
                  top: '50%',
                  transform: 'translateY(-50%)',
                  color: 'var(--text-muted)',
                }}
              />
              <input
                type="text"
                placeholder="Tìm công thức (ví dụ: Bernoulli, Schrödinger, Coulomb, Đạo hàm, Hô hấp...)"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                className="input-field"
                style={{ paddingLeft: '40px' }}
              />
            </div>
            <button type="submit" className="btn btn-primary" style={{ padding: '0 20px' }}>
              Tìm
            </button>
          </form>

          <select
            value={level}
            onChange={(e) => {
              setLevel(e.target.value);
              setCurrentPage(1);
            }}
            className="input-field"
            style={{ cursor: 'pointer' }}
          >
            <option value="">Tất cả cấp độ</option>
            <option value="tieu-hoc">Tiểu học (Lớp 1 - 5)</option>
            <option value="thcs">THCS (Lớp 6 - 9)</option>
            <option value="thpt">THPT (Lớp 10 - 12)</option>
            <option value="dai-hoc">Đại học / Olympic Quốc tế</option>
          </select>

          <select
            value={illusFilter}
            onChange={(e) => {
              setIllusFilter(e.target.value as any);
              setCurrentPage(1);
            }}
            className="input-field"
            style={{ cursor: 'pointer' }}
          >
            <option value="all">Tất cả minh họa (5,272)</option>
            <option value="has_illus">📐 Đã có sơ đồ 2D (748)</option>
            <option value="no_illus">⚠️ Chưa có sơ đồ riêng (4,524)</option>
          </select>
        </div>
      </div>

      {/* Grid of Formulas */}
      {loading ? (
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))',
            gap: '20px',
          }}
        >
          {Array.from({ length: 8 }).map((_, i) => (
            <div key={i} className="glass-card" style={{ height: '220px', opacity: 0.5, animation: 'pulse 1.5s infinite' }} />
          ))}
        </div>
      ) : formulas.length === 0 ? (
        <div className="glass-panel" style={{ padding: '60px 20px', textAlign: 'center' }}>
          <BookOpen size={48} style={{ color: 'var(--text-muted)', margin: '0 auto 16px' }} />
          <h3 style={{ fontSize: '1.2rem', marginBottom: '8px' }}>Không tìm thấy công thức phù hợp</h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
            Hãy thử tìm bằng từ khoá khác hoặc chọn lại danh mục môn học.
          </p>
        </div>
      ) : (
        <>
          <div
            style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))',
              gap: '20px',
            }}
          >
            {formulas.map((f) => {
              const nameDisplay = f.name_vi || f.name || f.name_en || f.id;
              const isCopied = copiedId === f.id;

              return (
                <div
                  key={f.id}
                  className="glass-card"
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'space-between',
                    cursor: 'pointer',
                    position: 'relative',
                    overflow: 'hidden',
                  }}
                  onClick={() => handleOpenDetail(f)}
                >
                  <div>
                    {/* Top row: Subject & Badges */}
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                      <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
                        <span
                          className={`badge ${
                            f.subject === 'math'
                              ? 'badge-indigo'
                              : f.subject === 'physics'
                              ? 'badge-cyan'
                              : f.subject === 'chemistry'
                              ? 'badge-emerald'
                              : 'badge-rose'
                          }`}
                        >
                          {f.subject === 'math'
                            ? 'Toán'
                            : f.subject === 'physics'
                            ? 'Vật Lí'
                            : f.subject === 'chemistry'
                            ? 'Hoá Học'
                            : f.subject === 'biology'
                            ? 'Sinh Học'
                            : f.subject}
                        </span>
                        {f.level && (
                          <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>
                            {f.level.toUpperCase()}
                          </span>
                        )}
                      </div>

                      <div style={{ display: 'flex', gap: '6px' }}>
                        {f.has_illustration_2d && (
                          <span className="badge badge-amber" style={{ fontSize: '0.65rem', padding: '2px 6px' }} title="Minh hoạ 2D">
                            2D
                          </span>
                        )}
                        {f.has_scene_3d && (
                          <span className="badge badge-cyan" style={{ fontSize: '0.65rem', padding: '2px 6px' }} title="Mô phỏng 3D">
                            3D
                          </span>
                        )}
                      </div>
                    </div>

                    {/* Formula Name */}
                    <h3
                      style={{
                        fontSize: '1.05rem',
                        fontWeight: 600,
                        lineHeight: 1.4,
                        marginBottom: '14px',
                        color: 'var(--text-primary)',
                      }}
                    >
                      {nameDisplay}
                    </h3>

                    {/* Math Preview */}
                    <div
                      style={{
                        background: '#f8fafc',
                        padding: '16px 14px',
                        borderRadius: 'var(--radius-md)',
                        border: '1px solid #e2e8f0',
                        color: '#0f172a',
                        textAlign: 'center',
                        overflowX: 'auto',
                        marginBottom: '14px',
                        minHeight: '74px',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                      }}
                    >
                      <MathView latex={f.latex} block />
                    </div>

                    {/* Direct Visual 2D Illustration Thumbnail */}
                    {f.has_illustration_2d && (
                      <div
                        style={{
                          height: '95px',
                          background: '#ffffff',
                          borderRadius: 'var(--radius-sm)',
                          marginBottom: '12px',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          overflow: 'hidden',
                          border: '1px dashed #cbd5e1',
                          padding: '6px',
                        }}
                      >
                        <img
                          src={`/api/illustrations2d/${f.id}`}
                          alt={nameDisplay}
                          style={{ maxHeight: '100%', maxWidth: '100%', objectFit: 'contain' }}
                          loading="lazy"
                          onError={(e) => {
                            const parent = e.currentTarget.parentElement;
                            if (parent) parent.style.display = 'none';
                          }}
                        />
                      </div>
                    )}
                  </div>

                  {/* Actions Footer */}
                  <div
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      paddingTop: '12px',
                      borderTop: '1px solid var(--border-subtle)',
                    }}
                  >
                    <button
                      className="btn btn-secondary"
                      style={{ padding: '6px 12px', fontSize: '0.8rem' }}
                      onClick={(e) => handleCopyLatex(e, f)}
                      title="Sao chép LaTeX"
                    >
                      {isCopied ? <Check size={14} color="#10b981" /> : <Copy size={14} />}
                      <span>{isCopied ? 'Đã sao chép' : 'LaTeX'}</span>
                    </button>

                    <button
                      className="btn btn-secondary"
                      style={{ padding: '6px 12px', fontSize: '0.8rem', color: '#0369a1', fontWeight: 600 }}
                      onClick={() => handleOpenDetail(f)}
                    >
                      <Eye size={14} />
                      <span>Chi Tiết</span>
                    </button>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Full Pagination */}
          <Pagination
            currentPage={currentPage}
            totalPages={totalPages}
            onPageChange={(page) => loadFormulas(page)}
            totalItems={total}
            pageSize={pageSize}
          />
        </>
      )}

      {/* Formula Detail & Calculation Modal */}
      {selectedFormula && (
        <FormulaModal formula={selectedFormula} onClose={() => setSelectedFormula(null)} />
      )}
    </div>
  );
};
