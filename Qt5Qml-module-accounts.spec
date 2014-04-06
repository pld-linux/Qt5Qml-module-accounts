Summary:	Ubuntu OnlineAccounts QML API
Summary(pl.UTF-8):	API języka QML do Ubuntu OnlineAccounts
Name:		Qt5Qml-module-accounts
Version:	0.4
Release:	1
License:	LGPL v2.1
Group:		Libraries
#Source0Download: http://code.google.com/p/accounts-sso/downloads/list
Source0:	http://accounts-sso.googlecode.com/files/accounts-qml-module-%{version}.tar.bz2
# Source0-md5:	ff337a0a2da65ecfeb5b842a120b61cc
URL:		http://code.google.com/p/accounts-sso/
BuildRequires:	Qt5Qml-devel >= 5
BuildRequires:	doxygen
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libaccounts-qt5-devel
BuildRequires:	libsignon-qt5-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
BuildRequires:	qt5-qtdeclarative >= 5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ubuntu OnlineAccounts QML API. It is part of the accounts-sso project.

%description -l pl.UTF-8
API języka QML do Ubuntu OnlineAccounts. Jest to część projektu
accounts-sso.

%package apidocs
Summary:	QML API documentation for Ubuntu OnlineAccounts
Summary(pl.UTF-8):	Dokumentacja API QML Ubuntu OnlineAccounts
Group:		Documentation

%description apidocs
QML API documentation for Ubuntu OnlineAccounts.

%description apidocs -l pl.UTF-8
Dokumentacja API QML Ubuntu OnlineAccounts.

%prep
%setup -q -n accounts-qml-module-%{version}

%build
qmake-qt5 accounts-qml-module.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_docdir}/qt5-doc
%{__mv} $RPM_BUILD_ROOT%{_datadir}/accounts-qml-module/doc $RPM_BUILD_ROOT%{_docdir}/qt5-doc/accounts-qml-module

# test
%{__rm} $RPM_BUILD_ROOT%{_bindir}/tst_plugin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/qml/Ubuntu
%dir %{_libdir}/qt5/qml/Ubuntu/OnlineAccounts
%attr(755,root,root) %{_libdir}/qt5/qml/Ubuntu/OnlineAccounts/libAccounts.so
%{_libdir}/qt5/qml/Ubuntu/OnlineAccounts/plugin.qmltypes
%{_libdir}/qt5/qml/Ubuntu/OnlineAccounts/qmldir

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/accounts-qml-module
