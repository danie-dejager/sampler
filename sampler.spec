%global commit 5da77618213bc6733efc1b585d8bbcbf1b486316

Name:           sampler
Version:        1.1.1
Release:        1%{?dist}
Summary:        Terminal dashboard for shell commands
License:        GPL-3.0-or-later
URL:            https://github.com/sqshq/sampler
Source0:        https://github.com/danie-dejager/sampler/archive/%{commit}.tar.gz

BuildRequires:  golang >= 1.26.0
Requires:       /bin/sh
Recommends:     alsa-lib

%description
Sampler is a terminal dashboard that periodically executes configured shell
commands and visualizes their output in charts, gauges, and text panels.

%prep
%autosetup -n sampler-%{commit}

%build
# Enable network access for the COPR build so Go can fetch modules pinned in go.sum.
export GOTOOLCHAIN=local
export GOPROXY=https://proxy.golang.org,direct
export CGO_ENABLED=0
go build -mod=readonly -buildmode=pie -trimpath -buildvcs=false -o sampler .

%check
export GOTOOLCHAIN=local
export GOPROXY=https://proxy.golang.org,direct
export CGO_ENABLED=0
go test -mod=readonly -buildvcs=false ./...

%install
install -Dpm0755 sampler %{buildroot}%{_bindir}/sampler

%files
%license LICENSE.md
%doc README.md
%{_bindir}/sampler
