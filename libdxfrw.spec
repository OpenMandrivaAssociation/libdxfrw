%define major 0
%define libname	%mklibname dxfrw %{major}
%define develname %mklibname dxfrw -d

Summary:	C++ library to read/write dxf files in binary and ascii form
Name:		libdxfrw
Version:	0.5.8
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		https://sourceforge.net/projects/libdxfrw
Source0:	http://prdownloads.sourceforge.net/libdxfrw/files/%{name}-%{version}.tar.bz2

%description
libdxfrw is a free C++ library to read and write DXF
files in both formats, ascii and binary form. It is licensed under
the terms of the GNU General Public License version 2
(or at you option any later version).

%package -n %{libname}
Summary:	A library of functions for manipulating DXF format files
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with libdxfrw.

%package -n %{develname}
Summary:	Development tools for programs to manipulate DXF files
Group:		Development/C++

%description -n	%{develname}
The libdxfrw-devel package contains the header files and libraries
necessary for developing programs using the libdxfrw library.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std 

%files -n %{libname}
%{_libdir}/libdxfrw.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/libdxfrw.so
%{_libdir}/pkgconfig/libdxfrw*.pc

