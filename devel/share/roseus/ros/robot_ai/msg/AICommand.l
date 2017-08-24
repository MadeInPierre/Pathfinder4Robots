;; Auto-generated. Do not edit!


(when (boundp 'robot_ai::AICommand)
  (if (not (find-package "ROBOT_AI"))
    (make-package "ROBOT_AI"))
  (shadow 'AICommand (find-package "ROBOT_AI")))
(unless (find-package "ROBOT_AI::AICOMMAND")
  (make-package "ROBOT_AI::AICOMMAND"))

(in-package "ROS")
;;//! \htmlinclude AICommand.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass robot_ai::AICommand
  :super ros::object
  :slots (_header _command _params ))

(defmethod robot_ai::AICommand
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:command __command) "")
    ((:params __params) "")
    )
   (send-super :init)
   (setq _header __header)
   (setq _command (string __command))
   (setq _params (string __params))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:params
   (&optional __params)
   (if __params (setq _params __params)) _params)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; string _command
    4 (length _command)
    ;; string _params
    4 (length _params)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; string _command
       (write-long (length _command) s) (princ _command s)
     ;; string _params
       (write-long (length _params) s) (princ _params s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; string _command
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _params
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _params (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get robot_ai::AICommand :md5sum-) "c39e2f3e5a34d4649f4b40daf60fbb03")
(setf (get robot_ai::AICommand :datatype-) "robot_ai/AICommand")
(setf (get robot_ai::AICommand :definition-)
      "Header header
string command
string params

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :robot_ai/AICommand "c39e2f3e5a34d4649f4b40daf60fbb03")


