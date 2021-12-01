import argparse
from extra.displaylist import Menu, Name
from extra.respond import proceed

def parse():
    paresr = argparse.ArgumentParser(f'''
        Threat Intelligence Project tool   .

            Possible Options with -d paramater 

            {Menu}

            Note : for Multiple commands Seperate options by commas 
        
                eg : {Name} -t example.com -d 1,2,3,4
                     {Name} -t example.com -d locate,2,github,activescan
                
        ''')
    paresr.add_argument("-t","--target",help="To Specify a target",required=True)
    paresr.add_argument("-d","--do",help="To Specify what to do ",required=True)
    return paresr.parse_args()

def main():
    try:
        arg=parse()
        target=arg.target
        todo=arg.do

        todo = todo.strip(" ")
        todo = todo.split(",")
        for i in todo:
            proceed(str(i),target)
    except:
        pass

if __name__ == "__main__":
    main()