from flask import Flask, render_template


# import torch
# import gradio as gr

# model = torch.hub.load("./", "custom", path = "best.pt", source = "local", force_reload=True)

# # initial threshold for confidence & iou
# base_conf, base_iou = 0.25, 0.45

# # to render different predictions with different confidence & iou thresholds
# def det_image(img, conf_thres, iou_thres):
#   model.conf = conf_thres
#   model.iou = iou_thres
#   return model(img).render()[0]


# # for user to adjust confidence & iou thresholds
# interface = gr.Interface(inputs = ["image", gr.Slider(minimum=0, maximum=1, value=base_conf), gr.Slider(minimum=0, maximum=1, value=base_iou)],
#              outputs = ["image"],
#              fn = det_image,
#              ).launch(share = True)

app = Flask(__name__)

@app.route("/gradio", methods=['GET', 'POST'])
def gradio_interface():
    return render_template("gradio.html")


@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')


@app.route('/map', methods=['GET', 'POST'])
def map():
    return render_template('map.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

app.run(host='0.0.0.0', port=81)