from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    #specifies 2 nodes to be launched
    return LaunchDescription([
            Node(
                package='lab2',
                executable='talker',
                name='my_talker'
            ),
            Node(
                package='lab2',
                executable='listener',
                name='my_listener'
            ),
        ])
