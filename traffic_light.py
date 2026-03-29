import time


class TrafficLightController:
    def __init__(self, red_duration: int = 5, green_duration: int = 5):
        self.red_duration = red_duration
        self.green_duration = green_duration
        self.state = "RED"

    def switch(self):
        if self.state == "RED":
            self.state = "GREEN"
            return self.green_duration
        self.state = "RED"
        return self.red_duration

    def run(self, cycles: int = 6):
        for _ in range(cycles):
            duration = self.switch()
            print(f"Light: {self.state}, duration: {duration}s")
            time.sleep(duration)


if __name__ == "__main__":
    controller = TrafficLightController(red_duration=3, green_duration=3)
    controller.run(cycles=4)
