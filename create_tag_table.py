from db_connect import load_config, connect

def create_tables(conn):
    # print(f"{conn=}")
    with conn:
        with conn.cursor() as cur:
            # print(f"{cur=}")
            # execute the CREATE TABLE statement
            cur.execute(open("create_tag_table.sql", "r").read())
        # conn.commit()
    print("Done creating TAG table")

if __name__ == '__main__':
    config = load_config()
    #print(config)
    conn = connect(config)

    create_tables(conn)
