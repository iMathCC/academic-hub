from dataclasses import dataclass
from models.compromisso import Compromisso

@dataclass
class AgendaSemanal:
    dias : dict[str, list[Compromisso]]
