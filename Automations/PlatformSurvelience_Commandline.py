# python ProcessSurveilance.py 2 MarvellousLog
# python ProcessSurveilance.py Time_Interver Log_File
#           0                   1               2
import psutil
import sys
import os

def main():
    Border = ("_"*50)
    print(Border)
    print("----Marvellous platform Surveilance System----")
    print(Border)

    # --h and --u handeling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform")
            print("1: Information of running processes")
            print("2: Information about on Ram")
            print("3: Information about on HDD")
            print("4: Information about on Microprocessor:")
            print("5: Information about on Scheduled periodically")
            print("6: Information about on all records log file")
            print("7: Information about on Scheduled mail periodically")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print(f"python {sys.argv[0]} <time_interval> <folder_name>")
            print("time_interval : Time in minutes for periodic execution")
            print("folder_name : Log folder name")
        else:
            print("Unable to proceed as arguements are not matching")
            print("Please use --u or --h for more information.")
    elif(len(sys.argv) == 3):
        pass
    else:
        print("Invalid number of arguements")
        print("Unable to proceed as arguements are not matching")
        print("Please use --u or --h for more information.")

    print(Border)
    print("----Thank you for using out automation System----")
    print(Border)

if __name__ == "__main__":
    main()