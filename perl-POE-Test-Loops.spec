%define upstream_name    POE-Test-Loops
%define upstream_version 1.360
Name:		perl-%{upstream_name}
Version:	1.360
Release:	1

Summary:	Reusable tests for POE::Loop authors
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/rcaputo/poe-test-loops
Source0:	https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Test-Loops-1.360.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
POE::Test::Loops contains one function, generate(), which will generate all
the loop tests for one or more POE::Loop subclasses.

The the /SYNOPSIS manpage example is a version of the poe-gen-tests
manpage, which is a stand-alone utility to generate the actual tests. the
poe-gen-tests manpage also documents the POE::Test::Loops system in more
detail.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{_mandir}/man3/*
%{_mandir}/man1/poe-gen-tests.1*
%{perl_vendorlib}/POE
%{_bindir}/poe-gen-tests


