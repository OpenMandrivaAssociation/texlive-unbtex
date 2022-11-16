Name:		texlive-unbtex
Version:	64634
Release:	1
Summary:	A class for theses at University of Brasilia (UnB)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unbtex
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unbtex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unbtex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a class based on abnTeX and compatible
with pdflatex and biber to prepare bachelor, master, and
doctoral theses for the University of Brasilia (UnB), Brazil.
The class also comes with a template for the various types of
theses for undergraduate and graduate programs at UnB. The
documentation for the class and the comments in the templates
are all written in Portuguese, the language of the target
audience.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/unbtex
%doc %{_texmfdistdir}/doc/latex/unbtex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
