<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn1.telesco.pe/file/DVl6JgTUMrFCax2-z4Eij6PNo8sjbYz51XNXn63PcGQNzESOKt_Pq4ejZjZ9FMo3qIDcJ1m_FI4QwpG0h8h7nRmKjiecHfAkP-c-wWeRqYl7sCHQ0yeQrKuDfV9tEvzCz-bKoUVPmmcytcM8p8G3WPkBKTmqzAkgNtxeS94Ai5rn3rnr1NfGAtdwSU36Y3_7a9JCwRO8tlmSDSaq90cn9E8jpNCvSyYIJMyB1wDpeG9ovNnzX8M1D7MlZIoSU29fR9AbIw69GPOnFsiLb7OB1cy21cJ5U60dMR7kz5eN4Ut8dndwVEqYVuWfEvK1iKMcTcl1k2YFzIz59r_gY5XfFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 160K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 13:13:25</div>
<hr>

<div class="tg-post" id="msg-3620">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RdMe_X7IDJ6gm74v2Tehhduvm5nnfE50AmFCKXqR-9XRnev5Xz6GfFpeOCLh2VYBp8Jjt3t0CliNj8SdbJKxp01LMXbYoWO_-pdJx6pdDrXfcmRNKqp6O3DdRV1J6BzXs4OptZ-C20eovxldWqS1iu1ojJ4dqj1T25d4Nm-gVE3ESHkk09wpECSEf_rc33wpkN9qZqpEv3b0fGL3a7fHj4cJYcBsPGNPdUjD2P_Wn-FDn_2IH3cczz4L5dypfzbxpWgWfqa1PSSLbLVYx5VfQlZGWJEFXKtHGSckcFXhCTPBGhzMKgMrhLGK2M2I-llbnD_PY7cmMH2bH-vPrvYl-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/MatinSenPaii/3620" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3619">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">من الان با این به Spoof وصلم:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "104.17.89.5",
"CONNECT_PORT": 443,
"FAKE_SNI": "www.speedtest.net"
}
به جای connect ip، میتونید هر آیپی وایت کلودفلری که از اسکنر(
https://t.me/MatinSenPaii/3598
) به دست میارید رو قرار بدید</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/MatinSenPaii/3619" target="_blank">📅 12:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3618">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید: hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/3618" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3617">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YL4AL4c5gsueWT3O4TlFhUC2_8EFh_F-5Tw_WAlaGFdTLOc54XHoTHLNbAXLvRfIrMIUVB8kjlX0ZeOQA2SLQvDNZLpRlfJj71ndP2RVaLf4yH4bYpbHfbptFG3rn8mok5acL6sxHjcIG_M7ungr8P93BBYOrETQSAUsAokmBKTTxeF_zLXcXufr-R6XdwL7y_P1QX0qtQT8kLUbjRlzuyfWTdpLvCI5fBP5Nu-DVVbtcTC-tnfa8oeFNdfuj6n0z0nBkstnQn8JZQkH5xJNa-sIleMnWEuUzj7HaamVpel2u0eERkkErfIYmmGctCACHey9efihk-Y87UtCaS20bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید:
hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:444?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:8880?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:1040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:4040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:54040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
این هم لینک سابش:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
این هم کانالشون:
https://t.me/Masir_Sefid
من با همین کانفیگ‌ها توی کالاف پینگ ۶۰ و گنشین پینگ ۱۰۰ دارم و راحت می‌تونم بازی کنم.
کانفیگ هیستریا هم آموزش ساختش روی یوتوب هست، باز اگر لازم بود یه آموزش ضبط می‌‌کنم واستون. اما نیاز به سرور داره</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/3617" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3616">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN1sfTh_Sk7z89uSTHKAqs8oiDZ_QTKc7PTxvrLeS_QNn9XyEE3Cov1X2WFJUqC8JUy5V295kY3Q_lPAFZNOFUtShuRmigvpJtKpPBylOdc1zwuzdj106aAqZ1_yU2CEtxJyGfVHuCFwHJf24zwCxkCe62Nt2BZewabj5rXvldo43atuiPrffy7sSpW8FbemH_RiGr0as7iDspW_2yQZeaRt9gqQcmlxP-Gq7tCMjeYKsNUUj06D5tG091dERJBIW7Jgf3Os3ESXZvJQiuxvWDLcwBu1sfGx408zhTH-it-snijJQspkDiWjbq6cXpSUCh7bgCIbf7GqBcOb4kV_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش تبدیل کانفیگ به آی‌پی سفید
از این به بعد برای تبدیل کانفیگ، آی‌پی‌های خودتان استفاده می‌شود.
@WhiteDNS_Installer_bot
مراحل کار:
1. وارد ربات شوید.
2. روی گزینه «تبدیل کانفیگ با آی‌پی سفید» بزنید.
3. کانفیگ V2Ray خود را ارسال کنید.
فرمت‌های پشتیبانی‌شده:
VLESS
VMess
Trojan
بعد از تایید کانفیگ، ربات از شما لیست آی‌پی‌ها را می‌خواهد.
می‌توانید آی‌پی‌ها را به این شکل بفرستید:
8.8.8.8
104.18.1.1:8443
یا با کاما:
1.1.1.1, 8.8.8.8, 104.18.1.1:8443
نکته مهم:
اگر پورت وارد نکنید، پورت پیش‌فرض 443 استفاده می‌شود.
اگر آی‌پی را همراه پورت بفرستید، همان پورت استفاده می‌شود.
مثال:
1.1.1.1
→  پورت 443
1.1.1.1:2053
→  پورت 2053
در پایان، ربات فایل کانفیگ جدید را برای شما ارسال می‌کند که host و port آن با آی‌پی‌های ارسالی خودتان جایگزین شده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/3616" target="_blank">📅 03:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3615">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X-eADWhXXl6gFYIaHdDKTqxGhju_SZ8DzWsfXyry3C2beAC00PLBBUD96ZSRZ4c-5FwkegFocDrtxaEeXwlZLGRRosoh9c7r6p42J7m3X4VsktduvjbCQcp048UqpauCWz36StJ2V1aRQzzYrjMqpmKFZL_MgZWHLw2U7Mgx23hPFW6oiGYLrlcKcdrlit-m886Oz81dmdNqii_ZOnC7qp2CXRV61uqLmd37CFqzfBXcVtGh_9dnrz7B2NaJ0dTGDb5uF9u3Lv73jdl3v8qlBgIHfFNd8mkzMUEz_N4iRdnzI5T5YDRSays7qUMjT4pxsgxrgCulbhSZ1kHoTUIkrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کانفیگ کاستوم دارید(ساب نرمال)، آیپی تمیز رو باید اینجا جای address قرار بدید</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/3615" target="_blank">📅 02:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3614">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑇𝑎ℎ𝑎</strong></div>
<div class="tg-text">https://t.me/MatinSenPaii/3613
خوبیش اینه با این روش میشه رفت و کانفیگ BPB ساخت
برا دوستانی که کلودفلر براشون بالا نمیاد یا نمیتونن وارد سایت اتومیک میل بشن
همه چیز با همین نت بدون نیاز به فیلترشکن کامل انجام میشه
بینظیرید شما
نخبه های ایران.</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/3614" target="_blank">📅 02:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3613">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting.json</div>
  <div class="tg-doc-extra">9.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3613" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/3613" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3612">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qJq8Ydrlw311Y_BigU1mDg2xV-_NvsJZ93-8ZSv7n1c01nzneXXBFXI0B1J-LRGwBReXMAbyXHVynBs3gFQrB8mLyjyhzdCMIyvAWIReOx0bRG6bzgW1XWtKwSuTMZudDP_rhX49JUw3j9VDVLc_ZwkC75EsbnyUTjWr5h8Va7yMTaBbspIJAogtBnsOl7VBCTHBWf2GAeVZkc2b-0ahl_k5AKodAG2tJLV9WEmPeb8TScx144j7z-l_R6pGsEfXfrB4aivGm3Cr_wp--i94DLhwS0yq5QHUwlspfaZ2vPbhfWC8w7-PP5u3_Wa52oFEosK6jQQ-fbUxoY_S19SdpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیستریا هم روی اینترنت من باز شد</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3612" target="_blank">📅 01:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3611">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mr Lou _ Ey Iran | مستر لو _ ای ایران (Rock Mr Lou Version)</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/MatinSenPaii/3611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3611" target="_blank">📅 00:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3610">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوستان اگر از Undefined در نمیاد،
