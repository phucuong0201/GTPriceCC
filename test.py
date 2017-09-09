import csv
import os
import pprint


ProductId = []
ProductInputPrice = []

def InputPriceReader():
  f = open('input_price.csv', 'rU' )
  for line in f:
    InputPriceData = line.split(",")
    ProductId.append(InputPriceData[0])
    ProductInputPrice.append(int(InputPriceData[1]))
  f.close()
InputPriceReader()

# ============================================================

DateProductOut = []
ProductIdOut= []
NumberProductOut = []
ProductOutputPrice = []

filename = raw_input('Enter "Product Output Price" file name here: ')
def ReadOutputPrice():
  with open(filename, "rt") as f:
    reader = csv.reader(f)
    next(reader, None)  # skip the headers
    for line in f:
      OutputPriceData = line.split(",")
      DateProductOut.append(OutputPriceData[0])
      ProductIdOut.append(OutputPriceData[1].upper()) #since we want the first, second and third column

      if OutputPriceData[2] == "":
        NumberProductOut.append(1)
      else:
        NumberProductOut.append(int(OutputPriceData[2]))
      # ProductOutputPrice.append(OutputPriceData[3])

      if OutputPriceData[3] == "\n":
        ProductOutputPrice.append(0)
      else:
        ProductOutputPrice.append(int(OutputPriceData[3].replace("\n", "")))
    ProductIdOut.append("")

    f.close()
  while True:
    try:
      DateProductOut.remove("")
    except ValueError:
      break
ReadOutputPrice()

# ===================================================

ProductOutputPriceList = []
ProductInputPriceList = []
OutputPriceSumList = []
InputPriceSumList = []
SubPriceList = []

def FitData():
  ofile  = open('MonthData.csv', "wb")
  outputWriter = csv.writer(ofile, delimiter = ",")
  outputWriter.writerow(["Date", "Product Output Price", "Product Input Price", "Earning"])

  for i in range(0, len(ProductIdOut)):
    for j in range(len(ProductId)):
      if ProductId[j] == ProductIdOut[i]:
        ProductOutputPriceList.append(ProductOutputPrice[i] * NumberProductOut[i])
        ProductInputPriceList.append(ProductInputPrice[j] * NumberProductOut[i])
      if (ProductIdOut[i] == ""):
        ProductOutputPriceList.append("")
        ProductInputPriceList.append("")
        break

  OutputSum = 0
  for x in ProductOutputPriceList:
    if x <> '':
      OutputSum = OutputSum + x
    else:
      OutputPriceSumList.append(int(OutputSum))
      OutputSum = 0

  InputSum = 0
  for y in ProductInputPriceList:
    if y <> '':
      InputSum = InputSum + y
    else:
      InputPriceSumList.append(int(InputSum))
      InputSum = 0

  for i in range(len(OutputPriceSumList)):
    SubPriceList.append(OutputPriceSumList[i] - InputPriceSumList[i])

  j=0
  for i in range(len(ProductIdOut)):
    if (ProductIdOut[i]== ""):
      outputWriter.writerow([DateProductOut[j], OutputPriceSumList[j], InputPriceSumList[j], SubPriceList[j]])
      j+=1
FitData()

# print ProductId
# print ProductInputPrice

# print DateProductOut
print ProductIdOut
# print NumberProductOut
# print ProductOutputPrice
# print NumberProductOut
# print ProductInputPriceList
# print ProductOutputPriceList
# print OutputPriceSumList
# print InputPriceSumList
# print SubPriceList
