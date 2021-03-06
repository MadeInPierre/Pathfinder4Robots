// Generated by gencpp from file robot_ai/addResponse.msg
// DO NOT EDIT!


#ifndef ROBOT_AI_MESSAGE_ADDRESPONSE_H
#define ROBOT_AI_MESSAGE_ADDRESPONSE_H


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
struct addResponse_
{
  typedef addResponse_<ContainerAllocator> Type;

  addResponse_()
    : sum(0)  {
    }
  addResponse_(const ContainerAllocator& _alloc)
    : sum(0)  {
  (void)_alloc;
    }



   typedef int32_t _sum_type;
  _sum_type sum;




  typedef boost::shared_ptr< ::robot_ai::addResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robot_ai::addResponse_<ContainerAllocator> const> ConstPtr;

}; // struct addResponse_

typedef ::robot_ai::addResponse_<std::allocator<void> > addResponse;

typedef boost::shared_ptr< ::robot_ai::addResponse > addResponsePtr;
typedef boost::shared_ptr< ::robot_ai::addResponse const> addResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robot_ai::addResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robot_ai::addResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robot_ai

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'robot_ai': ['/home/jack/Programming/Robotics/RobotOS/src/robot_ai/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robot_ai::addResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robot_ai::addResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_ai::addResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_ai::addResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_ai::addResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_ai::addResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robot_ai::addResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0ba699c25c9418c0366f3595c0c8e8ec";
  }

  static const char* value(const ::robot_ai::addResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0ba699c25c9418c0ULL;
  static const uint64_t static_value2 = 0x366f3595c0c8e8ecULL;
};

template<class ContainerAllocator>
struct DataType< ::robot_ai::addResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robot_ai/addResponse";
  }

  static const char* value(const ::robot_ai::addResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robot_ai::addResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 sum\n\
\n\
";
  }

  static const char* value(const ::robot_ai::addResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robot_ai::addResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.sum);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct addResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robot_ai::addResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robot_ai::addResponse_<ContainerAllocator>& v)
  {
    s << indent << "sum: ";
    Printer<int32_t>::stream(s, indent + "  ", v.sum);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOT_AI_MESSAGE_ADDRESPONSE_H
