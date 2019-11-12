import sqlite3


def show_user_c():  # チェックリスト作成
    conn = sqlite3.connect('user_list_db')
    c = conn.cursor()
    c.execute(f'select * from user_list')
    lists = c.fetchall()
    conn.commit()
    conn.close()
    li = []
    for list in lists:
        li.append(list[0])
    return li


li = show_user()
print(li)
