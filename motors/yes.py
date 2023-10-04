# motor19_control.py

import serial
import time
def stop_motors():
    neutral_position = 1500  # Adjust if needed
    ser.write(generate_command({18: neutral_position, 19: neutral_position}).encode())

def generate_command(servos, time_of_execution=None, delay=None):
    """
    Generate a command string based on the provided servo positions and timings.

    :param servos: Dictionary of servo channels and their desired positions.
                   E.g., {19: 1400}
    :param time_of_execution: Time of execution (speed). Range: 0-9999
    :param delay: Instruction interval of delay time. Range: 0-9999
    :return: Command string.
    """
    command_parts = []
    
    for channel, position in servos.items():
        command_parts.append(f"#{channel}P{position}")
    
    if time_of_execution is not None:
        command_parts.append(f"T{time_of_execution}")
        
    if delay is not None:
        command_parts.append(f"D{delay}")
    
    return "".join(command_parts) + "\r\n"

# Open the serial connection
ser = serial.Serial('/dev/tty.usbmodem8780696D12331', 9600)

try:
    while True:
        # Move motor 19 to position 1400
        command1 = generate_command({19: 2000}, time_of_execution=2000)
        ser.write(command1.encode())
        time.sleep(2.1)  # Wait for movement to complete

        # Move motor 19 to position 2600
        command2 = generate_command({19: 2500}, time_of_execution=2000)
        ser.write(command2.encode())
        time.sleep(2.1)  # Wait for movement to complete
        user_input = input("Enter 'kill' to stop the motors or any other key to continue: ")
        
        if user_input.strip().lower() == "kill":
            stop_motors()
            print("Motors stopped.")
            break

except KeyboardInterrupt:
    # This will stop the loop when you press Ctrl+C
    stop_motors()
    print("Motors stopped due to keyboard interrupt.")

# Close the serial connection
ser.close()
