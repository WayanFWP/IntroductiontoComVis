import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

def callback(msg):
    bridge = CvBridge()
    try:
        frame = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        rospy.logerr(f"CV Bridge error: {e}")
        return

    cv2.imshow("Camera Feed", frame)
    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        rospy.signal_shutdown("ESC pressed.")

def main():
    rospy.init_node('image_subscriber', anonymous=True)
    rospy.Subscriber('/camera/image_raw', Image, callback)
    rospy.loginfo("Image subscriber started.")
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
