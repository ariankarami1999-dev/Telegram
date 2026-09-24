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
<img src="https://cdn4.telesco.pe/file/NMWIfQ4HGdm3EbmbMQF6z5ky8onf_kjAXb0Q1Fp6g8XO4aMArY4ZZHQ-6zciu7mSliE1I7f9RP7Pp1SjtT2dDRRpTM2hzADzWXNp5wIhViCqPO3HdlYxftVVRg4-VKI6wMzK0-JbtgPBcnPgDeNr7pYFfpLz6ZtP-Ihfv9wSQa0yf_7EUbo3l6uVAJBHglfWSSYGYTr0fdgpttN0W5vdUkkHe7bWFoYJkl9zkZQ1hjSK6cdKWHS5ceT3che0vSeFDWZwgtV8NH7KDbGiyFqSTMK1ya2Db7vvIbsZ0etVkhqBrxRJhRnTes0Dk5VY6sHgzSip5Ri-4kjm7ae0GrrZQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 14:17:46</div>
<hr>

<div class="tg-post" id="msg-21168">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=oJXT-JIsALp6jyf1e07TaQdMSwOhKyKpv04-akZ0JAGbyz_Nzk4CCIxf0DU2MvB_dYmtS-f71gilcFYFcs9etiNXW86klz85Mm8FfTFLbSCvt1YJT_G_OJ2owbKyLIQoXX8DUFxufOcT8Uu8rDE_IINqjWXmTtP0Djl-XyER7v7y0rKlOVPBa-dhjz84rQ-j0juObYbhq4Vyo04w6OwvMOfU7Ty-I-Bnd-apVjSNmi-Am7PAgYxOroGR5TxvR_wgUJMJDRqLsHyhJqW0MWbNK4KA7YzYv_t3xpvSAY3TQJk7i0SoP1KXclbL_IQ5qNDbkbwf-G7lQdMO11N6cEvD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=oJXT-JIsALp6jyf1e07TaQdMSwOhKyKpv04-akZ0JAGbyz_Nzk4CCIxf0DU2MvB_dYmtS-f71gilcFYFcs9etiNXW86klz85Mm8FfTFLbSCvt1YJT_G_OJ2owbKyLIQoXX8DUFxufOcT8Uu8rDE_IINqjWXmTtP0Djl-XyER7v7y0rKlOVPBa-dhjz84rQ-j0juObYbhq4Vyo04w6OwvMOfU7Ty-I-Bnd-apVjSNmi-Am7PAgYxOroGR5TxvR_wgUJMJDRqLsHyhJqW0MWbNK4KA7YzYv_t3xpvSAY3TQJk7i0SoP1KXclbL_IQ5qNDbkbwf-G7lQdMO11N6cEvD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.
علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SBoxxx/21168" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21167">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پاکستان حملات هوایی متعددی را در افغانستان انجام داد که هدف از این حملات، مکان‌هایی بود که برای ذخیره‌سازی و پرتاب پهپادها استفاده می‌شد.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/21167" target="_blank">📅 11:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21166">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etQp54QNaQu4fBuGX6XwZ7idXZo0vxmWJkzliQipwtsFeHEGZeUX8vEwWqLUtnOmVWCXkg6MMEAVHv5aPYvnb3Uf02lZegfx70cwGg0KUL6i2ywaScL6SegqFm7lxnDf2Kf2SPAhT0jPAw_k0I5upNkKVuJzr0RNIp66brF8L52XzX1BLhpLKlDBU7_aeWMIUGZ9D95TMLEU5o_0wBWtxWCHjtA8FHB9TeVcNJA7MuJrNAEpi44TLWQfdvB65lwWxR1LGaGVrAXhz_EHYnPLZpVCQRjBZXUzHMhuf_opCmNVwW1uiommgl31NgW6d-WvueR3ijvGTZkBB2iurcZKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف خود می باشد.  در این شرایط و با این تناقض، 2 راه داریم:  — صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230  — خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/21166" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21165">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/21165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/21165" target="_blank">📅 11:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21164">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/21164" target="_blank">📅 10:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21163">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um-3HJgZ6H5HrE9blnTiB2rt1aMByV7hmglS5w4uzaTsWXqx6hzmrReI--0tycOhYN6SO7KRhpzIQLqT6E9UuI8sSLIi1yiZXl643sMNZdk2aQ972OVHINFHcbdBFzd4ng1FXGtNEBXJQl17T1meA7rMk_5pHTZIWg54LzK_8WuSe6pExdKR2GxzmE0MBZGyegPotZGaexhAzBkSZbVplUn3eAia5wP7zkshwRorCVAmho5h1UnGozjOhGY9MZjU-KuJPnWcK9bbT_CyWH2KZVuFI75V9tRW700MrV7S6yPX0UMkFZvMBk8FeBABLUZcXCqkvkwjkDBUqp5XVFEt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف خود می باشد.
در این شرایط و با این تناقض، 2 راه داریم:
— صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230
— خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/21163" target="_blank">📅 10:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21162">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKJ4wRnH2Q5jX5JBjMasZyLTaWrT0Lelo2S7oy4z2A2nPGN138gbSp9mbI_QpATZDG747zHz3DskKq4c3XIMnwa0Hmt70w5ZUO3s7ZHPUDbv_t96GGfcULGc9u5DFrqgijxFsv8oDoG48hqmfk8yDfj_jXjvqL7SkwKetmcHDitxIZ8edFjccbDEfMSqAN6BeCtl5ANgMTR07AbVdGEUSNXmqbKqcTOL95cOD-YA3wYe9B49VMnez5umwYA6omisZSauxP7bg_v4HE6FZD5fWW9Htq0DejpDsh7lzuYXGs361CRL-p5wj6tS3XUa6DghyZx3sKW2Utl4_2Oq-GoQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بسیار بالایی قرار دارد.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/21162" target="_blank">📅 10:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21161">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حملات هوایی پاکستان به ۳ استان افغانستان
نیروی هوایی پاکستان بامداد پنجشنبه حملاتی را به استان‌های «خوست» و «پکتیکا» و همچنین «قندهار» به عنوان دومین شهر بزرگ این کشور انجام داد.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/21161" target="_blank">📅 09:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21160">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مرندی ذوالاکتاف:
اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/21160" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21159">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شلیک موشک به سمت هرمز</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/21159" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21158">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEi7lzw36nMItqtGIpk9HbfthlpT8MnG4kk8qSolnlSQL3_j2BiRNtgTCbWO4JH6Ii6ak1boMZMXACawGenC_SvvXERazeCAdICRi3M5VoobNS6trYEK2g-ZKP6oHUK9uQfl1WNqw9kX3SUGucBabZBxFql-z-A6QmR6_nPCxHcxKue2_DF1rUkPwPbJO8I9O6Ymn5c-rnos9XeCJedPGFlCnkHUwnhPSZR321fSnvbuMzNoKbwoFHgARXx0MnUjgi72kFeu-Ko7aOjwARG4yPQSbUgyIe6sD9S8z1E5WH8iEBg6O_anzCvAOkgJYiu70wUonQQrrbyni8Zwzjg7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تی وی جبلی هم عجب سیرکی است!
خود مردم ایران صداوسیما را نمیبینند بعد اینها برای اسراییلی ها به عبری زیرنویس میزنند!
باز عربی بود یک توجیهی داشت؛ دستکم بدبخت‌ها میفهمیدند کی قرار است توی سرشان موشک بزنیم!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21158" target="_blank">📅 23:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21157">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بیانیه مشترک ترکیه و عراق اعلام می‌کند که ترکیه بر اساس یک زمان‌بندی توافق‌شده، به‌تدریج پایگاه نظامی بعشیقه-زیلکان خود را به عراق تحویل خواهد داد، در ازای آنکه عراق به‌طور کامل اقتدار دولتی را در سنجار برقرار کند و گروه‌های مسلح خارجی ممنوعه را از آنجا خارج سازد.
آن‌ها همچنین توافق کردند که تجارت، سرمایه‌گذاری و پروژه جاده توسعه را تسریع کنند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/21157" target="_blank">📅 23:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21156">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbAVDZ93w51VwaPxnGjnDzFAG3P1TJWbegZv-mWiNPhA-oa39SlHttJ61mT34JCVky6Dxv5nAYCG0E9YuRwRThYsbstAQ6rsJUr_ub1APMB7ASnJcOipSeaxaBRDScMd4ndttH5RkxFxHQYNFR_uXUELZ1th0bjnAP9twV6HN4xi80luudXafMLxdaTZbAR4vSwq9JA7Mi0Tt49GCTdtvdAordjvXLzuUfzZLJhvR-uIyHjqKws7l7I4fN4eI5qjLh9IUp7auHkyk6Sd_KfbowCOdbULNHcqjyWyr2wUNvMVKsC0ck-SvLAU-eLZj6wCu4YBGZ3AFRroYFIYciYWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا چین به عنوان قدرت بزرگ عناصر کمیاب جهان غالب است و چرا این موضوع اهمیت دارد
چین ۸۵ درصد از تولید جهانی عناصر کمیاب تصفیه‌شده را در اختیار دارد و در سال ۲۰۲۵ بیش از ۵ برابر  ایالات متحده استخراج کرده است.
این ارقام تصویری از بازار جهانی عناصر کمیاب پیش از بازدید آتی شی جین‌پینگ از ایالات متحده ارائه می‌دهند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/21156" target="_blank">📅 23:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21155">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درگیری مسلحانه‌ میان نیروهای امنیتی و افراد مسلح در محدوده جهادآباد سراوان</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21155" target="_blank">📅 20:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21154">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صندوق بین‌المللی پول: جنگ در خاورمیانه که از اواخر ماه فوریه آغاز شده، به طور قابل توجهی مسیر رشد جهانی را از طریق اختلالات در حوزه انرژی، کالاها و زنجیره تأمین، تغییر داده است.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21154" target="_blank">📅 20:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21153">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21153" target="_blank">📅 19:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21152">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ایران معتقد است که دموکرات‌ها در انتخابات پیروز خواهند شد و ترامپ نخواهد توانست علیه آن اقدامی انجام دهد.»</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21152" target="_blank">📅 18:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21151">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پزشکیان:   بمب اتمی در اسرائیل است، اما بازرسان در ایران حضور دارند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21151" target="_blank">📅 18:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21150">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21150" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21149">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21149" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پزشکیان:
با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21148" target="_blank">📅 18:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21147" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رویترز:
دولت امارات فعالیت شعب بانک ملی ایران در این کشور را از امروز ممنوع کرده است و بانک ملی ایران دیگر اجازه هیچ گونه فعالیتی در امارات را نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21146" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جنگ ایران.pdf</div>
  <div class="tg-doc-extra">300 KB</div>
