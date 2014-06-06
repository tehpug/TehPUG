#!/bin/bash

# Fix openshift bug, https://www.openshift.com/forums/openshift/postgres-92-backup-using-pgdump-after-upgrade
declare -x PATH='/opt/rh/postgresql92/root/usr/bin/':$PATH

$OPENSHIFT_REPO_DIR/wsgi/manage.py cleanup
$OPENSHIFT_REPO_DIR/wsgi/manage.py dbbackup -cz
