# Import required modules

import os
import shutil
import glob

rancidpath = '/path/to/rancid/configs/'  # Modify this to your rancid config backup path include trailing slash
dokuwikipath = '/path/to/dokuwiki/sub/namespace/'  # Modify this to your dokuwiki subnamespace path include trailing slash eg: /opt/dokuwiki/data/pages/namespace/subnamespace/str


# Change to the directory holding your rancid config files

os.chdir(rancidpath)

# Create a new text file with the devicename, prepend the file with <code>, read the config file, write the config file to the new text file, append </code> to the end of the file then close the new file

for filename in os.listdir(rancidpath):
    if os.path.isfile(filename):
        configFile = open(filename, 'r')
        newfilename = filename + '.txt'
        newfile = open(newfilename, 'a')
        newfile.write('<code>\n')
        newfile.write(configFile.read())
        newfile.write('\n</code>')
        newfile.close()
        configFile.close()

# Remove old dokuwiki device files

for file in glob.iglob(os.path.join(dokuwikipath, '*.txt')):
    os.remove(file)

# Copy text files from rancid config diretory to dokuwiki directory

for file in glob.iglob(os.path.join(rancidpath, '*.txt')):
        shutil.copy2(file, dokuwikipath)

# Change ownership from root to www-data

for filename in os.listdir(dokuwikipath):
    if os.path.isfile(filename):
        os.chown(filename, 33, 33)

# Clean up rancid config directory

for file in glob.iglob(os.path.join(rancidpath), '*.txt')):
    os.remove(file)



