import { useState } from 'react';
import { MathView } from '../components/MathView';
import { Brain, RotateCcw, ThumbsUp, Zap, Check } from 'lucide-react';

import confetti from 'canvas-confetti';

interface Card {
  id: string;
  front: string;
  latex?: string;
  back: string;
  subject: string;
  topic: string;
}

const SAMPLE_CARDS: Card[] = [
  {
    id: 'c1',
    front: 'Định luật Coulomb trong chân không biểu diễn như thế nào?',
    latex: 'F = k\\dfrac{|q_1 q_2|}{r^2}',
    back: 'Lực tương tác tĩnh điện giữa hai điện tích điểm tỉ lệ thuận với tích độ lớn của hai điện tích và tỉ lệ nghịch với bình phương khoảng cách giữa chúng. Hằng số k = 9·10^9 N·m²/C².',
    subject: 'physics',
    topic: 'Điện Tích & Điện Trường',
  },
  {
    id: 'c2',
    front: 'Phương trình dao động điều hoà tổng quát và công thức chu kỳ con lắc lò xo?',
    latex: 'x = A\\cos(\\omega t + \\varphi),\\quad T = 2\\pi\\sqrt{\\dfrac{m}{k}}',
    back: 'Dao động điều hoà có li độ biến thiên điều hoà theo hàm sin hoặc cos. Chu kỳ T phụ thuộc vào khối lượng m và độ cứng lò xo k, độc lập với biên độ dao động.',
    subject: 'physics',
    topic: 'Dao Động Cơ Học',
  },
  {
    id: 'c3',
    front: 'Đạo hàm của hàm hợp y = f(u(x)) tính như thế nào?',
    latex: 'y\'_x = f\'_u \\cdot u\'_x',
    back: 'Quy tắc chuỗi (Chain Rule): Đạo hàm của hàm hợp bằng đạo hàm của hàm ngoài theo biến trung gian nhân với đạo hàm của hàm trong theo biến x.',
    subject: 'math',
    topic: 'Đạo Hàm & Giải Tích',
  },
  {
    id: 'c4',
    front: 'Định luật tác dụng khối lượng cho phản ứng thuận nghịch aA + bB ⇌ cC + dD?',
    latex: 'K_c = \\dfrac{[C]^c [D]^d}{[A]^a [B]^b}',
    back: 'Hằng số cân bằng Kc chỉ phụ thuộc vào bản chất phản ứng và nhiệt độ, không phụ thuộc vào nồng độ ban đầu của các chất.',
    subject: 'chemistry',
    topic: 'Cân Bằng Hoá Học',
  },
];

