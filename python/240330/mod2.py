## list에서 sort()함수 -> 리스트의 정렬을 오름차순 정렬
## reverse 매개변수에 값을 True 변경 -> 내림차순 정렬
def sort_c(_list, reverse = False):
    # 입력받은 리스트 데이터를 각 원소들끼리 모두 비교 
    # 리스트에서 첫번째 데이터를 추출
    result = []
    for k in range(len(_list)):
        data = _list[0]
        # 리스트에 있는 2번째 데이터(index = 1)부터 마지막 데이터(index = len(_list)까지 비교
        for i in range(1, len(_list), 1):
            # print(i)
            # print(_list[i])
            # data와 list[i] 값을 비교하여 작은 값을 data에 대입
            if reverse:
                if data < _list[i]:
                    data = _list[i]
            else:
                if data > _list[i]:
                    data = _list[i]
            # print(data)
        # data는 _list에서 가장 작은 데이터
        # data를 비어있는 리스트에 추가(append) -> _list에서 해당하는 데이터를 제거(remove)
        result.append(data)
        _list.remove(data)
    print(result)
    return result
        
            
