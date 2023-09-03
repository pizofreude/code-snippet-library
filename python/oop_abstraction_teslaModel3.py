class TeslaModel3:
    """
    A class to represent a Tesla Model 3 car.
    """

    def __init__(self, color, range):
        """
        Initialize the car with the given color and range.
        """
        self.color = color
        self.range = range

        # Initialize the car's safety features.
        self.autopilot = Autopilot()
        self.forward_collision_warning = ForwardCollisionWarning()
        self.lane_departure_warning = LaneDepartureWarning()

    def accelerate(self):
        """
        Accelerate the car.
        """
        self.autopilot.enable()
        print("The car is accelerating.")

    def brake(self):
        """
        Brake the car.
        """
        self.autopilot.disable()
        print("The car is braking.")

    def get_color(self):
        """
        Get the car's color.
        """
        return self.color

    def get_range(self):
        """
        Get the car's range.
        """
        return self.range

    def safety_test(self):
        """
        Run the car's safety tests.
        """
        self.forward_collision_warning.test()
        self.lane_departure_warning.test()


class Autopilot:
    """
    A class to represent the car's autopilot feature.
    """

    def enable(self):
        """
        Enable the autopilot feature.
        """
        print("Autopilot enabled.")

    def disable(self):
        """
        Disable the autopilot feature.
        """
        print("Autopilot disabled.")


class ForwardCollisionWarning:
    """
    A class to represent the car's forward collision warning feature.
    """

    def test(self):
        """
        Test the forward collision warning feature.
        """
        print("Forward collision warning test passed.")


class LaneDepartureWarning:
    """
    A class to represent the car's lane departure warning feature.
    """

    def test(self):
        """
        Test the lane departure warning feature.
        """
        print("Lane departure warning test passed.")


def main():
    """
    The main function.
    """
    color = input("Enter the car's color: ")

    # Get the car's range from the user.
    range_options = {
        "Standard Range Plus": 272,
        "Long Range": 358,
        "Performance": 315,
    }

    while True:
        range = input("Enter the car's range (Standard Range Plus, Long Range, or Performance): ")
        try:
            range = range_options[range]
            break
        except KeyError:
            print("Please enter a valid range option.")

    car = TeslaModel3(color, range)

    print("The car's color is:", car.get_color())
    print("The car's range is: {} miles ({} km)".format(range, range * 1.60934))

    # Run the car's safety tests.
    car.safety_test()

    # Accelerate the car.
    car.accelerate()

    # Brake the car.
    car.brake()


if __name__ == "__main__":
    main()
