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
<img src="https://cdn4.telesco.pe/file/R-Gx3Mz_-1VjddNgHpdHQYlLi50S90lyzFtJoT9VcsHiidNeojEi7Kja1faHJacZt63hd-dLI-JnWxoG2Q9lTETruhOCxHMEKzyF7WpPHgpU9gQNbSy2FcxtsaYvRRc2xFyojbHkHZLZvJ25l92iYaPrVoBD981nMoYXhtDPmOLXkDX1DzZrbNV9iiK9sosTd5rv2VMSSOk1hkwOhvQdhRg_qE1qQBtKaLXmV0UKeWUeCqrNnVz348Nge5nco1Ait1EdAR4a_LtYvJ5mFyufSUfl8V5iwUIpSgE_BpKAtG3bHyV7Le6IggbrTHNLlKFBVB1XUdr3GBUBp86EMUhAfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 931K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 22:44:58</div>
<hr>

<div class="tg-post" id="msg-131141">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
قالیباف: غنی سازی حق ماست، خط قرمز ما در این حوزه مشخصه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21 · <a href="https://t.me/alonews/131141" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131140">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
قالیباف: بعضا می‌خواهند مدیریت و ترتیبات ایرانی در تنگه هرمز را رعایت نکنند و طبیعتا ایران عکس‌العمل نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16 · <a href="https://t.me/alonews/131140" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131139">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
قالیباف: از روزی که محاصره دریایی برداشته شده تا امروز بیش از ۴۰ میلیون بشکه نفت صادر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/131139" target="_blank">📅 22:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131138">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
قالیباف: در آمریکا روبیو موضوعات را یک‌جور دنبال می‌کند و ونس هم جور دیگر دنبال می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/131138" target="_blank">📅 22:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131137">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
قالیباف: وقتی می‌توانیم گره‌ای را با دست باز کنیم آیا ضرورتی وجود دارد که آن را با دندان باز کنیم؟
🔴
بعد از سفر ما به سوییس حجم آتش‌ها و درگیری‌ها  در لبنان سیر نزولی داشته است. البته هنوز اشکالاتی وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/131137" target="_blank">📅 22:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131136">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
قالیباف: الان هیچ مذاکره ای نداریم. سفر به سوئیس هم برای گفت و گو درباره اجرای بندهای ۵ گانه بود. در گفت و گوها ما نتایج مذاکرات قبلی را پیگیری می کنیم تا محقق شود.
🔴
پس از امضای یادداشت تفاهم اسرائیل تهاجم سنگینی به لبنان داشت و به دنبال اشغال برخی نقاط مهم بود تا تفاهم با مشکل مواجه شود.
🔴
این اتفاقات باعث شد به سوئیس برویم و در آنجا موضوع اصلی که پیگیری کردیم آتش بس لبنان بود. بعد از این پیگیری ها، حجم حملات به لبنان قابل مقایسه با قبل از آن نیست.
🔴
یک کمیته مشترک بین ایران، آمریکا و لبنان ایجاد می شود تا حاکمیت ملی لبنان را محقق کند، سفیر کشورمان نیز نماینده ما در این کمیته است.
🔴
این که تلویزیون تحولات لبنان را برجسته می کند خوب است اما گاهی به این موضوع هم اشاره کند که شرایط لبنان چطور بود و الان چطور شده است
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد. کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/131136" target="_blank">📅 22:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131135">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
قالیباف: آمریکا در یادداشت تفاهم متضمن شده که در لبنان جنگ پایان یابد و لبنان بر سرزمینش حاکمیت داشته باشد و ما دنبال اجرای قطعی این موضوع هستیم.
🔴
نسبت به اجرای تفاهم‌نامه مصریم
🔴
ما هم درحال گفت‌وگو هستیم و هم اگر تفاهم را اجرا نکنند آماده جنگ هستیم و عکس‌العمل نشان می‌دهیم.
🔴
ما در سرزمین خود کمتر درگیر آن هستیم. تنش‌های ما گاهی، همان‌طور که دیده‌اید، شب‌ها اتفاقاتی رخ می‌دهد
🔴
گاهی می‌خواهند عبور و مرور در تنگه هرمز را با ترتیبات ایران نپذیرند و اقداماتی خارج از توافق انجام دهند.
🔴
طبیعتاً جمهوری اسلامی متعهد است که عبور و مرور در تنگه هرمز حتماً در راستای آن تفاهم‌نامه انجام شود.
🔴
اتفاقاتی که این شب‌ها در خلیج فارس رخ می‌دهد را نقض تفاهم پایان جنگ می‌دانیم و حتماً به آن عکس‌العمل نشان می‌دهیم. در آخرین نقض آتش‌بس، مقرهای آمریکا در بحرین و کویت هدف قرار گرفتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/131135" target="_blank">📅 22:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131134">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
قالیباف: محاصره دریایی خودش جنگی غیرقابل وصف بود که با تفاهم برداشته شد./ما داریم دوران گفت‌وگو را دنبال می‌کنیم برای تحقق ماده ۱۳ یادداشت تفاهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/131134" target="_blank">📅 22:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131133">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaxnJAB2AyJk4YIqf4ARI3Z9etV2Ab-woro2vBarVcvYe_yRpjfVldqjvFm5XSVQPiN8t6fQe5fFIPfc8GKkkiURjwMPQcxnTGogbZw0mWLAYCshNuGqhqEgui0wnlChioNb0_qLWbOJ-HRFk2LKnUZdlg2tkdyr5fnx9LNR6K9vBSXMGw_ksWKrBl0sIFNd49LbssMdHJCGIkFZjKEmMxklzwE-6TjdUH63g0L1mCRaxJvf5YDO-_g4bfCfriBbUphmI7WlotnUQZfopHpSjGwAPm0utVzQo9-7n49DFKqv7R0S-Wcaa2T2AgeQkO-cgRa-YHH4U39332t8_IxzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ عراقچی به سخنان وزیر امنیت داخلی آمریکا: به جهانیان ثابت کردید که شایستگی میزبانی یک تورنمنت بین‌المللی را ندارید!
🔴
مارک‌وین مولین، وزیر امنیت داخلی آمریکا، در واکنش به حذف تیم ملی ایران از جام جهانی ۲۰۲۶ مدعی شد که پس از قطعی شدن این نتیجه «از خوشحالی رقصیده است».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131133" target="_blank">📅 21:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131132">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: ارزیابی ارتش اسرائیل این است که حماس از نظر انسانی و لجستیکی برای نبرد بعدی در نوار غزه آماده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131132" target="_blank">📅 21:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131131">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
دولت ونزوئلا : تعداد کشته‌‌های زلزله به "۱٬۹۴۳" نفر رسیده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131131" target="_blank">📅 21:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131130">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ9CvICBO13ea9AQsw_CKCRofPGEf-mkis_BhSr3EUvlIo5V5YFv2T33WB3oRIg7tVvqedWzthbjxN7D7pkUTn0aYF_Ot7te_N3Vuk-nedYak9fHkAY2f1sT4v86cstX25oxkHU8GU9UbfQomFRQnXaW-em9ViFa0QLckbSrkWcY4roXx8I8ujyebAvU6THsdPI_X-FnvRgu8BQDJy3537Z_xocDd4JG-Br4DrvlgaDjCRq9BZ7a8uvmerC-c6JkoWe_EUrJg_OLPC0h1XYy_lpggwc4o8HwHFaA3POe4D1EPN3BNFGzeTumKGf2NY4CAFh_1w2MeD6pmOqmgAvnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طعنه ترامپ  به چینی ها بعد از رای دیوان عالی کشور: من می‌خواهم رئیس‌جمهور شی و کشور بزرگ چین را به خاطر پیروزی بزرگ آن‌ها در تابعیت تولد تبریک بگویم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131130" target="_blank">📅 21:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131129">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
تانکر ترکرز: ایران از زمان رفع تحریم‌های آمریکا، ۵۰ میلیون بشکه نفت صادر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131129" target="_blank">📅 21:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131128">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سی‌ان‌ان: با تعلیق موقت عملیات در تنگه هرمز، تا کنون حدود ۲۵۰۰ دریانورد از تنگه تخلیه شده‌اند و بیش از ۸۵۰۰ نفر همچنان در تنگه سرگردان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131128" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131127">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXIyJuFkqmMsQZ5NVt-N4hYHU8AdHvaFz7oIW4xC7aduBX65pP4bRo2WbyMWZeO0RAqj7HA0MNjIiOXv5pvlbFLtWPeGWFlQAJOFsEoqTVPJVZ7B3isr-YEj0-VcTupS_S-dkCzO_EPTWmlytpewTPXxptAaalJNdu2K_YYQPIQqLn5v2LSwl2TvSQdacPV3opKPFGapaffuJYETO_vVS-b4XDXmej77pm6tLLyeCy5iLiaE51hbi1FU8AX83Vn84mCfRGH2jH5uN-kScNHPXDlRSaX-3-NR2W_7HBuBG43eDsyeD3rxscQjzsxuHGrw7e6rNBwzfFoF0cHbdecn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت‌های 6 سال پیش یه رستوران شمال تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131127" target="_blank">📅 21:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131126">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
پرتاب موشک کروز Kh-59/69 از جنگنده-بمب‌افکن سوخو-34 به سمت اودسا، اوکراین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131126" target="_blank">📅 21:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131125">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
بلومبرگ: پاکستان پس از اختلال در صادرات قطر که این کشور را با کمبود فوری عرضه مواجه کرد، یک محموله اضطراری LNG خریداری کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131125" target="_blank">📅 21:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131124">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
صدا و سیما: استعفای وزیر نفت تکذیب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/131124" target="_blank">📅 20:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131123">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: برای ازسرگیری تردد در هرمز منتظر اجازه ایران هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131123" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131122">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
در پی شکایت ایران‌ خودرو، تردد خودروهای پلاک منطقه آزاد انزلی در خارج از محدوده تعیین‌ شده، لغو شد
🔴
تفاهم‌نامه‌ای که به امضای ۵ استاندار رسیده بود، با یک شکایت و یک ابلاغیه، به تاریخ پیوست؛ حالا پلاک انزلی در جاده‌های همجوار، «خارج از محدوده» محسوب می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131122" target="_blank">📅 20:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131121">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بر اساس اعلام رئیس کارگروه آرد و نان اتاق اصناف کلیه نانوایی‌های بربری و سنگک مناطق ۱ تا ۳ تهران آزادپز شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131121" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131120">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f337fc8f1.mp4?token=YGW9KX6xyNKhEzFL0XXf1cX8p3Ho9Zp_ezaMtSZ7WINEUWdovrLYpmEaJVIwARcG5xVVm9LCJ-sIWP9Tt_fvjpXk8OqmG_Obt65JyvLP3NFNHAhIp1eliEu7V7Jeuvqj8dPxbcq3D1KRoIqyIsq8UVB4RvG1NPTYi24d900F_j-CiSptzkQF455CHt8XeVdnUHemw6lz9Foq5JS9rtDotwt7DoOXoo_WuJ_T1Y60ZA0ty1U30RRGlZGqZnbIw6Nn9W4sc2IUQGlyEF1TVsm2vzC-ei1aO0CjtLxiOInYD8dEl9A0srLNkGR65EgMv3aTJO8lV2RaBnyGXX3WeVbdnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f337fc8f1.mp4?token=YGW9KX6xyNKhEzFL0XXf1cX8p3Ho9Zp_ezaMtSZ7WINEUWdovrLYpmEaJVIwARcG5xVVm9LCJ-sIWP9Tt_fvjpXk8OqmG_Obt65JyvLP3NFNHAhIp1eliEu7V7Jeuvqj8dPxbcq3D1KRoIqyIsq8UVB4RvG1NPTYi24d900F_j-CiSptzkQF455CHt8XeVdnUHemw6lz9Foq5JS9rtDotwt7DoOXoo_WuJ_T1Y60ZA0ty1U30RRGlZGqZnbIw6Nn9W4sc2IUQGlyEF1TVsm2vzC-ei1aO0CjtLxiOInYD8dEl9A0srLNkGR65EgMv3aTJO8lV2RaBnyGXX3WeVbdnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحات سازی روسیه در منطقه ولگوگراد اصابت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131120" target="_blank">📅 20:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131119">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در نشست فردا عمدتاً در مورد دریافت پول‌های بلوکه‌شده و آتش‌بس در لبنان بحث خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131119" target="_blank">📅 20:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131118">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmQw_GrbywlTOnG-Td1QKhr1ha_qGnXZ4BgO-9h--jTFJH5vujl74r_q3khGpzd21kYZEPWPDjHrAV9CoV_KOYC0SkJ3iCPXOlVcImPKOuBs41s__W7bLETrudw1kWPOSvY0pJXxEQ9Pmoeihfuc2c1L6VpV6X6lucKSPx3ZfweGj8mQlDMJcU9F31vspyHzBEAXi9K1nOvYMiEfumshXSZPdKQHMriSMDTyhdMp7ct_EdrVNfly8M9TuOuVANH3u92e8RNAcALtJJ5dfHxEyBeg9oPVc20yaM3nKM41sB1F5Lt7dgxQgowVfbW_QtaS80IuvdFZNjBFhGxzj_Cmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: دیوان عالی کشور حق تابعیت از طریق تولد را تأیید کرد که برای کشور ما بسیار بد است، اما ما می‌توانیم به راحتی آن را از طریق قانون‌گذاری در کنگره جبران کنیم، با حمایت رئیس‌جمهور که اکنون در این فرآیند تعیین شده است.
🔴
هیچ اصلاحیه طولانی و غیرقابل مدیریت در قانون اساسی لازم نیست! کنگره باید از امروز شروع به کار کند برای پایان دادن به حق تابعیت از طریق تولد که پرهزینه و ناعادلانه برای کشور ما است.
🔴
آن‌ها حمایت کامل و مطلق من را خواهند داشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131118" target="_blank">📅 20:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131117">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: با طرف آمریکایی در قطر مذاکره‌ای نداریم
🔴
اعزام هیئت کارشناسی ایران به دوحه در راستای پیگیری اجرای تفاهم‌نامه است و طرف بحث قطر خواهد بود.
🔴
هیئت کارشناسی ایران به ریاست غریب‌آبادی، معاون حقوقی وزارت خارجه اعزام شده است.
🔴
‌ سخنگوی وزارت خارجه: تاکید داریم که توقف جنگ باید محقق شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131117" target="_blank">📅 20:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131116">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
به هر کدوم از بازیکنان تیم ملی فوتبال، حق الزحمه 100میلیارد تومانی پرداخت شده
🔴
قلعه نویی هم 170میلیارد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131116" target="_blank">📅 20:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131115">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtqw0jLcmRd3PF47eYbim4PAYhDhPdYKnx_kOTC1rKIROturMDwwPVOL6faqq9Uc2gG29Q37wBj8TIILwLgWRfvBy1KNoB1c4aWhT9fCmQTnoKYRjNzcn28j6qqu3sUu84RxcseM7S973G4_4eA5_m6NDNNZpQkWttRWBC7lDCdtU-t_CwRmtuyoV1prqC26Xr5GqXXWFdMo0QOOosQWagIVDbvR3FYEdsm-DXnRKAVWmP8HdsZvrQY3qvAG7cYjQGGH8y1j6Cds3DtQz8hVYnFq909GD7cWT8BW7dkEYw4gntEHuOAJoqTpWaUhYzkQ7aQtJimGGl4XB0n65YoIxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به هر کدوم از بازیکنان تیم ملی فوتبال، حق الزحمه 100میلیارد تومانی پرداخت شده
🔴
قلعه نویی هم 170میلیارد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131115" target="_blank">📅 20:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131113">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egsfGvL4grXNUxHSq9XAvmTjff-27MgtysKmrTwGlHYEhK5oIps9yACjIObr6ZONR_uBMIm3oE30iDj-Y5g7iSeY1PikC6528tp3BQoWt9lDbmXjbWEu4Vwn3PqLUKUTLjN8hSvTpYbhRKncYCzJdsnfE-xK2_oMYxN00QPFt0Ri73BxUfiAkWCDQSemy5QfLmF8VQRU7LopV-XgWYzS03M9cHQdhGoPw_yF7fjm-sV-Q16kd1XejO48lW5J1h5_i6M6ct7BKzEROwXdl0AljuY56nUHtEsn2qDZPtFQaOTC758tY8viPNgDItOgwYoCikiDzcgberDYQiBQpwdIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BR_7Hii8lRzGp6fs_yZ2aNajOOXWeunB-gcB2nerznr_WgX07CY2BATFJpfV7SHVC-nM1UFBUaSGppFhPZIA7r8TE9Kcz8vONqEIesYIbwecfa2ZXd2y56GIMROjhv6gEnSJADYvhGnmzdlHVEEL_IosctffBVyNghv2y68FspP6FyE6y1Ex0sk5ni3y7GAEckBC8vLASpNIECzOxXOoSEn1DpjGwhoDNeu_20czCbDO_Vy_dR5lFXOx98MR-3Gbs8ct9PMvdw8Hq1PsDmnDHvnERgaqwV1Yld2s7XMY_f-1n3tIDexQD_mjQngsAcXs3PGt1pnSdTGfXvxPEboMrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان امروز پیش از ظهر در مجتمع ریاست جمهوری در آنکارا با رئیس سیاست خارجی اتحادیه اروپا کایا کالاس و هیئت همراهش دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131113" target="_blank">📅 19:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131112">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
بر اساس مصوبه شورای‌عالی بورس و اوراق بهادار و در اجرای تصمیم هیئت دولت درباره تعطیلات سه‌روزه ابتدای هفته آینده، بازار سرمایه ایران در روزهای ۱۳، ۱۴ و ۱۵ تیرماه فعالیتی نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131112" target="_blank">📅 19:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131111">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رئیس پارلمان عراق: پارلمان، دولت و وزارت خارجه عراق با هرگونه حمله از اراضی عراق به کشورهای همجوار مخالفت کرده‌اند.
🔴
عراق منافع مشترکی با آمریکا و ایران دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131111" target="_blank">📅 19:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131110">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdKCY5EgPZqHZ0P1jjzr_izVZ4BUou2zmwmSKZUhh5Fn1iP_U09fcv9580Ivj-ipx7RkZdsU_5S_Tx7pcOM8dhBSz683gMbR2ieWi-I1wjTzjcBjLGdthOsUD592yaU40UDfgicKfSc2JrxquhqchpkSKAKnUSQ7UoS45uR14NCWsh2gQ5aGQKo4TgXbku3Hy0aruVHEPMbLQUlqx_5gMVTXbQ9c4o_Xh2vyBZtETJp0CpMHlv_S-qwm35HVZZ6xXcEc7bnq0TCX2QAd9Y11xaaOzxGhFvSzvvf0HVGid-yCLsUMudnnqmX7dZfRuzABptE0QE1xDTzNSshNbyncPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، جرد کوشنر و استیو ویتکاف در چارچوب مذاکرات جاری میان ایران و آمریکا وارد دوحه شده‌اند. با این حال، قرار است دیدارها به‌صورت غیرمستقیم برگزار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131110" target="_blank">📅 19:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131109">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=CZ20-7JzBepBTJOxCQQ65uBLoWFrFS8u8VPlmsmekgCjN80zApMm1cNi0hb_qqD3evmhODqJTb1lywH-dimIKl1PbBEF-9PDijG7cc32I6fLRmnjzeMS2FYyKK9zrwIkaIw8FTL4brKrxXAh1IkJnk_3Yi1I6p_X72MMSVui2foJyvXaAqsFJRHtdeRHJ02k-J7GO4uK5zQ8AV2ebGNy8i9auA91tdmKM5InNgrm2RSWfOz35eYmHJqA59g6lsxUkEYwkKUufy_AWkqVbsGOMkUVH40fo1rvp7zOSIAyFLJua-sSMjQGG5qjzpF_-ZU4f2tdqM42EhJzYwP3IkNtOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=CZ20-7JzBepBTJOxCQQ65uBLoWFrFS8u8VPlmsmekgCjN80zApMm1cNi0hb_qqD3evmhODqJTb1lywH-dimIKl1PbBEF-9PDijG7cc32I6fLRmnjzeMS2FYyKK9zrwIkaIw8FTL4brKrxXAh1IkJnk_3Yi1I6p_X72MMSVui2foJyvXaAqsFJRHtdeRHJ02k-J7GO4uK5zQ8AV2ebGNy8i9auA91tdmKM5InNgrm2RSWfOz35eYmHJqA59g6lsxUkEYwkKUufy_AWkqVbsGOMkUVH40fo1rvp7zOSIAyFLJua-sSMjQGG5qjzpF_-ZU4f2tdqM42EhJzYwP3IkNtOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات حق استاد محمود سریع‌القلم، مشاور سابق روحانی:دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.
🔴
مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.
🔴
اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131109" target="_blank">📅 19:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131106">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhfnwumjoWkckZCNrXtDxik893lz2opYjPuCfBIS-RGZFu1erW3TjlEmoBuruX0btTTeiNfa0iBnTGvm0gVIaUhO_iUZS4cN7C80uhxuNR0Px1KDXu-oPrbHUlVwH518COqzMXSMOFoZp-Kj6J5AGA1FGap77e1xRRhZevnePTDG6nC-RUYQEGPobvqZya3Kbi4hIYYkkY4tY2_UB0fdylQoMq5L9GUFtII1N99NylmaeMMbHYSqblhHszu3BqopaF445bztDjeSs86yQBv1UQgWPglUQGV5dCJ17ViDnmW6ZuUSmWZENidw3DJAxL_2We_NDStZyNrcvRv5cGFtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UEtCpFIu5ID1m2sENckPEnnh4rqQzxjU84H9_28QEMcrY3EQiyrNt_yyto9gUA268vgc-baXVfTlT330OwhsL0HZvZIur5bY8d4VVbTY08NXyB3GaxAme1t8vZPmUD4XfjJwSq0l8unwIJ_v29M7ZfGZFSPaGnG87FZoxPZ6I3L7A6BsYFFGWUtWfYbTaWaQg1gKoEfzaDsiOEEe_EBTBVZGvqWoH5kjeH5GSEUc7CJTaTGicMNM8eadD2crfjwgQ3lAHQCaXCSv5CTeKYsIKZLu63sVpBmRbHk95m8dCXM3Z2etMdz8eF7QXIAiScVenjxbe8IGaN3hzXprw6tbug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jEcfFh2PP_ygbrCESG_DhAUTSy3Y7LAB_C5wPR11WKTsbxADKYR7Q77fl7F7WH2cBH0K3uOekpH511r1-uqpjQJCFuC6BGEj-Cru8A4DREbdoFIAcQILWFFYrsMYnyUQ-2sj3T638nJrVGkJXvuxCozZ7XfyIrunh-kkVkoGZA1nU7JgY1bEj4mRadPiy_mkL9hK8LZpxH9aMeXF1KkXoOe03hFIS5M1mKxftdZuLQ2MZFYnA1mRwz2Nr4scg1t_khvBihA4g5J8w069XEaiQjoPchbLEz_jft9LK-UIawXMsknuXjiuVyAaf2E0cD6796xe--VC48CXcb9YY2bEZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سنتکام عکس‌هایی از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131106" target="_blank">📅 19:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131103">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bsbiLntHcFs1r_vLdhGe-1auKQrrLvvMAEvqj9sXSpd8DmIlFfry9B0rDTjny3CW-fkbXXwNvm4m423EFI6wS2XGuLhKsgJ4Sy-gSeCKcLEEa-KBA_UqyHwHcmuyq0zGyfKQXkSYIv2XiFUrxouORGkG-xDbFawqFJ08Kl1Bn3DxPzDynOs7F5GW_kgHqSrrBOq8RYcsM1-iZz9qQvq_eFbVs1DL1sazbNZU9jyRQt50mY0dN0cmirqix2HC4dxaYQGj1UDq6aMFbxlpeIrn7F9QpmiWrSJ0hbq6sdN9gqiNirIoFKai0BH7XmEgCdgUXa71Sh3LF6-dRSwD73IkVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5UPjRpEm9EhvFEgqE_nBsifidbneXpAaWsc09YnFovYZa3UJjeqW2EnKP6mufbt_peKo4iP3MGpg1vRsJ88jnJPvgqNkSUgVNsJob_1g1XbavVimIqoiFJB_cgrgQAf1sOlKQWYVQnMQson1vXss0T7ILq7nmQoJPBLTtUHQio8cQOiEf40z8GhHFlD9lZdhNLiTYygn_Ar2fsvGAgQ63c2O1XVm7IvDjs38DOTq9nYh4eEyNqRm_FzhYf_xTcfvvrwSIQ_kaapIPZeE_-gF27X9WoewogPzmR1TpxIM962tNvjU2NZemlOMw9JjsAMBju4pRZSti7KWP07LCk8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnG99bJ0NfV1lRdqeUOgWN8I-CxPYgkwdKPvfBdsXw95KtzjPOddaK2e80wK4_xBWpVOPKzu9vThU2UzqDmbog7YUoK0Wedr3Q6hMCwZbJxmdYA-kkhn_fMsHAp_AV8TjY4Wa1RueA9acnXMqNYzSSWgv1QeEtav05NQzoBKXiIU4DkyR2dd0SvpXRBgmJLJEZjn7cgp78BKujDvpzoYWY28bCTWLCu0U00vvPx7mxv0UfoAij-Kn4R5t0iL6d2yy-0j8bDvU-Ng23whxejNZf1AdkCzQShEBcXCDUzJv84HE8V_7MuFgLTt123uk_0-fSTvO2SUOwzopHlgCQ0nxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیروهای امنیتی عراق همچنان به منازل نمایندگان عراقی میریزن و کیلو کیلو پول از خونه‌ها درمیاران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131103" target="_blank">📅 19:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131102">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e16fea3ee.mp4?token=mkt12uzz4rX7AX52utdoOSCDq2zeqCgzi136Azvacx41WhPtuaZjngtBwj8A3ereowmsPMiZOTeensScWzyVZkzRL3IrkjrfGcVitZmF0XJmDtxucbRkaNhaVsfsjOHtus-JFknEuZ8q8faqwi0X5AJDaBZ6oGvZenF5_lxV5B-eH-QLUMG_rUsa1VWLKUp98VI20nJFG-vIrNfWmco7ugp3dpsVFcjQWtMW2i-wK93YXPR1XDG_ui0Kxj1XEhEj8x89-uPyY5p0g8Z5tdkFh3UIxxey3n-IpLHWgWcMwH_1IWCY6c5Ii09ev59n5QDPtRBjv3qWENCnPqkN9th2Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e16fea3ee.mp4?token=mkt12uzz4rX7AX52utdoOSCDq2zeqCgzi136Azvacx41WhPtuaZjngtBwj8A3ereowmsPMiZOTeensScWzyVZkzRL3IrkjrfGcVitZmF0XJmDtxucbRkaNhaVsfsjOHtus-JFknEuZ8q8faqwi0X5AJDaBZ6oGvZenF5_lxV5B-eH-QLUMG_rUsa1VWLKUp98VI20nJFG-vIrNfWmco7ugp3dpsVFcjQWtMW2i-wK93YXPR1XDG_ui0Kxj1XEhEj8x89-uPyY5p0g8Z5tdkFh3UIxxey3n-IpLHWgWcMwH_1IWCY6c5Ii09ev59n5QDPtRBjv3qWENCnPqkN9th2Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهد که شهر مجدل زون در جنوب لبنان در اثر اقدامات ارتش اسرائیل تقریبا به طور کامل ویران شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131102" target="_blank">📅 19:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131101">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7XV7lcY1y67kI_Mm4A4wcA5525Ujf2av0Jz4AGKh0wOzRo0Yrzqd1THGse1xhR1RbRx6LCJmGFXcXYGfcLCrxDEfTvJ3L5pzSp3mLifbO-wCuwwwWvI1xG_LmMzJGrilqW_9_hJOCIauFzPgGBxI0gzESZFJLLFyCSTziSFq4X_WPuY5FqytuVRIj-Jy_Bq8puKVyHGbQpDUzmLv3lXkFcbfAhAhmUxNXWjzYVUDM9m7y1oHTfcWQwadcX82v97kZAh_01q-MBHU-2R4T6S4zsteSX_Gwpr1yaAhOr5vZt8FW49-D2Lf4L_OBT3rnewpMJXF6goMQlKTMl2CXKErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل و شین بت اعلام کردند که حمله‌ای اسرائیلی در غزه دیروز محمد فتحی عبدالحی ابو فخر، فرمانده گردان یابنا در تیپ رفح حماس را کشت.
🔴
طبق اعلام نظامی، ابو فخر اخیراً در حال جذب نیروهای جدید و تلاش برای بازسازی توانایی‌های گردان برای حمله به نیروهای اسرائیلی بود.
🔴
ارتش اسرائیل همچنین گفت که او فرمانده‌ای باتجربه در حماس بود که دو دهه به عنوان چهره کلیدی در شبکه قاچاق سلاح گروه فعالیت داشت و بر تلاش‌ها برای وارد کردن سلاح به نوار غزه نظارت می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131101" target="_blank">📅 19:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131100">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا: موسسات مالی وابسته به حزب الله از جمله بنیاد القرض الحسن و مقامات ارشد آن را  به لیست تروریستی افزوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131100" target="_blank">📅 19:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131099">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab2996fef.mp4?token=ILSrXVX5-2qFVKNnHecJUho-6aKny_PrMv5DYUmLlVhuxOhDw3tUYNOcX0h2AJ2_0dk_j-5G5Dz7zeVXHMaMa8TZAwRksCmgdPCEjhFrW_XXCcrqqhQXKzUTB0IuCjvj5fUh0DNsF4GSyk10Q1OofQUb-Lyh2PFfA4tEf8VEZRCq9gmCdXDnrDVKQEB_jVZIMbQ7iYlYWw7AfPz7Z8-2gyt4Er4NDtepAbxxA6OeQC-3HgE8u_IzPj0JrxEj2q4Rzn3aDtCpzIiK8ddRAbT30QuK2Gqcu6Bk8BsFLf91cd2ohlxubfbI7bjcyaYxXZYzNgikAjkv-B7ircbmfHE5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab2996fef.mp4?token=ILSrXVX5-2qFVKNnHecJUho-6aKny_PrMv5DYUmLlVhuxOhDw3tUYNOcX0h2AJ2_0dk_j-5G5Dz7zeVXHMaMa8TZAwRksCmgdPCEjhFrW_XXCcrqqhQXKzUTB0IuCjvj5fUh0DNsF4GSyk10Q1OofQUb-Lyh2PFfA4tEf8VEZRCq9gmCdXDnrDVKQEB_jVZIMbQ7iYlYWw7AfPz7Z8-2gyt4Er4NDtepAbxxA6OeQC-3HgE8u_IzPj0JrxEj2q4Rzn3aDtCpzIiK8ddRAbT30QuK2Gqcu6Bk8BsFLf91cd2ohlxubfbI7bjcyaYxXZYzNgikAjkv-B7ircbmfHE5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اصابت 6 بمب FAB-250 و FAB-500 شلیک شده توسط جنگنده‌های روسی به سمت مواضع ارتش اوکراین در جبهه خارکف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131099" target="_blank">📅 19:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131098">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
وزیر امور خارجه عراق: ما مخالف گسترش جنگ هستیم و هدف قرار دادن کشورهای خلیج فارس را رد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131098" target="_blank">📅 19:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131097">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نتانیاهو: لبنان اسرائیل را به رسمیت میشناسد و اسرائیل نیز لبنان را به رسمیت میشناسد، به ایران و حزب‌الله میگوییم از اینجا خارج شوید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131097" target="_blank">📅 19:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131096">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzCC9uqf_c7xOu2ZeC6BO1DFy33B9tQIf-HNM92MtIY1emIT5kaBR2xeNAUCW1uR2cOw5pJzt9ZM8lP4wdwS0w4Ltg2gkoro2a1QcGbiSHSCkA1QXyn8g5mM4fBh8K4MzlQ89bkiA3vRTML8rWbF-8jjiSVAiHL1LcCCsaGWtdUy6NwXalL4sVxB-tdjH6DbmXV4VAdfHmmwWxy7vJ55qg5g3L3C6lsZLxDRlsvfQUG4BY3yYBNDs1mRIdvkwxU2TZYOPHjvsHVYKva6cBMPLCZDkKaPfvxmV1rA-fn2TNrAw51xMIdtYPwIo4rQRpgn9gXjTDQa-uliPxp0b12Tmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق تروث سوشال: دیوان عالی کشور همین حالا محدودیت‌های هزینه‌های سیاسی را برداشت! یک پیروزی بزرگ برای جمهوری‌خواهان و، مهم‌تر از آن، برای متمم اول قانون اساسی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131096" target="_blank">📅 19:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131095">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW1kOhMlkpy1WZoMBdSN6RWlB6WFcf4xtttYVcMUL8rgw31EkFvv9JuU8rCnJk7Zx3XZdv59XPlX71Xm0tQRmOr979_OdbOLiamask6xP7GLySFbAvdsOtwdpD-TPvyx4RvXy7LP6B8GSoockPc3Ccx67SAnN4onyJThGBaQrhY_RB6FoYg87w7-pENj3rwY6499D107LMjzzUP4MbBwUMsuaF3ZrcM3qh4_fTi-0_pSRXFfkrMIMRxCcpTSGt6f-j-ctzRsfjej6TN6kKRZlwFgJpCtn-WhGrQZzpweSEFLDu3dPjkq30AYCT8jp7w0mSxZgrx654ymVVXFyvp-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوان عالی ایالات متحده حکم داده است که ایالت‌ها اکنون می‌توانند از حضور دختران و زنان ترنس‌جندر در ورزش‌های زنان جلوگیری کنند و احکام دادگاه‌های پایین‌تر را در موارد ایالت‌های آیداهو و وست ویرجینیا نقض می‌کند
🔴
انتظار می‌رود این تصمیم بر قوانین مشابه در حداقل ۲۵ ایالت دیگر تأثیر بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131095" target="_blank">📅 18:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131094">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5XphorDXzBYVtXVzMtqWytEF-8bB0z_XcC8smJoTggPmvCsiSfvS8hDINZjNHA7STWMrtQ6xA1Vundp19ojbusQbTosrf3yxm3LittcYArgfRDR8IhnQM-vnEpUruMOYS24mbGoINATB45i9QLVx7btP6LDQFnu0zE2mP1fRGkrHyOKNG-Lc8sSPZR5KjCALb_0QkmkMN0Pibyuck8ByA35JgLxqqVInQ5J96zpAaxIaYz4Gd7CahKlFI6Sze7DLtOqun3uo-uO5rpXFU4lmL0zR1OTuuXIBBszOVyamSCKusrYZd1QkIuqP6dB4hmSt2nIXCVM3KmkD4i7udGvcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131094" target="_blank">📅 18:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131093">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d0469c5f.mp4?token=cDxaTQUfDTs0doTvaPw2JyyA4iQeLcKbQbXDqghUpOuvbgtLGd4cjV5xQOlSwrZ_zsE9_p9cXIYsawHp8EVMcRWV5eshTAekZnqRt8fj3ceTgyVyw9y-6lhJkI1bqZeAg3D_Q__ix9Ai1u3CMPOx0AOqA02SC5gm8aPXhorC8xEBRVHsal88wiCiNFs5BitCO2w9zFWTTJSd-98WKWb-azUtRX-MuZXplakfjXxbzi8KaE8ZXOWM20gTCj3WgOEAlsofwgjZD-r7fAzb6uqmnoDpQ-sJdCV02FJlUJGEEdBDwSQ1tIG6UqVqYR7jX-XQ49dE4tr378djcy9ksz6XE0fZU4GQSHnPBiSuelnEZFU6Vv8P2uROiZyNxNOcr8SzAv8eCSMymwYByVUIVTa25qqDB8SjkeTtbzZ3extNqJhEof4-03uBIltNdwWnnqLc9R_Y5G7jHk5ZHYaa3ntcTs5spjFBpvQws3GjkT8lvTd1S2Xyh1A_8N0Qvbd8IF01jit61FTfII3qhGDFQ_qQ888zfxHGv09lWHcAg-4H_sOCQYL3k6RhwVm48T0HuRzttf9szIl5rEVq-jn31fdxGBnNKPsauuqZHDahyWFRapnFZkGYMNqFvHVoTfzXVECHYDf61avF1CQBl-AC3hbH3lGO0PAcuw0n_HmxVAb1Z2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d0469c5f.mp4?token=cDxaTQUfDTs0doTvaPw2JyyA4iQeLcKbQbXDqghUpOuvbgtLGd4cjV5xQOlSwrZ_zsE9_p9cXIYsawHp8EVMcRWV5eshTAekZnqRt8fj3ceTgyVyw9y-6lhJkI1bqZeAg3D_Q__ix9Ai1u3CMPOx0AOqA02SC5gm8aPXhorC8xEBRVHsal88wiCiNFs5BitCO2w9zFWTTJSd-98WKWb-azUtRX-MuZXplakfjXxbzi8KaE8ZXOWM20gTCj3WgOEAlsofwgjZD-r7fAzb6uqmnoDpQ-sJdCV02FJlUJGEEdBDwSQ1tIG6UqVqYR7jX-XQ49dE4tr378djcy9ksz6XE0fZU4GQSHnPBiSuelnEZFU6Vv8P2uROiZyNxNOcr8SzAv8eCSMymwYByVUIVTa25qqDB8SjkeTtbzZ3extNqJhEof4-03uBIltNdwWnnqLc9R_Y5G7jHk5ZHYaa3ntcTs5spjFBpvQws3GjkT8lvTd1S2Xyh1A_8N0Qvbd8IF01jit61FTfII3qhGDFQ_qQ888zfxHGv09lWHcAg-4H_sOCQYL3k6RhwVm48T0HuRzttf9szIl5rEVq-jn31fdxGBnNKPsauuqZHDahyWFRapnFZkGYMNqFvHVoTfzXVECHYDf61avF1CQBl-AC3hbH3lGO0PAcuw0n_HmxVAb1Z2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو تو منطقه‌ی حائل لبنان : تا وقتی حزب‌الله اینجاست و ما رو تهدید می‌کنه
🔴
نیروهای ما هم اونجا می‌مونن، به نیروها هم گفتیم هر تهدیدی دیدید، همون لحظه اقدام کنید
🔴
به کاری که با شجاعت انجام دادید افتخار می‌کنیم و بهتون خیلی افتخار داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131093" target="_blank">📅 18:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131092">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
امارات ممنوعیت سفر شهروندانش به لبنان را لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131092" target="_blank">📅 18:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131091">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5133c623.mp4?token=fmuhda9nlGoAqKAt3f8_utKj-6RmZuoTaPx-_Cq6EZybAD86lu4d2Km5v4x_BSsxGDwhTurMt29dpwaNnVzR6CC5OvjY6_4mhI-Xq84mmvVIOS9yXQNaBKl-6neMOhdEto6voeQHO_aTZRL78Hbavo7K5ZYbRrl9QQ9gduAuBPdf4M95wBMPKkwcOXPUCBJQ9dxOPt2D5zQK_Mobi96_Wup7lwOUge4jpIs3Q925U-RaV9gBDg7v6UPNfbDoj5EyYBAB9wh0CjCdpdEpIdu6gFclBh4kt6lO43xlVJiZRC9bu-6_YGfFU3XX98yMxyfa8r0BzZ0Yf-7N8oKsdo42Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5133c623.mp4?token=fmuhda9nlGoAqKAt3f8_utKj-6RmZuoTaPx-_Cq6EZybAD86lu4d2Km5v4x_BSsxGDwhTurMt29dpwaNnVzR6CC5OvjY6_4mhI-Xq84mmvVIOS9yXQNaBKl-6neMOhdEto6voeQHO_aTZRL78Hbavo7K5ZYbRrl9QQ9gduAuBPdf4M95wBMPKkwcOXPUCBJQ9dxOPt2D5zQK_Mobi96_Wup7lwOUge4jpIs3Q925U-RaV9gBDg7v6UPNfbDoj5EyYBAB9wh0CjCdpdEpIdu6gFclBh4kt6lO43xlVJiZRC9bu-6_YGfFU3XX98yMxyfa8r0BzZ0Yf-7N8oKsdo42Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک خودرو در شهر حیفا با صدای انفجاری بسیار قدرتمند منفجر شد که موج آن در سراسر منطقه «کریوت» احساس گردید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131091" target="_blank">📅 18:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131090">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVfZVvXm9Pgu_5nVkVCzyrPrh-KEpPt0tz2-octraEU_eD0ybhl9SxKVQ3pmHhjhphgXjgZZsdtgJHO0q5m69QC2hR0HTHXk0Id5hr9wWZlujXjUmXQ8TvvHPHawjH9C4BEaowOMJ4hlo1L9zRFk19uhN7A2puczgmlSObXmt9YFWjnVVyHGjqji2j15OoCl3FdNYK4oSsCb1J83eydl5wF_UlJw7D7fPfFybs2wUeJuusD1zr-PgfkDpTnQCpXSQ_gu1ySv9zYPkuterNYTTXZ6QsCP516owJYpPz0ntb5yZDpRUbxqX1Wi6FQCcOSnEhNDnjQKLlkdtxjvpSYNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال:
"پیروزی بزرگ: دیوان عالی ایالات متحده همین حالا علیه حضور مردان در ورزش زنان رای داد و این رای، آن وضعیت مضحک را کلاً منتفی میکند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131090" target="_blank">📅 18:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131089">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نیویورک‌تایمز: ایران و عمان، علی‌رغم مخالفت آمریکا، در حال پیشبرد طرحی برای وضع کارمزد خدماتی برای کشتی‌های عبوری از تنگه هرمز هستند
🔴
عمان این طرح را رسماً به واشنگتن و سایر متحدان غربی ارائه کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131089" target="_blank">📅 18:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131088">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f02b732e9.mp4?token=oI7XWnYNUEEC6wu2yrxK61SVIVUMg_g-43OrjTMLNgNpXpqX792QLsa3mxbpfjF_dP1mgDKTn7e-k9zuBOX7k1xevrV1uRXjWQoab-zqWo2AreBsuwAgjMJCxdIQCFqthJjCZN7Or97uwhU8wOcN7UE3gBhJa7G2SSapwP2W6Q6FSgjSYXgavSZ2COECJVZsPPxhl87FyOD_9g-lawS6ksrzRHjgDVQ7_LZKVZJCGz0Wo2TBfZDiSvgG2WsrnaST6fOyd_78QN892bacJwv43HjCwIfMYKBaSElUcH8-Wai68DHy13OpmW7lMljN5ekCNVom_VEQQG8ecfRHap2ed4eyBA8ub1RkRHhdXTzZWB_Ldbnk1Kkhp6rd_rLpF9MLQQqd7HY6_1HpSiGhngHfZAPrTNyf1hsjQ_8az66-lRc1oPeDQdLEByMz-QBMIOCWzSH3oTtpMSRa13wWd6ElZMSjTER-vEGhhEGzM_B9KkwraFFRmgGUiN_rN-K5kVJvJ53WDh2JrfBZ4l79dX7yC_rj9ribgoIg3kin5_WreV7EOW80-Ry9NWh_DhqDO1vSIR8KGnmOY5ZiRpmPU3uKDBq3v8J0v4NFnZp_Z0bjPdkXTXZl8zET8rlPb4PdxZGFqt2L4YKBFuEhwSw7HL55CA5vi7yBJ5Rl-UQ6oRFOBWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f02b732e9.mp4?token=oI7XWnYNUEEC6wu2yrxK61SVIVUMg_g-43OrjTMLNgNpXpqX792QLsa3mxbpfjF_dP1mgDKTn7e-k9zuBOX7k1xevrV1uRXjWQoab-zqWo2AreBsuwAgjMJCxdIQCFqthJjCZN7Or97uwhU8wOcN7UE3gBhJa7G2SSapwP2W6Q6FSgjSYXgavSZ2COECJVZsPPxhl87FyOD_9g-lawS6ksrzRHjgDVQ7_LZKVZJCGz0Wo2TBfZDiSvgG2WsrnaST6fOyd_78QN892bacJwv43HjCwIfMYKBaSElUcH8-Wai68DHy13OpmW7lMljN5ekCNVom_VEQQG8ecfRHap2ed4eyBA8ub1RkRHhdXTzZWB_Ldbnk1Kkhp6rd_rLpF9MLQQqd7HY6_1HpSiGhngHfZAPrTNyf1hsjQ_8az66-lRc1oPeDQdLEByMz-QBMIOCWzSH3oTtpMSRa13wWd6ElZMSjTER-vEGhhEGzM_B9KkwraFFRmgGUiN_rN-K5kVJvJ53WDh2JrfBZ4l79dX7yC_rj9ribgoIg3kin5_WreV7EOW80-Ry9NWh_DhqDO1vSIR8KGnmOY5ZiRpmPU3uKDBq3v8J0v4NFnZp_Z0bjPdkXTXZl8zET8rlPb4PdxZGFqt2L4YKBFuEhwSw7HL55CA5vi7yBJ5Rl-UQ6oRFOBWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوباما در مورد ایران
:
ما تمایل داریم فراموش کنیم که هر جنگی - بار آن بر دوش مردم عادی است، مردمی که فقط سعی در زندگی کردن و مراقبت از خانواده‌هایشان دارند.
و بنابراین اگر بتوانیم از جنگیدن در منطقه جلوگیری کنیم، این برای مردمی که آنجا زندگی می‌کنند خوب است.
اگر تنگه هرمز دوباره باز شود، امیدوارم که به مرور زمان این موضوع به مردم عادی کمی تسکین از قیمت‌های بالای بنزین و قیمت‌های انرژی بدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131088" target="_blank">📅 18:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131087">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18bdf673ab.mp4?token=c_HZfUP0zJqKU1s35bMg0JTNA7D83Ek7O0hmrQhqSTOQRdy9YI-Z1hafABnQffeIomtSUAxYUcthz_2Fc8ElQbduOVegrhpiYA617jex1Oc6xStob9g8F3qsG5c6w1iOLexnyzKo5pCtyyLoRFgR1IrMA6MfnRZyM7HuxTylH-en4AHwPOHR7mSp8I6n-hue7uAQAxhXeYBbL1IkjWY3ubjfUBkMyMFfahvJyBwLR_7vPUtQvF6088d4zx09xR2QhTSZ2aF1aG1qFReu5PUZ7TATG_0Mhzi0hgHTbZl441CXVENgT20kv7_9jw1V8FVONkRkBS4Vek2zamoQiHzf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18bdf673ab.mp4?token=c_HZfUP0zJqKU1s35bMg0JTNA7D83Ek7O0hmrQhqSTOQRdy9YI-Z1hafABnQffeIomtSUAxYUcthz_2Fc8ElQbduOVegrhpiYA617jex1Oc6xStob9g8F3qsG5c6w1iOLexnyzKo5pCtyyLoRFgR1IrMA6MfnRZyM7HuxTylH-en4AHwPOHR7mSp8I6n-hue7uAQAxhXeYBbL1IkjWY3ubjfUBkMyMFfahvJyBwLR_7vPUtQvF6088d4zx09xR2QhTSZ2aF1aG1qFReu5PUZ7TATG_0Mhzi0hgHTbZl441CXVENgT20kv7_9jw1V8FVONkRkBS4Vek2zamoQiHzf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
در طول درگیری ایران، اقتصاد آمریکا به پیشرفت خود ادامه داد. اقتصاد بسیار قوی بوده است.
ما حدود ۱۷۰٬۰۰۰ شغل در ماه ایجاد کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131087" target="_blank">📅 18:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131086">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44dac01f78.mp4?token=J3P6kk8eTZOwyLMKO51YgLxrV6Oq-TOWdSWepwyBASIGMl5UWohvelqwcb0Lr17QlgQStGEE-Ox0IElqP-af3NTf-j5GRlid99WYit6xfc0IL8PeBchhWRO6_ANk8pO0g45yesMQCY1M7dCU6WdailVJkpHg8Wp947Z88UzMiUt0ut4bJ10ZZeaxetX5YZm2RyFsc5_FXq5Eu1phE3PMaPfdvnJxXtVsGHvI2-kxBZIa0yR9v166NbsFuQzDgCcmjSnzAZzUsQkom_RcEakiad7xAnXHMGNeJdb10OFDCSwvKhzgy6X8VF_49JxpLHACtrM8xhDV9FgXa5cj791Ofg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44dac01f78.mp4?token=J3P6kk8eTZOwyLMKO51YgLxrV6Oq-TOWdSWepwyBASIGMl5UWohvelqwcb0Lr17QlgQStGEE-Ox0IElqP-af3NTf-j5GRlid99WYit6xfc0IL8PeBchhWRO6_ANk8pO0g45yesMQCY1M7dCU6WdailVJkpHg8Wp947Z88UzMiUt0ut4bJ10ZZeaxetX5YZm2RyFsc5_FXq5Eu1phE3PMaPfdvnJxXtVsGHvI2-kxBZIa0yR9v166NbsFuQzDgCcmjSnzAZzUsQkom_RcEakiad7xAnXHMGNeJdb10OFDCSwvKhzgy6X8VF_49JxpLHACtrM8xhDV9FgXa5cj791Ofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی:باید طی روزهای آینده روند جاری را ارزیابی بکنیم و بر اساس آن تصمیم بگیریم که به چه شکلی و در چه زمانی مذاکره برای توافق نهایی را شروع بکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131086" target="_blank">📅 17:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131085">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
العربیه: ایران تا پایان هفته 3 میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131085" target="_blank">📅 17:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131084">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi2HnI7MxQke_uFNlYZjO2e1LTO9_b46QdZUZ_cUjwixbG8lbRPsWk3eto1bRIgB64rGVxBo9FCE9ZBEAE71Tq4THnS2FH-9XmUkwGR0f8pdx42LUqQI7WI88yyv54yZIkgupPRWCpj1iSeUF5CokPqjlRDJhTwpVYHjVaT36BVmN64ll7BXqox11i-M47vIC2jUkB73af8F02J4GIjVYPWrUf8KJNM02ct3NHWBlwT7ilZa4rQ7MctTTIk5FJrMbdlBRIPuWJgIb3w3RYKstTRRKMSV25EWaDGqjM0-dm9hsC-daLIe0NZg3y7lSAjHx2dYd8G7h9Y1xoGfTM5qFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مجلس رو باز کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131084" target="_blank">📅 17:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131083">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-3ZW_8LdSzYqvnxUO3tETLph09Z7dfeywzFof9C0sHaQTQtnZrIHXZxO4GLI8SJBcGR6L_0HFXZYCNRcumWV5ripdDlyUkv3JsDqPh5uuHSH_6sqt2LYtJoBMRVXVDAdVUwTSZY7AX2vlPKdrHIp1QptEHwBfcRbxZVu3Dh12muikYQLfBi361mYYYF2RsiNZ4hBt9iRfHGgqKvaheR6xnhv27-LB8-Ps94Rzd4T4tYyH9YBeV9mb90Ls2ZAr2ixH2bBh43oP3xczv0437C41hv9PBxvgsIlQtxlyYZBp_CclJOl_zOo2MKrc3PtQQ9d9X3ACZmACdm-ID2lU9oEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: با وجود معافیت تحریمی کشوری جز چین نفت ایران را نمی خرد و از بازگشت تحریم های ما می ترسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131083" target="_blank">📅 17:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131082">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6KdplXqAbvKIMC2qvcrITUkt1wNk4cqbqv176AJl9B1R_fkfuSvhe-ubBOXjgDaZOmK72S6U7fRIZIxQFzBMxYemxCVaxbZRm8-akXfmkO7M838h939pFR_SBvKJJmRkSowNNtsLaS43Uj83m1SqH8NVUOJx4mrQMeLdF5tjffMLIBSN_bX5vxTuJMuqbie03cIQJwcE2m6wzjXZSVu47SeGB4A1AhiMb30yv2UlwlIZc3cqDCtVOlnIvIv538HRfNenDTYj1wBMLs4w9aEtSeJKCfLjlNzhPbsYV_XUTYgtj2qNw4hAeBkPTF5_FtQcrizwsgkhjcWSZpRBOC9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو مراسم قرعه کشی جام جهانی هر مربی تیم بزرگی با قلعه نویی عکس گرفته تیمش حذف شده (هلند و آلمان) حالا مونده دوتا تیم دیگه که آرژانتین و اسپانیا هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131082" target="_blank">📅 17:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131081">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e51d5a7c.mp4?token=H3M163WwsQa6EBYyMh2QSim1tAaqDiYFGb7QmMh3v2pYZKNTZSo69DcQz5tyQP6MpqscmsHBniwj8rSQ7nvCITqIWYR-eZBZvIAaanhPdEwFeVzw07V-eP188KUTbmKqRS665sp1PGsc9S6NWAWysj8auH-BlQD32mFxHsaziECaYC3nbTZfumyzqFb58zSQ9RE0Ri_33H9e0Qt42Rz7NlesXmJU9yCyqZ3oCmqcfxARXP0j7BjaEGfXZPW3XjKDlDRwGvqt4XCHx-SWF7dDPDEPy-byXSUXH5xYGaPntTdklKMGGdscIBEbOqvdKgrfLtdwRdkx7FKyxZAI-2ZVqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e51d5a7c.mp4?token=H3M163WwsQa6EBYyMh2QSim1tAaqDiYFGb7QmMh3v2pYZKNTZSo69DcQz5tyQP6MpqscmsHBniwj8rSQ7nvCITqIWYR-eZBZvIAaanhPdEwFeVzw07V-eP188KUTbmKqRS665sp1PGsc9S6NWAWysj8auH-BlQD32mFxHsaziECaYC3nbTZfumyzqFb58zSQ9RE0Ri_33H9e0Qt42Rz7NlesXmJU9yCyqZ3oCmqcfxARXP0j7BjaEGfXZPW3XjKDlDRwGvqt4XCHx-SWF7dDPDEPy-byXSUXH5xYGaPntTdklKMGGdscIBEbOqvdKgrfLtdwRdkx7FKyxZAI-2ZVqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توهین زشت حسن آقامیری به شاه عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131081" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131080">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSNHXfAUsbwn4kxwUZ-omjug9G4ZSuGCtAz23wqoJRbaL9GbFVw2mbIYj7d6IKvpQtToFnU2Mq3D5psJ6NcAe6N3Qr3ilTcmUQca0guRIz5GZzKtdxUDYE0bRw_UP5RAg9Bz3TSq250cV-cLeVLqZD5oa9WCIzxcZYeO_XLk3XvAqxeQPuWAfd8a6JC7id2ze1ACcU4aeUPPywI3JCdhuxHwQMzPg1UQXv8fdXMIgkEOwzFDwEeRPI-1FtjXT6dFM9SYq1b_OeuAKr8mz6nvBR9D797NnV6t0IWtCkR1h91W3WU7oRV3QGYWmEiDucspPCfHWYzQA8e9Pyalu56Mig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاچ: نتایج تیم ملی عالی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131080" target="_blank">📅 16:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131079">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa861dd055.mp4?token=boDFwANOWIaUUIUk3RyaN_Ms5PAp_lqct95E8HzUVkfFPWaTuJUwlgc_wUCV5AMeEMh5KoemCREOQ0Y-GzwMb6HGktY6MCGiHZ7Pg-pmTNfGwlqbknnIHCW3iWRZLfQhLqLxpxyyF1B3365lSjovARdHV1yd9Nqyb4Otg88nu_c3lmCzX9eWkmC2vKcIieO6PSsEgiCTC14cq-6q6v4GqSGp9vlZrAKEyIPv0wXmIIkqWR6T7lPqjLz3QdPZJOccq2N7RebzRBUM7DadY8sg1SEP8o-zuS0HHQL7VkTJDzLyfarMLbr4vP4xV8PcwmVbgA3fiRhXogXdezeykFzPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa861dd055.mp4?token=boDFwANOWIaUUIUk3RyaN_Ms5PAp_lqct95E8HzUVkfFPWaTuJUwlgc_wUCV5AMeEMh5KoemCREOQ0Y-GzwMb6HGktY6MCGiHZ7Pg-pmTNfGwlqbknnIHCW3iWRZLfQhLqLxpxyyF1B3365lSjovARdHV1yd9Nqyb4Otg88nu_c3lmCzX9eWkmC2vKcIieO6PSsEgiCTC14cq-6q6v4GqSGp9vlZrAKEyIPv0wXmIIkqWR6T7lPqjLz3QdPZJOccq2N7RebzRBUM7DadY8sg1SEP8o-zuS0HHQL7VkTJDzLyfarMLbr4vP4xV8PcwmVbgA3fiRhXogXdezeykFzPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمسخر کلمه دلیل؟ تجربه، آیت الله خامنه‌ای توسط مشاور قالیباف در آنتن زنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131079" target="_blank">📅 16:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131078">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بقایی: مردم عراق برای حضور در مراسم وداع و تشییع پیکر رهبر شهید در کشورشان لحظه شماری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131078" target="_blank">📅 16:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131077">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
اگه واسه کانالت دنبال
ممبر، سین، ری‌اکشن اتوماتیک و حتی کامنت با هوش مصنوعی
می‌گردی ارزون‌ترین ربات
کلیکو
هستش
قیمت‌ها عالیه:
سین کایی ۵۰۰
ری‌اکشن کایی ۲۵۰۰
ممبر از کایی ۵۰.۰۰۰
⚡
تحویل سریع
💰
قیمت تضمینی
🤖
ثبت سفارش خودکار
👤
پشتیبانی 24 ساعته
لینک ربات
👇
👇
✅
@ClickooBot
🤖
✅
@ClickooBot
🤖</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131077" target="_blank">📅 16:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبرگزاری تسنیم : روز دوشنبه بورس ایران تعطیل میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131076" target="_blank">📅 16:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131075">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c7de37440.mp4?token=rIH7qqm9EShI_jv7BZzPGXlHjoZHKZSVH59i8nOhjfw8ew8IACNAUtfMsTcDiQr1ieie4S5efRhj6ud3VxR8d4zFAnZMoFSMMTvqGkolq0FQflQpn784fVehtvywy8399ofUsb8nv4tl2iSpW5bfUMDxLNnDoIxqXcFa3nDBVp37g9fZnPQEGPy8sw42G8fP9hJpkaETk67poVrRLWMG3nNIro-D10MgwRRfSha8uo_uHEMxHlJCVOklaPkWSpW4dZ2t4DhRefJgnQZwF4kffS3WJQuWUPyfaBvrxwEwhNvSQE97aMMi_4CUw9Jbt1fNp_fktXRhq8jpXZUEHnqF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c7de37440.mp4?token=rIH7qqm9EShI_jv7BZzPGXlHjoZHKZSVH59i8nOhjfw8ew8IACNAUtfMsTcDiQr1ieie4S5efRhj6ud3VxR8d4zFAnZMoFSMMTvqGkolq0FQflQpn784fVehtvywy8399ofUsb8nv4tl2iSpW5bfUMDxLNnDoIxqXcFa3nDBVp37g9fZnPQEGPy8sw42G8fP9hJpkaETk67poVrRLWMG3nNIro-D10MgwRRfSha8uo_uHEMxHlJCVOklaPkWSpW4dZ2t4DhRefJgnQZwF4kffS3WJQuWUPyfaBvrxwEwhNvSQE97aMMi_4CUw9Jbt1fNp_fktXRhq8jpXZUEHnqF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای نظامی اوکراین امروز صبح مرکز ارتباطات ماهواره‌ای دوبنا در منطقه مسکو روسیه را هدف قرار دادند.
🔴
این سایت که بیش از ۵۰۰ کیلومتر از مرز اوکراین فاصله دارد، برای شناسایی و هماهنگی فعالیت‌های نیروهای روسیه در اوکراین استفاده می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131075" target="_blank">📅 16:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131074">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آقای قالیباف به‌عنوان نمایندهٔ ویژهٔ ایران به چین سفر می‌کند و ترکیب هیئت همراه و جزئیات سفر به‌زودی اعلام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131074" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131073">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا به فاکس نیوز: پس از رفع تحریم‌ها، هیچ‌کس به جز چین نفت ایران را نخریده است. ایرانی‌ها نتوانستند نفت خود را به دلیل ترس خریداران بفروشند
🔴
ایران تلاش می‌کند نفت را با قیمت‌های پایین‌تر بفروشد و سود آن اندک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131073" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131072">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd78855cd.mp4?token=YlYQ6ahmq4guhRDC13twtNUsVMoNAjA9acqEhmUjw8P6YjshpTi6j1NHVXteuypc563spk_SMWrz5wWMFavCkj4fWEF08EeQb5QXnAaitlzUL7U0dIZGePR1NFS_YUJn4LFYiP6PWElfI5uZBGSteJzaL6UDfJ43220B3TrDDpeSHsb55N2u5UMiKLBL-ZguZEnaSKVUzkK07igYB8aAPQ6oyeTzkVu2worh4ONigMiNnv4d65zDzo8kckwg-9GlhPAOh8s0LNG5dLA6uI_9O4OhHd8s4LBRGPn8nzLuQI4DI9UBY0LVq3VOTJM6ELxnoIr_uR6P8bTH2MtFarSBRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd78855cd.mp4?token=YlYQ6ahmq4guhRDC13twtNUsVMoNAjA9acqEhmUjw8P6YjshpTi6j1NHVXteuypc563spk_SMWrz5wWMFavCkj4fWEF08EeQb5QXnAaitlzUL7U0dIZGePR1NFS_YUJn4LFYiP6PWElfI5uZBGSteJzaL6UDfJ43220B3TrDDpeSHsb55N2u5UMiKLBL-ZguZEnaSKVUzkK07igYB8aAPQ6oyeTzkVu2worh4ONigMiNnv4d65zDzo8kckwg-9GlhPAOh8s0LNG5dLA6uI_9O4OhHd8s4LBRGPn8nzLuQI4DI9UBY0LVq3VOTJM6ELxnoIr_uR6P8bTH2MtFarSBRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی: ما هیچ درخواست رسمی در خصوص بازگشایی سفارت کانادا دریافت نکرده‌ایم.
🔴
اگر درخواستی دریافت کنیم، آن را بررسی خواهیم کرد، اما تاکنون چیزی دریافت نکرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131072" target="_blank">📅 16:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131071">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3834c581a9.mp4?token=eH5uYC2x3_zsScCCekW6F6XsZ-yC5zphNsGTy7eGRdIvLksxPFN1UQvrc7o2BHEZFyiCEdNom2oYmo8S75-Mo2QWm5KQ1sezatkOlPLh5R4dCVI_MFhcqgOMZy-0cwYQsu-4Hy9OrTrGYu2p2zmf-a8hADrGp3rJtoeE5WXut4bRqZBzZjXfgirbo70tgpQUEXhVQAHrDiyPB4vdVeQvF9AkTQAggq44MxdZ3lWo5_GtnBH4Shaf2xiww4baJvnyBbuhR63p4x-MxAuWGiZI-FPeqwLkM1_G5rF-nZfLxqz7X04LSQjRdzTvy6qkrHCUdQn3Hjysb5z9eua6cRC95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3834c581a9.mp4?token=eH5uYC2x3_zsScCCekW6F6XsZ-yC5zphNsGTy7eGRdIvLksxPFN1UQvrc7o2BHEZFyiCEdNom2oYmo8S75-Mo2QWm5KQ1sezatkOlPLh5R4dCVI_MFhcqgOMZy-0cwYQsu-4Hy9OrTrGYu2p2zmf-a8hADrGp3rJtoeE5WXut4bRqZBzZjXfgirbo70tgpQUEXhVQAHrDiyPB4vdVeQvF9AkTQAggq44MxdZ3lWo5_GtnBH4Shaf2xiww4baJvnyBbuhR63p4x-MxAuWGiZI-FPeqwLkM1_G5rF-nZfLxqz7X04LSQjRdzTvy6qkrHCUdQn3Hjysb5z9eua6cRC95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی: رقص و جشن مقامات آمریکایی به خاطر عدم صعود ایران به مرحله بعدی جام جهانی، تمام استانداردها و هنجارهای پذیرفته شده میزبانی را نقض می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131071" target="_blank">📅 16:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131070">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
در رابطه با تنگه هرمز، تکلیف کاملاً روشن است. بند ۵ یادداشت تفاهم، مسئولیت جمهوری اسلامی ایران را به‌صراحت بیان کرده است.
🔴
بنابراین، روندی است که آغاز شده، تداوم خواهد داشت و قطعاً جمهوری اسلامی ایران به‌خوبی می‌تواند این روند را بدون نیاز به مداخله هر طرف دیگری انجام دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131070" target="_blank">📅 16:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131069">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
قیمت کولر ۳ برابر شد !!
🔴
مهدی بستانچی، رئیس انجمن تولیدکنندگان سیستم‌های تهویه مطبوع ایران: کولر آبی ۷۰۰۰ از حدود ۴۰ تا ۴۵ میلیون تومان آغاز و در برخی مدل‌ها و برندها تا ۸۰ میلیون تومان نیز افزایش پیدا می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131069" target="_blank">📅 16:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131065">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyR6Ik_c1evdBywLEbBCe1VJLya8BRg6LwyWkLzJ-YaIaYChK7hd5obahg3jPt4Z0LT8mQXmi01njK8dxvAA0WeymG8jzd2tVUf0lWhSyZkvcad7lED-enkphC3AFRDjUDT-dBvYeiai9OO-_Ssbm1rlUfM1RqogaLN0NTh1UHmuF8yvm67fmVmc539AzqaAOLgzX-9Xs-GX9ZqIDdOF09fCc6HhEtGexyfOzZvkhHA7GVGquw_-ispTE48Hou34O1eARdu9cBcadI6nI1ME6t5AznkenJdodf9mqg6wAWiUqdqdyXe5OfFV18Kr2AuehYBXFHVE-sLmuihGvI8xjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBzR9UhVCcrpDfiitX1UrMIxXQosVwORnBTfTDZO3pCVBOj-NFz46oFRsN2pPPW20kv2KsyeRz1--4pao-jRUQAKPK9BLn2YvJze3bufGW_QN5cLnIIEQPqHaCflNMIkbBwmBxXZh2ZTJIoQlSF3LUp1Beo85e7Nmux-kzxut6s6Peg5r-37eUgtTO8AuZRZz5sn1JH49iLcqrRLwmXupD8_6S1TFSFoye8RQK2_TUq7gbgLFBd5_lM_T6UoG2oBCM2hK-VbT_8u4T49vBoD3b4lVA7Vx6l8VAtYsz1YwNq9V8AS8hO0VBztf7h0yJwKgNRGJX0lXKSe6bH_GFnDvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lir2vP11d841bmQQb8IYDlEI3pOTeE5kdgc2iEQw4B47xCuNCXqc4P0DQv7hf0IbBoSvDn06oRx9lUcaIZHC0clUkm_G--A8QtN7URk3rpihi1YrUxEUbxTV5tRXpYcrhpbzdUW_f16UB9HkGIk5RFbQbXbFXgXAZoCrAU7SQBsVd7GAPVGNhEdF_kQq5Wi1ll3-r24wXRh_V73_ffeY-H1rFJOEOzSKywG9PCvu4D8Tw7Cw32m124tRkyrpReuZ8ATrE282Wnw8DQ17emVRXmpKBqzgj-rxUTKQdw8gK0BMqhpyoGS7lhgIfB8dscAMAZmmavhbi-z4YQ812AylhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7XSR4LJfWmiyQ34qvEcwwleIW867pI_wIuQHZ2h0MjAIR_T5nfkKfKPMhActMrZ1hAKIilCWVTCUwDyrMPJtvOnPp8xfz5mSzEgtvM08MixdYeY6kchciO7UOCF-nu8BrdtK17Qzg8BTxL2XtjfQtnJQJzbKZmVJPpv6a_jzziXiHMhWkV3Y4mnv-dTO0M4E0JLodOyXIqtE-S1Tk9SPilAu30JjEWD14aCp6n1ZTZxT79h0SauWcNPwtYw1nxfo6bwmQtullRPtSXtlUMC791Dki-uIC9v6_-JWk-O6llD3NxefL2PVRcdOuc3UzG3LqkTr2NBTaFuQvgvr9wuqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در ادامه دستگیری ها در عراق موقع بررسی پرونده معاون وزیر نفت این کشور، ۱۱ میلیون دلار و ۴ میلیارد دینار پول نقد تو خونشِ پیدا شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131065" target="_blank">📅 16:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131064">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7907cf315e.mp4?token=f8JmpQmAUiDwDOEYZSjX3M_v107k-VhmJvJxhfA31AJ35F9GSGn9sl81hOOS5shZoPNGlnlUBpONe6FKZse75hDzR0G84F37UsHrLRVtYkdmTLWGBGe_ZExZwWjysuCzdCXfueIdjWwBMpCXHsrLWYyCGGnnU4x31FbDSg7wDzEm3Beg_i_TEp-SyNc57VEAOdRwqLGzf43apLyd91qoyzcWF6uAoBXFpsy-Fwu_9vVeLMznsFohBq7MiDbLa320o9siAkfia8DY_RjW916iGZEZ5t6Vb15vB80BdcSMmUBNMCoaqqCKI5zFlXMpfY5yUAfPiigbaQ0Vfm7O72-13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7907cf315e.mp4?token=f8JmpQmAUiDwDOEYZSjX3M_v107k-VhmJvJxhfA31AJ35F9GSGn9sl81hOOS5shZoPNGlnlUBpONe6FKZse75hDzR0G84F37UsHrLRVtYkdmTLWGBGe_ZExZwWjysuCzdCXfueIdjWwBMpCXHsrLWYyCGGnnU4x31FbDSg7wDzEm3Beg_i_TEp-SyNc57VEAOdRwqLGzf43apLyd91qoyzcWF6uAoBXFpsy-Fwu_9vVeLMznsFohBq7MiDbLa320o9siAkfia8DY_RjW916iGZEZ5t6Vb15vB80BdcSMmUBNMCoaqqCKI5zFlXMpfY5yUAfPiigbaQ0Vfm7O72-13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی: احتمالاً آنچه فردا در دوحه اتفاق می‌افتد، بحث درباره اجرای بندهای یادداشت تفاهم است، از جمله بندی که مربوط به آزادسازی دارایی‌های مسدود شده ایران با طرف‌های قطری می‌باشد.
🔴
بنابراین، تأکید می‌کنم که هیچ جلسه‌ای در هیچ سطحی با طرف آمریکایی برای چند روز آینده برنامه‌ریزی نشده است
🔴
تمام آمادگی‌های لازم انجام شده است و امیدواریم کار به‌درستی پیش برود و به نتیجه رضایت‌بخشی برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131064" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131063">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucE8R2j3L2Va113IDtwa7UnSh5zoxKESc1Thi9rx8q59omaS6aGe_iH-WkJs6ePfHdI7Ql0DbN5m5eOzXfSA4EBZE75F2eeI74fXBaKOtSbZ08kiZkFWqJs9zJCLtHeTZwCjZBabeyEKOVATz_CBQAuiSv1dJyaBle08JGl3a07WJeLJI9SCr-24V5XFIx75gWpvaysF7T_bqhQpeNMI-NgGxTbPl8A8Vv4TluTW6OG32gvsuMJAjxR0KyobPJnGXHyfB2bcub_RdKIPj0RV8-_cdqV0ZJ9yPUo_rsy12mXcAQnCpqmBv1k8xKgtT3z_ADeENDWYNy3qSsLxwN73Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع العربیه: ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131063" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131062">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
بقایی وزارت امور خارجه ایران: خط ارتباط با واشینگتن میان این وزارتخانه و یکی از نهادهای سیاسی آمریکا است.
🔴
در روزهای آینده در مورد زمان و شکل شروع مذاکرات توافق نهایی تصمیم‌گیری خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131062" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131061">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a081ef12.mp4?token=BcuSDanl8lP6LotLnOw85cX4_XNaMoinLmyhjcT0bZCPy1lz1KJQrYxXwW9njwEuqiafsIPScVsGJuvekSrLYuIobAqowvETAJgIkb9bQje4N5eevyOkxO-NLW2CsD79JfZ01Y8doELrF7Y-U4Xc8b0Brewmn_HfLrO1qnW_UFgNfqJKwq09MI5gdlluW8_bU_VF8vIs6k8hQOiJMaNGMkIZPDrFTwdeCl0R2ShDSRDdeUbVyZBYO5uiF3SkotOEGkjFlPfiOkmvdZANbHjK9Sq_6-B5v_ha6QvOJgOqvdjf-9kwl7imd1L4vTeILCCT-nNUd5s0DOOUkTuBI5_3BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a081ef12.mp4?token=BcuSDanl8lP6LotLnOw85cX4_XNaMoinLmyhjcT0bZCPy1lz1KJQrYxXwW9njwEuqiafsIPScVsGJuvekSrLYuIobAqowvETAJgIkb9bQje4N5eevyOkxO-NLW2CsD79JfZ01Y8doELrF7Y-U4Xc8b0Brewmn_HfLrO1qnW_UFgNfqJKwq09MI5gdlluW8_bU_VF8vIs6k8hQOiJMaNGMkIZPDrFTwdeCl0R2ShDSRDdeUbVyZBYO5uiF3SkotOEGkjFlPfiOkmvdZANbHjK9Sq_6-B5v_ha6QvOJgOqvdjf-9kwl7imd1L4vTeILCCT-nNUd5s0DOOUkTuBI5_3BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: روند فروش نفت و محصولات نفتی ایران خیلی تسهیل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131061" target="_blank">📅 15:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131060">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/ منابع العربیه: مذاکرات غیرمستقیم فردا بین هیئت‌های آمریکایی و ایرانی در قطر با حضور میانجیگران برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131060" target="_blank">📅 15:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131059">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: جنگ با ایران ممکن است هر لحظه شروع بشود و ما برای آن آماده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131059" target="_blank">📅 15:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131058">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بقایی: هیچ درخواست رسمی درخصوص بازگشایی سفارت کانادا دریافت نکرده‌ایم/ در صورت دریافت بررسی خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131058" target="_blank">📅 15:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131057">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
در رابطه با مسئله لبنان، موضع ما روشن است
🔴
تعهد ایالات متحده آمریکا برای خاتمه دادن به جنگ در تمامی جبهه‌ها، از جمله جبهه لبنان، یک تعهد صریح و آشکار است که وفق بند اول یادداشت تفاهم بر آن تأکید شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131057" target="_blank">📅 15:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131056">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131056" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131055">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی:
با قبول کردن آتش بس، به آمریکا فرصت تنفس دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131055" target="_blank">📅 15:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131054">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f440c5937f.mp4?token=W8u-bVXN7P6-3B-gcoB85mZvuHInWYPi9gO23g4M9xr0w3HidowJl5pKJHsZlUu6Gtnrv663pAHm5SemLKmpDlUu6RzM6bzfvC0YEWI9l4xO5Jlt3qO0dISa8KljJDoA8JEKdYfOlwbNDhcRPqH1LVw_vZQTPIrZ5CHTotibZ2uroB_2mjHwYKb0luwHezRn-GT7FqHkAzSGnpzx7RxpdSKK4xhJnU7sfPMreWRtdrhx0-e3V1pvYpdC4yFAqKafnrvnYq09e1R_nAsgRFKKLjst6Z3NZbO0x7hdK7zgS0DoTzRwGGgb1hLFCZjkM1wutIYLTZnuOuEXEbwbkdvRWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f440c5937f.mp4?token=W8u-bVXN7P6-3B-gcoB85mZvuHInWYPi9gO23g4M9xr0w3HidowJl5pKJHsZlUu6Gtnrv663pAHm5SemLKmpDlUu6RzM6bzfvC0YEWI9l4xO5Jlt3qO0dISa8KljJDoA8JEKdYfOlwbNDhcRPqH1LVw_vZQTPIrZ5CHTotibZ2uroB_2mjHwYKb0luwHezRn-GT7FqHkAzSGnpzx7RxpdSKK4xhJnU7sfPMreWRtdrhx0-e3V1pvYpdC4yFAqKafnrvnYq09e1R_nAsgRFKKLjst6Z3NZbO0x7hdK7zgS0DoTzRwGGgb1hLFCZjkM1wutIYLTZnuOuEXEbwbkdvRWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برج ایفل ۱۰ سانتی‌متر بلندتر شد!
🔴
در گرمای شدید، سازه آهنی این برج به ازای هر ۱۰ درجه سانتیگراد افزایش دما، حدود ۲ سانتیمتر منبسط می‌شود. وقتی دما کاهش یابد، ارتفاع آن به حالت عادی بازمی‌گردد.
🔴
تابستان امسال برای این نماد مشهور پاریس روزهای سختی داشته؛ یک روز دمای هوا به ۴۰ درجه می‌رسد و روز دیگر صاعقه به آن برخورد می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131054" target="_blank">📅 15:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131053">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی وزارت خارجهٔ قطر: اموال مسدودشدهٔ ایران آزاد نشده و آزادی آن به پیشرفت مذاکرات ایران و آمریکا بستگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131053" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131052">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60302362c.mp4?token=CVSAObaE0_O_vxiNchfNeV3jL5gaMgUuDsYcNE0EL9VKeK5r9xiOo7y8AZ4zzZlR74t-_rIPD-gxATajU8dxGDnek-4k3yV70Uir0ohAC3OxlfvhG7VGSqECyrmxkEZDH-bw0yLbdjSmsXubry6q9e8sSYZ5PX-TZ-Rjsnesqkc6g43UntrJ9ToKBLD6L1H9c2ba_mm1rgiM3kBDuwhmngiZjT9sqTaHlJOhZnuX4eDehE__HY_brc46bbQ_HBkNlch9LVGh7Vw7YpCcdRQe0xRtjcOBNsiH-kkWdKM1EDwqlZ6XXQu0i-KuxYOXB0xEkubS2rw5Srw5VTA5BuzVBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60302362c.mp4?token=CVSAObaE0_O_vxiNchfNeV3jL5gaMgUuDsYcNE0EL9VKeK5r9xiOo7y8AZ4zzZlR74t-_rIPD-gxATajU8dxGDnek-4k3yV70Uir0ohAC3OxlfvhG7VGSqECyrmxkEZDH-bw0yLbdjSmsXubry6q9e8sSYZ5PX-TZ-Rjsnesqkc6g43UntrJ9ToKBLD6L1H9c2ba_mm1rgiM3kBDuwhmngiZjT9sqTaHlJOhZnuX4eDehE__HY_brc46bbQ_HBkNlch9LVGh7Vw7YpCcdRQe0xRtjcOBNsiH-kkWdKM1EDwqlZ6XXQu0i-KuxYOXB0xEkubS2rw5Srw5VTA5BuzVBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل یک تونل حماس به طول ۱۶ کیلومتر در غزه را با بیش از ۳۰,۰۰۰ متر مکعب بتن مسدود کرد.
🔴
این همان تونلی است که جسد اسرائیلی، سرهنگ هدار گلدین را به مدت بیش از ۱۰ سال در آن نگهداری می‌کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131052" target="_blank">📅 14:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131051">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe136f3fc.mp4?token=IglnOVkLxmZzeUYx00-JGNzcvSX_X027Ms2NIuUE5wbRfLfqoBz8duYAKre8Mt-PtM7rPLUm3E5SnZMPHB-eKucZ_IXUoGqegPZIl1_Fpj2jFQpNb4eNt6TCU7ia0n6KxUrqvR10osQB_UQ1JiF9kjW9V6VreULAEbOTd7-XcsLiXSA95dEwAlGsUSyhoknjPWSQCHNcGGe0BZ9dg5LjB1ZOYgLuqZsPx5LT57xIJ9qk3PBAHu5eHF2JW5Q00qJ9Wx02uT9FlTFalsBOb5hZbIiLZIjAaRO_HyfhyKbw5smWEX8Q31JUDE62Vlgc9DPqA9A7sSsvpO1fin0bjUb7Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe136f3fc.mp4?token=IglnOVkLxmZzeUYx00-JGNzcvSX_X027Ms2NIuUE5wbRfLfqoBz8duYAKre8Mt-PtM7rPLUm3E5SnZMPHB-eKucZ_IXUoGqegPZIl1_Fpj2jFQpNb4eNt6TCU7ia0n6KxUrqvR10osQB_UQ1JiF9kjW9V6VreULAEbOTd7-XcsLiXSA95dEwAlGsUSyhoknjPWSQCHNcGGe0BZ9dg5LjB1ZOYgLuqZsPx5LT57xIJ9qk3PBAHu5eHF2JW5Q00qJ9Wx02uT9FlTFalsBOb5hZbIiLZIjAaRO_HyfhyKbw5smWEX8Q31JUDE62Vlgc9DPqA9A7sSsvpO1fin0bjUb7Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا کیر استارمر:
۶۴ میلیارد پوند برای نوسازی بازدارندگی هسته‌ای بریتانیا سرمایه‌گذاری خواهد شد.
🔴
این پول صرف ساخت زیردریایی‌های جدید، توسعه یک کلاهک جنگی مستقل جدید و خرید ۱۲ فروند جنگنده F-35A خواهد شد تا نقش ما در تضمین امنیت بریتانیا و اروپا حفظ شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131051" target="_blank">📅 14:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131050">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از سخنگوی وزارت امور خارجه قطر: اموال مسدودشده ایران مشمول توافق سال ۲۰۲۳ است و به‌طور مشخص برای خرید کالاهای بشردوستانه اختصاص داده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131050" target="_blank">📅 14:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131049">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر ادعا کرد: جلسات فنی بین واشنگتن و تهران متوقف نشده است و میانجیگران برای تسهیل آنها تلاش می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131049" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131048">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر ارشاد: دیدگاه‌های مطرح شده توسط مراجع عظام، علما و فضلای حوزه علمیه قم در دیدار با رئیس‌جمهور، نشان داد که بخش اصلی و تاثیرگذار نهاد دین از دیپلماسی عقلانی حمایت می‌کند
🔴
در دام تبلیغات جنجال‌سازان قرار نگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131048" target="_blank">📅 14:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131047">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / سخنگوی وزارت خارجه قطر:  ایرانی ها از دیدار با تیم آمریکایی منصرف شدند. ویتکوف و کوشنر در دوحه حضور دارند اما با مقامات ایرانی دیدار نخواهند کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131047" target="_blank">📅 14:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131046">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: ۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
🔴
حاکمیت و سیاست جدید ایران در تنگه هرمز اعمال خواهد شد؛ چه با عمان، چه بدون عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131046" target="_blank">📅 13:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131045">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری / سخنگوی وزارت خارجه قطر:
ایرانی ها از دیدار با تیم آمریکایی منصرف شدند. ویتکوف و کوشنر در دوحه حضور دارند اما با مقامات ایرانی دیدار نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131045" target="_blank">📅 13:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131044">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7204ae52a8.mp4?token=li2w_mI0A4px0kATX78pXFs-WiaxOy49dZATIkRaeA8UcLrP0Wprd2mPxs7HgoC0DdK59DeOXIUBZLbzqIQnvLU6vS4NL8pLadU1BKjolQvsggdVl-TDEc37Tc6kNjDR8n2fCdRrwaq6kiAwYwhX9fOrkCR4ufbcY_d415IHdOIM8RRYK12jQ24y5CgPTnDSa_cXznYungUql_c_YZU_rxvI1of8ot46fLOMokAfVoj-TRDPiM7RwU7LQJHrUpKfXXzz6ofPRYNrmnFboc2Y-bmUPCe_t1_-9Q27JF3oyXoErDqUqb2t3buLKtgE0TMu_6LbO820qDydm5BYOWOr-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7204ae52a8.mp4?token=li2w_mI0A4px0kATX78pXFs-WiaxOy49dZATIkRaeA8UcLrP0Wprd2mPxs7HgoC0DdK59DeOXIUBZLbzqIQnvLU6vS4NL8pLadU1BKjolQvsggdVl-TDEc37Tc6kNjDR8n2fCdRrwaq6kiAwYwhX9fOrkCR4ufbcY_d415IHdOIM8RRYK12jQ24y5CgPTnDSa_cXznYungUql_c_YZU_rxvI1of8ot46fLOMokAfVoj-TRDPiM7RwU7LQJHrUpKfXXzz6ofPRYNrmnFboc2Y-bmUPCe_t1_-9Q27JF3oyXoErDqUqb2t3buLKtgE0TMu_6LbO820qDydm5BYOWOr-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایزدی : توافق ایران با ترامپ و کنگره آمریکا نیست توافق با نتانیاهو هست
🔴
باید ببینیم نتانیاهو متن رو می‌پذیره یا نه چون تصمیم‌گیری نهایی با اونه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131044" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131043">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66c8103ea.mp4?token=qW606jIk2x85X5VY4drO_SdvLfc9sDNDVvqfo3HQ_LGfSFo8nH3ErsjVgUtV4YlkUK9NCQYz5oUoIw4kSKie1R_UcEkshTFXfhbaXK0-2DmG23W__0L96FqeTbKaJYO2NcbbfEmFfXXrokj3VqpmC20-DJv0_qzDM4CON137WFjhww83PDwvh-c_Yaz4IGXSJxzp7fBi9aaRe4jkr4Xdwpph4tGplzXgniCT4hljm-IgLrFzYb04hy-BBK5F38JqoSPXnkTvab6XoADOcj_PDKo1IZpYZ1daLZAdaBsgEDTIdt1H7Unq5361lczAiFsR94fehLOUT-0r3Dif0P5pkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66c8103ea.mp4?token=qW606jIk2x85X5VY4drO_SdvLfc9sDNDVvqfo3HQ_LGfSFo8nH3ErsjVgUtV4YlkUK9NCQYz5oUoIw4kSKie1R_UcEkshTFXfhbaXK0-2DmG23W__0L96FqeTbKaJYO2NcbbfEmFfXXrokj3VqpmC20-DJv0_qzDM4CON137WFjhww83PDwvh-c_Yaz4IGXSJxzp7fBi9aaRe4jkr4Xdwpph4tGplzXgniCT4hljm-IgLrFzYb04hy-BBK5F38JqoSPXnkTvab6XoADOcj_PDKo1IZpYZ1daLZAdaBsgEDTIdt1H7Unq5361lczAiFsR94fehLOUT-0r3Dif0P5pkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایزدی : جای تعجبه که عراقچی می‌گه گرفتن عوارض از کشتی‌ها در تنگه هرمز خلاف قانونه؛
🔴
سؤال اینه، کدوم قانون؟
🔴
اگه حتی رئیس خلیج فارس هم باشیم ولی نتونیم از این موقعیت استفاده کنیم، این اسم و عنوان چه فایده‌ای داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131043" target="_blank">📅 13:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131042">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055600096f.mp4?token=DqM97dGXcyEnES9ocJ3-ooNSk3kDQa7wCt9HywFs6UxykoxxWzyQ7vDD7eKejFKpRq2boQDBZy488S3X8nwGkO2CMBievIMYrgYcGUnVUy5xEMMF5KsN6Nr9j71HX7t6EFaiqsIgrlxOfaqgKPccoEKQSDgOledurLrtCSAhTnC5CutUn-4Nm98fomYyjALcGtYpCk1NhBpfi7p2-a3m8NNH_p9tTCeSnq-E8CXjadANP_3otL28VzTQplEfjCTtCZBQ653Rna6ATkQn0v_qie4kSqPF2g9IekewwADwUeLK9wH21bRQKJlzrR9uvJDB_LW65cyQq9g0jCMOtwQcPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055600096f.mp4?token=DqM97dGXcyEnES9ocJ3-ooNSk3kDQa7wCt9HywFs6UxykoxxWzyQ7vDD7eKejFKpRq2boQDBZy488S3X8nwGkO2CMBievIMYrgYcGUnVUy5xEMMF5KsN6Nr9j71HX7t6EFaiqsIgrlxOfaqgKPccoEKQSDgOledurLrtCSAhTnC5CutUn-4Nm98fomYyjALcGtYpCk1NhBpfi7p2-a3m8NNH_p9tTCeSnq-E8CXjadANP_3otL28VzTQplEfjCTtCZBQ653Rna6ATkQn0v_qie4kSqPF2g9IekewwADwUeLK9wH21bRQKJlzrR9uvJDB_LW65cyQq9g0jCMOtwQcPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی، کارشناس مسائل آمریکا : ما
هی از آمریکا می‌خوایم تحریم‌ها رو برداره
🔴
در حالی که تصمیم اصلی برای برداشتن تحریم‌ها فقط دست ترامپ نیست؛
🔴
بخش زیادی ازش دست کنگره آمریکاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131042" target="_blank">📅 13:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131041">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAIaJQ8Ww19gLa86x8MSRdVVMizq9upee1GybPLYMLWcn7h1c0kSPHTq7nKwpgZvOZgum04ToGTifabffM3XKK4a4-CfPIlF-XZaNyJ4d-BhYmO1snfo6GTbwsrpD6dkPaVwfTL6LnSU9L9YRhAs-AS9sNyZh8fHKad3n9EW5f6a4zXJGydAfovrlQj17EEdvPghi4sa2JQsqrkgqj9EoUWzy8uHpfMGl8_y6r6EkjddT1MnZ1k81OatjVNI44mrIjAMiE3rw7bJpG_RrND0JqipzQlBmpFw3k-778Ka8DSEq6SOkWR6aiEyR11hfWpts6Wh8yDQ2gltsPtZFYGjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131041" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131040">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پزشکیان: اگر آمریکا به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/131040" target="_blank">📅 13:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131039">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نیویورک تایمز :  بیشتر سربازان تازه‌نفس روسیه در خطوط مقدم اوکراین تنها ۲۰ دقیقه عمر مفید دارند !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131039" target="_blank">📅 13:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131038">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت دفاع روسیه گزارش داد، شهرک‌های لسنویه و رونویه در منطقه زاپروژیا و شهرک مالینوفکا در دونتسک  توسط نیروهای مسلح روسیه آزاد شده است.
🔴
این وزارتخانه همچنین از انهدام هفت بمب هوایی هدایت شونده و ۸۰۶ پهپاد اوکراین طی شبانه روز گذشته خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131038" target="_blank">📅 13:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131037">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: چرا اعراب پس از جنگ اخیر دنبال رابطه با تهران هستند؟
🔴
پای یک چارچوب امنیتی جدید منطقه‌ای در میان است
🔴
کشورهای خلیج‌فارس در حال فاصله گرفتن از اسرائیل هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131037" target="_blank">📅 13:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131036">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg-l5vLRvX9-6qeVl0XXrfh2Vvt5E-SWoImG7qSvkMhiGu-dyCbA6yeezZ7HO44FSOPQBxopbnK85JNJjHsd08LtiAQk21IbF5A4U1CyEfnJwJ6JcbkfBQPbBYy9qnZzcBs6dsk5N4Pbf2P5YwUZnVIh2Fx5wAokIw8X8RlqalSRwloJ_pi05mzDoJ92DO2tqOdl40OO32uIUV0LeBsvWMFLXOH03vCVX3j-XEdSzg-PVlaAmQ7pRffF5EJbqvBKPbwtmmtYOEJnASuP7Peyjoj3EoJc51ILxdi3ANTQBFmX4L1RjTtrr0lH9whzr7aGXy8oc1yqTPq8YtlmPuEdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون اجرایی رئیس‌جمهور: جلیلی به امضای تفاهم‌نامه میان ایران و آمریکا رای مثبت داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131036" target="_blank">📅 12:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131035">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFRY0nYdCLuwUKO43nIIc_3ZgSusVcz-ctyccFbdxuJM7mKAo1JC5oapU7DioynI_Hye4CXQvyATv25BRF7ITCwDINoZyuMNwofvNmeZOzwj0pciG49NAiCAZh0S9yVvLJs8BAkqrFzjAHW1aukMqjPaYsQ-YjBNLPY6IFAHacmvqtF45dDstTIbExvZalrwGkzzGQ5FbjmQmgaUD90szL4_LmmgHiAOL6WK6qnmwLDtNG_VBeORxDg0VM-MvFI8G3WHgjMZCMRXqVP5AfABNmx8N8grvwFTK4j3xpqUydE-p1s2hsZNHu3Ma0rLUwPVatTL_lrj2sVuvKKDyqsh7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخزن ۳۰ میلیون بشکه‌ای هند و امارات برای دور زدن تنگه هرمز
🔴
بلومبرگ: هند در پی اختلال‌های ناشی از جنگ و انسداد تنگه هرمز، با امارات برای ذخیره‌سازی تا ۳۰ میلیون بشکه نفت در ذخایر راهبردی به توافق رسیده و قصد دارد برای نخستین‌بار ظرفیت ذخیره‌سازی گاز طبیعی و LPG را نیز توسعه دهد.
🔴
حدود ۴۰ درصد نفت خام وارداتی هند از تنگه هرمز عبور می‌کند و این کشور تقریبا ۸۵ درصد نیاز نفتی خود را از طریق واردات تامین می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131035" target="_blank">📅 12:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131034">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXycxp3MIH8xcaUxxXtY7hvsBIZHGOBjoTF_AJOyqzPxNUPVwvbOjzD_A_1JTAErfk26C_tbxouwEvjvKEbV6ljQltsFWtShrhRHrK2mMkOAZsWy0RgdHKIS5a4-sgoFd9d5pawshUvdvqNuOgN6YeY0_H2fgGkVUivGybhXbzdMSHE67a-4ADagiIvToMSdNFtK8T9Guia3XiOEvOe0dVGyJow4KChmxeiG9Nz_34b_1IYu5tq8rGo4O9f8Uyh5ML44RTZ5g5nzXwzDPWUDYcWUYSjkdcSpNi5r8bWhJa9TJp2tFSn-vP034nTCiWuLjayzN7boOJp9lKcHbMJXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۶۸ هزار واحدی به ۵ میلیون و ۱۲۸ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131034" target="_blank">📅 12:49 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
