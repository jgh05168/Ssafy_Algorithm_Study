def solution(papers):

    papers.sort()       # paper 오름차순 정렬
    ans = 0     
    other_papers = []   
    # n 편의 논문 중 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하 인용되었다면 ==> 중앙값 찾기
    for idx in range(len(papers)):
        if papers[idx] >= len(papers) - idx:        # 만약 n번쨰 논문이 현재 발표한 논문 수 - 현재 인덱스(논문 개수)
            ans = len(papers) - len(other_papers)       # answer 업데이트 : 전체 논문 수 - 다른 논문 개수
            break
        other_papers.append(papers[idx])        

    return ans


print(solution([3, 0, 6, 1, 5]))