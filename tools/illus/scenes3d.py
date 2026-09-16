"""Engine dựng scene 3D khai báo (định dạng ``aistem-scene-1``).

Mỗi scene là một dict JSON thuần: camera + helper (trục/lưới) + danh sách ``objects``.
Object thuộc một tập kiểu nguyên thuỷ mà viewer three.js dựng trực tiếp
(``vector, line, point, sphere, box, plane, mesh, label``). Các hình cong
(mặt z=f(x,y), khối tròn xoay, đường cong tham số) được "bake" sẵn thành ``mesh``/
``line`` trong Python nên viewer không cần đánh giá biểu thức.

Quy ước trục: toán học (x, y, z=f) ↦ thế giới three.js (X=x, Y=z, Z=y) — trục tung
Y là "lên". Generator đăng ký trong ``REGISTRY``; ``render(type, params)`` trả scene.
"""

from __future__ import annotations

import math
from typing import Callable, Iterable

from .mathexpr import compile_expr

VERSION = "aistem-scene-1"

# Bảng màu (hex) — viewer tự lo nền sáng/tối, vật thể giữ màu ổn định.
COL = {
    "x": "#dc2626", "y": "#16a34a", "z": "#2563eb",
    "a": "#2563eb", "b": "#dc2626", "c": "#16a34a", "d": "#d97706",
    "surface": "#2563eb", "solid": "#7c3aed", "curve": "#d97706",
    "atom": "#64748b", "bond": "#94a3b8", "nucleus": "#dc2626",
    "flux": "#0ea5e9", "ink": "#334155",
}

Vec = tuple[float, float, float]
Params = dict


# --------------------------------------------------------------------------
# tiện ích vectơ + bake lưới
# --------------------------------------------------------------------------
def _sub(a, b): return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
def _add(a, b): return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
def _dot(a, b): return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def _norm(a): return math.sqrt(_dot(a, a))


def _round3(x: float) -> float:
    return round(float(x), 4)


def grid_mesh(point_fn: Callable[[int, int], Vec], nu: int, nv: int,
              color: str, opacity: float = 1.0, wireframe: bool = False) -> dict:
    """Bake một lưới (nu+1)×(nv+1) đỉnh thành object ``mesh`` (tam giác hoá)."""
    positions: list[float] = []
    for i in range(nu + 1):
        for j in range(nv + 1):
            x, y, z = point_fn(i, j)
            positions += [_round3(x), _round3(y), _round3(z)]
    indices: list[int] = []
    stride = nv + 1
    for i in range(nu):
        for j in range(nv):
            a = i * stride + j
            b = a + 1
            c = a + stride
            d = c + 1
            indices += [a, c, b, b, c, d]
    return {
        "type": "mesh", "positions": positions, "indices": indices,
        "color": color, "opacity": opacity, "wireframe": wireframe, "side": "double",
    }


# --------------------------------------------------------------------------
# object nguyên thuỷ (helper tạo dict)
# --------------------------------------------------------------------------
def vector(frm: Vec, to: Vec, color: str, label: str = "") -> dict:
    return {"type": "vector", "from": [_round3(v) for v in frm],
            "to": [_round3(v) for v in to], "color": color, "label": label}


def point(at: Vec, color: str, label: str = "", size: float = 0.14) -> dict:
    return {"type": "point", "at": [_round3(v) for v in at], "color": color,
            "label": label, "size": size}


def sphere(at: Vec, radius: float, color: str, opacity: float = 1.0) -> dict:
    return {"type": "sphere", "at": [_round3(v) for v in at], "radius": _round3(radius),
            "color": color, "opacity": opacity}


def line(points: Iterable[Vec], color: str, dashed: bool = False) -> dict:
    return {"type": "line", "points": [[_round3(c) for c in p] for p in points],
            "color": color, "dashed": dashed}


def label(at: Vec, text: str, color: str = COL["ink"]) -> dict:
    return {"type": "label", "at": [_round3(v) for v in at], "text": text, "color": color}


