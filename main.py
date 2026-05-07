class Xislat:
    def __init__(self, qiymat):
        self._qiymat = qiymat

    @property
    def qiymat(self):
        return self._qiymat

    @qiymat.setter
    def qiymat(self, qiymat):
        if isinstance(qiymat, (int, float)):
            self._qiymat = qiymat
        else:
            raise TypeError("Qiymat faqat butun son yoki real son bo'lishi mumkin.")

class Xislat2:
    def __init__(self, qiymat):
        self.__qiymat = qiymat

    def get_qiymat(self):
        return self.__qiymat

    def set_qiymat(self, qiymat):
        if isinstance(qiymat, (int, float)):
            self.__qiymat = qiymat
        else:
            raise TypeError("Qiymat faqat butun son yoki real son bo'lishi mumkin.")

# Getter va setter metodlarini ishlatish
x = Xislat(10)
print(x.qiymat)  # 10

x.qiymat = 20
print(x.qiymat)  # 20

try:
    x.qiymat = "20"
except TypeError as e:
    print(e)  # Qiymat faqat butun son yoki real son bo'lishi mumkin.

x2 = Xislat2(10)
print(x2.get_qiymat())  # 10

x2.set_qiymat(20)
print(x2.get_qiymat())  # 20

try:
    x2.set_qiymat("20")
except TypeError as e:
    print(e)  # Qiymat faqat butun son yoki real son bo'lishi mumkin.
