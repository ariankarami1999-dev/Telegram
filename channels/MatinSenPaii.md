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
<img src="https://cdn1.telesco.pe/file/lFeoT09pnOBJHJOonf5e-tp6dBhjxgx6XUvJ8G0qAl1xEGiDsUFulGRZbDukptJzrYFJg80LVXAQNV0RF19IziyNzeV61WSIjdmjoJk5NdQu9yk3ioXJAkAxavA-ZL57r3ZjpqNSPh7ZMt4rqXvUYjFLaamdsxI2UbkeHT5ydnP2mcGqQGqpg3BwcP8E-3_GbUszkdpIKxfwZlkbAbx5KqGVKinxF-dT6Vo2k-uPw86U5RbvUxU_kWBZddsbcnqUtC8mvfVp1szgA7YSBuQq5kXzsrL3ZMy-h2-y8OqVllukngc2fWGN6YJIZth-3-YLm75uV8iQUvXDAiCDi70lwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">لایو انتخاب رشته و دانشگاه بریم یا نریم برای برنامه نویس شدن؟
🥸
https://www.youtube.com/live/nbOls9zPckM?si=dnW0hyhkqq7wyJ4-</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/MatinSenPaii/5529" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان) با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید: https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/MatinSenPaii/5528" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/udbi3SukRTmH8p5jpgVmVG8A6HxUEtXQTU5l3-LbNhMH5EhjstaafmED5tLp0BGuhBYTPMO6NlGIOss5aYuTGDAUuN8xceS_h-z193aiiGDwq7ygwbX8RGfSxg_YUpsWAtDqxhXCmEOWFuiI_1YgIIOBAxwjH5T2bS7T_4-mL_X9jC5AeZydOxTXYCK3OkJ026mKhu7GZipnbYw93611Aa38v5dbETIn_Bi4ted95vnjXr8h_WLv2_cD_nE-3zIbHz38T8r0aDdAFsQINEmjG3evNhm_Ozi5Z34UBmC9Qu7z6Q4ZzpKvY5F3SL4RD96izGBXCHp63xm3u2AbZs3NsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان)
با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید:
https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/5527" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Matin SenPai
pinned «
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:  1. CDN/WORKER with ECH  برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال 188.114.97.6 استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5526" target="_blank">📅 13:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dT7cSJfi8iAeoWgsWUnMA8jQeUDp399Wxzo57ceJ6W5x2p_gDekaJvVZe_YlOMeFEEajum3ZbmimSC9TSGZcTQXcYbL_CmgM1a15jxolZ42cQym27oXi83u6MPY1nBHcLnF1UmML7oGOWmv7ehSqvsbrkxtKaNgPJ3k9FrxRdBrDoN6OGY9TPf8eWyqJS-wmDNH22HainGEeaalejArMvjzJq7zqZf68idq_7rZL6Fn8G4Drd0VXMS3kIqCh1dJHDkNl34yCblJ_AuIx4t9kuBOK5lZb8DdPiCtWXMVwiWsahxA17H_iDHxs9TVTFIEdCk8fCVyOMW3SdV7i3En3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتای کشور به قدری اوپن سورسه که الان سایت زدن کد ملی و اسممون رو با شغلمون میفروشن که مخاطب مارکتینگ بقیه شیم :)))
✍️
davodm</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5525" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه قابلیت خفن به Cursor SDK اضافه شده که بهت اجازه می‌ده هوش مصنوعی رو حین اجرا هدایت کنی. دیگه لازم نیست صبر کنی تا کارش تموم بشه؛ با تابع run.steer() می‌تونی پیامتو به نوبت بعدی اضافه کنی و مسیر رو تغییر بدی.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5524" target="_blank">📅 08:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم
گفتم به یکی از بچه‌ها دوتا اکانت بهم بده
توی پنج دقیقه بهم داد:) اصلا باورم نمیشه
و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد
هرچند خب استفاده‌ی دیگه‌ای داره کلا.
اگر که اوکی بودش و نپرید و اینها، معرفی میکنم</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5523" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArasTey</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo7r3eToHQ7PzO2drF9IISKBXVuF7PmfNYePr1PG3jZM6ZoFGRj-n6c1hYyDsl9HWZN_sfNjFuZFfLzTLCqDnReBWkD2QYZe-yfFj1QGz1mAaJqu9uRU4sNxNi_2IA1ugW7MjR5NhOulwHf76fuXtv1y9-aTE5FWyZdZirKnYb1LQ_Tf2YW0c_bsQv-czabavwDPMFA8ODyXXWqpQlf_kHPnjSXdT4_XO4pI5mT5XyYSWtIzvj589XYJ9rrbVIkj0RrVpP5J07sx136k3zMomZv-zoNwo8Xq8sQAidCJa1a1WP9nkgLM3ijlQdDKVWZAqn2yzc9HjWBCR131iP95MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آپدیت هم دادم روی
بهینه ساز
که الان میتونید خیلی راحت ECH اضافه کنید به کانفیگا و کارتون راحت شد.
ArasTey.Github.io/cf-optimizor
Github.com/ArasTey/cf-optimizor</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5522" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:
1. CDN/WORKER with ECH
برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و در قسمت echConfigList به طور مثال مقدار:
cloudflare-ech.com
+udp://1.1.1.1
را وارد کنید.
2. CDN/WORKER with IPv6
ابتدا echConfigList و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و سپس از یک آدرس IPv6 به طور مثال 2a06:98c1:3121::7 استفاده کنید.
سپس در صورتی که دامنه‌ی شما فیلتر نیست، finalMask را خالی بزارید، در غیر این صورت finalMask را باید tlshello-0-len (همان مقدار متد f&f) قرار دهید.
3. WARP with IPv6
از قسمت add aether ابتدا پروتوکل را روی wireguard/warp-in-warp قرار دهید، نوع آیپی را IPv6 انتخاب کنید، اسکن کنید، بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال ایرانسل:
1. CDN/WORKER with F&F method
ابتدا echConfigList را پاک کنید، از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask را tlshello-0-len (همان مقدار متد F&F) قرار دهید و برای فایروال ایرانسل حتما باید cipherSuites را روی semi-python (همان مقدار متد F&F) و فینگرپرینت را روی unsafe قرار دهید، همچنین دقت کنید که مقدار ALPN را درست انتخاب کرده باشید (http/1.1 برای ws و h2,http/1.1 برای XHTTP)
2. WARP
همان مراحل فایروال همراه اول، منتها روی فایروال ایرانسل میتوانید از هر نوع IPی استفاده کنید.
3. MASQUE/H2
از قسمت add aether ابتدا پروتوکل را روی MASQUE-HTTP/2 قرار دهید، فینگرپرینت را روی semi-python و finalMask را روی tlshello-0-len قرار دهید سپس اسکن کنید، و بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
دقت کنید در برخی مناطق سیم کارتتون میتونه همراه اول باشه ولی فایروالتون ایرانسل باشه و بالعکس سیم کارتتون میتونه ایرانسل باشه ولی فایروالتون همراه اول باشه.
سایر نت ها هم معمولا از یکی از این دو فایروال استفاده میکنند.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n5FywmdaQk2qSwoQ-_ARTAdYx3CR8Kt_NgZ0N5WZDpJnGDPVysmtZ7oftEP_tHiQb8RaDJquVpIfEwEZDF8YKLn584QowHP0DlhMLg_rkp-F8n3HBTvpMeZCsKM2Jyj57GbXIFUpYs8gy9r8rmJ3I8NFJCKSplkkZZBOFZtG2qjMXNfaXankn8zOKEd419ILnQXSPnNzwXU0fV3h7kHmY1LoFXYGqm-NEBVDhzrXf1PTHAdk3rDDtapOuOhQymnni5Mr0IH5RT9rSvxLTMbPck-6ddZrx4bQzgCujKib6k5ZZ_QjdUoOzrXaAiS2mitZbS--LL2lB5PE5ABwrQvX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a8XG8dk-E2TA4N1VScLT4SFBrPxwj6Y8hHshLRE21DQ4xC0vkNK68rSUGhgVQgfgEeWRAt4nxthziszkyvP5LGxPJSE9E2LTVm5AG9e8DgdMLvOklEWhIdPc_NbVYvd-gYsTMsQ7CuOfhNwiqRqpJbtdIrcLgFjx6T5hf1mTHemUcGIirdlnAZJbUPhVxhWE61nPTXHfXRfNgIf2XCHK91E6HrMWBNYKmXCnoHpoeC9VBsFswY01vXaB9HmjUZjKyoDCXck9IsId8mHrxMZHkRucI21lRU-cJWfuS8bR65PypktBCgWte5YKmbIcCLYlP6tMkeuzw8-UVWX28ErqMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ij6YWTrtur0Te97uBca_7Ku4W9z3riIEijumqe06Sf5_rwMyg1aBM3v8fqdluE7hLvJBBJt5fNPo-3zVw4t46OO2_BVHLL-xyos3nZg4Xkuh-ioggJAAAVeOTS2vD9w3sj67Dx2UmC6xswyRxx5biYf_JrZPKiyJ-QT1H2EYBsw9hnUfg5WY-2Cy7b-XOzoakMdt472xZMG1frwUHEn7z3G_KrkwVSFj6aLKcZ-a06RVq3bpntETsquFGyBiRioR4u0flagcorEZIXNiFMHZZ-U7s3lRIN3Z0NbashY0TBrat27zMfjGY-gQEPKvRAShaFcBf-yfTAwoAGXtgveB1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hnt1KkV1Jzu762fuE2NVRXX8hZI0xfXeko0IF8yJcOVp5MPUrPS8LHcxsXu8j8wJA0T1OgE9gkXXrpfraJdRdnWjlyoIxeB9b2EHa64ckt7ianA986_m4Y9kOW7Q5n-z_YFo-0Cby5BI75TQYUeiNVjJcPQZQn8bc7X4HEn44LRfIRXEmVT-73avqwQv3UHLnPw0aifZlsKA1-3p6UhpWSSSJ4kzx_OIbPzr6j0xvjrR9BnDukrM057H-edWaIrs4gPc6maBV1WeuyH3TIyOwIEW1V8-NRhhvn1-GU1ZAQMl6MG5fxJTdduGlq1RqtEJEQi0MULcFpNGl1x3SmiAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z_rPabP-EHdTQfbRL8YmHjMbWNfStiv0BBCcDha4JKf4Lmyk2Njc7YqhECllUq0W552q19JY-llrMxWVK0fkJTCmdDXQ2IsVTCcAMporJ4hyJ8_mTuWJDODRTc0_zYfw7GQPcDWbpaSMH1NujtMTd0AzvxQienem4CK51hlclw932RSToRV9YQDjnQ9xOGmQiYMT0r6Bz_7I5NqeE5XDfl4AMmspoJAl_xTPV3Vy5_a42aHkGmn53_G46nQbPsNZXD34JAvr9aoWqPrKq_erv8iAwrhuaerk9ePLISRvjTNqAN9m0dMvVqlpsMmU1zIo16IlOpcPL8615NGCMn6hoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RmWcGVsJ3-E7w_sp-0lzak5jLiFXJYVqrCsAoaN2TzPOL3-ZPN5Ki6sBnvx0cigVV6lO71hjTxYwjqk7gJGQI-HXF65sPMnEJFZGN3MTObIt-5avm-3UYsaH2bB7EeguRUDffSFeXi1hHNyEM3olD73rdbRjLxsQuEzI8ZfaCO9166i-42TFk8Lz7zG2bnVOur0NnHA4tFB5LNjbjZKbRX5OJi0bThzhjLyigGC4cMEtXAo2BsPqnB7UDF-BpfWHzpea6EXg1w9jLIczZLF5eAgCQXLlSgZeIlwpXFaTrjr5V8_60LMFfa5Ln_bnfF5FdAAI8aYiolWmyK94CQTcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده.
توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل.
توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی وصل میشه ولی وقتی میرید جایی که پوشش شبکه وجود نداره، گوشی وصل میشه به استارلینک. یعنی همون اپراتور قبلی ولی با آنتهای فضایی. واسه همین اپراتور تلفن باید فضای فرکانسی خودش رو در اختیار استارلینک بذاره.
حالا در مورد ایران قطعا هیچ اپراتور ایرانی‌ای این کار رو نمیکنه ولی لزومی هم نداره حتما اپراتور ایرانی باشه، مثلا یه اپراتور امریکایی میتونه این کار رو به عهده بگیره. اون وقت شما وقتی دارید شبکه‌های موجود رو جستجو میکنید، اسم اون اپراتور رو میبینید در کنار ایرانسل و همراه اول و غیره.
یعنی از دید موبایل شما انگار یه اپراتور جدید داخل ایران فعال شده.
ولی مساله اصلی اینه که توان ارسال از موبایل به ماهواره خیلی محدود و ضعیفه و حکومت میتونه با ارسال پارازیت کاری کنه که ماهواره‌ها نتونن سیگنال کافی دریافت کنن. حتی توی مسیر ارسال از ماهواره به موبایل هم میشه پارازیت انداخت.
تفاوت این تکنولوژی با استارلینک اینه که توی استارلینک امواج رادیویی به صورت مستقیم ارسال و دریافت میشه واسه همین شناسایی و پارازیت انداختن روش سخته ولی امواج شبکه موبایل توی همه جهات پخش میشن و میشه راحت روش پارازیت انداخت.
من مخابرات بلد نیستم ولی اگه کسی تخصصش رو داره بهتر میتونه نظر بده که آیا روش عملی وجود داره که بشه سیگنال به نویز دریافتی و ارسالی رو بهتر کرد یا نه.
ولی میشه گفت توی مناطقی خالی از جمعیت که پوشش شبکه وجود نداره و در نتیجه پارازیت هم نیست، این روش جواب میده چون پارازیت پخش کردن توی همه نقاط ایران اقتصادی نیست.
✍️
aleskxyz</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lwn08fRq_tW2Rnh34AjY10Rh5nolj01NAXmkUPmDAJvGKHBEgejP0qcK3h1RCfPewS4yKjst7OFmHO0jhZpkrWFjhsD7t1C27OOWG6_Vp5U5GA116_HJhkB5DFlMAwlZoqhTcP07UKY2DsxIrs_M2H61opT2toaPf5obkPLpMRwdLVUe1MpqkdVRrjgprzaec_miwLG6P0yU_D00bhWWS-dXbUh9Ydd8qd3iwem6CrC2PmRZ-bVXziyT5WELXEU69i1cojDskwkRbHVp41QaCz6R0rsySGU98OBlg47oBpIMkuyRr_ca6ITDIl3pQBlvJ1PWcf5JJ6hTn_gJO8q-ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/soKU_obZJoI8dcCIIKFToMA-xKMVXYnaEVUzGUtw8SZPdIMbE6MQL17j4aJIeY0NUXpVIH3Ca5m_mLEhQ5fS2miQjnG-l5kCJfoCtN61l2Q_U1qfqh7rfskHYpFWnNjAWnNacetTbn5k9_n5i-EQQoZWhUyEgXsrvY9IzQY8A1QZxsbrrwfp0dMMMte0R14s2hIlaLbba8pO_f4JFvOspJuSCP09-YmyZBTC0ga1RsnCgZrbV1VFDj51CDjVclcVM1HCyuMEFRS58N16xRchHEp6RvUuTHWrTEAmbD3j7Fs6Rl18CQutc2Uijo_M-CkaX6p2gZ5P58EdICYxTsoEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vZpR8s1dBn4SRTTJTJdjITl7E84L37k4-n633w535fjNQG-BOlSgqX8bdubTVoEg74F76o53t9fE1CpjZJ5yfZLwoC-T8tUEEVOrbbeG7TFHx2hwTIuAyfrSgYJqw4UltrDrkLv5aIeg192FewLdp2boqR4vCRWax-ExTTl5xkiSsp5J7CDVaVaXnwUtI5xhHlD5EGiflJsVOnwwa0HO01K4ImIvyYCbquYDyNA1u3YP5l9dRCSCq4NiUpk9A9McPj-vxq4nunb3a1KwQVGGwCZBzf3ygflYtD9JuSRPIsKreQDsvsqSszByClFvJ50M8OJY49HvXd6Zv5sGHYGcKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه SenPai Scanner v1.1.1 منتشر شد
"برای اندروید، ورژن قبلی رو حذف و نسخه جدید رو نصب کنید"
• حالت متنی برای صفحه‌خوان (NVDA / JAWS) و افراد نابینا(ببخشید از اون سه عزیز نابینا که درخواست داده بودن و انقدر طول کشید. این آپدیت رو به خاطر شما خیلی زودتر دادم
❤️
)
• قابلیت Anti-DPI: ClientHello تکه‌تکه می‌شه، همون کاری که توی PattNG انجام میشه. مقادیرش هم قابل ویرایشه
• حالت Gentle برای اینترنت‌هایی که وسط اسکن قطع می‌شن
• Paste کردن IP / رنج / دامنه و شروع مستقیم از فاز ۲
• ذخیره و ادامه‌ی اسکن بعد از قطعی
• اندروید حالا همه‌ی قابلیت‌های دسکتاپ رو داره(برخلاف نسخه 1.1.0 که دیشب فراموش کرده بودم. این الان 1.1.1 هست
😂
)
• نسخه‌ی ۳۲ بیتی برای Termux
🛠
رفع باگ
• تست سرعت مستقیم همیشه fail می‌شد و الان نمیشه
• و Stop بعضی وقتا روی اندروید کار نمی‌کرد
📥
دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
این نسخه‌ها تماما روی گیتهاب بیلد گرفته شدن(مشکل اکانتم به لطف یکی از دوستان برطرف شد) و دیگه شبهه‌ای توی امنیتش نداره
👋
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJ7CyjMjJRb9JjQ3xZc-Qw2OaXGmcmwiD5klLPPh9HcjNUGjVAE0LGhFbbVPzaBOoIZg_GY4rXqjtOTkyhVu9c9lycTb_TJVStfSHn7sw_THFUcWim4HG3qeKeScwx_SSM1S7HbLYF_fXLTrHvf43bAYTmRHYb4LTOQ-4VER_EjaIJddHEfacu6GcNdERcwg4ChqBtStE5fYsL3cQ7q1SenUm-yNuR1ep4KAdncnZrKwBT7MyrwrgqVLFqolc8pQcR_U3uwi1oZteTa2kZO0xdqdUSjO7fQZ7V26CcZvZU6E-gS6Jm_5XSZwbp4VUQpX6cYm-MDJeeufaqg6j7i4_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sRKV7Rdep8-cXyaPIGGnRUAU2VT9TXtAaefRYJBHzQjjeIYrTZx1igMu-CZAasFZkeSY2TPPyCgKUHNpQ2xc2rgiV3PqtJH37LVHg4P-imak5X3ub5SRPe8iWjt3URWeleen6d2R1tf0d8hB3iNXXYZrYPKFMpVsyM376enmxrCo2Dbz5BN_Qt-Hg9G8pbUt22yb2qxt_lcHDZHR7PNy0N7W9nZXej9K4JBlbdMcfLQqcKas_d9nGU893lm-lIuzpcYuUQN3Pvevggr19Fp8niqiLycUW0hB8ffdNgzZ-9OdH_ylVxC3OiQORMme8eIkYVJ0aNn9AS7o0Eyb3M29dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cW34fjnwi-K1xz2OgopkREHCrh43lb3SHqhnSCNvTMj6tIgXzebpfIbHfvX9V3cKgvUHWATNMolvIjbd9MfbcBeX2szNFynHuOh9zWpGRfRujcu7cjZghhP4VLrEw5fNwh1LeHQE06gS7aLER0bRGf-1yfPBFIuphzSgpdlMhUcvHwp98O102LgTEvW33R13GY3p6aFeni92HA9O-2FIXApEB6SU66P7XIoM3dQrPza1cVyHyTyyc6ckhrDGro6DKe9MxYr0eUvscudrII3uxRG98ygboBeeKESU5SNTW7ctk6721zupLSZUtfv47kDA8CPZXgMqx2bjEgCxLnKE3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه دسکتاپ Cline برای لینوکس، منتشر شد
روی Cline می‌تونید از مدلهایی نظیر
Muse spark 1.3
Deepseek 4.1 flash
Mimo 2.6 flash
به رایگان برای کدنویسی استفاده کنید
https://cline.bot/desktop
ویندوز، مک و لینوکس
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=RfMQUpwRJSsrCrvDTXsbQ9qW6dlin1O2lrYvpem83lwfz7IxMdCoWMdSt1p58-cHA3cYdbTuY3H1Xcf6py9zcL0zCVNm65UnlbT_0XCXeBZYmVAozG8Ikb6Dh0p0mUiX6nwMlolbI9TTVkU7_04E2kI778hEmeRWaWbOoUHqqnHMKpPXMy1civhjdERuFcfw_No1vO3VyeFMyHKiGMaTPlaWKRlT-gIKk324dKcxsByFm9hw_RvVrjchvJ1G4gMM-owMHh1YWrX9q7auDnL88yeYqrrFfny_nQBcMTZc_Ns7Hnq_ZgYGhHau4JFIC18CgWFVpS_Kji-EIiOVF2qL9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=RfMQUpwRJSsrCrvDTXsbQ9qW6dlin1O2lrYvpem83lwfz7IxMdCoWMdSt1p58-cHA3cYdbTuY3H1Xcf6py9zcL0zCVNm65UnlbT_0XCXeBZYmVAozG8Ikb6Dh0p0mUiX6nwMlolbI9TTVkU7_04E2kI778hEmeRWaWbOoUHqqnHMKpPXMy1civhjdERuFcfw_No1vO3VyeFMyHKiGMaTPlaWKRlT-gIKk324dKcxsByFm9hw_RvVrjchvJ1G4gMM-owMHh1YWrX9q7auDnL88yeYqrrFfny_nQBcMTZc_Ns7Hnq_ZgYGhHau4JFIC18CgWFVpS_Kji-EIiOVF2qL9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqWXxstgBkFqUwaKkoIfbbJ5WCPXFiV2I3_DxTbhyUVe_hTzF-_ikOtBuYVO_iby9bdTKAu3rEH0Ehpm3H1nb5DB_ntBda_mVHTAjjqrFBB9mQarW0lAjFZrcqt0FF-Z-E7e9Qq15dPnFBMsC2qDmr9GND3DPItOQeHwbyDyVONMlMZiBWRqozEthAzvakJeSwGxCEXepV9W5uDFh-422Uxb4AjUPaWMltGrzOVDaCRaJc7wwXWwWGREVTvO-y2H7PewVO3DJYKVPO16Puur0_7SUfdVRP_nhvbpVVN5_8TvHLayTyfSIaVst6haBwfnmtRC1dzdKDpvRzEbfCxZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S3E0vtj2mUKf8UH9FEJqhWB9P95zw30SUtjrh9Y37NRfFFCKGWR1vPA_81Z7ofETonA_aU_iQRbTum1fzs_jEGWbM9_6YmiExFgN7HpB9m68yS6qFNlJuE7QDW6fQrt6a2UgkNnr39aEyo-zKbGXs_XEcdbE9WxN_0HxM_SQLuVsF-hrEVC-Px1CfcovpACtkeuE_UhqQ8ITTrIMSWm-nQ921z_hQdT0K4uMBbbolLcWYwOQY5-CZ4HRXoi4AIEIkOly8dfSdVBCoTtNtDzHFmKKAQpN9GoKDmQRkS00viL6pruXS8sIf-SVSimiFtwRPMPZMtRRDnHRVHy5MuN8aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gLtVBtcC2HyZQwgelNi6L05tw1DQIL_i4_LZ-9CN5Hk7fziO4ZL95qz8QMa_JvxGbbEwITzEE65rfyNcUiuWCfLXUuhTO2mL_dcbky8pprWow_UYk9pCa9MI3CWQuDSxkpNeIecQooExSwk5X_4Bfu46wFJloBKpFS2EPexUc2Bz8YVEY5nn5aYLfW18ohJdFChS7gpQJITwuw_MgZ8YHBePXA85eRK3RF0Yf49MxLnfgGG9bx0hPaC9Ya2AsSoiPxGJz5TIUQ2DZRjjyusx4tJW7j2KJYjPyeHgNa2dBlaX9qJCgbZ64yAiB6UmAlSseAGW1CpRHsF6Zk0H1OGvmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fe0DzwI3USpIlcwOi9dd5DbbdUf5QB-aQ2w_bgpkVkKhEpJCpAefJKULwW-W2MGeCW8zyXHQQo6hLMxil4v9rJZJi8LZZUV1M3JcmdsTZ8gBUxPBfgZVh9gDfMA-NymsBDFglFVwsGduwIlzt8lUYRN8o-WV2R1oDdi2GuLtdex-U8a1Enj-caZ6Jc-_KHxUJ1o5b0vKBm-QSmqnDHZBznp8gkO_7WO6gJu9qrZQvjj1nNLObaZUhswvIAtblTcbRvO5GVBzsqx3qBXxQliUiVL3BJI8rI3WKd4-msSW2g97NfCMVBIU8-EdvQrdaFlnNOFiIMme4X_-rE6plrXTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔤
🔤
🔤
🔤
🔤
استخدام ادیتور مانگا و مانهوا در تیم تِیلو
😳
شرایط:
1- تسلط به Photoshop(برای ادیت با کامپیوتر) و یا ابزارهای مربوطه در گوشی موبایل
2- حداقل 3 ساعت تایم خالی در روز
3- مسئولیت‌پذیری
4- کار کلین(پاکسازی متن) و تایپ‌ست(جایگذاری متن)
به همراه یکدیگر
انجام می‌شود.
5-
استفاده از هر مدل AI برای بخش Clean، هیچ مانعی ندارد.
وقت شما برای ما ارزشمند است.
حداقل حقوق
به ازای هر چپتر مانگا/کامیک: 60 هزار تومان
حداقل حقوق
به ازای هر چپتر مانهوا/مانها: 40 هزار تومان
نکته‌ی مهم:  پس از استخدام، یک ToolKit کامل افزونه‌ی تایپ اختصاصی برنامه‌نویسی شده‌ی فتوشاپ + اپلیکیشن کلین با هوش مصنوعی در اختیار ادیتور قرار می‌گیرد تا کار، ساده‌تر شود
برای انجام تست اینجا کلیک کنید
🥺
t.me/TaleoCo</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNjgX-fAh8gZ_k5Gg0SR5uFtEawktjgfEeE-jLNs21Z4ht_w7XD6pMIQ5MF-CSYKqtfq27XMWDnyC02xFP7mCfSLTnWQ6L4OdrjpKG5Tt9ZHYldreBz_Qsy5WeVquCRs2zHqwyskwCLFhlipgMSdJLf3GxMnRVVGNneY2Tuyyee1p0X_nJDJuIKgTt-pOrmfQvLG8FUJrBVST5eMsYr6ukJB9irVpU5GRTSZZy2E7kIlSpn6CcgH24izfumBUcDzYoXv736Rs7QQzPPrqSTNllUczVMQZTSnTC-Vez-sxNdApAQmykIi4OR1Paw6nmMdWVN5xr1dD4uFYS97Ou_6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YrgvNwnaU9babAR42rT_jRy0V5yj7Ju9KPnR9MLcZ33-T3OnHEuu-cd1Bw0knXfthPl0FjQKDgUb3I9V2gzYQoIbEnhPTLIs_ud2_jyOCzFbNA6JGCYKVj2I6UDCk5-IJ43cJUJshwkvJ9f_HZqDUEjBUwqqelFcbBPNccKTTfenOHksKzGvrSpk9l2TOLJWJo9HcMp1c8jq3o5NH6WRMzHeMkA5MkKukVdoMXbeHKzDvpjaMr_tNcydjRorLDVyL4o7SxsgEtK4uezNO3ZZELbM2gxIJJp8XBznjhcz4r033lt_4xU8gx5v5GGlVnj4d_h7R7qkkefn6-AI7OREhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDeq9aO3reSTYFdv76clObdk2nK4qV-UL_s5jYvDkVCS_yZLO2T4HBiLCS-8pQIlpjZM6wJYlCkccykvFTzfHJYwcYW4Ctoh9ue1KH_A5Cc63PrAPxtYiP1er4VDryPYHjztfmxzPzXJ8wlL8G7O_I4syNlFl-sSl4Y653MmUsyjF_KPYMlg4m166uEQfoLaeBEi2Nl6-BNKmVkh5hGPPlD6Z1s2E3V5c4W8PxgyESe-EclZEwD-4bCTs_3Gs3BdU8oQYADTe4SNjsXnI_ufTnWURD-KLfBABc-BOOcO-h0JD4NXNieg2vIArbpwjLO4T9zEQWkTM1cl5bjTR99Tow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PvemfSO8dToPdhI25oykz4rxQvEhJkKdYIL27DVxCMWGCGjOKxYY-hp6ho8igJBBJdXkt9BxKTEv-iXyyjvalc88g0PiPOim_3lkogpmwFBX9aEysxH70_JEPmSHlJA2HfpdlRz__CgB_jGDIkV0LFdgKG5pXK5qvlGP3k-1GDax_peBjn604-C-al8ax7OBKGJs0Q9YMVnl9_RpRywbXQu2G_lBZ_X5pdId7EGDJK1YDq7WN1DsQQY_mwPrm-gi4kAVcuIRrN7uJgkCkmMm39BnCyfIFhZQiipJkB-TQlaHZ2W3wFn7Uah3u1tbdpF1aIjBYj1bDtE4MSVC3gz4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LucFPiueuXgBcrMMVlFGOWrjL7tSTBeuI7rBYkx8L8wSjboqDz1g2N-71aoVdEFEh7hMauO2pjGfydndGECY5JUpFY1SyGhjKLUUXTwtkX4dBYkwGzcU5OkWWYOkM8_FeK2nsqzPxri0SvF3UrbHA471DsG4w5QATD36ZgDQOGVIX0OyDpmLImj6xycdhM-7Rjz8Rv9YK8yGpAKS7eNHzqowOKvh86x3C6Ps1kDcHFiClBeY15M7YOs4UiGAsApQByR5L-smUC8tVlkwH7Ab2TpevcNmNl2Ifp3tT_66A7_Zy-LctO6SchYmixL9xMHT61mPm0jnFVdnrmPll76ymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ixYgdzLvPQ11uQVBxv7ogulNNxb4YQtSOURSDppiHtxoyJb2W3Hco1wLdXEMYXRlRN44ymO81h-q-KutinCVbhjsVmP9iTuiDr18VNwMu7L9yRXNbM6e7cgg8JNQs2G7ozpMJih2rNfyQkbFslNXNZgcjTtGg7edmutrInJ5EI5yAmaGiPOLeHDD1tQnjxTmufFQ8IVQ-Onrc0XFZYoNR7FUO5SwKXpMX94zwaGcK0C3rIJMzx3vvlN81OCPX_bNprLKTQTrP8WkQvwY3WAupPIPMeSeS2uPc6mG-fOOZCEpLp50AsSQaKNxLRPyrNyCOTiP7bVf90isikJi0RB31Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jiX-GaTl_n2hpVqiohbJU1ZqRHhwcePi56BUlTet_L2ZTT4kFIwmId6VzFmKTBLZjsGjjQA4dJMKTpuH74ksxNgba7LEYIKyCtHL9SF5ZIWwumq_s0yX4e6Nbuq00rRuh3ASVhcSA3EOpCuhFmcWp7CTlcQ3ZEGPkOlOw9ws5DEFuOJKSZcgvOERBJXHcZoAVwv0T5rNtc-KLtPbtr9OWwsotuumKWqcpSF-Ij-Nd1mPP-Fditpm7F_SM4EZxcZ2CpGGsbGV0wYrU_U_K8f7QUpBxpuBDqukMe0XSabR2t4ca4uRw0S3K-IOL3lVT5Z3x97gVUaREp0zltXT32FGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv5rgkiGFIF5z-G1rV5dUT38RVgcIzKUa3W3pRvQ2uHsEbT04sRcNGTtTDkTeZnUD9OyDkfrIHj0v6o4aHCiu9sS7V_0kC-Mtr1fBWW7kaqSVBZsxf_Mw41zwrKbqU-kWRWCr1_yBjAtiD68rDq9ZW_TsABp_Nr1HV4U9ic0Sf_HErMIN5K2suvt9_A78rNxpEf-tbegHBV7xMRFnLBg0sLgUzsvMnRkOYxStw-TMw6Flct084uVMyJM4Ke7eT5HdPlMKXY3S6FlpWxLXsNnqaHqnb08OiIJ7dbjvxp6bza8GUerwxOayRGiOPQcsTbyvJ90czbl7HgCuXqTK-B0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m6_fnAxqxFMs1I7gFcuKBFpo9O0Si-8dGbSnAf25EQ5aZ9wUy5NneTmlUgUOwU3cBmRwu9lRHnc3oVogP_S4UhasCDVtCQZzQZ6fF5PwKR7JGLkF0Snl7d7n-lEf07rDtSzS1J7M2SPOmPCU-V028Fte7Rd6J72c2sNCVuYr7Xv5K1r_Hq2o5FQtE5g2qzpTsilaUegaQATbymJQh-LprEUuRPW9U_F4_4k--Mad_6hCaI-EAaL8VAD6ic0janFdCD3o8OLIMVvQS_Z8zAKOSczfN6ggvdLNsY4QviJQ74y-SP2x2SlLbNRObt4i3mUsvh8Rmq-v97HN0czo4Ad6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)
1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا
https://github.com/patterniha/PattNG/releases
)
یا نرم‌افزار PattN(برای ویندوز از اینجا
https://github.com/patterniha/PattN/releases
)
دانلود کنید.
2- کانفیگ V2ray خودتون که با Worker کلودفلر ساختید(آموزش ساخت کانفیگ رایگانش اینجاست:
https://youtu.be/iAbYpjXyLpY
) رو وارد اپلیکیشن(PattNG یا PattN) کنید
3- توی اپلیکیشن اندروید، روی مداد سمت راست کانفیگ و توی اپلیکیشن ویندوز، دوبار روی کانفیگِ وارد شده کلیک کنید تا پنجره‌ی تغییر تنظیماتش باز بشه
4- توی بخش Finalmask raw json، این مقدار رو وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
5- توی بخش Fingerprint، مقدار رو روی
Unsafe
تنظیم کنید.
6- مقدار Alpn رو روی http/1.1 تنظیم کنید
7- توی بخش Cipher Suits، این مقدار رو کپی پیست کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
8- کانفیگ رو ذخیره کنید و پینگ بگیرید. دقت کنید تمام موارد رو انجام بدید. آیپی تمیز
188.114.97.6
عموما کار می‌کنه. اگر کار نکرد، از اسکنر
https://github.com/MatinSenPai/SenPaiScanner/releases
که هم نسخه اندروید داره هم ویندوز و مک و لینوکس، استفاده کنید و آیپی تمیز پیدا کنید.
مقادیر ممکنه عوض بشن، مقادیر جدید رو می‌ذارم خدمتتون.
موفق باشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq-pU9wvBYcgQdHGbVWP0ijdu6sTPYrejA93kxTyxpUQoiGNviz13AnrTbPNba3G4LlARLDmI97rYri73N-U4htqV6dsgxSONMMNindUK1YU-YI68gNC0KVBlQ2SpJWYFTbvJ6z2UYrrSXallCCyDGGJYgdRatbROmI9zmA8d2FX7NYIFOmTnWY9yAERp5XTp6A8QgHkZ5o6xgSKu6dw7IgpodHczM4zDOIJf-1QRhyWBnY-VAw-jA1M2Djmip3vFxAWv4HwRQgeABcJv7bZNmyUnqHrt-mXAsSs6aG8bDtymNDhVWXg0wkURVM336EZyoj7ICJBcQOaEjNmWwRONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل Airbnb: ایجنت‌های هوش مصنوعی به سیستم‌عامل اختصاصی نیاز دارن
برایان چسکی، مدیرعامل Airbnb، توی گفتگوی جدیدش تأکید کرده که
پارادایم اپلیکیشن‌های فعلی پاسخگوی نیاز ایجنت‌های خودمختار نیست و دنیای هوش مصنوعی نیازمند سیستم‌عاملی مستقل و AI-Native هست تا هماهنگی بین ایجنت‌ها و خدمات به شکلی پایدار صورت بگیره.
خب مشتی یه کاری بکن. ما هم میدونیم
😂
طرح نیاز که خیلی وقته شده
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BkduDqMBwgKiWdPwXz2uGtKetygydXKiWm9_DpqMViBwnG4Bex4OnQJElJh7XqWY_AO34qxG_qj8Apsg2LA_OtEtUSpT3aTM1h0L0I7VPxs0_7yICeDfJMZ8gjnlTXQXP3e1poh37kO9fiVokpNHgdMhAUvHwFCOCwgHizcA_hBBH1gXyJzkMGEmO1RVS-UWsGkA6YsTO8nyDcmagpVownrwwwnHDzTQZ6-ATwS6Q7nDT79HcJqeunIK3SXOhV1v_4Rmr9WS29J6twANkb2seYd9sdBUO5YuxArrOcYhzRFirjvOTCkRQ9lCJhdLeGmWe6uMhw9zVi5TEIFv_PbtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sFzLw-4G_UB8Gj7rZ-1An7Rdodw88Q75873WhExLKDyg9yCFtaZ-pj__yWx-bfQ6_oRVw6CwAbg3EjjI63-HYe4Zksg6xvI3yEkBQFOaORk9AukjqsTsb-OW4jcV20mXz4x25rsWEvcodV5QprXdSlGIf5r5e5Jfic42lyl8AtUTZht6ntwGWLYb0DmXOpfjAj-ZCJV81a6mhBngPmWemYlOCPZGG1TFFKKQcYPXN0axCQloEBjtYG1FtTEPaeVG29eVV0VKzsSFMn7V3n8827w_QlsDk4rxWpWhZT8EBRYSZptR0WgHdMm_eLnIbjs9DDia6Hv0caRIg-vJCypkLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exfHMUmZSdOjeuPSYcah8hOZDGPK0Gy_z5hBhC6nipU0D0QfKTZwcRDwvkN6_T1esubWfz9wmwEAaqiEvhOCpuG8cARcMhf7lH9oO-3diu4N16JR-cWMw6H48_bpWkxe7BQ7qJc_gbhA_iuJ_R59I93U3nUaWZoUrO74bKRD1gtD78ARqnqzAt7wzT9lMv-bwBPVdulNUdiVGQnAPlehJCWmUv4mGX1bF_VdM4lUcYWOOasJWdQv8enlgKtkKoid7R4eU-ajJLO2dshO0DdJ880nA40QdFpFSjm9SFl90zlxMZED60VADXE6OGf6s0zj9LxAFWo65WOmP4Is4a8kLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lwJSqib8MyV_ePX6s3S6IyW07zuzeEu_y7YmZ0XRU5AH0MMD3N0TqIJI6DbkQtK4HfFCaVGJySpRy2XHArUpoQC3PZMhyNZ9CSJpQFcl6EGEfOzsabF_Lqmr8nOE7KnTlOCblGYWRJMtDHkNomRIBNDY-nBu77EgP4YbIjS8Rzm__ybECuAwac-sckn6mjuBSPlAmqAX-h8zQuIxrow3wYrlfH041ER2SwCq3OaE08adoSHG4A1s3pbZ3zLfkLuc_NILMk--hxfl53p2FWg1hiTPbLE1YbuW3M-sxEdH4e9KCQ7iMxS805C1j2ib5bzNJ_Nft9Wn_vFNAap1C5vnbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fTFeu0MtanruGIPFAXCPXvDgW8GSOh49kPTD1NodK31QNS_jCJ6AEYq5OWj78DAgyUAiE6Y8Yu02ECVoHrojv3vb0zwG9MwOe5XUg7RHQodcbpL13hMnDj3-Jbik5FZFwtW8xOTM0tkrjhvQ1elk2hjxckm7agXS0kflIHTAyFo1E5HstJIfwWcwmWuBACHReUbvvolqant9foPj8FxtvSK9sih_zRjSFNbvzHSjWh4bAqgI58E9g2-eH8W0X2JK9h9vzLm6SDJbUO2homquAXZdGN521T1OMFCty8O5FTJDQd2rzudDsVZ7qFcakOHhKxzy_5NrjMnCQv5fHya4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uuA71DH0qpH2TkczAW1DQ2UBHd9V6u76Ni2nX7I9n3St85TLnt7qwHZCcKQZb8zUeap3LEdBtuIq11iMUqMXuUPrpQp-z9IlIxLmKBdSacMEy3GpEoXi7KDSirdIEOODVl8qYdZnaWaModlXF4mLYMIsJQv049Jd2xZTN4XWWQD8Oji7duUrXudnSWSgLSY3P7faX4lmKqorQwfUldpkaoTI7ubbn4A1K-Iqf9w3sSNYhB1T551bBC4mNVscyUK6s0qujt9brhdTodAe1zxcEjsXefZlQqVVbQanDIYj9wlT9gnGKhsa1zOPGA3yUh01zrAk3oFv7Ap7eZhpnsJhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CflYPWCa0UYYooAttZ65ou3OMhCniou15gxGhy9OcDwwROtewrdp2pOgue9dGIE_7VSBLGSLl55Y-Jvf_MUtg4Z9a0JJpMA4i3J3jWcdIAzSt5NiAfXBwFscF3KFWIK-YXyUkvIm1HfEOpJS532fZc9jOnqjktTEyxoJ6foPYyqxppkg-D0FNLTuRQ0MvqgOHU30hDAu9WzPWkc7GklgCB9JhTMQt91lLicthd9w-Woupb94f8OYlhrtiUe1AKVezPjuQS7rsZ0XzHmi51FGOvPeAbWPfJO1v6H8FqVLK33zYUqqgLT8F1AEQkdlrUn101gNYjuDzBGSqv2veGtqMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hY75JCo22sWX9Ct0pYeqGTzdRayju-P5R5v0r5Wlm8H32cIPsOWNdAEuFufRO5vLG56dk7uIzbhOd-BA_m5DwmsakGUCRtCt4QJ-J2q13vKVksHkZnpx8xTu981A2xl59zXikUPcrfOuoqzfNKfQu5FqYcRyIihlRzx25_A5j4AYq6iGSrQc1RqvAJDIdIk39AfBzSDDARyjFdf_i4WHVMJdiQqkyvfVJACE1flBrNTDYuM04hvnWv_IBWrUqNc5AU_mX73ZaVBQbhcVtMFPymLufQwWpiHjQs7dnhaVmGsCz2cJc3nq1a_ivrhFe69FUPbAcIdEBs3CyszSXszQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LwM345t5lykWZI6f8laqosNcl2wsOHgHk-XKu4rQeBwgr3eOonqgmiexc7wk9Nb2T0X5eMDt47oDlboRy-PxE3J8VpaZ0D1n1FrJqq1UUSDbx3aRfdFXnKY83tH_7EGlvXYdtwfESAXqrxBbhUSLI81jeXN20_5WS-1d1cw8gkUueuZadwXUPPvj99IdNgZZeu00t3U6irA8QdsQ7innlDcxUJGDJKNz8ZYm-kzHIeqRHNFjRcgRF9JIC3tWQpjgOzKDbRw9QMTxgSCkPViexcQkCqWdKlNPM3ZvT2BX1Z4RQelxeHGDMKfk5iu2Qp78UtadAEl6lKYWe_KxUQ5qpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kPT29b19LqqVz7GMZ7-uwJJ0En1_DCfgXBKtEb1CQOSIyCFxe207sn6KZU5Gyc50JBdGZA69jxViGXjSGa32h__8HvoDpQuupRb-3MBJkL0ldrtQAx63h4DsFpVniLUxDIWHPJ2WC-8ZXBkppmJtyl1mRWc-1AI90M4CvnyJs9eVfhUo6JqdjZLu4s5hKi3vEP9GLBGyMAc9mhBO7Vj1lz4t1gvZU62kv0oYR_XnKkpjiBrV3jiIGe1UQFjY1_yloHu_QQhxcFzblgcEdYD6rOi-V8TWR8Hv91VRV539M4Dc210QZSwDCMylKK8WpN2_GJS-fWTZv-ooPHrlq01WgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G5Kz2iRzSzv7B-z4btmq6i8ZSUvsxvBWGkVFdLiCzX7yqvlm5XAGQ3v1l3Mt7KwFbBmCO6sAsGjhVkVm74UBujZFGLUB86vXkB7QC6cMpN1HSGJlq63l2X82q3vMdrh5Dbb7rev_MQAhxU9Qlu1Zg-b437IafL4GfkW_P9TlXXXq4ge7swyx7xI2za_ser35G7Q6NbO2guUj4xodjT1H9zFbNJ-NMG9LYWz_nrJVE--CChqkrq_LI8_dslzzuhJrL7UyoNkXNfCalOl16SKgS0vNdBW4a2RurJLfcnKqSHmY90HAz0iwBg28hi3OSQbcoGDc2cvKEdxxm97MSxvvfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=SeAOIlFfJRKRd3v4SVdz15ge4FU6mzqd-pV2Yl7pO675WsPtPDFzL56zDTJeuYv3_aJKJza3p_PWfFRuguQy1DLJZFhHbV1ad7IBuYIvVVDUL1HUjrXX1ZDU0caEMbQYSHuJga5CQ55t-lZftGR4M0qk_Ru3w_yr47tHLhv82Vqrt_G6nTQPBF4rjJFhCmxx8nqGHPQHkG2zsj00ltvPxJ6n4lucu48VpymNhyMjqQAyElPSDiPCpPIW4ZKgPwhESePkl5zTGRvgSMNlvhVdBl7X7wbmVHJQsWRPNu1XUkP0IFCtVzf4UyZ0zQm7J0LioSK_55G_UMEPo9z6P50DJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=SeAOIlFfJRKRd3v4SVdz15ge4FU6mzqd-pV2Yl7pO675WsPtPDFzL56zDTJeuYv3_aJKJza3p_PWfFRuguQy1DLJZFhHbV1ad7IBuYIvVVDUL1HUjrXX1ZDU0caEMbQYSHuJga5CQ55t-lZftGR4M0qk_Ru3w_yr47tHLhv82Vqrt_G6nTQPBF4rjJFhCmxx8nqGHPQHkG2zsj00ltvPxJ6n4lucu48VpymNhyMjqQAyElPSDiPCpPIW4ZKgPwhESePkl5zTGRvgSMNlvhVdBl7X7wbmVHJQsWRPNu1XUkP0IFCtVzf4UyZ0zQm7J0LioSK_55G_UMEPo9z6P50DJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M4V_8VPZ0PCx8k3gdQ2AJMH7t7UxpCcspMxM263TjHtgOK3ru_UZw7mk3Tn1Fr3IOabdXeBqkzbr7yvId4rvuuZT_Y6Ivzz9kl6QIIeg20-g-tMOC_aW-uQGtuY3mFOml4kFwTwsjZdF_iFQzsYG7IVWHVpvP0YPsMjFNPzoJGQTvuUpdXb3gKz2Wv8oBqQ1Cb5l-jlT6r5wcsdtNBck506WDLSAdk9wYYOO_jFAHyzw0Ap2ZQvynPYJ2DXH6b9dBAU-ug-BRtDOYDiQevXHhYOhmlN7btoYg4iWboHCFMo_p-s89r6iEWCMO45W3kVLbC9OpCy9ckjBJ__1ZbyI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری
گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای اکثر مدلا) تولید می‌کنه و توی بنچمارک‌های مهندسی نرم‌افزار (امتیاز ۷۷.۹٪ در DeepSWE v1.1) و امنیت سایبری پیشتاز شده که به زودی می‌ذارمش. آرگون با هدف کارهای سنگین کدنویسی، تحلیل دیتابیس‌های حجیم و کشف خودکار آسیب‌پذیری‌های امنیتی طراحی شده.
هزینه‌اش برای دوره معرفی، قیمت خیره‌کننده‌ی
2$/10$
و بعد از اون،
4$/20$
اعلام شده. با 0.1$(بعدش 0.2$) برای هر یک میلیون Cache ورودی
دقیقا هم‌قیمت با Opus 5.5
باید فردا ببرمش زیر تست ببینم گوگل واقعا پرقدرت برگشت یا هایپ الکیه:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TF0m47BLnao0Q7_hl5tOfDDXQW3AGfZwO2rJYlXY-ylfCrlVE8BM4NNqO0mjZh7fhmQR8B-JbTEklIIvnuzvkbOOdwl9nHx0IE33W9KJYTwxC70N_BInGGCy46beLfuBtVIsmjiPgHZjLyE-sefETPBUH8K8y6kXQCTYduNFyvU48jidJ6i_Qjs3mxL7tvoJVjFQ-pA5SvxQfjuVicyRxnfUHabG-oyyEoavEOhuubnq2LbtQ9mVaA844HJuIazw942dWcbZl3j9lGQ36GZxgtH_tzbvQ0oAiM7Qpac2VzdS3OWitFTb2pvZUphh_o-lV1TNEDpM4ZKXC3ktKzJx2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ujiL5zdM65Xv2B41gp55lnBa55sH1VXfgcH48KdNxKMzbquzcDBi4IKt-wR_Sg1yV_HhEpnHw0b-QMudv8-gXJpYclT9RMUHxZ8teYfTvSNVPfE2MklPhNyHJPYoJeElCLxWtotEnDaOYmaTWQSQpPMSvK3VGa4sxN8I3TVOCtT9lNpW3Ne4W98JjhsXdjr2vXN29u5JLeCkUt5b7P-hO-VqH1c2ZMNjnf1D9zhwxxkMrMU1OPqU05Cxyv7esv9xC70j3a0qvTJRaTIaPlBSeylyeqCTD4EacHZuikk_dPZCJLMtETfZQ2Bkk40xuRtK6e2VKYD5NOzLWQ5rEE3-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-poll">
<h4>📊 کدوم ایده رو با هم بسازیم؟</h4>
<ul>
<li>✓ تمرین انگلیسی با Shadowing</li>
<li>✓ زمین بازی سیستم‌دیزاین</li>
<li>✓ تبدیل کانال تلگرام به وب‌سایت</li>
<li>✓ ایده‌ی خودت رو بگو💡</li>
</ul>
</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ksPwaQWWrg_TH6AAkYF56dDjlXTVOgHzJ_dI5ulQb8uL7R7eGdmzsYA9YwVm9NJ3oBPbMZxQSo_Ue3RLSZVuySwnozg1p3UCh5QJm6NEFqDhieZz8sjvHIV1lcvnP_8mkHCnvcUJvK5y4xN32VpS-ICKIBE15E9_DAdVaSmUy4DLq58inUrVcD_OJRkvugtStuU5pdjyID2fPst31Ef_qCbH5Bq1rA2RAf5lZ7v-dgLJzt_FcZ99G61-RwOyFc7LOs1Dv_wDjdN_8X2-1LxkxItNDdcrZwgWfjUGv77vYMut-oQqBO0vSGeCJvu2RwqdyIM2JZIGjiNaFgmTIstJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/swVaPZufH7miJobSJIuXUiE37ZCY6Dc_Ts87TuCULV4aJ25DFE7brWgepPsZ1A7iQJmV9b1IoUfanQiiasNtuddGl9VmQ--xM3ubswC4SvV0PUme2yf3Eg9KYgAK4zkwPMycM-pFySWK3xSk8tpFZXJO104Zkspzw0XhqpyaktfeBomZoPS46MpE_M6_BwK1Q7Lbsrpcp0apQvxBIieEXs-OVNSm9_3zbRItkoFiLAqMYAF-AUOk_90UGdpU3zXdYaB3z_0ncWgdb5m241ISqEmFklCPXy5yhhgJqQgyGGe5D1nk3pAg2_Wze8siogJERb0-W5od641JXIHO6f3dGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fo5RKyW4mysPS8LCZH80YK-Febq0fRyNpX3MFtDfTS1QzL4lhimlvRz3xO4bmLB97niVw0I6XDpw7oLwuPqmTG9zEHkGc0YYJ9rsbuEppqxhWjCkSL_eOBkdDU1vQIwaHlqCDjTxQ8x65XLHp073G-uHAKgPKmpVyyi5zduRB96nyebd2RHpLFC1Nn-_jKpg3iIlJmeOF_oSUpo6I56hD2jvEQJEYhTcq1-_kDBcKx-m8eKbxC-mbsj81irdgCIXXLq0IrM0cMAASB6sPeuYx8IKsuxp6JDILDIB4QIhwFYKxKjOsdDO5wuJlQT9m5dmYE0WQ5rgRGq1wRJRLtGGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AS43lOpcvMXDIfj6ixs2jg1WpN9BmLCp3b3demnmMq2-_IYEEiCI24TxF3VEf59z7NAQX4_xj3IimC0PYeP5Gm0NQZkSB1CA_eYeEJ0vlklzedqGfdFje4hx7n2t-LPBv9P1WdisJKvIf7RAmLbBk81Vm6lOOvb4v2EKPySoPMRnKaTHTqSTtyNVVHvKJALfxI9qU5Eo5okO3pQ-N8yJU63BD03tlLuBESUdO6Sv7ryL9H0E0KwfLxrLSXUeptqsldC9ctgai6zUxKRdDm0fZSq6XRLKDcXOVbtsK8qezZJ38B1wN8fYa99BoQv_ZSFFFtVJeLEPdr6LTUz---oMog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=gAl2hXW-zhk8W04sUvG7kijDbnhGmzWM9uzwkjW1a15L3UdMlT1vtaVIzDAtpveBdhUFAoOdsKoE5e8ANjQ0t74NV2DMcHsl3qBnnaYUcgLvYxwZhIdsz7G5mEk7_VWZokscv9A38WNJXf3G2W7VIQJgDtwW5-i6IqgJJDtyNKYW2tgzsh-htHUGaCpAWE8FcV4-BcUFcy2ceJC4ZQzcO0leAcH4JKecRE_9MdkZKWg1yKGzsnTAY9HCgQ65EDTZeuVckGWW3pzw3s3Sd71-QKK643SGDne4887qoQ7l1dcElrqVrWz8b9XepG3v6xrrZrnpiWzf_XuRkL72f1bLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=gAl2hXW-zhk8W04sUvG7kijDbnhGmzWM9uzwkjW1a15L3UdMlT1vtaVIzDAtpveBdhUFAoOdsKoE5e8ANjQ0t74NV2DMcHsl3qBnnaYUcgLvYxwZhIdsz7G5mEk7_VWZokscv9A38WNJXf3G2W7VIQJgDtwW5-i6IqgJJDtyNKYW2tgzsh-htHUGaCpAWE8FcV4-BcUFcy2ceJC4ZQzcO0leAcH4JKecRE_9MdkZKWg1yKGzsnTAY9HCgQ65EDTZeuVckGWW3pzw3s3Sd71-QKK643SGDne4887qoQ7l1dcElrqVrWz8b9XepG3v6xrrZrnpiWzf_XuRkL72f1bLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XcHI0r1NjXClU64DHf7di6FBYTsvDAdyJYvwbgner503bZG9MvcP2NMBqNXlErcr_XL5Vwi9GF5ij13kcCLEI7LrHYBjZkb9pTTTCyY0KF6y0TvEoTzWsl_IJdcnTVlLqeOa0GfUGtH3r2Z7KOnrjizQ70cDvcjqMFlfefolMxNNDnw0kknQXb43c-39weiZxbnEnDRlcC-E2CaqqBhPvwViarH746Bxub0WvOKbWoeWH_NQ93Z1y_vBIY2v02o3_oLpmOvY6HRiUZ5c2mko7421_hZh2aVZBUrOoZKwKSjUWEv2gXpLTzts_QSckrdCRKRWD8af8aDpQHsy-OBWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lQy5zDFGaZW-lTvJU40jTiGUm7q-1P9rU13RKPH6L-c3PMrGAXMEjsVL_R78LtoPEG3WBWJ9QJQN2TZvVQtXZp7ELcKkR9kl1BK7A2ECowVC7fdUZyvavJm3HcCnvzRzT0ldChLySoNLexbt4hbWudcLhz31o3hffUaKtwc0AX7mENP7mRiHDzOh7tH9QObYQsiwWDbOMbJSkEP1_sWRAdoAXYM_fLMZ4HgHl0lh6fm-PE7XraLcfwnW0FkSYICwB7WO8s1pHDGNCyFQ9sqX4upwLdv4oVmh1XzkESuX9yBqrs217NHuc6Sj_xVEHb-FGfKi0efCc0_GacF-dZVghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q7RLBjCqAU5CooEA7AhtPh9unsfc7lpIExdM-e5OCk644IvGBslQSsm-AmNsLQ8k0eBW_yKGDD7m3872j6H9SlP3_LMfBLsRdXLLWOdAukZPvAYtgWUufVH7g85z63AOkehlfvCV6XgczbuN0G1H_GnQQqofvWE-vs00BGFiWtEXAvtG_RSwEHAmCe46Yqq7T6TXti7Fvc4GdHXUBSnz1D0vyi-uwfXR_oOWVHo34Zt6-4-5IgbOZbl-RYfB_F35IlPmelW0FtHDKtAIuYNAAJIMJIMDMEmtPWNgJVd7kbnf3Ji7mYCDBNYbnsYz4uzM7Mx7qHZauw0rJkkMDq-PMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XcBe4u_fMTXQ2iNtdIrlDJHSfeEO6XZwLCygQv6kUA0WuVX7DFlxC9kdm74J8QSctYDSgfH_SvRLWFhRMHTA3Lyr-1G4MqOkow92pXcFzzLj1ai9NbirIXde_PLxyf4qJeHnC9UtBCTGCYYK0liNOGBe2AS--v8jv8i75SjDprnsDavbrXE-3aoC51zMhzzfrCUygea2qikMlEkTn5uUYdavbk_GMEgEbuXHLUtFKo6yDV4uCQRW0GDrU8c9kYZEPGUdqZgDdXLircUblCxSkguaMDO-pRPV6iYtYCXSDiow11BIPjYoVKEMcpRb345IwUmsmBWDHtZuDu8u84fP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار جدید ماریسا مایر فقط از روی عکس‌های گوشیت می‌فهمه کی هستی
ماریسا مایر، مدیرعامل سابق یاهو، بعد از راند ۸ میلیون دلاریِ seed بالاخره Dazzle رو معرفی کرد:
یه دستیار AI که برخلاف Muse و Instinct، نه خبرنامه‌ات رو می‌خونه نه تقویمت رو؛ کل context از Camera Roll می‌آد. از روی عکس‌ها می‌فهمه چی دوست داری، آخرین سفرت کجا بوده و بچه‌هات به چی علاقه‌مندن.
مثلاً از عکس‌های خود مایر فهمیده خانواده‌اش escape room دوست دارن و چند جایی که نمی‌شناخته پیشنهاد داده
😂
😂
کمی ترسناکه حقیقتا
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
