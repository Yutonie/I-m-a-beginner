#泡沫排序法

Search_List = [135,5,86,12,33,79,45]

def Bubble_Sort(ListData):

	length = len(ListData)	#數列長度
	
	for x in  range(length-1):
		swapped = False
		for y in range(length-1-x):
			if ListData[y]>ListData[y+1]:	#比他右邊的數字大則交換
				swapped = True
				ListData[y],ListData[y+1] = ListData[y+1],ListData[y]
		if not swapped:
			break
	return ListData
	
print(Bubble_Sort(Search_List))
