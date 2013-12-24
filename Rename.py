import os
from shutil import copytree
from shutil import rmtree
import os.path as path


def Renamer(dir_path, mod_text, prefix=False, suffix=True, f_ext=False):
    dir_path = os.path.expanduser(dir_path)

    new_dir = os.path.join(dir_path, 'modified')

    if path.isdir(new_dir):
        rmtree(new_dir)
        copytree(dir_path, new_dir)
    else:
        copytree(dir_path, new_dir)

    new_name = ''
    for i in os.listdir(new_dir):
        t = os.path.splitext(i)
        if prefix and suffix:
            new_name = mod_text + t[0] + mod_text + t[-1]
        elif prefix:
            new_name = mod_text + t[0] + t[-1]
        elif suffix:
            new_name = t[0] + mod_text + t[-1]
        elif f_ext:
            new_name = t[0] + "." + mod_text
        os.rename(os.path.join(new_dir, i),
                os.path.join(new_dir, new_name))


if __name__ == '__main__':
    f = raw_input('Enter the full path plz : ')
    mod = raw_input('Enter text to added : ')
    Renamer(f, mod)
