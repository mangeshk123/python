import psutil
import sys
import os
import time
import schedule

def processScan():
    list_process = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()
        list_process.append(info)
    return list_process
 
def platformSurvellience(foldername):
    Border = ("-"*50)
    Ret = False
    Ret = os.path.exists(foldername)
    if(Ret == True):
        Ret = os.path.isdir(foldername)
        if(Ret == False):
            print("Unable to proceed as directory name is exists but its not a directory")
            return        
    else:
        os.mkdir(foldername)
        print("Directory for log file gets created successfully")
    
    #######################################################################################
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    fileName = os.path.join(foldername, "Marvellous_%s.log" %timestamp)
    fobj = open(fileName,"w")
    print(f"Logfile gets successfully created with name {fileName}")
    fobj.write(Border + "\n")
    fobj.write("----Marvellous platform Surveilance System----\n")
    fobj.write(f"Log file gets created at :{timestamp} \n")
    fobj.write(Border+ "\n\n")

    fobj.write("---------------------System Report----------------------\n")
    # CPU information
    fobj.write("Number of active cores %s \n" %psutil.cpu_count())
    fobj.write("CPU Usage %s %% \n" %psutil.cpu_percent())
    fobj.write(Border + "\n")
    # RAM information
    memory = psutil.virtual_memory()
    fobj.write("RAM usage %s %%\n" %memory.percent)
    fobj.write("Total RAM available %s \n" %memory.total)
    fobj.write(Border + "\n")

    # Network usage information
    netObj = psutil.net_io_counters()
    fobj.write("Network usage report")
    fobj.write("Sent : %.2f MB \n" %(netObj.bytes_sent/(1024*1024)))
    fobj.write("Received : %.2f MB \n" %(netObj.bytes_recv/(1024*1024)))
    fobj.write(Border + "\n")
    
    # Process log information
    Data = processScan()
    for info in Data:
        fobj.write(f"{info} \n")
        fobj.write(Border + "\n")

    fobj.write("\n"*10)

    fobj.write("---------------------End of log file-------------------- \n")
    fobj.close()
    

def main():
    Border = ("-"*50)
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
        # print("Cpu usage :", psutil.cpu_percent() )
        print("Schedular started successfully")
        print("Press Ctrl + c to abort")
        schedule.every(int(sys.argv[1])).minutes.do(platformSurvellience, sys.argv[2])
        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguements")
        print("Unable to proceed as arguements are not matching")
        print("Please use --u or --h for more information.")

    print(Border)
    print("----Thank you for using out automation System----")
    print(Border)

if __name__ == "__main__":
    main()