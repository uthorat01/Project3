#include "Graph.h"

int main() {
  Graph Wikipedia;
  while (true) {
	  std::string node;
	  std::string target;
	  std::cin >> node;
	  std::cin >> target;

	  auto t1 = std::chrono::high_resolution_clock::now();
	  std::pair<int, std::string> iddfs = Wikipedia.IDDFS(node, target);
	  auto t2 = std::chrono::high_resolution_clock::now();
	  std::cout << "IDDFS run time: " << std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count() << " ms|";

	  t1 = std::chrono::high_resolution_clock::now();
	  int bfs = Wikipedia.BFS(node, target);
	  t2 = std::chrono::high_resolution_clock::now();
	  std::cout << "BFS run time: " << std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count() << " ms|";

	  std::cout << iddfs.first << "|" << bfs << "|" << node + " -> " << iddfs.second.substr(0, iddfs.second.size()-4);
	  return 0;
  }
}