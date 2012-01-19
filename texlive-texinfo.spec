# revision 25086
# category Package
# catalog-ctan /macros/texinfo/texinfo
# catalog-date 2008-04-21 10:16:51 +0200
# catalog-license gpl
# catalog-version 2008-04-18.10
Name:		texlive-texinfo
Version:	20080418.10
Release:	5
Summary:	Texinfo documentation system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/texinfo/texinfo
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texinfo.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Info is the preferred format for documentation in the GNU
project; the format may be used to produce online or printed
output from a single source. The Texinfo macros may be used to
produce printable output using TeX; other programs in the
distribution offer online interactive use (with hypertext
linkages in some cases). Note that a developers' snapshot of
the latest working version of the Texinfo macros may be found
in the Texinfo 'latest' package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/texinfo/texinfo.ini
%{_texmfdistdir}/tex/texinfo/texinfo.tex
%{_texmfdistdir}/tex/texinfo/txi-cs.tex
%{_texmfdistdir}/tex/texinfo/txi-de.tex
%{_texmfdistdir}/tex/texinfo/txi-en.tex
%{_texmfdistdir}/tex/texinfo/txi-es.tex
%{_texmfdistdir}/tex/texinfo/txi-fr.tex
%{_texmfdistdir}/tex/texinfo/txi-it.tex
%{_texmfdistdir}/tex/texinfo/txi-nb.tex
%{_texmfdistdir}/tex/texinfo/txi-nl.tex
%{_texmfdistdir}/tex/texinfo/txi-nn.tex
%{_texmfdistdir}/tex/texinfo/txi-pl.tex
%{_texmfdistdir}/tex/texinfo/txi-pt.tex
%{_texmfdistdir}/tex/texinfo/txi-ru.tex
%{_texmfdistdir}/tex/texinfo/txi-sr.tex
%{_texmfdistdir}/tex/texinfo/txi-tr.tex
%{_texmfdistdir}/tex/texinfo/txi-uk.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
