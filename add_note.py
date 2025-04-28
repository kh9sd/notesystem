from db_connect import load_config, connect
from pathlib import Path
from safe_copy import safe_copy
import os

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

    # new_tag_name = 'Shit5'
    # add_tag(conn, new_tag_name)

    root_file_paths = list(Path().glob("ROOT"))
    assert(len(root_file_paths) == 1)

    root_file_path = root_file_paths[0].resolve()
    # print(f"{root_file_path=}")

    root_dir_path = root_file_path.parent
    # print(f"{root_dir_path=}")

    # test file
    shit = list(Path().glob("TEMP_FILE.txt"))
    assert(len(shit) == 1)

    # TODO: how do I get this
    new_file_abs_path = shit[0].resolve()
    new_file_raw_name = new_file_abs_path.name
    # print(f"{new_file_raw_name=}")

    # We will be saving this relative path in the DB
    relative_saved_dir_from_root = Path('saved')
    relative_saved_file_path_from_root = relative_saved_dir_from_root / new_file_raw_name
    print(f"{relative_saved_file_path_from_root=}")

    new_saved_file_path = root_dir_path / relative_saved_file_path_from_root

    os.makedirs(root_dir_path / relative_saved_dir_from_root, exist_ok=True)
    safe_copy(new_file_abs_path, new_saved_file_path)
