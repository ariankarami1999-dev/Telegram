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
<img src="https://cdn1.telesco.pe/file/Si5EgvsSuedudnmrZAHz5Pdz3Mjl-ZA9KmM6jSqkB_106XIPJX0G89o5DY96GBsNk5GY9NHzMOVQzdyw4uGbqhCx7s48F2wncPM9nvm6EsJU4wEOQEYq_VoH453PnElv9sfcyjI49oEGtL7_5ZMJW9Joy7PBwXT5w46koEN_H3YWb0mt6FcA2Vx2fL9lXyeWDcYpt9I4hRlJDzYIziQETI8S6XbQbgjjLzK00bPn3wXDk6Ij8xlF_U8EcKX3FnbppCPRARYnG1sCvstzwxS1uUn4OnCa_P9F29pUMBhBYb3Q6rFQVCRUE4af7VPILgFfT-x_u0hkq3pwJ_2UL8lMig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 115K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 23:28:14</div>
<hr>

<div class="tg-post" id="msg-3094">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دست از سرم بردار فیلترچی</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/3094" target="_blank">📅 17:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3093">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گویا یک سری دوستان با تغییر LTE(4g) توی تنظیمات شبکه گوشی به 3g تونستن راحتتر کانکت بشن به شیر و خورشید.</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3093" target="_blank">📅 17:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3092">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/3092" target="_blank">📅 16:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3091">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qMPi8ehrU1lIi2AHsE8vKwi4jHl2PQJJ3qWh0cbTKunPob_XxwxAWGMW_zjQllVN5iXa0GVm9vD4pi1FtqEL0eL5sHXBZTAEKnlezREpppxNrZwg4HO0NWuelp2o0NT4-kY-qKMI6KbQhmOQodMKESLLTnrF5QRoiV-i-75NLkofOo_DxHsipyFu0Zb7uNUgY5G-go5QrsPvwj4kfjZ43Vq6LPUQdKVvBbvEsdtaoCfWc6oRYyWP6enY0DZQduTCDKv-7DByZ-M5th8shTH8cwGPWII6kuN4fUt0ANVHYy0CGd4hLnux65hdeUoSH9ZHiplChOZewBzFqw4iUh4f4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست رو یکی از بچه‌های توییتر واسم فرستاد و گفتش که از دیشب(و تا الان) روی ایرانسل با یه کلیک وصل میشه روی شیر و خورشید. اگر کانکت نشد، مجدد عرض میکنم که بذارید هواپیما و بردارید، آیپی جدید بگیره: 184.24.77.42, 184.24.77.32, 184.24.77.5, 184.24.77.7, 184.24.77.16…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/3091" target="_blank">📅 13:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3090">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3090" target="_blank">📅 12:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3089">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این لیست رو یکی از بچه‌های توییتر واسم فرستاد و گفتش که از دیشب(و تا الان) روی ایرانسل با یه کلیک وصل میشه روی شیر و خورشید. اگر کانکت نشد، مجدد عرض میکنم که بذارید هواپیما و بردارید، آیپی جدید بگیره:
184.24.77.42
,
184.24.77.32
,
184.24.77.5
,
184.24.77.7
,
184.24.77.16
,
184.24.77.36
,
184.24.77.21
,
184.24.77.11
,
185.200.232.49
,
185.200.232.50
,
185.200.232.42
,
185.200.232.41
,
23.48.23.186
,
23.48.23.133
,
23.48.23.195
,
23.48.23.178
,
184.24.77.29
,
2.22.21.152
,
95.101.23.82
,
23.215.0.164
,
23.197.161.35
,
184.28.230.87
,
23.220.128.221
,
96.17.207.142
,
23.50.131.18
,
23.36.162.209
,
23.219.3.212
,
23.223.245.150
,
96.16.122.59
,
23.2.13.138
,
23.2.13.144
,
96.17.207.135
,
23.220.113.51
,
96.17.72.41
,
23.203.185.105
,
2.16.27.71
,
2.16.244.11
,
2.17.147.89
,
2.17.251.98
,
2.18.190.26
,
2.18.190.27
,
2.19.10.30
,
2.19.196.105
,
2.20.255.113
,
2.21.89.66
,
2.21.239.10
,
2.21.239.21
,
2.21.239.23
,
2.21.239.29
,
2.22.6.68
,
2.23.176.166
,</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3089" target="_blank">📅 12:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3088">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aK670Jd0TKfpMtOf-kuBBw2mZlMJHK-PIkYLmDIeCR3vrIyT-ac20fxA-xWH_8ShFjV02J1ZTd-1i6aDJ-yILj-eScrDcAOQD0qkOcAUwDAzxSkql5hLSzyLATCofS8n4AINSgC7RXeJ4t_Wuxhjva3EewYSxT4fF4C56orIXU5XfnvN9d89y_lOWi9fsf0iDr7EOdQ24jRU9v-GiFxecNeMR4z6PcBvaiUOKYk_u2wOTLF75MWkLRLaCFVpwSn9050Hjnh92dJ0mkaNQIvgUSjBf6-ne5M-QLP_58gj6P0qaCUoPOUXSoukEWEuXc3Eyo7mGX3YePzxfbJW12VPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر راس گلر
:
روی ایرانسل تست شدن، مناسب CDN شیروخورشید.
23.65.119.52
23.73.2.141
104.110.138.190
104.83.5.202
92.122.166.236
92.122.166.234
92.122.166.237
96.16.122.70
23.67.136.200
23.67.136.202
همینجوری paste کنید اوکیه نیازی به کاما(,) نیست</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/3088" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3087">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QZc-IET8eC6fs_LrDKO9sqD-cJqVKQ3BwuSKrX2UDFfOOuj3km42Rp1Hu8BShOsGYscFHEjB2TwKwqXruJ98Ekoh_NygrjnFnfV0QSls-z8VxYxVAbbh2KyKdD1cBaYJr-zHoPmHnBcQCgSmSVZuKTEEGAxqN8Arw0XuSRIOcD9ePuwflqLUOuJOzSmlrXS_BY9nyozswlsTcIAZlZ6lMf9KP1CneVdh_gmBwt5nbXaeAgmcVIqueOxpz3ETbWxXSaJig5OIf9NsYKV73C6LhER_E0mzxNBzZpvax-pHP0AbnFn0N5NKIecZ3PNr0HTPSjaUd19G0P28r7XSuvwgww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود اپلیکیشن‌های اندروید از گوگل پلی با اینترنت داخلی
از طریق این پروژه، میتونید ربات تلگرامی‌ای رو ران کنید که به راحتی لینک گوگل پلی شما رو تبدیل به لینک داخلی میکنه:
https://github.com/ZethRise/PlayDL
این هم نمونه ربات پیاده‌سازی شده:
https://t.me/APKNitoBot
✉️
@MatinSenPaii</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3087" target="_blank">📅 10:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3086">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه 1.0.3
یک آپدیت متمرکز بر پایداری است. در این نسخه پایداری اتصال بهتر شده، مپ شدن تنظیمات Advanced اصلاح شده، تفاوت بین SOCKS5 و System Proxy شفاف‌تر شده، و احتمال حالتی که برنامه Connected باشد ولی سایت‌ها باز نشوند کمتر شده است.
WhiteDns Windows v1.0.3
- راهنمای سریع تست
لطفا برای تست اول این تنظیمات را استفاده کنید:
1. برنامه را باز کنید.
2. وارد بخش Connect شوید.
3. گزینه Proxy Mode را روی System proxy بگذارید.
4. وارد بخش Advanced شوید.
5. گزینه Transport preset را روی Balanced بگذارید.
6. این موارد را بررسی کنید:
- Compression = off
- Base64-encode data = Off
- DNS listener enabled = Off
- SOCKS5 authentication = Off
- Packet duplication = 0
7. در صورت نیاز ذخیره کنید و سپس Connect بزنید.
اگر سایت ها ناپایدار بودند یا باز نشدند:
- فقط همین یک مورد را تغییر دهید:
- Transport preset = Stable Iran
لطفا این موارد را گزارش کنید:
- آیا اتصال با موفقیت انجام شد؟
- آیا یوتیوب و سایت های عادی باز شدند؟
- از چه Proxy Mode استفاده کردید؟
- سرعت مرور مناسب بود یا نه؟
- آیا برنامه یا سایتی بود که با وجود Connected بودن کار نکند؟
@whitedns</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/3086" target="_blank">📅 08:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3085">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینها رو یکی از بچه‌های توییتر جمع‌آوری کرده و منم واسه‌ی شما می‌ذارم. آیپی برای شیر و خورشیده، بخش sni رو خالی بذارید. خیلیا تونسته بودن وصل بشن باهاشون: 2.16.27.71 2.16.244.11 2.17.147.89 2.17.251.98 2.18.190.26 2.18.190.27 2.19.10.30 2.19.196.105 2.20.255.113…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3085" target="_blank">📅 08:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3084">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اینها رو
یکی از بچه‌های توییتر
جمع‌آوری کرده و منم واسه‌ی شما می‌ذارم.
آیپی برای شیر و خورشیده،
بخش sni رو خالی بذارید.
خیلیا تونسته بودن وصل بشن باهاشون:
2.16.27.71
2.16.244.11
2.17.147.89
2.17.251.98
2.18.190.26
2.18.190.27
2.19.10.30
2.19.196.105
2.20.255.113
2.21.89.66
2.21.239.10
2.21.239.21
2.21.239.23
2.21.239.29
2.22.6.68
2.22.21.152
2.23.176.166
23.2.13.138
23.2.13.144
185.200.232.50
23.2.13.152
23.2.13.153
23.2.13.186
23.2.13.201
23.2.13.227
23.33.126.163
23.36.162.196
23.36.162.198
23.36.162.202
23.36.162.208
23.36.162.209
23.36.162.215
23.37.197.128
23.37.206.186
23.38.49.97
23.39.249.249
23.40.63.69
23.41.37.129
23.44.10.10
23.58.222.147
23.59.235.208
23.60.69.118
23.65.119.52
23.67.136.200
23.67.136.202
23.72.248.214
23.73.2.141
23.73.2.148
23.73.2.161
23.73.207.11
23.73.207.16
23.79.20.249
23.79.48.162
23.192.46.51
23.192.237.208
23.192.237.209
23.192.237.222
23.197.161.35
23.200.143.71
80.67.82.179
88.221.92.177
88.221.132.162
88.221.168.5
88.221.168.138
88.221.213.81
92.122.73.138
92.122.166.141
92.122.166.146
92.122.166.175
92.122.166.182
92.122.166.197
92.122.166.234
92.122.166.236
92.122.166.237
92.123.102.104
92.123.104.7
92.123.104.67
92.123.112.7
92.123.189.41
92.123.189.82
95.100.69.108
95.100.156.147
95.101.23.25
95.101.23.27
95.101.23.82
95.101.23.168
95.101.23.170
95.101.29.12
95.101.29.30
95.101.29.54
95.101.35.73
95.101.35.83
95.101.181.125
95.101.200.63
96.7.218.219
96.16.122.48
96.16.122.55
96.16.122.59
104.83.5.65
104.83.5.82
104.83.5.201
104.83.5.202
104.83.5.203
104.83.5.208
104.83.5.216
104.83.15.66
104.94.100.73
104.96.143.134
104.103.64.7
104.103.90.156
104.109.128.153
104.109.250.232
104.110.138.190
104.110.191.57
104.111.202.158
104.117.76.26
104.117.76.40
184.24.77.32
184.24.77.36
184.24.77.42
184.25.52.200
184.28.230.87
184.51.252.4
184.51.252.36
184.51.252.38
184.51.252.135
184.51.252.152
184.51.252.157
184.86.251.12
184.86.251.27
185.200.232.41
185.200.232.42
185.200.232.49</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3084" target="_blank">📅 05:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3083">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نمیفهمم چرا هر متد جدیدی میاد و هر راه جدیدی باز میشه، یه لگد به گیتهابِ بدبخت می‌زنن
انگار فیلترچی می‌خواد ما رو تنبیه کنه
😂
داره میگه دفعه‌ی بعدی گوگل رو هم فیلتر میکنما، حواستون باشه این سری عصبانیم کردین</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3083" target="_blank">📅 04:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3082">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">طرف بله و روبیکا نصب کرده بعد میاد توییت میزنه که اپ شیر و خورشید(که اوپن سورسه همه کدهاش وسط گیت‌هابه) بو داره نصب نکنید امنیتش پایینه🫩
امنیت؟
با من شوخی میکنی؟</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/3082" target="_blank">📅 00:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3080">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uesmpPMz0sy8gaS61sqdyWb7CCcroMb_veoANmtp5b1ILIcyIk2-6bsw_jYdYsoxqHFjhDYzlrP0NB7Z_LUj9YSqHpqSy2oDQPBoqmCMXINS2A0lDaUKsMTdZd_5IC5uPujjIsZuXCZf-DhfJb11ggx0wNhQqgwGKFVhXHHjFiVij_y7EcbzJlPwDrRrgu9ECvaceT5okmFZcQwad1WgQ0xvtIk3silTZm9Fn4EIVet4se8AhuCuJmNbjorSJv38RS50hy9ziuQ5uLQFBGPX4esld9Lv5GJ7TU98oNOTXNNW2bSPxkFEot4v9rYXZacKXL318wj2tsBc3JD3D8WCsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62c2815606.mp4?token=P0nAWSLjCFcUmkO10zaDGb9wcbbBJM1NOirxEXoH4gtM9LqdNPS6YTS0bdDAbDNtWgQN86-oPuC5fwtYTJDWyD-UqB9q3UnZ_GOZ8MUfjoj6K7YZ4JAvtwI744UUChnSt66ylQYzKwGiH0fMHljqRlkbC3p-PMSMEldI-QSWOfjs5B1E9c3GIYMNvDbsL77yTrUOEFfoNOHY5YMNAV96Vfx6x4-0v3hHpe7uMQOMO5w6_P6kBDAXdeAmJz0hnfoF3GbCnAF_B-D0ZXGHYG_mhH5GLPUK3LZwZX5elXTQsqqPkCOafctzAj1heRvame7iaHJ10sii7eX-bD5ngWizOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62c2815606.mp4?token=P0nAWSLjCFcUmkO10zaDGb9wcbbBJM1NOirxEXoH4gtM9LqdNPS6YTS0bdDAbDNtWgQN86-oPuC5fwtYTJDWyD-UqB9q3UnZ_GOZ8MUfjoj6K7YZ4JAvtwI744UUChnSt66ylQYzKwGiH0fMHljqRlkbC3p-PMSMEldI-QSWOfjs5B1E9c3GIYMNvDbsL77yTrUOEFfoNOHY5YMNAV96Vfx6x4-0v3hHpe7uMQOMO5w6_P6kBDAXdeAmJz0hnfoF3GbCnAF_B-D0ZXGHYG_mhH5GLPUK3LZwZX5elXTQsqqPkCOafctzAj1heRvame7iaHJ10sii7eX-bD5ngWizOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چیه درست کردین
😂
😂</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3080" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3079">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبر خوب:
نسخه‌ی اولیه‌ی WhiteDNS برای IOS منتشر شد:
https://testflight.apple.com/join/GfUqXrFz</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3079" target="_blank">📅 00:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این آیپی‌ها رو موفق شدم از سرتاسر توییتر جمع‌آوری کنم برای شیر و خورشید، این بخش‌اش: https://t.me/MatinSenPaii/3070 کافیه که با کاما(,) پشت هم وارد کنین:  2.22.250.149 23.58.193.140 23.48.23.151 2.19.126.81 23.202.138.125 23.43.237.239 104.112.146.82 23.2.13.136…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/3078" target="_blank">📅 00:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3077">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این آیپی‌ها رو موفق شدم از سرتاسر توییتر جمع‌آوری کنم برای شیر و خورشید، این بخش‌اش:
https://t.me/MatinSenPaii/3070
کافیه که با کاما(,) پشت هم وارد کنین:
2.22.250.149
23.58.193.140
23.48.23.151
2.19.126.81
23.202.138.125
23.43.237.239
104.112.146.82
23.2.13.136
72.246.28.37
2.18.63.49
2.16.53.11
2.16.53.50
2.16.19.136
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
185.200.232.8
185.200.232.43
185.200.232.40
185.143.232.122
185.200.232.9
185.200.232.11
185.200.232.16
185.200.232.17
185.200.232.19
185.200.232.24
185.200.232.25
185.200.232.26
185.200.232.34
185.200.232.40
185.200.232.42</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/3077" target="_blank">📅 00:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دور زدن فیلترینگ با کانفیگ سرورلس با ترکیب nekobox و v2rayng</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/3076" target="_blank">📅 23:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DWKnuZ7jkZj1zm0mKgVjwGlLKi-7blaoivfNG7Ql7wX2U7ycTwup8FIuLYG-tO9nZMp1Tv5NxO5nBj8JRb0cQqAqF4dnvY3NrjBl5BJ4L0vR1m8vK_B5ILHl9qFRkScGwg6Gbqk53LNT5-cY4hoT9Wax5fPmrNr_1S5bvLPYCpiwrSthdN3pJRKGrVklqG38tty3InoAOKUSHAkIRYThZ-i2NXUPs7nPuk9SMwb3Uqfz-WyAcbffUFz2LBcyK8aCySPwzz__jn6qda5qOP-oTL3vtczl9tkVQP-55PoVMgmmZVc-wk7G_HySxRdmkMoggGNRAFFAZQRYo8w8M2aZ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kbDYb8a26l2iPBUfqCkVaQGhUqZoeo4jwMv0gxAr_R9MmhAhCf6SvxlgAhhwY8H-CV5khBe4PWqgFzcydHUNDtJoTqZttKIgKCMkKYtNQCNe7Q3_fNQr79o9Vhr6CYa-rni8CyA_6AsgMyYRr3K2Phkl7OWxLESOo7koT3ujmcjC5XnLi-dt09t_rxZ4Rrv2cEU6gBZdgTUE4LGoMgZwpZhCToFzn_vmN5PBC879Yj39Vl3_GKOtGkDfstWJJC6p61mPf51fDhy97Edv8t8hlk8uRh6hgnAeS4QuouayWXwoYvHmwlKhp7iyn77VWrnKZsibWuWtIWU1ttmJw3nSMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر با شیر و خورشید وصل می‌شید، گزینه‌ی Share proxy on network رو فعال کنید. سپس به یه WiFi وصل بشید و کانکت کنید VPN رو.
بعدش با هر دستگاه دیگه‌ای اگر این کانفیگ رو بزنید(با توجه به عدد و پورت خودتون تغییر بدید):
socks://Og==@192.168.1.147:46597#ShirOKhorshid-MatinSenPIi
و توی گوشی آیفون(با Streisand)، مک‌بوک(با V2Box)، و هر دستگاهی که کلاینت V2ray با پشتیبانی از Socks داره می‌تونید وصل بشید.</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/3074" target="_blank">📅 23:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bu0eo9ocjNo7xy15oVCVuS8Yhdyi52vATavl6p4mg6HLlWA3M8HCKalKyneri6wfdyKlwibG4O2rRlwQrApRlkVIGKhNqIPaK0KlQjWQ9odMKf4AyJWi6DB0AnQ_2VJy5iHGvvXI205hOiv8P_qFdaQ367__8TdFKQ1U9DpgjqZqw1TAZpNl_wIBVHcBE4dUbrNQISuyiXNX5GCh8kyRJfbFV9xJrMyYvKw0vKGt2Lh8lXkTzsc1fDo9Zgpiy3_UPA0_4pgZm4949THGorOlqO_yfs0Mq7_t3zodR9SWoWjhNPokJ2kpwvDAsVZCQsXYTH89OIgnksvkvwfgcM0hLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
‏این دوتا هنوز وایت لیست هستن، چک کنید ببینید میتونید باهاشون وصل بشید یا نه.
sophos . com >
185.200.232.27
,
185.200.232.16
> Akamai
www . mathworks . com >
2.23.169.12
> Akamai
برای mathworks حتما www بذارید.</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3071" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3070">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FohtnSqulARYveyiAZY9_Oi7JKl7-gDEr1BqosCgUcYqLtyT9to7bvo60HaHzpSicz8t83gwr8cDJgxEb1kaAA6AqjxFu1GNRMXbUuLo00MnltODbRMtypMLvqVJi-x7P9-ayrGyFV9xXSxKQxTycHH3GZ0MfN_wMH8cge2Z2EsZCFn4xZBW2PorDfmfPeiTH8d2WzU-htGW5KTwKnAVtHNXpjQDWI-IBlXpEpv5kAanA93fWxTPv_tpyfxTe-cDR39Fc3zdPP5hm4LY8mqCQ2a0dlIHzggbgTSrngtWyMGgaKnd3nKtzc0I5ppYqSQkFlVd_2nUu5agwA_MeGSQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان توییتر روی ایرانسل با این دوتا روی شیر و خورشید وصله کاملا اوکی:
CDN Edge IPs:
151.101.192.223
CDN SNI Hostname:
python.org
‎
توی همون قسمت More Options هستش</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3070" target="_blank">📅 17:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-MatinSenPai.npvt</div>
  <div class="tg-doc-extra">3.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3069" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرور رایگان</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3069" target="_blank">📅 17:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3068">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kRnomtE7fo_mZve81VHzZBGOoCFVP8glMesrWiAUPeaWM1FBgdaDkN8q49tE3CHup35jGxxSM-69gbFoVpkCRONioFYS8MkpM1U029bV3PrFrpk-HUTqzJIhVnZdDYsHZ8ILEzxd4RhbwjJlBJz0rWix1G9CQlzH6sCPGOX-UZ4AQspHE9lKWcEzV9GujTC3OYIfl7fEv9a4-_dhHkUo9ZBCIrFpKjiF-otkuM2Kfej3HG89WmPM5v0oCN9K8K4tu_ZatlmpkW_qtkT20qxH7x8qo11hXEfh9JQVFuh-oykvxyEzS330KKchQPqOBDmvXDXMZ_PGSc2Oz8L6DIWxoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود راحت‌تر پکیج‌های Dart و Flutter
