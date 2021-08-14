import argparse
import connexion
from .command import OnkyoCommand

GPIO = None


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--gpio', type=int, default=25)
    return parser.parse_args()


def main():
    """Command-line script for omm server."""

    global GPIO

    args = _parse_args()
    GPIO = args.gpio

    app = connexion.FlaskApp(__name__, specification_dir='api')
    app.add_api('openapi.yaml')
    app.run(port=args.port)
