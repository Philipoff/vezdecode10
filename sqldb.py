import mysql.connector


def load_image(blob_value):
    db = mysql.connector.connect(user='root', password='5555',
                                 host='localhost',
                                 database='pictures')

    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM pictures")
    rowcount = cursor.fetchone()[0]

    sql = "INSERT INTO pictures (ID, photo) VALUES (%s, %s)"
    val = (rowcount, blob_value)
    cursor.execute(sql, val)
    db.commit()

    db.close()
    return str(rowcount)


def get_image(photo_id):
    db = mysql.connector.connect(user='root', password='5555',
                                 host='localhost',
                                 database='pictures')
    cursor = db.cursor()

    sql_select_query = "SELECT photo FROM pictures where ID = %s"

    cursor.execute(sql_select_query, (photo_id,))

    result = cursor.fetchone()

    db.close()
    return result
