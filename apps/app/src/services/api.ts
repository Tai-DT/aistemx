/**
 * AISTEM API Client Service
 * Kết nối đồng bộ với Backend FastAPI & PostgreSQL Docker
 */

export interface Formula {
  id: string;
  name?: string;
  name_vi?: string;
  name_en?: string;
  subject: string;
  level?: string;
  topic?: string;
  latex?: string;
  description_vi?: string;
  description_en?: string;
  description?: string;
  vars?: Record<string, string>;
  units?: Record<string, string>;
  variables?: any;
  conditions?: string;
  note?: string;
  python_expr?: string;
  tags?: string[];
  has_illustration_2d?: boolean;
  has_scene_3d?: boolean;
  scene_3d?: any;
  interactive?: any;
}

export interface Choice {
  key: string;
  text: string;
  why_wrong?: string;
}

export interface SolutionStep {
  explain: string;
  latex?: string;
}

export interface Problem {
  id: string;
  subject: string;
  level: string;
  topic: string;
  grades?: number[];
  curriculum?: string[];
  type: string;
  title?: string;
  statement?: string;
  statement_vi: string;
  statement_en?: string;
  answer: string;
  answer_numeric?: number;
  answer_unit?: string;
  tolerance?: number;
  choices?: Choice[];
  solution_steps?: SolutionStep[];
  formulas_used?: string[];
  difficulty: number;
  estimated_minutes?: number;
  skills?: string[];
  hints?: string[];
  tags?: string[];
  cas_verified?: boolean;
  cas_status?: string;
  cas_details?: any;
}

export interface Scholarship {
  id: string;
  name: string;
  country: string;
  provider: string;
  type: string;
  coverage: string;
  financial_value_usd: number;
  gpa_min: number;
  sat_min: number;
  ielts_min: number;
  ap_recommended: number;
  target_majors: string[];
  overview: string;
  official_url: string;
  tags: string[];
}

export interface ReadinessScore {
  total_score: number;
  tier: string;
  tier_name: string;
  breakdown: {
    academics: number;
    stem_awards: number;
    spike_profile: number;
    essays_and_lors: number;
  };
  gap_analysis: string[];
  recommendations: string[];
}

export interface MatchResults {
  student_tier: string;
  total_scholarships_matched: number;
  reach: Array<{ scholarship: Scholarship; match_score: number; rationale: string }>;
  target: Array<{ scholarship: Scholarship; match_score: number; rationale: string }>;
  safety: Array<{ scholarship: Scholarship; match_score: number; rationale: string }>;
}

export interface STARFeedback {
  overall_score: number;
  scores: {
    situation: number;
    task: number;
    action: number;
    result: number;
  };
  components_found: {
    situation: boolean;
    task: boolean;
    action: boolean;
    result: boolean;
  };
  detected_keywords: {
    metrics: string[];
    actions: string[];
    challenges: string[];
  };
  actionable_advice: string[];
}

export interface SystemStats {
  total_records: number;
  formula: number;
  lesson: number;
  problem: number;
  exam: number;
  edges: number;
  illustrations: number;
  scholarships: number;
  problems: number;
  problems_cas_verified: number;
}

const API_BASE = '/api';

