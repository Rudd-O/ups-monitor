# $Id$

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
	find -name '*.png' -print | grep -v .svn | xargs -i $(INSTALL) -D -m 644 {} $(RPM_BUILD_ROOT)$(SHAREDIR)/{}
	$(INSTALL) -D -m 644 ups-monitor.png $(RPM_BUILD_ROOT)$(PIXMAPDIR)/ups-monitor.png
	$(INSTALL) -D -m 644 version $(RPM_BUILD_ROOT)$(SHAREDIR)/version
	$(INSTALL) -D -m 755 eggtrayiconmodule.so $(RPM_BUILD_ROOT)$(SHAREDIR)/eggtrayiconmodule.so
	desktop-file-install --vendor rudd-o --dir $(RPM_BUILD_ROOT)$(PREFIX)/share/applications ups-monitor.desktop

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
