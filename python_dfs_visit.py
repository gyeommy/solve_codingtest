# DFS(Depth First Search)
import sys
sys.setrecursionlimit(10**4)

def solution(maps):
    # 1-D array를 받아서, 2-D로 변환
    converted_map = [list(val) for val in maps]
    rows = len(converted_map)
    cols = len(converted_map[0])

    # array전체를 int형으로 변환
    for r in range(rows):
        for c in range(cols):
            if converted_map[r][c] == "x":
                converted_map[r][c] = 0
            else:
                converted_map[r][c] = int(converted_map[r][c])

    # dfs 중복 방지
    seen = set()


    def dfs(r, c):
        # 가장자리 조건, converted_map[r][c] 조건을 마지막에 두고 인덱스 에러 방지
        if (r<0 or c<0 or (r,c) in seen or
            r==rows or c==cols or converted_map[r][c] == 0):
            # 방문한 좌표 추가
            seen.add((r,c))
            # recursive dfs(재귀적 깊이 우선 탐색)
            return (converted_map[r][c] +
                        dfs(r+1, c) +
                        dfs(r-1,c) +
                        dfs(r,c+1) +
                        dfs(r, c-1))
        
    areas = []
    answer = []

    for r in range(rows):
        for c in range(cols):
            areas.append(dfs(r,c))

    if sum(areas) == 0:
        return [-1]
    

    for area in areas:
        if area != 0:
            answer.append(area)

    # 파이썬 리스트 sort(): 오름자순으로 정렬, reverse=True 옵션으로 내림차순 정렬 가능
    answer.sort()
    return answer