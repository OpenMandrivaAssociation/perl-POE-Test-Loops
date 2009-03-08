
%define realname   POE-Test-Loops
%define version    1.004
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Reusable tests for POE::Loop authors
Source:     http://www.cpan.org/modules/by-module/POE/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
POE::Test::Loops contains one function, generate(), which will generate all
the loop tests for one or more POE::Loop subclasses.

The the /SYNOPSIS manpage example is a version of the poe-gen-tests
manpage, which is a stand-alone utility to generate the actual tests. the
poe-gen-tests manpage also documents the POE::Test::Loops system in more
detail.



%prep
%setup -q -n %{realname}-%{version} 

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
%perl_vendorlib/*
/usr/bin/poe-gen-tests
/usr/share/man/man1/poe-gen-tests.1.lzma

