#collatz conjecture script

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import PySimpleGUI as sg
import random as r
import os

numList=[]
numTitle=0

info_enabled=False
view_enabled=False
go_enabled=False

tahoma10='"Tahoma" 10'
tahoma12='"Tahoma" 12'
tahoma14='"Tahoma" 14'

image_base64=b'iVBORw0KGgoAAAANSUhEUgAAAMIAAABACAMAAAB/R1jQAAAAP1BMVEVHcEz///////////////////////////////////////////////////////////////////////////////9KjZoYAAAAFXRSTlMAM0mGGQ4mAlMHPf5beajPu26VZebk/Tw1AAAF+UlEQVRo3u1a67qrKAzlHqGAAr7/s04CVm137Rlbe8bOt/OnrXuLWeS6iIz9ylcL/B8Q2G9HwHv+CUvA30MgLqk+DkheXub+Vnj08RkEoC7yI08wvH4o2wDAxywGLI7TDrrOdGL3ArY93RV+uzMiuGCsFlHj6so81dGotxCoS257oMTQ6UHvXED1ihTmMcf1VuLOcJZ8JwZHrlrKIDZ3WkmR/Ot2oEgozdBWRabizqXA8rqKlFqtnAIYDAqEYl3CbMczY91FbbpBx9jwekIBXLubfNVnFgLfmV+r1aweCiwXKprBMK8UupHFXTKgL1tmUKMCluUREKAI6ALfFwgi0N26jFLUgAJVpBAl4LYH7lmuy1ljmbmYWUmtJtE1pY/4kYcDILzmhSZgJGFA9TBd8aov7ScXzCfWedO8JS9P6eQkju51BEEeAAHVoUWDNHvWUkBVEe+dNVC8Z0A/8TdGVid10RgOKW8qQBBAHmIFZci2Ru8zQ4/6AQvXPQaWIrpFwKsW0I0wVB06k8ALy8K8m8TQDYYg5HiMI5nO7wtmgOixglkWywwhJqZ7JVDhghejAOcYLxg1S85xfpIaKWRINvhDwtlJlQYLu+6OpbPoM0uTZXvD1CCwRPKMySgEyksjid7UICsRX28010nVobXHnaVNO1vr26wB8NZboEdhVIFO3jHNUcxNPzXJ1bHEG63yXUYKea89KfVk/ySra9Y0hU91tGsIQFG3t1fF/+cxqVuFAO5/P+2B3+mQ76wgku5eabjsf8qY1rFg+mGI8HUsdG0Fa7X+Qhr9VoPxC+F/C0Fb0CjVs5dmwXb2eyCI2JeS8oB5JSw9CfC0oSX+X7mIM0HAniXSrmfLnJzrOHWSbhODREZ4JivA6C0Wmg6IL8GiJ58ah/vuBK+Ow7mMYEbFOHW/mlo/7Z0ShTiMjXozFPi5IJSxS4MmQkoUouN90Y1BRVKUmFmoIsW1Il/KudwIQ8GIXBu2SO5jsAmeIDSdtZlEN7cy/dmKAoYCs2aG0EggxTXLTVV7lSkyeO9OZgQKheYgvEJAPqh7Q0dD0VVH6vJ0drA4kj9VKCg5Kjtx+UhTg9EwPiiPf4rqIcuwzF/MiTBYH0Ix0/Zm9CcdkPmVTqPPb7GxsyXVm9ORsKoLLGxELUXJqUrbqmah1qbxP7pk5BaTOV2DsdZNl6XNK3qb+Z632a6t0YPvv3zhF8IvhL8NAf50ivcBCK+dqc1ZHB5n+TeWfskK8DzH7RLXznqd/uPScBQE68QfjrXVg7+DaeXH3zYAwHwy0hmVoq1DK/O0hqlDIKjkBLXeVERWuizne7z0P+o4MY46dxYxzNy2ORBNPIVwA7YvQPPntLnZuPA7vOsKgT41i/0PHYOa+2D1kB/puooM9z1nmzuXDrthh7SFrzviWwav1BN8e6ygBWN9riMOs7K6XNn4AQRd/9WaIajrtEszwxvVLZrnNhB8NndGOQgCPhz9lokUOyeXJRcIAD8ggO5ColmOH5Nry3Efi/MZvwQhiKaQlTAc3Gr6b9wkalr4IAhgXcjKCmJ+Ps40VaqZpv6wArb0Sso2d56X0xgxde6sDPX4NKii6Fq7u0iT8IncHGYFpKe9tRSWuZING5Ch9kRV1WMIdADa157eD9ASE24ExpNvc2eXWaJxIYYD2vWJDodAAJaytR6tPXiaWurrfEmqpTz13V1tIN0ZTcblMnfGLUDObpEAa3SjKJhDF/OCrRKnCJO4aYw1JDgCwoBpQ45W47Z2g50PBZ6GMz5c1JO36GcIuAWq13QmHQTNnQmCD4an5cjN8EnUMeEs6hkGJvgkOqwLfCAHWEZuVwgYn6nPd6N1TKaJXh+Bfs6YmEyZzjQUF5JOFyTyLdOP49hvnq6b0kev34Awv1KlHfUC9T2DVRme6wJ6gtXqx2aZllOXQ1rdqi36WK0Y9BqJ1ZQY7hnyXBceL7wHwzC2inrTrcxf/sXbAFh5fzjC8jZeU/Szrxea6QXJl9tJEx6+unHttT9PRtDi30566hs5/OsxWM2+XM5igX8AxTs+PPPbqMYAAAAASUVORK5CYII='
icon_base64=b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAx5JREFUSEvtVjtoFFEUPXd23q5aiEpmi1UEg0FjfkIqk8qIFkYEwYABxc4fiJWNoOAnBsEUFiLaaiGmEAQFFdQmoEVANyZ+UfCzRTYYsVB338y75s682SSbNUEwSZMHw+y82fs5n3d3CfO0aJ7qYqHwnDG/QPVcU92RiCr2muje4djP/J86ofKcorFc/6PAlOQWRALoDcoBhOZy0/UtxM7RMch18kyM+8WkuoBc/wgQs1EJe8jQdE1HoDLNVUrr0wBqtVI7kOv/SSpd1wROPAfwmMl0Ezs9ABrkWefXba3UbVkLcfIlrl9o9d1UnySOGu41Kt10EMzdAJZJnFbKE0Bk0fYBuKnz2c6k19DBoFsAvmulViZ1sd2ws16CHDKvmcxbNu5OB7yUKLhayG/4GLH2qo3YecBktvnDtY+Q+ZBCrv+Xm67f5DCtZNA1AIu1UqvCwhKU8urWFtSi78hVjyrvzQ0Au5ipyx95cc52fEW+x0ynyPHvxAw5CA4U8oPv5V2JOQo26uHBF+XCKK9xtKxwSElgA68LzQTcIwTHxpM2HQLzFdk3TE+JeLPOZ9tCpFVNJwU9E1YB2CPMEeOLAf3wk24PctUFZD4sV1q/m4I47C7TvET5v2sAd5MUEaqZTLs/XPssbMxrvAzgSCyBTZhSvn4FxuoK1hOpakKDSm6tv04unGmucov+YaEwpkh5jVlrsJs6v25vWeECgfcV8wO9oYFES0HuF1pLGovBZOX6f4Xndwri6lESqoj4DDEuFkeyx213T0PK7Z5Kh1QfIfBZaxJxZ4Qmcm8QmzQy18uHloHSjJig8YrwONmAuwA+j42sQRBaLHUDWqk25fu7Y32LSu23Wi0D4ZPDwZbY1SlvaA0jcYkpOKGHB7PRpBLTDdUTJ84zsD2cEeITMl0lVwfsdhLxBgDfCPykqJJ3pTNBywZeGOT4d+QohUdLDOUENyJ5ItSTdR43LZnEXjFbHGccc3umkfkv4/QvI7PytLe/x5XGYjwOJ76TvYjCaM04Mi27E2OiyIU/ApUFmYXdBapngdRpj9Oc1SsVmjeN/wD2mIjeMDpfvQAAAABJRU5ErkJggg=='

