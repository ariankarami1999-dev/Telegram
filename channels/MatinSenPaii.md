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
<img src="https://cdn1.telesco.pe/file/qMzAWoUUxrpB7f0tHMj4z3wZ22YfSv__GjHBcj7jVBwYUI7tTTvEvzspa0YsUZZyJ6SajzuA8CxZ1bLNIS6Ib7lrOQMYCt5n9qBoFfts8WY5PL5HaxkL0VsDCA68neHlfeW0tdfnozkkctmasElkp6GnIW_H4eBeSyT3KqfC5vRpOZTYM7tWj9e5hD0shN-RXMk8Z6NGm6_ibDmlfLpvN9wSCq6rN94br4wgJpOxCyrGTJ43RQFvxyORN6WeFfxlajQYL3sudvkTiiamRZlTw_AcajyC_QWD1ynSaE5PrCczS8ILJgqwWMtA8rZbpW5EH-Mjr7MVL1db9JMPT1xjkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 17:43:08</div>
<hr>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/MatinSenPaii/4947" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/MatinSenPaii/4946" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">من خودم به لپ تاپم دسترسی ندارم الان. اما Sni Spoof باید جوابگو باشه قاعدتا. اما اون متد تغییر دامین رو هم الان چک کردم و بستن</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/MatinSenPaii/4945" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PU-XAZJtM3fniVfe3s9Jutg7eaGn9dCcgwOttzSMsbXR661WoSau2D48f11yfXa3FDYRJ6SjZaJbj_peZzdc9icN_4M3OkUbeaGfG4gFmfiZdt6TAv3-wj4-8p5DzLDN2EqmGXS2BJ4Tf7Zd4GhwHWR8CseIbYtUmhR2sliZ9hozaXhQ3SpfWa0jGtVc0Ut6fc34gKdzYUcJxQ-_v7uXhONoIT8Z77liVhcHZJGm48WBOPB40xprtue61xhYQdByxQlPv6hH7DBE-s1JEMrqlwhjFN2BJ726JHfyXb6cJDKeB26VauXUwQVV-eq8p8kopFrBEfNHPb62pau66CmO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m8so8dHC1yC5axlczNCtN-Nk0-BwJDwk4eYh8-1QgcGrWu_R0qm_d-LTKBozupKeCG2-gxIdJDfum3w5x3zT3dKHKfXb36-OfvNzrxtjrt4mnfpwukKgxtfyeQC9n7O53DOV0UKpZ3gC5h7VZmtyqQOV4YDPlIlbz13vFmxfvNFuc-cdTCtbjLSOVotGjag81xTdER_kBqXqo6Fcmwc6KjZzPG9AzAK9VJQb5UwTDa1BYfQs0ljsW2ekTglh4eDhjWFslFjx0NKtcbPHrfuP1eG21lDcgU3JiI9ubQxp56m3AaDeOk21iQ1MwHwMMzX81CDxXsnkRh6aVHcLIExPNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد فکر کنم که ساب‌دامین‌های *.Workers.dev فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/MatinSenPaii/4943" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد
فکر کنم که ساب‌دامین‌های *.
Workers.dev
فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/MatinSenPaii/4942" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-poll">
<h4>📊 کانفیگای کلودفلر شما هم قطع شده؟ (چه Worker چه Pages و هر پنلی)</h4>
<ul>
<li>✓ آره❌</li>
<li>✓ نه. وصله✅</li>
<li>✓ نداشتم. دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/MatinSenPaii/4941" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">برای نجات یوتوب فارسی و درصد تشخیص ویورها، برنامه‌هایی داریم. و طبق تست‌های کاملی که دیشب گرفتم، خبرای خوبی دارم واستون و توی یکی دو روز آینده می‌بینید دوستای خوبم</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4939" target="_blank">📅 11:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RUdasHMFJwkUUQXoWGBkj7A-SsW3Ps9nm-LhcVoEenp6gZ3Y9pWOKetnPd9Reu16pB-z9hzUJafsxvyVbXA7N6s9-0taGbM7DwuL-RDSl6akHbr_YIk8SA3oL6xSp8-7yzrAYhG6JDOXB0vrIneuMwBlxAVwlMdvIRw1nfrYzLBvcg_JM4QnkjN1eGp-7tEU7RQA2RJAOw8sXbsV_SffSF3j-7rWFIEe0QYpvyyNjsOV1K3hxUZlzff37dSjI_np1CTKvzevE3ISxcvtmaJy7fKW7g4z_lhuEb2gllB4fgTI7UckoDG1Jh_iuprwyLUo66duswOZT_tXqoHb41JIQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nu-3gEcQtqxYMtRIiIped9BWvY5zD9AlFaESPms4Fw2-A-Bx3ugIGbLoxN9FXixMPUNg_b8eDTneoQjTn_GuMTPa8T9adH40L4fOW4dtmCBGDSKv-UgKUhiQxNqxpRIaJ06nS-NoJ3yzPUi76-TTaC08FAH7itgTjjrlaI6o-l2fMEWjEoBwn-hQHafS518ZfQrxvJYghxHqEXJe7EBMo50wFu1pV4LTHw-gTS7r7znsKgC7G3FLtppmItHPMoRTEclUt6i7Kuk7s9iRbT7g3Wsv1iP9t17NPqziqEuhfrKGV7teqgDAAI1HMfX99l4Hdcl0HcjPwP6R_mAnkgmtYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fJAPHnyBF-yWy8wQFMHdTsqavlSt9xJZdcjXUcohGH2ObD4hnpW1GRjHAMGzfGFLdq5FiZMOsoks6rQbVn3Ay4P74MTR9_jYnEMSEDcO4p-8LUyhWv6kLJ90OKiZoCFCVFB-CrkgaeM-k-pPxiHN1JDOgo7hrcREJUQs_PoT4F3aPCf0DfiH25cwa2eo4cT2UtI56MXqZkrdkd3xuuf_Gqrd9A1QlcJxB_5iv3EbcSluaFmgtWcOQ5zJ3XZeqN51n1efkfrlyVwld8iTF-urWQYbg9ROk3p5Ny0yGwKugGe-GaDJjH3IrfDxCbDgSlaHhNWEi3hMHpVOwZhEspiGIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZyQWF_n0JhEtaHjDKT1bj41pQuNiF-vcAhAu_6_o1MIYte_Zez3AgWq9MYKB7Oxq0xsheEewlQr7EgYyEUujAEXjUE-Ay66QFCfvU-divTA99e9D3WR4c-k5V735wa5vbrQ-D92V6yEVqpJVAWHQC5nnqyfoTrTe97FFXY_EYfQxofR6w70kMvIjC64LquC00hrszGw2DVddrPfIZPuizt0YD4eClp0mPvRFzuT2MiUGoQzESq-GXwCTAHg08cftyqu6DzWx49MES4aN59vW0v9MFpvEM5lTqwWyr8_EFrnbjJpHkvsX62gmwFmk13GoTV3rDeCoqydz6qLQg7gA0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WIskxBn0hiG7wTmnJ8bCT6Gwd0j2Sh-pncj2Omce2rs12CjOAuhI9V7NlaMrHHu48sbXjQM5XQCJoWoJFMGfuCx5j5tMbzH-ktcP7CFNR3d9h1l1kuFmOhTZRZjogxy0aWk0V72OlYYaYc4BP2yJSg5-pxHI65PU2INuNmHgg1fE2VeNZq8NMVhkxw9fjwtHtCuaggpS1RGErmD_rpkS2BNC8K5LaFKn8G4gbjDqXoClQpCTqyZlnvcOS-Rirsyp0qJC-T9TzY_jBQu-9REHl9J3FDoitnItG-cBjABgqXxTtK0nGEkGTjMD1764nop8L85XjCsrfO49x8kHEQWKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4933" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4932">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eZY8r5PseT6vCRi0Ovio0ZOvsdQNDHG1UHyG0InRkkt5kd0qmAaIGrBcFTn7XHN4aZJ6isEzDcj2IUlDhrraSqzWQV3UmvbC7N00SqYNFoL5ajAZyKYAeadcDBOLGt5NFAa46KKqSf4xWkU78YI4gL3qoT77xIG8XgTYXZZpciadBT6VMGEunRaUxz3CAQ6qHVa21tjoq0vE5m3yA4mDqPLCkBNz0fvqN-rA_Tx-Den46aOSSvAMeeM0zjg5EXLC6QrajTPIdK4Se5uFez8gGXei3DSM_PkwvOB-mSi0RILHA6rtsvY5BOQ2AJBiLiPDaqS68WX13m9AjD6pRbqUFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله
محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود.
باحالترین قابلیتش اینه که میشه Mode شخصی ساخت.
و از معایبش هم که بگم، درسته UI سبکه اما کاربر عادی ممکنه یه کم گیج بشه
و همینطور فعلا توی فاز تست هستش
و ساب ایجنت‌هاش هم مشکل دارن
پیشنهاد می‌کنم ستاپ فعلیتون رو ول نکنید بچسبید بهش، صرفا در حد تست
مدل سفارشی هم که می‌تونید اد کنید طبیعتا. من الان OpenCode Go اضافه کردم</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4932" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WvIrVXaHX_9AQTBk29UWUNuKehAXPHrCc-KXkjQ4d97G-_yii8xEq4YbAJdvmQTiy7rb0rwvNZYq0rpEu-a6MdQcXMfSw0qLjEEttBx8rqqZFQjj5nIG4aif7J83J0REtt0PE2e_VXc9BQckWjL7hpP4iJrEiZ_m2EbnqWZTPw6Lp1BXyvlXHAO1m2luuPoV-JUFmRq2LOnNmmMx-6CyL-sMnunz1Lb9TC11RIMuNv0H-TGrWzhdb0d_9mavgdHr6tlT_kTgh3khLnPK4pHRMA6a5EMQTYpQKxktWd7zZjSx_XJgoal7u3vDKoITX_KtNbCYFL5GRhP2uoZ6dpVj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود
😂
😭
اینو چرا پوش کردین مسلمونا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4931" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔺
ابزار کدنویسی متن‌باز DeepSeek Harness برای رقابت با Claude Code معرفی شد</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4930" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rtb7ZoQLAclqVzHoM5dLoOhWI_brMrQ2vejfoa_O3Tl55Iu5fP26d3LrI1BeS-C5m4zFiRPHvOQRFfxu321Tb8kI-lYpJzFzgvcpy4DQmGgQldnqieX7pOLWC6rHdnGNxqczIyCuUQSzHtZK3yumKBfXUtTuH-FsKaGVfoYEFXR_PncSqkuxiUPzA4WY6cmpbysQdqKEhImUQSQld24loEZnmoXXdINo2tvoUW-g2JOHGrIkOnx2iU31Hf2YmtLRH3c1yJPzEA5YcafMn0oVQYB0MtRY4BAU2UtNQSTMfvX3sQcZ9jPpjTiKdaHQOSW4Lf2HDnO1ApZdy7uPOLtOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه قابلیت خفن برای هرمس ایجنت معرفی شده به اسم Bot Mode
به جای اینکه هر بار سشن جدید باز کنی، می‌تونی چند تا بات جداگانه بسازی.
هر بات پروفایل، عکس، توضیح و کار مخصوص خودش رو داره و حتی می‌تونه با بقیه بات‌هات حرف بزنه و همکاری کنه.
https://github.com/NousResearch/Hermes-Bot-Mode
@RepoFA</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4929" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جالبه که من دقیقا سر Kimi3 هم همین مشکل رو داشتم توی کلاد کد.
الان توی OpenCode + DeepSeek V4 pro این مشکل رو دارم
سر دیپ سیک فلش هم داشتمش اینو توی کلاد کد</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4928" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d-oojeTR_LuwnJfRpFHwL5JmWR2Z-1zDDGLEEq6Xc5uZ5NM4xgVeLc0oWUnN0KOSPLdbSGx_OS3yV-4CVrIoZd1t4yvmczmHx3-TeZ3LbKuaXMavezavTOyxaoT0w9fIbcd6MSFc5gI9Y3S-1VbL7MpPUyDSKO10prj5rDtsGA6a3QDhkBIPvcVM5BfRQmZYSoX-OcBfHaM_LGkDKM6vl3DYuS98lFdWjhm5OSrRxUAv8F6UGBg_tHowDU7HJcEu5I_FsNeaAIKNy7UVrgmMgcRNOE-ZSf7JKtqboNSS9qZ0xTe8f95KkUgAmnc_CvmYrlq-SrqHJqQ2A40Cs6gEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا عوض کردن VPN فقط باعث میشه که از اول شروع کنه به Think و من اشتباه می‌کردم</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4927" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4924" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fdze1MGvzmQDXZIVvgbrQDmQCM5bTK4Cp3yHVwuEqq8vgPWC26LdW105MdbUeuDKuRUJVz6slU2FnqdYx2ZtYT1AjtfTIjMkct3cseDl3IR8w2WKnNkMZ1cgX5zV3aVMmSh5bhGC4IuYTDQm5LxxNOWZ8UKn4we39UZG46B8X3Q_D0OYxMSD4PhMa1gd_09kCzr81mRGvHMc9uAooYXkEtAkS4f9h7jz_O6MuP1otNIygqvYEGCmpQcqbNX4hKSqohkgAL92IK_dck0BO90d6Q_eibF6J5gO8glycWc5WHQLCwv0Gw4yNx3UKpplHNqQjWkOQV-ineb9wmsG8tsZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو
تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4923" target="_blank">📅 10:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CeynBGKW3c_hNj3dhSef1nDS6zybXys20AdA1KvFe1r-qCUYlnPoOAr-XTDkjdYL2Bgtem56sKjm1EA_AM1V3faW9ay0cI2_IStC4oYoywpEDbWzYtl0sGg15kBidj8LyBNC2sOzHClzfBnJtlnkiXshMXexugqPldcULzgX-B835aqKAOwqcnYAi1SnvNUu-Yrv82K0nD50yKit9Xb-i8tnnmqlrOMa2jJsi3pCbF73qPB_o8Xmvr46WMlr_Dkl76LxTsEQ2TlWZ_aXfYgLkk3fJcJG8DQ4Sds3Oal7rGzVQeSC0kS9CJgQdh41pe-AHmV_vtIsPxsZshMDhhoQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از پلن فری هرمس که گرفتم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4922" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lbYT84ojLcLIdNfN2eA3s1U2lM4tzKbGnh2O8aU37t1BN58uprMgvN5lmKzhvL5ahe7yprhsFBaqbqL6ppRPz4viFa7faSeOblAf77YEvAhvT8n3pV-9c2wHdsSQ43B484sbK8bI0vb1C8k6x0mLSPsFkunUmYDzEmt9MIBMVQv1eAOxPs9FdHx5JJ1oxgnU-E1rbvw3SSeOp5D69T9ULQ8I20oCw0Iro3jv1ZDhhabpvSEndVMxTAE3BVs1Zy2BWV4DPY1qwDFu5BdQxDia7IxC05_S1FjqlrTLPQKyeL8yI8FFurnng_cqWcGRLH50QCcGiK4lEqmO2rHHMnD5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4921" target="_blank">📅 20:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگر روی 9Router+Antigravity به ارور 403 می‌خورید، یه بار اکانت رو حذف و دوباره اد کنید درست میشه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4920" target="_blank">📅 20:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4919" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QSnfDZ4Njt-jenm4dDWq-Whe39pQRPKPhDOcTU3rutRXh3PCn6D3TO80nJ_G7LTwsALtIVxX5ouFMPiOnYOEQlpj1ZFOSo9ibCbHPj7caqS05wg7iRVXzmP-ZyiXqSfx7KqXXJIFW4NJ7Ezlb3i7bxqrWEHLJ9Q5rcftKaDGUkuVb3sKNrSK6WXbmFpx6QyS9u9GBh3pJghyOExokaFOn5fWR9w0yx5DnmAcXExJVshWt83l7F3jLdMwRyTJKP8rk4UtD-01PO0lK8SEVmzk-u4xWiTduTMhylKMRwEfOX1_3wEG2k3v9mh6uos2F90Or5LaTxuM4IpyWwnKgWEasQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4918" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nfit67JKvdemjxXRnb1TipufJGEah6ZoLd8jWAtQxbTRhRo-P0KIr84RgV6feDMfzT9nAadoClGu3q92sitYSSfjlBepI77ZKhk_FvIsj-x-48CR7-3pq84EypXpnCVwlSFz0BbdONkGX_R_8LOGvGj_rOyVxgFPacWrnkqikUCfXFvnk4LBRZz-v_-Fp62BrxQ2uKfaz-4zJVOYHJV44ExargonL30vZ0AefIqsaY2fYZ3VBzukuHMTEy3oHg5Da5sX-kFyZFlBI8iHvdjpn0EsXKoBTwoWAj7mYSxPGsqyQ_Gm32666FyIVHIHxjhgiyQLxI4pBYbhWhhAii0AsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FfJ9w6064ve4kbk2dXQ9eeGkfzkRcFufB2dUrA_gfkx5aOlTR0iX2vKY-4D4SFRZXEIFvIvr1ln9HVH7zJ3uj_xjbffNMbGObIdCL3OD7w1K3-G518q7PtRdag5ulMD0GsFro_ius3hXn-qqJZ_ZoGiciHcO1j1KLOZwNcMA3In7k5PgkpOaCx7CslHgMf7JMiRe2G6MtA_NTOPEKOd3i099JnS-6K1GR7hOuIRq02Vi_xESB_nTndLu78hHYnhjIdB_gJkfgybFKOCGMan8TwDH7GdfZZDE3j9s4RrnynDIg0es6-AmkL_bgiGMl0YiFVBd4MsGnfhBgvB39x-U9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cnrIC1HHSTMEwYs-HD7tCXZ_WBXrc0DpJyEdCur5KrVwmLrNHi03bX3L6FwxFVtBymdcxk5U5X83ihPbPyWykyy6SsfkxgKJHzPqyVSE3xkNoy8HDI0tS9WDux6wqmHKZ24TIAcJisZMg6U4yvP-q3whqoNAVWt8PGK7HD7j4kJL_I-2N1KML-nUq1sxyshT4b2p1SMpi_b_5Qi43qfuGh6L50gE0G8WiDLHU1OFODSP1_qavbDDW_ZRxtenAFfiSYDfYk6HCQl5qrIOILhwJ4yFSQy4cG0AiUZqG2S1HlqXfRxrTptVeqeeRkgeMzWYr0AR5xmlY273jHAUIoI3MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی
خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید:
https://app.mpay.cards?startapp=ref_PzwXZ8
(لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید)
1- بعد از اینکه وارد وبسایت شدید، Next بزنید تا با تصویر  اول رو به رو بشید
2- روی Apply بزنید
3- با ایمیلتون لاگین کنید. دقت کنید که تمام هویت کارت‌های اعتباری شما روی این ایمیل هستش
4- بعد از اینکه وارد شدید، با کریپتو 5 دلار پرداخت می‌کنید و کارت برای شما فعال میشه. از USDC و تتر و... هم پشتیبانی می‌کنه. برای آموزش پرداختش با نوبیتکس و...، می‌تونید یوتوب رو بگردید. من خودم با Trust Wallet زدم USDC و مشکلی نبود.
5- تبریک می‌گم، شما Visa card دارید به اسم خودتون!
مزایا:
- می‌تونید توی تمام سایت‌هایی که نیاز به کارت دارن و رایگان، اعتبار خوبی میدن، ثبت نام کنید(من توی Nous Research پلن free رو فعال کردم)
- می‌تونید برای OpenCode و سرویس‌های بین‌المللی، با شارژ کردنش پرداخت داشته باشید(کلاد رو هنوز امتحان نکردم)
- و تمام چیزهایی که سالها از ما گرفته شده و ازش محروم بودیم.
- ایرانیکارت و سایت‌های مشابه، با مبلغ‌های فضایی و میلیونی فعال می‌کنن همین رو. و به نظرم 5 دلار، منصفانه‌ست
معایب:
- برای واریز به حساب، باید اول 25 دلار شارژ کنید اکانت رو و بعدش می‌تونید به کارت منتقل کنید. تنها محدودیتی که بهش خوردم همین بود
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4915" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LpOI1kEJx71AMQEBY7SCQFhCMnVOkGQJKwSoR_PSx9GLCKTN8EpiyM6Ms-aXLGsWDc-oIhC8zUfcnI8lxhTJFoUe_P27njy3hutrZjOmbbe2fJQGRs3Z9HNXvB6cO-xq3IznE2mriOg6UnLQ0YwEfflaIM-4Gqu0vp_hL_tYhLwOc0yYkPLiXI5R1OizlsvsZ8q1cRbC6uSHLpqveCiovVFwTQoi5e12fzVzB5raPvRqkCc44VN9TL4XSRFZ4gi0G26Z_r7tm4fcHSZCWjHzqcYIx5sTV8u6A7L2UW2CbBizWCPl5y2LHpPy2GUWlyNLYbi3vNPu89A-hCvtGv9OXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.  از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4914" target="_blank">📅 19:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">همینطور روش رفع تحریم آنتی گرویتی هم چون یه کار کرک ماننده، باید همینجا آموزش بدم و اصلا نمیشه یوتوب گذاشت:) چنل سر دو دقیقه استرایک میگیره</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4913" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.
از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم به صورت متنی</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4912" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این دسته‌بندی جدید کاناله، با ادیتور جدید عزیزمون محمد.
پلی‌لیستِ "قصه‌های مدرن"
قراره چیزای باحالی با همدیگه بخونیم و یاد بگیریم
🤝</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4911" target="_blank">📅 18:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kgl0rDwbo-ZvisqM7dkYbg0NAx4oO6QwZQPNrS6Q3fkcibu1K1OrvFoescOMMzJqTguDjwcFM3x0vUgBcUDmi1HhK0GlnVFzdv46Lj98qOstFhBjmUT0dNsHbSX3MKgjb6zPsfA2PSJd8QbKleY6pb3S9u5IkCnCQVHMJ2elS8ccmYu5LVqu_MBbKZvL6KrtwFYpTLbL1XhhGeBKy69gZqlxyTdMH4hpoFdhaMe6djqmxsXwsOCnRWDTmTjOXK-_5xrFAxU6yKrZ6MrbG5e5Zp4YR2dZ2GHt17KpxaFV3CnCaO3jGGXN3KWRt6RXVQWMZI5z54ompeIfHw61q1fTdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
قصه بارکد، خطوط سیاه و سفیدی که دنیا رو عوض کردن
هر بار که کانفیگ V2ray اسکن می‌کنید یا یه چیزی می‌خرید، دارید یکی از هوشمندانه‌ترین اختراعات قرن بیستم رو استفاده می‌کنید. اما داستان اختراع بارکد اصلاً شبیه چیزی نیست که فکرش رو می‌کنید؛ نه آزمایشگاهی، نه تیم مهندسی‌ای، فقط یه دانشجوی بی‌قرار و چندتا خط روی شن‌های ساحل!
توی این ویدئو با هم می‌ریم سراغ:
➖
اینکه بارکد اولش دایره‌ای بود
😂
و اینکه چرا تا دهه ۷۰ روی زمین موند؟
➖
لحظه‌ی اسکن شدن اولین بارکد دنیا روی یه بسته آدامس
➖
بارکد دقیقاً چطور اطلاعات رو مخفی می‌کنه
➖
چرا و چطور QR کد به‌عنوان نسخه‌ی پیشرفته‌تر بارکد متولد شد
📹
تماشا در یوتوب:
https://youtu.be/PAHA55mHLWs</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4910" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">و اینکه مدل رایگان Hy3 خیلی از Nemotron3 ultra قوی‌تره. از اون استفاده کنید</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4909" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C8uO5Z-92dCyJedeJ3zxhw1s4OHlxVzq3I8XwATYWZWgYin8TPlbw5Q7CoQa0oNg3FJ9rHhNYDBcYPMKF3orXrulOR9AnxgCgJFcbgkBJMeG-ffYE0QxXKHH5DA-GfiG-1mTWJfx7Vuhe7WX58kgknkYlcvsQhgRa9mptTymbVYIObP4M0p2aygt6UGAFoPtDE1opidAbqoxhVe1Olg5D180MNIcuPq6V3-EW5MlNuOTvjUWJXlaube9gBpFXURk5K7QEUk_BZgjT-m5vi0U1OiGp6eFNsrM0--Vt88IXezOrfskzOgygbgcMo8qE9tqmPzb_zSFUfpvblPbOLZ5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا به آیپی‌های کلودفلر حساس شده کانفیگ‌های کلودفلر رو با آیپی‌های دیگه chain proxy کنید باید درست بشه</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4908" target="_blank">📅 14:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده و فقط روی خود OpenCode در دسترسه واسه‌ی خودم احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4907" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده
و فقط روی خود OpenCode در دسترسه واسه‌ی خودم
احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4906" target="_blank">📅 23:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حالا که شماره مجازی و کارت گرفتیم، هرچی سایت api رایگان میده باید شماره چینی تایید کنی و پیامک بیاد برات
😑</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4905" target="_blank">📅 22:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RGDb27AVooVVjB0EVY5Z23xacEacb68xYr6rNmArO7hg9BZ4PV7q4S1RCttb9rtXB4QiefvhBY8qQ8B5quYUtUsy3iu7kxAWuLiUtqPz6LWLEns4Fxd0AJWMoihbpKH21iui4BcTJAjl3MGi366u83ZaR0nxaoyXskCEwfYTCJpZO1GK2aQmT83HmOU0I82rDpwKngmtzCz0TG4rqVfOLVK7n_zlflCpx8o8ht7LGVzJqRqYVY1bZpTRbPPLu64K9_JzRnIwFGJgJS8_lpdLwuEMmrwjtNY2SD-xJ4IbMAQM48V90xxW_PBza5-rIqQY-MvwiQ8w8MIDOTSczMJpkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CBVTyOwLjDzLp96LMFYwIKn_TxzedJWaG27Gu-FPa_qbYB0jYRvjk8yAxIxF3SiUhQgjzkHyuRUaCYmVAr60PWtrt8TnCyFv0XxvndoXjW2gKFUkcbkRW0fZAJOtE5IlW7rPoTl-JqOn0xuJCaGdQBNkH2rFcm0izMKEhCVgMCPl4wMCkc_VkMiPM6zytCsuZySzf6whaKiVz-f7d-e1YCxL7fKz41NOxNYxzAKSoibc-my_GzvODkEnHMS1ciaPhBzzHrDpzx_XCN3tN5fzuOSLLlNxG9UbNHIrKWUCZPQqPwgo6GWAR6sXcRPCKp1PPTqRpPj5No-9KnSnLpigWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpl_yNYbkfzPIlDqk7IwsFrViOjwt0Mn_WfvxG21S2OhPrjH0IhqDjPVOGRNlfAoLeBORHRP9IVI9vCyQpPhQZ4KTuQHxMQbNS3SF0n68e3594g0-JFLro4x9o8omt9lulpYegOTPV8EsE0n0no2TawjgtBrfJAfARcjqwiEqz3osiKOjwBxYydZLj3AarmYciT7tr2_is78I1ZO1bZbcdwfXKSAsB0yaoAVfgIQktOUTNz913K8mtxzxmKsYQVwbtF2dngE2PU8jw2pBclCQzMnf1bfCJmCpYTv8Km5Nb4VTIfYqj0ExyCjtNzA_VUr0bhUI6TTU2eO6FZqTvCAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NvJ-OYnafw6Cz27r9-8I9_lnWDOyrStwTiIshXqQrqGZsU70qu3SpuJErqfH4UXciWwLBH0dZUD0jvw_-XU6uQFDMyY5-gLNHaDCBtZhQ-OBJscsAuAR-oUPRvl1orq1-zgp0G0VDSpvg-xw2MCj8mfmN6rXPQ6WinKYU0igcV2ppWTDkCUhto0Ncs-6fb5qiNgQKR5Xltegcs-S7pz1X8AUeVb53eGMbh--PuauvCZ602ReWMekwiG3A6dBdj-m83Fu0SYeOMLf45J-n8c2YcVZZUNIiDBwaV_wPLZdm5BIM3wwZ2iOlg7zAWWmjbTKs9LT4dS2ngR_AxQiANvakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5ViJVFUpITJYJ_dfK9dFMh7Q3LL2gr1G4hlLzahizoWJDscFKzOiX3k2eZIgL0etzP7gaGnMhyVYaZ_vEa-WyDeJBpyfUAghiX0yUpbEeadkIWWoV5kyeToyFDgGUAJUniWnf3p2r1FN-4ve8IQuK14stfsJwp0_EP8E8pxHHIyfFUKokI7IO_0ASafXXjSL66SilVR_9YsDOg9t4PPDVVII4q7R1DFgTpc5Fc2P0prck3j13D0pMiwtmUiFvaxrzHPZqwyffWFiy32SD6ho5VxMvs2sHDGoquZyQyo3DOzpCf6q7JcZvSiDE1EuEl4b2brevYxCN7arJ_f523rqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E6x_RlA2uypq08n0a2HeAvramkD63ueCAsMjEpBS8O2Uw7UeZ3qcgqhxKxAJV3k57VI_RDDtYG6ve4Lx2C8i5juMlO9RSmx7gSj73MW7EIY1Ihg7f9HfUPMkYmMuTUJeOko6IKgW0XSFRxqNco7Y1KkJROQlB07FBOT0MTGEFVGHxpj3V8NzvW_xgKaOkYFsgerx5lfpoFl3-sIhKssDQGB64apv7sIk-NOg5VGMoqAIRqHy-6ezaMMkzRkxA50t-b7VQst7nUjmABA2_dWR2JZh5ZBkxLJH-xcYiFBKJVLAcrRRVl-W4BhFsclpzALijdHdu8CgpCIjFhHiKBPSjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4883" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=iygeK7ibjm1rc6l3J-zYcK28dWYg2wtp9ZgEJLTPTL2MWn_tI0TDL9sZ9Pp-9CNkUqmds5vi1kVR9Vr9_WiZhOpMW9E9jP6IB9BIUjPQAwUm7C2KLHcAFJirdgGkwaiPtdBUx7QPreCJKEX9-VF-PaFL7ZFgeM05z-FDf3HMQfDNIOMsuW1fso627-2a1H6mcX73tdrg8l48H9LykrdziBsLfzbxMBSNktpfduQG-rgOqcuxM7nOJ6FOpsgMkTLGrASyQVKifR-OuvguWstmEVYt1XgPi1ObAF9sorJk8fNhIJw9tJ7l-nLisWwEqW69-Ly_38clc3_ZnBwRIj1nqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=iygeK7ibjm1rc6l3J-zYcK28dWYg2wtp9ZgEJLTPTL2MWn_tI0TDL9sZ9Pp-9CNkUqmds5vi1kVR9Vr9_WiZhOpMW9E9jP6IB9BIUjPQAwUm7C2KLHcAFJirdgGkwaiPtdBUx7QPreCJKEX9-VF-PaFL7ZFgeM05z-FDf3HMQfDNIOMsuW1fso627-2a1H6mcX73tdrg8l48H9LykrdziBsLfzbxMBSNktpfduQG-rgOqcuxM7nOJ6FOpsgMkTLGrASyQVKifR-OuvguWstmEVYt1XgPi1ObAF9sorJk8fNhIJw9tJ7l-nLisWwEqW69-Ly_38clc3_ZnBwRIj1nqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4882" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست قابلیت های هر پیام رسانی رو داره:  - چت های شخصی و ایجاد گروه ها - تنظیمات پیشرفته پنل کاربری - پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ  نصبش ساده ست و با یک کامند انجام…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4881" target="_blank">📅 13:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZethRise</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/REJ1r1IwK8oryS3tjVv3NOdFJuHx0GMstRVEZ3Zjwa5CfYKdNmxPCsjbAQ3LgYOElZwYSSaRKrzZgzbRYt6aqo4pxZHwdopn2SysWa3VyMMmA0QGSFOMaKuKe0FNl5ANyMNNRme-tvBgNxc191BfjDYYzH_BU_5kiXqfUIqiMN-H-IJXYlCA4RiDNs4M0PyH46JIPbeBrZjclI9DX1G16Up-xMdk1RwDE0OGbwPLBHBAEXLi9DGnqUbpa1WF3p5Ff7mIOGwgfGtuegEqFakylbS3OHBhQqJ3-TZ2XjSFxeck4P7txUzmtDfGJidJuFcYvNzL4in0Yi_rxQsT_ZidpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست
قابلیت های هر پیام رسانی رو داره:
- چت های شخصی و ایجاد گروه ها
- تنظیمات پیشرفته پنل کاربری
- پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ
نصبش ساده ست و با یک کامند انجام میشه:
curl -sL https://git.diastom.xyz/ZethRise/FelFelChat/-/raw/master/install.sh | bash
و سپس با کامند
felfel
در ترمینال سرور میتونید اون رو مدیریت کنید!
درحال حاضر فلفل چت ممکنه مشکلاتی در UI داشته باشه و همچنین در backend چون نسخه اولشه (v1.0) پس اگر به مشکلی برخوردید توی ریپازیتوری issue باز کنید!
👩‍💻
Git Self-Hosted Repo
📱
X Profile
🚀
Developed By
Zeth</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4880" target="_blank">📅 13:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
امروز اومدیم با یک
#آموزش
کوتاه از کلاینت/اپلیکیشن incy
🔥
داخل ویدیو به چه چیز هایی اشاره شده؟
. ایمپورت کردن کانفیگ ها
. وصل شدن اتوماتیک
. تغییر dns داخل اپلیکیشن
. تنظیمات مربوط به تست پینگ(مشکل پینگ فیک کانفیگ ها رو رفع میکنه)
. وصل شدن به پروکسی لوکال(باگ کانکتینگ تلگرام رفع میشه با این روش)
🔛
خلاصه:در قسمت dns از quad9 مقدار گفته شده استفاده کنید،تایم اوت کانفیگ رو بالای ۶ ثانیه بزارید در صورت باگ تلگرام از قسمت پروکسی استفاده کنید.
دانلود اپلیکیشن اندروید
دانلود اپلیکیشن ios
دانلود اپلیکیشن ویندوز
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VU5DJzPEA93lZXSIX1qUkSxKZ9OoK7MTc3mpc_bsxJMyg4Xd_-QDtPu8eyCzCG21He1N1mpBWnQiDSOLdeofJTNT5GphaU0llabSNa_07o2JxSAInp2nnnbAPOCUhEwZVIxJ8lvG-hSDsKxLiYmRb1ETfd9gg3ccvPBZRQV4J7Fd1TotPIyT3LDhn9iRuZGtu6VWujo7h0MPBDtv_y4TqEDLLGr4xNsNlgRHM7592qrp7rI6b3yq-fPUA9_5QANe-tcLBzBMOVivJaqiBW6UxfMZvoCy1jcHofYagfsGKBdY1lh-8JZIWVnqcAQlfoC-bAvPRj72jUX969nP-CO08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز دوم و هوشمند برای ایجنت‌های هوش مصنوعی؛ پروژه‌ی متن‌باز Synapse
🧠
حتماً دیدید هوش مصنوعی‌ها بعد از یه مدت حرفاتون رو فراموش می‌کنن یا اطلاعات قدیمی و جدید رو با هم قاطی می‌کنن. پروژه متن‌باز سیناپس، مثل یه سیستم‌عامل حافظه‌ی طولانی‌مدت عمل می‌کنه که روی دیتابیس محلی SQLite سیستم خودتون بالا میاد. این ابزار فکت‌های مکالمات شما رو استخراج می‌کنه و فکت‌های متغیر (مثل شغل یا محل زندگی) رو به شناسه‌های مشخص وصل می‌کنه تا با تغییر اون‌ها، مقادیر جدید بدون قاطی کردن جایگزین قبلی‌ها بشن. سیناپس اطلاعات قدیمی رو کمرنگ می‌کنه، تداخل‌ها رو رفع می‌کنه و به صورت خودکار مانع ذخیره پسوردها و توکن‌ها می‌شه
👍
این پروژه به صورت سرور MCP ارائه شده؛ یعنی می‌تونید اون رو مستقیم به ابزارهایی مثل Claude Code، ادیتور Zed یا Cursor وصل کنید تا یه حافظه واقعی و تحت کنترل خودتون داشته باشید. سیستم بازیابی حافظه‌ی ساینپس ترکیبی از سرچ معنایی، متنی و فاکتورهای زمانیه که همراه با هر حافظه، یه شاخص میزان اعتماد (Trust Qualifier) هم به ایجنت می‌ده تا بدونه اون فکت چقدر معتبره.
که به نظرم یکی از مهمترین قابلیت‌هاش هست.
با سیناپس، ایجنت هوش مصنوعی شما به مرور زمان با بازخوردهاتون هوشمندتر می‌شه و تمام داده‌ها هم کاملاً آفلاین دست خودتون باقی می‌مونه
✌️
🔗
لینک ریپوزیتوری پروژه:
https://github.com/Danialsamadi/synapse
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TE78pCAnNRroWrJ3XWvbqVUWUxIZ1aq5wpaw1Zs6ZutzVQ3AAYtGfO8oIdxBsxRlOZJ1s9C9fRnIJd87EzMgOZ0Xx7UkylDf5urUY7O_pQPdG5YlrAbIbpuCsLNZGJAvKeby5sRij-Afb-BmW1tCorN_WrLqIAAcVBfpe3JE8cBapq-b123oM_ukcwTI8v1gYxs9mwcD2O17XViH5oQHGDfhD5wyvAsNioklMf646GAqOCPO3FmtyFQYLecQlqF7qhb4DX66ZEspUi1wTEjKvG6DjkwX4LmzNy9Nr7kj4QliOTa7PWpZE2ZONh3R-IIO-F8cvSzpS2R8bUOKIH1SiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OotvdxcIRz3A_pIKri3GYHssX5de7s4EezFxatvkUwNaqgbNxx15Ej9FndnUxlZjlwcQF_wTqL4Ht6uKKl0eS6U0AvgKDx00ea20XI-pQy5vrYc-c_j1bK6QefVSBp_V2shb0FV8gEvMKXurnZH8GmorqpfU1TOXa0EXz0QizBqZwtajxJvPUNgGa876Vq-7gCN5Pyjms3FtutiToVF8uo3hvzoLNpkbruNLWlLd_IynoOwWf6L1ap9Hr9VTvequ_yIFzwN9oh_37b4RodrK-cyWzXZv-7k6TNrV6-y2wXcj21nUDcMvSzMurbPJwblOmTrTbUWHGEosuu0V1ctNkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mJPBhaxZ4aoe3wH6Q1ANH_QfwDIBzvbqojyQOXg6PKZ-NKe59wryNkgP7_047K083E51bFUvZ8EKoxTfXxgKjV7paBXXY-rsEW_NjhEptdcMgKGf6zywq98ID6Bh0gyTURHNseLyOLlfWXuewJJ8n0ayieOl2G1uXBaYxqe4uLTDLoaMrHEkScHzIg2c9Ty4a2DZ7mRNsuiHoTUdz8cRB0pgZcLM4WcKr4H6itHKz88HadvhyEg2sFiAqP-wqoYWCib4g7s5SVaZ61aZKc6fNmSNfOt1o6gE13_hWpNvoZYxR35zX3MZ_xL9yxi2uYS4l14GwK7LNlQlyfxnV8eZ-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دسترسی رایگان 14 روزه به تمام مدل های zed code
ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده!
​مراحل دریافت: وارد سایت بشید تیک Free trial پلن پرو رو بزنید
zed.dev/pricing
با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
✍️
CypherDeveloper</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pMEHJWV1mFX37m706IJQjX4fMcM2kDPFyxB7cAK-UXaR2DmS5WTFBDlGDbi_MmKi8pvZjDldJcK5qZI-81fBLr4hwzfw_af9xnt4qBIH85uhTJ41_WW5b_HPBSyclnWFXPObpG8ApRPWmcZH2-maHGCmShboIA9K3sw0BuLDL06MeV0J0rwV7VAxpnD0-28UBpW9fitLr31wy0g2npX2oZa_dbizLC8C6fAiHYU3VmOZhrVbTWckg_xvXFW1OvepIMGT1HFK3k9PNBLMNxs9WLR4_wxyApl46pEfd4baH0Wj8keDEhH83w7-2V-kdIv9Zb6AvDB4t-aew0Dit1t77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=Slw8JVxD65oJQW2jalEmARtRUi4n3S4ylORIMHhrooRktez3_Co6usuvgoQljy230PdNjYuJWUIqraCpLSWnSVE0TNS3DrCKCV38FJkssvgswYAA2--juDUKdmEXWYddc7pl0sxPR5XeNI4091KJq_lqnClfI3yrmyxZKzN14EDAv7X5ducC3kEIl4yr9c9YVw6OeAPROasKIhXourLwqxqVohCQY9S7Kvx1zGShDu0w99uUeUe2UkgcJ0i1vT4zWL9OANBHZupyqjJaRR_0UafMVyBt0GEfeqi-lIOle8KT3M_POPVPzpE090-lXUll0BkIprdobLDRlbkLt4kTDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=Slw8JVxD65oJQW2jalEmARtRUi4n3S4ylORIMHhrooRktez3_Co6usuvgoQljy230PdNjYuJWUIqraCpLSWnSVE0TNS3DrCKCV38FJkssvgswYAA2--juDUKdmEXWYddc7pl0sxPR5XeNI4091KJq_lqnClfI3yrmyxZKzN14EDAv7X5ducC3kEIl4yr9c9YVw6OeAPROasKIhXourLwqxqVohCQY9S7Kvx1zGShDu0w99uUeUe2UkgcJ0i1vT4zWL9OANBHZupyqjJaRR_0UafMVyBt0GEfeqi-lIOle8KT3M_POPVPzpE090-lXUll0BkIprdobLDRlbkLt4kTDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=q6TOZhsTtFrOiY-uf9UfyLcU1i_ddf2UcQS7nRpjtBTVP8Ki4lWhNQk4OMLQtAiT_-Jt0EBsR38_PdrArCcNmDLZANAc5MwzD05o3Vm4aDzZbTjNKfBXW7zuNigLXFyMkXCg-F-JdJKa2Bn0j9ah8n5O5YxQTHzn4xAx8Jn9MGGf-f8NpZgVpXk8zScrCBaJNEcrEBDLELLMcNMf7qaNEZ_PHF0HGmaOsM5BSvxaavgJBBQskeIYkxhyJS5GbWbBvO_KIky-qYSR4xR4JK_CFggHwslzWUPFWb1pVN6MTAOofdJ9zfjkM2_7-MQivA4yOFDz7ysk12g8QBKoZYsVlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=q6TOZhsTtFrOiY-uf9UfyLcU1i_ddf2UcQS7nRpjtBTVP8Ki4lWhNQk4OMLQtAiT_-Jt0EBsR38_PdrArCcNmDLZANAc5MwzD05o3Vm4aDzZbTjNKfBXW7zuNigLXFyMkXCg-F-JdJKa2Bn0j9ah8n5O5YxQTHzn4xAx8Jn9MGGf-f8NpZgVpXk8zScrCBaJNEcrEBDLELLMcNMf7qaNEZ_PHF0HGmaOsM5BSvxaavgJBBQskeIYkxhyJS5GbWbBvO_KIky-qYSR4xR4JK_CFggHwslzWUPFWb1pVN6MTAOofdJ9zfjkM2_7-MQivA4yOFDz7ysk12g8QBKoZYsVlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eAEg9gRYeGyWL-KDPmkq0q8JdUcg8dks9ZpFBJO6MTJyaKcUSvKiShCCfwAHZaRnoF0kBsBGuT8mxVBw4sj3DFxN8Cf_QuOPNQnhETlLp3eMIt_KIDLZBIjxmB1iTK-d3UVg0d1d8GGlIj4ItwJgZzxbXKnmx1qvcxv7g78m9jXPTMySJm-pHoHUSYUVFkHaSS4WoOU8fnQ3DfMqti5XwfrpmL_mXFavj737XbNq9QNUbNYIl5liTOQYOwA1jYxazzD7IgNcDRwQezi1Ox1ns_hAwsISiIdjBXLLrIk7PhfjgjlHYEDO4Iv9rqXwADalf3emO_vomwB6ok6mRwlwMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vPaXOz01hM2ORAP59rqxUSycFt78cVPk-ByRc52ddX3R4RG8vRH29q2qaR7IuahjCBZBxesWufihzm-98-LbKps2ODfPx8Lp9aVxCCtqLH9mtWYiN85OwQss9btKQc8lV07E2Ruf331_XafcF_DGufRIyzUcpLgorZvyJf4scZh4GdGmqfL4s3_FNyLihY_rhvFiHl4Ftec_WDSNcDkVkkQLVCcUXg_W-bh4rCkiE6FByYk2TMwUAH8Ff8r0g18gsWf0HvEtxpeSGb1iUqnMyhXltlNDPQSZTThW9WYsq0_bvypRGcbtxkc9sowaf8aONLCtvFpShwdPQTFltol8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/heMUAZb0hJTTB-xgNJow7n_I6B9xrr0UfLyGefIKVyFWwfAuks9NY7l2hvSQjfEIazpOpeeF2ltPUWBgX_glwlVn0c88vRjrs9seyI9w2JsIqFDpg1E2fW7iKCdDFT_yqGfh9tIE7ReouSlnqp1vxccIJDykEOvUXNnRic0-fGJ9QCW0m7pf57q7U8gwOGXIeWOVuOuMJNguFaU1T6k8e1aNGqHMynLTAeeAZnFczj1CZDvElVwOiWG_VfGD_3iw1723Sur5yJA-B_5msifekMdAbma6lJGipqpj4-I7H9Aaag9jJGluAGrMTs-2vYX6D5LZ5bgFzWIA8lWqqW10Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q469c3055TM7XPSbs3A7ZeWSR3U80iu-QMinXUI6HHIkMuWnB4Haue_6W8a_yYx_0rS1QzTcU3h_qv99U1HmIIuCQulvzasGmpUzWA3z7ZgEzf9Ui1Wu80imCWTaYTyYdYdHixr6IsyZ8-KsXuoAaEiQCw4XZ4EIKeF0SMA8soJupzKDn0A65Oe953OTN20tERnvgbcy1PpA4TB9IAX6Pm-kKOANVCyFLyzgAWXHvWzO1to047srRq4RwvL9EBzu1td1kx5INeEDd0xOlNOkM-OKI1I47ozCIGEuXlhjmnHskm3vpyhqNo_wXckhjGlpQm1i3HwxeQPbrpgB0Zmqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ Hermes، ایجنتِ دوست‌داشتنی ما، نسخه v0.20.0 منتشر شد!
📊
این نسخه که بهش "The Herald Release" می‌گن، کلی قابلیت باحال مثل ارتباط صوتی زنده، سرچ با منبع معتبر، وب‌هووک، اتصال ایجنت به ایجنت و بهبودهای شدید پرفورمنسی داره
🩰
تغییرات و ویژگی‌های اصلی این آپدیت:
1- گفتگوی صوتی زنده (Talk to Hermes): پشتیبانی از استریم صوتی زنده با قابلیت قطع کردن حرف ایجنت (Interruption) و کلیدواژه‌ای که باهاش بیدار میشه (Wake-phrase).
🎙
2- منابع و استنادات دقیق (Cited sources): توی کارهای پژوهشی تمام ادعاها رو با منابع واقعی و مستندات و سیستم راستی‌آزمایی (Fact-check) لینک می‌کنه.
📚
3- وب‌هووک‌های خروجی (Outbound webhooks): فرستادن اطلاعات و رویدادهای چرخه‌ی حیات ایجنت به HTTP Endpoint‌های خودتون به صورت امضا شده و امن.
🔗
4- ارتباط ایجنت به ایجنت (Agent to agent): پشتیبانی از پلاگین R2A v1.0 برای شناسایی و واگذاری کارها بین ایجنت‌های مختلف.
🤖
5- سرعت به‌شدت بالاتر (Faster everywhere): سرعت لود اولین توکن (First-token) تا ۸۰٪ کاهش پیدا کرده و پرفورمنس اپ دسکتاپ به ۶۰ فریم رسیده.
⚡️
6- پلتفرم دسکتاپ: قابلیت پیش‌نمایش زنده آرتیفکت‌ها، کیت توسعه پلاگین (Plugin SDK) به همراه تسک‌بورد Kanban و پنجره دسترسی سریع به دسکتاپ اضافه شدن.
💻
7- تاییدهای هوشمند (Smart approvals): پیشنهاد تایید دستورات ترمینال بر اساس تاریخچه استفاده و قطع‌کننده هوشمند برای لوپ‌های ریجکت شدن متوالی.
🛡
8- قدرت‌نمایی در CLI: اضافه شدن ابزارهای اسکن پروژه، مهاجرت ساده و اجرای مستقیم کدهای شل.
🛠
9- هدایت بهتر ایجنت وسط اجرای کار: قابلیت اصلاح مسیر و دادن دستور به ایجنت وسط کار بدون اینکه پیشرفت قبلیش خراب بشه. نسخه‌ی قدرتمندتر Steer که داشتیمش
🧭
10- ابزارهای خودترمیم: توانایی خواندن خروجی‌های نصفه‌کاره ترمینال، تشخیص خودکار خطاها و بالا رفتن محدودیت تعداد تلاش‌ها.
🧹
11- اتصالات جدید: هماهنگی کامل با پلتفرم‌ها و مدل‌های خفن جدید مثل Buzz, GPT-5.6, Claude Opus 5, Gemini 3.1 Pro, Grok-4.5 و  Vercel AI Gateway و رفع باگ‌هایی که داشتن
12- قابلیت‌های جانبی: پسورد Vault داخلی، فشرده‌سازی خودکار سشن‌ها، لوکال عربی، فایروال و مقاوم‌سازی امنیتی روی ویندوز اضافه شدن
🌐
این دستور رو توی ترمینال بزنید، آپدیت میشه:
hermes update
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jCjeP-o8KeBIhJvMeGus2cLoy86yFWW0vS_80q4tNTfaVwZhN_7qarZMbRT3w3DqH5M0eAAdgslRx4XZBgJkJcTCLdRMX7ZBk6bhjwc8gi_BRGZ6FTiqzKLZPCPU0Q0-LdjABZJMaMf-LgXczeZ8h1pGblpqQtmG-kRJkL4WypT2xyf0Pku0MBD02de0D5fx4pIgUEhsT6FMFH4VsCF1ICWnb7682frsC8ckiIwVxm-lQdjyq9YUnDI5WuemvKJ0Q5f_cRjNQRVnhSJIY7vz5L53pH8T7su7QfyK6fSRlsL_RWJFNYkaxtmCyNdK3LzP-w-ayBH76IYtXuxCOHbg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K7ahdSt1AWCt3cijXHhtz9DfIirs82tNVsuu_KczSXrUQ9dY1kP8G0rdFVKbOLszvrgQni4-eAOyZhSaXs24eNXRE7co_Mzku3P9f55nEBNDl1Aa-2IGagH0Ma-3bb14DrKIrQJ6tGmyOzolN5KT7mu5bmRbr0dDf0TvkiA6XhW6FSNTxpNT9gLA6XTqQaXUAxPC2eSZmwz2gX3TUV_G1oGquCF1UPIaeCJa23x81I6guKJh_7rybTHylhVTW3LeieqSa9zs0jxILAQYELj2Po-Vdk4rTYzU17uSulJCZgLSyUfRxvNkQlTmuFuhx8wWF5NdMACFbBHCMSlClC8hCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OTbjk68BhZVr6oaXqFBaisqfxK6r0Iw7yaC-m5K1iZONpm03ceevmeJYrsTpPv5icOC6IhtLpI0sIxv727WdWVwVb3T6zoD8UU-k5v8eNAWBtl7GM4xqgW770JGzKIeUIZ7dYQFyt2cHGb_Hw1KDPDNNURYMFB8YSEyfEURrVFzLOD-FFtViyCQT2G21MgDjFvTXZ7X90YqF8uatr4LvrVVuHs7NPmlH4PQAowKCFtxE47XnChkcpl7-rcxgdgz0wRXuUle_efSbLxiQsXaIqzWz-MQL9lx5t-9Y6mlwKgmMdxxIC4Q0Wp51H8T4Zp6zfRSn3s_ucJnDVDVu8OjqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LsbhN0sQKvXF2ojG58-Ls2sdgqkuewBdMFL0lJKmEsxzoRUdl8ynruDNeqltudwGplmjqUzAfvHF-FnB9To4zaI723tkKoHcVBmrntQbHBIUssIbkjlbVmBQN2Ya_IZa8vTd_R04aOo57enG--mYLd0-4JfE4lws6oST-bFmCnpwU1kmYYPoUJyD5ebt9TdhJ--U380mT1CEFMEi6eaRS_FpJR4K6b9EclSGrF_GnOvdabr1kXZh4_LyxVpJgoyyaGXwbwlBTW8o2a5Kugb9X7Q0s7AdLehc6bbb0GxsSx_UuzwGpwkQGFQ6S7ton-H4PHuVEl9TkLMggUAWP-f3HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZV_6iEEvFoeMrt7p79x7aFe_q1Vu-ahFLRqa7Xw8C9-QIjauUk06vTKvXGh34WqVYqzY7VEXAKRbXjLjwuqxBEK1MHKgkZfIZif7x0SAh6XFLDY1BYg3ATN8tvGCfsWLUzV1KNyN5zx66sKrNIMsjtB10lS2wYJPZCvfLAGtYosQra4jZkvw3cbTThiurVSr3QU8uKZHSxi76pR1rMDAptEP8LIl9--rUQnY_OsVuuLM2KoZBvOtY9sUagv2CtiEAs6_qqPQYnl246JwdKJRMtzI1scaN-_7BSUHsdmQNQJwgDiYRTJEe2JM9z3zs0qTav-kyKADt8CdmoNgnoBVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OhYXUUdyk0lS-zRATyup2AyatKOMQ_se8Vzu04jvncaDOqRog8578IzO5nRzBEaW73Qv7rl6zi0YaEKyoCIa8wsnl9wAHkDjHB2vUX_34UGyzj6UnxoS3mWGqwmd-jzJ1Y_Nt4Mz6HU8guepfIEWempVLRRHxEL8Ur0OUJqLbBlHNCGXL3SNbQC9svfQcfs4rqRzSlDl2bbQwCyxikTXK1Gh2lYntHlIxuZEN6JFdIjLWTN2YD9mU7xxqhzlCyYthP0ZaEjs4unv4iZ4ulZd4cjGoXr8DdfBTxfNJj31UfXobEqEJ02DqeA0BeDyps5gT4FABZjw80ISjhbVPCrJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mBY1BoOBOvqp91aSjfarsrJNT0mKMbBHBpw3nd_9w4vp1HIn-KnNbUKhQiXWUAqHmvFVszIIHpKPAZW4QhAKoZBQV3yq6oXpNgnr-6TiNbcCIBO-hnkEVro6chQnHlTr2XlVDjIkC6nZ2GArsGOgbBjrqGSNpX2HJYYChb5dIaq3_QuhQsZAIuShZIBMkp80qIUzX7_6IdFG1HJcrXBKXy-lrlEgX_yQbtN6z9kUQ8dO4WUAcVhjTFYDO905XcZCREIRcS3YWBZuRc96WdKKfmQPqklBCHv5In1f8IzYD4z1nOKOePHLlhKX86I5rLQiEZ4FyU5XR0sap_TBjZ6NWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NzwCnIh8uvmLN65uuebUqVy0xKEVprNXPeJpf9dK8OLGuQslSs6rkHboSllxl-_hCdv0nSNYLcYC4oDRVQt0CwZkDYex0GisLmU9g64ax9TMBCXAJROBPUNpSXgPBwewic1cf-v8MplpLzPdY4BJJkZX6q9eaAgrR5S0Vf7aLydlPdPu5OWsBmPsIMqeiES1QoC46whlEByeinOTk6K0tM5iNmlrx6ftkJJeCh_-kfdWChI0r1fiXmCkapqCUS1u5IDu6n4ftRjmcrndhTuEY274AJa6k1El5sfSSbIjWJ_wmoHREXRl82053NZoInN0qBQa_6dtfKbw3TnylO98Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xu-6cocz9WjVx38hJhmDwnyYEwIoh4NLsfB-vr5IrZTrmwE5ygV-zGa3KqbN7XLX9BHH1We_XR3ACDSBAtxM2IUdP-nue44ukfO_-uE4JXzWgv6aYkEU7NyxyRogScfBmoCdpp_Xi9cyCqtwRHHIXsIbzqvGWMvof6vJxWcaO1UTtgiwn0CnFeNOuo9eP5L-oFg4UfoJgt790lpZR5R_r5BP4TiXcQ4mpeiGZIGzBTcNuqON3P-CLBGji7fwt0Rs6QTSgro-0BHxgeiFf3FVG5ANhKQQXuFCnDb4L_Gac1u8vzIVDbCYXSHAe_QoZKvEQfHYPlEZCljZTIPDdo7zrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
