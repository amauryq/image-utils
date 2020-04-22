import sys
import os

def main():
   filepath = sys.argv[1]

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
  
   with open(filepath) as fp:
       for line in fp.readlines():
           filenames = line.split(',')
           filetodelete = filenames[0].replace('"', '').replace('\\\\', '\\')
           print(filetodelete)
           os.remove(filetodelete)

if __name__ == '__main__':
   main()