from StudentCard import StudentCard 

class MainShopCharger:

    # 学籍番号で指定した学生証を取得する
    def insertStudentCard(self, studentId):
        self.insertedStudentCard = StudentCard.getStudentCard(studentId)
    
    # 挿入している学生証にお金をチャージする
    def chargeMoney(self, money):
        if self.insertedStudentCard is not None:
            self.insertedStudentCard.setAccountBalance(self.insertedStudentCard.getAccountBalance() + money)
            self.printAccountBalance()
        else:
            print('学生証が挿入されていません')
    
    # コンソールに学生名と残高を表示する
    def printAccountBalance(self):
        print('残高を表示します')
        print('学生名: ' + self.insertedStudentCard.getStudentName())
        print('残高: ' + str(self.insertedStudentCard.getAccountBalance()))
    
    # main メソッド
    def main(self):
        # 学生証インスタンスの作成
        studentCard1 = StudentCard(0, 'tut')
        studentCard2 = StudentCard(1, 'tenpaku')
        
        # エラー処理の表示
        self.chargeMoney(200)
        # 学生証 1 枚目の挿入とチャージ
        self.insertStudentCard(0)
        # 加算
        self.chargeMoney(1000)
        # 引き出し
        self.chargeMoney(-300)
        # 学生証 2 枚目の挿入とチャージ
        self.insertStudentCard(1)
        # 加算
        self.chargeMoney(500)
        # 引き出し
        self.chargeMoney(-1000)


if __name__ == '__main__':
    mainInstance = MainShopCharger()
    mainInstance.insertedStudentCard = None  # インスタンス変数: 挿入されている学生証
    mainInstance.main()
