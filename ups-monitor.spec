# $Id: mydms.spec 57 2004-06-29 00:14:59Z rudd-o $

%define ver 0.1
%define rel 1
%define prefix /usr

Summary:        A graphical UPS monitor for the GNOME desktop
Name:           ups-monitor
Vendor:         Amauta
Version:        %ver
Release:        %rel
Copyright:      Amautacorp S.A. 
Group:          System/Monitoring
Source:         %{name}-%ver.tar.gz
URL:            http://www.amautacorp.com/staff/Rudd-O/ups-monitor/
BuildRoot:      %{_tmppath}/build-%{name}-%{ver}
Requires:       pygtk2 pygtk2-libglade
BuildArch:      noarch
Packager:       Manuel Amador (Rudd-O) <rudd-o@amautacorp.com>

%description
UPS monitor is a graphical application that lets you monitor your UPS
in real-time.  You can check locally attached UPSs or networked UPS.

UPS monitor requires a working Network UPS Tools (nut) server.


%changelog
* Wed Jul 21 2004 Manuel Amador (Rudd-O) <rudd-o@amautacorp.com> 0.1-0
- spec file improvements

* Sat Jul 17 2004 Manuel Amador (Rudd-O) <rudd-o@amautacorp.com> 0.1-0
- first time RPM creation
- first release

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build

%install
PREFIX=%prefix make install



%files
%defattr(-,root,root)
%prefix/bin/ups-monitor
%prefix/share/applications
%prefix/share/pixmaps
%prefix/share/ups-monitor
%doc %prefix/share/doc
