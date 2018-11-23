#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Path-Class
Version  : 0.37
Release  : 19
URL      : http://www.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Path-Class-0.37.tar.gz
Source0  : http://www.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Path-Class-0.37.tar.gz
Summary  : 'Cross-platform path specification manipulation'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Path-Class-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Path-Class,
version 0.37:
Cross-platform path specification manipulation

%package dev
Summary: dev components for the perl-Path-Class package.
Group: Development
Provides: perl-Path-Class-devel = %{version}-%{release}

%description dev
dev components for the perl-Path-Class package.


%package license
Summary: license components for the perl-Path-Class package.
Group: Default

%description license
license components for the perl-Path-Class package.


%prep
%setup -q -n Path-Class-0.37

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Path-Class
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Path-Class/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Path/Class.pm
/usr/lib/perl5/vendor_perl/5.28.0/Path/Class/Dir.pm
/usr/lib/perl5/vendor_perl/5.28.0/Path/Class/Entity.pm
/usr/lib/perl5/vendor_perl/5.28.0/Path/Class/File.pm
/usr/lib/perl5/vendor_perl/5.28.0/Path/README.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Path::Class.3
/usr/share/man/man3/Path::Class::Dir.3
/usr/share/man/man3/Path::Class::Entity.3
/usr/share/man/man3/Path::Class::File.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Path-Class/LICENSE
