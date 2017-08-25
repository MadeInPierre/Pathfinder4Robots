;; Auto-generated. Do not edit!


(when (boundp 'robot_ai::add)
  (if (not (find-package "ROBOT_AI"))
    (make-package "ROBOT_AI"))
  (shadow 'add (find-package "ROBOT_AI")))
(unless (find-package "ROBOT_AI::ADD")
  (make-package "ROBOT_AI::ADD"))
(unless (find-package "ROBOT_AI::ADDREQUEST")
  (make-package "ROBOT_AI::ADDREQUEST"))
(unless (find-package "ROBOT_AI::ADDRESPONSE")
  (make-package "ROBOT_AI::ADDRESPONSE"))

(in-package "ROS")





(defclass robot_ai::addRequest
  :super ros::object
  :slots (_a _b ))

(defmethod robot_ai::addRequest
  (:init
   (&key
    ((:a __a) 0)
    ((:b __b) 0)
    )
   (send-super :init)
   (setq _a (round __a))
   (setq _b (round __b))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:serialization-length
   ()
   (+
    ;; int32 _a
    4
    ;; int32 _b
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _a
       (write-long _a s)
     ;; int32 _b
       (write-long _b s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _a
     (setq _a (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _b
     (setq _b (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass robot_ai::addResponse
  :super ros::object
  :slots (_sum ))

(defmethod robot_ai::addResponse
  (:init
   (&key
    ((:sum __sum) 0)
    )
   (send-super :init)
   (setq _sum (round __sum))
   self)
  (:sum
   (&optional __sum)
   (if __sum (setq _sum __sum)) _sum)
  (:serialization-length
   ()
   (+
    ;; int32 _sum
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _sum
       (write-long _sum s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _sum
     (setq _sum (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass robot_ai::add
  :super ros::object
  :slots ())

(setf (get robot_ai::add :md5sum-) "f0b6d69ea10b0cf210cb349d58d59e8f")
(setf (get robot_ai::add :datatype-) "robot_ai/add")
(setf (get robot_ai::add :request) robot_ai::addRequest)
(setf (get robot_ai::add :response) robot_ai::addResponse)

(defmethod robot_ai::addRequest
  (:response () (instance robot_ai::addResponse :init)))

(setf (get robot_ai::addRequest :md5sum-) "f0b6d69ea10b0cf210cb349d58d59e8f")
(setf (get robot_ai::addRequest :datatype-) "robot_ai/addRequest")
(setf (get robot_ai::addRequest :definition-)
      "int32 a
int32 b
---
int32 sum

")

(setf (get robot_ai::addResponse :md5sum-) "f0b6d69ea10b0cf210cb349d58d59e8f")
(setf (get robot_ai::addResponse :datatype-) "robot_ai/addResponse")
(setf (get robot_ai::addResponse :definition-)
      "int32 a
int32 b
---
int32 sum

")



(provide :robot_ai/add "f0b6d69ea10b0cf210cb349d58d59e8f")


