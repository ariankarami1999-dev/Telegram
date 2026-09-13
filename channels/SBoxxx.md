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
<img src="https://cdn4.telesco.pe/file/QiFnG7BvGrrczFglE4ZkmaSLhGM3yODwT0iRSN8yYHq9hw4dPMMj03AT24m5rw1AV4bS5tiQX-y0d7TqYT3Dv4wmHLul3L-4Wsfbc2uuOsM92ErUUGqdwXsfbkcy2xIP7GPyvSz6gZk286tYVsRDvIuUgvVo--t9t6cz2HeiSbQQmWQHMYr8eGs8qC-4E3l-ALOTdD_PrPveK1SfyPOGpFqpsQ3XpFOxdObUlSMQ3MJDvdgd0Nv0iFsWseRQsxqACF8UwPOphdRKVJql_L34bl-APoS_ev0as6ONPx38HGAP7uxDBc-zg-9EAbVLZKnfOYFmIfiVzm1iuM1kW1IVvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-20854">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجار در بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/20854" target="_blank">📅 14:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20853">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هم میهن:  ترکیه به جای دلار گاز، غذا و دارو می‌دهد همتی به استانبول رفت  منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد  دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر…</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/20853" target="_blank">📅 14:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20852">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هم میهن:
ترکیه به جای دلار گاز، غذا و دارو می‌دهد
همتی به استانبول رفت
منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد
دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر اساس سازوکار توافق‌شده با آمریکا عمل می‌کند ، عبدالناصر همتی ، رییس کل بانک مرکزی ایران وارد استانبول شد
به گفته شیمشک، مبالغ مربوط به خرید گاز ایران در یک حساب به‌شدت تحت نظارت و تنظیم‌شده نگهداری می‌شود و ایران فقط می‌تواند از این منابع برای خرید اقلام مجاز در چارچوب رژیم تحریم‌ها، از جمله مواد غذایی، دارو و کالاهای مشابه استفاده کند.
سخنان شیمشک فقط درباره پول گاز نیست. این اظهارات نشان می‌دهد که ترکیه در دوره فشار حداکثری جدید آمریکا فعلا حاضر نیست برای حفظ تجارت با ایران، ریسک قرار گرفتن نظام بانکی خود در معرض تحریم‌های ثانویه را بپذیرد</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/20852" target="_blank">📅 14:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20851">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWkkK3tjXNqrEBicd6AWYU1Cg-69_mJRLKM4-yQtsW8eQtCA-oc45GWyuLqRsbd1cOGs1hc61pAHSi7_lvavk5dnyq8wURRiVv3WQjekk4C4OUVxaRIOlr5t2f0veSyaTKJd6_fhEIrQYv0RjWQ41jFx5tj3wduFLelx_bmHehxL6fi3x3Xobdi2jvFwAgsuY_JbD1bj_KRk_MCzD3VHjJo0c1vW5Afu1ykdQjf9OYm-wznz1_DXKBSb_Kxh8ZsO8ULMKqb7s_4Z3wpuE1WA8EGiathyD8fJ7OTCiyCfyowoYtXu3cIwxS381v0sjs69RTzstcOk8rFzMRDR-HxzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشیال تایمز:
حوثی ها با هوش مصنوعی آنتروپیک موشک بالستیک ساخته اند!</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/20851" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20850">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پزشکیان:   نمی‌دانم مشکل آنچه در پاکستان نوشتیم چیست که آمریکا می‌خواهد از نو گفت‌و‌گو کنیم</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/20850" target="_blank">📅 12:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20849">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پزشکیان:
نمی‌دانم مشکل آنچه در پاکستان نوشتیم چیست که آمریکا می‌خواهد از نو گفت‌و‌گو کنیم</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/20849" target="_blank">📅 12:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20848">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خب امروز و بعد از ۹ ماه تارگت ۲۴۰ هزار تومانی دلار محقق شد.  بعید نیست مدتی رنج بشود.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/20848" target="_blank">📅 11:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20847">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">— یک کشتی تجاری ایرانی در نزدیکی جزایر هنگام و قشم مورد حمله قرار گرفت که در نتیجه یک نفر کشته و سه نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/20847" target="_blank">📅 10:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20846">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">احمد اروزان کارشناس ترک:
خلبانان اسراییل برای حمله به ایران در قونیه ترکیه تمرین میکردند!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20846" target="_blank">📅 02:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20845">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">معاون وزیر خارجه یونان:
ترکیه و همه در منطقه می‌دانند که یونان کشوری بسیار قوی است که جایگاه بسیار بزرگی ژئوپلیتیکی، دیپلماتیک و نظامی کسب کرده است.
و من مطمئنم که هیچ‌کس هرگز این قدرت‌های یونان را آزمایش نخواهد کرد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20845" target="_blank">📅 00:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20844">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYRqOREvQwvjXu69T9MTVfg6rO0GjGWNFhGaZQhNKGinZrBK7zxd8UOP9mcvEtGobHLTQFQwzCnBNadjLgJV1nJ5WuNqMBIuUuhwCjafzAnsOfMFGzF8EAwZPVFD6AP_p5jG1KGlpj0Xu4FtL--x4QH35o73v-0T0eFByUFEdUTNrm-NJiYwtAq9H5GdxmW7YWf4uYbomoq-Uur7OhPWQQpGPwLITkgO49ugtyReFUYF_5vLGQ4cBu721-SvvonwNGRHjLCvboxDre7qCGMXYSWm0f0pWV2h0f-nf5qLarMbwsbAAAoQAkg9FXdzjX2-0DmFEmKrMZUYzPsqZdYwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت پیمان مکه!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20844" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20843">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پرتاب موشک از ایران به سمت هرمز</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20843" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20842">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
ایران در حال آماده سازی برای تست سلاح هسته‌ای است</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20842" target="_blank">📅 23:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20841">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtHIRVDOspckQtZxxr6xr8HVZF0QYFB_4FCWayB2wXY9dVfV4fRrdyxBoXeRrHSDa9O-apxlUm76VTW2-mr-kJdP5qJrAD36EWeKT-RJm0UW8C1e1ftL-AgWOLSl3FXJqq7uaFBUXQevObKMQpwJGKe8gD_n7ie6whrqwFI7DKCHNf4pqmP6xbLhYjGs7wjAFlhbmaq3NlE3FfKSoTVMp5Lvp6HGxisNDu0t3FL5QN5u8YxIiVEOzScyNt27Df4P-Z2dAJ-IL-UxLAoDNUTZH5ESu_7BHadTZbxXBKwdFyu8HVcRWju2yV-7jJIOSpTscjac1r7xrLWrbnLa2vRqiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20841" target="_blank">📅 23:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20840">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">توافق ایران و عمان برای تنگه هرمز به معنای باز شدن خودکار تنگه نخواهد بود   منبعی نزدیک به تیم مذاکره‌کننده ایرانی به تسنیم گفت: درک چارچوبی در مورد مسیرهای کشتیرانی «به زودی اعلام خواهد شد»، اما «فقط» بین این دو کشور است و مسیر جنوبی هرمز را بسته نگه می‌دارد.…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20840" target="_blank">📅 23:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20839">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پزشکیان مدعی امضای توافق هرمز با عمان در حضور کشورهای عربی شد  رئیس جمهوری مدعی شد مقام‌های ایران و کشورهای عربی خلیج فارس روز دوشنبه در مسقط توافقی برای ایجاد مسیر کشتیرانی مشترک میان ایران و عمان در تنگه هرمز امضا می‌کنند.  مسعود پزشکیان گفت: «کشورهایی که…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20839" target="_blank">📅 23:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20838">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترور یکی از بسیجیان عشایر منگور
سپاه پاسداران انقلاب اسلامی شهرستان پیرانشهر با انتشار بیانیه‌ای، شهادت حاج اسلام کاک درویشی را تسلیت گفت.  پاسدار پیشکسوت و دلاور عشایر منگور، حاج اسلام کاک درویشی توسط عوامل پلید ضدانقلاب در مقابل منزل خود در روستای کوپر به شهادت رسید.
شهید اسلام کاک‌درویشی از جانبازان سرآمد و از نیروهای مخلص و وفادار به ارزش‌های انقلاب اسلامی بود که سال‌ها در مناطق کردستان و آذربایجان‌غربی مجاهدت کرد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20838" target="_blank">📅 23:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20837">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">معاون رسانه‌ای انصارالله یمن: با هدف‌گیری خطوط‌لوله و پالایشگاه‌های عربستان کار به نفتکش‌های سعودی نمی‌رسد
درصورت تشدید تنش میتوانیم زیرساخت‌های نفتی را هدف قرار دهیم تا اندک صادرات نفت عربستان از کانال سوئز هم قطع شود.
همه چیز ممکن است؛ مگر این‌که محاصره علیه یمن برداشته شود؛ عربستان فعلا درحال لجبازی است.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20837" target="_blank">📅 23:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20836">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تهدید فاکستان به حمله موشکی در صورت دخالت نظامی در یمن</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20836" target="_blank">📅 20:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20835">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پزشکیان مدعی امضای توافق هرمز با عمان در حضور کشورهای عربی شد
رئیس جمهوری مدعی شد مقام‌های ایران و کشورهای عربی خلیج فارس روز دوشنبه در مسقط توافقی برای ایجاد مسیر کشتیرانی مشترک میان ایران و عمان در تنگه هرمز امضا می‌کنند.
مسعود پزشکیان گفت: «کشورهایی که خاکشان از سوی آمریکا برای حمله به ما استفاده شد نیز در این نشست حاضر خواهند بود.»</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20835" target="_blank">📅 20:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20834">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCs7ZZx8mnWD7Wa8LNRh6Mki7Lrqe73Auki8UMWYybVdBjw7n7KDYqNvb6uvRFCxZL1RcSZLhDaxRTOY8JfKOiDAK_WcZ3G9PRmroeI-Mz1BFsekOT7JHDRA9sgcZ5RWZWLjFtJ3wLoGzHHi34pxCEl7j_vwrxjMIAWDxF8Uk8nj5vv1l5aNOqrsBocvY1O_MT1KUQ05e5miT1WH5ehD-S815DjvWi95HiYwUKHc_dyF65yrqdJxSbnU3RRMDGGaHCHPJ_c4Cju6NujW-VESMaO1LAPpEjLvXgD3Jxzjyxf6e5RqujluYiKsqkFG3MOyRWh86dM8MQ33zOCHib8DCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی ان ان:
اوکراین در نبرد با روسیه، فراتر از اروپا، تیم‌های کوچک متخصص پهپاد را به آفریقا و خاورمیانه اعزام می‌کند تا نیروهای محلی را آموزش دهند، از گروه‌های ضد روس حمایت کنند و به منافع روسیه حمله کنند
حدود ۱۵ متخصص اوکراینی در شمال مالی در کنار جبهه آزادی‌بخش آزاواد (FLA) که توسط توآرگ‌ها رهبری می‌شود، فعالیت می‌کنند و به جای درگیری مستقیم در خط مقدم، آموزش پهپاد، اطلاعات و پشتیبانی عملیاتی از راه دور ارائه می‌دهند.
نیروهای اوکراینی همچنین نیروهای چاد، نیجر و بورکینافاسو را آموزش داده‌اند، در حالی که چندین متخصص در سودان نیز عملیات کرده‌اند.
سازمان اطلاعات اوکراین می‌گوید این اعزام‌ها با هدف فشار آوردن به روسیه در خارج از کشور و تبدیل تخصص اوکراین در پهپادها به یک «ابزار سیاست خارجی» انجام شده است.
نیروهای اوکراینی در سال جاری میلادی، هنگام تصرف کیدال توسط شورشیان توآرگ، به آن‌ها کمک کردند؛ جایی که نیروهای شورشی و وابسته به القاعده، نیروهای سپاه آفریقای روسیه را به عقب‌نشینی واداشتند.
نیروهای اوکراینی همکاری خود با توآرگ‌ها را عملیاتی و نه ایدئولوژیک توصیف کردند و یک منبع اطلاعاتی گفت: «وقتی توسط همان احمق‌ها مورد حمله قرار می‌گیرید، تفاوت‌های ایدئولوژیک در پس‌زمینه محو می‌شوند.»
اوکراین همچنین از اواخر سال ۲۰۲۵، اپراتورهای پهپادهای دریایی را در شمال غربی لیبی مستقر نگه داشته است. یک اپراتور گفت که یگان او از پایگاه نظامی بین‌المللی در مصراته برای انجام حملات علیه «ناوگان سایه» روسیه که از تحریم‌ها فرار می‌کند استفاده می‌کند و در عین حال نیروهای محلی را آموزش می‌دهد. یک پهپاد دریایی انفجاری اوکراینی از دست اپراتورهایش خارج شد و در سال جاری میلادی به سمت یونان هدایت شد که باعث اعتراض آتن و عذرخواهی کییف شد.
اوکراین همچنین تیم‌هایی را به حداقل ۵ کشور خاورمیانه اعزام کرد تا در طول جنگ، آموزش سرنگون کردن پهپادهای شاهد ایرانی را ارائه دهند.
مسئولان اوکراین مأموریت‌های خارجی را هم به عنوان راهی برای تضعیف روسیه در هر جایی که فعالیت می‌کند و هم به عنوان فرصتی برای آزمایش فناوری پهپاد اوکراین در شرایط میدان نبرد مختلف، از گرمای شدید و گرد و غبار ساحل در آفریقا تا عملیات دریایی در مدیترانه، معرفی می‌کنند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20834" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20833">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwAb3FJ7tY_QynQjmWN94ncOWRalOLg7h7QiYwafViLp5aAz85rM3P5QJca3TTPOZaUktlFnUHKZfum1MWYJeVt84BEvYyM5NZJJt2k38Ggcl9C15fFuf0EjXmWLJBUXqvV1g9loHdKactUMRDisA-GsnxT4Bxf_YHwGlyytdnA3d3EhldPzc7gztpTNEUVHc9jfPzU6q3A4qpT0abtoYDxICn_9-eEPKvOcyGtHYBMoRAikzuIO5s-4DtY-3gJCvYfPkc4INuDrysBZ1gIDOD8mDFwuOR2OSjZ655RgNQBEufOU8c8FNrWVOQOTRJlv9cu3ZW01TPadwow9GudIpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید فاکستان به حمله موشکی در صورت دخالت نظامی در یمن</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20833" target="_blank">📅 19:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20832">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…  توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20832" target="_blank">📅 17:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20831">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مدتی است به صورت آشکار و بی پرده، صحبت از لزوم ساخت سلاح هسته ای ایران از سوی مقامات کلان جمهوری اسلامی مطرح می‌شود</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20831" target="_blank">📅 15:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20830">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ:   حوثی ها با ما تماس گرفتند و به ما اطمینان دادند که به دنبال درگیری با ما نیستند.   ما با حوثی ها صحبت داشتیم، آن ها تماس گرفتند و به ما گفتند که دنبال درگیری با ما نیستند و نمی خواهند ما به سراغشان برویم. آن ها اجازه می دهند اکثر کشتی ها عبور بکنند…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20830" target="_blank">📅 13:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20829">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ:
حوثی ها با ما تماس گرفتند و به ما اطمینان دادند که به دنبال درگیری با ما نیستند.
ما با حوثی ها صحبت داشتیم، آن ها تماس گرفتند و به ما گفتند که دنبال درگیری با ما نیستند و نمی خواهند ما به سراغشان برویم. آن ها اجازه می دهند اکثر کشتی ها عبور بکنند و فقط با یک کشور (عربستان سعودی) مشکل دارند.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20829" target="_blank">📅 13:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20828">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20828" target="_blank">📅 13:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20827">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a939b42fc.mp4?token=OOIiGlz8KJO5KH9L0U4yUSN_7zS6QQokbSNnMI6b38r4Jowq6rF8UylsYTH6qFRnmDpMtkKVyL9H1Khk0shqFobT-neM1rKVe1bpMNfZ8j-qa9PqTKpIdFmaJr9sI6_XTAwGlbfdBM-lXoPPfudCbjuKt4FfVb5BVZgd4H1N06TWAaub_ivBowwAix8BJaYfNxEul80Ve5hYbCxrsh7eWUlvVIc5atbBj57Ahnaaaar6h86-5PXQNJax6KnUaMZzg-WHU6d2TvRSIkLpi-otKXOAUWf2WVxqV3SEDmH16xxdJ15_VSD8g9CCfkhh6SNz7wTbP8QVWQqpEGwbmTaGhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a939b42fc.mp4?token=OOIiGlz8KJO5KH9L0U4yUSN_7zS6QQokbSNnMI6b38r4Jowq6rF8UylsYTH6qFRnmDpMtkKVyL9H1Khk0shqFobT-neM1rKVe1bpMNfZ8j-qa9PqTKpIdFmaJr9sI6_XTAwGlbfdBM-lXoPPfudCbjuKt4FfVb5BVZgd4H1N06TWAaub_ivBowwAix8BJaYfNxEul80Ve5hYbCxrsh7eWUlvVIc5atbBj57Ahnaaaar6h86-5PXQNJax6KnUaMZzg-WHU6d2TvRSIkLpi-otKXOAUWf2WVxqV3SEDmH16xxdJ15_VSD8g9CCfkhh6SNz7wTbP8QVWQqpEGwbmTaGhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلی دیدنی از پتانسیل صعودی شدید ریال</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20827" target="_blank">📅 13:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20826">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ درباره ایران:   قیمت‌های نفت پس از پایان درگیری سقوط خواهند کرد</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20826" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20825">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ درباره ایران:   همه چیز به‌خوبی حل خواهد شد</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20825" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20824">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ درباره ایران:
همه چیز به‌خوبی حل خواهد شد</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20824" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20823">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده در آستانه گسترش تحریم‌های ثانویه علیه ایران
بر اساس اطلاعاتی که یک منبع آگاه از برنامه‌ها به
رویترز
گفت، انتظار می‌رود وزارت خزانه‌داری ایالات متحده دامنه تحریم‌های ثانویه‌ای که می‌تواند بر شرکت‌ها و کشورهایی که همچنان با ایران تجارت می‌کنند، اعمال کند را گسترش دهد
این منبع گفت که این اقدام به عنوان یک هشدار نهایی به کشورها برای قطع روابط تجاری با ایران انجام می‌شود
انتظار می‌رود اسکات بسنت، وزیر خزانه‌داری ایالات متحده، جزئیات بیشتری از این تدابیر را در یک نشست خبری در ساعت ۱۳:۰۰ به وقت شرقی ایالات متحده (۱۷:۰۰ به وقت گرینویچ) روز دوشنبه اعلام کند.
طبق گفته منبع، بسنت همچنین یک کمپین فشار اقتصادی گسترده‌تر علیه ایران را ترسیم خواهد کرد که او و دونالد ترامپ، رئیس‌جمهور ایالات متحده، آن را «روز D اقتصادی» نامیده‌اند.
این منبع گفت که انتظار می‌رود بسنت روشن کند که کشورها باید بین همسویی با ایالات متحده یا ریسک قطع دسترسی شرکت‌ها و نهادهای بزرگ از سیستم مالی مبتنی بر دلار، انتخاب کنند.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20823" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20822">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20822" target="_blank">📅 11:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20821">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مرزهای بازرگان و بصره بسته شدند.
مرز بصره جوری بسته شده که تیم تاج برای سفر به بصره جهت میزبانی بازی های آسیایی (سبحان الله چرا بازی پرافتخارترین تیم ابرقدرت چهارم جهان باید در بصره باشد اصلا؟!) به مشکل خورده!</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20821" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20820">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKZue3Z6h0IUx1Qxo2GHJlOB4u8zRgao6lX9k8VnEFbGHSUzjRJMUHfv8yoDNjDG-NXFEoTVOik2y0wlD4dJVKdEyOu0TjVqTKKt9ZHkPmNcu1L1V9UYh1LtOCQQV3uw8LPjyKmTD-9-YJM0gcaL5nK4DNMrfRW_nRuPiTzDw_U2SoQKqy0SwGaoAtpYgzN3UFAvIb3Ku2b9wa1TAn2JjwVEEqq3gMWtQBiPFop8ke9OXJY-aX9TdLNfCK8TmnnOFnw6URbhESxfkYUN2IBzvY-aoRM2Zx2V8dbZGGm5XYHRg9kQzggxHufb2Hr_9_sYtg_oFi4R46czGjTK4PLq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…
توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20820" target="_blank">📅 08:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20819">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">— یک مقام اسرائیلی به کانال ۱۲ گفت که کنترل حوثی‌ها بر تنگه باب‌المندب «خطرناک‌تر» از وضعیت فعلی در تنگه هرمز است و به جغرافیای این آبراه اشاره کرد.
کانال شرقی حمل‌ونقل دریایی در نزدیکی جزیره پریم تنها حدود ۳ کیلومتر عرض دارد، به این معنی که کشتی‌ها در محدوده دید مستقیم از مواضع حوثی‌ها عبور خواهند کرد.
«آن‌ها قادر خواهند بود با موشک‌های ضدتانک به هر چیزی که بخواهند شلیک کنند. آن‌ها می‌توانند کشتی‌ها را با چشم خود ببینند. این همان تفاوت است.
در هرمز، ایران به رادار، سیستم‌های نظارتی و موشک‌های ضدکشتی نیاز دارد تا ترافیک دریایی را تهدید کند. اما در باب‌المندب، یک جنگجو با یک موشک ضدتانک ساده در جزیره میون می‌تواند به یک کشتی تانکر شلیک کند که می‌تواند آن را به صورت فیزیکی ببیند،»</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20819" target="_blank">📅 07:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20818">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">— دادستان‌های فدرال آلمان هفت مظنون عضو حماس را متهم کرده‌اند.
به گزارش‌ها، اینها در حال برنامه‌ریزی برای انجام یک حمله مرگبار علیه اهداف اسرائیلی یا یهودی در آلمان یا اتریش بودند.
این توطئه تا ژوئیه ۲۰۲۵ به مرحله عملی رسید و قرار بود در دومین سالگرد حملات حماس به اسرائیل در ۷ اکتبر ۲۰۲۳ انجام شود.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20818" target="_blank">📅 07:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20817">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران
به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.
در این حمله ۳ نظامی آمریکایی کشته و چند نفر زخمی شدند.
آمریکا نام شرکت‌های چینی را اعلام نکرده و چین را مستقیماً به مشارکت در حمله متهم نکرده است. پکن نیز این ادعاها را رد کرده و خواستار ارائه مدارک شده است.
نگرانی اصلی واشنگتن این است که ایران از تصاویر ماهواره‌ای چین برای شناسایی و ردیابی نیروها و شناورهای آمریکایی نیز استفاده کند.
اگر این ادعا درست باشد، همکاری ایران و چین وارد مرحله مهم‌تری شده است: انتقال اطلاعات ماهواره‌ای می‌تواند دقت هدف‌گیری موشک‌ها و پهپادهای ایران را افزایش دهد.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20817" target="_blank">📅 06:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20816">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجار در استان خمیس مشیط عربستان سعودی</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20816" target="_blank">📅 00:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20815">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">باز سعودی ها دستکم کتک خوردن ترک‌ها در سوریه از اسراییل برای بار پنجم را محکوم کردند!  شهناز جوراب که کلا خودش را زده به کوچه علی چپ!   نه حملات یمنی ها به سعودی را محکوم کرد نه حملات اسراییلی ها به ترک‌ها را !  سبحان الله عجب پیمانی شد این پیمان ناتوی اسلامی…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SBoxxx/20815" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20814">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGKezcjwSKasbphH8Fd_yD39xi_2mPf1yBd_rqlfMKRdp_2Fw1rWoFXIfuk7cC_581-oUWd7cERN12BzczQ5QsjlMEHu8MWbvknzMedgYDZzONxLh4ucIACuADTnW_nt5qDD0iwBC0m-P5nszme_P5tUvpvcpFdYA7hALZ2OihnNnTwAX8tIYxiJEK_b5bgmKiIuJ4FAdQbzihFT8nC_elySE1JYa5C0UZn7gUu7JrPwcv4kTSMc5adXV3wEvvsqGDrNdecNdOY4AxjE7ujolrrO9xvdskXczWhYAG4iK9WTqjeNeegLd5Omy0B14fPxWa1EUVGXUFIWPr5M6ygJDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیره انشالله!</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/20814" target="_blank">📅 21:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20813">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">— ۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران ایران یک موشک کروز ضدکشتی به سمت تنگه هرمز شلیک کرد.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20813" target="_blank">📅 20:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20812">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=FR_JFTKpRTXlMF9fmyEz1vinteO9Q6Mf-m4nkQlqolMrAmZnmc-9sxDfF1WRzmvEd1EeZ7_0inG4UQaBkqwhp5sOd-tQqmWa-ce4Hp0Gp-TEAE736pugxC3Lv40M4smQZB4GowDiedTs5c7GzauvSFUThg-Qy-m9EXAt_eRp6kUvM5mYwL23vb4rkevXhXHoqgojBJtvVUNlLVQuJnXtEdDqQKh10Iap8fviKevuhDlMRO9jRslNfqL9Jpimjjop8mtRliRIRk65l5BRZT8E2Y0DMYzCYgAy9Fq36gGsgqFJGSzCfzUS340wO_eiIYX2DURvkTtgy0wmKrVpGom_dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=FR_JFTKpRTXlMF9fmyEz1vinteO9Q6Mf-m4nkQlqolMrAmZnmc-9sxDfF1WRzmvEd1EeZ7_0inG4UQaBkqwhp5sOd-tQqmWa-ce4Hp0Gp-TEAE736pugxC3Lv40M4smQZB4GowDiedTs5c7GzauvSFUThg-Qy-m9EXAt_eRp6kUvM5mYwL23vb4rkevXhXHoqgojBJtvVUNlLVQuJnXtEdDqQKh10Iap8fviKevuhDlMRO9jRslNfqL9Jpimjjop8mtRliRIRk65l5BRZT8E2Y0DMYzCYgAy9Fq36gGsgqFJGSzCfzUS340wO_eiIYX2DURvkTtgy0wmKrVpGom_dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از اولین توزیع قند و شکر کوپنی در دهه ۶۰:
عبدالناصر همتی
، خبرنگار صداوسیما در میانه گفتگو با مردم به مصاحبه شونده می‌گوید:
«اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره!»
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20812" target="_blank">📅 20:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20811">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmSzDwTN8xDoRrsmdkv-BgGDeJnX_3KUIKHPvQfmx5mnxaAzIoQ6Wswfga7sNhAQG9FkUQb-lVthw2U47PNv7jcVpFuewASSuOc1NRzvFsM4UVX-9ovJF-nA5BLTphPT9ZYVe10qZWwT_zLNdglklcEz-UeEEn53tD6-PQQCwNWhPd3rt-5OjJo5xrPJU5j8Ya1MPLPlhGObOzAvq9o0hzmP_BP332We21GBT1NQWMAe16EjOjlSF_ny7Z2uO0Or4_ONA2vNTdr7HQIh2InG9ETNvIHpA3c97Lf7tlSEPHL_LipeKa6gIwX2osM8NAfyNQ2yHHcaP474EonVEdrrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.  نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20811" target="_blank">📅 20:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20810">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مرتضی محمودی نماینده مجلس:
اکنون که قیمت نفت بار دیگر به 110 دلار رسیده از نیروهای امنیتی التماس میکنیم یک مدت کـوتاه هرگـونه وسایل ارتباطی و متصل به اینترنت را از دسترس عـراقچی و همتی و مشاوران و دستیاران پزشکیان و قالیباف‌دور نگهدارند تا قیمت ‌را در این جنگ اقتصادی کاهش ندهند</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20810" target="_blank">📅 18:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20809">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ:
ایران بزرگ‌ترین حامی تروریسم در جهان است</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20809" target="_blank">📅 18:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20808">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFt2Lcqxo0gqK8UHW9QRR_d3sUmK71nE3Y6vuLBg-QXJVDkNnpO4yLEKYBaiprJbOrtksfaa2ct0x8ZQuML8-vkmu3yKTPIC1W5Sh_0vVuUtUxxG5KPw1b7RYNmUmDltZp2UC4RoYAIHp8-NEt3_0Wty_Pcf6_QTLx9yjdtVhN5p7Qb4fGzdR4PwpdB8jCOQmmIEhGKlOReI3oVGhXz3sezYZ6muux9DWgfgs1S7AqwWivbntATVuzfJ8HWlzYT2x7Ir5Ye819NrAn2_blHUNdFkra-zbDZnczfnvakNfiteaGoMayAqDf1niYRsnmA8LzCCjQvGz_R0OoNUv6EX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟
اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از یک درگیری نظامی به یک فشار اقتصادی و مالی گسترده‌تر تبدیل می‌شود.
در این چارچوب، ایران می‌تواند از ناامنی مسیرهای انرژی و افزایش قیمت نفت به‌عنوان اهرم مذاکره استفاده کند؛ هرچند این راهبرد دو لبه است و در صورت تداوم، ممکن است هزینه‌های اقتصادی و سیاسی قابل‌توجهی برای خود ایران نیز ایجاد کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20808" target="_blank">📅 18:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20807">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTFGNn_Vd6tIeAwRN69e1-o0JKtvOod35MGC_0v_Ks-FYquOd8jAKHnarXrTvMUC7G5eAGnEM1xNZ8F85UWDZaYFq2KE4DyHpfr3GV6QSNn0ng3lYJq04kSTLLJcEW5rBI-UU7bIkcg8VMe2qEsEzbmNiNGb49E2nYTjcZgDGuFjIVMrhiYMij9qmE60fNEpxSSL_zlpP_m5HkyUa72mnNXUkaOd0rwwmV299GhMZKchZY_Iud0RK2-dG9RQ51BC08tTW_Q608OHvxaOX0ip6pdkuTBGqOsodERhL_saDkVLTmgK9oCmwb7FTdkYyhM7QoCybqT4p53EWAsDwvrklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس یادگاری روسای کشورهای بریکص</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20807" target="_blank">📅 16:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20806">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.  نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20806" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20805">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:   حکومت ایران در طول جنگ سقوط نخواهد کرد.  مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.  تأکید باید بر این باشد:…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/20805" target="_blank">📅 13:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20804">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 27</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 26
جمعه 11 سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20804" target="_blank">📅 13:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20803">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XngZG0hNnJoD463E1U6WPe-xZSBj7kUBhEjXlAgI_YlccLmad2MRu3-hZPhIm1NeZuctuCpvbRmlpx6-Tf8QB5qZjggNVNhbChYM6EbqZ0eaR2uR5X8vVvC_qAYCQFYdNEFjqnBrsZHb4LLZMn9l09UZ1X3vnr1DRhyP18FODmivLJvwT58tel7DJaeD1LKGND7hOp6CbM2Za4HyKznTZ6vd72-FV1cwCCWVqjVyevSuYW73oCFD7rPYuh-b9G35gPxCVp9j9MVqkdJ-1jEphhGKVaSpP7rWn8fTjB0hVVFowQy-4IZ_mnijf12qtUIQPVBheszZs4d8l0cZoNjzdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار خبری در فایننشال تایمز مبنی بر برنامه ریزی دیدار عراقچی با وزرای خارجه کشورهای عربی خلیج فارس و مذاکره درباره موارد بین ایران و این کشورها قیمت نفت کاهش یافت</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20803" target="_blank">📅 12:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20802">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پس از انتشار خبری در فایننشال تایمز مبنی بر برنامه ریزی دیدار عراقچی با وزرای خارجه کشورهای عربی خلیج فارس و مذاکره درباره موارد بین ایران و این کشورها قیمت نفت کاهش یافت</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20802" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20801">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر مالی فرانسه، لسکیور: هزینه‌های مربوط به بازپرداخت بدهی‌ها در سال جاری، 65 میلیارد یورو پیش‌بینی می‌شود، که این رقم 4.5 میلیارد یورو بیشتر از میزان پیش‌بینی‌شده به دلیل بحران‌های ژئوپلیتیکی است.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20801" target="_blank">📅 12:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزیر مالی فرانسه، لسکیور: هزینه‌های مربوط به بازپرداخت بدهی‌ها در سال جاری، 65 میلیارد یورو پیش‌بینی می‌شود، که این رقم 4.5 میلیارد یورو بیشتر از میزان پیش‌بینی‌شده به دلیل بحران‌های ژئوپلیتیکی است.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20800" target="_blank">📅 12:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an3m1uLrsEIq7uqys8HxKvvZiuKjN-2Bw2kLmMpk8dzC45L5dScFmVMBdXnhleoWFQmpMmR7l3uu1cXMn7U4pOJAyQcvKSGKbYOF-s6gFKLL6cpMIyFl8M9-RNvgV-1lat5CuCiOMIcbv5L2vvLuVvBPZnrrkADC-AzOBp4cBokPDaPKZQTirL1bjZwfAsprps42v4aQLVu-m4MkkoPRkXwYhPGtOVt0llkTbuph7h3kN9AUqh7ZjOcLl2uZoq_CG7reerxKD9NpR8EmIfXUTwmNDNY1qk6BVd1AgPz-JutyxwcvsMxYzB9Ve6HMYflbAvqFDR9AnVgUY1SIgaM_jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.
نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20799" target="_blank">📅 11:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6TW7AkCfx-0EovBb9ULWKjIxR8XqU-bGCOAOFFWL9l2LCx90VWUpb-BFihRdyQzsVUrBxzjtUDnOkO-LxTNglftYdCNJteCBdff_raIhsL_vae7VTQLWeShXTvo3XldB49F3rHMfwBiECtnnlFdy6XuSpphXtC-XRBDp35O7GXW9v6roCrSUZ4dOWCpv__SJ1q4_pE6-falBpGga3W1P1FpdTVIGXt5slJvZ58kEmLrxkqfe3TcIr3opWSbqj8ePwYAaf54tmHF_FvRlc3MEh74hIPT-nfYBUtFX-bWYqxLeytoC_9cp62_sLUpUygJegIs_3QBwZgF6LbJD-Jw_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جهش بهای نفت و تاثیر آن روی تورم تولیدکننده در آمریکا
جهش قیمت انرژی، به‌ویژه نفت، تورم تولیدکننده آمریکا را در اوت بالا برد و
فشارهای قیمتی را دوباره پررنگ کرد.
حالا بازار منتظر CPI است تا مشخص شود این شوک انرژی موقتی است یا می‌تواند مسیر سیاست پولی و قیمت طلا را تغییر دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20798" target="_blank">📅 11:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گویا امروز حوثی ها این خط لوله را هم در 6 نقطه هدف قرار داده اند!  با ادامه این وضعیت یعنی عربستان حتی از مسیرهای جایگزینی که طراحی کرده بود نیز نمی تواند نفت صادر کند!  به نظرم تشدید تنشی بسیار با اهمیت است و از دلایل جهش بی سابقه نفت در روز گذشته</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20797" target="_blank">📅 10:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvFsNyKOt2tXmr9XWtjh8PUMCA8g9nN4AtLfxG234LVhYt7ktIbLUoB-hU0gYeHv1Lw8Mxfe_ATzkwHTGUMNSw8fzgbVB9ujWP8U2vu0h0_Lv9QRuvtfCfa0YClKkhV08gqG_XISUwOP7Ly5NaZhYfbggP25M196BPBov_Mck4oAwzi_aae7UPUP0RhWOIYiUWKP_CsETsemkXKF2MKdQrErdtPH49VPNxeSAD1Q2L7foGrz5y56SKIF3TWP2OcUL0xsnhS9uIhsFw3CIFh_vZr58XZQWIcOrmFKpJqh4javw13vtDuPxKc74PtWZ9LByxqTSQsihqaAXR6RUxD5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای درک حجم و‌ عمق بی لیاقتی و بی عرضگی ارتش پفکی سعودی کافی است به این عکس یادگاری جنگجویان حوثی که پس از تصرف بندر راهبردی مخا گرفته شده نگاه کنید!</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/20796" target="_blank">📅 10:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حقوق ثابت نماینده‌های مجلس ۵۰درصد افزایش یافت و مزایای جانبی نیز افزایش پیدا کرد</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SBoxxx/20795" target="_blank">📅 01:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خط لوله شرق—غرب عربستان به ینبع برای خود سعودیها فعال است و گویا عراقی ها و کویتی ها هم می خواهند یک خط لوله از بصره به این خط متصل کنند</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/20794" target="_blank">📅 00:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20792">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ1YjE3NQVQHc4IWpFmfN4MCTr93pCPMVd1LoQi4LcspevwYCQHbzMDLJ5IxJeiBjHTapC96ZxkQ6XExCjUuE-BvEMF_aQT2Y6_9weYhUlH6v-fQL9qM_unlHd4HOC28l_uq3xdX5xIkn-JICJFJt0o8KSkYuMyoAtH4fGz2a0bQui7fVBGhdL6okLqKUJs9tkO_vVM91Wb2BKuw_RavGH0jVA_Y0Av9qcV4jbJfNSAvNBm1RPBGrKakzasHndA3Ba6CXufPDN9rBg7QNI3mt0d4bj08jk8iSNlPLZr6xylVt7kwRIhj_vrxwckIsn7Z9bAYuA2ikvp12TfKo0BUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.  نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20792" target="_blank">📅 00:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20791">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">علی الطاهر!</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20791" target="_blank">📅 00:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20790">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkm3t0xv1erriKoB-WRSNmoAT_IeGfz3FLfwjWY_5zXPUM6_dd04soeqynYzNLNgOUNxnP-9LAULrL_2D7P4eY7gQ_ayZIAU7gGWMUQCPgOoYh1RqUHmpfRDqp8be_9XewuRIFSMnJbuo4gjriuUfQoY-2VnyFKhEK56gdxhfYk4ABYJGh7YOqb4mnHTkQcwByGJR-jPsAvSqNdebJjL1uIl0QCG-_Ao2-2JtKDrqpJSnbLtA2w5LQHiqHOGBNRBp5Il8Pnrfg_Doqscyu1DcPR1gQwd4rIogpY-HDID0dQb6fUNVP-_NAyOQ9tuYtg5VFYQpqQpmDgu6uQBVHBZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکستن انحصار چین.pdf</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20790" target="_blank">📅 23:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20789">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">شکستن انحصار چین.pdf</div>
  <div class="tg-doc-extra">186.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/20789" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیا چین راه اوپک را می‌رود؟!  در دهه 1970، زمانی که کشورهای اوپک در واکنش به فشارهای ژئوپلیتیکی بر سر حمایت از اسرائیل، تولید و صادرات نفت خود را محدود کردند، کمبود عرضه نفت منجر به فشارهای تورمی شدید در اقتصادهای غربی شد. با این حال، این شوک عرضه، نوآوری…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20789" target="_blank">📅 23:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20788">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3O5LBOmsY085u9E20ELtrjRFkd00yy-wDPiLEi7wY3Bv4qRluF2DnlGLE6OQO1bDg-wMhaVn4-HzAPjoH3Qg9-ruqhLv6ub0I3XkQTdeipYmUeCHNEm7xl70pNRsWxR6Ud832vlRm6auDI8GFxwC761BzYYbBsnIwen8FZfAbQhzq3Ai2EDOx6YdqfjHwKEcjHAGCEmuCKkco4-8zxxMHoRVcAgfJu5YE7DqGJBMMJUrtqBOIkOJYkikUqYzXrlraGKxnvmFXR6CIMIXL5nLlfLvXXrtWOEcUBsiaINGydsRweiRea00wf1CAAk1OtYEpPZOW1swjgpmUMvaDfOQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسراییل کاتز وزیر دفاع اسراییل:  با توجه به دستور نخست‌وزیر و دستورات من، ارتش اسرائیل هم‌اکنون زیرساخت‌های زیرزمینی سازمان تروریستی حزب‌الله را در منطقه "علی طاهر" نابود کرده است و بدین ترتیب، ایجاد منطقه امن در جنوب لبنان تکمیل شده است.  این زیرساخت‌ها،…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20788" target="_blank">📅 22:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20787">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسراییل کاتز وزیر دفاع اسراییل:
