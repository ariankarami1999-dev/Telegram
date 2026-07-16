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
<img src="https://cdn4.telesco.pe/file/ETp76c6biJqfO4-WKWsg4UcrPlENKBpSujwTBGKHzVoQrvcAYFqozNcLeLmJbkKEnmR60IOEEASsiuCnAc8ZDjCUz8XBbNoY88rNAQi5IQ3HqW_s0sB7BGlMN30ibF5whCieic5sQ8aDmcVeZAi1tmxqb3Jee3199BPGVmFQqpq4YUq8oPU-g7M92ki-cONUWbnE1eZfqIbnXoioNeRH0bVbIlBxglp9RfYoEkx6zVuLD3hWkEIWRw2WLf9FNGhO0kWv0q0arbS6kPyQdOlyrv8RppdGLfCPQLUAvrU7FkHXWzddfodyZl0sR7vHVBHiDilCLabArTzdLU708NqU0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 07:27:19</div>
<hr>

<div class="tg-post" id="msg-134631">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سنتکام: این موج از حملاتمان علیه ایران پایان یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/134631" target="_blank">📅 05:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134630">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
انفجار در سمنان و همدان
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/134630" target="_blank">📅 04:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134629">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/134629" target="_blank">📅 04:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134628">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777fa47436.mp4?token=pPXYB4UJw0q598uNzQZd_5RK5Et4PYNfvw1E95LW5huYy-F67fAysC0g0OdbipzmO3JDYlaWQV7dVn2xUE5Y4Jb1OSVvAPerRwn-DybmhlmEcTEWU1AzfwNNhD_4AS_8wPyUHh6Ckd06-rSIk7CKOVNDVZWgMDf9K56wg7V3EoXCTkDOFaRFmh6wEMkqQrV3HA-__rMjPUVxC9cNzqm2l8hYVlqVgIxnKc6Hb1ystq0ngjpw94NfJFDF7WPv6GpkIohyto7LRrSDMpSO-hTjtnMKvrmNHHlITTr4pIICB0xPpEhpWe7qYqWnJwZF_0zRutLzsOEKz8WXGpm3M78iVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777fa47436.mp4?token=pPXYB4UJw0q598uNzQZd_5RK5Et4PYNfvw1E95LW5huYy-F67fAysC0g0OdbipzmO3JDYlaWQV7dVn2xUE5Y4Jb1OSVvAPerRwn-DybmhlmEcTEWU1AzfwNNhD_4AS_8wPyUHh6Ckd06-rSIk7CKOVNDVZWgMDf9K56wg7V3EoXCTkDOFaRFmh6wEMkqQrV3HA-__rMjPUVxC9cNzqm2l8hYVlqVgIxnKc6Hb1ystq0ngjpw94NfJFDF7WPv6GpkIohyto7LRrSDMpSO-hTjtnMKvrmNHHlITTr4pIICB0xPpEhpWe7qYqWnJwZF_0zRutLzsOEKz8WXGpm3M78iVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط ماهواره‌های ایلان ماسک بصورت خطی دارن میرن و تو ایران هم قابل رویت هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/134628" target="_blank">📅 04:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134627">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دفاع‌های هوایی اردن فعال هستند و در حال تلاش برای رهگیری موشک‌های سپاه می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/134627" target="_blank">📅 04:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134626">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3314d4420.mp4?token=ujAOHGiawT38gBiXavvGdrQamTGxcQ-jTk9K7zgPcrzu41c-3wfsUTL_8PESS0xc4OGNg7MV8-kjJfbhmWUb2LToc1xDum6PNpjQkYOOim0DZ8g2N5esViWluXRY6tHpwm8pTTiGpH5R7C1qntLt1lJ6Tke-43A9I1xOb5NH4xC6LKYyvzbpp4GHELQZH4HmxtGRRPue5iAkM2jKP636m-maCuTRSbnqJYGjmlaIKiZlSK2b-1P3bWuvl5gXbSM4XXRiBwCk-wLIqL0O-SiMP_zHMdCvHVsjn7NmCctfx5nsXwGAGILlTEXO9NmUnHcJPKL85apLyM86RTXeMmjd9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3314d4420.mp4?token=ujAOHGiawT38gBiXavvGdrQamTGxcQ-jTk9K7zgPcrzu41c-3wfsUTL_8PESS0xc4OGNg7MV8-kjJfbhmWUb2LToc1xDum6PNpjQkYOOim0DZ8g2N5esViWluXRY6tHpwm8pTTiGpH5R7C1qntLt1lJ6Tke-43A9I1xOb5NH4xC6LKYyvzbpp4GHELQZH4HmxtGRRPue5iAkM2jKP636m-maCuTRSbnqJYGjmlaIKiZlSK2b-1P3bWuvl5gXbSM4XXRiBwCk-wLIqL0O-SiMP_zHMdCvHVsjn7NmCctfx5nsXwGAGILlTEXO9NmUnHcJPKL85apLyM86RTXeMmjd9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت پدافند در شهر ری
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/134626" target="_blank">📅 04:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134625">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a093d1ef.mov?token=gown-aFIuorLj2-xPiD1U_mpNW9Bn4NC46xsrx8VkY-ch1I7GeiS5_lgyCOLBgS1rVoBXddHIqDLMHJigFuSz6moIVo3HiPiA-yUBMFQpwaHqJ6hbChoUp0WZI2j9XhOnoZX99aMZBp4TqbUCYNKXvbtUatQPEE5Zm8krSSys4oFCxuRxFZVlQpI7fQMo2QbjhuOJ3GDY68NkOdUjT5DLdzx1yBM5cnRMz-bNcgPLHoF5Sc4MuvpRfy8LlzTH3Xm3YB2diTNVK4BsdKvIwqvvPbdtY1sHwySH6E0aQfZ4_qTEwiuOW3hg4v7gxJI-6YrpJR3yzk1hemMQkZdHAmGYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a093d1ef.mov?token=gown-aFIuorLj2-xPiD1U_mpNW9Bn4NC46xsrx8VkY-ch1I7GeiS5_lgyCOLBgS1rVoBXddHIqDLMHJigFuSz6moIVo3HiPiA-yUBMFQpwaHqJ6hbChoUp0WZI2j9XhOnoZX99aMZBp4TqbUCYNKXvbtUatQPEE5Zm8krSSys4oFCxuRxFZVlQpI7fQMo2QbjhuOJ3GDY68NkOdUjT5DLdzx1yBM5cnRMz-bNcgPLHoF5Sc4MuvpRfy8LlzTH3Xm3YB2diTNVK4BsdKvIwqvvPbdtY1sHwySH6E0aQfZ4_qTEwiuOW3hg4v7gxJI-6YrpJR3yzk1hemMQkZdHAmGYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاکدشت تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/134625" target="_blank">📅 04:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134624">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فووووووووووری/صدای انفجار در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/134624" target="_blank">📅 04:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134623">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411fc596e1.mp4?token=jnwKdqegDYwEUsM-JSoVwWIufQcAgp7wL4-YP3z-GXrI4r4Npq0Kgdsuqzk-PrKbGOFnstCwJAhnY-rlgKlPdCONEk7rR308V7fyEXsNwiebMUvkmyQEXzQRDcwzFFRhoOFRGicZ7vAo2lZw6PAq1xTfT6xe8StMktDLEwhu5JpsKBP1_L9XpWiQdpl9tFUcO9bjc0vdtCmM5Nm5dnsP1I5ZWQCGhPBKomCgSZjgYrzgLLDy6zDJqliUEQK7vQ565PTtv56pkiGK54BQAB5p7XY49enlAgoL8RrfK6JQf1pWkxgq0jKSpNGiteCyDO_4DGUySxB05_yr9wDbf5is2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411fc596e1.mp4?token=jnwKdqegDYwEUsM-JSoVwWIufQcAgp7wL4-YP3z-GXrI4r4Npq0Kgdsuqzk-PrKbGOFnstCwJAhnY-rlgKlPdCONEk7rR308V7fyEXsNwiebMUvkmyQEXzQRDcwzFFRhoOFRGicZ7vAo2lZw6PAq1xTfT6xe8StMktDLEwhu5JpsKBP1_L9XpWiQdpl9tFUcO9bjc0vdtCmM5Nm5dnsP1I5ZWQCGhPBKomCgSZjgYrzgLLDy6zDJqliUEQK7vQ565PTtv56pkiGK54BQAB5p7XY49enlAgoL8RrfK6JQf1pWkxgq0jKSpNGiteCyDO_4DGUySxB05_yr9wDbf5is2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/فعالیت پدافند تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/134623" target="_blank">📅 04:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134622">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری/انفجار در خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/134622" target="_blank">📅 04:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134621">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری/پدافند مرکز تهران فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/134621" target="_blank">📅 03:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134620">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری/پدافند غرب تهران فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/134620" target="_blank">📅 03:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134619">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">💢
فووووووووری/جنگنده در تهران  احتمالا خودی
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/134619" target="_blank">📅 03:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134617">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
گزارش شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/134617" target="_blank">📅 03:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134616">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پدافند تهران فعاله
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/134616" target="_blank">📅 03:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134615">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
اطلاعات اولیه حاکی از آن است که سایت هسته‌ای طالقان ۲ واقع در منطقه پارچین هدف حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/134615" target="_blank">📅 03:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134614">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
انفجار در پارچین، شرق تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/134614" target="_blank">📅 03:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134613">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/718dd6f75e.mp4?token=DcM-umaRMQ1WUpXw4irt52lrh3y3IxepNIxGpcOkKSYUjCwzplTpKV35mi25_7TunbU6I49Kykp9CW1yYt2VJxSl18pvQTlUvT7iH70i14uIvfYitxKmaSAYbnuPTgPgM_FNUH5k8fy9hyR3NtlHhcXie7K2fHQwo2rUinh7OEtNKce4Ad2bHyMmUq4YgwS_YsKRmIVgvq3n0VAKJOF0H-M74cF_09W7-Msm4LMYc2Z0X3UhLkMAmXRLa1sAkMVtwkVDCnieYDa5fE8ElJoU699x_FA_Z4ADWtRL9DpKKh8WLlyHqHIdkcJvrp-GzbKikaIl1VBlf2XaPRRHaqbOdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/718dd6f75e.mp4?token=DcM-umaRMQ1WUpXw4irt52lrh3y3IxepNIxGpcOkKSYUjCwzplTpKV35mi25_7TunbU6I49Kykp9CW1yYt2VJxSl18pvQTlUvT7iH70i14uIvfYitxKmaSAYbnuPTgPgM_FNUH5k8fy9hyR3NtlHhcXie7K2fHQwo2rUinh7OEtNKce4Ad2bHyMmUq4YgwS_YsKRmIVgvq3n0VAKJOF0H-M74cF_09W7-Msm4LMYc2Z0X3UhLkMAmXRLa1sAkMVtwkVDCnieYDa5fE8ElJoU699x_FA_Z4ADWtRL9DpKKh8WLlyHqHIdkcJvrp-GzbKikaIl1VBlf2XaPRRHaqbOdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار ها در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/134613" target="_blank">📅 02:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134612">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826a7e9343.mp4?token=fYDNAY9pZdqLDXMmYHlGx122oabsPRC2CjKgYQhEDGGfRFXqZAmD7M45r8iSN_ScTLB4HvpMJa40vPModKqC0a9Wp4VqZrUjV1Kqu4DPGkw4M4IG6UMgj3W4Rssq0YvuPyney3iF2P7bcaj5bjo-UgComD1icreL23x0wADVDNNKa3whvM3va3NpwmhJysteq72h1zk2TpXKMpCJW8LSilsuPpQkeCYfjMYwbe4PM5cJqmXpemFoohvapijDPn5QmCOBei1KZtjQcJGAygLVQgt689KcLTUL8oUze7RLGIkWNL5auDsO_lBKlp28M_-78ADvu6KPubd8QfSAr6_jRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826a7e9343.mp4?token=fYDNAY9pZdqLDXMmYHlGx122oabsPRC2CjKgYQhEDGGfRFXqZAmD7M45r8iSN_ScTLB4HvpMJa40vPModKqC0a9Wp4VqZrUjV1Kqu4DPGkw4M4IG6UMgj3W4Rssq0YvuPyney3iF2P7bcaj5bjo-UgComD1icreL23x0wADVDNNKa3whvM3va3NpwmhJysteq72h1zk2TpXKMpCJW8LSilsuPpQkeCYfjMYwbe4PM5cJqmXpemFoohvapijDPn5QmCOBei1KZtjQcJGAygLVQgt689KcLTUL8oUze7RLGIkWNL5auDsO_lBKlp28M_-78ADvu6KPubd8QfSAr6_jRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرسشگر: آیا شما برای ایران ضرب‌الاجل تعیین می‌کنید؟
🔴
ترامپ: «آنها تقریباً از همه چیز باخبر هستند. آن‌ها باید رفتار مناسبی داشته باشند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/134612" target="_blank">📅 02:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134611">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
گزارش قطعی برق در برخی نقاط تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/134611" target="_blank">📅 02:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134610">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
۱۰ انفجار قوی در بحرین
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/134610" target="_blank">📅 02:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134609">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4XJ-sXaq3zRtfVdnEUe34pejMOwgeekqmzY5hPpdScfEGPdwQYzdOWfshb21SyTBk-vnBq-WDumOG-cUsO5fTiHSoVirq6CXsLBoSNZRPvaWNU_-0MtAKMaYHsm-0SQSRxReTDuRJDqm3FdKbTJgh5xIiG2i6xtNCLS8I0OIZHk0C7PLdh5iCThZ21uzbmDF4hyVfrh0lNNOZsKleFQgDwjctiJymKRaxBZeB_CmENbqOygHnZKUEREu0hhb7s70fyvu0bIXnxAH7bgGzkDDv2BOsld7qy0k4kJd-VN_yL32VNSsM2LQ_9TySwBEURlkwjwZr2w2HTHwPuIxC6w6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری و رسمی /افتخار ایرانیان واقعی
🔴
علیرضا فغانی داور فینال جام‌جهانی بین اسپانیا و آرژانتین شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/134609" target="_blank">📅 02:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134608">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwsAidXeDFC_C_9yJyx0pGrYqfrO6CF9_7STXX6vrUNnX1P_jZMNwzzcq3A5KKIoYEX-4AaD28FTvSf8vwGkuCv9Ts2jgTlIwjmABJFkbD5NQs6RWPrIqotSpXrxReof6hrjEbjol6Pbs3o-2A24wSPKSm9GAqTLcc3TxtYiu9cgVSeRsNlQcJLPAxZ6DfBQiui4922IfwkeqzB5HCyTmuHgB17dA-E1azcAwUAXsF1sfzgqOOs6NiFybVNl8A5FwoSR1OF743xJg7PDWYx5LJwH8D9imug8vAl9D0lnwl3X1aUUI9EK_j-WJK6sNvLBRzPve9adSHO4Rgj6Xyy78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:«ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴ در دوران «ریاست‌جمهوری» جو بایدن خواب‌آلود به‌طور ناعادلانه بازداشت شده بود، اجازه داد تا آن کشور را ترک کند. او اکنون در امنیت خارج از ایران و در شرایط خوبی است. ایالات متحده آمریکا از این اقدامِ مبتنی بر حسن نیت ایران قدردانی می‌کند!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/134608" target="_blank">📅 02:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134607">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
چندین انفجار در بندرعباس گزارش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/134607" target="_blank">📅 02:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134606">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/134606" target="_blank">📅 02:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134605">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJA_2_cCB7SH2EGh6Vxo6OMqnxe_cqrQ6dvgykiJhs1HxjlxCJMCyVBoBs9p3iaO7zxE-VPTgLG17P39DgDKYyc1Wft3EpEql5q2StdRBZCf-zyhxXBfMxotKCQYp1v2YP-JuKmTU0DH5fHvOu_EYhtAeDEUf0XgDes7GIYDBGjvzt4cD1i1NxDJcp1eMQ47X7mIwsQnKg-Y2TKEfHRcvzIEfxhhVcf_dJX1luKQ38qf6Q4YjDszpqcoS08JdxydDE7ZDm5e1O-n4RvwKzCPxKMYhdrkowIVaSB0t7Z13yLGVlQ5HykYWE8l8jQAt4qOkDRN3qQ7exdscWKiv-Z2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انهدام یک پهپاد جاسوسی در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/134605" target="_blank">📅 02:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134604">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfca85fe5e.mp4?token=sywY-553XA3VwLPoKhXSohdOvTz8y_JLXZCxBSEkKJ5TWCBC7TGMXnFy57bxwL_t_T1ENfmYIJUsZvupEuoe8Ih9jgGe6uGA4W3cAmU0o9L-b0xK7Y-JPZC8m4JBb4zfIZBczNMPMQ8290dgPg2HRCjT7aVFDakmuEjebu0esToLSp-mfFMLPscIam5k3r8nKRrQGIbugBgTNy1uuySZHrbHjTIkQFerplqwW-tyAH_iFWnYCmt_oCf_uDXs9dUZ5XPEVFqeNta399IYgnRs8OzC02-SK5kFFUZE9SMBPqA_wI99WS_FtTmFuJsIJ6gG0o9SFWwT-uBMxHB6pi0HXjzcBXjNZsqtSahR_LaQzEn2J_7FgXN_D6E1CoGMgu4vLCULOHd9V13Ld1ugMeDbwIFGC79dSR-sdIlb61HYOhl1IVD0V-9J-KKS2SxW391Y9D9Btqxygi2M071y0cq_TVo8CTzr8lbnhJeml2B0LbG-pFxgZXHVeVOvZhFlIOECjLZDS3OzOduwNUvJXf9VcnCD5Yy4CthfE6ggLA2vA-7HwX_6-BvgCYR4PEsn0Hz4tLQ1pWSewzFckxKzFq0IpS_5FcmNO_V9yS5jxU5b0v5v1ARJ5ChcoyB9h2rfvgXYqza4INq57_0daB3HNu5FgdPlAUzDfZobLu1Dt-MFHzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfca85fe5e.mp4?token=sywY-553XA3VwLPoKhXSohdOvTz8y_JLXZCxBSEkKJ5TWCBC7TGMXnFy57bxwL_t_T1ENfmYIJUsZvupEuoe8Ih9jgGe6uGA4W3cAmU0o9L-b0xK7Y-JPZC8m4JBb4zfIZBczNMPMQ8290dgPg2HRCjT7aVFDakmuEjebu0esToLSp-mfFMLPscIam5k3r8nKRrQGIbugBgTNy1uuySZHrbHjTIkQFerplqwW-tyAH_iFWnYCmt_oCf_uDXs9dUZ5XPEVFqeNta399IYgnRs8OzC02-SK5kFFUZE9SMBPqA_wI99WS_FtTmFuJsIJ6gG0o9SFWwT-uBMxHB6pi0HXjzcBXjNZsqtSahR_LaQzEn2J_7FgXN_D6E1CoGMgu4vLCULOHd9V13Ld1ugMeDbwIFGC79dSR-sdIlb61HYOhl1IVD0V-9J-KKS2SxW391Y9D9Btqxygi2M071y0cq_TVo8CTzr8lbnhJeml2B0LbG-pFxgZXHVeVOvZhFlIOECjLZDS3OzOduwNUvJXf9VcnCD5Yy4CthfE6ggLA2vA-7HwX_6-BvgCYR4PEsn0Hz4tLQ1pWSewzFckxKzFq0IpS_5FcmNO_V9yS5jxU5b0v5v1ARJ5ChcoyB9h2rfvgXYqza4INq57_0daB3HNu5FgdPlAUzDfZobLu1Dt-MFHzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سربازی که چند روز از خدمتش مانده بود و آرزوی یک پژو پرشیا داشت اما زیر حملات آمریکا اونو تو پادگان نگه داشتن و شهید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/134604" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134603">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
جی دی ونس: کارزاری با بودجه‌ کلان سعی دارد مذاکرات را از مسیر خارج و توافق را نابود کند
🔴
برای این کار، افرادی از یک مشاور سابق ترامپ حقوق گرفته‌اند/خود این فرد از عناصری در دولت اسرائیل دستمزد گرفته
🔴
این افراد به من حمله می‌کنند و می‌گویند نباید با ایران مذاکره کنیم بلکه باید کارزار نظامی را ادامه دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/134603" target="_blank">📅 01:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134602">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
حمله موشکی به کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/134602" target="_blank">📅 01:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134601">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
دو انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/134601" target="_blank">📅 01:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134600">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خبرگزاری فارس :
موشک‌های آمریکا به اطراف یه بیمارستان (بقایی) کودکان سرطانی تو اهواز برخورد کرده و بیماران هم چند دقیقه پیش تخلیه شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/134600" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134599">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGBorCQE4btqMFpROr_Y2Xvt5RLXe1ocKKbv8QjqEkdeQUUkwCg_maPX9KVjK7fp_ZiQI-4NvPrTTN2XlGrvxoAp8OFye0SZ_kGo-Pf31tFGUVas4Juj_kbXcCQaK7E-LRj3Yqt2DFuQwFutard2mZqhoH9N7Dz_2GHogTtwKcUKwzAR4kOUNQ2-0mNx6QAjDMuFmbCz1M5x6Q0DdJeXoMhGrOGsddm7NmRBQGucjEUrQZ1cWDF-l-nTT_mA4HLkiwSIUgf9SowgiwTTaxF7CwJj1NUzgY457z4NlCxJyOMTd3bOlPRpkVJY9HNPSTY1RvI1blX63lCR5rl5kz7vYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح
‼️
چرا باید پادگان ولیعصر سپاه کنار بیمارستان اطفال باشه؟
🔴
موقع ساخت حواسشون نبود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/134599" target="_blank">📅 01:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134598">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e619333efb.mp4?token=fkFD9W0tckPtKmauBAdSKwl8dRPXsrgh2VDEGTZWqqH7hFVAtv09edqjjufz7v5KnBxpZwIDDULXBGaQZfVLwPsZ2Yhka0-qVEoPhXCiOwYo5sORNIJQ29b5R11_zj99nSoDvWuowLMeqmnFKopziNQPBb5ApBNIHbSXE81wo8fnXGTUQv3MTa0eNsLN0HvS76x8Y__dzCxkwuzl1ifyoaKS0ifngSj4AnROYHdBKqJs3hqejgNHOqQ2796uavey1wz6qDeIktE9rkl1eJH6vVatJ1DWLG3abYUHJ-dXeTA7npw1theaiKNnWYNv6KF9D8R3PlbX1ejVZgXvxhQXfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e619333efb.mp4?token=fkFD9W0tckPtKmauBAdSKwl8dRPXsrgh2VDEGTZWqqH7hFVAtv09edqjjufz7v5KnBxpZwIDDULXBGaQZfVLwPsZ2Yhka0-qVEoPhXCiOwYo5sORNIJQ29b5R11_zj99nSoDvWuowLMeqmnFKopziNQPBb5ApBNIHbSXE81wo8fnXGTUQv3MTa0eNsLN0HvS76x8Y__dzCxkwuzl1ifyoaKS0ifngSj4AnROYHdBKqJs3hqejgNHOqQ2796uavey1wz6qDeIktE9rkl1eJH6vVatJ1DWLG3abYUHJ-dXeTA7npw1theaiKNnWYNv6KF9D8R3PlbX1ejVZgXvxhQXfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بله این جنگ تو جنوب نتیجه رقاصه بازی و گنده گوزی عده‌ای تو صد و خورده‌ای شب به صرف شربت و شیرینی و فالوده و.... با چاشنی عربده تو خیابون هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/134598" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134597">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
چندین انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/134597" target="_blank">📅 01:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134596">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
تایید شد/پادگان لشکر 92 اهواز بمباران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134596" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134595">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/پرواز 11 سوخت رسان امریکایی بر فراز خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/134595" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134594">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">💢
فووووووووری/جنگنده در تهران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/134594" target="_blank">📅 01:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134593">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/134593" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134592">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/134592" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134591">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
همچنان صدای انفجار در اهواز به گوش میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/134591" target="_blank">📅 00:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134590">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پشمااااااااااااام
😐
هوادار معروف آرژانتینی بازم تو استادیوم لباسش درآورد تا به بازیکنا روحیه بده
😐
◀️
◀️
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/134590" target="_blank">📅 00:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134589">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/dofIZJ9Tudtjow3LqvA8DVRE1Bv4PS8gW8ivgs41yF2BKotTpc7jRXeGb-UTsNIHI06rkxwAU6lfYhkS60eYKc8irNHndrKCpc3Zpnj3nTHHcy6RivrVNzvn7Nng2lfZ6PXSFiDuNumiMGL5oNH6bF4Jih_bmkJKD73pX6M08oa0RgEjgMY8JuUCL0oTn2kJk49W7sFPjPjzedZmX9stpgwBDCz3hjBt5NTu2lOLigExOajE9TPaRIk12prbaLrC7erBkC9JfLhP0YOFri1yakcIv87_aVyz3q10OgTup8u5Cr-D335GkiCkDk2-KuLfsQFGIH5d5P4rxBBKUO9q0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بعد دستِ خدا ، انگلیس طعمِ زهرِ پای چپ پادشاه رو هم چشید؛
آرژانتینِ مسی به دراماتیک‌ترین شکل ممکن به فینال جام جهانی 2026 رسید!
🇦🇷
آرژانتین 2-1 انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
@
AloSport</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/134589" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134588">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
آرژانتین با شکست روباه پیر(اربابان پایدارچی) به فینال رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/134588" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134587">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06951345cf.mp4?token=hFzYml-upKjDP_8HahQfNE_zBDhJLpmH7Iip2nKuEjs7_ReUMc26K64DNpaDvtLfXpo8oAxkLyLbZfZN37p_v1wtx99BD6RzalsMDu40KWAIf0rqneGRWe_Nq5D7iSTvu58tSpDUqSZHwLB6m8PMla7XYjrhqxj0293dmiCafMxKkX3x2YcrKn6pzA-Yl7JGlKFqH_uiOePo25eocduWScF5FJXbhabJoK5JuGiqxa9NISvQbNhUljK1tbKhsd03WUI-GgzaLECFhZ3lB6RDAiSVi-jBy99Bi5zEtVYRfIpkLhLAEqu_10Y3dscpuF4f_CLwS4ZtzjnDxBCWf4ogew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06951345cf.mp4?token=hFzYml-upKjDP_8HahQfNE_zBDhJLpmH7Iip2nKuEjs7_ReUMc26K64DNpaDvtLfXpo8oAxkLyLbZfZN37p_v1wtx99BD6RzalsMDu40KWAIf0rqneGRWe_Nq5D7iSTvu58tSpDUqSZHwLB6m8PMla7XYjrhqxj0293dmiCafMxKkX3x2YcrKn6pzA-Yl7JGlKFqH_uiOePo25eocduWScF5FJXbhabJoK5JuGiqxa9NISvQbNhUljK1tbKhsd03WUI-GgzaLECFhZ3lB6RDAiSVi-jBy99Bi5zEtVYRfIpkLhLAEqu_10Y3dscpuF4f_CLwS4ZtzjnDxBCWf4ogew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گل دوم آرژانتین به انگلیس توسط مارتینز رو پاس لیونل مسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/134587" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134586">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: «ما قرار نیست فقط بمباران کنیم، بمباران کنیم و باز هم بمباران کنیم.
🔴
ما تلاش خواهیم کرد از نیروی نظامی‌مان به‌عنوان یکی از ابزارهای متعددی که در اختیار داریم برای حل این مشکل استفاده کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/134586" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134585">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آرژانتین چی کرد
😐
😐</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/134585" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134584">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلللللللللل</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/134584" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134583">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8b8b35f7.mp4?token=s3fonU3OIbZUGKx1VX77FA5Qi0JezuLh1F7S1NRldrkQBXVjL5aP3olQgoS8hpgcDqWmgXokcLDg3r3ho7p-SjjxvtbN_6MW2OCkDmIn2cgLhbpb27OQDZH5VKOO74ICEsPtvVOZOROufimHgfNilUzobjZPTOr-KiYmaX5DY4NrZYXXN7va499o7Yv8vJufbZZOjRstPJrDEFUnfM51Ctj-QEO9ZMFz47-lUBjfKUiBbS63MpuRHewmC3YjeKU909iluVnLbTBurcGiI6V9zZcOEuHKIPSWJBU7oIAOagyxdTVlBLLdVyJ5e3GNF8LMfx0SBcMC67q5hD9XAQHeZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8b8b35f7.mp4?token=s3fonU3OIbZUGKx1VX77FA5Qi0JezuLh1F7S1NRldrkQBXVjL5aP3olQgoS8hpgcDqWmgXokcLDg3r3ho7p-SjjxvtbN_6MW2OCkDmIn2cgLhbpb27OQDZH5VKOO74ICEsPtvVOZOROufimHgfNilUzobjZPTOr-KiYmaX5DY4NrZYXXN7va499o7Yv8vJufbZZOjRstPJrDEFUnfM51Ctj-QEO9ZMFz47-lUBjfKUiBbS63MpuRHewmC3YjeKU909iluVnLbTBurcGiI6V9zZcOEuHKIPSWJBU7oIAOagyxdTVlBLLdVyJ5e3GNF8LMfx0SBcMC67q5hD9XAQHeZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گل اول آرژانتین به انگلیس توسط انزوووو فرناندز رو پاس مسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134583" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134582">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=kR2PeQgwjmvGJ0B2i5AsqzGkGyLACH7JvdvWwKx2HDSDbkcVtG3EFr1Nra7Lz3KEROSiq-wd7lYW0AW4V3XFzh-4XK-e2ucAnS-DqVvaHtHQ4E174gjd5j1sF5F9NTnWLF6t8erm_erPsCzmREJThy0dWXUcb3kq-208bh7sx8rTLjUgwN2ZaKNaB6nSuMCpa-K7DMEEMaqNykRJbjjeduNnzCDAznjVvKVzmKr6ZSw0JDKvTOvrQLnrsDt4HzXe3a8hQmUh1fhonNqitrAxEUDyyGEXRNML01GtOHXQ7cFhBnfJmOOLA9BMJqxB446kmAAxq5g1SxVQEOE0czA_XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=kR2PeQgwjmvGJ0B2i5AsqzGkGyLACH7JvdvWwKx2HDSDbkcVtG3EFr1Nra7Lz3KEROSiq-wd7lYW0AW4V3XFzh-4XK-e2ucAnS-DqVvaHtHQ4E174gjd5j1sF5F9NTnWLF6t8erm_erPsCzmREJThy0dWXUcb3kq-208bh7sx8rTLjUgwN2ZaKNaB6nSuMCpa-K7DMEEMaqNykRJbjjeduNnzCDAznjVvKVzmKr6ZSw0JDKvTOvrQLnrsDt4HzXe3a8hQmUh1fhonNqitrAxEUDyyGEXRNML01GtOHXQ7cFhBnfJmOOLA9BMJqxB446kmAAxq5g1SxVQEOE0czA_XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/134582" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134581">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چی زد
😐</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/134581" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134580">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/026bdaa5ca.mp4?token=vHydpzxMKoFmlOkSn_UtviCkLuWq6ohRN8f3DQ6jn_qiV8G4FZKJjc4Lt87PW8xYAOcw6d_SBFN9CNBSBfbimqNKDjfCWH3TCQTMm_ipt5AuPuoC0VP1szjrV8gaOk6zGFEAnV6OcWtZZTntUoqyEf1_O89oiunv1gpNoBKJL8asOTT8ENttcplKng2hsO7qZ6SBzmNgb1ihCVFLnwToMsgIMC-tgMpKX8R5PIM3eTVhVSFaT8CaVPLbn_PSuR2_TbhBRayr0QhT4uD-cHE2yNMz2ra4H1cUcX-y-suIZQzdX4TNlDr789pnqZRpG-xNYQfqdr60Jc9dAcDcQq8LpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/026bdaa5ca.mp4?token=vHydpzxMKoFmlOkSn_UtviCkLuWq6ohRN8f3DQ6jn_qiV8G4FZKJjc4Lt87PW8xYAOcw6d_SBFN9CNBSBfbimqNKDjfCWH3TCQTMm_ipt5AuPuoC0VP1szjrV8gaOk6zGFEAnV6OcWtZZTntUoqyEf1_O89oiunv1gpNoBKJL8asOTT8ENttcplKng2hsO7qZ6SBzmNgb1ihCVFLnwToMsgIMC-tgMpKX8R5PIM3eTVhVSFaT8CaVPLbn_PSuR2_TbhBRayr0QhT4uD-cHE2yNMz2ra4H1cUcX-y-suIZQzdX4TNlDr789pnqZRpG-xNYQfqdr60Jc9dAcDcQq8LpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134580" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134579">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شبکه المیادین به نقل از منابع خبري  گزارش داد در حملات امشب به اربیل واقع در شمال عراق، چندین نظامی آمریکایی کشته شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/134579" target="_blank">📅 00:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134578">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
صداوسیما: ساکنان اهواز شدت انفجارها بالاست؛ از خانه‌ها خارج نشوید و تو خونه بمونید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134578" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134577">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
انفجار های شدید در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134577" target="_blank">📅 00:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134576">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وال‌ استریت ژورنال:
دیروز پرزیدنت ‌ترامپ یک جلسه ویژه برای بررسی گسترش جنگ و تصرف جزایر ایران در کاخ سفید برگزار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/134576" target="_blank">📅 23:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134575">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e118a97982.mp4?token=aa6SBi8HKwz6Sgq8N_izpK-YY0AOfHJd8frso_rV-ezfbTUOtsjAoHn9G-Aj5IPPuJ8W9acNUtQxIL_NfOUxeR1VI50geRqv9G65PfR5GCADB1sU_3h_QVv6RdRTK6RQf-k6EpJikGKjNDejf17a7r7cB9odZpmePefzxYui-5sIXY9X0_an9CNcC-cKBi3IDoyt_bn6XJ1rUmwDexDV8HMwYtlBM_wLCVGaWjKa06ZllFbg_NQwU8jXsD0pTeAf2Df1WdbDnkP0L3t33iShnJq-FKjSlEuGu4QGDJiaK8esKKhuY84UNYDVjpZ2svqsi0bHqAHfWkCRgawLSp6V4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e118a97982.mp4?token=aa6SBi8HKwz6Sgq8N_izpK-YY0AOfHJd8frso_rV-ezfbTUOtsjAoHn9G-Aj5IPPuJ8W9acNUtQxIL_NfOUxeR1VI50geRqv9G65PfR5GCADB1sU_3h_QVv6RdRTK6RQf-k6EpJikGKjNDejf17a7r7cB9odZpmePefzxYui-5sIXY9X0_an9CNcC-cKBi3IDoyt_bn6XJ1rUmwDexDV8HMwYtlBM_wLCVGaWjKa06ZllFbg_NQwU8jXsD0pTeAf2Df1WdbDnkP0L3t33iShnJq-FKjSlEuGu4QGDJiaK8esKKhuY84UNYDVjpZ2svqsi0bHqAHfWkCRgawLSp6V4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گللللللللللل اوووووول انگللیییس به ارژاااااانتیییین تووووسط گوردووون دقیقههه54
@AloSport</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134575" target="_blank">📅 23:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134574">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/026bdaa5ca.mp4?token=IaFNntzmrLfDwBwHPsZw-xwOVcSy8-C5nE9klaW0lBw_xqr6I1-Vzbp75Q583u-UeC7j2ZlXI_0JdT85Lycubdw1RYdbF97t_GJgLiA8kegfSrlljMpj2X6kHAxFelsdYEZxVv1rnAT3MbPzscPC1_poTh2kMHQ7hKvN51F-Qs1Nah4SSfzZcwyJuJVm2rblQ63CIhFIdasat8MQUVMSCw_YXIOgkLVdANrttPIpQYx7JuDa3siOobGlyv1q83DkiNb6j5V6CZlH7te4R-gFTClx37_3bdlTIbBeUT1kk51ikn78JDyjJ6ku16BETH977oYg0EN-wCtOnQY9aq7wuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/026bdaa5ca.mp4?token=IaFNntzmrLfDwBwHPsZw-xwOVcSy8-C5nE9klaW0lBw_xqr6I1-Vzbp75Q583u-UeC7j2ZlXI_0JdT85Lycubdw1RYdbF97t_GJgLiA8kegfSrlljMpj2X6kHAxFelsdYEZxVv1rnAT3MbPzscPC1_poTh2kMHQ7hKvN51F-Qs1Nah4SSfzZcwyJuJVm2rblQ63CIhFIdasat8MQUVMSCw_YXIOgkLVdANrttPIpQYx7JuDa3siOobGlyv1q83DkiNb6j5V6CZlH7te4R-gFTClx37_3bdlTIbBeUT1kk51ikn78JDyjJ6ku16BETH977oYg0EN-wCtOnQY9aq7wuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/134574" target="_blank">📅 23:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134573">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: زمانی که ایران به ثبات برسد، قیمت نفت به ۵۵ دلار به ازای هر بشکه خواهد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134573" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134572">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3619cfce23.mp4?token=cPE3SdgUfM_xHIJUaaxicNqmic7vyvzHlA0BbFjHGBiHUm-LQaCcjao-wcQVVKU5uTZgaZYOaANtamVbt3Fvt5KWUeY4XhIKTM1mkxCDQJ_E0E2liQjI1082wAN6FRjlhRhq1-NtH_vlbXF66pyLSZvo3HzQVW5Nk6Gj-zXM0BZCumX2nc4WQuKa8yMfQgp4fwYiXphUzxSxEL0KKKkZUJyFwdecJFctOFbSH3x5dW7oEk4R9gb3es4Hwmx8qSHbwKdTt493CzIlyilBrcA9KA1uxj8bo12S_rNUmhn43N63tI9SAcFlOQWjhWjTLDnuqtwM1I5WFHbP4kuDQP4mig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3619cfce23.mp4?token=cPE3SdgUfM_xHIJUaaxicNqmic7vyvzHlA0BbFjHGBiHUm-LQaCcjao-wcQVVKU5uTZgaZYOaANtamVbt3Fvt5KWUeY4XhIKTM1mkxCDQJ_E0E2liQjI1082wAN6FRjlhRhq1-NtH_vlbXF66pyLSZvo3HzQVW5Nk6Gj-zXM0BZCumX2nc4WQuKa8yMfQgp4fwYiXphUzxSxEL0KKKkZUJyFwdecJFctOFbSH3x5dW7oEk4R9gb3es4Hwmx8qSHbwKdTt493CzIlyilBrcA9KA1uxj8bo12S_rNUmhn43N63tI9SAcFlOQWjhWjTLDnuqtwM1I5WFHbP4kuDQP4mig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس اذعان می‌کند: ما کاملاً ارتباطات پرونده‌های اپستین را خراب کردیم. ما همین الان این کار را کردیم.
🔴
اما آیا فکر می‌کنم دلیل خراب کردن ارتباطات این بود که سعی داشتیم چیزی را پنهان کنیم؟ خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134572" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134571">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وال استریو ژورنال:  ترامپ تمایل دارد فعالیت‌های نظامی آمریکا را در ایران گسترش دهد، این تصمیم پس از روزهای مشورت با مقامات ارشد مشاورانش اتخاذ شده است.
🔴
از جمله گزینه‌های مورد بررسی: گسترش حملات هوایی، اعزام نیروهای زمینی برای تصرف جزایر ایرانی نزدیک تنگه…</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134571" target="_blank">📅 23:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134570">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ درباره جمهوري اسلامي : ایران به زودی شکست خواهد خورد.
🔴
آن‌ها گفتند «قابل دسترس بودن»، این یک کلمه جعلی است که از آن استفاده می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134570" target="_blank">📅 23:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134569">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
انفجار های سنگین و پی در پی در اهواز...
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134569" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134568">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
امتحانات دانش‌آموزان بوشهری لغو شد
🔴
مدیرکل آموزش و پرورش استان بوشهر گفت: با تصمیم ستاد عالی آزمون‌های وزارت آموزش و پرورش امتحانات نهایی روزهای ۲۵ و ۲۷ تیرماه، در این استان تعطیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/134568" target="_blank">📅 23:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134567">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / پنج انفجار در کرمان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134567" target="_blank">📅 23:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134566">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcZ5MekGe_zSO8EbSfTXbmPlHdIQb65vxje7O-wAikdd25QkeqemC2ozOaE2cRb8Zhpj_k3GU0ZH591Pb3f94ECK9JPuG1nnVmW7yBMMLwejBZFWMqIw-PCfl3Y1hHMTwU0MyaEwiDYdwGRaUwyqooqO3KFk_h8Lowq_hAe2PswVglubjOC7c7M6iLlAAwPcZ4q_AJgzsnAq7MtAuzwm9XG6DqcCjtKGzsITatYyg6zeaaHcuRQw3Y0s8fLpVpPnD3CsnbKfG9Gqo3KbCSPlsQDTJL_Dn2_H3XoOuLwK_u0zjx3WRSV7JVg366iJOT4V3gfMl_X2Q5qy1HtQNX37qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریو ژورنال
:
ترامپ تمایل دارد فعالیت‌های نظامی آمریکا را در ایران گسترش دهد، این تصمیم پس از روزهای مشورت با مقامات ارشد مشاورانش اتخاذ شده است.
🔴
از جمله گزینه‌های مورد بررسی: گسترش حملات هوایی، اعزام نیروهای زمینی برای تصرف جزایر ایرانی نزدیک تنگه هرمز، و بمباران کوه پیک‌اکس (Pickaxe Mountain
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/134566" target="_blank">📅 23:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134565">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: موج جدیدی از حملات را بر ایران شاهد هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134565" target="_blank">📅 23:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134564">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkvetM4zi3NhKWUDSc0kt5gaSMBcqWOCbAroA57dtW-Matb8uuL-wMoihr9axWG2uIFBwq8uD1HQ25-mVgZw3DU-NcQtGLWRfFQ9xUQJylU44xrq-nlNg980LZi6AQB-zpwJu-mIoKEzYty2Ju1TgkR_Cu6Zdy5NbTNZOcpR-Y-fAgBRIddUYkgcXm-WTu6NG8ctjYDuzI001g_gMXPPVcz36MXM2mF2_1JwMzsOmE9ejVPDVO5ZwfWxp6KkDrMXeasSwgs76hVEOFZven2n1czn74xoyNsQMFCJYKuJBtAH8zZ1zEoPkdnhr9mt1o694dEKo4b6TagUk-szdiwq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134564" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134563">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd19d5490c.mp4?token=rhri5cLsp_BGg1ieMDkllT9dxscF0cLLcKkuvrY1j3i1cL3bXgedOL-yUDao7iUg0a5tUH5AG4fgBnGvjDW7s5qFJyF_bC7LQVomMwcglpUV2jVG9605h5MapQcZ5kCejiP-RUKSVgj33xWaOTFtooPIk6AezoBprVeCeGi_LxSA6p_Z_WhObxCSDWaRxbdd6bmnNdNXJyx6IuejPuZ6_Y34OHPjHMAGdWRP_vRUDBf1BzCOU01A95kLsrZxAv-1oojkajLtVUoFalC5YrTVTRVpVLkuc50jEikl4aG7uc_d_6I4kXxdp1XSe6-gRdJge6AhODZ8K5aTgDZXL0CAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd19d5490c.mp4?token=rhri5cLsp_BGg1ieMDkllT9dxscF0cLLcKkuvrY1j3i1cL3bXgedOL-yUDao7iUg0a5tUH5AG4fgBnGvjDW7s5qFJyF_bC7LQVomMwcglpUV2jVG9605h5MapQcZ5kCejiP-RUKSVgj33xWaOTFtooPIk6AezoBprVeCeGi_LxSA6p_Z_WhObxCSDWaRxbdd6bmnNdNXJyx6IuejPuZ6_Y34OHPjHMAGdWRP_vRUDBf1BzCOU01A95kLsrZxAv-1oojkajLtVUoFalC5YrTVTRVpVLkuc50jEikl4aG7uc_d_6I4kXxdp1XSe6-gRdJge6AhODZ8K5aTgDZXL0CAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستون دود در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134563" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134562">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
صدای ۲ انفجار مهیب در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134562" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134561">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1841f7e8.mp4?token=AsSyDk0P-RXvGyx3aimMAthneulbkKy0g7DCumUUiJr2Tr4QxkWwtjw5qKjMtVPREJ8ZWyApH3Oaafyg1JvUT6Wh7QrFYdMeNqOCR420Vk9mmsp4yrqXHlWXTHIQhAIxxRio2bzSFF8Grx6WqcYk5Gvypa11MJO_p4AoenZvOS05n4nUj1YtubtDNtzN6e0gu0I2TsfYmHZmdEWACApjiFHe13E6B0B5Itk5wXreqT0quM_etOeC89WHT0lqO45oOlEpL8FZPp0oL0kvlrf4K_t7n547-U9vz0paX1kLyb3kX45PPUQduGswJ13dqozqiRQ3qDZpW8M7d4WAp0AjgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1841f7e8.mp4?token=AsSyDk0P-RXvGyx3aimMAthneulbkKy0g7DCumUUiJr2Tr4QxkWwtjw5qKjMtVPREJ8ZWyApH3Oaafyg1JvUT6Wh7QrFYdMeNqOCR420Vk9mmsp4yrqXHlWXTHIQhAIxxRio2bzSFF8Grx6WqcYk5Gvypa11MJO_p4AoenZvOS05n4nUj1YtubtDNtzN6e0gu0I2TsfYmHZmdEWACApjiFHe13E6B0B5Itk5wXreqT0quM_etOeC89WHT0lqO45oOlEpL8FZPp0oL0kvlrf4K_t7n547-U9vz0paX1kLyb3kX45PPUQduGswJ13dqozqiRQ3qDZpW8M7d4WAp0AjgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی آمریکا به بندر چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134561" target="_blank">📅 23:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134560">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
گزارش انفجار در ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134560" target="_blank">📅 23:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134559">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
انفجار مجدد در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/134559" target="_blank">📅 23:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134558">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
صدای انفجار همچنان در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/134558" target="_blank">📅 23:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
انفجار مجدد در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/134557" target="_blank">📅 23:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134556">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6068a6a93e.mp4?token=rgLBolZrugtyU7YnhU0loQxBxMhwBk0_30rEUFg0UEHoolQL_k7Wmu_dX3ZTLfpj06nS4GYr9hA2mG6ZljTZQjtOl0gshGg7jHBe1qUWp17C0jSgd3sKyw6bQfTEK7PQLPUhfQpPwhhmCpLqV-Wyga3J1bIHm_Iv8Fne7Bu_gZpRyuhIa1wU4EXAboYwuncmWjYGU0G33ihAKApZgZ_3vztmg0aYWVaEogA2Ux3oyjNqcmDdLwkP5RtjOCwGv-n6rEoHVdbBtizVrg42wEwyv9saVBO3mtdiQINtFpiBok9RgWaH_IbliPszX9TE_FI-RD2Mnp_O4G8WQYyaFyC23g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6068a6a93e.mp4?token=rgLBolZrugtyU7YnhU0loQxBxMhwBk0_30rEUFg0UEHoolQL_k7Wmu_dX3ZTLfpj06nS4GYr9hA2mG6ZljTZQjtOl0gshGg7jHBe1qUWp17C0jSgd3sKyw6bQfTEK7PQLPUhfQpPwhhmCpLqV-Wyga3J1bIHm_Iv8Fne7Bu_gZpRyuhIa1wU4EXAboYwuncmWjYGU0G33ihAKApZgZ_3vztmg0aYWVaEogA2Ux3oyjNqcmDdLwkP5RtjOCwGv-n6rEoHVdbBtizVrg42wEwyv9saVBO3mtdiQINtFpiBok9RgWaH_IbliPszX9TE_FI-RD2Mnp_O4G8WQYyaFyC23g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به این نتیجه رسیده ام که نمیتوان با سپاه پاسداران انقلاب اسلامی مذاکره کرد.
🔴
خبرنگار: آیا یعنی ممکن است همانطور که با داعش کردی، آنها را از بین ببری؟
🔴
ترامپ: "بله، درست است. خواهیم دید چه میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134556" target="_blank">📅 23:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134555">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
استانداری هرمزگان: در حملات جدید آمریکا به حوالی بندرعباس  هیچ مصدوم غیر نظامی یا خسارت به زیر ساخت های مسکونی و تجاری  گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134555" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134554">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134554" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134553">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsD4deMENxxx9JbHLhwvX0YIqOMsK7SSzyL5ULGLADsd8uUVO4lovAYG2e-vxpSub5ZtSejSIbzCPuhFWoaSW0IjaLQmtu0XMX0LkSWUAj5LWwdpovJFpI9tp7zHr5AaFQL6QyYyj62H7lITCkGV_LcFEL75QyccuRwu3EzTGqKkfKH2V0GDTrfuQ0yHu6z8MBLx04yjvdD67Wn4lT6in4CCcdzEovZtlHK3XAKAEPPhJAniBfauJTt-m-p2nYromAtU49CRcFmydkMrLTzrrW7Ma71PXBrmckJOSBO6e1NTSOxMwuAuaZHQadi8j1LFD8FWABQAOjN9TgviaaVVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/134553" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134552">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fcebb661.mp4?token=YjPmAXVAedsHLeoqLsiqzO3ZmvFpGl5vWgt_Xe_JdS58sbFwQWXFhKE22gc8tP5jOxiwi-s9NYQbkTLYqbT6dbpN4xY5DKz2tnt1XwudR13OAPpPhybr8dOGWWFZeNrBLrKsJHjIxsLa0XXjYGjtUuIVUirctvs2q4D5GvvbqEkGKx5dvAEqlq5LI44Ss8C8MpS7e_2QP9XJ_1Ptx_8GeOKHKBEc6pRN899p_Ef8tbCbIPMXBGpNZ8vXZCGUIjv5F9WI46hxEabvlixS2spYCw1D4XOETHGxEAlVhFBRqhzv5t-9thc1-PVTlixVungHgMuMv3jlCoJmYMEJqj0GMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fcebb661.mp4?token=YjPmAXVAedsHLeoqLsiqzO3ZmvFpGl5vWgt_Xe_JdS58sbFwQWXFhKE22gc8tP5jOxiwi-s9NYQbkTLYqbT6dbpN4xY5DKz2tnt1XwudR13OAPpPhybr8dOGWWFZeNrBLrKsJHjIxsLa0XXjYGjtUuIVUirctvs2q4D5GvvbqEkGKx5dvAEqlq5LI44Ss8C8MpS7e_2QP9XJ_1Ptx_8GeOKHKBEc6pRN899p_Ef8tbCbIPMXBGpNZ8vXZCGUIjv5F9WI46hxEabvlixS2spYCw1D4XOETHGxEAlVhFBRqhzv5t-9thc1-PVTlixVungHgMuMv3jlCoJmYMEJqj0GMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از وضعیت اهواز پس از اصابت چندین بمب یا موشک به مناطقی از این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134552" target="_blank">📅 23:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134551">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
به گفته برخی منابع ساختمان گروه صنعتی فولاد ملی (INSIG) سه بار در اهواز هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/134551" target="_blank">📅 23:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134550">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
اهواز هنوز صدا میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/134550" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
گزارش ها از اختلال در اینترنت اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/134549" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134548">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
تسنیم: پرواز جنگنده‌های آمریکایی بر فراز سواحل جنوبی سیستان‌و‌بلوچستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134548" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134547">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پایگاه شیخ عیسی  بحرین صدای چند انفجار شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134547" target="_blank">📅 23:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134546">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
۴ نقطه در اطراف شهر اهواز مورد حمله آمریکا قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/134546" target="_blank">📅 23:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134545">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
طبق گزارشات مردمی، شدت حملات امشب به اهواز حتی از جنگ ۴۰ روزه هم بیشتر بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134545" target="_blank">📅 23:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134543">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEI1Ih41cjn7VzVcebL4KpZnavBel7ttxx0JWC9WJDWt86w89aUqrKF_INcRkzGMfKWss76I7SWhDAbxCuKbFnjn6vlPGNw6ETtBwohVuWt5h36GPkOOq_QtBNGScsptjYnpx1Oh-rv1ut960K5aNnFNaIFUVWnvAehPfVnurtypMvlXykJ4rJQpo0hGxwC2xBh30HGlqyfdrizESf-sCL86CMEKNwq1074XKNZqjj9CF8vc5aNf_l9nf-jLDfbOV-7B0qjrYGDcUsf37zmFUOOpvL8ewrbQ6rzpcI_9GJwAPANBWrlOTaaailLJGcO6BWsSvGjysBvb7HMKnsEZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9507b8c26a.mp4?token=CJd5ZeJ61FZP0InRr7_yjFlMq-jitVNgCv7So3Bhq7Hlm6zCPBc0Hj7rXdD3M8VhBSuqLEYLhPHmfL5d8p5VVGlneaUqTRhz_IPWB53FSiBKj8FGvi_NS33dA4S6PpJKVDiLedp9xaUkEP1d4cpMgJnGQQjVAAXZLTKrgO6qNDXGet_Sk5ekx-N7Q2v-nEd926iJnWKMgbPTgxvJKVPIVK7B_fcELZTowxM_-WGO7bylghp4YcknqOHAoHZDZZ5aUySErInWarQ953afIUqVOIVf7DzbyQhV2EoOhcIeiDVcpixlqtxmn8285RKereDwhtMs3p0g2rbzOWO0Z2GVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9507b8c26a.mp4?token=CJd5ZeJ61FZP0InRr7_yjFlMq-jitVNgCv7So3Bhq7Hlm6zCPBc0Hj7rXdD3M8VhBSuqLEYLhPHmfL5d8p5VVGlneaUqTRhz_IPWB53FSiBKj8FGvi_NS33dA4S6PpJKVDiLedp9xaUkEP1d4cpMgJnGQQjVAAXZLTKrgO6qNDXGet_Sk5ekx-N7Q2v-nEd926iJnWKMgbPTgxvJKVPIVK7B_fcELZTowxM_-WGO7bylghp4YcknqOHAoHZDZZ5aUySErInWarQ953afIUqVOIVf7DzbyQhV2EoOhcIeiDVcpixlqtxmn8285RKereDwhtMs3p0g2rbzOWO0Z2GVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اهواز از شدت انفجار زیاد صداش تا چندتا شهر دورِ دست هم رفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134543" target="_blank">📅 23:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134542">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری/شلیک موشک از کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134542" target="_blank">📅 23:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134541">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893a539e51.mp4?token=DccBK-q8vuSuN0fXhpR-Az18sImDRH98jZq4xLUDTkY1LLJyY-ioru0BjKipeeOJwQEyuCXW5UWGAsxMqkoQcNY2wsCN63kuuqMRvCPSHkuIrQ10r6pj0McoDncmRUhw4rV_VB4MldwsFs-ytPwSQbTYahzVuzMFY8GjKCpmvwseXKdX-9TP07rAtqNqOfimO_MYDL62NnCIWolm2veaenCo3cCbcOkn_QIVRUkx-tRlnEkNVk82L6SM6z5lQ0pQ95YddD5ndhh3MrrIqRm8AtRyr7vyn1GyVj4vooEbojEa1RyAhnBsaEnQZ0pC_K8b6OWG63y2ZNREB6C0dkfjMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893a539e51.mp4?token=DccBK-q8vuSuN0fXhpR-Az18sImDRH98jZq4xLUDTkY1LLJyY-ioru0BjKipeeOJwQEyuCXW5UWGAsxMqkoQcNY2wsCN63kuuqMRvCPSHkuIrQ10r6pj0McoDncmRUhw4rV_VB4MldwsFs-ytPwSQbTYahzVuzMFY8GjKCpmvwseXKdX-9TP07rAtqNqOfimO_MYDL62NnCIWolm2veaenCo3cCbcOkn_QIVRUkx-tRlnEkNVk82L6SM6z5lQ0pQ95YddD5ndhh3MrrIqRm8AtRyr7vyn1GyVj4vooEbojEa1RyAhnBsaEnQZ0pC_K8b6OWG63y2ZNREB6C0dkfjMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، این تصمیم با خودشان است.
اما ما قرار نیست ۱۵۰ هزار نیروی زمینی برای تغییر رژیم اعزام کنیم، مگر اینکه خودِ مردم در آنجا بخواهند به چنین نتیجه‌ای برسند.
البته ما در هر صورت قصد اعزام نیرو نداریم، اما پیشنهادِ اعزام نیرو عملاً به این معناست که ارتش آمریکا باید کار را برای مردم ایران انجام دهد.
ما دیگر دنبال چنین کارهایی نیستیم؛ واقعاً نیستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134541" target="_blank">📅 23:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134540">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری/ترامپ: ایرانی‌ها خواهان برگزاری جلسه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/134540" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134539">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری/ترامپ در مورد ایران:
من می‌توانم به شما بگویم که آنها می‌خواهند یک توافق انجام دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134539" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134538">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383751b9ae.mp4?token=vKpGUPAkDGdZcgJxtZrghfsbzrg35Y0uI_MHx0UPNK9B_mEblekRRQ3OgPbOyeivslDBNjn-NJHWXAzHCckjACuZjGJ_0ZApJlsYRc4Y_JbTe6CcK2-9wjQ7AQyEnd0Feu-jxnDwJ6vJ4slpo419xlhIGeWwXDQleV34Pb0CzUpsqIIj-ktqOsHU2xMwp7vzkQQ72R-q5ZWQJvPPsAnDGLp7o4nmncZYA1MOOKr4ewBZfaGalO-N8ZJiPRbYTaa41OnzCiHKFDjDIBjNKlp7N2eIXBIVSHzZLQ-8zYHiG6YILensWUJoQN3g00nsWkB1xgZ29hkfzc-puL9SAVq8zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383751b9ae.mp4?token=vKpGUPAkDGdZcgJxtZrghfsbzrg35Y0uI_MHx0UPNK9B_mEblekRRQ3OgPbOyeivslDBNjn-NJHWXAzHCckjACuZjGJ_0ZApJlsYRc4Y_JbTe6CcK2-9wjQ7AQyEnd0Feu-jxnDwJ6vJ4slpo419xlhIGeWwXDQleV34Pb0CzUpsqIIj-ktqOsHU2xMwp7vzkQQ72R-q5ZWQJvPPsAnDGLp7o4nmncZYA1MOOKr4ewBZfaGalO-N8ZJiPRbYTaa41OnzCiHKFDjDIBjNKlp7N2eIXBIVSHzZLQ-8zYHiG6YILensWUJoQN3g00nsWkB1xgZ29hkfzc-puL9SAVq8zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز:
چهره شما از این پس روی سکه حک خواهد شد...
🔴
پرزیدنت ترامپ
: من بسیار مفتخرم. عکس بامزه‌ای است. عکس بدی نیست. بسیار غیرمعمول بود، اما من به خاطر آن افتخار کردم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/134538" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134537">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
انفجار در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134537" target="_blank">📅 22:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134536">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
موج حملات ایران به آمریکا در این روزها خیلی کم شده و دلیلش نامشخصه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/134536" target="_blank">📅 22:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134535">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
چندین انفجار دیگه در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134535" target="_blank">📅 22:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134534">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری/اهواز رو دارن بدجور میزنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134534" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134533">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXseAEonHq9i33dgV49Lc3ZJU4vdDpLnLVxmRr-MRHfTeH5eklbBy2niq594-moJyQtjs-mRNUN5ZaDdA42lGym7SMGCiM3gJqdX2vpb-aKym_K_7z3LvivgQR_t_gNJhQUwkVl9LNeeBffj2gIJIh-s2yUSsnHZz0MrA_IzKIqQCl6r_ZgPhF_ylIUK8ltuyE9nJRT5y_P628jI5wHlySsMOpc_EvM1ILn-3iH7aWOPwHT4lS0n604MXwXJA4HaSFe4w78yKc1wkJFZ0cDgtSLbxlxNBwthDE2e8U8wxsaWIepsmb-ZT86vgtnIPp_d-vRfP7TjTfZXg2fjvp4ICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند؛ تنگه‌ای بین‌المللی که برای تجارت جهانی حیاتی است.
ارتش ایالات متحده در پی دستور فرمانده کل قوا، ایران را پاسخگو می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134533" target="_blank">📅 22:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134532">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
گویا لشکر 92 زرهی اهواز رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134532" target="_blank">📅 22:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134531">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
چندین انفجار شدید در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134531" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134530">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری/انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/134530" target="_blank">📅 22:40 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
