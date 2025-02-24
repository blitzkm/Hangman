from dataclasses import dataclass
from enum import Enum, auto

type PlayerName = str

@dataclass(frozen=True)
class Cell:
	cell_no: int

class Feedback(Enum):
	INVALID = auto()
	IT_HAS = auto()
	IT_DOES_NOT_HAVE = auto()
	GAME_OVER = auto()
