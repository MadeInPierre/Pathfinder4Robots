; Auto-generated. Do not edit!


(cl:in-package robot_ai-srv)


;//! \htmlinclude AIGenericCommand-request.msg.html

(cl:defclass <AIGenericCommand-request> (roslisp-msg-protocol:ros-message)
  ((department
    :reader department
    :initarg :department
    :type cl:string
    :initform "")
   (destination
    :reader destination
    :initarg :destination
    :type cl:string
    :initform "")
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

(cl:defclass AIGenericCommand-request (<AIGenericCommand-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AIGenericCommand-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AIGenericCommand-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_ai-srv:<AIGenericCommand-request> is deprecated: use robot_ai-srv:AIGenericCommand-request instead.")))

(cl:ensure-generic-function 'department-val :lambda-list '(m))
(cl:defmethod department-val ((m <AIGenericCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai-srv:department-val is deprecated.  Use robot_ai-srv:department instead.")
  (department m))

(cl:ensure-generic-function 'destination-val :lambda-list '(m))
(cl:defmethod destination-val ((m <AIGenericCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai-srv:destination-val is deprecated.  Use robot_ai-srv:destination instead.")
  (destination m))

(cl:ensure-generic-function 'command-val :lambda-list '(m))
(cl:defmethod command-val ((m <AIGenericCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai-srv:command-val is deprecated.  Use robot_ai-srv:command instead.")
  (command m))

(cl:ensure-generic-function 'params-val :lambda-list '(m))
(cl:defmethod params-val ((m <AIGenericCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai-srv:params-val is deprecated.  Use robot_ai-srv:params instead.")
  (params m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AIGenericCommand-request>) ostream)
  "Serializes a message object of type '<AIGenericCommand-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'department))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'department))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'destination))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'destination))
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AIGenericCommand-request>) istream)
  "Deserializes a message object of type '<AIGenericCommand-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'department) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'department) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'destination) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'destination) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AIGenericCommand-request>)))
  "Returns string type for a service object of type '<AIGenericCommand-request>"
  "robot_ai/AIGenericCommandRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AIGenericCommand-request)))
  "Returns string type for a service object of type 'AIGenericCommand-request"
  "robot_ai/AIGenericCommandRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AIGenericCommand-request>)))
  "Returns md5sum for a message object of type '<AIGenericCommand-request>"
  "0bbc3ecedf61307352ea72431f6a44e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AIGenericCommand-request)))
  "Returns md5sum for a message object of type 'AIGenericCommand-request"
  "0bbc3ecedf61307352ea72431f6a44e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AIGenericCommand-request>)))
  "Returns full string definition for message of type '<AIGenericCommand-request>"
  (cl:format cl:nil "string department~%string destination~%string command~%string params~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AIGenericCommand-request)))
  "Returns full string definition for message of type 'AIGenericCommand-request"
  (cl:format cl:nil "string department~%string destination~%string command~%string params~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AIGenericCommand-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'department))
     4 (cl:length (cl:slot-value msg 'destination))
     4 (cl:length (cl:slot-value msg 'command))
     4 (cl:length (cl:slot-value msg 'params))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AIGenericCommand-request>))
  "Converts a ROS message object to a list"
  (cl:list 'AIGenericCommand-request
    (cl:cons ':department (department msg))
    (cl:cons ':destination (destination msg))
    (cl:cons ':command (command msg))
    (cl:cons ':params (params msg))
))
;//! \htmlinclude AIGenericCommand-response.msg.html

(cl:defclass <AIGenericCommand-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil)
   (reason
    :reader reason
    :initarg :reason
    :type cl:string
    :initform ""))
)

(cl:defclass AIGenericCommand-response (<AIGenericCommand-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AIGenericCommand-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AIGenericCommand-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_ai-srv:<AIGenericCommand-response> is deprecated: use robot_ai-srv:AIGenericCommand-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <AIGenericCommand-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai-srv:success-val is deprecated.  Use robot_ai-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'reason-val :lambda-list '(m))
(cl:defmethod reason-val ((m <AIGenericCommand-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_ai-srv:reason-val is deprecated.  Use robot_ai-srv:reason instead.")
  (reason m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AIGenericCommand-response>) ostream)
  "Serializes a message object of type '<AIGenericCommand-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'reason))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'reason))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AIGenericCommand-response>) istream)
  "Deserializes a message object of type '<AIGenericCommand-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'reason) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'reason) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AIGenericCommand-response>)))
  "Returns string type for a service object of type '<AIGenericCommand-response>"
  "robot_ai/AIGenericCommandResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AIGenericCommand-response)))
  "Returns string type for a service object of type 'AIGenericCommand-response"
  "robot_ai/AIGenericCommandResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AIGenericCommand-response>)))
  "Returns md5sum for a message object of type '<AIGenericCommand-response>"
  "0bbc3ecedf61307352ea72431f6a44e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AIGenericCommand-response)))
  "Returns md5sum for a message object of type 'AIGenericCommand-response"
  "0bbc3ecedf61307352ea72431f6a44e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AIGenericCommand-response>)))
  "Returns full string definition for message of type '<AIGenericCommand-response>"
  (cl:format cl:nil "bool success~%string reason~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AIGenericCommand-response)))
  "Returns full string definition for message of type 'AIGenericCommand-response"
  (cl:format cl:nil "bool success~%string reason~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AIGenericCommand-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'reason))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AIGenericCommand-response>))
  "Converts a ROS message object to a list"
  (cl:list 'AIGenericCommand-response
    (cl:cons ':success (success msg))
    (cl:cons ':reason (reason msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'AIGenericCommand)))
  'AIGenericCommand-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'AIGenericCommand)))
  'AIGenericCommand-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AIGenericCommand)))
  "Returns string type for a service object of type '<AIGenericCommand>"
  "robot_ai/AIGenericCommand")