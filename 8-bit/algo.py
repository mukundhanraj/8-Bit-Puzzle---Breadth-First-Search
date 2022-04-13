import copy
import fn

if __name__ == '__main__':

    st_node = [[4, 7, 0], [1, 2, 8], [3, 5, 6]]  # Start node

    gl_node = [[1, 4, 7], [2, 5, 8], [3, 6, 0]]  # Goal node

    # Implementing Bradth First Search
    visited, p_index = fn.bfs(st_node, gl_node)
    path = fn.b_trk(visited, p_index)  # Implementing Backtracking

    #Creating Text Files
    with open('nodePath.txt', 'w') as f:
        for line in path:
            line = [[row[i] for row in line] for i in range(len(line[0]))]
            line = str(line).replace('[', '').replace(']', '').replace(',', '')
            f.write(line + '\n')

    with open('NodesInfo.txt', 'w') as f:
        f.write("Node_index   Parent_Node_index   Cost\n")
        for i in range(len(visited)):
            line = str(i + 1) + ' ' + str(p_index[i]) + " 0"
            f.write(line + '\n')

    with open('Nodes.txt', 'w') as f:
        for line in visited:
            line = [[row[i] for row in line] for i in range(len(line[0]))]
            line = str(line).replace('[', '').replace(']', '').replace(',', '')
            f.write(line + '\n')
