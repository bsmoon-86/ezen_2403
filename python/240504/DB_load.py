import pymysql

# class 선언 
class MyDB:
    # 생성자 함수 -> 매개변수의 기본값은 내 컴퓨터로 지정
    def __init__(
        self,
        _host = 'localhost', 
        _port = 3306, 
        _user = 'root', 
        _pw = '1234', 
        _db = 'ezen'
    ):
        # class 내부에서 사용이 되는 독립 변수를 생성 
        self.host = _host
        self.port = _port
        self.user = _user
        self.pw = _pw
        self.db = _db
    
    # class 안에서 사용을 하는 내장 함수 생성 
    def query_execute(self, _query, *_values):
        # DB server와 연결 
        _db = pymysql.connect(
            host = self.host, 
            port = self.port, 
            user = self.user, 
            password = self.pw, 
            db = self.db
        )
        # 가상 공간(cursor를 생성)
        cursor = _db.cursor(pymysql.cursors.DictCursor)
        try:
            # 입력받은 query문을 cursor에 질의를 보낸다. 
            cursor.execute(_query, _values)
        except:
            return "쿼리문 에러 발생"
        # select문인 경우 
        if _query.strip().upper().startswith('SELECT'):
            # cursor에서 결과값을 되돌려받는다. 
            result = cursor.fetchall()
        # select문이 아닌 경우 
        else:
            # DB server에 가상 공간 데이터를 동기화
            _db.commit()
            result = 'Query OK'
        # DB server와의 연결을 종료
        _db.close()
        # result를 되돌려준다. 
        return result