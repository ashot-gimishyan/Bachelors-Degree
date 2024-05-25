class Water:

    def __add__(self, other):
        if isinstance(other, type(None)):
            return None
        if isinstance(other, Water):
            return Ocean()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Earth):
            return Mud()
        if isinstance(other, Sun):
            return Rainbow()
        return None

    def __str__(self):
        return 'Water \U0001F4A7'


class Fire:

    def __add__(self, other):
        if isinstance(other, type(None)):
            return None
        if isinstance(other, Water):
            return Steam()
        if isinstance(other, Water):
            return Steam()
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other, Fire):
            return Sun()
        return None

    def __str__(self):
        return 'Fire \U0001F525'


class Air:

    def __add__(self, other):
        if isinstance(other, type(None)):
            return None
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Water):
            return Storm()
        if isinstance(other, Earth):
            return Dust()
        return None

    def __str__(self):
        return 'Air \u2601'


class Wind:

    def __add__(self, other):
        return None

    def __str__(self):
        return 'Wind'


class Earth:

    def __add__(self, other):
        if isinstance(other, type(None)):
            return None
        if isinstance(other, Water):
            return Mud()
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()
        if isinstance(other, Sun):
            return Desert()
        return None

    def __str__(self):
        return 'Earth \U0001F30E'


class Lightning:

    def __str__(self):
        return 'Lightning \U0001F4A5'

    def __add__(self, other):
        return None


class Dust:

    def __str__(self):
        return 'Dust \U0001F92E'

    def __add__(self, other):
        return None


class Mud:

    def __str__(self):
        return 'Mud \U0001F4A9'

    def __add__(self, other):
        if isinstance(other, type(None)):
            return None
        if isinstance(other, Sun):
            return Sprout()
        return None


class Steam:

    def __str__(self):
        return 'Steam \U0001F4A8'

    def __add__(self, other):
        return None


class Storm:

    def __str__(self):
        return 'Storm \U0001F32A'

    def __add__(self, other):
        return None


class Lava:

    def __str__(self):
        return 'Lava \U0001F30B'

    def __add__(self, other):
        return None


class Ocean:

    def __str__(self):
        return 'Ocean \U0001F30A'

    def __add__(self, other):
        return None


class Desert:

    def __str__(self):
        return 'Desert \U0001F3DC'

    def __add__(self, other):
        return None


class Rainbow:

    def __str__(self):
        return 'Rainbow \U0001F308'

    def __add__(self, other):
        return None


class Sprout:

    def __str__(self):
        return 'Sprout \u2618'

    def __add__(self, other):
        return None


class Sun:

    def __str__(self):
        return 'Sun \U0001F31E'

    def __add__(self, other):
        if isinstance(other, type(None)):
            return None
        if isinstance(other, Water):
            return Sun()
        if isinstance(other, Earth):
            return Desert()
        if isinstance(other, Mud):
            return Sprout()
        return None


sep = '\u23BA\u23BB\u23BC\u23BD\u23BC\u23BB\u23BA' * 5
water = Water()
fire = Fire()
air = Air()
earth = Earth()
sun = fire + fire
mud = water + earth
ocean = water + water

print(sep)
print('{} + {} = {}'.format(water, air, water + air))
print('{} + {} = {}'.format(water, fire, water + fire))
print('{} + {} = {}'.format(water, earth, water + earth))
print('{} + {} = {}'.format(water, water, water + water))
print('{} + {} = {}'.format(air, fire, air + fire))
print('{} + {} = {}'.format(air, earth, air + earth))
print('{} + {} = {}'.format(fire, earth, fire + earth))
print(sep)
print('{} + {} = {}'.format(fire, fire, fire + fire))
print('{} + {} = {}'.format(water, sun, water + sun))
print('{} + {} = {}'.format(earth, sun, earth + sun))
print('{} + {} = {}'.format(mud, sun, mud + sun))
print('{} + {} = {}'.format(water, ocean, water + ocean))
print(sep)