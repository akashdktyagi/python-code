
class Chip:


class Keyboard:
    keys={'A','B'}

class Motherboard:
    chip = Chip()
class Laptop:
    keyboardObject = Keyboard()
    motherboard = Motherboard()