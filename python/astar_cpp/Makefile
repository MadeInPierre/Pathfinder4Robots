CC=g++
CFLAGS=-O3 -Wall -shared -fpic -std=c++11
#LDFLAGS=
SOURCES=astar.cpp
OBJECTS=$(SOURCES:.cpp=.so)
all:
	$(CC) $(SOURCES) -o $(OBJECTS) $(CFLAGS) $(LDFLAGS)