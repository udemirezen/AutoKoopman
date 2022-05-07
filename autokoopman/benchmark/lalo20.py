import sympy as sp  # type: ignore

import autokoopman.core.system as asys


class LaubLoomis(asys.SymbolicContinuousSystem):
    r"""
    Laub-Loomis Benchmark (LALO20)
        They are boxes centered at :math:`x_1(0) = 1.2`, :math:`x_2(0) = 1.05`, :math:`x_3(0) = 1.5`, :math:`x_4(0) = 2.4`, :math:`x_5(0) = 1`, :math:`x_6(0) = 0.1`, :math:`x_7(0) = 0.45`.
        The range of the box in the :math:`i`-th dimension is defined by the interval :math:`[x_i(0) − W, x_i(0) + W ]`.

        We consider :math:`W = 0.01`, :math:`W = 0.05`, and :math:`W =0.1`. For :math:`W =0.01` and :math:`W =0.05` we consider the unsafe region defined by :math:`x4 \ge 4.5`,
        while for :math:`W = 0.1`, the unsafe set is defined by :math:`x4 \ge 5`. The time horizon for all cases is :math:`[0, 20]`.

        The dynamics are defined as

        .. math::
            \left\{\begin{array}{l}
            \dot{x}_{1}=1.4 x_{3}-0.9 x_{1} \\
            \dot{x}_{2}=2.5 x_{5}-1.5 x_{2} \\
            \dot{x}_{3}=0.6 x_{7}-0.8 x_{2} x_{3} \\
            \dot{x}_{4}=2-1.3 x_{3} x_{4} \\
            \dot{x}_{5}=0.7 x_{1}-x_{4} x_{5} \\
            \dot{x}_{6}=0.3 x_{1}-3.1 x_{6} \\
            \dot{x}_{7}=1.8 x_{6}-1.5 x_{2} x_{7}
            \end{array}\right.

        The system is asymptotically stable and the equilibrium is the origin.

    References
        Geretti, L., Sandretto, J. A. D., Althoff, M., Benet, L., Chapoutot, A., Chen, X., ... & Schilling, C. (2020).
        ARCH-COMP20 category report: Continuous and hybrid systems with nonlinear dynamics. EPiC Series in Computing, 74, 49-75. pp 59
    """

    def __init__(self):
        x1, x2, x3, x4, x5, x6, x7 = sp.symbols("x1 x2 x3 x4 x5 x6 x7")
        xdot = [
            1.4 * x3 - 0.9 * x1,
            2.5 * x5 - 1.5 * x2,
            0.6 * x7 - 0.8 * x2 * x3,
            2 - 1.3 * x3 * x4,
            0.7 * x1 - x4 * x5,
            0.3 * x1 - 3.1 * x6,
            1.8 * x6 - 1.5 * x2 * x7,
        ]
        super(LaubLoomis, self).__init__((x1, x2, x3, x4, x5, x6, x7), xdot)
