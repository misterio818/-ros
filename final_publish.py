
import rospy
from std_msgs.msg import Int64

def publish_std_id(std_id):
    rospy.init_node('final_publisher', anonymous=True)
    pub = rospy.Publisher('/std_id', Int64, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        pub.publish(std_id)
        rate.sleep()

if __name__ == '__main__':
    try:
        std_id = 6352500030  # รหัสนิสิตของคุณ
        publish_std_id(std_id)
    except rospy.ROSInterruptException:
        pass
