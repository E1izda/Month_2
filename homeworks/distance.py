class Distance:
    units = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self.units[self.unit]

    def from_meters(self, value_in_meters, unit):
        return Distance(value_in_meters / self.units[unit], unit)

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_meters = self.to_meters() + other.to_meters()
        return self.from_meters(total_meters, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_meters = self.to_meters() - other.to_meters()
        return self.from_meters(total_meters, self.unit)
