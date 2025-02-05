from typing import List, Optional
import json
from pydantic import BaseModel, RootModel

class Footnote(BaseModel):
    columns: List[str]
    value: str
    type: str

class TariffItem(BaseModel):
    htsno: Optional[str]
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

class TariffData(RootModel):
    root: List[TariffItem]

def load_tariffs_from_json(file_path: str) -> TariffData:
    with open(file_path, 'r') as file:
        tariff_data = json.load(file)
    return [TariffItem(**tariff) for tariff in tariff_data]

tariffs = load_tariffs_from_json('src/data/tariff_data.json')


for tariff in tariffs:
    print(tariff)