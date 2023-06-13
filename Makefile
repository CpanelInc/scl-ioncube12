OBS_PROJECT := EA4
DISABLE_BUILD := arch=i586 repository=CentOS_6.5_standard
scl-php74-ioncube12-obs : DISABLE_BUILD += repository=CentOS_9 repository=xUbuntu_22.04
include $(EATOOLS_BUILD_DIR)obs-scl.mk
