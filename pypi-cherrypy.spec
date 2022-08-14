#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cherrypy
Version  : 18.8.0
Release  : 43
URL      : https://files.pythonhosted.org/packages/60/ea/6c4d16b0cd1f4f64a478bac8a37d75a585e854afb5693ce80a9711efdc4a/CherryPy-18.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/60/ea/6c4d16b0cd1f4f64a478bac8a37d75a585e854afb5693ce80a9711efdc4a/CherryPy-18.8.0.tar.gz
Summary  : Object-Oriented HTTP framework
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-cherrypy-bin = %{version}-%{release}
Requires: pypi-cherrypy-license = %{version}-%{release}
Requires: pypi-cherrypy-python = %{version}-%{release}
Requires: pypi-cherrypy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cheroot)
BuildRequires : pypi(jaraco.collections)
BuildRequires : pypi(more_itertools)
BuildRequires : pypi(portend)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(zc.lockfile)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct.svg
:alt: SWUbanner

%package bin
Summary: bin components for the pypi-cherrypy package.
Group: Binaries
Requires: pypi-cherrypy-license = %{version}-%{release}

%description bin
bin components for the pypi-cherrypy package.


%package license
Summary: license components for the pypi-cherrypy package.
Group: Default

%description license
license components for the pypi-cherrypy package.


%package python
Summary: python components for the pypi-cherrypy package.
Group: Default
Requires: pypi-cherrypy-python3 = %{version}-%{release}

%description python
python components for the pypi-cherrypy package.


%package python3
Summary: python3 components for the pypi-cherrypy package.
Group: Default
Requires: python3-core
Provides: pypi(cherrypy)
Requires: pypi(cheroot)
Requires: pypi(jaraco.collections)
Requires: pypi(more_itertools)
Requires: pypi(portend)
Requires: pypi(zc.lockfile)

%description python3
python3 components for the pypi-cherrypy package.


%prep
%setup -q -n CherryPy-18.8.0
cd %{_builddir}/CherryPy-18.8.0
pushd ..
cp -a CherryPy-18.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658155159
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cherrypy
cp %{_builddir}/CherryPy-18.8.0/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-cherrypy/57a276aabf6e4c65ba334b8b92a08f95620517fc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cherryd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cherrypy/57a276aabf6e4c65ba334b8b92a08f95620517fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
