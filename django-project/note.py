#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# django 首次启动报如下错误
  File "C:\App\Python\Python37\lib\site-packages\django\views\debug.py", line 332, in get_traceback_html
    t = DEBUG_ENGINE.from_string(fh.read())
UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 9737: illegal multibyte sequence

# 解决方法：指定open方法的字符集
331     with Path(CURRENT_DIR, 'templates', 'technical_500.html').open(encoding='utf-8') as fh: