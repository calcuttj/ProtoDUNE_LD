# -*- coding: utf-8 -*-
"""
File Name: Main.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 1/13/2018 3:05:03 PM
Last modified: Mon Apr  9 16:09:52 2018
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl

import os
import sys
import copy
from datetime import datetime
import numpy as np
import time
import pickle
from timeit import default_timer as timer

###############################################################################
from ce_runs import CE_RUNS
from set_path import set_path
ceruns = CE_RUNS()

start = timer()
ceruns.APA = sys.argv[1]
test_runs = int(sys.argv[2],16)
RTD_flg = (sys.argv[3] == "True")
os_cs = sys.argv[4]

ceruns.wib_version_id = 0x116
ceruns.femb_ver_id = 0x323
rawpath = set_path(os=os_cs)

if (ceruns.APA == "APA40"):
    print ceruns.APA
    ceruns.path = rawpath 
    ceruns.wib_ips = [ "192.168.121.1", "192.168.121.2"  ]
    ceruns.wib_pwr_femb = [[1,1,1,1],[1,1,1,1]]
    ceruns.femb_mask    = [[0,0,0,0],[0,0,0,0] ]
    ceruns.tmp_wib_ips = ["192.168.121.1"] 
    ceruns.jumbo_flag = True
elif ( (ceruns.APA == "Coldbox") or \
       (ceruns.APA == "APA1") or  (ceruns.APA == "APA2")  or  (ceruns.APA == "APA3")  or  \
       (ceruns.APA == "APA4") or  (ceruns.APA == "APA5")  or  (ceruns.APA == "APA6") ): 
    print ceruns.APA
    if (ceruns.APA == "Coldbox"): 
        ceruns.wib_ips = ["10.73.137.20", "10.73.137.21", "10.73.137.22", "10.73.137.23", "10.73.137.24"]  
        ceruns.path = rawpath + "/Coldbox/" 
    elif (ceruns.APA == "APA1"): 
        ceruns.wib_ips = ["10.73.137.26", "10.73.137.27", "10.73.137.28", "10.73.137.29", "10.73.137.30"]  
        ceruns.path = rawpath + "/APA1/" 
    elif (ceruns.APA == "APA2"): 
        ceruns.wib_ips = ["10.73.137.31", "10.73.137.32", "10.73.137.33", "10.73.137.34", "10.73.137.35"]  
        ceruns.path = rawpath + "/APA2/" 
    elif (ceruns.APA == "APA3"): 
        ceruns.wib_ips = ["10.73.137.36", "10.73.137.37", "10.73.137.38", "10.73.137.39", "10.73.137.40"]  
        ceruns.path = rawpath + "/APA3/" 
    elif (ceruns.APA == "APA4"): 
        ceruns.wib_ips = ["10.73.137.41", "10.73.137.42", "10.73.137.43", "10.73.137.44", "10.73.137.45"]  
        ceruns.path = rawpath + "/APA4/" 
    elif (ceruns.APA == "APA5"): 
        ceruns.wib_ips = ["10.73.137.46", "10.73.137.47", "10.73.137.48", "10.73.137.55", "10.73.137.49"]  
        ceruns.path = rawpath + "/APA5/" 
    elif (ceruns.APA == "APA6"): 
        ceruns.wib_ips = ["10.73.137.50", "10.73.137.51", "10.73.137.52", "10.73.137.53", "10.73.137.54"]  
        ceruns.path = rawpath + "/APA6/" 

    ceruns.wib_pwr_femb = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    ceruns.femb_mask    = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    ceruns.tmp_wib_ips = ["10.73.137.24"] 
    ceruns.jumbo_flag = False
elif (ceruns.APA == "CHKOUT"): 
    print ceruns.APA
    ceruns.path = rawpath + "/CHKOUT/" 
    ceruns.wib_ips = [ "192.168.121.1" ]
    ceruns.wib_pwr_femb = [[1,1,1,1]]
    ceruns.femb_mask    = [[0,0,0,0]]
    ceruns.jumbo_flag = True

elif (ceruns.APA == "CRYO_CHKOUT"): 
    print ceruns.APA
    ceruns.path = rawpath + "/CHKOUT/" 
    ceruns.wib_ips = [  "10.73.137.20", "10.73.137.21", "10.73.137.22", "10.73.137.23", "10.73.137.24", \
                        "10.73.137.26", "10.73.137.27", "10.73.137.28", "10.73.137.29", "10.73.137.30", \
                        "10.73.137.31", "10.73.137.32", "10.73.137.33", "10.73.137.34", "10.73.137.35", \
                        "10.73.137.36", "10.73.137.37", "10.73.137.38", "10.73.137.39", "10.73.137.40", \
                        "10.73.137.41", "10.73.137.42", "10.73.137.43", "10.73.137.44", "10.73.137.45", \
                        "10.73.137.46", "10.73.137.47", "10.73.137.48", "10.73.137.55", "10.73.137.49", \
                        "10.73.137.50", "10.73.137.51", "10.73.137.52", "10.73.137.53", "10.73.137.54", \
                        "192.168.121.1"
                     ]
    ceruns.wib_pwr_femb = [ [1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1], 
                            [1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1], 
                            [1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1], 
                            [1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1], 
                            [1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1], 
                            [1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1], 
                            [1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1], 
                            [1,1,1,1],                                         ]
    ceruns.femb_mask    = [ [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0], 
                            [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0], 
                            [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0], 
                            [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0], 
                            [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0], 
                            [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0], 
                            [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0], 
                            [0,0,0,0],                                         ]
    ceruns.jumbo_flag = True


ceruns.jumbo_flag_set( )
if (os.path.exists(ceruns.path)):
    pass
else:
    try: 
        os.makedirs(ceruns.path)
    except OSError:
        print "Can't create a folder, exit"
        sys.exit()

logfile = ceruns.path +  ceruns.APA + "readme.log"
print "WIEC self check"
print "time cost = %.3f seconds"%(timer()-start)
ceruns.WIB_self_chk()

if (test_runs == 0x0 ):
    print "Power FEMBs ON"
    print "time cost = %.3f seconds"%(timer()-start)
    ceruns.FEMBs_PWR_SW(SW = "ON")
    ceruns.apa_cebox_chk() 
    with open(logfile, "a+") as f:
        f.write( "Begin\n") 
        f.write( "Turn PS on\n" ) 
        f.write (ceruns.runpath + "\n" )
        f.write (ceruns.runtime + "\n" )
        f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )

        wib_wrerr_cnt = ceruns.femb_meas.femb_config.femb.wib_wrerr_cnt
        wib_wr_cnt = ceruns.femb_meas.femb_config.femb.wib_wr_cnt
        femb_wrerr_cnt = ceruns.femb_meas.femb_config.femb.femb_wrerr_cnt
        femb_wr_cnt = ceruns.femb_meas.femb_config.femb.femb_wr_cnt
        udp_timeout_cnt = ceruns.femb_meas.femb_config.femb.udp_timeout_cnt
        udp_hstimeout_cnt = ceruns.femb_meas.femb_config.femb.udp_hstimeout_cnt
        f.write ("There are %d times WIB UDP Registers Write\n"%wib_wr_cnt )
        f.write ("There are %d times WIB UDP Registers Write Error\n"%wib_wrerr_cnt )
        f.write ("There are %d times FEMB UDP Registers Write\n"%femb_wr_cnt )
        f.write ("There are %d times FEMB UDP Registers Write Error\n"%femb_wrerr_cnt )
        f.write ("There are %d times UDP timeouts\n"%udp_timeout_cnt )
        f.write ("There are %d times UDP High Speed links timeouts\n"%udp_hstimeout_cnt )
        udp_err_np = ceruns.udp_err_np
        for oneerr in udp_err_np:
            if (oneerr[4] - oneerr[3] != 0) : 
                f.write ("RUNcode(%s)WIB%d(%s)FEMB%d: UDP Reg Write Error count = (%d-%d) = %d\n" \
                        %(oneerr[5], oneerr[1], oneerr[0], oneerr[2], oneerr[4], oneerr[3], oneerr[3] - oneerr[4] ))
        femb_wrerr_log = ceruns.femb_meas.femb_config.femb.femb_wrerr_log
        if len(femb_wrerr_log) != 0 :
            f.write ("Write ERROR happens at FEMB%d, Addr=%x, Value=%x"%(femb_wrerr_log[0], femb_wrerr_log[1],femb_wrerr_log[2]) )
            for logn in range(len(femb_wrerr_log)-1):
                log0 = femb_wrerr_log[logn]
                log1 = femb_wrerr_log[logn+1]
                if log0 != log1 :
                    f.write ("Write ERROR happens at FEMB%d, Addr=%x, Value=%x"%(log1[0], log1[1],log1[2]) )
        f.write( "End\n") 
        f.write( "\n") 

print "FEMBs self-check"
mask_femb = ceruns.FEMBs_Self_CHK()
with open(logfile, "a+") as f:
    f.write( "Begin\n") 
    f.write( "Broken FEMBs are masked\n" ) 
    f.write (ceruns.runpath + "\n" )
    f.write (ceruns.runtime + "\n" )
    f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )
    for onemaskfemb in mask_femb:
        f.write (onemaskfemb + "\n" )
    f.write( "End\n") 
    f.write( "\n") 

if (test_runs&0x7F != 0x0 ):
    if (RTD_flg == True):
        print "Please write a sentence to describe the test purpose: "
        test_note = raw_input("Please input: ")
    else:
        test_note = "Continuate test..."
    rtd_temp = " "
    rundate =  datetime.now().strftime('%m_%d_%Y')
    runtime =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(logfile, "a+") as f:
        f.write( "Begin\n") 
        f.write(runtime + "\n") 
        f.write(ceruns.APA + "\n") 
#        f.write(ceruns.env + "\n") 
        f.write("Test Code = 0X" + format(test_runs,"02X")+ "\n")  
        f.write(test_note + "\n") 
        f.write("RTDs(TT0206 to TT0200): %s"%rtd_temp + "\n")  
        f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )

    print "FEMB ADC offset calibration"

    print "time cost = %.3f seconds"%(timer()-start)
    apa_oft_info = ceruns.oft_run( test_runs&0x7F ) 
#    if (False):
#        oft_file = "D:/Hibay_V3/Rawdata/Rawdata_01_13_2018/run01oft/APA_ADC_OFT_01132018_155658.bin"
#        with open (oft_file, 'rb') as fp:
#            apa_oft_info = pickle.load(fp)

    with open(logfile, "a+") as f:
        f.write( "FEMB ADC offset calibration\n" ) 
        f.write (ceruns.runpath + "\n" )
        f.write (ceruns.runtime + "\n" )
        f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )

if (test_runs&0x10 != 0x0 ):
    print "Quick Checkout Test"
    print "time cost = %.3f seconds"%(timer()-start)
    ceruns.qc_run(apa_oft_info, sgs=[3], tps =[0,1,2,3], val = 100) 
    with open(logfile, "a+") as f:
        f.write( "%2X: Quick Checkout Test\n" %(test_runs&0x10) ) 
        f.write (ceruns.runpath + "\n" )
        f.write (ceruns.runtime + "\n" )
        f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )

if (test_runs&0x01 != 0x0 ):
    print "Noise Measurement Test"
    print "time cost = %.3f seconds"%(timer()-start)
    ceruns.rms_run(apa_oft_info, sgs = [1,3], tps =[0,1,2,3], val=1600) 
    with open(logfile, "a+") as f:
        f.write( "%2X: Noise Measurement Test\n" %(test_runs&0x01) ) 
        f.write (ceruns.runpath + "\n" )
        f.write (ceruns.runtime + "\n" )
        f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )

if (test_runs&0x02 != 0x0 ):
    print "FPGA DAC Calibration Test"
    print "time cost = %.3f seconds"%(timer()-start)
    ceruns.fpgadac_run(apa_oft_info, sgs = [1,3], tps =[0,1,2,3], val=100)
    with open(logfile, "a+") as f:
        f.write( "%2X: FPGA DAC Calibration Test\n" %(test_runs&0x02) ) 
        f.write (ceruns.runpath + "\n" )
        f.write (ceruns.runtime + "\n" )
        f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )

if (test_runs&0x04 != 0x0 ):
    print "ASIC DAC Calibration Test"
    print "time cost = %.3f seconds"%(timer()-start)
    ceruns.asicdac_run(apa_oft_info, sgs = [1,3], tps =[0,1,2,3], val=100)
    with open(logfile, "a+") as f:
        f.write( "%2X: ASIC DAC Calibration Test\n" %(test_runs&0x04) ) 
        f.write (ceruns.runpath + "\n" )
        f.write (ceruns.runtime + "\n" )
        f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )

if (test_runs&0x08 != 0x0 ):
    print "Brombreg Mode Noise Measurement Test"
    print "time cost = %.3f seconds"%(timer()-start)
    #ceruns.brombreg_run(apa_oft_info, sgs = [1,3], tps =[0,1,2,3], cycle=5) 
    ceruns.brombreg_run(apa_oft_info, sgs = [3], tps =[0,1,2,3], cycle=150) 
    with open(logfile, "a+") as f:
        f.write( "%2X: Brombreg Mode Noise Measurement Test\n" %(test_runs&0x08) ) 
        f.write (ceruns.runpath + "\n" )
        f.write (ceruns.runtime + "\n" )
        f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )

if (test_runs&0x20 != 0x0 ):
    print "Temperature Monitoring"
    print "time cost = %.3f seconds"%(timer()-start)

    if (RTD_flg == "pulse"):
        temp_or_pluse = "pulse"
    else:
        temp_or_pluse = "temp"
    ceruns.monitor_run(temp_or_pluse = temp_or_pluse) #"pulse"
    with open(logfile, "a+") as f:
        f.write( "%2X: Temperature Monitoring\n" %(test_runs&0x20) ) 
        f.write (ceruns.runpath + "\n" )
        f.write (ceruns.runtime + "\n" )
        f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )

if (test_runs&0x40 != 0x0 ):
    if (ceruns.APA == "CHKOUT"): 
        print "Average Checkout"
        print "time cost = %.3f seconds"%(timer()-start)
        ceruns.avg_run(val = 1600, avg_cycle=300)

    with open(logfile, "a+") as f:
        f.write( "%2X: Average Checkout\n" %(test_runs&0x40) ) 
        f.write (ceruns.runpath + "\n" )
        f.write (ceruns.runtime + "\n" )
        f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )

if (test_runs&0x80 != 0x0 ):
    print "Turn FEMBs OFF"
    print "time cost = %.3f seconds"%(timer()-start)
    ceruns.FEMBs_PWR_SW(SW = "OFF")
    with open(logfile, "a+") as f:
        f.write( "Begin\n") 
        for onelog in ceruns.linkcurs:
            f.write( onelog + "\n") 
        f.write (ceruns.runpath + "\n" )
        f.write (ceruns.runtime + "\n" )
        f.write ("Alive FEMBs: " + str(ceruns.alive_fembs) + "\n" )
        f.write( "PS is OFF\n" ) 
        f.write( "End\n") 
        f.write( "\n") 

if (test_runs&0x7F != 0x0 ):
    with open(logfile, "a+") as f:
        wib_wrerr_cnt = ceruns.femb_meas.femb_config.femb.wib_wrerr_cnt
        wib_wr_cnt = ceruns.femb_meas.femb_config.femb.wib_wr_cnt
        femb_wrerr_cnt = ceruns.femb_meas.femb_config.femb.femb_wrerr_cnt
        femb_wr_cnt = ceruns.femb_meas.femb_config.femb.femb_wr_cnt
        udp_timeout_cnt = ceruns.femb_meas.femb_config.femb.udp_timeout_cnt
        udp_hstimeout_cnt = ceruns.femb_meas.femb_config.femb.udp_hstimeout_cnt
        f.write ("There are %d times WIB UDP Registers Write\n"%wib_wr_cnt )
        f.write ("There are %d times WIB UDP Registers Write Error\n"%wib_wrerr_cnt )
        f.write ("There are %d times FEMB UDP Registers Write\n"%femb_wr_cnt )
        f.write ("There are %d times FEMB UDP Registers Write Error\n"%femb_wrerr_cnt )
        f.write ("There are %d times UDP timeouts\n"%udp_timeout_cnt )
        f.write ("There are %d times UDP High Speed links timeouts\n"%udp_hstimeout_cnt )
        udp_err_np = ceruns.udp_err_np
        for oneerr in udp_err_np:
            if (oneerr[4] - oneerr[3] != 0) : 
                f.write ("RUNcode(%s)WIB%d(%s)FEMB%d: UDP Reg Write Error count = (%d-%d) = %d\n" \
                        %(oneerr[5], oneerr[1], oneerr[0], oneerr[2], oneerr[4], oneerr[3], oneerr[3] - oneerr[4] ))

        femb_wrerr_log = ceruns.femb_meas.femb_config.femb.femb_wrerr_log
        if len(femb_wrerr_log) != 0 :
            f.write ("Write ERROR happens at FEMB%d, Addr=%x, Value=%x\n"%(femb_wrerr_log[0][0], femb_wrerr_log[0][1],femb_wrerr_log[0][2]) )
            for logn in range(len(femb_wrerr_log)-1):
                log0 = femb_wrerr_log[logn]
                log1 = femb_wrerr_log[logn+1]
                if log0 != log1 :
                    f.write ("Write ERROR happens at FEMB%d, Addr=%x, Value=%x\n"%(log1[0], log1[1],log1[2]) )
        f.write( "End\n") 
        f.write( "\n") 

print "Well Done"

