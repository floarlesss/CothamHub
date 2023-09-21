# This is the program that checks for updates from the CothamHub repo on GitHub.

# TODO:
# This updater will be started when CothamHub is ran.
# The two programs will communicate via a .chcom file (CothamHub Communicate). I imagine the file will be called something like update.chcom and will probably contain the following:

# "Idle": This is written by the CothamHub program and indicates that nothing is being done on the updating side of CothamHub. This will usually be written when CothamHub is started by the updater
# and a phrase/word indicating that updating has suceeded or that there were no updates in the update.chcom file. (this will also be written when the CothamHub is quit.)

# ---------------------------------------------------------------------
#     USUAL START SEQUENCE OF COTHAMHUB WHEN THERE IS NO UPDATE:

#-----COTHAM HUB:
# "Starting Updater and exiting": This will be written to the update.chcom file (in CothamHub/Modules/CH-Updater/update.chcom) by CothamHub. It indicated that CothamHub has
# just started and proceeded to run the Updater.

#-----UPDATER:
# "Checking update status": This will be written to the update.chcom file by the Updater when it has just been started and is checking for updates.

# "No update available, starting CH and waiting for response.": This will be written to the update.chcom file by the Updater when it has confirmed that no new updates are available for CothamHub. 
# The updater will continue to check this file for a change.

#-----COTHAM HUB:
# "CothamHub running, confirm Updater exit": This will be written to the update.chcom file by CothamHub. It is for the purpose of confirming to the Updater program that CothamHub has acknowledged the update status
# and that CothamHub is running OK, giving the updater permission to exit.

#-----UPDATER:
# "Updater exiting": This is the final message from the Updater, and confirms that the start process of CothamHub has completed successfully meaning that everything will be handled by the CothamHub program
# and that the Updater program will exit.