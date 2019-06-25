def bipartite(l):
    l1 = []
    l2 = []
    l1.append(V.pop(0))
    for p_vertex in V:
        if p_vertex in l1 and p_vertex in l2:
            print("Not a bipartite graph")
            break
        for i in l[1:]:
            if l[i][0] in l1 and l[i][1] in l1:
                print("Not a bipartite graph")
                break
            elif (((l[i][0],p_vertex) in l) or ((p_vertex,l[i][0]) in l)) and (l[i][0] not in l2) and (l[i][1] not in l1):
                l2.append(l[i][0])
                l1.append(l[i][1])
            elif (((l[i][1],p_vertex) in l) or ((p_vertex,l[i][1]) in l)) and (l[i][0] not in l1) and (l[i][1] not in l2):
                l2.append(l[i][1])
                l1.append(l[i][0])
            else:
                print("Not a bipartite graph")
                break
            
        
        
    
