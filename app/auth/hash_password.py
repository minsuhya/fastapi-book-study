#!/usr/bin/env python
# -*- coding: utf-8 -*-

# password를 암호화하는 함수가 포합된다.
# 이 함수는 계정을 등록할 때 또는 로그인 시 패스워드 비교에 사용

import hashlib


class HashPassword():
    # create_hash
    def create_hash(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()

    # verify_hash
    def verify_hash(self, password: str, hashed_password: str):
        if self.create_hash(password) == hashed_password:
            return True
        return False
