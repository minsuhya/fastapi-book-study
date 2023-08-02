# FastAPI를 사용한 파이썬 웹 개발

- 예제코드: https://github.com/hanbit/web-with-fastapi
- 저자 블로그: https://www.youngest.dev
    - 몽고DB, JWT인증, 리액트를 활용한 FastApi App 구축 예제
    - https://testdriven.io/authors/adeshina
    - Okteto를 사용한 방명록 구축 가이드 및 동영상
    - https://www.okteto.com/blog/authors/abdulazeez-adeshina

# Test(pytest)
    - fixture: 반복되는 코드 제거
    $ pytest tests/test_login.py # import error 발생 가능 시 아래 문장을 실행
    $ python -m pytest tests/test_login.py

# Coverage Test
- 테스트를 실행하여 테스트 대상이 되는 코드의 비율을 파악
- 테스트 커버리지 보고서: 테스트가 전체 애플리케이션 코드 중 어느 정도 비율의 코드를 테스트하는지 정량화

    $ pip install coverage
    $ coverage run -m pytest # 보고서 생성
    $ coverage report
    $ coverage html

# 배포
- requirements.txt
- 환경변수 설정
- 의존 라이브러리 관리
