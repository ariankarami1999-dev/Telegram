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
<img src="https://cdn4.telesco.pe/file/et1gtQISz72pKtT7VhEx2934eZkRn91129GfMv2PgI5nqiVUuPrWA1vp5n-uu7PJrASxwUQKgH8oV9ldQDqNtXqP-DQSVrZU7b1bJ1mkQIwe0fNe7upV5qv32V2UGDA9b3Y5JdhKxDyMpMHkhaNPRDF3GvK3qEeA4mLUoZxQakgKlafnumaEQQMV6wM6Ttoq87S5F5Qy39-u4Jb0CcTn-zyAGBnWogeSBJVS3ypXi2EAhU0qttw04iHHPXGoNaAKNuLtEsMcMhkx5s2wxg-yYp_9ycnnlbmO7QgbkY_BOGnbw4XkAV7sq7w3dfc7Ctl5L_60jd9-jSwKbJCmk5wYJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.8K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 21:10:54</div>
<hr>

<div class="tg-post" id="msg-8542">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید، خوشتون اومد فور کنید
🍸
😁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 524 · <a href="https://t.me/IranProxyV2/8542" target="_blank">📅 21:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8541">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?path=%2F&security=tls&encryption=none&insecure=1&host=sni.111000.indevs.in&type=ws&allowInsecure=1&sni=sni.111000.indevs.in#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
کانفیگ با پورت های متفاوت براتون میسازم، سعی کنید همرو تست کنید، ببینید با کدوم راحت تر هستین، حتما برای دوستاتونم بفرستید
✅
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/IranProxyV2/8541" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8540">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@104.16.7.70:443?mode=stream-one&path=%2Fde&security=tls&encryption=none&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=de.xn--q9jyb4c.online#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
چند ثانیه صبرکنید وصل بشه، هنوز پهنای باند اونقدری زیاد نیست که پرسرعت وصل بشه، یادتون نره فور کنید واسه دوستاتون
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/IranProxyV2/8540" target="_blank">📅 20:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8539">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">vless://8b84b146-3405-44f2-98e4-f0ac7dbad0c0@104.17.147.22:80?mode=auto&path=%2FTelegram%40SoonTeam&security=none&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&host=uk.im-eb.cc.&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
سرعت عالی، رو همه اپراتورها، بفرستید واسه دوستاتون وصل بشن، حجم نامحدودههههه
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/IranProxyV2/8539" target="_blank">📅 20:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8538">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">vless://48d1cb9d-bbd4-4444-b833-6720619a117e@104.16.89.120:8443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=nl8.bioritalin.ir&fp=chrome&type=ws&allowInsecure=0&sni=nl8.bioritalin.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همه اپراتور ها متصله، وصل شین لذت ببرید
✅
حجمممم نامحدودددد
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/IranProxyV2/8538" target="_blank">📅 20:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8537">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">vless://06ef598c-1555-4887-b3f9-08214a2f6792@172.64.152.23:443?path=%2F222.167.202.31%3A7443&security=tls&encryption=none&insecure=1&host=2026.hhhhh.eu.org&type=ws&allowInsecure=1&sni=2026.hhhhh.eu.org#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو تمامی اپراتور و نت های همراه وصله
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/IranProxyV2/8537" target="_blank">📅 20:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8536">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👑
اینترنت ایرانسل و همراه اوکی شد و باید فیلترشکن های رایگان برایتون وصل شده باشه
❤️
🛜
🛜
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/IranProxyV2/8536" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8535">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">vless://48d1cb9d-bbd4-4444-b833-6720619a117e@104.16.89.120:8443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=nl8.bioritalin.ir&fp=chrome&type=ws&allowInsecure=0&sni=nl8.bioritalin.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همراه اول متصله
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/IranProxyV2/8535" target="_blank">📅 20:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8534">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
اینترنت بین الملل روی خطوط همراه اول هم وصل شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/IranProxyV2/8534" target="_blank">📅 20:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8533">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کانفیگ رایگان برای وایفا
✅
vless://4493268e-2083-4a18-9c24-72c1f8f604d5@92.42.203.168:443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=dl-server1.tpchat.ir&fp=chrome&type=ws&allowInsecure=0&sni=dl-server1.tpchat.ir#
%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/IranProxyV2/8533" target="_blank">📅 20:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8532">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/IranProxyV2/8532" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8531">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/IranProxyV2/8531" target="_blank">📅 20:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8530">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پروکسی وصل
✅
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8530" target="_blank">📅 19:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8529">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">vless://fe23b0d9-ab91-4f7b-a5a4-89e4ae9b094e@www.speedtest.net:443?security=tls&sni=broken-mud-0a9a.rigacihir69.workers.dev&alpn=http/1.1&fp=chrome&type=ws&path=/eyJqdW5rIjoiZEFtaFJ6RlAiLCJwcm90b2NvbCI6InZsIiwibW9kZSI6InByb3h5aXAiLCJwYW5lbElQcyI6W119?ed%3D2560&host=broken-mud-0a9a.rigacihir69.workers.dev&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصله، رو وایفاها
✅
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/IranProxyV2/8529" target="_blank">📅 19:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8528">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزیر ارتباطات:
اینترنت همراه تا امشب وصل میشه، تا فردا اینترنت به قبل از دی برمیگرده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/8528" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8527">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📌
بزنید تو نپستر با ایرانسل تست کنید
🛜
ss://YWVzLTI1Ni1nY206WldZeVlUVTBZV1k0T0dNME5EUmhabU0xWkRRMFpqRTNNR0l5Wmpneg@ir.npvnot.com:10112#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/IranProxyV2/8527" target="_blank">📅 18:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8526">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭕️
شرکت مخابرات: اتصال کامل اینترنت بین‌الملل مشترکان برقرار شد
🔸
کاربران سرویس‌های پهن‌باند ثابت شامل FTTH، VDSL و ADSL هم‌اکنون بدون محدودیت به شبکهٔ جهانی اینترنت متصل هستند و امکان استفاده کامل از وب‌سایت‌ها و خدمات بین‌المللی برای آن‌ها فراهم شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/IranProxyV2/8526" target="_blank">📅 18:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8525">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
آمار لحظه‌ای وصل اینترنت کشور
✅
مخابرات (منطقه ای)
✅
آسیاتک
✅
شاتل (منطقه ای)
✅
‌پیشگامان
✅
مبین نت TD-LTE
✅
صبانت
✅
پارس آنلاین
✅
زیتل
✅
‌افرانت
✅
ایرانسل (TD-LTE)
❌
ایرانسل (سیمکارت)
❌
‌همراه اول (سیمکارت)
❌
رایتل (سیمکارت)
❌
سامانتل (سیمکارت)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/IranProxyV2/8525" target="_blank">📅 18:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8524">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔸
چه ‌وب‌سایت‌هایی در دسترس قرار گرفته‌اند؟ /دیجیاتو
ویکی‌پدیا
اپ‌استور
پینترست (Pinterest)
کنوا (Canva)
نوشن (Notion)
تردز (Threads)
کالاف
CallofDuty.com
پابجی (Pubg)
یاهو
دراپ باکس
پلی استیشن
ایکس‌باکس
استیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/IranProxyV2/8524" target="_blank">📅 18:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">از اونایی که پرو خریدن چه خبر
😂</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/IranProxyV2/8522" target="_blank">📅 18:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8520">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✈️
دوستان اگه در راستای قطع شدن بودین و وایفا نداشتین میتونید از ربات ثبت سفارش انجام بدین، آنی تایید خواهیم کرد و اینکه درنظر داشته باشین،
اطلاعیه
رو حتما مشاهده کنید.
📌
در صورتی که نت بین الملل بازگشایی شد، تمامی کاربران که از ما سفارش فعال دارند، به دیتاسنتر خارج منتقل خواهند شد و به ازای هر 1 گیگی که خریداری کرده بودند، 3 گیگ اضافه خواهد شد
❤️
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8520" target="_blank">📅 17:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8519">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">😼👊🏻.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8519" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تست کنید، منطقه ای وایفا
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8519" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8518">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این پروکسی های تلگرام هم داشته باشید فعلا با مخابرات و برخی اینترنت های خانگی متصلن:
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
ممکنه منطقه ای باشه، بهتره تست کنید.
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8518" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎁
بفرستید واسه دوستاتون
❤️
vless://27d6de57-240b-400e-a036-192608ae0459@mbv.followern.ir:443?encryption=none&security=tls&sni=tino.protag.ir&fp=chrome&insecure=0&allowInsecure=0&type=ws&host=tino.protag.ir&path=%2F#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصله رو وایفاها، قلب بزنید ببینیم چندنفرید، برا دوستاتون بفرستید که وصل نیستن تک خوری نکنیدا
😶
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8517" target="_blank">📅 17:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">درنظر داشته باشین که فعلا درحال حاضر تنها وایفاها وصل شدن مث مخابرات و آسیاتک، شاتل و... اونم بصورت منطقه ای، مشخص نیست اینم اختلال باشه یا اپدیت فایروال باشه، پس صبور کنید تا همچی مشخص بشع، فعلا اپراتور های همراه مث ایرانسل، همراه اول و رایتل و... وصل نشدن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8516" target="_blank">📅 17:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8515">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
پروکسی متصله، رو وایفا و مخابرات منطقه ای دوستان عزیز، اگه وصل نشد تو منطقتون ذخیره کنید داشته باشینش، صبور باشید شایدم اپدیت فایروال مشخص نیست هیچی
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8515" target="_blank">📅 16:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.21.7.21:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو وایفا و مخابرات وصله
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8514" target="_blank">📅 16:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8512">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مجدد بستن پهنای باندو
😐</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8512" target="_blank">📅 15:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8503">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw4zm-b4g0Wl_qRXesjxPJPujrIOrppewb52pD5iQOehx8jssOxtBRAV3qJx3y1Z72M21RLFQhqzMancYS4B17yvnTwqS3IXT_HvLyUN4DJZnpL8_OsBe2zhOBPxbQbpcVn0tHu8mwNZKNFTAcRICm35-5Vn4THkSvkDIrv5HYw3sP57U9iWmsD3zSHmi0JJzHc87gtaQSjdmeOUWGXhupDt35ec32OylnfzMJ5vDM_yUNvTBAL_RKTcdCtQLKq01kcJJq2Yfh2yMtoY5p_5mIFI9KT2DM7NJY1hM5zSE8XRKDSqgVSQX_1fFen1HMhoMQ-W2Cxf-RSfGN5OtJbDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=130T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8503" target="_blank">📅 14:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8502">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">روح و روانمون بگا رفت، از بس حرفای چرت و پرت تحویلمون دادن، رسما دارن مردم خر فرض میکنن و پاسکاریمون میکنن، من یکی که دیگه مخم نمیکشه حرفای اینارو باور کنم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8502" target="_blank">📅 14:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8501">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlC-FsutHciY6Tccm5c4D7rFVHPHQhmC0UWW8SGh4Z7k2FMnehih95GUb45zjK6jnkUXno7G4B_OA-8Fe6Mvt0Nr_X984jyZ3AmDLuVIGUCynEF_rVssFjIuitDXnl0bgqIeiYkRvHC9wv5RkSw0K2QoHCGsD2u2odXfomlR23fL0NLs5tGHeqJc-i9Xoyrsmey847glGjbyV5VJCkLlVJVwEv0nO4IDPUC3lLCMP7jqj_4eqsGzlwhkQtCTsF7VGrK37TNJcrqapx0RY5YDiAm97CXPBALCnq0nMCutLoGfdipm2qmwRGKjX-sd-hU2qjhGakaQYxsrlnyjc2dd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا حتی ذره ای تکنولوژی سردرنمیارن با اون کلشون
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8501" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8500">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرگزاری فارسی هم این موضوع موقت تاخیر در بازگشایی رو تایید کرد، درکل میگن که فعلا تاخیر خورده اینکه باز بشه یا نه
😬
وقتی مملکت بیوفته دست سپاه همین میشه دیگه، هیچکس دیگه هیچ کاره ای نیست
🥲
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8500" target="_blank">📅 14:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8499">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رئیس جمهور کشور اگه تا آخر هفته اینترنتارو باز کرد که کرد اگه نتونست بنظرم استعفا بده بهتره چون نه اونوریا حسابش میکنن که ترورش کنن حتی نه اینوریا حسابش میکنن
اونور دنیا رئیس جمهور یه کشور ناو میفرسته یه دنیارو بگا داده بعد اینجا رئیس جمهورش اینترنتم نمیتونه وصل کنه
جدی اگه نتونستین وصل کنید خودت و کل کابینت بنظرم استعفا بدید یه موز بزارید رو صندلی بجای خودتون حداقل فایده اش اینه موزه پتاسیم داره ولی شما همونم ندارید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8499" target="_blank">📅 14:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8498">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فارس: چندین نماینده مجلس که عضو جبهه پایداری و تندرو هستند درمورد مصوبه شورای فضای مجازی شکایت کردند و دیوان اداری دستور داد اجرای بازگشایی اینترنت متوقف شه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8498" target="_blank">📅 13:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8497">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پزشکیان داداش نقش تو چیه دقیقا تو کشور</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8497" target="_blank">📅 13:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8496">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iriO7_RiyRDMjCmo2C0Asvn-9rYKTcvE-3Z-AE2Bdz53T49RgLpbnjzH62ZGcY9tGHlcLkhTk1-QtNsqE-BdZjmeipXkiXMsBWvMYnc4-NfB2MlSI-kBUzQ_PWqPmxx8C5vtMPadb0KB2nVx6f7Vo_btHq0ngbU7RfrZdA4DuchMkza96q05ysTtZH_OkIOY_7i1MXzIvRgKRrJhq9BdfqaWxaFKd11wWM0bKsnoN_iSJhJYdvqysJJJ5PoIetAWvTXTlZqRxFCiTI9zbfWHeDEv6nJrBYHOq103EitqlJ-UN3eddIgUd_e_h_XvjyZ6gfvsvcMheH6lKBeJgIBG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارسی هم این موضوع موقت تاخیر در بازگشایی رو تایید کرد، درکل میگن که فعلا تاخیر خورده اینکه باز بشه یا نه
😬
وقتی مملکت بیوفته دست سپاه همین میشه دیگه، هیچکس دیگه هیچ کاره ای نیست
🥲
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8496" target="_blank">📅 13:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8495">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">در پی شکایاتی از مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»؛ دیوان عدالت اداری دستور موقت توقف اجرای مصوبه را صادر کرد
😐
🔹
مصوبات و تصمیمات ستاد تا زمان رسیدگی نهایی به شکایت، قابل ترتیب اثر نیست
🔹
دیوان عدالت اداری اعلام کرد، در پی طرح شکایاتی…</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/IranProxyV2/8495" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8494">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">در پی شکایاتی از مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»؛ دیوان عدالت اداری دستور موقت توقف اجرای مصوبه را صادر کرد
😐
🔹
مصوبات و تصمیمات ستاد تا زمان رسیدگی نهایی به شکایت، قابل ترتیب اثر نیست
🔹
دیوان عدالت اداری اعلام کرد، در پی طرح شکایاتی با خواسته ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» مصوب ۱۴۰۵/۲/۲۲ رئیس‌جمهور، هیأت تخصصی صنایع و بازرگانی دیوان عدالت اداری با احراز ضرورت و فوریت موضوع، دستور توقف اجرای این مصوبه را تا زمان رسیدگی به شکایت مطروحه صادر کرد.
حرومزاده ها یعنی چی، هی پاسکاریمون میکنید، بخدا خسته شدم دیگه
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8494" target="_blank">📅 13:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8493">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hClaLvh7yEAF_sL4yMwl7Eijlh-cwcbZ7UeqkkPoNsjwe4y-lVnEzSjE6cT4-2IxCvIhTheWbE0P8TQhMLPj1JlckhPX5D7PuOEJYqLncnWlEPpgsCP_EznAbtZI__O-97W4_vaUewypOPNOBC2gCos-fswW7_7k9xs3RXZh6tggQMV15V_Oz6i1h1JDJzhrmMHMsr3LD6XHy63HQPJmP4jKMHb-10CwWqgpvH4t1WsrgbP5gMEt_69T_CoytPR4ll2KDQGbhFZm-KfEcddwOzZmKzCzzoogsXmnSOLnJJeOe9PnrqggmpPbnsaekEGWgTe_ZQ11cMlSXVfIo4_ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=130T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8493" target="_blank">📅 12:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8491">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚠️
اطلاعیه، درصورتی که نت بین الملل بازگشایی شد، مجموعه روسیه پروکسی تصمیمی گرفته که به همه دوستانی که از مجموعه ما خرید داشتند به ازای هر 1 گیگی که خریداری کردین، 3 گیگ بصورت خودکار به کانفیگ هاتون اضافه خواهد کرد، پس حتما لینک ساب هاتون یا سروراتون رو یه جایی ذخیره کنید داشته باشید حتما
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8491" target="_blank">📅 12:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8490">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستان درصورت باز شدن و در دسترس گرفتن نت بین المللی و برگشتن نت به حالت عادی، حواستون به چنل باشه سرورای عمومی و رایگان براتون میزاریم حتما برای دسترسی راحتتر
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8490" target="_blank">📅 12:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8489">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وضعیت نت بلاکس هنوز هیچ دسترسی باز نشده، این چرت و پرتا که چنلا میزارن رو باور نکنید میگن نت بلاکس گفته باز شده  منبع:سایت رسمی نت بلاکس  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8489" target="_blank">📅 11:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8488">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbMR4zMP27i-Y380aLc-JucOtpAcBx5gLicN9oF_zsIdskv7W2BGjPZ383IwMUlTAhACpUQzLd2ioBSYHmnvgS9X1XW4uONSPm6wqEvstj1N34NlSp2RHyT8XhgawkvOIUM1B_OSJqJg5hrTtARuyshM18y1o02y7VIx8vmVRIBUYEOzWrJ_IhqdORc2rZ7iHGFxd0Sb44Uo7KGn17vh7E717xlp353onWhS5AR43-xDmby0WExpy2dFvwuiz6zyOJiV-AdltQOgOe53HBjUibM22s8D84bMnVuEnyhxASz16pr8zH3Zyk2qKQExCDjnPZczqckL6okc6ghZQ3oxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت نت بلاکس هنوز هیچ دسترسی باز نشده، این چرت و پرتا که چنلا میزارن رو باور نکنید میگن نت بلاکس گفته باز شده
منبع:سایت رسمی نت بلاکس
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8488" target="_blank">📅 11:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8487">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ادرس
mail.google.com
باز شده ولی
gmail.com
باز نیست ، اینطوری قراره نت باز بشه؟
😐
اینکه وایت لیستو دارن ادامه میدن اسمش نت باز کردن نیست عجبا
😐
!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8487" target="_blank">📅 11:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8486">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
trojan://humanity@193.151.132.136:40443?path=%2Fassignment&security=tls&insecure=1&host=www.ignitelimit.com&type=ws&allowInsecure=1&sni=www.ignitelimit.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8486" target="_blank">📅 11:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8485">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhZjrFnQTWA4hcvE99netjFjmdDQ404IRaYR6Yh1jsPw6us8BpcQB9LY-TeFZ5MmQoETphZCYils9eBz_M5QhB6ftxlW7_3ducqoLxtPaVFTntGQ4lBo5DH0aI1lQBAGXorSrh_2pBF4rPbObbjDxZb_KlWYh9ubV9XElhFjyEIXl4b3rBYxpiYSt_PPy9x_8p4yvV48Nhcs_L5t83qUstgJ9lK2XiMUUyfXnT2q85X0smZonWsI-9wNOSlFuvAyYFxr2vMca6ZKefsfHgbdYEKCVPAKVlkCfAJn2LubUKZB-diftpnFYJEQAUB8sPYVo7b9w4CzXZ5ya1lR4cVLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/IranProxyV2/8485" target="_blank">📅 10:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8484">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
trojan://humanity@193.151.132.136:40443?path=%2Fassignment&security=tls&insecure=1&host=www.ignitelimit.com&type=ws&allowInsecure=1&sni=www.ignitelimit.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/IranProxyV2/8484" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8483">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/8483" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8482">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مذاکرات طوری داره پیش میره که احتمال اینکه ایران اورانیوم غنی شده آمریکا رو بگیره بیشتره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/8482" target="_blank">📅 10:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8480">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWT1-9o3feZff23WG09Azzi-C18SouCtLmyfv23La_T6Ega_utZwPA53US_mmL0uRAtoBwxwmokdZ8_IDjFf5wEtpkSiUm8I7HOoI8fHZM9BO8SEeFiFJNxcZgIhjjn4Ns30T3sP6dZcrBNx89GYB0uxseDl0HRt99O_iHk9ymc5vDDzBY2_5HgGFuS0yoC5RFV9aXlejBAvzsvBTiuLh8Bos5_LDlgI1n0Qw3cygQ9HGjucvvppWPE6WrWXCagaACp_ENiiRdxUE--qgIqp9ZDjM3bfu7rlxQcjZMO8xONXkJ285LtqMlGLMf92ker8o5FByC2P_vPMQYxnhhhAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX7_oPdTb_adrCkFshDZi1HN4OQvq9KQ8v1MMPRjMdkB7uReZzjCzykX7DA-SVJSuGSIYUszUxQcypjlj0pVVAx1NHPNVtBSSMxiUWG41vSRflzLEwCuuwIm2d_D7-XAbYKSP4iWZMyTC9TJg4x9gSMjSjlvCXZrA4WMTzEASuHyqyQ5puT-tJOlgNculO74Ci3EPYB5a6Wq4hMcwoPKJaWKfV_fgg4A5TmfynzQgjinIH9RhatJxofa9eJ_GOPV5RTgb3dOF3nMK-eop3SCW6mgoVBgjmj4bEm516gVgg55DqgM_mZQ-tVeOKiliQFOgnzDJkQm2S2kdW69fq176A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8478">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ولی من که فکر میکنم، همه اینا برای کنترل قیمت نفت و باز شدن تنگه هرمزه، که ترامپ بعد از جام جهانی تا اون موقع بتونه باز حمله کنه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/8478" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8477">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تنها چیزی که تو این جنگ نصیب ما شد چی بود ؟
قطعی اینترنت
نابودی میلیون ها کسب و کار
افزایش شدید تمامی کالا و اجناس
فروپاشی روانی ملت
اتلاف وقت با ارزش و هدر رفتن زندگی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8476">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjRrmSf-3GFKkoNpkw8S5TuOT97heFcDHFBVnz3QLdUf2QtDODNWamYKStWsFE3Ijn0LhVTauJUNkH8baQ1y2CbzXmGwyDlskMtfeLdy2NFlbg18N2vsQMdHe0z8vE5-odtNSc0DnatPDjw8oKwCuLx_SPIUEt-hUzyWa-xr5iZhprTAswtTYIZ-T5I90Ohu6Yp5F7YilTgm4SGDS9nu4FRUESY0SWFlvKfqAMpem-CpTQPyZ1kJNS86wA2RonuIFLTt8zgbrMbo8Cj79x5D3P4XgDYunbmHweXgUG0CnYFRefLS-JGDuFZoPHPyOLr30sYlnm4ai6m7aZLL60YhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8475">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgTDP3x4P8r3oSVJl00nbrfNb7eSV8Sz4o4O5K4HrMz2ETLQlC6gLGL5OPuG0-83Mqm6JBNFAskJ9QhU1cqUPI-R0PSFUvjI6yc2MyHP9dOM2jgSAqkiMAeZjti45xeZcVQJWZP5CZ8swD_OeR55CHwpHwIxlrnIS1gjFjt1dxBg2EgFRjcDQuAOe5jGYx7k6fEFVXTmNJZA0IIxtlSimPTC1kUVfRDY7qXtxLvo0J9ki87d59-yxUhyVRqPsisIJNYcllr6SA8c-wWXCxvEoo1IW7VcGIHhURjRMnzIGB2fvCx0f5Q_AnDDYswcLKabh83LN2QLG0DAFhWUgUJLIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
طبق تلاش و زحمات تیم russia proxy بر پایه اصول صدور ترافیک خالصی بدون پکت لاست
⬅️
آپتایم ۱٠٠ درصدی با سرعت +89 مگابیت و قیمت بسیار پایین
گیگی ۱۵٠
⚠️
🔡
براتون پخت و پز کردم، ۳ روزه نخوابیدم، سرورارو بهینه کردم با بالاترین سرعت و بهترین پینگ از الان میتونید باهاش حتی گیمم بزنید، اختلالات به طور کامل برطرف شد و هیچ قطعی نخواهیم داشت
❤️
🍸
➡️
@RUSSIAPROXYY_Bot
⚡️
آیدی ربات جهت ثبت سفارش
⬆️</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHZt3s3k9lZ7_el_kXpffTQDCd5P0SdCL7X2_LKMpYHhzPyFKDLYWUxhPhtDYsu1tzQuMtc0AO4BZe2nsG9ZlDEokT_UUJ2MzdcyV3sOu4FdUW4af9Kxbsf2hZm8jqXa4Br0zzta74M1w3_nel6yve96AeQR2oLWKyn7OGC068y_-CNd3PFu7iRoANf8DTZWeOg9RU6HYNuxkmhFhpLnN3ntKGgw2gKvR8bUH0Buw7y19QvIDFUFDczaV1Cn309uAO0UJaPcSV7lb14QtRAQVhd_z5Cx5BrY28JhqFv-Om2qRoa4L97r9GO0B-sdjPnIFtRbNErGyBW767SA7nyYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8472">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meUiXzpIbjccYHmfcTXfR8mw3hj2nTsgyR8hFZjyllfwfQRZWfSEpDI7SWMAWfv8DaGpu0HaFKK4AOy88a3mZzUEHrF2lhs_P-7vJHKxZxQ-RCig6I_7kfIPudsVsR1MZCZzKwZamVQqYBoI85USNqoZeC-5C14PYqNhUbaeVii5p31tJIyFOxmQf4mmzvqW-tE7psK0GfTdBqx2Zj0sOIAkI5dUgfL-f2lyOttPNCkQsfy9Wy9lP9Lt6p_V7dq1dSYPK98v70LY3P3vhyjPmeyD_R0zw4rOFmAbrtW7ssYPsvKKopoUKbusN14AaRN0mO0pTnN-Lav0Vb0p4tggUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqV3W3vKDY40zlNxUITxognJ4oyugiZ0oQtEDx9MtK1rO_GJ0CsWsQes6mdnlw83MuoU327SzHKgGrT7imYF2bQj3nfQD7RnpqpaufOyekLg9uraRaZUXdFR-cKx3QuavdhUwBG2sk3K-fzpMgW-kDnlmKWC1U4GAHl2sSaj1vOTjIB7_KAoFeN1eIgFRiim2UUDuE-Raj2wLs0XwTbeTVgtZM_KslqG-l1XCpHrIN5VGZRM0GFQd2P4pLq675NqDacWZQF4aXEZb2CCAa8mTUb1zEnJ56fK1Fyt__m22wc2CXz9dIsSDtg2TT6KaCfcG7kbem5p0sn12XL2oFVhSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzbnnIezZ9TTBZFb-T9jWi6l_S3Fxoi0C3d6k9wgVGVc47wgUolX6tySOvaV9oAgmw6SnLue1zlRDRnqbWpwkugvAvSexpHtrUR2GYyXMa1NnuwxRnwG1wY9UOaSmuGTchwwcIjDF2wT7ZoVslCpkCJyHv6EbEo4l3LIpxol32G2mgXJF3wWqNCo3RqCi1MJPXElYhM37Eeczs8fWqz90fKv8JKCSSg-dqeXU_c37D22yxTIIxR1WPO3W93DgGRJ28EDBYFQhcGQ-h935nuJoF7GmdHgmI30vJpxEnuuyOM7PJ90Hb-bO7rlpO6_GzOZCJp9bz8nwhQaNjq_SXNXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0iogoFg8vW_OHK-2XfrzO2C3B-32vCZoxv3Cv7UNidNx2syCC58L3HIXRj8WZNjatKZB8AX4sKMe1N7J7hhA0Ye-CZY6nbJ-Di75KJHQY1jgHkLVBddWgP_i7aeksayagybr8hkchlrylXZuYBSjFnP0BflBLIJXwMhqM0zS6PYchlpkCuP_pC-YVh3EoBPGG2sb1ByaJ87P7PcBBqHp6qyNaOswgThE4DnmldbqapbFCRm3Ts0gk4kJ_mjPGle3C8CxocPXcJwORliyZNZdhTsOTf-fNO83thFvqOAR-ve6AGHRypH302mYusPFK3wlwGjOkNtyxYJJaUthRSvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Trrl0QU83h4tAQ_yPRXp1xOcu6NWvY_crBOlVDkv4pNOu88GBH1ty56XBF3CHXDZ1RWESuMoM2Mu6EXGqGQWH21K-RteK9hQKP6EIh0aN-SEYKxA5QJZ9T5zh_GmW1rYxv6YnS736Vj1d2_x0Y_p9CQmqRTapSEd3z3k0Hh6M_my_juKtjh2u6Hb5XKCyEjNe5KLH1eOHgBlLX5zemvuhq9gRKolVt9-UTBqCl0vRQ3DQAL--_ilCbWyZwvm6GBN9La-XTZyfYasSXyY6GIofoQ6CSPzQHxMig45_4bo9dztLKWHJQ-FASgrgELBLIPM2DVSpXrDcIhow15MRy0RtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار داده شده و حجم مصرفیتون، حجم باقی مونده، مقدار دانلود و اپلود و تاریخ انقضا کانفیگتون مشخصه
2⃣
پایینتر لینک ۲ تا سرور با لوکیشن های متفاوت قرار داده شده ، خواهشا لینک هارو از جایی که vless نوشته تا جایی که vless بعدی گذاشته تا قبلش، سرور اولی کپی کنید و وارد v2rayNG یا هربرنامه ای که دوست داشتین بکنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sb6MLDwBNfVysKxlj8bXn7_TtlzNWt3uFyRjG7W38m56q5it8HMfhptdd-iptozxrmM49qiwxk1SWb5iMAVLQvXAIBeytasA74-QS8a8Vx3cAuVJDDd0YhVlXVfNKpdn0lZg6KlK-9cy-MyAlJrG3PKWBcL45Nk-zXMwjYMZ8iEhD1CjIaZwpnmSehZDU2n91luJMmkDBZnsVKpTcS6WL5LswlY1sC4tgLEEZzGyi0eThvWSZrloFwLlm_z9UfdOrV_tJNgdKoPKbx0vo_V9Gxuyg_4Qqx0q-OOO83dNjpMxVDyhYV_B2hEh8tsuh-SYEgrUrUoZ0Nt7D65Ubrhk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APoor5Ug3UO3NoElnBvap6hrU0jjEdMZUEe7jBQuI9tMcHa4GklFlVhfh_X0IuSwtOeAS9ZMbFDyr__zFWkY20rVdzMkij-cXT37uU_gxztGoa2qgTKboTUa3Aotatvv3bEw5iC2RbLuOrzpi4hbZdUfLxtqEdfdFmgGzu9PQi7-CRGGTxWTZ3iU21eF-Cosc-eum13t2wUuVQqtKviVpsFxJxNZaxjHczOukjIKdPy2-5PjCQr0_ZQlbzK7Wo2xdlUBUm7EtE0Jiu0M1Vn3z9cslsXlLPW9QQ8wuwvUYOw-jSYQn12r5slxiQKQjXdWeV7Gxq6O2TFEkYq9ZAvrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=CtavZanuU7lQy6SQsW0Rzr4sdq22JlfFqm_2eTBooeOJROIqXkCLloWjy23oKTbSUxL-cjo0nVItyvtrLUGXCY7Pm414zkeSbeQZQyk_dvQqvhmtLvr1a6qliKmBdU1a-Fsi4U6uTsS5bKINj9AIV7B0aJk-8f_XjeP_O6j45BNQR7ZLyZRRe9zQkDshA3J1rzGhZtmkkZb_VaBj4FqFHveYRRX9s2qsO9JiKQvdkHpk67oi4vWYBbdGrCF7eeqivqYU8H0uUtLU60w3D5oJS46zMyQ4D3T5FD6xaQouTtP7en0BEGyVXWRW8KTWIPbEUr1z1Snn0VPBTpeAE5I6xyDOe8ZZx-eVhocwvaJC--P8pP1ypfvqKJhqFiZPCAFlV6SSwzMPhT4i2RLI4cp0LdWBepEoGfwEPK36SNAOjPM7--Nn00Umxp4ZHtQJgz89hDNJGjy8CJOl9WPvyoIFJ20g1WBCv_7t7pyzpp22BD0Ln_cutpAOcG0eFTsesxH39BkF6xIokWHRkMbOyX6FcN6GCGf8WCVC5rza6qSk73UMfQdaKe1Vqccy4lVF7xSnG-kon8Zt3JQ2slPVlEGUW7fxoXSdmBvD-EX-XphQET_UCxezGgPfHyXZSL1OWUnOF00KAwEJcFZ5aIM0M_LDi4kEAtIg5vhf4YuKdKx8OPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=CtavZanuU7lQy6SQsW0Rzr4sdq22JlfFqm_2eTBooeOJROIqXkCLloWjy23oKTbSUxL-cjo0nVItyvtrLUGXCY7Pm414zkeSbeQZQyk_dvQqvhmtLvr1a6qliKmBdU1a-Fsi4U6uTsS5bKINj9AIV7B0aJk-8f_XjeP_O6j45BNQR7ZLyZRRe9zQkDshA3J1rzGhZtmkkZb_VaBj4FqFHveYRRX9s2qsO9JiKQvdkHpk67oi4vWYBbdGrCF7eeqivqYU8H0uUtLU60w3D5oJS46zMyQ4D3T5FD6xaQouTtP7en0BEGyVXWRW8KTWIPbEUr1z1Snn0VPBTpeAE5I6xyDOe8ZZx-eVhocwvaJC--P8pP1ypfvqKJhqFiZPCAFlV6SSwzMPhT4i2RLI4cp0LdWBepEoGfwEPK36SNAOjPM7--Nn00Umxp4ZHtQJgz89hDNJGjy8CJOl9WPvyoIFJ20g1WBCv_7t7pyzpp22BD0Ln_cutpAOcG0eFTsesxH39BkF6xIokWHRkMbOyX6FcN6GCGf8WCVC5rza6qSk73UMfQdaKe1Vqccy4lVF7xSnG-kon8Zt3JQ2slPVlEGUW7fxoXSdmBvD-EX-XphQET_UCxezGgPfHyXZSL1OWUnOF00KAwEJcFZ5aIM0M_LDi4kEAtIg5vhf4YuKdKx8OPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M07svZFcmh9fUqKsDstLZ9W3EPIvzLRvkPMYZkTGf4jz53_gL9W63e65HOX99QU4ImzbDhjg6izaKkRRbSMTGmAHG67k786jUuViUaY9OyGjnwV88VAQY9f5ceslbQB8BS342gaQmZ0Nw6wuHIHDVKtdX3yLfcW9VUjLV74FnUWEuXoGjJ_tbzpaATcgZedB0pIWmFwiL57BnHTUPGEu5MGVCaQah1p5tApjHAU2qAhKmtekvlSspeATSbqg6WF2lNHubxFrLOadcPiFrc1oumHspNm97oB5xtRG7pHyTeec0JOcuvDcKs3txnYNCH-HT3oGk6EK5pDxXvctQa06uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy2KxX2AH9c_j0J2EuyHvpBA-Wx3tz8ygIt0I3nyP6gH4pcSLKHYzXTAIJ9eos7DcE_8iQhamLcAA7_4QugyHkt261DMf7iFh3Gk3D2up10SHcSif5I9HAfGcLtXqSipxUAseK7ALhzfm0UayS8AhsSthrKLboIX_46LG9Apqc_2VWU44wJk1vRIVooKWz5qVC0WvrRzACxNEMl86mIfaKsB6eDQWLg3dTewbUC0Fg4oSdShxgDBrgcYa1WI-UgqUtsWz0wwAvWknXvF_pk3wEeeXRSvWHx54Y6W0cjD_FQyMDBPzqOfDrUTiq4R003Bs_tpmNLZmqJd8ZPDN6Nchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRVn5KC_1QOTM46N_GYIuhJYn6lSoQIrT6_5twyaKLdVmmdvdIqUUfXDdEBwhcMU4Dp6-ppUWkQj65WlUsqVBN0JW_WeWiTV-3BZCd3BjaEUVS4wAjpLSwt2odb1rJgGbDobcS04Esru5a9_tlbREwrGopHueX-kIrp5Ip4Y9-l0bPEGZgSyYtMCUQelEPGk1tdE0X00HJikpFJqCDWGKoNjhD-cAA1lXq18BNx-4lOnvu3ZatqHTytfi9UdCpAdiB5xjxne9KrGXMGnorxoJPqf6oz1IOBy1Y6g_SqKK5EWl5Q5nRu49RObaYHC5PmTjUtMf6CUMEbp6Ed26KfVeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=JUGPIZbSfFTdTIPgwgE54J4sV4TPpUQ14hy31k3qsIMWlU7Rj1tchj8fyHCZXFIknx8LWYvC9c1SfkVrFXy4QfDSoXWkq8obgbBrE9EqRM3U2jWDp3lp9Ig7_3i2L3KWk-pJUpuCCoDG9hYrC8eSo-__rzTLPI-5IZEXSiIUtQsFKtPVnwYU4uWE3U9fcyb-5U2-P37mNmnIgXfhh0L4ssw80Luqe-n-H6B6dcw3ouh3jIPfzLEp-CJ3qqoiff3GKMlrDZkuhTORXLMKGJ7g_EKw6HefyfxNh4nrGVL4GIhDwJABTKaGX48zJ-wbOno-W3ciK2kbsLpa4D7WdGKsarpQWKLe-RC-yBqxupivLJDLPE2ILLkrcRZ_45ZRTdYDzFlMwWWUxATRSJbfHh_yOsMNY_GNia7XV0605ANVOEOGPN4QkJZXyL-eST7dJd0D3wIpg3OOKqDcin72zx4wVUU-28nWMHHbebLyJfIMel1REIArS4d_qcs3_CKMLfZsHdt_J_bmUqji-0ewha_Ge6Dhy-1TfZ9Yd7zBnASt7mrK6yo7ri9VANrPbEwZWD-lYMs1Me6pO8735lmY_g-P3oLp1pWwIPQmFbePo_BEc7-I92sL8Ts0GMymHavr2D0rr0ITuQ_7ptsxG0LmsYfSsTyAoBe7Cu-EVu7mVhhIAjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=JUGPIZbSfFTdTIPgwgE54J4sV4TPpUQ14hy31k3qsIMWlU7Rj1tchj8fyHCZXFIknx8LWYvC9c1SfkVrFXy4QfDSoXWkq8obgbBrE9EqRM3U2jWDp3lp9Ig7_3i2L3KWk-pJUpuCCoDG9hYrC8eSo-__rzTLPI-5IZEXSiIUtQsFKtPVnwYU4uWE3U9fcyb-5U2-P37mNmnIgXfhh0L4ssw80Luqe-n-H6B6dcw3ouh3jIPfzLEp-CJ3qqoiff3GKMlrDZkuhTORXLMKGJ7g_EKw6HefyfxNh4nrGVL4GIhDwJABTKaGX48zJ-wbOno-W3ciK2kbsLpa4D7WdGKsarpQWKLe-RC-yBqxupivLJDLPE2ILLkrcRZ_45ZRTdYDzFlMwWWUxATRSJbfHh_yOsMNY_GNia7XV0605ANVOEOGPN4QkJZXyL-eST7dJd0D3wIpg3OOKqDcin72zx4wVUU-28nWMHHbebLyJfIMel1REIArS4d_qcs3_CKMLfZsHdt_J_bmUqji-0ewha_Ge6Dhy-1TfZ9Yd7zBnASt7mrK6yo7ri9VANrPbEwZWD-lYMs1Me6pO8735lmY_g-P3oLp1pWwIPQmFbePo_BEc7-I92sL8Ts0GMymHavr2D0rr0ITuQ_7ptsxG0LmsYfSsTyAoBe7Cu-EVu7mVhhIAjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=jP0ax_5NUt87Q0-jZyJr8YDsmGfX5OHV_T2GWLGiBcztADWY-Cmfg3vAlfHjqBEmOx2P1zsq3_mNJjzxEqIT0LJGPH4KbWLE_sqCAwqhJ87u5Zrm0PFw-UsfaRNt_4YSTy6gSzkb4qoqpmN4ngtK7HNFL0aiVHVr7kIivSmVztlCZm8YwSmer4USLWLSGvPpT9QozdY1uA7rSY1O6cRu6NSZ0zOirtk9CmPR9I1Bt1YF3IHOf7GCmapnhBewA5rYSvmPDDhRPiACjUfrVvvDsuBrZeMoL_cQCpRR3_2LSr09nClV06ijFpVkACORFn2fYNBsg1tToelwlc8j7zlvW6DPaH1jI_JFjE5xM-eCcB-y5GPC1YSB2E2bkCJ97Z_1ifB1erBTeZPcEadP6xM_avDKiVhPao3DIi59lAj9N_N1Yt8rBcaeP3oZLLArVdzKtwyyAvQeEMeTNXXDDSUi5lOfoY3nuiEawMbLbqVbb94W_yC_LR3IRbEnc4Ruoh-2jTSiV7BR3-Hw4yV7NK-ljCOeUNOemNUI6aQ6gVkOZIGAfj2-K6WbnuvhBxG7MRMyZcRitzt_HmOCfPIznXH12RaSrIL_COv73RAzKxBzkkh0OmoqkoEVLTuxpS6qBcJRoo6pB3R6skb2nbJ7hhNA66Dq9nwuhS9OGRab3sPDTvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=jP0ax_5NUt87Q0-jZyJr8YDsmGfX5OHV_T2GWLGiBcztADWY-Cmfg3vAlfHjqBEmOx2P1zsq3_mNJjzxEqIT0LJGPH4KbWLE_sqCAwqhJ87u5Zrm0PFw-UsfaRNt_4YSTy6gSzkb4qoqpmN4ngtK7HNFL0aiVHVr7kIivSmVztlCZm8YwSmer4USLWLSGvPpT9QozdY1uA7rSY1O6cRu6NSZ0zOirtk9CmPR9I1Bt1YF3IHOf7GCmapnhBewA5rYSvmPDDhRPiACjUfrVvvDsuBrZeMoL_cQCpRR3_2LSr09nClV06ijFpVkACORFn2fYNBsg1tToelwlc8j7zlvW6DPaH1jI_JFjE5xM-eCcB-y5GPC1YSB2E2bkCJ97Z_1ifB1erBTeZPcEadP6xM_avDKiVhPao3DIi59lAj9N_N1Yt8rBcaeP3oZLLArVdzKtwyyAvQeEMeTNXXDDSUi5lOfoY3nuiEawMbLbqVbb94W_yC_LR3IRbEnc4Ruoh-2jTSiV7BR3-Hw4yV7NK-ljCOeUNOemNUI6aQ6gVkOZIGAfj2-K6WbnuvhBxG7MRMyZcRitzt_HmOCfPIznXH12RaSrIL_COv73RAzKxBzkkh0OmoqkoEVLTuxpS6qBcJRoo6pB3R6skb2nbJ7hhNA66Dq9nwuhS9OGRab3sPDTvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEDCJ2WqbXwnaJ9ChOJTSDDDM2EkoiJndYDduW_Pwj-AcNvTTTVm36n3LafIROM6Xib2GvyNvbVZTBG875H9opfxnKD0Q-pjK_Rd21VIRJ6tELaFGAySSq7AZ1R6_oQ98vx6DjQrf4T_k_naaScCUz3axHAK0AAXTF4QI1BZGgP6Y4qR1beTH7i18ETwJL_bx-heisPGOIHHKR20eOgh_hK85a2Yc881yU_N-HWRwLbdEkhL5rOvFfI-ZotatBa8WfQ9IOxmLYGM1lYSp36IpAS3i92LXFA_ndMXu1BsTatw-oo6ISCEfNUkQ39Cm1VplwKWD3H2D24E5oik_8ffaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
