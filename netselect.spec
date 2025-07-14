Summary:	Choose the fastest server automatically
Summary(pl.UTF-8):	Automatyczny wybór najszybszego serwera
Name:		netselect
Version:	0.3
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://alumnit.ca/~apenwarr/netselect/%{name}-%{version}.tar.gz
# Source0-md5:	3a3714946db2458e5db3d55373057ef2
Patch0:		%{name}-debian.patch
Patch1:		%{name}-Makefile.patch
URL:		http://alumnit.ca/~apenwarr/netselect/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is netselect, an ultrafast intelligent parallelizing
binary-search implementation of "ping". You give it a (possibly very
long) list of servers, and it chooses the fastest/closest one
automatically. It's good for finding the fastest ftp mirror, the least
laggy IRC server, or the best Squid neighbour.

%description -l pl.UTF-8
netselect to bardzo szybka, inteligentna, równoległa implementacja
polecenia "ping". Podaje mu się (prawdopodobnie bardzo długą) listę
serwerów, a on wybiera z nich automatycznie najszybszy/najbliższy.
Jest to przydatne do znajdowania najszybszego serwera ftp, najmniej
lagującego serwera IRC albo najlepszego sąsiedzkiego serwera proxy.

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p0

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