</div>
<a href="https://t.me/SBoxxx/21145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه یادداشتی از Foreign Policy درباره علل ناکامی آمریکا در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21145" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21144">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21144" target="_blank">📅 17:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21143">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">با این منطق، فاطماگل قوی ترین زن تورکیه است</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21143" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21142">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21142" target="_blank">📅 16:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21141">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21141" target="_blank">📅 16:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21140">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7ar-ycFuEVHjZ_1_6uXBwn-8ZJmpAXgvAC8gITZR896fBQnlWEGPNjvmK39___Svbc49SJ3D4Vmb1qq9AzfGo984A-FZTxtDhcPGKNDI8KLpJhet88YlwLhiDFyBkqp-jcOJI3hyUI6oGmZZOwgWmdJ3oDoXa3LGNlT5UbJWwSaVrEftFea_Ki0izXr2QBAyojRDGKbxNxBKwPkGG9g3IkKmeIFVdR-2JT4kUP87-joaI5VU9QvJROe9cj98fUFdY91XL1bEVPHKY_uWBoNeWkuglX4OZGo64ZKetyf0vdFep7OKE7SC3ecXXiudCgCgyk9W-LwoemcjKb_Rdfj0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باربی های وطنی به مقر سازمان ملل متحد وارد شدند!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21140" target="_blank">📅 16:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21139">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در هرمز و کشته شدن ۲ نفر</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21139" target="_blank">📅 15:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21138">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21138" target="_blank">📅 15:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21137">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در هرمز و کشته شدن ۲ نفر</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21137" target="_blank">📅 15:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21136">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چکیده تصویری پادکست</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21136" target="_blank">📅 15:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21135">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📌
خروج عربستان از mBridge؛ تقویت خاموش نظام دلاری  خروج عربستان از mBridge در کوتاه‌مدت اثر محسوسی بر دلار و بازارهای مالی ندارد، اما از نظر راهبردی یکی از مسیرهای بالقوه برای کاهش وابستگی به دلار را محدودتر می‌کند.  بااین‌حال، این تصمیم به معنای توقف دلارزدایی…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21135" target="_blank">📅 13:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21134">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4vAuJf6UQIKcwjXPx25XLCz9yg-Ye-txSaLn_5VGykD_PcXBj1dDtNeaowOFaRzIyRDrdpEzTqT3cLUA_Z3IehgxCGEknA2zoGKnvNqrvUz4QNlFlIIQpQOgbegXv6Y7pT3T4D7kAytiMM66uUN4Acm_xhNKQzeldwMcDXyPzCdmT3jf0FMM0jolgy0biwG1Y3fZ05BLZx7qlK3XUHGd2wS8n63cM96OpzhrYp8X0FThVijSIACFBKW6KVlrw_xz1JgymR6KKKIcprLdNaU4kjF1fLRbWbWsLam9u70Lv_8Xb_yppuFDj8q8da9HppccHV21udjY2Z3MHpQ8KeYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
خروج عربستان از mBridge؛ تقویت خاموش نظام دلاری
خروج عربستان از
mBridge
در کوتاه‌مدت اثر محسوسی بر دلار و بازارهای مالی ندارد، اما از نظر راهبردی یکی از مسیرهای بالقوه برای کاهش وابستگی به دلار را محدودتر می‌کند.
بااین‌حال، این تصمیم به معنای توقف دلارزدایی نیست؛ چین و سایر کشورها همچنان در حال توسعه زیرساخت‌های پرداخت جایگزین هستند و
mBridge
نیز ادامه دارد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21134" target="_blank">📅 13:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21133">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgvSIFBU1s9HaaNBcZBkStsbqcU-SoaFblq5CZSJKmKiWAXAVC7IpXO5_6l3j8orA5nQn72cg4UEpKOJCjQND6ZiqmN-qY7BsjR6lyA-DFu6_8uOluF0VTupzRiE0fZtUuEj4JkriCCQjDPZUk76ZeSjgwY79tKVWCIz2ztxfisJ3BAjHVX3FsfFmNbYWxwvqE1pBf5k2u7juTlDbKJDXQs6HphZRI2xjX5o50Fz3mrawoBdRdT6B5ecnhqDpxp2vzxSqdzhLZCVUumStYxiJeqezqDBI2BjUPGacG13vlEVTDB4aeNfMLOQd4FnIEKP0SqChDmktstH4y-7P4e0Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.
محدوده  مناسب خرید:
4302</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21133" target="_blank">📅 12:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21132">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_zQaYXVeLlyP-pdGl3nUbp-bNdJRWdy2qf7KCNY-ssIK8FdatXVjZ-w0_ghXelp82Z2W8gtCLuv8jnZSgv355EvofNSvyMw2zMYx77jm_XqxSWJFaKxwa5NcVraIY85p1WwJgjvDy6p4hojnmjLhw-mQ1PrbpQ4SddM7ofiW0Xo2CHoJtAb3EJ9lXG6nfGhF0xKw_zXO4JjNMiGNwKZl_dg97F890QOXTIFamVBrrSVIcpNaxL7ia_yoNLGq219IbC-9fZydOom_72pTLfZunaozvC238fQssO8opuOXNmvqBhooLrXG9DWs0VO0VUBU3vkJDPZ9c_J2oFbzXDRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بالایی است.
اما طلا از صبح ریزش سنگین داشته و لذا دیگر وقت فروش نیست.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/21132" target="_blank">📅 12:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21131">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=KkZm3BiDbZo99bwqIu5Cce-sfLd_62JLercu0EwGsE0dgShZ6gqnIQ4VMZAV7to7JuMX-YlQ6beqZ6pKWvOURwDO6cMza-gGeNGMgQBm5F9bb7PKrwIMKEXJOzCVX50H3B0ZkQF2JCWTsklVuPjfd_WjyQb2EE29bKlwLh7VHBFHB1CBjfvcs_0X3-fCnfQxjNCx7ztlf_zZXN6IcX5qtZrJMIUlwhg4alLyDdWv8cMChbGigDPLVQKDtQlJG1zSszhkYvWecCbLuYwLf-8qMYvaAJP7cFsz-McNeXoFS8orJgMCFPRxTDo-PnsSJsVOSPnKoZAr0HKthrnA8O_7RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=KkZm3BiDbZo99bwqIu5Cce-sfLd_62JLercu0EwGsE0dgShZ6gqnIQ4VMZAV7to7JuMX-YlQ6beqZ6pKWvOURwDO6cMza-gGeNGMgQBm5F9bb7PKrwIMKEXJOzCVX50H3B0ZkQF2JCWTsklVuPjfd_WjyQb2EE29bKlwLh7VHBFHB1CBjfvcs_0X3-fCnfQxjNCx7ztlf_zZXN6IcX5qtZrJMIUlwhg4alLyDdWv8cMChbGigDPLVQKDtQlJG1zSszhkYvWecCbLuYwLf-8qMYvaAJP7cFsz-McNeXoFS8orJgMCFPRxTDo-PnsSJsVOSPnKoZAr0HKthrnA8O_7RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21131" target="_blank">📅 12:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21130">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">زلنسکی
:
ما باید قوی باشیم و باید به پوتین نشان دهیم که او تنها در این سیاره نیست، حتی اگر این رؤیای اوست. و به همین دلیل او باید به مردم احترام بگذارد.
متأسفانه روس‌ها فقط زمانی به مردم احترام می‌گذارند که نشان دهید قوی هستید. آن‌ها به ضعف احترام نمی‌گذارند.
طبیعی است که گاهی اوقات مردم بخواهند ضعیف باشند، زندگی خود را بگذرانند، وقت خود را با عزیزانشان بگذرانند و به فرزندانشان عشق بورزند.
اما نه، باید با روس‌ها نشان دهید، باید نشان دهید که قدرتمند هستید.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/21130" target="_blank">📅 11:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21129">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آن دو دیگر (کوبا و میانسوسمار) هم که میبینید ستاره شوم کمونیسم بر بیرق چرکین خود دارند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21129" target="_blank">📅 10:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21128">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">موسسه مطالعات جنگ:
به نظر می‌رسد حوثی‌ها با تهدید شرکای بین‌المللی عربستان سعودی می‌خواهند این کشور را منزوی کرده و مانع تشکیل ائتلاف علیه فعالیت‌های آن‌ها در دریای سرخ شوند.
حوثی‌ها در حمله به پایگاه هوایی شاه‌فهد در طائف عربستان در ۱۷ سپتامبر، یک جنگنده اروپایی «یوروفایتر تایفون» ایتالیایی را آسیب زدند. ایتالیا این جنگنده‌ها را برای پشتیبانی از عملیات‌های دفاعی در برابر حملات ایران به عربستان مستقر کرده بود. مشخص نیست که حوثی‌ها عمداً این هواپیما را هدف گرفته باشند یا خیر، اما حوثی‌ها پرسیدند که چرا آن هواپیما آنجا بوده است.
حوثی‌ها احتمالاً این مأموریت پدافند هوایی را تهدیدی بالقوه برای کارزار تهاجمی خود علیه عربستان می‌دانند؛ کارزاری که عمدتاً از حملات به تأسیسات نفتی عربستان تشکیل شده و در میانه پشتیبانی دفاعی کشورهای مختلف از عربستان ادامه دارد.
حمله حوثی‌ها که به هواپیماهای اروپایی آسیب زد — هواپیماهایی که برای پشتیبانی از تلاش‌های دفاعی عربستان در برابر حملات ایران به این کشور مستشر شده بودند — در واقع اهداف ایران برای شکستن ائتلاف مدافع کشورهای خلیج فارس در برابر ایران را نیز پیش می‌برد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21128" target="_blank">📅 09:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21127">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiJe9ZghEoyOLrmhy3U9S60_vNuWmUMCdStkjgHqgavevPv3ih47AC29pE6rAwZJtPlgN47lwExGwEeOcZdHY5ZoxcNLnwjc1FqPagnwia7oobHpR5Hq1BcxEqfIVSUhbkh12YYOlnvrhuxOzm8e-b6w4ebz2qlTCKk8pPwT9kumTZrhUdvroY7d__lfMue1BSEQAV08oyALipwnaMzzKjaJ5PkC4rz2uMRJhCX4477W_rqKL-nEnYdpwRgyT9g65iaSK0KTaIzLxSB7DAJI-b9vnQgRV54RiKi3OsiGBBHYTIct5H6kiwQOZzog0qKA0vnFBCNT5FHmG7LQc1VR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21127" target="_blank">📅 08:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21126">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نخست وزیر یونان، کیریاکوس میتسوتاکیس:
ما در ۳۰ سال گذشته هزینه‌های زیادی برای دفاع صرف کرده‌ایم، اما در زمینه صنعت دفاعی داخلی، دستاورد چندانی نداریم.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21126" target="_blank">📅 08:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21125">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏
سخنگوی سپاه: نحوۀ پاسخ ما به حملۀ جدید آمریکا از اسرار نظامی است
اگر آمریکا به کوه کلنگ یا هر نقطه‌ای دیگر از ایران حمله کند با قدرت پاسخ خواهیم داد.
این‌که پاسخ ما چگونه است از اسرار نظامی است؛ ما اسرار نظامی خود را فاش نمی‌کنیم اما در میدان عمل نشان خواهیم داد.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21125" target="_blank">📅 08:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21124">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، انتظار می‌رود این هفته سفری کوتاه به ایالات متحده داشته باشد تا در مجمع عمومی سازمان ملل متحد سخنرانی کند، در حالی که نگرانی‌هایی در خصوص اعتراضات احتمالی وجود دارد.
نتانیاهو قرار است به جای فرودگاه بین‌المللی جی‌اف‌کی، در یک فرودگاه نظامی در نیوجرسی یا فرودگاه بین‌المللی لیبرتی نیوارک فرود آید، که این تصمیم تا حدی به دلیل نگرانی از پیچیدگی‌های مرتبط با ممدانی، شهردار نیویورک، اتخاذ شده است.
هیچ ملاقاتی با رئیس‌جمهور ترامپ برنامه‌ریزی نشده است، هرچند گفتگوها با مارکو روبیو، وزیر امور خارجه، و سایر رهبران خارجی همچنان در حال بررسی است.
بر اساس اظهارات مقامات نزدیک به نتانیاهو، سخنرانی او قرار است بر ایران متمرکز باشد و ممکن است «غافلگیری‌هایی» در بر داشته باشد.
مقامات اسرائیلی همچنین برای احتمال اختلال در سخنرانی او در سازمان ملل، از جمله آزار و اذیت یا خروج هماهنگ هیئت‌های چندین کشور، آماده‌سازی‌هایی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21124" target="_blank">📅 01:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21123">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21123" target="_blank">📅 01:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21122">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21122" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21121">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گویا جلسه برگزار شده و به نتیجه نرسیده!  First Time?!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21121" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21120">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuevzD0bn-rc7y7iFO_tcliroWidFvV8GS1f4f51OI4a6bt7bDsWJomB3zG-d8PxJ9rJraKlrAgon2RYkAof5aUo4522GWzH0_xVNfvfDdvLVlywISSq0ba6pgrQHNPp1TQo5i3J7rqqEhdg7xeLeVQ_m9MheXXolS-utbklqWm9IvZE6nOzMCeCFBPaWHuPUmg8vMSxUjnev9Wgfl84jy25rW1RvWcknygFHbyGFaooUNK-E8G1sBenowBqYaI_TBMLI5T4iDOumPAXze4Aft94kJR7-dnAP4AsPD8vSm7STHq2BYslG1eb45tXDwHGHBmkOGUGzQVsWZNtfRXG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21120" target="_blank">📅 00:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21119">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ah4LCzFVp8nJCRRJC2EhvjKZL7x59g1Oo66hVVKhRSDIpN6gAutocBUYaqiMa1eLkQXZupH8zS-Oz8ukKt_csvWt51QFfDy6v9RsXtIMLruzmkQ2QbFFv529LSOMJZVMtS1JDdyyDXJyr58HwSssUztdyPIz8BERIyX40V60Pz1s_TFADrzSXcU5t7wW97xBW8s3FtMb2EvaeVJbGJhiytQKwQhzKL4hUiJKPkqT9jUKgrKRkogL1VoIeHtWa5zIHlfCoXL_z9Ny3zg91PCo4WkUX5SX9v51ZTP8ySq6PYV3Tpedf_kXMU89S0DM7mOYRh-j5LQzK-0BjjAorXjzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/21119" target="_blank">📅 00:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21118">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ewju3zhs6pgmDd5DnPyIrJSgj6KoqBPVx11uaxepZPEpwhArVtO4Fkjb9VCO8TZI6CCFJLpOlW8llOtHq52PCLigQtCXnJdqml7qKgcdxrqKHoTzWRinl464MHmrSdeEgPXJCP4H5J7NC_kC4lBUj4UmrKCOlXg8GoFEEn-cKtaL5G-SUjcVIiyYj4he5srBXukWS00Jw3oWp9XRArJJKACII00mbck8BZsvs2MGRcl-j_ZeWl4PggrtFaQvSAZqfpkkXGsDeFDCVcICWqWPsaq2WLuzo-hwZ6BfIuoDmPbh09hD1J9fQ4EisGONp-ibWPpL2wqoWA8a_V8l3uV-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUN_CFD — D #SUNRUN  از محدوده ورود دوباره حتی اندکی نیز پایینتر نیامد.  البته هر چه پایین تر بیاید خوب است، این سهم یک رشد دستکم 3 برابری دارد.  همراهان Secret Box در خارج کشور این سهم را دریابند و هم میهنان اسیر در درون مرزها نیز میتوانند روی بروکر WM Markets…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/21118" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21117">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR23trVkC06of1Ti5e0AFPk2u6KmNRqT4sf8_PHcatDz48X3En69E9PEp43yWWerNrtJx1dKHy1_DSnXkMFZD7CsRD-F0yeZCzRePUkdhVL7vtTj3lJhe6sAqNTqgY1DEQtN8pT7YFLj6TV2_P-cicWz97zJEGVFAlk862RlCDK3QL2zHHTJO8jBhZWjchkmmBL1klAPRhQpc8DUzzjcIAO6aajN8VDgtgQMw8m4dhSy-l6-ip7d1M1FKM1QMd1UFNSjnrvJP8KqRpNGixt6moTyb0MqmyRiC3GwUxzeYhGi6fYjrBcRpwbCZANh6SaQ01LUrzjFSKnCyC1EgyH_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL   دوستانی که درباره نفت دایرکت دادند؛  پوزیشن های خرید ما به هر دو TP پیشنهادی رسیده اند و فعلاً خرید نداریم روی نفت.   تحلیل جدیدی از نفت ارائه می شود.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21117" target="_blank">📅 00:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21116">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP-laG_GJSpyhOJJHzBDxFlZ8eow6tjWIvVNAt7YFa9JYzJ98ZCYEdjf5EJI_HD9-0QFQFufb6ej3w72XcN3B919IM6JpC8wLTRlUB38ufS-jX_vwy520Yol1R1ghyZPkcSqJaNPSw2Y9JhJw-VH70NADfR45gnH1Ow_qKRnKktzkz7K6fo0jk34WdyCPDz5fUpP8N4y_s54HFNdoBxpdh8r8BJoH6JfxHPbz7uIJjq4fRdqCMcvXOz29veyrxBzFtJepUo6qzLO7R7-Kr8OTNNAaoV7ljrUH1qkkxm4BaOffEkCK2NHW5OPhrFV8-mkP6qSDZrxbRtz3a9DcJIyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/21116" target="_blank">📅 00:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21115">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تایید دیدار عراقچی و ویتکاف
صداوسیما:
با اصرار نماینده آمریکا دیدار آقای عراقچی با ویتکاف در حاشیه مجمع عمومی برگزار شد
ابلاغ شروط ایران برای بازگشایی تنگه هرمز دلیل پذیرش درخواست ویتکاف برای این دیدار بوده است.
رفع فوری محاصره دریایی، پرداخت فوری همه اموال مسدود شده ایران و پایان جنگ در همه جبهه های مقاومت از جمله شروط ایران برای بازگشایی تنگه هرمز است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21115" target="_blank">📅 23:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21114">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd2-Q5IdC2ZfK_GPaW4yBiNeeK_VPzo5hjbqlE6iJ6ebgb5OOk-_rIyqPipizF6-te-YINokb2KIWl5nK2XD99HgSGiszkIGSclvbFW-kbQF_6TUFO2Tg_6YzuU1fWy5uY4go8eTfG0GyahvuWJvARYfyX5Y7D2avPoPFkdy5YUQnFMQWQweA78r-D6APeew_hZS9dtAYGJfYsmO8CNtPE5Vv370KC5qj_RieFmz03noBFxbbstu-fOkrM5i86IInMv0WZy4ZV0zl8BimB6TutV4KIQr0B-9Blo7Rpdo5cqV4DDeFwCeeQLvqr-EefoaABXwrzpUBtHmykDrhV4D_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد بز برای پاسخ به کشورهای همسایه که در محاصره ایران نقش دارند</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21114" target="_blank">📅 22:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21113">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ادعاى ترامپ:   ایران در حال مذاکره با ماست؛ روابط با ایران در حال توسعه است.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21113" target="_blank">📅 22:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21112">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLUwEnNDFTzsaW6_UzOKjgwejC_XpA5oGRfODXip3FNHyz3d1RS5Myh8X0xyDsviHG3B4jTiZg8kqeIailnZaGsPFCNAdRFy3nUsGlqIqHRICf_riy6EbqRlf-nt7XE69RI-hRSawmwei1Rx2OD7ybp0tVO8nA83kys95Tt_7XqfnpfKiTC9a5_g4tE03NFyD61abO9jGPNAIJTNUyp-oibqsOtwuy4u1k2VXoR0FLW0ucjHUsuanq3OrjZ-oW12nPMgLNKv3qTHb3RO98qKpl-J6FF9nbqotWrlAZQoxXJTA0r4SueTzv7WXmvkwuSUEjKAw8ZgYKJw0QiNg24ClTYoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLUwEnNDFTzsaW6_UzOKjgwejC_XpA5oGRfODXip3FNHyz3d1RS5Myh8X0xyDsviHG3B4jTiZg8kqeIailnZaGsPFCNAdRFy3nUsGlqIqHRICf_riy6EbqRlf-nt7XE69RI-hRSawmwei1Rx2OD7ybp0tVO8nA83kys95Tt_7XqfnpfKiTC9a5_g4tE03NFyD61abO9jGPNAIJTNUyp-oibqsOtwuy4u1k2VXoR0FLW0ucjHUsuanq3OrjZ-oW12nPMgLNKv3qTHb3RO98qKpl-J6FF9nbqotWrlAZQoxXJTA0r4SueTzv7WXmvkwuSUEjKAw8ZgYKJw0QiNg24ClTYoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روند ساخت اسلحه های دورزن در یمن!
با همین تفنگ های دورزن، حوثی ها صدها نیروی مخالف خود را در هفته های اخیر کشته اند!
ثانیه 29 جالب است. یارو در دهانش قات می جوود اما دارد اسلحه دقیق زن هم می سازد!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21112" target="_blank">📅 22:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21111">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خاویر میلی، رئیس جمهور آرژانتین:  نسیم‌های تغییر به نفع ادعای ما در سراسر جهان در حال وزیدن است.  اخیراً، رئیس جمهور ترامپ اعلام کرد که ایالات متحده در حال ارزیابی مجدد موضع تاریخی خود در مورد جزایر مالویناس (فالکلند) است.  ایالات متحده در حال بررسی این تغییر…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21111" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21110">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=gUEaGLmGyo771tcCJ6cIYrP9lUzCrIYbbAJCPOH3Nzd1C8mMxIM1_v6uJtmotJn-JEwinEaW47I-4T0RUrqm3iiik4mPHKmOLgQrifMTGtlR35qiGc8bSmQgBhjvG-e1XCIFF4-zCwWS1QR0zhYMimXuC34SBKW1h6gFLFmLtWKoeR8Tycllwep3xTmsHNW_CZdtPEbm_We-yqiasxt5S9SAziuFYl5yQtGRep6preEsi_ELtXFBRXg6iVIaUGCmKcY4sAQTLJx_yTXuMR7SaAXZJOtic4aEVEuMydRKsOs-RoDJD1B7_Im44SsGnPp61Io71l1-bCI06_-EJbWQ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=gUEaGLmGyo771tcCJ6cIYrP9lUzCrIYbbAJCPOH3Nzd1C8mMxIM1_v6uJtmotJn-JEwinEaW47I-4T0RUrqm3iiik4mPHKmOLgQrifMTGtlR35qiGc8bSmQgBhjvG-e1XCIFF4-zCwWS1QR0zhYMimXuC34SBKW1h6gFLFmLtWKoeR8Tycllwep3xTmsHNW_CZdtPEbm_We-yqiasxt5S9SAziuFYl5yQtGRep6preEsi_ELtXFBRXg6iVIaUGCmKcY4sAQTLJx_yTXuMR7SaAXZJOtic4aEVEuMydRKsOs-RoDJD1B7_Im44SsGnPp61Io71l1-bCI06_-EJbWQ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:  باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.  از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21110" target="_blank">📅 20:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21109">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21109" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21108">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آکسیوس:   تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21108" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21107">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آکسیوس:
تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SBoxxx/21107" target="_blank">📅 20:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21106">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:
باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.
از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت بشناسد و روابط سیاسی، دیپلماتیک و اقتصادی با آن برقرار کند.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21106" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21105">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !  یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21105" target="_blank">📅 19:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21104">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=PopGQ-j5sM5B07fWLclV9tm9VP_1UVMYyflyE_mvDse7BlbT2n0ihqfT9glh4XdaKMQpYT5Ze-rhOETPjBq1vzbq4P0dGx_694O8VRfayCtfCq_Yz063txmxYIZ58OLTtvb0-LwQ0-wItmxMlEVFoboby0mqFq_BC87H5JghC8CjkBzRR3iPKHSjEu1AqAjSt2E6QR_xXt7BCw_-OERDatbTayNVnnjQLkcvfObAzjO1z5IvBY7eEuqs-0fnLkZJxIi8pReEcY2dpF6S_ZY9bDDf2ESpwpOUNVEFAarWsj1qqRJpdjF0s1ZVL27izNsAlJfgT8aXu1F0eh_4gTt9Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=PopGQ-j5sM5B07fWLclV9tm9VP_1UVMYyflyE_mvDse7BlbT2n0ihqfT9glh4XdaKMQpYT5Ze-rhOETPjBq1vzbq4P0dGx_694O8VRfayCtfCq_Yz063txmxYIZ58OLTtvb0-LwQ0-wItmxMlEVFoboby0mqFq_BC87H5JghC8CjkBzRR3iPKHSjEu1AqAjSt2E6QR_xXt7BCw_-OERDatbTayNVnnjQLkcvfObAzjO1z5IvBY7eEuqs-0fnLkZJxIi8pReEcY2dpF6S_ZY9bDDf2ESpwpOUNVEFAarWsj1qqRJpdjF0s1ZVL27izNsAlJfgT8aXu1F0eh_4gTt9Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !
یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21104" target="_blank">📅 19:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21103">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ:
در ۱۲ ماه گذشته ۱.۵ تریلیون دلار در ارتش ایالات متحده سرمایه‌گذاری شد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21103" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21102">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یک مقام عراقی به الجزیره:
«به فرودگاه‌های عراقی اکنون دستور داده شده‌ است از فرود هواپیماهای ایرانی، از نیمه‌شب امشب، جلوگیری کنند.
اقدامات انجام‌شده علیه هواپیماهای ایرانی مطابق با تحریم‌های ایالات متحده است».</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21102" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21101">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21101" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21100">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">— مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ترامپ آمادگی دیدار با پزشکیان را دارد، اما باید بدانیم که تصمیم‌گیرنده نهایی در ایران رهبر معظم است و او یک روحانی شیعه افراطی است».</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21100" target="_blank">📅 15:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21099">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21099" target="_blank">📅 14:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21098">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سخنگوی سپاه:   اگر مصلحت ملی ما ایجاب کند که در کنار جنگ، مذاکراتی انجام دهیم، باید مذاکره کنیم</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21098" target="_blank">📅 14:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21097">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21097" target="_blank">📅 14:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21096">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 28</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 28
سه شنبه 22 سپتامبر  2026</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/SBoxxx/21096" target="_blank">📅 13:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21095">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">— شرکت هواپیمایی ترکیش ایرلاینز، به همراه پگاسوس و ای‌جت، از ۲۱ سپتامبر تمام پروازهای خود به ایران را لغو کرده و حداقل تا مارس ۲۰۲۷ هیچ رزرو بلیطی در دسترس نیست.
تحریم‌های «عملیات سرد اقتصادی» ایالات متحده آنقدر گسترده است که حتی هواپیماهای ایرباس حاوی قطعات ساخت آمریکا را نیز شامل می‌شود و برای شرکت‌های هواپیمایی ترکیه چاره‌ای باقی نمی‌گذارد.
شرکت هواپیمایی ایرانی ماهان ایر نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، گفت که خطوط هوایی ایران از ۲۳ سپتامبر با تعطیلی جهانی مواجه خواهند شد و هشدار داد که شرکت‌هایی که به آنها خدمات ارائه می‌دهند، ممکن است در معرض خطر از دست دادن دسترسی به سیستم دلار آمریکا قرار گیرند.
ترکیه یکی از آخرین مسیرهای هوایی بین‌المللی مهم موجود برای ایرانیان بود.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21095" target="_blank">📅 13:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21094">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21094" target="_blank">📅 12:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21093">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4QFk_B7PVuNlZbk0AevoNdCvv2qYQ3UzQpLpSbxLQkUpRh16S_NPYgxt_rirrkRnuYwGkwbqi14JlXHgjySZs95DnoCQxJlpJR_CAaeQ79Gxqc58DQmFtXe226HRj7ue0DSAJwwhw3DSSKhqqcDemUFumbKuQJbvmzyylTtrTtibvHJFgQMJdaclWFmMTxDrvBz_nmTk176S6WtBVthB7MPA_UZg0smV5m-rKdmBfiYy3MiSEH5QBWwdQfFK1a-O89hijlfd_qTSYXpvBvJYJnt4E5dVsZuDlmre9n-6BshYb3ZHu-nNIsp3TrmhdYlE-EJk_4-gsE-8V5Oep-Ffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21093" target="_blank">📅 12:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21092">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJWxOrxt1xMvFR8XXPsItU13GViC-DjWP4zdbVqYdwLKCDnWCngYyZFQXA4ggJP-wCcKj_0DGtiMzMSFI67K6v6ulrKYaUG2tB5frdMp2Slw0u7Ax84ihJyJmcRPM9llZKXUdhD-mbjhepSv1813cY3MXY4Up5eF0dILUn7LmYZlyZuzhlk_baMc_v8uA7TROOxKpu0yu0fwlMux1Ia-CqcGjR_lTmtbiN7ZfFSsjSgtZYu1F5pZ9RPgLPll6R0as5RriKgUgHNBaq3ZRv1B9W1A_YMVqMdQihNQmO52i4doZSzJiEZPicNwFnmWbFguuFH5DDQZ5uRO2_66l2X1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه کله پوک پیمان مکه کم بودند، حالا وزیرخارجه مصر فقیر (خر دوم از راست) را هم با آن ریخت و ترکیب ش add to group  کردند!
فقط سیس هاکون فیدان !</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21092" target="_blank">📅 12:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21091">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3bOCnnBIPbdfXCmy8Q4qc4JCVDYCpvbGUkvjL4tw85xUDfEBHZZmxQ969_Ed1leezeg5TzsO1eTOvibfsT9DsxwwG6auWChQsbbNNNdTtGYzHSvepm9wzu7GWXHf5-eEp8qD_N8tHIU-twZ6D4JzIRM_HQtky_qxZqG--2vbnc3nVubUM7XDOoP68AW3uGrecp3SLekk3fJi0N_FjDgOHcaFhVu-TozuPdfPNCYFX03LFlY6MkJvGs8LoTDAoeCx1yXDSLDuxs4MwI2MMZSrPyJPNpEgLmiDdR3ag_QKAeBrgcKFCgpyumNHJptzkxuUwsS3MrAUR1q1vR4n6sB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/21091" target="_blank">📅 12:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21090">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/21090" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21089">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/21089" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21088">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21088" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21087">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21087" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21086">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLPIseaTR8cNmbjZUDyovoC6WG-Rp-RPqiTsc4q07peS-iTtaHeZNVoKbfX07xXze71n4AHr2GNe8-rGkgjJ3csmtGwaHhKEZ1R6S-3ZTAccGe_mkmJRzS8m0rAEnhiK8UNPq3imxlKaw7zJWCMAvmKggr--mrlM6ifg85-8wKWn3kwcwQKQu3hDXRZrC-FUBxYjzkji1u8r-1G0XH0XzqtJRlcKeahv8ODYJlBX-YeBtDaLLsbdyE_a6erJwcFUdINaYJCDGdgNB7fb6UzSuF9qX3sdD-kf0SxhzoypQp2sD7ov9k7oLEvxVbuRX3PRZTETJDVd7y2tOd5rxCzkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21086" target="_blank">📅 11:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21085">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyL36GJKDYdePIKgir4ME61YENFbxV9UDJUIwZ0TsuF0X3dS0aFHyi38z-3030jdIGuvZYWS5G9d7tu6lhTCoAVxQpIhfIMTWQQwCeYAHi-Lruw-yuqboqb0_Up3EhaHjS_dDHh9xqQcI-8OBF82074A3vgKLd-ZY0e5-BEYTl4GzoPZMTaWVf9HHVHvn6kWcBILXqCAP4jjXY3k1oCK5mTn78_MNVgpG9ZaTlLPOm0fTTAbs5cY7FzVPTIM6bUkeOsBigMx515-DyLXwGS5kYDZJljM0-NI1HnqfHRVATQwcI6SWBQFy5RmIGxGY4uGO8VXIXNm1BTfGelmQeR4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است. اما نظر به ریزش سنگین طلا، اثرگذاری اش را گذاشته است.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21085" target="_blank">📅 11:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21084">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XK8NbL0zsx7eeZnWX-OHKvIv0h8moRW1DY5VthISaa66Vfhh_JXOPtpKCzq7zu6n8rkX2ogClLrbFllnm6wQdlh8PiaidXdfXAJsEg6A-L_VPNCG6b70Apzrkz2cozHpNl1qowbV-ux9ZOWVRkJYywhMys4T-2oGqw3q8hzA1M71Q5yvRAHzrUuAaFmbdxA4t6aFeQ9ZHinvz_g_IRin2AXOd4N9w5twmG3f6hqAFEzn5PRhdY04dtIimi95khOPDY3ohPXhPPhoMB4fXaRfofnVC8GX3Tpu9iYSrYc6nRuChiK2yNqAplvYU-vgyFoeLZjPEdXnVw0wxTEUZDT5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پله خرید طلا توصیه می شود.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21084" target="_blank">📅 11:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21083">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کاخ سفید، پخش ۲۴ ساعته‌ی «کانال تلویزیونی ترامپ» را آغاز کرد
!
کاخ سفید، پخش مستمر
«کانال تلویزیونی ترامپ»
را از طریق یوتیوب و پلتفرم X (توییتر سابق) آغاز کرده است و وعده داده که سخنرانی‌ها، اطلاعیه‌ها و مهم‌ترین بخش‌های فعالیت‌های دولت را به صورت "به‌روزرسانی لحظه‌ای" ارائه خواهد داد.
کاخ سفید در پلتفرم X (توییتر سابق) اعلام کرد: "شاید همه لحظات مهم در تلویزیون شما پخش نشده باشد، اما اکنون این امکان وجود دارد."
کانال یوتیوب، این پخش را به عنوان
«پایگاه اصلی»
معرفی می‌کند و وعده می‌دهد که مهم‌ترین لحظات و بخش‌های برجسته دولت ترامپ را به صورت ۲۴ ساعته ارائه دهد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21083" target="_blank">📅 11:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21082">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5gPa-hNlYZg_5AIEupnBsOGhvFbMhA0XWDPpAUWKn5R_D2uowSozQ9EVSAjHEkuBaVbstGWq-QnxX54dBDc_0AIXkr00emeq88hTYEsb7lJS0Xs5wi9qAXILCg9GBGxRLjVSaoHUBQ0nsWUVS1KnqRPIDQbF2uOrvJVZZNGo97QKcQVSVKjdrh_p6B8S_6pj25hNiEP0i9oybF1DSQIEd-Jnd_kY-I_UIzQ77WfBszdz2mX8y2420WTrdy2Msr_3UWv0r6ZiRRQEDTBf6eEtAKKkYyZsmWWs1rBLFV03AHZqGYMv9pWKTdivpIgdKI_QiLhA0B_HvH4WsudBTJlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21082" target="_blank">📅 10:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21081">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKzyVwo7lTJMnadjSBNS1RKV5VI83h95r0OD1mQQRDOfzJMoLX8u_ZK0-V9Ik2N2A3BpulmhSVeGNTvx1A7MxTF943_TRBriKg2NNwoXOXA12VCMCJKnZYzwj9o5DI2gsrntTjpWL5D8xDdxbT9sMAXFWiXJFqPB_ZVLhR0ga9lI_6c8C8J8czyqXKX7HbrqPV6UZCu9D5TD0ezRrWvJieIztrLI2y_UDmpkrsFoJHX8Qg13YyEuhaCCduCHpeq4U9Fu2ycrm1Srf0ovRblFncIpQkWyrrP5bxyxnWXbi4deEjyle-kK6ylD_12fu69PmSQdSgnq-241Cuhz69gQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمونه ای از جامعه ای سرشار از زور و ریا!
حجاب اجباری بر سر دختر می کنیم تا در بلوغ و بزرگی محجبه باشد اما همین الان مادرش بدون حجاب است!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21081" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21080">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
ما آماده‌ایم همکاری‌هایی را که با ایالات متحده در حوزه‌هایی از جمله انرژی هسته‌ای و LNG، حمل‌ونقل هوایی مدنی و فناوری‌های پیشرفته برقرار کرده‌ایم، گسترش دهیم.
توسعه بیشتر صنعت دفاعی — که به‌طور سنتی یکی از قوی‌ترین حوزه‌های مشارکت ما بوده است — هم به‌صورت دوجانبه و هم در چارچوب ناتو ضروری است.
ما می‌خواهیم موانعی را که هرگز نباید بین دو متحد وجود داشته باشد، پشت سر بگذاریم و شتاب تازه‌ای ایجاد کنیم.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21080" target="_blank">📅 07:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21079">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOmOCEx4FLLLQ6QtnI2-QHiIsValSHBIyQM_zOF2Jwd3ydnVinvYe1CVEF-h252yLnbmmsrYejwbKp3tPcgaMuu0R_5F5erV57374xlF9-EFFCTZEq4M0-hiNXiNM1TS9XxMNTreyT-seoAHK2ShkHTweAZ7kNwD7suyQPlLi1iIbxKuqeqnvfAEmx0YXMKWdinDMKTBJn3A0WMxikLqRObGXwZrbBbeNODEybYj9sZs5O8RVqoEFbY9xYTcXH6eglS3HCLLqbYfIUU3GfoN4jxBj1OKUmjoyKygKzpOc8ByQC3ynOPklRIFBldMlqzLL3TmZ3c5BsmuXiAixl46MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
دلار، نفت و موقعیت های معاملاتی گرید از دید موسسه Danske
موسسه Danske با توجه به رشد اقتصاد آمریکا، سیاست انقباضی فدرال رزرو و اثر شوک نفتی، تداوم قدرت دلار و فشار بر یورو و پوند را پیش‌بینی می‌کند.
در بخش معاملات گرید،
GBP/JPY
به‌عنوان یکی از سناریوهای نزولی مطرح شده و ترکیب تحلیل بنیادی و تکنیکالی، افت قیمت تا محدوده 181 را مورد توجه قرار می‌دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21079" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21078">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21078" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21077">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21077" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21076">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21076" target="_blank">📅 22:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21075">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYGhAzN7OJaVJ29RxT5yVl6EeIyGRLnKODFFnK_1vcdZvTQUyHV1iHuzPAHEpJaiQk2mZE3BRYxnB364MsIuLBaN8deiPKmwSY3MUje6nl5uVp44Fho0nyGi9rk1C2pPjCXCRJemIuTgd9i4erS8rQL55XO2FWgv6yhBUCYE5BIBP3QNuULv-uaE3z4i6jM909uDgXyWpr1wVcLAgryN09vDVRGH5n-Hc-Ki2F5AmVk9MWkPpcGzF01vg-YcHiJxMDH1Xa1XeXJfZTsrUW1hY7y-S_QR9qQe-sTn461WIMOYc5oc6mGaxTT6bcGEK-kkAYbIQeC85A_wHFWzhX0JsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !  فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!  اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21075" target="_blank">📅 20:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21074" target="_blank">📅 19:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5CvouX7SmakYofnpxzii52OOkYusDcTENdFNsGVfQgCP8AMaSl7evNeWnXcTK321PS7evBGo7SnjoRNlom5ekzj8q62DO6TYiFvHqEefy4n8_p8jYzgTWdYb2cut-Zno4D00SqRjZZ8WKwdHE8O3OJjTKP7qyjJg0IfCvhuNQbKST5LJ8CaHqNUKFNRnlG9LQaUMqmOW0j0zF0MzN-k6NRmABaQ4OYmmjh3AXziKK3kHbMvBQ7vBn0wVCniwLWyTQnDcdw6KtlXz7H4O-0K5iH9liqQbQoALI4rh94FQDM6LOlaK2zKrUrMOjbQQ4muCYJ8OIdyw9hBh2QaM2wB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !
فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!
اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/21073" target="_blank">📅 19:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اظهارات جِی. دی. ونس درباره قیمت بالای بنزین:
به نظر من، همه ما باید این واقعیت را بپذیریم که تا زمانی که ایران در تلاش برای ایجاد وحشت در حمل و نقل بین‌المللی است، ما طبیعتاً تلاش خواهیم کرد تا در برابر این اقدام مقاومت کنیم. اما به همین دلیل است که قیمت بنزین اینقدر بالاست.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21072" target="_blank">📅 18:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBy8yD1q1qfCOLhb8FVCRHlKZcWcvCNirn5awRDGzf1qa2iIBnYBYVLn_vH1bNE51YxtHdKuL5ETE0-6MuAS6k9o8KzolPpdZOKi3IgqrB1SC8gpX5D9WQj2Ka3zpidQXM0JqV92UoPcCLO5FoekTCl74JJ06oOqmvDpP97RbhBiXaSmwhl4X1Gulfo3gRQtuImzkw1FwGg1NKOX04tXM6l171ZlHhNbCNZA3yFuKEPXEAVOU9vex7Z-Hen53xWD8qVOZFUouu94Z_qUnN8C9X-uPzfapS1qONehx7mY4uZZorYdgyYvTTv4wHthzXoAo3ht6ZBSNOA9EfHXBbOr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21071" target="_blank">📅 17:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21070" target="_blank">📅 17:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21069" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
