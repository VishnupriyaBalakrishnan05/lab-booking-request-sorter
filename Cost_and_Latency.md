# Cost and Latency Note

For 20 requests, the normal design makes one API call per request: **20 calls**. The retry policy permits one additional call for each request whose first response fails validation or encounters a retryable API/network error. Therefore the theoretical maximum is **40 calls** for 20 requests. A request with a missing API key makes zero calls and safely falls back to `needs_more_info`.

Planning estimate: allow roughly 1–5 seconds for a successful call under ordinary conditions, plus a short retry wait when needed. This is an estimate, not a measured benchmark; actual latency depends on provider load, network conditions, model and rate limits. A full 20-request run may take approximately 20–100 seconds before retry delays.

Cost depends on the model's current input/output token rates and actual token usage. If the selected Groq model is available under the account's free allowance and usage stays within that allowance, the direct API charge may be zero; otherwise calculate it as `(input tokens × input rate) + (output tokens × output rate)` for each call. Check the provider's current pricing and usage dashboard before reporting a monetary amount. No price is hard-coded because provider pricing and free-tier limits can change.
