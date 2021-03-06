# -*- mode: python -*-
import os
import sys
import inspect

base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def make_tree(base_path, subdir):
  path = os.path.join(base_path, subdir)
  prefix = "".join([subdir, "\\"])
  return Tree(path, prefix)

a = Analysis(['winmesh.py'],
             pathex=[base_path],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='winmesh.exe',
          icon='images\\commotion_fav.ico',
          debug=False,
          strip=None,
          upx=True,
          console=True )

coll = COLLECT(exe,
               make_tree(base_path, 'olsrd'),
               make_tree(base_path, 'images'),
               make_tree(base_path, 'profiles'),
               make_tree(base_path, 'templates'),
               make_tree(base_path, 'etc'),
               make_tree(base_path, 'lib'),
               make_tree(base_path, 'share'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='winmesh')
