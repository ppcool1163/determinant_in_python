import numpy as np #necessary for converting 2-d list to matrix
def determinant(arr):
	arr=np.array(arr)
	if len(arr)==0:
		return "Input a valid Matrix" # Confirming a valid input
	if len(arr)==1:
		return arr[0][0] # output for 1-D matrix
	if len(arr)==2:
		return arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0] # Output for 2-D matrix
	else:
		result=0
		for i in range(len(arr)):
			for j in range(len(arr)):
				arr[i][j],arr[0][j]=arr[0][j],arr[i,j] # Swaping ith row with 1st row
			result+=((-1)**i)*arr[0][0]*determinant(arr[1:,1:]) # recursion to find determinant of submatrix
		return result # Output for n-D matrix
			

# testing
x=[[1,0,0],[0,3,0],[0,0,2]]
y=determinant(x)
print(y)

