#!/usr/bin/env python3

import logging
import os
import sys

from nitro import Nitro, DomainNotFound

# config
import nsconfig


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        raise SystemExit('Usage: %s <hook_stage> <args>' % sys.argv[0])

    log_level = os.environ.get('LOGLEVEL', 'INFO').upper()
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=log_level, format=log_format)

    hook_stage = args[1]
    args = args[2:]

    nitro = Nitro(config=nsconfig.nitro_config)

    try:
        if hook_stage == 'startup_hook':
            pass
        elif hook_stage == 'deploy_challenge':
            domain, challenge_filename, challenge_value = args
            nitro.deploy_challenge(domain, challenge_filename, challenge_value)
        elif hook_stage == 'clean_challenge':
            domain, challenge_filename, challenge_value = args
            nitro.clean_challenge(domain, challenge_filename)
        elif hook_stage == 'deploy_cert':
            domain, key_file, cert_file, full_chain_file, chain_file, timestamp = args
            nitro.deploy_cert(domain, key_file, cert_file, full_chain_file, chain_file)
        elif hook_stage == 'exit_hook':
            # save the config as a final step
            nitro.save()
    except ValueError:
        raise SystemExit('Usage: ' + sys.argv[0] + ' <hook_stage> <args>')
    except DomainNotFound as e:
        logging.error('Domain not found %s' % e.domain)
