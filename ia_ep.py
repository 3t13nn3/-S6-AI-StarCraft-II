#Etienne PENAULT 17805598
'''
python -m pysc2.bin.agent --map FindAndDefeatZerglings --agent ia_ep.Simple --max_episodes=1 --step_mul 1

step return une action, elle peut return une queue d'actions.

'''


from pysc2.agents import base_agent
from pysc2.lib import actions

import time

class Simple(base_agent.BaseAgent):

    def step(self, obs):
        time.sleep(0.06)
        super(Simple, self).step(obs)
        return actions.FUNCTIONS.no_op()