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
<img src="https://cdn4.telesco.pe/file/A4V0Lb-ZoOnbaxjb9AWL__PJ89Wl9mmwbqcyDq9bdlEMkv3ih_ppjwIi17SJoalzEKS3jwrJ2iZifL3ByA6_JuSoVH1WjUtLQm6LtFznr4CcNzXggOY8UJY0v2U1eMkgZWfarm32apqIJSIA5ZcVIJU-UI6V1eVxRI22yK9RvYPrMdwZ-cIF3rhSZJBNmU8ie4-tNWHPCglFJZC7vXtBiS0fLlGFIT1U5X9RLl40hsd9cK_pDmHguSLan7YGFvh0Dn93icLsmlfJoQbt6bEAmk91wM2gBvZ9sYCjp3p4vjXnE0eGXoUWQguL7i_RWKGF6FCYT2htLirZes3CL2xuEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.6K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 00:15:23</div>
<hr>

<div class="tg-post" id="msg-9093">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🇨🇦.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9093" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/IranProxyV2/9093" target="_blank">📅 18:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9092">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 6 هزار
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/IranProxyV2/9092" target="_blank">📅 21:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9091">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POmILwi5DxDlYMs2oBWFUewHGWblkUNBon5o5XZPqvqUn17YP-3v_Ff7UiZZxqQoFN9jGO0-9CxtK-YDqjJlyOBtIRZ6XUG0WcIxb4YyzRDDwg38Aw5_eitt-KhCiykcYzwMBozinLmf3H61RWQ4mNGGYVqAExq10Md1F7eT7kop6pnmdg1Ue1NtfqS1HIgmKrZfgpZYXG7h6CFAgxCajkh1-lD-wgl7CY3aRTNtFnTaZYGgXyvrR9xXkilpiLZW7lHruGNJOkgD5iAMROf4dss9sD_owp2TpYVTR6aafb6YizI8hIqrZn0mual6rFJvkvXMcEW2d9z_Jkd4lLpa4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و...
فقط گیگی 6 هزار
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/IranProxyV2/9091" target="_blank">📅 12:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9090">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://d3d046fa-d372-430a-8ed9-083d62c44efb@45.130.125.194:8443?mode=auto&path=%2F%3Fed%3D2053&security=tls&alpn=h3%2Ch2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A1000000%2C%22scMaxConcurrentPosts%22%3A100%2C%22scMinPostsIntervalMs%22%3A30%2C%22xPaddingBytes%22%3A%22100-1000%22%2C%22noGRPCHeader%22%3Afalse%7D&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=ssd.mojaz-persian-music.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/IranProxyV2/9090" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9089">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=51.250.65.108&port=443&secret=ee3a9f22462890489c0bde045048ff9a17617669746f2e7275
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/9089" target="_blank">📅 11:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9088">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فول متصل⚡️.npvt</div>
  <div class="tg-doc-extra">149.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9088" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
🆓
npv tunnel
🙂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/IranProxyV2/9088" target="_blank">📅 11:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9087">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=zone.nolags.pw&port=443&secret=dd04d2a884220d45de24af8bade64322ac
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/IranProxyV2/9087" target="_blank">📅 21:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9086">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ʙᴇꜱᴛ🇳🇱🇩🇪⚡🚀.npvt</div>
  <div class="tg-doc-extra">14.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لوکیشن هلند و آلمان
🇳🇱
🇩🇪
Npv tunnel npsternet
💥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/IranProxyV2/9086" target="_blank">📅 20:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9085">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نامحدود🛰️.npvt</div>
  <div class="tg-doc-extra">149.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9085" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
👀
Npv tunnel npsternet
🛡
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/IranProxyV2/9085" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9084">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes⛱️.npvt</div>
  <div class="tg-doc-extra">3.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9084" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
💯
Npv tunnel npsternet
🟢
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/IranProxyV2/9084" target="_blank">📅 19:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9083">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CIVAX🍔.npvt</div>
  <div class="tg-doc-extra">1.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9083" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پرسرعت وصله دان بزنید
⚡️
Npv tunnel npsternet
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/IranProxyV2/9083" target="_blank">📅 17:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9082">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇺🇸سرور آمریکا.npvt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9082" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✔️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/IranProxyV2/9082" target="_blank">📅 16:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9081">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🚀🇩🇪.npvt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9081" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
💙
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/IranProxyV2/9081" target="_blank">📅 03:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9080">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=87.248.129.219&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/IranProxyV2/9080" target="_blank">📅 03:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9079">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🇳🇱.npvt</div>
  <div class="tg-doc-extra">24.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9079" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
📊
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/IranProxyV2/9079" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9078">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش به…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/9078" target="_blank">📅 03:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9077">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پرسرعت💯.npvt</div>
  <div class="tg-doc-extra">3.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9077" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/9077" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9076">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
