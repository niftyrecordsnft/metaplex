import json
import os
import random
import iso8601
import shutil

numberOfFiles = 1000
creatorAddress = "BjLKxBKRUjFX3WyfyTcTtotC5TfRaPJgVjEeMn1MuzPd"

# Build Blockchain JSON
for x in range(numberOfFiles):

    nftNumber = x + 1
    niftyRecordNFTData = {
        "name" : "NiftyRecord #" + str(nftNumber),
        "symbol": "NFRC",
        "uri" : "https://assets.niftyrecordsnft.com/niftyrecords/" + str(nftNumber) + "/NiftyRecord-" + str(nftNumber) + ".json",
        "image": "https://assets.niftyrecordsnft.com/niftyrecords/" + str(nftNumber) + "/NiftyRecord-" + str(nftNumber) + ".png",
        "properties": {
            "files": [
                {
                    "uri": "https://assets.niftyrecordsnft.com/niftyrecords/" + str(nftNumber) + "/NiftyRecord-" + str(nftNumber) + ".png",
                    "type": "image/png"
                }
            ],
            "category": "image",
            "creators": [
                {
                    "address": creatorAddress,
                    "share": 100
                }
            ]
        },
        "seller_fee_basis_points": 750
    }

    # When generating blockchain JSON
    with open('blockchain/' + str(x) + '.json', 'w') as f:
        json.dump(niftyRecordNFTData, f)

    # Paste in temporary white placeholder image
    shutil.copyfile('sleeves/white.png', 'blockchain/' + str(x) + '.png')


unrevealedSleeves = [
    {
        "name" : "White",
        "rangeStart": 1, 
        "rangeEnd": 40,
        "imagePath":"sleeves/white.png",
        "revealDate": "2022-03-28T21:00:00-04:00"
    },
    {
        "name" : "Black",
        "rangeStart": 41, 
        "rangeEnd": 70,
        "imagePath":"sleeves/black.png",
        "revealDate": "2022-03-28T20:00:00-04:00"
    },
    {
        "name" : "Silver",
        "rangeStart": 71, 
        "rangeEnd": 90,
        "imagePath":"sleeves/silver.png",
        "revealDate": "2022-03-28T19:00:00-04:00"
    },
    {
        "name" : "Gold",
        "rangeStart": 91, 
        "rangeEnd": 100,
        "imagePath":"sleeves/gold.png",
        "revealDate": "2022-03-28T18:00:00-04:00"
    }
]

generatedWhiteSleeves = 0
maxWhiteSleeves = numberOfFiles * 0.4
print("maxWhiteSleeves")
print(maxWhiteSleeves)

generatedBlackSleeves = 0
maxBlackSleeves = numberOfFiles * 0.3
print("maxBlackSleeves")
print(maxBlackSleeves)

generatedSilverSleeves = 0
maxSilverSleeves = numberOfFiles * 0.2
print("maxSilverSleeves")
print(maxSilverSleeves)

generatedGoldSleeves = 0
maxGoldSleeves = numberOfFiles * 0.1
print("maxGoldSleeves")
print(maxGoldSleeves)

# Build server unrevealed metadata JSON
for x in range(numberOfFiles):

    # Determine record sleeve
    # TODO: Increment generated number and ensure that we haven't gone over the allowed amount of sleeves for this limit
    thisSleeve = unrevealedSleeves[0] # default to the white sleeve

    while True:
        # Generate a random number between 1 and 100
        randomNumber = random.randint(1, 100)
        # Find the associated sleeve to this percent value
        for sleeve in unrevealedSleeves:
            if randomNumber > sleeve["rangeStart"] and randomNumber < sleeve["rangeEnd"]:
                thisSleeve = sleeve

        if thisSleeve["name"] == "White":
            if generatedWhiteSleeves < maxWhiteSleeves:
                generatedWhiteSleeves += 1
                break
            else:
                # Hit max number of sleeve, try once again
                print("Hit max white sleeves, trying again")
                continue

        elif thisSleeve["name"] == "Black":
            if generatedBlackSleeves < maxBlackSleeves:
                generatedBlackSleeves += 1
                break
            else:
                # Hit max number of sleeve, try once again
                print("Hit max black sleeves, trying again")
                continue

        elif thisSleeve["name"] == "Silver":
            if generatedSilverSleeves < maxSilverSleeves:
                generatedSilverSleeves += 1
                break
            else:
                # Hit max number of sleeve, try once again
                print("Hit max silver sleeves, trying again")
                continue
        
        elif thisSleeve["name"] == "Gold":
            if generatedGoldSleeves < maxGoldSleeves:
                generatedGoldSleeves += 1
                break
            else:
                # Hit max number of sleeve, try once again
                print("Hit max gold sleeves, trying again")
                continue

    print("thisSleeve")
    print(thisSleeve)

    nftNumber = x + 1
    niftyRecordNFTData = {
        "id" : nftNumber,
        "name" : "NiftyRecord #" + str(nftNumber),
        "symbol": "NFRC",
        "image": "https://assets.niftyrecordsnft.com/niftyrecords/" + str(nftNumber) + "/NiftyRecord-" + str(nftNumber) + ".png",
        "description": "This is NiftyRecords #" + str(nftNumber) + "!",
        "attributes": [
            {
                "trait_type": "Opened",
                "value": "No"
            },
            {
                "trait_type": "Record Sleeve",
                "value": thisSleeve["name"]
            }
        ],
        "collection": {
        "name": "NiftyRecords",
        "family": "NiftyRecords"
        },
        "revealed": False,
        "revealAfter": iso8601.parse_date(thisSleeve["revealDate"]).timestamp()
    }

    fileName = 'server/' + str(nftNumber) + "/NiftyRecord-" + str(nftNumber) + '.json'
    os.makedirs(os.path.dirname(fileName), exist_ok=True)

    # When generating server-JSON
    with open(fileName, 'w') as f:
        json.dump(niftyRecordNFTData, f)

    #Copy in the respective sleeve image that corresponds to the choice
    shutil.copyfile(thisSleeve["imagePath"], 'server/' + str(nftNumber) + '/NiftyRecord-' + str(nftNumber) + '.png')
