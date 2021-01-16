from tensorflow.keras import backend as K
from tensorflow.keras.models import load_model
import onnx
import keras2onnx

onnx_model_name = 'model.onnx'

model = load_model('test/model.h5')
onnx_model = keras2onnx.convert_keras(model, model.name)
onnx.save_model(onnx_model, onnx_model_name)