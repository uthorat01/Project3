#include <fstream>
#include <iostream>
#include <map>
#include <list>
#include <sstream>


int main() {
    std::ifstream fin("filtered.csv");
    std::map<std::string,std::list<std::string>> graph;
    std::string line,page,input;
    std::list<std::string> adj;
    if(fin.is_open()) {;
        while (getline(fin, line)) {
            adj.clear();
            std::stringstream s(line);
            while (getline(s, page, ',')) {
                adj.push_back(page.substr(page.find_last_of('/')));
            }
            std::string startPage = adj.front();
            adj.pop_front();
            graph[startPage] = adj;
        }
    }
}

