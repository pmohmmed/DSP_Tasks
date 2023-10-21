import matplotlib.pyplot as plt

def draw(x1 = [], y1 = [],x2 = None, y2 = None, label1 = "", label2="",type = "disctete", title = 'Signal'):
    plt.close()
    plt.axhline(0, color='black')
    count = 0
    if x1 is not None and y1 is not None and len(x1) > 0:
            
        count +=1
        
        if (type == "continuous" or type == 'both'):
            plt.plot(x1, y1, label=label1,color='#eb34ae')
            
        if(type == "discrete" or type == 'both'):
            plt.stem(x1, y1, linefmt='-',
                        markerfmt='ro', basefmt=' ')
            
    if x2 is not None and y2 is not None and len(x2) > 0:
        if (type == "continuous" or type == 'both'):
            plt.plot(x2, y2,  label=label2, color='#524a49')
            
        if(type == "discrete" or type == 'both'):
            plt.stem(x2, y2, linefmt='-',
                         basefmt=' ')
        count +=1
    
        

    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.title(title)
    plt.grid(True)
    if(count >1):
        plt.legend(loc='upper right')
    
    plt.show()
        
    
    
    