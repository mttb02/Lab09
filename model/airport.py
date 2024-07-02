from dataclasses import dataclass

@dataclass
class Airport:
    _id: int
    _iata_code: str
    _airport: str
    _city: str
    _state: str
    _country: str
    _langitude: float
    _longitude: float
    _timezone_offset: float

    @property
    def id(self):
        return self._id

    @property
    def airport(self):
        return self._airport

    def __hash__(self):
        return self._id

    def __str__(self):
        return f"{self.id}: {self.airport}"