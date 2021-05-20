airports = ['PHX','BKK','OKC','JFK','LAX','MEX','EZE','HEL','LOS','LAP', 'LIM']

routes = [
    ('PHX', 'LAX'),
    ('PHX', 'JFK'),
    ('JFK', 'OKC'),
    ('JFK', 'HEL'),
    ('JFK', 'LOS'),
    ('MEX', 'LAX'),
    ('MEX', 'BKK'),
    ('MEX', 'LIM'),
    ('MEX', 'EZE'),
    ('LIM', 'BKK')  
     ]

graph = {}

def addNode(airportName):
    graph[airportName] = []

def addEdge(origin,destination):
    originChildList = graph[origin]
    #print(originChildList)
    if destination not in originChildList:
        originChildList.append(destination)
    graph[origin] = originChildList

    destinationChildList = graph[destination]
    #print(currentDestination)
    if origin not in destinationChildList:
        destinationChildList.append(origin)
    graph[destination] = destinationChildList



for item in airports:
    addNode(item)
    
for parent,child in routes:   
    addEdge(parent,child)


# for n in graph:
#     print(str(n) + "-->" + str(graph[n]))

alreadyVisited = set()

def dfs(source, destination):

    alreadyVisited.add(source)

    childrens = graph[source]

    for currentChild in childrens:

        if currentChild in destination:
            print('We found the destination:', destination)
            break

        if currentChild not in alreadyVisited:
            print('We Reached: ', currentChild)
            return dfs(currentChild, destination)
            
        
     
                                 
       
dfs('PHX','BKK')