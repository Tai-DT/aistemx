# 🔄 BỘ SƠ ĐỒ LUỒNG HỆ THỐNG & KIẾN TRÚC KỸ THUẬT AISTEM X
**Dự Án**: AISTEM X — Nền tảng Siêu Tri Thức Khoa Học Liên Môn & Gia Sư AI STEM Chuẩn Quốc Tế  
**Tên Miền**: [aistemx.com](https://aistemx.com)  
**Phiên Bản Dự Thi**: 1.0.0 (Production Ready)  

---

## 📑 MỤC LỤC SƠ ĐỒ
1. [Sơ Đồ Kiến Trúc Hệ Thống Tổng Thể (Overall System Architecture)](#1-sơ-đồ-kiến-trúc-hệ-thống-tổng-thể)
2. [Sơ Đồ Luồng Dữ Liệu & Đồ Thị Tri Thức 4 Kho (Knowledge Graph Data Flow)](#2-sơ-đồ-luồng-dữ-liệu--đồ-thị-tri-thức-4-kho)
3. [Luồng Gia Sư AI Socratic & Kiểm Chứng CAS Chống Ảo Giác (Anti-Hallucination Sequence)](#3-luồng-gia-sư-ai-socratic--kiểm-chứng-cas-chống-ảo-giác)
4. [Luồng Nhận Diện Đề Bài Đa Phương Thức (Multimodal Vision Solve Flow)](#4-luồng-nhận-diện-đề-bài-đa-phương-thức)
5. [Luồng Thuật Toán Ghi Nhớ Ngắt Quãng FSRS (Spaced Repetition Flow)](#5-luồng-thuật-toán-ghi-nhớ-ngắt-quãng-fsrs)
6. [Luồng Triển Khai Hạ Tầng Mạng Biên & Zero-Trust (Cloudflare Edge & Local Engine)](#6-luồng-triển-khai-hạ-tầng-mạng-biên--zero-trust)

---

## 1. SƠ ĐỒ KIẾN TRÚC HỆ THỐNG TỔNG THỂ

```mermaid
flowchart TB
    subgraph ClientLayer ["1. CLIENT LAYER (Giao Diện & Tương Tác Học Viên)"]
        UI_Web["AISTEM X Web App (React 19 + Vite 8 + TypeScript)"]
        UI_Formula["Formula Explorer (5,272 Công Thức)"]
        UI_Practice["CAS Practice Lab (4,351 Bài Toán)"]
        UI_Socratic["Gia Sư AI Socratic Modal (3 Chế Độ)"]
        UI_Flashcard["FSRS Spaced Repetition Flashcards"]
        UI_Render["KaTeX + Three.js 3D + Deterministic SVG"]
    end

    subgraph EdgeLayer ["2. GLOBAL EDGE & ZERO-TRUST GATEWAY"]
        CF_DNS["Cloudflare DNS (aistemx.com)"]
        CF_Edge["Cloudflare Edge Cache & DDoS Shield"]
        CF_Tunnel["Cloudflare Zero-Trust Tunnel (QUIC Protocol)"]
        CF_AI["Cloudflare Workers AI (Llama 3.3 70B & Llama 3.2 11B Vision)"]
    end

    subgraph CoreEngine ["3. CORE BACKEND ENGINE (FastAPI / Python 3.13)"]
        API_Gateway["FastAPI Gateway (/api/*, Async & SSE Streaming)"]
        CAS_Engine["SymPy CAS Verification Engine (Giải tích, Đại số, Chống ảo giác)"]
        RAG_Module["Hybrid RAG Pipeline (Full-text Search + Semantic Graph Matching)"]
        Socratic_Router["Socratic Prompt Orchestrator (Foundation / Advanced / Scholarship)"]
        FSRS_Engine["FSRS v4.5 Scheduler (Bộ nhớ ngắt quãng tối ưu)"]
    end

    subgraph StorageLayer ["4. MULTI-MODEL STORAGE & KNOWLEDGE VAULT"]
        PG_DB["PostgreSQL 16 (10,682 Records, tsvector search, 23,482 Edges)"]
        SQLite_Local["SQLite Embedded Engine (aistem.db - Siêu tốc độ cục bộ)"]
        JSON_Corpus["Structured JSON/JSONL Corpus (Schemas & Usage Graph)"]
        Vector_Assets["887 SVG Vectors + 14 Three.js 3D Scenes"]
    end

    UI_Web --> CF_DNS
    CF_DNS --> CF_Edge
    CF_Edge --> CF_Tunnel
    CF_Tunnel --> API_Gateway

    API_Gateway --> CAS_Engine
    API_Gateway --> RAG_Module
    API_Gateway --> Socratic_Router
    API_Gateway --> FSRS_Engine

    Socratic_Router --> CF_AI
    RAG_Module --> PG_DB
    API_Gateway --> SQLite_Local
    CAS_Engine --> SQLite_Local
    UI_Render --> Vector_Assets
```

---

## 2. SƠ ĐỒ LUỒNG DỮ LIỆU & ĐỒ THỊ TRI THỨC 4 KHO

Hệ thống kết nối 4 kho dữ liệu học thuật qua các trường định danh khóa chéo, hình thành một mạng lưới tri thức liên môn (Interdisciplinary Graph):

```mermaid
graph LR
    subgraph FormulasVault ["Kho Công Thức (5,272 Items)"]
        F1["id: math.thpt.giai-tich.dao-ham-tich"]
        F2["id: phys.thpt.co-hoc.con-lac-lo-xo"]
        F3["id: chem.thpt.dong-hoa-hoc.arrhenius"]
    end

    subgraph LessonsVault ["Kho Bài Giảng (1,018 Items)"]
        L1["Bài học Đạo hàm & Ý nghĩa hình học"]
        L2["Bài học Dao động điều hòa"]
        L3["Bài học Động hóa học & Năng lượng hoạt hóa"]
    end

    subgraph ProblemsVault ["Kho Bài Tập CAS (4,351 Items)"]
        P1["Bài toán tiếp tuyến cực trị"]
        P2["Bài toán chu kỳ & con lắc lò xo"]
        P3["Bài toán tính tốc độ phản ứng"]
    end

    subgraph ExamsVault ["Kho Đề Thi Quốc Tế (41 Exams)"]
        E1["AP Calculus BC"]
        E2["IB Physics Higher Level"]
        E3["USNCO National Chemistry"]
        E4["Olympic Vật lý / Toán Quốc Gia"]
    end

    subgraph IllustrationsVault ["Kho Trực Quan Hóa (901 Items)"]
        I1["887 Bản vẽ Vector SVG Toán/Lý/Hóa"]
        I2["14 Mô hình Không gian 3D Three.js"]
    end

    L1 -- "formulas[]" --> F1
    P1 -- "formulas_used[]" --> F1
    E1 -- "formulas_must_memorize[]" --> F1

    L2 -- "formulas[]" --> F2
    P2 -- "formulas_used[]" --> F2
    E2 -- "formulas_must_memorize[]" --> F2

    L3 -- "formulas[]" --> F3
    P3 -- "formulas_used[]" --> F3
    E3 -- "formulas_must_memorize[]" --> F3

    F1 -- "illustrations" --> I1
    F2 -- "scenes3d" --> I2
```

---

## 3. LUỒNG GIA SƯ AI SOCRATIC & KIỂM CHỨNG CAS CHỐNG ẢO GIÁC

Quy trình giải quyết triệt để vấn đề "ảo giác số liệu" (hallucination) thường gặp của LLM trong toán học và khoa học tự nhiên:

```mermaid
sequenceDiagram
    autonumber
    actor Student as Học Sinh (Học Viên)
    participant Client as Web Frontend (AISTEM X)
    participant API as FastAPI Backend Gateway
    participant RAG as RAG & Knowledge Graph
    participant CAS as SymPy CAS Engine
    participant LLM as Cloudflare Workers AI (Llama 3.3)

    Student->>Client: Nhập câu hỏi toán/lý/hóa hoặc bước giải
    Client->>API: POST /api/ai/chat (Message, Mode, Context)
    
    rect rgb(240, 248, 255)
        Note over API, RAG: Bước 1: RAG Đồ Thị Tri Thức
        API->>RAG: Truy xuất công thức & định lý chuẩn liên quan
        RAG-->>API: Danh sách công thức tham chiếu chuẩn xác (Grounding)
    end

    rect rgb(255, 245, 238)
        Note over API, CAS: Bước 2: Kiểm Chứng Ký Hiệu Bằng CAS (Không Ảo Giác)
        API->>CAS: Phân tích biểu thức toán (Đạo hàm, Tích phân, Rút gọn)
        CAS-->>API: Kết quả toán học biểu tượng chuẩn xác 100%
    end

    rect rgb(245, 255, 245)
        Note over API, LLM: Bước 3: Sư Phạm Socratic Theo Chế Độ
        API->>LLM: Gửi Prompt: [Ngữ cảnh CAS + Định lý chuẩn + Câu hỏi + Mode]
        LLM-->>API: Phản hồi Socratic gợi mở tư duy (Không giải hộ)
    end

    API-->>Client: Trả về câu trả lời Socratic + KaTeX chuẩn + CAS Proof
    Client-->>Student: Hiển thị hướng dẫn từng bước trực quan
```

---

## 4. LUỒNG NHẬN DIỆN ĐỀ BÀI ĐA PHƯƠNG THỨC (MULTIMODAL VISION SOLVE)

Cho phép học sinh chụp ảnh đề thi viết tay, biểu đồ hình học hoặc phương trình hóa học phức tạp từ điện thoại/máy tính:

```mermaid
flowchart TD
    A["Học sinh chụp ảnh đề thi / bài giải viết tay"] --> B["AISTEM X App nén & mã hóa Base64 ảnh"]
    B --> C["POST /api/ai/vision-solve"]
    C --> D["Cloudflare Workers AI: Llama 3.2 11B Vision Instruct"]
    
    subgraph VisionPipeline ["Quy trình Xử lý Thị Giác"]
        D --> E["1. Trích xuất đề bài thành văn bản tiếng Việt"]
        D --> F["2. Chuyển đổi công thức toán/hóa thành chuẩn KaTeX ($...$)"]
        D --> G["3. Phân tách: Đại lượng đã cho vs Đại lượng cần tìm"]
    end

    E & F & G --> H["RAG Engine: Đối soát 5,272 công thức trong Knowledge Base"]
    H --> I["SymPy CAS: Xác thực điều kiện nghiệm số"]
    I --> J["Tạo Lộ trình Gợi ý Tư Duy Socratic cho Học sinh"]
    J --> K["Hiển thị màn hình giải đáp với công thức KaTeX sắc nét"]
```

---

## 5. LUỒNG THUẬT TOÁN GHI NHỚ NGẮT QUÃNG FSRS

AISTEM X ứng dụng chuẩn thuật toán **FSRS (Free Spaced Repetition Scheduler)** vượt trội hơn so với SM-2 của Anki, tính toán độ suy giảm trí nhớ dựa trên 3 thông số: Độ khó ($D$), Độ ổn định ($S$), Khả năng nhớ lại ($R$):

```mermaid
stateDiagram-v2
    [*] --> NewCard: Học sinh lưu công thức/khái niệm mới
    
    NewCard --> Learning: Bắt đầu ôn tập lần đầu
    Learning --> Review: Đánh giá kết quả (Again / Hard / Good / Easy)
    
    state Review {
        [*] --> CalculateFSRS
        CalculateFSRS: Tính Stability S và Difficulty D mới
        CalculateFSRS --> NextInterval: Tinh chỉnh khoảng cách lặp lại I = S * 9 * (1/R - 1)
        NextInterval --> Scheduled: Lên lịch ôn tập tối ưu
    }

    Review --> RetrievabilityCheck: Theo dõi đường cong quên Ebbinghaus
    RetrievabilityCheck --> Review: Đến ngày ôn tập định kỳ
    Review --> Mastered: Stability > 180 ngày (Nắm vững vĩnh viễn)
    Mastered --> [*]
```

---

## 6. LUỒNG TRIỂN KHAI HẠ TẦNG MẠNG BIÊN & ZERO-TRUST

Mô hình triển khai hybrid kết hợp Edge Network toàn cầu với Local Dedicated Server:

```mermaid
graph TD
    subgraph GlobalUsers ["Người Dùng Khắp Thế Giới (Web / Mobile / Tablet)"]
        UserVN["Học sinh Việt Nam"]
        UserUS["Học sinh Quốc tế / Du học sinh"]
    end

    subgraph CloudflareGlobalEdge ["Cloudflare Global Anycast Edge (330+ Cities)"]
        EdgeNodes["Edge Proxy & SSL Termination (aistemx.com)"]
        EdgeWAF["WAF & Anti-DDoS Shield"]
        EdgeDNS["DNSSEC Managed Resolver"]
    end

    subgraph TunnelBroker ["Cloudflare Zero-Trust Network Fabric"]
        CFTunnel["Cloudflare Tunnel (Dual QUIC/HTTP3 Virtual Wire)"]
    end

    subgraph LocalOnPremEngine ["AISTEM X Core Server Host"]
        ReverseProxy["Local Service Routing"]
        ViteNode["Frontend Service: Port 5173 (React Single Page App)"]
        FastAPIPython["Backend API Service: Port 8000 (10,682 Records API)"]
        DockerPG["PostgreSQL Database: Port 5434 (Relational & TSVector)"]
    end

    UserVN --> EdgeNodes
    UserUS --> EdgeNodes
    EdgeNodes --> EdgeWAF
    EdgeWAF --> EdgeDNS
    EdgeDNS --> CFTunnel
    CFTunnel --> ReverseProxy
    ReverseProxy -->|Static HTML/CSS/JS| ViteNode
    ReverseProxy -->|API Requests /api/*| FastAPIPython
    FastAPIPython --> DockerPG
```

---
*Tài liệu được thiết kế chuyên biệt cho hồ sơ kỹ thuật tham dự các cuộc thi Khoa học Kỹ thuật, Sáng tạo Khởi nghiệp & Chuyển đổi số.*
