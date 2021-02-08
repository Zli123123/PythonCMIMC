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
        if v == 1:
            self.graph.update({1: [0, None, c]})
        
    def printgraph(self):
        print(self.graph)
        
        
    def thehardpart_search(self):

        
        distancemark = 0
        self.visit.append(1)
        for i in range(len(self.graph)):
            x = (self.graph.get(i+1)) #v: ________
            y = x[2] #connections
            pred = x[1]            
            distance = x[0]
            if y[0] != None:
                for g in range(len(y)):
                    #if distance = none
                    connect = y[g]
                    checkthis = self.graph.get(connect) #characteristics of node g of connections
                    if checkthis[0] == None:
                        self.visit.append(y[g]) #visit connections
                        checkthis[0] = distance + 1
                        checkthis[1] = i+1  #predecessor of connection g is now v - #make predecessor later for connection g
                        self.graph.update({(connect): checkthis })
                
            #newlist2 = [distance, pred, y]
            #self.graph.update({(i+1): newlist2 })
        
            
        print("")
        print(self.graph)
            
                    
                    
        print(self.visit)

g1 = graph()
g1.buildgraph(1, [2, 3])
g1.buildgraph(2, [4])
g1.buildgraph(3, [5, 6])
g1.buildgraph(4, [None])
g1.buildgraph(5, [None])
g1.buildgraph(6, [None])
g1.printgraph()
g1.thehardpart_search()
                   
        
    