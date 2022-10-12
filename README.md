# pick_place
```
roslaunch kinova_with_d435 run.launch 
roslaunch j2s7s300_moveit_config j2s7s300_gazebo_demo.launch 
rqt_image_view
rosrun kinova_arm_moveit_demo pick_place
roslaunch gpd_ros ur5.launch 
```


# 一键启动
```
roscd tao-kinova
sudo chmod +x fake_run.sh
./fake_run.sh
```