def scene(sid: str, title_vi: str, objects: list[dict], *, camera: Vec = (6, 5, 8),
          target: Vec = (0, 0, 0), axes: float | None = 4.0, grid: float | None = 8.0,
          formula_id: str | None = None, caption_vi: str = "",
          axis_labels: list[str] | None = None) -> dict:
    helpers: dict = {}
    if axes:
        helpers["axes"] = {"size": axes, "labels": axis_labels or ["x", "y", "z"]}
    if grid:
        helpers["grid"] = {"size": grid, "divisions": int(grid)}
    return {
        "version": VERSION,
        "id": sid,
        "title_vi": title_vi,
        "formula_id": formula_id,
        "caption_vi": caption_vi,
        "camera": {"position": [_round3(v) for v in camera],
                   "target": [_round3(v) for v in target], "fov": 45, "up": [0, 1, 0]},
        "background": "auto",
        "helpers": helpers,
        "objects": objects,
    }


# --------------------------------------------------------------------------
# generator scene
# --------------------------------------------------------------------------
def build_coordinate_frame(p: Params) -> dict:
    pt = tuple(p.get("point", [2, 3, 2]))
    objs = [
        line([(0, 0, 0), (pt[0], 0, 0)], COL["x"], dashed=True),
        line([(pt[0], 0, 0), (pt[0], 0, pt[2])], COL["y"], dashed=True),
        line([(pt[0], 0, pt[2]), (pt[0], pt[1], pt[2])], COL["z"], dashed=True),
        vector((0, 0, 0), (pt[0], pt[1], pt[2]), COL["a"], "r"),
        point((pt[0], pt[1], pt[2]), COL["b"], f"({pt[0]}, {pt[2]}, {pt[1]})"),
    ]
    return scene("coordinate_frame", "Điểm trong hệ toạ độ Oxyz", objs,
                 camera=(6, 5, 8), caption_vi=p.get("caption_vi", ""),
                 formula_id=p.get("formula_id"))


def build_vector3d(p: Params) -> dict:
    vecs = p.get("vectors", [[3, 2, 1], [1, 3, 2]])
    colors = [COL["a"], COL["c"], COL["d"], COL["b"]]
    labels = p.get("labels", ["a", "b", "c", "d"])
    objs = []
    for i, v in enumerate(vecs):
        objs.append(vector((0, 0, 0), tuple(v), colors[i % len(colors)], labels[i % len(labels)]))
    if p.get("resultant", False) and len(vecs) >= 2:
        r = (sum(v[0] for v in vecs), sum(v[1] for v in vecs), sum(v[2] for v in vecs))
        objs.append(vector((0, 0, 0), r, COL["b"], p.get("resultant_label", "Σ")))
    return scene("vector3d", p.get("title_vi", "Vectơ trong không gian"), objs,
                 caption_vi=p.get("caption_vi", ""), formula_id=p.get("formula_id"))


def build_cross_product(p: Params) -> dict:
    a = tuple(p.get("a", [3, 1, 0]))
    b = tuple(p.get("b", [1, 3, 0]))
    axb = _cross(a, b)
    # thu nhỏ tích có hướng cho vừa khung nếu quá dài
    n = _norm(axb)
    disp = axb
    if n > 5:
        disp = tuple(c / n * 4 for c in axb)
    objs = [
        vector((0, 0, 0), a, COL["a"], "a"),
        vector((0, 0, 0), b, COL["c"], "b"),
        # hình bình hành dựng trên a, b (diện tích = |a×b|)
        grid_mesh(lambda i, j: _add(tuple(a[k] * i for k in range(3)),
                                    tuple(b[k] * j for k in range(3))),
                  1, 1, COL["d"], opacity=0.25),
        vector((0, 0, 0), disp, COL["b"], "a×b"),
    ]
    return scene("cross_product", "Tích có hướng a × b", objs,
                 camera=(6, 6, 7),
                 caption_vi=p.get("caption_vi", "|a×b| = diện tích hình bình hành; a×b ⊥ (a, b)."),
                 formula_id=p.get("formula_id"))


