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
<img src="https://cdn5.telesco.pe/file/MmVNw1imC60hETuqpU757ZhlgTDiyd4iDODdNCq437amDmWYoU4nYDbrBjItlj9HWvXutnlx_HylkupMIsL0Cy3CFqsDQJK95s4VW9Qt36QbklsNp3-2x2D0JfGFjcCEI00jArdJe6sQ88QUx7YWF1hTeh7K9EmpiQSONaE-JJXVY8_n3lPubkuVXp7CbZwrfjR-aTSrClHUmldCMQmw0F80gHgbC6a934Vfv2nQyxxMtm-eclCunApE4ygWWJ04Njun1JpZMNIFYO4Y8TupHfjshe4qDO-Gf67aK3_fYrwC6Z32M8zlgQ5eZwwrzLkltHofrIzw-EnRtLnltfvD3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 615K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 08:43:32</div>
<hr>

<div class="tg-post" id="msg-98998">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYoXSI__zPEJdeeuZg96-q3Qu8cv4ob4AssPuykjxcpGP7tHxzazeTtS78p1tdjE4-j5aKcQWnnDay3t__60gCH8Fx-lvkO9Gkfsl_WA0hhlcrsMj8QvpOmD1CywGwdazjt_-hwPkhCl2_AyJOIMGDNtAo39mRkq8ndjfMX7x5wBoRlYke6VIRqKls1P0wmXFv_7jzH2To0g5IKdItU025AHCzfKlRb9AqYwWLrYOUCgEoX-eRUpB9hZ4W9ryEJZWuRVFStzGeF5VCoq-KDp5BYuHFIJ6DPlwHnW5auAWmezNQkGx2RpoS_9aeirsusU2WC5ZCyeeThdEbhUZ9lE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
| فابریزیو رومانو: قرارداد کانسلو به احتمال ۹۹.۹٪ با بارسلونا نهایی‌خواهد شد. الهلال و بارسلونا بر سر مبلغ به توافق رسیده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/98998" target="_blank">📅 08:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98997">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO-GlPESKAk2oG3sX-xzVRNI4YY1NbWDDCynVrj4mARlJ9C8dU1rak922Tj4U7Kcrfse6S1LvsZzkbWjsU_ynMhtKID1UPOhmne0DwrFmxPHBkZUctTUO4Yyl58NuYTkiw55vsbjkG6X1Xia4N5OpMy8NlSm16WrCDNQAuEwU7S0PNTlLT9qNC2YtdBNmJLhkV2ImQjCmG9qy00Fjpyl0bDFRGn0qo9XQ2amuBN3HmyCpV7dsUfEaSJLg2ZTSKq5s1QQriS94Uu0XDn1FDqDmFb9Bsed50kK2j0FviMyF7atWGUJZkpANokJGTzzu_MxK6piv-t2cJT_lLL_2qsLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
◀️
تو گروه D جام‌جهانی ۲۰۱۴ یکی‌از عجیب‌ترین اتفاقات تاریخ جام‌جهانی رخ داد، جایی که کاستاریکا از گروهی که ایتالیا، انگلیس و اروگوئه ۳ قهرمان جام‌جهانی توش بودن صدرنشین صعود کرد و تا مرحله یک چهارم نهایی اون جام‌جهانی هم تونست بالا بیاد.
👏
🔹
جالبه بدونید سایت‌های شرط‌بندی شانس صعود کاستاریکا رو 6٪ پیش‌بینی کرده بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/98997" target="_blank">📅 08:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98996">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805dd3bff7.mp4?token=nVW5KHacsYDoq-Runlv-k4nGoUHzCFEm8ej38kokILnGmxX1Y5WzPpoeQDvvG8KRU1KMzFPIdZxKjjKI-W0f8Zwar2v3ZD6GbmHdx750_1vAilkArjVg0vyABquXqwcWuQlHQM5ZRKu_CBD6UZColOn4g7PkGFofCewidxkdKMpCCPZhJ4o9k7L3Bucu2RdvtpmW3JLqXZZNGNL2ubzyMO62KkGPcgEe1kKV4C6MsEuHzmOsOVwEeP9qqHxq2vvYwq4_WW9AqKSaOyc02sPtrVfRrlaWDjPNACEAHsU1dIIiObclnbPrVAuI8po2rA_8caKC5ePSiFve2sF9bKaLhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805dd3bff7.mp4?token=nVW5KHacsYDoq-Runlv-k4nGoUHzCFEm8ej38kokILnGmxX1Y5WzPpoeQDvvG8KRU1KMzFPIdZxKjjKI-W0f8Zwar2v3ZD6GbmHdx750_1vAilkArjVg0vyABquXqwcWuQlHQM5ZRKu_CBD6UZColOn4g7PkGFofCewidxkdKMpCCPZhJ4o9k7L3Bucu2RdvtpmW3JLqXZZNGNL2ubzyMO62KkGPcgEe1kKV4C6MsEuHzmOsOVwEeP9qqHxq2vvYwq4_WW9AqKSaOyc02sPtrVfRrlaWDjPNACEAHsU1dIIiObclnbPrVAuI8po2rA_8caKC5ePSiFve2sF9bKaLhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
برای خیلی از پسرها، فوتبال فقط یک بازی ساده با توپ نیست بلکه پناهگاهی است برای فرار از شلوغی‌های زندگی، جایی برای نفس کشیدن و رها شدن از فشارهای روزمره و فرار از دغدغه‌هایی که شاید هیچ‌وقت درباره‌شان حرف نزنند. وقتی بازی شروع می‌شود، برای دقایقی تمام نگرانی‌ها، استرس‌ها و خستگی‌ها رنگ می‌بازند و فقط یک چیز اهمیت دارد، عشق به فوتبال و تیم مورد علاقه.
🔺
فوتبال به آن‌ها یاد می‌دهد بعد از هر شکست دوباره بلند شوند، امیدشان را از دست ندهند و تا آخرین لحظه بجنگند. و در این میان لیونل مسی برای میلیون ها نفر از مردم دنیا شاید بزرگترین تراپیست دنیا باشد. برای خیلی‌ها، تماشای بازی مسی فقط تماشای ساده فوتبال نیست‌ ، تجربه‌ی آرامشی است که در کمتر چیزی می‌توان آن را پیدا کرد.
لذت ببرید از سالهای آخر بازی مسی
🩵
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/98996" target="_blank">📅 05:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98995">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d112899bf.mp4?token=seaauUlyBXUe5k2ne8KOrKrh3tHd5gjkGnyVIZHuaN4osjOC_y2azUZS3fY_FSg5JwzMQsWl9V3-PXEpaMkVW81G-ZU_3YioQ66cw4rei65AitJgX2RQ8JJeeNyhD_3BEQa0-9zeqyGx-5l95fwp5Jx0yJV3_TyscDEuaRAFcUvlH7jsIVa1vGsIIJmwANsFKVSDbRltfJvsM5qx5GRYZALaqGk68W-9MuCCtdc96ElioTYLqmXapxVLuQ3nNR75XW0uH1RjqkYemqhebnOTZj1DlnKxj2MisPZtpOGnXn-IWWfbwbvoS5DxhAi0M1wsyRNoCqqwuI7uXN8dfY_EgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d112899bf.mp4?token=seaauUlyBXUe5k2ne8KOrKrh3tHd5gjkGnyVIZHuaN4osjOC_y2azUZS3fY_FSg5JwzMQsWl9V3-PXEpaMkVW81G-ZU_3YioQ66cw4rei65AitJgX2RQ8JJeeNyhD_3BEQa0-9zeqyGx-5l95fwp5Jx0yJV3_TyscDEuaRAFcUvlH7jsIVa1vGsIIJmwANsFKVSDbRltfJvsM5qx5GRYZALaqGk68W-9MuCCtdc96ElioTYLqmXapxVLuQ3nNR75XW0uH1RjqkYemqhebnOTZj1DlnKxj2MisPZtpOGnXn-IWWfbwbvoS5DxhAi0M1wsyRNoCqqwuI7uXN8dfY_EgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‼️
12 سال پیش در چنین روزی تو جام‌جهانی ٢٠١۴ یکی از تحقیرآمیزترین نتیجه‌های تاریخ جام‌جهانی فوتبال رقم خورد؛ آلمان ٧-١ برزیل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/98995" target="_blank">📅 05:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98994">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts_t-3jn8AE77OezH-NUFGBRwDBYUx-H_KBGvmfauHA3M_-9QTGGveChhHmr-3uRh9R4fE43LA2Py7qh8ugMHb0OAbH14XYnPDMbvhxaDD4asAMK2ITq3_Hc1xqmNxfm4ND_tC0CAT17v0AzzltBcYtgdQIAXds2AeGm2T0S5FXrzAN8uRlpC-50ziTzPu6KUldfLs8PpkXUYJn4gJiB4z-c7zAEWK-qkcxlfHIUOYyeBF9MmP0Y0V8rni9_3thtQnc0upEqJ-LxiQYQielzOL5k8JIOLgYKQBFLRFDvK3N7JtEZGIktBJt5zUbrm1AoEXJ9MkjEehleux4JWae8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎙
💥
لیونل مسی:
«من گریه کردم، چون احساس کردم که هم‌تیمی‌هایم را به خاطر پنالتی که خراب کردم ناامید کردم. اما خدا برای من یک اتفاق ویژه دیگر در پایان این بازی در نظر داشت. من خیلی خیلی خوشحالم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/98994" target="_blank">📅 04:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98993">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98993" target="_blank">📅 02:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98992">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn1z5eXfMKK2ChUj2C2lSCsNO3oDwqlbXg7caO3Rc32ePmij33rwzCczciHjw1nDONO_Iuu3K5bj9zDJGRPdUlpSj2yHFoQCr-1CgqHPS5dYJgFCfP6AAGBYo2w5PoGJiJ8mvGet0yJXh4UcplFjzb-felipU2fJ3RsEtV8LykIw5-fcQYya3xqM_Nn_LfsCx96NKy1frrlnX_EkAl9hjmZKAXSmYF73zhKULLAITbaSVv7aXIYhG4X_uTJ3OavGLcWMyG1UZjmWnEZJzgUIQGsxgPDUuAhTIvFpWtMcj91WEbzZ1xQyUTvd9Z1bxNvKXFQsnWFFAjQ72HJ9T9eRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین گلزنان جام‌جهانی تا پایان دور‌ ⅛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98992" target="_blank">📅 02:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98991">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WC4S29JAPm5tbH9eQ4nhs01MNq4rMiw96GpM-5maQ0-CmkswXFiSnpFEoYwvu47CUhNMNSYWS843NghNaS6iE34qeQ_3FtjDvA7FR8c76eQsaAlbmYOYhFHEtmKjhkRk0GLDYO2V_CywoB13j1CXffwGlf022GAs7RYf-m44khv5tUZk3obv7TJW7N-5bBcP5Ebp2F-USeOX3gE8cIpyag_5w_Wvtbdaxp4S27eoIMiyH54HFxkbE6RSUKDiOpbgh6-H3YbzOQB6oGqu332tfIz9JLuCsYf4MdhIUnMPjSclRKxku2LeOPpaALe0W63SlFIbpkp_HNc7Djj_ILRPtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ اسطوره آربلوا سرمربی تیم فوتبال فولام انگلیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98991" target="_blank">📅 02:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98989">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRCueTDZ6mhvD71_WPCHlR8y6raQ09lqePIrxFhO7Tx1L_E27UKEXZKW2p0WsiNsS4UxnqXO5B_Jq3K0K5FSAUHsn5zxbMi6QkjeJjUAX7q2hz22_c7mWDOBljbDZ8S4nkOLbpoO3j-V7ySwRr7W7Va57fvAWD-c8FDWwepsCtNphzt_bMwp9je4uD9lAHxUPL8UtRygSOHogBgdo32p2EGR5Avp1xVa6nQyyifV9uLbDCcyFXsraqQqloz-TrJne_CJ4B4toOh9yqw0eiOStkDdcOYOYKUxK9bTOiyh404QjG-sli4zlguQla8i6-U-sKbgq0hTo0zHPVS5A2gDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98989" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98988">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2ezmqXtubYyJSDIu7UnYDih-u7dWHfOUv3qlWls8imJK31TjYdc7xiVNuVUbOZ_ZKkdxBKvxQBlsDEvJVQPyQ-2fdtncWfSaYo7tvtSgZsHxUMOybdg3D5kDsN4inBPV211bFfSjjdy5F-pU7-N_yLKE7_HmEB2dxouVn8TTP7mnIAVGqLn1fLLF1gP7R7eqfWjv2B0WTKc52BfVWfYRBwqrTs6XbF00H0kRWZ5Dqq86gcdgwDBET_KmqFx6yTsCPolvf4ahxyxeSOc2lKBdnD_1tWvBhgtaGKaex0sIRYMStUD3Mi0-G_3E4zJ5heQ17t3IcF2aZPaqOeoBJ2TEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
تیم‌ملی سوئیس با برتری مقابل کلمبیا در ضربات پنالتی راهی مرحله بعد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/98988" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98987">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/98987" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98986">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گلگلگلگلگگلگلگل و تمامممممممممم</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/98986" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98985">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سوئیس بزنه صعود میکنه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/98985" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98984">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/Futball180TV/98984" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98983">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلگلگلگگللگ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/98983" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98982">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لوئیز  دیاززز اومد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/98982" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98981">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کلمبیا نزنه حذفههههه</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98981" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98980">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
🇨🇭
✔️
✔️
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 563 · <a href="https://t.me/Futball180TV/98980" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگگلگلگ سوم سوئیس بالاخره شددد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98979" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98978">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
🇨🇭
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 461 · <a href="https://t.me/Futball180TV/98978" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98977">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پنالتی چهارم کلمبیا و گلگلگل سوووم نشددددد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/98977" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98976">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/Futball180TV/98976" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98975">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گلگلگلل سوم سوئیس نشدددد</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98975" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98974">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
🇨🇭
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 625 · <a href="https://t.me/Futball180TV/98974" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98973">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلگلگگلل دوم کلمبیاااا</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/98973" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98972">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
🇨🇭
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 400 · <a href="https://t.me/Futball180TV/98972" target="_blank">📅 02:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گلگگلگل دوم سوئیس</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/98971" target="_blank">📅 02:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98970">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
🇨🇭
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 722 · <a href="https://t.me/Futball180TV/98970" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98969">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلگگلگل دوم کلمبیا نشددددد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98969" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98968">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
🇨🇭
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/Futball180TV/98968" target="_blank">📅 02:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98967">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلگگلگل اول سوئیس</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/98967" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/Futball180TV/98966" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98965">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
گلگلل اول کلمبیا</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/98965" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98964">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98964" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98963">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
پایان بازی سوئیس و کلمبیا
بازی راهی ضربات پنالتی شد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98963" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98962">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tw-UYc2wlPHEg0mMJGu037BZElAlApQonTDVTQmuQw3nkNcYra9V5wthMCi9fpLMeTn5b9Hj7TOqwp3CYLB9e-B2SHebmauLQW6cgbzd-N3mtU7TqtBB36JEaKn3JjQ0lTDJaYZj60BgSs7SMlz9fM4BAQSL0b4GL6yi02IogNdq9RxYI7PHtzEfDQYZyKtrkT8_KNZxLYpisvDMPdl9Hdi0LoSqX3N-z5f-Fu1cDpajUqo-bm1n8NQyfFS34qm_u_emGdhCIF-jw9xxegLXGZWVz8TIiJOh5p0PDMmNRMLIjxuKBBuAT1lahV2YL0aMjB--DN5dt0Z2JGd-i8bkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلمبیا چه توپی نزددددد
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98962" target="_blank">📅 02:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98961">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ گزارش‌های محلی از موج جدید حملات آمریکا به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98961" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98960">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوووووری
؛ گزارش‌های تایید نشده از آمادگی همه‌جانبه نیروهای سپاه پاسداران برای حمله به کشورهای عربی و پایگاه‌های آمریکایی تا دقایقی‌دیگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98960" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98959">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وقت اضافه اول هم مساوی تموم شد</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98959" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98958">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e61389fce.mp4?token=A7sxW3Qz1nb4BKmqwH5QNoxFEwbvrxTXVdhX98ixuzqpO0XvoKs_Eearf-EtOnrikt7qUkYq__-eksHAVCqK8JvxUs4PFMYup1nGwZQWx5El192UabcF-KzNQhEn2opC2DdLAzdUl7CSSPUs0mSnXqGFNskN7Pj3xUfGNRh2iXzM84FaVnzYx-uOXShyux_ocAYZzecbKZRpfQnzli6J2CJ8sg-VQxXQoyakHylpqh-sQbF3hwRO7eui9GyzDYnYw7f9Op-0WeAve1E8rvHByua_2otK046-COobRS9caLCsn5RHrsDF52bb27nN8ntuGMYiQxWoUO5MicAppg9uf0OzZAhfiAaopIPHd3jC5WG2mt9s6jOYtjhinIBcdH9VuzRheYinem0laId0_jsbbU8aY76tw8WEh3OF0_HVuVKwqtt0qOYhxvFSDrfINwLb1zWD4VkLw8NbxmJFvlbXz19K3IT1kRE8T31uAw3Kfi_IfMXcQfWj8MGi4tB5EgIYRFZEeMvfUL8gZ96jzqNTRkeSZCvnCT2FOhb8-v_yTbEPDExQIWLNYiz18FGD1vP7G7uFIqvecUM3CUNCRXyyJQU-wWyZpjr8jENaMLolXgV13kiN46JNx-NAlPxUUpS5EksOyvxiRtaofNvWZEGeCCtcqCMRn3W6W3iAuACqzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e61389fce.mp4?token=A7sxW3Qz1nb4BKmqwH5QNoxFEwbvrxTXVdhX98ixuzqpO0XvoKs_Eearf-EtOnrikt7qUkYq__-eksHAVCqK8JvxUs4PFMYup1nGwZQWx5El192UabcF-KzNQhEn2opC2DdLAzdUl7CSSPUs0mSnXqGFNskN7Pj3xUfGNRh2iXzM84FaVnzYx-uOXShyux_ocAYZzecbKZRpfQnzli6J2CJ8sg-VQxXQoyakHylpqh-sQbF3hwRO7eui9GyzDYnYw7f9Op-0WeAve1E8rvHByua_2otK046-COobRS9caLCsn5RHrsDF52bb27nN8ntuGMYiQxWoUO5MicAppg9uf0OzZAhfiAaopIPHd3jC5WG2mt9s6jOYtjhinIBcdH9VuzRheYinem0laId0_jsbbU8aY76tw8WEh3OF0_HVuVKwqtt0qOYhxvFSDrfINwLb1zWD4VkLw8NbxmJFvlbXz19K3IT1kRE8T31uAw3Kfi_IfMXcQfWj8MGi4tB5EgIYRFZEeMvfUL8gZ96jzqNTRkeSZCvnCT2FOhb8-v_yTbEPDExQIWLNYiz18FGD1vP7G7uFIqvecUM3CUNCRXyyJQU-wWyZpjr8jENaMLolXgV13kiN46JNx-NAlPxUUpS5EksOyvxiRtaofNvWZEGeCCtcqCMRn3W6W3iAuACqzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو دیگر از حملات دقایقی‌پیش آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98958" target="_blank">📅 01:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98957">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=YEgRLWVBPpDsJYV-lIblLONVyIf9KgbVZhceeVf84dLRrydAEjNjJLF-Pol8CFzgnwC58Zixdl5slJH2l2-myb0O0fHwNgddaTulqQxGQRst0EA0-TsxXKCk6lt7CD3MeBEnviEXEDrbP8E1MqLBhQp3pFVj2I9QjGS4uImQp67N70tu5WX5yoYsFH0gBziG9Sa6CNoYcroQltPkA6qoJH2DF4RFykERxpdLk1cc4DgKO3LVRJ05WxyFeCEzNMqVfFPh86SexdPxdzkqhhFhk4fFU6vYcY0aMV2mqYGjcJYi12osK7ujMslXr2NarU-1KuFzMl7kf0Ruct0n-UeRPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=YEgRLWVBPpDsJYV-lIblLONVyIf9KgbVZhceeVf84dLRrydAEjNjJLF-Pol8CFzgnwC58Zixdl5slJH2l2-myb0O0fHwNgddaTulqQxGQRst0EA0-TsxXKCk6lt7CD3MeBEnviEXEDrbP8E1MqLBhQp3pFVj2I9QjGS4uImQp67N70tu5WX5yoYsFH0gBziG9Sa6CNoYcroQltPkA6qoJH2DF4RFykERxpdLk1cc4DgKO3LVRJ05WxyFeCEzNMqVfFPh86SexdPxdzkqhhFhk4fFU6vYcY0aMV2mqYGjcJYi12osK7ujMslXr2NarU-1KuFzMl7kf0Ruct0n-UeRPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو‌های منتسب به حملات آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98957" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98956">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98956" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98955">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oS9e4KiNZJyk1D_HvsaiFgB56ySXMFvfqvq0_i37lb_33eHi0Hr8xUZNWdBdusJRS4umQ2wfSQ4XcVQ2gqG3EyFNqS5d5F8FW4dPSm-IQd9jWOk8c4H9xPtnNV5oKLjZMZs7c9ufhU56Q8SMH7eX36O94JTUhcrfaaYzauBIuL5hrlWjXexj8YJJtUbV4G-xFFo42-d7K8Htw8XXv0HhBPp3d32JeVy6ClXZlKIBMHgY3xsqVoGpE3gFymkE86iGYjow7OxS3pTYvU_7Aa1nU5qqHdh8yiuUoRffPC1mrTOLlH7RSI1w3-NdLM6aSfIQR8mrQdiI8ABoQbdkH1dXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98955" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98954">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ سنتکام: در صورت نقض مجدد آتش‌بس از سوی ایران بار دیگر به دستور ترامپ محاصره دریایی ایران را با قدرت فراوان ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98954" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98953">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پایان بازی کلمبیا و سوئیس در ۹۰ دقیقه
باید شاهد ۳۰ دقیقه کیری دیگه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98953" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اینقدر بازی اونور کیریه که اخبار جنگ واجب تره پوشش بدم براتون
😐
😐
😐</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98952" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛
سنتکام: در صورت نقض مجدد آتش‌بس از سوی ایران بار دیگر به دستور ترامپ محاصره دریایی ایران را با قدرت فراوان ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98951" target="_blank">📅 01:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98950">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3b48AAXucW8wOyi1KSmtmTwwdXBfmnPHHSF2Q8jYZi1suoIepktmlqSfX2Mo2M4i7YJo-CLNLw82t5s5zVPwf1EvrJHAzE7ySMWWhJPrsQkK5-tB5sNs9StKM10BdRTi8EkYlhjNeCug13wOJ4cAK-U9WFUgv8jRoeyRYwpSZJTkaqA2pjx0R-S_tXYKoAWoED8_IDENwsYZBX21hVOfoUwFQ_AdxaBuRRu6kkHZgc4h6Qyn3NdN5xgk3O7is-Wr9Jko0Z9HrxppORj2sUbRWgsYXniw5J_f9s3p_hrm52Er6NIueXKWYGcFprsURS2g8eq4xk2YPG6sUfyvYLvxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری از حمله به دکل مخابراتی سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98950" target="_blank">📅 01:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f434bf30ec.mp4?token=M4l_UWhGue5owe1_o87rX2LnRvGA3W9kpJC-2wnZ432AKWUB_5jb5SSxph-1v-_I9AIqE1mK9PyWBj-IKnNIW7zFwt93xQEISp-JnGQR3ZaQ_Kldr3Zp4Vd_GRL9p9KXOMf03EedOs-Q8MuRw8PGrx1H1po9NR41aNP7U3pN_g7bDv_t8SjzqEQ1zXK5c-bVp8qRvfaTm0hnOrgCQYvAwYDV-9dLtvtIVtkWoZd6j3xT1DrH8bB7kqCxrdNj2aX9OVZrkX_ECQyH0qoI4mP7pEtmsIzx42FKNCL5NZb05fBlBddooVwj9w1z9Zri2k9HK5WoPj_KUI_cIT2JY7tYCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f434bf30ec.mp4?token=M4l_UWhGue5owe1_o87rX2LnRvGA3W9kpJC-2wnZ432AKWUB_5jb5SSxph-1v-_I9AIqE1mK9PyWBj-IKnNIW7zFwt93xQEISp-JnGQR3ZaQ_Kldr3Zp4Vd_GRL9p9KXOMf03EedOs-Q8MuRw8PGrx1H1po9NR41aNP7U3pN_g7bDv_t8SjzqEQ1zXK5c-bVp8qRvfaTm0hnOrgCQYvAwYDV-9dLtvtIVtkWoZd6j3xT1DrH8bB7kqCxrdNj2aX9OVZrkX_ECQyH0qoI4mP7pEtmsIzx42FKNCL5NZb05fBlBddooVwj9w1z9Zri2k9HK5WoPj_KUI_cIT2JY7tYCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇪🇬
اشک‌های زیکو بازیکن مصر از ناعدالتی داوری در بازی امشب مقابل آرژانتین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98949" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNeuiK1OLiS2g65bbkoZhREm6lskhORAzx5HwnE7QDLcY24FmXet3zgEL2-yYQvr9ebOpy9o1NXNibXmsR00VjxSvA7TCvvRBeMYiByIjTWIOoCeVs99ifkoZLftuai09MZxlydI7DPGr_PezhUbKdZ_AcPQxuawc3Eugbi0fJ1CTePVVWUxI37TUWSwznVA0V1gTzsoepgLwCtDTbfo3J94egb9LwOEAMe0pSYqG_3YKSJio5V03VEkKtINXIGYvX26n7Is87GyY550Do9szcuzdGlbSWpTQn4qL2AQ53a8gxKjVCJkN46azzoMmAUvzDWp4D8QGJASfXiI7Vunpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم‌ملی آلمان درحال تماشای بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98948" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7agG3SADGr3HGEXTRbx1ugdO46QH4gj0TnbT7Cx8Ry4mm96EeoJLn4wl4FSCl20ciqFh4kzyIMblv8jMse6OjzWWI9vV209NhSWz2C82N9d6wXdd15g2ozYUx-9UIxbWi55tkor3mOUZ9td1cbo3VzLQtl7UpFw1VeT-yOF_C9z17aJzVziDLcvNfLX-tgGAQgiUvG8j16a4d68BXFfda6kprFSxNJW1na3HjvB6b-dREi-yypG3qa7g1K6csB_Vb6WraVcglp7ToyEyBoArczjbTxjV2AQ0dQu6bBLFOfvhAMm1GpHtraFt2u94zUEvsXoDeUbqPuuZn4nYxhsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به شناورهای سپاه در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98947" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری ادعای سنتکام:  نیروهای فرماندهی مرکزی ایالات متحده، مجموعه‌ای از حملات قدرتمند علیه ایران را آغاز کرده‌اند تا هزینه‌های سنگینی را به دلیل هدف قرار دادن و حمله به کشتی‌های تجاری حامل خدمه غیرنظامی بی‌گناه در یک آبراه بین‌المللی تحمیل کنند.  حملات…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98946" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98945">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8QMWRRh5h2TeLOVMFq5n80cm0ecgCVHuUen3Trf6L1e9eLBMg3NPX0bIbYFZ3QQl9Vhgkpb_H6aHjzpxN_X91D5lGJP2G4lGCRH5I9lnF8xVESF3XR37_XOvEiB2UFZM0DMA3JKWhAwfsln56OJtGF3I8hxx6ROvfM74Pe4bG1p9Q09158lz2sm5VpTuHQuuQY3yGJ1LBOjSl9taGftHzU8K9Tng3oUQhT_mPYrccddUJ3vq3-ytxoR9keybWXAWk6ovof_lzNuviGtQoV8uH_l76slr69sKiuxrxzKY0OV-CzdZeu1X1bY8VMUcJAsev9sxUu3Bz80qPKIAB_OUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
ادعای سنتکام
:
نیروهای فرماندهی مرکزی ایالات متحده، مجموعه‌ای از حملات قدرتمند علیه ایران را آغاز کرده‌اند تا هزینه‌های سنگینی را به دلیل هدف قرار دادن و حمله به کشتی‌های تجاری حامل خدمه غیرنظامی بی‌گناه در یک آبراه بین‌المللی تحمیل کنند.
حملات ایالات متحده در پاسخ به حملات ایران به سه کشتی تجاری که در حال عبور از تنگه هرمز بودند، انجام شده است. تجاوز آشکار ایران، بی‌دلیل، خطرناک و نقض آشکار آتش‌بس بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98945" target="_blank">📅 00:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98944">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/101717de02.mp4?token=hcmwmai6OdGNKgTbnQw2BiJJq_Op62P01aUcswmGAI4_HevYSicPKjh8CvkAblm-2e9et02mAuujO4fzBjTTi41-cYcItOoDy14-U7RgacQeR-7HyBxXrZgfYweghMmuSFsPgQF4f80B4yNqSmPrK2HodcHthLUICC0CVVcKKjAHr5kMQgUolSvOJdUDujHACernj0qeOjvclEpkONomUB9OcCjBzfaVRBewE9GPgO4SQT6XfAp-0FdP4-ndxUCu-NzL-FqUq_ZUoyc2RifIHAYHFEZcpeC00ZQqhtwNCN_j_uB_PHPwdsDURSlkozt18UsS_5t0zREwKMphDW7QXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/101717de02.mp4?token=hcmwmai6OdGNKgTbnQw2BiJJq_Op62P01aUcswmGAI4_HevYSicPKjh8CvkAblm-2e9et02mAuujO4fzBjTTi41-cYcItOoDy14-U7RgacQeR-7HyBxXrZgfYweghMmuSFsPgQF4f80B4yNqSmPrK2HodcHthLUICC0CVVcKKjAHr5kMQgUolSvOJdUDujHACernj0qeOjvclEpkONomUB9OcCjBzfaVRBewE9GPgO4SQT6XfAp-0FdP4-ndxUCu-NzL-FqUq_ZUoyc2RifIHAYHFEZcpeC00ZQqhtwNCN_j_uB_PHPwdsDURSlkozt18UsS_5t0zREwKMphDW7QXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تفاوت توجه بازیکنان آرژانتین و پرتغال به دو اسطوره؛ یکی محبوب و دیگری منفور و مغضوب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98944" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98943">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ شنیده شدن صدای انفجار در جزیره هنگام و سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98943" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98942">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98942" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98941">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری
؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98941" target="_blank">📅 00:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98940">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEIbOCqXS3xNPAxAsfaCz0WB_zsXV-ztlzNTn1BJzlSxEJybz0KeJ4HdfDJJhpsEVAiJgIRQJcrW6wAb5lpU5ZtRVdMKtuHWVT6W2K2OQpQ7cwfKOKZDmhdtRuJmbh5d6GihW7AAQYLaM2TSzwKIZEnPdKvaIX7icDwXPHGyovPtcucZc0v466h3n-zNCIuI7PTlFTASglEBoA_ClThO6HXdlK8JsMhpbkLhF5dVD4qGdTlBt3DxkZ09dvR-UHM6mFcwRiA3a3l9JE4HsEo4mS_wSGt6lTn2sex0bB_fpUysymib9dCegUEZU6nyzxvDEThJLmzJd4rY1_n7uOMhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
آرسن ونگر: «هیچ تیمی نمی‌تواند در این جام جهانی بر فرانسه غلبه کند، فقط اسپانیا می‌تواند آن را شکست دهد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98940" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98939">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e80f1162.mp4?token=YE_2X9ocl55TBtDpCwmuUbfqreI4eJS2ISzgad2tZJQWXHHIFengGBUsR10dj7QaV5SoGZ2SgetipB9zTI52cZSPSacM6OWxzjKHP3r_CVFd265PmEBRkIiUt-KZY6Mx2Y1Zo5rDRGYYmEPisOxvjnusYwT_lkBvPD-uQK8XDlV8RVgiEP4Lgpeaj5hlyftMbxOPHB4Xh00IuFT0TDMBLGu1wn0YsVqw8ufrQJUJjp0xvcjmXrh5-DOK5jFgv3crLkIHxCkXPYFNHj0RYUn0kFX3qLk7W8Ri3jNdYhLFp7XbefsKEPv7yetTlx1KfjAwup7UZixQaZU2CKnDffuJmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e80f1162.mp4?token=YE_2X9ocl55TBtDpCwmuUbfqreI4eJS2ISzgad2tZJQWXHHIFengGBUsR10dj7QaV5SoGZ2SgetipB9zTI52cZSPSacM6OWxzjKHP3r_CVFd265PmEBRkIiUt-KZY6Mx2Y1Zo5rDRGYYmEPisOxvjnusYwT_lkBvPD-uQK8XDlV8RVgiEP4Lgpeaj5hlyftMbxOPHB4Xh00IuFT0TDMBLGu1wn0YsVqw8ufrQJUJjp0xvcjmXrh5-DOK5jFgv3crLkIHxCkXPYFNHj0RYUn0kFX3qLk7W8Ri3jNdYhLFp7XbefsKEPv7yetTlx1KfjAwup7UZixQaZU2CKnDffuJmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Legend
🐐
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98939" target="_blank">📅 00:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98938">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پایان نیمه‌اول بازی کلمبیا و سوئیس</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98938" target="_blank">📅 00:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98937">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQsmyHqAFBA7sO8UoWXGYG9JAFNsF64OPSHuQq6Aj0S9VVV4HuumLcdxHPXz-QnnyTnZiYN6-kWt_tR2s920hA6x6xxZE2KRkE2eU-qFGnUT_Pufygwr2hIq_THjhPBuTzuzo9LisA4oWG1XCDbenUzGpRRBapj-U7d9s7QgH3TFC-_ahUzZxp48bevTkFsmquRPltTChet1tc7_7EqcrKISuqV1IE1wxFJ_7XYL_j1OBT8RNGIR2OMbAm6v_xdd8tGEglULSrPk166HN60UhG4fVvc1NxMe62nR4r5iLYsLpx_wgjJl2rjPUFmncxdhTbxfpLWAvnpkacA4OdbM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇬
#فوووووری
؛ جیانی اینفانتینو پرچم مصر را در جریان مسابقه بین تیم‌های کلمبیا و سوئیس به اهتزاز درآورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98937" target="_blank">📅 00:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98936">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3e3abdb3.mp4?token=moQUVTGcKXLLQsQ6lUC8fwpErwXqAAPrCYSaQDkAKYYX5WloVxuPZReRgpg7i7bQY4ng_V7N0HsQXKEpA1VLyP6XgRPxNzlxtX5kwfJYleWuyB_62hWr_HRlvY11lGvSjsi-TNp2-dR74R33uaXpCGenLp_HSsf4zfesoT-3GHmatd5MFNsNXf8oTWHzQ7Plt0lF0M_TEYGkXiI-v0-5TZloHuQur_013oCV-pZlaJmFWUPXL4jYgS9rdJZCUlsA8fn-lY0hdhRil7pysVURZvQa0RD9v1WbebmBP7kg_zqNJrP6Oxd-3isy6_JDl2RMMHRFUgQleOYmzc2DcYGDRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3e3abdb3.mp4?token=moQUVTGcKXLLQsQ6lUC8fwpErwXqAAPrCYSaQDkAKYYX5WloVxuPZReRgpg7i7bQY4ng_V7N0HsQXKEpA1VLyP6XgRPxNzlxtX5kwfJYleWuyB_62hWr_HRlvY11lGvSjsi-TNp2-dR74R33uaXpCGenLp_HSsf4zfesoT-3GHmatd5MFNsNXf8oTWHzQ7Plt0lF0M_TEYGkXiI-v0-5TZloHuQur_013oCV-pZlaJmFWUPXL4jYgS9rdJZCUlsA8fn-lY0hdhRil7pysVURZvQa0RD9v1WbebmBP7kg_zqNJrP6Oxd-3isy6_JDl2RMMHRFUgQleOYmzc2DcYGDRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
لحظه گل‌دوم آرژانتین و واکنش اسکالونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98936" target="_blank">📅 00:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98935">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a31c10f53a.mp4?token=tiXe2aKFEP2X-39UqHorYlRFHJi4BJEuos7m5S96P-Exaa9RAHghp_8dnhyjh1kny-w5oBBR2Oojp9HZxcB6sCeQrMuHj-B7xFD-9YSAkLTnH37UGr8oKYcSYJQGVWFv6yzsNz58IlYCXF4TR4gfERU_4-F_5lUFeTJzXW0IpEsKrEg9BpGfUr9m1KiZXrdWFjM2dFzK4MfVZQNl9oqcE0G2P3NzTk-ryDJ_0IcNCUyrPNY3hEXefMiZAkPTwYJDoRL5DDKHLrK6yCRC745-Y8chYtmjW_DRt1z4rr0yNZhrL3LOwIaDBcVqCkSi4uXBI1ryqrCNbmIhfaEAHD7X2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a31c10f53a.mp4?token=tiXe2aKFEP2X-39UqHorYlRFHJi4BJEuos7m5S96P-Exaa9RAHghp_8dnhyjh1kny-w5oBBR2Oojp9HZxcB6sCeQrMuHj-B7xFD-9YSAkLTnH37UGr8oKYcSYJQGVWFv6yzsNz58IlYCXF4TR4gfERU_4-F_5lUFeTJzXW0IpEsKrEg9BpGfUr9m1KiZXrdWFjM2dFzK4MfVZQNl9oqcE0G2P3NzTk-ryDJ_0IcNCUyrPNY3hEXefMiZAkPTwYJDoRL5DDKHLrK6yCRC745-Y8chYtmjW_DRt1z4rr0yNZhrL3LOwIaDBcVqCkSi4uXBI1ryqrCNbmIhfaEAHD7X2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇦🇷
وضعیت رختکن تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/98935" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98934">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27ddcab60.mp4?token=qYAr7vlos_dFm1cROcpOnyDX79f_-uxQka7mDYHoNknGRZafcOKhcu2O_W22jwcoX4c5Y8WoFyKsm4vZTzRXbsEcN0koMLSj1dY-ThtFpFfHqwkBZ7kAgzeltqAs4SSPHOuEHxkkz5Eq7w5TnwjbFqqJEAcGFqVWPz12aQPP8mSAj1OfiKCG-vQHArXw9Osh-6Opu9yrli-Icqm5RAszt3BcUfA-mDRCRB_i07CsOPuSgkT5Zkr11_EXeby5azqkflmMukPNpYrxRdh3GGvnj83KBS4YbG1SFtU4nfib9IW84bFMPxg4IliYGEPeBd2ukdqgcyBtsn1SZ5YI8NEnGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27ddcab60.mp4?token=qYAr7vlos_dFm1cROcpOnyDX79f_-uxQka7mDYHoNknGRZafcOKhcu2O_W22jwcoX4c5Y8WoFyKsm4vZTzRXbsEcN0koMLSj1dY-ThtFpFfHqwkBZ7kAgzeltqAs4SSPHOuEHxkkz5Eq7w5TnwjbFqqJEAcGFqVWPz12aQPP8mSAj1OfiKCG-vQHArXw9Osh-6Opu9yrli-Icqm5RAszt3BcUfA-mDRCRB_i07CsOPuSgkT5Zkr11_EXeby5azqkflmMukPNpYrxRdh3GGvnj83KBS4YbG1SFtU4nfib9IW84bFMPxg4IliYGEPeBd2ukdqgcyBtsn1SZ5YI8NEnGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😍
🇦🇷
احساساتی شدن لیونل اسکالونی بعد از کامبک معجزه‌آسای آرژانتین مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98934" target="_blank">📅 23:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98933">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIqB_fxd3REMXVS2pVT6tzPrNywtxs_BaXeBZNv3w4b5vZVCJ8W2xM5cfZYYEfrXILh4KnAmyeTmdI3_Jd1HMM6MJ4R1_-krWUhqrb8XQGEe7bGVEq7Ja5tR9qsEZ87TWF0l3UyhpsQZbG_A_IFSbLp_JgddBGruvW1ujd3M3ZPfXHtfbRCohb2D4cREKm1zaSPygyMYHfnGYB-LKiBj3qW4NlCVNo4qBh7pGEov_Q5xwh2U7xBFDoOHMVNiuOhrdoPjzcc4XlkJFMd_ZBwm8Tz6iBtj_n76dBelETm-O6JEzSOiSoQuuPhfA06eIf8egasC83wqzb0KxB7rcXI8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بادوم زمینی استراحت نداری تو
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98933" target="_blank">📅 23:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98932">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZZ5wRe2-qt_2xoeSyTE28uWoGLCg1FKh8jcVP7j6FVhfbKZWmxgD06pUgcDR1gWwrQ58pkqBZd8-0pZLJLTExNdkgZgPn_gplEZWjYdHHay2W0XH7rHR0k5tZw0UHdzCO__oeFU7OM5VYsy7Dw1Dez9vTnVS8u0wMGwb04HmhiXEDWneaf5orOUTMH0amSCoXQVjJqBS6slKLCjrP1zFntkWoYfAcKsA_tdaycjkSLoPUjKRUFqNcrse6GSCp24kHJ2RXFqAS_-jg7_574UtmS6aWIkgIhTVbpWEoiuP-6pRgTRtQUNztYcufer653-kqotKaa8YOSx71W2znmM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عشق از چهارتا عشق همچنان داره ادامه میده..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98932" target="_blank">📅 23:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98931">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شروع بازی کلمبیا و سوئیس</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98931" target="_blank">📅 23:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98930">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8G0OQIK2o51w8t4mR5Vq2PvQdzILIY_9IwVGL3KevIR6sY4XlklAO7kdzF98oCL9vTpx0HZnKpazTtz0YZ-v07EAyWkioNMc3pp8RU3ipmRa-fz9z9EmAzShPcQZmxxPqnf6mIFUa6j0RK7BYN2dd2S697X3Isx3onZFvt4cLZP48yI8ECRWiDTzAPm9Fot493s-rw1LF_-rk-AauhobSSlLhrUKpIFP90PegsoQyojlAl2K6OT7ayIxrfmghJwz-Qp_7867l3sN3fx0x00TXqaEaXfv4t9_4DwJhJbOmCnqT60so3v776PCuUi6oMS3EgeDVa38Y5DonRVOfF-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
اسکالونی
: همانطور که لئو در قطر گفت، این تیم ما را ناامید نخواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98930" target="_blank">📅 23:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98929">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lMMRabrpeEzNSf9QsjwmvrdLxTTT5Al9j49xvqh14Ew3kmN-q43-ILsiBdfr5Pt_Fk3V5VeC4L3Br-nSqO7c9psCEwGCzlG7UnlUwolnl9X99BQhK5fmASRDF61Qlr-zixLPQ2f78f32sxoX7YEs6y-cHGVkQ4U9DD7eecNEZhdxDXG1LYJC_4WNX3FHPDhaZMXM7We0qlsm9ozUxUNvWqVNoGlElG6jk7ibm5gIzcX9beU4fwF9AmuJJKMCu9XjOQW0N2jrl9c4yu-QiahwRF5fdpx-R8fXEy1y0lgY13RtUsM7PWlFvIgnezie16m3l1m-00O21z2-LOsaAN-c2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه ESPN از مسی با این عنوان استفاده کرد:
"تنها او می‌توانست این کار را انجام دهد."
فقط او می‌توانست این کار را انجام دهد.
🥶
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/98929" target="_blank">📅 22:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98928">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏
🚨
🤣
کون آگوئرو بعد گل تساوی:
‏"نمی‌دانم که آیا الان دچار اختلال در ریتم قلب شده‌ام یا نه، اما اگر قرار است این اتفاق بیفتد، بهتر است همین الان اتفاق بیفتد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98928" target="_blank">📅 22:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98927">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjACMT4Y1sndjzOGpYwjtA74JBKAt8c7sk3adVQihGpWvSY0XHYB6wHdJH1v-NukDWVAOFPx6khxrswmZX6FCMtH87U-cd1FlrOFNbO8tir7vDhXAs-5plMOUqZOiCTGQdd8VPB1segoAYhDPzGQfF8BPZ8FM1tVEhPOuu1-CxPJmCX8AsazkxxF6bOrOspFvL-I0e1fyxOAYeEcd1kC9NcQu4vagJCsJJxZc2ibkylHPjYB2XNehjpJEBKWMBq_XSeutrtaP0yDPklnnMBPpOwOs6meGjVlAmmq3-A7c2G9XT--q9qpSx_fr9eivK_XO2BIlE7TGlBxRElvN8MYeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
گل انزو فرناندز، گل شماره 3000 در تاریخ جام جهانی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/98927" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98926">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
🚨
🚨
‼️
حسام حسن، سرمربی مصری:
‏" ما بهتر بودیم، اما فوتبال عادلانه نیست. ممکن است آن‌ها بخواهند قهرمان جهان و مسی همچنان در جام جهانی بمانند، به خاطر مسائل بازاریابی."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98926" target="_blank">📅 22:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AHXPwVKKCCxDlhcpHRLWzwTjap0jsdU96-Xl54repXbUZW1_9F5ufRZz7pGVE0Hche9X4ZyDLPM93ZWZuKD6Xd1LZrH9X-2JLZiPfdXGaTI7_WZWpwJRls4P1XbVc0rvBNlBuMgnCshS_66P3mIZk_bEW8b8N2whOSuh-VOXg-sK1_jvXz2gnvUziO7kiFBLmJYg5KbYLBAZlWH-JyecxdGvAjY5JS6PtVE7bjDTJ65a04oNqYfsGFURlybSlSg0sniMqo1Cl-QZSkh7tRhGiRaOnS94r7v5jhC9ZT3ED7YHUSnt2YYsaJdqW9K-7_CT8SrWQItJf_aM1Q1wCAunvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtkP6BCN0X4FRRJPbQTX389qc-ZgNN-7fm8CZdNOGg9y_bicweBmpkJGnMEAzxDvBE1sv5-V7XFeo5ASHR0hCUIJdabLkv6zZc1Sv_7gGDgVbkZ6rXRmxoHptNYLdQopv3icjPwFLnEuqIwvjVVEeZDr2llIXUfEuN0l9gY3cyk6kAavZ0nE2C2PnmZLGUUzXGJa7zAsaHtxy5rfaPLvieRLB1BAn9YWtGI9v40yWbcIpPWPKyzM3sfYeGO5zHXbtD8WP3wgEGNKXflQVpZnBagRMZrygbzHHEJyRkoWxnpL4UBvdJWmyraJuT4nipcUjqKRojGEQ8W_WiNWJsZAew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇭
🇨🇴
ترکیب سوئیس و کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98924" target="_blank">📅 22:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soZQshoems27v8WI9xvkklaV7y7JFiVaTHiMJoTYi51wkdFb82wJS80NQLIyWQByBUld9XphKh9f6T578zNsL_9PmgzZrU9VAlPl9xAs4PtR9-uo22skRIsJ38Xf2_L1nzexhjuTVdM8Wi6CK43EYjFsg9s5HaOrZ_JFetDzPshJ6l-0igb-6c0S7Blx1Q77kcO5Jy9qRdzx1SnuXJg3H_z6EpkIWXDBQIkGfXrOcwksPtsVoCmiFFYvG_W1kvczBw63vsu8_DtkR5dSOe-EqD9m8FoLDncpPqhWINFms4M3S-93eUQKHcCmrM241ASuJc_0GCrpijWrxeaVcEK22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی با 39 سال سن به مسن ترین بازیکن تاریخ جام جهانی تبدیل شد که در یک بازی حذفی گل زده و پاس گل داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98923" target="_blank">📅 22:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWWopQW3Y9u9BMPK4GWz7G_t-oYc8qMMVMVLo3MyLeBxXvgkq4stwHkIs772_iFC1IXhNdavYaqTYCheLek8SjYS-m0uxYthaxHT_3pvQ3Y0tGL8pRGZw03_nQDw9Gn1PR0cVhUFjIuzqpemklpsH4zyhve8SjPbAqJSfzSujo8WnZSR_RQBpdqQi9-o-pMasUose9Fy75KCJfD8m_Q8T56Mx46QhmqteD_i3NZ5EF-Sw96aUec7UhrSjAgYRaMgDfym_RP55upbG8Q45UfPLAv9AR4xsfUnQ7HFTi-CK_jHoXGnmZTIxPjcbZG1oIpnna0lvMUYaNsVRknNpX19uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
آرژانتین، اولین تیمی در تاریخ جام جهانی شد که موفق به پیروزی شد، در حالی که تا دقیقه 78 با دو گل یا بیشتر عقب بود (3-2 مقابل مصر).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98922" target="_blank">📅 22:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98921">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/l8k5pM7zizwPk_GhEbJ8GHI4GHWDNOfkj8tTMN47xp6fc45suHGa9lcVcJbbYvdWJqtV30nK2tx-B61o0q69R-87Mb_ifEnN6Dad45tw-ZQp1_iwyDq9EA9UXdQGJUii-gDVYET7JqlcMxUnVKEKmOZZEuiMyj7zPk6yOIA8uLhxoJWOvICAwAsJrlLnFewplCLNuWg8DTexk0ePj9W9LvUcPitBGNtAXlNAvmlmvLNt8YgqeVddADCBqgdAyvEdU5utCr3CO0sDvXdY73SorStMylFfIsOVrUBQBJFZofe641WZjCODQo6oRS-9Rhn9V0106Ah7yhrZtXdlGLtgKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادتونه مسی رو بخاطر اینکه جام جهانی ۲۰۱۴ رو باخت و گریه کرد مسخرش کردید
یادتونه مسی تو کوپای ۲۰۱۶ پنالتی خودشو خراب کرد و ارژانتین حذف شدو گریه کرد مسخرش کردید؟
یادتونه با ۱۰ چوب در جام جهانی ۲۰۱۸ بازی کرد و مقابل فرانسه که قهرمان شد اون سال حذف شد و گریه کرد مسخرش کردید
یادتونه میگفتید مسی تنها توی بارسلونا میدرخشه و جام ملی نداره مسخرش میکردید؟
اون الان هم گریه میکنه ولی اشکاش اشک شوقه اشک که بخاطر دومین جام جهانیش ریخته میشه اون ۳۹ سالشه ولی هنوزم بهترین بازیکن دنیاس
پس الان شماییکه ۲۰ ساله ازش متنفرین و فقط دربارش کصشعر میگین گریه کنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98921" target="_blank">📅 22:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98920">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXNs7uRqn9eo6KAF9iEOAZ9axuDCuF11OTI_cTHqvM130xRqIL1AHj2XEb-CaohaVUUAzcjUg9u4u1j7jShyds3Ts_o2g1B2w0QcAxfgcAIwQkrTeLWAc93qivOuXfUhmiGpEEdJs1ebkuPsKu6JjwE4tiLYSI-qndjJF9EM7laoLWx0-JS1_x9UbXLEnrzBa4Wx6rSuzFRs2nJ-DyP3Wdd46NjbMABJpWV3xAT2UgXQf4HxLnwYQHNXrBEWU2-4tZzG5k-91TaHbBqw4Ow9PMM2fE-mhss-xeh12ahPmY9hQN8rCj-KigZPCNiqNoHyGVG0KGFp3YoZ6A-lUUPn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
زلاتان ابراهیموویچ درباره لیونل مسی:
او به یک هیولا تبدیل شده است و هیچکس نمی‌تواند جلوی او را بگیرد. او بدون توقف به پیشروی خود ادامه می‌دهد، و این همان مسی است که من دیده‌ام، همان مسی که ما به دیدن آن عادت کرده‌ایم، و هنوز هم امروز او را می‌بینیم.
به یاد داشته باشید، او از قبل قهرمان جام جهانی شده است، و جام‌های متعددی را به دست آورده، و توپ طلایی را دریافت کرده، و همه چیز را به دست آورده است. می‌توانید به سابقه فعالیت او نگاه کنید، که بی‌نقص است، با این حال، او هنوز هم بیشتر می‌خواهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98920" target="_blank">📅 22:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98919">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tidsb9mK12_sWEplgbPU2DbhPiWQP1oFjh28F71wCxcftv4OhsQH5I4rue4oYiRKyQdiE3jFhZa7KxEpav4Ez6SbYFlXBKlJA4uWrUVrANBCNMxv553QXjoM99cisJxjkjXL6jxLsRiO1sQ2wb-2DM-8eV7V7QWjkykSuUMWoAf2nE_txu_7RVb37CsBij4EYfZKSkpvwrp7awmvCJQHFMX9hMolX2YtiggoES9BzT8QYXWCaCW8VMCjqMfZEPgf2E25Irh5y3hakLsGcO0Y_VlvqkBG0oU012QpCeBO8buRFRG61qkzFZcNLKyeeyqqUys0U-GH_SaA1Wr6fLArxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
– آرشیو VAR:
• در این صحنه، پنالتی برای مصر وجود ندارد. – یک تماس جزئی از مک آلیستر وجود دارد، اما این تماس ضعیف است و توپ دور بازیکنان بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98919" target="_blank">📅 21:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98914">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BT1o7qsgYqtRYLyCdLohXFACfsz3LmDtrvuG23tqDVPfZ4HL-OAxNWMgpLdXGMa33je4IVvHqI5vqPB32rpQoPcFP9EjNKkq3QjY-2Vv46aTmKpH4Eu95MlHSjXjRZsvA17eurI_RaFc-2M_oDHQsvj07P5cXmP8P3vJQq2vgA38uqB04iXLA6585lhyUeS5BroPY6krbbPDy6xJkjFOCPMty-q7i6_iGFaeFNpcaPLH0I0tRUigSl_8esZcLucdYnP7rlhXv1QGuP7ReDxDUztZQ9qmD0hTFcQlvua3hCFmmma-GTGuErQckcR1_hGpbqwu8Mmi12EdUwlN5tbJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDDYWESZ3IMEK38UbDZFXtCzAz-nFz15hCm8EyJQLnKprA3--2mRDmJA2bVXQFmjeonu9kylzyaPYCPgLaa5RvOxuHs1mf2D5KdZy8GdC7azEtrFfUPC8CZ5mfTEoBzl556N3SNyvMex1_2m8HpCUbGXvntEBDhiW7itFw7_bll0HB4ncKwdPAt_-P_RbLwd--wr4unHjRjDQjsZPQFr9xG7pYKJuKNBBOfpLs1at2eGlDn3Z1tyfV0POMPHZ4qXP4u7uuQCHOGplt0C_QlIpt-B6TI_R4rsDL-gGVBIU3C3TVNiSy8xsXlgzDmm1Xht0x9LsUlbJd99m4zP12NxAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQ-EIMvIcPf8trzXLaDok99Ca4FBhYTwNvD441WmvFRhbwr2_tFKproUivmEu_NLQeKTq5UQPPSNRVdUWbt_6mgVLSsDBDYz40KQkTs-MnTM27ab1uxSFMXpmmQaoXlkeY8q6-Cbnep1kThKLAgcUgHhMv64AFRfn7YXn-OBZE8M-k23SNM3SktUCqtRwsFXjYGVjwsvRfnlBoCoKcIvBGL90h2bz0W-E16cqpwTH53bKL1k4yQ0kL6ma2AZfXPvrjxHVE2_8Otb4MiQDboEXSE-1VSXEZhV_iPG3PWsUewhu_rD38LLEl6wBz5fnvrZ33bEdcdcFgf4ECVxscEeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZunTm6We-KQRuJuRn-xj7FasnmYHP4tBhITTynFoCCO-Qh8MOmayNT_dhk5eiSTVM5-0_fl3KY4l_uSgqYjMMfNPLdsRxZHOcOlx2XCla9VeeePkMI27lW3fd8V5HQsq2hPtZjgZXKqlDJnMc9ZFIdYJbO0UHgm-tqebqWZcBBPActd47DNhw_IXEafd8VTIq5QRemK8K1CvEdpCl7Xs-urpW9KIT3yfBvK4Gvlnl2iVJatgAUbtPdoWD_fkRF3o0c9J6DaXuLFM3xBVB5zQ0PB-ZCYEvo2pf-7Gg2gMBandvonm9ZQfkPGFmI4yVi2rcK5z_laS1Tb5khsrmNIHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvIGfBIG0vT3FDCaTTMhsBtviXjqwP8LbqF36TFRQrEG5V4bqGaoLUqdQWIi8G-8Fj7RPxT2WJe6g0gQQqRRY56UlvOIA1RYeTd_VbjlQ7VMvewwfJ-MEhBfcnl73GDO6n3sxKDateg6LW0w65OhSCDBQfNa1Xqo4eFQI7EjuOW2bDIP7W1hGk3ihvsiSUaqfsphxnsFnQgsWsrRzQbisZ5ybt0fhUckMRbtOaFhOLqmsl962TxZIDU2kL2hQshUS2PmzfUeRJ4x8DOsdCOll_l8c6_nPnoXloWNiV6yut-HiI28MwC8ZoiuSkNbEevsGz1Ezs4kcs5higl0LIP4Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دیگر مخصوص استوری امشب
🤩
🩵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98914" target="_blank">📅 21:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98913">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
‼️
مصطفی زیکو بازیکن مصر: داور تماما بر علیه ما سوت زد. امیدوارم خدا انتقام مارو بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/98913" target="_blank">📅 21:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98912">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ut-dtw_m_dQX6gDiLoiB6LQ4bpKSDGAtSlq8yenIed9s5hmLoeIFiWv2NQoKkC6jJx9XbDQvguDQ8Mis773JmEz076W7pdZUF4W7qNSU0XjxepiHjXMm9IdTDKcu9P-JYuFTHyUNAz7b-A4XOcPaND-d5FgnV0hE6HXisK-QtIcwlN3cUwPZYP6mAEn1UGCeSQmH9ROe-9ZrfZc7AAq2MFZ2Zv_T6MpRaPdNrqxyL9HPzuOd47G7hIhc6fNYYBdv_muREzn6aWLwxB5AMHqLFP-_rqXOCsSTCE24GW4VUsRHtkB4PW6suMxFgi8NEc5mhIKmxwJQCB7HjKuQ9s1shw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید بعد کامبک
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98912" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
آرژانتین اولین تیم در تاریخ کل جام جهانی است که 3 تیم آفریقایی را در یک دوره شکست داده است.
- مصر
- کیپ ورد
- الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98911" target="_blank">📅 21:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLztDppCpHjX7hjTEikZlve4L23-PeCdwpxuDTyG5vMcsY6VK36CfnbLiDL78-24CNJjSBUfBLMgWAQIPvM1hTrdyLFQfIprLH4PfMZZJbEQN6gGwiyTSkAAiVxdA7-wODtmzZZEsdYFIFo8zJOR4YVIxVgDNGQJXhIygjV0VeOM38p8aaabK3ST0S67gYedGyESpCQRnhhzyXM6yIXNBjiI-8UeAcKS9i9QuAjxwi3BLTd5ce7CAJMmoNzGGOaDW9O5QCOY1Cp6OOEXvJCjY5i8LhN1DHTzn-id9XUHvui0T38qdrHVRKmwoYRyTYilrl98NvyvNK2Q4YSWzeelOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
اینه فرق احترام به اسطوره‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98910" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98909">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌎
✅
تیم‌های راه یافته به مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98909" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98908">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5mGmoGkxh_qBAkMLw05Kh_s1QFJlRb4XpGrPb-vttHxSDuPP_IiSe0dBb5jZJ1VgGmxC21Z2U2_Ptc81KCnrjIHiQHmI_d8dHt5wapld0n91GoobO_SlXZ-1tAsB5fcglFOQFm4j3y8e6UQRkuH6p4RgcRtEsq1pked79RD1l4D8R0ONeQskEbZRm1wEjLgiGVB2Qh4LhM19HUCa2XB_7hBy2YaDK5iZWjn3WUqlvjX_CxjYE8QtYc1iAnftNZiJzqA20o9A3KMRPltEDtXtCieK9BR26vhkgRsUmDVaL17wDTx-xwyepWK9vbUnTYZtpp3ejgAIGMPl705jj4PTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
✅
تیم‌های راه یافته به مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98908" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98907">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5ozZDuPWUMSVh9nRZs_lxP-nd8Dtw2pbv7q_YNUOBI2ZMTrBH4JgEtma4s-sIREkapUhkjrCrYi0hBWRuyQEaV2xdiTK11eGksFytByTHvJKacyapJT80cFaLohFtWRz_R9xY-I75K3HsGV3qy1UmUFEZKoOF8bpxEhj0MS0QrB_4vXGvKZxPsftMfByg6QymElGNwPmhFfOUpH9gXqeHxXT3Ry032KHL9Cfh_x7QOa3PKVDWxM8fxEZuORRY4yWKr0GPA9QNFxW0P8a1n3zJx7MrUxExz-bx8gT1_nWtXS8rZs94T3shHXZP6d0-RrA84YNyGVVxqecjjnmFfMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
‏بازیکنان با بیشترین مشارکت در گل‌ها در تاریخ جام جهانی:
‏30 مشارکت —
🇦🇷
لیونل مسی
🫡
🫡
‏23 مشارکت —
🇫🇷
کیلیان امباپه
‏20 مشارکت —
🇧🇷
ادسون پله
‏19 مشارکت —
🇧🇷
رونالدو (اورجینال)
‏18 مشارکت —
🇩🇪
گرد مولر
‏17 مشارکت —
🇵🇱
لاتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98907" target="_blank">📅 21:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98906">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9deSeFH0d8Kvf74N21HWReSs74qCux20X1Is4VyqmcoMJvCtG7a6D5lPVrs9ELoc4Wrykn5Wr_53ZGMnW0AH9wnL4yucg5UF42k5jOxZ9sU5lrePKL2RNtWH3q9PsYM0gn2XfKEkw_XZYGAIcLFoz_eWo2_S2SJGEWagGqkic9UIaUBV2qIeFruGtTRBiq5RikIJEKoYZFYyq7flApA5DyzmkwH4EpgroVGcUDGeFhIsa65mg3fdEtkY4vb2IHDe-r2HxxRm8OAYgTsv--RWIcjxh_wTOJJEVdbJoa5xc4lF47WfzwIYcy56yhiArqRE8emGPyQLqR9uVbffE1pmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی، اسطوره فوتبال، با کسب این جایزه ۱۵ بار، بیشترین تعداد جایزه بهترین بازیکن زمین را در تاریخ جام جهانی به خود اختصاص داده.
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98906" target="_blank">📅 21:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98905">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8B-oLQLaIYbY5bl9dIZEeF9uY_2YsXcZfLrsfSiiLa_MfHR2db-kWE2dnL_TQhqoywJ_XJagIZ90bgHKbSFWrxwji7Tf7tioqsoaTgjtiPY1-NgRumKOrqj20MsD_O2fukCK_lkIid49osGmRyHmr_BbnUW-lJNhFAIwArqnq5PNkY-39JFoDjKprC646wdsfRG6A6CI6DRnJIl-lSokCYQON3gOBvMLwtBD7nUoaLK4eNX2S7vlZLLI1JIxAIaqw2HiAQyrC_PxJNkHIHfO7E8PnXoeJfz6tV9Y67OZCGfxUbqVQQmbmDlHoW4ebDdg8dBNH2nGCR0hYsA1uatdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
🇦🇷
| ‏اسطوره، لیونل مسی، در 9 بازی اخیر خود در جام جهانی:
‏— 9 بازی
‏— 13 گل
‏— 3 پاس گل
‏16 مشارکت در گلزنی در طول 9 بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98905" target="_blank">📅 21:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98904">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkqxHvc8mQaPSps5eb58bxcstNqr51K_6r6nNvbPzYv_ksoWy2XjnFvl9XNCorOJfGyZJTcsM8lpvSg2rJFyDoofjFQmSK30z92UZjfu9z85KLbvBIOL82BZB9hkssGs86XABr-Mg8vwbjvO-W3C3o54uu-WdgGp-GF64gDggj4rP0AvSlHUKmvDCjECLZA83kY9cdI49Ar62dKf551UDoXFm3POwXAVccAAuQh-BaLN9aNuPh9ZK9A_P4WWlLR1XEPcL2tLFK0abxLKVT7Cxt4TxLDPqAE5hPkYksBWih2DPHSXDOhXVpUK3X085CQxpx-OZ6cV5Td2c1EYCTTdDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
افسانه لیونل مسی، رکوردهای خود را به عنوان بازیکن با بیشترین مشارکت در گلزنی در تاریخ جام جهانی، افزایش داد!
😳
💙
30 مشارکت در گلزنی در 31 مسابقه
🇦🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98904" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98903">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR4f99mq_pd99P_bl6vMxm9yuDjuhz9CuMq4RyPfze_8aL7PjbxIliLFGWP51q6lQF3WJ_HiwjyYWiTDVARqMVsz0CXZqCV9jMDto62YUKxT_FLS2h43GCDQzqj0_03uyncUaV-MGweulF-66rA-uwrUW2PMml-j8rTTWb2ob9O0nflWBfs36ikNfkWnt8nrMRCGBte2JFXfWOqerdW7MWK1bPkDdyEfecZcToysTvZVjo-6juY7nV99isXgxJomFZOaWt79jt711Nf6pZdRXkQ7IyQDrxd9ST_FEY6_C0PaXYoPLWEOsu9vr9-6g3Iad2_gts4gkSSvCYORSmMSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
خایه‌مال باختی کههههههه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98903" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98902">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJlJfxzat8HQFKKfpWJlwOnwZl4wcIaWerLswPHlqV8MtE0Sc3W1vRU2r8He1RnuKJJlrCHCnJdeVd9xgmzqkcgKJfhz1xekN90U-TAXJBusFYi7qhWav3d668r2CJP4m0isTdIkDVxn9SkJ_E1MV4z1ca_gN7j9hXA2dO2iey9UhCKsCvtkGBEdF4vzzwmxjRaGQDzkRPdU1wXrNb1MHp-pb1LBXH4Qi1aPu64iRDpMMYBt4e5MOYc_3SSzRPmS90bfk6r6xGLwsVvszArYiYLWrfFJsgirXlJEKtkiUtmuF7PPUPIwTufT33r_CcShuLRIXg4BQ5d_R_CmfpIH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاریخی
معجزه‌آمیز
افسانه
🔥
🔥
🔥
🔥
لیونل مسی، بهترین بازیکن مسابقه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98902" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98901">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDDr99zX5BVsA3yMmab1yUioJ76l0HL2dFFZAxgoFEQNKy-igaR172Ri31Ee8d7S1Oxu96teXHUtZAAOPEZwldU7n9rsHqpLl1uhNtt7jiHaj_ZxQl9LwJ7Y6DZGupTqfIqP3ZAv8XALeCbQKcRlld_AOQnv21R41UPP2ZuehXzBnmTDk_hfo-x035ng2_B88v2M6XmiI-ucgsnzixjAWRuNslQqeplw6_mjg2Vqr1voTXOso1K6fSBl0EgFFhv460Zlp-HWnEeIzLBTk_eWXzNU9IMwAabUxkvVBbbsLHGlRXLw82y8d71mVXXK7xl-crs_YbP7bb5TVTQ4SsaLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98901" target="_blank">📅 21:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98899">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDdeOLWwM9Svg9x037-7-fUjk4hH9a1w9xB5UezrhfwuM5mwKgLagEGcDer_mYf0y9qx_xEPITT1fTPrAwP9bDCFYSvH3JjMD0srsMczJGrYPBCinojNXOaaAfM1fiq7lHzelhtuLwSgFQXL56BDVWK1Rr7LbvtZiCJ_ivjzKqxeoGtUfgH-aroMoh_YDabPIsHkbRTryt-mAlu0gtp4QPtj45U6q1jIfCa32q_6WXkTchTyqFxMs5AgTNVb6Twz1df09RzyXUFISNzMOGWtompD4AmTinhJw9lt2CsoMYgRFv-iMLCAi5gpGlQlrJkBpPIG6S6HK5vi78jS-nfZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ob3qw4RR0Qq0tmVwHdIQSP6wFgcoLX2fQyuFYXq629awZ6yGD7WIqoy85VT9WYCg1nCV5rR9MidU_IW7QzVU4RroXToYh6wP0KFV22xAw_A-ODqOkXzbAR9VKDIHEwxtbnItG-p8w-Juf3B0oCUIyLOt5I0dB8abALA34yERzAR8PgMECq8KenYo-LqWvPEEl7rLOW0ToWgQ4fv_uu5ZRSnlodFXxmU1FDhqu_0rTw-htJW6ks0lKjlXJTStlcZiWwaJZcy2NtGIdsoT9_yA09Sgc4XKOm_hAY4WoQ6oOT1aZKU4iD4v4EawG2dOXfT9j1tFXKKU7ZtHmwTMFACvxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گریه‌های اسطوره
😭
😭
😭
😭
😭
😭
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98899" target="_blank">📅 21:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98898">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8xPvSUEqYB42eJYm79WgEzQVT3qIk73B7YTyN2YKMRjNVmmsq3jqTeV5GKWvGZh9tKXv_VcTOtQtz-GEG4ojQWiZKA1JuNJrlJGC14h97F9AiLdg_AOQsgEqpp2_xp20hYQVPXBDla0gV113xjGaTf2zQ6R5po9oWLCJmoRDR44W_o5u_rSv2jmsZETwtLUpSzUi7uqM6uzD2PaZIrwasv__yKoS2WELnCYRROQd_OKsFdja2i9bOZ8sVHfOyLJuDu8yskSZr5FpdZCMuehWYhqpYYaEZ4IP4vRGtQdFcpup9OWAKO-fPFkeAVJEUIKn3zyuaCNfH6jaMbQbcVR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گریه‌های اسطوره
😭
😭
😭
😭
😭
😭
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98898" target="_blank">📅 21:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98897">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چقد دلم برات تنگ بشه مسی این دیگه نامردیه تو پیر بشی اخه
😭
😭
😭</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98897" target="_blank">📅 21:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98896">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qck-u5zh0JqwjFjLE64u5khIsYyjnRbeV-1Tydtuu0XZ09ca5Kt-w1BJSt22ZgP8YxR3FRpCvLNmrs_Vk-LUXdz8KwzYdp70LrXzYVbaQQ7WglsslSASd9GqelHROtEO4lnFFL9crszJQcI7tsyZPQQ2sHbP3-T_iP3JX0J8FC7qmCJewABKWT5OWDWXQxBIWKgLfT1joDIxHVkWka4_d_caFAmnYD4mQ-qBeLyK98p71AyXXWS7tHVkRipXzNG3vF_UiD4e6s6rZn4A7Ml--7hrvFbwNd5m0qPnW2of3bonm1y7qMt3Clx5PX9xY4UkBPFRLRreZM3_mRsNzsskFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|بازی تاریخی آرژانتین به رهبری لیونل‌مسی؛ مصر در ۱۰ دقیقه تار و مار شد؛ قهرمان دوره قبلی بازهم با خلق نمایش باورنکردنی راهی مرحله ¼نهایی شد
🇦🇷
آرژانتین
😆
-
😀
مصر
🇪🇬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98896" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98895">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swNprN-n17RFqq2hTB1HMsuP835BSzhGS5FiLOfA2V1HJaqefRvPSy4rfhDPuqERicdFipQyElLI13_IWXIzwyBqjN17B7FAjV_1v5tRwJ1-JNf1pfvEp2nGVLkZZIM7EEhCiDyRmW5DpiRvps22Ne_ux4A9wZuXwa_5di8YbN08CRgNBy3QUP_FtzIOin4Aa7V1tONO0jGggHo-O8MgVTfUKJlVHEgjAm1wl3jXTNZAbp4GWqyFkDMAOIMTcwv9neQRzz_Gc10ZklOuCJlOrjgvdKis8S3ZlJFFFBVdxiUJZmok-phT_YaApA4zuI74Q3ayyn5qp2aoIJr7pybHMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی خایه‌مال مصر زرد گرفتتتت</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98895" target="_blank">📅 21:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98894">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الان مصر نیاز به میکل مرینو داره</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98894" target="_blank">📅 21:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98893">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA4k7qBU1ud7-JzkvxViYd_gKtDNilY93hCAc0Ee49rXe1QBjOqIdJGjO3zjnTfL685X8BI1clpPqmpoesh3K4x0nta_E2OAno9AfHN6Bot1_yQDZ-ZrUbii5WpH4yrYqRNu1B5XAv4nWCdab5o9uEWAVUrWdU-kCN_ZHomlZUZPunkjH7Bk-H7AvvcQsS-I2SGyTS3F9FDPFmhHwgOJbKjtDHbfMJS_j559Y8lfd4RDoqHKvnjt1B-O5mdQ1Gp86siwlJDFmWZPUVCNUdQvfurz8keXTHFSJeeXYSJKZL0yO-9f0YJncCArQeVdc3o7c6GDehXuTPtji02EESaAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98893" target="_blank">📅 21:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98892">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
گل سوم آرژانتین به مصررررررر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98892" target="_blank">📅 21:27 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
