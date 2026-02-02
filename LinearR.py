def Media(vector):
    return sum(vector)/len(vector)

def ProPunt(vector1,vector2):
    res = []
    for x in range(len(vector1)):
	    res.append(vector1[x]*vector2[x])
    return sum(res)

def Vector2(vector):
	res = []
	for x in vector:
	    res.append(x**2)
	return sum(res)

def B(vector1,vector2):
	a = ProPunt(vector1, vector2) - len(vector1)*Media(vector1)*Media(vector2)
	b = Vector2(vector1)-len(vector1)*(Media(vector1)**2)
	return a/b

def A(vector1,vector2,b):
	return Media(vector2) - b*Media(vector1)

	
def LinearR(mat,x):
	b = B(mat[0],mat[1])
	a = A(mat[0],mat[1],b)
	return a + b * x

m = [[1,3,5,7],[2,4,5,8]]
print("El resultado de la prediccion para",10, "es",LinearR(m,10))

