%global tl_name unbtex
%global tl_revision 79382

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6.6
Release:	%{tl_revision}.1
Summary:	A class for theses at University of Brasilia (UnB)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unbtex
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unbtex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unbtex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a class based on abnTeX and compatible with
pdflatex and BibTeXr to prepare bachelor, master, and doctoral theses
for the University of Brasilia (UnB), Brazil. The class also comes with
a template for the various types of theses for undergraduate and
graduate programs at UnB. The documentation for the class and the
comments in the templates are all written in Portuguese, the language of
the target audience.

