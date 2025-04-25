from interbotix_xs_modules.xs_robot.arm import ArmModule
import recipies  # Assuming this is the correct import for the popcorn module


class ArmController:
    def __init__(self, robot_model="wx250", robot_name="arm1"):
        self.arm = ArmModule(robot_model=robot_model, robot_name=robot_name)

    def move_home(self):
        self.arm.go_to_home_pose()

    def make_regularpopcorn(self):
        print("[🍿] Arm1 making regular popcorn...")
        recipies.make_regularpopcorn(self.arm)

    def make_kettlecorn(self):
        print("[🍿] Arm1 making kettlecorn...")
        recipies.make_kettlecorn(self.arm)

    def make_coffee(self):
        print("[☕] Arm2 making coffee...")
        recipies.make_coffee(self.arm)

    def make_grape_juice(self):
        print("[🍇] Arm2 making grape juice...")
        recipies.make_grape_juice(self.arm)

    def make_apple_juice(self):
        print("[🍏] Arm2 making apple juice...")
        recipies.make_apple_juice(self.arm)

    def make_cranberry_juice(self):
        print("[🍒] Arm2 making cranberry juice...")
        recipies.make_cranberry_juice(self.arm)

    def shutdown(self):
        self.arm.shutdown()
