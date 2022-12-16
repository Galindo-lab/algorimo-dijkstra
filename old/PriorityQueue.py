

class Vertex():
    def __init__(self,nodo=0,distancia=0, padre=None, visto=False):
        self.nodo = nodo
        self.distancia = distancia
        self.padre = padre
        self.visto = visto

    def __str__(self):
        return "("+str(self.nodo)+","+str(self.distancia)+")"
    # +str(self.padre)+","+str(self.visto)+")"
        # return str(self.weight) + " "
    
            
        
# NOTE: hacer una mejor impremeditación
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = []

    def __str__(self):
        return ", ".join([str(i) for i in self.queue])
    
    def is_empty(self): 
        return len(self.queue) == 0
    
    def enqueue(self, data): 
        self.queue.append(data)
        # print(data)
        self.queue.sort(key=lambda x: x.distancia, reverse=False)
    
    def dequeue(self):
        try:
            return self.queue.pop(0)
        except IndexError as e:
            raise Exception("No hay mas elementos en la cola")
