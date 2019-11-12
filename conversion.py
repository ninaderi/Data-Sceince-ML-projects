# import os # this is to make sure that the passed in file path is a file that exists on the disk.
import re

#
#     while len(f_contents) > 0:
#         print(f_contents, end='')
#         f_contents = f.read(size_to_read)

with open('OCSG-04903_1 (177264002400).LAS', 'r') as rf:
    with open('OCSG-04903_1 (177264002400).strat', 'w') as wf:
        f_contents = rf.readlines()
        # for line in range(5):
        #     print(f_contents[line])

        api = str([int(i) for i in f_contents[13].split() if i.isdigit()][0])
        well_name = re.search('LL.(.+?):WE', f_contents[12]).group(1)

        wf.write("~1D SEQUENCE STRAT\n#\n")
        wf.write("VERSION: 2.3\n")
        wf.write("FILE NAME: \n")
        wf.write("WELL FILE: " + well_name.strip().replace(" 1", "_1_") + "(" + api + ")" + "\n")
        #wf.write("API: " + (re.search('I .(.+?):UN', f_contents[13]).group(1)).strip() + "\n") # this method is the fastest
        # wf.write("API: " + f_contents[13][5:].split()[0] + "\n")
        wf.write("API: " + api + "\n") # this method works on any file
        wf.write("WELL NAME: " + well_name.strip().replace(" 1", "_1") + "\n")
        wf.write("MEASUREMENT: TVD\n#\n\n")
        wf.write("~DATA\t1\n")
        wf.write("VSH\n")
        wf.write("~VSH\n")
        wf.write("~A\tMD\tVSH\tTVD\n")
        wf.write("1886.0\t0.1962323\t1805.9551\n")
        wf.write("1886.5\t0.2206677\t1806.455\n")
        wf.write("1887.0\t0.226923\t1806.955\n")
            # wf.write(f_contents[line])

        data_flag = False
        for i in range(len(f_contents)):
            if f_contents[i].startswith("~A"):
                data_flag = True
            if data_flag == False:
                continue
            line = f_contents[i].split()
            md = line[0]
            tvd = line[1]
            vsh = line[25]
            print(f_contents[i])
            print("md = " + md + "; tvd = " + tvd + "; vsh =", vsh)

    # f_contents = [line.strip('\n') for line in f_contents]
    # count = 0
    # for line in f:
    #     if line =
    # while len(f_contents) > 0:
    #     print(f_contents, end='')
    #     f_contents = f.readlines(size_to_read)
    # print(f_contents, end='')
    # count = 0
    # while len(f_contents) > 0:
    #
    #     if count > 10:
    #         break
    #     print(f_contents[count])
    #     count = count + 1
    #     f_contents = f.readline()