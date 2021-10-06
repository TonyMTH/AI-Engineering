import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

def gradient_descent(function, x, max_it, threshold):
    """This function computes the gration descent of a given function

    Args:
        function (func): The function whose gradient descent will be computed
        x (float): The interval of evaluation
        max_it (int): The maximum number of iteration
        threshold (float): minimum allowed error

    Returns:
        (list,int): A tuple containing a list of evaluated points in the x-axis and the number of iterations
    """

    index = np.random.randint(0, len(x))
    point = x[index]
    derivative_in_point = derivative(function, point)

    it = 0 
    points = []

    #plotting
    plt.figure()
    plt.plot(X,Y)
    
    
    while np.abs(derivative_in_point)> threshold and it<max_it:

        if derivative_in_point < 0:
            x = x[index:]
        else:
            x = x[0:index+1]
        
        index = np.random.randint(0, len(x))
        point = x[index]
        points.append(point)
        derivative_in_point = derivative(function, point)
        
        #plotting
        plt.scatter(np.array(points), function(np.array(points)), c=range(len(points)), cmap=cm.jet)
        plt.pause(1)

        it +=1
        
    return points, it

def function(x):
    return 10*np.sin(x) - np.sin(1/x) + 5*np.cos(2*x) + 1/2*np.sin(np.exp(x)) + x


max_it = 10
threshold = 0.01
no_of_plots = 4

x = np.linspace(-7,5,10000)
X, Y = x, function(x)

for i in range(no_of_plots):
    points,it = gradient_descent(function, X, max_it, threshold)
    print("done: "+str(i+1)+"/"+str(no_of_plots))

plt.show()
