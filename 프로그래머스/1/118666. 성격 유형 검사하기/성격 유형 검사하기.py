"""
문제 이해
- 입력
    - survey : 질문지 타입[리스트/문자]
    - choices : 선택한 답변[리스트/숫자] 1-7
- 출력
    - result : 점수를 기반으로 4자리 문자열
    
아이디어
- 성격 유형 테이블을 만들기(surveyTable)
- RT => 1 -> R:3, 7 -> T:3
- 1 ~ 7 (-4) => -3 ~ 3
    - 점수가 음수일때 : 앞에 유형에 점수를 더해줌
    - 점수가 양수일때 : 뒤에 유형에 점수를 더해줌
    - 성격 유형 테이블을 완성
- RT / CF / JM / AN 의 성격점수를 비교해서 최종 성격 타입을 만들어준다.

제한 사항
- survey : 1,000 : 1k
- O(N**2) 1K * 1K : 1M

"""

def solution(survey, choices):
    # 설문조사 결과 테이블 만들기 (초기화)
    surveyTable = {
        "R": 0, "T" : 0,
        "C": 0, "F" : 0,
        "J": 0, "M" : 0,
        "A": 0, "N" : 0,
    }
    # survey & choice를 함께 반복하기
        #   - 조건에 따라 점수주기
    #       - (-4) 가준 점수를 만들고
    #       - 음수일 때 앞 유형 / 양수일 때 뒷 유형에 점수 주기
    for i in range(len(survey)):
        surveyType = survey[i]
        typeA = surveyType[0]
        typeB = surveyType[1]
        
        score = choices[i] - 4
        
        if score <= 0:
            surveyTable[typeA] += abs(score)
        else:
            surveyTable[typeB] += abs(score)
    """
    {'R': 6, 'T': 1, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    """
    print(surveyTable)
    # 성격 유형별로 조건을 확인해서 최종 성격 유형 만들기
    answer = ''
    if surveyTable["R"] >= surveyTable["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if surveyTable["C"] >= surveyTable["F"]:
        answer += "C"
    else:
        answer += "F"
    
    if surveyTable["J"] >= surveyTable["M"]:
        answer += "J"
    else:
        answer += "M"
    if surveyTable["A"] >= surveyTable["N"]:
        answer += "A"
    else:
        answer += "N"
        
    return answer