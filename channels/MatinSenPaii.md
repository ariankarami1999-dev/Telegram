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
<img src="https://cdn1.telesco.pe/file/jjPIMj1CVgbr1d91qTZw3Kns9JVAoyzqb2Nn7sGqV49iBfUyDvCv6xUItp_RutDqMelZhqQBXqvlYzwZJNuZ9Nq8Xe1mMRJqkVlLcaEAlXULQn7IZS4A56KhzizP6TLtjp_WEmfzsU_xPnosrQRQMldGyVtQooYnxkVkumBi9H_3mQ10XeXTmZTJyOkpdMvTONEoXOCacOV2DwFsYSyrMgk4CEZqSoe08ucD00pFUE1yUEGo1uaY3uBYG_5sue64QSB1j8Vdn-X5nUv8YguFYlwfFKtq_fyKL_9kXduEeJkk1PeEeWLADNmzg3eK-Q4W628eWWEzxzKpeAncpL-prA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 140K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 03:15:52</div>
<hr>

<div class="tg-post" id="msg-3255">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">و اینکه دوستم عزیزی ران‌تایم‌های برنامه‌نویسی مثل پایتون و راست و گولنگ و  تمام نسخه‌های ادیتور VScode و Notepad++ رو گذاشته اینجا برای هر سیستم عاملی:
https://dlhub.465978.ir.cdn.ir</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/3255" target="_blank">📅 00:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3254">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">☠️
دانلود از یوتوب و Torrent با اینترنت ملی، به صورت نامحدود!(پارت2)  توجه: ابتدا باید قسمت اول این ویدئو(https://t.me/MatinSenPaii/3151) رو دیده باشید.  لینک داخلی: به زودی قرار میگیرد
⚡️
لینک پروژه عزیزی: https://github.com/TheGreatAzizi/AzuDL-GC2GD (با استار…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/3254" target="_blank">📅 00:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3253">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">و اینکه اگر Spoof واستون وصله و نتتون اوکیه، حتما متدهای جایگزین رو ستاپ کنید واسه‌ی خودتون. از جمله:  برای وقتی گوگل وصله:   MHR-CFW: https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG  MHRV-RUST: https://youtu.be/7YdJIJloIxY?si=WJgiFKDcCmISyDdB  برای وقتی…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/3253" target="_blank">📅 00:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3252">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb36e0d0.mp4?token=IAMwmBJZDuhm8iNNQtWoCIPrcR1WsqpXRnxONzhqsfEwDMYlVj9mFZdG1f2B4PkBG6OUwMuwkJZsl9-Hg5IhvRmKTgjX8OLnCFP8c_7Zz0bPY5Vgew-9nwvpiAD6tTPaCh_0B9ViE-Hf22Kw4Hu7Y73iZUoxABzV6DnRtViK7h29SugOPgaEX8nqXmEPavLEuB70HwdBWRa_vSvGN7oKQEBPSatGEsVjxncKDPVed30ZMEBkkkaXS4uHf5q-J7L5GvjyXBL0ozf5k5zS6vRNa_dV1r4HATog2uY6e14TiBi9v6FRlnw1oUBIk4D6U8zBBa4-7hextH8jCtdmr-ab3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb36e0d0.mp4?token=IAMwmBJZDuhm8iNNQtWoCIPrcR1WsqpXRnxONzhqsfEwDMYlVj9mFZdG1f2B4PkBG6OUwMuwkJZsl9-Hg5IhvRmKTgjX8OLnCFP8c_7Zz0bPY5Vgew-9nwvpiAD6tTPaCh_0B9ViE-Hf22Kw4Hu7Y73iZUoxABzV6DnRtViK7h29SugOPgaEX8nqXmEPavLEuB70HwdBWRa_vSvGN7oKQEBPSatGEsVjxncKDPVed30ZMEBkkkaXS4uHf5q-J7L5GvjyXBL0ozf5k5zS6vRNa_dV1r4HATog2uY6e14TiBi9v6FRlnw1oUBIk4D6U8zBBa4-7hextH8jCtdmr-ab3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/3252" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3251">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dhe47v6IpyxqoK5dY_fO_OMFzKi8DHkg1BDmvd5KrcJAcCqxHJ9qnJoALSI2GaGUs5GJ2m0U-1MWDN2jWoygNq0N-Bvr4xgdmDNP4ySYakLV4Wl8qOFOjED0veF3nwcvV6m85Qan_wlNvIFoPJZ3OdC6vaGJnUQqqRDmjCtatBZKS1CXKp4ISP5TIEuDB0k-DbgD6GWr_d2BLPUAhRa5_hZjLovczHMDtP8Mae66joLXDu6yDfCuCKd6RG-wmYNuq6BUFzN-td2eEcDIB338GjRvWtqIY93kgUjF0IP2Ep4hp869knrCfk5hpxmwOCHees6G4xtfOaGaGeKYkzc9EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدود کردن دسترسی اینترنت به اپلیکیشن‌های خاص بر روی ویندوز
این زخم رو من وقتی خوردم که با کانفیگ گیگی ۷۰۰ تومن اوایل جنگ ویندوزم تصمیم گرفت خودش رو آپدیت کنه و من وقتی فهمیدم که خیلی دیر شده بود:))
از طریق اپلیکیشن TunnelX، می‌تونید انتخاب کنید که به چه مسیرهایی روی ویندوزتون اینترنت بدید
با پشتیبانی از:
- WireGuard
- V2Ray / Xray
- OpenVPN
- l2tp
- SOCKS / HTTP Proxy
از اینجا می‌تونید این نرم‌افزار متن‌باز رو دانلود کنید:
https://github.com/MaxiFan/TunnelX/releases/latest
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/3251" target="_blank">📅 23:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3250">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">و اینکه اگر Spoof واستون وصله و نتتون اوکیه، حتما متدهای جایگزین رو ستاپ کنید واسه‌ی خودتون. از جمله:
برای وقتی گوگل وصله:
MHR-CFW:
https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG
MHRV-RUST:
https://youtu.be/7YdJIJloIxY?si=WJgiFKDcCmISyDdB
برای وقتی گوگل هم قطعه:
WhiteDNS:
https://t.me/MatinSenPaii/3130?single
theFeed:
https://t.me/MatinSenPaii/3109</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3250" target="_blank">📅 21:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3249">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این متد ناامن نیست دوستان، بلکه امنیتش کاملاً کنترل‌شده و لوکاله. شاید توضیحات من باعث شده که فکر کنید ناامنه، و نگرانی شما از کلمه‌ی «MITM» منطقیه، چون خب MITM حمله‌ایه که هکر وسط ارتباط می‌شینه و ترافیک رو می‌خونه و یا تغییر می‌ده. اما اینجا MITM داخل دستگاه خود ما و با سرتیفیکیت خود شما انجام می‌شه، نه توسط شخص ثالث.</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3249" target="_blank">📅 21:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3248">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VLR34T3awMSa7iEbf4OnYCUHllGff2enCQmAaf1wWL1uFFRxXt46TcRIfG26CxHuoB0RqUjGpxNhloxsP67bFrhuoglIXptW1nhdyl52G7a5CmTp1Qc89NroEbc6geM6JoWNhsqM-lS6bCHWbVIIUIA9tGkN5-c3QPIrlPXjAT128H7lkFzmLIxUK2fYKzzgtsnycOYBNgIYIm9w6PI058IwwFqilI741F2aCMUGu6RIprMxq1KZEUY-jrO79AoeRvae1X0NAJtl4hvLuQsBqjpoIOYROCy0ZYENJ6eC3KifNqM6cagL5y9AAhx-NUftVAiM92lYk8PM8g5eJqlzwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">kharabam
:
[موقت]
شیروخورشید یا سایفون MahsaNG برید Connection Protocol رو بذارید رو Direct یا Normal تست کنید ببینید براتون وصل میشه یا نه.</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3248" target="_blank">📅 19:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3247">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یکی از دوستان فرستادن، برای شیر و خورشید بخش edge ip:
2.23.168.7
2.23.168.47
2.23.168.96
2.23.168.144
2.23.168.174
2.23.168.213
2.23.168.254
2.23.170.80
5.160.13.85
5.160.128.142
31.214.169.244
37.191.76.110
37.191.95.70
37.255.133.30
46.32.31.30
63.141.252.203
65.109.34.234
78.39.234.140
78.157.41.60
80.191.243.226
81.12.72.218
81.91.145.2
94.130.13.19
109.72.197.1
142.54.178.211
178.252.128.66
185.109.61.27
185.137.25.214
185.141.106.238
185.208.175.228
185.255.91.60</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3247" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3245">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03524e951f.mp4?token=h1_SxfKr1gPQy73H9cUNjFAIjCbv68afvqy5hwnG6CEkO0e76zU5iX8o32qJfRS1BMrX0ASlagR660sj1panT08SwfALnjtWwiypJWqd9NAEsQOgViHMAQ3dV9c_LnZQXoNO95LJHaONv1d2GxtxMX34E3ke0XZqEkQiTnUUbdvp1pyyT_qdPCxIvp2KSKIGMjsB5YgT5d_gB6Sh2DkchDcZ3Eko838rbMf0ocpCQgegr4jfmS3DmctzRQNZXR787VgxhZUhlTsJYC6b8SzSVgKVNf_b5m8POCrgdgegaMCQOMVfMdPqFLDia0l9djzhD8YAzCVA7EHxE5j87uwGqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03524e951f.mp4?token=h1_SxfKr1gPQy73H9cUNjFAIjCbv68afvqy5hwnG6CEkO0e76zU5iX8o32qJfRS1BMrX0ASlagR660sj1panT08SwfALnjtWwiypJWqd9NAEsQOgViHMAQ3dV9c_LnZQXoNO95LJHaONv1d2GxtxMX34E3ke0XZqEkQiTnUUbdvp1pyyT_qdPCxIvp2KSKIGMjsB5YgT5d_gB6Sh2DkchDcZ3Eko838rbMf0ocpCQgegr4jfmS3DmctzRQNZXR787VgxhZUhlTsJYC6b8SzSVgKVNf_b5m8POCrgdgegaMCQOMVfMdPqFLDia0l9djzhD8YAzCVA7EHxE5j87uwGqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون مقدار sni که دادم آموزشش برای شما که چطور وارد کنید
✅
(مقدار sni hostname کاملا متفاوته با ip)
نکته:ip حتما باید پیدا کنید hostname فقط واسه افزایش سرعت و پایداری هست
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3245" target="_blank">📅 19:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3241">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">31.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3241" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ویژه گوشی‌های 2020 به بالا</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/3241" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3240">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromali</strong></div>
<div class="tg-text">شیر و خورشید هر ایپی اسکن میکردم نمیشد واقعا هر کاری میکردم وصل نمیشد
ولی نمیدونم چجوری از network checker ایپی اسکن کردم ۷ تا در اومد کار کرد واقعا</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3240" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3238">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fWLNxXifc5uOjMBk-ZwymQ5x6y1arcrJCz0fXAiVJ3T8g_HyXjTcGY8v-Q7KMobBQ-UV6ZLFiYsdtlEL1gEhKkdtTqMXu4YEazz-MLLoGAJ3PfN9jO4jBKQdBRxIMhqhLg0P9Yap2fHWkxYnHIU3pw3nVLkEa8mZBKnjcwYQQHpj96-TKolbYY6aF5beOmpIOhjpeaD2u2QQc12R0KdpyIHKv06ynnUD-Zxiy_Mn69mqYs25kXtSVFQkW5mN37CZM-qnnFSbiZId8FbgRXvUxWyW3274BUBti8aNofboIUBu8R8pdKV7IlAaAYDXzZWrvKHbG1BjA8FNzX1k90fuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kbXyK5ygTSNYuYQbRsv9hgDVtY2zl67cZe0ufv3-kPd6pSWj2aahXbe8_GItp0VDswqCUww9Xb9uHPRIIZ4pxCnghjqQgYu1Hm1dGZ50LMCZkRrt_GlzAXbM1eyc7NjH3FKYDXTvDe8xfGXxWkx5vUzngPiKm1bINAXjYuPU0n9UNqU1JanPH2HKfWrxCkVASrVTUDadiGr1x94xLYM2fICO_dm5ZfBDcA5YYOZ3LGzg-eriblBrrc0agYViCubHk-zAR8hNKvT360IdPGzuW4OUugi9HXqqeGlvkS1_NQxTLlIGYK2fCqnXkNDZza6c930Eryn4jpXFRg_oW0ReYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👑
داخل اپلیکیشن شیر و خورشید با sni های زیر که ir هستند میتونید متصل شید و شرایط نت رو بهینه تر کنید:  snapp.ir  varzesh3.com  digikala.com  telewebion.com  bmi.ir  aparat.com  لیست بروز میشه
✅
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3238" target="_blank">📅 19:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3237">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-text">👑
داخل اپلیکیشن شیر و خورشید با sni های زیر که ir هستند میتونید متصل شید و شرایط نت رو بهینه تر کنید:
snapp.ir
varzesh3.com
digikala.com
telewebion.com
bmi.ir
aparat.com
لیست بروز میشه
✅
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/3237" target="_blank">📅 19:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3236">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uQQqX2JWJTCRy23ntpYyNa6AaUEmRyFPymfS2Z3qhgMNrW-fpGuTt_CaBqsR9I_bxvKBZMGubaa_ZSEHBIN3ELPWC42GHGWwAdSHp0CZjSVbLAvfkh5EQpZfFxAF9LMbyYmVbKwonlXKsGbw6x-lOhOGHOF47E5otts-5J_-dsluvGA2gLW-ul9KU8Lt-PTrq5I2SSfbkzen7OKYTK6q3FxtoNKKox2g68C2eM7yRYS3D0lbvellv4IlfcpqiWxi0rmIfDqLR1kMy9KvF3xLHZXbvpNRxjkW5VNoDWobY68X_uPG9SiSgY2mTlRGAt1DQ4OMkpw2I9mvGsb1TQedDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان من هیچکسی رو توی تلگرامم معرفی نکردم و این کانال‌ها خودشون پول میدن به تلگرام تبلیغ میذارن زیر کانال من توی توییتر هم اینجوری میان میگن
😭
😭
😭</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3236" target="_blank">📅 19:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3235">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3235" target="_blank">📅 19:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3234">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jc4JuDUNG41pA3PD9S8DSo9lGbki_z2_qOmifhqracoAr-LkVEt15jqRH247DRYjyqzBGhLsrN_zbxXFT32AX1LCmoxA84lJZDFVYTpJczDSbnw5XJ9UvtgDf3TwXGs_wiE8T96PeTTfe8XZRfJTX1CMoggPQjrfANmYjNiD4nrIhu4GqdmfNG__IPiJV1SgeFGpht3Y0rOmdxMlFU5I2QBnHNz_BT3J8smdoLe4-yM7Fz5vqlAJb5QN--71q57RXhjEiHY6DysdgiQGCw6WQt4xA8OM_CdWyBE6chvdSJsh7b3YUiR5Mt54U5VDCm76srJx1-8Oba2mrgJrLhYnkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعریف ساده MITM:  در یک حمله MITM، مهاجم خودش را بین دو طرف ارتباط (مثلاً شما و سرور بانک یا سایت مورد نظر) قرار می‌دهد. دو طرف فکر می‌کنند مستقیم با هم در ارتباط هستند، اما در واقع تمام ترافیک از دست مهاجم رد می‌شود. مهاجم می‌تواند: 1- شنود کند (ببیند چه…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/3234" target="_blank">📅 18:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3233">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دلیل اینکه این ویدئو و ویدئوی پارت 1 اش رو توی یوتوب نذاشتم این بودش که MITM(Man In The Middle) یک نوع حمله‌ی سایبری هستش(که ما ازش داریم برای اتصال استفاده میکنیم) و دانلود از تورنت و یوتوب هم که غیرقانونیه
😂</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3233" target="_blank">📅 18:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3232">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دلیل اینکه این ویدئو و ویدئوی پارت 1 اش رو توی یوتوب نذاشتم این بودش که MITM(Man In The Middle) یک نوع حمله‌ی سایبری هستش(که ما ازش داریم برای اتصال استفاده میکنیم) و دانلود از تورنت و یوتوب هم که غیرقانونیه
😂</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/3232" target="_blank">📅 18:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3231">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">چنان انرژی‌ای برد از من توی یه روز دوتا ویدئوی سنگین دادن که الان جنازه شدم</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3231" target="_blank">📅 18:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3230">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">☠️
دانلود از یوتوب و Torrent با اینترنت ملی، به صورت نامحدود!
(پارت2)
توجه: ابتدا باید قسمت اول این ویدئو(
https://t.me/MatinSenPaii/3151
) رو دیده باشید.
لینک داخلی: به زودی قرار میگیرد
⚡️
لینک پروژه عزیزی:
https://github.com/TheGreatAzizi/AzuDL-GC2GD
(با استار دادن بهش ازش حمایت کنید)
و روی گیت شخصی خودش(اگر گیتهاب در دسترس نبود):
https://git.theazizi.ir/TheAzizi/AzuDL-GC2GD/
لینک وبسایت RiceDrive(بخش ساده):
https://ricedrive.com/
لینک وبسایت کولب(بخش سخت):
https://colab.research.google.com/
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از دوتا وبسایت خاص، به طور نامحدود با ترکیب روش MITM از یوتوب و سایت‌های دیگه، دانلود کنید.
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
بخش اول
رو دیده باشید
✉️
تماشا در تلگرام
💰
دونیت</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3230" target="_blank">📅 18:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3229">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3229" target="_blank">📅 18:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3228">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ویدئوی بعدی دانلود با نت ملی از یوتوب هم در حال ادیته. امیدوارم که به کارتون بیادش اگر اسپوف قطع شد</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3228" target="_blank">📅 17:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3227">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این نسخه، با نسخه دسکتاپ قبلی کلا فرق میکنه و بازنویسی شده. نسخه‌ی قبلی رو حذف، و این نسخه رو نصب کنید.
ویژه‌ی مک و ویندوز</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/3227" target="_blank">📅 16:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3223">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه WhiteDNS Desktop V1.0.0-beta2
✅
حل مشکل باز کردن در ورژن های قدیمی مک
✅
حل مشکل وصل نشدن و خطا بعد از ۴۵ ثانیه
✅
حل مشکل وارد کردن کانفیگ به صورت گروهی
✅
حل اضافه شدن دگه ذخیره برای ریزالور های سالم و. فعال به صورت جداگانه
✅
حل مشکل مشکی شدن صفحه در ویندوز
✅
اضافه شدن نسخه های لینوکس</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/3223" target="_blank">📅 16:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3222">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">☠️
آموزش روش جدید و قدرتمند SNI Spoofing - اتصال رایگان و بدون هزینه به اینترنت آزاد!  لینک داخلی(30 اردیبهشت): https://guardts.ir/f/9e2486ea4d04  دانلود فایل نرم افزار: https://t.me/MatinSenPaii/2617 آموزش edge tunnel روی کلودفلر: https://youtu.be/svYBcv4bSzo…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3222" target="_blank">📅 16:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3221">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JCkh_ZBMVXhXMX_Qkh1-93TqLtUoey_w8weLFboPfSO6eMplZ0YN4Eo49kFEv1YiPwpt75G-oNOUDaLpi2_nzjYJvt0CkUtBo6TCwXaF7GWpMbu0-CAiXyfwUGmhlgdWGG9AQK0OM-PckyNEzAZ-fw-T0gfH2tq_5jE6dpN--bnt5GYV1KEfHERm4UlxBT8joftrkDLbyhsYnB4WRCtF_SxqILykce-m9JX91HSPt_pPWG6TupQuv5piJ-iJph0SQRLyiFcfcBPmy_K57sMKGCKF688kM0jJ1oLSarCKFiSiQJYcYT9GwYh0DQFwKhlL2RTQcjeCFjR8wCE8LFPMaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭
😭
😭
😭
😭
😭
😭
😭</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3221" target="_blank">📅 16:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3220">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترسناک‌ترین اسکرین‌شات ممکن</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/3220" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3219">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ThUDXuCXsokpZO4AD0v4lZOsxHzVDvK_sIv7txBgOYcH5ZZvvaIJXLfiW7C5wMZRYZaKsTImV1USbIeMm5wZeSI4sRN-EqNlOyKMZKvivCzxgZIJd3spkC0hjIiT63cfAiRGZ22Xu6xkakIeHI63SJDFp8z7K_WTQfRM-2scrGVFu2BO-iMh55GzSEtB3dNgrsZu-f5e2vtM5Iu1hJ2MbA-hSYCBNhppxNyon_bpQ990flEQJbhYqpGmLaLpibu_skdZ7ABRcWt07sUGKed73Gxry62zUQ_cvNAh868q9FfEBKybkcGglmTSk6cdRQVtLYe_yFuqrA_G0G1UBHgNtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترسناک‌ترین اسکرین‌شات ممکن</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3219" target="_blank">📅 16:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3218">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">آموزش اپلیکیشن Cloak برای کانکت شدن به کانفیگ‌های SNI Spoofing روی مک
با این روش هیچ نیازی به استفاده از ترمینال ندارید و خیلی ساده‌تر هست
و همچنین توضیحات راجع به شیر کردن کانفیگ‌ها با دیوایس‌های دیگه‌تون
این ویدیو باید تقریبا تمام مشکلات دوستان مک‌دار رو حل کنه
لینک دانلود داخلی ویدیو
گیت‌هاب اپلیکیشن Cloak
لینک دانلود داخلی اپلیکیشن Cloak
لیست کانفیگای جمع آوری شده توسط متین عزیز
نکته: برای اپلیکیشن‌هایی مثل تلگرام که سیستم پروکسی رو اتوماتیک نمی‌گیرن شاید لازم باشه یه پراکسی ساکس دستی روی پورتی که اپلیکیشن توی ویدیو بهتون می‌گه اضافه کنید
نکته ۲: متاسفانه این اپلیکیشن هنوز تانل نداره و ممکنه یه سری اپ‌ها که سیستم پروکسی رو نمی‌گیرن باهاش کار نکنن.  برای تانل پیشنهادمون همون استفاده از
Throne
هست
پی‌نوشت: عذرخواهی می‌کنم بخاطر کیفیت فوق‌العاده میکروفون :)))
@khosrow_v2ray</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3218" target="_blank">📅 15:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3217">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔭
خب گویا GitHub دیروز یه بمب سنگرشکن(
😂
) امنیتی خورده. خودشون تو توییترشون اومدن جزئیات رو دادن. خلاصه‌ش اینه:
⚠️
یه اکستنشن آلوده‌ی VS Code نصب شده بوده رو دستگاه یه کارمندشون. این افزونه مثل یه تروجان عمل کرده و دسترسی به ریپازیتوری‌های داخلی گیت‌هاب داده. هکرها ادعا کردن حدود ۳۸۰۰ تا ریپو دزدیدن که گیت‌هاب هم می‌گه "تقریباً درسته". اما عمق فاجعه اینه که هکرها تونسته باشن به ریپوهای سازمانی و API key ها و غیره شرکت‌هایی که از گیتهاب استفاده میکنن، دسترسی پیدا کنن.
و خود کارمندهای گیت‌هاب هم در مقابل:
- سریع اکستنشن رو از marketplace وی‌اس کد برداشتن.
- دستگاه رو ایزوله کردن.
- کلیدها و سیکرت‌های مهم رو همون روز عوض کردن (rotate کردن).
- الان دارن لاگ‌ها رو می‌گردن، چک می‌کنن چیزی مونده باشه یا نه، و منتظر فعالیت بعدی هکرها هستن.
گیت‌هاب گفته فعلاً فقط ریپوهای داخلی لو رفته، نه کد مردم. قول دادن گزارش کامل‌تری رو بعداً ارائه بدن.
👋
چرا این خبر حسابی وایرال شده؟
- طنز تلخ: مایکروسافت/گیت‌هاب که خودشون VS Code و marketplace رو مدیریت می‌کنن، با یه افزونه مسموم هک شدن! و برنامه‌نویس‌ها توی توییتر و Reddit دارن می‌گن "ما سال‌هاست التماس می‌کردیم marketplace رو درست کنید، حالا خودتون خوردید!"
- ترس عمومی: نشون می‌ده حمله به supply chain developer tools چقدر خطرناکه. تو دیگه کدت رو هرچقدر امن نگه داری، اگه اکستنشن VS Codeت هک بشه، همه چی تمومه.
- مردم دارن می‌گن: "دیگه به هیچ اکستنشنی اعتماد نمی‌کنم"، "device protection لازمه"، "Self-Host و گیت‌لب بهتره تا گیتهاب" و اینها.
و نکته‌ی جالب توجه اینه که این جور حمله‌ها دارن تبدیل به یه روند می‌شن چون هکرها می‌دونن توسعه‌دهنده‌ها ابزارهای زیادی نصب می‌کنن و permission دسترسی‌شون به افزونه‌ها هم معمولاً بالاست.
این نشون می‌ده که حتی توی دنیای امروز، هیچ چیزی ۱۰۰٪ امن نیست
📚</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3217" target="_blank">📅 14:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3216">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سؤال: چرا نمیشه روی اندروید به تنهایی این متد رو راه انداخت؟
جواب: دقیقا مثل روش Paqet، اگر خاطرتون باشه متد SNI spoofing هم نیاز به دسترسی ادمین داره و برای همین باید گوشی اندروید، طی یه فرآیند پیچیده‌ای(که جز ضرر هیچی برای گوشی من و شما مردم عادی نداره)، Root بشه.
سر همین تا قطع نشده یه لپ تاپ ویندوزی‌ای گیر بیارید و انجامش بدید و استفاده کنید</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3216" target="_blank">📅 14:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3215">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو: https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3215" target="_blank">📅 13:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3214">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو:
https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری تنظیمات خاص، لوکیشن ثابت آمریکا بگیرید.
با تشکر از کاربر توییتر
Kharabam
که اون قضیه‌ی رجیستری رو یاد داد(توی ویدئو توضیح دادم)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
ابتدا ویدئوی اصلی SNI-Spoof رو باید دیده باشید و راه‌اندازی کرده باشید:
https://t.me/MatinSenPaii/3186
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/MatinSenPaii/3214" target="_blank">📅 13:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3213">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شاید دوستانی که تازه اومدن ندونن. اما رفقا من بارها از دی‌ماه که فعالیتم رو شروع کردم این قضیه گفتم.
من برنامه‌نویس بکند هستم اما متخصص شبکه نیستم. صرفا کامپیوتر رو دوست دارم و متدهایی که خودم یاد میگیرم رو سعی میکنم به زبان ساده واسه‌ی شما هم قرار بدم.
کار اصلی رو هم توسعه دهنده‌هایی که متخصص شبکه هستن و اون پشت دارن زحمت میکشن انجام میدن و من کوچیک همه‌شون هستم و تشکر بسیار زیاد دارم ازشون.
یک سری چیزها رو هم صرفا از سر کنجکاوی یاد میگیرم یا ترکیب کردن یه سری چیزا با همدیگه و صرفا محتواش رو ضبط میکنم و می‌ذارم
❤️
کانال یوتوبم هم قبل از دی‌ماه موضوعش انیمه و مانگا ژاپنی بود
😕</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3213" target="_blank">📅 13:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3212">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هردوتا ویدئو(دانلود با نت ملی از یوتوب(بدون روبیکا و بله) و ارورهای رایج و ثابت کردن لوکیشن sni-spoof) رو ضبط کردم، منتها چون گفتم SNI ممکنه قطع بشه، اونو زودتر ادیت میکنم و میذارم. ویدئو یوتوب هم بعدش ادیت میکنم و قرار میدم واستون(همون که دنباله‌ی روش MITM بود)</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/MatinSenPaii/3212" target="_blank">📅 12:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3211">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر اینترنت نداشتیم الان که اسپوف وصل شده موندیم با اینهمه اینترنت چیکار بکنیم:))</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3211" target="_blank">📅 12:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3208">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">امروز اگر برسم هم ویدئوی ادامه‌ی MITM رو داریم(سر یوتوب) و هم ویدئوی تغییر آیپی اسپوف برای گیم زدن</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3208" target="_blank">📅 09:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3207">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رفقا اسپوف همچنان وصل؟</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3207" target="_blank">📅 07:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3206">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8EXWoV_-spmXN-_3COpc4KC__vzFfeEp4PQAguPsTPhd2q5VBMul3Si5whY21jki-qMVGciHP5Vdw5D4XbBY0_NyHbSfV1yBoc7640dVi2Hqb_s8-ve8QHCbBqgyaJYvPM9tBKjU2z-5Ffs7WbdEjSbRLxyVmqHks_PFkWANjtBCn6eoQtfJkLBATcOR9e3R3wPANCE9NVMymgMH9d8M9u6a9HMQ0f_qFfzaBDPPDsbfznSL1IJxBPpleOmS1Xk7ttCQl0OxiFtwCZQA7lNucvTPnUQ6Uv7EeJuVEafRd4-R0vfz566leJwZImU8pDSm03p7RpgFYQkSop-CHankw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت رایگان برای یادگیری باگ بانتی :
vulnweb.inst.lk
@Linuxor</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/MatinSenPaii/3206" target="_blank">📅 23:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3205">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">خب این هم آموزش SNI Spoof برای مک.
فرآیندش برای ویندوز و لینوکس کاملاً مشابه هم هستش. فقط باید فایل اجرایی‌ای که برای sni spoof هستش رو مطابق سیستم‌عاملتون دانلود کنین.
فرقی هم نداره که از چه برنامه‌ای برای کانفیگ‌ها استفاده کنین.
لینک دانلود برنامه SNI Spoof برای مک و لینوکس
برنامه آپلود شده در تلگرام
لیست کانفیگای جمع آوری شده توسط متین عزیز.
کانفیگ JSON
لینک دانلود ویدئو بالا برای اینترنت ایران.
@khosrow_v2ray</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/3205" target="_blank">📅 22:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3204">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3204" target="_blank">📅 22:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3203">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P6Q-Xgacj44PQHfM1bWtRyJXYSbSY_020UPJwyRSmV8CVdOrYC7euRvhecIpn49jciIliYpyJptcZuPPx2U53czVbAE5OCtDoadx0pqKDOfqZgITPDOWROvCSiJzY6KnxoYSCZuQgFsv4igSI5nF00mdBFPtXGjAwkBjF0a_aWvXdKkj8ESgOE80JCywPW1cXJSCtlURV6Z0ToFMS-J0TZK4GqBZ7KrrI-5TghX4-ZI3NqCXJG-UbLWOLiMhOucx4Jejyw-ooBPbXeuK3O4-h7kJOnJNmwW9j64H1aNTD2nQ1hIhyZg_ZA9dYcMS-JEdK1wE4KaO-eijpkndVr5MWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ارور به علت پایین بودن ورژن ویندوزه</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/MatinSenPaii/3203" target="_blank">📅 21:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3202">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یک سری آیپی‌های کلودفلر وایت شدن گویا.
اما اختلال زیاد دارن
میرن و میان
اسکنرها رو روشن کنید، با تایم‌اوت بالا. ببینم چه می‌کنید</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/MatinSenPaii/3202" target="_blank">📅 20:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3201">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه حسی بهم میگه حکومت یهو باز میکنه این متدها رو که ملت بپرن بسته اینترنت بخرن و مجدد قطع بشه، نمیدونم واقعا. قشنگ یه الگو شده
هر دو سه هفته یک بار یهو اسپوف یا یه متد خیلی راحت برای اتصال باز میشه و مجدداً بسته میشه. اعصاب خورد کن شده. نه دارن باز میکنن نه دارن میبندن</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/MatinSenPaii/3201" target="_blank">📅 20:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3200">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MfQICw6VrnY0l1C8pyHpS4OapfG6Roj9-9ragcwzOBns5H7ozTJPrZp-4O6FVko6ZUAW0yLcBnvsDT_wjRI9CX1ub0w2IlBDFUIt-GM9DTi6hl-5wE6_B1h4gFHvuzHcL8wN0oP-D1LvKiWCHdyzBc3Xz6sCBPdRYXbNFkptgjLWKgRScRU3ILLcpkAfgAbsGI03num-ljT948ZxETI09Ex3zs2zyejslfFZJyjTvqwsWKloDQYB99A8ljW0Tlotp6iGIxTL36uQDl8ADTMCWgQVu3pH1gbJ3aQW8kIlm5rjd7SNb8T8INZT6DYH_V_t7V21UiInLzuqfmD4yILXfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر پنجره باز شد، و از کانفیگتون پینگ گرفتید، و -1 داد و اینجا هیچی ننوشت،
یا مجدد، WinError6 داد و بازم -1 گرفتید، یعنی اسپوف با این کانفیگ json(hcaptcha) روی اپراتور سرویس‌دهنده‌ی اینترنت شما بسته هستش</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/MatinSenPaii/3200" target="_blank">📅 20:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3199">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آیپی‌ای که اینجا بهتون میده، صد درصد کار میکنه روی شیر و خورشید و MahsaNG
❤️</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/MatinSenPaii/3199" target="_blank">📅 17:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3198">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bG0TB6ii9Rpyu5E0f-iqjPP1NkRih4x2HaJ7HXIom2WACUS7q1fpcltlzrtmzCGsYySmeyiVOnSw3sXYHuMkkC6CXgqmkXj-4kCr76jX7elVKCOJim2HjQ8PK2frX7cgvKgPOyZ3PYOc5xRhKYJZJWwr5qfjr3ZhMamo8VmFYdFKj6zP2L7GIkUHwZEC7drIs4Q-JlATKbdw6wmpMbK1K87vqCZ-ml-E-dO3o6d4h8R9purVm-iOJgVODsJb1R11_RquzziuWMw32idMAuoiQ6LiwpAkBqkNTa8R6Knsikdrw04m5KrLhTN-1fbZpKH6uPTn0MPwHBa8JgSVadPSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ رو هم چک کنید، اسکنر برای Akamai و کاربردی برای شیر و خورشیده https://github.com/mirarr-app/network-checker</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/MatinSenPaii/3198" target="_blank">📅 17:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3195">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K8VPP9otm5Sa0I8sXknNUmEY4qHyukOvGUyWWtYG5wzrexuFQYNDrRTzJLpuVU0rYOB0qt57xR0u-EQcRVhAEoTQF7FjWz8518BR3YP5QYRhnqrPDdBjWVLTgepflwpAhsKpe_RPx1HagP0xhgfVJeo2kCqhEAD7hGnyI04mrOilmwxxv5LvqrHLvhNjt_ouG5-YN6-hW_7HsrCGmw0_9GSMCmHV0B-mjtiLVof9vtQongVQJePikH10RrKvHn_4qBiI0ZwaG4bDcpq5Xmd3tRw58KxZ4G3os0urqZBS5tyo0zAZ2vdxoUzA8Aq_-KUUZkqgQW-g2U1w5eVdQhzuBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/MatinSenPaii/3195" target="_blank">📅 15:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3194">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دقت کنید، اگر خود Spoof لاگ داره
و V2ray هم لاگ داره اما پینگا -1 هستن همچنان
یعنی مشکل از اپراتوره. اپراتورتون رو عوض کنید و با هرچی سیمکارت توی خونه دارید تست کنید. روی اینترنت خونگی هم به کرات دیدم توی طیف وسیع‌تری پاسخگو هستش</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/MatinSenPaii/3194" target="_blank">📅 15:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3193">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/MatinSenPaii/3193" target="_blank">📅 14:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h9d-QDSaQjFT8wNHyhKf9WMRSmHsMwjRDAOsjHt5fGg6h2oVRHdvXAs2-dm4879rNvw3ovlgFaMZVrzmgQxJmmKA07Z-OjhGgr61Pr2zx8jo5wX3aowO58Ch4Ca3CkHCT0XG7JcItUNFB_8pzUi6MHujU54PQFh6toYg6S-EHTOmiUp1kb2aubgr47DMKKzmvMBiAdNLwyr5x-eFxe1fmH-x7l4D0WBYCkpg6e_Pmote8e-KhwT4spf0efgNF1ViSTy47ozUkxHodflS38JCEE9jSuRe0msqyjdsDDBEDJvvz8ksg4MqeV67fsozgLTzxSRWRZ58K29rsCynA-_wEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا داریم قله‌های پیشرفت رو فتح میکنیم</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/MatinSenPaii/3192" target="_blank">📅 13:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یکی از دوستان گفتش که روی آسیاتک، خود hcaptcha پینگ نمیده اما کانفیگ‌ها وصلن روی Spoof
یعنی json شما باید همون hcaptcha باشه، خیلی عادی ران میکنید و پینگ میگیرید و بعدش کانفیگ‌ها بهتون پینگ میدن.
راهنمای کامل</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/MatinSenPaii/3191" target="_blank">📅 12:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9a90f10d4b.mp4?token=U1X-00oigNovf55m0o2_YaPV4QpTjHYdZRR241cyZ0-kHA-P3P6o6YG12GMgly33uTcTHklnzGrN11f16PKZ1I59kW4Sc5u-uTeKdRgAg_c3kG0Rv9jHo8BqTTcgreUk4l4yhUibE5PaIc63edvVTmahxhg4ZPqfj0_sgN9o7G3ppWiGOcPDI2SJgdvUfE55uqfbAqCaH_NUuvpg1f4zPJ3mapXKRFdrUhKMIr2SMpf0bcrxiRyN_3_3iwzU2mdZMdtgKP7fz0lP53wRylUzNVrHzSFRPQ4D6HDj0Y6dN5rH3RVVTrKJ84BzCpL8X9Cnv1qkimtI7JjNVidw6fEDgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9a90f10d4b.mp4?token=U1X-00oigNovf55m0o2_YaPV4QpTjHYdZRR241cyZ0-kHA-P3P6o6YG12GMgly33uTcTHklnzGrN11f16PKZ1I59kW4Sc5u-uTeKdRgAg_c3kG0Rv9jHo8BqTTcgreUk4l4yhUibE5PaIc63edvVTmahxhg4ZPqfj0_sgN9o7G3ppWiGOcPDI2SJgdvUfE55uqfbAqCaH_NUuvpg1f4zPJ3mapXKRFdrUhKMIr2SMpf0bcrxiRyN_3_3iwzU2mdZMdtgKP7fz0lP53wRylUzNVrHzSFRPQ4D6HDj0Y6dN5rH3RVVTrKJ84BzCpL8X9Cnv1qkimtI7JjNVidw6fEDgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/MatinSenPaii/3190" target="_blank">📅 11:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✍️
سؤالات متداول راجب SNI-Spoof:
1- ارور WinError2 میگیرم توی اپ؟
این ارور به این معنیه که شما نرم‌افزار رو با Run as Administor ران نکردید. اگر مطمئنید که این کار رو کردید و باز هم این اروره رو میگیرید، به سادگی یک بار ببندید و مجددا باز کنید.
2- ارور WinError6 میگیرم توی اپ؟
این طبیعیه کاملا. باید هم بگیرید. اصلا اگر این رو نگیرید یعنی کانفیگتون کار نمیکنه. همینجوری پشت سر هم تکرار میشه و این اوکیه. مشکلی هم نیست
3- پس اگر ارور WinError6 میگیرم یعنی وصله؟
نه لزوما. ممکنه همچنان Hcaptcha روی اپراتورتون بسته باشه. پینگ هم بده اما کانفیگا -1 بدن بهتون با اینکه WinError6 هم میگیرید. با اپراتور دیگه‌ای امتحان کنید.
4- اگر
Hcaptcha.com
بهم پینگ بده توی ترمینال یعنی وصله قطعا؟
نه لزوما. توی سؤال قبلی عرض کردم
5- اگر
Hcaptcha.com
بهم پینگ نده توی ترمینال یعنی قطعه و کار نمیکنه؟
نه لزوما. توی یه برهه‌ای Hcaptcha پینگ هم نمیداد اما وقتی با اپ پترنیها ران میکردیم، کانفیگ‌هامون پینگ میداد
6- با چه اپراتوری بهتر جواب میگیرم؟
منطقه به منطقه فرق داره. همراه اول به طور مثال یه جا وصله، یه جا قطع. اکثر اپراتورهایی که دیدم وصل باشن، ایرانسل و سامانتل و رایتل و فیبر مخابرات و مبین نت بودش و adsl خونگی
7- کی این متد رو میبندن؟
به قول یکی از بچه‌ها هروقت ثبت نام ایران‌خودرو تموم شد:))
اصلا مشخص نیست کی میبندن و چرا باز شده و...
اما تا وصل هستش کارهای ضروریتون رو برسید لطفا. آپدیت‌های سیستم عامل و...
فقط روی اندروید حواستون باشه سیستم عاملتون نیاز به لاگین نداشته باشه بعد از آپدیت
8- دقت کنید، اگر خود Spoof لاگ داره
و V2ray هم لاگ داره اما پینگا -1 هستن همچنان
یعنی مشکل از اپراتوره. اپراتورتون رو عوض کنید و با هرچی سیمکارت توی خونه دارید تست کنید. روی اینترنت خونگی هم به کرات دیدم توی طیف وسیع‌تری پاسخگو هستش
9- چرا نمیشه روی اندروید به تنهایی این متد رو راه انداخت؟
دقیقا مثل روش Paqet، اگر خاطرتون باشه متد SNI spoofing هم نیاز به دسترسی ادمین داره و برای همین باید گوشی اندروید، طی یه فرآیند پیچیده‌ای(که جز ضرر هیچی برای گوشی من و شما مردم عادی نداره)، Root بشه.
سر همین تا قطع نشده یه لپ تاپ ویندوزی‌ای گیر بیارید و انجامش بدید و استفاده کنید</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/MatinSenPaii/3189" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v3zGQ4b0ndkn4_rOmJH-0Sq71vWM-TBXs7X-9szmWS_f1c3elDrry3Kdk37pfAqbGRveUm4-bpeen4IAsif45xsHD8wx6Scr_CzXavgBx_cyQ_v2kBWEBjVZt_tKdv5PjLxWKcKj8RlXvwXuDiE2b3rE4FCxybON-3Ri5qxt3bCp0MSjCahD-YQpjbgf2GTMU3X_BUEV6xlaf0yXv7tFbZTrdgcGFSTof_pk7Z3ZPqxA3JSH98SbtQ5-wSmvSFkKPVZjBkvt-hncdUEDs2xH9mv4f60gai2pRWaeIotQSPmL30bCsYX8GXWxL8f-mbw7pRppIxNly7Ft9HU_zod9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)))))))))))))))))))</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/MatinSenPaii/3188" target="_blank">📅 10:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Matin SenPai
pinned «
⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:  1- آموزش پایه: https://t.me/MatinSenPaii/2627 2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید: https://t.me/MatinSenPaii/3168 3- و کانفیگ‌های این پست: https://t.me/MatinSenPaii/3183…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3187" target="_blank">📅 10:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شاید شبیه کلاهبردارا به نظر برسم اما می‌خوای نامحدود به اینترنت آزاد وصل بشیییییییی؟
😂</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/MatinSenPaii/3186" target="_blank">📅 10:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3184">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BwJhz-ip_jGbSp8a6BYIDoCMdLCX4Oq1b-l20VMQzcWs5DXmNECsrKFa39NfSo-ukRtCNzpsA9g03C7X9Ng0U3VC2pcAB25wEo0SWpzEYzTr4KhVlLh2Ylpo90TtNJAq6KYCAO9vAZfN_QGtdX-wTU2fKGqNE4yurTSo8Ww906a3_eHPyl6b-It_faBrvCLbHQcX7tul87EaggMwvPfPhI7k6IafopU1uFKpHRSl4jftu8soZYdX64Qz07xbiQsnP7g5W25K6fkoQyzcCJsWyFAfclX8rHrLnrLPShUzT5PKYaWE6Vgy9PyFDjWFsyLXu72pFeYF5WJJcZIjy0Os5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ml9beVVhNi_RhyprZEzjm-VZO88R0bv6AmvF1lhq-9h9fRr0X6b4qW1HvBiT6I_g3L6lu6QeY9pjlMXTni0JW5ghSWOjjbSM3L_fvVcn-Npy-W4YuH7KJSF9kw_0uJ-Ta5dkpDu2TeJA0Vg5UGpaLlvZ2leSXaSCss5rIABX1OiYOIMZF-khz7mGXXwwSalmefTM8OHG2p3RA3LZVt-x9bLmmpWdtgP4DbmrThGJXx0-PjabP9Kq5L6u6L3EGxdQ_w9k56tbxm-pBstU8ww2EREPPEgAFhLtkURxPQw94beb-pDurT0kwHidyFyHy9mbuLmtlSJcd3fY5viVtJp7-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاید شبیه کلاهبردارا به نظر برسم اما می‌خوای نامحدود به اینترنت آزاد وصل بشیییییییی؟
😂</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/MatinSenPaii/3184" target="_blank">📅 10:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3183">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/MatinSenPaii/3183" target="_blank">📅 10:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3182">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اگه spoof وصل بمونه یه هفته قیمت کانفیگ به زیر گیگی 10 هزار تومن سقوط میکنه
😂
این خط و این نشون</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/MatinSenPaii/3182" target="_blank">📅 10:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3181">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خب دوستان نتم رو کردم ایرانسل مجددا متصل شد
همراه اول و شاتل برای منطقه من جواب نمیده</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/MatinSenPaii/3181" target="_blank">📅 09:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3180">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">☠️
آموزش روش جدید و قدرتمند SNI Spoofing - اتصال رایگان و بدون هزینه به اینترنت آزاد!  لینک داخلی(30 اردیبهشت): https://guardts.ir/f/9e2486ea4d04  دانلود فایل نرم افزار: https://t.me/MatinSenPaii/2617 آموزش edge tunnel روی کلودفلر: https://youtu.be/svYBcv4bSzo…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/MatinSenPaii/3180" target="_blank">📅 09:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3179">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mKW7RF7-bT3CTHQwvc_ORGkJ5krX8kZQcfc_vjyNnbpiXtxhV7e-3P5dQLh3kkaCbkxjkCDyCaVNPLrNwrNU8JPrlZ-2MdUsaijftYdHTCl63BBShrl30Ha8rfq3Vc21AQjAkwTrpQBP5HAqsYXYGzoJPgPEVWrG824X6G-brAx4hOQwUvg7vrYq-cyN9OJQsX4FwUvOiKrXg10RzeICGCb7-KoQW-9ZZdgBbBeCEMkfC9TQTEvinWCyUdRGxnhQOVI0r6lFrBeflVWe0M4SDh0Ruwfn4hloTNCa2fwVNHbq9ikpGeMVtSIPi8Dp974ir4-9TgLnp8bpKDKJu9gkjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
اگر hcaptcha بهتون پینگ میده اما هیچ کانفیگی هیچ جوره وصل نمیشه، علتش اینه که هنوز پشت NAT هستید.
حالا چطوری مطمئن بشیم؟
اینو چک کنید اگه IP خودتون رو نوشته بود یعنی باید وصل بشه و مشکل یه جا دیگس
hcaptcha.com/cdn-cgi/trace
‎
و اگه IP خودتون نبود یعنی هنوز پشت NAT هستید.</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/MatinSenPaii/3179" target="_blank">📅 08:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3178">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">همچنان وصلید؟</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3178" target="_blank">📅 03:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3177">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اینور کلا تعطیل شد آپدیتی چیزی دارید سریع انجام بدید</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3177" target="_blank">📅 03:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3176">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o-BuWHqY2Y1goTr-Dgm_kGL-k6WcKoF_N2AyFNjDpvhW70R4LlSZL8TgZ7Ydf7s5VUyk8J0_SV387gJ_427NxUVUi_158fzY64FD748PNrYVxzwHUsagrl1QAbEWuKxzCqooD3UsuzRmFa9a4DItgKvus4JKOv10hy6qZ4dQHZ7bgFT-SgoiJx8QW7pO6VKIuoi-7ZjfIHh0udeQa4v-iC04Cl50nOpPeH9EAX77qTo6vDnWxeb6m-b0IfZp_DrK9dDGeMOdM8-qJHTy1sps9b2lJ9-cHblpAjBw_3rfDG5cK8rWYNtZZCLQJ41DO1z8NVrvaGrzDdqFHCeUdS3ENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینور کلا تعطیل شد
آپدیتی چیزی دارید سریع انجام بدید</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3176" target="_blank">📅 02:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3174">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Spoof-SNI-Configs-List-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">12.5 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3174" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">هرچی کانفیگ ویژه‌ی SNI Spoof با پورت 40443 بود واستون جمع کردم از کانفیگای خودم و بچه‌ها و هرچیزی که توی کانال‌ها گذاشتن، توی این فایل txt واستون قرار دادم</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3174" target="_blank">📅 02:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3173">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">با این کانفیگ‌ها تست کنید:
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&type=ws&host=www.creationlong.org&path=%2Fassignment#1
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?encryption=none&security=tls&sni=sni.111000.indevs.in&fp=chrome&type=ws&host=sni.111000.indevs.in&path=%2F#2</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3173" target="_blank">📅 02:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3172">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یکی از دوستان توییتر گفته تامکت به قید وثیقه سنگین آزاد شده. امیدوارم که درست باشه این خبر
🔥</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3172" target="_blank">📅 02:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3171">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Matin SenPai
pinned «
انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست: https://t.me/MatinSenPaii/2627 جیسونش هم این: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "104.19.229.21",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com"…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3171" target="_blank">📅 02:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3170">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W0bO4Ha9rFbK6PdSv79lAONmNG2OwqJHKjURwTawd2mG6dJTVs1Ona4MD4HQBEfK5N0kDmthlpkpKl_WENE4jRiDIx1RxW7JHl5hLVT2_ISj933UlStaTlY5yJ7h5LKndLbBKBKMCF2oVXzMQMLiDHdYIaER7tDHFD980sFwQVuAaw8Q41DvEKuZTyP3JAehicGjFPGyadNy_bXbhhGS36ayvGMnUgWWm5g3hez6N0JJOlV9uR3jZFjsLhXNYTj1Rnmr-8ZRffOFdO2d06uB0S17FPBY1bTLcQQyIu3haddjpIXuwv_LJMXEsS54jmOppTttiQrvQU5zbExmdoVokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها واسم فرستاده از اسپوف
برید ببینم چه می‌کنید</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3170" target="_blank">📅 01:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3169">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست: https://t.me/MatinSenPaii/2627 جیسونش هم این: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "104.19.229.21",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com"…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/3169" target="_blank">📅 01:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3168">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست:
https://t.me/MatinSenPaii/2627
جیسونش هم این:
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
www.hcaptcha.com
"
}
پینگ بگیرید ممکنه به جای 229، 230 نیاز باشه بذارید</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/MatinSenPaii/3168" target="_blank">📅 01:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3167">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">thefeed-android-v0.18.10-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/MatinSenPaii/3167" target="_blank">📅 01:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3166">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مجددا، از تمام کسایی که استار میزنن زیر پست‌ها و یا دونیت‌های کوچیک و بزرگ می‌کنن تشکر می‌کنم. من قدردان همه‌تون هستم
❤️</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3166" target="_blank">📅 23:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3165">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">Matin SenPai
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3165" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3164">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://guardts.ir/f/19995aceb6bb…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3164" target="_blank">📅 23:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3163">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SMJEoz6kPIaNFSM46jugbeXOGsx3m8mJUMxjzsMU-CGjMx9Hb6Hnp13uw5DQqmjfpwiCh_JyqwKv8PfZjsQFPQd6xhodQl63eTUuaCGXNUL1KN-7Z9Gbgwd0nC0ypkk0c5lOTkrtVhgQlEZ9TYViaF-CenY1j0-BMSK6KYNu9HQGMo5w28DQdDtfPh0cO-7YlPRGM4tDI7lHWuY-WyGzNYHaqLZRyqkc9RfWT36Dqvajfrs0UjQEKA3zBHX4VjPzdgavR02Sv4fy_6utC_Koi8hFEGSPMlm49Z7wpmGAPUQy61vsktjMBF6hAT3BLgDiVu4dLHffv9aJjHY3Uphk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای میت، من با گوشی و لپ تاپ خودم روی دوتا جیمیل چک کردم و تماس برقرار شد و همون صدای Echo گوش‌خراش معروف میکروفون هم بین گوشی و لپ رد و بدل شد. نمیدونم چرا برای این دوستمون جواب نداده</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3163" target="_blank">📅 23:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3162">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3162" target="_blank">📅 23:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3161">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3161" target="_blank">📅 23:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3160">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting.json</div>
  <div class="tg-doc-extra">17.1 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3160" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ورژن 20 اومد چهل دقیقه پیش(توی ویدئو ورژن 19 استفاده شده بود)
