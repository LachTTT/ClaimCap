from algopy import ARC4Contract, abimethod, String, GlobalState, Txn, UInt64, Global, Box
import time

class ClaimCap(ARC4Contract):
    # NFT tracking: wallet -> timestamp of purchase
    owners = GlobalState(String, UInt64)
    claim_count = GlobalState(UInt64)
    MAX_CLAIMS = 100
    PRICE = 100000  # 0.1 ALGO in microAlgos (100000 microAlgos)

    HOLD_PERIOD = 30 * 24 * 60 * 60  # 30 days (in seconds)

    @abimethod()
    def buy_nft(self) -> String:
        sender = Txn.sender
        amount = Txn.amount

        # Require payment
        if amount < self.PRICE:
            return "❌ Need to pay 0.1 ALGO to buy NFT!"

        # Check if already owns
        if self.owners.get(sender):
            return "❌ You already own an NFT!"

        # Check limit
        count = self.claim_count.get() or 0
        if count >= self.MAX_CLAIMS:
            return "❌ All NFTs sold!"

        # Record buyer & time
        self.owners[sender] = Global.latest_timestamp
        self.claim_count.set(count + 1)
        return f"✅ NFT purchased! You must hold it for 30 days. ({count + 1}/100)"

    @abimethod()
    def sell_nft(self, buyer: String) -> String:
        sender = Txn.sender
        purchase_time = self.owners.get(sender)

        if purchase_time == None:
            return "❌ You don't own an NFT."

        # Check if 30 days passed
        now = Global.latest_timestamp
        if now - purchase_time < self.HOLD_PERIOD:
            return "❌ Hold period (30 days) not finished yet!"

        # Transfer ownership
        self.owners[buyer] = now
        self.owners.delete(sender)
        return f"✅ NFT sold to {buyer}!"

    @abimethod()
    def check_hold_days(self) -> UInt64:
        sender = Txn.sender
        purchase_time = self.owners.get(sender)
        if purchase_time == None:
            return 0
        now = Global.latest_timestamp
        elapsed = now - purchase_time
        return elapsed

    @abimethod()
    def get_claim_count(self) -> UInt64:
        return self.claim_count.get() or 0

    @abimethod()
    def hello(self, name: String) -> String:
        return "Hello " + name + "! Welcome to ClaimCap Market 🎉"
