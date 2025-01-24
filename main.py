import os
import shutil
import logging
from src.generate import generate_page

logging.basicConfig(level=logging.INFO)

def clean_directory(dst: str):
    """
    Deletes all files, symlinks, and subdirectories in the given directory.
    
    Args:
        dst (str): Path to the directory to clean.

    Raises:
        Exception: If a file or directory cannot be deleted.
    """
    if os.path.exists(dst) and os.path.isdir(dst):
        for entry in os.scandir(dst):
            try:
                if entry.is_file() or entry.is_symlink():
                    os.unlink(entry.path)
                    logging.info(f"Deleted file or symlink: {entry.path}")
                elif entry.is_dir():
                    shutil.rmtree(entry.path)
                    logging.info(f"Deleted directory: {entry.path}")
            except Exception as e:
                logging.error(f"Failed to delete {entry.path}. Reason: {e}")
    else:
        logging.warning(f"The path {dst} does not exist or is not a directory.")

def copy_dir(src, dst, src_path):
    if os.path.isfile(src):
        shutil.copy(src, dst)
        logging.info(f"Copying {src} to {dst}")
    else:
        rel_path = os.path.relpath(src, src_path)
        dst_path = os.path.join(dst, rel_path)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
            logging.info(f"Created directory: {dst_path}")
        items = os.listdir(src)
        for item in items:
            rel_src = os.path.join(src_path, rel_path, item)
            src_path = os.path.dirname(rel_src)
            copy_dir(rel_src, dst_path, src_path)

def copy_static(src, dst):
    clean_directory(dst)
    items = os.listdir(src)
    for item in items:
        copy_dir(os.path.join(src, item), dst, src)

def main():
    src = './static'
    dst = './public'
    copy_static(src, dst)
    generate_page('./content/index.md', './template.html', './public/index.html')
    

if __name__ == '__main__':
    main()
