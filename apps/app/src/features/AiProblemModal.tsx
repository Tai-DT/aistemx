import { useState, type FC } from 'react';
import { createPortal } from 'react-dom';
import { api, type Problem, type AIGeneratedProblemResult } from '../services/api';
import { MathView } from '../components/MathView';
import {
  X,
  Sparkles,
  ShieldCheck,
  CheckCircle2,
  XCircle,
  ChevronDown,
  ChevronUp,
  Brain,
  RefreshCw,
  BookOpen,
  PlusCircle,
  AlertCircle,
  Check,
} from 'lucide-react';
import confetti from 'canvas-confetti';

interface AiProblemModalProps {
  onClose: () => void;
  onAddToPractice?: (problem: Problem) => void;
}

const PRESET_PROMPTS = [
  {
    label: 'Toán 12: Cực trị hàm bậc ba',
    subject: 'math',
    level: 'thpt',
    difficulty: 3,
    prompt: 'Tìm các điểm cực trị của hàm số bậc ba y = ax^3 + bx^2 + cx + d và giá trị cực đại, cực tiểu tương ứng.',
  },
  {
    label: 'Toán 11: Giới hạn vô định 0/0',
    subject: 'math',
    level: 'thpt',
    difficulty: 3,
    prompt: 'Tính giới hạn dạng vô định 0/0 bằng phương pháp nhân lượng liên hợp hoặc phân tích nhân tử.',
  },
  {
    label: 'Vật lí 10: Ném ngang',
    subject: 'physics',
    level: 'thpt',
    difficulty: 3,
    prompt: 'Một vật ném ngang từ độ cao h với vận tốc ban đầu v0. Tính tầm xa và thời gian chạm đất.',
  },
  {
    label: 'Vật lí 12: Con lắc lò xo',
    subject: 'physics',
    level: 'thpt',
    difficulty: 3,
    prompt: 'Con lắc lò xo dao động điều hòa: tính cơ năng, động năng, thế năng và chu kỳ dao động.',
  },
  {
    label: 'Hoá 10: Thể tích khí (đkc)',
    subject: 'chemistry',
    level: 'thpt',
    difficulty: 2,
    prompt: 'Cho kim loại phản ứng với dung dịch axit HCl/H2SO4, tính thể tích khí H2 sinh ra ở điều kiện chuẩn 24.79 L/mol.',
  },
  {
    label: 'Hoá 11: Tính pH axit yếu',
    subject: 'chemistry',
    level: 'thpt',
    difficulty: 4,
    prompt: 'Tính pH dung dịch axit yếu CH3COOH có nồng độ C M và hằng số Ka cho trước.',
  },
  {
    label: 'Sinh 12: Lai 2 cặp tính trạng',
    subject: 'biology',
    level: 'thpt',
    difficulty: 3,
    prompt: 'Bài toán quy luật di truyền phân ly độc lập Menđen: tính tỉ lệ kiểu gen, kiểu hình ở đời F2.',
  },
];

