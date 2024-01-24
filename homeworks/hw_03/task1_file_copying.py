import os
import sys
from pathlib import Path
import shutil

COPY_DIR_NAME = "dist"
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


def path_is_directory(path):
    return path and os.path.exists(path) and os.path.isdir(path)


def main():
    """
    The main function handles the input arguments for path_from and path_to and
    sets the default paths if no arguments are provided. It then copies files
    recursively from the source path to the target path.
    """
    default_path_from = Path.joinpath(PARENT_DIR, TEST_DIR_NAME)
    default_path_to = Path.joinpath(PARENT_DIR, COPY_DIR_NAME)

    arg_path_from = None
    arg_path_to = None
    if len(sys.argv) > 2:
        arg_path_from = sys.argv[1]
        arg_path_to = sys.argv[2]
    elif len(sys.argv) > 1:
        arg_path_from = sys.argv[1]
    else:
        print("No arguments for path_from or path_to were provided")
        print(f"Using default paths: from - {default_path_from} to - {default_path_to}")
    
    path_from = arg_path_from if path_is_directory(arg_path_from) else default_path_from
    path_to = arg_path_to if path_is_directory(arg_path_to) else default_path_to
    
    try:
        copy_files_recursive(str(path_from), str(path_to))
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
