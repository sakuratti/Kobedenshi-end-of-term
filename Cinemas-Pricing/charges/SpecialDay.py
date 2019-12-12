'''
特別割引適応
サービスデイ/毎月1日、16日/1200円
レディースデイ/毎週火曜日/1200円
夫婦割/二人で/2400円
シニア割/60歳以上/1200円
レイトショー/20:00以降/1300円
映画の日/12月1日/1000円
障害者/付き添い2名まで/1000円
'''

class SpecialDayPrice():
    def __init__(self):
        self.service = 1200
        self.ladies = 1200
        self.couple = 2400
        self.late = 1300
        self.cinema = 1000
        pass

def Watch3D(origin):
    return origin + 300 

