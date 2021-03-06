# -*- mode: python -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2013-2016, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


__testname__ = 'test_option_wignore'

a = Analysis([__testname__ + '.py'],
             pathex=[])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          [('W ignore', '', 'OPTION')],
          exclude_binaries=1,
          name= __testname__ + '.exe',
          debug=True,
          strip=False,
          upx=False,
          console=True)
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               name=__testname__)
