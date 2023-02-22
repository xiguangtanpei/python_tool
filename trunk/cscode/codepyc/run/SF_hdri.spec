# -*- mode: python -*-

block_cipher = None


a = Analysis(['runst.py'],
             pathex=['L:\\pythonpro\\PythonApplication1\\PythonApplication1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SF_Hdri',
          debug=False,
          strip=False,
          upx=True,
		  workpath ='SF_Hdri',
          console=False ,icon=r"L:\pythonpro\PythonApplication1\PythonApplication1\cc.ico")
