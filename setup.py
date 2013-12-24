#Full working with icon working too.


from distutils.core import setup
import py2exe
import os

MFCDIR = r"C:\Python27\Lib\site-packages\pythonwin"
MFCFILES = ["mfc90.dll", "mfc90u.dll", "mfcm90.dll", "mfcm90u.dll",
            "Microsoft.VC90.MFC.manifest"]
mfcfiles = map(lambda x: os.path.join(MFCDIR, x), MFCFILES)

data_files = mfcfiles

#Find details in py2exe\build_exe.py and __init__.py
setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "1.0.0",
    description = "An application to edit multiple files at once",
    name = "BB Multi File Renamer",
    data_files = data_files,

    # targets to build
    windows = [
        {
            "script":"Main.py",
            "icon_resources":[(0,"desktop.ico")]
        }
              ],
    options = {"py2exe":
                          {
                              "dll_excludes":["MSVCP90.dll"],
                              "includes" : ["win32ui","win32con","win32print"]
                              
                          }
               }

    )
