;; Auto-generated. Do not edit!


(when (boundp 'robot_ai_timer::ai_timer)
  (if (not (find-package "ROBOT_AI_TIMER"))
    (make-package "ROBOT_AI_TIMER"))
  (shadow 'ai_timer (find-package "ROBOT_AI_TIMER")))
(unless (find-package "ROBOT_AI_TIMER::AI_TIMER")
  (make-package "ROBOT_AI_TIMER::AI_TIMER"))

(in-package "ROS")
;;//! \htmlinclude ai_timer.msg.html


(defclass robot_ai_timer::ai_timer
  :super ros::object
  :slots (_elapsed_time _time_left _is_finished ))

(defmethod robot_ai_timer::ai_timer
  (:init
   (&key
    ((:elapsed_time __elapsed_time) 0.0)
    ((:time_left __time_left) 0.0)
    ((:is_finished __is_finished) nil)
    )
   (send-super :init)
   (setq _elapsed_time (float __elapsed_time))
   (setq _time_left (float __time_left))
   (setq _is_finished __is_finished)
   self)
  (:elapsed_time
   (&optional __elapsed_time)
   (if __elapsed_time (setq _elapsed_time __elapsed_time)) _elapsed_time)
  (:time_left
   (&optional __time_left)
   (if __time_left (setq _time_left __time_left)) _time_left)
  (:is_finished
   (&optional __is_finished)
   (if __is_finished (setq _is_finished __is_finished)) _is_finished)
  (:serialization-length
   ()
   (+
    ;; float32 _elapsed_time
    4
    ;; float32 _time_left
    4
    ;; bool _is_finished
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _elapsed_time
       (sys::poke _elapsed_time (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _time_left
       (sys::poke _time_left (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _is_finished
       (if _is_finished (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _elapsed_time
     (setq _elapsed_time (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _time_left
     (setq _time_left (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _is_finished
     (setq _is_finished (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get robot_ai_timer::ai_timer :md5sum-) "c4cb09c8090b9afd36452fbb8fd74941")
(setf (get robot_ai_timer::ai_timer :datatype-) "robot_ai_timer/ai_timer")
(setf (get robot_ai_timer::ai_timer :definition-)
      "float32 elapsed_time
float32 time_left
bool is_finished
")



(provide :robot_ai_timer/ai_timer "c4cb09c8090b9afd36452fbb8fd74941")


