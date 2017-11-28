Format: 1.0
Source: czmq
Binary: libczmq1, libczmq-dev, libczmq-dbg
Architecture: any
Version: 3.0.2-3
Maintainer: Alessandro Ghedini <ghedo@debian.org>
Uploaders: Gergely Nagy <algernon@debian.org>, Arnaud Quette <aquette@debian.org>
Homepage: http://czmq.zeromq.org/
Standards-Version: 3.9.6
Build-Depends: debhelper (>= 9), cmake, libpgm-dev, libzmq4-dev, pkg-config, libtool, autoconf, automake
Package-List:
 libczmq-dev deb libdevel optional arch=any
 libczmq1 deb libs optional arch=any
DEBTRANSFORM-TAR: czmq-3.0.2.20171128130150~gita523b94f927e.tar.gz
