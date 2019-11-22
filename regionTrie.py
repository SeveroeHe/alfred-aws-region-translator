from regionMap import *
import json

class Node:
	def __init__(self, letter):
		self.trie = {}
		self.region_key_list = set()


def buildTrie():
	raw_input_map = {}
	country_map = read_template_to_dict("RegionTemplates", "country_region_template.json")
	region_info_map = read_template_to_dict("RegionTemplates", "region_info_template.json")
	input_mapping_dict = read_template_to_dict("RegionTemplates", "raw_search_template.json")

	for input_list in input_mapping_dict.values():
		region_key = input_list[0]
		for input_raw in input_list:
			raw_input_map[input_raw] = region_key

	root = Node('-')
	for key, value in country_map.items():
		AddStringToTrie(key, root, value)
	for key, value in raw_input_map.items():
		AddStringToTrie(key, root, value)
		AddStringToTrie(value, root, value)
	return root, region_info_map

def AddStringToTrie(s, node, value):
	trace = node
	for i in range(0, len(s)):
		c = s[i]
		if c not in trace.trie:
			trace.trie[c] = Node(c)
		trace = trace.trie[c]
		if isinstance(value, list):
			for v in value:
				trace.region_key_list.add(v)
		else:
			trace.region_key_list.add(value)
		

def getRegionKeys(root, s):
	for i in range(0, len(s)):
		c = s[i]
		if c in root.trie:
			root = root.trie[c]
		else:
			break
	return list(root.region_key_list)

