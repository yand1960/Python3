# 1. Использование модулей по относительному пути "вниз"
from module1.module12.po_28b_modules import Arith
from module1.module11.po_28a_modules import foo, foo1
from module1.module13 import minus

# 2. Задать переменную окружения %PYTHONPATH% на уровне ОС

# 3. Задать переменную окружения %PYTHONPATH% программно
# (довольно неудобно для девелопера: IDE ругается, подсказка не всплывает):
# import sys
# sys.path.append("C:\\temp\\module01")

# 4. Задать переменную окружения %PYTHONPATH%  среде разработки для проекта
# File -> Settings -> Python Interpreter -> cog -> Show All -> пятая кнопка -> +

# from module012.po_28b_modules import Arith
# from module011.po_28a_modules import foo, foo1
# from module013 import minus

# 5. Задать относительный импорт (т.е. с использованием . и ..)
# Но он работает только в составе пакетов.
# Так что работоспособный вариант - в файле po_28b_modules.py

# from .module1.module12.po_28b_modules import Arith
# from .module1.module11.po_28a_modules import foo, foo1
# from ..Python3.module1.module13 import minus

print(Arith().plus(1, 2), foo, foo1())