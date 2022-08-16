from picarx import Picarx
import time


if __name__ == "__main__":
    try:

        px = Picarx()
        px.forward(10)
        time.sleep(2.55)

        px.set_dir_servo_angle(-20)
        px.forward(2)
        time.sleep(0.5)


        px.set_dir_servo_angle(0)
        px.forward(10)
        time.sleep(3.75) 

        px.set_dir_servo_angle(20)
        px.forward(2)
        time.sleep(2)
   
        
        px.set_dir_servo_angle(0)
        px.forward(10)
        time.sleep(5.75) 

        
    finally:
        px.forward(0)