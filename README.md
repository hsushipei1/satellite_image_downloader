# Satellite Image Downloader(SID)
SID also means Still In Development XP

## Introduction
SID downloads satellite images from [CWB](http://www.cwb.gov.tw/V7/observe/satellite/Sat_T.htm). The images are categorized into different region and bands and the time resolution is 10 minutes. With SID, you can download multiple images at a time.

## Pre-requisite
[Python 2.x](https://www.python.org)

## Download
```
$ git clone https://github.com/hsushipei1/satellite_image_downloader.git
```

## How to run
Launch terminal(or cmd for windows users) and then type
```
$ python satel_img_downloader.py [ImageCategory] [StartTime] [EndTime] [DirectoryName]
```
`ImageCategory`: letter combination of REGION and COLOR. REGION: Global->G; East Asia->E; Taiwan->T; High resolution->H. COLOR: COLOR: Full color->F; Visible->V; Enhanced IR->I; Black white->B. For example: GV
`StartTime & EndTime`: Start time and end time of images in a row. The format is yyyymmddHHMM where yyyy is year(like 2016); mm is month; dd is day; HH is hour; MM us minute. For example: 201602041250
`DirectoryName`: Create a new directory and downloaded image will be saved into it.
