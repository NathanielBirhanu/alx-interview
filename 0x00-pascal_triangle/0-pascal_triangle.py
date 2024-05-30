def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        triangle.append(current_row)

    return triangle


def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(", ".join(str(x) for x in row)))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
