%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	List
Summary:	File::List - Crawling directory trees and compiling lists of files
Summary(pl):	Modu³ File::List - przechodz±cy po drzewach katalogów i tworz±cy listy plików
Name:		perl-File-List
Version:	0.3.1
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
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
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
