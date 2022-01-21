from turtle import width
import dearpygui.dearpygui as dpg

def grid_mouse_move_callback(sender, data):
    x, y = dpg.get_mouse_pos()
    print(f"Mouse Move ({x}, {y})")

def setup_grid():
    with dpg.window(id="Main",label="Robot Path Simulator") as window:
        size = size = 640
        grid_spacing = int(size / 20)

        with dpg.drawlist(width=size, height=size):
            for i in range(0, size + 1, grid_spacing):
                dpg.draw_line((i, 0), (i, size), color=(255, 255, 255, 255), thickness=1)
                dpg.draw_line((0, i), (size, i), color=(255, 255, 255, 255), thickness=1)

def main():
    dpg.create_context()

    setup_grid()

    dpg.create_viewport(title="Robot Path Simulator", width=1280, height=720)
    dpg.set_primary_window(window="Main", value=True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()