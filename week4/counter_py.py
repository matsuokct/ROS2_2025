import rclpy
from std_msgs.msg import Int32

def number_pub():
    rclpy.init()

    node = rclpy.create_node('simple_counter')

    publisher = node.create_publisher(Int32, 'number_topic', 10)

    counter=0

    def timer_callback():
        nonlocal counter

        counter += 1

        num_msg = Int32()
        num_msg.data =counter

        print('Publishing data:', num_msg.data)


        publisher.publish(num_msg)

    timer_period = 1.0

    timer = node.create_timer(timer_period, timer_callback)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Node shutdown requested by user!')
    
    finally:
        if rclpy.ok():
            node.destroy_timer(timer)
            node.destroy_node()
            rclpy.shutdown()

if __name__=='__main__':
    number_pub()
