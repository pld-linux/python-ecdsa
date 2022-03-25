#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2	# Python 2.x module
%bcond_without	python3	# Python 3.x module

%define 	module	ecdsa
Summary:	ECDSA cryptographic signature library
Summary(pl.UTF-8):	Biblioteka podpisów kryptograficznych ECDSA
Name:		python-%{module}
Version:	0.16.1
Release:	3
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/ecdsa/
Source0:	https://files.pythonhosted.org/packages/source/e/ecdsa/%{module}-%{version}.tar.gz
# Source0-md5:	98c0da4c046286e892fdba727f93edea
URL:		https://pypi.org/project/ecdsa
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-hypothesis
BuildRequires:	python-pytest
BuildRequires:	python-six >= 1.9.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-hypothesis
BuildRequires:	python3-pytest
BuildRequires:	python3-six >= 1.9.0
%endif
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an easy-to-use implementation of ECDSA cryptography (Elliptic
Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly
create keypairs (signing key and verifying key), sign messages, and
verify the signatures. The keys and signatures are very short, making
them easy to handle and incorporate into other protocols.

%description -l pl.UTF-8
Ten moduł to implementacja kryptografii ECDSA (Elliptic Curve Digital
Signature Algorytm - algorytmu podpisu cyfrowego opartego na krzywych
eliptycznych) w czystym Pythonie, wydana na licencji MIT. Przy użyciu
tej biblioteki można szybko tworzyć pary kluczy (podpisujący i
weryfikujący), podpisywać wiadomości oraz sprawdzać podpisy. Klucze i
podpisy są bardzo krótkie, co czyni je łatwymi do obsłużenia i
włączenia do innych protokołów.

%package -n python3-%{module}
Summary:	ECDSA cryptographic signature library
Summary(pl.UTF-8):	Biblioteka podpisów kryptograficznych ECDSA
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
This is an easy-to-use implementation of ECDSA cryptography (Elliptic
Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly
create keypairs (signing key and verifying key), sign messages, and
verify the signatures. The keys and signatures are very short, making
them easy to handle and incorporate into other protocols.

%description -n python3-%{module} -l pl.UTF-8
Ten moduł to implementacja kryptografii ECDSA (Elliptic Curve Digital
Signature Algorytm - algorytmu podpisu cyfrowego opartego na krzywych
eliptycznych) w czystym Pythonie, wydana na licencji MIT. Przy użyciu
tej biblioteki można szybko tworzyć pary kluczy (podpisujący i
weryfikujący), podpisywać wiadomości oraz sprawdzać podpisy. Klucze i
podpisy są bardzo krótkie, co czyni je łatwymi do obsłużenia i
włączenia do innych protokołów.

%prep
%setup -q -n ecdsa-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest src
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest src
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE NEWS README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
