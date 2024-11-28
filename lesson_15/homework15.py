"""
HW15.1 Geometry shape 'Rhombus'.

Create a 'Rhombus' geometry shape class.
The class must have the following attributes:
- side_a (length of side a).
- angle_a (the angle between sides a and b).
- angle_b (adjacent to angle angle_a).
The following requirements must be implemented:
1. The value of side_a must be greater than 0.
2. The angles angle_a and angle_b must satisfy the condition:
angle_a + angle_b = 180
3. The opposite angles of the rhombus are always equal,
so at a given value of angle_a,
the value of angle_b is calculated automatically.
Use the __setattr__ method to set attribute values.
"""


class Rhombus:
    """
    A class discribed a geometry shape Rhombus.

    Attributes:
        side_a (int): side a of the Rhombus.
        angle_a (int): angle between sides a and b.
        angle_b (int): adjacent to angle angle_a (Optional).
    """

    def __init__(self, side_a, angle_a, angle_b=None):
        """Initialize a new Rhombus with parameters."""
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = angle_b

    def __setattr__(self, key, value):
        """Set and check parameters."""
        # requirement 1
        if key in ('side_a', 'angle_a'):
            if not isinstance(value, int) or value <= 0:
                raise ValueError(f'{key} must be a positive number')
        super().__setattr__(key, value)

        # requirement 2
        if key in ('angle_b') and value is not None:
            if (180 - self.angle_a) != self.angle_b:
                raise ValueError('Sum of angel_a and b must be equal 180.')
        # requirement 3
        if key in ('angle_b') and value is None:
            super().__setattr__('angle_b', self.angle_a)
            if (180 - self.angle_a) != self.angle_b:
                raise ValueError('Sum of angel_a and b must be equal 180.')
        if key in ('angle_b') and value is not None and value <= 0:
            raise ValueError(f'{key} must be a positive number')
