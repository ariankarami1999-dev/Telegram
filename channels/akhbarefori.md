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
<img src="https://cdn4.telesco.pe/file/ei9NaVnKPmeXN0n2nZKXXwmOnxMxfDo3DM976HcReRA3IYQBaccEQi_YsqcSwO_Guec-UEkb8Ydp6bFbpKfHD-qz7olP0bMai7aXGiGMX2dwSeLm4Xhf384OXB4cjRo6Mbsm5fYMdakqIPJo84fLctKrhftAaO7Exp21nZSdohzQ1Mt9mwMytmfmetrx7_-kBoaywBlg0pqIxM2t1r8Lt2Qkv1wjHkNsJW9s6tIRBY6BeiLSbJP3VU9nzbO05Ump7MHs0kSQnY_XNGI5MQZKtD8dYFeVfGZm7qnAphmISZxl6m29IdvYgqRxurLcRs7UTvV1LdkyrV05HdTovpYJCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.91M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 10:11:36</div>
<hr>

<div class="tg-post" id="msg-652234">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c315d2d0bd.mp4?token=UUr0TDmH0F2lLyABqf_GU-naLJXqIKEFfXPk7Xt9i9wujgWoB8HLN-gf-gSGWDfl_wnqB8dXFZ5N-xzn_OBrBHuXyfHFtDbwWZJe1CVrcvHWEmX6G1rbJIliOb-ChZahUw8fRb--b4_q6KRrHeMn2Q9M3MVr-vYm4O4_lWEiIf-DDDKWoUIo48Qc-XnL6wEwp4yRSykKNE5llOtrShlnnb-BcLaddRk1-zbNddvkaP-ImMyCqD9vQA8oHcxcV0Y8DvDNmIOxrwK6NEkQeC74jr5gY5H0SwKaQJIk6JBcvVpWRsZ1rC-KGuaIE01J994ZlZHQPl2KiWHP5c_LE7wh7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c315d2d0bd.mp4?token=UUr0TDmH0F2lLyABqf_GU-naLJXqIKEFfXPk7Xt9i9wujgWoB8HLN-gf-gSGWDfl_wnqB8dXFZ5N-xzn_OBrBHuXyfHFtDbwWZJe1CVrcvHWEmX6G1rbJIliOb-ChZahUw8fRb--b4_q6KRrHeMn2Q9M3MVr-vYm4O4_lWEiIf-DDDKWoUIo48Qc-XnL6wEwp4yRSykKNE5llOtrShlnnb-BcLaddRk1-zbNddvkaP-ImMyCqD9vQA8oHcxcV0Y8DvDNmIOxrwK6NEkQeC74jr5gY5H0SwKaQJIk6JBcvVpWRsZ1rC-KGuaIE01J994ZlZHQPl2KiWHP5c_LE7wh7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هلال احمر از بیرون آوردن یک کودک از زیر آوار در حملات دشمن آمریکایی-صهیونیستی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/652234" target="_blank">📅 10:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652233">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce97e1e5e.mp4?token=GPEgMC5p-Q92KHru7c6RmukcsLSvann72bTYRCwz1HfHRfZT-Uwi7LfZ98Nh1LR_rg4ZCp4QnA-6Wxj_kGKcbf_cgiPvAedFcYnpzKqtABd8j0CZ7xExq_u3ai5yupWuhE8lg5IhbU2ZpcZ9IK1TQdRFFSDkEbuFJyAB0o3alY-7-nzcECmqV8uhxvi1-xzkjhZvqe1ebwmgkFhHwSN3vb2MJgJ6SxfadHKxNMkS571Tkr81RDSkZQE7omWniKZR1DbU-XERambB3jwo6abJXM6shehiM8H75n6Vs5jkmtoFGzjOrAKkKgox-khLrX5aFd5CJcZYWqZHNz3kBrC1aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce97e1e5e.mp4?token=GPEgMC5p-Q92KHru7c6RmukcsLSvann72bTYRCwz1HfHRfZT-Uwi7LfZ98Nh1LR_rg4ZCp4QnA-6Wxj_kGKcbf_cgiPvAedFcYnpzKqtABd8j0CZ7xExq_u3ai5yupWuhE8lg5IhbU2ZpcZ9IK1TQdRFFSDkEbuFJyAB0o3alY-7-nzcECmqV8uhxvi1-xzkjhZvqe1ebwmgkFhHwSN3vb2MJgJ6SxfadHKxNMkS571Tkr81RDSkZQE7omWniKZR1DbU-XERambB3jwo6abJXM6shehiM8H75n6Vs5jkmtoFGzjOrAKkKgox-khLrX5aFd5CJcZYWqZHNz3kBrC1aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دشمن ادعا داشت به مراکز نظامی حمله می کند اما کارخانه رب گوجه فرنگی را هدف قرار داد
🔹
رییس سازمان هلال احمر: حدود ۱۴۹ هزار واحد غیرنظامی آسیب دیده یا تخریب شده‌اند.
🔹
از این تعداد، ۱۲۳ هزار واحد مسکونی وجود دارد که حدود ۱۰ درصد آن‌ها به طور کامل تخریب شده‌اند.
🔹
۳۵۰ مرکز درمانی شامل بیمارستان‌ها و مراکز بهداشت در حمله آمریکایی صهیونیستی تخریب شده‌اند.
🔹
۹۹۳ مرکز آموزشی، از جمله مدارس، مورد حمله قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 597 · <a href="https://t.me/akhbarefori/652233" target="_blank">📅 10:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652232">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1B2K5g03ZNYs960_teCTOZj4nNj9YXHcyBIGmjyr0OXaB9YpTVISDl_K9pWGuxt5mGC5826pWpbPUlGfwxhavATjV7brpM_FsYn42a9iZ7JrckoIDLyRDkcGJUa8v8D2M-_8Ck9pz_KJ3uTFQDxnEtGvSkYoAwOze9vP-BIi7IHBRE41IcCxs8NXe7Rd3aQEr8MyKoI7DKSDOusHeY2WUJqZbceX9FzEz0NWZH6GDqXE5oCttguJO-lOOeIvQZySN6UxMPtPSgRV5vKpU1q6gYGlhvTWsCQfYTIGhPZyvpd1uL07CwDyK_icTFH66w2bG69TPViMD8QbvUXSo9WJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استفاده آمریکا از جزیره بوبیان کویت علیه ایران در جنگ تحمیلی سوم
🔹
ارتش آمریکا با استفاده از تاسیسات گارد ساحلی و تاسیسات نظارتی و لجستیکی کویت در جزیره بوبیان اقدام به استقرار سامانه‌های متحرک پرتاب موشک‌های هیمارس در جزیره بوبیان و تعرض به خاک جمهوری اسلامی ایران کرده بود.
🔹
این عملیات تجاوزکارانه از خاک کویت در روز ۴ فروردین سال جاری انجام شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/akhbarefori/652232" target="_blank">📅 10:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652231">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
اموال ۴۷ نفر از خائنین به وطن با حکم مقام قضایی در استان همدان توقیف شد
🔹
با دستور مقام قضایی اموال ۴۷ نفر از خائنین به وطن و کسانی که علیه امنیت و ثبات کشور اقدام کرده‌اند، در راستای حفظ حقوق عامه به نفع مردم در استان همدان توقیف و ضبط شد. رسیدگی به پرونده این افراد در جریان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/akhbarefori/652231" target="_blank">📅 09:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652230">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UurBURZTt-Ct03bgppN6GXX2Hx1ATCJPIVI6l3Qs6XE5QIhnXPUhtT76OKVopbWnkdCI9moF3gtjqamN4nVzJX87PunMoh4WNz0ib0wUD7TMFAcAMz9hvvR0daXyuF5Lq52rPevsvsgInOChL6qhVA3dqxMOPwim997QtPazgI_eOh_J5_8cELz1qFuZrfVBMgYi1g18XHV8_DXK6bNR6wtF5sq1dFk5b9wXV-94AwDcdaqBJl_E7LhBnkKVNp65iGzWcllDN9B8oj5M3w4MtW4f0aBziKMre3sj-Kc0fyqserq-bV2KPSlCFabsm9qF-GeIqSuwusrNvCEKFCgbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روند مورد علاقه ترامپ: وقفه‌ای کوتاه پیش از دور بعدی خشونت | پیروزی سریع تبلیغاتی و عکس یادگاری سیاسی | آتش‌بس هنری است که ترامپ ندارد
🔹
سودارسان راغاون، تحلیلگر باسابقه و خبرنگار ارشد سابق وال‌استریت ژورنال در تحلیل تازه خود در نیویورکر استدلال می‌کند که سیاست دونالد ترامپ در قبال ایران و بسیاری از بحران‌های جهانی، بر ایجاد «آتش‌بس‌های موقت و شکننده» استوار است، نه حل واقعی منازعات.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3214576</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/akhbarefori/652230" target="_blank">📅 09:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652229">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lK_i6x76ACeR9RfsCo67OhM0eN4_vyAc3uOzEvOqZV9a0Fl6aOMj-_BV-eaG3gGQv314ZoYk5h_qtWEYdbYwPd1-DIhCfE1JNWsgemJwqXVQqNeiK7qPrCn_jIOC2VSrG3K33OKS5RVfTNdYMR9wSKH452PYW9i8ni__-tDF2y72ED7efQV91nfJi4ZTq441p0wjcCMNWwBe36BocxJmNTQiLRi9SsBQCN44QzHmEq_DSdDQltpsitqv8hAQjatnzGq6Vjtw1hfsqA9lZMrt-Im0IWDu0dA-QT7NBQGi6CB7T6r3WEIlLf-CpHLcuhjHEPeVpuzg--RHO-wc2Z-YzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی در دهلی‌نو: هرگز در برابر هیچ فشار یا تهدیدی سرخم نمی‌کنیم
🔹
وزیر امور خارجه امروز در نشست بریکس در دهلی‌نو گفت: هیچ‌گونه راه‌حل نظامی برای هر موضوعی که به ایران مربوط باشد وجود ندارد. ما ایرانیان هرگز در برابر هیچ فشار یا تهدیدی سر خم نمی‌کنیم، اما به زبان احترام پاسخ متقابل می‌دهیم. هرچند نیروهای مسلح قدرتمند ما آماده‌اند پاسخی کوبنده و ویرانگر به متجاوزان خارجی بدهند، اما مردم ما صلح‌طلب هستند و خواهان جنگ نیستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/652229" target="_blank">📅 09:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652228">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJgZTziQF8gOIOU0UdUOzA6AIVMFAJ2f2hZI3rvP1naAn-oAMbxm8xEVM58kPt1SxNPeN_Trc_tZnuaYkDhmLoedOay9ZoA47DrASEUk7zTPxj2onJzdQ0LUOFd1WsuxQW336PNPCRj1OG1zrIl_Ldfp9wf91iUBXUL_lSby7RSayVRCok_Z5nirDjGrQY_BUqqQiVYKa7nxM4XqcIqloqUQmNzzjeLB1lTrSeIftPY2BWYEjsaoHIMJIE6dimEeY3NowL2FYK8Z6_AGeicCV04Vlka-bBNEP-qAFrZr107cC5BRcxrZI0MJe-ECiXqnwtfaRXcVLEZr0yL0wX5XFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شی جین پینگ: مساله تایوان مهمترین موضوع در روابط پکن-واشنگتن است
🔹
رئیس جمهوری چین، موضوع تایوان را مهمترین موضوع در روابط پکن-واشنگتن اعلام کرد و درباره حمایت آمریکا از جدایی‌طلبان جزیره تایوان هشدار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/652228" target="_blank">📅 09:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652227">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52781fd6a0.mp4?token=fAtWUbITRu0dubOHFu2EsrbGZwmT81Qbtjj-theTlzSkznzTugxU42GMUJDpXnJvU0A_FYhss5zt_oHBwWHimRZmE80Xsu8SubeMxGvTRVPkSIzDjS3qWWsyOFZc4ojiFGmrH5rnPqN4DVTUSEjNPMhljuPFDmCErcLfS_clfdRcdj4JTZBt50EI990o261I4nG_O3n13OgcL2N3BfEjxg0p0XHin1_N6035-6wSOVmSbYiEm-n4rLhy6iFHauTABRPowsEDpyilrjhJeeFEb_ztb1jAqnjyEVfR099KYBkkT8zawgGYmDwpaVkyJ3uxqdVwGm68vceJaoHYB5Ky4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52781fd6a0.mp4?token=fAtWUbITRu0dubOHFu2EsrbGZwmT81Qbtjj-theTlzSkznzTugxU42GMUJDpXnJvU0A_FYhss5zt_oHBwWHimRZmE80Xsu8SubeMxGvTRVPkSIzDjS3qWWsyOFZc4ojiFGmrH5rnPqN4DVTUSEjNPMhljuPFDmCErcLfS_clfdRcdj4JTZBt50EI990o261I4nG_O3n13OgcL2N3BfEjxg0p0XHin1_N6035-6wSOVmSbYiEm-n4rLhy6iFHauTABRPowsEDpyilrjhJeeFEb_ztb1jAqnjyEVfR099KYBkkT8zawgGYmDwpaVkyJ3uxqdVwGm68vceJaoHYB5Ky4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله نوری‌همدانی با صدور فتوایی، پرداخت وجوهات شرعی مقلدان «رهبر شهید» به رهبر معظم انقلاب را مجاز اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/akhbarefori/652227" target="_blank">📅 08:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652226">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین- داریوش بزرگ -قسمت هجدهم</div>
  <div class="tg-doc-extra">داریوش بزرگ</div>
