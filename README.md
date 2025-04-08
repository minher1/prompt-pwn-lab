# 🤖 prompt-pwn-lab

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![LLM Security Lab](https://img.shields.io/badge/type-LLM%20Security%20Lab-red)]()

> A red/blue team lab for testing prompt injection, jailbreaking, and prompt hardening in LLM-powered apps.

---

## 🤔 What is `prompt-pwn-lab`?

`prompt-pwn-lab` is a lightweight testing ground for **prompt injection**, **LLM jailbreaks**, and **prompt hardening**.  
It helps security researchers, AI developers, and prompt engineers explore vulnerabilities and defenses in generative AI systems.

---

## 🎯 Why This Exists

As LLMs become embedded in everything from chatbots to IDEs, they introduce a new frontier of vulnerabilities — many of which stem from how they're prompted, chained, or hijacked.

This lab gives you:
- 🔴 A **red team sandbox** to run injection scenarios
- 🔵 A **blue team toolkit** to test prompt defenses
- 🧪 A safe place to experiment with adversarial prompts

---

## 🧪 Run a Scenario

```bash
python3 lab_runner.py --scenario role_override
```

---

## 🗂️ Folder Structure

```
attacks/              # Red team prompt injection files
mitigations/          # Blue team prompt filters & guard modules
lab_runner.py         # CLI to simulate attacks and run filters
README.md             # You're looking at it
```

---

## 💣 Included Scenarios

| Scenario Name       | Description                                            |
|---------------------|--------------------------------------------------------|
| `role_override`     | Classic system prompt override                         |
| `hidden_instruction`| Injected payload in user-submitted HTML or content     |
| `persona_swap`      | Rogue persona hijack (e.g. 'You are DarkGPT')          |

---

## 🔐 Prompt Filtering (Mitigation)

Check out:
```python
mitigations/phrase_filter.py
```
> A simple keyword-based phrase blocker. You can extend it with regex, embeddings, or external LLM-based classifiers.

---

## 🔧 Coming Soon

- 🔍 Prompt trace visualization
- 🧠 Vector memory sanitization module
- ✅ LLM-generated response evaluation
- 🧪 LangTest + adversarial scenario chaining

---

## ⚠️ Disclaimer

This project is for **educational and ethical use only**.  
Please do not use these techniques outside environments where you have permission to test.

---

## 🧾 Project Summary

| Feature            | Status                                  |
|--------------------|------------------------------------------|
| 🔴 Prompt Injection | ✅ Included (`attacks/`)                 |
| 🔵 Prompt Filtering | ✅ Included (`mitigations/`)             |
| 🧪 Scenario Runner  | ✅ `lab_runner.py` ready                 |
| 🧠 LLM Defense Ideas| 🕒 Coming Soon                           |
| 📦 Deploy Ready     | 🛠️ Local simulation only (CLI)          |
| 📜 License          | [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) |

---

## 📜 License

MIT
