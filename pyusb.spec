Name:		pyusb
Version:	1.3.1
Release:	2
Summary:	Python bindings for libusb
Group:		Development/Python 
License:	BSD	
URL:		https://pypi.org/project/pyusb
Source0:	https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

BuildArch:	noarch

%description
PyUSB provides easy USB access to python. The module contains classes and 
methods to support most USB operations.

%prep
%autosetup -p1 -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info
# Fix python*dist(pyusb) dependency versioning
sed -i "/use_scm_version/i    version='%{version}',\n" setup.py

%build
%py_build

%install
%py_install
 
%files
%defattr(-,root,root,-)
%{python_sitelib}/*