با توجه به دستور نخست‌وزیر و دستورات من، ارتش اسرائیل هم‌اکنون زیرساخت‌های زیرزمینی سازمان تروریستی حزب‌الله را در منطقه "علی طاهر" نابود کرده است و بدین ترتیب، ایجاد منطقه امن در جنوب لبنان تکمیل شده است.
این زیرساخت‌ها، یک شبکه تروریستی استراتژیک است که طی دو دهه گذشته، با بودجه و برنامه‌ریزی ایران ساخته شده است. این زیرساخت‌ها و مقرها در منطقه "علی طاهر" قرار داشتند و قرار بود به عنوان پایگاهی برای اشغال جلجول و کنترل و تیراندازی به سمت شهرهای "متولا" و "کریات شمعونه" عمل کنند. نابودی آن‌ها، به معنای تکمیل کنترل عملیاتی در منطقه "علی طاهر" است، هم از سطح زمین و هم از زیر زمین.
نیروهای ارتش اسرائیل برای دفاع از منطقه و جلوگیری از بازگشت دشمن به این منطقه، آماده هستند.
ارتش اسرائیل در این منطقه امن باقی خواهد ماند، به نابودی زیرساخت‌های تروریستی ادامه خواهد داد و از هرگونه تلاش سازمان تروریستی حزب‌الله برای استقرار مجدد و بازسازی توانایی‌های خود، جلوگیری خواهد کرد.
دولت اسرائیل به حفاظت از شهرها و مناطق شمالی از داخل لبنان ادامه خواهد داد و هرگونه تلاش برای آسیب رساندن به شهروندان و نیروهای ما، با قاطعیت پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20787" target="_blank">📅 21:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20786">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وال استریت ژورنال :
ایران در حال ازسرگیری تولید محدود موشک‌های بالستیک در زیرزمین است و پس از آنکه حملات ایالات متحده و اسرائیل به تأسیسات تولیدی آن آسیب رساند و محاصره دریایی واردات سوخت را محدود کرد، در حال مونتاژ سلاح‌ها از قطعات ذخیره‌شده است.
تولید همچنان به‌طور قابل‌توجهی پایین‌تر از سطح پیش از جنگ باقی مانده است، اما تهران هنوز یک زرادخانه قابل‌استفاده از موشک‌ها را در اختیار دارد و در حال ساخت تأسیسات جدید زیرزمینی است که برای محافظت از ظرفیت‌های تولید سلاح در برابر حملات آینده طراحی شده‌اند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20786" target="_blank">📅 21:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20785">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">موج ۳ از ۵ در حال آغاز است.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20785" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20784">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نتانیاهو
:
توانمندی فوری ایران برای تولید بمب هسته‌ای را دو بار نابود کردیم و آن‌ها بار دیگر در حال تلاش هستند.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20784" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20783">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تنها دستاورد موشک پرانی های یمنی ها در دریای سرخ هم بدبخت تر شدن مصر بود و نیز برجسته شدن مسیر جایگزین ترانزیت دریایی از چین به روسیه</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20783" target="_blank">📅 19:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20782">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEJTl3JH6LB4LQLyz7r-X0sBqKKnsjXzZsnhzmkorE2R8lxw4dBfsQwSS_JjOLSn_SpO3IidIMk-09TIEKDV0F4wNHhHEq_lymi72yK_eT-BEZwVJZLcEovR06cskBhHqRWZkYs4ILhhlJB66pWa_hclIuDLtnKf5wH8bMcd7qA9HYQv-M1vZXV0E97tSYB1rG3CEz-7T1mTe_JWqpWhIbn0gv8FLJkhHYepKzxW4g2UV4obdY-hsEoirUK_25DuRPVlmIPoWtvohbWzPKmE10pFbQXs_JjicjaEXIbbvhbtqB15brvkVz-RX39MLI8gOe6LXP5YqogT805DroziIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذباب هم به تصرف حوثی ها درآمد و سلطه شان بر باب المندب تکمیل شد</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20782" target="_blank">📅 18:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20781">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عربستان سعودی به اوپک گزارش داد که تولید نفت این کشور ماه گذشته به دلیل اختلالات ایجاد شده توسط حوثی‌ها به ۶.۲۴ میلیون بشکه در روز کاهش یافته است که پایین‌ترین سطح از سال ۱۹۹۰ است.
احتمالاً این ماه، پس از حملات به جازان و ابها، این رقم حتی کمتر هم خواهد شد.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20781" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20780">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20780" target="_blank">📅 17:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20779">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ذباب هم به تصرف حوثی ها درآمد و سلطه شان بر باب المندب تکمیل شد</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20779" target="_blank">📅 17:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20778">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgsTHJQ8ZARRnB39zN6tUNHMqWuRqcOW65zueps8Rcx183XxtZz1ly3mz1heGsUuOVZ7mAC46YAq-gh0WJcjL3aSwsNT-gE-d4OrgV8Jt356tN86oLRjtqEAjijILuh0J5G06Jf-b0Biy84oUxbe6IlTj6lqQwAu5CrhKoanOmPq1CaExyjE2r36JYJqu3YeRApNvLA8OUeIH_pBHmzoyWb173pYVTgcDanPkKuD4D5vuO-jUsjtSxM-BfkldR4FnG32zZZW1NTdVWtO2_VyrUYChJhqn2PtzIa4DdTF7jpM51BMI6xzeu0hejplnPpPsPQPk8DtTYDAdJ0CBJUYzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به این ترتیب باب المندب هم بسته شد و ۱۲ درصد تجارت جهان زیر ساطور حوثی ها قرار گرفته است!</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/20778" target="_blank">📅 17:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20777">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20777" target="_blank">📅 16:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20776">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اخبار اولیه حاکی از آن است که نیروهای مسلح حوثی(انصارالله) جزیره میون را در قلب تنگه باب‌المندب تصرف کرده‌اند.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20776" target="_blank">📅 16:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20775">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گویا طلا منتظر انتشار خوانش شاخص بود تا ۳۰۰ پیپ بریزد!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20775" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20774">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">در یمن شاهد فروپاشی نیروهای مورد حمایت عربستان هستیم.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20774" target="_blank">📅 15:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20773">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irxD2R8YGGbgrD0Gi68JoLM9ioBh0yXbr-CjaNE5cSdYmVvoz7j6vI-npqJz7MSjmfdjnMYF5OI47GcHVTMMi5tR1JNKBfGeY7hps50FyqTYmL8x-lW3f1HzZPmeyeUovV5Gu6ZdiC0aHi3hGCHuhAibXfsa5Y7pAnahNddekwkGeB_iBnYQAHaFNBXCffOJDHTXoLA7mfnyLW9xJH0_4Ym2SFUyP9RRLvK-CXreIUp9ynN4KOTZvvvKBq4-eS64sZ17h4lyReE8o0mUj9SAPUI1kbQw7w4qAdj-nlB81-HwO5h1PJTqSYlV_oH-qRJ9_-thkppF9fq_PAmjm8sjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزیره زُقَر هم به دست حوثی ها تصرف شد.  این جزیره در مسیر کشتیرانی بین‌المللی در جنوب دریای سرخ قرار دارد.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20773" target="_blank">📅 15:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20772">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.  نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20772" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20771">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20771" target="_blank">📅 14:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20770">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ew3QrnJtaDgYHUjsmTCmd-dkbySXVxTO9eJfccVyvchXcIcgqH0j0v0BpKgtYwyykV4NWrCBs9Y-TVQTAKvyqzw01D-g3huREL-T543Qi211c4TNWMivD9vr7nV2BOoj5B_AmaZiKHf3J9VG6QpTDK7yq56D_fcQ9zchbm1BrPINOzzJ2fhmyziJnnrCiU-_w4sXVvw7mbs31pEOSTcedphbz2Fv866AomEH38GOCaI_Szn1JO49YKa6g_cxtYSuH5eLMhh92xfiAJpL4pl1xr_9BFgDJkwvGkbH7Bwqdq5xlq0VFfNZFRN_o25NeMLXCDEOxH-ZhtVNJOR2lcp07w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 26</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20770" target="_blank">📅 13:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20769">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حوثی‌ها در یک پیشروی ساحلی سریع، حدود ۲۶۰۰ کیلومتر مربع از قلمرو در غرب یمن را به دست گرفته‌اند.  این پیشروی به سمت استان‌های غربی تعز و جنوبی الحدیده هدف داشت و گزارش‌ها حاکی از آن است که نیروهای دولتی یمن با حمایت عربستان سعودی در سراسر یک جبهه گسترده به…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20769" target="_blank">📅 13:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20768">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 26</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20768" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 25
پنجشنبه 10 سپتامبر  2026</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20768" target="_blank">📅 13:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20767">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بلومبرگ به نقل از منبع ایرانی:
ایران تا زمانی که اطمینان پیدا نکنند آمریکا در آینده برای حمله مجدد بیش از حد محتاط خواهد بود، جنگ را ادامه می‌دهد
دولت ترامپ تنها به تهدید و تشدید تنش پاسخ می‌دهد
تهران آماده ورود به جنگی شدیدتر است و اگر واشنگتن به تجاوزات خود ادامه دهد، حملات متقابل خود را تشدید خواهد کرد</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20767" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20766">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRj5H9KsR_6JNZo1wXY9Go-pschrDlOSkz8m3bjcajZcYlv-UcmSD78FjRdqxLLkVy-K-wzQipjwS5-BvGFuhTuqV1mnwysj-MwCDrztNKbWr_CIs9tV06onHAbGqWdIFowyQGo1YawGfMSBvNQkPeEsgpg3sDN04VNvnHOKBlmUbTHw3d7CtoEd0ev5hsHp4GMlT2XeiXGii5xU94U70g_I9sy-q_1RHS1Xa2BbtIUU_puYSGAnFQJeu77U34HE76cl0A-k974PgYHGOfa5nyxVO4xTgAUn77nI8qZLCAiIcLOsG6bSbZERO9co4XeSW1WdBP3lGHfc8xbTWHpiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20766" target="_blank">📅 12:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20765">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">راستی فرهنگستان برای shemale هیچ برابر پارسی پیشنهاد نداده یک چند میلیاردی بدهیم شارژ بشود استاد؟</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20765" target="_blank">📅 12:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20764">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دارم حداد عادل را با شلوارک و پیراهن هاوایی و کلاه در پاتایا تصور میکنم!  اصلا آدم یک جوری می‌شود!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20764" target="_blank">📅 12:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20763">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWJaR5wn3wzQYYlj7SpWk9m2L4NnPGO7Rfbvz5ZIrYsVSOCIaF4b-RNrcS4rbfIREdjODP8sS_9f1N4YBzN8JoSv8Mcc3AxH7wDNEOIi_1K7oCu9k1YbQH-wNG_x6PoLNZteX9DDKAHe0_yMbhFZD3fBkAHyB4k4XD23qf8eq9MAz8PWUJJSa7fNsC32U8Y1VFwWu3ypcf2sVG_GgL3FbHkpqWdZJKxKCquZmkPZYXO7lja3iEGKIUgfk9fYEBaWWIqh_gmR5gqgkGY_Q3g7ko-Om3iQ_wInUMdN4pYAoH1SCjCN3uR3j3xErF8X1dNnYWO87UtjTmbXJaI6MCxwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آیا انتظارهای تورمی واقعاً اهمیت دارند؟
انتظارهای تورمی زمانی بر اقتصاد اثر واقعی می‌گذارند که مصرف‌کنندگان، شرکت‌ها یا سرمایه‌گذاران بر اساس آن‌ها رفتار خود را تغییر دهند؛ از افزایش دستمزد و قیمت‌ها گرفته تا تغییر در سرمایه‌گذاری.
بنابراین صرفِ افزایش نگرانی درباره تورم کافی نیست و سیاست‌گذاران باید در کنار انتظارات، عوامل بنیادی مانند عرضه و تقاضا، هزینه تولید و قدرت خرید را نیز در نظر بگیرند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20763" target="_blank">📅 12:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20762">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پس مشخص است سفرهایی با اهداف خاص هم داشته اید کلک ها!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20762" target="_blank">📅 12:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20761">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نیکزاد و حداد عادل از مشاوران قالیباف:  وضعیت برهنگی در جامعه طوری‌شده که در برخی سفرها دچار تردید می‌شویم آیا مقصد پرواز همان‌ جایی است که اعلام شده یا خیر  با اینکه میدانیم به دلیل شرایط جنگ فعلا نمیتوان آن‌طور که باید وارد جبهه حجاب شد اما از محسن رضایی…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20761" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20760">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیکزاد و حداد عادل از مشاوران قالیباف:
وضعیت برهنگی در جامعه طوری‌شده که در برخی سفرها دچار تردید می‌شویم آیا مقصد پرواز همان‌ جایی است که اعلام شده یا خیر
با اینکه میدانیم به دلیل شرایط جنگ فعلا نمیتوان آن‌طور که باید وارد جبهه حجاب شد اما از محسن رضایی انتظار داریم که قانون حجاب را تعیین تکلیف کند</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20760" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20759">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2oDCL8rIN8h03UMqljJiohhJCUo7jdX-7xIXXu1-XBUJaa9H209FP7NAXoOBGj6NyWa10BQ72xt16E_KL0nbNuqlR0uln5jjznpSSkcI0VgBeOxOhqzZzRlyv7mSJD-NPH1aV7hcBRVj6XWdXUFecAqMqhWL2g1OOpzU8oeSLfdH25ZWEAsmkiDv6h3xIc728b5J4gLWJecLfN_PtWFLgh3dHIoXnlHaYqXT89tH5i8scBWlnGD32yk-pUxv5SimJIsCHfr9bZd-pgQACc1FdjyOSeg9JhW3b44XvY5gRiY8bg-h4STGEUwi_BBsE4kelP33uIYxlVaCKO-WoaeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.
نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20759" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20758">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ درباره نظارت نیروی فضایی آمریکا بر کوه کلنگ:   «به لطف نیروی فضایی آمریکا، ما می‌توانیم همه‌چیز را ببینیم. حتی می‌توانیم نوشته روی لباس آنها را ببینیم؛ محمد الفیاض، ؛ هیچ وقت محمد جونز نیست مثلا؛ محمد العزوری.  می‌توانیم آن را از فضا بخوانیم؛ باور می‌کنید؟…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20758" target="_blank">📅 11:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20757">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J51Rwb-PA2kt4xQjvY2atItvZw-ycJU52v07tA8m-Nsi_qLX5W7Cur_G8eqRrLLVQg9tbiOP9ULJVvnoQRzi1oamrqDPEs43Gw6juZsCoqfbJ74bSWpPL_I2s96KSCB0gNJrCbqc9E6RlwyrO7zG4ktZM3YcVSZFGBgWltDcDC1SE9xVXOY3qbn4nYz6LRPJZtjefoWs_dvdOw3TFNk4SPrDKCfDgPt03R4ZESIF19JiGjisF8qD07AfY0RAyEyndnYU9ztGWPzADF83EAE-LfBA3CxnhKKhMsrOyEsEvFBtEVN7KQS61wr6Z636Bc6nlW9Cis4Tjk4Sz8hlSMlshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهر بندری راهبردی «مخا» هم توسط انصارالله تصرف شد</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20757" target="_blank">📅 11:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20756">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شهر حیس در یمن به تصرف نیروهای انصارالله (حوثی ها) درآمد</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20756" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20755">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ: «ما همه کارهایی که در ایران انجام می‌دهند را می‌بینیم.آن‌ها حتی نمی‌توانند بدون دیدن ما به دستشویی بروند»</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20755" target="_blank">📅 10:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20754">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شبکه سی‌بی‌اس گزارش داد در پی حمله موشکی ایران به پایگاه هوایی «موافق‌السلطی» در اردن، چند فروند هواپیمای نظامی آمریکا آسیب دیدند که یک فروند A-10 یک بال خود را از دست داد و حدود ۸ فروند جنگنده F-15 نیز دچار خسارت شدند.
بر اساس ادعای سی‌بی‌اس، نیروهای آمریکایی مستقر در اردن برای مقابله با حملات موشکی ایران مجبور شده‌اند، بیش از ۳۰ فروند موشک پاتریوت شلیک کنند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20754" target="_blank">📅 10:25 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
