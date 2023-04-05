import random
import numpy as np
import time

def randstring(l):
    arr = ['A','T','C','G']
    res = ""
    for i in range(l):
        res += random.choice(arr)
    return res

def print_mat(mat, s1, s2):
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            print(mat[i][j], end=" ")
        print()

def fillarray(mat, s1, s2, i=1, j=1):
    m, n = len(s1) + 1, len(s2) + 1
    
    if s1[i-1] == s2[j-1]:
        mat[i][j] = mat[i-1][j-1] + 2
    else:
        mat[i][j] = max(max(mat[i-1][j-1], mat[i][j-1]), mat[i-1][j]) - 1
    
    global maxr, maxc
    if mat[i][j] > mat[maxr][maxc]:
        maxr = i
        maxc = j
    
    if j < n - 1:
        fillarray(mat, s1, s2, i, j+1)
    if j == 1 and i < m - 1:
        fillarray(mat, s1, s2, i+1, j)

def backtrack(mat, s1, s2, ans1="", ans2=""):
    n = len(s2)
    
    global maxr, maxc
    if maxr == 0 and maxc == 0:
        print(ans1)
        print(ans2)
        return
    elif mat[maxr-1][maxc-1] + 2 == mat[maxr][maxc] and s2[maxc-1] == s1[maxr-1]:
        ans2 = s2[maxc-1] + ans2
        ans1 = s1[maxr-1] + ans1
        maxr -= 1
        maxc -= 1
    elif mat[maxr][maxc-1] - 1 == mat[maxr][maxc]:
        ans2 = s2[maxc-1] + ans2
        ans1 = "_" + ans1
        maxc -= 1
    elif mat[maxr-1][maxc] - 1 == mat[maxr][maxc]:
        ans2 = "_" + ans2
        ans1 = s1[maxr-1] + ans1
        maxr -= 1
    else:
        ans2 = "*" + s2[maxc-1] + ans2
        ans1 = "*" + s1[maxr-1] + ans1
        maxr -= 1
        maxc -= 1
        
    backtrack(mat, s1, s2, ans1, ans2)

if __name__ == "__main__":
    s1 = "AGCACACA"
    s2 = "ACACACTA"
    print(s1)
    print(s2)

    mat = np.zeros((len(s1) + 1, len(s2) + 1), dtype=int)
    maxr, maxc = 0, 0

    start = time.time()
    fillarray(mat, s1, s2)
    end = time.time()

    print_mat(mat, s1, s2)
    print("time taken:", (end - start) * 1000000, "microseconds")

