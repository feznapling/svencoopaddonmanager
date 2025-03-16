import sys, os, shutil, errno
from pathlib import Path

def ig_f(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]

def add_addon():
    working_dir = Path(os.getcwd())
    addons_dir = Path(working_dir / 'addons')
    game_dir = Path(working_dir / 'game')

    
    if game_dir.exists():
        print("game dir exists")
    if addons_dir.exists():
        print("addon dir exists")
    else:
        print("addon directory does not exist")
        print(f"creating directory \"{addons_dir}\"")

        os.mkdir(addons_dir)

    #src = Path(addons_dir / 'coolmod')
    src = Path(addons_dir / 'evilmansion_fixed')
    target = Path(game_dir)
    symlinks=False

    #Create directory structure
    for dir in os.listdir(src):
        file_source = os.path.join(src, dir)
        file_target = os.path.join(target, dir)
        if os.path.isdir(file_source):
            shutil.copytree(file_source, file_target, symlinks, dirs_exist_ok=True, ignore=ig_f)

    #Copy files
    for root, dirs, files in os.walk(src, topdown=True):
        #print(os.path.basename(root))
        relative_path = os.path.relpath(root, src)
        file_target = os.path.join(target, relative_path)

        for file in files:
            shutil.copy2(os.path.join(root, file), os.path.join(file_target, file))
            print(f"copying {os.path.join(relative_path, file)} to {file_target}...")


if __name__ == "__main__":
    add_addon()