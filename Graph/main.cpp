#include "Graph.h"

int main() {
  Graph Wikipedia;
  while (true) {
	  std::string node;
	  std::string target;
	  std::cin >> node;
	  std::cin >> target;

	  std::cout << Wikipedia.IDDFS(node, target, 100) << std::endl;
  }
}