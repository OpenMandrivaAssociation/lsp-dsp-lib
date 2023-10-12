#global debug_package %{nil}
%define _empty_manifest_terminate_build 0
%define major %{nil}
%define libpackage %mklibname lsp-dsp-lib %{major}
%define devpackage %mklibname -d lsp-dsp-lib


Name:          lsp-dsp-lib
Version:       1.0.18
Release:       1
Summary:       DSP library for signal processing
License:       LGPL-3.0
Group:         System/Libraries
URL:           https://github.com/sadko4u/lsp-dsp-lib
Source0:       https://github.com/sadko4u/lsp-dsp-lib/releases/download/%{version}/%{name}-%{version}-src.tar.gz

BuildRequires: make

%description
DSP library for digital signal processing (and more).

This library provides set of functions that perform SIMD-optimized 
computing on several hardware architectures.

%package -n %{libpackage}
Summary:	DSP library for digital signal processing (and more).
Group:		System/Libraries

%description -n %{libpackage}
DSP library for digital signal processing (and more).

%package -n %{devpackage}
Summary:       DSP library for signal processing (development files)
Group:         Development/Libraries/C and C++
BuildRequires: pkgconfig
Requires:	%{libpackage} = %{EVRD}

%description -n %{devpackage}
DSP library for digital signal processing (and more).

This library provides set of functions that perform SIMD-optimized 
computing on several hardware architectures.

These are the development files for lsp-dsp-lib.

%prep
%setup -q -n %{name}

%build
make config PREFIX=%{_prefix} LIBDIR=%{_libdir}
%make_build

%install
%make_install

%files -n %{libpackage}
%license COPYING
%{_libdir}/*.so

%files -n %{devpackage}
%{_libdir}/*.a
%{_includedir}/lsp-plug.in/
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/lsp-dsp-lib.pc