export const api = {
  // Thống kê hệ thống
  getStats: async (): Promise<SystemStats> => {
    try {
      const res = await fetch(`${API_BASE}/stats`);
      return await res.json();
    } catch {
      return {
        total_records: 10654,
        formula: 5272,
        lesson: 990,
        problem: 4351,
        exam: 41,
        edges: 22286,
        illustrations: 655,
        scholarships: 25,
        problems: 4351,
        problems_cas_verified: 259,
      };
    }
  },

  // Công thức
  getFormulas: async (params: { subject?: string; level?: string; topic?: string; q?: string; has_illustration?: boolean; page?: number; page_size?: number } = {}) => {
    const query = new URLSearchParams();
    if (params.subject) query.set('subject', params.subject);
    if (params.level) query.set('level', params.level);
    if (params.topic) query.set('topic', params.topic);
    if (params.q) query.set('q', params.q);
    if (params.has_illustration !== undefined) query.set('has_illustration', String(params.has_illustration));
    if (params.page) query.set('page', String(params.page));
    if (params.page_size) query.set('page_size', String(params.page_size));
    const res = await fetch(`${API_BASE}/formulas?${query.toString()}`);
    return await res.json();
  },

  getFormulaById: async (formulaId: string) => {
    const res = await fetch(`${API_BASE}/formulas/${encodeURIComponent(formulaId)}`);
    return await res.json();
  },


  // Bài tập (PostgreSQL)
  getProblems: async (params: { subject?: string; level?: string; type?: string; difficulty?: number; topic?: string; q?: string; cas_verified?: boolean; page?: number; page_size?: number } = {}) => {
    const query = new URLSearchParams();
    if (params.subject) query.set('subject', params.subject);
    if (params.level) query.set('level', params.level);
    if (params.type) query.set('type', params.type);
    if (params.difficulty) query.set('difficulty', String(params.difficulty));
    if (params.topic) query.set('topic', params.topic);
    if (params.q) query.set('q', params.q);
    if (params.cas_verified !== undefined) query.set('cas_verified', String(params.cas_verified));
    if (params.page) query.set('page', String(params.page));
    if (params.page_size) query.set('page_size', String(params.page_size));
    const res = await fetch(`${API_BASE}/problems?${query.toString()}`);
    return await res.json();
  },

  getProblemDetail: async (id: string): Promise<Problem> => {
    const res = await fetch(`${API_BASE}/problems/${id}`);
    return await res.json();
  },

  verifyProblemCAS: async (id: string) => {
    const res = await fetch(`${API_BASE}/problems/${id}/verify-cas`, { method: 'POST' });
    return await res.json();
  },

  // Học bổng
  getScholarships: async (params: { country?: string; coverage?: string; q?: string } = {}) => {
    const query = new URLSearchParams();
    if (params.country) query.set('country', params.country);
    if (params.coverage) query.set('coverage', params.coverage);
    if (params.q) query.set('q', params.q);
    const res = await fetch(`${API_BASE}/scholarships?${query.toString()}`);
    return await res.json();
  },

  evaluateReadiness: async (profile: { gpa: number; sat?: number; ielts?: number; stem_awards?: string[]; spike_projects?: string[]; research_papers?: number; leadership_roles?: string[]; essay_readiness?: number }) => {
    const res = await fetch(`${API_BASE}/scholarships/readiness`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(profile),
    });
    return await res.json();
  },

  matchScholarships: async (profile: any) => {
    const res = await fetch(`${API_BASE}/scholarships/match`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(profile),
    });
    return await res.json();
  },

  getInterviewQuestions: async () => {
    const res = await fetch(`${API_BASE}/scholarships/interview/questions`);
    return await res.json();
  },

  evaluateInterviewAnswer: async (question_id: string, answer: string): Promise<STARFeedback> => {
    const res = await fetch(`${API_BASE}/scholarships/interview/evaluate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question_id, answer }),
    });
    return await res.json();
  },

  // Ghi nhận lượt làm bài
  recordAttempt: async (payload: { learner?: string; problem_id: string; answer: string; correct: boolean; verdict?: string }) => {
    try {
      await fetch(`${API_BASE}/practice/attempt`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ learner: payload.learner || 'hs_01_minhanh', ...payload }),
      });
    } catch {
      // ignore
    }
  },

  // Student Auth APIs
  loginStudent: async (username_or_email: string, password: string) => {
    const res = await fetch(`${API_BASE}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username_or_email, password }),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: 'Đăng nhập không thành công' }));
      throw new Error(err.detail || 'Tên đăng nhập hoặc mật khẩu không chính xác');
    }
    return await res.json();
  },

  registerStudent: async (username: string, email: string, password: string, full_name?: string) => {
    const res = await fetch(`${API_BASE}/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, email, password, full_name }),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: 'Đăng ký không thành công' }));
      throw new Error(err.detail || 'Không thể đăng ký tài khoản');
    }
    return await res.json();
  },

  // Admin APIs
  loginAdmin: async (username: string, password: string) => {
    const res = await fetch(`${API_BASE}/admin/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || 'Đăng nhập không thành công');
    }
    return await res.json();
  },

  getAdminOverview: async () => {
    const res = await fetch(`${API_BASE}/admin/overview`);
    return await res.json();
  },

  getAdminLearners: async (q?: string) => {
    const query = q ? `?q=${encodeURIComponent(q)}` : '';
    const res = await fetch(`${API_BASE}/admin/learners${query}`);
    return await res.json();
  },

  getAdminLearnerDetail: async (learnerId: string) => {
    const res = await fetch(`${API_BASE}/admin/learners/${learnerId}`);
    return await res.json();
  },

  // Bài học (Lessons)
  getLessons: async (params: { subject?: string; level?: string; grade?: number; curriculum?: string; page?: number; page_size?: number } = {}) => {
    const query = new URLSearchParams();
    if (params.subject) query.set('subject', params.subject);
    if (params.level) query.set('level', params.level);
    if (params.grade) query.set('grade', String(params.grade));
    if (params.curriculum) query.set('curriculum', params.curriculum);
    if (params.page) query.set('page', String(params.page));
    if (params.page_size) query.set('page_size', String(params.page_size));
    const res = await fetch(`${API_BASE}/lessons?${query.toString()}`);
    return await res.json();
  },

  getLessonDetail: async (id: string) => {
    const res = await fetch(`${API_BASE}/lessons/${id}`);
    return await res.json();
  },

  // Đề thi chuẩn hoá (Exams)
  getExams: async () => {
    const res = await fetch(`${API_BASE}/exams`);
    return await res.json();
  },

  getExamDetail: async (id: string) => {
    const res = await fetch(`${API_BASE}/exams/${id}`);
    return await res.json();
  },

  // Gia sư AI AISTEM X
  explainWithAI: async (topic: string, content: string, targetAudience?: string) => {
    const res = await fetch(`${API_BASE}/ai/explain`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ topic, content, target_audience: targetAudience }),
    });
    return await res.json();
  },

  getAiHint: async (problemId: string, studentAnswer?: string, stepIndex: number = 1) => {
    const res = await fetch(`${API_BASE}/ai/hint`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        problem_id: problemId,
        student_answer: studentAnswer,
        step_index: stepIndex,
      }),
    });
    if (!res.ok) throw new Error('Không thể lấy gợi ý AI');
    return await res.json();
  },

  visionSolve: async (imageBase64: string, prompt?: string) => {
    const res = await fetch(`${API_BASE}/ai/vision-solve`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        image_base64: imageBase64,
        prompt: prompt,
      }),
    });
    if (!res.ok) throw new Error('Lỗi nhận diện thị giác AI');
    return await res.json();
  },

  saveFlashcardFromAi: async (card: { front: string; back: string; latex?: string; subject?: string; topic?: string }) => {
    const res = await fetch(`${API_BASE}/ai/save-flashcard`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(card),
    });
    return await res.json();
  },

  evalCas: async (expression: string, operation: string = 'solve', variable: string = 'x') => {
    const res = await fetch(`${API_BASE}/ai/cas-eval`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ expression, operation, variable }),
    });
    return await res.json();
  },

  // Sinh lộ trình học từ gốc rễ (Roadmap DAG)
  generateRoadmap: async (params: {
    goal: string;
    subject?: string;
    level?: string;
    curriculum?: string;
    learner?: string;
    known_lessons?: string[];
    weak_skills?: string[];
    practice_per_lesson?: number;
    minutes_per_session?: number;
    max_lessons?: number;
  }): Promise<LearningRoadmap> => {
    const res = await fetch(`${API_BASE}/roadmap`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(params),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: 'Lỗi máy chủ' }));
      throw new Error(err.detail || 'Không thể tạo lộ trình');
    }
    return await res.json();
  },

  // Tự động sinh bài toán STEM từ Prompt với CAS kiểm chứng độc lập
  generateProblem: async (params: {
    prompt: string;
    subject?: string;
    level?: string;
    difficulty?: number;
    model?: 'deepseek-r1' | 'llama-3.3' | 'qwq-32b';
  }): Promise<AIGeneratedProblemResult> => {
    const res = await fetch(`${API_BASE}/ai/generate-problem`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(params),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: 'Lỗi máy chủ khi sinh bài toán' }));
      throw new Error(err.detail || 'Không thể tạo bài toán từ AI');
    }
    return await res.json();
  },

  // Vẽ minh họa toán học & khoa học bằng AI Cloudflare (FLUX.1 & SVG Vector)
  aiDraw: async (prompt: string, mode: 'svg' | 'flux' | 'both' = 'both', subject: string = 'math'): Promise<{
    success: boolean;
    prompt: string;
    svg?: string | null;
    image_url?: string | null;
    mode: string;
  }> => {
    const res = await fetch(`${API_BASE}/ai/draw`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, mode, subject }),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: 'Không thể tạo hình ảnh minh họa' }));
      throw new Error(err.detail || 'Lỗi khi vẽ hình AI');
    }
    return await res.json();
  },
};


