#
# spec file for package 
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#    Copyright (C) 2014 - 2017 Eaton
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# To build with draft APIs, use "--with drafts" in rpmbuild for local builds or add
#   Macros:
#   %_with_drafts 1
# at the BOTTOM of the OBS prjconf
%bcond_with drafts
%if %{with drafts}
%define DRAFTS yes
%else
%define DRAFTS no
%endif
%define SYSTEMD_UNIT_DIR %(pkg-config --variable=systemdsystemunitdir systemd)
Name:           czmq
Version:        3.0.2
Release:        4
License:        LGPL-2.1+
Summary:        High-level C binding for ØMQ
Url:            https://github.com/zeromq/czmq
Group:          Development/Libraries/C and C++
Source0:        %{name}-%{version}.tar.gz
#Patch0:         0000-prevent-s_thread_shim-assert.patch
#Patch1:         0001-suppress-sndtimeo-assert.patch
#Patch2:         0001-Problem-zlist_dup-doesn-t-create-copy-autofree-list-.patch
#Patch3:         0002-Problem-zlist_dup-does-not-copy-comparison-function.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  zeromq-devel > 4.1
BuildRequires:  libsodium-devel
BuildRequires:  pkg-config
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
# documentation
BuildRequires:  asciidoc
BuildRequires:  xmlto
BuildRequires:  xz

%description
CZMQ has these goals:

 * To wrap the ØMQ core API in semantics that lead to shorter, more readable applications.
 * To hide as far as possible the differences between different versions of ØMQ (2.x, 3.x, 4.x).
 * To provide a space for development of more sophisticated API semantics.
 * To wrap the ØMQ security features with high-level tools and APIs.
 * To become the basis for other language bindings built on top of CZMQ.

%package -n lib%{name}3
Summary:    Shared library of %{name}
Group:      Development/Languages/C and C++

%description -n lib%{name}3
This package contain shared library of %{name}.

%package devel
Summary:    Devel files for %{name}
Group:      Development/Languages/C and C++
Requires:   lib%{name}3 = %{version}

%description devel
Development files (headers, pkgconfig, cmake) for %{name}.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

rm -f %{buildroot}/%{_bindir}/*.gsl
rm -f %{buildroot}/%{_libdir}/*.la

%post -n lib%{name}3 -p /sbin/ldconfig

%postun -n lib%{name}3 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/makecert

%files -n lib%{name}3
%defattr(-,root,root)
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS NEWS
%{_includedir}/*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_mandir}/man1/makecert.1.gz
%{_mandir}/man3/z*.3.gz
%{_mandir}/man7/%{name}.7.gz

%changelog
