import sqlite3


def create_table():  # テーブル作成
    conn = sqlite3.connect('user_list_db')
    c = conn.cursor()
    c.execute(f'create table user_list(name,age)')
    conn.commit()
    conn.close()


# def name_check():  # 名前の重複をチェック
#     pass


def add_user():  # 新規ユーザーを追加
    new_name = input('New user name >> ')
    new_age = input('New user age >> ')  # 重複をハジく
    if new_name not in li:
        print(f'Add new user: {new_name}')
        conn = sqlite3.connect('user_list_db')
        c = conn.cursor()
        c.execute(f'insert into user_list values ("{new_name}",{new_age})')
        conn.commit()
        conn.close()
    else:
        print('既に存在します。')



def show_user():  # ユーザーを表示
    conn = sqlite3.connect('user_list_db')
    c = conn.cursor()
    c.execute(f'select * from user_list')
    lists = c.fetchall()
    conn.commit()
    conn.close()
    for list in lists:
        print(f'Name: {list[0]} / age: {list[1]}')


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


li = show_user_c()

print(
    f'===== Welcome to CRM Application =====\n[S]how: Show all users info\n[A]dd: Add new user\n======================================')


def main():  # 入力表示追加
    y_command = input('Your command >> ')
    if y_command == 'a' or y_command == 'A':  # 追加
        add_user()
    elif y_command == 's' or y_command == 'S':  # 表示　
        show_user()
    elif y_command == 'q' or y_command == 'Q':  # さようなら
        print('Bye !')
    else:  # 見つからない的な
        print(f'{y_command} command not found ')
        main()


if __name__ == '__main__':
    main()
