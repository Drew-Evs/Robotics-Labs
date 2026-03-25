import threading
import rclpy
from rclpy.node import Node

#cmd_vel expects a twist message type to be published to it
from geometry_msgs.msg import Twist
#need to respond to ros interrupt to terminate robot
from rclpy.exceptions import ROSInterruptException
import signal

class FirstWalker(Node):
    def __init__(self):
        super().__init__('firstwalker')

        #define publiser to cmd_vel and the rate at which velocities are sent
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.rate = self.create_rate(10)  # 10 Hz

    def walk_forward(self):
        #empty twisst object - defining 0 velocity
        desired_velocity = Twist()
        desired_velocity.linear.x = 0.2  # Forward with 0.2 m/s

        #constant loop rate of 10Hz - publishing the speed
        for _ in range(30):  # Stop for a brief moment
            self.publisher.publish(desired_velocity)
            self.rate.sleep()

    #same concept with a negative forward velocity 
    def walk_backward(self):
        desired_velocity = Twist()
        desired_velocity.linear.x = -0.2  # Backward with 0.2 m/s
        for _ in range(30):  # Stop for a brief moment
            self.publisher.publish(desired_velocity)
            self.rate.sleep()

    #forces the robot to stop
    def stop(self):
        desired_velocity = Twist()
        desired_velocity.linear.x = 0.0  # Send zero velocity to stop the robot
        self.publisher.publish(desired_velocity)

def main():
    #signal defined to stop the robot when ctrl+c pressed
    def signal_handler(sig, frame):
        first_walker.stop()
        rclpy.shutdown()

    rclpy.init(args=None)
    first_walker = FirstWalker()

    signal.signal(signal.SIGINT, signal_handler)

    #creates seperate thread to handle communication - allowing other concurrent commands
    thread = threading.Thread(target=rclpy.spin, args=(first_walker,), daemon=True)
    thread.start()

    #inifinite loop in ROS
    try:
        while rclpy.ok():
            first_walker.walk_forward()
            first_walker.walk_backward()
    except ROSInterruptException:
        pass


if __name__ == "__main__":
    main()


