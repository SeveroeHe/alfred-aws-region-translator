from regionTrie import *
from sys import argv
from sys import stdout

def form_items(region_keys, region_info_dict):
	res = []
	for airport_code in region_keys:
		res.append(form_region_res(region_info_dict[airport_code]))
	return res

def main():
	arg_len = len(argv)
	if arg_len <= 1:
		return form_alfred_output([])

	query = argv[1]
	if not query:
		return form_alfred_output([])
	root,  region_info_map = buildTrie() 
	region_keys = getRegionKeys(root, str(query.upper()))
	items = form_items(region_keys, region_info_map)

	out = form_alfred_output(items)
	return json.dumps(out, indent=4, encoding='utf-8') + '\n'

if __name__ == '__main__':
	data = main()
	stdout.write(data)