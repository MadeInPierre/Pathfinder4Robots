
(cl:in-package :asdf)

(defsystem "robot_ai-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "AICommand" :depends-on ("_package_AICommand"))
    (:file "_package_AICommand" :depends-on ("_package"))
    (:file "ai_timer" :depends-on ("_package_ai_timer"))
    (:file "_package_ai_timer" :depends-on ("_package"))
  ))