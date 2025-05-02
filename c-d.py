#!/usr/bin/env python3
"""
A simple reversible string encoder/decoder using base64 only (no third-party libs).

Version: 2

Usage:
    # Encode a string:
    python c-d.py encode "your text here"

    # Decode a token:
    python c-d.py decode "token_here"
"""
import argparse
import base64
import sys

def encode_string(plaintext: str) -> str:
    """Encode plaintext to Base64 string."""
    try:
        # Encode to bytes, then to Base64, then decode to str
        encoded = base64.b64encode(plaintext.encode('utf-8')).decode('ascii')
        return encoded
    except Exception as e:
        print(f"Encoding error: {e}", file=sys.stderr)
        sys.exit(1)


def decode_string(token: str) -> str:
    """Decode Base64 token back to plaintext string."""
    try:
        decoded = base64.b64decode(token.encode('ascii')).decode('utf-8')
        return decoded
    except Exception as e:
        print(f"Decoding error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Reversible encoder/decoder for strings using Base64."
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # encode subcommand
    parser_enc = subparsers.add_parser('encode', help='Encode a string to Base64')
    parser_enc.add_argument('text', help='Plaintext to encode')

    # decode subcommand
    parser_dec = subparsers.add_parser('decode', help='Decode a Base64 string')
    parser_dec.add_argument('token', help='Base64 string to decode')

    args = parser.parse_args()
    if args.command == 'encode':
        print(encode_string(args.text))
    else:
        print(decode_string(args.token))

if __name__ == '__main__':
    main()
