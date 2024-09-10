import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'ui_main.py',
    '--onefile',
    '--windowed',
    f'--add-data={os.path.join("ui", "*")}{os.pathsep}ui',
    '--name=Batch Rename'
])