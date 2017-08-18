import ctypes, cv2
from time import time
import numpy as np


class PyAstar():
    def __init__(self):
        lib = ctypes.cdll.LoadLibrary('astar_cpp/astar.so') # TODO danger

        self.ASTAR = lib.astar
        ndmat_f_type = np.ctypeslib.ndpointer(
            dtype=np.float32, ndim=1, flags='C_CONTIGUOUS')
        ndmat_i_type = np.ctypeslib.ndpointer(
            dtype=np.int32, ndim=1, flags='C_CONTIGUOUS')
        self.ASTAR.restype = ctypes.c_bool
        self.ASTAR.argtypes = [ndmat_f_type, ctypes.c_int, ctypes.c_int,
                                ctypes.c_int, ctypes.c_int,
                                ndmat_i_type]
        self.GRID = None

    def updateMap(self, img):
        self.GRID = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
        self.GRID[self.GRID == 0] = np.inf
        self.GRID[self.GRID == 255] = 1
        assert self.GRID.min() == 1, 'cost of moving must be at least 1'

    def findPath(self, start, end):
        if self.GRID is None:
            raise ValueError, "Map image has not been loaded."
        else:
            print('loaded map of size %r' % (self.GRID.shape[0:2],))

        start = np.array(start)
        end = np.array(end)
        print "Starting at {0}, ending at {1}".format(start, end)

        t0 = time()
        path = self.execute(self.GRID, start, end)
        dur = time() - t0
        print path

        if path.shape[0] > 0:
            print('found path of length %d in %.2fms' % (path.shape[0], dur*1000))
            return path
            '''
            #save map with solution
            maze[path[:, 0], path[:, 1]] = (0, 0, 255)

            print('plotting path to %s' % (OUTP_FPATH))
            cv2.imwrite(OUTP_FPATH, maze)
            '''
        else:
            print('no path found')
            return []

        

    def execute(self, weights, start, goal):
        assert weights.min(axis=None) >= 1., ('weights.min() = %.2f != 1' % weights.min(axis=None))
        height, width = weights.shape
        start_idx = np.ravel_multi_index(start, (height, width))
        goal_idx = np.ravel_multi_index(goal, (height, width))

        paths = np.full(height * width, -1, dtype=np.int32)

        success = self.ASTAR(
            weights.flatten(), height, width, start_idx, goal_idx,
            paths  # output parameter
        )

        if not success:
            return np.array([])

        coordinates = []
        path_idx = goal_idx
        while path_idx != start_idx:
            pi, pj = np.unravel_index(path_idx, (height, width))
            coordinates.append((pi, pj))

            path_idx = paths[path_idx]

        if coordinates:
            return np.vstack(coordinates[::-1])
        else:
            return np.array([])
