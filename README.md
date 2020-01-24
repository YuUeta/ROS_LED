# ROS_LED

## 作成したプログラムについて
### 使用方法
```
sudo apt install ros-kinetic-rosbridge-suite
roscore
roslaunch rosbridge_server rosbridge_websocket.launch
rosrun mypkg led_pub.py
rosrun mypkg led_sub.py
```
### コマンド
+ a : 1つ目のLEDのみを点灯する
+ b : 2つ目のLEDのみを点灯する
+ c : 3つ目のLEDのみを点灯する
+ d : 4つ目のLEDを間欠点灯する
+ q : すべてのLEDを消す

## 動画URL
作成したプログラムの動画  
https://www.youtube.com/watch?v=6Zje_HVxAPc
