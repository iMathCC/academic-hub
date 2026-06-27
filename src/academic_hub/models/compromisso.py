from dataclasses import dataclass
from datetime import date
from academic_hub.enums.origem import Origem
from academic_hub.enums.tipo_compromisso import TipoCompromisso
from modelis.disciplina import Disciplina


@dataclass
class Compromisso:
    titulo: TipoCompromisso
    tipo: str
    data: date
    inicio: str | None
    fim: str | None
    disciplina: Disciplina | None
    origem: Origem
    descricao: str | None = None
    concluido: bool = False
