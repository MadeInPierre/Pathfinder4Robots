;; Auto-generated. Do not edit!


(when (boundp 'robot_ai::ai_timer)
  (if (not (find-package "ROBOT_AI"))
    (make-package "ROBOT_AI"))
  (shadow 'ai_timer (find-package "ROBOT_AI")))
(unless (find-package "ROBOT_AI::AI_TIMER")
  (make-package "ROBOT_AI::AI_TIMER"))

(in-package "ROS")
;;//! \htmlinclude ai_timer.msg.html


(defclass robot_ai::ai_timer
  :super ros::object
  :slots (_elapsed_time _time_left ))

(defmethod robot_ai::ai_timer
  (:init
   (&key
    ((:elapsed_time __elapsed_time) 0.0)
    ((:time_left __time_left) 0.0)
    )
   (send-super :init)
   (setq _elapsed_time (float __elapsed_time))
   (setq _time_left (float __time_left))
   self)
  (:elapsed_time
   (&optional __elapsed_time)
   (if __elapsed_time (setq _elapsed_time __elapsed_time)) _elapsed_time)
  (:time_left
   (&optional __time_left)
   (if __time_left (setq _time_left __time_left)) _time_left)
  (:serialization-length
   ()
   (+
    ;; float32 _elapsed_time
    4
    ;; float32 _time_left
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _elapsed_time
       (sys::poke _elapsed_time (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _time_left
       (sys::poke _time_left (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _elapsed_time
     (setq _elapsed_time (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _time_left
     (setq _time_left (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get robot_ai::ai_timer :md5sum-) "cb181220fc60bdfda16dca75f4b14070")
(setf (get robot_ai::ai_timer :datatype-) "robot_ai/ai_timer")
(setf (get robot_ai::ai_timer :definition-)
      "float32 elapsed_time
float32 time_left
")



(provide :robot_ai/ai_timer "cb181220fc60bdfda16dca75f4b14070")


