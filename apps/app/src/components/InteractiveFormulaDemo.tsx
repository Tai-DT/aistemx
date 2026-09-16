import { useState, useMemo, useEffect, type FC } from 'react';
import { MathView } from './MathView';
import {
  RotateCcw,
  Sparkles,
  Layers,
  Sliders,
  CheckCircle2,
  Maximize2,
  Minimize2,
} from 'lucide-react';

interface InteractiveInput {
  symbol: string;
  raw_symbol?: string;
  label?: string;
  unit?: string;
  default?: number;
  min?: number;
  max?: number;
  step?: number;
}

interface FormulaInteractiveData {
  formula_id?: string;
  name_vi?: string;
  subject?: string;
  interactive_type?: string;
  is_computable?: boolean;
  output?: {
    symbol?: string;
    raw_symbol?: string;
    name?: string;
    unit?: string;
  };
  expression_js?: string;
  expression_py?: string;
  inputs?: InteractiveInput[];
}

interface Illustration2D {
  url?: string;
  caption_vi?: string;
  title?: string;
  note?: string;
  generator?: string;
  svg?: string;
}

interface InteractiveFormulaDemoProps {
  formula: {
    id: string;
    name_vi?: string;
    name?: string;
    subject?: string;
    level?: string;
    topic?: string;
    latex?: string;
    vars?: Record<string, string>;
    units?: Record<string, string>;
    variables?: any;
    python_expr?: string;
    interactive?: FormulaInteractiveData;
    illustration_2d?: Illustration2D;
    has_illustration_2d?: boolean;
    note?: string;
  };
}

