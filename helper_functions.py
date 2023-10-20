import matplotlib.pyplot as plt

def draw(x = [], y = [],type = "disctete", title = 'Signal'):
    
    if x is not None and y is not None and len(x) > 0:
            

        plt.axhline(0, color='black')
        plt.xlim(min(x), max(x) + 1)
        plt.ylim(min(y) - 1, max(y) + 1)
        if (type == "continuous" or type == 'both'):
            plt.plot(x, y, 'b-', label="Continuous")
            
        if(type == "discrete" or type == 'both'):
            plt.stem(x, y, linefmt='-',
                        markerfmt='ro', basefmt=' ', label="Discrete")

    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    
    plt.show()
        
    
    
    