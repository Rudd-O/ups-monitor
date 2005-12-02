dnl Process with autoconf to produce configure

AC_INIT
AC_CONFIG_SRCDIR([ups-monitor.glade])
AM_INIT_AUTOMAKE(ups-monitor, `cat $srcdir/version`)
AM_MAINTAINER_MODE

AM_PATH_PYTHON

PKG_CHECK_MODULES(PREREQS, pygtk-2.0)
PKG_CHECK_MODULES(PREREQS, gnome-python-2.0)

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

dnl Needed to build eggtray.so lib
dnl AC_PROG_LIBTOOL

dnl ===============================================
dnl Checks for eggtray library dependancies
dnl ===============================================
PKG_CHECK_MODULES(EGG, gtk+-2.0 >= 2.4.0 libgnomeui-2.0 >=  2.2.0 pygtk-2.0 >= 2.4.0)
AC_SUBST(EGG_LIBS)
AC_SUBST(EGG_CFLAGS)

AC_CONFIG_FILES([Makefile eggtray/Makefile ups-monitor.spec])
AC_OUTPUT
