import rclpy

from geometry_msgs.msg import Twist

count=0

def pub_turtle():
    rclpy.init()
    node = rclpy.create_node('random_turtle')

    publisher = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
    vel_msg = Twist()

    vel_msg.linear.x = 2.0
    vel_msg.angular.z= 0.0
    
    def timer_callback():
        global count
        if count==6:
            count=0
        else:
            count += 1
        
        if count<2:
            vel_msg.linear.x = 2.0
            vel_msg.angular.z = 2.0
        else:
            vel_msg.linear.x = 2.0
            vel_msg.angular.z = 0.0

        publisher.publish(vel_msg)
            
    timer_period = 1.0
    timer=node.create_timer(timer_period, timer_callback)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Node shutdown requested by user!')
    finally:
        node.destroy_timer(timer)
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    pub_turtle()