وقتی "
pub.dev
" کند یا ناپایدار می‌شه، PubYar کمک می‌کنه پکیج‌ها سریع‌تر و مطمئن‌تر دانلود بشن.
پاب‌یار فقط یک mirror ساده نیست،
مسیرها و DNSهای مختلف رو بررسی می‌کنه و بهترین راه دانلود رو برای "flutter pub get" انتخاب می‌کنه.
مناسب توسعه‌دهنده‌های Flutter و Dart
PubYar.ir</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/MatinSenPaii/3068" target="_blank">📅 15:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3067">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گوگل من روی همراه اول یه بیست دقیقه‌ای بسته بود.
نمیدونم دارن چه گندی می‌زنن باز</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3067" target="_blank">📅 10:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3065">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hSyunhre7VNdcbGHoHmZDZ6XSn5r50gA43odxB9OgXSac6Tz-cCtEzI_QIgAKutEojo2rkMZaEl-PWetha8FvDnCoLRH4hDWdynRCqxlwwMVevbVrV61t6GuEGbOxu3Xv6vcK1yUnURT1ElvKQilmDmk3ja4RaYHwWYKfzFUcwnNWv3PPyJg0zravC-tdrDpCN1B_OjOdNn7aUfh-e7ZqqEr8B1Sb87rlSakJnzaVZ8EjMTtzQr_ig_sqUtzbXSTswA9_nSJs_BEncs0HTaotPX7Xw1S5LSdCpxp5GN-KaXtLZHEtefALp3v8rPsGlDSsOsU268EsEzEsvGX3whfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dIpFG1i11CPT9KkfrTMTIzlvAk8XmXUW4wnAQrGPVhlTpP1CO55fbskh4Z3PUMdJqOAWPSCtE0FwGwt5wJdkulU8kAyTpZifdiIiBbTUKjJu063Qe_Ge-_yAUrh5pnAI3a0YEgESNugIGkn2HYeISEaRWNOPYW3UJi7SZaRaVguFBTtrXG7c6ekizc7cdzyjMY7_l1Ec5E3CoADC3N4yyMXdhqjYjFNgGpQyuyBdADWUlrh8tHkMPrG3MH8ntCrrlqi_QuXYVoo34DN11jN2W29BmGDK0w3lDWjwJ_jTDfBuJVk-rg5rOyl7lFro2DsxT4Y-mjKCC9aO31DX3vnzMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرور رایگان</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3065" target="_blank">📅 08:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3064">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ورژن جدید White DNS با یه سرعتی ریزالور اسکن می‌کنه که آدم باورش نمیشه</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3064" target="_blank">📅 07:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
آموزش خیلی مقدماتی و ساده برای استفاده از این نسخه
@whitedns</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3063" target="_blank">📅 06:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3062">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">masscan.rar</div>
  <div class="tg-doc-extra">1002.7 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3062" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینم نسخه gui مس اسکن خیلی کار کردن باهاش راحت تره
