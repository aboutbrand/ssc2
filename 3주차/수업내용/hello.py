import requests # requests 라이브러리 설치 필요

def get_index(gu_name):
    data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    jdata = data.json()
    gu_infos = jdata['RealtimeCityAir']['row']
    for gu_info in gu_infos:
        if gu_info['MSRSTE_NM'] == gu_name:
            return gu_info['IDEX_MVL']
        return '옳바르지 않은 구 이름입니다.'

print(get_index('중구'))

# .strip() 함수를 사용하면 공백 문자를 인식하여 삭제한 데이터로 처리할 수 있다.

