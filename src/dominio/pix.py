from typing import Optional
from pydantic import BaseModel

class PixData(BaseModel):
    tipo: str
    valor: float
    endereco_pix: str
    agendado: Optional[bool] = None
    data_agendamento: Optional[str] = None

