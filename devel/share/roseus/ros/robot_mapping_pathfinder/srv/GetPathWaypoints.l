;; Auto-generated. Do not edit!


(when (boundp 'robot_mapping_pathfinder::GetPathWaypoints)
  (if (not (find-package "ROBOT_MAPPING_PATHFINDER"))
    (make-package "ROBOT_MAPPING_PATHFINDER"))
  (shadow 'GetPathWaypoints (find-package "ROBOT_MAPPING_PATHFINDER")))
(unless (find-package "ROBOT_MAPPING_PATHFINDER::GETPATHWAYPOINTS")
  (make-package "ROBOT_MAPPING_PATHFINDER::GETPATHWAYPOINTS"))
(unless (find-package "ROBOT_MAPPING_PATHFINDER::GETPATHWAYPOINTSREQUEST")
  (make-package "ROBOT_MAPPING_PATHFINDER::GETPATHWAYPOINTSREQUEST"))
(unless (find-package "ROBOT_MAPPING_PATHFINDER::GETPATHWAYPOINTSRESPONSE")
  (make-package "ROBOT_MAPPING_PATHFINDER::GETPATHWAYPOINTSRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass robot_mapping_pathfinder::GetPathWaypointsRequest
  :super ros::object
  :slots (_startpos _endpos ))

(defmethod robot_mapping_pathfinder::GetPathWaypointsRequest
  (:init
   (&key
    ((:startpos __startpos) (instance geometry_msgs::Pose2D :init))
    ((:endpos __endpos) (instance geometry_msgs::Pose2D :init))
    )
   (send-super :init)
   (setq _startpos __startpos)
   (setq _endpos __endpos)
   self)
  (:startpos
   (&rest __startpos)
   (if (keywordp (car __startpos))
       (send* _startpos __startpos)
     (progn
       (if __startpos (setq _startpos (car __startpos)))
       _startpos)))
  (:endpos
   (&rest __endpos)
   (if (keywordp (car __endpos))
       (send* _endpos __endpos)
     (progn
       (if __endpos (setq _endpos (car __endpos)))
       _endpos)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Pose2D _startpos
    (send _startpos :serialization-length)
    ;; geometry_msgs/Pose2D _endpos
    (send _endpos :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose2D _startpos
       (send _startpos :serialize s)
     ;; geometry_msgs/Pose2D _endpos
       (send _endpos :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose2D _startpos
     (send _startpos :deserialize buf ptr-) (incf ptr- (send _startpos :serialization-length))
   ;; geometry_msgs/Pose2D _endpos
     (send _endpos :deserialize buf ptr-) (incf ptr- (send _endpos :serialization-length))
   ;;
   self)
  )

(defclass robot_mapping_pathfinder::GetPathWaypointsResponse
  :super ros::object
  :slots (_waypoints ))

(defmethod robot_mapping_pathfinder::GetPathWaypointsResponse
  (:init
   (&key
    ((:waypoints __waypoints) (let (r) (dotimes (i 0) (push (instance geometry_msgs::Pose2D :init) r)) r))
    )
   (send-super :init)
   (setq _waypoints __waypoints)
   self)
  (:waypoints
   (&rest __waypoints)
   (if (keywordp (car __waypoints))
       (send* _waypoints __waypoints)
     (progn
       (if __waypoints (setq _waypoints (car __waypoints)))
       _waypoints)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Pose2D[] _waypoints
    (apply #'+ (send-all _waypoints :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose2D[] _waypoints
     (write-long (length _waypoints) s)
     (dolist (elem _waypoints)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose2D[] _waypoints
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _waypoints (let (r) (dotimes (i n) (push (instance geometry_msgs::Pose2D :init) r)) r))
     (dolist (elem- _waypoints)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(defclass robot_mapping_pathfinder::GetPathWaypoints
  :super ros::object
  :slots ())

(setf (get robot_mapping_pathfinder::GetPathWaypoints :md5sum-) "faeb4d9752daba214ce90de021e3676d")
(setf (get robot_mapping_pathfinder::GetPathWaypoints :datatype-) "robot_mapping_pathfinder/GetPathWaypoints")
(setf (get robot_mapping_pathfinder::GetPathWaypoints :request) robot_mapping_pathfinder::GetPathWaypointsRequest)
(setf (get robot_mapping_pathfinder::GetPathWaypoints :response) robot_mapping_pathfinder::GetPathWaypointsResponse)

(defmethod robot_mapping_pathfinder::GetPathWaypointsRequest
  (:response () (instance robot_mapping_pathfinder::GetPathWaypointsResponse :init)))

(setf (get robot_mapping_pathfinder::GetPathWaypointsRequest :md5sum-) "faeb4d9752daba214ce90de021e3676d")
(setf (get robot_mapping_pathfinder::GetPathWaypointsRequest :datatype-) "robot_mapping_pathfinder/GetPathWaypointsRequest")
(setf (get robot_mapping_pathfinder::GetPathWaypointsRequest :definition-)
      "geometry_msgs/Pose2D startpos
geometry_msgs/Pose2D endpos

================================================================================
MSG: geometry_msgs/Pose2D
# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
---
geometry_msgs/Pose2D[] waypoints


================================================================================
MSG: geometry_msgs/Pose2D
# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
")

(setf (get robot_mapping_pathfinder::GetPathWaypointsResponse :md5sum-) "faeb4d9752daba214ce90de021e3676d")
(setf (get robot_mapping_pathfinder::GetPathWaypointsResponse :datatype-) "robot_mapping_pathfinder/GetPathWaypointsResponse")
(setf (get robot_mapping_pathfinder::GetPathWaypointsResponse :definition-)
      "geometry_msgs/Pose2D startpos
geometry_msgs/Pose2D endpos

================================================================================
MSG: geometry_msgs/Pose2D
# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
---
geometry_msgs/Pose2D[] waypoints


================================================================================
MSG: geometry_msgs/Pose2D
# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
")



(provide :robot_mapping_pathfinder/GetPathWaypoints "faeb4d9752daba214ce90de021e3676d")


