def isSafe(pos, totalRow, totalCol, visited):
    if pos in visited:
        return False
    row, col = pos
    if row >= totalRow or col >= totalCol or row <0 or col < 0:
        return False
    return True

def solveBoggle(word, indexChar, arr, row, col, totalRow, totalCol, visited):
    if indexChar >= len(word):
        return True
    next_pos = [(row+1, col+1), (row+1, col), (row+1, col-1),(row, col-1),(row-1, col-1), (row-1, col),(row-1, col+1),(row, col+1)]
    for pos in next_pos:
        if isSafe(pos, totalRow, totalCol, visited):
            if arr[pos[0]][pos[1]] == word[indexChar]:
                visited.append(pos)
                if solveBoggle(word, indexChar+1, arr, pos[0], pos[1], totalRow, totalCol, visited):
                    return True
                visited.remove(pos)
    return False

def solve(word, arr, totalRow, totalCol, visited):
    indexChar = 0
    
    for row in range(totalRow):
        for col in range(totalCol):
            if arr[row][col] == word[indexChar]:
                visited.append((row,col))
                return solveBoggle(word, indexChar+1, arr, row, col, totalRow, totalCol, visited)
    print(False)

if __name__ == "__main__":
    words = ["GEEKS", "FOR", "QUIZ", "GO"]
    boggle = [['G', 'I', 'Z'],
          ['U', 'E', 'K'],
          ['Q', 'S', 'E']]
    for word in words:
        visited = []
        if solve(word, boggle, 3, 3,visited):
            print(word, visited)
        else:
            print(False)