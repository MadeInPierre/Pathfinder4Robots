// Generated by gencpp from file robot_ai/AICommand.msg
// DO NOT EDIT!


#ifndef ROBOT_AI_MESSAGE_AICOMMAND_H
#define ROBOT_AI_MESSAGE_AICOMMAND_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace robot_ai
{
template <class ContainerAllocator>
struct AICommand_
{
  typedef AICommand_<ContainerAllocator> Type;

  AICommand_()
    : header()
    , command()
    , params()  {
    }
  AICommand_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , command(_alloc)
    , params(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _command_type;
  _command_type command;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _params_type;
  _params_type params;




  typedef boost::shared_ptr< ::robot_ai::AICommand_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robot_ai::AICommand_<ContainerAllocator> const> ConstPtr;

}; // struct AICommand_

typedef ::robot_ai::AICommand_<std::allocator<void> > AICommand;

typedef boost::shared_ptr< ::robot_ai::AICommand > AICommandPtr;
typedef boost::shared_ptr< ::robot_ai::AICommand const> AICommandConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robot_ai::AICommand_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robot_ai::AICommand_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robot_ai

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'robot_ai': ['/home/jack/Programming/Robotics/RobotOS/src/robot_ai/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robot_ai::AICommand_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robot_ai::AICommand_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_ai::AICommand_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_ai::AICommand_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_ai::AICommand_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_ai::AICommand_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robot_ai::AICommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c39e2f3e5a34d4649f4b40daf60fbb03";
  }

  static const char* value(const ::robot_ai::AICommand_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc39e2f3e5a34d464ULL;
  static const uint64_t static_value2 = 0x9f4b40daf60fbb03ULL;
};

template<class ContainerAllocator>
struct DataType< ::robot_ai::AICommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robot_ai/AICommand";
  }

  static const char* value(const ::robot_ai::AICommand_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robot_ai::AICommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
string command\n\
string params\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::robot_ai::AICommand_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robot_ai::AICommand_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.command);
      stream.next(m.params);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct AICommand_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robot_ai::AICommand_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robot_ai::AICommand_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "command: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.command);
    s << indent << "params: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.params);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOT_AI_MESSAGE_AICOMMAND_H
