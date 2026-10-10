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
<img src="https://cdn4.telesco.pe/file/Omc2RfyXRMwm9N40octplrz-Kw2cj_33NRvXDHtSamGlDKKVZABlPrDojgpsQZ1mSiVUqXfGIs9qH3yrpDNbRUwpHk0KrojK_rhAZb_ulF76Ck4F-YLyLpz0Ar1HEzLrFFHQ1gRd03GAmX8djScUnEiGbOSj9H40OIObOD1qefvA70SQZOCPQ_56ng77rC4taXuw_IVNoikEv0fMO7sU5a3LjQRZ4AV7tZiieLmxcruP6L3Uaja3-VX5JvUQkCcXpWV5ZFElCCfL57S8fe1BVZaeYpG3zSMYhMF9BEKtB5HTbJS4253CxY5dmquP4SCoAaKjp0GYXdjGSkJQBH67pg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-697220">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231f67b31e.mp4?token=V-K_2vVl8LS8N1v7N0ThkvByO1y92Wl_HP5mrqX721ax66T4P6yM7hRoip1UIsZmfiEOmDw9rW1vByKoqm922Ir0rscSuZ2cgv8va9bKIwRj7L-Ibr3JU-jUANr-ZVbf_dgQp-bArwy9dacFHeatW8Hh5AVX8kzIr4r2wo-UcJA40lo3dQZJ5EoDKLvClLsIt6vfp4dLmI-FFTNcDPF9VIK_vn5erU8FDWHi5zWFOwkpdmtbxXt1yh5tlv0HEYsTnLkKuiYpeQ5NoKecj8exLsuI4ZyFHYZ3alSmVy4lS-BFrXch00wJm5cAl8QO7D49YMD2rtMgiTCD3mBMCc6gow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231f67b31e.mp4?token=V-K_2vVl8LS8N1v7N0ThkvByO1y92Wl_HP5mrqX721ax66T4P6yM7hRoip1UIsZmfiEOmDw9rW1vByKoqm922Ir0rscSuZ2cgv8va9bKIwRj7L-Ibr3JU-jUANr-ZVbf_dgQp-bArwy9dacFHeatW8Hh5AVX8kzIr4r2wo-UcJA40lo3dQZJ5EoDKLvClLsIt6vfp4dLmI-FFTNcDPF9VIK_vn5erU8FDWHi5zWFOwkpdmtbxXt1yh5tlv0HEYsTnLkKuiYpeQ5NoKecj8exLsuI4ZyFHYZ3alSmVy4lS-BFrXch00wJm5cAl8QO7D49YMD2rtMgiTCD3mBMCc6gow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون
بارش شدید باران زنجان
⛈️
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/697220" target="_blank">📅 16:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697219">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
پنتاگون برای جبران کاهش ذخایر موشک‌های رهگیر در جنگ علیه ایران، قراردادی ۶.۳ میلیارد دلاری با شرکت ریتیون امضا کرد
🔹
بر اساس این قرارداد، ریتیون طی پنج سال موشک‌های رهگیر SM-3 Block IB را به‌صورت مستمر به وزارت دفاع آمریکا تحویل می‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/697219" target="_blank">📅 16:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697214">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZsFH4gIMYL3UxmYU62nSkJz33D3Kmr_dbzmC6--NcURpLyMFfs5kw_fFaf7Px8hsDnNBJatWC_8v0K748d4WDKC_ZVxQ86MuDBLBBTkppWwK6xfxmCf7oMooFmrdLMjF2hRowPzMzGhWY5Gvdc2btq2tDYQX4D4m7VcfsQ28HAaRjz-X3G3C7LZKHlt3DXhP7iNuK14s8FN84Osi0KWgRcwIEl4AZgiP48wPinef19fJww70GkjWlXzCiSoriMqwdCGV54u18c9QIxCD2bxatgPS1hTMvttRS0GGOxnuDo2C4oSQKcFQsHTK1bqmLylhNEhRAXywl-Ww1uf-wM0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mID3a5Fk5FvQVU3ldi7SXnpcO3qck5mlw-ajUsOv3VZ4t7hbxP52iw5tdxowUyz_nAOEoY7ZhWfcrbGem2EH4yCy7Aor5FM9Zmg47515cYR8bWEyiLY4x5NkkaY8cnCRXs9seAXr4GxVE0QwebTpnhg9aBzayhR_8AWaJDtafet4ThbiWvuA7FpV_rIzohN5K7WqFCGrzK7Z1OrN8cohQNVAu1z0Jrp9rxFe6nfsSR98KbLF-WgbSNOpEwL1SW93BanbYZ-IqeQdxl05HRqEXI1I7kCXIW7ty-x3BdfxVeUxIz_8NFL1v2W7vrJnzfhCM-arffktonqZL7JEFhoTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUx8_O4J9hjgw0Bj8T9LqkenKN0nFrqQmARlr9iLYuC4RPtj44VxsPQRLVSZN0D3uPAe7BzqF4A5eaHpPUZtF4N0f3mfSAEJvKzGr1p41X3E7LpBDic-sqaCRoF0owjX2wvNBiyH5Z14zxN1BwjfLUXx3JCOXTRhOEaolAL1u19zPeC08GJWZYcpDPB5uVNqXCuu7d_tt8mP-chxXuJvRRrY6SwB9yAwPvjFq_F18Ieliw81VjvbyD7SRYaOdAogLER8jPLjYChkHRVAw9XTpR_md6WhzTzw2CU64L5gxqI8RZyvqdHPJd_p_vtWIMXXWch47a3v25-4C5rkoI2ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFmLY9W2o5d81Ewvm6kobi_XKCDw2a6-IOLjV7P-zTEfYHarX4BKA44nOXt0GpOXE-DTjckdoXPHwQCGSDCnlVH7I7pWVuZ2a4ZsSQxhYcIm-8-obYDOi3AlNVXbAV0IwGazZrhCIPcMWVGg11S6sh7V2GCAObM0rf71nU3CeW_Y_aYDcuEjQ_-TCqwBfN6MlTPmP78R8P15jOghUg6wqRWRjOl40EWedl0TOdoxU0yKY4eTrM3QSulkKfVX8OO9C4Q6ekvF2sFaH3xKuQ60BcwaApuo7K5Fyo0pq1SEmaJh0K0pLOBwtiOVZun86-z_oLxMF1jVZHHELfwt3MuUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHrFRbn8MWEyXEyNV_kipNN1hYHHeh2n0ERmvA0CdD7sBhmJ9qVblj6ABmeuPoMraiatygfLxqS2qJBvfK3FgMzv-BmCm0ruHn5ovzVRqOz8YzvPcwoo7STtoOOi8eotSMr4dA2mtfYfa7Spkjol1Up0926fpCxpUIDYloiA_hoZ9EXERQoMFIHJ1Pr2JU_tix9HwtauynEz5bG9leyCE3d9wU4fjKQSFxNSqfXejx-B64u-4aEks1tBNfRObRbfRmECEnibalGAP8t5Y8QioyBXUDwg0K1OG_s3Gy0YpPEookrBRtnUWpOliRrdrnfUEGgsASUgeE3ZsiPG_k4_pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برای هر بیماری، چه تغذیه‌ای مناسب‌تره؟
🥗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/697214" target="_blank">📅 16:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697213">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
لطفعلی بخشی، کارشناس اقتصادی: تصمیمات جزیره‌ای، سیاست‌های ارزی بانک مرکزی را تضعیف می‌کند / سیاست ارزی زمانی نتیجه می‌دهد که هماهنگی میان دستگاه‌ها وجود داشته باشد
🔹
تصمیمات مربوط به تخصیص ارز نمی‌تواند صرفا بر اساس مسائل یک وزارتخانه گرفته شود و باید با سیاست‌های کلی دولت و شرایط اقتصادی کشور هماهنگ باشد.
🔹
وقتی برای تامین نیازهای ضروری کشور محدودیت ارزی وجود دارد، اختصاص ارز به کالاهای لوکس و گران‌قیمت نیازمند توجیه است.
🔹
سیاست ارزی زمانی می‌تواند نتیجه بدهد که میان دستگاه‌های مختلف هماهنگی وجود داشته باشد.
🔹
اگر وزارتخانه‌ای تصمیمی بگیرد که با سیاست‌های ارزی کشور در تضاد باشد، این موضوع نمی‌تواند صرفا در سطح همان وزارتخانه باقی بماند.
🔹
نیاز ارزی کشور فقط به یک بخش محدود نمی‌شود و اگر منابع موجود به یک مصرف جدید اختصاص پیدا کند، نیاز سایر بخش‌ها همچنان باقی خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/697213" target="_blank">📅 16:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697212">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
اعزام زائران عمره که قرار بود از نیمه مهر آغاز شود، به‌دلیل نهایی‌نشدن جداول پروازی و تخصیص‌نیافتن ارز زیارتی به تأخیر افتاده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/697212" target="_blank">📅 16:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697211">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL2a4sf8Ss4j8FBFqNYX1pyAYjRaHZzYygHCV_rcpIhPSEoySdDS9x5If8gNjxMqdofo2ZutQgrQ6wxTceOj5DruuZVl94Drcw3IG16uUKDpFQ8EgbaltiNQrStDaNJPyuhJk1mdEK0V36C0ogWqYtQXHnpo9wEcAotJefy3BrUNTxIjSASga_c0sDUxUqG7CtX0TbFLfAF9JYH7mpl83ok7dqclcHg8XtvuqcTMONVADR82j1e4nqj7X6yd17ZLStePc7q7ssRkjO7f34n3UxUWnSGYK-1lE3CAtvH5sIiNfNqDKyZyqytz1be9Is3tkscyug52ddrPg7HKjd2QWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم اکنون؛ رنگین کمان در آسمان اراک
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/697211" target="_blank">📅 15:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697209">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
واکنش ولی نصر، مشاور سابق اوباما به توافق واشنگتن درباره گازوئیل روسیه:  آمریکا تصمیم گرفته برای ادامه جنگ با ایران، هدف مشترک خود و اروپا در قبال اوکراین را قربانی کند
🔹
این استدلال که ایران دشمن تمدنی غرب است، نمی‌تواند شکاف عمیق میان ایالات متحده و اروپا را بپوشاند/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/697209" target="_blank">📅 15:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/503f0a9d2e.mp4?token=pw6sh9gm7TW4buyfJAeaz8ZiA5tRYflQS6pU_xQW4NPH-hlrmgNOkqmxOh5KaC5XeWu05Oqlp0OZ5mFEGC8IIhYhczAbeWKRIQqZczmS2mA7osfqyGMSQj7QiP7GUBmxNYSZlJMxp5RZOPpK83kGB7kzPCG2FZ_2R_eZFVSmNEhN4PYxgAWT0EwcrPjFX7aCPY3cY_iTY4d_YjGjbA5TiZgBWXsrPX24o4bquuVdktGttzbXvLfwZ3cQrthHeOOhGWhs6k24pEN0LZq5MN90qehlsANSlheVRRSUBOsSvRW3o4ovEifGwwnPIrRDXh4g1SVh3oNR66vh9EQkBfNZhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/503f0a9d2e.mp4?token=pw6sh9gm7TW4buyfJAeaz8ZiA5tRYflQS6pU_xQW4NPH-hlrmgNOkqmxOh5KaC5XeWu05Oqlp0OZ5mFEGC8IIhYhczAbeWKRIQqZczmS2mA7osfqyGMSQj7QiP7GUBmxNYSZlJMxp5RZOPpK83kGB7kzPCG2FZ_2R_eZFVSmNEhN4PYxgAWT0EwcrPjFX7aCPY3cY_iTY4d_YjGjbA5TiZgBWXsrPX24o4bquuVdktGttzbXvLfwZ3cQrthHeOOhGWhs6k24pEN0LZq5MN90qehlsANSlheVRRSUBOsSvRW3o4ovEifGwwnPIrRDXh4g1SVh3oNR66vh9EQkBfNZhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بعضی وقت‌ها رگ‌های دستمون برجسته می‌شن؟ #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/697208" target="_blank">📅 15:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697207">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngWZ-jp0TdXNpsiR01uPp2fTqJ7ONUxZXgMV-4izXUa0PqAhCt0Uj435P8rqKtBD2Hp-6zcHSXlPMnrmbk5yXF2QsvFD5xOPOowuWhKvl7Tn3vr6f6hDNfjc_Xe4QF2zFD3u-UJeXMRv_oQIy7Jd6P70HBMr4eHBIZcJl7UVxAmES5vt-OF1o8yk40khOmhMpwUJtmA6jfdTzvlYjZoIhiJqld_iv6v7QaV3dWFiqPs9A47E8hACzhIlXcyGR439vm2tTK3E_d3qXtG_DOQ3Xf1cjMmkby-o9ScqKuwus9urnZZnPTBSIPsLBbdeCl2eYYS83v0dhTs3PkgcbJ1LSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ سفارت ایران در بوسنی به اظهارات روبیو: آفتابه ایرانی ده برابر کشور تو عمر دارد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/697207" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697206">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رئیس سازمان هدفمندسازی یارانه‌ها: یارانه نقدی تا پایان سال بدون تأخیر پرداخت خواهد‌ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/697206" target="_blank">📅 15:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697205">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ظریف: آمریکا من را به‌دلیل حمایت از رهبر شهید انقلاب و نیروی قدس تحریم کرده است؛ سخنرانی اخیر بازتاب‌یافته نیز مربوط به دو سال پیش است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/697205" target="_blank">📅 15:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697204">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmxckMRNZM7EcEccjo-Ey2qB9b26yFx085EMVGufHQsIq3RVRYfBnQp8rPGRhUICmLHtyxg4XsqjZO9hec10FGELSgEjhhorc4D0CSRQlHDxivVttZmdFwtDGuPW2Uh0mi4wJ1aLvZFyOKzzyAb-FZIaVb9w9SFqcrL90M0ml0vc1IkaQBzDTGAL7ZHI1p3IQlacLup-7O2L9Sey7k8KYrXlmCqcfobTvIPSQO6I8LuS_qQMkt4jMxFIo3oSsojoRY3JESmWzdxqGfUWBZT8O6P0MtvwsRehFh_jyRaHswgJgachUCitCtGjQnmhjSyJXVfvTO20KPKHIGLj-xztRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی طاعون مسکو را به شورش کشاند | از شایعات امروز درباره طاعون در روسیه تا همه‌گیری مرگبار عصر کاترین کبیر
🔹
این روزها انتشار خبرهایی درباره احتمال ابتلا به طاعون در روسیه و گمانه‌زنی‌ها درباره منشأ یک بیماری مرموز، بار دیگر نام این بیماری باستانی را به صدر اخبار بازگردانده است.
گزارش تاریخی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3251315</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/697204" target="_blank">📅 15:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697203">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgHVrT2k_l3kaJKXYc2zs_Mzr3wD2khDIoE-wv7v73ZEMAk5FnrB1-3vApgQyfiYHrByjp3n5uMD5ql8Gfo5n-qFs7co0FP8Ldo5lfpgEeAdMMLzl-Mu9j5tt52Dbz42hp2VW87NcsuZaIIq5ju0xGE8RTBT7ojHHZj-qz7XzsLUpI5iec_WrYeANqmsw9ljBjR450qeAp5a41JkajdHqnG4quPhcuAmPkYN-cwl-2RzkIeE8bl7XSv-zf9iLOfn9PkI1rbew-uCoECknCzT9PGxIF6eefOkLMJf0Wm7SXe8mqaK5VWo7ncfVJCt41iSPh8kdJ8XJf0uJqbi_WKNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
می‌دونستین یه ابر کومولونیمبوس میتونه ۱ میلیون کیلو وزن داشته باشه، یعنی بیشتر از وزن هزار تا پراید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/697203" target="_blank">📅 15:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697202">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAvdEajSAXHqSRoc1Am3znDT6iiOHGunaJCddr-NviywCb2LRQHLgC7zwgbxl_jqAPJPNnlz3IdYuS_LwKUSENMofOF6_E9B9jLfCBtVLtE5Wwl2DdOODoNShX1ViBCozrgvBZxCuNOFUmha2-gAt6O1xgRFUpDGB5dSBmwmv29rOY6tjWnAy8pPyVtv0Wt1kMbPCnq8ggwqD9lPQwHIQhn2HR7ttJ-K0NWTNkuo59ReRAnbquJsnjfCd9ET0OUS0D9m514SowoZyPQMm7y-IZZ0ncH6WvJzjGd6IzPkGvTj8V5dOAogYnYEe47CS80VBq4gw5SJxI4xSaz5jPXS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جباری برون، داوطلب برنامه مستربیست که در یک چالش بزرگ یک هواپیمای شخصی به قیمت ۲.۴ میلیون دلار برنده شده بود
🔹
سه هفته بعد از این اتفاق در فرودگاه بین‌المللی کشور پاراگوئه به همراه ۲۶۲ کیلوگرم مواد مخدر دستگیر شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/697202" target="_blank">📅 15:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697201">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b97db5a1cf.mp4?token=KxFnTEwnbHdCwYPkJdHwIzi-TpxmYz_D9aV6cAjcN13UI5jOUhovC6XSCC0AeWF-hnaT3Nc71o2i0CS0UycjqC1bognBzMmjGemGBRg2nziWfZawX6lZtxhVx33dPhAnnRLuBMlf_mXl3-NriitQ0cnFAIyv36fGeCsd9ErYhCtfAkU_JVpEzk8sIEv5-G49FV4ia8-ZUSw7dKVRI8Auaxj3Tyw_o5-kvX380sdr_SyMJERhB_IAOo5ULzYzyVP8heVE2GbfXPiEWCdEJXlN2zoxBUtgxDDXVRyZHDE2AvXftrsKENKpj-F__mRf8SOVDv4D12J1e9kThzHHcoNk2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b97db5a1cf.mp4?token=KxFnTEwnbHdCwYPkJdHwIzi-TpxmYz_D9aV6cAjcN13UI5jOUhovC6XSCC0AeWF-hnaT3Nc71o2i0CS0UycjqC1bognBzMmjGemGBRg2nziWfZawX6lZtxhVx33dPhAnnRLuBMlf_mXl3-NriitQ0cnFAIyv36fGeCsd9ErYhCtfAkU_JVpEzk8sIEv5-G49FV4ia8-ZUSw7dKVRI8Auaxj3Tyw_o5-kvX380sdr_SyMJERhB_IAOo5ULzYzyVP8heVE2GbfXPiEWCdEJXlN2zoxBUtgxDDXVRyZHDE2AvXftrsKENKpj-F__mRf8SOVDv4D12J1e9kThzHHcoNk2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژست نشستن این گوسفند سوژه فضای مجازی شد؛ انگار اومده یه دورهمی خودمونی!
😄
🐑
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/697201" target="_blank">📅 15:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697200">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVBbYyuA10P8shFuioy2gEzxZkBSq-r3g2XHTa0Xl__yujO4CepjnNn7zWn7ZFGZpeZUKZ5wQ4r4ImzBbVp-2w6VvYUwg-ro2OEmhAMO8xKjXDNAlWPXvMXod_gOGlSMU6XnjlDly69xR9T3KS2LRoDaeAV3Ktt-raHI_uakvAo0mNvFH-0WsiBpSZ07feH_gKewQ2MbruiaIwN4spZrc03mosGlUlYw7u1FydaY9_P1uy7cKaOFqJ0UgMtkyGyh6o8p_26zLfeojVJ4E3nIKw90OWFTspr86BR5SaMcDs24gL8I6LubtRlF0XPGhCxKgA5GPf6yeyBaYMWoUQz62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: سناتورهای آمریکایی خواهان خروج از مهلکه‌ شکست‌های فاجعه بار هستند
وزیر امور خارجه:
🔹
نتانیاهو یک جنایتکار جنگیِ تحت تعقیب است که دستش به خون اعراب، آمریکایی‌ها و ایرانیان آلوده است. او برای فرار از عدالت، هیچ ارزشی برای مردم خود قائل نیست.
🔹
او همچون قماربازی ورشکسته، ناامیدانه تلاش می کند با قربانی کردن هر چه بیشتر جان و مال آمریکایی‌ها خود را نجات دهد. حتی سناتورهای آمریکایی نیز خواهان پیدا کردن راهی برای خروج هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/697200" target="_blank">📅 15:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697198">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ظریف: آمریکا من را به‌دلیل حمایت از رهبر شهید انقلاب و نیروی قدس تحریم کرده است؛ سخنرانی اخیر بازتاب‌یافته نیز مربوط به دو سال پیش است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/697198" target="_blank">📅 15:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697197">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OByJpXm51bzSTz7rEhnK06LrYbV5cs7onC5vlwHoyh9FNBR0HqYe4ZSwu7IkZwdmy9lig-uty7FD3-PJktRJGAeqzv2ZUlpgxiJevJcz79_6psHvIeH3Gd73uPQe8Ni6l1wk5rbayuiqhzUzC7afFhl26oStJJoGinni5d2iN_H-cCyYbaPHtgEOFVqgLiawFLTYSu4RrxftrG9lUf3hAgmJJCiIM7jDybUsF-4_aSU50qoAfXxxtiS_Ov0oNhj9c4betAMcP87HGcA3Gt3-gmYXqu6-l38QwRSO0tuuPQlYm_qmwlN0cK-13wFmDo5wHMgUm1vsSdOOQKsHMWyxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تنهایی نتانیاهو در سازمان ملل برروی دیوارنگاره میدان انقلاب تهران
🔸
جدیدترین طرح دیوارنگاره میدان انقلاب تهران به مناسبت سالگرد عملیات طوفان‌الاقصی  با شعار " روز به روز منزوی‌تر" با موضوع پیامدهای جهانی و انزوای رژیم صهیونیستی اکران شد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/697197" target="_blank">📅 15:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697196">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d702b7e656.mp4?token=VS43bHUwnyzhks2H8rzdGH2KKZiVZHkdKXqY_XndobyAhnPrd8VH9_eGSv-gxDPufvfivn_EWsDuIg1S47ggBXZVJ5e-swI7SDPkk6-nMiF0TKtwlz6cRES6P0xHdT5RvuafofBiv6bzRLpbNprD4UUfTC6RjNba_B7aX_5uniiZuCK-FGqCflmwBNfjqJumV1JI-N6IszLZ9hIGPAGjAa-bt5Ffi92KPje0XsNXy4jxIzfCwe-sHfH5McAHN23oz3I85hHWN1wrxlp0Qrkky275MCHVA1IAt_Tdsn0l33UI2NZme2LGQ6trFDEsOTzpH160zsTgSAn9sFrrFiCUhzbzMvqeaGCVGsNSTQevrmd2krf80RCoEpUIl-GxjL5ORaOAMjGsOpJ9V-90BIp62nL5XpiBvb6aWajgjSs9vUjr-xbPuUl8ZPzR7dvIhPmNTkEMs91JEUxlkKrxwj91ufp1-bj9c0Ja8EwbeOC-sByZFqiwQXxXom1soMXb5fujcwD6QmrFw-2kKx45U69TrdPlfR2oRPgDKyBgu0g1TVkWOR2Weyqxbq4Nzik6wwfcMjbr9DtEdP8xG6MFd3d4nvb5rrqlSu9DnftIgOkc06MtZVT-OwUqc1qcCBNymTpWm-zLc5LwC2Ioeum5wPO99SC35WolkuEwQ-XogbDT3Nk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d702b7e656.mp4?token=VS43bHUwnyzhks2H8rzdGH2KKZiVZHkdKXqY_XndobyAhnPrd8VH9_eGSv-gxDPufvfivn_EWsDuIg1S47ggBXZVJ5e-swI7SDPkk6-nMiF0TKtwlz6cRES6P0xHdT5RvuafofBiv6bzRLpbNprD4UUfTC6RjNba_B7aX_5uniiZuCK-FGqCflmwBNfjqJumV1JI-N6IszLZ9hIGPAGjAa-bt5Ffi92KPje0XsNXy4jxIzfCwe-sHfH5McAHN23oz3I85hHWN1wrxlp0Qrkky275MCHVA1IAt_Tdsn0l33UI2NZme2LGQ6trFDEsOTzpH160zsTgSAn9sFrrFiCUhzbzMvqeaGCVGsNSTQevrmd2krf80RCoEpUIl-GxjL5ORaOAMjGsOpJ9V-90BIp62nL5XpiBvb6aWajgjSs9vUjr-xbPuUl8ZPzR7dvIhPmNTkEMs91JEUxlkKrxwj91ufp1-bj9c0Ja8EwbeOC-sByZFqiwQXxXom1soMXb5fujcwD6QmrFw-2kKx45U69TrdPlfR2oRPgDKyBgu0g1TVkWOR2Weyqxbq4Nzik6wwfcMjbr9DtEdP8xG6MFd3d4nvb5rrqlSu9DnftIgOkc06MtZVT-OwUqc1qcCBNymTpWm-zLc5LwC2Ioeum5wPO99SC35WolkuEwQ-XogbDT3Nk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍂
💦
جشنواره پاییزی سرزمین موج‌های آبی مشهد آغاز شد!
🔥
هیجان بی‌نظیر، تخفیف‌های باورنکردنی !
🎢
بیش از ۶۱ سرسره جذاب و هیجان‌انگیز
💦
دو مجموعه مجزا ویژه آقایان و بانوان
🎒
تخفیف ویژه گروه‌های دانش‌آموزی
🏢
امکان عقد قرارداد با سازمان‌ها، شرکت‌ها و ارگان‌های دولتی و خصوصی
🔥
فرصت استفاده از تخفیف‌های ویژه رو از دست ندید!
📍
آدرس مجموعه‌ها:
👩
مجموعه بانوان: مشهد، اندیشه ۷۹
👨
مجموعه آقایان: مشهد، بین اندیشه  ۸۳
🎟
خرید بلیت و اطلاعات بیشتر:
🌐
wwl.ir
📞
05136008
جشنواره های تخفیفی ما رو در کانال زیر دنبال کنید:
https://t.me/wwlpark_ir
🌊
سرزمین موجهای آبی مشهد ؛ پاییز پر از هیجان!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/697196" target="_blank">📅 15:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697195">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
رئیس بنیاد مسکن انقلاب اسلامی: سقف وام مسکن روستایی به یک میلیارد و ۱۰۰ میلیون تومان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/697195" target="_blank">📅 14:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697190">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eubod0mqRlLBHyXADlrqgMU-u0m7nnWIssYpR4yMS0rFUjh6u4hRf0GGNikwZBtmvOBFh_PR_OjYXNxYqOMRnpcF-lmxSdNMk0NSmeW5lIg0sc2qbgfCRdFE8fJkVS9wHacahNGX9aT26jfwblNsBAzE7ImBLgi7wUtB6rmkSDAZZKf2NI7QmHtml3TxVgF0I_a-PlAyFfFB7YijfrjugSkhMKoIfLC4Qs09r5E9iIwLNTnzYIG37-GYgfnR-IaeQrRI-PbcK7Oio-QNflwl309t8P0dLDPiY3OxyuU1jLaP-N6JOgRr2J5hgK6K5v5lEAUYkcpRtqc71E9tqWO-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YGn6o19u_2KeVtEz0D_7JtK1TYO2G7W8NJQ-opOqZ-eVgvuUx95ZUCR6BW04WH783TpOnW9o--VDZOFpzvQ8nqAIZ5SIHA1V2-FnsIPIpzJshsp-0G_h4BnOEnVxVyxvzSPffJa_GznqaCzFoSBmeKUl6ohYTjuR5MZa5XczPF6rMBadZY91HKODwwGqRZqeM-55MMgaxT1pZQ6rCB_GJNLdGBfGjxGmyA66z2aEZobK2gg_M-YaOEqTuPYTQ9YUeWkjLrdPrSRWVBQ2h3S-M8jU1CN59oW5uWXf0j3W6w7glO_TLKBFIz0HEdx845IsiDKD_Gw7OgfeNRs9D6mY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M64QsW2DcwS5FpGcWAupO_7rU2D0tEQ3MwElxo7RABquSrFr_eplFX7IRx1aJNaY450Q-e1DqxZssD_y0azHx5_S0gP1WI7YS8WDas8UZE2f50pOmV2-WClfXolg1CDo72XO3KKAHn3YmrQlLLx0xdNF4htM4aaUJmFkdHWeZBP1TZlGhh39RR5DZtQYBroZTGAkTbhdQzX3vB2QagQTqD6uFqUUXEYnT7QtaTnzPlAWL1_wXNSm4QrpvpYQ3zZfDY4oWyZGAJS-fCiJ-dCCf-50ro-kwRf1C5lPsQC3Xps0n99hKYKubmwQMuosghW_jgvTWkq7d6ifi2Qr4stIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JouwhaPya6_wy3Qj3DO2tpOE1uOFfRIoQWvmvjLwwR9eRfu4HDOjh4YEhMxy4ITp2ni48fS3JYYLH6rd6QWp5f1iyBHCSMT6tk3zI94VEnPok6NvKK4A69tR9Mdnkpl5DGaMj6JkVpCVpQEeKTTBmYFeK5-4bb8-VpBtxfoZc3gVsuoajd2Yzz9DqAfMdlKIYQwnKY3_12LGvgMYEPkMKA42wownJk_3SYuHjjDHMHSUfZujv3AlqnCYk53AjGiFhXlS589_5y9cSXwPE-XxBVp2YF6vaKipQzIqW5QGbA1Een-PAwE6140rxm8M7GEh3v4XmKSRjCiLgXUYL1Myfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRIc1ARuyH4DgLXnlTbKvRTYrUgOtF0f1LyXl8bW0BXMO_RotXOi7_8qlwsFfUmG-be-jPmcD2rP5U16DWG2GzLW5DnyKsFFqjcE9Lnv6XizgDO3UBassm7u5_IS2wAmZIik3RBfmhJ3tsr0f8RFYXDAaXd6Z1-_n5SyrDHqgCgwTaSddmKdg2iuSfHB-3PFdQLW_XvUJJ2fuGxAro8RRYkZkSNevsu77jh-lMank4BZ2cxllNyPJmkIKYp5dMvqzDwR3BG2TwzzLsBwHmlDQw0jfWQQH8jI5dgNMCqe_62H7TrSvtq7UbJ7LUWDjwX38eiRoQZ6DlvdaSRf1ETVzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طبیعت گاهی آن‌قدر هنرمندانه تقلید می‌کنه که چشم‌هات باورش نمی‌شه!
🦜
🦋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/697190" target="_blank">📅 14:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697187">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOFDxPnyULI9K2rOqrRH8fWrOPE2s8M2AhaJgQGUJAVgEnmxwMe-FEqREjcT7moQG-1RqWVbniPMP0Ud1fGuQ87z5fPEZfjwWhqyZjOWwc1ZZvgAmHKzeozWsVjLAZnV0t1echlMApNh19fZoN5ZnX89XDfsMaUW5909l6CmzaXWxkvaFnOc0J0yZXTgv2JMqnvBlfqe6MbxmXF4B-L_O4jq6YhC3oKsNTRL9CsdaEHVTBbIWXzCRSsU9lNTMY0puO5ZCye40M_mQ0pwhWwUUSwustagOvd79PmZjTMEi4odXg-imwA83yL_obWCATQX1kyM6X_Y81J8RqzFNT0wcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبدالملک رهبر یمن: از آغاز تاریخ عربستان سعودی تا امروز، شمشیر نقش‌بسته بر پرچم این کشور هیچ‌گاه جز علیه مسلمانان به کار گرفته نشده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/697187" target="_blank">📅 14:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697185">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a20ea3297f.mp4?token=tglDIMKqUILbPhRh__HvqRx07jcZoDLUdrtTwZeXMsvBqBGV-FjXdhrwsc4WS4hnHiRaOJcfKmunSDhvjk9lwnwZ1Yga73qz5bmnJWftVPVNz3LWE3M6dVofCav7pvhMyX6I1bm-FUOY6OQnNf9PnX7ckwbCLE76o9xZynvm_MEqXovsa4tOqFatIpH6Mlv1n8Q-nU8N0zLRkzLo-eElIN8Kwlach1tTbfolrNuH3aWVl2zBriiac5mOTKT8q4IFmpeEieAIJVFNMr24OT-kkm2Bbj604nxInWU7Pw844Cg2ywq3Kmd2fXvMbpx0WslTkZFUi96OyUOZlJx9hjRL8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a20ea3297f.mp4?token=tglDIMKqUILbPhRh__HvqRx07jcZoDLUdrtTwZeXMsvBqBGV-FjXdhrwsc4WS4hnHiRaOJcfKmunSDhvjk9lwnwZ1Yga73qz5bmnJWftVPVNz3LWE3M6dVofCav7pvhMyX6I1bm-FUOY6OQnNf9PnX7ckwbCLE76o9xZynvm_MEqXovsa4tOqFatIpH6Mlv1n8Q-nU8N0zLRkzLo-eElIN8Kwlach1tTbfolrNuH3aWVl2zBriiac5mOTKT8q4IFmpeEieAIJVFNMr24OT-kkm2Bbj604nxInWU7Pw844Cg2ywq3Kmd2fXvMbpx0WslTkZFUi96OyUOZlJx9hjRL8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای همچنین نشان می‌دهند که از مجتمع گاز الحوية در میدان الغوار عربستان سعودی نیز دود بلند می‌شود، این بدان معناست که اکنون با موارد زیر روبه‌رو هستیم
:
🔹
آتش‌سوزی در مجتمع گاز شدقم (احتمال استهداف)
🔹
آتش‌سوزی در مجتمع گاز الحوية ( اصابت قطعی نیست)
🔹
آتش‌سوزی در حقل الشيبة (اصابت قطعی نیست)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/697185" target="_blank">📅 14:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697183">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
آموزش و پرورش مجازی شدن مدارس از ۱۵ آبان را تکذیب کرد  مصطفی آذرکیش، معاون آموزش متوسطه وزارت آموزش و پرورش در #گفتگو با خبرفوری:
🔹
درحال‌حاضر هیچ بحثی درباره تعطیلی یا مجازی‌شدن مدارس از تاریخ مشخصی مانند ۱۵ آبان مطرح نیست و برنامه‌های آموزش و پرورش بر آموزش…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/697183" target="_blank">📅 13:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697182">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34a6ca658.mp4?token=MxVSNIxzSO5uCp3KqXr6I1i9Fkjx2MAktcdxekK1hHLm9laC4QlhRd60ae5Mz9kLddW8aS_zHM2SJN6BklNq4UfJdk7Umh8wnfxPHLilCCLsdoRRVlHlAmfwn2z2GIXEgh_di6lkxetUV75oFCh6E2OhLd9wSM9mR05PrnQR3Nk8-RefhTZk_N4rkIgTejG9E-xNUifKYy71Jk7X5RS-3DR_7Fok0GcZrOTQDfxuxAqq0-wGI25gWgR7C63f3IVtEQQUFydf2c3dH7z3O44--fjEBADaWHNgDuJkl8_RcO75x5YbGJIOOiF2FVh7uthzwfuKBXdjYkgUbBB1jhr7cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34a6ca658.mp4?token=MxVSNIxzSO5uCp3KqXr6I1i9Fkjx2MAktcdxekK1hHLm9laC4QlhRd60ae5Mz9kLddW8aS_zHM2SJN6BklNq4UfJdk7Umh8wnfxPHLilCCLsdoRRVlHlAmfwn2z2GIXEgh_di6lkxetUV75oFCh6E2OhLd9wSM9mR05PrnQR3Nk8-RefhTZk_N4rkIgTejG9E-xNUifKYy71Jk7X5RS-3DR_7Fok0GcZrOTQDfxuxAqq0-wGI25gWgR7C63f3IVtEQQUFydf2c3dH7z3O44--fjEBADaWHNgDuJkl8_RcO75x5YbGJIOOiF2FVh7uthzwfuKBXdjYkgUbBB1jhr7cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌ها و پهپادهای یمنی به قلب ثروت نفتی عربستان رسید
🔹
منابع عربی از حملات ارتش یمن به منطقه الشرقیه که ثروت نفتی عربستان را در خود جای داده و دهها چاه و پالایشگاه نفت و گاز در آن قرار دارد، خبر می‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/697182" target="_blank">📅 13:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697181">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt9HNMcHAIR79SpKkHBijbfuMDPPnugHspqKmmv9RJ_UmRkj22qL9IQaEmQMWhdy1cYjMMEHE3t2oTGa_HAnJPzG_RjTPYbOUBcG8aS0S1NLDdaGOMQ79_Y3JDrDhzjslzNPriIStN1Jwd0iVv_ScojlQBCuTeACLcdYfXj_Y0lFFXM3cxZLMKFfK8778CPPqwVkc4i7U_6jDO_qd8XhYvApFoNSyFw7v0JtCsx-P8eN43S6mbcqN20dyEDaO_7Hc2H2boY-4No7FMLvzsHD9gj4Plxa5BcTilbCtfr0-PU4CMaC6dRkKumyD8q2zj-cjkzbRdRhDFY-h3lTgHH6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ، کیتی زکریا را به‌ عنوان جانشین کارولین لیویت در سمت سخنگوی کاخ سفید انتخاب کرد
🔹
نکته جالب درباره این خانم اینکه پدر پدربزرگش ایرانی بوده و به ایتالیا مهاجرت کرده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/697181" target="_blank">📅 13:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697180">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سردار رویانیان: بی‌حجابی اگر از حد بگذرد فساد ایجاد می‌کند اما نمیشه دخترها رو به زور باحجاب کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/697180" target="_blank">📅 13:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697179">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31974bb27d.mp4?token=cJnj6XgOqcClSnz55TA2AHAHAYXFiiKuQiK-z_17jzjE2GiB8St5MHK4SXw0bDrhSgXrAmexgEmrwBVg4GTEH-sZ7EP4j0tVwGPpQP4hrdjWjfJDs1ksBDO_tzH2rzjS6AhyRWp_1b9bwBh1gVIN5Eq664gpxCypdEWtI_lgtVPauVpAHIwH6bA7pEceXJuUPdF7xqNxCEZV1TgQVorUcRj6k-8VfwjmMxReVjSPrc25D3DlXX38YXeCk1qYCKXMne2lX_TXyq68qBEz1V_grGPw7itTYf1QYLcxLSBuAKhvA-pHdUnFo4yrLQugsomkclCgplcAqAfOVY1DzthPtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31974bb27d.mp4?token=cJnj6XgOqcClSnz55TA2AHAHAYXFiiKuQiK-z_17jzjE2GiB8St5MHK4SXw0bDrhSgXrAmexgEmrwBVg4GTEH-sZ7EP4j0tVwGPpQP4hrdjWjfJDs1ksBDO_tzH2rzjS6AhyRWp_1b9bwBh1gVIN5Eq664gpxCypdEWtI_lgtVPauVpAHIwH6bA7pEceXJuUPdF7xqNxCEZV1TgQVorUcRj6k-8VfwjmMxReVjSPrc25D3DlXX38YXeCk1qYCKXMne2lX_TXyq68qBEz1V_grGPw7itTYf1QYLcxLSBuAKhvA-pHdUnFo4yrLQugsomkclCgplcAqAfOVY1DzthPtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاییز شیرگاه، مازندران
🍂
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/697179" target="_blank">📅 13:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697178">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWcxJrml_Y61Atuj5vPcl1W0yBjr0IpazWq8XmlGCweyPlNlpoBIgXCMsxIR1Inj6Ej7RP4UfQfiCwQpOvzAvIsCPMmCVeZMHHKEW_CQXrqEWHBXCiMWGXTRSRMUCjpo6zFtW67hqYd-TxdIH8dTsnKLlbAY_rcRsoKKLP1k5CR9_iID9OM94sdexNETqkzUT78apOdcB3oZ7yHbdzkCnbSpCaWhdZBKhFbdsbvRkX7CsNlWkUpabRmYDFN3_yTT76klLHugF4FdjhwR6n54m0fCA-ysm2AKqtRgcfHffrmMnSdMF8PrqknNdQcDB1P7JeDvhtukNLdMkQWDBQaraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
«اگر کارخانه دارید، قبل از اینکه برای سایت، محتوا یا تبلیغات هزینه کنید، اول باید مشخص شود مسئله واقعی کجاست.»
🔹
با یک جلسه‌ی کوتاه ما می‌توانیم بررسی کنیم :
حضور دیجیتال فعلی
مسیر جذب لید
ابزارهای فروش
سایت و محتوا
اولویت واقعی برای رشد»
رزرو جلسه شناخت و مشاوره دیجیتال
https://digitalcast.agency/consultation-landing/</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/697178" target="_blank">📅 13:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697177">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw74LjBZKMA7xjOmyY4iS3yM6jewcjIhBwHkdlVX2odwHkV5A5jpVaHBorxcQYHKS36URgzk07Mm61rxAPhGpkL5WMIGzmN0L3tlhoa6txBWFaQg9psS9lDVJb-BlDd-ehjsX6_QbCWuLlgmDY01AN35vx-x3X7BvoURmpJN_O6_nneMmQgzGPSq0faO65RvJUZN7QAbH8EGetRpmedEs4BtiNWqgdAhBttlfjMWXxKxI41mZiPWhU38K5qauIgkFEoIJymhk3O2mi7Ab6dUxPProPWjwbi4wDThL4YbQ1rAZwvfmvu7dOFdgJFXhEd5BHV1MSJadzmZoGcS4igzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر پربازدید از اعتراضات دانش آموزی در فرانسه
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/697177" target="_blank">📅 13:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697176">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89eb24a75c.mp4?token=rmZVALsfBZ1panFdXNI2o6gL8hD1foPavLBlbriym99IBuTnEpx1Rtoo33ic4n5DWUUh6rN2cp0LdmTmH1UX5HTMlcgOCdlKLpgWo7MWSs8AE3fSvk67hxOzCqQiOBvgV999c_tkZPaP0ghvI3IOhUttdOS8PQTXfCHPyHKb0BpTBF2zK_cnGRIrt34Ni2y5bZ5ac4_yh6SYcSMu0e9yXYEUmAecKnWPewbRHZZtAbrjfMrmii0dgEziZVhPmqpYdMaEikLev9akoCsJBTzW5o9Il5-yjm6hP8-4BVxMSqb67dQu8KWheFv3lAJIisOvf2D_f7b7kkrUQ1qnH-wdcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89eb24a75c.mp4?token=rmZVALsfBZ1panFdXNI2o6gL8hD1foPavLBlbriym99IBuTnEpx1Rtoo33ic4n5DWUUh6rN2cp0LdmTmH1UX5HTMlcgOCdlKLpgWo7MWSs8AE3fSvk67hxOzCqQiOBvgV999c_tkZPaP0ghvI3IOhUttdOS8PQTXfCHPyHKb0BpTBF2zK_cnGRIrt34Ni2y5bZ5ac4_yh6SYcSMu0e9yXYEUmAecKnWPewbRHZZtAbrjfMrmii0dgEziZVhPmqpYdMaEikLev9akoCsJBTzW5o9Il5-yjm6hP8-4BVxMSqb67dQu8KWheFv3lAJIisOvf2D_f7b7kkrUQ1qnH-wdcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دهان باز کردن جاده‌ها در پی زلزله ۷.۷ ریشتری جنوب پاناما
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/697176" target="_blank">📅 13:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697175">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCfcYQIOBAJSc8CBl1dP-2Y8VhTIGn8bKaVMOf3GMsg45K6YuiRixG1adBL6z9Ch4PtH6bOXMx53jWqUwZ-3UJZlXW2avPfsq3Q6uisFm_GXkjESJHhQP9OcpcAMQcyq7wBKRTx-F1fXHYTDFEZMbD8bppSGwcmfbQL4rIP-Yrr7E7XVY1SJxzIVU-I1mM7fDsfot3So7fND9o3VuhOE_5j8qO1vSXzTapTgqJX8WadDtH22fDimcUPM-kYRnEhWHk-TvhsJcjyYHQOBljcWCpyFuSeasTViM6MmS1azBXNMq16WOKU1tW3spSGd6AbnVk2B4iT79Ln8yUnFAiXLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غذاهایی که فاسد نمیشن رو بشناسیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/697175" target="_blank">📅 13:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697174">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95c8d48f9.mp4?token=qVpVELAr1siUOQemMvT_Xa34oKdTFANl6eJhQOznYkUGv-So1_RGWecqlQWqhj9nXATrlx4OymQtPcdONvkpM8jXlJ6i7BAf3JFhGDh9xJ6hMK51DqwTjGqH_GmcaHaZmwOQ4rTeyWMcGmUtpQncoMbLL2TYQ6GR2Jx_JgAg67TEHnn9yXNSUVPCd-cei_Cc1no0Ycqsk0cGMo_XQ3znufeiYqHd2LS4VR5lRXSYQx3U3YgG02PFaHpX1OGY3_dIVq0Ok45pyVrL5TP0_hMjehmZFR41KErgXFXGLJaeaAr8n8M0rQLaFRr0rKiOBfWx-WkZ_lwTgVEheRJC8h5aoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95c8d48f9.mp4?token=qVpVELAr1siUOQemMvT_Xa34oKdTFANl6eJhQOznYkUGv-So1_RGWecqlQWqhj9nXATrlx4OymQtPcdONvkpM8jXlJ6i7BAf3JFhGDh9xJ6hMK51DqwTjGqH_GmcaHaZmwOQ4rTeyWMcGmUtpQncoMbLL2TYQ6GR2Jx_JgAg67TEHnn9yXNSUVPCd-cei_Cc1no0Ycqsk0cGMo_XQ3znufeiYqHd2LS4VR5lRXSYQx3U3YgG02PFaHpX1OGY3_dIVq0Ok45pyVrL5TP0_hMjehmZFR41KErgXFXGLJaeaAr8n8M0rQLaFRr0rKiOBfWx-WkZ_lwTgVEheRJC8h5aoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاری شدن سیلاب در بخش‌هایی از شهر انگوت از توابع شهرستان گرمی استان اردبیل
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/697174" target="_blank">📅 13:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697173">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
افزایش اعتبار کالابرگ‌های یک میلیون تومانی آغاز شد
🔹
معاون رفاه و امور اقتصادی وزارت تعاون، کار و رفاه اجتماعی از افزایش ۵۰ درصدی کالابرگ حدود ۱۱ میلیون نفر از هموطنان خبر داد و گفت: در مرحله اول امروز حساب کالابرگ افراد تحت پوشش کمیته امداد و سازمان بهزیستی…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/697173" target="_blank">📅 13:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697172">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9d065a2a.mp4?token=sG1GBc3m7TybY8iSvUFjIVhzTPJgqX2fWUvl0SJG-RSGHp95mRcU8DOJdXHjH507mFq_lTPMyRgdmZXri3dWdpSrTXZIXHYG3yY6i1Q7jMcVRBPeBFNn9JsWsGbmbIOlGcuhHyrX_aZAYCZCmraoR4H3P8mh3RQbBC-UOJkqO6Xtb33p-9jZTKLwjw2lASaPN3VKqm472XV_1jXG7JQwgVr3HxO-Q4Q2p_ksNt2EK-v0jtNqF6qgVqncMHQjAcOye7oWuIIXutivC5dEPkA6ocZvdEOQmP77L_Blot6VeDPg3Qh8tT6KvzFKqlP-pgabDIJHzBvZ-wbBvaBDUeFvlKQpCPzf8GcuhcV3xdBnfrS46GHwOHKw0g9IyO6GySqPHI-U821m-m7PvD3HXxxqO6UZfgrOp107ITZA1CyzWJGlX3snbM1L0HhLOoikeBIvIiR5p6vHR3cVmkE9FOHtzKg4a2kWVkwNPEr2-si6cbpl-egFMk80SjZkrs8F8JlZXrcwL3kiWc9kKRwGwkdYnt2K67GfTeK2rPsKbE5-K4TMmZo0sIKbkNPtWwsn_CBfNEhUSdISVa_LVpiTqznsrWzlPa7ZasvoGhyuur0HG47y4St6CGHh-nN916a5ima6yIMEAMMj8ohkzMSkuOB9JIId0MSTZQDHoPrZ37eY0VU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9d065a2a.mp4?token=sG1GBc3m7TybY8iSvUFjIVhzTPJgqX2fWUvl0SJG-RSGHp95mRcU8DOJdXHjH507mFq_lTPMyRgdmZXri3dWdpSrTXZIXHYG3yY6i1Q7jMcVRBPeBFNn9JsWsGbmbIOlGcuhHyrX_aZAYCZCmraoR4H3P8mh3RQbBC-UOJkqO6Xtb33p-9jZTKLwjw2lASaPN3VKqm472XV_1jXG7JQwgVr3HxO-Q4Q2p_ksNt2EK-v0jtNqF6qgVqncMHQjAcOye7oWuIIXutivC5dEPkA6ocZvdEOQmP77L_Blot6VeDPg3Qh8tT6KvzFKqlP-pgabDIJHzBvZ-wbBvaBDUeFvlKQpCPzf8GcuhcV3xdBnfrS46GHwOHKw0g9IyO6GySqPHI-U821m-m7PvD3HXxxqO6UZfgrOp107ITZA1CyzWJGlX3snbM1L0HhLOoikeBIvIiR5p6vHR3cVmkE9FOHtzKg4a2kWVkwNPEr2-si6cbpl-egFMk80SjZkrs8F8JlZXrcwL3kiWc9kKRwGwkdYnt2K67GfTeK2rPsKbE5-K4TMmZo0sIKbkNPtWwsn_CBfNEhUSdISVa_LVpiTqznsrWzlPa7ZasvoGhyuur0HG47y4St6CGHh-nN916a5ima6yIMEAMMj8ohkzMSkuOB9JIId0MSTZQDHoPrZ37eY0VU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/697172" target="_blank">📅 13:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697171">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6560e7755c.mp4?token=tbV0Xz20ucWQRldOCsPJ6JHiuAbU5ag9ym7Z5Q4V8fKsQy7C2sGpA603WF0gizSAVQEIhV2AhIZFeCzy2Y13EpzpJPGl8B8eok-XfBHCBmhynxn6Z9oc76KAQOT4mfF4fmDEhi96MEQZ9GpwJEVcrXrJ4XAt3-jLmS8MdhkDSY4eDnCF7EGJAXzuYtbfrNef_EF3zjeus0jqb5X7orKbJA2181MvRaCdS9UoFbdnEwQpOh8QoR9xKhu5Ew0MD-UVFlzUl0oaiGx4WsWaCSnceNLhVKUPWTXLczpXaKKuzpVdYZNGGB8mgaYEKfuk1tEHWZNpAjnL4U7t6w3ui-erjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6560e7755c.mp4?token=tbV0Xz20ucWQRldOCsPJ6JHiuAbU5ag9ym7Z5Q4V8fKsQy7C2sGpA603WF0gizSAVQEIhV2AhIZFeCzy2Y13EpzpJPGl8B8eok-XfBHCBmhynxn6Z9oc76KAQOT4mfF4fmDEhi96MEQZ9GpwJEVcrXrJ4XAt3-jLmS8MdhkDSY4eDnCF7EGJAXzuYtbfrNef_EF3zjeus0jqb5X7orKbJA2181MvRaCdS9UoFbdnEwQpOh8QoR9xKhu5Ew0MD-UVFlzUl0oaiGx4WsWaCSnceNLhVKUPWTXLczpXaKKuzpVdYZNGGB8mgaYEKfuk1tEHWZNpAjnL4U7t6w3ui-erjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تک درخت دریا؛ وقتی نخل خرما در داخل آب زنده می ماند!!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/697171" target="_blank">📅 12:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697170">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
افزایش اعتبار کالابرگ‌های یک میلیون تومانی آغاز شد
🔹
معاون رفاه و امور اقتصادی وزارت تعاون، کار و رفاه اجتماعی از افزایش ۵۰ درصدی کالابرگ حدود ۱۱ میلیون نفر از هموطنان خبر داد و گفت: در مرحله اول امروز حساب کالابرگ افراد تحت پوشش کمیته امداد و سازمان بهزیستی ۵۰۰ هزار تومان شارژ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/697170" target="_blank">📅 12:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697169">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
پوتین به ترامپ: گزینه‌های دیپلماتیک در پرونده ایران هنوز به پایان نرسیده و دستیابی به توافق، امری ممکن و ضروری است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/697169" target="_blank">📅 12:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697168">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTHw5v0axqOAZ-PFqGx9lLVP9aosbeWvvKTSY0JPijBse19OLtGPe8jUGFSt0YF02pwtYnM-kaFLE02wWDNip1yMZhL2AoBM1Xlk7RIXqlIZ6KOOtcMgaO8NIRzpniw7mZ27pWjoAhxcm7p4N3MtTLu8HcWjFiPuaoG9yj_bVUXkikaTIZTnQ6FEtsWi8rxcJJkc_THl09QEgmrnVfvGtCsDDxJY7AEJYFFoJWy_DwWXNSB00wdQjhw_ZFOv1IPb61qOfUGAn-q_WjlCl73y9EHUuhUx-p0cYG7p85r4fAE2yPffIlofLxSg7Hb0yZe-I1t_mwXzgnkOl_4Qy8Q0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
برج ساعت حرم امام رضا (ع)
یادمانی از طنینِ خدمت،
آوایی که قرن‌هاست زائران را فرا می‌خواند.
روایتی‌ست از لحظاتِ حضور در صحن و سرایی که پناهِ دل‌هاست.
✨
مشخصات محصول:
▫️
ابعاد: ۳۱ × ۹.۵ × ۹.۵ سانتی‌متر
▫️
متریال: پلی‌استر
▫️
وزن: ۱۱۵۰ گرم
▫️
طراحی خاص و باجزئیات
▫️
مناسب دکور منزل، محل کار و فضای فرهنگی
💰
قیمت:
۵٬۹۳۰ هزارتومان
⏳
موجودی محدود؛
برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/697168" target="_blank">📅 12:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697167">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlAaWhA4Hc6OP9BqysmWTyZV4BFkooQgiAPXbR-STUan4HRGOBDwiIl_ARuEP57YIFWZQ42s9f8_CapwCemzoZXs1jsRTkQFRgEm-92feEHVplJ5GeYKVjtmgpEwfbKFagkX89Xel-VgDC5PFP8UcmEk1XFsW5QF18yaXRfEZKkVU5W2yWEfISB8c1D0yVgb4iFGE3HR9TimVPQ8QGDpAmq0Gj-hU7qnpVaOZ8xqAQG7_s13MAdyfAgUaayr-VUbWHz5-aJOiE6jFjaVV4irXAD3BHok3Dz6qLV2vEyb0JT3gwUr-IMZHdfF8H2CPqE3Sb5YXAq7eeiTnC_vpQGvAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقرار دبیرخانه دائمی جشنواره فیلم کودک در اصفهان
🔹
شهرداری اصفهان و بنیاد سینمایی فارابی با امضای تفاهم‌نامه تشکیل دبیرخانه دائمی جشنواره بین‌المللی فیلم‌های کودکان و نوجوانان، بر استمرار این رویداد در اصفهان و آغاز برنامه‌ریزی برای دوره‌های آینده توافق کردند.
🔹
این توافق که در حضور وزیر ارشاد به امضا رسید با هدف استمرار همکاری‌ها و فراهم‌کردن زمینه برنامه‌ریزی بلندمدت برای دوره‌های آینده جشنواره و افزایش کیفیت ساخت فیلم کودک و نوجوان انجام گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/697167" target="_blank">📅 12:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697163">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2GAg6jq29FCiqVC_e0C42Ezt5xbxNDJEc-avB6xvQkq7HKUINE_7Vl_Un6Qm3e7iCDKdAowR_COvvTG6gpl9s23HlVC4_tIDyQAn8vk_v6n-_ceolK0UU3lqTaPGHw7vDmIwxKRr0C2FFjHT_y31TlYT-ns5bTbHXVjsldSkAvpKEKhgBtOqkcgRWsDTBZtszFGnalUsWIRsdGCrXprKO7uesrSDSI1mhVsALit2FeOow7NHKHXogHStMBH3evyY2ohfYAmNysbdHwThcX5XKvDzgM4CUaNjn50A-wywsObHEwZu4KZBnvwSUXBtv5Vc32UJrT9PlyMoqQcuUBEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fK4wOyeCGeXqiexfMkkhBGRqqKwlqIZ8UWqXFEASKSqYwXVyjnTEkJb8F8xNo7lfiCkM_X2s12TC9Q8LaGVmtGnOKoauRsVPkuTgaRTqx6r_V9GLXpA6yCkWMnAv9UVKyJq0oUqDoyI11O0SaaDiM_xD5PvM33-Xu0-ozhiA3rYHfW4zugFRD7iDs8C7qloCh3RF_mB-3F7BZ_0Lld5SP06ECBu1KrXJuM9ZyWBjMgzsrl0zWLHELaKzNK2Fr5wv_8vU2DA_r5zVOH8qJ810UbmV5BGANfOqV7vdUxRQKRfj5COu36iGeCWbfl8HTeQNX2L48Fa48dROqgGUbzRurA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KC7ouOetWdctKkjxl5nwetglxujHcfSDDESgTqOVnVRjdoARJ489l-G1nfpC1CPlpnkG3Zno5dAryGKnhXag6k8zwTDW3n2_7VLY-W9oey3Z35FRF7_tdVtcJ4ZYHyNLbS9uKvZTU_az5dhYx9JSIQVjIMa5s7T6ffH9lM6Ahos7QXaDvLTN4elL4wR92Rbj3MFaLl0OPhgCaYMNUMZ4X1rqFM_bca_XBa5SOvEM_dttNz5zciSimYurm5Z3ltOssZK-jvpbCzA8wWAXdOT-LQzRsYp_w8NO-oP4ucBcrEC1TlORYUABPMozE10LBN4fcbOxyob4kvUGEck90KS1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDHlTymyVbYebu4TndvC0GwW0ucUeNGIRtqBSZpATZGfkDQBN3wPdVINfTZ3oTSBp2phQfjfirXSPcAakPkqwwRny_3P8Ml_XrKhen6sM7euUg7sLrPaSYS9XrcPom-6NROxcHjx_7Hu7LWJ7Y01Qba-SlpxEITIVQzhiiFvL2rSvK_x3ItZpcbHXOMcaaK2RGr9kGGyTBWGFaCqSEguO_yN-Pjp25CGy-Lm8xUGuN_JyAcK9bZDabRfo4sVjadvfMEzfuZb3KSyiAL0UFnbk-e8CRAeDpbOEuRXBLcm5UGphUYWFYEzls65XteHPqgLHsz5r5gwKOdghTe29nbbnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر تماشایی از رعدوبرق، دیشب در سلطان بلاغ آوج
#اخبار_قزوین
در فضای مجازی
👇
@akhbarghazvin</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/697163" target="_blank">📅 12:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697162">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9e3d3a97.mp4?token=jzHsxVbMrhuCAynKAfd1LHcaYrbdT6vUqM40z0WhJNXCxhsVejesi1YvVjHJ6ZQ1Vm8NH5k5vw8rR7fSW4OeQs5b7JEmXyuIEWNrosSg41RBd_dJhxKWIi1YUaV0ATxhPvVqD0j3If6x2_zcDKizbr4zogrIeaYe-bsCk_ZgrlDcW3cJOiG96pwBFLtUIi_waKAiR-iK20f1vATRgdkZanrZbg7d37cUisQ251vSnTv2PKvhaHf0lv_zyaDIgesBcu8EOlVbj0JmHioYLtqIZ0n182sNeULM7Td4ES-McrAX14Toi_RLNL2y1rYvrzY4cw1Y6E3o6vLdNSUzULU6BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9e3d3a97.mp4?token=jzHsxVbMrhuCAynKAfd1LHcaYrbdT6vUqM40z0WhJNXCxhsVejesi1YvVjHJ6ZQ1Vm8NH5k5vw8rR7fSW4OeQs5b7JEmXyuIEWNrosSg41RBd_dJhxKWIi1YUaV0ATxhPvVqD0j3If6x2_zcDKizbr4zogrIeaYe-bsCk_ZgrlDcW3cJOiG96pwBFLtUIi_waKAiR-iK20f1vATRgdkZanrZbg7d37cUisQ251vSnTv2PKvhaHf0lv_zyaDIgesBcu8EOlVbj0JmHioYLtqIZ0n182sNeULM7Td4ES-McrAX14Toi_RLNL2y1rYvrzY4cw1Y6E3o6vLdNSUzULU6BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیاتی از تیراندازی مرگبار در پاساژ سعدی  مرکز اطلاع‌رسانی فرماندهی انتظامی تهران:
🔹
مردی ۲۵ تا ۳۰ ساله با ورود اجباری به یک واحد تجاری، به منشی شرکت شلیک و سپس خودکشی کرد. انگیزه حادثه هنوز مشخص نیست.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/697162" target="_blank">📅 12:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697161">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
هزینه رجیستری خانواده آیفون۱۸ مشخص شد: آیفون ۱۸ پرو مکس ۱۹۷ میلیون تومان، آیفون ۱۸ پرو ۱۵۸ میلیون تومان
/ زومیت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/697161" target="_blank">📅 12:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697159">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سپاه سیدالشهدا تهران از انهدام مهمات عمل‌نکرده در ملارد از ساعت ۱۳ تا ۱۷ امروز خبر داد و احتمال شنیده‌شدن صدای انفجار را ناشی از این عملیات اعلام کرد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/697159" target="_blank">📅 12:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697158">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c56a9ea9e.mp4?token=hCjrwj3IyLJFzjiKm0fX8ZHsllS30MwXz_GIOSqR9l7au71BpLk8RW5w1XoIXUvnKFBEvHeVoMOmfXXB_AKL8PiSlIE0xjmTqXN-mGnBUuVXRzaWamm-c8sbasxre02Mnt_fYTCPlO56QtYZIaWHni90smIFLeBR0GJinlVsQUN95cFWR79ynabSMkdBS8-i8vX-ogAma6QvBgfSCwxi8aiI9Pj5HTbvV0hvMBeX2TND5PInjfmv1mURywH0n7WeEZWpO8x9avmNFt-Cir6TMnSYsF-bBsO2aSpJ3zWjgZV_ZNNAN2I4aJvjsXJf6hgvXlo7SmuNdQsrc3Sxj86sJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c56a9ea9e.mp4?token=hCjrwj3IyLJFzjiKm0fX8ZHsllS30MwXz_GIOSqR9l7au71BpLk8RW5w1XoIXUvnKFBEvHeVoMOmfXXB_AKL8PiSlIE0xjmTqXN-mGnBUuVXRzaWamm-c8sbasxre02Mnt_fYTCPlO56QtYZIaWHni90smIFLeBR0GJinlVsQUN95cFWR79ynabSMkdBS8-i8vX-ogAma6QvBgfSCwxi8aiI9Pj5HTbvV0hvMBeX2TND5PInjfmv1mURywH0n7WeEZWpO8x9avmNFt-Cir6TMnSYsF-bBsO2aSpJ3zWjgZV_ZNNAN2I4aJvjsXJf6hgvXlo7SmuNdQsrc3Sxj86sJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد تند رابرت دنیرو، بازیگر سرشناس آمریکایی از ترامپ: دست‌های لعنتی‌تون رو از رأی‌مون کوتاه کنید! آن‌ها نمی‌توانند رأی‌دهندگان را جذب کنند، پس تلاش می‌کنند حق رأی را بگیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/697158" target="_blank">📅 12:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697157">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1fa4aad0.mp4?token=EcaK_0q5Q97mOdB0JIucR3BwSDK-IPEOqswskgsnakA2f9S4pQUp-JlJwU5n6DBsa4IqFQKegfmGRNi-y2OwZf1TF1hs-PViHgNpPyxSeC-2h8e8FeHe46tVvrxIrPJMRt7z771cLAHlx5qH80pjew-ajL6qrxgg9i4McH6ngUJWDooG-NDiC7kQJW2BKZ8urUqZ6nPzItS11UGmW7TTUTF3WybXZzmHrbLv9-Bo6PweK59JYCAbVnVj5VmCWDo8TXccJx6791BDMfhP_h971LEApOovnatEp_cihcMFlVMRr5KO-nyaiz0KIKbuDoF_u2WfVbHKT4B5i6piGZijvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1fa4aad0.mp4?token=EcaK_0q5Q97mOdB0JIucR3BwSDK-IPEOqswskgsnakA2f9S4pQUp-JlJwU5n6DBsa4IqFQKegfmGRNi-y2OwZf1TF1hs-PViHgNpPyxSeC-2h8e8FeHe46tVvrxIrPJMRt7z771cLAHlx5qH80pjew-ajL6qrxgg9i4McH6ngUJWDooG-NDiC7kQJW2BKZ8urUqZ6nPzItS11UGmW7TTUTF3WybXZzmHrbLv9-Bo6PweK59JYCAbVnVj5VmCWDo8TXccJx6791BDMfhP_h971LEApOovnatEp_cihcMFlVMRr5KO-nyaiz0KIKbuDoF_u2WfVbHKT4B5i6piGZijvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستی علت‌های پنهان این رفتارها چیه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/697157" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697155">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd6b29328.mp4?token=EK1dqIqzk-FVmj4w1x6FUc9_bbrOKucpsW4-1m49zKTe-uVu1Na9l2WXcKRMmZXvs5tYvw87Ofrk3tKwzlOsbXayLIJsUlDLWBlx-lAifYjUK6WDDmxd9QxdCpeF6coKxA3vlYlonpD6WUF42ZTm8QKhOsCP7um3yy2KCDPiBbniOxsrMnHJfwsWedfGJsk0PvhiHYgUoUXV0O1KsFLgLFkR7r3cjCaAMJLy-72XG2YFhUG_CQuXYOIpLP4bAm5Vd1V8lfxfhsu8cixJ3qieAj72hrvEJe_GK701X5XkfjuL5y4s99m2wGIOIVkuS53B-gt0ZoEmsODETQX5qF4STw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd6b29328.mp4?token=EK1dqIqzk-FVmj4w1x6FUc9_bbrOKucpsW4-1m49zKTe-uVu1Na9l2WXcKRMmZXvs5tYvw87Ofrk3tKwzlOsbXayLIJsUlDLWBlx-lAifYjUK6WDDmxd9QxdCpeF6coKxA3vlYlonpD6WUF42ZTm8QKhOsCP7um3yy2KCDPiBbniOxsrMnHJfwsWedfGJsk0PvhiHYgUoUXV0O1KsFLgLFkR7r3cjCaAMJLy-72XG2YFhUG_CQuXYOIpLP4bAm5Vd1V8lfxfhsu8cixJ3qieAj72hrvEJe_GK701X5XkfjuL5y4s99m2wGIOIVkuS53B-gt0ZoEmsODETQX5qF4STw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌ها و پهپادهای یمنی به قلب ثروت نفتی عربستان رسید
🔹
منابع عربی از حملات ارتش یمن به منطقه الشرقیه که ثروت نفتی عربستان را در خود جای داده و دهها چاه و پالایشگاه نفت و گاز در آن قرار دارد، خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/697155" target="_blank">📅 12:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697154">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a05e90c6c.mp4?token=FdB5eN_QkIyYJUbG5uOEX-jg5f_AK3YB2xABWjtEEEhe_Jin-3MDD8HPxaHV5cNfjA4BaUSROHb-5vK5plaSv2w6OKTo_HnZu_M4mOYaCbyNUY0qBVgWHyhVt2lqyeIq90UqjmKV5tD_-8jrkKuB7np-adugj8xtA-ZWJGa95ALlbe8ZmbnmAQe7HNA9JvTiW_-pFNZYUgsYwlMksVlQQiBlafuo_7adyrP3zqvSBJ6uo69X2U5S0hace9fjEdcJG9UbjI4BpkIAIYCBclGroO0oEu0uAcg7XAMjlmqGEhJuiq9ddT9y626MVWhEVoWfwFZjFVcSfCjlB2pHACfB1Y3MgrOU0FqqJeFcYdz_3GzGOF7kSKE1HeYlBKkY2ygg4eQaa_ecu8n7Ms4cVfRn--49qBiBM0EexHThs1ZsoZNXjN6O9BPGAdd7IqDkWpvzxt7a9aSrA881xDKjLyKMAUS9lM2J5F65IPjotsQvhXjgFdNm5zShHosN0sHe89qLFKIe6rwl8LY1cjUB8WOIHlgt5vUEedZwOrlVK-YLA03i6s64TgMybLNyFqsc66Vu9QmLAAtyODlFj-vhAWojDd0_i8MRq3CrVuAQvFn1SEkjq5oGlDdsBH8VXq5xDksc7WmQ0RRgFgSzIOk-eiernSpTlP_M8ISdJeqSr25m9S0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a05e90c6c.mp4?token=FdB5eN_QkIyYJUbG5uOEX-jg5f_AK3YB2xABWjtEEEhe_Jin-3MDD8HPxaHV5cNfjA4BaUSROHb-5vK5plaSv2w6OKTo_HnZu_M4mOYaCbyNUY0qBVgWHyhVt2lqyeIq90UqjmKV5tD_-8jrkKuB7np-adugj8xtA-ZWJGa95ALlbe8ZmbnmAQe7HNA9JvTiW_-pFNZYUgsYwlMksVlQQiBlafuo_7adyrP3zqvSBJ6uo69X2U5S0hace9fjEdcJG9UbjI4BpkIAIYCBclGroO0oEu0uAcg7XAMjlmqGEhJuiq9ddT9y626MVWhEVoWfwFZjFVcSfCjlB2pHACfB1Y3MgrOU0FqqJeFcYdz_3GzGOF7kSKE1HeYlBKkY2ygg4eQaa_ecu8n7Ms4cVfRn--49qBiBM0EexHThs1ZsoZNXjN6O9BPGAdd7IqDkWpvzxt7a9aSrA881xDKjLyKMAUS9lM2J5F65IPjotsQvhXjgFdNm5zShHosN0sHe89qLFKIe6rwl8LY1cjUB8WOIHlgt5vUEedZwOrlVK-YLA03i6s64TgMybLNyFqsc66Vu9QmLAAtyODlFj-vhAWojDd0_i8MRq3CrVuAQvFn1SEkjq5oGlDdsBH8VXq5xDksc7WmQ0RRgFgSzIOk-eiernSpTlP_M8ISdJeqSr25m9S0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف تحلیلگر نظامی تلویزیون موساد به قدرت موشکی ایران
:
برای سیاستمداران آمریکایی هنوز این سؤال مطرح است که چطور با وجود این حجم از بمباران، ایران همچنان توان موشکی خود را حفظ کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/697154" target="_blank">📅 12:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697153">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
رئیس سازمان مدیریت بحران: قبل‌از حملات موشکی، هشدار داده بودیم که انبار نفت شهران و بلوار ارتش باید جابه‌جا شوند
🔹
الان هم مکتوب اعلام کردیم که مکان آنها باید تغییر کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/697153" target="_blank">📅 11:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697152">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
رئیس سازمان امور دانشجویان: دانشگاه‌ها در هیچ شرایطی تعطیل نمی‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/697152" target="_blank">📅 11:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697151">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-yt5mCHFvc2hXjcaKv6zNmyVhEEs3Mf4HGt211RTle0ffyvfpIdpjl0L8EaCvt32Fq7SVRWjZJ2r_rFdORBPxZyYb5o7MzM22ryNEHW6ptQlPQJ2t3D8L_caRjbJoWjql3AvQ4JL1bFur2i2gb1q3NlGld2-f28vCkYxiIwR3j8qCq0M02eTSkeYXj_UNb1I3oyhM6wVfc7Y7hWG6Tmd_RthCQCU4aOy3kxZon-ie9iZB4AApx2HeTXPcw18EMOeOEpmteXhouFZpf_g7nmv00l6dF3ZzYz6bTI0SIVo8CJQyMqhiLJ7QbZXGTkoM8XQRka9TaE8UFdSSjT4ERgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۰۴۸ گیمر به مرحله بعد مسابقات همراه اول رسیدند
🔹
در مرحله اول تورنمنت همراه اول، ۲۰۶ بازی برگزار شد و بازیکنان در مجموع ۱۷۳۶ گل به ثمر رساندند. میانگین گل در هر بازی ۸.۴۳ بود. دیدار بارسلونا و پاری‌سن‌ژرمن با نتیجه ۱۵ بر صفر، پرگل‌ترین بازی این مرحله شد.
🔹
رئال مادرید با ۳۱.۳ درصد انتخاب، محبوب‌ترین تیم مرحله اول تورنمنت بازی FC26 همراه اول شد. تیم ملی فرانسه با ۲۲.۳ درصد و پاری‌سن‌ژرمن با ۱۳.۷ درصد در رتبه‌های بعدی قرار گرفتند.
🔹
در پایان مرحله اول، ۲۰۴۸ گیمر شامل ۱۹۰۰ مرد و ۱۴۸ زن به مرحله بعد راه یافتند و مرحله بعد مسابقات از دوشنبه ۲۰ مهر آغاز می‌شود.
http://mci.ir/-A5VS2O
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/697151" target="_blank">📅 11:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697149">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTRFNsZeAi2ltggOqqfX-ZvU2yi5412shkYDwbvw44g6ViPmW38eZA8tYBXJ8eOyrMASb-SurvaB8YHJZ8Wyvx74ciVR3YjVV3K413GOb3RbketiUTquMhMg9wux4vG3hoFBa4PRzbEC66ytHhV2VE1wHw9dpIIeQ3Un4DRkX2sdAQgQef_3iz07hfWfATGShp0d6BQ-p2dod_e2PgbBJ6IXZ0Ce-OG-0cc9jFYTWFdpColDglWvvXYbYCIW51Db-BvFlr9Gt8b7-fgpx3DJZcDJL99eHFIqmdi3ZHjPSvoBP_THxE4JB78gWtwJPy3JZOfbCfViLz7cucDdMKtjOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقایسه ذخایر سدهای پنجگانه پایتخت در ۱۴۰۴ و ۱۴۰۵
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/697149" target="_blank">📅 11:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697147">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2JdBfxbeQak8yfMQiH10QiPwIGWWQhdZziJzIhdaKDwtEmfPHF_h6WoKlMc8ayiI-7fN1Z2aCW8tuMSLBCxM7S34ES8b-j6Ij1gue3gr-geVbvBFlF-l4fdpmmjw_gy6lVoVMnaccaMhb-p-d_CFeEB9bttTgW-ztzESl0n_rAwWL_iRul6nVTYk6p3sOrJ1aqgvcLKGd1HKENDRb2EriN4PHu0vi0S88VXDDzvlvSKGKNLGgRXu2romv3nl09HvqNTT38c0sig4GB_aZw7F2hlb_tcwVdhLY_1T773FdWf4k5vm64v8mtJcU-8yMqOCRFPy8L_vL_U3YWQ1gXJbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر خوش معاون علمی رئیس‌جمهور
صدور مجوز جذب ۱۷۵۰ نخبه در دستگاه‌های اجرایی
🔹
حسین افشین، معاون علمی رئیس‌جمهور، از نهایی‌شدن سازوکارهای استخدام ۱۷۵۰ نخبه در دستگاه‌های اجرایی و دانشگاه‌ها خبر داد؛ اقدامی که با همکاری سازمان اداری و استخدامی کشور و سازمان برنامه و بودجه به مرحله نهایی رسیده است.
🔹
به گفته افشین، فراخوان چهارم جذب نخبگان در دستگاه‌های اجرایی قرار است اوایل آذرماه از سوی بنیاد ملی نخبگان منتشر شود. او تأمین کدهای استخدامی این تعداد را هدیه‌ای به جامعه نخبگانی کشور به مناسبت روز ملی نخبگان عنوان کرد.
معاون علمی رئیس‌جمهور همچنین از توافق برای تسهیل جذب اعضای هیئت علمی نخبه در بازه زمانی ۱۴۰۳ تا ۱۴۰۵ خبر داد. بر اساس این توافق، کدهای استخدامی موردنیاز به‌صورت پیش‌دستانه تأمین شده تا روند جذب اعضای هیئت علمی با مشکلات پیشین در تأمین کد استخدامی مواجه نشود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/697147" target="_blank">📅 11:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697146">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55de7d3a71.mp4?token=tvSSqon5FiHhHAPWLZyjdYMoHufVCayF9SQKg8vVnHglpIwJwK0sYudRmH3OM3IYS6BgDvX3vttdNbr7Qn6I1sAfUo9LKiyH7u-uDwnR4A7I-vNsuWqTRUJjLWq2HQk72XQfJPlsE_5jqUn63ym5b5GAGLUip9dBrnwB4fhv_yCRkfQudCWvTaE62SDX2nyDr1s_njwlomBqVDO46enLQ6WRLkG_5pl8UPZ_BRXGW1UOOkaicUaqT3dufZPI2H2U-j26ueK3a2ghOY5zzzusF_VFFWJHEuVu1j3cZI4wpTdfh3xIqZA_K9Cl0rtY-5c2cfFfY3rBTf8VQsWVKlEgPwpUIYBcOqy0rm7Rv1QkrkkuooYCiIXd7jB0I7JgmLHFxfy_YGnPMintO8zg1ktJ9EIziqmVy2yy1bhuybLMmjpO6lXK1lsiI4Xjvgk-5BpuIRA5EYIbz-jBeOzVlIYKnHB1Ym7cCH15D7lUS_uqnI00oFDBEQcT2-yMzMeZ6iwQO9UghzBVEaD91xt5pQkambMmOOQJrzw5d7X9qg_oGC_WM_5oT7QlHWueuL9orrRrHiZJ1Xd2ZhPHoB36A9GINCQm5Mu5Z24OhwoPV03hkvL5tH3YZpIwHCHdhgsK09yZ7QHdYJUeCGGrmQgzNT6RWHiG_v8fnvkMjFghgkEL9F0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55de7d3a71.mp4?token=tvSSqon5FiHhHAPWLZyjdYMoHufVCayF9SQKg8vVnHglpIwJwK0sYudRmH3OM3IYS6BgDvX3vttdNbr7Qn6I1sAfUo9LKiyH7u-uDwnR4A7I-vNsuWqTRUJjLWq2HQk72XQfJPlsE_5jqUn63ym5b5GAGLUip9dBrnwB4fhv_yCRkfQudCWvTaE62SDX2nyDr1s_njwlomBqVDO46enLQ6WRLkG_5pl8UPZ_BRXGW1UOOkaicUaqT3dufZPI2H2U-j26ueK3a2ghOY5zzzusF_VFFWJHEuVu1j3cZI4wpTdfh3xIqZA_K9Cl0rtY-5c2cfFfY3rBTf8VQsWVKlEgPwpUIYBcOqy0rm7Rv1QkrkkuooYCiIXd7jB0I7JgmLHFxfy_YGnPMintO8zg1ktJ9EIziqmVy2yy1bhuybLMmjpO6lXK1lsiI4Xjvgk-5BpuIRA5EYIbz-jBeOzVlIYKnHB1Ym7cCH15D7lUS_uqnI00oFDBEQcT2-yMzMeZ6iwQO9UghzBVEaD91xt5pQkambMmOOQJrzw5d7X9qg_oGC_WM_5oT7QlHWueuL9orrRrHiZJ1Xd2ZhPHoB36A9GINCQm5Mu5Z24OhwoPV03hkvL5tH3YZpIwHCHdhgsK09yZ7QHdYJUeCGGrmQgzNT6RWHiG_v8fnvkMjFghgkEL9F0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگفتی غار کرفتو: اولین آپارتمان چهارطبقه دنیا در ایران
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/697146" target="_blank">📅 11:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697145">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
جزئیاتی از تیراندازی مرگبار در پاساژ سعدی
مرکز اطلاع‌رسانی فرماندهی انتظامی تهران:
🔹
مردی ۲۵ تا ۳۰ ساله با ورود اجباری به یک واحد تجاری، به منشی شرکت شلیک و سپس خودکشی کرد. انگیزه حادثه هنوز مشخص نیست.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/697145" target="_blank">📅 11:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697144">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9ba5dadbc.mp4?token=NG6zhsnlHPsYoHbQNXjMZF-oYVYswTWfYKY3-YZc7ghNf3s9_zglKhizkRvDK2qFXKojEbvIKsVpMuubhbktfGmUC_I96csp8L0vQzj1mbejqBfKLBrMTjTJ4mAEOCmX6Np7puMN4EO1v4dQq-Y0mAhipNi153yi4WEH7LcNIPxubQzX0WXXoo9FS1BZvjwlnPLXpeS8ksHC0oP4-IS21M9ZzT1hUrLlyxNZP2z68qkk9ZtJU5jUVrP4HIROEnYBYHswE4oq1xLLC1d_YezKCioaHdzFWavj3I4YXEjEjX0ajU50roftKP1VY3M_Ns3gZtXBgSan6IANM4KIuCpAjwtMMWoh4fYnKyS0tVEIMXxtjeHikE51jrJbg-ZdVwusFDKENPTOwFg548K75FICFuM9ZSIa7cZ0GQ6S4USoojBvp6e4qqaCciArBmSRPY3y98TuFqpdEKqFZBxSFNdq6z6JFjzmrI2y-rIgJiz9d_9Wd_p7QjruKX-wUw0q5KP-vimQWC0VMnOiJbsAgvqe4WsT7pumwFo--nSi5Kzh76XPYuIMkHSJrTbhU8pte7hsgzjSWk-hncfd2riNfovGpSEcYSbgF8rS7DdM4Cmt4YytfhsnL0bvjZucv9U1XUhdx3waJLqdmPb3zjfsoF-YhmxIXS6bwFQdZ1oJt0vRLfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9ba5dadbc.mp4?token=NG6zhsnlHPsYoHbQNXjMZF-oYVYswTWfYKY3-YZc7ghNf3s9_zglKhizkRvDK2qFXKojEbvIKsVpMuubhbktfGmUC_I96csp8L0vQzj1mbejqBfKLBrMTjTJ4mAEOCmX6Np7puMN4EO1v4dQq-Y0mAhipNi153yi4WEH7LcNIPxubQzX0WXXoo9FS1BZvjwlnPLXpeS8ksHC0oP4-IS21M9ZzT1hUrLlyxNZP2z68qkk9ZtJU5jUVrP4HIROEnYBYHswE4oq1xLLC1d_YezKCioaHdzFWavj3I4YXEjEjX0ajU50roftKP1VY3M_Ns3gZtXBgSan6IANM4KIuCpAjwtMMWoh4fYnKyS0tVEIMXxtjeHikE51jrJbg-ZdVwusFDKENPTOwFg548K75FICFuM9ZSIa7cZ0GQ6S4USoojBvp6e4qqaCciArBmSRPY3y98TuFqpdEKqFZBxSFNdq6z6JFjzmrI2y-rIgJiz9d_9Wd_p7QjruKX-wUw0q5KP-vimQWC0VMnOiJbsAgvqe4WsT7pumwFo--nSi5Kzh76XPYuIMkHSJrTbhU8pte7hsgzjSWk-hncfd2riNfovGpSEcYSbgF8rS7DdM4Cmt4YytfhsnL0bvjZucv9U1XUhdx3waJLqdmPb3zjfsoF-YhmxIXS6bwFQdZ1oJt0vRLfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری بیشتر از زلزله مهیب پاناما
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/697144" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697143">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHnbV0xl1FA-toltMQmJNVAfi3jVZbJolgltZ8x727ktqjdKkvBkClsn0Q3e0dtiLmF-r6UEJh5KTJfOYplPtk48S9aL84VBdWhSsq2nXFHueDj68FzLqLrVmGU1SQQFEmUho8EfnG84QbrVIXAA4bPta_ldmAhm5Q4yZyUF0PAJqg-FcvmwhYQe2co7m0DBpTpxvdXDS3j0VNmDoiIoZ6DDCqG5R0Ybk_Ctn-b2xVX-xFUtWDobLYwugEPuwv9Bl5xfhBsEvBOVaFq0_Rnio4SfTKsrKWSa8BkQQ4bsW45PbewrFWxWf3vC4GIycv0OsCftUswQMJBQrylDOt_l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از اینکه "دادگاه بین‌المللی لاهه"، ترامپ و دولت آمریکا را در حمله‌ وحشیانه به "مدرسه شجره طیبه" مقصر و جنايتکار دانست، این دادگاه مورد هجمه رسانه‌ای و تحریم مالی دولت آمریکا قرار گرفت و اکنون که "جایزه صلح نوبل" به قاضی این دادگاه داده شده است بخاطر شجاعتش در اعلام به شهادت رساندن ۱۶۸ کودک بی گناه، توسط دولت خبیث آمریکا، این دادگاه مورد تحریم آمریکا قرار میگیرد و هیچ دولت اروپایی این اقدام پلید دولت تروریست را مورد سوال قرار نمیدهد!
🔹
به این ساختار جنايتکار چه باید گفت؟
به توییتر خبرفوری بپیوندید
👇🏻
https://x.com/Akhbare_Fori/status/2108809077883289653</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/697143" target="_blank">📅 11:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697139">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaN1_OgF992MmEvRaRUbh9cOp3sSQQadtvLFt0bDTVUPSZ9Lt7EfAuu4-8gYoWtijm3gkutGNIG-6ZT6lrTN4xPJXxKsn5KeTWIgsfvf2p7f33KqQwj_ZG-v2vlQetMZjUFkOU1bBj7ME3Fag5pvh1HLy9ARJyIgq8Oln7eFHkaK7oEkov9PiT9EAtc86J2vwo73LH35E08idqOh45Z4O0IZByhCiCDwXk-ct-OaICiYPGUS9FXO3PPImIztfF9Vf5T6UOMrQDAD09O0Y5cwFPd8PdoTracoqPr-LXVhJ7E7CVAYfPZjP3SwAiiP35uDRF02IAfVKEuLokO9ps--Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ad75788f0.mp4?token=NxSQnBV3oNhgsT--BYkjeu8-zKFpEIiK4HERSamDKzKHSGn9Hw8phKPo8cYSzZnhvE6i6TLRfIhCZJ1Ak6UpPpNspdtRnIlahYzXSlNqMjYD70n49_7SLqAAQNif2jyQduvEXaddsILMYQtYP5CNGUASKCTWky3nOHJ-2R5tfbnZFO65bqQ9_oE144HDQuZOH-14Ef33SkkSIxHjYMpwKufTVVWPjrWwAMf9Xb_5jbVNL-ITLfspRHSRMB00vqrixZGsKwEaWuHoRjhMQCWAMBLxxZWoXMittRoBPdKue03c4KSTEimw8MWEeJvETfYVa0_3x-lbTqYw5WMqpocKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ad75788f0.mp4?token=NxSQnBV3oNhgsT--BYkjeu8-zKFpEIiK4HERSamDKzKHSGn9Hw8phKPo8cYSzZnhvE6i6TLRfIhCZJ1Ak6UpPpNspdtRnIlahYzXSlNqMjYD70n49_7SLqAAQNif2jyQduvEXaddsILMYQtYP5CNGUASKCTWky3nOHJ-2R5tfbnZFO65bqQ9_oE144HDQuZOH-14Ef33SkkSIxHjYMpwKufTVVWPjrWwAMf9Xb_5jbVNL-ITLfspRHSRMB00vqrixZGsKwEaWuHoRjhMQCWAMBLxxZWoXMittRoBPdKue03c4KSTEimw8MWEeJvETfYVa0_3x-lbTqYw5WMqpocKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه
وقوع گردباد سهمگین در ایتالیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/697139" target="_blank">📅 11:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697137">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
روایت برخورد با یک باند مهم کارچاق کنی در قوه قضائیه
🔹
کارچاق کن‌ها برای نفوذ در یک پرونده ۶۵۰ میلیارد تومان مطالبه و یک ملک را در شمال تهران به نام خود کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/697137" target="_blank">📅 10:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697136">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876f6f7880.mp4?token=dj6W8pIKys2_P3gs0VzHcKIrp6bcK_4hokzlEfFY12dnLP4f1T-taCF_uVh8PHM3Hv9gGQvf2ckVFlbqjCTNO_GCqW6gHI_SQzokMbpAPWxNNoX2h-3TLhQXha4dunOF67ybRbjQW_ibjONUWsn7qZmJRkZxPiMGVMUh-Bcz99nq7rYW_w5eLZolBHG1HwIuBxnBR_Yi_Fen2YNdV4yAXLJ5tlM4uRvee1MHuwCC69VF4wGmdIbZa_QMfwAPZuNuhZjrgVSQrFxgjr5Diz5Nqb0spm56iPZ2YboBYSAFaKf8FU1_lDy-nJ9kssnQmYZBZMsG8MisxHJ-u6WeLwzJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876f6f7880.mp4?token=dj6W8pIKys2_P3gs0VzHcKIrp6bcK_4hokzlEfFY12dnLP4f1T-taCF_uVh8PHM3Hv9gGQvf2ckVFlbqjCTNO_GCqW6gHI_SQzokMbpAPWxNNoX2h-3TLhQXha4dunOF67ybRbjQW_ibjONUWsn7qZmJRkZxPiMGVMUh-Bcz99nq7rYW_w5eLZolBHG1HwIuBxnBR_Yi_Fen2YNdV4yAXLJ5tlM4uRvee1MHuwCC69VF4wGmdIbZa_QMfwAPZuNuhZjrgVSQrFxgjr5Diz5Nqb0spm56iPZ2YboBYSAFaKf8FU1_lDy-nJ9kssnQmYZBZMsG8MisxHJ-u6WeLwzJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط ده دقیقه زمان لازمه تا این لقمه‌های خوشمزه رو برای بچه‌ها درست کنی  مواد لازم:
🔹
۶ عدد نان لواش
🔹
۲ عدد تخم‌مرغ
🔹
۱ استکان شیر
🔹
پنیر پیتزای رنده‌شده
🔹
جعفری خردشده
🔹
کمی نمک
🔹
چند برش سوسیس یا کالباس
🔹
مقدار کمی کره یا روغن برای رویه #آشپزی
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/697136" target="_blank">📅 10:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697135">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281f42eee8.mp4?token=sq1-MlI2AAgEqLtpVl1Z3f_vduczsDqEIWepnmdJlQxjAzWkkFlCWkDWaTf2604jbcOw0w5ZtmXFpDIA97bnpKjsjoHVvCX95aeWY7g37AU4YwRjglVz4LE-GMIkhpcoYamOKR0SjmllI2Cz3Z9bAVYOj0p78ak-F9xsMPiihlWuqeJu5NWqnLr3NdA2BcpUANGaQJZ6rdwmQ4z9X-PznHUZ6h1CvA4wHmWbct8WLiVg0P7JRBy3vk4P7sTEMFIs3zCB4vVja4Nk0laOcc78xH_qKzD5_ibalYejdxhgYK8nlEuKsZvoQUgNA1M_jtHZAu5oh2_GFoSQRetcVQUzTT7MpxqWqTIfI2crgbC-ovI-hMgN3ZfBmiFbqgB6j-jhOX-V5VuXgWg4v3Q6a5wi3EK3dq259pm7LAFb5lHFZDRmOdWbZMZHs_2MirXZ4KZlL8icnQA18qbGkh-iiB1SCHbgRum3p2cUMJdrLlEnmrE4VNrH0Af0nv3fNwRD_eTNcMgqr135odfMtTygS042z1bG__kImI_I_NAQ2g6RvRJM_hBavcdnxHHkq5jj0rA_HQ3QwUt0HzKSFakSlDRPtCBBFjAYap6KeHtY7vbiGr8FDGk0oHOQHadwoDt-SqsXPPgwYrFbD8W539z07jf1JWkHbxpSrLG1vHuy4YR6mbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281f42eee8.mp4?token=sq1-MlI2AAgEqLtpVl1Z3f_vduczsDqEIWepnmdJlQxjAzWkkFlCWkDWaTf2604jbcOw0w5ZtmXFpDIA97bnpKjsjoHVvCX95aeWY7g37AU4YwRjglVz4LE-GMIkhpcoYamOKR0SjmllI2Cz3Z9bAVYOj0p78ak-F9xsMPiihlWuqeJu5NWqnLr3NdA2BcpUANGaQJZ6rdwmQ4z9X-PznHUZ6h1CvA4wHmWbct8WLiVg0P7JRBy3vk4P7sTEMFIs3zCB4vVja4Nk0laOcc78xH_qKzD5_ibalYejdxhgYK8nlEuKsZvoQUgNA1M_jtHZAu5oh2_GFoSQRetcVQUzTT7MpxqWqTIfI2crgbC-ovI-hMgN3ZfBmiFbqgB6j-jhOX-V5VuXgWg4v3Q6a5wi3EK3dq259pm7LAFb5lHFZDRmOdWbZMZHs_2MirXZ4KZlL8icnQA18qbGkh-iiB1SCHbgRum3p2cUMJdrLlEnmrE4VNrH0Af0nv3fNwRD_eTNcMgqr135odfMtTygS042z1bG__kImI_I_NAQ2g6RvRJM_hBavcdnxHHkq5jj0rA_HQ3QwUt0HzKSFakSlDRPtCBBFjAYap6KeHtY7vbiGr8FDGk0oHOQHadwoDt-SqsXPPgwYrFbD8W539z07jf1JWkHbxpSrLG1vHuy4YR6mbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین افرادی که تونستن با اعضای اضافه روی بدن خودشون به دنیا بیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/697135" target="_blank">📅 10:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697134">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd722c03bd.mp4?token=fx-qAUJwRMghi9mRASBZUdbC0zoeLYQ0i9tgSA8xF3V45UT31Hg2xwv26mtGrcF4qHJDV40-8XZnCI7rakjzCTv3Z5Nsg_iA9pKiZvBs_knoW5VxjMxkU5Js1oXcTf6D2h1IExQyTBa7ltvYaSDlbaFxcUI3ClWPyPOGBaFU0NMlkAQcr2gZCNnyZJ4CFsB1LJwsGa9OougxK6_DlKPQmoFEkGtNj2HFfcbXQz7EyqRPSraLWL00uEHq9focnwPsJHMtT0Sb7e3TK2O3nIhiS_mRfxnr0NJrwHoa4VfgDpLVRHCcrQfM1gm5eD7d9iQyqH_Sn6j9PMqoKPHfW_n9Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd722c03bd.mp4?token=fx-qAUJwRMghi9mRASBZUdbC0zoeLYQ0i9tgSA8xF3V45UT31Hg2xwv26mtGrcF4qHJDV40-8XZnCI7rakjzCTv3Z5Nsg_iA9pKiZvBs_knoW5VxjMxkU5Js1oXcTf6D2h1IExQyTBa7ltvYaSDlbaFxcUI3ClWPyPOGBaFU0NMlkAQcr2gZCNnyZJ4CFsB1LJwsGa9OougxK6_DlKPQmoFEkGtNj2HFfcbXQz7EyqRPSraLWL00uEHq9focnwPsJHMtT0Sb7e3TK2O3nIhiS_mRfxnr0NJrwHoa4VfgDpLVRHCcrQfM1gm5eD7d9iQyqH_Sn6j9PMqoKPHfW_n9Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیراهن گلر PSG در دست سنگربان پرسپولیس؛
صفحه اینستاگرام تیم‌ملی روسیه ویدیویی از تبادل پیراهن سافونوف و نیازمند منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/697134" target="_blank">📅 10:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697132">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
مقام ارشد امنیتی ایران به تاس: برای مواجهه طولانی‌مدت با دشمن آماده‌ایم؛ در صورت درگیری، خود را به خویشتن‌داری یا محدود کردن دامنه جغرافیایی جنگ مقید نمی‌دانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/697132" target="_blank">📅 10:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697131">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_n1dX-KjYIWXfD8Vc0ClKfBUFVD1A1uMoSQPqKzSGRamgXOf746_ig52Iyo_LWIxschSDC83CNNKJrsgH00OA-xGnzhicP8xZJBmhTo1E83vrzfks4vlrPmnGH-tn-H0V93kbuTnZZ3zte0FARZJS0xD_a_SPFRr3mskJLpfMeDgWHBQWw6kTw1JOmBWyY4FIS8H48dz7l3BekxugdoEawb4x-sdalomcnjJ6c-U56-rwf8cGg5qto3mu_zng9qnl84e9DR0pzJ7MnmE2u6myC8enu53owUnKa23kAFWm5XxXMOtha-aWKK0ae4nGnO_0hrYs_fzJmBEuVFvbcFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/697131" target="_blank">📅 10:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697129">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
رئیس سازمان مدیریت بحران کشور: ۲۵ الی ۲۷ استان ما درگیر پدیده ال‌نینو خواهند شد ما بدترین وضعیت را در نظر گرفته‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/697129" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697128">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFes3G4B5wDAyrCQUElWwr-z8qaVfUaq_HGMu_c1iWltChNsqckH1O99T0UBlNvRLPfr0dw7qmVYg95sSPGVJp0Vtq8HwdW4mg7cC2bYhECrF9BzZq-TW-dQALXG_3BhVW-zzA5dVoqZ-q8gAHpR1ElrELqfNBjLeAsINjCeBW4D5lSmRIK88Zs0cenFsEiYw9NZtEUZ3TWbPnlRO_eWV_8y3Ly0FO9_z-HZFcXsF3FU8XTxl32J8ERzaX9OL6Gzvgvws52JdnXM4ZLhgHVwSum81zFC4MvroUVqoYptHcnTNV9xAmdbQHS5mRSR9sSdBnrDIhslLd_d1PzmfaDdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/697128" target="_blank">📅 10:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697126">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b9c829586.mp4?token=hjTNBJRGHxGU2ApUssXis1e5wKz2zt1nrPY8M7ic1Vp9B0Y1nxNyltkf6ctycZhJOh87x8AsZs4Sg5HR3Xmw26LbLjfyx5UBVwI_6QhhvtX7Z_CKfd249iHH0v9_YGSqvfl157SxoLQ0DiQ_Y0LATCAGXUZsmzjRj9i44qrb3xfwejFO8N7PcqWQGodpJDPAKs2-_xkAurubhdk_Q9s-hZFxhCJLneTJ5ePntxvpiRPCt8SmagxS0ycHuzSYcT07sTsDmzdPhoun1vApNnL4DMUljJzQXJW5_ZiHggvxVheAohYtFcnE-wyAbvHpYxWn8UdO2RVuwdFd-dm9RLmmjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b9c829586.mp4?token=hjTNBJRGHxGU2ApUssXis1e5wKz2zt1nrPY8M7ic1Vp9B0Y1nxNyltkf6ctycZhJOh87x8AsZs4Sg5HR3Xmw26LbLjfyx5UBVwI_6QhhvtX7Z_CKfd249iHH0v9_YGSqvfl157SxoLQ0DiQ_Y0LATCAGXUZsmzjRj9i44qrb3xfwejFO8N7PcqWQGodpJDPAKs2-_xkAurubhdk_Q9s-hZFxhCJLneTJ5ePntxvpiRPCt8SmagxS0ycHuzSYcT07sTsDmzdPhoun1vApNnL4DMUljJzQXJW5_ZiHggvxVheAohYtFcnE-wyAbvHpYxWn8UdO2RVuwdFd-dm9RLmmjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از زلزله ۷.۶ ریشتری در پاناما
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/697126" target="_blank">📅 10:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیوپنا(پایگاه خبری دانشگاه پیام نور)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxLmkfBQ7-XmUpgjwd1YY83asXhIjQjpVj4LTmoLI3umJBtigmlTS9-s3xOOnjDXXiAI26QvUMeQTwIgpb_qnlbUIehvVBucvuAEnaBZvlUAhZ-McRGCj-0aCKh_CBcB-TwP530JU5G9eQQvxxXaM9VF7LvxVnUH6qIn5DzWOOtlCRRK-TCFlwxP0yTnny4eTgK5cbyT9rv12LX9wNsE_k-lloYqI_aXvdtEDt-5vLp_ne2VwIihIpQizhoOX14k-Ulw8c2vfeWRiYOYXlborK4FjLjIWePXjQqV_e3Jv569J0dbxN42WgqM-4wAGm0H4ZXQHye_XH_8Yi8DEXa6bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
یه فرصتِ طلایی؛
📌
هرکجاے ایرانی؛ تا دیر نشده؛
✔️
گزینه برتر و انتخاب کن؛
▫️
انتخاب دلخواه محل آزمون
▫️
کلاس‌هاے حضورے و مجازے
▫️
وام‌هاے شهریه
🔻
ثبت نام، تا ۱۹ مهرماه تمدید شد
🔻
سایت سنجش؛
Sanjesh.org
┄┅┅┅┅┄❅
🇮🇷
❅┄┅┅┅┅┄
اداره کل روابط‌عمومی دانشگاه پیام‌نور
@upnanews1</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/697125" target="_blank">📅 10:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697122">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8b5isC_XB3bbq-bMo3TimQrFdRJjVBoQVLCJhZ2MrqsFfwKzs2teiEjzIm5Rirhp5UNsWMtR3iBJ4aEe6VnFSsjNMYYKO-kIRr2yvUIcKo24YKlwXBlJBn-nnpO-VQrrzjG46H1CCCqRYeWAV0bDOuu6GLcZu-WKo7oObMHVhhNGxTEEECdL88Dd7ZJkdbTEGpTH9kP3Sod8md-TEDffynehoyJlASGZGzDfkLJeq5t88edrS47yZpLcWUNAnE_AS_57Phui63J1zuc6zbzvm7LIf65V-aXGFB8X5CiafVfe4ATeMCba8KIlq8lniau9cIlQT6j7KEtKNU1NfeW6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای کامل کدهای حک شده بر روی طلا و نقره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/697122" target="_blank">📅 09:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697121">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzICpl_VOaxB0pm5ZVK3Ectt-7J-MhUjrfj9kfhzFZdSsEK2CtEpeVg7pxTq_BKSw5cpmpnPOoBW4IwgjmuyOMu1YDVOvZBA-5zwlcF4bBH6ezuGgKMYjNvaH7TW8-SLC8r6HvH-2JVLP12MXMNk-WpkEGqnrQ9Lo7CvvHf7eoqACNalStd_IH9lgm7jdqXehFezf-FbOFB1ZItLwcVL3d5ua3L2bd_GKwBkR3WXj_sN9sFve5HOmly9z15nBU7rD7TUFx0j1KT4Q3qjynHHDoGWb8kltI2yk4Tqkq3v6jOIxZJY4z2rSoL6OSw43iOJaK6irvOOUhGFF4zzZBDcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ، کیتی زکریا را به‌ عنوان جانشین کارولین لیویت در سمت سخنگوی کاخ سفید انتخاب کرد
🔹
نکته جالب درباره این خانم اینکه پدر پدربزرگش ایرانی بوده و به ایتالیا مهاجرت کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/697121" target="_blank">📅 09:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697120">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: سوابق تحصیلی داوطلبان با تاخیر به سازمان سنجش ارسال شد/ نتایج نهایی آبان ماه اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/697120" target="_blank">📅 09:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697119">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeMZ3jlo6B4WlU-07VkUpuzgNkQSKvQOc23AEuNihyItFwTYV95uDQsRlOw9h7w1CrMxh1rYhIMukxLPR50yMgzZKwgaIDe4GMygzDKWvKcPZ3sTWJbG-alzyUpdqUCu1yH4YE0HpjllZAFXxE1Lt6Uxmf85q6fzjtyce2JO4BU3eiKgAuqITQaRu0L7Whd2ZM3NA4hIt3-j2cQdaVdFenNZRHal5boifDaOkTDfMZyKqajci9cOXqOxhh09oHc5hG_hTA4NDxybx1Lkxtp1P9C98YOs4Zf2FLMdVixMV8calTMyUGJgexMDXhUst-6V4ywzzMgWsnYFd57CSvV5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دوباره از آرزوی خود برای دریافت جایزه صلح نوبل گفت! #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/697119" target="_blank">📅 09:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697118">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a448627028.mp4?token=mMH4CtAoUVKWfo8__q2NAMalAoiaJM44DrRDf1gIqIITYYYOdCS6jD5j4cXuZcsBM-0xEHevuAjo-V17wAoo0dSVz8R3YxAefE1BgwgjQJSz8spkO4KHP5mIcRv8w75eTIUjWQan27oZgrKJM3Or14UQzaxAeZGM0nnDJf074h5bET6taIeTj6VjM1pB0WJjavJst-FG6_-mccuyf_sz8bwtg2Gz54Rc7WwZuCOQtdWgiz4DY1NetVjPDy_8RabXFaj5tS3GIYYMVcbnNZK_Jzn1qvh_G7ofUpvb_uhQ5pHZojYcnwhxW1DC7BwYTHes9Qj7r4fSpPVoQo1ZWdBgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a448627028.mp4?token=mMH4CtAoUVKWfo8__q2NAMalAoiaJM44DrRDf1gIqIITYYYOdCS6jD5j4cXuZcsBM-0xEHevuAjo-V17wAoo0dSVz8R3YxAefE1BgwgjQJSz8spkO4KHP5mIcRv8w75eTIUjWQan27oZgrKJM3Or14UQzaxAeZGM0nnDJf074h5bET6taIeTj6VjM1pB0WJjavJst-FG6_-mccuyf_sz8bwtg2Gz54Rc7WwZuCOQtdWgiz4DY1NetVjPDy_8RabXFaj5tS3GIYYMVcbnNZK_Jzn1qvh_G7ofUpvb_uhQ5pHZojYcnwhxW1DC7BwYTHes9Qj7r4fSpPVoQo1ZWdBgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال شده از حضور یک روحانی در تجمع که شباهت زیادی به رهبر انقلاب دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/697118" target="_blank">📅 09:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697117">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه نوزدهم-</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/697117" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه نوزدهم؛ تنها حمایت‌گر
🔹
سالک باید در نام مبارک المضطر، دعای خود را صریح و شفاف خدمت صاحب‌الزمان ارائه دهد و طلب دستگیری کند تا به آن قوت بخشیده شود.
🔹
اگر انسان‌های ذاکر نام‌های خداوند را در هر کالا و لحظات زندگی بدمند، ذهن‌ کل به سمت نور حرکت می‌کند.
🔹
حکم الهی امروز بر همدلی، دوستی، اتحاد و کمک به دیگران است و افراد باید در نوازش و محبت الهی قرار گیرند تا عذاب الهی برداشته‌ شود.
🔹
امروز زمان تسویه حساب به خاطر خشم و دلخوری‌های قبلی نیست چون در شیوه‌ ابلیسی، نمی‌توانید به آخر‌الزمان باز‌گردید.
🔹
نور نام‌های«الوال و المتعال» در وجود انسان‌ها رشته‌ای از محبت ایجاد می‌کنند آنها را در محافظت فرشتگان قرار می‌دهند و به آنها توفیق می‌دهند رسولان حق باشند.
🔹
نور مبارک «الوال و المتعال» بر سرزمین‌ ایران تابش می‌کند و با ورود مهر و دوستی پروردگار، تقدیر این سرزمین را در جایگاه برتر و متعالی رقم می‌زند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/697117" target="_blank">📅 09:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697113">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ExPQdMdgCk8xXmALs4ahYpLDazknV8mOnwL6RRuSKtJUZWH3AUW8JVZn0RDdV4nQGz0TnmGrxIipMMyt0A_gIEh3-FGiz7O8ZfFf4sZuW2vKiX2WncjgJGqaJYOdFVLktlRRP78SPbqw68w1uQ6lxBuT-ilqjpAAaAkK7JCkB4-BtW6oUuX53Q6tX9Ipgp9h0d2KNwusBqz-pHiaAK9uVWXPDKV3CymC_hLz-9t79cfKn_MamDTzRWMwyIEzg87lxdOkKVXkgnzeGRh1V2kV-6SwIpdusd_pmkY-GawH1ui3sLvnvaKFlPGKq2Gxt_af-aT0XeEtoP_k8vMPVaprQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AojLv6XeuoqPL6zTbgvcYdIo5VVvo3AxiqC7-GqGrn5WoVzOfcAJ5OLkBVoohsMYNvtxmFt5rw5ZCaY6RDA_Uo7_1TbGzsqA_PHzfonrzvTGCHdPhPPguhwdFepTWHg4HmP_1IJamMfdXe4HaEONAtdOKWgUphVip-lqoPgImL1scHFQ8PFbME9ef9C_t5CdYaHY_XlPtU5XInZDMDuFOTJdev6LVTnjEJGfB3n0KI0x65KN4-baOmcWtGmSdw2XQhz4Rv7j4oLeBjUXfdeBG-a0S2YMB-qaNCuRKlk8W1ZdbJaGDLbIq47dCXf86cQUuxbwF1CQSlNo_pCL2faETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BoVDrg3cpub9O2aLFUno23DDSA7ZhWurheaCMsd7qlJ1b31kHQw3HQjH3eTHPDpFLHgT7v-dB3fi3_2kERLSY0km216ri3d22swMaBvY_BzQBd9Tqq3DX9C7IQw7ARUSIKZG2OF5wB0z7nH-h29CJpFy3msP1Chcfo_e1V5aLype-TJVB7ErzMCewPSMqX_FMA8IgHJ-XeK78TDax9JuZcMj1tTcdzdTxl9IfIsXaYU2DTJLAtAJjc75ZLUn5n2ipOJ6lO3mR0E4ERNyv_J3IgzxCupUD4VToDYed0-_XrFBBQYvJtKmgIyJ5fDapYULiii_fZ5CNmovELKkLBrQRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گاو دریایی، مهربان‌ترین حیوان دنیاست؛ مغز آن‌ها قابلیت تولید خشم ندارد
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/697113" target="_blank">📅 08:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697112">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdc8ffee1.mp4?token=V65jLKCVO1fxWkbxVXS0Cj5O3jdD9WaL6kBQkz5yR0kau0xwmQ0ryvUF_HIWTNgQviK36vLMF4im4wmiNCw9glNbX8_QXkD4gIpmGe1ZS1bs4pLlNdaUGe6RoQshHvrgXBUNS_rsgkNTlNviPkXTPT1trAPX8_ZJLHyzBQtw98wc2Pk90wRfjfwP_pP7o1Z6q2etIgeR-AXWjExLuCapdADPDJj-YaMuYYDOH8WES1VTxtPxy69Tshd1EmSvLjYXzBiG1xLjm9EmLsvf35ctM5FboOIEHjjA3I1sRaLZSTW3w8w3kUlD6POlmYGP2L6QobfT-xVTk0QEUPqHpss25Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdc8ffee1.mp4?token=V65jLKCVO1fxWkbxVXS0Cj5O3jdD9WaL6kBQkz5yR0kau0xwmQ0ryvUF_HIWTNgQviK36vLMF4im4wmiNCw9glNbX8_QXkD4gIpmGe1ZS1bs4pLlNdaUGe6RoQshHvrgXBUNS_rsgkNTlNviPkXTPT1trAPX8_ZJLHyzBQtw98wc2Pk90wRfjfwP_pP7o1Z6q2etIgeR-AXWjExLuCapdADPDJj-YaMuYYDOH8WES1VTxtPxy69Tshd1EmSvLjYXzBiG1xLjm9EmLsvf35ctM5FboOIEHjjA3I1sRaLZSTW3w8w3kUlD6POlmYGP2L6QobfT-xVTk0QEUPqHpss25Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی ترسناک از امواج عظیم همراه با رعدوبرق که یک کشتی باری غول‌پیکر را ناچیز نشان می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/697112" target="_blank">📅 08:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697111">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d59d8cdb.mp4?token=eM0NOzYYF3Ocs_BukYV35HjmVcsJg-miitea39FxaVEDdGnqqa2r1w24hE496cCfOYRy3adx-I-6FTBdp7vVOTL81AEnpUYfxJXxdtcIfT-mvd_baS3DC5YKmL_DLEHNqjYEFGEoMWeR1y9rJzy6JKvyxbJGmqLWrHTnmlxPxaABeRiOaiASFivYIT_DBYGITwmGrIVCSNDrhRGS8YKF0gxehNjK765-VT15A4RkLNF4H_daqltXvc672yR3NVPWqQP-Y3pJld6N2BC1ecxpiiWJ_qz9X4TA3ScwQHGhuNbAzkp5q7tpYl95SFK5tb2LQjQXZ9xeJxSSgQ4H8CcXnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d59d8cdb.mp4?token=eM0NOzYYF3Ocs_BukYV35HjmVcsJg-miitea39FxaVEDdGnqqa2r1w24hE496cCfOYRy3adx-I-6FTBdp7vVOTL81AEnpUYfxJXxdtcIfT-mvd_baS3DC5YKmL_DLEHNqjYEFGEoMWeR1y9rJzy6JKvyxbJGmqLWrHTnmlxPxaABeRiOaiASFivYIT_DBYGITwmGrIVCSNDrhRGS8YKF0gxehNjK765-VT15A4RkLNF4H_daqltXvc672yR3NVPWqQP-Y3pJld6N2BC1ecxpiiWJ_qz9X4TA3ScwQHGhuNbAzkp5q7tpYl95SFK5tb2LQjQXZ9xeJxSSgQ4H8CcXnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی چهار بار، این حرکات رو انجام بده و با قوز کمرت خداحافظی کن #ورزش_صبحگاهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/697111" target="_blank">📅 08:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697110">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
انتخاب رشته متقاضیان رشته‌های با آزمون دانشگاه آزاد شرکت‌کننده در آزمون سراسری تا ۲۴ مهرماه تمدید شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/697110" target="_blank">📅 08:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697109">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd37e68cad.mp4?token=eB8c5pDqiOdMmUmriXoXQsjQGBWzHMWqolz0cnxf5xhjQRNKMEKv-P7hAzIXqV-xnHCnLOTS0sW0nbHpqJEKZkeJ-tzL0cgiMLP_LKHtjCOGp9lTXa5T19lNSi30FxTbxldennD5aiVMnjeawDFolIv0WnborBGnL6hbTDJXByg4FIAiXx1wWiJ3FOSL0Yja7O5U0QmLBg4ipVQZUoOZKTyPMlkoD66NC_S-SO1NAxW-7H-_eQKec18n2LviqaIUBZRQokECVR3r2BrTsX3AVXEylndKtpnIoFCf4ZzK_0Rn7UYZlqZHK6wlxfF8LO-SQO0qFqT46WRqk2Y6NrEPlampL0OYjVa2KEzeMR_Ot6mfwxCtaIxNEmu5y2xBMRGbSUA7B-s8sYiCrhzaIw6wqgBNe0ftuQrZUYgHU2-jCRNg13n2j3eE9rF1dsA_gGhW5gTqBbvpbGbVa8IeovFDI7-PnSgmPYsukFd-Qcmex9CrzQjLjyhWgKZMqW-kChRjE1azndgKpcs7c2VU7U75L6bMexuKYoID8u0u3KmT9JZbMZlgrcF5ufC-EekVun8vkKVoWK7QbKaM50FMuU-82tibVX8Z8TaEotzcISYw7tlGb-vHdFz-qxsO-xrS7KvYgaiuzOq7NYA6_uRhmVpH5ekZpeDb2c1ylv9sTWOr1Ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd37e68cad.mp4?token=eB8c5pDqiOdMmUmriXoXQsjQGBWzHMWqolz0cnxf5xhjQRNKMEKv-P7hAzIXqV-xnHCnLOTS0sW0nbHpqJEKZkeJ-tzL0cgiMLP_LKHtjCOGp9lTXa5T19lNSi30FxTbxldennD5aiVMnjeawDFolIv0WnborBGnL6hbTDJXByg4FIAiXx1wWiJ3FOSL0Yja7O5U0QmLBg4ipVQZUoOZKTyPMlkoD66NC_S-SO1NAxW-7H-_eQKec18n2LviqaIUBZRQokECVR3r2BrTsX3AVXEylndKtpnIoFCf4ZzK_0Rn7UYZlqZHK6wlxfF8LO-SQO0qFqT46WRqk2Y6NrEPlampL0OYjVa2KEzeMR_Ot6mfwxCtaIxNEmu5y2xBMRGbSUA7B-s8sYiCrhzaIw6wqgBNe0ftuQrZUYgHU2-jCRNg13n2j3eE9rF1dsA_gGhW5gTqBbvpbGbVa8IeovFDI7-PnSgmPYsukFd-Qcmex9CrzQjLjyhWgKZMqW-kChRjE1azndgKpcs7c2VU7U75L6bMexuKYoID8u0u3KmT9JZbMZlgrcF5ufC-EekVun8vkKVoWK7QbKaM50FMuU-82tibVX8Z8TaEotzcISYw7tlGb-vHdFz-qxsO-xrS7KvYgaiuzOq7NYA6_uRhmVpH5ekZpeDb2c1ylv9sTWOr1Ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رهبر شهید انقلاب از نشانه‌های تغییر نظم جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/697109" target="_blank">📅 08:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697107">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377d650d8f.mp4?token=AgiljnhXiZQbKTczlyaEkRxlWFKnW5KUFf3_U0G6GzAcmCaruMKUtunXV00VFvhcPXiwPDsBtTmyTYVMvkz0naUSv1PZVCAxlt5sPA75fUHSoYICHY-95uUaZkSZ5r1-esGfUFUMG6Ek5m3J3NaHqd_fcW13WhwG6LiljMksH3FUspigjnZLzUuVczDBn6fwvifqeQzbdcVozKOqm4KYYWRTwEFs2qpg5YBW2U9wuPY2Rts5tQD2kGXlVuCme6-ixwpee7-JBnzg6Qh20s1OUdlp3NBdcKybObtUcnnzzV6mr69dWCDrzKyvZw3ImBFb0o5DRrO9pOnzj23UcgWLvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377d650d8f.mp4?token=AgiljnhXiZQbKTczlyaEkRxlWFKnW5KUFf3_U0G6GzAcmCaruMKUtunXV00VFvhcPXiwPDsBtTmyTYVMvkz0naUSv1PZVCAxlt5sPA75fUHSoYICHY-95uUaZkSZ5r1-esGfUFUMG6Ek5m3J3NaHqd_fcW13WhwG6LiljMksH3FUspigjnZLzUuVczDBn6fwvifqeQzbdcVozKOqm4KYYWRTwEFs2qpg5YBW2U9wuPY2Rts5tQD2kGXlVuCme6-ixwpee7-JBnzg6Qh20s1OUdlp3NBdcKybObtUcnnzzV6mr69dWCDrzKyvZw3ImBFb0o5DRrO9pOnzj23UcgWLvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های تازه منتشر شده ظریف وزیر اسبق امورخارجه که جنجال آفرین شده است: من گفتم با برجامی که یک جای بدی از بدنتان را پاک کردید، فردا بینی تان را پاک می‌کنید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/697107" target="_blank">📅 08:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw6Fgfgb7F1SIpSTchsPK6t8vrregK89bfpNvH6n1rmHdOeU1zCemZYi2NMdpBOm-tfAclZ9G8N_3hnO7wUzViJRrqXRevW5xTq5RWJgQTk4igzEIoNjwmEjl67HStD7nvC_KHSuOIf2Cm8zPPhKO-mi6038j6NV1yhEeNuKV4jpGYnME7CsBIApJBnrkjkxcwB50Vsin0GAAvZgYyUrteyIuO8GAeq308GKeKcTyz6H4SmLH5j-NPRqb61UVoiQqISZIJuiqYqnBpOKZKnfPCMT2vHdBdqmlgXRp9bSa6dBK_7Pzon0zCHG_nMPznMiYEsdJDnTuv5FPRTrk47fHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رابرت پیپ‌ استاد دانشگاه شیکاگو: پیاده‌سازی تفنگداران دریایی آمریکا در یکی از جزایر ایران، بزرگ‌ترین هدیه‌ای است که واشنگتن می‌تواند به تهران بدهد
🔹
آن‌ها عملاً به اهدافی ایده‌آل تبدیل می‌شوند؛ درست مثل ماهی‌هایی که درون یک بشکه گیر افتاده‌اند و پهپادها و موشک‌های ایران می‌توانند به‌ راحتی آن‌ها را هدف قرار دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/697105" target="_blank">📅 08:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0925073180.mp4?token=OCnNm8M4xywvdPFDjkFkeQ1GgyUGEhjR2Jv171GS0PUXQg8I-zGb3WZtyF8nxsSKIPN9nmzc9C1btMs3YJLFXPxVAmawkt-Hir4MuaRZIuHO2USvDeUXKJD89HQ8okIAJPQDA8JVMppZiAvf3HRwP36KqTMhEFoocWn0nX8moV-z6Siqnw5_zFY1omNbvK5ZEQTOxYKrn6lAplopq8UvLwfmdpp6qM1WBgPWEHC5kWFzjmlr-fOdwt-9gIN64sefEAA9eqAw2OeR7v_SkSERmH6jZF5s--bTz7qjcxtwBEFkeXdedv72mZLj4CG_08-TLMF773zPNUTcM04WLgIdcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0925073180.mp4?token=OCnNm8M4xywvdPFDjkFkeQ1GgyUGEhjR2Jv171GS0PUXQg8I-zGb3WZtyF8nxsSKIPN9nmzc9C1btMs3YJLFXPxVAmawkt-Hir4MuaRZIuHO2USvDeUXKJD89HQ8okIAJPQDA8JVMppZiAvf3HRwP36KqTMhEFoocWn0nX8moV-z6Siqnw5_zFY1omNbvK5ZEQTOxYKrn6lAplopq8UvLwfmdpp6qM1WBgPWEHC5kWFzjmlr-fOdwt-9gIN64sefEAA9eqAw2OeR7v_SkSERmH6jZF5s--bTz7qjcxtwBEFkeXdedv72mZLj4CG_08-TLMF773zPNUTcM04WLgIdcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: زلنسکی گفت که به دلیل توافق نفتی‌تان با پوتین، شما ضعیف هستید
🔹
ترامپ: چه کسی این را گفت؟
🔹
خبرنگار: زلنسکی
🔹
ترامپ: باشه.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/697104" target="_blank">📅 08:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697103">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpIVa1L4SxwCIXGIb2K4UIkop8PZSPSfpJ5V4SLoZLTdHz79TmVC1lkCs7v_IedES8ls_5JrRfuB2kEWmriuDk8cegJIIIX9UeQfdOCDKHHpLSM05iQx7KB8kYt4YCkbDJ22QnJeLFSUvW6mJXYk-f3RTn24BGmy--Pp0LQqYjdAO19g9O3TfEUMGkOo3DHr29VfZOyHHo7n-XhxILUVAxLXQkXhjK43IxJpfFSGEJM_FndlybNGEvYxJx48H5HkncEVZbTQC18lPHitINUUC6hBO7O5dfyOmyTiN1CCe6PinLUnqcrzFKthRj6727nLLtJPzsYIae65aaDVsZukFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور کریس مورفی: جنگ ترامپ علیه ایران، مایه تحقیر ملی است. این جنگ امنیت ما را کمتر کرده و باعث افزایش قیمت همه‌چیز شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/697103" target="_blank">📅 08:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697102">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ضرغامی: من دیگر عضو شورای عالی انقلاب فرهنگی نیستم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/697102" target="_blank">📅 08:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697101">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f201c233.mp4?token=BaU62YxK1S9g6E_FgbO6wG-VxZbw_BLHpAZRBPThwD-j8Tce3OJ-UQBQCJARhLnI95PE9IPr-W3_zFYRVFRikgtAR9P9CkfLRVReXEAhrgV7F7ZfMokeU6sjUk8HFW8f8OFSD2_q1Dme-n-qbR8z8MWo8qahDaCTVLnifsaF_UeUVIjqbdlcG5HzImI7w0SoASK6ZhD8Ca3mh3qoGJKUhMNrf0GAjC0D25gkxmD_wLyfkqaEnZyCgic-ueNcyiZcHS3H8XluMeRmg3OHcoRye286nVbbZtb_cTQguhyEPW9sdzzMum4m-98-l9rCEVzYZ4T7Qkhb0e4xCO3N2inDBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f201c233.mp4?token=BaU62YxK1S9g6E_FgbO6wG-VxZbw_BLHpAZRBPThwD-j8Tce3OJ-UQBQCJARhLnI95PE9IPr-W3_zFYRVFRikgtAR9P9CkfLRVReXEAhrgV7F7ZfMokeU6sjUk8HFW8f8OFSD2_q1Dme-n-qbR8z8MWo8qahDaCTVLnifsaF_UeUVIjqbdlcG5HzImI7w0SoASK6ZhD8Ca3mh3qoGJKUhMNrf0GAjC0D25gkxmD_wLyfkqaEnZyCgic-ueNcyiZcHS3H8XluMeRmg3OHcoRye286nVbbZtb_cTQguhyEPW9sdzzMum4m-98-l9rCEVzYZ4T7Qkhb0e4xCO3N2inDBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطع سخنرانی ترامپ توسط یک معترض
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/697101" target="_blank">📅 08:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697100">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56814e1060.mp4?token=iIhstFe2l6vDsanHhizeQ5Kq6yMYRW7VGum4rt54CzlMSFoE4kIqNGYDIA6plWqvM1qRg76m8njTi5VgxWy2dr8Ns5rjwwnZ7biVJEoznUwtIAh4POKOePBdDAr6c45S_iM68QB_sTMhxIGMotgSlHAARt6bKZo54h-uZ-cK-IJlGTdOzkhCCEEHmb6t04OGHanzeumlg0noI-8hLvGzcsPJmM5H1JrsJW8BlPo83fYTKGoTqR6y4T0vXtMPLMGVUeC4DyqTX207eSueQPcDYMvgY5atczxBVAPbFDxvo323e_Y8KcshpkR5dUEylWgojxtpWyFtoCJsBoL1VYwC9i8sG2B7pFI79-ljcm5DeGlcgTAKezfKTgmr32yeWgQ_uaQZyLAn2pG5OQSFJpT8KbFjBaWkkymTPxMlAmf12winP668oWWPmmHyW_stunBMygT9nOzNSS2UsVtoqGf0fcNKz7vuHPQBw5dfggtfTIjBAvBtSB1YigIn3h9uvRALfO-6xfmoSYOzRj9q2MRFlr5kl3tZQ3LmFkYHEK4imlPoZk3C5-GRalf0kd_ZlFTsImiZ4ct2guFt0-cgX3bqLlmnFiN9pLk51P8ROoO6byPXIDKXOJgx9ksFwpIx9RAyQvNdEc-rHQzeZAorOQ9dFjfSVQEBHx5klh3aa14eiLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56814e1060.mp4?token=iIhstFe2l6vDsanHhizeQ5Kq6yMYRW7VGum4rt54CzlMSFoE4kIqNGYDIA6plWqvM1qRg76m8njTi5VgxWy2dr8Ns5rjwwnZ7biVJEoznUwtIAh4POKOePBdDAr6c45S_iM68QB_sTMhxIGMotgSlHAARt6bKZo54h-uZ-cK-IJlGTdOzkhCCEEHmb6t04OGHanzeumlg0noI-8hLvGzcsPJmM5H1JrsJW8BlPo83fYTKGoTqR6y4T0vXtMPLMGVUeC4DyqTX207eSueQPcDYMvgY5atczxBVAPbFDxvo323e_Y8KcshpkR5dUEylWgojxtpWyFtoCJsBoL1VYwC9i8sG2B7pFI79-ljcm5DeGlcgTAKezfKTgmr32yeWgQ_uaQZyLAn2pG5OQSFJpT8KbFjBaWkkymTPxMlAmf12winP668oWWPmmHyW_stunBMygT9nOzNSS2UsVtoqGf0fcNKz7vuHPQBw5dfggtfTIjBAvBtSB1YigIn3h9uvRALfO-6xfmoSYOzRj9q2MRFlr5kl3tZQ3LmFkYHEK4imlPoZk3C5-GRalf0kd_ZlFTsImiZ4ct2guFt0-cgX3bqLlmnFiN9pLk51P8ROoO6byPXIDKXOJgx9ksFwpIx9RAyQvNdEc-rHQzeZAorOQ9dFjfSVQEBHx5klh3aa14eiLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از وقوع زلزله در پاناما
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/697100" target="_blank">📅 08:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697099">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
وزارت خزانه‌داری امریکا مجوز موقت انجام معاملاتی را صادر کرده که شامل فروش، تحویل، تخلیه و واردات گازوییل از روسیه تا تاریخ ۷ آوریل ۲۰۲۷ می‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/697099" target="_blank">📅 08:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697094">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
پوتین به ترامپ: گزینه‌های دیپلماتیک در پرونده ایران هنوز به پایان نرسیده و دستیابی به توافق، امری ممکن و ضروری است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/697094" target="_blank">📅 08:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697093">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420dde080d.mp4?token=u_1VXHJdamSk7WiKg2jLMfraavSQFuhZC94-GDrpy_QMJxb-4dKXz5pCbps-1eOytqBbkyxZHWmAUEBAod4yV7xOjoK1BM_COGJ5xD2BV_JXmUUHkz7mOz71FQk3qpodmSb2jsJBK1_zSJ_5J2RLbEiR5Yw-5TSREAQpANBowWC9bdXQcRFkuaHXTj8vfxZekXY9FFn2Nn5Hr9z-bDu37BEVsnDXOW0tc3uRko69FReo1V6kkVn1BHKjy-2_EutSH9XMncn1GUKQ8MqpqYy4K2LYCaO0ATERmVuy68GZV9oZ-VGT7nFOBvwFH0H9LnsL-hgrbKlO2tipfntl-Cg3wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420dde080d.mp4?token=u_1VXHJdamSk7WiKg2jLMfraavSQFuhZC94-GDrpy_QMJxb-4dKXz5pCbps-1eOytqBbkyxZHWmAUEBAod4yV7xOjoK1BM_COGJ5xD2BV_JXmUUHkz7mOz71FQk3qpodmSb2jsJBK1_zSJ_5J2RLbEiR5Yw-5TSREAQpANBowWC9bdXQcRFkuaHXTj8vfxZekXY9FFn2Nn5Hr9z-bDu37BEVsnDXOW0tc3uRko69FReo1V6kkVn1BHKjy-2_EutSH9XMncn1GUKQ8MqpqYy4K2LYCaO0ATERmVuy68GZV9oZ-VGT7nFOBvwFH0H9LnsL-hgrbKlO2tipfntl-Cg3wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلنسکی: اجازه دادن به روسیه برای فروش محصولات نفتی، به مثابه سرمایه‌گذاری در جنگی است که باید پایان یابد، نه اینکه طولانی‌تر شود ‎
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/697093" target="_blank">📅 08:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697092">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ff41a1b6.mp4?token=IIULpgBRQNSKLIK9pdpokQRBQYc29rRd7lVx9WHmVlI86BOr31zxTe2ZgXuRB6OUV8lCfJVVtNd350LZL4mHrOUNPK43tUGhJvm8-bJEhL2jw3TCpBX_Yp0LTPJSR-35BHY8vYbPe8FkQz4oUJap5ou8lkCbudY80SqWz_1TyaV79GOpkKZM-DnGnn5Y7cAqMpHe-N_UdmiD4F1LQfhKTXZ8p4Dmvk8EuBgAg6HpJjLcMshZWJ2kDKnHLZJGe108RZvf4OumsUNFi7QDI3v0luEnL9XCcGSAdhN8QDjTYoKIq21iDUo5DAtxBiYVveWC4qvWK1P-tfo9AeOadPVsvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ff41a1b6.mp4?token=IIULpgBRQNSKLIK9pdpokQRBQYc29rRd7lVx9WHmVlI86BOr31zxTe2ZgXuRB6OUV8lCfJVVtNd350LZL4mHrOUNPK43tUGhJvm8-bJEhL2jw3TCpBX_Yp0LTPJSR-35BHY8vYbPe8FkQz4oUJap5ou8lkCbudY80SqWz_1TyaV79GOpkKZM-DnGnn5Y7cAqMpHe-N_UdmiD4F1LQfhKTXZ8p4Dmvk8EuBgAg6HpJjLcMshZWJ2kDKnHLZJGe108RZvf4OumsUNFi7QDI3v0luEnL9XCcGSAdhN8QDjTYoKIq21iDUo5DAtxBiYVveWC4qvWK1P-tfo9AeOadPVsvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دوباره از آرزوی خود برای دریافت جایزه صلح نوبل گفت!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/697092" target="_blank">📅 08:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697091">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6d0c50b.mp4?token=e3Zg85_0MvrtzvOeoiIqznkWCJLAc4gZaL5mluI7Md6PIOOF3dlIiAX999bGUXQK2ELkSr11GpC0vfDIYfHrQC_5qGurjyrRxPiEJPpSeW9F99kmSRDIktDr-Vbly2Iz9m9fUYVCpjiKzfQXBGI_Qe2Ke6Jc_23h7z_GjEoz7npfG6ax6ZczBjsFhExo6DMRnlUXcV0xpsR9VfUxq_A334JtgCrwDkfjQk6XiA3xtnrx6ZEpxjuxTb6aDO8BDnu7pJ_Eh20e5OoGjmIwY-O3tBf07NsZFWh4o1GP39MAfDyuZpBbzbFHuwPSCXRq-Pi8KqrXaC2smZpOF1vuz_HRdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6d0c50b.mp4?token=e3Zg85_0MvrtzvOeoiIqznkWCJLAc4gZaL5mluI7Md6PIOOF3dlIiAX999bGUXQK2ELkSr11GpC0vfDIYfHrQC_5qGurjyrRxPiEJPpSeW9F99kmSRDIktDr-Vbly2Iz9m9fUYVCpjiKzfQXBGI_Qe2Ke6Jc_23h7z_GjEoz7npfG6ax6ZczBjsFhExo6DMRnlUXcV0xpsR9VfUxq_A334JtgCrwDkfjQk6XiA3xtnrx6ZEpxjuxTb6aDO8BDnu7pJ_Eh20e5OoGjmIwY-O3tBf07NsZFWh4o1GP39MAfDyuZpBbzbFHuwPSCXRq-Pi8KqrXaC2smZpOF1vuz_HRdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه گویی
ترامپ برای هزارمین بار: یا ایران هر آنچه را که می‌خواهیم به ما می‌دهد، یا دیگر وجود نخواهد داشت
!
🔹
مسئله ایران به هر طریقی که شده، خیلی سریع حل‌وفصل خواهد شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/697091" target="_blank">📅 08:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697090">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ترکیه دسترسی کودکان به شبکه‌های اجتماعی را ممنوع کرد
🔹
ارائه خدمات شبکه‌های اجتماعی به افراد زیر ۱۵ سال در تر به‌طور کامل ممنوع شد. پلتفرم‌ها موظف شدند نسخه‌های اختصاصی با پروتکل‌های امنیتی و حریم خصوصی تقویت‌شده برای کاربران ۱۵ تا ۱۸ سال ایجاد کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/697090" target="_blank">📅 08:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697088">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
پنتاگون آمار تلفات خود در جنگ علیه ایران را افزایش داد
🔹
آمار رسمی تلفات تا تاریخ ۹ اکتبر به ۲۱ کشته و ۸۶۵ زخمی رسید. این ارقام از اضافه شدن ۲ کشته و ۴ زخمی جدید به آمار قبلی حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/697088" target="_blank">📅 08:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697087">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crgyQN-Gf6N-HMYzdMvyAwOmGgHwl1LYs_PnU9rfdI81m1sroeu6uQBV_2IaNp_nUC8j-lqPcNrbEnhQHuexSMT1QkwXee27AV6V3VgPKb0nQPYoZZFHdwO_9OUU56DPsFQfedttxWDcA3aiXxQR4rSFGRr6VbCrp8m4AbUiF5myQrI8ZRbq005RQUwIO-_MD4evv_JSHJPnA0CHGOWcUYytD-i_ZtPQgDBVNF7bpLN1IUr0JYOQTRYVd7OBr1RsR0WRaiBdRRRsqNVJawezrizbK21S1HX_KX8KRsCVmFGcjRzGi07PyqV1mK7AFU6v9oRATRZmAf37M5Z2PP2o5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۸ مهر ماه
۲۸ ربیع‌الثانی ‌۱۴۴۸
۱۰ اکتبر ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/697087" target="_blank">📅 08:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697086">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBye6L9aKpfyYmVUj26ARoYMT8zf1N2_qWg9_PYmpY8fZjl_cK55DljnXVwKYktEmiyP9yLsitHQUfySn3bNve-SXTFsXBQQnv3-sq5ZR0ojk-NilG00MlBHY5buS-fQ8Q_0J2lEL0g2yEF5zCHUIr0Zm6P6WP_oxaxik8XAJxiOo9UwuvsvP8gbBSSz7IwIdgLdZa2IDP3SrLwbyG1G5vvrrms97ucYaJH4bwION42iIJQm85HPn3KRBMPNNdEuUPb0tlSb4qyzqAIIf5C6fotsiaFST_pKzC3qsRs4Dn2BDbEO-CJ7F0aK9_PPqeFbGnFqCraoEhlsmPyhgY2_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبری‌که همه‌منتظرشنیدنش‌بودن
❌
پژوهشگران موفق شده اند ترکیبی را معرفى كنند كه مى تواند سلول هاى بنيادى فوليكول هاى مو را از
خواب چندساله بيدار كند
😳
😳
✅
این تحقیق روی ۱۰۰۰ نفر تست‌بالینی گرفته شده و نتایج فوق العاده در
قطع ریزش و رویش مجدد
داشته است
✅
🔴
حتی روی کسانی که ریزش‌ارثی هم داشتند اثرگذار بوده
رویش مجدد مو به همراه دارد
🧬
در حال حاضر در ایران این روش بالای ۳۰۰۰+ نفر رضایت‌درمانجو داشته
به زبان ساده، موهاى خاموش را دوباره زنده مى كند!
دریافت اطلاعات کامل و نحوه و هزینه درمان روی
لینک واتساپ بزنید
👇
https://wa.me/message/F4D4OKDJSSCFI1</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/akhbarefori/697086" target="_blank">📅 00:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697085">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK9h3cXeElaUsF3s5wqv641CjLD1rHYCAEXx7eqVqMs2kD6xxtZrLou3KKb0GrosxjGygNW4lWFXcvNbXDrIVXQjGTe3noa3jno1u2mE-Qfjdn4_IpLTuREyVR8BdHXGsTmbSjy6bBIzzJ5tQLRusKJWoeH6-a_id4icgT5P5eP98lIBzTB5IX5xuIAfPZrdvCNhQGLYo-B0Guy6HZEpXFgqtWXYCyrNwCnwlbfHwNfvqZYdAxFD_-v9Xzz_AZuEKPqnvY_170g9Guvc7unA5h7_ticRBJ1D58JtXzTUQTTxaQ19SShsOsC0tG0tAuOnNLQkNo2EOcHlz4YHVXrCgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪥
✨
تمیزی عمیق‌تر، لبخند جذاب‌تر!
با
مسواک برقی اولتراسونیک شیائومی X-3
، مراقبت از دندان‌هات رو یه قدم حرفه‌ای‌تر کن.
😍
⚡️
تکنولوژی اولتراسونیک برای پاکسازی بهتر
🦷
مناسب استفاده روزمره
🔋
شارژی و کاربردی
✨
انتخابی مناسب برای مراقبت از بهداشت دهان و دندان
🔥
قیمت ویژه: فقط ۹۹۸,۰۰۰ تومان
💳
الان بخر، بعداً پرداخت کن!
✅
امکان پرداخت
قسطی با ترب‌پی
🔄
ضمانت تعویض ۳ روزه
🪥
یه انتخاب کوچیک برای شروع یک عادت بهتر!
❤️
https://memarket24.ir/product/fast/63753/180124/</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/akhbarefori/697085" target="_blank">📅 00:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697084">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff362a7ca.mp4?token=vzoTTzSM1vmlCyXSl7zJ96PubuQh1tTtgnFVUwXjHMYbc7-FKkOuier1p-tNG51dB8rRHMBe_bj6ThEOfmmrz5jiMvhRHe-ltMv4ijlszTBFG-SC3iKkGYIoLKsaMvSVClYxjw06N_d7JFENtHKtZNJKvcUwkANVLHG6nE9AWsKnZ6qb8BvhvH2UMIVuNH2vVILmRkPnz-4DjTXxWylo3Vi6aXjZDb4w81epvPnaebEdjxIhbdM8FNzQ9Smxur-8NI5ua_E5u3X8hcxSXjKwh5qXNxhddpi4xz8erKFbBoj-glK3cbJTBZ-dDWD4abENkDoMuySwwzQqX0XUu6Pl3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff362a7ca.mp4?token=vzoTTzSM1vmlCyXSl7zJ96PubuQh1tTtgnFVUwXjHMYbc7-FKkOuier1p-tNG51dB8rRHMBe_bj6ThEOfmmrz5jiMvhRHe-ltMv4ijlszTBFG-SC3iKkGYIoLKsaMvSVClYxjw06N_d7JFENtHKtZNJKvcUwkANVLHG6nE9AWsKnZ6qb8BvhvH2UMIVuNH2vVILmRkPnz-4DjTXxWylo3Vi6aXjZDb4w81epvPnaebEdjxIhbdM8FNzQ9Smxur-8NI5ua_E5u3X8hcxSXjKwh5qXNxhddpi4xz8erKFbBoj-glK3cbJTBZ-dDWD4abENkDoMuySwwzQqX0XUu6Pl3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور روی فلش رمز بذاریم و از فایل‌هامون محافظت کنیم؟
👨‍💻
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/akhbarefori/697084" target="_blank">📅 00:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697083">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بیرانوند ممنوع‌الخروج شد
🔹
سازمان نظام‌وظیفه اعلام کرد تا زمان مشخص‌شدن وضعیت کمیسیون پزشکی علیرضا بیرانوند، او حق خروج از کشور را ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/697083" target="_blank">📅 00:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697082">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0c0dc628.mp4?token=ZGxrAc95oU4lqMSR0eAbkpQR0hgnhRxRKCFza_uesLv43KDhUrUpF6JTGG8XXNIQoAisprAYd-hHhFF9H2QCk5_gXi2ani5J-70mkDge5yzYYdXPa21hy4M8v3V0bhbn4gDlZTOzkTyqQEPVquEVc-lepx4XMY_7J1abwvsU94wNPom56P0TmT01g33Xup_C2T9avewSLIR6tSrUXp3CKijSCnVwwHSThMTIYnb9WSY2_LWVcfJOqhTTJNNV4qCPrOoCvOgDZ52EhLN_R1TbqGblaU3M8BbULHEGBp5xdokGWkzaBcJg1hqrhm72JdZuiJ_-_uR7SyUarDSiCi4FoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0c0dc628.mp4?token=ZGxrAc95oU4lqMSR0eAbkpQR0hgnhRxRKCFza_uesLv43KDhUrUpF6JTGG8XXNIQoAisprAYd-hHhFF9H2QCk5_gXi2ani5J-70mkDge5yzYYdXPa21hy4M8v3V0bhbn4gDlZTOzkTyqQEPVquEVc-lepx4XMY_7J1abwvsU94wNPom56P0TmT01g33Xup_C2T9avewSLIR6tSrUXp3CKijSCnVwwHSThMTIYnb9WSY2_LWVcfJOqhTTJNNV4qCPrOoCvOgDZ52EhLN_R1TbqGblaU3M8BbULHEGBp5xdokGWkzaBcJg1hqrhm72JdZuiJ_-_uR7SyUarDSiCi4FoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلزله ۷.۵ ریشتری پاناما را لرزاند؛ آمریکا هشدار سونامی صادر کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/697082" target="_blank">📅 00:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697081">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10cb6c5bc.mp4?token=vPrbdogxbMyyFUFhekrvngxlneHQonwz_u9muVNcA3KCy3QMevolXy56zTNf50YgA6SZ-kNDcMgSHPZ7sbDyE8NZmBuakOt1RJLKA9QmAqA9gI1YkgTx1jpbXTP4AshdJVPlhWkUdy7Mp3punSlq4_xZYkkL2W--9koEac3h_8EpHuceMCxXpLx_if8bTUOeq1XjpVjSyExCynRnKPDLlX3XYh3MPinPYl73L7OsRJfvqhRMCIZJnU4tUx2KHeTZxHG0oNzR26GYpMGKNnxVl3mmf2MtCKeHHs904mYcJJnlo8sO_mrkjcfj_6g3pPvifVdND3X-pCwP7UGmDk3TIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10cb6c5bc.mp4?token=vPrbdogxbMyyFUFhekrvngxlneHQonwz_u9muVNcA3KCy3QMevolXy56zTNf50YgA6SZ-kNDcMgSHPZ7sbDyE8NZmBuakOt1RJLKA9QmAqA9gI1YkgTx1jpbXTP4AshdJVPlhWkUdy7Mp3punSlq4_xZYkkL2W--9koEac3h_8EpHuceMCxXpLx_if8bTUOeq1XjpVjSyExCynRnKPDLlX3XYh3MPinPYl73L7OsRJfvqhRMCIZJnU4tUx2KHeTZxHG0oNzR26GYpMGKNnxVl3mmf2MtCKeHHs904mYcJJnlo8sO_mrkjcfj_6g3pPvifVdND3X-pCwP7UGmDk3TIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عشق یا خودآزاری؟
🔹
با نوشیدنی داغ عشقتو ثابت کن؛ ترند جدید و عجیب این روزهای فضای مجازی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/697081" target="_blank">📅 00:03 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
