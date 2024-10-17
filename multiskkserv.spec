%define version	20051220
%define release	%mkrel 6

Name:		multiskkserv
Summary:	Simple skk multi-dictionary server
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Internationalization
URL:		https://www3.big.or.jp/~sian/linux/products/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Conflicts:		mecab-skkserv
Requires:		skkdic, cdb0.75
BuildRequires:		cdb0.75-devel

%description
Simple skk multi-dictionary server.


%prep
%setup -q

%build
%configure2_5x --with-cdb=%{_libdir}/cdb-0.75/

%make

%install
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post
# generate SKK-JISYO.L.cdb
cd %{_datadir}/skk/
	rm -f SKK-JISYO.L.cdb
	skkdic-p2cdb SKK-JISYO.L.cdb < SKK-JISYO.L
	chmod 644 SKK-JISYO.L.cdb
cd ..

echo ' '
echo '**********************************************************'
echo 'How to use multiskkserv:'
echo '# multiskkserv [SKKdic1.cdb] [SKKdic2.cdb]... &'
echo '(example)'
echo '# multiskkserv /usr/share/skk/SKK-JISYO.L.cdb &'
echo ' '
echo 'How to convert plain SKKdic to SKKdic.cdb:'
echo '$ skkdic-p2cdb [SKKdic].cdb < [SKKdic]'
echo '(example)'
echo '$ skkdic-p2cdb SKK-JISYO.zipcode.cdb < SKK-JISYO.zipcode'
echo '**********************************************************'
echo ' '


%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.j ChangeLog NEWS README README.j
%{_sbindir}/multiskkserv*
%{_bindir}/skkdic-p2cdb




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 20051220-6mdv2011.0
+ Revision: 620419
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 20051220-5mdv2010.0
+ Revision: 430121
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 20051220-4mdv2009.0
+ Revision: 253354
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20051220-2mdv2008.1
+ Revision: 130367
- kill re-definition of %%buildroot on Pixel's request
- import multiskkserv


* Wed Dec 21 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20051220-2mdk
- new release
- fix post scripts (Thanks to Yukiko)

* Sun Dec 18 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20050928-1mdk
- first spec for Mandriva Linux
