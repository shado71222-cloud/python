class Test_Pytest():

    def test_additive(self):
        print("test_login")
        a=2
        b=3
        assert a+b==5 ,"the summery is incorrect"


    def test_multiplicative(self):
        a=2
        b=3
        assert a*b==6 ,"the summery is incorrect"

    def test_divition(self):
        a=18
        b=3
        assert a//b==6 ,"the summery is incorrect"