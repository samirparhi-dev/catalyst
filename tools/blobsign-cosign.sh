#!/bin/bash

set -e

echo "Important !!! This script only sign the file/Blobs"

echo "Please keep this script in the same folder where your file is located which intended to be signed"

echo "Chose the Name for the Private and Public Key e.g(my-key)"

read keyName

echo "Generating the Private and Public Key in Cosign..."

cosign generate-key-pair --output-key-prefix $keyName

echo "Enter the File Name which has to be signed"

read fileName

echo "Enter the Output signature file Name"

read signatureFileName

echo " Now Sign the Given File Using Private Key e.g. ($keyName.key)"

cosign sign-blob $fileName --key $keyName.key -output-signature $signatureFileName

signText= cat $signatureFileName

echo "your signature is: $signText"

echo " Would you like to Verify the Signature Now ? Y = Yes, N = No"
read option
if [ $option -eq "Y" ]
echo " Verifying the Sign of $fileName Using Public Key e.g. ($keyName.pub)"

cosign verify-blob $fileName --key $keyName.pub --signature $signatureFileName
fi