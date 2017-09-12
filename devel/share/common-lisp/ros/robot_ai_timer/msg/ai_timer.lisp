; Auto-generated. Do not edit!


(cl:in-package robot_ai_timer-msg)


;//! \htmlinclude ai_timer.msg.html

(cl:defclass <ai_timer> (roslisp-msg-protocol:ros-message)
  ((elapsed_time
    :reader elapsed_time
    :initarg :elapsed_time
    :type cl:float
    :initform 0.0)
   (time_left
    :reader time_left
    :initarg :time_left
    :type cl:float
    :initform 0.0)
   (is_finished
    :reader is_finished
    :initarg :is_finished
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ai_timer (<ai_timer>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ai_timer>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ai_timer)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_ai_timer-msg:<ai_timer> is deprecated: use robot_ai_timer-msg:ai_timer instead.")))

(cl:ensure-generic-function 'elapsed_time-val :lambda-list '(m))
(cl:defmethod elapsed_time-val ((m <ai_timer>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai_timer-msg:elapsed_time-val is deprecated.  Use robot_ai_timer-msg:elapsed_time instead.")
  (elapsed_time m))

(cl:ensure-generic-function 'time_left-val :lambda-list '(m))
(cl:defmethod time_left-val ((m <ai_timer>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai_timer-msg:time_left-val is deprecated.  Use robot_ai_timer-msg:time_left instead.")
  (time_left m))

(cl:ensure-generic-function 'is_finished-val :lambda-list '(m))
(cl:defmethod is_finished-val ((m <ai_timer>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai_timer-msg:is_finished-val is deprecated.  Use robot_ai_timer-msg:is_finished instead.")
  (is_finished m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ai_timer>) ostream)
  "Serializes a message object of type '<ai_timer>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'elapsed_time))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'time_left))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'is_finished) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ai_timer>) istream)
  "Deserializes a message object of type '<ai_timer>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'elapsed_time) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'time_left) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'is_finished) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ai_timer>)))
  "Returns string type for a message object of type '<ai_timer>"
  "robot_ai_timer/ai_timer")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ai_timer)))
  "Returns string type for a message object of type 'ai_timer"
  "robot_ai_timer/ai_timer")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ai_timer>)))
  "Returns md5sum for a message object of type '<ai_timer>"
  "c4cb09c8090b9afd36452fbb8fd74941")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ai_timer)))
  "Returns md5sum for a message object of type 'ai_timer"
  "c4cb09c8090b9afd36452fbb8fd74941")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ai_timer>)))
  "Returns full string definition for message of type '<ai_timer>"
  (cl:format cl:nil "float32 elapsed_time~%float32 time_left~%bool is_finished~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ai_timer)))
  "Returns full string definition for message of type 'ai_timer"
  (cl:format cl:nil "float32 elapsed_time~%float32 time_left~%bool is_finished~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ai_timer>))
  (cl:+ 0
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ai_timer>))
  "Converts a ROS message object to a list"
  (cl:list 'ai_timer
    (cl:cons ':elapsed_time (elapsed_time msg))
    (cl:cons ':time_left (time_left msg))
    (cl:cons ':is_finished (is_finished msg))
))
