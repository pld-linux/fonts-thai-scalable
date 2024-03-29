#
# Conditional build:
%bcond_without	latex	# LaTeX fonts
#
Summary:	Collection of Thai scalable fonts
Summary(pl.UTF-8):	Kolekcja skalowalnych fontów tajskich
Name:		fonts-thai-scalable
Version:	0.7.3
Release:	2
License:	MIT (Waree font), GPL v2+ (the rest)
Group:		Fonts
Source0:	https://linux.thai.net/pub/thailinux/software/thaifonts-scalable/fonts-tlwg-%{version}.tar.xz
# Source0-md5:	d1de007dd0263acb0e64207b77df7f1c
URL:		https://linux.thai.net/projects/thaifonts-scalable
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	fontforge >= 20190801
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-fontforge >= 20190801
BuildRequires:	rpmbuild(macros) >= 1.751
BuildRequires:	xorg-app-mkfontscale
%if %{with latex}
# afm2tfm, vptovf, updmap-sys, mktexlsr
BuildRequires:	texlive
BuildRequires:	thailatex >= 0.4.6
%endif
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_latex:--enable-latex} \
	--enable-otf \
	--enable-pfb \
	--enable-ttf \
	--with-otfdir=%{_fontsdir}/OTF \
	--with-ttfdir=%{_fontsdir}/TTF \
	--with-type1dir=%{_fontsdir}/Type1
%{__make} %{?with_latex:-j1}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_fontsdir}/Type1/afm
%{__mv} $RPM_BUILD_ROOT%{_fontsdir}/Type1/*.afm $RPM_BUILD_ROOT%{_fontsdir}/Type1/afm
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
%texhash

%postun	-n thailatex-fonts
%texhash

%files -n fonts-OTF-thai
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_fontsdir}/OTF/Garuda*.otf
%{_fontsdir}/OTF/Kinnari*.otf
%{_fontsdir}/OTF/Laksaman*.otf
%{_fontsdir}/OTF/Loma*.otf
%{_fontsdir}/OTF/Norasi*.otf
%{_fontsdir}/OTF/Purisa*.otf
%{_fontsdir}/OTF/Sawasdee*.otf
%{_fontsdir}/OTF/Tlwg*.otf
%{_fontsdir}/OTF/Umpush*.otf
%{_fontsdir}/OTF/Waree*.otf

%files -n fonts-TTF-thai
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog ChangeLog.thai-ttf NEWS README
%{_fontsdir}/TTF/Garuda*.ttf
%{_fontsdir}/TTF/Kinnari*.ttf
%{_fontsdir}/TTF/Laksaman*.ttf
%{_fontsdir}/TTF/Loma*.ttf
%{_fontsdir}/TTF/Norasi*.ttf
%{_fontsdir}/TTF/Purisa*.ttf
%{_fontsdir}/TTF/Sawasdee*.ttf
%{_fontsdir}/TTF/Tlwg*.ttf
%{_fontsdir}/TTF/Umpush*.ttf
%{_fontsdir}/TTF/Waree*.ttf
%{_datadir}/fontconfig/conf.avail/64-??-tlwg-*.conf
%{_datadir}/fontconfig/conf.avail/64-15-laksaman.conf
%{_datadir}/fontconfig/conf.avail/89-tlwg-*-synthetic.conf

%files -n fonts-Type1-thai
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_fontsdir}/Type1/Garuda*.pfb
%{_fontsdir}/Type1/Kinnari*.pfb
%{_fontsdir}/Type1/Laksaman*.pfb
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
%{_fontsdir}/Type1/afm/Laksaman*.afm
%{_fontsdir}/Type1/afm/Loma*.afm
%{_fontsdir}/Type1/afm/Norasi*.afm
%{_fontsdir}/Type1/afm/Purisa*.afm
%{_fontsdir}/Type1/afm/Sawasdee*.afm
%{_fontsdir}/Type1/afm/Tlwg*.afm
%{_fontsdir}/Type1/afm/Umpush*.afm
%{_fontsdir}/Type1/afm/Waree*.afm

%files -n thailatex-fonts
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_datadir}/texmf/fonts/afm/public/fonts-tlwg
%{_datadir}/texmf/fonts/enc/dvips/fonts-tlwg
%{_datadir}/texmf/fonts/map/dvips/fonts-tlwg
%{_datadir}/texmf/fonts/opentype/public/fonts-tlwg
%{_datadir}/texmf/fonts/tfm/public/fonts-tlwg
%{_datadir}/texmf/fonts/type1/public/fonts-tlwg
%{_datadir}/texmf/fonts/vf/public/fonts-tlwg
%{_datadir}/texmf/tex/latex/fonts-tlwg
