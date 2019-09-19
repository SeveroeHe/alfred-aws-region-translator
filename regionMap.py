import json

def read_template_to_dict(path_prefix, template_name):
    template_location = "{}/{}".format(path_prefix, template_name)
    with open(template_location, 'r') as json_file:
        json_data = json_file.read()
    return json.loads(json_data)


def form_region_res(region_info):
    region_key = region_info[0]
    subtitle = "" if len(region_key) == 0 else region_key+" ; "+region_info[2]
    res = {
        'uid': region_key,
        'title': region_info[1],
        'subtitle': subtitle,
        'arg': region_key,
        'autocomplete': region_key,
        'icon': {
            'path': 'region_photo/'+region_key+'.png'
        }
    }
    return res

def form_alfred_output(items):
    return {'items': items}

