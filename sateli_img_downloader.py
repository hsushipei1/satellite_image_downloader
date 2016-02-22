__author__ = 'hsushipei'
from datetime import datetime, timedelta
from urllib import urlretrieve
import sys

"""
def cmd_argument():
    # Show usage of this program if user insert help
    if ( (sys.argv[1] == "--help") or (sys.argv[1] == "-h") ):
        print("Command line arguments: [imageCategory] [startTime] [endTime]")
"""

def convert_to_datetime(complete_time):
    # Convert raw time format yyyymmddHHMM to datetime object.
    # input: yyyymmddHHMM
    # output: datetime object with year, month, day, hour and minute

    yyyy = str(complete_time)[0:4]
    mm = str(complete_time)[4:6]
    dd = str(complete_time)[6:8]
    HH = str(complete_time)[8:10]
    MM = str(complete_time)[10:12]

    return datetime(int(yyyy),int(mm),int(dd),int(HH),int(MM))

def img_category( human_readable_cat ):
    if (human_readable_cat == "GF"):
        return "Global-Full color",s0p
    elif (human_readable_cat == "GV"):
        return "Global-Visible",sco
    elif (human_readable_cat == "GI"):
        return "Global-Enhanced IR",s0q
    elif (human_readable_cat == "GB"):
        return "Global-Black and white",s0o
    elif (human_readable_cat == "EF"):
        return "East Asia-Full color",s1p
    elif (human_readable_cat == "EV"):
        return "East Asia-Visible",sao
    elif (human_readable_cat == "EI"):
        return "East Asia-Enhanced IR",s1q
    elif (human_readable_cat == "EB"):
        return "East Asia-Black and white",s1o
    elif (human_readable_cat == "TF"):
        return "Taiwan-Full color",s3p
    elif (human_readable_cat == "TV"):
        return "Taiwan-Visible",sbo
    elif (human_readable_cat == "TI"):
        return "Taiwan-Enhanced IR",s3q
    elif (human_readable_cat == "TB"):
        return "Taiwan-Black and white",s3o
    elif (human_readable_cat == "HF"):
        return "High resolution-Full color",HS1P
    elif (human_readable_cat == "HV"):
        return "High resolution-Visible",HSAO
    elif (human_readable_cat == "HI"):
        return "High resolution-Enhanced IR",HS1Q
    elif (human_readable_cat == "HB"):
        return "High resolution-Black and white",HS1Oi


start_time = 201602041250
end_time = 201602051250

# convert raw time formate that user input to datetime object
start_time_dateT = convert_to_datetime(start_time)
end_time_dateT = convert_to_datetime(end_time)

n=0
each_img_time = start_time_dateT
while (each_img_time != end_time_dateT):
    # increase start time by increment of 10 min
    time_increment = n * 10
    each_img_time = start_time_dateT + timedelta(minutes = time_increment)

    # convert datetime object to struct_time
    each_img_time_tuple = each_img_time.timetuple()

    # retrieve img from CWB

    urlretrieve("http://www.cwb.gov.tw/V7/observe/satellite/Data/s1q/s1q-2016-02-22-13-20.jpg")


    print "%d %d %d %d %d" %(each_img_time_tuple[0], each_img_time_tuple[1], \
                            each_img_time_tuple[2], each_img_time_tuple[3], \
                            each_img_time_tuple[4])

    n = n + 1