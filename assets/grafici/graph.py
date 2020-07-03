import matplotlib.pyplot as plt
#ep , n_linee , score , Env rewards , step fatti 
with open('terzo_test.txt', 'r') as f:
    data = f.readlines()
game_1 = [[float(n) for n in el.split(' , ')] for el in data if el[0:2] == '1 ']
game_2 = [[float(n) for n in el.split(' , ')] for el in data if el[0:2] == '2 ']

# 20 o delta_step
#primo x = [200,300,400,500,600,700,800,900,1000]
#secondo x = [20,40,60,80,100,120,140,160,180,200,220,240,260]
#terzo 
x = [20,40,60,80,100,120,140,160,180,200,220,240]
y_1 = [el[2] for el in game_1]
y_2 = [el[2] for el in game_2]
plt.grid(True)
plt.xlabel('Learn Steps')
plt.ylabel('Game Score')
plt.plot(x, y_1, 'b', label="Game 1")
plt.plot(x, y_2, 'r', label="Game 2")
plt.legend()
plt.show()