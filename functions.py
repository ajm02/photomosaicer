class ImageTooSmallError(Exception):

    def __init__(self, message):
        super().__init__(message)

def dividing_size(width, height, size_const):
    width_multiple = (width // size_const) * size_const
    width_remainder = width % size_const

    if width_remainder >= size_const / 2:
        width_multiple += size_const

    height_multiple = (height // size_const) * size_const
    height_remainder = height % size_const

    if height_remainder >= size_const / 2:
        height_multiple += size_const

    together = (width_multiple, height_multiple)
    return together

def average_rgb(image, side_length):
    totalr = 0
    totalg = 0
    totalb = 0

    for j in range(0, side_length):
        for k in range(0, side_length):
            r, g, b, a = image.getpixel((j, k))
            totalr += r
            totalg += g
            totalb += b

    squared_length = side_length * side_length
    average = (round(totalr / squared_length), round(totalg / squared_length), round(totalb / squared_length))
    return average


