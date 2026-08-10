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
<img src="https://cdn4.telesco.pe/file/QY_HU2Yya9aMPyMnYzbNS4r6mShy8fDFDAzZng6aOkZmFv8h79511l63oGc_309f3nwCu-3SuB6AYW6vGKlHUPpJsGhuKYo34PC2FvNMrzC7MZWk8kwfZZ0HSDwaj1iA1KPtIySxiZqRUo_wmy0yccCMxxRxONg13ZaDsv6ZdyMS5iHAXYlWsDKeCTD8aXnnFfMeaKVHMDL0gv9f4WchFkngDHRXRB8TesR5cYI44K4FcoieOAJBRGMvXSVDSrNn19wFXTO7U1uHbbGzMLuHROnu7w6dPsXcCoFgNzDzuoXe4j0CUgEDtUnsElDdW8alkzUmr1Us7QlPFpOMeWnFgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 446K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 11:51:28</div>
<hr>

<div class="tg-post" id="msg-20763">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مقام ارشد به کانال 14 اسرائیل: بزرگترین ترس دشمنان ما این است که نتانیاهو در قدرت باقی بماند.
خب،این به چه معناست؟
نتیجه بگیرید.
@WarRoom</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/20763" target="_blank">📅 11:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20762">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مهدی محمدی ،مشاور قالیباف :  ترامپ با ما توافق نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/withyashar/20762" target="_blank">📅 11:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باراک راوید ، آکسیوس : یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «نگران یا ناراحت نیست» و آن را بخشی از فضای رقابت‌های انتخاباتی در اسرائیل می‌داند.
این مقام آمریکایی گفت: ما نیازهای سیاسی بیبی را درک می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/20761" target="_blank">📅 10:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbdnkiPypyzW1X7nmigqC-Spe7qLULSvK62UlbU5ljhYHokmAghE086lAuqqlTivK7Gk31SulN2sLyAD4iqD3nWK4vS10Zn1T7gEp7gzXh77lI5FiLg-Mo20720X826LOWtSj4VTO0oEpIprAmJRgOXr4vJIFdNEUKZ1r-Tjm5xb0WxeZqS6Hs0YOFX-Dzjy5Kq1wf7o_Inr1bm2_xJecB-s3LFv2hM6KW_NWFRshsa7uuXz1fNk6jiTE4zMUUToNDzZqiTa3MufVyxTJDXDZgRlIpBOKw21T01tsYLpYWZGbc7z1k-zvR2LfT2FfF_yoEiWfT-jcbgo0WSGfrkvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیز نیست، بی بی داره خنثی سازی و بازکردن ورودی های تونل ها رو براشون انجام میده.
@WarRoom</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/20760" target="_blank">📅 10:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">مهم نیست داش یاشار مهمات عمل نکرده دوران هخامنشیان هست</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/20759" target="_blank">📅 09:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20758">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbdiM9ET-ozVfpvEoltD6osL6zNo7b7Tco6BoPDhEPSUDJmIZQ4zKMPrGjGTk_UeMqD-M1Yz9vfKTziqSQS1p-D-YLXW9ZMpb41bpgtS9Vt2r2Od0Veymel6DaZU9tDWAl4LPaqhOIdaznS0O0KEPNqvqVII0XJ3H4JlL57RRY--HhhMGtoHZBBlwVPLIce9_4KLHoNrFqtBHNN3C1gMt3glEZTzEHVKCXGnzBG3SSwfU5JKWfGHVSOmXh21OcMfYsgr4dHhOdvxhTdQzqXFzrb8IkcCW8Yrml72ebkIx0Qgg_gDPS8ma_z9-9n1_wm1k42HpXWHEdTjUikp_CNidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان سمت پادگان ۱۵ خرداد انفجار جدید
@WarRoom</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/20758" target="_blank">📅 09:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20757">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtR7PoNHNRby1sGsYrPGareZ3ZOKD_hc3TCHK1TgYpBwGg7CTV7CKSb8E1UYCdBz-FkgWw8aJ8-76CUhojA1CJIj-oWSH0cG5txmWWwor2F0x7qTrFB9yzJjBU0ifTPRQm53yOuhZvbGNhalutFcO1FFebKw5eLFiZ-LKkEvrglSr0241ync24ujGCiPOIOV9xyERP9UAP4p4t8bqRT0BlQQ_bVs57RPidnHbE-s46cKhSdbHki05cjlNtKe-B5XVanPKKuCMhhE5x9NjiQl_CszWPNCjx-h6xL1NLlRoeEfON90KGPToBuEqJhE4PQNh6xHjoCNSuZZ39fNkio6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو انفجار شدید در اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/20757" target="_blank">📅 09:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0rGoUSc-VshvLifn6LO-ud2mTsUSIGMzY8T0OrQZbULoByjuAQPVwEN458VUWqu-LQHvlSQfHX9F5ro46I7on11XqkOXujtvns1hAvjeD0p0mKPA87e8CrbPaGNGDQw2NxpOPJ-N_VkD97KUV9be9tvJLzbzp4vvdl63UJbNV0MpgScSVbCxURzk_nClqL4qx9ADqeDNp8-tUOtxQl45DChpUXoZM8yfn6sMLdDUW8-EhN-sYDOA3G0_MdJDMsFgT2ZJ1N7emsAwsfZULpd201ry-6zUgHeZnUL-LgYtyMw74Xd0BKq0TXWtVLMDUeSe3uP795A42lUX6OuvMBcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز : زیردریایی جدید «روز قیامت» اسرائیل که با هزینه ۶۳۴ میلیون دلار در آلمان ساخته شده، توان بازدارندگی این کشور در برابر ایران را به‌طور چشمگیری افزایش می‌دهد.
این زیردریایی از کلاس «دلفین» است و شرکت آلمانی «تیسن‌کروپ» آن را ساخته است. همچنین، این بزرگ‌ترین زیردریایی ساخته‌شده در آلمان از زمان پایان جنگ جهانی دوم به شمار می‌رود و به جدیدترین موشکها مجهز است
@WarRoom</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/20756" target="_blank">📅 09:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4468b68072.mp4?token=MojkgO7b7T385qjP8Mrn36Pe-qXJriV8N4B1sUuBV7JEYUOku5B7rh4b4NF5qgD32pcaVforNTYnO7FgZwIP0DAWZIghl8NBhW-vhrLCOJZbeNqyEi7Xa4HpMgrvImMcRWjjhJ2GwuWOopR9O6fP0XfxO9cMbLKeYkN1HBqreoZBJC5kA10bvUDvhfOKNWewgW6zAu1QMSFtSNq2heQT5JkTsj9y720onF2Mzv8QG_pCIYw3lzPdt8lUMbT6ApYoRI3Nuo4nU_zs5LsUBb_GGiWd3wAFqtyG7hY---45EXcMSTqk5G8Ur34VtMtrgUuhhrZ6Eq8iz--GJMY80-05QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4468b68072.mp4?token=MojkgO7b7T385qjP8Mrn36Pe-qXJriV8N4B1sUuBV7JEYUOku5B7rh4b4NF5qgD32pcaVforNTYnO7FgZwIP0DAWZIghl8NBhW-vhrLCOJZbeNqyEi7Xa4HpMgrvImMcRWjjhJ2GwuWOopR9O6fP0XfxO9cMbLKeYkN1HBqreoZBJC5kA10bvUDvhfOKNWewgW6zAu1QMSFtSNq2heQT5JkTsj9y720onF2Mzv8QG_pCIYw3lzPdt8lUMbT6ApYoRI3Nuo4nU_zs5LsUBb_GGiWd3wAFqtyG7hY---45EXcMSTqk5G8Ur34VtMtrgUuhhrZ6Eq8iz--GJMY80-05QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در واشنگتن دی سی، در پایگاه اندروز فرود آمد و مصاحبه ای‌ نکرد که به نظر من بازی با رسانه هاست تا در خبر های‌ زرد و دروغین خود غلت بزنند تا غافلگیر شوند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20755" target="_blank">📅 02:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOO1UJq98eMOL6OaHLXOz6X9yPj-kdW16h10gSkxyOyMUUF8Mfw8223zYgPOUqP0CBI0vbCkjJEsIfqfSU2T-Uajyur-FspLmhDUlKyZIEpKMbrTIWVJMg1bcqUQq6zzOzB-cLW5NOBQ1x5cOLKcnkYVAD-SyWzTuzhTQGsvynjS6RaEc9esi7_l6--pAwuvgsWQJJYK26wue0tP72WYag5GZoLWYgNOKjkDCjZ1wNlEAVltn8Ut0RJ5HOMo5BEzrmOpYS4WC9w5MQX6d9wEHpZJIEMuEkl6W5yynZR5Ea9LMAaq4wjCIChc_z8CwsQv64gsS-j3fna92A_kgBahFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : تا اینجای کار امشب در حالی که در سراسر خاورمیانه آرامش برقرار بود، در ساعات اخیر، حکومت ایران تعدادی موشک به سمت یک کشتی که در حال عبور از تنگه هرمز بود و توسط نیروهای ارتش آمریکا اسکورت می‌شد، شلیک کرد. سپس، آمریکا و عربستان سعودی تعدادی…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20754" target="_blank">📅 01:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اتاق جنگ با یاشار : تا اینجای کار امشب در حالی که در سراسر خاورمیانه آرامش برقرار بود، در ساعات اخیر، حکومت ایران تعدادی موشک به سمت یک کشتی که در حال عبور از تنگه هرمز بود و توسط نیروهای ارتش آمریکا اسکورت می‌شد، شلیک کرد. سپس، آمریکا و عربستان سعودی تعدادی پهپاد به سمت جنوب ایران پرتاب کردند که پهپاد سعودی توسط سپاه رهگیری شد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20753" target="_blank">📅 01:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20752">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8M-sgXArjAkJaHjibnBPDrzrP0GC9_vNg-mvwb-F7hAaYx7uTYnrBwJlaxzrjg3-XnXJI7PlYXo5llJnqe8BaZb-BDfUcbod2Cxrj_RMC8Ys1gBTvFhe0geC6tPcELBfb8ZA6AAosMvZJz7G_9dKPpbQG4lj29QgxXHxkgYfraQDp538x1q0Se3fuQ-c161QnrAyjAgOrW0jgC_CbLpCrYZa-qUSR9u94i7LaR9k8T_k93SAqGKPZeATQXxNL-87L7-u1N5icBpkqTNhlT_mrL5DjKP_Ra3ey_q56m1QPDgTdVNEEPzEXWhoGPIEugCPSd6mLpK5ABLmzqD_VQ1-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام :
ملوانان نیروی دریایی آمریکا
بر روی پل فرماندهی ناوشکن
USS Ross (DDG-71)
در حال نگهبانی هستند. «راس» یکی از بیش از
۲۰ ناو جنگی آمریکا
است که برای پشتیبانی از مأموریت‌های نظامی در خاورمیانه مستقر شده‌اند؛ از جمله اجرای سخت‌گیرانه
محاصره دریایی آمریکا علیه ایران
. ما، تا
۱۸ مرداد ۱۴۰۵
(برابر با
۹ اوت ۲۰۲۶
) نیروهای آمریکایی
۵۵ کشتی تجاری
را تغییر مسیر دادهایم،
۲ شناور
را از کار انداخته‌ و برای اطمینان از اجرای این محدودیت‌ها،
۲ کشتی دیگر
را نیز مورد بازرسی و سوار شدن نیروهای نظامی قرار داده‌ایم
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20752" target="_blank">📅 01:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بلومبرگ: توافق هرمز همچنان دور از دسترس است، با توجه به اینکه ایران از مذاکرات مستقیم با آمریکا امتناع می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20751" target="_blank">📅 01:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20750">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20750" target="_blank">📅 01:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20749">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">روزنامه کیهان : اردوغان و شهباز شریف مثل روباه مکار و گربه نره بن سلمان را سرکیسه کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20749" target="_blank">📅 01:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20748">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead9f1f71d.mp4?token=CxE7JXE6eZzbk2bWgXhtCXLrmiYA_QnisgnSg82fy_eYPdqaltcilZrfaeRQKxkyUL-qHhjYtWvPBcnDrbcBCEpn-TdIy2O0yp-qIjQfPib798TsewTwkAmpQTWNgtBF9uhOsZ5RFAsPQeF2feYdZkZoWZx2SHiHEFoYHP7janaFgZBc7xqxDG2I7GQQkhkcuAN8hBFZ43SfyUzfOyvJ3ZtFV_39KkB1TeQPUNCdr7gGYYanuUPAKJBhe116zCD3ND1zhZ0RwIwHDZXSe9ExoJaz0N-uAGPIf3yYL6vStXf0h0GcVLd6CzCeaZHpRVpiczoBnYrWFyXCnNQ0V4X8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead9f1f71d.mp4?token=CxE7JXE6eZzbk2bWgXhtCXLrmiYA_QnisgnSg82fy_eYPdqaltcilZrfaeRQKxkyUL-qHhjYtWvPBcnDrbcBCEpn-TdIy2O0yp-qIjQfPib798TsewTwkAmpQTWNgtBF9uhOsZ5RFAsPQeF2feYdZkZoWZx2SHiHEFoYHP7janaFgZBc7xqxDG2I7GQQkhkcuAN8hBFZ43SfyUzfOyvJ3ZtFV_39KkB1TeQPUNCdr7gGYYanuUPAKJBhe116zCD3ND1zhZ0RwIwHDZXSe9ExoJaz0N-uAGPIf3yYL6vStXf0h0GcVLd6CzCeaZHpRVpiczoBnYrWFyXCnNQ0V4X8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پهپاد ساخت چین که توسط نیروی هوایی سلطنتی عربستان هدایت می‌شد، در سیریک، استان هرمزگان، ایران سرنگون شد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20748" target="_blank">📅 01:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20747">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بازهم صدای انفجار/پرتاب از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20747" target="_blank">📅 00:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20746">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dg4Aa0UKH3LGUtXtlmlagJibzOep1kI4-tf2Jt19dnU3bTdI4Z6CaOHL5rtaNB3LjjiNdbaviP32whshZs1KuyTM-w7SIVuRUSlaxlCPJA3MFMRFpnbnRPi6yHYkxSnY5pZy2SpYrBezAxKusbDTcWEj_YPsPuyBvMyP4RKX35_ohI5YqsoNyussBYdYUiFjWRpROy0io50b-bYuAuzU8iAqaCZlJtfw22ezr68oSV7d1dVAlwfjToVc_I-3Q9hdeSqOJHSq1fLeMS8yJQaxvSbK3a_cEg0lXFoy-3yqP5bu5BpDYzID573hNdCRdob5YfLBXG-AGvtI-DjUolVuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث
: 51 سال رفتار نامناسب ایران!
@WarRoom
حالا چرا ۵۱ !؟ ۴ سال آخر شاهنشاهی هم قبول نداشته ؟!</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20746" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20745">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766d8dae53.mp4?token=V6cN9wIewMThXBG7U5T3oY6lam92xb1lx0mHgbbdsmkAh64uOo3jSTlYMeluEWmwHZbM1IEiCaQbTzmiw4bkWh0Tn0pCRkH5Egy2JGObPBaDmZPU2xVE8nlToIzMM8I-61fb75IERa-7-z_PIZgweDr9KYpBLr4boPDeGlgaBmsiODIYLSy6ZnTO3GFUP7FI79oev3Gqx8GM19k9S9UOCXmbQU6DsnJog9sYJSLvM_5COSAI1-sZMl4X66bS68-GdxNOqPS204E-yPrNpVALuWkTu4hgLUyQ1yXkK09oQzo1K4bH1DDV7N_F1pe8EkQ346icklTLXcrHH3G38s37BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766d8dae53.mp4?token=V6cN9wIewMThXBG7U5T3oY6lam92xb1lx0mHgbbdsmkAh64uOo3jSTlYMeluEWmwHZbM1IEiCaQbTzmiw4bkWh0Tn0pCRkH5Egy2JGObPBaDmZPU2xVE8nlToIzMM8I-61fb75IERa-7-z_PIZgweDr9KYpBLr4boPDeGlgaBmsiODIYLSy6ZnTO3GFUP7FI79oev3Gqx8GM19k9S9UOCXmbQU6DsnJog9sYJSLvM_5COSAI1-sZMl4X66bS68-GdxNOqPS204E-yPrNpVALuWkTu4hgLUyQ1yXkK09oQzo1K4bH1DDV7N_F1pe8EkQ346icklTLXcrHH3G38s37BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش ۴ انفجار در تنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20745" target="_blank">📅 00:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20744">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش ۴ انفجار در تنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20744" target="_blank">📅 00:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوباره از سیریک موشک ول کردن سمت تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20743" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEq3_N-bDnMEAVPXQpUZsEyQiQzaP6cbMwh5ovCVBppd7lFL_7d4P7ySCpvmdxnWaR5y14PgPk_zUiCeivBV1d41G1Wgu_p4aay94Fsc1ne7-rBTJ-UjrfgrY3I5XVK3S4bN9xWAAEHkGxA-45BWPkGZLF933iTDTGggbVAt1a3P2QQ3JWt4oRy3eqGKk-KSgd880dTZACcjbg9JRR7jElhl3ZjIrfgo0A_YfkvYDfzh_-JMApPpwYJCfdIPK_yWXFul-46CheeM8mYMqFu0vJr7S_ty-mbB7v6VJIjgNdUe6qCk_bjsxOKNoHUl87qv5npUMhMAdw7fAqMb1JCr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک :
یه نفتکش میخواست از مسیر جنوبی
عمان عبور کنه مورد حمله قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20742" target="_blank">📅 00:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش صدای انفجار  پرتاب  موشک/پهپاد از سیریک @WarRoom
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20741" target="_blank">📅 00:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd95915a0b.mp4?token=nuBklJ_qhd1YNAwBJxTier4VgHHoTxjJ_SUT67kgOK6vBcOhyhUuB0-KZjUWEsjsp58QVCiLvwsXJ7qXGo-ta1QVebLaz6PX-3gw-NuuM6PDcvY4_8ERJZRYqXyrgk61sMz0gwfv6JQE1kbIKZDbk9OMSu5xtuD0o91BXsfW8_FO9ttKNQuvkFsDMt7wcOsM2IPD_VetSfmFCfWWWaKOP2v_kzd63YcrXGz4xzoeXmc8KrWJCeca9U69WZDvYgF0PysddTxu-7AjBu17Nvy5zAKJcDoOjQJY6VQBjKO4dVeFy5I-rZZtcDP0DfBcR2Z_tazQYyF7hBt4eZGDYCGycg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd95915a0b.mp4?token=nuBklJ_qhd1YNAwBJxTier4VgHHoTxjJ_SUT67kgOK6vBcOhyhUuB0-KZjUWEsjsp58QVCiLvwsXJ7qXGo-ta1QVebLaz6PX-3gw-NuuM6PDcvY4_8ERJZRYqXyrgk61sMz0gwfv6JQE1kbIKZDbk9OMSu5xtuD0o91BXsfW8_FO9ttKNQuvkFsDMt7wcOsM2IPD_VetSfmFCfWWWaKOP2v_kzd63YcrXGz4xzoeXmc8KrWJCeca9U69WZDvYgF0PysddTxu-7AjBu17Nvy5zAKJcDoOjQJY6VQBjKO4dVeFy5I-rZZtcDP0DfBcR2Z_tazQYyF7hBt4eZGDYCGycg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
نیوجرسی را ترک کرد و جواب خبرنگاران رو هم نداد، تا ساعاتی دیگه میره دم توالت شروع میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20740" target="_blank">📅 00:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شبکه i24 NEWS: اسرائیل فاش کرد که رهبر حماس، "باسل صالیه" را از دو سال پیش بازداشت کرده است. این خبر پس از دستگیری او در شهر حمد منتشر شد. این گزارش حاکی است که او پیش از این با سنوار و الضیف اختلافاتی داشته است. اسرائیل او را مسئول شلیک موشک کورنیت به یک اتوبوس در سال ۲۰۱۱ می‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20739" target="_blank">📅 00:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve0sNsWnvBz4brAhbQWYR9bLwc4izhD2J-GV2vXDuODpz9LwIq5RxrxD9H_5_F2ch_t2HmP2nOv7SvM_Kiqp1k-nZD1Y5v-JGZE5r85-BUstmNOhjw0WIoqRIOs4jUlDd9B38tTIjwjRazm7UPqI9RFqMpRiMUYnARi2xLFwqi421QYrZuVRojb2dATbEcuDUUwfIamZoKvY1BElD9UabAV0VmfeQN93VUX9Rja-5fmG_jxjmlWKOWgT1YwVNA0B9O6DlIvFGw4e2DVjCpjRjDFmw7uot_psqFGy5BBy0kCe6ZUiYBPwArBJ3aKnUyzAglxbwd7arDoTllTm1tjI0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت پیشرفته‌ترین نسخه عملیاتی خانواده E3-Sentry (آواکس)  بوئینگ E-3G Block 40/45  از پایگاه رامشتاین آلمان به سمت منطقه خاورمیانه،
با مشخصات :
قوی‌ترین ارتقای انجام‌شده روی E-3.
رایانه‌ها و نرم‌افزارهای مأموریتی کاملاً نوسازی شده‌اند.
توان پردازش اهداف بسیار بیشتر از مدل‌های قدیمی.
لینک‌های داده و ارتباطات پیشرفته‌تر
و موارد بکلی سری بسیار زیاد انجام شده
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20738" target="_blank">📅 00:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش صدای انفجار  پرتاب  موشک/پهپاد از سیریک
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20737" target="_blank">📅 00:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=lP6qX46WCrWYnCWl4N9ZK-ydAb0MNOeo4urRgwyUdwtuC-QwQfAee84fyAEOdJ1LmXskBkwz4CGOA35OLA0mJRGqfb7mzjiUfX8CRwCAqRLXO9Eop_3eEXtJ1y-nftETiHc8OnKZtvZI5ZxyXfe2BLWsAhUfZLY2xTlO6-7-OkDNahnjgX1-KHdhIqHliVvcGO4eekdd_WPQ-YK1zujYWHImPRKI92RcfXoK3grAtLeKuNclRVno9e2ZA1QjcmxGPgERiiEE99XGlvWayL7S1_UmbFVCeGNBw2L0ghXuw2539pjs5Shf4c7HTPsfAid6TR3KIilpKBymA2p6xApxy0hrTaSvUAc4dXB_cwVdsgdEipUtbybXpKxH5N_-3NvFgeqrha4YJcN3aYBltuzcAiCVAeKH0gBbjotti9wTkMNpeQ2wlbesHyDxivQvO_jeBXVuZGX_UrK6IuP7PwLGeGxUH5f8ewA0KbNy-jYriZfZVP0GPif7rZHE8fTVyewTqcVqHYOezUkD79XIVSVVCvmwbUzM0le-6j-zMHluDhVbXLK3l5QWvWN2kWVPIKIqE_zpiUum_UwF96_C5-SUU8PQYnjxJy4IV6bT9GnZQ9NWOhO4CgLVh-NObkR_9WQ50c92i-YQhE_9E_AskY8j0oFrYQWjbsewok-IRVihPm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=lP6qX46WCrWYnCWl4N9ZK-ydAb0MNOeo4urRgwyUdwtuC-QwQfAee84fyAEOdJ1LmXskBkwz4CGOA35OLA0mJRGqfb7mzjiUfX8CRwCAqRLXO9Eop_3eEXtJ1y-nftETiHc8OnKZtvZI5ZxyXfe2BLWsAhUfZLY2xTlO6-7-OkDNahnjgX1-KHdhIqHliVvcGO4eekdd_WPQ-YK1zujYWHImPRKI92RcfXoK3grAtLeKuNclRVno9e2ZA1QjcmxGPgERiiEE99XGlvWayL7S1_UmbFVCeGNBw2L0ghXuw2539pjs5Shf4c7HTPsfAid6TR3KIilpKBymA2p6xApxy0hrTaSvUAc4dXB_cwVdsgdEipUtbybXpKxH5N_-3NvFgeqrha4YJcN3aYBltuzcAiCVAeKH0gBbjotti9wTkMNpeQ2wlbesHyDxivQvO_jeBXVuZGX_UrK6IuP7PwLGeGxUH5f8ewA0KbNy-jYriZfZVP0GPif7rZHE8fTVyewTqcVqHYOezUkD79XIVSVVCvmwbUzM0le-6j-zMHluDhVbXLK3l5QWvWN2kWVPIKIqE_zpiUum_UwF96_C5-SUU8PQYnjxJy4IV6bT9GnZQ9NWOhO4CgLVh-NObkR_9WQ50c92i-YQhE_9E_AskY8j0oFrYQWjbsewok-IRVihPm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) اعلام کرد که جنگنده‌های اف-۱۶ این فرماندهی، چند هواپیما را در نزدیکی باشگاه گلف ترامپ در بدمینسترِ ایالت نیوجرسی رهگیری کردند؛ زیرا این هواپیماها بنا بر گزارش‌ها، محدودیت موقت پرواز اعمال‌شده بر فراز آن منطقه را نقض کرده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20736" target="_blank">📅 23:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20735">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانال ۱۳ : اسرائیل به فرمانده سنتکام اطلاع داده است که در صورت توسعه برنامه‌های هسته‌ای و موشک‌های بالستیک ایران، به ایران حمله خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20735" target="_blank">📅 23:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20734">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به گزارش اکسیوس، توافقی برای کنترل عبور و مرور از تنگه هرمز بین ایران، عمان و ایالات متحده مورد مذاکره قرار گرفته، اما چندین روز است که در حالت تعلیق مانده است.
مقامات آمریکایی می‌گویند اختلافات فزاینده‌ای در درون رهبری ایران وجود دارد. گفته می‌شود یک ساید به رهبری رئیس جمهور مسعود پزشکیان، به طور فزاینده‌ای نگران فروپاشی اقتصادی احتمالی است و معتقد است که تهران به توافقی با واشنگتن نیاز دارد. ساید دیگر به رهبری فرمانده سپاه احمد وحیدی، با امتیاز دادن به ایالات متحده مخالف است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20734" target="_blank">📅 21:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20733">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دونالد ترامپ، به آکسیوس گفت که ایالات متحده در قبال ایران «فعلاً با سر و صدای کمی پیش می‌رود»؛ اظهارنظری که نشان می‌دهد واشنگتن اجازه می‌دهد فشار اقتصادی افزایش پیدا کند.
ترامپ گفت: «ما فقط به‌صورت نیم‌بند با آنها مذاکره می‌کنیم. ما فقط داریم ایران را زیر نظر می‌گیریم؛ با این تورم شدید و این واقعیت که پولی ندارد.» او با اشاره به وضعیت اقتصادی ایران مدعی شد که این کشور «در شرایط بسیار بدی» قرار دارد و در پرداخت حقوق نیروهایش با مشکل روبه‌رو است؛ آن هم در شرایطی که محاصره دریایی آمریکا فشارها بر ایران را افزایش داده است.
ترامپ درباره رویارویی با تهران گفت: «همه‌چیز درست خواهد شد. همیشه درست می‌شود. این مثل یک بازی شطرنج است.»
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20733" target="_blank">📅 20:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20732">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اکسیوس: میانجی‌های قطری و پاکستانی اطمینان داشتند که این توافق روز
چهارشنبه
اعلام خواهد شد، اما از آن زمان، چشم‌انداز دستیابی به توافق کمرنگ‌تر به نظر می‌رسد
یک مقام آمریکایی مدعی شد که حدود ۸ میلیون بشکه نفت هر شب از خلیج فارس از مسیر کریدور جنوبی تنگه هرمز و با هماهنگی ارتش آمریکا خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20732" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20731">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCAh8fePLqBv5GR7hP31ev0FEDYiyatXCtdXoSqV0mwe2vHcPV8XrznIXyfpAQgVbyg7LfhBRizuhvrOnLAL5Pq-S6ANglmTr0nY3bj6U4ywZcOGZDxTYzuIcxd7XnXpgsvRhPfLOyrsCOxpUj0Uqhbw-Y9qToEkVbYdCBa_EssXJlNlgCtwkwUM_tyjruNPurZJw8YnnRkMnjvarI8jI4oCjMUeRTbSpLCLTrojN6BxwDhhTDSGGjiQZp_1T4ys8JYF9UOjKGR9bMCSRaQbojrBu6EsSJDuIV9Gg4sQsLcyphztxJ12cY83NKpITtcGQ-g3NNOBHhWkb11xFVe_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : جت‌های جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در آسمان خاورمیانه گشت‌زنی می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20731" target="_blank">📅 19:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20730">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حسن قشقاوی، سخنگوی کمسیون امنیت ملی مجلس، اعلام کرد کلیات طرح «اقدام راهبردی تامین امنیت و پیشرفت تنگه هرمز»، با اجماع همه اعضای کمیسیون حاضر در جلسه به تصویب رسیده است.
- کنترل بسیار بیشتری بر تردد کشتی‌ها در تنگه هرمز اعمال کند.
- برای برخی کشورها یا محموله‌ها محدودیت یا ممنوعیت ایجاد کند.
- برای عبور کشتی‌ها نظام مجوز و در برخی موارد تعرفه یا عوارض در نظر بگیرد.
- از تنگه هرمز به‌عنوان یک ابزار فشار سیاسی و امنیتی استفاده کند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20730" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20729">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رئیس مجمع تشخیص مصلحت نظام:
به هیچ قیمتی از موضع خود درباره تنگه هرمز عقب نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20729" target="_blank">📅 18:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20728">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=mNdpUWBy7YK0JGgzX9NPdoyBwdUhmDlx_ZdlC07SpF-nNUY-MLnn6nsasc2XjllRIu9zSWgzt84sQp3qE10keuZqNts9hLFOcVbJsZufUeqKkA1Aq4x_gRrGtkIPWp_QDQPM85LEOJhgoK7obFko9h9HVyEOn0ywywpsbqUd4GMXVep5BNILzpXBqUOdZ_T_XGnpn5hkVG3vcL-N6VhdXVzS2sxoV61BqAy9I0uKGrWbGss9XUuQMorXMDdjua9ds89TKSRJVzWEFFadaWCbM4dhl6YnzHEjIcsgv5_jWyJYxWrW7noLRbf8KThSxOP1qjQtsy7iVbLLyB5_nH7Q-wq69zaklGeHpgwzSaHrhAbNNQtZ5Oo1OW7B4jl5Ez8SA8PDeVMYYQ8SC9rTGzXA2t0KXe9BPyQsALLp8W_Rm7ZgLQhtIx1eGCXPVO8DdjEo6nmVSn__Z5wYQWH1lQ27UBfjkwpvhhe-LUkobMG6IMxhzcCFprtRDFA0XvM92TnjKbJE8dXwXBj1EYCzZFLrGvd35zPkDtVJbbl87if6iqFX7KEk_HLREbgPUCX9CcNJZyTWGnlCs3gSViYDL8eOCFJEgYLH7fcxiljRSz1CdAGslhN30teap6SNb_FstKnGgbxuvFeffAO8eRctWNTSoLncO9CWGEjDPkzG0LrkZtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=mNdpUWBy7YK0JGgzX9NPdoyBwdUhmDlx_ZdlC07SpF-nNUY-MLnn6nsasc2XjllRIu9zSWgzt84sQp3qE10keuZqNts9hLFOcVbJsZufUeqKkA1Aq4x_gRrGtkIPWp_QDQPM85LEOJhgoK7obFko9h9HVyEOn0ywywpsbqUd4GMXVep5BNILzpXBqUOdZ_T_XGnpn5hkVG3vcL-N6VhdXVzS2sxoV61BqAy9I0uKGrWbGss9XUuQMorXMDdjua9ds89TKSRJVzWEFFadaWCbM4dhl6YnzHEjIcsgv5_jWyJYxWrW7noLRbf8KThSxOP1qjQtsy7iVbLLyB5_nH7Q-wq69zaklGeHpgwzSaHrhAbNNQtZ5Oo1OW7B4jl5Ez8SA8PDeVMYYQ8SC9rTGzXA2t0KXe9BPyQsALLp8W_Rm7ZgLQhtIx1eGCXPVO8DdjEo6nmVSn__Z5wYQWH1lQ27UBfjkwpvhhe-LUkobMG6IMxhzcCFprtRDFA0XvM92TnjKbJE8dXwXBj1EYCzZFLrGvd35zPkDtVJbbl87if6iqFX7KEk_HLREbgPUCX9CcNJZyTWGnlCs3gSViYDL8eOCFJEgYLH7fcxiljRSz1CdAGslhN30teap6SNb_FstKnGgbxuvFeffAO8eRctWNTSoLncO9CWGEjDPkzG0LrkZtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فاکس نیوز آپدیت آخرین تحولات تا دقایقی پیش…
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20728" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20727">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtcQ3wjXO_H2Z3xzICoYX9HELGAfmme1-AykWZunapdWlZfkqdosT8xga1j1Mi8H0Ccs0dXX6TLfcrgGiHQCwaU3Mh1bmm03Xz7RIuMX9mD1zZV-x1f5hMXWSLQhylePawmgcdaevT1wKf-mIRV-LLv2UCIz_Rxt08S1-aKXvZ_Id2RaMehUdA3Vey2CxYCmsWfIUNjbk1GESZpuO2EwvomLbKzggGjig1IG11Qt4dD2LEvV3MykELOtwjG4y9G-tJt7TXexVFsonsxFfe2zmmcEVtqFbLWL9EAjEUqJDk_TD-_OsPPH5-AAM7KVjh4aIZavTY-cBm0JaCFmFGY4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود و صدای انفجار در اصفهان
چیزی نیست بی بی داره خنثی میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20727" target="_blank">📅 17:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20726">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77914048f8.mp4?token=iCAdxwCcmZC7HKnqNcVLc04E3FMUDFNYLGobcFC5KwJEmWpLb-xiTr7RsrpOVL-mL8RTpXkQawbLHrWIef4CvG-zJgvCsYtVEpEBBv8Ks7Gn3kxrhvne0HV0VCqgllCYaMxIg5JCbYulduoJOi68AxUjE537b5Po6p94dPpNr5NTz8RnwCYGc39752XJQkHKznOX0aXjSBKoy-VL9lP5tLKdnrkgcrHx_Jkvv4MI0CAPBcZU4NW6MTv1SrHl4S38vIFIniRudeaxK5eKI8AbspVVuc8stXMe_EDlpk9ncyR8-Ol12dmEY0vd_2Jp8YETrELyFC9BZNpMYe3seRLr9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77914048f8.mp4?token=iCAdxwCcmZC7HKnqNcVLc04E3FMUDFNYLGobcFC5KwJEmWpLb-xiTr7RsrpOVL-mL8RTpXkQawbLHrWIef4CvG-zJgvCsYtVEpEBBv8Ks7Gn3kxrhvne0HV0VCqgllCYaMxIg5JCbYulduoJOi68AxUjE537b5Po6p94dPpNr5NTz8RnwCYGc39752XJQkHKznOX0aXjSBKoy-VL9lP5tLKdnrkgcrHx_Jkvv4MI0CAPBcZU4NW6MTv1SrHl4S38vIFIniRudeaxK5eKI8AbspVVuc8stXMe_EDlpk9ncyR8-Ol12dmEY0vd_2Jp8YETrELyFC9BZNpMYe3seRLr9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی با جمع‌آوری ویدیوهای تیک تاک از آهنگی در وصف پهلوی یک دابسمش منتشر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20726" target="_blank">📅 17:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20725">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgAW4pshUl2zdzq36V9RaKiveJYs-ubUUhWn11QnvQP1ufQdcUPDzjeOSp49U1WOsU_5pxJN9XIOiRDswPgaw9l0lH0ELls-jiAb0jSjwqAD94nSvdvvlNKHSIekrtA-UCEmg2j6o2rI2Hjtupc2Wz07AxAYqlo76Izkoj7voWd3SwP2ulc3tjue1KQi12VT9aGOmJFyI-OPqz-S7SitFY4QY2GMFcQs_mmgF_v4gGz47NTqTvXEndlRYnNPFG9aM93T5OYXm88Go1WusxAZ5UT-mxLUZqTJ1jDnc9-fl-pHyZdR53fS6Bf7bsayvUko7yelj5gKSY5VjkTbfCWoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین با خطاب قرار دادن عراقچی به دولت آمریکا : این بیشرف می‌گوید هیچ مذاکره‌ای در کار نیست
یاشار: منظورش اینه بفرما این عراقچی بیشرف هم میگه مذاکره ای در کار نیست کار رو تمام کنید
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20725" target="_blank">📅 17:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20724">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یکی از معاونان نیروی شبه‌نظامی بسیج ایران ادعا کرد که تصاویری که مجتبی خامنه‌ای، رهبر ایران، را در میان مردم و در خیابان‌ها نشان می‌دهد، در آینده منتشر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20724" target="_blank">📅 16:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20723">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucn9kctbGEaUre59wE62H2SdkJxWScu9G3T0yX7bLTLQR1wlaJ8sy6LmFpOF9VRHtrGTX_dZAaPXqnHWR0PkC7QM9MzwI7QVrQQN3j-bdfQNcVRKO2zKV_JEnTE_JIkQDIBH0nL5puKdCZDCjIK8QJABB7hv5vTOo9PeayahEE1wMgzZICucDPRXH2mbmGSCp1X7X4Pd99ld6kkcBqdECNy4JMU_ydIhSKOMtt3OIoZCu5r5ixMqRuTIc_eQx0zKqJoLwy1wpnxJmMfLk2P4bAWJrQnBPGf4x4rhPMFLzY-4eyhsx9UHYJK2zfTdzUmGk1OouLno7omWFRlELp5fcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هر روز پیجو میززن و برمیگردونم
پیج اصلی :
instagram.com/yashar
پیج دوم : ‏
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20723" target="_blank">📅 16:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20722">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067ef90d71.mp4?token=P0mV8Un4ppkK7I_NmtyWvcLPxCur9jMP0U_cLqlFW-22DUhFsGwCrSKXCNxsU96HzJx_oKfOt1TGoi_F7_zYk16E_0WkXRVSHMzU9Brh2Ca0tN1yCdm2tol1ilbp45Y10aVEEucrsSdRcvnxoRUhogJkjN4TRHN8Kl9_dY_1ebWx1DEvr3pBz6kJOAye8PY-JJzqPtoVTOw8QenhDl0EjbyXFXm7VZQYhe2rdVffZpQOPTcqhEnjuK-I8sDbctU3mm0eMebQoklGyJmbsXjq7khwdEBPJD5T821ZZ3KqfPMouOHK5AHqN5uhNPBESBcB49aE-rHMgXabEIhVgS7A2CK2Eht_f9Y-tMuOQeKl25H5gmeYyTP783eGb8IQehgZeCQ8GRhY3ptr_OK1nHH7kLEa3EDxi6HLzcQ2dOYWPoTn3aFDhtdzxy8o0kubvooHZzM30Kxl_2X-ibOSfNUq9Ie0DFhtv8Wl0-ndXHWbRu93WOYL188dwVC5h6042g94vdGrxdww3o1wJ1P7rR8hR3r01Qtc0nanUBRtU5LTb6GMegIu1dyeDiYPdMHewiK3BgP1KEXLApHmI0Gr4XhdmDhe0l1Uq1xg1Acut9F90H9ac1jSxLV5xbJKQzo-Y2s3eMn18tzNUTm_wVGbINRp8dBup0IwBwgugLQ0g-DGmf8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067ef90d71.mp4?token=P0mV8Un4ppkK7I_NmtyWvcLPxCur9jMP0U_cLqlFW-22DUhFsGwCrSKXCNxsU96HzJx_oKfOt1TGoi_F7_zYk16E_0WkXRVSHMzU9Brh2Ca0tN1yCdm2tol1ilbp45Y10aVEEucrsSdRcvnxoRUhogJkjN4TRHN8Kl9_dY_1ebWx1DEvr3pBz6kJOAye8PY-JJzqPtoVTOw8QenhDl0EjbyXFXm7VZQYhe2rdVffZpQOPTcqhEnjuK-I8sDbctU3mm0eMebQoklGyJmbsXjq7khwdEBPJD5T821ZZ3KqfPMouOHK5AHqN5uhNPBESBcB49aE-rHMgXabEIhVgS7A2CK2Eht_f9Y-tMuOQeKl25H5gmeYyTP783eGb8IQehgZeCQ8GRhY3ptr_OK1nHH7kLEa3EDxi6HLzcQ2dOYWPoTn3aFDhtdzxy8o0kubvooHZzM30Kxl_2X-ibOSfNUq9Ie0DFhtv8Wl0-ndXHWbRu93WOYL188dwVC5h6042g94vdGrxdww3o1wJ1P7rR8hR3r01Qtc0nanUBRtU5LTb6GMegIu1dyeDiYPdMHewiK3BgP1KEXLApHmI0Gr4XhdmDhe0l1Uq1xg1Acut9F90H9ac1jSxLV5xbJKQzo-Y2s3eMn18tzNUTm_wVGbINRp8dBup0IwBwgugLQ0g-DGmf8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ناتو وارد میشود
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20722" target="_blank">📅 15:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20721">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نتانیاهو : ما می‌دانیم چگونه در موضع خود باقی بمانیم، حتی در برابر بهترین دوستانمان، زمانی که این کار ضروری باشد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20721" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20720">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏مسعود پزشکیان: «دشمن افرادی را ترور می‌کند که گره‌گشا و حلال مسئله هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20720" target="_blank">📅 14:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20719">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتانیاهو: تا زمانی که من نخست وزیر هستم، هیچ کشور فلسطینی، نه در غزه و نه در کرانه باختری، وجود نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20719" target="_blank">📅 14:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20718">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو : در روزهای اخیر در لبنان عملیات هدفمند انجام دادیم، از جمله در منطقه تپه علی الطاهر، اما وارد جزئیات نخواهم شد.
ایران به اسرائیل حمله نمی‌کند، زیرا می‌داند اگر چنین کاری انجام دهد، ضربه سنگینی به آن وارد خواهیم کرد.
من طرح ۱۵ بندی «شورای صلح» درباره غزه را رد می‌کنم و از غزه عقب‌نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20718" target="_blank">📅 14:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20717">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یکی از رسانه های رژیم نزدیک به جبهه پایداری، با انتشار پیامی از هوادارانش خواست برای سلامتی مجتبی خامنه‌ای دعا کنند و «قربانی گوسفند» انجام دهند. در این پیام ادعا شده که «گروهی از علما» از در خطر بودن جان او خبر داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20717" target="_blank">📅 14:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20716">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با کانال «12 نیوز» پیش‌بینی کرد تنگه هرمز طی 2 سال آینده اهمیت خود را از دست بدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20716" target="_blank">📅 14:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20715">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ادعای تسنیم : محسن رضایی کج بند ،نماینده مجتبی خامنه ای در شورای امنیت ملی شده‌ @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20715" target="_blank">📅 14:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20714">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ادعای تسنیم : محسن رضایی کج بند ،نماینده مجتبی خامنه ای در شورای امنیت ملی شده‌
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20714" target="_blank">📅 14:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20713">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ادعای فارس : پزشکیان با مجتبی خامنه ای دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20713" target="_blank">📅 14:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20712">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تسنیم با انتشار این کلیپ که قدیمی‌هست نوشت: پخش تصاویری از رهبر برای اولین بار @WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20712" target="_blank">📅 13:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20711">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnZM7q9qp2MKE9lQA8yAJDtVhdXf-9x07md0Rbjf0wQWNJJvkbK_zq30YqmzN93fSxMG5Mpd_ULZ8bTofm7tEOGcccXDrfnXrRvBs8meEBzkdUiKtzRovE5KDVsoiVEB-5ovC6fSkuiC4pciO39jaJHa7gxE_HFcpwJcj__hqhRsrP0aYdQsGMMA0RwgM3lliCWsXLRlzjqOYo-FVMu4bt__EgIuEVS7DPU_y8phXp47b3w32DvbA62q8TmcRTdzA8CnyV3KZTpEcE0EEFBFcdYZij6MnjDeWXIqTKNAXmAYg6TG9V07IuQAXjUzlxVoSJ5dzFSNlcb41OW9b16nKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دو آمریکای بسیار متفاوت.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20711" target="_blank">📅 13:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20710">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from╚»میلادم«╝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAsQdOo8eOjLUeSqZShQPhsaFp4GRncpPjn3ffXkWGGZzDtJvZwDD_KABxevwKaS1d2fhGP_yJXMLyqkN_FomeOJ63N9SAzxeCSBgbKIxyJTQ1U_p_ulqcl8C-Bp8vdyytlcDIDIBbHzTcSSkHOx0pUP-kYhohAbpiG_2PgyPfCLcpSzWWfJka5pJKwphNNX74kGJrdHLURhaFETs27Ben8htTw7fl8YftrwvboWa8IP4ko1Ga7btwNJhiuLvyfxUtLGoxTQTPWjFgs73aUDeikA2IuWoSCjI7sV0T5vsp8jK17hUQE_4-EmLOdEOnjkH58sLxy2qCxXNBHDmWzouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20710" target="_blank">📅 12:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عراقچی : در حال حاضر هیچ مذاکره‌ای با آمریکا نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20709" target="_blank">📅 12:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20708">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دبیر شورای امنیت ملی ایران می‌گوید که ایالات متحده باید دارایی‌های مسدود شده ایران را بدون قید و شرط آزاد کند، تحریم‌ها را لغو کند و غرامت دو جنگ اخیری را که علیه ما به راه انداخته است، بپردازد. @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20708" target="_blank">📅 12:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20707">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏وای‌نت : دولت اسرائیل امروز اختصاص یک میلیارد شکل(حدود ۳۴۰ میلیون دلار) به وزارت دفاع برای خریدهای فوری تسلیحات را تصویب خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20707" target="_blank">📅 12:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20706">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سپاه : استراتژی ما حفظ تنگه هرمز است تا زمانی که دشمن تمام شرایط ما را بپذیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20706" target="_blank">📅 12:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20705">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به جنوب لبنان
رسانه‌های لبنانی از گلوله‌باران منطقه واقع بین دو شهرک «میفدون» و «زوطر شرقیه» در جنوب این کشور توسط توپخانه‌های اسرائیلی خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20705" target="_blank">📅 10:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20704">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e5786aba1.mp4?token=fTumWpdFTnD0TJARHslIX3nIFxhnsifllGjR28gW4tQzdSLtyQZS1Cw-vBA6EBe3xMERmDvoJuCfse3pgbdDNVg3XvoS8cOxHi8c9aj1ipygQxkYIpGMJP53MP72mX-FeTysBs1T5zsyqh6qmLjtD9csI3SMfEQIpGrPADat9US7-682gh9jSTb1l2sBdO-IKSW3MEa3LIzKQhIUUPclT94pehl76TY2bf2N2E90kRtSPmUEi2DeF-rGJ819mw9XoXxqCIT1MA_jWFVCvyh9CkEPF2FlcC5OJ7yCN-D84jb5Z-EcNG8P1qNr5-L2pdAL8TMmYhkUwFl1yeWecC-kEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e5786aba1.mp4?token=fTumWpdFTnD0TJARHslIX3nIFxhnsifllGjR28gW4tQzdSLtyQZS1Cw-vBA6EBe3xMERmDvoJuCfse3pgbdDNVg3XvoS8cOxHi8c9aj1ipygQxkYIpGMJP53MP72mX-FeTysBs1T5zsyqh6qmLjtD9csI3SMfEQIpGrPADat9US7-682gh9jSTb1l2sBdO-IKSW3MEa3LIzKQhIUUPclT94pehl76TY2bf2N2E90kRtSPmUEi2DeF-rGJ819mw9XoXxqCIT1MA_jWFVCvyh9CkEPF2FlcC5OJ7yCN-D84jb5Z-EcNG8P1qNr5-L2pdAL8TMmYhkUwFl1yeWecC-kEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی آتش‌سوزی یک واحد صنعتی در شهرک نصیرآباد، ۶ نفر مصدوم شدند که یک نفر جان باخت و ۴ نفر به بیمارستان منتقل شدند
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20704" target="_blank">📅 10:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20703">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏حوثی‌ها اعلام کردند پالایشگاه آرامکو عربستان سعودی در جازان را هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20703" target="_blank">📅 10:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT-6ftaavg8Ts2oCD1CS-lLa2fDmG_Tbi-3rlyxShg9rd76i1tkwF-BI7JeZQJWrUDa4jPghqxaRSfBgOMFCj-IYsHfgqM1PKL0txh_YpzjVicR4Gyiw7iIjKlesC9z29m0hkrqQFHiXq00ntVeXTvEWxTJbRPJzlEhERuKQcifGIzfwkLi0aQ62Timr6ntmEah6OHXK9_DjNZxKjoLmWCzK-KJrARjt4wB_khLGcDKfxqesaIqThdB4OS0v2cCwzsJO8LMGerLKWnkuZjVEnHATGuP7VaejU2Y5IzkLn12Oz0R8sHZUDxMUMLq9JSVWK0ckM4rHZqBDLbXj_G3xMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورشلیم پست : ایرانیان آزاده و اسرائیلی‌ها باید در کنار هم بایستند و اطمینان حاصل کنند که سنگ بنای صلح فردا هرگز قربانی تیترهای جنجالی نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20702" target="_blank">📅 10:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20701">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کانال ۱۳: ارتش اسرائیل به فرمانده سنتکام اطلاع داده است که اسرائیل برای جنگ علیه ایران نیازی به تأیید یا حمایت ایالات متحده ندارد و اعلام کرد ما در حال حاضر در حال آماده‌سازی برای شروع جنگ هستیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20701" target="_blank">📅 02:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اتاق جنگ با یاشار :
برخی کانال‌های تلگرامی عبری مدعی شده‌اند که یک ناو هواپیمابر جدید آمریکا در راه خاورمیانه است.
بر اساس ارزیابی‌هایم، محتمل‌ترین گزینه
USS Theodore Roosevelt (CVN-71)
است؛ ناوی که به‌تازگی مأموریت
RIMPAC 2026
(بزرگ‌ترین رزمایش دریایی چندملیتی جهان به میزبانی آمریکا در اقیانوس آرام) را به پایان رسانده و به
سن‌دیگو
بازگشته تا وارد چرخه آماده‌سازی برای استقرار بعدی شود. برخی گزارش‌ها حاکی از آن است که این ناو احتمالاً در
ماه سپتامبر
جایگزین
USS Abraham Lincoln (CVN-72)
در منطقه خاورمیانه خواهد شد، اما
تاکنون هیچ دستور رسمی و علنی از سوی وزارت دفاع آمریکا یا نیروی دریایی این کشور برای اعزام Theodore Roosevelt به خاورمیانه منتشر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20700" target="_blank">📅 01:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">😁</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20699" target="_blank">📅 00:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvOsdLLJyM--QQJRokhLKI9aoRJ0CPIUA8gzTuLXlF4JJrHyfMRWiaYs8H79qeENfrYlkB_MAapdOczpYyifQEX1vPpg-rrZH02LxfvIaNUv-Le5uysPLWlu_0PLl7hCQMgXD-tZ3D0DbjPw5-58RE5aELq7dK-qjjhnLbmhanUOzzg-MLQ7lytOgJpKK95I8Ox9fL6CiUVNH7-qRFfDX7K8S5ahoauM0KbXBRhMGF61U4N3Xr78BKcoO_gxZwOgFtLYqDY2_GbzYFJxKEWmxgr7K2VIFeBD56--tDSIUlLnB9H0XgYcdpv_2asRSez5k0x_ygjHaCQKPBbM7CS6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین باز دید پیج اینستاگرام از شهر های داخل ایران
😁
تبریز
🥇
🏆
اصفهان
🥈
تهران
🥉
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20698" target="_blank">📅 00:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20697">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeKGUoayuChJHTthwyOc0Gx-I7ExIRElTKPutctjjdm3-cJE7D0im4ib5--nPakstJqJjCHJr6zR0WceYHKML-DH4QgtBMd4bEWWSjCXUlO2_u38hm2vZjiSCBCK7sxV6r-6s1gcn4mc3UuezFntXud4ziez5AvrApmABYWf1scbLRehTfONtT1dgyPG1VP7Rh-x62qTLm1KCljE9tAzkkmU-1NmjvZCQmp1VgbbGu0d6eK9pQa-77b0AmicorKcnctpkEBgMga3Hdq2j46K8aP9vXrgtu87-MYTCzNLpn_lvGCIl5Lz7AjxsFaThrCXTSjBaeOQ0CqHjjPOExpgTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست: تأسیسات هسته ای کوه «کلنگ
گزلا» در تیررس ترامپ قرار داره
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20697" target="_blank">📅 23:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20696">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtjnMuG9dtjxxCdkR4MA1ogsfvpaxQ6lEJjKcZR5VcVisKRUAtsi7n5JSw1-FxpLFrFR7ERghRHqYwOv6lYzGhY6vWf5tog9zHjv5sudOCDugj5nPeypdBokkw5cGj_96is_XfJGBra-NFoPssGBj5FwolA51CjrrzR5HgwNZnYGzhypkEeXpb4INhtGspBJwJ_I2LCvX9iSrWg7XhaRMLIxjr_FD9HfjcO0ApzOhsRSmezaDEHksUDGA8p4EzqtLXWBzaP3EDAtpKnEjo_RpRTU2y7jeyL2krkkWRVHgobYHcx2fEBEEUYSqMfuNBa0BgaMzs6E_BDBHIkkT2TBwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : ملوانان آمریکایی در حال تعمیر و نگهداری هواپیماهای F/A-18E Super Hornet در عرشه پرواز ناو هواپیمابر USS Abraham Lincoln (CVN 72) هستند تا اطمینان حاصل کنند که تجهیزات گروه ضربت ناو هواپیمابر برای اجرای محاصره ایالات متحده علیه ایران آماده ماموریت هستند. تا 8 آگوست، سنتکام 53 کشتی تجاری را تغییر مسیر داد، 2 کشتی را از کار انداخت و 2 کشتی دیگر را نیز توقیف کرد.
ارتش ایالات متحده همچنین به بیش از 30 کشتی اجازه عبور از محاصره برای کمک‌های بشردوستانه را داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20696" target="_blank">📅 23:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20695">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXvqS_2bukN31GmYVo6cicyw9USHuP8IqZBtPGb4ttQrFn57TZiKMtsm668UvQImzZ7ZJfpR7cpFqfhOD-F2ynOr5q9Kh_uCTFHsEzNiSJnEGXbMb-QhpdqJw4TBOhPVUkg_MU6t9VJNlt3ZN4KeZXzAbn7JArHpFa7OLnT9HJHLureyrnAQB_AsCXZpfyyw4EvD-u-bgWr_oKd-13FoV-2t0H_i0McKpeF9rof7PSOCnBl0xYfoX1xNZh_22C2_1WSVungvDQAqqpJH614EaC56gQ0fbutcoOFYSvP7c0fnI8dBmNyFPJTF0I1kZjv9aj7BXbzUrwZOeYM93FXuzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده سنتکام وارد تل‌آویو شد  برد کوپر با رئیس ستاد مشترک ارتش اسرائیل و دیگر مقامات ارشد ارتش دیدار خواهد کرد. @WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20695" target="_blank">📅 22:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20694">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تمام مرخصی های نیروهای نظامی اسرائیل تا اطلاع ثانوی لغو شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20694" target="_blank">📅 22:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20693">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وای نت عبری : آمریکا سلاح‌هایی را از آسیا و اروپا به خاورمیانه منتقل کرد، زیرا موجودی سلاح‌ها به سطح "نگران‌کننده‌ای" رسیده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20693" target="_blank">📅 22:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20692">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نیویورک تایمز به نقل از مقامات رسمی نوشت: ترامپ تصمیم گرفت با وجود هشدارهای ستاد مشترک ارتش در مورد مهمات، جنگ را آغاز کند و انتظار پایان سریع آن را داشته باشد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20692" target="_blank">📅 21:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20691">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فرمانده سنتکام وارد تل‌آویو شد
برد کوپر با رئیس ستاد مشترک ارتش اسرائیل و دیگر مقامات ارشد ارتش دیدار خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20691" target="_blank">📅 20:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20690">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانال ۱۳ اسرائیل : اسرائیل در حال آماده‌سازی برای احتمال اقدام یک‌جانبه علیه ایران است
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20690" target="_blank">📅 20:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20689">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anzv140pbAHtnuxSAsSGqXLUK2K68DTelC0YmJytfx8K7KjI7dBpBV8X3cDNATQeH9vpWq6J15GVPZNJ6LXPhpsqa6lPBXkjnaJ0i5qNQqrdoZ5nxFL64qGkdkZwMxsQV-cOBbkuqoXm582tjtD1lM7AqLdustssdkyYXvMXiXSf1jz1CMQ5VvXkIuD9OKtA8KeT-B_Mkwj72qlkEtWvc5WYFP0-5lNHZDucXDk1Xs17Q27S6-GhT_3h9otNLf1-fNZHFb9gwNX9BPDidHbt88I9FOZ0bO1vi4m1_l3SMz7j3Hhf8lLhEMXT5W00uLrEywwMgydQ9lYLiL87Oc0RNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است امروز دو بمب‌افکن B-1B "Lancer" از پایگاه هوایی RAF Fairford (EGVA) پروازهای آموزشی انجام دهند و گرم کنن حسابی برا حمله اصلی . یکی از آنها در حال حاضر قابل مشاهده است: B-1B "FROWN30" 86-0124 B-1B "FROWN31" (در انتظار تایید) @WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20689" target="_blank">📅 20:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20688">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وال استریت ژورنال : ایران به دنبال منع عبور ناوهای جنگی آمریکا از تنگه هرمز حتی با توافق است
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20688" target="_blank">📅 20:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20687">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9dsZANVUVE4hplJFQf3dtzUDVOW1mAejd1HCfUqpJgaddQ4EZS2Vh7Cn0wwsWJOwTDWobP4DG3Pv44Y4sCI6iooobWBZQ4QtYMiwv3EygsxoTW06RKIwBF3hP_DzeU_Z4dz_zbRGE1IpeXuu8Iysl0JK34C_kKjDCtqcQdivnCpbTPPv4GQdQt--jbV7Amg1mjNqEOInoK7jvaHvsOtS1VUKYX6pKTyyw-qkkri5ZO9hwNgommEYOGA74IL-jMzW1drNKilKaUOqV5s9q3Xc852nCvfGLDECyByQkwcbGeIO4zC49ahjv-Le4oNDacE53OuqzAaMkuuBFHqhEW5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت سوخترسان از اسرائیل بلندشدند
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20687" target="_blank">📅 20:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20686">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dc8a5363.mp4?token=aoj8kR4Fzhk6v2WBqvlHHhactWl-qeHSzA9AituVi9SMdpx55482Yeskx7Z2ILMZtfFihec2yt7Vnkii3Ct4uDBARV5rnXs6Vp_QhEuLeQnfD79kNmHtciBQzl8YXZYb6MLqva09MnIXzRAffWfYMsGANuVv2oGE7cN0vEkjvo1wcJBuectC6qmrH0iEsBm7BQd25udRlPfbUgoiOp1CAX-7VOLH1s2gI2M0Bs0HyybAYRdZTzRM16e63t_AhOjvaWcHZhNAQ5OKGVSUW3_ERAhssU1qd7qtOZ6kVeQPQnA00cin4BDDMeCrORERhIrhfRnE1JmSGK2wmkzb67TNmGAOkqbAZ5tICGAGa59yzPqRv1lH1n1my-vzROZwPYtVDLwvsrOfplhhzCDQicxV6h4f12D2Zg6J5qOFFU2ftAj_TalhGf2f20xpYatAdZPKIdUFKAaGTgeyhuHrudbsCGNpjlr3_Hv7-YswUaJbB8lThYXX69gnOTjVFYDulrpuchrWXtsOJv0z4sqf3nlgUAGW9Ric-YxXZX-dftb8LtQc8yGidgLjl9jsb06iA8FxihKI1sDRU8unKdcZGyfyrRFrBOJbW0vVjBOI7OmLfyeQI8mB54DI6R8Z3HP8fe5uxj_DCGFui52EF340N8F-NyejzU8nGwbHnARzZUORamM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dc8a5363.mp4?token=aoj8kR4Fzhk6v2WBqvlHHhactWl-qeHSzA9AituVi9SMdpx55482Yeskx7Z2ILMZtfFihec2yt7Vnkii3Ct4uDBARV5rnXs6Vp_QhEuLeQnfD79kNmHtciBQzl8YXZYb6MLqva09MnIXzRAffWfYMsGANuVv2oGE7cN0vEkjvo1wcJBuectC6qmrH0iEsBm7BQd25udRlPfbUgoiOp1CAX-7VOLH1s2gI2M0Bs0HyybAYRdZTzRM16e63t_AhOjvaWcHZhNAQ5OKGVSUW3_ERAhssU1qd7qtOZ6kVeQPQnA00cin4BDDMeCrORERhIrhfRnE1JmSGK2wmkzb67TNmGAOkqbAZ5tICGAGa59yzPqRv1lH1n1my-vzROZwPYtVDLwvsrOfplhhzCDQicxV6h4f12D2Zg6J5qOFFU2ftAj_TalhGf2f20xpYatAdZPKIdUFKAaGTgeyhuHrudbsCGNpjlr3_Hv7-YswUaJbB8lThYXX69gnOTjVFYDulrpuchrWXtsOJv0z4sqf3nlgUAGW9Ric-YxXZX-dftb8LtQc8yGidgLjl9jsb06iA8FxihKI1sDRU8unKdcZGyfyrRFrBOJbW0vVjBOI7OmLfyeQI8mB54DI6R8Z3HP8fe5uxj_DCGFui52EF340N8F-NyejzU8nGwbHnARzZUORamM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بورب مودین ، مأمور کا گ ب : همه دیپلماتها جاسوسند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20686" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20685">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یک کانال تلگرامی با دوتا فیلم از اون لحظه مدعی شده که نیروهاش "حمیدرضا رجب‌زاده"، بسیجی و مداحی که دو هفته‌ای هست گم شده بود رو به هلاکت رسوندن. علت کشتنش رو هم گفتن که این مداح جزو نیروهای سرکوبگر بوده و در ۱۸-۱۹ دی، تک تیراندازی می‌کرده. دقایقی پیش خبرگزاری‌های‌رژیم…</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20685" target="_blank">📅 19:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20684">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیویورک تایمز : ایران فهرستی از درخواست‌ها را ارائه کرد که امیدها را برای بازگشایی تنگه هرمز کمرنگ می‌کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20684" target="_blank">📅 18:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20683">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‎معاون ترامپ، جی دی ونس : ما توان نظامی ایران رو به‌طور چشمگیری ضعیف‌تر کردیم
بعضی‌ها داخل نظام ایران درباره موضوع "عوارض" صحبت می‌کنند
اما ایران به ما گفته که هیچ برنامه‌ای برای گذاشتن عوارض تو تنگه نداره و قصد چنین کاری رو نداره
انتظار ما اینه که صادرات نفت و گاز از خلیج فارس دوباره به همون میزان قبل از شروع درگیری‌ها برگرده
ایران در ابتدایجنگ، تعداد زیادی مین تو نقاط مختلف کار گذاشت
الان تلاش ما اینه که یک مسیر و برنامه تردد مشخص طراحی کنیم
تا کشتی‌هایی که از این مسیر عبور می‌کنن، بتونن با امنیت کامل رفت‌وآمد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20683" target="_blank">📅 18:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20682">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دبیر شورای امنیت ملی ایران می‌گوید که ایالات متحده باید دارایی‌های مسدود شده ایران را بدون قید و شرط آزاد کند، تحریم‌ها را لغو کند و غرامت دو جنگ اخیری را که علیه ما به راه انداخته است، بپردازد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20682" target="_blank">📅 17:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20681">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2y5am5PWAK398x2lpvnlL4PuDjoYbU4zmBjUOVa9LYDK0siqUKbmU0E4mDU_O8fChKTI118KY-XuiHqqS9kOudwssMMdlKySPtCDs6VwZ6fhp7Dht02KcvVk0p3gsrReWH7YRwKfixz_6b0mVbanxos6ihakM0qtf1g91Lqrt3eeaUDFS6R7XRgXZms480d_hCt7e0B3BRzLah3mnneDvt3Y5vMBpU0d2IrbxFhJ6lnBtyxnlJBWNVDxkZgszyzUOgGvN_buicdDcHP7VOf0w-6YdvnTXUb_iJChFLkbEkhYkc6p4HUDj-vFws0EIyx54WZxeGkqZOqoKXnljI6HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است امروز دو بمب‌افکن B-1B "Lancer" از پایگاه هوایی RAF Fairford (EGVA) پروازهای آموزشی انجام دهند و گرم کنن حسابی برا حمله اصلی . یکی از آنها در حال حاضر قابل مشاهده است:
B-1B "FROWN30" 86-0124
B-1B "FROWN31" (در انتظار تایید)
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20681" target="_blank">📅 17:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20680">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXGZxQ10u02et7HKdQsRKsTACAILSJjx5ACQKWld_QzyxusIp-CyqzOdkJR8evVQEX0itfCy0qOnTopdUfpI_gr-styzz-XgK6uEZ378rJmG6MefiRDXGYATbRulglTPM25dDNqoLOt8CeAjLL9YBPLVHantrs4M1knzVgmPhPzCLoGXUMLp0LmNEyIgbC8bN7vuQNGcjTNFnSLOIQEj5l-QCUzyw-4cYugLeLDq8tQuWm7QdBaJMPaFV_seYujQ_IWFUTESSqdsjPMrLC_Io1CKnv1rwrdDyk4cDYcym7Nng6hixKtWIjXbr13UMdueoMYDv4jm7_FD0Db_Qk4PXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از حادثه‌ای در ۱۸ مایل دریایی شرق خصب، عمان دریافت کرده است.یک منبع موثق گزارش داده است که یک کشتی مورد اصابت یک پرتابه ناشناخته قرار گرفته که باعث آتش‌سوزی شده و آتش خاموش شده است. هیچ گونه آسیب زیست‌محیطی گزارش نشده است. کشتی و خدمه در سلامت گزارش شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20680" target="_blank">📅 16:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20679">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb62efb6b.mp4?token=KCSD_nwqYMCWoSY2hplKW2-QhtwKxJtehgBE38smbwotkpW6r7IxwS9LQKDY4XqewQjBnTf6_dkNMolZVZ5RljXEvm4EezQ7mhhpFKDe2z5dxgE1Qi1NMugbmRUn-n5dN_l902iVbMYMj4DX59p4-6vE2iGw4NT0s7727ipZFtwViAPmNUF08vmvxQohqjyD6vOgMsr-sPz2_alBlmMLWGLsBhk7UbInAnMNrNkHOuNODLjq552V0gHS_ymxl_hn_NLYTlSN1zu5lkG57vP-0bJA9ngskRkvZuJreYhl0MeEu586b9wurccgpejxKXgp6eCuVx1ulZSUWJ5619fIdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb62efb6b.mp4?token=KCSD_nwqYMCWoSY2hplKW2-QhtwKxJtehgBE38smbwotkpW6r7IxwS9LQKDY4XqewQjBnTf6_dkNMolZVZ5RljXEvm4EezQ7mhhpFKDe2z5dxgE1Qi1NMugbmRUn-n5dN_l902iVbMYMj4DX59p4-6vE2iGw4NT0s7727ipZFtwViAPmNUF08vmvxQohqjyD6vOgMsr-sPz2_alBlmMLWGLsBhk7UbInAnMNrNkHOuNODLjq552V0gHS_ymxl_hn_NLYTlSN1zu5lkG57vP-0bJA9ngskRkvZuJreYhl0MeEu586b9wurccgpejxKXgp6eCuVx1ulZSUWJ5619fIdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌های توپخانه‌ای سنگین ارتش اسرائیل به شهرک المنصوری در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20679" target="_blank">📅 16:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20678">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‎فایننشال تایمز: محاصره دریایی آمریکا بر ایران، صادرات نفت از ایران را متوقف کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20678" target="_blank">📅 15:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20677">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f01922dde.mp4?token=Yh5eHzOoTcCH1qitnMNpIRTBDUlw6JJ7cTCACEumlHI-wGn_AIxrKVHwlSfh-G4tzEhLMQnfYrmMghmwhpS2CdlpKpGEhlHwKhasDYoDQ6Xatd_Nj5FYJCOUg9xFzHrob24QditAV_LvvkcPYlUPHFkrc0EinN621wQuDeOFO0dkyYFOc5sBKuv3Nz3WhH_pGitV-qGcNSaf_Z_lqsUwrE0vZ7C9kVHTSlOYq6C0rIuthYlnKXWNEBAyZgdwoQd2_JWbOirkDk9EOcheOibIwCBKvdhCK5M2g9urLMXAk5cVGdnNBkFFySuy-FvizZRQ01dFzPq9rzI0DXsVyRQZ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f01922dde.mp4?token=Yh5eHzOoTcCH1qitnMNpIRTBDUlw6JJ7cTCACEumlHI-wGn_AIxrKVHwlSfh-G4tzEhLMQnfYrmMghmwhpS2CdlpKpGEhlHwKhasDYoDQ6Xatd_Nj5FYJCOUg9xFzHrob24QditAV_LvvkcPYlUPHFkrc0EinN621wQuDeOFO0dkyYFOc5sBKuv3Nz3WhH_pGitV-qGcNSaf_Z_lqsUwrE0vZ7C9kVHTSlOYq6C0rIuthYlnKXWNEBAyZgdwoQd2_JWbOirkDk9EOcheOibIwCBKvdhCK5M2g9urLMXAk5cVGdnNBkFFySuy-FvizZRQ01dFzPq9rzI0DXsVyRQZ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسنیم با انتشار این کلیپ که قدیمی‌هست نوشت: پخش تصاویری از رهبر برای اولین بار
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20677" target="_blank">📅 15:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20676">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : فیلمی که کمر خیبر شکن را شکست…  https://www.instagram.com/reel/DbwJLvzRBwp/?igsh=YzEwMDhhc3d3em9u  بررسی اینکه چگونه یک فیلمی که همه به آن خندیدند، پرده از اسرار مهمی از تکنولوژی مورد استفاده در موشکهای جمهوری اسلامی برداشت.</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20676" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20675">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آغاز ساخت پناهگاه در پایتخت
معاون شهردار تهران:چندین مرکز را در سطح شهر تهران برای ساخت پناهگاه پیش برده‌ایم و کار اجرایی آنها آغاز شده است.امیدواریم در نیمه دوم امسال بتوانیم چند پناهگاه را به بهره‌برداری برسانیم.اقدامات احداث «پناهگاه و پارکینگ ـ پناهگاه» به تصویب رسیده و اقدامات اجرایی آن آغاز شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20675" target="_blank">📅 13:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20674">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وکیل ترامپ در پرونده حق‌السکوت، وزیر دادگستری آمریکا شد
سنای آمریکا پس از چهار ماه و چهار روز از برکناری وزیر دادگستری، با ۵۰ رأی موافق و ۴۹ رأی مخالف تاد بلانش را به عنوان وزیر دادگستری و دادستان کل تأیید کرد.
بلانش پیش‌تر وکیل ترامپ و از اعضای تیم حقوقی او در پرونده پرداخت حق‌السکوت به «استورمی دنیلز» بود.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20674" target="_blank">📅 13:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20673">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال ۱۲ اسرائیل: پزشکیان برای وادار کردن خامنه‌ای به ملاقات فوری با او تهدید به استعفا کرد.
"وضعیت اقتصادی ایران غیرقابل تحمل است"
پزشکیان می‌خواهد برای خامنه‌ای روشن کند که پریشانی اقتصادی کشور به نقطه بحرانی رسیده است، تا جایی که دستیابی به یک توافق سیاسی و رفع فشار اقتصادی به یک نیاز فوری تبدیل شده است که نمی‌توان آن را به تعویق انداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20673" target="_blank">📅 12:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20672">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bI3EviGVSc5wv1TuIO_Y9VZtznYSYmQ78vnPv1VuN2_-6XqQ0CrX6uoIO7zGOB03HWe9wQaUlRj48rCckgUyepz8N-70MAtU4t55Gki2gNRDREBqJE8l2tX1uM82IDKfjsIf4K0-41R9NKcaoSYdyCvz6fD_CAFQNeTdtY1WjAtvjY5qHBSlyCgFeu3bPGROwHzxu4ChlHygVctCANtdJYDkHrA7tn0kdq_-_dWdt_uGQF-TPFlb1ygxu2bCUXSKW-dDDkIZfRrubaUaGJAerQo8QXb0G8PkFZOlE8sLc3V8xFP1e-Melk_Gok2UNahIugKpZdnjhI5dJoqaJIypxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کانال تلگرامی با دوتا فیلم از اون لحظه مدعی شده که نیروهاش "حمیدرضا رجب‌زاده"، بسیجی و مداحی که دو هفته‌ای هست گم شده بود رو به هلاکت رسوندن.
علت کشتنش رو هم گفتن که این مداح جزو نیروهای سرکوبگر بوده و در ۱۸-۱۹ دی، تک تیراندازی می‌کرده.
دقایقی پیش خبرگزاری‌های‌رژیم خبر کشته شدن این فرد رو تایید کردند
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20672" target="_blank">📅 12:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20671">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20671" target="_blank">📅 11:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20670">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90587b68aa.mp4?token=QENoeQyJf51UjD1pH2uAw6Svn5n7-pO_gy9UnIkgl2DQWRudWPVzPKdPUq6hlPet2Ee9yJGA4x8Axy9l1T50p16XU6aZxs-0NA5J-6yxUOmc0bZC1DjsMIA-eq63yso43IE13k2sW9hzm3EZ9UMHfKUcusX87cZrF3oSYOVQShJo-Glw5pHOWcsuowYSGHvFrNKLSv3Tk5eCqiKzwzDnyg68Ineds7l0qIZWHmGd3GyFnMBXM24IdEau-8irTnPkfAWJZqcqDLRQkd_36TzNJyYbU0XDCTI3WNx9LMTRK__eMJQjcaGNEcUnZMfbbsS6cwI98kUc2nS5HoUxnk38yQ_TpWF39U0uRm7gYectE3lA7gma4uTtOjlNMqVJuRbV29oiKPamOMa4YEfBbBo7Ie42__OH4F9o-IhOvIDWlnr6xe82kDhhuhrli-E38rFMVwYAl-6QQ45Q5JolmlEKg8WjuFlG6OoXnpbpgjzFZ8kH_R_25NXylZ_E-tpHDvMAKM44QTyQlynH-VH4S3Fvn5ZyJpmBSf_rjzMSKYHcQw35foFB2RORUicnodiIdaG7JkVSes_1P58kOFMohhx34Ikj6TtxxVl7NuodmdMKOCBL9ZKSU21criKpXATP8p5ft3s55ffB_zQAB87dncuXlflGgWC2d_APVfvrAvJ4A3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90587b68aa.mp4?token=QENoeQyJf51UjD1pH2uAw6Svn5n7-pO_gy9UnIkgl2DQWRudWPVzPKdPUq6hlPet2Ee9yJGA4x8Axy9l1T50p16XU6aZxs-0NA5J-6yxUOmc0bZC1DjsMIA-eq63yso43IE13k2sW9hzm3EZ9UMHfKUcusX87cZrF3oSYOVQShJo-Glw5pHOWcsuowYSGHvFrNKLSv3Tk5eCqiKzwzDnyg68Ineds7l0qIZWHmGd3GyFnMBXM24IdEau-8irTnPkfAWJZqcqDLRQkd_36TzNJyYbU0XDCTI3WNx9LMTRK__eMJQjcaGNEcUnZMfbbsS6cwI98kUc2nS5HoUxnk38yQ_TpWF39U0uRm7gYectE3lA7gma4uTtOjlNMqVJuRbV29oiKPamOMa4YEfBbBo7Ie42__OH4F9o-IhOvIDWlnr6xe82kDhhuhrli-E38rFMVwYAl-6QQ45Q5JolmlEKg8WjuFlG6OoXnpbpgjzFZ8kH_R_25NXylZ_E-tpHDvMAKM44QTyQlynH-VH4S3Fvn5ZyJpmBSf_rjzMSKYHcQw35foFB2RORUicnodiIdaG7JkVSes_1P58kOFMohhx34Ikj6TtxxVl7NuodmdMKOCBL9ZKSU21criKpXATP8p5ft3s55ffB_zQAB87dncuXlflGgWC2d_APVfvrAvJ4A3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش ویژه آژیر خطر از فاکس نیوز: سربازان آمریکایی در جنگلهای بنگلادش تمرین آمادگی می کنند, حکومت ایران یا توافق را میپذیرد یا بمباران میشود. آیت الله گی قدرت پدرش را ندارد و اختلافات بالا گرفته… و عناوین دیگر که در این ویدیو خواهید دید
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20670" target="_blank">📅 10:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20669">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxxEMZiAE0hq7zoo_JTqG0GPMhU4rX3cA1OUzxh2hr8z5284MoWPwLyuWrfIqyXthKtY_5cJVpembDjyFmlfV4S-bSf_ULlyyt8XQxX7j9cIsZc62KRqGBlKC1UuZGIQ607osV0mcqkC9mCAyUChTLHAFn-n8Gbj-BzCbhWgJj0UMTyykAFiqiBHnco9UqpyNU99dMPMQqFwvKr56qG6R-SmFE3QbJz9p37rzyckjl-EtUVMw4FeNnhtO1KXpkMMQAJ7MlYyELqXyAgUwvxpl8hpkMAX5IluO6ncsi6s7akClAQdsYKQ5AGF0NnCqdcsnu1v9lv7K0_8cceG4GkwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن روحانی توی خونه خودش یک هیئت دولت خونگی ساخته با هم جلسه تشکیل میدن و خاله بازی میکنند!
@WarRoom</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/withyashar/20669" target="_blank">📅 09:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20668">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سفر مکه
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20668" target="_blank">📅 02:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20667">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shkX0nZpG_5zXtgvnxQWmlhuqoU6l49t6jnZgP8BgPzK4zC6yHvBUtPex-T26ATVe2Rk_Nwy87LzXFdxHKxOzv6M1x22mqLfdIsY7W70eWkK3OePxDA-aXWtTJknJJaKZs6YcAq5UtqxGqMC9zZJDapFlGkNjaYLfYdZtFoHh5OO8KI5rV78WkiJru0TRTBLoS4ynrVMbqmcGG7v1Uo2k3-XIDknOHQI1o-dLhVEqWMdaRWgpr5uMUHz7tKroHt07ipaqgTFEgiDkCWVn9t5klZeyw4NKRfZ3sy3QkvjHZxvE-NIxfmbAhFL7YUNRMg0lTDt-XrLdm7cdm3tfW4U3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین به ترامپ : کلکشون رو بکن
@WarRoom</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/withyashar/20667" target="_blank">📅 01:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20666">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20666" target="_blank">📅 00:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20665">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هربار نا امید میشم یهو میای و با انرژی ماوراییت میکشی بالا منو. نشسته بودم در اوج نا امیدی عرق میخوردم، کانالتو باز کردم و ویدیوی آخرتو دیدم‌ و چسبیدم به سقف. خیلی خفنی خیلی آدم حسابی هستی عمرت طولانی تنت سالم بمون برامون یاشار
❤️
🧿</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20665" target="_blank">📅 00:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20664">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">هربار نا امید میشم یهو میای و با انرژی ماوراییت میکشی بالا منو. نشسته بودم در اوج نا امیدی عرق میخوردم، کانالتو باز کردم و ویدیوی آخرتو دیدم‌ و چسبیدم به سقف. خیلی خفنی
خیلی آدم حسابی هستی
عمرت طولانی
تنت سالم
بمون برامون یاشار
❤️
🧿</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20664" target="_blank">📅 00:26 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