و روی این ورژن،
Github.com
هم باز میشه به راحتی</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3160" target="_blank">📅 23:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3157">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">moein.bpf</div>
  <div class="tg-doc-extra">4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3157" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یکی از دوستان این رو دادش:
این برا سینگ باکسه اپ ها هم میاره یعنی لازم نی از مثلا سایت گوگل میت استفاده کنی با اپش میری</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/3157" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3156">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">متأسفانه جمنای و گوگل کولب باز نمیشن چون ما تحریم هستیم. یعنی از خارج تحریم هستیم</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/MatinSenPaii/3156" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">با تشکر از
@patterniha
، برنامه‌نویس پروژه، علت ضبط این ویدئو اول این بودش که مقدمه‌ای باشه بر روشی که برای یوتوب می‌خوام بگم، دوما این بودش که حس کردم این پروژه به اندازه‌ی کافی دیده نشده.</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3154" target="_blank">📅 21:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3152">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">certificate_generator.bat</div>
  <div class="tg-doc-extra">56 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلهای سرتیفیکیت جنریتور(ویژه ویندوز)
و
کانفیگ MITM (ویژه اندروید و ویندوز)
لینک گیتهاب پروژه:
https://github.com/patterniha/MITM-DomainFronting
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/MatinSenPaii/3152" target="_blank">📅 21:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3151">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود
این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.
لینک داخلی ویدئو:
https://guardts.ir/f/19995aceb6bb
لینک داخلی V2rayNG:
https://guardts.ir/f/7ae1503cd755
https://c224731.parspack.net/c224731/v2/v2rayNG_arm64-v8a_v2.1.7.apk
لینک داخلی V2rayN:
https://c147793.parspack.net/c147793/v2rayN_windows64_v7.20.2.zip
⚡️
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
لینک سایت Regery برای سرتیفیکیت جداگانه روی اندروید:
https://regery.com/en/security/ssl-tools/self-signed-certificate-generator
لینک فایل‌های مورد نیاز:
https://t.me/MatinSenPaii/3152
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد MITM، تحریم سرویس‌های گوگل رو دور بزنید.
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
💰
دونیت</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3151" target="_blank">📅 21:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3150">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یکی از دوستان توییتر گفته تامکت به قید وثیقه سنگین آزاد شده. امیدوارم که درست باشه این خبر
🔥</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3150" target="_blank">📅 21:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3149">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عالی بود
تمام 133.9 کیلوبایتی که برای این ویس دادم ارزششو داشت
🤣
🤣</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/3149" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3148">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirmohammad</strong></div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3148" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">rdnbenet-windows.zip</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3147" target="_blank">📅 19:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3146">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XKi0Z7QyAS5Vatf0XJmCzimvyLMDSMk-uFO6KvkHwVurY6Xn1LL70JFa3itiswOnfoCzBiho1wkGuIbmeYREqU2MPHx944rZnbpUBX6sup2bPmcLbo-r85uT2T03EIBpV3GNKN37gdW5f9Mkef2YpW2FK6GV48BbB8K-vbD0FfYUYeyqMADDGKeuupLFUwHas9bx4xzNEi7ZQDJ2EPx87wzkXvsKXKQwZWFeZgcztZUun8E2xdZKXDUUjYi59_nIW3oDOO0xcjA7Kt-Fs6H3mhmOw-H9wqvPzPscVmrnWwqFNbkoqkvnLemPfsDlDswfSq2ef3T57YRDsv_h03hFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه متد یوتوبه زیاد ساده نیست، اما خب قابل تحمله و زیاد هم پیچیده نیست. اون شکلی نیست که بتونید راحت برید توی یوتوب بچرخید، اما خب محدودیت حجمی و... هم نداره.</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3146" target="_blank">📅 19:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3145">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رفقا متد بله رو چندتا از دوستای متخصص توصیه کردن که اصلا نه انجام بدیم نه من آموزشش رو بدم. بر پایه‌ی سروش هم یکی الان دیدم نوشته بود و واسم فرستاده بودین. چون حتی سر متدای ارسال فایل هم اکانت یه سری از بچه‌ها بسته شده بود توی روبیکا و بله</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/MatinSenPaii/3145" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3144">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خب با این اوصاف من آموزشه رو می‌ذارم. چیز پیچیده‌ای هم نیست اصلا
دوتا ویدئوی مجزا میشه اما چون خلاف قوانین یوتوبه فقط اینجا می‌ذارم</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/3144" target="_blank">📅 17:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3143">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-poll">
<h4>📊 اینایی که میزنن دیدن نتایج ایران نیستن یا حال ندارن چک کنن؟</h4>
<ul>
<li>✓ ایران نیستم</li>
<li>✓ ایرانم. حال ندارم چک کنم</li>
<li>✓ دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3143" target="_blank">📅 17:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3141">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-poll">
<h4>📊 بفرمایید که،</h4>
<ul>
<li>✓ meet و drive بسته‌ان یا یکیش بسته‌ست❌</li>
<li>✓ هر دو واسم بالا میان راحت✅</li>
<li>✓ دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3141" target="_blank">📅 17:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3138">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گوگل میت چی؟ :)</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3138" target="_blank">📅 17:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3137">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rRj86nLcxBVepJq0JbO8dLnYikjU8y2zSIUKmSts9metSMc-1IlM7TeYzW_wbtAdOh4OeHTZJSoPKyGd5h-Vb3GC_hfdPlI-ebQ3iOYQac09cZWy40KUqSPXU4Sd6OjKcvO5jEEu1wulH4TOz0fttwpFYY7F-L1UMNR0eLDeN9H03xTeFFla9wEYxz1dPbvUg94Dqa2FJtNiryVD9eXb-5xS0ZuyOZCXzb1vpINQ_3Wrb83X3ifSXZ078K76mEFPeLHhSe9Dy-6WD5evuF_2VVOKjMWlDzW0GraFONPyYVjewO0kHAzNkfkn6q5xhUxD6447JypTv5AO-fvFJcXuhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان، drive.google.com روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3137" target="_blank">📅 17:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3136">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوستان، drive.google.com روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3136" target="_blank">📅 17:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3135">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان،
drive.google.com
روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/3135" target="_blank">📅 16:57 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
