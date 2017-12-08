import psycopg2
import psycopg2.extras

def query_pgsql(dbname,query):
    try:
        conn = psycopg2.connect("dbname='{0}' user='postgres' host='localhost' password='123'".format(dbname))
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute(query)
    except:
        print "query failed"

    rows = cur.fetchall()

    return rows
