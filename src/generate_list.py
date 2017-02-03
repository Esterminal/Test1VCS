import random

def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    k = len(alist)
    s = sum(alist)
    if (k==0):
        print "value is null"
    if (s<-100):
        print "sum less than -100"
    
    assert k!=0,"value is null"
    assert s>-100,"sum alist < -100"
    
    return alist
    
    
def printIt():
    print(generate_list())
    
def main():
    printIt()
    
if __name__ == "__main__":
    print("Test printIt():")
    main()
