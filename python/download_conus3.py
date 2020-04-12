#!/usr/bin/env python3
import os
import shlex
import subprocess
import numpy
from datetime import datetime, timedelta
downloadbool = True
print(str(datetime.now()))


class Dldate:
    def __init__(self, subtract, julday, year):
        self.subtract = subtract
        self.julday = julday
        self.year = str(year)
        self.yearjul = str(year)+julday
        self.target = 'none'


minusarray = [2, 9, 16, 23]
python_dir = os.path.dirname(os.path.realpath(__file__))
staticpath = "/static/"
tilespath = "/var/www/html/recent_phenology/public/tiles4"
previoussuccess = -7
save_postgres = False

if os.path.isdir(tilespath):
    existingarray = os.listdir(os.path.join(tilespath))
    if len(existingarray) > 0:
        existingarray.sort()
        mostrecentdate = existingarray[-1]
    else:
        mostrecentdate = '0000000'
else:
    mostrecentdate = '0000000'
    os.system("mkdir -p {}".format(tilespath))

# DOWNLOAD
# credfile= open((os.path.join(python_dir,"cred")), "r")
# credcontents=credfile.readlines()
# credfile.close()
username = os.environ['USGSUSERNAME']
password = os.environ['USGSPASSWORD']
pgpassword = os.environ['POSTGRES_PASSWORD']
datearray = []
for subtract in minusarray:
    mytargetdate = datetime.today() - timedelta(days=subtract)
    julday = str((mytargetdate.toordinal() - 125) % 365 + 1)
    if len(julday) == 1:
        julday = "0"+julday
    if len(julday) == 2:
        julday = "0"+julday
    datearray.append(Dldate(subtract, julday, mytargetdate.year))

if downloadbool:
    if os.path.isdir(staticpath):
        os.system("rm -rf {}".format(staticpath))
        print('deleted static')
    os.system("mkdir -p {}".format(staticpath))

    datearray2 = []
    dlfailed = False

    for index, mydate in enumerate(datearray):
        totaltries = 0
        trial = 0
        success = False

        while (success == False and dlfailed == False):
            if totaltries > 100 or (index == 0 and int(mydate.yearjul[-7:]) < int(mostrecentdate[-7:])):
                dlfailed = True
                break
            print(str(datetime.now()))
            indexfile = os.path.join(
                staticpath, '{0}.html'.format(mydate.yearjul))
            zipdestination = os.path.join(staticpath, mydate.yearjul)
            url1 = 'https://dds.cr.usgs.gov/highvolume/emodis_v6/CONUS6/expedited/AQUA/{0}/comp_{1}/'.format(
                mydate.year, mydate.julday)
            htmldl = ['/usr/bin/wget', '-O', indexfile, '--no-proxy', '-t', '3', '-o', os.path.join(
                staticpath, 'dlhtml.txt'), '--no-check-certificate', '-L', '--user='+username, '--password='+password, '--no-parent', '-A', 'US_eMAE_NDVI.'+mydate.year+'.*.QKM.*.zip', url1]
            print(htmldl)
            subprocess.call(htmldl)

            openindexfile = open((indexfile), "r")
            textcontents = openindexfile.readlines()
            openindexfile.close()
            if len(textcontents) > 2:
                print("date {0} set to true".format(mydate.yearjul))
            else:
                print("date {0} set to false".format(mydate.yearjul))

            for item in textcontents:
                if "NDVI" in item and "QKM" in item and not ".sum" in item:
                    endcarrot = item.index(">")
                    startcarrot = item.index("<", 1)
                    target = item[endcarrot+1:startcarrot]
                    print("target is ", target)
                    mydate.target = target
            url2 = "https://dds.cr.usgs.gov/highvolume/emodis_v6/CONUS6/expedited/AQUA/{0}/comp_{1}/{2}".format(
                mydate.year, mydate.julday, target)
            dllist = ['/usr/bin/wget', '--no-proxy', '-t', '3', '-o', os.path.join(
                staticpath, 'dldata.txt'), '-O', zipdestination+'.zip', '--no-check-certificate', '-L', '--user='+username, '--password='+password, url2]
            print(dllist)
            subprocess.call(dllist)
            print("startingunzip")
            unzipCommand = "/usr/bin/unzip -o {0}.zip -d {0}".format(
                zipdestination)
            print(unzipCommand)
            subprocess.call(shlex.split(unzipCommand))
            if (os.path.isdir(zipdestination)):
                datearray2.append(
                    Dldate(mydate.subtract, mydate.julday, mydate.year))
                previoussuccess = mydate.subtract
                break
            else:
                print(trial)
                trial = trial+1
                if trial > 2:
                    trial = 0
                    newsubtract = mydate.subtract+1
                    if ((newsubtract-previoussuccess) < 7):
                        newsubtract = previoussuccess+7
                    newmydate = datetime.today() - timedelta(days=newsubtract)
                    newjulday = str((newmydate.toordinal() - 125) % 365 + 1)
                    if len(newjulday) == 1:
                        newjulday = "0"+newjulday
                    if len(newjulday) == 2:
                        newjulday = "0"+newjulday
                    print("real"+newjulday)
                    mydate = Dldate(newsubtract, newjulday, newmydate.year)

