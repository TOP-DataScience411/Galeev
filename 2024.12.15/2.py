from decimal import Decimal
from datetime import date, time, datetime
from numbers import Number

class PowerMeter:
    """
    Класс, которая описывает двухтарифный счётчик электроэнергии.
    """
    def __init__(self, tariff1: Number = 6.5,
                       tariff2: Number = 4.0,
                       tariff2_starts: int = 23,
                       tariff2_ends: int = 7):
        self.tariff1 = Decimal(tariff1)
        self.tariff2 = Decimal(tariff2)
        self.tariff2_starts = time(tariff2_starts)
        self.tariff2_ends = time(tariff2_ends)
        self.power = Decimal(0).quantize(Decimal('0.01'))
        self.charges: dict[date, Decimal] = {date.today(): Decimal(0)}

    def __repr__(self):
        """
        Специальный метод, который возвращает суммарную потреблённую мощность в машиночитаемом строковом представлении.
        """
        return f'<PowerMeter: {self.power} кВт/ч>'

    def __str__(self):
        """
        Специальный метод, который возвращает суммарную стоимость потреблённой мощности и месяц, в котором была потрачена электроэнергия, в человекочитаемом строковом представлении.
        """
        month = date.today().strftime('%b')
        return f'({month}) {self.charges[date.today()]}'

    def meter(self, power: Number) -> Decimal:
        """
        Функция, которая принимает значение потреблённой мощности, вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент
        """
        power = Decimal(power).quantize(Decimal('0.01'))
        self.power += power

        now = datetime.today().time()
        if self.tariff2_starts <= now or now <= self.tariff2_ends:
            current_tariff = self.tariff2
        else:
            current_tariff = self.tariff1

        daily_charge = power * current_tariff
        self.charges[date.today()] = self.charges.get(date.today(), Decimal(0)) + daily_charge
        return daily_charge.quantize(Decimal('0.01'))

        
# >>> pm1 = PowerMeter()
# >>> pm1.meter(2)
# Decimal('8.00')
# >>> pm1.meter(1.2)
# Decimal('4.80')
# >>> pm1
# <PowerMeter: 3.20 кВт/ч>
# >>> print(pm1)
# (Jan) 12.80        
                  