import matplotlib.pyplot as plt

def draw(x = [], y = [],type = "disctete", title = 'Signal', color='black'):
    
    
    plt.title = title
    plt.axhline(0, color='black')
    plt.xlim(min(x), max(x) + 1)
    plt.ylim(min(y) - 1, max(y) + 1)
    if (type == "continuous" or type == 'both'):
        plt.plot(x, y, 'b-', label="Continuous", color = color)
        
    if(type == "discrete" or type == 'both'):
        plt.stem(x, y, linefmt='-',
                     markerfmt='ro', basefmt=' ', label="Discrete")

    
    plt.show()
        
    
    
    