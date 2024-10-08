"""
문제이해
    - 입력 :
        테스트 케이스 T
        점원의 수 N, 선반의 높이 B
        점원의 키
    - 출력 : 
        탑의 높이가 B 이상인 탑 중 높이가 가장 낮은 탐 - 높이 B = answer

아이디어
    dfs를 통해 높이가 B 이상인 모든 탑을 검색
    정렬하여 그중 가장 낮은 값을 바탕으로 정답 도출
"""

def dfs(ii, ch): # 직원들 키의 인덱스, 현재 높이
    global top

    if ii == N:
        if ch >= B:
            top = min(top, ch)
        return

    # 해당 점원이 탑에 포함된다면
    dfs(ii+1, ch+data[ii])

    # 해당 점원이 탑에 포함되지 않는다면
    dfs(ii+1, ch)
T = int(input())

for i in range(1, T+1):
    N , B = map(int, input().split()) # 점원의 수, 선반의 높이

    data = list(map(int, input().split()))

    # top의 초기값은 무한으로 설정
    top = float("inf")
    dfs(0,0) # 직원들 키의 인덱스, 현재 높이

    # 기준을 충족하는 가장 작은 탑 - 선반의 길이
    answer = top - B
    print(f"#{i} {answer}")