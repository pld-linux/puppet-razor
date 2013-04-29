Summary:	Next-Generation Provisioning for bare metal and virtual servers
Name:		puppet-razor
Version:	0.9.0
Release:	0.2
License:	Apache v2.0
Group:		Applications
Source0:	https://github.com/puppetlabs/Razor/archive/%{version}.tar.gz?/%{name}-%{version}.tgz
# Source0-md5:	b7b595cfb9a523018e1139da2dd3ebd0
URL:		https://github.com/puppetlabs/Razor/wiki
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
Requires:	ruby-base62
Requires:	ruby-bson
Requires:	ruby-bson_ext
Requires:	ruby-colored
Requires:	ruby-daemons
Requires:	ruby-json
Requires:	ruby-logger
Requires:	ruby-mongo
Requires:	ruby-net-ssh
Requires:	ruby-pg
Requires:	ruby-rake
Requires:	ruby-require_all
Requires:	ruby-syntax
Requires:	ruby-uuid
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Razor is an advanced provisioning application which can deploy both
bare-metal and virtual systems. It's aimed at solving the problem of
how to bring new metal into a state where your existing
DevOps/configuration management workflows can take it over.

Newly added machines in a Razor deployment will PXE-boot from a
special Razor Microkernel image, then check in, provide Razor with
inventory information, and wait for further instructions. Razor will
consult user-created policy rules to choose which preconfigured model
to apply to a new node, which will begin to follow the model's
directions, giving feedback to Razor as it completes various steps.
Models can include steps for handoff to a DevOps system or to any
other system capable of controlling the node (such as a vCenter server
taking possession of ESX systems).

%prep
%setup -q -n Razor-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE CONTRIBUTING.md  TESTING.md
%attr(755,root,root) %{_bindir}/razor
%attr(755,root,root) %{_bindir}/razor_daemon.rb
# um?
%attr(755,root,root) %{_bindir}/api.js
%attr(755,root,root) %{_bindir}/common.js
%attr(755,root,root) %{_bindir}/http_range_req.js
%attr(755,root,root) %{_bindir}/image_svc.js
%{ruby_vendorlibdir}/project_razor.rb
%{ruby_vendorlibdir}/project_razor
