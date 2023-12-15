#!/bin/bash

set -e
RED=$(tput setaf 1)
RESET=$(tput sgr0)
BOLD=$(tput bold)
YELLOW=$(tput setaf 3)
GREEN=$(tput setaf 2)

echo -e "\n ${BOLD}${RED}Important !!!${RESET} This script only sign the file/Blobs 📂 Using Sigstore's Cosign Utility·"

echo -e "\n Please keep this script in the same folder where your file is located which intended to be signed. \n\n Enter ctrl+c or control+c to exit from this script any time ·"

echo -e "\n Provide the Name for the Private and Public Key (Something like my-secretkey)·"

read keyName

echo -e "\n Generating the Private and Public Key in Cosign·\n\n Please press enter if you do not want to provide the password for the Key generation (Not Recomended)·\n"

cosign generate-key-pair --output-key-prefix $keyName

echo -e "\n Enter the File Name which has to be signed ·"

read fileName

echo -e "\n Enter the Output signature file Name ·"

read signatureFileName

echo -e "\n Signing the Given File Using Private Key e.g. ($keyName.key)·"

cosign sign-blob $fileName --key $keyName.key --output-signature $signatureFileName -y

echo -e " \n Would you like to Verify the Signature Now ? y = Yes, n = No ·"

read option
 if [ "$option" == "y" ]; then
echo " \n Verifying the Sign of $fileName Using Public Key e.g. ($keyName.pub)·"
cosign verify-blob $fileName --key $keyName.pub --signature $signatureFileName
fi

echo -e "\n${BOLD}${GREEN}Process Ends Successfully ✅·\n "