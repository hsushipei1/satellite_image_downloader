__author__ = 'hsushipei'
from datetime import datetime, timedelta
from urllib import urlretrieve
import sys, os, shutil


def cmd_argument():
    # Deal with command line argument
    # output: "input_img_cat": human readable img category insert by user
    #         "starttime": start time
    #         "endtime": end time
    #         "save_desti": directory to save images

    arg_numbers = len(sys.argv)
    input_img_cat = sys.argv[1]
    starttime = sys.argv[2]
    endtime = sys.argv[3]
    dirName_to_save = sys.argv[4]

    return input_img_cat, starttime, endtime, dirName_to_save

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
        return "Global-Full color","s0p"
    elif (human_readable_cat == "GV"):
        return "Global-Visible","sco"
    elif (human_readable_cat == "GI"):
        return "Global-Enhanced IR","s0q"
    elif (human_readable_cat == "GB"):
        return "Global-Black and white","s0o"
    elif (human_readable_cat == "EF"):
        return "East Asia-Full color","s1p"
    elif (human_readable_cat == "EV"):
        return "East Asia-Visible","sao"
    elif (human_readable_cat == "EI"):
        return "East Asia-Enhanced IR","s1q"
    elif (human_readable_cat == "EB"):
        return "East Asia-Black and white","s1o"
    elif (human_readable_cat == "TF"):
        return "Taiwan-Full color","s3p"
    elif (human_readable_cat == "TV"):
        return "Taiwan-Visible","sbo"
    elif (human_readable_cat == "TI"):
        return "Taiwan-Enhanced IR","s3q"
    elif (human_readable_cat == "TB"):
        return "Taiwan-Black and white","s3o"
    elif (human_readable_cat == "HF"):
        return "High resolution-Full color","HS1P"
    elif (human_readable_cat == "HV"):
        return "High resolution-Visible","HSAO"
    elif (human_readable_cat == "HI"):
        return "High resolution-Enhanced IR","HS1Q"
    elif (human_readable_cat == "HB"):
        return "High resolution-Black and white","HS1O"

# check for arguments
if (len(sys.argv) != 5):
    print("Argument is incomplete")
    quit()

# create directory and cd into it to save downloaded images
dirName = cmd_argument()[3]
dirAbsPath = "/".join(((os.getcwd()),dirName))  # get absolute path to the directory
os.mkdir(dirAbsPath)  # create the directory
os.chdir(dirAbsPath)  # cd into it

# obtain start and end time from cmd line argument
start_time = cmd_argument()[1]
end_time = cmd_argument()[2]
img_cat_for_url = img_category(cmd_argument()[0])[1]
humanRd_img_cat_for_filename = img_category(cmd_argument()[0])[0]

# convert raw time format that user input to datetime object
start_time_dateT = convert_to_datetime(start_time)
end_time_dateT = convert_to_datetime(end_time)

n=0
each_img_time = start_time_dateT
while (each_img_time != end_time_dateT):
    # increase start time by increment of 10 min
    time_increment = n * 10
    each_img_time = start_time_dateT + timedelta(minutes = time_increment)

    # convert datetime object to ISO 8601 time representation(string)
    time_for_filename = each_img_time.strftime("%Y-%m-%d-%H-%M")

    # retrieve img from CWB
    img_url = "http://www.cwb.gov.tw/V7/observe/satellite/Data/%s/%s-%s.jpg" %(img_cat_for_url,\
                                                                               img_cat_for_url,\
                                                                               time_for_filename)
    img_filename ="%s_%s.jpg" %(humanRd_img_cat_for_filename, time_for_filename)
    urlretrieve(img_url, img_filename)

    print("Image %s downloaded.") %(img_filename)

    n = n + 1

