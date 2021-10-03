Name:       exwm-xsession
Version:    1

# Release Start

Release:    1%{?dist}

# Release End

Summary:    EXWM xsession package
License:    MIT

%description
Puts a EXWM xsession file in %{\_datadir}/xsessions/exwm.desktop

%prep

%build
cat > emacs.desktop <<EOF
[Desktop Entry]
Name=Emacs
Exec=emacs
Type=Application
EOF

%install
mkdir -p %{buildroot}%{\_datadir}/xsessions
install -m 755 emacs.desktop %{buildroot}%{\_datadir}/xsessions/emacs.desktop

%files
/%{\_datadir}/xsessions/emacs.desktop

%changelog

