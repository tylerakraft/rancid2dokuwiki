# rancid2dokuwiki
This python script copies rancid backups from a locally installed rancid instance to a locally installed dokuwiki instance

### Recommendations ###

I'd recommend using a subnamespace for your config files in dokuwiki so that your device configs are not mixed in with the rest of your dokuwiki pages and your file operations are limited to a single directory.  Example:  If you have a namespace "IT" in dokuwiki create a subname space named "IT:rancid" so that your config files are in their own directory.  You'd then have a directory named /path-to-dokuwiki/data/pages/it/rancid/ and in order to reference a config in dokuwiki you'd use [[IT:rancid:devicename | Device Name]]

### Usage ###

  1. Clone this script to your server running both rancid and dokuwiki
  2. Make sure to modify your paths so that they read from the proper directory and write to the proper directory
  3. Run the script and verify that everything works (I run this script at root)
  4. Create a cron entry to run 5-10 minutes after your rancid job kicks off so that it updates as your configs are backed up
  
### NOTES: ###

I'm new to python so I'm sure this code could be WAY better but it does what I need it to.  I'll optimize it eventually. 
