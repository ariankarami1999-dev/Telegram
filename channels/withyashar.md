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
<img src="https://cdn4.telesco.pe/file/Tr2qaGWDeCWS59IZD8ajN28a9Zq2zIH_veViWfXPI11t_FWB7HdaRQw56vAn7epoTznmBsnlD7P1bbWxXZb3ln145cBVWcVSKoE7Y7pw1TjYXBhRRjlMUCulAIT1UxFX7qZ4uHwrLfJgiyY2Y-2I8sM28Uj8CG-JDTkx8HQlg-qQSPhpqEMNRAeMa_3kcBrAFgYijyVDTKi61xxxd0WvtstGL-MZWNp7JB6YrymhZalIquSHdl9Q3jlTyZQnnsB5r8hZTw_JXjafNUk6_G-UidBYVT2N-6ZiHmQyUl3Xp6bnvG1bAgnMP-Yf_FPuu6HagXq1_2sEuqt4KC3GugSP5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 446K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 18:58:47</div>
<hr>

<div class="tg-post" id="msg-20766">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHl3r-kFR-piaRfoAvwgqz4gTeSDGAxkRvvGtovr_bgy2j83MHOk4q6ktUdns3xkGcmZSF6cKubpwPCI4aURksxuRnXKDYJj71BHHxyzn1iuEoR5plWn7EMzGy02t-xOfZACZO-7jFvyuOGvcZ8JZ6gDall7SHMeYLxY3BNId1QTq8v5eFiDrWMT_ej7zvm4hr6QEhve-bxx5Ta4tMfyPmbdFLsRTM_s7EyOY_ZwIkCW35yjDtIRxa3s3ZxpZh6tgurNYT3Zw_qxzDL-8kV0vv8cddBvEW28OFpHGbeGu_tCyE8iyRoygx_tg6ix6_rwQMPxmuRPEiZIR6jYWu1rjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ : عاملان کشتار جمعی اکنون کنترل ساختار نظامی و امنیتی ایران را در دست دارند.
ایران به‌تازگی قدرت را به‌طور کامل در اختیار دو فرد تحت تعقیب اینترپل قرار داده است. محسن رضایی اکنون با اختیاراتی هم‌تراز با رئیس‌جمهور، ریاست شورای عالی امنیت ملی را بر عهده دارد و احمد وحیدی نیز با اختیاراتی در سطح رهبر جمهوری اسلامی، فرماندهی سپاه پاسداران را در دست گرفته است. هر دوی آن‌ها به دلیل نقش ادعایی در طراحی و سازماندهی بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در آرژانتین، تحت اعلان قرمز اینترپل قرار دارند
@WarRoom</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/20766" target="_blank">📅 15:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20765">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وای نت : ‎نتانیاهو قصد دارد انتخابات 27 اکتبر کنست اسرائیل را تحت تأثیر حمله جدید به ایران قرار دهد تا ائتلاف لیکود متلاشی نشود
گزارش ynet می‌گوید نتانیاهو در شرایطی قرار گرفته که
تهدید ایران و بقای سیاسی شخصی‌اش عملاً به هم گره خورده‌اند
؛ زیرا اگر بدون یک دستاورد بزرگ وارد انتخابات شود، فرسایش قدرت نظامی و نبود موفقیت سیاسی می‌تواند برای اردوگاه او هزینه انتخاباتی سنگینی داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20765" target="_blank">📅 12:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20764">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecy1hqXO_X2a_4XmBNP6IA_uKMoetYPDANV7sdYyZijALDvqp-liaXeQ0LiHWk5r1D98_4wGOwQWE1TfFZNJWrg_JBm2rrS5EOWFlzldKQExoFiQk0EbZdmzrYkvzrxmSBIHd2sXl3OtzZjJHWRIfEd86Qb6VtRxnq2fz0XrRGYdP-er8av57diRJzAixCuXTJ3jBatSEcMjMbqucGehxeexc439AK5AkVwF9HTl4LTwMY1j7ob6J5DgmZxsqL8VqIZzspAybBjGEkfR3Bkf6NM7hdCNkgJaCgb41B_NsCkYVvvli1GR8dnCUTk4IPWIiOaGJh8-Yc2Wt4gOWHMY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور محمود بوتاکس در جلسه دیروز مجمع تشخیص مصلحت نظام
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20764" target="_blank">📅 12:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20763">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مقام ارشد به کانال 14 اسرائیل: بزرگترین ترس دشمنان ما این است که نتانیاهو در قدرت باقی بماند.
خب،این به چه معناست؟
نتیجه بگیرید.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20763" target="_blank">📅 11:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20762">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مجید شاکری ،مشاور قالیباف :  ترامپ با ما توافق نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20762" target="_blank">📅 11:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20761">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">باراک راوید ، آکسیوس : یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «نگران یا ناراحت نیست» و آن را بخشی از فضای رقابت‌های انتخاباتی در اسرائیل می‌داند.
این مقام آمریکایی گفت: ما نیازهای سیاسی بیبی را درک می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20761" target="_blank">📅 10:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbdnkiPypyzW1X7nmigqC-Spe7qLULSvK62UlbU5ljhYHokmAghE086lAuqqlTivK7Gk31SulN2sLyAD4iqD3nWK4vS10Zn1T7gEp7gzXh77lI5FiLg-Mo20720X826LOWtSj4VTO0oEpIprAmJRgOXr4vJIFdNEUKZ1r-Tjm5xb0WxeZqS6Hs0YOFX-Dzjy5Kq1wf7o_Inr1bm2_xJecB-s3LFv2hM6KW_NWFRshsa7uuXz1fNk6jiTE4zMUUToNDzZqiTa3MufVyxTJDXDZgRlIpBOKw21T01tsYLpYWZGbc7z1k-zvR2LfT2FfF_yoEiWfT-jcbgo0WSGfrkvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیز نیست، بی بی داره خنثی سازی و بازکردن ورودی های تونل ها رو براشون انجام میده.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20760" target="_blank">📅 10:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">مهم نیست داش یاشار مهمات عمل نکرده دوران هخامنشیان هست</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20759" target="_blank">📅 09:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20758">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbdiM9ET-ozVfpvEoltD6osL6zNo7b7Tco6BoPDhEPSUDJmIZQ4zKMPrGjGTk_UeMqD-M1Yz9vfKTziqSQS1p-D-YLXW9ZMpb41bpgtS9Vt2r2Od0Veymel6DaZU9tDWAl4LPaqhOIdaznS0O0KEPNqvqVII0XJ3H4JlL57RRY--HhhMGtoHZBBlwVPLIce9_4KLHoNrFqtBHNN3C1gMt3glEZTzEHVKCXGnzBG3SSwfU5JKWfGHVSOmXh21OcMfYsgr4dHhOdvxhTdQzqXFzrb8IkcCW8Yrml72ebkIx0Qgg_gDPS8ma_z9-9n1_wm1k42HpXWHEdTjUikp_CNidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان سمت پادگان ۱۵ خرداد انفجار جدید
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20758" target="_blank">📅 09:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20757">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtR7PoNHNRby1sGsYrPGareZ3ZOKD_hc3TCHK1TgYpBwGg7CTV7CKSb8E1UYCdBz-FkgWw8aJ8-76CUhojA1CJIj-oWSH0cG5txmWWwor2F0x7qTrFB9yzJjBU0ifTPRQm53yOuhZvbGNhalutFcO1FFebKw5eLFiZ-LKkEvrglSr0241ync24ujGCiPOIOV9xyERP9UAP4p4t8bqRT0BlQQ_bVs57RPidnHbE-s46cKhSdbHki05cjlNtKe-B5XVanPKKuCMhhE5x9NjiQl_CszWPNCjx-h6xL1NLlRoeEfON90KGPToBuEqJhE4PQNh6xHjoCNSuZZ39fNkio6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو انفجار شدید در اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20757" target="_blank">📅 09:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0rGoUSc-VshvLifn6LO-ud2mTsUSIGMzY8T0OrQZbULoByjuAQPVwEN458VUWqu-LQHvlSQfHX9F5ro46I7on11XqkOXujtvns1hAvjeD0p0mKPA87e8CrbPaGNGDQw2NxpOPJ-N_VkD97KUV9be9tvJLzbzp4vvdl63UJbNV0MpgScSVbCxURzk_nClqL4qx9ADqeDNp8-tUOtxQl45DChpUXoZM8yfn6sMLdDUW8-EhN-sYDOA3G0_MdJDMsFgT2ZJ1N7emsAwsfZULpd201ry-6zUgHeZnUL-LgYtyMw74Xd0BKq0TXWtVLMDUeSe3uP795A42lUX6OuvMBcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز : زیردریایی جدید «روز قیامت» اسرائیل که با هزینه ۶۳۴ میلیون دلار در آلمان ساخته شده، توان بازدارندگی این کشور در برابر ایران را به‌طور چشمگیری افزایش می‌دهد.
این زیردریایی از کلاس «دلفین» است و شرکت آلمانی «تیسن‌کروپ» آن را ساخته است. همچنین، این بزرگ‌ترین زیردریایی ساخته‌شده در آلمان از زمان پایان جنگ جهانی دوم به شمار می‌رود و به جدیدترین موشکها مجهز است
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20756" target="_blank">📅 09:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4468b68072.mp4?token=MojkgO7b7T385qjP8Mrn36Pe-qXJriV8N4B1sUuBV7JEYUOku5B7rh4b4NF5qgD32pcaVforNTYnO7FgZwIP0DAWZIghl8NBhW-vhrLCOJZbeNqyEi7Xa4HpMgrvImMcRWjjhJ2GwuWOopR9O6fP0XfxO9cMbLKeYkN1HBqreoZBJC5kA10bvUDvhfOKNWewgW6zAu1QMSFtSNq2heQT5JkTsj9y720onF2Mzv8QG_pCIYw3lzPdt8lUMbT6ApYoRI3Nuo4nU_zs5LsUBb_GGiWd3wAFqtyG7hY---45EXcMSTqk5G8Ur34VtMtrgUuhhrZ6Eq8iz--GJMY80-05QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4468b68072.mp4?token=MojkgO7b7T385qjP8Mrn36Pe-qXJriV8N4B1sUuBV7JEYUOku5B7rh4b4NF5qgD32pcaVforNTYnO7FgZwIP0DAWZIghl8NBhW-vhrLCOJZbeNqyEi7Xa4HpMgrvImMcRWjjhJ2GwuWOopR9O6fP0XfxO9cMbLKeYkN1HBqreoZBJC5kA10bvUDvhfOKNWewgW6zAu1QMSFtSNq2heQT5JkTsj9y720onF2Mzv8QG_pCIYw3lzPdt8lUMbT6ApYoRI3Nuo4nU_zs5LsUBb_GGiWd3wAFqtyG7hY---45EXcMSTqk5G8Ur34VtMtrgUuhhrZ6Eq8iz--GJMY80-05QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در واشنگتن دی سی، در پایگاه اندروز فرود آمد و مصاحبه ای‌ نکرد که به نظر من بازی با رسانه هاست تا در خبر های‌ زرد و دروغین خود غلت بزنند تا غافلگیر شوند
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20755" target="_blank">📅 02:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOO1UJq98eMOL6OaHLXOz6X9yPj-kdW16h10gSkxyOyMUUF8Mfw8223zYgPOUqP0CBI0vbCkjJEsIfqfSU2T-Uajyur-FspLmhDUlKyZIEpKMbrTIWVJMg1bcqUQq6zzOzB-cLW5NOBQ1x5cOLKcnkYVAD-SyWzTuzhTQGsvynjS6RaEc9esi7_l6--pAwuvgsWQJJYK26wue0tP72WYag5GZoLWYgNOKjkDCjZ1wNlEAVltn8Ut0RJ5HOMo5BEzrmOpYS4WC9w5MQX6d9wEHpZJIEMuEkl6W5yynZR5Ea9LMAaq4wjCIChc_z8CwsQv64gsS-j3fna92A_kgBahFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : تا اینجای کار امشب در حالی که در سراسر خاورمیانه آرامش برقرار بود، در ساعات اخیر، حکومت ایران تعدادی موشک به سمت یک کشتی که در حال عبور از تنگه هرمز بود و توسط نیروهای ارتش آمریکا اسکورت می‌شد، شلیک کرد. سپس، آمریکا و عربستان سعودی تعدادی…</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20754" target="_blank">📅 01:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اتاق جنگ با یاشار : تا اینجای کار امشب در حالی که در سراسر خاورمیانه آرامش برقرار بود، در ساعات اخیر، حکومت ایران تعدادی موشک به سمت یک کشتی که در حال عبور از تنگه هرمز بود و توسط نیروهای ارتش آمریکا اسکورت می‌شد، شلیک کرد. سپس، آمریکا و عربستان سعودی تعدادی پهپاد به سمت جنوب ایران پرتاب کردند که پهپاد سعودی توسط سپاه رهگیری شد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20753" target="_blank">📅 01:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20752">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20752" target="_blank">📅 01:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بلومبرگ: توافق هرمز همچنان دور از دسترس است، با توجه به اینکه ایران از مذاکرات مستقیم با آمریکا امتناع می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20751" target="_blank">📅 01:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20750" target="_blank">📅 01:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">روزنامه کیهان : اردوغان و شهباز شریف مثل روباه مکار و گربه نره بن سلمان را سرکیسه کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20749" target="_blank">📅 01:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20748">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead9f1f71d.mp4?token=CxE7JXE6eZzbk2bWgXhtCXLrmiYA_QnisgnSg82fy_eYPdqaltcilZrfaeRQKxkyUL-qHhjYtWvPBcnDrbcBCEpn-TdIy2O0yp-qIjQfPib798TsewTwkAmpQTWNgtBF9uhOsZ5RFAsPQeF2feYdZkZoWZx2SHiHEFoYHP7janaFgZBc7xqxDG2I7GQQkhkcuAN8hBFZ43SfyUzfOyvJ3ZtFV_39KkB1TeQPUNCdr7gGYYanuUPAKJBhe116zCD3ND1zhZ0RwIwHDZXSe9ExoJaz0N-uAGPIf3yYL6vStXf0h0GcVLd6CzCeaZHpRVpiczoBnYrWFyXCnNQ0V4X8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead9f1f71d.mp4?token=CxE7JXE6eZzbk2bWgXhtCXLrmiYA_QnisgnSg82fy_eYPdqaltcilZrfaeRQKxkyUL-qHhjYtWvPBcnDrbcBCEpn-TdIy2O0yp-qIjQfPib798TsewTwkAmpQTWNgtBF9uhOsZ5RFAsPQeF2feYdZkZoWZx2SHiHEFoYHP7janaFgZBc7xqxDG2I7GQQkhkcuAN8hBFZ43SfyUzfOyvJ3ZtFV_39KkB1TeQPUNCdr7gGYYanuUPAKJBhe116zCD3ND1zhZ0RwIwHDZXSe9ExoJaz0N-uAGPIf3yYL6vStXf0h0GcVLd6CzCeaZHpRVpiczoBnYrWFyXCnNQ0V4X8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پهپاد ساخت چین که توسط نیروی هوایی سلطنتی عربستان هدایت می‌شد، در سیریک، استان هرمزگان، ایران سرنگون شد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20748" target="_blank">📅 01:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بازهم صدای انفجار/پرتاب از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20747" target="_blank">📅 00:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dg4Aa0UKH3LGUtXtlmlagJibzOep1kI4-tf2Jt19dnU3bTdI4Z6CaOHL5rtaNB3LjjiNdbaviP32whshZs1KuyTM-w7SIVuRUSlaxlCPJA3MFMRFpnbnRPi6yHYkxSnY5pZy2SpYrBezAxKusbDTcWEj_YPsPuyBvMyP4RKX35_ohI5YqsoNyussBYdYUiFjWRpROy0io50b-bYuAuzU8iAqaCZlJtfw22ezr68oSV7d1dVAlwfjToVc_I-3Q9hdeSqOJHSq1fLeMS8yJQaxvSbK3a_cEg0lXFoy-3yqP5bu5BpDYzID573hNdCRdob5YfLBXG-AGvtI-DjUolVuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث
: 51 سال رفتار نامناسب ایران!
@WarRoom
حالا چرا ۵۱ !؟ ۴ سال آخر شاهنشاهی هم قبول نداشته ؟!</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20746" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20745">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20745" target="_blank">📅 00:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش ۴ انفجار در تنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20744" target="_blank">📅 00:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوباره از سیریک موشک ول کردن سمت تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20743" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEq3_N-bDnMEAVPXQpUZsEyQiQzaP6cbMwh5ovCVBppd7lFL_7d4P7ySCpvmdxnWaR5y14PgPk_zUiCeivBV1d41G1Wgu_p4aay94Fsc1ne7-rBTJ-UjrfgrY3I5XVK3S4bN9xWAAEHkGxA-45BWPkGZLF933iTDTGggbVAt1a3P2QQ3JWt4oRy3eqGKk-KSgd880dTZACcjbg9JRR7jElhl3ZjIrfgo0A_YfkvYDfzh_-JMApPpwYJCfdIPK_yWXFul-46CheeM8mYMqFu0vJr7S_ty-mbB7v6VJIjgNdUe6qCk_bjsxOKNoHUl87qv5npUMhMAdw7fAqMb1JCr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک :
یه نفتکش میخواست از مسیر جنوبی
عمان عبور کنه مورد حمله قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20742" target="_blank">📅 00:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش صدای انفجار  پرتاب  موشک/پهپاد از سیریک @WarRoom
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20741" target="_blank">📅 00:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20740">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20740" target="_blank">📅 00:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20739">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شبکه i24 NEWS: اسرائیل فاش کرد که رهبر حماس، "باسل صالیه" را از دو سال پیش بازداشت کرده است. این خبر پس از دستگیری او در شهر حمد منتشر شد. این گزارش حاکی است که او پیش از این با سنوار و الضیف اختلافاتی داشته است. اسرائیل او را مسئول شلیک موشک کورنیت به یک اتوبوس در سال ۲۰۱۱ می‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20739" target="_blank">📅 00:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve0sNsWnvBz4brAhbQWYR9bLwc4izhD2J-GV2vXDuODpz9LwIq5RxrxD9H_5_F2ch_t2HmP2nOv7SvM_Kiqp1k-nZD1Y5v-JGZE5r85-BUstmNOhjw0WIoqRIOs4jUlDd9B38tTIjwjRazm7UPqI9RFqMpRiMUYnARi2xLFwqi421QYrZuVRojb2dATbEcuDUUwfIamZoKvY1BElD9UabAV0VmfeQN93VUX9Rja-5fmG_jxjmlWKOWgT1YwVNA0B9O6DlIvFGw4e2DVjCpjRjDFmw7uot_psqFGy5BBy0kCe6ZUiYBPwArBJ3aKnUyzAglxbwd7arDoTllTm1tjI0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت پیشرفته‌ترین نسخه عملیاتی خانواده E3-Sentry (آواکس)  بوئینگ E-3G Block 40/45  از پایگاه رامشتاین آلمان به سمت منطقه خاورمیانه،
با مشخصات :
قوی‌ترین ارتقای انجام‌شده روی E-3.
رایانه‌ها و نرم‌افزارهای مأموریتی کاملاً نوسازی شده‌اند.
توان پردازش اهداف بسیار بیشتر از مدل‌های قدیمی.
لینک‌های داده و ارتباطات پیشرفته‌تر
و موارد بکلی سری بسیار زیاد انجام شده
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20738" target="_blank">📅 00:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش صدای انفجار  پرتاب  موشک/پهپاد از سیریک
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20737" target="_blank">📅 00:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=lP6qX46WCrWYnCWl4N9ZK-ydAb0MNOeo4urRgwyUdwtuC-QwQfAee84fyAEOdJ1LmXskBkwz4CGOA35OLA0mJRGqfb7mzjiUfX8CRwCAqRLXO9Eop_3eEXtJ1y-nftETiHc8OnKZtvZI5ZxyXfe2BLWsAhUfZLY2xTlO6-7-OkDNahnjgX1-KHdhIqHliVvcGO4eekdd_WPQ-YK1zujYWHImPRKI92RcfXoK3grAtLeKuNclRVno9e2ZA1QjcmxGPgERiiEE99XGlvWayL7S1_UmbFVCeGNBw2L0ghXuw2539pjs5Shf4c7HTPsfAid6TR3KIilpKBymA2p6xApxy0hrTaSvUAc4dXB_cwVdsgdEipUtbybXpKxH5N_-3NvFgeqrha4YJcN3aYBltuzcAiCVAeKH0gBbjotti9wTkMNpeQ2wlbesHyDxivQvO_jeBXVuZGX_UrK6IuP7PwLGeGxUH5f8ewA0KbNy-jYriZfZVP0GPif7rZHE8fTVyewTqcVqHYOezUkD79XIVSVVCvmwbUzM0le-6j-zMHluDhVbXLK3l5QWvWN2kWVPIKIqE_zpiUum_UwF96_C5-SUU8PQYnjxJy4IV6bT9GnZQ9NWOhO4CgLVh-NObkR_9WQ50c92i-YQhE_9E_AskY8j0oFrYQWjbsewok-IRVihPm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=lP6qX46WCrWYnCWl4N9ZK-ydAb0MNOeo4urRgwyUdwtuC-QwQfAee84fyAEOdJ1LmXskBkwz4CGOA35OLA0mJRGqfb7mzjiUfX8CRwCAqRLXO9Eop_3eEXtJ1y-nftETiHc8OnKZtvZI5ZxyXfe2BLWsAhUfZLY2xTlO6-7-OkDNahnjgX1-KHdhIqHliVvcGO4eekdd_WPQ-YK1zujYWHImPRKI92RcfXoK3grAtLeKuNclRVno9e2ZA1QjcmxGPgERiiEE99XGlvWayL7S1_UmbFVCeGNBw2L0ghXuw2539pjs5Shf4c7HTPsfAid6TR3KIilpKBymA2p6xApxy0hrTaSvUAc4dXB_cwVdsgdEipUtbybXpKxH5N_-3NvFgeqrha4YJcN3aYBltuzcAiCVAeKH0gBbjotti9wTkMNpeQ2wlbesHyDxivQvO_jeBXVuZGX_UrK6IuP7PwLGeGxUH5f8ewA0KbNy-jYriZfZVP0GPif7rZHE8fTVyewTqcVqHYOezUkD79XIVSVVCvmwbUzM0le-6j-zMHluDhVbXLK3l5QWvWN2kWVPIKIqE_zpiUum_UwF96_C5-SUU8PQYnjxJy4IV6bT9GnZQ9NWOhO4CgLVh-NObkR_9WQ50c92i-YQhE_9E_AskY8j0oFrYQWjbsewok-IRVihPm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) اعلام کرد که جنگنده‌های اف-۱۶ این فرماندهی، چند هواپیما را در نزدیکی باشگاه گلف ترامپ در بدمینسترِ ایالت نیوجرسی رهگیری کردند؛ زیرا این هواپیماها بنا بر گزارش‌ها، محدودیت موقت پرواز اعمال‌شده بر فراز آن منطقه را نقض کرده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20736" target="_blank">📅 23:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20735">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کانال ۱۳ : اسرائیل به فرمانده سنتکام اطلاع داده است که در صورت توسعه برنامه‌های هسته‌ای و موشک‌های بالستیک ایران، به ایران حمله خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20735" target="_blank">📅 23:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20734">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به گزارش اکسیوس، توافقی برای کنترل عبور و مرور از تنگه هرمز بین ایران، عمان و ایالات متحده مورد مذاکره قرار گرفته، اما چندین روز است که در حالت تعلیق مانده است.
مقامات آمریکایی می‌گویند اختلافات فزاینده‌ای در درون رهبری ایران وجود دارد. گفته می‌شود یک ساید به رهبری رئیس جمهور مسعود پزشکیان، به طور فزاینده‌ای نگران فروپاشی اقتصادی احتمالی است و معتقد است که تهران به توافقی با واشنگتن نیاز دارد. ساید دیگر به رهبری فرمانده سپاه احمد وحیدی، با امتیاز دادن به ایالات متحده مخالف است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20734" target="_blank">📅 21:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20733">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دونالد ترامپ، به آکسیوس گفت که ایالات متحده در قبال ایران «فعلاً با سر و صدای کمی پیش می‌رود»؛ اظهارنظری که نشان می‌دهد واشنگتن اجازه می‌دهد فشار اقتصادی افزایش پیدا کند.
ترامپ گفت: «ما فقط به‌صورت نیم‌بند با آنها مذاکره می‌کنیم. ما فقط داریم ایران را زیر نظر می‌گیریم؛ با این تورم شدید و این واقعیت که پولی ندارد.» او با اشاره به وضعیت اقتصادی ایران مدعی شد که این کشور «در شرایط بسیار بدی» قرار دارد و در پرداخت حقوق نیروهایش با مشکل روبه‌رو است؛ آن هم در شرایطی که محاصره دریایی آمریکا فشارها بر ایران را افزایش داده است.
ترامپ درباره رویارویی با تهران گفت: «همه‌چیز درست خواهد شد. همیشه درست می‌شود. این مثل یک بازی شطرنج است.»
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20733" target="_blank">📅 20:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20732">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اکسیوس: میانجی‌های قطری و پاکستانی اطمینان داشتند که این توافق روز
چهارشنبه
اعلام خواهد شد، اما از آن زمان، چشم‌انداز دستیابی به توافق کمرنگ‌تر به نظر می‌رسد
یک مقام آمریکایی مدعی شد که حدود ۸ میلیون بشکه نفت هر شب از خلیج فارس از مسیر کریدور جنوبی تنگه هرمز و با هماهنگی ارتش آمریکا خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20732" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20731">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRmct7--vMnwlnCyvv1EB-EFOfa5gW1Izon2Cwf_R46dkSnGIhF0ynnAksxbRA5DKpjEohHV3WYqgsuE2d-pzzvOCAUIDT-rPJngIEg9V3DP4oq_k_-e8-npVSH2Ob_BH3vKzBFQMnG2V-4tTmbpl1CEJoZHD5Cp2OcDpX379LfSuwKAClBsnsgptKyWXAxHtap580E1BC5cFvc8OPmceq1iyppWfne82bFYE3lsRDcECwSLiwd2bvr0UXtPQq40Gqx9DMh2zse9OuAkCyveXxsDE-ZP7Macu-ATcphYPsiZvbSWXNBJE4kmq0F--8zilbpLR9KOXhLnZ26cGPqK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : جت‌های جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در آسمان خاورمیانه گشت‌زنی می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20731" target="_blank">📅 19:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20730">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حسن قشقاوی، سخنگوی کمسیون امنیت ملی مجلس، اعلام کرد کلیات طرح «اقدام راهبردی تامین امنیت و پیشرفت تنگه هرمز»، با اجماع همه اعضای کمیسیون حاضر در جلسه به تصویب رسیده است.
- کنترل بسیار بیشتری بر تردد کشتی‌ها در تنگه هرمز اعمال کند.
- برای برخی کشورها یا محموله‌ها محدودیت یا ممنوعیت ایجاد کند.
- برای عبور کشتی‌ها نظام مجوز و در برخی موارد تعرفه یا عوارض در نظر بگیرد.
- از تنگه هرمز به‌عنوان یک ابزار فشار سیاسی و امنیتی استفاده کند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20730" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20729">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رئیس مجمع تشخیص مصلحت نظام:
به هیچ قیمتی از موضع خود درباره تنگه هرمز عقب نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20729" target="_blank">📅 18:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20728">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=ejuljQ7g2E5jjF5wT8QrRgISLg9nCA7YJlJx-AYQ2JJXi00o4z6AeOWr2wAxI55x4FAmjZ74a8kUx9xr9tEHoQy0WUNaGNd8LG3VboydGclZpDywJgnV4FGegKz21t6B9yR7Yv8yqXpXFvnd51hTasj-T77zf-TVbeRWRM4J-mfkf0anpeF9t5YbjoS-zfhUEe3hPRBSEurGr7rHkPSENypynY6FYOKQVq8irRxTzjPhEoGweetM7j4Bk17CAK424r3xnbP_CwG8M1eISBsgiyO3ohSdz3CQ9unc35OpPEoqb3yzUew0UXWGAym94CzJHuoOdA3j_IrfwTgOufb_JZXRPBq_dx9nr6h_7sD2aaxbUSb1H6G0sM8axlBLi_7an9KTdJK-vzP7lwF6bW4tFPjFtn3rE03jv1Tbc77hhT7jp3-vFFHEJIw0VtmRtk6RPoRARv_WPX0VAZ7qTaWxZg6dreEoWWjm-QFMbY5zq_nKflnqAEL7tQgEp4D3oxjQxY7bWbzAR2EILbp-Ba5dievQ-EsmQ7KUeHh_CPd_53JIcGBZ1ej-SzDOu5gIpSMptrs3FDj9RcpokIcQk-5jAA_TH9Gbo87Mjja2MFkofxaAKXExFY_egcLf5HyvzDk3tqZ1TBIYo5xa-dys9HwDAVfzPgrIEo_zGS06v4L0lfo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=ejuljQ7g2E5jjF5wT8QrRgISLg9nCA7YJlJx-AYQ2JJXi00o4z6AeOWr2wAxI55x4FAmjZ74a8kUx9xr9tEHoQy0WUNaGNd8LG3VboydGclZpDywJgnV4FGegKz21t6B9yR7Yv8yqXpXFvnd51hTasj-T77zf-TVbeRWRM4J-mfkf0anpeF9t5YbjoS-zfhUEe3hPRBSEurGr7rHkPSENypynY6FYOKQVq8irRxTzjPhEoGweetM7j4Bk17CAK424r3xnbP_CwG8M1eISBsgiyO3ohSdz3CQ9unc35OpPEoqb3yzUew0UXWGAym94CzJHuoOdA3j_IrfwTgOufb_JZXRPBq_dx9nr6h_7sD2aaxbUSb1H6G0sM8axlBLi_7an9KTdJK-vzP7lwF6bW4tFPjFtn3rE03jv1Tbc77hhT7jp3-vFFHEJIw0VtmRtk6RPoRARv_WPX0VAZ7qTaWxZg6dreEoWWjm-QFMbY5zq_nKflnqAEL7tQgEp4D3oxjQxY7bWbzAR2EILbp-Ba5dievQ-EsmQ7KUeHh_CPd_53JIcGBZ1ej-SzDOu5gIpSMptrs3FDj9RcpokIcQk-5jAA_TH9Gbo87Mjja2MFkofxaAKXExFY_egcLf5HyvzDk3tqZ1TBIYo5xa-dys9HwDAVfzPgrIEo_zGS06v4L0lfo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فاکس نیوز آپدیت آخرین تحولات تا دقایقی پیش…
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20728" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20727">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prveoNOWY-AUDUa2wt9orDzVQmkYmEa9uDROWYCuj6sZaJiSvMoPB1FiK3J1BV6gWn8q7k90xgXky4FORPPnZo2fljPUZ43fClKQ0i-yjaeHrLx0ReP6POwcR7Qys0wwNs1IHDWfZqOhEhWJfvef6LBQxjQ3o0AMUbz1-A0IkYSpzOtzIxhBYWKoHGarIZQWPOGrAIJVuKPBf98DhT0euES3nUyXD0EvNkM-sWZqeXR8Q0A2qh281grzp5kxqqKy_yT-gIPEB6zlwW0Gzj5GJosP_JukiCLQSHfreSau-FVhWSs6tcDdEp3MN0NRjrK_Hgfl4BHZwDB9mWbvkqcR_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود و صدای انفجار در اصفهان
چیزی نیست بی بی داره خنثی میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20727" target="_blank">📅 17:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20726">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77914048f8.mp4?token=WbuwfRQz8NvwS_PAlsYpgsIoTE0KmOPsNBVQrcCFX411nyY2erTo0zImCZzg3v-HiWbyevbkDHETMN5NA47xZdv03uV38KTNL2CkWLuI_y31bXG_7DBRwySX93bVQpl5vsZHRBvZkYscaA9y0mKnv7tBuFgShfFUFakiMyoDAU11ypv2_Zcv9LpzhrYP5SaIHE0fGctMrrQTU3vZA-J4CLIT77QLnjd7M96fipPOCAYKgLK4ezBAYOCxwoOVaYtietDN3u4_yovvNMtPnTwuXxEwQnzEmbh2SW_sE2mOli9rRxS-oxzHAKK6gIcsuROemRbaUw_7V1CCPz5pyh2bnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77914048f8.mp4?token=WbuwfRQz8NvwS_PAlsYpgsIoTE0KmOPsNBVQrcCFX411nyY2erTo0zImCZzg3v-HiWbyevbkDHETMN5NA47xZdv03uV38KTNL2CkWLuI_y31bXG_7DBRwySX93bVQpl5vsZHRBvZkYscaA9y0mKnv7tBuFgShfFUFakiMyoDAU11ypv2_Zcv9LpzhrYP5SaIHE0fGctMrrQTU3vZA-J4CLIT77QLnjd7M96fipPOCAYKgLK4ezBAYOCxwoOVaYtietDN3u4_yovvNMtPnTwuXxEwQnzEmbh2SW_sE2mOli9rRxS-oxzHAKK6gIcsuROemRbaUw_7V1CCPz5pyh2bnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی با جمع‌آوری ویدیوهای تیک تاک از آهنگی در وصف پهلوی یک دابسمش منتشر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20726" target="_blank">📅 17:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20725">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD0q0F03H1R7UCIkIw-5xEpSajzm9laCgT3FhY3jrrr-_J_XOEqZV9IHWS09X5FsGrs9MyJK_2dMcV_nbGvWOeUF5laOZAzRDo4u84DHl2v5DBIFU6xU_B1o1mNOAysLEBrzKf-hm6d8f_YpFnJNXjcmF3KFY99XiO4GnEef_k7X1fbESc3RpON0skDpx2i_EjUYCfv_RFxNtrWb3OFQDlqboLI666nvpXdNLuOG_8ZYvq2TT6i-0YNJrg528GFchJn9FUdATzKKEvI6JjQ_bN9pysDTfpShE8JqJi7tywiXupj3HMlP-atI4DWh7TrmTat-5ZRPTO1xlzvZ87-3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین با خطاب قرار دادن عراقچی به دولت آمریکا : این بیشرف می‌گوید هیچ مذاکره‌ای در کار نیست
یاشار: منظورش اینه بفرما این عراقچی بیشرف هم میگه مذاکره ای در کار نیست کار رو تمام کنید
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20725" target="_blank">📅 17:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20724">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یکی از معاونان نیروی شبه‌نظامی بسیج ایران ادعا کرد که تصاویری که مجتبی خامنه‌ای، رهبر ایران، را در میان مردم و در خیابان‌ها نشان می‌دهد، در آینده منتشر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20724" target="_blank">📅 16:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20723">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyH-MOZnh7wJnH_n2P-HybMGyBG77JYVmQ1HzwRRKF6VJp4OKM7boWVOZoJ9SGg4BvaTob7TAxAg74OMtkPV5R4VpC6QW0lyL7gyNYvyQvQAcXQHjfTW2GmRzlWb2Bf855g7uP4heIv8cgc8bejErr0ebY7mTbtjsTEXw6WjPzR4ggM4d7ebnsfn47attyWF6rW_wPiM-QL5PBwtcoSoqJSqJvgF1uPioV_H8yLADKRW9Bd_584-ZBq_WpNfz-ymXRfV7v55AYjYQ1ylYZ0FpgXO7dDrPxnz5arHIlw-TMERkpqHBOl4s87cXn_yz5CPJwuUhvCC1dRfOllaRYYw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هر روز پیجو میززن و برمیگردونم
پیج اصلی :
instagram.com/yashar
پیج دوم : ‏
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20723" target="_blank">📅 16:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20722">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067ef90d71.mp4?token=ATrqLRvqKEW-IIE_D9EGoB-HuzIBC-PqRtW9MnkyJve1bVSkXvcxvyvrtwAPD4jwVi_IeuMZu7ahZ3kmetpnvEdhKxn-Z_YLMuXHIk4KrIVeflVJnrzRH9QDB7_38ESKM7g35sCQQB8PkSbBXL8C8tmAr3GxGs1SFCH9SVOIUkUSosyHGcDUFfHLaNNehTn_3vKuvd7OW9F54j-VGCmFFHq-nDcKkpckD0d2jG1c8eEOM9LXBQozetR7l2d4FEnPkv7X5xfToaz-Rc-bWmzhTe51-TJ0bSAiy_wH6i2x1yDmbOgEmuUn5LuYn53gVh6TfVKEjuv6fleC2Ej0Q6vm9nRJ3nm-zcHvg2PjEk9FFq_EWrJBgka1nouCMZAqx9V2mNpvgSvlvWj73kKyqoHh0nqShawwZhxPqd5FD5quvT7E4IVxmb3lQSk-hnxk0ua80RpWU7BDAZgukkP1fn1WWBpP-D8JsOOXWRgOnpUBsk1VH97WmGNtQTZSVZtzLPoTELYAW9tYe_3sR9hrWUxha9g0Q-YSvVChlbpyLlOxBpNIOPT3KoOPE9tZrLtyGRLiSTY1gEe3RxULK1XGyOV4r_LavUoUXHOLH1S0b2o3gjqDrdAsK6sCi2XYeVoHwmCdVi3zG2tYD2TKqUFrCEo5I70igWZON-MdjFXWWo5-1_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067ef90d71.mp4?token=ATrqLRvqKEW-IIE_D9EGoB-HuzIBC-PqRtW9MnkyJve1bVSkXvcxvyvrtwAPD4jwVi_IeuMZu7ahZ3kmetpnvEdhKxn-Z_YLMuXHIk4KrIVeflVJnrzRH9QDB7_38ESKM7g35sCQQB8PkSbBXL8C8tmAr3GxGs1SFCH9SVOIUkUSosyHGcDUFfHLaNNehTn_3vKuvd7OW9F54j-VGCmFFHq-nDcKkpckD0d2jG1c8eEOM9LXBQozetR7l2d4FEnPkv7X5xfToaz-Rc-bWmzhTe51-TJ0bSAiy_wH6i2x1yDmbOgEmuUn5LuYn53gVh6TfVKEjuv6fleC2Ej0Q6vm9nRJ3nm-zcHvg2PjEk9FFq_EWrJBgka1nouCMZAqx9V2mNpvgSvlvWj73kKyqoHh0nqShawwZhxPqd5FD5quvT7E4IVxmb3lQSk-hnxk0ua80RpWU7BDAZgukkP1fn1WWBpP-D8JsOOXWRgOnpUBsk1VH97WmGNtQTZSVZtzLPoTELYAW9tYe_3sR9hrWUxha9g0Q-YSvVChlbpyLlOxBpNIOPT3KoOPE9tZrLtyGRLiSTY1gEe3RxULK1XGyOV4r_LavUoUXHOLH1S0b2o3gjqDrdAsK6sCi2XYeVoHwmCdVi3zG2tYD2TKqUFrCEo5I70igWZON-MdjFXWWo5-1_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ناتو وارد میشود
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20722" target="_blank">📅 15:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20721">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو : ما می‌دانیم چگونه در موضع خود باقی بمانیم، حتی در برابر بهترین دوستانمان، زمانی که این کار ضروری باشد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20721" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20720">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏مسعود پزشکیان: «دشمن افرادی را ترور می‌کند که گره‌گشا و حلال مسئله هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20720" target="_blank">📅 14:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20719">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتانیاهو: تا زمانی که من نخست وزیر هستم، هیچ کشور فلسطینی، نه در غزه و نه در کرانه باختری، وجود نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20719" target="_blank">📅 14:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20718">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو : در روزهای اخیر در لبنان عملیات هدفمند انجام دادیم، از جمله در منطقه تپه علی الطاهر، اما وارد جزئیات نخواهم شد.
ایران به اسرائیل حمله نمی‌کند، زیرا می‌داند اگر چنین کاری انجام دهد، ضربه سنگینی به آن وارد خواهیم کرد.
من طرح ۱۵ بندی «شورای صلح» درباره غزه را رد می‌کنم و از غزه عقب‌نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20718" target="_blank">📅 14:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20717">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یکی از رسانه های رژیم نزدیک به جبهه پایداری، با انتشار پیامی از هوادارانش خواست برای سلامتی مجتبی خامنه‌ای دعا کنند و «قربانی گوسفند» انجام دهند. در این پیام ادعا شده که «گروهی از علما» از در خطر بودن جان او خبر داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20717" target="_blank">📅 14:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20716">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با کانال «12 نیوز» پیش‌بینی کرد تنگه هرمز طی 2 سال آینده اهمیت خود را از دست بدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20716" target="_blank">📅 14:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20715">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ادعای تسنیم : محسن رضایی کج بند ،نماینده مجتبی خامنه ای در شورای امنیت ملی شده‌ @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20715" target="_blank">📅 14:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20714">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ادعای تسنیم : محسن رضایی کج بند ،نماینده مجتبی خامنه ای در شورای امنیت ملی شده‌
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20714" target="_blank">📅 14:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20713">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ادعای فارس : پزشکیان با مجتبی خامنه ای دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20713" target="_blank">📅 14:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20712">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تسنیم با انتشار این کلیپ که قدیمی‌هست نوشت: پخش تصاویری از رهبر برای اولین بار @WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20712" target="_blank">📅 13:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20711">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCyf9VkGYe4JvhP1KPMxRoT6KnVjTArVfzUh_9kBNGdPrK9ozowz4vdP4T9dmzPq03rhRMfL_zfEeiXaYKK4HCcIM_s_bkjLJTFVKPMW5TtRhqARQOw__lnCMOyv9TKmyDkWlJFLI2gq-feYPWaGrL0uBfi40-_BbpuaEGDwT2wKnI0V9ew7ekN4M2En6tfTIxPNZHIUHbuArc0Ah4VG2VxBWjAmx03SE5xO8SOuoWK4RhFA---VUp2Y2iwjIHqyFYh8f0S10UIWUI38Jx4GV3pXAkE1l3G42z8bxe7rhDez4FzI0ZfXunMOFgJlxJjipG6In3pbo16B5qhnLqeTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دو آمریکای بسیار متفاوت.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20711" target="_blank">📅 13:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20710">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from╚»میلادم«╝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsCf4bOp5r6kel-THkLfkacAPqoghgxoRDP5QDk4JoZ4i_swvD7N0JPyzuFtX4d8RoQzw6QmgUWwW1SdwjRng-3Wqn0olbgm2FvCywLLHUqUP1oQMDT2Kp1awNxjN5JKjprv6_3lCjLpl5VlDuTIPdLVMP6VYOloKs6SBiUmGhZPduKpsHNO666_x6DSbQmUEC-9rym2aMqRQmchEyzKCs-Dnhv11DAZ5Mv_aaSDp52pT5tz1jkX2Gbxbyw2pCBJU7lqtIqoBRV_vJ5fErm73qejCDllTr9s7sUGiqQhrfHfapzWgudThmqVvHMwMuli63y4y7pOP1Vy5ATdN45VLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20710" target="_blank">📅 12:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20709">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عراقچی : در حال حاضر هیچ مذاکره‌ای با آمریکا نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20709" target="_blank">📅 12:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20708">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دبیر شورای امنیت ملی ایران می‌گوید که ایالات متحده باید دارایی‌های مسدود شده ایران را بدون قید و شرط آزاد کند، تحریم‌ها را لغو کند و غرامت دو جنگ اخیری را که علیه ما به راه انداخته است، بپردازد. @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20708" target="_blank">📅 12:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20707">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏وای‌نت : دولت اسرائیل امروز اختصاص یک میلیارد شکل(حدود ۳۴۰ میلیون دلار) به وزارت دفاع برای خریدهای فوری تسلیحات را تصویب خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20707" target="_blank">📅 12:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20706">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سپاه : استراتژی ما حفظ تنگه هرمز است تا زمانی که دشمن تمام شرایط ما را بپذیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20706" target="_blank">📅 12:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20705">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به جنوب لبنان
رسانه‌های لبنانی از گلوله‌باران منطقه واقع بین دو شهرک «میفدون» و «زوطر شرقیه» در جنوب این کشور توسط توپخانه‌های اسرائیلی خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20705" target="_blank">📅 10:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20704">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e5786aba1.mp4?token=hryGDscea-1fNDi1xjqhPiNF7quadfccvRpfvm11EgBKBmmpjyfWL6XPH9HC_lrExI3OeVbXKTX6qh7K2v8pLhfQt2G7enkBb11WHzxN57rUg60dwKFwAmzZcVAyne178i_mHsYQrw6h34Xyaru7QiYadwuro1-BkmP4CiPOaNW0CiM0V9IQW_2Sb4zrC9FahYLGTzbiaOg3B7EAk7ls6h7MnVb2cS86O4iOo0ZRTOg61NXFketTtYM8TWiHLPls-shIr_gBXNiA1jusbFoxeBysI20I-K0aZKwOtxfhY6Qc-GTQc4gpNQ4zA6te4XEJtXN3c70U0Uf8I228t0f2IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e5786aba1.mp4?token=hryGDscea-1fNDi1xjqhPiNF7quadfccvRpfvm11EgBKBmmpjyfWL6XPH9HC_lrExI3OeVbXKTX6qh7K2v8pLhfQt2G7enkBb11WHzxN57rUg60dwKFwAmzZcVAyne178i_mHsYQrw6h34Xyaru7QiYadwuro1-BkmP4CiPOaNW0CiM0V9IQW_2Sb4zrC9FahYLGTzbiaOg3B7EAk7ls6h7MnVb2cS86O4iOo0ZRTOg61NXFketTtYM8TWiHLPls-shIr_gBXNiA1jusbFoxeBysI20I-K0aZKwOtxfhY6Qc-GTQc4gpNQ4zA6te4XEJtXN3c70U0Uf8I228t0f2IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی آتش‌سوزی یک واحد صنعتی در شهرک نصیرآباد، ۶ نفر مصدوم شدند که یک نفر جان باخت و ۴ نفر به بیمارستان منتقل شدند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20704" target="_blank">📅 10:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20703">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏حوثی‌ها اعلام کردند پالایشگاه آرامکو عربستان سعودی در جازان را هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20703" target="_blank">📅 10:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20702">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEje3WvWlIzOFimqJUFLHmGw6LMER8n-v-FY00Y-Xvei8JaAFMz1Z3GDKuVgL_JRa6iPqduyGP_PJ63_DznAq3kuYsmTyCRS7FaBaJWNmjanmnihUI6n1VYra9n7CIOYNZuMFU0XXiQBsoCwNJuxM_R5fdSpIe62e5Tkthfm1fuwB4pcsUFzxOjsj1lGv8IO1dV77MsRj4jpjXYvSyUqdsxkP8ymVhBOkfyZrR4ByQHod0-bQCZib_DvSiUgtpFOfw5F6TsLCmGZ57MQm9iYfU9kr6HdIF6Ey8R2jciMmCBlXnQg9utPEDqJkQmLAl8jbncS0TQF56VIGrf4Oqmndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورشلیم پست : ایرانیان آزاده و اسرائیلی‌ها باید در کنار هم بایستند و اطمینان حاصل کنند که سنگ بنای صلح فردا هرگز قربانی تیترهای جنجالی نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20702" target="_blank">📅 10:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20701">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانال ۱۳: ارتش اسرائیل به فرمانده سنتکام اطلاع داده است که اسرائیل برای جنگ علیه ایران نیازی به تأیید یا حمایت ایالات متحده ندارد و اعلام کرد ما در حال حاضر در حال آماده‌سازی برای شروع جنگ هستیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20701" target="_blank">📅 02:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20700">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">😁</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20699" target="_blank">📅 00:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20698">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYCm8WnBrGZoB-Yh9byi8vJwiNA_SMksv1nMS3Pbt2r7S92fkvuksdfqcNMNuUI-VG7RuffvROaygUrcrvqJbUEX-ZHSpOip5Cq2X1RTxb_ew6wXW1eXhLfhQIm_XEHgXhngHt6U06GwMYNEXYMSBXGKqsHrkTNYnBdyOTW1unduWkKad_jLlPuMnjE1fQOTWFSI77IHcpWav6lsSktsCGbpNRYcIpk86tEhTS1OrmmTanjzNblUC_IkWbjzS4W8XiHlhcA4uDPD9CvN02LvMrBmucU2HmqeTZtllzkSKlQmBvechVYSb-dTyVkwlXzA_Io3xdwiol0F281eVacp8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeKGUoayuChJHTthwyOc0Gx-I7ExIRElTKPutctjjdm3-cJE7D0im4ib5--nPakstJqJjCHJr6zR0WceYHKML-DH4QgtBMd4bEWWSjCXUlO2_u38hm2vZjiSCBCK7sxV6r-6s1gcn4mc3UuezFntXud4ziez5AvrApmABYWf1scbLRehTfONtT1dgyPG1VP7Rh-x62qTLm1KCljE9tAzkkmU-1NmjvZCQmp1VgbbGu0d6eK9pQa-77b0AmicorKcnctpkEBgMga3Hdq2j46K8aP9vXrgtu87-MYTCzNLpn_lvGCIl5Lz7AjxsFaThrCXTSjBaeOQ0CqHjjPOExpgTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست: تأسیسات هسته ای کوه «کلنگ
گزلا» در تیررس ترامپ قرار داره
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20697" target="_blank">📅 23:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20696">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5isWJLDWlZZbtX8In2LCD9u5oVfkZ8zDqtvgSVhOeixxz5wOsfwo62NG12qD6GwXibK4bXnC9aDeGM5Wf0Q6hkwlJjfSXOah4tJHco8AY-jXlBAvpTU-6_0CSUPIylkDlMoPYECjlvxk5k25EgJT7YRtyYIMo18wtUOqLGN3ec3_iqQlmKOyzo-RHUhyJz1MzAGyPXcEdEWuMB6vLN0BrMEk5SrtyrffODI5z2fAzMfsGID7zcEoMjAEcxlm2ibCkOAGNOkDDAXxti_mssGLPhJzVpsK5dc7DJPqnvfmA7BWhuwTJDrCcimuZlZA3cM5fhU2Ve3_p6dbGFxKe7Mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : ملوانان آمریکایی در حال تعمیر و نگهداری هواپیماهای F/A-18E Super Hornet در عرشه پرواز ناو هواپیمابر USS Abraham Lincoln (CVN 72) هستند تا اطمینان حاصل کنند که تجهیزات گروه ضربت ناو هواپیمابر برای اجرای محاصره ایالات متحده علیه ایران آماده ماموریت هستند. تا 8 آگوست، سنتکام 53 کشتی تجاری را تغییر مسیر داد، 2 کشتی را از کار انداخت و 2 کشتی دیگر را نیز توقیف کرد.
ارتش ایالات متحده همچنین به بیش از 30 کشتی اجازه عبور از محاصره برای کمک‌های بشردوستانه را داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20696" target="_blank">📅 23:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20695">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ3WWif1tS5s_-Q8JbdF5kJlCdg6SJA_m3bh__vzeN2x9xQKayTT0vmZ_WemfLIaiumytjOxmTXFEmseYXXEFWMJGbu2F9UWa0MxfcTJmWtAuANOu372f7S4ekl8yMv-hyZeXGH9hKsuYlnCi9zTLYnC_XD-UKQgfcPWEzpLuGyyvNymWh6coMCfih-ZkjU8h0Zb46t026jVKbo_-6WxeNheLQfArraJVMdpem0bR8ZcEt8gW3sIbMNq9xhdlS4PSFou1VyyDjmcPvapy-_UHHdORboRi1ITxYuc6987LpIEg3m5UwNwsFRDY-0MSrLZ8JYLnWOleeKZ-4dXROgJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده سنتکام وارد تل‌آویو شد  برد کوپر با رئیس ستاد مشترک ارتش اسرائیل و دیگر مقامات ارشد ارتش دیدار خواهد کرد. @WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20695" target="_blank">📅 22:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20694">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تمام مرخصی های نیروهای نظامی اسرائیل تا اطلاع ثانوی لغو شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20694" target="_blank">📅 22:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20693">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وای نت عبری : آمریکا سلاح‌هایی را از آسیا و اروپا به خاورمیانه منتقل کرد، زیرا موجودی سلاح‌ها به سطح "نگران‌کننده‌ای" رسیده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20693" target="_blank">📅 22:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20692">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیویورک تایمز به نقل از مقامات رسمی نوشت: ترامپ تصمیم گرفت با وجود هشدارهای ستاد مشترک ارتش در مورد مهمات، جنگ را آغاز کند و انتظار پایان سریع آن را داشته باشد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20692" target="_blank">📅 21:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20691">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فرمانده سنتکام وارد تل‌آویو شد
برد کوپر با رئیس ستاد مشترک ارتش اسرائیل و دیگر مقامات ارشد ارتش دیدار خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20691" target="_blank">📅 20:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20690">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال ۱۳ اسرائیل : اسرائیل در حال آماده‌سازی برای احتمال اقدام یک‌جانبه علیه ایران است
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20690" target="_blank">📅 20:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20689">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSHR0v8TZypFgQnaBJcPN6uOLiPFnB-6mNO8uOOK1OyqPMUWoaOdIxAcleQNThc2P_wYx8TAjBhl8XL7xeV-pqbUpGih-ELhuxnsseIlBaH8MR3HXtJGsxaW_bDMe34CWveha1QN8Kd8tewJ37lo3UqMxskh44nxF9BqolhVH1veL00KeX36SXJlmNaAieuuM_IMNZxPoBtbOPVHfnRcWzTYjY8iTN3EmzNFwCUJiEUcGNB81G4DG7XiIo0_K6uFWwmcdlGrb_FBjm1diAMuXI956D2y-6EsYCRH-pJjxBJ0MJvJWc4yUNBp3KK4fbIDrMZoQhSPYbnM1vX72bgoMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است امروز دو بمب‌افکن B-1B "Lancer" از پایگاه هوایی RAF Fairford (EGVA) پروازهای آموزشی انجام دهند و گرم کنن حسابی برا حمله اصلی . یکی از آنها در حال حاضر قابل مشاهده است: B-1B "FROWN30" 86-0124 B-1B "FROWN31" (در انتظار تایید) @WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20689" target="_blank">📅 20:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20688">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وال استریت ژورنال : ایران به دنبال منع عبور ناوهای جنگی آمریکا از تنگه هرمز حتی با توافق است
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20688" target="_blank">📅 20:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20687">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpKErafWaugIPL8dU4WxYt0l5KwjrS7RfC5y6yHn9EvIFNTrJqtyHsm8PIccRzZfhOBvHAUPdJJTCo7t8qlOihw0u7lVIG1JrMdHrMOAq3wro2GAMMO6Sb8DuSF8pduQw5_POC8ToaKFN7EkgQ-l9U2LYmNFqf-5QW-OmJAKovRLDmALKJpOHw0fHrp2YUNb-m5KhjQkTfsJ4TVoZuqKPbPR15W8CcsIZjm5iuGSx6XVilCJbbydhAFVCDwrEPc1lQEBtlN6L-fPydjFVZPhisoZwkjb0922FVPC9fUcP7nK_mzpN5KLDF-xLSt6w96RgaVQwdnpwhW2tj9CBQlctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت سوخترسان از اسرائیل بلندشدند
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20687" target="_blank">📅 20:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20686">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dc8a5363.mp4?token=djl3VmU9i2YiF4q9IV367sv8nR_dm3rqtOcjA5ojiR1vGtvQTNUGUqU17-HuSCwtaNB707YXK1gzkobh_hS39AGjnkPE9D2gLU9uOmj5SSOG1ne8uX4iL9xchWpnWH8uxt2fcj9YyQESwrEhcEnYPbxeALPoMZ50Ib5WiLGay2Vyvr4gw-hK7QXMEr5u7M6ntXB9nlpuKT4r1O_sqYmZkq-fpmn-kxjnHVPLJIzkIMSttPeUfcVFPDy5DUQlEvjywCXpLZ1AX_ARE8hP7K4kyLkeE5PXeP4gEKF1kUQKQbUSa992qaYO0CLjrS5srCQ5hH5jdLbAWCnhL6y85EB6bybY6Y2KtIKlGbXgEUkxCS6myqkqV10Q-4g4qEcFfy2z-OFDUtR8CdjePyzuN70bmnCWaCkaouZWNoqxMRU6S1VjQRyOUSf-x8l5Km1FJMPoXtim-TSPyHQju_qOmei8VQGLeiWULDTaMV7MheJFOKF2kYnpS06fJYy94FExfJVM-vglnOTyEc197qkmIVEr7eajH4djnndFazsVZ_P6oCZe_WYfLd7qx7lK9t5-DWNzjZ4xTgV8GX2GucFf5YZTr-0cBY7mJLNDjs7m5h3f5KhyvaiObyJFp3kqtuPhehD_xUU5hBFszRzurAFiWhQRGSnE1qRR476x0ta-tvrsmao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dc8a5363.mp4?token=djl3VmU9i2YiF4q9IV367sv8nR_dm3rqtOcjA5ojiR1vGtvQTNUGUqU17-HuSCwtaNB707YXK1gzkobh_hS39AGjnkPE9D2gLU9uOmj5SSOG1ne8uX4iL9xchWpnWH8uxt2fcj9YyQESwrEhcEnYPbxeALPoMZ50Ib5WiLGay2Vyvr4gw-hK7QXMEr5u7M6ntXB9nlpuKT4r1O_sqYmZkq-fpmn-kxjnHVPLJIzkIMSttPeUfcVFPDy5DUQlEvjywCXpLZ1AX_ARE8hP7K4kyLkeE5PXeP4gEKF1kUQKQbUSa992qaYO0CLjrS5srCQ5hH5jdLbAWCnhL6y85EB6bybY6Y2KtIKlGbXgEUkxCS6myqkqV10Q-4g4qEcFfy2z-OFDUtR8CdjePyzuN70bmnCWaCkaouZWNoqxMRU6S1VjQRyOUSf-x8l5Km1FJMPoXtim-TSPyHQju_qOmei8VQGLeiWULDTaMV7MheJFOKF2kYnpS06fJYy94FExfJVM-vglnOTyEc197qkmIVEr7eajH4djnndFazsVZ_P6oCZe_WYfLd7qx7lK9t5-DWNzjZ4xTgV8GX2GucFf5YZTr-0cBY7mJLNDjs7m5h3f5KhyvaiObyJFp3kqtuPhehD_xUU5hBFszRzurAFiWhQRGSnE1qRR476x0ta-tvrsmao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بورب مودین ، مأمور کا گ ب : همه دیپلماتها جاسوسند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20686" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20685">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یک کانال تلگرامی با دوتا فیلم از اون لحظه مدعی شده که نیروهاش "حمیدرضا رجب‌زاده"، بسیجی و مداحی که دو هفته‌ای هست گم شده بود رو به هلاکت رسوندن. علت کشتنش رو هم گفتن که این مداح جزو نیروهای سرکوبگر بوده و در ۱۸-۱۹ دی، تک تیراندازی می‌کرده. دقایقی پیش خبرگزاری‌های‌رژیم…</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20685" target="_blank">📅 19:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20684">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیویورک تایمز : ایران فهرستی از درخواست‌ها را ارائه کرد که امیدها را برای بازگشایی تنگه هرمز کمرنگ می‌کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20684" target="_blank">📅 18:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20683">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‎معاون ترامپ، جی دی ونس : ما توان نظامی ایران رو به‌طور چشمگیری ضعیف‌تر کردیم
بعضی‌ها داخل نظام ایران درباره موضوع "عوارض" صحبت می‌کنند
اما ایران به ما گفته که هیچ برنامه‌ای برای گذاشتن عوارض تو تنگه نداره و قصد چنین کاری رو نداره
انتظار ما اینه که صادرات نفت و گاز از خلیج فارس دوباره به همون میزان قبل از شروع درگیری‌ها برگرده
ایران در ابتدایجنگ، تعداد زیادی مین تو نقاط مختلف کار گذاشت
الان تلاش ما اینه که یک مسیر و برنامه تردد مشخص طراحی کنیم
تا کشتی‌هایی که از این مسیر عبور می‌کنن، بتونن با امنیت کامل رفت‌وآمد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20683" target="_blank">📅 18:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20682">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دبیر شورای امنیت ملی ایران می‌گوید که ایالات متحده باید دارایی‌های مسدود شده ایران را بدون قید و شرط آزاد کند، تحریم‌ها را لغو کند و غرامت دو جنگ اخیری را که علیه ما به راه انداخته است، بپردازد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20682" target="_blank">📅 17:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-qNtLMb6kYROyS7JifFoRnKxf5tJMN5nr4FHN6vqE-XL0HPecPJiUv_nBsY5W19Sxw751iPgatis7VjctgFnXynxsaAHTk-9Lt8moHYgvmyRqKBwJNXj2tr_263V2BazGoL5Gius5iuq0HCwBI8UUli1gzTZaUMUaQdc4En3KibScXKdksZPJ_MPgvwvW9IlSZazEvfS1oz5ZWUHnkbD5ew-ixunLVHWBzm1EbjFM_njbNyKfsEvNGaxLGkwDUdFdk-glQ1wzYvy3byZywxflFnLO1Q_jgd73JtX_9BegR6nFLe82TD-7T2OPj_VmtSuLfbYYJVra8C67xOCgLuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است امروز دو بمب‌افکن B-1B "Lancer" از پایگاه هوایی RAF Fairford (EGVA) پروازهای آموزشی انجام دهند و گرم کنن حسابی برا حمله اصلی . یکی از آنها در حال حاضر قابل مشاهده است:
B-1B "FROWN30" 86-0124
B-1B "FROWN31" (در انتظار تایید)
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20681" target="_blank">📅 17:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwym-z-RVpN10oOIMemMV442z8VvA94sJqRB9OIohx9e3PTXWG67NwkqxSY6_SUJMaEnc54ORxFmzhu4A14Om2ZS_qqv-Ef0E1zmDAqmVFO2rTnM5HsKtXodhEQNehbaNFBBVapxhMzIoMeMDkidDHnNcOPvX2mbOQijHuxPQVUyUPIqfGV-FbzA_dQu5SipRsMDRUyIgoyDXJ179r1v3yFRTEmnAu5LdmXOw1R6vcTshTbjwvcgPGLmA31krI-BWhiwIO5XiVAcObc3ZZG2gH2I7W8CYtBmntE87KAqdx-De_txHKfUPlg1_6gv4x-o_6o11qE9IuRcKYvf7pZX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از حادثه‌ای در ۱۸ مایل دریایی شرق خصب، عمان دریافت کرده است.یک منبع موثق گزارش داده است که یک کشتی مورد اصابت یک پرتابه ناشناخته قرار گرفته که باعث آتش‌سوزی شده و آتش خاموش شده است. هیچ گونه آسیب زیست‌محیطی گزارش نشده است. کشتی و خدمه در سلامت گزارش شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20680" target="_blank">📅 16:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb62efb6b.mp4?token=v9AoAIX2oHZZZ0djib9pyFIpHllU8J3bTZlpEXNmoCjb_EnA8wD4INIsPYBI5CPg_2_HNhuYjQWv9vvyn00jzmhYDnkOooul_xjkmSyJ7ztfXpRl-3cGDLMZ4Fgnl7yTSQyIatBvbe6FZD2ktjHrag1IpV1GIqXDjsfb6-d7Wsq7dGedaAyxa9zlU1fOWVyhc4EplMxXHWTzJrZy_i4wJHIXs8i1XkVNreKCvlUNCMXWJEGbpKt-R9aKZ0IEntQ9ObhSjCUP-avkrqe3mp67CMHiYcaq2ngZwU9NeLYatP7h4T1bLEh3RgSv-5-MsNI63fwg9iDpTebqWALhzJLdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb62efb6b.mp4?token=v9AoAIX2oHZZZ0djib9pyFIpHllU8J3bTZlpEXNmoCjb_EnA8wD4INIsPYBI5CPg_2_HNhuYjQWv9vvyn00jzmhYDnkOooul_xjkmSyJ7ztfXpRl-3cGDLMZ4Fgnl7yTSQyIatBvbe6FZD2ktjHrag1IpV1GIqXDjsfb6-d7Wsq7dGedaAyxa9zlU1fOWVyhc4EplMxXHWTzJrZy_i4wJHIXs8i1XkVNreKCvlUNCMXWJEGbpKt-R9aKZ0IEntQ9ObhSjCUP-avkrqe3mp67CMHiYcaq2ngZwU9NeLYatP7h4T1bLEh3RgSv-5-MsNI63fwg9iDpTebqWALhzJLdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌های توپخانه‌ای سنگین ارتش اسرائیل به شهرک المنصوری در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20679" target="_blank">📅 16:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‎فایننشال تایمز: محاصره دریایی آمریکا بر ایران، صادرات نفت از ایران را متوقف کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20678" target="_blank">📅 15:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20677">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f01922dde.mp4?token=DjUlXZRD8W8vQtrkk-ATOnVne04iwVQRXSmnF6s25eQOF7tJ-fXaGWeQy_iqrLNXk3vLfeCD51ipPE9nsjDrEGkfJ4Qd7x8PqkCt1JEKL4UvBhnboNH_wqnhjAr02_lNfQRclbXJACYowzcARFeveT0t4HTccf9DnOYlSoVvB5WuIzUkJwgHvCYPbGeTOy_qnduTWpFJXFVRbk7xpj4fKFUw8E9ZrkcfiBXQ31cio6jBxCwpZt0M20iaPnDAguSaMWM6swN1n8NqTwVHhtAEoTP85Ei0bPir0GcdkBfMeQttLdxUbI02Vl-KaFJFDb-tIFGfy7FvZmpLPqUlm7nMYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f01922dde.mp4?token=DjUlXZRD8W8vQtrkk-ATOnVne04iwVQRXSmnF6s25eQOF7tJ-fXaGWeQy_iqrLNXk3vLfeCD51ipPE9nsjDrEGkfJ4Qd7x8PqkCt1JEKL4UvBhnboNH_wqnhjAr02_lNfQRclbXJACYowzcARFeveT0t4HTccf9DnOYlSoVvB5WuIzUkJwgHvCYPbGeTOy_qnduTWpFJXFVRbk7xpj4fKFUw8E9ZrkcfiBXQ31cio6jBxCwpZt0M20iaPnDAguSaMWM6swN1n8NqTwVHhtAEoTP85Ei0bPir0GcdkBfMeQttLdxUbI02Vl-KaFJFDb-tIFGfy7FvZmpLPqUlm7nMYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسنیم با انتشار این کلیپ که قدیمی‌هست نوشت: پخش تصاویری از رهبر برای اولین بار
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20677" target="_blank">📅 15:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20676">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : فیلمی که کمر خیبر شکن را شکست…  https://www.instagram.com/reel/DbwJLvzRBwp/?igsh=YzEwMDhhc3d3em9u  بررسی اینکه چگونه یک فیلمی که همه به آن خندیدند، پرده از اسرار مهمی از تکنولوژی مورد استفاده در موشکهای جمهوری اسلامی برداشت.</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20676" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20675">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آغاز ساخت پناهگاه در پایتخت
معاون شهردار تهران:چندین مرکز را در سطح شهر تهران برای ساخت پناهگاه پیش برده‌ایم و کار اجرایی آنها آغاز شده است.امیدواریم در نیمه دوم امسال بتوانیم چند پناهگاه را به بهره‌برداری برسانیم.اقدامات احداث «پناهگاه و پارکینگ ـ پناهگاه» به تصویب رسیده و اقدامات اجرایی آن آغاز شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20675" target="_blank">📅 13:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20674">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وکیل ترامپ در پرونده حق‌السکوت، وزیر دادگستری آمریکا شد
سنای آمریکا پس از چهار ماه و چهار روز از برکناری وزیر دادگستری، با ۵۰ رأی موافق و ۴۹ رأی مخالف تاد بلانش را به عنوان وزیر دادگستری و دادستان کل تأیید کرد.
بلانش پیش‌تر وکیل ترامپ و از اعضای تیم حقوقی او در پرونده پرداخت حق‌السکوت به «استورمی دنیلز» بود.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20674" target="_blank">📅 13:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال ۱۲ اسرائیل: پزشکیان برای وادار کردن خامنه‌ای به ملاقات فوری با او تهدید به استعفا کرد.
"وضعیت اقتصادی ایران غیرقابل تحمل است"
پزشکیان می‌خواهد برای خامنه‌ای روشن کند که پریشانی اقتصادی کشور به نقطه بحرانی رسیده است، تا جایی که دستیابی به یک توافق سیاسی و رفع فشار اقتصادی به یک نیاز فوری تبدیل شده است که نمی‌توان آن را به تعویق انداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20673" target="_blank">📅 12:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20672">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1KFUWqULUQELsD1-V1oczkZ5onwMnX8A1j7G8b1mrutvUyZVAtUXg_bFGKLZLEthkUlMXY-NYwV70Ni567u46EPS3nCp17VlriN8A-fgAWDGW739PQZnVba8BoXQOhHIxKm3N3eOglzPyOATin0Q728Xlwd2VcaNT_Crh4ad09XadnVwSIjkNr-PcTJYCi4FlJB4cFei_WLj43vq5iQZq8xC3pq4xxk_4xSSTn7-EulGv2-CEg0Ip8SCQ06hJ7ZqsSZR_RsmdH9Z-m6ekNMjpRSd6VqY84SpthfiLsaT4u0fx9xhRM4THPlTojD3b-FzK_i_ZwFyGMEsX3Y5osAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کانال تلگرامی با دوتا فیلم از اون لحظه مدعی شده که نیروهاش "حمیدرضا رجب‌زاده"، بسیجی و مداحی که دو هفته‌ای هست گم شده بود رو به هلاکت رسوندن.
علت کشتنش رو هم گفتن که این مداح جزو نیروهای سرکوبگر بوده و در ۱۸-۱۹ دی، تک تیراندازی می‌کرده.
دقایقی پیش خبرگزاری‌های‌رژیم خبر کشته شدن این فرد رو تایید کردند
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20672" target="_blank">📅 12:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20671">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20671" target="_blank">📅 11:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20670">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90587b68aa.mp4?token=QENoeQyJf51UjD1pH2uAw6Svn5n7-pO_gy9UnIkgl2DQWRudWPVzPKdPUq6hlPet2Ee9yJGA4x8Axy9l1T50p16XU6aZxs-0NA5J-6yxUOmc0bZC1DjsMIA-eq63yso43IE13k2sW9hzm3EZ9UMHfKUcusX87cZrF3oSYOVQShJo-Glw5pHOWcsuowYSGHvFrNKLSv3Tk5eCqiKzwzDnyg68Ineds7l0qIZWHmGd3GyFnMBXM24IdEau-8irTnPkfAWJZqcqDLRQkd_36TzNJyYbU0XDCTI3WNx9LMTRK__eMJQjcaGNEcUnZMfbbsS6cwI98kUc2nS5HoUxnk38yb6WW0-CqQlPbQLTLrQYVNxCGxoLzyiosXyyN7-2dOwpY2Y9kbAv5UhHmLk_a9xx8D5IafbNVchtZmoSW33xNwKXiIRJVk2a_rNMd3ny0QeM4VqZ8lrngcBF6IXYdZGEb9DfZS-WKarK44eQistyzLWQfcz6VbdZaZeLQOVym_XV5EuhSN3hJ97_MqHMnkFAx97FHKmSz3AnYHJIkpuHDF8viPNi9z_DaVdNtidTQlMmWRVzXA29LXImJXfiW7bFhz3N6t8oZ6L-UllsUjXRb3vjLqaqh1EMQqPlxt83Ly4HgpndEiS05fkFMfnJS3qsJ5p1OfcDciXpc9d0FKgwvVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90587b68aa.mp4?token=QENoeQyJf51UjD1pH2uAw6Svn5n7-pO_gy9UnIkgl2DQWRudWPVzPKdPUq6hlPet2Ee9yJGA4x8Axy9l1T50p16XU6aZxs-0NA5J-6yxUOmc0bZC1DjsMIA-eq63yso43IE13k2sW9hzm3EZ9UMHfKUcusX87cZrF3oSYOVQShJo-Glw5pHOWcsuowYSGHvFrNKLSv3Tk5eCqiKzwzDnyg68Ineds7l0qIZWHmGd3GyFnMBXM24IdEau-8irTnPkfAWJZqcqDLRQkd_36TzNJyYbU0XDCTI3WNx9LMTRK__eMJQjcaGNEcUnZMfbbsS6cwI98kUc2nS5HoUxnk38yb6WW0-CqQlPbQLTLrQYVNxCGxoLzyiosXyyN7-2dOwpY2Y9kbAv5UhHmLk_a9xx8D5IafbNVchtZmoSW33xNwKXiIRJVk2a_rNMd3ny0QeM4VqZ8lrngcBF6IXYdZGEb9DfZS-WKarK44eQistyzLWQfcz6VbdZaZeLQOVym_XV5EuhSN3hJ97_MqHMnkFAx97FHKmSz3AnYHJIkpuHDF8viPNi9z_DaVdNtidTQlMmWRVzXA29LXImJXfiW7bFhz3N6t8oZ6L-UllsUjXRb3vjLqaqh1EMQqPlxt83Ly4HgpndEiS05fkFMfnJS3qsJ5p1OfcDciXpc9d0FKgwvVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش ویژه آژیر خطر از فاکس نیوز: سربازان آمریکایی در جنگلهای بنگلادش تمرین آمادگی می کنند, حکومت ایران یا توافق را میپذیرد یا بمباران میشود. آیت الله گی قدرت پدرش را ندارد و اختلافات بالا گرفته… و عناوین دیگر که در این ویدیو خواهید دید
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20670" target="_blank">📅 10:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20669">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5VNBqhlS9Bo1d8aLpy9A3XHiFvbtaEn_Rscd7HD4NxDKv64KxIbJpYKMwkVdCIUWG9JA_I8KYGgzaY5wj1271WoXvVGsqpyDpUxQNeVzF9h4WYYzHj2U5LPiaeZJioUakrxm4-ml2JRsLK0yplyS--ZH5ByuoC6fF0eRmfThyWSIA4iirwFvVeLveITcb6BO2zl1gKJ7jrxnD67KwqzvFAf2HsxsTCDPddkMVsZqqT0t8NwHEOqs922-NUD5CVLzaKii8008O5gCAoct5K2E3h5eSgd-Hnu_nHfcEmW7DVpV8OODjSVFWkoYD8S2zYXcHk7lAR6XVSYAH78daUvdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن روحانی توی خونه خودش یک هیئت دولت خونگی ساخته با هم جلسه تشکیل میدن و خاله بازی میکنند!
@WarRoom</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/withyashar/20669" target="_blank">📅 09:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20668">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سفر مکه
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20668" target="_blank">📅 02:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20667">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqCfdVRmN4sgAXfmH1ceZL_mqaH5MCnnlrn1LdW_mMSdMwNxQjhvSj4f7pL_nbyd4YXBf30CSpLGBnba7Pn15S9J3G2X6YG94CtoVizAHOpevHJlag2SUhu0-0o3YPpj88Uerhpi5pD9gZRxACegKYjA7EFjIRX--g9Ln-IUJ4dcLf1f6ej04_AxVGCSqF0oOqH1OwVcTvjL8Ymi82apvIE0vrK4C2tmeuUYX9Ec8OtckH1Rr6kaOK8vBXxr8B1VtE33GoJJqwAw3bl1ZIgfzp36M05axEULlgoW1Lgbd05fKnTN_hbPWDc0OGKYgbbEx8i_6pybzeTZ5tBXEbXybA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین به ترامپ : کلکشون رو بکن
@WarRoom</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/withyashar/20667" target="_blank">📅 01:12 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
