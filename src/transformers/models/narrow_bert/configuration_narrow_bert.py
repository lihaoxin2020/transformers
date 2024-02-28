# coding=utf-8
# Copyright 2022 Haoxin Li and The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" NarrowBERT model configuration """

from ...configuration_utils import PretrainedConfig
from ...utils import logging


logger = logging.get_logger(__name__)

NARROW_BERT_PRETRAINED_CONFIG_ARCHIVE_MAP = {
    "lihaoxin2020/narrowbert-sparse_attn-uncased": "https://huggingface.co/lihaoxin2020/narrowbert-sparse_attn-uncased/resolve/main/config.json",
    # See all NarrowBERT models at https://huggingface.co/models?filter=narrow_bert
}


class NarrowBertConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`~NarrowBertModel`].
    It is used to instantiate an NarrowBERT model according to the specified arguments, defining the model
    architecture. Instantiating a configuration with the defaults will yield a similar configuration to that of
    the NarrowBERT [lihaoxin2020/narrowbert-sparse_attn-uncased](https://huggingface.co/lihaoxin2020/narrowbert-sparse_attn-uncased) architecture.

    Configuration objects inherit from  [`PretrainedConfig`] and can be used
    to control the model outputs. Read the documentation from  [`PretrainedConfig`]
    for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the NarrowBERT model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`~NarrowBertModel`] or
            [`~TFNarrowBertModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimension of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        full_length_layers (`int`, *optional*, defaults to 2):
            Number of fully contextualized layers. 12 is equivalent to normal BERT.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimension of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler.
            If string, `"gelu"`, `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with.
            Typically set this to something large just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`~NarrowBertModel`] or
            [`~TFNarrowBertModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        pad_token_id (`int`, *optional*, defaults to 0): <pad> token ID.
        classifier_dropout (`float`, *optional*):
            The dropout ratio for the classification head.
        position_embedding_type (`str`, *optional*, defaults to `"absolute"`):
            Type of position embedding. Choose one of `"absolute"`, `"relative_key"`, `"relative_key_query"`. For
            positional embeddings use `"absolute"`. For more information on `"relative_key"`, please refer to
            [Self-Attention with Relative Position Representations (Shaw et al.)](https://arxiv.org/abs/1803.02155).
            For more information on `"relative_key_query"`, please refer to *Method 4* in [Improve Transformer Models
            with Better Relative Position Embeddings (Huang et al.)](https://arxiv.org/abs/2009.13658).

    Exampls:

    ```python
    >>> from transformers import NarrowBertModel, NarrowBertConfig

    >>> # Initializing a NarrowBERT lihaoxin2020/narrowbert-sparse_attn-uncased style configuration
    >>> configuration = NarrowBertConfig()

    >>> # Initializing a model from the lihaoxin2020/narrowbert-sparse_attn-uncased style configuration
    >>> model = NarrowBertModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = "narrow_bert"

    def __init__(
        self,
        vocab_size=30522,
        hidden_size=768,
        num_hidden_layers=12,
        full_length_layers=2,
        num_attention_heads=12,
        intermediate_size=3072,
        hidden_act="gelu",
        hidden_dropout_prob=0.1,
        attention_probs_dropout_prob=0.1,
        max_position_embeddings=512,
        type_vocab_size=2,
        initializer_range=0.02,
        layer_norm_eps=1e-12,
        use_cache=True,
        pad_token_id=0,
        classifier_dropout=None,
        position_embedding_type="absolute",
        **kwargs,
    ):
        if full_length_layers > num_hidden_layers:
            raise ValueError("You have to specify fewer full_length_layers than total num_hidden_layers.")
        self.vocab_size = vocab_size
        self.max_position_embeddings = max_position_embeddings
        self.hidden_size = hidden_size
        self.num_hidden_layers = num_hidden_layers
        self.full_length_layers = full_length_layers
        self.num_narrow_layers = num_hidden_layers - full_length_layers
        self.num_attention_heads = num_attention_heads
        self.intermediate_size = intermediate_size
        self.hidden_act = hidden_act
        self.hidden_dropout_prob = hidden_dropout_prob
        self.attention_probs_dropout_prob = attention_probs_dropout_prob
        self.initializer_range = initializer_range
        self.type_vocab_size = type_vocab_size
        self.layer_norm_eps = layer_norm_eps
        self.use_cache = use_cache
        self.classifier_dropout = classifier_dropout
        self.position_embedding_type = position_embedding_type

        super().__init__(pad_token_id=pad_token_id, **kwargs)