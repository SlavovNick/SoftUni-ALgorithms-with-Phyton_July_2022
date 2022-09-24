def find_path(row, col, direction, lab, path):
    if row >= len(lab) or row < 0 or col >= len(lab[0]) or col < 0 or lab[row][col] == '*' or lab[row][col] == 'v':
        return

    path.append(direction)

    if lab[row][col] == 'e':
        print(''.join(path))
    else:
        lab[row][col] = 'v'
        find_path(row + 1, col, 'D', lab, path)
        find_path(row - 1, col, 'U', lab, path)
        find_path(row , col + 1, 'R', lab, path)
        find_path(row, col - 1, 'L', lab, path)
        lab[row][col] = '-'

    path.pop()


#Input

rows = int(input())
cols = int(input())

lab = []

for _ in range(rows):
    lab.append(list(input()))



find_path(0, 0, '', lab, [])

