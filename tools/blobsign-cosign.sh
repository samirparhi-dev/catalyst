#!/bin/bash

set -e
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
BLUE=$(tput setaf 4)
RESET=$(tput sgr0)
BOLD=$(tput bold)


echo -e "\n ${BOLD}${RED}Important !!!${RESET} This script only sign the file/Blobs 📂 Using Sigstore's Cosign Utility· \n\n Enter ctrl+c or control+c to exit from this script any time ·"

echo -e "\n ${BLUE}Provide the Name for the Private and Public Key(Something like my-secretkey):${RESET}"

read keyName

echo -e "\n Generating the Private and Public Key in Cosign·\n\n Please Press ${BOLD}Enter${RESET} if you do not want to provide the password for the Key generation (${BOLD}${RED}Not Recomended)${RESET}·\n"

cosign generate-key-pair --output-key-prefix $keyName

echo -e "\n ${BLUE}Enter the File Name or path/to/fileName which has to be signed${RESET} ·"

read fileName

echo -e "\n ${BLUE}Enter the Output signature file Name or Path/to/fileName ${RESET} ·"

read signatureFileName

echo -e "\n Signing the Given File Using Private Key e.g. ($keyName.key) please Wait 5 sec·"

cosign sign-blob $fileName --key $keyName.key --output-signature $signatureFileName -y

echo -e "\n${BOLD}${BLUE}Your Signature is:${RESET} $(cat "$signatureFileName")\n"

echo -e "${BLUE}Would you like to Verify the Signature Now ?${RESET} y = Yes, n = No ·"

read option

 if [ "$option" == "y" ]; then

echo -e "\n Verifying the Sign of $fileName Using Public Key e.g. ($keyName.pub)·"

cosign verify-blob $fileName --key $keyName.pub --signature $signatureFileName
else
echo -e "\n${BLUE}${BOLD}You have Choosen not to verify the Signature rightnow.😊${RESET}"
fi
echo -e "\n${BOLD}${GREEN}Process Ends ✅·\n${RESET}"