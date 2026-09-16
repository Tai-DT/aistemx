import { useState, useEffect, useCallback } from 'react';
import { api, type Problem, type Formula } from '../services/api';
import { MathView } from '../components/MathView';
import { Pagination } from '../components/Pagination';
import { InteractiveProblemVisualizer } from '../components/InteractiveProblemVisualizer';
import { FormulaModal } from './formulas/FormulaModal';
import { AiProblemModal } from './AiProblemModal';
import {
  CheckCircle2,
  XCircle,
  ShieldCheck,
  ChevronDown,
  ChevronUp,
  Search,
  RefreshCw,
  Flame,
  Sparkles,
  Lightbulb,
} from 'lucide-react';
import confetti from 'canvas-confetti';

interface PracticeStats {
  attempted: number;
  correct: number;
  streak: number;
}

export const PracticeTab = () => {
  const [problems, setProblems] = useState<Problem[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(true);
  const [subject, setSubject] = useState<string>('');
  const [ptype, setPtype] = useState<string>('');
  const [difficulty, setDifficulty] = useState<string>('');
  const [query, setQuery] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 12;

  // Local user progress
  const [userStats, setUserStats] = useState<PracticeStats>(() => {
    try {
      const saved = localStorage.getItem('aistem_practice_stats');
      if (saved) return JSON.parse(saved);
    } catch {
      // fallback
    }
    return { attempted: 0, correct: 0, streak: 0 };
  });

  // User answer state: problemId -> { answer, isCorrect, submitted }
  const [answersState, setAnswersState] = useState<
    Record<string, { answer: string; isCorrect: boolean | null; submitted: boolean }>
  >({});
  const [numericInputs, setNumericInputs] = useState<Record<string, string>>({});
  const [expandedSolutions, setExpandedSolutions] = useState<Record<string, boolean>>({});
  const [expandedVisualizers, setExpandedVisualizers] = useState<Record<string, boolean>>({});
  const [selectedFormula, setSelectedFormula] = useState<Formula | null>(null);
  const [casLoading, setCasLoading] = useState<Record<string, boolean>>({});
  const [showAiModal, setShowAiModal] = useState(false);
  const [problemHints, setProblemHints] = useState<
    Record<string, { loading: boolean; text?: string; step: number; formulas?: string[] }>
  >({});

  const handleAddToPractice = (newProblem: Problem) => {
    setProblems((prev) => [newProblem, ...prev]);
    setTotal((prev) => prev + 1);
    setShowAiModal(false);
  };

  const handleRequestHint = async (p: Problem) => {
    const currentStep = (problemHints[p.id]?.step || 0) + 1;
    setProblemHints((prev) => ({
      ...prev,
      [p.id]: { loading: true, step: currentStep, text: prev[p.id]?.text, formulas: prev[p.id]?.formulas },
    }));
    try {
      const studentAns = answersState[p.id]?.answer;
      const data = await api.getAiHint(p.id, studentAns, currentStep);
      setProblemHints((prev) => ({
        ...prev,
        [p.id]: {
          loading: false,
          text: data.hint,
          step: currentStep,
          formulas: data.formulas_used || [],
        },
      }));
    } catch (e) {
      console.error('Lỗi lấy gợi ý AI:', e);
      setProblemHints((prev) => ({
        ...prev,
        [p.id]: { loading: false, step: currentStep, text: 'Gia sư AI đang bận, em hãy thử lại sau ít giây.' },
      }));
    }
  };

  const saveStats = (newStats: PracticeStats) => {
    setUserStats(newStats);
    try {
      localStorage.setItem('aistem_practice_stats', JSON.stringify(newStats));
    } catch {
      // ignore
    }
  };

  const loadProblems = useCallback(
    async (pageToLoad = 1) => {
      setLoading(true);
      try {
        const data = await api.getProblems({
          subject: subject || undefined,
          type: ptype || undefined,
          difficulty: difficulty ? Number(difficulty) : undefined,
          q: query.trim() || undefined,
          page: pageToLoad,
          page_size: pageSize,
        });
        setProblems(data.problems || []);
        setTotal(data.total || 0);
        setCurrentPage(pageToLoad);
      } catch (e) {
        console.error('Lỗi nạp bài tập:', e);
      } finally {
        setLoading(false);
      }
    },
    [subject, ptype, difficulty, query]
  );

  useEffect(() => {
    loadProblems(1);
  }, [subject, ptype, difficulty]);

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    loadProblems(1);
  };

  const recordResult = (isCorrect: boolean) => {
    const attempted = userStats.attempted + 1;
    const correct = isCorrect ? userStats.correct + 1 : userStats.correct;
    const streak = isCorrect ? userStats.streak + 1 : 0;
    saveStats({ attempted, correct, streak });

    if (isCorrect) {
      confetti({
        particleCount: 50,
        spread: 60,
        origin: { y: 0.8 },
      });
    }
  };

  const handleSelectChoice = (p: Problem, key: string) => {
    if (answersState[p.id]?.submitted) return; // already submitted

    const isCorrect = key.toUpperCase() === p.answer.trim().toUpperCase();
    setAnswersState((prev) => ({
      ...prev,
      [p.id]: { answer: key, isCorrect, submitted: true },
    }));

    recordResult(isCorrect);
    api.recordAttempt({
      learner: 'hs_01_minhanh',
      problem_id: p.id,
      answer: key,
      correct: isCorrect,
      verdict: isCorrect ? 'correct' : 'incorrect',
    });
  };

  const parseUserInputNumber = (raw: string): number => {
    const s = raw.trim().replace(/\s+/g, '');
    if (!s) return NaN;
    if (s.includes('/')) {
      const parts = s.split('/');
      if (parts.length === 2) {
        const num = parseFloat(parts[0].replace(',', '.'));
        const den = parseFloat(parts[1].replace(',', '.'));
        if (!isNaN(num) && !isNaN(den) && den !== 0) {
          return num / den;
        }
      }
    }
    return parseFloat(s.replace(',', '.'));
  };

  const normalizeMathString = (s: string): string => {
    return s
      .toLowerCase()
      .replace(/\$/g, '')
      .replace(/\\text\{[^{}]*\}/g, '')
      .replace(/\\mathrm\{[^{}]*\}/g, '')
      .replace(/\\dfrac|\\frac/g, '')
      .replace(/[{}\^_\\]/g, '')
      .replace(/\s+/g, '')
      .replace(/,/g, '.');
  };

  const normalizeDungSai = (s: string): string => {
    return s
      .toLowerCase()
      .replace(/đ/g, 'd')
      .replace(/[^ds]/g, '');
  };

  const normalizeGhepDoi = (s: string): string => {
    return s
      .toLowerCase()
      .split(/[;,]/)
      .map((part) => part.replace(/[\s\-_:]/g, ''))
      .filter(Boolean)
      .sort()
      .join(';');
  };

  const handleNumericSubmit = (p: Problem) => {
    const val = numericInputs[p.id] || '';
    if (!val.trim()) return;

    const num = parseUserInputNumber(val);
    let isCorrect = false;

    if (p.type === 'dung-sai') {
      const uNorm = normalizeDungSai(val);
      const aNorm = normalizeDungSai(p.answer || '');
      isCorrect = uNorm.length > 0 && uNorm === aNorm;
    } else if (p.type === 'ghep-doi') {
      const uNorm = normalizeGhepDoi(val);
      const aNorm = normalizeGhepDoi(p.answer || '');
      isCorrect = uNorm.length > 0 && uNorm === aNorm;
    } else if (!isNaN(num) && p.answer_numeric !== undefined && p.answer_numeric !== null) {
      const tol = p.tolerance || 0.05;
      isCorrect = Math.abs(num - p.answer_numeric) <= Math.abs(p.answer_numeric) * tol + 1e-6;
    } else {
      const cleanInput = normalizeMathString(val);
      const cleanAnswer = normalizeMathString(p.answer || '');
      isCorrect = cleanInput === cleanAnswer || val.trim().toLowerCase() === (p.answer || '').trim().toLowerCase();
    }

    setAnswersState((prev) => ({
      ...prev,
      [p.id]: { answer: val, isCorrect, submitted: true },
    }));

    recordResult(isCorrect);
    api.recordAttempt({
      learner: 'hs_01_minhanh',
      problem_id: p.id,
      answer: val,
      correct: isCorrect,
      verdict: isCorrect ? 'correct' : 'incorrect',
    });
  };

  const handleVerifyCAS = async (p: Problem) => {
    setCasLoading((prev) => ({ ...prev, [p.id]: true }));
    try {
      const res = await api.verifyProblemCAS(p.id);
      setProblems((prev) =>
        prev.map((item) =>
          item.id === p.id
            ? {
                ...item,
                cas_verified: res.cas_verified,
                cas_status: res.cas_status,
                cas_details: res.cas_details,
              }
            : item
        )
      );
    } catch (e) {
      console.error('Lỗi xác minh CAS:', e);
    } finally {
      setCasLoading((prev) => ({ ...prev, [p.id]: false }));
    }
  };

  const toggleSolution = (id: string) => {
    setExpandedSolutions((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  const toggleVisualizer = (id: string) => {
    setExpandedVisualizers((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  const handleOpenFormula = async (formulaId: string) => {
    try {
      const data = await api.getFormulaById(formulaId);
      if (data && data.id) {
        setSelectedFormula(data);
      }
    } catch (e) {
      console.error('Lỗi tải thông tin công thức:', e);
    }
  };

  const accuracy =
    userStats.attempted > 0 ? Math.round((userStats.correct / userStats.attempted) * 100) : 0;

  const totalPages = Math.ceil(total / pageSize);

  const subjectPills = [
    { id: '', label: 'Tất cả môn' },
    { id: 'physics', label: 'Vật Lí' },
    { id: 'math', label: 'Toán Học' },
    { id: 'chemistry', label: 'Hoá Học' },
    { id: 'biology', label: 'Sinh Học' },
  ];

  return (
    <div className="tab-container animate-fade-in">
      {/* Top Banner & User Scoreboard */}
      <div
        className="glass-panel"
        style={{
          padding: '24px',
          marginBottom: '24px',
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
          gap: '20px',
          alignItems: 'center',
        }}
      >
        <div>
          <h2 style={{ fontSize: '1.5rem', display: 'flex', alignItems: 'center', gap: '10px' }}>
            <ShieldCheck style={{ color: '#06b6d4' }} />
            <span>Luyện Tập Bài Toán</span>
          </h2>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.88rem', marginTop: '4px' }}>
            Tự luyện bài tập, tự động kiểm tra kết quả và xem hướng dẫn chi tiết từng bước.
          </p>
        </div>

        {/* User Progress Stats Card */}
        <div
          style={{
            display: 'flex',
            gap: '16px',
            background: '#f8fafc',
            padding: '12px 20px',
            borderRadius: 'var(--radius-md)',
            border: '1px solid #e2e8f0',
            justifyContent: 'space-around',
          }}
        >
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>ĐÃ LÀM</div>
            <div style={{ fontSize: '1.35rem', fontWeight: 800, color: '#f8fafc' }}>
              {userStats.attempted}
            </div>
          </div>

          <div style={{ width: '1px', background: 'var(--border-subtle)' }} />

          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>ĐÚNG</div>
            <div style={{ fontSize: '1.35rem', fontWeight: 800, color: '#10b981' }}>
              {userStats.correct}
            </div>
          </div>

          <div style={{ width: '1px', background: 'var(--border-subtle)' }} />

          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>TỶ LỆ</div>
            <div style={{ fontSize: '1.35rem', fontWeight: 800, color: '#06b6d4' }}>
              {accuracy}%
            </div>
          </div>

          <div style={{ width: '1px', background: 'var(--border-subtle)' }} />

          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '3px' }}>
              <Flame size={12} color="#f59e0b" />
              <span>CHUỖI</span>
            </div>
            <div style={{ fontSize: '1.35rem', fontWeight: 800, color: '#f59e0b' }}>
              {userStats.streak}🔥
            </div>
          </div>
        </div>
      </div>

      {/* Filter Bar */}
      <div className="glass-panel" style={{ padding: '20px', marginBottom: '24px' }}>
        {/* Subject Pills */}
        <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '16px', alignItems: 'center' }}>
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

          <button
            type="button"
            className="btn"
            onClick={() => setShowAiModal(true)}
            style={{
              marginLeft: 'auto',
              background: 'linear-gradient(135deg, #0284c7 0%, #6366f1 100%)',
              color: '#ffffff',
              fontWeight: 700,
              fontSize: '0.85rem',
              padding: '7px 18px',
              borderRadius: 'var(--radius-full)',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              border: 'none',
              boxShadow: '0 4px 14px rgba(2, 132, 199, 0.3)',
              cursor: 'pointer',
            }}
          >
            <Sparkles size={16} />
            <span>Tạo Đề Thi Bằng AI (SymPy CAS)</span>
          </button>
        </div>

        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
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
                placeholder="Tìm bài toán theo nội dung, chủ đề (ví dụ: Dao động, Glucose, Tích phân...)"
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
            value={ptype}
            onChange={(e) => {
              setPtype(e.target.value);
              setCurrentPage(1);
            }}
            className="input-field"
            style={{ cursor: 'pointer' }}
          >
            <option value="">Tất cả dạng bài</option>
            <option value="trac-nghiem">Trắc nghiệm nhiều lựa chọn</option>
            <option value="tu-luan-so">Tự luận số (Numeric)</option>
            <option value="dien-khuyet">Điền khuyết / Trả lời ngắn</option>
          </select>

          <select
            value={difficulty}
            onChange={(e) => {
              setDifficulty(e.target.value);
              setCurrentPage(1);
            }}
            className="input-field"
            style={{ cursor: 'pointer' }}
          >
            <option value="">Tất cả độ khó</option>
            <option value="1">Cơ bản (Mức 1)</option>
            <option value="2">Thông hiểu (Mức 2)</option>
            <option value="3">Vận dụng (Mức 3)</option>
            <option value="4">Vận dụng cao (Mức 4)</option>
            <option value="5">Olympic / Chuyên sâu (Mức 5)</option>
          </select>
        </div>
      </div>

      {/* Problem Cards List */}
      {loading ? (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {Array.from({ length: 4 }).map((_, i) => (
            <div key={i} className="glass-panel" style={{ height: '180px', opacity: 0.5, animation: 'pulse 1.5s infinite' }} />
          ))}
        </div>
      ) : problems.length === 0 ? (
        <div className="glass-panel" style={{ padding: '60px 20px', textAlign: 'center' }}>
          <ShieldCheck size={48} style={{ color: 'var(--text-muted)', margin: '0 auto 16px' }} />
          <h3 style={{ fontSize: '1.2rem', marginBottom: '8px' }}>Không tìm thấy bài toán nào</h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
            Hãy chọn lại bộ lọc hoặc tìm kiếm với từ khoá khác.
          </p>
        </div>
      ) : (
        <>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
            {problems.map((p) => {
              const state = answersState[p.id];
              const isSolutionOpen = expandedSolutions[p.id];
              const isVerifying = casLoading[p.id];

              return (
                <div
                  key={p.id}
                  className="glass-panel"
                  style={{
                    padding: '24px',
                    position: 'relative',
                    transition: 'all var(--transition-smooth)',
                  }}
                >
                  {/* Top Bar: Problem ID, Subject, Difficulty, CAS status */}
                  <div
                    style={{
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                      flexWrap: 'wrap',
                      gap: '10px',
                      marginBottom: '16px',
                    }}
                  >
                    <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
                      <span
                        className={`badge ${
                          p.subject === 'math'
                            ? 'badge-indigo'
                            : p.subject === 'physics'
                            ? 'badge-cyan'
                            : p.subject === 'chemistry'
                            ? 'badge-emerald'
                            : 'badge-rose'
                        }`}
                      >
                        {p.subject === 'math'
                          ? 'Toán'
                          : p.subject === 'physics'
                          ? 'Vật Lí'
                          : p.subject === 'chemistry'
                          ? 'Hoá Học'
                          : p.subject === 'biology'
                          ? 'Sinh Học'
                          : p.subject}
                      </span>

                      <span className="badge badge-amber">Độ khó: {p.difficulty || 1}/5</span>

                      {p.topic && (
                        <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                          • {p.topic}
                        </span>
                      )}
                    </div>

                    <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                      {/* CAS Verified Badge */}
                      {p.cas_verified ? (
                        <span
                          className="badge badge-emerald"
                          title={`Kiểm chứng SymPy: ${p.cas_details?.method || 'Toán học chuẩn xác'}`}
                        >
                          <CheckCircle2 size={13} />
                          <span>CAS Verified</span>
                        </span>
                      ) : (
                        <button
                          className="btn btn-secondary"
                          style={{ padding: '4px 10px', fontSize: '0.75rem' }}
                          onClick={() => handleVerifyCAS(p)}
                          disabled={isVerifying}
                          title="Xác minh bước giải toán học qua SymPy Engine"
                        >
                          <RefreshCw size={12} className={isVerifying ? 'spin' : ''} />
                          <span>{isVerifying ? 'Đang kiểm chứng...' : 'Kiểm chứng CAS'}</span>
                        </button>
                      )}
                    </div>
                  </div>

                  {/* Problem Statement */}
                  <div
                    style={{
                      fontSize: '1.05rem',
                      lineHeight: 1.65,
                      marginBottom: '14px',
                      color: 'var(--text-primary)',
                    }}
                  >
                    <MathView content={p.statement_vi} />
                  </div>

                  {/* Nút bật/tắt Mô hình minh hoạ trực quan & AI Gợi Ý Socratic */}
                  <div style={{ marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                    <button
                      className="btn btn-secondary"
                      style={{
                        padding: '6px 14px',
                        fontSize: '0.82rem',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '6px',
                        background: expandedVisualizers[p.id] ? '#f0f9ff' : '#ffffff',
                        borderColor: expandedVisualizers[p.id] ? '#0284c7' : 'var(--border-subtle)',
                        color: expandedVisualizers[p.id] ? '#0284c7' : 'var(--text-primary)',
                        fontWeight: 600,
                        boxShadow: expandedVisualizers[p.id] ? '0 0 0 2px rgba(2, 132, 199, 0.15)' : 'none',
                      }}
                      onClick={() => toggleVisualizer(p.id)}
                    >
                      <Sparkles size={14} color="#0284c7" />
                      <span>{expandedVisualizers[p.id] ? 'Thu gọn mô hình minh hoạ' : '🔬 Mô hình minh hoạ trực quan'}</span>
                    </button>

                    <button
                      className="btn btn-secondary"
                      style={{
                        padding: '6px 14px',
                        fontSize: '0.82rem',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '6px',
                        background: problemHints[p.id]?.text ? '#fffbeb' : '#ffffff',
                        borderColor: problemHints[p.id]?.text ? '#f59e0b' : 'var(--border-subtle)',
                        color: problemHints[p.id]?.text ? '#b45309' : 'var(--text-primary)',
                        fontWeight: 600,
                      }}
                      onClick={() => handleRequestHint(p)}
                      disabled={problemHints[p.id]?.loading}
                      title="Nhận gợi ý tư duy Socratic từng bước từ Gia sư AI AISTEM X"
                    >
                      <Lightbulb size={14} color="#d97706" />
                      <span>
                        {problemHints[p.id]?.loading
                          ? 'AI đang suy luận...'
                          : problemHints[p.id]?.text
                          ? `💡 Gợi ý bước ${problemHints[p.id]?.step + 1}`
                          : '💡 AI Gợi Ý Socratic'}
                      </span>
                    </button>
                  </div>

                  {/* Socratic Hint Box */}
                  {problemHints[p.id]?.text && (
                    <div
                      style={{
                        marginBottom: '16px',
                        padding: '14px 16px',
                        borderRadius: 'var(--radius-md)',
                        background: 'linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%)',
                        border: '1px solid #fde68a',
                        color: '#78350f',
                        boxShadow: '0 2px 8px rgba(217, 119, 6, 0.08)',
                      }}
                    >
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.82rem', fontWeight: 700, color: '#b45309' }}>
                          <Lightbulb size={15} color="#b45309" />
                          <span>GỢI Ý TƯ DUY SOCRATIC (BƯỚC {problemHints[p.id]?.step})</span>
                        </div>
                        <button
                          style={{ background: 'none', border: 'none', color: '#92400e', fontSize: '0.78rem', cursor: 'pointer', textDecoration: 'underline' }}
                          onClick={() => setProblemHints((prev) => ({ ...prev, [p.id]: { ...prev[p.id], text: undefined } }))}
                        >
                          Thu gọn
                        </button>
                      </div>
                      <div style={{ fontSize: '0.92rem', lineHeight: 1.6, color: '#451a03' }}>
                        <MathView content={problemHints[p.id]?.text || ''} />
                      </div>
                    </div>
                  )}

                  {/* Interactive Problem Visualizer Simulation Component */}
                  {expandedVisualizers[p.id] && (
                    <InteractiveProblemVisualizer
                      problem={p}
                      onOpenFormula={handleOpenFormula}
                    />
                  )}

                  {/* Choice Selection (Multiple Choice) */}
                  {p.choices && p.choices.length > 0 && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginBottom: '20px' }}>
                      {p.choices.map((choice) => {
                        const isSelected = state?.answer === choice.key;
                        const isCorrectKey = choice.key.toUpperCase() === p.answer.trim().toUpperCase();
                        const showVerdict = state?.submitted;

                        let btnStyle: React.CSSProperties = {
                          display: 'flex',
                          alignItems: 'flex-start',
                          gap: '12px',
                          padding: '12px 16px',
                          borderRadius: 'var(--radius-md)',
                          background: '#ffffff',
                          border: '1px solid var(--border-subtle)',
                          cursor: state?.submitted ? 'default' : 'pointer',
                          textAlign: 'left',
                          transition: 'all var(--transition-fast)',
                          boxShadow: '0 1px 3px rgba(15, 23, 42, 0.03)',
                        };

                        if (showVerdict) {
                          if (isCorrectKey) {
                            btnStyle = {
                              ...btnStyle,
                              background: '#f0fdf4',
                              border: '1px solid #86efac',
                            };
                          } else if (isSelected && !isCorrectKey) {
                            btnStyle = {
                              ...btnStyle,
                              background: '#fff1f2',
                              border: '1px solid #fecdd3',
                            };
                          }
                        } else if (isSelected) {
                          btnStyle = {
                            ...btnStyle,
                            border: '1px solid #0284c7',
                            background: '#f0f9ff',
                          };
                        }

                        const isCircleActive = (showVerdict && (isCorrectKey || isSelected)) || isSelected;

                        return (
                          <div key={choice.key}>
                            <div
                              style={btnStyle}
                              onClick={() => handleSelectChoice(p, choice.key)}
                              className={!state?.submitted ? 'choice-hover' : ''}
                            >
                              <div
                                style={{
                                  width: '28px',
                                  height: '28px',
                                  borderRadius: '50%',
                                  background: showVerdict
                                    ? isCorrectKey
                                      ? '#10b981'
                                      : isSelected
                                      ? '#f43f5e'
                                      : '#f1f5f9'
                                    : isSelected
                                    ? '#0284c7'
                                    : '#f1f5f9',
                                  display: 'flex',
                                  alignItems: 'center',
                                  justifyContent: 'center',
                                  fontWeight: 700,
                                  fontSize: '0.85rem',
                                  color: isCircleActive ? '#ffffff' : '#334155',
                                  border: isCircleActive ? 'none' : '1px solid #cbd5e1',
                                  flexShrink: 0,
                                }}
                              >
                                {choice.key}
                              </div>
                              <div style={{ flex: 1, paddingTop: '2px' }}>
                                <MathView content={choice.text} />
                              </div>

                              {showVerdict && isCorrectKey && (
                                <CheckCircle2 size={20} color="#10b981" style={{ flexShrink: 0 }} />
                              )}
                              {showVerdict && isSelected && !isCorrectKey && (
                                <XCircle size={20} color="#f43f5e" style={{ flexShrink: 0 }} />
                              )}
                            </div>

                            {/* Why Wrong Distractor Analysis */}
                            {showVerdict && isSelected && !isCorrectKey && choice.why_wrong && (
                              <div
                                style={{
                                  marginTop: '6px',
                                  marginLeft: '40px',
                                  padding: '10px 14px',
                                  borderRadius: 'var(--radius-sm)',
                                  background: 'rgba(244, 63, 94, 0.08)',
                                  borderLeft: '3px solid #f43f5e',
                                  fontSize: '0.86rem',
                                  color: '#fda4af',
                                  lineHeight: 1.5,
                                }}
                              >
                                <strong>⚠️ Phân tích sai lầm thường gặp:</strong> {choice.why_wrong}
                              </div>
                            )}
                          </div>
                        );
                      })}
                    </div>
                  )}

                  {/* Numeric Input Question */}
                  {(!p.choices || p.choices.length === 0) && (
                    <div style={{ marginBottom: '20px' }}>
                      <div style={{ display: 'flex', gap: '10px', maxWidth: '420px' }}>
                        <input
                          type="text"
                          placeholder={
                            p.type === 'dung-sai'
                              ? 'Ví dụ: Đ-Đ-S-Đ hoặc D-D-S-D...'
                              : p.type === 'ghep-doi'
                              ? 'Ví dụ: 1-b; 2-d; 3-a; 4-c...'
                              : p.type === 'tu-luan'
                              ? 'Nhập đáp số cuối cùng...'
                              : `Nhập đáp án số ${p.answer_unit ? `(${p.answer_unit})` : ''}...`
                          }
                          className="input-field"
                          value={numericInputs[p.id] || ''}
                          disabled={state?.submitted}
                          onChange={(e) =>
                            setNumericInputs({ ...numericInputs, [p.id]: e.target.value })
                          }
                          onKeyDown={(e) => e.key === 'Enter' && handleNumericSubmit(p)}
                        />
                        <button
                          className="btn btn-primary"
                          onClick={() => handleNumericSubmit(p)}
                          disabled={state?.submitted}
                        >
                          Kiểm Tra
                        </button>
                      </div>

                      {state?.submitted && (
                        <div style={{ marginTop: '10px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                          {state.isCorrect ? (
                            <span className="badge badge-emerald" style={{ fontSize: '0.85rem' }}>
                              <CheckCircle2 size={16} /> Chính xác!
                            </span>
                          ) : (
                            <span className="badge badge-rose" style={{ fontSize: '0.85rem' }}>
                              <XCircle size={16} /> Chưa chính xác. Đáp án chuẩn: {p.answer}{' '}
                              {p.answer_unit || ''}
                            </span>
                          )}
                        </div>
                      )}
                    </div>
                  )}

                  {/* Solution Steps Accordion */}
                  <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: '14px' }}>
                    <button
                      className="btn btn-secondary"
                      style={{ padding: '6px 12px', fontSize: '0.82rem' }}
                      onClick={() => toggleSolution(p.id)}
                    >
                      {isSolutionOpen ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                      <span>{isSolutionOpen ? 'Ẩn lời giải chi tiết' : 'Xem lời giải chi tiết'}</span>
                    </button>

                    {isSolutionOpen && (
                      <div
                        style={{
                          marginTop: '16px',
                          padding: '18px 20px',
                          borderRadius: 'var(--radius-md)',
                          background: '#f8fafc',
                          border: '1px solid #bae6fd',
                          boxShadow: '0 2px 8px rgba(2, 132, 199, 0.05)',
                        }}
                        className="animate-fade-in"
                      >
                        <h4 style={{ fontSize: '0.95rem', fontWeight: 700, color: '#059669', marginBottom: '12px' }}>
                          Đáp án chính thức: {p.answer} {p.answer_unit || ''}
                        </h4>

                        {p.solution_steps && p.solution_steps.length > 0 ? (
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                            {p.solution_steps.map((step, sIdx) => (
                              <div
                                key={sIdx}
                                style={{
                                  paddingLeft: '14px',
                                  borderLeft: '3px solid #0284c7',
                                }}
                              >
                                <div style={{ fontSize: '0.92rem', color: '#1e293b', lineHeight: 1.6, marginBottom: '6px' }}>
                                  <MathView content={step.explain} />
                                </div>
                                {step.latex && (
                                  <div style={{ fontSize: '1.08rem', color: '#0f172a', marginTop: '6px' }}>
                                    <MathView latex={step.latex} block />
                                  </div>
                                )}
                              </div>
                            ))}
                          </div>
                        ) : (
                          <p style={{ color: 'var(--text-secondary)', fontSize: '0.88rem' }}>
                            Xem công thức liên quan: {p.formulas_used?.join(', ') || 'N/A'}
                          </p>
                        )}
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>

          {/* Pagination */}
          <Pagination
            currentPage={currentPage}
            totalPages={totalPages}
            onPageChange={(page) => loadProblems(page)}
            totalItems={total}
            pageSize={pageSize}
          />
        </>
      )}

      {/* Formula Detail Modal khi bấm vào công thức áp dụng trong bài toán */}
      {selectedFormula && (
        <FormulaModal
          formula={selectedFormula}
          onClose={() => setSelectedFormula(null)}
        />
      )}

      {/* AI Problem Generator Modal */}
      {showAiModal && (
        <AiProblemModal
          onClose={() => setShowAiModal(false)}
          onAddToPractice={handleAddToPractice}
        />
      )}
    </div>
  );
};
