import { useState, useRef, useEffect, type FC } from 'react';
import {
  Sparkles,
  X,
  Send,
  Loader2,
  Brain,
  Zap,
  ChevronDown,
  ChevronUp,
  RotateCcw,
  BookOpen,
  Atom,
  HelpCircle,
  Camera,
  BookmarkPlus,
  Check,
  GraduationCap,
  Compass,
  Copy,
  CheckCircle2,
  Volume2,
  VolumeX,
  ThumbsUp,
  ThumbsDown,
  Printer,
  Palette,
} from 'lucide-react';
import { MathView } from './MathView';
import { api } from '../services/api';

interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  image?: string;
  svg?: string;
  image_url?: string;
  thinking?: string;
  model?: string;

  pedagogical_mode?: string;
  grounding_formulas?: Array<{
    id: string;
    subject?: string;
    name_vi?: string;
    latex?: string;
    topic?: string;
  }>;
  grounding_lessons?: Array<{
    id: string;
    subject?: string;
    title_vi?: string;
    unit?: string;
  }>;
  cas_verification?: {
    success: boolean;
    operation: string;
    result?: string;
    latex?: string;
    solutions?: string[];
    solutions_latex?: string[];
    equation_latex?: string;
  };
  timestamp: Date;
}

interface AiTutorModalProps {
  isOpen: boolean;
  onClose: () => void;
  initialQuestion?: string;
}

const QUICK_PROMPTS = [
  '🎨 Vẽ hình minh hoạ tam giác vuông ABC có đường cao AH',
  '📈 Vẽ đồ thị hàm số parabol y = x^2 - 4x + 3 có đỉnh và trục đối xứng',
  '⚡ Giải thích định luật Ohm và cho ví dụ tính toán $I = U/R$',
  '📐 Chứng minh công thức đạo hàm hàm hợp $(f(u))\' = f\'(u) \\cdot u\'$',
  '🧪 Hướng dẫn cân bằng phản ứng oxi hoá - khử bằng phương pháp thăng bằng electron',
];

const STEM_QUICK_ACTIONS = [
  { label: '🎨 Vẽ Tam Giác', prompt: 'Vẽ hình minh hoạ tam giác vuông ABC vuông tại A có đường cao AH' },
  { label: '📈 Vẽ Parabol', prompt: 'Vẽ đồ thị hàm số parabol y = x^2 - 4x + 3 có trục đối xứng và đỉnh' },
  { label: '🌀 Tỉ Lệ Vàng', prompt: 'Vẽ hình xoắn ốc tỉ lệ vàng hình học Fibonacci' },
  { label: '📐 Giải PT', prompt: 'Giải phương trình 2x^2 - 5x + 2 = 0' },
  { label: '📈 Đạo hàm', prompt: 'Tính đạo hàm của x^3 * sin(x)' },
  { label: '🧪 Cân bằng Hoá', prompt: 'Cân bằng phản ứng: Fe + HNO3 -> Fe(NO3)3 + NO + H2O' },
];


