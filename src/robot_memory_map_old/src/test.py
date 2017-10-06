from MapManager import MapManager, MapVisualizer
import Pathfinder as PF

mapman = MapManager("map.json")
#map.containerTransfer(map.getObject("tower_1").Chest, map.getEntity("ROBOT").Chest, "module_1")

#Pathfinder
start = mapman.getEntity("ROBOT").Position.tuple2()
goal  = ( 600 , 600  )
goal  = ( 2757, 988  )
goal  = ( 800 , 1100 )
goal  = ( 1700, 1450 )
goal  = ( 2700, 1800 ) # impossible path
goal  = ( 1400, 600  )
pfinder = PF.Pathfinder()
path = pfinder.Execute(mapman, start, goal)
mapman.getEntity("ROBOT").setCurrentPath(path)



# Debug visualize
mapman.updateVizImg()
viz = MapVisualizer()
viz.Draw(mapman.getVizImg(), mapman.getCollisionImg())

