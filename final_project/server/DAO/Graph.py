class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def Edges(self):
        return self.FindEdges()

    def AddEdge(self, edge):
        edge = set(edge)
        (vtx1, vtx2) = tuple(edge)

        if vtx1 in self.gdict:
            self.gdict[vtx1].append(vtx2)
        else:
            self.gdict[vtx1] = [vtx2]

    def FindEdges(self):
        edgename = []

        for vtx in self.gdict:
            for nextvtx in self.gdict[vtx]:
                if {nextvtx, vtx} not in edgename:
                    edgename.append({vtx, nextvtx})

        return edgename

    
    