from picarx import Picarx
import time


if __name__ == "__main__":
    try:

        px = Picarx()
        px.forward(10)
        time.sleep(2.25)

        px.set_dir_servo_angle(25)
        px.forward(2)
        time.sleep(0.90)

        px.set_dir_servo_angle(0)
        px.forward(10)
        time.sleep(3.25)

        px.set_dir_servo_angle(-25)
        px.forward(2)
        time.sleep(1)

        px.set_dir_servo_angle(0)
        px.forward(10)
        time.sleep(4.10)

        px.set_dir_servo_angle(27)
        px.forward(2)
        time.sleep(1.15)

        px.set_dir_servo_angle(0)
        px.forward(10)
        time.sleep(1.75)


        
    finally:
        px.forward(0)