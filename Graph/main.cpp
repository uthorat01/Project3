#include "Graph.h"
#include <cctype>

/*The int main() of this project creates a Graph object representing the Wikipedia section for animals
 * and then takes in source and target page from the users input of the GUI.This input is changed to
 * the correct format and then BFS and IDDFS are run to find the between the source and target Wikipedia
 * pages. The distance, runtime of BFS and IDDFS, and path are printed and outputted to the user through
 * the GUI*/
int main() {
    Graph Wikipedia;
    std::string node;
    std::string target;
    std::cin >> node;
    std::cin >> target;

    for (char a : node)
        a = std::tolower(a);
    node[0] = std::toupper(node[0]);
    for (char a : target)
        a = std::tolower(a);
    target[0] = std::toupper(target[0]);

    auto t1 = std::chrono::steady_clock::now();
    std::pair<int, std::string> iddfs = Wikipedia.IDDFS(node, target);
    auto t2 = std::chrono::steady_clock::now();
    std::string iddfstime =
            "IDDFS Runtime: " + std::to_string(std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count()) +
            " ms|";

    t1 = std::chrono::steady_clock::now();
    int bfs = Wikipedia.BFS(node, target);
    t2 = std::chrono::steady_clock::now();
    std::string bfstime =
            "BFS Runtime: " + std::to_string(std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count()) +
            " ms|";

    if (iddfs.first == INT_MAX || bfs == INT_MAX) {
        std::cout << "IDDFS Runtime: N/A|" << "BFS Runtime: N/A|" << "Distance: N/A|" << "Distance: N/A|"
                  << "The inputted source or target topics do not exist as Wikipedia pages or are not categorized as an animal related page.";
    } else {
        std::cout << iddfstime << bfstime << "Distance: " << iddfs.first << " page(s)|Distance: " << bfs << " page(s)|"
                  << node + " -> " << iddfs.second.substr(0, iddfs.second.size() - 4);
    }
    return 0;
}