#!/bin/bash

source debian/vars.sh

set -x

export php_version=`echo "$scl" | perl -pe '$_ =~ s/^ea-php(\d)(\d)$/$1.$2/'`

echo "SCL :$scl:"
echo "PHP_VERSION :$php_version:\n";

export full_php_version=${php_version}.0

# The module itself
install -d -m 755 $DEB_INSTALL_ROOT${php_extdir}
install -m 755 ${full_php_version}/ioncube_loader_${version}.so $DEB_INSTALL_ROOT${php_extdir}

# The ini snippet
install -d -m 755 $DEB_INSTALL_ROOT${php_inidir}
cat > $DEB_INSTALL_ROOT${php_inidir}/${inifile} <<EOF
; Enable v12 IonCube Loader extension module
zend_extension="${php_extdir}/ioncube_loader_${version}.so"
EOF

mkdir -p ${DEB_INSTALL_ROOT}/opt/cpanel/$scl/root/usr/share/doc/${full_package_name}
cp LICENSE.txt ${DEB_INSTALL_ROOT}/opt/cpanel/$scl/root/usr/share/doc/${full_package_name}
cp README.txt ${DEB_INSTALL_ROOT}/opt/cpanel/$scl/root/usr/share/doc/${full_package_name}

echo "FILELIST"
find . -type f -print | sort


