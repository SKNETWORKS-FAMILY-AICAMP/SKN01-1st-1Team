import logging, sqlite3, datetime
import pymysql
import pymysql.cursors

# cur.execute("insert~~") # insert문을 쿼리로 실행

class DatabaseHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)
        
        # db연결 위한 커넥션 (워크벤치에서 미리 db를 만들어 놨음)
        self.conn = pymysql.connect(user="encore", passwd="encore1234", host="localhost", database="logdb")
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor) # dict cursor 설정
        
        # self.database = 'test.db' >> 이 경우 이미 워크벤치로 만들었으니 필요없음
        # self.conn = sqlite3.connect(self.database)
        # self.cur = self.conn.cursor()

        mk_table_query = '''
            CREATE TABLE IF NOT EXISTS log (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                insertTime TEXT,
                logLv TEXT,
                filename TEXT,
                lineno INTEGER,
                message TEXT
                )
        '''
        self.cur.execute(mk_table_query)
        self.conn.commit()

    def time_format(self, record):
        self.now = datetime.datetime.now()
        record.nowstr = self.now.strftime('%Y-%m-%d %H:%M:%S')

    def emit(self, record):
        self.format(record)
        self.time_format(record)
        insert_db_query = '''
            INSERT INTO log (
            insertTime, logLv, filename, lineno, message) VALUES
            ('{}', '{}', '{}', {}, '{}')
        '''.format(record.nowstr, record.levelname, record.filename, record.lineno, record.message)

        self.cur.execute(insert_db_query)
        self.conn.commit()

    def __del__(self):
        try:
            self.conn.close()
        except:
            pass



