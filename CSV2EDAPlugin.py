import sys
#import numpy


class CSV2EDAPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      firstline = filestuff.readline()
      self.bacteria = firstline.split(',')
      self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = []
      i = 0
      for line in filestuff:
         contents = line.split(',')
         self.ADJ.append([])
         for j in range(self.n):
            value = float(contents[j+1])
            if (i != j and value != 0):
               self.ADJ[i].append(value)
            else:
               self.ADJ[i].append(0)
         i += 1

   def output(self, filename):
      #gmlfilename = self.myfile[0:len(self.myfile)-3] + "gml"
      #gmlfile = open(gmlfilename, 'w')
      edafile = open(filename, 'w')
 
      edafile.write("name\tnewweight\n")
      for i in range(self.n):
         for j in range(self.n):
            if (self.ADJ[i][j] != 0):
               self.bacteria[i] = self.bacteria[i].strip()
               self.bacteria[j] = self.bacteria[j].strip()
               if (self.bacteria[i][0] == '\"'):
                  self.bacteria[i] = self.bacteria[i][1:len(self.bacteria[i])-1]
               if (self.bacteria[j][0] == '\"'):
                  self.bacteria[j] = self.bacteria[j][1:len(self.bacteria[j])-1]
               edafile.write(self.bacteria[i]+" (pp) "+self.bacteria[j]+"\t"+str(self.ADJ[i][j])+"\n")




