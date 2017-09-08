// Auto-generated. Do not edit!

// (in-package robot_ai.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ai_timer {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.elapsed_time = null;
      this.time_left = null;
      this.is_finished = null;
    }
    else {
      if (initObj.hasOwnProperty('elapsed_time')) {
        this.elapsed_time = initObj.elapsed_time
      }
      else {
        this.elapsed_time = 0.0;
      }
      if (initObj.hasOwnProperty('time_left')) {
        this.time_left = initObj.time_left
      }
      else {
        this.time_left = 0.0;
      }
      if (initObj.hasOwnProperty('is_finished')) {
        this.is_finished = initObj.is_finished
      }
      else {
        this.is_finished = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ai_timer
    // Serialize message field [elapsed_time]
    bufferOffset = _serializer.float32(obj.elapsed_time, buffer, bufferOffset);
    // Serialize message field [time_left]
    bufferOffset = _serializer.float32(obj.time_left, buffer, bufferOffset);
    // Serialize message field [is_finished]
    bufferOffset = _serializer.bool(obj.is_finished, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ai_timer
    let len;
    let data = new ai_timer(null);
    // Deserialize message field [elapsed_time]
    data.elapsed_time = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [time_left]
    data.time_left = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [is_finished]
    data.is_finished = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'robot_ai/ai_timer';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c4cb09c8090b9afd36452fbb8fd74941';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 elapsed_time
    float32 time_left
    bool is_finished
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ai_timer(null);
    if (msg.elapsed_time !== undefined) {
      resolved.elapsed_time = msg.elapsed_time;
    }
    else {
      resolved.elapsed_time = 0.0
    }

    if (msg.time_left !== undefined) {
      resolved.time_left = msg.time_left;
    }
    else {
      resolved.time_left = 0.0
    }

    if (msg.is_finished !== undefined) {
      resolved.is_finished = msg.is_finished;
    }
    else {
      resolved.is_finished = false
    }

    return resolved;
    }
};

module.exports = ai_timer;
