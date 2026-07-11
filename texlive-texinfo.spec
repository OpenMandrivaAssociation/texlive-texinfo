%global tl_name texinfo
%global tl_revision 79244

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Texinfo documentation system
Group:		Publishing
URL:		https://www.ctan.org/pkg/texinfo
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texinfo.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Texinfo is the preferred format for documentation in the GNU project;
the format may be used to produce online or printed output from a single
source. The Texinfo macros may be used to produce printable output using
TeX; other programs in the distribution offer online interactive use
(with hypertext linkages in some cases). The latest release of the
texinfo.tex macros and texi2dvi and texi2pdf scripts may be found in the
texinfo-latest package, which are usually newer than the last full
release. CTAN does not hold any other Texinfo-related files; see its GNU
home page for downloads and other info.

