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
<img src="https://cdn4.telesco.pe/file/jDFH9e1F1WWYmGaAYELCFkiT1x3VyNUYST8tzWPT_egOpT-6akL1D4jgGCoXBphpxgZLNOznq_CskYKP2XvrAHQCGpjbs29FJ1jmLLeDSwKI4F_ha2h7AR0w-Xdpt_jC04IriuE2WcVcJBP1Dlb6QIKzu_HITf_WhQFMFdvsy8fo1BylAjLcaS1XhG-hdeias2066ZVQCDk9aqg1tdD-6TZ2tJJkChJ90DoqvhjauTKNo7K6rBPfsOQuHD1Yhwxftt4rF6gv1rbJ0XhYrt-VOdRJf0v9C9t4_uC9b09RJpuEPWl5Klcz6Co7Vn1HMws0T0EWaYqafybkxUrAZoxc-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-21175">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/21175" target="_blank">📅 15:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21174">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbBRpDkIG5V3R9odAF7VcleOaB5zXW9hOjPB24w3fQ5ZmRhSxbMC3vC0RT0A_DcYvE8PgPWjsJJ30LoCADa8VmGStL_O669Y4uXZm1wSwV-bqbADJ7MZxxowVO-GbEHXZCFwqnMKj2wHXqQdQ2JjcZqRpPbvYRGUoC4uSJ1UzsDQcCobamoJacPzcsN2NVImk9B8Uu9Rv2EvWxSQLUARK7f4UorGo0DsDUAOjzLyy33V-TlHGFNKuAj7dNILSo-DG1-n9zFplNhxN9iAaOcnYlPZL6YSQsYRj3Ltb-KgCd9-o7L8PCHe_atBvcQMTkWke9MugHz3UI2-_i4gR_xikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس صداوسیما اشاره نکرد که اگر ما توان تصرف بحرین را که میزبان نیروهای آمریکایی است داریم، چطور توان حفظ خارک را که مال خودمان است در برابر نیمی از همان آمریکایی‌ها نداریم؟!</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/21174" target="_blank">📅 15:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21173">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/21173" target="_blank">📅 15:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21172">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کارشناس صداوسیما:
در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/21172" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21171">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مرندی ذوالاکتاف:  اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/21171" target="_blank">📅 14:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21170">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.  علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/21170" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21169">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏
مصادره ۶ میلیون بشکه نفت ایران توسط آمریکا
تانکر ترکرز مدعی شد:
نزدیک به شش میلیون بشکه نفت خام ایران (به ارزش تقریبی ۶۰۰ میلیون دلار) که توقیف شده، بی‌سروصدا در حال عبور از اقیانوس اطلس به سمت ایالات متحده آمریکا است.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/21169" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21168">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=oJXT-JIsALp6jyf1e07TaQdMSwOhKyKpv04-akZ0JAGbyz_Nzk4CCIxf0DU2MvB_dYmtS-f71gilcFYFcs9etiNXW86klz85Mm8FfTFLbSCvt1YJT_G_OJ2owbKyLIQoXX8DUFxufOcT8Uu8rDE_IINqjWXmTtP0Djl-XyER7v7y0rKlOVPBa-dhjz84rQ-j0juObYbhq4Vyo04w6OwvMOfU7Ty-I-Bnd-apVjSNmi-Am7PAgYxOroGR5TxvR_wgUJMJDRqLsHyhJqW0MWbNK4KA7YzYv_t3xpvSAY3TQJk7i0SoP1KXclbL_IQ5qNDbkbwf-G7lQdMO11N6cEvD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=oJXT-JIsALp6jyf1e07TaQdMSwOhKyKpv04-akZ0JAGbyz_Nzk4CCIxf0DU2MvB_dYmtS-f71gilcFYFcs9etiNXW86klz85Mm8FfTFLbSCvt1YJT_G_OJ2owbKyLIQoXX8DUFxufOcT8Uu8rDE_IINqjWXmTtP0Djl-XyER7v7y0rKlOVPBa-dhjz84rQ-j0juObYbhq4Vyo04w6OwvMOfU7Ty-I-Bnd-apVjSNmi-Am7PAgYxOroGR5TxvR_wgUJMJDRqLsHyhJqW0MWbNK4KA7YzYv_t3xpvSAY3TQJk7i0SoP1KXclbL_IQ5qNDbkbwf-G7lQdMO11N6cEvD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.
علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/21168" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21167">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پاکستان حملات هوایی متعددی را در افغانستان انجام داد که هدف از این حملات، مکان‌هایی بود که برای ذخیره‌سازی و پرتاب پهپادها استفاده می‌شد.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/21167" target="_blank">📅 11:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21166">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etQp54QNaQu4fBuGX6XwZ7idXZo0vxmWJkzliQipwtsFeHEGZeUX8vEwWqLUtnOmVWCXkg6MMEAVHv5aPYvnb3Uf02lZegfx70cwGg0KUL6i2ywaScL6SegqFm7lxnDf2Kf2SPAhT0jPAw_k0I5upNkKVuJzr0RNIp66brF8L52XzX1BLhpLKlDBU7_aeWMIUGZ9D95TMLEU5o_0wBWtxWCHjtA8FHB9TeVcNJA7MuJrNAEpi44TLWQfdvB65lwWxR1LGaGVrAXhz_EHYnPLZpVCQRjBZXUzHMhuf_opCmNVwW1uiommgl31NgW6d-WvueR3ijvGTZkBB2iurcZKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف خود می باشد.  در این شرایط و با این تناقض، 2 راه داریم:  — صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230  — خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/21166" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21165">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/21165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/21165" target="_blank">📅 11:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21164">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/21164" target="_blank">📅 10:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21163">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um-3HJgZ6H5HrE9blnTiB2rt1aMByV7hmglS5w4uzaTsWXqx6hzmrReI--0tycOhYN6SO7KRhpzIQLqT6E9UuI8sSLIi1yiZXl643sMNZdk2aQ972OVHINFHcbdBFzd4ng1FXGtNEBXJQl17T1meA7rMk_5pHTZIWg54LzK_8WuSe6pExdKR2GxzmE0MBZGyegPotZGaexhAzBkSZbVplUn3eAia5wP7zkshwRorCVAmho5h1UnGozjOhGY9MZjU-KuJPnWcK9bbT_CyWH2KZVuFI75V9tRW700MrV7S6yPX0UMkFZvMBk8FeBABLUZcXCqkvkwjkDBUqp5XVFEt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف خود می باشد.
در این شرایط و با این تناقض، 2 راه داریم:
— صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230
— خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/21163" target="_blank">📅 10:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21162">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKJ4wRnH2Q5jX5JBjMasZyLTaWrT0Lelo2S7oy4z2A2nPGN138gbSp9mbI_QpATZDG747zHz3DskKq4c3XIMnwa0Hmt70w5ZUO3s7ZHPUDbv_t96GGfcULGc9u5DFrqgijxFsv8oDoG48hqmfk8yDfj_jXjvqL7SkwKetmcHDitxIZ8edFjccbDEfMSqAN6BeCtl5ANgMTR07AbVdGEUSNXmqbKqcTOL95cOD-YA3wYe9B49VMnez5umwYA6omisZSauxP7bg_v4HE6FZD5fWW9Htq0DejpDsh7lzuYXGs361CRL-p5wj6tS3XUa6DghyZx3sKW2Utl4_2Oq-GoQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بسیار بالایی قرار دارد.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/21162" target="_blank">📅 10:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21161">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حملات هوایی پاکستان به ۳ استان افغانستان
نیروی هوایی پاکستان بامداد پنجشنبه حملاتی را به استان‌های «خوست» و «پکتیکا» و همچنین «قندهار» به عنوان دومین شهر بزرگ این کشور انجام داد.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/21161" target="_blank">📅 09:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21160">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مرندی ذوالاکتاف:
اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21160" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21159">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شلیک موشک به سمت هرمز</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21159" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21158">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEi7lzw36nMItqtGIpk9HbfthlpT8MnG4kk8qSolnlSQL3_j2BiRNtgTCbWO4JH6Ii6ak1boMZMXACawGenC_SvvXERazeCAdICRi3M5VoobNS6trYEK2g-ZKP6oHUK9uQfl1WNqw9kX3SUGucBabZBxFql-z-A6QmR6_nPCxHcxKue2_DF1rUkPwPbJO8I9O6Ymn5c-rnos9XeCJedPGFlCnkHUwnhPSZR321fSnvbuMzNoKbwoFHgARXx0MnUjgi72kFeu-Ko7aOjwARG4yPQSbUgyIe6sD9S8z1E5WH8iEBg6O_anzCvAOkgJYiu70wUonQQrrbyni8Zwzjg7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تی وی جبلی هم عجب سیرکی است!
خود مردم ایران صداوسیما را نمیبینند بعد اینها برای اسراییلی ها به عبری زیرنویس میزنند!
باز عربی بود یک توجیهی داشت؛ دستکم بدبخت‌ها میفهمیدند کی قرار است توی سرشان موشک بزنیم!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21158" target="_blank">📅 23:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21157">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بیانیه مشترک ترکیه و عراق اعلام می‌کند که ترکیه بر اساس یک زمان‌بندی توافق‌شده، به‌تدریج پایگاه نظامی بعشیقه-زیلکان خود را به عراق تحویل خواهد داد، در ازای آنکه عراق به‌طور کامل اقتدار دولتی را در سنجار برقرار کند و گروه‌های مسلح خارجی ممنوعه را از آنجا خارج سازد.
آن‌ها همچنین توافق کردند که تجارت، سرمایه‌گذاری و پروژه جاده توسعه را تسریع کنند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21157" target="_blank">📅 23:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21156">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbAVDZ93w51VwaPxnGjnDzFAG3P1TJWbegZv-mWiNPhA-oa39SlHttJ61mT34JCVky6Dxv5nAYCG0E9YuRwRThYsbstAQ6rsJUr_ub1APMB7ASnJcOipSeaxaBRDScMd4ndttH5RkxFxHQYNFR_uXUELZ1th0bjnAP9twV6HN4xi80luudXafMLxdaTZbAR4vSwq9JA7Mi0Tt49GCTdtvdAordjvXLzuUfzZLJhvR-uIyHjqKws7l7I4fN4eI5qjLh9IUp7auHkyk6Sd_KfbowCOdbULNHcqjyWyr2wUNvMVKsC0ck-SvLAU-eLZj6wCu4YBGZ3AFRroYFIYciYWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا چین به عنوان قدرت بزرگ عناصر کمیاب جهان غالب است و چرا این موضوع اهمیت دارد
چین ۸۵ درصد از تولید جهانی عناصر کمیاب تصفیه‌شده را در اختیار دارد و در سال ۲۰۲۵ بیش از ۵ برابر  ایالات متحده استخراج کرده است.
این ارقام تصویری از بازار جهانی عناصر کمیاب پیش از بازدید آتی شی جین‌پینگ از ایالات متحده ارائه می‌دهند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21156" target="_blank">📅 23:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21155">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">درگیری مسلحانه‌ میان نیروهای امنیتی و افراد مسلح در محدوده جهادآباد سراوان</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21155" target="_blank">📅 20:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21154">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صندوق بین‌المللی پول: جنگ در خاورمیانه که از اواخر ماه فوریه آغاز شده، به طور قابل توجهی مسیر رشد جهانی را از طریق اختلالات در حوزه انرژی، کالاها و زنجیره تأمین، تغییر داده است.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21154" target="_blank">📅 20:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21153">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21153" target="_blank">📅 19:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21152">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ایران معتقد است که دموکرات‌ها در انتخابات پیروز خواهند شد و ترامپ نخواهد توانست علیه آن اقدامی انجام دهد.»</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21152" target="_blank">📅 18:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21151">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پزشکیان:   بمب اتمی در اسرائیل است، اما بازرسان در ایران حضور دارند.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21151" target="_blank">📅 18:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21150">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21150" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21149">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21149" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21148">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پزشکیان:
با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21148" target="_blank">📅 18:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21147">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21147" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21146">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رویترز:
دولت امارات فعالیت شعب بانک ملی ایران در این کشور را از امروز ممنوع کرده است و بانک ملی ایران دیگر اجازه هیچ گونه فعالیتی در امارات را نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21146" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21145">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جنگ ایران.pdf</div>
  <div class="tg-doc-extra">300 KB</div>
