#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module

%define 	module	ecdsa
Summary:	ECDSA cryptographic signature library
Name:		python-%{module}
Version:	0.11
Release:	4
License:	GPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/e/ecdsa/%{module}-%{version}.tar.gz
# Source0-md5:	8ef586fe4dbb156697d756900cb41d7c
URL:		https://pypi.python.org/pypi/ecdsa
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an easy-to-use implementation of ECDSA cryptography (Elliptic
Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly
create keypairs (signing key and verifying key), sign messages, and
verify the signatures. The keys and signatures are very short, making
them easy to handle and incorporate into other protocols.

%package -n python3-%{module}
Summary:	ECDSA cryptographic signature library
Group:		Libraries/Python
Requires:	python3

%description -n python3-%{module}
This is an easy-to-use implementation of ECDSA cryptography (Elliptic
Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly
create keypairs (signing key and verifying key), sign messages, and
verify the signatures. The keys and signatures are very short, making
them easy to handle and incorporate into other protocols.

%prep
%setup  -q -n ecdsa-%{version}

%build
%if %{with python2}
%py_build --build-base py2
%endif
%if %{with python3}
%py3_build --build-base py3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
%py_build \
	--build-base py2 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%py3_build \
	--build-base py3 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{_examplesdir}/python-%{module}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE NEWS README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif
