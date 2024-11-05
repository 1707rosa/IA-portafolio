def selection_sort(A):
   
    for r in range(len(A) - 1):
        iMin = r
        
        for i in range(r + 1, len(A)):
            if A[i] < A[iMin]:
                iMin = i
      
        if iMin != r:
            A[r], A[iMin] = A[iMin], A[r]
    return A


lista = [64, 25, 12, 22, 11]
print("Lista original:", lista)
print("Lista ordenada:", selection_sort(lista))