def build_parallelepiped(p: Params) -> dict:
    a = tuple(p.get("a", [3, 0, 0]))
    b = tuple(p.get("b", [1, 3, 0]))
    c = tuple(p.get("c", [1, 1, 3]))
    vol = abs(_dot(a, _cross(b, c)))
    O = (0, 0, 0)
    verts = {
        "O": O, "a": a, "b": b, "c": c,
        "ab": _add(a, b), "ac": _add(a, c), "bc": _add(b, c), "abc": _add(_add(a, b), c),
    }
    faces = [  # mỗi mặt là 1 grid 1×1 theo hai vectơ cạnh
        (O, a, b), (O, a, c), (O, b, c),
        (c, a, b), (b, a, c), (a, b, c),
    ]
    objs: list[dict] = []
    for origin, u, v in faces:
        objs.append(grid_mesh(
            lambda i, j, o=origin, uu=u, vv=v: _add(o, _add(tuple(uu[k] * i for k in range(3)),
                                                            tuple(vv[k] * j for k in range(3)))),
            1, 1, COL["solid"], opacity=0.16))
    objs += [
        vector(O, a, COL["a"], "a"),
        vector(O, b, COL["c"], "b"),
        vector(O, c, COL["z"], "c"),
        label(verts["abc"], f"V = |a·(b×c)| = {_round3(vol)}"),
    ]
    return scene("parallelepiped", "Hình hộp — tích hỗn tạp", objs, camera=(7, 6, 8),
                 caption_vi=p.get("caption_vi", "Thể tích hình hộp = trị tuyệt đối tích hỗn tạp a·(b×c)."),
                 formula_id=p.get("formula_id"))


def build_surface(p: Params) -> dict:
    expr = str(p.get("expr", "x^2 - y^2"))
    umin, umax = p.get("u", [-2.2, 2.2])
    vmin, vmax = p.get("v", [-2.2, 2.2])
    res = int(p.get("res", 34))
    fn = compile_expr(expr, ("x", "y"))

    def pt(i, j):
        x = umin + (umax - umin) * i / res
        y = vmin + (vmax - vmin) * j / res
        try:
            z = fn(x, y)
        except (ValueError, ZeroDivisionError, OverflowError):
            z = 0.0
        if not math.isfinite(z):
            z = 0.0
        return (x, z, y)  # math (x,y,z) -> world (X=x, Y=z, Z=y)

    mesh = grid_mesh(pt, res, res, COL["surface"], opacity=0.92)
    objs = [mesh, label((umax, fn_safe(fn, umax, vmax), vmax), f"z = {expr}")]
    span = max(umax - umin, vmax - vmin)
    cam = (span * 1.6, span * 1.3, span * 1.9)
    return scene("surface", p.get("title_vi", f"Mặt z = {expr}"), objs,
                 camera=cam, axes=span, grid=None, axis_labels=["x", "z", "y"],
                 caption_vi=p.get("caption_vi", "Đồ thị hàm hai biến z = f(x, y)."),
                 formula_id=p.get("formula_id"))


def fn_safe(fn, x, y):
    try:
        z = fn(x, y)
        return z if math.isfinite(z) else 0.0
    except Exception:  # noqa: BLE001
        return 0.0


def build_solid_revolution(p: Params) -> dict:
    """Khối tròn xoay: quay đường y = f(x), x∈[a,b], quanh trục Ox."""
    expr = str(p.get("expr", "sqrt(x)"))
    a, b = p.get("domain", [0.2, 4])
    nu = int(p.get("res_x", 40))
    nt = int(p.get("res_theta", 36))
    fn = compile_expr(expr, ("x",))

    def pt(i, j):
        x = a + (b - a) * i / nu
        r = fn_safe(fn, x, 0)
        th = 2 * math.pi * j / nt
        # trục quay là Ox (thế giới X); bán kính trải trên mặt phẳng Y-Z
        return (x, r * math.cos(th), r * math.sin(th))

    solid = grid_mesh(pt, nu, nt, COL["solid"], opacity=0.55)
    # đường sinh f(x) nằm trên mặt phẳng y (world Y)
    gen_curve = [(a + (b - a) * i / nu, fn_safe(fn, a + (b - a) * i / nu, 0), 0) for i in range(nu + 1)]
    objs = [solid, line(gen_curve, COL["curve"]), label((b, 0, 0), f"y = {expr}")]
    span = max(b - a, 2 * max(fn_safe(fn, b, 0), 1))
    return scene("solid_revolution", f"Khối tròn xoay quanh Ox: y = {expr}", objs,
                 camera=(b * 1.1, span, span * 1.4), axes=max(b + 1, 4), grid=None,
                 caption_vi=p.get("caption_vi", "Thể tích V = π∫f(x)² dx (quay quanh trục Ox)."),
                 formula_id=p.get("formula_id"))


