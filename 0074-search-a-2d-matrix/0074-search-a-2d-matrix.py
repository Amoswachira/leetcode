class Solution:
    def binarySearch(self, row, target):
    	length = len(row)
    	if length == 1:
    		if row[0] == target:
    			return True
    		else:
    			return False

    	mid = length // 2
    	if target == row[mid]:
    		return True
    	elif target < row[mid]:
    		return self.binarySearch(row[:mid],target)
    	else:
    		return self.binarySearch(row[mid:],target)


    def searchMatrix(self, matrix, target):
    	if len(matrix) == 0:
    		return False

    	for row in matrix:
    		if len(row) == 0:
    			return False
    		if target <= row[len(row)-1]:
    			return self.binarySearch(row,target)
    	return False
    
        