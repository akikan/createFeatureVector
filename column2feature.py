import numpy as np

def makeDictionary(column):
	if column is None or len(column)==0:
		print("column is None. Please check column")
		return []

	# 重複なしのリストを作成
	ret=[]
	for cell in column:
		if ret.count(cell)==0:
			ret.append(cell)
	return ret

#複数の選択肢から一つを選ぶようなものを特徴量化する
def Choice2Feature(column, dictionary=None):
	if dictionary is None:
		dictionary = makeDictionary(column)
	colLen = len(column)
	ret = list(np.zeros((len(dictionary), colLen)))
	for i, cell in enumerate(column):
		if dictionary.count(cell) > 0:
			index = dictionary.index(cell)
			if cell == dictionary[index]:
				ret[index][i] = 1
	return ret



#複数の選択肢から複数を選ぶようなものを特徴量化する
def Flag2Feature(column, dictionary):
	# if dictionary is None:
	# 	dictionary = makeDictionary(column)

	colLen = len(column)
	ret = []
	for word in dictionary:
		temp = [0]*colLen
		for i,cell in enumerate(column):
			if cell.count(word) > 0:
				temp[i] = 1
		ret.append(temp)
	return ret


def Column2Stdardization(column):
	if column is None or len(column)==0:
		print("column is None. Please check column")
		return [],[],[]
	try:
		column = [float(i) for i in column]
	except:
		print("this column cannot convert str to float")
		return [],[],[]

	ave = sum(column) / len(column)
	dev = np.std(np.asarray(column))

	for cell in column:
		cell = (cell-ave)/dev
	return column, ave, dev

def column2row(column):
	return list(np.asarray(column).T)

def row2column(column):
	return list(np.asarray(column).T)

