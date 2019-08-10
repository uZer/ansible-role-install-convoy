#!/bin/sh

convoy daemon \
  --cmd-timeout 10m \
  --ignore-config-file \
  --drivers vfs \
  --driver-opts vfs.path=/mnt/glusterfs \
  --log /var/log/convoy.log
