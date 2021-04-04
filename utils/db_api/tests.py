from  utils.db_api.sqlite import Database

db = Database("test.db")

def test():
    db.create_table_users()
    users = db.select_all_users()
    print(f"До добавления: {users=}")
    db.add_user(1, "Vasya")
    users = db.select_all_users()
    print(f"После добавления: {users=}")
    user = db.select_user(name="Vasya")
    print(f"Найденный пользователь: {user=}")
    db.update_email(1, "vasya@eu.ru")
    db.update_rating(1, 5.0)
    db.update_lat(1, -10)
    db.update_lon(1, 10)
    users = db.select_all_users()
    print(f"После обновления: {users=}")

test()
