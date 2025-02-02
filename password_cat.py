import subprocess

# Provided password dump data
password_dump = """
experthead:e10adc3949ba59abbe56e057f20f883e
interestec:25f9e794323b453885f5181f1b624d0b
ortspoon:d8578edf8458ce06fbc5bb76a58c5ca4
reallychel:5f4dcc3b5aa765d61d8327deb882cf99
simmson56:96e79218965eb72c92a549dd5a330112
bookma:25d55ad283aa400af464c76d713c07ad
popularkiya7:e99a18c428cb38d5f260853678922e03
eatingcake1994:fcea920f7412b5da7be0cf42b8c93759
heroanhart:7c6a180b36896a0a8c02787eeafb0e4c
edi_tesla89:6c569aabbf7775ef8fc570e228c16b98
liveltekah:3f230640b78d7e71ac5514e57935eb69
blikimore:917eb5e9d6d6bca820922a0c6f7cc28b
johnwick007:f6a0cb102c62879d397b12b62c092c06
flamesbria2001:9b3b269ad0a208090309f091b3aba9db
oranolio:16ced47d3fc931483e24933665cded6d
spuffyffet:1f5c5683982d7c3814d4d9e6d749b21e
moodie:8d763385e0476ae208f21bc63956f748
nabox:defebde7b6ab6f24d5824682a16c3ae4
bandalls:bdda5f03128bcbdfa78d8934529048cf
"""

# Step 1: Extract hashes
hashes = [line.split(":")[1] for line in password_dump.strip().split("\n")]

# Step 2: Write hashes to a file
with open("hashes.txt", "w") as f:
    for h in hashes:
        f.write(f"{h}\n")

print("hashes.txt file created successfully.")

# Step 3: Run Hashcat to Crack the Passwords
def run_hashcat(hash_file, wordlist):
    command = f"hashcat -a 0 -m 0 {hash_file} {wordlist}"
    process = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.stdout.decode(), process.stderr.decode()

def show_cracked_passwords(hash_file):
    command = f"hashcat -m 0 {hash_file} --show"
    process = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.stdout.decode(), process.stderr.decode()

# Example usage:
output, error = run_hashcat("hashes.txt", "rockyou.txt")
print("Hashcat Output:\n", output)
print("Hashcat Error:\n", error)

# Retrieve and display cracked passwords
cracked_passwords, error = show_cracked_passwords("hashes.txt")
print("Cracked Passwords:\n", cracked_passwords)
print("Show Command Error:\n", error)
