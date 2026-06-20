class Conversion:
     def binary_to_decimal(self,binary):
          decimal = 0
          power_place = 1
          while binary>0:
               decimal+=(binary%10)*power_place
               power_place*=2
               binary//=10
          return decimal
     def decimal_to_octal(self,decimal):
          if decimal == 0:
               return "0"
          octal_value = ''
          while decimal>0:
              octal_value = str(decimal%8) + octal_value
              decimal//=8
          return octal_value
     def binary_to_octal(self,binary):
          decimal = self.binary_to_decimal(binary)
          return self.decimal_to_octal(decimal)


converter = Conversion()
n = 101011
print(converter.binary_to_octal(n))
