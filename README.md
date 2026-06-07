<h1>ExpNo 1 :Developing AI Agent with PEAS Description</h1>
<h3>Name: Priyaadarshini K</h3>
<h3>Register Number: 212223240126</h3>


<h3>AIM:</h3>
<br>
<p>To find the PEAS description for the given AI problem and develop an AI agent.</p>
<br>
<h3>Theory</h3>
<h3>Medicine prescribing agent:</h3>
<p>Such this agent prescribes medicine for fever (greater than 98.5 degrees) which we consider here as unhealthy, by the user temperature input, and another environment is rooms in the hospital (two rooms). This agent has to consider two factors one is room location and an unhealthy patient in a random room, the agent has to move from one room to another to check and treat the unhealthy person. The performance of the agent is calculated by incrementing performance and each time after treating in one room again it has to check another room so that the movement causes the agent to reduce its performance. Hence, agents prescribe medicine to unhealthy.</p>
<hr>
<h3>PEAS DESCRIPTION:</h3>
<table>
  <tr>
    <td><strong>Agent Type</strong></td>
    <td><strong>Performance</strong></td>
     <td><strong>Environment</strong></td>
    <td><strong>Actuators</strong></td>
    <td><strong>Sensors</strong></td>
  </tr>
    <tr>
    <td><strong>Medicine prescribing agent</strong></td>
    <td><strong>Treating unhealthy, agent movement</strong></td>
     <td><strong>Rooms, Patient</strong></td>
    <td><strong>Medicine, Treatment</strong></td>
    <td><strong>Location, Temperature of patient</strong></td>
  </tr>
</table>
<hr>
<H3>DESIGN STEPS</H3>
<h3>STEP 1:Identifying the input:</h3>
<p>Temperature from patients, Location.</p>
<h3>STEP 2:Identifying the output:</h3>
<p>Prescribe medicine if the patient in a random has a fever.</p>
<h3>STEP 3:Developing the PEAS description:</h3>
<p>PEAS description is developed by the performance, environment, actuators, and sensors in an agent.</p>
<h3>STEP 4:Implementing the AI agent:</h3>
<p>Treat unhealthy patients in each room. And check for the unhealthy patients in random room</p>
<h3>STEP 5:</h3>
<p>Measure the performance parameters: For each treatment performance incremented, for each movement performance decremented</p>

## PROGRAM
```
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
```
## OUTPUT
![alt text](image.png)

## RESULT
Thus the Developing AI Agent with PEAS Description was implemented using python programming.
