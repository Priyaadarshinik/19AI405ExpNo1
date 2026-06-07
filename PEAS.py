import random

class MedicinePrescribingAgent:
    def __init__(self):
        self.performance = 0

    def check_patient(self, room, temperature):
        print(f"\nChecking Room {room}")
        print(f"Patient Temperature: {temperature}°F")

        if temperature > 98.5:
            print("Patient is unhealthy (Fever detected).")
            self.actuators.prescribe_medicine(room)
            self.performance += 1
        else:
            print("Patient is healthy.")

    def move(self, from_room, to_room):
        print(f"\nMoving from Room {from_room} to Room {to_room}")
        self.performance -= 1

    def display_performance(self):
        print("\nFinal Performance:", self.performance)


class TemperatureSensor:
    def get_temperature(self):
        # Random temperature between 97 and 103
        return round(random.uniform(97.0, 103.0), 1)


class MedicineActuator:
    def prescribe_medicine(self, room):
        print(f"Medicine prescribed to patient in Room {room}")


if __name__ == "__main__":

    sensor = TemperatureSensor()
    actuator = MedicineActuator()

    agent = MedicinePrescribingAgent()
    agent.actuators = actuator

    # Room A
    tempA = sensor.get_temperature()
    agent.check_patient("A", tempA)

    # Move to Room B
    agent.move("A", "B")

    # Room B
    tempB = sensor.get_temperature()
    agent.check_patient("B", tempB)

    # Display performance
    agent.display_performance()