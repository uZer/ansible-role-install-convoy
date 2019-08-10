#!/usr/bin/env python3

import subprocess
import shutil
import glob
import pathlib
import os
import re
import sys
import yaml
import argparse
from datetime import datetime

# function backup {

    # $VOLUME
    # rm -rf $BACKUP_DIR
    # mkdir -p $BACKUP_DIR
    # rm -f backup_urls
    # touch backup_urls
    # SNAP="$(convoy snapshot create $VOLUME)"
    # convoy backup create $SNAP --dest vfs://$BACKUP_DIR >> $BACKUP_DIR/backup_urls

    # echo "Generated backup on ${DATE} from snapshot ${SNAP}"

  # }

  # function restore {
    # head backup_urls | {
      # read -r CURRENT_BACKUP
      # convoy delete $VOLUME
      # convoy create $VOLUME --backup "${CURRENT_BACKUP}"
    # }
  # }

def backup(volume,backup_dir):

    snap_command = [ "convoy", "snapshot", "create", f"{volume}" ]
    print("#" + ' '.join(snap_command)
    snap_result = subprocess.run(snap_command, check=True, stdout=PIPE, stderr=PIPE,)

    backup_command = [
            "convoy", "backup", "create",
            f"{snap_result.output}", "--dest" f"vfs://{backup_dir}" ]
    print("#" + ' '.join(backup_command)
    backup_result = subprocess.run(backup_command, check=True, stdout=PIPE, stderr=PIPE,)
    print(backup_result.output)

def restore():

def main():
    parser = argparse.ArgumentParser(
        description='Prepare a tezos shell dev enviromemnt')

    parser.add_argument('--backup-dir', '-d', dest='backup_dir', metavar='DIR', type=str,
                        help='Default /mnt', required=False, default="/mnt")

    parser.add_argument('--restore', '-r', dest='restore', action='store_true')

    parser.add_argument('volume', metavar='VOLUME', type=str, nargs=1,
                        help='docker volume')

    args = parser.parse_args()

    if args.restore :
        restore()
    else :
        backup(args.volume[0],args.backup_dir)

if __name__ == "__main__":
    main()
