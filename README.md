# jumpToPython
- - -
## study1
- - -
* 프롬프트로 파이썬 코드 작성.
* 세미콜론과 블럭을 쓰지 않는다.
* 들여쓰기 indentation 으로 블럭을 구분한다. 
* C 와 python 의 기본적인 문법 차이
* C++ 에서 bool true false 는 True False 대분자이다.
* 문자열 은 "" 과 '' 의 구분을 하지 않는다. 
* 문자형이 없다. char 
* 치환문에 의해서 타입이 결정이 되고 만들어진다.  a = 100
* 파이썬의 모든 자료들은 heap 에 저장된다.
* 파이썬의 자료형은 레퍼런스 카운트를 사용한다. 
* locals() 네임 스페이스의 모든 dictionary 를 반환.
* dir() 네임 스페이스의 이름만을 리스트로 반환.
* "\_\_dict__" 를 사용해서 네임 스페이스 반환.  
* 기본적인 연산 파일 만들기 triangle, circle, average
* f-string formatting
* 삼항 연산자 a if b else c
* if 문 각종 연산자 복습.
- - -
## study2
- - -
* 파이썬 특징 복습
* maxMidmin 작성. input().split() 사용. 
* 야구게임 baseball 파이썬으로 작성.
* 파이썬에서의 shallow copy deep copy 
* 대입 연산자는 shallow 
* [:] copy() 내부 원소는 shallow 지만 그 자체는 다른 주소. 
* copy.deepcopy() 는 내부 원소까지 deepcopy.
* mutable 한 객체 까지 복사 하지는 않는다.
- - -
## study3
- - -
* list 복습 list comprehension
* tuple 설명 기본.
* packing 과 unpacking 추가 설명.
* https://wikidocs.net/22801
* set 설명.
* gradCount program dictionary 활용.
* wordCount program file open 활용.
* dictionary 안의 value 값으로 크기 비교.
* python 으로 server client TCP 사용.
* https://realpython.com/python-sockets/ 참고.
- - -
## study4
- - -
* sum find 함수 작성
* 파라미터로 변수 받을 때의 주의 사항( 레퍼런스 와 포인터로 이해)
* 전역 변수 사용 global
* 클래스 선언
* 클래스 멤버의 private 설정 __ 과 _ 의 차이
* https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=amethyst_lee&logNo=221889506975
( 참고. )
* 상속 account Minus_account 만들기.
* 데코레이터 사용. abstractmethod, staticmethod, classmethod
- - -
## study5
- - -
* function overloading 파이썬에서는 기본적으로 안됨. 
* 비슷한 방식의 코딩은 디폴트 인자를 사용하거나 @dispatch 데코레이터를 사용.
http://daplus.net/python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%A8%EC%88%98-%EC%98%A4%EB%B2%84%EB%A1%9C%EB%94%A9/
  (참고)
* account.py 작성.
* __변수 와 _변수 의 차이점. private 접근.
* @property @name.setter 로 private 변수 접근.
* 패키지 만들기 __init__.py 의 역할
* 예외 처리 raise try: except : ... account2.py
* 내장함수( abs, all, any, chr, odr, divmod, enumerate, eval, filter hex, id, input, int, isinstace, issubclass, len, list, map, max, min, oct, open, pow, range, round, sorted, str, sum, tuple, type, zip)
* 라이브러리( sys, picke, os, shutil, glob, tempfile, time, calendar, random, webbrowser, threading)
- - -
## study6
- - -
* 정규표현식 
* 몇가지 예제, 파일 입출력, 조건식과 더하기 문제. 
* os.path.isdir os.path.isfile 함수가 제대로 동작 하지 않음... 이유 모름.
* html 문법 분석 xml.etree.ElementTree 사용.
* xml Element 를 이용해서 html 문서 작성하기. testXml3.py
* 기타 문제 풀기.