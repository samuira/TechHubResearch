class LogicalFunction:
	"""

	"""
	def __init__(self):
		pass

    def group_by_ss(list_of_json, order_title):
		list_of_json = sorted(list_of_json, key = lambda i: i[order_title])
		temp_title = None
		j = {}
		for obj in list_of_json:
		    if temp_title == obj['title']:
		        j[obj['title']].append(obj)
		    else:
		        j[obj['title']] = [obj]
		        temp_title = obj['title']
		        
		return j