def build_sphere_flux(p: Params) -> dict:
    """Mặt cầu Gauss + vectơ trường hướng tâm (điện trường điểm / thông lượng)."""
    R = float(p.get("R", 2.5))
    objs = [
        sphere((0, 0, 0), R, COL["flux"], opacity=0.2),
        point((0, 0, 0), COL["nucleus"], "+q", size=0.2),
    ]
    dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
            (0.7, 0.7, 0), (0.7, 0, 0.7), (0, 0.7, 0.7), (-0.7, 0.7, 0)]
    for d in dirs:
        n = _norm(d)
        u = tuple(ci / n for ci in d)
        objs.append(vector(tuple(ci * R for ci in u), tuple(ci * (R + 1.1) for ci in u),
                           COL["flux"], ""))
    return scene("sphere_flux", "Mặt Gauss & điện trường hướng tâm", objs,
                 camera=(6, 5, 7), axes=R + 1.5, grid=None,
                 caption_vi=p.get("caption_vi", "Thông lượng qua mặt cầu Φ = q/ε₀; E hướng tâm, đều trên mặt cầu."),
                 formula_id=p.get("formula_id"))


def build_wave_surface(p: Params) -> dict:
    """Mặt sóng z = A·sin(kx − ωt) (chụp tại một thời điểm)."""
    A = float(p.get("A", 0.8))
    k = float(p.get("k", 1.2))
    expr = f"{A}*sin({k}*x)"
    return build_surface({
        "expr": expr, "u": [-3.2, 3.2], "v": [-3.2, 3.2], "res": 40,
        "title_vi": "Mặt sóng phẳng", "formula_id": p.get("formula_id"),
        "caption_vi": p.get("caption_vi", "Sóng phẳng lan theo Ox; mỗi điểm dao động điều hoà."),
    })


def build_atom_bohr(p: Params) -> dict:
    """Mẫu nguyên tử Bohr: hạt nhân + các quỹ đạo tròn mang electron."""
    shells = int(p.get("shells", 3))
    objs = [sphere((0, 0, 0), 0.45, COL["nucleus"], opacity=1.0), label((0, 0.7, 0), "hạt nhân")]
    for s in range(1, shells + 1):
        r = 1.0 + 1.1 * s
        ring = [(r * math.cos(2 * math.pi * t / 72),
                 0.0,
                 r * math.sin(2 * math.pi * t / 72)) for t in range(73)]
        # nghiêng mỗi quỹ đạo một chút cho có chiều sâu
        tilt = math.radians(18 * s)
        ring = [(x, y * math.cos(tilt) - z * math.sin(tilt), y * math.sin(tilt) + z * math.cos(tilt))
                for (x, y, z) in ring]
        objs.append(line(ring, COL["bond"]))
        objs.append(sphere(ring[0], 0.2, COL["z"], opacity=1.0))
    return scene("atom_bohr", "Mẫu nguyên tử Bohr", objs, camera=(7, 5, 7), axes=None, grid=None,
                 caption_vi=p.get("caption_vi", "Electron chuyển động trên các lớp; bán kính rₙ ∝ n²."),
                 formula_id=p.get("formula_id"))


def build_molecule(p: Params) -> dict:
    """Mô hình bi-que từ danh sách nguyên tử và liên kết."""
    atoms = p.get("atoms", [
        {"at": [0, 0, 0], "r": 0.5, "color": COL["atom"], "label": "C"},
        {"at": [1.2, 0.8, 0], "r": 0.32, "color": "#e2e8f0", "label": "H"},
        {"at": [-1.2, 0.8, 0], "r": 0.32, "color": "#e2e8f0", "label": "H"},
        {"at": [0, -1, 1], "r": 0.32, "color": "#e2e8f0", "label": "H"},
        {"at": [0, -0.3, -1.3], "r": 0.32, "color": "#e2e8f0", "label": "H"},
    ])
    bonds = p.get("bonds", [[0, 1], [0, 2], [0, 3], [0, 4]])
    objs: list[dict] = []
    for a in atoms:
        objs.append(sphere(tuple(a["at"]), a.get("r", 0.4), a.get("color", COL["atom"])))
        if a.get("label"):
            objs.append(label(_add(tuple(a["at"]), (0, a.get("r", 0.4) + 0.25, 0)), a["label"]))
    for i, j in bonds:
        objs.append(line([tuple(atoms[i]["at"]), tuple(atoms[j]["at"])], COL["bond"]))
    return scene("molecule", p.get("title_vi", "Mô hình phân tử (bi-que)"), objs,
                 camera=(5, 4, 6), axes=None, grid=None,
                 caption_vi=p.get("caption_vi", ""), formula_id=p.get("formula_id"))