</div>
<a href="https://t.me/akhbarefori/652226" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
▶️
«داریوش بزرگ؛ معمار امپراتوری ایران»
🗓
این قسمت روایتی‌ست از پادشاهی که پس از طوفان شورش‌ها، ایران را یکپارچه کرد؛ از مردی که با نظم اداری، قانون‌گذاری و ساخت پارسه (تخت جمشید)، پایه‌های یکی از بزرگ‌ترین امپراتوری‌های جهان را استوار ساخت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/652226" target="_blank">📅 07:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652225">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac1de98ac.mp4?token=E61yxjsbp1iRuB46HYW4D6RJJ7JkI4gkOZ1U_DIt60S1Qd9ef46BNEw_eIxfun0lxf4rh6ee_vgZs811bQ8Iw5dtRNG-nCRx59F0HQT89Zvt_JFgkhXGzgdl2_ZWBwVwXClnB5rHDcpaagFe1EijFlgP7avOOQ_sedLqKegM4ARXHpJ5rP1sV357h1JidVjaijO2RDmJS00ygpGh_Cs5yQqpuL4CoUYnoE35sm61A04iZQGmVMmzG-o-UB4mXFevP8Yu5ON1aLBdJfTIJ-aCaBy33_mbFjALNFtNg32bYDisZyRspgz1EgRcELTBPb73G6cKHAINsLnvduMTkJCZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac1de98ac.mp4?token=E61yxjsbp1iRuB46HYW4D6RJJ7JkI4gkOZ1U_DIt60S1Qd9ef46BNEw_eIxfun0lxf4rh6ee_vgZs811bQ8Iw5dtRNG-nCRx59F0HQT89Zvt_JFgkhXGzgdl2_ZWBwVwXClnB5rHDcpaagFe1EijFlgP7avOOQ_sedLqKegM4ARXHpJ5rP1sV357h1JidVjaijO2RDmJS00ygpGh_Cs5yQqpuL4CoUYnoE35sm61A04iZQGmVMmzG-o-UB4mXFevP8Yu5ON1aLBdJfTIJ-aCaBy33_mbFjALNFtNg32bYDisZyRspgz1EgRcELTBPb73G6cKHAINsLnvduMTkJCZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریوش بزرگ، پادشاهی که امپراتوری را از نو ساخت…
​قسمت هجدهم پادکست کافئین منتشر شد
☕️
⚪️
با قانون، جاده شاهی و نظمی کم‌سابقه، ایران به قدرت اول جهان باستان بدل شد…
​
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتون باشید!
​از اینجا ببینید و بشنوید
👇
https://youtu.be/Qfgg8RqcuBg?si=5uXMp7EKJBtDtAjp
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/652225" target="_blank">📅 07:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652224">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6URnY8s8A-JhAF5EAmCGVq7PGTNNBWfXwvM7aWTxsQ7Qd5pYTGCL7ur5CL2FQg3Qx6FPmr0Bbx-AfL74HsAivRjTO7wp6n8Rfw9NbgNBiA1g8O-U-rco-mDxr3Z5hqwsXrZ1z1LF56_CE7-hgFlM_xQC1_XdvbT42tm0SC1hnyTbHvlyFnaGlEr04OzfE5pGMJTpLrd-YIKdRNFohqnqy3ZwRlRrFDrKXCbHN4hMwaCEjA_h0Z1TOeoSsQzsvGcvJbzFL-eoEwOik7BJPifee1UiN2U9eO4DPkrmwXhhqg0LP6hURLd65-axfLJu9UPPmDPzx6MbIDD-JxZoZUCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز ثبت‌نام وام ۷۵ میلیون تومانی بازنشستگان کشوری از امروز
🔹
معاون توسعه مدیریت و منابع صندوق بازنشستگی کشوری: فرآیند ثبت‌نام وام سال ۱۴۰۵ از امروز پنجشنبه ۲۴ اردیبهشت ماه آغاز شده و تا ۲۰ خردادماه ادامه خواهد داشت.
🔹
مبلغ این وام از ۵۰ میلیون تومان در سال گذشته به ۷۵ میلیون تومان افزایش یافته است.
🔹
وام ۷۵ میلیون تومانی در ۱۰ نوبت به متقاضیان واجد شرایط پرداخت خواهد شد.
🔹
مطابق با ضوابط و شرایط اعلامی از سوی بانک عامل، مبلغ کارمزد و نرخ سود تسهیلات برابر با ۴ درصد است‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/akhbarefori/652224" target="_blank">📅 07:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652223">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw22DznoiHs4dtHVNVOe_6gUn2XTL149FLLv1mGhZU0XxvZOaycFbKPfqJMx4W5nwagg3uYLR_zcXGPP1JXwNRdcgupQAB7nTSTQWGfBWYEsdUdV_nndagkuVS9fDOOM73W79vimTiYwqsvfjy0jT5-2U5ApbksNJOtMCrLawbJuecYptjESvK2Soiaj4dmx9a5zAP7ikf901nn5Hm7jcm23anuC4raC-_9Ov2yrR7adblrPPpk_YbrWTXpvDo9buZrZKG3VvDfv8c4_246AJZLQ80tznle5-d1mBa34f_lJfKQCJAcLCnFSbfPkueOCPEcU5_p6zc3KXQnimb6UAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۴ اردیبهشت ماه
۲۶ ذی‌القعدة ۱۴۴۷
۱۴ می ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/akhbarefori/652223" target="_blank">📅 07:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652222">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
اسپوتنیک: حملات ایران به پایگاه های نظامی آمریکا، ضعف نظم منطقه‌ای واشنگتن را آشکار کرد
🔹
حملات ایران به پایگاه‌های نظامی آمریکا در سراسر خاورمیانه به گونه ای بود که بازسازی آنها ممکن است امکان پذیر نباشد و «ضعف اصلی نظم منطقه‌ای واشنگتن» را آشکار کرد.
🔹
جنگ ایران مجموعه‌ای از چالش‌ها را برای آمریکا آشکار کرد به این معنی که ایران از دکترین نظامی مدرن با تعداد زیادی موشک و پهپاد استفاده کرد، پایگاه‌های پراکنده و زیرزمینی ایران حملات آمریکا را بی‌اثر کرد، قلمرو و جمعیت وسیع ایران مشکلات استراتژیک دیگری را به همراه داشت، برتری هوایی آمریکا خنثی شد و نتیجه جنگ به تساوی رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/akhbarefori/652222" target="_blank">📅 06:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مشاور ویژه در دولت ژاپن: ایران فراتر از حد انتظار در انسداد تنگه هرمز موفق عمل کرده و تن به هیچ عقب‌نشینی نخواهد داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/652221" target="_blank">📅 05:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652217">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEMUYOnF8ShKK6naScBkeQ8hBV1vjn3wrF-tUmjU98rnTut6eduOV846qVqAL7NXkpQQ1XndTsBj839V5SgBaKrpVaKEZzHmG-1Yom_6fztUbw6l57e45XqWPvt6PIMsk27u-k7ZE0bNyyber8oZ4lDP-Sje6rqgLgd6oFY8v_OZf35gaEFQjp5bD6GWFvKrESzXNg2LnaTMWkjY6VClFqsE020UBmrtKbLm0tzuV9q-mfy-qEByHqNShiZx53zjdvcfax9YSpqjYa_iEta-pfnkaozHo2foAqjvgl87ldRPPaqq-5Ow9aONiC8cMpb1HPwD9Yxd0XWicf2WyiEvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5606f153ba.mp4?token=knbZGaBtpUcdPAJATd6n_V3TDzgakHTTHErav814gOCbtDScUqv4b8POI4FOIzTJzNPQeoTBD3JHNyJktG3IEKt-HOcMmOtd4MtK13h5nVNYccGA856hiATgQy3Cvmp76qIGZG-t3caHj4DCTC0TM3KutCSMFdSI_fzcgBjg1CtvyV8YzYMmgu7dyZXqGujtS05XhkS5RG2EdxGf2ZpU4xCpppGW-Dm8-Kz_WQeE9uOpYD8T4n0cIZdJhzK4B49mMEYXNeCPUa_66TOi3H30m17i71yeqkwCXfDHhwkixf4pzhRXsFkG1wlNfXTi_hd_9wU0Pzj4KcdYfgo9R1CmBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5606f153ba.mp4?token=knbZGaBtpUcdPAJATd6n_V3TDzgakHTTHErav814gOCbtDScUqv4b8POI4FOIzTJzNPQeoTBD3JHNyJktG3IEKt-HOcMmOtd4MtK13h5nVNYccGA856hiATgQy3Cvmp76qIGZG-t3caHj4DCTC0TM3KutCSMFdSI_fzcgBjg1CtvyV8YzYMmgu7dyZXqGujtS05XhkS5RG2EdxGf2ZpU4xCpppGW-Dm8-Kz_WQeE9uOpYD8T4n0cIZdJhzK4B49mMEYXNeCPUa_66TOi3H30m17i71yeqkwCXfDHhwkixf4pzhRXsFkG1wlNfXTi_hd_9wU0Pzj4KcdYfgo9R1CmBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات گسترده روسیه به کی‌یف، پایتخت اوکراین، با پهپادهای گران-۲ و موشک‌های بالستیک اسکندر‌-ام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/652217" target="_blank">📅 05:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652216">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijI6GZ_SLBo2Kc6HBHX59cXkcM-PTLDE4-qZu9q4zshiXPf7z3K70_Rrc7SFXysC1U6J8Hq4ZBSzzcHBXsXsWROpempDKmUqnOqfb-xFUdoB8Doc1oU8ehbCnjmjR8fcm55xe8OiPIOeDoPj2hK0z0fLO75lGYH-i7Yao4IFOOrrTWWQ0EYsC9-Yh4ND3k9g7RDGz9II86J_c_XuuqoVwOdqGVc5Ap00A_Yew0lLX6WaBwiP0w39PaK1kHs5tln7tEeeJzJg3CMfNOsA8zHpvdd8hJXAi0bWGNPcVr8juPjnCVlsu-7nCpJwjDyJxalkfCqT3g1XRwlz4vJQx8of_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناوگان اورژانس کشور جان می‌گیرد
🔹
معاون وزیر بهداشت: در سال جاری، ۱۰ هزار و ۵۰۰ میلیارد تومان به حوزۀ اورژانس کشور اختصاص‌یافت تا فرسودگی ناوگان و مشکلات این حوزه مرتفع شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/akhbarefori/652216" target="_blank">📅 05:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6Yst4EfJ6YsmKUiRCccNqa-E6C_UlE_EgVUr7ryMFYhuqSvK9VqZ6XFQr-VRkicNhgPt4UevpBTylvqJrLE1Vhw-youwRhZL_XKaurXrSK9Atd8UFvI9Kr21zqXIWFXBAiuVU0XuPQDnzWN6zk9ZIZgSbTxgXxHyq-7dsFJ8oZmwNjEQxCPzPFldn3NyANhoXtBP7oTeVJx97CmszRLPUfr3T5ucTVIEyYNu7jA0WVJBIVC5Zrqk9Q68-nlkJ_0usIQH_mGAOp1t4-eZX9hi9EgBNafl9i-juq5gVBtiHl_KOXyXsRucpQiO_GKATGpRjZ_ZDeDlRMQbmhHFyZ6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا در فکر تسهیل خرید نفت ایران توسط دو بانک چینی
🔹
انتظار می‌رود وزیر خزانه‌داری آمریکا موضوع تسهیل خرید نفت ایران توسط دو بانک چینی را مطرح کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/652215" target="_blank">📅 04:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تصمیم اسرائیل برای عملیات در عمق خاک لبنان
🔹
نشریه «اسرائیل هیوم» بامداد پنجشنبه گزارش داد: «کابینه امنیتی اسرائیل به ارتش دستور داده تا طرح‌های جدیدی را برای عملیات‌های عمیق‌تر در لبنان آماده کند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/akhbarefori/652214" target="_blank">📅 03:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2da36df3a.mp4?token=j8Pa3pYzoHzzs0tnHGQb64cDEW2lVN24zgjp5IVhn5gBwuxuel0JED4gvO6WsFtCpOjhRYoYh5kZr1z-52vz4MwrzkSYqxyXsGtBlBuMV1tOB5mYPcC_2ffcgy8is7KCthB1T0xPLmFrtSIvFY6wQ7AJCvjIn3rhfDWBKFRpVtOc6JD4ZFNSVkDRpvuUMLvVXxyqu96Z771fqc9VnuaHcEy1R8bY3Lgz1DEgzx8hSkXeQwmnkgqNldnCjysayDwlgQ7Tab1DNZtIJ1BjGHOZEW1TtMAFuP_iinyjUnHTjc2EXO28dEA750MTmlWzXaB45v9Nn6OeEhK7otHOwrOcAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2da36df3a.mp4?token=j8Pa3pYzoHzzs0tnHGQb64cDEW2lVN24zgjp5IVhn5gBwuxuel0JED4gvO6WsFtCpOjhRYoYh5kZr1z-52vz4MwrzkSYqxyXsGtBlBuMV1tOB5mYPcC_2ffcgy8is7KCthB1T0xPLmFrtSIvFY6wQ7AJCvjIn3rhfDWBKFRpVtOc6JD4ZFNSVkDRpvuUMLvVXxyqu96Z771fqc9VnuaHcEy1R8bY3Lgz1DEgzx8hSkXeQwmnkgqNldnCjysayDwlgQ7Tab1DNZtIJ1BjGHOZEW1TtMAFuP_iinyjUnHTjc2EXO28dEA750MTmlWzXaB45v9Nn6OeEhK7otHOwrOcAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف سناتور ارشد آمریکایی به شکست و تحقیر یک ابرقدرت نظامی با بودجه تریلیون دلاری
🔹
واشنگتن با بودجه‌های تریلیون ‌دلاری مقابل ایران با بودجه‌ای بسیار ناچیز به گروگان گرفته شده است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/akhbarefori/652213" target="_blank">📅 03:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7dV017WBlwOe-QDubMm53jTtXxT0bquIZF81ukTIELDjR18lXkVWGVw-SjtItcBQq-tGQEg7SR2peaNx2JXb90T40s6i8G8qIm_6fSszrcQTzUmAxfpSACG2Z5nqQeakzCkEsApCiVMqn95q72ZViRMUHr8hyNJKHToG_0oLJZ7N9oWrm1o83DtEOPcWnbBMRyrg-alftyXOWK6-apH6OiiFcHfHnuNA4_i1FQgu2AmxFw6_yUQAWesf4VP2Yq7D5r_YUyrS_Q6fCGPRAgzy7HPIli_qGKTFuvkej5gG83374GPK1BtLDA7-fEezzoYYhRFR6MT-gS5qCMUTnnkCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لغو استقرار ۴ هزار نظامی آمریکایی در لهستان
🔹
مقام‌هایی در ارتش آمریکا می‌گویند که وزارت جنگ این کشور برنامه استقرار بیش از چهار هزار نیروی نظامی در لهستان را لغو کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/akhbarefori/652212" target="_blank">📅 02:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شهادت ۲۲ لبنانی در حملات رژیم صهیونیستی در ۲۴ ساعت گذشته
🔹
وزارت بهداشت لبنان خبر داد که طی حملات رژیم صهیونیستی در منطقه جبل لبنان و جنوب این کشور طی ۲۴ ساعت گذشته، ۲۲ نفر به شهادت رسیده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/akhbarefori/652211" target="_blank">📅 02:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وزیر خارجه آمریکا: تلاش داریم که چین را برای قانع کردن ایران قانع کنیم
🔹
مارکو روبیو، وزیر خارجه آمریکا: امیدواریم که بتوانیم چین را قانع کنیم تا نقش فعال‌تری برای قانع کردن ایران جهت توقف اقداماتش در خلیج فارس ایفا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/652210" target="_blank">📅 01:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
رئیس ائتلاف حاکم در اراضی اشغالی، با مشارکت تمام رؤسای فراکسیون‌های ائتلاف، رسماً لایحه انحلال پارلمان این رژیم (کنست) را ارائه کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/akhbarefori/652209" target="_blank">📅 01:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652208">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf6sWzwHurecJNQJSWpzhPQIRMzBHOb4M7PqoVZ5RCi9ZE84l4lD1qX8K39sLhre6XGNLPGZvImdu6SexY0zzV_dy__xn5q3aFEQ2uBNg1A58i7jnHgOODQmJ72v2WOY2UC2AzOPn-fYaDY8kq0zdKwEvCJAsJBTKWQ4WNwdKEThYshSWrpiBW81BF_28-CIhMem7jboFdIiiaaNR9UeWQEcrCVgC0ZVAEOGzjr7NRP7je466NKe3tRagdT1uAldcbv5BwQt-DiuRr9aoiOPEd_mskwo7MWrMy7pki-PClAOtIMo1fZm8EpLeKvA5GIOU60tn1FXMRNTIR7O2PLneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بجنگ برو جلو
🔹
تیم ملی فوتبال کشورمان بیش از اعزام به مسابقات جام جهانی امشب بدرقه ای خاص و متفاوت داشت و در میدان انقلاب توسط مردمی که بیش از ۷۰ روز میدان دار خیابان بودند بدرقه شدند. ملی پوشان ایران میثاق نامه ای قرائت کردند و گفتند که قول میدهیم تا پای جان برای موفقیت و سربلندی ایران در جام جهانی تلاش کنیم
🔹
هفتصدوچهل‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori
,</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/akhbarefori/652208" target="_blank">📅 00:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652207">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
توافق محرمانه آمریکا و چین بر سر ایران
👇
khabarfoori.com/fa/tiny/news-3214648
🔹
سخنی که گور بی بی را می کند | نتانیاهو به زودی ترور می شود؟
👇
khabarfoori.com/fa/tiny/news-3214727
🔹
حرف‌های منشوری پشت سر امانوئل مکرون و گلشیفته | سیلی برژیت به‌خاطر بازیگر ایرانی بود؟
👇
khabarfoori.com/fa/tiny/news-3214825
🔹
روند مورد علاقه ترامپ: وقفه‌ای کوتاه پیش از دور بعدی خشونت | آتش‌بس هنری است که ترامپ ندارد
👇
khabarfoori.com/fa/tiny/news-3214576
🔹
تمام قاره‌‌ها درگیر انواع‌‌ هانتاویروس | بیماری که با آنفولانزا اشتباه گرفته می‌شود اما کشنده است
👇
khabarfoori.com/fa/tiny/news-3214245
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/652207" target="_blank">📅 00:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652206">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حال دریاچه ارومیه خوب است اما تو باور نکن!
محمد کوهانی، دبیر شبکه ملی محیط زیست سازمان‌های مردم نهاد جوانان کشور در
#گفتگو
با خبرفوری:
🔹
بیش از ۸۰ درصد بستر دریاچه ارومیه زیر آب رفته، اما کارشناسان می‌گویند هنوز تا احیای کامل فاصله زیادی وجود دارد.
🔹
با وجود بهبود وضعیت، تراز دریاچه به رکورد سال ۹۸ نرسیده است. سال ۹۸ تراز دریاچه نزدیک به ۵ونیم میلیارد مترمکعب پیش‌بینی می‌شد اما در سال ۱۴۰۰ بدترین ترازها را ثبت کرد و برای رسیدن به تراز اکولوژیک باید حدود ۱۶ میلیارد مترمکعب آب در دریاچه وجود داشته باشد.
🔹
کارشناسان هشدار می‌دهند کاهش بارش و مدیریت نشدن آب در تابستان می‌تواند دوباره تراز دریاچه را کاهش دهد.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/652206" target="_blank">📅 00:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYm3wHn6dq2R5zklL6mTEixvv72C8RIW2Z_nfh8kR_c6p6aIrv4CDJK8JSb9qpzIcAzCN7AFQAbbiEyNNp-9gB3uU_T6jSiylEn91t5OTWWh7PYGYMf4gdJa1IKQJyS0yHsMgwewz3cmp4AL_Bfa0moZ5wVK55XbNg9KUh4wb5MZ1ez7X3Z7bbRC0eK_r6GqRtN1MpN6nuDd7iJHcBgqwDImimslP787sQBeciSeUd8IeJbUd5RjIqeVt96uNHSi1JHgUWutujFMCAXp_O_P1_DBIIvxkx1dK9bG-yrphr35p3bg8YIBjy7HlyJGQ0PE_mgHOGsq98zUPz4ZYIEmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی: حملات حزب‌الله شمال اسرائیل را فلج کرده است
🔹
مقامات محلی اسرائیلی به رسانه‌ها گفتند که حملات حزب‌الله باعث شده هیچ فعالیت اقتصادی و اجتماعی متمرکز و ثابتی انجام نشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/akhbarefori/652204" target="_blank">📅 00:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کاهش تقاضا قیمت کاغذ را کاهش داد!
نیکدل، رئیس اتحادیه صنف فروشندگان کاغذ و مقوای تهران، در
#گفتگو
با خبرفوری:
🔹
قیمت کاغذ تحریر و کاغذ A4 کاهش یافته است. کاغذ تحریر از ۶ میلیون و ۲۰۰ هزار تومان به ۵ میلیون و ۷۰۰ هزار تومان رسیده و قیمت یک بسته کاغذ A4 نیز به‌طور میانگین ۸۵۰ هزار تومان است.
🔹
این در حالی است که کاغذ A4 در هفته‌های گذشته با افزایش ۵۰ تا ۷۰ درصدی قیمت مواجه شده بود.
🔹
جنگ بر روی افزایش قیمت کاغذ موثر بود، اما دلیل کاهش اخیر قیمت کاغذ، افزایش عرضه، کاهش مصرف، کاهش تقاضا، نظارت سازمان بازرسی و کم‌کار شدن چاپخانه‌دار‌‌ها بوده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/652203" target="_blank">📅 00:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652202">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
توافق محرمانه آمریکا و چین بر سر ایران
👇
khabarfoori.com/fa/tiny/news-3214648
🔹
سخنی که گور بی بی را می کند | نتانیاهو به زودی ترور می شود؟
👇
khabarfoori.com/fa/tiny/news-3214727
🔹
حرف‌های منشوری پشت سر امانوئل مکرون و گلشیفته | سیلی برژیت به‌خاطر بازیگر ایرانی بود؟
👇
khabarfoori.com/fa/tiny/news-3214825
🔹
روند مورد علاقه ترامپ: وقفه‌ای کوتاه پیش از دور بعدی خشونت | آتش‌بس هنری است که ترامپ ندارد
👇
khabarfoori.com/fa/tiny/news-3214576
🔹
تمام قاره‌‌ها درگیر انواع‌‌ هانتاویروس | بیماری که با آنفولانزا اشتباه گرفته می‌شود اما کشنده است
👇
khabarfoori.com/fa/tiny/news-3214245
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/652202" target="_blank">📅 00:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652201">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfHqeolspBs83CbWTvzIKxx7RKTd5z_PCLQlhzchWmydlfE7OFCrSC_lNGNVEPuLsNjC-19z1_U3J_pZBd5650ll4qr9rpSZU9kx8GlLOocLocnTOZXK8QV7R1UVguOzDZl_lGl99aifzuVbFxENrp-25t5bcfW6KSVmBuK5t3FpvuMrgxFO4YxCCUefdscM54Spx5QurYzjpOT8xHF6p93-i5hVvHeHftcVYvnYm4KCeTXLtyq5AKyriux0tVUdS1gAg7cFNX-gtQ1aczwITKJiERInppMM8Cdzuskf9r4i5_X5l00Cj4o4km_X5TXU3Ri2-gcR5ulkF4CuMop3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به اظهارات اخیر نتانیاهو؛ همدستی با رژیم اسرائیل غیرقابل بخشش است
🔹
نتانیاهو اکنون به‌صورت علنی آنچه را که نهادهای امنیتی ایران مدت‌ها قبل به رهبری ما منتقل کرده بودند، افشا کرده است.
🔹
دشمنی با ملت بزرگ ایران، قماری احمقانه‌ است؛ و همکاری و همدستی با اسرائیل در این مسیر، غیرقابل بخشش است.
🔹
کسانی که در همدستی با اسرائیل برای ایجاد تفرقه نقش دارند، باید پاسخگو باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/akhbarefori/652201" target="_blank">📅 23:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652200">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtvmL3zNdsef4ep7CMhLHTBlmY6SG0c1fpYCTJfb_B5rvAFRmIE-IavWDqshBHeJB6t4FJPO3Ylq_o0QjxLTONWgQhvQC4XrJenOBaJ0K1F9dWjTBoo1S8b67Z3CEzCVutLysidQv_hcaawHaYc5kgMBUG7JXntQ2DyINgHJu9gPrA_3L6oVCgEFFRgiCRKlxa4lGfN-k3DA4KGKw1gKuPkbjjDcrlLOT6ghMJrkGg5rgYZjOT_xuZCVguPqXmfg4TKLHX1dJq1p1sZMI5WSMfSZ5v23Om76iroRcj78MZwxe5GHNjBKL9hSrBexfBVsHh2lIcJcdmz3eKzIXdt1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روبیو در اقدامی معنادار با لباس مادورو راهی چین شد؛ او چه پیامی به شی داد؟!
🔹
برخی رسانه‌ها و کاربران این اقدام را غیرحرفه‌ای و کودکانه و دون شأن یک وزیر خارجه دانستند؛ رسانه‌های چینی هم این اقدام را تحریک‌آمیز توصیف کردند، به‌ویژه با توجه به اینکه روبیو قبلا به دلیل مواضعش، هدف تحریم چین قرار گرفته بود.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3214685</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/652200" target="_blank">📅 23:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652199">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/611faee3e5.mp4?token=FOrm-NE4ZKUdYLsVFtN4FcR0ZylQU-LeA6xdGZsLryx60WiPhbqeI0j28Ct7NjICam7zX72KBGOhi_mQ_S4tOPPULtw6wXpOb-znP9-QTZRWemyIkJtscxjo_DT7-bHmcrJaT3M07mV_afls4dvRX_Z3H70qPWmTRuUMJpxX_DU_KVZ4MUzMdOAP06g9HNZTbVkQiRkrRN7-PAMCfRZRcOCWZVHV_3bdiRrk5SAeX_2m728RIpQVZzCT9ovOQ1Mu6v1iz_cW9kE1h29JyZYnhVPGUNG-mlHaq7MxetUPkIw04U4uPrQu_X6QJckjeQLK2zj9oiYtnUw1aKhtNUGPDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/611faee3e5.mp4?token=FOrm-NE4ZKUdYLsVFtN4FcR0ZylQU-LeA6xdGZsLryx60WiPhbqeI0j28Ct7NjICam7zX72KBGOhi_mQ_S4tOPPULtw6wXpOb-znP9-QTZRWemyIkJtscxjo_DT7-bHmcrJaT3M07mV_afls4dvRX_Z3H70qPWmTRuUMJpxX_DU_KVZ4MUzMdOAP06g9HNZTbVkQiRkrRN7-PAMCfRZRcOCWZVHV_3bdiRrk5SAeX_2m728RIpQVZzCT9ovOQ1Mu6v1iz_cW9kE1h29JyZYnhVPGUNG-mlHaq7MxetUPkIw04U4uPrQu_X6QJckjeQLK2zj9oiYtnUw1aKhtNUGPDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری سی‌ان‌‌ان‌: براساس آن‌چه به ما گفته شده بود تا الان ایرانی باید تسلیم می‌شدند و محاصره آن‌ها را پای میز مذاکره می‌آورد اما نه‌تنها این اتفاق نیفتاده بلکه آن‌ها توانمندی‌های موشکی خود را بازسازی کردند و مواد هسته‌ای نیز در اختیارشان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/akhbarefori/652199" target="_blank">📅 23:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652198">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvGNy3dillNJM8e31Hzb1be1Q0gVbrkmQkdyrHZSTVqVf1W-gA1udbYuBauOXsKwGy0hZW_UhAee20xDjkqn6Agsb_I9NpDo0602YtOCWV02JtSCK4pylUeiC9En2VQ5zQY5bslirG9PgwEke6gAEVejupaPmEggDYunU5MN4K3She1qRrETaIksJHDtioUnrZvaqd8yQobeblmCQwGtp6LlOa258HCnu1hJM0ySeLQpYahTNIqQGA96mUlimyab06ml191kwAHTx9CTi4DgT5G7K34HoJwfpTVn8JMVSck9BkBEteLKGMQV8AI1IGTjCbGF_7obBqfZafuf0gKQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفیر روسیه در پاکستان: مسکو آمادگی خود را برای حمایت از تلاش‌های دیپلماتیک اسلام‌آباد با هدف اتمام جنگ آمریکا علیه ایران ابراز کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/akhbarefori/652198" target="_blank">📅 23:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652197">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bb06e773.mp4?token=ea1s5ItNb1kKruk1CLqpOWdDnMypRS5SokcsiEvYYWyxkhOACTJjWKb6KqICeSm1BDYyceuyEMUnWMetMhbgkYi3VDp_Mf62A-LbpNyDiCHlW969ldrYA-iJljPASxWMaLW0fPPujx5ZxgmBcylhVX60zjmwUf65xTfJZSlrQEEhzOWM6gotXMPm_4irVSiTS9HX0CRqWS86ImkiMUY3wjFotguR0pubSosFTwUx-yGJHlJEjS9WDeG3mytEx22DszxltWeHl6c0GhDOEcTyh0U3Gfwz6_RclNL8VhvaGNbtJ6tsJp5jQokI4kUb8HO2_hGWEXylzQfhWNDF4kl1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bb06e773.mp4?token=ea1s5ItNb1kKruk1CLqpOWdDnMypRS5SokcsiEvYYWyxkhOACTJjWKb6KqICeSm1BDYyceuyEMUnWMetMhbgkYi3VDp_Mf62A-LbpNyDiCHlW969ldrYA-iJljPASxWMaLW0fPPujx5ZxgmBcylhVX60zjmwUf65xTfJZSlrQEEhzOWM6gotXMPm_4irVSiTS9HX0CRqWS86ImkiMUY3wjFotguR0pubSosFTwUx-yGJHlJEjS9WDeG3mytEx22DszxltWeHl6c0GhDOEcTyh0U3Gfwz6_RclNL8VhvaGNbtJ6tsJp5jQokI4kUb8HO2_hGWEXylzQfhWNDF4kl1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی پربازخورد در فضای مجازی از تشبیه فروشندگان vpn به خوک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/652197" target="_blank">📅 23:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652196">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نسخه نجات بورس در بحران؛ چرا بستن بورس خطرناک است؟
🔹
بورس بیش از ۷۰ روز است که تعطیل شده، اما راهکار واقعا تعطیلی بود.
🔹
در این ویدئو چند پیشنهاد جهانی برای عبور بورس از بحران‌هایی چون جنگ پیشنهاد شده که می‌تواند به بورس ایران نیز در صورت بازگشایی کمک کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/akhbarefori/652196" target="_blank">📅 23:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652195">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31dde9b497.mp4?token=gP-yAHa9tDgb9LCgWcbz9gx8uIlpZG5YxFtnAQbKdkf4A5_W1minVl_Ajwd6eZ4Le6itberPX3PrsNaAaGZEXQSMxRJ05wmMH8FcqFpxhFlqHhCdK2tIoBbMWJtc55FKyzhFdEToDAfnkUAn-WTiM1NV-8_I5u6OfnzcvwQqx0Gu6nwLhoOBWadb2sMj4tT8DcPBukHnom2rFqnAc83rsmwwmIM3oxfvrceQpJjjBn1UXiqz8-nC9yHuPzzvJWJwZRUM9mYRf2MLiu0SN4dYrch8lCE8EOHkgEoWCRVkTTdMWk9gQiZVV4DrkoFpnAKG-0j0uhquQzLPErj4jKYVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31dde9b497.mp4?token=gP-yAHa9tDgb9LCgWcbz9gx8uIlpZG5YxFtnAQbKdkf4A5_W1minVl_Ajwd6eZ4Le6itberPX3PrsNaAaGZEXQSMxRJ05wmMH8FcqFpxhFlqHhCdK2tIoBbMWJtc55FKyzhFdEToDAfnkUAn-WTiM1NV-8_I5u6OfnzcvwQqx0Gu6nwLhoOBWadb2sMj4tT8DcPBukHnom2rFqnAc83rsmwwmIM3oxfvrceQpJjjBn1UXiqz8-nC9yHuPzzvJWJwZRUM9mYRf2MLiu0SN4dYrch8lCE8EOHkgEoWCRVkTTdMWk9gQiZVV4DrkoFpnAKG-0j0uhquQzLPErj4jKYVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب آبادی، معاون وزیر خارجه: موضوع تجاوز نظامی رژیم آمریکا و رژیم صهیونیستی علیه ایران، در گفتگوهای وزیر خارجه در هند مورد توجه خواهد بود
🔹
البته با پیچیدگی‌هایی نیز مواجه هستیم. یکی از کشورهای همسایه که عضو بریکس است، در طول تجاوز نظامی علیه ایران سابقه خوبی از خود نشان نداد و قلمرو خود را در اختیار متجاوزان قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/652195" target="_blank">📅 23:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652194">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
چینی‌ها از افزایش قیمت نفت ناراضی هستند/ تاکید برای بازگشایی تنگه‌‌هرمز در این دیدار
عرفان حمزه، کارشناس مسائل چین:
🔹
با توجه به تنش‌هایی که بعد از روی کار آمدن ترامپ پیش آمد، یک نبرد مخفی میان آمریکا و چین رخ داد.
🔹
ترامپ می‌خواهد چین نفت را با قیمت بالاتری بخرد و از ابتدای جنگ نفت ۷۰ دلاری به۱۱۰دلار رسیده است که افزایش قیمت نفت سرعت توسعه چین را کاهش می‌دهد و چینی‌ها به شدت ناراضی‌اند.
🔹
ممکن است این تنش‌ها جدی تر شود مگر اینکه آمریکا و چین با هم به یک توافق جامعی برسند.
🔹
پرونده ایران به عنوان یک مسئله اقتصادی و سیاسی برای هردو طرف مهم است.
🔹
احتمالا در این دیدار هردو کشور به بازگشایی تنگه هرمز تاکید داشته باشند.
🔹
توصیه می‌کنم سیاستمداران ایرانی لحظه به لحظه این رویداد اقتصادی و سیاسی را رصد کنند تا در صورت نیاز بتوانند در پاسخ به آن اقداماتی انجام دهند./جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/akhbarefori/652194" target="_blank">📅 23:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652193">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/856039f6ff.mp4?token=FNo9CYcsv-HbnRwSJ9Fl-b85uthyqnhlTeVxS2ZTwYKvxJntB82g5Ypt6q2S_QIfiyF5kjfTPlE1PG7qv68icm1GaoGJXvSS0PxfihwT0J-uiYPFo8J4_Gh7URQLMt-Jva2yOhpVHVRPU72Z0ljBlffDo6zqALzcQ462nHvnGZGYsYy7niYWaKafeThnSwFO3PhPLZ0R8ZUdt1w7qrh7du9pDlzvA7OLXcvrkQHXaPKfv5okiuIvdwkfyyTkXtHu9RIjpcamBx00Xt1EvsHG-DyG6YhcMAwK_vzzA7jMAHWzM2_Khca6g6tN5yWVyqje2F7nkbx7vKz72bEcaKyfzzUACJ1G2aJUyiML7opbrbCYXBwcC0eGP0-U59SG0KF6rBiEAbBP3h0NxGErmsd6y8423mm9JvdZBiy4De-WWw_wMYszMm2vX58vJMQxBd2I9lnPFlO-CB7OP82nVJMGJU066biib6h8U_CfkAJWRosqWFZu68tSJBAFQE0lQkJ-ETLwBX0jnzJqmGS9zhnQSHeXCVRVeOMPrAmiiJmtafurOoArx19bj3ECglTrs0jU8v4e_XsBGYKdjSwuwz9xCxyfZcQwcwE3E9V3DojjcRQRVzAgx7F_TiT3OTJtJqPj_ghK_DZ8bZ7QyLHvwtmH1jmdqVAfPx7cgqAeJ4hiIG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/856039f6ff.mp4?token=FNo9CYcsv-HbnRwSJ9Fl-b85uthyqnhlTeVxS2ZTwYKvxJntB82g5Ypt6q2S_QIfiyF5kjfTPlE1PG7qv68icm1GaoGJXvSS0PxfihwT0J-uiYPFo8J4_Gh7URQLMt-Jva2yOhpVHVRPU72Z0ljBlffDo6zqALzcQ462nHvnGZGYsYy7niYWaKafeThnSwFO3PhPLZ0R8ZUdt1w7qrh7du9pDlzvA7OLXcvrkQHXaPKfv5okiuIvdwkfyyTkXtHu9RIjpcamBx00Xt1EvsHG-DyG6YhcMAwK_vzzA7jMAHWzM2_Khca6g6tN5yWVyqje2F7nkbx7vKz72bEcaKyfzzUACJ1G2aJUyiML7opbrbCYXBwcC0eGP0-U59SG0KF6rBiEAbBP3h0NxGErmsd6y8423mm9JvdZBiy4De-WWw_wMYszMm2vX58vJMQxBd2I9lnPFlO-CB7OP82nVJMGJU066biib6h8U_CfkAJWRosqWFZu68tSJBAFQE0lQkJ-ETLwBX0jnzJqmGS9zhnQSHeXCVRVeOMPrAmiiJmtafurOoArx19bj3ECglTrs0jU8v4e_XsBGYKdjSwuwz9xCxyfZcQwcwE3E9V3DojjcRQRVzAgx7F_TiT3OTJtJqPj_ghK_DZ8bZ7QyLHvwtmH1jmdqVAfPx7cgqAeJ4hiIG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا جلسه اخیر هگست برای افزایش بودجه نظامی آمریکا اهمیت دارد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/akhbarefori/652193" target="_blank">📅 23:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652192">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رسانه‌های عراقی از شنیده‌شدن صدای چندین انفجار در اربیل خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/652192" target="_blank">📅 23:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652191">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
سخنگوی جنبش حماس: آماده واگذاری اداره غزه هستیم اما سلاح مقاومت در مرحله دوم بررسی می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/652191" target="_blank">📅 23:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652190">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آخرین تغییرات قیمتی روغن، برنج و حبوبات
کنگری، رئیس اتحادیه بنکداران مواد غذایی تهران در
#گفتگو
با خبرفوری:
🔹
روغن در فروردین ماه، ۱۶ درصد و الان ۱۵ درصد افزایش قیمت داشته است. قیمت روغن ۸۱۰ گرمی در بورس کالا ۳۲۷ هزارتومان می‌باشد اما در شبکه‌ تنظیم بازار این محصول ۲۸۱،۹۵۰ تومان به دست مصرف‌کننده می‌رسد.
🔹
سایر کالاها مانند حبوبات و برنج روند کاهشی در بازار داشته‌ است.
🔹
روند عرضه و تقاضا به طوری هست که انگار در شرایط جنگی نیستیم. زنجیره تامین در کنار زنجیره توزیع قرار گرفته و روند عادی را طی می‌کند. تا این لحظه مشکلی در راستای مواد غذایی به خصوص کالاهای اساسی نداشتیم.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/652190" target="_blank">📅 23:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652189">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
نخست‌وزیر انگلیس در نخستین جلسه مجلس عوام پس از بازگشایی پارلمان، بار دیگر ورود شتاب‌زده به جنگ علیه ایران را خلاف منافع کشورش دانست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/652189" target="_blank">📅 22:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652188">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Muq37frzlYQHtSFbjFA-u2dG8iPIu8KiHD6wTY6xplPZdlC64CdOjJgCopPU9GLuuoOkjaEAK9rxPZBLWMKHcrHQKsWEaWtU05CjDCJfBGyBhY_F5weoNOM66U3_CHuBCY9I0NIuZashMZFWkeAbBD6K-k9YIjQijStuPtsU7b7mXo4AGLx-C0SmuIsn3mwzNCiHC-90w2lnFJCnxdYFWQ2XvEPUSHr4zyW0Uf8Pj3rxhWcHTUAm8V4if_UmJi0kb1wBoLNwQz-Ywe7jcofjUPrTWlf7kxQ28sQ4jEj4eh6lgvJj_h2Xz9K2IlepdkQlp1gwM8XUtsifDon28J6gEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رأی ۵۰ در برابر ۴۹؛ سه سناتور جمهوری‌خواه مخالف جنگ با ایران شدند!
هیل:
🔹
سه سناتور جمهوری‌خواه از رهبری خود جدا شدند و به پیشبرد قطعنامه‌ای برای توقف درگیری با ایران رأی دادند.
🔹
سناتور لیزا مورکوفسکی، سوزان کالینز و رند پال و تقریباً تمام دموکرات‌های سنا در رأی‌گیری برای پیشبرد قطعنامه‌ای که به ترامپ دستور می‌دهد نیروهای مسلح را از خصومت‌ها علیه ایران خارج کند، پیوستند.
🔹
پیشنهاد لغو قطعنامه از کمیته روابط خارجی سنا همچنان با رأی ۴۹ در برابر ۵۰ شکست خورد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/652188" target="_blank">📅 22:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652187">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
نیویورک تایمز به نقل از مقامات آمریکایی: شرکت‌های چینی در حال مذاکره با ایران در خصوص فروش تسلیحات هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/akhbarefori/652187" target="_blank">📅 22:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652186">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
«ناوگان جهانی صمود» فردا (پنجشنبه) از شهر مرمریس ترکیه در ساحل مدیترانه، در تلاشی دوباره برای شکستن محاصره تحمیلی رژیم اسرائیل بر نوار غزه با مشارکت ۵۴ کشتی، حرکت خود را آغاز می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/akhbarefori/652186" target="_blank">📅 22:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652185">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fc80f2a9d.mp4?token=uk61O8B_lRNT323cNJt0WdEtYDDg3WqSsxyxdz09oALKYY3L-mH9saNkTkh4Brtt9rrvWivk-9XvCV2_YjwtwzNX-My6rDE08ywfC-E0Ehw-ydQ-xkG9CzOY_hF_LJSLOyB4DO7oFfVt3prkACCRNjT7evIze0M76Ub99dNHqeVQIr59vbC1x0t2wIOa5q5Kl6keT-l7YBODGrEOnE0pgWcQmFMRJDMMx16RjbIHFaPX58XATMTPn16NK7B7WBmZWsIkyCPN-TLgmKrbkigd1V-qDDhNtDoRbLjQWxD7hN63S_zHwZkGArBvUTpxoD3oq3ow2TzGnT2IAs5E3q6DbEgh2upbf1l57GRu0bPTX6OqRpfN5WKy-VK18-5C45m-jmOXkxY4wJTYamOXjPHmnsTFl6YA1WoV2a1iS5TIB9HSlRvx1LpstM8A7ZrgBPC__y2OcPN1Fd9I1ut8Z1ru3-9lvyuPN3bTOZvHfTg6TPKXINqq5H_IcYF92iEqudHe-yjvFGzJu2QGmRFQqnUaRhspfA2N5ZQ7-rmRLArVqaeSST6fZxcz-Nw52hYr5wTSrikD9sQPCAdjclfxS1IEXEN2jJ5eYKKg26DfcVO40h6kP8JR7njVPV84y992owqg6GeeUmRpS75pDtG2tWo6-BiJE1oGrnqFRQ-fBS_EnwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fc80f2a9d.mp4?token=uk61O8B_lRNT323cNJt0WdEtYDDg3WqSsxyxdz09oALKYY3L-mH9saNkTkh4Brtt9rrvWivk-9XvCV2_YjwtwzNX-My6rDE08ywfC-E0Ehw-ydQ-xkG9CzOY_hF_LJSLOyB4DO7oFfVt3prkACCRNjT7evIze0M76Ub99dNHqeVQIr59vbC1x0t2wIOa5q5Kl6keT-l7YBODGrEOnE0pgWcQmFMRJDMMx16RjbIHFaPX58XATMTPn16NK7B7WBmZWsIkyCPN-TLgmKrbkigd1V-qDDhNtDoRbLjQWxD7hN63S_zHwZkGArBvUTpxoD3oq3ow2TzGnT2IAs5E3q6DbEgh2upbf1l57GRu0bPTX6OqRpfN5WKy-VK18-5C45m-jmOXkxY4wJTYamOXjPHmnsTFl6YA1WoV2a1iS5TIB9HSlRvx1LpstM8A7ZrgBPC__y2OcPN1Fd9I1ut8Z1ru3-9lvyuPN3bTOZvHfTg6TPKXINqq5H_IcYF92iEqudHe-yjvFGzJu2QGmRFQqnUaRhspfA2N5ZQ7-rmRLArVqaeSST6fZxcz-Nw52hYr5wTSrikD9sQPCAdjclfxS1IEXEN2jJ5eYKKg26DfcVO40h6kP8JR7njVPV84y992owqg6GeeUmRpS75pDtG2tWo6-BiJE1oGrnqFRQ-fBS_EnwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین پاک، کارشناس جبهه مقاومت: امکان ندارد ایران به خاطر واسطه شدن چینی‌ها از شروطش کوتاه بیاید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/akhbarefori/652185" target="_blank">📅 22:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652184">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
وزیر خارجه کوبا: حمله آمریکا منجر به حمام خون خواهد شد
🔹
شهروندان کوبایی و آمریکایی کشته خواهند شد و تنها سیاستمدارانی که فرزندان و خانواده‌های خود را به جنگ نمی‌فرستند، جرات اجرای چنین سناریویی را دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/652184" target="_blank">📅 22:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652183">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
حکم قصاص قاتل شهید دهقانی اجرا شد
🔹
سرهنگ دوم شاهین دهقانی دی‌ماه به شهادت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/akhbarefori/652183" target="_blank">📅 22:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652182">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FApJDKowJpH9q0Tmco8nlq1qKYfVTU9iN2PzN7UnwgU3gX6gHRtuRE6CjAbQiGuHrfLJHEkCvKgBX6_y8-HqPNVKDjwEQv2F_4zetRmQBVj-4kL-KSfKMaE5cGLCBWOA2IDuwu-febYGEZ8rKtL2oIptV1xtBrhpJDeaSt2HghxEiqUlS8cjOIIFWTHch-o2pnRcJWy413_-fAlgE-jD5WwaZd4ZsJ9pBmNJy6LkVOA7Zpp1nbt2BM3vJdgxA8ByFHgIoF9dp9WoBUObuK6P7V0Se3V8_8aRl0jyetVjXMcd13jja0Zch4zotzth4ioPPcBw23IDZFtisJiCaMLqAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یمن: عواقب جنگ علیه ایران دامن تمام دنیا را خواهد گرفت
🔹
معاون وزیر خارجه یمن تصریح کرد حمله خصمانه علیه ایران، امنیت و ثبات منطقه و جهان را تحت الشعاع قرار داده و تداوم آن، منطقه و جهان را به جنگی خواهد کشاند که پیامدهای آن گریبانگیر همه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/akhbarefori/652182" target="_blank">📅 22:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652181">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6670d6dcb3.mp4?token=NHhhe0mi3P_zckoq2OqhyRBr7lmpzyfPffgQJdhx4lqX8Zdz7yNFHVemsjCCefa3Trt-GBEX3ReEGHMbQMDKlyXV9Qh53LQwt3lGliOenHOz611kIrsGK7fnAYx27Wek5QhSu6PfBdE8Y9k94NW4HkYmRaNUZ98HetVOkG_D6DmbvsGYJ2aLzCT03QaEOwwOMip0IaRwxBjQV82mbbXXWpSN8TgtGkCZDczi7ruXgSUchkq7KYkC8ZgGauK8pBew4ATqBAqBqr56NdCBnBIt5B5KWgVasMpLH4yqNT5Ifqfs4r3TH68eBQynppcu9lXUGgOCLcfQw0SGXyW3uCZqcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6670d6dcb3.mp4?token=NHhhe0mi3P_zckoq2OqhyRBr7lmpzyfPffgQJdhx4lqX8Zdz7yNFHVemsjCCefa3Trt-GBEX3ReEGHMbQMDKlyXV9Qh53LQwt3lGliOenHOz611kIrsGK7fnAYx27Wek5QhSu6PfBdE8Y9k94NW4HkYmRaNUZ98HetVOkG_D6DmbvsGYJ2aLzCT03QaEOwwOMip0IaRwxBjQV82mbbXXWpSN8TgtGkCZDczi7ruXgSUchkq7KYkC8ZgGauK8pBew4ATqBAqBqr56NdCBnBIt5B5KWgVasMpLH4yqNT5Ifqfs4r3TH68eBQynppcu9lXUGgOCLcfQw0SGXyW3uCZqcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های طوفانی مردم به توهم ترامپ!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/akhbarefori/652181" target="_blank">📅 22:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652180">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084593e8e6.mp4?token=gy46WyZer1gwu8zbvj7wklzJJscFBZlZwPSiPVg7FH18IqP9Bu7o6uwT8Ew0c3B3Muxd-RjbjiYBzHLmKzTA0aVgV8vnv2M9w-KG_l6w9Tla8I9HdnOgi2Lha-xOwb_Hpa_x16E3V-fQQiuCTUFRKDf6g91b6Y31PBGMMwnoKX3-1Ezx6sIMiAkEbUuHShlEPSKDyg8jMzbFNumGuHE94h4og07A3kt84GG0O9w9VjR3hb2wUwD6KwZANc7Gwrod5lw3cUsKYvE6ggCRqPtPYs2Aaq0ChNnlRblK3wWKcCrwd7uLWcyw1QhvvyI2Xr_6qzfWoUinI72dUYVi2iftVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084593e8e6.mp4?token=gy46WyZer1gwu8zbvj7wklzJJscFBZlZwPSiPVg7FH18IqP9Bu7o6uwT8Ew0c3B3Muxd-RjbjiYBzHLmKzTA0aVgV8vnv2M9w-KG_l6w9Tla8I9HdnOgi2Lha-xOwb_Hpa_x16E3V-fQQiuCTUFRKDf6g91b6Y31PBGMMwnoKX3-1Ezx6sIMiAkEbUuHShlEPSKDyg8jMzbFNumGuHE94h4og07A3kt84GG0O9w9VjR3hb2wUwD6KwZANc7Gwrod5lw3cUsKYvE6ggCRqPtPYs2Aaq0ChNnlRblK3wWKcCrwd7uLWcyw1QhvvyI2Xr_6qzfWoUinI72dUYVi2iftVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
زیباترین پادشاه ایران در مقابل هیولایی مانند محمد خان قاجار ...
نسخه کامل را اینجا ببینید
👇
https://youtu.be/IpMt8R6uBX4?si=-7JMsyhn60BXSofd
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/akhbarefori/652180" target="_blank">📅 22:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72a4aeebd.mp4?token=in8Iie36dp1BN0n3PY6oOlvbos5ubxFox4R_qPUCs7BaOuS0sWqtlPWdmQ3RRqNtXzCDijDqgmEfZtlN6NrL8ytNcxjoMAu4uxGAn8vwPnluM_xHXfkKxCOL4-Iz-TsAueYFrqDP-nkXfn5MxRlxjTgCpWlbBcmkTA1UkRT2KCjE997o2HI9bnUI54D0T4pw3hzle8D-jWqoMx4-MsF04d7vcuWIwXZhZWOI2uJYoMdCL_-NUCYnVhG_BdqeY0RbkaVuv8Y6PUYsbf2rcSZ1OOC4RV4XYWnqTY8Dms8OJ3Fc0La6lT72A3qXYZak7NoaheTAKlWExHmdGsZAlfvr84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72a4aeebd.mp4?token=in8Iie36dp1BN0n3PY6oOlvbos5ubxFox4R_qPUCs7BaOuS0sWqtlPWdmQ3RRqNtXzCDijDqgmEfZtlN6NrL8ytNcxjoMAu4uxGAn8vwPnluM_xHXfkKxCOL4-Iz-TsAueYFrqDP-nkXfn5MxRlxjTgCpWlbBcmkTA1UkRT2KCjE997o2HI9bnUI54D0T4pw3hzle8D-jWqoMx4-MsF04d7vcuWIwXZhZWOI2uJYoMdCL_-NUCYnVhG_BdqeY0RbkaVuv8Y6PUYsbf2rcSZ1OOC4RV4XYWnqTY8Dms8OJ3Fc0La6lT72A3qXYZak7NoaheTAKlWExHmdGsZAlfvr84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چی این چمدون رو سنگین کرده؟!
@TV_Fori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/652179" target="_blank">📅 22:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652178">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2AoVpbWvi60N0_O6NZ-f9r4bGF9zIDKOXOrFv0UUvUXr_zT1nFD9ph9SYLRu5AiAQWVsdyCbrW38MMGtOKVLqCQZChxarmWIbAACdSSPXMspB4VAjHhq_uXOlO40yFOUVUbHJ6h1Thg4A2V9r3qhMloirSABU3fhy1rpbV0jZv9xSNCZ-3b497lrgRyHRiDqz589LpyftJJ6mTLEyvL5DtBjQVAoIXskQAfqlWY5SDpqokqW9DnDX0nf4L7G1d1yIydHx-v7ZcEWO9EGJD-WqNPA7srK4Oj6E8vvVjl8dtWN5WwP6dr34ycgbf1Sy_GT2oleo_ab1Brg6CeUGrtIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد عباسی، قاتل شهید سرهنگ دهقانی که در اغتشاشات ۱۷ دی ماه با ضربات متعدد سلاح سرد به شهادت رسید، قصاص شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/652178" target="_blank">📅 22:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652177">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رسانه هندی: آمریکا جنگید، چین برد
تایمز آو ایندیا:
🔹
در حالی که آمریکا موشک‌های خود را شلیک می‌کرد و اسرائیل زیرساخت‌های ایران را هدف گرفته بود، چین بی‌سروصدا درحال برنده شدن بود.
🔹
پکن بدون کوچکترین مداخله نظامی، با محکوم کردن حملات آمریکا و اسرائیل، دفاع از دیپلماسی و تثبیت روابط انرژی با کشورهای مردد در قبال واشنگتن، جایگاه خود را به عنوان یک جایگزین آرام و قابل اعتماد تثبیت کرد.
🔹
آمریکا سرمایه دیپلماتیک خود را سوزاند، چین بدون هیچ هزینه‌ای نفوذ خود را از خلیج فارس تا اقیانوس آرام گسترش داد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/652177" target="_blank">📅 22:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652176">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D--FPf4f4baA4p7vVlFLo5A72Wg76-g2PxUJFnzIa14MIeuqbDrUaUMKPutESjjVuwYvtkloIkx5T1qyE5TyW6RUU9babKr3NmNafv5SK-e3aLvQ4NUANZnwEh9dcEFK4TfPBSXyoqXSR0m7gje_8NcHEQAIz4wNLILDTwnAsFlv53zLyRpviGGfQD2SFEwratJS8wJglZXosn965tan92gtWmwYef8rXoti0EOVhirqWxkhGN_IGsqmFNid8dt7lgF9y27xg-FORVteeXuc1-hOAMPS-0nA0f484ViR9MtyKwXCcXFnyMvgBrlbwZi8sf8iZ-Qx-QBcUzKYq4F9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ارتش: کنترل بر تنگه هرمز، دو برابر درآمدهای نفتی برای ما آورده اقتصادی خواهد داشت
🔹
امیر سرتیپ محمد اکرمی‌نیا: نظارت ما بر تنگه هرمز، هم درآمدهای سرشار اقتصادی به میزان حتی دو برابر درآمدهای نفتی برای کشورمان به همراه خواهد داشت و هم قدرت ما را در بعد سیاست خارجی تقویت می‌کند.
🔹
پس از پایان این جنگ، دیگر جایی برای عقب‌نشینی وجود نخواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/akhbarefori/652176" target="_blank">📅 22:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652175">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مراسم دعای ندبه_جلسه 48</div>
  <div class="tg-doc-extra">سخنرانی استاد رائفی پور</div>
