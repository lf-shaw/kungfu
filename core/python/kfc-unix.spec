import os
import tushare
import plotly
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None
a = Analysis(['kungfu/__main__.py'],
     pathex=['python'],
     binaries=[],
     datas=[
        ('../build/' + os.environ['CMAKE_BUILD_TYPE'] + '/*', '.'),
        ('extensions', 'extensions'),
        ('../build/build_extensions', 'extensions'),
        ('../cpp/yijinjing/include', 'include'),
        ('../cpp/wingchun/include', 'include'),
        ('../build/deps/nanomsg-1.1.5/include', 'include'),
        ('../deps/spdlog-1.3.1/include', 'include'),
        ('../deps/json-3.5.0/single_include', 'include'),
        ('../deps/fmt-5.3.0/include', 'include'),
        ('../deps/rxcpp-4.1.0/include', 'include'),
        ('../deps/hffix-b67d404f/include', 'include'),
        ('../deps/SQLiteCpp-2.3.0/include', 'include'),
        ('../deps/pybind11-2.2.4', 'pybind11'),
        (os.path.join(tushare.__path__[0], 'VERSION.txt'), 'tushare'),
        (os.path.join(plotly.__path__[0], 'package_data'), 'plotly/package_data')
     ] + collect_data_files('wcwidth'),
     hiddenimports=[
          'pkg_resources.py2_warn',
          'numpy',
          'pandas',
          'tushare',
          'plotly',
          'plotly.graph_objects',
          "recordclass",
          "sortedcontainers",
          'wcwidth',
          "dotted_dict"
          ],
     hookspath=["python/hooks"],
     runtime_hooks=None,
     excludes=['extensions', 'matplotlib'],
     cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
     cipher=block_cipher)
exe = EXE(pyz,
                a.scripts,
                exclude_binaries=True,
                name='kfc',
                debug=False,
                strip=False,
                upx=True,
                console=True )
coll = COLLECT(exe,
                    a.binaries,
                    a.zipfiles,
                    a.datas,
                    strip=False,
                    upx=True,
                    name='kfc')
