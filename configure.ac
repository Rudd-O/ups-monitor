dnl Process with autoconf to produce configure

AC_INIT(ups-monitor.glade)
AM_INIT_AUTOMAKE(ups-monitor, `cat $srcdir/version`)
AM_MAINTAINER_MODE

AM_PATH_PYTHON

PKG_CHECK_MODULES(PREREQS, pygtk-2.0)

AC_PATH_PROG(DESKTOP_FILE_INSTALL, desktop-file-install, NO)
if test x"$DESKTOP_FILE_INSTALL" = xNO ; then
   AC_MSG_ERROR([You need to install the program desktop-file-install.
It can be found in the desktop-file-utils package.])
fi

AC_SUBST(DESKTOP_FILE_INSTALL)

AC_OUTPUT([Makefile])
