;; Auto-generated. Do not edit!


(when (boundp 'robot_ai::AIGenericCommand)
  (if (not (find-package "ROBOT_AI"))
    (make-package "ROBOT_AI"))
  (shadow 'AIGenericCommand (find-package "ROBOT_AI")))
(unless (find-package "ROBOT_AI::AIGENERICCOMMAND")
  (make-package "ROBOT_AI::AIGENERICCOMMAND"))
(unless (find-package "ROBOT_AI::AIGENERICCOMMANDREQUEST")
  (make-package "ROBOT_AI::AIGENERICCOMMANDREQUEST"))
(unless (find-package "ROBOT_AI::AIGENERICCOMMANDRESPONSE")
  (make-package "ROBOT_AI::AIGENERICCOMMANDRESPONSE"))

(in-package "ROS")





(defclass robot_ai::AIGenericCommandRequest
  :super ros::object
  :slots (_destination _command _params ))

(defmethod robot_ai::AIGenericCommandRequest
  (:init
   (&key
    ((:destination __destination) "")
    ((:command __command) "")
    ((:params __params) "")
    )
   (send-super :init)
   (setq _destination (string __destination))
   (setq _command (string __command))
   (setq _params (string __params))
   self)
  (:destination
   (&optional __destination)
   (if __destination (setq _destination __destination)) _destination)
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:params
   (&optional __params)
   (if __params (setq _params __params)) _params)
  (:serialization-length
   ()
   (+
    ;; string _destination
    4 (length _destination)
    ;; string _command
    4 (length _command)
    ;; string _params
    4 (length _params)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _destination
       (write-long (length _destination) s) (princ _destination s)
     ;; string _command
       (write-long (length _command) s) (princ _command s)
     ;; string _params
       (write-long (length _params) s) (princ _params s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _destination
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _destination (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _command
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _params
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _params (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass robot_ai::AIGenericCommandResponse
  :super ros::object
  :slots (_success _reason ))

(defmethod robot_ai::AIGenericCommandResponse
  (:init
   (&key
    ((:success __success) nil)
    ((:reason __reason) "")
    )
   (send-super :init)
   (setq _success __success)
   (setq _reason (string __reason))
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:reason
   (&optional __reason)
   (if __reason (setq _reason __reason)) _reason)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ;; string _reason
    4 (length _reason)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _reason
       (write-long (length _reason) s) (princ _reason s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _reason
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _reason (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass robot_ai::AIGenericCommand
  :super ros::object
  :slots ())

(setf (get robot_ai::AIGenericCommand :md5sum-) "486981db1cfa05f3d7fa6076f176b704")
(setf (get robot_ai::AIGenericCommand :datatype-) "robot_ai/AIGenericCommand")
(setf (get robot_ai::AIGenericCommand :request) robot_ai::AIGenericCommandRequest)
(setf (get robot_ai::AIGenericCommand :response) robot_ai::AIGenericCommandResponse)

(defmethod robot_ai::AIGenericCommandRequest
  (:response () (instance robot_ai::AIGenericCommandResponse :init)))

(setf (get robot_ai::AIGenericCommandRequest :md5sum-) "486981db1cfa05f3d7fa6076f176b704")
(setf (get robot_ai::AIGenericCommandRequest :datatype-) "robot_ai/AIGenericCommandRequest")
(setf (get robot_ai::AIGenericCommandRequest :definition-)
      "string destination
string command
string params
---
bool success
string reason

")

(setf (get robot_ai::AIGenericCommandResponse :md5sum-) "486981db1cfa05f3d7fa6076f176b704")
(setf (get robot_ai::AIGenericCommandResponse :datatype-) "robot_ai/AIGenericCommandResponse")
(setf (get robot_ai::AIGenericCommandResponse :definition-)
      "string destination
string command
string params
---
bool success
string reason

")



(provide :robot_ai/AIGenericCommand "486981db1cfa05f3d7fa6076f176b704")


