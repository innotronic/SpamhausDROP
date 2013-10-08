Name: SpamhausDROP
Summary: Applies the "Spamhaus Don't Route Or Peer" IP blacklist
Version: 1.1
Release: 1
License: GPL
Group: System Environment/Network
Source1: SpamhausDROP
Source2: SpamhausDROP.cron
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: initscripts coreutils curl grep diffutils iproute

%description
This System V init script fetches and adds or removes the Spamhaus DROP IP blacklist to the routing table.
A daily cron job triggers refreshing.

%prep


%build


%install
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
mkdir -p %{buildroot}%{_sysconfdir}/cron.daily

install -m 755	%{SOURCE1}	%{buildroot}%{_sysconfdir}/rc.d/init.d/SpamhausDROP
install -m 755	%{SOURCE2}	%{buildroot}%{_sysconfdir}/cron.daily/SpamhausDROP


%clean
rm -rf %{buildroot}


%post
/sbin/chkconfig --add SpamhausDROP
/sbin/service SpamhausDROP start


%preun
/sbin/service SpamhausDROP stop
/sbin/chkconfig --del SpamhausDROP


%files
%{_sysconfdir}/rc.d/init.d/SpamhausDROP
%config %attr(0655,root,root) %{_sysconfdir}/cron.daily/SpamhausDROP


%changelog
* Tue Oct 08 2013 Innotronic Ingenieurburo GmbH <http://www.inno.ch/> 1.1
-Optimize data handling
-Store actual ruleset for later removal
* Tue Sep 16 2008 Innotronic Ingenieurburo Markus Meier <http://www.inno.ch/> 1.0
-First release
