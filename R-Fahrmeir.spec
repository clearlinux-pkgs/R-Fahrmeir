#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Fahrmeir
Version  : 2016.5.31
Release  : 37
URL      : https://cran.r-project.org/src/contrib/Fahrmeir_2016.5.31.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Fahrmeir_2016.5.31.tar.gz
Summary  : Data from the Book "Multivariate Statistical Modelling Based on
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
Modelling Based on Generalized Linear Models", first edition, by 
              Ludwig Fahrmeir and Gerhard Tutz.  Useful when using the book.

%prep
%setup -q -c -n Fahrmeir
cd %{_builddir}/Fahrmeir

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641010851

%install
export SOURCE_DATE_EPOCH=1641010851
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Fahrmeir
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Fahrmeir
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Fahrmeir
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Fahrmeir || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Fahrmeir/DESCRIPTION
/usr/lib64/R/library/Fahrmeir/INDEX
/usr/lib64/R/library/Fahrmeir/Meta/Rd.rds
/usr/lib64/R/library/Fahrmeir/Meta/data.rds
/usr/lib64/R/library/Fahrmeir/Meta/features.rds
/usr/lib64/R/library/Fahrmeir/Meta/hsearch.rds
/usr/lib64/R/library/Fahrmeir/Meta/links.rds
/usr/lib64/R/library/Fahrmeir/Meta/nsInfo.rds
/usr/lib64/R/library/Fahrmeir/Meta/package.rds
/usr/lib64/R/library/Fahrmeir/NAMESPACE
/usr/lib64/R/library/Fahrmeir/NEWS
/usr/lib64/R/library/Fahrmeir/data/Rdata.rdb
/usr/lib64/R/library/Fahrmeir/data/Rdata.rds
/usr/lib64/R/library/Fahrmeir/data/Rdata.rdx
/usr/lib64/R/library/Fahrmeir/data/datalist
/usr/lib64/R/library/Fahrmeir/help/AnIndex
/usr/lib64/R/library/Fahrmeir/help/Fahrmeir.rdb
/usr/lib64/R/library/Fahrmeir/help/Fahrmeir.rdx
/usr/lib64/R/library/Fahrmeir/help/aliases.rds
/usr/lib64/R/library/Fahrmeir/help/paths.rds
/usr/lib64/R/library/Fahrmeir/html/00Index.html
/usr/lib64/R/library/Fahrmeir/html/R.css
