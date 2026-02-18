import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8


class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        #subscribes to the chatter topic (type of message, topic, method to prcoess messages)
        self.subscription = self.create_subscription(String, 'chatter', self.listener_callback, 10)
        self.numeric_subscription = self.create_subscription(Int8, 'numeric_chatter', self.numeric_listener_callback, 10)
        self.subscription  # prevent unused variable warning
    
    #callback when recieved
    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data!r}')

    def numeric_listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data!r}')


def main(args=None):
    rclpy.init(args=args)
    listener = Listener()
    rclpy.spin(listener)


if __name__ == '__main__':
    main()
