Name:           perl-Test-CPAN-Meta
Version:        0.12
Release:        3%{?dist}
Summary:        Validation of the META.yml file in a CPAN distribution
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-CPAN-Meta/
Source0:        http://www.cpan.org/authors/id/B/BA/BARBIE/Test-CPAN-Meta-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Parse::CPAN::Meta) >= 0.02
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More) >= 0.70
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.08
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of package makers
and installers such as ExtUtils::MakeMaker, Module::Build and
Module::Install.

%prep
%setup -q -n Test-CPAN-Meta-%{version}

iconv -f iso-8859-1 -t utf-8 LICENSE > LICENSE.tmp
mv -f LICENSE.tmp LICENSE

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test AUTOMATED_TESTING=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Artistic Changes LICENSE README examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 01 2008 Steven Pritchard <steve@kspei.com> 0.12-1
- Update to 0.12.
- BR Test::Builder and Test::Builder::Tester.

* Wed Jun 04 2008 Steven Pritchard <steve@kspei.com> 0.11-1
- Update to 0.11.

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 0.10-1
- Specfile autogenerated by cpanspec 1.75.
- Enable author tests.
- Add examples to docs.
- BR Test::More.
- Convert LICENSE to UTF-8.
- Drop bogus Requires.
