class Node:
    def __init__(self, parent, UpperX, UpperY, UpperZ, LowerX, LowerY, LowerZ):
        self.parent = parent
        self.UpperX = UpperX
        self.UpperY = UpperY
        self.UpperZ = UpperZ
        self.LowerX = LowerX
        self.LowerY = LowerY
        self.LowerZ = LowerZ
        self.CenterX = (self.UpperX + self.LowerX)/2
        self.CenterY = (self.UpperY + self.LowerY)/2
        self.CenterZ = (self.UpperZ + self.LowerZ)/2
        self.IsLeafNode = True
        self.value = value

    parent = None
    value = None

    TRF = None      # top right front
    TRB = None      # top right back
    TLF = None      # top left front
    TLB = None      # top left back

    BRF = None      # bottom right front
    BRB = None      # bottom right back
    BLF = None      # bottom left front
    BLB = None      # bottom left back

    branch = [TRF, TRB, TLF, TLB, BRF, BRB, BLF, BLB]

# Position in space
    UpperX = None
    UpperY = None
    UpperZ = None
    LowerX = None
    LowerY = None
    LowerZ = None

    def AddNode(self, data, coordinates, position):
        if position == 0:
            self.value.append((coordinates, data))

        else:
            position -= 1
            # For determining the Quadrant
            if coordinates[0] <= self.CenterX:
                if coordinates[1] <= self.CenterY:
                    if coordinates[2] <= self.CenterZ:
                        UpperX = self.CenterX
                        UpperY = self.CenterY
                        UpperZ = self.CenterZ
                        LowerX = self.LowerX
                        LowerY = self.LowerY
                        LowerZ = self.LowerZ
                        self.BLB = Node(self.BLB, UpperX, UpperY, UpperZ, LowerX, LowerY, LowerZ)
                        self.BLB.AddNode(data, coordinates, position)

                    else:
                        UpperX = self.CenterX
                        UpperY = self.CenterY
                        UpperZ = self.UpperZ
                        LowerX = self.LowerX
                        LowerY = self.LowerY
                        LowerZ = self.CenterZ
                        self.BLF = Node(self.BLB, UpperX, UpperY, UpperZ, LowerX, LowerY, LowerZ)
                        self.BLF.AddNode(data, coordinates, position)

                else:
                    if coordinates[2] <= self.CenterZ:
                        UpperX = self.CenterX
                        UpperY = self.UpperY
                        UpperZ = self.CenterZ
                        LowerX = self.LowerX
                        LowerY = self.CenterY
                        LowerZ = self.LowerZ
                        self.BRB = Node(self.BLB, UpperX, UpperY, UpperZ, LowerX, LowerY, LowerZ)
                        self.BRB.AddNode(data, coordinates, position)

                    else:
                        UpperX = self.CenterX
                        UpperY = self.UpperY
                        UpperZ = self.UpperZ
                        LowerX = self.LowerX
                        LowerY = self.CenterY
                        LowerZ = self.CenterZ
                        self.BRF = Node(self.BLB, UpperX, UpperY, UpperZ, LowerX, LowerY, LowerZ)
                        self.BRF.AddNode(data, coordinates, position)

            else:
                if coordinates[1] <= self.CenterY:
                    if coordinates[2] <= self.CenterZ:
                        UpperX = self.UpperX
                        UpperY = self.CenterY
                        UpperZ = self.CenterZ
                        LowerX = self.CenterX
                        LowerY = self.LowerY
                        LowerZ = self.LowerZ
                        self.TLB = Node(self.BLB, UpperX, UpperY, UpperZ, LowerX, LowerY, LowerZ)
                        self.TLB.AddNode(data, coordinates, position)

                    else:
                        UpperX = self.UpperX
                        UpperY = self.CenterY
                        UpperZ = self.UpperZ
                        LowerX = self.CenterX
                        LowerY = self.LowerY
                        LowerZ = self.CenterZ
                        self.TLF = Node(self.BLB, UpperX, UpperY, UpperZ, LowerX, LowerY, LowerZ)
                        self.TLF.AddNode(data, coordinates, position)

                else:
                    if coordinates[2] <= self.CenterZ:
                        UpperX = self.UpperX
                        UpperY = self.UpperY
                        UpperZ = self.CenterZ
                        LowerX = self.CenterX
                        LowerY = self.CenterY
                        LowerZ = self.LowerZ
                        self.TRB = Node(self.BLB, UpperX, UpperY, UpperZ, LowerX, LowerY, LowerZ)
                        self.TRB.AddNode(data, coordinates, position)

                    else:
                        UpperX = self.UpperX
                        UpperY = self.UpperY
                        UpperZ = self.UpperZ
                        LowerX = self.LowerX
                        LowerY = self.LowerY
                        LowerZ = self.LowerZ
                        self.TRF = Node(self.BLB, UpperX, UpperY, UpperZ, LowerX, LowerY, LowerZ)
                        self.TRF.AddNode(data, coordinates, position)

RootCoordinates = (0,0,0)
Maximum = 7

class Octree:
    def __init__(self, MaxX, MaxY, MaxZ, MinX, MinY, MinZ, RootCoordinates, Maximum):
        self.MaxX = MaxX
        self.MaxY = MaxY
        self.MaxZ = MaxZ
        self.MinX = MinX
        self.MinY = MinY
        self.MinZ = MinZ
        self.RootCoordinates = RootCoordinates
        self.Maximum = Maximum
        self.root = Node("Root", MaxX, MaxY, MaxZ, MinX, MinY, MinZ)

    def Insert(self, data, coordinates):
        self.root.AddNode(data, coordinates, Maximum)

    def FindPositon(self, position, count=0, branch=0):
        if Node.IsLeafNode:
            return(Node.value)
        branch = Octree.FIndBranch(Node, position)
        child = Node.branch[branch]
        if child is None:
            return None
        return Octree.FindPositon(child, position, count + 1, branch)

    def FindBranch(self, root, position):
        index = 0
        if (position[0] >= root.position[0]):
            index |= 4
        if (position[1] >= root.positiom[1]):
            index |= 2
        if (position[2] >= root.position[2]):
            index |= 1
        return index












