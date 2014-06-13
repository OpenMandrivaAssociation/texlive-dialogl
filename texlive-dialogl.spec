# revision 28946
# category Package
# catalog-ctan /macros/latex/contrib/dialogl
# catalog-date 2013-01-25 11:22:08 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-dialogl
Version:	20130125
Release:	6
Summary:	Macros for constructing interactive LaTeX scripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dialogl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dialogl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dialogl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dialogl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Gathers together a bunch of code and examples about how to
write macros to carry on a dialogue with the user.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dialogl/dialog.sty
%{_texmfdistdir}/tex/latex/dialogl/grabhedr.sty
%{_texmfdistdir}/tex/latex/dialogl/listout.tex
%{_texmfdistdir}/tex/latex/dialogl/menus.sty
%doc %{_texmfdistdir}/doc/latex/dialogl/Makefile
%doc %{_texmfdistdir}/doc/latex/dialogl/README
%doc %{_texmfdistdir}/doc/latex/dialogl/cnvunits.tex
%doc %{_texmfdistdir}/doc/latex/dialogl/codialog.pdf
%doc %{_texmfdistdir}/doc/latex/dialogl/default.los
%doc %{_texmfdistdir}/doc/latex/dialogl/dia-driv.pdf
%doc %{_texmfdistdir}/doc/latex/dialogl/dia-driv.tex
%doc %{_texmfdistdir}/doc/latex/dialogl/dialogl-doc.sty
%doc %{_texmfdistdir}/doc/latex/dialogl/diatest.tex
%doc %{_texmfdistdir}/doc/latex/dialogl/fontmenu.lg
%doc %{_texmfdistdir}/doc/latex/dialogl/fontmenu.tex
%doc %{_texmfdistdir}/doc/latex/dialogl/manifest.txt
#- source
%doc %{_texmfdistdir}/source/latex/dialogl/dialogl.dtx
%doc %{_texmfdistdir}/source/latex/dialogl/dialogl.ins
%doc %{_texmfdistdir}/source/latex/dialogl/grabhedr.dtx
%doc %{_texmfdistdir}/source/latex/dialogl/listout.dtx
%doc %{_texmfdistdir}/source/latex/dialogl/menus.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
