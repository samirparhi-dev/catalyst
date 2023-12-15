#!/bin/bash

set -e

echo -e "\n Important !!! This script only sign the file/Blobs"

echo -e "\n Please keep this script in the same folder where your file is located which intended to be signed"

echo -e "\n Provide the Name for the Private and Public Key e.g(my-key)"

read keyName

echo -e "\n Generating the Private and Public Key in Cosign..."

cosign generate-key-pair --output-key-prefix $keyName

echo -e "\n Enter the File Name which has to be signed"

read fileName

echo -e "\n Enter the Output signature file Name"

read signatureFileName

echo -e "\n Signing the Given File Using Private Key e.g. ($keyName.key)"

cosign sign-blob $fileName --key $keyName.key -output-signature $signatureFileName

signText= cat $signatureFileName

echo -e "\n your signature is: $signText"

echo -e " Would you like to Verify the Signature Now ? Y = Yes, N = No"

read option

if [ $option -eq "Y" ]

echo " \n Verifying the Sign of $fileName Using Public Key e.g. ($keyName.pub)"

cosign verify-blob $fileName --key $keyName.pub --signature $signatureFileName

fi

echo -e "\n  ✅ Process Ends Successfully "