class Conversion:
    def decimal_to_octal(self,decimal):
        if decimal ==0:
            return '0'
        octal_value = ''
        while decimal>0:
            octal_value = str(decimal%8)+octal_value
            decimal//=8
        return octal_value

converter = Conversion()
print(converter.decimal_to_octal(456))
