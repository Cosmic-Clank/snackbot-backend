def make_regularpopcorn(bot):
    bot.arm.go_to_home_pose()


def make_kettlecorn(bot):
    go_to_home_pose(bot)


def make_cranberry_juice(bot):
    go_to_home_pose(bot)


def make_grape_juice(bot):
    go_to_home_pose(bot)


def make_apple_juice(bot):
    go_to_home_pose(bot)


def make_coffee(bot):
    go_to_home_pose(bot)


def go_to_upright_pose(bot):
    pass


def go_to_home_pose(bot):
    bot.go_to_home_pose()


def go_to_juice_cranberry(bot):
    bot.set_single_joint_position("waist", 0.5)
    bot.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_juice_grape(bot):
    bot.set_single_joint_position("waist", 0.5)
    bot.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_juice_apple(bot):
    bot.set_single_joint_position("waist", 0.5)
    bot.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_coffee(bot):
    bot.set_single_joint_position("waist", 0.5)
    bot.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_kettlecorn(bot):
    bot.set_single_joint_position("waist", 0.5)
    bot.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_regularpopcorn(bot):
    bot.set_single_joint_position("waist", 0.5)
    bot.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_serve_popcorn(bot):
    bot.set_single_joint_position("waist", 0.5)
    bot.set_single_joint_position("shoulder", -0.5)
    # more steps...


def go_to_serve_drink(bot):
    bot.set_single_joint_position("waist", 0.5)
    bot.set_single_joint_position("shoulder", -0.5)
    # more steps...
