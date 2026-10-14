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
<img src="https://cdn4.telesco.pe/file/X8_YRHetvm-zgeeNh8mVx4Xa8YZufAvKE2ENa9TDZFw67-8AP4L08vaHAfMjplg8x_ktmStQgUyC_oxOFPFMvskOMXY_cI5oFw5-lm7HLlImmRtCrjTRs6C_K1ZyLRT_JgBmUW-FBVpGiOOUSxgZg84hEz9EUdmJmb5-v47aTLwk4iEHsDwQkE3q_ebAWXUQU0zaVTffH8ugcclaJuikrp9r3nt_5IUtamd05vaRtLQMn7oemn67_UWrTm9wlM1DoBbMI-xkuRqEG8kpV5BSmHDJS32ekhVJtGf_rlSunnkAlpzAqXeR56JHkpBxlrJN4h-uUjyI-BswAJNYg6CwwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-1977">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامیرپارسا گودمن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440846a5df.mp4?token=V8Ian-1Erg1ukcMA8ehwQnFt5Qx4MgnzOPx9a7Cjs4uKzjONTFaBidTW4IKHz0I8m7kL1F0TJYu4x9O2dUgfgVRwu5tJhGOxX2SgCHbHbQTxu6rtZ5IC8uG52Q6FOemOU9f0D15oN5N8RV4RZuMNtOTzHmw5P1ZKr-QlCe2KL52QKZ2BQS2uhMNe9oDIWDwlF779ziEntU7UusR-ZddsxbEj2JySj8Hxbmjc4DW5Wd7iOKcxwfYLn_Yo0N3TwJBeeMt9iwfCFc7zMPbMIwbrpJa4jSrUJViQDSLd8LJ8vpZoR_81Tfk2-tjjNpKcRL_UzZBRATZdJkBqZq4kk-QWkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440846a5df.mp4?token=V8Ian-1Erg1ukcMA8ehwQnFt5Qx4MgnzOPx9a7Cjs4uKzjONTFaBidTW4IKHz0I8m7kL1F0TJYu4x9O2dUgfgVRwu5tJhGOxX2SgCHbHbQTxu6rtZ5IC8uG52Q6FOemOU9f0D15oN5N8RV4RZuMNtOTzHmw5P1ZKr-QlCe2KL52QKZ2BQS2uhMNe9oDIWDwlF779ziEntU7UusR-ZddsxbEj2JySj8Hxbmjc4DW5Wd7iOKcxwfYLn_Yo0N3TwJBeeMt9iwfCFc7zMPbMIwbrpJa4jSrUJViQDSLd8LJ8vpZoR_81Tfk2-tjjNpKcRL_UzZBRATZdJkBqZq4kk-QWkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">https://t.me/yebekhe/4393</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/whitedns/1977" target="_blank">📅 00:39 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1976">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تنظیمات پیشنهادی توسط یکی از دوستان
💡</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/whitedns/1976" target="_blank">📅 20:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1972">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from👑𝓐𝓵𝓲 𝓐𝓱𝓶𝓪𝓭𝓲👑</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eT1h1LNecqVMN75mrQ3KrSa31WVHoUQDieY9ncmqEFugkwINvyup-kifE4DlLehMKqUMlIoQwCtz83AadQnBuZkXyzuur9Nwijhn1gTskJrPMqa-6_tGT6TV9atiGaFI3s2ubvskUW73HDQM9rBD4jU_hKv6Hggu0YunMVJFI1pQJl6b6RATBgV0zsUpq-f5m5V5m7RGED412X3Zx6UY3gCHFeKAMmLSd22sihUlf8Q-L5l1PitrbquLlqiD0edHB2XnbPRktPlLClXg59ae1dEfLM1lKyTphSGr6KwbKm1imYp40HQSMwpOe4YleqDTz6Dt4nhWhdbhjGsuQdJH0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTNb_fV_g3QhrO6_alSWjQtXmNIYiI2jmcyMDxhzhx9evTv_JB1Dp0tE7nftjQFamro2Z1P4dcDWOQhUPvEBAUnhVkGdzzx-SjVQWTptBz9owcIXJRI-Kslb1tNksXFNtm1lPaEG8QSX6maIFAMEzcafW-v0yI6RY9h30ysMgkxPG9C6l_aLk4LUt2Ayg1aElQgCrElQgkm-HFa6cyEqmi6kwrfjRDUQ8dFAe-lj6vMV4UjMVE92mDx9r0-lAKTaAFjmEEZ9s5tuZsy8_tvS9dELWmCqtw1MBQs9XmL-cfhn3GB5QAKmIc4sFdmB0O8xmNKWA8rAcsJGWJKzOIfrvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z9-Okw5E_RnkEW2RBNeP6XfAaLsabG9JmCUc3A7Nd4XKWIc1Ff1kYeL239trfOwVAH3vO2GwaKmGVIkKVcapGWqW9vcr7BlaJb7P0kw2NokR25HBF6fyFPCFZfw2pYya3VzEEUTW47NF6o7IjwwX4w91n04KfYz8g3B05uJV-RpfW8jLSbEgxU9Jbr47NJKoyHXlUAJxEkAsY08uMt-Yq6RVk6twZYYT2QaDhUDyP_cp_79vNmGC3ebhqiRvJq70Gq13O33MLZDTf1-OkK_loBezp_QUvcEIDwiXVUgWq05DU6hr_hHOzArRMoqRVpGmcChxrCZFY0Uo_Aol3Cg5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3e7A0CFWKGl7TgZ_6UjohXPKbjvBCHyk1DazqK_19Uar4zE7bql4JfGgIcqUqhE4mSDzWD2xHVjapz0IDeKPvn6r4R_qJyi7kJ3jMw5xnn0BJo4uNZ4rHpTNQQIN8v3eXt1-FoOzmy0prOZydn81nZUoDDFtT-j31QqTUvqMVY6YPuSsmUWkOKwg7UqsOBX993jc6Iw-cs9iZYUWvlJ-c-EdMEtgi14mtvJ5_Mmr9qjltYro16Z5bmR-14MemEF1zdQfIzS3wSTiqMLdyfot9U4BUxa4V_Bhcw49NmFv8m2OIS0S3J_UndKK8PeP6KMALzoDqwoFuI_wAz3JvNuAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/whitedns/1972" target="_blank">📅 20:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1971">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوستان :
نسخه قبلی را پاک کنید ،و جدید را نصب کنید و امتحان کنید ،
الکی خیر نزنید ، این آمار اگر اشتباه باشه به خودتون ضرر می زنید
یکم تلاش کنید</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/whitedns/1971" target="_blank">📅 20:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1970">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-poll">
<h4>📊 ایا در نسخه ازمایشی  whiteaesther مشکل اتصال شما در همراه اول و مخابرات و .... حل شد ؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/whitedns/1970" target="_blank">📅 20:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1967">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.12.0-mci-stackfix.1-universal.apk</div>
  <div class="tg-doc-extra">136.6 MB</div>
</div>
<a href="https://t.me/whitedns/1967" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخهٔ آزمایشی whiteaesther مخصوص همراه اول و مخابرات و اپراتورهایی که توی نسخه های قبلی دچار مشکل بودند .</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/whitedns/1967" target="_blank">📅 20:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1966">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cvu5DlWQFfDWKtuMa6ovqpK8c9hZSpeU25e9sTle2baa4IJj8pp2TzjY9x-51qacpgk3wsR2JYXHQIYfYz2szNUhnqTQi0DQnBcvDozLhu22nuyV4_B_62yD8yiTKCYKDvNwpvA9pD1PFPh3BrlesPW4FBYzRn263ucpnEuFdfKdC8Pg8lnCqpGv_gw9d0_fisY2HBsvrijGQ5hGLntK5RIWXdEHW7IINjZEsCbXKCMNeTHcZzbANwiVvVlNA4p8jB-9KzNMDPjwaVZmVjV8an1B4hb_3n9PC2jaTXtMi7aXEtDsHepIy6G3DZ9YMr6iGUgyG0eNVYwts2qawvOIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
⚠️
نسخهٔ آزمایشی whiteaesther مخصوص همراه اول و مخابرات و اپراتورهایی که توی نسخه های قبلی دچار مشکل بودند .
حتما نسخه قبلی را uninstall کنید و بعد این نسخه را نصب و تست کنید
این Pre-release برای آزمایش بهبود اتصال روی اپراتورهایی مثل همراه اول تهیه شده است؛ مخصوص کسانی که نسخهٔ فعلی برایشان وصل نمی‌شود یا هنگام زدن Connect کرش می‌کند.
👀
اگر با نسخهٔ فعلی مشکل اتصال ندارید، فعلاً آپدیت نکنید.
پایداری این تغییرات روی همهٔ شبکه‌ها و گوشی‌ها هنوز به آزمون میدانی نیاز دارد.
لطف کنید این نسخه را تست و در نظرسنجی پست بعدی شرکت کنید
ممنون از همراهی همیشگی شما
❤️
https://github.com/WhiteDNS/WhiteAestherMobile/releases/edit/preview-1.12.0-mci-stackfix.1</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/whitedns/1966" target="_blank">📅 20:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1963">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hpxsuCcbIW02-qCfMfOWR6_ZkZFeSf8RKK6jwfk2HjFtaHuoL-DUn_nusXiG3m1HIM9DiMo9I3uFmw6G6vZoNV0D99Ry2RQqPT31HC1301tlOZF8qdDZGoRiiuNR1YbzVPczENhFyvdwr3FRZhSMk8Gi3Gta8mQgB6jhPvR-ZWaHjVxF4JfhFzfv8pOdwYPdRCNcHZjRB3bv9bTuh340EMBrKJctDxePK1cBAVNGlgY_bvNoeekvSUYew5-GZJLileu8EaOYbt2bif-RTcTuHCD1AFwzeTO0hhcAo-nIdBr6cXorIarut6s3JzHXSU3L2UL7M5lu1FsX2lbthBmjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت هر اتصال موفق، کسی هست که ساعت‌ها وقت گذاشته، آزمون و خطا کرده و تسلیم نشده تا راهی برای دسترسی به اینترنت باز بماند.
خواستیم از صمیم قلب از سازندهٔ Aether، یعنی
CluvexStudio،
تشکر کنیم. پروژه‌های WhiteAesther موبایل و دسکتاپ به لطف Aether ممکن شدند. ما رابط کاربری و قابلیت‌های خودمان را روی پایه‌ای ساخته‌ایم که او با زحمت و زمان بسیار توسعه داده و رایگان و متن‌باز در اختیار همه گذاشته است. سهم سازندهٔ این هسته باید روشن باشد و زحمتی که کشیده دیده شود.
خواندن حرف‌هایش دربارهٔ کمبود حمایت و بی‌انگیزگی برایمان تلخ بود. پشت پروژه‌ای که دانلود می‌کنیم، انسانی هست که وقت، انرژی و امیدش را صرف آن کرده است. بابت Aether و فرصتی که برای ساختن WhiteAesther فراهم کردی، ممنونیم. زحمتت برای ما ارزشمند است و امیدواریم این قدردانی کوچک، کمی دلگرمت کند که کارت دیده شده و به دیگران کمک کرده است.
🤍
اگر Aether یا WhiteAesther برایتان مفید بوده و مایل و قادر به حمایت هستید، می‌توانید مستقیماً از سازندهٔ Aether حمایت کنید. به گفتهٔ خودش، این کمک‌ها برای تهیهٔ سرورهای قوی‌تر و ادامهٔ توسعهٔ پروژه‌ها استفاده می‌شوند. حمایت کاملاً داوطلبانه است و هیچ انتظاری از کسی نیست؛ معرفی پروژه، ستاره دادن به ریپو و یک پیام قدردانی هم می‌تواند دلگرم‌کننده باشد.
ریپوی اصلی Aether:
https://github.com/CluvexStudio/Aether
کانال سازنده:
https://t.me/CluvexStudio
آدرس‌های حمایت اعلام‌شده توسط سازنده:
TRX / USDT — شبکهٔ Tron:
TRxVSHcoADZnBfztFmFb2TQopusAwWYEVR
USDT — شبکهٔ BNB:
0x20c980AEF36Aa71D0A0e7bE382AeD20b73bC6D27
TON (Gram):
UQAH75bXaaRUhZMwiF0ZujOXFDDmvLSPASKoOsWF0HNasiaM
با احترام و سپاس، از طرف WhiteDNS و پروژه‌های WhiteAesther
🤍</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/whitedns/1963" target="_blank">📅 17:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1962">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/TirSXZD-qBgVGUBJmhAU5-HC6qgPOQfgJFihE5mGpwWOPlM58zEzndq01mWxf44Nq2C0Wb9u6vnLDnaMiuTTzHn5FSw38c0K1mMm6NZkB3xkXmrwNyA8Waf-rfWoIrQosVeHdtD_fY-P2u5i43Lt_M41rE5s6talAOKAvY4umHkohXHA9m-5BOtPiIFA0UJaOnHelku1bq4rqQIvzvb5jwPqkmshLoOHkPKiBckYpYigdr5hcFZGdtjNnFWWliInXDYHZ-dS1PwQzrfLn3BCrvFf-82mkeCpYV2yjxjqpbvNq7CDDOlDN666toOXBVQyt6MzBk0SfpNhVsAJQmwjrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه ازمایشی
WhiteAesther Desktop v1.10.0 منتشر شد
اگر ورژن قبلی برای شما کار میکند و مشکلی ندارید اپدیت نکنید
⚠️
⚠️
هستهٔ برنامه به
Aether 2.3
ارتقا پیدا کرده و تنظیمات بیشتری برای آزمایش اتصال در شبکه‌های محدود در اختیار شماست.
✨
تغییرات مهم
• پشتیبانی ECH روی MASQUE H2 و H3
• اضافه شدن
WireGuard over MASQUE
• تنظیم cipherهای TLS 1.2، گروه‌های تبادل کلید و GREASE
• تنظیم آدرس ثبت‌نام WARP و resolver/domain کلید ECH
• اضافه شدن
Verified edges
به جست‌وجوی گیت‌وی‌ها
• اصلاح Save دیرهنگام؛ ویرایش تازهٔ شما هنگام ذخیره بازنویسی نمی‌شود
📖
آموزش انتخاب پروتکل دلخواه
اگر با انتخاب H3 یا WireGuard باز هم برنامه روی H2 وصل می‌شود، احتمالاً انتخاب خودکار مسیر فعال است.
۱. اتصال را قطع کنید.
۲. وارد
Advanced → Routes & transports
شوید.
۳. گزینهٔ
«راه خروج را برایم پیدا کن»
را خاموش کنید.
۴. carrier را روی
Aether
و مرحلهٔ دوم را روی
Nothing further
بگذارید.
۵. در
Protocol
روش دلخواه را انتخاب و دوباره وصل شوید.
💡
در حالت Automatic، برنامه چند روش را امتحان می‌کند و مسیر برنده را انتخاب می‌کند. انتخاب Protocol در این حالت، برنامه را به همان روش محدود نمی‌کند.
برای ثابت ماندن H2 یا H3 حتی پس از شکست اتصال،
اتصال مجدد خودکار
را هم خاموش کنید؛ retryهای MASQUE می‌توانند بین این دو جابه‌جا شوند.
🔐
آموزش تنظیم TLS و ECH
در همان صفحه، بخش
TLS and ECH
را باز کنید:
ا-
Encrypted Client Hello:
برای دریافت خودکار کلید، auto وارد کنید. خالی یا off یعنی خاموش.
ب-
ECH resolver:
خالی بگذارید تا هنگام ECH فعال، از DoH پیش‌فرض
https://1.1.1.1/dns-query
استفاده شود.
ج-
ECH key domain:
خالی یعنی پیش‌فرض
cloudflare-ech.com
.
ه-
TLS groups
:
نام گروه‌ها را با : جدا کنید؛ نمونه: X25519:P-256:P-384
ه-
TLS 1.2 cipher suites:
نمونهٔ معتبر: ECDHE-RSA-AES128-GCM-SHA256؛ این گزینه cipherهای TLS 1.3 را تعیین نمی‌کند.
ی-
Disable GREASE:
پیش‌فرض خاموش است؛ برای آزمایش سازگاری تغییرش دهید.
هر بار فقط یک گزینه را تغییر دهید،
Save profile
بزنید و دوباره اتصال را آزمایش کنید. خالی بودن فیلدهای TLS یعنی استفاده از پیش‌فرض هسته.
🧭
در
Verified edges
گیت‌وی‌های شناخته‌شده را در اولویت می‌گذارد و مسیر را بررسی می‌کند؛ تضمین اتصال نیست.
📦
این نسخه
prerelease
است. بسته‌های پنج پلتفرم ساخته و هستهٔ داخل هر ۱۰ نصب‌کننده بررسی شده است.
پیش از حذف یا نصب مجدد، از
Identity → Save a backup
بکاپ بگیرید. اگر
Core executable
به هستهٔ قدیمی اشاره می‌کند، آن را خالی کنید تا هستهٔ همراه برنامه اجرا شود.
⬇️
دانلود نسخهٔ جدید
📚
راهنمای کامل فارسی</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/whitedns/1962" target="_blank">📅 12:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1959">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.12.0-universal.apk</div>
  <div class="tg-doc-extra">136.6 MB</div>
