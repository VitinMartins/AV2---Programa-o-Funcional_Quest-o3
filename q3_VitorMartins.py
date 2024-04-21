import mysql.connector

config = {
    'user': 'root',
    'password': "admin",
    'host': 'localhost',
    'database': 'meudb'
}

#Esta parte é para a conexão ao banco de dados
connect_db = lambda: mysql.connector.connect(**config)

#Parte do cursor
create_cursor = lambda conn: conn.cursor()

#Fazer o comando para INSERIR
insert = lambda conn, cursor, table, fields, values: (
    cursor.execute(insert_record(table, fields, values), values),
    conn.commit()
)

#Fazer o comando para REMOVER
remove = lambda conn, cursor, table, condition: (
    cursor.execute(remove_record(table, condition)),
    conn.commit()
)

#Fazer o comando de CONSULTA
select = lambda conn, cursor, fields, table, condition=None: (
    cursor.execute(select_records(fields, table, condition)),
    [print(row) for row in cursor.fetchall()]
)

#Instruções SQL
insert_record = lambda table, fields, values: (
    f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(['%s'] * len(values))})"
)

remove_record = lambda table, condition: f"DELETE FROM {table} WHERE {condition}"

select_records = lambda fields, table, condition=None: (
    f"SELECT {', '.join(fields)} FROM {table} WHERE {condition}" if condition else
    f"SELECT {', '.join(fields)} FROM {table}"
)


conn = connect_db()
cursor = create_cursor(conn)

insert(conn, cursor, 'USERS', ['name_users', 'country', 'id_console'], ['Taty', 'Brasil', 1])
remove(conn, cursor, 'USERS', 'id = 1')
select(conn, cursor, ['name_users', 'country'], 'USERS')

cursor.close()
conn.close()
