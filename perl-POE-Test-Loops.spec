%define upstream_name    POE-Test-Loops
%define upstream_version 1.354

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Reusable tests for POE::Loop authors
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/POE-Test-Loops-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.312.0-1mdv2011.0
+ Revision: 684820
- update to new version 1.312

* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.311.0-1
+ Revision: 672863
- update to new version 1.311

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.50.0-1
+ Revision: 660012
- update to new version 1.050

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.40.0-1
+ Revision: 635544
- update to new version 1.040

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.36.0-1mdv2011.0
+ Revision: 626856
- new version

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 1.35.0-1mdv2011.0
+ Revision: 532154
- update to 1.035

* Mon Feb 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.33.0-1mdv2010.1
+ Revision: 506242
- update to 1.033

* Mon Jan 04 2010 Jérôme Quelin <jquelin@mandriva.org> 1.31.0-1mdv2010.1
+ Revision: 486117
- update to 1.031

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.1
+ Revision: 460845
- update to 1.030

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.22.0-1mdv2010.0
+ Revision: 435705
- update to 1.022

* Sun Jul 26 2009 Jérôme Quelin <jquelin@mandriva.org> 1.21.0-1mdv2010.0
+ Revision: 400197
- update to 1.021

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 399605
- update to 1.020
- using %%perl_convert_version
- fixed license field

* Mon Mar 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.005-1mdv2009.1
+ Revision: 353094
- update to new version 1.005

* Sun Mar 08 2009 Jérôme Quelin <jquelin@mandriva.org> 1.004-1mdv2009.1
+ Revision: 352843
- update to new version 1.004

* Sat Jan 31 2009 Jérôme Quelin <jquelin@mandriva.org> 1.003-1mdv2009.1
+ Revision: 335706
- update to new version 1.003

* Mon Jan 19 2009 Jérôme Quelin <jquelin@mandriva.org> 1.002-1mdv2009.1
+ Revision: 331235
- import perl-POE-Test-Loops


* Mon Jan 19 2009 cpan2dist 1.002-1mdv
- initial mdv release, generated with cpan2dist


