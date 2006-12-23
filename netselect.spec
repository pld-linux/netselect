Summary:	Choose the fastest server automatically
Summary(pl):	Automatyczny wybór najszybszego serwera
Name:		netselect
Version:	0.3
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://people.nit.ca/~apenwarr/netselect/%{name}-%{version}.tar.gz
# Source0-md5:	3a3714946db2458e5db3d55373057ef2
Patch0:		%{name}-debian.patch
Patch1:		%{name}-Makefile.patch
URL:		http://people.nit.ca/~apenwarr/netselect/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is netselect, an ultrafast intelligent parallelizing
binary-search implementation of "ping". You give it a (possibly very
long) list of servers, and it chooses the fastest/closest one
automatically. It's good for finding the fastest ftp mirror, the least
laggy IRC server, or the best Squid neighbour.

%description -l pl
netselect to bardzo szybka, inteligentna, równoleg³a implementacja
polecenia "ping". Podaje mu siê (prawdopodobnie bardzo d³ug±) listê
serwerów, a on wybiera z nich automatycznie najszybszy/najbli¿szy.
Jest to przydatne do znajdowania najszybszego serwera ftp, najmniej
laguj±cego serwera IRC albo najlepszego s±siedzkiego serwera proxy.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p0

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog HISTORY README README.traceroute debian/changelog debian/copyright
%attr(4754,root,adm) %{_bindir}/netselect
%{_mandir}/man1/netselect.1*
