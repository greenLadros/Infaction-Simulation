
#import
import pygame
import random
import time
from math import sqrt

#creating the class
class Sandbox():
    def __init__(self, population, plague, infected=1, width=1200, height=800):
        """
        The sandbox class.
        """
        self.population = population
        self.infected = infected
        self.width = width
        self.height = height
        self.plague = plague

    def run(self):
        #init
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Infection')
        icon = pygame.image.load('props/icon.png')
        pygame.display.set_icon(icon)
        deadNode = pygame.image.load('props/dead.png')

        #creating initial nodes
        initNode = pygame.image.load('props/node.png')
        initNodes = {}
        for node in range(1, self.population):
            loc = (random.randint(0, self.width), random.randint(0, self.height))
            screen.blit(initNode, loc)
            initNodes[loc] = loc
        
        infNode = pygame.image.load('props/inf_node.png')
        infNodes = {}
        print(self.infected)
        for node in range(0 ,self.infected):
            loc = (random.randint(0, self.width), random.randint(0, self.height))
            screen.blit(infNode, loc)
            infNodes[loc] = loc

        pygame.display.update()

        #Game loop
        running = True
        while running:
            for event in pygame.event.get():
                #checking if close button have been pressed
                if event.type == pygame.QUIT:
                    running = False
            
            #recovery and death system
            recNodes = []
            dedNodes = []
            for node in infNodes:
                if random.randint(0, 100) < self.plague['recovery_rate']: 
                    screen.blit(initNode, node)
                    initNodes[node] = node
                    recNodes.append(node)
                elif random.randint(0, 100) < self.plague['death_rate']: 
                    screen.blit(deadNode, node)
                    dedNodes.append(node)
            
            #deleting the nodes from infNodes
            for node in recNodes:
                del infNodes[node]
            for node in dedNodes:
                del infNodes[node]

            #checking for interaction between nodes
            susNodes = []
            for node in initNodes:
                for inf in infNodes:
                    x1, y1 = inf
                    x2, y2 = node
                    if sqrt((x1-x2)**2 + (y1-y2)**2) < self.plague['infection_radius']:
                        susNodes.append(node)
            
            #chances of becoming infected
            for node in susNodes:
                if random.randint(0, 100) < self.plague['infection_rate']: 
                    screen.blit(infNode, node)
                    infNodes[node] = node

            #print(susNodes)

            #updating display
            pygame.display.update()
            time.sleep(1)
