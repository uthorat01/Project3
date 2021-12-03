#include "Graph.h"

Graph::Graph() {
  readInput();
}

// reads datapoints from CSV file
void Graph::readInput() {
    std::ifstream fin("data/filtered.csv");
    std::string line,page,input;
    std::list<std::string> adj;
    if(fin.is_open()){
        while (getline(fin, line)) {
            adj.clear();
            std::stringstream s(line);
            while (getline(s, page, ',')) {
                adj.push_back(page.substr(page.find_last_of('/')+1));
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

bool Graph::DLS(std::string src, std::string target, int limit)
{
    if (src == target)
        return true;
  
    // If reached the maximum depth, stop recursing.
    if (limit <= 0)
        return false;
  
    // Recur for all the vertices adjacent to source vertex
    for (auto i = graph[src].begin(); i != graph[src].end(); ++i)
        if (DLS(*i, target, limit - 1) == true) {
            std::cout << src << std::endl;
            return true;
        }
  
     return false;
}
  
// IDDFS to search if target is reachable from v.
// It uses recursive DFSUtil().
int Graph::IDDFS(std::string src, std::string target, int max_depth)
{
    // Repeatedly depth-limit search till the
    // maximum depth.
    for (int i = 0; i <= max_depth; i++) {
        int temp = i;
        if (DLS(src, target, temp) == true)
            return i;
    }

    return INT_MAX;
}






