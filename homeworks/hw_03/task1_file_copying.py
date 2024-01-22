import os
from pathlib import Path
import shutil

COPY_DIR_NAME = "copy"
TEST_DIR_NAME = "test_dir_task1"
PARENT_DIR = Path(__file__).parent
IGNORED_DIRECTORIES = {"venv", "node_modules", "bin", "build", "dist",
                       "__pycache__", "dist", "lib", "var", "cache", "tmp", "bin", "log", "env", "opt"}


def copy_files(path_from, path_to, filenames):
    """
    Copy files from source directory to target directory/subdirectory based on file extension.
    :param path_from: The source directory path
    :param path_to: The destination directory path
    :param filenames: A list of filenames to be copied
    """
    for filename in filter(lambda fn: not fn.startswith("."), filenames):
        file_extension = os.path.splitext(filename)[1]
        directory_name = file_extension[1:] if file_extension else 'default'
        directory_path = os.path.join(path_to, directory_name)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        file_path_from = os.path.join(path_from, filename)
        file_path_to = os.path.join(str(directory_path), filename)
        # print(f"Copying file {filename} from {file_path_from} to {file_path_to}")
        shutil.copyfile(file_path_from, file_path_to)


def copy_files_recursive(path_from, path_to):
    """
    Recursively copies files from one directory to another.
    Hidden files and directories are ignored as well as lib directories and caches.
    Args:
        path_from (str): The source directory path.
        path_to (str): The destination directory path.
    """
    with os.scandir(path_from) as entries:
        for entry in entries:
            if entry.name.startswith(".") or entry.name in IGNORED_DIRECTORIES:
                print(f"Ignoring {entry.name}")
                continue
            if entry.is_file():
                copy_files(path_from, path_to, [entry.name])
                continue
            copy_files_recursive(entry.path, path_to)


def main():
    try:
        test_dir_path = Path.joinpath(PARENT_DIR, TEST_DIR_NAME)
        copy_target_path = Path.joinpath(PARENT_DIR, COPY_DIR_NAME)
        copy_files_recursive(str(test_dir_path), str(copy_target_path))
    except FileNotFoundError as e:
        print(f"File not found {e.filename}")
    except PermissionError as e:
        print(f"Permission denied {e.filename}")
    except OSError as e:
        print(f"OS error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
