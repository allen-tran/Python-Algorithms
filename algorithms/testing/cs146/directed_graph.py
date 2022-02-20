class AdjacentMatrix:
    def main(self, args):

        vertices = []
        # print("Enter vertices : ")
        while True:
            ver = input("Enter vertices: ")
            if ver == "stop":
                break
            vertices.append(ver)
        pairs = []
        print("Enter pairs : ")
        while True:
            pair = input()
            if pair == "stop":
                break
            pairs.append(pair)
        matrix = self.getAdjacentMatrix(vertices, pairs)
        print("Adjacent Matrix")
        i = 0
        while i < len(vertices):
            if i == 0:
                print("  " + vertices[i] + " ", end="")
            else:
                print(vertices[i] + " ", end="")
            i += 1
        print()
        i = 0
        while i < len(matrix):
            print(vertices[i] + " ", end="")
            j = 0
            while j < len(matrix):
                print(str(matrix[i][j]) + " ", end="")
                j += 1
            print()
            i += 1
        print("Adjacent List")
        getAdjacentList = self.getAdjacentList(vertices, pairs, matrix)
        for strg in getAdjacentList:
            print(strg)

    def getAdjacentMatrix(self, verticies, pairs):
        matrix = [[0] * (len(verticies)) for _ in range(len(verticies))]
        i = 0
        while i < len(pairs):
            splitted = pairs[i].split(" ")
            edgeFrom = splitted[0]
            edgeTo = splitted[1]
            weight = int(splitted[2])
            indexPair = [0] * (2)
            j = 0
            while j < len(verticies):
                if edgeFrom == verticies[j]:
                    indexPair[0] = j
                if edgeTo == verticies[j]:
                    indexPair[1] = j
                j += 1
            matrix[indexPair[0]][indexPair[1]] = weight
            i += 1
        return matrix

    def getAdjacentList(self, verticies, pairs, matrix):
        adjacentList = []
        i = 0
        while i < len(matrix):
            ans = verticies[i] + ": "
            j = 0
            while j < len(matrix):
                if matrix[i][j] != 0:
                    ans += "[" + verticies[j] + ", " + str(matrix[i][j]) + "], "
                j += 1
            adjacentList.append(ans)
            i += 1
        return adjacentList


if __name__ == "__main__":
    AdjacentMatrix().main([])
