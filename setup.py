from setuptools import setup

setup(
    name='hpos-seed',
    packages=['hpos_seed'],
    entry_points={
        'console_scripts': [
            'hpos-seed-send=hpos_seed.send_cli:main',
            'hpos-seed-send-qt=hpos_seed.send_qt:main'
        ],
    },
    install_requires=['magic-wormhole']
)
