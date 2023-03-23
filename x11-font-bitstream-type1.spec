Name: x11-font-bitstream-type1
Version: 1.0.4
Release: 1
Summary: Xorg X11 font bitstream-type1
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-bitstream-type1-%{version}.tar.xz
License: MIT-like
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font bitstream-type1.

%prep
%autosetup -p1 -n font-bitstream-type1-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/Type1
%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/Type1/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/Type1/fonts.scale

%post
mkfontscale %{_datadir}/fonts/Type1
mkfontdir %{_datadir}/fonts/Type1

%postun
mkfontscale %{_datadir}/fonts/Type1
mkfontdir %{_datadir}/fonts/Type1

%files
%doc COPYING
%{_datadir}/fonts/Type1/c0*