go_base64=b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAARVBMVEX///////////////////////////////9HcEz////////////////////////////////////////////////////////9mtPbAAAAFnRSTlMB8DPBGdROAwALsl33bYWQe+M+o8onBZnxpAAAAmNJREFUSMedVgmWgyAMBWQVxK3m/kedJKDVqp0ZaV9LIJ+ELCTCn4ZwTmwzd7F/4ucVF3C43cItRBCXtrk1o5SjaXPUhBf3EASE2CagkepfGwNvXEJQROgMgGwHq3QIWtmhlQCmCwdBYi/CvgCaTu9toGODILsXJN6I0CPA8hz5cVR7WQT14Y0RG0I3IDv3eVkyiOskNHrDiBWxGDCqmOxj4JLCzWXFiPqrzf6gEwhVMHpjZumhgSbcIfiixFB0Lr72PR1yi2A5BvrCIZi2INU3BPEoCZZ5ECJEMNB9RxCmAxOEYAgRL3eKvnN8v8rBAj9hrCJ/EWNhDAxwPkKzyXA8/BXlXAMR2QnU8mx125e/CC0B0ItJ6s18Ks9zntiQuLUM8zws1YVo6JTQn5h0lrHlhj0nCfQUl07kQmW/+rClS2NQZRhKaJFHU56mQcKAmiMlu2XBmMxFCScGhldo8RakSHsRAJNmgsSpMCVQlYEVQouZbaXHFbbR3CrvZ5iZwkm/nWlc8YouHkJfReG2fDBMISqip4vPdfFMkInDmmYwUeYoNU16pfA7FUbPxr2CCFOstIfID8heMYvWjTk3ZDJU010rdrh+X1yAdvdI3Vz/aGRMG5I/EgSp6dLIB1dmGKPWFm8z+HtXVmh9gEqIjJFU2cIni2PA7MMSFyksB+07xZdiSn2G5X+D320p5vZJJXylb1Ps34n84Ll48ig9ePqePLBPnvEHxeJdkvyfS1I9KN0VvnRR+E7l1XF1/VpeP4v4Or4V8XerkLhVwPFrq/CkIXnU9uyaK+yu3J+aq3MLd7H/A9kJVWh9iZ38AAAAAElFTkSuQmCC'
go_disabled_base64=b'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'
info_base64=b'iVBORw0KGgoAAAANSUhEUgAAACYAAAAmCAMAAACf4xmcAAAAOVBMVEVHcEz///////////////////////////////////////////////////////////////////////99PJZNAAAAEnRSTlMAVo6dNA+6AgTKb+Cl6kAlcHqe2jmqAAABTElEQVQ4y51UC7KDIAwMCCRo1Tb3P+wLFiRRO8M8ZlQgy27MB4D/DCRCGeX9G0Q/F5pJnjBPKec0zaFuPKDinPkceY5wV5YNt4h1TZP3U1plurgboVC9xJJc/K6jS7J8RYsTlOjlrcxIRjFuZcfisKA8iTNtVybkC075hyCKn+oJti/CR3Q7HYITrnugCITPdVxcOFc9xD3nvZoIMy/xPDQzh2aBiXmqzAiBeW4ylDk16sOBU4ggFZ3ziFOehaC8c02I4M1rNPlQsYorvw+K4k3Slm3TZ1L1tM+++zvzfp7SHFkF7fA0KJjnXOdDsKvoBdZE7S9cYJ3DBuQC6wGx4bUwFV4xmWRpGPZk2dQbmE29KSQD04V0KUvynp7L0hQ59G6wRV5kVcsc6k8toxoQjgaE5wa8tjM+t/Po5XD818BVM3xxjV6Dw5fq7/EHJbcVNEpv1/sAAAAASUVORK5CYII='
info_disabled_base64=b'iVBORw0KGgoAAAANSUhEUgAAACYAAAAmCAYAAACoPemuAAAAAXNSR0IArs4c6QAAA7BJREFUWEfNWDFvEzEUfu9U5doBNR0YEQMqIzC0CImFpfAPQKILAiaGxsfQSrDcAlI7cE4HJkAsQYJ/AF1YQIgwACOdKsZKbSqGNhHKA5/s6J1rny9Jh0TKkpztz9/3ve/ZhzChHxwVV5qmEQCor/r0rXkKv6dpav8fXHZoYGmaTqVp+jc4M3tglDGVgSmG+M6TJFkAgKtEdAEAzgBAXWPpAMBvRPwJAJ+yLPtmMNpzlG2uEjAz4dra2myv17tDRMsAsFiRtTYitmq12uv19fUDbQEIyVsKjO8wSZKbRLQBAGcZoF0A+K4YIqID9TsizmoGLwHAafbsDiKuZln2Tv0WYs8LjLN0dHT0HBFvs0W2EPFFrVZ7r1hwMafZvUFE9/9LumSeIaI309PTDwx7PuacwDiobre7xWRrA8CqlPIj37UytwWuzxcUQlwDAMW2kb8dx/FSGTgvsMPDw1McFBFlc3Nzq6oijU80OG8UcD8p8Pv7+xuImOhN5OBmZmb+uOY5Bsyw1Wg0WkY+RHycZdlTnze4X1ze4QCTJHlERE/UXErWZrO57BpTAGYe0EZ/qwdnzWbz4ShZZHvPzNFoNJ4Z5hDxlioIG9wxxpRpu93uD1197Xq9foXlUEE2w8Te3t65KIpaeQvo95c3Nze3fVWn/djvdDpftOd24ji+aBfRAJjZTZIkDSKSuvQXVUCWLaI8J4R4CQB39QZeSSnv+RhmqiwQkSomFTEiy7ImH2NLOdXpdD7rnWxJKa+X5Y1Lep80XFYDQAjxQUfJQBlTzTkwzy6M9pV6o25RwFuQrzMwdVRo515GxII6Bli+uBBCAEAGALtxHM/7wtNh6kEfDSU6H6v9vK07RCKllAa0Dcx4JSijDU6HKJjwDfVRswEmZ8GbBSl9D5VIkjO1srIyH0XRL12V58uqklW4UclJRsH8Qoivyvgq5atkl8ebpZVsA2OZ1pZSXjb/TzawkN4hKVVFskwaijGWgQVfj2X+MaXM/Rky/0hxMQ4wpUKVuMjRW5IEA3ZUYJUDllVKxJprMMvGAGbL6G5Jui3lcg7ZxF1Mhxq/a0x5E2e6Vz72OCwQBKbWqXzssZr5oLlWCVtzbFZzmOO3K2LGOiiOcrSu0hf1xlWBDX+0dnT+wQ0pdBlxXWRP9DLCJdU5472+8b5nHQQL7zZO7Ppmgxv2wquYUte/Xq93shdenmvmqDsxrwhcZ/SJealigZu811Au9kIRMe6YSu/HPGE5Wa86h2FqnGf/AdkAWmPhCMEnAAAAAElFTkSuQmCC'
clear_base64=b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAMAAAAM7l6QAAAANlBMVEVHcEz///////////////////////////////////////////////////////////////////+GUsxbAAAAEXRSTlMAbOlO+Q18A1veOgj1MIvNrI5H7JwAAACwSURBVCjPvZLJFsMgCEVR0+CY9v3/z9YhDskirFoW4cCN+ECI/mPM15DuYXhNu58l/9Fx6xbf6kotoN004Jj1mRQ2tVb0DqnzSs3Qwy2jRrgjmuxCTVTPFnvDlfqcs87mgKunjpkOaF/aNoAtfwFm4HK20FO9bZ9wYqYEnfotGR1bpswD71li6B2Y2EROrJ7xY3FBmtTYOhZ9jkUvY5GGKj2J9KDSOkjLJK2itMg/sC8oSwzGWKLwbgAAAABJRU5ErkJggg=='
exit_base64=b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAMAAAAM7l6QAAAAPFBMVEX///////////////////////////////9HcEz////////////////////////////////////////////hvLLZAAAAE3RSTlMD7SAHnesCPAABgMiiLd/38b1h7eoplwAAALdJREFUKM+Fk9sSwyAIRIlGlKS5lf//19rmAtoYNg+Z8cwqwgrpUbD/EJSwwkSlBwuc4RSVXCKFMbmNtZbh4l8MG4+96BX4fdYE2TzxiProyONph/xF7pO/6vaAc40JtN17rNwKU5qcnF1jSn5Z47EgmE4BDhwOfuGicQN3O1ebe9HOUTC5OYi6wLy6zO9xqLGxuVmaXAxuLma15ampxUjofyTNgf7iAM04GGGyomgE2XoG1iNq6wOCABqwuhVsDQAAAABJRU5ErkJggg=='
view_base64=b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAwZJREFUSEvFl0uIjmEUx39noyzERti5hEYaI0lJKYSdGbcikeSWQiQlM2ZMKTuUMLIgUS6DHUIpKUnNSCYjlx2ywexsjve8c57pzOv75mZ886y+nu8853/O/zn/85xXGMBS1bHAcmAZsACYCozxo13AR+AF8Ah4KCI/+3MrfRmo6kRgF7AJmNafM///A3AVOC8iX8udKQusqtuAZmCSH+4E7mdZPwPeAz98fxwwPct2EbASmOH7X4B6EblUCrwksKqeBvb6gefAKeCeiPzuh6FRwKosqP0Z5Qvd9oyI7Cue+wtYVa8BG9ywATiZAFXVHJddBbvDwHE3vi4iG+PBXsAhUyuYzSJy14wNsL9sk9Noq6q1WSFe8ULslXkPsKquA264gzoDLQKqag0wD6gGxrvtd+A18EpE2ooBOPgd318vIjftdw7scunwQmoQkeYSkR8K91aO7rwekvPkQ1XrnXYruCqTWwJOf7RnmdaEAyans1lGqwOSOX8DfPO9CcDsQlCtwB6TU/BlbMwB8sSkkG1OsbNgtN4K+m0BzkU6Y9p+DVuDGkzPa5N9oLw767BhhrOsiFS1Cnjs1Nv+DhF5Eu5vMmCB2WoTkc/hvyWABWkNx0CWikiHK+Kt79cZ8AVzDORV5ww8dVqsaawwx0FKR12nsWXavTYEWi0wY86obQcW270G1bQYcOI+r7gQSK9onYnGrBaPeXYWlK3UqZpEpDGAR9ZaRGRnUE67Af9ynU3JmsVowOiwlQLJNayqloXJxjJtAk643REPxrRfndjxM1Gic73NfgK6DFjdgfXkVMGtIrIm0etOrBmYHjtFZGahsN555j36z7XaHfBtV0Ve6X7vjCjwiFE9YsXVl5xMCrWFgrHKPlCYQErJ6YHfe1k5paIZbAOZ7wX2cqgNxOap9ED8a8vc7c3IYuq7ZXpf/h+PxMHCFfV+JAb4LFojiOPM8DyLDl75QSC8LGnIq9zoE8ArP+yVyNy2KjPeBvDKD/QB3Gau7cCWQX7CXAYuDukTpvDsDftH2x+CL42LpQ1MwwAAAABJRU5ErkJggg=='
view_disabled_base64=b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAA5FJREFUSEvFV11oXUUQ/uaeTaEP5vgitm/V0kpEYopIoRQKKupbU20Kimjk7o0pBVsqUihtTC0IvqVCMd47F6IUhUZjfLNFBUEKUoQ0FIspUd9S8cWTvDV77pg57IZNmpukP0nydLM7O9/Mt/PNziGs4q+npyfN8/xFInqBiHaLyOMAHvJHZ4joTxH5VUR+SJLkcrVazVZyS8sZdHd3bzHG9AJ4A8D2lZz5/UkAF5xzg0NDQ7eanWkKbK0tAzgLYKs/PAHgexH5pVQq3UyS5D9dz/P84UajsYOI9gJ4GcBObz81t32ametLgS8JbK09B+Bdf+CKiAxMT09/Nzw8fHu5rLu6uja1trbuJ6JjAPZ420+Y+ejic3cAW2u/BPCaN+zLsuzjAKiOlwOO7dI0PQHgQ2//FTO/Hp9dABxlOiMib9br9VE1VsCVsg1OY9tyudxJRF/4QlyQ+TxwuVzuIqKL6kBEDijoYsBKpdIhIs8AaAfwiAf7F8A4Ef1Wq9XGFgfgwb/1fg/V6/Vh/V0Aq1wajcYNX0h9zHx2icjfj+6tGeNFPQTnwYe19rSnfapUKrWp3ArgsEFE12q1Wkc44OV0fi6jVyKkKwCuA/jHrz0K4KlFQY04546onIKvSqUyJiJPAygSozjbQLE69LR+Hem3SkSfxnTGaXv7tyM1TBLRwWAfUV5kTdHCZJZlT2oRWWvbAPzoqdeG0MPMPwWg3t7ebbOzsx36f0tLy9jg4ODfYc9a+xyAqg9Ytfw8M9/QzNM0/V3XNUGy1n6mjgEUVacMiMjPnpYJY8xL6jhIKU3TUwBUp/MtE8AAM/cFWjWwPM9H1YdeHxHt03uNVFOlwL2IFBUXBbIgWs9E/1zRfxB1Mv0ZOtUZZu6PCipmrcrM7wTlFMFYa6c1emPMY865zQCUDpVUEUichXNu3Gd6Jsuyj9QuTdOTPpgZY0x7YEcDjSVKRLu0zTrn/gIwo8CiDpxzW40xoYJHmPnVQK93os1A9TjBzE/EhWWt/UMzj/Wv+56lb7wqiko3xiiT2FDgjaF6I4urqZy0+pIk6YwLxlqrlX18JTk55y7pvTeV0300kGd9A7l6Tw3kAbfMw74ZaUzLt8y1eiSMMe/FV3THI7HKZ1Hf6niceTDPonrZkEEgelnCkLd+o08Evv7D3hKZ69L6jLcR+PoP9AHcz1wVAG/d5SfM58652j19wsR6WYuPtv8BWyxh2lRUjNQAAAAASUVORK5CYII='

