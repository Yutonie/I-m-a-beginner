#選擇排序法
#A___A

Search_List = [135,5,86,12,33,79,45]
'''
def swap(a,b):
	a,b = b,a
	return a,b
'''
def Slection_Sort(ListData):
	length = len(ListData)	#數列長度
	minIndex = 0	#設定位置為0
	for x in range(length-1):	#index從0開始，所以要減1
		print('x=',x)
		min = ListData[x]	#先假設最小值為數列最左邊的數
		
		print(ListData)
		
		for i in range(x+1,length):	
			print('i=',i)
			if ListData[i]<ListData[minIndex]:
				minIndex = i
			
		ListData[minIndex],ListData[x] = ListData[x],ListData[minIndex]
	
	return ListData
		
print(Slection_Sort(Search_List))