</div>
<a href="https://t.me/SBoxxx/21145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه یادداشتی از Foreign Policy درباره علل ناکامی آمریکا در جنگ با ایران</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21145" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21144">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21144" target="_blank">📅 17:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21143">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">با این منطق، فاطماگل قوی ترین زن تورکیه است</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21143" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21142">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21142" target="_blank">📅 16:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21141">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21141" target="_blank">📅 16:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21140">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY96bjL5_Clc1DihzRhfjmZ1pBPNrtBAYpIraL7ZxpYNMvw5gBPQOzSJzkIFXybyiDKVqGy-qNB6xobveziNGZ40HHswFqSZQh2O8fLMmH5iqhbXPjBUHnxEKiKkk_JNCEtN5e0HeMqSgqtRFGkGvPvV11kkF__MxTyfzGgcjz5hLpVSbP26sBaitX9ETtfGW3u94_4CRJyv2v0dmN5cFn58V-9IRRga9WFw8HBFIPXjnybOtbaubyGTw-mYirrtgZsksdNokNcY2OXTLYVA1OzPRvGYxkk0FuK4oTbZDvH8XhwEzkhB6f6159cDQNoX1pft7ToyIBmjuBM6zV8HGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باربی های وطنی به مقر سازمان ملل متحد وارد شدند!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21140" target="_blank">📅 16:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21139">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در هرمز و کشته شدن ۲ نفر</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21139" target="_blank">📅 15:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21138">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21138" target="_blank">📅 15:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21137">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در هرمز و کشته شدن ۲ نفر</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21137" target="_blank">📅 15:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21136">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">چکیده تصویری پادکست</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21136" target="_blank">📅 15:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21135">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📌
خروج عربستان از mBridge؛ تقویت خاموش نظام دلاری  خروج عربستان از mBridge در کوتاه‌مدت اثر محسوسی بر دلار و بازارهای مالی ندارد، اما از نظر راهبردی یکی از مسیرهای بالقوه برای کاهش وابستگی به دلار را محدودتر می‌کند.  بااین‌حال، این تصمیم به معنای توقف دلارزدایی…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21135" target="_blank">📅 13:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21134">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juBIJGzDzgqDm57qQHTNj5N65o4Z0K9QxEP0kFGx_gGbqtnQXxDe_8UjI09ag9t7dTsufV8DQdykjQO7xWBFWxS3otJtKNGzXva-IYtAARkTHfPeDHweEtyDzX1Z0UrRsy6k5s1YB8yJD9LW-uHEr1hys1sj0gCeSv991x1s8xvVGezZiDDR26eUGGZuQx0LZgu1qqS6GlvSzkqx-3JnuzL8jNjQBjqHhND8Uc2yykxpcbcEKem6cYOJ2ZmEYanpgJBwc_YQHJvCB2Sj4eCcM3VFPk8RmV6_mirRfAK0LUzoCYCMZg-_pqenUhzhMhAa5t7MfwSz6paYU650BMZafg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/21134" target="_blank">📅 13:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21133">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koLl4FSaGW9YNmhO4hQ1vEM8mVGso2virH_ufr5XRlCUSRv5QKfTgY3bjCPFq0Y4J4YBjI8cDZGjrR6B7-_pfBJgBS5N3unbVIVcEq5di7C4jK3yGJJwggUwojkh7IZ7oXNCdoZA6YWu_C2YqOtsIPcmCb6FhWEvysE9xnXeUKNAJZoLMPK0epFLkxUv7VB-8FlmAJh0zLCbQLGbVpFXSCLgEp4J9o8BkJbakvXn45DCKRXFJHsNEfvgoNn8g_9nS-BbnlgouMZJk5f28k3kZbICviQ-NuqFzalNcOfFod-ck-4is3me3n6aU6lGIP8H7jtxDTr0G-uhhHjJGanSJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.
محدوده  مناسب خرید:
4302</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21133" target="_blank">📅 12:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21132">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzhBplQRjHX4oIR7x_08mbXXfS_08mn8A8tjUAJiL3PUt7Pau8l1hqWvodv6IWGqGwFJJ7hlxgnq8uUXcvxgJo8hdeSSSndI1o15QHNjkyI6Ss4Gudxjg7JRjBj4wTWs7mviylfXr2W53VXO-VJpnfD1zMkjHjOgv90Z5-EompzH4BJz2xW9Abl6KdtDkZs_7EH6ZiScM0_3S3bZjv-yzMnql8rwC017ifUvF47V7wyMfpZPJCkqF_QkXfshqzcd4WFoReL8tlnLyOOH7SHnOb0Cr-TrPssnUl3bAJvLXpyQ5_V_3UR8_BSk7nedd5VAbOk9n16TX6vNO0wHOXzCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بالایی است.
اما طلا از صبح ریزش سنگین داشته و لذا دیگر وقت فروش نیست.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21132" target="_blank">📅 12:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21131">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=sWVb8gpiM2iyP_Y8ZPDUnxddVEhgi1Z6orxTHUuYELWoeQIcDjJJ89Q6L7uBnxceI-9QoChX332yjAmr-M7vxTBx-iv5A3na--9THyyL8r8vz3fE2ZbFJNM0vZ5gNWVlqAqRWOjb87mgcudN5mzXch9ztfWAa_uWCdOD5fJbLO08fPsnu7Cq6VCYUtMkxmj5_a3oXTzDXeWyiiHKwDBXSoJd6TreaAGS9BHvUgIs8qfaQbpb0gkBOPoolbmwpVGfc3oeGUKD7r5wrhZfJuuX70EoKk-fY1OQKXW8UKwjpfUkzI_cC_5c9jQ0wHLN5jJHut1yz6NfOiawrd8jkwFN1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=sWVb8gpiM2iyP_Y8ZPDUnxddVEhgi1Z6orxTHUuYELWoeQIcDjJJ89Q6L7uBnxceI-9QoChX332yjAmr-M7vxTBx-iv5A3na--9THyyL8r8vz3fE2ZbFJNM0vZ5gNWVlqAqRWOjb87mgcudN5mzXch9ztfWAa_uWCdOD5fJbLO08fPsnu7Cq6VCYUtMkxmj5_a3oXTzDXeWyiiHKwDBXSoJd6TreaAGS9BHvUgIs8qfaQbpb0gkBOPoolbmwpVGfc3oeGUKD7r5wrhZfJuuX70EoKk-fY1OQKXW8UKwjpfUkzI_cC_5c9jQ0wHLN5jJHut1yz6NfOiawrd8jkwFN1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21131" target="_blank">📅 12:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21130">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">زلنسکی
:
ما باید قوی باشیم و باید به پوتین نشان دهیم که او تنها در این سیاره نیست، حتی اگر این رؤیای اوست. و به همین دلیل او باید به مردم احترام بگذارد.
متأسفانه روس‌ها فقط زمانی به مردم احترام می‌گذارند که نشان دهید قوی هستید. آن‌ها به ضعف احترام نمی‌گذارند.
طبیعی است که گاهی اوقات مردم بخواهند ضعیف باشند، زندگی خود را بگذرانند، وقت خود را با عزیزانشان بگذرانند و به فرزندانشان عشق بورزند.
اما نه، باید با روس‌ها نشان دهید، باید نشان دهید که قدرتمند هستید.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/21130" target="_blank">📅 11:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21129">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آن دو دیگر (کوبا و میانسوسمار) هم که میبینید ستاره شوم کمونیسم بر بیرق چرکین خود دارند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21129" target="_blank">📅 10:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21128">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">موسسه مطالعات جنگ:
به نظر می‌رسد حوثی‌ها با تهدید شرکای بین‌المللی عربستان سعودی می‌خواهند این کشور را منزوی کرده و مانع تشکیل ائتلاف علیه فعالیت‌های آن‌ها در دریای سرخ شوند.
حوثی‌ها در حمله به پایگاه هوایی شاه‌فهد در طائف عربستان در ۱۷ سپتامبر، یک جنگنده اروپایی «یوروفایتر تایفون» ایتالیایی را آسیب زدند. ایتالیا این جنگنده‌ها را برای پشتیبانی از عملیات‌های دفاعی در برابر حملات ایران به عربستان مستقر کرده بود. مشخص نیست که حوثی‌ها عمداً این هواپیما را هدف گرفته باشند یا خیر، اما حوثی‌ها پرسیدند که چرا آن هواپیما آنجا بوده است.
حوثی‌ها احتمالاً این مأموریت پدافند هوایی را تهدیدی بالقوه برای کارزار تهاجمی خود علیه عربستان می‌دانند؛ کارزاری که عمدتاً از حملات به تأسیسات نفتی عربستان تشکیل شده و در میانه پشتیبانی دفاعی کشورهای مختلف از عربستان ادامه دارد.
حمله حوثی‌ها که به هواپیماهای اروپایی آسیب زد — هواپیماهایی که برای پشتیبانی از تلاش‌های دفاعی عربستان در برابر حملات ایران به این کشور مستشر شده بودند — در واقع اهداف ایران برای شکستن ائتلاف مدافع کشورهای خلیج فارس در برابر ایران را نیز پیش می‌برد.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21128" target="_blank">📅 09:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21127">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtYtEJ04C-Hh0619U9bxARW1BFmzpl4mBBkf7UkTWOMP3stSqmgLNLO-UMeqTFOU0y1VpVsz5VT-IToWPLLtMUuemPUZ8NvW9jYlbvLOuu72XREvJlN_CuEG85KkfJr2oYW3Z0MBtbnxCjQDUQV72EqPGQsubNYTaJVZBZpWGFz9Y6Fa5eREV5wYMAHRxP3IbQrXnjZEIBZ4EgUlGns3d7cAKyt_huA5omN31bzRVk6JUO6TCwAeqXYM3-5cdxROufnn8LPzhygQI5xNa78dgVCoS0SY7RkijU2PYlag8wSOMCfRn8VJPkSA1BJSsktRAnIOlgFlDZQbGmX_vns5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21127" target="_blank">📅 08:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21126">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نخست وزیر یونان، کیریاکوس میتسوتاکیس:
ما در ۳۰ سال گذشته هزینه‌های زیادی برای دفاع صرف کرده‌ایم، اما در زمینه صنعت دفاعی داخلی، دستاورد چندانی نداریم.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21126" target="_blank">📅 08:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21125">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏
سخنگوی سپاه: نحوۀ پاسخ ما به حملۀ جدید آمریکا از اسرار نظامی است
اگر آمریکا به کوه کلنگ یا هر نقطه‌ای دیگر از ایران حمله کند با قدرت پاسخ خواهیم داد.
این‌که پاسخ ما چگونه است از اسرار نظامی است؛ ما اسرار نظامی خود را فاش نمی‌کنیم اما در میدان عمل نشان خواهیم داد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21125" target="_blank">📅 08:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21124">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، انتظار می‌رود این هفته سفری کوتاه به ایالات متحده داشته باشد تا در مجمع عمومی سازمان ملل متحد سخنرانی کند، در حالی که نگرانی‌هایی در خصوص اعتراضات احتمالی وجود دارد.
نتانیاهو قرار است به جای فرودگاه بین‌المللی جی‌اف‌کی، در یک فرودگاه نظامی در نیوجرسی یا فرودگاه بین‌المللی لیبرتی نیوارک فرود آید، که این تصمیم تا حدی به دلیل نگرانی از پیچیدگی‌های مرتبط با ممدانی، شهردار نیویورک، اتخاذ شده است.
هیچ ملاقاتی با رئیس‌جمهور ترامپ برنامه‌ریزی نشده است، هرچند گفتگوها با مارکو روبیو، وزیر امور خارجه، و سایر رهبران خارجی همچنان در حال بررسی است.
بر اساس اظهارات مقامات نزدیک به نتانیاهو، سخنرانی او قرار است بر ایران متمرکز باشد و ممکن است «غافلگیری‌هایی» در بر داشته باشد.
مقامات اسرائیلی همچنین برای احتمال اختلال در سخنرانی او در سازمان ملل، از جمله آزار و اذیت یا خروج هماهنگ هیئت‌های چندین کشور، آماده‌سازی‌هایی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21124" target="_blank">📅 01:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21123">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21123" target="_blank">📅 01:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21122">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21122" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21121">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گویا جلسه برگزار شده و به نتیجه نرسیده!  First Time?!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21121" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21120">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i61mluB5GOtR2HbDXLSMNqjCQJaLyzWxD44HVUZq1pNkmw1Fa0v_De8zlXLgTwtmfBJ3LnMrM2jRfwOcV-0kRty8CfF3cvUme7r9zdsUwkhiiTzH6TJHwStUbcnyaj5HQFq5Q8BeGBxfm58RsOp_Fx9PJ-XX7rDKOWXuqmZhdqeYihHgJK1DZXfE59oUJIe-jfi4Eqe4h2YO8JHk8w-bgIGTJezm1HU8fGnxA4C2qvFeIIVc6vHGFjJSKO55kV1Z2ySoNnH9SxAZij1BXDB9V4cOrcRV9fJfOc_ldbYe5_uqciLN9nx4QWIXeFrzIy5RPMtglUKA8jhm1X6sk_0Qcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21120" target="_blank">📅 00:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21119">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGAj-Qr_shsYOEv7oM5O95d2uNy5o97PUopB-1x41qvt876Bod8Dh0pACKKVGzXtwZUYJVs7_ADaHKfV_MpHxga4uaJ6BOnmOK4ZfP-ac0r8Rm3yypnhqJP2DGZz7lhKMFPgMt8yJnpoZMu75I26QajaPtqzf4XAv1zrcZicrHPms5OF6VaOzgBZhOmb-em7hV5XWWR1Cfhq_jl6aTXxgSzp7uZCTeRYckoDwcTdLxq21TpJTXo8di0ypIsMk9a91-aX7zP8PEkzF2mht9pMGTtocRub4GxUnnrYt7sGVymTGPz2CEcYUzLxxkBAtesfPGWFHAwRuFbUCPC7qi9qAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/21119" target="_blank">📅 00:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21118">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFCAcIa9WvYTD4WIMVO-y8NVZ1tSwGmjLbnqFjHhXq1jjxd_8dod-hDlQjC4HDWYCpb4PBthPpTKGa-krtOXthc9kS6odQW4QUG_8TBVltUnrikp5xfRw4fHdErg23SKb0HOekyLvmoRTVuOx70aC8XGVLO7fh9F0KVoN4IrWJz0z3ugI6VRcPKyJj74LcFcX3_oXQvPTlV9YFM2XsmW6rnUgYdPRp_4SXXRuQ3Jdk-PC9rZ5IhcbbwCEGCLrirYci0ZdMUZRSEX9K97REXJj2Gpao0tS-1UMAMn-bfvxgIdogmo-Ong3n5WXr6PwijznJOA6mN8aWFyZp-pfjav4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUN_CFD — D #SUNRUN  از محدوده ورود دوباره حتی اندکی نیز پایینتر نیامد.  البته هر چه پایین تر بیاید خوب است، این سهم یک رشد دستکم 3 برابری دارد.  همراهان Secret Box در خارج کشور این سهم را دریابند و هم میهنان اسیر در درون مرزها نیز میتوانند روی بروکر WM Markets…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/21118" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21117">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-nZOS_yKJhoWRdHEfJ78JTdBxdpaCyUGZhJvTcJGrivau84_FiET952XhPJ0GRGy6oqcgBQsYnRgMteEdhaqySk3Q8DqpnSc1lDI6SJyETbRSC56AhEVI8uPsqGEdvJhiL05JXreWsQB5mU-3f1te_NSPeekqQ5Q0Gus0Z75ii2qTekG0hafB-GRMuibwqKaiyYoE91mg2N79bkNgnPzGqL4dHnKcZZ3VJvZPrqISoqg42KQNW6Nk-ndQqLWnzsBQoR8Fdk7k0J1Z6ly5nOPhw7AI4X2-lfw1-a6jPSP92dP8MDO9-BSfGHID0ViVbE8AtWEVErGP6JHailFI3ICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL   دوستانی که درباره نفت دایرکت دادند؛  پوزیشن های خرید ما به هر دو TP پیشنهادی رسیده اند و فعلاً خرید نداریم روی نفت.   تحلیل جدیدی از نفت ارائه می شود.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21117" target="_blank">📅 00:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21116">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsWB5x_bfRCnkSAZOKmunK7ygYIsf0pYEFcN29-Pnu3UAccBV5VINPFiBzw2HdXxuRmXN3CympdUKT3C_E-L942pMz8alLvSFskCOSFXvhW53xxh2fGot4mF8TGwf1Ag6Ew1N31YnsDa2Os0DV3aWPdx9JwGzIdQqhJXDICanXpxMqbhQCtiAfNVkribw51OUbZ51oWaERt_RSSsZ-RBAQSxjlqkRtajdpZj5noOWjj2BfmzaDfSG7do_JQqi7g7HJ7da09DqF14kQzmaL43Z89ds-W9y3KarhkzDR_Q9fZ6E8_zuFFoOqNfdNiOvlygbiTmAbz2II534I0heAmYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/21116" target="_blank">📅 00:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21115">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تایید دیدار عراقچی و ویتکاف
صداوسیما:
با اصرار نماینده آمریکا دیدار آقای عراقچی با ویتکاف در حاشیه مجمع عمومی برگزار شد
ابلاغ شروط ایران برای بازگشایی تنگه هرمز دلیل پذیرش درخواست ویتکاف برای این دیدار بوده است.
رفع فوری محاصره دریایی، پرداخت فوری همه اموال مسدود شده ایران و پایان جنگ در همه جبهه های مقاومت از جمله شروط ایران برای بازگشایی تنگه هرمز است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21115" target="_blank">📅 23:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21114">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soJ9Ieat01MZejJZwtxlnIlxVygtrI84OG-f9ttVIxJm6zz4Fvv13k6YRBFMfIBsHQFQaVYVL3b3BB8x9BEqL7i7xfCMmUaAPGkLATjdPTsHl37NHTGy4uKMqyKj0lewy5B3PmuvPJQ5uLOoswFjSdXdP4D4YktR_0LXR9bq3jtYoOBzqZhUThAXaR1gokkdElVjX6yUduz4ftix47w-5TWyhh2GcKb43pLazZLEl8xmM56ovhvqFKL1H95eq06rpRdB9KGT4lHS4OR4kfnQBjWiaE8eDst5n1FFYUABnfRgfCL-0ezZvTDjcfyNaj9eRQvuIh-d4nNOY9SD6jLOAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد بز برای پاسخ به کشورهای همسایه که در محاصره ایران نقش دارند</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21114" target="_blank">📅 22:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21113">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ادعاى ترامپ:   ایران در حال مذاکره با ماست؛ روابط با ایران در حال توسعه است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21113" target="_blank">📅 22:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21112">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLU1viuGuK35Vzb_zFiLLFYXSmFfcpKaZM9m9maEzg2znFuvclafEHHY6gctQZ27Am6ZUR-xlxKI7XKk9WsSvCDq4r8aJNT9HtG8wQR-DwhQ6_hQljkj2ZwU121TM9QWyXCegyvPsOwQNKQfewbPnoF7KYly7qdw_1uY-XdwnM8mBz8MwSziCZ4-eGXwWeXCb3hjX-BPjVZwAnvga5SZaJzciB4ENgeiAr1q7hLE6BYWgk0BfEvGymfUm-fHUxUxJnhMqo5aJuTC3V1aJiRQpDq8OQpiVRzg4T1C_VcnOUbBKAFbj0RYPEG6BDsdMgDNJxQvD5lOs7TkiZHoD1jhscs6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLU1viuGuK35Vzb_zFiLLFYXSmFfcpKaZM9m9maEzg2znFuvclafEHHY6gctQZ27Am6ZUR-xlxKI7XKk9WsSvCDq4r8aJNT9HtG8wQR-DwhQ6_hQljkj2ZwU121TM9QWyXCegyvPsOwQNKQfewbPnoF7KYly7qdw_1uY-XdwnM8mBz8MwSziCZ4-eGXwWeXCb3hjX-BPjVZwAnvga5SZaJzciB4ENgeiAr1q7hLE6BYWgk0BfEvGymfUm-fHUxUxJnhMqo5aJuTC3V1aJiRQpDq8OQpiVRzg4T1C_VcnOUbBKAFbj0RYPEG6BDsdMgDNJxQvD5lOs7TkiZHoD1jhscs6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روند ساخت اسلحه های دورزن در یمن!
با همین تفنگ های دورزن، حوثی ها صدها نیروی مخالف خود را در هفته های اخیر کشته اند!
ثانیه 29 جالب است. یارو در دهانش قات می جوود اما دارد اسلحه دقیق زن هم می سازد!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21112" target="_blank">📅 22:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21111">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خاویر میلی، رئیس جمهور آرژانتین:  نسیم‌های تغییر به نفع ادعای ما در سراسر جهان در حال وزیدن است.  اخیراً، رئیس جمهور ترامپ اعلام کرد که ایالات متحده در حال ارزیابی مجدد موضع تاریخی خود در مورد جزایر مالویناس (فالکلند) است.  ایالات متحده در حال بررسی این تغییر…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21111" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21110">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=vK7PPlnQEUuLSB8yW02NcXtybMWQ8HzwIzsBZ3mmzj3RzvvN2_pR_GOwScFWIQprWE-YO7BGpd6P33C8XPgfutk8Ov4hsNQkFK01I185PAHdG33AHujCm8S1V1PymuTLDn-TYVcMvYJYS3kDPPh6mABORkirtOAA219u7Yhz6bBZzyQxWfG5Nc99LMjh_czhUVOZ0guUhWrl2y_T5Dwj7Kw9nnWKbeT2piLCakot79O3DXNOdkf9Nglz3PLYLPYGtLBhYjkhaGmoGRRqbOEMsH6ZdcuoK9M4VVoj-Eg2d-d-Wa32Ij8nYaL9nMb9QDrxZdDFsw4ejFq8KKDI_FfQlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=vK7PPlnQEUuLSB8yW02NcXtybMWQ8HzwIzsBZ3mmzj3RzvvN2_pR_GOwScFWIQprWE-YO7BGpd6P33C8XPgfutk8Ov4hsNQkFK01I185PAHdG33AHujCm8S1V1PymuTLDn-TYVcMvYJYS3kDPPh6mABORkirtOAA219u7Yhz6bBZzyQxWfG5Nc99LMjh_czhUVOZ0guUhWrl2y_T5Dwj7Kw9nnWKbeT2piLCakot79O3DXNOdkf9Nglz3PLYLPYGtLBhYjkhaGmoGRRqbOEMsH6ZdcuoK9M4VVoj-Eg2d-d-Wa32Ij8nYaL9nMb9QDrxZdDFsw4ejFq8KKDI_FfQlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:  باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.  از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21110" target="_blank">📅 20:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21109">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21109" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21108">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آکسیوس:   تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21108" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21107">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آکسیوس:
تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SBoxxx/21107" target="_blank">📅 20:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21106">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:
باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.
از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت بشناسد و روابط سیاسی، دیپلماتیک و اقتصادی با آن برقرار کند.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21106" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21105">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !  یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21105" target="_blank">📅 19:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21104">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=mwrXPMKX_FsHKYqxluAv46bGIjo2MeFxb5Zilwk0JvEjkDkGVS7IztTnR6ExxY-6L2eSenpBOvAf2rT-l85s_vzpT36x6yyT4zTDD7joRc5IOBUKZJ8gebdvbO4E5SK1vRiNH7NR1WQRiufGBu1rR-VU4Qzn9Q2gxoJfXaUOi_ghd3Uq9Su-K2AdViDdAs8te3ajD_Tcoret-yO7nAerCeKTqYVmDxmp9XTItKG-HKutxdiLYMD8Hnzrz5SopEjJKHth1Z0owz0Ox1Nr26GmXCAyH8C10SvgbSsNt6WsBBlnzcLLQCD4Cx016CuzLXJsRlqH1cdHBjkD9Ep-K1B_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=mwrXPMKX_FsHKYqxluAv46bGIjo2MeFxb5Zilwk0JvEjkDkGVS7IztTnR6ExxY-6L2eSenpBOvAf2rT-l85s_vzpT36x6yyT4zTDD7joRc5IOBUKZJ8gebdvbO4E5SK1vRiNH7NR1WQRiufGBu1rR-VU4Qzn9Q2gxoJfXaUOi_ghd3Uq9Su-K2AdViDdAs8te3ajD_Tcoret-yO7nAerCeKTqYVmDxmp9XTItKG-HKutxdiLYMD8Hnzrz5SopEjJKHth1Z0owz0Ox1Nr26GmXCAyH8C10SvgbSsNt6WsBBlnzcLLQCD4Cx016CuzLXJsRlqH1cdHBjkD9Ep-K1B_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !
یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/21104" target="_blank">📅 19:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21103">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ:
در ۱۲ ماه گذشته ۱.۵ تریلیون دلار در ارتش ایالات متحده سرمایه‌گذاری شد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21103" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21102">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک مقام عراقی به الجزیره:
«به فرودگاه‌های عراقی اکنون دستور داده شده‌ است از فرود هواپیماهای ایرانی، از نیمه‌شب امشب، جلوگیری کنند.
اقدامات انجام‌شده علیه هواپیماهای ایرانی مطابق با تحریم‌های ایالات متحده است».</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21102" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21101">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21101" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21100">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">— مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ترامپ آمادگی دیدار با پزشکیان را دارد، اما باید بدانیم که تصمیم‌گیرنده نهایی در ایران رهبر معظم است و او یک روحانی شیعه افراطی است».</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21100" target="_blank">📅 15:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21099">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21099" target="_blank">📅 14:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21098">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سخنگوی سپاه:   اگر مصلحت ملی ما ایجاب کند که در کنار جنگ، مذاکراتی انجام دهیم، باید مذاکره کنیم</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21098" target="_blank">📅 14:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21097">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21097" target="_blank">📅 14:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21096">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/SBoxxx/21096" target="_blank">📅 13:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21095">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">— شرکت هواپیمایی ترکیش ایرلاینز، به همراه پگاسوس و ای‌جت، از ۲۱ سپتامبر تمام پروازهای خود به ایران را لغو کرده و حداقل تا مارس ۲۰۲۷ هیچ رزرو بلیطی در دسترس نیست.
تحریم‌های «عملیات سرد اقتصادی» ایالات متحده آنقدر گسترده است که حتی هواپیماهای ایرباس حاوی قطعات ساخت آمریکا را نیز شامل می‌شود و برای شرکت‌های هواپیمایی ترکیه چاره‌ای باقی نمی‌گذارد.
شرکت هواپیمایی ایرانی ماهان ایر نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، گفت که خطوط هوایی ایران از ۲۳ سپتامبر با تعطیلی جهانی مواجه خواهند شد و هشدار داد که شرکت‌هایی که به آنها خدمات ارائه می‌دهند، ممکن است در معرض خطر از دست دادن دسترسی به سیستم دلار آمریکا قرار گیرند.
ترکیه یکی از آخرین مسیرهای هوایی بین‌المللی مهم موجود برای ایرانیان بود.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21095" target="_blank">📅 13:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21094">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21094" target="_blank">📅 12:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21093">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9yF4ad862ku5LtYNi-r2qA1fAVtE7VUIso2aIfBuH30pl_0d3SJD9uPBgRL4Cf_LYmviWQOjdXq_dao0x6kUNLVfZrK5XZfQ9CJl8vfwA-efjvx4htLbxbXgmVi9B8LGO5Z6SzJ2RkCbXN06qVxF_HycXGcvIVEBdmr4dY05Szy3vByQelVKRLcptcMZwYMCIYetENVSHwQPE-QnUJPn5Ceyoy2Wf9MVI7uRg_Y283R4ZeknjJRAMIFetDUI6UxXE7MIYVPKTyW8tCx_4fdSRz1G8zg1Hhe9eRXSxrS-MlxHSevyoV3zFGaVQWZcgA0PZj1yzkxI3k3xtzzaT1tyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21093" target="_blank">📅 12:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21092">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX8fP7d3X5jhVp86jPJBy94iwFokOzClt0ewsTTt738-zUu5kNY1Z_FE81x5fVTFNFINQ1bWKYnGpLVn3DV9YldG_3Ku-qtjtHdzAa8jG5QM7D-JZR77VGL3DMDn8sA3os7cjR3zBjdP4wVUOlZo3XPrR5XXFAGzK39qOjYjOg8YMmCfLDI-haQZObSNzMBSJ7qFgPuajwr1iDyx2wHxLIACuBdBGNf9dbxLvblj1vxzNPXEyuVGfyiC5990dP-f0amuraZxho4X3uwaPI0cGacsVKsxyiKrAFTMxWIqUodyTcRsb09zMkhj5m494gf9i3LR_NQGWD5bQJ4I7lYQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه کله پوک پیمان مکه کم بودند، حالا وزیرخارجه مصر فقیر (خر دوم از راست) را هم با آن ریخت و ترکیب ش add to group  کردند!
فقط سیس هاکون فیدان !</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/21092" target="_blank">📅 12:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21091">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwCfDfvKxKVSbn_mNhR6ew3DJunDrFRj8ExrMKxr6kPtF-tRqcmwrqpXoZmkZEwIHnW2nIvRm1VhMabHVVDABVuCvpy8Fv4IwOTwmczGMD5-GIbY9c2g2nG6pFCr-kArzJIutBI0aSBaI42KAZBil8Xg2mohDuCJMp7kjB2bmjzpOQFW5bjhz00mQjlHA1tNHv2bpKef33b0fZ2N92Y4K5TMbUo9zSbkxXF1MQ5ox3ikk84liq5tTHwXay3U1c3MxDbT65pnpZP37NA26Kx8XatOg7n-LqeL8LLh0Hm5EdFzYNYbNFt_Nx5e8E1b1gz3WHx5kaQ0E7ThJPq4DwPT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/21091" target="_blank">📅 12:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21090">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/21090" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21089">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/21089" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21088">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21088" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21087">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21087" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21086">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiytMIXRxPxw924AaA8qPXh_kyKUFsPJSkKbEiphCkte3nY3b728TIMcdftuvmwpqO33DY2A_gpn0ncOdaTplMnH8A3h5OFeZ9gFMbtdCWN0wn5E3Aq1TZiivpI2_TMHyyiOrofRb1feRiPrO1dPdUnp4F1R3nTM-1aah2Zw-ZbQfrGgQe7a91tv26cBLKZJmNSYQgzljHDLhvvyISO5U3UI1ZOqJzKhPjxsUGCX6k5zDz082oym3mql-5yYPQN4oCqVWKmXjZGGgIF7rIlzuGdAK6QJqrCcN9y1ceYZXcWRR9QM0xOcVrTNPO9Oyy3us2XE8QUC3seOje7jQKp1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21086" target="_blank">📅 11:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21085">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1MqOl6JvPMDaSBqSI8aWYJfOelzX2efp_FB0YM26LUai1Oi79woJ0EVhoBHMpudv6P_uHfpB_1saiu5FdjYo4Qt1TGHdZwYA6cqvbXN5Zo290Oig39cm0XgCBRvmZFe4u3kKfDWp5RPrsCLXWolcHxjArbxjLp3KBG6WExTwySV5f_QhsKZ0AitT_M6GyjVbKSRmRYNXXJb1NWZEnJGtafXyfCRqtvUuepCC7Ter5MG4SD6DtCJdsxl4sa9fjTcEHJrvMI1f7W-MR5RW50hjU4izmyo7nPppXdKeC22iFqfq9DYUlX3Tl75MrtV9sWRPfBzL6p6tXlD3tsp9agWIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است. اما نظر به ریزش سنگین طلا، اثرگذاری اش را گذاشته است.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21085" target="_blank">📅 11:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21084">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EULZeV_nO8JV8SyCTA9zbRWHQuuDj2P0jM19Cky1RmkjvAR-T6ruMCyCuoAfdFE5r9SBfozTrCXGiCyw90gZmq9VtNP-569fd5Gu2qbjyF-9bay5ktu-gCCIJmgX-6kV5vFoUWBKXibRPC9VAbNMfXKMmFITwUaNKuqd73Ja5Uxwjug5C0LEP8ztigPUDJpsNrsQZ3h-1outXD2SUVhHZHfHTB9_DW6HgpyflTb_CYmbi7Umo0ipsWrCJvjUTeLVuE6-sIpbUv4nNow5fuJ_L5hW7zfLRkLfgElGkO1rvJ2rWVOTl6iJM7pgt_75rU-eRXLjLWY7A1O0lTS4EkAqzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پله خرید طلا توصیه می شود.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21084" target="_blank">📅 11:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21083">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کاخ سفید، پخش ۲۴ ساعته‌ی «کانال تلویزیونی ترامپ» را آغاز کرد
!
کاخ سفید، پخش مستمر
«کانال تلویزیونی ترامپ»
را از طریق یوتیوب و پلتفرم X (توییتر سابق) آغاز کرده است و وعده داده که سخنرانی‌ها، اطلاعیه‌ها و مهم‌ترین بخش‌های فعالیت‌های دولت را به صورت "به‌روزرسانی لحظه‌ای" ارائه خواهد داد.
کاخ سفید در پلتفرم X (توییتر سابق) اعلام کرد: "شاید همه لحظات مهم در تلویزیون شما پخش نشده باشد، اما اکنون این امکان وجود دارد."
کانال یوتیوب، این پخش را به عنوان
«پایگاه اصلی»
معرفی می‌کند و وعده می‌دهد که مهم‌ترین لحظات و بخش‌های برجسته دولت ترامپ را به صورت ۲۴ ساعته ارائه دهد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/21083" target="_blank">📅 11:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21082">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBABDLnBE-eSjoN_wKOiRBNB5DIgmeXrNG20zbVnwARoRL8gqVYMTb6QsPMHokMTgJm8ZU4-P1_rPAv4bzrJDxODKfwWnErFdofe5v1wTE5LyzFoE7mfmCn_39CsjOdA6buUanwQcCzVLnc2wLBifKGXcz6FIFIyyE2KGFV53yAJ0cpeFVKKbQN_xUjp1-YXhntWfB3HSis_6CYXZn9UE4g552L2AuGmJ-O8ZQr8Vr6GtS1KzqnN8RAe2qBjBGjmnRFDHBL11Rd56olPTGEKjFgdu25ITaCMlhWUbjwEqjJ1PNandoaJEowwtVlRX-8io4mx7cwZFisxfZemFD5EkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21082" target="_blank">📅 10:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21081">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sedy_BN162LzHHxp1AYieJPQrOPOiMmeAgPZ9wZ_A5fRpllI8PUHn5YwalsODgxYO-RjY1qOP-MqrdKuvpbUkEM47M1x74A5ze7p2yrWk8V6KCaFuzJGUpXHCHqAcDW3TiUinDfmUyfpmJg1zMrhKUoYDBK6mpDmOtS3F5WAIn3DO7e4BAC-x05Kus60b1FFTxb3v15p0vIRMgD9U9vp9xlVvEzS23Qbx_GzBrXTpjnvAbCwBgrW72-GaI_wJNPF8P4zfgcCvIEy5yswnr32x-8ElvO1ZxqjAuBBBbWpZkWTZOK5_g_jG67WDiqVGUpRI1AWATmrTtCu9hX1N2yw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمونه ای از جامعه ای سرشار از زور و ریا!
حجاب اجباری بر سر دختر می کنیم تا در بلوغ و بزرگی محجبه باشد اما همین الان مادرش بدون حجاب است!</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21081" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21080">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
ما آماده‌ایم همکاری‌هایی را که با ایالات متحده در حوزه‌هایی از جمله انرژی هسته‌ای و LNG، حمل‌ونقل هوایی مدنی و فناوری‌های پیشرفته برقرار کرده‌ایم، گسترش دهیم.
توسعه بیشتر صنعت دفاعی — که به‌طور سنتی یکی از قوی‌ترین حوزه‌های مشارکت ما بوده است — هم به‌صورت دوجانبه و هم در چارچوب ناتو ضروری است.
ما می‌خواهیم موانعی را که هرگز نباید بین دو متحد وجود داشته باشد، پشت سر بگذاریم و شتاب تازه‌ای ایجاد کنیم.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21080" target="_blank">📅 07:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21079">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlqYoEaVql13O7Gm_e0O2OBG8aldBQZZT9xPXsWmUOoiFCvNKzJP_NzW2AHM1BgCzYoGSq8x318HN-GUYjtGAhzSRvfjhPD_JjBLg64hCfrQvvii4d8gFLrhVfLKOJ3pMuO5Wi4rhvhhGd2MLRqHN3iBl5CxFbv4r8Pj4hQTnJM1T3uZaY7OHIUPzNI6KsIrp3jI-Dl-ckSanyucI-j5T8W4gHS4csBQxl0Wy_J6mitaCZtBO4k-A2y4mndQN-pLEO_UFXtG88nl2ZeeWX1ReyPTGnE4-4IkXcnXSFU4YepMtyJY-FecXkxgZTT5dsdyF7suyDKBsy9XOC2r4pI75w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21078" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21077">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21077" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21076">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21076" target="_blank">📅 22:07 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
