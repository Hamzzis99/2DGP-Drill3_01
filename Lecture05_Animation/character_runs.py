from pico2d import *
from math import *
open_canvas(800, 800)  # 캔버스 크기를 800x800으로 조정

def run_circle():
    grass = load_image('grass.png')
    character = load_image('run_animation.png')
    frame = 0


    for x in range(0, 400, 10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

#원 공식은 GPT를 이용하여 구했습니다.
    r, cx, cy = 300, 800 // 2, 300 + 90  # 반원의 반지름, 중심 좌표 x, 중심 좌표 y 조정
    for i in range(270, 630):  # 270도(바닥을 가리킴)에서 630도까지 각도를 증가시키면서 반원을 그림 GPT수학
        clear_canvas()
        grass.draw(400, 30)

        angle = radians(i)  # 현재 각도를 라디안으로 변환
        dx = cos(angle) * r
        dy = sin(angle) * r

        # 각도에 따라 캐릭터 회전
        direction = angle + pi / 2  # 캐릭터가 원의 중심을 바라보도록 조정

        # 캐릭터 그리기
        character.clip_composite_draw(frame * 100, 0, 100, 100, direction, '', cx + dx, cy + dy, 100, 100)

        update_canvas()
        frame = (frame + 1) % 8  # 다음 프레임으로 업데이트
        delay(0.05)  # 0.05초 지연

    for x in range(400, 700, 10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    for y in range(90, 700, 10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, 700, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    for x in range(700, 100, -10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 700)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    for y in range(700, 90, -10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, 100, 700)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    for x in range(100, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)


# 애니메이션 실행
run_circle()

close_canvas()

