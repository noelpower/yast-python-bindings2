#
# spec file for package yast2-python-bindings2
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           yast2-python-bindings2
Version:        1.0
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.gz

Group:	        System/YaST
License:        GPL-3.0
BuildRequires:  yast2-ycp-ui-bindings
BuildRequires:  autoconf-archive
BuildRequires:  swig
BuildRequires:  yast2-core-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  g++

Requires:       yast2-ycp-ui-bindings
Requires:	    yast2-core
Requires:	    python

Summary:	    Python bindings for the YaST platform.

%description
The bindings allow YaST modules to be written using the Python language
and also Python scripts can use YaST agents, APIs and modules.

%prep
%setup -n %{name}-%{version}

%build
autoreconf -if
%configure --prefix=%{_prefix}
make

%install
make install DESTDIR=%{buildroot}

%files
%defattr (-, root, root)

