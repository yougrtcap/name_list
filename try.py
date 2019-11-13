# def show_user_c():  # チェックリスト作成
#     conn = sqlite3.connect('user_list_db')
#     c = conn.cursor()
#     c.execute(f'select * from user_list')
#     lists = c.fetchall()
#     conn.commit()
#     conn.close()
#     print(lists)
#
# show_user_c()
# def show_user():  # ユーザーを表示
# conn = sqlite3.connect('user_list_db')
# c = conn.cursor()
# c.execute(f'select * from user_list　where name  == "{found_name}"')
# lists = c.fetchall()
# conn.commit()
# conn.close()
# print(lists)

abc = ('a', 'b', 'c')
list = list(abc)
print(list)
print()
