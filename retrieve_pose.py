from interbotix_xs_modules.xs_robot.arm import ArmModule
import time


def main():
    arm = ArmModule(robot_model="wx250", robot_name="arm1")
    arm.go_to_home_pose()
    time.sleep(1)

    print("\n[🤖] Move the arm where you want, then type 's' to capture position.")

    while True:
        cmd = input("\nType 's' or 'exit': ").strip()

        if cmd == "exit":
            break
        elif cmd == "s":
            joints = arm.arm.get_joint_positions()
            pose = arm.arm.get_ee_pose()
            print("\n[📋] Saved Joint Positions:", joints)
            print("[📋] Saved EE Pose (x,y,z,r,p,y):", pose)
        else:
            print("[⚠️] Unknown command.")

    arm.shutdown()


if __name__ == "__main__":
    main()
