#!/usr/bin/env python3
"""Quản lý Cơ sở Dữ liệu Người dùng, Xác thực và Tiến độ Học tập AISTEM."""
from __future__ import annotations

import hashlib
import hmac
import secrets
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "users.db"
SECRET_KEY = "aistem-super-secret-key-for-jwt-and-session-tokens"


def get_db():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Khởi tạo các bảng cơ sở dữ liệu nếu chưa tồn tại."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with get_db() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            full_name TEXT,
            avatar TEXT DEFAULT '👨‍🎓',
            xp INTEGER DEFAULT 100,
            streak_days INTEGER DEFAULT 1,
            role TEXT DEFAULT 'student',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS sessions (
            token TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            problem_id TEXT NOT NULL,
            subject TEXT NOT NULL,
            user_answer TEXT,
            is_correct INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            problem_id TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, problem_id),
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS tournaments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            subject TEXT NOT NULL,
            entry_fee INTEGER NOT NULL DEFAULT 99000,
            min_participants INTEGER NOT NULL DEFAULT 30,
            max_participants INTEGER DEFAULT 200,
            prize_pool INTEGER NOT NULL DEFAULT 5000000,
            prize_desc TEXT,
            status TEXT DEFAULT 'REGISTERING', -- REGISTERING, ACTIVE, COMPLETED, CANCELLED
            duration_minutes INTEGER DEFAULT 60,
            total_questions INTEGER DEFAULT 20,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS tournament_registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tournament_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            payment_status TEXT DEFAULT 'PAID', -- PENDING, PAID, REFUNDED
            payment_code TEXT UNIQUE NOT NULL,
            fee_paid INTEGER NOT NULL,
            score INTEGER DEFAULT 0,
            time_spent_seconds INTEGER DEFAULT 0,
            has_submitted INTEGER DEFAULT 0,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(tournament_id, user_id),
            FOREIGN KEY (tournament_id) REFERENCES tournaments (id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS ai_training_dataset (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            instruction TEXT NOT NULL,
            input_context TEXT DEFAULT '',
            response TEXT NOT NULL,
            subject TEXT DEFAULT 'stem',
            pedagogical_mode TEXT DEFAULT 'socratic',
            rating INTEGER DEFAULT 1,
            feedback_text TEXT DEFAULT '',
            cas_verified INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        conn.commit()


def hash_password(password: str) -> str:
    salt = "aistem_salt_2026"
    return hashlib.sha256((password + salt).encode("utf-8")).hexdigest()


def register_user(username: str, email: str, password: str, full_name: str = "") -> dict:
    pwd_hash = hash_password(password)
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password_hash, full_name) VALUES (?, ?, ?, ?)",
            (username.strip(), email.strip().lower(), pwd_hash, full_name.strip() or username)
        )
        user_id = cursor.lastrowid
        conn.commit()

        token = secrets.token_hex(24)
        cursor.execute("INSERT INTO sessions (token, user_id) VALUES (?, ?)", (token, user_id))
        conn.commit()

        return {
            "token": token,
            "user": {
                "id": user_id,
                "username": username,
                "email": email,
                "full_name": full_name or username,
                "avatar": "👨‍🎓",
                "xp": 100,
                "streak_days": 1,
                "role": "student"
            }
        }


def login_user(username_or_email: str, password: str) -> Optional[dict]:
    pwd_hash = hash_password(password)
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE (username = ? OR email = ?) AND password_hash = ?",
            (username_or_email.strip(), username_or_email.strip().lower(), pwd_hash)
        )
        row = cursor.fetchone()
        if not row:
            return None

        user_id = row["id"]
        token = secrets.token_hex(24)
        cursor.execute("INSERT INTO sessions (token, user_id) VALUES (?, ?)", (token, user_id))
        conn.commit()

        return {
            "token": token,
            "user": {
                "id": user_id,
                "username": row["username"],
                "email": row["email"],
                "full_name": row["full_name"],
                "avatar": row["avatar"],
                "xp": row["xp"],
                "streak_days": row["streak_days"],
                "role": row["role"]
            }
        }


