import re


class Passport:
    birthYear = ""
    issueYear = ""
    expiryYear = ""
    height = ""
    hairColour = ""
    eyeColour = ""
    passportId = ""
    countryid = ""

    hexMatch = re.compile(r'#[a-fA-F0-9]{6}$')

    valid = False

    def __init__(self, dictionary):
        self.birthYear = dictionary.get("byr")
        if self.birthYear is None or len(self.birthYear) != 4 or not self.birthYear.isnumeric() or not 1920 <= int(self.birthYear) <= 2002:
            return

        self.issueYear = dictionary.get("iyr")
        if self.issueYear is None or len(self.issueYear) != 4 or not self.issueYear.isnumeric() or not 2010 <= int(self.issueYear) <= 2020:
            return

        self.expiryYear = dictionary.get("eyr")
        if self.expiryYear is None or len(self.expiryYear) != 4 or not self.expiryYear.isnumeric() or not 2020 <= int(self.expiryYear) <= 2030:
            return

        self.height = dictionary.get("hgt")
        if self.height is None:
            return
        if not (self.height.endswith("cm") and 150 <= int(self.height[:-2]) <= 193):
            if not (self.height.endswith("in") and 59 <= int(self.height[:-2]) <= 76):
                return

        self.hairColour = dictionary.get("hcl")
        if self.hairColour is None or not Passport.hexMatch.match(self.hairColour):
            return

        self.eyeColour = dictionary.get("ecl")
        if self.eyeColour is None or self.eyeColour not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return

        self.passportId = dictionary.get("pid")
        if self.passportId is None or not self.passportId.isnumeric() or len(self.passportId) != 9:
            return

        self.countryId = dictionary.get("cid")

        self.valid = True
