#
# Conditional build:
%bcond_without	latex	# LaTeX fonts
#
Summary:	Collection of Thai scalable fonts
Summary(pl.UTF-8):	Kolekcja skalowalnych fontów tajskich
Name:		fonts-thai-scalable
Version:	0.5.0
Release:	1
License:	MIT (Waree font), GPL v2+ (the rest)
Group:		Fonts
Source0:	http://linux.thai.net/pub/thailinux/software/thaifonts-scalable/fonts-tlwg-%{version}.tar.gz
# Source0-md5:	e407df4a9652aa1555e3dd5894d6ddd8
URL:		http://linux.thai.net/projects/thaifonts-scalable
BuildRequires:	fontforge >= 20080110
BuildRequires:	xorg-app-mkfontscale
%if %{with latex}
BuildRequires:	texlive
BuildRequires:	thailatex >= 0.4.6
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
thaifonts-scalable is a collection of Thai scalable fonts available in
free licenses. Its goal is to provide fonts that conform to existing
standards and recommendations, so that it can be a reference
implementation.

%description -l pl.UTF-8
thaifonts-scalable to kolekcja fontów skalowalnych dostępnych na
wolnych licencjach. Celem pakietu jest dostarczenie fontów zgodnych z
istniejącymi standardami i rekomendacjami, aby był implementacją
wzorcową.

%package -n fonts-OTF-thai
Summary:	Collection of OpenType Thai scalable fonts
Summary(pl.UTF-8):	Kolekcja skalowalnych fontów tajskich w formacie OpenType
Group:		Fonts
Requires(post,postun):	fontpostinst

%description -n fonts-OTF-thai
thaifonts-scalable is a collection of Thai scalable fonts available in
free licenses. Its goal is to provide fonts that conform to existing
standards and recommendations, so that it can be a reference
implementation.

This package contains fonts in OpenType format.

%description -n fonts-OTF-thai -l pl.UTF-8
thaifonts-scalable to kolekcja fontów skalowalnych dostępnych na
wolnych licencjach. Celem pakietu jest dostarczenie fontów zgodnych z
istniejącymi standardami i rekomendacjami, aby był implementacją
wzorcową.

Ten pakiet zawiera fonty w formacie OpenType.

%package -n fonts-TTF-thai
Summary:	Collection of TrueType Thai scalable fonts
Summary(pl.UTF-8):	Kolekcja skalowalnych fontów tajskich w formacie TrueType
Group:		Fonts
Requires(post,postun):	fontpostinst

%description -n fonts-TTF-thai
thaifonts-scalable is a collection of Thai scalable fonts available in
free licenses. Its goal is to provide fonts that conform to existing
standards and recommendations, so that it can be a reference
implementation.

This package contains fonts in TrueType format.

%description -n fonts-TTF-thai -l pl.UTF-8
thaifonts-scalable to kolekcja fontów skalowalnych dostępnych na
wolnych licencjach. Celem pakietu jest dostarczenie fontów zgodnych z
istniejącymi standardami i rekomendacjami, aby był implementacją
wzorcową.

Ten pakiet zawiera fonty w formacie TrueType.

%package -n fonts-Type1-thai
Summary:	Collection of Type1 Thai scalable fonts
Summary(pl.UTF-8):	Kolekcja skalowalnych fontów tajskich w formacie Type1
Group:		Fonts
Requires(post,postun):	fontpostinst

%description -n fonts-Type1-thai
thaifonts-scalable is a collection of Thai scalable fonts available in
free licenses. Its goal is to provide fonts that conform to existing
standards and recommendations, so that it can be a reference
implementation.

This package contains fonts in Type1 format.

%description -n fonts-Type1-thai -l pl.UTF-8
thaifonts-scalable to kolekcja fontów skalowalnych dostępnych na
wolnych licencjach. Celem pakietu jest dostarczenie fontów zgodnych z
istniejącymi standardami i rekomendacjami, aby był implementacją
wzorcową.

Ten pakiet zawiera fonty w formacie Type1.

%package -n thailatex-fonts
Summary:	Collection of Thai scalable fonts for LaTeX
Summary(pl.UTF-8):	Kolekcja skalowalnych fontów tajskich dla LaTeXa
Group:		Fonts
Requires(post,postun):	texlive
Requires:	texlive
Requires:	thailatex >= 0.4.7

%description -n thailatex-fonts
thaifonts-scalable is a collection of Thai scalable fonts available in
free licenses. Its goal is to provide fonts that conform to existing
standards and recommendations, so that it can be a reference
implementation.

This package contains LaTeX fonts for use with thailatex.

%description -n thailatex-fonts -l pl.UTF-8
thaifonts-scalable to kolekcja fontów skalowalnych dostępnych na
wolnych licencjach. Celem pakietu jest dostarczenie fontów zgodnych z
istniejącymi standardami i rekomendacjami, aby był implementacją
wzorcową.

