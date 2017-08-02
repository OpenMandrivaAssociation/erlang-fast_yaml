%global srcname fast_xml
%define with_tests 0

Name:    erlang-%{srcname}
Version: 1.1.15
Release: %mkrel 2
Group:   Development/Erlang

License: ASL 2.0
Summary: Fast Expat based Erlang XML parsing and manipulation library
URL:     https://github.com/processone/fast_xml/
Source0: https://github.com/processone/fast_xml/archive/%{version}.tar.gz

Provides:  erlang-p1_xml = %{version}-%{release}
Obsoletes: erlang-p1_xml < 1.1.11

BuildRequires: erlang-edoc
BuildRequires: erlang-rebar
BuildRequires: erlang-p1_utils >= 1.0.5
BuildRequires: expat-devel

%{?__erlang_nif_version:Requires: %{__erlang_nif_version}}


%description
Fast Expat based Erlang XML parsing and manipulation library, with a strong
focus on XML stream parsing from network. It supports full XML structure
parsing, suitable for small but complete XML chunks, and XML stream parsing
suitable for large XML document, or infinite network XML stream like XMPP.
This module can parse files much faster than built-in module xmerl. Depending
on file complexity and size xml_stream:parse_element/1 can be 8-18 times faster
than calling xmerl_scan:string/2.


%prep
%autosetup -n fast_xml-%{version}


%build
%{rebar_compile}


%install
%{erlang_install}

install -p -D -m 755 priv/lib/* --target-directory=$RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/

%if %with_tests
%check
%{rebar_eunit}
%endif

%files
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{erlang_appdir}




%changelog
* Sun Jun 04 2017 neoclust <neoclust> 1.1.15-2.mga6
+ Revision: 1106719
- Disable tests on the BS

* Thu Nov 17 2016 neoclust <neoclust> 1.1.15-1.mga6
+ Revision: 1067873
- imported package erlang-fast_xml

