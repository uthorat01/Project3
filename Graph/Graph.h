#include <fstream>
#include <iostream>
#include <unordered_map>
#include <chrono>
#include <list>
#include <queue>
#include <utility>
#include <set>
#include <sstream>
#include <string>
#include <iostream>
#include <climits>

class Graph {
private:
    std::unordered_map<std::string, std::list<std::string>> graph;
public:
    Graph();

    void readInput();

    std::unordered_map<std::string, std::list<std::string>> getGraph();

    bool DLS(std::string src, std::string target, int limit, std::string &path);

    std::pair<int, std::string> IDDFS(std::string src, std::string target);

    int BFS(std::string src, std::string target);
};

