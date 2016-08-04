Name:           ros-jade-variant-topic-tools
Version:        0.1.3
Release:        0%{?dist}
Summary:        ROS variant_topic_tools package

Group:          Development/Libraries
License:        GNU Lesser General Public License (LGPL)
URL:            http://github.com/ethz-asl/ros-topic-variant
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-roscpp
Requires:       ros-jade-roslib
Requires:       ros-jade-variant-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-variant-msgs

%description
Topic tools for treating messages as variant types.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Aug 04 2016 Ralf Kaestner <ralf.kaestner@gmail.com> - 0.1.3-0
- Autogenerated by Bloom

