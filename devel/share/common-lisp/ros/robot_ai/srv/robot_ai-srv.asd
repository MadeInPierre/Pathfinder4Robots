
(cl:in-package :asdf)

(defsystem "robot_ai-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AIGenericCommand" :depends-on ("_package_AIGenericCommand"))
    (:file "_package_AIGenericCommand" :depends-on ("_package"))
  ))