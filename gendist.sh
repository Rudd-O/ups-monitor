#!/bin/sh
# generate distribution tarball
# $Id: gendist.sh 53 2004-06-28 23:27:58Z rudd-o $


basedir="$PWD/`dirname $0`"
version=`head -1 "$basedir/version"`
tmpdir=`mktemp -d /tmp/targz.XXXXX`
mkdir $tmpdir/ups-monitor-$version
cd "$basedir/"
pwd
cp -R * $tmpdir/ups-monitor-$version
cd $tmpdir
find -name '.svn' -print0 | xargs -0 rm -rf
find -name '*~' -print0 | xargs -0 rm -rf
tar cvzf ups-monitor-$version.tar.gz ups-monitor-$version
mv -f ups-monitor-$version.tar.gz  "$basedir/"
rm -rf $tmpdir