def get_user_from_token(token: str) -> Optional[dict]:
    if not token:
        return None
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT u.* FROM users u 
               JOIN sessions s ON u.id = s.user_id 
               WHERE s.token = ?""",
            (token.strip(),)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return {
            "id": row["id"],
            "username": row["username"],
            "email": row["email"],
            "full_name": row["full_name"],
            "avatar": row["avatar"],
            "xp": row["xp"],
            "streak_days": row["streak_days"],
            "role": row["role"]
        }


def record_submission(user_id: int, problem_id: str, subject: str, user_answer: str, is_correct: bool):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO submissions (user_id, problem_id, subject, user_answer, is_correct) VALUES (?, ?, ?, ?, ?)",
            (user_id, problem_id, subject, user_answer, 1 if is_correct else 0)
        )
        # Tăng điểm XP nếu làm đúng (+15 XP)
        if is_correct:
            cursor.execute("UPDATE users SET xp = xp + 15 WHERE id = ?", (user_id,))
        conn.commit()


def toggle_bookmark(user_id: int, problem_id: str) -> bool:
    """Trả về True nếu bài đã được bookmark, False nếu đã bỏ bookmark."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM bookmarks WHERE user_id = ? AND problem_id = ?", (user_id, problem_id))
        row = cursor.fetchone()
        if row:
            cursor.execute("DELETE FROM bookmarks WHERE user_id = ? AND problem_id = ?", (user_id, problem_id))
            conn.commit()
            return False
        else:
            cursor.execute("INSERT INTO bookmarks (user_id, problem_id) VALUES (?, ?)", (user_id, problem_id))
            conn.commit()
            return True


def get_user_bookmarks(user_id: int) -> list[str]:
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT problem_id FROM bookmarks WHERE user_id = ? ORDER BY created_at DESC", (user_id,))
        return [row["problem_id"] for row in cursor.fetchall()]


def get_user_analytics(user_id: int) -> dict:
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) as total, SUM(is_correct) as correct FROM submissions WHERE user_id = ?", (user_id,))
        stats = cursor.fetchone()
        total_sub = stats["total"] or 0
        correct_sub = stats["correct"] or 0

        # Submissions by subject
        cursor.execute(
            "SELECT subject, COUNT(*) as count, SUM(is_correct) as correct FROM submissions WHERE user_id = ? GROUP BY subject",
            (user_id,)
        )
        by_subj = {}
        for r in cursor.fetchall():
            by_subj[r["subject"]] = {
                "total": r["count"],
                "correct": r["correct"] or 0,
                "accuracy": round((r["correct"] or 0) / r["count"] * 100, 1) if r["count"] else 0
            }

        return {
            "total_submissions": total_sub,
            "correct_submissions": correct_sub,
            "accuracy_rate": round(correct_sub / total_sub * 100, 1) if total_sub else 0,
            "by_subject": by_subj,
        }


def get_all_users() -> list[dict]:
    """Lấy danh sách toàn bộ người dùng cho trang quản trị."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.id, u.username, u.email, u.full_name, u.role, u.xp, u.streak_days, u.created_at,
                   COUNT(s.id) as submissions_count,
                   SUM(CASE WHEN s.is_correct = 1 THEN 1 ELSE 0 END) as correct_count
            FROM users u
            LEFT JOIN submissions s ON u.id = s.user_id
            GROUP BY u.id
            ORDER BY u.id ASC
        """)
        return [dict(row) for row in cursor.fetchall()]


def update_user_role(user_id: int, new_role: str):
    """Cập nhật quyền của người dùng (student, teacher, admin)."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET role = ? WHERE id = ?", (new_role, user_id))
        conn.commit()


def get_system_audit_stats() -> dict:
    """Thống kê tổng hợp toàn hệ thống cho Admin Dashboard."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) as total_users FROM users")
        total_users = cursor.fetchone()["total_users"] or 0

        cursor.execute("SELECT COUNT(*) as total_sub, SUM(is_correct) as correct_sub FROM submissions")
        sub_stats = cursor.fetchone()
        total_sub = sub_stats["total_sub"] or 0
        correct_sub = sub_stats["correct_sub"] or 0

        cursor.execute("""
            SELECT username, full_name, xp, streak_days 
            FROM users 
            ORDER BY xp DESC 
            LIMIT 5
        """)
        top_students = [dict(row) for row in cursor.fetchall()]

        return {
            "total_users": total_users,
            "total_submissions": total_sub,
            "correct_submissions": correct_sub,
            "overall_accuracy": round(correct_sub / total_sub * 100, 1) if total_sub else 0,
            "top_students": top_students
        }


