from algopy import ARC4Contract, abimethod, String, GlobalState, Txn, UInt64

class ClaimCap(ARC4Contract):
    # Track who has claimed and total claim count
    claimed = GlobalState(String, String)   # wallet_address -> "claimed"
    claim_count = GlobalState(UInt64)       # total claimed
    MAX_CLAIMS = 100                        # only 100 NFTs available

    @abimethod()
    def claim_nft(self) -> String:
        sender = Txn.sender

        if self.claimed.get(sender) == "claimed":
            return "❌ You already claimed your NFT!"

        count = self.claim_count.get() or 0
        if count >= self.MAX_CLAIMS:
            return "❌ All NFTs have been claimed!"

        self.claimed[sender] = "claimed"
        self.claim_count.set(count + 1)

        return "✅ NFT successfully claimed! (" + str(count + 1) + "/100)"

    @abimethod()
    def get_claim_count(self) -> UInt64:
        return self.claim_count.get() or 0

    @abimethod()
    def hello(self, name: String) -> String:
        return "Hello " + name + "! Welcome to ClaimCap 🎉"
