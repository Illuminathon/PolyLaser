import pygame 
import math

def get_ray_end_position(start_pos, angle, max_length=1000):
    rad = math.radians(angle)
    end_x = start_pos[0] + max_length * math.cos(rad)
    end_y = start_pos[1] + max_length * math.sin(rad)
    return (end_x, end_y)

def draw_laser(surface, start_position, initial_angle, buildings):
    current_start = start_position 
    current_angle = initial_angle
    points = [current_start] # list of the points the laser has to go through

    for _ in range(5):

        target_x, target_y = get_ray_end_position(current_start, current_angle)
        ray_line = (current_start, (target_x, target_y))

        hit_point = None 
        hit_wall = None


        # There is a list of object, we can change it in the future
        for obj in game_objects:
            collision = obj.check_collision(ray_line)
            if collision:
                hit_point = collision
                hit_object = obj
                break

            if hit_point:
                points.append(hit_point)
                #if the laser hits the mirror
                if hit_object.type == "mirror":

                    current_angle = hit_object.calculate_reflection(current_angle)
                    current_start = hit_point
                # If the laser hits sensor you will win so we can add here something else than break 
                elif hit_object.type == "sensor":
                    break
                # If the laser hits the wall:
                elif hit_object.type == "wall":
                    break
            else:
                points.append((target_x, target_y))
                break
    


    # end_position = (1180, 360)

    # pygame.draw.line(surface, (255, 0, 0), start_position, end_position, width=5)


