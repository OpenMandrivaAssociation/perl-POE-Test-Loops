%define upstream_name    POE-Test-Loops
%define upstream_version 1.040

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Reusable tests for POE::Loop authors
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
POE::Test::Loops contains one function, generate(), which will generate all
the loop tests for one or more POE::Loop subclasses.

The the /SYNOPSIS manpage example is a version of the poe-gen-tests
manpage, which is a stand-alone utility to generate the actual tests. the
poe-gen-tests manpage also documents the POE::Test::Loops system in more
detail.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/man3/*
%{_mandir}/man1/poe-gen-tests.1*
%{perl_vendorlib}/POE
%{_bindir}/poe-gen-tests
