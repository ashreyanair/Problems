Matrix=[
    [1,2,3,20],
    [4,5,6,30],
    [7,8,9,40],
    [10,11,12,50],
    [2,3,4,1]
]
rows=len(Matrix)
columns=len(Matrix[0])

left=0
right=columns-1
top=0
bottom=rows-1
while(top<=bottom and left<=right):
    for i in range(left,right+1):
        print(Matrix[top][i],end=" ")
    top=top+1
    for i in range(top,bottom+1):
        print(Matrix[i][right],end=" ")
    right=right-1
    for i in range(right,left-1,-1):
        print(Matrix[bottom][i],end=" ")
    bottom=bottom-1
    for i in range(bottom,top-1,-1):
        print(Matrix[i][left],end=" ")
    left=left+1