def build_plane_normal(p: Params) -> dict:
    """Mặt phẳng trong không gian Oxyz và vectơ pháp tuyến n = (A, B, C)."""
    pt = tuple(p.get("point", [1.0, 1.0, 1.0]))  # (x, z, y)
    n_vec = tuple(p.get("normal", [1.5, 2.5, 1.0]))
    n_len = _norm(n_vec) or 1.0
    nn = tuple(c / n_len for c in n_vec)
    # tìm hai vectơ u, v vuông góc với nn và trực giao nhau
    arb = (0.0, 1.0, 0.0) if abs(nn[1]) < 0.9 else (1.0, 0.0, 0.0)
    u_raw = _cross(nn, arb)
    u_len = _norm(u_raw) or 1.0
    u = tuple(c / u_len for c in u_raw)
    v = _cross(nn, u)
    span = float(p.get("size", 2.8))
    # dựng lưới phẳng 2x2
    def plane_pt(i, j):
        ui = (i - 1) * span
        vj = (j - 1) * span
        return (pt[0] + ui * u[0] + vj * v[0],
                pt[1] + ui * u[1] + vj * v[1],
                pt[2] + ui * u[2] + vj * v[2])

    mesh_plane = grid_mesh(plane_pt, 2, 2, COL["surface"], opacity=0.35)
    objs = [
        mesh_plane,
        point(pt, COL["b"], "M₀", size=0.15),
        vector(pt, _add(pt, n_vec), COL["b"], "n = (A, B, C)"),
        label(_add(pt, (u[0] * span * 0.8, u[1] * span * 0.8, u[2] * span * 0.8)),
              p.get("equation", "Ax + By + Cz + D = 0")),
    ]
    return scene("plane_normal", p.get("title_vi", "Mặt phẳng và vectơ pháp tuyến"), objs,
                 camera=(6, 5, 7), caption_vi=p.get("caption_vi", "Vectơ pháp tuyến n vuông góc với mọi vectơ nằm trong mặt phẳng."),
                 formula_id=p.get("formula_id"))


def build_sphere_geometry(p: Params) -> dict:
    """Mặt cầu tâm I bán kính R và mặt phẳng tiếp diện tại điểm tiếp xúc M."""
    center = tuple(p.get("center", [0.0, 1.5, 0.0]))
    R = float(p.get("R", 2.0))
    M = _add(center, (R * 0.7071, R * 0.7071, 0.0))
    rad_vec = _sub(M, center)
    rad_len = _norm(rad_vec) or 1.0
    nn = tuple(c / rad_len for c in rad_vec)
    arb = (0.0, 0.0, 1.0)
    u_raw = _cross(nn, arb)
    u_len = _norm(u_raw) or 1.0
    u = tuple(c / u_len for c in u_raw)
    v = _cross(nn, u)
    span = 1.6
    def tan_pt(i, j):
        ui = (i - 1) * span
        vj = (j - 1) * span
        return (M[0] + ui * u[0] + vj * v[0],
                M[1] + ui * u[1] + vj * v[1],
                M[2] + ui * u[2] + vj * v[2])

    objs = [
        sphere(center, R, COL["surface"], opacity=0.28),
        point(center, COL["x"], "I(a, b, c)", size=0.15),
        point(M, COL["b"], "M(x₀, y₀, z₀)", size=0.14),
        vector(center, M, COL["a"], "R"),
        grid_mesh(tan_pt, 2, 2, COL["d"], opacity=0.35),
        label(_add(center, (0, -R - 0.4, 0)), f"(x-a)² + (y-b)² + (z-c)² = R²"),
    ]
    return scene("sphere_geometry", p.get("title_vi", "Mặt cầu và tiếp diện trong Oxyz"), objs,
                 camera=(6, 5, 7), caption_vi=p.get("caption_vi", "Tiếp diện vuông góc với bán kính IM tại tiếp điểm M."),
                 formula_id=p.get("formula_id"))


