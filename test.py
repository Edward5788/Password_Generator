
def main():
    print("Shalom to you all!")
    loop = False
    printCounter = 0
    while loop == False:
        
        print("Testing...")
        printCounter = printCounter + 1
        
        time.sleep(0.443)
        if printCounter == 2:
            calc = 0.443 * 2
            print("Calc: " + str(calc))
            loop = True
        
        

    
import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))




"""
import atexit

def my_exit_function(some_argument):
    # Your exit code goes here
    print("Shalom")

def testLol():
    if __name__ == '__main__':
        atexit.register(my_exit_function, 'some argument', )

        # Your script goes here
        
    
    
loop = False
while loop == False:
    
    print("Testing...")
    
    testLol()
    """