from dataclasses import dataclass
from academic_hub.models.disciplina import Disciplina

@dataclass
class Semestre:
    nome:str
    disciplinas:list[Disciplina]
    percentual_conclusao:float
