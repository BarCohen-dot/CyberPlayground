This cheatsheet covers all essential `john` commands for password cracking, session control, optimization, and filtering.

> ⚠️ Use only in ethical and authorized environments.

---

Basic Usage
===========

```bash
john [OPTIONS] [PASSWORD-FILES]
```

- Run John with general options on the given password file.

```bash
john --single [PASSWORD-FILES]
```

- "Single crack" mode – tries to crack based on usernames.

```bash
john --wordlist=FILE --stdin
```

- Wordlist mode – reads passwords from a file or stdin.

```bash
john --rules --wordlist=FILE --stdin
```

- Uses wordlist mode with transformation rules.

```bash
john --incremental [MODE] [PASSWORD-FILES]
```

- Incremental mode – brute-force with all combinations.

```bash
john --external=MODE [PASSWORD-FILES]
```

- External mode – apply a custom cracking strategy.

```bash
john --stdout=LENGTH
```

- Display candidate passwords up to a specified length.

---

Session Management
==================

```bash
john --restore=NAME
```

- Resume a previously interrupted session.

```bash
john --session=NAME [PASSWORD-FILES]
```

- Start a new session with a custom name.

```bash
john --status=NAME
```

- Display the status of a specific session.

```bash
john --flush [PASSWORD-FILES]
```

- Clean and reset saved session data.

---

Output & Statistics
===================

```bash
john --show [PASSWORD-FILES]
```

- Show passwords that were already cracked.

```bash
john --test=TIME
```

- Benchmark test for performance and cracking speed.

```bash
john --status
john --status=all [PASSWORD-FILES]
```

- View cracking progress or interruptions.

---

User / Group / Shell Filters
============================

```bash
john --users=[-]LOGIN|UID[,..] [PASSWORD-FILES]
```

- Load only specific users (or exclude with `-`).

```bash
john --groups=[-]GID[,..] [PASSWORD-FILES]
```

- Load only certain groups.

```bash
john --shells=[-]SHELL[,..] [PASSWORD-FILES]
```

- Filter users based on shell types.

---

Memory, Format, Distribution
============================

```bash
john --salts=[-]N [PASSWORD-FILES]
```

- Load hashes with at least N salts (or exclude with `-`).

```bash
john --save-memory=LEVEL
john --save-memory=3 [PASSWORD-FILES]
```

- Save memory (levels 1–3).

```bash
john --format=NAME [PASSWORD-FILES]
```

- Define password hash format (e.g. `md5crypt`, `bcrypt`, `descrypt`).

```bash
john --node=MIN[-MAX]/TOTAL
john --node=1-10/100 [PASSWORD-FILES]
```

- Divide cracking across distributed nodes.

```bash
john --fork=N [PASSWORD-FILES]
```

- Run N processes in parallel (multi-process cracking).

---

Customization & Advanced
========================

```bash
john --wordlist=custom_wordlist.txt [PASSWORD-FILES]
```

- Use a custom wordlist for cracking.

```bash
john --external=custom_profile [PASSWORD-FILES]
```

- Use a user-defined external cracking method.

```bash
john --rules --wordlist=custom_wordlist.txt [PASSWORD-FILES]
```

- Apply custom cracking rules from configuration.

```bash
john --make-charset=FILE
```

- Create a custom charset file for incremental cracking.

```bash
john --format=md5crypt [PASSWORD-FILES]
```

- Target old/legacy hashes using a specific format.
