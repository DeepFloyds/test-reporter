from dataclasses import dataclass

@dataclass
class TestCase:
    index: int
    name: str
    category: str
    result: str
    duration: float
    note: str