export const InteractiveFormulaDemo: FC<InteractiveFormulaDemoProps> = ({ formula }) => {
  const fId = formula.id.toLowerCase();
  const topic = `${formula.topic || ''} ${(formula as any).subtopic || ''} ${formula.name_vi || ''} ${Array.isArray((formula as any).tags) ? (formula as any).tags.join(' ') : ''}`.toLowerCase();
  const subj = formula.subject || 'math';

  // Xác định chính xác công thức thuộc lứa tuổi Tiểu học (Lớp 1 đến Lớp 5, đặc biệt Lớp 5)
  const isElementary = useMemo(() => {
    const fLevel = (formula.level || '').toLowerCase();
    const fGrades = (formula as any).grades as number[] | undefined;
    const fTags = (formula as any).tags as string[] | undefined;
    return (
      fLevel === 'tieu-hoc' ||
      fLevel === 'tieu_hoc' ||
      fLevel.includes('tieu') ||
      fId.includes('tieu-hoc') ||
      fId.startsWith('math.tieu-hoc') ||
      (Array.isArray(fGrades) && fGrades.length > 0 && fGrades.some((g) => g <= 5)) ||
      (Array.isArray(fTags) && fTags.some((t) => ['lop1', 'lop2', 'lop3', 'lop4', 'lop5', 'tieu-hoc'].includes(t.toLowerCase())))
    );
  }, [formula.level, fId, formula]);

  // Bộ thanh trượt thông minh chuẩn mực SGK & nhận thức học sinh Tiểu học / Lớp 5
  const elementaryInputs: InteractiveInput[] = useMemo(() => {
    if (!isElementary) return [];

    // 1. Chuyển động đều quãng đường s = v * t
    if (fId.includes('quang-duong') || (fId.includes('chuyen-dong') && !fId.includes('nguoc-chieu') && !fId.includes('cung-chieu') && !fId.includes('dong-nuoc') && !fId.includes('van-toc') && !fId.includes('thoi-gian'))) {
      return [
        { symbol: 'v', label: 'Vận tốc xe ô tô (v)', unit: 'km/h', default: 40, min: 10, max: 90, step: 5 },
        { symbol: 't', label: 'Thời gian xe đi (t)', unit: 'giờ', default: 2.5, min: 0.5, max: 6, step: 0.5 },
      ];
    }
    if (fId.includes('chuyen-dong-deu.van-toc')) {
      return [
        { symbol: 's', label: 'Quãng đường đi được (s)', unit: 'km', default: 120, min: 20, max: 300, step: 10 },
        { symbol: 't', label: 'Thời gian xe đi (t)', unit: 'giờ', default: 3, min: 0.5, max: 6, step: 0.5 },
      ];
    }
    if (fId.includes('chuyen-dong-deu.thoi-gian')) {
      return [
        { symbol: 's', label: 'Quãng đường đi được (s)', unit: 'km', default: 120, min: 20, max: 300, step: 10 },
        { symbol: 'v', label: 'Vận tốc xe đi (v)', unit: 'km/h', default: 40, min: 10, max: 90, step: 5 },
      ];
    }

    // 2. Thời điểm hai vật gặp nhau: t_gap = t0 + s / (v1 + v2)
    if (fId.includes('thoi-diem-gap-nhau')) {
      return [
        { symbol: 't0', label: 'Thời điểm xuất phát (t₀)', unit: 'giờ', default: 7, min: 5, max: 12, step: 1 },
        { symbol: 's', label: 'Khoảng cách hai xe lúc đầu (s)', unit: 'km', default: 180, min: 30, max: 400, step: 10 },
        { symbol: 'v1', label: 'Vận tốc Xe Đỏ từ A (v₁)', unit: 'km/h', default: 50, min: 15, max: 80, step: 5 },
        { symbol: 'v2', label: 'Vận tốc Xe Xanh từ B (v₂)', unit: 'km/h', default: 40, min: 10, max: 70, step: 5 },
      ];
    }

    // 3. Hai vật chuyển động ngược chiều gặp nhau (Đúng bài học SGK: 180 km, 50 km/h, 40 km/h)
    if (fId.includes('nguoc-chieu') || topic.includes('ngược chiều')) {
      return [
        { symbol: 's', label: 'Khoảng cách hai xe lúc đầu (s)', unit: 'km', default: 180, min: 30, max: 400, step: 10 },
        { symbol: 'v1', label: 'Vận tốc Xe Đỏ từ A (v₁)', unit: 'km/h', default: 50, min: 15, max: 80, step: 5 },
        { symbol: 'v2', label: 'Vận tốc Xe Xanh từ B (v₂)', unit: 'km/h', default: 40, min: 10, max: 70, step: 5 },
      ];
    }

    // 4. Hai vật chuyển động cùng chiều đuổi kịp (Đúng bài học SGK: 40 km, 50 km/h, 10 km/h)
    if (fId.includes('cung-chieu') || topic.includes('cùng chiều') || fId.includes('duoi-kip')) {
      return [
        { symbol: 's', label: 'Khoảng cách xe trước lúc đầu (s)', unit: 'km', default: 40, min: 10, max: 150, step: 5 },
        { symbol: 'v1', label: 'Vận tốc xe sau - nhanh hơn (v₁)', unit: 'km/h', default: 50, min: 25, max: 90, step: 5 },
        { symbol: 'v2', label: 'Vận tốc xe trước - chậm hơn (v₂)', unit: 'km/h', default: 10, min: 5, max: 40, step: 5 },
      ];
    }

    // 5. Chuyển động trên dòng nước
    if (fId.includes('dong-nuoc') || fId.includes('xuoi-dong') || fId.includes('nguoc-dong') || topic.includes('dòng nước')) {
      return [
        { symbol: 'v', label: 'Vận tốc thuyền khi nước đứng yên (v)', unit: 'km/h', default: 15, min: 8, max: 30, step: 1 },
        { symbol: 'vn', label: 'Vận tốc dòng nước chảy (v_nước)', unit: 'km/h', default: 3, min: 1, max: 6, step: 0.5 },
      ];
    }

    // 6. Hình tam giác (Đúng hình học phẳng lớp 5: đáy 8 cm, cao 5 cm)
    if (fId.includes('tam-giac')) {
      if (fId.includes('chu-vi')) {
        return [
          { symbol: 'a', label: 'Cạnh thứ nhất (a)', unit: 'cm', default: 5, min: 2, max: 20, step: 1 },
          { symbol: 'b', label: 'Cạnh thứ hai (b)', unit: 'cm', default: 6, min: 2, max: 20, step: 1 },
          { symbol: 'c', label: 'Cạnh thứ ba (c)', unit: 'cm', default: 7, min: 2, max: 20, step: 1 },
        ];
      }
      return [
        { symbol: 'a', label: 'Độ dài cạnh đáy (a)', unit: 'cm', default: 8, min: 3, max: 20, step: 1 },
        { symbol: 'h', label: 'Chiều cao tương ứng (h)', unit: 'cm', default: 5, min: 2, max: 15, step: 1 },
      ];
    }

    // 7. Hình thang (Đáy lớn 8 cm > Đáy bé 4 cm, chiều cao 5 cm)
    if (fId.includes('hinh-thang') || topic.includes('hình thang')) {
      return [
        { symbol: 'a', label: 'Độ dài đáy lớn (a)', unit: 'cm', default: 8, min: 5, max: 20, step: 1 },
        { symbol: 'b', label: 'Độ dài đáy bé (b)', unit: 'cm', default: 4, min: 2, max: 12, step: 1 },
        { symbol: 'h', label: 'Chiều cao (h)', unit: 'cm', default: 5, min: 2, max: 12, step: 1 },
      ];
    }

    // 8. Hình hộp chữ nhật / lập phương (Kích thước chuẩn xếp khối Lego 1cm³)
    if (fId.includes('hinh-hop') || (topic.includes('thể tích') && isElementary)) {
      return [
        { symbol: 'a', label: 'Chiều dài (a)', unit: 'cm', default: 5, min: 2, max: 10, step: 1 },
        { symbol: 'b', label: 'Chiều rộng (b)', unit: 'cm', default: 3, min: 1, max: 8, step: 1 },
        { symbol: 'c', label: 'Chiều cao (c)', unit: 'cm', default: 4, min: 1, max: 8, step: 1 },
      ];
    }
    if (fId.includes('lap-phuong')) {
      return [
        { symbol: 'a', label: 'Cạnh hình lập phương (a)', unit: 'cm', default: 4, min: 1, max: 8, step: 1 },
      ];
    }

    // 9. Hình tròn (Bán kính 5 cm)
    if (fId.includes('hinh-tron') || topic.includes('hình tròn')) {
      return [
        { symbol: 'r', label: 'Bán kính hình tròn (r)', unit: 'cm', default: 5, min: 1, max: 15, step: 0.5 },
      ];
    }

    // 10. Hình chữ nhật / hình vuông
    if (fId.includes('chu-nhat')) {
      return [
        { symbol: 'a', label: 'Chiều dài (a)', unit: 'm', default: 8, min: 3, max: 25, step: 1 },
        { symbol: 'b', label: 'Chiều rộng (b)', unit: 'm', default: 5, min: 1, max: 18, step: 1 },
      ];
    }
    if (fId.includes('hinh-vuong')) {
      return [
        { symbol: 'a', label: 'Cạnh hình vuông (a)', unit: 'm', default: 6, min: 1, max: 20, step: 1 },
      ];
    }

    // 11. Tìm hai số khi biết Tổng và Hiệu (Đúng bài học SGK: Tổng 50, Hiệu 10)
    if (fId.includes('tong-hieu') || topic.includes('tổng và hiệu')) {
      return [
        { symbol: 'tong', label: 'Tổng hai số', unit: '', default: 50, min: 10, max: 200, step: 2 },
        { symbol: 'hieu', label: 'Hiệu hai số', unit: '', default: 10, min: 2, max: 60, step: 2 },
      ];
    }

    // 12. Tìm hai số khi biết Tổng và Tỉ số (Đúng bài học SGK: Tổng 45, tỉ số 2/3)
    if (fId.includes('tong-va-ti-so') || (topic.includes('tổng') && topic.includes('tỉ'))) {
      return [
        { symbol: 'tong', label: 'Tổng hai số', unit: '', default: 45, min: 10, max: 150, step: 5 },
        { symbol: 'p_be', label: 'Số phần của số bé', unit: 'phần', default: 2, min: 1, max: 6, step: 1 },
        { symbol: 'p_lon', label: 'Số phần của số lớn', unit: 'phần', default: 3, min: 2, max: 8, step: 1 },
      ];
    }

    // 13. Tìm hai số khi biết Hiệu và Tỉ số (Đúng bài học SGK: Hiệu 12, tỉ số 1/3)
    if (fId.includes('hieu-va-ti-so') || (topic.includes('hiệu') && topic.includes('tỉ'))) {
      return [
        { symbol: 'hieu', label: 'Hiệu hai số', unit: '', default: 12, min: 2, max: 80, step: 2 },
        { symbol: 'p_be', label: 'Số phần của số bé', unit: 'phần', default: 1, min: 1, max: 5, step: 1 },
        { symbol: 'p_lon', label: 'Số phần của số lớn', unit: 'phần', default: 3, min: 2, max: 8, step: 1 },
      ];
    }

    // 14. Tỉ số và phân số (Mô hình băng giấy phân số)
    if (fId.includes('ti-so') || fId.includes('phan-so') || topic.includes('phân số') || topic.includes('tỉ số')) {
      return [
        { symbol: 'a', label: 'Tử số (số phần tô màu)', unit: 'phần', default: 3, min: 1, max: 8, step: 1 },
        { symbol: 'b', label: 'Mẫu số (tổng số phần)', unit: 'phần', default: 5, min: 2, max: 10, step: 1 },
      ];
    }

    // Mặc định cho số học tiểu học
    return [
      { symbol: 'a', label: 'Số thứ nhất (a)', unit: '', default: 8, min: 1, max: 20, step: 1 },
      { symbol: 'b', label: 'Số thứ hai (b)', unit: '', default: 3, min: 1, max: 20, step: 1 },
    ];
  }, [isElementary, fId, topic]);

  // Xác định công thức Toán THCS (Lớp 6 đến Lớp 9) hoặc các chủ đề hình học / đại số cơ bản
  const isSecondaryMath = useMemo(() => {
    if (subj !== 'math' || isElementary) return false;
    const fLevel = (formula.level || '').toLowerCase();
    const fGrades = (formula as any).grades as number[] | undefined;
    const isHs = fLevel === 'thpt' || fLevel === 'dai-hoc' || fId.includes('.thpt.') || fId.includes('.dai-hoc.');
    if (isHs) return false;
    const isTrig = fId.includes('luong-giac') || topic.includes('lượng giác') || fId.includes('trigonometry');
    if (isTrig) return false;
    return (
      fLevel === 'thcs' ||
      fId.includes('.thcs.') ||
      (Array.isArray(fGrades) && fGrades.some((g) => g >= 6 && g <= 9)) ||
      fId.includes('ta-let') ||
      fId.includes('thales') ||
      fId.includes('pytago') ||
      (fId.includes('he-thuc-luong') && !fId.includes('luong-giac')) ||
      fId.includes('hinh-thang') ||
      fId.includes('duong-tron') ||
      fId.includes('hang-dang-thuc') ||
      fId.includes('truc-so') ||
      fId.includes('parabol') ||
      topic.includes('ta-lét') ||
      topic.includes('thales') ||
      topic.includes('pytago') ||
      topic.includes('hệ thức lượng') ||
      topic.includes('đường tròn') ||
      topic.includes('hằng đẳng thức') ||
      topic.includes('parabol')
    );
  }, [subj, formula.level, fId, formula, topic, isElementary]);

  // Bộ thanh trượt thông minh chuẩn mực SGK & nhận thức học sinh THCS (Lớp 6-9)
  const secondaryMathInputs: InteractiveInput[] = useMemo(() => {
    if (!isSecondaryMath) return [];

    // 1. Định lý Ta-lét trong tam giác
    if (fId.includes('ta-let') || fId.includes('thales') || topic.includes('ta-lét') || topic.includes('thales')) {
      return [
        { symbol: 'k', label: 'Tỉ lệ chia AM/AB (k)', unit: '', default: 0.6, min: 0.2, max: 0.8, step: 0.05 },
        { symbol: 'ab', label: 'Cạnh AB', unit: 'cm', default: 10, min: 4, max: 20, step: 1 },
        { symbol: 'ac', label: 'Cạnh AC', unit: 'cm', default: 12, min: 4, max: 24, step: 1 },
      ];
    }

    // 2. Định lý Pytago
    if (fId.includes('pytago') || topic.includes('pytago')) {
      return [
        { symbol: 'a', label: 'Cạnh góc vuông a', unit: 'cm', default: 3, min: 1, max: 12, step: 1 },
        { symbol: 'b', label: 'Cạnh góc vuông b', unit: 'cm', default: 4, min: 1, max: 12, step: 1 },
      ];
    }

    // 3. Hệ thức lượng tam giác vuông
    if (fId.includes('he-thuc-luong') || fId.includes('duong-cao') || fId.includes('hinh-chieu') || topic.includes('hệ thức lượng') || topic.includes('hình chiếu')) {
      return [
        { symbol: 'bh', label: "Hình chiếu BH (c')", unit: 'cm', default: 4, min: 1, max: 16, step: 1 },
        { symbol: 'ch', label: "Hình chiếu CH (b')", unit: 'cm', default: 9, min: 1, max: 16, step: 1 },
      ];
    }

    // 4. Đường trung bình & Hình thang
    if (fId.includes('hinh-thang') || topic.includes('hình thang') || fId.includes('trapezoid')) {
      return [
        { symbol: 'b', label: 'Đáy bé (b)', unit: 'cm', default: 4, min: 2, max: 12, step: 1 },
        { symbol: 'a', label: 'Đáy lớn (a)', unit: 'cm', default: 8, min: 4, max: 20, step: 1 },
        { symbol: 'h', label: 'Chiều cao (h)', unit: 'cm', default: 5, min: 2, max: 12, step: 1 },
      ];
    }

    // 5. Đường tròn & Tiếp tuyến
    if (fId.includes('duong-tron') || topic.includes('đường tròn') || topic.includes('tiếp tuyến') || topic.includes('dây cung') || topic.includes('góc nội tiếp')) {
      return [
        { symbol: 'R', label: 'Bán kính R', unit: 'cm', default: 5, min: 2, max: 10, step: 0.5 },
        { symbol: 'd', label: 'Khoảng cách d (OA)', unit: 'cm', default: 7, min: 1, max: 12, step: 0.5 },
      ];
    }

    // 6. Bảy hằng đẳng thức đáng nhớ
    if (fId.includes('hang-dang-thuc') || topic.includes('hằng đẳng thức') || topic.includes('bình phương')) {
      return [
        { symbol: 'a', label: 'Số thứ nhất (a)', unit: '', default: 3, min: 1, max: 8, step: 1 },
        { symbol: 'b', label: 'Số thứ hai (b)', unit: '', default: 2, min: 1, max: 8, step: 1 },
      ];
    }

    // 7. Trục số thực nghiệm
    if (fId.includes('truc-so') || fId.includes('so-nguyen') || fId.includes('gia-tri-tuyet-doi') || topic.includes('trục số') || topic.includes('số nguyên') || topic.includes('giá trị tuyệt đối')) {
      return [
        { symbol: 'x', label: 'Tọa độ điểm x', unit: '', default: -3, min: -10, max: 10, step: 1 },
        { symbol: 'y', label: 'Tọa độ điểm y', unit: '', default: 4, min: -10, max: 10, step: 1 },
      ];
    }

    // 8. Parabol hàm số bậc hai
    if (fId.includes('parabol') || fId.includes('bac-hai') || topic.includes('parabol') || topic.includes('ax^2') || topic.includes('bậc hai')) {
      return [
        { symbol: 'a', label: 'Hệ số a (a ≠ 0)', unit: '', default: 1, min: -3, max: 3, step: 0.5 },
        { symbol: 'b', label: 'Hệ số b', unit: '', default: -2, min: -6, max: 6, step: 1 },
        { symbol: 'c', label: 'Hệ số c', unit: '', default: -3, min: -8, max: 8, step: 1 },
      ];
    }

    return [];
  }, [isSecondaryMath, fId, topic]);

  // Xác định công thức Toán THPT & Đại Học (Lớp 10 đến Lớp 12 & ĐH)
  const isHighSchoolMath = useMemo(() => {
    if (subj !== 'math' || isElementary || isSecondaryMath) return false;
    const fLevel = (formula.level || '').toLowerCase();
    const fGrades = (formula as any).grades as number[] | undefined;
    const isHsLevel = fLevel === 'thpt' || fLevel === 'dai-hoc' || fId.includes('.thpt.') || fId.includes('.dai-hoc.');
    const hasHsGrades = Array.isArray(fGrades) && fGrades.some((g) => g >= 10 && g <= 12);
    return (
      isHsLevel ||
      hasHsGrades ||
      fId.includes('luong-giac') ||
      fId.includes('trigonometry') ||
      fId.includes('sin') ||
      fId.includes('cos') ||
      fId.includes('tan') ||
      fId.includes('dao-ham') ||
      fId.includes('derivative') ||
      fId.includes('tich-phan') ||
      fId.includes('nguyen-ham') ||
      fId.includes('integral') ||
      fId.includes('riemann') ||
      fId.includes('so-phuc') ||
      fId.includes('complex') ||
      fId.includes('vector') ||
      fId.includes('tich-vo-huong') ||
      fId.includes('dot-product') ||
      fId.includes('cap-so') ||
      fId.includes('logarit') ||
      fId.includes('mu-logarit') ||
      topic.includes('lượng giác') ||
      topic.includes('đạo hàm') ||
      topic.includes('tích phân') ||
      topic.includes('nguyên hàm') ||
      topic.includes('số phức') ||
      topic.includes('vector') ||
      topic.includes('tích vô hướng') ||
      topic.includes('cấp số') ||
      topic.includes('logarit')
    );
  }, [subj, formula.level, fId, formula, topic, isElementary, isSecondaryMath]);

  // Bộ thanh trượt thông minh chuẩn mực SGK & nhận thức học sinh THPT (Lớp 10-12 & ĐH)
  const highSchoolMathInputs: InteractiveInput[] = useMemo(() => {
    if (!isHighSchoolMath) return [];

    // 1. Lượng giác & Vòng tròn đơn vị
    if (
      fId.includes('luong-giac') ||
      fId.includes('trigonometry') ||
      fId.includes('sin') ||
      fId.includes('cos') ||
      fId.includes('tan') ||
      topic.includes('lượng giác') ||
      topic.includes('sin') ||
      topic.includes('cos')
    ) {
      return [
        { symbol: 'alpha', label: 'Góc quay α', unit: '°', default: 45, min: 0, max: 360, step: 5 },
      ];
    }

    // 2. Ý nghĩa hình học của Đạo hàm & Tiếp tuyến đồ thị
    if (
      fId.includes('dao-ham') ||
      fId.includes('derivative') ||
      fId.includes('tiep-tuyen') ||
      topic.includes('đạo hàm') ||
      topic.includes('tiếp tuyến')
    ) {
      return [
        { symbol: 'x0', label: 'Hoành độ tiếp điểm (x₀)', unit: '', default: 1.0, min: -2.0, max: 2.0, step: 0.1 },
      ];
    }

    // 3. Tích phân & Tổng Riemann
    if (
      fId.includes('tich-phan') ||
      fId.includes('nguyen-ham') ||
      fId.includes('integral') ||
      fId.includes('riemann') ||
      topic.includes('tích phân') ||
      topic.includes('nguyên hàm')
    ) {
      return [
        { symbol: 'n', label: 'Số dải phân hoạch (n)', unit: 'dải', default: 8, min: 4, max: 24, step: 2 },
        { symbol: 'b', label: 'Cận tích phân trên (b)', unit: '', default: 3.0, min: 1.5, max: 4.5, step: 0.5 },
      ];
    }

    // 4. Số phức & Mặt phẳng phức Gauss (Argand)
    if (
      fId.includes('so-phuc') ||
      fId.includes('complex') ||
      topic.includes('số phức')
    ) {
      return [
        { symbol: 'a', label: 'Phần thực (a)', unit: '', default: 3, min: -6, max: 6, step: 1 },
        { symbol: 'b', label: 'Phần ảo (b)', unit: '', default: 4, min: -6, max: 6, step: 1 },
      ];
    }

    // 5. Vector & Tích vô hướng
    if (
      fId.includes('vector') ||
      fId.includes('tich-vo-huong') ||
      fId.includes('dot-product') ||
      topic.includes('vector') ||
      topic.includes('tích vô hướng')
    ) {
      return [
        { symbol: 'len_u', label: 'Độ dài vector |u|', unit: '', default: 4, min: 1, max: 8, step: 0.5 },
        { symbol: 'len_v', label: 'Độ dài vector |v|', unit: '', default: 5, min: 1, max: 8, step: 0.5 },
        { symbol: 'theta', label: 'Góc giữa hai vector (θ)', unit: '°', default: 60, min: 0, max: 180, step: 5 },
      ];
    }

    // 6. Cấp số cộng & Cấp số nhân
    if (
      fId.includes('cap-so') ||
      topic.includes('cấp số') ||
      topic.includes('dãy số')
    ) {
      return [
        { symbol: 'u1', label: 'Số hạng đầu (u₁)', unit: '', default: 2, min: 1, max: 10, step: 1 },
        { symbol: 'd', label: 'Công sai d (hoặc công bội q)', unit: '', default: 3, min: 1, max: 5, step: 1 },
      ];
    }

    // 7. Hàm số Mũ & Logarit
    if (
      fId.includes('logarit') ||
      fId.includes('mu') ||
      topic.includes('logarit') ||
      topic.includes('mũ')
    ) {
      return [
        { symbol: 'a', label: 'Cơ số (a > 0, a ≠ 1)', unit: '', default: 2.0, min: 0.5, max: 3.5, step: 0.5 },
        { symbol: 'x', label: 'Biến số (x)', unit: '', default: 2.0, min: -2.0, max: 4.0, step: 0.5 },
      ];
    }

    return [];
  }, [isHighSchoolMath, fId, topic]);

  // Kiểm tra công thức có thể tính toán số học thực sự hay không
  const isComputable = useMemo(() => {
    if (isElementary) return true; // Học sinh tiểu học luôn được tương tác trực quan
    if (isSecondaryMath && secondaryMathInputs.length > 0) return true; // Toán THCS với các mô hình chuyên biệt
    if (isHighSchoolMath && highSchoolMathInputs.length > 0) return true; // Toán THPT & ĐH với các mô hình chuyên biệt
    if (formula.interactive?.is_computable === false) return false;
    const expr = formula.interactive?.expression_js;
    if (expr && expr.trim() && formula.interactive?.inputs && formula.interactive.inputs.length > 0) {
      return true;
    }
    return false;
  }, [formula, isElementary, isSecondaryMath, secondaryMathInputs, isHighSchoolMath, highSchoolMathInputs]);

  const illustrationUrl = formula.illustration_2d?.url || (formula.has_illustration_2d ? `/api/illustrations2d/${formula.id}` : '');
  const hasIllustration = Boolean(illustrationUrl);

  // Mặc định luôn ưu tiên simulation cho tiểu học để học sinh dễ hiểu bằng mắt
  const [viewMode, setViewMode] = useState<'simulation' | 'diagram'>(
    isElementary ? 'simulation' : (hasIllustration ? 'diagram' : (isComputable ? 'simulation' : 'diagram'))
  );
  const [isExpanded, setIsExpanded] = useState(false);

  useEffect(() => {
    setViewMode(isElementary ? 'simulation' : (hasIllustration ? 'diagram' : (isComputable ? 'simulation' : 'diagram')));
  }, [formula.id, hasIllustration, isComputable, isElementary]);

  // Cấu hình tham số đầu vào: Ưu tiên bộ tham số chuẩn Tiểu học, THCS & THPT
  const inputConfigs: InteractiveInput[] = useMemo(() => {
    if (isElementary && elementaryInputs.length > 0) {
      return elementaryInputs;
    }
    if (isSecondaryMath && secondaryMathInputs.length > 0) {
      return secondaryMathInputs;
    }
    if (isHighSchoolMath && highSchoolMathInputs.length > 0) {
      return highSchoolMathInputs;
    }
    if (formula.interactive?.inputs && formula.interactive.inputs.length > 0) {
      return formula.interactive.inputs;
    }
    return [];
  }, [formula.interactive?.inputs, isElementary, elementaryInputs, isSecondaryMath, secondaryMathInputs, isHighSchoolMath, highSchoolMathInputs]);

  // Trạng thái giá trị thanh trượt
  const [sliderValues, setSliderValues] = useState<Record<string, number>>({});

  useEffect(() => {
    const initial: Record<string, number> = {};
    for (const inp of inputConfigs) {
      initial[inp.symbol] = inp.default ?? 5.0;
    }
    setSliderValues(initial);
  }, [inputConfigs]);

  const handleSliderChange = (symbol: string, val: number) => {
    setSliderValues((prev) => ({ ...prev, [symbol]: val }));
  };

  const handleReset = () => {
    const initial: Record<string, number> = {};
    for (const inp of inputConfigs) {
      initial[inp.symbol] = inp.default ?? 5.0;
    }
    setSliderValues(initial);
  };

  // Helper lấy giá trị thanh trượt theo tên biến ngữ nghĩa chuẩn xác
  const getVal = (symbols: string[], fallback: number): number => {
    for (const sym of symbols) {
      if (sliderValues[sym] !== undefined) return sliderValues[sym];
    }
    for (const [k, v] of Object.entries(sliderValues)) {
      if (symbols.some((s) => s.toLowerCase() === k.toLowerCase())) return v;
    }
    for (const sym of symbols) {
      const cfg = inputConfigs.find((c) => c.symbol.toLowerCase() === sym.toLowerCase());
      if (cfg && cfg.default !== undefined) return cfg.default;
    }
    return fallback;
  };

  // Tính toán kết quả đầu ra chuẩn xác
  const calculatedOutput = useMemo(() => {
    if (!isComputable) return null;

    if (isElementary) {
      if (fId.includes('thoi-diem-gap-nhau')) {
        const t0 = getVal(['t0', 't_0'], 7);
        const s = getVal(['s', 'dist'], 180);
        const v1 = getVal(['v1', 'v_1'], 50);
        const v2 = getVal(['v2', 'v_2'], 40);
        return (v1 + v2) > 0 ? t0 + (s / (v1 + v2)) : t0;
      }
      if (fId.includes('nguoc-chieu') || topic.includes('ngược chiều')) {
        const s = getVal(['s', 'dist'], 180);
        const v1 = getVal(['v1', 'v_1'], 50);
        const v2 = getVal(['v2', 'v_2'], 40);
        return (v1 + v2) > 0 ? s / (v1 + v2) : 0;
      }
      if (fId.includes('cung-chieu') || topic.includes('cùng chiều') || fId.includes('duoi-kip')) {
        const s = getVal(['s', 'dist'], 40);
        const v1 = getVal(['v1', 'v_1'], 50);
        const v2 = getVal(['v2', 'v_2'], 10);
        const diff = v1 - v2;
        return diff > 0 ? s / diff : 0;
      }
      if (fId.includes('quang-duong') || (fId.includes('chuyen-dong') && !fId.includes('dong-nuoc') && !fId.includes('van-toc') && !fId.includes('thoi-gian'))) {
        const v = getVal(['v'], 40);
        const t = getVal(['t'], 2.5);
        return v * t;
      }
      if (fId.includes('chuyen-dong-deu.van-toc')) {
        const s = getVal(['s'], 120);
        const t = getVal(['t'], 3);
        return t > 0 ? s / t : 0;
      }
      if (fId.includes('chuyen-dong-deu.thoi-gian')) {
        const s = getVal(['s'], 120);
        const v = getVal(['v'], 40);
        return v > 0 ? s / v : 0;
      }
      if (fId.includes('xuoi-dong')) {
        return getVal(['v'], 15) + getVal(['vn'], 3);
      }
      if (fId.includes('nguoc-dong')) {
        return getVal(['v'], 15) - getVal(['vn'], 3);
      }
      if (fId.includes('tam-giac')) {
        if (fId.includes('chu-vi')) return getVal(['a'], 5) + getVal(['b'], 6) + getVal(['c'], 7);
        return (getVal(['a'], 8) * getVal(['h'], 5)) / 2;
      }
      if (fId.includes('hinh-thang')) {
        return ((getVal(['a'], 8) + getVal(['b'], 4)) * getVal(['h'], 5)) / 2;
      }
      if (fId.includes('hinh-hop') || (topic.includes('thể tích') && isElementary)) {
        return getVal(['a'], 5) * getVal(['b'], 3) * getVal(['c'], 4);
      }
      if (fId.includes('lap-phuong')) {
        const a = getVal(['a'], 4);
        return a * a * a;
      }
      if (fId.includes('hinh-tron')) {
        const r = getVal(['r'], 5);
        if (fId.includes('dien-tich')) return r * r * 3.14;
        return 2 * r * 3.14;
      }
      if (fId.includes('chu-nhat')) {
        const a = getVal(['a'], 8);
        const b = getVal(['b'], 5);
        if (fId.includes('dien-tich')) return a * b;
        return (a + b) * 2;
      }
      if (fId.includes('hinh-vuong')) {
        const a = getVal(['a'], 6);
        if (fId.includes('dien-tich')) return a * a;
        return a * 4;
      }
      if (fId.includes('tong-hieu') || topic.includes('tổng và hiệu')) {
        const tong = getVal(['tong'], 50);
        const hieu = getVal(['hieu'], 10);
        return (tong + hieu) / 2;
      }
      if (fId.includes('tong-va-ti-so') || (topic.includes('tổng') && topic.includes('tỉ'))) {
        const tong = getVal(['tong'], 45);
        const pBe = getVal(['p_be'], 2);
        const pLon = getVal(['p_lon'], 3);
        const tongPhan = pBe + pLon;
        const motPhan = tongPhan > 0 ? tong / tongPhan : 0;
        return Number((motPhan * pLon).toFixed(1));
      }
      if (fId.includes('hieu-va-ti-so') || (topic.includes('hiệu') && topic.includes('tỉ'))) {
        const hieu = getVal(['hieu'], 12);
        const pBe = getVal(['p_be'], 1);
        const pLon = getVal(['p_lon'], 3);
        const hieuPhan = Math.max(1, pLon - pBe);
        const motPhan = hieu / hieuPhan;
        return Number((motPhan * pLon).toFixed(1));
      }
      if (fId.includes('ti-so') || fId.includes('phan-so') || topic.includes('phân số') || topic.includes('tỉ số')) {
        const a = getVal(['a'], 3);
        const b = getVal(['b'], 5);
        return b > 0 ? Number((a / b).toFixed(2)) : 0;
      }
    }

    if (isSecondaryMath) {
      if (fId.includes('ta-let') || fId.includes('thales') || topic.includes('ta-lét') || topic.includes('thales')) {
        const k = Math.min(0.85, Math.max(0.15, getVal(['k', 'tile'], 0.6)));
        return Number(k.toFixed(2));
      }
      if (fId.includes('pytago') || topic.includes('pytago')) {
        const a = getVal(['a', 'b'], 3);
        const b = getVal(['b', 'c'], 4);
        return Number(Math.sqrt(a * a + b * b).toFixed(2));
      }
      if (fId.includes('he-thuc-luong') || fId.includes('duong-cao') || fId.includes('hinh-chieu') || topic.includes('hệ thức lượng') || topic.includes('hình chiếu')) {
        const bh = getVal(['bh', 'b1'], 4);
        const ch = getVal(['ch', 'c1'], 9);
        return Number(Math.sqrt(bh * ch).toFixed(2));
      }
      if (fId.includes('hinh-thang') || topic.includes('hình thang') || fId.includes('trapezoid')) {
        const a = getVal(['a', 'b_lon'], 8);
        const b = getVal(['b', 'b_nho'], 4);
        return Number(((a + b) / 2).toFixed(1));
      }
      if (fId.includes('duong-tron') || topic.includes('đường tròn') || topic.includes('tiếp tuyến')) {
        const R = getVal(['R'], 5);
        const d = getVal(['d'], 7);
        if (d >= R) return Number(Math.sqrt(d * d - R * R).toFixed(2));
        return 0;
      }
      if (fId.includes('hang-dang-thuc') || topic.includes('hằng đẳng thức') || topic.includes('bình phương')) {
        const a = getVal(['a'], 3);
        const b = getVal(['b'], 2);
        return (a + b) * (a + b);
      }
      if (fId.includes('truc-so') || fId.includes('so-nguyen') || fId.includes('gia-tri-tuyet-doi') || topic.includes('trục số')) {
        const x = getVal(['x'], -3);
        return Math.abs(x);
      }
      if (fId.includes('parabol') || fId.includes('bac-hai') || topic.includes('parabol') || topic.includes('ax^2')) {
        const a = getVal(['a'], 1) || 1;
        const b = getVal(['b'], -2);
        const c = getVal(['c'], -3);
        return Number((-(b * b - 4 * a * c) / (4 * a)).toFixed(2));
      }
    }

    if (isHighSchoolMath) {
      if (fId.includes('luong-giac') || fId.includes('trigonometry') || fId.includes('sin') || fId.includes('cos') || fId.includes('tan') || topic.includes('lượng giác')) {
        const deg = getVal(['alpha', 'a'], 45);
        const rad = (deg * Math.PI) / 180;
        if (fId.includes('cos') || topic.includes('cos')) return Number(Math.cos(rad).toFixed(3));
        if (fId.includes('tan') || topic.includes('tan')) {
          const c = Math.cos(rad);
          return Math.abs(c) > 0.001 ? Number(Math.tan(rad).toFixed(3)) : null;
        }
        return Number(Math.sin(rad).toFixed(3));
      }
      if (fId.includes('dao-ham') || fId.includes('derivative') || fId.includes('tiep-tuyen') || topic.includes('đạo hàm') || topic.includes('tiếp tuyến')) {
        const x0 = getVal(['x0', 'x_0'], 1.0);
        // Hàm số chuẩn f(x) = 1/4 x^3 - x => f'(x) = 3/4 x^2 - 1
        const slope = 0.75 * x0 * x0 - 1.0;
        return Number(slope.toFixed(2));
      }
      if (fId.includes('tich-phan') || fId.includes('nguyen-ham') || fId.includes('integral') || fId.includes('riemann') || topic.includes('tích phân')) {
        const b = getVal(['b'], 3.0);
        // f(x) = 0.4 x^2 + 0.8 => Tích phân từ 0 đến b là (0.4/3)*b^3 + 0.8*b
        const exact = (0.4 / 3) * Math.pow(b, 3) + 0.8 * b;
        return Number(exact.toFixed(2));
      }
      if (fId.includes('so-phuc') || fId.includes('complex') || topic.includes('số phức')) {
        const a = getVal(['a'], 3);
        const b = getVal(['b'], 4);
        return Number(Math.sqrt(a * a + b * b).toFixed(2));
      }
      if (fId.includes('vector') || fId.includes('tich-vo-huong') || fId.includes('dot-product') || topic.includes('vector') || topic.includes('tích vô hướng')) {
        const u = getVal(['len_u'], 4);
        const v = getVal(['len_v'], 5);
        const th = getVal(['theta'], 60);
        const dot = u * v * Math.cos((th * Math.PI) / 180);
        return Number(dot.toFixed(2));
      }
      if (fId.includes('cap-so') || topic.includes('cấp số')) {
        const u1 = getVal(['u1'], 2);
        const step = getVal(['d', 'q'], 3);
        if (fId.includes('nhan') || topic.includes('nhân')) {
          return Number((u1 * Math.pow(step, 5)).toFixed(1));
        }
        return Number((u1 + 5 * step).toFixed(1));
      }
      if (fId.includes('logarit') || fId.includes('mu') || topic.includes('logarit') || topic.includes('mũ')) {
        const base = Math.max(0.1, getVal(['a'], 2.0));
        const x = getVal(['x'], 2.0);
        if (fId.includes('logarit') || topic.includes('logarit')) {
          return x > 0 && base !== 1 ? Number((Math.log(x) / Math.log(base)).toFixed(2)) : 0;
        }
        return Number(Math.pow(base, x).toFixed(2));
      }
    }

    try {
      const expr = formula.interactive?.expression_js;
      if (expr && expr.trim()) {
        const keys = Object.keys(sliderValues);
        const vals = Object.values(sliderValues);
        // eslint-disable-next-line no-new-func
        const fn = new Function(...keys, `try { return (${expr}); } catch(e) { return null; }`);
        const res = fn(...vals);
        if (typeof res === 'number' && !isNaN(res) && isFinite(res)) {
          return res;
        }
      }
    } catch {
      // Fallback
    }

    return null;
  }, [isComputable, formula.interactive?.expression_js, sliderValues, isElementary, isSecondaryMath, isHighSchoolMath, inputConfigs, fId, topic]);

  // Thông tin ký hiệu & đơn vị đầu ra chuẩn mực (Ưu tiên chuẩn Tiểu học Lớp 5, THCS & THPT)
  const outputInfo = useMemo(() => {
    if (isElementary) {
      if (fId.includes('thoi-diem-gap-nhau')) return { symbol: 't_gặp', unit: 'giờ', name: 'Thời điểm hai xe gặp nhau' };
      if (fId.includes('quang-duong')) return { symbol: 's', unit: 'km', name: 'Quãng đường ô tô đi được' };
      if (fId.includes('van-toc-xuoi-dong')) return { symbol: 'v_xuôi', unit: 'km/h', name: 'Vận tốc thuyền khi xuôi dòng' };
      if (fId.includes('van-toc-nguoc-dong')) return { symbol: 'v_ngược', unit: 'km/h', name: 'Vận tốc thuyền khi ngược dòng' };
      if (fId.includes('van-toc')) return { symbol: 'v', unit: 'km/h', name: 'Vận tốc ô tô' };
      if (fId.includes('thoi-gian') || fId.includes('nguoc-chieu') || fId.includes('cung-chieu')) return { symbol: 't', unit: 'giờ', name: 'Thời gian đi' };
      if (fId.includes('tam-giac') && !fId.includes('chu-vi')) return { symbol: 'S', unit: 'cm²', name: 'Diện tích hình tam giác' };
      if (fId.includes('hinh-thang')) return { symbol: 'S', unit: 'cm²', name: 'Diện tích hình thang' };
      if (fId.includes('hinh-hop') || fId.includes('lap-phuong') || topic.includes('thể tích')) return { symbol: 'V', unit: 'cm³', name: 'Thể tích khối hộp' };
      if (fId.includes('hinh-tron') && fId.includes('dien-tich')) return { symbol: 'S', unit: 'cm²', name: 'Diện tích hình tròn' };
      if (fId.includes('hinh-tron')) return { symbol: 'C', unit: 'cm', name: 'Chu vi hình tròn' };
      if (fId.includes('chu-vi')) return { symbol: 'P', unit: 'm', name: 'Chu vi' };
      if (fId.includes('dien-tich')) return { symbol: 'S', unit: 'm²', name: 'Diện tích' };
      if (fId.includes('tong-hieu')) return { symbol: 'Số lớn', unit: '', name: 'Số lớn (Số bé = Tổng - Số lớn)' };
      if (fId.includes('tong-va-ti-so')) return { symbol: 'Số lớn', unit: '', name: 'Số lớn (bằng số phần lớn × 1 phần)' };
      if (fId.includes('hieu-va-ti-so')) return { symbol: 'Số lớn', unit: '', name: 'Số lớn (bằng số phần lớn × 1 phần)' };
      if (fId.includes('ti-so') || fId.includes('phan-so')) return { symbol: 'Tỉ số', unit: '', name: 'Tỉ số a/b' };
    }
    if (isSecondaryMath) {
      if (fId.includes('ta-let') || fId.includes('thales') || topic.includes('ta-lét') || topic.includes('thales')) {
        return { symbol: 'Tỉ số k', unit: '', name: 'Tỉ số đoạn thẳng Ta-lét AM/AB' };
      }
      if (fId.includes('pytago') || topic.includes('pytago')) {
        return { symbol: 'c', unit: 'cm', name: 'Cạnh huyền c = √(a² + b²)' };
      }
      if (fId.includes('he-thuc-luong') || fId.includes('duong-cao') || fId.includes('hinh-chieu') || topic.includes('hệ thức lượng')) {
        return { symbol: 'AH', unit: 'cm', name: 'Đường cao AH = √(BH · CH)' };
      }
      if (fId.includes('hinh-thang') || topic.includes('hình thang') || fId.includes('trapezoid')) {
        return { symbol: 'MN', unit: 'cm', name: 'Đường trung bình MN = (a + b) : 2' };
      }
      if (fId.includes('duong-tron') || topic.includes('đường tròn') || topic.includes('tiếp tuyến')) {
        return { symbol: 'AB', unit: 'cm', name: 'Đoạn tiếp tuyến AB = √(OA² − R²)' };
      }
      if (fId.includes('hang-dang-thuc') || topic.includes('hằng đẳng thức') || topic.includes('bình phương')) {
        return { symbol: '(a + b)²', unit: '', name: 'Khai triển hằng đẳng thức' };
      }
      if (fId.includes('truc-so') || fId.includes('so-nguyen') || fId.includes('gia-tri-tuyet-doi') || topic.includes('trục số')) {
        return { symbol: '|x|', unit: '', name: 'Khoảng cách đến gốc O' };
      }
      if (fId.includes('parabol') || fId.includes('bac-hai') || topic.includes('parabol') || topic.includes('ax^2')) {
        return { symbol: 'y_đỉnh', unit: '', name: 'Tung độ đỉnh parabol' };
      }
    }
    if (isHighSchoolMath) {
      if (fId.includes('luong-giac') || fId.includes('trigonometry') || fId.includes('sin') || fId.includes('cos') || fId.includes('tan') || topic.includes('lượng giác')) {
        if (fId.includes('cos') || topic.includes('cos')) return { symbol: 'cos α', unit: '', name: 'Giá trị cos α' };
        if (fId.includes('tan') || topic.includes('tan')) return { symbol: 'tan α', unit: '', name: 'Giá trị tan α = sin/cos' };
        return { symbol: 'sin α', unit: '', name: 'Giá trị sin α' };
      }
      if (fId.includes('dao-ham') || fId.includes('derivative') || fId.includes('tiep-tuyen') || topic.includes('đạo hàm') || topic.includes('tiếp tuyến')) {
        return { symbol: "k = f'(x₀)", unit: '', name: 'Hệ số góc tiếp tuyến tại x₀' };
      }
      if (fId.includes('tich-phan') || fId.includes('nguyen-ham') || fId.includes('integral') || fId.includes('riemann') || topic.includes('tích phân')) {
        return { symbol: 'S', unit: 'đvdt', name: 'Diện tích hình phẳng tích phân Riemann' };
      }
      if (fId.includes('so-phuc') || fId.includes('complex') || topic.includes('số phức')) {
        return { symbol: '|z|', unit: '', name: 'Mô-đun số phức |z| = √(a² + b²)' };
      }
      if (fId.includes('vector') || fId.includes('tich-vo-huong') || fId.includes('dot-product') || topic.includes('vector') || topic.includes('tích vô hướng')) {
        return { symbol: 'u · v', unit: '', name: 'Tích vô hướng |u|·|v|·cos(θ)' };
      }
      if (fId.includes('cap-so') || topic.includes('cấp số')) {
        return { symbol: 'u₆', unit: '', name: 'Số hạng thứ 6 của dãy cấp số' };
      }
      if (fId.includes('logarit') || fId.includes('mu') || topic.includes('logarit') || topic.includes('mũ')) {
        if (fId.includes('logarit') || topic.includes('logarit')) return { symbol: 'logₐ(x)', unit: '', name: 'Logarit cơ số a của x' };
        return { symbol: 'y = aˣ', unit: '', name: 'Giá trị hàm số mũ' };
      }
    }
    if (formula.interactive?.output?.symbol) {
      return {
        symbol: formula.interactive.output.symbol,
        unit: formula.interactive.output.unit || '',
        name: formula.interactive.output.name || formula.name_vi || 'Giá trị tính toán',
      };
    }
    return {
      symbol: '',
      unit: '',
      name: formula.name_vi || 'Giá trị tính toán',
    };
  }, [formula.interactive?.output, formula.name_vi, isElementary, isSecondaryMath, isHighSchoolMath, fId, topic]);

  const outputSymbol = outputInfo.symbol;
  const outputUnit = outputInfo.unit;
  const outputName = outputInfo.name;

  // Lấy các tham số chính để dựng đồ họa trực quan logic (tương thích ngược)
  const v1 = Object.values(sliderValues)[0] ?? 10;
  const v2 = Object.values(sliderValues)[1] ?? 5;

  const renderElementarySimulation = () => {
    // 0.1 Chuyển động đều quãng đường s = v * t (hoặc tìm v, t)
    if (
      fId.includes('quang-duong') ||
      (fId.includes('chuyen-dong') && !fId.includes('nguoc-chieu') && !fId.includes('cung-chieu') && !fId.includes('dong-nuoc') && !fId.includes('van-toc') && !fId.includes('thoi-gian') && !fId.includes('thoi-diem') && !fId.includes('gap-nhau'))
    ) {
      const speed = getVal(['v'], 40);
      const time = getVal(['t'], 2.5);
      const distance = speed * time;
      const carX = Math.min(270, Math.max(30, 30 + (Math.min(6, time) / 6) * 240));

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 135" style={{ width: '100%', height: '125px' }}>
            <rect x="0" y="0" width="350" height="90" fill="#f0fdf4" rx="4" />
            <circle cx="50" cy="25" r="12" fill="#e2e8f0" opacity="0.6" />
            <circle cx="65" cy="20" r="15" fill="#e2e8f0" opacity="0.6" />
            <circle cx="80" cy="25" r="12" fill="#e2e8f0" opacity="0.6" />

            {/* Mặt đường nhựa và vạch kẻ */}
            <rect x="10" y="85" width="330" height="28" fill="#334155" rx="3" />
            <line x1="20" y1="99" x2="330" y2="99" stroke="#f59e0b" strokeWidth="2" strokeDasharray="12 8" />

            {/* Cột cây số 0km */}
            <g transform="translate(25, 62)">
              <rect x="0" y="0" width="18" height="22" rx="3" fill="#ef4444" />
              <circle cx="9" cy="8" r="4" fill="#ffffff" />
              <text x="9" y="19" textAnchor="middle" fontSize="6.5" fontWeight="bold" fill="#ffffff">0km</text>
            </g>

            {/* Cột cây số đích đến s km */}
            <g transform="translate(305, 62)">
              <rect x="0" y="0" width="22" height="22" rx="3" fill="#10b981" />
              <circle cx="11" cy="8" r="4" fill="#ffffff" />
              <text x="11" y="19" textAnchor="middle" fontSize="6" fontWeight="bold" fill="#ffffff">{distance}km</text>
            </g>

            {/* Chiếc xe ô tô màu đỏ chuyển động */}
            <g transform={`translate(${carX - 25}, 65)`}>
              <path d="M 0 15 L 8 6 L 32 6 L 42 15 L 48 15 Q 50 15 50 18 L 50 25 L 0 25 Z" fill="#ef4444" />
              <polygon points="10,14 14,8 24,8 24,14" fill="#bae6fd" />
              <polygon points="26,14 26,8 31,8 37,14" fill="#bae6fd" />
              <circle cx="12" cy="25" r="5" fill="#1e293b" />
              <circle cx="12" cy="25" r="2" fill="#cbd5e1" />
              <circle cx="38" cy="25" r="5" fill="#1e293b" />
              <circle cx="38" cy="25" r="2" fill="#cbd5e1" />
              <polygon points="50,19 55,16 55,23" fill="#fef08a" opacity="0.8" />
              <text x="25" y="4" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#b91c1c">v = {speed} km/h</text>
            </g>

            {/* Thước đo quãng đường */}
            <line x1="25" y1="120" x2="325" y2="120" stroke="#0284c7" strokeWidth="1.5" />
            <line x1="25" y1="116" x2="25" y2="124" stroke="#0284c7" strokeWidth="1.5" />
            <line x1="325" y1="116" x2="325" y2="124" stroke="#0284c7" strokeWidth="1.5" />
            <text x="175" y="131" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0369a1">
              Quãng đường s = {speed} × {time} = {distance} km (sau {time} giờ)
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#166534', background: '#f0fdf4', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            🚗 <b>Quy luật Lớp 5:</b> Cứ 1 giờ xe đi được {speed} km. Đi trong {time} giờ thì quãng đường là lấy {speed} nhân với {time} = <b>{distance} km</b>.
          </div>
        </div>
      );
    }

    // 0.2 Hai xe chuyển động ngược chiều gặp nhau (Đúng số liệu SGK: 180 km, 50 km/h, 40 km/h)
    if (fId.includes('nguoc-chieu') || fId.includes('thoi-diem-gap-nhau') || topic.includes('ngược chiều')) {
      const sDist = getVal(['s', 'dist'], 180);
      const vA = getVal(['v1', 'v_1'], 50);
      const vB = getVal(['v2', 'v_2'], 40);
      const t0 = getVal(['t0', 't_0'], 7);
      const vSum = vA + vB;
      const tMeet = vSum > 0 ? sDist / vSum : 0;
      const meetRatio = vSum > 0 ? vA / vSum : 0.5;
      const meetX = 30 + meetRatio * 280;
      const isThoiDiem = fId.includes('thoi-diem-gap-nhau');

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 135" style={{ width: '100%', height: '125px' }}>
            <rect x="0" y="0" width="350" height="90" fill="#eff6ff" rx="4" />
            <rect x="10" y="85" width="330" height="28" fill="#334155" rx="3" />
            <line x1="20" y1="99" x2="330" y2="99" stroke="#f59e0b" strokeWidth="2" strokeDasharray="12 8" />

            <circle cx="30" cy="76" r="4" fill="#ef4444" />
            <text x="30" y="66" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#dc2626">A (Xe Đỏ)</text>

            <circle cx="310" cy="76" r="4" fill="#2563eb" />
            <text x="310" y="66" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#2563eb">B (Xe Xanh)</text>

            {/* Xe Đỏ chạy từ A sang phải */}
            <g transform="translate(45, 68)">
              <rect x="0" y="0" width="28" height="14" rx="2" fill="#ef4444" />
              <circle cx="6" cy="14" r="3.5" fill="#1e293b" />
              <circle cx="22" cy="14" r="3.5" fill="#1e293b" />
              <polygon points="32,7 28,3 28,11" fill="#ef4444" />
              <text x="14" y="-3" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#dc2626">v₁ = {vA} km/h</text>
            </g>

            {/* Xe Xanh chạy từ B sang trái */}
            <g transform="translate(265, 68)">
              <rect x="0" y="0" width="28" height="14" rx="2" fill="#2563eb" />
              <circle cx="6" cy="14" r="3.5" fill="#1e293b" />
              <circle cx="22" cy="14" r="3.5" fill="#1e293b" />
              <polygon points="-4,7 0,3 0,11" fill="#2563eb" />
              <text x="14" y="-3" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#1d4ed8">v₂ = {vB} km/h</text>
            </g>

            {/* Cờ cắm điểm gặp nhau */}
            <g transform={`translate(${meetX}, 45)`}>
              <line x1="0" y1="0" x2="0" y2="40" stroke="#059669" strokeWidth="2" strokeDasharray="3 2" />
              <polygon points="0,0 14,5 0,10" fill="#10b981" />
              <text x="2" y="-4" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#059669">
                {isThoiDiem ? `Gặp lúc ${(t0 + tMeet).toFixed(1)}h` : `Gặp nhau sau ${tMeet.toFixed(1)}h`}
              </text>
            </g>

            <line x1="30" y1="120" x2="310" y2="120" stroke="#64748b" strokeWidth="1.5" />
            <line x1="30" y1="116" x2="30" y2="124" stroke="#64748b" strokeWidth="1.5" />
            <line x1="310" y1="116" x2="310" y2="124" stroke="#64748b" strokeWidth="1.5" />
            <text x="170" y="131" textAnchor="middle" fontSize="8.5" fontWeight="bold" fill="#334155">
              Khoảng cách s = {sDist} km | Tổng vận tốc v₁ + v₂ = {vSum} km/h
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#1e40af', background: '#eff6ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            🤝 <b>Logic Lớp 5:</b> Sau 1 giờ cả hai xe cùng đi được {vA} + {vB} = <b>{vSum} km</b>. Thời gian gặp nhau: t = {sDist} : {vSum} = <b>{tMeet.toFixed(2)} giờ</b>.
            {isThoiDiem && <span> (Hai xe xuất phát lúc <b>{t0} giờ</b> $\rightarrow$ Gặp nhau lúc: {t0} + {tMeet.toFixed(1)} = <b>{(t0 + tMeet).toFixed(1)} giờ</b>).</span>}
          </div>
        </div>
      );
    }

    // 0.3 Hai xe cùng chiều đuổi kịp (Đúng số liệu SGK: 40 km, 50 km/h, 10 km/h)
    if (fId.includes('cung-chieu') || topic.includes('cùng chiều') || fId.includes('duoi-kip')) {
      const sDist = getVal(['s', 'dist'], 40);
      const vChaser = getVal(['v1', 'v_1'], 50);
      const vLeader = getVal(['v2', 'v_2'], 10);
      const vDiff = Math.max(1, vChaser - vLeader);
      const tCatch = sDist / vDiff;

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 135" style={{ width: '100%', height: '125px' }}>
            <rect x="0" y="0" width="350" height="90" fill="#fffbeb" rx="4" />
            <rect x="10" y="85" width="330" height="28" fill="#334155" rx="3" />
            <line x1="20" y1="99" x2="330" y2="99" stroke="#f59e0b" strokeWidth="2" strokeDasharray="12 8" />

            <g transform="translate(40, 68)">
              <rect x="0" y="0" width="30" height="14" rx="2" fill="#ef4444" />
              <circle cx="7" cy="14" r="3.5" fill="#1e293b" />
              <circle cx="23" cy="14" r="3.5" fill="#1e293b" />
              <polygon points="34,7 30,3 30,11" fill="#ef4444" />
              <text x="15" y="-3" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#dc2626">Xe sau ({vChaser} km/h)</text>
            </g>

            <line x1="75" y1="60" x2="195" y2="60" stroke="#d97706" strokeWidth="1.5" strokeDasharray="4 3" />
            <polygon points="195,60 190,57 190,63" fill="#d97706" />
            <text x="135" y="54" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#d97706">Cách {sDist} km</text>

            <g transform="translate(200, 68)">
              <rect x="0" y="0" width="24" height="14" rx="2" fill="#059669" />
              <circle cx="5" cy="14" r="3.5" fill="#1e293b" />
              <circle cx="19" cy="14" r="3.5" fill="#1e293b" />
              <polygon points="28,7 24,3 24,11" fill="#059669" />
              <text x="12" y="-3" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#059669">Xe trước ({vLeader} km/h)</text>
            </g>

            <g transform="translate(305, 55)">
              <line x1="0" y1="0" x2="0" y2="30" stroke="#b45309" strokeWidth="2" strokeDasharray="2 2" />
              <circle cx="0" cy="0" r="4" fill="#f59e0b" />
              <text x="0" y="-4" textAnchor="middle" fontSize="7.5" fontWeight="bold" fill="#b45309">Đuổi kịp!</text>
            </g>

            <text x="175" y="128" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#78350f">
              Hiệu vận tốc = {vChaser} - {vLeader} = {vDiff} km/h | Thời gian đuổi kịp t = {tCatch.toFixed(1)} giờ
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#92400e', background: '#fffbeb', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            🏃 <b>Logic Lớp 5:</b> Mỗi giờ xe sau rút ngắn được khoảng cách là {vChaser} - {vLeader} = <b>{vDiff} km</b>. Thời gian để đuổi kịp: t = {sDist} : {vDiff} = <b>{tCatch.toFixed(2)} giờ</b>.
          </div>
        </div>
      );
    }

    // 0.4 Thuyền trên dòng nước
    if (fId.includes('dong-nuoc') || fId.includes('xuoi-dong') || fId.includes('nguoc-dong') || topic.includes('dòng nước')) {
      const vBoat = getVal(['v'], 15);
      const vStream = getVal(['vn'], 3);
      const vDown = vBoat + vStream;
      const vUp = Math.max(0, vBoat - vStream);

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 135" style={{ width: '100%', height: '125px' }}>
            <rect x="10" y="20" width="330" height="90" fill="#e0f2fe" rx="6" />
            <path d="M 20 45 Q 40 40, 60 45 T 100 45 T 140 45 T 180 45 T 220 45 T 260 45 T 300 45" fill="none" stroke="#bae6fd" strokeWidth="2" />
            <path d="M 30 75 Q 50 70, 70 75 T 110 75 T 150 75 T 190 75 T 230 75 T 270 75 T 310 75" fill="none" stroke="#bae6fd" strokeWidth="2" />

            <g transform="translate(140, 32)">
              <line x1="0" y1="0" x2="60" y2="0" stroke="#0284c7" strokeWidth="2" />
              <polygon points="60,0 54,-3 54,3" fill="#0284c7" />
              <text x="30" y="-4" textAnchor="middle" fontSize="7.5" fontWeight="bold" fill="#0369a1">Dòng nước chảy: {vStream} km/h →</text>
            </g>

            <g transform="translate(150, 52)">
              <polygon points="0,20 8,30 38,30 46,20" fill="#b45309" stroke="#451a03" strokeWidth="1" />
              <line x1="23" y1="5" x2="23" y2="20" stroke="#451a03" strokeWidth="2" />
              <polygon points="23,5 36,15 23,18" fill="#ffffff" stroke="#cbd5e1" strokeWidth="1" />
              <text x="23" y="-2" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#0f172a">Thuyền ({vBoat} km/h)</text>
            </g>

            <text x="175" y="125" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0369a1">
              Xuôi dòng: {vBoat} + {vStream} = {vDown} km/h | Ngược dòng: {vBoat} - {vStream} = {vUp} km/h
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#0369a1', background: '#f0f9ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            🚤 <b>Logic Lớp 5:</b> Xuôi dòng được nước đẩy thêm ({vBoat} + {vStream} = <b>{vDown} km/h</b>). Ngược dòng bị nước cản ({vBoat} - {vStream} = <b>{vUp} km/h</b>).
          </div>
        </div>
      );
    }

    // 0.5 Hình tam giác cắt ghép đôi
    if (fId.includes('tam-giac')) {
      const baseA = getVal(['a'], 8);
      const heightH = getVal(['h'], 5);
      const areaTri = (baseA * heightH) / 2;

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 135" style={{ width: '100%', height: '125px' }}>
            <rect x="0" y="0" width="350" height="135" fill="#f8fafc" rx="4" />
            <rect x="100" y="25" width="140" height="75" fill="#e0f2fe" stroke="#0284c7" strokeWidth="1.5" strokeDasharray="4 3" opacity="0.6" />

            <polygon points="100,100 240,100 150,25" fill="#38bdf8" stroke="#0284c7" strokeWidth="2" />
            <line x1="150" y1="25" x2="150" y2="100" stroke="#dc2626" strokeWidth="1.5" strokeDasharray="2 2" />
            <rect x="150" y="93" width="7" height="7" fill="none" stroke="#dc2626" strokeWidth="1" />
            <text x="140" y="65" fontSize="8" fontWeight="bold" fill="#dc2626">h = {heightH}</text>

            <polygon points="100,100 150,25 100,25" fill="#fed7aa" stroke="#f59e0b" strokeWidth="1" opacity="0.7" />
            <polygon points="240,100 150,25 240,25" fill="#fed7aa" stroke="#f59e0b" strokeWidth="1" opacity="0.7" />

            <text x="170" y="114" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0284c7">Đáy a = {baseA} cm</text>
            <text x="170" y="16" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0369a1">
              Ghép 2 tam giác = 1 hình chữ nhật (a × h)
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#0369a1', background: '#f0f9ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            ✂️ <b>Logic Lớp 5:</b> Hai tam giác bằng nhau ghép lại sẽ tạo thành một hình chữ nhật diện tích a × h. Do đó 1 tam giác có diện tích bằng một nửa: S = ({baseA} × {heightH}) : 2 = <b>{areaTri.toFixed(1)} cm²</b>.
          </div>
        </div>
      );
    }

    // 0.6 Hình thang ghép thành hình bình hành (Đáy lớn a > Đáy bé b)
    if (fId.includes('hinh-thang') || topic.includes('hình thang')) {
      const baseBig = Math.max(5, getVal(['a'], 8));
      const baseSmall = Math.min(baseBig - 1, Math.max(2, getVal(['b'], 4)));
      const heightTrap = getVal(['h'], 5);
      const areaTrap = ((baseBig + baseSmall) * heightTrap) / 2;

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 135" style={{ width: '100%', height: '125px' }}>
            <rect x="0" y="0" width="350" height="135" fill="#faf5ff" rx="4" />
            <polygon points="70,100 210,100 170,35 110,35" fill="#c084fc" stroke="#7e22ce" strokeWidth="2" />
            <polygon points="210,100 310,100 270,35 170,35" fill="#fbcfe8" stroke="#db2777" strokeWidth="1.5" strokeDasharray="3 2" />

            <line x1="110" y1="35" x2="110" y2="100" stroke="#dc2626" strokeWidth="1.5" strokeDasharray="2 2" />
            <text x="100" y="70" fontSize="8" fontWeight="bold" fill="#dc2626">h={heightTrap}</text>

            <text x="140" y="27" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#7e22ce">b = {baseSmall}</text>
            <text x="140" y="114" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#7e22ce">a = {baseBig}</text>
            <text x="240" y="27" textAnchor="middle" fontSize="7.5" fill="#db2777">Ghép đáy (a + b)</text>

            <text x="175" y="130" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#6b21a8">
              S = ({baseBig} + {baseSmall}) × {heightTrap} : 2 = {areaTrap.toFixed(1)} cm²
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#6b21a8', background: '#faf5ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            📜 <b>Bài thơ Lớp 5:</b> <i>'Muốn tính diện tích hình thang / Đáy lớn đáy bé ta mang cộng vào / Thế rồi nhân với chiều cao / Chia đôi lấy nửa thế nào cũng ra!'</i>
          </div>
        </div>
      );
    }

    // 0.7 Hình hộp chữ nhật & hình lập phương xếp khối Lego 1 cm³
    if (fId.includes('hinh-hop') || fId.includes('lap-phuong') || (topic.includes('thể tích') && isElementary)) {
      const lenA = Math.min(5, Math.max(1, Math.round(getVal(['a'], 5))));
      const widB = Math.min(4, Math.max(1, Math.round(getVal(['b'], 3))));
      const heiC = Math.min(3, Math.max(1, Math.round(getVal(['c'], 4))));
      const volBox = lenA * widB * heiC;

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 135" style={{ width: '100%', height: '125px' }}>
            <rect x="0" y="0" width="350" height="135" fill="#f8fafc" rx="4" />
            <g transform="translate(90, 32)">
              {Array.from({ length: heiC }).map((_, z) =>
                Array.from({ length: widB }).map((_, y) =>
                  Array.from({ length: lenA }).map((_, x) => {
                    const isoX = (x - y) * 16 + 80;
                    const isoY = (x + y) * 8 - z * 16 + 25;
                    return (
                      <g key={`${x}-${y}-${z}`} transform={`translate(${isoX}, ${isoY})`}>
                        <polygon points="0,0 12,-6 24,0 12,6" fill="#38bdf8" stroke="#0284c7" strokeWidth="0.8" />
                        <polygon points="0,0 12,6 12,18 0,12" fill="#0284c7" stroke="#0369a1" strokeWidth="0.8" />
                        <polygon points="12,6 24,0 24,12 12,18" fill="#0ea5e9" stroke="#0284c7" strokeWidth="0.8" />
                      </g>
                    );
                  })
                )
              )}
            </g>
            <text x="175" y="128" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0369a1">
              Dài ({lenA}) × Rộng ({widB}) × Cao ({heiC}) = {volBox} khối 1 cm³
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#0369a1', background: '#f0f9ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            🧱 <b>Logic Lớp 5:</b> 1 hàng có {lenA} khối Lego 1cm³. Lớp đáy có {lenA} × {widB} = {lenA * widB} khối. Xếp cao {heiC} tầng → Thể tích là: V = {lenA} × {widB} × {heiC} = <b>{volBox} cm³</b>.
          </div>
        </div>
      );
    }

    // 0.8 Hình tròn (Chu vi & Diện tích)
    if (fId.includes('hinh-tron') || topic.includes('hình tròn')) {
      const radiusR = getVal(['r'], 5);
      const circ = 2 * radiusR * 3.14;
      const areaCircle = radiusR * radiusR * 3.14;

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 135" style={{ width: '100%', height: '125px' }}>
            <rect x="0" y="0" width="350" height="135" fill="#fef2f2" rx="4" />
            <circle cx="95" cy="65" r="42" fill="#fecaca" stroke="#dc2626" strokeWidth="2" />
            <line x1="95" y1="65" x2="137" y2="65" stroke="#991b1b" strokeWidth="2" />
            <circle cx="95" cy="65" r="3" fill="#991b1b" />
            <text x="115" y="59" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#991b1b">r = {radiusR}</text>
            <text x="95" y="60" textAnchor="end" fontSize="8" fill="#7f1d1d">Tâm O</text>

            <g transform="translate(165, 30)">
              <rect x="0" y="0" width="165" height="34" rx="4" fill="#ffffff" stroke="#fca5a5" />
              <text x="8" y="14" fontSize="8" fontWeight="bold" fill="#b91c1c">Chu vi (viền quanh):</text>
              <text x="8" y="27" fontSize="8.5" fill="#1e293b">C = 2 × {radiusR} × 3,14 = {circ.toFixed(2)} cm</text>
            </g>
            <g transform="translate(165, 72)">
              <rect x="0" y="0" width="165" height="34" rx="4" fill="#ffffff" stroke="#fca5a5" />
              <text x="8" y="14" fontSize="8" fontWeight="bold" fill="#b91c1c">Diện tích (mặt trong):</text>
              <text x="8" y="27" fontSize="8.5" fill="#1e293b">S = {radiusR} × {radiusR} × 3,14 = {areaCircle.toFixed(2)} cm²</text>
            </g>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#991b1b', background: '#fef2f2', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            ⭕ <b>Logic Lớp 5:</b> Chu vi là sợi dây đo quanh viền bánh xe ($C = 2 \times r \times 3,14$). Diện tích là phần mặt phẳng bên trong chiếc bánh ($S = r \times r \times 3,14$).
          </div>
        </div>
      );
    }

    // 0.9 Hình chữ nhật & hình vuông
    if (fId.includes('chu-nhat') || fId.includes('hinh-vuong')) {
      const recA = getVal(['a'], 8);
      const recB = fId.includes('hinh-vuong') ? recA : getVal(['b'], 5);
      const recP = fId.includes('hinh-vuong') ? recA * 4 : (recA + recB) * 2;
      const recS = recA * recB;

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 135" style={{ width: '100%', height: '125px' }}>
            <rect x="0" y="0" width="350" height="135" fill="#f0fdf4" rx="4" />
            <g transform="translate(110, 25)">
              <rect x="0" y="0" width="130" height="65" fill="#bbf7d0" stroke="#16a34a" strokeWidth="2" />
              <text x="65" y="-6" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#15803d">Dài a = {recA} m</text>
              <text x="-10" y="36" textAnchor="end" fontSize="9" fontWeight="bold" fill="#15803d">{fId.includes('hinh-vuong') ? `a = ${recA} m` : `Rộng b = ${recB} m`}</text>
              <text x="65" y="38" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#166534">S = {recS} m²</text>
            </g>
            <text x="175" y="118" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#166534">
              Chu vi P = {recP} m | Diện tích S = {recS} m²
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#166534', background: '#f0fdf4', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            📐 <b>Logic Lớp 5:</b> Chu vi bằng (Dài + Rộng) nhân 2. Diện tích bằng Dài nhân Rộng (cùng đơn vị đo).
          </div>
        </div>
      );
    }

    // 0.10 Sơ đồ đoạn thẳng (Tape Diagram) cho bài toán Tổng - Hiệu (Chuẩn phương pháp GDPT Lớp 4-5)
    if (fId.includes('tong-va-hieu') || fId.includes('tong-hieu') || (topic.includes('tổng') && topic.includes('hiệu') && !topic.includes('tỉ'))) {
      const sTong = getVal(['s', 'tong', 's_tong'], 50);
      const sHieu = getVal(['h', 'hieu', 's_hieu'], 10);
      const soBe = (sTong - sHieu) / 2;
      const soLon = (sTong + sHieu) / 2;
      const totalW = 180;
      const barBase = Math.min(130, Math.max(40, (soBe / Math.max(1, sTong)) * totalW));
      const diffW = Math.min(90, Math.max(20, (sHieu / Math.max(1, sTong)) * totalW));

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 145" style={{ width: '100%', height: '135px' }}>
            <rect x="0" y="0" width="350" height="145" fill="#eff6ff" rx="4" />

            {/* Hàng số lớn */}
            <text x="18" y="38" fontSize="9.5" fontWeight="bold" fill="#1e40af">Số lớn:</text>
            <rect x="68" y="24" width={barBase} height="18" fill="#3b82f6" rx="2" />
            <text x={68 + barBase / 2} y="36" textAnchor="middle" fontSize="8" fill="#ffffff" fontWeight="bold">{soBe}</text>
            <rect x={68 + barBase} y="24" width={diffW} height="18" fill="#bfdbfe" stroke="#2563eb" strokeDasharray="3 2" rx="2" />
            <text x={68 + barBase + diffW / 2} y="36" textAnchor="middle" fontSize="8" fill="#1d4ed8" fontWeight="bold">+{sHieu}</text>

            {/* Dấu ngoặc nhọn chỉ phần hiệu ở số lớn */}
            <line x1={68 + barBase} y1="20" x2={68 + barBase + diffW} y2="20" stroke="#2563eb" strokeWidth="1.2" />
            <line x1={68 + barBase} y1="18" x2={68 + barBase} y2="22" stroke="#2563eb" strokeWidth="1.2" />
            <line x1={68 + barBase + diffW} y1="18" x2={68 + barBase + diffW} y2="22" stroke="#2563eb" strokeWidth="1.2" />
            <text x={68 + barBase + diffW / 2} y="15" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#1d4ed8">Hiệu: {sHieu}</text>

            {/* Đường nét đứt gióng xuống từ mốc số bé */}
            <line x1={68 + barBase} y1="42" x2={68 + barBase} y2="60" stroke="#94a3b8" strokeDasharray="2 2" strokeWidth="1" />

            {/* Hàng số bé */}
            <text x="18" y="74" fontSize="9.5" fontWeight="bold" fill="#1e40af">Số bé:</text>
            <rect x="68" y="60" width={barBase} height="18" fill="#3b82f6" rx="2" />
            <text x={68 + barBase / 2} y="72" textAnchor="middle" fontSize="8" fill="#ffffff" fontWeight="bold">{soBe}</text>

            {/* Ngoặc ôm tổng hai số bên phải */}
            <path
              d={`M ${68 + barBase + diffW + 8} 24 Q ${68 + barBase + diffW + 18} 51, ${68 + barBase + diffW + 8} 78`}
              fill="none"
              stroke="#1e3a8a"
              strokeWidth="1.5"
            />
            <text x={68 + barBase + diffW + 24} y="54" fontSize="9" fontWeight="bold" fill="#1e3a8a">Tổng: {sTong}</text>

            {/* Dòng kết luận số học */}
            <text x="175" y="112" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#1e40af">
              Số bé = ({sTong} - {sHieu}) : 2 = {soBe}  |  Số lớn = ({sTong} + {sHieu}) : 2 = {soLon}
            </text>
            <text x="175" y="132" textAnchor="middle" fontSize="8.5" fill="#475569">
              Thử lại: {soBe} + {soLon} = {sTong} (Tổng)  •  {soLon} - {soBe} = {sHieu} (Hiệu)
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#1e40af', background: '#eff6ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            📊 <b>Logic Sơ Đồ Đoạn Thẳng Lớp 5:</b> Bớt phần hiệu {sHieu} ở số lớn thì hai đoạn thẳng bằng nhau (bằng 2 lần số bé). Vậy: <b>Số bé = ({sTong} - {sHieu}) : 2 = {soBe}</b>; <b>Số lớn = {soBe} + {sHieu} = {soLon}</b>.
          </div>
        </div>
      );
    }

    if (fId.includes('tong-va-ti-so') || fId.includes('tong-ti') || (topic.includes('tổng') && topic.includes('tỉ'))) {
      const sTong = getVal(['s', 'tong', 's_tong'], 45);
      const pBe = Math.max(1, Math.round(getVal(['m', 'p_be', 'be'], 2)));
      const pLon = Math.max(pBe + 1, Math.round(getVal(['n', 'p_lon', 'lon'], 3)));
      const tongPhan = pBe + pLon;
      const motPhan = Number((sTong / tongPhan).toFixed(1));
      const soBe = Number((motPhan * pBe).toFixed(1));
      const soLon = Number((motPhan * pLon).toFixed(1));
      const unitW = Math.min(35, Math.max(15, 180 / tongPhan));

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 145" style={{ width: '100%', height: '135px' }}>
            <rect x="0" y="0" width="350" height="145" fill="#f0fdf4" rx="4" />

            {/* Số bé */}
            <text x="18" y="38" fontSize="9.5" fontWeight="bold" fill="#166534">Số bé ({pBe}p):</text>
            {Array.from({ length: pBe }).map((_, i) => (
              <g key={`be-${i}`}>
                <rect x={78 + i * unitW} y="24" width={unitW - 2} height="18" fill="#22c55e" rx="2" />
                <text x={78 + i * unitW + (unitW - 2) / 2} y="36" textAnchor="middle" fontSize="7.5" fill="#ffffff" fontWeight="bold">{motPhan}</text>
              </g>
            ))}

            {/* Số lớn */}
            <text x="18" y="74" fontSize="9.5" fontWeight="bold" fill="#166534">Số lớn ({pLon}p):</text>
            {Array.from({ length: pLon }).map((_, i) => (
              <g key={`lon-${i}`}>
                <rect x={78 + i * unitW} y="60" width={unitW - 2} height="18" fill="#15803d" rx="2" />
                <text x={78 + i * unitW + (unitW - 2) / 2} y="72" textAnchor="middle" fontSize="7.5" fill="#ffffff" fontWeight="bold">{motPhan}</text>
              </g>
            ))}

            {/* Ngoặc tổng hai số */}
            <path
              d={`M ${78 + pLon * unitW + 8} 24 Q ${78 + pLon * unitW + 18} 51, ${78 + pLon * unitW + 8} 78`}
              fill="none"
              stroke="#14532d"
              strokeWidth="1.5"
            />
            <text x={78 + pLon * unitW + 24} y="54" fontSize="9" fontWeight="bold" fill="#14532d">Tổng: {sTong}</text>

            <text x="175" y="112" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#166534">
              Tổng số phần = {pBe} + {pLon} = {tongPhan} phần  |  1 phần = {sTong} : {tongPhan} = {motPhan}
            </text>
            <text x="175" y="132" textAnchor="middle" fontSize="8.5" fill="#334155">
              Số bé = {motPhan} × {pBe} = {soBe}  •  Số lớn = {motPhan} × {pLon} = {soLon}
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#166534', background: '#f0fdf4', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            🌱 <b>Logic Tổng – Tỉ Lớp 5:</b> Coi số bé gồm {pBe} phần bằng nhau, số lớn gồm {pLon} phần như thế. Tổng số phần bằng nhau là {pBe} + {pLon} = {tongPhan} phần. Giá trị một phần là {sTong} : {tongPhan} = <b>{motPhan}</b>. <b>Số bé = {soBe}</b>, <b>Số lớn = {soLon}</b>.
          </div>
        </div>
      );
    }

    // 0.12 Sơ đồ đoạn thẳng cho bài toán Hiệu - Tỉ số (Chuẩn SGK Toán 5: Hiệu 12, tỉ số 1/3)
    if (fId.includes('hieu-va-ti-so') || fId.includes('hieu-ti') || (topic.includes('hiệu') && topic.includes('tỉ'))) {
      const sHieu = getVal(['h', 'hieu', 's_hieu'], 12);
      const pBe = Math.max(1, Math.round(getVal(['m', 'p_be', 'be'], 1)));
      const pLon = Math.max(pBe + 1, Math.round(getVal(['n', 'p_lon', 'lon'], 3)));
      const hieuPhan = pLon - pBe;
      const motPhan = Number((sHieu / hieuPhan).toFixed(1));
      const soBe = Number((motPhan * pBe).toFixed(1));
      const soLon = Number((motPhan * pLon).toFixed(1));
      const unitW = Math.min(38, Math.max(16, 180 / pLon));

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 145" style={{ width: '100%', height: '135px' }}>
            <rect x="0" y="0" width="350" height="145" fill="#fff7ed" rx="4" />

            {/* Số bé */}
            <text x="18" y="38" fontSize="9.5" fontWeight="bold" fill="#c2410c">Số bé ({pBe}p):</text>
            {Array.from({ length: pBe }).map((_, i) => (
              <g key={`be-${i}`}>
                <rect x={78 + i * unitW} y="24" width={unitW - 2} height="18" fill="#f97316" rx="2" />
                <text x={78 + i * unitW + (unitW - 2) / 2} y="36" textAnchor="middle" fontSize="7.5" fill="#ffffff" fontWeight="bold">{motPhan}</text>
              </g>
            ))}

            {/* Đường nét đứt gióng xuống từ số bé */}
            <line x1={78 + pBe * unitW - 2} y1="42" x2={78 + pBe * unitW - 2} y2="60" stroke="#ea580c" strokeDasharray="2 2" strokeWidth="1" />

            {/* Số lớn */}
            <text x="18" y="74" fontSize="9.5" fontWeight="bold" fill="#c2410c">Số lớn ({pLon}p):</text>
            {Array.from({ length: pLon }).map((_, i) => {
              const isDiff = i >= pBe;
              return (
                <g key={`lon-${i}`}>
                  <rect
                    x={78 + i * unitW}
                    y="60"
                    width={unitW - 2}
                    height="18"
                    fill={isDiff ? '#fed7aa' : '#ea580c'}
                    stroke={isDiff ? '#c2410c' : 'none'}
                    strokeDasharray={isDiff ? '2 2' : 'none'}
                    rx="2"
                  />
                  <text x={78 + i * unitW + (unitW - 2) / 2} y="72" textAnchor="middle" fontSize="7.5" fill={isDiff ? '#9a3412' : '#ffffff'} fontWeight="bold">{motPhan}</text>
                </g>
              );
            })}

            {/* Nhãn hiệu số phần */}
            <line x1={78 + pBe * unitW} y1="84" x2={78 + pLon * unitW - 2} y2="84" stroke="#c2410c" strokeWidth="1.2" />
            <text x={78 + ((pBe + pLon) / 2) * unitW} y="96" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#9a3412">
              Hiệu: {sHieu} ({hieuPhan} phần)
            </text>

            <text x="175" y="118" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#c2410c">
              Hiệu số phần = {pLon} - {pBe} = {hieuPhan} phần  |  1 phần = {sHieu} : {hieuPhan} = {motPhan}
            </text>
            <text x="175" y="136" textAnchor="middle" fontSize="8.5" fill="#475569">
              Số bé = {motPhan} × {pBe} = {soBe}  •  Số lớn = {motPhan} × {pLon} = {soLon}
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#9a3412', background: '#fff7ed', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            🔥 <b>Logic Hiệu – Tỉ Lớp 5:</b> Số lớn nhiều hơn số bé {hieuPhan} phần, ứng với hiệu là {sHieu}. Giá trị một phần là {sHieu} : {hieuPhan} = <b>{motPhan}</b>. Vậy: <b>Số bé = {soBe}</b>; <b>Số lớn = {soLon}</b>.
          </div>
        </div>
      );
    }

    // 0.13 Băng giấy phân số & Tỉ số (Fraction Strip Model)
    if (fId.includes('ti-so') || fId.includes('phan-so') || topic.includes('phân số') || topic.includes('tỉ số')) {
      const valA = Math.max(1, Math.round(getVal(['a'], 3)));
      const valB = Math.max(valA, Math.round(getVal(['b'], 5)));
      const pct = Number(((valA / valB) * 100).toFixed(1));
      const stripW = 240;
      const cellW = stripW / valB;

      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <svg viewBox="0 0 350 145" style={{ width: '100%', height: '135px' }}>
            <rect x="0" y="0" width="350" height="145" fill="#faf5ff" rx="4" />

            <text x="175" y="24" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#6b21a8">
              Mô hình Băng Giấy Phân Số: {valA}/{valB}
            </text>

            {/* Băng giấy chia thành valB phần */}
            <g transform="translate(55, 38)">
              {Array.from({ length: valB }).map((_, i) => {
                const isColored = i < valA;
                return (
                  <g key={i}>
                    <rect
                      x={i * cellW}
                      y="0"
                      width={cellW}
                      height="38"
                      fill={isColored ? '#a855f7' : '#f3e8ff'}
                      stroke="#7e22ce"
                      strokeWidth="1.5"
                    />
                    <text
                      x={i * cellW + cellW / 2}
                      y="23"
                      textAnchor="middle"
                      fontSize="9"
                      fontWeight="bold"
                      fill={isColored ? '#ffffff' : '#9333ea'}
                    >
                      1/{valB}
                    </text>
                  </g>
                );
              })}
            </g>

            {/* Ngoặc phần đã tô màu */}
            <line x1="55" y1="84" x2={55 + valA * cellW} y2="84" stroke="#7e22ce" strokeWidth="2" />
            <line x1="55" y1="81" x2="55" y2="87" stroke="#7e22ce" strokeWidth="2" />
            <line x1={55 + valA * cellW} y1="81" x2={55 + valA * cellW} y2="87" stroke="#7e22ce" strokeWidth="2" />
            <text x={55 + (valA * cellW) / 2} y="98" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#7e22ce">
              Đã lấy {valA} phần ({valA}/{valB} = {pct}%)
            </text>

            <text x="175" y="128" textAnchor="middle" fontSize="9.5" fontWeight="bold" fill="#581c87">
              Băng giấy chia đều {valB} phần bằng nhau, tô màu {valA} phần $\rightarrow$ Biểu diễn phân số {valA}/{valB}
            </text>
          </svg>
          <div style={{ fontSize: '0.78rem', color: '#6b21a8', background: '#faf5ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
            🎨 <b>Trực quan Phân số:</b> Mẫu số ({valB}) cho biết dải băng được chia thành bao nhiêu phần bằng nhau. Tử số ({valA}) cho biết ta đã lấy (hoặc tô màu) bao nhiêu phần trong số đó.
          </div>
        </div>
      );
    }

    // 0.11 Tìm X & Bốn phép tính (Chiếc cân thăng bằng)
    const valA = getVal(['a', 'tong'], 15);
    const valB = getVal(['b', 'hieu'], 7);
    const valX = valA - valB;

    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        <svg viewBox="0 0 350 135" style={{ width: '100%', height: '125px' }}>
          <rect x="0" y="0" width="350" height="135" fill="#fffbeb" rx="4" />
          <line x1="80" y1="50" x2="260" y2="50" stroke="#78350f" strokeWidth="3" />
          <polygon points="170,50 160,95 180,95" fill="#b45309" />
          <circle cx="170" cy="50" r="4" fill="#f59e0b" />

          <line x1="100" y1="50" x2="80" y2="75" stroke="#92400e" strokeWidth="1" />
          <line x1="100" y1="50" x2="120" y2="75" stroke="#92400e" strokeWidth="1" />
          <line x1="70" y1="75" x2="130" y2="75" stroke="#92400e" strokeWidth="2" />
          <rect x="75" y="58" width="18" height="16" rx="2" fill="#3b82f6" />
          <text x="84" y="70" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#ffffff">x</text>
          <rect x="98" y="60" width="16" height="14" rx="2" fill="#d97706" />
          <text x="106" y="71" textAnchor="middle" fontSize="8" fontWeight="bold" fill="#ffffff">{valB}</text>

          <text x="170" y="42" textAnchor="middle" fontSize="14" fontWeight="bold" fill="#b45309">=</text>

          <line x1="240" y1="50" x2="220" y2="75" stroke="#92400e" strokeWidth="1" />
          <line x1="240" y1="50" x2="260" y2="75" stroke="#92400e" strokeWidth="1" />
          <line x1="210" y1="75" x2="270" y2="75" stroke="#92400e" strokeWidth="2" />
          <rect x="230" y="56" width="22" height="18" rx="2" fill="#10b981" />
          <text x="241" y="69" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#ffffff">{valA}</text>

          <text x="170" y="118" textAnchor="middle" fontSize="9.5" fontWeight="bold" fill="#78350f">
            Cân thăng bằng: x + {valB} = {valA}  →  x = {valA} - {valB} = {valX}
          </text>
        </svg>
        <div style={{ fontSize: '0.78rem', color: '#78350f', background: '#fffbeb', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
          ⚖️ <b>Logic Lớp 5:</b> Hai đĩa cân thăng bằng giống như dấu '='. Muốn tìm chiếc hộp bí ẩn x, ta chỉ cần nhấc bớt quả cân {valB} ra khỏi cả hai đĩa cân: x = {valA} - {valB} = <b>{valX}</b>.
        </div>
      </div>
    );
  };

  /**
   * Render mô hình đồ họa tương tác logic & đúng lứa tuổi:
   * - Tiểu học / Lớp 5: Chuyển động xe cộ, cắt ghép tam giác, hình thang, Lego xếp khối thể tích
   * - Vật lý cơ học: Vật kéo, vector lực, lò xo, con lắc
   * - Vật lý điện: Mạch điện nguồn + điện trở + bóng đèn phát sáng
   * - Hóa học: Bình thí nghiệm đổi màu pH hoặc nồng độ hạt
   * - Sinh học: Chuỗi xoắn kép ADN, phân bào 2^k, khung Punnett
   * - Toán học (THPT/ĐH): Đồ thị hàm số trên hệ tọa độ Descartes Oxy
   */
  const renderLogicalSimulation = () => {
    // Ưu tiên số 1: Nếu là lứa tuổi Tiểu học hoặc Lớp 5, hiển thị mô hình trực quan thuần túy Lớp 5
    if (isElementary) {
      return renderElementarySimulation();
    }
    // =========================================================================
    // 1. VẬT LÝ (PHYSICS) - MÔ HÌNH THỰC NGHIỆM ĐÚNG LỨA TUỔI
    // =========================================================================
    if (subj === 'physics') {
      // 1.1 Dao động điều hòa & Con lắc (THPT Lớp 11-12 & ĐH)
      if (
        topic.includes('dao động') ||
        topic.includes('con lắc') ||
        topic.includes('lò xo') ||
        fId.includes('dao-dong') ||
        fId.includes('con-lac') ||
        fId.includes('shm') ||
        fId.includes('harmonic')
      ) {
        const length = Math.min(110, Math.max(50, 50 + v1 * 4));
        const thetaDeg = Math.min(35, Math.max(-35, (v2 - 5) * 5));
        const thetaRad = (thetaDeg * Math.PI) / 180;
        const bobX = 80 + length * Math.sin(thetaRad);
        const bobY = 20 + length * Math.cos(thetaRad);
        const period_T = (2 * Math.PI * Math.sqrt(Math.max(0.1, v1) / 9.8)).toFixed(2);

        return (
          <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
            {/* Giá đỡ con lắc */}
            <line x1="40" y1="20" x2="120" y2="20" stroke="#475569" strokeWidth="3" />
            <line x1="80" y1="20" x2="80" y2="135" stroke="#cbd5e1" strokeWidth="1" strokeDasharray="3 3" />

            {/* Dây treo & Quả nặng con lắc */}
            <line x1="80" y1="20" x2={bobX} y2={bobY} stroke="#0284c7" strokeWidth="2" />
            <circle cx={bobX} cy={bobY} r="9" fill="#0284c7" stroke="#0369a1" strokeWidth="2" />
            <text x={bobX + 12} y={bobY + 4} fontSize="9" fontWeight="bold" fill="#0369a1">m</text>

            {/* Cung góc lệch alpha */}
            <path
              d={`M 80 50 A 30 30 0 0 ${thetaDeg >= 0 ? 1 : 0} ${80 + 30 * Math.sin(thetaRad)} ${20 + 30 * Math.cos(thetaRad)}`}
              fill="none"
              stroke="#d97706"
              strokeWidth="1.5"
            />
            <text x="92" y="46" fontSize="9" fontWeight="bold" fill="#d97706">α = {thetaDeg}°</text>

            {/* Đồ thị li độ - thời gian x(t) = A cos(omega t) bên phải */}
            <g transform="translate(180, 20)">
              <line x1="0" y1="50" x2="140" y2="50" stroke="#94a3b8" strokeWidth="1.5" />
              <line x1="0" y1="10" x2="0" y2="90" stroke="#94a3b8" strokeWidth="1.5" />
              <polygon points="140,50 134,47 134,53" fill="#94a3b8" />
              <polygon points="0,10 -3,16 3,16" fill="#94a3b8" />
              <text x="135" y="62" fontSize="9" fill="#64748b">t</text>
              <text x="6" y="16" fontSize="9" fill="#64748b">x</text>

              {/* Đường cong hình sin điều hòa */}
              <path
                d="M 0 50 Q 25 15, 50 50 T 100 50 T 135 50"
                fill="none"
                stroke="#2563eb"
                strokeWidth="2"
              />
              <circle cx="50" cy="50" r="3" fill="#ef4444" />
              <text x="2" y="105" fontSize="10" fontWeight="bold" fill="#0f172a">
                T = 2π√(l/g) ≈ {period_T} s
              </text>
            </g>
          </svg>
        );
      }

      // 1.2 Quang học & Thấu kính / Khúc xạ (THCS Lớp 9 & THPT Lớp 11)
      if (
        topic.includes('quang') ||
        topic.includes('khúc xạ') ||
        topic.includes('thấu kính') ||
        fId.includes('quang') ||
        fId.includes('thau-kinh') ||
        fId.includes('khuc-xa') ||
        fId.includes('lens') ||
        fId.includes('optic')
      ) {
        const objDist = Math.min(100, Math.max(40, v1 * 8));
        const focal = 45;
        // Công thức thấu kính 1/f = 1/d + 1/d' => d' = d*f / (d - f)
        const imgDist = (objDist * focal) / Math.max(1, objDist - focal);
        const clampedImgDist = Math.min(120, Math.max(20, imgDist));

        return (
          <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
            {/* Trục chính quang học */}
            <line x1="10" y1="70" x2="330" y2="70" stroke="#64748b" strokeWidth="1.5" />
            <polygon points="330,70 324,67 324,73" fill="#64748b" />

            {/* Thấu kính hội tụ tại x = 160 */}
            <line x1="160" y1="20" x2="160" y2="120" stroke="#0284c7" strokeWidth="2.5" />
            <polygon points="160,18 156,26 164,26" fill="#0284c7" />
            <polygon points="160,122 156,114 164,114" fill="#0284c7" />
            <text x="164" y="32" fontSize="9" fontWeight="bold" fill="#0284c7">Thấu kính (f)</text>

            {/* Tiêu điểm F và F' */}
            <circle cx="115" cy="70" r="2.5" fill="#d97706" />
            <text x="113" y="84" fontSize="9" fontWeight="bold" fill="#d97706">F</text>
            <circle cx="205" cy="70" r="2.5" fill="#d97706" />
            <text x="203" y="84" fontSize="9" fontWeight="bold" fill="#d97706">F'</text>

            {/* Vật sáng AB tại x = 160 - objDist */}
            <line x1={160 - objDist} y1="70" x2={160 - objDist} y2="35" stroke="#dc2626" strokeWidth="2.5" />
            <polygon points={`${160 - objDist},33 ${157 - objDist},40 ${163 - objDist},40`} fill="#dc2626" />
            <text x={152 - objDist} y="32" fontSize="9" fontWeight="bold" fill="#dc2626">B</text>
            <text x={155 - objDist} y="84" fontSize="9" fill="#dc2626">A</text>

            {/* Tia 1: Song song trục chính qua F' */}
            <line x1={160 - objDist} y1="35" x2="160" y2="35" stroke="#16a34a" strokeWidth="1.5" />
            <line x1="160" y1="35" x2={160 + clampedImgDist} y2={70 + (35 * clampedImgDist) / objDist} stroke="#16a34a" strokeWidth="1.5" />

            {/* Tia 2: Qua quang tâm O đi thẳng */}
            <line x1={160 - objDist} y1="35" x2={160 + clampedImgDist} y2={70 + (35 * clampedImgDist) / objDist} stroke="#2563eb" strokeWidth="1.5" />

            {/* Ảnh thật A'B' ngược chiều */}
            <line x1={160 + clampedImgDist} y1="70" x2={160 + clampedImgDist} y2={70 + (35 * clampedImgDist) / objDist} stroke="#7c3aed" strokeWidth="2.5" />
            <text x={164 + clampedImgDist} y={75 + (35 * clampedImgDist) / objDist} fontSize="9" fontWeight="bold" fill="#7c3aed">B' (ảnh)</text>

            <text x="20" y="138" fontSize="10" fontWeight="bold" fill="#0369a1">
              Định luật thấu kính: 1/f = 1/d + 1/d'  (d = {v1} cm, d' ≈ {imgDist.toFixed(1)} cm)
            </text>
          </svg>
        );
      }

      // 1.3 Khí lý tưởng & Nhiệt động lực học (THPT Lớp 12 & ĐH)
      if (
        topic.includes('khí') ||
        topic.includes('nhiệt') ||
        fId.includes('khi') ||
        fId.includes('nhiet') ||
        fId.includes('carnot') ||
        fId.includes('p-v')
      ) {
        const volumeHeight = Math.min(80, Math.max(25, 20 + v1 * 4));
        const pressureVal = (100 / Math.max(1, v1)).toFixed(1);

        return (
          <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
            {/* Xylanh khí */}
            <rect x="30" y="25" width="80" height="90" fill="#f8fafc" stroke="#475569" strokeWidth="2" rx="2" />
            {/* Khí bên trong xylanh */}
            <rect x="32" y={115 - volumeHeight} width="76" height={volumeHeight - 2} fill="#bae6fd" opacity="0.6" />

            {/* Pít-tông di động */}
            <rect x="28" y={110 - volumeHeight} width="84" height="8" fill="#334155" rx="2" />
            <line x1="70" y1={110 - volumeHeight} x2="70" y2="15" stroke="#334155" strokeWidth="4" />

            <text x="70" y="132" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#0369a1">
              Thể tích V = {v1} L
            </text>

            {/* Đồng hồ đo áp suất P */}
            <circle cx="145" cy="55" r="22" fill="#ffffff" stroke="#0f172a" strokeWidth="2" />
            <line x1="145" y1="55" x2={145 + Math.cos(Number(pressureVal) * 0.5) * 16} y2={55 - Math.sin(Number(pressureVal) * 0.5) * 16} stroke="#dc2626" strokeWidth="2" />
            <circle cx="145" cy="55" r="3" fill="#dc2626" />
            <text x="145" y="90" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#dc2626">
              P = {pressureVal} atm
            </text>

            {/* Đồ thị P-V đẳng nhiệt bên phải */}
            <g transform="translate(200, 20)">
              <line x1="0" y1="85" x2="120" y2="85" stroke="#94a3b8" strokeWidth="1.5" />
              <line x1="0" y1="0" x2="0" y2="85" stroke="#94a3b8" strokeWidth="1.5" />
              <text x="115" y="97" fontSize="9" fill="#64748b">V</text>
              <text x="5" y="10" fontSize="9" fill="#64748b">P</text>

              {/* Đường hypebol đẳng nhiệt P = const / V */}
              <path d="M 15 15 Q 30 50, 105 78" fill="none" stroke="#2563eb" strokeWidth="2" />
              <circle cx={Math.min(100, Math.max(15, v1 * 4))} cy={Math.min(78, Math.max(15, 100 / Math.max(1, v1)))} r="4" fill="#ef4444" />
              <text x="10" y="112" fontSize="9.5" fontWeight="bold" fill="#0f172a">
                Định luật Boyle: P · V = const
              </text>
            </g>
          </svg>
        );
      }

      // 1.4 Điện học: Mạch điện nguồn + điện trở + bóng đèn (THCS Lớp 9 & THPT)
      if (
        topic.includes('điện') ||
        fId.includes('dien') ||
        fId.includes('om') ||
        fId.includes('mach')
      ) {
        const current_I = calculatedOutput !== null ? Math.max(0.1, Math.min(10, calculatedOutput)) : v1 / Math.max(0.1, v2);
        const bulbOpacity = Math.min(1, Math.max(0.2, current_I / 4));
        const bulbGlow = Math.min(25, current_I * 4);

        return (
          <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
            <rect x="30" y="20" width="280" height="95" fill="none" stroke="#0284c7" strokeWidth="2.5" rx="10" />

            {/* Nguồn điện một chiều (Pin) */}
            <g transform="translate(30, 67)">
              <rect x="-10" y="-18" width="20" height="36" fill="#f8fafc" stroke="none" />
              <line x1="-12" y1="0" x2="-2" y2="0" stroke="#0284c7" strokeWidth="2.5" />
              <line x1="-2" y1="-14" x2="-2" y2="14" stroke="#0f172a" strokeWidth="3" />
              <line x1="6" y1="-8" x2="6" y2="8" stroke="#0f172a" strokeWidth="2" />
              <line x1="6" y1="0" x2="16" y2="0" stroke="#0284c7" strokeWidth="2.5" />
              <text x="-8" y="-18" fontSize="10" fontWeight="bold" fill="#0284c7">+</text>
              <text x="10" y="-18" fontSize="10" fontWeight="bold" fill="#64748b">-</text>
              <text x="-15" y="30" fontSize="10" fill="#0369a1" fontWeight="bold">Nguồn U = {v1}V</text>
            </g>

            {/* Điện trở R */}
            <g transform="translate(170, 20)">
              <rect x="-32" y="-10" width="64" height="20" fill="#ffffff" stroke="#0f172a" strokeWidth="2" rx="2" />
              <text x="0" y="4" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#0f172a">
                R = {v2} Ω
              </text>
            </g>

            {/* Bóng đèn phát sáng */}
            <g transform="translate(170, 115)">
              <circle cx="0" cy="0" r="14" fill={`rgba(245, 158, 11, ${bulbOpacity})`} stroke="#d97706" strokeWidth="2" />
              <circle cx="0" cy="0" r={14 + bulbGlow / 2} fill={`rgba(253, 224, 71, ${bulbOpacity * 0.4})`} />
              <text x="0" y="4" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#78350f">💡</text>
              <text x="0" y="24" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#b45309">
                I = {Number(current_I.toFixed(2))} A
              </text>
            </g>
          </svg>
        );
      }

      // 1.5 Cơ học: Lực kéo, mặt phẳng, trọng lực, công (THCS & THPT)
      const forceMag = Math.min(80, Math.max(15, v1 * 2));
      const distPercent = Math.min(180, Math.max(20, v2 * 8));

      return (
        <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
          <line x1="20" y1="95" x2="320" y2="95" stroke="#64748b" strokeWidth="2" />
          {Array.from({ length: 16 }).map((_, i) => (
            <line key={i} x1={30 + i * 18} y1="95" x2={22 + i * 18} y2="103" stroke="#cbd5e1" strokeWidth="1" />
          ))}

          {/* Khối vật m */}
          <g transform={`translate(${40 + distPercent * 0.5}, 55)`}>
            <rect x="0" y="0" width="50" height="40" fill="#e0f2fe" stroke="#0284c7" strokeWidth="2" rx="3" />
            <text x="25" y="24" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#0369a1">m</text>

            {/* Vector Lực kéo F */}
            <line x1="50" y1="20" x2={50 + forceMag} y2="20" stroke="#dc2626" strokeWidth="3" />
            <polygon points={`${50 + forceMag},16 ${50 + forceMag + 8},20 ${50 + forceMag},24`} fill="#dc2626" />
            <text x={55 + forceMag} y="15" fontSize="11" fontWeight="bold" fill="#dc2626">F = {v1} N</text>

            {/* Trọng lực P và Phản lực N */}
            <line x1="25" y1="40" x2="25" y2="65" stroke="#475569" strokeWidth="1.5" />
            <polygon points="22,65 25,70 28,65" fill="#475569" />
            <text x="30" y="65" fontSize="9" fill="#475569">P</text>

            <line x1="25" y1="0" x2="25" y2="-20" stroke="#475569" strokeWidth="1.5" />
            <polygon points="22,-20 25,-25 28,-20" fill="#475569" />
            <text x="30" y="-15" fontSize="9" fill="#475569">N</text>
          </g>

          {/* Thước đo quãng đường s */}
          <line x1="40" y1="114" x2={90 + distPercent * 0.5} y2="114" stroke="#059669" strokeWidth="1.5" strokeDasharray="3 2" />
          <line x1="40" y1="110" x2="40" y2="118" stroke="#059669" strokeWidth="2" />
          <line x1={90 + distPercent * 0.5} y1="110" x2={90 + distPercent * 0.5} y2="118" stroke="#059669" strokeWidth="2" />
          <text x={(130 + distPercent * 0.5) / 2} y="128" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#047857">
            Quãng đường s = {v2} m  (Công A = F · s = {Number((v1 * v2).toFixed(1))} J)
          </text>
        </svg>
      );
    }

    // =========================================================================
    // 2. TOÁN HỌC (MATHEMATICS) - HÌNH HỌC, LƯỢNG GIÁC, ĐẠO HÀM, TÍCH PHÂN
    // =========================================================================
    if (subj === 'math') {
      if (isHighSchoolMath) {
        // 2.10 Lượng giác & Vòng tròn đơn vị (THPT Lớp 10-11)
        if (
          topic.includes('lượng giác') ||
          topic.includes('sin') ||
          topic.includes('cos') ||
          topic.includes('tan') ||
          fId.includes('luong-giac') ||
          fId.includes('trigonometry') ||
          fId.includes('sin') ||
          fId.includes('cos') ||
          fId.includes('tan')
        ) {
          const deg = Math.min(360, Math.max(0, getVal(['alpha', 'a'], 45)));
          const rad = (deg * Math.PI) / 180;
          const rPx = 46;
          const oX = 170, oY = 70;
          const ptX = oX + rPx * Math.cos(rad);
          const ptY = oY - rPx * Math.sin(rad);
  
          const sinVal = Math.sin(rad);
          const cosVal = Math.cos(rad);
          const tanVal = Math.abs(cosVal) > 0.001 ? sinVal / cosVal : null;
  
          // Trục tan tiếp xúc tại x = oX + rPx
          const tanPxY = tanVal !== null ? Math.min(135, Math.max(8, oY - rPx * tanVal)) : null;
  
          return (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
                <rect x="0" y="0" width="340" height="145" fill="#f8fafc" rx="4" />
  
                {/* Hệ trục tọa độ cos (ngang) và sin (dọc) */}
                <line x1="85" y1={oY} x2="255" y2={oY} stroke="#94a3b8" strokeWidth="1.5" />
                <line x1={oX} y1="125" x2={oX} y2="15" stroke="#94a3b8" strokeWidth="1.5" />
                <polygon points="255,70 248,67 248,73" fill="#94a3b8" />
                <polygon points="170,15 167,22 173,22" fill="#94a3b8" />
                <text x="250" y="62" fontSize="9" fontWeight="bold" fill="#64748b">cos</text>
                <text x="176" y="24" fontSize="9" fontWeight="bold" fill="#64748b">sin</text>
                <text x="162" y="82" fontSize="8" fill="#94a3b8">O</text>
  
                {/* Vòng tròn đơn vị R = 1 */}
                <circle cx={oX} cy={oY} r={rPx} fill="none" stroke="#0284c7" strokeWidth="2" strokeDasharray="3 2" />
  
                {/* Trục tan thẳng đứng tại x = 1 */}
                <line x1={oX + rPx} y1="12" x2={oX + rPx} y2="128" stroke="#d97706" strokeWidth="1.2" strokeDasharray="2 2" />
                <text x={oX + rPx + 4} y="22" fontSize="8" fontWeight="bold" fill="#d97706">tan</text>
  
                {/* Cung góc alpha */}
                <path
                  d={`M ${oX + 16} ${oY} A 16 16 0 ${deg > 180 ? 1 : 0} 0 ${oX + 16 * Math.cos(rad)} ${oY - 16 * Math.sin(rad)}`}
                  fill="none"
                  stroke="#dc2626"
                  strokeWidth="1.5"
                />
  
                {/* Bán kính OM nối tâm đến điểm M trên đường tròn */}
                <line x1={oX} y1={oY} x2={ptX} y2={ptY} stroke="#dc2626" strokeWidth="2" />
                <circle cx={ptX} cy={ptY} r="3.5" fill="#dc2626" />
                <text x={ptX + (cosVal >= 0 ? 5 : -14)} y={ptY + (sinVal >= 0 ? -4 : 10)} fontSize="8.5" fontWeight="bold" fill="#dc2626">M</text>
  
                {/* Tia OM cắt trục tan nếu hợp lý */}
                {tanPxY !== null && Math.cos(rad) > 0.05 && (
                  <>
                    <line x1={ptX} y1={ptY} x2={oX + rPx} y2={tanPxY} stroke="#ea580c" strokeWidth="1.2" strokeDasharray="2 2" />
                    <circle cx={oX + rPx} cy={tanPxY} r="3" fill="#ea580c" />
                  </>
                )}
  
                {/* Hình chiếu cos (trục hoành) & sin (trục tung) */}
                <line x1={ptX} y1={ptY} x2={ptX} y2={oY} stroke="#16a34a" strokeWidth="1.5" strokeDasharray="2 2" />
                <line x1={ptX} y1={ptY} x2={oX} y2={ptY} stroke="#2563eb" strokeWidth="1.5" strokeDasharray="2 2" />
                <circle cx={ptX} cy={oY} r="2.5" fill="#16a34a" />
                <circle cx={oX} cy={ptY} r="2.5" fill="#2563eb" />
  
                {/* Bảng giá trị bên góc trái */}
                <g transform="translate(10, 20)">
                  <rect x="0" y="0" width="70" height="66" fill="#ffffff" stroke="#e2e8f0" rx="3" />
                  <text x="6" y="14" fontSize="8.5" fontWeight="bold" fill="#dc2626">α = {deg}°</text>
                  <text x="6" y="28" fontSize="8" fontWeight="bold" fill="#16a34a">cos = {cosVal.toFixed(2)}</text>
                  <text x="6" y="42" fontSize="8" fontWeight="bold" fill="#2563eb">sin = {sinVal.toFixed(2)}</text>
                  <text x="6" y="56" fontSize="8" fontWeight="bold" fill="#d97706">tan = {tanVal !== null ? tanVal.toFixed(2) : '∞'}</text>
                </g>
  
                <text x="170" y="138" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0f172a">
                  sin²α + cos²α = ({sinVal.toFixed(2)})² + ({cosVal.toFixed(2)})² = {(sinVal * sinVal + cosVal * cosVal).toFixed(2)} = 1
                </text>
              </svg>
              <div style={{ fontSize: '0.78rem', color: '#1e40af', background: '#eff6ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
                📐 <b>Đường Tròn Lượng Giác Đơn Vị Lớp 10-11:</b> Mỗi góc <i>α</i> tương ứng một điểm <i>M</i> trên đường tròn đơn vị (bán kính R = 1): <b>Hoành độ là cos α</b>, <b>Tung độ là sin α</b>, và <b>tan α = sin α / cos α</b>.
              </div>
            </div>
          );
        }
  
        // 2.11 Ý nghĩa hình học của Đạo hàm & Tiếp tuyến đồ thị (THPT Lớp 11-12)
        if (
          topic.includes('đạo hàm') ||
          topic.includes('tiếp tuyến') ||
          fId.includes('dao-ham') ||
          fId.includes('derivative') ||
          fId.includes('tiep-tuyen')
        ) {
          const x0 = Math.min(2.0, Math.max(-2.0, getVal(['x0', 'x_0'], 1.0)));
          // Hàm số chuẩn f(x) = 0.25 x^3 - x
          const y0 = 0.25 * Math.pow(x0, 3) - x0;
          // Đạo hàm f'(x) = 0.75 x^2 - 1
          const slope = 0.75 * x0 * x0 - 1.0;
  
          const oX = 170, oY = 70;
          const scaleX = 38, scaleY = 32;
  
          const pts: string[] = [];
          for (let x = -2.6; x <= 2.6; x += 0.1) {
            const y = 0.25 * Math.pow(x, 3) - x;
            const px = oX + x * scaleX;
            const py = oY - y * scaleY;
            if (py >= 10 && py <= 135) {
              pts.push(`${px},${py}`);
            }
          }
  
          const mPx = oX + x0 * scaleX;
          const mPy = oY - y0 * scaleY;
  
          // Điểm trên tiếp tuyến tại x1 và x2
          const tLen = 1.6;
          const tx1 = x0 - tLen;
          const ty1 = y0 - slope * tLen;
          const tx2 = x0 + tLen;
          const ty2 = y0 + slope * tLen;
  
          return (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
                <rect x="0" y="0" width="340" height="145" fill="#f8fafc" rx="4" />
                <line x1="20" y1={oY} x2="320" y2={oY} stroke="#cbd5e1" strokeWidth="1.5" />
                <line x1={oX} y1="10" x2={oX} y2="135" stroke="#cbd5e1" strokeWidth="1.5" />
                <text x="315" y={oY + 12} fontSize="9" fill="#94a3b8">x</text>
                <text x={oX + 6} y="18" fontSize="9" fill="#94a3b8">y</text>
  
                {/* Đồ thị hàm bậc 3 f(x) = 1/4 x^3 - x */}
                {pts.length > 2 && (
                  <polyline points={pts.join(' ')} fill="none" stroke="#2563eb" strokeWidth="2.5" />
                )}
  
                {/* Đường tiếp tuyến tại x0 */}
                <line
                  x1={oX + tx1 * scaleX}
                  y1={oY - ty1 * scaleY}
                  x2={oX + tx2 * scaleX}
                  y2={oY - ty2 * scaleY}
                  stroke="#dc2626"
                  strokeWidth="2"
                />
  
                {/* Tiếp điểm M(x0, y0) */}
                <circle cx={mPx} cy={mPy} r="4" fill="#dc2626" />
                <text x={mPx + 6} y={mPy - 6} fontSize="8.5" fontWeight="bold" fill="#dc2626">
                  M({x0.toFixed(1)}, {y0.toFixed(1)})
                </text>
  
                <line x1={mPx} y1={mPy} x2={mPx} y2={oY} stroke="#dc2626" strokeWidth="1" strokeDasharray="2 2" />
  
                <text x="20" y="24" fontSize="8.5" fontWeight="bold" fill="#2563eb">y = ¼x³ − x</text>
                <text x="20" y="38" fontSize="8.5" fontWeight="bold" fill="#dc2626">k = f'(x₀) = {slope.toFixed(2)}</text>
                {Math.abs(slope) < 0.15 && (
                  <text x="20" y="52" fontSize="8" fontWeight="bold" fill="#16a34a">★ Điểm cực trị (k ≈ 0)</text>
                )}
  
                <text x="170" y="138" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0f172a">
                  Phương trình tiếp tuyến: y = {slope.toFixed(2)}(x − {x0.toFixed(1)}) + ({y0.toFixed(1)})  |  Hệ số góc k = {slope.toFixed(2)}
                </text>
              </svg>
              <div style={{ fontSize: '0.78rem', color: '#1e40af', background: '#eff6ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
                📈 <b>Ý Nghĩa Hình Học Của Đạo Hàm Lớp 11-12:</b> Đạo hàm <i>f'(x₀)</i> chính là <b>hệ số góc (độ dốc) k của tiếp tuyến</b> với đồ thị tại tiếp điểm <i>M(x₀, f(x₀))</i>. Khi tiếp tuyến nằm ngang (<i>k = 0</i>), đồ thị đạt cực trị!
              </div>
            </div>
          );
        }
  
        // 2.12 Tích phân & Tổng Riemann (THPT Lớp 12 & ĐH)
        if (
          topic.includes('tích phân') ||
          topic.includes('nguyên hàm') ||
          fId.includes('tich-phan') ||
          fId.includes('nguyen-ham') ||
          fId.includes('integral') ||
          fId.includes('riemann')
        ) {
          const strips = Math.min(24, Math.max(4, Math.round(getVal(['n'], 8))));
          const bVal = Math.min(4.5, Math.max(1.5, getVal(['b'], 3.0)));
          const oX = 50, oY = 110;
          const scaleX = 220 / 4.5;
          const scaleY = 12;
  
          const deltaX = bVal / strips;
          let sumArea = 0;
  
          const rects = [];
          for (let i = 0; i < strips; i++) {
            const xLeft = i * deltaX;
            const xMid = xLeft + deltaX / 2;
            const fMid = 0.35 * xMid * xMid + 0.8;
            sumArea += fMid * deltaX;
  
            const rPxX = oX + xLeft * scaleX;
            const rPxW = deltaX * scaleX;
            const rPxH = fMid * scaleY;
  
            rects.push(
              <rect
                key={i}
                x={rPxX}
                y={oY - rPxH}
                width={Math.max(1, rPxW - 0.8)}
                height={rPxH}
                fill="#bae6fd"
                stroke="#0284c7"
                strokeWidth="0.8"
                opacity="0.85"
              />
            );
          }
  
          const exactInt = (0.35 / 3) * Math.pow(bVal, 3) + 0.8 * bVal;
  
          // Đường cong hàm f(x) = 0.35 x^2 + 0.8
          const pts: string[] = [];
          for (let x = 0; x <= 4.5; x += 0.2) {
            const y = 0.35 * x * x + 0.8;
            pts.push(`${oX + x * scaleX},${oY - y * scaleY}`);
          }
  
          return (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
                <rect x="0" y="0" width="340" height="145" fill="#f0f9ff" rx="4" />
                <line x1="30" y1={oY} x2="315" y2={oY} stroke="#64748b" strokeWidth="1.5" />
                <line x1={oX} y1="15" x2={oX} y2="125" stroke="#64748b" strokeWidth="1.5" />
                <text x="310" y={oY + 12} fontSize="9" fill="#64748b">x</text>
                <text x={oX - 10} y="22" fontSize="9" fill="#64748b">y</text>
                <text x={oX - 10} y={oY + 10} fontSize="8" fill="#64748b">0</text>
  
                {/* Các hình chữ nhật Riemann */}
                {rects}
  
                {/* Đường cong f(x) */}
                <polyline points={pts.join(' ')} fill="none" stroke="#dc2626" strokeWidth="2.2" />
                <text x={oX + 3.8 * scaleX} y={oY - (0.35 * 3.8 * 3.8 + 0.8) * scaleY - 6} fontSize="8.5" fontWeight="bold" fill="#dc2626">
                  f(x) = 0.35x² + 0.8
                </text>
  
                {/* Vạch cận b */}
                <line x1={oX + bVal * scaleX} y1={oY - 5} x2={oX + bVal * scaleX} y2={oY + 5} stroke="#0f172a" strokeWidth="2" />
                <text x={oX + bVal * scaleX} y={oY + 14} textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0f172a">b = {bVal}</text>
  
                <text x="170" y="138" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0369a1">
                  Tổng Riemann S_{strips} = {sumArea.toFixed(2)}  |  Tích phân chuẩn ∫₀ᵇ f(x)dx = {exactInt.toFixed(2)}  (Sai số {Math.abs(sumArea - exactInt).toFixed(2)})
                </text>
              </svg>
              <div style={{ fontSize: '0.78rem', color: '#0369a1', background: '#e0f2fe', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
                ∫ <b>Bản Chất Tích Phân Riemann Lớp 12:</b> Diện tích hình phẳng được xấp xỉ bằng tổng diện tích các cột hình chữ nhật con. <b>Khi số dải n càng lớn, tổng Riemann càng tiệm cận chính xác diện tích tích phân</b>!
              </div>
            </div>
          );
        }
  
        // 2.13 Số phức & Mặt phẳng phức Gauss (THPT Lớp 12 & ĐH)
        if (
          topic.includes('số phức') ||
          fId.includes('so-phuc') ||
          fId.includes('complex')
        ) {
          const pA = Math.min(6, Math.max(-6, getVal(['a'], 3)));
          const pB = Math.min(6, Math.max(-6, getVal(['b'], 4)));
          const modZ = Math.sqrt(pA * pA + pB * pB);
  
          const oX = 170, oY = 70;
          const scale = 16;
          const mX = oX + pA * scale;
          const mY = oY - pB * scale;
          const conjY = oY + pB * scale;
  
          return (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
                <rect x="0" y="0" width="340" height="145" fill="#faf5ff" rx="4" />
  
                {/* Trục thực Re và Trục ảo Im */}
                <line x1="20" y1={oY} x2="320" y2={oY} stroke="#94a3b8" strokeWidth="1.5" />
                <line x1={oX} y1="10" x2={oX} y2="135" stroke="#94a3b8" strokeWidth="1.5" />
                <polygon points="320,70 312,66 312,74" fill="#94a3b8" />
                <polygon points="170,10 166,18 174,18" fill="#94a3b8" />
                <text x="310" y="62" fontSize="9" fontWeight="bold" fill="#64748b">Re (Thực)</text>
                <text x="176" y="20" fontSize="9" fontWeight="bold" fill="#64748b">Im (Ảo)</text>
                <text x="160" y="82" fontSize="8" fill="#94a3b8">O</text>
  
                {/* Vector OM biểu diễn số phức z */}
                <line x1={oX} y1={oY} x2={mX} y2={mY} stroke="#7c3aed" strokeWidth="2.2" />
                <circle cx={mX} cy={mY} r="4" fill="#7c3aed" />
                <text x={mX + 6} y={mY - 4} fontSize="9" fontWeight="bold" fill="#6d28d9">M(z = {pA} + {pB}i)</text>
  
                {/* Hình chiếu số phức */}
                <line x1={mX} y1={mY} x2={mX} y2={oY} stroke="#9333ea" strokeWidth="1.2" strokeDasharray="2 2" />
                <line x1={mX} y1={mY} x2={oX} y2={mY} stroke="#9333ea" strokeWidth="1.2" strokeDasharray="2 2" />
  
                {/* Số phức liên hợp z-ngang đối xứng qua trục thực */}
                <circle cx={mX} cy={conjY} r="3" fill="#a855f7" opacity="0.6" />
                <text x={mX + 6} y={conjY + 6} fontSize="8" fill="#9333ea">M'(z̄ = {pA} − {pB}i)</text>
                <line x1={mX} y1={mY} x2={mX} y2={conjY} stroke="#c084fc" strokeWidth="1" strokeDasharray="2 2" />
  
                <text x="170" y="138" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#581c87">
                  z = {pA} + {pB}i  |  Mô-đun |z| = √(a² + b²) = √({pA}² + {pB}²) = {modZ.toFixed(2)}  |  z̄ = {pA} − {pB}i
                </text>
              </svg>
              <div style={{ fontSize: '0.78rem', color: '#6b21a8', background: '#faf5ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
                ⚛️ <b>Mặt Phẳng Phức Gauss Lớp 12:</b> Mỗi số phức <i>z = a + bi</i> được biểu diễn bởi một điểm <i>M(a, b)</i> hoặc vector <i>OM</i>. <b>Mô-đun |z| chính là độ dài đoạn OM</b>, và số phức liên hợp <i>z̄</i> đối xứng qua trục thực!
              </div>
            </div>
          );
        }
  
        // 2.14 Vector & Tích vô hướng (THPT Lớp 10 & 12)
        if (
          topic.includes('vector') ||
          topic.includes('tích vô hướng') ||
          fId.includes('vector') ||
          fId.includes('tich-vo-huong') ||
          fId.includes('dot-product')
        ) {
          const lenU = Math.min(8, Math.max(1, getVal(['len_u'], 4)));
          const lenV = Math.min(8, Math.max(1, getVal(['len_v'], 5)));
          const thDeg = Math.min(180, Math.max(0, getVal(['theta'], 60)));
          const thRad = (thDeg * Math.PI) / 180;
          const dotProd = lenU * lenV * Math.cos(thRad);
  
          const oX = 130, oY = 95;
          const scale = 16;
          const uX = oX + lenU * scale, uY = oY;
          const vX = oX + lenV * scale * Math.cos(thRad);
          const vY = oY - lenV * scale * Math.sin(thRad);
  
          const isPerp = thDeg === 90;
  
          return (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
                <rect x="0" y="0" width="340" height="145" fill="#f8fafc" rx="4" />
  
                {/* Gốc vector O */}
                <circle cx={oX} cy={oY} r="3" fill="#0f172a" />
                <text x={oX - 10} y={oY + 12} fontSize="9" fontWeight="bold" fill="#0f172a">O</text>
  
                {/* Vector u (nằm ngang) */}
                <line x1={oX} y1={oY} x2={uX} y2={uY} stroke="#2563eb" strokeWidth="2.5" />
                <polygon points={`${uX},${uY} ${uX - 7},${uY - 4} ${uX - 7},${uY + 4}`} fill="#2563eb" />
                <text x={uX + 6} y={uY + 4} fontSize="9.5" fontWeight="bold" fill="#1d4ed8">u (|u|={lenU})</text>
  
                {/* Vector v (góc theta) */}
                <line x1={oX} y1={oY} x2={vX} y2={vY} stroke="#16a34a" strokeWidth="2.5" />
                <circle cx={vX} cy={vY} r="3" fill="#16a34a" />
                <text x={vX + (Math.cos(thRad) >= 0 ? 6 : -18)} y={vY - 4} fontSize="9.5" fontWeight="bold" fill="#15803d">v (|v|={lenV})</text>
  
                {/* Cung biểu diễn góc theta */}
                <path
                  d={`M ${oX + 22} ${oY} A 22 22 0 0 0 ${oX + 22 * Math.cos(thRad)} ${oY - 22 * Math.sin(thRad)}`}
                  fill="none"
                  stroke="#d97706"
                  strokeWidth="1.5"
                />
                <text x={oX + 26 * Math.cos(thRad / 2)} y={oY - 26 * Math.sin(thRad / 2)} fontSize="8.5" fontWeight="bold" fill="#d97706">θ = {thDeg}°</text>
  
                {isPerp && (
                  <rect x={oX} y={oY - 10} width="10" height="10" fill="none" stroke="#dc2626" strokeWidth="1.5" />
                )}
  
                <text x="170" y="136" textAnchor="middle" fontSize="9.5" fontWeight="bold" fill={isPerp ? '#dc2626' : '#0f172a'}>
                  u · v = |u| · |v| · cos(θ) = {lenU} × {lenV} × {Math.cos(thRad).toFixed(2)} = {dotProd.toFixed(2)} {isPerp ? '★ HAI VECTOR VUÔNG GÓC (u ⊥ v)' : ''}
                </text>
              </svg>
              <div style={{ fontSize: '0.78rem', color: '#166534', background: '#f0fdf4', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
                ➡️ <b>Tích Vô Hướng Vector Lớp 10:</b> Tích vô hướng đo lường mức độ cùng hướng của hai vector: <b>u · v = |u|·|v|·cos(θ)</b>. Đặc biệt, <b>hai vector vuông góc khi và chỉ khi tích vô hướng bằng 0</b> (θ = 90°)!
              </div>
            </div>
          );
        }
  
        // 2.15 Cấp số cộng & Cấp số nhân (THPT Lớp 11)
        if (
          topic.includes('cấp số') ||
          topic.includes('dãy số') ||
          fId.includes('cap-so')
        ) {
          const u1 = Math.min(10, Math.max(1, getVal(['u1'], 2)));
          const step = Math.min(5, Math.max(1, getVal(['d', 'q'], 3)));
          const isGeo = fId.includes('nhan') || topic.includes('nhân');
  
          const terms: number[] = [];
          for (let i = 0; i < 6; i++) {
            if (isGeo) {
              terms.push(u1 * Math.pow(step, i));
            } else {
              terms.push(u1 + i * step);
            }
          }
  
          const maxTerm = Math.max(...terms, 1);
          const barW = 28;
          const startX = 65;
  
          return (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
                <rect x="0" y="0" width="340" height="145" fill="#fffbeb" rx="4" />
                <line x1="45" y1="110" x2="315" y2="110" stroke="#94a3b8" strokeWidth="1.5" />
  
                {terms.map((t, idx) => {
                  const bH = Math.min(85, Math.max(8, (t / maxTerm) * 85));
                  const bX = startX + idx * (barW + 12);
                  const bY = 110 - bH;
                  return (
                    <g key={idx}>
                      <rect x={bX} y={bY} width={barW} height={bH} fill={isGeo ? '#fde68a' : '#bfdbfe'} stroke={isGeo ? '#d97706' : '#2563eb'} strokeWidth="1.5" rx="3" />
                      <text x={bX + barW / 2} y={bY - 4} textAnchor="middle" fontSize="8" fontWeight="bold" fill="#0f172a">{t}</text>
                      <text x={bX + barW / 2} y="122" textAnchor="middle" fontSize="8" fill="#64748b">u_{idx + 1}</text>
                    </g>
                  );
                })}
  
                <text x="170" y="138" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#92400e">
                  {isGeo ? `Cấp số nhân (q = ${step}): uₙ = u₁ · qⁿ⁻¹` : `Cấp số cộng (d = ${step}): uₙ = u₁ + (n − 1)d`}  |  u₆ = {terms[5]}
                </text>
              </svg>
              <div style={{ fontSize: '0.78rem', color: '#92400e', background: '#fffbeb', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
                📊 <b>So Sánh Tăng Trưởng Lớp 11:</b> {isGeo ? 'Cấp số nhân tăng trưởng theo cấp số mũ (nhân q liên tiếp), tạo nên bước nhảy vọt khổng lồ!' : 'Cấp số cộng tăng trưởng tuyến tính đều đặn (mỗi bước cộng thêm công sai d).'}
              </div>
            </div>
          );
        }
  
        // 2.16 Hàm số Mũ & Logarit (THPT Lớp 11-12)
        if (
          topic.includes('logarit') ||
          topic.includes('mũ') ||
          fId.includes('logarit') ||
          fId.includes('mu')
        ) {
          const base = Math.max(0.2, getVal(['a'], 2.0));
          const oX = 170, oY = 70;
          const scale = 22;
  
          const expPts: string[] = [];
          const logPts: string[] = [];
  
          for (let x = -3; x <= 3; x += 0.2) {
            const yExp = Math.pow(base, x);
            if (yExp >= 0 && yExp <= 5) {
              expPts.push(`${oX + x * scale},${oY - yExp * scale}`);
            }
          }
          for (let x = 0.1; x <= 5; x += 0.2) {
            const yLog = Math.log(x) / Math.log(base);
            if (yLog >= -3 && yLog <= 3) {
              logPts.push(`${oX + x * scale},${oY - yLog * scale}`);
            }
          }
  
          return (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
                <rect x="0" y="0" width="340" height="145" fill="#f8fafc" rx="4" />
                <line x1="20" y1={oY} x2="320" y2={oY} stroke="#cbd5e1" strokeWidth="1.5" />
                <line x1={oX} y1="10" x2={oX} y2="135" stroke="#cbd5e1" strokeWidth="1.5" />
                <text x="315" y={oY + 12} fontSize="9" fill="#94a3b8">x</text>
                <text x={oX + 6} y="18" fontSize="9" fill="#94a3b8">y</text>
  
                {/* Đường phân giác y = x nét đứt */}
                <line x1="90" y1="130" x2="250" y2="10" stroke="#94a3b8" strokeWidth="1" strokeDasharray="3 3" />
                <text x="245" y="24" fontSize="7.5" fill="#94a3b8">y = x</text>
  
                {/* Đồ thị hàm mũ y = a^x (xanh dương) */}
                {expPts.length > 2 && (
                  <polyline points={expPts.join(' ')} fill="none" stroke="#2563eb" strokeWidth="2.2" />
                )}
                <text x="110" y="30" fontSize="8.5" fontWeight="bold" fill="#2563eb">y = {base}ˣ</text>
  
                {/* Đồ thị hàm logarit y = log_a(x) (đỏ) */}
                {logPts.length > 2 && (
                  <polyline points={logPts.join(' ')} fill="none" stroke="#dc2626" strokeWidth="2.2" />
                )}
                <text x="255" y="85" fontSize="8.5" fontWeight="bold" fill="#dc2626">y = log_{base}(x)</text>
  
                <text x="170" y="138" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0f172a">
                  Cơ số a = {base} ({base > 1 ? 'Đồng biến khi a > 1' : 'Nghịch biến khi 0 < a < 1'})  |  Đối xứng qua đường thẳng y = x
                </text>
              </svg>
              <div style={{ fontSize: '0.78rem', color: '#1e40af', background: '#eff6ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
                🔄 <b>Tính Đối Xứng Mũ & Logarit Lớp 11-12:</b> Hàm số mũ <i>y = aˣ</i> và hàm số logarit <i>y = logₐ(x)</i> là hai hàm số ngược nhau, <b>đồ thị của chúng luôn đối xứng nhau qua đường phân giác y = x</b>!
              </div>
            </div>
          );
        }
  
      }

      // 2.1 Định lý Ta-lét trong tam giác (THCS Lớp 8)
      if (
        fId.includes('ta-let') ||
        fId.includes('thales') ||
        topic.includes('ta-lét') ||
        topic.includes('thales')
      ) {
        const k = Math.min(0.85, Math.max(0.15, getVal(['k', 'tile'], 0.6)));
        const abLen = getVal(['ab'], 10);
        const acLen = getVal(['ac'], 12);
        const am = (k * abLen).toFixed(1);
        const mb = ((1 - k) * abLen).toFixed(1);
        const an = (k * acLen).toFixed(1);
        const nc = ((1 - k) * acLen).toFixed(1);

        const topAx = 170, topAy = 18;
        const bBx = 60, bBy = 110;
        const cCx = 280, cCy = 110;

        const mX = topAx + k * (bBx - topAx);
        const mY = topAy + k * (bBy - topAy);
        const nX = topAx + k * (cCx - topAx);
        const nY = topAy + k * (cCy - topAy);

        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
              <rect x="0" y="0" width="340" height="145" fill="#f8fafc" rx="4" />
              {/* Tam giác ABC */}
              <polygon points={`${topAx},${topAy} ${bBx},${bBy} ${cCx},${cCy}`} fill="#eff6ff" stroke="#3b82f6" strokeWidth="2" />
              {/* Đoạn MN song song BC */}
              <line x1={mX} y1={mY} x2={nX} y2={nY} stroke="#ef4444" strokeWidth="2.5" />
              <circle cx={mX} cy={mY} r="3.5" fill="#ef4444" />
              <circle cx={nX} cy={nY} r="3.5" fill="#ef4444" />

              {/* Tên các đỉnh và điểm */}
              <text x={topAx} y={topAy - 5} textAnchor="middle" fontSize="10" fontWeight="bold" fill="#1e40af">A</text>
              <text x={bBx - 10} y={bBy + 5} textAnchor="middle" fontSize="10" fontWeight="bold" fill="#1e40af">B</text>
              <text x={cCx + 10} y={cCy + 5} textAnchor="middle" fontSize="10" fontWeight="bold" fill="#1e40af">C</text>
              <text x={mX - 12} y={mY + 3} textAnchor="middle" fontSize="9.5" fontWeight="bold" fill="#dc2626">M</text>
              <text x={nX + 12} y={nY + 3} textAnchor="middle" fontSize="9.5" fontWeight="bold" fill="#dc2626">N</text>

              {/* Độ dài các đoạn bên trái và phải */}
              <text x={(topAx + mX) / 2 - 12} y={(topAy + mY) / 2} fontSize="8" fontWeight="bold" fill="#2563eb">AM={am}</text>
              <text x={(bBx + mX) / 2 - 14} y={(bBy + mY) / 2 + 3} fontSize="8" fontWeight="bold" fill="#64748b">MB={mb}</text>
              <text x={(topAx + nX) / 2 + 12} y={(topAy + nY) / 2} fontSize="8" fontWeight="bold" fill="#2563eb">AN={an}</text>
              <text x={(cCx + nX) / 2 + 14} y={(cCy + nY) / 2 + 3} fontSize="8" fontWeight="bold" fill="#64748b">NC={nc}</text>

              {/* Nhãn song song */}
              <text x={topAx} y={mY - 4} textAnchor="middle" fontSize="8" fontWeight="bold" fill="#dc2626">MN ∥ BC</text>

              <text x="170" y="132" textAnchor="middle" fontSize="9.5" fontWeight="bold" fill="#1e3a8a">
                Tỉ số Ta-lét: AM/AB = AN/AC = {k.toFixed(2)}  •  AM/MB = AN/NC = {(k / Math.max(0.01, 1 - k)).toFixed(2)}
              </text>
            </svg>
            <div style={{ fontSize: '0.78rem', color: '#1e40af', background: '#eff6ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
              📐 <b>Logic Định Lý Ta-lét Lớp 8:</b> Khi đường thẳng <i>MN</i> song song với cạnh <i>BC</i>, nó định ra trên hai cạnh <i>AB, AC</i> những đoạn thẳng tương ứng tỉ lệ. Kéo thanh trượt để di chuyển <i>MN</i> và thấy tỉ số không đổi!
            </div>
          </div>
        );
      }

      // 2.2 Định lý Pytago (THCS Lớp 7 & 9)
      if (
        fId.includes('pytago') ||
        topic.includes('pytago')
      ) {
        const sideA = Math.min(12, Math.max(1, getVal(['a'], 3)));
        const sideB = Math.min(12, Math.max(1, getVal(['b'], 4)));
        const sideC = Math.sqrt(sideA * sideA + sideB * sideB);
        const sqA = sideA * sideA;
        const sqB = sideB * sideB;
        const sqC = sqA + sqB;

        const scale = 55 / Math.max(sideA, sideB, 5);
        const pA = sideA * scale;
        const pB = sideB * scale;

        const ox = 125, oy = 105;
        const topY = oy - pA;
        const rightX = ox + pB;

        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
              <rect x="0" y="0" width="340" height="145" fill="#fafafa" rx="4" />

              {/* Hình vuông trên cạnh a */}
              <rect x={ox - Math.min(35, pA * 0.7)} y={topY} width={Math.min(35, pA * 0.7)} height={pA} fill="#fee2e2" stroke="#ef4444" strokeWidth="1.2" />
              <text x={ox - Math.min(35, pA * 0.7) / 2} y={topY + pA / 2 + 3} textAnchor="middle" fontSize="8" fontWeight="bold" fill="#b91c1c">a²={sqA}</text>

              {/* Hình vuông trên cạnh b */}
              <rect x={ox} y={oy} width={pB} height={Math.min(32, pB * 0.7)} fill="#dcfce7" stroke="#22c55e" strokeWidth="1.2" />
              <text x={ox + pB / 2} y={oy + Math.min(32, pB * 0.7) / 2 + 3} textAnchor="middle" fontSize="8" fontWeight="bold" fill="#15803d">b²={sqB}</text>

              {/* Tam giác vuông chính */}
              <polygon points={`${ox},${oy} ${ox},${topY} ${rightX},${oy}`} fill="#e0f2fe" stroke="#0284c7" strokeWidth="2" />
              <rect x={ox} y={oy - 8} width="8" height="8" fill="none" stroke="#0284c7" strokeWidth="1.2" />

              <text x={ox - 8} y={(topY + oy) / 2 + 3} textAnchor="end" fontSize="9" fontWeight="bold" fill="#dc2626">a={sideA}</text>
              <text x={(ox + rightX) / 2} y={oy + 14} textAnchor="middle" fontSize="9" fontWeight="bold" fill="#16a34a">b={sideB}</text>
              <text x={(ox + rightX) / 2 + 10} y={(topY + oy) / 2 - 4} fontSize="9" fontWeight="bold" fill="#2563eb">c={sideC.toFixed(2)}</text>

              <text x="260" y="45" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#0369a1">c² = a² + b²</text>
              <text x="260" y="65" textAnchor="middle" fontSize="9" fill="#475569">{sqC} = {sqA} + {sqB}</text>
              <text x="260" y="85" textAnchor="middle" fontSize="9.5" fontWeight="bold" fill="#0284c7">c = √{sqC} ≈ {sideC.toFixed(2)}</text>
            </svg>
            <div style={{ fontSize: '0.78rem', color: '#0369a1', background: '#f0f9ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
              📐 <b>Định Lý Pytago Lớp 7 & 9:</b> Diện tích hình vuông dựng trên cạnh huyền bằng tổng diện tích hai hình vuông dựng trên hai cạnh góc vuông: <b>a² + b² = c²</b> ({sqA} + {sqB} = {sqC}).
            </div>
          </div>
        );
      }

      // 2.3 Hệ thức lượng trong tam giác vuông: Đường cao & Hình chiếu (THCS Lớp 9)
      if (
        fId.includes('he-thuc-luong') ||
        fId.includes('duong-cao') ||
        fId.includes('hinh-chieu') ||
        topic.includes('hệ thức lượng') ||
        topic.includes('hình chiếu')
      ) {
        const bh = Math.min(16, Math.max(1, getVal(['bh', 'b1'], 4)));
        const ch = Math.min(16, Math.max(1, getVal(['ch', 'c1'], 9)));
        const bc = bh + ch;
        const ah = Math.sqrt(bh * ch);
        const ab = Math.sqrt(bc * bh);
        const ac = Math.sqrt(bc * ch);

        const bX = 50, cX = 290, baseY = 110;
        const hX = bX + (bh / bc) * 240;
        const ahPx = Math.min(80, Math.max(25, (ah / bc) * 240));
        const aY = baseY - ahPx;

        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
              <rect x="0" y="0" width="340" height="145" fill="#f8fafc" rx="4" />
              <polygon points={`${bX},${baseY} ${hX},${aY} ${cX},${baseY}`} fill="#eff6ff" stroke="#2563eb" strokeWidth="2" />
              <line x1={hX} y1={aY} x2={hX} y2={baseY} stroke="#dc2626" strokeWidth="2" strokeDasharray="3 2" />
              <rect x={hX - 6} y={baseY - 6} width="6" height="6" fill="none" stroke="#dc2626" strokeWidth="1" />

              <text x={hX} y={aY - 5} textAnchor="middle" fontSize="10" fontWeight="bold" fill="#1e40af">A</text>
              <text x={bX - 8} y={baseY + 4} textAnchor="middle" fontSize="10" fontWeight="bold" fill="#1e40af">B</text>
              <text x={cX + 8} y={baseY + 4} textAnchor="middle" fontSize="10" fontWeight="bold" fill="#1e40af">C</text>
              <text x={hX} y={baseY + 12} textAnchor="middle" fontSize="9.5" fontWeight="bold" fill="#dc2626">H</text>

              <text x={(bX + hX) / 2} y={baseY + 12} textAnchor="middle" fontSize="8" fontWeight="bold" fill="#16a34a">BH={bh}</text>
              <text x={(hX + cX) / 2} y={baseY + 12} textAnchor="middle" fontSize="8" fontWeight="bold" fill="#16a34a">CH={ch}</text>
              <text x={hX + 18} y={(aY + baseY) / 2} fontSize="8.5" fontWeight="bold" fill="#dc2626">AH={ah.toFixed(1)}</text>
              <text x={(bX + hX) / 2 - 10} y={(aY + baseY) / 2 - 4} fontSize="8" fill="#475569">c={ab.toFixed(1)}</text>
              <text x={(hX + cX) / 2 + 10} y={(aY + baseY) / 2 - 4} fontSize="8" fill="#475569">b={ac.toFixed(1)}</text>

              <text x="170" y="138" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0f172a">
                AH² = BH · CH ({bh} × {ch} = {bh * ch} → AH = {ah.toFixed(1)})  |  BC = {bc}
              </text>
            </svg>
            <div style={{ fontSize: '0.78rem', color: '#1e40af', background: '#eff6ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
              📐 <b>Hệ Thức Lượng Lớp 9:</b> Trong tam giác vuông, bình phương đường cao ứng với cạnh huyền bằng tích hai hình chiếu: <b>AH² = BH · CH</b>, và <b>AB² = BC · BH</b>, <b>AC² = BC · CH</b>.
            </div>
          </div>
        );
      }

      // 2.4 Đường trung bình của hình thang & tam giác (THCS Lớp 8)
      if (
        fId.includes('hinh-thang') ||
        fId.includes('duong-trung-binh') ||
        topic.includes('hình thang') ||
        topic.includes('đường trung bình')
      ) {
        const bTop = Math.min(15, Math.max(2, getVal(['b'], 4)));
        const aBot = Math.min(25, Math.max(bTop + 2, getVal(['a'], 8)));
        const hVal = Math.min(15, Math.max(2, getVal(['h'], 5)));
        const midline = (aBot + bTop) / 2;
        const area = midline * hVal;

        const cX = 170;
        const pTop = bTop * 10;
        const pBot = aBot * 10;
        const topL = cX - pTop / 2, topR = cX + pTop / 2;
        const botL = cX - pBot / 2, botR = cX + pBot / 2;
        const topY = 30, botY = 105;
        const midY = (topY + botY) / 2;
        const midL = (topL + botL) / 2, midR = (topR + botR) / 2;

        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
              <rect x="0" y="0" width="340" height="145" fill="#fffbeb" rx="4" />
              <polygon points={`${topL},${topY} ${topR},${topY} ${botR},${botY} ${botL},${botY}`} fill="#fef3c7" stroke="#d97706" strokeWidth="2" />
              <line x1={midL} y1={midY} x2={midR} y2={midY} stroke="#ea580c" strokeWidth="2.5" strokeDasharray="4 2" />
              <circle cx={midL} cy={midY} r="3" fill="#ea580c" />
              <circle cx={midR} cy={midY} r="3" fill="#ea580c" />

              <line x1={topL + 15} y1={topY} x2={topL + 15} y2={botY} stroke="#7c3aed" strokeWidth="1.5" strokeDasharray="2 2" />
              <text x={topL + 22} y={(topY + botY) / 2 + 3} fontSize="8" fontWeight="bold" fill="#7c3aed">h={hVal}</text>

              <text x={cX} y={topY - 5} textAnchor="middle" fontSize="9" fontWeight="bold" fill="#b45309">Đáy bé b = {bTop}</text>
              <text x={cX} y={botY + 12} textAnchor="middle" fontSize="9" fontWeight="bold" fill="#b45309">Đáy lớn a = {aBot}</text>
              <text x={cX} y={midY - 4} textAnchor="middle" fontSize="8.5" fontWeight="bold" fill="#c2410c">Đường trung bình MN = {midline}</text>

              <text x="170" y="135" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#78350f">
                MN = (a + b) : 2 = ({aBot} + {bTop}) : 2 = {midline}  |  Diện tích S = MN × h = {area.toFixed(1)} cm²
              </text>
            </svg>
            <div style={{ fontSize: '0.78rem', color: '#92400e', background: '#fffbeb', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
              📐 <b>Đường Trung Bình Hình Thang Lớp 8:</b> Đoạn thẳng nối trung điểm hai cạnh bên thì song song với hai đáy và dài bằng <b>nửa tổng hai đáy: MN = (a + b) : 2</b>. Diện tích hình thang bằng <b>MN × h</b>!
            </div>
          </div>
        );
      }

      // 2.5 Đường tròn: Tiếp tuyến, Dây cung, Bán kính (THCS Lớp 9)
      if (
        fId.includes('duong-tron') ||
        topic.includes('đường tròn') ||
        topic.includes('tiếp tuyến') ||
        topic.includes('dây cung') ||
        topic.includes('góc nội tiếp')
      ) {
        const R = Math.min(10, Math.max(2, getVal(['R'], 5)));
        const d = Math.min(15, Math.max(R + 0.5, getVal(['d'], 7)));
        const tanLen = Math.sqrt(d * d - R * R);

        const oX = 110, oY = 70;
        const rPx = 40;
        const dPx = Math.min(150, Math.max(65, (d / R) * rPx));
        const aX = oX + dPx, aY = oY;

        const cosAngle = rPx / dPx;
        const sinAngle = Math.sqrt(Math.max(0, 1 - cosAngle * cosAngle));
        const t1X = oX + rPx * cosAngle;
        const t1Y = oY - rPx * sinAngle;
        const t2X = oX + rPx * cosAngle;
        const t2Y = oY + rPx * sinAngle;

        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
              <rect x="0" y="0" width="340" height="145" fill="#f0fdf4" rx="4" />
              <circle cx={oX} cy={oY} r={rPx} fill="#e0f2fe" stroke="#0284c7" strokeWidth="2" />
              <circle cx={oX} cy={oY} r="3" fill="#0284c7" />
              <text x={oX - 10} y={oY + 4} fontSize="9.5" fontWeight="bold" fill="#0369a1">O</text>

              <circle cx={aX} cy={aY} r="3" fill="#dc2626" />
              <text x={aX + 8} y={aY + 4} fontSize="10" fontWeight="bold" fill="#dc2626">A</text>

              <line x1={aX} y1={aY} x2={t1X} y2={t1Y} stroke="#16a34a" strokeWidth="2" />
              <line x1={aX} y1={aY} x2={t2X} y2={t2Y} stroke="#16a34a" strokeWidth="2" />
              <circle cx={t1X} cy={t1Y} r="3" fill="#16a34a" />
              <circle cx={t2X} cy={t2Y} r="3" fill="#16a34a" />
              <text x={t1X - 2} y={t1Y - 6} fontSize="9" fontWeight="bold" fill="#15803d">B</text>
              <text x={t2X - 2} y={t2Y + 12} fontSize="9" fontWeight="bold" fill="#15803d">C</text>

              <line x1={oX} y1={oY} x2={t1X} y2={t1Y} stroke="#0284c7" strokeWidth="1.5" strokeDasharray="3 2" />
              <line x1={oX} y1={oY} x2={t2X} y2={t2Y} stroke="#0284c7" strokeWidth="1.5" strokeDasharray="3 2" />
              <line x1={oX} y1={oY} x2={aX} y2={aY} stroke="#94a3b8" strokeWidth="1" strokeDasharray="2 2" />

              <text x="170" y="136" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#065f46">
                Tiếp tuyến AB ⊥ OB → AB = √(OA² − R²) = √({d}² − {R}²) = {tanLen.toFixed(1)} cm
              </text>
            </svg>
            <div style={{ fontSize: '0.78rem', color: '#166534', background: '#f0fdf4', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
              ⭕ <b>Đường Tròn & Tiếp Tuyến Lớp 9:</b> Tiếp tuyến vuông góc với bán kính tại tiếp điểm (<i>AB ⊥ OB</i>). Hai tiếp tuyến xuất phát từ <i>A</i> thì bằng nhau: <b>AB = AC = √(d² − R²)</b>.
            </div>
          </div>
        );
      }

      // 2.6 Bảy Hằng Đẳng Thức Đáng Nhớ - Cắt ghép hình học (THCS Lớp 8)
      if (
        fId.includes('hang-dang-thuc') ||
        topic.includes('hằng đẳng thức') ||
        topic.includes('bình phương')
      ) {
        const valA = Math.min(8, Math.max(1, getVal(['a'], 3)));
        const valB = Math.min(8, Math.max(1, getVal(['b'], 2)));
        const total = valA + valB;
        const sqTotal = total * total;
        const sqA = valA * valA;
        const sqB = valB * valB;
        const rectAB = valA * valB;

        const boxSize = 90;
        const cutA = (valA / total) * boxSize;
        const cutB = boxSize - cutA;
        const startX = 65, startY = 18;

        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
              <rect x="0" y="0" width="340" height="145" fill="#faf5ff" rx="4" />

              <rect x={startX} y={startY} width={cutA} height={cutA} fill="#bfdbfe" stroke="#2563eb" strokeWidth="1.5" />
              <text x={startX + cutA / 2} y={startY + cutA / 2 + 3} textAnchor="middle" fontSize="8" fontWeight="bold" fill="#1e40af">a²={sqA}</text>

              <rect x={startX + cutA} y={startY} width={cutB} height={cutA} fill="#bbf7d0" stroke="#16a34a" strokeWidth="1.5" />
              <text x={startX + cutA + cutB / 2} y={startY + cutA / 2 + 3} textAnchor="middle" fontSize="8" fontWeight="bold" fill="#15803d">ab={rectAB}</text>

              <rect x={startX} y={startY + cutA} width={cutA} height={cutB} fill="#bbf7d0" stroke="#16a34a" strokeWidth="1.5" />
              <text x={startX + cutA / 2} y={startY + cutA + cutB / 2 + 3} textAnchor="middle" fontSize="8" fontWeight="bold" fill="#15803d">ab={rectAB}</text>

              <rect x={startX + cutA} y={startY + cutA} width={cutB} height={cutB} fill="#fed7aa" stroke="#ea580c" strokeWidth="1.5" />
              <text x={startX + cutA + cutB / 2} y={startY + cutA + cutB / 2 + 3} textAnchor="middle" fontSize="8" fontWeight="bold" fill="#9a3412">b²={sqB}</text>

              <text x="250" y="38" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#6b21a8">(a + b)²</text>
              <text x="250" y="58" textAnchor="middle" fontSize="9.5" fontWeight="bold" fill="#2563eb">= a² + 2ab + b²</text>
              <text x="250" y="78" textAnchor="middle" fontSize="9" fill="#475569">= {sqA} + 2({rectAB}) + {sqB}</text>
              <text x="250" y="98" textAnchor="middle" fontSize="10.5" fontWeight="bold" fill="#6b21a8">= {sqTotal}</text>

              <text x="170" y="132" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#581c87">
                Hình vuông cạnh (a + b) = {total} có diện tích = {sqTotal}
              </text>
            </svg>
            <div style={{ fontSize: '0.78rem', color: '#6b21a8', background: '#faf5ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
              🟧 <b>Hằng Đẳng Thức Lớp 8:</b> Hình vuông lớn cạnh <i>(a + b)</i> được chia thành 1 hình vuông <i>a²</i>, 1 hình vuông <i>b²</i>, và 2 hình chữ nhật <i>ab</i>. Vậy: <b>(a + b)² = a² + 2ab + b²</b>!
            </div>
          </div>
        );
      }

      // 2.7 Trục số thực nghiệm: Số nguyên & Giá trị tuyệt đối (THCS Lớp 6-7)
      if (
        fId.includes('truc-so') ||
        fId.includes('so-nguyen') ||
        fId.includes('gia-tri-tuyet-doi') ||
        topic.includes('trục số') ||
        topic.includes('số nguyên') ||
        topic.includes('giá trị tuyệt đối')
      ) {
        const ptX = Math.min(10, Math.max(-10, getVal(['x'], -3)));
        const ptY = Math.min(10, Math.max(-10, getVal(['y'], 4)));
        const dist = Math.abs(ptX - ptY);

        const oX = 170, axisY = 65;
        const unitPx = 12;
        const xPos = oX + ptX * unitPx;
        const yPos = oX + ptY * unitPx;

        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
              <rect x="0" y="0" width="340" height="145" fill="#f8fafc" rx="4" />
              <line x1="20" y1={axisY} x2="320" y2={axisY} stroke="#475569" strokeWidth="2" />
              <polygon points="320,65 312,61 312,69" fill="#475569" />

              {[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10].map((num) => {
                const px = oX + num * unitPx;
                const isZero = num === 0;
                return (
                  <g key={num}>
                    <line x1={px} y1={axisY - (isZero ? 8 : 4)} x2={px} y2={axisY + (isZero ? 8 : 4)} stroke={isZero ? '#0284c7' : '#94a3b8'} strokeWidth={isZero ? 2 : 1} />
                    <text x={px} y={axisY + 18} textAnchor="middle" fontSize="7.5" fontWeight={isZero ? 'bold' : 'normal'} fill={isZero ? '#0284c7' : '#64748b'}>
                      {num}
                    </text>
                  </g>
                );
              })}

              <circle cx={xPos} cy={axisY} r="4" fill="#dc2626" />
              <text x={xPos} y={axisY - 14} textAnchor="middle" fontSize="9" fontWeight="bold" fill="#dc2626">x = {ptX}</text>

              <circle cx={yPos} cy={axisY} r="4" fill="#16a34a" />
              <text x={yPos} y={axisY - 14} textAnchor="middle" fontSize="9" fontWeight="bold" fill="#16a34a">y = {ptY}</text>

              <path d={`M ${Math.min(xPos, yPos)} ${axisY - 6} Q ${(xPos + yPos) / 2} ${axisY - 24}, ${Math.max(xPos, yPos)} ${axisY - 6}`} fill="none" stroke="#6366f1" strokeWidth="1.5" />
              <text x={(xPos + yPos) / 2} y={axisY - 26} textAnchor="middle" fontSize="8.5" fontWeight="bold" fill="#4f46e5">
                Khoảng cách = |{ptX} − {ptY}| = {dist}
              </text>

              <text x="170" y="132" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#0f172a">
                |x| = {Math.abs(ptX)} (khoảng cách đến 0)  |  |y| = {Math.abs(ptY)}  |  Khoảng cách xy = {dist}
              </text>
            </svg>
            <div style={{ fontSize: '0.78rem', color: '#1e3a8a', background: '#eff6ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
              📏 <b>Trục Số & Giá Trị Tuyệt Đối Lớp 6:</b> Giá trị tuyệt đối <i>|a|</i> là khoảng cách từ điểm <i>a</i> đến mốc <i>0</i> trên trục số (luôn không âm). Khoảng cách giữa hai điểm là <i>|x − y|</i>.
            </div>
          </div>
        );
      }

      // 2.8 Hàm số bậc hai & Parabol y = ax^2 + bx + c (THCS Lớp 9 & THPT Lớp 10)
      if (
        fId.includes('parabol') ||
        fId.includes('bac-hai') ||
        topic.includes('parabol') ||
        topic.includes('ax^2') ||
        topic.includes('bậc hai')
      ) {
        const coefA = getVal(['a'], 1) || 1;
        const coefB = getVal(['b'], -2);
        const coefC = getVal(['c'], -3);
        const delta = coefB * coefB - 4 * coefA * coefC;
        const vX = -coefB / (2 * coefA);
        const vY = -delta / (4 * coefA);

        const oX = 170, oY = 70;
        const scale = 12;

        const pts: string[] = [];
        for (let x = -5; x <= 5; x += 0.5) {
          const y = coefA * x * x + coefB * x + coefC;
          const px = oX + x * scale;
          const py = oY - y * (scale * 0.4);
          if (py >= 10 && py <= 135) {
            pts.push(`${px},${py}`);
          }
        }

        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
              <rect x="0" y="0" width="340" height="145" fill="#f8fafc" rx="4" />
              <line x1="20" y1={oY} x2="320" y2={oY} stroke="#cbd5e1" strokeWidth="1.5" />
              <line x1={oX} y1="10" x2={oX} y2="135" stroke="#cbd5e1" strokeWidth="1.5" />
              <text x="315" y={oY + 12} fontSize="9" fill="#94a3b8">x</text>
              <text x={oX + 6} y="18" fontSize="9" fill="#94a3b8">y</text>

              {pts.length > 2 && (
                <polyline points={pts.join(' ')} fill="none" stroke="#2563eb" strokeWidth="2.5" />
              )}

              <circle cx={oX + vX * scale} cy={oY - vY * (scale * 0.4)} r="3.5" fill="#dc2626" />
              <text x={oX + vX * scale + 6} y={oY - vY * (scale * 0.4) - 4} fontSize="8.5" fontWeight="bold" fill="#dc2626">
                I({vX.toFixed(1)}, {vY.toFixed(1)})
              </text>

              <text x="170" y="138" textAnchor="middle" fontSize="9.5" fontWeight="bold" fill="#0f172a">
                y = {coefA}x² {coefB >= 0 ? `+ ${coefB}x` : `- ${Math.abs(coefB)}x`} {coefC >= 0 ? `+ ${coefC}` : `- ${Math.abs(coefC)}`}  |  Đỉnh I({vX.toFixed(1)}; {vY.toFixed(1)})
              </text>
            </svg>
            <div style={{ fontSize: '0.78rem', color: '#1e40af', background: '#eff6ff', padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
              📈 <b>Parabol Lớp 9 & 10:</b> Đồ thị có bề lõm quay lên khi <i>a &gt; 0</i> (quay xuống khi <i>a &lt; 0</i>). Trục đối xứng <i>x = −b/(2a) = {vX.toFixed(1)}</i>.
            </div>
          </div>
        );
      }

      // 2.9 Tam giác thường & Hình học phẳng Euclid cơ bản
      if (
        topic.includes('tam giác') ||
        fId.includes('tam-giac')
      ) {
        const sideA = Math.min(50, Math.max(25, 20 + v1 * 2));
        const sideB = Math.min(60, Math.max(30, 25 + v2 * 2));

        return (
          <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
            <g transform="translate(100, 15)">
              <polygon points={`0,${sideA} ${sideB},${sideA} ${sideB * 0.4},0`} fill="#e0f2fe" stroke="#0284c7" strokeWidth="2" />
              <text x={-18} y={sideA / 2} fontSize="10" fontWeight="bold" fill="#dc2626">c = {v1}</text>
              <text x={sideB / 2 - 8} y={sideA + 16} fontSize="10" fontWeight="bold" fill="#16a34a">a = {v2}</text>
            </g>
            <text x="170" y="138" textAnchor="middle" fontSize="10.5" fontWeight="bold" fill="#0f172a">
              Hình học tam giác: Tổng ba góc trong tam giác luôn bằng 180°
            </text>
          </svg>
        );
      }

      // 2.17 Đồ thị hàm số & Hệ tọa độ Descartes Oxy (Khi công thức thực sự về hàm số/đồ thị/tọa độ)
      const isFunctionGraphTopic =
        topic.includes('hàm số') ||
        topic.includes('đồ thị') ||
        topic.includes('tọa độ') ||
        topic.includes('toạ độ') ||
        fId.includes('ham-so') ||
        fId.includes('do-thi') ||
        fId.includes('toa-do');

      if (isFunctionGraphTopic) {
        const slope = Math.min(3, Math.max(-3, (v1 - 10) / 5));
        const yIntercept = Math.min(30, Math.max(-30, v2));

        return (
          <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
            <line x1="20" y1={70} x2="320" y2={70} stroke="#94a3b8" strokeWidth="1.5" />
            <line x1="170" y1="125" x2="170" y2="15" stroke="#94a3b8" strokeWidth="1.5" />
            <polygon points="320,70 314,67 314,73" fill="#94a3b8" />
            <polygon points="170,15 167,21 173,21" fill="#94a3b8" />
            <text x="315" y="85" fontSize="10" fontWeight="bold" fill="#64748b">x</text>
            <text x="180" y="22" fontSize="10" fontWeight="bold" fill="#64748b">y</text>
            <text x="160" y="82" fontSize="9" fill="#94a3b8">O</text>

            <line
              x1="50"
              y1={70 - (-120 * slope + yIntercept)}
              x2="290"
              y2={70 - (120 * slope + yIntercept)}
              stroke="#0284c7"
              strokeWidth="2.5"
            />
            <circle cx="170" cy={70 - yIntercept} r="4" fill="#ef4444" />
            <text x="30" y="28" fontSize="11" fontWeight="bold" fill="#0369a1">
              Đồ thị hàm số: y = {slope !== 0 ? `${slope.toFixed(1)}x` : ''} {yIntercept >= 0 ? `+ ${yIntercept}` : `- ${Math.abs(yIntercept)}`}
            </text>
          </svg>
        );
      }

      // 2.18 Các dạng Toán học khác (Số học, Đại số, Phương trình, Tỷ lệ...):
      // Tuyệt đối KHÔNG vẽ trục Oxy hay hàm số y=ax+b bất chấp!
      // Hiển thị mô hình Bảng Thay Số Trực Quan & Tỷ Lệ Thực Nghiệm:
      return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', padding: '6px 4px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: '#f8fafc', padding: '8px 12px', borderRadius: '6px', border: '1px solid #e2e8f0' }}>
            <div style={{ fontSize: '0.85rem', color: '#475569', fontWeight: 600 }}>
              📊 Quan hệ giá trị các tham số:
            </div>
            <div style={{ fontSize: '0.92rem', fontWeight: 700, color: '#0284c7' }}>
              {outputSymbol || 'Kết quả'}: {calculatedOutput !== null ? `${calculatedOutput} ${outputUnit}` : 'Đang tính...'}
            </div>
          </div>

          {/* Biểu diễn trực quan tỷ lệ các biến bằng thanh độ dài (Visual Ratio Bars) */}
          <div style={{ background: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '6px', padding: '10px 12px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {inputConfigs.slice(0, 3).map((inp, idx) => {
              const val = sliderValues[inp.symbol] ?? inp.default ?? 1;
              const range = Math.max(1, (inp.max ?? 100) - (inp.min ?? 0));
              const pct = Math.min(100, Math.max(5, (((val - (inp.min ?? 0)) / range) * 100)));
              const colors = ['#3b82f6', '#10b981', '#f59e0b'];
              const col = colors[idx % colors.length];

              return (
                <div key={inp.symbol} style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '0.8rem' }}>
                  <span style={{ width: '85px', color: '#64748b', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                    {inp.label || inp.symbol}:
                  </span>
                  <div style={{ flex: 1, height: '14px', background: '#f1f5f9', borderRadius: '4px', overflow: 'hidden', position: 'relative' }}>
                    <div style={{ width: `${pct}%`, height: '100%', background: col, borderRadius: '4px', transition: 'width 0.2s' }} />
                  </div>
                  <span style={{ width: '60px', textAlign: 'right', fontWeight: 700, color: '#0f172a' }}>
                    {val} {inp.unit}
                  </span>
                </div>
              );
            })}
          </div>

          <div style={{ fontSize: '0.78rem', color: '#475569', background: '#f0fdf4', padding: '6px 10px', borderRadius: '4px', border: '1px solid #bbf7d0', textAlign: 'left' }}>
            ✨ Kéo các thanh trượt bên dưới để quan sát giá trị đầu vào thay đổi và theo dõi kết quả tự động tính theo công thức.
          </div>
        </div>
      );
    }

    // =========================================================================
    // 3. HÓA HỌC (CHEMISTRY) - BÌNH THÍ NGHIỆM, CÂN BẰNG, PIN ĐIỆN HÓA
    // =========================================================================
    if (subj === 'chemistry') {
      // 3.1 Cân bằng hóa học & Chuyển dịch Le Chatelier (THPT Lớp 10-11)
      if (
        topic.includes('cân bằng') ||
        topic.includes('chatelier') ||
        fId.includes('can-bang') ||
        fId.includes('chatelier')
      ) {
        const shiftRight = Math.min(40, Math.max(-40, (v1 - v2) * 5));
        return (
          <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
            <text x="170" y="25" textAnchor="middle" fontSize="12" fontWeight="bold" fill="#0369a1">
              Phản ứng thuận nghịch: A + B ⇌ C + D
            </text>

            {/* Cột nồng độ chất phản ứng [A, B] */}
            <rect x="60" y={90 - (40 - shiftRight * 0.5)} width="50" height={40 - shiftRight * 0.5} fill="#3b82f6" rx="3" />
            <text x="85" y="105" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#1e3a8a">[A] + [B]</text>

            {/* Mũi tên cân bằng hai chiều */}
            <text x="170" y="75" textAnchor="middle" fontSize="18" fill="#d97706">⇌</text>
            <text x="170" y="95" textAnchor="middle" fontSize="10" fill="#b45309">
              {shiftRight > 5 ? 'Chuyển dịch Thuận →' : shiftRight < -5 ? '← Chuyển dịch Nghịch' : 'Đang Cân Bằng'}
            </text>

            {/* Cột nồng độ sản phẩm [C, D] */}
            <rect x="230" y={90 - (40 + shiftRight * 0.5)} width="50" height={40 + shiftRight * 0.5} fill="#10b981" rx="3" />
            <text x="255" y="105" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#064e3b">[C] + [D]</text>

            <text x="170" y="132" textAnchor="middle" fontSize="10" fill="#64748b">
              Nguyên lý Le Chatelier: Hệ tự cân bằng để chống lại sự thay đổi bên ngoài
            </text>
          </svg>
        );
      }

      // 3.2 Pin điện hóa Galvani (THPT Lớp 12 & ĐH)
      if (
        topic.includes('pin') ||
        topic.includes('điện hóa') ||
        fId.includes('pin') ||
        fId.includes('galvani') ||
        fId.includes('dien-hoa')
      ) {
        return (
          <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
            {/* Bình Anot (Zn) */}
            <rect x="50" y="55" width="70" height="60" fill="#e0f2fe" stroke="#475569" strokeWidth="2" rx="3" />
            <rect x="75" y="35" width="16" height="50" fill="#94a3b8" stroke="#334155" strokeWidth="1.5" />
            <text x="83" y="28" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#334155">Zn (-)</text>

            {/* Cầu muối nối hai bình */}
            <path d="M 95 65 Q 170 35, 245 65" fill="none" stroke="#f59e0b" strokeWidth="6" strokeLinecap="round" />
            <text x="170" y="52" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#b45309">Cầu muối</text>

            {/* Bình Catot (Cu) */}
            <rect x="220" y="55" width="70" height="60" fill="#dbeafe" stroke="#475569" strokeWidth="2" rx="3" />
            <rect x="245" y="35" width="16" height="50" fill="#ea580c" stroke="#9a3412" strokeWidth="1.5" />
            <text x="253" y="28" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#ea580c">Cu (+)</text>

            {/* Vôn kế đo suất điện động */}
            <circle cx="170" cy="22" r="14" fill="#ffffff" stroke="#0f172a" strokeWidth="1.5" />
            <text x="170" y="26" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#059669">E = 1.1V</text>

            <text x="170" y="132" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#0f172a">
              Pin Galvani: Zn + Cu²⁺ → Zn²⁺ + Cu (Dòng electron từ Anot sang Catot)
            </text>
          </svg>
        );
      }

      // 3.3 Bình thí nghiệm nồng độ dung dịch & pH (THCS & THPT)
      const conc = Math.min(100, Math.max(10, v1 * 5));
      const solColor = conc > 60 ? '#2563eb' : conc > 30 ? '#06b6d4' : '#10b981';

      return (
        <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
          <g transform="translate(140, 20)">
            <rect x="20" y="5" width="20" height="25" fill="none" stroke="#64748b" strokeWidth="2" />
            <path d="M 20 30 L -5 90 C -10 98, -5 100, 5 100 L 55 100 C 65 100, 70 98, 65 90 L 40 30 Z" fill="rgba(241, 245, 249, 0.6)" stroke="#475569" strokeWidth="2" />
            <path d={`M 5 96 L 55 96 L ${40 - (100 - conc) * 0.15} ${60 + (100 - conc) * 0.3} L ${20 + (100 - conc) * 0.15} ${60 + (100 - conc) * 0.3} Z`} fill={solColor} opacity="0.45" />

            <circle cx="25" cy="80" r="3" fill="#ffffff" opacity="0.8" />
            <circle cx="35" cy="70" r="2.5" fill="#ffffff" opacity="0.8" />
            <circle cx="28" cy="60" r="2" fill="#ffffff" opacity="0.7" />
            <text x="30" y="116" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#0f172a">
              Dung dịch: C = {v1} M
            </text>
          </g>

          <text x="240" y="55" fontSize="11" fontWeight="bold" fill="#0284c7">Phản ứng hóa học</text>
          <text x="240" y="75" fontSize="10" fill="#64748b">Hạt chất tan: {Math.round(conc)} mmol</text>
          <text x="240" y="95" fontSize="10" fill="#059669">Tốc độ v ∝ [C]</text>
        </svg>
      );
    }

    // =========================================================================
    // 4. SINH HỌC (BIOLOGY) - MENDEL PUNNETT, ADN, PHÂN BÀO, THÁP DINH DƯỠNG
    // =========================================================================
    if (subj === 'biology') {
      // 4.1 Quy luật di truyền Mendel & Khung Punnett (THCS Lớp 9 & THPT)
      if (
        topic.includes('di truyền') ||
        topic.includes('mendel') ||
        topic.includes('phân li') ||
        fId.includes('di-truyen') ||
        fId.includes('mendel') ||
        fId.includes('punnett') ||
        fId.includes('lai-')
      ) {
        return (
          <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
            {/* Khung Punnett 2x2 cho phép lai Aa x Aa */}
            <g transform="translate(60, 15)">
              <text x="50" y="14" textAnchor="middle" fontSize="10" fill="#64748b">Giao tử ♂ (Aa)</text>
              <text x="80" y="32" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#2563eb">A</text>
              <text x="130" y="32" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#dc2626">a</text>

              <text x="40" y="60" textAnchor="end" fontSize="10" fontWeight="bold" fill="#2563eb">A</text>
              <text x="40" y="100" textAnchor="end" fontSize="10" fontWeight="bold" fill="#dc2626">a</text>

              {/* Ô 1: AA (Trội - Vàng) */}
              <rect x="55" y="40" width="50" height="40" fill="#fef08a" stroke="#ca8a04" strokeWidth="1.5" />
              <text x="80" y="65" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#854d0e">AA</text>

              {/* Ô 2: Aa (Trội - Vàng) */}
              <rect x="105" y="40" width="50" height="40" fill="#fef08a" stroke="#ca8a04" strokeWidth="1.5" />
              <text x="130" y="65" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#854d0e">Aa</text>

              {/* Ô 3: Aa (Trội - Vàng) */}
              <rect x="55" y="80" width="50" height="40" fill="#fef08a" stroke="#ca8a04" strokeWidth="1.5" />
              <text x="80" y="105" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#854d0e">Aa</text>

              {/* Ô 4: aa (Lặn - Xanh) */}
              <rect x="105" y="80" width="50" height="40" fill="#bbf7d0" stroke="#16a34a" strokeWidth="1.5" />
              <text x="130" y="105" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#166534">aa</text>
            </g>

            <g transform="translate(235, 30)">
              <text x="0" y="20" fontSize="11" fontWeight="bold" fill="#0f172a">Tỉ lệ đời con:</text>
              <text x="0" y="40" fontSize="10.5" fill="#854d0e">🟡 3 Trội (1AA : 2Aa)</text>
              <text x="0" y="60" fontSize="10.5" fill="#166534">🟢 1 Lặn (1aa)</text>
              <text x="0" y="85" fontSize="10" fontWeight="bold" fill="#0284c7">Kiểu hình 3 : 1</text>
            </g>
          </svg>
        );
      }

      // 4.2 Cấu trúc chuỗi xoắn kép ADN (THCS & THPT)
      if (
        topic.includes('adn') ||
        topic.includes('gen') ||
        fId.includes('adn') ||
        fId.includes('dna') ||
        fId.includes('phien-ma')
      ) {
        return (
          <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
            <g transform="translate(30, 20)">
              <text x="140" y="15" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#0369a1">
                Chuỗi xoắn kép ADN & Nguyên tắc bổ sung
              </text>

              {/* Hai mạch xoắn đối song song */}
              <path d="M 20 40 Q 60 70, 100 40 T 180 40 T 260 40" fill="none" stroke="#0284c7" strokeWidth="2.5" />
              <path d="M 20 70 Q 60 40, 100 70 T 180 70 T 260 70" fill="none" stroke="#2563eb" strokeWidth="2.5" />

              {/* Các cặp base nối hai mạch */}
              <line x1="60" y1="45" x2="60" y2="65" stroke="#dc2626" strokeWidth="3" />
              <text x="60" y="85" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#dc2626">A = T</text>

              <line x1="140" y1="45" x2="140" y2="65" stroke="#16a34a" strokeWidth="3" />
              <text x="140" y="85" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#16a34a">G ≡ X</text>

              <line x1="220" y1="45" x2="220" y2="65" stroke="#dc2626" strokeWidth="3" />
              <text x="220" y="85" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#dc2626">T = A</text>
            </g>
            <text x="170" y="132" textAnchor="middle" fontSize="10" fill="#64748b">
              Quy tắc Chargaff: %A = %T, %G = %X (Tổng số Nu N = 2A + 2G)
            </text>
          </svg>
        );
      }

      // 4.3 Chỉ số khối cơ thể (BMI) & Phân loại thể trạng WHO
      if (fId.includes('bmi') || topic.includes('bmi') || topic.includes('khối cơ thể')) {
        const m = getVal(['m', 'w', 'weight'], 60);
        const h = getVal(['h', 'height'], 1.65);
        const bmiVal = h > 0 ? Number((m / (h * h)).toFixed(1)) : 22.0;

        let category = 'Bình thường';
        let catColor = '#16a34a';
        let catBg = '#dcfce7';
        if (bmiVal < 18.5) {
          category = 'Gầy / Thiếu cân';
          catColor = '#0284c7';
          catBg = '#e0f2fe';
        } else if (bmiVal < 25) {
          category = 'Bình thường / Chuẩn';
          catColor = '#16a34a';
          catBg = '#dcfce7';
        } else if (bmiVal < 30) {
          category = 'Thừa cân / Tiền béo phì';
          catColor = '#d97706';
          catBg = '#fef3c7';
        } else {
          category = 'Béo phì';
          catColor = '#dc2626';
          catBg = '#fee2e2';
        }

        // Tọa độ kim chỉ trên thanh đo (10 -> 40)
        const gaugeX = Math.min(300, Math.max(40, 40 + ((bmiVal - 10) / 30) * 260));

        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
              <rect x="0" y="0" width="340" height="145" fill="#f8fafc" rx="4" />
              <text x="170" y="22" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#0f172a">
                Thang Đánh Giá Thể Trạng BMI (WHO & Bộ Y Tế)
              </text>

              {/* 4 Dải màu phân loại BMI */}
              {/* < 18.5: Gầy (x: 40 -> 113.6) */}
              <rect x="40" y="45" width="74" height="22" fill="#38bdf8" rx="2" />
              <text x="77" y="60" textAnchor="middle" fontSize="8.5" fontWeight="bold" fill="#0369a1">&lt; 18.5</text>

              {/* 18.5 - 24.9: Chuẩn (x: 114 -> 170) */}
              <rect x="114" y="45" width="56" height="22" fill="#4ade80" />
              <text x="142" y="60" textAnchor="middle" fontSize="8.5" fontWeight="bold" fill="#14532d">18.5 - 24.9</text>

              {/* 25 - 29.9: Thừa cân (x: 170 -> 213) */}
              <rect x="170" y="45" width="43" height="22" fill="#facc15" />
              <text x="191" y="60" textAnchor="middle" fontSize="8.5" fontWeight="bold" fill="#713f12">25 - 29.9</text>

              {/* >= 30: Béo phì (x: 213 -> 300) */}
              <rect x="213" y="45" width="87" height="22" fill="#f87171" rx="2" />
              <text x="256" y="60" textAnchor="middle" fontSize="8.5" fontWeight="bold" fill="#7f1d1d">≥ 30</text>

              {/* Nhãn dưới dải */}
              <text x="77" y="80" textAnchor="middle" fontSize="8" fill="#0284c7">Thiếu cân</text>
              <text x="142" y="80" textAnchor="middle" fontSize="8" fill="#16a34a">Bình thường</text>
              <text x="191" y="80" textAnchor="middle" fontSize="8" fill="#d97706">Thừa cân</text>
              <text x="256" y="80" textAnchor="middle" fontSize="8" fill="#dc2626">Béo phì</text>

              {/* Con trỏ vị trí hiện tại */}
              <polygon points={`${gaugeX},40 ${gaugeX - 6},30 ${gaugeX + 6},30`} fill="#0f172a" />
              <line x1={gaugeX} y1="36" x2={gaugeX} y2="70" stroke="#0f172a" strokeWidth="2" />
              <circle cx={gaugeX} cy="70" r="3" fill="#0f172a" />

              {/* Badge Kết quả */}
              <text x="170" y="112" textAnchor="middle" fontSize="13" fontWeight="bold" fill={catColor}>
                BMI = {bmiVal} kg/m²  ({category})
              </text>
              <text x="170" y="132" textAnchor="middle" fontSize="9" fill="#64748b">
                Khối lượng: {m} kg  |  Chiều cao: {h} m  (BMI = m / h²)
              </text>
            </svg>
            <div style={{ fontSize: '0.78rem', color: catColor, background: catBg, padding: '6px 10px', borderRadius: '4px', textAlign: 'left', lineHeight: 1.45 }}>
              🩺 <b>Nhận xét sức khỏe:</b> Thể trạng hiện tại được phân loại <b>{category}</b>. Duy trì chế độ dinh dưỡng cân bằng và tập luyện thể thao đều đặn.
            </div>
          </div>
        );
      }

      // 4.4 Mặc định Sinh học: Phân bào & nhân đôi tế bào 2^k
      const generation = Math.min(6, Math.max(1, Math.round(v1 / 3)));
      const cellCount = Math.pow(2, generation);

      return (
        <svg viewBox="0 0 340 145" style={{ width: '100%', height: '135px' }}>
          <g transform="translate(40, 20)">
            <text x="60" y="15" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#0369a1">
              Phân bào & Nhân đôi ({generation} chu kỳ)
            </text>

            <g transform="translate(10, 35)">
              <circle cx="20" cy="30" r="14" fill="#dbeafe" stroke="#0284c7" strokeWidth="2" />
              <text x="20" y="34" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#0369a1">Mẹ</text>

              <line x1="38" y1="30" x2="65" y2="30" stroke="#94a3b8" strokeWidth="2" />

              <circle cx="85" cy="18" r="11" fill="#dcfce7" stroke="#16a34a" strokeWidth="1.5" />
              <circle cx="85" cy="42" r="11" fill="#dcfce7" stroke="#16a34a" strokeWidth="1.5" />

              <line x1="100" y1="30" x2="125" y2="30" stroke="#94a3b8" strokeWidth="2" />

              <circle cx="145" cy="10" r="8" fill="#fef3c7" stroke="#d97706" strokeWidth="1.5" />
              <circle cx="145" cy="25" r="8" fill="#fef3c7" stroke="#d97706" strokeWidth="1.5" />
              <circle cx="145" cy="40" r="8" fill="#fef3c7" stroke="#d97706" strokeWidth="1.5" />
              <circle cx="145" cy="55" r="8" fill="#fef3c7" stroke="#d97706" strokeWidth="1.5" />
            </g>

            <text x="220" y="55" fontSize="12" fontWeight="bold" fill="#059669">
              2^{generation} = {cellCount} tế bào con
            </text>
            <text x="220" y="74" fontSize="10" fill="#64748b">
              Bảo tồn bộ NST 2n
            </text>
          </g>
        </svg>
      );
    }

    // Fallback mặc định
    return null;
  };

  return (
    <div
      style={{
        marginTop: '16px',
        padding: isExpanded ? '24px' : '18px 20px',
        background: '#ffffff',
        border: '1px solid #bae6fd',
        borderRadius: 'var(--radius-md)',
        boxShadow: '0 4px 14px rgba(2, 132, 199, 0.06)',
      }}
    >
      {/* Header Panel with Mode Switcher */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          marginBottom: '14px',
          flexWrap: 'wrap',
          gap: '10px',
          borderBottom: '1px solid #f1f5f9',
          paddingBottom: '12px',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <div
            style={{
              width: '30px',
              height: '30px',
              borderRadius: '8px',
              background: '#0284c7',
              color: '#ffffff',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            <Sparkles size={16} />
          </div>
          <div>
            <h4 style={{ fontSize: '1rem', fontWeight: 800, color: '#0f172a', margin: 0 }}>
              {isElementary ? '🌱 Mô Phỏng Trực Quan Dành Cho Lớp 5' : 'Mô Hình Trực Quan & Thí Nghiệm Số'}
            </h4>
            <div style={{ fontSize: '0.78rem', color: isElementary ? '#16a34a' : '#64748b', fontWeight: isElementary ? 600 : 400 }}>
              {isElementary
                ? 'Minh họa bằng đồ vật thực tế: xe chạy, que tính, khối Lego xếp hình - chuẩn tư duy tiểu học'
                : 'Chuẩn mực giáo khoa: Sơ đồ khoa học chính xác & mô phỏng tương tác logic'}
            </div>
          </div>
        </div>

        {/* Switcher & Actions */}
        <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
          {hasIllustration && isComputable && (
            <div style={{ display: 'flex', background: '#f1f5f9', padding: '3px', borderRadius: 'var(--radius-sm)' }}>
              <button
                className="btn"
                style={{
                  padding: '4px 10px',
                  fontSize: '0.78rem',
                  fontWeight: 600,
                  borderRadius: 'var(--radius-sm)',
                  background: viewMode === 'diagram' ? '#ffffff' : 'transparent',
                  color: viewMode === 'diagram' ? '#0369a1' : '#64748b',
                  boxShadow: viewMode === 'diagram' ? '0 1px 3px rgba(0,0,0,0.08)' : 'none',
                }}
                onClick={() => setViewMode('diagram')}
              >
                <Layers size={13} style={{ marginRight: '4px' }} />
                <span>Sơ Đồ Chuẩn 2D</span>
              </button>

              <button
                className="btn"
                style={{
                  padding: '4px 10px',
                  fontSize: '0.78rem',
                  fontWeight: 600,
                  borderRadius: 'var(--radius-sm)',
                  background: viewMode === 'simulation' ? '#ffffff' : 'transparent',
                  color: viewMode === 'simulation' ? '#0369a1' : '#64748b',
                  boxShadow: viewMode === 'simulation' ? '0 1px 3px rgba(0,0,0,0.08)' : 'none',
                }}
                onClick={() => setViewMode('simulation')}
              >
                <Sliders size={13} style={{ marginRight: '4px' }} />
                <span>{isElementary ? 'Trực Quan Kéo Thả' : 'Thí Nghiệm Tham Số'}</span>
              </button>
            </div>
          )}

          <button
            className="btn btn-secondary"
            style={{ fontSize: '0.78rem', padding: '5px 8px' }}
            onClick={() => setIsExpanded(!isExpanded)}
            title={isExpanded ? 'Thu nhỏ' : 'Phóng to'}
          >
            {isExpanded ? <Minimize2 size={13} /> : <Maximize2 size={13} />}
          </button>
        </div>
      </div>

      {/* ================= VIEW 1: SƠ ĐỒ KHOA HỌC CHUẨN 2D SVG ================= */}
      {viewMode === 'diagram' && (
        <div className="animate-fade-in" style={{ textAlign: 'center', padding: '10px 0' }}>
          {hasIllustration ? (
            <div
              style={{
                background: '#ffffff',
                border: '1px solid #e2e8f0',
                borderRadius: 'var(--radius-md)',
                padding: '16px',
                display: 'inline-block',
                maxWidth: '100%',
                overflow: 'hidden',
                boxShadow: '0 2px 8px rgba(15, 23, 42, 0.04)',
              }}
            >
              <img
                src={illustrationUrl}
                alt={formula.illustration_2d?.title || formula.name_vi || 'Minh họa khoa học'}
                style={{
                  maxWidth: isExpanded ? '640px' : '480px',
                  width: '100%',
                  height: 'auto',
                  display: 'block',
                  margin: '0 auto',
                }}
              />
            </div>
          ) : (
            <div style={{ padding: '20px', background: '#f8fafc', borderRadius: 'var(--radius-md)', border: '1px solid #e2e8f0', textAlign: 'left' }}>
              <h5 style={{ fontSize: '0.92rem', fontWeight: 700, color: '#0369a1', marginBottom: '10px' }}>
                Ý Nghĩa Đại Lượng & Đơn Vị Đo Lường
              </h5>
              {formula.vars && Object.keys(formula.vars).length > 0 ? (
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '8px' }}>
                  {Object.entries(formula.vars).map(([sym, name]) => (
                    <div key={sym} style={{ padding: '8px 12px', background: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '6px' }}>
                      <span style={{ fontWeight: 700, color: '#0284c7' }}>{sym}</span>
                      <span style={{ color: '#64748b', fontSize: '0.8rem', marginLeft: '6px' }}>
                        {formula.units?.[sym] ? `(${formula.units[sym]})` : ''}
                      </span>
                      <div style={{ fontSize: '0.85rem', color: '#1e293b', marginTop: '2px' }}>{String(name)}</div>
                    </div>
                  ))}
                </div>
              ) : null}
            </div>
          )}

          {(formula.illustration_2d?.caption_vi || formula.illustration_2d?.note || formula.note) && (
            <div
              style={{
                fontSize: '0.86rem',
                color: '#334155',
                lineHeight: 1.55,
                marginTop: '12px',
                maxWidth: '620px',
                margin: '12px auto 0',
                padding: '10px 16px',
                background: '#f0fdf4',
                border: '1px solid #bbf7d0',
                borderRadius: 'var(--radius-sm)',
                textAlign: 'left',
              }}
            >
              <div style={{ fontWeight: 700, color: '#166534', marginBottom: '4px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <CheckCircle2 size={15} />
                <span>Bản chất khoa học & Quy luật thực nghiệm:</span>
              </div>
              <span>{formula.illustration_2d?.caption_vi || formula.illustration_2d?.note || formula.note}</span>
            </div>
          )}
        </div>
      )}

      {/* ================= VIEW 2: THÍ NGHIỆM ĐỘNG VỚI THANH TRƯỢT THAM SỐ ================= */}
      {viewMode === 'simulation' && isComputable && (
        <div className="animate-fade-in">
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(290px, 1fr))', gap: '20px', alignItems: 'center' }}>
            {/* Cột Trái: Thanh trượt tham số thực nghiệm */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2px' }}>
                <span style={{ fontSize: '0.82rem', fontWeight: 700, color: isElementary ? '#166534' : '#0369a1', textTransform: 'uppercase' }}>
                  {isElementary ? '🎮 Thanh trượt bạn nhỏ điều khiển' : 'Các biến số thực nghiệm'}
                </span>
                <button
                  className="btn btn-secondary"
                  style={{ fontSize: '0.74rem', padding: '3px 8px', display: 'flex', alignItems: 'center', gap: '4px' }}
                  onClick={handleReset}
                  title="Đặt lại thông số mặc định"
                >
                  <RotateCcw size={12} />
                  <span>Đặt Lại</span>
                </button>
              </div>

              {inputConfigs.map((inp) => {
                const currentVal = sliderValues[inp.symbol] ?? inp.default ?? 1;
                return (
                  <div
                    key={inp.symbol}
                    style={{
                      background: '#f8fafc',
                      border: '1px solid #e2e8f0',
                      padding: '10px 14px',
                      borderRadius: 'var(--radius-sm)',
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                      <span style={{ fontSize: '0.84rem', fontWeight: 600, color: '#1e293b' }}>
                        {inp.label || inp.symbol} {inp.raw_symbol && <span style={{ color: '#0284c7' }}>({inp.raw_symbol})</span>}
                      </span>
                      <span style={{ fontSize: '0.88rem', fontWeight: 700, color: '#0369a1', fontFamily: 'monospace' }}>
                        {currentVal} {inp.unit}
                      </span>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                      <input
                        type="range"
                        min={inp.min ?? 0.1}
                        max={inp.max ?? 50}
                        step={inp.step ?? 0.1}
                        value={currentVal}
                        onChange={(e) => handleSliderChange(inp.symbol, parseFloat(e.target.value))}
                        style={{
                          flex: 1,
                          accentColor: '#0284c7',
                          cursor: 'pointer',
                          height: '6px',
                        }}
                      />
                      <span style={{ fontSize: '0.72rem', color: '#64748b', minWidth: '35px', textAlign: 'right' }}>
                        {inp.max ?? 50} {inp.unit}
                      </span>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Cột Phải: Mô hình trực quan logic & Kết quả */}
            <div
              style={{
                background: '#f0f9ff',
                border: '1px solid #bae6fd',
                borderRadius: 'var(--radius-md)',
                padding: '16px',
                textAlign: 'center',
              }}
            >
              {/* Kết quả số học */}
              <div style={{ marginBottom: '12px' }}>
                <div style={{ fontSize: '0.76rem', fontWeight: 700, color: '#0369a1', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                  {outputName} {outputSymbol ? `(${outputSymbol})` : ''}
                </div>
                <div
                  style={{
                    fontSize: '1.9rem',
                    fontWeight: 900,
                    color: '#0284c7',
                    lineHeight: 1.2,
                    marginTop: '2px',
                    fontFamily: 'monospace',
                  }}
                >
                  {calculatedOutput !== null ? Number(calculatedOutput.toFixed(4)).toLocaleString() : '—'}
                  <span style={{ fontSize: '1rem', fontWeight: 700, color: '#475569', marginLeft: '6px' }}>
                    {outputUnit}
                  </span>
                </div>
                {formula.latex && (
                  <div style={{ fontSize: '0.86rem', color: '#64748b', marginTop: '4px' }}>
                    <MathView latex={formula.latex} />
                  </div>
                )}
              </div>

              {/* Mô hình đồ họa chuyên ngành */}
              <div
                style={{
                  background: '#ffffff',
                  border: '1px solid #bae6fd',
                  borderRadius: 'var(--radius-sm)',
                  padding: '8px',
                  boxShadow: '0 2px 6px rgba(2, 132, 199, 0.05)',
                }}
              >
                {renderLogicalSimulation()}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
