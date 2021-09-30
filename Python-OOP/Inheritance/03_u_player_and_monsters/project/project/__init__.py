from blade_knight import *
from dark_knight import *
from dark_wizard import *
from elf import *
from hero import *
from knight import *
from muse_elf import *
from soul_master import *
from wizard import *


hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
