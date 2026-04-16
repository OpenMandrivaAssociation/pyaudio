%define module PyAudio

Name:		pyaudio
Summary:	Python bindings for PortAudio v19
Version:	0.2.14
Release:	1
License:	MIT
Group:		System/Libraries
URL:		https://people.csail.mit.edu/hubert/pyaudio/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	gcc
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# For docs
BuildRequires:	python%{pyver}dist(sphinx)

%description
PyAudio provides Python bindings for PortAudio v19, the cross-platform audio
I/O library.

With PyAudio, you can easily use Python to play and record audio on a
variety of platforms.

%prep -a
# Remove bundled egg-info
rm -rf src/%{module}.egg-info

# module fails to build with clang / lld due to hardcoded /usr/lib paths on
# ln118 in setup.py, remove them with sed.
sed -i '/external_libraries_path += \[\x27\/usr\/local\/lib\x27, \x27\/usr\/lib\x27\]/d' setup.py

%build -p
export LDFLAGS="%{ldflags} -lpython%{py_ver}"

%install -a
# Docs require the built module installed in order to build.
PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}" sphinx-build -b html sphinx/ %{buildroot}%{_docdir}/%{name}
# Remove build artifact
rm -rf %{buildroot}%{_docdir}/%{name}/{.buildinfo,.doctrees}

%files
%doc README.md CHANGELOG
%{_docdir}/%{name}/*
%{python_sitearch}/%{name}
%{python_sitearch}/%{name}-%{version}.dist-info
