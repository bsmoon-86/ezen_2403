import requests
import xmltodict

# openapi 함수 
# 특정 주소에 요청을 보낸다 함수를 생성 
def request_url(_url, _param):
    response = requests.get(_url, params=_param)

    result = response.content

    return result

# parameter를 생성하는 함수 
def request(_url, _keys, _values, _type = 'xml'):
    # _key의 데이터와 _values 데이터들을 dict로 생성
    params = dict()

    # for문을 이용(변수가 2개)
    for key, value in zip(_keys, _values):
        params[key] = value
    
    # request_url함수를 호출
    response_data = request_url(_url, params)
    
    # response_data를 xml인 경우 dict 형태로 변환
    if _type == 'xml':
        result = xmltodict.parse(response_data)
    else:
        result = response_data
    return result
