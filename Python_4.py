# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:29:06 2021

@author: Josh Mossing
Week 4 Discussion HW- Classes
"""
#The Class Wrestler is initialized with following attributes below
#team, weight_class, wins, losses, and rank

#The methods within the class wrestler are __init__, compute_win_percentage
#get_weight_group, and compute_rank_percentage

#The instances that were created are wrestler1 and wrestler 2. 
#Their information is passed into the methods 

class Wrestler: 
    num_wrestlers = 0
    def __init__(self, team: str, weight_class: int, wins: int, losses: int, rank: int):
        self.team = team
        self.weight_class = weight_class
        self.wins = wins
        self.losses = losses
        self.rank = rank
        
        Wrestler.num_wrestlers +=1
    def compute_win_percentage(self) -> float: 
        win_percentage = self.wins / (self.wins + self.losses) 
        return win_percentage
        
    def get_weight_group(self) -> str:
        if self.weight_class <= 141:
            weight_group = "Lower weight"
        elif self.weight_class <=174:
            weight_group = "Middle weight"
        else:
            weight_group = "Heavyweight"
        return weight_group

#rank percentage is divided by 78 because there are 78 division 1 wrestling teams 
    def compute_rank_percentage(self) -> float:
        rank_percentage = self.rank / 78
        return (rank_percentage)
    
    @classmethod
    def set_raise_amt (cls, amount):
        cls.num_wrestlers = amount
    

        
Wrestler.set_raise_amt(5)
#wrestler 1 and 2 are instances that are created from the Wrestling class
wrestler1 = Wrestler("Iowa", 141, 30, 1, 2)
# print(wrestler1.team)
# print(wrestler1.compute_win_percentage())
# print(wrestler1.get_weight_group())
# print(wrestler1.compute_rank_percentage())

wrestler2 = Wrestler("Navy", 197, 6, 24, 66)
print(Wrestler.num_wrestlers)
# print(wrestler2.team)
# print(wrestler2.compute_win_percentage())
# print(wrestler2.get_weight_group())
# print(wrestler2.compute_rank_percentage())