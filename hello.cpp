#include <ros/ros.h>                             // 引用 ros.h 檔
#include <ros/ros.h>                             // 引用 ros.h 檔

int main(int argc, char** argv){
    ros::init(argc, argv, "hello_cpp_node");     // 初始化hello_cpp_node
    ros::NodeHandle handler;                     // node 的 handler
    double frq;
    while (ros::ok()){                           // 在 ros 順利執行時
	handler.getParam("/print_freq", frq);
        ROS_INFO("Hello World! by cpp");                // 印出 Hello World
        ros::Duration(frq).sleep();                // 間隔 1 秒
    }
}
