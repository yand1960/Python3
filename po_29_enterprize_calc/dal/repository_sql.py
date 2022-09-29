# Используя этот код, как заготовку, реализуйте репозиторий
# для нашего корпортаивного калькулятора на основе хранилищу, и переключите
# наше приложение  на его использование

import pymssql

connection: pymssql._pymssql.Connection
with pymssql.connect(
    server = "yand.dyndns.org",
    database = "MyDb",
    user = "northwind",
    password = "northwind"
) as connection:

    sql = "INSERT INTO calcs(x, y, result, author) VALUES(12, 13, 25, 'YA')"
    cursor: pymssql._pymssql.Cursor
    with connection.cursor() as cursor:
        cursor.execute(sql)

    connection.commit()

