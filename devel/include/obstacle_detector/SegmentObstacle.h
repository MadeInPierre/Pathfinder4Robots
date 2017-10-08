// Generated by gencpp from file obstacle_detector/SegmentObstacle.msg
// DO NOT EDIT!


#ifndef OBSTACLE_DETECTOR_MESSAGE_SEGMENTOBSTACLE_H
#define OBSTACLE_DETECTOR_MESSAGE_SEGMENTOBSTACLE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Point.h>
#include <geometry_msgs/Point.h>

namespace obstacle_detector
{
template <class ContainerAllocator>
struct SegmentObstacle_
{
  typedef SegmentObstacle_<ContainerAllocator> Type;

  SegmentObstacle_()
    : first_point()
    , last_point()  {
    }
  SegmentObstacle_(const ContainerAllocator& _alloc)
    : first_point(_alloc)
    , last_point(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Point_<ContainerAllocator>  _first_point_type;
  _first_point_type first_point;

   typedef  ::geometry_msgs::Point_<ContainerAllocator>  _last_point_type;
  _last_point_type last_point;




  typedef boost::shared_ptr< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> const> ConstPtr;

}; // struct SegmentObstacle_

typedef ::obstacle_detector::SegmentObstacle_<std::allocator<void> > SegmentObstacle;

typedef boost::shared_ptr< ::obstacle_detector::SegmentObstacle > SegmentObstaclePtr;
typedef boost::shared_ptr< ::obstacle_detector::SegmentObstacle const> SegmentObstacleConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::obstacle_detector::SegmentObstacle_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace obstacle_detector

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'obstacle_detector': ['/home/jack/Programming/Robotics/RobotOS/src/obstacle_detector/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> >
{
  static const char* value()
  {
    return "37ecbf7e1053bae89f0770466b37c3c3";
  }

  static const char* value(const ::obstacle_detector::SegmentObstacle_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x37ecbf7e1053bae8ULL;
  static const uint64_t static_value2 = 0x9f0770466b37c3c3ULL;
};

template<class ContainerAllocator>
struct DataType< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> >
{
  static const char* value()
  {
    return "obstacle_detector/SegmentObstacle";
  }

  static const char* value(const ::obstacle_detector::SegmentObstacle_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> >
{
  static const char* value()
  {
    return "geometry_msgs/Point first_point  # First point of the segment [m]\n\
geometry_msgs/Point last_point   # Last point of the segment [m]\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const ::obstacle_detector::SegmentObstacle_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.first_point);
      stream.next(m.last_point);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SegmentObstacle_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::obstacle_detector::SegmentObstacle_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::obstacle_detector::SegmentObstacle_<ContainerAllocator>& v)
  {
    s << indent << "first_point: ";
    s << std::endl;
    Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "  ", v.first_point);
    s << indent << "last_point: ";
    s << std::endl;
    Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "  ", v.last_point);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OBSTACLE_DETECTOR_MESSAGE_SEGMENTOBSTACLE_H