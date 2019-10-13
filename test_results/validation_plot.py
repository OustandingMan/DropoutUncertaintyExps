import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

taus = []
rates = []
scores = []

with open('validation_MC_rmse_10_xepochs_1_hidden_layers.txt', 'r') as score_file:
    for line in score_file.readlines():
        line_split = line.split()
        rates += [float(line_split[1])]
        taus += [float(line_split[3])]
        scores += [float(line_split[5])]
        
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
ax.scatter3D(rates, taus, scores, c=scores)
ax.set_xlabel('tau')
ax.set_ylabel('dropout rate')
ax.set_zlabel('score')