</div>
<a href="https://t.me/whitedns/1959" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید whiteaesther mobile منتشر شد !
📱
✨
whiteaesther mobiel 1.12.0
🚀</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/whitedns/1959" target="_blank">📅 07:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1957">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/c06rNM7R7zj4R1YXlyfL_oP8ZxouXlsNogn7DFdhozxd8A2SEXrW_FAE5NXzUWUqMY0gXteA2CexBmuIQvDgXOgszCJlxRoDMinG_ffZAOiA09kpGJrvuBULIFG14MQEQADnNWNQ8qTrKE_Uvj0TJOfqv7Zkva74uNvDLimOLaJw6JNDJDjaIcXNJfi9JA6jqDOqsqPkOvjpVxiu6YyDzV-vqYSoI7m8QFYMphxZ-jlj9fCFBsYl3PgLZ8qclVHVbnsOqCeD3_jb89C5BcO3hiKKCOriamRbIA5nEA_UZGGTXANnferoqJxACzn7SMN7eqhQVioaSx-RW-XeonlNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید whiteaesther mobile منتشر شد !
🔥
🔥
🛠
راهنمای تنظیمات جدید WhiteAesther 1.12.0
با ارتقای هسته به Aether 2.3.0، تنظیمات TLS و ECH کامل‌تر شده‌اند. سه گزینهٔ زیر در Traffic → Advanced قرار دارند. اگر اتصال خوب کار می‌کند، دو کادر را خالی بگذار و Disable GREASE را تیک نزن؛ موتور از تنظیمات پیش‌فرض استفاده می‌کند.
۱️⃣
ا- TLS 1.2 cipher suites
فهرست الگوریتم‌های TLS 1.2 را مشخص می‌کند و می‌تواند شکل پیام آغاز اتصال را تغییر بدهد. برای شروع خالی بگذار.
نمونهٔ قالب برای آزمایش:
ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256
نام‌ها با دونقطهٔ انگلیسی : جدا می‌شوند. این نمونه نسخهٔ پیشنهادی برای همهٔ شبکه‌ها نیست؛ محدود کردن فهرست ممکن است سازگاری را کمتر کند. این کادر رمزهای TLS 1.3 و تونل H3 را تغییر نمی‌دهد، ولی می‌تواند روی ارتباط HTTPS ثبت‌نام یا دریافت کلید ECH اثر بگذارد.
TLS key exchange groups
گروه‌هایی را تعیین می‌کند که برای ساخت کلید مشترک TLS پیشنهاد می‌شوند. ترتیبشان هم اهمیت دارد. برای استفادهٔ معمول خالی بگذار.
نمونهٔ قالب برای آزمایش:
X25519:P-256:P-384
این تنظیم می‌تواند روی H2، H3، ثبت‌نام WARP و دریافت کلید ECH از طریق HTTPS اثر داشته باشد. نام‌ها را با حروف و علائم انگلیسی وارد کن.
Disable GREASE
GREASE مقادیر رزروشده‌ای را در پیام TLS می‌فرستد تا سازگاری با توسعهٔ پروتکل حفظ شود. برای امتحان یک مشکل دست‌دادن TLS می‌توانی این گزینه را جداگانه تغییر بدهی:
▫️
بدون تیک: GREASE فعال است؛ پیش‌فرض موتور.
▫️
با تیک: GREASE غیرفعال می‌شود.
اگر نتیجه بهتر نشد، تیک را بردار. این گزینه رمزگذاری یا بررسی گواهی سرور را خاموش نمی‌کند.
➕
WARP registration address
کادر پایین این سه گزینه، مقصد درخواست‌های ثبت‌نام و مدیریت حساب WARP را تغییر می‌دهد. معمولاً خالی بماند. فقط آدرس سازگار و آزموده‌شدهٔ سرویس ثبت‌نام را با قالب IP:port یا host:port وارد کن؛ بدون پورت یعنی 443. این کادر با Endpoint تونل فرق دارد. لینک اشتراک، کانفیگ نود، https:// یا مسیر سایت در آن وارد نکن. اگر ثبت‌نام بعد از تغییر شکست خورد، کادر را خالی کن.
🧪
چطور درست آزمایش کنیم؟
• در Routes → Carrier، حالت Manual و سپس Aether را انتخاب کن؛ TLS داخلی سایفون و تور با این کادرها تغییر نمی‌کند.
• برای مقایسه روی یک روش مشخص، در Routes → Advanced → Protocol، H2 یا H3 را انتخاب کن.
• هر بار فقط یک گزینه را تغییر بده، قطع و دوباره وصل شو. Check the connection works روشن بماند.
• اگر خطای --tls-ciphers، --tls-groups یا --enroll-address دیدی، کادر همان گزینه را خالی کن و دوباره امتحان کن.
✨
چه چیزهای دیگری تازه شده؟
الان ECH روی H2 هم کار می‌کند و در اتصال خودکار هم امتحان می‌شود. با روشن کردن Encrypted ClientHello، کادرهای ECH resolver و ECH key domain را می‌بینی؛ ابتدا هر دو را خالی بگذار. پیش‌فرض اندروید برای دریافت کلید،
https://1.1.1.1/dns-query
و دامنهٔ پیش‌فرض
cloudflare-ech.com
است. این resolver فقط کلید ECH را می‌گیرد؛ DNS ترافیک اپ‌ها را عوض نمی‌کند. تلاش دارای ECH بدون کلید قابل استفاده ادامه پیدا نمی‌کند؛ حالت Automatic برنامه ممکن است روش دیگری را امتحان کند.
حالت Verified edges هم در Routes → Advanced → Discovery depth اضافه شده است؛ گیت‌وی‌های شناخته‌شده را در اولویت می‌گذارد و همچنان مسیر را آزمایش می‌کند. هشت سابقهٔ گیت‌وی موفق و انتخاب بهتر بین IPv4/IPv6 هم به بازیابی اتصال کمک می‌کنند.
مشکل تایپ در کادرهای تازه و خطای نبودن libc++_shared.so هم در نسخهٔ جدید اصلاح شده‌اند.
📥
دریافت نسخهٔ 1.12.0:
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.12.0
📖
آموزش کامل و روش برگشت به تنظیمات قبلی:
https://github.com/WhiteDNS/WhiteAestherMobile/blob/main/docs/GUIDE.fa.md#aether-23
#WhiteAesther
#WhiteDNS
#Aether
@whitedns</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/whitedns/1957" target="_blank">📅 07:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1956">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👆
اگر نمیدونید master/cotton / storm dns چی هست لطفا درخواست ندید
این کانفیگ پرسرعت نیست - برای دیدن یوتیوب و اینستاگرام و ....... نیست - برای گیم نیست و برای تست نیست و ........
این کانفیگ را جلو جلو برای قطعی در زمان جنگ درخواست نکنید . اون موقع ما به صورت عمومی سرورهای دیگه ای را در اختیار شما میگذاریم .
یک کانفیگ با سرعت فوق العاده پایین برای لود کردن محتوای نوشتاری است .
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/whitedns/1956" target="_blank">📅 06:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1955">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔥
⚠️
🔥
به دلیلی بروز اختلالات شدید توی چند روز گذشته :
ما روی سرورهای whitedns یک پلن هفتگی(ازمایشی-موقت) هم اضافه کردیم که نیاز نباشه روزانه درخواست بدید ( در صورت overload شدن سرورها این پلن حذف خواهد شد )
دوستانی که امکان کمک مالی (کاملا اختیاری) دارند لطفا به ادرس ولتی که توی بات در پروسه درخواست کانفیگ میبیند مبلغی هر چند کوچک را هدیه کنید . این کمک مالی صرف ارتقای سرور و بهتر کردن امکانات خواهد شد
ادرس ربات :
@MasterDnsManager_bot
نرم افزار whitedns :
دانلود اندروید
•
دانلود دسکتاپ
نرم افزار  WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
@whitedns</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/whitedns/1955" target="_blank">📅 06:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1954">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سرور whitedns که از طریق بات درخواست میکنید یک روزه هست اگر لازم دارید
به درد روز مبادا نمیخوره ،درخواست ندید</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/whitedns/1954" target="_blank">📅 13:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1953">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/se0MK4tbhT4zzmUWiIQabqbXiP_WPGmsPwAo48GCeU1S1lohyifsYOFJdOwkFrQ58XP7DLMtSWCWtWnapykXXbzjWSdjbT-1mkknSVn2QRlOo5TenqEIGRteDjuGPF0gdCDoAlS8zp9g-kXLMDrtx3uS-6QX1deFNR0q95dr-S6lOdTQKinEkmZB7sAv1S2G1UgJxbZfGpbeluTeJILc8NcJp7K62qD3G8slw7uSMPiu5V79ItcVZrCb17ezh8QP_05MekchGnZu5epyIZRFkVgLgqvjYzEj72FjTPEKeVLv0VD35A8a4b6AoPtyy_729Tw97hiFZjsGFjGC7qnrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری (مستر دی ان اس )
⚠️
⚠️
whitedns app config bot/ masterdns config   :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/whitedns/1953" target="_blank">📅 13:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1952">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-text">🎬
آموزش کامل TheFeed | از صفر تا صد + پیام‌رسان جدید + ظاهر جدید
اگر تازه با TheFeed آشنا شدید یا می‌خواهید با قابلیت‌های جدید آن آشنا شوید، این ویدیو را از دست ندهید.
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
استفاده از کانفیگ‌های پیش‌فرض
✅
آشنایی با ریزالورها و DNS
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با TeleMirror
✅
رفع مشکلات رایج
✅
فعال‌سازی پیام‌رسان TheFeed
دفید یک پلتفرم مبتنی بر DNS است که برای شرایط محدودیت اینترنت طراحی شده و حالا علاوه بر دریافت محتوای کانال‌ها، امکان گفت‌وگوی امن بین کاربران را هم فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصبی:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
ضبط و تدوین ویدیو:
@vahid_4444</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1952" target="_blank">📅 11:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1950">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tqRJIE3xZ4jO6-l6ntx0guTDbRBOsvKn3w_f0Ga6Y3VZQOzMCJ9XPYTkpevxpiL_Chsgvk-nxlJQFvT758hkhgXi_M6-u7MVGJliR6dBQPGbOZ4iapMob0kHom7M-_Y3_91dDND6NFa-u_bAlHHec7vCEaZbpAsJFhhQR-U2-mDR9AmuuvcRrqbZSLmmTNiQY7WM_lN6ciq352QyNdZmoAOE8rtb3yevdzLz7iCWVpGCi4hBG1QHwZ-nJGw-tGyKob6VyNtjegAWD5hIIgQf35247KP5hSmtSx2VyORwtGy_5Yoa-RQmsxwqBDlHiy1wUlKLK0T_yASV8rOoTDSozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتیم برای WhiteDNS یه Patreon راه بندازم.
حدود 9 ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱5 هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://www.patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/whitedns/1950" target="_blank">📅 06:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Dge4oy7M2ZNSvBQ3Fu2ZcEYF5E1RWrsjDkvpt44sfubybDZMGTk_dT9Tg_4KVgeP3SPzdzwPbnTNt-6jJMAIlSW2BVLZldQ5aOZf0fLb-yFWA9UuM6hjqjaeDIo301tGrFCANsigWBfyKMgbVefbGwXFdKLZpzWKlwKBFRP7cmy0Q6fZHfrPTJPBOwI3aY_8hZxNFMW_617tXu3F-6dJMmMRtRgGi-TNKeOy7NbcBEDxMpOsIVeUZ2ib7Y_8_O3qHHd3HcyTXBVSg6KOcD1GxWbENDMwr7AoZVWHGefCnksqneG0qzx_BkSOG1ulHUzIxA8bn5kw4AVAr63Cz63ZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
WhiteDNS
مسیری که قبل از روزهای قطعی اینترنت شروع شد
تیم WhiteDNS از مدت‌ها قبل از قطعی‌ها و محدودیت‌های گسترده اینترنت فعالیت می‌کرد. از همان ابتدا تلاش کردیم ابزارها، سرویس‌ها و آموزش‌هایی بسازیم که رایگان و در دسترس همه باشند.
در این مدت افراد زیادی به این جمع پیوستند؛ بعضی ماندند و بعضی مسیرشان جدا شد، اما چیزی که ما را کنار هم آورد همچنان پابرجاست:
حرکتی جمعی برای دسترسی آزادتر به اینترنت.
تیم WhiteDNS تا امروز کاملاً مستقل و بدون هیچ منبع درآمدی اداره شده و تمام هزینه‌ها را خودمان پرداخت کرده‌ایم. با این حال، این مسیر را ادامه می‌دهیم و همچنان ابزارها و سرویس‌های رایگان بیشتری را با کمک همین جامعه خواهیم ساخت.
حالا تنها مسیر درآمدی ما کانال یوتیوب WhiteDNS است. اگر می‌خواهید از این حرکت حمایت کنید، کانال را سابسکرایب کنید و ویدیوها را ببینید. همین همراهی کمک می‌کند WhiteDNS مستقل، فعال و جامعه‌محور باقی بماند.
📺
https://www.youtube.com/@WhiteDNS
ممنون که بخشی از این مسیر هستید
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1948" target="_blank">📅 06:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1947">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXEIox0EyTuXWpKKFOqKlSv2ChXFlSgO7lQeHuK3VRrcOBBD7ChFDlZzhp-ToNTiljV3dvjk4Zv47VuN8RxWQ4fArZrhdqlhxMEX-EjiNJScQe8dAKN_usrvIPETnhUfqkJbRhBjkO8pyuHCLGPR2UWlOadj8S88t4OBZJ7UzqlY4c2CullEpXEO_3_XZXKm8aBZBE8kullwcKMNkM3mc_MZI44ihK6PXulR-fE8WPpcv2NFTJf-1p65j-QeNHeObarqIW45LYVwpXSbsrrSuX4Pesm0dHYPC4Wx8IYv6Mqny1jwrfXRSuqRTPXa_2F046pU7ZBoZg8Mr2Ut6mxAJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
درود به همه رفقا...
بعد از محدودیت های اخیر در فیلترنت و محدود شدن بیشتر پروتوکل ها و روش های رایگان مربوط به کلودفلر و...
تصمیم بر این گرفتم تست های مختلف طی چند روز انجام بدم و بهتون بگم چه روش هایی/اپلیکیشن هایی متصل هستند تا کمکی به شما رفقا باشه.
بهترین اپلیکیشم اتصال برای همه
دیوایس ها(ios,android,windows) از نظر بنده:
📱
اپلیکیشن defyx vpn: هست،اپلیکیشن کامل و متن باز که از نظر من جای بدافزار هایی مثل جامپ جامپ که روی همه گوشیا نصبه باید از defyx استفاده کنید ویژگی xray و بروز بودن این اپ در
#فیلترینگ
کمک بزرگی میکنه
😍
لینک دانلود بر اساس سیستم عامل متفاوت:
👽
android:
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
🛍️
ios:
https://apps.apple.com/pk/app/defyx/id6746811872
💻
windows :
https://github.com/UnboundTechCo/defyxVPN/releases
🤝
اپلیکیشن بعدی Mahsang:
بهترین روش برای اتصال به مهسا روش هایی مثل سایفون داخل اپ هست که کاملا متصله روی همه نتا فقط نیاز که برنامه رو بریزید و از بالا گزینه P و روی حالت سایفون بزارید تا متصل شید اگر اون حالت جواب نده
#کانفیگ
های EMS در سخت فیلترینگ هم وصله.
🛒
دانلود اپلکیشن Mahsang:
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
🔥
اپلیکیشن white vpn:
اپلیکیشن بروز با هسته های بسیار خوب و داشتن ساب پیشفرض در برنامه برای وصل شدن در شرایط سخت
#فیلترنت
این اپلیکیشن هم کلاینت و هم روشی برای دور زدن محدودیت ها بر مبنا dns هست:
💻
گیتهاب پروژه:
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🙂
روش های کلودفلر و پترینها:
1️⃣
روش اول:
داخل پنل های کلودفلر(bpb) خود گزینه ECH رو فعال کنید مشکل وصل نشدن حله میشه مهم ترین پیدا کردن ip تمیز بر اساس نت هست بهترین اسکنر از نظر من:
https://github.com/ashanews9776-eng/asha_scanner/releases/tag/v0.8.3
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
2️⃣
روش دوم:(استفاده از ساب رایگان پترنیها)
پیشنهاد میشه این لینک ساب یا هر کانفیگی از نوع پروتوکل رو داخل اپ های خود پترنیها یعنی
pattng
/
pattn
بزنید اگر هم بلد نیستید میتونید از
ویدیو آموزش استفاده کنید
.
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt#Patterniha-F
💡
توجه:ممکنه بسیاری از روش های دیگه مثل وارپ(AETHER) یا حتی SERVER LESS رو نت شما کار کنه اما این بیشتر بستگی به محدودیت های اینترنت و منطقه شما داره این روش ها رو داخل این پست اشاره نکردم زیرا روی همه نتا متصل نیست و منتظر آپدیت جدید از CluvexStudio و patterniha برای هسته Aether و همچنین sni spoof میمونم و بعد از رفع مشکل معرفی میکنم.
@xsfilterrnet
🙂</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/whitedns/1947" target="_blank">📅 18:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kwF3SUxhEP6k6vNqqpAYrQIsd4MPQpl2WtgeeBXAG2Q2zY13Vw1KbWu3uPNZSu4TvxIdCAllhwO6dbN-0EStfhDYdJspBfU7GEoQ0-H0kuSJzv8c-q_upVapVUeLP_YDSR75TuL9R0F1i5NsbBQKdCccU0yJBLmucWR6VP7aqx_dkK502Rm84SlE6MdP7ZXHSHiaYBl_dueTipC_CVpvvu8biux0Iv5SrXVOGqU8A1Jxvgo7a4lv1zPgk6sHYPr5z0tfoxFDsn2HRHfdaR0_gGMbSxDpQGSf3GtKalyE26Bfaonua7fz2Runge4vtW-N-V9fz0IUrSZPhD7ngJEyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📘
آموزش سادهٔ TLS Split و ECH در WhiteAesther 1.11.0
این دو قابلیت به اتصال
Aether
کمک می‌کنند:
🔹
TLS Split
پیام آغاز اتصال را به قطعات کوچک‌تر تقسیم می‌کند.
🔹
ECH
بخش داخلی همان پیام، از جمله نام سرور، را رمزگذاری می‌کند؛ سرور باید پشتیبانی کند.
✅
برای کاربران معمولی: حالت خودکار
۱. اتصال را قطع کنید.
۲. در
مسیرها / Routes
، انتخاب مسیر را روی
خودکار
بگذارید.
۳. وارد
ترافیک / Traffic ← پیشرفته / Advanced
شوید.
۴.
Split the TLS handshake
را روشن و گزینهٔ
خودکار
زیر آن را انتخاب کنید.
۵. برای ECH نیز
Encrypted Client Hello
را روشن و زیر آن
خودکار
را انتخاب کنید.
۶. به خانه برگردید و وصل شوید. هیچ کادر سفارشی را پر نکنید.
⚠️
هر قابلیت کجا کار می‌کند؟
• تقسیم TLS: روی
MASQUE H2
و تونل بیرونی
WireGuard over MASQUE / WOM
.
• ECH: فعلاً فقط روی
MASQUE H3
.
• این گزینه‌ها تنظیمات داخلی Psiphon یا Tor را تغییر نمی‌دهند.
🛠
تنظیم دستی تقسیم TLS
در
ترافیک ← پیشرفته
، تقسیم TLS را روشن کنید:
•
Records / پیش‌تنظیم رکوردهای TLS:
الگوی آماده؛ عدد لازم ندارد.
•
Compact / پیش‌تنظیم فشرده:
الگوی آمادهٔ دیگری است.
•
Custom / سفارشی:
مقدارها را خودتان وارد می‌کنید.
مقدارهای پیش‌فرض بخش سفارشی:
▫️
اندازهٔ قطعه:
16-32
▫️
تأخیر:
2-10
▫️
تقسیم در محل نام سرور:
روشن
16-32 یعنی اندازه از بازهٔ ۱۶ تا ۳۲ بایت انتخاب شود. 2-10 یعنی تأخیر بین قطعات از بازهٔ ۲ تا ۱۰ میلی‌ثانیه انتخاب شود.
اندازهٔ مجاز:
1 تا 16384
تأخیر مجاز:
0 تا 100
فقط عدد یا بازه را با اعداد انگلیسی وارد کنید. این مقدارها تضمین اتصال نیستند؛ قطعات خیلی کوچک یا تأخیر زیاد می‌توانند اتصال را کند کنند.
برای انتخاب مشخصِ H2 یا WOM، در
مسیرها ← خودم انتخاب می‌کنم
، مسیر شامل Aether را انتخاب کنید؛ سپس در
پیشرفته ← پروتکل
، H2 یا WOM را بگذارید.
🔐
تنظیم ECH
برای بیشتر کاربران،
خودکار
کافی است؛ برنامه تلاش می‌کند تنظیمات لازم را دریافت کند.
سفارشی / Custom
را فقط وقتی انتخاب کنید که یک
ECHConfigList معتبر و سازگار با سرور، با فرمت Base64
از پشتیبانی دریافت کرده‌اید. خود رشته را بدون عنوان ech= یا کوتیشن در کادر بچسبانید.
آدرس IP، نام دامنه و کلید وایرگارد برای این کادر کاربرد ندارند. اگر رشته را ندارید، حالت
خودکار
را انتخاب کنید.
برای انتخاب دستی H3:
مسیرها ← خودم انتخاب می‌کنم ← مسیر شامل Aether ← پیشرفته ← پروتکل ← MASQUE H3
H3 به عبور UDP نیاز دارد؛ ECH به‌تنهایی مسدودبودن UDP را حل نمی‌کند. همچنین روشن‌بودن گزینهٔ ECH، فعال‌شدن موفق آن را تضمین نمی‌کند؛ دریافت خودکار ممکن است ناموفق باشد و تلاش اتصال بدون ECH ادامه پیدا کند.
💾
تنظیمات خودکار ذخیره می‌شوند. پس از تغییر مقدارهای دستی،
قطع و دوباره وصل شوید
. اگر ورودی خطا دارد یا اتصال بعد از تغییر ناموفق شد، تنظیم مربوط را به
خودکار
برگردانید.
@whitedns</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1946" target="_blank">📅 19:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1943">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.11.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/whitedns/1943" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخهٔ 1.11.0 Whiteaesther mobileمنتشر شد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1943" target="_blank">📅 19:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1942">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/behYqDfK7STDGag0KLgQgTqrcJfO5BLSeVW68IaVKLQR7QxVCyU091wsSnmKOIaTEvJ_EJBOiw7Y4WwtEmZUeuj75rXCPsWa7QpEkYFI-2ure8uU5GjTqIrEr-g7db47mwWGQ5dcLzvw5DrLnNJK2csQJ5WvTWLIwfB2nS29-o3VBGdhDXgKu_hPC_44bW9IE-Zv4bE_TRL9fvunlxi524DGDZ-Y-uxnPJNMnzStJ6GA0ovbbxQvnDT9i6KISP87luWglq30reSnizQSOD2Ydk6WOkN6nk9FHGeJy1WYBBHGvM-kMvVuQGgqD_VT5FvNUyhkdSGoBNgTcaxD_25Mhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخهٔ 1.11.0 Whiteaesther mobile منتشر شد
این نسخه روی اتصال‌های ناموفق، انتظار طولانی و گیرکردن VPN تمرکز دارد:
🔹
پروتکل جدید WARP WireGuard over MASQUE
وایرگاردِ خودِ WARP داخل یک تونل MASQUE روی H2/TCP حمل می‌شود. این مسیر، وقتی ارتباط مستقیم وایرگارد با UDP مشکل دارد، یک گزینهٔ دیگر برای اتصال فراهم می‌کند. سرور وایرگارد شخصی لازم نیست و می‌توانید آن را به‌عنوان مسیر Aether در ترکیب Aether + Psiphon هم استفاده کنید. قبل از نمایش «متصل»، عبور داده از هر دو تونل بررسی می‌شود.
برای انتخاب دستی: در «مسیرها»، «خودم انتخاب می‌کنم» را بزنید، Aether یا Aether + Psiphon را انتخاب کنید و در «پیشرفته ← پروتکل»، «وایرگارد روی MASQUE» را بگذارید. حالت خودکار خودش مسیرهای جایگزین را انتخاب می‌کند.
🔹
اتصال خودکار بهتر
حالت خودکار زودتر سراغ مسیرهای جایگزین می‌رود؛ روش‌های مختلف دست‌دهی H2، تکه‌تکه‌کردن TLS، IPv6 در صورت فعال‌بودن و WireGuard over MASQUE را بررسی می‌کند. مسیر موفق برای همان شبکه ذخیره می‌شود تا اتصال بعدی از آن شروع شود. آدرس ذخیره‌شدهٔ WARP هم پیش از انتظار برای دریافت دوباره از API امتحان می‌شود.
🔹
تنظیم دستی کنار حالت خودکار
در «ترافیک ← پیشرفته»:
• «تکه‌تکه کردن دست‌دهی TLS»: پیام آغاز اتصال را به قطعات کوچک‌تر تقسیم می‌کند. حالت خودکار، Records، Compact یا تنظیم سفارشی دارد. در حالت سفارشی اندازهٔ قطعه، تأخیر و تقسیم نام سرور را تعیین کنید؛ مثلاً اندازهٔ 16-32 بایت و تأخیر 0-1 میلی‌ثانیه. این اعداد فقط نمونهٔ ورودی هستند.
• «سلام اولیهٔ رمزگذاری‌شده / ECH»: نام سرور را در بخش رمزگذاری‌شدهٔ ClientHello قرار می‌دهد. دریافت خودکار یا واردکردن ECHConfigList با فرمت Base64 در دسترس است؛ این مقدار، نام دامنه یا SNI نیست.
تقسیم TLS روی H2، از جمله تونل بیرونی WOM، اعمال می‌شود؛ ECH فعلاً مخصوص H3 است. تنظیمات سفارشی در تلاش‌های بازیابی حفظ می‌شوند و تغییرشان با اتصال بعدی اعمال می‌شود.
🔹
رفع باگ‌های اتصال و تغییر پروفایل
تونلِ در حال آماده‌سازی پس از شکست یا لغو اتصال بسته می‌شود. هنگام تغییر پروفایل، موتور قبلی کامل متوقف می‌شود تا پاک‌سازی آن اتصال جدید را خراب نکند. خطای تنظیمات ناقص هم پیش از روشن‌شدن VPN بررسی می‌شود.
اگر در Aether + Psiphon پیام «اشتراک یا نود اضافه کنید» می‌دید، در «مسیرها» گزینهٔ «فقط مسیرهای انتخاب‌شده / Use carriers only» را بزنید. این گزینه زنجیرهٔ خروجِ بدون نود را خاموش می‌کند و ترکیب انتخاب‌شدهٔ شما را نگه می‌دارد؛ خودِ Aether + Psiphon به اشتراک نود نیاز ندارد.
📥
دانلود نسخهٔ جدید:
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.11.0
اگر معماری دستگاه را نمی‌دانید، APK نسخهٔ universal را انتخاب کنید.
@whitedns</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1942" target="_blank">📅 19:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1941">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qtdKAlrCgoG6oEh1rf3XlJhGH0lA3sMuWOTe2Hs07C8AbrcuyEqeSbhfuA3MAJtyel1veHmWYdiAS74mXRV4yLuWhiTuSVARBB93Rl3nN-Fx7O6mnJ2d6YtXrTKbpkXLPAtLEeZK9zVk_GFPRsy6jWdQ9Ke3By00OCWEgalEIrxMhr19vH7RZH_DC7eGkfw5AC0Nlf2Z-7XX_hhwkXtdpwkIp6DvRCQt3HSWR8blzp68RZUUPMmS0aAyvOcfDWSMOUhbeAGwqmCYiVau2Ls9gg3H49Ke8ImCG8DJ0vQd8v70guDNSVrVHzkRkZI_6Mq77fXKwkbNnFzuT4X27GsG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری (مستر دی ان اس )
⚠️
⚠️
whitedns app config bot/ masterdns config   :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1941" target="_blank">📅 12:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1940">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Fragment + Fingerprint
📱
روی بعضی از اپراتورها
میتونید با اعمال کردن مقادیر زیر در pttn/pttng روی کانفیگ های BPB دوباره متصل بشید .
💻
https://github.com/patterniha/PattNG/releases
/ windows ,linux . mac
📱
https://github.com/patterniha/PattN/releases
/ android
در قسمت finalMask کل عبارت زیر را وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
در قسمت cipherSuites کل عبارت زیر را وارد کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
@whitedns</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1940" target="_blank">📅 12:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1939">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n8BZK_dd2CMKXO29wRLCOzR8eLN8svtN4wxNRa-Zf8P9fBLaMAKJZHt5K_BIfuZCyFOkzDQRIOf8XS2BE7yLSx5GWdweSw7z1slJrE_ueXqMHgm7nbTbvubh1TerVUq_yCuVQmc8pzXybWr8H-Nstl8yGa64igbLUb8B-QHg50-wnB_GMJ1xquxBG3lQD9LlOB1HlGKnou_tWeU4wIegpqV0KXp14BGZCjICSHCkzZw_dDY-a8msdJbayr9cYivKkl-ltRcuPqo4E8d91ZU-qEbF4oOSJH4b9Rweh9PEF7So_fGcZb5BbRvsCoNlx66Fw1zsJYuMEOvqwwzV-kKpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دو عدد تصویر هم برای دوستان هستش که ایرانسل دارن که باید طبق آموزش گزینه های موجود رو انتخاب کنند
@whitedns</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1939" target="_blank">📅 05:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1938">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rdTnK1Zx14h3opmEsXKvGSBOR6GqIWB8c406XMYMudMdraOghKXNsvkOIyzciunRdC86NcpCJPgaQjh9m4xrlzwTmhFro0LFqcoOPZDKeQOIHS6UJVlBECCK_RQaE1C1vy3R8fVX9IVcBNcqftvD-ojA4Zd6HXazLmys1oEGL3T5vkYTEYvAJQLUvzlwyKow4IaGMN2Wui1fUrFV39xzllz_epUkd6nXHWwfMAPG7rggx7RIGcJ3RueXC6t4cGhRVoveQK2gL4hKnO3-v9kh4samS4uCvrmrK_YzMkC0c_Cs3xo9Ck2qHN5FZcz2_pd-j-9PggdWk1ncQYa9tC9SOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ین تصویر هم مربوط به آموزش هستش برای
دوستانی که اپراتور هاشون رایتل و همراه اول هستش در این بخش باید مقادیر وارد بشود
cloudflare-ech.com
+udp://1.1.1.1
cloudflare-ech.com
+udp://9.9.9.9
cloudflare-ech.com
+udp://208.67.222.222
cloudflare-ech.com
+udp://8.8.8.8
نکته : فقط یکی از این عبارت ها باید وارد بشه یکی یکی تست کنید ببینید کدوم بهتر هستش
@whitedns</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1938" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1937">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سلام به همهٔ همراهان عزیز
👋
امیدوارم این روزها با وجود همهٔ فراز و نشیب‌ها، حال دلتون خوب باشه و اینترنتتون هم روان و بی‌دردسر
💚
از وقتی فیلترچی‌های عزیز محبتشون رو بیشتر کردن، دیگه هر روز باید یه راه تازه پیدا کنیم. این روش رو اول کانال پترنی‌ها (
https://t.me/patt_channel_x
) با کلی آموزش مفصل معرفی کردن؛ من فقط یه بخشش رو برداشتم و یه تغییر کوچیک روش دادم که جوابش واقعاً عالی درومد.
📌
نکتهٔ مهم: توی منطقهٔ من این روش فقط روی رایتل و همراه اول جواب داد. برای ایرانسل هم پایین‌تر آموزش جدا گذاشتم.
---
🟢
روش اول — مخصوص رایتل و همراه اول
۱) کانفیگ رو وارد کن
هر کانفیگی که دوست داری از هر پنلی بردار و توی PattNG بازش کن.
۲) آی‌پی رو عوض کن
برو توی بخش ویرایش، یکی از این آی‌پی‌ها رو کپی کن و توی «نشانی» (Address) بذار:
۱۸۸.114.97.1
188.114.97.1
۱۸۸.114.97.2
188.114.97.2
۱۸۸.114.97.3
188.114.97.3
۱۸۸.114.97.4
188.114.97.4
۱۸۸.114.97.5
188.114.97.5
۱۸۸.114.97.7
188.114.97.7
۱۸۸.114.97.8
188.114.97.8
۳) اثر انگشت
همون‌جا پایین برو و گزینهٔ «اثر انگشت» (Fingerprint) رو روی Chrome بذار.
۴) echConfigList
باز پایین‌تر برو و یکی از این‌ها رو توی بخش echConfigList بذار:
ECH ۱
cloudflare-ech.com+udp://1.1.1.1
ECH ۲
cloudflare-ech.com+udp://9.9.9.9
ECH ۳
cloudflare-ech.com+udp://208.67.222.222
ECH ۴
cloudflare-ech.com+udp://8.8.8.8
ECH ۵
cloudflare-ech.com+udp://1.0.0.1
ECH ۶
cloudflare-ech.com+udp://8.8.4.4
ECH ۷
cloudflare-ech.com+udp://149.112.112.112
ECH ۸
cloudflare-ech.com+udp://208.67.220.220
ECH ۹
cloudflare-ech.com+udp://76.76.19.19
ECH ۱۰
cloudflare-ech.com+udp://76.76.2.0
ECH ۱۱
cloudflare-ech.com+udp://94.140.14.14
ECH ۱۲
cloudflare-ech.com+udp://94.140.15.15
ECH ۱۳
cloudflare-ech.com+udp://64.6.64.6
ECH ۱۴
cloudflare-ech.com+udp://64.6.65.6
ECH ۱۵
cloudflare-ech.com+udp://45.90.28.0
ECH ۱۶
cloudflare-ech.com+udp://45.90.30.0
ECH ۱۷
cloudflare-ech.com+udp://185.228.168.9
ECH ۱۸
cloudflare-ech.com+udp://185.228.169.9
⚠️
نکته: این عبارت‌های ECH ممکنه منطقه به منطقه فرق کنن؛ پس همه رو تست کن تا بهترینش رو پیدا کنی.
۵) ذخیره و وصل شو
روی تیک بالای کانفیگ بزن که ذخیره بشه و تموم — راحت وصل می‌شی.
✅
---
🟢
روش دوم — مخصوص ایرانسل
بازم ممنون از پترنی‌های عزیز که روش فایروال ایرانسل رو هم گذاشتن. من یه تغییر کوچیک روش دادم که به نظرم سرعتش خیلی بهتر شد. اینجوری:
۱) آی‌پی
کانفیگ رو توی PattNG باز کن، برو بخش ویرایش و یکی از این‌ها رو توی «نشانی» بذار:
۱۸۸.114.97.1
188.114.97.1
۱۸۸.114.97.2
188.114.97.2
۱۸۸.114.97.3
188.114.97.3
۱۸۸.114.97.4
188.114.97.4
۱۸۸.114.97.5
188.114.97.5
۱۸۸.114.97.7
188.114.97.7
۱۸۸.114.97.8
188.114.97.8
۲) finalMask
یه کمی پایین‌تر توی finalMask گزینهٔ tlshello-0-len رو انتخاب کن.
۳) اثر انگشت
باز پایین‌تر توی «اثر انگشت» گزینهٔ unsafe رو بزن.
۴) مجموعه رمزنگاری
باز هم پایین‌تر توی «مجموعه رمزنگاری» (Cipher Suites) گزینهٔ real_firefox_cipherSuites رو انتخاب کن.
۵) ذخیره
توی پایان روی دکمهٔ ذخیره/سیو بزن تا اعمال بشه.
---
امیدوارم این راهکار به دردتون بخوره. موفق و پایدار باشید
🌹
🚀
⚠️
یادآوری آخر:
توی بعضی مناطق سیم‌کارتت ممکنه همراه اول باشه ولی فایروالت ایرانسل، و برعکس؛ سیم ایرانسل ولی فایروال همراه اول. بقیهٔ اپراتورها هم معمولاً از یکی از همین دو فایروال استفاده می‌کنن. پس یه زحمت بکش و هر دو روش رو روی اینترنت خودت تست کن
❤️
@whitedns</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1937" target="_blank">📅 05:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1936">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAH57g7GtNAfCJw3NFMCKW3MnZV21UvmuYAGsl6zDBc5rHI8VXNo5GTP0Vv1xd8zdcCEQeMxGc8EtO4HFRmGns8_HOWJrb7S8PL0raRjANDw6wMwRNfn76LJZLoCE--7dZaHzx3FD5U5hillXcFEOC6y-nPkkl7paT6xTi-xDbL1aknrOIuoW1Z1i_BfWlU3ID1BnfpkZZkq6CvnkPPn-lUogL52CkXtFD0SX7iQIgzXQqvZKeT1Y88RTOJqZp5lu3zDyH92fYoT7JR820GWWLPrzFWI21E2birGZXQ1v0FUYXe_CXJOhEU5Qg-BgN2-KkUdi5I8O0-aFZURluLXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
ساخت پروکسی رایگان با Cloudflare!
⚡️
توی این آموزش یاد می‌گیری چطور فقط توی چند دقیقه پروکسی خودت رو بسازی.
🚀
🔗
لینک ویدیو:
https://youtu.be/8JytQZ1unz0
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1936" target="_blank">📅 18:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1935">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q06nmM1IXlR4srh_qvvgVANISGpnh34GGnP89m8onXj2z9m-LyW4wZBFA3exo_vICFcIGS1SsVhDvqixKdgQA3uD1Qia2dMEwoKOw-AtY9QmhHvLz9rVRSMTRXFPhl_-e00kaioqa2WDzR9DwmJSdwZdCkGMudMVn9J82A8Q91fqt4R5kpJzmM4bacUPViABTSv8l_vCD21t23lRCWg0_VVw_hCW0nsmPXJcHvB-JBBkLOYTCV991r1cpX9VIzNaG4RKeK7-7hrDmthtuqkbYPPyH6A_HE0pAU3vWL5prVSL3F_aBOeBps8a-g18Ke8rjYwC6dQ7Yn3Vb9yZREuU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی ویدیوی جدید رفتیم سراغ CoreForge، یه اپلیکیشن کاربردی برای آیفون که از روش‌های مختلف اتصال، از VPN معمولی تا DNS Tunnel، برای شرایط متفاوت اینترنت ایران پشتیبانی می‌کنه.
🔥
از نصب و تنظیمات تا قابلیت‌هاش رو بررسی کردیم.
📹
تماشای ویدیو:
https://www.youtube.com/watch?v=yPLb4z4nF70
📱
کانال برنامه:
@coreforgeios</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1935" target="_blank">📅 14:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1934">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PattNG_2.3.10-P63_arm64-v8a.apk</div>
  <div class="tg-doc-extra">73 MB</div>
