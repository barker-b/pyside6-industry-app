import math

class CylFormula():
    def __init__(self, bore, rod, pressure):
        self.bore = bore
        self.rod = rod
        self.pressure = pressure

    def piston_area(self):
        return math.pi * self.bore**2 / 4

    def annulus(self):
        return math.pi * self.bore**2 / 4 - math.pi * self.rod**2 / 4

    def cyl_ext_force(self):
        return self.pressure * self.piston_area()

    def cyl_ret_force(self):
        return self.pressure * self.annulus()

class MotorFormula():
    def __init__(self, displacement, flow, pressure):
        self.displacement = displacement
        self.flow = flow
        self.pressure = pressure

    def motor_torque(self):
        if self.displacement <= 0:
            return 0
        return (self.pressure * self.displacement) / (2 * math.pi) / 12

    def motor_speed(self):
        if self.displacement <= 0:
            return 0
        return 231 * self.flow / self.displacement

class PumpFormula():
    def __init__(self, rpm, displacement, pressure):
        self.rpm = rpm
        self.displacement = displacement
        self.pressure = pressure

    def output_flow(self):
        return self.rpm * self.displacement / 231

    def horse_power(self):
        return self.output_flow() * self.pressure / 1714

    def torque(self):
        return self.pressure * self.displacement / (2 * math.pi) / 12