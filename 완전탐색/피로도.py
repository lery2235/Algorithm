

k = 80
dungeons = [[80,20],[50,40],[30,10]]


def solution(k, dungeons):
    ans = 0
    cnt = 0
    visited = [False for _ in range(len(dungeons)+1)]

    def dfs(L, cnt, k):
        nonlocal ans
        if len(dungeons) == L:
            ans = max(ans, cnt)
            return
        else:
            for i in range(len(dungeons)):
                if not visited[i] and k >= dungeons[i][0]: # 최소 필요 피로도 이상이면
                    visited[i] = True
                    dfs(L+1, cnt + 1, k - dungeons[i][1])
                    visited[i] = False
    dfs(0,0, k)

    return ans



solution(k, dungeons)