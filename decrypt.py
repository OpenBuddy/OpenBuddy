# Due to licensing restrictions from LLAMA, you need to have the original LLAMA-7B model to use this model. 
# To decrypt the model weights, obtain the original LLAMA-7B model (not the huggingface version) and run the following command:
# python decrypt.py [path-to-llama-7b-consolidated.00.pth-file] [path-to-our-model-folder]

import os
import sys
import glob
import numpy as np
import hashlib


SEED_SIZE = 16*1024*1024
SEED_MD5 = "08cf0f43451cc4ae056e0b19e56c1fcf"


def xor_files(input_path, output_path):
    # Check if output file exists
    if os.path.exists(output_path):
        print('Skipping already decrypted file: ' + output_path)
        return
    print('Decrypting: ', input_path, ' to ', output_path)
    with open(input_path, "rb") as input_file, open(output_path, "wb") as output_file:
        while True:
            input_data = input_file.read(SEED_SIZE)
            if not input_data:
                break
            inputLen = len(input_data)
            bufTmp = np.frombuffer(input_data, dtype=np.uint8) ^ bufSeed[:inputLen]
            output_data = bufTmp.tobytes()
            output_file.write(output_data)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decrypt.py <path-to-llama-7b-consolidated.00.pth-file> <our-model-folder>")
        sys.exit(1)

    seed_path = sys.argv[1]
    folder_path = sys.argv[2]

    with open(seed_path, "rb") as seed_file:
        # Read first 16MB of seed file
        seed_data = seed_file.read(SEED_SIZE)
        # store to bufSeed
        bufSeed = np.frombuffer(seed_data, dtype=np.uint8)
    # Get md5 hash of seed
    md5 = hashlib.md5()
    md5.update(seed_data)
    md5Hex = md5.hexdigest()
    print('Seed MD5: ', md5Hex)
    if md5Hex != SEED_MD5:
        print('Seed MD5 does not match. Please check seed file.')
        sys.exit(1)

    enc_files = glob.glob(os.path.join(folder_path, "*.enc"))

    for enc_file in enc_files:
        output_path = os.path.splitext(enc_file)[0]
        xor_files(enc_file, output_path)