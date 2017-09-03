// Auto-generated. Do not edit!

// (in-package robot_ai.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class AIGenericCommandRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.department = null;
      this.destination = null;
      this.command = null;
      this.params = null;
    }
    else {
      if (initObj.hasOwnProperty('department')) {
        this.department = initObj.department
      }
      else {
        this.department = '';
      }
      if (initObj.hasOwnProperty('destination')) {
        this.destination = initObj.destination
      }
      else {
        this.destination = '';
      }
      if (initObj.hasOwnProperty('command')) {
        this.command = initObj.command
      }
      else {
        this.command = '';
      }
      if (initObj.hasOwnProperty('params')) {
        this.params = initObj.params
      }
      else {
        this.params = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type AIGenericCommandRequest
    // Serialize message field [department]
    bufferOffset = _serializer.string(obj.department, buffer, bufferOffset);
    // Serialize message field [destination]
    bufferOffset = _serializer.string(obj.destination, buffer, bufferOffset);
    // Serialize message field [command]
    bufferOffset = _serializer.string(obj.command, buffer, bufferOffset);
    // Serialize message field [params]
    bufferOffset = _serializer.string(obj.params, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type AIGenericCommandRequest
    let len;
    let data = new AIGenericCommandRequest(null);
    // Deserialize message field [department]
    data.department = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [destination]
    data.destination = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [command]
    data.command = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [params]
    data.params = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.department.length;
    length += object.destination.length;
    length += object.command.length;
    length += object.params.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot_ai/AIGenericCommandRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '121cf84ef2958e8916f9792ec575e134';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string department
    string destination
    string command
    string params
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new AIGenericCommandRequest(null);
    if (msg.department !== undefined) {
      resolved.department = msg.department;
    }
    else {
      resolved.department = ''
    }

    if (msg.destination !== undefined) {
      resolved.destination = msg.destination;
    }
    else {
      resolved.destination = ''
    }

    if (msg.command !== undefined) {
      resolved.command = msg.command;
    }
    else {
      resolved.command = ''
    }

    if (msg.params !== undefined) {
      resolved.params = msg.params;
    }
    else {
      resolved.params = ''
    }

    return resolved;
    }
};

class AIGenericCommandResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.response_code = null;
      this.reason = null;
    }
    else {
      if (initObj.hasOwnProperty('response_code')) {
        this.response_code = initObj.response_code
      }
      else {
        this.response_code = 0;
      }
      if (initObj.hasOwnProperty('reason')) {
        this.reason = initObj.reason
      }
      else {
        this.reason = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type AIGenericCommandResponse
    // Serialize message field [response_code]
    bufferOffset = _serializer.int16(obj.response_code, buffer, bufferOffset);
    // Serialize message field [reason]
    bufferOffset = _serializer.string(obj.reason, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type AIGenericCommandResponse
    let len;
    let data = new AIGenericCommandResponse(null);
    // Deserialize message field [response_code]
    data.response_code = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [reason]
    data.reason = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.reason.length;
    return length + 6;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot_ai/AIGenericCommandResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a40e2e8a729fb2f435e3fce71dfeed71';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 response_code
    string reason
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new AIGenericCommandResponse(null);
    if (msg.response_code !== undefined) {
      resolved.response_code = msg.response_code;
    }
    else {
      resolved.response_code = 0
    }

    if (msg.reason !== undefined) {
      resolved.reason = msg.reason;
    }
    else {
      resolved.reason = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: AIGenericCommandRequest,
  Response: AIGenericCommandResponse,
  md5sum() { return '03627a98e56c86556490728af60f9ba4'; },
  datatype() { return 'robot_ai/AIGenericCommand'; }
};
