import type { FC } from 'react';
import { ChevronLeft, ChevronRight } from 'lucide-react';

interface PaginationProps {
  currentPage: number;
  totalPages: number;
  onPageChange: (page: number) => void;
  totalItems?: number;
  pageSize?: number;
}

export const Pagination: FC<PaginationProps> = ({
  currentPage,
  totalPages,
  onPageChange,
  totalItems,
  pageSize = 24,
}) => {
  if (totalPages <= 1) return null;

  const startItem = (currentPage - 1) * pageSize + 1;
  const endItem = totalItems ? Math.min(currentPage * pageSize, totalItems) : currentPage * pageSize;

  const getVisiblePages = () => {
    const delta = 2;
    const range: number[] = [];
    const rangeWithDots: (number | string)[] = [];

    for (
      let i = Math.max(2, currentPage - delta);
      i <= Math.min(totalPages - 1, currentPage + delta);
      i++
    ) {
      range.push(i);
    }

    if (currentPage - delta > 2) {
      rangeWithDots.push(1, '...');
    } else {
      rangeWithDots.push(1);
    }

    range.forEach((i) => rangeWithDots.push(i));

    if (currentPage + delta < totalPages - 1) {
      rangeWithDots.push('...', totalPages);
    } else if (totalPages > 1) {
      rangeWithDots.push(totalPages);
    }

    return rangeWithDots;
  };

  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: '12px',
        padding: '16px 0',
        marginTop: '20px',
        borderTop: '1px solid var(--border-subtle)',
      }}
    >
      {totalItems !== undefined && (
        <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
          Hiển thị <strong>{startItem.toLocaleString()} - {endItem.toLocaleString()}</strong> trong <strong>{totalItems.toLocaleString()}</strong> mục
        </div>
      )}

      <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginLeft: 'auto' }}>
        <button
          className="btn btn-secondary"
          style={{ padding: '6px 12px', fontSize: '0.85rem' }}
          disabled={currentPage <= 1}
          onClick={() => onPageChange(currentPage - 1)}
          title="Trang trước"
        >
          <ChevronLeft size={16} />
          <span>Trước</span>
        </button>

        {getVisiblePages().map((p, idx) =>
          typeof p === 'number' ? (
            <button
              key={idx}
              className={`btn ${currentPage === p ? 'btn-primary' : 'btn-secondary'}`}
              style={{
                minWidth: '36px',
                height: '36px',
                padding: '0 8px',
                fontSize: '0.85rem',
                justifyContent: 'center',
              }}
              onClick={() => onPageChange(p)}
            >
              {p}
            </button>
          ) : (
            <span
              key={idx}
              style={{
                padding: '0 4px',
                color: 'var(--text-muted)',
                fontSize: '0.9rem',
                userSelect: 'none',
              }}
            >
              {p}
            </span>
          )
        )}

        <button
          className="btn btn-secondary"
          style={{ padding: '6px 12px', fontSize: '0.85rem' }}
          disabled={currentPage >= totalPages}
          onClick={() => onPageChange(currentPage + 1)}
          title="Trang sau"
        >
          <span>Sau</span>
          <ChevronRight size={16} />
        </button>
      </div>
    </div>
  );
};
