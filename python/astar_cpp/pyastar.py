import ctypes, cv2
from time import time
import numpy as np

class PyAstarCPP():
    def __init__(self):
        lib = ctypes.cdll.LoadLibrary('astar_cpp/main.so') #TODO danger
        self.ASTAR = lib.astar
        ndmat_f_type = np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, flags='C_CONTIGUOUS')
        ndmat_i_type = np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='C_CONTIGUOUS')
        self.ASTAR.restype = ctypes.c_bool
        self.ASTAR.argtypes = [ndmat_f_type, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_bool, ndmat_i_type]


    def findPath(self, collision_map, start, goal):
        height, width = collision_map.shape[:2]
        MAP = cv2.cvtColor(collision_map, cv2.COLOR_BGR2GRAY).astype(np.float32)
        start_idx = np.ravel_multi_index(start[::-1], (height, width))
        goal_idx = np.ravel_multi_index(goal[::-1], (height, width))

        paths = np.full(height * width, -1, dtype = np.int32)

        success =  self.ASTAR(MAP.flatten(), 100, 150, start_idx, goal_idx, True, paths) # paths is the output parameter
        #print "success : {0}, path : {1}".format(success, paths)


        if not success:
            return np.array([])

        coordinates = []
        for p_idx in paths:
            if p_idx == -1:
                break
            pi, pj = np.unravel_index(p_idx, (height, width))
            coordinates.append((pj, pi)) # revert back to x, y

        if coordinates:
            return np.vstack(coordinates[::-1])
        else:
            return np.array([])

        return []