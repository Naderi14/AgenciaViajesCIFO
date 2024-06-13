import sys, os
from packages.menu import menu_script as ms

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'packages')))

ms.Agencia_MenuPrincipal()