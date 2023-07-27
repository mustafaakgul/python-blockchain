import hashlib
from _datetime import datetime, date

class Block:
    def __init__(self, data, previoushash = ''):
        self.data = data
        self.timestamp = datetime.now()
        self.previoushash = previoushash
        self.hash = self.addHash()

    def addHash(self):
        block_hash = hashlib.sha256()
        data = '_'.join(map(str, self.data))
        block_hash.update(
            data +
            self.timestamp.isoformat() + self.previoushash
        )

        return block_hash.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.genesisBlock()]

    def genesisBlock(self):
        return Block([], '000')

    def lastChain(self):
        return self.chain[-1]

    def addBlock(self, newblock):
        newblock.previousHash = self.lastChain().hash
        newblock.hash = newblock.addHash()
        self.chain.append(newblock)

    def chainvalid(self):
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            previous_block = self.chain[i-1]

            if block.hash != block.addHash():
                return False
            elif block.previoushash != previous_block.hash:
                return False

        return True