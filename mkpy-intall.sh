#!/usr/bin/env bash

# mkpy-install.sh -- Устанавливает в систему утилиту mkpy.py
# После инсталляции утилиту можно вызывать по упрощённому имени: mkpy
# 2019-21, Александр Жевак
# zhevak@mail.ru
# +7 (950) 194-4504


#rm /usr/bin/mkpy*
#rm /etc/alternatives/mkpy*
cp mkpy-0.2.8.py /usr/bin/
update-alternatives --install /usr/bin/mkpy mkpy /usr/bin/mkpy-0.2.8.py 5
