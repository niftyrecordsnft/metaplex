import json
import os

numberOfFiles = 10
# /Users/willmero/.config/solana/NiftyRecords_DevNetDeploy1.json
creatorAddress = "9ifxZqGBXBuTRSpiHxfuzapyrP2KLLGyeRLuEoGbwrde"

# Build Blockchain JSON
for x in range(numberOfFiles):

    nftNumber = x + 1
    niftyRecordNFTData = {
        "name" : "NiftyRecord #" + str(nftNumber),
        "symbol": "NFRC",
        "uri" : "https://assets.niftyrecordsnft.com/niftyrecords/" + str(nftNumber) + "/" + str(nftNumber) + "-metadata.json",
        "image": "https://assets.niftyrecordsnft.com/niftyrecords/" + str(nftNumber) + "/" + str(nftNumber) + "-main.png",
        "properties": {
            "files": [
                {
                    "uri": "https://assets.niftyrecordsnft.com/niftyrecords/" + str(nftNumber) + "/" + str(nftNumber) + "-main.png",
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

# Build server unrevealed metadata JSON
for x in range(numberOfFiles):

    nftNumber = x + 1
    niftyRecordNFTData = {
        "id" : nftNumber,
        "name" : "NiftyRecord #" + str(nftNumber),
        "symbol": "NFRC",
        "image": "https://assets.niftyrecordsnft.com/niftyrecords/" + str(nftNumber) + "/" + str(nftNumber) + "-main.png",
        "description": "This is NiftyRecords #" + str(nftNumber) + "!",
        "attributes": [
            {
                "trait_type": "Opened",
                "value": "No"
            }
        ],
        "collection": {
        "name": "NiftyRecords",
        "family": "NiftyRecords"
        },
        "revealed": False,
        "revealAfter": 1645916400000,
        "hasNiftyAdapter": False
    }

    fileName = 'server/' + str(nftNumber) + "/" + str(nftNumber) + '-metadata.json'
    os.makedirs(os.path.dirname(fileName), exist_ok=True)

    # When generating server-JSON
    with open(fileName, 'w') as f:
        json.dump(niftyRecordNFTData, f)
