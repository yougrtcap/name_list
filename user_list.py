import sqlite3

conn = sqlite3.connect('user_list_db')
c = conn.cursor()

def create_table():  # テーブル作成

    c.execute(f'create table user_list(name strings,age integer )')
    conn.commit()
    conn.close()


def add_user():  # 新規ユーザーを追加
    new_name = input('New user name >> ')
    new_age = input('New user age >> ')  # 重複をハジく
    li = show_user_c()
    if new_name not in li:
        print(f'Add new user: {new_name}')
        c.execute(f'insert into user_list values ("{new_name}",{new_age})')
        conn.commit()
        conn.close()
    else:
        print('既に存在します。')


def show_user():  # ユーザーを表示

    c.execute(f'select * from user_list')
    lists = c.fetchall()
    conn.commit()
    conn.close()
    for list in lists:
        print(f'Name: {list[0]} / age: {list[1]}')


def show_user_c():  # チェックリスト作成
    c.execute(f'select * from user_list')
    lists = c.fetchall()
    conn.commit()
    conn.close()
    li = []
    for list in lists:
        li.append(list[0])
    return li


def found_user():  # 表示したい人を検索
    found_name = input('User name >> ')
    lists = c.execute(f'select * from user_list where name == "{found_name}" ').fetchone()

    if type(lists) is tuple:
        print(f'Name : {lists[0]} // Age : {lists[1]}')  # リスト表示

    else:
        print('そんなのナイィッ！！')
    conn.commit()
    conn.close()


def delete_user():  # ユーザーの削除
    user_name = input('User name >> ')
    c.execute(f'delete from user_list where name == "{user_name}"')
    conn.commit()
    conn.close()
    print(f'User "{user_name}" is Delete')


def edit_user():  # 編集
    user_name = input('User name >> ')
    new_name = input('New user name >>')
    new_age = input('New user age >>')
    c.execute(f'update user_list set name ="{new_name}",age ="{new_age}"  where name = "{user_name}" ')
    conn.commit()
    conn.close()
    print(f'Update user {new_name}')


def main():  # 入力表示追加
    y_command = input('Your command >> ')
    if y_command == 'a' or y_command == 'A':  # 追加
        add_user()
    elif y_command == 's' or y_command == 'S':  # 表示
        show_user()
    elif y_command == 'f' or y_command == 'F':  # 検索
        found_user()
    elif y_command == 'd' or y_command == 'D':  # 削除
        delete_user()
    elif y_command == 'e' or y_command == 'E':  # 編集
        edit_user()
    elif y_command == 'q' or y_command == 'Q':  # さようなら
        print('Bye !')
    else:  # 見つからない的な
        print(f'{y_command} command not found ')
        main()

if __name__ == '__main__':
    print(
        f'===== Welcome to CRM Application =====\n[S]how: Show all users info\n[A]dd: Add new user [F]ind:Find user\n[D]elete: Delete user\n[E]dit: Edit a user\n======================================')
    main()
