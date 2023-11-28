import ccm
log = ccm.log()

class State(ccm.Model):
    name = 'working'
    tower_a = []
    tower_b = []
    tower_c = []

class TowerOfHanoi(ccm.Model):

    state = State()

    def move_disk(self, disk):
        if self.state.name == 'working' and self.state.tower_a and not self.state.tower_b and not self.state.tower_c:
            self.state.tower_a.remove(disk)
            self.state.tower_b.append(disk)

    def move_disk_back(self, disk):
        if self.state.name == 'working' and not self.state.tower_a and self.state.tower_b and not self.state.tower_c:
            self.state.tower_b.remove(disk)
            self.state.tower_a.append(disk)

    def solve_tower(self):
        if self.state.name == 'working' and not self.state.tower_a and not self.state.tower_b and not self.state.tower_c:
            self.state.name = 'solved'

env = TowerOfHanoi()

# Initial state
env.state.tower_a = [3, 2, 1]
env.state.tower_b = []
env.state.tower_c = []

# Production rules
ccm.Model(isa='state', name='working', tower_a='top-of-tower ?disk', tower_b='top-of-tower nil', tower_c='top-of-tower nil').\
    add_rule(env.move_disk)

ccm.Model(isa='state', name='working', tower_a='top-of-tower nil', tower_b='top-of-tower ?disk', tower_c='top-of-tower nil').\
    add_rule(env.move_disk_back)

ccm.Model(isa='state', name='working', tower_a='top-of-tower nil', tower_b='top-of-tower nil', tower_c='top-of-tower nil').\
    add_rule(env.solve_tower)

# Run the model
ccm.display(env)
env.run()
ß