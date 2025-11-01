import rclpy
from turtlesim.msg import Pose

def callback(msg):
    print('x=:',msg.x)
    print('y=:',msg.y)

def position_sub():
    rclpy.init()
    node = rclpy.create_node('turtle_position')
    subscription = node.create_subscription( Pose, '/turtle1/pose', callback, 10)

    try:
        rclpy.spin(node)
    
    except KeyboardInterrupt:
        print('Node shutdown requested by user!')

    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__=='__main__':
    position_sub()