</div>
<a href="https://t.me/whitedns/1934" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/whitedns/1934" target="_blank">📅 04:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1933">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">PattNG v2.3.10-P63
منتشر شد.
تغییرات اصلی
:
۱. با تغییرات انجام شده امکان اتصال به پروتکل MASQUE-HTTP/2 روی اکثر نت‌ها امکان پذیر شد.
همچنین پروتوکل جدید
Wireguard-Over-Masque (new gool)
اضافه شده، اتصال به این پروتوکل به شما ipی غیر ایران میده، در نتیجه برای دور زدن تحریم‌ها نیاز به چین کردن آن با سایفون و یا سایر کانفیگها ندارید (نوع HTTP/2ش رو اکثر نت‌ها وصل میشه).
۲. کانفیگ‌های اتر (warp/psiphon/tor) را اکنون میتوانید به سادگی از طریق exit-node با هر کانفیگ دلخواهی از همان منوی اتر چین کنید:
selected-config -> warp/psiphon/tor
(برای برعکسش همچنان باید از قسمت add proxy chain اقدام کنید)
///
فرگمنت به طور کامل روی فایروال همراه اول حتی روی IPv6 هم بسته شد، در نتیجه فعلا تا انتشار متد جدید امکان استفاده از Serverless-for-Iran رو اکثر نت‌ها مقدور نیست (همچنان برای دسترسی مستقیم به یوتویوب برای سرعت و حذف تبلیغاتش میتونید از Mitm-DomainFronting استفاده کنید)
///
با توجه موارد بالا پست
https://t.me/patt_channel_x/166
هم آپدیت شد.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/whitedns/1933" target="_blank">📅 04:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1931">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eaahi2S6ftxREmrWhVvQ7ufxodfbA6-MF2ADk8GAOuziXVB5Ty4vfj4Ftpt_gjuzmg_QW9Uce5eqpY4Rucy1DB2--HRzaS01p712q4-s0ltrhp0jppOuxbw0Fnxox0hIv8AqyxbjH1ygpDDY34wLDSxWa_NPyGKIPt93NXe4SbofO7Z0EA8PeYYFzfv0Zwf6A3FM610HGSZjVSbXEes41resHqqNj4_eQvwq8ptm0YssPmoswo3z44hDhi_EvIMtTM0HPSgL3q1FdM-h82gceAoqTDiZAJtX5qzupBjD-rIJ4mwxjMz13ldI8EI12ZHEixamvntyfYaPFrue49-W3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lzmgOsJTt80BhwwTJrpTLAqArDFyf2BUvhNJmf_x9UdxqQ-O9Je82_unUswDOvvi6cW2uvriFk8IP9BPsXGw5d1g2Z_ZtC3CcvIL-HhpMLy-xXKBAPdD_5dp6989-4ABKfDxT-ANF_W-QA-3nofcllNwpBeZd3bxv12iNeI0_ZqEDxohLyx-MoQkixj954aQpsTV0O8P1WrPmW3hN45xRHJfCTpW2Zb2FgpAjMIfTbrQiddVgv95JuwOMZRNIBDnMg7Is9IyER5BKo3Nf7fPlTW8R3D476HMZHeV43kRkOBslMAAFS87l-n9RSb6dP0cyIoDoo5BTHxw_xsN0CEzeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این تصاویر هم مربوط به تغییراتی هستش که باید در کلاینت MahsaNG ایجاد کنید دوستان گرامی</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1931" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1930">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">درود بر همگی دوستان عزیز
😊
یک راهکاری را یکی از بچه های کانال پیشنهاد داده
اسمش رو نمیشه «متد» گذاشت، ولی راهکار خوبی هست.
میتونید امتحان کنید امیدوارم برای شما هم کار کنه
مرحله ۱ — آماده سازی کانفیگ
ابتدا یک کانفیگ از هر پنلی که میخواید (مثلاً BPB و ...) بگیرید و متد Fragment + Fingerprint رو روی اون اعمال کنید. برای این کار، نصب کلاینت PattNG لازمه:
🔗
https://github.com/patterniha/PattNG
مرحله ۲ — آموزش اعمال متد
۱. کانفیگی که از پنل گرفتید رو در کلاینت وارد کنید.
۲. روی آیکون ویرایش (مداد) کانفیگ بزنید و مقادیر زیر رو اعمال کنید:
address:
188.114.97.6
(or any clean ip)
finalMask: tlshello-0-len
fingerprint: unsafe
cipherSuites: semi-python
۳. بعد از اعمال، یک تست بگیرید و سرعت رو بررسی کنید.
⚠️
نکته: من به تازگی متوجه شدم سرعت متد افت کرده — و به نظر «فیلترچی» عاملش هست، بگذریم!
😅
برای افزایش سرعت این متد، دو راهکار داریم:
راهکار اول — ساخت کانفیگ ترکیبی (Chain)
۱. یک کانفیگ «اتر» با قابلیت سایفون روشن و پروتکل WireGuard بسازید (نوع پروتکل برای هر اپراتور فرق داره، نوع اتصال سایفون هم خودکار).
۲. کانفیگ ساخته شده رو در کلاینت، از بخش «افزودن کانفیگ»، گزینه یChain Proxy رو انتخاب کنید.
۳. دو کادر خالی ظاهر میشه:
- یک اسم دلخواه بذارید (پیشنهاد من: «فیلترچی احوال مادر گرامی چطوره؟»
😄
)
- در کادر اول: کانفیگ BPB که متد روش اعمال شده
- در کادر دوم: کانفیگ اتر
- بعد دکمهی Save رو بزنید.
۴. حالا سرعت رو روی منطقهی خودتون تست کنید. اگه کارتون رو راه انداخت که عالیه؛ اگه سرعت ضعیف بود، برید سراغ راهکار دوم.
راهکار دوم — کلاینت مهسا NG
۱. کلاینت MahsaNG رو از گوگل پلی دانلود کنید:
🔗
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
۲. همون کانفیگ BPB که متد روش اعمال شده رو کپی و در مهسا NG وارد کنید.
۳. نحوهی انجام کار رو به صورت تصویری براتون میگذاریم
موفق باشید!
🚀
به امید آزادی
🫡
@whitedns</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1930" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1929">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!  نسخهٔ مک ForgeCore از ریویو اپل گذشت و حالا روی TestFlight در دسترسه.
🚀
📥
دانلود و نصب: https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید: اول اپ رو کامل پاک کنید، بعد از لینک بالا دوباره…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1929" target="_blank">📅 08:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1926">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCoreForge</strong></div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!
نسخهٔ مک
ForgeCore
از ریویو اپل گذشت و حالا روی
TestFlight
در دسترسه.
🚀
📥
دانلود و نصب:
https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید:
اول اپ رو کامل
پاک کنید
، بعد از لینک بالا دوباره نصبش کنید. بدون این کار ممکنه نسخهٔ جدید درست بالا نیاد.
ForgeCore چیه؟
یه کلاینت شبکه برای وصل شدن به سرورها و کانفیگ‌های پروکسی/VPN خودتون:
- افزودن کانفیگ با
لینک اشتراک
،
QR کد
یا
لینک تکی
- تست
پینگ و در دسترس بودن
همهٔ کانفیگ‌ها
- پشتیبانی از پروتکل‌های متنوع
- اشتراک‌گذاری اتصال روی
شبکهٔ محلی و Personal Hotspot
برای نصب کافیه اپ
TestFlight
رو از App Store بگیرید و لینک بالا رو باز کنید.
🐞
اگه کرش یا مشکلی تو اتصال دیدید، همین‌جا بگید تا سریع درست بشه.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1926" target="_blank">📅 00:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1925">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3EbQcevKjtacMrXXwVdt0Ei2dgUy9F7AEb4drGHntoWfHos_ZRmdIWzSJvI_Lkk-3QbEe5aq0yKALQ4NTtUzc5H-IIZlCtEOOKpTqv3QX7FTK-nKKB13QY6XUoSytxGkXBcquLoMLlfk5OrJAVqlyErcdGnHeHMYEMUUcd91RfsLC4arLD-bH_LSaVlohERYrJPHjqf2q4MzTxoG5OOqsNJjA1_tiPweCSsxK79aoZNaO4bDc-egDec1l0GoNZNRdbkSRlSXnxM1vkC9Il3qvZgLDwTjQTbxvU42wsSS9nDkOcV2wNu7DW3-j5-4uhJvyo-_ALd9_jnpu4vAKTW1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
درود به همه رفقا...
بعد از محدودیت های اخیر در فیلترنت و محدود شدن بیشتر پروتوکل ها و روش های رایگان مربوط به کلودفلر و...
تصمیم بر این گرفتم تست های مختلف طی چند روز انجام بدم و بهتون بگم چه روش هایی/اپلیکیشن هایی متصل هستند تا کمکی به شما رفقا باشه.
بهترین اپلیکیشم اتصال برای همه
دیوایس ها(ios,android,windows) از نظر بنده:
📱
اپلیکیشن defyx vpn: هست،اپلیکیشن کامل و متن باز که از نظر من جای بدافزار هایی مثل جامپ جامپ که روی همه گوشیا نصبه باید از defyx استفاده کنید ویژگی xray و بروز بودن این اپ در
#فیلترینگ
کمک بزرگی میکنه
😍
لینک دانلود بر اساس سیستم عامل متفاوت:
👽
android:
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
🛍️
ios:
https://apps.apple.com/pk/app/defyx/id6746811872
💻
windows :
https://github.com/UnboundTechCo/defyxVPN/releases
🤝
اپلیکیشن بعدی Mahsang:
بهترین روش برای اتصال به مهسا روش هایی مثل سایفون داخل اپ هست که کاملا متصله روی همه نتا فقط نیاز که برنامه رو بریزید و از بالا گزینه P و روی حالت سایفون بزارید تا متصل شید اگر اون حالت جواب نده
#کانفیگ
های EMS در سخت فیلترینگ هم وصله.
🛒
دانلود اپلکیشن Mahsang:
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
🔥
اپلیکیشن white vpn:
اپلیکیشن بروز با هسته های بسیار خوب و داشتن ساب پیشفرض در برنامه برای وصل شدن در شرایط سخت
#فیلترنت
این اپلیکیشن هم کلاینت و هم روشی برای دور زدن محدودیت ها بر مبنا dns هست:
💻
گیتهاب پروژه:
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🙂
روش های کلودفلر و پترینها:
1️⃣
روش اول:
داخل پنل های کلودفلر(bpb) خود گزینه ECH رو فعال کنید مشکل وصل نشدن حله میشه مهم ترین پیدا کردن ip تمیز بر اساس نت هست بهترین اسکنر از نظر من:
https://github.com/ashanews9776-eng/asha_scanner/releases/tag/v0.8.3
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
2️⃣
روش دوم:(استفاده از ساب رایگان پترنیها)
پیشنهاد میشه این لینک ساب یا هر کانفیگی از نوع پروتوکل رو داخل اپ های خود پترنیها یعنی
pattng
/
pattn
بزنید اگر هم بلد نیستید میتونید از
ویدیو آموزش استفاده کنید
.
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt#Patterniha-F
💡
توجه:ممکنه بسیاری از روش های دیگه مثل وارپ(AETHER) یا حتی SERVER LESS رو نت شما کار کنه اما این بیشتر بستگی به محدودیت های اینترنت و منطقه شما داره این روش ها رو داخل این پست اشاره نکردم زیرا روی همه نتا متصل نیست و منتظر آپدیت جدید از CluvexStudio و patterniha برای هسته Aether و همچنین sni spoof میمونم و بعد از رفع مشکل معرفی میکنم.
@xsfilterrnet
🙂</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/whitedns/1925" target="_blank">📅 00:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1924">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔥
آپدیت مهم WhiteDNS
فایروال جدید، ترافیک DNS بالاتر از حدود ۶ کوئری در ثانیه را محدود می‌کند و همین موضوع باعث قطع شدن بسیاری از تونل‌ها شده است.
برای اتصال پایدارتر، برنامه را به آخرین نسخه آپدیت کنید
👇
📱
دانلود نسخه اندروید 1.6.4
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.4
💻
دانلود نسخه دسکتاپ 1.2.4
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases/tag/desktop-v1.2.4
⭐️
تغییرات و تنظیمات پیشنهادی
🔹
محدودیت نرخ ارسال کوئری
در تنظیمات پروفایل CottenDNS، گزینه Query Rate Limit را روی ۳ کوئری در ثانیه قرار دهید. ممکن است سرعت کمی کاهش پیدا کند، اما اتصال پایدارتر خواهد بود.
اگر با اضافه کردن Resolverهای بیشتر سرعت بهتر شد، گزینه Rate Limit Counts را روی Per Resolver قرار دهید.
🔹
تصادفی‌سازی زمان ارسال کوئری‌ها
گزینه Timing Mask را روی Light یا Strong تنظیم کنید تا زمان ارسال کوئری‌ها تصادفی شود و ترافیک شما ریتم ثابت و قابل تشخیص نداشته باشد.
🔹
تعویض خودکار دامنه
اگر دامنه سرور مسدود شود، برنامه به‌صورت خودکار به یکی از دامنه‌های جایگزین دریافت‌شده از سرور سوییچ می‌کند؛ بدون نیاز به ساخت پروفایل جدید.
🔹
اتصال پایدارتر
پاسخ‌های جعلی Domain Does Not Exist یا NXDOMAIN که فایروال ایجاد می‌کند، دیگر باعث حذف Resolverهای سالم هنگام برقراری اتصال نمی‌شوند.
👀
محدودیت نرخ ارسال کوئری و تصادفی‌سازی زمان ارسال به‌صورت پیش‌فرض خاموش‌اند. برای استفاده از آن‌ها، تنظیمات بالا را فعال کنید.
🖥
برای مدیران سرور
ابتدا نسخه سرور CottenDNS را به آخرین نسخه آپدیت کنید:
https://github.com/WhiteDNS/CottenDNS/releases/latest
• برای استفاده از Domain Rotation، دامنه‌های جایگزین را در ADVERTISE_DOMAINS قرار دهید
• مقدار ZONE_NS را روی Nameserverهای خود تنظیم کنید تا سرور به کوئری‌های نوع NS مانند یک DNS Server عادی پاسخ دهد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1924" target="_blank">📅 14:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1923">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مادر بزرگ ۷۰ساله من برای اینکه بتونه با بچش ۱۰دقیقه در روز صحبت کنه VPN استفاده کردن باید یاد بگیره.
باید استرس بکشه که الان قطع میشه، همراه خوبه یا سامانتل، باید بدونه سابسکرسپشن چیه، سرور چیه و ۱۰تا روش امتحان کنه تا به گوش من برسونه که 《مامان VPN من بازم قطع شده》
😭
لعنت بهتون که به دل کوچیک و بزرگ حسرت گذاشتید.
ببخشید یکم شخصیش کردم و میدونم این وضعیت دردسر هممونه و نه فقط من. شاید این در مقابل دردسر خیلی ها حتی چیزی هم نباشه.
خیلی از این متد ها مناسب افراد مسن تر با دانش کم نیست. تا جایی که میتونید هواشون رو داشته باشید
🥲</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/1923" target="_blank">📅 13:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1921">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-GUI_0.8.0_x64-setup.exe</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1921" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/whitedns/1921" target="_blank">📅 13:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1920">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EtuJ_UapLyzq-LiqlWJpmjZ0MzgkdTNTFM_M_40p276tKjRrWoLoFmEmDAQ873LpJGKFnMa_8qnCmV50w1sTNCXZFk5Eyqr4C9bUa_Zzphisu9_nm__8Ssqy02Z3jHFw04e8riL3j1SCzWxcw3ZcFykkBTqH3y-iDjdQ-_ljcw8HLNOpdFvZ6CtRRr-JejzzGL8WEh4kD1Anl-eLfBVl3YdzjpIUn5CE5gBqq-QBE-hAp8wBYNK-oXPgou9Y4brc2f77ER-yO5T5TdHJfnL2Cw1-XuGafCicJ8CUR9YjEuQUw4mIYufvUWeIIs1U8xZDptVEphhCK5hU7foLjRB0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/whitedns/1920" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1918">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/tUAghwZUkN2S7Bn9oUZiSjCFcvtJkKskXh_OOdYJ4GItneiXu0zQpeZ1graPSixcKcZLpbPCrZiLpaD-Ey3G7g3LHeUs0w6PsuJV_Wzm9nitHY-CXlYYe3zBG4fMyeL_SS3MLOOsIAqYIKsxis507PIR76fu-RZsFoDIMG7pC6sbtfLZ8TUgfIgOD0GcRMtSRt-WuU42sqnj51xmLDJETyq4NSvMAUm7u09R7piwMCSgCOdiFRZCsnCvs6JybEdM9-rQmdvQVM35lrNJxu9bqtcGBFLn3Smx2m7PFxmCGUMDGAyxglZHqDWWoNORQp10L-BeV19zkwRVfqrKjehYXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/XXu2HeGqNEDPTLAOj5eR5VHyM3dq4-MnUamo6BmsbFOIYUQHr-a5GXytweXPK-GntTWpemq0nGZrQwMuIBhbN2A9hE1yp4nMxUBeNcAkHNRS42gbvXUpjf5EFiWjUwoB8WDSRTn5H96yRMpph8wQsezY6Y7-xPzqt8R2TVfcUTv-_ZeCcPtZJUtaXuSFhdQmxMNT8EOFfr0lN_ure28dv6EB9EmuTa-6J9KpB7GYop2S04DKKZSq8wEcmA25kgv-P4yIVH8fcECGYTE7V9OOYkN9N8uSeXwroXCjdZGY2rIKgFiu2jT9wFhXxehRWtd6G6O_J2nNn-UVH0dXKagU8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان
🙋‍♂️
در نرم افزار
whiteaesther
اگر برای اتصال مستقیم با aether مشکل دارید، این احتمال وجود دارد که دستگاه شما به هر دلیلی روی اپراتور کنونی نمی‌تواند هویت WARP/MASQUE ثبت کند
📡
برای حل این مشکل برید routes  و اولی را روی تور  یا سایفون و دومی را روی aether بگذارید و دکمه اتصال را بزنید
⚡️
. صبر کنید تا سبز شود
✅
حالا شما هویت masque خودتان را دارید و می‌توانید از aether به تنهایی یا ترکیبی استفاده کنید
🚀
@whitedns</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1918" target="_blank">📅 13:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1917">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/h7c3VtZPEPOYeVsdEkQo-0xezwgxhOOT-7gTtTccJ4KNCQHMjfNdlkkxcMlNHIwuxfcKgvSCXaRFQYfqhnSMF8br3L43uf4Mtx7fClQVR0PEL4J8l-fEf5OXVGcJ6ei6lyXjxBpqQcdm2BYlBfvRfQKX8vQTw1Ne_zviQKiRDbPUrTMcMHNq3m-K9IzWdR0dpDLR5LXFAI6rKonEyFyDPSLwW5_WVl8PMgwXtHPWL2nEPspQiICy8SfXd9DpWQGCk4ZfXe3_x4W4cH1wcK34J_Dvier47ExzTzotw2QAUMGje5ZGZVBftuN4L1SnP1VOyGCHws-OuAcWU8NSBXh-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر WARP محدود شد، چطور از WhiteAesther استفاده کنیم؟
⚠️
طبق گزارش‌های دریافتی، ارتباط UDP با IPهای کلودفلر روی همراه اول محدود شده است. احتمال گسترش این محدودیت به اپراتورهای دیگر وجود دارد، اما هنوز نمی‌توان آن را قطعی دانست.
این محدودیت می‌تواند اتصال
WireGuard و MASQUE H3
را مختل کند؛ با این حال، WhiteAesther مسیرهای دیگری هم دارد.
۱️⃣ ابتدا حالت خودکار را امتحان کنید
در تنظیمات برنامه:
🔹
Traffic → Coverage:
گزینهٔ «کل دستگاه»
🔹
Routes → Carrier:
گزینهٔ «خودکار»
در نسخه‌های دارای این قابلیت، برنامه مسیرهای Aether، Psiphon و Tor را بررسی می‌کند.
⚠️
اولین اتصال روی شبکهٔ محدود ممکن است چند دقیقه( تا پنج دقیقه ) زمان ببرد.
⚠️
۲️⃣ برای اتصال مستقیم، MASQUE H2 را امتحان کنید
از مسیر زیر پروتکل را تغییر دهید:
🔹
Routes → Advanced → Preferred transport → MASQUE H2
H2 روی
TCP
کار می‌کند؛ بنابراین بسته‌شدن UDP به‌تنهایی آن را از کار نمی‌اندازد. البته اگر مسیر TCP هم فیلتر باشد، اتصال برقرار نمی‌شود.
۳️⃣ امکان استفاده از IPv6 را حفظ کنید
🔹
Traffic → Addresses → IPv4 + IPv6
اگر IPv6 روی اینترنت شما قابل‌دسترسی باشد، ممکن است مسیر اتصال باقی مانده باشد. انتخاب این گزینه داخل برنامه، به‌تنهایی روی خط فاقد IPv6 دسترسی ایجاد نمی‌کند.
۴️⃣ تکه‌تکه‌کردن دست‌دهی TLS را امتحان کنید
🔹
Traffic → Advanced → Split the TLS handshake → روشن
این گزینه ممکن است در برابر بعضی روش‌های فیلترینگ کمک کند، اما مسدودشدن کامل IP یا TCP را برطرف نمی‌کند.
۵️⃣ اگر اتصال مستقیم جواب نداد، حامل را تغییر دهید
در
Routes → Carrier
حالت دستی را انتخاب کرده و
Psiphon
را امتحان کنید. گزینهٔ دیگر،
Tor با پل خصوصی obfs4
است؛ معمولاً کندتر است و ترافیک UDP را حمل نمی‌کند.
نام و محل گزینه‌ها ممکن است در نسخه‌های مختلف متفاوت باشد.
⚠️
هیچ‌کدام از این روش‌ها اتصال را تضمین نمی‌کند. بسته‌شدن WARP لزوماً به معنی ازکارافتادن کل WhiteAesther نیست؛ نتیجه به مسیرهای باز روی اینترنت شما بستگی دارد.
تشکر ویژه از
@patt_channel_x
@whitedns</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/whitedns/1917" target="_blank">📅 09:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1916">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">پروتوکل UDP هم به طور کامل روی ip های کلودفلر بسته شد (فعلا فقط روی فایروال همراه اول)
در نتیجه امکان اتصال به warp از طریق پروتوکل wireguard و یا masque-h3 دیگر امکان پذیر نمیباشد.
برای پروتوکل masque-h2 نیز، امکان استفاده از ECH از سمت خود کلودفلر بسته است، بنابراین در حال حاضر فقط با استفاده از IPv6 میتوان از این پروتوکل استفاده کرد.
روشهای جدیدی که بزودی منتشر خواهد شد امکان اتصال کانکشنهای TCP را به کلودفلر فراهم میکنند، در نتیجه، میتوان از آنها برای masque-h2، کانفیگهای ورکر، cdn و به طور کلی تمام اتصالات TCP روی کلودفلر استفاده کرد.
حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/whitedns/1916" target="_blank">📅 09:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1915">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">PattNG v2.3.10-P59
منتشر شد.
امکانات اضافه شده
:
۱. مقادیر متد فرگمنت+فینگرپرینت اکنون به صورت آپشن تو خود اپ اضافه شده، بنابراین برای اجرای متد فرگمنت+فینگرپرینت کافیست:
address:
188.114.97.6
(or any clean ip)
finalMask: tlshello-0-len
fingerprint: unsafe
cipherSuites: semi-python
را انتخاب کنید، و دیگر نیاز به کپی پیست ندارید.
برای اجرای این متد روی کانفیگ‌های اتر نیز کافیست:
finalMask: tlshello-0-len
fingerprint: semi-python
را قرار دهید.
۲. اکنون امکان chain کردن کانفیگ‌های psiphon/tor/warp با هر کانفیگ دلخواهی به صورت
دو طرفه
برقرار شده.
به طور مثال برای chain کردن سایفون با یک کانفیگ دلخواه ابتدا باید یک کانفیگ psiphon-only بسازید و سپس از قسمت Add Proxy chain میتوانید آن را با هر کانفیگ دلخواهی به صورت
دو طرفه
chain کنید.
همچنان برای chain کردن سایفون با خود warp باید از همان منوی aether اقدام کنید (warp -> psiphon/psiphon -> warp)
۳. با توجه به فیلتر شدن دامنه دریافت کلید وارپ، اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) و یا حتی ech این محدودیت را دور بزنید و بدون نیاز به فیلترشکن مجزا کلید وارپ را دریافت کنید.
۴. به طور مشابه با توجه به فیلتر شدن دامنه masque-h2, اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) این محدودیت را دور بزنید و به پروتکل masque-h2 نیز متصل شوید.
امیدوارم حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1915" target="_blank">📅 04:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1914">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eqxTlPnZWRqnzWrZTcyPjow9UM-2mc6PfpjriY7XY5RzhiQOpL9EmgvDVEmvuwpNV1CQQRjKwNuVAaDwCUcIvsyoag8sqRugGI0MSfka7tg9X5w3Klkxiv3LZi4EziaLxelJo31fYlfkCMxEMCX6wgvIb2Q3uf5lgapK3XsrQIeaady_L4AjIaH11uuxZvsLvkXv2q_RctpVdtm0vFp5sO4mAV-Hr4aXpEdQNI6u08qenexUt_C-A1DdFEhTi-E9YY4zrV_v3prg0wYQYFqb2IEaEztAuc-P1C4F6-E18vPlQWCCNuC0Xn0kNcAerYJksnMWlZgSvExgqga3xoBTyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1914" target="_blank">📅 01:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1913">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👆
این کانفیگ ها را هم برای amneziawg روی آپ whitevpn امتحان کنید
یکی از دوستان خوب زحمت کشیدند این کانفیگ ها را بازنویسی کردند
❤️</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1913" target="_blank">📅 19:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1908">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-mx-free-5.conf</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/whitedns/1908" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/whitedns/1908" target="_blank">📅 19:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1907">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوستان عزیز:
به جز خود سرورهای whitevpn , الان ۶ موتور اضافه شده است که هر کدوم روی یک نوع اپراتور و یا منطقه کار میده
شما باید خودتون موردی که الان کار میده را پیدا کنید .
فیلترینگ مثل سالهای گذشته یک الگوی ثابت نداره و نمیشه یک نوع خاص از فیلترشکن را به شما داد که روی همه چیز کار کنه
ارادتمند
تیم وایت
❤️</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1907" target="_blank">📅 19:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1906">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn3.10.2026.conf</div>
  <div class="tg-doc-extra">2.8 KB</div>
