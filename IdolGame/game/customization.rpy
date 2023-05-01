init python:
    ## Calculate the scale needed for an image to fill the screen
    def get_img_fill_scale(img):
        img_w, img_h = get_img_size(img)
        need_w_scale = config.screen_width / float(img_w)
        need_h_scale = config.screen_height / float(img_h)
        return max(need_w_scale, need_h_scale)

    ## Calculate the scale needed for an image to fill the screen vertically
    def get_img_fill_vert_scale(img):
        img_w, img_h = get_img_size(img)
        return config.screen_height / float(img_h)

    ## Get the height and width of an image
    def get_img_size(img):
        tmp1 = renpy.loader.load(img)
        tmp2 = renpy.display.scale.image_load_unscaled(tmp1, img)
        return tmp2.get_size()

    ## Upscale an image for use as a background
    def make_bg(img):
        return make_fillscreen(img)

    ## Upscale an image for use as a CG
    def make_cg(img):
        return make_fillscreen(img)

    ## Scale an image to use as a sprite
    def make_sprite(img):
        return make_fillvert(img)

    ## Upscale an image to fill the screen
    def make_fillscreen(img):
        return im.zoom(img, get_img_fill_scale(img))

    ## Upscale an image to fill the screen vertically
    def make_fillvert(img):
        return im.zoom(img, get_img_fill_vert_scale(img))

    ## Matrix for boosting opacity in an image
    def boost_opacity(val):
        return [1,0,0,0,0, 0,1,0,0,0, 0,0,1,0,0, 0,0,0,val,0]

