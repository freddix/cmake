Summary:	Cross-platform, open-source make system
Name:		cmake
Version:	3.0.2
Release:	1
License:	BSD
Group:		Development/Building
Source0:	http://www.cmake.org/files/v3.0/%{name}-%{version}.tar.gz
# Source0-md5:	db4c687a31444a929d2fdc36c4dfb95f
URL:		http://www.cmake.org/HTML/Index.html
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CMake is used to control the software compilation process using simple
platform and compiler independent configuration files. CMake generates
native makefiles and workspaces that can be used in the compiler
environment of your choice. CMake is quite sophisticated: it is
possible to support complex environments requiring system
configuration, pre-processor generation, code generation, and template
instantiation.

%prep
%setup -q

cat > "init.cmake" <<EOF
SET (CMAKE_VERBOSE_MAKEFILE ON CACHE BOOL "Verbose build" FORCE)
EOF

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CFLAGS="%{rpmcflags}%{rpmcppflags}"
export CXXFLAGS="%{rpmcxxflags}%{rpmcppflags}"
export LDFLAGS="%{rpmldflags}"
./bootstrap \
	--datadir=/share/cmake	\
	--init=init.cmake	\
	--mandir=/share/man	\
	--prefix=%{_prefix}	\
	--verbose
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/cmake

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright.txt
%attr(755,root,root) %{_bindir}/ccmake
%attr(755,root,root) %{_bindir}/cmake
%attr(755,root,root) %{_bindir}/cpack
%attr(755,root,root) %{_bindir}/ctest
%{_aclocaldir}/cmake.m4
%{_datadir}/cmake
%dir %{_libdir}/cmake

