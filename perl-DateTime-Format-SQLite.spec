#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	DateTime
%define	pnam	Format-SQLite
Summary:	DateTime::Format::SQLite - Parse and format SQLite dates and times
#Summary(pl.UTF-8):	
Name:		perl-DateTime-Format-SQLite
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9cc9cc861407a1bbc696226605279842
URL:		http://search.cpan.org/dist/DateTime-Format-SQLite/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime >= 0.1
BuildRequires:	perl-DateTime-Format-Builder >= 0.6
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module understands the formats used by SQLite for its
date, datetime and time functions.  It can be used to
parse these formats in order to create DateTime objects, and it
can take a DateTime object and produce a timestring accepted by
SQLite.

NOTE: SQLite does not have real date/time types but stores
everything as strings. This module deals with the date/time
strings as understood/returned by SQLite's date, time,
datetime, julianday and strftime SQL functions.
You will usually want to store your dates in one of these formats.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DateTime/Format/*.pm
%{_mandir}/man3/*
