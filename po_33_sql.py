import pymssql

connection: pymssql._pymssql.Connection
with pymssql.connect(
    server = "yand.dyndns.org",
    database = "AdventureWorks",
    user = "northwind",
    password = "northwind"
) as connection:

    # 1. Вывести список товаров с ценами
    sql = "SELECT Name, ListPrice FROM Production.Product"
    cursor: pymssql._pymssql.Cursor
    with connection.cursor() as cursor:
        cursor.execute(sql)
        products = cursor.fetchall()

    # for p in products:
    #     print(f"{p[0]}\t-\t{p[1]}")


    # 2. Вывести, у скольких товаров не заполнена колонка ProductSubcategoryID
    sql = """
        SELECT COUNT(*) 
        FROM Production.Product 
        WHERE ProductSubcategoryID IS NULL
    """
    cursor: pymssql._pymssql.Cursor
    with connection.cursor() as cursor:
        cursor.execute(sql)
        # categories = cursor.fetchall()
        result = cursor.fetchone()

    # print(len(list(filter(lambda c: c[0] is None, categories))))
    # print(len(categories))
    print(result[0])