</div>
<a href="https://t.me/whitedns/1906" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1906" target="_blank">📅 19:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1905">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-13.conf</div>
  <div class="tg-doc-extra">340 B</div>
</div>
<a href="https://t.me/whitedns/1905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1905" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1904">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-5.conf</div>
  <div class="tg-doc-extra">342 B</div>
</div>
<a href="https://t.me/whitedns/1904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1904" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1903">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-poll">
<h4>📊 دوستانلطف کنید اول این فایل ها را ذخیره کنید بعد از قسمت پروفابل - افزودن- amneziaWG  -وارد کردن فایل پیکربندی این فایل را وارد کنید و امتحان کنید که ایا وصل میشید یا نه</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1903" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1902">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-poll">
<h4>📊 کدام پروتکل(های) زیر روی شبکه شما کار میکند ؟</h4>
<ul>
<li>✓ سایفون</li>
<li>✓ تور</li>
<li>✓ Ssh</li>
<li>✓ امنزیا amnezia wg v3</li>
<li>✓ IKEV2</li>
<li>✓ سرورهای عمومی whitevpn</li>
<li>✓ سرورهای اختصاصی whitevpn</li>
<li>✓ اتر whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1902" target="_blank">📅 15:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1901">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ehwf4OCy4UejvlBGstPTlY7YF92cheHq9kLiX05_iFntnTP7SrvqXb-PsnkMQnajwyAK4ArF18cJ3E_QRqVyM7I6YACuICwzDQ5EpUN9vgEZ90QieuM-bGoEaSV6v3LpGWiWvE106jxzw-lACViZqsiyw3aIMyUfgbxz-Hvw0U4DTd8FyPE8cH9sgjMRwyt9stAL0OFi1cxka4yzo7XSTR0-pkNBkZhjua3w5lNnxFkY12wHmIpfPLJCo_zK4nKJgwyMvSNRbAKTTVgMiT4R2R1v2rX8DoFIQDX94LJgcdWsKcf33-rqN9FNkAdV5XZuGJl2LR_iTpqhVWk3ip0nLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای دسترسی به امکانات جدید نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 میتونید با مراجعه به تب "پروفایل" - "افزودن" آنها را مشاهده کنید
@whitevpn</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1901" target="_blank">📅 14:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1898">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.7.0-beta.1-universal.apk</div>
  <div class="tg-doc-extra">203.4 MB</div>
