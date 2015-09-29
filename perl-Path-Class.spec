#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Path-Class
Version  : 0.35
Release  : 8
URL      : http://www.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Path-Class-0.35.tar.gz
Source0  : http://www.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Path-Class-0.35.tar.gz
Summary  : 'Cross-platform path specification manipulation'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Path-Class-doc
BuildRequires : perl(Module::Build)

%description
This archive contains the distribution Path-Class,
version 0.35:
Cross-platform path specification manipulation

%package doc
Summary: doc components for the perl-Path-Class package.
Group: Documentation

%description doc
doc components for the perl-Path-Class package.


%prep
%setup -q -n Path-Class-0.35

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/Path/Class.pm
/usr/lib/perl5/site_perl/5.22.0/Path/Class/Dir.pm
/usr/lib/perl5/site_perl/5.22.0/Path/Class/Entity.pm
/usr/lib/perl5/site_perl/5.22.0/Path/Class/File.pm
/usr/lib/perl5/site_perl/5.22.0/Path/README.pod

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