قبل شروع اسکن باید winpcap-4.13.exe نصب بشه روی سیستم(سرچ و دانلود کنید از گوگل)</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/3062" target="_blank">📅 01:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3061">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.txt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3061" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر بسیار پرسرعت Masscan برای اسکن آیپی‌های Akamai:
یکی از دوستان این رو نوشته و خواست بدون انتشار اسمش منتشر کنم این رو:
متین اسکنر سم و پینگ خیلی کندن
از masscan استفاده کنن چند هزارتا در ثانیه اسکن میکنه، من راحت تو ۵ ۶ دقه ۹۰ تا آیپی پیدا کردم
دراپ ریتش ولی رو نرخای بالا زیاد میشه.
کپی از چتای خودم:
چجوری اسکن کنیم؟‌ اگر masscan داشته باشید خیلی کار راحته صرفا این دستور رو بزنید:
sudo masscan
2.16.0.0/13
-p443 --rate=500 -Ss -Pn
جای اون رنج هر کدوم از رنجای زیر (رنجای آکامای هستن) رو میتونید استفاده کنید:
104.64.0.0/10
23.32.0.0/11
23.192.0.0/11
23.0.0.0/12
172.224.0.0/12
2.16.0.0/13
23.72.0.0/13
172.232.0.0/13
184.24.0.0/13
23.64.0.0/14
ریت هم می‌تونید زیاد کنید
https://github.com/robertdavidgraham/masscan
این خود پروژه
ویندوز هم داره
کل رنجای آکامای هم اتچ کردم با فلگ
-iL
میتونی بدی بهش
همشون رو هم ۵ ۶ ساعت بیشتر طول نمیکشن (خیلی زیادن)</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3061" target="_blank">📅 01:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3056">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">psiphon-helper-force-fastly-1.json</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3056" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چند کانفیگ سایفون‌هلپر متصل.
تمام اینها صرفا با تغییر ip یا sni در کانفیگهای
force-fastly, force-akamai
که در
https://t.me/projectXhttp/354790
قرار داده شده بدست آمده.</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/MatinSenPaii/3056" target="_blank">📅 00:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">برای اسکنر آیپی که خیلی‌هاتون پرسیده بودید دایرکت، ساده‌ترین راه اینه توی ترمینال(چه cmd ویندوز چه ترمینال termux) بنویسید
ping
20.20.20.20
(آیپی مورد نظر)
حالا اگر اسکنر هوشمند بخواید، میتونید از پروژه سم استفاده کنید که اصلش برای کلودفلره، اما میتونید کلا لیست آیپی بدید اسکن کنه:
https://github.com/SamNet-dev/cfray</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3055" target="_blank">📅 00:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3054">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یکی از بچه‌ها(abol) گفته بودش که:
از وقتی سرتیفیکیتو نصب کردم رو سیستم
دیگه نت سیستم به کل قطع شده
هر چی میگردم راهی برای حذف سرتیفیکیت پیدا نمیکنم
و این شکلی مشکلش رو حل کرد:
ریست شبکه در ویندوز گاهی همه فایل‌ها رو پاکسازی نمی‌کنه. این دستورات رو در حالت ادمین امتحان کن:
توی منوی استارت تایپ کن cmd و روش راست‌کلیک کن و Run as Administrator رو بزن.
این دستورات رو یکی‌یکی وارد کن و بعد از هر کدوم اینتر بزن:
netsh winsock reset
netsh int ip reset
ipconfig /release
ipconfig /renew
ipconfig /flushdns
در نهایت سیستم رو Restart کن.</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3054" target="_blank">📅 20:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3053">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان من، خیلی ممنونم بابت حرف‌های پر از مهرتون
🥰
خیلی خیلی زیاد خوشحال شدم از دیدن اینهمه پیام‌ زیبا
🌱</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/MatinSenPaii/3053" target="_blank">📅 20:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3052">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان من، خیلی ممنونم بابت حرف‌های پر از مهرتون
🥰
خیلی خیلی زیاد خوشحال شدم از دیدن اینهمه پیام‌ زیبا
🌱</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/MatinSenPaii/3052" target="_blank">📅 20:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اگر حمایت‌های پارتنرم نبود، مدتها پیش سلامت روانم رو از دست داده بودم حقیقتا. و اصلا بعد از دی‌ماه نمیتونستم هیچ کدوم از آموزش‌ها رو استارت بزنم و شاید از مبارزه ناامید شده بودم. تشکر ویژه از شما، بانو
❤️</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/MatinSenPaii/3051" target="_blank">📅 19:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3050">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خب گویا آی‌پی دیفالتی که پشت جیسون بودش رو زدن. مجددا موش و گربه بازی سر آیپی و sni تمیز.
Pypi رو زدن،
خود
python.org
بذارید باید اوکی بشه. همینطور از آیپی های این پست استفاده کنید:
https://t.me/MatinSenPaii/3040?single</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/MatinSenPaii/3050" target="_blank">📅 18:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگر حمایت‌های پارتنرم نبود، مدتها پیش سلامت روانم رو از دست داده بودم حقیقتا. و اصلا بعد از دی‌ماه نمیتونستم هیچ کدوم از آموزش‌ها رو استارت بزنم و شاید از مبارزه ناامید شده بودم.
تشکر ویژه از شما، بانو
❤️</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/MatinSenPaii/3049" target="_blank">📅 17:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_rQHOtILYlw6jwLFcNyW9YcjICGSIUU1z2pCAjdkvcYVb6wCtDnoSM-yW8NPfu0Z0Fyu2VRgvxjG8tedMq24qMJ7PH1X7Wlt14AjHRc9XlgjaUsayWi9chAucV_E6wQf11cE5iM9vCXxBuV_W5baGxOBP0K4SaclqMuAAfFTHDi3jjnggHBBVg5jI7_El0_b31bJqdkKvhetN2bg4QhZLM8kPh32UvPyY8yfxh-NKy1aCrqiex64g7LRecei6z1ZfekJQHzuCK1EIgRPF-DVRC0A4DoAWbk_Lz4QZ9Clo2A9XCfXcsrItMwFz1osUhck_XF0tKJaaY_3GSbnQTuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
وقتی رو سایفون ویندوز upstream proxy ست میکنید دیگه اجازه انتخاب لوکیشن نمیده برای دور زدن این محدودیت ریجستری ادیتور رو باز کنید برید به این آدرس
Computer\\HKEY_CURRENT_USER\\Software\\Psiphon3
و EgressRegion رو ادیت کنید و Value data کد هر کشوری که میخواید بهش وصل بشید بذارید</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/MatinSenPaii/3048" target="_blank">📅 17:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3047">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اگر به ارور Upstream proxy میخورید، یعنی پورت رو دقیقا اونی که توی ویدئو گفتم ست نکردید. یا توی بخش مناسبی نزدید. باید مو به مو چیزایی که گفتم انجام بشه دوستان</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/MatinSenPaii/3047" target="_blank">📅 17:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3046">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">روی ویندوز از این آموزش استفاده کنید:
https://t.me/MatinSenPaii/3035
روی اندروید مستقیم وصل میشید با این اپ:
https://t.me/MatinSenPaii/3038</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/MatinSenPaii/3046" target="_blank">📅 16:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">Matin SenPai
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3045" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TNSuk-Kv4i-sYSDjzIUUqb0dKpJxSvnWS92sDUHmTu4KKxhffWWQP-t5IXoNMknJ3eaA9OsveBX-DVKQ7rcJDyUSzFZ2QuE9NygaWjXauN0NduGQ8yZRih7Dm3SPONiQboLC2cimpERyVqfz9fwUCjyYT28eMD9JZ5y_FPMne4U2_HbKu2ngEC3SvyNMNPlbbHdxLx1xaa-pwQV3YsyKoONz6SJ_l2L-ckK6SEV7FEBaKkxR_010UEIIfNt05G1x5jaPWdiO5rsTILsuCDtIm9w12kVua24p5g0-FH0kZFuefBF5NMAf6-bpOPyu6uZcbQcH1vWy1OCqKapzoWGrSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/MatinSenPaii/3044" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/3043" target="_blank">📅 15:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NASog7cSfs4xrMhI5ImvMWNt-VlOu0-HC5VT5gPsUkGgsEOZxTBIUQqu_lvoWi_RA73wVhxQIXpq78NRqDeq3_A1yqf6Gk9n4UlojmrGGXydhz9e1WA7F-MPzbNqkFtARc6Vz6j_r6gGlVE19P158o-qGehC4OuViaelM9hXAgmP3pWWOifEX4Oq6uaP-RFYeZbuooTPStXv7vLcSnSjzpGAa5dweR37Os8bWerEkka2RS4i4J8yTxvmxYvkHnN_VkDaFJS1cGGngKX9TtdFvXyq8OtoF9fX7hr8fL3kk796iILycjbv7ErAE0UpWX8F4506t5WwALg5dbgYDrY9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/MatinSenPaii/3042" target="_blank">📅 15:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3041">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3041" target="_blank">📅 15:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j1_frsPEMymyK7WVCxQtKeI4KfX91VU6Ig_ASAUBE4P0bWhjHmvUrnFfHbWcSY1yUE0weD4af7R5fMyXhwy2DhzX9CaX__nfyju9HPRLC216rjAZVZt5oJcwLDwa53imJWdP3Sa5spmdh55g2kQHIWgqEUiF7hHItBIMLfz8DLkf7JHd3aLG4_hNtR-am4bR17YGeC4Ybc24XmxIUlYwFBidnlPXrknY6tKfaqJj2mj0O4te6wxqyHrjUetwsCarH2j5Lb3xdKW4xKTiW2zlOl8_BEQtZ_Jbk-bmCOmBM0A89rk84KaMEi5qye_wIAfi5T4XwjW6RE-I9Pqz1zzQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D6gbu63b1-9-MGwxmozLpAkeNW7vXt5GbiqJA87m5Qwl7mJ6kQ9CFvCRK7sw1flS2qvmUtVFq0SDE9V0oU7n0pynBLEZ9XwJ0hd5rIl9XFOnJmA_6gK3rdRmZWcfCsxqYDh3Ds7mtjkDS8WcN7rYxEp3lO2L_oUr1KgOP102wQeXt5W3gGkXBFLLghFSQUGx1AxL9evmVHx2ouyV_511_9eb6_rOpqA55jaKBhNAAYbBbmi9FBfukbfEhHHdZPEj7UAdBKUt6Jj1L6LMNUHnc62ByvbwgXNC9UfPrs8Cy3NHULF5LIwd5UZnCyu9Yun3rEM1BlB0p-4i6MKHvGtgiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ShirOKhorshid-2026.05.14.apk</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/MatinSenPaii/3039" target="_blank">📅 15:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3038" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛡
مهم: اگر این نسخه رو نصب کنید دیگه دردسر ستاپ کردن MITM و... ندارید!
این نسخه حدودا یک ساعت پیش توسط برنامه‌نویس شیر و خورشید آپدیت شد و به راحتی می‌تونید طبق این آموزش بهش وصل بشید:
1- وارد اپلیکیشن شیر و خورشید(آخرین نسخه که امروز منتشر شده) می‌شید
2- وارد بخش Options میشید از نوار بالا
3- روی More Options کلیک میکنید
4- گزینه‌ی  Connection Protocol رو قرار میدید روی CDN Fronting
5- میرید و عادی کانکت میشید و به راحتی وصل میشه!</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/MatinSenPaii/3038" target="_blank">📅 15:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3037">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حالا دیدین متد ترکیبی سایفون افسانه نبود و واقعا وصل میشد؟
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/MatinSenPaii/3037" target="_blank">📅 15:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دوستان عزیز، خواهش میکنم به DNS بها بدید. معلوم نیست کی مجددا متدهای حال حاضر رو می‌بندن. از نرم‌افزار و آموزش‌های
@WhiteDNS
استفاده کنید و الان که اینترنتتون شاید اوکی تر باشه، نصب و ستاپ کنید</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3036" target="_blank">📅 15:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">☠️
آموزش اتصال رایگان و نامحدود به اینترنت با متد ترکیبی MITM + Psiphon
⚡️
لینک‌های داخلی جهت دانلود:
https://guardts.ir/f/db4006f1197c
و
https://uploadgirl.ir/d/1f4fb76a-c869-494a-b439-b11cb8d35947
(شامل فایلهای V2rayNG، کلاینت شیر و خورشید، ویدئو آموزشی، V2rayN و فایل Certificate Generator و خود فایل Json پترنیها)
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد ترکیبی سایفون(کلاینت شیر و خورشید) + کانفیگ دامین فرانتینگ پترنیها، به اینترنت بین‌الملل وصل بشید!
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/MatinSenPaii/3035" target="_blank">📅 15:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چه حالی میده رایگان وصل بودن
📚
از زمان SNI Spoof اینو تجربه نکردم خدایی</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3034" target="_blank">📅 11:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3033">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بی‌زحمت لینک سایت‌های داخلی برای آپلود(هرسایتی که میشناسید اوکیه) واسم بفرستید، تا زمانی که ویدئو حاضر شد واستون همزمان به همراه کلاینت شیر و خورشید و فایل جیسون و ... روی چندین جا آپلود کنم:
https://t.me/MatinSenPaii?direct</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3033" target="_blank">📅 11:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3032" target="_blank">📅 11:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قطع و وصلی داره ها، اما هر 5 دقیقه، 10 ثانیه قطعه مثلا
برای گیم شاید عالی نباشه، اما وبگردی، اینستاگرام، تلگرام، توییتر و هوش مصنوعی‌ها همه اوکین</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3031" target="_blank">📅 11:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3030">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jFQfHlhbqSTrtVHZ_7htEwFmbV8AfXaDPsLJBkcvsenevIp2e8mtxhXrZng0JljWnMpBOHi1UHwrYni7Pfi_14RtcIY5TSwcj-fC4GR_KFR4vyHJOYNj_DpmJHRkhpEvb3UCVcb1rILTOcDqRv6y6XVb8tQY2Sh1mnbXB_PgjZsW_XOaIRx7mrJfRbEehDZd7oR4pJj4NGi1pr8O1kjuErpWgQomwaZwfTu5zTUPUZLZnR-RiJtwtLPBbtVipkMlcmTcY33PLqpKOcgLTREZvQ-y6Gsz1Hdouj7X6D3C_hghxKilW7wSTHy1c6T-rNfzdYfR16Ji3l1lUAg3UOWsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم روی گوشی(تمام باگ‌ها و مشکلاتی که توی گروه‌ها گفته شده بود رو در آوردم و دسته‌بندی کردم و خودم امتحان کردم)
این پست هم با همین متد داره فرستاده میشه
🕶️</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/3030" target="_blank">📅 11:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3029">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VyFXgCFsZvPP-SxOu8RPjzbegfm9rax8NGRg2iO1Jxqe0ZL8SH_L7CX4Jh4IhcyOzeXaKoHfPQc2dZ7WyJ5QnzLd7XHOXHemHhTrwtt6OlQ5AImRtSJ3gqN7sg8d0hQ5yi-IOO_rzt32Nv1dw8nHrb1q3ifjc6NlmGq609tHgGZhz3qlSiB7es2-sb5QgTyFXA0KHWp3lI9nZJOXp-JopM-_y6sMIJbWK3QqilQvs-pgvv6OPsxt2BnXfWeNzncumzroyFntMRj3RA7cnTrza3FKBo9fFGyyF95gI-dwidu3keOnmx7Mbn7wty96bO5aDCotEI-qfSF9LHsbhYI62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای یه روش کاملا رایگان، بدون نیاز به سرور، بدون نیاز به اکانت گوگل، بدون نیاز به شماره حساب خارجی و هیچی، سرعتش عالیه. آموزشش رو می‌ذارم واستون. خیلی ساده‌ست
با تشکر از
@patterniha</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/MatinSenPaii/3029" target="_blank">📅 10:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوستان عزیز که با اپ میتونن وصل بشن اما چیزی براشون لود نمیشه.</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3028" target="_blank">📅 20:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQKT18cUscTs25MeXXTAViW61dayIyXExy3CWwlwbX0dGWmC3rxXrVJ9iUOBI3rHK_jpFVl3Dcv8pnIAEk8-SBmyZbvcV5iiIj8iYIzizaFqD78iJ10H9K4D6bxGf-Hxg-0dWG1Vgr1ahTUYg3Bz-oGaaZCr4HXu2CRJZ9vQ9Foh4I805q9lKFRDq-TRalnS73sA3gGIVlvtC_hAXRUpImeaqsCmHB6bp6zf3vxfjBIikeuIqtIl8iwuBv9l9fcEICuQWp2n8DJ3xEKKKD11an_cqB4QXq0GZOSSfMOIj0UyhvvdWAmBfowLoVLX4BkM1MH5bFQGxDs4gR7kxHmnhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات
@dns_resolvers_bot
اضافه شد
@WhiteDNS</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/3027" target="_blank">📅 06:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره. اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3022" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره. اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/MatinSenPaii/3021" target="_blank">📅 21:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره.
اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم صرفا این محتوا رو دوست داشتن، نه اینکه شخصِ من رو دوست داشته باشن.»
و اینجاست که مغز ما رو به بی‌راهه میکشه.
متأسفانه عموماً از اون لحظه، شخص دیگه حرف‌هاش رو برای بیان نمیگه، بلکه برای حفظ اون حس میگه. و همونجاست که گم میشه و مسیر رو کلا گم میکنه.
به خاطر همین هم هستش خیلی از افرادی که این روزها وایرال میشن، بعدش چیزهایی میگن که ممکنه ازشون بدتون بیاد. توی فرهنگ عامیانه، می‌گن طرف جنبه‌ی شهرت نداشت؛ ولی واقعیت علمیش چیزی بود که خدمتتون گفتم.
اگر وایرال شدید، خواه ناخواه دوپامین کار خودشو میکنه و حس خوبی دریافت می‌کنید اما مدام حواستون به این نکته باشه(همونطور که منِ متین حواسم هست) که این صرفا یک عدده و من تغییری نکردم.
پیروز باشید
✍️
Amir Mokhtari
با کمی تغییر از سمت من</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/MatinSenPaii/3020" target="_blank">📅 18:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do3E-7ed-lafVmtqncJ5XZDPi2H1xPi0QSHG7u7PDKdEZqg0xZMlcTnQhiFcIoI1GDlRCMT5oiQ2gMtZk7YHChdrwpOTGk3G6Z3p-i4vCeq3TKqPZkq4yhpdjN-GICFxjTU8DksU6O_WuRElzGfA2CMJvNeGJubdzNOI3CsvSzsBOl8wvsXAv4m3LOEE17FUaICH7W4BLQUr77U5g5H9rdAxWgT6C0mOP3Y6SMXvt9ArQ17N1AJuslBjNw2Y6jCvd7G5LYxnwVg8L6idUhiV2LOFwPeUwiCA6r4DYgP_ZtcH4bdHRScRQWr7LuCoU26WWEoisv555Qhg5Yd5eEH4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IRCF | اینترنت آزاد برای همه (Twitter/X)
🍷
اپ متن‌باز و
#رایگان
TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
لینک پروژه:
⚡️
http://github.com/MaxiFan/TunnelX/releases/latest
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3019" target="_blank">📅 17:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ1Nc3unQZvv08_g-2VaEAl_F0PC90oG884PeSp11bLl9r_39CO_TKTQ7MyRkhqCCEXDukTXrgq0SMWmqKptYC3UjU-5bwDHTn178R1d1pNDefNXfYWrcM_G6AULWs82GM2OgHLZNMOvIW979EfLfMbnevXEZ4VkN5bB6QfetuVWmd4Wa6kR9EGO5qFrfotr59Q1-PMYCbSbw3eLuv2UvDVC5pG-eT531Obfm0HXcXmrcb7S_l8PiUmZMDDr5I_SN59pZyozDpg0UuNCi63f_T2aTmosTlMacbLyybEfyl3S4n7Rl9qE0HlyU6A58j8W_0zmlZ4LtXrDC7G7WTvk-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای دریافت ریزالورهای MasterDNS / StormDNS در WhiteDNS
ربات WhiteDNS حالا امکان جدیدی برای دریافت ریزالورهای MasterDNS / StormDNS دارد.
برای دریافت لیست ریزالورها مراحل زیر را انجام دهید:
1️⃣
وارد ربات زیر شوید:
@dns_resolvers_bot
2️⃣
دستور زیر را برای ربات ارسال کنید:
/dns_master
3️⃣
بعد از نمایش لیست ریزالورها، برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید.
4️⃣
لیست کپی‌شده را داخل اپلیکیشن WhiteDNS وارد کنید و از آن برای اتصال استفاده کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/3018" target="_blank">📅 17:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3013">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3013" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی بهبودهای داخلی VPN در خود WhiteDNS بوده است. هدف این بود که اتصال کامل‌تر، پایدارتر و مستقل‌تر شود تا کاربران برای باز شدن سایت‌ها و اپ‌ها دیگر نیازی به NekoBox، NVPN یا راه‌حل‌های مشابه نداشته باشند.
در این نسخه مسیر DNS و ترافیک داخل خود WhiteDNS بهتر مدیریت می‌شود، بنابراین تجربه اتصال ساده‌تر شده و کاربر می‌تواند مستقیماً از داخل اپ وصل شود.
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
✅
حالت Full VPN کامل‌تر و پایدارتر شده
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
✅
ظاهر صفحه اتصال و دکمه Connect/Stop مرتب‌تر و جمع‌وجورتر شده
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.2.0
از همراهی و حمایت شما ممنونیم
❤️
1⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/3013" target="_blank">📅 17:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rKR8XqTGDAdfft8lA4eSoX_s-h_KCBJijsrfT3nxTUT6eulXY3E6FDIYLu8jdOqsBnb8ws89WI1cv7qk88pDnIXgu7gJRPZHWJwFcP6lcSjy6Kg1BDydLrahcEY9wOjT-iSIp-4UOYeD61KuMRrhk2zxm_6aT3eK454sqxGUATqq7pELJSjPS5yFz5WfPqAflPjLg1lkZYQ_xlCHNA8uDNHZ_ik9Jjx5TJrQgkuFrkvekB5KTaVXdoVDnayy7WaCygj0Ah58He2FEP7wTK7cf1KIQ8E8J2ib5AE2-vB638TKwphhIH8nbi0ljYkMnVzSPJqKyyO0KHrT2v-sAvtDOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CzGB3dmqqVoN3dxHKU53hxXAiQ1dhI3kz-aYnfpuCu8F_hWUoluH3EC5NoB1O7EJiu5LcT0p1qMp78FpqcFqqh9tkIyBN_kI7zzLJcP4sUWMORKEEwsGoQgOsTsROWZ35vzlmZKJJeQAxMjK7wDzMswpp1bb_mZExH9zXOrKHyuXjwchCyFDnX4MNxxzo0ef98LPPa6ig0AmJkuNQO12u2aeJF4wCFiaU7QDr-mv1aEkseH3ztCRmyC-DuHmLBeBYT0BVH8VbCxKFmON0iGSF8RffGfAXBsawRPoaCXP2WVKcRGPQA7lZHN_FO-aKxBGLuuCVmV9w5GyKFaau7zY-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی یه آموزش بر پایه‌ی DNS داریم. یک دونه رایگان بدون سرور، یکی با سرور.
به همراه آموزش پیدا کردن ریزالور
با تشکر از بچه‌های تیممون، WhiteDNS
(توی این عکس با سرور رایگان وصلم)</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3011" target="_blank">📅 23:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">من تازه دیدم که یک نفر امروز صبح 500 دلار دونیت کرده به wallet های روی پروفایل توییترم. و هر کس که بوده، واقعا ازش ممنونم
❤️
کمک بسیار بزرگی به ادامه‌ی فعالیت و همینطور دلگرمی هست برای من توی شرایطی که درآمد یوتوب قابل برداشت نیست و شرایط اقتصادی داغونه. اگر…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3010" target="_blank">📅 23:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پول پارو کردنی در کار نیست. این پول‌هایی که دارن می‌گیرن بیشتر واسه جبران ضرر و damage control هست که بتونن یه مدت بیشتر قطع نگه دارن.</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/MatinSenPaii/3007" target="_blank">📅 09:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فیبر نوری مخابرات کلادفلر وایت لیست شده ظاهرا.. امیدوارم بازش کنن ناموسا بریم دنبال زندگیمون</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/MatinSenPaii/3006" target="_blank">📅 09:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3005">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromfarzad</strong></div>
<div class="tg-text">متأسفانه همه راهها رو معنای واقعی کلمه بستن (غیر از mhr که اونم نصف و نیمه و داغونه) وشما به هر نحوی بخوای به نت بیرون دسترسی داشته باشی باید هزینه زیاد بکنی ، یا بری نت پرو گیگی ۴۰ هزار تومنی بخری یا وی پی ان گیگی ۱۵۰ تومنی مثلا یا بری سرور بگیری cdn بخری وdns بخری و .... بازم هزینه گیگی بالا میوفته ته همشونم پولش تو جیب خود دولت و سپاهه همه ی اینا</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3005" target="_blank">📅 09:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آقا من نمیدونم این چه وضعیتی هست که درست شده توی این کشور !
هر چی میاد میگن پاپلیک نشه ! شما متوجه هستین مردم بیشتر از 60 روزه با این قطعی نت مشکل توی زندگی ش پیش اومده ؟!</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3004" target="_blank">📅 08:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رفقا من متد‌های حال حاضر رو میدونم. بله میدونم که CDN آروان چطوریه داستانش
منتها برام معقول نیست آموزش دادنش. نه هزینه‌ای که باید واسه‌ی CDN داد منطقیه و نه پابلیک بودنش. اینم احساسی که بهش دارم مثل Shecan هستش. یه Back-Door توسط خود حکومت که خب دست خودشونه.
مثل گوگل نیست که بهشون فشار بیاد که باز نگهش دارن. اگر اشتباه میکنم من رو متقاعد کنید</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3003" target="_blank">📅 08:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3001">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromペコリーヌ</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sp1K2umgexv_z7V9InjLXhO_kHr9Dundd32M_M-U59REsbmkeP25vawxKvA71wzJpuI4TEqWCfQxP6cy4lcCHC4PlRjRmgpuPGKJrbFUkgkusLVpH5vqOzgsVS0DmUDN-ZeF0OaFUz7dAFaSM6AyHJUlRHtgRXGAJGOXoH7XdNiLl4CZaZcq7O5islBPA73TmF6lSszwT2OklHq23pYllerU6TFpS-c3wj_fsDeG9VJ10IOUQQ0ZHZm_uAORPM1yU_5mcTfqEvX3IPjONwLqsOrfZSsVyWL-dE76q3PHSa8NfVoN0cH2fSbsmSySrHa-grinB2irO0486qdQLmBLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O0r8pvPJOcYbRvVipyt7AMo-J8hKrVCUa73mSxLpBgOq1e6lhDlkkperjtwHD2HwJY1XwKK_2pTM8TGJFrt-91o1FJHHlAUFj17ryuEl_Ihgn8qubYWKPC50a9BSwYQ0COa-61BN9nei8MhlkUaKL5ugDMHJcTPX6BECEdhRtXRW72ZEDuTJDM55emuMe2lPMyFRxlEXT9ropTcfifRYPft8EFnKcJR6SOP-RbR5n47EYyvzpjm0m-ix_Jh3-b8rdV0nWtWDG6Op9TMPyWmIRojtu7EFeh9JQ0MZKGUzGI_BlG8ZMLmKWL53RV_Wwg-JNXsTmUbEl89WIjR64Eu8rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واسه ۸ گیگ اکانت رو بستن ؟!</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3001" target="_blank">📅 20:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اینا رو سرور ایرانی شکن فعال کردن روش vpn زدن و کانفیک میفروشن، طرف در عرض چند روز یک ترا ترافیک رد کرده مشخصه مشکوک و پیگیر میشن</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3000" target="_blank">📅 20:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نقره ای دارم یه ماهه استفاده میکنم راضیم چرت و پرت هست این</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/2999" target="_blank">📅 19:28 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tc_Kveld2bdCSQFc9bSSM3kbnv09wPhOq6Te5SsNZc00UZYG7Ds8RsHv-4mWmKWa-UoAN61Rnk-mw9xiTy2JECPXLgzP-wbj68tgE9_NPJypwuudZN38XxRDhPKc0mAzzGpCz0oU3-4B6fJuZayOOclxdeUDzilYwMr2Vbg8giBrtRpHZC0RIYzxwIojNhqbLDHxWQ66GINw72yHl-vRVz6itTVP0lsNFD8cLt5Kh5z2cue0C75QxTseXy6gOz4qepP0CidvCWTXlGA2FV0_uCNpwImNDD-ypZC5pzoW2ze80Gz1q6PDiegPyEHygjhGnY9OSUNoT0UE1mcAdVwiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول به "شکن" و امثالهم هم ندید. یادآوری کنم که چند هفته پیش، به مدت دو سه روز chatgpt روش باز شد و ملت کلی اشتراک خریدن و روش کانفیگ ساختن و باز مسدود شد. پول مردم هم رفت سطل آشغال</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/2998" target="_blank">📅 19:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2997">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">من این تایم 70 روزه رو خودم 5-6 روزشو قطعِ قطع بودم. اما با اینکه توسط چندنفر بهم آشنا و پارتی از زیرساخت معرفی شد(از فعالیت من هم خبر نداشتن و سر آشنایی بود صرفا) باز قبول نکردم همچین چیزی رو و توی تاریکی و قطعیِ کامل در حالی که لپ تاپم بیست-سی ساعت بود داشت dns اسکن میکرد به دی‌ماه فکر می‌کردم. اگر چند روزی دیدید که من نیستم، بدونید قطع بودن رو ترجیح دادم و یا Dns رو هم بستن عزیزان. کسب و کارها یا نابود شدن یا رو به نابودی هست. هر روز کلی پیام دریافت میکنم که من تدوینگر/هانتر/دیزاینر/فری‌لنسر/برنامه‌نویس/... بودم خرج زن و بچه میدم و تمام درآمدم از اینترنت بوده و لطفا یه متد معرفی کن بتونم وصل بشم و من باید با شرمندگی این جواب دردناک رو بدم که هیچ راه معمولی‌ای وجود نداره برای وصل شدن با سرعت قبل.
اما چه کاری میشه کرد! جز نگه داشتن امید و صبر.</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/2997" target="_blank">📅 21:17 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سوخی با همچین موضوعاتی چیز درستی نیست</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/2996" target="_blank">📅 21:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آهنگ (هفتاد روز که من از تو خبر ندارم) ایرانی</div>
  <div class="tg-doc-extra">•(Ali....Amin)•</div>