</div>
<a href="https://t.me/whitedns/1898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1898" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1897">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tymBqYO2bv0GQksFlhxFtK-RN3pW_5Bq60nHdE_CVB4FfaqUhOnruh8xJuPORG7w4NtNL0XnhWp8jl0vmI9HzVSnb1-fVez4WGhL3oVjcUtE-zlT6I7c0khuJn3zFyaQnDyUW1724J5MdcYbb8vtsg_6VpjzBrp3wQXbdpyAkFnMxX5Px_hz6NPCMGqn8wQD7ebFKHRzkd2DcQFVUltiPw9W76SoqGhPeCDHQLYMhG8jDPYhmnza7f-EutOdqGb6G7MrCewI00YtvqY-w1KufQ1yGSRvQryB302SxAU26phP3bMJoF279mjs5kEgQwetjDfVGgilBWueYxDoXNnxnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!
⚠️
🔥
در این نسخه، شش موتور اتصال در دسترس هستند:
Psiphon، Tor، SSH، DNS Tunnels، IKEv2 و AmneziaWG
✨
تغییرات اصلی:
• صفحهٔ یکپارچهٔ «پروفایل‌ها» برای مدیریت اشتراک‌ها و اتصال‌ها
• واردکردن کانفیگ AmneziaWG از فایل یا لینک
vpn://
• انتخاب کشور سایفون از فهرست
• هماهنگ‌سازی فرم‌های فارسی و انگلیسی و اصلاح نمایش گذرواژه‌های طولانی
• بهبود پایداری اتصال و قطع سایفون و نمایش ترافیک
⚠️
این نسخه
آزمایشی
است؛ بررسی کامل همهٔ موتورها روی دستگاه‌های مختلف هنوز ادامه دارد. برخی موتورها به سرور و کانفیگ سازگار نیاز دارند. نسخهٔ پایدار
1.6.10
همچنان در دسترس است.
⚠️
📥
دانلود نسخهٔ آزمایشی
اگر مشکلی دیدید، همراه با نام موتور، مدل گوشی و نسخهٔ اندروید گزارش کنید.
@whitedns</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1897" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1896">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RkqM5YifbgnPFuJLPznOB14WvbSWViHsuKo4NQJBYrosIVvUJ690i2_e0pIP6i24OgIKErrYc8-WuPewYzu-qxK9ifmtQX07uvW_mNJawtSKAJHUB4CNCcKL3ULk-RWRLWfssFuoviIn8NqrNYlOBm9lPpoZQlRDww2Z4grq6t6YYRXl1rSNKYaAfZ-RWUXW0Oe73e8yRarAHn8Ez9umGlUCsqx2Od2hCjDiwrgbfPBhQkHlmunPxdrMvVdk5qAoTMrH_h50O4gn8CJaAkUP6sxD7NPG_w7ej1iAh-I4cksM97_DiyhOXGQIkHKCtxR0GL59vLFXY0fHo0DHQvu3tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/whitedns/1896" target="_blank">📅 19:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1895">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BhB0FgOkUPxH6_-kLOWsydWu64Wflmd2Ws5INYhV-3bEQr9GNUQZPzuJ3gSWUhednxKU5a5JbqAAfsi_Zly6UdUcbYiWydR8cpOKzMjSEKvO6J3s4os3R6NkT5FSO5SPEY5axVc-xMlUc2Ip54LwhWm-n2CBZlogmx1f0tf1R1dw6u5iagzm1v2bSZkCywEhAcnb079wk1onWbFMraRIltpIWeCYIPaWw9XHsW3_cSNtuyAH-qDgoIeJW9cHeeaxkz9kB-YjYaLhWRLDvrWKErxkxCnwDEJqbyCs51DVu-BgAnVz_oa9qxipBIa5v7EI__zzfIOoCDD4CAXwUHvFdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری (مستر دی ان اس )
⚠️
⚠️
whitedns app config bot/ masterdns config   :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/whitedns/1895" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1894">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFxCKYmKtaz44ZmPYA3H2_vcrIfUTzAcscsH5gNunjTmP32Cwgx1aiNP3s_Roic8r-fcAgDg5Tn2I6Tn2TiclP7eGTJl7UeVSxKYTSSxPd1PzqZAwCkx7B0SPv81WcSzLTvMUe1PjttoZfzsf_CLcdnUHibNn7HLgHLctoC1D2muhZisY0ito4UUeChNXOEMuKizWHTzyKKKJjkGoIINfNND8PcRTfLh9dRKqdXc-xMsq8Ii3gf66wjHpYuOGMAjVMSXHkgU0Dijf_MOf9u3lroxSwgeTfh2Zp_S7zeSypQdxUsrmA2XwHxXpoiL3C_PzPmksH5Cq6WsHdYpDe7PMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/whitedns/1894" target="_blank">📅 17:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1893">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommmahdi_sz</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agzA6PXv2zGQ3P26FKaJrBvDv4v2JRZYFE8KUZoKZ1czAv__0psdQN4V1X3lJFnDPvSzZmskydL91UMzoASORAZVGZn2FYyJKiFWRtLqb1R35A5VEk9oBVYw-RtNC2O8owWIo-oNdC9_nFxCBJoJUb0DMDuSJNsYd531anq9yNaQLxs7lwNoNi7CCJtMaVPjQAc6tzckWdf72_SVF3D5rXVgogzoQ_8XzJte6WBQSZV5Ih3VZvn_Y0qlwh0Gr1balNHVI9jgrAifHIUEdrNd7dR4vuc4WwMWY2wawuA0XF-ZsFa_K5XCSFzi-mi5DVkAKnAUCXovqS-h0hWy-6borQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ArasClient | کلاینت قدرتمند اندروید
یک کلاینت مدرن و متن‌باز برای مدیریت کانفیگ‌ها، Subscriptionها و اتصال‌های مختلف، با امکانات پیشرفته برای تست و مدیریت سرورها.
➿
➿
➿
➿
➿
➿
➿
➿
➿
⚡️
Smart Connect
تست هم‌زمان کانفیگ‌ها و مرتب‌سازی بر اساس Latency برای پیدا کردن سریع‌تر گزینه مناسب.
📡
Subscription Management
مدیریت چند Subscription، بروزرسانی کانفیگ‌ها، نمایش حجم مصرفی و زمان باقی‌مانده و امکانات بیشتر برای مدیریت سرورها.
.arasc
فرمت اختصاصی ArasClient برای Import / Export و اشتراک‌گذاری کانفیگ‌ها با حالت Protected.
🔐
Per-App & Routing
پشتیبانی از Per-App، Routing، Proxy Chain و Policy Group در بخش‌های پشتیبانی‌شده.
🔥
پروتکل‌های پشتیبانی‌شده
VLESS • VMess • Trojan
Shadowsocks • Hysteria • Hysteria2
WireGuard • AnyTLS • AmneziaWG
MASQUE • Mieru • SOCKS • HTTP
➿
➿
➿
➿
➿
➿
➿
➿
➿
🌐
Aether / WARP
پشتیبانی از پروفایل‌های Aether و قابلیت‌هایی مثل:
• WireGuard / MASQUE
• ECH و Fragmentation
• Endpoint Scanner
• WARP Key
• Psiphon و Tor
📊
امکانات بیشتر
• تست و مرتب‌سازی جهانی کانفیگ‌ها
• نمایش اطلاعات اتصال و مصرف ترافیک
• تشخیص کشور سرور بر اساس IP
• Backup & Restore
• Dark / Light Theme
• Logcat و ابزارهای عیب‌یابی
• تنظیمات پیشرفته Core و شبکه
➿
➿
➿
➿
➿
➿
➿
➿
➿
😎
Open Source • Android
👩‍💻
GitHub:
https://github.com/ArasTey/ArasClient
🖼️
Telegram :
https://t.me/imArasTey
📥
Releases:
https://github.com/ArasTey/ArasClient/releases</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1893" target="_blank">📅 17:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1892">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مشکل ربات
@WhiteDNS_installer_bot
حل شد
با این ربات میتتونید ازطریق تلگرام روی سرور خودتون MasterDNS نصب و سرور خدتون رو مدیریت کنید.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1892" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1891">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOOWNVlNnS-6tV40S-hTtIuhw0fkPKgot36CCZb4-iQ30v4HPPIAaaNYvRE8_lPR5Yp84fD3SyjyH5UThDWjVGJQ0NcVVHkuGx2m3BvLqDin9p1PNncOCPaKZXH_nhE0wPmqOjBBprkfxj6995ycNXiIsW_VZjf6yRxu8GraiTpxgGu8mu27FTl7eQ2WWxNk6-XAM-VgSP15tavEKEt6KHaxYpYiM6pHKDFxmo1ZBQsWm5sD9iAdKn384_OHdFJbisa5ZJAEtrAi-FhMUW_8-apizxQ0hvo31XulXtoYXPZT5KlkULhbkMSqtPxYCDqMJqsLkZRd6CGWHLXxgkdgew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
آموزش جدید رسید!
🥹
✨
اسکن آیپی تمیز با WhiteDNS Scanner و استفاده ازش توی کانفیگ
🔥
💗
از نصب اپ تا تست نهایی، همه‌چیز مرحله‌به‌مرحله توی ویدیو هست
🎀
🎬
ببینینش:
https://youtu.be/GDo6p_z3CAw
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1891" target="_blank">📅 19:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1889">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوست عزیز :
خرید ، فروش ، درخواست خرید ، آگهی فروش هر چیزی که توش پول رد و بدل بشه ممنوعه
🚫
بلافاصله بن میشید</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/whitedns/1889" target="_blank">📅 15:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1888">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1888" target="_blank">📅 13:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1887">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1887" target="_blank">📅 13:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1886">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1886" target="_blank">📅 13:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1883">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1883" target="_blank">📅 13:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1882">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel WispByte.rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1882" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1881">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiTKH6oERHXlraVIwd7key6qyUUrIkw1MvTYP1QZZHand9FdVhPibt0LY1sTbLSgvD0EJc3Ox3SCS1w4ZP-gynEO1AMPnoYpg-GY2GyZrnKHkwyl8Lpv5twtN_ac2gnZAa3kANU1h-wOlQd1erWYAH0La65y7K5Lw9top2yUOlJ0SeXMdLH_xk6P9YMAviZ1yzXxUqNACpD8zuf0WrxqC_KgMOnmQazR62IcxLCY-1ZElTU1zcDMUk34YvaQwmt7lSfWgfDQk6_kA2BEycAw5pWvXi2_5M5RJvN7hufrt0oxpym0qHemoH3feTekbNN37r_dWuAMz6X9l9gXbc5qtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎀
بچه‌هااا یه آموزش خفن و کاربردی جدید دارم براتون!
🥹
💗
می‌خواین هاست رایگان بسازین و ازش کانفیگ V2Ray رایگان بگیرین؟
👀
✨
توی این ویدیو با Blue Knight Panel همه‌چیز رو از صفر باهم ساختیم و آخرش هم کانفیگ رو تست کردیم
😍
🔥
اگه این چیزا برات جالبه، حتماً یه سر به ویدیو بزن؛ قول میدم ارزش دیدن داره
🫶🏻
🎬
ویدیوی جدید رو ببین:
https://youtu.be/TmHM_yBPOUU
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/whitedns/1881" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1880">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">💬
تعدادی سرور اختصاصی جدید اضافه شد!
دوستان عزیز، برای استفاده از سرورهای جدید، لطفاً از مسیر زیر سابسکریپشن اختصاصی رو تازه‌سازی کنید:
✨
بخش سابسکریپشن
✨
سابسکریپشن اختصاصی
✨
دکمهٔ تازه‌سازی
🔄
فکر می‌کنیم ظرفیت فعلی برای همهٔ کاربران کافی باشه، ولی اگر نیاز به ظرفیت بیشتری باشه، حتماً سرورهای بیشتری اضافه می‌کنیم.
آی‌پی‌های این سرورها اختصاصی هستن و انتظار داریم باهاشون بتونید به‌راحتی به شبکه‌های اجتماعی و تمام ابزارهای هوش مصنوعی دسترسی داشته باشید
❤️</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/whitedns/1880" target="_blank">📅 11:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1879">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-poll">
<h4>📊 الان با چی وصلین ؟</h4>
<ul>
<li>✓ whitevpn</li>
<li>✓ whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1879" target="_blank">📅 11:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1878">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
۵۰ سرور اختصاصی اضافه شد!
دوستان عزیز، لطفاً تست کنید و نتیجه رو به من بگید. موقع فرستادن نتیجه، اسم اپراتورتون رو هم بنویسید تا بهتر بتونیم وضعیت اتصال رو بررسی کنیم
🙏</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/whitedns/1878" target="_blank">📅 07:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1877">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌎
سرور IPهای اختصاصی ری‌استارت شدن
🔭
برای دریافت آخرین تغییرات، برید به:
سابسکریپشن ← سرور اختصاصی ← دکمه تازه‌سازی
بعد از به‌روزرسانی، دوباره وصل بشید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/whitedns/1877" target="_blank">📅 03:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1875">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚠️
دوستانی که از نرم افزار whiteasther استفاده میکنند و مشکل ورود به وبسایت ها و یا سرویس های  تحریمی دارند
:
🔥
با یک سری تغییرات که روی سرور exit chain  یا همان زنجیره خروج  دادیم . احتمالا مشکل خیلی از دوستان حل خواهد شد
🛠
برای این منظور کارهای زیر را انجام دهید :
1. وارد ربات
@WhiteDnsChainbot
شوید و کانفیگ(های) مورد نظر خود را انتخاب و دریافت کنید
📥
2.در تنظیمات اپ whiteaesther به مسیرها-زنجیره خروج و در نسخه دسکتاپ به قسمت پیشرفته - زنجیره خروج  بروید و ادرس ساب خودتون را وارد کنید
⚙️
3.کانکت شوید
🚀
موفق باشید
🙏
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/whitedns/1875" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1874">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1874" target="_blank">📅 13:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1873">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">💬
با از کار افتادن سرویس های BPB فشار بیشتری روی سرور های اختصاصی هستش (شاید براتون کار کنه و شاید درست بشه).
ما سعی میکنیم کیفیت سرویس های عمومی رو بیشتر مدیریت کنیم و از شما هم میخوام اگر مایل هستید به ما کمک کنید.
❤️
تنها راه کمک به ما سرویس Patreon هستش و فقط برای ساکنین خارج از ایران قابل دسترسی هستش.
🗺
امروز به ما ماهی ۲۲دلار بهمون کمک میشه اما ماه ها بوده که هزینه های ما بیشتر از ۱۰برابر این هستشو همش از هزینه شخصی پرداخت شده و تا جایی که بتونیم ادامه میدیم.
https://www.patreon.com/cw/WhiteDNS
یک سرور آمریکا
🇺🇲
جدید اضافه کردیم و سرور هایی که براتون کار نمیکرد رو حذف کردیم.
برای دسترسی به سرور جدید، به بخش سابسکریپشن برید و ساب اختصاصی رو بروزرسانس کنید.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/1873" target="_blank">📅 13:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1872">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👀
یه تغییر آزمایشی روی
سرورهای اختصاصی
دادیم
فعلاً تعداد سرورها به
۴ سرور
در این کشورها کاهش پیدا کرده:
🇺🇸
آمریکا |
🇸🇬
سنگاپور |
🇫🇮
فنلاند |
🇩🇪
آلمان
آی‌پی این سرورها
هر ۲۴ ساعت یک‌بار تغییر می‌کنه
تا احتمال فیلتر شدن کمتر بشه.
قبل از تست، حتماً اشتراک رو به‌روزرسانی کنید:
بخش اشتراک‌ها → اشتراک اختصاصی → گزینه «تازه سازی»
بعد از به‌روزرسانی، سرورها رو تست کنید و نتیجه رو بهمون بگید
🙌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/1872" target="_blank">📅 06:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1870">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان سلام :
ما برای کانفیگ whitedns ربات داریم
@MasterDnsManager_bot
این کانفیگ ها یک روزه هست ، با حجم محدود
⚠️
به درد افرادی میخوره که هیچی براشون کار نمیده و با یک سرعت خیلی خیلی پایین فقط می‌خوان یک وبسایت چک کنند و یا تلگرام اخبار بخوانند و یا پیام متنی بدهند
این روش سرعتش در بهترین حالت ممکن شاید به ۵۰۰ کیلوبایت برسه
عده ای از دوستان درخواست میفرستند که برای روز مبادا می‌خوایم ، که درخواست رد میشه ، توضیح دادیم که دوستان دلخور نشن
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/whitedns/1870" target="_blank">📅 14:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1869">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/eUACdYthLJdceY-7ZW8dMukaD-MqvbC2jN9h7DZxnkE57pP8TvVGmE2Y0EU7cWG2f5aaiVSKiSPJGd4X3HB8JzXPM3LhxDLaLciif9MA0s6fEBA9wBVNavJeo0zMPvL9LZbSq0IEJIHEfcR1aChQKGhy0KSWDqyM-iqW18kQshuadRXf1cjeLA3uH_KXoqIInSoJYkXDKvnWH9Z8AMWqqHcyltVOscdqsZpHt2QaWrcBAFCaEpPC3LfoUBWeeZ1gthVKQntirRdaQi_fijdCsAX2EdlOnjZTVyPxLl_gH0_BFjuZFTOs7ATPfFPdt41KW__nf2ltU_Sk36xl8y93tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه پایان فعالیت ربات
@WhiteDnsResponder_bot
کاربران و همراهان عزیز،
به اطلاع می‌رسانیم که فعالیت این ربات و خدمات مرتبط با آن از امروز به‌طور کامل متوقف می‌شود و پس از این، هیچ‌گونه سرویس، پاسخ‌گویی یا پشتیبانی از طریق این ربات ارائه نخواهد شد.
از اعتماد، همراهی و بازخوردهای ارزشمند شما در تمام این مدت صمیمانه سپاسگزاریم. حضور شما نقش مهمی در مسیر فعالیت این پروژه داشت.
با آرزوی بهترین‌ها برای همه شما
🌹
تیم WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/whitedns/1869" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1868">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مهم "
⚠️
⚠️
⚠️
📢
راهنمای تست اتصال WhiteVPN نسخه 1.6.10
لاگ‌های ارسال‌شده از چند دستگاه، نسخهٔ مختلف اندروید، وای‌فای و اینترنت همراه بررسی شدند. در بسیاری از موارد، کاربران فقط چند ثانیه بعد از زدن دکمهٔ اتصال، آن را دستی قطع کرده‌اند؛ درحالی‌که برنامه هنوز مشغول بررسی سرورها بوده است.
در نسخهٔ 1.6.10 برنامه ابتدا سرورهای اختصاصی را آزمایش می‌کند و اگر آن‌ها پاسخ ندهند، سراغ مسیرهای جایگزین می‌رود. این فرایند در شرایط فعلی اینترنت ایران ممکن است
تا دو یا سه دقیقه
طول بکشد.
لطفاً برای تست دقیق، مراحل زیر را به‌ترتیب انجام دهید:
مطمئن شوید نسخهٔ نصب‌شده
WhiteVPN 1.6.10 (85)
است.
وارد تنظیمات برنامه شوید و گزینهٔ
تعمیر اتصال / Repair connection
را اجرا کنید.
بخش
Split Tunneling
را موقتاً خاموش کنید.
در بخش انتخاب موقعیت، گزینهٔ
Automatic / خودکار
را انتخاب کنید.
اگر امکان انتخاب سابسکریپشن دارید، فعلاً
سابسکریپشن عمومی WhiteDNS
را انتخاب کنید.
دکمهٔ اتصال را بزنید و تا
سه دقیقه کامل
برنامه را قطع نکنید.
هنگام اتصال، بین وای‌فای و اینترنت همراه جابه‌جا نشوید و برنامه را از Recent Apps نبندید.
اگر پیام «متصل» نمایش داده شد، حداقل ۳۰ ثانیه صبر کنید و سپس موارد زیر را آزمایش کنید:
بازکردن یک سایت در مرورگر
ارسال یک پیام در تلگرام
بازکردن یک سایت خارجی دیگر
⚠️
اگر برنامه متصل شد ولی اینترنت یا تلگرام کار نکرد:
لطفاً اتصال را بلافاصله قطع نکنید. در همان وضعیت متصل:
اگر برنامه «متصل» شد ولی اینترنت کار نکرد، اتصال را قطع نکنید. در همان وضعیت، از همان گزینه‌ای که قبلاً برای
کپی و ارسال گزارش اتصال
استفاده کرده‌اید، لاگ را کپی و برای ما ارسال کنید. سپس نوع اینترنت، نام اپراتور، مدل گوشی، نسخهٔ اندروید و اینکه سابسکریپشن خصوصی یا عمومی انتخاب شده را بنویسید.
آیا هیچ سایتی باز نمی‌شود یا فقط تلگرام مشکل دارد؟
آیا حالت Always-on VPN یا «مسدودکردن اتصال بدون VPN» فعال است؟
اتصال با سابسکریپشن خصوصی انجام شده یا عمومی؟
اگر برنامه بیشتر از سه دقیقه روی «در حال اتصال» ماند، باز هم ابتدا گزارش را کپی کنید و سپس اتصال را قطع کنید. گزارش‌هایی که بعد از قطع اتصال گرفته می‌شوند ممکن است بخشی از اطلاعات اصلی خطا را نداشته باشند.
بررسی‌های فعلی نشان می‌دهد تعدادی از مسیرهای اختصاصی
AnyTLS
داخل ایران پاسخ پایدار ندارند. در چند آزمایش، سرورهای اختصاصی شکست خورده‌اند ولی برنامه پس از انتقال به سابسکریپشن عمومی با موفقیت متصل شده است. به همین دلیل تا زمان اصلاح مسیرهای اختصاصی، استفاده از
سابسکریپشن عمومی
پیشنهاد می‌شود.
همچنین اگر از نسخهٔ 1.6.9 استفاده می‌کنید و برنامه «متصل» نشان می‌دهد ولی دیتا ردوبدل نمی‌شود، حتماً به نسخهٔ
1.6.10
به‌روزرسانی کنید. نسخهٔ 1.6.9 در بعضی شرایط ممکن بود اتصال ناموفق را به‌اشتباه متصل نمایش دهد.
از ارسال گزارش‌های دقیق شما ممنونیم. این گزارش‌ها مستقیماً برای شناسایی اپراتورها و مسیرهای مسدودشده استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1868" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1866">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚠️
🔥
تعدادی از دوستان به خاطر فیلترینگ شدید توی منطقه ای که زندگی میکنند توی نسخه 1.6.9 دچار مشکل شده بودند .
کانکشن برقرار میشد ولی ترافیک نداشتند .توی نسخه 1.6.10 این مشکل به طور کامل رفع شده است و احتمالا خیلی از کاربران مثل نسخه های گذشته به راحتی متصل خواهند شد
دوستان تا ما مشکل سرورهای اختصاصی را حل کنیم فعلا از سرورهای عمومی استفاده کنید
⚠️
دوستان چنانچه هنوز برای اتصال مشکل دارید لطفا با نگه داشتن انگشتتون روی دکمه اتصال لاگ برنامه را کپی و برای ایدی ادمین که توی بایو هست بفرستید
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/whitedns/1866" target="_blank">📅 11:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1863">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/whitedns/1863" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/whitedns/1863" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1862">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GS0vYD1gj-mmxe9V4QAbydza1D4M7pha-9CzN_1MFc98vLfn8aiVWCgv8pqEn4pjG0uSkTVJN2cLFT8yk6nytDKfgZrSCWcdPGQGFGTyHubPqt23u-2rSnwhOOIZ0WdXuYozH7gAR9u5PT1CKITeJdws9mHaJvvqYKOWIGVAOOE1Ev9biHoYhVNW2q9XskFDRI4yx6k2sHgXUqZloQ0CUbo-4AZZwoFyEokzP0zpLtLtxvku2jRimCZjC6BGJ--aszZ9scqAfaPtEhtWOAUPhygjqf_tGuyjO271DCStSAi258TFKDM-znfbq8-EAJvAmn_RLBwikZuv8et4Y0kY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/whitedns/1862" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1860">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PZUNGyaHhDxABhIoCary_egDz9jwoNGb8CO1M1PQQVCReOTecr6w_AipAJ7x2R0OjsiwUND0Wfe-pY_JjMRKQjMjPmORkBrcfjM2GI0lTIvIEpUUS_9Vw38Fnz5wjmxEuINq6SRfe4LrEtGEQnYn0UQQC9g0KY9Qh7r6nT7oFf1tN9yASzHRmc7WiHCRh_vdqUTh43vn8OVrM2ABi3EMJahpw3T0R93aFDkT1DcJq8PpPQ-YUT6iVMBmN3fwjq9GPdafvGyazQGa-coVErEGT_LxvzMCLGRy6G7xDvdLE8Ns1HDHPlTNVAK9hybx5Xyx2e2QJKL-7J12LeWswxI_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/1860" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1855">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.10.0-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/whitedns/1855" target="_blank">📅 11:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1854">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GDyJ-B4g303KZ_Zm_ZFoXbz6yG-ZnY1vimBvo4sfyf7QYedyg7IbdgCrrA1fFlGo010yRdV_LssE27Ws3gjn4HLq8vPIme0z8CwJY4p2q1O27YA-n4Pgf989tamgpAOyKffCqGmTMurA3LYJhFiu2pq8wox0mQQC20XdJ9HsbXFaXKkIjniw_BN9v2pPROic6mfz96ghSJW9qpQ6cvffnNZEub18pjKTme9UlAGrWhvhwYsrDPPO24C7xcb_2YJkEevbSMidlt7Y2J-rg67HJsWrmxeype0N_OkB-VEREPPpJ0xlYQGw2-mk4hietaAuD504HknVD5rNZoh81yyegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Whiteaesther mobile v 1.10.0
حالت خودکار حالا جست‌وجوی مسیر را ادامه می‌دهد و مسیر موفق هر شبکه را به خاطر می‌سپارد
🧠
پایداری اتصال بهتر شده و سرعت دانلود و آپلود در اعلان برنامه دیده می‌شود.
📶
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.10.0
@whitedns</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/whitedns/1854" target="_blank">📅 11:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1852">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-poll">
<h4>📊 الان با چی وصل هستید ؟</h4>
<ul>
<li>✓ اخرین نسخه whitevpn</li>
<li>✓ اخرین نسخه whiteaesther</li>
<li>✓ اخرین نسخه whitedns/coreforge</li>
<li>✓ هیچ کدام</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1852" target="_blank">📅 18:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1851">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آمار اتصال ها داره برمیگرده به حالت عادی
❤️</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/1851" target="_blank">📅 13:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1850">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.  لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید.…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1850" target="_blank">📅 12:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1848">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piTKo1WLs3hZteGe7ljug-TithJ5NOlFryOWbQT3vCKAH818mTkrk3rd7CH900eQLMO-2y-NVMVTKmI0bXaH3Upf_AKrJy7jelM-b3w_BwzLcQpuIamz-Fhg-epWSuyPM5IQhriNaTz4U-9zSA4kbf_cqW-L4KP-h_M0HoUuB1OSUmEgBSOTdDF0NkJ2oXl-i4p_jhv7j-0TWpcWdwueXZXrrCHFMWdHr7GYe2JOu-ZS2km76lO8e1n5y8FPn5Pe34Y2RF_LbYirtGrTFN00_ckjAZByWA7pl-Xa0vgPRFxUgXgaEq9u6NTujM-T73wKw5tbcBSJgHpWZgszZ7LUOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.
لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید. نسخه جدید رو می‌تونید از صفحه GitHub ما هم دانلود کنید:
🛡
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.9
💬
بعد از نصب نسخه جدید، اگر هنوز مشکلی داشتید لطفاً بهمون خبر بدید. گزارش‌هاتون کمک می‌کنه مشکل‌های باقی‌مونده رو دقیق‌تر پیدا کنیم.
ممنون که با گزارش‌هاتون کمکمون می‌کنید
🤍</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/whitedns/1848" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1847">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/m2mBjxFolWyUbx_-WqP1VlA1BDbQEVy39nr2ICW-THTwRDIsGSdvwcFMGT-fTyUuIoT4U7CSbIlht-1eFLGpdgT8WWd7spQzkzrtDWBAwsMu6zXZqw1V6GWfzUa7MeKNup-tymOvlEVcUDRhvSywoLoLcaapPe6F8QyEyACHmQM2Cu2KjBa6CY-xcCiHIN-kW_9JlWrqG-pBiCVbItzK0_Kz7eU1mJ35UWQmkS4rAY2qMrLLgZ-YFvtFTXGmikAcN3M5o8JgIClQSpR03UNvpL0FR6vMem2dU1C2-DK9zeFO36n8Kx3SXVfGlkRrwtf8XO8_Lrb1gC7FANdfm-PpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی whiteaesther desktop 1.9.7 pre-release
⚡️
اتصال باید خیلی سریع‌تر شود
کلادفلر در همان جواب ثبت‌نام، آدرس دقیقی را که به دستگاه شما داده اعلام می‌کند. موتور آن را می‌خواند، ذخیره می‌کرد، و بعد نادیده می‌گرفت — و به‌جایش حدود ۲۵۰۰ آدرس را یکی‌یکی امتحان می‌کرد تا یکی جواب بدهد.
🔑
و مشکل «دیگر نمی‌توانم ثبت‌نام کنم»
اگر تا حالا پیش آمده که بعد از چند بار نصب مجدد یا اتصال ناموفق، برنامه اصلاً نتوانسته شناسه بگیرد — این همان بود.
ثبت‌نام همان لحظه‌ای که سرور جواب می‌داد خرج می‌شد، ولی تا چند مرحله بعد روی دیسک ذخیره نمی‌شد. اگر وسطش چیزی قطع می‌شد، ثبت‌نام رفته بود ولی شمرده شده بود. و چون سهمیهٔ کلادفلر روی آی‌پی است، همین می‌توانست گوشی روی همان وای‌فای را هم از کار بیندازد.
حالا اول ذخیره می‌شود، بعد بقیهٔ کارها.
🛡
و یک حالت خراب که دیگر ممکن نیست
قبلاً اگر با وایرگارد وصل بودید و MASQUE را امتحان می‌کردید، هیچ‌کدام دیگر کار نمی‌کرد. ساختار جدید طوری است که این وضعیت اصلاً قابل ساختن نیست.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.7
⚠️
نسخهٔ آزمایشی است — در فهرست به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد.
شناسهٔ فعلی‌تان خودش منتقل می‌شود؛ کاری لازم نیست بکنید و چیزی پاک نمی‌شود.
💬
اگر اتصال سریع‌تر نشد، یا هر چیز عجیبی دیدید، بگویید.
@whitedns</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1847" target="_blank">📅 12:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1845">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/tPWarNJdcj901ioQQUroGjfsFLBtmYUN7A8136saFPxtPjLwCNfLfEB7FiJYDHqasqwTx1TtpFml65RVTVtV9GsRrTZ929gjeIEbITAScmhRav_FAnaQu3W9J4e1M_VozoP6rtyOw7NW6NdiwZDOEDxHvr0T1EBNXIADhkquq3ounkOBWaGw9_gWOYeMrI8D2blu_WPL389W5kk7JU240HC-jogaA3nA_127QlEPnn50dJDnKrYEnpsW4wwzdBodfZRCbqLt38zKjGt-NmZ1NCyd6nrViji5yf_-GRb1_84NZL3CDgik58gEjSSXrGxsIj3YLTkCy5_lLUSP3VTp2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/V0kMcAaEHMLNOiLyoLzJVCEu-8k5eTjsxX2eBSSAE-fpUYlYJQGL98MXrukozZbBQ7bxsde4RyJFd78bB6ibvaOJ_c1ZTZDLPazAINuiqzK4-oI6AKgsg3gvvux-YWIxgVPWQtOYI2gGt9QHGieWs8v9CopuzD3_Fs9h3gFM1KPpz5v76zD7pdlRZ6LyymPYPFeNqAbFXxMrFNbNKrch6kwSpRByNWB-1-9oscTaxi-urgOnQbOKA1j8SC6Sj9COylv53_4S38YQzn4FPhK8Fr8URUM6e12PKHLjaSE6d0pJSwNJINpwp9MbbYrBpd15O8X4V1xw8YDRvDQ-aTdfmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚠️
یک امکانی که توی اخرین نسخه ازمایشی whiteaesther موبایل و دسکتاپ تقویت و بهینه سازی شد - امکان ست کردن dns بود که تقریبا هیچ کس بهش توجه نکرد جز یک گروه خیلی کوچک به نام گیمرهای عزیز
😁
😃
از این امکان استفاده کنید حتما خیلی از مشکلات شما را حل میکنه
🤓
لیست dns های عمومی :
۱. DNSهای عمومی و معمولی
Google
8.8.8.8
8.8.4.4
Cloudflare
1.1.1.1
1.0.0.1
Yandex
77.88.8.8
77.88.8.1
Quad9
9.9.9.9
149.112.112.112
OpenDNS
208.67.222.222
208.67.220.220
AdGuard Unfiltered
94.140.14.140
94.140.14.141
Control D
76.76.2.0
76.76.10.0
DNS.WATCH
84.200.69.80
84.200.70.40
DNS.SB
185.222.222.222
45.11.45.11
AliDNS
223.5.5.5
223.6.6.6
DNSPod
119.29.29.29
—
Hurricane Electric
74.82.42.42
—
Comodo Secure DNS
8.26.56.26
8.20.247.20
Neustar UltraDNS
156.154.70.1
156.154.71.1
LibreDNS
88.198.92.222
—
360 Secure DNS
101.226.4.6
218.30.118.6
OneDNS
117.50.10.10
52.80.52.52
Quad9 Unfiltered
9.9.9.10
149.112.112.10
DNS4EU Unfiltered
86.54.11.100
86.54.11.200
۲. DNSهای امنیتی، ضدتبلیغات و خانوادگی
Yandex Family
77.88.8.7
77.88.8.3
Cloudflare Security
1.1.1.2
1.0.0.2
Cloudflare Family
1.1.1.3
1.0.0.3
AdGuard Default
94.140.14.14
94.140.15.15
AdGuard Family
94.140.14.15
94.140.15.16
OpenDNS FamilyShield
208.67.222.123
208.67.220.123
CleanBrowsing Security
185.228.168.9
185.228.169.9
CleanBrowsing Adult
185.228.168.10
185.228.169.11
CleanBrowsing Family
185.228.168.168
185.228.169.168
Control D Malware
76.76.2.1
76.76.10.1
Control D Ads
76.76.2.2
76.76.10.2
Control D Family
76.76.2.4
76.76.10.4
DNS4EU Protective
86.54.11.1
86.54.11.201
۳. DNSهای رمزگذاری‌شده (DoH و DoT)
Google
https://dns.google/dns-query
Cloudflare
https://cloudflare-dns.com/dns-query
Quad9
https://dns.quad9.net/dns-query
AdGuard
https://dns.adguard-dns.com/dns-query
Control D
https://freedns.controld.com/p0
NextDNS
https://dns.nextdns.io
Mullvad
https://dns.mullvad.net/dns-query
DNS.SB
https://doh.dns.sb/dns-query
AliDNS
https://dns.alidns.com/dns-query
DNSPod
https://dns.pub/dns-query
OpenDNS
https://doh.opendns.com/dns-query</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1845" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1844">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">💬
کاربران WhiteVPN روی اندروید
اگر اخیراً داخل برنامه با مشکل اتصال یا اختلال مواجه شدید، لطفاً برای کمک به تست و بررسی مشکل این مراحل رو انجام بدید:
1. ابتدا گوشی رو یک‌بار
Restart
کنید.
2. وارد تنظیمات گوشی بشید و برای WhiteVPN گزینه
Force Stop / توقف اجباری
رو بزنید.
3. سپس
Clear Data / پاک کردن داده‌های برنامه
رو انجام بدید.
4. برنامه رو دوباره باز کنید و اتصال رو تست کنید.
در اکثر موارد بعد از انجام این مراحل مشکل برطرف میشه.
اگر بعد از انجام این مراحل همچنان مشکل داشتید، لطفاً نتیجه رو به ما گزارش بدید تا بتونیم دقیق‌تر بررسی کنیم.
ممنون که با تست و گزارش‌هاتون به بهتر شدن WhiteVPN کمک می‌کنید
🤍</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1844" target="_blank">📅 09:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1843">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ww8Ms4LMbTqXjCYgUJSew3CxlHwn1aNiWvHouwoR0obYWG6aqQJqLu5UOjubMDlSr_bTWvvmcSrCSkW_MDX6HX6lRJo-73d4Cj2mtoo7lhrXHYsYWKm3p7YIijPSVWJapbbeyX5UeAml8v5PCPtid-rWlCY10W6C6bA-Qgt-_hhy6RxeE-Ho6Xz2eMkgU2gwisa2ActBWU4t9W7zraK16qeMbcDfpPrMm5Ux8talepeitQhyAYJ2esgV0XmpT3GDUE8oOYdVSwfpGwaTZk8AdGigs5Q5M_hPnaS3czkYtj8sBfsYO81aPO8NHvq7k18x4PWraR_uGYy5HJzFTS22Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ازمایشی whitevpn desktop1.0.23 pre-release
🧪
این نسخه آزمایشی است، نه انتشار رسمی. برنامه خودش آن را پیشنهاد نمی‌دهد. اگر نسخه پایدار می‌خواهید، روی ۱.۰.۲۲ بمانید.
چه چیزی تازه است:
- فایل نصبی
.msi
برای ویندوز — نصب در Program Files، میانبر منوی Start، و حذف از تنظیمات ویندوز. نسخه zip هم هست.
📦
- گزینه «همه سرورها» — اگر چند سابسکریپشن دارید، از میان سرورهای همه آن‌ها انتخاب می‌کند.
🌐
- پروکسی سیستم و حالت تونل حالا در منوی آیکون کنار ساعت هستند.
⏰
بیشتر از همه به تست فایل نصبی نیاز داریم، چون اولین بار است ساخته می‌شود. اگر ۱.۰.۲۲ را دارید، این را رویش نصب کنید و ببینید درست جایگزین می‌شود.
اگر مشکلی دیدید گزارش بدهید — اگر بتوانید محتوای صفحه Logs را هم بفرستید کمک بزرگی است.
📝
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.23-rc1
@whitedns</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1843" target="_blank">📅 06:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1839">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-poll">
<h4>📊 خیلی از دوستان میگن الان یکی دو روزه اختلال شدید دارند و برنامه های white براشون کار نمیکنه . شما چطور؟</h4>
<ul>
<li>✓ هیچی کار نمیکنه</li>
<li>✓ همه کار میکنند</li>
<li>✓ فقط whitevpn کار میکنه</li>
<li>✓ فقط whiteaesther کار میکنه</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1839" target="_blank">📅 15:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1838">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LSL7hIj55bTk-M_99YQAT5WcA30ZIgXIIbsh8Wmuif9fGWFi50xdXABfqapVdhY-pWmKXvfCwO4XG63NmFHlafPf0xez7zk-LrIxu5i0NkuUFLPT15-ueyhjamdhUxNPjel7i59iMg0qinHT_QnX59GhmyuZAKzBF3AMtLBJsOp_C7T7stvz8hZxMK27oz-EePvdCVrUZSKqyQlvxQBx3QUXQYk6TpfevA1WJLPilXg4T2qKmDjZKhoT07QiohS536qpZH0rGxsdKteI2k7xqf4_s0s-heJ3sBbUlZUMq_Yu0JOUS7FrKHpSOewo0Vx2Tynk_iB7d-yklEvg2WslwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther mobile V1.9.4
pre-release
الان DNS inside the tunnel روی همه حالت ها اعمال میشود - قبلا این امکان فقط برای حالت proxy بود.
🌐
چی درست شد
▫️
فیلد «DNS inside the tunnel» بالاخره کار می‌کند.
✅
تا حالا هر چی وارد می‌کردید نادیده گرفته می‌شد و همیشه از
1.1.1.1
استفاده می‌شد. اگه با سایت‌های تست DNS چک کرده بودید و جواب عوض نمی‌شد، دلیلش همین بود.
اگه خالی بگذارید مثل قبل
1.1.1.1
می‌ماند. در حالت chain اعمال نمی‌شود، چون آنجا نام‌ها رمزگذاری‌شده و از سمت خروجی پرسیده می‌شوند.
🔒
و بهینه سازی موتور و routing , ......................
نصب:
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.4
@whitedns</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1838" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1837">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CYLumHsVjY2ItldNt7EGBqTdWFMkLwZ8z-LqDBuAp9GL6d975B6lRI9TGxqYZKynR2VhAyfANE-Jd4Fxw996-YQ_4XXumUtxBmwJEfhcmktUSTVQCLBNVZ0TMPkUzH0afd6xAQ7ggU2GJEH55Y_v0REQsavmMmcgv_I8F0vVpBPBvunN64muWS85ft8EUkCIY8qUzQHdDTUkfjgrFR42LanPrsFM5h2L2YdeglNoC1rFn9o5sKMHhP3M1iEkWXuB5p8NYYLucMlNSV9sJjvCHi-eg4biNeT8QZiNY5eT1VXgmpsYCGGfTDe6JR8qHClS-d7B3QOoMs7AQSZGRDroMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخهٔ آزمایشی whiteaesther desktop 1.9.5  — رفع باگ پورت و یک سری بهینه‌سازی روی موتور و .........
🚀
اگر بعد از هر بار اتصال، پورت پراکسی محلی عوض می‌شد و تنظیماتتان به هم می‌ریخت، این نسخه همان را درست می‌کند.
✅
پورت دوباره ۱۸۱۹ می‌ماند — هر کریری که وصل شود.
🔒
این باگ از نسخهٔ ۱.۹.۲ به بعد دیده می‌شد، از وقتی دکمهٔ اتصال شروع کرد خودش راه خروج را پیدا کند و سایفون یا تور بیشتر برنده می‌شدند.
🕵️‍♂️
📥
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.5
⚠️
نسخهٔ آزمایشی است — در فهرست دانلودها به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد. با همین لینک بگیریدش.
اگر پورت باز هم جابه‌جا شد، حتماً بگویید.
📢
@whitedns</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1837" target="_blank">📅 14:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1836">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه WhiteGame یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1836" target="_blank">📅 09:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1835">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVpHD5TXlgaY7o-zXVy70h9tkdqHYNV5fsHAxvwi2QXkcu6rUXpn867KzwhUpOcH0mTAjsQqzcZogiuzPI7EcNPCy0H2B6X1HVv53PmXNRIQoSPSFSVllFHRD5oc7G10636aCUXkwDtplGVgAUwupfe1I_TcRx1edSNgEoXu_BfXhizNZe0e8sDKwcSxaYGJg69r0DjB-wD1P_K9MeAlyeNEm__0XksRe7dImo-pACWDOcb0O7ruPpavis4kQVccDXQBA0-ajF5g22SjzsdJX3o_RmAOsR8hcyoZCdLHejK-SRcAtF4KGmr9yrafnh3E54jZCQWLzLUUbz5AoBXEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه
WhiteGame
یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور ویژه برای بهینه‌سازی پینگ، سنجش کیفیت اتصال (QoS) و رفع چالش‌ها و محدودیت‌های ارتباط با سرورهای بازی طراحی شده است.
📊
این ابزار با شبیه‌سازی پروپ‌های شبکه‌ای و سنجش شاخص‌های کلیدی و نوسانات پکت‌ها تحت وب، به گیمرها این امکان را می‌دهد که وضعیت زیرساخت اتصال خود را پیش از ورود به بازی ارزیابی کنند. جای دارد گفته شود که تمرکز ما روی
UDP
است، همچنین قابلیت
Test Real Path
در اپلیکیشن، پینگ واقعی و دقیق شما را در زمان Matchmaking و InGame نمایش می‌دهد .
🔐
پروتکل‌های پشتیبانی‌شده:
Warp | WireGuard | Amnezia | Xray
✨
ویژگی‌های برجسته:
• Packet Loss Injector
• Jitter Plus
• Gaming DNS Spy
• Optimizer Warp و WireGuard
⚙️
علاوه بر این، ابزارهایی برای ساخت و مدیریت کانفیگ در اختیار شماست؛ با استفاده از بخش Generation برنامه، تنها کافی است Public Key سرور خود را قرار دهید تا خروجی موردنظر به‌صورت خودکار تولید شود .
📉
همچنین در مرحله تست آزمایشی (Beta)، حدود ۳۰۰ نفر از کاربران با استفاده از ترکیب Warp و پنل BpB توانستند میزان Packet Loss خود را در شرایط ناپایدار کنونی به نزدیک ۰٪ برسانند.
🤝
امیدواریم با بازخوردها و پیشنهادات شما، این پروژه را روزبه‌روز بهبود ببخشیم.
https://github.com/TaJirax/WhiteGame
@Whitedns</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/whitedns/1835" target="_blank">📅 06:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1834">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jj_aOUUAckTBztmc2dptxrp5w3-4vtDCllcX-5HHW31z63I7cTL7B60Gy5NswGuBPwuvyCpRTbsjdUfpcPrVcTO3PMQThB5ab7NG1ERao3aTBRGv2GnefrrZQzF3kdHF75Ql7K8HT4BwtmardSUSCGfXHDyn4P6A18dHnDRbUAyNH5CENeKt7WJG6vylWXtybGHQ79IrRCBXl1C6IftQ-tlvPN-4K4D9Idzj5y3OWbB1urhB-pdWsaapjneMTZKP6p9Y7OjwrA67N2PvhklD5V52oTKT0zEB1ar7iOT3ASrYhxC-w6WjKau2C9UIayrWA_oyNVR2KOmVuT_aNWmodQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا در گروه whitedns عضو بشید
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1834" target="_blank">📅 20:16 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