export const FlashcardsTab = () => {

  const [cards] = useState<Card[]>(SAMPLE_CARDS);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const [stats, setStats] = useState({ reviewed: 0, easy: 0, good: 0, hard: 0, again: 0 });

  const currentCard = cards[currentIndex % cards.length];

  const handleRate = (type: 'again' | 'hard' | 'good' | 'easy') => {
    setStats((prev) => ({
      ...prev,
      reviewed: prev.reviewed + 1,
      [type]: prev[type] + 1,
    }));

    if (type === 'easy') {
      confetti({ particleCount: 30, spread: 50 });
    }

    setFlipped(false);
    setCurrentIndex((prev) => (prev + 1) % cards.length);
  };

  return (
    <div className="tab-container animate-fade-in" style={{ maxWidth: '800px', margin: '0 auto' }}>
      {/* Header */}
      <div className="glass-panel" style={{ padding: '24px', marginBottom: '24px', textAlign: 'center' }}>
        <h2 style={{ fontSize: '1.75rem', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '10px' }}>
          <Brain style={{ color: '#a855f7' }} />
          <span>Hệ Thống Ôn Tập Giãn Cách Thông Minh (FSRS)</span>
        </h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.92rem', marginTop: '4px' }}>
          Tối ưu hoá khả năng ghi nhớ dài hạn theo thuật toán lặp lại ngắt quãng khoa học
        </p>
      </div>

      {/* Flashcard Component */}
      <div
        className="glass-panel"
        style={{
          minHeight: '340px',
          padding: '40px 30px',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          cursor: 'pointer',
          border: flipped ? '1px solid var(--accent-primary)' : '1px solid var(--border-subtle)',
          boxShadow: flipped ? 'var(--shadow-glow)' : 'var(--shadow-md)',
          transition: 'all 0.3s ease',
          marginBottom: '24px',
          position: 'relative',
        }}
        onClick={() => setFlipped(!flipped)}
      >
        <span style={{ position: 'absolute', top: '16px', left: '20px' }} className="badge badge-indigo">
          {currentCard.subject} · {currentCard.topic}
        </span>

        <span style={{ position: 'absolute', top: '16px', right: '20px', fontSize: '0.85rem', color: 'var(--text-muted)' }}>
          Thẻ {currentIndex + 1}/{cards.length} (Bấm để lật thẻ)
        </span>

        {!flipped ? (
          <div style={{ textAlign: 'center', maxWidth: '600px' }}>
            <h3 style={{ fontSize: '1.4rem', color: 'var(--text-primary)', lineHeight: 1.5, marginBottom: '20px', fontWeight: 700 }}>
              {currentCard.front}
            </h3>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.88rem' }}>
              👆 Bấm vào thẻ để xem công thức và lời giải thích
            </p>
          </div>
        ) : (
          <div className="animate-fade-in" style={{ textAlign: 'center', maxWidth: '650px' }}>
            {currentCard.latex && (
              <div style={{ background: '#f8fafc', border: '1px solid #e2e8f0', padding: '18px', borderRadius: 'var(--radius-md)', marginBottom: '18px' }}>
                <MathView latex={currentCard.latex} block={true} />
              </div>
            )}
            <p style={{ fontSize: '1rem', color: 'var(--text-primary)', lineHeight: 1.6 }}>
              {currentCard.back}
            </p>
          </div>
        )}
      </div>

      {/* FSRS Rating Buttons (Only shown when flipped) */}
      {flipped && (
        <div className="animate-fade-in" style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '12px', marginBottom: '24px' }}>
          <button className="btn btn-secondary" style={{ borderColor: 'rgba(239, 68, 68, 0.4)' }} onClick={() => handleRate('again')}>
            <RotateCcw size={16} style={{ color: '#ef4444' }} />
            <div>
              <div style={{ fontSize: '0.9rem', color: '#ef4444' }}>Lại (Again)</div>
              <div style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>&lt; 1 phút</div>
            </div>
          </button>

          <button className="btn btn-secondary" style={{ borderColor: 'rgba(245, 158, 11, 0.4)' }} onClick={() => handleRate('hard')}>
            <ThumbsUp size={16} style={{ color: '#f59e0b' }} />
            <div>
              <div style={{ fontSize: '0.9rem', color: '#f59e0b' }}>Khó (Hard)</div>
              <div style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>1 ngày</div>
            </div>
          </button>

          <button className="btn btn-secondary" style={{ borderColor: 'rgba(99, 102, 241, 0.4)' }} onClick={() => handleRate('good')}>
            <Check size={16} style={{ color: '#818cf8' }} />
            <div>
              <div style={{ fontSize: '0.9rem', color: '#818cf8' }}>Tốt (Good)</div>
              <div style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>3 ngày</div>
            </div>
          </button>

          <button className="btn btn-secondary" style={{ borderColor: 'rgba(16, 185, 129, 0.4)' }} onClick={() => handleRate('easy')}>
            <Zap size={16} style={{ color: '#10b981' }} />
            <div>
              <div style={{ fontSize: '0.9rem', color: '#10b981' }}>Dễ (Easy)</div>
              <div style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>7 ngày</div>
            </div>
          </button>
        </div>
      )}

      {/* Progress & Stats */}
      <div className="glass-panel" style={{ padding: '16px 24px', display: 'flex', justifyContent: 'space-around', fontSize: '0.85rem' }}>
        <div>Đã ôn tập: <strong>{stats.reviewed}</strong></div>
        <div>Dễ: <strong style={{ color: '#10b981' }}>{stats.easy}</strong></div>
        <div>Tốt: <strong style={{ color: '#818cf8' }}>{stats.good}</strong></div>
        <div>Khó: <strong style={{ color: '#f59e0b' }}>{stats.hard}</strong></div>
        <div>Lặp lại: <strong style={{ color: '#ef4444' }}>{stats.again}</strong></div>
      </div>
    </div>
  );
};
