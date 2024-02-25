import hashlib
import time
import sys

def loading_animation():
    
    animation1=" MD5 Hash Cracker v4\n"
    animation2="░▒▓███████▓▒░░▒▓█▓▒░       ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░▒▓████████▓▒░\n"
    animation3="░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░\n"
    animation4="░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░\n"  
    animation5="░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░ ░▒▓█▓▒░\n"  
    animation6="░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░\n"
    animation7="░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░\n"  
    animation8="░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░\n"
    animation9="By BL4CKH4T @pcstat 💎\n"


    animations = [animation1, animation2, animation3, animation4, animation5, animation6, animation7, animation8, animation9]

    for animation in animations:
        print(animation, end='\r')
        time.sleep(0.1)

loading_animation()

def is_md5(hash_str):
    return len(hash_str) == 32 and all(c.isalnum() for c in hash_str)

def find_md5_hash(target_md5, wordlist_path):
    try:
        with open(wordlist_path, 'rb') as wordlist:
            total_words = sum(1 for _ in wordlist)  # Calculate the total number of words
            wordlist.seek(0)  # Reset the file pointer

            for idx, line in enumerate(wordlist, start=1):
                word = line.decode('utf-8', errors='ignore').strip()
                calculated_md5 = hashlib.md5(word.encode()).hexdigest()
                if calculated_md5 == target_md5:
                    return word, idx, total_words

                sys.stdout.write(f"Scanning word {idx} of {total_words} | Time elapsed: {time.time() - start_time:.2f}s\r")
                sys.stdout.flush()

        return None, total_words, total_words
    except Exception as e:
        return None, 0, 0

if __name__ == "__main__":
    target_hash = input("[+] Enter the Target Hash: ")

    if is_md5(target_hash):
        wordlist_path = input("[+] Enter the Wordlist File Path: ")

        # Print the given output before scanning starts
        prompt = "PING 142.251.40.164"
        print(f"[*] {prompt} ping (142.251.40.164)")
        time.sleep(2.25)
        print(f"[*] {prompt} ping (142.251.40.164) 32 bytes of data")
        time.sleep(1.25)
        print(f"[*] {prompt} Packets: Sent = 4, Received = 4, Lost = (0% loss)(142.251.40.164): bytes=32 time=284ms TTL=111")
        time.sleep(1.25)

        start_time = time.time()
        found_word, current_word, total_words = find_md5_hash(target_hash, wordlist_path)
        elapsed_time = time.time() - start_time

        if found_word:
            print(f"[+] Password Found! '{found_word}' Matches MD5 Hash = {target_hash}")
        else:
            print("[!] Password not Found in the Wordlist.")

        print(f"[+] Scanning Complete. Time elapsed: {elapsed_time:.2f}s")
        print(f"[+] Scanning Word {current_word} of {total_words}")
    else:
        print("[+] Please Enter Valid MD5 hash ( 32-digit hexadecimal number ) ")
