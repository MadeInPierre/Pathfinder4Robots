// Auto-generated. Do not edit!

// (in-package robot_mapping_pathfinder.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------


//-----------------------------------------------------------

class GetPathWaypointsRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.startpos = null;
      this.endpos = null;
    }
    else {
      if (initObj.hasOwnProperty('startpos')) {
        this.startpos = initObj.startpos
      }
      else {
        this.startpos = new geometry_msgs.msg.Pose2D();
      }
      if (initObj.hasOwnProperty('endpos')) {
        this.endpos = initObj.endpos
      }
      else {
        this.endpos = new geometry_msgs.msg.Pose2D();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetPathWaypointsRequest
    // Serialize message field [startpos]
    bufferOffset = geometry_msgs.msg.Pose2D.serialize(obj.startpos, buffer, bufferOffset);
    // Serialize message field [endpos]
    bufferOffset = geometry_msgs.msg.Pose2D.serialize(obj.endpos, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetPathWaypointsRequest
    let len;
    let data = new GetPathWaypointsRequest(null);
    // Deserialize message field [startpos]
    data.startpos = geometry_msgs.msg.Pose2D.deserialize(buffer, bufferOffset);
    // Deserialize message field [endpos]
    data.endpos = geometry_msgs.msg.Pose2D.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 48;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot_mapping_pathfinder/GetPathWaypointsRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4b38870893a4a10eb2a6096ddd927b62';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/Pose2D startpos
    geometry_msgs/Pose2D endpos
    
    ================================================================================
    MSG: geometry_msgs/Pose2D
    # This expresses a position and orientation on a 2D manifold.
    
    float64 x
    float64 y
    float64 theta
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GetPathWaypointsRequest(null);
    if (msg.startpos !== undefined) {
      resolved.startpos = geometry_msgs.msg.Pose2D.Resolve(msg.startpos)
    }
    else {
      resolved.startpos = new geometry_msgs.msg.Pose2D()
    }

    if (msg.endpos !== undefined) {
      resolved.endpos = geometry_msgs.msg.Pose2D.Resolve(msg.endpos)
    }
    else {
      resolved.endpos = new geometry_msgs.msg.Pose2D()
    }

    return resolved;
    }
};

class GetPathWaypointsResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.waypoints = null;
    }
    else {
      if (initObj.hasOwnProperty('waypoints')) {
        this.waypoints = initObj.waypoints
      }
      else {
        this.waypoints = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetPathWaypointsResponse
    // Serialize message field [waypoints]
    // Serialize the length for message field [waypoints]
    bufferOffset = _serializer.uint32(obj.waypoints.length, buffer, bufferOffset);
    obj.waypoints.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Pose2D.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetPathWaypointsResponse
    let len;
    let data = new GetPathWaypointsResponse(null);
    // Deserialize message field [waypoints]
    // Deserialize array length for message field [waypoints]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.waypoints = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.waypoints[i] = geometry_msgs.msg.Pose2D.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 24 * object.waypoints.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot_mapping_pathfinder/GetPathWaypointsResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0b9e83915d91f5a57f9839688cdeccfb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/Pose2D[] waypoints
    
    
    ================================================================================
    MSG: geometry_msgs/Pose2D
    # This expresses a position and orientation on a 2D manifold.
    
    float64 x
    float64 y
    float64 theta
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GetPathWaypointsResponse(null);
    if (msg.waypoints !== undefined) {
      resolved.waypoints = new Array(msg.waypoints.length);
      for (let i = 0; i < resolved.waypoints.length; ++i) {
        resolved.waypoints[i] = geometry_msgs.msg.Pose2D.Resolve(msg.waypoints[i]);
      }
    }
    else {
      resolved.waypoints = []
    }

    return resolved;
    }
};

module.exports = {
  Request: GetPathWaypointsRequest,
  Response: GetPathWaypointsResponse,
  md5sum() { return 'faeb4d9752daba214ce90de021e3676d'; },
  datatype() { return 'robot_mapping_pathfinder/GetPathWaypoints'; }
};
