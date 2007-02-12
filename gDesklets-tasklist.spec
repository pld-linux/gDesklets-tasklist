
%define		pname	tasklist

Summary:	This is a simple display that embeds the GNOME tasklist via Bonobo
Summary(pl.UTF-8):   Prosty desklet osadzający pasek zadań GNOME poprzez Bonobo
Name:		gDesklets-%{pname}
Version:	0.10
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{pname}-desklet-%{version}.tar.bz2
# Source0-md5:	fc749acb2dfb3754e626d4c1d1eb05d5
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=80
BuildRequires:	python >= 2.3
BuildRequires:	python-pygtk-gtk >= 1.99.14
Requires:	gDesklets
Provides:	gDesklets-display
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_displaysdir	%{_datadir}/gdesklets/Displays

%description
This is a simple display that embeds the GNOME tasklist via Bonobo.
It floats on top of the other windows.

%description -l pl.UTF-8
Prosty desklet osadzający pasek zadań GNOME poprzez Bonobo. Umieszcza
się on na górze innych okien.

%prep
%setup -q -n %{pname}-desklet-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_displaysdir}/%{pname}

cp *.display $RPM_BUILD_ROOT%{_displaysdir}/%{pname}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_displaysdir}/*
