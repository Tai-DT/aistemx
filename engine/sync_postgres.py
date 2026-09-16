#!/usr/bin/env python3
"""Script đồng bộ toàn diện dữ liệu AISTEM từ SQLite và JSON Vaults vào PostgreSQL trên Docker."""
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "engine") not in sys.path:
    sys.path.insert(0, str(ROOT / "engine"))

from aistem.config import settings
from aistem.store.postgres import (
    get_postgres_connection,
    init_postgres_schema,
    migrate_sqlite_to_postgres,
    migrate_scholarships_to_postgres,
    migrate_problems_to_postgres,
    migrate_interactive_to_postgres,
    get_postgres_summary,
)


def main():
    print("=" * 65)
    print("⚡ KHỞI TẠO & ĐỒNG BỘ DỮ LIỆU AISTEM VÀO POSTGRESQL TRÊN DOCKER")
    print("=" * 65)

    pg_url = os.environ.get("AISTEM_POSTGRES_URL") or settings.postgres_url
    print(f"📌 Địa chỉ kết nối: {pg_url}")

    sqlite_db = settings.database
    if not sqlite_db.exists():
        print(f"❌ Không tìm thấy file SQLite: {sqlite_db}")
        sys.exit(1)
    print(f"📂 Nguồn SQLite: {sqlite_db} ({sqlite_db.stat().st_size / (1024*1024):.2f} MB)")

    scholarships_file = ROOT / "data" / "scholarships" / "scholarships.json"
    print(f"🎓 Nguồn Học bổng: {scholarships_file}")

    print("\n1. Đang kết nối tới PostgreSQL và khởi tạo cấu trúc bảng...")
    t0 = time.perf_counter()
    with get_postgres_connection(pg_url) as conn:
        init_postgres_schema(conn)
        print("   ✅ Đã khởi tạo schema, GIN indexes và extension thành công.")

        print("\n2. Đang nạp toàn bộ bản ghi (Formulas, Lessons, Problems, Exams, Edges, Skills)...")
        report = migrate_sqlite_to_postgres(sqlite_db, conn, batch_size=1500)
        print(f"   ✅ Đã đồng bộ {report['records']:,} bản ghi trong {report['elapsed_seconds']}s.")
        print(f"   - Liên kết cạnh (Edges): {report['edges']:,}")
        print(f"   - Kỹ năng bài tập (Problem Skills): {report['problem_skills']:,}")
        print(f"   - Tokens kỹ năng (Skill Tokens): {report['skill_tokens']:,}")
        print(f"   - Minh họa công thức (Illustrations): {report['illustrations']:,}")

        print("\n3. Đang nạp cơ sở dữ liệu 25 Học bổng Toàn phần & Tinh hoa Toàn cầu...")
        sch_count = migrate_scholarships_to_postgres(scholarships_file, conn)
        print(f"   ✅ Đã đồng bộ {sch_count} chương trình học bổng toàn cầu.")

        print("\n4. Đang nạp cơ sở dữ liệu Chuyên sâu 4,351 Bài toán STEM (PostgreSQL Table)...")
        prob_dir = ROOT / "data" / "problems"
        prob_count = migrate_problems_to_postgres(prob_dir, conn)
        print(f"   ✅ Đã đồng bộ {prob_count:,} bài toán với đầy đủ JSONB, steps, choices và TSVector.")

        print("\n5. Đang nạp cơ sở dữ liệu Tham số Tương tác 5,272 Công thức (Interactive Math Engine)...")
        interactive_file = ROOT / "data" / "interactive" / "index.json"
        inter_count = migrate_interactive_to_postgres(interactive_file, conn)
        print(f"   ✅ Đã đồng bộ {inter_count:,} cấu hình công thức tương tác vào PostgreSQL.")

        print("\n6. Kiểm tra thống kê dữ liệu thực tế trên PostgreSQL:")
        stats = get_postgres_summary(conn)
        print("   " + "-" * 50)
        print(f"   * Công thức (Formulas):      {stats.get('formula', 0):,}")
        print(f"   * Bài giảng (Lessons):       {stats.get('lesson', 0):,}")
        print(f"   * Bài tập (Problems):        {stats.get('problem', 0):,}")
        print(f"   * Kỳ thi (Exams):            {stats.get('exam', 0):,}")
        print(f"   * TỔNG SỐ BẢN GHI (Records): {stats.get('total_records', 0):,}")
        print(f"   * Đồ thị cạnh (Edges):       {stats.get('edges', 0):,}")
        print(f"   * Kỹ năng (Problem Skills):  {stats.get('problem_skills', 0):,}")
        print(f"   * Minh họa 2D/3D:            {stats.get('illustrations', 0):,}")
        print(f"   * Học bổng (Scholarships):   {stats.get('scholarships', 0):,}")
        print(f"   * Bảng Problems Chuyên sâu:  {stats.get('problems', 0):,}")
        print(f"   * CAS Verified:              {stats.get('problems_cas_verified', 0):,}")
        print(f"   * Công thức Tương tác (All): {stats.get('formula_interactive', 0):,}")
        print(f"   * Tương tác Động (Sliders):  {stats.get('interactive_computable', 0):,}")
        print("   " + "-" * 50)

    total_time = time.perf_counter() - t0
    print(f"\n🎉 HOÀN TẤT ĐỒNG BỘ TOÀN BỘ DỮ LIỆU SANG POSTGRESQL TRONG {total_time:.2f} GIÂY!\n")


if __name__ == "__main__":
    main()
