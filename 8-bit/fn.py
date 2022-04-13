import copy

def swap(mat, pos1, pos2):
    #Swapping Elements of nodes
    mat1 = copy.deepcopy(mat)
    mat1[pos1[0]][pos1[1]] = mat[pos2[0]][pos2[1]]
    mat1[pos2[0]][pos2[1]] = mat[pos1[0]][pos1[1]]
    return mat1


def pstn(x, arr):
    #To create 2D list
    for i in arr:
        if x in i:
            return arr.index(i), i.index(x)
    print("No Zero Found")
    return -1, -1


def bfs(init, end):
    #Function to implement Breadth First Search on the puzzle
    vstd = [init]
    queue = [init]
    p_index = [0]
    flag = False

    while queue:
        crnt_nde = queue.pop()
        row, col = pstn(0, crnt_nde)
        if (col + 1) < 3:
            # Move Left
            new_node = swap(crnt_nde, (row, col), (row, col + 1))
            if new_node not in vstd:
                vstd.append(new_node)
                p_index.append(vstd.index(crnt_nde) + 1)
                if (new_node == end):
                    flag = True
                    break
                queue.insert(0, new_node)
        if (col - 1) > -1:
            # Move Right
            new_node = swap(crnt_nde, (row, col), (row, col - 1))
            if new_node not in vstd:
                vstd.append(new_node)
                p_index.append(vstd.index(crnt_nde) + 1)
                if (new_node == end):
                    flag = True
                    break
                queue.insert(0, new_node)

        if (row + 1) < 3:
            # Move Up
            new_node = swap(crnt_nde, (row, col), (row + 1, col))
            if new_node not in vstd:
                vstd.append(new_node)
                p_index.append(vstd.index(crnt_nde) + 1)
                if (new_node == end):
                    flag = True
                    break
                queue.insert(0, new_node)

        if (row - 1) > -1:
            # Move Down
            new_node = swap(crnt_nde, (row, col), (row - 1, col))
            if new_node not in vstd:
                vstd.append(new_node)
                p_index.append(vstd.index(crnt_nde) + 1)
                if (new_node == end):
                    flag = True
                    break
                queue.insert(0, new_node)

    if(flag):
        print('Path Generated')
        return vstd, p_index

    print('No Solution Exists')
    return -1, -1


def b_trk(vstd, p_index):
    #Back Tracking Algorithm
    crnt_nde = vstd[-1]
    pth = []
    p_idx = 1
    while p_idx:
        pth.append(crnt_nde)
        p_idx = p_index[vstd.index(crnt_nde) - 1]
        crnt_nde = vstd[p_idx]
    pth.append(crnt_nde)
    return pth[::-1]
