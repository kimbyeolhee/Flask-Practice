# flask blueprint

- 한 파일에 모든 기능 코드를 넣으면 복잡하고 관리가 어려움
- 재사용성을 생각해야 함

## flask 백엔드 구조

- 기능별로 폴더/파일 구분(blueprint를 사용해서 기능별로 추가/삭제가 용이하도록 구성)
- MVC에서 M은 데이터베이스/데이터 모델, C는 API (View는 프론트엔드 별도 구축)

# flask blueprint

- 여러 소스 파일에 flask 코드를 작성할 수 있도록 하는 기능

```python
from flask import Flask
from 하위폴더명 import 하위폴더의 소스파일 명

app = Flask(__name__)
app.register_blueprint(하위폴더의 소스파일 명.블루프린트객체이름, url_prefix='기본경로명')
```

```python
# app.register_blueprint(하위폴더의 소스파일 명.블루프린트객체이름, url_prefix='/blog')일 경우

from flask import Blueprint
# 블루프린트객체이름
blog_abtest = Blueprint('blog', __name__)

# URL/기본경로명/라우팅경로
# http://localhost:8080/blog/blog1
@blog_abtest.route('/blog1')
def blog():
  return "blueprint"
```
