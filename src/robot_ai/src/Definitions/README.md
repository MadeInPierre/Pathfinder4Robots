# AI Definition

This is where the robot is told what to do.

##1. Strategies
	Is a an ordered list of objectives and actions.


##2. Objectives
	Is an ordered or non-ordered list of actions or objectives.
##3. Actions
	Is an ordered list of Harware Actions.
##4. Hardware Actions
	Supported embedded actions that can be used:
		- The `wheels` group communicates with the ROS `robot_movement_wheels` package. This is how the AI asks for the robot to move from a point to another. Actions defined :
			- `wheels_gotoxy`: Ask the robot to move to a certain position. angle doesn't matter.
			- `wheels_gotoxya`: Go to a certain position and angle.
			- `wheels_gotoa`: Ask the robot to turn toward a certain direction.
			- `wheels_delay`: Stop the robot for a certain duration (seconds).

		- The `actuators` group:
			- `actuator_open`: Set the actuator to the `closed` position set in the `robot.json` description file.
			- `actuator_close`: Set the actuator to the `open` position set in the `robot.json` description file.
			- `actuator_toggle`: Toggle between open/close position. 
			- `actuator_setpos`: Manually set a position to the actuator.


##4. Actions execution
The last layer, `HardareActions.json`, 