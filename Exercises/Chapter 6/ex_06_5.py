text = "X-DSPAM-Confidence:    0.8475"

pos = text.find(':')

num = text[pos+2:]
num2 = float(num.lstrip())
print(num2)