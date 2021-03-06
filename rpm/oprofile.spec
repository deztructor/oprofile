Name:       oprofile
Summary:    System-Wide Profiler for Linux Systems
Version:    0.9.8
Release:    1
Group:      Development/Tools
License:    GPL v2 or later
URL:        http://oprofile.sourceforge.net/
Source0:    %{name}-%{version}.tar.gz
Requires(pre): /usr/sbin/groupadd
Requires(pre): /usr/sbin/useradd
BuildRequires: pkgconfig(popt)
BuildRequires: libxslt
BuildRequires: binutils-devel
BuildRequires: fdupes
BuildRequires: libtool

%description
OProfile is a system-wide profiler for Linux systems, capable of
profiling all running code at low overhead. OProfile is released under
the GNU GPL.

It consists of a kernel module and a daemon for collecting sample data,
and several post-profiling tools for turning data into information.

OProfile leverages the CPU hardware performance counters to enable
profiling of a wide variety of interesting statistics, which can also
be used for basic time-spent profiling. All code is profiled: hardware
and software interrupt handlers, kernel modules, the kernel, shared
libraries, and applications (the only exception being the oprofile
interrupt handler itself).

OProfile is currently in alpha status; however it has proven stable
over a large number of differing configurations. As always, there is no
warranty.

This is the package containing the userspace tools.

Authors:
--------
    John Levon <moz@compsoc.man.ac.uk>
    Philippe Elie <phil_e@clubinternet.fr>
    Dave Jones <davej@suse.de>
    Bob Montgomery <bobm@fc.hp.com>


%package devel
Summary:    System-Wide Profiler for Linux Systems
License:    GPL v2 or later; LGPL v2.1 or later
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   binutils-devel

%description devel
OProfile is a system-wide profiler for Linux systems, capable of
profiling all running code at low overhead. OProfile is released under
the GNU GPL.

It consists of a kernel module and a daemon for collecting sample data,
and several post-profiling tools for turning data into information.

OProfile leverages the CPU hardware performance counters to enable
profiling of a wide variety of interesting statistics, which can also
be used for basic time-spent profiling. All code is profiled: hardware
and software interrupt handlers, kernel modules, the kernel, shared
libraries, and applications (the only exception being the oprofile
interrupt handler itself).

OProfile is currently in alpha status; however it has proven stable
over a large number of differing configurations. As always, there is no
warranty.

This package contains the development files.

Authors:
--------
    John Levon <moz@compsoc.man.ac.uk>
    Philippe Elie <phil_e@clubinternet.fr>
    Dave Jones <davej@suse.de>
    Bob Montgomery <bobm@fc.hp.com>

%prep
%setup -q -n %{name}-%{version}/oprofile

%build
sh autogen.sh
%configure --disable-static \
    --prefix=%{_prefix} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir} \
    --with-kernel-support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
%fdupes  %{buildroot}/%{_datadir}

%pre
/usr/sbin/groupadd -r oprofile 2>/dev/null || :
/usr/sbin/useradd -r -g oprofile -d /var/lib/empty -s /bin/false -c "Special user account to be used by OProfile" oprofile 2>/dev/null || :

%files
%defattr(-,root,root,-)
%doc COPYING README TODO
%doc %{_docdir}/oprofile/*
%dir %{_libdir}/oprofile
%{_bindir}/*
%{_datadir}/oprofile
%{_libdir}/oprofile/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
%dir %{_libdir}/oprofile
%{_includedir}/*
%{_libdir}/oprofile/*.so
