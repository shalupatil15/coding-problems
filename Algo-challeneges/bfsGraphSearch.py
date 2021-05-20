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

#print(graph)

for n in graph:

    print(str(n) + "-->" + str(graph[n]))

#visitedOrigin = set()
#print(type(visitedOrigin))

def bfs(searchOrigin, searchDestination):
    queue = []
    visitedOrigin = set()

    queue.append(searchOrigin)
    visitedOrigin.add(searchOrigin)
    print(f'Origin is {searchOrigin}')
    while len(queue) != 0 :

        childList = graph[queue[0]]
        for child in childList:

            if searchDestination in child:
                print(f'{searchDestination} is found')
            else:
                if child not in visitedOrigin:
                    visitedOrigin.add(child)
                    queue.append(child)
                    print(child)

        queue.pop(0)


bfs('PHX','BKK')

            


    