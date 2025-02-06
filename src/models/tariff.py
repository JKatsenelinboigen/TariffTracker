from typing import List, Optional
import json
from pydantic import BaseModel, RootModel

class Footnote(BaseModel):
    columns: List[str]
    value: str
    type: str

class TariffItem(BaseModel):
    htsno: Optional[str]
    htsno_list: Optional[List[str]]
    indent: str
    description: str
    superior: Optional[str]
    units: List[str]
    general: Optional[str]
    special: Optional[str]
    other: Optional[str]
    footnotes: Optional[List[Footnote]]
    quotaQuantity: Optional[str]
    additionalDuties: Optional[str]
    addiitionalDuties: Optional[str]

    # override the constructor to handle the htsno_list
    def __init__(self, **data):
        if 'htsno_list' not in data:
            data['htsno_list'] = data['htsno'].split('.') if data['htsno'] else []
        super().__init__(**data)

class TariffData(RootModel):
    root: List[TariffItem]

def load_tariffs_from_json(file_path: str) -> TariffData:
    with open(file_path, 'r') as file:
        tariff_data = json.load(file)
    return [TariffItem(**tariff) for tariff in tariff_data]

