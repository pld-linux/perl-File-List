#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	List
Summary:	File::List Perl module - crawling directory trees and compiling lists of files
Summary(pl.UTF-8):	Moduł Perla File::List - chodzenie po drzewach katalogów tworząc listy plików
Name:		perl-File-List
Version:	0.3.1
Release:	4
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

%description -l pl.UTF-8
Ten moduł przechodzi po drzewie katalogów zaczynając od zadanego
katalogu bazowego i zwraca pliku (i/lub katalogi, jeśli sobie tego
zażyczyć) pasujące do wyrażenia regularnego.

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
