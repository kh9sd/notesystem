from db_connect import load_config, connect

def add_tag(conn, tag_name):
    sql = """INSERT INTO tags(name)
             VALUES(%s) RETURNING id;"""
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (tag_name,))

            # Contains result of INSERT from RETURNING clause
            # Should be exactly 1 element
            returned_rows = cur.fetchone()

            assert(len(returned_rows) == 1)

            print(f"Done adding tag '{tag_name}' with id={returned_rows[0]}!")

if __name__ == '__main__':
    config = load_config()
    # print(config)
    conn = connect(config)

    new_tag_name = 'Shit5'
    add_tag(conn, new_tag_name)
