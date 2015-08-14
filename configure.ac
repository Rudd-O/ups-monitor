dnl Process with autoconf to produce configure

AC_INIT
AC_CONFIG_SRCDIR([ups-monitor.glade])
AM_INIT_AUTOMAKE(ups-monitor, `cat $srcdir/version`)
AM_MAINTAINER_MODE

AM_PATH_PYTHON

AC_PATH_PROG(DESKTOP_FILE_INSTALL, desktop-file-install, NO)
if test x"$DESKTOP_FILE_INSTALL" = xNO ; then
   AC_MSG_ERROR([You need to install the program desktop-file-install.
It can be found in the desktop-file-utils package.])
fi

AC_SUBST(DESKTOP_FILE_INSTALL)

dnl *************************************************
dnl gettext support
dnl *************************************************

GETTEXT_PACKAGE=ups-monitor
AC_SUBST(GETTEXT_PACKAGE)
dnl AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE,"$GETTEXT_PACKAGE",
dnl		[the gettext domain])

AC_CONFIG_FILES([Makefile ups-monitor.spec])
AC_OUTPUT
