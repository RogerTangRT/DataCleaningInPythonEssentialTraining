
import sqlite3

conn = sqlite3.connect("rides.db")
cursor = conn.cursor()

# Lista as tabelas e o SQL de criação
cursor.execute("""
SELECT name, sql
FROM sqlite_master
WHERE type='table'
ORDER BY name;
""")

tabelas = cursor.fetchall()

for nome_tabela, create_sql in tabelas:

    print("\n" + "=" * 80)
    print(f"TABELA: {nome_tabela}")
    print("=" * 80)

    print("\nCREATE TABLE:")
    print(create_sql)

    print("\nCOLUNAS:")
    cursor.execute(f"PRAGMA table_info('{nome_tabela}')")

    for cid, nome, tipo, notnull, default, pk in cursor.fetchall():
        print(
            f"  {nome:<20} {tipo:<15} "
            f"NOT NULL={bool(notnull)} PK={bool(pk)}"
        )

    print("\nREGISTROS (primeiros 10):")

    try:
        cursor.execute(f"SELECT * FROM '{nome_tabela}' LIMIT 10")

        colunas = [desc[0] for desc in cursor.description]
        print(colunas)

        for linha in cursor.fetchall():
            print(linha)

    except Exception as e:
        print(f"Erro ao consultar {nome_tabela}: {e}")

conn.close()
