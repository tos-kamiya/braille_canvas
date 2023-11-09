import braille_canvas as bc

SIZE_X = 100
SIZE_Y = 80
ORIGIN_X = 50
ORIGIN_Y = 40

SCALE = 20

# キャンバスのサイズを設定
bc.resize(SIZE_X, SIZE_Y)

# x軸
bc.line(0, ORIGIN_Y, SIZE_X, ORIGIN_Y, 1)
bc.text(SIZE_X - 4, ORIGIN_Y + 4, "x")

# y軸
bc.line(ORIGIN_X, 0, ORIGIN_X, SIZE_Y, 1)
bc.text(ORIGIN_X + 4, 4, "y")

# 点の座標を表示
bc.text(ORIGIN_X + 4, ORIGIN_Y + 4, "0")  # 原点
bc.text(int(1 * SCALE) + ORIGIN_X, ORIGIN_Y + 4, "1")  # (1, 0)
bc.text(int(-1 * SCALE) + ORIGIN_X, ORIGIN_Y + 4, "-1")  # (-1, 0)
bc.text(ORIGIN_X + 4, ORIGIN_Y + int(-1 * SCALE), "1")  # (0, 1)
bc.text(ORIGIN_X + 4, ORIGIN_Y + int(1 * SCALE), "-1")  # (0, -1)

# 放物線を描く
for sx in range(0, SIZE_X):
    x = (sx - ORIGIN_X) / SCALE
    y = x ** 2
    sy = ORIGIN_Y + int(-y * SCALE)
    bc.pixel(sx, sy, 1)

# キャンバスを表示
bc.show()
