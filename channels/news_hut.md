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
<img src="https://cdn4.telesco.pe/file/YY-4eU9szcio3jYsSIK7XMye_jOm4spUPlrh53aQYlFe7ejE6st-wmMG3t7zWAPtrD6i5JUQsT6RtKzCuNhTW363kHclFjTFCoW4I-91UWM-xGK3m0MpXAOXtjqpBTo_feooY1CC_yyLNhhThs6nujWoybJqdUClhDqk8B-ujRkXiGFTFAiLg7b6xHWIHy5R4z5HRuYgqNl39ptnGxBjWCeG-27lynKW2JWmYWUInte4CMsQTTrpAX2IswXKc-1qWoTBqtp50Ci3mgiL9uy_rXsovP4Mv_gqP6PYYZWlrdl8csm2bclFJv9boB6aAacz-bal6nPZtMEqx-MzM4_FeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 136K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 00:51:44</div>
<hr>

<div class="tg-post" id="msg-69441">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=gYm8Zwq2tlYclVz707nAiGsy8GhAs2CUEGHYFVi6iPtLynS1I3XR3crZI8ZKrjQ3aOQBPM3nXT8UcQ3PsNhc6r9aHnfHlwOiKozwgyLf7cm7sjETk4fxPK7elk4s3uYhfl62KiTln-2w-CGwfM2QaI1NlTc0XsElrtBEBPM_snWIpb7OMr2CYCk4ImbWiznVFbFT6cQh8wK6oQldzQuvYDqdjO4r0TuQyHXqRORAtbWNuju4tG0SfenWVaXsWyNr9ToSQCpc2diN00Nwnu_-OHcvNCBXA-UGtTqhGEwL-tbBzFSf1LNPQWmrFB6jLlscGHZjYPJ9-kP262CV645iPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=gYm8Zwq2tlYclVz707nAiGsy8GhAs2CUEGHYFVi6iPtLynS1I3XR3crZI8ZKrjQ3aOQBPM3nXT8UcQ3PsNhc6r9aHnfHlwOiKozwgyLf7cm7sjETk4fxPK7elk4s3uYhfl62KiTln-2w-CGwfM2QaI1NlTc0XsElrtBEBPM_snWIpb7OMr2CYCk4ImbWiznVFbFT6cQh8wK6oQldzQuvYDqdjO4r0TuQyHXqRORAtbWNuju4tG0SfenWVaXsWyNr9ToSQCpc2diN00Nwnu_-OHcvNCBXA-UGtTqhGEwL-tbBzFSf1LNPQWmrFB6jLlscGHZjYPJ9-kP262CV645iPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی وقتی می بینه دلار شده 190 هزار تومن و آب و برقم هر روز قطع میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/news_hut/69441" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69440">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93362f281c.mp4?token=Y5NJuv7jOcFx52BWy-W5lW9nBKeO_qRyQ2kjwHvGKfDwcu1KspCPXAnMuaVN926gxkY3ZrEaELfyfT11-ZO2mExiRp4ri_4q7tR4XtuPEGirsGU_air3aGDxeowLRi1rhPn56uVxyd55XjPeD-y9npyX57XKmeklCIT1mf181OqzEY0LXBafYiJvaqM8_HIo4y6ATB2cuSdCHwNPiultJxd94ZE-zxs0NnVn1645QIuC5V3j7ofpBRvH3_JrOjh7wIcyC_de2AYfJoNdAKN9oLHs1SAoVJ_Y5hkSuCsOevYbLpIZz6sG3cI13LiXVVyqx7FTh_53FwD5oX9hzgZ5hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93362f281c.mp4?token=Y5NJuv7jOcFx52BWy-W5lW9nBKeO_qRyQ2kjwHvGKfDwcu1KspCPXAnMuaVN926gxkY3ZrEaELfyfT11-ZO2mExiRp4ri_4q7tR4XtuPEGirsGU_air3aGDxeowLRi1rhPn56uVxyd55XjPeD-y9npyX57XKmeklCIT1mf181OqzEY0LXBafYiJvaqM8_HIo4y6ATB2cuSdCHwNPiultJxd94ZE-zxs0NnVn1645QIuC5V3j7ofpBRvH3_JrOjh7wIcyC_de2AYfJoNdAKN9oLHs1SAoVJ_Y5hkSuCsOevYbLpIZz6sG3cI13LiXVVyqx7FTh_53FwD5oX9hzgZ5hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
شوت برنده در مسابقات قهرمانی باشگاه بدمنستر! از تمام کسانی که شرکت کردند، بسیار سپاسگزارم.
من با امتیاز 70 برنده شدم و از این بابت بسیار مفتخرم، زیرا برخلاف سایر شرکت‌کنندگان، زمان بسیار کمی برای تمرین دارم، زیرا تمرکزم روی مسائل دیگری است.
این را "استعداد" می‌گویند و من آن را دارم، در حالی که آنها ندارند!
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/69440" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69439">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsLd-lYl8htLb5cAZrksQQrvay1Lv9EBY74jh9Db94QYFkh6XjqyKYn0_hdEfzaEwVK7D-lOiVhQTt2fnA_vCzrpA5bvl-gFQ23IWGxaFKKDHqNiIn2PvmfOlx5pfChD1FvtdvhKRAJd1C5VZnl1X-Ywyk0Y0Z-mkkjUNKZtP55aGd_4t46C50r1pY-JoFJ087J727rsB0uLXTlXVJq-4pHTxaS1f_pjps6_XZ99aVciXsHHYCJ_jpACbdtTC_5g3Wt7Qhm_stACSFgTVcML8PJ3K4o8839ZtwvY9uZyMoiHflQIn72mBuU7va0OAjksIc4KO-TXabpxxTEYOU7Q8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پزشکیان:
تفاهم نامه که امضا شد حاصل خرد جمعی اعضای شعام بود
این تفاهم نامه ثقل روابط خارجی ما توی آینده هستش و باید دشمن رو وادار کنیم بهش پایبند باشه
امنیت کشور و منطقه و هم‌پیمانان با این تفاهم نامه ارتقا پیدا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/69439" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69438">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⏺
شکار و هدف قرار دادن ۶۷ سرباز روس توسط مولتی روتورهای اوکراینی در اطراف پوکروفسک
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/69438" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69437">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=rK8JWYgmHB_Bs9ViQ26L9b5GNCli_-ulgpQ0PUbNwJQNVT_lPtq6DEDl6VIIvw5lAAljIMx8LzsYOFevIgnBpyPwUJVMn_xDwnJWC-AU-6Jp0Eb-ZuSohxMKcBmxR9ak_5tRXuQ4kqYEna4UclJFOx-Obzp7du3IhhmablvgDJRfjxTrIvFQ2FsM6TrcIlqcuv76rzTFy9BdhfWlxOOjNH9H5uU9SNeBJoEVn1etdhJKArorV1jnWGLnKIFSag2k7mVfmJIOseePrbKjoegqncKAFNpoxM3013spqBr7PtV_zf82ftF6biI4R5BDFc7m-EFWIpO8ZhXokaiuk-HG5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=rK8JWYgmHB_Bs9ViQ26L9b5GNCli_-ulgpQ0PUbNwJQNVT_lPtq6DEDl6VIIvw5lAAljIMx8LzsYOFevIgnBpyPwUJVMn_xDwnJWC-AU-6Jp0Eb-ZuSohxMKcBmxR9ak_5tRXuQ4kqYEna4UclJFOx-Obzp7du3IhhmablvgDJRfjxTrIvFQ2FsM6TrcIlqcuv76rzTFy9BdhfWlxOOjNH9H5uU9SNeBJoEVn1etdhJKArorV1jnWGLnKIFSag2k7mVfmJIOseePrbKjoegqncKAFNpoxM3013spqBr7PtV_zf82ftF6biI4R5BDFc7m-EFWIpO8ZhXokaiuk-HG5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
‼️
روح الله قرهی رئیس حوزه علمیه:
«وقتی ماهواره به فضا می‌فرستیم، می‌توانیم سرش را کج کنیم و خود آمریکا را بزنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69437" target="_blank">📅 22:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69436">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4MEqkCzjjRRxUQUKTk4F5FCbtDXfSFKRCnFGl4cC-sDvN8UXMCxUCGjUPxkepV3cq65zN8CAD2glBg-1-BQfm3w_UH2EcmZ_etJ4r11LNVlzhOH2c43RxzEZRACq8QTIV4IdjYoWEbzYmy_FpHFIr98Y7qhEQ0Kz3CKv9kqcjDBICrj1ugCPZnZDMR4gAQf7mP1aXsD3YmQfJGWv4PylycqG3IxrF4F6VIooIH9UEDcBgBgXZT8KuupQJI0zyJQ1cbXu-FIub4Qt8_v5HBMKjDZwFr0mXmksvWOsNTlg_Co2Svjh86Xqr7KXbr64ZHpHQFOhlKC29ezIVgmNUHQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کان‌نیوز به نقل از یک منبع امنیتی:
رفتار دونالد ترامپ — که منجر به لغو حمله گسترده به ایران شد — به توانمندی عملیاتی آسیب می‌زند و آن را تضعیف می‌کند.
این مقام امنیتی گفت: «این دومین بار در طول یک هفته است که ایالات متحده اسرائیل را در جریان حمله‌ای برنامه‌ریزی‌شده قرار می‌دهد که می‌توانست خاورمیانه را تکان دهد، اما آن حمله در آخرین لحظه و بدون هیچ توضیحی لغو شد.»
یک منبع اسرائیلی نیز افزود: «با وجود رفتار رئیس‌جمهور ترامپ، آماده‌سازی و تدوین جدی برنامه‌های آتی دشوار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69436" target="_blank">📅 21:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Dd87kvz72qdAtWSt8xWvTqEzo89w9nH7ZQDBJDlP32Aqe0m_G3dNvVZj2STggXDP_oeh_IEFhd89uXhd-piXa_atmFWrgaR8VNWhNKyFXgAyHsCZJ2COa05BszJ7zT4puq3nNtm573s3y7WhpM8uvJ14ZCt34TJzQAI0gYk3P8Dfdj4spXfg8_be8kZVT4pvEvFV2Res_rU98DCUczlZK6qPMJPGYcO39RbjhT10jT3izJVWtNipaRTFieYdqHYqC1uhwxBt4Lx4z_OeCHLT4pjjje-dPOOqBk2bpD6oVecKfKFINdaxAighfzkaM7zKbgyq8vaCbM7Ej3tdfZb5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=XnEwoNsZ03YX0Z-sAg9F95uBj9FOLVnAPJm4gsKmypLsPulKdjs0NcWI-sTWvSHqHoUO0kVUBmADMofhjV3RmYB9ftRTly_LtwtCLRC3QSRFO-eh_0jDMbYO7kxkzORxBZze8Y6SrQl2Xgst2UMz_cuXWo-rkFX1cQAhvc7EJiP5MhsWhhLaU1xxO2RI66ssLZ93ERzWbrMSCE-aE9bu0uMMeBBpAu5x1T40frc8eH-CRIGhWeRXXWlVAOnepJvVoR15dJoj8ChpWy46bgqooHe7Q2YTeKK0AWVx_Hw-TmBQ4zyyOoi1FERNaHFOsEDAjmTVV2Z8hx4z6HeSPjXbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=XnEwoNsZ03YX0Z-sAg9F95uBj9FOLVnAPJm4gsKmypLsPulKdjs0NcWI-sTWvSHqHoUO0kVUBmADMofhjV3RmYB9ftRTly_LtwtCLRC3QSRFO-eh_0jDMbYO7kxkzORxBZze8Y6SrQl2Xgst2UMz_cuXWo-rkFX1cQAhvc7EJiP5MhsWhhLaU1xxO2RI66ssLZ93ERzWbrMSCE-aE9bu0uMMeBBpAu5x1T40frc8eH-CRIGhWeRXXWlVAOnepJvVoR15dJoj8ChpWy46bgqooHe7Q2YTeKK0AWVx_Hw-TmBQ4zyyOoi1FERNaHFOsEDAjmTVV2Z8hx4z6HeSPjXbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انبار شرکت Wildberries در منطقه سمارا دچار آتش‌سوزی شد، این اتفاق پس از حمله اوکراین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69433" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5208110eae.mp4?token=XbBcsf17yCuz1FT8w_LVkwbVvnseEdycyrDJv0fpQ8BrV_n46Znl5KCqsO9GRS7dNh5og60Fb89h2QzGTNIsdHa2jgkSbRQuvcxadW-DS-MZvyJw3Y89CNDPHc_pes6-TsDytw7qz63JIpybqXm9N49_qLeVK3lh-wYTjYZ9fbnBImK7SYi7bxB67JOGicrKW8sl3z86GGD4eLJbNwXqQ7ivODiokPa3bN8b9pI9U26qiLfkVXr7b2nRGgk3n3bPvD33xTn0rWOM_6qewFhhpyyZfzcaYBANnTe-L6DrdTFJb3f-4c2HI7EuK2lnxJ-l0mon7GilvHxi2BZxP0pdmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5208110eae.mp4?token=XbBcsf17yCuz1FT8w_LVkwbVvnseEdycyrDJv0fpQ8BrV_n46Znl5KCqsO9GRS7dNh5og60Fb89h2QzGTNIsdHa2jgkSbRQuvcxadW-DS-MZvyJw3Y89CNDPHc_pes6-TsDytw7qz63JIpybqXm9N49_qLeVK3lh-wYTjYZ9fbnBImK7SYi7bxB67JOGicrKW8sl3z86GGD4eLJbNwXqQ7ivODiokPa3bN8b9pI9U26qiLfkVXr7b2nRGgk3n3bPvD33xTn0rWOM_6qewFhhpyyZfzcaYBANnTe-L6DrdTFJb3f-4c2HI7EuK2lnxJ-l0mon7GilvHxi2BZxP0pdmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی امور خارجه، اسماعیل بقایی:
مدیریت آینده تنگه هرمز توسط ایران و با مشورت عمان انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69432" target="_blank">📅 20:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04acf28261.mp4?token=XEcZSALoPXZIAs2oWloLRMOIXAZ1JFxhGQdbUBPLN8sL6hqNEWYMeKS-YFNAzh_N2WKHGZEq58LGH-whfMsF17GhQNDvUgDEvUrDc0TxCUliY-ptJT20WqwtYRR4tyjbov3WSd5XeO6oNwCZPKJDbZFCIQWbjtq8CFhCQRRo0lUjaO_TzfBVWZZ0keSPut9nVKg3-FyqhbT_4P_yxBhszGfOKS7JgksE0jKe_TJoXVydb0R44u84DNo3MLYewCk2QHRP9MhrjIy2jh1oZkUKCg7W-_X9XatKEf-gn0lWKWDC5a4TuQmkcdFbUpW_DGPqhdOVs3yQCGtvghy1YdqGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04acf28261.mp4?token=XEcZSALoPXZIAs2oWloLRMOIXAZ1JFxhGQdbUBPLN8sL6hqNEWYMeKS-YFNAzh_N2WKHGZEq58LGH-whfMsF17GhQNDvUgDEvUrDc0TxCUliY-ptJT20WqwtYRR4tyjbov3WSd5XeO6oNwCZPKJDbZFCIQWbjtq8CFhCQRRo0lUjaO_TzfBVWZZ0keSPut9nVKg3-FyqhbT_4P_yxBhszGfOKS7JgksE0jKe_TJoXVydb0R44u84DNo3MLYewCk2QHRP9MhrjIy2jh1oZkUKCg7W-_X9XatKEf-gn0lWKWDC5a4TuQmkcdFbUpW_DGPqhdOVs3yQCGtvghy1YdqGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی وزارت خارجه اسماعیل بقایی:
توافق ایران و عمان بر سر مسیر جدید هیچ ارتباطی با بازگشایی تنگه هرمز یا حفظ بسته بودن آن ندارد.
مسیر جنوبی از طریق تنگه هرمز با ناامن کردن منطقه و آسیب رساندن به منافع ملی ایران همراه بوده است و تهران آن را نمی‌پذیرد.
مسیر مورد توافق نه مسیر شمالی و نه مسیر جنوبی فعلی خواهد بود. در عوض، مسیر جدیدی خواهد بود که هر دو طرف متقابلاً بر سر آن توافق دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69431" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=KOeMvZI2E5EWKnN4PlLEZnQlFm33F4zNVCuDhGfKb8KjiQt5n9xeRxal381oeCEoQ1V2zFDRHnw6WK2uxcl4OPSVzNolnf64QwLWtci7JYzd8WsBOkaPvuouAxAr1xbc5cVcMDlEdoLKK6C4iF37Gg_SbnMGu-NFZqbo0Xvq3JhuhmNKDaqmMXcv2HcpXryvoq9d0bjgE2MyWTDUJPv4vJ7ptitcZIVrR6ekByzvoNrVkWH39ACyYB7xLy-YNnfqZWdqpsuNwjMKxPnkw_CWbc9x6yR1ijPmV-MBcWWRe1_FzmFDnWbsf1gRvZqLwU6i6VSa_2ti1eicrWxK45Dj2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=KOeMvZI2E5EWKnN4PlLEZnQlFm33F4zNVCuDhGfKb8KjiQt5n9xeRxal381oeCEoQ1V2zFDRHnw6WK2uxcl4OPSVzNolnf64QwLWtci7JYzd8WsBOkaPvuouAxAr1xbc5cVcMDlEdoLKK6C4iF37Gg_SbnMGu-NFZqbo0Xvq3JhuhmNKDaqmMXcv2HcpXryvoq9d0bjgE2MyWTDUJPv4vJ7ptitcZIVrR6ekByzvoNrVkWH39ACyYB7xLy-YNnfqZWdqpsuNwjMKxPnkw_CWbc9x6yR1ijPmV-MBcWWRe1_FzmFDnWbsf1gRvZqLwU6i6VSa_2ti1eicrWxK45Dj2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کارشناس صداسیما:
مسعود رجوی (رئیس سابق مجاهدین خلق) فرد باسواد و کتاب‌خونده‌ای بود و قطعا خیلی باهوش‌تر از رضا پهلوی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69430" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=TSC0r0MbQruwXFQj5KKRoyXSJHhBrkyY7JaiMjJfNGYnnEWCkTsCe7eZ1ceobWIk293JwDZMzxg8wkGUv8dncP0_L9gzvJ5KOA9nbdPijd__Xmw3oYh5KMDt61oWyc-DGyUfu4qlRqks13pIE-vkmGO_QkADzmGIHym8HHmlm8QbEvBUSyjOreGlh_C0mf4f7aOrq7h932QjnEdg6n-BsC5EnHZtm-W9grVGQTkUnz6omctCQscz-PV34P-le3GiZ40wEORUWnJR0SqdaEzWo-A8sRl8GsF0bKU96zpXDuWbXdTK_eHfe8hYH3pC3FhyoApZJn1N7e8eM0LTRhfZQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=TSC0r0MbQruwXFQj5KKRoyXSJHhBrkyY7JaiMjJfNGYnnEWCkTsCe7eZ1ceobWIk293JwDZMzxg8wkGUv8dncP0_L9gzvJ5KOA9nbdPijd__Xmw3oYh5KMDt61oWyc-DGyUfu4qlRqks13pIE-vkmGO_QkADzmGIHym8HHmlm8QbEvBUSyjOreGlh_C0mf4f7aOrq7h932QjnEdg6n-BsC5EnHZtm-W9grVGQTkUnz6omctCQscz-PV34P-le3GiZ40wEORUWnJR0SqdaEzWo-A8sRl8GsF0bKU96zpXDuWbXdTK_eHfe8hYH3pC3FhyoApZJn1N7e8eM0LTRhfZQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
من یه مشکلی برام پیش اومد که گفتم نمی‌تونم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و غلامرضا رضاییان، رییس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69429" target="_blank">📅 19:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69426">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=TyfR0YIo30LIG7zScGYGKMHnsvvRo9DkOr5QO18o_uueq3UO4W6lwLPMCRmPoUi0bxfIlPNCvZZmy5D8lK8VR9aD4L6IwJRIa85JpVtJXBBI0FOiwK6AIIdkpQ2JPVaS4c4ukWVjM8r2Vl89EioMShtBbjODR4oU-_3F6jAQlVfAaBOH39Yz6a-6CAl-Ohzxb86Lxe4ezkXNsgHX3Ne8Rx2ozSsLdxpkJVCMnFFlXFNrMaG3_-8-0oPGoA7Lk4NhDDgXiHO26g9JtWE6lzDruyoVkHEo4aQucOuqR4I8l3Ws8-OWmB2-6Sou02CD7t1xK_mMkiZauaMlNCjWl2rS2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=TyfR0YIo30LIG7zScGYGKMHnsvvRo9DkOr5QO18o_uueq3UO4W6lwLPMCRmPoUi0bxfIlPNCvZZmy5D8lK8VR9aD4L6IwJRIa85JpVtJXBBI0FOiwK6AIIdkpQ2JPVaS4c4ukWVjM8r2Vl89EioMShtBbjODR4oU-_3F6jAQlVfAaBOH39Yz6a-6CAl-Ohzxb86Lxe4ezkXNsgHX3Ne8Rx2ozSsLdxpkJVCMnFFlXFNrMaG3_-8-0oPGoA7Lk4NhDDgXiHO26g9JtWE6lzDruyoVkHEo4aQucOuqR4I8l3Ws8-OWmB2-6Sou02CD7t1xK_mMkiZauaMlNCjWl2rS2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💋
🇮🇷
این جنده‌اینستاگرامی که خیلی ماجراش وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های
🔞
عجیب منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69426" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69425">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=pMMvXzjg5EXqNvK-ZDecz1nIgPTGXz2IhTMSP3wGlgpaHsIbWNR-jGOn7WosZKoLdpdyLC69zn3PwUtWD7A_PZ4OZkaItAY_7B7H5ithdnD07Ihj9k3Z18J98XNlU6CUhD2ZDx1tSy9VrQRZ1RNX2Z7vS2PneZHoJI-j77nfy5IdDEgBTfunuLusNUigAye-rXdm--YRRYEqyJUGnmNR78n16HvupcKoLOnWi23IPViJ33vcI09ojeo5sT2XlWGFRTjfkEQhHIJuYrEUW88NpXHR77yX9ccdh-GIjpZfpnLcFqFzjeGUOFBWr7H-YlErHNkiW0t1vBg8jHatuD3zYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=pMMvXzjg5EXqNvK-ZDecz1nIgPTGXz2IhTMSP3wGlgpaHsIbWNR-jGOn7WosZKoLdpdyLC69zn3PwUtWD7A_PZ4OZkaItAY_7B7H5ithdnD07Ihj9k3Z18J98XNlU6CUhD2ZDx1tSy9VrQRZ1RNX2Z7vS2PneZHoJI-j77nfy5IdDEgBTfunuLusNUigAye-rXdm--YRRYEqyJUGnmNR78n16HvupcKoLOnWi23IPViJ33vcI09ojeo5sT2XlWGFRTjfkEQhHIJuYrEUW88NpXHR77yX9ccdh-GIjpZfpnLcFqFzjeGUOFBWr7H-YlErHNkiW0t1vBg8jHatuD3zYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند پناهیان به پزشکیان و قالیباف:
همه پیامبران را مسخره کردند؛ از تمسخر نترسید و با عظمت صحبت کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69425" target="_blank">📅 18:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69424">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🇮🇷
بیانیه سپاه پاسداران :
انتقام خون رهبر شهید و اسماعیل هنیه اجتناب ناپذیره
پاسخ این جنایت بشدت سخت و قاطع و سخت گیرانه خواهد بود
توطئه خلع سلاح حماس به نتیجه نخواهد رسید و از همین الان شکست خورده بدانید
دنیا بداند اراده ضد صهیونیستی ادامه دار خواهد بود و پیروزی نهایی فلسطین خیلی نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69424" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69423">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=M0SrIJ2yJf5SAy99gPy0qfJ_vcEuel9LQ0YL4wlMpVNZTwdS8uCS-LNomjozvE-JEyH4Tribhnglt58eskpKIL-sY3JBZLoyME9i971RqdxItsI8akF4oMkSulyN05Bdg8QKCGdWxrf74z7XRVPFAcyR2qiCvA7mELMoRwGsYI2pPT6FXARdWZut3HLfx1XStE-p8tYmHFnSJePcWyIihrUmFHfatIVCIEVhM3YmeQQ48h--eNb0JVW34xu4gDeakuvWAls4zakfRsvqA2KPdnZ3VWYi4tSntA5XzDgmY_2nlpIRsOLeRlWJolRuB1yiC9nIp6QrogNESMkrQ_igxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=M0SrIJ2yJf5SAy99gPy0qfJ_vcEuel9LQ0YL4wlMpVNZTwdS8uCS-LNomjozvE-JEyH4Tribhnglt58eskpKIL-sY3JBZLoyME9i971RqdxItsI8akF4oMkSulyN05Bdg8QKCGdWxrf74z7XRVPFAcyR2qiCvA7mELMoRwGsYI2pPT6FXARdWZut3HLfx1XStE-p8tYmHFnSJePcWyIihrUmFHfatIVCIEVhM3YmeQQ48h--eNb0JVW34xu4gDeakuvWAls4zakfRsvqA2KPdnZ3VWYi4tSntA5XzDgmY_2nlpIRsOLeRlWJolRuB1yiC9nIp6QrogNESMkrQ_igxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو هلیکوپتر آتش‌نشانی در حین مبارزه با آتش‌سوزی جنگلی در نزدیکی پساتا، یونان، در هوا با هم برخورد کرده و سقوط کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69423" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69422">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=lq8g9JmLPkMkC5dALz2WhK-g6boGXBfx2Ft9XuLXIDIqElxw8MZPcgU1QIw42GulsDCeC14VQfsYGeUJG0h9zCYJ4JaaVGIhmBbJ9zUDGdoQN2gpyTaBbY-HpUd-8vp7mCqcYI3hPBV2wyD0lMXzePTZz1EI9iuySS5hzVoQZzRge_CG2l8a5gW-L0HeaFME1sol4ZnviNjuqsONsIFxx-ggfRsmTCKIXZ-omb_T9tXVicuToVdW4X0_bBy7odvuw3shjmylareX-UOk-JfTfQHfZ_MIkK2mA4PInXXVMHbsgDiTgVsXE-l5EiF5Fbg5W7D26IpZULBaxDnJHnk3LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=lq8g9JmLPkMkC5dALz2WhK-g6boGXBfx2Ft9XuLXIDIqElxw8MZPcgU1QIw42GulsDCeC14VQfsYGeUJG0h9zCYJ4JaaVGIhmBbJ9zUDGdoQN2gpyTaBbY-HpUd-8vp7mCqcYI3hPBV2wyD0lMXzePTZz1EI9iuySS5hzVoQZzRge_CG2l8a5gW-L0HeaFME1sol4ZnviNjuqsONsIFxx-ggfRsmTCKIXZ-omb_T9tXVicuToVdW4X0_bBy7odvuw3shjmylareX-UOk-JfTfQHfZ_MIkK2mA4PInXXVMHbsgDiTgVsXE-l5EiF5Fbg5W7D26IpZULBaxDnJHnk3LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی اینو ببینید توی پخش‌زنده صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69422" target="_blank">📅 17:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69421">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6QrJ7VTAGWkwyM0RvsO0V2kIrL6mpe_bfiuIzDDt6CQFiFwDFJF6BV8RBtV-bhes6evPhf8a7Jc5BVZ4aXbNCMDTLyjn4RCJ9XFgc53qS-kr9_fG67wGuCr_q3oN8PKqMpQf_2kFFBaTzu_eEXuFNYI4wYXiHbXkpO3DqUrZzjZ2FFond0QjJyCQ_YOL0C5ICKIRhYTXTVgs1_7poaDRQ2mIgOaC49S-WW-ipSJNTYlc5cTfPvtUHoGZAEKIysQgt3kU2pF4Hrc7mO8e7LcliytDFqA9Lprkt8dnMdMbYrXSztNV4e2ZlTRMjZ2mJHybxv03NoPoJ8RP_rhnkq7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
نیویورک پست:به گفته منابع آگاه، در حالی که رهبران اعتراضات در تلاش برای دستیابی به سلاح هستند، انقلاب ایران ممکن است «هر لحظه» رخ دهد.
چهره‌های مخالف حکومت در تهران به نشریه «پست» گفتند که خیابان‌های ایران به دلیل اعدام‌های در ملأعام، فروپاشی اقتصادی و جنگی که بیش از پنج ماه است ادامه دارد، به مرز انفجار رسیده‌اند.
یکی از رهبران اعتراضات با اشاره به سرکوب بی‌رحمانه ماه ژانویه توسط رژیم — که به گفته رئیس‌جمهور ترامپ منجر به کشته شدن ۵۲ هزار نفر شد — گفت: «انقلاب ممکن است هر لحظه رخ دهد؛ مردم خواهان انتقام هستند.»
یک روزنامه‌نگار مستقلِ فعال در جریان‌های زیرزمینی ایران گفت که تدارکات برای خیزش بعدی هم‌اکنون در حال انجام است و فعالانی از تمامی اقشار جامعه مصمم‌اند تا ضربه‌ای نهایی و تعیین‌کننده به رژیم وارد کنند.
این روزنامه‌نگار گفت: «ما در حال بررسی اعتراضات ماه ژانویه و تشخیص این نکته هستیم که چه تاکتیک‌هایی مؤثر بوده‌اند و کدام‌یک نه؛ همچنین نقشه‌ها را تحلیل می‌کنیم تا امن‌ترین و خطرناک‌ترین مناطق برای تجمع را شناسایی کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69421" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69420">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ptkphn8-Et9KcIJ8LiaJV5ea31O7KfEuomSC2REylrdLeRIuXHquO6-jQl2RSElA04rs0407NFlGceb2yhHQ60eg1BObUnel-3Bo2-MNHECGKVjUIZD55iSYXksxPVeurfl7POptFBGk6spjwSkfKyVD1CcIEV-c-JAOuab-FCSebSFBLw7hIl9fy625jzn9qJafpHPFa11S_j_9WUqP9_FxtzQR8UvWNg4X1HQ4WOR8mQji6xzZmCNcV8XjrXv2EAcemE6LmRs2QneA48sKQ_b_2Ss7Eiv348nre2m2ZWOQVdS1gP4m07Z2YkU8V21k5rTCUhf_H_yVobY7gaNPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
صفحه فارسی وزارت خارجه اسرائیل:
هفته خوبی از اسرائیل برای شما آرزومندیم!
💦
اسرائیل داغ‌تر از همیشه به نظر می‌رسد... و ما فقط در مورد آب و هوا صحبت نمی‌کنیم
😉
🇮🇱
☀️
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69420" target="_blank">📅 16:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=fga37cRtC424zZVaZ9hH84zVQbCV1zd27FlGH492C8FUKryC3tIhkZBWyWRKLi70_9HEsm8NDVHw2W3mvmHwKkS_nJ1WdZpSP-R5HidHCZlclrn5BLfjFwxiSG2XrBqmYxENACbB-Nr2fxY9w8cHP8aznug-54HzlLy-RXE2LQ1M0sGeUqSGp5UN_jBlMXRhl3uQdQTI1MRXAOVXvQbjBOyYSYKcQrrF_vfJ2ixxzfMUwQhHIJmMNK0tYavdV5rjvT3s-gAXtoWf99FIP9m2J3tgkI1T41dTbiGlAQT3eO2bvXOqat-uKMc6PEurKJgNyjTR6tYumzmWLyaXtYR3vA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=fga37cRtC424zZVaZ9hH84zVQbCV1zd27FlGH492C8FUKryC3tIhkZBWyWRKLi70_9HEsm8NDVHw2W3mvmHwKkS_nJ1WdZpSP-R5HidHCZlclrn5BLfjFwxiSG2XrBqmYxENACbB-Nr2fxY9w8cHP8aznug-54HzlLy-RXE2LQ1M0sGeUqSGp5UN_jBlMXRhl3uQdQTI1MRXAOVXvQbjBOyYSYKcQrrF_vfJ2ixxzfMUwQhHIJmMNK0tYavdV5rjvT3s-gAXtoWf99FIP9m2J3tgkI1T41dTbiGlAQT3eO2bvXOqat-uKMc6PEurKJgNyjTR6tYumzmWLyaXtYR3vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از نیروهای سرکوبگر: تا تهش پای حکومت وایسادیم، بازم بیاین بیرون بهتون رحم نمی کنیم!
چون داریم دستور خدا رو انجام میدیم، شما اصلا کسی نیستین جلوی جمهوری اسلامی وایسین.
کل دنیا هم جمع بشن نمیتونن کاری کنن، پاینده جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69419" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f215b551.mp4?token=toi1jcQXLmx3JRwX5YuN_9G76RGLBeSWQvu_SNwQbRveYgV9ubc7k8Gk61vs5QMdYec1OseZH4iZ-IAfkEmraasAn4x6XN53Df9TcYC1at6I2avZTIsMeCM0yMidJu0vXgTLXy994gpUdMr3FdwXZOwQY_FPWwx9_trvkWpSF_UXSNh--n1EcN16drQMbronvJo155jWkiC-M-HyjaB2NxxxBN1P3tpIj1L63TqpQiNMqMeZHCkVQdwicv_J0SCAK5BNKywIpHk-h9WI7KtFxa68plEWCIC2ST7IqRxbErlKE8pWqnLw92642a5003-9UcCezCHFfTZGep0NyNTJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f215b551.mp4?token=toi1jcQXLmx3JRwX5YuN_9G76RGLBeSWQvu_SNwQbRveYgV9ubc7k8Gk61vs5QMdYec1OseZH4iZ-IAfkEmraasAn4x6XN53Df9TcYC1at6I2avZTIsMeCM0yMidJu0vXgTLXy994gpUdMr3FdwXZOwQY_FPWwx9_trvkWpSF_UXSNh--n1EcN16drQMbronvJo155jWkiC-M-HyjaB2NxxxBN1P3tpIj1L63TqpQiNMqMeZHCkVQdwicv_J0SCAK5BNKywIpHk-h9WI7KtFxa68plEWCIC2ST7IqRxbErlKE8pWqnLw92642a5003-9UcCezCHFfTZGep0NyNTJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو با اختلاف زیاد عجیب‌ترین و دارک ترین چیزیه که تا آخر هفته می‌تونید ببینید؛
هربار یکی از این خانواده رو دنبال کنید تا متوجه عمقِ نفهمیدن بشید...
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69418" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d8743494.mp4?token=IeXBzw4sas3cbIize4-ZW8Xn4tK-hqkN2GCm9DvnCRtbClJhqtNiQg4kkCEjONamEvc8K4_vmyk5y4NeuK3s1wgiBuiiU83rCrhqQsp43k7MpvSFMovFEHvgFOcz8-3h5TGFQaP7FGMukrFS7-WI1KGWmx9Va0gO9C1OIVHbeH2IVtwyF9CvwUcMaa5t6_tQIi5pK2Sf_DzuuMlfEcv2s_QM4AxoS-3qep_zqfq1Oj5tYxRN5EJxPLVirfvE2j0CsYNHu51hzL1DXwmg1L1aE9hRD6OB1ExrdUOdqMk2-c-BhpQ8hK83dYGhDMi9We5OPeSZENGaMMOjSlr5Sgew6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d8743494.mp4?token=IeXBzw4sas3cbIize4-ZW8Xn4tK-hqkN2GCm9DvnCRtbClJhqtNiQg4kkCEjONamEvc8K4_vmyk5y4NeuK3s1wgiBuiiU83rCrhqQsp43k7MpvSFMovFEHvgFOcz8-3h5TGFQaP7FGMukrFS7-WI1KGWmx9Va0gO9C1OIVHbeH2IVtwyF9CvwUcMaa5t6_tQIi5pK2Sf_DzuuMlfEcv2s_QM4AxoS-3qep_zqfq1Oj5tYxRN5EJxPLVirfvE2j0CsYNHu51hzL1DXwmg1L1aE9hRD6OB1ExrdUOdqMk2-c-BhpQ8hK83dYGhDMi9We5OPeSZENGaMMOjSlr5Sgew6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بر اساس تصاویر ماهواره‌ای، پایگاه هوایی شیخ عیسی در بحرین که مورد استفاده نیروهای آمریکایی است، اخیراً تخلیه شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69417" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69416">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=VAMxtv8wEYXvcy9oJ_tnDY658fkRF15sLqv8uL4FYDaZOg2ekAjm6EnT7CAWMfSMI8ylOX24WJAFJtEh_pSH4bfkOe-0QNpE79UMglO2PBvlE4ANawjRe7QmV7N94S_KxA3BrV1VJYNSbJ_Kj0ftMdmp4CVLC67gM06_2shS4e5u-h18Zgmxx7XpUkPmQ1G0YAquam5CHuTz0nCo4QCwZme-TCiftpyOnLkQyIXl0DiipicLqef3nRh2sghi51lKqW2kOzRLXZ7CyBgeKrXDlE22X9anxQLXQR9RdM_Y0Y1i3_PUpiJdIOqPb_nh9lnFGGa0ZkSv88-iIOyA5sLgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=VAMxtv8wEYXvcy9oJ_tnDY658fkRF15sLqv8uL4FYDaZOg2ekAjm6EnT7CAWMfSMI8ylOX24WJAFJtEh_pSH4bfkOe-0QNpE79UMglO2PBvlE4ANawjRe7QmV7N94S_KxA3BrV1VJYNSbJ_Kj0ftMdmp4CVLC67gM06_2shS4e5u-h18Zgmxx7XpUkPmQ1G0YAquam5CHuTz0nCo4QCwZme-TCiftpyOnLkQyIXl0DiipicLqef3nRh2sghi51lKqW2kOzRLXZ7CyBgeKrXDlE22X9anxQLXQR9RdM_Y0Y1i3_PUpiJdIOqPb_nh9lnFGGa0ZkSv88-iIOyA5sLgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر مارو خندوندی حاج اقا دارم پاره میشم
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69416" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69415">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇮🇱
بنسالل اسموتریچ، وزیر دارایی اسرائیل:
رژیم ایران در جریان جنگ سقوط نخواهد کرد.
مردم ایران در شرایطی که هواپیماهای اسرائیلی و آمریکایی بر فراز آسمانشان در پرواز بودند، به خیابان‌ها نمی‌آمدند؛ چرا که نمی‌خواستند در نظر دیگران، همدست دشمن به نظر برسند.
تأکید اصلی باید بر این موارد باشد: اقتصاد، اقتصاد، اقتصاد و باز هم اقتصاد. این همان عاملی است که در نهایت موجب سقوط رژیم خواهد شد.
به گمان من، رژیم ممکن است به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی چنین وضعیتی پیش بیاید، ترس دیگر مانعی نخواهد بود؛ آنگاه مردم به خیابان‌ها می‌آیند، قیام می‌کنند و رژیم را سرنگون می‌سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69415" target="_blank">📅 13:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69414">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
خبرگزاری فارس، وابسته به سپاه:
گزارش‌های حاکی از موافقت ایران با بازگشایی تنگه هرمز نادرست است و هیچ تغییری در سیاست تهران ایجاد نشده.
منابع نظامی گفته‌اند این آبراه راهبردی همچنان بسته است و عبور از آن نیازمند مجوز صریح و هماهنگی با نیروی دریایی سپاه پاسداران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69414" target="_blank">📅 12:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69413">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835653bd72.mp4?token=JrjWFGmaqmlf3NvbAAomY6_zK46m4TklNO5hWZAsAJIGBAcWR65JAAVDi-xaHRfMPYcFusXtqDGM9hpzxAIFVMBhHwlh7RiQfYu-z6DF-MySPPSue1p9WauzseQ7ixHyilg-EKIZXk_zLoBvTyXEsavvFjJGSvU--d9eHrNlGYWmlJIRdKSU8kfN9bB_SV9LRszH_Y45UOjoCP2qAACaGgxbokQnGH28q6OsHQO819kTE2YjFbEKyYILUGPAho5Cq1mu1AuxsCLijbK2oUI7Wv_07p2XzGKVejOx-4upeBiPD0J6r9eW0284Z4Nn6U__pfOUF5gwfdeGbkXymJwEBUXWFcQMmojfKfzQ3c2jdG_kk2Nd5SMrAfTbtJdxAFSUvCz_2F1wbTnItZOx8hUIiMjbJNgoRh3sJxeo215TiWyVOWIruDtCZVEdZ8JMyOAsQNdZ0kfBjuIDSt3MDPtefMI1mpLNeYcEpVbeUx8QhcIHTGQJi8IH0c_5nbMZacMFxmc1yfbi7m8VeU_T0VTKdxEPJcKMQ4bdwjNJvkbKN6kdvGqScCjQbXnbZTC42LsnQux3MojsLBhQYhW6dqr3ANuiJwCYTk78I6Z_wM4VN0hoborH3MI_GQZ6WouF1h8SIcOb4hMsOr4Z32e992O_VH3H8-KCApl5ZPbCSHnDWR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835653bd72.mp4?token=JrjWFGmaqmlf3NvbAAomY6_zK46m4TklNO5hWZAsAJIGBAcWR65JAAVDi-xaHRfMPYcFusXtqDGM9hpzxAIFVMBhHwlh7RiQfYu-z6DF-MySPPSue1p9WauzseQ7ixHyilg-EKIZXk_zLoBvTyXEsavvFjJGSvU--d9eHrNlGYWmlJIRdKSU8kfN9bB_SV9LRszH_Y45UOjoCP2qAACaGgxbokQnGH28q6OsHQO819kTE2YjFbEKyYILUGPAho5Cq1mu1AuxsCLijbK2oUI7Wv_07p2XzGKVejOx-4upeBiPD0J6r9eW0284Z4Nn6U__pfOUF5gwfdeGbkXymJwEBUXWFcQMmojfKfzQ3c2jdG_kk2Nd5SMrAfTbtJdxAFSUvCz_2F1wbTnItZOx8hUIiMjbJNgoRh3sJxeo215TiWyVOWIruDtCZVEdZ8JMyOAsQNdZ0kfBjuIDSt3MDPtefMI1mpLNeYcEpVbeUx8QhcIHTGQJi8IH0c_5nbMZacMFxmc1yfbi7m8VeU_T0VTKdxEPJcKMQ4bdwjNJvkbKN6kdvGqScCjQbXnbZTC42LsnQux3MojsLBhQYhW6dqr3ANuiJwCYTk78I6Z_wM4VN0hoborH3MI_GQZ6WouF1h8SIcOb4hMsOr4Z32e992O_VH3H8-KCApl5ZPbCSHnDWR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گزارش روزنامه همشهری از دلایل عدم انتشار صدای مجتبی خامنه‌ای :
از طریق صدا میتونن پیدا بکنن چون هر فضای بسته امضای صوتی منحصر به فردی داره و از بازتاب صدا از طریق فرش و دیوار میتونن مکان رو تشخیص بدن و ارتفاع اتاق و فاصله گوینده رو از محل بازتاب رو پیدا بکنن
همچنین از طریق تحلیل شبکه برق میتونن ردیابی بکنن چون همهمه ضعیف الکترومغناطیسی در پس زمینه صدا ضبط میشه و سرویس های اطلاعاتی میتونن از طریق شبکه های اتصال برقی مکان رو ردیابی بکنن
هر میکروفون و دستگاه ضبط اثر متفاوت داره و مختص خود دستگاهه مثل اثر انگشت خود شخص لذا از طریق ردیابی دستگاه میتونن مکان رو پیدا بکنن
صدای پس زمینه مثل خنک کننده ها یا ژنراتور ها و حتی توی مکان باز صدای ترافیک ها و صدای محیط و نوع حشرات و پرندگان میتونن محل جغرافیایی رو لو بدن
😳
😳
ویس ابعاد فیزیکی نای دهان و مجرای صوتی رو نشون میده و حتی فیلتر هم باشه با دستگاه هایی میشه ردیابی کرد و تشخیص داد طرف زنده باشه محل حضورش کجاست
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69413" target="_blank">📅 12:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69412">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇺🇸
ویدیو ای که صفحه رسمی وزارت جنگ آمریکا به تازگی منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69412" target="_blank">📅 11:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=K6J4WrxtLQp4c78asx7FP3XeoRzyz6xdejcuYb6a_5dxc2j-uUY1D-95JXYrXvAgtwuy39R1c54pUm63uU1-b0vAhGgqSSABC5uSnTFOmvdcQaieeCuM0QLOVYYYCJZuGzVqzSNAlNldYXnVx2eHPy3V4uF49e7V8koNaIcgi3f_UNYahOfPH3oh6xyMMNysbxC8E46mxh0yUC5SoMTMVFgJ0VxauwUw8vFBxu3WwwxBmGPBeWghgPXYHq-D1E3qC64tAhTSDUFI3w2xuvivJGSwRRKwSr8kbOnXgnA0wbybmM46JndCCLGK6K4wS2cPph2c4uvUaiOBA9-BTJ94eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=K6J4WrxtLQp4c78asx7FP3XeoRzyz6xdejcuYb6a_5dxc2j-uUY1D-95JXYrXvAgtwuy39R1c54pUm63uU1-b0vAhGgqSSABC5uSnTFOmvdcQaieeCuM0QLOVYYYCJZuGzVqzSNAlNldYXnVx2eHPy3V4uF49e7V8koNaIcgi3f_UNYahOfPH3oh6xyMMNysbxC8E46mxh0yUC5SoMTMVFgJ0VxauwUw8vFBxu3WwwxBmGPBeWghgPXYHq-D1E3qC64tAhTSDUFI3w2xuvivJGSwRRKwSr8kbOnXgnA0wbybmM46JndCCLGK6K4wS2cPph2c4uvUaiOBA9-BTJ94eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها:
این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69411" target="_blank">📅 11:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل:
عراقچی، وزیر امور خارجه ایران، شبانه با یک مصالحه میان قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد؛ اقدامی که باعث شد دونالد ترامپ، رئیس‌جمهور آمریکا، حملات تلافی‌جویانه برنامه‌ریزی‌شده را لغو کند.
بر اساس این طرح، کشتی‌های عازم خلیج فارس از طریق آب‌های سرزمینی ایران وارد و از مسیر آب‌های عمان خارج خواهند شد؛ هرچند عمان خواستار تأیید رسمی این موضوع شده است که سپاه پاسداران از این توافق حمایت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69410" target="_blank">📅 11:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69409">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66dc919056.mp4?token=VUTrkY8AmNJGwhc6c5fR8NmPkpyt9-ZI9UE_PIfgXfsGysCvttqJ8CCI_7P1pidwKd3twXXQwGo0JBN4MV3mW3wTI2cAMtJcXJrHlPHdBML1SP1849MjN7NY77-1iLjyr0A5Sy2mD4FnIaX5pwpeD4toM5K6uHS7mLXrk04ToSKjBiunFusO8oNBVfycJOMg2wguggCaETD1ohF9MQH0g5SscHXVBgJImOyzwBqwjdmbxYpNdG4WQJCsplcyxomK3o646-YMAj1eZBjn1JZTjI6qjSP1Le6Im6YrLjbFbi4up1f7Q3mI2laOM1GP78N6x7ml4I3pD-dJChlvA8Wq3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66dc919056.mp4?token=VUTrkY8AmNJGwhc6c5fR8NmPkpyt9-ZI9UE_PIfgXfsGysCvttqJ8CCI_7P1pidwKd3twXXQwGo0JBN4MV3mW3wTI2cAMtJcXJrHlPHdBML1SP1849MjN7NY77-1iLjyr0A5Sy2mD4FnIaX5pwpeD4toM5K6uHS7mLXrk04ToSKjBiunFusO8oNBVfycJOMg2wguggCaETD1ohF9MQH0g5SscHXVBgJImOyzwBqwjdmbxYpNdG4WQJCsplcyxomK3o646-YMAj1eZBjn1JZTjI6qjSP1Le6Im6YrLjbFbi4up1f7Q3mI2laOM1GP78N6x7ml4I3pD-dJChlvA8Wq3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
با این حال، تغییر رژیم هرگز هدف اصلی نبوده است؛ هدف، خلع سلاح هسته‌ای بوده است. آیا می‌توان یکی را بدون دیگری داشت؟
🇺🇸
مارکو روبیو:
هرکاری که توی خاورمیانه و جهان انجام دادیم کسی مانع ما نشده و موفقیت بدست آوردیم
رژیم باید تغییر بکنه شما شاید تغییر رژیم نداشته باشید ولی باید اینا تغییر بکنه
اونا میخان
انقلابشون رو به کل دنیا صادر بکنن و باید این تغییر پیدا بکنه
ایران تابحال با رئیس جمهوری مثل ترامپ که مرد عمل هست رو به رو نشده
اونا هنوزم موشک و پهپاد دارن میتونن صدمه بزنن ولی خب سپری ندارن پشتش قایم بشن
از روی قدرت باهاشون مذاکره میکنیم نه ضعف
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69409" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69408">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=qBFQkw1xFqxFuw8olggR7EtfA3suK6JCuQWbrVKYh7f6CesvV8B7UG1zUWumK3qtw7ONQ05-PALBEWglg7xVE748K6osMCcKOlup0YG8aLqjB_FNK2pDcVdOZyk8KVHLNJ7E8RnVpzPd1QtQ0l2NC-yhxd6rRg1oNov1E5oDeQE6D4pvE8dF_PSUnHW5hdLZpM71W-xdqdfmn97fpnXsSySvmvT_DfPO40NKIV8IhkPQNk0gl6r_1dnGd_wWn3pJ_hsv4JsPjg1axJTM86cfFYmEvlQLVkUHMsdcsUBxOOJ4jvncK2CpATJ4yDL5JI2kzU2QOl1EiOEsanB4aBFABg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=qBFQkw1xFqxFuw8olggR7EtfA3suK6JCuQWbrVKYh7f6CesvV8B7UG1zUWumK3qtw7ONQ05-PALBEWglg7xVE748K6osMCcKOlup0YG8aLqjB_FNK2pDcVdOZyk8KVHLNJ7E8RnVpzPd1QtQ0l2NC-yhxd6rRg1oNov1E5oDeQE6D4pvE8dF_PSUnHW5hdLZpM71W-xdqdfmn97fpnXsSySvmvT_DfPO40NKIV8IhkPQNk0gl6r_1dnGd_wWn3pJ_hsv4JsPjg1axJTM86cfFYmEvlQLVkUHMsdcsUBxOOJ4jvncK2CpATJ4yDL5JI2kzU2QOl1EiOEsanB4aBFABg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مرادویسی، تحلیلگر ارشد اینترنشنال:هدف‌های احتمالی آمریکا تو جنگ جدید میتونه شامل این موارد بشه:
1. مراکز نظامی سپاه تو جنوب کشور
2. شهرهای موشکی و پهپادی تو عمق خاک ایران
3. تاسیسات هسته‌ای "کوه کلنگ"
4. مراکز نظامی سراسر کشور
5. سامانه‌های پدافندی و راداری
6. پایگاه‌های هوایی ارتش
7. مراکز و نهادهای حکومتی
8. ساختارهای سرکوب (سپاه، بسیج و نیروی انتظامی)
9. مقامات و فرماندهان ارشد باقی‌مونده
10. مکان‌های نمادین مثل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69408" target="_blank">📅 09:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69407">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=t7Xx-rFRC9O22-7XGm7zb6x2kn7r24I8YL_6I87Ii30o6qdJnRspxYIhP61TzdBZKiyPM_AY9lgy2a429w7jtp7lbjqcGqoHCDVPMf5ZIUr81-PqvTNYFAb8Sl3Tm3SELN8WKNRHNucaFdgBH3nNUe4kNrxM-q9xSyCxG3PPEpDvnpORcjrTQd4fpIOq6PajaLKBymYl9TbBy56Fzbi-ES709SWkKv7GMRlVA276Po_ztF_hjyGfYyd9_rY8NEqs19rPnXX5n6eGuOOj8XGuHi5eGOQc4CTwELt9AhyGrW4VPTIBD-GShV-H221X-RXXqajHL1D6PIGHBqkUq9T_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=t7Xx-rFRC9O22-7XGm7zb6x2kn7r24I8YL_6I87Ii30o6qdJnRspxYIhP61TzdBZKiyPM_AY9lgy2a429w7jtp7lbjqcGqoHCDVPMf5ZIUr81-PqvTNYFAb8Sl3Tm3SELN8WKNRHNucaFdgBH3nNUe4kNrxM-q9xSyCxG3PPEpDvnpORcjrTQd4fpIOq6PajaLKBymYl9TbBy56Fzbi-ES709SWkKv7GMRlVA276Po_ztF_hjyGfYyd9_rY8NEqs19rPnXX5n6eGuOOj8XGuHi5eGOQc4CTwELt9AhyGrW4VPTIBD-GShV-H221X-RXXqajHL1D6PIGHBqkUq9T_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
حاکم بحرین:
حضرت محمد (ص) پس از قرن ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگه به بحرین حمله نکنید.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69407" target="_blank">📅 09:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69406">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s09093O-_hNw6MiFoJRxHd5y2dh10ROsfoQKvhAlfeJoVx1lr-hjVTGDiAt7beVCHE3l1dDW1RJKW5tqc3djfma_qoD-ExHHwc6a4H80Hrq1FFfyPOzUM3RN-tFnGsUu_PGXpXqY9ZgacHwjuvLGLMT_-dFqxoZ78JRjBWResRBcSp4lQBWcYA6y2_LHW_TgeSZqNQHbw3qh4GHc_6QU2xJj4UTgyA6-CcpbxYpGOU3O0hSnEGL8li8zydLmc9viZ0QipO44N0fHtsXHMO_BDbUleUDSXkhXg9q_W5TDVsraPf1rkJxvmcLDJ7QNaVNdTirc4GIZIDt-W8u3M2QI7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حمله رو کنسل کردم
!
ایالات متحده آمریکا آماده و مجهز به سلاح است تا علیه جمهوری اسلامی ایران، در سطوحی از ترور نظامی، قدرت و صلابت که از زمان جنگ جهانی دوم دیده نشده است، اقدام کند. با وجود این، ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب توافق‌نامه‌ای که مورد توافق قرار گرفته است، متوقف کنیم. این شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران می‌شود. بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافق‌نامه‌ای دست یابم. کشور اسرائیل در این تعهد به من می‌پیوندد. همه دست به کار شوید و آن را انجام دهید. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/69406" target="_blank">📅 06:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69405">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTbWcFqK-wmHBdHOLMQ9B2GqQyRSlPacvcSruz2BUlnwKCqTxddm3s22crvxW9bxiuc_187DWnfFLjEqsMpomKx_F0fI_3ai0SSlnWODZMrjhv3Xf0hi-ToPbyk2Ld9R3UoIJflB19raPq696XBKAR1S6zr5uMLbhool2cPSYSssazbEE5uKhxRAjrOX7i4fCfbocnB1dhTBkAVRW6SDLbaAze0_MLtTRej-_t43zQ-Bw8dOCF_x1Z32Xq-5GyGs4aHzdI11Xm6QwA-kr56EVARlGBcFqzXu0RrTL76OzNWglejlc5CDRa2aX2KftGRkaINyioolzYI9zfIVbjZSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیکه و ترامپ چیزی نگفته.
#hjAly‌</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/69405" target="_blank">📅 02:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69404">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=DwFe2LHFEqJsgnLtepq1V2nYsD8chLLnyTkHVmPhn0hzvA54TBP2unxcAP9-qaR5w-X8OX6CM6I3e2Y4K652cOZI_R9X9OWQKRGpSLftGSxJctTkmsnPSCszYWtOTqc_-uHirS94RwMSB_bWJzns1Ls8cTvonxgAQFHL0SGWEZR1aF1hEH0iurHx7nTzIBVaWsEyPTcKL4qEC7XSBo3SrJuZCUjwrG5MlxW2N54XkdQ3V-iW2M2Se-fcwED3ujIzmNGadb5l23xArRXhW81ygf9lc9Yhe5buwO7C3TSrOZOEtwmH9VwfEEsn06z6mfnRkqVRHBTo8xo5tTFlhAPiIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=DwFe2LHFEqJsgnLtepq1V2nYsD8chLLnyTkHVmPhn0hzvA54TBP2unxcAP9-qaR5w-X8OX6CM6I3e2Y4K652cOZI_R9X9OWQKRGpSLftGSxJctTkmsnPSCszYWtOTqc_-uHirS94RwMSB_bWJzns1Ls8cTvonxgAQFHL0SGWEZR1aF1hEH0iurHx7nTzIBVaWsEyPTcKL4qEC7XSBo3SrJuZCUjwrG5MlxW2N54XkdQ3V-iW2M2Se-fcwED3ujIzmNGadb5l23xArRXhW81ygf9lc9Yhe5buwO7C3TSrOZOEtwmH9VwfEEsn06z6mfnRkqVRHBTo8xo5tTFlhAPiIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان سلیمانیه
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/69404" target="_blank">📅 02:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69403">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=kCvLolWW8UTbQ9Ll5gAaPbP-Y_okmGfprtQPPy3UN4UW3ZKEVh_ZY3mr6gGqdLAcP6lZAqg55GBrXRCfMC5-TFhSfWlsowT1MG1ybPsELfZOp9bbBKA3lkF0Ay5CiP_LCBkk1o2TXa6y5NbYRHv_ht4DJGDRtZxQaqqTgFr3q7TL7lkkT7y0SjxiiIVz09enD6T0kPMRY0Gqy1bwG1mx6j9IZDg4QmiyIuYgNTtootdt9TWe4sd2VL_kPdQMK7h6AfGtAP30jv6ZTC1eUdWn2iQBZgewAqrvEOT3eMwSR0VGvkW7vGTI76ztIOPqkIrt63lhbi07-C92zO_6bz_3xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=kCvLolWW8UTbQ9Ll5gAaPbP-Y_okmGfprtQPPy3UN4UW3ZKEVh_ZY3mr6gGqdLAcP6lZAqg55GBrXRCfMC5-TFhSfWlsowT1MG1ybPsELfZOp9bbBKA3lkF0Ay5CiP_LCBkk1o2TXa6y5NbYRHv_ht4DJGDRtZxQaqqTgFr3q7TL7lkkT7y0SjxiiIVz09enD6T0kPMRY0Gqy1bwG1mx6j9IZDg4QmiyIuYgNTtootdt9TWe4sd2VL_kPdQMK7h6AfGtAP30jv6ZTC1eUdWn2iQBZgewAqrvEOT3eMwSR0VGvkW7vGTI76ztIOPqkIrt63lhbi07-C92zO_6bz_3xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات سپاه به‌ سلیمانیه عراق
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/69403" target="_blank">📅 02:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69399">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZZpaHFq1WJf3wUvz9j_SqxjYNBdtXjSbSGpJjhDlg-ZcUR2uPVLP9Tg30gCSz-SZ8FkIgqMa0-o8t55Sd04MG0eirUmtVppTocc0IrgnpqXHjIZN6D3sT_VIk9Ao_fy1K_5azdHNWHrGkPGM75wePaIEuwZQQVQc9rfcnln35o4_hyrWz8ViJ3AKENtOe-5uGd00m8-gyfh4YYXpC7rRlZ_0TqA9ZqWII_RX2OPYKzf1of1qZfw69vm_ektA85Gx-w8leL6zGEFCcbRFMcj4uxtIP1OrzwMF2iQfgZi8d6b6HwBtV9EAyYmtl6gRbcqrjXDTuDGISKYhccp3PGXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tME_uG6_SgkzPmhJACwXCgGWGKH6eM7mAaoPWJCmjGCTQPJOHy9yDoxO0v3JNF4YQlk2iBaq1upfQJ7AySp4xr9YUTzYyGMwMttXaW76LQDrdRk6I0ei6lZfE3ebfFoHAnnFGHBj8WFnnDwPb62ntQxprb0nCqwITyUo3zC8eTBAfLnNoIwaU5ANPkSfaNC2RYJ8uwI9aeHAHro2bzz4GUoxV2qeB0p-dJRkrXM33qP2tvBh_SfzEouYUHM_opup8RcpQ7Ek6bQUYIibNpBbdnzNnyqNdTmhntVNxOCmcKP_oot9abD3cL0_KGi1cn2x6RdIsWkiosrAwkGpGEtyXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=ouZuCmTRrUngWDR4lZKnD6RGL61I9h3M3VHOmGVHhM1bdYwyvUsG8o0RJ-dGCnyWTtNTW-gR6Ex9VMo6s7J8EKgUb0QL8c8CNQ7iAy5VC-7PFOE4C49ZGjz-FquM1xP3_48QDT5Ikp1orvtHVXzucEsC3b-4Si8Lqx5V3ZCat80Oo-hKfwfZjtLD0-kTDRnuUNkAH6HpowNLoiwUy3rKbO0YPEtc7S5lfYJ47culORXYKmQIv_96sqzqgK1YTfD6R06RGGhRDvyfw0gcUVMFQR-M94nDWaUP-8sBSQMUZGp4MCuuqtH9p-zyvECglMmaVk5owNCLWSO7rEz7duNErg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=ouZuCmTRrUngWDR4lZKnD6RGL61I9h3M3VHOmGVHhM1bdYwyvUsG8o0RJ-dGCnyWTtNTW-gR6Ex9VMo6s7J8EKgUb0QL8c8CNQ7iAy5VC-7PFOE4C49ZGjz-FquM1xP3_48QDT5Ikp1orvtHVXzucEsC3b-4Si8Lqx5V3ZCat80Oo-hKfwfZjtLD0-kTDRnuUNkAH6HpowNLoiwUy3rKbO0YPEtc7S5lfYJ47culORXYKmQIv_96sqzqgK1YTfD6R06RGGhRDvyfw0gcUVMFQR-M94nDWaUP-8sBSQMUZGp4MCuuqtH9p-zyvECglMmaVk5owNCLWSO7rEz7duNErg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇷🇺
ساعاتی پیش یه انفجار تو یه رستوران تو مرکز مسکو رخ داد؛
جایی که به گفته منابع روسی، مراسم عروسی خصوصی با حضور چند نفر از فرماندهان ارشد نظامی در حال برگزاری بود.
کانال‌های تلگرامی روسیه می‌گن "الکساندر چایکو"، فرمانده نیروی هوافضای روسیه هم بین مهمون‌ها بوده.
گزارش‌های اولیه حاکی از کشته شدن دست‌کم 3 نفر و زخمی شدن بیش از 20 نفره!
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/69399" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69398">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⏺
المیادین:
بر اساس اطلاعات بدست آمده، گروه‌های کرد حاضر در خاک عراق در حال آمادگی و برنامه‌ریزی برای اجرای عملیات علیه جمهوری اسلامی ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69398" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69397">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/69397" target="_blank">📅 01:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69396">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=tDjZBT02CoFLAhF9VLv24OJ6BxrLEZgfW6lFLfh6dAe9xFAJ-kwQxCJYw2bu69nvvDvNUxo7_GOhMRMW2FDZho4YbCSUTNmHw9qOJUDqRUJGKvwgBbCS1qIAOfPxBK1uypkvpQz9FlOUV_BJm0TVBxo7uGTH98T-r-Wqv4cKqRFD_eYC-AMETpUVyuk9FpMWE8p7VbLWFx7ucXPR3ve-7Ts02BxHi4hPr_Uw7ljhGpMC8KJ75ZvF9r7ENLJaEMDZHSVdRMxMZ6F4H7pVVbLWm9szzfumBoJXk84zPHGuSuHYYI_VDLzmbeJXPLDTGtIOhxRvje7unc2pm6NrtpXtXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=tDjZBT02CoFLAhF9VLv24OJ6BxrLEZgfW6lFLfh6dAe9xFAJ-kwQxCJYw2bu69nvvDvNUxo7_GOhMRMW2FDZho4YbCSUTNmHw9qOJUDqRUJGKvwgBbCS1qIAOfPxBK1uypkvpQz9FlOUV_BJm0TVBxo7uGTH98T-r-Wqv4cKqRFD_eYC-AMETpUVyuk9FpMWE8p7VbLWFx7ucXPR3ve-7Ts02BxHi4hPr_Uw7ljhGpMC8KJ75ZvF9r7ENLJaEMDZHSVdRMxMZ6F4H7pVVbLWm9szzfumBoJXk84zPHGuSuHYYI_VDLzmbeJXPLDTGtIOhxRvje7unc2pm6NrtpXtXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/69396" target="_blank">📅 01:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69395">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L99cmWi2IdGgL9aVt4luzqUqWHEHbHzncPnWrLuFSGSQxUL9tWoo-funitVl_5Rz1HnsSazfmyDTI5EaFurAdmaSaWW6blccodPVCR_j43sN5FWx-u9_u9ECXBADmcGkHLZ6fNXBAlhabvRSeteZDQz5x1DWvmHxvP71__qij_HDhNMNZion41da4sRBG070ND_Mr6RQrZefBxjZS2o2y-k97QQ_hfIDNhg3eG1lgTyjK5wA6yCNkeWOAZ1f4YHBsvoW9EKbYqC5EYQsa5zrTBXzt-ieI2ofUMbpzOPl47n1iKT4byrlqEA9SFdk9TIY3BODpvWPcv0KV_7gYvpvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
توییت اتاق جنگ اسرائیل و اون ساعت شنی معروفش
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/69395" target="_blank">📅 00:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69394">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=Ar5PxQcdH4avyAwkVZ1L-GS8x7-bfoVfHMN57R_EeozZrfUlGtkLv8-tD-VWIXDi4Ed44rZRcQvvNqBgt3UE6xCGK2mNB_XkqiDzxMtt71oia7ijYhhXIPh7Fgb_8yrcqt8lD3yLjBSXRfeuMVq4h5Pe4UeAAYjymUNdcHjGSWB6hfLmQ3R3QGCBEmXW-rQjkaCprsgfYGoj3dWClV_T8gB52Q0Zqfr5SWELkFrnLmaJXE762vaB2sCEhDjGL8rIuVovZITMMvR7vAgHKG_joq2taMiHIGKY9eijNM-lbHLhicPG0zq3Zi15EpOgsPvA2dc0qtOYiIne5A5a4T-bVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=Ar5PxQcdH4avyAwkVZ1L-GS8x7-bfoVfHMN57R_EeozZrfUlGtkLv8-tD-VWIXDi4Ed44rZRcQvvNqBgt3UE6xCGK2mNB_XkqiDzxMtt71oia7ijYhhXIPh7Fgb_8yrcqt8lD3yLjBSXRfeuMVq4h5Pe4UeAAYjymUNdcHjGSWB6hfLmQ3R3QGCBEmXW-rQjkaCprsgfYGoj3dWClV_T8gB52Q0Zqfr5SWELkFrnLmaJXE762vaB2sCEhDjGL8rIuVovZITMMvR7vAgHKG_joq2taMiHIGKY9eijNM-lbHLhicPG0zq3Zi15EpOgsPvA2dc0qtOYiIne5A5a4T-bVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمود احمدی‌نژاد درباره دستگاه سرکوب جمهوری اسلامی:
نیروهای امنیتی خود افرادی را به میان معترضان می‌فرستند تا با ایجاد تلفات و آسیب به اماکن عمومی، بهانه‌ای برای سرکوب خونین فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/news_hut/69394" target="_blank">📅 23:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69392">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mB-J5mnXMtISeOqO9RVjY2LX0zc4elwcnt9RCYBZ7BUKCePEb5i91W3m6nTUyiOqs-sUG0zxVKzjCTLhfnIpq3MIXOf4KgyOPo_411tpN4DMgG0Tzxonn5PW_MAK416ldELXo3r5_QWAuVrBkm5T0Tuok3TiKPs3aq0Ugn9DtstDVbnHE0Re1A2XnDWjRnkHTk32MDhJHU9jx3k_Vka3jErgYmpNGthBEE-mRAuHy5y6sYZzg0kJY7xkE4tqObiUk1du-NJCB1MHdbed1acyxB3cGuJHw3YWZVeTnVMG4NO1sKVcQfy43m_I-szb5tqjbG1tBPc1d7Uw18kZUa3fOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=r9kWyG5Zboxyy1qMQLccJ_ISV8TqM8M0c7KBp6mhwI79j1M1ReCn4nHMKaGeFMFmoBFRE5RGw6cDc-jcIRBM_KVOwYnei9u1fApCMyN6ybNZArwM7vqC0utMVqtON9X0vFeOP1W6mPhn4wEGVLEo_7GDZBPgYdsKE1UQFu3qVsVXbzNr5PPI14nZgpfsPkp1ucMMYWwKgnYZ0lDv8LY0hiz-WM9J3dzSF9aOSEnJrsqsNdcp40vN6mf1orgu2HyOuWPAwjCKS-i837L74zAlH1r6KqznQBn6KjrEUuL88OFmeWIr4ZQAKG6q1MCoFdtjOPZ3FMTjykPQVzrEFftqug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=r9kWyG5Zboxyy1qMQLccJ_ISV8TqM8M0c7KBp6mhwI79j1M1ReCn4nHMKaGeFMFmoBFRE5RGw6cDc-jcIRBM_KVOwYnei9u1fApCMyN6ybNZArwM7vqC0utMVqtON9X0vFeOP1W6mPhn4wEGVLEo_7GDZBPgYdsKE1UQFu3qVsVXbzNr5PPI14nZgpfsPkp1ucMMYWwKgnYZ0lDv8LY0hiz-WM9J3dzSF9aOSEnJrsqsNdcp40vN6mf1orgu2HyOuWPAwjCKS-i837L74zAlH1r6KqznQBn6KjrEUuL88OFmeWIr4ZQAKG6q1MCoFdtjOPZ3FMTjykPQVzrEFftqug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا کاظمیان از حامیان جمهوری اسلامی در انگلیس که کارش زیرآب زنی مخالفین رژیم بود، دستگیر شد.
حالا فیلم لحظه بازداشتش رو ببینید که پلیس اومده بازداشتش کنه، میگه تروخدا بذارین زنگ بزنم پلیس
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/69392" target="_blank">📅 23:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69391">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=eolZUXCE3TZ4OfXc_8LW6wAV3-eRtCOsiYCP2sK5-2tGyp-0ooe0bZmRL4NKuN08TGJEm6Ub1we2DsbPQDAjwrsDOel51vtCa425yaVmpPEBXeyF2VJGm47LWu4xhXc8z2Q7T6C6SDJyJKXNpr3Gw_1fKOtjlYW18CGHjcTtTKntdcqRi5lsp7b6oHaXsXP2T8J5fpT329fUnR-471wxszImbrDS03XJTljLmTa1CCSiv2IFY81uJE5n-8toViUvcrI3KXB8hJFvdY0k9uTnLeJN2yoIBzKp1nfPBB8X6jy92pWWKlhoKxlx2L37xFYIbEC3hd7Px3zFX3k9dS4d3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=eolZUXCE3TZ4OfXc_8LW6wAV3-eRtCOsiYCP2sK5-2tGyp-0ooe0bZmRL4NKuN08TGJEm6Ub1we2DsbPQDAjwrsDOel51vtCa425yaVmpPEBXeyF2VJGm47LWu4xhXc8z2Q7T6C6SDJyJKXNpr3Gw_1fKOtjlYW18CGHjcTtTKntdcqRi5lsp7b6oHaXsXP2T8J5fpT329fUnR-471wxszImbrDS03XJTljLmTa1CCSiv2IFY81uJE5n-8toViUvcrI3KXB8hJFvdY0k9uTnLeJN2yoIBzKp1nfPBB8X6jy92pWWKlhoKxlx2L37xFYIbEC3hd7Px3zFX3k9dS4d3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کانال 13 اسرائیل:ترامپ تصمیم خودشو برای حمله گرفته؛
میانجی‌ها که آدم‌های خیلی خوشبینی‌ان و همیشه میگن راه مذاکره بازه، حتی اونا هم میگن حمله‌ی آمریکا از هر وقت دیگه‌ای نزدیکتره.
آمریکا هم از طریق سفارت خونه‌هاش به مردمش تو خاورمیانه هشدارهایی داده که اینم یه نشونه بزرگه برای حمله مگه اینکه ایران همه رو سوپرایز کنه و برگرده به مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/69391" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69390">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⏺
🇮🇷
نیروی هوایی جمهوری اسلامی هم از دیروز تا الان مشغول آماده‌سازی خودشه تا در صورت نیاز، بعضی از اهداف تو خاورمیانه رو هدف قرار بده:
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/69390" target="_blank">📅 22:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69389">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkrCxrp40tLuHpqIQffzboRPwPzOYHYJQ2YBhM9vD5wsqVEhnVI7ZyBwYRzQRZl9IQV1g9G_yTE8lyW2noJW0fq5aDUlBi02r1TwFjbneNsOTm4XkvsWXYRBOAa6g7YXmOfJRFbECGX1FKRrqJyuGTi-hG6LNJ7n0B5A8ix3jercIpjaXzU0KHKxo0iFc-pmuaO0ay20p138FvedM3JTyeQB4M35xren7P5kIh9kqp3n7dp8bB4lOcSDiexqDWToKuHg4jefbLIYYxdrar1YuB9a_pDU6LsDz3ybgX5658DNKz8k235Ne7cYabFE8tHgysh_HbH1WGO8dR_7Ocvm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/69389" target="_blank">📅 21:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69388">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsznZO83aRb3MD2wpfcthE_7_RNATIUeetz85IAoODNp6lS87BwK1hbUq62j4ptCICL2lGgiC3j-TLbbUc8jhEHj_WPN8bbw2T7eW-KTs47bf4ACvn2Gswc2_LW87r0aYtRhWFV-36yuMRUFINCU8jRsxPhZ1fMk5PDLW18vf3iJ65Q1IuNj6uXvRdFMIofmqJ9Yd354bPgye6aAryhm_zm3z2ixt866QR16mK7k2QyJm2iRHx14UpmgC1Omfag_10fIUEAILYeL-9CfhRtD24Ju6-EUwG1l8lh63887_1EwaT4RZGYiC-bb5N3tVGWASethGJCnsq1chwG_7JX08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/69388" target="_blank">📅 21:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69384">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rzbgp8pZduslZNOveAfExGv4vQKRepTeraMod0QOJNL2ZMp-raTO53w2hgmuZblgUzvgQwUQt4niXFp2n5bN3MEKRIRnwhM9myh765TkriIR0-6OTja9gT7XPHb_7fN7IXc0RlsvgOacICmZw6PFQvohKU4yvf2vCJZVtFhScyrZTlAosGJyMAUM_TxW18D8-Lys9O3PtY4IvxYD1HEypv0nLets8LHcWHLMCT2SyTVcSuWquIi615_7U0JFOFo24diB7OdY9_8v_-nanEJ931VzAHG1BT6U9HBIvJK5JAuQRidKVMHx2XHkulCFY8AWG2esjhpPb2kmJsp9iOtL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/paBqBNm1Bb_odA5A_amF_JpBUOE7xDSCtw4YpVkO0CFboT5ooZvz_4QuI53jjZbwqXvr6peCtA7fWx1PNY9I_XiHXeXwdL8XO0P8PIVgxV-lZ1JTfkCK-4n9ZAaiOdJu_cBtZ7nDvPuiQ-79X5YR6lHrj-hheuHss-SrKajYN3H93Lat6kHvt6PFJa8dsVusOKeNbjB3JUYl9AUEvZgoCR62uvVQaQTHyDRIRK05-bwlK_0zuTnBGtQIxSCv6_3cJSJAsK_2nSzy0C0HkF3EP4_FP4dvsfII6ot4Rlzw6qK6sBGOAI4ZYhKzE3Zl4VqcwLlwXrLrRV_N_y8Qp1lPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mk2mUOeeUU_0I6tWnRCJ8OqBfLkfO0XyHcoELLEKscvvODrN9eR0E2UPMVmRuznB0XNVpKAN63oFVaYp96kZmHNBpZk3ch19i_ok0_wr7gZRLnQJQt8-j-hrxkSbmorGFdDzIk-sG6FOBbkYU_x_TI0DU1kAqMSsjWjOELeBYG1HO9of--0VlCEpFrFaI1oE6AaAbb4CbfCQWF9DAbRUoz9xE0t_1eKvKh7a1CHzWZfksPdrgOmMokbFDr9R4OXVQGHw-xBT6N9EX_1jkRmU11nzc4cU3oZ2KfdMGC_uo6B1lzfS4dREpC7JwFU8hFjC9VX9he5g5-vTXMwcYowkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSJagFF22U9TmRTSyjGJmnR4m4kPC8RnNx5tj-fu6QDBJ0038GP8AEKETds_6oinjlRBG6j5ObBC77v2JjKj_BZCZRy8JYzXedDjtT-Etis3OpIu1XYMwvmMcxsqTJZur5fKapj0-XHnMWolDz1Wsblz6hswB-eW--hbApMbBcCQpzK9VT3utOLKfbE-UuKn6d49bYkADoqwccaJR-mQciw6-9N9fN2XVE6XI2ma43uzg8ZLlHxQHF5sTcO9v37r4M1Hji5tmRSTA2WOTg99yPaDHA_uc6we-5VgRL6VuxsxLeSM3WJCQp6OZG3wCB8CFk_LRLb2Llc4ldbvCONXgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
پست های جدید ترامپ
از تصاحب گرینلند تا جنگنده و انهدام ۱۵۹ شناور جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/69384" target="_blank">📅 21:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69383">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-xIG9ENy9O02lIb7dCSpYmsRQXejW0jMxs2qvhek2TWUhLvXKm9cBQ1wzxD7HuOsxyE64sf3WruET_wKAnB3CPkN9yke0mvsORKw6Od9HS-5ogiwgm3zoMip8kCRT6CaqVPCHfbxsgurMWwwotlc8jY1kf-tpGYMF_-o9tI4iIY7BxGqTAGD-LYWQeTP1pE740zIomWFygNCP2F7DaOT0RGouZlpHC1RNFZGfadbEqtqMTyGdkfRFlHl_VRacICfTntBwho5pZri5wEPRN92rY6i6w4uSXXN7VMPXS9kvQmpF4mJwkCJyrFc3z6a5VAm89FVDklP2VmDStaQsO-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69383" target="_blank">📅 21:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69382">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZinJbPCy64hGhpcUim0rn1jn_erWOU-cuO8NM33O-lZ9jwcvu8E8VJDrnwFIDVJwkGxy_b2iWRTL1eJxlW16qjtInX_RkQwM-0XgAfTU8PUloJVlCasmYQhPC63khZiszJrIqxPjPFKwMZUFK86RD6Kh7qTNfBW-htV0EtzXs0knA162Rs8qFsUnD9Dj2aWmv1WjgUizItf5UU6cNAe7N8a4oS-sBXqlza0DGT_obWa4HAQoIDgPpDN-Ea6F_Tfi9OECP6woirTgdgfv2ClVag6zmo22bb7c8kFwcqh8aGPwUh_03oefDARqKcxwE4NCyU5A7B3PXgtCcYaJwdyhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
بر اساس اظهارات رژیم ترامپ، کاملاً محتمل به نظر می‌رسد که پس از ماه‌ها تهدیدهای وحشیانه، امشب آخرین شبِ وضعیت عادی در قطر، عربستان سعودی، کویت، بحرین، امارات و احتمالاً عمان باشد.
اگر حملاتی علیه زیرساخت‌های غیرنظامی ایران صورت گیرد، زیرساخت‌های حیاتی این رژیم‌های همدست — به همراه زیرساخت‌های رژیم صهیونیستی و شاید اردن — ویران خواهد شد.
مردم ساکن در قلمرو این رژیم‌ها باید فوراً برای تخلیه آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/69382" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69381">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل:
این کشور در بالاترین سطح آماده‌باش قرار گرفته و مقامات ارشد سیاسی و امنیتی در طول تعطیلات آخر هفته مشغول رایزنی بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69381" target="_blank">📅 20:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69380">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGxfFFSyYlYDmjf_WTAboF-cS6C9q_tD1mI-Ywg-2iWZZnzFkyl8CO-h6fM4TV1bVe44Ms0HfY37HGtBRoJI4udNyS2csNwfczZmzY56VYosOOeEu9v4KlomP4N_kVyeG9hqxtbQAndRCHFfwN1D4fmBDQlLzdyLnu9rI_noE3zvvQkVDMbdpERxfaDI32mnMBJHlPis7Q41MsT8AD9EDQibl_dpcg5JY2HVr7JRfd4B7q-0344rygclN2lw-kXFcOj49M3WehUoh9EMr9ys6uhl9Z5hV6EVbEuHSuuvb_XdWPpkZvSpWGAvw1DBttHXhBjlglEpBc1kShBrr9Gm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
کانال 12 اسرائیل:یک مقام اسرائیلی؛
«تنش‌ها به بالاترین حد خود رسیده است؛ ترامپ بیش از هر زمان دیگری به انجام حمله‌ای بزرگ علیه ایران نزدیک است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/69380" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69378">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799177ea92.mp4?token=rlK7bKc3zkZO772tzPvF_yMheXTwybQPo7v_LzSM-6HGKPn0Vr5ZOFIEm1t_sK4nQi736R8M28yt2evnkXUJg3hxq6RiTnPEB6tXbhktNx5HnfWB4UiA-M3EgdzH1gkbtaeQBym-BfyZStulLK_vwKjIpJlKUBQlNitT1AedlKDIu4v0Nst07Q5a6pTleyhNMqXJmPZdCpub4jsLM5223imyAcSEKVzqbNtffHzrtrBH_Lvj0dY190Bv_fkGQWrwBqh0leu2HUWwYDzmik_hAuIPDmFLkisgmJvA-FnuMTjWlJxsCfWwJAjMAzrGNhEwLa9MtXLQ1XM9YqQ27d52hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799177ea92.mp4?token=rlK7bKc3zkZO772tzPvF_yMheXTwybQPo7v_LzSM-6HGKPn0Vr5ZOFIEm1t_sK4nQi736R8M28yt2evnkXUJg3hxq6RiTnPEB6tXbhktNx5HnfWB4UiA-M3EgdzH1gkbtaeQBym-BfyZStulLK_vwKjIpJlKUBQlNitT1AedlKDIu4v0Nst07Q5a6pTleyhNMqXJmPZdCpub4jsLM5223imyAcSEKVzqbNtffHzrtrBH_Lvj0dY190Bv_fkGQWrwBqh0leu2HUWwYDzmik_hAuIPDmFLkisgmJvA-FnuMTjWlJxsCfWwJAjMAzrGNhEwLa9MtXLQ1XM9YqQ27d52hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تخلیه پایگاه های هوایی آمریکا در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69378" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69377">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483837b794.mp4?token=eJaLWSJ1iJ9QpwlihYBwGHhbwa0obHCxn_1yxTozlkhhDhSQWg4XeYEKl6EgtdGe4gREJD4nB5wf3g8xwmGWld6HhQf0falnz3Ndy21K0wD5oxUQ9sr_OffjcYOId4Utp41v18jDJgMoLLMk9AEWXM7GGyDi-RyA85sN7KtMfFFyPkLlYmEEsAsB9f6_2HhTMzOm7Y1dF9fjAjd0ngP19sXXBbybEgWWhrn2fzJNu9URMqmp1t_QM17we81prBzpG69hq4ewBoNcMRx1DPEgnP2AYmM57kM4uCZHXDll1BnLG_A6sXmk8BhmnWiT5YcDGJASiWRzV2ap8wjNAo2bwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483837b794.mp4?token=eJaLWSJ1iJ9QpwlihYBwGHhbwa0obHCxn_1yxTozlkhhDhSQWg4XeYEKl6EgtdGe4gREJD4nB5wf3g8xwmGWld6HhQf0falnz3Ndy21K0wD5oxUQ9sr_OffjcYOId4Utp41v18jDJgMoLLMk9AEWXM7GGyDi-RyA85sN7KtMfFFyPkLlYmEEsAsB9f6_2HhTMzOm7Y1dF9fjAjd0ngP19sXXBbybEgWWhrn2fzJNu9URMqmp1t_QM17we81prBzpG69hq4ewBoNcMRx1DPEgnP2AYmM57kM4uCZHXDll1BnLG_A6sXmk8BhmnWiT5YcDGJASiWRzV2ap8wjNAo2bwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاخ سفید:خداوند سربازان مارا حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69377" target="_blank">📅 19:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69376">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746862829.mp4?token=UcXYk8Q3QpOhgKYXPkidaIcVjUXT4cEt21qGCGajZMvTdFG1zhTeoAyknvR4iGfTYjd88bEvRLPcR2Ismvx2THAznwRYNyy_h0qlwMIhALTH8YCoVrrbxpB2VcsKHJPjSOJNcCnKV1AObnaINTvGAOmq4RmzQ_iXf0xE9W71l_wRT83QD8nZ9xL0-qao-CloYyh2S_f62iFZtCqCIt0WkcWWPFzPSS-4wbmmD_lautlYMnS2BLEG9JCjBc1ZXGvvmezjcL_CYymUNu5bS55uEo9WHnsXBG2oMcKJxxm-n1XxzXdBs5SG1zd5EC89PTXdTfIIRr8E-2l2fRrKBDblimivp3z2xGKjHUvqrg-_BH933nDws6_cNyvi5nfje3HO6e0FxSb2EFUEecA6iHzIHhp8gGRds3KZuV11DT9ngbeeUKsBp8vmUAgYfTak2cIh06PzCQjAiarCsQwaKS6XNAES-ypz1u-id59GeMU3WDVm4VcQpq4szndHh5LFNXwahtqB0qMDN6R-pQbExn3upjVHH2HN1QqP3Bk3N_zoyg6FW_VkQUhwhGfPr03Af5aEpziy9ybSLmFXdKLAJ6Xlt1J5d8Q0AIpe1egs_M7TAHEy61KVxEs9Q6kbwJvlSNtBupy6hLkMGRgQcjOhApM5YZSimqH1uaSCLiAhpS9EqPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746862829.mp4?token=UcXYk8Q3QpOhgKYXPkidaIcVjUXT4cEt21qGCGajZMvTdFG1zhTeoAyknvR4iGfTYjd88bEvRLPcR2Ismvx2THAznwRYNyy_h0qlwMIhALTH8YCoVrrbxpB2VcsKHJPjSOJNcCnKV1AObnaINTvGAOmq4RmzQ_iXf0xE9W71l_wRT83QD8nZ9xL0-qao-CloYyh2S_f62iFZtCqCIt0WkcWWPFzPSS-4wbmmD_lautlYMnS2BLEG9JCjBc1ZXGvvmezjcL_CYymUNu5bS55uEo9WHnsXBG2oMcKJxxm-n1XxzXdBs5SG1zd5EC89PTXdTfIIRr8E-2l2fRrKBDblimivp3z2xGKjHUvqrg-_BH933nDws6_cNyvi5nfje3HO6e0FxSb2EFUEecA6iHzIHhp8gGRds3KZuV11DT9ngbeeUKsBp8vmUAgYfTak2cIh06PzCQjAiarCsQwaKS6XNAES-ypz1u-id59GeMU3WDVm4VcQpq4szndHh5LFNXwahtqB0qMDN6R-pQbExn3upjVHH2HN1QqP3Bk3N_zoyg6FW_VkQUhwhGfPr03Af5aEpziy9ybSLmFXdKLAJ6Xlt1J5d8Q0AIpe1egs_M7TAHEy61KVxEs9Q6kbwJvlSNtBupy6hLkMGRgQcjOhApM5YZSimqH1uaSCLiAhpS9EqPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیستون؛
جایی که سنگ،
به زبان تاریخ سخن می‌گوید.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/69376" target="_blank">📅 19:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69375">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=SBRqRXVaxfOZXbM--4umwvjtPd5rX_zudRRhTo2mhyKhrxiNHrqVcSTpTzJhWwm0KMm4QUX7AJMQZcxwUZGEhwgutH9SviArOFj-n_29BzhfrDzJ-43PC2L743cx4hjvYbYuZKV4HR1Unl0L0FLmgbqhh884fL4R8GdLqCkl14oMmZo9Wea-O1J05MRXXNDs8sh04HXbI3_U9MJmyqWMMLXjdNn11JSqG9Y9wee43WOTr_i5C6NG4REQvVOs1eSL_jtyhT3tDeMvwbYiORxRyqpYRQKNzbRDug6rz5mCJ2OZF-lEwFfJpiyHwin-hLBDp25MhF79TnB5lipICOILVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=SBRqRXVaxfOZXbM--4umwvjtPd5rX_zudRRhTo2mhyKhrxiNHrqVcSTpTzJhWwm0KMm4QUX7AJMQZcxwUZGEhwgutH9SviArOFj-n_29BzhfrDzJ-43PC2L743cx4hjvYbYuZKV4HR1Unl0L0FLmgbqhh884fL4R8GdLqCkl14oMmZo9Wea-O1J05MRXXNDs8sh04HXbI3_U9MJmyqWMMLXjdNn11JSqG9Y9wee43WOTr_i5C6NG4REQvVOs1eSL_jtyhT3tDeMvwbYiORxRyqpYRQKNzbRDug6rz5mCJ2OZF-lEwFfJpiyHwin-hLBDp25MhF79TnB5lipICOILVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
دونالد ترامپ، رئیس‌جمهور آمریکا، و ولادیمیر پوتین، رئیس‌جمهور روسیه، در قالب «زوج در حال بوسه» در رژه کانال‌های آمستردام:
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69375" target="_blank">📅 18:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69374">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=RisJmYCz5UpP64m4nxE9j6M_OjEnpNbE66CKMvBG0A5ybNHKeynHu2UBTXvjNHpsOg58hHExMrVVz0HQ5yW5jvF2qCMEdnHIn3WG3jMXc3NiLmH8_xOIEAKkAxFIK09FDmlN_Vp3sUYLU64Cb6U74F2oV3_AoI8Qp7Vmx_MgLA4SsFGWgDr1veK8Gez9Jl50f1YcL-f4I7t9ouxMeel04CSTEqLHIcenWBHOmm-4VnaHUZG-7ABs4W4R66iC17oRlKNrHX3HKv6WGrCjddZrbYR-7xtmRIcfwJxS2ir47vSI2FBg6btvsdKGZ8QE2ofV2K9f_FrM-JrSjkFoa5OsFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=RisJmYCz5UpP64m4nxE9j6M_OjEnpNbE66CKMvBG0A5ybNHKeynHu2UBTXvjNHpsOg58hHExMrVVz0HQ5yW5jvF2qCMEdnHIn3WG3jMXc3NiLmH8_xOIEAKkAxFIK09FDmlN_Vp3sUYLU64Cb6U74F2oV3_AoI8Qp7Vmx_MgLA4SsFGWgDr1veK8Gez9Jl50f1YcL-f4I7t9ouxMeel04CSTEqLHIcenWBHOmm-4VnaHUZG-7ABs4W4R66iC17oRlKNrHX3HKv6WGrCjddZrbYR-7xtmRIcfwJxS2ir47vSI2FBg6btvsdKGZ8QE2ofV2K9f_FrM-JrSjkFoa5OsFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
فاکس نیوز:
رئیس‌جمهور ترامپ در حال تشدید فشارها بر ایران است و می‌گوید در صورتی که مذاکرات دیپلماتیک به نتیجه نرسد، انجام حملات نظامی جدید همچنان یکی از گزینه‌های روی میز است.
ترامپ پس از دیدار با اعضای کابینه خود در «کمپ دیوید» اظهار داشت که توان نظامی ایران به‌طور قابل‌توجهی تضعیف شده، اما این کشور همچنان از برخی قابلیت‌های موشکی برخوردار است.
مقامات آمریکایی می‌گویند این حملات ممکن است حتی در همین آخر هفته انجام شود؛ در مقابل، ایران اعلام کرده است که در صورت هدف قرار گرفتن زیرساخت‌های حیاتی‌اش توسط آمریکا یا اسرائیل، آماده پاسخگویی است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/69374" target="_blank">📅 18:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69373">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=M6DJhXwfBYpVeUdc2BUXqOTR3rytZwCpHfHt4uhiovowCdLwaaANSEhVNypKddmQqB4mDAD7lRZemAZ_AR57jcVD-MBCeAq66_LJQDF8_XEYtFdc9plKFtypamgGRNoOz_sJkfiRGKgTjv1pDFy5U1dvjcJZ0LPqQP77m9coKFt6g231qhwy6lBnXQCYseM5ywoaDro_50ngjl3M9OdS6XuZQ9NgBLSqo6Vs0vwhWAiCI7KIipZibUKswol7s-ULjm06RTDZg-XrsO_jOrwj9SOqCeukfd_L0HMlrbHLYeU2_t1mCARndz0twvTxIwRWQ5jVJOjtEPMNOCESEmg-Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=M6DJhXwfBYpVeUdc2BUXqOTR3rytZwCpHfHt4uhiovowCdLwaaANSEhVNypKddmQqB4mDAD7lRZemAZ_AR57jcVD-MBCeAq66_LJQDF8_XEYtFdc9plKFtypamgGRNoOz_sJkfiRGKgTjv1pDFy5U1dvjcJZ0LPqQP77m9coKFt6g231qhwy6lBnXQCYseM5ywoaDro_50ngjl3M9OdS6XuZQ9NgBLSqo6Vs0vwhWAiCI7KIipZibUKswol7s-ULjm06RTDZg-XrsO_jOrwj9SOqCeukfd_L0HMlrbHLYeU2_t1mCARndz0twvTxIwRWQ5jVJOjtEPMNOCESEmg-Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک هواپیمای سبک قاچاقچیان کلمبیایی در حال فرار از رهگیری توسط جت جنگنده ونزوئلایی.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69373" target="_blank">📅 18:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69372">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=pYRKNhLbKgLoLX_Er7M-4QpmWkBwiPxjFxakIsmZ04WV0T7F6XfRr8BwcRp03ynRWMu--aKxv1E5x0ZL9JWHVcOhJEtf7FGYP2sCkPheU0ZseadiY5RXHpWpl0ddejN2TAuYwgc5CtxoyxpiyilBin6UOVvPsxyy9t0wNc6DPUxSGmRp-r7RZ6aViJg82AtvsnLOOoZg3-1ldA4colviGKRVBiWivN_Lc53JZauJHk__89DtRZoZAr0VSajRdRlpbqmM4efYr3LI02F3yt9ZLcC_gSwhbjH3h__AMBvFxbZDqmztDhTyvmYSj2l6L7T-uZ5xP1yFYpT30TxrfptL7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=pYRKNhLbKgLoLX_Er7M-4QpmWkBwiPxjFxakIsmZ04WV0T7F6XfRr8BwcRp03ynRWMu--aKxv1E5x0ZL9JWHVcOhJEtf7FGYP2sCkPheU0ZseadiY5RXHpWpl0ddejN2TAuYwgc5CtxoyxpiyilBin6UOVvPsxyy9t0wNc6DPUxSGmRp-r7RZ6aViJg82AtvsnLOOoZg3-1ldA4colviGKRVBiWivN_Lc53JZauJHk__89DtRZoZAr0VSajRdRlpbqmM4efYr3LI02F3yt9ZLcC_gSwhbjH3h__AMBvFxbZDqmztDhTyvmYSj2l6L7T-uZ5xP1yFYpT30TxrfptL7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح تو یکی از حوزه‌های امتحانات نهاییِ اردبيل، 9 تا از بچه‌ها مونده بودن پشت در و داشتن گریه می‌کردن؛
طبق ادعای خودِ دانش‌آموزا، مسئول حوزه ساعت 07:03 در ورودی رو بسته!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69372" target="_blank">📅 17:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69371">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
ویدیو وایرال شده از این هموطنمون که در زمان شاه حضور داشته :
زمان شاه به دانشجو هایی که میومدن اینجا درس بخونن ماهی 400 دلار حقوق میداد
اون زمان صدتا نارنگی یک دلار بود
یه اپارتمان سه خوابه تو نیویورک میگرفتیم با سه تا توالت و حمام اجاره اش 210 دلار بود ما ماهی 400 دلار اونوقت حقوق میگرفتیم از شاه
شورلت کامارو یکی از ماشین های اسطوره ای امریکا بود سه هزار و صد دلار
با یک سال تونستم ماشینو بخورم
امریکایی ها میگفتن کجایی هستی میگفتم ایرانی همشون میگفتن شاه شاه شاه
کدوم شاه شما دیدید بیاد تو امریکا براش با کلی عزت مراسم بگیرن که برای شاه ما گرفتن
چه افتخار و عزتی و لوکی بود شاه واقعا نوع بیانش و لباس پوشیدنش هرچیزی نگاه میکردی لذت میبردی
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69371" target="_blank">📅 16:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69370">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mpm-ppqw96RHHtjLgZiCbOXxrDcEuD9O0kdqGAh2wGBoTIfgqqN0Sh3UWlNl3fESK4HbZjWzugqNT2UWTLzzn5Z-V9c5xAsaclCuhXO-EP4dW8TssTYiOwpZwH07f3Y5Wr0rGwIPRk-qmoLo05iKGLilM_Gip4MOhHbMY98mOrLbqPmtQRtiMQWab80sOxIVsQGp51ITGilbLoNCPTPGMj3YBEFS7r0pDiNHXZNJe70R3VX8tnLSZ0K6kGVy0frHoUGubPazTMdILqXS8gPOdoBTfhbmPSxcuvFJ53QWFHTyQWOYzMNGcg3MWAEYWlnBfZZ-rwhpo-wDWS6ezTartA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سفارت آمریکا در مصر هم برای شهروندان آمریکایی هشدار صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69370" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69369">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=tgKQQRxamWXY3p3WzQzlSwMSxaa2HwoU2l5z3KLlc3fBZhiFEPKxIaTRF1Oc-rvfP9tqK_L1DR7I0bQvJTfhMIisO3V11MDQetvD6MnEiv1PDjksCzYesNEhClNPoDXu6oeHoAx6eZxXbOD32oXSYhOpebMp-J1XaaGWPbBoUYf7ZSaTjekfu8y9nnDlF4SPtj9Ui4flkyAafu6W6ilhMXPHsEXFvpj1nVlapE0lL6F8NfjAZkTJIgE9X9o1FzciA1zB6qr3_TGxq9Ay-2M0qNDvJLtgjt-HHw7jNw9oMEp6nGGfi54lCkat22eQqQMKojvcWmjY95DCepxXJmc4Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=tgKQQRxamWXY3p3WzQzlSwMSxaa2HwoU2l5z3KLlc3fBZhiFEPKxIaTRF1Oc-rvfP9tqK_L1DR7I0bQvJTfhMIisO3V11MDQetvD6MnEiv1PDjksCzYesNEhClNPoDXu6oeHoAx6eZxXbOD32oXSYhOpebMp-J1XaaGWPbBoUYf7ZSaTjekfu8y9nnDlF4SPtj9Ui4flkyAafu6W6ilhMXPHsEXFvpj1nVlapE0lL6F8NfjAZkTJIgE9X9o1FzciA1zB6qr3_TGxq9Ay-2M0qNDvJLtgjt-HHw7jNw9oMEp6nGGfi54lCkat22eQqQMKojvcWmjY95DCepxXJmc4Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیرزن ایرانی توی مراسم اربعین، برای اینکه از یه زن عراقی صندلی‌شو بگیره، بهش حمله‌ور شد
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69369" target="_blank">📅 16:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69368">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حالا ما کجا بریم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69368" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69363">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkKGAVXRQjaZUcE7_6wbe66DsAiKuc2OgTDE4Wkdh-iDPbS0mY1g5R944TbhAQuV_gT1UZOz0_mN0jSbVUDJfp-_5z_U7FqXK40QEuJ_aroi-4Bk0iR5XAKWRFfmthm0hnDEtaTCgFmp1OOyj9Lf6D2hBQ_QSf343HfKn5mi1wi6E4eeqcY_Dw_R0hp_c8imQ6h8ohddPb2qrPOBVzGIocxupQc9PN2u1EnD43xV0Sm4pd79fBMFSLIA9k3xDpIv6LXNiNRHlrA0MMGbb1ByNCpfPy5EpdP0XYI9eBsKVztFFGVRZg3MzgjXcWvOTFj7YK2RpXAtNndn-5MqsFbB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auwfhAR7cNQO3GYXqStQTizk98e9vDWndRnOhdRnBZVXjvErYQvSBCynoWb8ATxOCT9A7_liU859VRMJQjJ-ws2kyjdycIST49L3ifhcCBdzbydEXhe-nV2po5EypHl1RtgP3WH_wxqme_5A9B4sjdio3w96JHVa5G4iKxPlbvyuBnEnrLLHU8HVYjwPqUlLKTOJwN6BqOkYuXmQ_faq_Wi8bgYvJNKOkoeu7zfKfnT2cXuEj5C-O43KBhjRH_xERnXvxJa7JHpcU133wq9fgxpHGzoXEm_7hXRdHbtkMWwt2d0l6u34Phpr2qIUE1Cq3ymdTAbm8eEB1Z-wNBR2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXsznxWvBiWtPbvA9vfryK4Rc6hd0ZlnPUP8VtuBSOJCM5UGFg-_IAuuZLpi-NKcMrVPzcqyiJUc1wqnfuh74FLrld3lg15_Uh4pbK54qT8KkcjVi3ixOE3rdXmYMbvIttbKnskUPUtLVK1Hg0bQhs47RHQ-enCBwv9dnPe-AyP4nyjWnJrd_H9T38hDTcCHaRypttxbyMZ9OmZLh8l4duDM0NIvsJNXmKrYwrViVE2sZ0_w0VGjhwUojpWNPS5htq2vCCWV9zrMpLxF0NgaAyfvzjnBcgUff0JKZJPIuuQn4-O4EUHHxrdsOdBwLX0pqMxgAGXzMpK9T03ARfhfmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPYIXAc3vKcyDUhGPWOfs-M8eNjoAkeCO49CaIc6LDi7AZ24BYlGLq6w3RiKDywgfW5E20hWA60gS2BPvkpW0hvtMop2YHNF_QNmWJBP1RTORRpMGLgPlktW56zxR0v705TNAoSH-StSf74wRYJiGQjcM8-OEpxeIcYeiWrEWS71ChXhpsIsdTeH5w9FVKT6DU5ntojNPUws9fnLAekZZftm7VEvaf_V-W8AIAMuTORBz_N5NPaoTCUl3LM8KSCMSodHRe5Fj130zag6osuMMF9mI02bfA3WNjkyeE6kZADajcQVN3Zm-kCQ1t7AXb6LuSiKL-TjRrVqos3StvdR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8tlTw1YneKV6Y4t6XF9rfBNUG6SHnrpPSDvQcqEJZYHWw24UGL_Y_n5BremYBnljDvgkcf613KA82LBZAPw0mBZH4kUjcQrZ85N11mbh1TTFPCjO-ldMPMJzjYwpBzuXAyoYwXqWb5RHdymUGs1b0scFqGdFZfjBBG-P_XtSiEsqjDYPDwyM4jEnfZTAvNRwL7sKommeeWxqojhYRImP73NH99zUP5VaSmKZBfHQ1wRyiXGsKPIc400wVGkY6irdLznEZr9dHKypnCPHlq8pNfBzuEhq266azXa46thNZlQ5Nhkt5YlXic1CH3IXW2CjU3E3djsvR-JMoGZ79eU9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارتخانه‌های آمریکا در خاورمیانه یکی پس از دیگری درحال صدور هشدار به شهروندان خود هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69363" target="_blank">📅 15:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69362">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=VYf1FHdhFZvC9drcJ3I4FwEPCWYb74g6guZ2mg0EdHlWHXwn84c5vxZMiQgNSk78K3fgc78EF1sRmASU3i3dJ7MCWvvPz6sdrk0A_TWMKHpFf422v3U4sRcpXCY27ugQJCyupPe6-OyugYpwwBXq8xUOiynCpUqY5Cl9ppYVZDvDjHcadYHaM7c_tZ5w71Jj-7UD89F4R7m87i9rjNWc6KTbKYl2JxCYZFn2JFIZbCNwvYcdVr0cxELRTUVgkCvJUkCu5GHAZcFipII1IDJfjbnpxhuDsawPN5JGZ4knJ11S4mEhjebFS7z5mWw1tsvoeNrDjykdHuSrSoUmJ8pIeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=VYf1FHdhFZvC9drcJ3I4FwEPCWYb74g6guZ2mg0EdHlWHXwn84c5vxZMiQgNSk78K3fgc78EF1sRmASU3i3dJ7MCWvvPz6sdrk0A_TWMKHpFf422v3U4sRcpXCY27ugQJCyupPe6-OyugYpwwBXq8xUOiynCpUqY5Cl9ppYVZDvDjHcadYHaM7c_tZ5w71Jj-7UD89F4R7m87i9rjNWc6KTbKYl2JxCYZFn2JFIZbCNwvYcdVr0cxELRTUVgkCvJUkCu5GHAZcFipII1IDJfjbnpxhuDsawPN5JGZ4knJ11S4mEhjebFS7z5mWw1tsvoeNrDjykdHuSrSoUmJ8pIeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده‌یاد مانوک خدابخشیان: دو شعاری که کار این رژیم را تمام کرد؛
رضاشاه، روحت شاد.
اصلاح طلب اصولگرا دیگه تمومه ماجرا.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69362" target="_blank">📅 15:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69360">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKRONH0SHZB8Sv8slYnhSydIxWGCaN0xTAz2f7rLqIzGVYorZMEDleb5qjqgpkAEWpt6PRfuvwgmeOKHKsO3ee9L1OjlwqUxz9zyRr76OGMNw_1EgCkaAlqBqcxjwumRv-tJJt2Bwp1aUrNIWi-BmVK9vV4ZsREBXwfM0fAHMrzk1l2Ox1kJqhmjUyJEPCNYkxRItNB25ElhcJWzvFPtgK4KZtld3_2b063vyzIwufU9qHKbAhZ9VOTTclEZ1LsCaCeqCJdRiCeL7UwIj94O8Z6aHnR0UXFBw4SdUiunTamlBwXWEZllLY8ynmJxbQSqMd2JBs7dvn-AbLbJdUG34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gR2Sa7Esh01icWypyfb3pwdsvPwBr-iyEJpImkYRHgRidN1IKg2eKgcWe-VRdh5-i-RlnGXAwv1VrtFDq9poReKS5n-aw3KngV23nTUu8IwQkFyu6W2QDQUG73LfC-BpMQYX5mcU2I-46Wr1Rnl23kenmv3BysNKKII5W0MJyrEy1CEn3kNGZuxfTjK_3XPLeSZgE3Xd50VdDhdhiafU5r8vHqY3HROoS9dLDG3sQmRB6g0QqVb1NfXiOmWa3WubgfNTzncaKOpkfsvU5c9TD421lzQjSEDpjQTh_ocW_wyEYrdIkT2sPOiDp0fwnrg4UGgDBuEbiFP1BHlay38FlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارت آمریکا در اسرائیل و عراق:
آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69360" target="_blank">📅 14:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69359">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLi53MH7DjPqMP0ZK26f71l4giA0CBtn42EOeA9xUesDcICFs7CnXVvYiQDnLSQ9c8wkZb5lans3d0SjImJGGGyNtERm_UYCNJU0rRNIl8RVJ6QTGFMgtcAe1TXRnBB21rFvrgZaXpXs9z7Z12wPhxqDAimdj5Q_5wn9FMs26AhlNtH2cAAZhzYj6kmh0BGctZ0OIw2Q0OJiIYvWbRg_FCxsc5ksjc2Z2oSBBGM-dU4sRWCQj4mt4A6fpaM39sZgfWlpkGgyHfd4UgnwD4BgJdceO8JtXQjxlMGCvUZflqlnwgrw6SclfAXzwj6UmjsZhmG7h9T4CnUDp713QixQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:  بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.  @News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69359" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69358">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
تسنیم:
بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69358" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69357">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
دقایقی پیش از حوالی اسلام‌آباد غرب کرمانشاه، صدای چند انفجار شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69357" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69356">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=GacWaoiSUpohtqbUL0lwrD2wA0I6mnu4mlvqtdw7hwxOzdPzgOawP_T0OuPQ-KGvH80Kh8Wm2Z1TGR5YzJ4iueSi5hFOSQL7FVuGOzXYxOS2IFcINyB8m5SF-4JeU3mAFUc52sQU7RcHJZRhY_Jwkv6Dton5mTJKegEIioS45OHkqov3S8yj2bcqntLIjRiacFL_gcYJxGYnGIpOybHMnRoSaPGj8TLZt-0ZUG6rPAh-jyu3nJ06Nk0px1bzT5I6gWzeJM64lXKEAphABdQIHPbHjBiJ6tNDoEoWiRtt9UtTpMcnA0rfAO6wEkOoPkbWFfLG1qp9qQLIn_xqKG4SrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=GacWaoiSUpohtqbUL0lwrD2wA0I6mnu4mlvqtdw7hwxOzdPzgOawP_T0OuPQ-KGvH80Kh8Wm2Z1TGR5YzJ4iueSi5hFOSQL7FVuGOzXYxOS2IFcINyB8m5SF-4JeU3mAFUc52sQU7RcHJZRhY_Jwkv6Dton5mTJKegEIioS45OHkqov3S8yj2bcqntLIjRiacFL_gcYJxGYnGIpOybHMnRoSaPGj8TLZt-0ZUG6rPAh-jyu3nJ06Nk0px1bzT5I6gWzeJM64lXKEAphABdQIHPbHjBiJ6tNDoEoWiRtt9UtTpMcnA0rfAO6wEkOoPkbWFfLG1qp9qQLIn_xqKG4SrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه جوون عرب داشت به زائرا میگفت بیاید آب انگور بخورید که یه ایرانی رسید و بهش گفت:
آب‌انگور نه، بگوآب‌شنگول
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/69356" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69355">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=oMfz2dMwtU6WTjlpuGF0-GJSsZWZKxG2bxC1dY1I-LZEIIt63RMzrt9h0zMlsjtRTaM5o82yZybzOkiZY01BGgqrPAiaxpKHg6gYlIfoz2EJQ6A_T11GaCL4MKAsMNPOpRb9AemuueFiTqZod4x2jTavSgeYzoX8Kvo90pLJRQCmwV7aodpeLiSkHv556tuduBJMXzvND4blXXV2IfYNrcYIwXPDNZDTmuPDoFfMsK4mKUWpGPRxYJPLY9p5c5JQLGByc2eXPeNOcmtdu2JlmYM934ksShostN_b5uBTpP4DvDTI7u5g4Y2ANO-OxhrfES9NyWEySQnQV9cR_OQsHx8gOzz44palnKXbqVBpOd3JkunyiyKrYAl-skdXKgMI0_-c_VA5glnWnF1AoMgcokaBOKVjVyvTbgENVEUl5rgQJ9wIdhbvKnoud5dVbva2hhfUCPlHP8Gv2bfvSqv7edmEbRmac60sxWQpIcEsfcLMw4nBZEJUdIkmSVq2bOJryIzVQbm3iQEqRPuKMJbWkXQknxnMd_BIdZTF0KL8McLhm17jSxFwOAE97sYJS--BnmCyNnWt-NRJX5qylZSsrmdcDwDSiMIpjZLMBk5jr3MDjpDB0UY6DSbQ1lYOH15g0Ozoofhjn-UcG2H7OXewUprFW5vGAdVqqCB7JnZyfs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=oMfz2dMwtU6WTjlpuGF0-GJSsZWZKxG2bxC1dY1I-LZEIIt63RMzrt9h0zMlsjtRTaM5o82yZybzOkiZY01BGgqrPAiaxpKHg6gYlIfoz2EJQ6A_T11GaCL4MKAsMNPOpRb9AemuueFiTqZod4x2jTavSgeYzoX8Kvo90pLJRQCmwV7aodpeLiSkHv556tuduBJMXzvND4blXXV2IfYNrcYIwXPDNZDTmuPDoFfMsK4mKUWpGPRxYJPLY9p5c5JQLGByc2eXPeNOcmtdu2JlmYM934ksShostN_b5uBTpP4DvDTI7u5g4Y2ANO-OxhrfES9NyWEySQnQV9cR_OQsHx8gOzz44palnKXbqVBpOd3JkunyiyKrYAl-skdXKgMI0_-c_VA5glnWnF1AoMgcokaBOKVjVyvTbgENVEUl5rgQJ9wIdhbvKnoud5dVbva2hhfUCPlHP8Gv2bfvSqv7edmEbRmac60sxWQpIcEsfcLMw4nBZEJUdIkmSVq2bOJryIzVQbm3iQEqRPuKMJbWkXQknxnMd_BIdZTF0KL8McLhm17jSxFwOAE97sYJS--BnmCyNnWt-NRJX5qylZSsrmdcDwDSiMIpjZLMBk5jr3MDjpDB0UY6DSbQ1lYOH15g0Ozoofhjn-UcG2H7OXewUprFW5vGAdVqqCB7JnZyfs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69355" target="_blank">📅 13:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69354">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532a951287.mp4?token=F5Qvkpyqzy0R08cRwwE6aCuU3keM0fHMwZM6YOvKvsfzlUYGCNYByNYZgw77N1OwdBXgpDMznQoKEDi8MVJ9mUVBL3ikgGWIvaM96lniCWUdKpBrqUIN340snNhBberxuWW_1enK2qj9dKn-NZsvlpdAOn1OXBb6ZvzlJ3HyQFGZctiPEuEsi28KraWtep55QCs8xsUHB2qsVnH1pcH8yteaIBWlwgOodJzOQjpqnpVP53p5SFczVnvbAnwurbYQjLmGNjNBbNPTRFw6PZfB_F1mb6cwnkentNulmkBvhhhAZNWoSGLreWHjLLrRwZtNKUqdurdoP4ro9lHv_UrQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532a951287.mp4?token=F5Qvkpyqzy0R08cRwwE6aCuU3keM0fHMwZM6YOvKvsfzlUYGCNYByNYZgw77N1OwdBXgpDMznQoKEDi8MVJ9mUVBL3ikgGWIvaM96lniCWUdKpBrqUIN340snNhBberxuWW_1enK2qj9dKn-NZsvlpdAOn1OXBb6ZvzlJ3HyQFGZctiPEuEsi28KraWtep55QCs8xsUHB2qsVnH1pcH8yteaIBWlwgOodJzOQjpqnpVP53p5SFczVnvbAnwurbYQjLmGNjNBbNPTRFw6PZfB_F1mb6cwnkentNulmkBvhhhAZNWoSGLreWHjLLrRwZtNKUqdurdoP4ro9lHv_UrQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه لیلی فیلیپس پورن استار معروف که تو 24 ساعت با 2 هزار نفر سکس کرده بود!
دوس پسر لیلی: من اصلا از این موضوع ناراحت نیستم، چون اون واقعا زحمت می‌کشه.
مهم اینه که آخر شبا میاد پیش من، و اینکه من بوسیدن رو براش ممنوع کردم، اگه با بقیه سکس کنه مشکلی نداره، ولی فقط باید منو بوس کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69354" target="_blank">📅 13:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69353">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26851041.mp4?token=guoO1rrGI4w-tpm0a4fmDo3IKnt1kqiRsq5symavmCGz2pFvlv-CRzJPLwJgsOyCvzDn6yPLH82o4NmYj_5SnxLWEUgs740itMm7kl8MsLoyQvJ1-nreAJmeBevDFH0AxOPHY-kKRlm0QH0l1lcz3esjvS93QIdygXjvugxakDKCLNefsIgs3DF97nUl7Lsfr00L_rmkBd_3q1GsHyTacEB4YHW6TAvL-YB2jpKER8l2KvyWDgA4bFX_uMgQb5K9DPjaUIadotgkm29dmw_fE1tiZqpdC39YhVK1xvouOMAeGN4japyQE5RXNcgwYON4wwDM_7v4DKpGFz2QDajQAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26851041.mp4?token=guoO1rrGI4w-tpm0a4fmDo3IKnt1kqiRsq5symavmCGz2pFvlv-CRzJPLwJgsOyCvzDn6yPLH82o4NmYj_5SnxLWEUgs740itMm7kl8MsLoyQvJ1-nreAJmeBevDFH0AxOPHY-kKRlm0QH0l1lcz3esjvS93QIdygXjvugxakDKCLNefsIgs3DF97nUl7Lsfr00L_rmkBd_3q1GsHyTacEB4YHW6TAvL-YB2jpKER8l2KvyWDgA4bFX_uMgQb5K9DPjaUIadotgkm29dmw_fE1tiZqpdC39YhVK1xvouOMAeGN4japyQE5RXNcgwYON4wwDM_7v4DKpGFz2QDajQAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عوارض خوردن ساندیس زیاد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69353" target="_blank">📅 12:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69352">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=SXfM21OvL1bEoYysLxjZY8DJV0bIpEdfI_9lob_cMX-XUEkv7PyfnXS2mhDqiij8dIyvSDoEeFWeh7W4mqyS7hYzJzXisXHZmdWCMyY6MBIQ_QhieJru_IaXHQduAmEy2hsfihbSwz7_kjcwcSZeKcBZFiUj0zyeVFXvXRST0BB_vi2AN1d2K4QqZ7POsZEt7xLP-UZeXAafSkkHuaK7Npac_kOCkz1cwIDM3vGVmyoNwkutLG9rtFkznUNhiVWJsb6NtACeswXpc2vEJyGXIyUtBN4cI7STwIg69qbx1OihXTZ-_Q9TbN5USMV6C9FAblUVJqf7ETAmINK9SyBiRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=SXfM21OvL1bEoYysLxjZY8DJV0bIpEdfI_9lob_cMX-XUEkv7PyfnXS2mhDqiij8dIyvSDoEeFWeh7W4mqyS7hYzJzXisXHZmdWCMyY6MBIQ_QhieJru_IaXHQduAmEy2hsfihbSwz7_kjcwcSZeKcBZFiUj0zyeVFXvXRST0BB_vi2AN1d2K4QqZ7POsZEt7xLP-UZeXAafSkkHuaK7Npac_kOCkz1cwIDM3vGVmyoNwkutLG9rtFkznUNhiVWJsb6NtACeswXpc2vEJyGXIyUtBN4cI7STwIg69qbx1OihXTZ-_Q9TbN5USMV6C9FAblUVJqf7ETAmINK9SyBiRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: میخواستیم خبر شهادت رهبر را ساعت ۸ صبح اعلام کنیم اما تلویزیون‌های خارجی، زودتر اعلام کردند
.
در روز نخست جنگ و تنها یک ساعت پس از بمباران بیت، شهادت رهبر قطعی شده بود.
تا همدیگر را پیدا کنیم و هماهنگ شویم، ساعت ۸ شب شده بود.
قرار شد خبر را فردا ساعت ۸ صبح اعلام کنیم و از مردم بخواهیم به خیابان بیایند. اما تلویزیون‌های خارجی، [ منظور اعلام رسمی ترامپ]  خبر را ساعت ۹ و نیم شب اعلام کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69352" target="_blank">📅 12:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69351">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⏺
سفارت آمریکا در اردن:
از شهروندان آمریکایی مقیم در خاورمیانه درخواست می‌شود که برای ترک در صورت تشدید اوضاع آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69351" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69349">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=G_c4FFu_itlIS4FPFRxlw4fwdmU0HdAqVHoQdIeOPm7gw0B0cS1opZSL7EbVN3mYXcUHPMe9A4sJuylm67jRG5C7RVDCz4DaHRLCdfvpuHJEkDemWA8ypIpcHH4bWnAWQADawRmXndSK2U_da3gtk3YVCwQLgJyRIOaGvrkykfZ-LdPMS-dIOsH5wJ8s39nP-NczkqXBb8kLmhTCLvkrw4qEsBwA94NkTS7kjeZlBheocA9Mwpvtt98YVbsueSYjuz4NpsXNEXuhtn17LclZTLlz4co_wGgoGPQCOBLNqDxp7BTcIDz3gqlyviSu5hhFAx5xq-Np7BADv6NYkObttw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=G_c4FFu_itlIS4FPFRxlw4fwdmU0HdAqVHoQdIeOPm7gw0B0cS1opZSL7EbVN3mYXcUHPMe9A4sJuylm67jRG5C7RVDCz4DaHRLCdfvpuHJEkDemWA8ypIpcHH4bWnAWQADawRmXndSK2U_da3gtk3YVCwQLgJyRIOaGvrkykfZ-LdPMS-dIOsH5wJ8s39nP-NczkqXBb8kLmhTCLvkrw4qEsBwA94NkTS7kjeZlBheocA9Mwpvtt98YVbsueSYjuz4NpsXNEXuhtn17LclZTLlz4co_wGgoGPQCOBLNqDxp7BTcIDz3gqlyviSu5hhFAx5xq-Np7BADv6NYkObttw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک انفجار بسیار بزرگ در یک انبار مهمات در شهر خملنیتسکی، واقع در غرب اوکراین، رخ داده است که پس از آن، انفجارهای ثانویه گسترده‌ای نیز به وقوع پیوسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69349" target="_blank">📅 11:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69348">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=E-4Siawmb52jgcogfu9V0R1JFbK5bRhPH6_wK4EZX4qMXB1yTpNSVw3idoBu8CnSMN1iHSRz7jy17CxJP9joMGDgGMPrpG4A_afP0NhybyAzenJe05P3mideR8q0CDaF5Vho-MwqTSgbGYckqAHYtVct3vOpJdqAa35z0uf0UqnMeP0H90qIj9xhhf0NVjmWz_B2XoYdb6zBEHyLGCdHKubXWfFQBAa2sGpjK-Xpd-euW21S3ZvphIk2HeIalcN9jm0IgpMUt3CqC76Jm0I9yOzf9KUYQCV2WJWcAQAwL_1U-2JEA1KPyC7Qa2E-tQ7O2qiwXWXOtoqltGQUThGP-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=E-4Siawmb52jgcogfu9V0R1JFbK5bRhPH6_wK4EZX4qMXB1yTpNSVw3idoBu8CnSMN1iHSRz7jy17CxJP9joMGDgGMPrpG4A_afP0NhybyAzenJe05P3mideR8q0CDaF5Vho-MwqTSgbGYckqAHYtVct3vOpJdqAa35z0uf0UqnMeP0H90qIj9xhhf0NVjmWz_B2XoYdb6zBEHyLGCdHKubXWfFQBAa2sGpjK-Xpd-euW21S3ZvphIk2HeIalcN9jm0IgpMUt3CqC76Jm0I9yOzf9KUYQCV2WJWcAQAwL_1U-2JEA1KPyC7Qa2E-tQ7O2qiwXWXOtoqltGQUThGP-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
آمریکا و اسرائیل برای شدیدترین بمباران در روزهای شنبه و یکشنبه آماده شدن و ترامپ دستور حمله رو صادر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69348" target="_blank">📅 11:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69347">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_JMn-wZI_cFL8ydhDCNx6_5VJXuGga2Wc3x-NuEZ6xZN3I4_RvVxhsFFt2kf5WG7IfGaPua4E80z_bYNXRzYG0aV4mUfCl-IkephlVIVR0qbCM37vV8ebnEHSLgx6bOgt465qB8_pLQZ2PlnntZqYxQwNgIES3LrCy5QL875xMYsYb9F8oK4x-JcZVwSc0PJBIbAaDc1e8JHLWGttWVXmukAM2eksRo17TJvT4OOderNnAPQ-bE5t73pjIF4UHuURCJGxu7OkTCEEA2oxWKZ9Wz59qGmARBknlrMQ18HSj90qP78-T_8UsfLsmGn3AjG_g7ja1UR893-IJRwoIIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دقایقی قبل یک کشتی در نزدیکی خصب عمان مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69347" target="_blank">📅 10:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69344">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=EtihQaNRRvFCoLS-iZTwZoiFmzNu9chPTqCtKhN-d_FsaCHexCGnnRKofQ3d2TUjvrbUQ4c8WLBUYHZoX9_HZeBf_6HkJFmH5Vwq1yGKy7PAZzdkXwCDxI-eGcIRtsXIgVwbl1tvbcw0VUJiJ1DYkSFyDv-73OZKauokpSwZu__DpPZpIuBTd4mZdnXCfpOfxgCnrk8GWSttpybJkxbD_r4kVLuGmv-gC8LabHO7cNPbG1P3YIMoh4n3DK0Dj0HUJuY-_GU0l8cmiAS-HrQTV4nwmLZ04X33Sn3z5vO2RDSQi1YHUM_F-O1QJ-NVZraAJoZS_0IRuJ1-jbeBrWMfig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=EtihQaNRRvFCoLS-iZTwZoiFmzNu9chPTqCtKhN-d_FsaCHexCGnnRKofQ3d2TUjvrbUQ4c8WLBUYHZoX9_HZeBf_6HkJFmH5Vwq1yGKy7PAZzdkXwCDxI-eGcIRtsXIgVwbl1tvbcw0VUJiJ1DYkSFyDv-73OZKauokpSwZu__DpPZpIuBTd4mZdnXCfpOfxgCnrk8GWSttpybJkxbD_r4kVLuGmv-gC8LabHO7cNPbG1P3YIMoh4n3DK0Dj0HUJuY-_GU0l8cmiAS-HrQTV4nwmLZ04X33Sn3z5vO2RDSQi1YHUM_F-O1QJ-NVZraAJoZS_0IRuJ1-jbeBrWMfig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
بروزرسانی از اسپانیا:
نزدیک ۵۰ هزار نفر از مراکش و الجزایر فرار کردن و غیرقانونی ریختن اسپانیا!
برای کنترل این مهاجرای غیرقانونی پلیس فرستادن که پلیس هم کتک زدن.
این مهاجرا ریختن توی فروشگاه‌ها دارن غارت میکنن، از مردم دزدی میکنن و...
مثلا از یه مراکشی رندوم میپرسن چرا اومدی؟ میگه توی مراکش رفیقمو به قتل رسوندم، مردم هم باهام بد رفتار میکردن، منم فرار کردم اومدم اسپانیا.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69344" target="_blank">📅 10:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69343">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=lnF4lJwb1EIqBIH4-re1q_ZP__9q8euY2FVJlZum2MSs9BDvTMvUZKBe7fvZuWNKbdD8m_uGZLMdeJC4DoFRJw4_gMe2XUgCxYestDiP0uDISij6tAful11pxMNxWP4HmML8N_MjP0-AWmjourw5tbw1z67DIKIMUeSEeyCG1TceaPws3M3WwD54ZTyiiZjeXRashYOK2kx9P_gTDie8NcdItFwWNhRdsXh463hMVXQpRDgyjD-9MlXKZy8ptiirGYD6z5armd9soRnEYuuDS-UXJk2wkmTb8o9kXo1Ck32HXWSwUTjWkTZlAYEvKU6V8LzCjn1bot13qVVbk8WzzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=lnF4lJwb1EIqBIH4-re1q_ZP__9q8euY2FVJlZum2MSs9BDvTMvUZKBe7fvZuWNKbdD8m_uGZLMdeJC4DoFRJw4_gMe2XUgCxYestDiP0uDISij6tAful11pxMNxWP4HmML8N_MjP0-AWmjourw5tbw1z67DIKIMUeSEeyCG1TceaPws3M3WwD54ZTyiiZjeXRashYOK2kx9P_gTDie8NcdItFwWNhRdsXh463hMVXQpRDgyjD-9MlXKZy8ptiirGYD6z5armd9soRnEYuuDS-UXJk2wkmTb8o9kXo1Ck32HXWSwUTjWkTZlAYEvKU6V8LzCjn1bot13qVVbk8WzzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
صحبت‌های عادل فردوسی‌پور درباره ماجرای دست‌بوسی عباس صالحی :
تو عُمرم دستِ مسئولی رو نبوسیدم!
عباس صالحی وارد مسجد شد و کاملاً اتفاقی روی صندلی کنار من نشست. به شوخی بهش گفتم اگه یه روزی فیلتر 360 برداشته بشه، همه این نشستن شما کنار من رو ربط میدن به رفع فیلتر!
همون موقع که داشتیم دست می‌دادیم و روی صندلی جا‌به‌جا می‌شدیم، شب دیدم یه ویدیو وایرال شده و با یه تیتر زشت نوشتن که من دست عباس صالحی رو بوسیدم.
اگه قرار بود دست‌بوس باشم که الان برنامه 90 رو داشتم و 360 رو هم فیلتر نمی‌کردن.
چطور ممکنه من برم تو اون مسجد، بین اون همه آدم، بیام دست عباس صالحی رو ببوسم و برای خودم حاشیه درست کنم؟
من همین چند روز پیش هم گفتم؛ بله‌قربان‌گو نبودم، نیستم و نخواهم بود!
همیشه روی اصول خودم ایستادم و سعی کردم کنار مردم باشم. واقعاً این حجم از هجمه‌ای که به من وارد میشه حیرت‌آوره.
من عاشق کارمم و اینو خودشون هم می‌دونن، ولی نه به هر قیمتی. اگه شرایطش فراهم باشه، تو فوتبال 360 به کارم ادامه میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69343" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69342">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=JTPaVFtwhfUFH_YVU3W4WUO7xu43Bdd8QkCfTK4lLFRPTsnaTdTb6RaMYNXPhziSyarXn3Evq4c2dXHejtJRf4bwOwWTOJ8lEMeRyxrXY0M1M_c_XPc-VWsj94N60zTc-n4JN1udHnA89RhEzMi84gRktxVkC61w9mhfYqWSU3I_HWjGIgA4hEefGls4rxqaqnha_i2JUN1xfMbmcBfW_sdZEr8uKcuA5_GoS-JAahbLFH9-61x6pIo2j1XXYdW8sT19vkblhKIHdxhPq_T0q2d94BVH3pn3PKeGZslpYGSomoep0ptA__BTJ3svXtnEoEMUCWjEcCl7LWUur_up2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=JTPaVFtwhfUFH_YVU3W4WUO7xu43Bdd8QkCfTK4lLFRPTsnaTdTb6RaMYNXPhziSyarXn3Evq4c2dXHejtJRf4bwOwWTOJ8lEMeRyxrXY0M1M_c_XPc-VWsj94N60zTc-n4JN1udHnA89RhEzMi84gRktxVkC61w9mhfYqWSU3I_HWjGIgA4hEefGls4rxqaqnha_i2JUN1xfMbmcBfW_sdZEr8uKcuA5_GoS-JAahbLFH9-61x6pIo2j1XXYdW8sT19vkblhKIHdxhPq_T0q2d94BVH3pn3PKeGZslpYGSomoep0ptA__BTJ3svXtnEoEMUCWjEcCl7LWUur_up2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سیدمحمود نبویان، نماینده مردم تهران، درباره شاهنشاه آریامهر؛
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69342" target="_blank">📅 09:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69341">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69341" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69340">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=hY8UI19BXa94Fws7kHGWwo_KALjd9aP7cqO6L6GLXuPwJ9fsKrn1Ng4LpRNDDtSRPvPw9AKo9bO2pffAmkNAA3r2Mnv-9lSC11_kZbG4Bjicx6HbC_FC13BKDgFTTfrtmoG0c9c8XzvWbHVJFcAbr27jUsBDceZASWvK1JKFNVAGkfTYbh4A_cKIbyLic59Dp0OvR4d9Td5UtQg_v1jMCEDqYYYwgHx3c__jHJVRw68gEyYCB3LvUhfqasmSO5k12e5NMvkHX_HO4DNCey9yuEIuVxJu2e_p8FltdZ4hF-nawvTYO4o3Bd39eU06Xt8ONwMY6GoimfuwwsVvF_fsQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=hY8UI19BXa94Fws7kHGWwo_KALjd9aP7cqO6L6GLXuPwJ9fsKrn1Ng4LpRNDDtSRPvPw9AKo9bO2pffAmkNAA3r2Mnv-9lSC11_kZbG4Bjicx6HbC_FC13BKDgFTTfrtmoG0c9c8XzvWbHVJFcAbr27jUsBDceZASWvK1JKFNVAGkfTYbh4A_cKIbyLic59Dp0OvR4d9Td5UtQg_v1jMCEDqYYYwgHx3c__jHJVRw68gEyYCB3LvUhfqasmSO5k12e5NMvkHX_HO4DNCey9yuEIuVxJu2e_p8FltdZ4hF-nawvTYO4o3Bd39eU06Xt8ONwMY6GoimfuwwsVvF_fsQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69340" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69339">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس لیست اهداف انرژی منطقه رو منتشر کرد:مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی؛
❌
میدان نفتی غوار در عربستان
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
❌
تأسیسات ابقیق و خریص عربستان
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
❌
پالایشگاه الرویس و میدان نفتی زاکوم در امارت
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
❌
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
❌
میدان نفتی برقان کویت
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
❌
پالایشگاه ستره و تأسیسات المعامیر بحرین
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
❌
میدان‌های گازی لویاتان و تامار اسرائیل
ویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69339" target="_blank">📅 02:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69338">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkfBS0WLtKPCjKng0S7oFGiWp3Is2AB3aG3GyN3hotWiwEexTMRaAblVgkFEcKoD2j6Orzid8lyH2XqNuR2usQiIZf0dcVt4s4x9s6A7ISW2Gl3w9UvVaNlbo9H9QLnpG9zejriW-rSUy6v5ytAvP5aLX8CPZ5XInFPtZ01Mj9mW9vJi3V9ViPNqZwBmqRzZ34MobLwuD05vSeCWKgu7soCIKmgsX80jaEVMcff_KmUM0GgdzKyF8yaB0xn9SLmLLF-DFrgEXK-Ex6n1MKC6_uuSIGDFmPQkQDTTn013A3HQosnQULp5nvL2jL91kNfjLDmdaWxz4qO9RczxNH5pOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:یه مقام ارشد امنیتی به ما‌گفته؛اگه آمریکا یا اسرائیل بخوان به زیرساخت‌های ایران حمله کنن؛
ایران از قبل یه برنامه گسترده برای جواب دادن آماده کرده.
به گفته این مقام، توی این برنامه، زیرساخت‌های حیاتی اسرائیل و تأسیسات انرژی آمریکا تو منطقه هم جزو اهداف در نظر گرفته شدن.
نیروهای مسلح ایران توی جنگ 40 روزه و اتفاقات هفته‌های اخیر نشون دادن هم توان انجام چنین عملیاتی رو دارن و هم برای انجامش اراده لازم رو.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69338" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69337">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4mWBba1DDh37q46m-MaBRqo1EWeZUfTZf0XensmmTqCX-Lo91v8ZvHcMXRtcgBXHpiwPQid_llf5fn45kK0P2DTKDJNqcjgYkg7mOIgB9F095tTJUndZHjQAUTWH623eXGM8F7i19BKrpLxODTNbhj7P0ODibeMtGg19FHrOAz2fQjI3IBdFOQgtDH8kjBlnW5ZYXEhC99H6MQgjqfuBrghW2dbykXQXG8u2JAQYc4M7Rv27GzdYrvid-JfSIoGdjGcJFDeGOyCNsmES7QSKWzgpPvGceBoyT08w4kBLoDpqxmAVBaFd1m6kACOSoPbsugXyx9FAd3SLOiUSbfIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛آکسیوس:ترامپ در حال بررسی حمله به تأسیسات انرژی ایران ظرف چند روز آینده است.
یک مقام آمریکایی روز جمعه به «اکسیوس» گفت که رئیس‌جمهور ترامپ به‌طور جدی در حال بررسی انجام حملاتی علیه تأسیسات انرژی ایران در چند روز آینده است، اما هنوز دستور نهایی برای اجرای آن را صادر نکرده است.
این حملات همچنین ممکن است برای نخستین بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدید تنشی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین بار درباره حملات احتمالی گزارش دادند.
ترامپ در آغاز جلسه روز جمعه کابینه، با اشاره به حمله احتمالی گفت: «خب، ما ضربات بسیار سختی به آن‌ها وارد خواهیم کرد و می‌دانید، بالاخره زمانی فرا می‌رسد که آن‌ها خواهند گفت دیگر تاب و تحملش را نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69337" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69336">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbBtKRY8751TkkaaQj45PU_sE7E0fJj2KRVCGwyiUWRso6Yi1naHifbf_i-BmonjhkXToh450rRHw-1-Gsjh-TW-QF_7zpzCt9PVsWZNwrC4wsm8OPo8uekxXidCZ4pMNFPibKGy3dzQwBARRn6k_fKQBjQULJTg-wjvlt9vv4nQiTvZ_UbTeiYaYx3JNScafEjbg-4c3O9LNr86caakdenQcKva86GwbvaiIkKta9jqU23BKkXOXHzTvsM7TG2mRSSu2_n6XJ875tc0P2k-r-Rl6-4wi26l8WsszVURN2hU4o6aTXmaSfX9T4dmcvMEvh1JT-PdxXqRFVvKYyN9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
سی‌بی‌اس نیوز:
ایالات متحده و اسرائیل در حال آماده‌سازی یک کمپین بمباران مشترک بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده است، اما حملات ممکن است این آخر هفته آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69336" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69335">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5040574e14.mp4?token=M4Ufjbj5cX4EFZyxkI6qHWM42Ubz4PTiF3OiYbByOaLQgPN2W0g7u5TYMjB_UaifE3zzVoX--FUjJ6kPNDRAuQuY-42eE0SfvF3h0ZsGw8jtm7FY2sFKRw4sEcKMsYDsovDo_CijSSgLCqAgsi2bGlo0nQDQCS7y-Jl0h_TvubpvYYWpcIbDRFi5A1FpYNLzJW3Da5Gr5vFittY4gGQlDxzTiEoS-LwFTQzODc3BeELVosFtzh6vQeIadH5kaR2hD-fzIiNYN_8LowJHebM7QfH_kfXcV1aJaAn7SS5XypRaYqpkVFAKism3h6pFY6QMAD9oH89Ksg898RWBBdHm2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5040574e14.mp4?token=M4Ufjbj5cX4EFZyxkI6qHWM42Ubz4PTiF3OiYbByOaLQgPN2W0g7u5TYMjB_UaifE3zzVoX--FUjJ6kPNDRAuQuY-42eE0SfvF3h0ZsGw8jtm7FY2sFKRw4sEcKMsYDsovDo_CijSSgLCqAgsi2bGlo0nQDQCS7y-Jl0h_TvubpvYYWpcIbDRFi5A1FpYNLzJW3Da5Gr5vFittY4gGQlDxzTiEoS-LwFTQzODc3BeELVosFtzh6vQeIadH5kaR2hD-fzIiNYN_8LowJHebM7QfH_kfXcV1aJaAn7SS5XypRaYqpkVFAKism3h6pFY6QMAD9oH89Ksg898RWBBdHm2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مهاجر مراکشی درحال رفتن به منطقه برون‌بومی اسپانیایی «سئوتا»
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69335" target="_blank">📅 01:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69334">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.   مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69334" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69333">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozYNII70pH-AYG3c08M5kQM4x7qUqG_F3TS3VOD6RXodNUzsIWTrbzv_jfZTjQyG1sfel9uq3IqgOsXtLw6FnbBhAdRm4OK3WvZsXLUtyFTjRRJ9_F9enQYSexT3BndV2QaID-T0clC8XzoptG9sMQ6ABTA44jLI-FCUI7rrT5yXijVoqErrp972fJbJlJyfgMDEo5hmByXyAm-4qMqhM5Je7dIhqb1QVT7u8Eh2XVCLClO9cqA8KK4rQlq60rTdtNb12GWeKcuXUOAsnJWL8HYDc3Qdo3TgoQ1f0_B--zCcioraEEd2B-J5kr9Dd-n1F-N1th6cycEZGXBih4RfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.
مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند روز به طول انجامد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69333" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69332">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چندین منبع به CBS News گفته‌اند که حملات ممکن است در طول آخر هفته انجام شود</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69332" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69331">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=JDCTuWpxtfFaSiMMw_dmUvpPLl6WROkTHUj9Xvgy1rwdh1ejLGVCxydAFNCUgUNQKHzdHjKnV4Qi7cAUvqEKOQNF48fHZ04vmleRmrDDksLWAzllQBx5ohNPCNiaEnrzjcOy2mFl5c-Z9nM3RB85ZVYska9Go4zicnIOzHzgZCTk8GcQodeObspEf3q95V3obZ2yCQG_6ZUzt8n3Rozi_ZJ6nPN_6m6yPnOJsvp4kQc999fZOMp35wqUkojm90_4JkXFFWSM3sMWt5YrLyYD46PJG21Bxj0LAH1LMMTwE8BGrVXkOCRT1vqsjNM3DMV9VIzpytRHD7fVUx5lOnuFsBHhcsXxzc85o0LjQn1FlFvZmlXBe8LqPlNzScicEtgkVeSJErnWV8Y9cZw9Y7jiHxydx4lSjDVX0HkpcRtfQ5ThRvd17nDByz9AOcEHvFGzotrR8lxZIPImY9eh3CLg99lmZ9IW8ETrj9ER7Lw6Vo0we2CFKVEE8yb01knXPEtifwrTjzHIT1PEUYqUYebR5ossSlpU3KtY4pZ5E_RD-UwmP6q4SUDaIwNUL2M7t5unwa9TVMJwQJLD--FKcWp0rQfJotP5unboiLMbPHlNDqL7p2Cx3ljJRPf4Rw-4V6wNjLn0PHgvp6JhF2SZcow8KHSBYuJqpOOnLrk5yTqgg90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=JDCTuWpxtfFaSiMMw_dmUvpPLl6WROkTHUj9Xvgy1rwdh1ejLGVCxydAFNCUgUNQKHzdHjKnV4Qi7cAUvqEKOQNF48fHZ04vmleRmrDDksLWAzllQBx5ohNPCNiaEnrzjcOy2mFl5c-Z9nM3RB85ZVYska9Go4zicnIOzHzgZCTk8GcQodeObspEf3q95V3obZ2yCQG_6ZUzt8n3Rozi_ZJ6nPN_6m6yPnOJsvp4kQc999fZOMp35wqUkojm90_4JkXFFWSM3sMWt5YrLyYD46PJG21Bxj0LAH1LMMTwE8BGrVXkOCRT1vqsjNM3DMV9VIzpytRHD7fVUx5lOnuFsBHhcsXxzc85o0LjQn1FlFvZmlXBe8LqPlNzScicEtgkVeSJErnWV8Y9cZw9Y7jiHxydx4lSjDVX0HkpcRtfQ5ThRvd17nDByz9AOcEHvFGzotrR8lxZIPImY9eh3CLg99lmZ9IW8ETrj9ER7Lw6Vo0we2CFKVEE8yb01knXPEtifwrTjzHIT1PEUYqUYebR5ossSlpU3KtY4pZ5E_RD-UwmP6q4SUDaIwNUL2M7t5unwa9TVMJwQJLD--FKcWp0rQfJotP5unboiLMbPHlNDqL7p2Cx3ljJRPf4Rw-4V6wNjLn0PHgvp6JhF2SZcow8KHSBYuJqpOOnLrk5yTqgg90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«قیمت‌ها حسابی اومده پایین، به‌جز نفت.
دو هفته پیش، وقتی همه فکر کردن توافق نزدیکه، قیمت‌ها مثل سنگ سقوط کرد.
ولی ما یه
توافق واقعی
می‌خوایم، نه یه توافق الکی.»
🎙
استیو گروبر:
درباره ایران، فکر می‌کنید چقدر طول بکشه تا این ماجرا تموم بشه؟ یه ماه؟ یه سال؟
🇺🇸
ترامپ:
«پیش‌بینی کردنش همیشه سخته.
ما ماجرای ونزوئلا رو توی کمتر از یه روز جمع کردیم.
اگه می‌خواید همه‌چیز خیلی سریع تموم بشه، کافیه به یه عده سلاح هسته‌ای بدید!
اون‌وقت همه‌چیز خیلی سریع تموم می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69331" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69330">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=i1_BvXy8YSiOmB-GbzwFdM3pJDv9v_3teF7Towud43RI0QCytI84th3mysbcf_4JBINHh4_nDcUEEt1pBkr79MPcUN9JNZxSA8eRtlSqzasPLHjf0n4o1Drgj5GA-_BJPg63Yqr3q7LveaqFWfZhc8rM2GAjF8Szz4zg0_F8hMa7HmkstN4tsbgrMYc6Mii_hHsHSuMTv4UiETpYUZnY5zAU6hDL8Lhd5boUFdoAJ0QfUUiuknHPPYTkTNWS9zNspiS4iF9gE7udGBIE9hfGVHFfy3QxqnfePX698YRSlqxlFfCmfXd4zKHdL4o4CyNp7Bc-koCeiX8UNlRv329ZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=i1_BvXy8YSiOmB-GbzwFdM3pJDv9v_3teF7Towud43RI0QCytI84th3mysbcf_4JBINHh4_nDcUEEt1pBkr79MPcUN9JNZxSA8eRtlSqzasPLHjf0n4o1Drgj5GA-_BJPg63Yqr3q7LveaqFWfZhc8rM2GAjF8Szz4zg0_F8hMa7HmkstN4tsbgrMYc6Mii_hHsHSuMTv4UiETpYUZnY5zAU6hDL8Lhd5boUFdoAJ0QfUUiuknHPPYTkTNWS9zNspiS4iF9gE7udGBIE9hfGVHFfy3QxqnfePX698YRSlqxlFfCmfXd4zKHdL4o4CyNp7Bc-koCeiX8UNlRv329ZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توی درگیری با ایران، بسته به اینکه چه آماری رو حساب کنید،
16 تا 18 نفر
از نیروهامون رو از دست دادیم؛ که همین هم خیلی زیاده، چون حتی از دست دادن
یه نفر هم زیاده.
جنگ ویتنام
21 سال
طول کشید. ما تازه وارد
ماه پنجم
شدیم، ولی همون‌ها که آمریکا رو 21 سال توی ویتنام نگه داشتن، حالا می‌گن "چرا ماجرای ایران این‌قدر طول کشیده؟"
من الان دارم کاری خیلی بزرگ‌تر از چیزی که اول گفته بودم انجام می‌دم. قرار بود فقط وارد بشیم، توان نظامی ایران رو نابود کنیم و برگردیم.
ولی بعد دیدم اگه فقط این کار رو بکنیم و بریم، دوباره خودشون رو بازسازی می‌کنن. برای همین باید یه جور
کنترل و نظارت
هم وجود داشته باشه، وگرنه دوباره همه‌چیز رو از نو می‌سازن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69330" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69329">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=mEIWpyg-FmMLeSftVAAEcujlHvanACa1d2rosvvRcU_Hv69o5yTP4npA8SxfEGiPcW4fx4bvTzWeEml6vTuTo2Jb82XflADRpxfQmQrcohXc6n63X-Im2TzERwG4Myuk3v3KNm8hVpDpX_G6qIMcUdBVajb325vwxFL4McoAD5Kjl4VEO6F5LU9EqSY46UbFUQ5uL9uvJpWaBgK5mhgWHjHxjH6WZQhfFI9uq8xf0IEKRrFLeXk6VWeY430g9RZNcWDu8o18-dOwKAmIfxp8L-y98rcy_ShGCl8MyeReelzngfTNgU6Sc1aXEc0y2UhMshvIoHeHV8IyEjHN1XYlZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=mEIWpyg-FmMLeSftVAAEcujlHvanACa1d2rosvvRcU_Hv69o5yTP4npA8SxfEGiPcW4fx4bvTzWeEml6vTuTo2Jb82XflADRpxfQmQrcohXc6n63X-Im2TzERwG4Myuk3v3KNm8hVpDpX_G6qIMcUdBVajb325vwxFL4McoAD5Kjl4VEO6F5LU9EqSY46UbFUQ5uL9uvJpWaBgK5mhgWHjHxjH6WZQhfFI9uq8xf0IEKRrFLeXk6VWeY430g9RZNcWDu8o18-dOwKAmIfxp8L-y98rcy_ShGCl8MyeReelzngfTNgU6Sc1aXEc0y2UhMshvIoHeHV8IyEjHN1XYlZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه هموطن که تو خونش کره خر نگهداری میکنه و بردتش رو تردمیل تا دلتنگی بیرونو نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69329" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LigTAYS8E4vc62yzkvRJlZBN1FWJR9NcHTz4mObplVqHel_DqyUNYz8x3biLM8TuDgWw9srXIwM9mcAC7lYSwcSYRo8x91_8uGBnaw7HTmhJr4IiRXo7MBE-nXvRgiaq4x5WyBiIbIaR0Z4_I17aYM4pnvsu-UnJi3qHmhOjRadhg9jkF3NDdZrx-A75MnzrBHAaVPYbJzR5zwZbT5M20_iLkjzIEOL1Si7oXY0VEdY12Ep4un8zLfJqsB58AEQ8pb1if4K6pRalOSUvuSo9WmyyjgtAbbPk2hPaC0Ex3ZFPt4TzbhdeUhs6-gc0QElI3LUuFYdqDyd1ISqg_f4mqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=CAoDxYXkdDbXtANdLR2AIifwjfnQSgLbNE-Pz4FcDh-IYV-ACeHCPWhK66bJaoGqGNcv6WnT0nDtPJ9WdfXLxTettrb2HnUji1h12TsLKq4TLKAA9M1_8Tk2zBxI3XcENWnIm6Y7GWxTicQgda-2Odpa1lG-um4iuQ3FgHeZ6GrlbYQkL6PzLPy-7VAMl0YGt4xwvTegKK6pot2WYXPWBcSZoMxDawVZAQwAY7RbbsN1kLqB3BZuAbsYsshu0RAbSLklTj3k6feJwzwQyI-zwdZg1tSARG_3jmTJ0j3hfROdMiM_Y4u9PqBNe3N5hl8ei9_5n6cK8LaEhg1JfIzymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=CAoDxYXkdDbXtANdLR2AIifwjfnQSgLbNE-Pz4FcDh-IYV-ACeHCPWhK66bJaoGqGNcv6WnT0nDtPJ9WdfXLxTettrb2HnUji1h12TsLKq4TLKAA9M1_8Tk2zBxI3XcENWnIm6Y7GWxTicQgda-2Odpa1lG-um4iuQ3FgHeZ6GrlbYQkL6PzLPy-7VAMl0YGt4xwvTegKK6pot2WYXPWBcSZoMxDawVZAQwAY7RbbsN1kLqB3BZuAbsYsshu0RAbSLklTj3k6feJwzwQyI-zwdZg1tSARG_3jmTJ0j3hfROdMiM_Y4u9PqBNe3N5hl8ei9_5n6cK8LaEhg1JfIzymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=vGVNN8XvY0ndDnw-fCwVH8IY_fir4BPsh1THnCIg8ytgKTFVqNYGCDWsbmAxlOCssKmSq89nxi-TJ_XtW4vz9U-MthtTEOH3_fIqOrmXtQALq6-AZCRQBWnUu6aegFZpts1Od2QJfUa42W-bpm3APp8SDXUrduvuH62bKAgcRS8j3IMmObqeBFPRZJ-QrDbMaVQdjlQbWm2S2psP7ppSdnH0FZSxWBxGhrZtdB-X73uR6sWxV-Z77wj5TGTis7K4zz0VRRnWqanyLISOp9YisqCWdjCZCMNrcv9l1In_s1td9a5q2G8mjOKTziokLe02hxjhrdZ97iyoDdmefOYmYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=vGVNN8XvY0ndDnw-fCwVH8IY_fir4BPsh1THnCIg8ytgKTFVqNYGCDWsbmAxlOCssKmSq89nxi-TJ_XtW4vz9U-MthtTEOH3_fIqOrmXtQALq6-AZCRQBWnUu6aegFZpts1Od2QJfUa42W-bpm3APp8SDXUrduvuH62bKAgcRS8j3IMmObqeBFPRZJ-QrDbMaVQdjlQbWm2S2psP7ppSdnH0FZSxWBxGhrZtdB-X73uR6sWxV-Z77wj5TGTis7K4zz0VRRnWqanyLISOp9YisqCWdjCZCMNrcv9l1In_s1td9a5q2G8mjOKTziokLe02hxjhrdZ97iyoDdmefOYmYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVURUujawD0aAQmeubHvcuFoI5b41c8iGbWz9yYWI0C66Te4QcnLj17dCX45zH3h-QpTPRvT2_Tz-Up3TB8lITti-4lJyHwZKL7Papl27Z2H7e9UhIPYe_8QM50CCPB7fwp2YEKEdU-0YByA81UBJfuielMsojYjGNQleXjyyL2e3EfcBbK68YNlbUDwLLax9IWrnLa0hL4dQYuxyXpjPw2vwVwUj2w_NHBT5e97DUMm-gE6UiK8T-MqeKsfINLxUBjfN_kmOlXxvt2-yaOJnlNFJa_HWplL2avOebjaXIlo01EA3mEkJe9c_0wgraX6Wfi_XO3B3xgHhYRuO9H1m8zUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVURUujawD0aAQmeubHvcuFoI5b41c8iGbWz9yYWI0C66Te4QcnLj17dCX45zH3h-QpTPRvT2_Tz-Up3TB8lITti-4lJyHwZKL7Papl27Z2H7e9UhIPYe_8QM50CCPB7fwp2YEKEdU-0YByA81UBJfuielMsojYjGNQleXjyyL2e3EfcBbK68YNlbUDwLLax9IWrnLa0hL4dQYuxyXpjPw2vwVwUj2w_NHBT5e97DUMm-gE6UiK8T-MqeKsfINLxUBjfN_kmOlXxvt2-yaOJnlNFJa_HWplL2avOebjaXIlo01EA3mEkJe9c_0wgraX6Wfi_XO3B3xgHhYRuO9H1m8zUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=JC6fFMHBkFiH_qW3TOEeMGG311JF54E0wQWZS-WkqYosA_toSol8s5bFkiYsDMu9WsQgFkKDq7JW_tvZaz7mC-buTtFGPxgxQHZg6gdy1EbQ-fgKgQfMWv9YYLcV2P25e-FqEP_zP11U3-4wUgrZLMHdckPbSizSVa2J5s40MkyLQj2uPnCNCZ7EcWD2j8n6rQ7z4Zv7n53oPwdHmH2mkBD7hFsu-2BDonEQWUPnouRFZYis7X82VTUCqxSHzv4m9C5gTKkWe-IzoaWqzfPhuRpqH9fU7BqgXQZR7o3zzZJ9f3CKIvM48UuCHQ9T7oZbd87M8F_Z0bip7kLb-fzZwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=JC6fFMHBkFiH_qW3TOEeMGG311JF54E0wQWZS-WkqYosA_toSol8s5bFkiYsDMu9WsQgFkKDq7JW_tvZaz7mC-buTtFGPxgxQHZg6gdy1EbQ-fgKgQfMWv9YYLcV2P25e-FqEP_zP11U3-4wUgrZLMHdckPbSizSVa2J5s40MkyLQj2uPnCNCZ7EcWD2j8n6rQ7z4Zv7n53oPwdHmH2mkBD7hFsu-2BDonEQWUPnouRFZYis7X82VTUCqxSHzv4m9C5gTKkWe-IzoaWqzfPhuRpqH9fU7BqgXQZR7o3zzZJ9f3CKIvM48UuCHQ9T7oZbd87M8F_Z0bip7kLb-fzZwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=la_cqTrkSSgoUulQNCFvV_UDfdxHFjqhGrFjZXKRqrLpCmqmdQFM6Wxp9WwVilI9Iucd66XIw-ZQyTumbzqr3yuO1mC0on-wUbL34gMfq9RnR2SjKtlM1qAI-zsV304hREleSE5vzNXdD_RDsjKY3rwwq9WVdvz_umhczZpvRKf9NSdQjniGFBVZa0DLz-EAjfHZPywLdPYFSHCYTpD7tNY2b8LXiM5zMEq0OWyhYFurc3-_eajmTIhySTtPsAxXeb3h709lgzs0_x7_BJH_mhB5NdZ_53vnddTSnrTuWa3TunHR059Gg56DHOCfbKLoEfQmsIN3K5C_UwKm6BnYDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=la_cqTrkSSgoUulQNCFvV_UDfdxHFjqhGrFjZXKRqrLpCmqmdQFM6Wxp9WwVilI9Iucd66XIw-ZQyTumbzqr3yuO1mC0on-wUbL34gMfq9RnR2SjKtlM1qAI-zsV304hREleSE5vzNXdD_RDsjKY3rwwq9WVdvz_umhczZpvRKf9NSdQjniGFBVZa0DLz-EAjfHZPywLdPYFSHCYTpD7tNY2b8LXiM5zMEq0OWyhYFurc3-_eajmTIhySTtPsAxXeb3h709lgzs0_x7_BJH_mhB5NdZ_53vnddTSnrTuWa3TunHR059Gg56DHOCfbKLoEfQmsIN3K5C_UwKm6BnYDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=eXkvxRNdVMiU-BHEFuudWaoce_hgNFcxVXgUq5rhlgv0SIJ97xdQULLpZB_JLCNjClYVOSoD4ZnWKGnpsgC88jjsP3CZWQHwqw0xPSX071U7niM52rYnO4wZ-5USPI7J8WhpMBPc7Pb9aawTud_oMYED1Bfi-k3HHbxIz0gtJ9zysh0YOLecAYSDy6rATCeyi064-YN8KcptgKPoYHT5mbUJVoXU09z76U0PqwidcgnnHtVKVZlCg5KCgf6l4epLkwPUFcFUMqXoDO23ywEpK1vrjwOIKCDveLYhGFwPx4obd0M2OILGnFBhPjAHJzJiha2rwW8w6CiFl8UsrS4qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=eXkvxRNdVMiU-BHEFuudWaoce_hgNFcxVXgUq5rhlgv0SIJ97xdQULLpZB_JLCNjClYVOSoD4ZnWKGnpsgC88jjsP3CZWQHwqw0xPSX071U7niM52rYnO4wZ-5USPI7J8WhpMBPc7Pb9aawTud_oMYED1Bfi-k3HHbxIz0gtJ9zysh0YOLecAYSDy6rATCeyi064-YN8KcptgKPoYHT5mbUJVoXU09z76U0PqwidcgnnHtVKVZlCg5KCgf6l4epLkwPUFcFUMqXoDO23ywEpK1vrjwOIKCDveLYhGFwPx4obd0M2OILGnFBhPjAHJzJiha2rwW8w6CiFl8UsrS4qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