export const AiProblemModal: FC<AiProblemModalProps> = ({ onClose, onAddToPractice }) => {
  const [prompt, setPrompt] = useState('Tìm cực trị của hàm số bậc ba y = x^3 - 3x^2 - 9x + 2');
  const [subject, setSubject] = useState<string>('math');
  const [level, setLevel] = useState<string>('thpt');
  const [difficulty, setDifficulty] = useState<number>(3);
  const [model, setModel] = useState<'deepseek-r1' | 'llama-3.3' | 'qwq-32b'>('deepseek-r1');

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<AIGeneratedProblemResult | null>(null);

  // User interaction with the generated problem
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null);
  const [isAnswerCorrect, setIsAnswerCorrect] = useState<boolean | null>(null);
  const [showSolution, setShowSolution] = useState(false);
  const [showThinking, setShowThinking] = useState(false);
  const [addedToPractice, setAddedToPractice] = useState(false);

  const handleGenerate = async (customPrompt?: string) => {
    const finalPrompt = (customPrompt ?? prompt).trim();
    if (!finalPrompt) return;

    setLoading(true);
    setError(null);
    setSelectedAnswer(null);
    setIsAnswerCorrect(null);
    setShowSolution(false);
    setShowThinking(false);
    setAddedToPractice(false);

    try {
      const data = await api.generateProblem({
        prompt: finalPrompt,
        subject,
        level,
        difficulty,
        model,
      });
      setResult(data);
    } catch (err: any) {
      console.error('Lỗi sinh bài toán AI:', err);
      setError(err?.message || 'Không thể tạo bài toán lúc này. Hãy thử lại.');
    } finally {
      setLoading(false);
    }
  };

  const handleSelectChoice = (choiceKey: string) => {
    if (!result?.problem) return;
    setSelectedAnswer(choiceKey);
    const correct = choiceKey.trim().toUpperCase() === result.problem.answer.trim().toUpperCase();
    setIsAnswerCorrect(correct);
    if (correct) {
      confetti({ particleCount: 50, spread: 60, origin: { y: 0.8 } });
    }
  };

  const handleAdd = () => {
    if (!result?.problem) return;
    if (onAddToPractice) {
      onAddToPractice(result.problem);
      setAddedToPractice(true);
    }
  };

  const applyPreset = (preset: typeof PRESET_PROMPTS[0]) => {
    setPrompt(preset.prompt);
    setSubject(preset.subject);
    setLevel(preset.level);
    setDifficulty(preset.difficulty);
    handleGenerate(preset.prompt);
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
        background: 'rgba(15, 23, 42, 0.55)',
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
          maxWidth: '880px',
          maxHeight: '92vh',
          overflowY: 'auto',
          padding: '28px 28px',
          borderRadius: 'var(--radius-lg)',
          background: '#ffffff',
          border: '1px solid #bae6fd',
          boxShadow: '0 25px 50px -12px rgba(15, 23, 42, 0.25)',
          position: 'relative',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '20px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
              <span
                style={{
                  background: 'linear-gradient(135deg, #0284c7 0%, #6366f1 100%)',
                  color: '#ffffff',
                  padding: '4px 10px',
                  borderRadius: '9999px',
                  fontSize: '0.78rem',
                  fontWeight: 700,
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px',
                }}
              >
                <Sparkles size={14} /> AI STEM GENERATOR
              </span>
              <span
                style={{
                  background: '#ecfdf5',
                  color: '#059669',
                  border: '1px solid #a7f3d0',
                  padding: '3px 8px',
                  borderRadius: '9999px',
                  fontSize: '0.75rem',
                  fontWeight: 600,
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px',
                }}
              >
                <ShieldCheck size={13} /> SymPy CAS Anti-Hallucination
              </span>
            </div>
            <h2 style={{ fontSize: '1.4rem', fontWeight: 800, color: '#0f172a', margin: '4px 0' }}>
              Tạo Đề & Bài Toán Thông Minh Bằng AI
            </h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem' }}>
              Nhập yêu cầu bằng ngôn ngữ tự nhiên. AI sẽ thiết kế đề bài, kiểm chứng toán học bằng hệ CAS độc lập và tự động gắn minh hoạ 2D.
            </p>
          </div>

          <button
            onClick={onClose}
            className="btn-icon"
            style={{
              background: '#f1f5f9',
              border: 'none',
              borderRadius: '50%',
              width: '34px',
              height: '34px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              cursor: 'pointer',
            }}
          >
            <X size={18} color="#64748b" />
          </button>
        </div>

        {/* Quick Suggestion Chips */}
        <div style={{ marginBottom: '16px' }}>
          <div style={{ fontSize: '0.75rem', fontWeight: 600, color: '#64748b', marginBottom: '6px' }}>
            GỢI Ý CHỦ ĐỀ PHỔ BIẾN:
          </div>
          <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
            {PRESET_PROMPTS.map((p, idx) => (
              <button
                key={idx}
                type="button"
                onClick={() => applyPreset(p)}
                style={{
                  background: '#f8fafc',
                  border: '1px solid #e2e8f0',
                  borderRadius: '16px',
                  padding: '4px 10px',
                  fontSize: '0.78rem',
                  color: '#334155',
                  cursor: 'pointer',
                  transition: 'all 0.15s ease',
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.borderColor = '#38bdf8';
                  e.currentTarget.style.background = '#f0f9ff';
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.borderColor = '#e2e8f0';
                  e.currentTarget.style.background = '#f8fafc';
                }}
              >
                {p.label}
              </button>
            ))}
          </div>
        </div>

        {/* Controls Bar: Subject, Level, Difficulty, Model */}
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))',
            gap: '10px',
            marginBottom: '14px',
            background: '#f8fafc',
            padding: '12px',
            borderRadius: 'var(--radius-md)',
            border: '1px solid #e2e8f0',
          }}
        >
          <div>
            <label style={{ fontSize: '0.72rem', fontWeight: 700, color: '#64748b', display: 'block', marginBottom: '4px' }}>
              MÔN HỌC
            </label>
            <select
              value={subject}
              onChange={(e) => setSubject(e.target.value)}
              className="input-field"
              style={{ width: '100%', fontSize: '0.84rem', padding: '6px 10px', height: '36px' }}
            >
              <option value="math">Toán Học</option>
              <option value="physics">Vật Lí</option>
              <option value="chemistry">Hoá Học</option>
              <option value="biology">Sinh Học</option>
            </select>
          </div>

          <div>
            <label style={{ fontSize: '0.72rem', fontWeight: 700, color: '#64748b', display: 'block', marginBottom: '4px' }}>
              CẤP HỌC
            </label>
            <select
              value={level}
              onChange={(e) => setLevel(e.target.value)}
              className="input-field"
              style={{ width: '100%', fontSize: '0.84rem', padding: '6px 10px', height: '36px' }}
            >
              <option value="thpt">THPT (Lớp 10-12)</option>
              <option value="thcs">THCS (Lớp 6-9)</option>
              <option value="tieu-hoc">Tiểu học (Lớp 1-5)</option>
            </select>
          </div>

          <div>
            <label style={{ fontSize: '0.72rem', fontWeight: 700, color: '#64748b', display: 'block', marginBottom: '4px' }}>
              ĐỘ KHÓ
            </label>
            <select
              value={difficulty}
              onChange={(e) => setDifficulty(Number(e.target.value))}
              className="input-field"
              style={{ width: '100%', fontSize: '0.84rem', padding: '6px 10px', height: '36px' }}
            >
              <option value={1}>1 - Nhận biết (Cơ bản)</option>
              <option value={2}>2 - Thông hiểu</option>
              <option value={3}>3 - Vận dụng</option>
              <option value={4}>4 - Vận dụng cao</option>
              <option value={5}>5 - Chuyên sâu / Olympic</option>
            </select>
          </div>

          <div>
            <label style={{ fontSize: '0.72rem', fontWeight: 700, color: '#64748b', display: 'block', marginBottom: '4px' }}>
              MÔ HÌNH AI
            </label>
            <select
              value={model}
              onChange={(e) => setModel(e.target.value as any)}
              className="input-field"
              style={{ width: '100%', fontSize: '0.84rem', padding: '6px 10px', height: '36px' }}
            >
              <option value="deepseek-r1">DeepSeek-R1 (Toán & Logic sâu)</option>
              <option value="llama-3.3">Llama 3.3 (Tốc độ cao 5s)</option>
              <option value="qwq-32b">QwQ-32B (Lí luận STEM)</option>
            </select>
          </div>
        </div>

        {/* Prompt Input Box */}
        <div style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Nhập yêu cầu bài toán... (Ví dụ: Tạo 1 bài toán cực trị hàm số bậc ba có chứa tham số m, có 4 lựa chọn trắc nghiệm và lời giải chi tiết)"
            rows={2}
            className="input-field"
            style={{
              flex: 1,
              resize: 'vertical',
              fontSize: '0.9rem',
              lineHeight: 1.5,
              padding: '10px 14px',
            }}
          />
          <button
            type="button"
            className="btn btn-primary"
            onClick={() => handleGenerate()}
            disabled={loading || !prompt.trim()}
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '0 24px',
              minWidth: '130px',
              background: 'linear-gradient(135deg, #0284c7 0%, #4f46e5 100%)',
              fontWeight: 700,
            }}
          >
            {loading ? (
              <>
                <RefreshCw size={20} className="animate-spin" style={{ marginBottom: '4px' }} />
                <span style={{ fontSize: '0.78rem' }}>Đang sinh...</span>
              </>
            ) : (
              <>
                <Sparkles size={20} style={{ marginBottom: '4px' }} />
                <span style={{ fontSize: '0.85rem' }}>Sinh Đề Bài</span>
              </>
            )}
          </button>
        </div>

        {/* Error Message */}
        {error && (
          <div
            style={{
              padding: '14px 16px',
              background: '#fef2f2',
              border: '1px solid #fecaca',
              borderRadius: 'var(--radius-md)',
              color: '#b91c1c',
              fontSize: '0.88rem',
              display: 'flex',
              alignItems: 'center',
              gap: '10px',
              marginBottom: '20px',
            }}
          >
            <AlertCircle size={20} />
            <span>{error}</span>
          </div>
        )}

        {/* Loading Skeleton */}
        {loading && (
          <div
            style={{
              padding: '30px',
              textAlign: 'center',
              background: '#f8fafc',
              borderRadius: 'var(--radius-lg)',
              border: '1px dashed #cbd5e1',
              marginBottom: '20px',
            }}
          >
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '10px', color: '#0284c7', fontWeight: 600 }}>
              <RefreshCw size={24} className="animate-spin" />
              <span>AI đang phân tích kiến thức STEM và chạy SymPy CAS xác thực số học...</span>
            </div>
            <p style={{ color: '#64748b', fontSize: '0.82rem', marginTop: '8px' }}>
              Mô hình {model} đang xây dựng các bước giải thích và đối chiếu công thức vector 2D.
            </p>
          </div>
        )}

        {/* Generated Problem Presentation */}
        {result && result.problem && (
          <div
            style={{
              border: '1px solid #e2e8f0',
              borderRadius: 'var(--radius-lg)',
              background: '#ffffff',
              padding: '24px',
              boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05)',
            }}
          >
            {/* Top Bar with CAS Status & Model badge */}
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                flexWrap: 'wrap',
                gap: '8px',
                marginBottom: '16px',
                paddingBottom: '12px',
                borderBottom: '1px solid #f1f5f9',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                {result.cas_verified ? (
                  <span
                    style={{
                      background: '#ecfdf5',
                      color: '#047857',
                      border: '1px solid #a7f3d0',
                      padding: '4px 10px',
                      borderRadius: '9999px',
                      fontSize: '0.78rem',
                      fontWeight: 700,
                      display: 'flex',
                      alignItems: 'center',
                      gap: '5px',
                    }}
                  >
                    <ShieldCheck size={14} /> SymPy CAS Đã Kiểm Chứng (100% Không Ảo Giác)
                  </span>
                ) : (
                  <span
                    style={{
                      background: '#f0f9ff',
                      color: '#0369a1',
                      border: '1px solid #bae6fd',
                      padding: '4px 10px',
                      borderRadius: '9999px',
                      fontSize: '0.78rem',
                      fontWeight: 600,
                      display: 'flex',
                      alignItems: 'center',
                      gap: '5px',
                    }}
                  >
                    <BookOpen size={14} /> Bài toán STEM chuẩn hoá ({result.cas_status})
                  </span>
                )}
                <span style={{ fontSize: '0.75rem', color: '#64748b' }}>
                  Mô hình: <b>{result.model_used}</b>
                </span>
              </div>

              {/* Add to practice button */}
              {onAddToPractice && (
                <button
                  type="button"
                  onClick={handleAdd}
                  disabled={addedToPractice}
                  className="btn btn-secondary"
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px',
                    fontSize: '0.82rem',
                    padding: '6px 14px',
                    borderRadius: '8px',
                    borderColor: addedToPractice ? '#10b981' : undefined,
                    color: addedToPractice ? '#10b981' : undefined,
                  }}
                >
                  {addedToPractice ? (
                    <>
                      <Check size={15} /> Đã Thêm Vào Luyện Tập
                    </>
                  ) : (
                    <>
                      <PlusCircle size={15} /> Thêm Vào Luyện Tập
                    </>
                  )}
                </button>
              )}
            </div>

            {/* Title & Topic */}
            <div style={{ marginBottom: '12px' }}>
              <div style={{ fontSize: '0.78rem', color: '#64748b', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                {result.problem.subject.toUpperCase()} • {result.problem.topic || 'STEM'} • Độ khó {result.problem.difficulty}/5
              </div>
              <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#0f172a', marginTop: '2px' }}>
                {result.problem.title || 'Bài toán tạo bởi AI'}
              </h3>
            </div>

            {/* 2D Vector Illustration if available */}
            {result.illustration_url && (
              <div
                style={{
                  margin: '16px 0',
                  padding: '16px',
                  background: '#f8fafc',
                  borderRadius: 'var(--radius-md)',
                  border: '1px solid #e2e8f0',
                  textAlign: 'center',
                }}
              >
                <div style={{ fontSize: '0.75rem', color: '#64748b', fontWeight: 600, marginBottom: '8px' }}>
                  📐 SƠ ĐỒ / MINH HOẠ VECTOR CHUẨN:
                </div>
                <img
                  src={result.illustration_url}
                  alt="Minh hoạ bài toán"
                  style={{
                    maxHeight: '220px',
                    maxWidth: '100%',
                    objectFit: 'contain',
                    margin: '0 auto',
                    display: 'block',
                  }}
                />
              </div>
            )}

            {/* Statement */}
            <div
              style={{
                fontSize: '1.02rem',
                lineHeight: 1.65,
                color: '#1e293b',
                background: '#fdfefe',
                padding: '16px',
                borderRadius: '8px',
                border: '1px solid #f1f5f9',
                marginBottom: '20px',
              }}
            >
              <MathView content={result.problem.statement_vi || result.problem.statement} />
            </div>

            {/* Multiple-Choice Buttons */}
            {result.problem.choices && result.problem.choices.length > 0 && (
              <div style={{ marginBottom: '20px' }}>
                <div style={{ fontSize: '0.8rem', fontWeight: 700, color: '#64748b', marginBottom: '8px' }}>
                  HÃY CHỌN ĐÁP ÁN ĐÚNG:
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: '10px' }}>
                  {result.problem.choices.map((c) => {
                    const isSelected = selectedAnswer === c.key;
                    const isCorrectAnswer = c.key.trim().toUpperCase() === result.problem.answer.trim().toUpperCase();

                    let bg = '#ffffff';
                    let border = '1px solid #cbd5e1';
                    let textColor = '#1e293b';

                    if (selectedAnswer !== null) {
                      if (isCorrectAnswer) {
                        bg = '#ecfdf5';
                        border = '2px solid #10b981';
                        textColor = '#065f46';
                      } else if (isSelected) {
                        bg = '#fef2f2';
                        border = '2px solid #ef4444';
                        textColor = '#991b1b';
                      }
                    }

                    return (
                      <button
                        key={c.key}
                        type="button"
                        onClick={() => handleSelectChoice(c.key)}
                        style={{
                          background: bg,
                          border: border,
                          borderRadius: '10px',
                          padding: '12px 16px',
                          textAlign: 'left',
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '12px',
                          transition: 'all 0.15s ease',
                        }}
                      >
                        <span
                          style={{
                            width: '28px',
                            height: '28px',
                            borderRadius: '50%',
                            background: isSelected ? (isCorrectAnswer ? '#10b981' : '#ef4444') : '#f1f5f9',
                            color: isSelected ? '#ffffff' : '#475569',
                            fontWeight: 700,
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            flexShrink: 0,
                            fontSize: '0.85rem',
                          }}
                        >
                          {c.key}
                        </span>
                        <div style={{ color: textColor, fontSize: '0.92rem', flex: 1 }}>
                          <MathView content={c.text} />
                        </div>
                        {selectedAnswer !== null && isCorrectAnswer && <CheckCircle2 size={18} color="#10b981" />}
                        {selectedAnswer !== null && isSelected && !isCorrectAnswer && <XCircle size={18} color="#ef4444" />}
                      </button>
                    );
                  })}
                </div>

                {selectedAnswer !== null && (
                  <div
                    style={{
                      marginTop: '12px',
                      padding: '10px 14px',
                      borderRadius: '8px',
                      background: isAnswerCorrect ? '#ecfdf5' : '#fef2f2',
                      color: isAnswerCorrect ? '#065f46' : '#991b1b',
                      fontSize: '0.88rem',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px',
                    }}
                  >
                    {isAnswerCorrect ? (
                      <>
                        <CheckCircle2 size={18} />
                        <span><b>Chính xác!</b> Em đã trả lời đúng bài toán. Hãy xem lời giải chi tiết dưới đây.</span>
                      </>
                    ) : (
                      <>
                        <XCircle size={18} />
                        <span><b>Chưa chính xác!</b> Đáp án đúng là <b>{result.problem.answer}</b>. Hãy xem hướng dẫn từng bước.</span>
                      </>
                    )}
                  </div>
                )}
              </div>
            )}

            {/* Expandable Detailed Solution */}
            <div style={{ marginTop: '16px', borderTop: '1px solid #f1f5f9', paddingTop: '16px' }}>
              <button
                type="button"
                onClick={() => setShowSolution(!showSolution)}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  width: '100%',
                  background: 'none',
                  border: 'none',
                  padding: '8px 0',
                  color: '#0284c7',
                  fontSize: '0.92rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                }}
              >
                <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <BookOpen size={16} /> Lời Giải Chi Tiết Từng Bước
                </span>
                {showSolution ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
              </button>

              {showSolution && (
                <div
                  style={{
                    marginTop: '10px',
                    padding: '16px',
                    background: '#f8fafc',
                    borderRadius: '8px',
                    border: '1px solid #e2e8f0',
                  }}
                >
                  {result.problem.solution_steps && result.problem.solution_steps.length > 0 ? (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                      {result.problem.solution_steps.map((step, sIdx) => (
                        <div
                          key={sIdx}
                          style={{
                            paddingLeft: '12px',
                            borderLeft: '3px solid #0284c7',
                          }}
                        >
                          <div style={{ fontSize: '0.92rem', color: '#1e293b', lineHeight: 1.6 }}>
                            <MathView content={step.explain} />
                          </div>
                          {step.latex && (
                            <div style={{ marginTop: '4px' }}>
                              <MathView latex={step.latex} block />
                            </div>
                          )}
                        </div>
                      ))}
                    </div>
                  ) : (
                    <div style={{ fontSize: '0.9rem', color: '#334155' }}>
                      <MathView content={(result.problem as any).explanation || 'Không có giải thích chi tiết.'} />
                    </div>
                  )}

                  {/* Formula used */}
                  {(result.problem as any).formula_used && (
                    <div style={{ marginTop: '12px', paddingTop: '10px', borderTop: '1px dashed #cbd5e1', fontSize: '0.82rem', color: '#64748b' }}>
                      <b>Công thức cốt lõi:</b> {(result.problem as any).formula_used}
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* Expandable AI Thinking Process (if available) */}
            {result.thinking && (
              <div style={{ marginTop: '8px' }}>
                <button
                  type="button"
                  onClick={() => setShowThinking(!showThinking)}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    width: '100%',
                    background: 'none',
                    border: 'none',
                    padding: '8px 0',
                    color: '#64748b',
                    fontSize: '0.82rem',
                    cursor: 'pointer',
                  }}
                >
                  <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <Brain size={14} /> Xem chuỗi suy luận nội tâm AI (DeepSeek Reasoner)
                  </span>
                  {showThinking ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                </button>

                {showThinking && (
                  <pre
                    style={{
                      marginTop: '6px',
                      padding: '12px',
                      background: '#1e293b',
                      color: '#94a3b8',
                      borderRadius: '6px',
                      fontSize: '0.78rem',
                      lineHeight: 1.5,
                      whiteSpace: 'pre-wrap',
                      maxHeight: '200px',
                      overflowY: 'auto',
                    }}
                  >
                    {result.thinking}
                  </pre>
                )}
              </div>
            )}
          </div>
        )}
      </div>
    </div>,
    document.body
  );
};
