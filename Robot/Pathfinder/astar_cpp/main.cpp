#include <iostream>

#include "AStar.hpp"
#include <chrono>

extern "C" {
	// map:        flattened h*w grid of costs
	// start, goal:    index of start/goal in flattened grid
	// paths (output): for each node, stores previous node in path
	bool astar(const uint8_t* map, const int height, const int width,
			   const int start, const int goal, const bool do_simplify,
			   int* paths) 
	{
		auto start_time = std::chrono::high_resolution_clock::now();

			AStar::Generator generator;
			generator.setWorldSize({height, width});
			generator.setHeuristic(AStar::Heuristic::euclidean);
			generator.setDiagonalMovement(true);
			//bool do_simplify = true;
			
			for (int i = 0; i < height * width; ++i)
			{
				if(map[i] == 0) { //0 is a wall, 1 is free space
					generator.addCollision({(int)(i / width), i % width});
				}
			}
				
			//std::cout << "Generate path ... \n";
			//std::cout << "Starting at coord : " << (int)(start / width) << "," << start % width << "(" << generator.detectCollision({(int)(start / width), start % width}) << " at pos)\n";
			auto path = generator.findPath( {(int)(start / width), start % width}, 
											{(int)(goal  / width), goal % width});
			


		auto current_time = std::chrono::high_resolution_clock::now();
		std::cout << " | C++ pathfinding took " << std::chrono::duration_cast<std::chrono::milliseconds>(current_time - start_time).count() << "ms." << std::endl;

			if(path.size() == 0)
				return false;

			if(do_simplify)
				path = generator.simplifyPath(path, 0.3);

			int i = 0;
			for(auto& coordinate : path) {
				//std::cout << "(" << coordinate.x << "," << coordinate.y << ", " << coordinate.x * width + coordinate.y << ") ";
				paths[i] = coordinate.x * width + coordinate.y;
				i++;
			}



		current_time = std::chrono::high_resolution_clock::now();
		std::cout << " | C++ TOTAL ran for " << std::chrono::duration_cast<std::chrono::milliseconds>(current_time - start_time).count() << "ms." << std::endl;
		std::cout << " | RESULT : " << path.size() << " waypoints.\n";
		return true;
	}
}