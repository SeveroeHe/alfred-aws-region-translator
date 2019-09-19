from sys import argv
from sys import stdout
import json
from regionMap import read_template_to_dict
from regionMap import form_alfred_output
from regionMap import form_region_res

def build_Map():
    input_mapping_dict = {}
    country_to_region_dict = read_template_to_dict("RegionTemplates", "country_region_template.json")
    region_info_dict = read_template_to_dict("RegionTemplates", "region_info_template.json")
    raw_search_dict = read_template_to_dict("RegionTemplates", "raw_search_template.json")
    for input_list in raw_search_dict.values():
        region_key = input_list[0]
        for input_raw in input_list:
            input_mapping_dict[input_raw] = region_key
    return country_to_region_dict, region_info_dict, input_mapping_dict

def get_region_info(input):
    country_to_region_dict, region_info_dict, input_mapping_dict = build_Map()
    input = input.upper()
    res = []
    # if it is a country/region
    if input in country_to_region_dict:
        for region_key in country_to_region_dict[input]:
            res.append(form_region_res(region_info_dict[region_key]))
    elif input in input_mapping_dict:
        region_key = input_mapping_dict[input]
        res.append(form_region_res(region_info_dict[region_key]))
    else:
        res.append(form_region_res(["", "Not a valid region", ""]))
    return res

def main():
    arg_len = len(argv)
    if arg_len <= 1:
        return form_alfred_output([])

    query = argv[1]
    if not query:
        return form_alfred_output([])

    items = get_region_info(query)
    out = form_alfred_output(items)
    return json.dumps(out, indent=4, encoding='utf-8') + '\n'

if __name__ == '__main__':
    data = main()
    stdout.write(data)