# PROCESS
targetdatearray = datearray
if downloadbool:
    targetdatearray = datearray2

if len(targetdatearray) == len(minusarray):
    if os.path.isdir(tilespath):
        os.system("rm -rf {}".format(tilespath))
        print('deleted tilespath')
        os.system("mkdir -p {}".format(tilespath))

    for (ind, mydate) in enumerate(targetdatearray):
        os.system("rm -rf {}.zip".format(os.path.join(staticpath, mydate.yearjul)))

        for item1 in os.listdir(os.path.join(staticpath, mydate.yearjul)):
            if 'QKM.VI_NDVI' in item1 and item1[-3:] == 'tif':
                ndvi = os.path.join(staticpath, mydate.yearjul, item1)
            if 'QKM.VI_QUAL' in item1 and item1[-3:] == 'tif':
                qual = os.path.join(staticpath, mydate.yearjul, item1)

        ndviwarp = os.path.join(staticpath, "ndviwarp")
        qualwarp = os.path.join(staticpath, "qualwarp")
        if ind == 0:
            ndviwarp = os.path.join(staticpath, "firstndviwarp")
            qualwarp = os.path.join(staticpath, "firstqualwarp")

        subprocess.call(['gdalwarp', "-s_srs", "EPSG:2163", "-t_srs",
                         "EPSG:4326", "-of", "VRT", "-overwrite", ndvi, ndviwarp])
        subprocess.call(['gdalwarp', "-s_srs", "EPSG:2163", "-t_srs",
                         "EPSG:4326", "-of", "VRT", "-overwrite", qual, qualwarp])

        # os.system("rm -rf {}".format(os.path.join(staticpath,mydate.yearjul)))

        if ind == 0:
            firstdate = mydate.yearjul
            firstndviwarp = ndviwarp
            firstqualwarp = qualwarp
            subprocess.call(["python", os.path.join(python_dir, 'gdal_calc.py'), "--type=Int32", "-A", ndviwarp,
                             "-B", qualwarp, "--outfile=gdal_calc.tif", "--calc", "-13000+13000*(B<1)+A*(B<1)", "--overwrite"])
            savetodb = ("raster2pgsql -s 4326 -t auto -I -C -M -F {0} public.{1} | PGPASSWORD={2} psql -U root -d ndvidb2").format(
                "gdal_calc.tif", mydate.yearjul, pgpassword)
            print(savetodb)
            try:
                if save_postgres:
                    suboutput = subprocess.check_output(savetodb, shell=True)
            except:
                pass

        else:
            outfolder = os.path.join(tilespath, str(
                firstdate)+"-"+str(mydate.yearjul))

            colorsfile = os.path.join(python_dir, "colors.txt")
            postqual = os.path.join(staticpath, mydate.yearjul+"postqual")

            withcolor = os.path.join(staticpath, mydate.yearjul+"withcolor")

            subprocess.call(["python", os.path.join(python_dir, 'gdal_calc.py'), "--type=Int32", "-A", firstndviwarp, "-B", ndviwarp, "-C", firstqualwarp,
                             "-D", qualwarp, "--outfile={0}".format(postqual), "--calc", "-13000+13000*(C<1)*(D<1)+A*(C<1)*(D<1)-B*(C<1)*(D<1)", "--overwrite"])
            subprocess.call(["python", os.path.join(python_dir, 'gdal_calc.py'), "--type=Int32", "-A", firstndviwarp,
                             "-B", postqual, "--outfile=gdal_calc.tif", "--calc", "-13005+13005*(A>-2000)+B*(A>-2000)", "--overwrite"])
            os.system("rm {}".format(postqual))

            subprocess.call(['gdaldem', "color-relief", "-of",
                             "VRT", "gdal_calc.tif", colorsfile, withcolor])

            subprocess.call(["python", os.path.join(
                python_dir, 'gdal2tiles.py'), "-z", "1-11", withcolor, outfolder])
            os.system("rm {}".format(withcolor))

print(str(datetime.now()))
if os.path.isdir(staticpath):
    os.system("rm -rf {}".format(staticpath))
    print('deleted static')
os.system("mkdir -p {}".format(staticpath))