چنل دوممون مربوط ب اخبار رو دنبال کنید
✅
با ما اخبار جنگی بروز باشید
@russiamilitery</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/9076" target="_blank">📅 01:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9075">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noqHNVt-5HNIeNE84O6g4zKRHGAiEYJjq720Ai6HxSYHVjQ0ZJ1rsjqM-vJnP-zGdVwGTgOKL4DjTZlBoTrLMkdL_-gdwFMhPwEvvU4TqSld4_4GBfw26YKzq0mLuD5Nzzr6YVw6B2eY9_GmCBBeVFvUVxlvAVNhXjkWLC2OFKX8xoVNZpYL-asxXw_ZLrKGSC1xXEv1XFLK26oC5zxeG3QvsBvS1CE3UJywGFXav6rcWxJ_8pl0SJfZOddypTzM97TVOUN3g5IfeMPTFyh_xC3XQ4fzddPKiIZNqHwBzKRMXw0mzsPrUBOVHD0-OboP0ZzTFYH_wIRKothofAfaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت اختلال و قطعی نت بصورت موقت مارو در روبیکا دنبال کنید، هرمتود رایگان متصلی که پیدا کنیم براتون قرار میدیم.
🔴
rubika:
@activityall</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/IranProxyV2/9075" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9074">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=157.90.171.183&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=178.105.50.21&port=8443&secret=dd104462821249bd7ac51913020c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/IranProxyV2/9074" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9073">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=north.nolags.pw&port=443&secret=dd9760e74174fb9717de21cc7e17027e34
https://t.me/proxy?server=87.248.129.226&port=443&secret=FgMBAgABAAH8AwOG4kw63QFgMBAgABAAH8AwOG4kw63Q
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/IranProxyV2/9073" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9072">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
احتمال اختلال و قطعی اینترنت بالاست
کار ضروری دارید انجام بدید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/IranProxyV2/9072" target="_blank">📅 00:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9071">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری/ترامپ : به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/IranProxyV2/9071" target="_blank">📅 23:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9070">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=46.224.226.79&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=91.98.229.218&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/IranProxyV2/9070" target="_blank">📅 21:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9069">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
ترامپ: شاید نیروگاه‌ها و پل‌هارو بزنم شایدم نزنم، محرمانه‌ست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/IranProxyV2/9069" target="_blank">📅 19:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9068">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
💣
🇺🇸
فوری ترامپ: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. ما بمباران رو از سر خواهیم گرفت. ما حق انجام این کار رو داریم. آنها هلیکوپتر ما رو ساقط کردن.
🚨
ترامپ: ما امروز دوباره به آنها حمله میکنیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/IranProxyV2/9068" target="_blank">📅 19:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9067">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-t9OoCRXB3p0W3Dohi3dKjlPlblDVnQ_0sLuHtBehAiO2KZz2Zwj3u1mSJWCmdm1VTsXVP70u6tLAvm_oLlDOETh01HRdSGrAOfvcqCxt3j-6_qYj0eavoDAQI7HpX8_jaqVA4PGbvivJc-ZRZalK0TitgFPrXPo6qXWkrKaLfB_gvyHK748wtHP1A4p7UAj61RmkMFF0j1sN4ynd3X5IZu2NgiffTJ4rs4ACU4Zvsszeo4clmnBDParrMQ_xkX6AlAlNfH98fuWI0XLRpy2_6HhnFf92ZeP-GqUH2lbqbIryRslu9lN4FF0QL4fdR83NmfLJ1qa7rri21b9HareQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/IranProxyV2/9067" target="_blank">📅 18:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9066">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تازه نفس♥️🤌🏻.npvt</div>
  <div class="tg-doc-extra">1.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🎁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/IranProxyV2/9066" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9065">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرعت قوی🚀🔥.npvt</div>
  <div class="tg-doc-extra">2.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9065" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/IranProxyV2/9065" target="_blank">📅 17:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9064">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دکترنیک ظهرونه.npvt</div>
  <div class="tg-doc-extra">17.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9064" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/IranProxyV2/9064" target="_blank">📅 17:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9063">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🐕‍🦺.npvt</div>
  <div class="tg-doc-extra">6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/IranProxyV2/9063" target="_blank">📅 17:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9062">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری
