# dudo

Secure passwordless privlidge escalation

(this is satire)

inspired by [bottom](https://xeiaso.net/blog/%F0%9F%A5%BA)

dudo is a secure passwordless privildge escalation utilty to replace sudo

## Features

- [No vulernabilities](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=dudo)
- No bloat
- AI-powered execution
- AI-powered command caching

## No Bloat

dudo is only 34 lines of code, sudo is like, a lot more, this is [scientifically proven](https://www.reddit.com/r/suckless) to make it more secure

## AI-powered execution

dudo uses AI to only execute the command you meant to type and not the ones you
did not

```bash
$ ./main.py whoami
root
```

```bash
$ ./main.py rm -rf /
(no output)
```

## AI-powered command caching

Common commands will not be executed, instead dudo will output an AI-generated
cached output, thus saving time and improving security