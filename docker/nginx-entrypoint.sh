#!/bin/bash

set -e 

if [ "$1" = "nginx" ]; then
      exec $@ -g 'daemon off;'
fi

exec "$@"
