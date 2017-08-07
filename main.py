import csv
import os
import pprint


ProductId = []
ProductInputPrice = []

def InputPriceReader():
  f = open('input_price.csv', 'rU' ) #open the file in read universal mode
  for line in f:
    InputPriceData = line.split(",")
    ProductId.append(InputPriceData[0]) #since we want the first, second and third column
    ProductInputPrice.append(InputPriceData[1])
    # ProductOutputPrice.append(cells[2].replace("\n", ""))
  f.close()
  return ProductId
  return ProductInputPrice

InputPriceReader()

# ============================================================
DateProductOut = []
ProductIdOut= []
ProductOutputPrice = []

def ReadOutputPrice():
  with open("today.csv", "rt") as f:
    reader = csv.reader(f)
    next(reader, None)  # skip the headers
    for line in f:
      OutputPriceData = line.split(",")
      DateProductOut.append(OutputPriceData[0])
      ProductIdOut.append(OutputPriceData[1]) #since we want the first, second and third column
      ProductOutputPrice.append(OutputPriceData[2].replace("\n", ""))
    ProductIdOut.append("")
    f.close()
ReadOutputPrice()

# ===================================================

DateProductOutList = []
ProductOutputPriceList = []
ProductInputPriceList = []
OutputPriceSumList = []
InputPriceSumList = []
SubPriceList = []

def FitData():
  ofile  = open('MonthData.csv', "wb")
  outputWriter = csv.writer(ofile, delimiter = ",")
  outputWriter.writerow(["Product Out ID", "Product Output Price", "Product Input Price", "Earning"])

  for i in range(0, len(ProductIdOut)):
    for j in range(len(ProductId)):
      if ProductId[j] == ProductIdOut[i]:
        DateProductOutList.append(DateProductOut[i])
        ProductOutputPriceList.append(ProductOutputPrice[i])
        ProductInputPriceList.append(ProductInputPrice[j])
      if (ProductIdOut[i] == ""):
        ProductOutputPriceList.append("")
        ProductInputPriceList.append("")
        break

  OutputSum = 0
  for x in ProductOutputPriceList:
    if x <> "":
      OutputSum = OutputSum + int(x)
    else:
      OutputPriceSumList.append(str(OutputSum))
      OutputSum = 0

  InputSum = 0
  for y in ProductInputPriceList:
    if y <> "":
      InputSum = InputSum + int(y)
    else:
      InputPriceSumList.append(str(InputSum))
      InputSum = 0

  for i in range(len(OutputPriceSumList)):
    SubPriceList.append(int(OutputPriceSumList[i]) - int(InputPriceSumList[i]))
  j=0
  for i in range(len(ProductIdOut)):
    if (ProductIdOut[i]<> ""):
      # outputWriter.writerow([DateProductOut[i], ProductIdOut[i], ProductOutputPriceList[i], ProductInputPriceList[i]])
      print "ssss"
    else:
      outputWriter.writerow(["", OutputPriceSumList[j], InputPriceSumList[j], SubPriceList[j]])
      # outputWriter.writerow(["\n"])
      j+=1
    # break
FitData()

print DateProductOutList
# print ProductIdOut
# print ProductOutputPriceList
# print ProductInputPriceList
# print OutputPriceSumList
# print InputPriceSumList
# print SubPriceList
