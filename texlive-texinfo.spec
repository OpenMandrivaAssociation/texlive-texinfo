# revision 27289
# category Package
# catalog-ctan /macros/texinfo/texinfo
# catalog-date 2012-07-07 16:36:49 +0200
# catalog-license gpl
# catalog-version 2012-06-05.14
Name:		texlive-texinfo
Version:	20120605.14
Release:	1
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


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120605.14-1
+ Revision: 812897
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080418.10-8
+ Revision: 805105
- Update to latest release.

* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080418.10-7
+ Revision: 790743
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080418.10-6
+ Revision: 772174
- Update to latest release.

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080418.10-5
+ Revision: 762736
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080418.10-4
+ Revision: 756626
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080418.10-3
+ Revision: 739922
- texlive-texinfo

* Mon Dec 05 2011 Zé <ze@mandriva.org> 20080418.10-2
+ Revision: 737795
- add missing scriplets requires
- rpm isnt able to handle = in conflicts

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080418.10-1
+ Revision: 719689
- texlive-texinfo
- texlive-texinfo
- texlive-texinfo

