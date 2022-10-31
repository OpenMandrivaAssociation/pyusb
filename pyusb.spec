Name:		pyusb
Version:	1.2.1
Release:	1
Summary:	Python bindings for libusb
Group:		Development/Python 
License:	BSD	
URL:		https://pypi.org/project/pyusb
Source0:	https://files.pythonhosted.org/packages/source/p/pyusb/pyusb-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	pkgconfig(libusb)
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
PyUSB provides easy USB access to python. The module contains classes and 
methods to support most USB operations.

%prep
%autosetup -p1 -n pyusb-%{version}

%build
%py_build

%install
%py_install
 
%files
%defattr(-,root,root,-)
%{python_sitelib}/*
