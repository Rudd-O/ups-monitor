# $Id: Makefile 53 2004-06-28 23:27:58Z rudd-o $

VERSION	= $(shell head -1 ./version)
INSTALL	= install
XARGS	= xargs
FIND	= find


ifndef PREFIX
 PREFIX	= /usr/local
endif

ifndef BINDIR
 BINDIR	= $(PREFIX)/bin
endif
ifndef SHAREDIR
 SHAREDIR	= $(PREFIX)/share/ups-monitor
endif
ifndef PIXMAPDIR
 PIXMAPDIR	= $(PREFIX)/share/pixmaps
endif
ifndef DOCDIR
 DOCDIR	= $(PREFIX)/share/doc/ups-monitor-$(VERSION)
endif


install:
	$(INSTALL) -D -m 644 README $(RPM_BUILD_ROOT)/$(DOCDIR)/README
	$(INSTALL) -D -m 644 COPYING $(RPM_BUILD_ROOT)/$(DOCDIR)/COPYING
	$(INSTALL) -D -m 644 TODO $(RPM_BUILD_ROOT)/$(DOCDIR)/TODO
	$(INSTALL) -D -m 755 ups-monitor $(RPM_BUILD_ROOT)$(BINDIR)/ups-monitor
	$(INSTALL) -D -m 644 ups-monitor.glade $(RPM_BUILD_ROOT)$(SHAREDIR)/ups-monitor.glade
	$(INSTALL) -D -m 644 ups-monitor.gladep $(RPM_BUILD_ROOT)$(SHAREDIR)/ups-monitor.gladep
	$(INSTALL) -D -m 644 battery-level.png $(RPM_BUILD_ROOT)$(SHAREDIR)/battery-level.png
	$(INSTALL) -D -m 644 load.png $(RPM_BUILD_ROOT)$(SHAREDIR)/load.png
	$(INSTALL) -D -m 644 remaining-time.png $(RPM_BUILD_ROOT)$(SHAREDIR)/remaining-time.png
	$(INSTALL) -D -m 644 ups-monitor.png $(RPM_BUILD_ROOT)$(SHAREDIR)/ups-monitor.png
	$(INSTALL) -D -m 644 ups-monitor.png $(RPM_BUILD_ROOT)$(PIXMAPDIR)/ups-monitor.png
	$(INSTALL) -D -m 644 version $(RPM_BUILD_ROOT)$(SHAREDIR)/version
	desktop-file-install --vendor amauta --dir $(RPM_BUILD_ROOT)$(PREFIX)/share/applications ups-monitor.desktop

dist:
	make clean
	./gendist.sh



clean:
	find . -name '*~' -print0 | xargs -0 rm -f
	find . -name '*.bak' -print0 | xargs -0 rm -f
	rm -f ups-monitor-*.tar.gz
	rm -f ups-monitor-*.rpm


rpm:
	make dist
	rpmbuild -ta ups-monitor-*.tar.gz
