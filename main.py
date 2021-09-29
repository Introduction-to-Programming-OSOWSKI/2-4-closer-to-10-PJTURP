#def close10
def close10(x,y):
    if abs(x-10)<abs(y-10):
        return x 

    elif abs(x-10)==abs(y-10):
         return 0

    else:
        return y

#run
print(close10(8,11))