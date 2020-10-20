#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab_pygments
Version  : 0.1.2
Release  : 1
URL      : https://files.pythonhosted.org/packages/d1/79/3677d138eeacbba7cf6d0e51e6b8c094448329f7b8a523a5d2599bc898e7/jupyterlab_pygments-0.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/d1/79/3677d138eeacbba7cf6d0e51e6b8c094448329f7b8a523a5d2599bc898e7/jupyterlab_pygments-0.1.2.tar.gz
Summary  : Pygments theme using JupyterLab CSS variables
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jupyterlab_pygments-license = %{version}-%{release}
Requires: jupyterlab_pygments-python = %{version}-%{release}
Requires: jupyterlab_pygments-python3 = %{version}-%{release}
Requires: Pygments
BuildRequires : Pygments
BuildRequires : buildreq-distutils3

%description
# JupyterLab Pygments Theme
This package contains a syntax coloring theme for [pygments](http://pygments.org/) making use of
the JupyterLab CSS variables.

%package license
Summary: license components for the jupyterlab_pygments package.
Group: Default

%description license
license components for the jupyterlab_pygments package.


%package python
Summary: python components for the jupyterlab_pygments package.
Group: Default
Requires: jupyterlab_pygments-python3 = %{version}-%{release}

%description python
python components for the jupyterlab_pygments package.


%package python3
Summary: python3 components for the jupyterlab_pygments package.
Group: Default
Requires: python3-core
Provides: pypi(jupyterlab_pygments)
Requires: pypi(pygments)

%description python3
python3 components for the jupyterlab_pygments package.


%prep
%setup -q -n jupyterlab_pygments-0.1.2
cd %{_builddir}/jupyterlab_pygments-0.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603155274
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyterlab_pygments
cp %{_builddir}/jupyterlab_pygments-0.1.2/LICENSE %{buildroot}/usr/share/package-licenses/jupyterlab_pygments/9627fe5214679aa301dcdbb0f788b000d2cbf30e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyterlab_pygments/9627fe5214679aa301dcdbb0f788b000d2cbf30e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
