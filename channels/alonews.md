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
<img src="https://cdn4.telesco.pe/file/iAxVfNDfbUhAPEbjiIMNtdLkwvqpQHsCe0S8vEat5uo-iijOSsuWHSiq4GvpfneEbRlmUFO7yGEftEiNAO_iR2XgfkdYB9ZPThUSwqJCEVLY4h0tXkvca3AuUU6J9hzoWvrayX6hDOZeeoilcw31Tw7I_m4h9k0FIJ8nGOZOdZFOjDaRv6QsdaW_ClIl_cBpinRveKR5B09GvVcGSIDljUzHuGwdGOQL-VSkwL5d-ilgxI3FgaAf-yVYQgLmynJySXAk6pAygGxPLEFHUqtJcWoyCCkAmBaKKvxU9CL0RILHTv8vowh2fo-XsHUcEMFF3x2vq84yxCI4ZbJZEdb3KA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 930K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 15:26:42</div>
<hr>

<div class="tg-post" id="msg-137481">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت بهداشت: در سال ۱۴۰۴، ۴۹ مورد ابتلا به تب کریمه کنگو و ۵ مورد مرگ ناشی از آن در هرمزگان، فارس، کرمان و اصفهان گزارش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/alonews/137481" target="_blank">📅 15:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137480">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نیویورک پست:ایالات متحده در حال بررسی طرحی برای تصرف اورانیوم غنی‌شده از تاسیسات هسته‌ای ایران است.
🔴
جوزف رودجرز، معاون مدیر مرکز مطالعات استراتژیک و بین‌المللی، گفت: "متاسفم که این را می‌گویم، اما به نظر من محتمل‌ترین راه، اعزام هزاران نیروی زمینی به تاسیسات هسته‌ای ایران است - با در نظر گرفتن تله‌های انفجاری، استفاده از تیم‌های ساختمانی و حفظ یک نیروی دفاعی بزرگ که اطراف این مکان‌ها را محاصره کند.
🔴
از آنجا، یک تیم کوچک از نیروهای ویژه، عملیات واقعی تصرف را انجام خواهد داد - که عملیاتی "بسیار خطرناک"، از نظر لجستیکی پیچیده و در یک محیط پر تنش، دشوار است. ارتش ایران تا حد زیادی نابود شده است، اما هنوز از نظر تجهیزات، پیشرفته‌تر از نیروهایی است که مادورو را محافظت می‌کردند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/137480" target="_blank">📅 15:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137479">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO8AVzHsABkEf2BsebM-u-ROFw14tWna8TM4EbhHQFcetcDxWmYGAfG7eO6W5xTMYHZ0UWZlw7NLcSAeh8Lux79KiQA3MTmAB_QVoNlPaocugcEPgJQ9j79AYdCddDv6PEUIED4PdI3AehWMgpbxKoMc7BqiMjM28S3GNTIpfKqfFcsJGI7UOAG8-hze7WUX0yM835-I1IQmOTZmxEe5CBjQk6C_16yhPwwbbj7IDCdl9ojXo6Kq_RJbui6jo2Trb_g5RB75JoOpG5Pcfc84kzuuzc5_PRRO16byS31ZHfXdSG7ruAlHdo0jZzXce3zpky-1mmFNiQowsfzCCgg6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخورد دو اتوبوس مسافربری در مسیر دیر الزور- دمشق در سوریه باعث کشته شدن ۱۹ نفر و زخمی شدن ۲۷ نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/137479" target="_blank">📅 15:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137478">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/entDWYFI7SPLuyR1i9rweZlBptxZv8rikO1M5mYemB0ikASRIzwNNrmQ6bSdABuMdgEKYIkg5lx4cNAetsaPXqN5Fdz8uhyAnrSEnaQT9DhcKDA7HVwuVPBdCQpY4tO86zsmvHn2hNMCv_R-le8xzb82iI6BMK38uEhK8whoV2hf396m6Lv9FGe3SfOgNT_IRGBFL8DcKuFis-3uoxBgqEyisyZX03YE4KLGomIM7Q9SY9ippepesSg9mgDmNsV3fANXTCg9x8WqZ2END_TfSO3ze8TfkyzG8_3r4p7Eeo2HX1QEwnJtaWmE3SzFn3NDs9tWldtdvbht0VwPmcTIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: اگه وزیر نبودم میرفتم پشت لانچر
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/137478" target="_blank">📅 15:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137477">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a782cab2.mp4?token=V1oD-uQbYbk4UZ9jSqJEzRVZ5ee2p5KyoC9jKdXHHe5R43VK8-V_elMReM7K_TFR81QRPncJTsz6fU6A8nPunRkS8lcV3IPeFEIuOnBZxjwYW2lYJgY3eg80yLrvbxAByjRCSZk-pkRvN03_YuX6yXLmKdre6teauYJMzajk0je1kx1v6ZT7WmR0QqF9652RKVzL9CifC1rZJp8L-NyoQ0Kzc7Lz4uQNLQCmFijykKqJ46NRylpVvQ1RZZ1YZH8Ue_2nNguAOS1U5t-cuioy4bDe0BelulLimO2NJjdFuIDyPiG1yew2q7yTGGIjBZXkB_voxNU26MTSFDMfsCcN0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a782cab2.mp4?token=V1oD-uQbYbk4UZ9jSqJEzRVZ5ee2p5KyoC9jKdXHHe5R43VK8-V_elMReM7K_TFR81QRPncJTsz6fU6A8nPunRkS8lcV3IPeFEIuOnBZxjwYW2lYJgY3eg80yLrvbxAByjRCSZk-pkRvN03_YuX6yXLmKdre6teauYJMzajk0je1kx1v6ZT7WmR0QqF9652RKVzL9CifC1rZJp8L-NyoQ0Kzc7Lz4uQNLQCmFijykKqJ46NRylpVvQ1RZZ1YZH8Ue_2nNguAOS1U5t-cuioy4bDe0BelulLimO2NJjdFuIDyPiG1yew2q7yTGGIjBZXkB_voxNU26MTSFDMfsCcN0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ثابتی: بعد از جنگ با عرب‌ها کار داریم و نباید اجازه دهیم تنگه هرمز را از طریق خاک خودشان دور بزنند
🔴
شهریاری، عضو کمیسیون امنیت ملی مجلس: به چه حقی؟
🔴
ثابتی: چون قدرت داریم و رئالیست هستیم!
🔴
شهریاری: خدا نکنه قدرتِ آمریکا دست شماها بیفته وگرنه پدر دنیا رو درمی‌آوردین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/137477" target="_blank">📅 15:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137476">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وال استریت ژورنال: موشک‌های خیبرشکن ایرانی با ترکیبی از مسیر‌های پروازی، مانور‌ها و سرعت‌ها، سامانه‌های پدافند هوایی را گیج می‌کنند
🔴
تهران از این موشک‌ها در حملات پیچیده استفاده می‌کند
🔴
خیبرشکن‌ها می‌توانند مسیر خود را بیش از برخی موشک‌های بالستیک دیگر تغییر دهند تا تشخیص آن‌ها دشوارتر شود
🔴
این موشک‌ها همچنین بسیار ارزان‌تر از رهگیرهایی هستند که برای انهدام آن‌ها استفاده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/137476" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137475">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2877734558.mp4?token=nL0tjJjogezJgNhuhskX4_1Lw3JuXW_CmcYwOYQXvEYVII6CchICdOd-vWvnbyMLDCzQBC91bUeOa8lzQheZr29PfrCnvWx3_UH4twIhqYmPNZhUVXnAKA6YuOtb2lhghH3lnlM7-HCsSq6_7luBidgApkh2MbZHWnxKFsb9MvsloqyYItuV6xZS0QVpnGY6eSaKIjDr8csAJ07AtXSTVcfXGxncqwT9QZch_FoFNU8MQBSdHg_s9sTA04SV2RK0V_AnTrEeymxNm8fGx_vDV4Nquw2ysfbRGf67BFk_Ot8kXwQ4c74heQDRlRztg39MKmefD4GVWm4CTCAtoPMshQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2877734558.mp4?token=nL0tjJjogezJgNhuhskX4_1Lw3JuXW_CmcYwOYQXvEYVII6CchICdOd-vWvnbyMLDCzQBC91bUeOa8lzQheZr29PfrCnvWx3_UH4twIhqYmPNZhUVXnAKA6YuOtb2lhghH3lnlM7-HCsSq6_7luBidgApkh2MbZHWnxKFsb9MvsloqyYItuV6xZS0QVpnGY6eSaKIjDr8csAJ07AtXSTVcfXGxncqwT9QZch_FoFNU8MQBSdHg_s9sTA04SV2RK0V_AnTrEeymxNm8fGx_vDV4Nquw2ysfbRGf67BFk_Ot8kXwQ4c74heQDRlRztg39MKmefD4GVWm4CTCAtoPMshQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: اهالی جاسک اسلحه‌ به‌ دست منتظر آمدن نیروهای آمریکایی هستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/137475" target="_blank">📅 14:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137474">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAPnCowLEAzsz85SUmbTL6e1niTR8OvAajhuFzA2tEZ3hZc4G_EBubkm7Fj9f7zBWeaDVH42gcKK5hFrDjjp3F5SylwPxWEK51RRcjPwZCvc1mnfsS5r8i5PDADxzm1zOQRIWllIS3hM7FVXS6FpKUB2RWmI7C8IEFXtTQC4S23pAj2AhdVRcggx1_moleND_OIEKQZdo0IzmmYbFXW-78g1FOO6aGQCqKvxsDV_BIL-QzmTbUJtST6f2OCZNtovq2d7ivkDGcvH_YSoRN2zpm1EuEecsNvUXc5dfVtwkQLHoy6jSKZ0ScAmaM-ZBazqIbPrP7GRjtRTFUUIp4G4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آموزش تیراندازی با سلاح به کودکان در میدان آزادی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/137474" target="_blank">📅 14:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137473">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjJwtu91LTVifa42C84OdtHz98U6dQ3ujFenu_OJdYWcEJ8SRWF4IaDgsAhf8EkWTWpxFo58lGgTZi4PbCbO_G62P3hBZMw5Xg6nxmoSRmVFq6daojFZladt9JP8RqxHDrrJh1AHYDli4y1Fe5g1THj6ou4Q29x3sv3ZDVrmKSYM_1k-wwapTfwc93O_Jgpgy_6FxNzuTiI8kGFSjfHo1UzCsV0Y6AedvDOs1hcnG_jE3ds2E8X8DHd9a9Mll3Q_YdSE3pclqfi-07Wbi0aGinuyxw-aJPLB74dIgVPT6nx9IXoJpM4nSbO3RMH6Db-dHFQ7BYlm7X6bKSNwRLO6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه لبنانی المدن مدعی شد: بحرین و کویت از محمد جولانی،خواسته‌اند در صورت وقوع جنگ زمینی با ایران، نیروهای این گروه را به جنگ اعزام کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/137473" target="_blank">📅 14:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137472">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
صداوسیما: در ۲۴ ساعت گذشته ۴ کشتی با شلیک اخطار نیروی دریایی سپاه متوقف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/137472" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9eae7c3a.mp4?token=T4JoR7ZyzHyM6-HxjVKgPcvfdybKqyHrwhUUOR8GmASbun3ce0P88d93drQgHue5Rz4h9KUxM2La6qwqheayh8AdP6G37BPHB7lj6xIEBGM_lyA3U0ll1CpR0RjnsgsNiaManW7ymnPybuAi09jU3jPz-HkH3GeNbTnisnNsQEJDDv738XKpwOybhBkp8GnylfKEQqLi1vNXin7uszN6ABD_3tNR_RhllSQn-7wXhuYQk37uM8IZ4drhjVxY8iqqDCA8VkFlitkF3LXReGBZ3Kl7MkzEAtwtBbKls28UjxGDgL_pYUVQJULLxTmnNQMkK4XMYwb8k7jgNpC69sHHqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9eae7c3a.mp4?token=T4JoR7ZyzHyM6-HxjVKgPcvfdybKqyHrwhUUOR8GmASbun3ce0P88d93drQgHue5Rz4h9KUxM2La6qwqheayh8AdP6G37BPHB7lj6xIEBGM_lyA3U0ll1CpR0RjnsgsNiaManW7ymnPybuAi09jU3jPz-HkH3GeNbTnisnNsQEJDDv738XKpwOybhBkp8GnylfKEQqLi1vNXin7uszN6ABD_3tNR_RhllSQn-7wXhuYQk37uM8IZ4drhjVxY8iqqDCA8VkFlitkF3LXReGBZ3Kl7MkzEAtwtBbKls28UjxGDgL_pYUVQJULLxTmnNQMkK4XMYwb8k7jgNpC69sHHqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
الجزیره: ایران بانک اهداف جدیدی در داخل اسرائیل تهیه کرده است/اهداف جدید از نوعی خواهند بود که تعمیر یا بازسازی آنها برای سال‌ها غیرممکن خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/137471" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137467">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqAriM3Sabi7Wxaha64u0i0EEU8A4EXgaqvl-Wb_tE00zOmN02ute8u2jj_un5_cpaaul6uiDFUzrypYH0pwQjF9cnWFkE-sjR3PHSPb6W2JR13Z0whgqQPxUkZSKhu29Yf-4pyf7LBdGDSKfYK3Ke7SaPe2HiayoZZ5V00d7EQvmtrDR7cka1SHsQQ9RAAJBy2cfbDPbp6AHPXbiutRFiru3-vSJLs3Ir9pxTvEeLJzbRPtpTfO9bFXO-_hcUGRb-v0_rQKkS9d2vma0J9nYRveVfV82UrpnEU1zHHXuwTSKboL4wnTvuzMb9IP9Q_doK_5xKxwRYQ7YtZhSRTgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4ku3c2Jeey6VW64AxLl4OjVFtvmeZ0xqaxp3bBkIRVE6ZIQFpphZu-OSkPEsxyKWmEY52rwECNFaTeCLB-l7ThyFeVg3Z2BuD39UfMJDi4ANrQYnlmPjMi49V6K-gY5snssXucqYdY6Jde3Y26gf0BR_IiQu3_xFQaqtUx5C0o2x-266U9Koxbbew4z_RE27X3z3xf0v_G6myqvQp6pbYshXw7VRy_gvCz-BZu3oR4V9sEC11GJ7d6jvLaT6mZvbaTjXvzbJoFJsaZ5Y4mgahj8Ed6xBajBN_dWOADC1J1o8pzsmXXMR_vo80M3_AoffUnm_suRLZmOMxd5NG3B-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdwNmRXROr0Q6meXQO97Nl5it9_D6Xks6GFruJAFlU7_w6Z9FPSby0RqEv-njjT3P2vD1WrrjSR7mtyqSpsBcSTl7xhAyITtYAuepXWisajH9GEkRrosTeAjCCGfDJ7oz9WIEbj4W7C2lWohGbF03LWvtSzHomWvP3P4vpjocH1V9fhh0yJPz0Ik5Lt2fsMFA02EoIT_nW-mZebGhyKwoUtOQDeDoE141TBrzXrxQGCXbJGxlObWJ8x5J-1JiZNWe-O92J3GlaoUsNf1XdqhCjWrT8GrxqNbsFGzvL4kE4wrIzSRwwAXpmEKKc9QAwVS8GHbTrMkffUGA54jadN2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2FoSK4bwpriq8h1cRjB4GPDfE0T0BNogGOG7TBbCnf7drSHzflW898RGIGKSo86MfCPSOfQPgfB7LSwV_D-obviyfNLGVkyBWIpVZrh3MhwfWjiiFLadeG5bstyurshe1VxDgEryiDmdcRSrdvoONA7D74IxGQx3j7iCYWQvBKkUEtUR6aiDJKSODq_NcAZUgFH6P-n80nddncF6N1aeJJrG6Lr80kU6Xs9a3HZgJwS0SS-wFGL5sdCWY5GIuuk253HKvdDD-l7V4tDbitdfEz5D_rUTTeoxMzJMbUjHmljP81Sg8eZC9TVgy3-_XxPP6pUIqq5Um4hD6fDM5dSXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از دونالد ترامپ در مراسم شب گذشته ضیافت شام با خبرنگاران در هتل والدورف آستوریا
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/137467" target="_blank">📅 14:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137466">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ثابتی: بعد از جنگ با عرب‌ها کار داریم و نباید اجازه دهیم تنگه هرمز را از طریق خاک خودشان دور بزنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/137466" target="_blank">📅 14:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137465">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
شرکت هواپیمایی ایتالیایی ITA، پروازهای خود به اسرائیل را، از جمله پروازهای فردا، لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/137465" target="_blank">📅 14:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137464">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سفیر کویت در آمریکا در واکنش به خبر وال استریت ژورنال: «دولت کویت در هیچ گونه عملیات نظامی علیه ایران شرکت نکرده است و نیز اجازه نداده است که از خاک آن برای انجام عملیات تهاجمی علیه هیچ یک از کشورهای همسایه استفاده شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/137464" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137463">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCMtpFXjUFibtblof8PTomT86GqJpiRP0mb3zeUPH7HRPfm2KxWI4zRbpcSid4HjQu7aZIvKdRZjHZaG4xHGV_p_Om47xTKM6pjvxtXg_Ww-r-dK8aROqcsI0vrOu2XnTLLz5YBfsp6fd0bHg0TBPLzUvBh3I-vdg6Pf1W14M5kAtvos2ZA-EX5DXYhCB5_xFLdV3al8NIPjxGg0ur9ZJtpzo3npDgugn_1XU1N1juhZr9ewBPDFSGWpT8QaSZpqBEFo4wHlzsxM0VJspJk5TKcIxaTAcaTqtRGyT595U53wFSnhxko0bDEFsC71XxaandEJYsIqDzE96g6Szt36Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شیخ خطیب، رئیس مجلس اعلای اسلامی شیعیان لبنان: فریب آمریکا و اسرائیل را نخوریم، به ایران تکیه می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/137463" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137462">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
دولت آلمان ۲ فروند شناور نیروی دریایی خود را که برای مشارکت احتمالی در ماموریت بین‌المللی تامین امنیت تنگه هرمز در حالت آماده‌باش قرار داشتند، از خلیج عدن خارج و به دریای مدیترانه منتقل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137462" target="_blank">📅 14:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137461">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
خبرنگار العربیه: وضعیت کشتیرانی در تنگه باب‌المندب به‌صورت عادی در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/137461" target="_blank">📅 13:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137460">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نیرو های دفاعی اسرائیل هم اکنون در حال ورود به شهرک ها و روستا های کرانه باختری فلسطین هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137460" target="_blank">📅 13:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137459">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
زلنسکی : کشتی‌هایی رو توی دریای خزر هدف قرار دادیم
🔴
اونا محموله‌های نظامی مرتبط با ایران رو جابه‌جا می‌کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137459" target="_blank">📅 13:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137457">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/994ea698fa.mp4?token=G59eJecGB9-Pkdet6d12opEmgm9I6rS0lHLAwEsEndTUkOHB1py2h7Lp_TicpWz96MsNUGs6-FlD2KYYVgBopTHKa0gHjWdK4jvhGfqLmDW521tLfysHy2iXMF74luhd3LY3maePR0OyVj3eqrqyURMd3Q8V_KBuODTyuCSeYxQS92B9EUfXF44zJByjBQzucmCebFPOresmDaUq_G9fpxSGJDXYOYj66yoGPjz5W7QLBbJV82d-8Befrz8AT7WYqGHDwK3rEuWxao3vFO2_K2qeENT4T2YGAA_K6dDNFPtMyDenTy9Gz8OoyrfGuo2cHePOIC7UXIFCSIJB3E13pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/994ea698fa.mp4?token=G59eJecGB9-Pkdet6d12opEmgm9I6rS0lHLAwEsEndTUkOHB1py2h7Lp_TicpWz96MsNUGs6-FlD2KYYVgBopTHKa0gHjWdK4jvhGfqLmDW521tLfysHy2iXMF74luhd3LY3maePR0OyVj3eqrqyURMd3Q8V_KBuODTyuCSeYxQS92B9EUfXF44zJByjBQzucmCebFPOresmDaUq_G9fpxSGJDXYOYj66yoGPjz5W7QLBbJV82d-8Befrz8AT7WYqGHDwK3rEuWxao3vFO2_K2qeENT4T2YGAA_K6dDNFPtMyDenTy9Gz8OoyrfGuo2cHePOIC7UXIFCSIJB3E13pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل در آنکارا حادثه آفرید
🔴
بارندگی شدید در آنکارا باعث ریزش بخشی از یک خیابان شد و خودروی در حال حرکت به داخل گودال سقوط کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137457" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137456">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
اخبار حاکی از حملات سعودی به منطقه مأرب در یمن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137456" target="_blank">📅 13:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137455">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rX1cUYZI-Ux_rJuvba9E2GAKLlgbU3CUKfHwsdasR-u_w_o_KCtc1cBKPXEYny4KMoi6iFfpDTQdjA5ufSvxEBwPfRsYBxJFUbuEC9dKO5ApgDHJQzcMXj5LJ964aYsvj4NQd0jPzK6xcMFVQ_-7QUq9TPovlaE5-bykPV4g8r9i3xwVqTjip28DLMw3tpeTjs82Us3BGcx9bHLrVzK7MxZS0sSBKfZPFElfwHzVQ3CJk1JPNSySjRlqV9fndrhL5VVfBQV9RAHRhjDnaI6Dq5vFL2BhbJdyU4USg9i1v5KP64aJ8QNP9WTpvL0-qDHbJX-8AYS9jWxFOPLs4M6CIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی: هر ستون دود در منطقه، یعنی هدف قرار گرفتن یک مرکز نظامی یا امنیتی و یا مالی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/137455" target="_blank">📅 13:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137454">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
روسیه گردشگران خارجی را برای جنگ در اوکراین به خدمت می‌گیرد
🔴
رسانه های اوکراینی  مدعی شده است که روسیه از یک روش جدید برای جذب نیروی انسانی استفاده می‌کند؛ به این صورت که برخی اتباع خارجی با وعده کار یا سفر وارد روسیه شده، اما پس از ضبط مدارک هویتی، در برابر انتخابی اجباری قرار می‌گیرند: پیوستن به ارتش یا ناتوانی در بازگشت به کشورشان.
🔴
بر اساس این گزارش، این افراد عمدتاً از کشورهای در حال توسعه هستند و پس از امضای قرارداد، به مناطق جنگی در اوکراین اعزام می‌شوند. همچنین ادعا شده که برخی از این نیروها بدون اطلاع کامل از ماهیت مأموریت خود، وارد چرخه جذب شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137454" target="_blank">📅 13:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137453">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=McUqpLEbIDzlpkskt9E2LD6WBINzaJz3A9FCDbWmcV-6Wf_xJdZRie5pNEnuwpakopAoSJ13hq9V1mN95U_Z5Sh8i-JPVg61BRYSqx2nerFq1137rEpFIPCmkAN5wUuHFIixeS1LWTlY1fMz-soIce5SPLUbWNmh8YqIepXumU2eHHMNcvkX-EoF6EwWxDS68pRZYwyKQjQSHWUE7xgy6ClIJLzy3X2xDJJ0jNuWnhqCribPd1Z7JECN1QE7cpoFoTrMUUyWfzkEj_amaO_Rvw90IX1erbBnUn0a_GDk8OA_7W_zf1J0nlvYZ5K7a3GiR_JJKXUbPGV4No9G5gNPoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=McUqpLEbIDzlpkskt9E2LD6WBINzaJz3A9FCDbWmcV-6Wf_xJdZRie5pNEnuwpakopAoSJ13hq9V1mN95U_Z5Sh8i-JPVg61BRYSqx2nerFq1137rEpFIPCmkAN5wUuHFIixeS1LWTlY1fMz-soIce5SPLUbWNmh8YqIepXumU2eHHMNcvkX-EoF6EwWxDS68pRZYwyKQjQSHWUE7xgy6ClIJLzy3X2xDJJ0jNuWnhqCribPd1Z7JECN1QE7cpoFoTrMUUyWfzkEj_amaO_Rvw90IX1erbBnUn0a_GDk8OA_7W_zf1J0nlvYZ5K7a3GiR_JJKXUbPGV4No9G5gNPoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: تغییر قیمت یا سهمیه بنزین قطعی است
‏
🔴
مبلغ کالابرگ افزایش نمی‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137453" target="_blank">📅 13:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137452">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
اخبار حاکی از حملات سعودی به منطقه مأرب در یمن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137452" target="_blank">📅 13:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137451">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
خبرگزاری های داخلی از یک برخورد دیگه به ساختمان مرکز داده‌های شرکت آمازون در بحرین خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137451" target="_blank">📅 13:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شرکت ملی فراورده های نفتی: سوخت کم داریم، مردم از حمل و نقل عمومی استفاده کنند و در مصرف سوخت صرفه جویی کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/137450" target="_blank">📅 13:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137449">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8vX-mViBUResNYzZaQHXDXCcqVo38egQVd7l4iPW5MpYdCMjjxw25bcAX_11kNdJnW-NGLjDLglCL2w-8sF1y_fl64ta1rNyWNl5bSpw4bsu4Dinq_EXfhoNrtAT22E5PJc7hjq-Rjb7VA3JehXEHH79A2WqWhJAvdyUr9evXRtK0iAs7vYqn373qJF8HC0hevRNw6oWfRpWX3xz4el3ZtNZuyOe4VSPXWBHyA4odXqiRHmlKx5KZYOC7SJKanZ3ouKkv4jIR44ued6lp-8_VB_UTnqhvnm3KkoXU8eXsOwAb3Zk3QoIWPjH6cxygAjQK6RE_y5TTmszDKKyxvaKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال جهانی در سرویس ChatGPT گزارش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/137449" target="_blank">📅 13:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137448">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqZkJVlPT76FqFOAyYOlIsYQLTX_hmrsmUXzepcGjbM77Iio_6jU8v4kSW23M6t24lltREsRTdz1GEKpuF-Rw3fho2RuvJPDYIdP9Vcvv1wSyc3Q8HR_rjEuH1XRakEL5Dv6CeGy6Uf0ijK4MJiCxO_VLEEC99L3_RfXN5SABdLX0CSwRcwaUVufSuCHCktmB8lx8LtOa6JxGxN8r2tpuFGyg5juzwy6kEHc5ej6iVC44KNWUDq59HAxq3GP7n5-0GPHL6zFdYEnfo-KcrtjpJUHfGNOOCx4_kW9lfIk8-UGmoO-_wp8lxgjjfB-m9oF_4-kxZhkAgecIQadqKlKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیکوشور دان، رئیس‌جمهور رومانی:
این صبح، ساعت 8:30، یک پهپاد جدید در حریم هوایی رومانی، در فاصله 10 کیلومتری غرب شهر سنت جورجه (در دلتای دانوب) سرنگون شد. این پهپاد توسط یک خلبان رومانیایی از یک هواپیمای F-16 مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137448" target="_blank">📅 13:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137447">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وای نت به نقل از مقامات اسرائیلی: بعد از آزادسازی تمامی گروگان ها، دست اسرائیل برای انجام ترورهای هدفمند در غزه زیاد شده و اینکار با شتاب بیشتری انجام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137447" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137446">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFxs3M9EYZbs-UNyreqCVCxfg3CV7R7DBKeuAym7U8loj0YE78KMfQQKuXBcKOOovkMxvgx6VoYqm-oxe49_MGHLRTru8lNL9KqYvhHWFufIJ3Gvzan94zmUpeu3UJO3B3WrahsxETtccA5QyrM7kI7llbd-olDEnUklySW3-7jWfFcASI0K1O0lLjBcE7uHnlC7KyzRaPRe7aR-DbK-D1qExdPpqJHWJ4X2isd6QLOyAfsvyXTSedHSTOJw2FmQ4bmlSx76BpFM8SB4kk35b7ROprUKGRJX8RT5mv57_YTs1HCNnQ3U3ZGHXgyunzUiGiKohPFY_yKMbqS2oDty4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره : چراغ سبز عراقچی به شروع مذاکرات
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/137446" target="_blank">📅 13:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137445">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8394759b84.mp4?token=d3bbkwLsEgp0521f8eGRxTSrw3IYlhdQ5yL6l4JCQpy4v6dTZlP8YOJ0uWqh8KjdUMrTg3rVUGaH41hpvCr85E9StsMR5cwltuaiHGqFL7Kp9UwrMQDd3fWZLXOMnWPReHgxHiI_fLu3YOMH4GEUfe4nLjue_nIvYFOhGJITj_bEr-dU4GPGsdunLO_DnnjcS76ughG2FnlVIGL6hvoxjWtNton163unyvaB0SpIUEwiQVlVRZUkF2yymdj0pLqGGK2LLDNyPhCAmWS0lVD2c6_KYUx_xTA0_KYAc8qESl5gD8chqT3yl1plucFtuB4F0A0GCIs4lB4jVD02QxAIfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8394759b84.mp4?token=d3bbkwLsEgp0521f8eGRxTSrw3IYlhdQ5yL6l4JCQpy4v6dTZlP8YOJ0uWqh8KjdUMrTg3rVUGaH41hpvCr85E9StsMR5cwltuaiHGqFL7Kp9UwrMQDd3fWZLXOMnWPReHgxHiI_fLu3YOMH4GEUfe4nLjue_nIvYFOhGJITj_bEr-dU4GPGsdunLO_DnnjcS76ughG2FnlVIGL6hvoxjWtNton163unyvaB0SpIUEwiQVlVRZUkF2yymdj0pLqGGK2LLDNyPhCAmWS0lVD2c6_KYUx_xTA0_KYAc8qESl5gD8chqT3yl1plucFtuB4F0A0GCIs4lB4jVD02QxAIfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درحالی که یه سکوت عجیبی تو خاورمیانه حاکم شده؛ ارتش آمریکا داره خودش رو برای هر سناریویی تو خاورمیانه آماده می‌کنه، به همین خاطر، تعدادی بمب‌افکن B-2 در حالت آماده‌باش کامل قرار گرفتن و هواپیماهای سوخت‌رسان بیشتری هم به منطقه اعزام شدن تا اگه لازم شد؛  عملیات هوایی طولانی‌مدت راحت‌تر انجام بشه. گزارش‌ها همچنین از تقویت حضور نظامی آمریکا در منطقه خبر میدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137445" target="_blank">📅 13:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137444">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی انصارالله یمن: محاصره دریایی عربستان، اولین گام در نبرد محاصره در برابر محاصره است
🔴
ریاض از هر نظر به اسرائیل شباهت دارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/137444" target="_blank">📅 13:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137443">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce10267406.mp4?token=Sx8OeI1WHYftYYR7649esIayUL1KXn7xTq3nVBknAD1KNl71CdhEeqJf40kh0q7CBBTNdtdpFJjmye4g1sltOLvYsfhuxLfl1ZzgBvJG9ky6H-z7sxT80ueJLJK52dAXwopg1_JyOABdnryLG-giorJ3VkJB5smWzlgGhN2zVQERNQ5sAyN0YkP2xeJdYp7n8C6s55kdjow7cBy0TdLBTnV_fbkyat9SLdSvqLzZPL35eAAtNY8ZOQQAVV3pPxNR2LFUfjYp2yCzruVUCqBpcvwhihEPs_nyDgv2vBTTbkKmdHVmsbKeO_wRS2itf2VrotpjBRpE23I7c-P710viTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce10267406.mp4?token=Sx8OeI1WHYftYYR7649esIayUL1KXn7xTq3nVBknAD1KNl71CdhEeqJf40kh0q7CBBTNdtdpFJjmye4g1sltOLvYsfhuxLfl1ZzgBvJG9ky6H-z7sxT80ueJLJK52dAXwopg1_JyOABdnryLG-giorJ3VkJB5smWzlgGhN2zVQERNQ5sAyN0YkP2xeJdYp7n8C6s55kdjow7cBy0TdLBTnV_fbkyat9SLdSvqLzZPL35eAAtNY8ZOQQAVV3pPxNR2LFUfjYp2yCzruVUCqBpcvwhihEPs_nyDgv2vBTTbkKmdHVmsbKeO_wRS2itf2VrotpjBRpE23I7c-P710viTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
یان دیومانده:
الگوی من کریستیانو رونالدوئه.
- مسی یا رونالدو؟
🎙️
یان دیومانده:
مسی قطعا.
@AloSport</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137443" target="_blank">📅 13:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137442">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ادعای تلگراف: جمهوری‌اسلامی از شبکه‌های قاچاق انسان برای انتقال عوامل خود (نیروهای انقلابی) به بریتانیا استفاده می کند تا تو خاک این کشور عملیات ترور انجام دهند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/137442" target="_blank">📅 13:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137441">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83b077ce4.mp4?token=YkRAM8f4pzf6SsSxCPJXaiuTGRj_UtG8D570donBLO_DmAVzVEHC-QTB-r1XIlUj2tFaepHktNjzcPzqdDeCs_4oFJfSDr4zrkfW437SRvcU9n0RZyW17x2K0N4BFfMZ-n6j8bZy_Z12P8LxCz025FcjVyata-mPNwtDZX1rDpljozkOTs_KLXigWUQMQbmmG67dHTi9iKWfLs7NyEQuwci84SxPdLp2nPznuQiXx-wphO08Y1C_BcTmhVS5l30769TlbzpTdd8A38n6vQ1mdNwGftbwJSzNFPHJKnGMCes8lxMYm_7-i63RIpxrb-9NBPg8lULsdbblOB1lhUGwhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83b077ce4.mp4?token=YkRAM8f4pzf6SsSxCPJXaiuTGRj_UtG8D570donBLO_DmAVzVEHC-QTB-r1XIlUj2tFaepHktNjzcPzqdDeCs_4oFJfSDr4zrkfW437SRvcU9n0RZyW17x2K0N4BFfMZ-n6j8bZy_Z12P8LxCz025FcjVyata-mPNwtDZX1rDpljozkOTs_KLXigWUQMQbmmG67dHTi9iKWfLs7NyEQuwci84SxPdLp2nPznuQiXx-wphO08Y1C_BcTmhVS5l30769TlbzpTdd8A38n6vQ1mdNwGftbwJSzNFPHJKnGMCes8lxMYm_7-i63RIpxrb-9NBPg8lULsdbblOB1lhUGwhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حرف های استاد اکبر عبدی رو باید طلا گرفت.
🔴
همیشه سیاست های دینی و ایدولوژی جمهوری اسلامی باعث شد که این هنرمندان نتونن به حق واقعی خودشون برسن.
💔
روحش شاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137441" target="_blank">📅 13:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137440">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عراقچی: صداوسیما هیچ‌ یک از مصاحبه‌های مهم من را پخش نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/137440" target="_blank">📅 13:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZL7YeIG7KacqWaRJsuM6XdTaPPngWVMtB2YOWgWaCt37elOjS1qmXat9aT3l7jIj_f53KbnrCDTLT9EXE6WFQkrkPuEy5RhAaBpTAUZ_eVwryN3HcEUSfYv3BQhkfzSABuBxvr2AfZo1_pjlOQmDd32edZeSMgoqAFu5sAJ8tPGAHkyP5tlCOSJpV8ahwhtXnEtIyKSq5io9Kwa2C_q_L3b1XgKE7OLSGLfJEp-FI51vCHmaNhRtuIr7MCBO4Tpoh9qBEhR3CHhNG6uIhWRNajihoO5FyiS5pPtuKeKKPhvvQkr5ncZEogGXW1qDo7nCGUb-ya7cYIbarr8fUQAFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1LfRP0HC1WA5mOey68MuickqfPftHSdWWIidSSWSZGRqIXLRu_oZJvBKcvH5lH7EkZ26mwZD9yS4ICZRfzHU4NX1TED9WUYOWQ_CcP4-68FbZc4I9_7lgDpTsr8LeT3tutNi9ElZ6xq46jyXTot-kbpTwRthTQPcj5z-UoEkMworvZqZhnIAqB4INE2Um_H4oUJfHnt6152VN2B12NutyISptNiQ54NPULrwS97c05vQq27i15YGdkOaCnRQeibK3h3uEtLwgTIgqjNhKBhPNzAXHOV0jKVka08XFYTJAslOosN055jvkrKva3nWIu79YjVJfuQpD2slytglZfxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1gvcoKOmtnXY7Zcm2Mx0leFBN083eyubWnC8h78A0Pv3Dk5V7m8v0OqSDDHDVyk3KxtY2kl6ZnHnrSJp4DL-6VguQoCz8WFjB84c-sCM3e0E6L0rnASPiDGioWsh5pjTiu1fHXjivgRPt_cDaZUj_sPdkDvy16EoxtE4qdNTp5iuF7e9XCwGuK0Jnud1sKsQpVlGxwk5fqpHR3sFlcl33K4XxoZUKuhG9ZhCJkJ8VAmQy-X-eLlnKAV3HD08L5FsbK6dt1QmrzfLMLOpzr7InGD8KJD4kmIqJptkGcos_HLLiQiHNOQgo4-yX-ACETx5MrDn5-RkiyP737XqCnv0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از انهدام کامل سوله مهمات نیروهای ویژه ارتش امریکا -پایگاه ملک فیصل، اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/137437" target="_blank">📅 13:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دلار هم اکنون 190,750
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/137436" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
تمامی ادارات مازندران یکشنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137435" target="_blank">📅 12:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyiqxri-QC3W-SlCz0RQEPrAOHxvh9Q-Y6yFfpMTo1NmP1HQ58xcbVYYyqV3FY94q5im3oVc12ow0PnyblnGI9ErjSRh5WXmN8irYXoH8e3vXoRhwf1CQn1YTg0rUnzyWNLi0rdIJl2EYspdhzoJyVP01khMg0s_h-D_yRTqozezj0T8InbWFHQs-3SZ3RfvXzOHMsvKFbOeUQ6SO2GOlctVbsQKqK9WxDZyEgmxz3j4bjkT0mgzSsoVJ_bhlmq69n1Hvmn7nMyht6vtDYRKMUL_xqfEDtVwCNTYFhnCLhtkUtXfFpwUv1I2gxphlmlK72idjOTvCxKN4hlXxF0Yrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش فرهیختگان از آخرین وضعیت ذخایر نفت آمریکا: کمترین میزان در ۴۳ سال گذشته است؛ یعنی پایین‌ترین سطح از سال۱۳۶۲
🔴
ذخایر استراتژیک نفت آمریکا در تیرماه ۱۴۰۵ به ۳۱۱.۴ میلیون بشکه سقوط کرده ‌است؛ پایین‌ترین سطح از بهار ۱۳۶۲
🔴
هم‌زمان، قیمت هر گالن بنزین به ۴ دلار رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137434" target="_blank">📅 12:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH7hlyb_CgY79MNOcUcCzMdaSOhAV8lfeAeDROuIjhHwCaet9Kah1JxTSkHyhsFUqlU2fjbUwiIJJ9SBiuZxQh37WcTeWVgbnVwbZ9Eat4kHk3k-vNDJtuQ77P3qW0FUAuUUXH7KAm6IBI8QDZor5ie0beBupMua4ikpAGuVOekF0Ac93MDBG_-EGrrnYGWsV5NF0uiyw16hWKfedt1x22RZiSaoKGzB_-WCnd3uo73sVCa0pblqLC-ymijP3GkmjAqPZG617EKUO9PSAnddK2vq2PwZSk09PMksO9pCbdfwYB5E2Suw0EuwTkuySTmradXxoVqjNQ-CZFH-7SYv8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت فرانسه در تهران روز شنبه سوم مرداد ماه، گزارش‌ها درباره بسته شدن یا تخلیه این سفارتخانه را تکذیب کرد.
🔴
سفارت فرانسه در پیامی در شبکه اجتماعی ایکس با انتشار ویدیویی از نشست خبری سخنگوی وزارت امور خارجه فرانسه که گزارش‌های منتشرشده مبنی بر تخلیه سفارت پاریس در تهران را تکذیب می‌کرد، نوشت: «شایعات مبنی بر بسته شدن یا تخلیه سفارتمان در تهران را تکذیب می‌کنیم.»
🔴
خبرگزاری دولتی فارس روز پنجشنبه اول مرداد ماه اعلام کرده بود، فرانسه به دلیل نگرانی از افزایش تنش‌ها، دیپلمات‌های خود را از تهران خارج کرده و سفارت این کشور را تخلیه کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/137433" target="_blank">📅 12:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137431">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4TOt17j5yE1RP6QkStuB-es5oaNO0sooDYi1wTsKXRC6F4HdcQ6b0UCzAJ4srFwfHkMDhreAaLAyeFu4MERrhVKsOSKNBAhNlki6OOOtTeDXskGtuOuDYoHlDWrXtW4LTOugsAfNaButmES1dk7L0lIhNNDcJ7WEaxT7VX1fkOZkVupbXZRb5Dkt5qg14v7qjo3wlPk8rmtQqj-rpFVx-FcLb3P1UreE7c-ddnfCj29wizuEBJWUiY8gPiKZaa9mYFna5u-ol-x49RdF8xmGB1CEfPfXv-8LhUc8EczqSv12W6LiFCGPHaket-gs5-yCxXDIVXMf6qajzX3n5no9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1gV6hlFGDGFCwj0paKqyW4ICMPxSFiN6U4vfy_JhufRgyMUMYweWgsRnPIUpmueK1I07fgUsO4vU7eWdOv58IRgWFD-g0iuWB6s8N2zend2m17s43TwvOg5kCvMnBZlCOpQPf1b5VPszp7WiXWlhjOSWibPxP2M5gWM-xEMMoBwSnF9LpaQ58nx6R0kIQ6rUbhlGs1eH2p5C1tPIaCQMjqxopWuSngTEcE1vBnrSiOvExpYgzqgzO1WH8X8ybimOsYQ3NLw5X4j8j00AcXB0w8iLvwEl59oAwkQmG3hzTmo-uVNrO3mSwPbGSthxCHlzD2s51Y74PxYrxpmq_5F0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بعد از ایمان صفا؛ مهتاب ثروتی بازیگر، هم پیراهنی به یاد جاویدنام حمید مهدوی به تن کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137431" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137430">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزارت بهداشت: شب گذشته حمله‌ای به کشور انجام نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137430" target="_blank">📅 12:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgvtU7fE4UrIf-jbMpaVCvq3n1Nc6A7H41srAjkvhNE_bD4YhE-yQR9ehkgHG32iEN-F8s5riA9C99Ce2b9kbmHURqWr4Kx9Rjop1k4qUcZTEORdqUq87iUPevWTRRUuc7BrJ8ANfHuJTVKvAG8inWgWlAgMlXow8GSnDqEEierNsmhOfH7y_2MxyVnl43NlbuYwBpbuClEMcYytg6g04oyIByCQN0EN8afVW7A0L6ZFEsoRgZnOXI0SXqioiWc8KK4edMEtEmQf7ZCrY_4JnOfUtbDnWALfOVqMpAQaq7sa-ndncYnGQl1a2fC2hq4IkqpmG0sWr4PV1rVNgLz8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با رشد ۱۰ هزار واحدی به ۴ میلیون و ۸۹۴ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137429" target="_blank">📅 12:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
مشاور امنیت ملی کاخ سفید در دوران اوباما: توافق هسته‌ای آمریکا با عربستان می‌تواند مذاکرات با ایران را با چالش جدی روبه‌رو کند زیرا تهران چنین چیزی را نخواهد پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137428" target="_blank">📅 12:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137427">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAwZI26yW25GRMjJQ3Buw9NS9GBXouVVtKmN_F-hvT5RiPst3KO4haqw2moeBRyke488YE5z1vPTyBZgMQbSfHRUuylplFs1Bbuf5rHS_w5kQ_1-O2Lq1VlV3u_pCmiY8Lhvtpx9HqqvIc6oHvz1noVjEdgOeTA5XoCdX6vo6j7FbcRgoffzhMhB-ID8HRTFyO0akr3P2NosCUQnWtLNprSzEKS1RGv0qbJwp8XWvu6knbwNLDqHGvi8Hql4Nr9Fq-w5aLjw7MhZaxQ1ftkA6zSbBGiOI5BCZtWsfs35DvvP3foxEbgDQyyAzEk2UWo7P200kIKU21xTSZhXR2DlZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) امروز اعلام کرد گزارشی از وقوع یک حادثه مرتبط با یک نفتکش و نیروهای نظامی در دریای عمان دریافت کرده است
🔴
این نهاد در اطلاعیه‌ای که در ایکس منتشر کرد، افزود مقامات از این حادثه مطلع هستند و تحقیقات مرتبط همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137427" target="_blank">📅 12:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137426">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / گزارش ها از هدف قرار گرفتن یک کشتی در سواحل عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137426" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137422">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIuDJMUZUGbbDrr_UecvVPhDi7jhm-DPo1rC9j2NMljUKAuxxNmESMSGGNYLoXQbIN8Tc_FNmqzdYpxyBkTmo6Z-3B8B7i4qO5ZOF30UTBF7SO0SCy5mXau2rixOsemj8L3qzpmhSM2SjeoE50EVU37RpPqwCJywu3LwttaGzUBnvmQB8halQ-zke3I_T1n9b7q2WoRl7rXmoMGMgX0M0KuJwIGItNczLRGyXcgkV1BpAQgbEb07weA7SQ4Z_02UsWIFWpGwtvnCfEu3Fuyj_70HDEde58xJv1v5nr21n4eu4zSjZFuYHwE2ZJRlWtPYvMYqdBOVyTADl9KIcCg7qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFqmRZb-u3jSxCqyDwDEW6LwV9XOeWrrqeaeh3352V0hb_P0I7ctSqL-EZjkeWF5aqL0Z64X941RscP_CR5z09Y6XLU3i5735pZPCCLAyiPTKmnujnN_2ST3l24RT-LBRap9y1rFjan7UJ_04bbYMrGs5bOnjHAm-xhDB_hnm1FlnRXcIerEWi39OeJjiqWzw5qqT_Wl3rbEzTBMKWUHVdsrlBKH9mz-1h4FLgU3oWosZaVCxAMbDSWMrYvJ3g8W8YLaTxJtzHJhnlYOKxF9Ft8Y5uBjA-M6XBZk4xFeXGFlVDueM8qG514g3716Ebc2Qu14ap3SYBUtbkt2_NA3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZXHVdzYE2MuWli0cXydPOUZc5MIbUE5bivS0HjwJeSRKF6ZsexAzauIpJB-AhVaPi5MO9vS9qYEHiyz1IXxgs2bcAkcPBYW_Zg866HiRyHaJhn6GElGaFYugSMkuZYWt1-V9kQ6rwHvRpGDEsoKKPgnhoO6GBmRxc6m1gyw3-_6hfSCbw8-VRmOApqo4CqdVNBvQyic05GhTLYvapU6MB3q0z6FDB7cbvI62k72JhNcbB_zEEwUaV_Qj3gGmeWWpGeUDsmXA9CAyFoI3OURSq4Sc1DO74I4fGI7weYfo3x-AkVxA-BAMXqvW-nm80S_v-jZe9xqC716qZFMNX3NUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da4780fd8.mp4?token=uf-tTTbK4DbKrjfOQluyWgA1LgWGzxXyw1LizJEyeHH84w2T3vo281G9RPDCgs8vIDVl47f9mT4n_qHGruSxhtvQcBxhk4Tg9S5BkCWNOhuSPi0TSXClCj_NeZqXTB_kCu2HEC9W02WL2holvywSYvQQKSAxoNjBGhxZDef1_d3rrV9sxhZ3B7aCZ6cIhnWsEs_EI5CmeioPjvOhKcr9IP3AGiI-j1TLcN-0XaWRjp_npxmbyr0o0il5IHEV2_3yJTnNFqG9cyYXx7JXBDO7TM8wcfDNwiKy8CSqn6DTjQTTRlf211qTOify1g0h7CBiFprnd-oFx38_HfyCXqeWkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da4780fd8.mp4?token=uf-tTTbK4DbKrjfOQluyWgA1LgWGzxXyw1LizJEyeHH84w2T3vo281G9RPDCgs8vIDVl47f9mT4n_qHGruSxhtvQcBxhk4Tg9S5BkCWNOhuSPi0TSXClCj_NeZqXTB_kCu2HEC9W02WL2holvywSYvQQKSAxoNjBGhxZDef1_d3rrV9sxhZ3B7aCZ6cIhnWsEs_EI5CmeioPjvOhKcr9IP3AGiI-j1TLcN-0XaWRjp_npxmbyr0o0il5IHEV2_3yJTnNFqG9cyYXx7JXBDO7TM8wcfDNwiKy8CSqn6DTjQTTRlf211qTOify1g0h7CBiFprnd-oFx38_HfyCXqeWkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تأسیسات نفتی تو استان تومِن روسیه، هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137422" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137421">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رویترز: سامانه پدافندی یونان که در عربستان مستقر شده بود، توانست دو موشک بالستیک پرتاب شده از یمن را رهگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137421" target="_blank">📅 12:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137420">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی هیأت رئیسه مجلس از ارجاع ۱۲ طرح راهبردی تنگه هرمز به کمیسیون امنیت ملی مجلس خبرداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/137420" target="_blank">📅 12:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137419">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANHJOp5diAotLQO4C48JtazgngvuXS5UUo_k_QOgrCtr6yq90UvGT0EgONleLPfFVPmON5It6dgBtGmOet9BoRlVgKD8yNU8IhWsJ4buzVCvJM2z3NVhJ_qXXcwGLyrcDKdhVawJWJ8mG7ZKM5m8-2Q_0gFxcwK-sYZXIu7P9BV8upllbniz0THiS-z3BxZ4IDwWV-mZs06ANxwLQG4czkzEDzGSX_ZmCb9Z2zP0mX4B9PAK-iCY7WZ_zAkcatVBPosfHX-GPjqsDMe4hb6YAqqfpTSm9jiUKcN35mrZVkmh_U5V92bJjcmSGCqTEaTvT1nvDYp7EqV-R5c_UU_pmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیم ایل سانگ رهبر پیشین کره شمالی که با وجود علف خاری و بدبختی ملتش پروژه اتمی را پیش برد و تمام ثروت کشور را صرف آن کرد و سپس پسرش کیم جونگ ایل بمب اتم را ساخت و کره شمالی به یک کشور بدبخت تبدیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137419" target="_blank">📅 12:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137417">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSFNZFWA7ihgaTArurNkGJR0pUDvHG32dSlSj7Xn-eh1rqKb5946g-TaRsQCvYadj9r107_G0X5vscdd5uEQF1lXfFKRepirFL3IPmE92m57SjhqNU0_r0KjWgJQFqHeRHOcVG8_Lnj0mPP6lkp2P5k1-Jmd0mBK0pPuTUr1RaYRjo2mBTYBdaFqvt3QetzbNc2vshFdpDYE0LDpFjErtWXrdlWqx4oPScnsERL_mtdmE9naxLIbDE5YIDKCaDYJFnRlcjFx9T4YZVHFlb9MtCleRVqWtgcSfchHUkYnQEr6o2dupT0zqlL5DsAbt_eIcubxn5d2B17JRHVpy251hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9zDYUGo5wM_W90YYwED2w9ZElE793BqFQRXkKL1J6gwYrkjueOQFQUOSpGOUR6jTxM0Ct00G0C_ehG-ox_PKAtFZC5yeapw1QJINstHyFAksjhQE2iSg4ieuI4VjEDL45ntvWoUEhR9DttFYKs6N6ETukVu8L3DSq1Ht3GH2u_X6iYN82ahNW_vPt_SKemadqT89luSC3VCoJG_Z5dmE6UfcRD8rz1ZLI82p7nh5hfX49iz-dNBnDRXJe1J91M7qsQHqFy5wkdjjP5TnHQ_Uav0fzVEvzteZEq3OOCFUM8tvGtq3hCdrzkeagRj91aC8ZjDeMFomLgA3IqOHbf3Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک هواپیمای سعودی که برای سوخت‌رسانی در آسمان یمن پرواز می‌کرد، پس از شلیک موشک‌هایی از سوی نیروهای یمنی به سمت آن، از حریم هوایی یمن دور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137417" target="_blank">📅 12:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137416">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162e46ebc4.mp4?token=SqOxBDaArMKJvvENl4fkHGKQ9AqMkJYcrzgTeuMMZ5RWkBQzlDIyGFZtFR7Rg25ucx8JyokksNpOVMrhtbS32A5O40h-iFn7hUaE97KysBrkXS3_3zumDGKMUn07EqNqFyza8yp9aoG3XDzOmICRuzaV0un4rUvHevhoUiEj34ASjL5Z5JemAIdUyexNdqdIESZf2aph6i3qyAZmwu2h49XOM3QB2j7cSyRwKDpBhglFZGA0EJP09aCzlKGTMNWscpWADoBFrkUV0tHAkvyA8GMb9W_26RkdoKHDsOfQqMEBT9d8B8Ng0qT3f8UJQXnP0xwcNPxleh4GuRmAcBH9Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162e46ebc4.mp4?token=SqOxBDaArMKJvvENl4fkHGKQ9AqMkJYcrzgTeuMMZ5RWkBQzlDIyGFZtFR7Rg25ucx8JyokksNpOVMrhtbS32A5O40h-iFn7hUaE97KysBrkXS3_3zumDGKMUn07EqNqFyza8yp9aoG3XDzOmICRuzaV0un4rUvHevhoUiEj34ASjL5Z5JemAIdUyexNdqdIESZf2aph6i3qyAZmwu2h49XOM3QB2j7cSyRwKDpBhglFZGA0EJP09aCzlKGTMNWscpWADoBFrkUV0tHAkvyA8GMb9W_26RkdoKHDsOfQqMEBT9d8B8Ng0qT3f8UJQXnP0xwcNPxleh4GuRmAcBH9Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آبفشان چابهار با وزش بادهای موسمی اقیانوس هند و بالا آمدن سطح آب دریا، حدود سه ماه فعال می‌شود و از نیمه شهریور دیگر این جاذبه طبیعی قابل مشاهده نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/137416" target="_blank">📅 11:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137415">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
تماس تلفنی وزیر خارجه مصر با عراقچی و البوسعیدی
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/137415" target="_blank">📅 11:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137413">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oB52eIqWik-C_7CevxGfGmDZYWa01MdMA-87KvKyQUPNL5KVUGvvy00HHypabUoOHkrqwJC4Mgk39Iz1CAmaDLW1sTBLW7EENPQpYDOs9pUbNL3b127ysqau8dHuhq4OceEADN_VEEai_JBmp6FaIWlQNZhVB06cINZFeLL2AgA7FR8xSHPZg4XPNjjPS5OXKct8SG9COyM7tH6q6SJ-lBGhDM1SGxylBQdm3x3BsJuMh4vTwXWVTgTOLTbXBCdwMw7qP2u1pzI-cwYnfuLEIwj0kQNG59-sCu5YaoAe5eqjNOAffV5E_S6tmcqNqAPDC61ZycKgVJeDmbU-C99Nbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qwsv6LMUH8-ZigOEcEUVTJ7TCbgPPV9xukougT2w478ebs56Vqp-Bt7NL7nqEk38PQLjcBYFUHZfeZeBjiv4lcoNVfkzYOHkKE2PBiJRmX193QjyDyaZYtY1OM0ZLQcppcOVtNtVfgtpCSAFtb2aF6GkLZWO-DG5AFVw2JGZBMH8fNK4_m3c2mPOFKVzFgpjJVZke-ACndK4Lo5niQu9i3_Qt5rsNVi1E9gDpj0G1hP6pPf_apFGluI8IFfKwD873YDqoOs4ODUs8-UA6IybMad4mIpbh_VaFBvjC3Zzf13JpdRBNvm2wTWp-JTWdnn6oPHGDU2O-MYiRwkqs91VKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اوکراین بار دیگر انبارهای شرکت لجستیکی وایلدبریز (Wildberries)، بزرگ‌ترین فروشگاه اینترنتی روسیه که به «آمازون روسیه» شهرت دارد، را هدف حمله پهپادی قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137413" target="_blank">📅 11:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137412">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وال استریت ژورنال: کویت و بحرین با پشتیبانی امارات به ایران حمله کردند
🔴
وال‌استریت ژورنال به نقل از منابع آگاه گزارش داد جنگنده‌های کویتی و بحرینی اوایل ماه جاری با پشتیبانی دفاعی و اطلاعاتی امارات، حملاتی علیه سایت‌های ذخیره موشک و پهپاد سپاه پاسداران انجام دادند. امارات نیز پوشش هوایی دفاعی فراهم کرد.
🔴
یک منبع در همین گزارش ادعا کرده عربستان سعودی در حال بررسی پیوستن یا عدم پیوستن به جنگ علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137412" target="_blank">📅 11:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137411">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
زلنسکی: حاضرم در آمریکا توافق صلح با روسیه را امضا کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/137411" target="_blank">📅 11:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137410">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d41997f2d5.mp4?token=Vrc9dT9dVRRgOWH2F7JRjUd1qs39WgmV-32fQhH1ofmuhdMzZZEJOu06PTtB4iNkk3mndpPZMxfaTela7J1pLWltzb-tY7r1cdpegvEQ3nUrH5cNK5G0iCP3BqPjrQDXtZ6wiqf6K4K59BMQQyaYewUkMAeLW39oPVlWu89T-NN4ygsXYUEoz0BH7S3KjY-vtGiBElPfcO06IyhlyNlULnMoH7TrWjOJQoHi4kle1k2YuwTxFiPOvtjPB41u5SzQTOuH9-zqQGFlqbaWhjYu57756c874OpZNA9Za50zY0pfU1r7OWuUvmRBO8EfzW-FkmlHs2cAxy4laeSs2U1qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d41997f2d5.mp4?token=Vrc9dT9dVRRgOWH2F7JRjUd1qs39WgmV-32fQhH1ofmuhdMzZZEJOu06PTtB4iNkk3mndpPZMxfaTela7J1pLWltzb-tY7r1cdpegvEQ3nUrH5cNK5G0iCP3BqPjrQDXtZ6wiqf6K4K59BMQQyaYewUkMAeLW39oPVlWu89T-NN4ygsXYUEoz0BH7S3KjY-vtGiBElPfcO06IyhlyNlULnMoH7TrWjOJQoHi4kle1k2YuwTxFiPOvtjPB41u5SzQTOuH9-zqQGFlqbaWhjYu57756c874OpZNA9Za50zY0pfU1r7OWuUvmRBO8EfzW-FkmlHs2cAxy4laeSs2U1qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد صاعقه با موشک چینی در حین پرتاب
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137410" target="_blank">📅 11:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137409">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFvfHEoou6SK7mR2B7889du-xsQOeM4BQFMdBwhVmI8Kl3tEMQROAy5J6-CE4OH6jd-ZZrnJaug4qkkOcGjPTXz0eyHfYThWK3rNIaFe0CMsw3zSam3YACRogc_gUmXBRB9Uyr-qlW1m6lhQ9I962i94ApEhikJH0cwdY2CDRSTojfG4TDTAFdKw2PnLARfjx50nxByPON7ZppPH35P_GSG0hUruR8nXLoyvC8YCkPf8dWADZmGa1glLq1E7C3Op6oPEsirgmoN1wSjau8mE-dWvl2hG_KXScAzd8DP-LiRDv4zi_zOXsg5Jwuykd8lmZ_e4MYDG2nF-Ly-6XmTPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهریاری، گوینده جمله تنگه ارث مامان ثابتی:
متوهم ها باید قبول کنن‌که آمریکا ابرقدرته و حریفش نمیشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137409" target="_blank">📅 11:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137408">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
اتحادیه اروپا به درخواست دولت امریکا پذیرفته است تصاویر ماهواره‌ای این برنامه را که منطقه خلیج فارس، از جمله دریای عمان و مسیرهای کشتیرانی منتهی به تنگه هرمز را پوشش می‌دهند، با ۲۴ ساعت تاخیر منتشر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137408" target="_blank">📅 11:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137407">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مشاور مالی نخست‌وزیر عراق، مظهر محمد صالح، تخمین زد که جنگ ایران بین ۴۰ تا ۴۵ میلیارد دلار برای عراق هزینه داشته است که ناشی از کاهش شدید صادرات نفت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137407" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137406">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK9aL7xTbwq0KyNUsrxDchK9HW8eQM3gXR4McbrGlIuKtE0eT5B0_0FkEQbxAMaRvHO9U0AQdWX51ETWWU4b9T9iLeJ3yA5RgoAOEenpdNH2oHVRHc_uaClR9X57W8y9HsJUs9VSUyC-V5TnJO6zi8QGX5XrJOnH1umc8BU42ly3eddoWCcPunbyF9ciKnwb4dCipwdFh3v_TMRhiuqFAQa5IcF1PrCdVM48EdEOtp9UVqzSYu5r4mW10PGDRGOOvRA3L5lLc2SPWx1vF3PLpT9Z4aQrpcgmtX0S79TNE44-OZewNeV4GxnKPEDEazL3tXppnBa6QVJC5SysnLk3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی: توافق قطعی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137406" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137405">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137405" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137404">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزارت دفاع یمن اعلام کرد که پدافند هوایی این کشور با شلیک به سمت جنگنده‌های عربستان سعودی مانع از ورودشان به آسمان یمن شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137404" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137403">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
شبکه سی‌ان‌ان: پس از ۱۳ شب حملات متوالی آمریکا علیه ایران، فرماندهی مرکزی ایالات متحده (سنتکام) روز جمعه هیچ اطلاعیه‌ای مبنی بر انجام حمله جدید منتشر نکرده است.
🔴
هنوز مشخص نیست این موضوع به معنای توقف عملیات نظامی است یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/137403" target="_blank">📅 11:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137402">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز: برای اولین بار در دو هفته گذشته، نیروهای آمریکایی از یک دور جدید از حملات روزانه علیه ایران خبر منتشر نکردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/137402" target="_blank">📅 11:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137401">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
به گفته برخی منابع ترکیه در حال ارسال تجهیزات نظامی به حکومت جولانی برای حمله به حزب الله است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137401" target="_blank">📅 11:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137400">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در شهرستان ری
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137400" target="_blank">📅 11:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137399">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بلومبرگ: عربستان سعودی در تلاش است تا یک راه حل جایگزین پیدا کند، در صورتی که حوثی‌ها مسیر باب المندب را مسدود کنند.
🔴
طراحی یک مسیر جایگزین جدید که از تنگه باب المندب در جنوب دریای سرخ عبور نکند، یک کار دشوار خواهد بود. این امر مستلزم استفاده از یک یا دو خط لوله اضافی، تعداد زیادی نفتکش و همچنین تلاش‌های دیپلماتیک پنهانی در خاورمیانه برای حفظ جریان امور، علی‌رغم تهدیدات موشک‌ها و پهپادها خواهد بود. این کار نه آسان و نه ارزان خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/137399" target="_blank">📅 11:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137398">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlUzoXS74IYTiixyBv85IO309-DO--cxDk1dulItCcpnyxgi9mH_yMQ9c0R8nq6w_t1O4iRU0K9RCzeVttEreazBmcqklBrOq5HGosaxdLuM6t-6X8joZlwMTWYPwRU2M-JM5bUJIgx2MfbNOPPJPFtozxDbqVVGEfLvimz4b8XsAx0I5a6qqkabjL3N8s3_5P78v1xhbAbFWCYhzJbgNSP_WFAaP8TBC5N_jiYY8aXEVMULH1QLuWSR5uzu4Pl7IPq_spZGX8cr9nET-44OnsWUjLcVfp_C3hwNwocXFtrG1rOlRIOFUyxEX4EmlsfnEZ66ont6QOBhIV1s4-kPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری اینفانتینو رئیس فیفا، برای تولد مهدی مهدوی‌کیا:  «صمیمانه‌ترین تبریک تولد را به یکی از بزرگان فوتبال آسیا و جهان، مهدی مهدوی‌کیا، تقدیم می‌کنم. دوران درخشان بازی تو در سطح باشگاهی و ملی، به‌ویژه نمایش فراموش‌نشدنی‌ات در جام جهانی ۱۹۹۸، هرگز از یادها نخواهد رفت.»
@AloSport</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137398" target="_blank">📅 11:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137397">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری / آکسیوس: آمریکا و بریتانیا در تدارک نشستی برای تشکیل ائتلاف دریایی در تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137397" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137396">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
مدیرعامل شرکت توانیر: از ساعت ۱۰ صبح امروز (سوم مردادماه) برق تمامی صنایع دارای حتی یک دستگاه رمزارز غیرمجاز به مدت یک هفته قطع خواهد شد.
🔴
تاکنون نزدیک به ۴۰۰ واحد صنعتی مشمول این مصوبه شناسایی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137396" target="_blank">📅 11:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137395">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
شرط واشنگتن برای فروش F-۳۵ به آنکارا
🔴
سازمان‌هایی که در ترکیه فعالیت می‌کنند از طریق شبکه‌های مالی و صرافی‌های ثبت‌نشده و فاقد مجوز، برای جنبش حماس پول ارسال می‌کنند.
🔴
این سند همچنین آنکارا را مسئول تداوم این وضعیت می‌داند و تأکید می‌کند که فروش جنگنده‌های اف۳۵ به ترکیه بدون برآورده شدن پیش‌شرط‌های لازم امکان‌پذیر نخواهد بود.
🔴
ترکیه باید تضمین دهد که در آینده سامانه‌های اس۴۰۰ یا تجهیزات مشابه را خریداری نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/137395" target="_blank">📅 10:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137394">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
استانداری اصفهان: احتمال شنیدن صدای انفجار در اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137394" target="_blank">📅 10:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137393">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
هاآرتص: تل آویو می‌خواهد تهران را به حمله پیش‌دستانه علیه اسرائیل سوق دهند و در نتیجه برای پاسخ اسرائیل، مشروعیت بین‌المللی فراهم شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137393" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137392">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2e0a325d.mp4?token=DzRzHVzrunNmvvjAUqRFXSoSab_ms3g-03n2rxLSQckpZ7k3LPlKC5Ggx73jo_CcZ4a_ojmfXhngxCnNimA17kaIz0nuXDkeqXNEezH5HZ0TeV6oJO-xIt86IUvYDLuhxM9kTtgstDAqw8t62NhFgdseBGdq7fBIztDj565_Soi_Up8PggsJWp6I2o5PFArqSeKcBGCffMFbl4owabFZdJQUVEDGAP-euLyPELryQJkCjA6zEJEtjpGqBVlvSb-UZ1edcBwjBr_otAWq1EiHT-g-_hidyWsi-y8STfHVm1aaZx8zID4AAc_pPS4LmIxtlAfXfAqBJnj7dsBYSmfpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2e0a325d.mp4?token=DzRzHVzrunNmvvjAUqRFXSoSab_ms3g-03n2rxLSQckpZ7k3LPlKC5Ggx73jo_CcZ4a_ojmfXhngxCnNimA17kaIz0nuXDkeqXNEezH5HZ0TeV6oJO-xIt86IUvYDLuhxM9kTtgstDAqw8t62NhFgdseBGdq7fBIztDj565_Soi_Up8PggsJWp6I2o5PFArqSeKcBGCffMFbl4owabFZdJQUVEDGAP-euLyPELryQJkCjA6zEJEtjpGqBVlvSb-UZ1edcBwjBr_otAWq1EiHT-g-_hidyWsi-y8STfHVm1aaZx8zID4AAc_pPS4LmIxtlAfXfAqBJnj7dsBYSmfpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کتک کاری پسرها بر سر دختر در یک ایونت ورزشی در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/137392" target="_blank">📅 10:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر امور خارجه: آمریکا می توانست از طریق گفت‌وگو ابهامات بند 5 تفاهمنامه درباره تنگه هرمز را برطرف کند اما راه دیگری را انتخاب کرد
🔴
استفاده از مسیر جنوبی، حدود ۱۰ روز پس از بازگشایی تنگه آغاز شد. از نظر ما این اقدام واقعاً مغرضانه بود.
🔴
آنها می‌توانستند اجازه دهند مفاد بند ۵ روند طبیعی خود را طی کند و سپس در پایان مهلت تعیین‌شده، ارزیابی کنند که آیا شرایط به‌صورت منظم و مطابق توافق پیش رفته است یا خیر.
🔴
اما آنچه برای ما روشن شد، این بود که موضوع فراتر از یک سوءتفاهم است. به نظر می‌رسید آنها اصرار داشتند که در کنار مسیری که ایران برای تأمین عبور و مرور ایمن و آزاد تعیین کرده بود، مسیرهای دیگری نیز ایجاد کنند.
🔴
آمریکایی‌ها کشتی‌ها را از مسیر تعیین‌شده از سوی ایران دور می‌کردند و در عمل آنها را به استفاده از مسیر دیگری هدایت می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137390" target="_blank">📅 10:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137389">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f61992002.mp4?token=XlEFNcZmwEhTzJfnrnCKUZiNVieNspGYr5gjswzcXyJpxlAFla1jdxreO_1skoaZ-SG8-RHopKgcM5qMprOFAZu5wPJEnMu_3cwtAHe5_hMKsklF5ibp5DPJgGfrmc6h-ed_w2I38h78A5y52vim96yCCr2hvuo2Z31Glt-PHTRIPJ9B2i8sumiv5Na27gzAiE6djLQwxv9JgdxGx0F9KEPg6Has1pLuUEvYRT3-wVdt7fJOuntHbx2Z15PIgQqwkhx_bTRJXh9fcY9cYAAdL1ytKCRgCrSM2_Vhld9j4nJodVO_V4hYaED6ZtX1IeLPfX967CNtK1pjtw4ACAKOyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f61992002.mp4?token=XlEFNcZmwEhTzJfnrnCKUZiNVieNspGYr5gjswzcXyJpxlAFla1jdxreO_1skoaZ-SG8-RHopKgcM5qMprOFAZu5wPJEnMu_3cwtAHe5_hMKsklF5ibp5DPJgGfrmc6h-ed_w2I38h78A5y52vim96yCCr2hvuo2Z31Glt-PHTRIPJ9B2i8sumiv5Na27gzAiE6djLQwxv9JgdxGx0F9KEPg6Has1pLuUEvYRT3-wVdt7fJOuntHbx2Z15PIgQqwkhx_bTRJXh9fcY9cYAAdL1ytKCRgCrSM2_Vhld9j4nJodVO_V4hYaED6ZtX1IeLPfX967CNtK1pjtw4ACAKOyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روی آنتن زنده، مشاور قالیباف و الله کرم، نماینده جبهه پایداری دعواشون شد.
🔴
الله کرم: شما مذاکره کردین که هسته‌ای رو بدین بره، من به عنوان نماینده مردم نمیذارم.
🔴
مشاور قالیباف: تو خر کی باشی نذاری؟
اصلا کی گفته ما قراره هسته‌ای رو بدیم بره؟ شما میخواستین قالیباف رئیس مجلس نشه ولی شد.
🔴
الله کرم: نذار بگم قالیباف چطوری رئیس مجلس شد !
🔴
مشاور قالیباف: سیکتیر بابا
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/137389" target="_blank">📅 10:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
اوکراین: حداقل ۱۵ نفر در حملات روسیه کشته شدند
🔴
در ادامه جنگ روسیه و اوکراین، رسانه‌ها از کشته شدن حداقل ۱۵ اوکراینی در حملات به کی‌یف و دیگر نقاط این کشور خبر دادند.
🔴
ولودیمیر زلنسکی گفت که در حمله روسیه به یک نمایشگاه دفاعی در کی‌یف حدود ۱۰۰ نفر هم زخمی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/137388" target="_blank">📅 10:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ایلان ماسک: تا ۱۰ سال دیگر هوش مصنوعی از کنترل انسان خارج می‌شود و کنترل آن دیگر در اختیار بشر نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137387" target="_blank">📅 10:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بلومبرگ: کویت با وجود حملات روزانه ایران، یک همکاری زیرساختی ۱۶ میلیارد دلاری با بلک‌استون، بروکفیلد و KKR در زمینه خطوط لوله صادرات نفت خود به امضا رسانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137386" target="_blank">📅 10:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsraDnT-tM_QuotEhQzwV8D7vR5rvxL5BWrN4UPMCMs3nUII50ndclHRJcHp-XpvJlPcL8ZYq2d-qyLKOWVThKdrQ9uoxeZn8MY-dtiKUe86tqbAI5C7r8o1kp18ZCzartQjykVYf7vDnr4ID6TSHP_GgB5XHv-4NxOP9F3Ldt589mNMG3g3RxY8T1tArp_uNvUvTOfn1eZPKHo64ZEhSjK2-LFvrPlKi4l2UOhyQaP3FYU2H_krsCvG2BUByUL3U5eKR9SyM4EjJL0QtGH5OATG-UFnr-ygxPdumP_vqycrcauTO2SVY3lqecK2j8ymT2fj6Wb9WH-_8Kau8Ff81w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص بورس کانال ۴.۹ میلیون واحد را پس گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/137385" target="_blank">📅 09:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137384">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پایگاه‌های ردیابی پرواز از به هم ریختگی در جریان پروازها و عدم امکان فرود تعدادی از هواپیماها در فرودگاه‌های جنوب عربستان خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/137384" target="_blank">📅 09:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137383">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/137383" target="_blank">📅 09:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137382">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeLCL-jbpHJ2AlDz7D317fo4nAhOJz20rXQPvlHdORoWiuc3D40g799y0LKPE-y7rf5zvkhjDAJjshH9yIXt8iMktU2mM94PJpdqEmmvg7sMFvA3Z95tRyQY0tNiGYPgtXg4pflPnobNEnVSe6skmCNE2YqNsOvCl4WtdKCCcGh39fP2RCOz0z2irbiizN9Z-1CptI_phzX8QxkzNKg3X96oOMUysgIr9SNcEaPaP076qPHP9rEAyO9Xe0Rl0s0mTtCrNAWXqC4aufwwxNAKfWEvrnjy7dNr892YmzkQKwRQEX2bO9gPPPhWpdZLeEHONbq91585mdmkqGzHmhul8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تأسیسات نفتی در جیزان همچنان در آتش می سوزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137382" target="_blank">📅 09:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137381">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گاردین: ایران توانسته توانایی خود در حملات را از طریق پیشرفت فنی در برنامه موشکی و بهره‌گیری از تصاویر ماهواره‌ای، تقویت کند
🔴
شواهد نشان نمی‌دهد که تهران در این مورد از پشتیبانی اطلاعاتی خارجی استفاده کرده باشد
🔴
از برجسته‌ترین روش‌های ایران، استفاده ابتدایی از پهپاد‌ها با هدف خسته کردن پدافند هوایی ، پیش از حمله اصلی است؛ این موضوع شاید نتیجه تبادل تجارب نظامی با روسیه باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137381" target="_blank">📅 09:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137380">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137380" target="_blank">📅 09:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137379">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ:  کارها در ایران فوق‌العاده پیش می‌رود. اخبار جعلی را باور نکنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137379" target="_blank">📅 09:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137378">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRvJbcADHT-KXuxLvPnSu-QPWYObq_qa8q1G4Hsc4r6dI58g-7Sq64-LBIdo7PCtya-thu-WXuIS2Ydwot6h1Eyp-I9ILORkbZln5-UycDULoo01z7uFFZZNIlrRuRIHo9AiXAukQV49-iOOGeX8cpYiV8OTLYCn7jn1-vxSyOsYtYowg8UrRapayDjwTTyC09_ou7yUOYRQvZ3q2CVASE4g0uVMI5G-964aH0bc6IuS9sFA_J2fPQ-6OcZmstE8CIBiUch8wgV2P694pTPUwRLLTF1_vqCUhE8Obd75wF_LfYtSoaoXCFlt6GyPF_lud70iXdj_1APEmys1oSjt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ازدحام بی‌سابقه در جایگاه‌های سوخت عربستان پس از حملات موشکی یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137378" target="_blank">📅 09:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137377">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
دونالد ترامپ: "دوباره این کار را انجام خواهم داد. باید آسان باشد. من واقعاً در نامزد شدن برای ریاست‌جمهوری خیلی خوب شده‌ام. سه بار پیروز شدم. بار دوم انتخابات دستکاری شده بود."
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137377" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137376">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: کایا کالاس(مسئول سیاست خارجی اتحادیه اروپا) از نگرانی‌های حقوق بشری حرف می‌زند، اما در برابر جنایات و حملات علیه ایران سکوت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137376" target="_blank">📅 09:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137373">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a61b348325.mp4?token=lEm3QnWgx8f6qqj7P_VwGgCtipVOYFojLH5KOqTCAJwC5-nCo5sTXL-IjEV5KxTcv5fFN03phOxQjbwBV3ZnsxPf2KHMjzKswcbVOR2XAbxu1_MHBcmcEfcsNvpWxRlyhsLc3Xsb8oD4YYs2PNChUrQQnnlInen-OQNRSsfyllQMFod2Iac3p0uSl_EjQLFWf79glnG7HUtY8I16Ps1oc5bKFTd9Gc6NAHcraQpeEPZh7iZVMASwuZ-VRE58m0rY34IeY0JHYt1sMssynuZc4fa_OjeLTUV-Ej36eweFejUjnl_eY_rPrRWYF4bs1SxOtv1xfsSVGotxclwvRJQXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a61b348325.mp4?token=lEm3QnWgx8f6qqj7P_VwGgCtipVOYFojLH5KOqTCAJwC5-nCo5sTXL-IjEV5KxTcv5fFN03phOxQjbwBV3ZnsxPf2KHMjzKswcbVOR2XAbxu1_MHBcmcEfcsNvpWxRlyhsLc3Xsb8oD4YYs2PNChUrQQnnlInen-OQNRSsfyllQMFod2Iac3p0uSl_EjQLFWf79glnG7HUtY8I16Ps1oc5bKFTd9Gc6NAHcraQpeEPZh7iZVMASwuZ-VRE58m0rY34IeY0JHYt1sMssynuZc4fa_OjeLTUV-Ej36eweFejUjnl_eY_rPrRWYF4bs1SxOtv1xfsSVGotxclwvRJQXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات سنگین شب گذشته پهپادهای اوکراینی به شهر روستوف روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137373" target="_blank">📅 09:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137372">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO_UdhMgmZpzvgKPtpUx-N6dOyt9qsaodgdI4GK31jT0OgBF_5LpBvxZzIS5Z4IeIIHqzGjCZMWrr4Nj5me36Yh9O4M95MGRqKxbZKe1XSJLhb0gOrp_cPHFm5MkpaU4Ir9ygrGKSTUznrSy2t0pHzWl9BjBss_RIHyjI3r9Dzk1WRtJ4n4nNqRmzcXFKSRiZDcS_6gavpRSK9UC-0Mpp4JmyuhpqdpOPLhCdriuRSONfoY2ZC7XI8o2AfOkNDl3u2IgpH5KNBNzaxosAs-7vUS88DuuVGyB7CoLJ-8oQfaNiVbDFtk9a5WQj7SDUZfyE4LqhYE7YKhvrjD8BDRmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت و WTI به ترتیب با ثبت اعداد ۹۶.۷ و ۸۹.۳ دلار بر بشکه وارد تعطیلات آخر هفته میلادی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137372" target="_blank">📅 09:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137371">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxB3oOkuaxXvmyfKGrgRHMh3gSsBq4DiLfYZDT4xIHuyu0we2aNn2jg6rar-VqaJjMvWpG7p4owG8oBKHcnSDC3ueeRnuSYWB2ozU1jfvTUUXo_m0Gtc_68v6DY0GkTHlKP75ubgzSJRrv8-c4XBsFp28JEE_zWyLoZVDpJiIiJCsDDeYzMZa4eLqWtjs8aWdJmhmsyKaN9n-Zz7c3imnkk4AWEFwqQtgoLyOO7PIWajbiCjLJhZGX7wJALUWVwK173J2wQhQGTACZdjLzrGfQ5230ySIKGGYSykMv6ICV1R1k_suqC_iLvkOG75Lbl6Re6uomSCyUzW9_579L5Tlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای تایید می‌کنند که آتش‌سوزی در پالایشگاه نفت واقع در جازان، در نتیجه حملات یمن، رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/137371" target="_blank">📅 08:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137367">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d2b02766.mp4?token=tyzg0503uEn6_5mY-Kj9BP8ezHBRX5kBtYNN9o52sD9O5Fw-jBprx86cwfzIW1CHuurhD-Uds3-qzI7y3i6UEej0Tz83QP2wqz2hW25TJHae56ng8JncnJDHsiSAF9kYCt2XIE2G-6Ba8GE7CNlcWpIz-b42gXjilikKffLdh5ux2lDQVF9N_I9pQlGIwQVKL6_uXQk87Nm9-IpHbpTbT4deFecPuCHS5moCbqKtzAi8JM0V7DABAW2CpFV-Yrn_DlgrgjaFhE8ZMzp_Z9PPukIHCUO3HZG-_wLeDDFD3eP6aVCnZi8KB1dE3--HXQKMzDQWFeuUlSbssRp4DcHkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d2b02766.mp4?token=tyzg0503uEn6_5mY-Kj9BP8ezHBRX5kBtYNN9o52sD9O5Fw-jBprx86cwfzIW1CHuurhD-Uds3-qzI7y3i6UEej0Tz83QP2wqz2hW25TJHae56ng8JncnJDHsiSAF9kYCt2XIE2G-6Ba8GE7CNlcWpIz-b42gXjilikKffLdh5ux2lDQVF9N_I9pQlGIwQVKL6_uXQk87Nm9-IpHbpTbT4deFecPuCHS5moCbqKtzAi8JM0V7DABAW2CpFV-Yrn_DlgrgjaFhE8ZMzp_Z9PPukIHCUO3HZG-_wLeDDFD3eP6aVCnZi8KB1dE3--HXQKMzDQWFeuUlSbssRp4DcHkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله یمن به تاسیسات نفتی عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/137367" target="_blank">📅 08:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137366">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTgGkRDBuLyxetuq5laD1XaEL4bTFh7eCI1cB1_0POez7meckMqzeOe_gZg9c6iDNgHxG755DPVfRG5hyuBkjjKaA1mfrHi2e5H5Zqlb1piQSgnAHkwB37Embt7sPMawC7BLqq6xItzt_4LLeSH_hoDDZ1542Z7aCGfhyF883AGQzVVyWiDycV0atZD8UwXo3qW25BV-VzQVTz2qFeFvT6m9pUVQXqMx0c5-asqLRXZaIJpeq7gRZNOeY9Exu-8q87-1Fh4s5Hi_DMBWH0lzCFUqcVCkJy6vmdj_Y4dE7RoD1feooOYJ4syuRWdlLNKBYpdI_MdpEqwS_-VU_4Tf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا معتقدن مجتبی خامنه‌ای، رهبر جدید ایران، نسبت به علی خامنه‌ای تمایل بیشتری به دنبال کردن برنامه ساخت سلاح هسته‌ای داره.
🔴
با این حال، مقام‌های آمریکایی میگن ایران هنوز برنامه هسته‌ایش رو از سر نگرفته، اما به گفته اون‌ها، رهبری جدید ظاهراً آمادگی و تمایل بیشتری برای توسعه توانمندی‌های پیشرفته هسته‌ای نشون میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/137366" target="_blank">📅 03:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137365">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66640af45a.mp4?token=kSgNNsm87byclsghNccbgH3T5ZkqF7EIbwb5_H4ICVJ2pvJ-OdcpTeH7z0Ysme6jZ24ocxxke2CY_HIFtaSfLviNF6Ygg0sHTQmWCyEmbBdWxfoUkgRKj0GCYjwuTyMlMS5YEhpnTWzSCesUAKed8J65Qmkd7BdpxjfHCLmt0gGKxDA5xRQjv06cf3D4G4bRVdTrOhb6ehCSYRgIiIe5f6uFRxQZj2UkmYMQ1V4vg-AViYLD-ar5la6LtVXWFGza9dlf5d4BWw-Pb1fxZrRQUT0d69kLWFZmxlPlS4tqYTLEQUzurBaZSkYM17cD3wptFKUJJ9RiuO--zQ-zq7-yqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66640af45a.mp4?token=kSgNNsm87byclsghNccbgH3T5ZkqF7EIbwb5_H4ICVJ2pvJ-OdcpTeH7z0Ysme6jZ24ocxxke2CY_HIFtaSfLviNF6Ygg0sHTQmWCyEmbBdWxfoUkgRKj0GCYjwuTyMlMS5YEhpnTWzSCesUAKed8J65Qmkd7BdpxjfHCLmt0gGKxDA5xRQjv06cf3D4G4bRVdTrOhb6ehCSYRgIiIe5f6uFRxQZj2UkmYMQ1V4vg-AViYLD-ar5la6LtVXWFGza9dlf5d4BWw-Pb1fxZrRQUT0d69kLWFZmxlPlS4tqYTLEQUzurBaZSkYM17cD3wptFKUJJ9RiuO--zQ-zq7-yqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لشکرکشی شبانه در عراق
‼️
🔴
گویا ساعاتی قبل نیروهای وابسته به جمهوری اسلامی به سمت پایگاه آمریکا پهپاد شلیک کردن و ارتش عراق یه ستون زرهی سنگین را راهی پایگاه‌های حشدالشعبی کرده تا پهپادها رو جمع کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137365" target="_blank">📅 02:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137364">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
فعالیت شدید جنگنده ها در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/alonews/137364" target="_blank">📅 02:42 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
