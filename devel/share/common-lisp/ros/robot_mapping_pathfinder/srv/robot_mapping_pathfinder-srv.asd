
(cl:in-package :asdf)

(defsystem "robot_mapping_pathfinder-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "GetPathWaypoints" :depends-on ("_package_GetPathWaypoints"))
    (:file "_package_GetPathWaypoints" :depends-on ("_package"))
  ))