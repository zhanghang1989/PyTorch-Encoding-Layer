# pylint: disable=wildcard-import, unused-wildcard-import

from .resnet import *
from .resnest import *
from .wideresnet import *
from .fcn import *
from .psp import *
from .encnet import *
from .deepten import *
from .xception import *

__all__ = ['get_model']


def get_model(name, **kwargs):
    """Returns a pre-defined model by name

    Parameters
    ----------
    name : str
        Name of the model.
    pretrained : bool
        Whether to load the pretrained weights for model.
    root : str, default '~/.encoding/models'
        Location for keeping the model parameters.

    Returns
    -------
    Module:
        The model.
    """
    models = {
        'resnest50': resnest50,
        'resnet50': resnet50,
        'resnet101': resnet101,
        'resnet152': resnet152,
        'xception65': xception65,
        'wideresnet38': wideresnet38,
        'wideresnet50': wideresnet50,
        'deepten_resnet50_minc': get_deepten_resnet50_minc,
        'fcn_resnet50_pcontext': get_fcn_resnet50_pcontext,
        'encnet_resnet50_pcontext': get_encnet_resnet50_pcontext,
        'encnet_resnet101_pcontext': get_encnet_resnet101_pcontext,
        'encnet_resnet50_ade': get_encnet_resnet50_ade,
        'encnet_resnet101_ade': get_encnet_resnet101_ade,
        'fcn_resnet50_ade': get_fcn_resnet50_ade,
        'psp_resnet50_ade': get_psp_resnet50_ade,
        }
    name = name.lower()
    if name not in models:
        raise ValueError('%s\n\t%s' % (str(name), '\n\t'.join(sorted(models.keys()))))
    net = models[name](**kwargs)
    return net
