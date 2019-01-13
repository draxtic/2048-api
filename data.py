from game2048.game import Game
from game2048.agents import Agent, RandomAgent, ExpectiMaxAgent

import numpy as np
import datetime
import csv
import math

class Data(ExpectiMaxAgent):
    
    def log(self, data_dir="./data/", max_iter=np.inf):
        
        filename = data_dir + datetime.datetime.now().strftime('%y%m%d_%H%M%S_%f') + ".csv"
        with open(filename,"w") as csvfile: 
            writer = csv.writer(csvfile)
            n_iter = 0
            while (n_iter < max_iter) and (not self.game.end):
                direction = self.step()
                bd = list(self.game.board.flatten())
                bd = [int(s) for s in bd]
                bd = [int(math.log(i,2)) if i>0 else i for i in bd]
                bd.append(direction)
                writer.writerow(bd)
                self.game.move(direction)
                n_iter += 1
        DataAgent.count += 1
Data.count = 0

def gen(data_dir = "./m/data", number = 10):
    for i in range(number):
        game = Game(4, score_to_win=2048, random=False)
        agent = DataAgent(game, display=None)
        agent.auto_log(data_dir=data_dir)

THREAD_NUM = 8
LOGFILE_NUM = 500

import os
if not os.path.exists("./m/"):
    os.mkdir("./m/")
for i in range(THREAD_NUM):
    path = "./m/data%d/"%i
    if not os.path.exists(path):
        os.mkdir(path)

import _thread
DataAgent.number = 0
for i in range(THREAD_NUM):
    _thread.start_new_thread( gen, ("./m/data%d/"%i, LOGFILE_NUM) )


while 1:
    pass
