#!/usr/bin/env python3
"""
Standalone tests for ending logic without pytest.
Run:

    python3 test_endings_simple.py

This uses only the Python standard library and Flask's test client.
"""
from app import app
import sys


def post_choice_with_session(client, node, stats, choice_index=0):
    with client.session_transaction() as sess:
        sess['current_node'] = node
        sess['fatigue'] = stats.get('fatigue', 0)
        sess['belonging'] = stats.get('belonging', 0)
        sess['selfworth'] = stats.get('selfworth', 0)
        sess['tension'] = stats.get('tension', 0)
    return client.post('/story', data={'choice': str(choice_index)}, follow_redirects=True)


tests = [
    ('high_fatigue', {'fatigue': 14}, b'The Body Keeps Score'),
    ('low_selfworth', {'selfworth': -7}, b'Quietly Becoming Smaller'),
    ('high_tension', {'tension': 12}, b'The Jaw Remembers'),
    ('low_belonging', {'belonging': -6}, b'A House, Not a Home'),
    ('high_tension_via_standout', {'selfworth': -7, 'tension': 12}, b'The Jaw Remembers'),
    ('balanced', {'fatigue': 0, 'selfworth': 0, 'belonging': 0, 'tension': 0}, b'Learning to Live With It'),
]


def run():
    failures = 0
    with app.test_client() as client:
        for name, stats, expected in tests:
            resp = post_choice_with_session(client, 'tv', stats)
            ok = expected in resp.data
            print(f'{name}:', 'PASS' if ok else 'FAIL')
            if not ok:
                print('  expected to find:', expected)
                print('  --- response snippet ---')
                print(resp.data[:400])
                failures += 1

    if failures:
        print(f'\n{failures} test(s) failed.')
        sys.exit(1)
    else:
        print('\nAll tests passed.')
        sys.exit(0)


if __name__ == '__main__':
    run()
