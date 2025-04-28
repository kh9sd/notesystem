from db_connect import load_config, connect
from ROOT import get_root_dir_path

from pathlib import Path

def create_tables(conn):
    # print(f"{conn=}")
    with conn:
        with conn.cursor() as cur:
            # execute the SELECT statement
            cur.execute(open("select_all_notes.sql", "r").read())

            returned_rows = cur.fetchall()
        # conn.commit()

    print("Done with SELECT")
    return returned_rows

if __name__ == '__main__':
    config = load_config()
    #print(config)
    conn = connect(config)

    returned_rows = create_tables(conn)
    # pprint(returned_rows)

    root_dir_path = get_root_dir_path()
    #print(f"{root_dir_path=}")

    for id, rel_path, created_at in returned_rows:
        saved_file_path = root_dir_path / rel_path

        with open(saved_file_path) as f:
            print(f"Saved item {id=} with {rel_path=} has contents {f.readlines()}")
