from PIL import Image


def get_julia(zoom, center_x, center_y, dx, dy,
              iterations=200, width=1024, height=1024):
    img = Image.new("RGB", (width, height))
    res = img.load()

    for x in range(width):
        for y in range(height):
            zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + center_x
            zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + center_y
            i = iterations
            while zx * zx + zy * zy < 4 and i > 1:
                tmp = zx * zx - zy * zy + dx
                zy, zx = 2.0 * zx * zy + dy, tmp
                i -= 1
            res[x, y] = (i << 32) + (i << 5) + i * 10
            # res[x, y] = (i << 21) + (i << 10) + i * 8
    return img


def get_mandelbrot(min_x, min_y, max_x, max_y,
                   iterations=100, width=1024, height=1024):
    image = Image.new("RGB", (width, height))

    for y in range(height):
        zy = y * (max_y - min_y) / (height - 1) + min_y
        for x in range(width):
            zx = x * (max_x - min_x) / (width - 1) + min_x
            z = zx + zy * 1j
            c = z
            for i in range(iterations):
                print(abs(z))
                if abs(z) > 2.0:
                    break
                z = z * z + c
            # image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))
            image.putpixel((x, y), (i % 4 * 40, i % 8 * 40, i % 16 * 40))
    return image


def main():
    # mandelbrot
    min_x = -2.5
    max_x = 1.0
    min_y = -1.5
    max_y = 1.5
    mandel = get_mandelbrot(min_x, min_y, max_x, max_y)

    # julia
    zoom = 1.5
    dx, dy = -0.7, 0.27015
    # jull = get_julia(zoom, 0.0, 0.0, dx, dy)

    mandel.show()
    # jull.show()


main()
