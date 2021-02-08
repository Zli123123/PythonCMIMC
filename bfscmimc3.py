#same thing but robot / farthest robot: [distance, pred, x, y, type] no connections bcause those are just x +- 1 and y +- 1
# {1: [None, None, 1, 1]
#bfs
#same thing but return directions and apply directions in a different function
l = 100
w = 100

    

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
        
        
    def thehardpart_search(self, l, w):
        xlist = []
        counter = 0
        ylist = []
        counter1 = 1
        backtow = w
        j = w
        for i in range(1, (w*l) + 1):
            if i == j + 1:
                counter = 1
                counter1 += 1
                j += w
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
        
        rlist = [] #robot cords
        rlist2 = [] #robot numeral
        elist = [] #entrance cord
        typer = input("")
        numr = 0
        source = 0
        entrance = 0
        for i in range(len(typer)):
            if typer[i] != " ":
                graph[i].append(typer[i])
                if typer[i] == "R":
                    numr += 1
                    source = i
                    rlist.append(xlist[i])
                    rlist.append(ylist[i])
                    rlist2.append(i)
                if typer[i] == "E":
                    entrance = i
                    elist.append(xlist[i])
                    elist.append(ylist[i])
        distances = []
        for k in range(1, numr+1):
            one = abs(rlist[k*2 - 2] - elist[0]) 
            two = abs(rlist[k*2 - 1] - elist[1]) 
            three = one + two
            distances.append(three)
        if len(distances) > 0:
            mm = max(distances)
        for j in range(len(distances)):
            if distances[j] == mm:
                source = rlist2[j]
                break
            
            
        print(source, entrance, distances)
        
        rlist3 = rlist
        rlist4 = rlist2
        distances2 = distances
        mm = 0
        if len(distances2) > 0:
            mm = max(distances2)
        for j in range(len(distances2)):
            if distances[j] == mm:
                rlist4.pop(j)
                distances2.pop(j)
                rlist3.pop((j+1) * 2 - 1)
                rlist.pop((j+1) * 2 - 2)        
     
        if len(distances2) > 0:
            mm = max(distances2)
        for j in range(len(distances2)):
            if distances2[j] == mm:
                source2 = rlist4[j]
                break        
     
        #_____________________________________
        #firstfindconnections 
        #EX.X...XXX.....RXX.XX..X..XX...XR.X....R
        
        #EX.X
        #...X
        #XX.6
        #...R
        #XX.X
        #X..X
        #..XX
        #...X
        #R.X.
        #...R
        
        #..XEXXRR....
        connect = []
        for k in range(w*l): #up, down, left, right
            grr = graph[k] 
            x1 = grr[2] #x cord
            y1 = grr[3] #y cord
            if y1 + 1 <= l: #if x + 1 is not over 4
                connect.append(y1+1) #downconnect
            if y1 + 1 > l: #or it equals X
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
        print(graph)
        #check for a point in the graph with same x and why as the connect list, then create a new connection list where connections are index + 1 (since index starts at 0)
        graphdup = []
        
        for k in range(len(graph)): #point to add connections
            ppp = graph[k] #current point to examine
            clist = ppp[5] #connection list
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
            graph[i].pop(5)
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
            y = x[5] #connections
            pred = x[1]            
            distance = x[0]
            if y[0] != None and x[4] != "X":
                for g in range(len(y)):
                    #if distance = none
                    connect = y[g]
                    checkthis = graph[connect] #characteristics of node g of connections
                    if checkthis[0] == None and checkthis[4] != "X":
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

        #XEX.
        #..XX
        #X...   
        print("")
        #print(graphdup)
        print("")
        print("_____________________________")
        print(graph)
        
        #entrance so - entrance backtracks to source
        complete = 0
        nower = graph[entrance]
        directions = []
        while complete != 1:
            if len(nower) == 6:
                break
            pred = nower[1]
            d = nower[6]
            directions.append(d)
            index = pred
            nower = graph[pred]
            
            
            
            
        out = open('output1.txt', 'w')    
        directions.reverse()
        print("")
        for i in range(len(directions)):
            out.write(directions[i])
        out.close()
        out = open('output1.txt', 'r')
        print(out.read())
        
        graph[source][4] = "."
        
        for i in range(len(graph)):
            if len(graph) == 7:
                graph[i].pop(6)        
        listofthings = []
        listofthings.append(directions) #0
        listofthings.append(rlist3)#1
        listofthings.append(rlist4) #2
        listofthings.append(distances2) #3
        listofthings.append(source) #4
        listofthings.append(len(typer)) #5
        listofthings.append(graph)
        listofthings.append(entrance)
        
        
        return listofthings
    
    def apply(self, listofthings, l, w):
        rlist2 = listofthings[2]
        #________________________________________
        while len(rlist2) > 0:
            graph = listofthings[6]
            distances = listofthings[3]
            #find new source, then apply
            x1 = 0
            y1 = 0
            source = listofthings[4]
            firstsource = listofthings[4]
            rlist = listofthings[1] #robot cord
            rlist2 = listofthings[2] #robot pos
            mm = 0
            rlist4 = rlist2
            rlist3 = rlist
            distances2 = distances
            if len(distances) > 0: #new max distance
                mm = max(distances)        
            for j in range(len(distances)):
                if distances[j] == mm:
                    source = rlist2[j]
                    x1 = rlist[(j+1) * 2 - 2]
                    y1 = rlist[(j+1) * 2 - 1]
                    break   
                
            #next rounds robots
            if len(distances2) > 0:
                mm = max(distances2)
            for j in range(len(distances)+1):
                if distances[j] == mm:
                    rlist4.pop(j)
                    distances2.pop(j)
                    rlist3.pop((j+1) * 2 - 1)
                    rlist3.pop((j+1) * 2 - 2)
                    break                
            print(mm, distances, rlist, source, x1, y1)
            directions = listofthings[0]
            expl = []
            for i in range(len(directions)):
                #run through directions, and then apply them
               
                if directions[i] == "U":
                    for k in range(len(graph)): 
                        if graph[k][2] == x1 and graph[k][3] == y1 - 1 and graph[k][4] != "X": #1, 2  1, 1
                            source = k
                            x1 = graph[source][2]
                            y1 = graph[source][3]
                            expl.append("U")
                            break
                        
                if directions[i] == "D":
                    for k in range(len(graph)):
                        if graph[k][2] == x1 and graph[k][3] == y1 + 1 and graph[k][4] != "X":
                            source = k
                            x1 = graph[source][2]
                            y1 = graph[source][3]            
                            expl.append("D")
                            break
                if directions[i] == "R":
                    for k in range(len(graph)):
                        if graph[k][3] == y1 and graph[k][2] == x1 + 1 and graph[k][4] != "X": #1 1   #2, 1
                            source = k
                            x1 = graph[source][2]
                            y1 = graph[source][3]      
                            expl.append("R")
                            break
                if directions[i] == "L":
                    for k in range(len(graph)):
                        if graph[k][3] == y1 and graph[k][2] == x1 - 1 and graph[k][4] != "X":
                            source = k
                            x1 = graph[source][2]
                            y1 = graph[source][3] 
                            expl.append("L")
                            break
                                    
            print(source, x1, y1)

                
            graph[source][4] = "."
            graph[firstsource][4] = "R"
            
            for i in range(len(graph)):
                if len(graph) == 7:
                    graph[i].pop(6)
            print("__________________________________________")
            print(graph)
            print("++++++++++++++++++++++++++++++++++++")
            
            if len(rlist2) == 1:
                break
            source = firstsource
            sources.append(source)
            
            listofthings = listofthings
            listofthings[0] = directions
            listofthings[1] = rlist3
            listofthings[2] = rlist4
            listofthings[3] = distances2
            listofthings[4] = max(sources)
            listofthings[6] = graph 
            
        return listofthings
                
    def everyother(self, listofthings):
        #source work 
        directions = []
        listofthings2 = listofthings
        source = listofthings2[4]
        graph = listofthings2[6]
        graph[source][0] = 0
        #________________
        distancemark = 0
        self.queue = []
        self.queue.append(source)
        now = self.queue[0]
        while self.queue != []:
            x = graph[now] #v: ________
            y = x[5] #connections
            pred = x[1]            
            distance = x[0]
            if y[0] != None and x[4] != "X":
                for g in range(len(y)):
                    #if distance = none
                    connect = y[g]
                    checkthis = graph[connect] #characteristics of node g of connections
                    if checkthis[0] == None and checkthis[4] != "X":
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

        #XEX.
        #..XX
        #X...   
        print("")
        #print(graphdup)
        print("")
        print("_____________________________")
        print(graph)
        
        #entrance so - entrance backtracks to source
        complete = 0
        entrance = listofthings[7]
        nower = graph[entrance]
        directions = []
        while complete != 1:
            if len(nower) == 6:
                break
            pred = nower[1]
            d = nower[6]
            directions.append(d)
            index = pred
            nower = graph[pred]
            
            
            
            
        out = open('output1.txt', 'a')    
        directions.reverse()
        print("")
        for i in range(len(directions)):
            out.write(directions[i])
        out.close()
        out = open('output1.txt', 'r')
        print(out.read())
        
        graph[source][4] = "."

        listofthings2[6] = graph
        listofthings2[0] = directions
        
        mm = 0
        rlist4 = listofthings[2]
        rlist3 = listofthings[1]
        distances2 = listofthings[3]              
        if len(distances2) > 0:
            mm = max(distances2)
            for j in range(len(distances2)):
                if distances2[j] == mm:
                    rlist4.pop(j)
                    distances2.pop(j)
                    rlist3.pop((j+1) * 2 - 1)
                    rlist3.pop((j+1) * 2 - 2)        
        
        for i in range(len(graph)):
            if len(graph) == 7:
                graph[i].pop(6)          
        listofthings2[0] = directions
        listofthings2[2] = rlist4
        listofthings2[1] = rlist3
        listofthings2[3] = distances2   
        listofthings2[6] = graph
        return listofthings2        
                
                    #if y - 1 is not an X    
def multipleR():     
        g1 = graph()
        g1.buildgraph(graph)
        d = g1.thehardpart_search(10, 4)  
        for i in range(2):
            c = g1.apply(d, 10, 4)
            d = g1.everyother(c)
            

multipleR()

#EX.X...XXX.....RXX.XX..X..XX...XR.X....R

#EX.X
#...X
#XX.6
#...R
#XX.X
#X..X
#..XX
#...X
#R.X.
#...R