def build_tetrahedron(p: Params) -> dict:
    """Khối tứ diện vuông OABC hoặc tứ diện đều trong không gian."""
    a = float(p.get("a", 3.0))
    b = float(p.get("b", 2.5))
    c = float(p.get("c", 3.2))
    O = (0.0, 0.0, 0.0)
    A = (a, 0.0, 0.0)
    B = (0.0, 0.0, b)
    C = (0.0, c, 0.0)  # C trên trục tung
    # Tạo 4 mặt tam giác
    verts = [O, A, B, C]
    pos = []
    for v in verts:
        pos += [_round3(v[0]), _round3(v[1]), _round3(v[2])]
    # 4 mặt: OAB, OBC, OCA, ABC
    idx = [0, 2, 1,  0, 3, 2,  0, 1, 3,  1, 2, 3]
    vol = a * b * c / 6.0
    objs = [
        {"type": "mesh", "positions": pos, "indices": idx, "color": COL["solid"], "opacity": 0.3, "wireframe": False, "side": "double"},
        line([O, A], COL["ink"]), line([O, B], COL["ink"]), line([O, C], COL["ink"]),
        line([A, B], COL["ink"]), line([B, C], COL["ink"]), line([C, A], COL["ink"]),
        point(O, COL["ink"], "O", size=0.12),
        point(A, COL["a"], "A", size=0.12),
        point(B, COL["c"], "B", size=0.12),
        point(C, COL["x"], "C", size=0.12),
        label((a * 0.35, c * 0.4, b * 0.35), f"V = ⅙abc = {_round3(vol)}"),
    ]
    return scene("tetrahedron", p.get("title_vi", "Khối tứ diện vuông O.ABC"), objs,
                 camera=(6, 5, 7), caption_vi=p.get("caption_vi", "Thể tích tứ diện vuông đỉnh O: V = ⅙·OA·OB·OC."),
                 formula_id=p.get("formula_id"))


def build_octahedron(p: Params) -> dict:
    """Khối bát diện đều 8 mặt tam giác đều."""
    a = float(p.get("a", 2.2))
    verts = [
        (a, 0.0, 0.0), (-a, 0.0, 0.0),
        (0.0, a, 0.0), (0.0, -a, 0.0),
        (0.0, 0.0, a), (0.0, 0.0, -a),
    ]
    pos = []
    for v in verts:
        pos += [_round3(v[0]), _round3(v[1]), _round3(v[2])]
    idx = [
        2, 0, 4,  2, 4, 1,  2, 1, 5,  2, 5, 0,
        3, 4, 0,  3, 1, 4,  3, 5, 1,  3, 0, 5,
    ]
    edges = [
        (0, 2), (0, 3), (0, 4), (0, 5),
        (1, 2), (1, 3), (1, 4), (1, 5),
        (4, 2), (2, 5), (5, 3), (3, 4),
    ]
    objs: list[dict] = [
        {"type": "mesh", "positions": pos, "indices": idx, "color": COL["surface"], "opacity": 0.38, "wireframe": False, "side": "double"}
    ]
    for i, j in edges:
        objs.append(line([verts[i], verts[j]], COL["ink"]))
    vol = (a ** 3) * math.sqrt(2) / 3.0 * (math.sqrt(2) ** 3)  # a_edge = a*sqrt(2)
    objs.append(label((0.0, a + 0.4, 0.0), "Khối bát diện đều (8 mặt tam giác đều)"))
    return scene("octahedron", p.get("title_vi", "Khối bát diện đều {3, 4}"), objs,
                 camera=(5, 4, 6), caption_vi=p.get("caption_vi", "Khối đa diện đều loại {3,4} gồm 6 đỉnh, 12 cạnh, 8 mặt tam giác đều."),
                 formula_id=p.get("formula_id"))


