def max(input_list):
	temp = input_list[0]
	for item in input_list:
		if(item > temp):
			temp = item
	return temp

def min(input_list):
	temp = input_list[0]
	for item in input_list:
		if(item < temp):
			temp = item
	return temp
