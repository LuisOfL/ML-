def Kmeans(data, k, iteraciones=10):
    centroides = data[:k]
    
    for _ in range(iteraciones):
        # Asignar clusters
        clusters = [[] for _ in range(k)]
        for x in data:
            mini = float('inf')
            ind = 0
            for i, c in enumerate(centroides):
                dist = ((x[0]-c[0])**2 + (x[1]-c[1])**2)**0.5
                if dist < mini:
                    mini = dist
                    ind = i
            clusters[ind].append(x)
        
        # Recalcular centroides
        new_centroides = []
        for i,group in enumerate(clusters):
            if len(group) == 0:
                # Si un cluster queda vacío, mantener centroide anterior
                new_centroides.append(new_centroides[i])  # dataset simple, no debería pasar
            else:
                x_new = sum(p[0] for p in group) / len(group)
                y_new = sum(p[1] for p in group) / len(group)
                new_centroides.append([x_new, y_new])
        centroides = new_centroides
    
    return centroides, clusters

# Dataset
data = [[1,2],[2,3],[3,4],[8,8],[9,9],[10,10]]
centroides, clusters = Kmeans(data, k=2)

print("Centroides finales:", centroides)
print("Clusters finales:", clusters)
