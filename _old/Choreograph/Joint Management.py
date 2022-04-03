from naoqi import ALProxy
import qi 
import argparse
import sys
import time
import json


def set_angles(session,name,angle):
    motion_service  = session.service("ALMotion")

    motion_service.setStiffnesses(name, 1.0)

    # Example showing how to set angles, using a fraction of max speed
    fractionMaxSpeed  = 0.1
    motion_service.setAngles(names, angles, fractionMaxSpeed)

    time.sleep(3.0)
    motion_service.setStiffnesses(name, 0.0)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    
    #Write main code here
    





