import rclpy
from rclpy.node import Node
#specify publishing a string
from std_msgs.msg import String

#define talker as inheriting from node
class Talker(Node):
    def __init__(self):
        #inheritance passing in node name
        super().__init__('talker')
        #creating a publisher (message typ, name of the topic, outgoing queue size)
        self.publisher = self.create_publisher(String, 'chatter', 10)

        #timer object - states how log in between each message
        timer_in_seconds = 0.5
        self.timer = self.create_timer(timer_in_seconds, self.talker_callback)
        self.counter = 0

    #create a string object, populate with data then publishj message
    def talker_callback(self):
        msg = String()
        msg.data = f'Hello World, {self.counter}'
        self.publisher.publish(msg)
        #simply logging
        self.get_logger().info(f'Publishing: {msg.data}')
        self.counter += 1

#initiate communications and instance class
def main(args=None):
    rclpy.init(args=args)

    talker = Talker()
    #spin allows script to run until killed
    rclpy.spin(talker)


if __name__ == '__main__':
    main()


