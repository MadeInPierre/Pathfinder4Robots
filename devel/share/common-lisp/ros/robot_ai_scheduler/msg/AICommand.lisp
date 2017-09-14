; Auto-generated. Do not edit!


(cl:in-package robot_ai_scheduler-msg)


;//! \htmlinclude AICommand.msg.html

(cl:defclass <AICommand> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (command
    :reader command
    :initarg :command
    :type cl:string
    :initform "")
   (params
    :reader params
    :initarg :params
    :type cl:string
    :initform ""))
)

(cl:defclass AICommand (<AICommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AICommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AICommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_ai_scheduler-msg:<AICommand> is deprecated: use robot_ai_scheduler-msg:AICommand instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <AICommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai_scheduler-msg:header-val is deprecated.  Use robot_ai_scheduler-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'command-val :lambda-list '(m))
(cl:defmethod command-val ((m <AICommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai_scheduler-msg:command-val is deprecated.  Use robot_ai_scheduler-msg:command instead.")
  (command m))

(cl:ensure-generic-function 'params-val :lambda-list '(m))
(cl:defmethod params-val ((m <AICommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai_scheduler-msg:params-val is deprecated.  Use robot_ai_scheduler-msg:params instead.")
  (params m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AICommand>) ostream)
  "Serializes a message object of type '<AICommand>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'command))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'command))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'params))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'params))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AICommand>) istream)
  "Deserializes a message object of type '<AICommand>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'command) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'command) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'params) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'params) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AICommand>)))
  "Returns string type for a message object of type '<AICommand>"
  "robot_ai_scheduler/AICommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AICommand)))
  "Returns string type for a message object of type 'AICommand"
  "robot_ai_scheduler/AICommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AICommand>)))
  "Returns md5sum for a message object of type '<AICommand>"
  "c39e2f3e5a34d4649f4b40daf60fbb03")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AICommand)))
  "Returns md5sum for a message object of type 'AICommand"
  "c39e2f3e5a34d4649f4b40daf60fbb03")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AICommand>)))
  "Returns full string definition for message of type '<AICommand>"
  (cl:format cl:nil "Header header~%string command~%string params~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AICommand)))
  "Returns full string definition for message of type 'AICommand"
  (cl:format cl:nil "Header header~%string command~%string params~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AICommand>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:length (cl:slot-value msg 'command))
     4 (cl:length (cl:slot-value msg 'params))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AICommand>))
  "Converts a ROS message object to a list"
  (cl:list 'AICommand
    (cl:cons ':header (header msg))
    (cl:cons ':command (command msg))
    (cl:cons ':params (params msg))
))
