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
  :slots (_department _destination _command _params ))

(defmethod robot_ai::AIGenericCommandRequest
  (:init
   (&key
    ((:department __department) "")
    ((:destination __destination) "")
    ((:command __command) "")
    ((:params __params) "")
    )
   (send-super :init)
   (setq _department (string __department))
   (setq _destination (string __destination))
   (setq _command (string __command))
   (setq _params (string __params))
   self)
  (:department
   (&optional __department)
   (if __department (setq _department __department)) _department)
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
    ;; string _department
    4 (length _department)
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
     ;; string _department
       (write-long (length _department) s) (princ _department s)
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
   ;; string _department
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _department (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
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
  :slots (_response_code _reason ))

(defmethod robot_ai::AIGenericCommandResponse
  (:init
   (&key
    ((:response_code __response_code) 0)
    ((:reason __reason) "")
    )
   (send-super :init)
   (setq _response_code (round __response_code))
   (setq _reason (string __reason))
   self)
  (:response_code
   (&optional __response_code)
   (if __response_code (setq _response_code __response_code)) _response_code)
  (:reason
   (&optional __reason)
   (if __reason (setq _reason __reason)) _reason)
  (:serialization-length
   ()
   (+
    ;; int16 _response_code
    2
    ;; string _reason
    4 (length _reason)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _response_code
       (write-word _response_code s)
     ;; string _reason
       (write-long (length _reason) s) (princ _reason s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _response_code
     (setq _response_code (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; string _reason
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _reason (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass robot_ai::AIGenericCommand
  :super ros::object
  :slots ())

(setf (get robot_ai::AIGenericCommand :md5sum-) "03627a98e56c86556490728af60f9ba4")
(setf (get robot_ai::AIGenericCommand :datatype-) "robot_ai/AIGenericCommand")
(setf (get robot_ai::AIGenericCommand :request) robot_ai::AIGenericCommandRequest)
(setf (get robot_ai::AIGenericCommand :response) robot_ai::AIGenericCommandResponse)

(defmethod robot_ai::AIGenericCommandRequest
  (:response () (instance robot_ai::AIGenericCommandResponse :init)))

(setf (get robot_ai::AIGenericCommandRequest :md5sum-) "03627a98e56c86556490728af60f9ba4")
(setf (get robot_ai::AIGenericCommandRequest :datatype-) "robot_ai/AIGenericCommandRequest")
(setf (get robot_ai::AIGenericCommandRequest :definition-)
      "string department
string destination
string command
string params
---
int16 response_code
string reason

")

(setf (get robot_ai::AIGenericCommandResponse :md5sum-) "03627a98e56c86556490728af60f9ba4")
(setf (get robot_ai::AIGenericCommandResponse :datatype-) "robot_ai/AIGenericCommandResponse")
(setf (get robot_ai::AIGenericCommandResponse :definition-)
      "string department
string destination
string command
string params
---
int16 response_code
string reason

")



(provide :robot_ai/AIGenericCommand "03627a98e56c86556490728af60f9ba4")


