# flask and logging

- logging 라이브러리와 함께 flask logging 기능 사용 가능
- 주요 logging handler

  - FileHandler : 파일로 로그를 저장
  - RotatingFileHandler : 파일로 로그를 저장하되, 파일이 정해진 사이즈를 넘어가면 새로운 파일로 생성
    - maxBytes = 하나의 파일 사이즈, backupCount = 파일 갯수
  - NTEventLogHandler : 윈도우 시스템 로그를 남김

  <br/>

  상용화 시에는 debug를 False로 설정하고 디버그 정보를 로그로 남김

  ```python
  app.run(host="127.0.0.1", port="8000", debug=False)
  ```

  ```python
  if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('test.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
  ```
