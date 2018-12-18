class StudentCard:
    # クラス変数
    studentCardList = []  # 存在する学生証のリスト

    # 学籍番号, 学生名, 初期残高(¥0)を設定 + 学生証のインスタンスをリストに追加
    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName
        self.accountBalance = 0
        self.studentCardList.append(self)
    
    # 残高 accountBalance の値を取り出すための getter
    def getAccountBalance(self):
        return self.accountBalance
    
    # 残高 accountBalance の値を設定するための setter
    def setAccountBalance(self, accountBalance):
        self.accountBalance = accountBalance
    
    # 学生証を取得するための getter
    @classmethod
    def getStudentCard(cls, studentId):
        return cls.studentCardList[studentId]
    
    # 学生名を取得するための getter
    def getStudentName(self):
        return self.studentName
    