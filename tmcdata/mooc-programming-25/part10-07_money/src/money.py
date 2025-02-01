# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02} eur"
    
    def __eq__(self, another):
        return (self._euros == another._euros and self._cents == another._cents)

    def __lt__(self, another):
        return (self._euros + self._cents / 100) < (another._euros + another._cents / 100)

    def __gt__(self, another):
        return (self._euros + self._cents / 100) > (another._euros + another._cents / 100)
    
    def __ne__(self, another):
        return (self._euros + self._cents / 100) != (another._euros + another._cents / 100)

    def __add__(self, another):
        new = Money(0, 0)
        new._euros = self._euros + another._euros
        new._cents = self._cents + another._cents
        if new._cents >= 100:
            new._cents -= 100
            new._euros += 1
        return (new)

    def __sub__(self, another):
        sub = Money(0, 0)
        sub._euros = self._euros - another._euros
        sub._cents = self._cents - another._cents
        if sub._cents < 0:
            sub._cents += 100
            sub._euros -= 1
        if sub._euros < 0:
            raise ValueError("a negative result is not allowed")
        return (sub)


if __name__ == "__main__":
    e1 = Money(4, 5)

    print(e1)
    e1.euros = 1000
    print(e1)