%define pkg_name PyAudio
Name:		pyaudio
Version:	0.2.4
Release:	2
License:	MIT
Url:		http://people.csail.mit.edu/hubert/pyaudio/
Source0:	http://people.csail.mit.edu/hubert/pyaudio/packages/%{name}-%{version}.tar.gz
Group:		System/Libraries
Summary:	Python bindings for PortAudio
BuildRequires:	portaudio-devel
BuildRequires:	python-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O
library. With PyAudio, you can easily use Python to play and record audio on
a variety of platforms. 

%prep
%setup -q -n %{pkg_name}-%{version}

# remove some pre-built binaries
rm -rf packaging

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README CHANGELOG docs
%{python_sitearch}/*.py*
%{python_sitearch}/*.so
%{python_sitearch}/*egg-info


%changelog
* Fri Oct 07 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.2.4-1
+ Revision: 703506
- first mandriva version
- Created package structure for 'pyaudio'.

