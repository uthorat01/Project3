#include <fstream>
#include <iostream>
#include <map>
#include <list>
#include <sstream>
#include <string>
#include <iostream>


// ==================================== Graph Class Definition ==================================== //
class Graph {
  private:
    std::map<std::string,std::list<std::string>> graph;
  public:
    Graph();
    void readInput();
    std::map<std::string, std::list<std::string>> getGraph();
    bool DLS(std::string src, std::string target, int limit);
    int IDDFS(std::string src, std::string target, int max_depth);
};
// ===================================== End Graph Definition ===================================== //