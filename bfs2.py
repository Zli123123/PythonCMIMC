#bfs

class graph:
    
    def __init__(self):
        self.graph = {}
        self.queue = []
        self.visit = []
        self.check = []
        
    def buildgraph(self, v, c):
        self.graph.update({int(v): [None, None, c]}) #(distance, predecessor, connections)
        self.check.append(v)

        
        
    def printgraph(self):
        print(self.graph)
        
        
    def thehardpart_search(self, source):
        self.source = source
        X = (self.graph.get(source))
        c = X[2]
        self.graph.update({source: [0, None, c]})        
        
        distancemark = 0
        self.queue.append(self.source)
        now = self.queue[0]
        while self.queue != []:
            x = (self.graph.get(now)) #v: ________
            y = x[2] #connections
            pred = x[1]            
            distance = x[0]
            if y[0] != None:
                for g in range(len(y)):
                    #if distance = none
                    connect = y[g]
                    checkthis = self.graph.get(connect) #characteristics of node g of connections
                    if checkthis[0] == None:
                        self.queue.append(connect) #add next place to queue
                        checkthis[0] = distance + 1
                        checkthis[1] = now  #predecessor of connection g is now v - #make predecessor later for connection g
                        self.graph.update({(connect): checkthis })
            
            self.queue.remove(now)
            if self.queue == []:
                break
            now = self.queue[0]
            #newlist2 = [distance, pred, y]
            #self.graph.update({(i+1): newlist2 })
            
           
        print("")
        print(self.graph)
            
                    
                    
        print(self.visit)

g1 = graph()
g1.buildgraph(1, [2, 3])
g1.buildgraph(2, [1, 4])
g1.buildgraph(3, [1, 5, 6])
g1.buildgraph(4, [2])
g1.buildgraph(5, [3])
g1.buildgraph(6, [3])
g1.printgraph()
g1.thehardpart_search(4)
                   
        
