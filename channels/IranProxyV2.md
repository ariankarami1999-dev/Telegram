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
<p>@IranProxyV2 • 👥 39.6K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 11:07:02</div>
<hr>

<div class="tg-post" id="msg-8485">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0rgwf-gQ_9lqDGbZ1ybmV8gQc7o8O4966Xz1AjaHBh21bLyNL8VoRpNBQ3Aizp24SgmGaytD-4J7NrBGDQgVzNlXPyd5MYP8vIhwrG-1oIxL1ycbB2JsHZQwJXkMkfxz2MrMPq3xTfRGtNy0BfHYXsnixpnTS6ACbs400urEONuCQtJHvSeZksK65ldcbFQURPLdSPlf_SnqGu-azSADTFmY6Def8N5sXnfxBdnsKZArxWsxrWX3l6i6hlYD-hb444SqKJ5N0AY-wvafZf1pWXoTtOXd0xp5hRDqtJqQ3DvXqS0uGS_EBRDB4c47-xAcjG_7ad6bts2-qMeysDfVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8485" target="_blank">📅 10:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8484">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
trojan://humanity@193.151.132.136:40443?path=%2Fassignment&security=tls&insecure=1&host=www.ignitelimit.com&type=ws&allowInsecure=1&sni=www.ignitelimit.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8484" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8483" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8482">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مذاکرات طوری داره پیش میره که احتمال اینکه ایران اورانیوم غنی شده آمریکا رو بگیره بیشتره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8482" target="_blank">📅 10:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8480">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiXXtYZyaEhuTkVqlb63T9RMIcSW4H3YjRLZhuVUBb6bKPMb_WTjcRBjFKYwpz4cm-ZhWvazBxhAK-yX82eVaKDkys-hsbxIe5numAB-TBX7tdp4jiYbxmnX5-8lLkfEOznJ51YocvZOpkZve0hSi9EtESrkDpI8D-hJoauileyM7jgXNO1wzCU_c336g3ML3ROz59RX2knG6zHknnKfgyqkuCpYc6Rdx2fsGN70D7Jj42CQlmDpMNllAJ3hPcim4J00zlUX2N_Lqr4vKZdroex7SiU5h3vnO4EThcXDhsXzObhyXXNKzjcEhIeVuFy0-bJQNnLSwMOXmfVcdvog8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc_E9uCalqK7lYdTWpquvM9NnYoTxal32pU7ycG7szRyZPQ1_280ppq5ngESoJBTCDL2kVvEx5zVOAfmvKzDG7VCiXoaYFo4nGwZtAaP-dsTdJomi_xias78rH8FSDSCxGsiAbnaqajCBWIUMDDYL6ZkhmfLa91NEslJgnc2yrjj99wdSBfyxfS5yNQ_oAH12rtPja02F9YgTlZvEYQkxksNOPKmt3wxdbLL2IofMXoZpDV1G_n4JLrV1QKIyC-gfRdxV0uPdIZTBGIlOAZJezCfA8MM-Uj8DUy4cri70i05-dSGZymbVPAJz0S1qNHOtISfVipdpC6l-bBJKIRmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ولی من که فکر میکنم، همه اینا برای کنترل قیمت نفت و باز شدن تنگه هرمزه، که ترامپ بعد از جام جهانی تا اون موقع بتونه باز حمله کنه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8478" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تنها چیزی که تو این جنگ نصیب ما شد چی بود ؟
قطعی اینترنت
نابودی میلیون ها کسب و کار
افزایش شدید تمامی کالا و اجناس
فروپاشی روانی ملت
اتلاف وقت با ارزش و هدر رفتن زندگی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8476">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teAoLK6kRmg43FvnSkSILSUOarcPtzXEUr3wb7u7bxkGlaZ9lGv4qkoxieRedlkTlvBhgkgalyU33ChYaXDOLN7CIovMQFbzPIQae1eCttKUjXlYRhYvha7s4yo4zrmjYdeCpgObeGBPFn1Qi-E6a6tI5ebg17InBTAdntapjpIOSB7gOhrYN2pjt9tGw7KCNLq89yuizfIvrL_K2ZCsfetqjWtlQ5ZuVSCOWqn50q5Obo0ZsjHSBaZ2gvxArdt8LcmBpzHyCwOQKY1w1EeQYzpXjQLx529oAMImdpoW6UiZrFBMgxByFQxZArolJTFpXkTZ6OBGie8X0ynAm1Kimg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCbckK6TTtgJfAiNB8cTAagOrCgOG1Dj6aZBc96z-aJHkW_oozS7UvC_YOxsUYxP334t4YXOd0F4YuoloQttLu2XUwqfAR-BzbmIg03REke9869hUFk3P1HgcksP9Bmieohsl-pTh06SBjwAwppTTW31TRJ9K3jAG01BMqgYUaptq7YWuDfoIJQrnGKE7R700rfam-Wmia3TifsNxJkf5NsgP1JG-hCdKedUSXPAmo-QNw5P8-enjoZttiHZTgXTKxDQGCh7anvfWrMgHekrClBWfbtNbW_xgjn-GhQlrZbXV7wVKB3drwjYwJioA300NOCBWMJCyClIB7-mhRrGnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8473">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoYGIlYTT7qDC3bKcE-fyoSymRWqfog43GrlKjYtFwNDaw9tY9qhkmhSZwx9Nvq1qUqkIBjQdl5WL_dYFs_4Qt_4kY2KzSEf-cm4Rvx1E_1hpJtFFgYkd67UvsgPSKVJ_eMPCPxH3fKEH7ybZw3pNsW4MqncqtHzJLTwkLG0bmi0wo7TOTPkamwwkUVkuKXi1mcqi_QFVk4WaE_iIL314z5TaBXTy-3qZClWgprqCqbYZBhRLBxTXftn2UAEDg3WOVCLW0ZudvVG3GDjlHtiyqnMbtC_t3Kvt-yGrui1jQvN2AmJL-KdrNarSssZbdEq3Z8igQz9gDwsZxS97Ir4_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8472">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQvPMwL0u_dM0W4VJgDkeiHgCXAGbwwmZfC7iVa-55D_eUpE9OCxBHamX5APZwqAbdIyWAq1HYOr0W60FkgVWhyypBzj-mF9PXoUB64EBbxXzxb4tgnnKTou176xkmAmmSRCOoGNWhnGPLoIPEHuh2M3tZ2XjcWyGD4On448SqEXDVdrxwLmijGNc9n0l0urUb3cH4sZVF0epDmhl2YpHRu67Ms4NrarL66V0RWq00P5RE9-4r2MzGW03dBK15ufSqYxyiJ44G9ucthpMtRsT74sdsEjy5yX2PKpmr0nJVTr-p1UXrvWZ8Uujp8ugV2PslCGkHiwoN5_oApR4hdpAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLlafg79FWLZ0VkRilKKZxKUZVCzzY_AZhhO2Qi5DYZ3DM3ssxGUcNEMeWXttK_Y-RtjlG4g2ll9oOuuVBaMS29-kEs9wki0TWhX5wzxFLZbmk91ABT1iO8nIWMX6677KvfoD4wU3kWv2eg_o-Mxf21nMviAVnSP-kH7D3U3_XC0eeH1-QifP3jFasIuoVVFco0tFHJYBXNadisvzIMZ4rHMN2EYt986ovUMLmW4eIlk6_gF_J1O0gmhQCCwqxwrzPAaz6TgPrRnF7T3z6Cw5Qs1hJQ41-bdtY_15vuUAZl71-IGFgZ8WqELrWk0X1rVkZ_uQJAzskEKthGVcDOEfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFeGq_Ep4MUVnMiVSsFj1yMZwFxZvqxOBApsd8kGrWUY5ofqJvFz6QHtocj2mUJgO0ToU4EHYXUcoq4Q2o8BtvQp1U24BELfeHrWSQcLKsB3vbYHHOEDyeUo5lW_SnI1xpZ4OgNYWsSmRXFAFl8CRfLgjiazGrcFBEM4SMpTFKaSR9NEyVNUPy_K6a7E8-t6vKBbf1wDOrxEnpwYohptXCtpXgzlPmy6p5dAHudriAMIr-tpTndcOzb0zIggX-FJJTFKaMQf4Qtz6ae0YevLw24tCDVVTmgXlLmxmtFofpy3IqN1Ck48KY8GYc5HFwJ6YZyt_2HS9nArqT4xdeC5Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B__n_7DYp56At2IycRPbuQJKrXJMuwpJqHdEpi6D1ZEBYV8RzzKpW_wJ22VBYxM_SaJvDSHXCgUJIuruL1qrMveYuF2SeQEVESTXj6ID3Hkg9l9X3_kpFhFpKJiNVV3XLKl6IMKZefx-It4J96E8VwJp8ZcBq5uY_AKMncguMt-gtvloVdDaocoWBnMIbFbUbERIkaa2bEgePL4FdfSdp9mZI6L-tIWY3vXss5M4Emn-zz4zvTyrr4m-LehGx6cH5mXhzcpWXp22imIiUzZytADeNJII37kIwXsJGTu33waDTKNdn4kZIrV3ohXHTMEfav2cH2PnD0Yfjb-JVKS9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2FDjA2maVostBj2rKYVEvljc32S564J6bHqNtafBlF40uVF8BDbKSdZFwsNSoIHc6br5KZNMMjG39eZZ2UI0Rm3pcJ4oP-GVsph4QQa-uRY75pqHYj-QbdCxyp79RV9uEQaRegTtHzOjncaa5g3EjQSvYJm7Gl76ViWGEyAsivhZs-wlQJcs25B5CS21QGRSNzUzhvGjZIizZnKAzxDb7SYiSRmuzJvQrEO12K39Z6aB-eYdUIzJHmpPCz2zrrkF7WrjK_N9ZxO6Xgjfz9GcP9Icr4YkTt89EQrX-MDYEEJ0tWy4o3cDx5LckCBlo_KOZYs-twQe_RHYdKh-QJScQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHgu_y5BbK4EIiBoAJBAF-73MNvIfSRzyAVYx9atZSF5joLucw59O-55qRN7i7WhDE3TFZbbzzO6IWroEbzI5arhHRDZNrRw9NJlhK32ok0liy4A_tulLB4vafmC0hnNd7RPVaFAwqOohYSo2ZSL6nr994OFX7ZNgd-suRFKcUFTKNXdk5XYsTR7XtaYyPpmTlAtisuy-0vKAFC-fIBIzI6aTim0QVzvX4J2nq2vQf1Ag1F88bNiaL6KIjjBL9WQCSux5C8K0Clg3zpAzvUS2_8oK9DSOM2wi2NW3uYOOKq6PFFYZSAJs_5knVBy-SmIFCIaMCuA6sxz1jllRoQmgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le1dQ2MNR3MszGhM6lqrgJ0v8FYYC_Wo2tPirqmDAHBzsRvjUJC7yxgvGEULXqYzhdsTPspngugOX82ovHkYV3QUqAYpimb0_QyeXRM5xLF973QT-z-2fFtTfCYrtl3QPDDQmmyXx-vkI5QTVLhcM2m85DyKJX0-KeIim_ImJz4tkbZPB5OmvSu2M8GajznC5X3jAdbEzr-0z8kDWOka7nPrbvMDh_mJ0FGgCpaW50JA06BILLNp_wUnjaiodS6JnriGE5nf7Mf_YDd5113SCEMLvkM9LT27NcTm1yE3RiDVeRpL6ySGHkwcNXd7zLNxhi-SA8Qdj4Qra_vdJPwjmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=bFki-wrvFsU9v_FG8M8XOE6Lj8GhfXknrxEmUQQDRYOWMi-ZfXbEJc0CyiIkzA6iS87VfZSFZmq-ccvE7dKigkZm_7lh1dRkbA6SH0KhO1aRUaV1-HRMw5adqLFsFb6X44ETqr9_a8zyCsp283mtO9_cKjY2pf1QVbJ9zG_EBNxxBHPGtTZ9qS3ucR_mQxvdS0sZ576pC8bvBIZyJAe7y0rWqXAZ18b3owVV1W-Lo_uHsusm2Srd7Sa33f4nPuKfCJwLdlKneDWAt5pCDKWc8A53be7lP1ruHPjGDva2n96zSqDTI9M5J6KLyfOluHrXZLCp_dBTp5DDyxvSOJNUvJeDAnPVbMxdmmhV7JQhYqPH8KuFBh2R9ucZCibGHT2zt6vmp3Opy8G920Zlz8ZA-LSKyNyoCAZNx8M9xO3Eelen6htYUKkkRmm9vGBVh0OqCd-oRwmSVL1kTrlre1UeAxkOj9l5YDcafJ3tFLMpBL9LQYjrwTSxsafcOwYwNtoASLB1z9XofihxPpMsVZihrvgMGyBc42c9QPpdoFiFe7pUVsYSZ8sZnpA0U0w6gxlK-bZLIQFLDqlkdGGOyxq5cSjoCjP6kfg3BHe9GvGmkWAZGaFjRw0RBNJ2a1G0Artfs0i3ju2rWItEFdRYSMEiqIc5p1rBTGMPxaDS_JwZIOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=bFki-wrvFsU9v_FG8M8XOE6Lj8GhfXknrxEmUQQDRYOWMi-ZfXbEJc0CyiIkzA6iS87VfZSFZmq-ccvE7dKigkZm_7lh1dRkbA6SH0KhO1aRUaV1-HRMw5adqLFsFb6X44ETqr9_a8zyCsp283mtO9_cKjY2pf1QVbJ9zG_EBNxxBHPGtTZ9qS3ucR_mQxvdS0sZ576pC8bvBIZyJAe7y0rWqXAZ18b3owVV1W-Lo_uHsusm2Srd7Sa33f4nPuKfCJwLdlKneDWAt5pCDKWc8A53be7lP1ruHPjGDva2n96zSqDTI9M5J6KLyfOluHrXZLCp_dBTp5DDyxvSOJNUvJeDAnPVbMxdmmhV7JQhYqPH8KuFBh2R9ucZCibGHT2zt6vmp3Opy8G920Zlz8ZA-LSKyNyoCAZNx8M9xO3Eelen6htYUKkkRmm9vGBVh0OqCd-oRwmSVL1kTrlre1UeAxkOj9l5YDcafJ3tFLMpBL9LQYjrwTSxsafcOwYwNtoASLB1z9XofihxPpMsVZihrvgMGyBc42c9QPpdoFiFe7pUVsYSZ8sZnpA0U0w6gxlK-bZLIQFLDqlkdGGOyxq5cSjoCjP6kfg3BHe9GvGmkWAZGaFjRw0RBNJ2a1G0Artfs0i3ju2rWItEFdRYSMEiqIc5p1rBTGMPxaDS_JwZIOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucurzUY5BnadQiNwnL1INaZ7u3SfG2AZzN1FhKDn5mkTv-tJPGv69zUfzWjvjefqTjMxTdccVEwlpGHjlWloBzfa3rleDaKBBb1B6HHW1UJHELRSLJA17r0vw6w0uPZviRfGCPizPAit0ueFOp-33RsKz2yJNP7CeX1UwVzIw5GSTA9bminYTB6SQPgyqeuwHgjlCFVaCJL3pewjRJa4U-C_exipI9gKJQCnfw3oxQ6d0HkzZYosouiMwKIijZHpUYKcZAbgpAs-APGZZfjL8-dJk4PwNNzS0VPWYZ3LNN-VuGsAXs_1JmJBWbs9uWNU-KStjhR9xLLF2h9KYt_qsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMMiXPyEUluNV3CHXpPYxrT27ql7-exvqg2KHZYoRSuMU_gdc2DvUi-XRz6s-1qDEDKmAEZnoRQqWxBUXdqzYg1JYvym5Fw1NY2rtjOGEMssLK_2OYHZWqAnYhR47JL7N_d6dQA77g8NsKi245zLR9U27I3PEOfu_Fj81E9RS3Tp6ofKix1gvLPD7-uF1iuJ8NW_Sn1G8xTEEMVXax-xXV7kaPEzUYTZfv4GM_yQ29Xjx4r8QTRAtAeMu5wj-IE1CJL-yGpcotyooIyxqrd_gtriTlVxIUrlwku0Nyj5zAqIq3YxVf6jbYcHTJSJKZ8eevdxqHmziGkZfG35O8xK9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piIEIS5T37lKxTq6ZjSa68IZ80Jd4KdLjzyUnUGocEUanPE5LyGvUJQVJboajZCj9jBI_R7lawpU5GGUfA9bwTojHkhoUER-fi7U76S8hmp819EzDIpIHRYxt_VEtn_8OSw2iFT0lhb0rcaAEVP_tI-pulzwpvexeT_A9FFMJHx9uKql0kc7hZYn2Hv9T4L0mAQt9OIGjX_daXlCeyK4iQ9tiQLLx2ExmTdvXP14swSaLK31Nw6bWxMA9dIOtdo0h-IWovSSfyxBvU5YCN7a3hCghq3kUJQCWOKxlFx3Mczdu7uGm-B3tNSzV-U0TRt6gm_vOOr6PrTbFxCLdeR44g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=EqcgFSsv5L-ZbVQ7wF7y6JplvHrieX_R25rUdyFAOrRIr3NX2WO2jqYumVAvK3pixs8ofCjkqTm-iyUPzHyfmZwCrGLyICEY8lFj9JP3F1w1KZE6Cf-Gaf8MsdP7BXvuhfzkQ7pMyCsuDvrO3FmM7rLq6ChSQrOMLHT7--BFOqq5dV3NjxrwXAgYZzHdvnokf4eXwVpE1xEAusKWdYTqnMcZLyS-FXZk2tHehDPgSiqlxpCEejE3e2UejN84yBWQAdT9URoNymTt5KwB4xj5K-OBZPetbPTAK31VcL9FbPZ4GReozVxZaFwZ18y3fRia9UaHfo-ln2hFhJjJcsMmrLD0tnxf9I1LmMK8LHk4_CUMGUGP6k7enrSUkMhcpGf1WYyiLys3mcnIZYJ6RGcpAQdVlw5VVriDwyixAyXhgfqDgNUgrpMZozQV_CO1Zo_AX6HTnPqyqs1KKKD-bSpK04rmrGLlU8DH68cxKKUqG7-ACDFMD5nPbFmnSkbdYSQe9gPZLkJCqcrNbA4ILncPeUVRhX68SE16MIasgUTeX90MOuZpoRT9-H7VIaZ1gRP77Cnr-0A8Kj59zGsdHfeSCCEN0c19WsFmri6Lnh7wXOwVFXTlmTnTVkfhdpwk5AoOsOsKLMAugwR5bUEIguyKWA3c_XxVZ4T24osdLScrxRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=EqcgFSsv5L-ZbVQ7wF7y6JplvHrieX_R25rUdyFAOrRIr3NX2WO2jqYumVAvK3pixs8ofCjkqTm-iyUPzHyfmZwCrGLyICEY8lFj9JP3F1w1KZE6Cf-Gaf8MsdP7BXvuhfzkQ7pMyCsuDvrO3FmM7rLq6ChSQrOMLHT7--BFOqq5dV3NjxrwXAgYZzHdvnokf4eXwVpE1xEAusKWdYTqnMcZLyS-FXZk2tHehDPgSiqlxpCEejE3e2UejN84yBWQAdT9URoNymTt5KwB4xj5K-OBZPetbPTAK31VcL9FbPZ4GReozVxZaFwZ18y3fRia9UaHfo-ln2hFhJjJcsMmrLD0tnxf9I1LmMK8LHk4_CUMGUGP6k7enrSUkMhcpGf1WYyiLys3mcnIZYJ6RGcpAQdVlw5VVriDwyixAyXhgfqDgNUgrpMZozQV_CO1Zo_AX6HTnPqyqs1KKKD-bSpK04rmrGLlU8DH68cxKKUqG7-ACDFMD5nPbFmnSkbdYSQe9gPZLkJCqcrNbA4ILncPeUVRhX68SE16MIasgUTeX90MOuZpoRT9-H7VIaZ1gRP77Cnr-0A8Kj59zGsdHfeSCCEN0c19WsFmri6Lnh7wXOwVFXTlmTnTVkfhdpwk5AoOsOsKLMAugwR5bUEIguyKWA3c_XxVZ4T24osdLScrxRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=TLNmELI080nX8wxI-xle5-nb_GgwxWcubDyHkvJQWqlaAsmhJsGuab18lGm4pVH-Jkt-Beibb8zxnetWa_qj--Aj-9bCQs4IpDijiKGH7JP5yNdRqnlXopcU-yiwONw1WiMDwVqSmIuldMkWy9Z2YdxfIzF0F3G4cB4rGvFw5l-ZnS0KX93jctyrz_mFjE-TWQUztrqIyAdoCkKoLD1OlReVri7NC4JyHLrFGOuocx1RsVFk-szDVFeClMSEFDeA-xjBEQvO-EGBJIylZh35P1To3D70UTmuaFHkzlz6St51wwgQT3XGSdTMKqPcEqQvvC9bv1idSEXI5sJXtMi4PRQ0on3VuyIDkBoiixxM96RTnMor4nWZHgVhEsykib2oI62jv4GsxwvsMF16rz9ew1X6GzGovOe-a47IvXnLRinoiBenqTJLdbB_5p9HbvkR6QRqSLR4F5-69q0CZb2d0HDRKW8Kz-2vbTucK1MODjxzIQoQ5PlyL0eLmyE39ivqTgczajCccZMM4v_b5np2ASy29D4fsv23hyxEZ2wX2cquPy4UEPkeuYo06RyqluifTYkoNPpzeeKmdrhJ8SK6czciaCq023JaoKKdAcgFBGu5EVPsgPDhxcmbHrHA7_gBbTtmsZgpvFwQZ6130Ya48wJewZkME6JWDq0mkJfuP7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=TLNmELI080nX8wxI-xle5-nb_GgwxWcubDyHkvJQWqlaAsmhJsGuab18lGm4pVH-Jkt-Beibb8zxnetWa_qj--Aj-9bCQs4IpDijiKGH7JP5yNdRqnlXopcU-yiwONw1WiMDwVqSmIuldMkWy9Z2YdxfIzF0F3G4cB4rGvFw5l-ZnS0KX93jctyrz_mFjE-TWQUztrqIyAdoCkKoLD1OlReVri7NC4JyHLrFGOuocx1RsVFk-szDVFeClMSEFDeA-xjBEQvO-EGBJIylZh35P1To3D70UTmuaFHkzlz6St51wwgQT3XGSdTMKqPcEqQvvC9bv1idSEXI5sJXtMi4PRQ0on3VuyIDkBoiixxM96RTnMor4nWZHgVhEsykib2oI62jv4GsxwvsMF16rz9ew1X6GzGovOe-a47IvXnLRinoiBenqTJLdbB_5p9HbvkR6QRqSLR4F5-69q0CZb2d0HDRKW8Kz-2vbTucK1MODjxzIQoQ5PlyL0eLmyE39ivqTgczajCccZMM4v_b5np2ASy29D4fsv23hyxEZ2wX2cquPy4UEPkeuYo06RyqluifTYkoNPpzeeKmdrhJ8SK6czciaCq023JaoKKdAcgFBGu5EVPsgPDhxcmbHrHA7_gBbTtmsZgpvFwQZ6130Ya48wJewZkME6JWDq0mkJfuP7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQWJ1etmqs56p_WM4PsTvW2JwgnIDP2XLEKn80EnkaFPDqkGO20yB0JF1gUVIuSJzlSg6t5MD9cIbdRP5RGYY3wzsQJzgw1iqjM6ino288dcCuef6kTf2Ijxiomyuzf5Y7q3JPRNEOk4zL5LT6_YIzXwCaPz2Ow7FKecsxWECkVjfbZvMadDq5dsc_s8Sg3gO66Qp4-C8EqGmOPiPg9TOzdVP4eliMD4fl-Jt-b_GnyGVycApur1h38_NqlEkMP_xtdTasLBAGDPO5w3DMq8nuFriV0sdrtiEkQy7rMX-hppVECQ8YbeoMQ6Z_8biYW33wJ7yxX8Q0M5vG68CsnxeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=UpsdqCTlYs7nembCdmaVGhCMDbDSXhyOgG25Y2ls2ILgeZTm2KOE7H543P3sxLD6kZg6SaZpMaoRlKfnib8JMRYMJTBoDHu85Qwde5dubkJafldeXJStTkle3VUTwOf0TwwhHft3JStoj-xOYxgAMNlBIrAG295rj31m06avn3RenAmG82c1iuwuR-ZeZsfAO3Hct-kElJPHupBfbPlkzvpYDtdmDK9NA9MldSsEACG8VK7ojPFO00myFdSwwyn56MHmzdiu73Ue0bor3kVxuOUCHFAQ-ioo3ghgvbrI3KVo7o7lO9VyS9SyJkp4lRvA25PX-iBFQLTEaZDQ2DKokWTwSR8JgOXnjvG1PughjvNBw2KTA8RYketYggC1-qJ0lKaMxh_CreIMMmsYOw8BceGU_rB2Vk_zQ587A_rxB4MIjzNwJ-lvJyeqAZLGGwooLj3IC0psRkpzkzvoQoe8ARqK3nioWip0u4BuDhPkW3i3K0wztPxBlM-CHTsg2hkBJA21vjKw1o1Q1F994A_lpm__7yTV2UebA40odwVPYDmVmQqJ6YUZUSG49z6ef3IeyoDyTiv2suVSgDmkVHHspDvAGppf1RvelK6mWpNX9MUulkZXud-0Nc9Qas8mtuVvkiEDHIx85VpwqNNyG0bZMADdWIMDXm8PkNydLytYZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=UpsdqCTlYs7nembCdmaVGhCMDbDSXhyOgG25Y2ls2ILgeZTm2KOE7H543P3sxLD6kZg6SaZpMaoRlKfnib8JMRYMJTBoDHu85Qwde5dubkJafldeXJStTkle3VUTwOf0TwwhHft3JStoj-xOYxgAMNlBIrAG295rj31m06avn3RenAmG82c1iuwuR-ZeZsfAO3Hct-kElJPHupBfbPlkzvpYDtdmDK9NA9MldSsEACG8VK7ojPFO00myFdSwwyn56MHmzdiu73Ue0bor3kVxuOUCHFAQ-ioo3ghgvbrI3KVo7o7lO9VyS9SyJkp4lRvA25PX-iBFQLTEaZDQ2DKokWTwSR8JgOXnjvG1PughjvNBw2KTA8RYketYggC1-qJ0lKaMxh_CreIMMmsYOw8BceGU_rB2Vk_zQ587A_rxB4MIjzNwJ-lvJyeqAZLGGwooLj3IC0psRkpzkzvoQoe8ARqK3nioWip0u4BuDhPkW3i3K0wztPxBlM-CHTsg2hkBJA21vjKw1o1Q1F994A_lpm__7yTV2UebA40odwVPYDmVmQqJ6YUZUSG49z6ef3IeyoDyTiv2suVSgDmkVHHspDvAGppf1RvelK6mWpNX9MUulkZXud-0Nc9Qas8mtuVvkiEDHIx85VpwqNNyG0bZMADdWIMDXm8PkNydLytYZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feJngCBhVP1LihRNQlSN18lS8_iNY_7FGfTOpMNZi1avwDdeJHzTWGz53jXuyw3FzZekvH-kxt1UmkYqm9bh9jPntpeG_P1BLIY-zhs09Gr2Mh8ifDUTOBlo5OdS0oe78ml2WF-1EG_El_BNF4oAowhdU0FAJRuib6uCN6qbMS6mEk3akVh92nVRCzoKYSYzHXmxgcA8kDITi6uMYUBnmCRRSgQyjjLwI5wG0AyaUhDkgpNfCeHDz0txeSN37yz1Jt1w6DdQ_i8e10jvIA74BOD68i_zZYA-XqCNHlwAnM-Km9jeLjVXLwFLHUA0-yQl2vszt4vyGDyzIYWV3ppj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIDtingMBgVyrRNpgEvUeN7MQXFdt4vZSXXIEgMEI5LAh9DGKLLBqpy84_ykpjPG9OyWGf3FJ-hThWI_heKwZK6NRXoJfnxwf2i5gde6TuPX_SL9NZ_GSsPSItiD04-BjTPBXq7naTFxSji4DpoAZqUG_6I1HW56_qjH3-bTeLKBaggM6fn7sllnkSygBEI48lNCJNcO74Dm-i9mwyDbbDpZhqTauUREKUslpB9rteGPxe8yJKdVyp_zuru5OyYA7hsAzqJFHtiPOi53Uyr3B-dC2dbCRlfq-OY1YuxdZZFHvNpSr64N1rgySfKk0KbP4ausTWLSkM-LRTXJ6_kWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
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
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=Buw7tBi4T-gj_UIyzMADRyuXotSXJral_SUuO-7i_ZW4uD4fBTpEUaMaIk0nNYomBAUhBnrvv03_wgSubbj5D-sOEk0QA9HaCZpEaR-bFCGelhEaJWm6Q6gKMAmc_jZqWZ7oPkPgcEzvBnaLrQMOfTMdb4OWaIQTiQ4iLNCkm_I2I04Deksb9l0S8kNf_nb9gGCilSd-sH94IHH50jYOIo4nXe84CMi7CtTGw-pOf35LP9fv9jGciYlvnX1qIqMfMNur-J1LSwy5qglM34p7RYVwvnbrTq_8bQ3qEo3kq227VG2kdxTbzW2Go8YhhshUjHeug4p6teQC41rXyJBq8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=Buw7tBi4T-gj_UIyzMADRyuXotSXJral_SUuO-7i_ZW4uD4fBTpEUaMaIk0nNYomBAUhBnrvv03_wgSubbj5D-sOEk0QA9HaCZpEaR-bFCGelhEaJWm6Q6gKMAmc_jZqWZ7oPkPgcEzvBnaLrQMOfTMdb4OWaIQTiQ4iLNCkm_I2I04Deksb9l0S8kNf_nb9gGCilSd-sH94IHH50jYOIo4nXe84CMi7CtTGw-pOf35LP9fv9jGciYlvnX1qIqMfMNur-J1LSwy5qglM34p7RYVwvnbrTq_8bQ3qEo3kq227VG2kdxTbzW2Go8YhhshUjHeug4p6teQC41rXyJBq8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z09aLL6g_KJLkXNmt_t8qqg7lhle42_hURx65Liv1bVZYBVU65DUHEJuhmitrEvyYoc5UjEgTCiOrofu0ySdEFH--2BUZKRYzqJnnYgXRX_NPSKxUzm0wey3mMv8YLzVOgNcnaGhLP8EMxijmDxfhX3eW4dUN4-CIkAY48NPYgLUOUzpdJIQYmnb8zEscM4lMVmDDHYEF1d6urVf9YJPvGDzciMmsIOXpoHEsSty2Bd54KOZE32kl2a9QzWkSGcyyybKeLfJYKr78PL2L_S8hc3-ahcdpbpVcd1shy-YkJN3Ouy1PYmbjkBG1AzfE2n6RDsy3JtDu6_AWUfch5E2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
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
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qri-qb91V_hwXZG4Y4KCdxqkfxlZMn9F_YyIEeievgilqCsnlKP_K4yA5AXKvDafIQaekJchORj9MWPc9BKELMsGThCWwlGPPjlqJLcAWDoN2cjePEFfNC7rrZuBYEFaKeCycS6DpqjgRbgD_k1BeeSZNC-PUauHzNLM9q7Otrv5E1lPHxft-g_0Ya9PtKicwCiAHVBMJcGuXSofnb5kzQOUEsVvPeSknTajzkSQrFG7hfr3tzAgYuAmMbrSp_qR8VsSj_UtoHVnZAy1i8aK-lJLb-xuGRDdR9Nbo5SLlLl712qk8lU7Sb9EGsFn6uyKIDuQpGXbUljilLAyB4R5MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)  ‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)  ‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)  ‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)  ‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)  ‏
✅
…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)
‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)
‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)
‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)
‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)
‏
✅
✅
❌
❌
✅
✅
❌
❌
❌
✅
❌
✅
❌
✅
❌
❌
❌
✅
✅
✅
‏۶ )
🥷
𝐑𝐚𝐝𝐢𝐧.𝐳𝟐𝟎𝟎𝟕: ‏(۱۲۳
❣
)
‏
✅
❌
✅
❌
❌
⚪
✅
✅
❌
❌
❌
✅
✅
✅
✅
✅
❌
⚪
✅
⚪
‏۷ )
🥷
Matin: ‏(۱۱۸
❣
)
‏
⚪
❌
⚪
✅
⚪
✅
⚪
✅
❌
✅
✅
✅
✅
✅
✅
❌
✅
❌
❌
❌
‏۸ )
🥷
𝘿 𝙀 𝙑 𝙄 𝙇: ‏(۱۱۵
❣
)
‏
⚪
❌
❌
❌
❌
❌
❌
✅
❌
✅
✅
✅
✅
❌
✅
✅
✅
⚪
✅
❌
‏۹ )
🥷
Paranoid: ‏(۱۰۸
❣
)
‏
✅
✅
✅
⚪
✅
⚪
❌
❌
❌
✅
❌
⚪
✅
❌
✅
✅
⚪
⚪
✅
⚪
‏۱۰ )
🥷
Robert: ‏(۱۰۲
❣
)
‏
⚪
⚪
✅
✅
⚪
✅
✅
⚪
❌
⚪
❌
❌
❌
❌
✅
✅
⚪
✅
❌
✅
‏۱۱ )
🥷
♧: ‏(۹۹
❣
)
‏
⚪
⚪
❌
✅
❌
⚪
❌
✅
✅
✅
❌
⚪
✅
✅
❌
❌
❌
❌
❌
✅
‏۱۲ )
🥷
Zaker: ‏(۹۷
❣
)
‏
✅
✅
✅
❌
⚪
✅
⚪
✅
⚪
✅
✅
❌
⚪
✅
⚪
❌
⚪
✅
⚪
❌
‏۱۳ )
🥷
✗ᏦℕiႺℍᎢ✗: ‏(۹۵
❣
)
‏
⚪
❌
✅
❌
⚪
✅
❌
❌
⚪
✅
❌
✅
✅
✅
✅
✅
❌
❌
❌
❌
‏۱۴ )
🥷
❥sheyda☙: ‏(۹۴
❣
)
‏
✅
⚪
❌
⚪
❌
⚪
❌
✅
⚪
⚪
✅
✅
⚪
✅
❌
✅
⚪
✅
⚪
✅
‏۱۵ )
🥷
Ахмед: ‏(۹۰
❣
)
‏
⚪
✅
❌
⚪
❌
✅
⚪
✅
❌
⚪
⚪
⚪
❌
✅
✅
✅
⚪
✅
✅
⚪
‏۱۶ )
🥷
Ali Moheb: ‏(۸۹
❣
)
‏
⚪
⚪
❌
✅
✅
❌
⚪
❌
❌
✅
✅
❌
❌
❌
❌
✅
✅
✅
⚪
❌
‏۱۷ )
🥷
Vista: ‏(۸۴
❣
)
‏
⚪
⚪
⚪
✅
⚪
⚪
✅
❌
⚪
❌
❌
✅
✅
❌
⚪
✅
⚪
✅
⚪
⚪
‏۱۸ )
🥷
ㅤ: ‏(۷۵
❣
)
‏
✅
⚪
✅
❌
❌
✅
❌
⚪
❌
⚪
✅
❌
⚪
❌
❌
❌
✅
❌
✅
⚪
‏۱۹ )
🥷
Mohammad: ‏(۷۴
❣
)
‏
⚪
⚪
⚪
❌
✅
⚪
✅
✅
⚪
✅
⚪
✅
⚪
✅
⚪
⚪
❌
⚪
✅
⚪
‏۲۰ )
🥷
✨
𝒫𝒶𝓇𝓂𝒾𝓈
✨
: ‏(۷۲
❣
)
‏
⚪
⚪
⚪
❌
⚪
✅
⚪
❌
❌
❌
⚪
❌
✅
⚪
✅
✅
⚪
✅
❌
⚪
‏
👥
و ۶۳ بازیکن دیگر با امتیاز (
❣
) کمتر از ۷۲
❤
خسته نباشید
❤
‏</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1ys5ufQQQsfKs8CoYF468u3G1a7ToU13I1B_VF-6CO9qJ3qHF5WbneE3-7S4ngxVtEvyx1y9B3qKJwKXwkubq-PFtgI_YXpGxgqyScs9XuEXQcu2AUE1ZyZ3tniBk9S2-1g7TGvjohw1xvoUKmAeZhh-HbY5BOCZi4tn5Iz9aeN_z62Ci7N9W_Qp3GmSEKbSTNHtDLtWf72ExiYzHUZc8klBxwiHAzPbBIYpO24LH7Xrz1x9jrOF3Q4WaHPfztt-XgytC3t-Or7ycOgUsD78euqbEkpLDzmy25nAB1ljTKW2ACQM5nP-RIu9oVx8woiHA2UVsIs6sUfkac9y1psuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=oGPI8Fj3qI36zhzYN43Cy7x0OlzkzV02wk0N_2pbt1din9yyv7TVUob8n68RTWf6lVX-XmWWbF9wcVCDPVPU1NbaM71y2ymd8AyF2UtwmmZmkT-JYd_LKEtQy31gyHbL0LLFRdLlppnENPBO74__VCUlDG-BcuToUbINWqCs9znRRn0Zz8AgNRcbekwZ8kkWaOAF7678gFA9op9s3iDlPEs_aPpixzJDaJGeRAXuIp2nABr9ySBsfbsKxuag82IH3ORtlrzVaW_lYXa1l3ggDtW9MtzdmE2L6AT8oNNDkTbh8LR94oYBG26pjJbWSVFrP-2GqCQIW9YUtcKdw34srw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=oGPI8Fj3qI36zhzYN43Cy7x0OlzkzV02wk0N_2pbt1din9yyv7TVUob8n68RTWf6lVX-XmWWbF9wcVCDPVPU1NbaM71y2ymd8AyF2UtwmmZmkT-JYd_LKEtQy31gyHbL0LLFRdLlppnENPBO74__VCUlDG-BcuToUbINWqCs9znRRn0Zz8AgNRcbekwZ8kkWaOAF7678gFA9op9s3iDlPEs_aPpixzJDaJGeRAXuIp2nABr9ySBsfbsKxuag82IH3ORtlrzVaW_lYXa1l3ggDtW9MtzdmE2L6AT8oNNDkTbh8LR94oYBG26pjJbWSVFrP-2GqCQIW9YUtcKdw34srw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Iy1bUTV61pOCduwm2mQkqOyZIuGkpNY6Gva2exUU94qMmvx_02xM41vvobPF8VTageqM5MObatq1Giy2USclFxGBYdTFO0k1-id5GPDclCLh5mJkrtgZM2053WI3S4-Ww47F5EZ4X51C-zLrFpqZcH9QXL2eoFW3qDXpJpmGaLNmOlU2tHakD7ZEaBFwqj_hZtu6m2zRucXt8am-FTYmIkMdGIvDM8A34d4e0h8VoPfebVeMEZ7Zi6AgrRCsYjYVctuLzTbvj4IRjHvMS-b57eTCycznad_33Tmo3F3t5X2U1FCNveIX8lWbuEQiJc1Pn9deI6ZNI8c3IoxVLECAUndCt0PlZDx_ozYe0_fDRCFER0iYic99QLgTl4gXVVuHVDQO_-5bHDd4k_MMHl2p5a4H5RBu2lE_18l0PHNyY0YKpAFG0N6l4ocnsimkxRq2xDESZ0zQ5g5dPxl_LgxVqDGY8aYiKJg9uAv_Hl1DIi54cvf3zc1jc20382HbEBQcblvZMDnhGe75pDdjDoreM20QGrHjzPgLqn9tJyBD3ZT6Wn9LilhJAH7A-OpuAe5EvaJVZUsDt7xO-1-cOabjNVBXuHhTybxhzlPWlrhvmQ_THOllXFAVLwWqMnd4vBgY-NjNMAXIfgNTE88RdqU7NKY-QiCFAswSLo40FZ2AxAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Iy1bUTV61pOCduwm2mQkqOyZIuGkpNY6Gva2exUU94qMmvx_02xM41vvobPF8VTageqM5MObatq1Giy2USclFxGBYdTFO0k1-id5GPDclCLh5mJkrtgZM2053WI3S4-Ww47F5EZ4X51C-zLrFpqZcH9QXL2eoFW3qDXpJpmGaLNmOlU2tHakD7ZEaBFwqj_hZtu6m2zRucXt8am-FTYmIkMdGIvDM8A34d4e0h8VoPfebVeMEZ7Zi6AgrRCsYjYVctuLzTbvj4IRjHvMS-b57eTCycznad_33Tmo3F3t5X2U1FCNveIX8lWbuEQiJc1Pn9deI6ZNI8c3IoxVLECAUndCt0PlZDx_ozYe0_fDRCFER0iYic99QLgTl4gXVVuHVDQO_-5bHDd4k_MMHl2p5a4H5RBu2lE_18l0PHNyY0YKpAFG0N6l4ocnsimkxRq2xDESZ0zQ5g5dPxl_LgxVqDGY8aYiKJg9uAv_Hl1DIi54cvf3zc1jc20382HbEBQcblvZMDnhGe75pDdjDoreM20QGrHjzPgLqn9tJyBD3ZT6Wn9LilhJAH7A-OpuAe5EvaJVZUsDt7xO-1-cOabjNVBXuHhTybxhzlPWlrhvmQ_THOllXFAVLwWqMnd4vBgY-NjNMAXIfgNTE88RdqU7NKY-QiCFAswSLo40FZ2AxAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xc1DteD1Bhoju4aXWg9JVbvB1Of9NxDb_7I8s3aJmf8wh3-0YsrCxs4FJm89COtAbo2sNrF1Vo6eNGcOdcjPzaS4x5CGeIDD1OQZ9LrNpUt26kzI3PK09uA6ZnGWmNo5OttT5r67qUp5eaBHU7eoUxPre41WPn1KkX9S1mJe6nSJypwkkv1rN0_EpXwOT1GwkVHK02s4-947727FnQn_Lgr8FeIa4gThF96RfFO3PfJS3rjp7dT9FiT_QRFDJJjtI3Ogz2Akv0LeLjVj340Br8puyL9ST6D758bbtpL0ybCLbg3M9EpJSQeFrLUApHaMWHOLf4pBM13BtEmqGsaSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwRE8Ov1lwkAtGQmFG0rZi1X42wDg3MW3VpQn58Ikp2e2hSzrzV3kFy7nCwzaJi0Be5p2mbNQUn3rNE1PXNXhyQ8zsFZhaSDzChSNZ3tmzOcv6k-gIqnBK5RGClYNjd2H6C4ELRJRnMIYKyql02K42L-npCI_DgWctag-aIdKteSHWSZAhIk_HbWlWiP825JpXf-9jl5TuW5hvn9gdDiXGxOzA7nhmbdNy_dqI3Z6Tm3WDTWG9cSVkOvCHyFQo_d7e-jlhDybRU37F2cF5mJTOUNLli494B3pqnuGMeNoLM1YWFIq4K-UOiA8WEQEOuW9v7zecvuIh-ZkUQ2v_T6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
کد تخفیف حذف شد برای راحتی قیمت هارو آوردم پایین راحتر بتونید خرید بزنید
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M022I9iYUmtzMsdb4LoS6Wbms69PnoFllpaO-2lRfMk40mi0sgVQBDXsabUQt5gG_DUa5BwLRAAPb4CssugxBtMYXQkXYAKtvM4oOSfzy7A9tlSjTKMN8FOi4voBEufPu0i9ITI9fUMF8z-UpXX4f-MIuZDlJewxuhQN-vUXjonsrWIGVC76F2av9scTaRloPuLr3a9LXBqhKgPNE71xtVbk-Wh1nqiAKeC7FH1KCmd-7RTQoPpV17n_88UbQPPS79GPF93rjdTg3anMtKiMyKhXgHWcuhSy3Wor9mn684rAQhfs70shNfhvmnmjdFYxGqsWEI3sJTZWdugkNmgVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=UpUlyGxu2OrLh_opf5GS15ByduS_kOYA03sHuBYZDft_HXymLn3AY63pXssBGt8WgSWibbfJe8ngunkCEJ26qouMEIkawo0AIHBCwax8IqCagvgE-VzSHPve898YnXXXID2aZFJUfmVE1HxNgG7yIGqJXyzckTsDGJKYWv0FmK7l9b11quyj1iZ5LDBuUl9gdtd7w5pakiCNMJ3rWbAxcNptY5-vgJZ1aUNlPq-fyskpCWoxmlFNxPpELMUQ6bedMtkYfGhR9RaZLeOi58ALxw5GVkds9Xw1ZnWdoZlyghlVhYuPSCeAyWtWBAZt2zAHEWEKiucIH-eq-yYb7OCZwkcdgvHXs_D0PeWHJSzJvQSD9H0P6aHHsezY_YHDc4Na71GBxXQ13LLoH2ei19Dst4hTRf801ZLk6dv2sxOJXHfzS8ziJfyp-yv0TGCzXBkzy7aSBUDF57B4JDAUqPs9AKSeTiPxnprE4CTvKwnjxRs7GJ8-YL3_BMwYrn8hSGmaezwrw0lsvMvDIKZVvoixEIyJBvmHKtc6eBQF0uLHzSXWBE6oWlv4fTHC_Cducge8mBCfD0aCgeZXHQVaTabKJoJGSqmi3Y8479VQNkBb7F7-p4mmNMPGbBDyga9Nd6BtSGiYXSGqQd9qC43BbqbSFkaWBsIH18xdepQGyrAXNQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=UpUlyGxu2OrLh_opf5GS15ByduS_kOYA03sHuBYZDft_HXymLn3AY63pXssBGt8WgSWibbfJe8ngunkCEJ26qouMEIkawo0AIHBCwax8IqCagvgE-VzSHPve898YnXXXID2aZFJUfmVE1HxNgG7yIGqJXyzckTsDGJKYWv0FmK7l9b11quyj1iZ5LDBuUl9gdtd7w5pakiCNMJ3rWbAxcNptY5-vgJZ1aUNlPq-fyskpCWoxmlFNxPpELMUQ6bedMtkYfGhR9RaZLeOi58ALxw5GVkds9Xw1ZnWdoZlyghlVhYuPSCeAyWtWBAZt2zAHEWEKiucIH-eq-yYb7OCZwkcdgvHXs_D0PeWHJSzJvQSD9H0P6aHHsezY_YHDc4Na71GBxXQ13LLoH2ei19Dst4hTRf801ZLk6dv2sxOJXHfzS8ziJfyp-yv0TGCzXBkzy7aSBUDF57B4JDAUqPs9AKSeTiPxnprE4CTvKwnjxRs7GJ8-YL3_BMwYrn8hSGmaezwrw0lsvMvDIKZVvoixEIyJBvmHKtc6eBQF0uLHzSXWBE6oWlv4fTHC_Cducge8mBCfD0aCgeZXHQVaTabKJoJGSqmi3Y8479VQNkBb7F7-p4mmNMPGbBDyga9Nd6BtSGiYXSGqQd9qC43BbqbSFkaWBsIH18xdepQGyrAXNQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBgIiXvoiIVK_Fx3vK_8EFulAt_8y2ZhZCC-mqMgQPzKcUh8cSjZxDvGRK9DM0lDYe2I1LsG5QqrNFZ1BwcjJpcuYWUM51sj23Jx3qFI8P2C8AiGYJ1IH8JtI-eRgsvIesJF0U49R7UNIcmX7tKUXJuDcA_r32qkvioNj26b0BZo0L5MAxZ8P2OCOIyzzvJn_k5f3QExFIHdRzja1SgWsn7OS7Jge3iYBljt7u8DMR6_R3-HJX5DGIdHMHmNa7IxQVU73t-t4E9whWLAxhEr8pvT7-JXur56Q-NMQUr6oyZzFzeKfEzHRxS1ASvw83bSRZZ83DhFZQZFZw-DPulCGwN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBgIiXvoiIVK_Fx3vK_8EFulAt_8y2ZhZCC-mqMgQPzKcUh8cSjZxDvGRK9DM0lDYe2I1LsG5QqrNFZ1BwcjJpcuYWUM51sj23Jx3qFI8P2C8AiGYJ1IH8JtI-eRgsvIesJF0U49R7UNIcmX7tKUXJuDcA_r32qkvioNj26b0BZo0L5MAxZ8P2OCOIyzzvJn_k5f3QExFIHdRzja1SgWsn7OS7Jge3iYBljt7u8DMR6_R3-HJX5DGIdHMHmNa7IxQVU73t-t4E9whWLAxhEr8pvT7-JXur56Q-NMQUr6oyZzFzeKfEzHRxS1ASvw83bSRZZ83DhFZQZFZw-DPulCGwN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
وضعیت سرعت سرورها
@RUSSIAPROXYY
🇷🇺
📌
آیدی ربات جهت ثبت سفارش
👇🏻
✉
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/evcpGbg5wdPB0DO2CbADgGAgtemmWTyQUFVlinRwrgVMJk8NDcoLC-rPr2Q4WPIkf4iKk0Ii_S2Nd5Ei93Y5ck82WjNncyGhFt4nRjnHJkMDWM_VlFuKP8vZzXgaoJOeCRfraxn0YVBlqtZKwhbyUukfFKAn5sEUpFiba6h4PDrShjwE1wjIP5TVkQuNH9bSoBHKJH3pm9dD_VcoNASf_vx9fmwx3RiK0JSVEcHLLYhZve9tWs_KHDks4t5RX6Nqq-Mk88nepOBZR3YnATlroC6hZvx8x8SssN5-uWzy_9h6AehXj9UqX_p4-d2oEPsjzZvLqZ9J18LJSanQWV6Plw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8WAPfNLMHKd7VpmqapEnmgzqOWHexXylTki-HlaL4etOdvz-XlqglWjsAxgpY4DNRDbuvlky8G34cT5kxX4fEXGaQXw3JmGIBKgRN6C83dtAaz2R0ychDVWI4m1JinFQ9CsiafwmFXtNCr6hknfp_7lSQjG7hzcMSso95NjSLHUf2zNO3l7EhrpWFa-UZ4rngi9VQ71Kb8mbLtZSHSLrAp0OUEbn5iQvOcx2_pwndzy7Wn62dVvgoJozBEAevJvBYLaYKwMOlhKeYNitLxmPBZo9No7XhNhOez_hPjWPfWC4wLizCYrSLWQAV0KN5WBqplrvTWZE0qsmLaEhenEBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