1- صفحه رو رفرش کنید
2- حداقل نیم ساعت صبر کنید
3- اگر نشد، پروژه‌ی Worker جدید بسازید و دوباره مراحل رو انجام بدید</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/3610" target="_blank">📅 00:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3609">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3609" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3608">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/3608" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3607">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/3607" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3606">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e3IyAaA5kHR2u44Xo3sudtGVhDV7JjX6a3GyTStiyXPxYHuWEY1GLrqYIDGh1uNQCVzNbbGd0r6AfTUOAFap62vIO9AANAW2AOXyk_MNGEDMbXQ5YCbpWwbp2zB6Db14I2Gs-xcF9j4T4TshFV2phYjDUjYVAfqzqikZgPCa9aUQwNsyHcLPHQxPtOsa5Gk2i5rDjrXOhxOjMPHFAee2HaxMN2c51Pk7Atq4mq15z4i7Axzy5_1y8X-kuClyVNZvO9v4i3vtJBpFFWT09UOvwLZJLsm9-LhUiImUjoKDn6UvQyUW7dfphlNbuJfIvop_4EbH8IYY9pLaTCapFrOpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای SNI Spoofing
SNI =
www.speedtest.net
IP =
104.17.148.22
✍️
Kharabam</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3606" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3605">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3605" target="_blank">📅 22:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3598">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3598" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ورژن 0.5.0 اسکنر
راهنمای نسخه ها</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3598" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3597">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر:
https://t.me/MatinSenPaii/3598
پنل BPB روی گیتهاب:
https://github.com/bia-pain-bache/BPB-Worker-Panel
پروژه اسکنر روی گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت پنل BPB ورژن جدید
2- رفع مشکل پینگ -1 کانفیگ‌های آپدیت جدید و درست کردن تنظیمات کلودفلر برای کار کردن پنل
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Worker
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- توضیح حجم مصرفی و استفاده از این روش روی کلاینت‌های متفاوت
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3597" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3596">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.  https://github.com/MatinSenPai/SenPaiScanner/…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3596" target="_blank">📅 19:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3595">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.5.0</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3595" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3594">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN6oF-xDiVJA7REBMznUELxpHxlscLxOnQDsQBaViiK_t7_qLGJW0VlT9i7TqAQCd1j2F74diss8hB05UTjkRMA5ysDelZnQFR-EruCXf7l9WPU0dRbnQVXYkwbXt8xToZStSed2j_0G0swuQlri5F4dWBHgCfUL5GrqCIaklR-BP6K9BjTAiXHFGF6MrbHGJWdZ9hN2RgveC6ZhVCgdyKSpYtkKWDUuGIikwv7YsTabQ1k1e6DtY-0v6_ziu81npU7T1xkDMEUNrlJa02OPtTbZNYW_NTkxpo_N_MaPiYsiY8Wiabg4D7kCZOH4-LvrzNX4pEQaWimMF99_G3apVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
آموزش V2Ray از صفر تا صد | نصب پنل، ساخت Inbound و Cloudflare Clean IP روی سرور شخصی
در این ویدیو نحوه نصب و راه‌اندازی پنل V2Ray روی سرور را به صورت کامل آموزش می‌دهیم. همچنین با نحوه ایجاد Inbound، مدیریت کاربران، استفاده از IPهای تمیز Cloudflare و اتصال کانفیگ‌ها از طریق اپلیکیشن WhiteDNS آشنا خواهید شد.
سرفصل‌های آموزش:
✅
نصب و راه‌اندازی پنل V2Ray
✅
ایجاد و مدیریت Inboundها
✅
ساخت و مدیریت کاربران
✅
آشنایی با تنظیمات مهم پنل
✅
استفاده از IPهای تمیز Cloudflare
✅
آموزش پیدا کردن و تست Cloudflare Clean IP
✅
آموزش استفاده از اپلیکیشن WhiteDNS برای قرار دادن کانفیگ‌های V2Ray پشت IPهای Cloudflare
✅
افزایش پایداری و کیفیت اتصال با WhiteDNS
✅
تست و بررسی عملکرد کانکشن‌ها
✅
نکات امنیتی و بهینه‌سازی تنظیمات
😊
لینک تماشا در یوتیوب
https://www.youtube.com/watch?v=vVjqNQBUGIc&feature=youtu.be
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/3594" target="_blank">📅 17:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3592">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اینترنت دیتاسنترها هم برگشت بالاخره؟</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3592" target="_blank">📅 17:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3591">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏دوستان می‌دونستید که این روشن/خاموش شدن Wifi ویندوزتون باگ نیست؟! به‌خاطر فیلترینگ شدید فایروال‌های ایرانه
🤦🏻‍♀️
دلیل و راه‌حلش:
تست اتصال مایکروسافت (NCSI) که فیچر ویندوز ۱۰ به بعده بلاک می‌شه؛ به زبان ساده، به‌خاطر فیلترینگ، ویندوز فکر می‌کنه اینترنت قطع شده و برای همین هی وای‌فای رو خاموش/روشن می‌کنه تا اتصال برقرار شه.
راه غیرفعال کردنش:
۱. همزمان کلید Windows + R رو فشار بده (کلید ویندوز همون لوگو ویندوز روی کیبورد)
۲. توی کادر Run که باز شد، بنویس regedit و اینتر رو بزن.
۳. برو این مسیر:
HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\NlaSvc\\Parameters\\Internet
۴. روی EnableActiveProbing دابل‌کلیک و بعدش Value رو ۰ کن.
۵. سیستم رو ری‌استارت کن و تمام.
دیگه این فیچر غیرفعال می‌شه و VPNتون قطع نمی‌شه :(
البته تا وقتی که غیرفعاله حتی اگه اینترنت قطع باشه، همیشه «Connected» نشون می‌ده.
✍️
گیک‌زهرا</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3591" target="_blank">📅 16:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3590">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gyk017JawKUQ0jKkIkPc9JVtnOZ1K_dLx753UIn6uKo9Mo0kIE5tiB8Gwc-i7fezmm7H_iIy2cGd-G0CKCDWP5I3AorC4CxoTT_gl2qViOIN8WqYLu-KMSzbM71hujfThVVY7ZQ72bMhCrtjmu8MdR5DxsSZ3UaVME6xUDa-h9cHdIgjiHrRsh7GKvkVx3_fUzls4as6X6xbI6SyPSIvhbOIOEv1j0FQzkAE4ytN3Kjq02HxerR4oTUX6fx4MWXwlxCxpd07G6llnEUysgpzW-G-iwU7qydEick6uNzyosN4Aa9F1hOiHqQ2JgGLlPg4psH6o-mvLykO0ja2uQW6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه به این علت باید حتما اسکنر رو توی لیست سفید آنتی ویروس قرار بدید. ویندوز دقیقا این بلا رو سر BPB Wizard هم آورده بود یادمه</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3590" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3589">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">متشکرم از دوتا دوست عزیزی که 105 و 3 دلار دونیت کردن. من تازه ولت رو چک کردم
❤️
مقدارش مهم نیست. کم یا زیادش یه اندازه ارزشمنده و کمک بسیار بزرگیه به من. ازتون ممنونم</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3589" target="_blank">📅 09:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3588">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3588" target="_blank">📅 09:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3587">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3587" target="_blank">📅 07:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3586">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gPm6VUDtoT525TJS7RejuPKcIGzYnsoPF_UWOeQIrFA9smdWGqwVThLokSMumkAygA1L60E-yx3Z5y3RlNzEg3zQlhd-EMFj6pAKaoPs-HUe3qK7Vn1B6_i7gIqhoDmmXtF9wgKePweEawuMJfByDnot_hHdpxt6hJw_FR5SiICalfKwcQmoK1FYgnftXUTop8fDOR9Q6cxEiCE1esdGW30ArOKGJgelWR6UBumEM_kOfxOGtLIH0yYDyc_AXfY9WJ3n1V8oanH02kGXZ9TZsIf4WKvso4xD17p4WkOkX5jo4HryiGu2GdJTgcvG_jLfxRxmLeWV3hUDrPIDfY_1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/3586" target="_blank">📅 07:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3585">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gal6ERpLs2PkpgRE3eZb2Mme-qIjVuf2eFuht7Gf94nqmG6G23WHMTUI5dYGbz90HkdD-6ers0poR912Pz1pHw7npP6RzmCR4BknGAX4pJv7I2MpxHuINdF7afLvww5h8ShxF-vlEdhIh-bsTbR14NxWPKUl4fbMc5cGqjnLKjlb3ss69lads6BPCF2xfBZyyFD1viV7g2FEKuuAExxOUDgEh3IdjTDFULfWHn-O2Q4Xofhn_4Q85C-NtkIHqMF52f7Uq98LxkrhkoY65saXoQfWA1Zx_UhJS_129mE9c27f98U0oqNOVdgwWhudLNOhTaZrFyua1QIAXUBrDBx4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار که عملکرد اوکی شد بالاخره. چندتا دیگه از دوستان هم گفتن
نسخه‌ی اندروید و دارای ui درست و حسابی به احتمال زیاد منتشر نمیکنم چون خیلی درگیری و کار و درس دارم، اما سعی میکنم روش کار کنم با contributerها. فعلا تمرکز روی درست بودن عملکرد بود که حل شد
برای همین prهای فعلی هم reject میشن همه. تا ببینم تست چطور بوده تا به اینجا</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3585" target="_blank">📅 07:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3578">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3578" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V0.4.0</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3578" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3577">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DtA1Tl3ABM8FjIClAyvWJwBIxLX0toXWv7nfgokWtmAuu_QEtzgl-cAHA8whk4UsVsk5wKiUEm8m-uJLoyS4LeH_RcMN5u_uJLSPVtktgWl2gRHE_ybeiTwRNERvYieOwcNFnEplcmsaa-UWHKlIYdhr42b1zGVG4X7vq6OIf-5PW6wMDSbHIR7GGg5lkbc6x8VCcrMoUUePKChZZjlOJRycq0fY5PL--2BNZX3XNAKfOcycLT_rb3qXndjvNuXBcse3gqPoRqrUxXplm_zA00sILD7aPeIERB27aHO2XV4IjzMQw4cl5FTeQU1h-Xbuvm9Gr2ZG4i6Cc9UFkCRVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب، فکر کنم یک بار برای همیشه مشکل آیپی تمیز فیک حل شد.
و ممنون میشم تست کنید و بازخوردتون رو بگید. تا اگر مشکلی داره برطرف بشه و بره برای ریلیز</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3577" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3576">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVf_hoVj5i4znEUf7MAB3eBdNJ_pjZpdECx1L_DIlGDkl3mTFdgxVeRPbi5mwVN3030l9T8LS40MY927B0Udd3e5C4W2QByqJgQ1OyJwlHVV79TArhu5vclfK5qjTIThPdOFf1HEPkvjcb1UKdGxgcpISGrIHO3ZW96suHACpkx0aBxIw2mCC1wMLHIrmmi4kCjRHxg478rfaTONXumV3MOm-30DHr9BWQjPyO2zrVMBEESY_iXSfg51_eRFC87pMut0xTzszqZrKXJ_CkRlCSv2JmHEFo5Dhw3IQdSST4p12rWhjlKr0UxgIIE5uD5VdVIz6y-K7RvT6GCIeqwXlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها گویا روی یه متد جدید کار میکنه که به راحتی می‌تونه فیلترینگ الان رو با یه استراتژی جدید دور بزنه.
منتظریم ببینیم تصمیمش این میشه که الآن منتشر کنه، یا بعدا</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3576" target="_blank">📅 04:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3575">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/3575" target="_blank">📅 03:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3574">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hVNkoHMsqfEBnm3VinIbYAhkaJJut1Z8MC7yoTsANpa-rULUlQnwclwxIKXWn1f433FvyETnMqQd96U196xnGjnW6zSZl1zWY6Q9TJESV0pyJp0fANOEggsAfKh7sW5DLEGUVmtODIaNc8Cc5JdiyRGpOZIrv8jJqvgWLmTJggJ6WeIpw8kYWFdCdUDFb0Twk4l3vDmFG9fqiGp0UdP9A5LKI8bPQ5QVqlVwNAUsh0mgMXOggg2XncV6zL0Lpjkz8PYLoZDm2DTXei_N3GrUPz4wkTqH8nlUPEP6sn74fWStwFwS5uLBBj3RpVpeMjRrto-tlRdmQnbs6Kltd0xFsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک 20 دلاری Cursor اصلا نمی‌ارزید. خیلی خیلی خیلی زود تموم شد با اینکه از مدل‌هایی مثل Opus هم استفاده نکردم
اکثرا gpt 5.3 بود یه کم هم Sonnet
افتضاح زود تموم شدش</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3574" target="_blank">📅 03:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3573">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مشغول حل کردن مشکل رو اعصاب آیپی healthy فیک هستم. خدا رو شکر یه سیمکارت پیدا کردم که روش دقیقا همین مشکل رو داره</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3573" target="_blank">📅 03:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3572">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D2kPll_2IXOOnFl-wIGXlkdH5yBUyacIxt5e3VU0mhfvZg8RU9GM3x4xh_B1CWoOUSQunKDH82FIOp9jmZpmCQVI8tWvZTJgZNH1MnVw82oXPVnMunA7l9cxqo84OfJHGHhO2jx-gISoP1GL-q7Hk_XQPKwmqYaqa1CdiNxDHRbqQr1p1PS-xHPPphH0HJgO5n9Iu9xvOlzqHMc1F3Dk9ulbSYKGg-9dT75I3iF2TLuIabaFRXKIMcFn4FXrCYBilyyc1J7pnVmPL6VGFFYw7Q0P_FtILrIphrp03305HcxEjQ4dbvEJwSD-Ud4hWu165EUeLgUDSkUhCaxE0_cpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی یه اینترنت عادی هم این شکلیه نسبت. یعنی تعداد آیپی‌های سالم کمه و همین هم شانسیه چون range ها به صورت رندوم انتخاب میشن. حداقل 200 هزارتا اسکن کنید</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/MatinSenPaii/3572" target="_blank">📅 20:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3571">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">V4-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3571" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3570">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسکنر همچنان مشکل داره متاسفانه روی اینترنت‌های دارای اختلال. دارم روش کار می‌کنم</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3570" target="_blank">📅 20:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3569" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3569" target="_blank">📅 20:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3568">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ورژن 3 منتشر شد https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3568" target="_blank">📅 19:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3567">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اگر اکانت جدید می‌خواید بسازید، از BPB استفاده نکنید فعلا. با این آموزش، edge tunnel بسازید:
https://www.youtube.com/watch?v=svYBcv4bSzo&t=618s</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/MatinSenPaii/3567" target="_blank">📅 19:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3566">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ورژن 3 منتشر شد
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/3566" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3565">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qI1a82kfn9J_JRYOTpDkKyfEHWr5EYEQ7Vq7OdoEDgADkGDl2ixAAlL6jKzTG5lUtZ46KRzaeCHM9GhQVo4sEmi7ftZemmjRovVbNnzftVK4OhlOkn-yN0EQey6bhV-OSxD2OFhZ2ouT4mPyi4_6UYz8W3K3-5Hdevy5zyXESyf0GVxbd8_AALNomuBNaLDVcnp2kzO7hngvpmg88f5Middv8eY-os3ea1XDn3u1MAOXKv6ovxpeqiprgxy-zxwyy8zkIMaQrouhh-r1Gtbw34I1y3GkOXA3uqwl2TunnCa3el_pDFw6Z_e9av5W1-DorixOlHNNrNq_tyVvmYlS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3565" target="_blank">📅 19:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3564" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3563">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lIN_FDxgqub9GBuRhuXb_OUqQ5riyU6z9V0lp4AMA5uWuM0gWbECWjbWg5fbBlHnV1MWIenXG8x5aFlmdLHZWZWkZYWcp6QwCbUqABwzgyv0ErK8TE7guxcco901lfXX4QjCOo4Sf0ugvLgujhzvxzKhwwxo8UppKFX484gT_KDvgCHxqLVDoDXCm_VJrXewKaLesl4YpGQwszvK-w0r93lwNy6ibGkx6_Y-nW2k1qvMERisrlTtTocArhvC5SPpJGLh-akCcgL4M7Wzkt0M5eT_MNtlGyYSwyZaT3F-1rAHCH-nopM4IehOWW10FuIXJx8ai731LORPyAPLnpevow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">BPB - Edge - VahidFarid
فقط Edge داره کار میکنه. هر سه هم روی یک اکانت</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3563" target="_blank">📅 17:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3562">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خب انگار مشکل از BPB بودش. چون الان edge tunnel بالا آوردم کار کرد اما bpb دوتا بالا آوردم روش کار نکرد</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3562" target="_blank">📅 16:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3561">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">امروز به دوتا نتیجه‌ی مهم رسیدم:
1- روی یه سری از اپراتورها، اسکنر نتایج فیک میده
2- پنل BPB ممکنه از اول تا آخرش ستاپش درست باشه، اما در نهایت کانفیگا کار نکنن. که دارم سر در میارم علتش چیه. فرای از اپراتور این شکلیه. یعنی با یه vpn دیگه هم ازشون پینگ میگیرم پینگ ندارن با اینکه tcping میدن</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3561" target="_blank">📅 16:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3560">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">همچنان از
@Whitedns_Installer_bot
می‌تونید کانفیگ رایگان دریافت کنید. تا الان 21 هزار نفر دریافت کردن دیروز و حدود 5000 نفر، حجمشون رو تموم کردن(که امروز دوباره شارژ میشه). به زودی مقدار حجم روزانه هم افزایش پیدا می‌کنه</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/MatinSenPaii/3560" target="_blank">📅 13:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3559">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یه آموزش کوچولو داریم امروز</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/MatinSenPaii/3559" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3555">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kKUrJN_fThwa1VaRQzNKE4S0civHHV73W42ln_l6aElsUv98zoMm9TPqvoMjwC6yyRowrA3jKool9knpE5lGnlf6_guAMmDERdGq3wr8TLoA8QO_5sx7RltU0A8gVa0jHmJ9pMjJcTNcbzX2LQa3Fmmhmp4Rs7DwlLBoJ37qhE1HmNIxqhTakkKdh6dETWH0hUzFLzlSrG6vQezPqx-lbGoAngijidbsyzxWi02QkEUrJrhGoBuCNRoMvKcj3juXLhuFhZgbKsNHCIX-IUAqQgPnjSTdJq2bCmehq7bbweftPWDcstPmN_eiCWqQpGhNVwPA_RZmmeNcUMFaxvQuzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/izkV2rBdyFTaWotmseWkGlSFlPVRxSLqCYtd3AvSFJ8ZtcjO8s654G1rnlLw7H_UHM5FcRxkaBC6eahal9wVwuJEy-V_9CzeF259SfpnuXFVr_5ntUrYW-_kvvKHhofglejD4qEXbH7juzS-uc0uiX8g7TUqsDkPugW_mOqqJ2QNH1kSCzkv5oMK1eN4V4K6n5naNm2Hc2nioo9pwZLHE9iBbBu_GjjtelklTl9GRuKuXiV4nNTf48leMEHPEGHYUO_p65BM3ZJEqwslBwCzWO2qzwiFhx-GiyiaEvxd86iGhpBKOAdIDlszb0wlZSlhMBHlaOGkAIv0iy6dRNAjNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZP3tq-2TyEX0m-qF0SCAbpF6Pz6uDnnQNxn6e6n1-wN_UPQyXh2RxRah65pW7fkXKj799DewaA3npFGFv-4WJxdH0uN2uOkYmorhhVCN3LgKxDvnSAvJPzoM8wLalUPE_L2dy-lwRc0ppylecdWCvw2UzsB8PYbizXejqve6f52XTjo46oyz5C_0HxnkNps-kTTvAHlmWB2C_ObIz9cRKvEGPcO2PFaGZOv-ruIHIfEhjUDJUr1OLqOoSrhkt9fi9h5ajjmToGTrGpXZBKJqekccpsL5dRUWq4eBSvdntnh1cuQqV74-I2tEAjDSmcEFRievDsXoVp979N2TergbUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PfgyzsU_j0Pp6QTW1m_bBHZxyNuow1RT2La0nx-fj8HLQ8ZIktWgr6y0EoRJgvTAD7geAEUor_vjnx3hutXEOiVTqibdUqvxjvSe8wbINdBSOCg06ErW0Gswhauro7ljNm93RZetE9qO7WtR9IXLNM2DWLGNOgzfbnBPE0BDt906rLE-CcJztz9wkSXMgKCVDaFoHBmAt2J5xQ3Eo_ONxM8sSrx24Oxf7esFhwmdl9YA5STzqO1eQHJgbZ-Ex7ycIIeeqcUiNMc48YnnIe7jxmzaxkY6BPn9qZa7O6H8Bo7yxOaDi6E6zsyxCvbzg_7T2FVvah3m1s33slMxbCO7Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاری که خودم کردم:
1- صد هزارتا زدم بره برای اسکن با ورژن جدید سنپای‌اسکنر. با 200 تا worker کلا 10 دقیقه طول کشید
2- برای من 4 تا آیپی پیدا کرد
3- آیپی‌ها رو با این پروژه‌:
https://t.me/MatinSenPaii/3554
بازنویسی کردم روی کانفیگ پنل BPB(هرچند خودش داره اما این شکلی راحتتره)
(صفر تا صد ساخت BPB رایگان)
4- کپی پیست به v2rayN و ادامه ماجرا
سرعت آپلودا هم اوکی شده الان راحت اندازه دانلودم میگیرم</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/MatinSenPaii/3555" target="_blank">📅 09:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3554">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اشکالاتی که فرموده بودید رفع شد. پروژه با هوش مصنوعی نوشته شده و تمرکز بر سادگی و استفاده‌ی راحت مردمه. اگر اشکالی دارید توی استفاده باهاش بفرمایید و issue ثبت کنید یا اگر خواستید، pr بزنید و مشارکت کنید.
باز هم عرض میکنم خدمتتون که این اولین تجربه‌ی من از اوپن سورس هست و اگر اشکالی به وجود اومد در آینده، پیشاپیش عذرخواهی می‌کنم. سعی می‌کنم که یاد بگیرم و نیاز فعلی رو خوب پوشش بدم و همینطور پروژه رو هم در بهترین حالت ممکن maintain کنم</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3554" target="_blank">📅 04:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3547">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3547" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای ورژن‌ها
تغییرات و بهبود‌ها:
- رفع کامل LOSS% اشتباه روی شبکه‌های محدود و DPI (مشکل اصلی کاربران). حالا تایم‌اوت بین Dial، TLS و HTTP به‌درستی تقسیم می‌شه و پکت‌لاس فیک کاملاً برطرف شد.
- ذخیره خودکار IPهای سالم بعد از Quick Scan و کپی در کلیپ‌بورد با زدن دکمه C
- خروجی فقط شامل IPهای سالم (بدون IPهای مرده)
- فرمت txt حالا ساده: فقط یک IP در هر خط( از
https://t.me/MatinSenPaii/3543
برای بازنویسی کانفیگ استفاده کنید)
- پیش‌فرض‌های هوشمندتر برای شبکه‌های محدود (تایم‌اوت ۵ ثانیه، دانلود ۶۴KB)
- کاهش تخصیص حافظه و فشار GC
- حذف IPهای تکراری در اسکن
- اسکریپت نصب یک‌خطی (شامل آپدیت و Termux برای اندروید)
- بهینه‌سازی منو و تمیزکاری کد
ممنون از همه Contributorها:
ProArash
،
M-logique
،
Mralimoh
،
Hoot-Code
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/MatinSenPaii/3547" target="_blank">📅 03:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3545">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iDgccKsEp3SEZekQo7w08h9CKg9DTHDYAdUTbudtU62mqpKNlTAMooMaj-AU5cxx9jC8r_TnCWttud56Gb4Nz6Oy2ZEWSl1_T-L-pOIosiiu9L8I6QWkdIz236GW6Jw65kuu3FXNPuPJWYi41lgvLclqPwG-I6oDW-Pi_3HM-U7EPJzZfDZqmZrhwn91lOOj0ZKcRVmnFl1TuF2EXKplp8XmyheEOyi6_EFIozSpCsCrb262D5e947buou2KjzG51Lho5RN79JPvVb87ay84vI9dXWE5p-dfhrYHcHFyYSgz0Joe6R7zoCAfKYt-sdngOLj4nTbwt1sJGvBJQ-gbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DkkDtf8zxaA4DItALSzpQtJ8YLWicCFTA3gnGIEkwmwAKFPCs6E4gCiBIJwSg1wkQIWLDD5GsToIkmhQbeqXdR-zL8mH9q--3kL6FB0Vg4LEyCBYSyF5NnkK7zak_Kxr2HazCoFd_td1yL-HveyfOFGCEQANONa3INjo7ELc9hCLdO8Smyhv0_aRhF3INhSL8tPSxGsOVhX7ZBdKlyCJGFBJkDzC0oV1RAzHfBxLu--H4_Eqt6bPccXEJ180psU_aMBujlG8qkFK2sDn093nGyLLSXloGoXZygsenH7IlHrHHerIgNvQcmTsey8DKCJPORb8AJK04bna9dnTqt_T-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی آپدیت جدید اسکنر، آیپی‌ای که Healthy هست واقعا بهتون پینگ میده!
همینطور با زدن دکمه‌ی c روی کیبوردتون توی تست لایو، میتونید این آیپی‌ها رو کپی کنید.
یک سری دوستان عزیز متخصص هم برای تست بهتر، روی پروژه pr زدن که دستشون درد نکنه واقعا.
تا دقایقی دیگه منتشر می‌کنم
همینطور که توی تصویر می‌بینید، یک آیپی به من healthy داده شده و همون داره واسم کار می‌کنه با سرعت عالی</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/3545" target="_blank">📅 03:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3543">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CjWdSL7emK0yFJakk3spFnPefMqJJCmK9MQFnh4Y7n9Z-lQjDnOYS7thhh99wfwv6xVVQIV_phQX3r4w0XOdgi2QfvvexCS-2RRlWIM0TfVtFCGo8MltLcwgXo9BOi-hmT-wym11JgC0p0dg3qXBfx2P-EEaMMTI0xi0QnugKd1KW2I5LEJFZHKOXUzTewI4K1i-RRDDihQS7pQ8aioX2rXVvE2V1sqnPtIoX-kKVE4lEg66zcym4-S05-Rh5UfZVg3zdJN43ZclyzhirMZRIlJR8FAzgJSKM8ycP8lLpW9ptBWPZ0XWfmFUSOFMjkmHNnzG10yh6qTYI4RGOcN9eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازنویسی یک کانفیگ تکراری با آیپی تمیز‌های متفاوت!
با این پروژه‌ی رسول عزیز می‌تونید این کار رو به سادگی انجام بدید:
https://github.com/seramo/v2ray-config-modifier/
این هم نسخه تحت وب ساده‌اش بدون نیاز به نصب:
https://seramo.github.io/v2ray-config-modifier/
برای حمایت از سازنده، روی گیتهاب بهش استار بدید اگر دوست داشتید</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/3543" target="_blank">📅 03:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3542">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeXuwqtBXF5l2PELzCv_GtXy0uM4EIdHrKZYUrQ80jTJXTTCecJ7S_OZmUwUdFAKOendBGe9y7bRAPYcwN-6tGK8ldqv0DjVBHFgBthDzHZxHa2cK6Gkch3fkjPTx0mBvJX99sxY3cd9ZiuzzCewcEZiq7bHnRF_GxghK0nquPbrY00Q50cUe-GYVajfr9PxwOPrITbRDTGHMiTwuKuR1hwTkd_XgwvLem2v7lL6C7D5i0wI4X95SDLEfyawY8bPHsQyrjab-qFbH0uMHi0SlESdjPQPwjfo8E70wNs97g1XZDnrbFhSYCILDZuKogBD4YiDee8l8oPhGOT4mzAjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3542" target="_blank">📅 01:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3541">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/MatinSenPaii/3541" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3540">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/MatinSenPaii/3540" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3539">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خیلی باگ‌ها پروژه داره و تا الان نزدیک به ۱۰ تا issue ثبت شده و دوتا pull request
دمتون گرم. همه رو اوکیش می‌کنم تا صبح
❤️</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/MatinSenPaii/3539" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3538">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WHtmWWQgtPGy0motscK9Sy9DKOx6ogVT-gZ7aY0xfofU4ES9lGMzlSYVlncAUlNAnUIKqT7_UmBTmR3abdgyBVYXLQZVjtrbTm115E1LqT3Zo7aHMgIt0FTcUCzNwI2DMchlu-CnjLOSxJ34t_nCvUupi39t8-7R4RrlB23G6JgVrtVnVQnZnTcng0WdegIIRf4ujLEmNQlXn-h5capSaPH7TQaSq48Fw7VE_WoiXXlKwaIzxVJbwL4LXjKggqUEfs9eglwMG-kRdRV5PEgxJ1yu4Hdi30vl1ZYGJgDpUoV4Pxf_d0qQckju1hEObpfWuw9QhoyycPhyWEkwvIDF-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3538" target="_blank">📅 23:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3537">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3537" target="_blank">📅 23:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3536">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X6KwuEXIg-yAwpyjbopuobidh3KJgTM3LxaTt7lkTLY6ULRWsK3qcSlcKkbeLKKL4WKWuHbO3IJRnPR0N4zei2STaPG1l6LXojeBtqKTLYKfhuQkR80A8-bWFbhN-u5rduota-m0q3v1QtR7FwbVJSsqR1TM6b7D8K4dXYRY3ctLbLHf_oNJ2A8d7tkWTou-dztQcWWJewbBeVAwwiGcoyS-ttA3E1fTPIG3tOySRh1jDsQvNMOLaovBArMfwy1SF2m8v2c8-5elM5BciXoerejNkG1TFEekFv-ns8nJOaKFke48o1Qc3NVSOcxTu-WveMAEHH8HJlmSZTEFyW-P4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه
و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3536" target="_blank">📅 22:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3535">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NFRHArDS3yhgWOF_-_P2KHERQANS7Aigr31B8htPREYkYLr6ITWhElRLIwEk5IR73P2xIZ0pMzWZysXk84_Qgez7LRbukgJvwF1lExgXVbPEI6Ec1Js0hKTTqMFxlSCn1rhCywoQWL2HZtiaxxNwWPQH9dzDluQyxo7iDuNbKaZJfPBkVejJyhjqKf9AZui_myiYbc3Q_TY1RVxdFuWK-gDDQ3HmFonnmKGBywSr4lG4arYSND1RZKj7a_u1FziV_z8DVak9i9jkrEnj-YHF33qSMkxSwmgU3KeUgNk7rBhbbWu9ePV_0mu_o_DcctRr0bI7xT1JC7Y5JkjFti4EJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌ها کاملا رندوم اسکن می‌شن. برای همین باید تعداد رو خیلی بالاتر در نظر بگیرید. حداقل ۱۰۰ هزار</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3535" target="_blank">📅 22:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3534">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این اولین تجربه‌ی واقعی من از اوپن سورسه پس اگر کم و کاستی داره، ببخشید. صرفا این پروژه رو زدم که نیاز خودم رو برطرف کنه اما دوست داشتم پابلیک باشه و یه پایه‌ای باشه که از ایراد‌هایی که روش گرفته میشه، دانش برنامه‌نویسی و شبکه‌ام رو هم ارتقا بدم
❤️
امیدوارم که این پروژه‌ی کوچولو به دردتون بخوره
به شخصه از اسکنرهای پیچیده‌ای که هزارتا مقدار داره داخلش و نه میشه به عموم توضیح داد نه میشه به راحتی ازشون استفاده کرد، خسته شدم. نیاز داشتم یه اسکنر داشته باشم که به صورت رندوم، به تعداد دلخواه آیپی اسکن کنه و تست کارکرد بگیره ازشون</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/3534" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3527">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای نسخه‌ها:
🪟
ویندوز (Windows)
senpaiscanner-windows-amd64.exe
مناسب برای:
سیستم‌های ویندوزی ۶۴ بیتی (بیشتر لپ‌تاپ‌ها و کامپیوترهای امروزی با پردازنده‌های Intel یا AMD).
senpaiscanner-windows-336.exe
(یا همان
windows-386.exe
)
مناسب برای:
سیستم‌های ویندوزی قدیمی ۳۲ بیتی.
🍏
مک‌بوک / اپل (macOS / Darwin)
senpaiscanner-darwin-arm64
مناسب برای:
مک‌بوک‌ها و آی‌مک‌های جدید با تراشه‌های اختصاصی اپل (
M1, M2, M3
و جدیدتر).
senpaiscanner-darwin-amd64
مناسب برای:
مک‌بوک‌ها و کامپیوترهای قدیمی‌تر اپل که پردازنده
Intel
دارند.
🐧
لینوکس (Linux)
senpaiscanner-linux-amd64
مناسب برای:
توزیع‌های لینوکس ۶۴ بیتی روی کامپیوترها و سرورهای استاندارد (Intel/AMD).
senpaiscanner-linux-arm64
مناسب برای:
مینی‌کامپیوترها (مثل رزبری پای ۴ و ۵)، سرورهای ابری ARM، یا لینوکس‌های نصب‌شده روی مک‌های M1/M2.
senpaiscanner-linux-386
مناسب برای:
سیستم‌ها یا سرورهای بسیار قدیمی لینوکس با ساختار ۳۲ بیتی.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/MatinSenPaii/3527" target="_blank">📅 21:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3526">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCVmQ4pAZDVmH7jDZBp_c9SCs4EDdqj_0_l5clxc3x3AfIKyocnoX7BcAWye5sfus6rqSgVhEQNIFwsebUmYeghANVwNWQS1pmnZIamqg46QRjkf22xR0b-KLAtynZx2XTSMgrXA-TDyV9YHqOXi5giy9TPXWEXooIJNnvbfb2vDFnG-qugp7sLUHz78KvUDFNmvZEOCgzFjQdWjtfwZggNcooU7kuP5XyUo0Tfz04nVGun67HFie1G3hf_kiWPTTWhqKVlHkhYXAIuFYqL9FrvpOc7J7QMW6_S-vI_QLfb35rMVxsJZh0xJNyiChf3Dr0raGT6y_jQwp3Uc0xDnsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
پروژه‌ی
SenPai Scanner
— اسکنر IPهای Cloudflare
چی کار می‌کنه؟
از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.
چطور اجرا می‌شه؟
فقط فایل مخصوص سیستم عاملت رو دانلود کن و اجرا کن.
۴ حالت اصلی:
⚙️
Quick Scan
— سریع: تعداد IP، تعداد worker و timeout رو انتخاب می‌کنی و اسکن شروع می‌شه (پیش‌فرض: حالت HTTP + تست واقعی داده)
⚙️
Custom Scan
— کامل: تعداد IP، پورت، محدوده CIDR، فیلتر دیتاسنتر (مثل FRA)، حالت tcp/tls/http، خروجی CSV/JSON/TXT
⚙️
Test IPs
— لیست IPهای خودت رو از فایل
ips.txt
عمیق‌تر تست می‌کنه
⚙️
Discover Colos
— می‌فهمی از شبکه‌ات به کدوم دیتاسنترهای Cloudflare دسترسی داری
چی اندازه می‌گیره؟
- تأخیر (latency) و jitter
- درصد packet loss
- در حالت HTTP: تأیید Cloudflare + شناسایی colo (مثل FRA، AMS)
- یک نمونه دانلود کوچک — تا گول IPی که «وصل می‌شه ولی داده نمی‌ده» رو نخوریم
نکته مهم:
این یه ابزار
پروکسی نیست
— فقط IPهای خوب رو پیدا می‌کنه. تست نهایی هنوز با همون کانفیگ واقعی‌ات روی Xray/V2Ray هست.
---
🎄
پلتفرم‌ها:
Linux · macOS · Windows
🔗
لینک پروژه:
https://github.com/MatinSenPai/SenPaiScanner
دانلود فایل‌ها از گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner/releases
دانلود فایلها از تلگرام:
https://t.me/MatinSenPaii/3526</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/MatinSenPaii/3526" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3524">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kqbwiu--T74bePGvh4wiiI-hP7Tnj7fyDHTJbtLvYsMFC4JklCkU1BfjyFOhf8IJJLsR2-bXOywKtpzchQGUVHS8qncAPZnuQEeQYsqBDXbZ9doCGcNMWBXm8DKm6NBf7YGJh3Lja8OdiGvIijus72NHsQDDmJTKJNdg9wv1isFkAJJmxJqdUlE6MMnebric5DsTXYK2rjAYaZygxtgEcVHWuJieVEElsXxGXm7dUPaA9fHquTuM-qD1Tez0WGiT37Gx8b7i1kXA83VnP-meckTgO9argLCz9Q2xbK_IHJUPPV75FXFNlGkBrD0npck3EnbHudxASTB7Lev4OSVP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JHuplmRFXAc0jaBuHr8-KlA0CsSaliWzBuCpBe5upjX-e8QIYHOVWRPWFKvOErjfytKBPryaBUELkLXqlUybUXJ1SyoH-0v9WDTqcA1lfNPix3QyB0HR6aiWDJJfheYeknvoLcacnzbkC3iGlznu6mGbyk4mYTidy4JV1-pUAtoCSADlfIy8TZXWA1Tw3tJLpRVtcKRdhPwv1uPj6NaczaaMw5uR6ppKn4K3oFXSFJUa49444nzSUk9BjQRnDhiGZAh_QyBzHdeOoU98nt8ZGfMf5h48PmznoeA5B6gNeOdbhj_8uBkLgu2VJYUdhqRJEV_abfgfZcduPhCHRbfFQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین آیپی ای که اسکنر پیدا کرد و داره کار میکنه
مبارکه</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3524" target="_blank">📅 20:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3523">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/MatinSenPaii/3523" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3522">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/arqMHsf2DV98dFdBQw2wbRciOPU5PrKCWHsk9mjyOiQDNAt5jYeX8VLQ919yP1WHyKTvL2mBhmF7B_wCfGjq4CCBKODwN68hnCC8HYiTYivocAYRQvJb-mdm_AdnZJIldLGJPDJntTsP8cX74x7PKa4iRTVtF7UCUQgBYoUjAgOGF6yXyc2v6jfwQ6sPQUlaNxbgAplCiZ6gHgQHtbGNzpJhtUFpcmznFJRneo0ZpsrLxxWUjRad013voOGskwXJBidmXZRObXXt20JPE7x1hhuIV_KW42P0SZCmkkpdq1vPkDAlFVJMiEyq_85j_f3gXEk5kh0gOGuKlGJWgJCQxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/MatinSenPaii/3522" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3521">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jzq-NQ8mKu-o7MKmx2NyzciC-_pVFvDNK5iEwltRTNKZ_8VWec0EqqGei-Q0IyBj7F6egRHQXiORj8N4m4EPPxL1GoviaDjg0aYjYCfoYnBSnDc3yZ9cmH-cmJR7fdntLIXWULljXgIEm1y-vmsG9E6WU6I0e40ZwhO6OHFdfF-qa-dGN_IqxCCZJPj_btIlIAXHTWfUE0_liXHk4hAUh-H9zWBBjYgtiidjh6aNSNIceAWn9UJI0LjQ_lEjGEZnDPLlUpvGnVi-GVSQm0E4DaUMaOQ8Bw703OsF7nxXWC85CKwNIclqFiCZ1YJP49dWXhD4v3Q2T_MSFyuKb30CPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/MatinSenPaii/3521" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3520">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آیپی تمیز مخابرات
69.84.182.49</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/MatinSenPaii/3520" target="_blank">📅 17:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3515">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.8-fdroid_universal (1).apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3515" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت آخر V2rayNG fdroid
🔴
🔴
🔴
دوستان برای اتصال به کانفیگ های بات از این اپ استفاده کنید.
@WhiteDNS_Installer_Bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/MatinSenPaii/3515" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3506">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a5dUlclCX0CNrG9IO0cLUGPn88k27U3LnBszMwY6VVZvbSQZeQ13jhrsKM-O4prlV3liFwByGcwlt4u97LXfTTvW0vi9H7UdXxVbZ4hgcvYUXMLsal3rKql5nldmm0cxP64CsOxYCvOZN8qGMfyagTKUHRULTiFMCTxPP2Xg-vRlWSTEJgWfjruppcLX9pJyMo6qX6wgnXsSV491em50FlY53Um9_ZY0Xvco7hqlL_ccTJ8Dq6ieUJgxbjujGwv943q1ZoVAM6NOd9J7gaRMErHiUZzwcZlf9v_QjRwuhQvAF-_TGn5cDpgOg3jiypwtAHXr1u6PUXheYHEN-CB1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hPsAc3pNYHme2P7ae5973XeAuAOpF_yL7ORbPJetQI9VBddsqPdE5bfDYBpJghOvShyu-bQjR9yG5BbvPJNizsWUDJKwwjRW79wOe1BIHzpTBs_41uN4CB9UYOCBF6v9sWBsZKHf4aWQBvviWgRgHWx0XdMWXn-3rplzoSl8spLw_D823EcxuxUQx10TpY6uTqx5MbPaMsgPb6MRf3GiD_X2kT2hJyxLFLEP4daeqNiZ5sOwzZScjPH5IWhV-5hk3xiJ-ztdsQHIt_CxUCU7-zlb27dHstYdpsegSj5uzaY39NrECq5oPecQ5x5p_UQkXcy6CPQnZqGomrtQuzpYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aO94P1mEmKqZ_8_XDa5pWm4cPXrX31vAQTJoT-D3zYsbXSwWxuxyH9s_vVG46njiw-biJoQJ9jCVnAq-WOnZlFF_8HdAbZ5p42SscDYUhrsSt0bq2rPOTWp2BVNCuVHgXNJBspJuHmCv7QIQca-LwCluU3BsrQ7ysEVbDgVeh4OQZD2jWZwIHHKwbx7UTvA71PfG4mh6uxuYJ9i7ZFPnaE6uvNiG_DG4cXCaQJ2joPGlHYyZx8JYZkFSbgMvJo8YRSDXGENa714mSUpaTD9_z8zNK3HvUfwUKbpHXm-JgkEWEkIVdDayDy8MgULy8lNv58BvSiM3ttllNR1H3W4Rpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H1rqeqX_fPFMiW_cns8bYJ9JUQONJvgwjGGeGCGmJEaSM92As_Fszd6b1vVnZdOec4uvAeyZlucieGMmrqbNbROyerXlRt5fnxxs6N30LNP5nGAE9CdlmRmqyZ1A1X_jb-wVcEsdQrEg8Ib--K2cJagS7fiA079nR7j8HKvpYS7Beo4rtOSTnnUbW7Hg-l4eJSKmNnDHxYP_slOHHWriV9AqTWeBgiq3ZhVmZ-EhZG7OfGPPYpztll2iHzgjZaOu2U2fspw_QMaySEWB7RfzdRlLrBpG3aLe_rDZsnkf9DA4jRzjqvcnOeJPlerBYmmfBlCqwT2y7TbcpPHS1KBJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OXvVxG55JZGeXsJ7eeAn_fFOWVBEh4ELemxWvysZ4diJ0AdNqG0Dc2gaA5UnoEOdaf0vZTuoBudLFL3OXKaYDlaueBucbwrnpdgCAjYmfZH508yWPnnLbLnU4hKSsuvDIcP4NjtvPkV-o5CsCV2l83TUnoU4DPAQnaSiDrKY2OiXwCNO5kML1eVyRr7Ys4Kj1JJqBJWEXWIQyDFiQ5sPtGC929hRM8RrbWXdX2TzXoLSfGSQmySYF2A85SGcMi_SPZg0Apis_3WWrjFAPPvI3R2Xuvm2KJ_kx84nRZARrkQwYcGQticmR-OfLRo0ZCT1b1CYBXkpgZxC2zOuBLoDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JH1a69jms-p8QVOI0wKMwP9fqlKmEgScjd-4qLFUt1SM_IoRQ2usUCWZnrC3mFqfxb-vd-c4jqhYdajVpDANRuQf_dZxuDwdK0_06NzCgEDbEnPx2DrIHCq_1Jbr4YqRp_CAsZA_WyOPL_7les-hqBc7CQ9FoI3V8KEeZsl7D6UJ0Sq1ZUvSFTvIJN_nSw8RXkneu4xUbogMz4E9anicH_TXdVvBoz7DzwcjhBM1ZWyQzEK1Hgqo0Sn2IYR-FtVB0hB-8cBnmS-EloCl04l1eqcaBhJESAlF2l5-oHJd_ApMpZsr2k8ZN--I14zVU3kYovxZPgEf6kuelcm_bmfjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qIxBX4Yw1oiFznPEhd6s2N9qfSFKu5lj25bBdSkJDj6R5WxadRyESA8pLw2R8XFj0SwpeFa-N0QhO-bH85dSuDzvgFPtLuCB7LKFfbBUv-hUIa63OoFJ6ThDlyzqOMRspl29enucg-aC_fJz6kWiZpaARpeEfMshHPpbyqMtBegtuNUa-S3OFxN0trV4HukRT3LGcio48d4zZrx7WA5UqOKdncQLQXKqxHamN9yYQcSsz2kwhz1sy_2-5bTmvJeLLoZLkGdfOVScMjPFUJiOKhx1-a5gHSZzFSZbPJVBNJzPR-bMs3P6TPGSPt9kEJTbv8_wBUeOItKSGAv2rIuNwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bNuJlG71S8KAn0gVfg5ndspfZC_DbTtqcUA05ykURqZyfCZb71T5vMrJOir2Q9vrY0thgS3nkr_SMT3H0F85rk0x5No13tLzUna_VKJCnLU5MdBLSculWFx4vikFmNI19p1Of9U2cVDMGuM_KosUwEu1bXopVK2vj1bvo_FIfpg5YMBTk6X7Xm-7T-pLpVd7jkR376SUHxxQDEdJ6qMF35ZOUSHHyRNtq0DJPBTiAll0lj1uE77BM7gcWDB8Q6hVGNkyhRvGRvWATTEraRSFPS_Ui592tw6NtWpTUMI2I0HcLI1SuFOV2xW_0Abqu-uphx7SDEUKBpxX-efo8s8awQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o5UHluKS3Ywb9DwCQnUyJeg6LY7MuBfFkvPReIx7jaMAqwIXrQ_OwULcYnmYOTko2PspXtg1QeRz8c2mlu-HwIPDazRN3GY2bYvmx0q2VAycwGP5OOczrig3h4WNhkpTjdyBRAhdYQalMaGrv0P6lQ-d3hslTWvwqFcMOW65bnJx7rjMwgVov-15JA0l-zvbC7tEJQeJHDpclTbbTJN97jlVB-5AI_ME_bBi7TjhvcK9DZLhIGvm3vLyJR8MEHNXq3EAOHfZdikUaezAWwG1RYxw4ebfjsU89wEAKWii5wLOu5M8r9R_H_Us1HPyhBMixQ4Cz4kwGXzGe8O_XymsSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش قدم به قدم اتصال به کانفیگ های بات
نکته
از آپدیت آخر  V2rayNG استفاده کنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3506" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3505">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3vtqFQxkLCnxlDqnM7F0YtxZr0ruECE5mH7DOPpSKSsMuTCee85xwaTjCDtoJkNwAasaUrjUd12_PQAbemjmSVwOrtIISPreA4-P-Qhws0aOErlVmBYdtUXzk97tT7tkf7cQVtquXgdLnajneLoEjnI-zt2CuFQFsEbQzj_mwM0fonwHAs8-MfPc0wOo-98tq1DCyHxXCuh4q-nWG6Us3NMQQGK3WEBBH3GMpDdQZUaBIMI8lmGBpSMwbMEx0nv9PQ6gkZSLsUG9-O8B8yciav05VfAg4ibEKZDlh6XMsZAsCdNJ9rusxCnVEZxne7su42RAMSsJT-yxoUVYd3x6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3505" target="_blank">📅 15:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3504">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستان ربات تحت بار و فشار زیادیه. کمی صبر کنید پدرام داره روش کار می‌کنه یه کم دیگه مجدد واستون قرار میدم</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3504" target="_blank">📅 14:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DJ6mNZJ1dS21ixTlPq_8Cdo6wQb01GLVGwyUfK13A58pSJ4ADQUg6zHuind9PjlyOzxDg5GOA8xrWGddZEtgAk_IPdpnVtxAufhjamSoJcA4SLD3R7RHPE8wiGeK9Dx-R_g-GZF_iiVrCyAxWXrL30n10DZqaX0PBf20fFDogynPkKpePpAbqTPDz3DbYDioSYslROhS5v5rd380exCWY6hChyaLSmTTUPuFr1cB4WkBcnr6L6l5AeuTmDSkl-NgSeD8IIaYPt8ibn-D8B47YzM7qp_4b_qDEI0ruDXcI1rhZgP8ugQLlmL-HxZkmds4TZ9kD-xWhscrjIrkcCOR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شما رو نمیدونم ولی این اینترنتی که الان دسترسی دارم بهش، هرچی هست بجز اینترنت.
در آستانه‌ی ۳ ماه قطعی، اختلال و نابودیِ کار و زندگی مردم، اینترنتی را «برگرداندند» که طبق مصوبه خودشان باید به وضعیت قبل از ۱۸ دی برمی‌گشت؛ یعنی دقیقاً همان دوره‌ای که فیلترینگِ گسترده، مسدودسازی IP و دامنه‌ها و قطع دسترسی به پروتکل‌هایی مثل IPv6 ،UDP و QUIC در شدیدترین حالت ممکن بود.
دنیا در این ۳ ماه جلو رفت، اما شما ما را ۶ ماه نسبت به جهان عقب‌تر بردید.
۳ ماه از عمر، جان، سرمایه، فرصت و اعتماد مردم گرفته شد؛ بدون حتی یک عذرخواهی. و حالا همان اینترنت ناقص، محدود و ازکارافتاده را دوباره تحویل داده‌اید و اسمش را «بازگشایی» گذاشته‌اید.
اینترنت واقعی یعنی دسترسی آزاد و پایدار به تمام پروتکل‌ها؛ نه نسخه‌ای دستکاری‌شده که فقط اسم اینترنت را یدک می‌کشد.
روی «طرح تبعیض آمیز اینترنت طبقاتی پرو» همه این پروتکل‌ها در دسترس بود؛ یعنی وقتی پول بیشتری می‌گرفتید، ناگهان همه‌چیز ممکن می‌شد. سؤال ساده است:
مگر امروز مردم پول اینترنت نمی‌دهند؟
دسترسی کامل به اینترنت، لطف و منت نیست؛ حداقلِ وظیفه‌ شماست.
هرکسی این توییت را می‌بیند اگر اینترنت واقعی می‌خواهد، باید فریاد کند که این وضعیت عادی‌سازی نشود. مسئول مستقیم این وضعیت، شخص مسعود پزشکیان و ستار هاشمی هستند و باید بابت این سطح از سرکوب دیجیتال و اینترنت ناقص مورد سؤال و بازخواست قرار بگیرند.
خبرنگارها، رسانه‌ها و فعالان حوزه فناوری هم باید بپرسند:
این چه اینترنتی است که به مردم تحویل داده‌اید؟
✍️
iSegar0 || سگارو</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/MatinSenPaii/3502" target="_blank">📅 12:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">همه میگن سایفون افسانه‌ست و مال پیرمرداست و هیچوقت کانکت نشده و...
برای من WindScribe این شکلیه. حتی قبل از دی ماه هم یه بار واسم کانکت نشد
😂</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/MatinSenPaii/3501" target="_blank">📅 12:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3500">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خنده دار ترین اتفاق امروز این بود که دیدم کلی کانال که تا سه روز پیش گیگی ۳۰۰-۴۰۰ میفروختن، شروع کردن کانفیگ رایگان بذارن
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/MatinSenPaii/3500" target="_blank">📅 11:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3499">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
apple.com : 17.253.144.10</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/MatinSenPaii/3499" target="_blank">📅 10:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3498">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🍷
invizible pro
🍷
با این روش و sni های زیر میتونید توی برخی اپراتور ها متصل شید رفقا
✅
sni: certum.pl, neshan.org, subkade.ir, gifpey.info, shaadbin.ir, uupload.ir, letsencrypt.org, gerdoo.me, nairobi.saymyname.website, actualities.google.com, myf2mi.top, chatgpt.com…</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/MatinSenPaii/3498" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3497">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsvAPYdl4F4xRdVcFYV1oZnvTmTQ-spL19OP76bDQsRqrupUNTGnZW93e_wpeFg52Phiyae6Obyv01w4sPH0N4LtNbqvCwOPYuaC-AM0Of3ctKONPPSl0cXRwxWc4gl_J4jcRr3pLQTYdq2KlarSYbS_kl6SGoVNDQZxc6ntYxdpSsvNagUpsPKWhTNMbxeMt9pCWODjWjFSSa4QnW4EWkOYvqtfDVqQ2I3lomHifjXvZkxfnm0c0diL1aT7-waz1irjpZ5T8q4pzxY-s1ChwwS4eGdcdAPvb3EpeFBMZONE5dCOJeby8UUAHrKzU6jAyN1Offxj9RFASiEvqEIUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
invizible pro
🍷
با این روش و sni های زیر میتونید توی برخی اپراتور ها متصل شید رفقا
✅
sni:
certum.pl, neshan.org, subkade.ir, gifpey.info, shaadbin.ir, uupload.ir, letsencrypt.org, gerdoo.me, nairobi.saymyname.website, actualities.google.com, myf2mi.top, chatgpt.com, bazion.ir, 8.6.112.0.sslip.io, abadis.ir, ikac.ir, ebooksworld.ir, iranicard.ir, gameq.ir, melovaz.ir, sourceforge.net, google.com, scholar.google.com, libra-books.com, uploadboy.com, soft98.ir, daneshpaz.top, berlin.saymyname.website, epicgames.com, uploadina.com, sarzamindownload.com, asiatech.ir, shecan.ir, par30games.net, 3fa.ir, taaghche.com, downloadly.ir, oldtowns.top, cafebazaar.ir, Shaparak.ir, uploadkon.ir, news.google.com, varzesh3.com, hooshang.ai, downloadha.comfilimo.com, gitlab.com, search.bertina.ir, mail.google.com, chat.boofai.com, support.google.com, search.google.com, vercel.com, farsroid.com, bosgame.ir, 2.188.21.46.sslip.io, divar.ir, okta.com, snap.ir, nic.ir, flzios.ir, digikala.com, fastdic.com, cdnjs.com, 162.159.152.4.sslip.io, hooshyar.golrang.ai, openai.com, aparat.com, download.ir, yasdl.com, pastehub.ir, downloadha.com, iranmatlab.ir, bitpin.ir, Python.org, my.files.ir, post.ir, picofile.com, namnak.com, gov.ir, dl2.sermoviedown.pwmyf2mi.top, nixfile.com, pirategames.ir, balad.ir, supermario.corp.google.com, faraazin.ir, vgdl.ir, aharvesal.ir, chat.smartbytes.ir, cdn77.com, behmelody.in, cup.theazizi.ir, alibaba.ir, zarebin.ir, patoghu.com, subzone.ir, navaar.ir, zoomit.ir, rio.ggusers.com, linklick.ir, gold-team.org, dlfox.com, centos.org, fidibo.com, tamin.ir, guardnet.ir, atlassian.com, 2059.ir, site.google.com, sheets.google.com, react.dev, irimo.ir, m.ulni.ir, 2.188.21.130.sslip.io, f2me.top, myket.ir, dls2.iran-gamecenter-host.com, Telewebion.com, airport.ir, ubuntu.com, email.google.com, radio.9craft.ir, torob.com, vercel.app, rubika.ir, dic.b-amooz.com, mizanonline.ir, 87.107.110.155.sslip.io, chess.com, gapgpt.app, ninisite.com
لینک دانلود اپ
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/3497" target="_blank">📅 10:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3496">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شاتل و همراه اول هم شروع کردن به رفع فیلترینگ بالاخره(لااقل منطقه‌ی ما)
الان با شاتل با کانفیگای رایگان هیدیفای پیام میدم</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/MatinSenPaii/3496" target="_blank">📅 10:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3495">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-text">این ساب تیم مهسا داخل هایدیفای هم رو بیشتر نتا اوکیه پینگ بگیرید یسری سرعت بهتریم دارن
https://raw.githubusercontent.com/hiddify/hiddify-app/refs/heads/main/test.configs/mahsa
داخل خود هایدیفای هم + بزنید داخل نسخه جدید گزینه free روشن کنید هستش</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/MatinSenPaii/3495" target="_blank">📅 09:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3494">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اینها هنوز کار می‌کنن دوستان. برای من اوکین</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/MatinSenPaii/3494" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3493">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3493" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3492">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iGym8XQ2TCYigwRHjb33dTvF8gaScwijlEl9_PSL2Qs3HbHzvEp8sztcdvbTulymR9VcguK51OoOl0SNXSJMzdY6jnog8-fYkjm-tQGuKcid_sVvojNotlPLyoPhSIyQuJ9oQS_p238aHzKustXQEHoza4omgIztDacUTry9TDYs5eWDtDUpyZKod1ZLJ4xkPKcfWuFshwgYc-6yWarYwJRCU-Jk51F0MGMtti6fCGxPDPWtClit9CDmEcDyyz-Btq3d4gKFah7JIhekR5EF7PPcPnW0Qqt7cwKY7qZ7r4xvKYVV9uD6MDTh88PlI2AmULh0abPwVuJkTsgcec3FCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت اینجا توضیح داده شده:
https://t.me/MatinSenPaii/3467
اگر یادتون باشه دی ماه هم همین بودش. یک هفته‌ای طول کشید تا همه چیز یه کم نرمال‌تر بشه(هیچوقت به قبل از دی بر نگشت) و الآن هم متاسفانه احتمالا همون روند هستش</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/MatinSenPaii/3492" target="_blank">📅 02:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3491">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مورد داشتیم از چنل WhiteDNS و بقیه‌ی کانال‌ها، سرور اسلیپ‌نت برمیداشت می‌دزدید می‌ذاشت کانالش از ملت پول دونیت هم میگرفت. یک شارلاتان‌هایی لو رفتن سر این ربات که فقط خدا می‌دونه
دوران عجیبی بود خلاصه</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/MatinSenPaii/3491" target="_blank">📅 01:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3490">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">1- هرکسی میتونه با دی‌کامپایل کردن کدهای اپ npv منطق هش پسوورد و... اش رو در بیاره و فیلترچی خیلی وقته که این ابزار رو در اختیار داره. 2- آیپی پشت کانفیگ‌ها رو به راحتی میشه با وایرشارک فهمید نیازی به این جنگولک بازیا هم نیست. 3- آیپی‌های کلودفلر ای که باز…</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/MatinSenPaii/3490" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3489">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">با این ربات می‌تونید قفل کانفیگای NPVT رو بشکونین و لینک Vless معمولی دریافت کنید. حتی اگر رمز داشته باشه:
@DickiriptorBot</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/MatinSenPaii/3489" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3488">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">طرف با کانال دو میلیونی برداشته کانفیگ worker گذاشته توی npv و اکسپورت گرفته گذاشته چنلش نوشته کانفیگ موشکی وصل:/</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/MatinSenPaii/3488" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3487">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فایل Json جدید برای Spoof: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "172.67.139.236",   "CONNECT_PORT": 443,   "FAKE_SNI": "security.vercel.com" } برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/MatinSenPaii/3487" target="_blank">📅 01:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hiddify-Android-arm64.apk</div>
  <div class="tg-doc-extra">113.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3483" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/MatinSenPaii/3483" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=JtVLB47ZfFmI3OWNLHzKHmssbJkgfWEsqF6qSLYhQJ6EOCINj9L1NuOIU8i8BXUv1Qav7y7fYcYltar6O31_NJOgMMALJJ9kMkgJM3o9BzpLFvO8MCig6dNMPuTOChpM_lAGX3NoleG_r7klV8TgRVqq66bX9D3PosEALnMAsOlWbUvvNAtTtgfd9ivDzfqSrg4Dnckjl1qZcE2vYik_0vnPaaecMsC8NET2no7YG4kydp5jQEQC5--odTtsA6aWRrrsH8gm4MwFvE-G9SIfsSTCd5XRDWRosNtLqo6PJl9Ma-HrQGgroksFG7_ZZ9NN17cN0L6BrMb2NBgBB4oh1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=JtVLB47ZfFmI3OWNLHzKHmssbJkgfWEsqF6qSLYhQJ6EOCINj9L1NuOIU8i8BXUv1Qav7y7fYcYltar6O31_NJOgMMALJJ9kMkgJM3o9BzpLFvO8MCig6dNMPuTOChpM_lAGX3NoleG_r7klV8TgRVqq66bX9D3PosEALnMAsOlWbUvvNAtTtgfd9ivDzfqSrg4Dnckjl1qZcE2vYik_0vnPaaecMsC8NET2no7YG4kydp5jQEQC5--odTtsA6aWRrrsH8gm4MwFvE-G9SIfsSTCd5XRDWRosNtLqo6PJl9Ma-HrQGgroksFG7_ZZ9NN17cN0L6BrMb2NBgBB4oh1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☠️
آموزش اتصال رایگان با اپلیکیشن Hiddify (اندروید، ios، ویندوز، مک و لینوکس)
در صورتی که کانفیگ‌های CDN روی اینترنتتون کمی نفس بکشه می‌تونید به رایگان با کانفیگ‌های مجانی هیدیفای وصل بشید. چون مدام عوض میکنه کانفیگ رو، به شخصه تجربه‌ی بهتری از خود MahsaNG تجربه میکنید
لینک ریپو برای دانلود:
https://github.com/hiddify/hiddify-app/releases
فایل‌های اندروید و ویندوز:
https://t.me/MatinSenPaii/3483
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/MatinSenPaii/3482" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3481">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رفقا، Paqet مستقیم:
https://youtu.be/q4BbgdhPm-w?si=yd2q8LmmyvZ_VfsQ
و Paqet تانل:
https://youtu.be/nwpLOANv7VY?si=OMOXPs7XTV9uqk_M
رو چک کنید که آموزش داده بودم قبلا. رسپینا شنیدم تانل تونستن بزنن بچه‌ها، اما مستقیم هم شنیدم چندین اپراتور. به توضیحات ویدئو دقت کنید Paqet مستقیم با اینترنت سیمکارت(CGNAT) امکان‌پذیر نیست</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/MatinSenPaii/3481" target="_blank">📅 21:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3480">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">متد SNI همچنان فعاله دوستان. کانفیگ‌هایی هم که گذاشته بودم(
https://t.me/MatinSenPaii/3183
) همچنان کار میکنه ۱۵-۲۰ تاش</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/MatinSenPaii/3480" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3479">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:
1- آموزش پایه:
https://t.me/MatinSenPaii/2627
2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید:
https://t.me/MatinSenPaii/3168
3- و کانفیگ‌های این پست:
https://t.me/MatinSenPaii/3183
ترجیحا با ایرانسل یا سامانتل
4- سؤالات متداول راجب این متود:
https://t.me/MatinSenPaii/3189
و تبریک میگم! شما به اینترنت آزاد دسترسی دارید.</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3479" target="_blank">📅 19:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3478">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t0K__9MeAAl9NtMypDZ1r2h7H1af7NemVAr_N-FFTKcS7hAXhSKO1zSCj3q74lK03nOdy3mD1QsuPGehfAFqOBBNFU2PMhx_X0r-NZ6ilfE34flWE4bOHFrAjCowmG-du3ZhD7grQSP5WwkDu0PfqNPLdPEo6xeX1QlQR-pEfWgRijV1Qs3_MQwivJKFPbdBLWBj-XDWDbxmqUah5A6meO21JQ0gRcnhXxN9-aRTin3D9vpfKBULaq4Ty9zBY0VlON91jdSnOuU_y1xsjY5FvEbdNFHHJngMusv3yIFFatApksdfBUumfols4lrKCdiBzZB0ULsQgBJl18z04vgQCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت اینترنتی که واسه مردم وصل کردن
خط قرمزا اختلاله !!!!
✍️
SamAlpha_</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/MatinSenPaii/3478" target="_blank">📅 18:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3474">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TaRD1dpo6DUENaog-6p-0RK31DBOwIkZXdgfC4hT_QXs2gtst1Lrzw9xS2Hl8bNUZRFYxJk44VHCvQrjTd4k1I81gJ1CAamdR8O7jF5-lFoXH1ZPiHhBxsWI-WqSYj61WwyBkMGX8IRzKnSDn9SZscv09VfPMtq7phBB819hTu6ALch2cwHbPL1HxvecDSv3b2izIOmAi7D9IScTTWlkloeTmECoL0iDcgmTTdyVUrcZcqLR7NfLXzsxtZRcktQhpkLxvgbQHUPEtwLi4RDlIEwRla3nlQuCaZlDUcpqTEQtlSVNGtIUdDI_bor2XFxsBcN4zgLnF7W9Cz-1tD8pvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AvjRWubifP0ZxB55N_dtCJp8DKVpbNq8ezOdE9g6SRGp90ap_o9zIJ7kMN6C63wVfr5mfSLgjrFHLbExt1ZK1gNLeWfNt55EME5koGww3yum-1L5z-CDeueYA1_TStSKu-DGOqyLjgFp8uFNuulv5B36fBzCKeIGtahWNyC4F4m8KsRnFa3fidbEY-35hDLfRaobUVdhNc_84aqQ4OLoySQpvx2RK6NWX9X1YLpWx7LmGeWFvjIa8rYCJK7m5OX0rdGWLVuEdDcSa7uIJI1_P_iRyBr82sxI76noGdh7sZ7zg9z-NVhJJefQDzt26z9J_ufsjG8rTZY2VEd7pAvQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M-oAwZpD83P_O7XNLTi9iVGPajB-J9hPXzVYq8YzWF0jnWiNVi5hMnWjNETMJIDCHkTYM4djsCT2JhAB5YbqMzU-9jFeFkdfn6RN0r3t_O9Nm6kYzXx20onuQ4WeHDPLlrzmXut_6q2xAVBcqS0_leE10phRWzSjNFWRm56DSoC4iWhOzUvJAwUw6B3uv8SOPX7UT7DkyYJhhjBN71jjMUjW4LJCiFkr4SIkggBCbIJ_9DXuUCTghq13p6hhGPnqVijC3v4QB5e4El3TrP5SPnqHrvvMuwSUeh0zfVAKwTdLvjq8CBr0aT0i5cr3x4c9S31664-zNXj1m6cx3EbhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MqkDlpirelEelg9cRQNZk3EnHN7U-38BKLBbPxVJ0rDDpC6C2diaTGDAP5bBrrNEK-a9mW0CbSLlxRqWtFg4dDf_rexMUCtRy2LrERo-o7G6uF50Geqwj9P4mC-IIEFnHYO6PIEd6LRw5_vXnJ0ByfgXFHiAlIELreb6y-iJdD8zCUKoeutSFvFcPtr11zphkggS-rDQ5aaM3VZJKxI2F88r-swS4UE_4coRUsxxG7l8PmqA1S2EHL9pWGGwEtDwxZB1twe9_wbpN5ZjkeH_WMI_IwHb1r3HM0l17IpSoprWADHrguLbGNOnrPvXYIqCRj-yQfTCby-aHX-8s2px0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیر و خورشید برای من این شکلی شده که وصل میشه اما هیچی کانکت نمیشه</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/MatinSenPaii/3474" target="_blank">📅 17:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3473">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فایل Json جدید برای Spoof:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "172.67.139.236",
"CONNECT_PORT": 443,
"FAKE_SNI": "security.vercel.com"
}
برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/MatinSenPaii/3473" target="_blank">📅 16:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3472">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آموزش ساخت کانفیگ BPB شخصی:
https://t.me/MatinSenPaii/3443
آموزش  Sni-Spoof هم این:
https://t.me/MatinSenPaii/3186</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/MatinSenPaii/3472" target="_blank">📅 16:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3471">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RucwVMyb30xQ5lqQyRMX4OAeVG8K3MekNsgxgW_K_oOZv6oMNxbby63JXH6uP3_d9X_SPAJWUKPUPx4ua53mVQLys4XdQMXI1OPCVG5_AVfBoFDvue30rxMSkjPQCkrdm4bwqiNNAFy7Yd0OUH1vmcfssk3zEfd6RM9m62OiQ3aHerHdbIxpwHF0USxGMd3Zz0fDtZNHk31tjkF8jYaRBLwBmSBaGctmbZJ0KFSxgE80zTyIEbYn0DBybZX3OSQYDHu8kYOh2xJwP23Qq5xzqL2Le1cg9GEKwUvpci2DoPKaJi31YTVcecfGsOkAuvkaAvKKfP4okq5Jx_SMwgdTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سرعت آپلود روی CDN و Worker Cloudflare</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/MatinSenPaii/3471" target="_blank">📅 16:17 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
