#include "Graph.h"


//Graph Constructor
Graph::Graph() {
    readInput();
}

//This method uses file I/O functions to read in data from a CSV file to fill in the graph
// object of th Graph class in a manner which represents the Animal section of Wikipedia.
void Graph::readInput() {
    //The filtered.csv file consists of data gathered from Python based scraper
    std::ifstream fin("Data/filtered.csv");
    std::string line, page, input;
    std::list <std::string> adj;
    //Perform file I/0
    if (fin.is_open()) {
        while (getline(fin, line)) {
            adj.clear();
            std::stringstream s(line);
            while (getline(s, page, ',')) {
                adj.push_back(page.substr(page.find_last_of('/') + 1));
            }
            //The first value on a line in this CSV is the title of the Wikipedia page and the
            // subsequent entries are the front links of this page. The title of the page is
            // removed from the list to serve as the key in the map
            std::string startPage = adj.front();
            adj.pop_front();
            graph[startPage] = adj;
        }
    }
}

//This method returns the graph variable of the Graph class
std::unordered_map <std::string, std::list<std::string>> Graph::getGraph() {
    return graph;
}

//This method is utilized by the IDDFS method to perform a recursive depth limited search
//SOURCE: GeeksforGeeks
bool Graph::DLS(std::string src, std::string target, int limit, std::string &path) {
    //Ends recursive call if target is found
    if (src == target)
        return true;
    //Ends recursive call if limit is reached
    if (limit <= 0)
        return false;
    //Iterates through vertices of the source node to find path leading to target
    for (auto it = graph[src].begin(); it != graph[src].end(); it++)
        //Recursive call find the optimal path
        if (DLS(*it, target, limit - 1, path) == true) {
            path = *it + " -> " + path;
            return true;
        }
    return false;
}

// The IDDFS method uses the DLS method to find the path between a source node and the
// target node, if one exists within a limit of 1000 nodes
// SOURCE: GeekforGeeks
std::pair<int, std::string> Graph::IDDFS(std::string src, std::string target) {
    std::string path = "";
    //A depth limited search is performed at increasing depths until the maximum depth
    for (int i = 0; i <= 1000; i++) {
        int temp = i;
        if (DLS(src, target, temp, path) == true)
            return std::make_pair(i, path);
    }
    return std::make_pair(INT_MAX, "");
}

//The BFS method performs a level order search using a queue data structure
//SOURCE: https://stackoverflow.com/questions/31247634/how-to-keep-track-of-depth-in-breadth-first-search
int Graph::BFS(std::string src, std::string target) {
    int dist = 1;
    std::queue <std::string> queue;
    queue.push(src);
    while (!queue.empty()) {
        int levelSize = queue.size();
        //Loops through nodes added to the queue at each level to find correct
        //distance between the source node and target node
        while (levelSize--) {
            std::string s = queue.front();
            queue.pop();
            for (auto it = graph[s].begin(); it != graph[s].end(); it++) {
                if (*it == target) {
                    return level;
                }
                queue.push(*it);
            }
        }
        dist++;
        //Ends BFS if distance between source and target is larger than 1000
        if (dist > 1000)
            return INT_MAX;
    }
    return INT_MAX;
}
