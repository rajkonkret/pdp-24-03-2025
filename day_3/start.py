# import fun_1
#
# fun_1.dodaj()

import pakiet
from pakiet import fun1
import pakiet.fun1 as pk  # jako alias

# import pakiet
# po dodaniu __all__ = ['info']
pakiet.info()  # Jestem pakietem

# from pakiet import fun1
fun1.powitanie()
fun1.info()
# Cześć
# Jestem pakietem

# import pakiet.fun1 as pk # jako alias
pk.info()
pk.powitanie()
# Jestem pakietem
# Cześć