-
ترامپ به فاکس نیوز :
به صدور دستور برای حمله‌های جدید به نیروگاه‌ها و پل‌های ایران نزدیک شده‌ام!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/IranProxyV2/9062" target="_blank">📅 15:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9061">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ladC5R1ilZhdnDeyO3RPAUlTn5gdvvaJ_2XXHDEtdkIV_gGfBblXVODA0Pp0W1HvldIC0eaHM3ZfXU7PGADaKw6mj0hSkD4saMrL7j3_axai4wfcwIuW2HIyYAR72ItClWSnlNa-8f_2IMMXdsvJop63ECs4ToV6NE4W8wtuQnpIeT0P5rZP82DM9HUd0QHQlBZRbWCgq3x8lOYGrDVICy2QA3cIXIFpjlHMsVzgSgWdBItryKfDfMr9CcGrT1WTES2ruXQbF77GzND4LxtV48W9GBQLehTZK5rgBjD9P0EKt9twViUV3cO6s91LxBg_eYaj3TguajbXpKgfbdKY7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری-
ترامپ:
«ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. قلدر خاورمیانه مُرد!!! آنها خیلی طول کشیدند تا برای توافقی که برایشان عالی بود مذاکره کنند، حالا باید هزینه‌اش را بپردازند!!!»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/IranProxyV2/9061" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9060">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اکثر نتا وصله
🍸
✅
vless://9dbaa630-c895-4883-aa8a-20e8a48ff4b2@fff.oakcup.ir:2052?encryption=none&type=httpupgrade&path=%2Fapi&host=Ip.oakcup.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://5960576d-829e-4d09-8232-0e80121a6fe4@45.130.125.193:8443?encryption=none&type=xhttp&security=tls&path=%2F%3Fed&mode=auto&sni=ssj.new-persian-song.ir&alpn=h2&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://0c09799a-47ca-494e-a50e-828632ef9d81@199.232.78.159:443?encryption=none&type=ws&security=tls&path=%2F&host=bazaryabab.global.ssl.fastly.net&sni=default.ssl.fastly.net&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://5960576d-829e-4d09-8232-0e80121a6fe4@45.130.125.162:8443?encryption=none&type=xhttp&security=tls&path=%2F%3Fed&host=vi.mojaz-persian-music.ir&mode=auto&sni=vi.mojaz-persian-music.ir&alpn=h2&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://07dce2d7-9849-4e22-adb9-36d2763c3b89@snapp.ir:2095?encryption=none&type=ws&path=%2F&host=api.aramonlineshop.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://fc965ad9-bdd7-4815-ad71-b39ec5972dc1@141.193.213.11:443?encryption=none&type=ws&security=tls&path=%2Ftsghdws&host=octopusss4.com&sni=octopusss4.com&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://cabbfe13-038b-4dbb-9c45-5079c829abfa@167.82.0.1:80?encryption=none&type=ws&path=%2F&host=max-gb1.global.ssl.fastly.net#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://8dc7722c-2767-4eea-a28b-2f8daacc07e3@sca11.myfymain.com:8880?encryption=none&type=grpc&mode=gun#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://fc965ad9-bdd7-4815-ad71-b39ec5972dc1@89.116.46.68:443?encryption=none&type=ws&security=tls&path=%2Ftsghdws&host=octopusss4.com&sni=octopusss4.com&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://44b3ee72-cffb-4d66-ab7c-3138b9bdeeef@54.36.162.217:443?encryption=none&type=tcp&security=reality&headerType=none&sni=speedtest.net&fp=chrome&allowInsecure=1&pbk=upTVUrc_t7xF1ULni8pHRDhRES1sT4BDm1r8rugTzyQ&sid=ff815f58c7e77aa9&flow=xtls-rprx-vision#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e4e7866d-920b-4a53-a8e2-6ae9b2a42fc2@47.77.214.201:10035?encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://ae852d97-85f5-45cf-82a4-254eba345480@144.31.131.33:443?encryption=none&type=tcp&security=reality&headerType=none&sni=cdn.cdnjst.org&fp=chrome&allowInsecure=1&pbk=djH9iD2QV748ocK-wPH7HvDd03lu88zHhS4G-61w6Dc&sid=a120&flow=xtls-rprx-vision#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://d3d59da0-31a4-45da-bf9e-373c6ab140db@62.60.251.131:45656?encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e0de62c9-f317-4275-b7e5-8da7b7fa9bc6@77.110.127.191:9443?encryption=none&type=ws&path=%2Fpourya#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprMWRCT21PQjRvcWk3VW1wMzdhMWJR@82.38.31.192:8080#
%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/IranProxyV2/9060" target="_blank">📅 12:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9059">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=45.32.233.182&port=8443&secret=dd1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=mercedes.nine-gear.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/IranProxyV2/9059" target="_blank">📅 03:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9058">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
♨️
مهر:
شنیده شدن مجدد صدای انفجار در جاسک
✅
موج دوم حمله درحال انجامه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/IranProxyV2/9058" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9057">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
لیست جدید پروکسی متصل پخش کنید مخصوص نت ملی و شرایط عادی
🇮🇷
https://t.me/proxy?server=87.248.129.106&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=87.248.129.235&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d#proxydotnet
https://t.me/proxy?server=protocol.fast-mt.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=proxy.speedbreaker.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=free.feel-fly.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=www.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d
https://t.me/proxy?server=87.248.129.107&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=172.65.104.042&port=25565&secret=7hYDAQIAAQAB_AMDhuJMOt1iaXNjb3R0aS55ZWt0YW5ldC5jb20
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/IranProxyV2/9057" target="_blank">📅 02:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9056">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
پروکسی
✅
tg://proxy?server=5.78.53.137&port=8443&secret=dd104462821249bd7ac519130220c25d09
tg://proxy?server=5.78.57.102&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/IranProxyV2/9056" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9055">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=rec.nolags.pw&port=443&secret=dd0603553657b3f54b6bff0d3759e8db1d
https://t.me/proxy?server=5.78.59.193&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=office.proxytg.live&port=443&secret=eed604acbe90be65ddf34629f1e2234f7d6f66666963652e70726f787974672e6c697665
https://t.me/proxy?server=feed.proxytg.live&port=443&secret=ee7c1dc73472aff6b273c603d9713900d1666565642e70726f787974672e6c697665
https://t.me/proxy?server=87.248.129.222&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/IranProxyV2/9055" target="_blank">📅 01:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9053">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پروکسی نت ملی میفرستم حتما ذخیره کنید داشته باشید
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/9053" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9052">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مث اینک این دفعه اوضاع واقعا خرابه، از اونطرف صدا و سیما میگ ما نزدیم، از اونطرف آمریکا میگ شما زدید پس باید ما بزنیم، فک کنم آمریکا میخواد شروع دوباره جنگو این دفعه بنداز گردن ایران
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/IranProxyV2/9052" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9051">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پروکسی فول متصل،ذخیره کنید
✅
tg://proxy?server=5.78.48.55&port=8443&secret=dd104462821249bd7ac519130220c25d09
tg://proxy?server=95.216.42.228&port=4455&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/9051" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9050">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
تیتر شبکه خبر :
حملات موشکی سپاه ایران بزودی...
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/IranProxyV2/9050" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9049">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
بیانیه جدید سپاه : حمله شرورانه آمریکا را بی جواب نخواهیم گذاشت
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/IranProxyV2/9049" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9048">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به لبنان که حمله نشده جمهوری اسلامی بهش بر بخوره؛ خاک ایرانه دیگه، مگه مهمه براشون؟
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/IranProxyV2/9048" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9047">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حالا پاسخ ایران چه خواهد بود؟
🦦
بزن پایگاه هاشو تو منطق بگا بده مشتی
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/IranProxyV2/9047" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9046">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
سنتکام اعلام کرد که حملاتی را در قالب دفاع از خود علیه ایران آغاز کرده است؛ این اقدام در پاسخ به سرنگونی یک بالگرد آپاچی آمریکایی در روز گذشته صورت گرفت. این مأموریت، پاسخی متناسب به تجاوزات غیرموجه ایران است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/IranProxyV2/9046" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9045">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
صدای انفجار در بندرعباس
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/IranProxyV2/9045" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9044">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usdaTnYSc5EHnpvcyId0KwjFboKbRI8eMiR9vL4g-Lbz2Gxh0DZzeoRcsnEmmG-FQkoFCjcWnmy2qTJnubCk6xNUiOVAJDR9u_0qfnaP25xB6tHh63gR9thEq080Drtn5llmBqEI_G_S6iDfCvmMV4lfHKQrAOq_8kklQadoDKrTV4eAUej2lNEnnMYAEf2GSdwf6wP04dITUCFP-kouooXRq24LjkDr-GGUWRIe8n7ITLGNFmV6ZHiJc7iqtoHz1Ryo0tvxZ3ut4EqN-6pXc3IdWEYjv6TSOx0EMK8UmvfJv9Eq_l_jqWTh3TyL5zakcEAutU4QPmZPXsm88IC-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/IranProxyV2/9044" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9043">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCrlFJmeWff-GGLKbBL_zgSpQkWP_lhqmfkQFhJ7NWkZ1EtHFwf35aEaaaiScpzHo7mfM0S6BqwzAGQO9feqrmU4Q2G2_Y5aBeCLnJ9JG5HdwtwkAy4Iw7bQJwJxn75Aq2dFEqOaU7EDhu7UrenFlzu0vLsu93onW1GV9dqlLtUVTV-tx94TCNtKfLGGb2MrBRsiyRoclAhoPUnDnnIxGvmwDkCGY9IFc_AV5q0yI_Bdd9Xyfyx2YdMfSwMm23qz3shjQ7_RZEmDpF5N9RjMfR6LePivZhA70fTjTuqambYyJohA91NjCyn42hGe9U67KokRw44EIHTrtf9LbRKU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تونل کردن ترافیک ایران به سمت کشورهایی نظیر اذربایجان برای باز کردن سایتهای تحریم شده مثل ChatGPT و Claude بدون نیاز به VPN، باعث شده که ظرف مدت چند ماهه بعد از عملی شدن قرارداد انتقال ترافیک، رتبه کشور اذربایجان در نرخ سرانه تعداد پیامهای ارسال شده به ChatGPT از رتبه 44 در اوایل سال 2025، به رتبه 6 در اوایل سال 2026 صعود کنه!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/IranProxyV2/9043" target="_blank">📅 20:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9042">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=5.161.143.78&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/IranProxyV2/9042" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9041">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
بیانیه رسمی فیفا :
دیدار ایران و مصر دیدار افتخار همجنسگرایان رنگین کمونی خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد. کاپیتان هر دو تیم الزامی هست که بازوبند رنگین کمونی  ببندن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/IranProxyV2/9041" target="_blank">📅 18:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9040">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQZlMbIzo1r8LL5OXKcGbiyDTJgrgAhZNIC4-Xmw5PTOwDLDFGU5cLSqyT1-O7fb2NUwVYKwEr5IExufSYMuivIIjaV9XnnlX8QJH8xvIFLy_Pmca2abruw_dJCxNlRGPUrvRPOp-6ghKjxhhxEtZ12Upm2PB_IuuzJvPhXLYfsapMb8tIawHoMmmLsfRTKVvKlqTo2jjrL81VSIMDt0muB0DKggo0EQ_biaeDsTc3H0mpX2Eyx8NbIwg219W2jCcngUoejbBmuDst5u1wNXHDv5IJ_JtIYZ-mnvLxlSM6adfWV9bamxg6hvSlwY3E_9ZcSMFWylCeUgEs5sr49CYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/IranProxyV2/9040" target="_blank">📅 17:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9039">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://d4eb1900-6515-494e-85c5-306bb9594f56@45.130.125.194:8443?mode=auto&path=%2F%3Fed%3D2053&security=tls&alpn=h3%2Ch2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A1000000%2C%22scMaxConcurrentPosts%22%3A100%2C%22scMinPostsIntervalMs%22%3A30%2C%22xPaddingBytes%22%3A%22100-1000%22%2C%22noGRPCHeader%22%3Afalse%7D&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=vo.new-persian-song.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/IranProxyV2/9039" target="_blank">📅 17:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9038">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://10a6b923-e349-4594-92bb-d81a6245aaec@172.67.74.10:443?path=%2Fdownload.php&security=tls&encryption=none&insecure=0&host=sertraline.adaspoloandco.com&fp=chrome&type=ws&allowInsecure=0&sni=sertraline.adaspoloandco.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/IranProxyV2/9038" target="_blank">📅 17:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9037">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=135.125.216.18&port=8080&secret=dd112760f4d4ccf54d5c3bc40a6776c73b
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/IranProxyV2/9037" target="_blank">📅 13:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9036">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرعتی🔥🚀.npvt</div>
  <div class="tg-doc-extra">2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9036" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🆕
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/IranProxyV2/9036" target="_blank">📅 13:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9035">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">📱
یوتیوب رفع فیلتر می‌شه.
📔
مصطفی پوردهقان، نماینده مجلس:
وزیر ارتباطات در کمیسیون قول دادن که فضا رو به شرایط عادی برگردونن و بعد از رفع فیلتر واتساپ، رفع فیلتر یوتیوب هم در دستور کار بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/IranProxyV2/9035" target="_blank">📅 13:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9034">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zkr4lv0LtOHbPTqoVF9je_8yBfL7Yy9BZY3scR6-j_4e-7NxlqpJoQZ3or8ilDGOlGpXWkUxBTBS11u1lg26PtsfOfoZxcFap1IEYm9ENQYUM9PZJg5VZbBabYo8R3mGv2CVGXnhPl4wNcdWuduHL1-W53vt3IM5IBdYbpu0QxjCXXSMcVq9FMbVoAl8LXWDQ9Z95PuGqe7VZTjD_oM2spwCut5AylKmS5_JTTkMlcGeyG591LK4Rv8cgi54gGb0sK8iC_IV4X1wxVnwrE5zC0cTB0nLrJ1V7SptEJY4XQgOclH_1Oqmpb6r9WohDOKECmewHfbEqepsLhzFHzIR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش به ربات مراجعه…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/IranProxyV2/9034" target="_blank">📅 22:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9033">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqyFb2c-I79RI0HJLtMdcsso9Yd90E8yNTB7yeOqD25PsJSVJy4v1dE5oF8aGkoMP7hjumZnw-NpWU49xcKqv2EisBoxjagQYS2vM0kdWuUL8AoVfGRT5RO0RGyDp8_3gino8zx0o4RbrTYNjr458JfFiDIC7-4r66vDqDsrZPuVvvjx8xm7d9i-LCwpMNKRbzKbcGspI7d-Oj0Zo0A8wY3YvzI4gxuWfb-Uq0vxiS_CNVzrTIH8ofHWn8qUeTI3A1uoF4jBRrWS5bbmmMMupNvBvdb9ez7e806fYl44QBFuNCkL4c44E_PsfVIDBvnFH5Qdy1f7mkt0RLb358nI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/IranProxyV2/9033" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9032">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=178.105.226.182&port=443&secret=ee396219a1e9b2aebf6f245a1495777811706c61792e676f6f676c652e636f6d
https://t.me/proxy?server=orbit.proxyonline.online&port=443&secret=eea49899bfb9f5b061d6213e6f6480ea006f726269742e70726f78796f6e6c696e652e6f6e6c696e65
https://t.me/proxy?server=94.183.221.165&port=443&secret=a252e3eb41417da5e2332193f25bcf34
https://t.me/proxy?server=relay.proxyb.site&port=443&secret=eeee9dfed6b3721e5b2788f5100af2ff4272656c61792e70726f7879622e73697465
https://t.me/proxy?server=5.75.200.229&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/IranProxyV2/9032" target="_blank">📅 15:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9031">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
مث اینکه جنگ فعلا به پایان رسیده، هردرطرف از موضع خود کوتاه اومدن ولی البته یه نکته بهتون عرض کنم که این شرایط فقط تا پایان جام جهانی فک میکنم آتش بس برقرار باشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/IranProxyV2/9031" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9030">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:   نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/IranProxyV2/9030" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9029">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/IranProxyV2/9029" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9027">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=fresh.nolags.pw&port=443&secret=dd691fa48fcc661b68fe4f5200c5b174f9
https://t.me/proxy?server=91.217.166.212&port=16&secret=dd1603010200010001fc030386e24c3add
https://t.me/proxy?server=fool.feel-fly.info&port=25565&secret=7hYDAQIAAQAB_AMDhuJMOt1iaXNjb3R0aS55ZWt0YW5ldC5jb20
https://t.me/proxy?server=91.217.166.22&port=20&secret=dd1603010200010001fc030386e24c3add
https://t.me/proxy?server=91.217.166.21&port=20&secret=dd1603010200010001fc030386e24c3add
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/IranProxyV2/9027" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9026">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/IranProxyV2/9026" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9025">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
دوستان احتمال داره دوباره اینترنت بین‌الملل با محدودیت یا قطعی روبه‌رو بشه.
✅
از همین الان برنامه‌هاتون رو آپدیت کنید و این اپ‌ها رو نصب داشته باشید:
• Happ
• NPV Tunnel
• V2RayNG
• Psiphon
• ShiroKhorshid
• Http Injector
• NetMod
⚠️
قبل از هر محدودیتی، آماده باشید
💙
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/IranProxyV2/9025" target="_blank">📅 13:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9024">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6QqpWO1HeK0Q2l8olq6TKVaIcv-OvBmqh0I8-KXehRThWueC0at03ghlGtQk3T5qDQnNeoQ_6Xc7b2r_-R2124Lq2ruEyrldz35hjGn0crbXqDqwAjn2GYl36drSEovlnrOZfLrfuS1w-DjOV8HmYT6uXv0y97-5UlAgTA-hyeolCwM4JMOPmEvETd2rF1u_OmFFOBzs2W30E48OXnDSD94I3CmntBpShNIo_dRs_Qjk2px5xyNGeE-Z0iToopNltbI15RF4QW0WhdGn7qPUuKaeRW2L_45FTkOnFLCexKO8NxYuXhM3Gt1w7zcmy94nKOj5IQYJzaUZAM12Sftug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دوستانی که سرورا براشون متصله نمیشه، ۵ پورت و ۵ لوکیشن جدید اضافه کردیم، لینک سابتونو بردارین، حتما دامنه جدید رو از قسمتی که نوشته
info.russiaproxyy.shop
به این دامنه جدیدی که براتون قرار دادم
⬅️
doc.midnightfits.com
➡️
تغییر بدید و وارد ساب لینکتون بشید سرور جدید رو بردارین
🔹
نمونه ساب لینک جدید
https://doc.midnightfits.com:2096/reza/xxxxxxxxxxxxx
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/IranProxyV2/9024" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9023">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=s3.mowork.twc1.net&port=443&secret=ee90872f20ccc37e3aa2681602f51df71273332e6d6f776f726b2e747763312e6e6574
https://t.me/proxy?server=s4.mowork.twc1.net&port=443&secret=ee3e9cfe9af4494731b9a566075ee8c3bc73342e6d6f776f726b2e747763312e6e6574
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/9023" target="_blank">📅 13:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9022">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
vless://a78bf929-6883-48af-902d-7737793eeb17@hu02.sonicsonic.icu:443?security=reality&encryption=none&pbk=z-TKWOWgZLfzQ-wNdwXQqVwaUgCmbchM2Xtrk1NGynU&headerType=none&fp=qq&spx=%2F&type=tcp&flow=xtls-rprx-vision&sni=hu02.sonicsonic.icu#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/9022" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9020">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پروکسی مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=imtproxy.ir.imtproxy-ir.info..&port=443&secret=ee16550001232d00bb5190728b72644171706c61792e676f6f676c652e636f6d
https://t.me/proxy?server=65.108.154.5&port=443&secret=eecdf95381f978fb348f233a14b2251e6d7777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=91.107.148.135&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=5.75.206.125&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=91.107.167.170&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/IranProxyV2/9020" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9019">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پروکسی مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=91.107.156.186&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=153.80.241.214&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=51.254.130.47&port=8443&secret=a84102e409230c3b69dd4f68cef86baf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/9019" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9017">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
براتون پروکسی نت ملی و اوپن و... میزارم، حتما ذخیره کنید و برای دوستاتون بفرستید درصورت قطعی اینترنت استفاده کنید تا بتونید، حداقل کانکشن رو به تلگرام داشته باشین
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/9017" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9016">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری-آکسیوس به نقل از رادیو ارتش اسرائیل اعلام کرد که ارتش خود را برای چندین روز درگیری در ایران و احتمال بازگشت به یک نبرد طولانی‌مدت آماده می‌کند.
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/IranProxyV2/9016" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9015">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
دفتر نتانیاهو:
در پاسخ به شلیک موشک از سوی جمهوری اسلامی، اهدافی در داخل ایران رو هدف قرار دادیم. اسرائیل همچنین در بالاترین سطح آماده‌باش دفاعی و تهاجمی قرار داره.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/9015" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9014">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
فوری/نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد  بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
✅
با ما اخبار جنگی بروز باشید  @russiamilitery</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/IranProxyV2/9014" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9013">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پروکسی | فیلترشکن | کانفیگ v2:
🚨
فوری
⚠️
👑
نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد
بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
پروکسی نت ملی:
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/IranProxyV2/9013" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9010">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
ارتش اسرائیل:
در ۲۴ ساعت گذشته بیش از ۹۰ هدف متعلق به حزب‌الله، از جمله انبارهای تسلیحات، مراکز فرماندهی و سکوهای پرتاب موشک در لبنان رو هدف قرار دادیم. این حملات با هدف از بین بردن تهدیدات علیه شهروندان و نیروهای اسرائیلی انجام شده.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/IranProxyV2/9010" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9009">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
لشکر10 سیدالشهداء سپاه کرج مورد حمله اسرائیل قرار گرفت
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/IranProxyV2/9009" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9008">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🆕
خبرگزاری فارس:
در صورت ادامه حملات به تاسیسات انرژی و زیرساخت های ما؛ کل زیرساخت های منطقه رو میزنیم.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/IranProxyV2/9008" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9007">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
مهر: شنیده شدن صدای انفجار در جنوب تهران
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/IranProxyV2/9007" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9006">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
رفقا جنگ جنگه مراقب باشید از یک سری مراکز نظامی فاصله بگیرید ،امیدوارم تموم بشه این جنگ و همه مردم ایران سلامت باشن
❤️
💎
پروکسیارو ذخیره داشته باشید حتما
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/9006" target="_blank">📅 12:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9005">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9i1OzLZJtwGcdOyqRfUSvYlUskmGg7jqSLkBRi2LEWkSLmcEjCSoduP4WC-3VkXlvs2JTQpsjoUoGaTXaq72Av57a875b6ggv0G9Hzrq9tT67462qD6bvmlUt-8azr-pV2EdteCHxyJPSYiRH7OddgyAHIlgrLuJVpsBJLhHActQW5zBdyN6MMjaPD0Z0X5O9abN1PPFJjRAgsg2QPsLkL9_eP87rojnU3Y5rxa0iLZmQFzhjOj6x3WJY8uLI6HcwbnNlgyfDYwQ4P5F_RYA695a5_x4DUpzQ0z79qsg03LsFu9tIqPS7QuxRyNyDZPWLrwMI1O7GolK_r77kzu2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون تهران
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/9005" target="_blank">📅 12:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9004">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5d-ovwYVaHxUENpK6eZCkFJhfqKr0af-KcHtf1DHPh31M_G_nIKohldHkHFL4OClNuHOon4tLZX6y1wp2qMf26BTjOnNXfaAHuDiNWouNqTfCeuLiab3J_ehsRgEcmXg0iTzHcenleyolaJiBduQ1B58kM_COD-7qI3Z5PhwbOE1Z5NgakX5Ob3fkGYw07puHQVJjOOITozQ7zj784msRhawZ5yRcNO6hvPgf3XHkyNPX3AFaKYuBdneG9bQ8oA2Bw5vinUopgjfTCLadAnyxcynT0arWYHsHmA9Hc_s6avxM1zWsJRS4DZv2KhVWVJc4w07TCfGQynQ9JKvF0QKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تهران، شمس آباد:
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/IranProxyV2/9004" target="_blank">📅 12:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9003">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
حمله اسرائیل به فرودگاه شیراز
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/9003" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9002">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
لشکر 8 زرهی اصفهان مورد حمله قرار گرفت
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/9002" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9001">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
❗️
دانشگاه عاشورا هوافضای سپاه مورد هدف قرار گرفت.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/IranProxyV2/9001" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9000">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
❗️
وزیر جنگ اسرائیل: شروع کردیم.
Proxy
|
Proxy
|
Proxy
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/IranProxyV2/9000" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8999">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🆕
ایرنا : انفجار در استان همدان
پروکسی نت ملی:
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/IranProxyV2/8999" target="_blank">📅 11:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8998">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
تو اکثر نقاط تهران، پدافندا درگیرن.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/IranProxyV2/8998" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8997">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
تو اکثر نقاط تهران، پدافندا درگیرن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/IranProxyV2/8997" target="_blank">📅 11:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8996">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
بنا بر گزارشات دیتاسنتر آسیاتک قطع شده و به دیتاسنترها جهت قطعی اینترنت آماده‌باش دادند.
در صورت تبادل آتش بیشتر قطعی اینترنت بعید نیست.
اگر فایل یا اطلاعاتی به صورت آنلاین دارید بهتر است همین الان آن را دانلود کنید و تنظیمات حذف حساب‌های کاربری به حداکثر زمان تنظیم کنید. راهی برای وصل شدن خود حتماً داشته باشید.
چنل مارو حتما دنبال کنید، ما هر راهی که برای اتصال مجدد پیدا کنیم حتما حتما براتون قرار میدیم درسریعترین زمان ممکن
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/IranProxyV2/8996" target="_blank">📅 11:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8995">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری-صدای انفجار در اصفهان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/IranProxyV2/8995" target="_blank">📅 11:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8994">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در اسلامشهر و ملارد و کهریزک و باقرشهر
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/8994" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8993">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در غرب و جنوب تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8993" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8992">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4t8xMV26VUmbInjaeayZWDvICiFruAVg8V7hxhAReUjATbrp-XdaEM-LH9z-tNBlJr2iz2NPYsMVSjKplttS68Gwe47lWhiZayGX3wtqEeortRTz6xEiYsX-FenH96XD94taM0-mRopWmktP2621lYzvqkNhrjbgPfeSoHXJdWjbXxxn9t7JK5lfJ3soB_YW6uTIwrkkPOAUjrvuzmwqG6FZBW8835JTMdRtPPgDQZJ-wY1U_yIVrFd60DRrdPqYR2ihwmgkIGl0_GCCthV1gKhKhLT4hCveFyZ4b4oIxfnDac_yqVLQiNXMRX3-WUdcN_QfGnDQYsEqDnZX8hFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وضعیت آسمان اصفهان:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/IranProxyV2/8992" target="_blank">📅 11:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8990">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سپاه: حمله دشمن به صنایع پتروشیمی پاسخ داده شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8990" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8989">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=DXoutAStxYfLU9SuwVxcQCiEAzn6xCSdUoq6fURcb751bJFjsrToUh56SvaTEcjcjbYkbaKD5Om5F_mcezpSwcoJQOTgWmQjKP41jExEXiiK372ifKxUtSunRJEqPh8-qDAZpSc1mnwtgC2zKXTIVYfPs0wlTzEYSPHO0Ep6uKPVUWSOrN-KCUPD34zjXZCQ618xIdNUw-noi5T--_FE8lVopVnCGFjH1uJdELLgqKLVeD4A84u4etdYuhwNcbWCucfsvi2LgJsgb18xqD5B_BlLCuNqo4RF1AWDvQpBm2H5q266A2gTGnoGCtuhNmMg6XlRSm4jn7Z7EhvE49Mr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=DXoutAStxYfLU9SuwVxcQCiEAzn6xCSdUoq6fURcb751bJFjsrToUh56SvaTEcjcjbYkbaKD5Om5F_mcezpSwcoJQOTgWmQjKP41jExEXiiK372ifKxUtSunRJEqPh8-qDAZpSc1mnwtgC2zKXTIVYfPs0wlTzEYSPHO0Ep6uKPVUWSOrN-KCUPD34zjXZCQ618xIdNUw-noi5T--_FE8lVopVnCGFjH1uJdELLgqKLVeD4A84u4etdYuhwNcbWCucfsvi2LgJsgb18xqD5B_BlLCuNqo4RF1AWDvQpBm2H5q266A2gTGnoGCtuhNmMg6XlRSm4jn7Z7EhvE49Mr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم‌های اضافی از موشک بالستیک ایرانی که در نزدیکی یک شهرک اسرائیلی در کرانه باختری اشغالی اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/8989" target="_blank">📅 11:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8988">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=kAM9tQbmUFfyXoDUuB2rXiNfrLaL65elf-c0sucfltURzHj2F9vNDsH1RmP6FW_63oJocbloV2XJRRXBvFCpqYNAaJMYP9g3RYK7u8UpBFmBwJfMaYPCVd-wQ-f1_wudlGQf4StB2XP2sL5jtDtuwQWZZguP2xZoucIv3D5LdmcLeP-3UohK2yQ0W7LZ5SbKbsr2dLku3XganbPLAmyUW_eotACyVBwhjbYW6XB_OtYdj8wdqQmMQBTDQINCYKsT_V_jx698bmL43aWh82pvV-Tkzh9orfR_J2EhC1inZT7bfLPSbkTJQ5pa7YpoRDrpvo6YaJpiLmhG-eFrkrwLnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=kAM9tQbmUFfyXoDUuB2rXiNfrLaL65elf-c0sucfltURzHj2F9vNDsH1RmP6FW_63oJocbloV2XJRRXBvFCpqYNAaJMYP9g3RYK7u8UpBFmBwJfMaYPCVd-wQ-f1_wudlGQf4StB2XP2sL5jtDtuwQWZZguP2xZoucIv3D5LdmcLeP-3UohK2yQ0W7LZ5SbKbsr2dLku3XganbPLAmyUW_eotACyVBwhjbYW6XB_OtYdj8wdqQmMQBTDQINCYKsT_V_jx698bmL43aWh82pvV-Tkzh9orfR_J2EhC1inZT7bfLPSbkTJQ5pa7YpoRDrpvo6YaJpiLmhG-eFrkrwLnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از تأسیسات پتروشیمی هدف قرار گرفته در ماهشهر، جنوب ایران.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/IranProxyV2/8988" target="_blank">📅 11:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8987">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
رسانه‌های اسرائیل:
پس از شلیک یک موج موشکی از ایران، صدای انفجار در منطقه مرکزی و تل آویو شنیده شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/8987" target="_blank">📅 10:46 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
