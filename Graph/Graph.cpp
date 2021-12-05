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

int BFS(std::string src, std::string target){
    // Mark all the vertices as not visited
    bool *visited = new bool[V];
    for(int i = 0; i < V; i++)
        visited[i] = false;
     
    // Create a queue for BFS
    list<int> queue;
    int dist = 0;
    
    // Mark the current node as visited and enqueue it
    visited[s] = true;
    queue.push_back(s);
     
    // 'i' will be used to get all adjacent
    // vertices of a vertex
    list<int>::iterator i;
     
    while(!queue.empty())
    {
        // Dequeue a vertex from queue and print it
        s = queue.front();
        cout << s << " ";
        queue.pop_front();
     
        // Get all adjacent vertices of the dequeued
        // vertex s. If a adjacent has not been visited,
        // then mark it visited and enqueue it
        for (i = adj[s].begin(); i != adj[s].end(); ++i)
        {
            if (!visited[*i])
            {
                    visited[*i] = true;
                    queue.push_back(*i);
            }
        }
        dist++;
    }
    return dist;
}