def build_helix(p: Params) -> dict:
    """Đường xoắn ốc không gian r(t) = (R·cos t, c·t, R·sin t) và vectơ tiếp tuyến."""
    R = float(p.get("R", 2.0))
    c = float(p.get("pitch", 0.35))
    turns = float(p.get("turns", 2.5))
    num_pts = 120
    pts = []
    for i in range(num_pts + 1):
        t = 2.0 * math.pi * turns * i / num_pts
        pts.append((R * math.cos(t), c * t, R * math.sin(t)))

    t0 = 2.0 * math.pi * 1.5
    P0 = (R * math.cos(t0), c * t0, R * math.sin(t0))
    tan_v = (-R * math.sin(t0), c, R * math.cos(t0))
    objs = [
        line(pts, COL["curve"]),
        line([(0.0, 0.0, 0.0), (0.0, c * 2 * math.pi * turns, 0.0)], COL["ink"], dashed=True),
        point(P0, COL["b"], "M(t)", size=0.15),
        vector(P0, _add(P0, tan_v), COL["b"], "r'(t) (tiếp tuyến)"),
        label(_add(P0, (0.4, 0.4, 0.0)), "r(t) = (R·cos t, c·t, R·sin t)"),
    ]
    return scene("helix", p.get("title_vi", "Đường xoắn ốc 3D và vectơ tiếp tuyến"), objs,
                 camera=(6, 5, 8), caption_vi=p.get("caption_vi", "Vectơ tiếp tuyến r'(t) tiếp xúc với đường cong không gian tại mỗi điểm."),
                 formula_id=p.get("formula_id"))


REGISTRY: dict[str, Callable[[Params], dict]] = {
    "coordinate_frame": build_coordinate_frame,
    "vector3d": build_vector3d,
    "cross_product": build_cross_product,
    "parallelepiped": build_parallelepiped,
    "surface": build_surface,
    "solid_revolution": build_solid_revolution,
    "sphere_flux": build_sphere_flux,
    "wave_surface": build_wave_surface,
    "atom_bohr": build_atom_bohr,
    "molecule": build_molecule,
    "plane_normal": build_plane_normal,
    "sphere_geometry": build_sphere_geometry,
    "tetrahedron": build_tetrahedron,
    "octahedron": build_octahedron,
    "helix": build_helix,
}


def render(scene_type: str, params: Params | None = None) -> dict:
    if scene_type not in REGISTRY:
        raise KeyError(f"scene 3D không tồn tại: {scene_type}")
    return REGISTRY[scene_type](params or {})


# --------------------------------------------------------------------------
# kiểm định scene
# --------------------------------------------------------------------------
_PRIMS = {"vector", "line", "point", "sphere", "box", "plane", "mesh", "label"}


def validate_scene(s: dict) -> list[str]:
    """Trả danh sách vấn đề (rỗng nếu hợp lệ) cho một scene dict."""
    problems: list[str] = []
    if s.get("version") != VERSION:
        problems.append(f"version sai: {s.get('version')!r} (cần {VERSION!r})")
    cam = s.get("camera", {})
    for key in ("position", "target"):
        v = cam.get(key)
        if not (isinstance(v, list) and len(v) == 3):
            problems.append(f"camera.{key} phải là [x,y,z]")
    objs = s.get("objects")
    if not isinstance(objs, list) or not objs:
        problems.append("objects rỗng")
        return problems
    for i, o in enumerate(objs):
        t = o.get("type")
        if t not in _PRIMS:
            problems.append(f"object[{i}] kiểu lạ: {t!r}")
            continue
        if t == "mesh":
            pos = o.get("positions")
            idx = o.get("indices")
            if not isinstance(pos, list) or len(pos) % 3 != 0 or not pos:
                problems.append(f"object[{i}] mesh.positions không hợp lệ")
            if not isinstance(idx, list) or len(idx) % 3 != 0:
                problems.append(f"object[{i}] mesh.indices không chia hết 3")
            elif idx and max(idx) >= len(pos) // 3:
                problems.append(f"object[{i}] mesh.indices vượt số đỉnh")
        elif t == "vector":
            for key in ("from", "to"):
                if not (isinstance(o.get(key), list) and len(o[key]) == 3):
                    problems.append(f"object[{i}] vector.{key} phải [x,y,z]")
        elif t == "line":
            pts = o.get("points")
            if not (isinstance(pts, list) and all(len(q) == 3 for q in pts)):
                problems.append(f"object[{i}] line.points không hợp lệ")
    return problems