def get_leaderboard_rankings(limit: int = 20) -> list:
    """Bảng xếp hạng học viên toàn cầu theo điểm thưởng XP và chuỗi streak."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.id, u.username, u.full_name, u.role, u.xp, u.streak_days,
                   COUNT(s.id) as total_submissions,
                   SUM(CASE WHEN s.is_correct = 1 THEN 1 ELSE 0 END) as correct_submissions
            FROM users u
            LEFT JOIN submissions s ON u.id = s.user_id
            WHERE u.role != 'admin'
            GROUP BY u.id
            ORDER BY u.xp DESC, u.streak_days DESC
            LIMIT ?
        """, (limit,))
        rows = cursor.fetchall()
        rankings = []
        for rank, row in enumerate(rows, start=1):
            r = dict(row)
            r["rank"] = rank
            total_sub = r["total_submissions"] or 0
            corr_sub = r["correct_submissions"] or 0
            r["accuracy"] = round(corr_sub / total_sub * 100, 1) if total_sub > 0 else 0
            rankings.append(r)
        return rankings


def list_tournaments() -> list:
    """Lấy danh sách tất cả các giải đấu kèm số lượng thí sinh đã đăng ký."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT t.*, 
                   COUNT(r.id) as current_participants,
                   SUM(CASE WHEN r.payment_status = 'PAID' THEN r.fee_paid ELSE 0 END) as total_revenue
            FROM tournaments t
            LEFT JOIN tournament_registrations r ON t.id = r.tournament_id
            GROUP BY t.id
            ORDER BY t.id DESC
        """)
        rows = cursor.fetchall()
        tournaments = []
        for row in rows:
            t = dict(row)
            curr = t["current_participants"]
            min_p = t["min_participants"]
            t["quota_percentage"] = min(100, round(curr / min_p * 100, 1)) if min_p > 0 else 100
            t["is_quota_met"] = curr >= min_p
            tournaments.append(t)
        return tournaments


def get_tournament_by_id(tournament_id: int, user_id: Optional[int] = None) -> Optional[dict]:
    """Lấy chi tiết giải đấu và trạng thái đăng ký của user hiện tại."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT t.*, 
                   COUNT(r.id) as current_participants
            FROM tournaments t
            LEFT JOIN tournament_registrations r ON t.id = r.tournament_id
            WHERE t.id = ?
            GROUP BY t.id
        """, (tournament_id,))
        row = cursor.fetchone()
        if not row:
            return None
        t = dict(row)
        curr = t["current_participants"]
        min_p = t["min_participants"]
        t["quota_percentage"] = min(100, round(curr / min_p * 100, 1)) if min_p > 0 else 100
        t["is_quota_met"] = curr >= min_p

        t["user_registered"] = False
        t["user_payment_status"] = None
        if user_id:
            cursor.execute("""
                SELECT * FROM tournament_registrations 
                WHERE tournament_id = ? AND user_id = ?
            """, (tournament_id, user_id))
            reg = cursor.fetchone()
            if reg:
                t["user_registered"] = True
                t["user_payment_status"] = reg["payment_status"]
                t["has_submitted"] = bool(reg["has_submitted"])
                t["score"] = reg["score"]
        return t


def register_user_tournament(user_id: int, tournament_id: int) -> dict:
    """Đăng ký tham gia giải đấu và tạo mã thanh toán."""
    with get_db() as conn:
        cursor = conn.cursor()
        # Kiểm tra giải đấu
        cursor.execute("SELECT * FROM tournaments WHERE id = ?", (tournament_id,))
        t = cursor.fetchone()
        if not t:
            raise ValueError("Giải đấu không tồn tại")

        # Kiểm tra đã đăng ký chưa
        cursor.execute("SELECT * FROM tournament_registrations WHERE tournament_id = ? AND user_id = ?", (tournament_id, user_id))
        if cursor.fetchone():
            raise ValueError("Bạn đã đăng ký tham gia giải đấu này rồi")

        payment_code = f"AISTEM-T{tournament_id}-U{user_id}-{secrets.token_hex(3).upper()}"
        cursor.execute("""
            INSERT INTO tournament_registrations (tournament_id, user_id, payment_status, payment_code, fee_paid)
            VALUES (?, ?, 'PAID', ?, ?)
        """, (tournament_id, user_id, payment_code, t["entry_fee"]))
        
        # Thưởng 50 XP cho việc đăng ký tham gia giải đấu
        cursor.execute("UPDATE users SET xp = xp + 50 WHERE id = ?", (user_id,))
        conn.commit()

        return {
            "success": True,
            "payment_code": payment_code,
            "fee_paid": t["entry_fee"],
            "tournament_id": tournament_id
        }


