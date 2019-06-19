from random import randrange

class Robot():
    max_damage = 5

    def __init__(self, lifes, jmeno):
        self.lifes = lifes
        self.jmeno = jmeno

    def _make_damage(self, target_robot):
        """Generates random damage and forces the
        other robot to defend."""
        damage = randrange(0, self.max_damage)
        target_robot.defend(damage)


    def _take_damage(self, damage):
        """Sets new number of lifes when not already 0."""
        if self.lifes - damage < 0:
            self.lifes = 0
        else:
            self.lifes -= damage
    
    def is_alive(self):
        """Returns True if robot has any lifes left."""
        return self.lifes > 0

    def defend(self, damage):
        """Default defend. Simply takes damage."""
        self._take_damage(damage)

    def attack(self, target_robot):
        """Default attack. Simply makes damage."""
        self._make_damage(target_robot)

class Aggressive(Robot):
    max_damage = 7
    def attack(self, target_robot):
        """Makes damage to the other robot twice. Special for aggresive robot."""
        self._make_damage(target_robot)
        self._make_damage(target_robot)

class Defensive(Robot):
    max_damage = 3    
    
    def defend(self, damage):
        """Special for deffensive robot, takes only half damage."""
        self._take_damage(damage // 2)

class Angry(Robot):
    max_damage = 5
    
    def complaining(self, lifes):
        """Just for fun, talking to other robots"""
        if lifes > 10:
            print("{}: You can never beat me".format(self.jmeno))
        elif lifes > 5 and lifes < 10:
            print("{}: Is that all you do?".format(self.jmeno))
        elif lifes < 5 and lifes > 0:
            print("{}: It is not end".format(self.jmeno))
        else:
            print("{}: Wait for the next time".format(self.jmeno))
    
    def defend(self, damage):
        self._take_damage(damage // 3)

class SuprAngry(Angry, Robot):
    max_damage = 3

    def complaining(self, lifes):
        print("{}: You loosers, can give it up right now".format(self.jmeno))
        super().complaining(lifes)
    
    def defend(self, damage):
        self._take_damage(damage)


aggr = Aggressive(15, "Aggr")
deff = Defensive(7, "Deff")
henry = Angry(15, "Henry")
jack = SuprAngry(7, "Jack")

while True:
    aggr.attack(henry)
    print('Henry: {}'.format(henry.lifes))
    henry.complaining(henry.lifes)
    if not henry.is_alive():
        print('Henry lost')
        break
    
    deff.attack(jack)
    print('Jack: {}'.format(jack.lifes))
    jack.complaining(jack.lifes)   
    if not jack.is_alive():
        print('Jack lost')
        break

    henry.attack(aggr)
    print('Aggr: {}'.format(aggr.lifes))
    if not aggr.is_alive():
        print('Aggr lost')
        break
    
    jack.attack(deff)
    print('Deff: {}'.format(deff.lifes))
    if not deff.is_alive():
        print('Deff lost')
        break