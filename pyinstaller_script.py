import PyInstaller.__main__

PyInstaller.__main__.run([
    'ui_main.py',
    '--onefile',
    '--windowed',
    '--add-data=ui;ui',
    '--name=Batch Rename'
])