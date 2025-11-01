# 🪙 ClaimCap — NFT Claim & Trade dApp on Algorand

## 🚀 Project Description

ClaimCap is a **decentralized NFT marketplace** built on the **Algorand blockchain**, allowing users to **buy, hold, and sell NFTs** with a built-in holding period. It’s designed as a simple proof-of-concept for NFT-based asset holding logic using smart contracts written in Python with **AlgoPy** and **PyTeal (puyapy)**.

This dApp demonstrates how to combine **ARC4 smart contracts**, **box storage**, and **global state tracking** to create real-world Web3 applications with enforceable ownership rules.

---

## 💡 What It Does

ClaimCap enables users to:

1. **Buy an NFT** (limited to 100 total).
2. **Hold it for 30 days** — enforced by smart contract logic.
3. **Sell it to another wallet** after the holding period.
4. **Check ownership and claim statistics** in real-time.
5. **Interact via ARC4-compliant methods**, making it compatible with Algorand dApp tools like `algokit` and `algorand-sdk`.

---

## ✨ Features

✅ **Buy NFTs securely** — using ALGO micro-payments
⏳ **Enforced 30-day hold period** before resale
🔒 **Smart ownership tracking** stored on-chain via box storage
📊 **Global claim counter** to monitor total NFT sales
💬 **User-friendly messages** for validation feedback
🧠 **Built with AlgoPy ARC4** for clarity, safety, and composability

---

## 🧱 Smart Contract Code

Below is the core logic for the ClaimCap Algorand smart contract.

```python
//paste your code
```

---

## 🌐 Deployed Smart Contract Link

👉 [View Contract on Algorand Explorer](XXX)

---

## 🧭 How to Build & Deploy

**Prerequisites:**

* [Algokit CLI](https://github.com/algorandfoundation/algokit)
* Python 3.10+
* Poetry installed (`pip install poetry`)

**Steps:**

```bash
# 1️⃣ Install dependencies
poetry install

# 2️⃣ Compile the smart contract
algokit project run build

# 3️⃣ Deploy to localnet or testnet
algokit deploy
```

---

## 🧪 Interaction (ARC4 Methods)

| Method              | Type  | Description                          |
| ------------------- | ----- | ------------------------------------ |
| `buy_nft()`         | write | Purchase NFT (requires ALGO payment) |
| `sell_nft(buyer)`   | write | Transfer NFT after hold period       |
| `check_hold_days()` | view  | Returns how long user has held NFT   |
| `get_claim_count()` | view  | Returns total NFTs sold              |
| `hello(name)`       | view  | Returns welcome message              |

---

## 🧰 Tech Stack

* **Language:** Python (AlgoPy ARC4)
* **Framework:** Algokit / Poetry
* **Blockchain:** Algorand
* **Compiler:** Pu
