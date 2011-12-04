Name: hunspell-hi
Summary: Hindi hunspell dictionaries
Version: 20050726
Release: 6%{?dist}
Source: http://hunspell.sourceforge.net/hi-demo.tar.gz
Group: Applications/Text
URL: http://hunspell.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Hindi hunspell dictionaries.

%prep
%setup -q -c -n hi-demo
iconv -f ISO-8859-1 -t UTF-8 hi/Copyright > hi/Copyright.utf8
mv hi/Copyright.utf8 hi/Copyright

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
mv hi/hi.dic hi/hi_IN.dic
mv hi/hi.aff hi/hi_IN.aff
cp -p hi/*.dic hi/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc hi/README hi/COPYING hi/Copyright
%{_datadir}/myspell/*

%changelog
* Thu Feb 18 2010 Parag <pnemade AT redhat.com> - 20050726-6
- Resolves:rh#566340: Fix Copyright encoding issue in %%prep

* Thu Feb 18 2010 Parag <pnemade AT redhat.com> - 20050726-5.1
- Resolves:rh#566340: Spec file cleanup

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20050726-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 06 2008 Parag <pnemade@redhat.com> - 20050726-2
- Added Copyright

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20050726-1
- Initial Fedora release
