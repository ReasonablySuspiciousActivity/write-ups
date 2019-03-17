import binascii

def chunk(input_data, size):
    return [input_data[i:i + size] for i in range(0, len(input_data), size)]


def xor(*t):
    from functools import reduce
    from operator import xor
    return [reduce(xor, x, 0) for x in zip(*t)]


def xor_string(t1, t2):
    t1 = map(ord, t1)
    t2 = map(ord, t2)
    return "".join(map(chr, xor(t1, t2)))

plaintext = """The Song of the Count

You know that I am called the Count
Because I really love to count
I could sit and count all day
Sometimes I get carried away
I count slowly, slowly, slowly getting faster
Once I've started counting it's really hard to stop
Faster, faster. It is so exciting!
I could count forever, count until I drop
1! 2! 3! 4!
1-2-3-4, 1-2-3-4,
1-2, i love couning whatever the ammount haha!
1-2-3-4, heyyayayay heyayayay that's the sound of the count
I count the spiders on the wall...
I count the cobwebs in the hall...
I count the candles on the shelf...
When I'm alone, I count myself!
I count slowly, slowly, slowly getting faster
Once I've started counting it's really hard to stop
Faster, faster. It is so exciting!
I could count forever, count until I drop
1! 2! 3! 4!
1-2-3-4, 1-2-3-4, 1,
2 I love counting whatever the
ammount! 1-2-3-4 heyayayay heayayay 1-2-3-4
That's the song of the Count!
"""

c = "9d5c66e65fae92af9c8a55d9d3bf640e8a5b76a878cbf691d3901392c9b8760ebd5c62b22c88dca9d1c55098cbbb644ae9406ba32c8293bdd29139bbc2b4605bba51238f2cb399a9d0894ad9cbb8774be9406ce66fae89a6c8ef7ad9c4b87442ad1470af78e19da6d8c55096d2b9750ea8586fe668a085c2ef8a5e9cd3be6c4bba144ae66ba488e8df84418bceb2650ea84362bf0688dcabd3905d8d87a46d414626be04a58215b84263a620de3203fa4626be08e2940da35c61b82c98201ce15438cd67eb921cf77c28a969de321bf4433ea24ca59216a25b7bb662996106e11639e75ae09015bb4c2fb76d8c254fe15e6ab45cea817391547cab698c6d4ff35039b34df7df599e412fb67fde3200b55432a441f19817b01405962c9d2e1af9556aa447f09f0df75360ad6988241db91129a85deb8559a25b7bb660de084ff1cc3a0e8041bc71d71fb29883931d9d3e8f784ca743b065c91ea386909e1a9100925f4fa742b1718c1efec4d4d609df5bcb3b17e417bd268d5fe6ced4d65b9c40d6305eeb1df03e9050e68bcad241dd15b46453b85dae7cd112b2c3c7ca50dd4ddf2c1ff350f5349c5febcadbd2509c40d6340aad03bd258d5bb2d8cdc647d814d1335efe18f8718651e7c5d6b9609c57d12010fe50e939801ee1dbcbd74cce4739c1eeceba8ef87360b629ed82a6eb9d508ee381bb88e97363bf20a1cfe7a7e07cccf3cea788bd277fb265e9cde4a9b937808aa7ee85f22679a365f5c4ede5f478c0e482ab95bd3c79f731e9c9a8b6ff7cc2e6c0e0c897047fb22ba1e5afa8b778c2ef80abcabd1a37b42af4c2fce5fa60dde582a8c7971a37b42af4c2fce5e475c1f782b7cabd207bb832edd5a4e5e4130a976ad4a2fe86ac99c18491f9f6c86adae59cc4a9f33072f70ca6daede5e40b049272c8e6b980b798c69e9fb7f7891611c7758df0fc82b481d1ca9eb8e2cd5f118f26def6f693d2abc99982bce2855f038175d9e7ebcdf8a4dcca9faab0da1045857eceebed8ab68a89e0bff9f3c60a098426ceedec8daccdce8584bce6cc0d49c065c2f7f797f898c69e9fb5b0e05f019269dd88a8c2f8df89cac5f8b09d00ad16dc760ead7c3518baed47603c5b5251cc269cae93d1f8a4888699aff58942c8529f304af0362143f2bd1e37670d538753992129ff3c6c5befb21e7331590c950ac26917be39644dfba50b2b70117fcbccba57b209ae95721a1c9d36073d934b75014109102be14fb6a044a7cf9e468748976457f6342177f5a9042630622f97d2ba5a8c04a7890d4e5fcb445b7600d7c1be71b711b6b32b4444f078557ef82e4f0559225437b455aa9a0bbaff89c834531a45115125c933d6cd6cdca8f8"

chunks = chunk(plaintext, 16) # AES CTR chunk size used is 16
c = chunk(c, 32) # 32 hex chars = 16 bytes

for i in range(len(c)): # Get raw bytes from hex
    c[i] = binascii.unhexlify(c[i])

keys = []
for i in range(57): # Get all possible keys used
    keys.append(xor_string(chunks[i], c[i]))

for k in list(set(keys)): # The flag must be encrypted with one of the keys
    for ct in c[-4:]:
        print(xor_string(k, ct))

# p4{at_the_end_of_the_day_you_can_only_count_on_yourself}