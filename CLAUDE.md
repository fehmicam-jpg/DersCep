# DersCep — Claude için notlar

## NVIDIA API kullanımı (kullanıcı talimatı)

Bu ortamda bir `NVIDIA_API_KEY` mevcut (build.nvidia.com / NIM API,
`https://integrate.api.nvidia.com/v1` — OpenAI uyumlu `chat/completions`).

**Bu key, DersCep'e veya kullanıcının başka uygulamalarına bir AI
özelliği olarak entegre edilmeyecek.** Kullanıcı bunu açıkça reddetti.

Kullanım amacı tamamen farklı: Claude (bu asistan) kendi başına
yapamadığı bir görevi, NVIDIA'nın barındırdığı bir model yapabiliyorsa
(örn. farklı bir modelin çıktısına ihtiyaç, belirli bir görsel/video
model yeteneği vb.), o modeli arka planda çağırıp sonucu kullanıcıya
sunabilir — bir araç gibi. Sonuç asla kullanıcının projelerine kod
olarak gömülmez.

Yani: **NVIDIA modelleri = Claude'un kullanabileceği bir araç.**
**NVIDIA modelleri ≠ DersCep'e eklenecek bir ürün özelliği.**

Kullanıcı açıkça "şunu uygulamama ekle" demediği sürece, hiçbir NVIDIA
model entegrasyonu koda/repoya eklenmemeli.