def is_valid_input(value):
    # Allow only numbers, symbols, and empty input
    allowed_characters = "0123456789"
    return all(char in allowed_characters for char in value)

def drawPlot(amounts):
    global numTitle
    
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title('sequence graph') # set title
    
    # Plot the main sequence
    ax.plot(amounts, label='Sequence', color='blue')
    
    # Highlight the last three points (if they exist)
    if len(amounts) >= 3:
        ax.scatter(range(len(amounts)-3, len(amounts)), amounts[-3:], color='red', label='4-2-1 Loop', zorder=5)
    
    # Set titles and labels
    ax.set_xlim(0, len(amounts))  # Set x-axis limit
    ax.set_ylim(0, max(amounts) + 10)  # Set y-axis limit slightly above the max value
    ax.set_xlabel('Term')
    ax.set_ylabel('Value')
    ax.set_title(f'Collatz Conjecture Sequence of {numTitle}')
    ax.legend()  # Add a legend for clarity

    plt.show(block=False)

def getList(num):
    global numTitle, terms_until_loop, largest_term
    numTitle=num
    numList.append(num)
    while num != 1:
        if '.5' in str(num/2):
            num = num * 3 + 1
        else:
            num = num / 2
        numList.append(num)
    drawPlot(numList)

    terms_until_loop = len(numList)
    largest_term = max(numList)

