Name:    gem-jekyll-watch
Version: 2.2.1
Release: alt1

Summary: Rebuild your Jekyll site when a file changes with the `--watch` switch.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/jekyll/jekyll-watch

Packager:  Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch: noarch

Source:  %name-v%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Rebuild your Jekyll site when a file changes with the `--watch` switch.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %name.

%prep
%setup -n %name-v%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc *.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Mar 16 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 2.2.1-alt1
- initial build
