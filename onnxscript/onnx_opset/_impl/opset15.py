# --------------------------------------------------------------------------
# ⚠️ WARNING - AUTO-GENERATED CODE - DO NOT EDIT ⚠️
# ⚙️ Generated by 'python -m opgen'
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------
# pylint: disable=W0221,W0222,R0901,W0237
# ruff: noqa: N801,E741
# ruff: noqa: D214,D402,D405,D411,D412,D416,D417
# --------------------------------------------------------------------------

from __future__ import annotations

from typing import Optional as _Optional
from typing import Sequence, Tuple, TypeVar

from onnx import TypeProto
from onnx.defs import get_schema

from onnxscript.onnx_opset._impl.opset14 import Opset14
from onnxscript.onnx_types import (
    BFLOAT16,
    BOOL,
    COMPLEX64,
    COMPLEX128,
    DOUBLE,
    FLOAT,
    FLOAT16,
    INT8,
    INT16,
    INT32,
    INT64,
    STRING,
    UINT8,
    UINT16,
    UINT32,
    UINT64,
)
from onnxscript.values import Op, Opset


class Opset15(Opset14):
    def __new__(cls):
        return Opset.__new__(cls, "", 15)

    T = TypeVar("T", BFLOAT16, DOUBLE, FLOAT, FLOAT16)

    T1 = TypeVar("T1", BFLOAT16, DOUBLE, FLOAT, FLOAT16)

    T2 = TypeVar("T2", BFLOAT16, DOUBLE, FLOAT, FLOAT16)

    def BatchNormalization(
        self,
        X: T,
        scale: T1,
        B: T1,
        input_mean: T2,
        input_var: T2,
        epsilon: float = 9.999999747378752e-06,
        momentum: float = 0.8999999761581421,
        training_mode: int = 0,
    ) -> Tuple[T, T2, T2]:
        r"""[🌐 BatchNormalization(15)](https://onnx.ai/onnx/operators/onnx__BatchNormalization.html#batchnormalization-15 "Online Documentation")


        Carries out batch normalization as described in the paper
        https://arxiv.org/abs/1502.03167. Depending on the mode it is being run,
        There are five required inputs 'X', 'scale', 'B', 'input_mean' and
        'input_var'.
        Note that 'input_mean' and 'input_var' are expected to be the estimated
        statistics in inference mode (training_mode=False, default),
        and the running statistics in training mode (training_mode=True).
        There are multiple cases for the number of outputs, which we list below:

        * Output case #1: Y, running_mean, running_var (training_mode=True)
        * Output case #2: Y (training_mode=False)

        When training_mode=False, extra outputs are invalid.
        The outputs are updated as follows when training_mode=True:
        ::

            running_mean = input_mean * momentum + current_mean * (1 - momentum)
            running_var = input_var * momentum + current_var * (1 - momentum)

            Y = (X - current_mean) / sqrt(current_var + epsilon) * scale + B


        where:
        ::

            current_mean = ReduceMean(X, axis=all_except_channel_index)
            current_var =  ReduceVar(X, axis=all_except_channel_index)


        Notice that `ReduceVar` refers to the population variance, and it equals to
        `sum(sqrd(x_i - x_avg)) / N`
        where `N` is the population size (this formula does not use sample size `N - 1`).

        The computation of ReduceMean and ReduceVar uses float to avoid overflow for float16 inputs.

        When training_mode=False:
        ::

            Y = (X - input_mean) / sqrt(input_var + epsilon) * scale + B



        For previous (depreciated) non-spatial cases, implementors are suggested
        to flatten the input shape to (N x C * D1 * D2 * ... * Dn) before a BatchNormalization Op.
        This operator has **optional** inputs/outputs. See `ONNX <https://github.com/onnx/onnx/blob/master/docs/IR.md>`_ for more details about the representation of optional arguments. An empty string may be used in the place of an actual argument's name to indicate a missing argument. Trailing optional arguments (those not followed by an argument that is present) may also be simply omitted.


        Args:
            X: (differentiable) Input data tensor from the previous operator; dimensions
                are in the form of (N x C x D1 x D2 ... Dn), where N is the batch size,
                C is the number of channels. Statistics are computed for every channel
                of C over N and D1 to Dn dimensions. For image data, input dimensions
                become (N x C x H x W). The op also accepts single dimension input of
                size N in which case C is assumed to be 1

            scale: (differentiable) Scale tensor of shape (C).

            B: (differentiable) Bias tensor of shape (C).

            input_mean: (differentiable) running (training) or estimated (testing) mean
                tensor of shape (C).

            input_var: (differentiable) running (training) or estimated (testing)
                variance tensor of shape (C).

            epsilon: The epsilon value to use to avoid division by zero.

            momentum: Factor used in computing the running mean and variance.e.g.,
                running_mean = running_mean * momentum + mean * (1 - momentum).

            training_mode: If set to true, it indicates BatchNormalization is being used
                for training, and outputs 1, 2, 3, and 4 would be populated.
        """

        schema = get_schema("BatchNormalization", 15, "")
        op = Op(self, "BatchNormalization", schema)
        return op(
            *self._prepare_inputs(schema, X, scale, B, input_mean, input_var),
            epsilon=epsilon,
            momentum=momentum,
            training_mode=training_mode,
        )

    T1 = TypeVar("T1", DOUBLE, FLOAT, FLOAT16)

    T2 = TypeVar(
        "T2",
        BFLOAT16,
        BOOL,
        DOUBLE,
        FLOAT,
        FLOAT16,
        INT16,
        INT32,
        INT64,
        INT8,
        UINT16,
        UINT32,
        UINT64,
        UINT8,
    )

    def Bernoulli(
        self, input: T1, dtype: _Optional[int] = None, seed: _Optional[float] = None
    ) -> T2:
        r"""[🌐 Bernoulli(15)](https://onnx.ai/onnx/operators/onnx__Bernoulli.html#bernoulli-15 "Online Documentation")


        Draws binary random numbers (0 or 1) from a Bernoulli distribution. The input tensor should be a tensor
        containing probabilities p (a value in the range [0,1]) to be used for drawing the binary random number,
        where an output of 1 is produced with probability p and an output of 0 is produced with probability (1-p).

        This operator is non-deterministic and may not produce the same values in different
        implementations (even if a seed is specified).


        Args:
            input: All values in input have to be in the range:[0, 1].

            dtype: The data type for the elements of the output tensor. if not
                specified, we will use the data type of the input tensor.

            seed: (Optional) Seed to the random generator, if not specified we will auto
                generate one.
        """

        schema = get_schema("Bernoulli", 15, "")
        op = Op(self, "Bernoulli", schema)
        return op(*self._prepare_inputs(schema, input), dtype=dtype, seed=seed)

    T1 = TypeVar(
        "T1",
        BFLOAT16,
        BOOL,
        DOUBLE,
        FLOAT,
        FLOAT16,
        INT16,
        INT32,
        INT64,
        INT8,
        STRING,
        UINT16,
        UINT32,
        UINT64,
        UINT8,
    )

    T2 = TypeVar(
        "T2",
        BFLOAT16,
        BOOL,
        DOUBLE,
        FLOAT,
        FLOAT16,
        INT16,
        INT32,
        INT64,
        INT8,
        STRING,
        UINT16,
        UINT32,
        UINT64,
        UINT8,
    )

    def CastLike(self, input: T1, target_type: T2) -> T2:
        r"""[🌐 CastLike(15)](https://onnx.ai/onnx/operators/onnx__CastLike.html#castlike-15 "Online Documentation")


        The operator casts the elements of a given input tensor (the first input) to
        the same data type as the elements of the second input tensor.
        See documentation of the Cast operator for further details.


        Args:
            input: (differentiable) Input tensor to be cast.

            target_type: (non-differentiable) The (first) input tensor will be cast to
                produce a tensor of the same type as this (second input) tensor.
        """

        schema = get_schema("CastLike", 15, "")
        op = Op(self, "CastLike", schema)
        return op(*self._prepare_inputs(schema, input, target_type))

    V = TypeVar(
        "V",
        Sequence[BOOL],
        Sequence[COMPLEX128],
        Sequence[COMPLEX64],
        Sequence[DOUBLE],
        Sequence[FLOAT],
        Sequence[FLOAT16],
        Sequence[INT16],
        Sequence[INT32],
        Sequence[INT64],
        Sequence[INT8],
        Sequence[STRING],
        Sequence[UINT16],
        Sequence[UINT32],
        Sequence[UINT64],
        Sequence[UINT8],
        BOOL,
        COMPLEX128,
        COMPLEX64,
        DOUBLE,
        FLOAT,
        FLOAT16,
        INT16,
        INT32,
        INT64,
        INT8,
        STRING,
        UINT16,
        UINT32,
        UINT64,
        UINT8,
    )

    O = TypeVar(
        "O",
        _Optional[Sequence[BOOL]],
        _Optional[Sequence[COMPLEX128]],
        _Optional[Sequence[COMPLEX64]],
        _Optional[Sequence[DOUBLE]],
        _Optional[Sequence[FLOAT]],
        _Optional[Sequence[FLOAT16]],
        _Optional[Sequence[INT16]],
        _Optional[Sequence[INT32]],
        _Optional[Sequence[INT64]],
        _Optional[Sequence[INT8]],
        _Optional[Sequence[STRING]],
        _Optional[Sequence[UINT16]],
        _Optional[Sequence[UINT32]],
        _Optional[Sequence[UINT64]],
        _Optional[Sequence[UINT8]],
        _Optional[BOOL],
        _Optional[COMPLEX128],
        _Optional[COMPLEX64],
        _Optional[DOUBLE],
        _Optional[FLOAT],
        _Optional[FLOAT16],
        _Optional[INT16],
        _Optional[INT32],
        _Optional[INT64],
        _Optional[INT8],
        _Optional[STRING],
        _Optional[UINT16],
        _Optional[UINT32],
        _Optional[UINT64],
        _Optional[UINT8],
    )

    def Optional(self, input: _Optional[V] = None, type: _Optional[TypeProto] = None) -> O:
        r"""[🌐 Optional(15)](https://onnx.ai/onnx/operators/onnx__Optional.html#optional-15 "Online Documentation")


        Constructs an optional-type value containing either an empty optional of a certain type specified by the attribute,
        or a non-empty value containing the input element.


        Args:
            input: (optional) The input element.

            type: Type of the element in the optional output
        """

        schema = get_schema("Optional", 15, "")
        op = Op(self, "Optional", schema)
        return op(*self._prepare_inputs(schema, input), type=type)

    O = TypeVar(
        "O",
        _Optional[Sequence[BOOL]],
        _Optional[Sequence[COMPLEX128]],
        _Optional[Sequence[COMPLEX64]],
        _Optional[Sequence[DOUBLE]],
        _Optional[Sequence[FLOAT]],
        _Optional[Sequence[FLOAT16]],
        _Optional[Sequence[INT16]],
        _Optional[Sequence[INT32]],
        _Optional[Sequence[INT64]],
        _Optional[Sequence[INT8]],
        _Optional[Sequence[STRING]],
        _Optional[Sequence[UINT16]],
        _Optional[Sequence[UINT32]],
        _Optional[Sequence[UINT64]],
        _Optional[Sequence[UINT8]],
        _Optional[BOOL],
        _Optional[COMPLEX128],
        _Optional[COMPLEX64],
        _Optional[DOUBLE],
        _Optional[FLOAT],
        _Optional[FLOAT16],
        _Optional[INT16],
        _Optional[INT32],
        _Optional[INT64],
        _Optional[INT8],
        _Optional[STRING],
        _Optional[UINT16],
        _Optional[UINT32],
        _Optional[UINT64],
        _Optional[UINT8],
    )

    V = TypeVar(
        "V",
        Sequence[BOOL],
        Sequence[COMPLEX128],
        Sequence[COMPLEX64],
        Sequence[DOUBLE],
        Sequence[FLOAT],
        Sequence[FLOAT16],
        Sequence[INT16],
        Sequence[INT32],
        Sequence[INT64],
        Sequence[INT8],
        Sequence[STRING],
        Sequence[UINT16],
        Sequence[UINT32],
        Sequence[UINT64],
        Sequence[UINT8],
        BOOL,
        COMPLEX128,
        COMPLEX64,
        DOUBLE,
        FLOAT,
        FLOAT16,
        INT16,
        INT32,
        INT64,
        INT8,
        STRING,
        UINT16,
        UINT32,
        UINT64,
        UINT8,
    )

    def OptionalGetElement(self, input: O) -> V:
        r"""[🌐 OptionalGetElement(15)](https://onnx.ai/onnx/operators/onnx__OptionalGetElement.html#optionalgetelement-15 "Online Documentation")


        Outputs the element in the optional-type input. It is an error if the input value does not have an element
        and the behavior is undefined in this case.


        Args:
            input: The optional input.
        """

        schema = get_schema("OptionalGetElement", 15, "")
        op = Op(self, "OptionalGetElement", schema)
        return op(*self._prepare_inputs(schema, input))

    O = TypeVar(
        "O",
        _Optional[Sequence[BOOL]],
        _Optional[Sequence[COMPLEX128]],
        _Optional[Sequence[COMPLEX64]],
        _Optional[Sequence[DOUBLE]],
        _Optional[Sequence[FLOAT]],
        _Optional[Sequence[FLOAT16]],
        _Optional[Sequence[INT16]],
        _Optional[Sequence[INT32]],
        _Optional[Sequence[INT64]],
        _Optional[Sequence[INT8]],
        _Optional[Sequence[STRING]],
        _Optional[Sequence[UINT16]],
        _Optional[Sequence[UINT32]],
        _Optional[Sequence[UINT64]],
        _Optional[Sequence[UINT8]],
        _Optional[BOOL],
        _Optional[COMPLEX128],
        _Optional[COMPLEX64],
        _Optional[DOUBLE],
        _Optional[FLOAT],
        _Optional[FLOAT16],
        _Optional[INT16],
        _Optional[INT32],
        _Optional[INT64],
        _Optional[INT8],
        _Optional[STRING],
        _Optional[UINT16],
        _Optional[UINT32],
        _Optional[UINT64],
        _Optional[UINT8],
    )

    B = TypeVar("B", bound=BOOL)

    def OptionalHasElement(self, input: O) -> B:
        r"""[🌐 OptionalHasElement(15)](https://onnx.ai/onnx/operators/onnx__OptionalHasElement.html#optionalhaselement-15 "Online Documentation")


        Returns true if the optional-type input contains an element. If it is an empty optional-type, this op returns false.


        Args:
            input: The optional input.
        """

        schema = get_schema("OptionalHasElement", 15, "")
        op = Op(self, "OptionalHasElement", schema)
        return op(*self._prepare_inputs(schema, input))

    T = TypeVar("T", BFLOAT16, DOUBLE, FLOAT, FLOAT16, INT32, INT64)

    T1 = TypeVar(
        "T1",
        BFLOAT16,
        DOUBLE,
        FLOAT,
        FLOAT16,
        INT16,
        INT32,
        INT64,
        INT8,
        UINT16,
        UINT32,
        UINT64,
        UINT8,
    )

    def Pow(self, X: T, Y: T1) -> T:
        r"""[🌐 Pow(15)](https://onnx.ai/onnx/operators/onnx__Pow.html#pow-15 "Online Documentation")


        Pow takes input data (Tensor<T>) and exponent Tensor, and
        produces one output data (Tensor<T>) where the function `f(x) = x^exponent`,
        is applied to the data tensor elementwise.
        This operator supports **multidirectional (i.e., Numpy-style) broadcasting**; for more details please check `Broadcasting in ONNX <https://github.com/onnx/onnx/blob/master/docs/Broadcasting.md>`_.

        Args:
            X: (differentiable) First operand, base of the exponent.

            Y: (differentiable) Second operand, power of the exponent.
        """

        schema = get_schema("Pow", 15, "")
        op = Op(self, "Pow", schema)
        return op(*self._prepare_inputs(schema, X, Y))

    T = TypeVar(
        "T",
        BFLOAT16,
        BOOL,
        COMPLEX128,
        COMPLEX64,
        DOUBLE,
        FLOAT,
        FLOAT16,
        INT16,
        INT32,
        INT64,
        INT8,
        STRING,
        UINT16,
        UINT32,
        UINT64,
        UINT8,
    )

    T1 = TypeVar("T1", bound=INT64)

    def Shape(self, data: T, end: _Optional[int] = None, start: int = 0) -> T1:
        r"""[🌐 Shape(15)](https://onnx.ai/onnx/operators/onnx__Shape.html#shape-15 "Online Documentation")


        Takes a tensor as input and outputs an 1D int64 tensor containing the shape of the input tensor.
        Optional attributes start and end can be used to compute a slice of the input tensor's shape.
        If start axis is omitted, the slice starts from axis 0.
        The end axis, if specified, is exclusive (and the returned value will not include the size of that axis).
        If the end axis is omitted, the axes upto the last one will be included.
        Negative axes indicate counting back from the last axis.
        Note that axes will be clamped to the range [0, r-1], where r is the
        rank of the input tensor if they are out-of-range (after adding r in the case of
        negative axis). Thus, specifying any end value > r is equivalent to specifying an end
        value of r, and specifying any start value < -r is equivalent to specifying a start
        value of 0.

        Examples:

        ::

            Input tensor with shape: [2, 3, 4]
            No attributes specified.
            Output: [2, 3, 4]



        ::

            Input tensor with shape: [2, 3, 4]
            start: -1
            Output: [4]



        ::

            Input tensor with shape: [2, 3, 4]
            end: -1
            Output: [2, 3]



        ::

            Input tensor with shape: [2, 3, 4]
            start: 1
            end: 2
            Output: [3]




        Args:
            data: (non-differentiable) An input tensor.

            end: (Optional) Ending axis for slicing the shape. Negative value means
                counting dimensions from the back. If omitted, sizes of all axes upto
                (including) the last one will be included.

            start: (Optional) Starting axis for slicing the shape. Default value is
                0.Negative value means counting dimensions from the back.
        """

        schema = get_schema("Shape", 15, "")
        op = Op(self, "Shape", schema)
        return op(*self._prepare_inputs(schema, data), end=end, start=start)
