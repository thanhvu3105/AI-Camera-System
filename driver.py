import sys
from multiprocessing import Process 


from Camera import PorchCam

def main():
    PCam = PorchCam.PorchCam(0)
    PCam.run()
    
    
if __name__ == '__main__':
    main()