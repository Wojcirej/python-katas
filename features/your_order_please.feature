Feature: Your order please

  Scenario Outline: One of many test cases
    Given sentence = <sentence>
    When function 'your_order_please' is called with these params
    Then function 'your_order_please' returns <result>

    Examples:
    | sentence                                          | result                                            |
    | ""                                                | ""                                                |
    | "is2 Thi1s T4est 3a"                              | "Thi1s is2 3a T4est"                              |
    | "4of Fo1r pe6ople g3ood th5e the2"                | "Fo1r the2 g3ood 4of th5e pe6ople"                |
    | "d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6"  | "wha1t sh2all 3we d4o w5ith a6 dru7nken s8ailor"  |
    | "3 6 4 2 8 7 5 1 9"                               | "1 2 3 4 5 6 7 8 9"                               |
    | "lo2ok smal1l"                                    | "smal1l lo2ok"                                    |
    | "7look f5rom bi1g 4last w8ould 6way their2 gi3ve" | "bi1g their2 gi3ve 4last f5rom 6way 7look w8ould" |
    | "worl3d th2ey 1an"                                | "1an th2ey worl3d"                                |
    | "as1"                                             | "as1"                                             |
    | "w1ill problem2"                                  | "w1ill problem2"                                  |
    | "fee1l"                                           | "fee1l"                                           |
    | "w1oman"                                          | "w1oman"                                          |
    | "c1hild wo2man"                                   | "c1hild wo2man"                                   |
    | "c1hild 2at"                                      | "c1hild 2at"                                      |
    | "smal1l im2portant new3"                          | "smal1l im2portant new3"                          |
    | "time1 differ2ent"                                | "time1 differ2ent"                                |
    | "d2ay ma1ke"                                      | "ma1ke d2ay"                                      |
    | "ther1e"                                          | "ther1e"                                          |
    | "e1arly ge2t"                                     | "e1arly ge2t"                                     |
    | "t1o"                                             | "t1o"                                             |
    | "ove1r 2small"                                    | "ove1r 2small"                                    |
