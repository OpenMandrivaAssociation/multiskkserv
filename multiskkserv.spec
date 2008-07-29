%define version	20051220
%define release	%mkrel 4

Name:		multiskkserv
Summary:	Simple skk multi-dictionary server
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Internationalization
URL:		http://www3.big.or.jp/~sian/linux/products/
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


