%global tl_name dialogl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros for constructing interactive LaTeX scripts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dialogl
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dialogl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dialogl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dialogl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Gathers together a bunch of code and examples about how to write macros
to carry on a dialogue with the user.

