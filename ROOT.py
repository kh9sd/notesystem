from pathlib import Path

def get_root_dir_path():
    return Path(__file__).parent.resolve()

    """
    Previous implementation assuming a "ROOT" file in cur dir
    root_file_paths = list(Path(__file__).parent.glob("ROOT"))
    assert(len(root_file_paths) == 1)

    root_file_path = root_file_paths[0].resolve()
    # print(f"{root_file_path=}")

    root_dir_path = root_file_path.parent
    return root_dir_path
    """

if __name__ == "__main__":
    print(get_root_dir_path())
