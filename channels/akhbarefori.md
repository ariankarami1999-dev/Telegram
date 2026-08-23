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
<img src="https://cdn4.telesco.pe/file/uOjE-jBvy0SBNKaCgzMCLwWI1S5i3llXovSkYAoRpq2UYvKJ4CzDBbLhkxxB9la7gjyjE7eO-1Vzma93lNGjiRau2JGiTg5b9O2scYlRu9029JH2D7QRLZzrRL8qH5arV6LjHRXvZhDhNnpoAsoGSVUdxCpDX0BKU2LkOIZOYi1gfYBJAyLXQi69Is-oluJJ2Vo4y8kmgb9OH09_Jo2ENL1iT07JjYwW3m6ZfdwaIcno2B-oFOobsXReM9FyDg-IOBBDldmGG6iavVs3EPwbc0TPsC-kf07dM9ZnRCILma0ybP0oaI_pQnHl4jDK0AYy8qp3KaF7W7W2NEsCqUGRMw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 20:18:15</div>
<hr>

<div class="tg-post" id="msg-683724">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت: جهاد اقتصادی باید بازتعریف شود
عباس مقتدایی،نایب رئیس اول کمیسیون امنیت ملی و سیاست خارجی مجلس در
#گفتگو
با خبرفوری:
🔹
قیام اقتصادی ملت برای حراست از فضای کسب‌وکار، تولید و عرصه خلق ثروت، یک ضرورت عینی است. همچنین می‌بایست مقامات دولتی، نهادهای قانون‌گذاری و همه بخش‌هایی که می‌توانند، در این زمینه ایفای نقش کنند.
🔹
در این مقطع زمانی، جهاد اقتصادی باید بازتعریف شود تا معیشت خانوارها را دگرگون سازد و  از مرحله بیان به مرحله عملیات برسد و زمان‌بندی آن محقق شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/akhbarefori/683724" target="_blank">📅 20:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683723">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW7wm1hmhZyT33OJrtVNq5FUncOc_WvvFNrvvQ7nDhlYi8DlYly7wA-ai5ZbhjohKDACZ8FrvY1dM_5734gBL8FwNA4RXYi_PxYsh6KmwAvt3B-xE8UiGqdbKYsf9zRQ3zrdWOcmkgLLJ945tmL3K-vR7YE3SXHIURyoW2JUl3XBJpZUCRalDMzYUa3S0cbk-kM1gd88aSCfJS-_VAwNgfkauHXWXM-oiXdEH4Ts_tMKskvAdktK3Mr56ArWQImboxCl4R-xG4stxZSomxNxrgHYyaPSKvT3btufeL_SFCJqV5dCbgXZ_Tmw0KEuduwdXY4qkd4E7xhzk1rUBfkqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جلسه اضطراری نتانیاهو برای مقابله با بادبادک‌های غزه
🔹
دفتر نخست‌وزیر رژیم صهیونیستی از برگزاری نشست فوری با حضور نتانیاهو و وزیر جنگ این رژیم برای بررسی تهدیدهای ناشی از پرتاب بادبادک‌ها و بالون‌های آتش‌زا از نوار غزه خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/683723" target="_blank">📅 20:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683722">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">02 Ane Manaee (1403-07-19) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/683722" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه دوم
حجت‌الاسلام امینی‌خواه:
🔹
روانشناسی باور؛ تقابل عمیق بین مؤمن و کافر [01:45]
🔹
دسیسه‌های شیطانی: شانتاژ و تخریب مسیر ایمان [02:55]
🔹
قرآن، کتاب زندگی یا کتاب مراسم؟ [08:00]
🔹
تماشاچیان عاشورا؛ بازیگرانی خاموش [19:00]
🔹
حضرت حمزه و درس‌های بزرگی از غیرت و تعصبِ به‌جا [25:28]
🔹
وقتی پیامبر (صل‌الله‌علیه‌وآله) کوتاه آمد ولی امیرالمؤمنین(علیه‌السلام) کوتاه نیامد... [26:45]
🔹
تکرار تاریخ؛ از سکوت مرگبار جامعه تا فریاد‌های رسای حضرت زهرا (سلام‌الله‌علیها) [36:50]
🔹
۱۲ قرن تنهایی و مراقبت از دشمن؛ روضه‌ای که با زندگی سید حسن نصرالله دوباره خوانده شد [44:56]
🔹
چقدر باید ظلم کنند تا بیدار شویم؟ [51:50]
🔹
پاسخی از جنس شعر، کرامت رضوی در کلام صائب تبریزی  [55:20]
🔹
رهبر معظم انقلاب؛ دلی که با یقین می‌تپد [59:58]
🔹
توبه جناب حر؛ امید در تاریک‌ترین لحظات [01:017:00]
🔹
معجزه‌ای از کربلا؛ بدن سالم جناب حر پس از قرن‌ها [01:23:43]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/683722" target="_blank">📅 20:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683721">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c153e7d278.mp4?token=v3vpsmKog4KHtv93eTDkQ78WAzZVOSX0JYB2A2DSLRu-szAHZ4TdcaVrN5ZlFS3hGzj9e-3SwJSuCTcSJ_Nc6S6McUSMos7ZLP0lb-I_4EsSRYqmvaQHgGNOiqf4db62D2uwpCfWaKeKUASg9i9Tvwx0Spw0SD1pdk96TH0HSx2LCZa7HwtACYnhWgiVRA8PK2cBRgO2EuTbOgWoNacHNKG2JoFBY5zBYjIjcfiN-HYA7mZ2UTFISPoS8bj149LcHgY9L1IjNkWZDatLSGS5207ICyO8UHrjRRMVdtleSoQLAdWQ_c-w7uNFYPfjoQ5qlT4SlJN9oatE01lv-K77IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c153e7d278.mp4?token=v3vpsmKog4KHtv93eTDkQ78WAzZVOSX0JYB2A2DSLRu-szAHZ4TdcaVrN5ZlFS3hGzj9e-3SwJSuCTcSJ_Nc6S6McUSMos7ZLP0lb-I_4EsSRYqmvaQHgGNOiqf4db62D2uwpCfWaKeKUASg9i9Tvwx0Spw0SD1pdk96TH0HSx2LCZa7HwtACYnhWgiVRA8PK2cBRgO2EuTbOgWoNacHNKG2JoFBY5zBYjIjcfiN-HYA7mZ2UTFISPoS8bj149LcHgY9L1IjNkWZDatLSGS5207ICyO8UHrjRRMVdtleSoQLAdWQ_c-w7uNFYPfjoQ5qlT4SlJN9oatE01lv-K77IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با چند ترفند ساده، اتوی بخارت‌ رو مثل روز اول تمیز و آماده استفاده نگه دار! #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/683721" target="_blank">📅 20:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683720">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: ۴ روز بعد از آغاز جنگ، جلسۀ دولت تشکیل شد، آقای عراقچی در جلسه گفت ممکن است دشمن اینجا را بزند، رئیس‌جهور گفت به درک که می‌زند. من جلسات را تعطیل کنم از ترس اینکه او می‌زند؟ خُب بزند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/683720" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683719">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2781b49bbf.mp4?token=MtyhS_tjR2ED2Y_ee9Zy6tfZ5ct7S_1msayDeTMm08YQwmt3F9ktpStmStCUmzClYm5Et36gFoOSuBkPQZFhJD4RmRJVPXU-KW_hojR3lvV-xkiuF_J7mKgn9vo1w3nTA-zvS5QFqstJLwl1FZm_45i2Pwcna3BCGq7-ZR98wlOiQGg_Np1ZKYBKHeldEzgfdkO484sbKJ_F8_6Vzw_4a_8dwMVK1z2PMfywy9GnEG7O7mZTjB-mL0FW4SRnSXrmp74k5ZT8zsBiDOsxQObyRYCC0ZM-q2hxK2UkPrCGiX3bZDb68tvEAncu09BLg9dlNwGmF2L695uXtepdVqS0Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2781b49bbf.mp4?token=MtyhS_tjR2ED2Y_ee9Zy6tfZ5ct7S_1msayDeTMm08YQwmt3F9ktpStmStCUmzClYm5Et36gFoOSuBkPQZFhJD4RmRJVPXU-KW_hojR3lvV-xkiuF_J7mKgn9vo1w3nTA-zvS5QFqstJLwl1FZm_45i2Pwcna3BCGq7-ZR98wlOiQGg_Np1ZKYBKHeldEzgfdkO484sbKJ_F8_6Vzw_4a_8dwMVK1z2PMfywy9GnEG7O7mZTjB-mL0FW4SRnSXrmp74k5ZT8zsBiDOsxQObyRYCC0ZM-q2hxK2UkPrCGiX3bZDb68tvEAncu09BLg9dlNwGmF2L695uXtepdVqS0Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقاب اصفهانی: بخشی از مصرف بالای بنزین به خاطر کیفیت خودرو است  رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی:
🔹
با اینکه کیفیت برخی تجهیزات پایین است اما تغییر رفتار، زودتر از اصلاح تجهیزات و اقدامات دیگر قابل انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/683719" target="_blank">📅 19:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683718">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08c8d12a6.mp4?token=MclD0lcZNoLJ-YDHfTGoL91OOS3Mb_UVRQmTynUPeNuDi9mLxXRGDarJg7ffiJuoBhM4m7aPpWNF2WbVIC3nwckui6LUg5VGisInzXue6ZPuI3JjzdgqMVC4e5a14oqVMUI0PDzHPMvMTgCXs9-DQSufXZnSefD4FIDTWHFAVhY5fY_emeCCjMVJTIYa2GKIHjErg6bnzOW1Cv8Npo4ctWVZmwoH4LA5gpoMBkxThokfy7L9wg4rpoQiBiB3W-iW5ZeGREDh1E75UbiAun55ZTnmDuaBiwEpSnYjDKF8Q2pEfm5ZJlJp4JVIrLqENalJKRPWcc-HHR15YR9to7NLlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08c8d12a6.mp4?token=MclD0lcZNoLJ-YDHfTGoL91OOS3Mb_UVRQmTynUPeNuDi9mLxXRGDarJg7ffiJuoBhM4m7aPpWNF2WbVIC3nwckui6LUg5VGisInzXue6ZPuI3JjzdgqMVC4e5a14oqVMUI0PDzHPMvMTgCXs9-DQSufXZnSefD4FIDTWHFAVhY5fY_emeCCjMVJTIYa2GKIHjErg6bnzOW1Cv8Npo4ctWVZmwoH4LA5gpoMBkxThokfy7L9wg4rpoQiBiB3W-iW5ZeGREDh1E75UbiAun55ZTnmDuaBiwEpSnYjDKF8Q2pEfm5ZJlJp4JVIrLqENalJKRPWcc-HHR15YR9to7NLlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: در ایام جنگ به رئیس‌جمهور گفتم حاضرید باهم برویم پای لانچر؟ او گفت برویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/akhbarefori/683718" target="_blank">📅 19:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683717">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7cb82fdaa.mp4?token=E5Syvsrgu0fOBg3hM5x5VdmuUCdZFJrC_t-JkkBwMlsp18Xp92DtK3ruk2lsV0jf0rngy3QUIzfzxva84KSCb7C7lZlhVEEZQw_9MFy920zffi4JAS14c_Bk6kTNcIX_hQOK0pIUOvLEVgXIXXerJ5KFjsSYIBKJVab3RRPUCupIACxyeZ6-K5H1jQ3sm8SAprjUxHM4o7jtCcz3ApqCNfR4UbtgHsC9Q08yZUyNeL-M1Z8AZoKp7w66xMFLjgRv8wBWueVw8zKP7gKdXeL6E4ifUn5gFGk1L62ca021vxAEiPpZbk3NbTiO_RVuy-bQxEHQNtbSejffeFD9ZdLLVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7cb82fdaa.mp4?token=E5Syvsrgu0fOBg3hM5x5VdmuUCdZFJrC_t-JkkBwMlsp18Xp92DtK3ruk2lsV0jf0rngy3QUIzfzxva84KSCb7C7lZlhVEEZQw_9MFy920zffi4JAS14c_Bk6kTNcIX_hQOK0pIUOvLEVgXIXXerJ5KFjsSYIBKJVab3RRPUCupIACxyeZ6-K5H1jQ3sm8SAprjUxHM4o7jtCcz3ApqCNfR4UbtgHsC9Q08yZUyNeL-M1Z8AZoKp7w66xMFLjgRv8wBWueVw8zKP7gKdXeL6E4ifUn5gFGk1L62ca021vxAEiPpZbk3NbTiO_RVuy-bQxEHQNtbSejffeFD9ZdLLVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: به رئیس‌جمهور گفتم باید کارهایی کنیم که در کوتاه‌مدت فحش بخوریم اما در بلندمدت از ما تشکر شود
🔹
آقای پزشکیان به من گفتند حتما این‌کار را بکن زیرا ما باید مسائل را حل کنیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/akhbarefori/683717" target="_blank">📅 19:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683716">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96dbefcd54.mp4?token=EyzWCJmvuZLL5BrDuG6_BZOgeiOdJtvg7Z7KQkT44-ius0ctibhFYsGLnS8qXb6nc1VzhTGQOu9a83_LxJbNtWKpn4MwLHCj2JfJvJhS2HuRfU-cTuDf5YbtFf2ZiHyI49fYRkP9BpF7otlE90_exvm2P0xPkEI2FYv0HiJJ7n6UiqyzgQc1YAFH2vV2gjYAzvAP86vDKr8234Qz_K7hQApFJqWABeTfXUEBEX_xUFw0f8u7LjLtxtNklwaxYSkZ5jeyIlpwniTobce287iHjJOM7YfiBAq-qtcrX0CtApK9VkkP30bClqs9rAbybRGHB1dg73S1UiMYW5T1ZlQZRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96dbefcd54.mp4?token=EyzWCJmvuZLL5BrDuG6_BZOgeiOdJtvg7Z7KQkT44-ius0ctibhFYsGLnS8qXb6nc1VzhTGQOu9a83_LxJbNtWKpn4MwLHCj2JfJvJhS2HuRfU-cTuDf5YbtFf2ZiHyI49fYRkP9BpF7otlE90_exvm2P0xPkEI2FYv0HiJJ7n6UiqyzgQc1YAFH2vV2gjYAzvAP86vDKr8234Qz_K7hQApFJqWABeTfXUEBEX_xUFw0f8u7LjLtxtNklwaxYSkZ5jeyIlpwniTobce287iHjJOM7YfiBAq-qtcrX0CtApK9VkkP30bClqs9rAbybRGHB1dg73S1UiMYW5T1ZlQZRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: به رئیس‌جمهور گفتم باید کارهایی کنیم که در کوتاه‌مدت فحش بخوریم اما در بلندمدت از ما تشکر شود
🔹
آقای پزشکیان به من گفتند حتما این‌کار را بکن زیرا ما باید مسائل را حل کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/683716" target="_blank">📅 19:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683715">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534e133ebb.mp4?token=GsQbQiH1G1GQp04bL2Rykj_skGCwXf50GnFKF3see7a4KfNfPPt3uklNuB-09J4dLWDx7HZOxrw25SYNo9nwmLuBCMqDb8pKt7zOYpUJTZvDuonWUZEzCWr7YZS7bXOgdJkWi9gu5_ruS64REpn_HAL0C7B8O3qPPfvQksTWEUezA6e2u03ECARmCS4H7pIRupyghp-ZdTe-d3_SJHEAPX8dOwR3MedNiLdSSZmJWeB2QN7rpuuGUu5bpIArnD1X0mB_HIYCJbAEzLfRxAv3rJk1ulTJzZA_AauW5Qy2fgJ41C2aDyv8QltXgWyI5xfDmpaGrR0cxUw_UoiuJ9Pv6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534e133ebb.mp4?token=GsQbQiH1G1GQp04bL2Rykj_skGCwXf50GnFKF3see7a4KfNfPPt3uklNuB-09J4dLWDx7HZOxrw25SYNo9nwmLuBCMqDb8pKt7zOYpUJTZvDuonWUZEzCWr7YZS7bXOgdJkWi9gu5_ruS64REpn_HAL0C7B8O3qPPfvQksTWEUezA6e2u03ECARmCS4H7pIRupyghp-ZdTe-d3_SJHEAPX8dOwR3MedNiLdSSZmJWeB2QN7rpuuGUu5bpIArnD1X0mB_HIYCJbAEzLfRxAv3rJk1ulTJzZA_AauW5Qy2fgJ41C2aDyv8QltXgWyI5xfDmpaGrR0cxUw_UoiuJ9Pv6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد ضدصهیونیستی در آرژانتین، معترضان پایان «نسل‌کشی» رژیم اشغالگر در غزه را خواستار شدند
🔹
صدها تن از شهروندان آرژانتینی با برگزاری راهپیمایی گسترده، سیاست‌های جنایتکارانه رژیم صهیونیستی در نوار غزه را به‌شدت محکوم کرده و توقف فوری ماشین کشتار این رژیم را فریاد زدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/683715" target="_blank">📅 19:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683714">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پزشکیان: صرفه‌جویی مصرف بنزین باید از دولتی‌ها شروع شود
رئیس‌جمهور در جلسه هیئت دولت:
🔹
برنامه‌ریزی کنید که چگونه می‌شود ماشین‌های دولتی و مصرف دستگاه‌های دولتی را کاهش داد و میزان ترددهای ماشین‌ها را پایین آورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/683714" target="_blank">📅 19:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683713">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12fbb21d0.mp4?token=LN90fthTBiSW3gbcrLr2cXD4mBskgR6qdP-kYtD7W3kQVBH7BAw5OMmhnEF9vOTeJRdxBLVK4CyEaHVaECUSRYnEljGK1jJi21o_HKnzSe1uobH1HPgorPHXoNx9QlUPZ2tuqeDwAda9J9U3ZzJGQUFWfb1LW4z0S5VQ7yyjfgwoRWhF8JXviTQ1UgCpSerb5YmeEA2zx7YqJskNVQ2jKjmq1j0nsYSw6Cd2i7cOE0-dyhxbUBtEZdJ5jG3rZE7QJrrssUPV9M8nyO4J78UaVRvMX0VRp72FVV8K3ruD0DxEBQm8dxr88jmG7rvwrK4l6TpUCV-y0pvtCo3qthYjnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12fbb21d0.mp4?token=LN90fthTBiSW3gbcrLr2cXD4mBskgR6qdP-kYtD7W3kQVBH7BAw5OMmhnEF9vOTeJRdxBLVK4CyEaHVaECUSRYnEljGK1jJi21o_HKnzSe1uobH1HPgorPHXoNx9QlUPZ2tuqeDwAda9J9U3ZzJGQUFWfb1LW4z0S5VQ7yyjfgwoRWhF8JXviTQ1UgCpSerb5YmeEA2zx7YqJskNVQ2jKjmq1j0nsYSw6Cd2i7cOE0-dyhxbUBtEZdJ5jG3rZE7QJrrssUPV9M8nyO4J78UaVRvMX0VRp72FVV8K3ruD0DxEBQm8dxr88jmG7rvwrK4l6TpUCV-y0pvtCo3qthYjnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به سپاهان توسط یاسر آسانی   استقلال ۱ _ ۰ سپاهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/683713" target="_blank">📅 19:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683712">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رسانه صهیونیستی: همه جای جهان اسرائیلی‌ها را کودک‌کش می‌خوانند
🔹
کانال ۱۴ تلویزیون اسرائیل اعتراف کرد، حتی در دور افتاده ترین نقاط هم صهیونیست‌ها را کودک‌کش لقب می دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/683712" target="_blank">📅 19:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683711">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhGaOTgg72hVrf6USvnVQR2JdrFr4b5QxQMcYAGdOleeVExtpfDBx2ey7ZgINg_WnFYRoxInlbSq30j3Ap5qVWuVdmYY0kcP-JtqxmMj08QT-RaNHh2mrVJh49G1IMA6LHeztAx3179Q56VGAP-FQZsFGhRC9-XjhYnunA7E-6LBY2v3yRwo0lEveSP6V70QyDbATbjrk-vPJ1wwFRzxeqo4aWD4xIkUtd63TnYuGuMmXOgeXvcoDpZmZhxZBG_cofrUKaNmcqBqfOZX2EoyN9cGA3yuWCh0Xi2gL08yzPqOX-Msl6nZKBmJYRpfiAuyzkAS0hjRjmaGqHJu_GAFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گسترش فرصت‌های سرمایه‌گذاری در وال‌گلد؛ نقره به میدان آمد!
💎
تنوع، کلید موفقیت در بازارهای مالی است. پلتفرم «وال‌گلد» در گام جدید خود این امکان را فراهم کرده است تا کاربران بتوانند در کنار طلا، روی «نقره» هم سرمایه‌گذاری کنند.
🔸
روند یک سال اخیر نشان می‌دهد نقره بازدهی‌های چشمگیری در بازار سرمایه داشته است.
🔸
با این امکان جدید، سرمایه‌گذاران می‌توانند با ترکیب طلا و نقره، یک سبد مطمئن‌تر، کلاسیک و پربازده بسازند.
ورود به بازار جذاب نقره
ورود به بازار جذاب نقره</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/683711" target="_blank">📅 19:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683709">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96b95162d0.mp4?token=PwvRP6hIMyjPXbrFd8IcwyMhI58MLgbPrD0KTDUORDBrKz1TwxUQYB8EmxYTuQXSZoHMCI05aTbwZ0KO5kPUanVWM6T1XDszhly0wkyWBlVhlAgO8SwtoYniveKlvCQnXvb7Pn5TkpQXj8P64FfSxfYhcnzAitugi9N6_zh8yWe85Ag7vduQg_sbNERG0rMo1ui_cG-hWNA_lsSdDCdrRjs5LPfuKiLtVjj66jMtjbCvXnmKaVUS8wcaWk3AX2IN6lk7kJBr4NdC2PtpCPsPKl6GnCuw22t_CndD22xvbUac5OBECQxaEjjKvBkcSaSLEpGHddL-QkkMGDSqKuw_WUX-h6osgBjor7ZkysoXBwtvQZ8ezG2xg76bdmSv-Yyda9jxUtxYAxUD8bw_MeQW8LRF2c69FZOSXGOqJffh94msIb-nMrgDdfvnoFtReYCTKFy7pj_mOxHs3nQ80RQaVDHhJ00fqGlbBgVsoGLG50-k0QoWDBuLf3ORFJtGAFSYqdSkKd4MYGm_8sqovTatKHhMThLNmAxmtDJmomD27jW_RoRn2jZNk9f1Pr86qzcy1R-kUg0uPZoiOexxP2N0G9gavIzTvDybsM6lhJuAIlvr0l7kP3p1tmvnmJSFAeRLN_8xZDaJiugsrBUn8w2HxO2FOQFwRyBBsn_rHYccRuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96b95162d0.mp4?token=PwvRP6hIMyjPXbrFd8IcwyMhI58MLgbPrD0KTDUORDBrKz1TwxUQYB8EmxYTuQXSZoHMCI05aTbwZ0KO5kPUanVWM6T1XDszhly0wkyWBlVhlAgO8SwtoYniveKlvCQnXvb7Pn5TkpQXj8P64FfSxfYhcnzAitugi9N6_zh8yWe85Ag7vduQg_sbNERG0rMo1ui_cG-hWNA_lsSdDCdrRjs5LPfuKiLtVjj66jMtjbCvXnmKaVUS8wcaWk3AX2IN6lk7kJBr4NdC2PtpCPsPKl6GnCuw22t_CndD22xvbUac5OBECQxaEjjKvBkcSaSLEpGHddL-QkkMGDSqKuw_WUX-h6osgBjor7ZkysoXBwtvQZ8ezG2xg76bdmSv-Yyda9jxUtxYAxUD8bw_MeQW8LRF2c69FZOSXGOqJffh94msIb-nMrgDdfvnoFtReYCTKFy7pj_mOxHs3nQ80RQaVDHhJ00fqGlbBgVsoGLG50-k0QoWDBuLf3ORFJtGAFSYqdSkKd4MYGm_8sqovTatKHhMThLNmAxmtDJmomD27jW_RoRn2jZNk9f1Pr86qzcy1R-kUg0uPZoiOexxP2N0G9gavIzTvDybsM6lhJuAIlvr0l7kP3p1tmvnmJSFAeRLN_8xZDaJiugsrBUn8w2HxO2FOQFwRyBBsn_rHYccRuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به سپاهان توسط یاسر آسانی
استقلال ۱ _ ۰ سپاهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/683709" target="_blank">📅 19:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683708">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سرپرست وزارت دفاع: یافته‌های فراوان اطلاعاتی و فناورانه‌ای از دشمن به دست آوردیم
🔹
کمیسیون امور داخلی مجلس: اعتبار گذرنامه افراد بالای ۱۵ سال ۱۰ ساله و زیر ۱۵ سال ۷ ساله می‌شود.
🔹
وزارت دفاع عراق: ۹ مهر تاریخ نهایی خروج نیروهای بیگانه از عراق است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/683708" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683707">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
خبرهایی درباره انفجار در حلب سوریه
🔹
منابع خبری از انفجار در حلب خبر دادند، ولی هنوز جزئیاتی درباره علت انفجار منتشر نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/683707" target="_blank">📅 19:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683706">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc966282fc.mp4?token=vCJ0FoRjEyDZZXMG9V22gNIpPMgsT0MJ0xSec4jo4tm7zauu5IO-Nhi22jyXx25LBuw6Ebm9cXv0NLNNyt1a_Q6hXruf0WlSw47ZLvNJ0Ds22U5pLijOyTaQw9dU0jOskfRT26kY3HooEiy7thd_CZdzfwb9c7ozjugF-jzYBU1Cphx4ICRHicH4SQ27TDFvSjHBMliwu54TQEVNe1KT9HnRt3ijETv91si24SVUZ203At7v7Q5JaG0F0KAcsb4VP61IawIvqw9v9pS_Vo60jaA-8J724ly-w5A6nOgqwlMz_Ue2dhyAkfGYKqSaHjiH6EmrGyJkcNI_W6lUHigWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc966282fc.mp4?token=vCJ0FoRjEyDZZXMG9V22gNIpPMgsT0MJ0xSec4jo4tm7zauu5IO-Nhi22jyXx25LBuw6Ebm9cXv0NLNNyt1a_Q6hXruf0WlSw47ZLvNJ0Ds22U5pLijOyTaQw9dU0jOskfRT26kY3HooEiy7thd_CZdzfwb9c7ozjugF-jzYBU1Cphx4ICRHicH4SQ27TDFvSjHBMliwu54TQEVNe1KT9HnRt3ijETv91si24SVUZ203At7v7Q5JaG0F0KAcsb4VP61IawIvqw9v9pS_Vo60jaA-8J724ly-w5A6nOgqwlMz_Ue2dhyAkfGYKqSaHjiH6EmrGyJkcNI_W6lUHigWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش زیبا روی خورشید
🔹
این ساختار حلقه‌ای تاج خورشیدی، یک مسیر مغناطیسی است که پلاسمای فوق‌داغ پس از یک شراره خورشیدی از طریق آن به سطح خورشید بازمی‌گردد.
🔹
ثبت این ساختارهای ظریف و رشته‌ای در هیدروژن آلفا با این میزان پایداری بسیار نادر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/683706" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683705">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a398e28d40.mp4?token=AaD_fulNOvey57FaryfS4HjUMygBd20zNidkAtkg4r79SIWjYoUrqA7FWcX7CpSAth6yOYNokjjXzxsDmX3JIaimsUTIzbGoYuytgGWk3aXtH9MsmW18dcn-BUzmLw66Y9jkOqsk-KascJbWDVWzQAjJ0m6red9-3FykxZzeBwGNh7qx8WeZRsNfaXC-Q1YR0gXBJ2YOCI67pJFJ1lB9jgwVZPtxYh_GSOobIQM3Mpo_eBzAFTVmlgs_M5O0bhphsPpe-M1ZT_9WiPRNwNKYuqaTxOXxYvX5fFTrHLFGf_oD1yGbe0FNu9HMptDZCyPPpImqBF8Ez9ZEKWlk_n8OVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a398e28d40.mp4?token=AaD_fulNOvey57FaryfS4HjUMygBd20zNidkAtkg4r79SIWjYoUrqA7FWcX7CpSAth6yOYNokjjXzxsDmX3JIaimsUTIzbGoYuytgGWk3aXtH9MsmW18dcn-BUzmLw66Y9jkOqsk-KascJbWDVWzQAjJ0m6red9-3FykxZzeBwGNh7qx8WeZRsNfaXC-Q1YR0gXBJ2YOCI67pJFJ1lB9jgwVZPtxYh_GSOobIQM3Mpo_eBzAFTVmlgs_M5O0bhphsPpe-M1ZT_9WiPRNwNKYuqaTxOXxYvX5fFTrHLFGf_oD1yGbe0FNu9HMptDZCyPPpImqBF8Ez9ZEKWlk_n8OVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان: کسانی که در مسئله علی‌الاصول دل رهبر انقلاب را خون کردند امروز همچنان از بخش‌هایی از توافقنامه دفاع می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/683705" target="_blank">📅 19:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683704">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس مرکز امور زنان و خانواده وزارت کشور: محققان می‌گویند غلظت ماری‌جوانای مصرفی در ایران بالاتر از جاهای دیگر است
پروین داد اندیش، مشاور وزیر و رییس مرکز امور زنان و خانواده وزارت کشور در
#گفتگو
با خبرفوری:
🔹
درباره زنان بی‌خانمان نگاه سلیقه‌ای است و می‌خواهند مسئله را پاک کنند، اما تاجایی که می‌دانم اگر به آقای پزشکیان مهلت بدهند، رویکردشان این است که با مسائل کارشناسانه برخورد می‌کنند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/akhbarefori/683704" target="_blank">📅 19:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683703">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
قشقایی: ماده ۳ طرح اقدام راهبردی تأمین امنیت و پیشرفت تنگه هرمز به تصویب رسید  سخنگوی کمیسیون امنیت ملی:
🔹
بر اساس این ماده، در قبال خدماتی از جمله خدمات دریانوردی، محیط‌زیستی، سوخت‌رسانی در شرایط خاص، بیمه‌ای، ایمنی و سایر خدماتی که ارائه می‌دهیم، هزینه…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/683703" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683701">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a928736d65.mp4?token=QnZiBW4hsZduHY_lTnCFIUYJqdLrXK6cdczU7p_7aAer66lscugsMbtBBu3shimUGXdhIPBtzMFnEYaJL0TzZpssiniU6Lc2zC0WZ3rYCuBpCF13o7c7Plk3y7jk3J7Yp3isMIHpL5QELdZmA4EI3AwZQkzEAaoHiHOms1Ow-2ld0uUnjsvy5ZjX4e2vftwIS2e7uhYe00adCXVOeEZ5sFSlx8mMj_MFzNEO0GVjY9XqVe8APo0UPPP2A1PL5C1q469i49ZnNAmvic3mXOoOHhYZbHXOdmX4Ftl6F_pWdJM_dN3oth70hRvq-A6zt4AbydcwR2wvPKpDafcha_kf1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a928736d65.mp4?token=QnZiBW4hsZduHY_lTnCFIUYJqdLrXK6cdczU7p_7aAer66lscugsMbtBBu3shimUGXdhIPBtzMFnEYaJL0TzZpssiniU6Lc2zC0WZ3rYCuBpCF13o7c7Plk3y7jk3J7Yp3isMIHpL5QELdZmA4EI3AwZQkzEAaoHiHOms1Ow-2ld0uUnjsvy5ZjX4e2vftwIS2e7uhYe00adCXVOeEZ5sFSlx8mMj_MFzNEO0GVjY9XqVe8APo0UPPP2A1PL5C1q469i49ZnNAmvic3mXOoOHhYZbHXOdmX4Ftl6F_pWdJM_dN3oth70hRvq-A6zt4AbydcwR2wvPKpDafcha_kf1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات انسان‌نمای چینی رکورد پرش ارتفاع را شکست
🔹
ربات انسان‌نمای شرکت X-Humanoid در دومین دوره بازی‌های جهانی ربات‌های انسان‌نما در پکن، با پرش ۲.۸۸ متری رکورد این مسابقات و رکورد ۲.۴۵ متری پرش ارتفاع ایستاده انسان‌ها را که خاویر سوتومایور در سال ۱۹۹۳ ثبت کرده بود، شکست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/683701" target="_blank">📅 18:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683700">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سردار ابن‌الرضا: برخی بمب‌ها اختصاصاً برای استفاده علیه ایران ساخته شده بود
سرپرست وزارت دفاع:
🔹
دشمن در «جنگ تحمیلی سوم» با استفاده از ابزارهای سایبری، نظامی، نیروهای نیابتی و عناصر ضدانقلاب وارد میدان شد و برخی سلاح‌ها و بمب‌ها برای نخستین بار و به‌صورت اختصاصی علیه ایران به‌کار گرفته شدند.
🔹
وی این جنگ را نخستین جنگ موشکی و پهپادی گسترده، دارای بالاترین حجم عملیات هوایی و یکی از پیچیده‌ترین عملیات‌های نامتقارن دانست که در نهایت با شکست دشمن همراه شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/683700" target="_blank">📅 18:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683699">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af592104d.mp4?token=Z-M-CunCKyS_I9pwrju3hd71R77PJDBdGa-D1ZDWbEuR_DVQqwEua8omqGa_Q9a5MVPzT02n3O1nFShkRwXIENDAaLvddgxjjFTcNGuf5br879rGFjNdCZifYcHTU5tBFXdOwCjkFAVzZbxu9t3jbQEsbb0g41JNGt6L74G-p-r3VIe3LLKjfY9WBoj5UXdhcF0bev6u5E4lBTQuXBS4Q-NNElNtMR-Das9rbyQ0hIYzQD2TvtR5JE-3RI_u4bK_1KYgXhZBODJyI1OFXV9pPzWYo1sVHmswjGbCy8jZCNz0dDgjgCPL5QXfInUgpe9mhB-3AvVYELqOKegKjVI1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af592104d.mp4?token=Z-M-CunCKyS_I9pwrju3hd71R77PJDBdGa-D1ZDWbEuR_DVQqwEua8omqGa_Q9a5MVPzT02n3O1nFShkRwXIENDAaLvddgxjjFTcNGuf5br879rGFjNdCZifYcHTU5tBFXdOwCjkFAVzZbxu9t3jbQEsbb0g41JNGt6L74G-p-r3VIe3LLKjfY9WBoj5UXdhcF0bev6u5E4lBTQuXBS4Q-NNElNtMR-Das9rbyQ0hIYzQD2TvtR5JE-3RI_u4bK_1KYgXhZBODJyI1OFXV9pPzWYo1sVHmswjGbCy8jZCNz0dDgjgCPL5QXfInUgpe9mhB-3AvVYELqOKegKjVI1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادهای اوکراینی به مرکز لجستیک بزرگ نزدیک سن پترزبورگ در روسیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/683699" target="_blank">📅 18:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683698">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: دریافت هزینه خدمات از کشتی‌های عبوری از تنگه هرمز تصویب شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/683698" target="_blank">📅 18:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683697">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f4a95602.mp4?token=kAlMj2tsqBZu_6C-0Pei4sih5aSGNN82lXPWBcoIBVb7YH1KKYotAep57V30GO02NcyEgazVUa5eujQ_hmaTSs7WrKqp8M7cxPRDfSFFFPdhVmANut9Ov19GHfomZc8ys4aZaj6Eaa5SBO5Fkvv3Hwvj6Yl3HWEqT8SVlUOSACi08nLHX5QuhsZruIVl3Eei4WmaQq2q0nnXAq0LS9kJH8lBzV4wSXEFLj9YaBoIP_DfJaDIsSBtHHpaeJ0V09atspFmK66SAozuqpwzEvdOMIb_D21JvCX-cOP-FFf9nZ1MJi1BEZHg5USPsFFrs8NN9soYoYMPe9kUy39mOzaSUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f4a95602.mp4?token=kAlMj2tsqBZu_6C-0Pei4sih5aSGNN82lXPWBcoIBVb7YH1KKYotAep57V30GO02NcyEgazVUa5eujQ_hmaTSs7WrKqp8M7cxPRDfSFFFPdhVmANut9Ov19GHfomZc8ys4aZaj6Eaa5SBO5Fkvv3Hwvj6Yl3HWEqT8SVlUOSACi08nLHX5QuhsZruIVl3Eei4WmaQq2q0nnXAq0LS9kJH8lBzV4wSXEFLj9YaBoIP_DfJaDIsSBtHHpaeJ0V09atspFmK66SAozuqpwzEvdOMIb_D21JvCX-cOP-FFf9nZ1MJi1BEZHg5USPsFFrs8NN9soYoYMPe9kUy39mOzaSUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احیای مراتع خشک تانزانیا با گودال‌های هلالی
🔹
پنج سال پیش، در مراتع خشک آروشا در تانزانیا گودال‌های هلالی برای مهار روان‌آب و هدایت رطوبت به خاک ایجاد شد؛ روشی که با کاهش سرعت آب و فرسایش، به رشد دوباره پوشش گیاهی و احیای زمین کمک کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/683697" target="_blank">📅 18:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683696">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: دریافت هزینه خدمات از کشتی‌های عبوری از تنگه هرمز تصویب شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683696" target="_blank">📅 18:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683695">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0f10383f9.mp4?token=vokg-3BjgoiZykdbqJPECGa9u4Xs_Pj3VruHxiWiVnUAGxveiiz8ecfVAvWlOkVpjmK9-Y-DFU-a_tDuXXhvrvw6I_LJ4vrEKp4mljpHx0fDvw-UKc1Qirjq3rcAEkKedhcY3LnTVemDNwWslbW-HHiRaooLxlYi9kTKZRz1icp7Lqc83I7LShAzN0oMI9NigqeEqj0BHd5N7_GyjsraFhNaQdti7SaWGD11EO01E9fQmaR0g8-ve6ceYFPr-dIqnTlM1xPv6xRhbgB26idYqMHciStAcDgnPL03K-DO-jsVzBG6QNHuTUATkKa6C3VgrD9QCNnYDOwjoOPRC8aoLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0f10383f9.mp4?token=vokg-3BjgoiZykdbqJPECGa9u4Xs_Pj3VruHxiWiVnUAGxveiiz8ecfVAvWlOkVpjmK9-Y-DFU-a_tDuXXhvrvw6I_LJ4vrEKp4mljpHx0fDvw-UKc1Qirjq3rcAEkKedhcY3LnTVemDNwWslbW-HHiRaooLxlYi9kTKZRz1icp7Lqc83I7LShAzN0oMI9NigqeEqj0BHd5N7_GyjsraFhNaQdti7SaWGD11EO01E9fQmaR0g8-ve6ceYFPr-dIqnTlM1xPv6xRhbgB26idYqMHciStAcDgnPL03K-DO-jsVzBG6QNHuTUATkKa6C3VgrD9QCNnYDOwjoOPRC8aoLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین طرح هواپیمای مسافربری ۸۰۰ نفره را رونمایی کرد
🔹
این هواپیمای بال‌تک‌سوار با عرضی ۱.۶ برابر بمب‌افکن B-2، ظرفیت حمل بیش از ۸۰۰ مسافر را خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/683695" target="_blank">📅 18:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683694">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoojtCqzS_tW4Ob2OSothNByRBOYYdENXLI3vZnSykBaJpuJCGSzop3Jx6l12mGitt8RURhMqdc-cxKo2Zh1_gkUQyvlPXCjW-SD_jectfe-ucSlqcdcgQYq8EuYiVLoWfzF_Zepz5IRLO5OVvTdgVzTwvkSm2tV4tCLHeUfOET-zlzvfOjGc-PzfjeQBeAsODS9ELIW5Ru4U43TqiE6eDRT-DnakGL0YC9yI1hgj9FFkTuyQLoEWGXVxrUpWkf5dqE8ztdOiJPuGL5QNsaQCE9xOWobgMx5ccmh3znhYOrku_Y5hdRukNEdk0C3j8BtmiQ-tKD_CgxGZhLFN20eBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در انتخاب پزشک، کدام عامل برای شما مهم‌تر است؟
🔹
در این نظرسنجی حدود ۲۶ هزار نفر شرکت کردند که سهم روبیکا ۵۳، بله ۲۹ و تلگرام ۱۸ درصد بوده است.
🔹
حدود ۷۳ درصد از شرکت‌کنندگان، تخصص پزشک را مهم‌ترین عامل در انتخاب پزشک دانسته‌اند و ۱۱ درصد نیز توصیه دوستان و خانواده را در رتبه بعدی قرار داده‌اند.
🔹
این یعنی در انتخاب پزشک،
اعتماد به توانمندی
نقش شرط اولیه را دارد و عوامل دیگر بیشتر تعیین می‌کنند که از بین پزشکانی که قابل اعتماد به نظر می‌رسند، کدام‌یک انتخاب شود.
@amarfact</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/683694" target="_blank">📅 18:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683693">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erkZ0mLJBsUrQOsP0J_7RCwckM6nvN6pYSE-IrWoH1YpW37Rfi7PyJQMxZCSQu4eJ94_xS2PzQZ3_g52pRbP4dCuzAuIyykci5JwCMj5TWf0koasOUUtVA7-wspRVF6sXpQbIZiBJ3Y-JPb8FhhV3usapkdMpJo_WCaa3C52xkmiw0_7E6IRFqdJL45eJfutS-ksxUT_LCkdhpw0Gj5iZ9LuYAuHAqPWOjkNd4nGf6e_U8TJ38qYDjeSq7rtWcry4w6juT4DhY7n5gFxK1SQKRBSfCLXx7IeBpsUKDaox8R5LTF7emePxSkHc8roBDLX17zfQNIduH9LXC84yjzSsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال‌تایمز: جنگ با ایران آسیب‌پذیری حضور نظامی آمریکا در غرب آسیا را نشان داد
فایننشال‌تایمز:
🔹
پایگاه‌های عظیم نظامی آمریکا نزدیک به چهار دهه ستون فقرات حضور این کشور در غرب آسیا بودند، اما شش ماه جنگ با ایران میزان آسیب‌پذیری این ساختار را آشکار کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/683693" target="_blank">📅 18:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683692">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02b1d573bc.mp4?token=TxAS8qScDj_0OzYfwKtlYTTj0heDRLBfUBWdCXffALj0cKKUAlUfH7Tq2SFcYolEOvVEcwIX-CwB_Mb5-dfLILZKuGMVoQ8RfY5e9gzN08NBfNsKn7v8v0-8ItBkM3yr0eJa2kbv5CxSQYHwW2bSxxKczTnsF_ZjnfJtGT-iutKhT23N7JtbSFTccSPOsbkX5S-Mnx073lkY7sZiHsWVmA3IT4AKz6iTrftkydbgby0azJXXxxPbOjY2vx-a9rQSrBvpxgjtNIkfQnBWeBucY24F0fcF9GnfN96xdhjzvSgJ8FslBKZHSTdYBzHkj1RqqeK69ByD1PmoDVQ6xt3iYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02b1d573bc.mp4?token=TxAS8qScDj_0OzYfwKtlYTTj0heDRLBfUBWdCXffALj0cKKUAlUfH7Tq2SFcYolEOvVEcwIX-CwB_Mb5-dfLILZKuGMVoQ8RfY5e9gzN08NBfNsKn7v8v0-8ItBkM3yr0eJa2kbv5CxSQYHwW2bSxxKczTnsF_ZjnfJtGT-iutKhT23N7JtbSFTccSPOsbkX5S-Mnx073lkY7sZiHsWVmA3IT4AKz6iTrftkydbgby0azJXXxxPbOjY2vx-a9rQSrBvpxgjtNIkfQnBWeBucY24F0fcF9GnfN96xdhjzvSgJ8FslBKZHSTdYBzHkj1RqqeK69ByD1PmoDVQ6xt3iYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۶ جمله کاربردی زبان انگلیسی که مطمئنا به کارتون میاد #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/683692" target="_blank">📅 18:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683689">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzRlfJND5wTuVrhBcyUtU0Eflaop2WTVgBvZzVCyAqovvbOgfwAEIrzwyYiNhgWTOTh0P4HbiYrc-rK609-0aaLBP_jm9Mm5z4uAHKznWmR6jgIzMTyl6WZo8fN5ZmnvEbE-xuxjUse54GkssPR_m0ZtNAyeCkEep2aSVPX2p_SbslrHbjZbBydMIhgAXBEIWMk70M5Q_88Lzl1umHcPoowSNfb1crjYdaggo19p4E7ePObymoVyIXRFjjiXICHZMcyubdI1EsjB9jkz0oPh1r_Fzo9QPuGoxV-wnwYS-3Hz7MLrS-QawB0_0PO9iZD0Vh6ziSfPyxMZ0eCh8hekTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دوره آموزش طراحی طلا و جواهر با Rhino و Matrix
+ گواهینامه قابل ترجمه از سازمان جهاد دانشگاهی صنعتی شریف
🔹
برخی سرفصل‌ها:
📌
آموزش پروژه‌محور طراحی طلا و جواهر
📌
مدل‌سازی سه‌بعدی با Rhino و Matrix
📌
طراحی انگشتر، گوشواره و آویز
📌
اصول سنگ‌گذاری و ضخامت‌دهی
📌
آماده‌سازی فایل برای پرینت سه‌بعدی
⏱️
مدت دوره:
۴۰ ساعت
🎯
سطح:
مقدماتی | همراه با منتورینگ اختصاصی
✅
بدون نیاز به پیش‌زمینه
اطلاعات بیشتر و ثبت نام
👇
https://t.me/+FN40rMsbFhoyZjU0</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/683689" target="_blank">📅 18:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683688">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaI5TcnVI2dCisFRDQPVKRCV1N9rV78WES-D_LE0zJU0p0SSDaLLVbNpNPgGMI5lY3cmb_o_KacK6SEZpTDf7A2z_Jt7CWdxpRoieK7kaInscGgl6J_EvvfbvaunLl6DuFhByPVmsZQ4GVKZwgpS8_dmjCSBJGx1o1_FCdugnxci7nuHwn2ZvtdOpGWmw0I9wy-D29lneYlXTozLr9bEGpi3Dy9CnY5Xc2dWhXBhlq_Kan8VZts01TQaZFxSenFlBBLJolxNmfLA3oXvg2wF85sWbnfluG9EqVEutt7Ncigjo6df7t_wG49KA1kNlxeVabVK1JywZ083CUXnvq7yeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: فشار اقتصادی علیه ایران مثل بومرنگ به صورت آمریکا می‌خورد
🔹
واردات گوشت یخ‌زده برای کنترل قیمت گوشت؟ باشه، شاید جواب بدهد.
🔹
اما برای اوراق قرضه چه نقشه‌ای دارید؟ می‌خواهید بازدهی یخ‌زده وارد کنید؟
🔹
برای مسکن، خریداران یخ‌زده وارد می‌کنید؟
🔹
برای چاره‌اندیشی دستمزدها، فیش‌های حقوقی یخ‌زده صادر کنید؟
🔹
یک سیاست خارجی یخ‌زده و بدون ابتکار، اقتصادی یخ‌زده و راکد به بار می‌آورد.
🔹
تنها چیزی که هنوز در حرکت است؟ بومرنگ ایران که به صورت خودتان برمی‌گردد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/683688" target="_blank">📅 17:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683687">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87707f32c3.mp4?token=kpDAaQeJF3Ez2m4SCZqKyK9HVsF6EhgpH4sdm77TQ6oYhVbJbOzXZRfGpbsLB6nRHxd0TKxHhbotdX092YAbP3wDLdAyiG3UdxmEtFoOOhqF3GL5O4YgEV3i120Ja9RtYGQB8MUTpR5UaPrWgmQQwhWcMudAPClTMgNRdcayqA4Ut59E87xw1T0l7vmQ7qgxwpaHL4rMXiKCVJJYkM6RLe636BMU6Meu-Lm8PVdqvRCbAMlM3oerQn_lULEPxfRzH-Rnh6pL3w1FxAbNsuMot6fpGvX5ra3Bz0zLuTZIMjb3vwrk2411jaF9xKt1IApEfcYVXFv9tSVG-VEvF259DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87707f32c3.mp4?token=kpDAaQeJF3Ez2m4SCZqKyK9HVsF6EhgpH4sdm77TQ6oYhVbJbOzXZRfGpbsLB6nRHxd0TKxHhbotdX092YAbP3wDLdAyiG3UdxmEtFoOOhqF3GL5O4YgEV3i120Ja9RtYGQB8MUTpR5UaPrWgmQQwhWcMudAPClTMgNRdcayqA4Ut59E87xw1T0l7vmQ7qgxwpaHL4rMXiKCVJJYkM6RLe636BMU6Meu-Lm8PVdqvRCbAMlM3oerQn_lULEPxfRzH-Rnh6pL3w1FxAbNsuMot6fpGvX5ra3Bz0zLuTZIMjb3vwrk2411jaF9xKt1IApEfcYVXFv9tSVG-VEvF259DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای تلخ سقوط یک خانواده در هند
🔹
یک جوان ۱۸ ساله در هند به‌دلیل اختلاف با پدرش بر سر پرداخت اقساط آیفون قصد داشت از بالای دره خودکشی کند.
🔹
مردم با وعده خرید آیفون ۱۵ پرو او را منصرف کردند، اما هنگام نزدیک شدن پدر، هر دو به دره سقوط کردند و مادر خانواده نیز پس از مشاهده این صحنه به پایین پرید؛ در نهایت هر سه جان باختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/683687" target="_blank">📅 17:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
رئیس سازمان نظام دامپزشکی: همه پت‌شاپ‌ها در کشور غیرقانونی هستند
رئیس سازمان نظام دامپزشکی:
🔹
پت‌شاپ‌ها در کشور به‌صورت غیرقانونی فعالیت می‌کنند. آن‌ها اجازۀ فروش دارو و مکمل‌ها را ندارند.
🔹
درحال حاضر اتحادیۀ گل‌فروشان، آرایشگران و بعضاً اتاق اصناف برای راه اندازی پت شاپ‌ها مجوز می‌دهد، درحالی‌که طبق قانون سازمان نظام دامپزشکی مسئول صدور مجوز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/683686" target="_blank">📅 17:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683685">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db946df252.mp4?token=PYUE6QlwZW8WWtBjSfHqAEo-R3xQSUDdrSQ-4n6DWv8V63PVzg0ThBLOTkrPq4A6PUfjFIipSHuo-U6WLMUcza0XeQzCWr8D2N9tM5_xOcmYP_4ktNO4VbJIAMQqto9-TtIcGe0be0AKbarFGvp4u23vo4X26E-cScDF2Zv-VGrbXZ7eUy46LaKxQaQET8uwhSHN3iFdaEZjpEAnW-ltq3ml1tw8DcqZ-qPW_DudbRja-w66lDJ7FuDRws9_ZsUBfs7fBuj_HSk-2BsNki4EFhGCO-GTGdp1aw7GxHH2V36xqfR6fUi_va8gHsc35v0-1QboCRKAyJC76Ram34wEiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db946df252.mp4?token=PYUE6QlwZW8WWtBjSfHqAEo-R3xQSUDdrSQ-4n6DWv8V63PVzg0ThBLOTkrPq4A6PUfjFIipSHuo-U6WLMUcza0XeQzCWr8D2N9tM5_xOcmYP_4ktNO4VbJIAMQqto9-TtIcGe0be0AKbarFGvp4u23vo4X26E-cScDF2Zv-VGrbXZ7eUy46LaKxQaQET8uwhSHN3iFdaEZjpEAnW-ltq3ml1tw8DcqZ-qPW_DudbRja-w66lDJ7FuDRws9_ZsUBfs7fBuj_HSk-2BsNki4EFhGCO-GTGdp1aw7GxHH2V36xqfR6fUi_va8gHsc35v0-1QboCRKAyJC76Ram34wEiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: رزمندگان حزب‌الله در علی‌الطاهر در شرایط عاشورایی هستند/ اگر به شکل هدفمند به نیروهای اسرائیل در خاک لبنان حملۀ موشکی شود، فشار زیادی به اسرائیل وارد می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/683685" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683684">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dd18bba1f.mp4?token=GhiMRRK8TTXC19uNmr9DXBgV7vY8NHbwp1AQfVf1U4HiGF8BJQCZCqbrr8oq6LqX1cZqVBzb_aa9apU0ww_692wlo7bbgiUqUbPIZSovoYEulUiw-5jAakq0HBOszcwUnYiHB_9V3cDdDuaUcWUZBHvxdZCiYmelRJ5XFJsi7EPS5xVyE_kfmRqWjLzGzXeuC7qilpEdLzMGeX02BWkmrT5BPR-A6X_0DZCsNtoYj8S8cKBqVvzmub6NTB9GH8smV38Kf_DuvlE_65S4Z9kqu_KnnTy110qLT7nPu6QHv8NVEeECcixqbCj7v015qKsmYG3z0r5brZAwHXGPjo75WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dd18bba1f.mp4?token=GhiMRRK8TTXC19uNmr9DXBgV7vY8NHbwp1AQfVf1U4HiGF8BJQCZCqbrr8oq6LqX1cZqVBzb_aa9apU0ww_692wlo7bbgiUqUbPIZSovoYEulUiw-5jAakq0HBOszcwUnYiHB_9V3cDdDuaUcWUZBHvxdZCiYmelRJ5XFJsi7EPS5xVyE_kfmRqWjLzGzXeuC7qilpEdLzMGeX02BWkmrT5BPR-A6X_0DZCsNtoYj8S8cKBqVvzmub6NTB9GH8smV38Kf_DuvlE_65S4Z9kqu_KnnTy110qLT7nPu6QHv8NVEeECcixqbCj7v015qKsmYG3z0r5brZAwHXGPjo75WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان شدید چند هواپیما را در ایتالیا جابه‌جا کرد
🔹
وزش باد شدید در شهر فورلی ایتالیا چندین هواپیما را جابه‌جا کرد؛ سرعت تندبادها به ۱۲۰ کیلومتر بر ساعت رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/683684" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683683">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
عاصم منیر در راه تهران  اسماعیل بقائی سخنگوی وزارت امور خارجه:
🔹
فرمانده ارتش پاکستان برای تقویت همکاری‌های دوجانبه و رایزنی درباره امنیت منطقه دوشنبه به ایران می‌آید.
🔹
منابع العربیه ادعا کردند: فرمانده ارتش پاکستان، پیام‌های آمریکایی را در جریان سفر خود…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/683683" target="_blank">📅 17:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683682">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2576646bde.mp4?token=lOqml2QihMxyAfBJJTsRDsADXB-9gJhi4D4mjuzIqb645UPpjIVKVnBJh2ukpU9lew_PU35m1KQvhSi0CgXaJWwYxQYmr1_l2lf6H_oKN94TmIuJP7JmwSPnfaQluo2G-JmchU0qtlEJmeYhi2yXTnYMRyaHFh0tvShZECYQyEVtdDwd_FKL4pk36ZkUIu-rsv0W-8W6yKq6-xMbinLoa5wtKWHOZLyygg1kGSSzOPQKjkebra9vgdc-4dgK_2xRn6aK1oYYWzPBE3XPyNqs6mARMHwkHf-M_9CD91KoRBdiHkUUFVBHBWJy9sA7cru1ybHDiMsHpjtb3NjY8bcLHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2576646bde.mp4?token=lOqml2QihMxyAfBJJTsRDsADXB-9gJhi4D4mjuzIqb645UPpjIVKVnBJh2ukpU9lew_PU35m1KQvhSi0CgXaJWwYxQYmr1_l2lf6H_oKN94TmIuJP7JmwSPnfaQluo2G-JmchU0qtlEJmeYhi2yXTnYMRyaHFh0tvShZECYQyEVtdDwd_FKL4pk36ZkUIu-rsv0W-8W6yKq6-xMbinLoa5wtKWHOZLyygg1kGSSzOPQKjkebra9vgdc-4dgK_2xRn6aK1oYYWzPBE3XPyNqs6mARMHwkHf-M_9CD91KoRBdiHkUUFVBHBWJy9sA7cru1ybHDiMsHpjtb3NjY8bcLHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات‌های انسان‌نما در پکن قدم برداشتن را تمرین کردند
🔹
در افتتاحیه دومین دوره بازی‌های جهانی ربات‌های انسان‌نما در پکن، ربات‌های کوچک دوپا با گام‌های لرزان و زمین‌خوردن‌های پیاپی، تلاش کردند مهارت راه‌رفتن و حفظ تعادل را تمرین کنند.
🔹
این ربات‌ها برای حرکت و حفظ تعادل، بارها به کمک نیاز داشتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/683682" target="_blank">📅 17:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683681">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e9d4a30cf.mp4?token=gSuvgS21YXDP3mEYHDClkiwKp_t7y7bS-aRmzr2XzuOGFAtMSOXWRKEsaooM9ZNOpY7JCSh5u7W7y0rNXSWIZN6zc5d0wmwd4y9eKxxgd2xeRFdq7fDuIT7kvNPP3lGBPFVMLyM5oX5UhkCWwNG4NKvS5BRB6TPM0A6iT63ob2qwKJVHcaex2oSA-VfPDjWWXh5hXvGy9h0QU702p1o4jhydZkCg3E2GRMmIMWkj26NoGsTzK25bX3m6w4Mje5bH2fiEfNqTo8eiDzuDov3MpcS8Gf7BhAv5p-78P4EGXvsU1ydsFYHoLbYpXlRK0JNls0ZlRlk62C_294qDTg4ahw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e9d4a30cf.mp4?token=gSuvgS21YXDP3mEYHDClkiwKp_t7y7bS-aRmzr2XzuOGFAtMSOXWRKEsaooM9ZNOpY7JCSh5u7W7y0rNXSWIZN6zc5d0wmwd4y9eKxxgd2xeRFdq7fDuIT7kvNPP3lGBPFVMLyM5oX5UhkCWwNG4NKvS5BRB6TPM0A6iT63ob2qwKJVHcaex2oSA-VfPDjWWXh5hXvGy9h0QU702p1o4jhydZkCg3E2GRMmIMWkj26NoGsTzK25bX3m6w4Mje5bH2fiEfNqTo8eiDzuDov3MpcS8Gf7BhAv5p-78P4EGXvsU1ydsFYHoLbYpXlRK0JNls0ZlRlk62C_294qDTg4ahw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
روایت شما از ایده‌هایی که در خانه جان گرفتند؛ تلاش‌هایی امیدبخش برای رونق اقتصاد خانواده و ساختن فردایی بهتر.
🔸
یک پیام صوتی حداکثر ۳۰ ثانیه‌ای شامل نام، شهر، نحوه شروع و نتیجه کسب‌وکارتان، به‌همراه عکس کسب‌وکار برای ما ارسال کنید. روایت‌های برتر فرصت معرفی و تبلیغ در خبرفوری و کانال‌های زیرمجموعه را خواهند داشت
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/683681" target="_blank">📅 17:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683680">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/513dfe4113.mp4?token=qEFIUqgUvdUHntICA-lt_534ZEWTmBIo9UIQ5xka9tqgzH7kvSfJUSWpZGm-YpN1SIKEEn5Ie0na4VJ0JWEr8bQPYBR6B8Iw5-UbgiZa3pP_qXdIOWP9LHa0aqvFPTI0E3d0kIzj3pAxFBKqa2oIYLFm7RnaXlMQutQHPWCoLkEhxzvuHqy-Fg1hrQ8hQHpxf11ffV9HVDNXgZG7kNbmfCszLqYsawm1m4MD-0VWPIjNnPwmaGujnXWMHBZFvbyaB03ZQtag3Ct3XBYGgK24vZpjnY8UMk-cyLoxTZia3WtPQZrAYL_OKGeRRPe70DlDTSQgEdzZLoKASJ6e2OTHprW2vqDNufgqKQnIuNLjqC8TQ01kJhM1V22MxghZTXrXr5TDpSlQIqipFjwvw-6kWXnqyObOVWhxI8SA5plk0VRtQOJ5s_rBdOOsjO4AFLmH4JWJRCVG1EFNnyjWh8AOm8cByvagz8iBw6Sy6kPHjCPVQAhk757zFy5LGN9yriWouEgjeE9pmB2YJJFEXrvv_eDvL_XcE5PusU-EPBTxaCu-7MKIIl9sl6QUyl76zLRgrtqlEqvObq_2LFV4SUiAO8XtNGc-wSsbZHQEn-v6vVvPibV6Nk-Kfsnmh1t61Eet6Uxxtzu3r_cQoloy8lecG39bRJUa8WSkCdwwQu-dffQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/513dfe4113.mp4?token=qEFIUqgUvdUHntICA-lt_534ZEWTmBIo9UIQ5xka9tqgzH7kvSfJUSWpZGm-YpN1SIKEEn5Ie0na4VJ0JWEr8bQPYBR6B8Iw5-UbgiZa3pP_qXdIOWP9LHa0aqvFPTI0E3d0kIzj3pAxFBKqa2oIYLFm7RnaXlMQutQHPWCoLkEhxzvuHqy-Fg1hrQ8hQHpxf11ffV9HVDNXgZG7kNbmfCszLqYsawm1m4MD-0VWPIjNnPwmaGujnXWMHBZFvbyaB03ZQtag3Ct3XBYGgK24vZpjnY8UMk-cyLoxTZia3WtPQZrAYL_OKGeRRPe70DlDTSQgEdzZLoKASJ6e2OTHprW2vqDNufgqKQnIuNLjqC8TQ01kJhM1V22MxghZTXrXr5TDpSlQIqipFjwvw-6kWXnqyObOVWhxI8SA5plk0VRtQOJ5s_rBdOOsjO4AFLmH4JWJRCVG1EFNnyjWh8AOm8cByvagz8iBw6Sy6kPHjCPVQAhk757zFy5LGN9yriWouEgjeE9pmB2YJJFEXrvv_eDvL_XcE5PusU-EPBTxaCu-7MKIIl9sl6QUyl76zLRgrtqlEqvObq_2LFV4SUiAO8XtNGc-wSsbZHQEn-v6vVvPibV6Nk-Kfsnmh1t61Eet6Uxxtzu3r_cQoloy8lecG39bRJUa8WSkCdwwQu-dffQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریه آیت‌الله آملی لاریجانی زمان نام بردن از برادر شهیدش، دکتر علی لاریجانی
رئیس مجمع تشخیص مصلحت نظام:
🔹
از برادر عزیز و شهیدم، دکتر علی لاریجانی یاد کنم که شخصیت واقعاً ممتازی بود؛ دلسوخته نظام بود، در برابر جفاها صبور بود، تجربه‌های اجرایی مهمی در وزارت ارشاد و صداوسیما داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/683680" target="_blank">📅 17:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683679">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9acc6d6680.mp4?token=YRm0sXzjYciWB_3_-ef9pJcSepQptCr77I7hKVr2hiv-CxrUvV-HaCIoLkCnPmPswjLZ8sx8093l6Vur580UeEckkuL7STZ7ojGkjkRLz0weMTz4NMPkfBO-oh0rNbXVsUHTStmJ3oOg5dgb5CU4H13U8gtIRhjBE8xe_kKz48zOeA2IZBfej94Nh8pl5YyrhNbxQd2xeFtSAEBMdORUtEAy_aEMA7UU944mDOkd3Oy62I7XX-i7ve7xfhp5OEItf-IhfLx5ZO6czcFpzSEszV2Cy6PnTQLXCS5f7IXZLzwoimYuLal5-mAUYq2Oe7i6231dKSBz_hbuDbWL1tl58yn52NU7csrm5kTESkzV8__MX5XP5Py55fo-4ShbFBtTEfa8-sKxpR83UKUwI_q-ir2G-epRMz4RBEnBcVhHtHwyMlVTuxDvix4UgQL3VmEaHQb72ZGQtSS0AEYHt4_Hj_Jd1aczLQxNyPt_xykOykSdx28Ut5LWRsSCKCNXB16Ye5XqTTVaoHHM4_LlbNBcfQ1OP5jG3enX90O6RqlIsjLnwNaC_x2Kgjk9X1gf7VXPMt8PLqMy1adyRDQIu8UXtcN52owa0sTRoVnYE423QG2u1j_ze9elEeT5pr-nKd3Zm-tWuDzsQqYjbwlx1vyhZfQeAd7FyfGdS310LoaSIaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9acc6d6680.mp4?token=YRm0sXzjYciWB_3_-ef9pJcSepQptCr77I7hKVr2hiv-CxrUvV-HaCIoLkCnPmPswjLZ8sx8093l6Vur580UeEckkuL7STZ7ojGkjkRLz0weMTz4NMPkfBO-oh0rNbXVsUHTStmJ3oOg5dgb5CU4H13U8gtIRhjBE8xe_kKz48zOeA2IZBfej94Nh8pl5YyrhNbxQd2xeFtSAEBMdORUtEAy_aEMA7UU944mDOkd3Oy62I7XX-i7ve7xfhp5OEItf-IhfLx5ZO6czcFpzSEszV2Cy6PnTQLXCS5f7IXZLzwoimYuLal5-mAUYq2Oe7i6231dKSBz_hbuDbWL1tl58yn52NU7csrm5kTESkzV8__MX5XP5Py55fo-4ShbFBtTEfa8-sKxpR83UKUwI_q-ir2G-epRMz4RBEnBcVhHtHwyMlVTuxDvix4UgQL3VmEaHQb72ZGQtSS0AEYHt4_Hj_Jd1aczLQxNyPt_xykOykSdx28Ut5LWRsSCKCNXB16Ye5XqTTVaoHHM4_LlbNBcfQ1OP5jG3enX90O6RqlIsjLnwNaC_x2Kgjk9X1gf7VXPMt8PLqMy1adyRDQIu8UXtcN52owa0sTRoVnYE423QG2u1j_ze9elEeT5pr-nKd3Zm-tWuDzsQqYjbwlx1vyhZfQeAd7FyfGdS310LoaSIaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سونامی استعفاء در پلیس رژیم صهیونیستی
🔹
در ادامه بحران‌های داخلی در ساختار امنیتی رژیم صهیونیستی، گزارش‌ها از وقوع موج بی‌سابقه استعفاء در میان فرماندهان ارشد پلیس این رژیم حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/683679" target="_blank">📅 17:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683678">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgERqAtcUSi1gKJ4gIDoXqAu-DuBdGbmg14SL123ufn3ks0AniU7bgK6hRcIrmUFl7u4ADzL4xMWJo439S5HRVh1HpmDx6uzIEQFLcL-_h-ErUSCHB-bNfkIlnft8iP6frRkXow9cVH4pvXEzWwqLLElQJZLCLG7_H62hzrZJAsakI6uKy5pc3xvdq-qV3T_2RnJQunMkadISkayGvc1eArID8NgKMVc61UT3g9sstdsBJBOeAzik9oLFiwEM6ltRY_mZ7fNN0wEAQM_S35vgPEftdG68IUj4YkgP6Ec4xE6u6ulvKzq3qeKdRffKtbddAE5bLHe4AdElOAzKK4J-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفاعی از جنس تناقض؛ چرا پرونده پژمان جمشیدی همچنان خبرساز است؟ | مامک جمشیدی چه می‌گوید و چه چیز را نمی‌گوید؟ | کسی که شهرت دارد می‌تواند «عشق و حال» کند!؟
🔹
در ماه‌های اخیر، پرونده حقوقی پژمان جمشیدی، بازیگر سرشناس سینما و فوتبالیست سابق، از یک پرونده قضایی عادی به یک میدان نبرد فرهنگی و اجتماعی تبدیل شده است.
گزارش میثم اسماعیلی دراین‌باره را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3239817</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/683678" target="_blank">📅 17:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683677">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebc59613b.mp4?token=IFXZow_c-7AfgeEg5jKsQEJspjv9jkRGAqA6upslCcbT19V9XkG47ADu4Ds3qOZy3d8v3Xz4BVnz2b-fIa83miKQmPwjiPz7sLN91-uM2zPrwiUIpe7vgK62HkEh7G2A2SS8zJce9b6_reufrdloQ6chW46q3vYnv8pQgjhNNGvfFqnzlFTImShS2z7u5a70y4EW2C2XaRn3ea3eFT0wrD32D78ZFvmHY9XvnYco0K-JOhjRvkBOLJXR_MJBgAxNSAdsuqnCVoeKMdKC0xOQmB9HfmD1J3rj1dptqq1CNu-CJCFsG9-KXWdVbKEHxwf64nZKK3JgW5sL1R230l1dbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebc59613b.mp4?token=IFXZow_c-7AfgeEg5jKsQEJspjv9jkRGAqA6upslCcbT19V9XkG47ADu4Ds3qOZy3d8v3Xz4BVnz2b-fIa83miKQmPwjiPz7sLN91-uM2zPrwiUIpe7vgK62HkEh7G2A2SS8zJce9b6_reufrdloQ6chW46q3vYnv8pQgjhNNGvfFqnzlFTImShS2z7u5a70y4EW2C2XaRn3ea3eFT0wrD32D78ZFvmHY9XvnYco0K-JOhjRvkBOLJXR_MJBgAxNSAdsuqnCVoeKMdKC0xOQmB9HfmD1J3rj1dptqq1CNu-CJCFsG9-KXWdVbKEHxwf64nZKK3JgW5sL1R230l1dbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالروز ازدواج حضرت خاتم‌الانبیاء و ام‌المومنین؛ خدیجه‌کبری‌"صلوات‌الله‌علیهما"
خجسته باد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/683677" target="_blank">📅 16:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683676">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پلیس فتا تهران از شکار هکرهای تلگرام و اینستاگرام بعد از نقض حریم خصوصی ۳۵ شهروند تهرانی خبر داد.
🔹
سوریه: گفت‌وگو با اسرائیل درباره توافق امنیتی به‌زودی از سر گرفته می‌شود.
🔹
میدل ایست آی: ده‌ها پایگاه اروپایی از عملیات آمریکا علیه ایران در جنگ ۴۰ روزه، پشتیبانی کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/683676" target="_blank">📅 16:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683675">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8-X_t6UsYPTZt58Szbc--ktmpTw-BEhABZjYcRsAh9SEiAdrtiwjN0vvceD8N8W2FYvBQ58ch3MixwJ_B-w7-YTEdRO5FTeVaWNUoSM5gHe6mmRHHU9Gki6S39TNNkR2mfz9alyYTltBxc1FLZJtbIWWfZpIj2wStVaUdsYQ89xU4BE8wfbJKwPT11H8e2LqLiqY_7EVGENJ9uDud47FrpK3pDeSa3SSmlMX9cAAGKqwQZBiMo1LVL5WOLt1wdyEiR8gVvy-2BakAyW1BCBAWPPAGL1TwIESLlO7GULWb6TZmRJ8Rpup6Z5g96_M4-3eUdMBHlQU8F6BTIp25dSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای داشتن موهای پرپشت و بدون ریزش، باید چند نکته را رعایت کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/683675" target="_blank">📅 16:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683674">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f578783ddf.mp4?token=NPzdO8t7WxP742FrJm87Uyv-t2onUcLnWKZwkOIbi1WUZek7nipC6F5R9fd_zv8IsvC-IztN0IAQs3UorISYjISO-zg_2EyJxb6bLjY7Qi91yZok9eY2xOBSbOmQ5Y9eEukxaZEb2XRcPlHXnxgn3V04o7QHb-t6nQ5FJewVIwdi8nMeu1lDe-r5yMFQvpIW3PZqP34LMjeqgiZ6f3sfKf_QOLa0HdmrzrOEzZyiDgY0eD59At-wV5CQ4clCsQk6ppbvApW92AFhngnbT8BPjGZMhgFZ1sKnOH0et2wUZpXr2fDEa3niagDllduKlQZ2AMLoZy3NiYpUD6ZyhQ1o3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f578783ddf.mp4?token=NPzdO8t7WxP742FrJm87Uyv-t2onUcLnWKZwkOIbi1WUZek7nipC6F5R9fd_zv8IsvC-IztN0IAQs3UorISYjISO-zg_2EyJxb6bLjY7Qi91yZok9eY2xOBSbOmQ5Y9eEukxaZEb2XRcPlHXnxgn3V04o7QHb-t6nQ5FJewVIwdi8nMeu1lDe-r5yMFQvpIW3PZqP34LMjeqgiZ6f3sfKf_QOLa0HdmrzrOEzZyiDgY0eD59At-wV5CQ4clCsQk6ppbvApW92AFhngnbT8BPjGZMhgFZ1sKnOH0et2wUZpXr2fDEa3niagDllduKlQZ2AMLoZy3NiYpUD6ZyhQ1o3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعبیر تند اندیشمند سرشناس آمریکایی از ترامپ
پروفسور جفری ساکس:
🔹
سیستم سیاسی آمریکا فاسد و ساختارش فروپاشیده است؛ «یک خودشیفته خبیث» قدرت آغاز جنگ را در دست دارد!
🔹
دونالد ترامپ رسماً و به شکلی بسیار جدی دچار بیماری و اختلال روانی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/683674" target="_blank">📅 16:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683673">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
جرائم بیمه شخص ثالث از ۲ تا ۱۳ شهریور بخشیده می‌شود
🔹
جرائم وسایل نقلیه فاقد بیمه شخص ثالث از ۲ تا پایان ۱۳ شهریور ۱۴۰۵ به مناسبت هفته دولت و هفته وحدت، به‌طور کامل بخشوده می‌شود.
🔹
این بخشودگی فقط برای خرید بیمه‌نامه شخص ثالث یک‌ساله اعمال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/683673" target="_blank">📅 16:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683672">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZFN3dgqsp8gl-dlQsa0h7E1tE0-trVVqzqVL-eDN6qvtQo3pG9cyBPMq54FH_LrTkOBiuC1xlxs_gFPvAYuQnPldUshOdwpNWb0MACp8u1fCA9XmaKFt-dOo_LZ_IU9Xxa5TjS4r0OPQhcBGLynX6BYsPMYLeiJAJM6zTFbDFo4jAeq3Le7jdE1ebCIDmB2zx-acco5Fw11YWxSaDYA3OVaEC3DFcBSCtfZojHHAlRyzssQH3Hfcm3Q4Gknik7c0wXfqrPI4WDejik-9EPvX6IE3z3P4GWvLHcS2pMRCQpLs1OnsWD68zCSjYbUgNrftqsC_fJoTpCuVggOGIWxGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سخنگوی سپاه‌ به جنگ اقتصادی ترامپ
؛
برای هر اقدام خصمانه آمریکا سناریو داریم
سردار محبی:
🔹
رئیس‌جمهور آمریکا می‌گوید دستور جنگ اقتصادی را صادر و شدیدترین جنگ اقتصادی علیه ایران را شروع کردیم. این اعتراف ضمنی به شکست مفتضحانه دشمن در عرصه نظامی است.
🔹
اگر در عرصه نظامی پیروز می‌شدید، لازم نبود جنگ اقتصادی را آغاز کنید. مگر جنگ اقتصادی تازگی دارد؟ ۴۷ سال است جنگ اقتصادی می‌کنید و همه ارکان اقتصادی ما را تحریم کرده‌اید. کار فعلی دشمن فقط ادراک‌سازی و ایجاد باور برای مردم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/683672" target="_blank">📅 16:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683671">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
حمله پهپادی یمن به مواضع مزدوران سعودی
🔹
برخی منابع خبری گزارش دادند که نیروهای مسلح یمن در تازه‌ترین عملیات تهاجمی خود، مواضع و تجهیزات مزدوران وابسته به رژیم سعودی را با استفاده از پهپادهای تهاجمی در استان الضالع هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/683671" target="_blank">📅 16:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683670">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b72c5b22.mp4?token=UBBISplgumnkMs7LUXvcN7fduQoGT6WnbssGv5ZY1YJdbIuwum4eTlAeaW5SdOGTkIs1sQSufdo2LB3KNEVaVVvUNeeqKMmYbrS0OWZCyuuD9sJjejBMV8zx1mi75rfCGEVNbBtmNiZwjKNgDipspl-gWfqcdkjvjQHKpfeTi4iFbZI7YC19j9jvn2kItnBdj6X0LWKzr0ejk6H0UIFgJE8Di2nMTKVU8s-iTvCY36EBI3mkUDJvnWK8ofx2_U1SG0_C3hHgdmxYzEQOVgdHzb5Fq8j-3wo10laSuHn7eew6NLJsok6yJY-Gye79avtzpDLEnuPGQKgPk8YkxumOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b72c5b22.mp4?token=UBBISplgumnkMs7LUXvcN7fduQoGT6WnbssGv5ZY1YJdbIuwum4eTlAeaW5SdOGTkIs1sQSufdo2LB3KNEVaVVvUNeeqKMmYbrS0OWZCyuuD9sJjejBMV8zx1mi75rfCGEVNbBtmNiZwjKNgDipspl-gWfqcdkjvjQHKpfeTi4iFbZI7YC19j9jvn2kItnBdj6X0LWKzr0ejk6H0UIFgJE8Di2nMTKVU8s-iTvCY36EBI3mkUDJvnWK8ofx2_U1SG0_C3hHgdmxYzEQOVgdHzb5Fq8j-3wo10laSuHn7eew6NLJsok6yJY-Gye79avtzpDLEnuPGQKgPk8YkxumOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید سوپاپ زودپز چطور کار می‌کند این ویدیو را ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/683670" target="_blank">📅 16:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683668">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2358d2fbe1.mp4?token=nIRB5QywmghbL3BZcYDHNh9i2VasNRkbs0s4aDoiC7M0mhJGKlZIW33f1g1OqNtw6fwGhPL8B7_pvHQfddHPY6dqowsGE0PPmhseR4HD5SKvki5Pj74b0hvuElmbiOejNrMeuAA3iWYdj4ak6go7t-XDK4yekmFIkIFlfbYja8vJLwJA5X0RJdOfDRD0CQUoIRQua6H0ZH29_FZBAqqfAMFVKlVl0WGaKl02Za9Oyz99n5NTeuT1U6tP88j_PTIASkpYkC7caAdYwm1wZPYBoCJSkd7kOAp0LRGouC3fbSBKl8WvGetFvI-xzNWx95LcVZxjc1LWwwdiUb9rwBQ-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2358d2fbe1.mp4?token=nIRB5QywmghbL3BZcYDHNh9i2VasNRkbs0s4aDoiC7M0mhJGKlZIW33f1g1OqNtw6fwGhPL8B7_pvHQfddHPY6dqowsGE0PPmhseR4HD5SKvki5Pj74b0hvuElmbiOejNrMeuAA3iWYdj4ak6go7t-XDK4yekmFIkIFlfbYja8vJLwJA5X0RJdOfDRD0CQUoIRQua6H0ZH29_FZBAqqfAMFVKlVl0WGaKl02Za9Oyz99n5NTeuT1U6tP88j_PTIASkpYkC7caAdYwm1wZPYBoCJSkd7kOAp0LRGouC3fbSBKl8WvGetFvI-xzNWx95LcVZxjc1LWwwdiUb9rwBQ-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسئول کانادایی: توافق با آمریکا دوام نمی‌آورد
🔹
پس از شکست ماه‌ها مذاکرات کانادا و آمریکا و توسل واشنگتن به جنگ تعرفه‌ای، نخست‌وزیر استان بریتیش کلمبیا در کانادا دیوید اِبی گفت: «نمی‌توان به ترامپ اعتماد کرد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/683668" target="_blank">📅 16:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683667">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259fa82692.mp4?token=FJhBmuFee0noUMJuK8n5LxfuyWQ8zkCEIgi2_Aafn6xqcT8jQm8pkC2KUTdznFDqy3Kx5aUi3oCBKsXk3wVviI2yS_wUdQN5_2e1_JdqJyL1pAh0bWa5rrW2Ew3K8GRkE0dYgkkqM01oV8VHQX0RgaVljjfWD1-MLb8aigW52VwPZoKPDRP_CYl_TANubBUssRwtZBoXF09qgKdDNLYM01V6nNMVn0zxv8sOsU1zpzNOyhQuOEWhPh01V4SkWrKawVdTnsbPQGkLBVl_uZo5FFIXYnPIY73OCPSya5cPXOHzSWe5VTXqpQ-UDjxHQtk3zBB0JPX0HLoHZH1CmSPnuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259fa82692.mp4?token=FJhBmuFee0noUMJuK8n5LxfuyWQ8zkCEIgi2_Aafn6xqcT8jQm8pkC2KUTdznFDqy3Kx5aUi3oCBKsXk3wVviI2yS_wUdQN5_2e1_JdqJyL1pAh0bWa5rrW2Ew3K8GRkE0dYgkkqM01oV8VHQX0RgaVljjfWD1-MLb8aigW52VwPZoKPDRP_CYl_TANubBUssRwtZBoXF09qgKdDNLYM01V6nNMVn0zxv8sOsU1zpzNOyhQuOEWhPh01V4SkWrKawVdTnsbPQGkLBVl_uZo5FFIXYnPIY73OCPSya5cPXOHzSWe5VTXqpQ-UDjxHQtk3zBB0JPX0HLoHZH1CmSPnuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قبل از خرید و سرما‌یه‌گذاری روی ملک، حتما این سه سوال رو‌ از مالک بپرس تا سرت کلاه نره #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/683667" target="_blank">📅 16:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683666">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cae100903.mp4?token=iQ8q8rGE8pAPSHpHclEifHPCDaj1tNRRCNTs1k0azMplCA1_Nnxg3Pe6bUa6uoyJnDinBx3pMTx22Rv1_zyOLTUu65Penj9AGZ15bwrnAXCbE04D3_e5gRGXK-KOsAYceY7xXv-daiW3i5PL3Kqd0ug3wdTnlOlFmc5IlsmnEUIXafmPW6WMFg6LDCdcEin_g_KsZjSOLiyUP-r0mxy35x8jcBdMAUNHliMwSlMDsoiWrHMyqyCSIGXm1r7U1wiIoKhXuhAPK4UPH3YS0sx8AqP5HgoabwNQ98EX9FvKDp-ByIVUbHYKX_gVpkDxSm4YdriJNBKEWOxgdByDiwm58YZX-iU4QSlOXWO4s_aWGFKOQUsRtbeMzr1M6nkbpS4iTvEffOpnLitE6n-qkaT-R5NpExIHxzDfZugtKR7WxAFUWOY-E8etwwNQ8DArBS9z1kpQhIwjnSCfuctymo6CrqoK1yrCqRDT0i3EPcsGO7zXMvcodK7QH1Hnhl0xfcPQW6zIsJ5aMkUubOWwrr4-vvqzDK7Q8e66DleNFLIcPVGoOwrBdvqRu8iInkUOZiKXxBa6df7yXZPXiiJdgZvIEamLTHOKbMed9XfPtWOFxhQlF1GDfKyDvY5-bRq_EGGPfDMLE0xoZZJqUju_8wRF6nEQT-y0PGCZTU852AvWzU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cae100903.mp4?token=iQ8q8rGE8pAPSHpHclEifHPCDaj1tNRRCNTs1k0azMplCA1_Nnxg3Pe6bUa6uoyJnDinBx3pMTx22Rv1_zyOLTUu65Penj9AGZ15bwrnAXCbE04D3_e5gRGXK-KOsAYceY7xXv-daiW3i5PL3Kqd0ug3wdTnlOlFmc5IlsmnEUIXafmPW6WMFg6LDCdcEin_g_KsZjSOLiyUP-r0mxy35x8jcBdMAUNHliMwSlMDsoiWrHMyqyCSIGXm1r7U1wiIoKhXuhAPK4UPH3YS0sx8AqP5HgoabwNQ98EX9FvKDp-ByIVUbHYKX_gVpkDxSm4YdriJNBKEWOxgdByDiwm58YZX-iU4QSlOXWO4s_aWGFKOQUsRtbeMzr1M6nkbpS4iTvEffOpnLitE6n-qkaT-R5NpExIHxzDfZugtKR7WxAFUWOY-E8etwwNQ8DArBS9z1kpQhIwjnSCfuctymo6CrqoK1yrCqRDT0i3EPcsGO7zXMvcodK7QH1Hnhl0xfcPQW6zIsJ5aMkUubOWwrr4-vvqzDK7Q8e66DleNFLIcPVGoOwrBdvqRu8iInkUOZiKXxBa6df7yXZPXiiJdgZvIEamLTHOKbMed9XfPtWOFxhQlF1GDfKyDvY5-bRq_EGGPfDMLE0xoZZJqUju_8wRF6nEQT-y0PGCZTU852AvWzU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#
فیلیمو
رو نصب کن
😍
۱۰ دقیقه تماشا کن
🍿
سفر استانبول ببر
✈️
فقط تا ۲۰ شهریور فرصت داری جزو برنده‌های ۱۰ سفر استانبول و ۱۰ سفر باتومی باشی؛ اونم با امکان سفر با هم‌سفرت و دریافت ۵۰۰ دلار وجه نقد!
💰
⛱️
r.filimo.com/Tsummer1405
@filimo</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/683666" target="_blank">📅 16:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683665">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8e1AiH4rPm9Gov2POrSD72JDX3unHwnkB1LQw5MklLos2NHbqmvlRtV4A4aI8JR8OADSivSUTfpyiWEAB0Nkc0Fz_AVreaRo92VL7D_9TVbh6X5xrZKzUNHgUrSt8WjTB7GDTKuy369TFmNRHx87fyF70YIMnq217YEnASEFhXITxJYodCbgoRgCKOZ_GEXmWzvib7Yh9B6agiQIuRTJ6cH5ICBTv6mbHmOj_Rrx_wfqF6VnQkGmjnY-TVmShFlfqIZi0Kqkpn9U2-Q4OAq6z5yaNN4R0a-jFmvTaPtSFYIpJwZ1_YwKtLl10oj4xt4HIURGC8cO3Ka7FG2Ouvamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
روایت ناقص و غیرمنصفانه رسانه ملی از بیمه سینا
🔰
هلدینگ مالی و سرمایه‌گذاری سینا با انتقاد از نحوه طرح برخی مطالب درباره بیمه سینا در یک برنامه تلویزیونی، تأکید کرد: ارزیابی عملکرد یک شرکت بیمه باید بر مبنای صورت‌های مالی، اطلاعات رسمی منتشرشده در سامانه
#کدال
و شاخص‌های تخصصی صنعت بیمه انجام شود.
بر اساس گزارش منتشر شده در سامانه کدال،
#بيمه_سینا
در سه‌ماهه نخست سال ۱۴۰۵ حدود ۶۷۰ میلیارد تومان سود شناسایی کرده است.
📎
مشاهده خبر
🔘
روابط عمومی هلدینگ مالی و سرمایه‌گذاری سینا
🔘
🌐
سایت
📱
بله
📲
ایتا
📲
تلگرام</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/683665" target="_blank">📅 16:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683664">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93519f61b6.mp4?token=f8GQz1rd0paw5QEjXUYJDQrzixTzE3EYHeBUXkJcFCybrgzsxdbGNbbdV9GtJ1Tj3_TCx6C_Gvsvli-a9wHsx15OhtiY65MH_wEGLB5fdiLwUj7twKuyWML07aCDzM8iD6XQf8XDVjIFG_WAfEPHMRFklrA2ykfepM0uGnSvKeO0B6Cm9iqn-r-c1CP2TUHWaXcSKk0xHCO79hvFj2KjgHfzlWofxgZJtK18W-0Ps3nZkzSikKRSNZzP8euxflSvAJ4A9l43m6LGOzFe-p_EnRAndfrpqEFYsvxiHp_FBOxYi7weonwkRvSL_V3qVaci6eQo8-hLH-Blt7cQhnb-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93519f61b6.mp4?token=f8GQz1rd0paw5QEjXUYJDQrzixTzE3EYHeBUXkJcFCybrgzsxdbGNbbdV9GtJ1Tj3_TCx6C_Gvsvli-a9wHsx15OhtiY65MH_wEGLB5fdiLwUj7twKuyWML07aCDzM8iD6XQf8XDVjIFG_WAfEPHMRFklrA2ykfepM0uGnSvKeO0B6Cm9iqn-r-c1CP2TUHWaXcSKk0xHCO79hvFj2KjgHfzlWofxgZJtK18W-0Ps3nZkzSikKRSNZzP8euxflSvAJ4A9l43m6LGOzFe-p_EnRAndfrpqEFYsvxiHp_FBOxYi7weonwkRvSL_V3qVaci6eQo8-hLH-Blt7cQhnb-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلوستر استالون در ۸۰ سالگی همچنان بدون بدلکار فیلم بازی می‌کند
🔹
پشت‌صحنه فیلم جدید سیلوستر استالون نشان می‌دهد این بازیگر ۸۰ ساله همچنان برخی صحنه‌ها را بدون استفاده از بدلکار اجرا می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/683664" target="_blank">📅 15:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
از این پس برای پرداخت مهریه بیشتر از ۱۴ سکه فقط ملائت زوج ملاک است
🔹
با رای نمایندگان مجلس شورای اسلامی هرگاه مهریه در زمان وقوع عقد تا ۱۴ سکه تمام بهار آزادی یا معادل آن باشد وصول آن مشمول مقررات ماده (۳) این قانون است؛ چنانچه مهریه بیشتر از این میزان…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/683663" target="_blank">📅 15:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683662">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff65586258.mp4?token=fBRZs7Jg3uvbuy_wicqmp7rC2c-oTIa_3wdmwMSbhTvb0cO07DLVszC9NV2x8GqguPgkZITlEqqxgOy1x6H1NxRC0xX4EuoVAc6c9BHWWz_evrYCkGuGkcHSMfEM0IZ33_92legYmynOI7SUBEc-aEC1ksKv5L8TBqRWZ-YpHonjzUVVa0PxYLRxLIYjJVyeZOgvjoIf5MNnZXwfDjHs1fkVdON0whreuhc9p1t-7D8syHzUTodjhaXWcvVfA2ZxEbiHIlYRI_hNucF_BcxzaXfB8gOnJTvHfjoluPVwB7v4d0BMBlLnz1oH4K6979W7I93di4IpijWuPlilUuAfKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff65586258.mp4?token=fBRZs7Jg3uvbuy_wicqmp7rC2c-oTIa_3wdmwMSbhTvb0cO07DLVszC9NV2x8GqguPgkZITlEqqxgOy1x6H1NxRC0xX4EuoVAc6c9BHWWz_evrYCkGuGkcHSMfEM0IZ33_92legYmynOI7SUBEc-aEC1ksKv5L8TBqRWZ-YpHonjzUVVa0PxYLRxLIYjJVyeZOgvjoIf5MNnZXwfDjHs1fkVdON0whreuhc9p1t-7D8syHzUTodjhaXWcvVfA2ZxEbiHIlYRI_hNucF_BcxzaXfB8gOnJTvHfjoluPVwB7v4d0BMBlLnz1oH4K6979W7I93di4IpijWuPlilUuAfKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دست از خیال‌پردازی برای تنگه هرمز بر نمی‌دارد
🔹
رئیس‌جمهور آمریکا بار دیگر با انتشار تصویری از خلیج فارس «تنگه هرمز» را «قلمرو جدید آمریکا» نام نهاد.
🔹
این توصیف طی روزهای گذشته موجب تمسخر و انتقادات زیادی در محافل آمریکایی شده است.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/683662" target="_blank">📅 15:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: تولید روزانه ۳۰ رهگیر ۵ هزار دلاری برای مقابله با پهپادهای ایرانی در امارات
🔹
طبق این ادعا، یک شرکت آمریکایی در امارات روزانه ۳۰ رهگیر پهپادی با قیمت حدود ۵ هزار دلار تولید می‌کند؛ این رهگیرها بر اساس طراحی اوکراینی ساخته شده‌اند و فرزندان دونالد ترامپ از سرمایه‌گذاران این شرکت هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/683661" target="_blank">📅 15:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683660">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6310a3a91.mp4?token=EPjbJFUoLql7fk1zD7YJNishL_CObc9gONgH_bNx6fLwG4YrPcQ-aqJItFxcEHcOMN9WFllyS2SLqfgy2uSPXX4A4o3k0OV3JDE8ziUoSknd51blvMnEu9YZSP7OQF03Z-z_TLhH1vR3idTrWRc1lDJVCAWMeTDaRaWEjqL7J0Oopopy9KjHNUejgQKrhg24XbS7CcI8Ioda7Q4JJ8lmw9BGt1mscNWc0A-23RtwgTKk3hzhAEaYdOZ8NnvdSNui4rckKbXu7eJ-OeYdWGCM9ghqzQUQqL-tA_tnkI1e4JOfkIbwHbup4ibgm17AiBj4AgSVcCHZWoK4vWtyX3Ojmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6310a3a91.mp4?token=EPjbJFUoLql7fk1zD7YJNishL_CObc9gONgH_bNx6fLwG4YrPcQ-aqJItFxcEHcOMN9WFllyS2SLqfgy2uSPXX4A4o3k0OV3JDE8ziUoSknd51blvMnEu9YZSP7OQF03Z-z_TLhH1vR3idTrWRc1lDJVCAWMeTDaRaWEjqL7J0Oopopy9KjHNUejgQKrhg24XbS7CcI8Ioda7Q4JJ8lmw9BGt1mscNWc0A-23RtwgTKk3hzhAEaYdOZ8NnvdSNui4rckKbXu7eJ-OeYdWGCM9ghqzQUQqL-tA_tnkI1e4JOfkIbwHbup4ibgm17AiBj4AgSVcCHZWoK4vWtyX3Ojmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش‌سوزی در پالایشگاه الدوره در بغداد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/683660" target="_blank">📅 15:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683659">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2060940b7.mp4?token=N3DRC9efDqheLzEBXeXDVUUQXuQLaTYnvd4sESGO6MikmtdjeJ6Oos6bVQkpmKC0nXI66zVlJEakxeWmjTmqWyrlvtIIMAC6UMBL5oHX_G3lkUw-s_1Suuo-bZTfMwb6eIMwcMrsjh97G9Cn1fIjuL_iZ_jjMCIp5gC2_rM8K4vwfXCRnKo8JMcot19PxmrLr_zWYEWpC2wMlDFdQwS0KsnokTXzjp-gvfUboFyPxlm_0LvzVfeGlb948LrzMyEQtaK8LTlcE1RGSqOY52o4odek9JhYfJceVNSrPGcQF_EMLNJKCWVrGLbsWi7Vmk6FkjR6Rr2J25mjZdcj2T5WPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2060940b7.mp4?token=N3DRC9efDqheLzEBXeXDVUUQXuQLaTYnvd4sESGO6MikmtdjeJ6Oos6bVQkpmKC0nXI66zVlJEakxeWmjTmqWyrlvtIIMAC6UMBL5oHX_G3lkUw-s_1Suuo-bZTfMwb6eIMwcMrsjh97G9Cn1fIjuL_iZ_jjMCIp5gC2_rM8K4vwfXCRnKo8JMcot19PxmrLr_zWYEWpC2wMlDFdQwS0KsnokTXzjp-gvfUboFyPxlm_0LvzVfeGlb948LrzMyEQtaK8LTlcE1RGSqOY52o4odek9JhYfJceVNSrPGcQF_EMLNJKCWVrGLbsWi7Vmk6FkjR6Rr2J25mjZdcj2T5WPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لپ‌تاپ تاشوی هواوی MateBook Fold در عمل
💻
🔹
هواوی MateBook Fold با نمایشگر ۱۸ اینچی OLED تاشو، به دو نمایشگر ۱۳ اینچی تبدیل می‌شود و قابلیت استفاده به‌عنوان تبلت را دارد؛ این لپ‌تاپ حدود ۱.۱۶ کیلوگرم وزن و ضخامت بسیار کمی دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/683659" target="_blank">📅 15:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683658">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17363ff22.mp4?token=Tj18tfcgYG_VoAsrweB1qxPU8mtbw8MbwkQP9JrPs0RPLfZ6YygA4D-QQiOZbR1Ii15KfxXZ7h-iVcVXhcDennKJgR4NiKX4auJnW0aRoTkK76eiH-FdFW5U65uZy4d9aZXcZoZ0ZGnn2Oo-LehsyHjocFsmbbchfvQWnoDKjjEn8ysTkTvqbIKf-wj-hUCuCKzsBmje2SbGKSIzZZVSF0x-cWqLt0WuLZL_XkfYXnAhyXPjEGGoeKhV5zlDfYuh3cC-S2UPCmTxxL6WfpOLC-UoIrRiHsatYxHhdcbrhr_mY6VR5XIVk01sImFZImUtvwZKBI1QovkbuKQ3nzE7-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17363ff22.mp4?token=Tj18tfcgYG_VoAsrweB1qxPU8mtbw8MbwkQP9JrPs0RPLfZ6YygA4D-QQiOZbR1Ii15KfxXZ7h-iVcVXhcDennKJgR4NiKX4auJnW0aRoTkK76eiH-FdFW5U65uZy4d9aZXcZoZ0ZGnn2Oo-LehsyHjocFsmbbchfvQWnoDKjjEn8ysTkTvqbIKf-wj-hUCuCKzsBmje2SbGKSIzZZVSF0x-cWqLt0WuLZL_XkfYXnAhyXPjEGGoeKhV5zlDfYuh3cC-S2UPCmTxxL6WfpOLC-UoIrRiHsatYxHhdcbrhr_mY6VR5XIVk01sImFZImUtvwZKBI1QovkbuKQ3nzE7-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار انتاریو: ترامپ هر روز بخشی از دارایی شما را می‌دزدد
داگ فورد، استاندار انتاریو کانادا، با انتقاد از ترامپ:
🔹
ترامپ از آن دسته افرادی است که روز اول پول ناهار شما، روز دوم کلاه و روز سوم کفش‌هایتان را می‌دزدد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/683658" target="_blank">📅 15:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683657">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Armg3q0L2eD8c_24C9HGmZiJNHGI2FsUEOC05y_jomolCIs714b5ovmhjaU1mVSoY5By1w9tkmnSUxLWbKj7eogH1NJkl1AeJeE_nO1t7hm6BIYcAlD1EkVZ4qxn3uy0KVTh9fNFBPITREmxZxiUuDuOdsN0c8MlKGXFjWAdzV6t9ZFPScvv6kgP_E2Kh0UmAfVFG01OscfgwfQWexSqDr0afiewOSHjYA5LbSJzWB-l1J7JldajywTmYNFAhYCFtKEiDm35ycQc7Lj5BP1sMQC8TdWnOcV3dTSMpwZxb4ZelNjqKVsCYRFeUFhu8rGMkr-YoBFz3I0eGqlUTHCpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا و دلار یک قدم تا فتح کانال جدید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/683657" target="_blank">📅 15:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683654">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13dd860634.mp4?token=dtiuyZBqckH_WIre6Qg_ZLcXlT_9OSmZV6mmymRk5loyaMV_tMF4ee9dQLIiiK_VQwmvCAV_Mz-Yn8CvTR5jU5jREF-kX3qFjSZcd47VicUQrDEdgLGpip8Ww0KHqWUyuI9TuNhmNbJXiREHzYU5eXz5ylCgBeLUhI0hodhh-uuhyC_8mNSxb-m_hkxfWlfLgCbtf_BuESVes7YSouZvBKUvJVkDiR5-5SW0HztyYq2QSA-asixXgxacD5J9k8wxn8D5PH_spwG6SrtfxUbXThHvJ4bR5xX829BkQXmDqK_5QAtjEoWp0e4vujp091iyxAqUjTabxGhAosW46aHg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13dd860634.mp4?token=dtiuyZBqckH_WIre6Qg_ZLcXlT_9OSmZV6mmymRk5loyaMV_tMF4ee9dQLIiiK_VQwmvCAV_Mz-Yn8CvTR5jU5jREF-kX3qFjSZcd47VicUQrDEdgLGpip8Ww0KHqWUyuI9TuNhmNbJXiREHzYU5eXz5ylCgBeLUhI0hodhh-uuhyC_8mNSxb-m_hkxfWlfLgCbtf_BuESVes7YSouZvBKUvJVkDiR5-5SW0HztyYq2QSA-asixXgxacD5J9k8wxn8D5PH_spwG6SrtfxUbXThHvJ4bR5xX829BkQXmDqK_5QAtjEoWp0e4vujp091iyxAqUjTabxGhAosW46aHg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فکر می‌کنین کاربرد فلش کوچک کنار آمپر بنزین چیه؟
🤔
#حواست_هست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/683654" target="_blank">📅 15:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683653">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsN02R1X2_K36DQ6hobOCBlvvfR2C71LOGhwRdGLgu9doSkYskN8EFtZ3A3tOwcDjnY6R243ArdcHrAoHXnrf199BVA2hvWgfTcg7RLSqsyiYyzOMUk7VVfKN5uUm31za0KJreIzC8KIO8XtAF4LOSj2aB7Gi2uuwXpxUnxUKA0ITpH2G8OgX-qqkeKjfaEpwfpoJeNoNpiK78192FPjxL1lpJdiqF0TtCzXGbih5vLWJijpoqiltxDKshEGNhAFPkuz-Utoc3h71JClFa3fuuE9zzAb7_wwD3aXL7gK96kIyEhlMQEiiOUVCGD030BUtm7jWizNMG6_BQ76H86h2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام پلتفرم طلا در بازار هیجانی رفتار با ثبات‌تری دارد؟
دیجیاتو نوشت:
🔹
بررسی داده‌های روزانه پنج پلتفرم خرید و فروش آنلاین طلا نشان می‌دهد همه پلتفرم‌های آنلاین طلا در روزهای پرتلاطم به یک اندازه نوسان نمی‌کنند. این تفاوت برای سرمایه‌گذارانی که با هدف حفظ ارزش دارایی وارد این بازار می‌شوند اهمیت دارد؛ زیرا هرچه دامنه تغییرات قیمت کمتر باشد، احتمال مواجهه با نوسان‌های ناگهانی نیز کمتر خواهد بود.
🔹
طبق گزارش دیجیاتو پلتفرم میلی با میانه نوسان ۲ درصد و میانگین ۲.۴ درصد کم‌نوسان‌ترین رفتار را در میان پلتفرم‌های بررسی‌شده ثبت کرده است.
🔹
نزدیک بودن میانگین و میانه «دامنه نوسان روزانه» در میلی نیز نشان می‌دهد کم‌نوسان بودن این پلتفرم فقط حاصل یکی دو روز آرام نبوده، بلکه در بیشتر روزهای بررسی‌شده نیز الگوی مشابهی داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/683653" target="_blank">📅 15:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683651">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db7395b22.mp4?token=W_huEe7MnFImu_zWzWyN10CPJ62L-HXCZyxz5PhK_jPc3rb1CW41UBZY5yopc8DPs69nrj8AJZaCPbdITzi0H149uBCxhrjy8gEpluzX4kZ7WrvxIeV7dNYNV4Jho75Uy9vBxvES03-pMWXawMTSUqHk-AP4_iPx4eOZ5mGDs0Ror8WghxW9CfACmERMbw0GV-EWf8UuSlAx0OygCc1oa3MUZrWWJ_j-aHwUaLYls8juWZcH9ooD2h08wjnf5CdMqzdf_WPZE55y38as-H3e17rjffL6JDByybJrafzGku1cSCFsL52GVmKrIo7NVr5RDeNoQRGo9rMtwL_KCgV8Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db7395b22.mp4?token=W_huEe7MnFImu_zWzWyN10CPJ62L-HXCZyxz5PhK_jPc3rb1CW41UBZY5yopc8DPs69nrj8AJZaCPbdITzi0H149uBCxhrjy8gEpluzX4kZ7WrvxIeV7dNYNV4Jho75Uy9vBxvES03-pMWXawMTSUqHk-AP4_iPx4eOZ5mGDs0Ror8WghxW9CfACmERMbw0GV-EWf8UuSlAx0OygCc1oa3MUZrWWJ_j-aHwUaLYls8juWZcH9ooD2h08wjnf5CdMqzdf_WPZE55y38as-H3e17rjffL6JDByybJrafzGku1cSCFsL52GVmKrIo7NVr5RDeNoQRGo9rMtwL_KCgV8Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درّه‌های بی‌نظیر توران زمین، سیستان و بلوچستان
🇮🇷
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/683651" target="_blank">📅 14:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683649">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21eaf8b00f.mp4?token=OlLaZm2VwzGjXHt5SMl_Iqik0EuQ3-uhOXyaKsB1GXeHNzkr2QFJi_8J1t-n33ORViaofEfZCDiQw2zqmJoaVvM772LV-OjkOASeNa-sPnDZPgFimdA50qnEZquBZRMysIg1NunRaYcYVJunc19LRdh683bb3g7HdO7dlqDRAC-rtzXwe1rqzRkFCu03O8fWW7pSOsIDvPDxkqwnoBluXIodEOob0-LPETeDNbPvHae3FS4zVWJhG_RzTvNRCuXnmQceftdijuIs1byNAub4gwjYYIZ0M1lOyOlEeCoFNs1Th0MXfbqJ5gJRYyO2C5Qp1WSmnHl6qP2sD8Dv0iP62A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21eaf8b00f.mp4?token=OlLaZm2VwzGjXHt5SMl_Iqik0EuQ3-uhOXyaKsB1GXeHNzkr2QFJi_8J1t-n33ORViaofEfZCDiQw2zqmJoaVvM772LV-OjkOASeNa-sPnDZPgFimdA50qnEZquBZRMysIg1NunRaYcYVJunc19LRdh683bb3g7HdO7dlqDRAC-rtzXwe1rqzRkFCu03O8fWW7pSOsIDvPDxkqwnoBluXIodEOob0-LPETeDNbPvHae3FS4zVWJhG_RzTvNRCuXnmQceftdijuIs1byNAub4gwjYYIZ0M1lOyOlEeCoFNs1Th0MXfbqJ5gJRYyO2C5Qp1WSmnHl6qP2sD8Dv0iP62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیویورک آمریکا پس‌از بارش باران غرق شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/683649" target="_blank">📅 14:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683648">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
حذف حبس برای مهریه‌های بالای ۱۴ سکه  نماینده نجف‌آباد در مجلس:
🔹
طرح اصلاح نحوۀ اجرای محکومیت‌های مالی در صحن علنی بررسی شد. با تصویب این طرح، مجازات حبس برای مهریه‌های بالای ۱۴ سکه حذف شد.
🔹
در خصوص مهریه‌های زیر ۱۴ سکه، امکان اجرای احکام از طریق «پابند…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/683648" target="_blank">📅 14:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5tfF7VlVL_rEAzJSwli012TqEz6QfwPxgLCFfsikkrEN0TCYzD-HNF0aNx3zaZVgBn3uOT31bYaTAdSLfU9fawUDK_6IMLRKHrSqWJ1_f7bbJvx6wmAsytQBbz6NdXWVzNxIBNjsimg87xizscFj_aLCZk8TyZSvENFyMPxco0G3sHGAEPTHn8b8FPjywFZzxIp2AfbOc62qKNNS55lNP2KAgzSONJzggandQq1YWBZjrLwfUGOJ1Z_dp1n691moIgfxf0PAcCnYCFybLSJiGSfpt_9eRJCAd3GTx1qZIjdDwY3lGNhffMuHvj8r7QaMK61FG7WIMvmc_Oa0hesLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقاد کانال دو میلیونی حامیان پزشکیان از عطریان‌فر و تیم اطلاع رسانی دولت/ آقای پزشکیان همانطور که  بارها گفتی. اختلاف  افکنی به نفع صهیونیست هاست/ عطریانفر اعتماد به نفس عجیبی دارد و در فضای سیاسی غرق شده است
🔹
انتقاد از دبیر شعام و نماینده رهبری را باب نکنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/683646" target="_blank">📅 14:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405ef17751.mp4?token=PGuMiIH6DRu89MyDlqk0GQOklrb3ZfeGHAnn6_ZxORcAwc5zbXuGuZdFs1x4mWcdQ9PluvwcfcFbUuXu3ROK9uVsrsegpTPgtt64_NAmfG7RotKjdMGX_0a_3qanhi66XOfDNR_v0WNbF7EdlTubxl8nI9-00wCnLdrNm6viOf2sft_B5_afIf7tubX1TRtvL3UKayXgl-LPnxBTS2Q-gYy2DDjjbRBzy5xAGyIb2oLgX-2a4kEa_kpiGkK4Pvs-gzh8xR6Mcw1IoT1EFZ31HamSVEOmqUlnjCh8Q2l-qM0HI_1qAuyt9CtycETZIAkQbuLNnK5QITMMZZxC9M9dgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405ef17751.mp4?token=PGuMiIH6DRu89MyDlqk0GQOklrb3ZfeGHAnn6_ZxORcAwc5zbXuGuZdFs1x4mWcdQ9PluvwcfcFbUuXu3ROK9uVsrsegpTPgtt64_NAmfG7RotKjdMGX_0a_3qanhi66XOfDNR_v0WNbF7EdlTubxl8nI9-00wCnLdrNm6viOf2sft_B5_afIf7tubX1TRtvL3UKayXgl-LPnxBTS2Q-gYy2DDjjbRBzy5xAGyIb2oLgX-2a4kEa_kpiGkK4Pvs-gzh8xR6Mcw1IoT1EFZ31HamSVEOmqUlnjCh8Q2l-qM0HI_1qAuyt9CtycETZIAkQbuLNnK5QITMMZZxC9M9dgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مورچه‌های بافنده با کمک لاروهایشان لانه می‌سازند
🐜
🔹
مورچه‌های بافنده با استفاده از ابریشمی که لاروهایشان تولید می‌کنند، برگ‌ها را به هم می‌دوزند و لانه می‌سازند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/683645" target="_blank">📅 14:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05a479cdd2.mp4?token=P2EXkI_m9vCvoC1eiKDfNZTtFM2vf0dnVS3r4PfrgZwxkIVpIxWJxO5qNCuJmXuLTbYfKZT_5QWbqZPmdI7Jrr3tlteaJvqFbgzK8yZOyBWxMuqbtEcRrifme4EBJRD5i7zk4SsvfUmUO4GgdaCGExmGh5FTfqsay_TLx3pCGm3eKyiBTar0OJ6biAWCf5W1sQXObcJzb3hVT55eA9sb1pth2DYUzt94h25oLknS7pM4dW5nRrFG3jl6qVYKVT_GjFdClhtkkA4KJFZtI-XnlHlUJMVjrVl9GH_zr90rWUhoboLrsZi6EyVnQ0aWOn0fRy8475KtuHRydf6iLFwqQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05a479cdd2.mp4?token=P2EXkI_m9vCvoC1eiKDfNZTtFM2vf0dnVS3r4PfrgZwxkIVpIxWJxO5qNCuJmXuLTbYfKZT_5QWbqZPmdI7Jrr3tlteaJvqFbgzK8yZOyBWxMuqbtEcRrifme4EBJRD5i7zk4SsvfUmUO4GgdaCGExmGh5FTfqsay_TLx3pCGm3eKyiBTar0OJ6biAWCf5W1sQXObcJzb3hVT55eA9sb1pth2DYUzt94h25oLknS7pM4dW5nRrFG3jl6qVYKVT_GjFdClhtkkA4KJFZtI-XnlHlUJMVjrVl9GH_zr90rWUhoboLrsZi6EyVnQ0aWOn0fRy8475KtuHRydf6iLFwqQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/683644" target="_blank">📅 14:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
کشف ۷۰ هزار تلفن همراه احتکار شده
رئیس پلیس امنیت اقتصادی فراجا:
🔹
در مدت اخیر قیمت تلفن همراه به یکباره سه الی چهار برابر شده است.
🔹
همین موضوع باعث ایجاد حساسیت و فعال شدن تیم های عملیاتی شد که در یک فقره ۷۰ هزار دستگاه تلفن همراه به ارزش ۳ همت از ۶ شرکت کشف شد که احتکار کرده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/683643" target="_blank">📅 14:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a36cfee22c.mp4?token=J6HDpxL8SXCi9lxNLFoZ5cZC8gApXaQfBusFIZp_0YJU8UzBdJhqRGsB2UACuUflkWygZyd6ia6QI-fwF329xa64sqcPJm3Ev7REODMKaBvBFgfaKa1Coc_MPTkhdhw7Ut-NnFdkBlCad3hhggnNJ68jdXSsh-vTX-_4RkRpwwHeRTF0iGuHtiAAc0jHH9c91w1q_QUSapCSKvbiGcZdLynuvXs14oPsCTSV_X2V3zxfWn8Bk35kKM2bQ6_4KNBGKfFUwvWmjuM5LRr8MkZEXm-QoelAJRs2dDKSRSy3B86_3KQFWKZttSDcs6Kt1SL1kFkOdW7V3qxvCHPDSAUViiY8zu7iWu2wwqVL673JCPsWSZbSe259kBstquKjqE5yFxCaSaosq4ciIf1cCSY8Ok_V5niCjAUj-lL6-3H8nOj3-BtWv35otTAZdwZ1fVc6MeVZ-_HbjsTN6pAkRTjEqPyZmUTiUeLMvM6G0nSJe0yNn65NqlhQzw-qbn0HBtTN_-GsxF_BPbqYajEEVLLBM4E8QK4pvz5YrcTw9S4-qsrJVUqKiE82wTShDwB1phFkk3JSXSnDfuwIjEHbiGqUTpDs8URsNsAvQVQ6CZpoMxEGgHg3GfBaReasc0gOLZZbDVUJ5sFy6SFbgHMnrPfXqOAknNjuB-jK2X8uq4NlzOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a36cfee22c.mp4?token=J6HDpxL8SXCi9lxNLFoZ5cZC8gApXaQfBusFIZp_0YJU8UzBdJhqRGsB2UACuUflkWygZyd6ia6QI-fwF329xa64sqcPJm3Ev7REODMKaBvBFgfaKa1Coc_MPTkhdhw7Ut-NnFdkBlCad3hhggnNJ68jdXSsh-vTX-_4RkRpwwHeRTF0iGuHtiAAc0jHH9c91w1q_QUSapCSKvbiGcZdLynuvXs14oPsCTSV_X2V3zxfWn8Bk35kKM2bQ6_4KNBGKfFUwvWmjuM5LRr8MkZEXm-QoelAJRs2dDKSRSy3B86_3KQFWKZttSDcs6Kt1SL1kFkOdW7V3qxvCHPDSAUViiY8zu7iWu2wwqVL673JCPsWSZbSe259kBstquKjqE5yFxCaSaosq4ciIf1cCSY8Ok_V5niCjAUj-lL6-3H8nOj3-BtWv35otTAZdwZ1fVc6MeVZ-_HbjsTN6pAkRTjEqPyZmUTiUeLMvM6G0nSJe0yNn65NqlhQzw-qbn0HBtTN_-GsxF_BPbqYajEEVLLBM4E8QK4pvz5YrcTw9S4-qsrJVUqKiE82wTShDwB1phFkk3JSXSnDfuwIjEHbiGqUTpDs8URsNsAvQVQ6CZpoMxEGgHg3GfBaReasc0gOLZZbDVUJ5sFy6SFbgHMnrPfXqOAknNjuB-jK2X8uq4NlzOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک مدل بستن روسری که هم جلوی لباستو نمی‌پوشونه و هم مرتب می‌مونه و از روی سرت تکون نمی‌خوره
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/683642" target="_blank">📅 14:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683640">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a239b09a6a.mp4?token=vYi08PJYPbOcWNpTCQQHeJj1xUIQ8oa6HlWWx5z1jE9KQEukPDJ-JPApK37eblm5rzq9X8fQ6dOTR3rM72gaBdLBkQO1Ml-UP3_upG2HRXRcs0WoEKpZBz7y6CLg1rP1JAjbJWwf7orknxVuHijGnFSZH8QzPKakXJ7m2aeAQR-zM0p8K1wXYayX9zbwAdIZ3fScVdqv6XY8sqSYZeLl368GVa9kEJOi9QkV5RPnOrNCbYj7_my5QM7NOIJI9Nyo1dTeJMSRksTsaoXcxviyldgpk3vmkZyyS9vMkIx91rsGx89iz3p5wEN-J-2ZKeqLys1WgCCT-ip-DukfvsJbdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a239b09a6a.mp4?token=vYi08PJYPbOcWNpTCQQHeJj1xUIQ8oa6HlWWx5z1jE9KQEukPDJ-JPApK37eblm5rzq9X8fQ6dOTR3rM72gaBdLBkQO1Ml-UP3_upG2HRXRcs0WoEKpZBz7y6CLg1rP1JAjbJWwf7orknxVuHijGnFSZH8QzPKakXJ7m2aeAQR-zM0p8K1wXYayX9zbwAdIZ3fScVdqv6XY8sqSYZeLl368GVa9kEJOi9QkV5RPnOrNCbYj7_my5QM7NOIJI9Nyo1dTeJMSRksTsaoXcxviyldgpk3vmkZyyS9vMkIx91rsGx89iz3p5wEN-J-2ZKeqLys1WgCCT-ip-DukfvsJbdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کینِیو، نخست‌وزیر کانادا: «با آدم بد معامله خوب نمی‌شود»؛ ترامپ با جنگ ایران بنزین را گران کرد
اظهارات نخست‌وزیر کانادا، کینیو، درباره ترامپ:
🔹
افراد بسیار عاقلی گفته‌اند که "نمی‌توان با یک فرد بد، به توافقی خوب رسید"، و من فکر می‌کنم این اصل در اینجا نیز صدق می‌کند.
🔹
رئیس‌جمهور ترامپ دلیل این است که ما همگی در حال حاضر برای بنزین هزینه بسیار زیادی پرداخت می‌کنیم، به دلیل جنگ نادرست او در ایران.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/683640" target="_blank">📅 13:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683638">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c37dfca6.mp4?token=Z1d7Gc2Y2dLRp-XTzG-k290raBgL3qro2CiZse6r8JO0_5o9FeZLi3egpYxNu1R-LRK_p11PnHne4wRi3K-71pt_3LDn7_A6yagfMtXvTt6Ax4iwHoQ-PsN6EU4gtwz3BJaU9gJPj990o-lhQo_J3XoY1C2uifYynN4hvJNUTgZoLh6R7v11rq4jXgNR7ustrB9Mny1V14xO5XNcnbYj0gfZ1aKZoX8uOxgnVc2xWsbAQ5C9CUVv64rD8Odr41bCltUjExG0DyVzOmRDWEXgFGtSQTd3ITA3QHsmFrobtgCoRtYmYUdavH_J5faTBUSlB2pvmtdg_PBZzAuxJ2FngrHPD3TWTdjdgALyz7QPJoTELBF-Qr_hFVBxIyMYhlVkdtKsbkPDF-4Y9SfpaCJCoPGaRv3yRANC8AWe3ArbePPWFgPsxun8Dq-oV9rqN3Lv6w9J7bNb6TKXgYIqFYX31Tj3kOtn5I1-Ve0BfgWYvdRHwsuSL0WbiOWEVSj4-v6RjziHjGbd6ljNgpbI-XDTqdFIVo7mpf5yiM6-fKaWtZ-TpCnB3Mx9Z-isQmqyEi6JOfBCY8xFpZPdiYJF-c3kJ1JYm8ARW-XmaErs-8TEHOmEDkuVQgOgwbhOQ7v5ZoW-UFKGZfcPMbNtxqjiUoTm51EV1yb94oxgiHkdqpeAf0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c37dfca6.mp4?token=Z1d7Gc2Y2dLRp-XTzG-k290raBgL3qro2CiZse6r8JO0_5o9FeZLi3egpYxNu1R-LRK_p11PnHne4wRi3K-71pt_3LDn7_A6yagfMtXvTt6Ax4iwHoQ-PsN6EU4gtwz3BJaU9gJPj990o-lhQo_J3XoY1C2uifYynN4hvJNUTgZoLh6R7v11rq4jXgNR7ustrB9Mny1V14xO5XNcnbYj0gfZ1aKZoX8uOxgnVc2xWsbAQ5C9CUVv64rD8Odr41bCltUjExG0DyVzOmRDWEXgFGtSQTd3ITA3QHsmFrobtgCoRtYmYUdavH_J5faTBUSlB2pvmtdg_PBZzAuxJ2FngrHPD3TWTdjdgALyz7QPJoTELBF-Qr_hFVBxIyMYhlVkdtKsbkPDF-4Y9SfpaCJCoPGaRv3yRANC8AWe3ArbePPWFgPsxun8Dq-oV9rqN3Lv6w9J7bNb6TKXgYIqFYX31Tj3kOtn5I1-Ve0BfgWYvdRHwsuSL0WbiOWEVSj4-v6RjziHjGbd6ljNgpbI-XDTqdFIVo7mpf5yiM6-fKaWtZ-TpCnB3Mx9Z-isQmqyEi6JOfBCY8xFpZPdiYJF-c3kJ1JYm8ARW-XmaErs-8TEHOmEDkuVQgOgwbhOQ7v5ZoW-UFKGZfcPMbNtxqjiUoTm51EV1yb94oxgiHkdqpeAf0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین رقابت برای هوش مصنوعی خودمختار را وارد مرحله تازه‌ای کرد
🔹
چین روز گذشته چراغ «سینگولاریتی» را روشن کرد؛ اقدامی که به معنای تغییر یک‌شبه نیست، بلکه نشان‌دهنده ورود رقابت برای ساخت سیستم‌های هوش مصنوعی خودمختار و جایگزین نیروی انسانی به مرحله‌ای جدی‌تر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/683638" target="_blank">📅 13:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683637">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/369b433627.mp4?token=Je8qAYsnH847YJuPLX1EgGyomjmefNtPFkBAG4cXB1tb0yeZNJXeOGNTdHrdj3F_ANW2KsWJrH2K4jfnbQAytAo1wNIaq1YD48MDe1J4h7YX-niVAqhct_llRRcEhlRLiI-PEZUTsjjMdXMaxVwiZZPyMg5y-tW1ojlw0BhmSwZjU6ibQau37Am1ziVQup51zy5kUYeZbxNHGyQtPvtgNZOMamXWhklFsG4JUXKD8DVRgriw8-hLIGRAmj1hgj8tiLo-xAR0TRvCnXYqzudpcK5aOrYYboCrTvBCAH1EkjIvqRn8_H65Ydhd0VJCpADnQ_vbZHT-ZADYpxcFkFl9ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/369b433627.mp4?token=Je8qAYsnH847YJuPLX1EgGyomjmefNtPFkBAG4cXB1tb0yeZNJXeOGNTdHrdj3F_ANW2KsWJrH2K4jfnbQAytAo1wNIaq1YD48MDe1J4h7YX-niVAqhct_llRRcEhlRLiI-PEZUTsjjMdXMaxVwiZZPyMg5y-tW1ojlw0BhmSwZjU6ibQau37Am1ziVQup51zy5kUYeZbxNHGyQtPvtgNZOMamXWhklFsG4JUXKD8DVRgriw8-hLIGRAmj1hgj8tiLo-xAR0TRvCnXYqzudpcK5aOrYYboCrTvBCAH1EkjIvqRn8_H65Ydhd0VJCpADnQ_vbZHT-ZADYpxcFkFl9ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی: ۹۰ روز آینده برای ایران بسیار مهم است
منوچهر متکی، وزیر اسبق خارجه:
🔹
ترامپ می‌خواهد ایران را درگیر تفاهم اسلام‌آباد نگه دارد تا پس از انتخابات به سراغ ایران بیاید.
🔹
او افزود آمریکا در سه ماه آینده چهار راهبرد «جنگ محدود، آتش‌بس، محاصره و مذاکره» را دنبال می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/683637" target="_blank">📅 13:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683636">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbc6b4c1b.mp4?token=qvK78xx4GUE1dPvzfaiLri85s4CP5SaqdhSrAxeFSK8jTHg1JTxPLpUr3yWaiP31PDzdlr_reUJ7z5tz8bAhEv0KAn8Fx_C3oH3nLP1_WA3rPw5NpC8YXIA18nbFNBHrH_yEK2SN-ep5sHm23dzZTyLcdo8XEKVq_6YddQCx4QkQAkLG6cmEhxwCz4-DrqP9Mo91CTrc90_7qanXivK2n5kQAQ_wrM2SQOlmzUF1EMaSaDdtBZN3ZZ4g3tB51F__DLM-oe3dZwUnMZVqtaKfDu_E7ZuvPmh8OcGc8kR49y-jZiCBfGXg6rPagGKD2T_K9x40kM7JaXpnhrjjOBV-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbc6b4c1b.mp4?token=qvK78xx4GUE1dPvzfaiLri85s4CP5SaqdhSrAxeFSK8jTHg1JTxPLpUr3yWaiP31PDzdlr_reUJ7z5tz8bAhEv0KAn8Fx_C3oH3nLP1_WA3rPw5NpC8YXIA18nbFNBHrH_yEK2SN-ep5sHm23dzZTyLcdo8XEKVq_6YddQCx4QkQAkLG6cmEhxwCz4-DrqP9Mo91CTrc90_7qanXivK2n5kQAQ_wrM2SQOlmzUF1EMaSaDdtBZN3ZZ4g3tB51F__DLM-oe3dZwUnMZVqtaKfDu_E7ZuvPmh8OcGc8kR49y-jZiCBfGXg6rPagGKD2T_K9x40kM7JaXpnhrjjOBV-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار غیرحرفه‌ای و فرار رئیس سازمان غذا و دارو در نشست خبری
🔹
رئیس سازمان غذا و دارو پس از پایان سخنانش در یک نشست خبری، بدون حضور در نشست پرسش‌وپاسخ و از مسیری دیگر سالن را ترک کرد؛ درست زمانی که خبرنگاران می‌خواستند درباره مهمترین بحران‌های دارویی کشور مطالبات مردم را پیگیری کنند.
🔹
مسئولان حاضر در جلسه نیز از پرسش به پاسخ خبرنگار خبرفوری درباره ضعف نظارت ها خودداری کردند و مدیر روابط عمومی این سازمان گفت: «بعداً جواب می‌دهم.»
🔹
خبرفوری همچنان پیگیر و منتظر پاسخ این پرسش از سوی مسئولان ذی ربط است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/683636" target="_blank">📅 13:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683634">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d313a5cb6b.mp4?token=irUaNe1hp_AV1m7TI5DcjVG0B4X5i0CG_0NMDFaROt2sOoW0WJvdM5fTpgr7As3PO96bpYG6OYTJFx2BOejpwC7FewLckT45UrI-JKL5lwlH3wsxjJ1v2c_q3DiiptjQ9A1EbXxSVtQqNrDaRS4K7PDTy0e2qqPr43Hbx_SUAy-0e1F4A6653dPt7cwNgtZfWRJUba2EdZ8iaAeIdq-nHU3blyaZq2Mjct0ouVvFNjhlxCbgJzSu9MHC_a_rmAIxx7pQllhb50W5OvAVvOgJAC_-nRrGPueYDWV9wlskXn_HMZk0Iuv0J_kiJpRKgVd0_z3JLuak5jd-88QwOI_Omw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d313a5cb6b.mp4?token=irUaNe1hp_AV1m7TI5DcjVG0B4X5i0CG_0NMDFaROt2sOoW0WJvdM5fTpgr7As3PO96bpYG6OYTJFx2BOejpwC7FewLckT45UrI-JKL5lwlH3wsxjJ1v2c_q3DiiptjQ9A1EbXxSVtQqNrDaRS4K7PDTy0e2qqPr43Hbx_SUAy-0e1F4A6653dPt7cwNgtZfWRJUba2EdZ8iaAeIdq-nHU3blyaZq2Mjct0ouVvFNjhlxCbgJzSu9MHC_a_rmAIxx7pQllhb50W5OvAVvOgJAC_-nRrGPueYDWV9wlskXn_HMZk0Iuv0J_kiJpRKgVd0_z3JLuak5jd-88QwOI_Omw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موهایش را کوتاه کرد؛ ظاهر جدید هالند با سر تراشیده شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/683634" target="_blank">📅 13:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683633">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJMfFH3bZ27z_StVaIJQzu0b5ZfA6e-yDMAZ1E4FRpDPKT8uthGbKJHfhCVxc4t2yrWiDfUGMYgMAmggxnGkC_My5ZTqa10JQAQ6dZFzjZFPkyKONVhd9OQueVySzj_CyyIAT5S39Rq7DSQzE0JxotZziYwokG-IxeYQdSGofiA14ZVlGXUh35Zje3fAfCX4sMpN_0kHcItCfB7MkhMz2TAy6KSOErSxL-aBg5A9phPeUrJMrfojhRPCHCvaxrxcQy8sF9I1UFvuYSaoIvD26nkH1eceowjsOh3faVbCArdpPjutm7NSBeuokfIW52ZG4M0se95hOQwvAxNQLgJ8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
150 هزار تومان هدیه افتتاح حساب
اگر هنوز در ویپاد افتتاح حساب نکرده‌اید، با درج کد هدیه WP150k، پس‌از تکمیل افتتاح حساب 150 هزار تومان هدیه نقدی دریافت می‌کنید.
📋
دریافت هدیه افتتاح حساب:
1️⃣
اپلیکیشن ویپاد را نصب کرده و با وارد کردن کد هدیه WP150K، فرایند افتتاح حساب خود را تکمیل کنید.
* بلافاصله پس‌از افتتاح حساب، 150 هزار تومان هدیه نقدی دریافت می‌کنید.
🔗
همین حالا ویپاد را نصب کنید.
https://jryn.me/JvrbAQ</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/683633" target="_blank">📅 13:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683632">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
حذف حبس برای مهریه‌های بالای ۱۴ سکه
نماینده نجف‌آباد در مجلس:
🔹
طرح اصلاح نحوۀ اجرای محکومیت‌های مالی در صحن علنی بررسی شد. با تصویب این طرح، مجازات حبس برای مهریه‌های بالای ۱۴ سکه حذف شد.
🔹
در خصوص مهریه‌های زیر ۱۴ سکه، امکان اجرای احکام از طریق «پابند الکترونیک» فراهم شده است.
🔹
مصوبه برای طی مراحل قانونی و تأیید نهایی به شورای نگهبان ارسال شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/683632" target="_blank">📅 13:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683631">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e0cae6cc.mp4?token=vyhy5RL19_nkUHm0XgmiABs-5Ap4LNPcaukBYJ7VMrvH5e_Jqb-AjJ2d0b_VG_dZp2LYnfOKHm-PgVbHIraa9zk8nmH2KW0Q0zwtIRJKzosKXhjFzqRje9HN5NGkLdfAErbzN8cWcBm9hmZL6nQ3ydS4uRNp45csG83nzmhoQbqiLiKlX1ZhJMT0Qracqh7DW61f0CrOqjyKWEaqrg4UCH0YOazjhzHxbKGXnz2W_1GxhMIA6LUv6q8g7vlsLXdnav7Siikmy5pMzLHQUxCfDNcqLMuh7ZP1rj6IAzLbw2xG7O70kfQ35phSLeSKxA553GSPVnMxO8KMQ6qlWT-WnU4TlfkNf12RpC4XNJvSmSQAXuSFKWoH0ol0zY08bRbA7BDC64y2Ww1BNQiWpd1F6wseBovPYEzNKK14d7YrEzyGr_eUqj_aETNbVZcNQYKTNqN4GxQFcCs4OcFxJXhAbGlzL20qiWcIH3XJellFIH9FWRCzWLfdcDpC7x3_xskVQvgjL-ZERKbXreMgRfN8COsuPxCuhVm8YiJJxJv70R7Q_mcaTtl6mVAEVcawrrEoMITyNxBjeNuE0MHe6uEcH_H0PEJpkVVW-f0kSc012-xKFby9b0bAq8UFnZgBugHOZg9J53hielMXw_WIoqXbNF9evnM2FNYrXsazftQZ4Rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e0cae6cc.mp4?token=vyhy5RL19_nkUHm0XgmiABs-5Ap4LNPcaukBYJ7VMrvH5e_Jqb-AjJ2d0b_VG_dZp2LYnfOKHm-PgVbHIraa9zk8nmH2KW0Q0zwtIRJKzosKXhjFzqRje9HN5NGkLdfAErbzN8cWcBm9hmZL6nQ3ydS4uRNp45csG83nzmhoQbqiLiKlX1ZhJMT0Qracqh7DW61f0CrOqjyKWEaqrg4UCH0YOazjhzHxbKGXnz2W_1GxhMIA6LUv6q8g7vlsLXdnav7Siikmy5pMzLHQUxCfDNcqLMuh7ZP1rj6IAzLbw2xG7O70kfQ35phSLeSKxA553GSPVnMxO8KMQ6qlWT-WnU4TlfkNf12RpC4XNJvSmSQAXuSFKWoH0ol0zY08bRbA7BDC64y2Ww1BNQiWpd1F6wseBovPYEzNKK14d7YrEzyGr_eUqj_aETNbVZcNQYKTNqN4GxQFcCs4OcFxJXhAbGlzL20qiWcIH3XJellFIH9FWRCzWLfdcDpC7x3_xskVQvgjL-ZERKbXreMgRfN8COsuPxCuhVm8YiJJxJv70R7Q_mcaTtl6mVAEVcawrrEoMITyNxBjeNuE0MHe6uEcH_H0PEJpkVVW-f0kSc012-xKFby9b0bAq8UFnZgBugHOZg9J53hielMXw_WIoqXbNF9evnM2FNYrXsazftQZ4Rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید حسن خمینی: بعضی‌ها در لباس دوست یا دشمن نمی‌خواهند نام امام برای آیندگان بماند
🔹
مراد شهید ما خوب به ما یاد داد امام روح و جان انقلاب و جمهوری اسلامی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/683631" target="_blank">📅 13:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683630">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92478c154.mp4?token=pgQWuZT_LPmgLyLh0bgsrSSKviaJxDqsDdh07L4T7w8ouOjuxq77VUhubXC1xtwLTs7QVUj_Pf2-VtTDnd4BezJbRfY-7a1amHukrPyZbB6oYuHVw9Yjo6Lq0Y5cLIrIFGAAJkt5j3xDW56kJ0yOqOczH0eeeu46C4cVtdX457V3Qius9pxmxIWodwaQiMoRLAuG-C39jShMMWQs6EcvUduZWf2DYg5SHgJmfqrnSBzc_S79YiR5wJK75S-PjuNhtNiIU5pdNLXCBTkz2GoitkvipPNPJxoq6yOvxrCWpr0ESLq58ivJPUcwb5YTHGniSYI10BHXoeOwxVvvm6XdZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92478c154.mp4?token=pgQWuZT_LPmgLyLh0bgsrSSKviaJxDqsDdh07L4T7w8ouOjuxq77VUhubXC1xtwLTs7QVUj_Pf2-VtTDnd4BezJbRfY-7a1amHukrPyZbB6oYuHVw9Yjo6Lq0Y5cLIrIFGAAJkt5j3xDW56kJ0yOqOczH0eeeu46C4cVtdX457V3Qius9pxmxIWodwaQiMoRLAuG-C39jShMMWQs6EcvUduZWf2DYg5SHgJmfqrnSBzc_S79YiR5wJK75S-PjuNhtNiIU5pdNLXCBTkz2GoitkvipPNPJxoq6yOvxrCWpr0ESLq58ivJPUcwb5YTHGniSYI10BHXoeOwxVvvm6XdZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی صداها فقط شنیده نمی‌شوند؛ از میان خاطره‌ها عبور می‌کنند و به عمیق‌ترین جای دل می‌رسند…
🇮🇷
🖤
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/683630" target="_blank">📅 13:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683628">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/solpiAhijaDM9FOKV7O82AOcqaXzmSLGtWBP8Fn6xF0NQke5o6Of0JvBK2_qan0G69FKimeH_pO-lnu0BZFFmmLy747XY5B4McFm8COlxBNfqw0esSQQLA7WikdYFvC7lg3UNO4P_wgtcEFsouhxIhfK3ba8kjaakuOIH_ZJ4cRjFDr2GnlZ4wzsFjeFnlBlz06uSQS_3qdsXC0bQQbSlah8wNDSLBEKseOHPnKNM2JbhR_fYcePP5YlFKN4GFvmWaBPK0Z1geRQsxSU1hpW1hqQonfFcfByS7uHscbIDu-bAAPAVZDd5V3Dmb1IBy6ZhTCGiJlL8Wq-R8hhrJFUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین تصویر از مرجع عالیقدر آیت‌الله العظمی سید علی حسینی سیستانی به مناسبت ۹۹ سالگی عمر مبارک ایشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/683628" target="_blank">📅 12:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683627">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d7a17fbd0.mp4?token=iY-Pv1Kmegc-J8vhMFxUWGfKCrRvyuxtQ0LlHa_WyF8QG0YJKHREN8Iu3IgjpXR-G47iPWYektzEloJCKHiaXY3bfLSOmSCZpV2yBWiHCcM1SCw28eIOt_W7PXHAzdOBlGgC8ttdu-D9-D3OGL2bLDXgbveQFrW7m0KpxVcFtVncyjNKlbCQUyry3aytC9kliOdm3l05Z1zHar_OhvHtDVpCpowCF5zy79RJipWkaPR7DgnIwU2udgnLJgjLVOSk2yHfd3_KgOX24evmx7y-mUz1IlfRseTBD6w83I5Uq5dyWpG-KDxiccrsq1oDd7JEepSqKMK6XTZY2Hag6jtRuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d7a17fbd0.mp4?token=iY-Pv1Kmegc-J8vhMFxUWGfKCrRvyuxtQ0LlHa_WyF8QG0YJKHREN8Iu3IgjpXR-G47iPWYektzEloJCKHiaXY3bfLSOmSCZpV2yBWiHCcM1SCw28eIOt_W7PXHAzdOBlGgC8ttdu-D9-D3OGL2bLDXgbveQFrW7m0KpxVcFtVncyjNKlbCQUyry3aytC9kliOdm3l05Z1zHar_OhvHtDVpCpowCF5zy79RJipWkaPR7DgnIwU2udgnLJgjLVOSk2yHfd3_KgOX24evmx7y-mUz1IlfRseTBD6w83I5Uq5dyWpG-KDxiccrsq1oDd7JEepSqKMK6XTZY2Hag6jtRuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در جاده‌هایی که از دل پارک‌ ملی‌ها می‌گذرد، با احتیاط رانندگی کنید
🥲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/683627" target="_blank">📅 12:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683623">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
مصرف خانگی گوشت بوفالو مجاز است
مدیرکل دامپزشکی استان تهران:
🔹
گوشت بوفالو از هند وارد می‌شود و کشتار آن در مبدأ تحت نظارت‌های شرعی و بهداشتی انجام می‌گیرد. این گوشت تا سال گذشته عمدتاً برای مصارف صنعتی مانند تولید سوسیس و کالباس استفاده می‌شد.
🔹
سازمان دامپزشکی اکنون مصرف خانگی گوشت بوفالو را مجاز اعلام کرده است؛ با این حال، واحدهای عرضه‌کننده حق ندارند آن را با عنوان گوشت گاو به مردم بفروشند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/683623" target="_blank">📅 12:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683621">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZZ2XxylsVQyPRIhxGdCWdbrYo3aBBYBOHmp8ps6NBmYomZdjKSnmm4p7XWn6NDrbEvxWKBgAm3QUqF-sxBD3UIAImIytjRxcMQ2GmJFOnmmtQba4Vaaiyt6uJoXe8zKFitKL5dZ9qgZGn1jiJdRPEIbwgP_IyHdKRtQRNPd2n_Whe3c0Y08X3x1jfMscnT0npjA-lyi_uEyvWWCDvpxp9N9hAmhgSMAbbk99YrzqQX6K_SXT7MHMnV3hzD6CHRQZzdcn0sBQzu-JGdHrppxDHaza-19GcbK7jd6j2cOHI2BErvsUulbU-Qr7zrQ6Q5z1rhzq0hSLwubTZ1nYTxOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این بیلبوردهای مرموز با تصویر دماوند توی شهر دیده شدن
👀
نه اسم برندی روشونه، نه محصولی معرفی شده.
🔹
فقط یک جمله: «از آنچه دوست داریم، مراقبت می‌کنیم»
🔹
به نظرتون قراره آخر این ماجرا به چی برسیم؟
🤔</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/683621" target="_blank">📅 12:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683620">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTtnwjjFVlPGb56cItXB447h9rN1zFKaeMCvZbEz0UBRr5-EjLxJgifan2SKGG3ibb4WusoHQTxAyEdNi1fL-CUa3xyRHZa56qX2eVeU7efJDIJ2xM4gkHiyTDBTOGhhFOnf3c4XwJzSWHVWTs7vcTiARPnSfNpSa6kMAJZE5Flx2aeog1Wws-B7ZPoMmlnYEaiKXjEZSLJEyNVSoD63-53vHo6Sy4RFA0snM_3djVH8eAFT2G_95JJmJ4bCr1NnGsrzPPkOdg7PXINHlqI_rcj2mvvON1u8epFs30ixYIYqcFH7WJmtOqAoj29gVuPdLkOU6atjKCxLjVBc3g6RCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موبایل؛ ۴ برابر گران‌تر از یک سال قبل شد
🔹
قیمت برخی گوشی‌های پرمخاطب در بازار ایران طی یک سال گذشته تا ۴ برابر افزایش یافته و فشار بیشتری به قدرت خرید مصرف‌کنندگان وارد کرده است.
🔹
افزایش هزینه واردات، نوسانات نرخ ارز و محدودیت عرضه از مهم‌ترین عوامل رشد قیمت موبایل در این دوره عنوان شده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/683620" target="_blank">📅 12:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683619">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
درگیری لفظی در والیبال منجر به قتل جوان ۱۸ ساله اصفهانی شد
رئیس پلیس آگاهی استان اصفهان:
🔹
جوان ۱۸ ساله‌ای در جریان بازی والیبال بر سر مسائل بازی با فردی دیگر درگیر شد و مشاجره لفظی آنها به درگیری فیزیکی انجامید؛ متهم در لحظه‌ای از شدت خشم، صدماتی به او وارد کرد که منجر به فوتش در محل شد.
🔹
متهم پس از حادثه متواری شد، اما مأموران پلیس آگاهی با شناسایی مسیر فرار، او را در شهرستان بویین و میاندشت و پیش از خروج از استان دستگیر و برای طی مراحل قانونی تحویل مرجع قضایی کردند.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/683619" target="_blank">📅 12:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683618">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqPbHCH39IHmONHIMKZ6nKzqFXJPL4PQ7-Qh4K32djenyPUqKU9Y2pktVCd3hjqj1otl5d_lBabOPT6_C-Ntm9zpTkYca5xsIEsA8M9XZOIFujqzZVoDHNwug0poe-qdnj1_D-9jZJoGAaBwaEeZpJLyTBKfcZSFZY_Jbs6QB3hfs624SVt7LxbqYd3yGqHkW8WKyjOHdh6p5sYPX9HBzKVhSIFkNuEX3pJOS9M2BcSsVXTPHglRpkDEmhMA5irxIhz1IJiq7psAs5htVXDVEsc9KYDKdOXMYhnCLxFKt69-3qtO0xzSUjtM7aviSFTuh45LgrLFVoW6mGkbbDmkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از چند تکه پارچه تا یک کسب‌وکار خانگی
🔹
این بار در #چرخ_زندگی رفتیم سراغ یک ایده ساده، کاربردی و کم‌هزینه؛ ساخت و دوخت هدبند و تل‌های پارچه‌ای دست‌ساز.
🔹
با کمی پارچه کشی، نخ و یک چرخ خیاطی می‌شود هدبندهایی زیبا و رنگارنگ ساخت و با فروش آن‌ها، قدم اول یک…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/683618" target="_blank">📅 12:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683617">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
همسر، همکار یا یکی از نزدیکانت همیشه بهت شک می‌کنه؟ شاید این ویدیو دلیلش رو برات روشن کنه… #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/683617" target="_blank">📅 12:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683616">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره تخصصی اتاق تهران برای موفقیت در تجارت بین‌الملل
🔺
معاونت امور بین‌الملل و توسعه تجارت اتاق تهران با ارائه مشاوره تخصصی مالی و بانکی بین‌الملل، به فعالان اقتصادی در کاهش ریسک‌های ارزی و اعتباری و تسهیل تجارت خارجی کمک می‌کند.
👈🏻
88725269| واتساپ: 09102669714 |
service.tccim.ir/intl</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/683616" target="_blank">📅 12:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683615">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس مرکز امور زنان و خانواده وزارت کشور: کاندیداهای زن را فقط به خاطر یک عکس بی‌حجاب رد صلاحیت می‌کنند ولی یک آقا ممکن است هزار کار کرده باشد و بگویند دیده نشده است
پروین داد اندیش، مشاور وزیر و رییس مرکز امور زنان و خانواده وزارت کشور در
#گفتگو
با خبرفوری:
🔹
۶۱ درصد زنان ما تحصیل کرده هستند و ۷ تا ۸ درصد آنها در شوراهای شهر و روستاها حضور دارند.
🔹
۱۰۰ بخشدار و ۲۵ فرماندار زن داریم. خیلی از آنها وقتی در جایگاه قرار می‌گیرند از مردان (نسبت به مسائل زنان ) سختگیرتر می‌شوند درحالیکه خانم‌ها این پست را به آنها داده‌اند.
🔹
یکی از پیشنهادات ما این بود در هیئت نظارت، خانم ها نیز باید حضور داشته باشند چون یک عکس بدحجاب پیدا می‌کنند و راحت خانم رد صلاحیت می‌شود.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/683615" target="_blank">📅 12:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683610">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
باج‌گیری از مدیران پتروشیمی و فولادی؛ حساب ۱۶ عضو باند مسدود شد
رئیس پلیس امنیت اقتصادی:
🔹
حساب بانکی ۱۶ عضو یک شبکه باج‌گیر مسدود و نزدیک به هزار میلیارد تومان از اموالشان توقیف شد.
🔹
۱۹ نفر ممنوع‌الخروج و ممنوع‌المعامله و ۳ مجوز رسانه‌ای مرتبط با این افراد نیز تعلیق شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/683610" target="_blank">📅 11:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683609">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dd21d1a4a.mp4?token=AHQDnvuTm1lqBNcZAFstdazAtwh_XCooceo7z-FUWktefjScA7FB6xnq9HpP6SfqcKE5LP8ZaUR2SeDEX4Lm6fogVJ-k3SpWCVOW_-vLnAk-ixFmy3DLLx6yOo6FvvTnDZi01z3wV4ayQ_vLSyAYFC7I3iJmtgDDuiUL-n7hnnvIC2_skakAkVyrgT-ope_LKIXN_Uil0uIL-h_Lw3VxffVXlrKSiybN-0355O28U9ewqd7LZpiDs4Eoc6xDVNldBRsgdpn6LSKv6rkRsoSh7ABLrpYvdqYQYDABoy_Co5z8_HROaiSTzJb7H29wZxmzIi6p_4NurL2XFvNns8IbRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dd21d1a4a.mp4?token=AHQDnvuTm1lqBNcZAFstdazAtwh_XCooceo7z-FUWktefjScA7FB6xnq9HpP6SfqcKE5LP8ZaUR2SeDEX4Lm6fogVJ-k3SpWCVOW_-vLnAk-ixFmy3DLLx6yOo6FvvTnDZi01z3wV4ayQ_vLSyAYFC7I3iJmtgDDuiUL-n7hnnvIC2_skakAkVyrgT-ope_LKIXN_Uil0uIL-h_Lw3VxffVXlrKSiybN-0355O28U9ewqd7LZpiDs4Eoc6xDVNldBRsgdpn6LSKv6rkRsoSh7ABLrpYvdqYQYDABoy_Co5z8_HROaiSTzJb7H29wZxmzIi6p_4NurL2XFvNns8IbRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
روایت مخاطبان خبرفوری از کسب‌وکارهای خانگی؛ تلاش‌هایی ساده اما اثرگذار برای ساختن آینده‌ای بهتر.
🔸
یک پیام صوتی حداکثر ۳۰ ثانیه‌ای شامل نام، شهر، نحوه شروع و نتیجه کسب‌وکارتان، به‌همراه عکس کسب‌وکار برای ما ارسال کنید. روایت‌های برتر فرصت معرفی و تبلیغ در خبرفوری و کانال‌های زیرمجموعه را خواهند داشت
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/683609" target="_blank">📅 11:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683605">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHDTNfDx8rXQpw6ovCvN9s0AxjvS4hxFxIJ0JGbtzgVxw7SIjmZK2-sP36Eoqc5sichoshotkbTkahJyZ7ZZj4PCnkPpZtIZ3Sdg8bFTQQfzD-LVLxlgeBlQYUuFrnudvVPbTFTpQK8cHymF6cc9g_bmwwF8Mn6HJtuOSzkG7F5x_2-EDt4AOpRF1BmvkeGHrlDlse4mgjPcksHAJ8vzguW9PK28cU9SvNCA0aNlvCf3aJroqZM5pDVe72eKJlGw6p-7B-UTegxujBn_iYRhnCyHVZ7iA2_j6T9By-MPdCltDXJ29jEvf-5iooM88K2I0JndQqtjQzi3QPKpA_Rc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکذیب مشاهده دایناسور در خراسان رضوی
🔹
اداره کل محیط زیست خراسان رضوی در پی انتشار تصاویری در شبکه‌های اجتماعی مبنی بر مشاهده یک دایناسور در این استان، وجود این گونه را تکذیب کرد./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/683605" target="_blank">📅 11:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683602">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IcmknEYQIKAI-g3RCifX5y-qyuT3PmKQ9yDPALOkoIzc7qUhkIXKJ9BnbPLGfB29zR41mwXyQiulWheQsrOKiuqtI7wXf688OeTTk8vlEFaWvASY2Rq8Sp0xIb5dTGeDum8vEcDgFTVBJHzPuEBP4syETBmHkNuXGk1MWehm19BwnJuoFj2iEQyEZZBO5WZBpTNgaAt0l-41e1fKm2esS9U7sZo0SYRD3srsgYDis2qVyXOo9k6-DTACMY_Jnk_buz2xMx65Po3Zt5CUDTEFJzmJoZ_kV6mIaLPpuy2YVid95CUzLhWaBNDERBIuAFUf3IGqVnvu8LE7Q7bdiTQakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ni40k2zFwJOt0W2aHsXU9_u9cTtYVgdYKu1CkikmQ_ULAvIJybm1FGA706A7uMB_44x9lQN5cSEC4ijb59xN-v8h3Zazf6_cYvGZUwib5z7E6Lq-83uU1_xipGuS1Jdyv1wfrqATawFtpapZxjCpohzQVwiky22KxykCIkXdjbppwqFzl3JVA-bOKAzL3gjK4zBHpB7lIRwohxofcYbZEPSGjlnLiZBiUaeH9uX6-7cj5dfvMghzpqH9IvW2jNUGU36JWd-Y43Qr2hh_c7r78zwFb9aUN7pmLCuWOragyFfZD4zEEj2APQQLfJzwb5zW7Pk2cyFCFuJgKKHmJ1jXTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad448831b7.mp4?token=IcIebRx0NuNHeLeP6G-wicX3mNJVwKkwRzaqJ0iccp2InDuXLTpqP3KgOe8gp3I6rKCmySJpTgnMmLgR_rOk3I6yZskGcROYoRq4qFKlUjPVo9JB6AXXsMxj5dlddQFYULvi13BiDFdn2-GkxYJCsuqysB7_S0gnY-VAZFbgw05G4vNQHOxGGb45Ynob9vlT_obXs5qbRqA0RwwUSdqdRM9S73rFSukWXpkZN9XJijYrNyxPhfO7X1zGpiVCUABnXxDKC6n45_Ee3ukOjUFm39DXA0bL_mM9z8-eCaBIVFawGVg9PJNrOtdGlVMXKJnnfYvJzZ9uH8Q0hiJOGxXtcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad448831b7.mp4?token=IcIebRx0NuNHeLeP6G-wicX3mNJVwKkwRzaqJ0iccp2InDuXLTpqP3KgOe8gp3I6rKCmySJpTgnMmLgR_rOk3I6yZskGcROYoRq4qFKlUjPVo9JB6AXXsMxj5dlddQFYULvi13BiDFdn2-GkxYJCsuqysB7_S0gnY-VAZFbgw05G4vNQHOxGGb45Ynob9vlT_obXs5qbRqA0RwwUSdqdRM9S73rFSukWXpkZN9XJijYrNyxPhfO7X1zGpiVCUABnXxDKC6n45_Ee3ukOjUFm39DXA0bL_mM9z8-eCaBIVFawGVg9PJNrOtdGlVMXKJnnfYvJzZ9uH8Q0hiJOGxXtcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از خمیر ساده تا یک کسب‌وکار خانگی
🔹
با کمی خمیر، چند ابزار ساده و چاشنی خلاقیت می‌شود عروسک‌هایی زیبا و خاص ساخت و از دل یک هنر کوچک، قدم اول یک کسب‌وکار خانگی را برداشت. #چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/683602" target="_blank">📅 11:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683597">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c317f9e52.mp4?token=v7taiqHWRxp07ftPkxwyPuFhDO4J-_X-7COfUiCoaUULPHtdcPxZZDsofHQbDW4Hcj5fuXImV-jfGRU3QFuk2Pqmb_UQ6QieS0MxpixxFzPfNp8FZOHMeMcq19qtJDt36gAiIcXCn5m7x7KfMqTDORn__rhBYd8PqbyFY8dxhKXz4TnboEv-LQARO6k9uK8jh3f_LbQ_vrPQ4GaHAXTXKRF9HXvvRUfhArq4VKh-RNyblqQVcTTqUg35PFPOrso8dfmlMHbyFbhQJf1-xJ93NqKJxdejk7L0-_J0TFqY8n2iuAozLdKcfJS3W6fCdHiigFIdpLsgfjcpK_0Bay-jtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c317f9e52.mp4?token=v7taiqHWRxp07ftPkxwyPuFhDO4J-_X-7COfUiCoaUULPHtdcPxZZDsofHQbDW4Hcj5fuXImV-jfGRU3QFuk2Pqmb_UQ6QieS0MxpixxFzPfNp8FZOHMeMcq19qtJDt36gAiIcXCn5m7x7KfMqTDORn__rhBYd8PqbyFY8dxhKXz4TnboEv-LQARO6k9uK8jh3f_LbQ_vrPQ4GaHAXTXKRF9HXvvRUfhArq4VKh-RNyblqQVcTTqUg35PFPOrso8dfmlMHbyFbhQJf1-xJ93NqKJxdejk7L0-_J0TFqY8n2iuAozLdKcfJS3W6fCdHiigFIdpLsgfjcpK_0Bay-jtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قولنج می‌شکنیم، اما این صدا دقیقاً از کجاست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/683597" target="_blank">📅 11:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683596">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2Emmi9QHOoQXeF44iXx1QgumpKuJnwNPOruT02UJ2BUqtT0zNuhnO-b3lkt3jf6Ms9r8Amx-IEhbDqUy7WOqgSeSEK1szh3ePvQ_Bqhmc7esILGvwNIl_0xVUSYs_A0n7OnAzSwKLxLMV44zkFiWTjcaKXbPZkoMJS6QI8xgUGCTv4fQWg_7TPpZI1qrgtaWu-ILT3h5H9LRd0yoaI-zHygmrGOYThYYvXCyEO52zk6vbOAvdIwT1gq2AJshNXhvgOhO_TvR7oZx0qNJeDyJ6KylRfvh_Tv4yAbQdyMWvbUYytqjNXhbBwY3m0nMpR9g7sbpV7fQyxL7fBD15K50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰ دوره آموزشی مکتب‌خونه رایگان شد.
🔹
مکتب‌خونه در ادامه طرح‌های حمایتی خود برای گسترش دسترسی کاربران به آموزش، در طرح «ایران‌ماهر» ۵۰۰ دوره آموزشی را تا ۸ شهریور رایگان کرده است.
🔹
این طرح فرصتی فراهم می‌کند تا افراد بدون دغدغه مالی، مهارت مورد نیازشان را برای ورود به بازار کار، پیشرفت شغلی یا توسعه فردی یاد بگیرند.
🔹
دوره‌ها موضوعاتی مثل برنامه‌نویسی، هوش مصنوعی، زبان، مدیریت، بازاریابی، مهارت‌های شغلی، مالی و حسابداری و فناوری اطلاعات را پوشش می‌دهند.
برای استفاده از این طرح، کافی است وارد کلیک زیر شوید،  آموزش دلخواه خود را انتخاب کنید و با کد تخفیف IRANMAHER آموزش مورد نظر را با تخفیف ١٠٠% دریافت کنید.
👇
https://mktb.me/k4h1/
https://mktb.me/k4h1/</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/683596" target="_blank">📅 11:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683595">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
عاصم منیر در راه تهران
اسماعیل بقائی سخنگوی وزارت امور خارجه:
🔹
فرمانده ارتش پاکستان برای تقویت همکاری‌های دوجانبه و رایزنی درباره امنیت منطقه دوشنبه به ایران می‌آید
.
🔹
منابع العربیه ادعا کردند: فرمانده ارتش پاکستان، پیام‌های آمریکایی را در جریان سفر خود به ایران خواهد برد.
🔹
این سفر تلاشی برای شکستن بن‌بست و از سرگیری مذاکرات خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/683595" target="_blank">📅 10:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683594">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce468430e.mp4?token=Wk6yApm-zve-zfKq174tqSZvQiYuZ5M8nb9OnM3ZmGT_TtcwDK31TKq-b0u-dpJVa0Pb66c11EVMlV0FbMqS-d8anXieFCTf5QIjq4r5IYShSxbLQlS6zi0JtzOS_cRk9QhOUMt1ptiDvmRMhlp5l7oP8E5Stn5hP9IUEqAtGwB4e5TaPaBBpismn2KgSkf9n8Wr1l1s8_QhQ9uer1TUyTBHgbzYnSRmd4NMjYhdd5Uw_hiW9db6TpoV0Sp2PJQQc6kOrssCRHIw378eHPLBcJXRiKzz7sDlCaCi1K-V76lBvuJYp9wfKSqdj8Sj5gxh8Zw6XfvRzhqa1PcFNz4YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce468430e.mp4?token=Wk6yApm-zve-zfKq174tqSZvQiYuZ5M8nb9OnM3ZmGT_TtcwDK31TKq-b0u-dpJVa0Pb66c11EVMlV0FbMqS-d8anXieFCTf5QIjq4r5IYShSxbLQlS6zi0JtzOS_cRk9QhOUMt1ptiDvmRMhlp5l7oP8E5Stn5hP9IUEqAtGwB4e5TaPaBBpismn2KgSkf9n8Wr1l1s8_QhQ9uer1TUyTBHgbzYnSRmd4NMjYhdd5Uw_hiW9db6TpoV0Sp2PJQQc6kOrssCRHIw378eHPLBcJXRiKzz7sDlCaCi1K-V76lBvuJYp9wfKSqdj8Sj5gxh8Zw6XfvRzhqa1PcFNz4YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسئولیت پذیری اساتید در قبال ایران؛ گمشده دانشگاه های کشور
دکتر جزایی، پژوهشگر دانشگاه سیمون فریزر کانادا:
🔹
«فرد دانشگاهی خودش را جدا از سیستم می‌بیند، اما در تصمیم‌های اساسی نقش دارد و از پذیرش مسئولیت آن‌ها فرار می‌کند؛ من به این وضعیت می‌گویم «دانشگاه بی‌فاعل»/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/683594" target="_blank">📅 10:50 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
