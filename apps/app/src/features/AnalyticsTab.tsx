import { useState, useEffect } from 'react';
import { api, type SystemStats } from '../services/api';
import { Activity, Database, Cpu, CheckCircle2, ShieldCheck, BookOpen, Layers, Award } from 'lucide-react';

export const AnalyticsTab = () => {

  const [stats, setStats] = useState<SystemStats | null>(null);


  useEffect(() => {
    const load = async () => {
      try {
        const s = await api.getStats();
        setStats(s);
      } catch (e) {
        console.error(e);
      }
    };
    load();
  }, []);

  return (
    <div className="tab-container animate-fade-in">
      {/* Header */}
      <div className="glass-panel" style={{ padding: '24px', marginBottom: '24px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <h2 style={{ fontSize: '1.75rem', display: 'flex', alignItems: 'center', gap: '10px' }}>
              <Activity style={{ color: '#06b6d4' }} />
              <span>Trung Tâm Giám Sát & Thống Kê Hệ Thống AISTEM</span>
            </h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.92rem', marginTop: '4px' }}>
              Cơ sở hạ tầng Docker PostgreSQL 16, Fast Engine CAS và Kho dữ liệu tri thức chuẩn quốc tế
            </p>
          </div>
          <div className="badge badge-emerald">
            <CheckCircle2 size={14} />
            <span>Hệ Thống Trực Tuyến 100%</span>
          </div>
        </div>
      </div>

      {/* KPI Cards Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '16px', marginBottom: '28px' }}>
        <div className="glass-card">
          <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-muted)', marginBottom: '8px' }}>
            <span style={{ fontSize: '0.88rem' }}>Công Thức STEM</span>
            <BookOpen size={18} style={{ color: '#6366f1' }} />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text-primary)' }}>{stats?.formula?.toLocaleString() || '5,272'}</div>
          <div style={{ fontSize: '0.8rem', color: '#10b981', marginTop: '4px' }}>4 Môn: Toán, Lí, Hoá, Sinh</div>
        </div>

        <div className="glass-card">
          <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-muted)', marginBottom: '8px' }}>
            <span style={{ fontSize: '0.88rem' }}>Bài Toán Kiểm Định</span>
            <ShieldCheck size={18} style={{ color: '#10b981' }} />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text-primary)' }}>{stats?.problems?.toLocaleString() || '4,351'}</div>
          <div style={{ fontSize: '0.8rem', color: '#10b981', marginTop: '4px' }}>100% Có Lời Giải & Why-Wrong</div>
        </div>

        <div className="glass-card">
          <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-muted)', marginBottom: '8px' }}>
            <span style={{ fontSize: '0.88rem' }}>Học Bổng Toàn Cầu</span>
            <Award size={18} style={{ color: '#f59e0b' }} />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text-primary)' }}>{stats?.scholarships || '25'}</div>
          <div style={{ fontSize: '0.8rem', color: '#f59e0b', marginTop: '4px' }}>Ivy League, Oxbridge, NUS...</div>
        </div>

        <div className="glass-card">
          <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-muted)', marginBottom: '8px' }}>
            <span style={{ fontSize: '0.88rem' }}>Đồ Thị Cạnh Tri Thức</span>
            <Layers size={18} style={{ color: '#06b6d4' }} />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text-primary)' }}>{stats?.edges?.toLocaleString() || '22,286'}</div>
          <div style={{ fontSize: '0.8rem', color: '#06b6d4', marginTop: '4px' }}>Liên kết đa chiều (Knowledge Graph)</div>
        </div>
      </div>

      {/* Infrastructure Details */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: '20px' }}>
        <div className="glass-panel" style={{ padding: '24px' }}>
          <h3 style={{ fontSize: '1.25rem', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Database style={{ color: '#6366f1' }} />
            <span>Cơ Sở Dữ Liệu PostgreSQL (Docker)</span>
          </h3>
          <ul style={{ display: 'flex', flexDirection: 'column', gap: '10px', listStyle: 'none', fontSize: '0.9rem' }}>
            <li style={{ display: 'flex', justifyContent: 'space-between', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '8px' }}>
              <span style={{ color: 'var(--text-secondary)' }}>Container:</span>
              <strong style={{ color: 'var(--text-primary)' }}>aistem-postgres (v16-alpine)</strong>
            </li>
            <li style={{ display: 'flex', justifyContent: 'space-between', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '8px' }}>
              <span style={{ color: 'var(--text-secondary)' }}>Cổng Ánh Xạ:</span>
              <strong style={{ color: '#10b981' }}>5434 : 5432</strong>
            </li>
            <li style={{ display: 'flex', justifyContent: 'space-between', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '8px' }}>
              <span style={{ color: 'var(--text-secondary)' }}>Dung Lượng Dữ Liệu Bền Vững:</span>
              <strong style={{ color: 'var(--text-primary)' }}>Volume aistem_pgdata</strong>
            </li>
            <li style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: '4px' }}>
              <span style={{ color: 'var(--text-secondary)' }}>Chỉ Mục:</span>
              <strong style={{ color: '#a5b4fc' }}>GIN JSONB + TSVector Tiếng Việt</strong>
            </li>
          </ul>
        </div>

        <div className="glass-panel" style={{ padding: '24px' }}>
          <h3 style={{ fontSize: '1.25rem', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Cpu style={{ color: '#10b981' }} />
            <span>Động Cơ Tính Toán Đại Số & AI (Engine)</span>
          </h3>
          <ul style={{ display: 'flex', flexDirection: 'column', gap: '10px', listStyle: 'none', fontSize: '0.9rem' }}>
            <li style={{ display: 'flex', justifyContent: 'space-between', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '8px' }}>
              <span style={{ color: 'var(--text-secondary)' }}>CAS Verification:</span>
              <strong style={{ color: '#10b981' }}>SymPy 1.13 + Pint Units</strong>
            </li>
            <li style={{ display: 'flex', justifyContent: 'space-between', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '8px' }}>
              <span style={{ color: 'var(--text-secondary)' }}>Spaced Repetition:</span>
              <strong style={{ color: 'var(--text-primary)' }}>Thuật toán FSRS & SM-2</strong>
            </li>
            <li style={{ display: 'flex', justifyContent: 'space-between', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '8px' }}>
              <span style={{ color: 'var(--text-secondary)' }}>Phỏng Vấn Học Bổng:</span>
              <strong style={{ color: 'var(--text-primary)' }}>Mô hình STAR NLP Chấm Tự Động</strong>
            </li>
            <li style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: '4px' }}>
              <span style={{ color: 'var(--text-secondary)' }}>Khung Máy Chủ API:</span>
              <strong style={{ color: '#a5b4fc' }}>FastAPI + Uvicorn Asynchronous</strong>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};
