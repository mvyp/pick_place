gnome-terminal -t "gazebo" -x bash -c "roslaunch kinova_with_d435 run.launch;exec bash;"
sleep 5s
gnome-terminal -t "rviz" -x bash -c "roslaunch j2s7s300_moveit_config j2s7s300_gazebo_demo.launch; exec bash;"
sleep 0.1s
gnome-terminal -t "pick_place" -x bash -c "rosrun kinova_arm_moveit_demo my_pick_place;exec bash;"
sleep 0.1s
gnome-terminal -t "fake" -x bash -c "python3 -u '/home/tao/catkin_ws/src/gpd_ros/src/gpd_ros/test.py';exec bash;"
