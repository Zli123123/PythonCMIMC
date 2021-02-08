#same thing but robot / farthest robot: [distance, pred, x, y, type] no connections bcause those are just x +- 1 and y +- 1
# {1: [None, None, 1, 1]
#bfs
l = 3
w = 4

    

class graph:
    
    def __init__(self):
        self.graph = []
        self.queue = []
        self.visit = []
        self.check = []
        
    def buildgraph(self, list):
        self.graph = list
        #self.graph.update({int(v): [None, None, c]}) #(distance, predecessor, connections)
        #self.check.append(v)

        
        
    def printgraph(self):
        print(self.graph)
        
        
    def thehardpart_search(self, source, entrance, l, w):
        xlist = []
        counter = 0
        ylist = []
        counter1 = 1
        backtow = w
        for i in range(1, (w*l) + 1):
            if i == w + 1:
                counter = 1
                counter1 += 1
                w += w
            else:
                counter += 1
            xlist.append(counter)
            ylist.append(counter1)
        
        graph = []
        gitem = []
        w = backtow
        for i in range(w*l):
            gitem.append(None)
            gitem.append(None)
            gitem.append(xlist[i])
            gitem.append(ylist[i])
            graph.append(gitem)
            gitem = []
        print(graph)
        #_____________________________________
        #firstfindconnections 
        
        connect = []
        for k in range(w*l): #up, down, left, right
            grr = graph[k] 
            x1 = grr[2] #x cord
            y1 = grr[3] #y cord
            if y1 + 1 <= l: #if x + 1 is not over 4
                connect.append(y1+1) #downconnect
            if y1 + 1 > l:
                connect.append(None)
                
            if y1 - 1 > 0: 
                connect.append(y1-1) #upconnect
            if y1 - 1 == 0:
                connect.append(None)    
                
            if x1 + 1 <= w:
                connect.append(x1+1) #right
            if x1 + 1 > w:
                connect.append(None)    
                
            if x1 - 1 > 0:          #left
                connect.append(x1-1)
            if x1 - 1 == 0      :
                connect.append(None)      
                
            graph[k].append(connect)
            connect = []
            #y, y, x, x
        
        #check for a point in the graph with same x and why as the connect list, then create a new connection list where connections are index + 1 (since index starts at 0)
        graphdup = []
        
        for k in range(len(graph)): #point to add connections
            ppp = graph[k] #current point to examine
            clist = ppp[4] #connection list
            ppx = ppp[2] #xcord
            ppy = ppp[3] #ycord
                        
                       
            edges = []
            for i in range(len(graph)): #check all points in graph for same x and y
                
                grr = graph[i] 
                x1 = grr[2] #x cord
                y1 = grr[3] #y cord                 
                v = i
                if k != i:
                
                    if clist[0] == y1 and ppx == x1:
                        edges.append(v) 
                        
                    if clist[1] == y1 and ppx == x1:
                        edges.append(v) 
                        
                    if clist[2] == x1 and y1 == ppy:
                        edges.append(v)     
                        
                    if clist[3] == x1 and y1 == ppy:
                        edges.append(v)             
            
             
            graphdup.append(edges)
            
        for i in range(len(graph)):
            graph[i].pop(4)
            graph[i].append(graphdup[i])
            
        #_______________________
        #source work 
        graph[source][0] = 0
        #________________
        distancemark = 0
        self.queue.append(source)
        now = self.queue[0]
        while self.queue != []:
            x = graph[now] #v: ________
            y = x[4] #connections
            pred = x[1]            
            distance = x[0]
            if y[0] != None:
                for g in range(len(y)):
                    #if distance = none
                    connect = y[g]
                    checkthis = graph[connect] #characteristics of node g of connections
                    if checkthis[0] == None:
                        self.queue.append(connect) #add next place to queue
                        checkthis[0] = distance + 1
                        checkthis[1] = now  #predecessor of connection g is now v - #make predecessor later for connection g
                       # self.graph.update({(connect): checkthis })
                        graph[connect] = checkthis #adds new stuff 
                        
                        #+_________
                        four = 0
                        if x[2] == checkthis[2] + 1:
                            four = "L"
                        if x[2] == checkthis[2] - 1:
                            four = "R"
                        if x[3] == checkthis[3] + 1:
                            four = "U"      
                        if x[3] == checkthis[3] - 1:
                            four = "D"    
                            
                        graph[connect].append(four)
    
            self.queue.remove(now)
            if self.queue == []:
                break
            now = self.queue[0]       
           
        print("")
        print(graphdup)
        print("")
        print("_____________________________")
        print(graph)
        
        #entrance so - entrance backtracks to source
        complete = 0
        nower = graph[entrance]
        directions = []
        while complete != 1:
            if len(nower) == 5:
                break
            pred = nower[1]
            d = nower[5]
            directions.append(d)
            index = pred
            nower = graph[pred]
            
            
            
            
                    
        directions.reverse()
        print("")
        for i in range(len(directions)):
            print(directions[i], end = "")
        
        

g1 = graph()
g1.buildgraph(graph)
g1.thehardpart_search(4, 1, 3, 4)