import pyfirmata as py

# Check from device manager
port = 'COM7'

board = py.Arduino(port)

#SpeedR = board.get_pin('d:9:p')  # Assuming this is a PWM pin
Rpin1 = board.get_pin('d:7:o')   # Purple
Rpin2 = board.get_pin('d:8:o')
Lpin3 = board.get_pin('d:4:o')
Lpin4 = board.get_pin('d:6:o')
#SpeedL = board.get_pin('d:5:p')   # Assuming this is a PWM pin


def control_motor(gaze):
    if gaze.is_blinking():
        #SpeedR.write(0)
        #SpeedL.write(0)
        Rpin1.write(0)
        Rpin2.write(0)
        Lpin3.write(0)
        Lpin4.write(0)
        print("BRAKE")
        return "Brake"
        
    if gaze.is_right():
        #SpeedR.write(0)
        #SpeedL.write(1)
        Rpin1.write(0)
        Rpin2.write(0)
        Lpin3.write(1)
        Lpin4.write(0)
        print("RIGHT")
        return "Right"

    if gaze.is_left():
        #SpeedR.write(1)
        #SpeedL.write(0)
        Rpin1.write(1)
        Rpin2.write(0)
        Lpin3.write(0)
        Lpin4.write(0)
        print("LEFT")
        return "Left"

    if gaze.is_center():
        #SpeedR.write(1)
        #SpeedL.write(1)
        Rpin1.write(1)
        Rpin2.write(0)
        Lpin3.write(1)
        Lpin4.write(0)
        print("FORWARD")
        return "Up"
