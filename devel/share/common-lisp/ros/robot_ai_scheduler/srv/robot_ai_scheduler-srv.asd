
(cl:in-package :asdf)

(defsystem "robot_ai_scheduler-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AIGenericCommand" :depends-on ("_package_AIGenericCommand"))
    (:file "_package_AIGenericCommand" :depends-on ("_package"))
    (:file "TimerCommand" :depends-on ("_package_TimerCommand"))
    (:file "_package_TimerCommand" :depends-on ("_package"))
    (:file "TimerGetTime" :depends-on ("_package_TimerGetTime"))
    (:file "_package_TimerGetTime" :depends-on ("_package"))
  ))