def get_tournament_leaderboard(tournament_id: int) -> list:
    """Bảng xếp hạng điểm thi của giải đấu."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.id, u.username, u.full_name, r.score, r.time_spent_seconds, r.has_submitted, r.registered_at
            FROM tournament_registrations r
            JOIN users u ON r.user_id = u.id
            WHERE r.tournament_id = ? AND r.payment_status = 'PAID'
            ORDER BY r.score DESC, r.time_spent_seconds ASC
        """, (tournament_id,))
        rows = cursor.fetchall()
        rankings = []
        for rank, row in enumerate(rows, start=1):
            r = dict(row)
            r["rank"] = rank
            rankings.append(r)
        return rankings


def seed_tournaments_if_empty():
    """Khởi tạo các giải đấu có phí mẫu nếu chưa có."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) as cnt FROM tournaments")
        if cursor.fetchone()["cnt"] == 0:
            cursor.execute("""
                INSERT INTO tournaments (title, description, subject, entry_fee, min_participants, max_participants, prize_pool, prize_desc, status, duration_minutes, total_questions)
                VALUES 
                ('AISTEM Grand Prix Season 1: Đấu Trường Olympic Toán & Vật Lí Quốc Tế', 
                 'Giải đấu đỉnh cao quy tụ học sinh chuyên toán - lý cả nước. Yêu cầu tối thiểu 30 thí sinh đăng ký để chính thức mở phòng thi đấu.', 
                 'math', 99000, 30, 200, 5000000, 'Top 1: 2,500,000đ + Cúp Vàng · Top 2: 1,500,000đ · Top 3: 1,000,000đ', 'REGISTERING', 60, 25),
                
                ('STEM World Championship: Chinh Phục Thử Thách Hoá Sinh Toàn Cầu', 
                 'Đấu trường kiểm tra năng lực phản ứng chuỗi Polymerase, di truyền Mendel và cấu trúc orbital. Yêu cầu tối thiểu 50 thí sinh.', 
                 'chemistry', 149000, 50, 300, 10000000, 'Top 1: 5,000,000đ + Kỷ niệm chương · Top 2: 3,000,000đ · Top 3: 2,000,000đ', 'REGISTERING', 90, 30)
            """)
            conn.commit()


def create_admin_if_not_exists():
    """Tạo tài khoản quản trị mặc định nếu chưa có."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = 'admin'")
        if not cursor.fetchone():
            pwd_hash = hash_password("admin123456")
            cursor.execute("""
                INSERT INTO users (username, email, password_hash, full_name, role, xp)
                VALUES ('admin', 'admin@aistem.vn', ?, 'Quản Trị Viên AISTEM', 'admin', 9999)
            """, (pwd_hash,))
            conn.commit()


def save_ai_training_sample(
    instruction: str,
    response: str,
    input_context: str = "",
    subject: str = "stem",
    pedagogical_mode: str = "socratic",
    rating: int = 1,
    feedback_text: str = "",
    cas_verified: bool = False,
) -> int:
    """Lưu mẫu hội thoại chuẩn hóa (instruction, input, output) phục vụ Fine-tuning LoRA sau này."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ai_training_dataset 
            (instruction, input_context, response, subject, pedagogical_mode, rating, feedback_text, cas_verified)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                instruction.strip(),
                input_context.strip(),
                response.strip(),
                subject,
                pedagogical_mode,
                rating,
                feedback_text.strip(),
                1 if cas_verified else 0,
            ),
        )
        conn.commit()
        return cursor.lastrowid


def get_ai_training_dataset(min_rating: int = 1, limit: int = 1000) -> list[dict[str, Any]]:
    """Trích xuất tập dữ liệu Gold Dataset chuẩn format Alpaca/ShareGPT phục vụ huấn luyện mô hình."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, instruction, input_context, response, subject, pedagogical_mode, rating, cas_verified, created_at
            FROM ai_training_dataset
            WHERE rating >= ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (min_rating, limit),
        )
        rows = cursor.fetchall()
        return [dict(r) for r in rows]


# Khởi tạo DB ngay khi import
init_db()
create_admin_if_not_exists()
seed_tournaments_if_empty()



