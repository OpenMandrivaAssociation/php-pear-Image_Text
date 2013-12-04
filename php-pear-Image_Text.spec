%define		_class		Image
%define		_subclass	Text
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.7.0
Release:	1
Summary:	Comfortable processing of texts in images
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Image_Text/
Source0:	http://download.pear.php.net/package/Image_Text-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This class allows you to add text to dynamic generated images more
comfortable. It allows you to process multiline text and manipulate:
- Border
- Shading
- Alignment
Another nice feature is to let the class measurize your text in respect
to font size and line splitting to fit a given text box.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean


%files
# %doc %{upstream_name}-%{version}/example 
# %doc %{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/packages/%{upstream_name}.xml
%{php_pear_dir}/Image/Text/Exception.php
