class Ball:

    def __init__(
        self,
        x: int,
        y: int,
        z: int,
        pitch: int,
        yaw: int,
        roll: int,
        velocity_x: int,
        velocity_y: int,
        velocity_z: int,
        angular_velocity_x: int,
        angular_velocity_y: int,
        angular_velocity_z: int,
        towards_our_goal: bool,
        towards_their_goal: bool,
        towards_neutral: bool,
        grid_position: int
        ):

        self.x = x
        self.y = y
        self.z = z
        self.pitch = pitch
        self.yaw = yaw
        self.roll: roll
        self.velocity_x = velocity_x,
        self.velocity_y = velocity_y,
        self.velocity_z = velocity_z
        self.angular_velocity_x = angular_velocity_x,
        self.angular_velocity_y = angular_velocity_y,
        self.angular_velocity_z = angular_velocity_z,
        self.towards_our_goal = towards_our_goal,
        self.towards_their_goal = towards_their_goal,
        self.towards_neutral = towards_neutral,
        self.grid_position = grid_position

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_pitch(self):
        return self.pitch

    def get_yaw(self):
        return self.yaw

    def get_roll(self):
        return self.roll

    def get_velocity_x(self):
        return self.velocity_x

    def get_velocity_y(self):
        return self.velocity_y

    def get_velocity_z(self):
        return self.velocity_z

    def get_angular_velocity_x(self):
        return self.velocity_x

    def get_angular_velocity_y(self):
        return self.velocity_y

    def get_angular_velocity_z(self):
        return self.velocity_z

    def get_towards_our_goal(self):
        return self.towards_our_goal

    def get_towards_their_goal(self):
        return self.towards_their_goal

    def get_towards_neutral(self):
        return self.towards_neutral

    def get_grid_position(self):
        return self.grid_position

    def set_towards_our_goal(self, towards_our_goal: bool):
        self.towards_our_goal = towards_our_goal

    def set_towards_their_goal(self, towards_their_goal: bool):
        self.towards_their_goal = towards_their_goal

    def set_towards_neutral(self, towards_neutral: bool):
        self.towards_neutral = towards_neutral