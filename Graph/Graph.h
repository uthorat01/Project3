#include <fstream>
#include <iostream>
#include <map>
#include <chrono>
#include <list>
#include <queue>
#include <utility>
#include <set>
#include <sstream>
#include <string>
#include <iostream>
#include <climits>


// ==================================== Graph Class Definition ==================================== //
class Graph {
  private:
    std::map<std::string,std::list<std::string>> graph;
  public:
    Graph();
    void readInput();
    std::map<std::string, std::list<std::string>> getGraph();
    bool DLS(std::string src, std::string target, int limit, std::string& path);
    std::pair<int, std::string> IDDFS(std::string src, std::string target);
    int BFS(std::string src, std::string target);
};
// ===================================== End Graph Definition ===================================== //
