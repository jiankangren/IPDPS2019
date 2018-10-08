import sys
import re
if len(sys.argv) < 1 :
    print 'usage: python %s <file' % sys.argv[0]
    sys.exit(0)

def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split() for line in fr.readlines()]
    print shape(stringArr)
   # print stringArr
    datArr = [map(float, line) for line in stringArr]
    return mat(datArr)



fname= sys.argv[1]
fp1 = open(sys.argv[1]+"_1.dat", 'r')
fp2 = open(sys.argv[1]+"_2.dat", 'r')
fp3 = open(sys.argv[1]+"_3.dat", 'r')
fp4 = open(sys.argv[1]+"_4.dat", 'r')
fp5 = open(sys.argv[1]+"_5.dat", 'r')
fp6 = open(sys.argv[1]+"_6.dat", 'r')
fp7 = open(sys.argv[1]+"_7.dat", 'r')
fp8 = open(sys.argv[1]+"_8.dat", 'r')
#fp9 = open(sys.argv[1]+"_9.dat", 'r')
#fp10 = open(sys.argv[1]+"_10.dat", 'r')
#fp11 = open(sys.argv[1]+"_11.dat", 'r')
#fp12 = open(sys.argv[1]+"_12.dat", 'r')
#fp13 = open(sys.argv[1]+"_13.dat", 'r')
#fp14 = open(sys.argv[1]+"_14.dat", 'r')
#fp15 = open(sys.argv[1]+"_15.dat", 'r')
#fp16 = open(sys.argv[1]+"_16.dat", 'r')
#fp17 = open(sys.argv[1]+"_17.dat", 'r')
#fp18 = open(sys.argv[1]+"_18.dat", 'r')
#fp19 = open(sys.argv[1]+"_19.dat", 'r')

fout=open("whole.dat", 'w')
#except IOError:
#	print "can not open file"

s1 = fp1.readline()
s2 = fp2.readline()
s3 = fp3.readline()
s4 = fp4.readline()
s5 = fp5.readline()
s6 = fp6.readline()
s7 = fp7.readline()
s8 = fp8.readline()
#s9 = fp9.readline()
#s10 = fp10.readline()
#s11 = fp11.readline()
#s12 = fp12.readline()
#s13 = fp13.readline()
#s14 = fp14.readline()
#s15 = fp15.readline()
#s16 = fp16.readline()
#s17 = fp17.readline()
#s18 = fp18.readline()
#s19 = fp19.readline()


j=0;
while s1:
        aList1 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s1)
        aList2 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s2)
        aList3 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s3)
        aList4 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s4)
        aList5 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s5)
        aList6 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s6)
        aList7 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s7)
        aList8 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s8)
        #aList9 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s9)
        #aList10 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s10)
        #aList11 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s11)
        #aList12 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s12)
        #aList13 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s13)
        #aList14 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s14)
        #aList15 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s15)
        #aList16 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s16)
       # aList17 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s17)
       # aList18 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s18)
       # aList19 = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s19)


#        print aList
        for i in range(len(aList1)):
          
                aNum = float(aList1[i][0]+aList1[i][2])
                str1=str(aNum)
               
                fout.write(str1);
                fout.write(" ");
                aNum = float(aList2[i][0]+aList2[i][2])
                str1=str(aNum)

                fout.write(str1);
                fout.write(" ");
                aNum = float(aList3[i][0]+aList3[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                aNum = float(aList4[i][0]+aList4[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                aNum = float(aList5[i][0]+aList5[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                aNum = float(aList6[i][0]+aList6[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");
                aNum = float(aList6[i][0]+aList6[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");
                

                aNum = float(aList7[i][0]+aList7[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write("\n");
       		j=j+1
        #print j
        s1 = fp1.readline()
	s2 = fp2.readline()
	s3 = fp3.readline()
	s4 = fp4.readline()
	s5 = fp5.readline()
	s6 = fp6.readline()
	s7 = fp7.readline()
	s8 = fp8.readline()
 
'''
                aNum = float(aList8[i][0]+aList8[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                aNum = float(aList9[i][0]+aList9[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                aNum = float(aList10[i][0]+aList10[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                aNum = float(aList11[i][0]+aList11[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                aNum = float(aList12[i][0]+aList12[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                aNum = float(aList13[i][0]+aList13[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                aNum = float(aList14[i][0]+aList14[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                aNum = float(aList15[i][0]+aList15[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                aNum = float(aList16[i][0]+aList16[i][2])
                str1=str(aNum)
                fout.write(str1);
                fout.write(" ");

                #aNum = float(aList17[i][0]+aList17[i][2])
                #str1=str(aNum)
                #fout.write(str1);
                #fout.write(" ");

                #aNum = float(aList18[i][0]+aList18[i][2])
                #str1=str(aNum)
                #fout.write(str1);
                #fout.write(" ");

                #aNum = float(aList19[i][0]+aList19[i][2])
                #str1=str(aNum)
                #fout.write(str1);
'''
   	#s9 = fp9.readline()
	#s10 = fp10.readline()
	#s11 = fp11.readline()
	#s12 = fp12.readline()
	#s13 = fp13.readline()
	#s14 = fp14.readline()
	#s15 = fp15.readline()
	#s16 = fp16.readline()
	#s17 = fp17.readline()
	#s18 = fp18.readline()
	#s19 = fp19.readline()
             
fp1.close()
fp2.close()
fp3.close()
fp4.close()
fp5.close()
fp6.close()
fp7.close()
fp8.close()
#fp9.close()
#fp10.close()
#fp11.close()
#fp12.close()
#fp13.close()
#fp14.close()
#fp15.close()
#fp16.close()
#fp17.close()
#fp18.close()
#fp19.close()


