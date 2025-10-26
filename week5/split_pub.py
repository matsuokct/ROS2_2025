import rclpy
from std_msgs.msg import Int32
count=0

def split():
    rclpy.init()

    #               Question1                #

    pub_odd = node.create_publisher(Int32, 'odd', 10)
    #                     Question2                 #
    
    

    def timer_callback():
        global count

        count += 1

        num_msg = Int32()
        num_msg.data =count

        if count%2 ==0:
            print('Publishing even_data:', num_msg.data)
            pub_even.publish(num_msg)
        else:
            #                 question3                #
            #    question4             #


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
    #     question5      #