</div>
<a href="https://t.me/MatinSenPaii/2995" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مردم ایران خطاب به اینترنت
01:00
🫩🫩🫩</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/2995" target="_blank">📅 20:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آمریکا هم عجیبه
ما داریم زجر میکشیم از نت اونا هم اسنادشون رو منتشر کردن راجب یوفو و بشقاب پرنده
https://www.war.gov/UFO/</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/2994" target="_blank">📅 20:02 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2992">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد Advanced Settings شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup:…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/2992" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2991">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilwwBHDA24LWPn9y5GPWyDivxfGIqNQ-_BDluskTJ97O3yjy8_Fh6o5ubM5ww4jZ9hcBQkPbCtl8WfFWuPTP_IBJtLGsxJkc80fcuFJAiWo7BBb-ucRe4YPv3v1I3UrKHkwLOWDqaNzoOldpKAbUFbjryfcI0SXHkR2UDRrMlIu79Mg25dA_4LMEzkwECOELf6Fd-grl-E3pHhCqDqh319-uiuqd-KQHZiApJ0oXQOv_8lnwmNBUlwLwV4UlEIsJCp20mT3hgI54iPAWw5E-j9i7CiO2PEVY1OLNEgmW1mZNOX2I9MCClRM29TdQzgpyIdIySU2Qd-q6nJaI9gpDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد
Advanced Settings
شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup: 1
🔸
Download Dup: 4
🔸
Upload Compress: OFF
🔸
Download Compress: LZ4
📊
این کانفیگ به‌صورت حدسی انتخاب نشده.
ما لاگ‌های سرور در ۷۲ ساعت گذشته را پردازش و بررسی کردیم و بر اساس پروفایل‌های موفق‌تر، MTUهای پایدارتر و مسیرهایی که سرعت بهتری داده‌اند، این تنظیمات را پیشنهاد دادیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/2991" target="_blank">📅 17:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2990">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">thefeed-android-v0.17.4-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/MatinSenPaii/2990" target="_blank">📅 16:40 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2989">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.17.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/2989" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
thefeed-android-v0.17.4-arm64-v8a.apk
📊
Size: 8.9 MB
🔐
SHA256:
466659489e5429db20710d85241012002aec644cb739220338b9dd6aef186fe8
نسخه جدید TheFeed (v0.17.4)
🚀
🟧
تغیرات بخش اصلی
:
🔸
نسخه IOS بصورت ipa در دسترس هست، اگر بلدید خودتون ساین کنید و تست کنید بهم خبر بدید که چطور بود (دارم تلاش میکنم بزارمش روی تست فلایت تا همه بتونن نصب کنن)
📱
🔸
برنامه زمان اجرای اول زبان رو میپرسه
🗣️
🔸
فیلد جستجو فقط با یوزرنیم جستجو میکرد، الان با اسم کانال هم جستجو میکنه
🔍
🔸
زمانی که اسکرول کنید مثل تلگرام تاریخ پست رو بالاش نشون میده
📅
🔸
اضافه شدن بخش حمایت مالی
❤️
🟦
تغیرات بخش کانال های دلخواه
(TeleMirror):
🔹
دکمه نمایش پست های بیشتر به بالای اولین پیام اضافه شده تا بتونید میام های قدیمی تر رو هم لود کنید و ببینید
👀
🔹
قابلیت باز کردن عکس ها
🖼️
🔹
قابلیت تغیر سایز فونت
📝
🔹
نشان دادن ای دی پیام ها
🔢
🔹
رفع مشکل نمایش فایل تکراری
🗑️
🔹
دکمه برای پریدن به اخرین پیام
⏩
کانال اصلیم:
@networkti
کانال کانفیگ:
@thefeedconfig
لینک دانلود نسخه جدید برای تمام سیستم‌عامل‌ها از داخل ایران (با گیتهاب):
https://github.com/sartoopjj/thefeed-files/archive/refs/heads/main.zip
📥</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/2989" target="_blank">📅 16:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به نظرم اولین اقدام دولت این خواهد بود که یه لگد میزنه به Google و ما، و MHR قطع میشه</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/2988" target="_blank">📅 01:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این کار «زدن و گردن نگرفتن» واقعا رو اعصاب‌ترین بخش جنگه
کی اینو بهتون یاد داد اصلا</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/2987" target="_blank">📅 23:20 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JhZXjVxVdgdoDN8xkZIR8HCqbjVFNGUIBRV3-mMM3wEqQAGvDRajcNsc4b74UTzpNro_DOKLrNtDgy7K9vtA1NRGGXsKg53GAzpql1uv2KfDbzB8xPSy-8ANPF5qQdugSNuKUr5BCwzMtnHgulaEH5wVREBUXLd334FddxM_Cmz1vi6QMNobV0u_ElTaKbpaP3bU2LcmHBL5CVTOXABmSkfStl2FqAGnpfA674cZXDzXITu4AXo67MLWv5rxhfmanbH6ENqwWw8cjXh_ulHDg3FqJr3TSePLAJqaItlUPzqiFmCxFePnsrx183ooikbYI36JKNshJPAolvlDNvxGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر اکانت مایکروسافت ویندوزتون رو از مایکروسافت به Local تغییر بدید تا این بلا سرتون نیاد. همینطور علاوه بر پین کد، پسوورد هم تنظیم کنید و راه‌های دیگه‌ی لاگین.
من دو بار به این مشکل خوردم و متأسفانه تنها راهی که پیش بردم این بود که از طریق Advanced Troubleshooting رفتم و ویندوز رو دوباره نصب کردم(فقط اپ‌های روی درایو C پاک میشن و بقیه درایو‌ها و همینطور پوشه دانلودهاتون سر جاش میمونن)
اینجا یه ضربه‌ی وحشتناک خوردم و اونم این بودش که مجددا بعد از چند روز قفل شد و روز از نو روزی از نو. که فهمیدم راه حلش اینه:
1- تغییر اکانت مایکروسافت روی ویندوز به Local account
2- حذف پین کد(که بکاپش ایمیل مایکروسافت هست) و اد کردن password یا یه راه لاگین دیگه. بعدش مجددا میتونید پین کد هم اضافه کنید
الان سه هفته اینهاست که به مشکل نخوردم دیگه</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/MatinSenPaii/2986" target="_blank">📅 22:44 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2985">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uSjmzROz16NIMCrhVXOQOVa0NygNlRxxSlt8_EH65rItBC_DSZtHX__XJyHydArIE-BN9TTtFF6eEigH228hOrw6ZGcmQ9f9AZrEyqVDSFcAlAlX0OWkXsNUPU7yqnuOM6FxxLg1fHeE3T9FGxRaDVgUWMGUHtpl5BzprwFmudlJlRC_THzBi30qyn-K6lVA9xDneXj7RrFj48J1HuX4wgtk6NLd_4poVuEUUbSqf9sEILF846h4lnEhXaVAg5zAheUn-60R4xB4nPneHUOQkp0MXQ7De-YpYehnXCfHeI00iXt_vxU5QFRLtfbkNEPeMoDV2HMPAxst0-NGYkKejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان فرمودن که با این ریپو: https://github.com/ThisIsDara/mhr-cfw-go تونستن مشکل کامنت‌ها و ارور restricted رو برطرف کنن</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/2985" target="_blank">📅 21:22 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه سریا برمیدارن Deployment id هایی که من توی ویدئو استفاده میکنم رو می‌زنن و استفاده می‌کنن
😂
من عادت ندارم اصلا پاک کنم چیزیو. و اشکالی هم نداره. فقط کلودفلرم و گوگل اسکریپتمو ترکونده بودین هرچی اکانت روش آموزش دادم
😂</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/2984" target="_blank">📅 21:17 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mAcm6s52OpBLcRVbYZouIQXjHnG44MeeLMkRS5-N5vgvHvxKEN43HKSirRjHtqc0rMtty48tMYxmxS6237yi8q2qSM4TVOAlntH5NmLyrQKa-34zMkWX_jxuFRnxai7cHY_6ZrhsddBWreaUaoG3T9aHu663ZcoLFp_xo6P0NmTYUSui_gcc_gRdMx7PfQbVg5wfy9arN7AiY8KQ4wm6QBsSLGfaZxLE8LEaoKmU9E_DwUejAJfhoO5Ey2dDmYFinH8eqn_V5q6vJi5GHq1Ds3Z080l5cH9GuFFkkQOzkrWFpEu6o4Op_UmyJ3k2IdUoTlRrCIkLJI2OWFiuW_5qwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان فرمودن که با این ریپو:
https://github.com/ThisIsDara/mhr-cfw-go
تونستن مشکل کامنت‌ها و ارور restricted رو برطرف کنن</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/2983" target="_blank">📅 21:06 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قوانین مسخره ios که نه
خارج از ایران اصلا نیازی نیست mhr بزنن</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/MatinSenPaii/2982" target="_blank">📅 20:51 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2981">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اندروید نداریم</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/MatinSenPaii/2981" target="_blank">📅 20:45 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">☠️
آموزش ساخت متد MHR با گوشی + کاهش مصرف ریکوئست های گوگل
⚡️
لینک‌های داخلی جهت دانلود: https://t.me/MatinSenPaii/2969  لینک پروژه اصلی: https://github.com/therealaleph/MasterHttpRelayVPN-RUST
⭐️
توی این ویدئو بهتون یاد میدم که چطوری متد MHR رو صفر تا صد…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/2980" target="_blank">📅 20:43 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2979">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">می‌دونستین یه نوع اعتیاد هم داریم به اسم اعتیاد اطلاعاتی؟
شما ممکنه ساعت ها با هوش مصنوعی چت کنید و خسته نشید و ولعتون بیشتر بشه برای چت کردن باهاش، یا اینکه یه نصفه روز توی صفحات ویکی پدیا بچرخید و مدام اطلاعات مفید بخونید با این فکر که آره دارم چیزای مفید یاد می‌گیرم، اما این کار شاید ظاهرش به اعتیاد نخوره اما جالب اینجاست چون دوپامین پسیو (دوپامینی که بدون سختی داده بشه) می‌ده و هیچ سودی هم نداره دقیقا خود اعتیاده. فرمول خاصی هم برای ترک کردنش وجود نداره اما مثل همه اعتیاد ها میشه با سختی کشیدن ترکش کرد برای مثال یه کتاب (فقط حتما یک موضوع واحد باشه) رو بخونید دقت کنید فقط موضوعش واحد باشه.
یادتون باشه هرچقدر هم درباره چیز ها در طول روز بخونید اگه اخر شب نتونید 3 خط دربارش بنویسید اون چیز هیچ وقت به آیندنتون کمک نمیکنه و بیشتر جنبه سرگرمی داره.
@Linuxor</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/2979" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💬
یه سری مطالب از Repo سازنده‌ی MHR واستون قرار میدم(مربوط به این روش: https://t.me/MatinSenPaii/2785) :  اول از همه دقت داشته باشید که به روز ترین نسخه‌ی code.gs رو حتما از گیتهاب پروژه گرفته باشید: https://github.com/masterking32/MasterHttpRelayVPN/blob/…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/2978" target="_blank">📅 15:54 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2977">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ولی من دقت کردم نه کسی پین نگاه میکنه نه سوالشو سرچ میکنه تو گروه فقط میپرسن پشت هم</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/MatinSenPaii/2977" target="_blank">📅 04:14 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">به نظرم تریدرا الان باید به جای دوره‌ی آموزشی، دوره‌ی تحلیل رفتاری ترامپ رو ببینن</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/2976" target="_blank">📅 01:35 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uT9TGkDn69_2Dq6ir0mdDdGHAmTeII4_B5ioKyEyNweKmd75V_edhPF9gVFE6jCdwACB-WAzz1KAK6KmxrF0-C3DyFQ6roMB63-xcfwH6OFlt76jb5KKeabwuQ4g3c4bS02ldjjIjiRwBcVAFqxmIfdGsAKiq6jtJb0Utl6IVqFTPyvM1puI_wAxUr77HusPEiMt0VFfo8mQySAhqpLMQLDeDRIeI4rE-4uFgJp4TjfoPo_Mcbnz4jT1uGoj_3mJrGpcGcb5H3vhCW4gklWb8XinBzZuKisCPEhxqocS4UhhhBVpsakl_FV1iJf-tCrMU6o_7rvw0NF8CzmKXC6jwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
دانلود با اینترنت ملی از یوتوب و تورنت و هرجای دیگه!
پروژه AzuDL - GC2GD یه ابزار کاربردیه برای دانلود فایل‌ها از طریق Google Colab و ذخیره مستقیم اونها روی Google Drive
با استفاده از این ابزار می‌تونید لینک‌های مختلف رو داخل Colab اجرا کنید و فایل نهایی رو مستقیم داخل گوگل درایو تحویل بگیرید؛ سپس با متود MHR فایل نهایی رو دریافت کنید.
🖥
قابلیت‌های اصلی پروژه شامل دانلود لینک مستقیم، دانلود ویدیو و پلی‌لیست یوتوب، استخراج فایل Mp3 و... هستش
💡
ویدیوی آموزشی پروژه AzuDL -
GC2GD
سورس پروژه:
https://github.com/TheGreatAzizi/AzuDL-GC2GD
✉️
@MatinSenPaii</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/MatinSenPaii/2975" target="_blank">📅 01:23 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/2974" target="_blank">📅 01:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لینک های داخلی اموزش و برنامه
📥
mhrv-rs-android-universal-v1.9.14 39.2 MB
📥
mhrv-rs-android-arm64-v8a-v1.9.14 18.1 MB
📥
mhrv-rs-android-armeabi-v7a-v1.9.14 15.8 MB
📥
ویدیو اموزش ساخت متد MHR نت داخلی 18.3 MB
📽️
﻿</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/2973" target="_blank">📅 01:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-text">لینک های داخلی اموزش و برنامه
📥
mhrv-rs-android-universal-v1.9.14
39.2 MB
📥
mhrv-rs-android-arm64-v8a-v1.9.14
18.1 MB
📥
mhrv-rs-android-armeabi-v7a-v1.9.14
15.8 MB
📥
ویدیو اموزش ساخت متد MHR نت داخلی
18.3 MB
📽️
﻿</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/2972" target="_blank">📅 01:11 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
