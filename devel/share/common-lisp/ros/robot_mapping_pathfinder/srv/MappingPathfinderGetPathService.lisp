; Auto-generated. Do not edit!


(cl:in-package robot_mapping_pathfinder-srv)


;//! \htmlinclude MappingPathfinderGetPathService-request.msg.html

(cl:defclass <MappingPathfinderGetPathService-request> (roslisp-msg-protocol:ros-message)
  ((startpos
    :reader startpos
    :initarg :startpos
    :type geometry_msgs-msg:Pose2D
    :initform (cl:make-instance 'geometry_msgs-msg:Pose2D))
   (endpos
    :reader endpos
    :initarg :endpos
    :type geometry_msgs-msg:Pose2D
    :initform (cl:make-instance 'geometry_msgs-msg:Pose2D)))
)

(cl:defclass MappingPathfinderGetPathService-request (<MappingPathfinderGetPathService-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MappingPathfinderGetPathService-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MappingPathfinderGetPathService-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_mapping_pathfinder-srv:<MappingPathfinderGetPathService-request> is deprecated: use robot_mapping_pathfinder-srv:MappingPathfinderGetPathService-request instead.")))

(cl:ensure-generic-function 'startpos-val :lambda-list '(m))
(cl:defmethod startpos-val ((m <MappingPathfinderGetPathService-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_mapping_pathfinder-srv:startpos-val is deprecated.  Use robot_mapping_pathfinder-srv:startpos instead.")
  (startpos m))

(cl:ensure-generic-function 'endpos-val :lambda-list '(m))
(cl:defmethod endpos-val ((m <MappingPathfinderGetPathService-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_mapping_pathfinder-srv:endpos-val is deprecated.  Use robot_mapping_pathfinder-srv:endpos instead.")
  (endpos m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MappingPathfinderGetPathService-request>) ostream)
  "Serializes a message object of type '<MappingPathfinderGetPathService-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'startpos) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'endpos) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MappingPathfinderGetPathService-request>) istream)
  "Deserializes a message object of type '<MappingPathfinderGetPathService-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'startpos) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'endpos) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MappingPathfinderGetPathService-request>)))
  "Returns string type for a service object of type '<MappingPathfinderGetPathService-request>"
  "robot_mapping_pathfinder/MappingPathfinderGetPathServiceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MappingPathfinderGetPathService-request)))
  "Returns string type for a service object of type 'MappingPathfinderGetPathService-request"
  "robot_mapping_pathfinder/MappingPathfinderGetPathServiceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MappingPathfinderGetPathService-request>)))
  "Returns md5sum for a message object of type '<MappingPathfinderGetPathService-request>"
  "faeb4d9752daba214ce90de021e3676d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MappingPathfinderGetPathService-request)))
  "Returns md5sum for a message object of type 'MappingPathfinderGetPathService-request"
  "faeb4d9752daba214ce90de021e3676d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MappingPathfinderGetPathService-request>)))
  "Returns full string definition for message of type '<MappingPathfinderGetPathService-request>"
  (cl:format cl:nil "geometry_msgs/Pose2D startpos~%geometry_msgs/Pose2D endpos~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MappingPathfinderGetPathService-request)))
  "Returns full string definition for message of type 'MappingPathfinderGetPathService-request"
  (cl:format cl:nil "geometry_msgs/Pose2D startpos~%geometry_msgs/Pose2D endpos~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MappingPathfinderGetPathService-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'startpos))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'endpos))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MappingPathfinderGetPathService-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MappingPathfinderGetPathService-request
    (cl:cons ':startpos (startpos msg))
    (cl:cons ':endpos (endpos msg))
))
;//! \htmlinclude MappingPathfinderGetPathService-response.msg.html

(cl:defclass <MappingPathfinderGetPathService-response> (roslisp-msg-protocol:ros-message)
  ((waypoints
    :reader waypoints
    :initarg :waypoints
    :type (cl:vector geometry_msgs-msg:Pose2D)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Pose2D :initial-element (cl:make-instance 'geometry_msgs-msg:Pose2D))))
)

(cl:defclass MappingPathfinderGetPathService-response (<MappingPathfinderGetPathService-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MappingPathfinderGetPathService-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MappingPathfinderGetPathService-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_mapping_pathfinder-srv:<MappingPathfinderGetPathService-response> is deprecated: use robot_mapping_pathfinder-srv:MappingPathfinderGetPathService-response instead.")))

(cl:ensure-generic-function 'waypoints-val :lambda-list '(m))
(cl:defmethod waypoints-val ((m <MappingPathfinderGetPathService-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_mapping_pathfinder-srv:waypoints-val is deprecated.  Use robot_mapping_pathfinder-srv:waypoints instead.")
  (waypoints m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MappingPathfinderGetPathService-response>) ostream)
  "Serializes a message object of type '<MappingPathfinderGetPathService-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'waypoints))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'waypoints))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MappingPathfinderGetPathService-response>) istream)
  "Deserializes a message object of type '<MappingPathfinderGetPathService-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'waypoints) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'waypoints)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Pose2D))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MappingPathfinderGetPathService-response>)))
  "Returns string type for a service object of type '<MappingPathfinderGetPathService-response>"
  "robot_mapping_pathfinder/MappingPathfinderGetPathServiceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MappingPathfinderGetPathService-response)))
  "Returns string type for a service object of type 'MappingPathfinderGetPathService-response"
  "robot_mapping_pathfinder/MappingPathfinderGetPathServiceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MappingPathfinderGetPathService-response>)))
  "Returns md5sum for a message object of type '<MappingPathfinderGetPathService-response>"
  "faeb4d9752daba214ce90de021e3676d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MappingPathfinderGetPathService-response)))
  "Returns md5sum for a message object of type 'MappingPathfinderGetPathService-response"
  "faeb4d9752daba214ce90de021e3676d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MappingPathfinderGetPathService-response>)))
  "Returns full string definition for message of type '<MappingPathfinderGetPathService-response>"
  (cl:format cl:nil "geometry_msgs/Pose2D[] waypoints~%~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MappingPathfinderGetPathService-response)))
  "Returns full string definition for message of type 'MappingPathfinderGetPathService-response"
  (cl:format cl:nil "geometry_msgs/Pose2D[] waypoints~%~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MappingPathfinderGetPathService-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'waypoints) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MappingPathfinderGetPathService-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MappingPathfinderGetPathService-response
    (cl:cons ':waypoints (waypoints msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MappingPathfinderGetPathService)))
  'MappingPathfinderGetPathService-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MappingPathfinderGetPathService)))
  'MappingPathfinderGetPathService-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MappingPathfinderGetPathService)))
  "Returns string type for a service object of type '<MappingPathfinderGetPathService>"
  "robot_mapping_pathfinder/MappingPathfinderGetPathService")