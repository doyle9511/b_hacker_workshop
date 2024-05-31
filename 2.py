import requests

address = "1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa"
message = "1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa"
signature = "HCsBcgB+Wcm8kOGMH8IpNeg0H4gjCrlqwDf/GlSXphZGBYxm0QkKEPhh9DTJRp2IDNUhVr0FhP9qCqo2W0recNM="
// address, message, signature 변수를 생성합니다.

url = "https://bitcoin-mainnet.g.allthatnode.com/archive/json_rpc"
data = {
    "jsonrpc": "1.0",
    "id": "0",
    "method": "verifymessage",
    "params": [address, signature, message]
}

response = requests.post(url, json=data)
response_data = response.json()

result = response_data.get("result")
error = response_data.get("error")

if error:
    print(f"Error: {error}")
else:
    print("Verification Result:", result)