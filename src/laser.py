import pygame 

MAX_RAY_LENGTH = 2000
MAX_REFLECTIONS = 10


def _closest_collision(start, end, objects, ignored_object=None):
    closest = None
    closest_distance = float("inf")

    for obj in objects:
        if obj is ignored_object:
            continue

        check_collision = getattr(obj, "check_collision", None)
        if check_collision is None:
            continue

        collision = check_collision((start, end))
        if collision is None:
            continue

        point = pygame.Vector2(collision)
        distance = point.distance_squared_to(start)
        if distance < closest_distance:
            closest = (point, obj)
            closest_distance = distance

    return closest


def trace_laser(start_position, initial_angle, objects):
    current_start = pygame.Vector2(start_position)
    direction = pygame.Vector2(1, 0).rotate(initial_angle).normalize()
    points = [current_start]
    ignored_object = None

    for _ in range(MAX_REFLECTIONS):
        ray_end = current_start + direction * MAX_RAY_LENGTH
        hit = _closest_collision(current_start, ray_end, objects, ignored_object)
        ignored_object = None

        if hit is None:
            points.append(ray_end)
            break

        hit_point, hit_object = hit
        points.append(hit_point)

        if getattr(hit_object, "type", None) == "mirror":
            direction = hit_object.calculate_reflection(direction)
            current_start = hit_point + direction * 0.1
            ignored_object = hit_object
            points.append(current_start)
        else:
            break

    return points


def draw_laser(surface, start_position, initial_angle, objects):
    points = trace_laser(start_position, initial_angle, objects)
    if len(points) > 1:
        pygame.draw.lines(surface, (255, 0, 0), False, points, 3)
