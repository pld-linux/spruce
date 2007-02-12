Summary:	Spruce - a GTK+-based e-mail client supporting local spools, POP3 and IMAP
Summary(pl.UTF-8):	Spruce - oparty na GTK+ klient poczty obsługujący skrzynki lokalne, POP3 i IMAP
Name:		spruce
Version:	0.7.7
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/spruce/%{name}-%{version}.tar.gz
# Source0-md5:	de46fc100806a7d2d24e5ebdb8d751c1
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://spruce.sourceforge.net/
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1.2.7
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	libglade-devel
BuildRequires:	perl-base
Requires:	glib >= 1.2.7
Requires:	gtk+ >= 1.2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spruce is a GTK+-based e-mail client designed to provide all of the
basic features people have grown to need. Spruce may be used to
receive mail from local mail spools, POP3 accounts and IMAP accounts.
PGP and GNU Privacy Guard are supported for secure, encrypted
communications. MIME attachment support and a powerful filtering
capability (including plain text matching, regular expressions support
and shell wildcards) help to make Spruce a powerful tool. Its simple
GUI design and available set of NLS translations make spruce an
easy-to-use tool for everyone.

%description -l pl.UTF-8
Spruce to oparty na GTK+ klient poczty elektronicznej zaprojektowany
aby dostarczyć wszystkie podstawowe możliwości, które zaczęły być
ludziom potrzebne. Spruce'a można używać do odbierania poczty z
lokalnych skrzynek (spooli) pocztowych, kont POP3 i kont IMAP.
Program obsługuje PGP i GNU Privacy Guarda dla zapewnienia
bezpiecznej, szyfrowanej komunikacji. Obsługa załączników MIME i duże
możliwości filtrowania (włącznie z dopasowywaniem czystego tekstu,
obsługą wyrażeń regularnych i masek powłoki) pomaga uczynić Spruce'a
potężnym narzędziem. Jego prosty projekt interfejsu graficznego i
dostępny zbiór tłumaczeń NLS czyni go prostym w użyciu programem dla
każdego.

%prep
%setup -q

mv -f po/{ru_RU,ru}.po
mv -f po/{zh_TW.Big5,zh_TW}.po

%{__perl} -pi -e 's/ru_RU/ru/;s/zh_TW\.Big5/zh_TW/' configure

%build
%configure \
	GPG=/usr/bin/gpg \
	--enable-pgp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DESIGN NEWS README README.SSL README.mbox README.tools THANKS TODO WISHLIST sprucesig.sample tools doc/html
%attr(755,root,root) %{_bindir}/spruce
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_mandir}/man1/spruce.1*
