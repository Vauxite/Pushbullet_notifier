#!/usr/bin/python
from pushbullet import Pushbullet
import argparse



parser = argparse.ArgumentParser(description='Pushbullet notifier')

parser.add_argument('--api', help='Your pusbullet api-key')
parser.add_argument('--msg', help='Message to be sent')
parser.add_argument('--url', help='URL to be sent')
parser.add_argument('--title', help='Title to be used')
parser.add_argument('--dev', help='Send to specific device')

args = parser.parse_args()

if args.api:
    pb = Pushbullet(args.api)
    if pb and args.title:
        if args.dev:
            dev = pb.get_device(args.dev)
            if args.msg:
                pb.push_note(args.title, args.msg, device=dev)
            elif args.url:
                pb.push_link(args.title, args.url, device=dev)
        else:  
            if args.msg:
                pb.push_note(args.title, args.msg)
            elif args.url:
                pb.push_link(args.title, args.url)
