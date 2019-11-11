import pyodbc

connString = 'Trusted_Connection=no;' \
             'DRIVER={ODBC Driver 13 for SQL Server};'\
             'SERVER=.\\SQL_UAI;' \
             'PORT=;' \
             'DATABASE=ejemplosqlpython;UID=uPython;PWD=1234;'


try:
    cn = pyodbc.connect(connString)
    print('You are connected to db ')

except Exception as e:
    print('Error connecting to database: ', str(e))

finally:
    cn.close()
    print('Connection closed')