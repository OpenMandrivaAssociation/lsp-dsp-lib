Name:          lsp-dsp-lib
Version:       0.5.11
Release:       1
Summary:       DSP library for signal processing
License:       LGPL-3.0
Group:         System/Libraries
URL:           https://github.com/sadko4u/lsp-dsp-lib
Source0:       https://github.com/sadko4u/lsp-dsp-lib/releases/download/0.5.11/lsp-dsp-lib-0.5.11-src.tar.gz

BuildRequires: make

%description
DSP library for digital signal processing (and more).

This library provides set of functions that perform SIMD-optimized 
computing on several hardware architectures.

%package devel
Summary:       DSP library for signal processing (development files)
Requires:      %{name} = %{version}
Group:         Development/Libraries/C and C++
BuildRequires: pkgconfig

%description devel
DSP library for digital signal processing (and more).

This library provides set of functions that perform SIMD-optimized 
computing on several hardware architectures.

These are the development files for lsp-dsp-lib.

%prep
%autosetup -p1 %{name}-%{version}-src

%build
make config PREFIX=%{_prefix} LIBDIR=%{_libdir}
%make_build

%install
%make_install

%files
%doc README.md
%license COPYING
%{_libdir}/*.so

%files devel
%{_libdir}/*.a
%{_includedir}/lsp-plug.in
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/lsp-dsp-lib.pc
