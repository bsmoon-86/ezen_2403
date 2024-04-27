import pandas as pd
import os
from glob import glob

## 특정 디렉토리의 데이터 파일들을 결합하는 함수 생성
# 매개변수
    # 특정 경로 (_path)
    # encoding engine (_encoding = 'UTF-8')
def dir_load(_path, _encoding = 'UTF-8'):
    # _path에서 확장자 부분만 따로 추출
    # 경로와 파일의 이름을 분리 
    # ex) ../csv/corona.csv -> (../csv/, corona.csv)
    dir, file_name = os.path.split(_path)
    # print(dir, file_name)
    # 파일의 이름에서 확장자를 분리
    # ex) corona.csv -> (corona, .csv)
    head, tail = os.path.splitext(file_name)
    # print(head, tail)

    # 비어있는 데이터프레임 생성
    result = pd.DataFrame()

    # _path를 이용하여 파일의 목록을 로드 
    file_list = glob(_path)
    # print(file_list)

    # file_list를 기준으로 반복문을 생성 
    for file in file_list:
        # tail이 csv라면 read_csv()를 이용
        if tail == '.csv':
            df = pd.read_csv(file, encoding=_encoding)
        # tail이 json이라면 read_json()을 이용
        elif tail == '.json':
            df = pd.read_json(file, encoding=_encoding)
        # tail이 xml이라면 read_xml()을 이용
        elif tail == '.xml':
            df = pd.read_xml(file, encoding=_encoding)
        # tail이 .xlsx이거나 .xls라면 read_excel()을 이용
        # elif (tail == '.xlsx') | (tail == '.xls'):
        elif tail in ['.xlsx', 'xls']:
            df = pd.read_excel(file)
        else:
            print('지원하지 않는 확장자입니다.')
            break
        # df를 result에 단순한 행 결합 
        result = pd.concat([result, df], axis=0)
    # result의 인덱스를 초기화하고 기존의 인덱스는 제거 
    result.reset_index(drop=True, inplace=True)
    # result를 되돌려준다
    return result