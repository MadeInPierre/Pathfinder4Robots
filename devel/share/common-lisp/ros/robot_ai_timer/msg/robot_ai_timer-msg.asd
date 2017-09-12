
(cl:in-package :asdf)

(defsystem "robot_ai_timer-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ai_timer" :depends-on ("_package_ai_timer"))
    (:file "_package_ai_timer" :depends-on ("_package"))
  ))