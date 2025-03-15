#ALTIMETER GUI#
import time
import math


class Altimeter:
    def __init__(self, sea_level_pressure=1013.25):
        """
        Initialize the altimeter with sea-level pressure in hPa.
        """
        self.sensor = BMP085.BMP085()
        self.sea_level_pressure = sea_level_pressure

    def get_pressure(self):
        """
        Get the current atmospheric pressure in hPa.
        """
        return self.sensor.read_pressure() / 100.0  # Convert from Pa to hPa

    def get_temperature(self):
        """
        Get the current temperature in Celsius.
        """
        return self.sensor.read_temperature()

    def calculate_altitude(self):
        """
        Calculate the altitude based on current pressure and sea-level pressure.
        """
        pressure = self.get_pressure()
        altitude = 44330 * (1.0 - (pressure / self.sea_level_pressure) ** (1/5.255))
        return altitude

    def display_readings(self):
        """
        Display the current temperature, pressure, and altitude.
        """
        temperature = self.get_temperature()
        pressure = self.get_pressure()
        altitude = self.calculate_altitude()

        print(f"Temperature: {temperature:.2f} °C")
        print(f"Pressure: {pressure:.2f} hPa")
        print(f"Altitude: {altitude:.2f} meters")

if __name__ == "__main__":
    altimeter = Altimeter(sea_level_pressure=1013.25)  # Adjust sea-level pressure as needed

    try:
        while True:
            print("\nAltimeter Readings:")
            altimeter.display_readings()
            time.sleep(2)  # Wait for 2 seconds before updating
    except KeyboardInterrupt:
        print("Exiting Altimeter Interface.")
