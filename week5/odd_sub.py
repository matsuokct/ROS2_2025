import rclpy
from std_msgs.msg import Int32

def callback(msg):
    print('odd_data:',msg.data)

def odd_number_sub():
    rclpy.init()
    node = rclpy.create_node('odd_subscriber')
    subscription = node.create_subscription( Int32, 'odd', callback, 10)

    try:
        rclpy.spin(node)
    
    except KeyboardInterrupt:
        print('Node shutdown requested by user!')

    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__=='__main__':
    odd_number_sub()