sg.theme('pythonplus')
mainLayout = [ [sg.Push(), sg.Image(image_base64), sg.Push()],
               [sg.Radio('Set Number', group_id=1, default=True, key='set', font=tahoma10, enable_events=True), sg.Radio('Random In Range', group_id=1, default=False, key='random', font=tahoma10, enable_events=True)],
               [sg.Text('Enter starting number: ', font=tahoma12, text_color='snow', key='prompt'), sg.Input(key='INPUT', size=(20,1), background_color='deepskyblue2', text_color='navy', font=tahoma14, enable_events=True),
                sg.Button('', image_data=clear_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='Clear')],
               [sg.Button('', image_data=go_disabled_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='GO'),
                sg.Button('', image_data=info_disabled_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='Info'),
                sg.Button('', image_data=view_disabled_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='View'), sg.Push(),
                sg.Button('', image_data=exit_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='Exit')] ]

mainWindow = sg.Window('Soup\'s Collatz Conjecture Grapher', mainLayout, finalize=True)

while True:
    event, values = mainWindow.read()

    if event in ('Exit', sg.WIN_CLOSED):
        break

    if event == 'Clear':
        mainWindow['INPUT'].update('')
        mainWindow['GO'].update(image_data=go_disabled_base64)
        go_enabled=False

    if event == 'GO' and go_enabled:
        numTemp = int(current_value)
        if values['set']:
            getList(numTemp)
        elif values['random']:
            getList(r.randint(1,numTemp))
        mainWindow['Info'].update(image_data=info_base64)
        mainWindow['View'].update(image_data=view_base64)
        info_enabled=True
        view_enabled=True

    if event == 'Info' and info_enabled:
        sg.popup(f'''Chosen number: {numTitle}
Terms until loop: {terms_until_loop}
Largest term: {round(largest_term)}''', font=tahoma12, title='Stats')

    if event == 'View' and view_enabled:
        sg.popup_scrolled('\n'.join(map(str, numList)), font=tahoma10, text_color='white', size=(15,20), title='values')

    if event in ('set','random'):
        if values['set']:
            mainWindow['prompt'].update('Enter starting number')
        if values['random']:
            mainWindow['prompt'].update('Enter maximum value')

    if event == 'INPUT':
        current_value = values['INPUT']
        if not is_valid_input(current_value):
            # If invalid input detected, revert to the last valid state
            mainWindow['INPUT'].update(current_value[:-1])
            current_value=(current_value[:-1])

        if current_value != '' and current_value is not None:
            mainWindow['GO'].update(image_data=go_base64)
            go_enabled=True
        else:
            mainWindow['GO'].update(image_data=go_disabled_base64)
            go_enabled=False

    if go_enabled:
        mainWindow.bind('<Return>','GO')
mainWindow.close()
os._exit(0)
