Author: Ryan Hawkins




Prgram Description:
	Program will search through hackerone.com and count all disclosed reports since the Big Bang under the tab "Top"
	hackerone.com>hacktivity>Top>Since:TheBigBang && Filterby: Disclosed


To Run:
	python urlTry.py

This will take some time to run, I have attempted to sleep for a time that seems appropriate, and should allow enough time
for loading of javascript to read the files. Which seems to be ~ 1.5 second. I have not tried inbetween 1.01 - 1.49.

SIDE NOTE:
this is going to create some gecko file that just needs to be removed when finished. I did not set up any make files to clean
the junk out yet. just do:
rm -f ge  (type this much and hit tab for autofill)
