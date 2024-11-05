def binary_search(B, C):
    L = 0
    R = len(B) - 1
    
    while L <= R:
        m = (L + R) // 2  
        
        if B[m] < C:
            L = m + 1  
        elif B[m] > C:
            R = m - 1 
        else:
            return m  
    
    return "unsuccessful"  

listaOrdenada = [1, 3, 5, 7, 9, 11]
elemento_a_buscar = 6

resultado = binary_search(listaOrdenada, elemento_a_buscar)
print("Resultado:", resultado)
