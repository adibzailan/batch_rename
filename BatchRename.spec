# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['ui_main.py'],
    pathex=['.'],  # Add current directory to Python path
    binaries=[],
    datas=[('ui/*', 'ui')],
    hiddenimports=[
        'PyQt6.QtCore',
        'PyQt6.QtGui',
        'PyQt6.QtWidgets',
        'PyQt6.sip',
        'ui.main_window',  # Updated import paths
        'ui.file_list',
        'ui.folder_selection',
        'ui.progress_bar',
        'ui.action_buttons'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt5'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BatchRename',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None  # You can add an icon file here if desired
)
