# 기본적인 웹 서버 설정 
# flask 프레임워크에서 특정 기능을 로드
# render_template 함수는 templates라는 폴더에서 html 문서를 유저에게 보내준다.  
from flask import Flask, render_template, request
import pandas as pd

# Flask라는 Class 생성 
# Flask Class에 __init__(생성자 함수) -> 필수 인자값 1개(파일의 이름)
# __name__ -> 현재 실행되는 파일의 이름(app.py)
app = Flask(__name__)

# 주소 값(api)들을 생성 (식당에서 메뉴판을 생성)
# 네비게이터 : 특정한 주소로 요청이 들어왔을때 특정 함수를 연결 
# 127.0.0.1:5000(기본 주소) + '/' -> 127.0.0.1:5000/ 요청 시
# 바로 아래의 함수를 호출
@app.route('/')
def index():
    # return "Hello world"
    return render_template('index.html')

# 또 다른 api 생성 
# 127.0.0.1:5000/second 주소로 요청시 아래의 함수를 호출
@app.route('/second')
def second():
    # return "Second Page"
    return render_template('second.html')

# index 페이지에서 입력한 데이터를 받는 api 생성 
# 127.0.0.1 = localhost
# localhost:5000/signin 생성
@app.route('/signin')
def signin():
    # 유저가 보낸 데이터를 확인 
    # 유저가 데이터를 보낸다(요청) -> request
    # get 방식으로 보낸 데이터는 request 안에(.) args 키 값에 데이터가 존재
    meg = request.args
    # meg 데이터의 타입 : dict
    # { input_id : asdf, input_pass : 1234 }
    # 유저가 입력한 id 값을 변수에 저장
    _id = meg['input_id']
    _pass = meg['input_pass']
    # 로그인의 성공 조건 id가 'test' 이고 password가 '1234'인 경우
    if (_id == 'test') & (_pass == '1234'):
        # print(meg)  
        # return "로그인이 성공"
        # 외부의 csv 파일을 로드 
        # 상위 폴더로 이동(../) -> python 폴더 이동 (python/)-> csv 폴더로 이동(csv/) -> 파일이름(corona.csv)
        df = pd.read_csv('../python/csv/corona.csv')
        # 데이터프레임의 타입을 dict 타입으로 변경 
        data = df.to_dict()
        return data

    else: 
        return "로그인이 실패"



# 웹 서버를 실행
app.run(debug=True)