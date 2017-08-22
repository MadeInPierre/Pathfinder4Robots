#include "AStar.hpp"
#include <algorithm>

using namespace std::placeholders;

bool AStar::Vec2i::operator == (const Vec2i& coordinates_) {
    return (x == coordinates_.x && y == coordinates_.y);
}

AStar::Vec2i operator + (const AStar::Vec2i& left_, const AStar::Vec2i& right_) {
    return{ left_.x + right_.x, left_.y + right_.y };
}

AStar::Node::Node(Vec2i coordinates_, Node *parent_) {
    parent = parent_;
    coordinates = coordinates_;
    G = H = 0;
}

AStar::uint AStar::Node::getScore() {
    return G + H;
}

AStar::Generator::Generator() {
    setDiagonalMovement(false);
    setHeuristic(&Heuristic::manhattan);
    direction = { 
        { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 },
        { -1, -1 }, { 1, 1 }, { -1, 1 }, { 1, -1 }
    };
}

void AStar::Generator::setWorldSize(Vec2i worldSize_) {
    worldSize = worldSize_;
}

void AStar::Generator::setDiagonalMovement(bool enable_) {
    directions = (enable_ ? 8 : 4);
}

void AStar::Generator::setHeuristic(HeuristicFunction heuristic_) {
    heuristic = std::bind(heuristic_, _1, _2);
}

void AStar::Generator::addCollision(Vec2i coordinates_)
{
    walls.push_back(coordinates_);
}

void AStar::Generator::removeCollision(Vec2i coordinates_) {
    auto it = std::find(walls.begin(), walls.end(), coordinates_);
    if (it != walls.end()) {
        walls.erase(it);
    }
}

void AStar::Generator::clearCollisions() {
    walls.clear();
}

AStar::CoordinateList AStar::Generator::findPath(Vec2i source_, Vec2i target_) {
    CoordinateList path;

    if(detectCollision(source_) || detectCollision(target_)) {
        std::cout << " | ERROR Invalid start or target position. Outside the map or in a wall.\n";
        return path;
    }

    const int MAX_TRIES = 500;
    int tries = 0;

    Node *current = nullptr;
    NodeSet openSet, closedSet;
    openSet.insert(new Node(source_));

    while (!openSet.empty() && tries <= MAX_TRIES) {
        current = *openSet.begin();
        for (auto node : openSet) {
            if (node->getScore() <= current->getScore()) {
                current = node;
            }
        }

        if (current->coordinates == target_) {
            break;
        }

        closedSet.insert(current);
        openSet.erase(std::find(openSet.begin(), openSet.end(), current));

        for (uint i = 0; i < directions; ++i) {
            Vec2i newCoordinates(current->coordinates + direction[i]);
            if (detectCollision(newCoordinates) ||
                findNodeOnList(closedSet, newCoordinates)) {
                continue;
            }

            uint totalCost = current->G + ((i < 4) ? 10 : 14);

            Node *successor = findNodeOnList(openSet, newCoordinates);
            if (successor == nullptr) {
                successor = new Node(newCoordinates, current);
                successor->G = totalCost;
                successor->H = heuristic(successor->coordinates, target_);
                openSet.insert(successor);
            }
            else if (totalCost < successor->G) {
                successor->parent = current;
                successor->G = totalCost;
            }
        }

        tries++;
    }


    if(tries == MAX_TRIES) {
        return path;
    }

    while (current != nullptr) {
        path.push_back(current->coordinates);
        current = current->parent;
    }

    releaseNodes(openSet);
    releaseNodes(closedSet);

    return path;
}

AStar::Node* AStar::Generator::findNodeOnList(NodeSet& nodes_, Vec2i coordinates_) {
    for (auto node : nodes_) {
        if (node->coordinates == coordinates_) {
            return node;
        }
    }
    return nullptr;
}

void AStar::Generator::releaseNodes(NodeSet& nodes_) {
    for (auto it = nodes_.begin(); it != nodes_.end();) {
        delete *it;
        it = nodes_.erase(it);
    }
}

bool AStar::Generator::detectCollision(Vec2i coordinates_) {
    if (coordinates_.x < 0 || coordinates_.x >= worldSize.x ||
        coordinates_.y < 0 || coordinates_.y >= worldSize.y ||
        std::find(walls.begin(), walls.end(), coordinates_) != walls.end()) {
        return true;
    }
    return false;
}

AStar::Vec2i AStar::Heuristic::getDelta(Vec2i source_, Vec2i target_) {
    return{ abs(source_.x - target_.x),  abs(source_.y - target_.y) };
}

AStar::uint AStar::Heuristic::manhattan(Vec2i source_, Vec2i target_) {
    auto delta = std::move(getDelta(source_, target_));
    return static_cast<uint>(10 * (delta.x + delta.y));
}

AStar::uint AStar::Heuristic::euclidean(Vec2i source_, Vec2i target_) {
    auto delta = std::move(getDelta(source_, target_));
    return static_cast<uint>(10 * /*sqrt*/(pow(delta.x, 2) + pow(delta.y, 2)));
}

AStar::uint AStar::Heuristic::octagonal(Vec2i source_, Vec2i target_) {
    auto delta = std::move(getDelta(source_, target_));
    return 10 * (delta.x + delta.y) + (-6) * std::min(delta.x, delta.y);
}




/*=====================================
=            Simplify Path            =
=====================================*/

AStar::CoordinateList AStar::Generator::simplifyPath(CoordinateList path, float tolerance) {
    AStar::CoordinateList simplified_path = douglaspeucker(path, tolerance);
    simplified_path.insert(simplified_path.end(), path.end() - 1, path.end());
    return simplified_path;
}

AStar::CoordinateList AStar::Generator::douglaspeucker(CoordinateList path, float tolerance) {
    float dmax = 0;
    int index = 0;

    for (int i = 1; i < (int)path.size(); ++i){
        float d = distance_point_to_line(path[i], path[0], path[path.size() - 1]);
        if(d > dmax) {
            index = i;
            dmax = d;
        }
    }

    if(dmax > tolerance) {
        AStar::CoordinateList recResults1 = douglaspeucker((AStar::CoordinateList)std::vector<Vec2i>(path.begin(), path.begin() + index), tolerance); ////////
        AStar::CoordinateList recResults2 = douglaspeucker((AStar::CoordinateList)std::vector<Vec2i>(path.begin() + index, path.end()), tolerance); ////////
        recResults1.insert(recResults1.end(), recResults2.begin(), recResults2.end());
        return recResults1;
    } else {
        AStar::CoordinateList result;
        result.insert(result.end(), path.begin(), path.begin() + 1);
        return result;
    }
}

float AStar::Generator::distance_point_to_line(Vec2i point, Vec2i p1, Vec2i p2) {
    return  (float)(abs((p2.y - p1.y)*point.x - (p2.x - p1.x)*point.y + p2.x*p1.y - p2.y*p1.x) / 
            (float)(sqrt( pow(p2.y - p1.y, 2) + pow(p2.x - p1.x, 2) )));
}


/*=====  End of Simplify Path  ======*/
