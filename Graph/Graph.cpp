#include "Graph.h"


Graph::Graph() {
    readInput();
}

// reads datapoints from CSV file
void Graph::readInput() {
    std::ifstream fin("Data/filtered.csv");
    std::string line, page, input;
    std::list<std::string> adj;
    if (fin.is_open()) {
        while (getline(fin, line)) {
            adj.clear();
            std::stringstream s(line);
            while (getline(s, page, ',')) {
                adj.push_back(page.substr(page.find_last_of('/') + 1));
            }
            std::string startPage = adj.front();
            adj.pop_front();
            graph[startPage] = adj;
        }
    }
}

std::map<std::string, std::list<std::string>> Graph::getGraph() {
    return graph;
}

//from GeeksforGeeks
bool Graph::DLS(std::string src, std::string target, int limit, std::string& path)
{
    if (src == target)
        return true;

    // If reached the maximum depth, stop recursing.
    if (limit <= 0)
        return false;

    // Recur for all the vertices adjacent to source vertex
    for (auto i = graph[src].begin(); i != graph[src].end(); ++i)
        if (DLS(*i, target, limit - 1, path) == true) {
            path = *i + " -> " + path;
            return true;
        }

    return false;
}

// IDDFS to search if target is reachable from v.
// It uses recursive DFSUtil().
std::pair<int, std::string> Graph::IDDFS(std::string src, std::string target)
{
    // Repeatedly depth-limit search till the
    // maximum depth.
    std::string path = "";
    for (int i = 0; i <= 10; i++) {
        int temp = i;
        if (DLS(src, target, temp, path) == true)
            return std::make_pair(i, path);
    }

    return std::make_pair(INT_MAX, "");
}

// from GeeksforGeeks
int Graph::BFS(std::string src, std::string target) {
    int level = 1;
    std::queue<std::string> queue;
    queue.push(src);
    while(!queue.empty()){
        int level_size = queue.size();
        while (level_size--) {
            std::string s = queue.front();
            queue.pop();
            for (auto i = graph[s].begin(); i != graph[s].end(); ++i)
            {
                if (*i == target) 
                {
                    return level;
                }
                queue.push(*i);
            }
        }
        level++;
        if(level > 10)
            return INT_MAX;     
    }
    return INT_MAX;    

}
