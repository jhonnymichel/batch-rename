import sys
import os
import csv

def rename_files(path, name_map, ext):
   with open(name_map, 'rb') as csv_map:
      map_reader = csv.reader(csv_map)
      for row in map_reader:
          old_name, new_name = list(row)
          old_filename = '%s/%s.%s' % (path, old_name, ext)
          new_filename = '%s/%s.%s' % (path, new_name, ext)
          try:
            os.rename(old_filename, new_filename)
          except Exception as e:
              print('Rename for file %s failed. Details: ' % old_filename)
              print(e)

if __name__ == '__main__':
    filename, path, name_map, ext = sys.argv
    rename_files(path, name_map, ext)