Ten pakiet zawiera fonty LaTeXowe do używania z pakietem thailatex.

%prep
%setup -q -n fonts-tlwg-%{version}

%build
%configure \
	%{?with_latex:--enable-latex} \
	--enable-pfb \
	--enable-otf \
	--with-otfdir=%{_fontsdir}/OTF \
	--with-ttfdir=%{_fontsdir}/TTF \
	--with-type1dir=%{_fontsdir}/Type1
%{__make} %{?with_latex:-j1}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_fontsdir}/Type1/afm
mv $RPM_BUILD_ROOT%{_fontsdir}/Type1/*.afm $RPM_BUILD_ROOT%{_fontsdir}/Type1/afm
mkfontscale -o $RPM_BUILD_ROOT%{_fontsdir}/Type1/fonts.scale.thai-scalable $RPM_BUILD_ROOT%{_fontsdir}/Type1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n fonts-OTF-thai
fontpostinst OTF

%postun	-n fonts-OTF-thai
fontpostinst OTF

%post	-n fonts-TTF-thai
fontpostinst TTF

%postun	-n fonts-TTF-thai
fontpostinst TTF

%post	-n fonts-Type1-thai
fontpostinst Type1

%postun	-n fonts-Type1-thai
fontpostinst Type1

%post	-n thailatex-fonts
umask 022
%{_bindir}/texhash

%postun	-n thailatex-fonts
umask 022
%{_bindir}/texhash

%files -n fonts-OTF-thai
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_fontsdir}/OTF/Garuda*.otf
%{_fontsdir}/OTF/Kinnari*.otf
%{_fontsdir}/OTF/Loma*.otf
%{_fontsdir}/OTF/Norasi*.otf
%{_fontsdir}/OTF/Purisa*.otf
%{_fontsdir}/OTF/Sawasdee*.otf
%{_fontsdir}/OTF/Tlwg*.otf
%{_fontsdir}/OTF/Umpush*.otf
%{_fontsdir}/OTF/Waree*.otf

%files -n fonts-TTF-thai
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog ChangeLog.thai-ttf NEWS README TODO
%{_fontsdir}/TTF/Garuda*.ttf
%{_fontsdir}/TTF/Kinnari*.ttf
%{_fontsdir}/TTF/Loma*.ttf
%{_fontsdir}/TTF/Norasi*.ttf
%{_fontsdir}/TTF/Purisa*.ttf
%{_fontsdir}/TTF/Sawasdee*.ttf
%{_fontsdir}/TTF/Tlwg*.ttf
%{_fontsdir}/TTF/Umpush*.ttf
%{_fontsdir}/TTF/Waree*.ttf
/etc/fonts/conf.avail/64-ttf-thai-tlwg.conf
/etc/fonts/conf.avail/89-ttf-thai-tlwg-synthetic.conf

%files -n fonts-Type1-thai
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_fontsdir}/Type1/Garuda*.pfb
%{_fontsdir}/Type1/Kinnari*.pfb
%{_fontsdir}/Type1/Loma*.pfb
%{_fontsdir}/Type1/Norasi*.pfb
%{_fontsdir}/Type1/Purisa*.pfb
%{_fontsdir}/Type1/Sawasdee*.pfb
%{_fontsdir}/Type1/Tlwg*.pfb
%{_fontsdir}/Type1/Umpush*.pfb
%{_fontsdir}/Type1/Waree*.pfb
%{_fontsdir}/Type1/fonts.scale.thai-scalable
%{_fontsdir}/Type1/afm/Garuda*.afm
%{_fontsdir}/Type1/afm/Kinnari*.afm
%{_fontsdir}/Type1/afm/Loma*.afm
%{_fontsdir}/Type1/afm/Norasi*.afm
%{_fontsdir}/Type1/afm/Purisa*.afm
%{_fontsdir}/Type1/afm/Sawasdee*.afm
%{_fontsdir}/Type1/afm/Tlwg*.afm
%{_fontsdir}/Type1/afm/Umpush*.afm
%{_fontsdir}/Type1/afm/Waree*.afm

%files -n thailatex-fonts
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_datadir}/texmf/fonts/afm/public/fonts-tlwg
%{_datadir}/texmf/fonts/enc/dvips/fonts-tlwg
%{_datadir}/texmf/fonts/map/dvips/fonts-tlwg
%{_datadir}/texmf/fonts/tfm/public/fonts-tlwg
%{_datadir}/texmf/fonts/type1/public/fonts-tlwg
%{_datadir}/texmf/fonts/vf/public/fonts-tlwg
%{_datadir}/texmf/tex/latex/fonts-tlwg
