import unicodedata


_canvas = []
_canvas_height = 0
_canvas_width = 0


def resize(width, height):
    global _canvas_width
    global _canvas_height

    assert width >= 0
    assert height >= 0

    while len(_canvas) < height:
        _canvas.append([])
    _canvas[:] = _canvas[:height]

    for row in _canvas:
        while len(row) < width:
            row.append(0)
        row[:] = row[:width]

    _canvas_width = width
    _canvas_height = height


def clear():
    for row in _canvas:
        for x in range(_canvas_width):
            row[x] = 0


def pixel(x, y, v = 1):
    if 0 <= y < _canvas_height and 0 <= x < _canvas_width:
        _canvas[y][x] = v


def line(x1, y1, x2, y2, v = 1):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    x, y = x1, y1
    pixel(x, y, v)
    while not(x == x2 and y == y2):
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
        pixel(x, y, v)


# def rect(x1, y1, x2, y2, v = 1):
#     if x1 > x2:
#         x1, x2 = x2, x1
#     if y1 > y2:
#         y1, y2 = y2, y1

#     for x in range(x1, x2 + 1):
#         set_pixel(x, y1, v)
#     for x in range(x1, x2 + 1):
#         set_pixel(x, y2, v)
#     for y in range(y1, y2 + 1):
#         set_pixel(x1, y, v)
#     for y in range(y1, y2 + 1):
#         set_pixel(x2, y, v)


def text(x, y, text):
    x0 = x // 2 * 2
    y0 = y // 4 * 4

    if 0 <= y0 < _canvas_height and 0 <= x0 < _canvas_width:
        _canvas[y0][x0] = text


BRAILLE_PATTERNS_DOT_OFFSETS = [
    (0, 0), (0, 1), (0, 2), (1, 0), 
    (1, 1), (1, 2), (0, 3), (1, 3),
]


def show(file=None):
    for y0 in range(0, _canvas_height, 4):
        row = []
        for x0 in range(0, _canvas_width, 2):
            c = 0
            v = 1
            for x, y in BRAILLE_PATTERNS_DOT_OFFSETS:
                if y + y0 < _canvas_height and x + x0 < _canvas_width and _canvas[y + y0][x + x0] == 1:
                    c += v
                v = v << 1
            row.append(chr(0x2800 + c))
        for x0 in range(0, _canvas_width, 2):
            t = _canvas[y0][x0]
            if isinstance(t, str):
                cx = x = x0 // 2
                for ch in t:
                    if x >= _canvas_width // 2:
                        break
                    if unicodedata.east_asian_width(ch) in ["W", "F", "A"]:
                        row[cx:cx + 2] = [ch]
                        x += 2
                    else:
                        row[cx:cx + 1] = [ch]
                        x += 1
                    cx += 1
        print("".join(row), file=file)


if __name__ == '__main__':
    import importlib
    bc = importlib.import_module(__name__)  # このモジュール自身をインポートする

    bc.resize(40, 40)
    for y in range(0, 40 + 1, 10):
        bc.line(0, 0, 40, y, 1)
    bc.text(10, 20, "Line drawing")
    bc.text(10, 30, "線を引くデモ")
    bc.show()
