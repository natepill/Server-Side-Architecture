from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    SMALL = 'SM'
    MEDIUM = 'MD'
    LARGE = 'LG'
    SIZE = (
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large')
    )
    size = models.CharField(
        max_length=2,
        choices=SIZE,
        default=SMALL,
    )
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)


    @property
    def get_price(self):
        return self.size

    @get_price.setter
    def set_price(self, size):
       if size == 'small':
           self.price = 10.30

       elif size == 'medium':
           self.price = 15.30

       elif size == 'large':
           self.prize = 20.30

       return self.price

class Topping(models.Model):

    name = models.CharField(max_length=200)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
