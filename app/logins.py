# -*- coding: utf-8 -*-
#
# Copyright 2015 Ramil Nugmanov <stsouko@live.ru>
# This file is part of nmrdb.
#
# nmrdb is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
__author__ = 'stsouko'
from app import login_manager, db
from flask_login import UserMixin


@login_manager.user_loader
def load_user(userid):
    user = db.getuserbyid(userid)
    if user:
        return User(**user)

    return None


class User(UserMixin):
    def __init__(self, **kwargs):
        self.__id = kwargs['id']
        self.name = kwargs['fullname']
        self.__login = kwargs['name']
        self.__active = kwargs['active']
        self.__role = kwargs['role']
        self.__lab = kwargs['lab']

    def is_active(self):
        return self.__active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_id(self):
        return self.__id

    def get_role(self):
        return self.__role

    def get_login(self):
        return self.__login

    def get_lab(self):
        return self.__lab

