


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def soultion(sizes):
    ans = 0
    max_width = 0
    max_height = 0

    for size in sizes:
        if size[0] <= size[1]:
            size[0], size[1] = size[1], size[0]
        max_width = max(max_width, size[0])
        max_height = max(max_height, size[1])

    ans = max_height * max_width

    return ans




soultion(sizes)