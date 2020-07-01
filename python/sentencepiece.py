# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _sentencepiece
else:
    import _sentencepiece

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


EncoderVersion_kOptimized = _sentencepiece.EncoderVersion_kOptimized
EncoderVersion_kOriginal = _sentencepiece.EncoderVersion_kOriginal
class SentencePieceProcessor(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _sentencepiece.SentencePieceProcessor_swiginit(self, _sentencepiece.new_SentencePieceProcessor())
    __swig_destroy__ = _sentencepiece.delete_SentencePieceProcessor

    def LoadFromSerializedProto(self, serialized):
        return _sentencepiece.SentencePieceProcessor_LoadFromSerializedProto(self, serialized)

    def SetEncodeExtraOptions(self, extra_option):
        return _sentencepiece.SentencePieceProcessor_SetEncodeExtraOptions(self, extra_option)

    def SetDecodeExtraOptions(self, extra_option):
        return _sentencepiece.SentencePieceProcessor_SetDecodeExtraOptions(self, extra_option)

    def SetVocabulary(self, valid_vocab):
        return _sentencepiece.SentencePieceProcessor_SetVocabulary(self, valid_vocab)

    def ResetVocabulary(self):
        return _sentencepiece.SentencePieceProcessor_ResetVocabulary(self)

    def LoadVocabulary(self, filename, threshold):
        return _sentencepiece.SentencePieceProcessor_LoadVocabulary(self, filename, threshold)

    def SetEncoderVersion(self, encoder_version):
        return _sentencepiece.SentencePieceProcessor_SetEncoderVersion(self, encoder_version)

    def GetEncoderVersion(self):
        return _sentencepiece.SentencePieceProcessor_GetEncoderVersion(self)

    def EncodeAsPieces(self, input):
        return _sentencepiece.SentencePieceProcessor_EncodeAsPieces(self, input)

    def EncodeAsIds(self, input):
        return _sentencepiece.SentencePieceProcessor_EncodeAsIds(self, input)

    def NBestEncodeAsPieces(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncodeAsPieces(self, input, nbest_size)

    def NBestEncodeAsIds(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncodeAsIds(self, input, nbest_size)

    def SampleEncodeAsPieces(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAsPieces(self, input, nbest_size, alpha)

    def SampleEncodeAsIds(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAsIds(self, input, nbest_size, alpha)

    def DecodePieces(self, pieces):
        return _sentencepiece.SentencePieceProcessor_DecodePieces(self, pieces)

    def DecodeIds(self, ids):
        return _sentencepiece.SentencePieceProcessor_DecodeIds(self, ids)

    def EncodeAsSerializedProto(self, input):
        return _sentencepiece.SentencePieceProcessor_EncodeAsSerializedProto(self, input)

    def SampleEncodeAsSerializedProto(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAsSerializedProto(self, input, nbest_size, alpha)

    def NBestEncodeAsSerializedProto(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncodeAsSerializedProto(self, input, nbest_size)

    def DecodePiecesAsSerializedProto(self, pieces):
        return _sentencepiece.SentencePieceProcessor_DecodePiecesAsSerializedProto(self, pieces)

    def DecodeIdsAsSerializedProto(self, ids):
        return _sentencepiece.SentencePieceProcessor_DecodeIdsAsSerializedProto(self, ids)

    def GetPieceSize(self):
        return _sentencepiece.SentencePieceProcessor_GetPieceSize(self)

    def PieceToId(self, piece):
        return _sentencepiece.SentencePieceProcessor_PieceToId(self, piece)

    def IdToPiece(self, id):
        return _sentencepiece.SentencePieceProcessor_IdToPiece(self, id)

    def GetScore(self, id):
        return _sentencepiece.SentencePieceProcessor_GetScore(self, id)

    def IsUnknown(self, id):
        return _sentencepiece.SentencePieceProcessor_IsUnknown(self, id)

    def IsControl(self, id):
        return _sentencepiece.SentencePieceProcessor_IsControl(self, id)

    def IsUnused(self, id):
        return _sentencepiece.SentencePieceProcessor_IsUnused(self, id)

    def IsByte(self, id):
        return _sentencepiece.SentencePieceProcessor_IsByte(self, id)

    def unk_id(self):
        return _sentencepiece.SentencePieceProcessor_unk_id(self)

    def bos_id(self):
        return _sentencepiece.SentencePieceProcessor_bos_id(self)

    def eos_id(self):
        return _sentencepiece.SentencePieceProcessor_eos_id(self)

    def pad_id(self):
        return _sentencepiece.SentencePieceProcessor_pad_id(self)

    def serialized_model_proto(self):
        return _sentencepiece.SentencePieceProcessor_serialized_model_proto(self)

    def LoadFromFile(self, arg):
        return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)

    def Init(self,
             model_file=None,
             model_proto=None,
             out_type=int,
             add_bos=False,
             add_eos=False,
             reverse=False,
             enable_sampling=False,
             nbest_size=-1,
             alpha=0.1):
      """Initialzie sentencepieceProcessor.

      Args:
        model_file: The sentencepiece model file path.
        model_proto: The sentencepiece model serialized proto.
        out_type: output type. int or str.
        add_bos: Add <s> to the result (Default = false)
        add_eos: Add </s> to the result (Default = false) <s>/</s> is added after
          reversing (if enabled).
        reverse: Reverses the tokenized sequence (Default = false)
        nbest_size: sampling parameters for unigram. Invalid for BPE-Dropout.
                    nbest_size = {0,1}: No sampling is performed.
                    nbest_size > 1: samples from the nbest_size results.
                    nbest_size < 0: assuming that nbest_size is infinite and samples
                      from the all hypothesis (lattice) using
                      forward-filtering-and-backward-sampling algorithm.
        alpha: Soothing parameter for unigram sampling, and merge probability for
          BPE-dropout.
      """

      _sentencepiece_processor_init_native(self)
      self._out_type = out_type
      self._add_bos = add_bos
      self._add_eos = add_eos
      self._reverse = reverse
      self._enable_sampling = enable_sampling
      self._nbest_size = nbest_size
      self._alpha = alpha
      if model_file or model_proto:
        self.Load(model_file=model_file, model_proto=model_proto)


    def Encode(self,
               input,
               out_type=None,
               add_bos=None,
               add_eos=None,
               reverse=None,
               enable_sampling=None,
               nbest_size=None,
               alpha=None):
      """Encode text input to segmented ids or tokens.

        Args:
        input: input string. accepsts list of string.
        out_type: output type. int or str.
        add_bos: Add <s> to the result (Default = false)
        add_eos: Add </s> to the result (Default = false) <s>/</s> is added after
          reversing (if enabled).
        reverse: Reverses the tokenized sequence (Default = false)
        nbest_size: sampling parameters for unigram. Invalid for BPE-Dropout.
                    nbest_size = {0,1}: No sampling is performed.
                    nbest_size > 1: samples from the nbest_size results.
                    nbest_size < 0: assuming that nbest_size is infinite and samples
                      from the all hypothesis (lattice) using
                      forward-filtering-and-backward-sampling algorithm.
        alpha: Soothing parameter for unigram sampling, and merge probability for
          BPE-dropout.
      """

      if out_type is None:
        out_type = self._out_type
      if add_bos is None:
        add_bos = self._add_bos
      if add_eos is None:
        add_eos = self._add_eos
      if reverse is None:
        reverse = self._reverse
      if enable_sampling is None:
        enable_sampling = self._enable_sampling
      if nbest_size is None:
        nbest_size = self._nbest_size
      if alpha is None:
        alpha = self._alpha

      if enable_sampling == True and (nbest_size is None or nbest_size == 0 or
                                          nbest_size == 1 or alpha is None or
                                          alpha <= 0.0 or alpha > 1.0):
        raise RuntimeError(
            'When enable_sampling is True, We must specify "nbest_size > 1" or "nbest_size = -1", '
            'and "0.0 < alpha < 1.0". "nbest_size = -1" is enabled only on unigram mode and '
            'samples from all candidates on the lattice instead of nbest segmentations. '
        )

      def _encode(text):
        if out_type is int:
          if enable_sampling:
            result = self.SampleEncodeAsIds(text, nbest_size, alpha)
          else:
            result = self.EncodeAsIds(text)
        else:
          if enable_sampling:
            result = self.SampleEncodeAsPieces(text, nbest_size, alpha)
          else:
            result = self.EncodeAsPieces(text)

        if reverse:
          result.reverse()
        if add_bos:
          if out_type is int:
            result = [self.bos_id()] + result
          else:
            result = [self.IdToPiece(self.bos_id())] + result

        if add_eos:
          if out_type is int:
            result = result + [self.eos_id()]
          else:
            result = result + [self.IdToPiece(self.eos_id())]

        return result

      if type(input) is list:
        return [_encode(n) for n in input]

      return _encode(input)


    def Decode(self, input):
      """Decode processed id or token sequences."""

      if not input:
        return self.DecodeIds([])
      elif type(input) is int:
        return self.DecodeIds([input])
      elif type(input) is str:
        return self.DecodePieces([input])

      def _decode(input):
        if not input:
          return self.DecodeIds([])
        if type(input[0]) is int:
          return self.DecodeIds(input)
        return self.DecodePieces(input)

      if type(input[0]) is list:
        return [_decode(n) for n in input]

      return _decode(input)


    def piece_size(self):
      return self.GetPieceSize()


    def vocab_size(self):
      return self.GetPieceSize()


    def __getstate__(self):
      return self.serialized_model_proto()


    def __setstate__(self, serialized_model_proto):
      self.__init__()
      self.LoadFromSerializedProto(serialized_model_proto)


    def __len__(self):
      return self.GetPieceSize()


    def __getitem__(self, piece):
      return self.PieceToId(piece)


    def Load(self, model_file=None, model_proto=None):
      """Overwride SentencePieceProcessor.Load to support both model_file and model_proto.

      Args:
        model_file: The sentencepiece model file path.
        model_proto: The sentencepiece model serialized proto. Either `model_file`
          or `model_proto` must be set.
      """
      if model_file and model_proto:
        raise RuntimeError('model_file and model_proto must be exclusive.')
      if model_proto:
        return self.LoadFromSerializedProto(model_proto)
      return self.LoadFromFile(model_file)


# Register SentencePieceProcessor in _sentencepiece:
_sentencepiece.SentencePieceProcessor_swigregister(SentencePieceProcessor)

class SentencePieceTrainer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    @staticmethod
    def _TrainFromString(arg):
        return _sentencepiece.SentencePieceTrainer__TrainFromString(arg)

    @staticmethod
    def _TrainFromMap(args):
        return _sentencepiece.SentencePieceTrainer__TrainFromMap(args)

    @staticmethod
    def _TrainFromMap2(args, iter):
        return _sentencepiece.SentencePieceTrainer__TrainFromMap2(args, iter)

    @staticmethod
    def _TrainFromMap3(args):
        return _sentencepiece.SentencePieceTrainer__TrainFromMap3(args)

    @staticmethod
    def _TrainFromMap4(args, iter):
        return _sentencepiece.SentencePieceTrainer__TrainFromMap4(args, iter)

    @staticmethod
    def Train(arg=None, **kwargs):
      """Train Sentencepiece model. Accept both kwargs and legacy string arg."""
      if arg is not None and type(arg) is str:
        return SentencePieceTrainer._TrainFromString(arg)

      def _encode(value):
        """Encode value to CSV.."""
        if type(value) is list:
          if sys.version_info[0] == 3:
            f = StringIO()
          else:
            f = BytesIO()
          writer = csv.writer(f, lineterminator='')
          writer.writerow([str(v) for v in value])
          return f.getvalue()
        else:
          return str(value)

      sentence_iterator = None
      model_writer = None
      new_kwargs = {}
      for key, value in kwargs.items():
        if key in ['sentence_iterator', 'sentence_reader']:
          sentence_iterator = value
        elif key in ['model_writer']:
          model_writer = value
        else:
          new_kwargs[key] = _encode(value)

      if model_writer:
        if sentence_iterator:
          model_proto = SentencePieceTrainer._TrainFromMap4(new_kwargs,
                                                           sentence_iterator)
        else:
          model_proto = SentencePieceTrainer._TrainFromMap3(new_kwargs)
        model_writer.write(model_proto)
      else:
        if sentence_iterator:
          return SentencePieceTrainer._TrainFromMap2(new_kwargs, sentence_iterator)
        else:
          return SentencePieceTrainer._TrainFromMap(new_kwargs)

      return None


# Register SentencePieceTrainer in _sentencepiece:
_sentencepiece.SentencePieceTrainer_swigregister(SentencePieceTrainer)

def SentencePieceTrainer__TrainFromString(arg):
    return _sentencepiece.SentencePieceTrainer__TrainFromString(arg)

def SentencePieceTrainer__TrainFromMap(args):
    return _sentencepiece.SentencePieceTrainer__TrainFromMap(args)

def SentencePieceTrainer__TrainFromMap2(args, iter):
    return _sentencepiece.SentencePieceTrainer__TrainFromMap2(args, iter)

def SentencePieceTrainer__TrainFromMap3(args):
    return _sentencepiece.SentencePieceTrainer__TrainFromMap3(args)

def SentencePieceTrainer__TrainFromMap4(args, iter):
    return _sentencepiece.SentencePieceTrainer__TrainFromMap4(args, iter)



import re
import csv
import sys
from io import StringIO
from io import BytesIO


def _add_snake_case(classname):
  """Added snake_cased method from CammelCased method."""

  snake_map = {}
  for k, v in classname.__dict__.items():
    if re.match(r'^[A-Z]+', k):
      snake = re.sub(r'(?<!^)(?=[A-Z])', '_',
                     k).lower().replace('n_best', 'nbest')
      snake_map[snake] = v
  for k, v in snake_map.items():
    setattr(classname, k, v)


def _batchnize(classname, name):
  """Enables batch request for the method classname.name."""
  func = getattr(classname, name, None)

  def _batched_func(self, arg):
    if type(arg) is list:
      return [func(self, n) for n in arg]
    else:
      return func(self, arg)

  setattr(classname, name, _batched_func)


_sentencepiece_processor_init_native = SentencePieceProcessor.__init__
setattr(SentencePieceProcessor, '__init__', SentencePieceProcessor.Init)

SentencePieceProcessor.Tokenize = SentencePieceProcessor.Encode
SentencePieceProcessor.Detokenize = SentencePieceProcessor.Decode

for m in [
    'PieceToId', 'IdToPiece', 'GetScore', 'IsUnknown', 'IsControl', 'IsUnused',
    'IsByte'
]:
  _batchnize(SentencePieceProcessor, m)

_add_snake_case(SentencePieceProcessor)
_add_snake_case(SentencePieceTrainer)



