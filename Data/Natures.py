class Nature:
    def __init__(self, name, multipliers):
        self._name = name
        self._multipliers = multipliers

class ModestNature(Nature):
    def __init__(self):
        super().__init__("Modest", [0.9, 1.1, 1, 1, 1])

class AdamantNature(Nature):
    def __init__(self):
        super().__init__("Adamant", [1.1, 0.9, 1, 1, 1])

class RelaxedNature(Nature):
    def __init__(self):
        super().__init__("Relaxed", [1, 1, 1.1, 1, 0.9])