#!/bin/sh
# Run this to generate all the initial makefiles, etc.

srcdir=`dirname $0`
test -z "$srcdir" && srcdir=.

PKG_NAME="ups-monitor"

(test -f $srcdir/configure.ac \
  && test -f $srcdir/ups-monitor.glade) || {
    echo -n "**Error**: Directory "\`$srcdir\'" does not look like the"
    echo " top-level directory of $PKG_NAME"
    exit 1
}

aclocal
autoconf
automake -a
./configure "$@"

