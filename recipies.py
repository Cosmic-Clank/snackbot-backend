def make_regularpopcorn(arm):
    go_to_home_pose(arm)


def make_kettlecorn(arm):
    go_to_home_pose(arm)


def make_cranberry_juice(arm):
    go_to_home_pose(arm)


def make_grape_juice(arm):
    go_to_home_pose(arm)


def make_apple_juice(arm):
    go_to_home_pose(arm)


def make_coffee(arm):
    go_to_home_pose(arm)


def go_to_upright_pose(arm):
    pass


def go_to_home_pose(arm):
    arm.go_to_home_pose()


def go_to_juice_cranberry(arm):
    arm.set_single_joint_position("waist", 0.5)
    arm.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_juice_grape(arm):
    arm.set_single_joint_position("waist", 0.5)
    arm.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_juice_apple(arm):
    arm.set_single_joint_position("waist", 0.5)
    arm.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_coffee(arm):
    arm.set_single_joint_position("waist", 0.5)
    arm.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_kettlecorn(arm):
    arm.set_single_joint_position("waist", 0.5)
    arm.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_regularpopcorn(arm):
    arm.set_single_joint_position("waist", 0.5)
    arm.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_serve_popcorn(arm):
    arm.set_single_joint_position("waist", 0.5)
    arm.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_serve_drink(arm):
    arm.set_single_joint_position("waist", 0.5)
    arm.set_single_joint_position("shoulder", -0.5)
    # more steps...
