code = {"a":"Lys", "m":"Pro", "i":"Asn", "*":"Met", "s":"Iso", "e":"His", "l":"Arg", "k":"Glu", "o":"Asp", "d":"Ala", "t":"Gly",  "r":"Val", "b":"Tyr", "c":"Ser", "g":"Spe", "n":"Trp", " ":" "}
lookup = [["Lys","AAA","AAG"],["Pro"],["Asn"],["Met"],["Iso"],["His"],["Arg"],["Ala"],["Gly"],["Val"],["Tyr"],["Ser"],["Spe"],["Glu"],["Trp"],[" "],["Asp"]]

string = "*I like small meese* said elias at a robotics meeting".lower()
returner = ""
for bag in string:
    print code[bag]
print code["i"]
