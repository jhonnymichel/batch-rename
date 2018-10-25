# batch-rename
batch rename files with a csv or JSON (soon) map

To run the script, just call it providing 3 arguments:

```
python batch_rename.py directory mapfile extension
```

## Example:
To rename all .pdf files on a directory:
```
1.pdf
2.pdf
3.pdf
```

1. Create an old_name->new_name map (currently only the csv format is supported)
```
1,new-name1
2,new-name2
3,new-name3
``` 
2. Call the script providing the path for the pdfs, the path for the map file and the extension of the files to be renamed
```
python batch_rename.py /path/to/pdf/files /path/to/map.csv pdf
```
3. The files will be renamed after the script finishes running
```
new-name1.pdf
new-name2.pdf
new-name3.pdf
```
