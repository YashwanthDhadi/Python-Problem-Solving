class Conversion :
    def octal_to_decimal(self,octal):
        power_value = 1
        decimal_value = 0
        while octal>0:
            decimal_value += (octal%10)*power_value
            power_value*=8
            octal//=10
        return decimal_value
    def decimal_to_binary(self,decimal):
        if decimal==0:
            return "0"
        binary_value = ''
        while decimal>0:
            binary_value = str(decimal%2)+binary_value
            decimal//=2
        return binary_value
    def octal_to_binary(self,decimal):
        decimal_value = self.octal_to_decimal(decimal)
        return self.decimal_to_binary(decimal_value)

converter = Conversion()
octal_number = 234
print(converter.octal_to_binary(octal_number))