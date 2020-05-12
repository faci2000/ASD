# def kings_path( A ):
#     Cost = [[0 for i in range(len(A))]for j in range(len(A))]
#     for i in range(len(A)):
#         for j in range(len(A)):
#             if i==0 and j==0:
#                 Cost[i][j]=A[i][j]
#             elif i==0:
#                 Cost[i][j]=A[i][j]+Cost[i][j-1]
#             elif j==0:
#                 Cost[i][j]=A[i][j]+Cost[i-1][j]
#             else:
#                 Cost[i][j]=min(Cost[i-1][j]+A[i][j],Cost[i][j-1]+A[i][j])
#     for i in range(len(A)):
#         for j in range(len(A)):
#             if i==0 and j==0:
#                 Cost[i][j]=A[i][j]
#             elif i==0:
#                 Cost[i][j]=min(A[i][j]+Cost[i+1][j],Cost[i][j])
#             elif j==0:
#                 Cost[i][j]=min(A[i][j]+Cost[i][j+1],Cost[i][j])
#             else:
#                 Cost[i][j]=min(Cost[i-1][j]+A[i-1][j-1],Cost[i][j-1]+A[i-1][j-1])

#     return Cost


# # policz koszt trasy

# print( kings_path( A ) ) # wypisze 5
def kings_path(A):
# policz koszt trasy
    length = len(A)
    B = [[0 for i in range(length)] for j in range(length)]

    B[0][0] = A[0][0]

    for i in range(1, length):
        B[i][0] = A[i][0] + B[i - 1][0]
        B[0][i] = A[0][i] + B[0][i - 1]
        j = 1
        while (j < i):
            B[i][j] = A[i][j] + min(B[i - 1][j], B[i][j - 1])
            B[j][i] = A[j][i] + min(B[j - 1][i], B[j][i - 1])
            j = j + 1
        B[i][i] = A[i][i] + min(B[i - 1][i], B[i][i - 1])

    for i in range(1, length - 1):
        B[i][0] = A[i][0] + min(B[i + 1][0], B[i - 1][0], B[i][1])
        B[0][i] = A[0][i] + min(B[0][i - 1], B[0][i + 1], B[1][i])
        j = 1
        while (j < i):
            B[i][j] = A[i][j] + min(B[i - 1][j], B[i + 1][j], B[i][j - 1], B[i][j + 1])
            B[j][i] = A[j][i] + min(B[j - 1][i], B[j + 1][i], B[j][i - 1], B[j][i + 1])
            j = j + 1
        B[i][i] = A[i][i] + min(B[i - 1][i], B[i + 1][i], B[i][i - 1], B[i][i + 1])

    B[length - 1][0] = A[length - 1][0] + min(B[length - 2][0], B[length - 1][1])
    B[0][length - 1] = A[0][length - 1] + min(B[0][length - 2], B[1][length - 1])

    for i in range(1, length - 1):
        j = length - 1
        B[j][i] = A[j][i] + min(B[j][i - 1], B[j][i + 1], B[j - 1][i])
        B[i][j] = A[i][j] + min(B[i][j - 1], B[i - 1][j], B[i + 1][j])

    B[length - 1][length - 1] = A[length - 1][length - 1] + min(B[length - 2][length - 1], B[length - 1][length - 2])

    return (B[length - 1][length - 1])


#A = [[1,1,2],[5,1,3],[4,1,1]]
A = [[1,5,5,1,1,1,1],
     [1,5,5,1,5,5,1],
     [1,5,5,1,5,5,1],
     [1,1,1,1,5,5,1],
     [5,5,5,5,5,5,1],
     [5,5,5,5,5,5,1],
     [5,5,5,5,5,5,1]]
print( kings_path( A ) )  # wypisze 5