export interface AIGeneratedProblemResult {
  success: boolean;
  problem: Problem;
  cas_verified: boolean;
  cas_status: string;
  cas_details: any;
  illustration_url?: string | null;
  thinking?: string;
  model_used: string;
}

export interface RoadmapMilestone {
  order: number;
  lesson: {
    kind: string;
    id: string;
    title: string;
    minutes: number;
    difficulty?: number;
    subject?: string;
    level?: string;
    topic?: string;
    reason?: string;
  };
  practice: Array<{
    kind: string;
    id: string;
    title: string;
    minutes: number;
    difficulty?: number;
    subject?: string;
    level?: string;
    topic?: string;
    reason?: string;
  }>;
  unit: string;
  prerequisites_met: string[];
}

export interface RoadmapStudySession {
  index: number;
  items: Array<{
    kind: string;
    id: string;
    title: string;
    minutes: number;
    difficulty?: number;
    subject?: string;
    reason?: string;
  }>;
  minutes: number;
}

export interface LearningRoadmap {
  goal: string;
  goal_lessons: string[];
  milestones: RoadmapMilestone[];
  sessions: RoadmapStudySession[];
  total_minutes: number;
  total_hours?: number;
  lesson_count: number;
  practice_count: number;
  skipped_known: number;
  truncated: boolean;
  subjects: string[];
  summary: string;
  warnings: string[];
}

