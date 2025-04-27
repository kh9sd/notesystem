import shutil
import os

# copy with no overwrite, with no TOCTOU issues
def safe_copy(src_path, dest_path):
    dest_fd = os.open(dest_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)

    with os.fdopen(dest_fd, "w") as dest_f:
        # TODO: copy rest of file metadata?
        with open(src_path) as src_f:
            return shutil.copyfileobj(src_f, dest_f)

