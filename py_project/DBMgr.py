# 디비 처리, 연결, 해제, 검색어 가져오기, 데이터 삽입
# pymysql 깃허브 주소 https://github.com/PyMySQL/PyMySQL

import pymysql as my

# DB Connection을 하나만 들고 있음
class DBHelper:
    '''
    멤버변수 : 커넥션
    '''
    conn = None
    '''
    생성자
    '''
    def __init__(self):
        self.db_init()
    '''
    멤버 함수
    '''
    def db_init(self):
        self.conn = my.connect(
            host='localhost',
            user='root',
            password='##@@',
            db='pythondb',
            charset='utf8',
            cursorclass=my.cursors.DictCursor
        )
    def db_free(self):
        if self.conn:
            self.conn.close()

    # 검색 키워드 가져오기 => 웹에서 검색
    def db_selectKeyword(self):
        #커서 오픈
        # with => 닫기 처리를 자동으로 처리해준다 => I/O 많이 사용
        rows = None
        with self.conn.cursor() as cursor:
            # Read a single record
            sql = "select * from tbl_keyword;"
            cursor.execute(sql)
            rows = cursor.fetchall() # cursor.fetchone() 은 하나만 들고옴
            print(rows)
        return rows

    def db_insertCrawlingData(self, title, price, area, contents, keyword):
        with self.conn.cursor() as cursor:
            sql = '''
            insert into `tbl_crawlingdata` 
            (title, price, area, contents, keyword)
            values(%s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (title, price, area, contents, keyword))
        self.conn.commit()

# 단독으로 수행시에만 작동 => 테스트코드를 삽입해서 사용  
# 임포트해서 쓸 때는 main이 아니니까 작동 안함      
if __name__ == '__main__':
    db = DBHelper()
    #print( db.db_selectKeyword())
    #print( db.db_insertCrawlingData('1', '2', '3', '4', '5') )
    db.db_free()