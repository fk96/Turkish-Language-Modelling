import torch

from pytorch_transformers.modeling_bert import BertConfig, BertForPreTraining, load_tf_weights_in_bert


tf_checkpoint_path="working/model.ckpt"
bert_config_file = "working/bert_config.json"
pytorch_dump_path="working/pytorch_model"

config = BertConfig.from_json_file(bert_config_file)
print("Building PyTorch model from configuration: {}".format(str(config)))
model = BertForPreTraining(config)

# Load weights from tf checkpoint
load_tf_weights_in_bert(model, config, tf_checkpoint_path)

# Save pytorch-model
print("Save PyTorch model to {}".format(pytorch_dump_path))
torch.save(model.state_dict(), pytorch_dump_path)
