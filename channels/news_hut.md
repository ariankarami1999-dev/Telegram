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
<img src="https://cdn4.telesco.pe/file/DpwU85WkkTHmIyBfLtCzPo4brBpvbgP3fZ-pkYF9o8no2I3h4w79Z23_9HDg87q2lu8aChM1QNjilYl0ez_efsZjHF1Ihq9x3BYQJIOKomEwnLg_MihA34yjV2Otzx6y_2oggQrFkyyA7yWhQRoQZwvMcjYUOLbLzQq1iIzQg7ZXoUh9WpeWiW-0awuCBklTq0iaYcX-6mqhVZd9FSs3s5GpMHqCGlaVVrODG5EeraxV4nAt-j85dwltDMa0VuREfFOXNWetRtbqRTE2843y-iEKRoKE3MVNRWIZfDARnSp7Lf9fKe14708Un0ShIr01wja48lJe99_tqrU7rTQOhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 114K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 04:27:56</div>
<hr>

<div class="tg-post" id="msg-70896">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70896" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/news_hut/70896" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70895">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DV8kNJFufhleY8y7y5jtKJXtkFDS8hddYDKc8XFePs1jtJ1whEO6aZmJWU63SeTqbEevSYES1gpTu-u8p0JtkkAPqNKF7yOmXV7zJuIfGBqjn7exFTPIABpWLEEwbi8C86_v5h1_qDpdV7dDKUUUk2CyqXL9avz4qap_XYxp9UgtcKiirunfZ22MVW6y34aRWrruR_BO820KTe4rkz5Vjna8BgKeNLa_kCjWnhaIv7G7tCz6Gu8U8OYIqeSHQTzoNjnCsxMgKhKmPcSU_eWqkIrYwJlQS5U1qd9IYOn_bwyU0BcZZLznoyKJ7QEhs0MdKGPxm5vs6iXpWB0pzx8jVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/news_hut/70895" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70894">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/news_hut/70894" target="_blank">📅 00:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70893">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):  گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است. به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/70893" target="_blank">📅 00:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70892">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0EY8wprVwSEm4vhKw117kz0dhw1J0N2qe8Hccb7_dEWQkc3Tlu7epGDCzyaMmaDHSNS4YDte2I-F3ncoDL3gB1WVaEtONlT-bO3_fSuQKz3Z9mfQOJi4llFQmPw39cI8Jm7te7UqXjbUCWzFjlLsLA1A6LCt8f4lgeeXZ221HlyeVhh-CMQDeONuDkwKjtscwMBPinNkWSbTEDaYYt6qtp8H-VQZwWmkp2Yg8goLdp5GJs2Z3OFB0Nl3K74uL0Jbcq2uz_9cS3zcOq7WoWksFQgbVvMW7nyKjf4jLzHAC1KFWIAIwGfh8AqJlC-0IkvV0uH7RY1GW7QE_01lGBIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)
:
گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است.
به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار باشند. مقامات ذی‌ربط در جریان موضوع قرار گرفته‌اند و تحقیقات در این خصوص ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/70892" target="_blank">📅 00:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70891">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=ZCMB7iB5xXvE_FZyXJyXS8zna0lKZkDB5NYuTVTj1vKvnqTDV-25p_eh5tvEJD-ERqdjw_EoXAvNlaoUtbXqsBeP6ZOVuG3eoeCmHxuzwgdjIrPi84aWtDuj9ThCsSzTM7f2_gUYgY9HYz9Hrgz0_ofjJ0E62DYlr1jZI4gsARDO7Dq53du0cKOAKyhYXWjJXqn19EdAKDAE8QdjZHC8XWyeLSyqq-BU7_omSk6fnw4TSvSSYTpsmXtAWvltHjhuIje2fAqMZmiDaO7g3TwRzrxE-atyj-Lk8cDTEznihrEWKdVXBbY_Ui9JRpcL0qoctHe7MwyZ15rzKJ9yjYPgu4cwkC0_xeJO98ilUC-6nAhO4nFim4ri9Qglniszue9W85BaUDSDFBp55rbsG7wzXOtUnF2riTDRnxb2EcbN-Cxw5O6Ga68jufXxjy5FdE_RXD3om-kdJ3uE611roh49pOSsY2PhbvWnjUmoMxriSEFrdXWcD7fo9_Otj8YC5SNVeYR2upe_bhrstHzmb099vxsM4IVxN8gra1-t8_w0K_2wpuh2sb9AtosvfAmiGgDWwCr99ktsB4kxfBJ1uNq6KXsLRIKmgN8BUj2BeK4T3-Lh9M923oLYZLQ3FyHsf75SZ9hmjHSDj8zlSohqcE5y2sy-1fcOxrPdj3grggB47hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=ZCMB7iB5xXvE_FZyXJyXS8zna0lKZkDB5NYuTVTj1vKvnqTDV-25p_eh5tvEJD-ERqdjw_EoXAvNlaoUtbXqsBeP6ZOVuG3eoeCmHxuzwgdjIrPi84aWtDuj9ThCsSzTM7f2_gUYgY9HYz9Hrgz0_ofjJ0E62DYlr1jZI4gsARDO7Dq53du0cKOAKyhYXWjJXqn19EdAKDAE8QdjZHC8XWyeLSyqq-BU7_omSk6fnw4TSvSSYTpsmXtAWvltHjhuIje2fAqMZmiDaO7g3TwRzrxE-atyj-Lk8cDTEznihrEWKdVXBbY_Ui9JRpcL0qoctHe7MwyZ15rzKJ9yjYPgu4cwkC0_xeJO98ilUC-6nAhO4nFim4ri9Qglniszue9W85BaUDSDFBp55rbsG7wzXOtUnF2riTDRnxb2EcbN-Cxw5O6Ga68jufXxjy5FdE_RXD3om-kdJ3uE611roh49pOSsY2PhbvWnjUmoMxriSEFrdXWcD7fo9_Otj8YC5SNVeYR2upe_bhrstHzmb099vxsM4IVxN8gra1-t8_w0K_2wpuh2sb9AtosvfAmiGgDWwCr99ktsB4kxfBJ1uNq6KXsLRIKmgN8BUj2BeK4T3-Lh9M923oLYZLQ3FyHsf75SZ9hmjHSDj8zlSohqcE5y2sy-1fcOxrPdj3grggB47hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی دانسته‌اید؟
🇺🇸
ترامپ:
من هرگز چنین حرفی نمی‌زنم، اما پاسخ «بله» است. هیچ دلیلی برای آن وجود ندارد. چه سوال احمقانه‌ای. آن‌ها از نظر نظامی کاملاً شکست خورده‌اند.
من آن‌ها را شکست داده‌ام، آن‌وقت باید علاوه بر آن از سلاح هسته‌ای هم استفاده کنم؟ چه سوال احمقانه‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/70891" target="_blank">📅 23:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70890">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=Bndr2fGlvKupq5ucyy8geCuubA10yNfyW_dryQvVz_SzZZO6Bzm6ZUvgcygsq2LtAk18HDypg2_sHZTvLIOvc1bhPFQw_osIAFTxGerslDXOri-DAMHEF1gevS-cWoQ9EOtBUXNO-mUG3ETPlC1QC5BK34WaMhJzWdBO7ks-4U4idbnLo7P55nOx51OlkXLD-myJjYKKU8o8RlrpR8obafrm-MhOaLV0uO5mQpH4Xutv7Mxi1N2LdeReVAKdJRFtAI5UkTm9z8nRPYXfcaEXuZpMrm1QrL1Z1K-94Fm4xafwtuL9Q_X7cW6fulDvFCb0T8NC3okiVc-LwIsI4V1FcIGmg_1OIPQ1KJBYiF8DUZGD1PQ9GyYc3B0h-R2aLUm1DyNM8K7aNSzc_eTvwBmbUamwjRjckbWLeE7Tg13a_USfhrjR5Pt5uAdaEmY-m2A7_YJ-ajn1sCks5AeU1ELL8LNaUA9DBySamL9wNqQwmE96m_N8cJLe4AXmknlMYueMGnINdwSIPvfpNFCpt6hAmY92g1uL7kM1Wj8RhK3ex_kb4m7cQth_9tRbHf_iokSrAjGLph0W5FJY-QfNDLzSnM21LOHwLcKH0SlaVLwQ2u4DFt3dzBFCfkfEN8AJbvKsZ8ZzZM6YtVFeM3P7B_2RXHRXjzXUmc_JSRLpd8DGyUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=Bndr2fGlvKupq5ucyy8geCuubA10yNfyW_dryQvVz_SzZZO6Bzm6ZUvgcygsq2LtAk18HDypg2_sHZTvLIOvc1bhPFQw_osIAFTxGerslDXOri-DAMHEF1gevS-cWoQ9EOtBUXNO-mUG3ETPlC1QC5BK34WaMhJzWdBO7ks-4U4idbnLo7P55nOx51OlkXLD-myJjYKKU8o8RlrpR8obafrm-MhOaLV0uO5mQpH4Xutv7Mxi1N2LdeReVAKdJRFtAI5UkTm9z8nRPYXfcaEXuZpMrm1QrL1Z1K-94Fm4xafwtuL9Q_X7cW6fulDvFCb0T8NC3okiVc-LwIsI4V1FcIGmg_1OIPQ1KJBYiF8DUZGD1PQ9GyYc3B0h-R2aLUm1DyNM8K7aNSzc_eTvwBmbUamwjRjckbWLeE7Tg13a_USfhrjR5Pt5uAdaEmY-m2A7_YJ-ajn1sCks5AeU1ELL8LNaUA9DBySamL9wNqQwmE96m_N8cJLe4AXmknlMYueMGnINdwSIPvfpNFCpt6hAmY92g1uL7kM1Wj8RhK3ex_kb4m7cQth_9tRbHf_iokSrAjGLph0W5FJY-QfNDLzSnM21LOHwLcKH0SlaVLwQ2u4DFt3dzBFCfkfEN8AJbvKsZ8ZzZM6YtVFeM3P7B_2RXHRXjzXUmc_JSRLpd8DGyUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شرایط وحشتناک بازار با قیمت بالای دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70890" target="_blank">📅 23:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70888">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iReVn0kQpskLd4lTn6-KTipo7l2DHElOjd2TZCUHG1bLq33nIumKd-cXAGnhGlnC5qrzUU33N3ib-lxryX_2nm7ChFllmtadMquolYa4zZtSs-gje1_vzcI7aJAiBifTZ-vsNkHGktn7cv5hu8Jy2tttVOezRXyzFjZzSuNruFmlQu8oge61Wux8_pqRInEA0UMNmoSzbNOEkrKT_1upLCgc1leNjb-oFneb-_1HYmWCk9Tc3o1QZrb-KPHchJyTo-Ni5hL_2_fDyXO9Xj3tZqsp34_1kZ3-YwmTdi2E3XjfHBHg95YtbI4W9IKDVe8e19WI35lt8udXKrXdl43TdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6D5TEsFe5wHRJhkmjKrgIoNBD7G4x2vGICKds-WBPbkeniNRtsEVJdxycmge4tRMKlxwNxlWZlx4cgq6YmlNFUlygepAjc79mCai7dwVvBM1umiem1VjF_WM74s8oehNaeypMJ1qFKk5wNCLr0KCfRsnD3eQ5bTndQVA1IczxC_whHI1bR_V1V-ihAOJ9dwtqewgvM47wg2PoVapmn7l00_h1IS0HV5enGbCdcpoFYI-jkR7weXy_9zeSbIUxKS2kAkUuHQHsD3sPdtqo_yGKYmN1_LYFZHLBYZTfebmh4fnfRvfObVwykE2wu2KMosNvAr0AT31rSeJEr9EmxXYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سلنا گومز و همسرش:
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/70888" target="_blank">📅 23:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70887">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=SU_eXnnawLJ3u898lf8zsZ-OgZUrQzHjx3oxCzBzzrdr-YuG_2P6AT-BkwaVGnbHeRDrbMc7t1L1HUq2yW3-k_3lwztGWuOwtESYaxvK6ijnfWY7qgjWuu7U_-AaA7LzsVFiTVf6gqKgI-PXssoxsF9avg1blvrlGCG0b1SF3dp-lL8UQ7Gei7LF029zZkqjcR8_HNOcFDdrZQBACSMFFa_zjXs3pmcHQeXlkJ88DfJxYbNmuM7A9CEmji_7AJV1G-0MuBnEibkMRwyQigzOaAL2rLbELF6rShb6U1UnCbOZgf9RU2ENtn-LCY3ZOkr_2ilEOx6XeCX7AeJU40EqZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=SU_eXnnawLJ3u898lf8zsZ-OgZUrQzHjx3oxCzBzzrdr-YuG_2P6AT-BkwaVGnbHeRDrbMc7t1L1HUq2yW3-k_3lwztGWuOwtESYaxvK6ijnfWY7qgjWuu7U_-AaA7LzsVFiTVf6gqKgI-PXssoxsF9avg1blvrlGCG0b1SF3dp-lL8UQ7Gei7LF029zZkqjcR8_HNOcFDdrZQBACSMFFa_zjXs3pmcHQeXlkJ88DfJxYbNmuM7A9CEmji_7AJV1G-0MuBnEibkMRwyQigzOaAL2rLbELF6rShb6U1UnCbOZgf9RU2ENtn-LCY3ZOkr_2ilEOx6XeCX7AeJU40EqZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنسرت محسن نامجو در پاریس، ۷ آذر ۱۳۹۱
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70887" target="_blank">📅 22:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70886">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=UTEGLMQB4Gj__qZNYFIyvhmzVtRokTvPWr_MfsIq7nC4fSjeIlULv-RrfhIpoiJjXcW0sdEeR-Go8jcpdfdwlleYZB6dj7on8PxeROx8eI7hsSdJoFdAGbZaiy42EjWDDeOqL9476RhNj5PI-45WriHCCykEb63N58ORqDGEyOl1fTfzRaQ4k83yODua98zRjoziHdh4a1EroCGbrlgOSaox3LHNmeExZNNB4GH4Jwm5DQYaoyHYeIL82ESdzxp2t_rU2Dk-4p3__Ok11Yfv82SFigaKNHVvXZ9n1GCQTYH1dFi5e1gRVsQe_RIhgCKGdIlbFJZibcYtHmfGsDL8_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=UTEGLMQB4Gj__qZNYFIyvhmzVtRokTvPWr_MfsIq7nC4fSjeIlULv-RrfhIpoiJjXcW0sdEeR-Go8jcpdfdwlleYZB6dj7on8PxeROx8eI7hsSdJoFdAGbZaiy42EjWDDeOqL9476RhNj5PI-45WriHCCykEb63N58ORqDGEyOl1fTfzRaQ4k83yODua98zRjoziHdh4a1EroCGbrlgOSaox3LHNmeExZNNB4GH4Jwm5DQYaoyHYeIL82ESdzxp2t_rU2Dk-4p3__Ok11Yfv82SFigaKNHVvXZ9n1GCQTYH1dFi5e1gRVsQe_RIhgCKGdIlbFJZibcYtHmfGsDL8_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای بدل ایرانی آنجلینا جولی:
تا حالا یک دفعه هیچکی دست رد رو به من نزده.
به هر مردی میگم با من ازدواج بکن نه نمیاره.
از هر جای دنیا باشه سریع خودشو میرسونه پیش من.
بعد دوستام میگن تو مهره مار داری دعانویست رو بده به ما.
علتی که اون هم قبول میکرد این بود که چون من شبیه آنجلینا جولی بودم، او میخواست این وجود رو در کنار خودش داشته باشه که مثلا مهمونی میره، پیش دوستاش میره پز بده.
من حتی بیماری‌های مشترک با خانم آنجلینا جولی دارم. هم قلشون هستم. ما ژنتیکمون مثل همه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70886" target="_blank">📅 21:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70885">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
📰
اکسیوس:
ترامپ طرحی را برای حملات محدود علیه ایران در نزدیکی تنگه هرمز بررسی کرد.
وزیر جنگ از طرح «حملات محدود» علیه ایران که ترامپ در حال بررسی آن است، حمایت می‌کند.
طرح «حملات محدود آمریکا» علیه ایران هنوز تصویب نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70885" target="_blank">📅 20:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70884">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⏺
🚀
فارس:انهدام یک فروند پهپاد MQ9 در شرق تنگه هرمز
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70884" target="_blank">📅 19:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70883">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f517057c.mp4?token=wBtnk8YviofleUf8iUMB_5EhpsROtRzHeXWWBKM5MgLs02_9hYg0xmaKnzZx0h11NKL9LHdifBiZIFQgdE4HghAP9LodAJNtVqatZz4C776nRdCKba5UYV-ynsZNaLlG81u8XljAh8x7E-JBJZqepfkCUQOdKAYFAYf1akqkgJ2W1EoUoVsq4JSyR-Ie5sZm6uMV95uXN3nkrjZ_ztAzHWpOcQHinBcq4OP-1foa9zpFMJBZa18mEdHbDLjXdkzY-4LkIpRY62V3Dcjqf9kOkREAg_D-Wl_cXAPWrRjfyM3518QJNBwWH88R2OCBhfZH0o0LzIG0mMrkqo1tMvinzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f517057c.mp4?token=wBtnk8YviofleUf8iUMB_5EhpsROtRzHeXWWBKM5MgLs02_9hYg0xmaKnzZx0h11NKL9LHdifBiZIFQgdE4HghAP9LodAJNtVqatZz4C776nRdCKba5UYV-ynsZNaLlG81u8XljAh8x7E-JBJZqepfkCUQOdKAYFAYf1akqkgJ2W1EoUoVsq4JSyR-Ie5sZm6uMV95uXN3nkrjZ_ztAzHWpOcQHinBcq4OP-1foa9zpFMJBZa18mEdHbDLjXdkzY-4LkIpRY62V3Dcjqf9kOkREAg_D-Wl_cXAPWrRjfyM3518QJNBwWH88R2OCBhfZH0o0LzIG0mMrkqo1tMvinzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
فرزانه صادق وزیر راه:
به علت از بین رفتن زیرساخت‌ها هواپیما بدون رادار هدایت می‌شوند و تعداد پروازها کمتر شده است
👌
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70883" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70882">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇦🇷
پست جدید لئو مسی از خاطراتی که واسه تیم ملی آرژانتین ساخت
🩵
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70882" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70881">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70881" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
http://TrexBet.com</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70881" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70880">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyZ7_Fhg2OBUZNVbg9B4uBtUt9TPf2MMdWyQJkoWEGijH3KpuViHC563AMjWZqFThl4FLHJlNIM5bkvpZYf-smbGD4YjIz_jcmqMfO9rNJ1jKcTuWrUorZNIBSU788STm0ZsIfEv1qD_V0LXbIEDBS-sYiQA2gXRu4Gd9eNeX-v0L91pzzGqcI6_9eGpUDDh9vasKgvk7QxUMYO-1gmuF4GzQ1GoEoOAcGfvvq_guEENZG-ALir4Nf88YIqs1kiJMgoCO0-YjVa1__POC2wWstxn4BtZ3WGlW81QCoX4esql4vO1kj69pkososmBpUrarOGE428hrb-pWGWzZNF5Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
میکس پیشنهادی ضریب
〰️
برای بچه‌های
TrexBet
🦖
Code TrexBet:
SKCU6
آموزش استفاده از کد شرط در سایت بین المللی تیرکس بت</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70880" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70879">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8uCQ53S67N_UCgJOQ0DsnC8rbFhp0EDfT5RHWOjGOjqCpvqqxpLPHvteQboZf6cgjaMzo-0bthUmV4RUxYiy-fnlsr9pQt6PKOTdc9fojpv1Jn7u4mKwZijQN__6bVflbW3EASU2MUMvmQ5x8VTeiLVT_1JdhtggfcJicjTnBTPgQSji6mMD1iQU6qFaNtDtb2vIvHpWfuHu_daSumNJSGoR36jH2q45H8A7yeYjBbPdE5HzTPeWazi8YaTrOlXlP43ZKeio1iQtAXVwWeUyhDSwStrTH7JiKX1t0SVeGm0j8P5OUaiewAm9kAwWRJ9ze_ViZwyxlB8qEYyINvy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💋
#فوری
؛لیونل مسی اسطوره فوتبال جهان از تیم ملی آرژانتین خداحافظی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70879" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70878">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=jTcPALFHQKmgC8xKM0gjnJ0FBRgA7DHMx5Qr7-7ONyLU9D0XDUQTmSdC1UhhW1CW0KknP9nmlcYmTljSfcJIp736NEn5iDKKkzH2afZC0-iE_Yddx_aV0eVsj5yZqm8f8M2V6G8swIsApJEl-7-RThc5otDv8k2VEUxcHePPUVFM_iqHjVI6OasdDBn1TGUE9dzLmcBWKi4gQu9Pq5pR16HQQ-oGksPyIaGwX0BwDWgnHpxbKAGbO84tzqYFTrZ-B8y2M0Gp8eaJu0nTBrMkxuVUD50IoEijLQOefpnhneRTbrKYD_mQ35EXfo8pXHzVeOQk-aitgzL7Hn7Z4JB2hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=jTcPALFHQKmgC8xKM0gjnJ0FBRgA7DHMx5Qr7-7ONyLU9D0XDUQTmSdC1UhhW1CW0KknP9nmlcYmTljSfcJIp736NEn5iDKKkzH2afZC0-iE_Yddx_aV0eVsj5yZqm8f8M2V6G8swIsApJEl-7-RThc5otDv8k2VEUxcHePPUVFM_iqHjVI6OasdDBn1TGUE9dzLmcBWKi4gQu9Pq5pR16HQQ-oGksPyIaGwX0BwDWgnHpxbKAGbO84tzqYFTrZ-B8y2M0Gp8eaJu0nTBrMkxuVUD50IoEijLQOefpnhneRTbrKYD_mQ35EXfo8pXHzVeOQk-aitgzL7Hn7Z4JB2hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدرضا نقدی:
ما انتظار پیروزی را داشتیم، زیرا به وعده و یاری خداوند یقین و اطمینان داشتیم.
اما انتظار نداشتیم که پیروزی به این آسانی به دست آید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70878" target="_blank">📅 18:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70877">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=iLvM0IlrdilUfxcOoMHe5NJUVSQvfMi0DgU-kDL_hVmgJ1nMxUtQwgnbSSpHUtM7CgVKJ2xnIJTgo6izy8asFpQ8qk9QTp8yhebf__Mm7vgrO8aHKyYSnpzHDhr5ztZnXcPGIlXriNFsRpZsrfztKYMEPWuKo8UElh3bTWgq-ZpUJkgkUWBd2NgdTw4736oxiik634toLfDtwRXmTizE_P2HhVW8dxSHA3O66fIH0zrbgXbNuE_Z9UkwEo__wS9Jk9rrN6W3wWF71UXsvy6965RG4PNXmR6Woe7wxCLB9_ZWgCZ7lrHsRPuLpaG0bHPYoftFprudDQUcSQgCDUKHMoikgNsI3hX8wrCa4jUPSKQFjlZFwOUDKjTWXurnIJVlawp21ZJvZl5mYtFOaBss55x74UDPk2dWMtOD1DltSK9DRujtU_deH9eyfCDBsFipgxJjbz9yp3DfW5Al0IL1u3pmv4MlGHqLthaHDTuab4kQRE4MFQc8QRL28aIEPlbKrCmbDEUEpI1iUkt1oOdiutfcbLP-PIE4LXPjphpm5mNZ1fedHFmsvfnNDUiRLhuq-hjPTvGHzsN3NJL3YrfYQXp77Aw_wORo1KiiDyFeOEjrIvYkogmRS4RguEe2AjShBaeOQiSPD2jXvS5yHEuzhfJUtnLVoWDQCx7VZZ1YyPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=iLvM0IlrdilUfxcOoMHe5NJUVSQvfMi0DgU-kDL_hVmgJ1nMxUtQwgnbSSpHUtM7CgVKJ2xnIJTgo6izy8asFpQ8qk9QTp8yhebf__Mm7vgrO8aHKyYSnpzHDhr5ztZnXcPGIlXriNFsRpZsrfztKYMEPWuKo8UElh3bTWgq-ZpUJkgkUWBd2NgdTw4736oxiik634toLfDtwRXmTizE_P2HhVW8dxSHA3O66fIH0zrbgXbNuE_Z9UkwEo__wS9Jk9rrN6W3wWF71UXsvy6965RG4PNXmR6Woe7wxCLB9_ZWgCZ7lrHsRPuLpaG0bHPYoftFprudDQUcSQgCDUKHMoikgNsI3hX8wrCa4jUPSKQFjlZFwOUDKjTWXurnIJVlawp21ZJvZl5mYtFOaBss55x74UDPk2dWMtOD1DltSK9DRujtU_deH9eyfCDBsFipgxJjbz9yp3DfW5Al0IL1u3pmv4MlGHqLthaHDTuab4kQRE4MFQc8QRL28aIEPlbKrCmbDEUEpI1iUkt1oOdiutfcbLP-PIE4LXPjphpm5mNZ1fedHFmsvfnNDUiRLhuq-hjPTvGHzsN3NJL3YrfYQXp77Aw_wORo1KiiDyFeOEjrIvYkogmRS4RguEe2AjShBaeOQiSPD2jXvS5yHEuzhfJUtnLVoWDQCx7VZZ1YyPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمدرضا نقدی:
همه فوتبالیست‌ها با توپی بازی می‌کنند که طبق استانداردهای یکسانی ساخته شده است، اما همه آن‌ها رونالدو نیستند.
گل زدن نیازمند فردی با انگیزه، هوش و توانایی است؛ کسی که بداند چگونه از آن ابزار استفاده کند.
آمریکایی‌ها صد برابر ما سلاح در اختیار دارند و از موشک‌ها و پهپادهای بهتری برخوردارند، اما نمی‌توانند به‌طور مؤثر از آن‌ها استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70877" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70876">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=Ib33fc2xl3uSMWgDsHsvCtj6w_nGctCnGBcrVqxKEm0l420G5DTweR4nsRD3NWGcTOufnIYi2hEocsMGodh-HhuRY0lAxGda8bxbiC4n1LCfB4nq3_nxfeWNaqwtEqgMwVns70QksouXs1LyQs5btH_ktN9GH-xB_Feu1vWxkbdPm_5NYRhc6nW0pdNh4jbDa-jWCRWQOccgWX4hyNvRBBJE0xLRVHOeCU2sF61lzgnA1mrFQBKUUP3Ckhx_sMZEKuuvdK2er-wM4f1yHCyJkrHnkyJqmPZadqGlIHN-8xnGALOQc3i1UyG-QOZR7Q5W6pawUXuWKZ29Ptn-THUJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=Ib33fc2xl3uSMWgDsHsvCtj6w_nGctCnGBcrVqxKEm0l420G5DTweR4nsRD3NWGcTOufnIYi2hEocsMGodh-HhuRY0lAxGda8bxbiC4n1LCfB4nq3_nxfeWNaqwtEqgMwVns70QksouXs1LyQs5btH_ktN9GH-xB_Feu1vWxkbdPm_5NYRhc6nW0pdNh4jbDa-jWCRWQOccgWX4hyNvRBBJE0xLRVHOeCU2sF61lzgnA1mrFQBKUUP3Ckhx_sMZEKuuvdK2er-wM4f1yHCyJkrHnkyJqmPZadqGlIHN-8xnGALOQc3i1UyG-QOZR7Q5W6pawUXuWKZ29Ptn-THUJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماموران نیروی انتظامی روز دوشنبه ۹ شهریور ۱۴۰۵، به سمت کارگران معترض به استخدام‌های رانتی در پالایشگاه لیشتر گچساران تیراندازی کردند.
در این تیراندازی چند معترض زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70876" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70875">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYsKIidGnlX60TMUCjMihwZSc0cSMFSRzt4pS4SEZ6ZgM2Q-D5VJixx2borUrCujyGbn7d_oayPAIW8KSz5YSUmUsfcYtUWU4ZuRS0_CKTTAu3loO7Zhp1uy6bV3zP0cG5GndOUgM-pe8ScUfl6NBn03ibPixq3FNnfadMuYSaaIgyHUGSuvYx7zQGh5oWJLhoyZpMacb9mP-Sa98n7BxzvhHIbxW0KvW8GJFUfUxgKXinJJ4-UeBUqWR295E-DPZKP6KvtuK1NYKSnj1sBOYqFJQLJ3irh_Ld3IEf53yMeoH7g0PxoHFxQqr8M7AmwBJkNqn_QMelgxqpkSfus4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضع خیلی قاراشمیش (یاغی)
وزارت نیرو اومده هشدار داده که مردم بنزین و گازوئیل غیرمجاز تو خونه، زیرزمین یا حیاط انبار نکنن، چون خطر آتش‌سوزی و انفجار داره و ممکنه با افزایش قیمت سوخت بیشتر بشه این کار.
گفته فقط اگه واقعاً لازم بود، مقدار خیلی کم و استاندارد با رعایت کامل ایمنی نگه دارین و موارد مشکوک رو به ۱۲۵ یا نیروهای انتظامی خبر بدین.
خلاصه مواظب جون و مال خودتون و همسایه‌ها باشین، این کارا خطرناکه و به نفع کسی نیست.
@Moris_news</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/70875" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70874">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237073d371.mp4?token=sKPxXUhkNoYkYVnvTqOprXIm6MTCGGVbmhXsK6k5WoG9_gAmLzpD3NJ5DLOt5kZLeUFhWMEwCrt1084rlIvfABJqjkG6jUs6bc3do1ecwDmrGJsOgO1jtYBuAS4KXx1Y3mwGN6J3qmVIFhAwMaoFxgXf6xjgpP9yyv-DnMWhLdWpymhDS8Q9TkJRRZnnVSixLPC_0o-pnFoTPTfDExvZ0BZgT8tOf1d415NsZV7sv4En4ERe1sbBlTcj1TptaBgf6x2Q9zMDULNf7p4Rj94H_BbLZ0wsJV0U5MWEmIb_HtHKioNn6wmXNcCiQzmqWAgtPs19Vf10Zj4BfobhXn7Gmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237073d371.mp4?token=sKPxXUhkNoYkYVnvTqOprXIm6MTCGGVbmhXsK6k5WoG9_gAmLzpD3NJ5DLOt5kZLeUFhWMEwCrt1084rlIvfABJqjkG6jUs6bc3do1ecwDmrGJsOgO1jtYBuAS4KXx1Y3mwGN6J3qmVIFhAwMaoFxgXf6xjgpP9yyv-DnMWhLdWpymhDS8Q9TkJRRZnnVSixLPC_0o-pnFoTPTfDExvZ0BZgT8tOf1d415NsZV7sv4En4ERe1sbBlTcj1TptaBgf6x2Q9zMDULNf7p4Rj94H_BbLZ0wsJV0U5MWEmIb_HtHKioNn6wmXNcCiQzmqWAgtPs19Vf10Zj4BfobhXn7Gmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری دختر اکیپی قرار دعوا گذاشتن پسرا هم دوره کردن و تشویقشون میکنن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70874" target="_blank">📅 18:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70873">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f793f615.mp4?token=MW-PZfV_gGbL1b7VaxSETmgLkvhhRyTdXjTOeH-WiEAPz7vtEOyqNOulldmxzh1R8MtDkiKxApgvqcKwVOCIDlBAqdTDeqDsEwkUqxJ9-lwDj4vcznLypEYRVu7hfBSu3rQq-yKHihKLa2Nz81DECt1M2c_4e_Jgwz0znQ2cIvFeJUylZrPHdox93bAHgpZTQDfaSt6FytyZp4tcS0ODF_KwbxVONtgmyCUIfGV3EMa0pnFXwBwJgQHMPEKm5fQ1TPzkep7p-gvpqTSH-7QITR-fFYtse8myocS5dR8f75z7DFWpQPvisURp1UA7K7H3wQYvbtzXh1gAGM2RfWIKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f793f615.mp4?token=MW-PZfV_gGbL1b7VaxSETmgLkvhhRyTdXjTOeH-WiEAPz7vtEOyqNOulldmxzh1R8MtDkiKxApgvqcKwVOCIDlBAqdTDeqDsEwkUqxJ9-lwDj4vcznLypEYRVu7hfBSu3rQq-yKHihKLa2Nz81DECt1M2c_4e_Jgwz0znQ2cIvFeJUylZrPHdox93bAHgpZTQDfaSt6FytyZp4tcS0ODF_KwbxVONtgmyCUIfGV3EMa0pnFXwBwJgQHMPEKm5fQ1TPzkep7p-gvpqTSH-7QITR-fFYtse8myocS5dR8f75z7DFWpQPvisURp1UA7K7H3wQYvbtzXh1gAGM2RfWIKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت وزیر خزانه‌داری آمریکا:
می‌خواهم از اتحادیه اروپا و بانک مرکزی اروپا به خاطر بیانیه قوی‌شان در حمایت از اقدامات اقتصادی ما علیه رژیم ایران تشکر کنم.
و این گروه با هم، به این حکومت وحشتناک چهل‌وهفت‌ساله آن‌ها پایان خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70873" target="_blank">📅 17:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70872">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0baed51151.mp4?token=BhnEobZvrVNR4_wpZ_vAu5ND6bsKSCjSEzbCErigIQH1GCHOkf3XWJuqKJAkBH0-Gw0LV8p_SC4XmoUPELe14HWLbp7ehjrwt0QWziz2zr8LCRY-m_4t4jq63UorEqBW4iSsEPIvmLi6TAU813QToGt2ueLJ25Ytmw_P299urL1mcGZp1peuS8foF0EW7y5BMbsWU3Xgy_woc4pwcP7Za9b_cJID3RpvdiTulF8CQ_EXRNmBy83e5jcDLhuCWG1jpCzL0Qq8LsmJgmEfApSvMR_OQ42LKC9i4wFq9FshhYano4TXVCYfvvWw8FJL81Ujel_5y_9COlzibFlHiYnJig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0baed51151.mp4?token=BhnEobZvrVNR4_wpZ_vAu5ND6bsKSCjSEzbCErigIQH1GCHOkf3XWJuqKJAkBH0-Gw0LV8p_SC4XmoUPELe14HWLbp7ehjrwt0QWziz2zr8LCRY-m_4t4jq63UorEqBW4iSsEPIvmLi6TAU813QToGt2ueLJ25Ytmw_P299urL1mcGZp1peuS8foF0EW7y5BMbsWU3Xgy_woc4pwcP7Za9b_cJID3RpvdiTulF8CQ_EXRNmBy83e5jcDLhuCWG1jpCzL0Qq8LsmJgmEfApSvMR_OQ42LKC9i4wFq9FshhYano4TXVCYfvvWw8FJL81Ujel_5y_9COlzibFlHiYnJig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس‌نیوز به نقل از ترامپ:
همین الان با رئیس‌جمهور ترامپ صحبت کردم؛ او به فاکس‌نیوز گفت که ایالات متحده به حمله ایران به نیروهای آمریکایی در اردن — که دیشب رخ داد — پاسخ خواهد داد.
رئیس‌جمهور گفت: «ما ضربه سختی به آن‌ها خواهیم زد. پاسخی در کار خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70872" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70871">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puq4Sy8Obe_gPR842Y40_eKzhnCqPViJplqZVjYAEmiXA-c1WTVp2ljft75JOvbaMDqlHe0PSvcRUvW7dsBieNmIHXWD6HdLq2gd5kL2YKma1uFr7QdnWex9vJe-4Qh95re62N5P7jZf1Z6jsOvFDzqtiJaOqBmeVfA242w_JMMltkxQ1hmT3JvSqxEEAQmHQbkWb3mlWNCcwaoLInPoaS76FgQMwHO51fZKml72IUa4ZNS7dPqjdyX3WeEuLPLeGgylKbNNJOLnw1ZwA6s7EnLEpITh-WQdUxU1Cyy46rrntkcfYU7W5cf4X1pZpMpeDhgqEGvNBd55hU0HoLyzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:ایران رسماً یک کشور شکست‌خورده است. کارش تمام است!
آن‌ها نه نیروی دریایی دارند، نه نیروی هوایی و نه پول ملی؛ حقوق سربازان یا نیروهای پلیس خود را نمی‌پردازند، نرخ تورم به ۳۰۰ درصد رسیده و رهبری‌شان دچار آشفتگی کامل است و توانایی نمایندگی شایسته کشور را ندارد.
تنها چیزی که دارند «اخبار جعلی» (از سوی آمریکا)، تمایل به کشتار معترضانشان (که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است؛ آن‌ها باید به جرم جنایات جنگی علیه بشریت محاکمه شوند!) و البته ردیفی از «چرندیات» است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70871" target="_blank">📅 17:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70870">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا بدونید شما اگه عاشق ترین فرد دنیام باشی بعد از حدود دوسال هیجان رابطتتون میاد پایین بعد از رابطتتون تکلیف مشخص میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70870" target="_blank">📅 17:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70869">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=vDTrSWnaah40hhmMKX1TPatA4F2XPPl1ZQbbhFxZmom50qwFTW0x05nTDGVgozfUaiyr3EuyRwWU7pVPw_nnA9geU9pIleDhGshTLNMYbWGT3RCTXoANOe-tvHbZ8YUt9SGmNVOrhEL0yJWmRxNPYCXtODr_gNRaOwEWXUji1aYGgRkOhEmTIBMYSYQG-djxtBPYKe9kPhaBrNQ8oVVXGOCb4dKIyXkOEWW9d1X-npzXMI_2tam3KlCog47J-NWyqMqn-XGXyUMrmmplHnbNndPEszTj7PTTcdh1sFxeZLTNxe4kMcAQEEBkyZy7YyICVPNg98Cf9OsPeaW4qCqFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=vDTrSWnaah40hhmMKX1TPatA4F2XPPl1ZQbbhFxZmom50qwFTW0x05nTDGVgozfUaiyr3EuyRwWU7pVPw_nnA9geU9pIleDhGshTLNMYbWGT3RCTXoANOe-tvHbZ8YUt9SGmNVOrhEL0yJWmRxNPYCXtODr_gNRaOwEWXUji1aYGgRkOhEmTIBMYSYQG-djxtBPYKe9kPhaBrNQ8oVVXGOCb4dKIyXkOEWW9d1X-npzXMI_2tam3KlCog47J-NWyqMqn-XGXyUMrmmplHnbNndPEszTj7PTTcdh1sFxeZLTNxe4kMcAQEEBkyZy7YyICVPNg98Cf9OsPeaW4qCqFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کاظم غریب‌آبادی، معاون وزیر امور خارجه:
این اقدامات تجاوزکارانه با پاسخی مناسب مواجه خواهد شد.
حضور بیگانگان باید از این منطقه حذف شود و آن‌ها باید درس‌های جدی بیاموزند تا دیگر دست به تجاوز علیه کشور ما نزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70869" target="_blank">📅 16:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70868">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=GTGjK9cKU8jtxumD-vrHrPzBn9rGfX46LO-OSUTi0Tye9_rBNruGeq0LM8iTcvar4jTy7GAJJ-6POn_XZvcGCMBfejmdSOlRq6vgEolvMRTi6vKhoNuK1cCNx4AL2wbTO1WVm5CEtpPT_BlFjD1AUVXJSn08XXTIRbxr5kWcM4752cpTDmnnV_VQRaElZ0_RF8LQoeLZ5AmrVXPInU6HpO6IE_4lSeaCsPmBDpmT34qS7GRzY7fRzGj3o3nQ_HiRi-5jgx9FG9Ha79rp2AD7FwFdbS6I61F7fBB2JlukeHjnJUmDht-Le_hxQoCrCfOj641WI36dzRzuOTXEtG-aYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=GTGjK9cKU8jtxumD-vrHrPzBn9rGfX46LO-OSUTi0Tye9_rBNruGeq0LM8iTcvar4jTy7GAJJ-6POn_XZvcGCMBfejmdSOlRq6vgEolvMRTi6vKhoNuK1cCNx4AL2wbTO1WVm5CEtpPT_BlFjD1AUVXJSn08XXTIRbxr5kWcM4752cpTDmnnV_VQRaElZ0_RF8LQoeLZ5AmrVXPInU6HpO6IE_4lSeaCsPmBDpmT34qS7GRzY7fRzGj3o3nQ_HiRi-5jgx9FG9Ha79rp2AD7FwFdbS6I61F7fBB2JlukeHjnJUmDht-Le_hxQoCrCfOj641WI36dzRzuOTXEtG-aYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین شهر مراغه رفتن سر چاه فاضلاب میگن با یاد رهبر شهید پروژه رو افتتاح میکنیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70868" target="_blank">📅 16:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70867">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUoTZ2ZYFej4Nn5RJfcqkHlI7ZFnR4FC0TRi6UVLJG2Ug0V3WmejJIxoOlbcDXDrGA4vgQwikuFgQEVwLkH8_gfg0qEPppZO1uUOv9n5aW2dYLWGBmClTQnASrYWehcM9hZtMzqmj2BTqIm-chwiNJ3ZDajs63NC4sXovwwFtu1fmJk5MLhrFD5TJ87JUJeg-2WJAj5mpCt10BDJS3EBeLJjQ2cREyK45Dh-p_2I1UfD-0VeYdFhY5BU53CRvsy1h7ytaCEUBTmzLP9kXX3BhqzGMbxAEbKxsMFfFkXVxU-AG2b-S9tv9X1AFyKWOdTiuaFBZuovOCIFpO3Tel_Y0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی:
نتانیاهو به زبان عبری آشکارا می‌بالد که چگونه دولت آمریکا را فریب داده و به نفع اسرائیل، آن را به جنگ با ایران کشانده است.
او صراحتاً و با خنده از این می‌گوید که چگونه با اختصاص ۱۰۰۰ ساعت زمان پخش در شبکه‌های آمریکایی، بر آمریکا «تأثیر» گذاشته است.
اما به زبان انگلیسی، از رهبری رئیس‌جمهور آمریکا تمجید می‌کند.
مار خوش‌خط‌ و خال.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70867" target="_blank">📅 15:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70866">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=cf7hR3Md8tdtmHM4tR6TxbIO5h6wq_6l8--oG2rZtIZl3vLspu2aZ65WbHF3YFSEMPyUUPDY4JEeYsxUEIUsBgLUireRlyj3EEHIH5p-hk6gx6T0szkYo4E3goQ0wdfx-U0kVRRtgk4P1Yy82I5Qkhb20eAOKXIg44eQjkgAZnZ6qEHzMcYCkF10rFbpnbFTkbIjtgIj27cwR0UuQ-JtLzT_Dn_vTBnXVzevS8QyIieMkFeZ2dyKsdbJ6hD3gneI_KXE0TFTWFL_suWuADn952C6mbP53PEdmyHJoYdZY7NVX-Ra1batCapVIq4DmoIWb3jCbOUKhkTWIyaMwIt2RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=cf7hR3Md8tdtmHM4tR6TxbIO5h6wq_6l8--oG2rZtIZl3vLspu2aZ65WbHF3YFSEMPyUUPDY4JEeYsxUEIUsBgLUireRlyj3EEHIH5p-hk6gx6T0szkYo4E3goQ0wdfx-U0kVRRtgk4P1Yy82I5Qkhb20eAOKXIg44eQjkgAZnZ6qEHzMcYCkF10rFbpnbFTkbIjtgIj27cwR0UuQ-JtLzT_Dn_vTBnXVzevS8QyIieMkFeZ2dyKsdbJ6hD3gneI_KXE0TFTWFL_suWuADn952C6mbP53PEdmyHJoYdZY7NVX-Ra1batCapVIq4DmoIWb3jCbOUKhkTWIyaMwIt2RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه وایرال شده از صداوسیما:
یه نفرو آوردن برای مصاحبه؛ بعد خود مجریه فکر‌ میکنه صداش نمیره تو میکرفون؛ به اون میگه اینا رو بگو اونم همونا رو تکرار میکنه
😂
آخرشم میگه دم غیرتت گرم به‌به چه شیرزنی بود
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70866" target="_blank">📅 15:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70864">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=jqESuGJmd59q4dvrnd9pKuIe9bC2xU8Sepe0L53ZPAWTOcbxtej0_X9hv4BXZIwZeITkl5kjFWyh0e-y2aCjpohbgwYjLK1DNm685uoDqwNLYxTJoLMUeJpGQ3l-M-JAYO9_2ToASLC6PKuD11Hll6ll0nFQivhyDuG7AeV3z90DMEVX6DF4ChCcqL2bhGU89nxU8mymlhvCtbzE7UP6WEp7Okx1TSB-XP2zQ9Re_TGvYaSx4eIOxVJUxyFhi7XUqoH_Duoz7YcRIdOH6FohxVCnbwynkBhs5EQ3AakbEgZ-hnPO7koD0GYazjP-MIMHyESvOA3ea639Li6RWt6VlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=jqESuGJmd59q4dvrnd9pKuIe9bC2xU8Sepe0L53ZPAWTOcbxtej0_X9hv4BXZIwZeITkl5kjFWyh0e-y2aCjpohbgwYjLK1DNm685uoDqwNLYxTJoLMUeJpGQ3l-M-JAYO9_2ToASLC6PKuD11Hll6ll0nFQivhyDuG7AeV3z90DMEVX6DF4ChCcqL2bhGU89nxU8mymlhvCtbzE7UP6WEp7Okx1TSB-XP2zQ9Re_TGvYaSx4eIOxVJUxyFhi7XUqoH_Duoz7YcRIdOH6FohxVCnbwynkBhs5EQ3AakbEgZ-hnPO7koD0GYazjP-MIMHyESvOA3ea639Li6RWt6VlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حواستون به دوربین مخفی توی ویلاها و اقامتگاه‌های اجاره‌ای باشه!
موارد واقعی از جاسازی دوربین مخفی داخل وسایل معمولی مثل ساعت، شارژر، دتکتور دود و حتی گیرنده‌ها و وسایل کنار تلویزیون گزارش شده.
پس وقتی جایی رو اجاره می‌کنید، مخصوصاً اتاق خواب و فضاهای خصوصی، یه نگاه به وسایلی بندازید که مستقیم به سمتتون قرار گرفتن. سوراخ خیلی ریز یا لنز غیرعادی روی یه وسیله می‌تونه ارزش بررسی داشته باشه.
البته اینکه «جدیداً بعضی ویلا‌دارهای ایران داخل رسیور ماهواره دوربین می‌ذارن» رو نمی‌شه به‌عنوان یک اتفاق فراگیر و تأییدشده گفت؛ امکان و نمونه چنین کاری وجود داره، ولی تعمیمش درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70864" target="_blank">📅 14:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70863">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=d3114cWbpGgm5A2tdE-XewJBPGFuAd9kCgit6Eh00iV3ed5ksXhvh6ZDPnlvUew1U3MRsu15Vyusg1E0USC7kKaz7OCFnxFvXaByXQIcaP-lrqzPnlhyVWlBff0C_u21T9U_-GNt4pNwYMCOXyyQLYdcgMQx7w-4Lh-GlukDiwbkg_CS_cjMnnlGm1zAQcf3GtFOUTlPrOPrBxRynzIPIfcCJXG15jORdG8mt7nsUcK1s5izWM3AGWGlMlqJJxre4flI7eorEXqf3GuuKoynI0alqM7MaGcjAyr-q-BOJ1RTCtwaLXorK8mEQd-joVuy-FwzmFPY36PPXiB7yx3hNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=d3114cWbpGgm5A2tdE-XewJBPGFuAd9kCgit6Eh00iV3ed5ksXhvh6ZDPnlvUew1U3MRsu15Vyusg1E0USC7kKaz7OCFnxFvXaByXQIcaP-lrqzPnlhyVWlBff0C_u21T9U_-GNt4pNwYMCOXyyQLYdcgMQx7w-4Lh-GlukDiwbkg_CS_cjMnnlGm1zAQcf3GtFOUTlPrOPrBxRynzIPIfcCJXG15jORdG8mt7nsUcK1s5izWM3AGWGlMlqJJxre4flI7eorEXqf3GuuKoynI0alqM7MaGcjAyr-q-BOJ1RTCtwaLXorK8mEQd-joVuy-FwzmFPY36PPXiB7yx3hNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
پست جدید اسرائیل به فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70863" target="_blank">📅 13:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70862">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K14LfXfXcwrMxX3inPHXYSaoRhvtPYyNC2lreEVGXbGM1SouODDp2UB4JFWjkFHo1qXv0eYJLrFq3ICFjlldwKiQzj4BB4BDz7k6XLsI9Z91Du07IcVjOYhKg2s1gcfIjfbQBfZt9U3CGnbmqWXYoRZ89OiZZQrVQNRIl2VPSnp622LjfsE6nuMmpqG8jxYh7AKLEezv_PEDlJ19nR8hZsS55bmRWxky5o3tkZMj4OBQN0908aiyfeJWPC-ZhXEB3swt4PSR3hOTwfUT19N94Ii7Eju_0a91nd7O7-YLm5c9bywB1ZAYyT2RbWTHtKGgw50qnPQUZkOGPoy8JNLd4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت، وزیر خزانه‌داری آمریکا، به خبرگزاری آسوشیتدپرس گفت که دولت ترامپ قصد دارد در راستای کارزار خود برای قطع دسترسی ایران به نظام مالی بین‌المللی، در هفته جاری یک بانک دیگر را تحریم کند.
بسنت اظهار داشت که واشنگتن به کشورهایی که همچنان با ایران مراودات تجاری دارند فشار خواهد آورد تا روابط مالی خود را قطع کنند، وگرنه با اقدامات تلافی‌جویانه آمریکا مواجه خواهند شد؛ او در این باره هشدار داد: «اگر ناچار شویم، این کار به مثابه خشونت مالی خواهد بود.»
انتظار می‌رود بسنت این موضوع را در جریان نشست‌های گروه ۲۰ در «اشویل» — از جمله در گفتگو با مقامات چینی — پیگیری کند. وی تأکید کرد که در خصوص اعمال تحریم علیه پکن به دلیل ادامه تعاملاتش با ایران، «همه گزینه‌ها روی میز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70862" target="_blank">📅 13:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70861">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=C5GoXr_SPnr5x5182slF-fmZBKQdog_X6TxbLS69AnsEvnVB1FI4HWqEtHH7gljUWNPqM_6beBcZ8oRohOUYuDTn_wc-q0e6n6nPemhprfKjTLLIFh69WFjMc3GDOLgiaCQqLdkqlNTV5lpKNCt-vQq_wpjYKKq-wUV6ktCoydYs03MezARNz2oGkCPVM-K6sBVER-4RxEJYZ25hhy4eKHWvTKnWdD7xpIR3lvKn9ZR-VDHVmlK4gm6GM80XlNsxLCxHDeF0RjSHLyFb3kal3z2pIxgqX23Fa7YARfMMfWKEOXEddGO3nrkE8mmWoDxSYGFoXRQ0_CiDgMl3mo-CpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=C5GoXr_SPnr5x5182slF-fmZBKQdog_X6TxbLS69AnsEvnVB1FI4HWqEtHH7gljUWNPqM_6beBcZ8oRohOUYuDTn_wc-q0e6n6nPemhprfKjTLLIFh69WFjMc3GDOLgiaCQqLdkqlNTV5lpKNCt-vQq_wpjYKKq-wUV6ktCoydYs03MezARNz2oGkCPVM-K6sBVER-4RxEJYZ25hhy4eKHWvTKnWdD7xpIR3lvKn9ZR-VDHVmlK4gm6GM80XlNsxLCxHDeF0RjSHLyFb3kal3z2pIxgqX23Fa7YARfMMfWKEOXEddGO3nrkE8mmWoDxSYGFoXRQ0_CiDgMl3mo-CpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇺🇸
ترامپ با هوش مصنوعی جزیره خارک رو نابود کرد.
جزیره خارگ دارد به تلی از خاکستر و آوار تبدیل می‌شود!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70861" target="_blank">📅 12:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70859">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=SJdfqIfJHWIgWh-0n4i3GbIDETtBOvkuyBEnN0SC4V1MUDfta1YVY8rQnHB4962mSeZ9e6yoYg8WudVeK5DDnNBphI6pWCoCLh_HP13gdX7Ng58RgCliUkX36VM0UOoKx51Isy-8busYA-sjPu429PjwkBxvjs_qvYsoOfTMYQroO0LEr_pFqWslt5RyMOVwTncTtXQ1GfLasyASSHZwncuzuzAgYOSXZxXae-07dhyKoEPQKtyZa9EsVdwzC-DonfdDyE0t_7I2r6m2Vsi8vnTqUGGiD8Jrwyk1J6uCql_X9oAFpy1nuhQXvKVTjmq9ENYGQLjyEpRAG9_FFGW3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=SJdfqIfJHWIgWh-0n4i3GbIDETtBOvkuyBEnN0SC4V1MUDfta1YVY8rQnHB4962mSeZ9e6yoYg8WudVeK5DDnNBphI6pWCoCLh_HP13gdX7Ng58RgCliUkX36VM0UOoKx51Isy-8busYA-sjPu429PjwkBxvjs_qvYsoOfTMYQroO0LEr_pFqWslt5RyMOVwTncTtXQ1GfLasyASSHZwncuzuzAgYOSXZxXae-07dhyKoEPQKtyZa9EsVdwzC-DonfdDyE0t_7I2r6m2Vsi8vnTqUGGiD8Jrwyk1J6uCql_X9oAFpy1nuhQXvKVTjmq9ENYGQLjyEpRAG9_FFGW3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آزاده اخلاقی همسر محسن نامجو:
بی‌ناموس تو که چهارتا ورقه گرفتی دستت گفتی دارم میرم همین سرکوچه تو آمریکا پرینت بگیرم، تو فرودگاه امام چیکار میکنی؟ چرا چمدون من رو اصلا بردی؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70859" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70858">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70858" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70858" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70857">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKrnFogNmbedFjbrtDR73zOHWi3J1F_8jbozpIqJ6oUVEmiuFrZtmGHErDhhcdVDkLLkgE7V7Qk_NlIwq-36wVn4XdmTdBB6pHvnHcr9-eeZzu11a98piLkLLGR0W2XBBQO-r0aGLuEeZkxJ6LjYze-gHMIA5fyqwTbIxoBmwLsx_Yqv9Q61U4aCD0L7cvs2_5MVQUCW1M_fplJRW5YqEFKZKNHciCL4prilbeHuicba5kQGav7qnAzqqnDa7sJ30MBiMRJznnWlWTro-vezOEKJfid10kWc--4Oc7uKnusl7tNH-JgxV6XV02N_MjGOzSP058EaekB3J-xfUcKNeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آرسنال
🆚
استون ویلا
رایو وایکانو
🆚
لیدز یونایتد
رم
🆚
لچه
بولونیا
🆚
آتالانتا
ختافه
🆚
اوساسونا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70857" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70856">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=OUyXrZsgs10rB2fxvf1OnhNiTo2vnjWCZepy45T0mEVkh110B3rzwVpD1CTauQk3YN3wxVili9kIUyLfrwRHgHM-Xllwigctc92vZ8Q_eFuNzCloM9PdeH4kCgXpekXlrMjuAdsDblG0qTIs3O8s0Lvtrcc0osnzqa3GqcofVBvq6hpL_rS6upvbNFdaRo0gvHSl4l_yoMbsdN-YgYktYaB89aeiM3UjEW7FrSY4Y7xOhTazf6cVuXuAeaFcTCxRJIFTWElQ3Jqg6Pf9rFL28n-nGFDWuQRsi1qxRFpXlV4zvl-hGFzilK_vLdxxgqVei-MmWyWX1njgig7LQxZ17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=OUyXrZsgs10rB2fxvf1OnhNiTo2vnjWCZepy45T0mEVkh110B3rzwVpD1CTauQk3YN3wxVili9kIUyLfrwRHgHM-Xllwigctc92vZ8Q_eFuNzCloM9PdeH4kCgXpekXlrMjuAdsDblG0qTIs3O8s0Lvtrcc0osnzqa3GqcofVBvq6hpL_rS6upvbNFdaRo0gvHSl4l_yoMbsdN-YgYktYaB89aeiM3UjEW7FrSY4Y7xOhTazf6cVuXuAeaFcTCxRJIFTWElQ3Jqg6Pf9rFL28n-nGFDWuQRsi1qxRFpXlV4zvl-hGFzilK_vLdxxgqVei-MmWyWX1njgig7LQxZ17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای ایشون که داره وایرال میشه:
با این شرایطِ گرونی، هیچ دلیلی نداره که شما به دختر مردم غذای مفتی بدی.
اصلا به حرف کساییم که میگن مردایی که پول میگیرن پرنسسن و لَنگن گوش ندین.
خیلی از دخترا بخاطر اینکه حوصلشون سر میره با شما میان بیرون و یه غذا میخورن، پس دنگتونو بگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70856" target="_blank">📅 11:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70855">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=dxCahEe11HyQ8gfqMKUdFRYJGAmGYb3pOotwjkKfe9vjaIo9Ic96GIMUSThyAJuVk7nqVqtBUWVQ3RHYQ2vYaFPTvr2lEu5AuXdzCTX-LpMBctvUqtp0UtailRQF_ofEuVmkMgD41JWxS95zXSOVqSpGa8anvpz8Y0Ms65r-Andli6_yazB9lvHux5zwHSNEgG3hgg7dcHa6vRFIppFekReENmr6d9JVUFYeUoNP9tK0h-tYhRN2bwbxHWCkMrT4dg4uW69KMJHP0PJmbfsz9urwTTSTRSF9YhAnU9nzc18UnZEe1GAib4HdObIZOw_Ez3wc0CpDIylzU-ZzlBVo_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=dxCahEe11HyQ8gfqMKUdFRYJGAmGYb3pOotwjkKfe9vjaIo9Ic96GIMUSThyAJuVk7nqVqtBUWVQ3RHYQ2vYaFPTvr2lEu5AuXdzCTX-LpMBctvUqtp0UtailRQF_ofEuVmkMgD41JWxS95zXSOVqSpGa8anvpz8Y0Ms65r-Andli6_yazB9lvHux5zwHSNEgG3hgg7dcHa6vRFIppFekReENmr6d9JVUFYeUoNP9tK0h-tYhRN2bwbxHWCkMrT4dg4uW69KMJHP0PJmbfsz9urwTTSTRSF9YhAnU9nzc18UnZEe1GAib4HdObIZOw_Ez3wc0CpDIylzU-ZzlBVo_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وایرال شده از طرفدار حکومت با پوششی جالب که میگه:
آقا فکر کنید شعب ابی طالب هستیم و محاصره مون کردن
این محاصره از شعب ابی طالب سخت تر نیست که
ما مذاکره نداریم و آمریکا هیچ غلطی نمیتونه بکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70855" target="_blank">📅 11:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70854">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=dHwvxBR2jl5njZr_i6wKB_JVnPrk_IbYfFw7tAKs2UKfMKnAQgj1FbV1up3CMkPbebquyVQTAOD3hrzfFBLDFwn2CGIdTzp_ku5GpoktOtHCbSvpyqTDOyLPyg_7USwoXLcWl3JxkyHJLnaUxNKRqGtZ--EWjW7iM4xpHk3gUgPFjw0bZdtLR3zO6uqZIsTHpGM6hmfhHpfCTvW59eFa8biUYw2SZN1x3PmE_ExtGovaLVb3vJtm383Aqs5xOVJGewWFrLRgDYHiFcO5C8kDmWAPT77NWj7xCWCwQBAZFkf--z4CD7LyBAQjH4PoukCwNKO_moNnehUHX3JA_snkVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=dHwvxBR2jl5njZr_i6wKB_JVnPrk_IbYfFw7tAKs2UKfMKnAQgj1FbV1up3CMkPbebquyVQTAOD3hrzfFBLDFwn2CGIdTzp_ku5GpoktOtHCbSvpyqTDOyLPyg_7USwoXLcWl3JxkyHJLnaUxNKRqGtZ--EWjW7iM4xpHk3gUgPFjw0bZdtLR3zO6uqZIsTHpGM6hmfhHpfCTvW59eFa8biUYw2SZN1x3PmE_ExtGovaLVb3vJtm383Aqs5xOVJGewWFrLRgDYHiFcO5C8kDmWAPT77NWj7xCWCwQBAZFkf--z4CD7LyBAQjH4PoukCwNKO_moNnehUHX3JA_snkVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
رهبرانشان از میان رفته‌اند.
تمام... خب، تمام تجهیزات ضدهوایی‌شان، منظورم این است که همگی نابود شده‌اند.
آن‌ها آدم‌های سرسختی هستند؛ آدم‌های باهوشی هستند. اما... خب، بسیار شرورند.
تا سه ماه پیش، پنجاه و دو هزار معترض را کشتند و متأسفانه، شمار بسیار زیادی را هم به آن فهرست افزوده‌اند. حتی سراغ کسانی که معترض هم نیستند می‌روند؛ به خانه‌هایشان هجوم می‌برند، آن‌ها را با خود می‌برند و به ضرب گلوله می‌کشند.
خب، این‌ها آدم‌هایی بسیار خشن و شرور هستند و اگر سلاح هسته‌ای در اختیار داشتند، اسرائیل نابود می‌شد.
اگر من رئیس‌جمهور نبودم، اسرائیل از بین رفته بود. دیگر اسرائیلی وجود نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70854" target="_blank">📅 10:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70853">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z49SMyQ184Q6Z6X_tCjvvusovNmPKiSYvGyjcO6yiLCKXSlGYwmu-jRIwyITt8IDnv2ygiZPgRDln17zMDhb-qvdZQxTwU0GDRAitQTPOqefjfqSY-wBafCgJ0bdky9uI8m3ZkLsL_AqhqDCtyLRcqw4D_zFQboZJd3VR8BzzQLZWseu_ZY6dGU_opUBBBRqI9qTymeb2hhGkRrWEE8rYIULoJKRi1Zmwk9-zMD9BX-Jab_acosiLkS0NMBCKZq1Q7AHGAWSYSaNrWTCIbIEXJyBxAVYwQhJc3sLVqxZRSbBWDKg_iGr75SFJneSVEeutWC-7P-lmNNYYJ57ul87YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
〰️
سنتکام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران در بیانیه‌ای اخیر مدعی شد که حملات نیروهای آمریکایی برای جلوگیری از مین‌گذاری سپاه در تنگه هرمز، «اقدامی تجاوزکارانه» بوده است. این ادعا کاملاً نادرست است.
✔️
واقعیت: نیروهای آمریکایی علیه یگان‌های مین‌گذار سپاه که در تنگه هرمز تهدیدی قریب‌الوقوع ایجاد کرده بودند، دست به اقدامی محدود و دقیق زدند. در واقع، ایران عامل ایجاد این تهدید بود و ارتش ایالات متحده برای حفاظت از دریانوردان غیرنظامی، کشتی‌های تجاری و جریان آزاد تجارت جهانی، آن تهدید را خنثی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70853" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70852">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=q9Wf58FKd3OFic9jJm6n5iCWjtQmLQhL38Y7ONZRYpExlx5nwa22pXo9dGuKtBM1zkHshe9Ib0Q8p9zKUJN3RPwYwv7D8IsOGT1_2aJPhOlxcpw1XrieA21K5KKgD4GNAwKDYCAc0cXwbYadSX2QjO6EVSkctFWGKM9TJs_N-fk7kXs3X11Ht-cwjo5um17Xg0AwHbb9xl4_ZFuEN_Pr2EkM6oVuYmywi-zUvfuAaJ2FAts4_gWeNV4Mps3yd0k91iWiDSnjYBx8-WozH1PAWPsd-Ixm9u77S48RsMxLdX_ayAm5u1G8hHyNSGNhjlAanns3I2kjmdCdZwT7ZWd9dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=q9Wf58FKd3OFic9jJm6n5iCWjtQmLQhL38Y7ONZRYpExlx5nwa22pXo9dGuKtBM1zkHshe9Ib0Q8p9zKUJN3RPwYwv7D8IsOGT1_2aJPhOlxcpw1XrieA21K5KKgD4GNAwKDYCAc0cXwbYadSX2QjO6EVSkctFWGKM9TJs_N-fk7kXs3X11Ht-cwjo5um17Xg0AwHbb9xl4_ZFuEN_Pr2EkM6oVuYmywi-zUvfuAaJ2FAts4_gWeNV4Mps3yd0k91iWiDSnjYBx8-WozH1PAWPsd-Ixm9u77S48RsMxLdX_ayAm5u1G8hHyNSGNhjlAanns3I2kjmdCdZwT7ZWd9dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سرهنگ خلبان بهمن فرقانی، جانشین فرمانده پایگاه چهارم شکاری دزفول :
زمان جنگ، آخوند رسول منتجب‌نیا به پایگاه ما آمد و پیشنهاد داد برای بستن تنگه هرمز، فاصله عمان تا ساحل ایران را با قایق‌های موتوری با طناب به هم دیگه ببندیم تا عرض تنگه بسته بشه
به ریشش خندیدم و گفتم: «چرا مزخرف می‌گویی؟»
زیرآبم را زد و از نیروی هوایی اخراجم کرد!"
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70852" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70851">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=FvzxafToLuLMiK5TBDzy8NGFbqmcfhNWVugQInSc80uZKc1PQ_8ZDSWDTY-LJ1U1gbo3nNVLFa-otOjtk5T7uEbzDzOezQB9S7LUvCYxiRRkjRaXENRcc09LYwSz2dnVhb2ceDxzchmFPFAsTwr7XF_fe0IiJ0YgyMlbv1-24nx_-3cc14_jJtQ_mYB2PRJSjHg5IZj5Ny7lc945MkJsAcCeAgXXV_H2SPZtjFwZsnSUM3eKWkrSVjgRWS_OdH-XJPhDBG1YlL8I3-qJLKeTWb6m3DEjAnFL3BKAW_aaZbMBaVdT9Dy5YdESVFi69MP-lCOBHZzQqEjYZoSEEvzzu1g5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=FvzxafToLuLMiK5TBDzy8NGFbqmcfhNWVugQInSc80uZKc1PQ_8ZDSWDTY-LJ1U1gbo3nNVLFa-otOjtk5T7uEbzDzOezQB9S7LUvCYxiRRkjRaXENRcc09LYwSz2dnVhb2ceDxzchmFPFAsTwr7XF_fe0IiJ0YgyMlbv1-24nx_-3cc14_jJtQ_mYB2PRJSjHg5IZj5Ny7lc945MkJsAcCeAgXXV_H2SPZtjFwZsnSUM3eKWkrSVjgRWS_OdH-XJPhDBG1YlL8I3-qJLKeTWb6m3DEjAnFL3BKAW_aaZbMBaVdT9Dy5YdESVFi69MP-lCOBHZzQqEjYZoSEEvzzu1g5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یک سرهنگ فراجا:
متأسفانه مدتی عده‌ای از مراجعه کنندگان و یا به تعبیری ارباب رجوع به ما مراجعه می‌کنند و در خصوص گرانی‌ها معترض‌اند و هر بار که به ما مراجعه فکر می‌کنند، فکر می‌کنند که مسبب و اینکه ما از دست ما کاری بر می‌آید و نمی‌توانیم برایشان انجام بدهیم.
آقایون مسئول، عزیزان مسئول، به خدا گرانی بیداد می‌کند. آقای برادر تعزیرات، آقای بازرسی کننده، آقای بازرس اتحادیه، به خدا با کت و شلوار اتو شده و موهای ژل زده و عینک دودی نمی‌توان با فساد مبارزه کرد.
آقا یه جای کارو درست کنید که یه جای دیگر را بخواهید گوش‌نظر بدید. تو رو به خدا، تو رو به هر کسی که می‌پرستید وضعیت معیشت مردم را درست کنید.
فکر می‌کنند به عنوان پلیس ما از جای دیگه درآمد داریم، از جای دیگه خرید می‌کنیم. به خدا این چنین نیست. ما هم مثل همه شماها از همین فروشگاه‌ها خرید می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70851" target="_blank">📅 09:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70850">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78504efb49.mp4?token=ZHIf6Dq0YzIjdJenc0hXX1gbJekhSXI1I0IW6HeGrHaVE5aFCzFj5iCR_iRWys2JtZZcDtHySGDVvDkWp51pq00vfxp0Yk4DfMaZUE5D6e64wMR_Mh2v10MTovYMPKuZeoFwgozx7EfegUUuhuVNhIslso_cBWwgdZYRw0UQ6EGykFq5WIF0-YdsMZ5gJqmVIiDIxW-QbqRkosfZowvxGzgGFY6CoyzvJwfvRNVxtdldoIHFH5vYkeMFTJhYqUHuhHiVa3jtuCcqN2iJECvHe-9sbZYo6znFXL-Ap76MprlJWkyq5ARmJZ6n7aAn9Ki5BbWFf8EBOx-5gZGfvaJ_hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78504efb49.mp4?token=ZHIf6Dq0YzIjdJenc0hXX1gbJekhSXI1I0IW6HeGrHaVE5aFCzFj5iCR_iRWys2JtZZcDtHySGDVvDkWp51pq00vfxp0Yk4DfMaZUE5D6e64wMR_Mh2v10MTovYMPKuZeoFwgozx7EfegUUuhuVNhIslso_cBWwgdZYRw0UQ6EGykFq5WIF0-YdsMZ5gJqmVIiDIxW-QbqRkosfZowvxGzgGFY6CoyzvJwfvRNVxtdldoIHFH5vYkeMFTJhYqUHuhHiVa3jtuCcqN2iJECvHe-9sbZYo6znFXL-Ap76MprlJWkyq5ARmJZ6n7aAn9Ki5BbWFf8EBOx-5gZGfvaJ_hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل به فارسی:
جمهوری اسلامی و سپاه پاسداران سال‌هاست که ثروت و منابع ملی ایران را صرف تروریسم و جنگ‌افروزی می‌کنند، در حالی که سهم مردم از این ثروت، ایستادن در صف‌های طولانی و بحران کمبود بنزین است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70850" target="_blank">📅 09:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70849">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70849" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70848">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pci6o0eTGFCz_NwAzRETbdzC0R2_qwnGi-OYSwwjMSwWoPtkheVW8M2hDnWHsVSNpAWqD4i3qyfwgWjyRPTXS4_OsskmzVC-So_a3hG8GxP8qyKS0EEOzDj2_JF3XEUxkSCYfI-rkXW2x3JXGF3QqcUA_jC5zMYqxsBbPtz9TRs5RP0I5zfPl_EXoSoQT4jvxP6oBZTXf4W3DyzbVKrnDjmaEwokqUFrR8w-3QJkctPUvOjqB0yVbgMx_CRzAZ9jFzollC6odMBW4-Mi58FT_eho5CsSMugwFJf1Lgw9Z5yFP2nHnFQy-RkpgdgpxbCI0MZwYdk2n5qrldGL947r8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70848" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70847">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
نایا:حملات موشکی به قطر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70847" target="_blank">📅 01:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70846">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">یادآوری: علی خامنه‌ای، دیکتاتور و بزرگترین جلادِ وقتِ خاورمیانه در ساعت ۹:۳۰ دقیقه صبحِ ۹ اسفند ۱۴۰۴ توسط ارتش اسرائیل و آمریکا، تکه تکه و تجزیه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70846" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70845">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بچه ها بزارید منم این وسط یچیزیو یادآوری کنم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70845" target="_blank">📅 01:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70844">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr. NOBODY</strong></div>
<div class="tg-text">خواست پاتریوت رو با لهجله بیریتیش بگه اذیتش نکنین</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70844" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70843">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɴᴀᴢɪ</strong></div>
<div class="tg-text">امیر پهن مغز پتریوت چیه؟</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70843" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70842">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaxmCTapQcDuKwlqbM91_iuXt5obespog5cJT_dEU58o-PVCHr7sOmKOeKRfbsD9O_MCQVdDSZ4mI-m6RQQGdxRdfYHshGBfVEiPngyEzS_Ga3PG2qXcgndtrBX8xkCH23ZyGd3Ru95NHQsoz-3XE0GxHeZe745OsHvnI84YJVq7sRDDf02Nj2CZUShjCWTolgKOnhIQBgxoyzos08FbuMkYqWGjq70LQ2UYep5hDiZypN2dmYcnQaiIoWq3_PdgZUf28uQEQ41lke5AX-ybKOx2kQlfjopHZQSMqoAH0r8JpnpBq00YL_A_w-Hur1xyO50ErBcW0BruH84k79fhaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا برخورد موشکی صورت نگرفته، اکثرا رهگیری شدن #hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/70842" target="_blank">📅 01:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70841">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=Anq5y5gK_wXs3QhFjQH9NdsHFkbBulayZ1EtTxFUaFVzZkSYVscvm_QpqoHF8ioBLaOVHwbYAyO5Um4MFpoyWHq1sH9PEzEqTG-kPHw8sDMluSwoOw49AQ4pgzne3MCaU9YM5cX1jM04KXa64VfLYvqzaoYQDzuE8SwO4zheiI7xsZdyEJkJb7i2RKPQzoWiKlox4lLKPbpJzgGso23ytHbiBU7qWzTwnOGPYIzVvxi8roxQ3sqj9KuzIPU9bMfRZ81qPY0nFgE41qEOfMfrxfB_Wc3I3i_v_Cf0bIokRjwsl7QRGLgy0LpL-K-zI6CAiEWZECLixcV5iUZ0k-lF1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=Anq5y5gK_wXs3QhFjQH9NdsHFkbBulayZ1EtTxFUaFVzZkSYVscvm_QpqoHF8ioBLaOVHwbYAyO5Um4MFpoyWHq1sH9PEzEqTG-kPHw8sDMluSwoOw49AQ4pgzne3MCaU9YM5cX1jM04KXa64VfLYvqzaoYQDzuE8SwO4zheiI7xsZdyEJkJb7i2RKPQzoWiKlox4lLKPbpJzgGso23ytHbiBU7qWzTwnOGPYIzVvxi8roxQ3sqj9KuzIPU9bMfRZ81qPY0nFgE41qEOfMfrxfB_Wc3I3i_v_Cf0bIokRjwsl7QRGLgy0LpL-K-zI6CAiEWZECLixcV5iUZ0k-lF1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رهگیری دو موشک سپاه پاسداران بر فراز اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70841" target="_blank">📅 01:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70840">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن  @News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70840" target="_blank">📅 01:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70839">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:  از خرم‌آباد صدای انفجار شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70839" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70838">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از خرم‌آباد صدای انفجار شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/70838" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70837">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">صدای انفجار شدید تو خرم‌آباد شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70837" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70836">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44471a1938.mp4?token=Zy6DZNUDVJW_e6vzOpV1_GuCSAnqkdVKDPBn0-JeVHuIn-vauCidaEac3zFJcmE-IvyLAOqHsAPmK_lgrHVH6krgwXH6eQkSVbqjlHb6FwRt8j7Hj8EKjpQacpdBpXGsbl80kcW_y9mI6H2SDLrONnmPKL3FM1nuG6xvfDPyOkrhiYj5m6V5450ioZD6v0JlehaKScvLuFu9GppyAEDnJ_-tN32oBOe0znXN4-rJk_VOx9IzaAo-BMNKAZhW1Auw4UnKICxZ7_vrg7c3BgMkmfiP56qyWILfz9EuSdDrwrv2F7Xqlic_GJSCcjg2-KJNW66XGD1Pwhxt4G3TJnoA_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44471a1938.mp4?token=Zy6DZNUDVJW_e6vzOpV1_GuCSAnqkdVKDPBn0-JeVHuIn-vauCidaEac3zFJcmE-IvyLAOqHsAPmK_lgrHVH6krgwXH6eQkSVbqjlHb6FwRt8j7Hj8EKjpQacpdBpXGsbl80kcW_y9mI6H2SDLrONnmPKL3FM1nuG6xvfDPyOkrhiYj5m6V5450ioZD6v0JlehaKScvLuFu9GppyAEDnJ_-tN32oBOe0znXN4-rJk_VOx9IzaAo-BMNKAZhW1Auw4UnKICxZ7_vrg7c3BgMkmfiP56qyWILfz9EuSdDrwrv2F7Xqlic_GJSCcjg2-KJNW66XGD1Pwhxt4G3TJnoA_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/70836" target="_blank">📅 01:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70835">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبر متوقف شدن پروازای فرودگاه مهرآباد هم فیکه #hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70835" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70834">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
منابع عربی:شنیده شدن صدای انفجار در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70834" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70833">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🔴
گزارش ها از شلیک موشک از نقاط مختلف کشور به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70833" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70832">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب  تلگرام یه‌پا شده روبیکا... #hjAly‌</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70832" target="_blank">📅 01:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70831">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbAeYUyDK4M_FCgQi1FGbwn4dX-6eVCyFDrMuJqTwfxoHa44dPB7_3LvAJYaRf9kT2Sqyyx0nfqS_bEtohVtyG8nAp19Ps-AxGezjJzXSIl--Jo02WEbJfca0dxwn-7idwphoXDX4zbUsMPCweWni1bjtrNi4BQVaW3Lo67Nnfe2ZAmfjEaHi6FKjolxz0OM2VfK5_FHqtTajNHpp5wAyXfHS7rDcRplGeTI4h20_G_RK2hwi7kolYDoPHpzd72bHHIfC5KrKnLal8ot246tkN1sGZY7ZA-WhQvExDsKDUq7Yo7w3uSVN7vcOpBGEvDWkrdduAo8CjJhrTPHQTNIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70831" target="_blank">📅 01:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70830">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=qRNzT9qoJbq6zVjpYQejjZSRgXzSbVKx7rNu-gRqEyTGe4piTR4pt3-NK_udgmgKDO1zm3UMS7cG_knBfTAKq9xCLZbepTn9Ms2uBCWY6jMLWZNaopWvGKfMfq9J3qaq-3-mTKVy-RdpbzfZvDSto9QGyFg4k_ztDh1SBGPLGOdv8z0sJ7UjMUu3iDqrV4lOVdhK89WPYsLyOaS5RJhPHWmqDPsOXSpsj-2nFSDI0H_86EKKd2oLWmtH68B8OY8hVyLUMX2I_VYwXrIaM7AmjVNroeTF3NBmHZ0BQ0TKneAThAgTLQScx2-H1-iqpkuWm6ORDU65w99dIVyRgQIbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=qRNzT9qoJbq6zVjpYQejjZSRgXzSbVKx7rNu-gRqEyTGe4piTR4pt3-NK_udgmgKDO1zm3UMS7cG_knBfTAKq9xCLZbepTn9Ms2uBCWY6jMLWZNaopWvGKfMfq9J3qaq-3-mTKVy-RdpbzfZvDSto9QGyFg4k_ztDh1SBGPLGOdv8z0sJ7UjMUu3iDqrV4lOVdhK89WPYsLyOaS5RJhPHWmqDPsOXSpsj-2nFSDI0H_86EKKd2oLWmtH68B8OY8hVyLUMX2I_VYwXrIaM7AmjVNroeTF3NBmHZ0BQ0TKneAThAgTLQScx2-H1-iqpkuWm6ORDU65w99dIVyRgQIbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش ها از شلیک موشک از سایت موشکی بیدگنه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70830" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70829">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب
تلگرام یه‌پا شده روبیکا...
#hjAly‌</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70829" target="_blank">📅 00:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70828">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E28pSVw31yadK_4nWeGYp7jek0pojHTCBoy7Rd1_bcAMWmkTqLOf0tahWCjFllz3wWElIkQJq8H0pdZvK5CwTtc0rsHEA_I85KloVUElDPWLs_1Pd9BjYD7lI-hXmgyWQP57suE8T72EPzvNDwHu74swLO9vOzG_JhiYFqChi2yaaOcH2m-_XmKYWTY4ijZEWxENSZlbwxSXf0q0c3uZwX3TCvi7IO1cjxY1Z8_jTb0UL7F-zgek_SSpt6WKv2Fh3Rwi_g29WYpQ1cloirobBO9FdekxqTFK_o5qM-iKOCPgtK1CvuEA1FQ668SuAGKc_ZyD7zhZRTSRcIGKlcv4Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
ابراهیم عزیزی:
یک بار دیگر اراده ما را بیازمایید و بهایی سنگین‌تر بپردازید.
انتقام در راه است؛
فقط فرار کنید!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70828" target="_blank">📅 00:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70827">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=OH3L8j2zZBTNoCaOq7b7wNbYiWz9KC3xkTu-G28XjTsDkZo3s8t1AKvXNhiu-CMcFnTtAq7-cIjfeLTl9wA6h5SBC_b41Rp9teW_wBkn7zoN22wf52DDrqxzqDcN8KwLzgjLdB0-bnepFpwkhd04aAHBCHAKfP01OWJcV0iShba7bD-sSq2biQGCaKhmBuDvCPZCoOOl2KLK6NAIsFcxZA4bCfaTCOVBWvVxvoPO03_R1T5KR71uuhW7GZ_7gdSHFl8_nMZLqvLnQX7dowIg3bTjDS4Ovf88WDQfYrqcBZB1q84pM6jz2urr6wxeihwMXx5VKQwdOfcZcP87HfCctagYtOE6in4mceHGlvL6af-rTHIwQhrZ51sX9ufGO-MIDT55rV3wtzlANW8gE_wHVWYascG-xY60YnMDgp_PPL2kzt6U5MC_h4hMY7Kfjad-Bdr3hgDNsWrfFPuT5sYRLaTLiD1ohHaQPIiltxKgttKqN99-MMSI2OPoz9phT0Hg7pcT6smYHl3gyfnxWxQgufPqVfi15G6HO7BUqG20Cnb8xuqfMkrKW2bG5UF-qdH3SgtPvwFE1guUbwJbK4OKYbcEVstAqI4Y9W8aRPUid8X-CCo1xdy8ACgeS8B-EpvNRefyTA13xo8yRTMcaK2fP6a5J_fTJRhKHS_YB1ruIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=OH3L8j2zZBTNoCaOq7b7wNbYiWz9KC3xkTu-G28XjTsDkZo3s8t1AKvXNhiu-CMcFnTtAq7-cIjfeLTl9wA6h5SBC_b41Rp9teW_wBkn7zoN22wf52DDrqxzqDcN8KwLzgjLdB0-bnepFpwkhd04aAHBCHAKfP01OWJcV0iShba7bD-sSq2biQGCaKhmBuDvCPZCoOOl2KLK6NAIsFcxZA4bCfaTCOVBWvVxvoPO03_R1T5KR71uuhW7GZ_7gdSHFl8_nMZLqvLnQX7dowIg3bTjDS4Ovf88WDQfYrqcBZB1q84pM6jz2urr6wxeihwMXx5VKQwdOfcZcP87HfCctagYtOE6in4mceHGlvL6af-rTHIwQhrZ51sX9ufGO-MIDT55rV3wtzlANW8gE_wHVWYascG-xY60YnMDgp_PPL2kzt6U5MC_h4hMY7Kfjad-Bdr3hgDNsWrfFPuT5sYRLaTLiD1ohHaQPIiltxKgttKqN99-MMSI2OPoz9phT0Hg7pcT6smYHl3gyfnxWxQgufPqVfi15G6HO7BUqG20Cnb8xuqfMkrKW2bG5UF-qdH3SgtPvwFE1guUbwJbK4OKYbcEVstAqI4Y9W8aRPUid8X-CCo1xdy8ACgeS8B-EpvNRefyTA13xo8yRTMcaK2fP6a5J_fTJRhKHS_YB1ruIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:
من این رژیم را به زانو درخواهم آورد. به این امر متعهد هستم. این کار شدنی است.
آن‌ها بسیار ضعیف‌تر از گذشته شده‌اند و در موقعیتی متزلزل قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70827" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70826">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
آن‌ها از برنامه هسته‌ای دست نکشیده‌اند. ما آن را به عقب راندیم، اما آن‌ها کاملاً قصد دارند برنامه هسته‌ای خود را برای تولید بمب‌های اتمی از سر بگیرند.
بنابراین، این تهدید از بین نرفته است. ما این سرطان، این غده سرطانی را ریشه‌کن کردیم. می‌دانید که اگر سرطان را ریشه‌کن نکنید، می‌میرید. این همان کاری بود که ما انجام دادیم.
اما سرطان ممکن است دچار متاستاز (گسترش) شود و در صورت بروز متاستاز، می‌تواند دوباره به تهدیدی تازه و بسیار جدی تبدیل گردد.
ایران می‌خواهد برنامه هسته‌ای خود را از سر بگیرد.
من پیش‌تر یک بار مانع این کار آن‌ها شدم و تا زمانی که نخست‌وزیر باشم، مانع انجام آن خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70826" target="_blank">📅 00:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70825">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcop_3JdymKSEDghBxCcml5D5ibG-whDQVZROQcGbyyHMCTg3kF_2Vg57N5zvMN3uI1o9c3_yDGtLmx1WQhwESDtY2UAxawF8zqak3k10Qu8tBQKkevA1Na5-vSDdV7SBnlaR5VTQtBH7yPyjaBVa8ojtawC7OCWuyfgp7ygeTuVtRdfppgquJxSS9xqyAFfEeJBrCrb2_lhYeX6a3i4ZPSJj7hIBSsdKUUmva14eCWkzpRplZeVU0IzDBrdVgBKDSIs_N9X28yR-aWrFtdM7tJ6Mkl5Dk0M3BdfEjEneKyxTINnqza-F9nDVe-yo4GoLIGpaRPQZPblGD8iPvehDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
سخنگوی سپاه پاسداران انقلاب اسلامی:
این اقدام، یک خطای راهبردی و مهلک از سوی دولت ترامپ در چارچوب جنگ اقتصادی است؛ اشتباهی که کفه ترازو را به زیان طراحان آن تغییر خواهد داد و هزینه‌های سنگینی در پی خواهد داشت.
دشمن پیامدهای این محاسبات نادرست را در هر دو عرصه اقتصادی و نظامی متحمل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70825" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70824">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
مجدد صدای انفجار در جزیره لارک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70824" target="_blank">📅 00:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70823">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری؛سپاه پاسداران:   تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/70823" target="_blank">📅 23:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70822">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛سپاه پاسداران:
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/70822" target="_blank">📅 23:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70820">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-MSRwVLE85uICbKHDzT4F-JLKZTnHkzSpd3tumb3kvsISg9acBLxusvf6KK8o9IGK0cmwqY7A3OJ5T5pkG2P89pibJfH_q-3KMD6YhnpgDkvWi9SxtT3lS8bg40oLTxVEoDnTK6Dtq1Rihtcfy-Grlef_CT-AdN8Gh_B79fppVnzlFF1tYmXnVNjE0QXCBwAyBRlwFmlRL9XblsV_HqAOUaWQoEwkwQwTzzlW8oBeG-Je9RXhrfxSZzkVXH2s7oMrXteTwjH24dR6S5DM3ufVai5oUS-tP6pgL6CvTGpxKXRF7FBddXauGKccOBHzP95BNxR4Oa-kKjBlJLOM1vQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d778b593.mp4?token=ZC_uDa7SRp3F_qEyVynRpTj3GhmoR5hlNJ9cwZs5_kuG4ox1vqZWiQ4xzF_Cuob3oTmYgoLTOgemBbPRNUYJYQOwGs9rrUd_iE0CdX4G2y38GV8xFhyTnwMSuS0M9TrwPiA31SQ7wDZ4_MdzeFx7-0byComlFF4DZD2glOtE6ovp6BbieEwmQkALFxb4T4tr6mg05_SyITiqMdRxEIPY0TdKrGfs9R5CVG6TOZzNes5LD49TrRvqr5FqKOu4L_mFKJ1afoA4ASAOX6sHHzXEvsOIdt6gRJGzuEA4-E-Qn0E6DJgFbNvTA-cWff2ZrcIMrjXjO1RXfmlGpb-bg1RtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d778b593.mp4?token=ZC_uDa7SRp3F_qEyVynRpTj3GhmoR5hlNJ9cwZs5_kuG4ox1vqZWiQ4xzF_Cuob3oTmYgoLTOgemBbPRNUYJYQOwGs9rrUd_iE0CdX4G2y38GV8xFhyTnwMSuS0M9TrwPiA31SQ7wDZ4_MdzeFx7-0byComlFF4DZD2glOtE6ovp6BbieEwmQkALFxb4T4tr6mg05_SyITiqMdRxEIPY0TdKrGfs9R5CVG6TOZzNes5LD49TrRvqr5FqKOu4L_mFKJ1afoA4ASAOX6sHHzXEvsOIdt6gRJGzuEA4-E-Qn0E6DJgFbNvTA-cWff2ZrcIMrjXjO1RXfmlGpb-bg1RtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
یه نمایشگاه عراقی اومده پژو پارس گذاشته برای فروش؛
و اما کامنت مردم همیشه در صحنه :))
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/70820" target="_blank">📅 23:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70819">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
#فووری؛ باراک راوید به نقل از مقام امریکایی: امریکا امروز به دو پرتابگر ایرانی در جزیره لارک حمله کرد  نیروهای سپاه پاسداران سعی داشتن موشک‌های حامل مین دریایی به تنگه هرمز شلیک کنند که قبل از پرتاب توسط امریکا منهدم شدن @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/70819" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70818">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ua5l-_2eSrjwViHXQweW2_DxNk8R1KttgQQ22iBUZbbPxAvrZjHdDYDb5qFcgAxFVjXlWekJGTbHRWAbdy7W7Cuy5_mkY12lSWImPkFtmfI7Dk4pupiafa5AJlmpt_iiXFu_AfWQLGTLmvaLMZ9DfEW9YkmN-yjGp3YK5PAzzy36YVXNiPBbFw4wOdMJgdZYM35EdGNsbj01pU2UZimx7EMi9P8jJgafV4CqDvaXeiTX9FrnEG2s8G3WiOB794ifhv8jpvlXe2LINxGnxKbMDTP7yoAr0O9witR8TAwm0IZaxo3T2ID74Tvrit59QoFash9GXR3J54iuA2SJIu9-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووری
؛ باراک راوید به نقل از مقام امریکایی: امریکا امروز به دو پرتابگر ایرانی در جزیره لارک حمله کرد
نیروهای سپاه پاسداران سعی داشتن موشک‌های حامل مین دریایی به تنگه هرمز شلیک کنند که قبل از پرتاب توسط امریکا منهدم شدن
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/70818" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70817">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6826005e4.mp4?token=UVQtF9S_zyjbOubo4D0XOvkNDZ4cGroNxHhgeCgwhlIKUFHq1LXXTULYm3Va_rLoD1PcAoXU7q9KFkLzsfAiufnQ16Xh__j6cvaqmsGTZvNFIgXIsf6a85W8A1yVLQw938LP3LfeFp7YDyLOPYbp1Nq-AsiuiV9VOQsYTESGMDmr-PGzfvPooMVPpzJFO5R8Wnl2cRLKBrkz6WXtl9qBgiQv-7qECuVJ61CCakATk5vtDO7XJIVNop2dCTNMIryWrUkeiiEoc7N5Vz3elVBOrOIhGgDC1JFvE4IbNWbiMkoZIJLMCoaZoZvrO2-puF2rx7ZTxQKHRyZ7USpLt8U8tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6826005e4.mp4?token=UVQtF9S_zyjbOubo4D0XOvkNDZ4cGroNxHhgeCgwhlIKUFHq1LXXTULYm3Va_rLoD1PcAoXU7q9KFkLzsfAiufnQ16Xh__j6cvaqmsGTZvNFIgXIsf6a85W8A1yVLQw938LP3LfeFp7YDyLOPYbp1Nq-AsiuiV9VOQsYTESGMDmr-PGzfvPooMVPpzJFO5R8Wnl2cRLKBrkz6WXtl9qBgiQv-7qECuVJ61CCakATk5vtDO7XJIVNop2dCTNMIryWrUkeiiEoc7N5Vz3elVBOrOIhGgDC1JFvE4IbNWbiMkoZIJLMCoaZoZvrO2-puF2rx7ZTxQKHRyZ7USpLt8U8tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
محسن نامجو در کنسرت نیویورک، شانزده شهریور نود و دو
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70817" target="_blank">📅 23:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70816">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d075c961c.mp4?token=fejBjMd9cxYfaoOx_ksaTDBJUBRy-cTPJhvWnnwP_V8pLRx-jI_pxFljreIqJRErwNVL18AtMveBDxIWoiBuAlgjw4uH3A64-_juvvvF71iWdLhqNegnw-s7FAdONGRh85nParEN5BfuCNnQ5kEuTATB89kUZEe821ImGI8MTzJkJcDge5YJfKnraFZPcO5qHiqujmniu5FctkRqdnhI1KvN7i0zqmplgddUZfqjtfaWb2ImD-tVlvZYACuCwM4JJwEdsEQuBF1zyy70AkUOmKU6VcB_tRqNXPNs6gniuKPsym3HX5tebK1VUnBguZ6uqrahN90rcXO0fP_jExPtNoF3zrAlJdvLsY2umxzzU7z_lr6wtLuWb5q_I5NDWpg5radCdiKX4ZgaswrG6I1NNnjB_VWNxD7rzJM1VgP8w-U1zyaR4Ov013ehI-wBj5sFjqpUb4jU460C4b9pVtQvchPgh88FORhaCD5dJBjqZaopkXdECDTLrMW0VWx24IngxdNjR1AEtDT8BEsgP3mGfc-qcRhy8l0RnYFpiDwnIHXhBtU4Vd-4n4hU7rpTl4W-tKxYa-bhhNRtFen4CRbznfHdNn4Z_r55FtL6Y6mly86fc2oMoPh45Y0Ky4DvNAkEJzbfgn1OVfgy03-d_xkparQ8hbvLH36dB3rLzcD1-i8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d075c961c.mp4?token=fejBjMd9cxYfaoOx_ksaTDBJUBRy-cTPJhvWnnwP_V8pLRx-jI_pxFljreIqJRErwNVL18AtMveBDxIWoiBuAlgjw4uH3A64-_juvvvF71iWdLhqNegnw-s7FAdONGRh85nParEN5BfuCNnQ5kEuTATB89kUZEe821ImGI8MTzJkJcDge5YJfKnraFZPcO5qHiqujmniu5FctkRqdnhI1KvN7i0zqmplgddUZfqjtfaWb2ImD-tVlvZYACuCwM4JJwEdsEQuBF1zyy70AkUOmKU6VcB_tRqNXPNs6gniuKPsym3HX5tebK1VUnBguZ6uqrahN90rcXO0fP_jExPtNoF3zrAlJdvLsY2umxzzU7z_lr6wtLuWb5q_I5NDWpg5radCdiKX4ZgaswrG6I1NNnjB_VWNxD7rzJM1VgP8w-U1zyaR4Ov013ehI-wBj5sFjqpUb4jU460C4b9pVtQvchPgh88FORhaCD5dJBjqZaopkXdECDTLrMW0VWx24IngxdNjR1AEtDT8BEsgP3mGfc-qcRhy8l0RnYFpiDwnIHXhBtU4Vd-4n4hU7rpTl4W-tKxYa-bhhNRtFen4CRbznfHdNn4Z_r55FtL6Y6mly86fc2oMoPh45Y0Ky4DvNAkEJzbfgn1OVfgy03-d_xkparQ8hbvLH36dB3rLzcD1-i8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇵
🇨🇳
تصاویر بالگرد چینی از  سرچشمه سیلاب مرگبار در مرز چین و نپال
یک بالگرد چینی خود را به نقطه‌ای رساند که در آن یک یخچال طبیعی فروپاشیده و حجم عظیمی از آب آزاد شده بود.
این حجم آب با حرکت به سمت نپال، خسارات گسترده‌ای بر جای گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70816" target="_blank">📅 22:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70813">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BPpAfpawY8wBwEXuCR8K7oDG9H5djtPu6isABAs7nyOhZyzKLffPF71k0M8bpnWK-_kE72U5ubhoKgGYKzWhKoS1oPiVL2ojBSgoehKFEfip_bnX5NDXn425DwojhtDJFTcEWtQalyqfBimYw9qQzvx4tczTg6ms9wjjp_uAM_r5vx-N2t7FrrpyblURTKaFSrATRWXnrqZ7qb-LpWAL3OxXaaXu4lAtCir0dTKSEOH3IbgP7qoUIt-QeKwsNTJTyc-xOHsxmPccpWOyhEmA6LFl6jEHQml5fdtxZHd0LOoIBbQAHOAiHdO9LRS1X_q9cYeCUd6DPkzHkhy9HpFw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s_r01WvoZ25M99cCKZtXF6g-Pszy0G9AP4u8dl_nwVmOURwb9wUwpCXw5q7B4X8BsY0htw-dW9t6Iwz4zoXSwwMegLXKXz4vvAy-aic8LvkYaEtYQrRO5Ph74aSH7c7B0NdLWENdl1d6Y9uOB30SXFP2y1XhsAwuDERUVsgSD38s6a-VAmal6rvYFyphsIK1VM2NVPXRKZasOV70bnu2AXFG5ZpafruZBIka8lvR9A-ZgeMYOByCd40Dymh-p2UUIVGTp01bIQ4VthHRMSYR9ZBMM66KbxQGG3M69zJo0F_whJ_4epbMwbed4lJad90AZRCMHGJMBEj-xgqzQzGq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r4w50KjSPEyZbc0Fhk9hop_i2H_SX3PFOv6SYp5aWGSPFE-7CAYU1WO-LCUKKgGYJ-l5xbLJ0Qag5K_FFBh1c2C6G2f_fyhvO_VvR37oOjtyKk39LPld--3Lc0uJDlaeGiJGA8jRu2aZWUf7WAHHxU49Lb492Ajx7M6h9p2DiEff7cVdzP04jpLQtu8xG-bP8wrmMoZYoHxNwpe9ulxld04ZEJKVhlOGwo5ArmL0VKRUTD2AhfFlAlSH_NcjT_2s2gPyQPPPF-53BsOiuVGG6axy8ChunPurmboLntNar78yPJjZhuxI59s6-ZinWzUxiEGN67GLp90bOpWxs3up3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
از کیوت‌ترین عروسک ایران به اسم:
کون‌کش، رونمایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70813" target="_blank">📅 21:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70812">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedd59487c.mp4?token=qqviy15q7IEs_e7IfG8lk1W9cKHLXCD2xtTIv2xTz83e2W_HaRXP7jwayv5Tk4xfF40wh_yipuTR6B1KEFjomoQFXQbCi9zXKlZNwOMGM0i8hm04-D82GxVsIITlm3hhncaOGhmGxsIG5kEwwhAbEhnW85FovJXnTh7UAtUurGhy-sHxRdIjqt_O7bSTgFwSZvPOOjKRSMUsK7sBk5JD00wODAXLpyMr2AWriq72OwmxeLV9vM8-avMk4Dlt6ZAsHK3z2WC39cTNWbIHCsvu-FkqwSPMqbi0JRKjz4lTfxnI8UabZDiTZH6yJD-0pZFgu-605fm0FVJgDgACcyWiDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedd59487c.mp4?token=qqviy15q7IEs_e7IfG8lk1W9cKHLXCD2xtTIv2xTz83e2W_HaRXP7jwayv5Tk4xfF40wh_yipuTR6B1KEFjomoQFXQbCi9zXKlZNwOMGM0i8hm04-D82GxVsIITlm3hhncaOGhmGxsIG5kEwwhAbEhnW85FovJXnTh7UAtUurGhy-sHxRdIjqt_O7bSTgFwSZvPOOjKRSMUsK7sBk5JD00wODAXLpyMr2AWriq72OwmxeLV9vM8-avMk4Dlt6ZAsHK3z2WC39cTNWbIHCsvu-FkqwSPMqbi0JRKjz4lTfxnI8UabZDiTZH6yJD-0pZFgu-605fm0FVJgDgACcyWiDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر برا مراجعه کنندش تزریق لب انجام داده و از شدت ریدمان، خودشم نتونست جلوی خندشو بگیره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70812" target="_blank">📅 20:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70811">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruUoXL4Pb4rdGzAd4ZRAswJEcmGFREp7Th4z4gpUwt6t7jvqZcWwax3xZRDUUq0vdaf-U6CxqxProUublaewzIelRyOtyxCkKN0Mm_UaGUgaGNkJG3BDGnDd-2GrK2wNprYzVIAba6NoLpL5HUxw5hzDJ9098hxB281oGcoLJxSBaXd7XTsh5mjvW-Zl8FDhecBuZzyiv-b7ynZiKD490lfdbbaYAWAL00K6MCl_MVEB1ibKIRA-JxSpf1kCJpcIVBzw8KcXOSi-S4wuxg3P5-iOZcx29ygQ3aZPwYBiygthJn0g-YcKUss2B9-onD4TIDuKJaua66uuvbvV9riYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
یک نفتکش هنگام عبور از تنگه هرمز در مسیری به سمت داخل (شمال)، در موقعیتی تقریباً ۱۲ مایل دریایی در شمال «خصب» عمان، هدف اصابت یک پرتابه ناشناس قرار گرفته است.
این حادثه هیچ‌گونه تلفات جانی یا پیامدهای زیست‌محیطی در پی نداشته است.
موقعیت مکانی حمله نشان می‌دهد که این شناور هنگام استفاده از مسیر کشتیرانی تعیین‌شده توسط ایالات متحده در آب‌های عمان، هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70811" target="_blank">📅 20:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70810">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKOr1jNADEcY6HtUuVX1vAharedoP9qMJDW22D4OHPV3NjG4mrOMGceh7Af5U78eGtCYCtX-6CIz6ARv5kQaHJisDsAOZqFGsrIoJEgI9H4DG0SIJuc37ZQR4WewltJ6YTn8Zs7pT-y-BU5-Cl9Tc66T4xTdBgVoPxPSJdTdUQ9C3FJvZZ8teMw24_XH4hy_V7t4NSt7zS3_1TXFDWZRqjh8PJpxtk08FuufmR9L_QQd-cNShWXFHV44kymwRvmsv97NLg_o6YNFOjiOVISUM9lfy7ZYltmnhLRNgK2TKmDfyFa8efUUYjyekZQf3n7BasNzM6FYaVWWbmbvWz9CdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ برای اینکه لج کانادایی‌ها رو دربیاره، اسم دریاچه کانادا(Lake Ontario) رو گذاشت «دریاچه آمریکا»؛
کانادایی‌ها هم کم نیاوردن و از لج ترامپ اسم دریاچه رو گذاشتن «دریاچه هرمز» و تاجایی که میتونستن این موضوع رو تو فضای مجازی وایرال کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70810" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70809">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ce04d5d87.mp4?token=cnYK4NuBDnY_k4pb5I6ytGE4sfEGYcjdsR_RZCocjBKIrutipcLE2m3Dbhf4N48X3R6EJ-eY0qhdUFWQwsxzMYQwYw6bfmGNJKmPiv40bCCxRIhOcRudXo0s7Jd3wsjK4mlW_wTbOw0Sla6eSoCj10lCPSk8Hxp4BUAWesS8TV2e3ubsqcjHHdEfmttEjO_mggPYeW1U0goYdwZ1Pupc1tqqu0-4E_xvokWZE-AbnoAZPLsCeQpbLxEpqexIn8jBYnlPwz4HWBJhfLfoV9kMcQ7vquQfWDZFP8d5sd2KS0qZXpA99blEchOvRcs9XY7tzfNKsHXXB8PmGaVci68KVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ce04d5d87.mp4?token=cnYK4NuBDnY_k4pb5I6ytGE4sfEGYcjdsR_RZCocjBKIrutipcLE2m3Dbhf4N48X3R6EJ-eY0qhdUFWQwsxzMYQwYw6bfmGNJKmPiv40bCCxRIhOcRudXo0s7Jd3wsjK4mlW_wTbOw0Sla6eSoCj10lCPSk8Hxp4BUAWesS8TV2e3ubsqcjHHdEfmttEjO_mggPYeW1U0goYdwZ1Pupc1tqqu0-4E_xvokWZE-AbnoAZPLsCeQpbLxEpqexIn8jBYnlPwz4HWBJhfLfoV9kMcQ7vquQfWDZFP8d5sd2KS0qZXpA99blEchOvRcs9XY7tzfNKsHXXB8PmGaVci68KVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
حمله پزشکیان به صداوسیما:
مسعود پزشکیان، رئیس‌جمهور ایران، از سازمان صداوسیما به دلیل سانسور خود و سایر حامیان تفاهم‌نامه با آمریکا انتقاد کرد و این نهاد را به اتخاذ رویکردی افراطی متهم ساخت.
پزشکیان خطاب به جبلی رئیس صداوسیما: «این روزها دیگر اصلاً تلویزیون آن‌ها را تماشا نمی‌کنم. آن‌ها مایه وحدت نیستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70809" target="_blank">📅 18:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70808">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b978362a.mp4?token=o-I3rPqPZEND8bPq55bYVqYHBZfWBpkVNGkm2g6qkDNl5MhcKf9fsLDgp_R8FLKfsFUAxsnGMNbV8u0YXuxAjwEOxdsUtOOOclcgtKTrO-IjL0I93HN5j18kG4mZuNe935-UZ1FXX5-p2LcD8hVT5uDgZU60vBa9sv4UjtFKwdavkFEQxSYGuBskbG9t1xdxeM2CDeH45g9yxiqJh1cr0QpxV5eZ72XgbvwrbzbgT-ZrlGspZhjMZVrtwOFj8rhdv3iU0HM1e1jC19SL6XovHfAvOphLWrH60FIeyiWJvI1rXmv_lYXKbBZ10MSNJPPbbogopkUu4Dm_fzu-_aMGpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b978362a.mp4?token=o-I3rPqPZEND8bPq55bYVqYHBZfWBpkVNGkm2g6qkDNl5MhcKf9fsLDgp_R8FLKfsFUAxsnGMNbV8u0YXuxAjwEOxdsUtOOOclcgtKTrO-IjL0I93HN5j18kG4mZuNe935-UZ1FXX5-p2LcD8hVT5uDgZU60vBa9sv4UjtFKwdavkFEQxSYGuBskbG9t1xdxeM2CDeH45g9yxiqJh1cr0QpxV5eZ72XgbvwrbzbgT-ZrlGspZhjMZVrtwOFj8rhdv3iU0HM1e1jC19SL6XovHfAvOphLWrH60FIeyiWJvI1rXmv_lYXKbBZ10MSNJPPbbogopkUu4Dm_fzu-_aMGpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر ابراهیم رسولی، دستیار قالیباف:  ما تا آخرین روز خون‌خواه رهبرمان هستیم امّا پوشکی که من برای فرزندم قبل از جنگ می‌خریدم ۳۶۰ هزار تومان بود. امروز همان پوشک ۸۶۵ هزار تومان است. باید آرمان و شعار را با واقعیات جامعه تطابق بدهیم.  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70808" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70807">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUFvxa-STdN4HK-04iaVdxHH8C5rC8k_XCB6bKnfv5Jv1r5OHbHRJAb3sb1aazGX6Lih6JhLb763_CUax-4SL_CD2FbIp6_wH5TmLknCTOxNthx4wi3jlI83I4WvJKtMjNFcEayG0y__r-71qGQ_ScJn5gW5JZjF35dSEYe82r93F8RLgyHeLtHZR-97-zqQLTyFU_1VKqQtSWJVMsVi5pRgJpRrfWM7DjeyqY3gXvHuqr8q6IdhCDbMrzb6WrxOaPuEtqZSNHU2GJYpAPAZ39cNU2vVRv4yHjFH_PF2gGDg_3ubiU-mZlOGCHUr206pdlV62u0RvmpwbHao3oVR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70807" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70806">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اوپراتور های حروم‌خور ایرانی مشخصه رو بسته های اینترنتی ضریب می‌ذارن، من صبح یه ۴ گیگ هفته‌ای گرفتم الان تموم شد، آخه چطور ممکنه فقط چن ساعت اینستا بودم
😐
از سال ۲۰۱۳ تو اینستا بودم قدیما با مودم یدونه ۳ گیگ می‌خریدیم تا یماه می‌رفت، شما دیگه مرز های وقاحت و خارکصگی رو جابجا کردین خدایی
#hjAly‌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70806" target="_blank">📅 18:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70804">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZOObi9LwmXRpuW3pfgFTH1yufCaczEgUR3VAqFtwDazda5HKA18Sr9HE2m8edNGyj6z1EEOyl5EFKPuTMHEaG_kD1JQWaZpKneWDuygDHrf_H4VrSbVyfmBSpArxlp7bHTR-Z1gBfHCm5YSMspHoyotqZtvlRdp4J6re6qIHH4DjWYUo_EgZAFRdt33W5W_m7xpOolAuq5cR266ACE9rteEZR_3w_lG5NCDSfUlmzAvav25_GeQbFYwK4o2Utvbtq-fme0o3xfRaOt3_cROsQCaCSTvaRnKqSR_j9mohoxdguoufvYn8t2qq8S9HY2XYsGx4OqqAwXpGDzsMLUCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMog29yezAshl8U2ArkwOMaTXFurU9_sr36DMZK2zG98HqmkzTtRUB_zP653pEhY6_cLfsoFPX1LZPLDW19TIgEUGgXcueIIh6_ROBnltoNMrz6Rw9D-1K5hIcyarQBCowTTH6ByPSX96kUWtnumjsWp7GSbDkj5hm2Nx7VX1yaChbkMnKrIx10nb1ZaX0j8RfmOQito93nZUPszJnBN2G6FeJcPN9q8h7bNKfxLT9MDj5ehSmNw3SKkHojmeo4PtBOm4dFW3STikylxSuGEuf4EDO9DxGknfslHNSk3lh0thQny2-qgH9vIjnAILimazHQzbm7zZbzP90ag3lmQkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصاویر جدید مادورو در زندان های آمریکا که گویا در اونجا از ایرانیا خوشحال تره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70804" target="_blank">📅 17:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70803">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc84ead5.mp4?token=GFadt4rnlvp6_Hz-ImvbyP8O3GO_DOKowGAbTDC659EBuiCMla_XWpZ7oukuxrXl_9HAPUqAQ4wbwnuenG9EOW3qZGTJqquaioF8ydENVX1SqfRCUrczaCHsll7JJJhfzp1RRJZjCVGzq93Er8zOkQz6a_WANA2GomFOc2WTSZLq_CgI29Mc216cSGqyd7RmAxV44smcXnxDaZrAqWonFInIIeMTVotFa5sxSSCR7Xb1klwFl51eT0lk2-3qD0gfw9M_spxDa1K-D7ijZHBzBeYEgk5nenguo_Q-A4gkjxYYK_hifKPDUmH6oCI5iWi3lwNXo9p7GuivrBcpm9otsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc84ead5.mp4?token=GFadt4rnlvp6_Hz-ImvbyP8O3GO_DOKowGAbTDC659EBuiCMla_XWpZ7oukuxrXl_9HAPUqAQ4wbwnuenG9EOW3qZGTJqquaioF8ydENVX1SqfRCUrczaCHsll7JJJhfzp1RRJZjCVGzq93Er8zOkQz6a_WANA2GomFOc2WTSZLq_CgI29Mc216cSGqyd7RmAxV44smcXnxDaZrAqWonFInIIeMTVotFa5sxSSCR7Xb1klwFl51eT0lk2-3qD0gfw9M_spxDa1K-D7ijZHBzBeYEgk5nenguo_Q-A4gkjxYYK_hifKPDUmH6oCI5iWi3lwNXo9p7GuivrBcpm9otsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حرفای وایرال شده رحمان و رحیم پایتخت درباره ازدواج :
ازدواج نباید دوقلو باشن چون ممکنه این وسط اشتباه بگیریم اونارو
آقا کاره دیگه یهو دیدی در رفت دیگه نشد جمع بکنی
سارا و نیکا هم خب اون زمان تازه بچه بودن کلا نمیشد
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70803" target="_blank">📅 17:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70802">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5696dbdc.mp4?token=lM_gBROwCIjImdGvKNqkWM8oZzoceAThN36uzIfD8wHzt_OANxHmqaIfgTsOjSXSXJxuo9hhkSHP_ukOG3pAKDzvz3KPlGqxwFYItt-J5b0f6aHSu1xfA6w43rh7PNDfOW0Tdh9sS_lq3qQDz1lpMs83VuIxQ2Pi0SsxEwfcUvatHS6_r1bFhVNqfaMe3oNXufeulkReEAlrPl4RaW3NcF5RuziuWaZ88bs2Q3CCqE7jLS8X6CrlGHq1osyzRSeZIgdu_Es_C8_Bb-qnHU-H3gFHd-DO2UifxLcqvNyGcNVr7ooG8JYDomFX2zo9eSKLmoEK-yR_yS_XxcDTqSRoVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5696dbdc.mp4?token=lM_gBROwCIjImdGvKNqkWM8oZzoceAThN36uzIfD8wHzt_OANxHmqaIfgTsOjSXSXJxuo9hhkSHP_ukOG3pAKDzvz3KPlGqxwFYItt-J5b0f6aHSu1xfA6w43rh7PNDfOW0Tdh9sS_lq3qQDz1lpMs83VuIxQ2Pi0SsxEwfcUvatHS6_r1bFhVNqfaMe3oNXufeulkReEAlrPl4RaW3NcF5RuziuWaZ88bs2Q3CCqE7jLS8X6CrlGHq1osyzRSeZIgdu_Es_C8_Bb-qnHU-H3gFHd-DO2UifxLcqvNyGcNVr7ooG8JYDomFX2zo9eSKLmoEK-yR_yS_XxcDTqSRoVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صادق الحسینی کارشناس اقتصاد :
کیفیت بنزین رو جوری پایین آوردن که تا ۳ ماه آینده تعداد زیادی از خودروها قراره تعمیرگاه صف بکشن و موتور تعمیر کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70802" target="_blank">📅 17:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70801">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1befe3460.mp4?token=o6w0hELIi9h0Rm89NLE_fXW6uW4S-UmQg4Yh6viiHmtV4wzBlxBOL0clWXXeeJRXA8WTjNGHGZxRIQXTHbqLTOroGKwNyZd63wF8McabtiYEmHRDZlWomoohNkBqOJPvAPM4Ugsj6S57aI1iwBC320ZHhlqel2Jzamx3LdjX8wo1lYE7x7egy3jXQPHLJCApF0y0XQ8xS5Ywyvx2pb_qwe9x2Xal8KcOQhFqlBL_W5FKkIuEc6j_XoI2Q298NBOgQ0zwen1_5xs89T2UvBMaX0X-4aoVA2PAFhVCoXF_u8uvVzhGeTNANTuvDXUc7UM25QarQqL5bzxQaUIe5jsAtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1befe3460.mp4?token=o6w0hELIi9h0Rm89NLE_fXW6uW4S-UmQg4Yh6viiHmtV4wzBlxBOL0clWXXeeJRXA8WTjNGHGZxRIQXTHbqLTOroGKwNyZd63wF8McabtiYEmHRDZlWomoohNkBqOJPvAPM4Ugsj6S57aI1iwBC320ZHhlqel2Jzamx3LdjX8wo1lYE7x7egy3jXQPHLJCApF0y0XQ8xS5Ywyvx2pb_qwe9x2Xal8KcOQhFqlBL_W5FKkIuEc6j_XoI2Q298NBOgQ0zwen1_5xs89T2UvBMaX0X-4aoVA2PAFhVCoXF_u8uvVzhGeTNANTuvDXUc7UM25QarQqL5bzxQaUIe5jsAtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
پایین کشیدن تصویر مجتبی خامنه‌ای در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70801" target="_blank">📅 16:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70800">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c5ff11496.mp4?token=wBKpsXXBKjk8mPRtL5EG0EFtolQ0GWY6mdC6J3Nrt6LHtYlHDKNV6un8fmbb3pJSLeIK54IwVx4FwFJ6jx7aT-AXz8UdNlxhZdZUw45mY95bmqgZpDoEh4fWy0jNoBY21mN2wTCWp8y1Z-lkKei0PaZGElSzqWSAHf7kf5Daa-3H3fDtwEiz9ROF4Urebvf6AMNoXab3UHF7RNtwlakbENPB2TbrsgfuNElJOUzmIkK0SI6dZTwGce-GGnHrxJh45JhitVhYFxM1dlcFx54zuN31in25WjbWfl8JwxGanZ2no7nwTyE005iHTS0jveS-03AxkUmZWAed5KTu5iDhEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c5ff11496.mp4?token=wBKpsXXBKjk8mPRtL5EG0EFtolQ0GWY6mdC6J3Nrt6LHtYlHDKNV6un8fmbb3pJSLeIK54IwVx4FwFJ6jx7aT-AXz8UdNlxhZdZUw45mY95bmqgZpDoEh4fWy0jNoBY21mN2wTCWp8y1Z-lkKei0PaZGElSzqWSAHf7kf5Daa-3H3fDtwEiz9ROF4Urebvf6AMNoXab3UHF7RNtwlakbENPB2TbrsgfuNElJOUzmIkK0SI6dZTwGce-GGnHrxJh45JhitVhYFxM1dlcFx54zuN31in25WjbWfl8JwxGanZ2no7nwTyE005iHTS0jveS-03AxkUmZWAed5KTu5iDhEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دوربین مخفی و تلاش این خانم برای اینکه جلوی خفتگیر رو بگیره خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70800" target="_blank">📅 16:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70799">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fdd874dd6.mp4?token=lDjt1EYcoSiopW5NASTXJf1LQyYzaanD5aBiWZ_k3gXutva79QyEe0LgZvdtnVs0gjzHeBqL7F6bULfGoy7h8zwcAO7jzpGRs5gTH-gaYVGZG2MjIthXIgqbYqS39nxY3q81nOj9VBqMCzLp2r91UWrqyRQ8sqhDiVC8mkpzlwAR9M4OhYpXrSybbZ8O0-lT716i7vmoy7VhFzn9RUHJCN0L8VIedwJsTzBNB98fevIqn9xjAT1dkx3nIhnpdRTXlrdZcPz1rz9jZMYfxYFmj62faqeAKJ7z8Zy7XoFfLTSaejjD0YodKHvL4T9CqHFobUjYBjT1PRm8ULbsXQoY0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fdd874dd6.mp4?token=lDjt1EYcoSiopW5NASTXJf1LQyYzaanD5aBiWZ_k3gXutva79QyEe0LgZvdtnVs0gjzHeBqL7F6bULfGoy7h8zwcAO7jzpGRs5gTH-gaYVGZG2MjIthXIgqbYqS39nxY3q81nOj9VBqMCzLp2r91UWrqyRQ8sqhDiVC8mkpzlwAR9M4OhYpXrSybbZ8O0-lT716i7vmoy7VhFzn9RUHJCN0L8VIedwJsTzBNB98fevIqn9xjAT1dkx3nIhnpdRTXlrdZcPz1rz9jZMYfxYFmj62faqeAKJ7z8Zy7XoFfLTSaejjD0YodKHvL4T9CqHFobUjYBjT1PRm8ULbsXQoY0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره کسایی که میگن تحریم هیچ اثری نداره:
نمی‌دونم چی به اینا باید بگم فقط همین رو میگم که عقلم خوب چیزیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70799" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036dee7c15.mp4?token=IU1yuAbShpVzO6LSFinCVAsbULGskbjlI8nprbGvrWYEdrMtYMCa1uC9QOpNihgpaxj2Fb4pWOtkIL1qs4JKFxt2D65gnawODG5Rck9Ar0sn-ZkD5ImNeA8y592bH0JGkhbiiulVcv0v_Ev6GzTlADNG1GmKhWXOdSFH7b4FtmKQGe4hAdnS2MS6_QhHowAjHne_f1uxUEDhz64lPMgIpk3DRd_L--Fh9TbcGWpJtEK7JtchQkFcE7LEG2_rXMHLh84qBreJL1fZb9E7O2drt4ZlNscUHmI-95wpbecx-QThrDT2V41aWEwGmOhmPz8jn72bnQrV3T7DDUYPbQ4Jmw5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036dee7c15.mp4?token=IU1yuAbShpVzO6LSFinCVAsbULGskbjlI8nprbGvrWYEdrMtYMCa1uC9QOpNihgpaxj2Fb4pWOtkIL1qs4JKFxt2D65gnawODG5Rck9Ar0sn-ZkD5ImNeA8y592bH0JGkhbiiulVcv0v_Ev6GzTlADNG1GmKhWXOdSFH7b4FtmKQGe4hAdnS2MS6_QhHowAjHne_f1uxUEDhz64lPMgIpk3DRd_L--Fh9TbcGWpJtEK7JtchQkFcE7LEG2_rXMHLh84qBreJL1fZb9E7O2drt4ZlNscUHmI-95wpbecx-QThrDT2V41aWEwGmOhmPz8jn72bnQrV3T7DDUYPbQ4Jmw5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنلاین شاپ های اینستاگرام برای ویو دست به هرکاری میزنن
مثلا این ویدیو با ترفند شیک باسن باعث شد میلیونی ویو بگیره
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70798" target="_blank">📅 15:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70797">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0459b57f2.mp4?token=Ws_FBeF00ZZyqFfkUa0d0Ns1p8GX7MLeOqZc9IhF0UgGEZ8MipkHo5U49vfR8jKn2S3k9MekJ_HUCYnIf5MTUw9SQBg0RHVR_7ABeOj2WTZgDRmmSAkhCSx3d94tp622dThDFuCQUeUGPhGLZjgjKCg0iwKpVRxObTl-M_0TVtcm5PV5JJlY3CxvqYBW7a67KeUU-UH6d0OQ5SpV-slE9_19xDgYT_yuYeLObNakVATK2qGbLFk39_PFheNmBhbeSYsxn2ployz0gUDZTQcMTQdONDtGopQ_Iyjh5Z083hmQQQZgFz6vAXIIYVShKiHe5_ryE-Gp-LvfkqzUdUDt0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0459b57f2.mp4?token=Ws_FBeF00ZZyqFfkUa0d0Ns1p8GX7MLeOqZc9IhF0UgGEZ8MipkHo5U49vfR8jKn2S3k9MekJ_HUCYnIf5MTUw9SQBg0RHVR_7ABeOj2WTZgDRmmSAkhCSx3d94tp622dThDFuCQUeUGPhGLZjgjKCg0iwKpVRxObTl-M_0TVtcm5PV5JJlY3CxvqYBW7a67KeUU-UH6d0OQ5SpV-slE9_19xDgYT_yuYeLObNakVATK2qGbLFk39_PFheNmBhbeSYsxn2ployz0gUDZTQcMTQdONDtGopQ_Iyjh5Z083hmQQQZgFz6vAXIIYVShKiHe5_ryE-Gp-LvfkqzUdUDt0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
آیفون 17 پرو از ارتفاع ۳۰ کیلومتری سقوط کرد و سالم موند!
آیفون 17 پرو رو با قاب محافظ
RhinoShield AirX
از یه بالن، از ارتفاع
۳۰ هزار و ۶۰۷ متری
زمین ول کردن!
باورکردنی نیست، ولی گوشی بعد از این سقوط وحشتناک
کاملاً سالم موند
و حتی یه آسیب جدی هم ندید.
🔥
🏆
این اتفاق توسط
گینس
به‌عنوان «بلندترین سقوط تلفن همراه درون قاب محافظ روی عوارض طبیعی زمین» ثبت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70797" target="_blank">📅 14:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70796">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omjsdcxc6Eclk-IxoBGRs9eMBT1esi89_TDSa4bLsHedwxanWdWodbc0OWB8Re4wQ6Ii3pCSPisPznZQCec93LNQXvHTmooc7SWYzVpPwChw_gS-U4fV9hc-O2WJJ7hiSFR-Z-4st6qoAwNCwZ41Hdsae2rkNs54H6IH2A2DdqUfu9wsoCKXJdcmfLnSCese3ElDtTnZU8Sb7DhVDholIhLSKqP_td4qB8sgcazLDtYyVCKDxDrJhsMlJIcCx2Ljpk3mRpenlfX5dBqveoPAe3eoTHsxt5LWzeMwGXUXDcO0MSGGyVxV7oJCXZzIX6SO0Vt9u8NnRooy0arjlBctKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تصویر ماهواره‌ای از بقایای شناورهای غرق‌شدۀ جمهوری اسلامی:
تصویر ماهواره‌ای تازه،بقایای ناوچه‌های جماران،نقدی و بایندر را نشان می‌دهد که در حملات اخیر آمریکا طی جنگ ۴۰روزه غرق شدند.
در این تصویر همچنین بقایای احتمالی یک شناور کلاس دلوار و دو شناور گشتی کلاس هندیجان دیده می‌شود.
محوطۀ پیرامونی نیز آثار گستردۀ تخریب ناشی از حملات را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70796" target="_blank">📅 13:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70795">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45caa5a649.mp4?token=J8GlJKcwd5xrtzOt781hJSGbAOmq0MxpnvjT4jppQldk2wCFCRjCUffLaEbaOg51VIbAeG_NBvEtck16DHMVr_9r9NcwrEcKVAF-LHwteITm3uHw4kuxUzSwBguXx_KUNrLyPOJsS8QUGXL0oDykTBpixQPW4KTr9BboX6gbohp1ku8dEc0x-wD6vMCGYnn6cR_wNRtKMYJIO8atdhlh3peAeDVDUiQqAYo1AOaDXdi3l9IyEeNsW1myjPbSwzlzZs7bqHhfVZNeTOFjwOXMVuDST4mnq0SFGCCFXeoKwKoPzHLYv5xWKtJLIv2iQL476kz1GApQ-DrDu4tT4oPptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45caa5a649.mp4?token=J8GlJKcwd5xrtzOt781hJSGbAOmq0MxpnvjT4jppQldk2wCFCRjCUffLaEbaOg51VIbAeG_NBvEtck16DHMVr_9r9NcwrEcKVAF-LHwteITm3uHw4kuxUzSwBguXx_KUNrLyPOJsS8QUGXL0oDykTBpixQPW4KTr9BboX6gbohp1ku8dEc0x-wD6vMCGYnn6cR_wNRtKMYJIO8atdhlh3peAeDVDUiQqAYo1AOaDXdi3l9IyEeNsW1myjPbSwzlzZs7bqHhfVZNeTOFjwOXMVuDST4mnq0SFGCCFXeoKwKoPzHLYv5xWKtJLIv2iQL476kz1GApQ-DrDu4tT4oPptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
تاکر کارلسن، تحلیلگر آمریکایی:
در نشست‌های پنتاگون درباره نحوه واکنش به ایران، گزینه استفاده از سلاح‌های هسته‌ای تاکتیکی بررسی شده است.
روسیه، آمریکا و اسرائیل در حال بازنگری در دکترین‌های هسته‌ای خود هستند و آمریکا نیز این موضوع را بررسی می‌کند.
سلاح‌های هسته‌ای تاکتیکی با وجود قدرت انفجاری کمتر، همچنان تسلیحات هسته‌ای محسوب می‌شوند و استفاده از آنها علیه اهدافی در ایران در پنتاگون مورد بحث قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70795" target="_blank">📅 12:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70794">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=Z7Xw7curDCSVTE-yypmZr2-bc1ILCmrZN_KXibRd1N4o3bKKd3r2dKeY7zqXrBv41GBfSjfEq251VPr3VOikBzkl6gRjgXS9nT_1DSKJKvlSGnGp031J9G8YflPUNdXDcnjGz1hV68x9o7rrhZBUGjQufF7Iao-Fncku6VI0cjDUox0fc7IH80sUhEVuwAP7Xt6daWJeS9xzIvnZqjDL9aoLpTxTN4eM85cDc-0tpaqkZytt3kVjz-jXm5Y1FWVYuR5NiTi1haFW7owByhQY6-R5BGVgMC6BYzNuePCKRYiw-_j63wI4jYgY3AWPjJzlRq38vaD8vkEHsbgM-CfTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=Z7Xw7curDCSVTE-yypmZr2-bc1ILCmrZN_KXibRd1N4o3bKKd3r2dKeY7zqXrBv41GBfSjfEq251VPr3VOikBzkl6gRjgXS9nT_1DSKJKvlSGnGp031J9G8YflPUNdXDcnjGz1hV68x9o7rrhZBUGjQufF7Iao-Fncku6VI0cjDUox0fc7IH80sUhEVuwAP7Xt6daWJeS9xzIvnZqjDL9aoLpTxTN4eM85cDc-0tpaqkZytt3kVjz-jXm5Y1FWVYuR5NiTi1haFW7owByhQY6-R5BGVgMC6BYzNuePCKRYiw-_j63wI4jYgY3AWPjJzlRq38vaD8vkEHsbgM-CfTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدویی از روش جالب روشن کردن مشعل گاز با فلر
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70794" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70793">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70793" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70793" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70792">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq2E0BboVYMN8xHvNe3FvN5XRs1AY3Zffpw22Tkw7ySXSco2jx6-r5g2QOH7lTnF_7anPONxVLIUe6iGGuTn1km-Fid5PV9eiOKYSzH6sZKDDJMtJ6noUQ_ESIxvpbkj02wDswElIBT8xoik60xRboudPBVWjwVJyVLA1g9jngyVeiLf1hGdGK3kU5jtfTfPhC4LT6tLy_Vy6mUUb4tsvaE0xjsaVVg6KzCjYFZrssD8iQNy_yHLma7gALcov-Kds9lE__LZkbDeapQyTLCshkEkuxIIVQrLjyxAbP57pkOWyxHFvLmtpX8MZKb379WyZOSHPS183zZGOb6PCrYtYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN
.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70792" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70791">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b95ccb0b.mp4?token=UqqtuhjFXU2DA4oXd7cQCWbX9SyXa9eNS-VR5tjYDFO4QfDw668SZ3V-MNPulNKpCtb7GDTbNN6fCQs71DEqkE592mzJbjMcJR9n7vAG8ULQqwiC8FQoDh5lsirr1XQTGYNtBGExLn2M6LDCvfime0Sqxc105N1rRz_jF4q-t7piazhGSbciaKNVm9G7UJL0exvpdXQwEtdF_nG0XuERbIc7lIrMTv1_Y5XS74Iqee3F3BWqKOFQWFhZaLlc0MwqgRIQ2E-H8OuKvB3IJipTkPqsWL-HyCm017BRvGmc8BrFnajMU3RW7QXSVbqW3dCxF2_O3SPnjYUdFybiBfcK24EhJtEpQixfa3DSOVbVQ5xOVXd5w7QeSO2HGwLfIzXMeQKzRnQaoib72LPJGjdMlGLChZ9FK69RIk1Y27ynhbvq0sIG5UXfnojUUx9cNm8NXEr93XsKPEYEieZnUqhS3mKArYnVOqgmBpYd9joNFPF9dhLzW_d80FsE2-teKkmxjLqS9M6N4-LA5c2J9jCMxLNaGyLbHJVjnvj7_DH4JjTPX88t9YSGPPkiD-4R1_HrT72Ag5KXQQx3tdL8q2mRWT_OKvAAxb8vAQd39M-LmQNYVqxtJDg4BpLFvDynxnMOFjUC_DUwPLwf4qDdVxj3-nDqLoy3naCDtA19VOmsdaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b95ccb0b.mp4?token=UqqtuhjFXU2DA4oXd7cQCWbX9SyXa9eNS-VR5tjYDFO4QfDw668SZ3V-MNPulNKpCtb7GDTbNN6fCQs71DEqkE592mzJbjMcJR9n7vAG8ULQqwiC8FQoDh5lsirr1XQTGYNtBGExLn2M6LDCvfime0Sqxc105N1rRz_jF4q-t7piazhGSbciaKNVm9G7UJL0exvpdXQwEtdF_nG0XuERbIc7lIrMTv1_Y5XS74Iqee3F3BWqKOFQWFhZaLlc0MwqgRIQ2E-H8OuKvB3IJipTkPqsWL-HyCm017BRvGmc8BrFnajMU3RW7QXSVbqW3dCxF2_O3SPnjYUdFybiBfcK24EhJtEpQixfa3DSOVbVQ5xOVXd5w7QeSO2HGwLfIzXMeQKzRnQaoib72LPJGjdMlGLChZ9FK69RIk1Y27ynhbvq0sIG5UXfnojUUx9cNm8NXEr93XsKPEYEieZnUqhS3mKArYnVOqgmBpYd9joNFPF9dhLzW_d80FsE2-teKkmxjLqS9M6N4-LA5c2J9jCMxLNaGyLbHJVjnvj7_DH4JjTPX88t9YSGPPkiD-4R1_HrT72Ag5KXQQx3tdL8q2mRWT_OKvAAxb8vAQd39M-LmQNYVqxtJDg4BpLFvDynxnMOFjUC_DUwPLwf4qDdVxj3-nDqLoy3naCDtA19VOmsdaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که کلینیک بیماری زنان داره تعریف میکنه که یه خانم 56 ساله بهش مراجعه کرده و گفته که همسر 67ساله‌ام از وقتی بازنشست شده، روزی چندبار باهام رابطه داره؛
قسمت عجیب ماجرا اینجاست که جدیدا یه فانتزی‌ای پیدا کرده که میگه سرت رو بکن تو ماشین لباسشویی تا از پشت باهات رابطه داشته باشم!!
الانم این خانم سوزش شدید پیدا کرده و مجبور شده موضوع رو به پسرش بگه تا اون بره باباش رو از خر شیطون بیاره پایین...
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70791" target="_blank">📅 12:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=smMpmn4YRoNLziVvZwhAR7PG7Wv-vDVa4NCd_RVGdCl4fkrxbGfdwz1Rhhk-3aEBquDEq7RfApxlGrOuhahWxVCJxDSB4v5If6cglk49ZrGNHBm4lcYxtKYxOas-G7VtCAWjnsxLoLJtFXQv-mZ8qe7ECGNDoQlEx8Yx9pzOZSQioaFl0RAOwsNTOqZ8J7Y_KYjbR-06kCoGi04b4eZoEAIhEA9kmiSpVph4k5cCW0SVqp8en0KrN10k9G3DgHZ3eGYNXnTknj8SNE_-N55SWAn7BX9XRyLuE8TFtwGhwCGliEept9g0uLhiuvup86ujHgFF02H41V-n_DnVugkjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=smMpmn4YRoNLziVvZwhAR7PG7Wv-vDVa4NCd_RVGdCl4fkrxbGfdwz1Rhhk-3aEBquDEq7RfApxlGrOuhahWxVCJxDSB4v5If6cglk49ZrGNHBm4lcYxtKYxOas-G7VtCAWjnsxLoLJtFXQv-mZ8qe7ECGNDoQlEx8Yx9pzOZSQioaFl0RAOwsNTOqZ8J7Y_KYjbR-06kCoGi04b4eZoEAIhEA9kmiSpVph4k5cCW0SVqp8en0KrN10k9G3DgHZ3eGYNXnTknj8SNE_-N55SWAn7BX9XRyLuE8TFtwGhwCGliEept9g0uLhiuvup86ujHgFF02H41V-n_DnVugkjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش توی باشگاه انقلاب تهران مسابقات و ایونت تنیس برگزار شد که حسابی سر و صدا کرده:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70787" target="_blank">📅 11:36 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
