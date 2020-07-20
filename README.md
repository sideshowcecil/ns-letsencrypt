# Let's Encrypt NetScaler

Let's Encrypt support for Citrix NetScaler/ADC using [dehydrated](https://github.com/lukas2511/dehydrated) and the [Nitro API](https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/12.0/).

## Installation

1. Install pipenv
```
$ pip install pipenv
```
2. Install dependencies
```
$ pipenv run pip freeze > requirements.txt
$ pip install -r requirements.txt
```
3. Doing confiuration, see below
4. Run `./letsencrypt_cron.sh`
```
$ ./letsencrypt_cron.sh
```
5. Configure cronjob:
```
0 0 1 * * <path-to-this-dir>/letsencrypt_cron.sh
```

## Setup

To use this project one needs to provide the following information:
* config.sh
  * contains basic dehydrated configuration, use config.sh.example
* nsconfig.py
  * provides connection details to the NetScaler/ADC instances, see nsconfig.py.example

## References

Kudos to @ryancbutler for the initial project: https://github.com/ryancbutler/ns-letsencrypt

