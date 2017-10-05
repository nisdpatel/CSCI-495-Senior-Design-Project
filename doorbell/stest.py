from gpiozero import DistanceSensor

ultrasonic = DistanceSensor(echo=24, trigger=23)
while True:
    ultrasonic.wait_for_in_range()
    print("in range")
    ultrasonic.wait_for_out_of_range()
    print("out") 
    
