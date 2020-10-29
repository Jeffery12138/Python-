import csv
from datetime import datetime


class Temperature():
    """可视化日期、最高气温和最低气温的类"""
    def __init__(self, filename):
        """初始化"""
        self.filename = filename
        self.dates = []
        self.highs = []
        self.lows = []
        self.get_data()

    def get_data(self):
        """获取csv文件里的日期、最高气温和最低气温信息"""
        with open(self.filename) as f:
            reader = csv.reader(f)
            head_row = next(reader)

            for row in reader:
                try:
                    self.current_date = datetime.strptime(row[0], "%Y-%m-%d")
                    self.high = int(row[1])
                    self.low = int(row[3])
                except ValueError:
                    print(self.current_date, 'missing data')
                else:
                    self.dates.append(self.current_date)
                    self.highs.append(self.high)
                    self.lows.append(self.low)