# Process with automake to create Makefile.in

SUBDIRS = eggtray

pixmapsdir = $(datadir)/pixmaps
docdir = $(datadir)/doc/$(PACKAGE)-$(VERSION)
appsdir = $(datadir)/applications

bin_SCRIPTS = ups-monitor

pixmaps_DATA = \
	ups-monitor.png

pkgdata_DATA = \
	version \
	ups-monitor.glade \
	ups-monitor.gladep \
	ac-icon.png \
	bat-icon.png \
	battery-critical.png \
	battery-good.png \
	battery-level.png \
	battery-low.png \
	load.png \
	remaining-time.png \
	ups-monitor.png \
	ups-monitor-small.png \
	warning-icon.png

doc_DATA = \
	README \
	COPYING \
	TODO \
	AUTHORS \
	ChangeLog \
	NEWS

man_MANS = ups-monitor.1

# Why do these need to be explicitly put in EXTRA_DIST?

EXTRA_DIST = \
	$(bin_SCRIPTS) \
	$(pkgdata_DATA) \
	$(pixmaps_DATA) \
	$(man_MANS) \
	eggtrayiconmodule.so \
	ups-monitor.desktop ups-monitor.spec autogen.sh

eggtrayiconmodule.so:
	make -C $(srcdir)/eggtray

install-data-hook:
	$(mkinstalldirs) $(DESTDIR)$(appsdir)
	$(DESKTOP_FILE_INSTALL) --vendor rudd-o --dir $(DESTDIR)$(appsdir) $(srcdir)/ups-monitor.desktop

rpm: dist
	rpmbuild -ta $(PACKAGE)-$(VERSION).tar.gz

bzdist: dist
	gunzip -c $(PACKAGE)-$(VERSION).tar.gz | bzip2 > $(PACKAGE)-$(VERSION).tar.bz2
