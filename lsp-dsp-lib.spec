Name:          liblsp-dsp
Version:       0.5.8
Release:       0
Summary:       DSP library for signal processing
License:       LGPL-3.0-or-later
Group:         System/Libraries
URL:           https://github.com/sadko4u/lsp-dsp-lib
Source0:       lsp-dsp-lib-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildRequires: gcc gcc-c++

%description
DSP library for digital signal processing (and more).

This library provides set of functions that perform SIMD-optimized 
computing on several hardware architectures.

%package devel
Summary:       DSP library for signal processing (development files)
Requires:      %{name} = %{version}
Group:         Development/Libraries/C and C++
BuildRequires: pkg-config

%description devel
DSP library for digital signal processing (and more).

This library provides set of functions that perform SIMD-optimized 
computing on several hardware architectures.

These are the development files for lsp-dsp-lib.

%prep
%setup -q -n lsp-dsp-lib-%{version}

%build
make config PREFIX=%{_prefix} LIBDIR=%{_libdir}
%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license COPYING
%{_libdir}/*.so

%files devel
%{_libdir}/*.a
%{_includedir}/lsp-plug.in
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/lsp-dsp-lib.pc
