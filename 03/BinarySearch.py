#!/usr/bin/env python
# -*- coding: utf-8 

def binarySearch(lists, select):
	is_find = False
	print lists, select
	if len(lists) > 0:
		mid_len = len(lists)/2
		mid_num = lists[mid_len]
		gt_list = lists[0:mid_len]
		lt_list = lists[mid_len+1:]
		if mid_num == select:
			is_find = True
			return is_find
		elif mid_num < select:
			return binarySearch(gt_list, select)
		else:
			return binarySearch(lt_list, select)
	return is_find

list_nums = [9,8,7,6,5,4,3,2,1,0]
selectNum = 3
print binarySearch(list_nums, selectNum)
selectNum = 10
print binarySearch(list_nums, selectNum)