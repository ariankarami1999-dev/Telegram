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
<img src="https://cdn4.telesco.pe/file/qBBaAtJ09tqvVINbISTTwahx4ofkV1RKngVrJ9Eeste1H3iMP4chdLAZpmp60wnbsh_cAzFXkqo1vmsTBLRfqzSV2R0AEDvEiUln6FZDIixY5vqyDUSKjOUD7rFO0yetAuybAkzsPNsBwHp3KjDzzqG7YaOhUVqqX25Q94bFwvvbLt4ydZnFi-h8q403kyHPdENwSH54eQxKyfmaVE06bYz2Znw5ml0z75fIbF5QveBIVvv8pfxsALAMaClIArhJDQhGaP_x5EL0G29SVnd_fol_y03EB2dKd-ConnDkgY6CDthm389Ayv1LZai59yyvDtsR721VZKG_pwKn-DaFJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 21:36:25</div>
<hr>

<div class="tg-post" id="msg-685638">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رویارویی کشتی‌های جنگی ترکیه و اسرائیل
شبکه کان اسرائیل:
🔹
اخیرا کشتی‌های جنگی ترکیه به کشتی‌های نیروی دریایی رژیم صهیونیستی نزدیک شده و مسیر دریایی آنها را مشخص کردند.
🔹
نیروی دریایی اسرائیل برای مقابله با هرگونه تحول در دریای مدیترانه، سطح هشدار خود را افزایش داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/685638" target="_blank">📅 21:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685637">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1dyGh0VBViijdZk7R78EJeB_F8QeCp5nf6VZY2XySWajmHrZq-EfIphJqo7a16-ah7M65ueYKRbJy6ZT4qCZ1-lzuUPaMF3nqkjnrLO8PdEymCOTjlKuIlVuf-_ZU1GtpUSq4EkjV4atS7LvekKEO1dXdq1MlOJlX6AjICOVEhtTnB1ccaDmwWn_0QJDeFh7MmzGKLwvxXdM9JtTO_V4X12JdQcYI_ofTjXwCkeBTaPqTwIj3dmBfPx-Q3qIi0GiZW5m9AlQ5vR8Y0hpLME0uZNAJVnsjKxIQ3wu6DW7FCkK0NAqa-wJ3gwh2Ss_RvWVihuxkonw0CJZKwLDG6aJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوکیا ساده هم به ۸ میلیون تومن رسید
🔹
گوشی‌ای که سال‌ها نماد ارزونی تو بازار ایران بود، حالا به قیمت عجیب ۸ میلیون تومن رسیده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/685637" target="_blank">📅 21:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685636">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a490610f9.mp4?token=OdIfQLEOEi1gpq0AUglJ9SNkqnu0cm-rGwrSXhLcZNJFRdHqSU7n0FxZksvkjtU28UFlc_--mnCazOraq6ppYTRfEDNnZp_HM1HJzfGxaW7X9iN1E8QCtStoLD9c2djQ7cmvRGSWx2FomKiqhp7X3KxK0Km15YYTO4xEA5JJRiWaNATRF_ZJoucWDFBn1rxhVuauw8OMbRmFNcxQ2c6yA73nMfTssa9YxsYG1F3dQBRvGE0PJEbuxE73EsmSnesWP31BdoNpP8i6JOCM8V2EKb290Uc0hOVe0wUfabCF38aICHh24qMX59WsB1JCa-6ItBH7cV3EJfkUXsJXenEFOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a490610f9.mp4?token=OdIfQLEOEi1gpq0AUglJ9SNkqnu0cm-rGwrSXhLcZNJFRdHqSU7n0FxZksvkjtU28UFlc_--mnCazOraq6ppYTRfEDNnZp_HM1HJzfGxaW7X9iN1E8QCtStoLD9c2djQ7cmvRGSWx2FomKiqhp7X3KxK0Km15YYTO4xEA5JJRiWaNATRF_ZJoucWDFBn1rxhVuauw8OMbRmFNcxQ2c6yA73nMfTssa9YxsYG1F3dQBRvGE0PJEbuxE73EsmSnesWP31BdoNpP8i6JOCM8V2EKb290Uc0hOVe0wUfabCF38aICHh24qMX59WsB1JCa-6ItBH7cV3EJfkUXsJXenEFOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملکرد جالب دستگاه فروش خودکار از موقع پرداخت تا تحویل کالا
#موشکافی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/685636" target="_blank">📅 21:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685635">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QahA3tbCtFNK6B2c3X5_hl1jI5OoKfCVpFyfqFJ_kyglC46Guhxup0o_YP7BgP1uBAB5KtN9vOq04Kx2-lmIyn66Ias5gwzB8uetu57qxI-vTthHFwSmXp0ToAq7DUFYnbxYJA-eQy9h7XPnfNGr0BwJFLQtEa8sq-RgV9PsmdCRSSDIl0E9Z3JKYw8Ah-uCdqLP7-Zco-Nrt7SdE2LJlpbK3Sv3qecWRW1UbpP9C1Auxi8WQwLWV2sNU9ahofZqWtgM54TJpat3GsPH65oDzSHyXNKT8z4ulgxl48yfMHBzy8rMczobSUgZZHvS9VbTJIIDSlPk-vBVHV6tL1RhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای مرموز فرار پسر نتانیاهو از آمریکا/ چه کسی دنبال ترور «یائیر نتانیاهو» است؟
🔹
چرا پسر نتانیاهو را به سرعت از آمریکا خارج کرده و به اراضی اشغالی بازگردانده اند؟ آیا واقعا قرار است گروهی نتانیاهو را ترور کنند؟ آیا نقشه ای برای دزدیدن پسر نتانیاهو کشیده شده است؟ آیا میان شایعات در رابطه با ترور پسر ترامپ و حوادث مربوط به پسر نتانیاهو ارتباطی وجود دارد؟
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3241559</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/685635" target="_blank">📅 21:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685634">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8fbf2e61.mp4?token=Na6QjscnvqawcxmhtusLoej6wPvXxvuJbYXnUIK7j66PbkMjMThpL5AIqgqxwG8rlmVRwaQBaW65TQtqCN4jWogakXanCz0hJ444GFHZhjmQwtaD3GX3uyNWwEQUym8alHy1aiLzTHxPG2jDY7RQoep7Frd0y4-er6XkzyXH3PcxL1-kO-Oa-ewCiVa5AJpARoZs3t4rGq99avNEWQcf21DUKeHWqM_LuYs-vRilTAKdxb4PKBsdx0hSbaYsxID1ea9WXUjJ9h0x59An_KLPMXUtr51JdiKlBYfY0C_NMji7LldAKXeuoceljvs9n3KGz36z4AKpJnm5Z61iIRncDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8fbf2e61.mp4?token=Na6QjscnvqawcxmhtusLoej6wPvXxvuJbYXnUIK7j66PbkMjMThpL5AIqgqxwG8rlmVRwaQBaW65TQtqCN4jWogakXanCz0hJ444GFHZhjmQwtaD3GX3uyNWwEQUym8alHy1aiLzTHxPG2jDY7RQoep7Frd0y4-er6XkzyXH3PcxL1-kO-Oa-ewCiVa5AJpARoZs3t4rGq99avNEWQcf21DUKeHWqM_LuYs-vRilTAKdxb4PKBsdx0hSbaYsxID1ea9WXUjJ9h0x59An_KLPMXUtr51JdiKlBYfY0C_NMji7LldAKXeuoceljvs9n3KGz36z4AKpJnm5Z61iIRncDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیرکل خانه پرستار: اگر کشور با کمبود پرستار مواجه است، پس چرا ۶۰ تا ۷۰ هزار پرستار خانه‌نشین هستند/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/685634" target="_blank">📅 21:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685633">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhHw5VXCVxg1q3YsyYXBR3f0LiFX0ufm4h4TNUY9x9pVBWSeFGrd1PAIVRJ-iA37y195XPV-xe_STDZK_FvQw_gTsSL4rbqJy69xwVgXVh-rMVGvUrQXdObUWq_6HJcclKmskMG3GZ-lAA7BUTtZsPeWsu0MTVdjSN44OQjH68gssz-7git-7-FC8Er_9wTPKnFITKM9Qj6k88T0NBkIMSXdFZKAivYme6ewiNnXqPymfcmFBV0raZbcRcA-DSsByuRX3rborKPrCIiTg0HbwTI-g7Kf8CXv6jElycmhBqwFLjAFOt5wyja-blGYDOdhQEzbf6H8x9gpniob0kmgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان اطلاعات سپاه: دشمنِ مستاصل از مقاومت ۲۰۰روزه ایرانیان، «فرسایش ثبات و تاب‌آوری ملی از مسیر جنگ روانی» را دنبال می کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/685633" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685632">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb9e28a81.mp4?token=DUx5o4IOk5oVgYzQvz4HakFiZgcEwfD-E4M1mmkEIg6MHSqjRFaCn9FTsKcxfLO3WK_nyBHmgkfCq1ekwVLZ7oVa8grIw6Dkwgj5dLmLlwSOaUpcajCNEkPC6u5FT9HuSDnYdOZ1YsgVOvYHUsbcIiLm2HCcx8nHKgNTaHzOXxTg5GJmdAiPrzlt2lvvIQqa3YAARxa4C06oxzuL5btzZviNSBufIO6Su4QsM0XgixFodt3CVITAx_eBdEv1V_nGzNF7RX_hcjNUrtswkHEtjPmFru6NNd4s3UlMMKTl2XDRgDbkmA5882rwZkOBMjomipwqATudoUshZNMtuygO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb9e28a81.mp4?token=DUx5o4IOk5oVgYzQvz4HakFiZgcEwfD-E4M1mmkEIg6MHSqjRFaCn9FTsKcxfLO3WK_nyBHmgkfCq1ekwVLZ7oVa8grIw6Dkwgj5dLmLlwSOaUpcajCNEkPC6u5FT9HuSDnYdOZ1YsgVOvYHUsbcIiLm2HCcx8nHKgNTaHzOXxTg5GJmdAiPrzlt2lvvIQqa3YAARxa4C06oxzuL5btzZviNSBufIO6Su4QsM0XgixFodt3CVITAx_eBdEv1V_nGzNF7RX_hcjNUrtswkHEtjPmFru6NNd4s3UlMMKTl2XDRgDbkmA5882rwZkOBMjomipwqATudoUshZNMtuygO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دزدگیر گاراژ بهانه‌ای برای یک دوستی شیرین؛ مردی که بازی کودک را جدی گرفت
🔹
مردی متوجه شد کودکی هر روز وارد گاراژ خانه‌اش می‌شود و دزدگیر را فعال می‌کند. اما به‌جای شکایت از خانواده‌اش، برای کودک مسیری نقاشی کرد تا بتواند همان‌جا بازی کند و بیشتر خوش بگذراند. هر بار که باران خط‌ها را می‌شست، دوباره آنها را برایش می‌کشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/685632" target="_blank">📅 21:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685631">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0BpiZxlYCMbvogg6WaIPTZOJE-CRxH8RSHzbDoHmv3T919_EHqsNmAkJngNO-4_Vreu_P4xtcRchDS9tTTlBCnZhqLwACjKRCJ0sALrmAg3VPTYAMyETbWTrONqIo1VKtb7A50nTBZlVIxTClBLi1szmgkxm09F9TPFxTGow_UV1hCcMX7q2T2QLLFW1_oyfbnr9RzDVUiM-pH_dtD3ud1CZCoMGO_YfRB28KQiec4rh1_p4U1FiO4fHbHA4j4-TA7y2PIDCG_KNQ7VYpO8X3NcE-nTW7_EaGLqgWhaaMrtcO424kJyEqSuHitCS8pBvatjRWGWpggls3HDjHvQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهمینه ها هنوز هستند،
تنها جامه شان عوض شده...
گراد، با حضور خود در دنیای زنان، به سراغ یک روایت اساطیری رفته است؛ نه برای بازسازی چهره‌ای از گذشته، بلکه برای بازخوانی معنایی که هنوز در زندگی زن امروز جاری‌ست.
زیرا زمانه تغییر می‌کند، شکل زندگی تغییر می‌کند و جامه‌ها نیز؛
اما بعضی ویژگی‌ها، همچنان بخشی از هویت ما باقی می‌مانند.
انتخاب. جسارت. خرد.
این‌بار، روایت این زنان را بر تنِ امروز می‌بینیم.
www.gerad.ir</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/685631" target="_blank">📅 21:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تاکر کارلسون: ترامپ باید فوراً از سمت خود برکنار شود
🔹
یک روزنامه‌نگار برجسته آمریکایی با اشاره به اظهارات رئیس‌جمهوری این کشور درباره از بین بردن تمدن ایران با سلاح‌های کشتار جمعی، خواستار برکناری فوری دونالد ترامپ از قدرت شد.
🔹
تاکر کارلسون در این رابطه گفت: اظهارات ترامپ درباره استفاده از سلاح هسته ای عبور از خط قرمز است. هر مقامی که استفاده نخست از سلاح‌های هسته‌ای را مطرح کند، حق خود برای رهبری را از دست داده است. او باید فوراً برکنار شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/685630" target="_blank">📅 20:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554cabedad.mp4?token=e2e9AuE0rF7MG0X5cMHLc046PfDqEp_qcmb6k2iM22kn4Nuh47HWXOKvPUoG3gyRk6tl12sHrd7EMtVBU5JO7VHR4YTpDdWlyB4M5A9pyfHYeEr4WNmPyiokzbRa9APt8fJE_-VDk986UZ55OJ3IzBLQLTodzVzSBU6p20m4rIP0ZZmKOHwiF8P0LUmY1ldXXrKXRvH2jBodyWH7JBdYjbkAFEH_0SRE0aCnhzKYKi1POyFJ2buVScXiUBmwqBoFP6_Xt1cVacQassDVdMWgiRS3q9rKGlGb6zY3POj7AAEcc1HCcEivD55kgIvZe4c3ak7WFqkHGtLh3wj2Bzxwcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554cabedad.mp4?token=e2e9AuE0rF7MG0X5cMHLc046PfDqEp_qcmb6k2iM22kn4Nuh47HWXOKvPUoG3gyRk6tl12sHrd7EMtVBU5JO7VHR4YTpDdWlyB4M5A9pyfHYeEr4WNmPyiokzbRa9APt8fJE_-VDk986UZ55OJ3IzBLQLTodzVzSBU6p20m4rIP0ZZmKOHwiF8P0LUmY1ldXXrKXRvH2jBodyWH7JBdYjbkAFEH_0SRE0aCnhzKYKi1POyFJ2buVScXiUBmwqBoFP6_Xt1cVacQassDVdMWgiRS3q9rKGlGb6zY3POj7AAEcc1HCcEivD55kgIvZe4c3ak7WFqkHGtLh3wj2Bzxwcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی تماشایی از رنگین‌کمان در پس‌زمینه کوه‌های یخ شناور در نزدیکی گرینلند که در شبکه‌های اجتماعی سراسر جهان پربازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/685629" target="_blank">📅 20:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685628">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13dc475bc0.mp4?token=VSCk_KMMWrlsNKHyib_0P7areIxQyTkFVnpgoDCS3s8ot72Nlgp1_C3UNs95Xs4UtT7OTxbfF4YvE1fu159G1MbLzwLB3wztdS5kWpkd0otMfS_I7f_hdQ9jM7h9kHL472iGattmIoOK4Ir133CZ8y_9UmjpXfcUMFpESv-QnYLeRVcfJhBWWOu75LMGwlIbzv4PcZUARqzpWyebCRyAjHRfRF133sf_P85_Y92LLsrHufC5LKGd_OsxVJiojAFgTmEb-d78hQw8stPqc0ybTjns_6q54s7YrgItjbnyu5m_j0Yy5gtNEnPuEuVUNu0_28z9saVDdcvlSzdsYRnHJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13dc475bc0.mp4?token=VSCk_KMMWrlsNKHyib_0P7areIxQyTkFVnpgoDCS3s8ot72Nlgp1_C3UNs95Xs4UtT7OTxbfF4YvE1fu159G1MbLzwLB3wztdS5kWpkd0otMfS_I7f_hdQ9jM7h9kHL472iGattmIoOK4Ir133CZ8y_9UmjpXfcUMFpESv-QnYLeRVcfJhBWWOu75LMGwlIbzv4PcZUARqzpWyebCRyAjHRfRF133sf_P85_Y92LLsrHufC5LKGd_OsxVJiojAFgTmEb-d78hQw8stPqc0ybTjns_6q54s7YrgItjbnyu5m_j0Yy5gtNEnPuEuVUNu0_28z9saVDdcvlSzdsYRnHJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین رباتی که رباط صلیبی پاره کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/685628" target="_blank">📅 20:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685627">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0P6ckGp-PfQiyUsKHzB6p-ArhpY3BgnuBk8b-DHabLGaHMVuRcgZ6qj1EURgzBkm5-ZQ_cxrGlOyRPfeRWiV26NGvZwPT5k4-41Ff13otfbLu44aMnH8qCFVTnV-A6wtTPn1qJQoF83tdNaMvJWml3CzIZp8IPgS7HAc4ct7OLFP5ljvQHhx78Le5pqBzE09hYlxEp_gejy2wuYbVLdSGM4RuUaDl6T29E15HflZb0-y_RFoCb605FGgKssWTM9LuZDYszIJRNumZUp1vjKptwT3X3dWtKJKr8qazG3QuVrtOa59yClsBHoANIpT3gSXx9tQ1eiGE3zO1aDCaD7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ راهکار کلیدی برای حل مشکل ناترازی بنزین
🔹
حل مسئله ناترازی بنزین در کشور نیازمند اقدامات هم‌زمان در بخش‌های زیرساختی، پالایشی و الگوی مصرف است.
🔹
از مهم‌ترین راهکارهای کلیدی می‌توان به توزیع عادلانه یارانه، افزایش ظرفیت پالایشگاهی و مهار قاچاق سوخت اشاره کرد.
🔹
کاهش مصرف خودروها، مشارکت بخش خصوصی و اصلاح کل زنجیره تولید تا مصرف از دیگر راهکارهای این حوزه هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/685627" target="_blank">📅 20:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685624">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHyoXkqWdKLlzJSD5vJ1E8ImafVegPW2WWgDdCPOzOOtALZm2XloG4Kn0Fx_q4CH-pov5Jqz2rLgCQa-1p_EaKcQilSmBMHz5oG_tCWFe2cicIe6so7HPJHa8z1rMCTnEQBSnxQHHDvbTxb5dYQVCZAd2Z-qx3ycNRowrUly_kvSCnbixpHHVBwONnK1marrkHe4zfZQRVWsYX_pmcLbVbB8Zm80MZWWJvRZBtTIYzskNR55TJE4bSoWuXzpvSYypIdaD4Cx_d1txuc1e5h8jPx0JO6hHGHNyNmx5VbcwYIxV5uZWn2UQWl91V6KpqrCM8uox6C0kWfMAZz7hL5gPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تانکر ترکرز: میانگین روزانه صادرات نفت خام از طریق تنگه هرمز طی هفت روز گذشته ۳.۸ میلیون بشکه در روز بوده است
🔹
در دوره اجرای تفاهم‌نامه (MoU) که عملاً تنها ۲۵ روز دوام داشت، این رقم ۹.۸ میلیون بشکه در روز بود.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/685624" target="_blank">📅 20:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685623">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
یک توقف کوتاه در یاسوکند؛ استاندار پای درد و دل یک مادر نشست
🔹
استاندار کردستان پای درد دل مادر سالمند ترک‌زبان نشست.
🔹
در جریان سفر آرش زره‌تن لهونی، استاندار کردستان، به شهر حسن‌آباد یاسوکند بیجار، وی هنگام مواجهه با یک مادر سالمند ترک‌زبان، از خودرو پیاده شد و پای صحبت‌های او نشست. این مادر برای بیان مشکل و خواسته خود به استاندار مراجعه کرده بود.
🔹
لهونی نیز پس از شنیدن صحبت‌های او، از همراهانش خواست موضوع را پیگیری و برای حل مشکل این شهروند اقدام کنند.
🔹
مسئولیت یعنی شنیدن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/685623" target="_blank">📅 20:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685622">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هزینه بسته‌بندی کالا ۲۰۰ درصد افزایش یافت
بابک عابدین، رئیس اتحادیه چاپخانه‌داران و صحاف تهران در
#گفتگو
با خبرفوری:
🔹
حدود ۸۰ درصد هزینه بسته‌بندی کالا مربوط به بسترهای چاپی مانند کاغذ، مقوا و فیلم‌های انعطاف‌پذیر است و افزایش قیمت این مواد باعث شده هزینه بسته‌بندی حدود ۲۰۰ درصد بالا برود که در نهایت این افزایش قیمت مستقیماً به قیمت کالاهای داخلی و صادراتی منتقل می‌شود.
🔹
قیمت مقوا، یکی از پرمصرف‌ترین اقلام صنعت بسته‌بندی، از کیلویی ۷۰ هزار تومان در مهر سال گذشته و ۱۸۰ هزار تومان در بهمن، به ۳۶۰ هزار تومان رسیده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/685622" target="_blank">📅 20:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685621">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
معاون سیاسی سپاه: کسانی که جنگ را نتیجه غنی‌سازی می‌دانند، تاریخ را درست نخوانده‌اند؛ ریشه اصلی اختلاف آمریکا با ما «ایران مستقل و قدرتمند» است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/685621" target="_blank">📅 20:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aVTBhhQGClf4BRKMJ5UI6PMJNFxRhFpASwWE_IARcrMZPLdOGvz46984ttg-mlKjTtPB2B-2r8NyL2U7QbmdzhCfJmf_QVuKW0qvwUKGJDkl8VBLgW9JQaUyh83Ho5R6kIOp94-2250K9CdH6DdPxHYQrvCGW_6qVw2lCMhAeGvazJUVfFCcnrDks6MvwF6C_y4RuoQyPPFmC0sb6fBn3oZz2J8wGuMVVwg11qHfRFRXauxFG5P5tmGZSWNcXcq2N5hX6L_FN9Ca7LEeg2odUWUnW91bfjrgsG_qt5Y18kT9iWGgh77ckU66N_X70MTa_wgrX42IauvFx4c7mcqUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbzCPiVCUYl2A-0V4Ql0-SVKGvEFoMqVlt938UZofwzO5DYkFPTHwyW6TzVq4Z-C6SX3NJYjjhpynh3GyppMyK3-scNgnNDIWJ_6l-Tw3NULU5S2XOixJzxexbD8vO9iCtxcfqpjytmVh4KLAcLDb0Kr366H5SIpaRRHyV_hG0PJ6AtZUyniNkEhW488hToKqWX8BtRbTpOR_0m2jqW02kUDOc56j_yuuCeBqbBRHIsfrJuB6fH2olGPVg1ZA4FD56YMOL2RKmy1Yj2QPygfjPBgD2gQD2WcAUgkQZct3_cxwfH2-H68sN6J68Q1ZaURWLh0hb41Su8aMRIBcq0WuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArPVtHyQ5nM_Oq9NdjTQ5GPZTLVG-wXQnicKS_CJTh14XB7bBc70lD19NUzmxekABV2s9Zl9KV5ZO8xr0oI6hNQJp31h_gy0Iekiq_hr3OxE_QXXZWZrQHw9ZOhK47lmfoH7PGXvaO8J3pu8hpLQUWTHqvyL4pGjhHoXryaIWR9Hojyzfh0wwnJqFDpgG1afJt1VlfYJ_7vUzRU9eJUcEhjjmKukuNEKcrS67Ty2Je4l1TUCYoU4VJf0_YXRTpCW6GfcRsZUd8ZkADrxB8X0KChfJvHwWw3u_a9O0XiiLaGRZdQJM0n2yF_qiW4WGcUo_yOtCJ2hBZfhorvS2bglww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdUe1ZYumKqjWMscCCfBu5cSC0-1nir5tBz64jx-D3kUojUp2V1NIB16HcxqD5Anji8cMIzFKCa_8rDCj6v0f3SAy6oSrcbdMiULx_WcLE6v3t_0E7tcFo-V_FKpBBcuhAjPF6cqiFSg2W7v4261SxJzw97dYcQKOWQ30EbJ2xISh5ZMSRwO3fjQYEadwsmARUIlyKZxI4p7mzgAVUzdNBiQlne0XxHd4KHF3C-_lje89_CDm-f1Y_9-ef-kfqPwJrGZo1rGjq3Tj1mJOeiCEQkHZPC-OOoVLOjiBY0dBDwWKuZt0k7vpsdTQ9tBD8X9ATTCgKl5d93XUwzSZHEXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dA_5i5e5wWFbu0w_RcYQc20JUcvbr4C3N-h6doSFHq07tRM-9Dpqo7WrJ_01qY6l07tTjUmwcrtDjwmTrMv5py7N1PhLVf5mTYd_y73vbwWLbyq72IIo5qUulfTtCAxQhAdDKImGpfoxAhVGHh7uQzbpEPNgUMzW2pVxz6lm7VRt0sKwfAdPWMAeWHQaIClLs14KAwFXLZ0lQRygOGPSvz2FXdRST4RDxyGqzBJkgS9L27eyy5pQDU0L1f-kDY9vJ1tYfvdLeCpDf5Xds7XA4fHvPWn2rxJjxmOlPjrzuYSyW71bjzA8oQT_XDPrn_u5cpXW91FTbpM_QBm8qWzvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8AUYG2Y2430a-8PcKFjtyGHTsYRsWMGkwPGv8PzdOzvDSz0e47xTCyWDQNnDqISZXUAetzcBFqpV5OoWGbtOXSSTwmNnAgb6TquSqwA9fb9i1A3SETzGFwp1FDviF6m6X_lEoN3Lnq_7XhNxG_Pz45qfeDURRZLXk2DMl97iQDrKK-W6aJB4Is2Qzul4kDQOIGSa0WGkMriojX2kKLgXnv_8RiPy9pENwvZRmZY2hDG2l7ddlCp_nJWs_DiDYDS_QBS_wSWiQOL7JgyAiJl69jKrTogbiU43UTqi3Y4uB2q770W42ThZvIvUqK2caumj1QyB53-aptRCKIkuY37hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pihTzxM_JkWQfDWxIuL-7hsFYGbbu_CfXPK-5_9TPUj3lCfri-3d7Z2EJ69aYVoHxzZZdw-yFkQqr8w3H-F431JVXs7UmZ-ZqShaTU0sAN-QWB5haMWxGppwQgKJ8GSVVdLFLH7dQXKiyNKd0kc2tkbd-_Eb5hsVszjwO2wh1zj3h7F_50IIDCI6Y5GH7zxJx3ntfx2naS9QZplLRyA-MIIbZpyzmlzdk1V0rUVPSwzroG8Oufx71Dz-xTqOp8YAki0iujzlb1x8GmcTLv6g-6KCAMNICS0IDC_OQc3un_EzwTTrVFTzuoMXKHuvHZB8eVzFa6d4C1OLBFg97cI--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpLs7pM3Qhwtu8Nss0Bl_cOar12avjEkG0Sy6f99eW4MvR8JGxhtewbMcK8qRmMX3kyjHX2QmZIe26wK-QscJoYE13I04VwH7FvEJAj_xWwfOOI2Ve20e39d5vReMcoZn5Cpr-Ly_7ATJW8UFKKHMaZ1lDVXujG8pG9iETW0iQSRjMTCzyhlTrlN1lnPFsM6CIEruf9swTG9o6pM9hR-zrd668aFlx1X7YIqzcRvvJLJ6-mnJxu0gSRjyapt1JRCnmu37Mp93xSRDLZiLO3gI4Q2r69Gg285I_aIpViRvmarGZ4o2I6JfQDpEOhD6Vpbyp3GQpR0ooBokb-YReqJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBZfhHEP-_nRWnkGHgVeTN01I2htTwrjEa5BywwjNMXb7VkzhNSBTBZoPkwYslNLH15lclQpbbZRZWp36WnX3D5gK49qePQ0gUr77-s1iv9wRoXSI6VTDchDdiGtxAlS_fyux6vcR0syhTTDU8IGxFVApzW-4juwGSNhoRE0Wk-gCA8NA7kRkMTEk6OFkfp3W3sxuzTu2PxFvTM842FrRQruXpPl7xv-dNpx4kqi6fHFY_mS5XCNk3ITPauy2D3Ei6n_Z4fF3OSxOMAc_nGivHYsglQlNJ98EbrpJmlWpNppS2l4VDn0F-BJ6nH5bweBLxLlIBQ4RfCMbbzQMl_ZNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
✨
هیچ قدم خیری کوچک نیست؛ وقتی مقصدش، گره‌گشایی از زندگی دیگری باشد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های کم‌برخوردار، قدمی برای همراهی بیشتر برمی‌دارد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_ghararr
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/685611" target="_blank">📅 20:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">08 Ane Manaee (1403-09-08) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/685610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هشتم
حجت‌الاسلام امینی‌خواه:
🔹
از بود و نبود تا باید و نباید: مرز باریک تکوین و تشریع [3:18]
🔹
تشریع، راهنمای کاربری عالَم تکوین [10:18]
🔹
نقشه هستی و راهنمای عمل: خالقِ تکوین همان قانونگذارِ تشریع است [12:33]
🔹
ابلیس را راندند به خاطر تو، اما تو با او هم‌نشین شدی؟! [17:35]
🔹
صدای حق در جدال تاریخ؛ صاحب "سلونی قبل ان تفقدونی" در برابر نادان‌های سقیفه [23:58]
🔹
صف‌های طولانی برای حجاب در هلند؛ صف‌های کوتاه برای فهم در اینجا! [34:52]
🔹
وقتی خداوند آب را مامور می‌کند: داستان مادر حضرت موسی (علیه‌السلام) و گذاشتن ایشان در سبد [48:01]
🔹
کائنات، گوش به فرمانِ بنده‌ خدا [53:51]
🔹
صبر و تقوا در برابر گرفتاری‌ها: وعده پاداش از سوی خداوند [1:08:27]
🔹
حضرت زهرا (سلام‌الله‌علیها)؛ تنها دختر پیامبر (صل‌الله‌علیه‌وآله) و این همه سختی و مصیبت؟! [1:17:06]
🔹
شب اول زندگی مشترک حضرت زهرا و امیرالمؤمنین (علیهماالسلام): بشارت و روضه‌خوانی جبرئیل بر امام حسین (علیه‌السلام) [1:24:00]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/685610" target="_blank">📅 20:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mifAZ4WhZh_vjgAgu2N29MLs9fCFDmDQRQssDmuC5XdPOvs7wcWkJB8vb7zfxkt3z8YmNAOWDu6PI_NdxddEDcbX1D0xyTjWfyljxAFePGc0FPjKmVyHUsuqYZtA8bZI3YB36nqyMc3Y2J67WjoI4koJPqE_BJUyDoq0QV_2TLsHudDvNpq6t2Hl2q808yLOkhFU8_7gq_0-mTbqDPKO0Tr5BTUrCVXwGvpLs5q-uuuLHLXak7yUcKVlCTZVPIqOZ9iVpOoVG_NdGYpD0Fnuk5XyQ-j8stZCBY2-upA4NMI5LE1_BsSFj01TYz18slSHh6648uBRNqBfcjAAfS_sJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف قرار گرفته شدن یک نفتکش در تنگه هرمز
🔹
سازمان عملیات دریایی انگلیس خبر داد که روز گذشته یک نفتکش در فاصله ۱۲  مایل دریایی شمال شهر خصب در کشور عمان مورد اصابت یک پرتابه قرار گرفت.
🔹
این نفتکش هنگام تردد از تنگه هرمز به سوی خلیج فارس مورد هدف پرتابه ناشناس قرار گرفته و دچار آسیب شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/685609" target="_blank">📅 20:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiMfs6K5ORM7cQYutVGAFNeqdHqDoM5YGzTyLyjGGBiToeHyKlQ9_6IsoONz4St4FCMWrPbJ7ox4HYLqDb_Wtoqor9Pdo5EXd6WMA0M1iYBBhYEPXklWjiWmwAE5KAUgEBLL6MKrueldNSwgF2ByDICSBncLWhxo0i-IHe8P4Y5XJxL37xE78K3SkgSHSwexkG89H6joZssSUDfFQJXUTZiGfwdcMBmstAV-dafZCplC8G3IeUzb09MNrKVBTGObK9JgbLCFordoBr0kpXWE0YnLa3J8LQPJCziImjoy8bM5sXUyheplMeTHljApNSHxXRDZx7DCixpYnJWVZPEDoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایگاه اینترنتی «میلیتاری تایمز»: میزان خسارتی که به پایگاه آمریکا در بحرین وارد شده، باورنکردنی است
🔹
ارزش خسارات واردشده به پایگاه آمریکا در بحرین حدود ۴۰۰ میلیون دلار برآورد می‌شود.
🔹
از جمله تأسیساتی که در حملات ایران به‌شدت آسیب دیده‌ است، مقر ناوگان پنجم آمریکا، پادگان‌های نظامی، چندین انبار، برج‌های ارتباطی و یک ایستگاه تأمین آب آشامیدنی هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/685608" target="_blank">📅 20:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685606">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتصویر بامداد</strong></div>
<div class="tg-text">🔹
تی
زر قسمت دوم مناظره «تصویر بامداد»
📣
خاکسترِ جنگ؛ ریشه‌های داغ جنگ‌های تحمیلی
👇
جنگ‌های تحمیلی علیه ایران از کجا آغاز شدند؟ چه زمینه‌ها و عواملی در شکل‌گیری آن‌ها نقش داشتند و قدرت‌های خارجی چه نقشی در این جنگ‌ها ایفا کردند؟
📽
در قسمت دوم «مناظره» تصویر بامداد،
دکتر ابراهیم متقی
و
دکتر مهدی ذاکریان
درباره ریشه‌های جنگ‌های تحمیلی، سیاست خارجی و نقش بازیگران منطقه‌ای و بین‌المللی گفت‌وگو می‌کنند.
🖼
این اپیزود را کامل ببینید:
📹
یوتیوب
🎧
کست‌باکس
💻
آپارات
☀️
@bamdad_org</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/685606" target="_blank">📅 20:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685604">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWDBB2wQdudcOXyS7n9jHIRMQcwDyH2cmjwjwe-bnzp0oEMarMKtFeONhy5quYnr3cBmqZobcuRPcY-uGNjDpp3AuQ5t6-QkzCF7wr8fh5uNWbiXYlgU7Lq3m3uwNzx6cYJuqg7wzgFYiC5WJGDpVhZAl2MYjhLKI8g82vButcAbsPKNidMFxoGQ8DKfCGIY1-M91JFRVcErQNRs2BSlo9JBc2GJxLpK93iGeMB2IkYRy9UsvL1baMQVUcZsoRsvfUi3VZ3vTRaFjHF_zty0dlGdkOw6RJAyMg8Za8fc7TjB1tjhdYq8CXA8vUPRTrwBsnyL5o3OH7UjqpY_Z1_xxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پولیتیکو: جنگ ایران قدرت آمریکا را کم و پنتاگون را تحت فشار قرار داد
پولیتیکو:
🔹
جنگ ایران توانایی پنتاگون برای نمایش و اعمال قدرت نظامی آمریکا در سایر مناطق جهان را تضعیف کرده است.
🔹
به گفته پنج مقام پیشین وزارت دفاع آمریکا و یک منبع مطلع از برنامه‌ریزی‌های پنتاگون، کاهش چشمگیر حضور نظامی آمریکا در اقیانوس آرام و اروپا همزمان با رویکرد آشتی‌جویانه دونالد ترامپ در قبال رقبای سنتی واشنگتن، از جمله روسیه و کره شمالی، نگرانی‌ها درباره کاهش نفوذ و قدرت بازدارندگی آمریکا در جهان را افزایش داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/685604" target="_blank">📅 19:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685603">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
لحظه شکار مزدوران سعودی توسط ارتش یمن
🔹
نیروهای مسلح یمن ویدئویی از حملات دقیق پهپادی علیه مزدوران سعودی در مناطق مختلف یمن منتشر کردند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/685603" target="_blank">📅 19:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685601">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مسیرهای مخفی عبور نفت برای دور زدن تنگه هرمز
🔹
برخی‌ها مدعی‌اند که می‌توان تنگه هرمز را دور زد، اما این امر چقدر امکانپذیر است؟ از چه مسیرهایی می‌توان این‌کار را انجام داد؟
🔹
چرا نمی‌توان از تنگه هرمز چشم‌پوشی کرد و قدرتی برای ایران محسوب می‌شود؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/685601" target="_blank">📅 19:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685600">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953533f9d8.mp4?token=joTPpayP1DMZX7fp4IuXMXHi-7XhWdVJ7LSwomjkiyEtMGmt1SXEHiTi7rQHN6bx8jtOLlZu1swwiA2qTLjdBLROMUsDF4GEx4BRBsS5qftPlCb_bRk5u3RRhdFMIfhc-x4q0jinFebsbz-STZtoVfe18YbZTs7w2w0esqb1RYs0SJqJOtgnhzlAlgq85TS9daUfLWNptH_Jh-tQIDoRK2RSlZhy6H3tXBdVLb-H-8XypKIRRZkjDGgdz8MQVOR9U6u6_iuwS2W9s-AukpksuvEQvuLGwIJT-bzynzcqyqk0U17-30k3H__Deu9KrHHxrMNSVqIVxIQk-HYBc1vUWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953533f9d8.mp4?token=joTPpayP1DMZX7fp4IuXMXHi-7XhWdVJ7LSwomjkiyEtMGmt1SXEHiTi7rQHN6bx8jtOLlZu1swwiA2qTLjdBLROMUsDF4GEx4BRBsS5qftPlCb_bRk5u3RRhdFMIfhc-x4q0jinFebsbz-STZtoVfe18YbZTs7w2w0esqb1RYs0SJqJOtgnhzlAlgq85TS9daUfLWNptH_Jh-tQIDoRK2RSlZhy6H3tXBdVLb-H-8XypKIRRZkjDGgdz8MQVOR9U6u6_iuwS2W9s-AukpksuvEQvuLGwIJT-bzynzcqyqk0U17-30k3H__Deu9KrHHxrMNSVqIVxIQk-HYBc1vUWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان در مرز پرویزخان
🔹
وزش باد شدید در محدوده مرز پرویزخان بدون هیچ‌گونه خسارت جانی یا مالی به پایان رسید و روند فعالیت‌های پایانه مرزی طبق روال عادی ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/685600" target="_blank">📅 19:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685599">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما، مهم‌ترین عامل کاهش تعداد افراد بیمه‌شده چیست؟</h4>
<ul>
<li>✓ افزایش پیری جمعیت</li>
<li>✓ عدم پوشش بیمه‌ برای مشاغل آنلاین و دورکاری</li>
<li>✓ عدم تمایل نسل جدیدبه بیمه</li>
<li>✓ ناکارمدی بودن بیمه</li>
<li>✓ گسترش مشاغل غیررسمی</li>
<li>✓ عدم ثبت بیمه توسط کارفرمایان</li>
<li>✓ بازنشستگی پیش از موعد</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/685599" target="_blank">📅 19:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685596">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOrNrMpqAdabOckshfmV0u9APtVUu2Q92cd1f7RvSpP4_K3FsCWX6LLcD8Hn4fyyv4-CDg5iRgYnJZU3eH1i3XFLHy7U66_OlTE8MaI558nMlxS_MRGwxG2bHhImifv6QTQJRgSg3IB2RrsOCNxBLHG_rVwefssFR3yWY545_rOf7q4IjZByugmVI24o7eM-bEEUsQ37i4CYjGh2KJdqZQTsldwDBmV4LNBhCbIjiPuFsVB9l2zD7Qg5lhPLVtVQBL3mPGM0gqMtVYP8ORi8KH80b4grd9Svmlx-TMWIWO2WBjytPlqOEzL58-YiDi_FnQfv8Tu4ecjAj2J7BoQI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
🔻
مشاوره رایگان پزشکی برای متقاضیان کاهش وزن با آمپول‌های لاغری
🔹
با توجه به سیر صعودی مصرف خودسرانه آمپول های لاغری و با همکاری شرکت های دانش بنیان دوراپزشکی ، این امکان فراهم شده تا افرادی که قصد استفاده از آمپول های لاغری را دارند به صورت کاملا رایگان و آنلاین توسط پزشک ویزیت شوند.
🔸
کاربران در این سامانه با تکمیل فرم کوتاه ارزیابی، شرایط خود را از نظر BMI، سوابق بیماری و داروهای مصرفی بررسی کرده و سپس با مشاوره رایگان توسط پزشک از شرایط مصرف آمپول های لاغری با خبر می شوند.
👈
شروع ارزیابی
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/685596" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685595">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWBqTBkoKJujfntSjpJriwSkoQAea52w6iCUx4EU5HuXRLpKxx3vlgGaUzM6RtTtOJurLJ_0UCOlXrARYIzoLgc7SDCVrKvVkU4YX4WPBC9ub1LGmLUd9biN2nlA1FY3Bbtj6ZG2h0XBZZrqZ-kZvTTanGaY1dP4jW7T5ZHA0sGSgj0Gbj4Fa9zW5jVGXmh5yxBzU179IbIQaQ29F2AQq7-KvUJg6QwpNrGotVJfR-ANGcrg7dVEaQDC9yfDm1gOeRBVvFo6xZ6Rs49mRNDbwKlPRwualmlj_bWeS9e6n2TbSqZ-vnju07cy3AGC076sCX1bp6myxwppd71PlfKsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📛
کانون ایران نوین در الکامپ ۲۹ از آینده صنعت بازاریابی و برند ایران رونمایی می‌کند
🔹
کانون ایران نوین در آستانه ۳۶ سالگی و  پس از یک سال و نیم تحقیق، توسعه و آزمون در محیط‌های واقعی از پلتفرمی رونمایی می‌کند که می‌تواند مسیر ورود هوش مصنوعی به صنعت بازاریابی و برند ایران را وارد مرحله ای تازه کند.
🔹
این محصول، حاصل یک سال و نیم توسعه مستمر است و سیستمی هوشمند که تلاش می‌کند دانش، هویت، استانداردها و فرآیندهای اختصاصی هر برند را با ظرفیت‌های هوش مصنوعی پیوند دهد و آن را از یک ابزار عمومی، به بخشی از زیرساخت بازاریابی سازمان تبدیل کند.
🔹
این سیستم پیش از رونمایی عمومی، در بیش از ۲۰ شرکت و هلدینگ و همچنین با ۱۰ برند فعال در بازار امارات مورد استفاده و ارزیابی قرار گرفته است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/685595" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685594">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
۳ میلیون سالمند هیچ پوشش حمایتی ندارند
🔹
آمارهای رسمی نشان می‌دهد از مجموع ۹ میلیون و ۸۸۱ هزار نفر جمعیت سالمندان کشور، نزدیک به ۳ میلیون نفر (معادل ۳۰ درصد) هیچ گونه پوشش بیمه‌ای یا حمایتی ندارند.
🔹
بر اساس داده‌های منتشر شده، سازمان تأمین اجتماعی با ۲ میلیون و ۹۱۵ هزار نفر، صندوق بازنشستگی کشوری با یک میلیون و ۱۸۰ هزار نفر، صندوق بیمه کشاورزان با ۱۹۴ هزار نفر، و سازمان‌های بهزیستی و کمیته امداد با ۲ میلیون و ۶۰۵ هزار نفر، در مجموع ۶۹.۷ درصد از سالمندان را تحت پوشش دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/685594" target="_blank">📅 19:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685593">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXpdhjxAxVZlZFHOgH9OLDYS9JlvPoKp6aSsRK9Ed-uT3iywyrjEm4JEAKaQHnoboBrVceAt3ph359A9MygRTg1AzitbOY77wiBkJsNtIzYNueR6YqD2OrJ7kgA6BJBst0hBhj5_xoYo9_l1DNkjBUgbdIFR4MMSffLAO0uyoh6DfbVfqiu8P3m0t4aOHtA0ZylGD-lLrxSvWmUwFRAgRwivsqV01A65iCmva5kSCXODyBo9GcV7HepSvHKytSfezstzqzDiiVkNAguMREH1IgwUx0COxX8JTSsqAIHzDx4nX8iKNzrNNWL4zzV9zq3IF6iZpc57iI7FIiZh49zOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات جدید از پهپاد «رجوم» نیروهای مسلح یمن
🔹
پهپاد «رجوم» یک سامانه پهپادی ساخت داخل است که یکی از تجهیزات کلیدی در زرادخانه نیروهای مسلح یمن محسوب می‌شود.
🔹
رسانه جنگی یمن به‌زودی جزئیات دقیق فنی این پهپاد را منتشر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/685593" target="_blank">📅 19:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685591">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
واشنگتن‌پست: فرماندهان نظامی به هگست هشدار دادند که جنگ ایران را طولانی‌تر نکنید
واشنگتن‌پست:
🔹
چندین مقام ارشد نظامی آمریکا به پیت هگست، وزیر دفاع، درباره جنگ ایران هشدار داده‌اند. آنها گفتند که ادامه عملیات گسترده علیه ایران قابل تداوم نیست و خطر تضعیف توانایی ارتش آمریکا برای مقابله با تهدیدها در سایر مناطق، از جمله در داخل خاک آمریکا، را به همراه دارد.
🔹
این موضوع بر اساس اظهارات افرادی است که از یک ارزیابی اخیر تهیه‌شده برای رئیس پنتاگون اطلاع دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/685591" target="_blank">📅 19:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU2Q4WzgdmQBRz1Kg0KOcp5GE6wV65ziKTobi8nEmGJhmyQFSJ4dzUz44Jw7QMIpXQ1NbTRBC9MLThpghEuBNUxVvqo80EpvU-v-c_GL9N5_KNDkI2scKpZm9sfUQpOLpaJj_ZK9Eyza9pVghlSURFtNu7D5CYRpyrykQ5xC_KcKvvqSoLu-q8z5cSyD6sfq2xdfl3unWvPkyP0_ISdsiemRrPVG8jyNqmX0FNgQTe0HOnVpJWjM8cl9l1KnJloHxUfEXioEbdhu9awEQD1CHVz5LnT5dnWEXtWJbhVXd-POUAIC5eMyXvLYQX-9rFh-869qkDojplzgZc1wK4Qcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: همزمان با تلاش ترامپ برای انتقام از ناتو بابت عدم حمایتش از جنگ ایران، آمریکا ممکن است درباره ادعای انگلیس بر جزایر فالکلند «بازنگری» کند
🔹
ترامپ بارها به کی‌یر استارمر توهین کرده و او را به‌دلیل عدم تمایل به پیوستن به جنگ، «بزدل» خوانده است.…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/685589" target="_blank">📅 18:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAzoh0-2jlwoDemBMs9I6RleqbuXIE8H8yWmGa8KKoC92nrMxV8t9nyL2S-0OT3gge0kop0iwgH559ncTk_wK1l6zHXeaoy3a3D8jHNkBiDnV3xZgoYLmAWqKzD8muoTEdNpBhes1GTlL33QMcGEf7D0dFEfTgiYR1GuWD7caD5jp8ky4FInr7vIVMIjKYvjUUcLERmEkGnoVJ9vZzQ6V4jULPnutOZUTOzCgSjyPlGp7JyOxazr_ujMI5OQ-i_I8ba3hRs6NVq93P08tFhc9INGmx0nPRIln3VU1AXsIEcp7La6SBBI4_ohuXYk5b2YH1JQuqst_1ypRY0HVSecwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین تورم سالانه مربوط به کدام خوراکی ها بوده است؟/ تیتر تجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/685588" target="_blank">📅 18:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
کوچک‌ترها در بورس ترکاندند!
🔹
رالی پساجنگ بورس تهران فقط به کام غول‌های بازار نبوده، سهام کوچک و متوسط حتی از شاخص‌سازها هم جلو زده‌اند.
🔹
از زمان بازگشایی بازار پس از جنگ، شاخص کل ۷۱.۸ درصد رشد کرده، اما شاخص هم‌وزن با بازدهی ۸۸.۷ درصدی حدود ۱۷ واحد درصد پیشتاز بوده است.
🔹
این اختلاف نشان می‌دهد موج صعودی به بخش گسترده‌ای از بازار سرایت کرده و برخلاف رالی‌های متکی بر چند نماد بزرگ، این بار کوچک‌ترها در صف برندگان اصلی بورس ایستاده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/685587" target="_blank">📅 18:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJBGruagVohRaV0JIdesmOoPo0kxcVmGEL_QwBHyqrB9cGUdaI81IL1Hn7uAiolTSoOL333WMNlQQIduYdseeKSVBbm85rMB2T_-atFCAkRp9fRflG5X-nevzgAjHUsWEHWAlHEDAFrH8mC9n2DdQiUXAvdAhR7miUYByP5mVJ27RFloeslz_IhXcaNVMuXL7yaF3cgBEWTwgd_yfpwDBgfd-3-P-mL2lkLACkk5X_GVYYk0PbGpHEix4pykoHnbESiovMN5F871KKiGBl1Dm9AsVLUBd3I5H9rvuwYg8FQrQImdrDewLM45ps9O9RcuYA0HfdCGlrQYAjUwjXyl3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری این‌بار از نزدیک با شماست
✨
🔹
بیست‌ونهمین نمایشگاه بین‌المللی الکامپ، فرصتی برای دیدار، گفت‌وگو و همراهی با تازه‌ترین جریان‌های فناوری و تجارت الکترونیک.
🔹
در غرفه خبرفوری منتظر حضورتان هستیم...
سالن ۶، غرفه ۳۲
۹ تا ۱۲ شهریور
ساعت ۸ تا ۱۵
نمایشگاه بین‌المللی تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/685586" target="_blank">📅 18:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685582">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اتحادیه مرغداران: تخم‌مرغ الان ۷۰ هزار تومان ارزان‌تر فروخته می‌شود
حمیدرضا کاشانی، رئیس اتحادیه مرغداران میهن در
#گفتگو
با خبرفوری:
🔹
قیمت تمام‌شده پیشنهادی اتحادیه برای تخم‌مرغ ۲۶۸ هزار تومان به ازای هر کیلو درب مرغداری است اما در یک ماه گذشته میانگین قیمت فروش تخم‌مرغ توسط تولیدکنندگان به حدود ۱۹۰ هزار تومان رسیده است.
🔹
تخم‌مرغ اکنون حدود ۷۰ هزار تومان پایین‌تر از قیمت تمام‌شده پیشنهادی تولیدکنندگان در بازار عرضه می‌شود و این موضوع توان اقتصادی مرغداران را کاهش داده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/685582" target="_blank">📅 18:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685581">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
شعری که آقای شهید، دو سال پیش در سالروز میلاد پیامبر اعظم(ص) خواندند...
#رهبر_شهید
میلاد
#پیامبر
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/685581" target="_blank">📅 18:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685580">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290a466da7.mp4?token=R3Xe1zwnttXphEyn1K85bOEzBwPEst_J7OmcFayV1UeSQZUl8vVG4k62xUuTecfyOzhtU8p63hFNBNXuxgDhFly6jlV398pWk23LRc-vJBnoUGFEFuy7VXgLz3CFF8u6-sz49MMBXTeIMGpPlIqo5joBkbIiohesYynfWSdfL2Mw_9l5XJ3k0TC0EbgUZIGYQRxGgbYG7NHEixKDoJfF5hZE84AHBIO98uBNmMwAsUkjAi18JosVpkj0cf2OzAPj420L1RfAfE2ovtA9HpOZdJht1APUynomXVOrEAYmV8PNS0aPVP5STvKT0qUfDTtpEgRZ-xMtvrMJGrefvinKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290a466da7.mp4?token=R3Xe1zwnttXphEyn1K85bOEzBwPEst_J7OmcFayV1UeSQZUl8vVG4k62xUuTecfyOzhtU8p63hFNBNXuxgDhFly6jlV398pWk23LRc-vJBnoUGFEFuy7VXgLz3CFF8u6-sz49MMBXTeIMGpPlIqo5joBkbIiohesYynfWSdfL2Mw_9l5XJ3k0TC0EbgUZIGYQRxGgbYG7NHEixKDoJfF5hZE84AHBIO98uBNmMwAsUkjAi18JosVpkj0cf2OzAPj420L1RfAfE2ovtA9HpOZdJht1APUynomXVOrEAYmV8PNS0aPVP5STvKT0qUfDTtpEgRZ-xMtvrMJGrefvinKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میلیتاری تایمز: خسارت سنگین به پایگاه آمریکا در بحرین
🔹
حملات به پایگاه پشتیبانی دریایی آمریکا در بحرین خسارت گسترده‌ای بر جای گذاشته و توان عملیاتی یکی از مهم‌ترین مراکز نظامی آمریکا در منطقه را به‌شدت کاهش داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/685580" target="_blank">📅 17:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685578">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_VDk4u85w0ShmgMpc2QEdkpF1cgEIS4G9BYK-jI87oMeEGcOt8Pbhhz-D9jh8enjFGVq2ix2S-EdeF8XEQgAWNfOh0TTYWn7OOiah_cIFcLiEctEfluyAC1ggAtbGD0MwZ1wvcFDfZ6o0e2zB8C-x0AZtWmudUbp68v_q7VoeWllWA90lqVpEJPe_gNwfhQW4WH0NPavPAasJXlg3zXEX_-8wMP_I1hFFbRb3Au25xoUXCALs3MhlH6stxr5XxfRyicA57nkBJSnJG6UWrkH0rTp6u-y7T47Dwg2tCE3uZBYqkYxVrUsnh9xPrQrBgR70jzn2xfv5NSCzSRmNkZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لری جانسون تحلیلگر آمریکایی: راننده و محافظان شخصی نیکولاس مادورو در ازای پاداش میلیون دلاری با ایالات متحده آمریکا همکاری کردن اما بعد از پایان عملیات دستگیری مادورو، دونالد ترامپ از دادن پاداش نقدی به آنها خودداری کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/685578" target="_blank">📅 17:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685576">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ترمز پول کشیده شد!
🔹
در عملیات بازار باز هفته گذشته، بانک مرکزی از ۴۲۰ همت تقاضای پول بانک‌ها، تنها ۷۰ همت را پاسخ داد.
🔹
در حالی که ۶۰ همت از توافق‌های بازخرید سررسید شده بود، یعنی عملاً ۱۰ همت خالص پول به بازار تزریق شد.
🔹
این موضوع نشان می‌دهد پاسخ بانک مرکزی فقط به حدود یک‌ششم تقاضای بانک‌ها بوده است.
🔹
اثر این سیاست در کاهش سرعت تورم ماهانه دیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/685576" target="_blank">📅 17:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685575">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx6BoBNJt3LfYGGizqPR8Ly9Em_ck-vNpA0mTnxFOtysbEzaOk7S7gGWsq5OYmYxEpKAkujoxQCc3aAwFaJZZcp_Uy680d7UAUMICsRStbXRfaaVYmvVdhshCGKB4HRR9NvbxpUCpvdieEL99jm8riuxxLagayLtxrz9WI4wvGx8XhvAhvuiv4pv7bODC9GSNPLZE60VTEJ8siObO6mopwTZb9WjKCXltVd6tBEy-_MtOsUftmxpwAzoGh_Yo2zcsEt3_Zmsdss1QjqSGiBF6JzVVBZV1WCyk8QsxrkAnJzTbOFzYpP6RlEiak0ZtseGZGV-z65H9yxFVfHHYdqgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#همراه_اول
صدرنشین پوشش روستایی، جاده‌ای و توسعه 5G
🔹
تازه‌ترین گزارش
#رگولاتوری
در بهار ۱۴۰۵ نشان می‌دهد همراه اول در سه شاخص پوشش روستایی، پوشش جاده‌ای و تعداد سایت‌های
#نسل_پنجم
، بالاتر از سایر اپراتورها قرار گرفته است.
🔹
پوشش ۴۴ هزار و ۹۱۸ روستا
🔹
پوشش ۸۲ هزار و ۸۳۰ کیلومتر جاده
🔹
راه‌اندازی یک‌هزار و ۴۳۲ سایت 5G
🔹
براساس این آمار، همراه اول در این سه شاخص جایگاه نخست را در میان اپراتورهای تلفن همراه کشور به خود اختصاص داده است./ سیتنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/685575" target="_blank">📅 17:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685574">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چرا ترامپ از تهدید نظامی ایران عقب‌نشینی کرد؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/685574" target="_blank">📅 17:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685573">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
لحظه شکار مزدوران سعودی توسط ارتش یمن
🔹
نیروهای مسلح یمن ویدئویی از حملات دقیق پهپادی علیه مزدوران سعودی در مناطق مختلف یمن منتشر کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/685573" target="_blank">📅 17:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685571">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e26c0994.mp4?token=t-D2vN9Tx9Cs0jaAbSAGu0YnkJ7Yk8gnzd72L9FOgRO7bGdh9TxSVNb43TZUIcM8CrIh18GAZSKHSatrT7lZ6LJNSnQdufr73OcgJ2IgbEXkdU-poFFio4bUOP2uni-LFX95fhhaNamrDJo2ZlVqyhUW_5l3YeBXPkYN0R7Q0_c0qs3snIFGX7JhXjsd8XsxVWpAKnLsxQzqAyQ8Ztzpl9w_TAM6zA4iFy9vAHs3GLpKAKgeHl8QS8HQu-rExC9YK9fUf4PXbOCLHZpkP-n9Awc4yhfowfixcd8dOknKJeSoNcnafjRYghOdKRzB9ZdEIGafDT2gaSgAoX82yrL-rIPiUNRB1EcyrHTqGdXhDSxcedMJiDqOoNIWc6caBvzNwsY2Mrf9nkvRF7xf7EemmlqOobGNcExq9E0Pd5l9_duRWV7TJWaAFSpdImcN6B8V7B2Bq2qC8c9qrDN3sISOI-Bfn7b-8Yhw-ZJ033aXkRNDeZvMpaxkcZc6twd4rRQ9zCmSf6UVMhUDiQuP5fsdvVBxcEGCAXhx_P26hs53o8FgHPJkj3FMblf9EEFnEsuGEJ_JrE2UE-Po-3w29GnhXSq7tBoFasSvIKgpPiwnPXYTeE9hbiqcsdHM5PuWZwhmTDUCDEnvXy0baI-Bs7qvS_5LkoUFn_fYPEFAUcAosdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e26c0994.mp4?token=t-D2vN9Tx9Cs0jaAbSAGu0YnkJ7Yk8gnzd72L9FOgRO7bGdh9TxSVNb43TZUIcM8CrIh18GAZSKHSatrT7lZ6LJNSnQdufr73OcgJ2IgbEXkdU-poFFio4bUOP2uni-LFX95fhhaNamrDJo2ZlVqyhUW_5l3YeBXPkYN0R7Q0_c0qs3snIFGX7JhXjsd8XsxVWpAKnLsxQzqAyQ8Ztzpl9w_TAM6zA4iFy9vAHs3GLpKAKgeHl8QS8HQu-rExC9YK9fUf4PXbOCLHZpkP-n9Awc4yhfowfixcd8dOknKJeSoNcnafjRYghOdKRzB9ZdEIGafDT2gaSgAoX82yrL-rIPiUNRB1EcyrHTqGdXhDSxcedMJiDqOoNIWc6caBvzNwsY2Mrf9nkvRF7xf7EemmlqOobGNcExq9E0Pd5l9_duRWV7TJWaAFSpdImcN6B8V7B2Bq2qC8c9qrDN3sISOI-Bfn7b-8Yhw-ZJ033aXkRNDeZvMpaxkcZc6twd4rRQ9zCmSf6UVMhUDiQuP5fsdvVBxcEGCAXhx_P26hs53o8FgHPJkj3FMblf9EEFnEsuGEJ_JrE2UE-Po-3w29GnhXSq7tBoFasSvIKgpPiwnPXYTeE9hbiqcsdHM5PuWZwhmTDUCDEnvXy0baI-Bs7qvS_5LkoUFn_fYPEFAUcAosdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش‌ها به پیام محسن نامجو به همسرش | آیا او به همسرش نگفته بود به ایران می‌رود؟ | نامجو یک هفته پیش از بازگشت ناپدید شده بود!
🔹
بازگشت ناگهانی محسن نامجو، خواننده و آهنگساز سرشناس به ایران پس از نزدیک به دو دهه مهاجرت، به یکی از داغ‌ترین سرخط‌های خبری…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/685571" target="_blank">📅 17:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685570">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR_byhIsZXRpbJZ1bK6sCZ4rLxXMIQWWHWWkmb_AD4jrsA0x3up-rPFIo6A0qRa0hiLVyAlRae3YxlNYNruebSojszmHlZjMHjk1Rgm0Imyl2tWqOpWH6CDo3f5lGmbGRSm-X41QHgnWGzeQ7F748vOvxR8VJOdrscY0yXOooo-20FNmFTCPpyTnqzu3YJfjxieiXkLM6ra_x3JJfQlqsCtObtfiL6lMiEuIENXPJQkfUM6u1zHEzzXALmF7LR_nHAQgtr7X6bN3VvNiEX12egfHu6KaIjyp0-FIhnHjUR7stgbikZbA5r-osdZhlp5gPkbfUbCgLqgYB6e5LFPCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه CBS: ترامپ با خبر آتش‌بس با ایران، نوسان نفتی می‌گرفته است
🔹
حساب‌های سرمایه‌گذاری ترامپ در سه ماههٔ اول سال، حدود ۳۶۰۰ معاملهٔ سهام یا اوراق بهادار به ارزش کل بین ۲۱۲ تا ۶۹۵ میلیون دلار انجام داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/685570" target="_blank">📅 17:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685569">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUqiJy4FO3JqBop6mnNVeR2of58ZJ9beq3DHVl2SqciK2eSsLcIxUGotvxekqK-DmJtEGWeLI4u81zUG_Q_ojNm3EpeuEvDNfjh4_0BldkXB17QwvPpGKvsKwOgxz74FpNE86lPHcjMejI608HtY-njbvcSQgGeH-dMHpDlC2H71MLYFLIECkDfN3smepMp1RfU0XWaYmZ01HXZ3qboB15UY801DpOlzx_qdCdIAfhNL9ingg2CDaQDfn9RH9ErUZbmBwzNhXdAjh14tVNLoNjNrFRzYkUYO32UhDFRakcbztEO39XXn8KWmqE4cFDTkh4c3SLIOZzaHrZ5cstxPdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر اسپانیایی: ترامپ کاملاً دنیا رو بی‌ثبات کرده، دیگه قانون بین‌المللی وجود نداره؛ می‌تونی کلاهبردار مالیاتی، پدوفیل یا جنایتکار جنگی باشی و انتخابات رو ببری، رئیس یه کشور بشی و مثل هیتلر تو زمان خودش برات هورا بکشن. واقعیت وحشتناک جدید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/685569" target="_blank">📅 17:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685568">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEREh-oEH95dh2ccJvZd0wvjXCDgetBZdzskxciRLi1GXTKW9w2e5AEaihg8XUsS3z-fGOgwMRq4GnFA9HK-yUl31Tr4RF2L4zKz7HYslGIV8dhnTtuOtUDwbbhB7OQbXyDTvB0xtsWETXSvHnnKjkJquzHMQ9gbE436-WcmuNTzjdj564EUQE0VkKRN6EBnWWiuOowErQux05XOHrU7BLe70ldNDNQX0DXsGUWm6TYYYWX1a3rUHShcz6t43Tu0ubrHHI609QID1rmqilBknYbit-fE1-pwTfob8hQk-iyNO4ax7wDannylxwr2N3MvWI0btykl6wVMqBQVA2g7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه‌نگار و مفسر سیاسی کانادایی: دونالد ترامپ فکر می‌کند اگر مدام چیزهای احمقانه در رسانه‌های اجتماعی پست کند، ما فراموش خواهیم کرد که او با جفری اپستین به کودکان تجاوز کرده است
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/685568" target="_blank">📅 16:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685567">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227990e230.mp4?token=k9RFrzOTgLaDsY6hKRPJDIj0D79rZ60ivBPhY-yjVqnE8dMceafsGmWmTWWLBEvjzbfEw4cyjaTr-2OUpAOkd4RKU4uH8_L4gaVOOHoe4ZNtqoMaMNIz1kpD-wgTjH-F7JqbGrmRKN3l_G8ixemw2K08fpVYU3o_xpoFrRwK8MH7p72DQkYtDl7F8MP4ycJecqjfDBFDR99gIA7eG2sU4smfTJW_4QLaPvYhb_9i9R1s3WCLe2-7942a03TXCL9K8_lulqBr_Ol8VUdgtGxkCakN_iYD6lPoAWwd2k_PDILaQXZpNZVvbu1YloNuUzcoNnvKaoR7ctYDK405NA5WXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227990e230.mp4?token=k9RFrzOTgLaDsY6hKRPJDIj0D79rZ60ivBPhY-yjVqnE8dMceafsGmWmTWWLBEvjzbfEw4cyjaTr-2OUpAOkd4RKU4uH8_L4gaVOOHoe4ZNtqoMaMNIz1kpD-wgTjH-F7JqbGrmRKN3l_G8ixemw2K08fpVYU3o_xpoFrRwK8MH7p72DQkYtDl7F8MP4ycJecqjfDBFDR99gIA7eG2sU4smfTJW_4QLaPvYhb_9i9R1s3WCLe2-7942a03TXCL9K8_lulqBr_Ol8VUdgtGxkCakN_iYD6lPoAWwd2k_PDILaQXZpNZVvbu1YloNuUzcoNnvKaoR7ctYDK405NA5WXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تذکر مادر لیلی رشیدی به وضعیت نشستنش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/685567" target="_blank">📅 16:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685566">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: سران ایران، چین و روسیه با هم دیدار می‌کنند
خبرگزاری فرانسه:
🔹
پوتین، شی جین‌پینگ و پزشکیان، در یک نشست دو روزه در قرقیزستان با یکدیگر دیدار می‌کنند.
🔹
حدود ۱۲ رئیس دولت به بیشکک، سفر خواهند کرد تا بیست‌وپنجمین سالگرد تأسیس سازمان همکاری شانگهای (SCO) را گرامی بدارند.
🔹
این گروه شامل روسیه، چین، هند، پاکستان، ایران، چهار کشور آسیای مرکزی و بلاروس، متحد مسکو، است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/685566" target="_blank">📅 16:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685565">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd07QA7pTt8rwaU6Xvd73blCEtjEstXDhGHuJH1rZ9EP_LToMMOq-YeNRwiSrA4Xug01gF0i7z8vFoC3o_oR6XVI36L3u1SVqM9VO8Lkj7cg2QjUExS7i6yDmRIGoYBf9lY-YMCL8Hn0PI9fj14H0StDsH_3n7X_MZXPOikLps2Ffz9-f9WZj2FbmCmMddng83tx6ek7nTLnUJq7TS0WX6nDs4hKXos1_LbhFacJHw7ZiasgnUqzK9tuW0XP-nG9a_AjfwcHTiTrKRzHX682jJDjgo1_eHXAj0bHRgsWHD2JxPpXcj6--SJSHHKp_lQSj81yBXiMZ_ISWCYu_12yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای اتهام جنسی به محسن نامجو چه بود؟ | یک فایل صوتی جنجالی و میراث یک اتهام | شاکیان او چه کسانی بودند؟
🔹
شهریور ۱۳۹۹ و در جریان داغ شدن جنبش آزارهای جنسی عموما از سوی جامعه ایرانی به یکباره نام محسن نامجو مطرح شد. اما این پرونده به کجا رسید؟
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3241480</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/685565" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685562">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8L2md2br1gJcxiwIGDQKIfqdWWru_JwT-gbGkkUk6vNMEN92du-skFWv-FH8ttay4YwMeOM1A9fipkSGZIqEFtcZchd7H9tEwjVtluuG3z3CEnYfXQRQOO6NZPfJ3mjodGaNt2BaNEyR--EOJRwe3LFCs6byaSDAe-b6qoxYK6QDxwJqdxMMwKZLP4M2vgtrewpRcDvrhTqNPBRlp6mQxmnKlGacKdRujz7dHRs3iXzgVQVQ0BEalXGNH8I0V15NN211VgxZyN_vnKDtYFlk8jyHlsK46OVEyx5svCIjEL_1joGZRZhxsI0aE8eUO8mKSu0MzdVRcesi51gJUg-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان زمین‌شناسی آمریکا (USGS) امروز رسماً نام «دریاچه انتاریو» را در تمامی اسناد الکترونیکی این سازمان به «دریاچه آمریکا» تغییر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/685562" target="_blank">📅 16:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685557">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سی‌بی‌اس: در آمریکا علیه ترامپ سند رو شد/ او از جنگ با ایران کاسبی کرد!
سی‌بی اس:
🔹
طبق اسناد افشای مالی، تا سه ماهه دوم سال ۲٠۲۶، حساب‌های سرمایه‌گذاری ترامپ در حالی که او بر جنگ آمریکا با ایران نظارت دارد، به خرید و فروش سهام در شرکت‌های نفت و گاز طبیعی ادامه داده‌اند.
🔹
طبق جدیدترین داده‌های موجود از دفتر اخلاق دولتی، ترامپ سهام نفت و گاز به ارزش صدها هزار دلار خرید و فروش کرده است.
🔹
ترامپ سبد سرمایه‌گذاری گسترده‌ای با دارایی‌هایی در هر ۱۱ بخش دارد و تحقیقات سی‌بی‌اس نیوز نشان داد که در سه ماه اول سال، حساب‌های او حدود ۳۶٠٠ معامله سهام یا اوراق بهادار انجام داده‌اند که ارزش کل آن بین ۲۱۲ میلیون دلار تا ۶۹۵ میلیون دلار بوده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/685557" target="_blank">📅 16:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685556">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751875e9d9.mp4?token=H9FNXICA7T0azqsA_A047Nm-AkRSOiedYBkKMC3ahR0DMKHrT-zjGc2uFzgQcIlXuyVxHnPJmwPET6_lSO7A5VwEqsF2LN7-WlFBWq5ZXDWBfMf7BiVf0ps_RF7MODgJ2t6jBLvK1ahP2m-YR7Lyc5ZWEwqX2yp1rMEiVKDfgai027dXQtTokoa0mjcrVm7KaP-ThzEan43ztsycfEKx8uDYLbBrwGH6sZvRaDKVgjGR7wAl11mW-j6Xp74CXEs805Kf5Z5rHw-vfLMpGjlxJl8obwOfuGnoIe5c9cAxU6ECVtbnu5BXIqwOh2sy1zupcaEChgbg3UoLcT0Vpl1VyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751875e9d9.mp4?token=H9FNXICA7T0azqsA_A047Nm-AkRSOiedYBkKMC3ahR0DMKHrT-zjGc2uFzgQcIlXuyVxHnPJmwPET6_lSO7A5VwEqsF2LN7-WlFBWq5ZXDWBfMf7BiVf0ps_RF7MODgJ2t6jBLvK1ahP2m-YR7Lyc5ZWEwqX2yp1rMEiVKDfgai027dXQtTokoa0mjcrVm7KaP-ThzEan43ztsycfEKx8uDYLbBrwGH6sZvRaDKVgjGR7wAl11mW-j6Xp74CXEs805Kf5Z5rHw-vfLMpGjlxJl8obwOfuGnoIe5c9cAxU6ECVtbnu5BXIqwOh2sy1zupcaEChgbg3UoLcT0Vpl1VyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، سرزمینِ ماست؛ و ما، مردمِ این آب و خاکیم؛ ریشه‌دوانده در خاکش، با قلبی که برای نامش می‌تپد.
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/685556" target="_blank">📅 15:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685555">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID0ZTkBbys0rZaPhGYXo8BGy9NcCSLfHosjdK3Vq9QzYzfyLLWXk7cUgK2zqWRZbZ-k2mClRZNZpBTaerjdHZBCgL8hf4Tt_yMnYGO2lM5dqRVsXbRWKfAAjfVmx5iu2ond-sujJ6Qzi4GDrLU3ajzl2Q9QopthBuBGApvPnykLKVFVE-GzfEXwELfssWrG77m32ZBFLHFXNEZxIqmkznzjFs_PYioFxEdWuEDi5h1yrJGEJOF48TRkMeZEuapJGPYh_tILds5kwfoGXCKhIDxQPgECW93KkfI5q5RfBvYhEHlAk5cDJDcj1UiX-X8xfvjcRp72sCdJnvhrAR5-1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستبرد ترامپ به ثروت ملی ونزوئلا؛ غارت ۶۵ میلیارد بشکه نفت
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا، در جدیدترین اقدام خود برای تاراج منابع کشورهای مستقل، مدعی دستیابی به توافقی با ونزوئلا شده است که از آن به عنوان «عظیم‌ترین معامله تاریخ جهان» یاد می‌کند.…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/685555" target="_blank">📅 15:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685553">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دستان پنهان در جیب مغازه‌داران؛ افزایش عجیب سرقت مواد غذایی
🔹
برای فروشنده‌ها، نگرانی فقط فروش و تأمین کالا نیست؛ امنیت مغازه هم به یکی از دغدغه‌های جدی تبدیل شده است.
🔹
سرقت، خسارتی است که گاهی جبران آن برای یک کسب‌وکار کوچک آسان نیست. نگرانی هر روزه صاحبان مغازه‌ها می‌گویند حالا علاوه بر گرانی و کاهش قدرت خرید، باید نگران امنیت فروشگاه خود هم باشند.
🔹
دغدغه‌ای که آرامش کسبه را تحت تأثیر قرار داده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/685553" target="_blank">📅 15:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685549">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
یونیوز: ایران در صورت گسترش جنگ، شمال اسرائیل را هدف قرار می‌دهد
یونیوز:
🔹
تهران هشدار داده در صورت گسترش عملیات اسرائیل در لبنان، فرودگاه‌ها و پادگان‌های شمال اسرائیل هدف حملات موشکی قرار خواهند گرفت و حمایت ایران از مقاومت ادامه خواهد داشت./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/685549" target="_blank">📅 15:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685548">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9acccbce2.mp4?token=na5D4k3I-oL-89-5lfevlx0AgyLhQ-2uhEUQkUMKNAFWL_UYIVFIlqcYkhkn9yJ1jFes7puAVyYetaJi7YB3w3o6q0mfDgjLYdt7B8BpXp2ZCLCx_ANN-cMrvXWD3kNF8d-Y2Wmy4si-suXHleAS_JH8-axOAShdWu98cOfwiDV_PSNpE7_CfTC7Wti-TNy71CtSIVBTVaD8tvPkVRFnCzFEWS4Eg5aTIL9mPLicq8Ledv_CI86N-rw2XioiMW93InbHRk0lda7-4NVhBQkEPABrc34-IS9sKabJPvR-oQt-ooxMO40KtTCJHot_l3p1MEoVXXGdr0hVWjQAGmp_pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9acccbce2.mp4?token=na5D4k3I-oL-89-5lfevlx0AgyLhQ-2uhEUQkUMKNAFWL_UYIVFIlqcYkhkn9yJ1jFes7puAVyYetaJi7YB3w3o6q0mfDgjLYdt7B8BpXp2ZCLCx_ANN-cMrvXWD3kNF8d-Y2Wmy4si-suXHleAS_JH8-axOAShdWu98cOfwiDV_PSNpE7_CfTC7Wti-TNy71CtSIVBTVaD8tvPkVRFnCzFEWS4Eg5aTIL9mPLicq8Ledv_CI86N-rw2XioiMW93InbHRk0lda7-4NVhBQkEPABrc34-IS9sKabJPvR-oQt-ooxMO40KtTCJHot_l3p1MEoVXXGdr0hVWjQAGmp_pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کردستان و هورامانات؛ جلوه‌ای بی‌نظیر از طبیعت و تمدن ایران‌زمین
🌱
😍
#اخبار_کردستان
در فضای مجازی
👇
@Akhbarkordestan</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/685548" target="_blank">📅 14:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685547">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_-THgpEoWs1cyQ_vcwOOkIrxgdBePgmO32FJ1DiUzYrCFw0z6HMt1nMgr2tA1LpAUFYzuAl9BaD_uuMYPBHApl0lxf7tVBdDe3GICe9yiC6ABgCHybnmkYp4XbYSlTZQA7fa3x18sVbdyENTuSG-U-EtuT1v_fPNdrQ0fCo3PgMe9tHGEhGwoLPpPXsDTiQ8BisCFe3hzZnlGHoeG_ks9DaWdAPtfHBzA0nNxvxNk9VnIhT92Lavpiu3WTkpLs_45LtAz7kLyeRoEcr6SgQWf2ZicRSu3PCmZOmsNsGw6tZRRDsFu-X_F34Lj-XWndnnkED2Od7wXgN6OG-9nTGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای ناب ساغر مرادی در مسابقات قهرمانی آزاد زنان جهان
🔹
ساغر مرادی نماینده وزن ۶۷- کیلوگرم کشورمان با یک عملکرد تاریخی پس از پیروزی مقابل رقبایی از روسیه، چین، آمریکا، کرواسی و یونان بدون از دست دادن حتی یک راند در طول مسابقات صاحب نشان زرین طلا شد‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/685547" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685546">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
گرانی کالاها دو برابر خدمات؛ شکاف ۷۲ واحدی اقتصاد را تکان داد
🔹
داده‌های بانک مرکزی از تشدید شکاف تورمی میان کالا و خدمات حکایت دارد.
🔹
بر اساس این آمار، تورم نقطه‌به‌نقطه کالا به ۱۲۱.۵ درصد رسیده، در حالی که تورم نقطه‌به‌نقطه خدمات ۴۹.۳ درصد ثبت شده است؛ یعنی فاصله‌ای ۷۲.۲ واحد درصدی میان دو بخش.
🔹
این واگرایی می‌تواند نشانه‌ای از فشار همزمان تورم سمت عرضه و رکود تقاضا باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/685546" target="_blank">📅 14:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685545">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjwzQd-Gguj2eMy-916T9Vkri0GI0L0lPUUAO8Z5t--7wcgkKmbxO3aVMWXVBF_LRQt2tJ5id83vN9Daog4j6a90H3PfGgUCi9_OnF6cRYHyKAgMqT9_vK2nPlJwEVT7u5Ag9k0HHzJq6yEuVjOtaELA3yoBbUHbGacWupYRaX5ZFqDeTjNa7v2vLAd2i_zxQKR3V_lcSeCoHBCLiJgV_pjvXeCQQpJLJ2oEt_3PIrd7CvHUajWYn5ZJeFV_ufo8wXadDCTZ7HTwbnn_xD4F5vRsJl-TvRozbsoZmiEBx39nahnpyUJHXdoiSTk3xVf1kUiPgz6w-2IQNboa43hbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ از کنترل آمریکا بر ۶۵ میلیارد بشکه نفت ونزوئلا خبر داد
🔸
دونالد ترامپ روز جمعه از توافق جدید نفتی ایالات متحده با «دلسی رودریگز»، رئیس‌جمهور موقت ونزوئلا خبر داد.
🔸
او اعلام کرد که بر اساس این توافق، آمریکا کنترل اکثریت ۶۵ میلیارد بشکه از ذخایر نفتی اثبات‌شده این کشور را در اختیار خواهد داشت.
@amarfact</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/685545" target="_blank">📅 14:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685544">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad1ca53df6.mp4?token=H1Cvfsc7dGgOdpqYJDf-rDnBDp7RHeny2I0V3_r4e3pL1B-fg3WCvBuLenJ73Rvb63M2256TALw8_3tOC7WFh_e4y-02HQePf7tvtHq9o58q_tCYFw1MX5JYQRCY1e6rANsy7xoEnnTgFoNCnKhTBXQOH0_-KZnf9Q8q1eTVjzOeqvNuFXgKX_OOvNOy3fqa9bLbPoyQjomy8cJ1SzWIX2tjbg1Lm8Bty51s_IxmnNK6T6l2_pNyeLvyPyL6-8rdmvx_yY6v3zYdeIUiwvxmLL984kseNUqy76ioCVB1ByE6ecaaS71Jzu-GmmaD4AL3mWen5CGCqk4NoxW8WBHjyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad1ca53df6.mp4?token=H1Cvfsc7dGgOdpqYJDf-rDnBDp7RHeny2I0V3_r4e3pL1B-fg3WCvBuLenJ73Rvb63M2256TALw8_3tOC7WFh_e4y-02HQePf7tvtHq9o58q_tCYFw1MX5JYQRCY1e6rANsy7xoEnnTgFoNCnKhTBXQOH0_-KZnf9Q8q1eTVjzOeqvNuFXgKX_OOvNOy3fqa9bLbPoyQjomy8cJ1SzWIX2tjbg1Lm8Bty51s_IxmnNK6T6l2_pNyeLvyPyL6-8rdmvx_yY6v3zYdeIUiwvxmLL984kseNUqy76ioCVB1ByE6ecaaS71Jzu-GmmaD4AL3mWen5CGCqk4NoxW8WBHjyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش جالب یک معلم؛ گاو نر تا زمانی که احساس خطر نکند، به جمعیت حمله نمی‌کند
🐂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/685544" target="_blank">📅 14:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMFtFWA6Mz8CApAkfHjyvh1FfJxmiwRxzmq1BjCN62RljseYUFSVHLljm8WQQDmIe0kOVP4-_mKoxipQXj6FVa2PomJtb66_9OEgu4dPu-GrRuQfzOGYBjBl9p0vmBwLyiwyADcxkuCrei2XQr5Sm9WWJjaMmU83FBwjnM8x5ns-86IUKWEqfXIpH_RdGGeNTP-fPvWziQj1XYGH8BV1SZ3OcYqToWyLb8CbaVA7psJFCPn39L1PAF0sB2ymPRt5R-z-dqNEYrSyHBceB70KG_FPn0l4PofPtfJUolWN6tk0aqD9zEYY72707BrbBIXDj84rWHfc1obo8KcQ8ZYrMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlXdsBQjaA5p0wYIKegGqOc5jyMtRW48c4M-cGoi43Pncf4JiHsn-yfMaGwtiv0JedOdwk0zvru6KNwbn6ko7j8AJJy9IO3F_LqOQrBa_4mtomoRv0xCV8ml-eAFo6Yx6x4J30PA7D9_dL6YvVdv9iLaFxT9LFUirXMR4pG12hGVTPiVIt-fpS0S2cBZ1T8yEBmmfkuU-BqZcOkYOUdoC23qDvG2Bio-nACuHdM1UDwe1FlvQscL_wHWP54Qb0K7AOzEzBSR1KKMwpZO_kPcP-lt-a3Y4UA_DonECea-1bo-doMWFD5fgKYLLQr-ep_IkTWw9Ow1jXOmmir6IooaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSvp0XAKPpn516U5Q_BxoiRv0Z_docamnroI0mNQLkYB0aHj4Q5tIIXxlBvkLybxXXDSy4DHlII7thGH6rP0N2-ri8nyrpQjs53DA8XDK1mjAKCNniJ4HnJlmGuP1cLrdy5BQSX_4msXmutJ36lcLyNypzaXXWnrY9wMsJUNYjh7uHh0_VDyGyyeGmNyBh7wLRkiAZbIDSbI8uis3bxeqFHyDAvhNQQUrotJ1xirrAGocJSOGTaLVWaWtOR78hcImTsou3xRvDneI_V8v84bCFMjE7EeT0zap3JRpcBsGYQy2iHR7P53xWnIvxSK8Mv0zLWf5W8jMufSFZPKIMRPjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انتشار دستخطی از فیش‌برداری شخصی شهید لاریجانی پیرامون مقام شهادت و شهید
🔹
حدیث اول:
رَسُولِ اَللَّهِ (صَلَّى‌اَللَّهُ‌عَلَيْهِ‌وَ آلِهِ): «مَا مِنْ قَطْرَةٍ أَحَبَّ إِلَى اَللَّهِ مِنْ قَطْرَةِ دَمٍ فِي سَبِيلِ اَللَّهِ.»
پیامبر (صلی‌الله‌علیه‌و‌آله‌وسلم): «هیچ قطره‌ای در مقیاس حقیقت و در نزد خداوند، از قطره خونی که در راه خدا و ریخته شود، بهتر نیست.»
🔹
حدیث دوم:
رَسُولِ اَللَّهِ (صَلَّى‌اَللَّهُ‌عَلَيْهِ‌وَ آلِهِ): «فَوْقَ كُلِّ ذِي بِرٍّ بَرٌّ حَتَّى يُقْتَلَ اَلرَّجُلُ فِي سَبِيلِ اَللَّهِ فَإِذَا قُتِلَ فِي سَبِيلِ اَللَّهِ فَلَيْسَ فَوْقَهُ بِرٌّ.»
رسول خدا (صلی‌الله‌علیه‌وآله‌وسلم): «بالا دست بر نیکوکاری، نیکوکاری دیگر است، تا آنگه که در راه خدا شهید شود، همینکه در راه خدا شهید شد، دیگر بالا دست ندارد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/685539" target="_blank">📅 14:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۳۰ تا ۴۰ درصد بازار کسب‌وکارهای مجازی از دسترس خارج شد
پشوتن پورپزشک، عضو هیئت مدیره اتحادیه کسب‌وکارهای مجازی در
#گفتگو
با خبرفوری:
🔹
برآوردها نشان می‌دهد بازار کسب‌وکارهای مجازی در سال ۱۴۰۴ پیش از قطعی‌های اینترنت حدود ۱۲۰ همت بوده است.
🔹
پس از قطعی‌های چندماهه اینترنت حدود ۳۰ تا ۴۰ درصد از این بازار از دسترس خارج شد و بخش قابل توجهی از کسب‌وکارها آسیب دیدند.
🔹
اگر دسترسی پایدار به پلتفرم‌ها ایجاد شود امکان ترمیم تدریجی این بازار وجود دارد اما رشد واقعی نیازمند ثبات در زیرساخت، اقتصاد و شرایط خرید مردم است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/685538" target="_blank">📅 14:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d31c32e4.mp4?token=XWlQr4K0KcBTrYQPDpuXUCBCixIz2sDmCmFvQHBdfGJ2bJGugL8Oadpf9BcUQUTRKJLP3tmE1Rajku3hxOdEihsdRtIcr0kQuHjmZs7_UVs1EhkkBZyzLmcV7UxxaN62TtyJOlNT0fPuQFzIyp-6rl3drxOLnTY7tlF5N2CzlNU6SGWoXEH_s4L44beEaNacO73mkngetIsYCrkoxQhDwl0kR3MfaH--C-ng_x5OtvmUgA5gwOMvCXWOVTYeB7Hu1IMoPofVFN4nJK4Zedq6UG48EtNJc5QhC3qQoRWadYRYRGurZxLS9XEvjM8ulwKG3RWjIrboUgcju_qLk3LRTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d31c32e4.mp4?token=XWlQr4K0KcBTrYQPDpuXUCBCixIz2sDmCmFvQHBdfGJ2bJGugL8Oadpf9BcUQUTRKJLP3tmE1Rajku3hxOdEihsdRtIcr0kQuHjmZs7_UVs1EhkkBZyzLmcV7UxxaN62TtyJOlNT0fPuQFzIyp-6rl3drxOLnTY7tlF5N2CzlNU6SGWoXEH_s4L44beEaNacO73mkngetIsYCrkoxQhDwl0kR3MfaH--C-ng_x5OtvmUgA5gwOMvCXWOVTYeB7Hu1IMoPofVFN4nJK4Zedq6UG48EtNJc5QhC3qQoRWadYRYRGurZxLS9XEvjM8ulwKG3RWjIrboUgcju_qLk3LRTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دارکوب خالدار بزرگ؛ استفاده هوشمندانه از درخت برای شکستن فندق
🐦
🌰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/685537" target="_blank">📅 13:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c275b5876d.mp4?token=lZOuCXSKiCsJs7vmnQ3ClGcwijJ8DI8w-1ewIlEl0gfHO3-Igj4U5N00_giMlLzn-QzqYprUjU2K1mn5_f0hKPX4Hd-GUtvAfud8rvZlJ3mkgcinsLlyHx2yTLCUWEVljVJclaEVkHS9nhQ4zViy2gxqjFHl4jVkWYMFixUuOs1ZH1x8ZS-0Qi1WzfT3D2ySJClj6JCeeS08He38PLa0pncYE-4CjEnynlndiUyi3UBRIPUiV01UKYpZCh3pd3GZXkGnKBnE58gH_0-1QAffL5qmQe0k9eMijVcJnN-XlDOJla4KCITYNBdfeiDxDi3JtMjwgOA258R6frPlWrwLDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c275b5876d.mp4?token=lZOuCXSKiCsJs7vmnQ3ClGcwijJ8DI8w-1ewIlEl0gfHO3-Igj4U5N00_giMlLzn-QzqYprUjU2K1mn5_f0hKPX4Hd-GUtvAfud8rvZlJ3mkgcinsLlyHx2yTLCUWEVljVJclaEVkHS9nhQ4zViy2gxqjFHl4jVkWYMFixUuOs1ZH1x8ZS-0Qi1WzfT3D2ySJClj6JCeeS08He38PLa0pncYE-4CjEnynlndiUyi3UBRIPUiV01UKYpZCh3pd3GZXkGnKBnE58gH_0-1QAffL5qmQe0k9eMijVcJnN-XlDOJla4KCITYNBdfeiDxDi3JtMjwgOA258R6frPlWrwLDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
از خانه تا بازار؛ نگاهی به داستان‌های موفق کسب‌وکارهای کوچک که با تلاش و خلاقیت رشد کردند.
🔸
داستان موفقیت و تلاش شما در کسب‌وکارتان، انگیزه‌بخش مسیر دیگران است، در یک پیام صوتی ۳۰ ثانیه‌ای از چگونگی شروع کارتان بگویید و همراه با عکسی از محصول یا خدماتتان ارسال کنید. روایت‌های  شما در خبرفوری بازتاب داده می‌شود.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/685536" target="_blank">📅 13:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فایننشال تایمز: دو بانک تحریمی ایران (صادرات-ملی) همچنان در امارات فعال هستند
.
🔹
یمن: سازمان‌های امدادی تحت فشار عربستان از ورود داروهای مورد نیاز مردم جلوگیری می‌کنند.
🔹
رئیس‌جمهور لبنان بر ادامه پیگیری پرونده ناپدیدشدن امام موسی صدر و کشف حقیقت سرنوشت او تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/685535" target="_blank">📅 13:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4592fb4ffd.mp4?token=ToIcHztstL__rOSgzEkif0cVANgQ2xaDZB0rz8Jxhs6aojdpg0V1Xp-8EiDRTe0LQzvF5xciaxY_9fZcQAl3FYSOltiR5RWKOFJgKxPNf9Eh49oOHP8TuUE0dXKfO0s34tm_PEWNDcW3mWwQk6Uw-V_5lM3vkk_8MRMFiMJXPK6vU5vY4qAElJ_kYzpo3IqAqBHeOtmVrJ4yg_A_zdld1NZrtNDNSoh1JlATdm22v9n7lxt-w-lEB_gFe2W1_8Bz7eBA-mxgdhqvtkl_t4ygKqyE_U9bUu13LtuStPDOyvAI5hzugl6Y9uRLT5b9rULMXY4xYqjMczrzHRVjSm1seA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4592fb4ffd.mp4?token=ToIcHztstL__rOSgzEkif0cVANgQ2xaDZB0rz8Jxhs6aojdpg0V1Xp-8EiDRTe0LQzvF5xciaxY_9fZcQAl3FYSOltiR5RWKOFJgKxPNf9Eh49oOHP8TuUE0dXKfO0s34tm_PEWNDcW3mWwQk6Uw-V_5lM3vkk_8MRMFiMJXPK6vU5vY4qAElJ_kYzpo3IqAqBHeOtmVrJ4yg_A_zdld1NZrtNDNSoh1JlATdm22v9n7lxt-w-lEB_gFe2W1_8Bz7eBA-mxgdhqvtkl_t4ygKqyE_U9bUu13LtuStPDOyvAI5hzugl6Y9uRLT5b9rULMXY4xYqjMczrzHRVjSm1seA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
السلام عليك يا سيدي يا رسول الله
🕊️
✨
💚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/685534" target="_blank">📅 13:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
الجزیره: آمریکا فعلاً از تحریم چین بابت خرید نفت ایران اجتناب می‌کند
🔹
به گفته یک مقام سابق امنیت ملی آمریکا، تحریم چین همچنان به‌عنوان گزینه ذخیره ترامپ باقی مانده و واشنگتن امیدوار است مجبور به استفاده از آن نشود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/685533" target="_blank">📅 13:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ایندیپندنت: جنگ ترامپ در ایران به یک شکست تماشایی انجامیده است
ایندیپندنت:
🔹
جنگ ترامپ در ایران به یک شکست تماشایی انجامیده است. تنها برنده مسلم، صنایع دفاعی است. به لاکهید مارتین ده‌ها میلیارد دلار برای تسریع تولید موشک پاتریوت اعطا شده است.
🔹
ترامپ در جنگ ایران پیروز نشده است، او نقاط ضعف آمریکا را به قیمت متحدانش در معرض روسیه و چین قرار داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/685532" target="_blank">📅 13:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685531">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb7ff1ee0.mp4?token=Oq5rS34lUE2Z2rQwRIu4C6kkGd0g_DvrVfbYEEr9DZAIPOvZU8RtO_XpKS7bGzDIICmbYRQgMhLgNw4ipkmzTeaoJBHdpxuo-8TmCX2lk5y4wiuPdlbZ4h9b3Qd3Pb9ZVr90Bj99yYvcAhyvUZ57FciJD943nHerENdDyuVQ9-uw0oKRdZcNxZTIc_0kqf_sJBvU4ePDBZvwaAZlurq0TE6ENblhn7dWqwLOmIs5PcjYDxzFOvEtt1hgcah4467-icaUf7DAfX74VbW3G8E7c5TiGOGn8AUlcJJe8QTfdBA59H52GuAu12y0SuOjEoOtFg75ewod22a4JzrlEqXHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb7ff1ee0.mp4?token=Oq5rS34lUE2Z2rQwRIu4C6kkGd0g_DvrVfbYEEr9DZAIPOvZU8RtO_XpKS7bGzDIICmbYRQgMhLgNw4ipkmzTeaoJBHdpxuo-8TmCX2lk5y4wiuPdlbZ4h9b3Qd3Pb9ZVr90Bj99yYvcAhyvUZ57FciJD943nHerENdDyuVQ9-uw0oKRdZcNxZTIc_0kqf_sJBvU4ePDBZvwaAZlurq0TE6ENblhn7dWqwLOmIs5PcjYDxzFOvEtt1hgcah4467-icaUf7DAfX74VbW3G8E7c5TiGOGn8AUlcJJe8QTfdBA59H52GuAu12y0SuOjEoOtFg75ewod22a4JzrlEqXHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عینک تاشو انگلیسی؛ ساخته‌ شده ۱۰۶ سال پیش
👓
🇬🇧
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/685531" target="_blank">📅 13:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685530">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K854ZngugkrU3GRFGQtUFVIV0ic82hSAImRpRcYoWqfca4vVo1Cg9K8YDUDREecYtODNDXUSvyTWQOx50upLHgRuQTUM3KyRPinkV6r59sWl-5RxTYIaKvuCF19I--85dBYBSI43JHNnUrMRf00isaoagjWbHHodT78PUz6ldCA-2D_cI2bS2hJxgzgiligyIBmZB0kuIuovYytv7hhASaioIEbY3dzs9Ud5WonYj4Pu9zQ9Rdu4F6niXmovmSsfWCiPfR-bdt3JTBm641Zy2o5WuO-JQbHmsRSriRLBxkkD990hn8UFB5m0fo_1sjOduqibXIpW--QqRX-ddWyCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز جواهرات ایرانی که دیگر در ایران نیستند/ از گوشواره‌‌ای که ستاره هالیوود به گوش انداخت تا گردنبند گمشده همسر محمدرضا شاه
گزارش خبرفوری را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3241302</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/685530" target="_blank">📅 13:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685529">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
قیمت بنزین در اسراییل به بالاترین قیمت خود در ۱۵ سال اخیر رسید
🔹
هر لیتر بنزین ۸.۵ شیکل ۴۰۰ هزار تومان.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/685529" target="_blank">📅 13:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685528">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4f4f2828.mp4?token=KpiuV4FiKNoRMTiGTGNld56R1wB76-YZHQ1RaqqCJZ32oX0DBbJM0XTQMBhg5X-M-pwO608yg0sT4BHKBHiEmaq8PE3BJKow799XrkRLtFoiy7NHzLphQI0Ei8Qw-Mw_QE6wemPnrqbEaxu0xCpSmMsIDk3KwDK2TCEcdVQ1-m99KuDdEOW559mGqVYI-YZn63waZWu0FYPkvpWwRcZMI2NIaB67MMB61FnJyiv8949OF2lHOAfJHNbtLdBPpwyHPt2G13PgV4ZhYFUW-3_Xw7TVOn71uUbnM8meq7LxwnEKzqkD-j_x1Wv4p79E_Mjg9dLwu26Hr3Vw96TSSeAvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4f4f2828.mp4?token=KpiuV4FiKNoRMTiGTGNld56R1wB76-YZHQ1RaqqCJZ32oX0DBbJM0XTQMBhg5X-M-pwO608yg0sT4BHKBHiEmaq8PE3BJKow799XrkRLtFoiy7NHzLphQI0Ei8Qw-Mw_QE6wemPnrqbEaxu0xCpSmMsIDk3KwDK2TCEcdVQ1-m99KuDdEOW559mGqVYI-YZn63waZWu0FYPkvpWwRcZMI2NIaB67MMB61FnJyiv8949OF2lHOAfJHNbtLdBPpwyHPt2G13PgV4ZhYFUW-3_Xw7TVOn71uUbnM8meq7LxwnEKzqkD-j_x1Wv4p79E_Mjg9dLwu26Hr3Vw96TSSeAvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجسمه‌های رنگ‌آمیزی کودک؛ ایده‌ای ساده برای تبدیل خلاقیت به درآمد
🔹
این بار در #چرخ_زندگی دنبال یک ایده ساده و خلاقانه برای کسب درآمد در خانه رفتیم، ساخت مجسمه‌های خام مخصوص کودکان.
🔹
این مجسمه‌ها را می‌توان در طرح‌های مختلف تولید کرد تا کودکان با رنگ‌آمیزی…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/685528" target="_blank">📅 13:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685527">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
۲ نوجوان اسرائیلی به اتهام جاسوسی برای ایران محاکمه شدند
🔹
دادستانی اسرائیل علیه دو نوجوان ۱۴ و ۱۶ ساله از حیفا به اتهام همکاری با یک عامل مرتبط با ایران کیفرخواست صادر کرد.
🔹
طبق ادعای یدیعوت آحارانوت، آن‌ها در ازای دریافت پول اقدام به تصویربرداری از اماکن، نوشتن شعارهای گرافیتی و جذب نوجوانان دیگر برای انجام مأموریت‌های مشابه کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/685527" target="_blank">📅 13:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685526">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuSfL1s8iNLvEqg2zbEW6YwrmMS1WmwE9_lIEAWRiMz5E7s5B3WUjvtgu3836H6c_BMJxJnQbos-nd5NStARdITcp0hsCSVZ393bSqQznnP-JnjTDG-sAKzFaFi3MTORk0E87LVeAe4kjYz_13WUML5PDUPvXwx0X5vcHzidCFQzxkMukgj9qBMaLwKrERZ7D6AjWq0tNNG7kZvQc4ovRk-0UZtQTjy_PzzFmXPtpkYx-_ho3TUJJb3Faa3-bkz5ny9kjPlN0-20YsDpm6gXizsa2DHm3lkyTOdL1KxIpTIzLQ10QcqK8AC0Dnk2DWo9XU6OfdZc9AFY-Od_2v6z_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۲ درصد آب شیرین کشور به بخش کشاورزی اختصاص داده می‌شود
🔸
کشورهای افغانستان و پاکستان با اختصاص ۹۸ و ۹۴ درصد از آب شیرین خود به بخش کشاورزی، در صدر این آمار قرار دارند.
🔸
ایران نیز با اختصاص ۹۲ درصد از کل برداشت آب شیرین خود، در میان کشورهای با بیشترین مصرف آب در این بخش جای گرفته است.
🔸
از طرفی دیگر، کشوری مانند هلند توانسته با بارندگی مناسب و بهره‌گیری از کشاورزی مدرن گلخانه‌ای و سامانه‌های بازچرخانی، این سهم را به تنها ۵ درصد برساند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/685526" target="_blank">📅 13:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ab68c2f.mp4?token=F066t_yUdGNnNzKD8aWv-c_mWEeKDqi3Y1LjsifZP8d1up-T_zyUEw-Z6AFeoFL-M7rUOzzkhGs2ZwBBO0g3uD9Kni-EkWvEPJGgm8W2_aIePYZGdOblHLDw4R218EF0DAAskcd6EddsUjX0jGr4C_OKTyjX-Rq_Q3oJAn5Y6aDY6u1IsHP0F4qQZSYiMnDC4EgzpZfVVl0bJyue9thr1z8i3SM1gPGBtb_e_gSshUxoOC1kZ44XYaH01byHjOtH1EPWSKcAb38I37FgG7RXV3UNr24NDmzySd421W7Z_gp2uQLD7Zkd95VSmfEt7VtyrbmtvH2LEponccqVEgTIbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ab68c2f.mp4?token=F066t_yUdGNnNzKD8aWv-c_mWEeKDqi3Y1LjsifZP8d1up-T_zyUEw-Z6AFeoFL-M7rUOzzkhGs2ZwBBO0g3uD9Kni-EkWvEPJGgm8W2_aIePYZGdOblHLDw4R218EF0DAAskcd6EddsUjX0jGr4C_OKTyjX-Rq_Q3oJAn5Y6aDY6u1IsHP0F4qQZSYiMnDC4EgzpZfVVl0bJyue9thr1z8i3SM1gPGBtb_e_gSshUxoOC1kZ44XYaH01byHjOtH1EPWSKcAb38I37FgG7RXV3UNr24NDmzySd421W7Z_gp2uQLD7Zkd95VSmfEt7VtyrbmtvH2LEponccqVEgTIbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازمان زمین‌شناسی آمریکا (USGS) امروز رسماً نام «دریاچه انتاریو» را در تمامی اسناد الکترونیکی این سازمان به «دریاچه آمریکا» تغییر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/685525" target="_blank">📅 13:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685524">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b86de90f3a.mp4?token=PQHR7eBUU_22AjV38tWMYfS4COfrfVQVWwIMtjrmEUtouuMORxfowcWQShs4p12C644W0ry8FUT2NrWle5UoknxPS9fhdVU05u_lBo9rgVlM20BC00UQBSjO300sXk2xN9cEvJoT0MrboKOcOl9NiIndWpka41e8lByTb1HfLdCa1H-7o7SWnU-_lUvvgUJMIePrqHKsxVPKuz8z-2BZp2JXR7ZOXM3z2m9Z2IzhZJDxekdnNA38K_uey_Of2yyHcp3MJ_E6zobDzS7z1vWKYfSBlgoptnz5hFIOtHt1sC8N58hxvSX8rsg8yIo4eMhh5gZSmBu8HPqUF28EEKoadQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b86de90f3a.mp4?token=PQHR7eBUU_22AjV38tWMYfS4COfrfVQVWwIMtjrmEUtouuMORxfowcWQShs4p12C644W0ry8FUT2NrWle5UoknxPS9fhdVU05u_lBo9rgVlM20BC00UQBSjO300sXk2xN9cEvJoT0MrboKOcOl9NiIndWpka41e8lByTb1HfLdCa1H-7o7SWnU-_lUvvgUJMIePrqHKsxVPKuz8z-2BZp2JXR7ZOXM3z2m9Z2IzhZJDxekdnNA38K_uey_Of2yyHcp3MJ_E6zobDzS7z1vWKYfSBlgoptnz5hFIOtHt1sC8N58hxvSX8rsg8yIo4eMhh5gZSmBu8HPqUF28EEKoadQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین پرواز HÜRJET؛ جت آموزشی مافوق‌صوت ترکیه
🇹🇷
✈️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/685524" target="_blank">📅 13:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685523">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlUtNsRZo-QJHMWIolQU5zg2qcl7F247IJ_SsjWrwpssp07agfIeK1nieKnPHafH5dLItDtp3ngeyIsDuN_hvSXf_IT4nL6WuO6Ruq-9JvAzb7wlFj6girk_M7XRo3-ThgeMaqtqgYBdOVHEydhYb0pBb48hcDeOYChwQeek55dq4DuG9417jvwnTwupXzxX7UQJqz4oZ1tw3KiOdcWbGMNkoWlxwJbGPCAnp2AgSvzFDSDeOlu8N_YsR6ZYNbi2nmqq0xuohK_cj7L1rhJZ7DJv_vtcT2jzD9k4ZNxayDN8QvLcTPKgmwDIS8fFkIppcDo1ZMV3jv6Mq4q9Qm50Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از یک محفل زنانه در ایران دوران قاجار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/685523" target="_blank">📅 12:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685522">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
تانکر ترکرز: میانگین روزانه صادرات نفت خام از طریق تنگه هرمز طی هفت روز گذشته ۳.۸ میلیون بشکه در روز بوده است
🔹
در دوره اجرای تفاهم‌نامه (MoU) که عملاً تنها ۲۵ روز دوام داشت، این رقم ۹.۸ میلیون بشکه در روز بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/685522" target="_blank">📅 12:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685521">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79a8ee04d3.mp4?token=WuJs3AzB9VPN20BBa6qnxR9_2QJdjsrw8PmW636pEIqXRQjd7uvQQQ3OOTAUrP8qO0Jd2PQLPn_vs9Woi5_RKEUEuN3slXXufOdkgL_hhefuwp-XQN_0KGlmg8vK1iQtUiZJN9a_b9AiNfb1CWBLyUlsisIHyMQt8zDqWJBiqnl7GVKD0blh4UAqfVG0vMmcq-aUai3smaQHLjklG320g8C2meQAYTGV2X2aR8qvtIYvkbA5ngfC0j-xzzv8C603sNmaFP4z-TRoEFhZ535r0oQ3cwAprANNGasnceYWEySg8PEKOQx3hcDTPpd5COMDQ48idLHWMlzNlTbhRl6k81jGUGLReyDP3HByirv1qx7LKhOroZTV97c1u0dnLqCvKsbQQl1iPY5kswwLs4puo0zAFi-Wd-GCLbwKHCnxAXbKxEpru-KZSGcDY2DQtDnNmBa7UDOIJaA8H6mzU9BS6TYut3bzfhQWvIENMijBXZlOJum7PQ-1e3xpps9ju0P4gXet7aeEce5Ow35CbrVwr93xUxMAdwCFxSPJ5TTCkUIMXlTJz3zFt0GRa8-hTAaU1jnfzhP7E-THwEH7pCwsRHChaa86vW4SLQkDLDpOdK8a4nfrwpyFCIcrDaPqzTHqCb4vAPtzQmfrpPqR-gn-N0N5RsJeB-Kid0c9MwzQ2ks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79a8ee04d3.mp4?token=WuJs3AzB9VPN20BBa6qnxR9_2QJdjsrw8PmW636pEIqXRQjd7uvQQQ3OOTAUrP8qO0Jd2PQLPn_vs9Woi5_RKEUEuN3slXXufOdkgL_hhefuwp-XQN_0KGlmg8vK1iQtUiZJN9a_b9AiNfb1CWBLyUlsisIHyMQt8zDqWJBiqnl7GVKD0blh4UAqfVG0vMmcq-aUai3smaQHLjklG320g8C2meQAYTGV2X2aR8qvtIYvkbA5ngfC0j-xzzv8C603sNmaFP4z-TRoEFhZ535r0oQ3cwAprANNGasnceYWEySg8PEKOQx3hcDTPpd5COMDQ48idLHWMlzNlTbhRl6k81jGUGLReyDP3HByirv1qx7LKhOroZTV97c1u0dnLqCvKsbQQl1iPY5kswwLs4puo0zAFi-Wd-GCLbwKHCnxAXbKxEpru-KZSGcDY2DQtDnNmBa7UDOIJaA8H6mzU9BS6TYut3bzfhQWvIENMijBXZlOJum7PQ-1e3xpps9ju0P4gXet7aeEce5Ow35CbrVwr93xUxMAdwCFxSPJ5TTCkUIMXlTJz3zFt0GRa8-hTAaU1jnfzhP7E-THwEH7pCwsRHChaa86vW4SLQkDLDpOdK8a4nfrwpyFCIcrDaPqzTHqCb4vAPtzQmfrpPqR-gn-N0N5RsJeB-Kid0c9MwzQ2ks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی تاشوی سه‌تکه Huawei Mate XT 2 معرفی شد
🔹
هواوی از نسل جدید گوشی سه‌تکه خود با طراحی U‌شکل رونمایی کرده؛ ساختاری که برخلاف نسل قبل، نمایشگر را به سمت داخل جمع می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/685521" target="_blank">📅 12:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685520">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
تیم ملی والیبال بانوان ایران چهارم آسیا شد
🔹
تیم ملی والیبال بانوان ایران در دیدار رده‌بندی رقابت‌های قهرمانی آسیا ۲۰۲۶ با نتیجه ۳ بر صفر مغلوب ژاپن شد و به رتبه چهارم آسیا دست یافت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/685520" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685519">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
کاهش جمعیت اتباع خارجی به زیر ۵ میلیون نفر
رئیس مرکز امور اتباع و مهاجرین خارجی وزارت کشور:
🔹
جمعیت اتباع خارجی از ۶.۱ میلیون نفر به زیر ۵ میلیون نفر کاهش یافته و طی سال گذشته نزدیک به ۱.۸ میلیون تبعه غیرمجاز از کشور خارج شده‌اند.
🔹
همچنین جمعیت دانش‌آموزان اتباع خارجی از ۶۰۰ هزار به ۳۲۰ هزار نفر رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/685519" target="_blank">📅 12:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685517">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920d463811.mp4?token=VQ780u9SrtxvaQA1AnTEh2RVUyJn7NvnWlt5Equwbg5KawwFnIeHFkh9eE5mEp1_HDgeRs4Pv1XRbvgEBX7aRhjzoKCbSmkelk-VdJzHIqcxucLcsn6aoZJKVNziqSgKD7Y-69KthG9s6CWX5ZYUexZVpbq36kgMyAh7_zwi_YawgPn4eCczzcFwqY7gCPYxSWnSfJkoqyfOR0aWKTtakP95pJJBBAN8ZqVjIWZ0WecQFkDuNUNsq_ImZrw_IMbsJc28yAM8Jz3VkUL9jIAPuCp8rPtVcHPIvoXxOurP3nrD3ahlVbYJaRtgBcumBoGXVGMySFT7eJVDF6pRcJM4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920d463811.mp4?token=VQ780u9SrtxvaQA1AnTEh2RVUyJn7NvnWlt5Equwbg5KawwFnIeHFkh9eE5mEp1_HDgeRs4Pv1XRbvgEBX7aRhjzoKCbSmkelk-VdJzHIqcxucLcsn6aoZJKVNziqSgKD7Y-69KthG9s6CWX5ZYUexZVpbq36kgMyAh7_zwi_YawgPn4eCczzcFwqY7gCPYxSWnSfJkoqyfOR0aWKTtakP95pJJBBAN8ZqVjIWZ0WecQFkDuNUNsq_ImZrw_IMbsJc28yAM8Jz3VkUL9jIAPuCp8rPtVcHPIvoXxOurP3nrD3ahlVbYJaRtgBcumBoGXVGMySFT7eJVDF6pRcJM4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر پاهایتان حالت پرانتزی دارند یا زانوها به داخل یا خارج متمایل شده‌اند، این تمرین‌های خانگی می‌توانند به بهبود وضعیت پا و کاهش درد زانو کمک کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/685517" target="_blank">📅 12:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685514">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f83e55167.mp4?token=dOw5csm8KQvv4rvNBxscau0Tb26VhdSu8GfJoU45OlHwTUmvpD9WTT0W2ymU0i6d5t814TTuAveOSUhQXzAOwGj_yVePZGrsPQ8_wBd22mo1H8ajBJEpCLq3fF_7NpFgCywuPWFlMHusbRtASBibd8kaxv3Wn2U5UHiHc76PBfI2A-c7Y2hWYOPL-1H2onzifbavHtFAPlNg_EWRBtMCSFaVY4qvJtrqp8odumWjnXAl1oUUewBOBkMQwR0934HcxXaoN6NHvuayIJvYubrZTgA8oWMUKd7VkgW35A9sFz4xlvnxgaR7hXj57FD4m5Yt9SzQSQqRJiShn7tgXFzDtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f83e55167.mp4?token=dOw5csm8KQvv4rvNBxscau0Tb26VhdSu8GfJoU45OlHwTUmvpD9WTT0W2ymU0i6d5t814TTuAveOSUhQXzAOwGj_yVePZGrsPQ8_wBd22mo1H8ajBJEpCLq3fF_7NpFgCywuPWFlMHusbRtASBibd8kaxv3Wn2U5UHiHc76PBfI2A-c7Y2hWYOPL-1H2onzifbavHtFAPlNg_EWRBtMCSFaVY4qvJtrqp8odumWjnXAl1oUUewBOBkMQwR0934HcxXaoN6NHvuayIJvYubrZTgA8oWMUKd7VkgW35A9sFz4xlvnxgaR7hXj57FD4m5Yt9SzQSQqRJiShn7tgXFzDtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوخت چگونه از مخازن زیرزمینی به داخل خودروی شما منتقل می‌شود؟
#موشکافی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/685514" target="_blank">📅 11:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685512">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIBJOL0elxvvu6PphSHWrdHdfpV9JEEYGmw6TAWJff5VJR-SLqqjqyx9Zaz9mHGkLNnLe4pGXOXAmqew8R1DK56cjXNa8NEkij9W1xTykpYEmK2TCW-uUuKA-DOVoL4xHkIgIkxsqrMIrGAaD0a0g6YCEu8yA_Nqbx56DogvAZRYDH0QC6U-hD_iVn2vjJfIP9xubLZ3B1PDy3TCW59KxEryYyCMBJ9ziC4R0GIC2vUtdFjKaPEBKyysITNo5SE8N37zCwx0RxEPszuZwAoOsOwYFieMCFK04DJDQR10KqpPP4JZyaUCY5oZPZWcGAib1gIIKV0p4oGrTH2bOl9K0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiUxh1vIK461JGAMMXgQleEoPHO_KLVb0Kj2stp3w8Ql25xloEiGNBQF93SWjD_aaZkLJwzXs38nH5CN5fWcDOmhG7W322TC_CKo-PoF7_E3zRbQSRvCl47JjVwYMvI4DQZ_hV0WEcN_bP8m9pYD_lYvMaYz_i3VOWXhphzuwsgXp1vL67_YkAV9kB7hPtJxou7ZB-AErJru_8FXjwAbBGHZysQzKe3PFLvO7gcLMTssyZtAFcZYnWSA9KUpspm5xPTGkeBl8ug93dQA5otlzj-kDjc0TKG8SrLubPIK93XUlWPl2hmrbg72LAKacKIadaEvx5NGB4EmkDnKDEYj1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آزمون تافل در ابهام، آزمون دولینگو با محدودیت روبرو شده است
🔹
دولینگو اعلام کرده افرادی که از مدرک هویتی ایرانی استفاده می‌کنند، امکان شرکت در آزمون این مجموعه را نخواهند داشت و همزمان، گزارش‌هایی درباره نبود امکان ثبت‌نام و انتخاب تاریخ آزمون تافل در تهران منتشر شده است.
🔹
این تحولات، ابهام‌ها درباره دسترسی داوطلبان ایرانی به آزمون‌های بین‌المللی زبان را افزایش داده و لغو یا توقف برگزاری تافل برای ایرانیان هنوز به‌صورت رسمی تأیید نشده است./ فرهیختگان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/685512" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685511">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
سود سهام عدالت در روزهای آینده واریز می‌شود
؟
🔹
رئیس هیئت مدیره اتحادیه تعاونی سهام عدالت کشور از احتمال واریز مرحله نخست سود سهام عدالت در روزهای آینده خبر داد؛ با این حال، زمان دقیق و مبلغ نهایی سود سهام عدالت ۱۴۰۵ هنوز به‌صورت رسمی و قطعی اعلام نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/685511" target="_blank">📅 11:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685510">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a2c950187.mp4?token=M4x4ppLMqZ6nEICfmK10g4g2mEcWLtchmTBFMVK9cbWvJ6_P_EE9egYqy6bkk_HtkzJ_L9zA_vspkJ2H2XaZAxlTAMvRfaihJmRO4WLiTmlx7sapGQYYC1N4fCWXNRlHA4XQZjDzo-lIdvPAsyC1aAp-JZULb_zaQBRzzLyhC80ibWZCORpXvSLVFiUGbv3-Br_123Qp_qbjgW9GHSzAv2GaiTR5GA26kD7om7A2NH3Y9b-rxWBlKc5wHJCpW6yo9cTr5Zlh-KYrY8NccGf_2HIJyX3qv2l6DwnPJCGpcuBM1gaX2mUU5PsglCdgvXlCxK1oV9VcgKrmWAhC2gQ_RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a2c950187.mp4?token=M4x4ppLMqZ6nEICfmK10g4g2mEcWLtchmTBFMVK9cbWvJ6_P_EE9egYqy6bkk_HtkzJ_L9zA_vspkJ2H2XaZAxlTAMvRfaihJmRO4WLiTmlx7sapGQYYC1N4fCWXNRlHA4XQZjDzo-lIdvPAsyC1aAp-JZULb_zaQBRzzLyhC80ibWZCORpXvSLVFiUGbv3-Br_123Qp_qbjgW9GHSzAv2GaiTR5GA26kD7om7A2NH3Y9b-rxWBlKc5wHJCpW6yo9cTr5Zlh-KYrY8NccGf_2HIJyX3qv2l6DwnPJCGpcuBM1gaX2mUU5PsglCdgvXlCxK1oV9VcgKrmWAhC2gQ_RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوت ناگهانی هنگام سخنرانی شبانه
🔹
نعمت‌ الهامی از چهره‌های شناخته شده منطقه مغان و کاندیدای دوازدهمین دوره انتخابات مجلس شورای اسلامی از حوزه انتخابیه پارس‌آباد، بیله‌سوار و اصلاندوز، به‌طور ناگهانی دار فانی را وداع گفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/685510" target="_blank">📅 11:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685509">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQjSfM2T2q5Ryylb_4slTUGcO4d8SyXyDV3FZ1shzNV4Rr4SeBWRwOo4DfFJNUzgKD4t47GS2MXo83ajX3z97PKm4-V89TWF1wzaATVsiNPuK5fk03COestziCcbK1dr_9ZfCLPKYtd7n2GWUzyVI9eIXMU4_33m2gsX_6c86TXKq8EAgbbcU0F-qHSo1jJFJa-S0qWVJ23hvgiLQAZ2Gg6ZxbNhC3sC5_Zo1p9ZSKWfdvwmvgv9RhnXxSKBN-5UhVsEe7Am4-5v6BQUgNnuPzX9PfQ8E5MBrf_8qvaMg1WBeRUHsqdQpbS1dFt50GfJq6HZCxRA2qu0Cco3L1jPXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آماده‌باش سرویس مخفی آمریکا برای حفاظت از پسر ترامپ  ادعای سی‌ان‌ان:
🔹
پس از پخش ویدئویی از تلویزیون ایران با عنوان «بارون ترامپ را کجا خواهیم کشت؟»، سرویس مخفی در حالت آماده‌باش کامل قرار گرفت.
🔹
این ویدئو حاوی ادعاهایی درباره نظارت بر دانشگاه بارون ترامپ،…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/685509" target="_blank">📅 11:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685508">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81ff99cf26.mp4?token=ODo1rvsNYj5bpx0uw1qhsHVPMRcTEF_aaBgqVY-fHDSkbqIfhHCVz_fGZjPuQwZCjussl3jcqkjIxuj5rxZltVFeMTZ3Wwb_S45oFleAlJ3fDvfbX4KKMx2PyvC0FcdSBmyGVLw3NyL2q1NxZBz4wHGO80psrRn_LAN7Mfj9AvQf7vBTxmuyiQFmJ1d0BuYqMQ0anppCiy9aPJiyxyu3HpVvMy3vCozf-5Ugd2P86N2XK6mFIt2H5h3qUiYCdCVmossfJCaSdEWy0fIGHwfvE9FOoreJW1a0MVHmHwzLf4qNLCxLxv3RoXyRJW0kVbbYVrR1K0hqS5ODXD9xvaKbIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81ff99cf26.mp4?token=ODo1rvsNYj5bpx0uw1qhsHVPMRcTEF_aaBgqVY-fHDSkbqIfhHCVz_fGZjPuQwZCjussl3jcqkjIxuj5rxZltVFeMTZ3Wwb_S45oFleAlJ3fDvfbX4KKMx2PyvC0FcdSBmyGVLw3NyL2q1NxZBz4wHGO80psrRn_LAN7Mfj9AvQf7vBTxmuyiQFmJ1d0BuYqMQ0anppCiy9aPJiyxyu3HpVvMy3vCozf-5Ugd2P86N2XK6mFIt2H5h3qUiYCdCVmossfJCaSdEWy0fIGHwfvE9FOoreJW1a0MVHmHwzLf4qNLCxLxv3RoXyRJW0kVbbYVrR1K0hqS5ODXD9xvaKbIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کف پا مرتبط‌ترین اندام بدن با ارگان‌های داخلی است
🔹
باید با انتخاب کفش مناسب و استاندارد، سلامتی پاها را مدنظر قرار دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/685508" target="_blank">📅 11:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685500">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sP3i7HgTj8EXQo02O6-ChX2OQBnb8ydKIe_vAlMbIztVWueFj3Sa2nTA8NdwOD-BpDq3D3HEOOO_nC0wcRkDDY3B8n28qjrhNr2SwK-hSlr4tdHGkBI1pem3zqQDvf-ubHcNKunZ8vcraT1Lj8IiBIVIqbGATDSb4kzSg6ECnQJF-RLDTaGYKbpQPJt4AZt1SAMXoWL5bp6V3f-_8z8w2XComUK83chKtuBtijX_NeNLABVzlabNGtMFYMvEuDkpq3lHdvpOA6v87MjKn0kZ3vBeoh3txuf_8W5_O0cLpKUqJqiZYY3NWr87DwQUWd32XQiEK8J2I3-RkH7oCTkEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqoxqKBCasOEoXaUpGyrxdKnUXwhyNkn-d54t_M8JOS99a1053LidXA0Exr-UJQecxrTnBx_-_3-4tsgZkn7ELdxZ4vJpc8bBg5BKgHJM1bc9fZXmVhRL7dL6sLAnkNGGQq2dy2gCLTvKrN-KoYjAHsl1cbBeHSnaLXxFkqdlk-lDpCCex9WmmnMzPysAvMAwn8LTZKF7hWDoU7X4yPHlSGij8kghLO-vkGRI7KOn0tcJihZefHPK4AfuBiLJ0Sh-7RCQXyAp7hwbSVuiF05bYkLhWgZIhlcyd40mDvu5QnSCWj--WNArd7IHUT-hR_CdbvKQJIyfdGOY4RqnoaZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KK7lKLva7n-4YOHV_PWSoH3-YVXURBn-M_aUqt5rkW05cTMC-Q1ntIpGmnBf_Z63Wqv3_UyjQ648-IFEagToOCE_dsOe10Yheom0VPBeGYIUNUDp6Y8jA5QDFI7Ux3g-BL5w9KJSX7Q3OyKDzcRbk2ZqebPqO_3ECitP0mMZj8Dx97x-3tYct91WTudhpLfHBdc-TJp-ZfZrEhIgQYtwMTM64KVoKHkZNipelMMgcIU2FaoqLokNMVGL0yih7p4SsMczQ6RlBNy1GWMsf5QkNDarjPw23Qq-FBiigYN0OaaxFnbZGV1drQsUvThMPCAKqoBK8x0TNYesJGX7htjX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRao_-wlH6ni4P2doIFw2Pk_NPy9p0_mUVtDu7XXjeOfxNRkvwJWF6K-_i8Nj3VK0yndFyF7oflsyuw9A0-Gmxx7vwzKcb-VrWlTSfX-Eee9ePyDHErThmCOeBLBxowXKiifEwdDiBepLVZSUcGbnSkiGW5lr1q2d-tHyhXnBImLli8hdiYJHFh3PPkDdZZZCmfL6kSmK6rsE-qqDqFp78nV54Bdhflu2_cGr2rC6DaMn85ZFao0NK42flO_LhqN8cy5GdCDxmLTlnhzAr_CYGCFFYX2pgLD59tERDGf2AsMYnMO9dPjw4Zce40a7UUBpAx1rd9hLwZ-5qMbhn-Dcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCIx_h0R-w0moo7c1gbzV_Beu26yTcklhnsydUCYZvsv0L0o8-UANccyeGoQ69dUlIIJL2UvWPwInBsLHW9-UvLNH9I0KYaD2MKww7R8SJhCB3omPVo3WDQWKShVhaf4ZDGa34YZCB_hoBlPUu44fcb2GOmsez4MP-0sa01UXxW5XcaAu1GWzWoHEADqKKgc7yf9oqL3_VOYYwmiB8zzjszz5JZSHVFZzwg5sIkVaChbklHlwq4igiPR7g76oryDsjMIhJCRY336LLOzQcVorn-M_bIg-jsBrKaLh-PXEIFyekRNoYmeV4AJ8uFUJAHFxlg-558Y9Lim_S9IN6vHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNAfCQLuiYb4DN535LOJQIpl5_kv0GMSmZ8Nh6rtzMieiEx23C6OvDyO_5gHRdQQVu-5_wDcRNJCcg9YNHdppWl5C0yeDx0I8rqVpEMEY7Dtak0mBFejWhdKLB4DYFVyd55ufO-NWaGR7UMWQ4E5kSj3CyOSuHEWY71wfrBS-Z8cUqVPKzSnOqhMxl1A-lLaA2kmpPtDbOKqLfH5mYjaBw5nWUWHAXecfJwfLXGP4e_THJ_KAFEzgFevxcY9nwtFLuY1-B5yGnoc_VXpY-u8rn7k_6kxLQmKlnMBk-CI1uMxAZPtGU-4Zi_EvdN_ZHfjpXNvoqBwPzqOV-7612QBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYsx0V_8yjgICpTv9FpijhxH9Nqt2ehHkCLZ_7tyyUeLhjz6yj5WvEY4xTAOM7O_U7HpSUylUDWWTS2i6ia6Kyo2Eg72xWsVJOfSGsm7YfhV4lAM4YKcywP3PkLiEzgNT92a7pDo-V1-3stFQ4EkdcrGcH9XzxWFyfl7oCJHc2jLNdLt5yKUG2UFqVKcuUN4rxEDOXbqeqqWGO5kqLve4KbalHWLZX1Y25xc2_tRNPBaSRRtXvjEa6Xvqns-aoKIlMjvkNREPJhpwVV34LdM6-SL8FDP9fJTWpi5xVTSr_wKhghSFxsY-Yg5mUqJSncqKf0b17hoNXz_lY14u2aLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETWWDUBdAQ9pRR3DISkUo_7AHGFqQ5gYpA0Av5B8EnjXIGCjEIT5BxvceCrlJ-yHnXT_s0xNeiuqyXCL7MQNkbymM05LOnbFCXD69Jm9rm3OrKIEjWpKMDPLRSXIiOkHU-bFo9cGdCCoyEPNtY2jze6stohid0Id2ByZVc3EV4YDuNlblTYOm9Yv371Cv-hzoWHOxCeiGkcuc9Bit7mXNesQaRUUxkbd0xVN6sx152mXJzTPLJQciqQ17RZcUWXBV7jpomhiQs-FhKj1R7VdgMTiXYCGxDI2p4tBTQ_tMhmmbrLX8WKSkURtFeOFjklCahJQYjlDSeqCHzMRnDw1FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری متفاوت و تماشایی از ماه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/685500" target="_blank">📅 11:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00434ac85.mp4?token=EtYLpWjW-kfGqcb_ZTyrxOd0DQlv_3ENfGUOX2jKDk2PUNYv9_8u_kZkrYIm8xnUM-kLQV4168CEwLA-8n3sAL4d35oXUSu_auSMFF_cP0pjEE98N5pXWDZ_sqtWc9mGdDfMjkTGC_zLnyWtBCvd4eRU6BXQdVT_QuIlzkCA_GtdPFyyVlYhFD_ZGlbevM8442hTtxu7UU-z5LFjgJ-cHh8O1m18ZMJeXryW_eA2XSW7MusyV7ukfnru-YHTTSUkmZBk-uKlIkOUc5_jMAwfECYQ3ABwuN6zsWvyMgzVOvDPUCtpD0hZT9yIu3lqJxwM5ZMYvJeHWKn3uiflMMzOuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00434ac85.mp4?token=EtYLpWjW-kfGqcb_ZTyrxOd0DQlv_3ENfGUOX2jKDk2PUNYv9_8u_kZkrYIm8xnUM-kLQV4168CEwLA-8n3sAL4d35oXUSu_auSMFF_cP0pjEE98N5pXWDZ_sqtWc9mGdDfMjkTGC_zLnyWtBCvd4eRU6BXQdVT_QuIlzkCA_GtdPFyyVlYhFD_ZGlbevM8442hTtxu7UU-z5LFjgJ-cHh8O1m18ZMJeXryW_eA2XSW7MusyV7ukfnru-YHTTSUkmZBk-uKlIkOUc5_jMAwfECYQ3ABwuN6zsWvyMgzVOvDPUCtpD0hZT9yIu3lqJxwM5ZMYvJeHWKn3uiflMMzOuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت در ورزشگاه کیپ‌تاون با عبور خطرناک ۲ هواپیما از بالای سر تماشاگران
🔹
پرواز نمایشی دو هواپیمای «ایرلینک» پیش از مسابقه راگبی آفریقای جنوبی و نیوزیلند، تماشاگران ورزشگاه ۵۵ هزار نفری را ترساند.
🔹
یکی از هواپیماها در ارتفاع حدود ۵۰ متری نزدیک سقف ورزشگاه پرواز کرد، اما مسئولان اعلام کردند خطری برای برخورد وجود نداشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/685493" target="_blank">📅 10:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCuJ5XFD-4wtphN7pwT9RLS0XFV1T2tXLkvcWh8BTXetTQu9t1CMkHJxxheAls4rznM9aEnLJgX9XuV-5AWStyDCYcwLVfo_KiHnj4Ja1btgalpJr9F4D_bnXXYRaQzxOwqq84FNZEz1WyXO_0eBfB-hvbgorvHSi4u40bZqOEdeMkQYy3T1R6VzsOTxq5nyUUCF6KZbYoRJdwfqKjjj4p0HshXXFRscMFiwWNwlLnqzYF2z-iuotpXT6utrpKeksygRfUI121NiD7-Jd1CHSvx_CQYlTpttoLL1q1qUsOuPeCzhCIeWkUV0fqpjmE_mgr9m4Ckn25mPNDutuiCZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای دریافت و اهدای خون
🔹
دانستن سازگاری گروه‌های خونی در شرایط اورژانسی حیاتی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/685492" target="_blank">📅 10:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685491">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OSXvavIZ_eTYxHXcYt6jsutmDjnICa2s9WFyGKEuo5KYqvTMDlKmBNOCF1GkJdsGjDVTOcoKJmpQW85kz_c5yVTsZE3oBgdOz0wfBLvJHxTBsLvBR7zknwHvyxkoGiaO-MYbm6644GqV_rPdEpAP_DMCk4y6c0KUT77Sv0__iZVoYVP9Ln-eFb5VPnvecXuR0vEY6CRMfSRRaqRIIZH0NvQadTnYjZwiHG9lBAWO0mg25_tet4GHNSblUqdWoYPo_v9-kDWqrOokZAAdm40D5vvjBclcOl634KdoTSE5u0nFosy9A3UXDYCPdO2MVWi9yAuNX8yGZPe_lgQTsoU-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوسف پزشکیان: اگر غنی‌سازی نکنیم نمی‌میریم!
🔹
حیات ما به غنی‌سازی وابسته نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/685491" target="_blank">📅 10:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685490">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd0ac0aa2a.mp4?token=DhHNx-cZ9TE8P5V8f5VhcUTfytjo89EoyFipHaKUEgTgGYMqMzMpQZq7IiJqosfLjJ_88h8x6GCpNKOX9uMn1hQ7r-uuRaIpWvSn65Dkav68OZKerdmNA6rKhcwY4e9uZLe2t9leAVueuaCnac4t9ojFnO3pu2o0bIpzrB8tUlBWCPjZUTXFMJ5T9dvADVzDvWtprPDQL4nCLDZalcHVDVsA_THuZaImw6LxOqZo8wVxa6Wg2Ct8frDVcm6sneW_1Rg2uHUlxy5kDNgd3G3gC2CTmpyxdWDFgVLVFdqJuKfi6FTVop_xkb1TpFiVupIKYyKyPY2U-nsdIfiwqmyihA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd0ac0aa2a.mp4?token=DhHNx-cZ9TE8P5V8f5VhcUTfytjo89EoyFipHaKUEgTgGYMqMzMpQZq7IiJqosfLjJ_88h8x6GCpNKOX9uMn1hQ7r-uuRaIpWvSn65Dkav68OZKerdmNA6rKhcwY4e9uZLe2t9leAVueuaCnac4t9ojFnO3pu2o0bIpzrB8tUlBWCPjZUTXFMJ5T9dvADVzDvWtprPDQL4nCLDZalcHVDVsA_THuZaImw6LxOqZo8wVxa6Wg2Ct8frDVcm6sneW_1Rg2uHUlxy5kDNgd3G3gC2CTmpyxdWDFgVLVFdqJuKfi6FTVop_xkb1TpFiVupIKYyKyPY2U-nsdIfiwqmyihA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری هوایی از قله کلیمانجارو؛ بلندمرتبه ترین قله آفریقا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/685490" target="_blank">📅 10:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685487">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9394581bae.mp4?token=RG71K0rXz6c5FN6xVEBu4zNKhsc4A3AfrnvtZ4tepfaIrHe-TD1U08X3id7rkkhW0cNO50ZBWKzHIarJuowjbSJ18qOm5zd4wHEYQJdeWrivlM4K0CmVCirlD6fST0_E_QlvE9kwVdUpGlabBS5dIxGYoOYEN6uhYNfvpQ56cfEnuOjcMK7tMueefHfg08VM1KpAxolwfbvioNOUo1XSPnRUOgZWPFFprC_0nSeGYNqG8eax3gaGdSFeOOuaUC_IreMVvxt4l3DY9JOjVkOjXQNXJUoe40nEJwKYNHOWr0poUEPmoVLSDcWh_GaK-H3pg1VKlReFz0FwHjwc-uR8kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9394581bae.mp4?token=RG71K0rXz6c5FN6xVEBu4zNKhsc4A3AfrnvtZ4tepfaIrHe-TD1U08X3id7rkkhW0cNO50ZBWKzHIarJuowjbSJ18qOm5zd4wHEYQJdeWrivlM4K0CmVCirlD6fST0_E_QlvE9kwVdUpGlabBS5dIxGYoOYEN6uhYNfvpQ56cfEnuOjcMK7tMueefHfg08VM1KpAxolwfbvioNOUo1XSPnRUOgZWPFFprC_0nSeGYNqG8eax3gaGdSFeOOuaUC_IreMVvxt4l3DY9JOjVkOjXQNXJUoe40nEJwKYNHOWr0poUEPmoVLSDcWh_GaK-H3pg1VKlReFz0FwHjwc-uR8kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود سامانه بارشی به غرب و شمال غرب کشور و صدور هشدار نارنجی سازمان هواشناسی برای برخی نقاط
🔹
هوا در نیمه دوم هفته خنک می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/685487" target="_blank">📅 09:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685486">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c84f5d91.mp4?token=XNcOkz_cNdSw3pFvLUYHpLtU7jIHnHjgLd_EBLXlHOwuEUNtmCo8d4nR7yOmMieJ1wVSB7TyW64EuXYktpvwXm0X8zPgR7cqU3Bfvj16WQ_EEI691s9NHbVxI7HY24_WdoZwaPGiMufRJcwf5QVN-w-hjdh8NzqI7kjzaVoilDSJXf141YvcykX989l_xvHgtdtZWT1ciyeRQHHDGTnH_SS95Ll6KqRs7wIh9S1umlWfTp6Mjagnu7c-D0sAg54D5f-G1prw30Ix8DgHLKf6W8td8_Wgp9O79LTGSuJm6jR1l0VZ1seL3Rk1qkzjllZUDuZLCJoes4A8JYni3YtZVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c84f5d91.mp4?token=XNcOkz_cNdSw3pFvLUYHpLtU7jIHnHjgLd_EBLXlHOwuEUNtmCo8d4nR7yOmMieJ1wVSB7TyW64EuXYktpvwXm0X8zPgR7cqU3Bfvj16WQ_EEI691s9NHbVxI7HY24_WdoZwaPGiMufRJcwf5QVN-w-hjdh8NzqI7kjzaVoilDSJXf141YvcykX989l_xvHgtdtZWT1ciyeRQHHDGTnH_SS95Ll6KqRs7wIh9S1umlWfTp6Mjagnu7c-D0sAg54D5f-G1prw30Ix8DgHLKf6W8td8_Wgp9O79LTGSuJm6jR1l0VZ1seL3Rk1qkzjllZUDuZLCJoes4A8JYni3YtZVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
کارلسن: گزینه استفاده از سلاح هسته‌ای تاکتیکی علیه ایران در پنتاگون مطرح شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/685486" target="_blank">📅 09:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685485">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49cb916dca.mp4?token=YO2E2NVN-ACJe-5162wQ9VLXCgP_pwop5hFYjkMz_c8eBFqOcsLuIGyw50kjP3g80PpI1GRHo6W5wrTI2p5FV7Tz0VzCl4aRHuUXxbNjCluZK7C3Kybd-crAFBSiWHfBdYu8PNoMfT_hZ8NdZvEHzApgEvUKtvZPkbB4B42Mt_-ppxWijpSGxA0BjmNpUXQPjU59soAGIuTM0MHETvP-dq9pidG8yfZ3nibDnr-jvFUdR8MesTcm01Z9cg0YLkqA-uzgfZzTxb7xFAQu51o17i5BJ-4oEMzM0HsNnXC4GOObfI1pQIIqI-Y9-Q_nXe7Wvx1aEp6rX_1OUv5xFOfbxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49cb916dca.mp4?token=YO2E2NVN-ACJe-5162wQ9VLXCgP_pwop5hFYjkMz_c8eBFqOcsLuIGyw50kjP3g80PpI1GRHo6W5wrTI2p5FV7Tz0VzCl4aRHuUXxbNjCluZK7C3Kybd-crAFBSiWHfBdYu8PNoMfT_hZ8NdZvEHzApgEvUKtvZPkbB4B42Mt_-ppxWijpSGxA0BjmNpUXQPjU59soAGIuTM0MHETvP-dq9pidG8yfZ3nibDnr-jvFUdR8MesTcm01Z9cg0YLkqA-uzgfZzTxb7xFAQu51o17i5BJ-4oEMzM0HsNnXC4GOObfI1pQIIqI-Y9-Q_nXe7Wvx1aEp6rX_1OUv5xFOfbxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدوم امگا ۳ برای تو بهتره؟
🔹
منع مصرف امگا ۳: اگر داروی ضدانعقاد خون مصرف می‌کنید یا مبتلا به هموفیلی هستید، این مکمل مناسب شما نیست و یا حتما با پزشک مشورت کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/685485" target="_blank">📅 09:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685484">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_p9Eb8d-ebtBVEWflISiePe0WmzkSqltO-l_UibfbF2a3dvxCAB7xRlygGgkw5H5AfSxKoV9CMethMnYgo0_-YTIA7N5YHLAJmsUZmXIRhPadLAS4kj0Wf_QgCNIQDPgZPw_K0tyg5Ygryi4txomFyHNdnU1GEXmHCkbxUNpQbhdP1MjPL_Qv-zyLQgVYK6bq_aHoA9BXRfGVXSZwMz2ep1fQXXUOjiGr_O5DZana1acCs6EvjvCMxg6vq1kI0n-uzdvixGIBdZJAYi2DGFMuh4VBpIb9cVfqqJNnHOrB34AkuUjhcgzIRK6yRqqUAEa2GQZtpbO8cR2AW2qRTXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر انقلاب: حاکمان آمریکا و رژیم صهیونی، دشمن همۀ امت اسلامی و حتی حکام این کشورها هستند؛ بکار بردن تعابیر زشت آن‌ها نسبت به بعضی سران کشورهای منطقه در حافظه‌ها موجود است
🔹
حاکمان جنایتکار امریکا و نظام جعلی صهیونی دشمنان قسم خورده این اتّحاد و دوستی هستند.…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/685484" target="_blank">📅 09:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685483">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
اتّحاد، دفاع متقابل در مقابل کفر و همکاری مسلمانان؛ سه گام برای وصول به تمدّن نوین اسلامی
🔹
درس مهمّ اتّحاد و عدم تنازع، درس اوّل مکتب اسلام در مورد نوع مواجهه با دشمن و دوست است. امّا درس دوّم آن، دفاع از یکدیگر در مقابل کفر و درس سوّم، انواع همکاریها و…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/685483" target="_blank">📅 09:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685482">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
رهبر انقلاب: اگر مسلمانان متحد بودند، فلسطین این‌گونه بی‌پناه می‌ماند؟/ حکّام کشورهای منطقه دشمن واقعی را بشناسند و  با آن مقابله کنند/ اکنون وقت آن است که مسلمانان به فکر فرو روند و حوادث را دقیق‌تر بنگرند
🔹
آیا اگر مسلمین یدِ واحده‌ای می‌بودند که مشت خود…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/685482" target="_blank">📅 09:13 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
