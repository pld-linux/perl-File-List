#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	List
Summary:	File::List Perl module - crawling directory trees and compiling lists of files
Summary(pl):	Modu³ Perla File::List - chodzenie po drzewach katalogów tworz±c listy plików
Name:		perl-File-List
Version:	0.3.1
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0fdefea8d6dffabc3c2244ea0c627c50
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module crawls the directory tree starting at the provided base
directory and can return files (and/or directories if desired)
matching a regular expression.

%description -l pl
Ten modu³ przechodzi po drzewie katalogów zaczynaj±c od zadanego
katalogu bazowego i zwraca pliku (i/lub katalogi, je¶li sobie tego
za¿yczyæ) pasuj±ce do wyra¿enia regularnego.

%prep
%setup -q -n %{pdir}/%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
