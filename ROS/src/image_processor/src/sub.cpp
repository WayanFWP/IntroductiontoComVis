#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/opencv.hpp>

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
    try
    {
        // Konversi pesan ROS -> OpenCV
        cv::Mat frame = cv_bridge::toCvShare(msg, "bgr8")->image;

        // Tampilkan gambar
        cv::imshow("Camera Feed (C++)", frame);
        cv::waitKey(1);
    }
    catch (cv_bridge::Exception& e)
    {
        ROS_ERROR("cv_bridge exception: %s", e.what());
    }
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "camera_subscriber");
    ros::NodeHandle nh;

    // image_transport untuk efisiensi transfer image
    image_transport::ImageTransport it(nh);
    image_transport::Subscriber sub = it.subscribe("/camera/image_raw", 1, imageCallback);

    ROS_INFO("Camera subscriber running...");
    ros::spin();
}