</div>
<a href="https://t.me/akhbarefori/652175" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه چهل‌وهشتم
رائفی‌پور:
🔹
0:15:30 عاملی که آدمیت را از حیوان مجزا می کند
🔹
0:22:00 دنیا برای مؤمن مانند قفس است
🔹
0:26:15 عاقبت جامعه‌ای که در آن امربه‌معروف و نهی‌ازمنکر نباشد
🔹
0:41:00 معنای اصلی کشتی نجات بودن امام حسین(ع) چیست
🔹
0:46:50 ارزشمندی اشک بر امام حسین(ع)
🔹
0:58:50 مخفی بودن قبر مطهر حضرت علی(ع) تا زمان امام صادق(ع)
🔹
01:13:00 حضور امام زمان(عج) در روضه حضرت عباس
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/akhbarefori/652175" target="_blank">📅 22:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652174">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
نشست مشترک مجمع نمایندگان استان تهران در مجلس شورای اسلامی با جانشین فرمانده سپاه پاسداران انقلاب اسلامی برگزار شد
🔹
در این نشست مسائل مربوط به استان تهران اعم از نحوه تامین انرژی، آسیب‌های ناشی از جنگ، نحوه خدمات رسانی به شهروندان، وضعیت امنیتی و سیاسی مورد بحث و بررسی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/akhbarefori/652174" target="_blank">📅 22:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652173">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWrbnscwo-FXBI1b-Zl1TDiZ7bKSUYP6ElTyofQoVR7Vc4n5oiJ4-odC_l6-xkZ1Jg9_HdMAvRwPd-wJJG4GQa5n94PlUzbMP94-pAaCePGUL_PPQdrZmFDjg137l9aAR9lbq4NZVURdfWDppTcsAhID0M4ULaDTOd6tmaq_HNilvNQqOpt4NCrhWSBku9JopbhzpxtmuKmScK1l4me2e857MUtb39cudTTgGQkL7360NQ7xvnYf_sUywoEdp7cTCHQdPsOICafuhfYRQtHLWhiArdEEEXYLeXoKBWcZ3PbeTYggIHkeRybYOT-OEoJ3GjtbG-z582jKiS83OJ2Y4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن افرز: آیا ترامپ می‌تواند به توافق هسته‌ای جدیدی با ایران دست یابد؟ آن هم وقتی واشینگتن مطالبات بیشتری دارد و تهران اهرم فشار بیشتری
🔹
دستیابی به توافقی بهتر از برجام به مراتب دشوارتر است؛ چرا که توانمندی‌های هسته‌ای ایران از زمان خروج آمریکا از توافق سال ۲۰۱۵ به‌شدت پیشرفت کرده است.
🔹
ایران در سال‌های اخیر دانش فنی در تولید سانتریفیوژهایی کسب کرده که شش برابر کارآمدتر از مدل‌های سال ۲۰۱۵ هستند و سرعت نصب آنها نیز سه برابر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/akhbarefori/652173" target="_blank">📅 22:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652172">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
آرایش جنگی در کشور و کلیت جامعه در قبال جنگ جدید دشمن ایجاد نشده است
🔹
مهمترین گزاره های تحلیلی اقتصاددان فرهیخته دکتر خوش چهره در دومین نشست «مقابله با جنگ اقتصادی» در ستاد رسانه کشور:
🔹
درک درستی از تهدیدات وجود ندارد و بعضا شاهد ساده انگاری هستیم.
🔹
نابرابری میان تهدیدات و مدیریت تهدیدات در کشور وجود دارد.
🔹
قرارگاه جنگ اقتصادی با افراد امین، علیم و دلسوز می بایست تشکیل شود.
🔹
در درجه نخست نیازمند اقدامات آنی و کوتاه مدت برای کم اثرسازی برنامه تورمی دشمن هستیم.
🔹
مقابله با لیدرهای تورم، ضرورتی اجتناب ناپذیر است.
🔹
در تاریخ جنگهای جهان، دولتهای موفق در شرایط جنگی بیشترین سطح  مداخلات را در بازارها داشته اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/akhbarefori/652172" target="_blank">📅 21:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652171">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03968759d.mp4?token=pczm-X7zgr6qlXeLWuD7v5CEpqpwEQKcy4_9L2w-gf6ZWtDT2W-P2DPASgBBoqIjXzkPZ8uj4uZM-VKQt1idoIuJbbkDt50u692ESD_njQO7EZWlL--yB2KELJlGMzRClNp5phdwjv9q-k0SgWvKPo2lUVijmg1AIpu2QXsbgV3IPk8DzjfJFlGpQvh3PfEM4t3yPlWXnFA_yRCXe4pLB0Hmmf6_3CjHU5MxRQodxCyMW9-sfxzpRkTxwESJFALSEqFMTs_FaFDuuoI0T0bV5jZ40lekkdJakCqAZs3yLH7CjOgH80BzIcDn-bm5WnbinOXRT4nnFONJCnP1M0Sstg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03968759d.mp4?token=pczm-X7zgr6qlXeLWuD7v5CEpqpwEQKcy4_9L2w-gf6ZWtDT2W-P2DPASgBBoqIjXzkPZ8uj4uZM-VKQt1idoIuJbbkDt50u692ESD_njQO7EZWlL--yB2KELJlGMzRClNp5phdwjv9q-k0SgWvKPo2lUVijmg1AIpu2QXsbgV3IPk8DzjfJFlGpQvh3PfEM4t3yPlWXnFA_yRCXe4pLB0Hmmf6_3CjHU5MxRQodxCyMW9-sfxzpRkTxwESJFALSEqFMTs_FaFDuuoI0T0bV5jZ40lekkdJakCqAZs3yLH7CjOgH80BzIcDn-bm5WnbinOXRT4nnFONJCnP1M0Sstg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام رسمی خسارت‌های آمریکا در جنگ
🔹
اعدادی که امروز در رسانه‌ها خبرساز شدند.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/akhbarefori/652171" target="_blank">📅 21:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652170">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a758a0344c.mp4?token=hpO06GTrlX3wQ4Cfqgwo9dxfJTuIVjz0q3UOheksumJ3gS7dNnmOqZij5j2TEDgkNNShpB0--zhaPRlRneBbeofILUvG9LY1SZVV64nEYPAHq60-NwEBXBX4zZ90nhSXjpcUg42vNZ7vahcixolMjg-qeLhBmpwYmWwuf8WZ0nbwo4-uNm0TCE4C2zP7-B4j3R-t8lxZIXcWTkjhMUjAlrkLn_FuZs8TY-vcTtLvt7k0IBPC3Uv62WcKMuW0RwQoxoVMHhqv5Th1WzM6lUgd_-fDgBsuHQ7OBVLH44tzY_uRsna95hRMKyf5QSuTk5G-zVOjxi-2DvsVXIP7m0VCG3uyb6FduByUeVIcur0T7NDheCMQ9NiBoUi1PIn_CKTgdQCc7GauXnCWqGmY12k_jbBQYQ6qM95Luj7m0SuCplRwUR_Xo4NZVSyo0iZCWvz1DDTOePiJWnVUPLSzZcnDlkvzgdOjoVZwtiJqVEjTVDzY5i_XztDrkA1qy8-QYjEyttn2FBCeOxsCqnoVPe-oh2NzDKWTY1PDYnBlOWrZwAnaolMsC_eU2cFqsK872Vn5UGVliUrACzlsrlKOC2tCdBnkpoFizcEcUZr9ULv09kZV4fnwBEzOM7pDW2JiAbiJjtQCp1J2Uk4iLiLyavCi7fxS8rmBQqhgsVdrQzYIZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a758a0344c.mp4?token=hpO06GTrlX3wQ4Cfqgwo9dxfJTuIVjz0q3UOheksumJ3gS7dNnmOqZij5j2TEDgkNNShpB0--zhaPRlRneBbeofILUvG9LY1SZVV64nEYPAHq60-NwEBXBX4zZ90nhSXjpcUg42vNZ7vahcixolMjg-qeLhBmpwYmWwuf8WZ0nbwo4-uNm0TCE4C2zP7-B4j3R-t8lxZIXcWTkjhMUjAlrkLn_FuZs8TY-vcTtLvt7k0IBPC3Uv62WcKMuW0RwQoxoVMHhqv5Th1WzM6lUgd_-fDgBsuHQ7OBVLH44tzY_uRsna95hRMKyf5QSuTk5G-zVOjxi-2DvsVXIP7m0VCG3uyb6FduByUeVIcur0T7NDheCMQ9NiBoUi1PIn_CKTgdQCc7GauXnCWqGmY12k_jbBQYQ6qM95Luj7m0SuCplRwUR_Xo4NZVSyo0iZCWvz1DDTOePiJWnVUPLSzZcnDlkvzgdOjoVZwtiJqVEjTVDzY5i_XztDrkA1qy8-QYjEyttn2FBCeOxsCqnoVPe-oh2NzDKWTY1PDYnBlOWrZwAnaolMsC_eU2cFqsK872Vn5UGVliUrACzlsrlKOC2tCdBnkpoFizcEcUZr9ULv09kZV4fnwBEzOM7pDW2JiAbiJjtQCp1J2Uk4iLiLyavCi7fxS8rmBQqhgsVdrQzYIZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مثلث مرگ!
🔹
داستان واقعی نبرد ۴۸ ساعته سه سرباز ایرانی در مقابل ارتش دشمن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/652170" target="_blank">📅 21:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652169">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل به نقل از یک منبع نظامی گزارش داد: حزب‌الله از ابتدای جنگ ۴۵۰ پهپاد پرتاب کرده است که شامل ۱۲۰ پهپادی است که با استفاده از فیبر نوری عمل می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/652169" target="_blank">📅 21:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652168">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رویترز: عربستان و کویت در میانه جنگ ایران، حملاتی به عراق انجام دادند و پایگاه برخی گروه‌های عراقی را بمباران کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/akhbarefori/652168" target="_blank">📅 21:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652167">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA9d6xL-9RryguqokAX5s1FKwo5P-zRUjoarhei4MlwmHboq57lT0_K5ViXnTNdQT07W_JzQk3zOiPlK1YgT5b0El9eV_TaVlIt16aSWvCbVNd35fMqhR3St7LnMH1feftjXkBX2ynEj5PXwIsTZk6sTqg-2Wo9PSsIOhB-cD6u1Ht8DVF0cFrgFekgTXECVrlfpuHKGJpQQ97RWkBB5c2f7ZUV2FmnmPXfVuBPF2OuxrADH10Oh9KDVJFvOlsproqHAO3n7lbLNPOoqJZ1fFrAz3rL8ZbGzKiXG94K4a4ctnBdx7ztypRfze6eGKc3Q-TCgHYp-coKuSLETKRGf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: اطلاعات آمریکا نشان می‌دهد که ایران توانمندی‌های موشکی خود را به‌شکل قابل توجهی حفظ کرده است
🔹
تصویر ارائه‌شده دولت ترامپ از یک ارتش درهم‌شکسته، با آنچه آژانس‌های اطلاعاتی آمریکا در پشت درهای بسته به سیاست‌گذاران می‌گویند، تفاوت فاحشی دارد.
🔹
ارزیابی‌های جدید و محرمانه حاکی از آن است که ایران به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز دسترسی عملیاتی دارد.
🔹
نگران‌کننده‌ترین بخش برای مقامات ارشد، شواهدی است که نشان می‌دهد ایران دسترسی عملیاتی به ۹۰ درصد از ۳۰ سایت موشکی در تنگه هرمز را بازگردانده؛ امری که ناوهای جنگی و نفتکش‌های آمریکایی را در این آبراه باریک تهدید می‌کند.
🔹
به‌علاوه، ایران همچنان حدود ۷۰ درصد از لانچرهای متحرک و ذخایر موشکیِ پیش از جنگ خود را در اختیار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/akhbarefori/652167" target="_blank">📅 21:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652166">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdVI-BnZpWjsRVd86PqXcoIeC8YlYwz8ekFDv_8D8GcfbuDHL9RVaLWK2jYufzm2QlAEpKLjl7qHwRCJggtevVhxCHa4-w3frG3zpjdIQ4KilwAFx_7vgYYin0YhfB7JyAuyzu7iUAg6nvI5U3qkRhmWSD5GZ9677035hyKv9mVICGCf4yGj-74yJIHE6jwaivPl3O3cu0tAWvwTPx3SMHj_7SBzKojiW_drI_tVkQrM0h18Q4adN_ImsHiFsx7AQu2pGjWIIvzPwcRgpJczdqklXx-zHTdLmdx9p_IPERhRQS8XUH0QMdWZlY7XQuZasy9B6iHc1JoTlL_IhRvh2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: ایران ۶۰ درصد از توانایی موشکی خود را دارد
ایندیپندنت:
🔹
دو ماه پس از بمباران مشترک آمریکا و اسرائیل، زرادخانه موشکی ایران عمدتاً دست نخورده است و هنوز قادر به حمله به متحدان آمریکا فراتر از کشورهای خلیج فارس است.
🔹
کاخ سفید بارها ادعا کرده است که ظرفیت نظامی ایران «تخریب» و از بین رفته است، اما منابع ناتو به ایندیپندنت گفته‌اند که این درست نیست.
🔹
یک منبع ارشد ناتو در اروپا: «هرچه که دیگران در ملاءعام می‌گویند، ما تخمین می‌زنیم که ایرانی‌ها حداقل ۶۰ درصد از توانایی موشکی خود را دارند. ورودی‌های آنها بسته شده است، اما آنها هنوز در زیرزمین هستند.»/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/akhbarefori/652166" target="_blank">📅 21:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652165">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac658f9344.mp4?token=h94_dGmyKRSXXuW3CpkkUnNwHNu0viY0eCKIPLyE6oAQHnFuCvueM8wB2-47DAh6imlibYpyYWZESoo-dIyYMfTAxeiDVFhZYSkCWyTrjt4bKkMLDZVq-wxk-9QaW9Ht9ToMYyK2OiAsW9Hu92TSrsRKoBO2DN2plgeMaTvVLHVLEi442omOgh6rzuq84BUnePiyy25yvGAMsIxOqcS3rNRvigYMcIfJby6G2XCwkj4I63wO2LsnB9T4YlUJGxgS2cEBXpFQaiWi6nXR-KAEaXlE7AwSIpMMKi01KWxiMWj9Q0op2mU-nOe3HuXqy7M662u5oMaC9fzhXqsgGbWexw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac658f9344.mp4?token=h94_dGmyKRSXXuW3CpkkUnNwHNu0viY0eCKIPLyE6oAQHnFuCvueM8wB2-47DAh6imlibYpyYWZESoo-dIyYMfTAxeiDVFhZYSkCWyTrjt4bKkMLDZVq-wxk-9QaW9Ht9ToMYyK2OiAsW9Hu92TSrsRKoBO2DN2plgeMaTvVLHVLEi442omOgh6rzuq84BUnePiyy25yvGAMsIxOqcS3rNRvigYMcIfJby6G2XCwkj4I63wO2LsnB9T4YlUJGxgS2cEBXpFQaiWi6nXR-KAEaXlE7AwSIpMMKi01KWxiMWj9Q0op2mU-nOe3HuXqy7M662u5oMaC9fzhXqsgGbWexw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه روغن میخوای، تن ماهی بخر!
🔹
فروش اجباری کالاها از کجا آب می‌خورد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/akhbarefori/652165" target="_blank">📅 21:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652164">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfCeAPXHdNfMiCq_pHmeroG6nbR6BXphjucwdG_MapnmPIwhQRnmIzGdr5fEKopZSHmsXEbVKqKMgwp-qXCjtKkaVjWUwNE4B-h18WYGUAvmq22KNKBZmbreQMv1yy0nMqTQ6Q3tbW-LjGPOdWFyBs6fSPTdX-NO8_gNc6qTbZ50aM1AZSNHogORbyFINPz6b6dtL-eU27VXtBedNYXfvh021hVFxvJHrZf1XT28o7mBnl2NwRvnnuXluLePmRsb2cyGMLtPN6b8i4wPBYP1SlTARp9h6OvJ7SERH_rtN0NPXUVnR7QcLdveXIG9FFVKyHyYKE8ICxnUJccl8E1_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حداقل دستمزد در کشورهای اطراف ایران
🔹
مقایسه حداقل دستمزد ساعتی کشورهای همسایه در سال ۲۰۲۶ نشان می‌دهد ایران با حدود ۰.۴۸ دلار، تنها بالاتر از تاجیکستان قرار دارد.
🔹
در مقابل، حداقل دستمزد ساعتی در عربستان بیش از ۶ دلار ثبت شده؛ یعنی حدود ۱۲ برابر ایران. عمان با نزدیک ۵ دلار و ترکیه با بیش از ۳ دلار، در رتبه‌های بعدی قرار دارند.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/akhbarefori/652164" target="_blank">📅 21:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652163">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3FUh9XrFILx8WDJ_4XFr2GtssUG2TzKi_EOy6SxGF05zDpWs2Ysmc6HcFg99a0uxekc-WseyMRNsT5YkXdM6TVNmS-iJ8HkyYiFdZeqzJHyW0UZ9IH1B-PVkHnm3xM6CjGALtdQALVY5Qm3j_X6D190cDutDX-Qmch09kTTQVPfoCzwKRDc-Vw3FE7HwBwDEApTUVklQY-VEOi7Eo0Hzfruu45YIY655YRYhmYuUjzk4RJ5XV--5Ht7oEgd_YY7MdEKQDmKJwzm4L9ZbsgUHFIpxPJxwskWMl79uAJFMQP6XAj1iUp1kOcddhCT9U3Asc7Tu6rILt4Lsf2fDyo_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تابستان امسال، خانه‌ها بدون خاموشی/ کاهش ۵۰ درصدی قطعی برق کشاورزی و صنعت
🔹
رضایی کوچی، رئیس کمیسیون عمران مجلس در تشریح جزئیات نشست این کمیسیون با حضور نیکزاد نایب رئیس مجلس، وزیر نیرو و معاونان این وزارتخانه گفت: تاکید نمایندگان در این نشست اتخاذ سیاست‌های دقیق برای جلوگیری از قطعی آب و برق است.
🔹
بر اساس برنامه‌ریزی‌ها و توسعه نیروگاه‌های خورشیدی، مقرر شد در تابستان امسال قطعی برق خانگی نداشته باشیم.
🔹
همچنین قطعی برق چاه‌های کشاورزی و صنایع کشور حداکثر معادل پنجاه درصد سال گذشته خواهد بود؛ هرچند هدف‌گذاری ما رسیدن به قطعی صفر است تا امرار معاش کشاورزان و تولید صنایع دچار اختلال نشود.
🔹
در جریان جنگ، برخی از پست‌ها و شبکه‌های برق آسیب دیدند که با تلاش شبانه‌روزی کارشناسان در کوتاه‌ترین زمان ممکن بازسازی شدند، به گونه‌ای که مردم کمبود برق را احساس نکردند. اکنون نیز با رعایت اصول پدافند غیرعامل، شرایطی فراهم شده است که در صورت بروز آسیب مجدد، ترمیم‌ها بلافاصله انجام شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/akhbarefori/652163" target="_blank">📅 20:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652162">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
سفر مخفیانه نتانیاهو به امارات در میانه جنگ ایران
🔹
شبکه ۱۳ تلویزیون رژیم صهیونیستی فاش کرد که بنیامین نتانیاهو نخست‌ وزیر این رژیم اخیراً با محمد بن زاید رئیس امارات دیدار کرده است.
🔹
این شبکه افزود که این دیدار در سایه احتمال ازسرگیری حملات علیه ایران و همچنین در پی حملات صورت‌ گرفته علیه امارات انجام شده و سه مقام ارشد اسرائیلی این خبر را تأیید کرده‌اند.
🔹
دفتر نتانیاهو نیز اعلام کرد که نخست ‌وزیر رژیم صهیونیستی در جریان جنگ علیه ایران، سفری محرمانه به امارات داشته و با محمد بن زاید دیدار کرده است.
🔹
در بیانیه دفتر نتانیاهو آمده است که این سفر به گشایش تاریخی در روابط میان رژیم صهیونیستی و امارات منجر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/akhbarefori/652162" target="_blank">📅 20:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652161">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5GMLfDW5coi9lVn7si-uIKpiNwaMcTzDf0j6Wk23tYclnVTokK0U0bB159egIq13uwHdg-77wAU9_P-zHzXH3ocCO7UwqT7FNuWx04NhQKGTPZGmfeAPL232rhhmNJUhlqibHh7_IQpdh6xdMABuad41pw4AluCkchGdBPmMpm8ry6xX5MYhpuqcN8zB_GPcYIXJyYHgU96qRFzuR8K36j3xKy__wxHzePNrzFCKS0WDVInB1DQzqepl4AKyp8pC-2SlHUrAkvRohRmlvteT5CTHQzcguZj_e15YXdnW_mS5vBSohYVa7ewwr4Qmzoac6vgwTkLNom7cNw-Xb4J5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسقاط خودروهای فرسوده به ۱۱۵ هزار دستگاهی سقوط کرد
🔹
آمار شش ماهه نخست ۱۴۰۴ نشان می‌دهد تنها ۱۱۵ هزار دستگاه خودروی فرسوده اسقاط شده‌اند. این در حالیست که این رقم در مدت مشابه سال قبل ۱۲۱ هزار دستگاه بود.
🔹
طبق قانون برنامه هفتم، ایران باید تا پایان برنامه سالانه ۵۰۰ هزار خودروی فرسوده را از رده خارج کند، یعنی در نیمه اول سال، فقط ۲۳ درصد مسیر سالانه طی شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/akhbarefori/652161" target="_blank">📅 20:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652160">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjtgDxAy7c69aa6RNzWUYgq7iF-fiLASQPjTtIUvAL6iPF3I_O1YGcSVO4yv67NSx8jAwM00bBQ6VyBkhR0dNV4gG_ZX8Aw57-iT5iGBPRxwN3C9oAQwSDo-jyTRGfJPOLFiO3jWA8qOWQCjVJ9eRMiyTWL1nW99gVUTsGLPzMVqV0Pebu5cD7vo1ORmXQGIE3qacXaN5vlDhJa8H99hQ1UFn6of1RY57lS_mMoQFYwUVfKNLq0ojyYC2IjaAvbJ_lZG_eEGeusHeOPD1bFmdxcpDrFPItYS8vhbNQPI9uqamWb6JY-qfD_5hzO64jE-nshikxe3QzfFa1eLrUOufQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم بدرقه ملی‌پوشان رونمایی شد؛
سرود رسمی تیم ملی فوتبال ایران با صدای پرواز همای
سرود رسمی تیم ملی فوتبال ایران  در جام جهانی ۲۰۲۶ با صدای پرواز همای، که به سفارش فدراسیون فوتبال جمهوری اسلامی ایران توسط مرکز هنری رسانه‌ای نهضت تولید شده است، امشب همزمان با مراسم بدرقه ملی‌پوشان فوتبال به رقابت‌های جام جهانی ۲۰۲۶، با حضور گسترده مردم، هواداران فوتبال، هنرمندان و چهره‌های ورزشی در میدان انقلاب تهران رونمایی شد.
این سرود با صدای پرواز همای برای نخستین‌بار در جمع مردم و ملی‌پوشان رونمایی و اجرا شد. همچنین لازم به ذکر است، شعر، آهنگسازی و تنظیم این اثر نیز توسط خواننده کشورمان پرواز همای انجام شده است.</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/akhbarefori/652160" target="_blank">📅 20:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652159">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
مجلس سنا روز چهارشنبه برای هفتمین بار قطعنامه پیشنهادی برای توقف جنگ با ایران را مسدود کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/akhbarefori/652159" target="_blank">📅 20:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652158">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a35ca03f.mp4?token=Gyj8BE7UOUJS91hfcra1VNTUNDyQ2ysiAQLQL7y-cssoLIoi3EBqmveDvjweiRUNsWmh3-du2Fjz-ljQoVsAH7H_I4ATmLg03XEKEexLw1KswhTgelK6GUBJY7MalomifRRmWn8od77nB7fEMyrDRep6syQmwAKEstcD-xwoVLPIdEvNd6Ls20Vz_r--6_IMULwGi8X4sm_Oc1oB35yzznWBzPjHTX4Q00VzI9Zkq_Hm51jbKQGaZ7AlLnjMlSdCpeC-12iuTixEHFiV_hpMt6N5oGCAXwh5ACyileSa6WqHT1snqGRNi6XnevM-kpgYA2flhWxBd47GEfDMgxMIBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a35ca03f.mp4?token=Gyj8BE7UOUJS91hfcra1VNTUNDyQ2ysiAQLQL7y-cssoLIoi3EBqmveDvjweiRUNsWmh3-du2Fjz-ljQoVsAH7H_I4ATmLg03XEKEexLw1KswhTgelK6GUBJY7MalomifRRmWn8od77nB7fEMyrDRep6syQmwAKEstcD-xwoVLPIdEvNd6Ls20Vz_r--6_IMULwGi8X4sm_Oc1oB35yzznWBzPjHTX4Q00VzI9Zkq_Hm51jbKQGaZ7AlLnjMlSdCpeC-12iuTixEHFiV_hpMt6N5oGCAXwh5ACyileSa6WqHT1snqGRNi6XnevM-kpgYA2flhWxBd47GEfDMgxMIBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش متفاوت یک کودک به سوال خبرنگار در محفل یادبود شهدای دانش آموز میناب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/652158" target="_blank">📅 20:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652157">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dea98ae1.mp4?token=MoAk0907aNZAy21wn8gxX0jRyF2eDfL_yQQ1RFG2N5o6BzDnd2c852-UVyc4DN6tjyF9dpQdFHfN5Lv5gDXj5Bm3PgVUC-tgl7yHKkvj78dXhq5iLdX4bmkKNjqCzodsoUlgq_Z3PYc3FWcVQRjedECrKm835TwfuLvPMYuEECEt14hvFVHkevdsO0HURQLyzdnCYAFkmYnP6PadLQX27KzROPqLHoE3gNK3-ts2BsILNClCTesRbGwAqBXEfcW2BuWLcmW4gHHKa8P6B_Rtati0HS7wUUT7nqso33efQQbq9rIEp4G-ggoLd9LPgQGftXDBU_c0vTcFB5ciniq1q7spxbntvDyN1sxz8SvPjxDA9XBX4ByvgmpNONr2M_lY4Y7Vfr0IuTQwh6pKtQiLswFg0rv5Ff6kmrySBYJEYkdNBeG0iCDpoMVFpbII8yy8eQf9Xb0jP0qllbHyxqp4RheciZnwTH5ynC4vKEod6m9q9UIK_74zr93Bh9NqD8CA3juywBSBYW0ULg1nydWru850aBvPvFut1QeF7aWvka2TGICoCHfaeYCM1IUhqyd8_x9zsgfvldYEuBCqiRaccTfWHaHZ_OHqNN-RVlWDCFwnSKGTZ9_fR5ljfyjVOTySXK1W-sWaTumkVJBt9ZgSIIH9Qojb3B1e2GK_J81FZa8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dea98ae1.mp4?token=MoAk0907aNZAy21wn8gxX0jRyF2eDfL_yQQ1RFG2N5o6BzDnd2c852-UVyc4DN6tjyF9dpQdFHfN5Lv5gDXj5Bm3PgVUC-tgl7yHKkvj78dXhq5iLdX4bmkKNjqCzodsoUlgq_Z3PYc3FWcVQRjedECrKm835TwfuLvPMYuEECEt14hvFVHkevdsO0HURQLyzdnCYAFkmYnP6PadLQX27KzROPqLHoE3gNK3-ts2BsILNClCTesRbGwAqBXEfcW2BuWLcmW4gHHKa8P6B_Rtati0HS7wUUT7nqso33efQQbq9rIEp4G-ggoLd9LPgQGftXDBU_c0vTcFB5ciniq1q7spxbntvDyN1sxz8SvPjxDA9XBX4ByvgmpNONr2M_lY4Y7Vfr0IuTQwh6pKtQiLswFg0rv5Ff6kmrySBYJEYkdNBeG0iCDpoMVFpbII8yy8eQf9Xb0jP0qllbHyxqp4RheciZnwTH5ynC4vKEod6m9q9UIK_74zr93Bh9NqD8CA3juywBSBYW0ULg1nydWru850aBvPvFut1QeF7aWvka2TGICoCHfaeYCM1IUhqyd8_x9zsgfvldYEuBCqiRaccTfWHaHZ_OHqNN-RVlWDCFwnSKGTZ9_fR5ljfyjVOTySXK1W-sWaTumkVJBt9ZgSIIH9Qojb3B1e2GK_J81FZa8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم نوشت| ریزپرنده‌های دشمن در این جنگ چگونه از کار انداخته شدند؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/akhbarefori/652157" target="_blank">📅 20:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652156">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123da29c75.mp4?token=RcHhgcdIeeYuvfGOj5OdMLW9rXoFQxDHEqxWCAaBcM7K0k-iL4LIHXGRu3gkHmOt1NYSGrNhPE4TEcQWyGaygVbLLngS2uRcvg0YUmryHGDQI04nyDPZbLh3U4n4bcO8A9_OplhzucTi54eboBUXgWs4NfdgJJyDK1c3kjqn9Wf-YsizZ-NULzdO5oBIj25zQjCDKOdOTjJxTcKNVfjpno0prKMa3R93K530_hzZb6flRXNz3A-eohTjax6dYwLbK7js4PdkYOcdeAGjtpzCxhJlVIny9oajsNj5efX35VbsVXCQ6tWpjw6qAvVwbPRLoM9g-0aAu5EzIXBVGgVysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123da29c75.mp4?token=RcHhgcdIeeYuvfGOj5OdMLW9rXoFQxDHEqxWCAaBcM7K0k-iL4LIHXGRu3gkHmOt1NYSGrNhPE4TEcQWyGaygVbLLngS2uRcvg0YUmryHGDQI04nyDPZbLh3U4n4bcO8A9_OplhzucTi54eboBUXgWs4NfdgJJyDK1c3kjqn9Wf-YsizZ-NULzdO5oBIj25zQjCDKOdOTjJxTcKNVfjpno0prKMa3R93K530_hzZb6flRXNz3A-eohTjax6dYwLbK7js4PdkYOcdeAGjtpzCxhJlVIny9oajsNj5efX35VbsVXCQ6tWpjw6qAvVwbPRLoM9g-0aAu5EzIXBVGgVysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرهای خوش هفته‌ای که گذشت
🔹
در لابه‌لای خبرهای مهم و پر استرس این روزها، این چند خبر حالمان را خوب کرد!
@TV_Fori</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/652156" target="_blank">📅 20:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652155">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxiZjqsScw1YmDPAP_cT3q_yWzI3k6L3tHzUyA883ycZH5U4yrpMkbFlgy9_nkdSnY8Iq4wPMP6cVQ_RQIZQQz2Bmj8yuIyjSzs9HjG7h6zB8zEh_aOMEmp64J_QSeqgI6L9EoBHaDy8no0Oe7ypAxxxdo3i5ld3314ERN3PC_pT8DeJONAlHKNv1VTcfrLbAr6FBSfW7V5JlN-BpRgrO4tBB_3x19Jf8odhC2jEJF0-h8Qxj7spWJTbjG1fehC_inAICOMHW3uqRLL8PfcjrOXrdRq3SMXDKrv11jCoyH4bvppG6F_XDDiUgfFbmIp1Jnc6S37MoQfKuDruHsa0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسیجی جهادگر «محمدامین صابرکار» در بندر دیّر به شهادت رسید
🔹
بسیجی جهادگر محمدامین صابرکار در جریان آموزش‌های دفاعی در بخش بردخون شهرستان دیّر به شهادت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/akhbarefori/652155" target="_blank">📅 20:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652153">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2eQNHBJBaPUbw5vYO8x4b-j32QG0_u0RxxVpOlODo9e7Kk6jlHg4V67BjWjaIALsyG3M08H7V90bpv-Yx0YCFNCXRpZPPGrl5uAS65C7suHnbGbWtx0B3XX0VGuMa0-C90bK7PWu93fpJd8yZatIDERZJqubmV7NXi_p-LQnJVAVirJP3syrOvUWCwgUKVQgnEnSlk0Ytr3Pw5K3Aantm2jbhC9JM09LTbLzTg1UInW0vJTMw-lx-ZbB02HaCqv26sleQlLxwt5pHfGmfJdTUiqHAB1McogDl70zj5bk8VT3oTTPLOOnn3-n-M2-rxZQh_4S2qYFJk9vQXrbifW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراض وزیر خارجه ایران به دستگیری غیرقانونی اتباع ایران در کویت؛ حق پاسخ‌گویی را برای خود محفوظ می‌دانیم
🔹
در تلاشی آشکار برای ایجاد تفرقه و تنش، کویت به‌صورت غیرقانونی به یک شناور ایرانی در خلیج فارس حمله کرده و ۴ تن از اتباع ما را بازداشت کرده است. این اقدام غیرقانونی در نزدیکی جزیره‌ای رخ داده که ایالات متحده از آن برای حمله به ایران استفاده می‌کرد.
🔹
ما خواستار آزادی فوری اتباع خود هستیم و حق پاسخ‌گویی را برای خود محفوظ می‌دانیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/akhbarefori/652153" target="_blank">📅 20:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652152">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggMObWheAnKJdYquAv8K_8oBixmBmgZlfMdBpUvgsDlW7OyhqbcYZGKcDxRUtYOcPnrjqKKnNnOIGbDD1SDbH3O1FxIWqlHWY4dESdwTABFzEscXbtnGTtG2s6gcLeuaA6uCkGG3HWvvwJi5RofRDYF7mU8GmtMQygkVjPwHvqmehQm47-BGkOS0chcp4ZT0qkYOuWIVPWD4INP3xzlVeFNFA6Vjj-0TkM3Rdh2N3S4sutTfDoBHsKqcomQpCVY53q3yPGnN7mUEauLu_NPaauVN_HFOYZ-ZXC0_t9utURJdSrQC8Iyd9gHjD0Q-jN-7MRNnpLP3Wne_WLrXiABEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان استخدام فعالین رسانه‌ای، اقتصادی، سیاسی و فعالین صنفی دانشجویی در ۴ استان
مجموعه خبرفوری بدینوسیله از تمامی فعالین رسانه‌ای استان‌های گلستان، گیلان، خوزستان و اصفهان جهت همکاری دعوت به عمل می‌آورد.
اطلاعات علاقه‌مندانی که سابقه فعالیت رسانه‌ای، سیاسی، اقتصادی یا فعالیت صنفی دانشجویی داشته باشند و در فرم ذیل اطلاعات خود را بارگذاری کنند، توسط واحد نیروی انسانی خبرفوری بررسی می‌شود و برگزیدگان به مصاحبه دعوت خواهند شد.
برای پر کردن فرم کلیک کنید</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/akhbarefori/652152" target="_blank">📅 20:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652151">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ed274467.mp4?token=M7JWCswnfi6n0NMTVgl0gMUGIx7_JFIcZ7T_z2Ryehk8Hbf69oNHVFFOMqWNKTCSud_STs0n1voBW5SEfwIrboQyf5scpsTr955PzAbTtlyI1EIza5UWM_pSxpQnsNDUzmQyc7sEUDZ483Aa0Wnt0sZLoQu9SA9hR1GB96vYgJvl5wysYYGe8WSRGxOBhjInDUuN225ZWYA7YWxvBuk3vTk72aYqVgvbdj4eKCj0S-tG14UWxiJli7mn81hfKc9xE01tb_JwkonYGNR-WAlNXpVA9CAEABZT3huYgn8EQBdUm6Niq2UDdWWyGEEc71JVW-9h_2TPz2r5GU1gWjZDyklw_Q77mcGkIsxINRVbo7TV3Hlnj1yl7WDR1EjO12kSDaifJe5UfkJVVsAd5Hzpsn6d7ZRUY7swVayjXeaPEJkhVyEdwVCocL-_Zjf4Ha8Kag8nrjWP2-L_DCLVmghGaXlwB8kGEs0KoYCI7FNNo-r1yAvGbWgZduRdMOjpiYJMk5XUG1AmLsc2gsBXGEiMHhr2Orp9kVSGvxgO0VDYE9mFMHS2LwPqkol1f8Kw49mURvUo3X4y1fQNgyE0Ff-HHU-f6sRSLFx3PfSdMxjRdzutW49Ls76j9XZNwzSRuAk1d7VDvtdHtLHHyOj53CrXAlrniPwEtUN0CrtvCzLY8zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ed274467.mp4?token=M7JWCswnfi6n0NMTVgl0gMUGIx7_JFIcZ7T_z2Ryehk8Hbf69oNHVFFOMqWNKTCSud_STs0n1voBW5SEfwIrboQyf5scpsTr955PzAbTtlyI1EIza5UWM_pSxpQnsNDUzmQyc7sEUDZ483Aa0Wnt0sZLoQu9SA9hR1GB96vYgJvl5wysYYGe8WSRGxOBhjInDUuN225ZWYA7YWxvBuk3vTk72aYqVgvbdj4eKCj0S-tG14UWxiJli7mn81hfKc9xE01tb_JwkonYGNR-WAlNXpVA9CAEABZT3huYgn8EQBdUm6Niq2UDdWWyGEEc71JVW-9h_2TPz2r5GU1gWjZDyklw_Q77mcGkIsxINRVbo7TV3Hlnj1yl7WDR1EjO12kSDaifJe5UfkJVVsAd5Hzpsn6d7ZRUY7swVayjXeaPEJkhVyEdwVCocL-_Zjf4Ha8Kag8nrjWP2-L_DCLVmghGaXlwB8kGEs0KoYCI7FNNo-r1yAvGbWgZduRdMOjpiYJMk5XUG1AmLsc2gsBXGEiMHhr2Orp9kVSGvxgO0VDYE9mFMHS2LwPqkol1f8Kw49mURvUo3X4y1fQNgyE0Ff-HHU-f6sRSLFx3PfSdMxjRdzutW49Ls76j9XZNwzSRuAk1d7VDvtdHtLHHyOj53CrXAlrniPwEtUN0CrtvCzLY8zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استفاده آمریکا و اسرائیل از یک موشک جدید با ۱۸۰ هزار ترکش برای حمله به یک سالن ورزشی دخترانه در لامرد فارس در ۹ اسفند ماه ۱۴۰۴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/akhbarefori/652151" target="_blank">📅 19:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652150">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
آشنا: تنگۀ هرمز دیگر رهاشدنی نیست و یک وضع واقع پیداکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/652150" target="_blank">📅 19:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652149">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فروش فوری ویلا ساحلی در شمال ( مازندران )
💰
قیمت ۲۰میلیارد اقساطی
🏕️
ویلا مدرن لاکچری
🔥
فول هوشمند ، داخل شهرک
🔥
✅
متراژ زمین ۵۵۰متر
✅
متراژ بنا ۴۰۰ متر تریبلکس
✅
۵ خوابه (مستر)
✅
شهرک با گیت نگهبانی
✅
معاوضه با خودرو ،طلا،دلار و...
✅️
دارای سند تکبرگ
✅️
💰
قیمت ۲۰ ميليارد اقساطی
⭐
اقساط بدون بهره
⭐
- تماس جهت بازدید :
برای قیمت و اطلاعات بیشتر و ارتباط با ما
وارد لینک زیر شوید
👇
👇
🆔
شناسه:
https://ble.ir/vila_aghsat</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/652149" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652148">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSrEDOAjIMI8pb0LAxJdmF1vhOrwcF96YOSCmfx-No14c4KKZ_hh0FDUSNIBa158nRW_nGTd_hgcLcQfHc2MBwcC1IziX0kYoQWBSl5HzE-2H3RxQyB6fmksWKgP-BRqFhqTahCETfDB9k2bR8jwI9e_yakK-Ezhim7lcpOVooSNz_guXvtpaKnKe7YnKbZebvP-AkkjTJuFfRpwGso_UJtiGlrBIy5UtZayv2fdrmjk_Bn32b4e2ADv_Ez8-PG8OUgwD0o91dZu17z9ZARBEh1uDSxJQBAy1hjnvi9H4AYnQdPVi7ZTOgUwU7H9QYUcyzXYLTtweJ_Qo5nR17dWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایتن لوینز، تحلیلگر و روزنامه‌نگار آمریکایی: امارات متحده عربی شروع به نصب تورهای فلزی مخصوص پهپاد در اطراف انبارهای نفت کرده است تا از حملات ایران محافظت کند
🔹
من نمی‌دانستم که پدافند هوایی آمریکا چقدر ضعیف (رقت انگیز) است...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/akhbarefori/652148" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652147">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBu4nc-fovNhUd11FlRo444mxRyxR5saAwcOsjB9tauUpTKmHsQWMCSY6Kqe38bB-7kyptwxqMiMEtELQBGsgOpWuqRxTEUFpeB-V_ONejwLEPKMyjzAkakWw9YqA57SXCn9EbGz3973W0HAWTNHusZFWMNAPJLZp44S-vAwbNnuzImlF4pSD8wmmMxRwstldGiMnNd-ZodNnxrBHgsLZVu714WVk88D7XopZUiVCSSD-kxJzA9tZPv_zCF49LMiw5hso9VczmXn2vlDwFzl7OQ72oMkZ06iNa8b-p7aqPvCBifSox19LsRdHJ6gxPq1G6ewBEPYWtkjzvZJE23VCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر نیرو: تابستان خاموشی نخواهیم داشت
🔹
عباس علی‌آبادی وزیر نیرو: با همکاری مردم و افزایش ظرفیت تولید، وضعیت امسال از سال گذشته به مراتب بهتر خواهد بود و امید است تابستان بدون خاموشی سپری شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/akhbarefori/652147" target="_blank">📅 19:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652146">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-kzTU_WIVwlDeKbqAAFuNSe5K8SRceGp8AXhLWLUkAAhNcXXfS6-pCMCNcL187iF7_v6ZCtkHXqpE5xlB6bRe2tiHu7dIIU_xB3DpR1tL9dkR2TPsknDz2vlX8McKkOrOADQYMjhthNxdhIUAV6ICxNUAQB_7R1jc3TFxRrfwxMckqdDjRfwNuhe1qpk57hFkOTHDnH-ZzxDqUVYUmfWF_T0NSLjnuaK7Oe61BUSvJaHj3fxn5uMaIuEequhZlZOeU3QVAbaZDl6Cb59KoaGqN_7sFeltYDax36X77g5NE-yCBcXH4trSWmSIdN895z1sv4ipO1sMxSCWUnlcDldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احسان تقدسی، روزنامه نگار: ایران همیشه بهشت صورت مسئله پاک کن ها بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/akhbarefori/652146" target="_blank">📅 18:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652145">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 در زمان انتشار اخبار مهم نظامی و درگیری‌ها، کدام شیوه اطلاع‌رسانی برای شما جذاب‌تر و قابل‌اعتمادتر است؟</h4>
<ul>
<li>✓ ترجیح می‌دهم اخبار را به صورت فوری و کوتاه (بدون تایید نهایی) دریافت کنم</li>
<li>✓ ترجیح می‌دهم کمی صبر کنم اما گزارش‌های جامع و تاییدشده را بخوانم</li>
<li>✓ بیشتر به دنبال تحلیل‌ها و چرایی اتفاقات هستم تا خود خبر خام</li>
<li>✓ فقط تیترهای اصلی را می‌خوانم و وارد جزئیات نمی‌شوم</li>
</ul>
</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/akhbarefori/652145" target="_blank">📅 18:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652144">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نزدیک ۴ هزار نفر به خاطر مهریه در زندان هستند
سید اسدالله جولایی، رییس هیئت امنای ستاد دیه کشور در
#گفتگو
با خبرفوری:
🔹
سال گذشته ۱۲ هزار و ۶۹۷ نفر زندانی را که رقم کل بدهی آنها ۴۷ همت بوده است از زندان آزاد کردیم که ۱۲ هزار و ۴۸ نفر از آنها آقا بودند.
🔹
هم اکنون در کل کشور ۲۰ هزار و ۳۶۵ زندانی غیرعمد داریم که از این زندانیان ۱۵۶ نفر بدهکار دیه، ۱۷ هزار و ۳۵۸ نفر محکومان مالی و ۳ هزار و ۸۵۱ نفر زندانیان ناشی از تعهدات مهریه و نفقه هستند.
🔹
مجموعه بدهی همه زندانیان غیرعمد موجود در کل کشور ۲۰۰ همت است.
@TV_Fori</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/akhbarefori/652144" target="_blank">📅 18:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652143">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuQ35caBqywSC2K-mO-hWPJ4wK-gkZqAerqgYbP6y8hiLhBVK-UomxmaalvhE6AB6v1H0sx-z-bwK6O29MAr-nCjaxJxJwS_aBPDmFnJ4U-RgOAy2a0tW6Px-xZdFfP5TDPPKnihzS8DFRb6sbcOh6t6Dfaq_TzWDmPEk8vXMFqbSGMEDHbRcEZLDylqarQDuwX3zNgBjNcdWr_EGvOVIV2kvcqnYKZ4ZCsavxP-1RQMIxjWtE6lurBJ6pr6977KTf3mWPDvx2omMmvBjXz55CFcGreeheFNGwJsCs6Yr1BJFMsWg2lNr8E3MXm6_xHeJpLBr9XmN7BpTZTPsmOVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موجی از زباله، دریایی از درد
🔹
پلاستیک‌ها تجزیه نمی‌شوند، فقط خرد می‌شوند و وارد زنجیره غذایی ما می‌شوند. برای حفظ سلامت دریاها و خودمان، وقت آن است که جدی‌تر با پلاستیک خداحافظی کنیم.
شما هم به کمپین
#نه_به_پلاستیک
بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic
#نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/akhbarefori/652143" target="_blank">📅 18:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652141">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
معاون ارتباطات دفتر رئیس‌جمهور: اینترنت بین‌الملل حتما وصل می‌شود
🔹
محدودیت‌ها ناشی از ملاحظات امنیتی دوران جنگ است.
🔹
دولت قصدی برای دائمی شدن محدودیت‌های اینترنت بین‌الملل ندارد.
🔹
محدودیت‌های ایجادشده ناشی از ملاحظات فنی، امنیتی و نظامی بوده است.
🔹
دسترسی به اینترنت همانند بسیاری از خدمات عمومی، حق طبیعی شهروندان است و دولت نیز قصد سلب این حق را ندارد، اما در شرایط خاص و اضطراری، مسئله امنیت کشور بر بسیاری از حوزه‌های دیگر تقدم پیدا می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/akhbarefori/652141" target="_blank">📅 18:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652140">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZf-Y0Dbl5L-vPwhyrKuqlmenZjoOphdJ8fEl6uW8E0BoOOjLWFiBEQbCsRBHw5DvtOxLQfsDx1BbhZdRBVxJFSXPwJja5GBvet_BZ6UDxqV1FavDlzKXhJhT1YkcyrZOU9JlhhWInLB8HGK3l8RIK1DpPD4xU_c3bpjQhglvRqp2QvaD5FqIKe3oeHPmGUyKyxTb0UKpzdZLBKpAcvkiGmG5OWsHlZFSfAUHaSBLFAqpNwflZBiAxPklFNDziSzg92ravgvxGqUWfIPLc21580xP7vdYR85p68lixiFA3ukuWJ0fiC8lHKzGS8DMzsk5KSeb5LdyO7kFrrYCbE3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهم خودروسازان از ارزش ریالی بازار
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/akhbarefori/652140" target="_blank">📅 18:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652139">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2a897a4f.mp4?token=VKLSJmqidGqfxdGYBWQV6Shz8zm-iFwbZGqRoSzYvrtr06jnjNQ8LcKqc8C-5R08XbehTByKZuUoqXK56Yvo3vIj-b2y0NOL3kX3EHg240kb4axn-RpqW4QZlu0788y74jmjRp1ZhiON6SsSB7R5YX15Kk-nDnngmCS6a-DfArBvHkkEzYcNNmZjqiHv2ek0HR5DS29wLLlwcgHzJwtqzB6s2LXO0MNwDVAzSauLl5QBBhLBmSfrmHLwMRzvQTIPCLI4T4UzpXBQn_P2WnELb7NEfkAlB3YEXi06kqkaZGxCQqszldma6tpGsnyCC77NMNWPLAeJPAkEzXhqWjEufLp9eJqUL-o_dPNuLiBoNulyDXjz3aS6pfTRCmQHd3JTLlQSzI9WP7_1Ilj1xO95bgshaFStwogphm89zxz8MBNaw8WwH7lSmCSwhiqGoI9ENbaUkrLlAlD5x1QJ4I4_s-b6sSR0uYJxLAoYL0mgp90WsVKlzSV6c2b_9imyO8zMwZcPxP7eQI2fjOqMxqrUB73eLVC9C2FYQqcyd9EOkBNHxiugXaZFFzjRPnC4bp8BBOQeFbpxV4N39Zizrd-8_auJtIAkg6oUtQFIFK4Dwiq6dp3DjCzpDdnRMXe8zRn0y0cHUo_F93cX89P3GKVOaVBzq3DkZ5V7E90lI71i5lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2a897a4f.mp4?token=VKLSJmqidGqfxdGYBWQV6Shz8zm-iFwbZGqRoSzYvrtr06jnjNQ8LcKqc8C-5R08XbehTByKZuUoqXK56Yvo3vIj-b2y0NOL3kX3EHg240kb4axn-RpqW4QZlu0788y74jmjRp1ZhiON6SsSB7R5YX15Kk-nDnngmCS6a-DfArBvHkkEzYcNNmZjqiHv2ek0HR5DS29wLLlwcgHzJwtqzB6s2LXO0MNwDVAzSauLl5QBBhLBmSfrmHLwMRzvQTIPCLI4T4UzpXBQn_P2WnELb7NEfkAlB3YEXi06kqkaZGxCQqszldma6tpGsnyCC77NMNWPLAeJPAkEzXhqWjEufLp9eJqUL-o_dPNuLiBoNulyDXjz3aS6pfTRCmQHd3JTLlQSzI9WP7_1Ilj1xO95bgshaFStwogphm89zxz8MBNaw8WwH7lSmCSwhiqGoI9ENbaUkrLlAlD5x1QJ4I4_s-b6sSR0uYJxLAoYL0mgp90WsVKlzSV6c2b_9imyO8zMwZcPxP7eQI2fjOqMxqrUB73eLVC9C2FYQqcyd9EOkBNHxiugXaZFFzjRPnC4bp8BBOQeFbpxV4N39Zizrd-8_auJtIAkg6oUtQFIFK4Dwiq6dp3DjCzpDdnRMXe8zRn0y0cHUo_F93cX89P3GKVOaVBzq3DkZ5V7E90lI71i5lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: بانک مرکزی منابع مالی بازسازی واحدهای آسیب دیده در جنگ تحمیلی سوم را تامین می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/652139" target="_blank">📅 17:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652138">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ec3b0e04.mp4?token=EwPWvuh_eJNkQ8fgOBh3Gdr_zXV2pZcpAkPuAQEPbdE5HDAAqK0iRM_P6w8sy5oeXmohIp0MRhUvLnvDhR-5kmYYDwUxkZsq89F-hlVHzOANq_igM28KdIcWF4PxFwbwM3a21uf4FAyN7ibpGxkRzyOj-qA8O6GPoEKhocG-d2jczw51gbJYRcrdN6emgIW2sZNFR0ejy257hw_zEmIiy5D9_fa80hNW6Jopc2FdMHW5TWPo7u1NDEWmGg3itD9GS_wsoFR8pQA857sT1nvwNwPe_Jt_6kdsZL0sLaeXiP_tjBmjPspbsanrmmVGIJ3h-U4qhtwVQq0hWVY1tey3iDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ec3b0e04.mp4?token=EwPWvuh_eJNkQ8fgOBh3Gdr_zXV2pZcpAkPuAQEPbdE5HDAAqK0iRM_P6w8sy5oeXmohIp0MRhUvLnvDhR-5kmYYDwUxkZsq89F-hlVHzOANq_igM28KdIcWF4PxFwbwM3a21uf4FAyN7ibpGxkRzyOj-qA8O6GPoEKhocG-d2jczw51gbJYRcrdN6emgIW2sZNFR0ejy257hw_zEmIiy5D9_fa80hNW6Jopc2FdMHW5TWPo7u1NDEWmGg3itD9GS_wsoFR8pQA857sT1nvwNwPe_Jt_6kdsZL0sLaeXiP_tjBmjPspbsanrmmVGIJ3h-U4qhtwVQq0hWVY1tey3iDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین  انهدام بالگردهای دشمن توسط رزمندگان سپاه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/akhbarefori/652138" target="_blank">📅 17:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652134">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o76XmQOPALwX11_fOooySlG0sT15jSfmm7J7hrukZtPo0QyYVJelFrn4Rvvmh62ez-QH5HFjNrcnY4LZV_Trxr6Y4M5oXbSCHndMDRtSSmt399Echg86vSJprU0Go7chHdkfEBQQu8kmzRcNubbU9qPW-cQpFYuEkzBhxDVjnuK0YcW02yI3tEhJYWk_YyEDSFGsMK0NuOlH1wP3BmQylZ6a2KBO-lac2t6enlzLa6bOtYRo2RnZ614m_Ez9pvvAbK8RCqUkAj1Cqxo2JpwQrz3WE2a5U8CmsRwvlNhlxISzm5d4j0r7JJAC3KvDzK0wpXGYs3C1722fj-be5N-jVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دعوت از اعراب برای حضور در نشست ناتو با محوریت جنگ ایران
🔹
به گفته منابع آگاه، سازمان پیمان آتلانتیک شمالی (ناتو) قصد دارد از نمایندگان چهار کشور حوزه خلیج فارس برای حضور در نشست آنکارا دعوت کند، نشستی که احتمالاً جنگ ایران و شکاف فراآتلانتیک بر گفتگوهای آن سایه خواهد انداخت.
🔹
بر این اساس،‌ انتظار می‌رود وزرای خارجه کشورهای بحرین، کویت، قطر و امارات متحده عربی به نشست ۷ تا ۸ جولای (دو ماه دیگر) در پایتخت ترکیه دعوت شوند، اگرچه دفتر مطبوعاتی ناتو از اظهارنظر در این باره خودداری کرد.
🔹
این نشست در پی افزایش تنش‌های فراآتلانتیک بر سر جنگ ایران برگزار می‌شود. دونالد ترامپ، رئیس‌جمهور آمریکا، متحدان ناتو را به دلیل عدم کمک برای بازگشایی تنگه هرمز مورد انتقاد قرار داده و متعاقباً از خروج حدود ۵۰۰۰ سرباز از آلمان خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/652134" target="_blank">📅 17:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652132">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e1a3ee0e.mp4?token=mzuUcFhplo7kRaodv_MmsY_OAQnJXKXGwDfF-GiUZ0R5hrTGyF6SZ380kDzVS6AOwy59FVITJurvWVp9LmVL8cOm670w7_VxOb8qaJ8yvt51SzuR3OWtc6nrOoeQ8zWHBL9ZXb9r5xJIcrp-n4MGQwrNJrjHRNSN_nyE1RWjqNvrvqM-2GwzGdkzi0JF7lZ-79Ai0wa-itSbrMxhc-0vNRhArX0qBmEP3Qr6FE2SsTIWffILl5RhasAUyjeqA1u4rwimucjyf23FQt5OGJlxfWK96jqDlt4Gd6yWBvocqEjosVbCQljb0vivjw-hO0pIoPLRpBJYCMi3EGlhL8nX0Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e1a3ee0e.mp4?token=mzuUcFhplo7kRaodv_MmsY_OAQnJXKXGwDfF-GiUZ0R5hrTGyF6SZ380kDzVS6AOwy59FVITJurvWVp9LmVL8cOm670w7_VxOb8qaJ8yvt51SzuR3OWtc6nrOoeQ8zWHBL9ZXb9r5xJIcrp-n4MGQwrNJrjHRNSN_nyE1RWjqNvrvqM-2GwzGdkzi0JF7lZ-79Ai0wa-itSbrMxhc-0vNRhArX0qBmEP3Qr6FE2SsTIWffILl5RhasAUyjeqA1u4rwimucjyf23FQt5OGJlxfWK96jqDlt4Gd6yWBvocqEjosVbCQljb0vivjw-hO0pIoPLRpBJYCMi3EGlhL8nX0Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کولر پوشیدنی رونمایی شد!
🔹
جذاب‌ترین خبرهای حوزه فناوری و تکنولوژی را که با هوش مصنوعی تولید شده را ببینید و بشنوید.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/akhbarefori/652132" target="_blank">📅 17:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652131">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
۷۷ واحد صنعتی اصفهان در جنگ رمضان به صورت کامل تخریب شد
🔹
مدیرکل امور اقتصادی استانداری اصفهان: بر اساس آمارهای دقیق، یک‌هزار و ۴۴۸ واحد صنعتی، صنفی، تولیدی و توزیعی در سطح استان دچار خسارت شده‌اند که از این تعداد، ۷۷ واحد به‌صورت صددرصدی تخریب شده‌اند.
🔹
تاکنون چهار هزار و ۲۷۵ نفر شغل خود را از دست داده‌اند.
🔹
میزان خسارت خوداظهاری‌شده این واحدها نیز بالغ بر ۳۷ همت، معادل ۳۷۰ هزار میلیارد ریال برآورد شده که این رقم، ضرورت مداخله فوری شبکه بانکی را بیش از پیش آشکار می‌کند.
🔹
از این تعداد، ۱۰۶ واحد نیازمند تسهیلات خرد زیر ۱۰۰ میلیارد ریال هستند که با تأمین آن، ۹۲۹ فرصت شغلی احیا خواهد شد.
🔹
همچنین ۲۸ واحد دیگر به نقدینگی بین ۱۰۰ تا ۵۰۰ میلیارد ریال نیاز دارند که بازگشت ۵۰۶ نفر به بازار کار را تضمین می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/652131" target="_blank">📅 16:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652130">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
سخنگوی ارتش: تنگه هرمز تحت کنترل راهبردی نیروهای مسلح ایران است
🔹
دیگر اجازه نخواهیم داد تسلیحات آمریکایی از تنگه هرمز عبور کرده و وارد پایگاه‌های منطقه شود، هر کشوری بخواهد از این آبراه عبور کند، باید تحت نظارت نیروهای مسلح ایران باشد و عبوری بدون ضرر انجام گیرد.
🔹
غرب تنگه در اختیار نیروی دریایی سپاه و شرق آن در کنترل نیروی دریایی ارتش قرار دارد.
🔹
دشمن با وجود برنامه‌ریزی ۲۰ ساله برای حمله به ایران، هرگز پیش‌بینی نمی‌کرد نیروهای مسلح نه تنها توان رزم خود را حفظ کنند، بلکه با شلیک موشک و عملیات زمینی، مانع تحقق اهداف دشمن شوند و این مقاومت، عامل بزرگ پیروزی امروز ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/akhbarefori/652130" target="_blank">📅 16:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652129">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL5hpXIjBxGcOjVpHi-iOWwzL9dacDsnIfSb8McsXD7HARKjuEXclhgN7-Jou6Or7jtDq370c5Z91iwWqbJul1dvcbbBLGRgylyJP-_Hl9zjESyaNPJja_8xn3qwKcdIsflTVpN5D-anwget0lwWxe-5G1bhKqNY71jAViqthK-PeWzLxxo3iws0OONMReRHqGl5K5eKRgNWK5qbZyMuBbBowtB_W5SndCg4mw0iI0-7r0dhITcnlGXFbzjFagHY-hYjtHaURxdW9HtiaswtyMBfulnIuiYNAWwiG56J5QiVutWCX2X7cdA_OferLQ_e5HRbGs4BMfa0BWEIq5GxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حذف ارز ترجیحی بیشتر از جنگ قیمت‌ها را بالا برد
🔹
درحالی‌که بعضاً ادعا می‌شود قیمت مواد خوراکی و اقلام سفره خانوار عمدتاً از زمان شروع جنگ تحمیلی وارد شوک افزایشی شده، اما بررسی آمارها نشان می‌دهد درصد قابل‌توجهی از این افزایش قیمت مربوط به بازه زمانی آذر تا بهمن‌ماه ۱۴۰۴ یعنی دوماهه اول سیاست یکسان‌سازی نرخ ارز و حذف ارز ترجیحی ۲۸۵۰۰ تومان می‌شود.
🔹
بنابراین مرتبط دانستن کل افزایش قیمت‌ها با تغییر سیاست ارزی یعنی یکسان‌سازی نرخ ارز و حذف ارز ترجیحی، نمی‌تواند گویای تمام واقعیت‌ها باشد، همچنین ادعای اینکه کل افزایش قیمت‌ها در این مدت به دلیل شوک ناشی از جنگ بوده نادرست است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/akhbarefori/652129" target="_blank">📅 16:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652128">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
وال استریت ژورنال: حمله به پالایشگاه ایران در جزیره لاوان، کار امارات بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/652128" target="_blank">📅 16:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652127">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ایران یک آژانس جدید به نام اداره تنگه خلیج‌فارس تأسیس کرد
نیویورک تایمز:
🔹
طبق گزارش لویدز لیست اینتلیجنس، که کشتیرانی جهانی را رصد می‌کند، تهران در حال حاضر یک آژانس جدید به نام اداره تنگه خلیج فارس تأسیس کرده است.
🔹
لویدز اعلام کرده، با این کار، ایران «خود را به عنوان تنها مرجع معتبر برای اعطای مجوز به کشتی‌هایی که از تنگه عبور می‌کنند، تثبیت می‌کند».
🔹
این مرجع جدید ایرانی فرم درخواست کشتی‌هایی که به دنبال عبور هستند را برای آن ایمیل کرده است تا ترانزیت را تأیید کرده و از هر کشتی که از تنگه عبور می‌کند، عوارض دریافت کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/akhbarefori/652127" target="_blank">📅 16:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652126">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تب گرانی بی ‌حد و حصر خودرو خوابید؛ افت ۷ درصدی خودروهای داخلی
کرمی، رئیس اتحادیه خودرو در
#گفتگو
با خبرفوری:
🔹
وضعیت بازار خودرو حباب داشت که مجدد مقداری از آن برگشت. فعلا بازار خودرو رکود است و خرید‌وفروش نمی‌شود. اگر همین روال باشد، شاید تا چند روز دیگر قیمت‌‌ها ریزش بیشتری داشته باشد.
🔹
حدودا قیمت خودروهای داخلی ۷ الی ۸ درصد و خودروهای خارجی ۱۰ الی ۱۵ درصد افت‌ قیمت داشته است. درحال حاضر نه خودروهای خارجی و نه داخلی خرید و فروش نمی‌شود.
🔹
ثبت‌نام ماشین از طریق سایت معمولا الکی و بیخودی است و حتی یک ثبت‌نام هم نشده، سایت را الکی باز می‌کنند و می‌گویند ثبت‌نام کنید و مردم را سرکار می‌گذارند.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/akhbarefori/652126" target="_blank">📅 16:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652125">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: طرح مدیریت هوشمند تنگه هرمز در کمیسیون به جمع بندی نهایی رسیده و برای بررسی و تصویب  در سامانه مجلس بارگذاری شده است
🔹
عزیزی:
🔹
سه گانه موشکی، مردم و تنگه هرمز محصول پنجاه سال تلاش آمریکا را بر باد داد.
🔹
پیام حضور و ایستادگی مردم در خیابان ها و میادین ، بخشی از رسالت مبعوث شدن است.
🔹
جمهوری اسلامی ایران با مدیریت هوشمند تنگه هرمز می خواهد از این ظرفیت جغرافیایی به عنوان اهرم قدرت‌ساز استفاده کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/akhbarefori/652125" target="_blank">📅 15:53 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
