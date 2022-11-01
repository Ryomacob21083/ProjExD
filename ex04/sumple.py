import pygame as pg
import sys

def main():
    pg.display.set_caption("初めてのPyGame")    ##タイトルバーに「初めての...」を表示
    scrn_sfc = pg.display.set_mode((800, 600)) ## 800×600の画面surfaceを生成

    tori_sfc = pg.image.load("fig/6.png")
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 700, 400
    scrn_sfc.blit(tori_sfc, tori_rct)


    clock = pg.time.Clock()
    pg.display.update()
    clock.tick(0.2)
    

if __name__ == "__main__":
    pg.init()           ##モジュールを初期化
    main()
    pg.quit()           ##モジュールの初期化を解除
    sys.exit()          ##プログラムを終了
