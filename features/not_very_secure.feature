Feature: Not very secure

  Scenario Outline: One of many test cases
    Given string = <string>
    When function 'not_very_secure' is called with these params
    Then function 'not_very_secure' returns <result>

    Examples:
    | string                           | result |
    | "Mazinkaiser"                    | True   |
    | "hello world_"                   | False  |
    | "PassW0rd"                       | True   |
    | "     "                          | False  |
    | ""                               | False  |
    | "\n\t\n"                         | False  |
    | "ciao\n$$_"                      | False  |
    | "__ * __"                        | False  |
    | "&)))((("                        | False  |
    | "43534h56jmTHHF3k"               | True   |
    | "V_ c2k"                         | False  |
    | "v3BmBt6uFJJZzCPS7N_FPSmeKVHq7"  | False  |
    | "j7yXHfMZuFYfiLIazP9Qes5CX"      | True   |
    | "53TOjjfz15JpX_0e UXB"           | False  |
    | "2a72Rs7u"                       | True   |
    | "JO8 k01"                        | False  |
    | "49e28a"                         | True   |
    | "dybxRD7jtc49mZ1"                | True   |
    | "y2xGD"                          | True   |
    | "8jrSaWRQ8"                      | True   |
    | "e7tOevpd!49V"                   | False  |
    | "q"                              | True   |
    | "GvJzYce rD !j8y Jcz"            | False  |
    | "w34QPQNTq1s8SWpvqT7rc"          | True   |
    | "_S3S0OKKjojtaDtRpcvacY yGb7uBY" | False  |
    | "rPF7uVGZ"                       | True   |
    | "Qb_WZjkvG5KpcGPDFr"             | False  |
    | "SeCnT6Y 5HQC7urcPYvXFC531tYS4"  | False  |
    | "exfnm5JO 53u!h3qX5nHysenfunD"   | False  |
    | "XgKfq8XSKQleZCggIr"             | True   |
    | "_5pgbNOA3"                      | False  |
    | "w8!s"                           | False  |
    | "yTDdnzHxRvyNidugkYIhDW"         | True   |
    | "2PFzgV d7d3iF8eM8Whc"           | False  |
    | "xUxCmQZj"                       | True   |
    | "TQ"                             | True   |
    | "BLhy1CIf8c"                     | True   |
    | "APiIHRa0"                       | True   |
    | "SX"                             | True   |
    | "3FRzNN_sK7UCXljB"               | False  |
    | "yU!sSxHYVJwlBfrfU6RPXFry mLdZy" | False  |
    | "JS jth6I4v4AiqbXyXWo tMl4kUP"   | False  |
    | "f8kzX"                          | True   |
    | "PbVV1Hrv"                       | True   |
    | "KhcOP0U KFqG6C_IQTIhxOkiW9WBR"  | False  |
    | "3VOFW"                          | True   |
    | "nPNvvUozr"                      | True   |
    | "aCG0k!"                         | False  |
    | "xDQG8zvmh_kvhx rJ0S0HiwaHZys"   | False  |
    | "vzgryXuLtvsO9_2SaCjH7HzXb8D"    | False  |