

k = 80
dungeons = [[80,20],[50,40],[30,10]]

def solution(dungeons, k):
    ans = 0
    visited = [False for _ in range(len(dungeons))]
    def dfs(L, cnt, k):
        nonlocal ans
        ans = max(ans, cnt)
        if L == len(dungeons):
            return
        else:
            for i in range(len(dungeons)):
                if not visited[i] and k >= dungeons[i][0]:
                    visited[i] = True
                    dfs(L+1, cnt + 1, k - dungeons[i][1])
                    visited[i] = False
    dfs(0, 0, k)
    return print(ans)

solution(dungeons, k)