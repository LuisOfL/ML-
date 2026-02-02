def DisEucl(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def OrdList(p, X, y):
    l3 = []
    for x1, y1 in zip(X, y):
        n = DisEucl(p, x1)
        l3.append([n, y1])
    return sorted(l3, key=lambda x: x[0])

def KNN(p, X, y, k):
    vecinos = OrdList(p, X, y)[:k]
    dic = {}
    for vecino in vecinos:
        clase = vecino[1] 
        if clase in dic:
            dic[clase] += 1
        else:
            dic[clase] = 1
    return max(dic, key=dic.get)  


X = [
    [2, 6],  # persona A
    [3, 7],  # persona B
    [5, 5],  # persona C
    [6, 4],  # persona D
    [7, 3]   # persona E
]

y = [0, 0, 1, 1, 1]  
p = [4, 6]
k = 3

resultado = KNN(p, X, y, k)
print("Clase predicha para p =", p, "es:", resultado)
