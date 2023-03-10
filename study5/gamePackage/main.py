# import game.sound.echo                # test1
# from game.sound.echo import echo_test
from game.sound import *
from game.graphic.render import render_test

if __name__ == '__main__':
    # game.sound.echo.echo_test()       # test1
    # echo_test()
    echo.echo_test()
    wav.wav_test()
    render_test()
