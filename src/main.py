from models.tariff import load_tariffs_from_json
import json

def build_tariff_dict(tariffs):
    tariff_dict = {}
    for tariff in tariffs:
        current_level = tariff_dict
        for htsno in tariff.htsno_list:
            if htsno not in current_level:
                current_level[htsno] = {}
            current_level = current_level[htsno]
        current_level['tariff'] = tariff.model_dump()

    return tariff_dict


file_path = 'src/data/tariff_data.json'
tariffs = load_tariffs_from_json(file_path)

tariff_dict = build_tariff_dict(tariffs)
with open("tariff_hierarchy.json", "w") as file:
    json.dump(tariff_dict, file, indent=4)  # `indent=4` makes it readable