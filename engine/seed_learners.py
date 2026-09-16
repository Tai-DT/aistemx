import json
import random
from aistem.store.postgres import get_postgres_connection, init_postgres_schema

def seed_learners():
    print("Khởi tạo bảng và nạp dữ liệu quản trị học viên...")
    with get_postgres_connection() as conn:
        init_postgres_schema(conn)
        with conn.cursor() as cur:
            # Danh sách học sinh mẫu
            learners = [
                ("hs_01_minhanh", "Nguyễn Minh Anh", "minhanh.nguyen@ams.edu.vn", "THPT Chuyên Hà Nội - Amsterdam", 12, "Artificial Intelligence / MIT", "student"),
                ("hs_02_ducthang", "Trần Đức Thắng", "ducthang.tran@lhp.edu.vn", "THPT Chuyên Lê Hồng Phong TP.HCM", 12, "Quantum Physics / Oxford", "student"),
                ("hs_03_baongoc", "Lê Bảo Ngọc", "baongoc.le@khtn.edu.vn", "THPT Chuyên Khoa Học Tự Nhiên HN", 11, "Bioengineering / Stanford", "student"),
                ("hs_04_quanghuy", "Phạm Quang Huy", "quanghuy.pham@lamson.edu.vn", "THPT Chuyên Lam Sơn Thanh Hóa", 12, "Applied Mathematics / NUS", "student"),
                ("hs_05_thuylinh", "Hoàng Thùy Linh", "thuylinh.hoang@cbn.edu.vn", "THPT Chuyên Bắc Ninh", 11, "Data Science / TU Munich", "student"),
                ("hs_06_viethoang", "Vũ Việt Hoàng", "viethoang.vu@ptnk.edu.vn", "Phổ Thông Năng Khiếu ĐHQG TP.HCM", 12, "Aerospace Engineering / Georgia Tech", "student"),
                ("hs_07_khanhhuyen", "Đỗ Khánh Huyền", "khanhhuyen.do@flss.edu.vn", "THPT Chuyên Ngoại Ngữ", 10, "Computational Biology / Cambridge", "student"),
                ("hs_08_tuananh", "Bùi Tuấn Anh", "tuananh.bui@chuyensp.edu.vn", "THPT Chuyên Đại Học Sư Phạm", 11, "Materials Science / Tokyo Univ", "student"),
                ("admin_root", "Quản Trị Viên AISTEM", "admin@aistem.edu.vn", "AISTEM Center of Excellence", 0, "System Administration", "admin")
            ]

            for l in learners:
                cur.execute("""
                    INSERT INTO learners (id, name, email, school, grade, target_major, role)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET
                        name = EXCLUDED.name,
                        school = EXCLUDED.school,
                        grade = EXCLUDED.grade,
                        target_major = EXCLUDED.target_major,
                        role = EXCLUDED.role;
                """, l)

            # Lấy một số bài toán ngẫu nhiên từ bảng problems
            cur.execute("SELECT id, answer, subject FROM problems LIMIT 60;")
            sample_problems = cur.fetchall()

            if sample_problems:
                # Xoá attempts cũ của các học sinh này nếu có
                learner_ids = [l[0] for l in learners if l[6] == 'student']
                cur.execute("DELETE FROM attempts WHERE learner = ANY(%s);", (learner_ids,))

                for lid in learner_ids:
                    num_attempts = random.randint(15, 35)
                    # Một số bạn giỏi hơn, tỷ lệ đúng cao hơn
                    correct_rate = 0.85 if lid in ["hs_01_minhanh", "hs_02_ducthang", "hs_06_viethoang"] else 0.65
                    chosen = random.sample(sample_problems, min(num_attempts, len(sample_problems)))
                    for pid, ans, subj in chosen:
                        is_correct = random.random() < correct_rate
                        user_ans = ans if is_correct else ("C" if ans != "C" else "A")
                        cur.execute("""
                            INSERT INTO attempts (learner, problem_id, answer, correct, verdict, created_at)
                            VALUES (%s, %s, %s, %s, %s, NOW() - (%s || ' days')::INTERVAL)
                        """, (lid, pid, user_ans, is_correct, 'correct' if is_correct else 'incorrect', random.randint(1, 14)))

            # Nạp hồ sơ học bổng mẫu
            evals = [
                ("hs_01_minhanh", 3.96, 1560, 8.5, ["national_first", "international_olympiad"], ["founder_ai_for_blind"], 2, "tier_1_elite", "Tier 1: Ứng Viên Xuất Sắc Toàn Cầu", 96.5, ["Cần hoàn thiện bài luận Diversity"]),
                ("hs_02_ducthang", 3.92, 1540, 8.0, ["national_second"], ["quantum_sim_open_source"], 1, "tier_1_elite", "Tier 1: Ứng Viên Xuất Sắc Toàn Cầu", 91.0, ["Nâng cao điểm AP Physics C"]),
                ("hs_03_baongoc", 3.88, 1480, 7.5, ["provincial_first"], ["stem_lab_volunteer"], 0, "tier_2_competitive", "Tier 2: Ứng Viên Cạnh Tranh Cao", 82.5, ["Cần bổ sung bài báo khoa học hoặc giải quốc gia"]),
                ("hs_04_quanghuy", 3.90, 1510, 8.0, ["national_third"], ["math_olympiad_coach"], 1, "tier_2_competitive", "Tier 2: Ứng Viên Cạnh Tranh Cao", 86.0, ["Cần bài thi SAT Math II và thư giới thiệu"]),
                ("hs_05_thuylinh", 3.75, 1420, 7.0, ["provincial_second"], ["school_coding_club"], 0, "tier_3_developing", "Tier 3: Ứng Viên Tiềm Năng Cần Bồi Dưỡng", 72.0, ["Cần thi lại SAT nâng lên 1500+", "Nâng IELTS lên 7.5"]),
                ("hs_06_viethoang", 3.94, 1550, 8.0, ["national_first"], ["drone_ai_navigation"], 1, "tier_1_elite", "Tier 1: Ứng Viên Xuất Sắc Toàn Cầu", 93.5, ["Sẵn sàng nộp đơn Early Decision"]),
            ]

            cur.execute("DELETE FROM scholarship_evaluations WHERE learner = ANY(%s);", ([e[0] for e in evals],))
            for e in evals:
                cur.execute("""
                    INSERT INTO scholarship_evaluations 
                    (learner, gpa, sat, ielts, stem_awards, spike_projects, research_papers, tier, tier_name, total_score, gap_analysis)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (
                    e[0], e[1], e[2], e[3], json.dumps(e[4]), json.dumps(e[5]), e[6], e[7], e[8], e[9], json.dumps(e[10])
                ))

        conn.commit()
    print("✅ Đã khởi tạo và nạp dữ liệu mẫu thành công cho hệ thống Admin!")

if __name__ == "__main__":
    seed_learners()
