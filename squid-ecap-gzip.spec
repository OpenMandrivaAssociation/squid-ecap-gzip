Summary:	Squid-Gzip compresion on the fly
Name:		squid-ecap-gzip
Version:	1.3.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/Other
URL:		http://code.google.com/p/squid-ecap-gzip/
Source0:	http://squid-ecap-gzip.googlecode.com/files/squid-ecap-gzip-%{version}.tar.gz
BuildRequires:	ecap-devel
BuildRequires:	zlib-devel
Buildroot:	%{_tmppath}/%{rname}-%{version}-%{release}-buildroot

%description
For years, there is a huge demand for a HTTP compression feature of the popular SQUID proxy 
cache. With SQUID 3.1, the eCAP feature was introduced to support third-party modules for content 
adaption, which was earlier performed by the ICAP protocol. VIGOS, a Germany-based software 
company specialised on Web content delivery, is now proud of offering the first eCAP adapter 
providing GZIP content-encoding / HTTP compression for SQUID.

%prep
%setup -n squid-ecap-gzip

%build
%configure2_5x 
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/ecap_adapter_*
