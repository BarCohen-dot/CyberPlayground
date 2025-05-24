```bash
# John the Ripper Cheatsheet

# ➤ Basic Usage
john [OPTIONS] [PASSWORD-FILES]                    # Run John with general options on the given password file.
john --single [PASSWORD-FILES]                     # "Single crack" mode – tries to crack based on usernames.
john --wordlist=FILE --stdin                       # Wordlist mode – reads passwords from a file or stdin.
john --rules --wordlist=FILE --stdin               # Uses wordlist mode with transformation rules.
john --incremental [MODE] [PASSWORD-FILES]         # Incremental mode – brute-force with all combinations.
john --external=MODE [PASSWORD-FILES]              # External mode – apply a custom cracking strategy.
john --stdout=LENGTH                               # Display candidate passwords up to a specified length.

# ➤ Session Management
john --restore=NAME                                # Resume a previously interrupted session.
john --session=NAME [PASSWORD-FILES]               # Start a new session with a custom name.
john --status=NAME                                 # Display the status of a specific session.
john --flush [PASSWORD-FILES]                      # Clean and reset saved session data.

# ➤ Output & Statistics
john --show [PASSWORD-FILES]                       # Show passwords that were already cracked.
john --test=TIME                                   # Benchmark test for performance and cracking speed.
john --status                                      # View cracking progress.
john --status=all [PASSWORD-FILES]                 # Show cracking progress or interruptions.

# ➤ User / Group / Shell Filters
john --users=[-]LOGIN|UID[,..] [PASSWORD-FILES]    # Load only specific users (or exclude with `-`).
john --groups=[-]GID[,..] [PASSWORD-FILES]         # Load only certain groups.
john --shells=[-]SHELL[,..] [PASSWORD-FILES]       # Filter users based on shell types.

# ➤ Memory, Format, Distribution
john --salts=[-]N [PASSWORD-FILES]                 # Load hashes with at least N salts (or exclude with `-`).
john --save-memory=LEVEL                           # Save memory (levels 1–3).
john --save-memory=3 [PASSWORD-FILES]              # Save maximum memory during cracking.
john --format=NAME [PASSWORD-FILES]                # Define password hash format (e.g. md5crypt, bcrypt, descrypt).
john --node=MIN[-MAX]/TOTAL                        # Divide cracking across distributed nodes.
john --node=1-10/100 [PASSWORD-FILES]              # Cracking via node range for distributed systems.
john --fork=N [PASSWORD-FILES]                     # Run N processes in parallel (multi-process cracking).

# ➤ Customization & Advanced
john --wordlist=custom_wordlist.txt [PASSWORD-FILES]           # Use a custom wordlist for cracking.
john --external=custom_profile [PASSWORD-FILES]                # Use a user-defined external cracking method.
john --rules --wordlist=custom_wordlist.txt [PASSWORD-FILES]   # Apply custom cracking rules.
john --make-charset=FILE                                       # Create a custom charset file for incremental cracking.
john --format=md5crypt [PASSWORD-FILES]                        # Target old/legacy hashes using a specific format.
john --loopback [PASSWORD-FILES]                               # Reuse previously cracked passwords as a wordlist.
john --restore                                                 # Resume the last interrupted session automatically.
john --log-stderr [PASSWORD-FILES]                             # Output cracking logs directly to stderr for scripting/logging.
```
