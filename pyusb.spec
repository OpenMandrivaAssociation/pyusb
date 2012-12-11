%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global alphatag a1
Name:		pyusb
Version:	1.0.0
Release:	%mkrel 1%{alphatag}
Summary:	Python bindings for libusb
Group:		Development/Python 
License:	BSD	
URL:		http://pyusb.sourceforge.net/
Source0:	pyusb-%{version}-%{alphatag}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	python-devel
BuildRequires:	libusb-devel
BuildArch:	noarch

%description
PyUSB provides easy USB access to python. The module contains classes and 
methods to support most USB operations.

%prep
%setup -q -n %{name}-%{version}-%{alphatag}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
sed -i -e 's/\r//g' README

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE
%{python_sitelib}/*


%changelog
* Mon Oct 24 2011 Alexander Barakin <abarakin@mandriva.org> 1.0.0-1a1mdv2012.0
+ Revision: 705876
- imported package pyusb


