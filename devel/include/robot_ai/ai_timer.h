// Generated by gencpp from file robot_ai/ai_timer.msg
// DO NOT EDIT!


#ifndef ROBOT_AI_MESSAGE_AI_TIMER_H
#define ROBOT_AI_MESSAGE_AI_TIMER_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace robot_ai
{
template <class ContainerAllocator>
struct ai_timer_
{
  typedef ai_timer_<ContainerAllocator> Type;

  ai_timer_()
    : elapsed_time(0.0)
    , time_left(0.0)  {
    }
  ai_timer_(const ContainerAllocator& _alloc)
    : elapsed_time(0.0)
    , time_left(0.0)  {
  (void)_alloc;
    }



   typedef float _elapsed_time_type;
  _elapsed_time_type elapsed_time;

   typedef float _time_left_type;
  _time_left_type time_left;




  typedef boost::shared_ptr< ::robot_ai::ai_timer_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robot_ai::ai_timer_<ContainerAllocator> const> ConstPtr;

}; // struct ai_timer_

typedef ::robot_ai::ai_timer_<std::allocator<void> > ai_timer;

typedef boost::shared_ptr< ::robot_ai::ai_timer > ai_timerPtr;
typedef boost::shared_ptr< ::robot_ai::ai_timer const> ai_timerConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robot_ai::ai_timer_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robot_ai::ai_timer_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robot_ai

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'robot_ai': ['/home/jack/Programming/Robotics/RobotOS/src/robot_ai/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robot_ai::ai_timer_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robot_ai::ai_timer_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_ai::ai_timer_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_ai::ai_timer_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_ai::ai_timer_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_ai::ai_timer_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robot_ai::ai_timer_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cb181220fc60bdfda16dca75f4b14070";
  }

  static const char* value(const ::robot_ai::ai_timer_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xcb181220fc60bdfdULL;
  static const uint64_t static_value2 = 0xa16dca75f4b14070ULL;
};

template<class ContainerAllocator>
struct DataType< ::robot_ai::ai_timer_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robot_ai/ai_timer";
  }

  static const char* value(const ::robot_ai::ai_timer_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robot_ai::ai_timer_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 elapsed_time\n\
float32 time_left\n\
";
  }

  static const char* value(const ::robot_ai::ai_timer_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robot_ai::ai_timer_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.elapsed_time);
      stream.next(m.time_left);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ai_timer_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robot_ai::ai_timer_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robot_ai::ai_timer_<ContainerAllocator>& v)
  {
    s << indent << "elapsed_time: ";
    Printer<float>::stream(s, indent + "  ", v.elapsed_time);
    s << indent << "time_left: ";
    Printer<float>::stream(s, indent + "  ", v.time_left);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOT_AI_MESSAGE_AI_TIMER_H