// Generated by gencpp from file robot_ai_scheduler/AIGenericCommand.msg
// DO NOT EDIT!


#ifndef ROBOT_AI_SCHEDULER_MESSAGE_AIGENERICCOMMAND_H
#define ROBOT_AI_SCHEDULER_MESSAGE_AIGENERICCOMMAND_H

#include <ros/service_traits.h>


#include <robot_ai_scheduler/AIGenericCommandRequest.h>
#include <robot_ai_scheduler/AIGenericCommandResponse.h>


namespace robot_ai_scheduler
{

struct AIGenericCommand
{

typedef AIGenericCommandRequest Request;
typedef AIGenericCommandResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AIGenericCommand
} // namespace robot_ai_scheduler


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::robot_ai_scheduler::AIGenericCommand > {
  static const char* value()
  {
    return "03627a98e56c86556490728af60f9ba4";
  }

  static const char* value(const ::robot_ai_scheduler::AIGenericCommand&) { return value(); }
};

template<>
struct DataType< ::robot_ai_scheduler::AIGenericCommand > {
  static const char* value()
  {
    return "robot_ai_scheduler/AIGenericCommand";
  }

  static const char* value(const ::robot_ai_scheduler::AIGenericCommand&) { return value(); }
};


// service_traits::MD5Sum< ::robot_ai_scheduler::AIGenericCommandRequest> should match 
// service_traits::MD5Sum< ::robot_ai_scheduler::AIGenericCommand > 
template<>
struct MD5Sum< ::robot_ai_scheduler::AIGenericCommandRequest>
{
  static const char* value()
  {
    return MD5Sum< ::robot_ai_scheduler::AIGenericCommand >::value();
  }
  static const char* value(const ::robot_ai_scheduler::AIGenericCommandRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::robot_ai_scheduler::AIGenericCommandRequest> should match 
// service_traits::DataType< ::robot_ai_scheduler::AIGenericCommand > 
template<>
struct DataType< ::robot_ai_scheduler::AIGenericCommandRequest>
{
  static const char* value()
  {
    return DataType< ::robot_ai_scheduler::AIGenericCommand >::value();
  }
  static const char* value(const ::robot_ai_scheduler::AIGenericCommandRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::robot_ai_scheduler::AIGenericCommandResponse> should match 
// service_traits::MD5Sum< ::robot_ai_scheduler::AIGenericCommand > 
template<>
struct MD5Sum< ::robot_ai_scheduler::AIGenericCommandResponse>
{
  static const char* value()
  {
    return MD5Sum< ::robot_ai_scheduler::AIGenericCommand >::value();
  }
  static const char* value(const ::robot_ai_scheduler::AIGenericCommandResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::robot_ai_scheduler::AIGenericCommandResponse> should match 
// service_traits::DataType< ::robot_ai_scheduler::AIGenericCommand > 
template<>
struct DataType< ::robot_ai_scheduler::AIGenericCommandResponse>
{
  static const char* value()
  {
    return DataType< ::robot_ai_scheduler::AIGenericCommand >::value();
  }
  static const char* value(const ::robot_ai_scheduler::AIGenericCommandResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROBOT_AI_SCHEDULER_MESSAGE_AIGENERICCOMMAND_H