export const AiTutorModal: FC<AiTutorModalProps> = ({ isOpen, onClose, initialQuestion }) => {
  const [model, setModel] = useState<'llama-3.3' | 'deepseek-r1'>('llama-3.3');
  const [pedagogicalMode, setPedagogicalMode] = useState<'socratic' | 'deep_dive' | 'scholarship'>('socratic');
  const [input, setInput] = useState('');
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [savedFlashcardIds, setSavedFlashcardIds] = useState<Record<string, boolean>>({});
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [speakingMsgId, setSpeakingMsgId] = useState<string | null>(null);
  const [feedbackState, setFeedbackState] = useState<Record<string, 'liked' | 'disliked'>>({});
  const [loading, setLoading] = useState(false);
  const [expandedThinking, setExpandedThinking] = useState<Record<string, boolean>>({});

  const handleCopyMessage = (msg: ChatMessage) => {
    navigator.clipboard.writeText(msg.content);
    setCopiedId(msg.id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const handleFeedback = async (msg: ChatMessage, rating: 1 | -1) => {
    try {
      const msgIdx = messages.findIndex((m) => m.id === msg.id);
      const userMsg = msgIdx > 0 ? messages[msgIdx - 1] : null;
      const instruction = userMsg ? userMsg.content : 'Câu hỏi học tập STEM';

      await fetch('/api/ai/feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          instruction: instruction,
          response: msg.content,
          subject: 'stem',
          pedagogical_mode: msg.pedagogical_mode || 'socratic',
          rating: rating,
          cas_verified: !!msg.cas_verification?.success,
        }),
      });
      setFeedbackState((prev) => ({ ...prev, [msg.id]: rating === 1 ? 'liked' : 'disliked' }));
    } catch (err) {
      console.error('Lỗi lưu phản hồi:', err);
    }
  };

  const handlePrintPdf = () => {
    window.print();
  };

  const cleanTextForSpeech = (text: string) => {
    return text
      .replace(/\$\$(.*?)\$\$/gs, ' công thức $1 ')
      .replace(/\$(.*?)\$/g, ' $1 ')
      .replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, ' $1 trên $2 ')
      .replace(/\\cdot|\\times/g, ' nhân ')
      .replace(/\\sqrt\{([^}]+)\}/g, ' căn bậc hai của $1 ')
      .replace(/\\rightarrow|->|→/g, ' tạo thành ')
      .replace(/[_*#`>]/g, '')
      .replace(/\n+/g, '. ')
      .trim();
  };

  const handleToggleSpeech = (msg: ChatMessage) => {
    if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
      alert('Trình duyệt của bạn chưa hỗ trợ đọc giọng nói Web Speech.');
      return;
    }

    if (speakingMsgId === msg.id) {
      window.speechSynthesis.cancel();
      setSpeakingMsgId(null);
      return;
    }

    window.speechSynthesis.cancel();
    const cleanText = cleanTextForSpeech(msg.content);
    const utterance = new SpeechSynthesisUtterance(cleanText);

    const voices = window.speechSynthesis.getVoices();
    const viVoice = voices.find((v) => v.lang.startsWith('vi') || v.lang.includes('VIE'));
    if (viVoice) {
      utterance.voice = viVoice;
    }
    utterance.lang = 'vi-VN';
    utterance.rate = 1.0;
    utterance.pitch = 1.0;

    utterance.onend = () => setSpeakingMsgId(null);
    utterance.onerror = () => setSpeakingMsgId(null);

    setSpeakingMsgId(msg.id);
    window.speechSynthesis.speak(utterance);
  };
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 'welcome',
      role: 'assistant',
      content:
        'Xin chào bạn! Mình là **Gia Sư AI AISTEM X** 🎓.\n\nMình được kết nối trực tiếp với toàn bộ kho tri thức **10 682 công thức & bài toán** cùng **1 018 bài giảng chuẩn hoá**. Hãy đặt câu hỏi, chụp ảnh bài tập hoặc tải ảnh bài nháp lên nhé!',
      timestamp: new Date(),
    },
  ]);

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (isOpen) {
      if (initialQuestion && initialQuestion.trim()) {
        handleSendMessage(initialQuestion.trim());
      }
      setTimeout(() => textareaRef.current?.focus(), 150);
    }
  }, [isOpen, initialQuestion]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  if (!isOpen) return null;

  const toggleThinking = (id: string) => {
    setExpandedThinking((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  const handleClearHistory = () => {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    setSpeakingMsgId(null);
    setMessages([
      {
        id: 'welcome-reset',
        role: 'assistant',
        content: 'Cuộc trò chuyện đã được làm mới. Bạn có câu hỏi hay bài toán STEM nào cần mình hỗ trợ không?',
        timestamp: new Date(),
      },
    ]);
  };

  const handleCloseModal = () => {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    setSpeakingMsgId(null);
    onClose();
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      if (typeof reader.result === 'string') {
        setSelectedImage(reader.result);
      }
    };
    reader.readAsDataURL(file);
    e.target.value = '';
  };

  const handleSaveFlashcard = async (msg: ChatMessage) => {
    try {
      await api.saveFlashcardFromAi({
        front: 'Kiến Thức & Công Thức từ Gia Sư AI AISTEM X',
        back: msg.content,
        subject: 'stem',
      });
      setSavedFlashcardIds((prev) => ({ ...prev, [msg.id]: true }));
    } catch (e) {
      console.error('Lỗi lưu thẻ ghi nhớ:', e);
    }
  };

  const handleSendMessage = async (textToSend?: string) => {
    const q = (textToSend || input).trim();
    if ((!q && !selectedImage) || loading) return;

    const userMsgId = 'user-' + Date.now();
    const currentImg = selectedImage;
    const newUserMessage: ChatMessage = {
      id: userMsgId,
      role: 'user',
      content: q || 'Phân tích và giải bài toán trong ảnh đính kèm này.',
      image: currentImg || undefined,
      timestamp: new Date(),
    };

    const newHistory = [...messages, newUserMessage];
    setMessages(newHistory);
    setInput('');
    setSelectedImage(null);
    setLoading(true);

    try {
      if (currentImg) {
        const data = await api.visionSolve(currentImg, q || undefined);
        const botMsgId = 'bot-' + Date.now();
        const botMessage: ChatMessage = {
          id: botMsgId,
          role: 'assistant',
          content: data.reply || 'Xin lỗi, không nhận được nội dung trả lời.',
          thinking: data.thinking || '',
          model: 'llama-3.2-vision',
          pedagogical_mode: pedagogicalMode,
          grounding_formulas: data.grounding_formulas || [],
          grounding_lessons: data.grounding_lessons || [],
          cas_verification: data.cas_verification || undefined,
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, botMessage]);
      } else {
        const historyPayload = newHistory
          .filter((m) => m.id !== 'welcome' && m.id !== 'welcome-reset')
          .slice(-6)
          .map((m) => ({
            role: m.role,
            content: m.content,
          }));

        const botMsgId = 'bot-' + Date.now();
        const placeholderMsg: ChatMessage = {
          id: botMsgId,
          role: 'assistant',
          content: '',
          thinking: '',
          model: model,
          pedagogical_mode: pedagogicalMode,
          grounding_formulas: [],
          grounding_lessons: [],
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, placeholderMsg]);

        try {
          const streamRes = await fetch('/api/ai/chat-stream', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              message: q,
              history: historyPayload,
              model: model,
              pedagogical_mode: pedagogicalMode,
            }),
          });

          if (!streamRes.ok || !streamRes.body) {
            throw new Error(`Streaming failed: ${streamRes.status}`);
          }

          const reader = streamRes.body.getReader();
          const decoder = new TextDecoder('utf-8');
          let buffer = '';
          let streamText = '';

          while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split('\n');
            buffer = lines.pop() || '';

            for (const line of lines) {
              const trimmed = line.trim();
              if (!trimmed.startsWith('data:')) continue;
              const payload = trimmed.slice(5).trim();
              if (!payload || payload === '[DONE]') continue;
              try {
                const item = JSON.parse(payload);
                if (item.type === 'metadata') {
                  setMessages((prev) =>
                    prev.map((m) =>
                      m.id === botMsgId
                        ? {
                            ...m,
                            cas_verification: item.cas_verification || undefined,
                            grounding_formulas: item.grounding_formulas || [],
                            grounding_lessons: item.grounding_lessons || [],
                            model: item.model || m.model,
                          }
                        : m
                    )
                  );
                } else if (item.type === 'delta') {
                  streamText += item.text;
                  setMessages((prev) =>
                    prev.map((m) => (m.id === botMsgId ? { ...m, content: streamText } : m))
                  );
                }
              } catch {
                // chunk JSON đang parse dở
              }
            }
          }
        } catch {
          // Dự phòng fallback sang REST API thông thường nếu stream bị ngắt
          const fallbackRes = await fetch('/api/ai/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              message: q,
              history: historyPayload,
              model: model,
              pedagogical_mode: pedagogicalMode,
            }),
          });
          const fallbackData = await fallbackRes.json();
          setMessages((prev) =>
            prev.map((m) =>
              m.id === botMsgId
                ? {
                    ...m,
                    content: fallbackData.reply || '',
                    thinking: fallbackData.thinking || '',
                    cas_verification: fallbackData.cas_verification || undefined,
                    grounding_formulas: fallbackData.grounding_formulas || [],
                    grounding_lessons: fallbackData.grounding_lessons || [],
                  }
                : m
            )
          );
        }

        // Tự động vẽ hình nếu câu hỏi có ý định vẽ sơ đồ/hình học
        const isDrawingIntent = /vẽ|hình vẽ|đồ thị|parabol|tam giác|hình học|minh hoạ|sơ đồ|hình tròn|lăng trụ|vectơ|vector|draw|diagram|illustration/i.test(q);
        if (isDrawingIntent) {
          try {
            const drawData = await api.aiDraw(q, 'both', 'math');
            if (drawData && (drawData.svg || drawData.image_url)) {
              setMessages((prev) =>
                prev.map((m) =>
                  m.id === botMsgId
                    ? {
                        ...m,
                        svg: drawData.svg || undefined,
                        image_url: drawData.image_url || undefined,
                      }
                    : m
                )
              );
            }
          } catch (drawErr) {
            console.warn('Lỗi vẽ hình AI kèm theo:', drawErr);
          }
        }
      }
    } catch (err: any) {
      const errMsgId = 'err-' + Date.now();

      setMessages((prev) => [
        ...prev,
        {
          id: errMsgId,
          role: 'assistant',
          content: `⚠️ **Đã xảy ra lỗi**: ${err.message || 'Không thể kết nối tới mô hình AI'}. Vui lòng thử lại.`,
          timestamp: new Date(),
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div
      className="stem-print-modal-wrapper"
      style={{
        position: 'fixed',
        inset: 0,
        zIndex: 1000,
        background: 'rgba(15, 23, 42, 0.55)',
        backdropFilter: 'blur(8px)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '16px',
      }}
      onClick={handleCloseModal}
    >
      <div
        className="stem-print-card"
        style={{
          width: '100%',
          maxWidth: '860px',
          height: '90vh',
          maxHeight: '840px',
          background: 'var(--bg-surface)',
          borderRadius: 'var(--radius-xl)',
          boxShadow: 'var(--shadow-lg), 0 0 35px rgba(2, 132, 199, 0.2)',
          border: '1px solid var(--border-subtle)',
          display: 'flex',
          flexDirection: 'column',
          overflow: 'hidden',
          animation: 'fadeIn 0.25s ease-out forwards',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <header
          style={{
            padding: '16px 20px',
            borderBottom: '1px solid var(--border-subtle)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            background: 'linear-gradient(135deg, rgba(2, 132, 199, 0.05), rgba(99, 102, 241, 0.04))',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <div
              style={{
                width: '38px',
                height: '38px',
                borderRadius: 'var(--radius-md)',
                background: 'linear-gradient(135deg, #0284c7, #6366f1)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: '#ffffff',
                boxShadow: '0 4px 12px rgba(2, 132, 199, 0.3)',
              }}
            >
              <Sparkles size={20} />
            </div>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: 'var(--text-primary)' }}>
                  Gia Sư AI STEM
                </h3>
                <span
                  style={{
                    fontSize: '0.72rem',
                    fontWeight: 600,
                    padding: '2px 8px',
                    borderRadius: 'var(--radius-full)',
                    background: 'rgba(2, 132, 199, 0.12)',
                    color: 'var(--accent-primary)',
                  }}
                >
                  Cloudflare Workers AI
                </span>
              </div>
              <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                Tư vấn học thuật, giải bài & chứng minh biểu tượng theo chuẩn Tam Giác Vàng
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            {/* Bộ chọn Model AI */}
            <div
              style={{
                display: 'flex',
                background: 'var(--bg-base)',
                padding: '3px',
                borderRadius: 'var(--radius-sm)',
                border: '1px solid var(--border-subtle)',
              }}
            >
              <button
                type="button"
                onClick={() => setModel('llama-3.3')}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '5px',
                  padding: '5px 10px',
                  fontSize: '0.78rem',
                  fontWeight: 600,
                  border: 'none',
                  borderRadius: '6px',
                  cursor: 'pointer',
                  background: model === 'llama-3.3' ? '#ffffff' : 'transparent',
                  color: model === 'llama-3.3' ? 'var(--accent-primary)' : 'var(--text-secondary)',
                  boxShadow: model === 'llama-3.3' ? 'var(--shadow-sm)' : 'none',
                  transition: 'all var(--transition-fast)',
                }}
                title="Llama 3.3 70B: Tốc độ cao, ngôn ngữ tự nhiên, giải thích khái niệm sư phạm"
              >
                <Zap size={13} />
                <span>Llama 3.3 (Nhanh)</span>
              </button>

              <button
                type="button"
                onClick={() => setModel('deepseek-r1')}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '5px',
                  padding: '5px 10px',
                  fontSize: '0.78rem',
                  fontWeight: 600,
                  border: 'none',
                  borderRadius: '6px',
                  cursor: 'pointer',
                  background: model === 'deepseek-r1' ? '#ffffff' : 'transparent',
                  color: model === 'deepseek-r1' ? '#6366f1' : 'var(--text-secondary)',
                  boxShadow: model === 'deepseek-r1' ? 'var(--shadow-sm)' : 'none',
                  transition: 'all var(--transition-fast)',
                }}
                title="DeepSeek R1: Mô hình suy luận toán học & logic sâu sắc, hiển thị quá trình tư duy"
              >
                <Brain size={13} />
                <span>DeepSeek R1 (Tư duy)</span>
              </button>
            </div>

            {/* Nút reset hội thoại */}
            <button
              type="button"
              className="no-print"
              onClick={handleClearHistory}
              style={{
                background: 'none',
                border: 'none',
                color: 'var(--text-muted)',
                cursor: 'pointer',
                padding: '6px',
                borderRadius: 'var(--radius-sm)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
              title="Làm mới đoạn chat"
            >
              <RotateCcw size={16} />
            </button>

            {/* Nút In / Xuất PDF */}
            <button
              type="button"
              className="no-print"
              onClick={handlePrintPdf}
              style={{
                background: 'none',
                border: 'none',
                color: 'var(--text-muted)',
                cursor: 'pointer',
                padding: '6px',
                borderRadius: 'var(--radius-sm)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
              title="Xuất bài giảng ra PDF / In ấn"
            >
              <Printer size={16} />
            </button>

            {/* Nút đóng */}
            <button
              type="button"
              className="no-print"
              onClick={handleCloseModal}
              style={{
                background: 'none',
                border: 'none',
                color: 'var(--text-muted)',
                cursor: 'pointer',
                padding: '6px',
                borderRadius: 'var(--radius-sm)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
              title="Đóng cửa sổ"
            >
              <X size={20} />
            </button>
          </div>
        </header>

        {/* Thanh Chọn Chế Độ Sư Phạm Học Đường (Pedagogical Mode Selector) */}
        <div
          className="no-print"
          style={{
            padding: '8px 20px',
            background: 'var(--bg-base)',
            borderBottom: '1px solid var(--border-subtle)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            flexWrap: 'wrap',
            gap: '8px',
            fontSize: '0.82rem',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: 'var(--text-secondary)', fontWeight: 600 }}>
            <span>Chế độ sư phạm:</span>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <button
              type="button"
              onClick={() => setPedagogicalMode('socratic')}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '4px',
                padding: '4px 10px',
                borderRadius: 'var(--radius-full)',
                border: '1px solid',
                fontSize: '0.78rem',
                fontWeight: 600,
                cursor: 'pointer',
                background: pedagogicalMode === 'socratic' ? '#eff6ff' : '#ffffff',
                borderColor: pedagogicalMode === 'socratic' ? '#3b82f6' : 'var(--border-subtle)',
                color: pedagogicalMode === 'socratic' ? '#1d4ed8' : 'var(--text-secondary)',
                transition: 'all 0.15s ease',
              }}
              title="Gia sư Socratic: Đặt câu hỏi gợi mở từng bước, không giải hộ"
            >
              <GraduationCap size={13} />
              <span>🎓 Socratic (Gợi mở)</span>
            </button>

            <button
              type="button"
              onClick={() => setPedagogicalMode('deep_dive')}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '4px',
                padding: '4px 10px',
                borderRadius: 'var(--radius-full)',
                border: '1px solid',
                fontSize: '0.78rem',
                fontWeight: 600,
                cursor: 'pointer',
                background: pedagogicalMode === 'deep_dive' ? '#f0fdf4' : '#ffffff',
                borderColor: pedagogicalMode === 'deep_dive' ? '#22c55e' : 'var(--border-subtle)',
                color: pedagogicalMode === 'deep_dive' ? '#15803d' : 'var(--text-secondary)',
                transition: 'all 0.15s ease',
              }}
              title="Chứng minh bản chất: Đi sâu vào nguồn gốc toán học, giải tích và tiên đề"
            >
              <Compass size={13} />
              <span>🔍 Bản chất (Chứng minh)</span>
            </button>

            <button
              type="button"
              onClick={() => setPedagogicalMode('scholarship')}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '4px',
                padding: '4px 10px',
                borderRadius: 'var(--radius-full)',
                border: '1px solid',
                fontSize: '0.78rem',
                fontWeight: 600,
                cursor: 'pointer',
                background: pedagogicalMode === 'scholarship' ? '#fef3c7' : '#ffffff',
                borderColor: pedagogicalMode === 'scholarship' ? '#f59e0b' : 'var(--border-subtle)',
                color: pedagogicalMode === 'scholarship' ? '#b45309' : 'var(--text-secondary)',
                transition: 'all 0.15s ease',
              }}
              title="Săn học bổng: Kết nối bài toán với đề tài nghiên cứu và hồ sơ du học"
            >
              <Sparkles size={13} />
              <span>🌍 Săn Học Bổng</span>
            </button>
          </div>
        </div>

        {/* Nội dung tin nhắn */}
        <div
          style={{
            flex: 1,
            overflowY: 'auto',
            padding: '20px',
            display: 'flex',
            flexDirection: 'column',
            gap: '18px',
          }}
        >
          {messages.map((msg) => (
            <div
              key={msg.id}
              style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: msg.role === 'user' ? 'flex-end' : 'flex-start',
                gap: '6px',
              }}
            >
              {/* Thẻ người gửi */}
              <div
                style={{
                  fontSize: '0.75rem',
                  fontWeight: 600,
                  color: 'var(--text-muted)',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                }}
              >
                {msg.role === 'user' ? (
                  <span>Bạn</span>
                ) : (
                  <>
                    <Sparkles size={12} color="var(--accent-primary)" />
                    <span>Gia Sư AI STEM</span>
                    {msg.model && (
                      <span
                        style={{
                          fontSize: '0.68rem',
                          background: 'rgba(15, 23, 42, 0.06)',
                          padding: '1px 6px',
                          borderRadius: '4px',
                        }}
                      >
                        {msg.model.includes('deepseek') ? 'DeepSeek R1' : 'Llama 3.3'}
                      </span>
                    )}
                  </>
                )}
              </div>

              {/* Khối suy nghĩ nếu có từ DeepSeek R1 */}
              {msg.thinking && (
                <div
                  style={{
                    maxWidth: '85%',
                    background: 'rgba(99, 102, 241, 0.05)',
                    border: '1px dashed rgba(99, 102, 241, 0.3)',
                    borderRadius: 'var(--radius-sm)',
                    overflow: 'hidden',
                    fontSize: '0.82rem',
                  }}
                >
                  <button
                    type="button"
                    onClick={() => toggleThinking(msg.id)}
                    style={{
                      width: '100%',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      padding: '8px 12px',
                      background: 'none',
                      border: 'none',
                      cursor: 'pointer',
                      color: '#4f46e5',
                      fontWeight: 600,
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <Brain size={14} />
                      <span>Quá trình tư duy phân tích (Reasoning Trace)</span>
                    </div>
                    {expandedThinking[msg.id] ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
                  </button>

                  {expandedThinking[msg.id] && (
                    <div
                      style={{
                        padding: '10px 14px',
                        borderTop: '1px dashed rgba(99, 102, 241, 0.2)',
                        color: 'var(--text-secondary)',
                        lineHeight: 1.6,
                        whiteSpace: 'pre-wrap',
                        fontFamily: 'var(--font-mono)',
                        fontSize: '0.78rem',
                      }}
                    >
                      {msg.thinking}
                    </div>
                  )}
                </div>
              )}

              {/* Ảnh đính kèm (nếu có) */}
              {msg.image && (
                <div style={{ maxWidth: '85%', marginBottom: '4px' }}>
                  <img
                    src={msg.image}
                    alt="Đề bài tải lên"
                    style={{
                      maxWidth: '260px',
                      maxHeight: '180px',
                      borderRadius: '8px',
                      objectFit: 'contain',
                      border: '1px solid var(--border-subtle)',
                      boxShadow: 'var(--shadow-sm)',
                    }}
                  />
                </div>
              )}

              {/* Huy hiệu xác thực toán học CAS SymPy */}
              {msg.cas_verification && msg.cas_verification.success && (
                <div
                  style={{
                    maxWidth: '85%',
                    marginBottom: '8px',
                    padding: '8px 14px',
                    borderRadius: '8px',
                    background: 'linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%)',
                    border: '1px solid #86efac',
                    boxShadow: '0 1px 3px rgba(22, 163, 74, 0.08)',
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: '#15803d', fontWeight: 700, fontSize: '0.78rem' }}>
                    <CheckCircle2 size={14} color="#16a34a" />
                    <span>XÁC THỰC BỞI ENGINE ĐẠI SỐ BIỂU TƯỢNG SYMPY (CHÍNH XÁC 100%)</span>
                  </div>
                  <div style={{ fontSize: '0.84rem', color: '#166534', marginTop: '4px' }}>
                    Phép toán: <strong>{msg.cas_verification.operation}</strong> &bull; Kết quả: {msg.cas_verification.latex ? `$${msg.cas_verification.latex}$` : (msg.cas_verification.result || msg.cas_verification.solutions?.join(', '))}
                  </div>
                </div>
              )}

              {/* Sơ đồ hình học Vector SVG */}
              {msg.svg && (
                <div
                  style={{
                    maxWidth: '85%',
                    marginBottom: '10px',
                    padding: '12px',
                    background: '#f8fafc',
                    borderRadius: '12px',
                    border: '1px solid #cbd5e1',
                    boxShadow: '0 2px 8px rgba(0,0,0,0.06)',
                    overflow: 'hidden',
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px', borderBottom: '1px solid #e2e8f0', paddingBottom: '6px' }}>
                    <span style={{ fontSize: '0.8rem', fontWeight: 700, color: '#475569', display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <Sparkles size={14} color="#7c3aed" /> Sơ đồ Hình học Vector SVG
                    </span>
                    <span style={{ fontSize: '0.72rem', color: '#64748b' }}>Sắc nét &bull; Chuẩn tọa độ</span>
                  </div>
                  <div
                    dangerouslySetInnerHTML={{ __html: msg.svg }}
                    style={{ width: '100%', maxHeight: '380px', display: 'flex', justifyContent: 'center' }}
                  />
                </div>
              )}

              {/* Minh họa 3D / Nghệ thuật (FLUX.1 AI) */}
              {msg.image_url && (
                <div
                  style={{
                    maxWidth: '85%',
                    marginBottom: '10px',
                    padding: '10px',
                    background: '#ffffff',
                    borderRadius: '12px',
                    border: '1px solid #e2e8f0',
                    boxShadow: 'var(--shadow-md)',
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
                    <span style={{ fontSize: '0.8rem', fontWeight: 700, color: '#0284c7', display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <Palette size={14} color="#0284c7" /> Minh họa Toán học 3D (Cloudflare FLUX.1)
                    </span>
                    <a
                      href={msg.image_url}
                      download="aistemx-math-illustration.jpg"
                      style={{ fontSize: '0.74rem', color: '#0284c7', textDecoration: 'none', fontWeight: 600 }}
                    >
                      Tải ảnh gốc (1024x1024)
                    </a>
                  </div>
                  <img
                    src={msg.image_url}
                    alt="Minh họa toán học FLUX.1"
                    style={{
                      width: '100%',
                      maxHeight: '380px',
                      objectFit: 'contain',
                      borderRadius: '8px',
                    }}
                  />
                </div>
              )}

              {/* Bong bóng tin nhắn */}
              <div

                style={{
                  maxWidth: '85%',
                  padding: '14px 18px',
                  borderRadius:
                    msg.role === 'user'
                      ? '18px 18px 4px 18px'
                      : '18px 18px 18px 4px',
                  background:
                    msg.role === 'user'
                      ? 'linear-gradient(135deg, #0284c7, #0369a1)'
                      : 'var(--bg-surface)',
                  color: msg.role === 'user' ? '#ffffff' : 'var(--text-primary)',
                  border:
                    msg.role === 'user'
                      ? 'none'
                      : '1px solid var(--border-subtle)',
                  boxShadow:
                    msg.role === 'user'
                      ? '0 2px 8px rgba(2, 132, 199, 0.25)'
                      : 'var(--shadow-sm)',
                  fontSize: '0.92rem',
                  lineHeight: 1.65,
                }}
              >
                <MathView content={msg.content} />
              </div>

              {/* Các nút hành động của trợ lý (Flashcard & Sao chép & Đọc & Đánh giá) */}
              {msg.role === 'assistant' && msg.id !== 'welcome' && msg.id !== 'welcome-reset' && (
                <div
                  className="no-print"
                  style={{ maxWidth: '85%', marginTop: '4px', display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}
                >
                  <button
                    type="button"
                    onClick={() => handleSaveFlashcard(msg)}
                    disabled={savedFlashcardIds[msg.id]}
                    style={{
                      display: 'inline-flex',
                      alignItems: 'center',
                      gap: '5px',
                      padding: '4px 10px',
                      borderRadius: 'var(--radius-sm)',
                      background: savedFlashcardIds[msg.id] ? '#dcfce7' : '#f8fafc',
                      border: '1px solid ' + (savedFlashcardIds[msg.id] ? '#86efac' : '#e2e8f0'),
                      color: savedFlashcardIds[msg.id] ? '#15803d' : '#64748b',
                      fontSize: '0.74rem',
                      fontWeight: 600,
                      cursor: savedFlashcardIds[msg.id] ? 'default' : 'pointer',
                      transition: 'all var(--transition-fast)',
                    }}
                    title="Lưu kiến thức này vào Bộ thẻ Ghi nhớ FSRS để ôn tập lặp lại ngắt quãng"
                  >
                    {savedFlashcardIds[msg.id] ? <Check size={12} color="#15803d" /> : <BookmarkPlus size={12} />}
                    <span>{savedFlashcardIds[msg.id] ? '✓ Đã Lưu Vào Thẻ Ghi Nhớ' : '📌 Thêm vào Flashcard FSRS'}</span>
                  </button>

                  <button
                    type="button"
                    onClick={() => handleCopyMessage(msg)}
                    style={{
                      display: 'inline-flex',
                      alignItems: 'center',
                      gap: '5px',
                      padding: '4px 10px',
                      borderRadius: 'var(--radius-sm)',
                      background: copiedId === msg.id ? '#f0fdf4' : '#f8fafc',
                      border: '1px solid ' + (copiedId === msg.id ? '#86efac' : '#e2e8f0'),
                      color: copiedId === msg.id ? '#15803d' : '#64748b',
                      fontSize: '0.74rem',
                      fontWeight: 600,
                      cursor: 'pointer',
                      transition: 'all var(--transition-fast)',
                    }}
                    title="Sao chép toàn bộ lời giải và định dạng KaTeX"
                  >
                    {copiedId === msg.id ? <Check size={12} color="#15803d" /> : <Copy size={12} />}
                    <span>{copiedId === msg.id ? '✓ Đã sao chép' : '📋 Sao chép lời giải'}</span>
                  </button>

                  <button
                    type="button"
                    onClick={() => handleToggleSpeech(msg)}
                    style={{
                      display: 'inline-flex',
                      alignItems: 'center',
                      gap: '5px',
                      padding: '4px 10px',
                      borderRadius: 'var(--radius-sm)',
                      background: speakingMsgId === msg.id ? '#fef3c7' : '#f8fafc',
                      border: '1px solid ' + (speakingMsgId === msg.id ? '#f59e0b' : '#e2e8f0'),
                      color: speakingMsgId === msg.id ? '#b45309' : '#64748b',
                      fontSize: '0.74rem',
                      fontWeight: 600,
                      cursor: 'pointer',
                      transition: 'all var(--transition-fast)',
                    }}
                    title="Nghe AI giảng giải bằng giọng đọc tiếng Việt"
                  >
                    {speakingMsgId === msg.id ? <VolumeX size={12} color="#b45309" /> : <Volume2 size={12} />}
                    <span>{speakingMsgId === msg.id ? '⏸ Dừng đọc' : '🔊 Nghe giảng'}</span>
                  </button>

                  {/* Đánh giá phản hồi & thu thập mẫu huấn luyện Gold Dataset */}
                  <div style={{ display: 'inline-flex', alignItems: 'center', gap: '3px', marginLeft: 'auto' }}>
                    <button
                      type="button"
                      onClick={() => handleFeedback(msg, 1)}
                      style={{
                        display: 'inline-flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        padding: '4px 8px',
                        borderRadius: 'var(--radius-sm)',
                        background: feedbackState[msg.id] === 'liked' ? '#dcfce7' : '#f8fafc',
                        border: '1px solid ' + (feedbackState[msg.id] === 'liked' ? '#86efac' : '#e2e8f0'),
                        color: feedbackState[msg.id] === 'liked' ? '#15803d' : '#64748b',
                        cursor: 'pointer',
                        fontSize: '0.74rem',
                        fontWeight: 600,
                        gap: '4px',
                        transition: 'all var(--transition-fast)',
                      }}
                      title="Lời giải chính xác, chuẩn sư phạm (Thu thập vào Gold Dataset để huấn luyện AI)"
                    >
                      <ThumbsUp size={12} />
                      <span>{feedbackState[msg.id] === 'liked' ? 'Hữu ích' : ''}</span>
                    </button>
                    <button
                      type="button"
                      onClick={() => handleFeedback(msg, -1)}
                      style={{
                        display: 'inline-flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        padding: '4px 8px',
                        borderRadius: 'var(--radius-sm)',
                        background: feedbackState[msg.id] === 'disliked' ? '#fee2e2' : '#f8fafc',
                        border: '1px solid ' + (feedbackState[msg.id] === 'disliked' ? '#fca5a5' : '#e2e8f0'),
                        color: feedbackState[msg.id] === 'disliked' ? '#b91c1c' : '#64748b',
                        cursor: 'pointer',
                        fontSize: '0.74rem',
                        fontWeight: 600,
                        gap: '4px',
                        transition: 'all var(--transition-fast)',
                      }}
                      title="Chưa chính xác hoặc cần cải thiện"
                    >
                      <ThumbsDown size={12} />
                      <span>{feedbackState[msg.id] === 'disliked' ? 'Chưa chuẩn' : ''}</span>
                    </button>
                  </div>
                </div>
              )}

              {/* Grounding Citations (Nguồn đối chiếu chuẩn trong kho AISTEM) */}
              {msg.role === 'assistant' &&
                ((msg.grounding_formulas && msg.grounding_formulas.length > 0) ||
                  (msg.grounding_lessons && msg.grounding_lessons.length > 0)) && (
                  <div
                    style={{
                      maxWidth: '85%',
                      marginTop: '4px',
                      padding: '8px 12px',
                      background: 'rgba(2, 132, 199, 0.04)',
                      borderRadius: 'var(--radius-sm)',
                      border: '1px solid rgba(2, 132, 199, 0.15)',
                      display: 'flex',
                      flexDirection: 'column',
                      gap: '6px',
                    }}
                  >
                    <div
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: '6px',
                        fontSize: '0.74rem',
                        fontWeight: 700,
                        color: 'var(--accent-primary)',
                        textTransform: 'uppercase',
                        letterSpacing: '0.04em',
                      }}
                    >
                      <BookOpen size={12} />
                      <span>Tham chiếu trực tiếp từ Kho AISTEM X</span>
                    </div>

                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                      {msg.grounding_formulas?.map((gf) => (
                        <div
                          key={gf.id}
                          style={{
                            fontSize: '0.75rem',
                            background: '#ffffff',
                            border: '1px solid var(--border-subtle)',
                            padding: '3px 8px',
                            borderRadius: '4px',
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '4px',
                            color: 'var(--text-secondary)',
                          }}
                          title={`LaTeX: ${gf.latex}`}
                        >
                          <Atom size={11} color="var(--accent-primary)" />
                          <span>{gf.name_vi}</span>
                        </div>
                      ))}

                      {msg.grounding_lessons?.map((gl) => (
                        <div
                          key={gl.id}
                          style={{
                            fontSize: '0.75rem',
                            background: '#ffffff',
                            border: '1px solid var(--border-subtle)',
                            padding: '3px 8px',
                            borderRadius: '4px',
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '4px',
                            color: 'var(--text-secondary)',
                          }}
                        >
                          <BookOpen size={11} color="#059669" />
                          <span>{gl.title_vi}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
            </div>
          ))}

          {loading && (
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--text-muted)' }}>
              <Loader2 size={18} className="animate-spin" color="var(--accent-primary)" />
              <span style={{ fontSize: '0.85rem' }}>
                {model === 'deepseek-r1'
                  ? 'DeepSeek R1 đang tư duy suy luận & tra cứu kho dữ liệu AISTEM X...'
                  : 'Gia sư AI đang phân tích bài học & soạn câu trả lời...'}
              </span>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Quick Prompts khi mới vào chat */}
        {messages.length <= 2 && !loading && (
          <div
            style={{
              padding: '8px 20px 12px',
              display: 'flex',
              flexWrap: 'wrap',
              gap: '6px',
              borderTop: '1px solid var(--border-subtle)',
              background: 'var(--bg-base)',
            }}
          >
            <div
              style={{
                width: '100%',
                fontSize: '0.72rem',
                fontWeight: 600,
                color: 'var(--text-muted)',
                marginBottom: '2px',
                display: 'flex',
                alignItems: 'center',
                gap: '4px',
              }}
            >
              <HelpCircle size={12} />
              <span>Gợi ý câu hỏi nhanh:</span>
            </div>
            {QUICK_PROMPTS.map((promptText, idx) => (
              <button
                key={idx}
                type="button"
                onClick={() => handleSendMessage(promptText)}
                style={{
                  background: '#ffffff',
                  border: '1px solid var(--border-subtle)',
                  borderRadius: 'var(--radius-full)',
                  padding: '5px 12px',
                  fontSize: '0.78rem',
                  color: 'var(--text-secondary)',
                  cursor: 'pointer',
                  textAlign: 'left',
                  transition: 'all var(--transition-fast)',
                }}
                className="hover-card"
              >
                {promptText}
              </button>
            ))}
          </div>
        )}

        {/* Thanh phím tắt STEM Nhanh */}
        <div
          style={{
            padding: '6px 20px',
            background: 'var(--bg-base)',
            borderTop: '1px solid var(--border-subtle)',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
            overflowX: 'auto',
            whiteSpace: 'nowrap',
          }}
        >
          <span style={{ fontSize: '0.72rem', fontWeight: 700, color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px', flexShrink: 0 }}>
            <Atom size={12} />
            <span>Mẫu STEM:</span>
          </span>
          {STEM_QUICK_ACTIONS.map((item, i) => (
            <button
              key={i}
              type="button"
              onClick={() => {
                setInput(item.prompt);
                textareaRef.current?.focus();
              }}
              style={{
                padding: '3px 9px',
                borderRadius: 'var(--radius-sm)',
                border: '1px solid var(--border-subtle)',
                background: '#ffffff',
                fontSize: '0.74rem',
                fontWeight: 600,
                color: 'var(--text-secondary)',
                cursor: 'pointer',
                transition: 'all 0.15s ease',
                flexShrink: 0,
              }}
              className="hover-card"
              title={item.prompt}
            >
              {item.label}
            </button>
          ))}
        </div>

        {/* Ô nhập liệu tin nhắn */}
        <footer
          className="no-print"
          style={{
            padding: '14px 20px',
            borderTop: '1px solid var(--border-subtle)',
            background: 'var(--bg-surface)',
          }}
        >
          {/* Xem trước ảnh tải lên (nếu có) */}
          {selectedImage && (
            <div
              style={{
                marginBottom: '10px',
                padding: '8px 12px',
                borderRadius: 'var(--radius-md)',
                background: '#f1f5f9',
                border: '1px solid #cbd5e1',
                display: 'flex',
                alignItems: 'center',
                gap: '10px',
              }}
            >
              <img
                src={selectedImage}
                alt="Xem trước ảnh đề bài"
                style={{ width: '44px', height: '44px', objectFit: 'cover', borderRadius: '6px', border: '1px solid #94a3b8' }}
              />
              <div style={{ flex: 1, fontSize: '0.82rem', color: '#334155' }}>
                <div style={{ fontWeight: 700, color: '#0284c7' }}>Đã đính kèm ảnh đề bài / bài giải</div>
                <div style={{ fontSize: '0.74rem', color: '#64748b' }}>AI Llama 3.2 Vision sẽ trích xuất KaTeX và hướng dẫn tư duy</div>
              </div>
              <button
                type="button"
                onClick={() => setSelectedImage(null)}
                style={{
                  background: 'none',
                  border: 'none',
                  color: '#64748b',
                  cursor: 'pointer',
                  padding: '4px',
                }}
                title="Gỡ ảnh"
              >
                <X size={16} />
              </button>
            </div>
          )}

          <div
            style={{
              display: 'flex',
              alignItems: 'flex-end',
              gap: '10px',
              background: 'var(--bg-base)',
              border: '1px solid var(--border-subtle)',
              borderRadius: 'var(--radius-lg)',
              padding: '8px 12px',
              transition: 'border-color var(--transition-fast)',
            }}
          >
            {/* Input file ẩn cho upload ảnh */}
            <input
              type="file"
              ref={fileInputRef}
              accept="image/*"
              style={{ display: 'none' }}
              onChange={handleFileSelect}
            />

            {/* Nút Upload ảnh / Camera */}
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              style={{
                width: '36px',
                height: '36px',
                borderRadius: '50%',
                border: '1px solid ' + (selectedImage ? '#38bdf8' : 'var(--border-subtle)'),
                background: selectedImage ? '#e0f2fe' : '#ffffff',
                color: selectedImage ? '#0284c7' : '#64748b',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: 'pointer',
                flexShrink: 0,
                transition: 'all var(--transition-fast)',
              }}
              title="Chụp ảnh đề bài hoặc tải ảnh viết tay để AI nhận diện (Vision OCR)"
            >
              <Camera size={18} />
            </button>

            {/* Nút Vẽ hình minh hoạ Toán học */}
            <button
              type="button"
              onClick={() => {
                const samplePrompt = 'Vẽ hình minh hoạ tam giác vuông ABC có đường cao AH';
                setInput(samplePrompt);
                textareaRef.current?.focus();
              }}
              style={{
                width: '36px',
                height: '36px',
                borderRadius: '50%',
                border: '1px solid #c084fc',
                background: '#faf5ff',
                color: '#7e22ce',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: 'pointer',
                flexShrink: 0,
                transition: 'all var(--transition-fast)',
              }}
              title="Vẽ sơ đồ hình học & minh hoạ toán học bằng AI (FLUX.1 & SVG)"
            >
              <Palette size={17} />
            </button>


            <textarea
              ref={textareaRef}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder={
                selectedImage
                  ? 'Nhập thêm yêu cầu cho ảnh đề bài (hoặc bấm Gửi để AI phân tích ngay)...'
                  : 'Nhập câu hỏi, công thức toán hoặc bấm icon Camera để tải ảnh đề bài (Enter để gửi)...'
              }
              disabled={loading}
              rows={2}
              style={{
                flex: 1,
                border: 'none',
                outline: 'none',
                background: 'transparent',
                resize: 'none',
                fontSize: '0.9rem',
                fontFamily: 'inherit',
                color: 'var(--text-primary)',
                lineHeight: 1.5,
              }}
            />

            <button
              type="button"
              onClick={() => handleSendMessage()}
              disabled={(!input.trim() && !selectedImage) || loading}
              style={{
                width: '38px',
                height: '38px',
                borderRadius: '50%',
                border: 'none',
                background:
                  (!input.trim() && !selectedImage) || loading
                    ? 'var(--border-subtle)'
                    : 'linear-gradient(135deg, #0284c7, #0369a1)',
                color: '#ffffff',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: (!input.trim() && !selectedImage) || loading ? 'not-allowed' : 'pointer',
                transition: 'all var(--transition-fast)',
                boxShadow: (input.trim() || selectedImage) && !loading ? '0 2px 8px rgba(2, 132, 199, 0.35)' : 'none',
              }}
              title="Gửi câu hỏi"
            >
              <Send size={16} />
            </button>
          </div>
          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              marginTop: '6px',
              fontSize: '0.72rem',
              color: 'var(--text-muted)',
              padding: '0 4px',
            }}
          >
            <span>Hỗ trợ KaTeX ($...$ và $$...$$) cho mọi công thức Toán · Lí · Hoá</span>
            <span>Mô hình: Cloudflare Workers AI ({model === 'deepseek-r1' ? 'DeepSeek R1' : 'Llama 3.3 70B'})</span>
          </div>
        </footer>
      </div>
    </div>
  );
};
