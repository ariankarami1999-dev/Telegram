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
<img src="https://cdn4.telesco.pe/file/AvrEjUeEN7UKx-Z8EXsbu19WRRQNzjKnDdbOFgqU2wW8lZr0xK40GN5WpoNyivhGzCf2mOEKD3wS-6aryX9L1x12rvLUT27xTsv2U_xxeaUSpzD5u0ZFEMxcAvpeRgcdP4uo76HwVd8NaO4LmlIeIbq9QP6rS_O_oUE2pQyWwTOpVcgwtm2qn_WFdLNBJbq0GzDk9iNK-MwORn2NxYuT0QvgQZ9k2eg5UQxaB8cD_7nxdkoGiPMRNKdGyzy9GMIQG0xUNlX1sxDjmW6MoOqMy6IXuyJyT0NrYzpE2ITHok2a9apZAzUePf6tOIuFvV43IbAbpzIbg1ZYa4TcWIZk1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 908K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 10:21:56</div>
<hr>

<div class="tg-post" id="msg-123859">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQS6Fc3AA2PUC-wdBcKgv-36jXiLw-h-KZBBTyYTtKW8kGrIoZk0rDZd-tqerW3bSWOjodBRemdFY0EC4cp837MWkstMGSZxqN4kMEgpHATMrHhEIUkUw8RIrzwlIUEAp7ESHnVGyrf5VIjnhX2V7BwRjWqou483zcZ0P7Jb4ifWJPhLccNHzv1aS-DhchQJUnpUjGAkDCWjsrSOfp-8dp3SzG6mN6sm8j95EgJvbr2b2_q7uV3_3tvEFB5377oy_bvr-HJt7H2SB4SOfJ9vWzSrdiixDY9yPnbXP-1LZEhYkDxRKR_PAnG1b7MZNg8Oiwpq4HIf-E0AsZbqnAxh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تلاش است جنگ ایران را تقریباً تمام شده و کاملاً موفق نشان دهد، اما روایت او با واقعیت همخوانی ندارد و پس از سال‌ها تحمیل نسخه خود از وقایع، اکنون با بحرانی مواجه است که با داستانش در تضاد است، طبق گزارش نیویورک تایمز.
🔴
در بهترین حالت، تغییر رهبری رخ داده است، اما ارائه آن به عنوان یک تغییر مثبت توسط طرفداران جنگ نادرست است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/alonews/123859" target="_blank">📅 10:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123858">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
آکسیوس به نقل از منابع: درخواست های اخیر ترامپ جرقه دور جدیدی از رفت و آمد بین واشنگتن و تهران را زده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123858" target="_blank">📅 09:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123857">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
یکی از مقامات کاخ سفید، به آکسیوس:  آماده ایم یک هفته یا بیشتر منتظر بمانیم تا اطمینان حاصل کنیم که رئیس جمهور به خواسته های خود از ایران می رسد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/123857" target="_blank">📅 09:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123856">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
یکی از مقامات کاخ سفید، به آکسیوس:
آماده ایم یک هفته یا بیشتر منتظر بمانیم تا اطمینان حاصل کنیم که رئیس جمهور به خواسته های خود از ایران می رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123856" target="_blank">📅 09:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123855">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAGLiiYeyuZVmVSU_bOdIDlrRsxlzgybhmudsVi_5Xak_hUHMFy2MUcv5CaKUqnJ5FoL8nUbSrquVId9TzayjUNbCpnnT8PjMLarXA4Ry0sm5FXzp4ctErv6Rvh-sicdM-6zdUNhKkiTlgo41T1C7kN_fcpT_vKimiRpD6VybK82i8Jehv0OUejvAWAHxViTD_s5_UctIPaXFqGR1BhOUQXDuytYcEkI5Tfpc5a1kFJdIv_pOE-O5bk69Fqmjnm2o1wPO7yuS_85RLyx9zojwpRBgd7bvYJJQBx4oDGojcOtqfvO7SbhjyhXSmc-pjkWVIGbzbBbt4FTkedFEIal4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس برای دومین روز متوالی سبزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/123855" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123854">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs4JsOhn1cbgDX8TgwYne0hzuqntgNt3r-PnQVg-cCGpZcUX61EsmCOZQQSwZFeM4laloE66LKkRuowauhiQ9Oh146kBmltOC-ZunodQX01fNI60x5dUDzwXwXkfitgfm9f8iVavo79CnvVIsutAr4k4YxNTxvcZ095QaMMs9eCfWqiVkki-5UV07pRmDmXV6uqUJ9oQUGKcZAZZdbQUpF3GX03N7fVTxEsFv7UwwVi06UhOyfuJZ6SjGdjfjbaQ5RbYfK7QoeDGN0jaFwIZeIpzmOuEslcKpn09_VnjtQSqnyw8kHROz8iDd5d6BO8I2Z6T1s_vn0bJN5O6pBi9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در Truth Social:  «دارید گیج می‌شوید»
🔴
دونالد ترامپ در پیامی کوتاه در شبکه اجتماعی Truth Social نوشت:
«You’re getting discombobulated»
که میتوان آن را به «دارید گیج و سردرگم میشوید» ترجمه کرد.
🔴
ترامپ توضیح بیشتری درباره مخاطب یا منظور این پیام ارائه نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/123854" target="_blank">📅 09:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123853">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
روزنامه جمهوری اسلامی: دستور پزشکیان برای بازگرداندن اینترنت بین‌الملل کاملاً مطابق با قانون اساسی است / فروش اینترنت پرو هیچ توجیه قابل قبولی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/123853" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123852">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
جزئیات ثبت‌نام دانش‌آموزان در مدارس سراسر کشور
🔴
پایۀ اول ابتدایی: اول خرداد تا ۱۰ تیر
🔴
پایۀ هفتم: اول تیر تا ۷ تیر
🔴
پیش‌ثبت‌نام مدارس شاهد:
🔴
پایۀ هفتم: اول تیر تا ۲۰ تیر
🔴
پایۀ دهم: ۲۵ تیر تا ۱۵ مرداد
🔴
ثبت‌نام پایۀ دهم (عادی): اولویت الف ۲۷ تیر تا ۱۰ مرداد، اولویت ب ۱۱ مرداد تا ۳۱ شهریور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/123852" target="_blank">📅 09:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123851">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUJF8gBH9aAWASY8Rr3U8iEq-UPeVBryhrMSQJZxYIHm4zwMeZ2-fg8gkOhy_cZM9pOjCchLam4YfE0bEOYWg9Xc29sWQ0gtrxnM5zX55p_7ITg0mEfXILmAS5TMuEw_A06Oy_t8YyINmusIftFAOpk4EY_O3mnoJvJ4e0SuK33bsKYB_69W3w6RSUCHG8Ic3iRoBJC7aqD-YZrHTubMpmKi03lO_-73OadO3RGd-4C3GdiQDkJfjAaEjizMn3VVGZA4VeCiF79k48ARS7xOGPQaW2jmh4qQLUO6XoPdNCVtwBl3JqbXKuQ2O5864wuALtEvW3lDdlNiuE53vbhXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه‌های هواشناسی تا پایان هفته برای شمال‌غرب، شمال، و شمال شرق کشور ادامه بارش‌های بهاری را پیش‌بینی کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/123851" target="_blank">📅 09:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123850">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
اسرائیل هیوم: ایالات متحده به نفتکش‌ها و کشتی‌های حمل گاز مایع قطر اجازه داده است پس از پرداخت پول به ایران، تنگه هرمز را ترک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/123850" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123849">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
روابط عمومی سپاه: : رهگیری و انهدام یک فروند پهپاد MQ1
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/123849" target="_blank">📅 09:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123848">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ در گفتگو با فاکس نیوز: ما به یک توافق بسیار خوب با ایران نزدیک شده‌ایم. اگر این توافق برای ما عادلانه نباشد، دوباره به وزارت جنگ متوسل خواهیم شد.
🔴
گزینه دیپلماتیک را ترجیح می‌دهم، زیرا امضای توافق به معنای بازگشایی فوری تنگه هرمز به روی کشتیرانی است.
🔴
تنها تضمین اصلی و اساسی که بر آن پافشاری می‌کنم، جلوگیری از در اختیار داشتن سلاح هسته‌ای توسط ایران است.
🔴
ایرانی‌ها در عمل قبول کرده‌اند که سلاح هسته‌ای تولید یا خریداری نکنند.
🔴
ایرانی‌ها مذاکره‌کنندگان بسیار باتجربه‌ای هستند و این موضوع زمان می‌برد، اما من عجله ندارم.
🔴
تنگه هرمز باید فوراً و بدون عوارض عبور باز شود و باید به طور قطعی از در اختیار گرفتن هرگونه سلاح هسته‌ای توسط تهران جلوگیری شود.
🔴
نیروهای ما به محض بازگشایی تنگه هرمز و پایان یافتن رسیدگی به پرونده هسته‌ای، از منطقه خارج خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/123848" target="_blank">📅 08:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123847">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ شرایط چارچوب پیشنهادی برای پایان دادن به جنگ با ایران را سخت‌تر کرده و پیشنهاد اصلاح‌شده را برای بررسی به تهران بازگردانده است.
🔴
مقامات گفتند که شرایط به‌روزشده تا حدی ناشی از نگرانی‌های ترامپ درباره بندهای مربوط به آزادسازی دارایی‌های ایران بوده است.
🔴
ترامپ همچنین از طولانی شدن زمان پاسخ ایران به پیشنهادات آمریکا ناامید شده است.
🔴
چارچوب سخت‌تر اصلاح‌شده ممکن است به منظور فشار آوردن به ایران برای پذیرش سریع توافق باشد.
🔴
در حال حاضر مشخص نیست چه تغییرات دقیقی در متن توافق ایجاد شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123847" target="_blank">📅 08:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123846">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
العربی الجدید: همکاری نظامی بین مسکو و کابل؛ روسیه از طالبان در زمینه سیستم‌های دفاع هوایی و سلاح‌ها پشتیبانی می‌کند
🔴
در جریان درگیری اخیر، ضعف اصلی طالبان، فقدان ابزار لازم برای بازدارندگی نیروی هوایی پاکستان بود که مسکو برای پر کردن این خلأ حیاتی وارد عمل شد
🔴
پاکستان انتظار نداشت مسکو اقدامی انجام دهد که مغایر با منافع اسلام‌آباد تلقی شود، اما این اتفاق افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/123846" target="_blank">📅 08:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123845">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ادعای اکسیوس: ترامپ چند اصلاحیه جدید به توافق به دست آمده اضافه کرد
🔴
ترامپ در جلسه روز جمعه، خواستار چندین اصلاحیه در توافقی شد که فرستادگانش با همتایان ایرانی خود به آن دست یافته بودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/123845" target="_blank">📅 08:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123844">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6XG423WQsbs-vHMX6wCwMTVL3pn811Lb57-umHVrpXOJevqi0x7XpbsUuxStgBafgNNceNxdaIjPrKFMNQd-ZChhaWF0lYgSt9PQhvJGBqZELvFvJ2ZLhRYLW2i7_sCl87AmZQqETpjAxoJgDx5vlioQWkepQ1fHCYl32lmz282nQEr8DiaErdtJRg5iCsUh4Qn8uk5j2OWEcMVojtUzGSzWyHt5ckCh-l9Cbow1iYWJ3_ZHmdoOWMn-6yPbaSp5zyrnS-hF-CcVPmSsptuZPVjzoKqAFTBp2mW6tJkk8XY8mr5DWOVUiAFVwwdLWXTsJyST1gDdPUICGeent7uwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:
مطمئنم آمریکا بازم به ما حمله میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/alonews/123844" target="_blank">📅 07:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123843">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f990f36121.mp4?token=Hzpa0ZE9MDR_ZqU-A6qNunwI1_yUx9i5LXfXYfZaydSSSn6wY-VCXLo2aLMCvokRioiJJ3NVbaoq2gbwPHZXKS4drVbc0caTGUFSY5oCTlHBZLt37ZVqryLOeDfkbiNbEiHzHuqkzxABAr6_rMgFiLv_4UJ43Tri4cD5MXcFkPELPFR7QHfmospfifiGesn4bymKlMu66t9X1nCmXPnVXg7H1sQVorPLDqpTp_s79oh_njL9vUKN787oUzVx5X1Z7PXeJVTcC5lDDIQ0j0Fll6jataskgdQYHOng04fySClKI_LAExiBHve8ijToKkmZuIeyfvNj7qdOK7IuI_TEZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f990f36121.mp4?token=Hzpa0ZE9MDR_ZqU-A6qNunwI1_yUx9i5LXfXYfZaydSSSn6wY-VCXLo2aLMCvokRioiJJ3NVbaoq2gbwPHZXKS4drVbc0caTGUFSY5oCTlHBZLt37ZVqryLOeDfkbiNbEiHzHuqkzxABAr6_rMgFiLv_4UJ43Tri4cD5MXcFkPELPFR7QHfmospfifiGesn4bymKlMu66t9X1nCmXPnVXg7H1sQVorPLDqpTp_s79oh_njL9vUKN787oUzVx5X1Z7PXeJVTcC5lDDIQ0j0Fll6jataskgdQYHOng04fySClKI_LAExiBHve8ijToKkmZuIeyfvNj7qdOK7IuI_TEZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوریا زراعتی مجری اینترنشنال: اپوزیسیون ما رویا فروشی میکنه و وعده هاش دروغ بود
🔴
ما به کسی مثل جولانی نیاز داریم نه رهبران فعلی اپوزیسیون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123843" target="_blank">📅 07:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123842">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ifk8ZdESzLu2A1IDJWn8GgxHD7jRaW4dKbzYj2085FWxgHLlsv0Y8aug05VFzMgCKdfAhfoQ1JPztsUZFym1FXu-ChdOBo2jblEF-_FviFB8N_OhcqKiOnArM5xBzEi-v4vq74c1Pn8dEdlkd27Rmt4veEldm24TjgDyZ-dp0rZ4iVMIDIcAFI9d9jPqt1WlN8wvMlaOxT21xBmJy_-JUWMgKVprgzyZfJec-1eXFGtoD4hhgM17dyCLv6o-tYJ1o7np9GZ8rkFYu78rVHe7umwAEfOTrA47dphsuQ1mThrgKot-uGZWK4rgBEY4o1hoU_bUMc3mcNI95cLD22OcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/123842" target="_blank">📅 01:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123841">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS5o2S54tZH8WovvN66N5ykGbIJGfaORAU9V9h8iTQqrBzyf2_hT77U8d-AdohRQ788MA0YjKGLcYcROcZGIEq5U2gafyBYyXNJgAr86VHLcVGcJPX9yFkTAfgRIGKPWm5WLs75svLEsPT1Pj7592pXWQ8NGj7Ogq4wpZ3dBcycm6-4wIBcuo-csC5ifpiyL5pYbA_a6Egoe1ARrjBQdZYVwPFgl3hEr-ZpBDl72GlRmdWmp6oqg-7CRaHjNwz0ml0N-r12C2aIjZNF33P8cqlI6Bc2YFuuFTXUoVWCWj_mHYluirLhbZdHAdU-E_Fe-BEBCupzMSK6DgIcmCEUQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/123841" target="_blank">📅 01:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123837">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lepcHbcUjQV2HqYzVp6244I2eeY7gQDGwydn0W-UcyuVW31wvis1i_khbgaPyu9Lt5FCcisrpjb_cDwc3XBUe7JOKfMk4MMtHkF9tJqObOPINWU8tlIEgfQKGpjAQIObyIMQi3-nwu_SZfqWz3IJCqjzZWrsTzRc3IxDtcvi8yv2KDFl4WmZucEbhRVr3d-G7hgh7lWIMF6VvzKR9tWcnc9NQwAFBnY1uiti28C8W0p-WU-PRUNOuXA3n8Vy7JjVkRT5JKtV-mCI_sXJQDsD1LuZ-wEr-bL3z-QYYTU_FVpiAZpqV3Z3KcDZ8fc3ea4a8SIovyacoqxdDgVtYNjXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTGwytZPK3qFsGyqEbITT2978zaYg-rXQ5irKUBtIBIHr_wEismpQhEIl2LVUPSYu8SCibxy7uW3frcrgjJptuZkYFpdi1ANKOtS9A5BVXG-_DURmQOtejb2Ocx9mHbZDlbSSL68cG7EkM_OCfXjnofNOSvEz0_w9lu1kwacSbdzwuaADDvvAGBDPugpzSYevz2jjvZPTsEQY75Z-9_1o8zP_SgfU5Wi-hqksbNj1AQAcVD_adsSqlrhpL0mCE4uaOAVPh0j5CVbZ2crpgVTHhIi94ID_5MP8sWGD0GL5bImQR_4nvpYycv7jPbLemdBGpt05vg8PgKm1pfcMuDOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uf6yKb1W-diEGNqFZp2r53t8qwAWfuf-i4eXXAn26YVNxIhNw7jV8hn5Hz9FOsIpJaLv0hx6_JnvSM0RRQCYuGS1eGpQeOCdioQJZvzMgvvHR68yAj0jRXilD1SiDlWQneTNsCj7QGd1vl8PzduvFXvBeI4bKAhYbIv6abOMsFOXNtYkimIrcg_lcxU6bYSAOEWiGa7e7-tZZ5n0kHhdeM3pePndUPBC3b7OG5sWLFXVG9D4FD9onN_8vDs29V7yKVomg2Y7MB3DOtENSoSy5SLOFDFCTwcNRfhblK_4KNIj8BZnB9w7mvTHSMiUsv_I9GX1S5kS5pXmqJd37imdcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ss3kZ5KDH1D5zC_GbF5J2J5PoRa60qLfZtaqGj6GXyl0Mw6U5WgxSbdPIf30lWFv5-8gYoGLVm5zL_ijjGIEDso8wKNTqKxElZ34-geQyrbpd05OsvJ7OKpnDRtFw3ZF3K10LXo98B-HQOc1OKtkrxRSErYClhfsCXvcf2KvIFRAGZM7MrH2HNqFKud4GPBxBz5iiSZFmDdzoct_CL7vN1Pf0s7ImBmK6M_EsD3k_99Lz_-5woqesHt0BFrdux31IWWLINScGY0rHHZUTKc6_xy_2yfEykbIZxPyJdJCMbvJ4WYEZ0cecn0HA1y4VYeTT-a1zNf9h9edLTrgP2OgOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ بازهم رگباری پست گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/123837" target="_blank">📅 01:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123836">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1def876b8.mp4?token=FDMjpzKNunQFYZPhjKEYLeLVMkrgC7hMpl25diCseMj0jF8mKmoI6ZOEqUSuQVg4uSlUb7E4k95_oMUAw18cMrUrTwrhMhc2SvH29W9ekTwWYdWbk29GwtOEb5HEdUdlSAwlTvEbF1rDX0j30nLnZMR0wOFZA48zkEWOr4P_wsnGdiaEgVQ08hfkjjuc2_ISpyW-luyAqQeSSaljXSavsB5qe8Xklx5qGtPeo7feJVjKAFzh7S9iTIpkUH9p1IzMsTwdflkvht7DvYaRWMyuM-kmMsFvpcusm2TLMLkxHKzEykU2zLDDiWjeC5VY4hnyUzL7Oq6bhLmO9MsydMeYpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1def876b8.mp4?token=FDMjpzKNunQFYZPhjKEYLeLVMkrgC7hMpl25diCseMj0jF8mKmoI6ZOEqUSuQVg4uSlUb7E4k95_oMUAw18cMrUrTwrhMhc2SvH29W9ekTwWYdWbk29GwtOEb5HEdUdlSAwlTvEbF1rDX0j30nLnZMR0wOFZA48zkEWOr4P_wsnGdiaEgVQ08hfkjjuc2_ISpyW-luyAqQeSSaljXSavsB5qe8Xklx5qGtPeo7feJVjKAFzh7S9iTIpkUH9p1IzMsTwdflkvht7DvYaRWMyuM-kmMsFvpcusm2TLMLkxHKzEykU2zLDDiWjeC5VY4hnyUzL7Oq6bhLmO9MsydMeYpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تبلیغ چادر پلنگی در ایتا و روبیکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/123836" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123835">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAkh1HZlOo_MLw39XWlIBdyrJUSWnYB7QVjgBPLgWGTttsWf3Xw-_D4wFF-d761_AwlMfaVXNjWpd834cHmQEEmsFd2gxLjSgDKCdN9-WSutvC0DpbJ4EyaFU5L7BheNLyohzsyaxRH6ErCDBUcHul5wjL_9E_jR4d3NnP3hJ905weOP5t_6GR1b_wTfCtga_E_AiUAwYp6KQqZo9NJND7BUR2W0euBW50ATCgMB4nUFCHczBFiSWxqiQo1RnsSGjIgsvdHU6FPPlxwjanflMSZnqJXAS7pBxgjq3Q0GAolga4P2IeDdG_q0VJglpyGC-skAyxFDpI5b7usuhOUung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تابش فرابنفش
🔴
این هفته شاخص فرابنفش بالا است، تا جای ممکن در ساعات میانی روز(ساعات۹-۱۵، با توجه به داده‌ها) کمتر در برابر تابش مستقیم خورشید قرار بگیرید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/123835" target="_blank">📅 01:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123834">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1s1JaMNF6xsmarGKKDfCR1EwIIWV99_ywlo_EgaFeWW0Wo1RO5S6iwyDNbgFBho6_jJWtOuG8AXqsVvXJAeGpagTELppGVglx5Wz2JPFiKwaAe__Kt0NUjNJ81EGkpErQV4WCjaZn6JTDkbK2lZjpJArt91uwTiLPJ20bFnjQi2y29hGEcRdnParSEZ8nlJJ3kIxJj0J1SE-Vvy_HKyr9G8A0iyrY1MKwsVQt945uCX_X2k4F5MdnK6wToAkN9OPIuG3uAquywRvv3ZWWwQdto9WLfgAAwRXOTAUORH7V7ejlYRas1r3LpLvJ5Zp0rZioZKSMq7mDKm4mGo6KKjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب الله: یه تانک اسرائیلی رو زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/123834" target="_blank">📅 01:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123833">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=Tf76oSPYuon8Lrje9JDmnDRtI6rIXb25HXWKOr2OdJe-SKwkl7_5ZNf5eaHbnuN5yotv8apj31ZmxaQ2U_xi2fgQ3-EKhJEAwTMAEOkw_DYYlU73xPAwDI1K-aSm649Hf9WmJcogJIorrnXiwVGZIDPZPF_JdBHzM3LFZOBFrgjHPKPi-sfHW1j9LltE4mTx0675cUpEtOdtW0kxLen8KQp27sltB5hVy4-wdkIoTsnEZKjr14EPY6Lwvqr_jbOIiCQ-s-KOEOcTgWxPtGNvfrHoYdX0RXOxvV0sALliwkzEf2y8YIJSyXYBdUAEkVlx_jdAkdUyklw0_1AHzLD8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=Tf76oSPYuon8Lrje9JDmnDRtI6rIXb25HXWKOr2OdJe-SKwkl7_5ZNf5eaHbnuN5yotv8apj31ZmxaQ2U_xi2fgQ3-EKhJEAwTMAEOkw_DYYlU73xPAwDI1K-aSm649Hf9WmJcogJIorrnXiwVGZIDPZPF_JdBHzM3LFZOBFrgjHPKPi-sfHW1j9LltE4mTx0675cUpEtOdtW0kxLen8KQp27sltB5hVy4-wdkIoTsnEZKjr14EPY6Lwvqr_jbOIiCQ-s-KOEOcTgWxPtGNvfrHoYdX0RXOxvV0sALliwkzEf2y8YIJSyXYBdUAEkVlx_jdAkdUyklw0_1AHzLD8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت های امشب عادل فردوسی‌پور در آپارات اسپورت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/123833" target="_blank">📅 00:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123832">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نیروی هوایی ایالات متحده آمریکا برنامه دارد در قالب بودجه سال مالی ۲۰۲۷، تعداد ۱۵ فروند هواپیمای سوخت‌رسان KC-۴۶A Pegasus را به ارزش ۳.۵۲ میلیارد دلار خریداری کند
🔴
با تحویل این ۱۵ فروند تعداد کل سوخت رسان‌های پگاسوس تحویلی به نیروی هوایی آمریکا به ۱۲۰ فروند می‌رسد و برنامه نهایی تحویل +۱۷۹ فروند است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/123832" target="_blank">📅 00:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123831">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqwnvD8A9T1qnNKWqH4wEdIMK6CuWDsk23NUKvrTg9tSV0_0RH1DDz5mB-yDR8po0iB-uQc-l3Pu5bIiF6DRjL05ZpuLQO8-ada70tQwPVfs-jG9jE55MCYC-g-GO5zsjivcQ5vOiTmRHjO4nfgiKOHxpL39s4vaZD-ZwYqiWNrxZiUrKJJwMM4LKDOYMO88UeGo5hwnpDh9Gb4U_sQukRimmhI_9jgMWFzeUj_esu2dPOzzZCppTef1G6q9r45zaHaz_b0MrWi7q0kUIP-CwlTMG3Y_H6NQKAkDqJ9vy28siUYrnDVxP3YM4i8yJvkvy0jYW4VDmh0uwJw_4ZpTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :
- یکی باید به پاپ بگه شهردار شیکاگو به درد نمی‌خوره، و ایران هم نباید بمب هسته‌ای داشته باشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/123831" target="_blank">📅 00:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123830">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30f8f1e279.mp4?token=RYezsZKYeY5isiGz30V3oY-N-sCGjcBWesHeKFeW7KRZe1FF2raTIHEnmjkcJuiCHN3IKILBDwrcNwAj1Y7FW8D-pPN8JvUULxvet2ny7ousVWIvertgOtqzCJ48N6Rjy48T4FtK3mi1IrERkpSyQTkQ3i8xSv_nLwxWZzpJHRv6f2eo6DzWM06ltqXD7nNmV7qAH6jk4uG4HcWNtuHNVZALHNcbY4kzqd876mGUIPdpG4dNHmJ8REmWGbKXg3gdQrspazMos7r_mi38DvV3fFxcAFgkiQKYLrjyNYLwykyb5zZDR1x9pMnPrXOnxHpXEc5uEm0aowUvi3vGSrECZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30f8f1e279.mp4?token=RYezsZKYeY5isiGz30V3oY-N-sCGjcBWesHeKFeW7KRZe1FF2raTIHEnmjkcJuiCHN3IKILBDwrcNwAj1Y7FW8D-pPN8JvUULxvet2ny7ousVWIvertgOtqzCJ48N6Rjy48T4FtK3mi1IrERkpSyQTkQ3i8xSv_nLwxWZzpJHRv6f2eo6DzWM06ltqXD7nNmV7qAH6jk4uG4HcWNtuHNVZALHNcbY4kzqd876mGUIPdpG4dNHmJ8REmWGbKXg3gdQrspazMos7r_mi38DvV3fFxcAFgkiQKYLrjyNYLwykyb5zZDR1x9pMnPrXOnxHpXEc5uEm0aowUvi3vGSrECZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کنایه مجری تلویزیون به تاخیر ۹ روزه در انتشار آمار تورم توسط مرکز آمار: اعداد را اعلام کنید یا نکنید مردم تورم را لمس می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/123830" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123828">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgWw7HvlskBioyIOEY1wuEMujs-hopR9moUmWBcPM0VVlfrUjNCwdw0ko59Td-KCHFYRFUhyEmAYrlTguvj4uBBYKYTz5jqchz1Ntk5096bQ9lvt05AAT0H87Op8UFhpvpC5zNAkU2qVmxVAPzhj1jJbeej1wPQ7J5qY-Eyk7cOG8Dkeo4813vaBOh3dQomN2MJLzt8Z_PQ07C-ULERQ8hm_HQKUE2MLFZdvJq6Tsia6IWv27P6050FTukEXaktSVQ9A3rNueKwqJG0-Wye7yd114E-3-Zh2uCIjpAsJ5KeQeBTblMx6IF-s9OGUq8OWJKjDo1TYLCLqQuByKQ1-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwuEjm2Mo3_wXAQZAJ6iQ7q6lWjwkUdRXst2EBLawxT3NeyGxvLPHI2fEBehHvfBP-khhBYne26upbeZyz8ioAwmp17mE3PDEvcSPAjy8Z9d-LcRuqVpdV5OZMIPThRNqb1PlXt9uOCqGwHwP80GsN-xoGG-sIIGk8hfU0fA4VTXr-9zvym10o2mUE41Q8KgKMSwh3iiLesNb-5xNWl1NKW63E2KGH0lgIAIiIvZh6exbHwNAcE42odEE7kj2p1r5RleBiDsyHZc6gqh7KNcf3FEJnFsmUg3JsuPTMEUzCZ_eOEqh5LNytWIKlFv9-qLIuTxXYBG4Yy9LH1MJXv8vQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل بر کفرجوز و شوکین در جنوب لبنان انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/123828" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123827">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مدارس شمال اسرائیل فردا تعطیل اند و بنظر می‌رسد اسرائیل خودش را برای موج جدید و مرگبارتری از درگیری با حزب‌الله آماده می‌کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/123827" target="_blank">📅 00:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123826">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
به حداقل ۵ جهت به سمت فضای هوایی اوکراین، پهپادهای روسی Geran-2 پرتاب شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/123826" target="_blank">📅 23:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123825">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAc6wWM_i6X8GdsCl-5FNTlBT2DPKTFzD5R9tg0O2aoUGHUT61C5kEdoeFZQUfzs2pRkCgAhG59rb_yAXCHqwG-VrIdtlXpjbJeONvj34U1LkJpdWUvexQX_kRf6rV0coAtek9qX_21TvkNfVVLDc1nHRvf1PrP5VUhSPkq04LYLJZGzIjND7bK_rEsny3RBK9lwtrn27HAjDkgBFC0sBpNs2ZUKdBO896tn9rKWn8SM_yhIzrlItIUneYx8hxu7CTqgNqwDyL09adJjQO7JVOjsxD0k1xnMxf7cxAKaAOvHqUbyVejqUhSY2DTGkj5fL5M6Y8LAy3LpNpgVixZhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری جدید و پربازدید از دونالد ترامپ درحال عزیمت به زمین گلف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/123825" target="_blank">📅 23:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123824">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کابینه جنگ اسرائیل در ساعت ۲۲:۳۰ (به وقت محلی) تشکیل جلسه خواهد داد. در حال حاضر ارزیابی وضعیت در دفتر نخست‌وزیر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/123824" target="_blank">📅 23:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123823">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
معاون سیاسی سپاه: ایران بر تنگه هرمز مسلط شده و پس از ۵۰۰ سال، به موقعیتی دست یافته که حق مسلم مردم ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/123823" target="_blank">📅 23:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123822">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: میدان و دیپلماسی دوشادوش هم آماده برای هر وضعیتی
🔴
سخنگوی ارتش: امروز دیپلماسی و میدان نزدیک‌تر و هماهنگ‌تر از هر زمانی در مسیر تحقق منافع و عزت ملی کشور می‌کوشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/123822" target="_blank">📅 23:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123820">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI6QdrB8QuDB0MtApR_BEHLkQDq8z2B3QzTGiNAm4ETMol54CG0tR_jzZB4IxFImJSqK-E_LvZJl3g3Mm9AA0wV601cdP7mZJF8vxwHamdDBal6NFViEV4Hxcp8jH7GhTn_3W1vP0hcnQlb4OOrTAU16-oGxPRUQe4gHM79qxleLPSOjkmjDPeQaTsyV5PDMASTQKNmrkVfh1eKNjq6YHZ2-YNFGUtWZMwvpnN0qOkIVm7DR7gN-CeR-_amymTE57Z8prIXxdHGK2Ci2W3mK9mxSADhoQRvufxkZQh2v_z53lcBKw7AKCzq2bQpxivODm4JSIrLxlHY2tKIXf_eQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7752c409d.mp4?token=vZ-oCzoySIgfmB7eqw1SldTBidF5Nsa5u8zBZD2Hm3U3QG6Ux3sBnvuypM_FEEzz5fiRM5XqbL1647XUsJOJmJm5HG1llYQ-8UhVT6IcGxUT8n8jM3DzaIkUzP_Q3zNYxcn-MH83xHEM6zdQZDprqWExDNm9E1GfJsK3r-SUDeK7iwRgUAX_NfH7M1_YKzxhaorME-26ALm8Keg1jfy5sVupvjG8MoMIfR2hhpAgXGlSLszTy_QEvDkkdCSOqQIELtiINOexdEe20L0O38km9iMOU5wUaaZlcZjzNCh2-KHVXXOwhOsMsvNXh1_5t2xCGjLqTqR7SvWZm-TWA5R0Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7752c409d.mp4?token=vZ-oCzoySIgfmB7eqw1SldTBidF5Nsa5u8zBZD2Hm3U3QG6Ux3sBnvuypM_FEEzz5fiRM5XqbL1647XUsJOJmJm5HG1llYQ-8UhVT6IcGxUT8n8jM3DzaIkUzP_Q3zNYxcn-MH83xHEM6zdQZDprqWExDNm9E1GfJsK3r-SUDeK7iwRgUAX_NfH7M1_YKzxhaorME-26ALm8Keg1jfy5sVupvjG8MoMIfR2hhpAgXGlSLszTy_QEvDkkdCSOqQIELtiINOexdEe20L0O38km9iMOU5wUaaZlcZjzNCh2-KHVXXOwhOsMsvNXh1_5t2xCGjLqTqR7SvWZm-TWA5R0Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز یه مین دریایی ایرانی نزدیک سواحل عمان تو تنگه هرمز پیدا شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/123820" target="_blank">📅 23:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123819">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی:
پیشرفت‌هایی در مذاکرات وجود دارد و ما این را انکار نمی‌کنیم، اما باید مراقب باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/123819" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123818">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktvMgtqnKhagdb8ZP6YfNzugM92aJIJs9vUfUAbFQiNodkqnefZHZ2DlgqbjA2EvKdNVscQyZcdPqkqqMpv4MS4VwVXhsva0EUF-4nLa0bAx-Lrk9OAD9oi9-ObPAkx0Dc4ap1Bmo4VLVA9hmSm-n_Prddu8veZLUMh_F41PqC4qS4rRKn6ncKR16PT0gKD7q2Yni37EsyT1qac1CzHH8e3XYpwXdxI-aqIFnNv4rbDR1sq1FR3dU9KgGXN4LIHVCQvjYaLCiD7PDeZFyogH3hSZmoZxANniWbeVebTWtvpMnWxnSoDmQvo9QlCDDFxlf-5QKkQ0Ieir3ZkxoFqB_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال
:
موزه ریاست جمهوری اوباما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/123818" target="_blank">📅 23:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123817">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a49146ae6.mp4?token=h_6RUURP4nuh1xgGqAo3aKCmWe_TzT73mlVCUvf21aPO6z-W3849kxykGhU3zK6WgT3V77djuVRW1SxODlwnan3Pbz9iInqidyjbruF9ch512m0t7d9t6ptL5Yk_q-_iYJGsoTb7VT8jxL-jIBgxOuVS4f8DiLZc8kUI5CibJnqL59epW8BrOOvklqGai_6CCTJbV3mMEhwntrMoBCwpQmIZYIZQ9F4n0GdiQny06GspkLr7e4bcobT7Hi5XhzxuGM5dFJslsAeX-K8tRpKzNmmiSa_4-Fw8-ih3j7TnZAg8vfFdaL8SEumC9xg46uLbUJZUEudV8NxbGpmoc3qJoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a49146ae6.mp4?token=h_6RUURP4nuh1xgGqAo3aKCmWe_TzT73mlVCUvf21aPO6z-W3849kxykGhU3zK6WgT3V77djuVRW1SxODlwnan3Pbz9iInqidyjbruF9ch512m0t7d9t6ptL5Yk_q-_iYJGsoTb7VT8jxL-jIBgxOuVS4f8DiLZc8kUI5CibJnqL59epW8BrOOvklqGai_6CCTJbV3mMEhwntrMoBCwpQmIZYIZQ9F4n0GdiQny06GspkLr7e4bcobT7Hi5XhzxuGM5dFJslsAeX-K8tRpKzNmmiSa_4-Fw8-ih3j7TnZAg8vfFdaL8SEumC9xg46uLbUJZUEudV8NxbGpmoc3qJoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام حديثه اكبرزاده ، 18 دی در فرديس كرج با شليک مستقیم گلوله به سينه‌اش آسمانی شد.
🤔
عرزشی حرام زاده این دختر ایرانی تروریست بود؟ ظلم پایدار نیست به وقتش سر عزیزان شما هم میاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/123817" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123816">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1e62f376.mp4?token=DXa-yJFUK4_7ztbed-1mIrdpfH_6Dpl3hs1_PuU0fcFvKqdpBxH8HRSRr9bsj2eBlsoHbltvI84A-DOWt13hRZ0-XXlIJfE5nuO2DJMGktraDFLxhAWlbBT37XPvJOjIywKcrvwxkbHh5NneosqUrfu1J_OtPfn7mqn8DoOARTGDB63qrHBfBvxe3FlNZG8LtP9GOwJ-ECazhQy3RFZ647o-nE6B6TwdQxjqJ0kK6-jbWpMMVS4NfEOj_31FUxfGebSH4iVv4yMs3Qq3E4otzxYLQr2iNid-cO5dXbR8R78yXgXEhnc3U7sdqnaZRW_-9Cjqy1YVOcDX9RjKsBfWKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1e62f376.mp4?token=DXa-yJFUK4_7ztbed-1mIrdpfH_6Dpl3hs1_PuU0fcFvKqdpBxH8HRSRr9bsj2eBlsoHbltvI84A-DOWt13hRZ0-XXlIJfE5nuO2DJMGktraDFLxhAWlbBT37XPvJOjIywKcrvwxkbHh5NneosqUrfu1J_OtPfn7mqn8DoOARTGDB63qrHBfBvxe3FlNZG8LtP9GOwJ-ECazhQy3RFZ647o-nE6B6TwdQxjqJ0kK6-jbWpMMVS4NfEOj_31FUxfGebSH4iVv4yMs3Qq3E4otzxYLQr2iNid-cO5dXbR8R78yXgXEhnc3U7sdqnaZRW_-9Cjqy1YVOcDX9RjKsBfWKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت ملی اسرائیل:
«باید بیروت را صاف کنیم!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/123816" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123815">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: محاصره دریایی یا با زور یا با مذاکره پایان خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/123815" target="_blank">📅 23:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123814">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی: محاصره دریایی یا با زور یا با مذاکره پایان خواهد یافت</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/123814" target="_blank">📅 23:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123813">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ارتش: هرگونه تعرض به خاک کشور پاسخ محکم‌تر از گذشته را دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/123813" target="_blank">📅 23:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123812">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خبرنگار الحدث: درگیری‌های شدید بین حزب‌الله و نیروهای اسرائیلی در داخل شهرک دبین در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/123812" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123811">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c0b1479d.mp4?token=jAFbdFQkz1rK-dtoMcxHgIjYiPKOWbV5hcqfoB5lchbIv2H-ahnkw6To2_DqBBRoGtEnHFrfrnSEy1FmhUvgHOfZl5B6HIHn4BuLW_AOl5-QWIvgx5VL1kKXvllA9BrKArw4lKXHs3PQSRYZXLKIPtNB11PXL-aoq9oOmnacAqFqP-Uq5d6RFghvG9bSDt4eOTcT3zgUX3c9cKp46CSDiWQlz_mfla9WlxgMy9KXxT88jIaewa_HhG08Wvt8IOhXfX05ZuFpPr1ikGKWwtUiuprPUyyfb26c8CQ41aFcKtlHgzZkF8nHO36EMd4uwnlVP0fBM3ra7oM7dfZaiMELNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c0b1479d.mp4?token=jAFbdFQkz1rK-dtoMcxHgIjYiPKOWbV5hcqfoB5lchbIv2H-ahnkw6To2_DqBBRoGtEnHFrfrnSEy1FmhUvgHOfZl5B6HIHn4BuLW_AOl5-QWIvgx5VL1kKXvllA9BrKArw4lKXHs3PQSRYZXLKIPtNB11PXL-aoq9oOmnacAqFqP-Uq5d6RFghvG9bSDt4eOTcT3zgUX3c9cKp46CSDiWQlz_mfla9WlxgMy9KXxT88jIaewa_HhG08Wvt8IOhXfX05ZuFpPr1ikGKWwtUiuprPUyyfb26c8CQ41aFcKtlHgzZkF8nHO36EMd4uwnlVP0fBM3ra7oM7dfZaiMELNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت سد کرج طی سه ماه اخیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/123811" target="_blank">📅 23:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123810">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
اظهارات عجیب مشاور قالیباف درباره مذاکرات ایران و آمریک
🔴
توافق صرفاً یک تاکتیک برای خرید زمان و منابع است نه استراتژی صلح‌طلبانه
🔴
توافقی وجود ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/123810" target="_blank">📅 23:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123809">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0eeee36654.mp4?token=IPY7BuKPY6_RQVsXe6T4jWa4D32kqf0VnLbvGPN6-OY19Hq1JOwtE_fhhCTa_HU4dvBE7bB9Uq5nKlReXaUEdR42UW5By4GtaMJJE30q8j7fBAa3gnSpqxKEJAz_6Dn-coATa0ven1tP9D5V7oGvUD2YY9TJuWDQL3PmCgMJc-J0ar-4yAWmeQdGHeZx-4B1J65G69sFVuQ-b89ZxGaQKNPur1qeYKGQuHOWxrd7CXsWHhGhpoSmoq8kUVOtwbDiHrCl5zqTty8KuKo5mql9bD0TcMgXxUagFJaSovXAPAnpyd3ZUwKkD-U2gYUCSuFUNEjzL3zC3Tvxnf7Qd2YuwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0eeee36654.mp4?token=IPY7BuKPY6_RQVsXe6T4jWa4D32kqf0VnLbvGPN6-OY19Hq1JOwtE_fhhCTa_HU4dvBE7bB9Uq5nKlReXaUEdR42UW5By4GtaMJJE30q8j7fBAa3gnSpqxKEJAz_6Dn-coATa0ven1tP9D5V7oGvUD2YY9TJuWDQL3PmCgMJc-J0ar-4yAWmeQdGHeZx-4B1J65G69sFVuQ-b89ZxGaQKNPur1qeYKGQuHOWxrd7CXsWHhGhpoSmoq8kUVOtwbDiHrCl5zqTty8KuKo5mql9bD0TcMgXxUagFJaSovXAPAnpyd3ZUwKkD-U2gYUCSuFUNEjzL3zC3Tvxnf7Qd2YuwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ویرال شده از حرکت ورزشی یه پسر جوون توی ایران که شاهکار خلق کرده
🔥
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/123809" target="_blank">📅 23:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123808">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
کانیه وست برای شلوغ‌ترین کنسرت دوران حرفه‌ای‌اش در استانبول روی صحنه است.
🔴
هزاران توریست برای تماشای این کنسرت راهی استانبول شدند و میلیون‌ها دلار درآمد وارد اقتصاد ترکیه شد.
🔴
حالا تصور کن اگر یک خواننده محبوب خارجی بخواهد در ایران کنسرت برگزار کند؛ عرزشی حرام زاده با فریاد و جنجال، کاری می‌کنند که ایران و ایرانی را در چشم دنیا عقب‌مانده و وحشی نشان دهند.
🤔
ایران می‌توانست مرکز گردشگری، موسیقی، هنر و درآمد باشد؛ اما جمهوری اسلامی فقط فقر، سانسور و انزوا ساخته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/123808" target="_blank">📅 22:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123807">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
گزارش ها از درگیری شدید نیروی زمینی ارتش اسرائیل و حزب الله در نزدیک شهر نبطیه، پایتخت جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/123807" target="_blank">📅 22:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123806">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
پاریس تو ضربات پنالتی آرسنال رو برد و قهرمان اروپا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/123806" target="_blank">📅 22:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123805">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
این هفته مراقب تابش فرابنفش باشید
🔴
این هفته شاخص فرابنش بالا است، تا حد ممکن در ساعات میانی روز(ساعات۹-۱۵، با توجه به داده‌ها) کمتر در برابر تابش مستقیم خورشید قرار بگیرید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/123805" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123804">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExpXHc30W2oHWw_Ezx4tO6F1ndvM7VuTBxkM9kZQhocHJELRDaQ1HSZ2gYofpmupI-Wi5X2VE7jpMHouJrJgMoNaP8Ly47eAus9lXxfPYpY2HBg0fal6amawtmLIGXw1WRZqczj1mfWvcbGcbUYKLGj5Z2WwW_Q4k86IvbIQMUN0n-hfoU4Ruy_5x_6_ryl3giRImo1nOWOJe_oAsNuPVV5J6fp0jAM_ASXANotvHOaaNvswX6fMTetIShKG1i_ITSsO012m5IcPfi--X7TsR89idafeWhHBE5hhMN1AoUh1B7IOeVNFlDNZRo0FgV5_j8ycjASnjuV3tS_DDQBRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
فروش باز شد.
✔️
✔️
✔️
گیگی
5⃣
1⃣
هزار
✔️
✔️
✔️
کابوس هرچی گرون فروشه
✔️
حداقل خرید 10گیگ.
✔️
با لینک ساب
✔️
بدونه محدودیت کاربر
✔️
چندین لوکیشن مختلف
✔️
بدونه کوچیکترین ضریب مصرفی
🔽
🔽
🔽
🔽
🔽
🔽
🔽
🔽
🔽
🔽
🔽
فقط فقط گیگی
5⃣
1⃣
هزار
✔️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
⬆️
فقط فقط گیگی
5⃣
1⃣
هزار
✔️
https://t.me/V2ray_confing1
@aMi41garavand12
😎
چطوری اعتماد کنی؟ چنل اعتماد
https://t.me/v2rayaMirconfing</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/123804" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123803">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8MHmv16FWOsgyl9Wpd2YhWn3gLwc93EXm7UuQxbpqVsCYYVlOBuSTYUE5wwNzrds_p1yIOeAz-CpsDBqrpcKYwMAnWxVug6sv_EQqMYPFqVW3h_9nzNtOvQgyhyfhW-XQbJyZxgWf1FD_1ji4WWqtEgUoXY6o8HdCiGOzGr2dFNyJrobzkY1iDMtBdA6xCC3Mfjzf2Es2ScwRenP1CxAzQGFzv7ibLZjZbcKCU-LxdK_JaSRr7HdZA-nK5kswjtR5UANEBAtBmHnzZRRulHqLQqEYGAZ2dR34e80eU-1L_k3XoIBDGkplcAdviwvjeQwP9OOTWRJ3U-kpZ5ueYFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا مدعی است که در جریان این جنگ، دست‌کم ۱۶۰ شناور دریایی ایران را غرق کرده است. هر یک از این شناورها می‌تواند منبعی بالقوه برای آلودگی باشد. وقوع یک نشت جدی در تنگه، مهار آن را بسیار دشوارتر از حالت معمول خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/123803" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123802">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
به گزارش منابع خبری ، صدای انفجار در سراسر بوستون بزرگترین شهر در ایالت ماساچوست واقع در آمریکا شنیده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123802" target="_blank">📅 22:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123801">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsQjMoiEa1Hxs7G3MbzVE9AUowDvQkzENNjwtn4BwUKFcTKU8qbUjxWSVKyaERTUKh0_bdZPn-obUo6cF499kGtDMzR-fg-BEMxAbO3O8wVuDT9E2YkQ_HG8zkA0LwslwzHNtYGc9azAEEHwxnm41nydRRo4TIU10h8PXxegLx0WK6NOIwUYP0OKnU4fsl1DU5ioKWJ_SPunmHlmt7VIzjF_Z_AEYA8tk6XVoW-8TtuAwzafvzpRkhpDKkDTYpu-jNtXBL0MirFsCy1sfUPALNmwXJFPZ3VGDI8h8mpXksVUhPm80BL3LcKef9sxFlFkNpoRTJwe-YSTx8ZbduecAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: چرا نمی‌ذارید صداسیما سخنان رهبر درگذشته در مخالفت در مذاکره را پخش کند؟
🔴
نماینده مجلس: جای تاسف است که رئیس جمهور در دیدار اخیرش با مسئولان صداوسیما به آنها فشار آورده که چرا صحبت‌های رهبر فقید در مخالفت با مذاکره با امریکا را پخش میکنید؛ عده‌ای…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/123801" target="_blank">📅 22:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
شبکه 12 اسرائیل: ارتش یک طرح تهاجمی در عمق لبنان آماده کرده است که منتظر تایید سطح سیاسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/123800" target="_blank">📅 22:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uk3uTHG15QOCQYqoOmNYmRY6Pe65FK3YeATKaZq7dRD6AmbRaTupzJKAsjYkfwZbj2DZlxL17lC6Q8jX7WvCTBTvKA1l53PHjJ0MAZ9HdGwqj7aEy5AGwxJyWgzKN1OUQydWtRyEhoTt84G-c-otp5JjK1UilLthO6UzUggcvKo4WPGIjNRIE6Bx77aRZs3H12GCBSFZzbXfhddyYtMhlNhIyia1IZn6qIQtksRUSn3hZitUhP6xfvrexxcDgPSGZgtu5slJbdLoEQloniuCogJX3zbkRpUip8Xui0_XZN3kZOas7VCfScMJvdu39XWKd003eEIHyNCraAnOMH9gLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موجودی انبارهای آلومینیوم به سرعت در حال کاهش است
🔴
ذخایر موجود در انبارهای بورس‌های کالایی، نیاز جهانی آلومینیوم را برای کمتر از ۵ روز پوشش می‌دهد.
🔴
نمودار فلزات و میزان پوشش ذخایر:
🔴
نیکل: حدود 31 روز
🔴
سرب: حدود 29 روز
🔴
قلع: حدود 21 روز
🔴
مس: حدود 13 روز
🔴
روی: حدود 6 روز
🔴
آلومینیوم: حدود 3 تا 4 روز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123799" target="_blank">📅 22:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7AU3spuar8r7ql4Vb9jMkpoqraB9ampMr5nMCB0oYjpTN7WgGmwzqW-aWcUaUc2_VOqlXOdzfoa35_rezoZgykVvDzfKyHYMoRjwIG64TZ8QYex97-Zx6i3BwB8rmwR8UPOT_5Y3tMQz7zDxHoatTrw-jfZlKxzw4Sj5emylsAqjFQm-w1kDZV0ypqUyqveGG9wVlxcgdDm-unizMmnTwG9GrTbsj2jiBOFt-moFsocU91R2N1IoGJUYeRYcbAzqn1zBDWIrw9FyXB_bOPWCuuAbBaGdec1CIQXK_wk6nqfFqLEAo_pHsjEhwM-wVOE6QVWrM17nc2bcknjceyX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: چرا نمی‌ذارید صداسیما سخنان رهبر درگذشته در مخالفت در مذاکره را پخش کند؟
🔴
نماینده مجلس: جای تاسف است که رئیس جمهور در دیدار اخیرش با مسئولان صداوسیما به آنها فشار آورده که چرا صحبت‌های رهبر فقید در مخالفت با مذاکره با امریکا را پخش میکنید؛ عده‌ای هم به ما میگویند سکوت کنید تا وحدت بهم نخورد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/123798" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123796">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3bcc37acf.mp4?token=Orc08PIWQMB9FTtxc3kcmBq7Y2rrZbxR3sJ3_w-0R9MyTLohbmVZWC2aJehykRdvvSGdIugdvciXdtelz6n0N2nfaRVfhSZh_XfYJIvVFy5DVN5Yv7XegHNpCn_U-J_PpIMIYYsRD0Aw5jcQqdPL5JbF1UtXGj5H2Iv_SlZD8Ujav88Ku9_3CDABpdxss5wAD1lp6x20k80lPif-iLUdZGtcsGfMMCWB3Jz58q89wfXzIKYJ2fFrhD2irPTcw-mlSB13y10pADGwIaI6Lpk9N89Mq7C6SK_OdSvnDWju2IOIaEbOJUNvA9GdeXZo5GdG6wxdgvSpGDUcVNY95Rzkzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3bcc37acf.mp4?token=Orc08PIWQMB9FTtxc3kcmBq7Y2rrZbxR3sJ3_w-0R9MyTLohbmVZWC2aJehykRdvvSGdIugdvciXdtelz6n0N2nfaRVfhSZh_XfYJIvVFy5DVN5Yv7XegHNpCn_U-J_PpIMIYYsRD0Aw5jcQqdPL5JbF1UtXGj5H2Iv_SlZD8Ujav88Ku9_3CDABpdxss5wAD1lp6x20k80lPif-iLUdZGtcsGfMMCWB3Jz58q89wfXzIKYJ2fFrhD2irPTcw-mlSB13y10pADGwIaI6Lpk9N89Mq7C6SK_OdSvnDWju2IOIaEbOJUNvA9GdeXZo5GdG6wxdgvSpGDUcVNY95Rzkzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز امشبِ جنگنده‌های ارتش ایران شهر"
کرج
"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/123796" target="_blank">📅 22:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123795">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزارت بهداشت لبنان گزارش می‌دهد که از زمان آغاز تهاجم در ۲ مارس، ۳۳۷۱ نفر کشته و ۱۰۱۲۹ نفر در حملات اسرائیل زخمی شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123795" target="_blank">📅 22:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123794">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
این هفته شاخص فرابنفش بالا است، تا جای ممکن در ساعات میانی روز(ساعات۹-۱۵، با توجه به داده‌ها) کمتر در برابر تابش مستقیم خورشید قرار بگیرید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/123794" target="_blank">📅 22:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123793">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">💔
همه اعضای این خانواده جاوید نام شدن.
🔴
جاویدنام بیژن مصطفوی، ۵۸ ساله، بازنشسته آموزش و پرورش، رزمنده جنگ ایران و عراق
🔴
جاویدنام زهرابنی‌عامریان، ۴۸ ساله، بازنشسته تامین اجتماعی
🔴
جاویدنام دانیال مصطفوی، ۲۰ ساله، دانشجوی کامپیوتر
🔴
اصالتا از شهرستان سنقر،…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/123793" target="_blank">📅 22:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123792">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کارول ناوروتسکی، رئیس‌جمهور لهستان:
متأسفانه، رئیس‌جمهور زلنسکی نشان داده است که اوکراین به دلیل حمایت از راهزنان و قاتلانِ ارتش شورشی اوکراین (UPA)، آمادگیِ عضویت در خانواده اروپایی را ندارد.
🔴
در خانواده اروپایی برای راهزنان و قاتلانی که زنان و کودکان را کشتند و لهستانی‌ها را به قتل رساندند، جایی وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/123792" target="_blank">📅 22:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123791">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAdGZMoT9TH4Qg68KIQIC0zbYclSE3cGTsySTE54hqsSC3xW32oTM-A6ZsY8s9aT5xcIhIopQ-i_OBTEI0_WVmRuoPe9zYZ-cQ7n092dUjgcKFOc79i0N38tBfAxeoJU8T7GVs04BXZlvUMJr8sENFUgz6n_Vf0RDSDX2zDPPHL-ymT0q3YY1OHB1s4lgtpq2kxk1eLBXG5liE-6a0figSRc638f4morEGquenMmskIkup4-Wi3PYItYiL5GPAUNg-CvM3tddZNecer616w2nezXwxFBn-BkKD_YE2qotFyLHAY7B85FY4GcVusydd0nxfdnsTfr89xvjSR7XACOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام اعلام کرد کشتی تجاری Lian Star که از یک بندر ایران خارج شده بود پس از 20 هشدار توقف و عدم توجه آن توسط یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت و در دریای عمان توقیف شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/123791" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123789">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سازمان رادیو و تلویزیون اسرائیل مدعی شد: ارزیابی‌های آمریکا و اسرائیل بر این است که حزب‌الله با هدف کارشکنی در مذاکرات اقدام به حملات موشکی می‌کند.
🔴
انتظار می‌رود مذاکرات بین نمایندگان نظامی اسرائیل و لبنان در هفته آینده نیز ادامه یابد. نتانیاهو طرح را به کابینه امنیتی ارائه داد که به موجب آن دامنه کنترل بر غزه گسترش می‌یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123789" target="_blank">📅 21:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123788">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
صداوسیما جزئیات غیررسمی از یادداشت تفاهم [ایران و آمریکا] را منتشر کرد:
🔴
موضوع آزادسازی منابع بلوکه شده ایران از مهمترین بندهای رونوشت غیررسمی چارچوب تفاهم اسلام آباد است.
🔴
بر این اساس آمریکا متعهد شده طی ۶۰ روز امکان دسترسی کامل ایران به ۱۲ میلیارد دلار از دارایی‌هایش را فراهم کند.
🔴
به گونه‌ای که این منابع قابلیت انتقال و هزینه کرد در بانک‌های مقصد موردنظر ایران را بدون محدودیت داشته باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/123788" target="_blank">📅 21:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123787">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سنتکام :  تا الان مسیر ۱۱۶ کشتی تجاری عوض کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123787" target="_blank">📅 21:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123786">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، وزیر دفاع کاتز، رئیس ستاد کل ارتش اسرائیل و مقامات ارشد امنیتی امشب جلسه‌ای برای ارزیابی امنیتی برگزار خواهند کرد، گزارش کانال ۱۲.
🔴
بحث‌ها بر تشدید تنش‌ها در شمال اسرائیل و سخت‌گیری در دستورالعمل‌های فرماندهی جبهه داخلی متمرکز خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/123786" target="_blank">📅 21:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123785">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
مهدی خانعلی‌زاده، عضو رسانه‌ای هیات مذاکره‌کننده جمهوری اسلامی، نوشت: جمهوری اسلامی هیچ پولی در قطر ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/123785" target="_blank">📅 21:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123784">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کانال 12 اسرائیل: حزب الله در 48 ساعت اخیر 100 موشک و پهپاد به سمت شمال اسرائیل پرتاب کرده است،
ارتش اسرائیلی در حال تدارک برای حمله گسترده در بیروت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/123784" target="_blank">📅 21:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123783">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e34f3b02.mp4?token=cn5mC4NawJZf4hRMcn4OB3X9p5XOQ1rBwlwo80SRWRzHIi13dJ_-wTaDdqnxpQML4myjhThlUI53CY6Svvp3hWoOeVXCduUp0v9cXTHmKFZsU7R2vtFq2sed-TlO3qr5OcVhd2eek9jMIQMjxcAvZAlTkdory543W8XE8E0WpeltfTqdHI484hs0gO0s2QYzEjD54pENmn26SPdJi-2fQ6WQkQUNMpZ2Eo7MuCM45zVrEIRY-Ucxf8XrFRNRy9dZJWYNYQzknsi7AiTYVcNdhamLLejlHLxakMc4q3Wab2zs1A00bnmQbPWwOfKAsnUMTx8k3utDdV6qTqB9kDcyxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e34f3b02.mp4?token=cn5mC4NawJZf4hRMcn4OB3X9p5XOQ1rBwlwo80SRWRzHIi13dJ_-wTaDdqnxpQML4myjhThlUI53CY6Svvp3hWoOeVXCduUp0v9cXTHmKFZsU7R2vtFq2sed-TlO3qr5OcVhd2eek9jMIQMjxcAvZAlTkdory543W8XE8E0WpeltfTqdHI484hs0gO0s2QYzEjD54pENmn26SPdJi-2fQ6WQkQUNMpZ2Eo7MuCM45zVrEIRY-Ucxf8XrFRNRy9dZJWYNYQzknsi7AiTYVcNdhamLLejlHLxakMc4q3Wab2zs1A00bnmQbPWwOfKAsnUMTx8k3utDdV6qTqB9kDcyxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جزئیاتی جدید و غیررسمی از یادداشت تفاهم احتمالی ایران و آمریکا
🔴
گزارش صدا و سیما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/123783" target="_blank">📅 21:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
الجزیره: ترامپ برای جلوگیری از جنگ با ایران پیش از جام جهانی بسیار مصمم است
🔴
او همچنان برای دستیابی به یک توافق موقت با تهران تحت فشار است، اما پیشرفت فوری بعید به نظر می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/123782" target="_blank">📅 21:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1713e4ae.mp4?token=uxAJoE8429FERMfFSrYu2GaMXcgVPtUVJXVABhIKLyvrbZTLWujefWNDZP4ECvd7SZvTU8AyAmUkqnK3X1rwFQGMxysl5Fl4YYbXhm_wL1E14bQ2HEIMyeqBpDemreSsOkMn3SNqUFoe0doCRlrJcvxinJzryaFhosqos8JYPjpT1ATUAa1j73Nmao-WS_E2yWF1p_m7mLEWqiW7qAnGDeUp37W1dH5_kk_s3kMmDGbAEz71bXtQL5PZPMTzKBpOxAokvoiWYzlpiF8FRGKMjpDYqen_gdPGNnC53swGgo8Qmf2_EcL5GDa018AIF4A1YZyLLFwe-ct5TV8DcL1k-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1713e4ae.mp4?token=uxAJoE8429FERMfFSrYu2GaMXcgVPtUVJXVABhIKLyvrbZTLWujefWNDZP4ECvd7SZvTU8AyAmUkqnK3X1rwFQGMxysl5Fl4YYbXhm_wL1E14bQ2HEIMyeqBpDemreSsOkMn3SNqUFoe0doCRlrJcvxinJzryaFhosqos8JYPjpT1ATUAa1j73Nmao-WS_E2yWF1p_m7mLEWqiW7qAnGDeUp37W1dH5_kk_s3kMmDGbAEz71bXtQL5PZPMTzKBpOxAokvoiWYzlpiF8FRGKMjpDYqen_gdPGNnC53swGgo8Qmf2_EcL5GDa018AIF4A1YZyLLFwe-ct5TV8DcL1k-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلللللل مساااوی پاری‌سن‌ژرمن به ارسنااال توووسط دمبلههه دقیقه 65
@AloSport</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/123781" target="_blank">📅 21:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123780">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/123780" target="_blank">📅 21:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123779">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C5gloSiXES-9Lz6fQcfzzno7qdMyvunMfzSQVS9dThHml6T3jM5IthVB1-93oL6gLlH987SxKSe-Qx8_EvCeNsnL-oSAjLSMB-ftDA-iJQiTjJwK4v7G03FDFsz3EZal6IfKUQwYdEwCrBe5oTSp1cfLRF9T5iDCpeSM3K8S_UAlm2kb3Yrjs7bmk5E81YSm1KV6beA0WrOVXVEZpZJLD_Cnj900UuWFbrQk3eFlL_4ZNt_9YLNH4R4newcRUMzI7zn3x2QGPfPzNQjGkIJPgwEoBY_aNK6IejX1Y7pV7QJwiSHnoJSe9xLRQyXg7S5dNuanJ4KUICmKMyc4dMHHNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/123779" target="_blank">📅 21:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123778">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
معاون هوانوردی سازمان هواپیمایی: بیش از ۹۰ درصد از بلیت‌های پروازهای لغوشده تعیین‌تکلیف و وجه آنها برگشت داده شده است؛ ۱۰ درصد باقی‌مانده نیز افرادی هستند که هنوز برای استرداد بلیت خود اقدام نکرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123778" target="_blank">📅 20:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123777">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2BQTfZbRGjmvBxGKceefiL9gdvcVVlAHTRm7C0Xdnuk5ruhNEFFxymCzSTh6MUhb4pchQrFtaktvgnw9tiFvBASTyy3mb4pzaK45WsU_FoLWv_VJ2Zb_h5llNfP1huRvHG0eBhA4sz3lP9TqSa4Pi9bzKzrHxPKa-EU1sNusAKEjt5T0CISCTTw3YxGROkMy3EY4eqIjXrVV8BlyuX6iD-pLs-Gthb-ScrXLf23iKaNeS9_yNzyiIa5tTncK5KHTl4CPOX14F6I2DNPLxvdpO92U4GjaOJfcjM0sTaIw20cyRdr7492_zwW2LLNj_uFjCKsvL5iFYP_mv3N7fzXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیمام خیلی جالبه فوتبال دزدی پخش میکنه بعد کنار زمین تبلیغ بیمه قسطی میکنه وسط زمینم تبلیغ تشک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/123777" target="_blank">📅 20:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123776">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل : نتانیاهو، قراره به‌زودی یه جلسه امنیتی برگزار کنه تا درباره نحوه پاسخ به شدت گرفتن حملات حزب‌الله تصمیم بگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/123776" target="_blank">📅 20:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123775">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
پزشک رئیس‌جمهور آمریکا: ترامپ با «تورم ساق پا» و نیز «کبودی خوش‌خیم» دست دست‌وپنجه نرم می‌کند، اما همچنان از وضعیت سلامت «عالی» برخوردار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123775" target="_blank">📅 20:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123774">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358ce379f1.mp4?token=vPBxRWOXVKMi3-uAUZJ_-6emD9MUshZGaPw_lSZAVpFyJ7LahC7KtrFO1m4HFup8SRsSLMKlQpQEmK-uuUX--aozQWcn3uIGMr4Fnue4d-ogK9SXksaCaTAz0DT2i9lLB7MOgGuZLoQj815DzPshZWhoA-qCXF-_tJ0H1RTQ5xihhOmLeCs1DnLvlbxjyPbViGQSfM8RkfvCho9RsAsm1-8btXTELwW5UlVYcCaSa8yD0m3QL1_2lSlDu6a1FTqM-Z8VyE-h2NTpVoOyS-yPFsnNxHprTxCjjqgc95M1u0dHFY0zgcpBLOL1Wk3zFGlGD46ABgrm08MkEn_-s707tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358ce379f1.mp4?token=vPBxRWOXVKMi3-uAUZJ_-6emD9MUshZGaPw_lSZAVpFyJ7LahC7KtrFO1m4HFup8SRsSLMKlQpQEmK-uuUX--aozQWcn3uIGMr4Fnue4d-ogK9SXksaCaTAz0DT2i9lLB7MOgGuZLoQj815DzPshZWhoA-qCXF-_tJ0H1RTQ5xihhOmLeCs1DnLvlbxjyPbViGQSfM8RkfvCho9RsAsm1-8btXTELwW5UlVYcCaSa8yD0m3QL1_2lSlDu6a1FTqM-Z8VyE-h2NTpVoOyS-yPFsnNxHprTxCjjqgc95M1u0dHFY0zgcpBLOL1Wk3zFGlGD46ABgrm08MkEn_-s707tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاطمه مهاجرانی، سخنگوی دولت:
دولت پول بازسازی خانه هایی که در جنگ تخریب شده را نمی دهد، چنانچه تصمیم بگیرند خودشان بازسازی کنند، دولت مجوز ساخت دو طبقه بیشتر می‌دهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/123774" target="_blank">📅 20:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123773">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBDYzhJ8kul2g2EJ4KXI1mCavS1t-ns3kkoLnt46QSOqhIIvRHaiVXPpW0cdh9QLwr_Y2yFGXlDgGTPM5R_2Na9mVbbSUZ_2nEZK3ZgpBWPH_jSnSgxdah9RsAqqZF94sPGQCOZeeniPaB3T9LEgYn13FsTjmi-lSz4nbugv9KvY4S4lMsGN0ayWE3SOjLtHiMvl3Yd-FziR2y_T5B0YBp3nd6oKrERkIznf4eE_235IB54_BizzYps2IozbtG2E0iic0IdmHccI6lcjYLpNjGwq60LG_tCtyrBKHCiCAG1QTmps3v7bk7NIdZgDRe38ZouioGf2RfDLwMDPzAPe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ در طریق Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/123773" target="_blank">📅 20:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123772">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xi38hlcCmu6tl5oqq2fzGn2jwbC0mXlVxONa9lt761bb5jPLO0lyUFzwXirV94TS5VXhnaY85wqRGZIoMe3QtJCP5KCP9mUy8JdCMp0p-0B7OcMJbLZvasUPsP7BfgXSiZnRlHXIPBankhliDFMi88G5VKDKSaDDQjfVABJmYcaVA3Y4e_kxyabbqZQoOK0ks261tf3SbN8hAyKZbihUvSw6TW3HWjDqX2DBVxSml0TA95bdIYeLjXI6aPJuralv8UI3ZBze7KuoWdhN5208FC8fvnOYkXvaU4nc8vpvYjOp8Q4GmjWez-sp3IT8li2qs9saZU9jJIDTcS6OGJxA_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در شبکه اجتماعی «تروث سوشال» درباره «سندرم جنون ترامپ» پستی منتشر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/123772" target="_blank">📅 20:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123771">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lryYXdUvQ-SWg684VpcALSSfK9gwj42ZkdDTSE1YjULD4Zmk_m3m7eOenf13NAlJgPr2gcBDadu7cc5fw8UNd0u_ZH4HMyZs9SJb6h_oiF5buo-M7KxQkePp31uTwXocxfYJN8_JUTKLs84Ywtgt6iaGQww7_RSntuDLTGfdLdrn1ioupsGAashehZqeg_pOtKQWlkD-TRkGXGYdUqxlZ53-r23b-8qC4O3HaZe8r_Z0zmH0iYRmrkHNHjpTbBh6h4KPtWCvTxGxdUAXZMXx7YHYB8kcqx3xI8NrHSL5a67gvyzzU7rehFAAS3Ib93x8rqpZxUGoLse2FGghfrVFbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
می‌دانم که هنرمندان دچار «ییپس» شده‌اند و نگران اجرای خود در روز چهارشنبه هستند، بنابراین دارم به آوردن جذاب‌ترین شماره یک در هر جای دنیا فکر می‌کنم، مردی که مخاطبان بسیار بزرگ‌تری نسبت به الویس در اوجش دارد و این کار را بدون گیتار انجام می‌دهد، مردی که کشور ما را بیشتر از هر کس دیگری دوست دارد و مردی که برخی می‌گویند بزرگ‌ترین رئیس‌جمهور تاریخ است (THE GOAT!)، دونالد ج. ترامپ، برای جایگزینی این «هنرمندان» درجه سوم و بسیار پردرآمد، و ایراد یک سخنرانی مهم که کشور را به جلو سوق دهد، همانطور که از زمان ریاست‌جمهوری‌ام انجام داده‌ام!
🔴
دو سال پیش، ایالات متحده مرده بود. اکنون ما «داغ‌ترین» کشور در هر جای دنیا هستیم. من هنرمندان به اصطلاحی که پول زیادی می‌گیرند و راضی نیستند را نمی‌خواهم. من فقط می‌خواهم در کنار مردم خوشحال، باهوش، موفق و کسانی باشم که می‌دانند چگونه پیروز شوند.
🔴
پس، با کپی این حقیقت، به نمایندگانم دستور می‌دهم امکان‌سنجی برگزاری تجمع «آمریکا بازگشته است» را در روز چهارشنبه، واشنگتن دی.سی، همان زمان و مکان بررسی کنند. فقط میهن‌پرستان بزرگ دعوت خواهند شد — این جشن وحشیانه و زیبایی از آمریکا خواهد بود!
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123771" target="_blank">📅 20:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123770">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
دلار در بازار آزاد تهران: ۱۶۹ هزار و ۷۰۰ تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123770" target="_blank">📅 20:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123769">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou2nQ9W2EvniGE5iFvv-gsXpf27EByw5H-7ijoNuAw_Dfij3NBjvnc-kWDfUKHvbwsdysGMEEcjX0AxsMunIaDxyqTwVelDfFas_TsQf8VhYDkr2zAVbjqNXeh_1_YvY3-gVRkKT76rp_-DDcldsvSGZmRvAsQOb7d-W42eEkw9xUa_dbPwi3BdF-3ry99C1TPcHFWFv7PsbfJBnN-ShExzDjYzbmANr3X4otIOWEBO4iT8sgeim_PwIaMWVGf_kNv0YKLbjElQ5E0f7YIav5-0IbGruEHjNhPEvRPhK-fnls1NaVYTfOQ6vsPQXwjAz9UeCj5ckNbUyHe82Yon2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتلانتیک
:
تلاش‌های دونالد ترامپ برای پایان دادن به جنگ ایران نشان می‌دهد که او همیشه در مورد مهارتی که برند خود را بر اساس آن بنا کرده، اغراق کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123769" target="_blank">📅 20:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123767">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
حزب‌الله ویدیوی جدیدی از حملات پهپاد FPV خود به مواضع ارتش اسرائیل منتشر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123767" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123766">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی اعلام کرد ذخایر هسته‌ای یک نقطه اختلاف بین ایران و آمریکا است و برای کمک به حل آن آماده‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/123766" target="_blank">📅 20:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123764">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50be41a822.mp4?token=tBKN2ypnVFJyT80qkMLZTvtxKUgMRkRBTOyQlyqHDdNYGfOKbZUCIkCxtyqDJ1PSp5DSQE52-5ljLwj8bXmjqjGqAH6n3hvG9an32fa1PD-34KV6OY7org0ABnq4AXPpZwQKHqPnyN5TtLg9EQ26kQuz0gsPklQBBMfgs8Xovimd3_rG_Y4Fzyg8FYPg4dVFJCEw4eHmYJ-GpDeMVE30dn2dMcJdi4U6_AESxq94VHwqOY2rorevMTQgyuYPUzgipP25xHNImyRN_PTqHvbPz7b87PVzCEg0NEy5i37Nw2dELS6P5B6lrZ-RwlBsiYJNwAB6w-cWGL7-JcNyJ1eiKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50be41a822.mp4?token=tBKN2ypnVFJyT80qkMLZTvtxKUgMRkRBTOyQlyqHDdNYGfOKbZUCIkCxtyqDJ1PSp5DSQE52-5ljLwj8bXmjqjGqAH6n3hvG9an32fa1PD-34KV6OY7org0ABnq4AXPpZwQKHqPnyN5TtLg9EQ26kQuz0gsPklQBBMfgs8Xovimd3_rG_Y4Fzyg8FYPg4dVFJCEw4eHmYJ-GpDeMVE30dn2dMcJdi4U6_AESxq94VHwqOY2rorevMTQgyuYPUzgipP25xHNImyRN_PTqHvbPz7b87PVzCEg0NEy5i37Nw2dELS6P5B6lrZ-RwlBsiYJNwAB6w-cWGL7-JcNyJ1eiKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های شدیدِ ارتش اسرائیل ساعتی پیش، به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/123764" target="_blank">📅 19:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123763">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: دوستی واقعی بین واشنگتن و اسلام‌آباد در حال شکل‌گیری است؛ این مدیون رهبری پاکستان است که به تلاش‌ها برای مذاکره با ایران کمک کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/alonews/123763" target="_blank">📅 19:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123762">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6f96dc5.mp4?token=GlgnoohIKp2L7A1h7khaSTmsrNdmUMvxsgwXvCHMvEuxAFqszfvi9PUiBLjkYEjsK7hxoZ5Ne8A5xnfAWIuG-SUyke_o5vUDrvWJNuho4YvsErDxycywHnyKNDvaA1IxOS3BAwz1slQhl27K1Mm0igMiMDL4ra-Su2ZE_qgMxCqrs68y7HHsViYd5PUiGS4QLjIj5d01xnpurwUO_wHL1K6_PNcqYFTo-Z8Gwtui6gSwmQ27ECYPTETMS0w3mtX0GeBB0eyNvMRsNNlToDH78qijesgKQ11aN2_5D7n4UUj-iGM_4UBSmF4YLh6koSYh1X97roBXsRpWAsSccjBucg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6f96dc5.mp4?token=GlgnoohIKp2L7A1h7khaSTmsrNdmUMvxsgwXvCHMvEuxAFqszfvi9PUiBLjkYEjsK7hxoZ5Ne8A5xnfAWIuG-SUyke_o5vUDrvWJNuho4YvsErDxycywHnyKNDvaA1IxOS3BAwz1slQhl27K1Mm0igMiMDL4ra-Su2ZE_qgMxCqrs68y7HHsViYd5PUiGS4QLjIj5d01xnpurwUO_wHL1K6_PNcqYFTo-Z8Gwtui6gSwmQ27ECYPTETMS0w3mtX0GeBB0eyNvMRsNNlToDH78qijesgKQ11aN2_5D7n4UUj-iGM_4UBSmF4YLh6koSYh1X97roBXsRpWAsSccjBucg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلللللل اووول آرسنال به پاریس توووسط هاورتزز دقیقه 6
@AloSport</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/alonews/123762" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123761">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
هم اکنون نیروی دریایی ارتش آمریکا از شلیک و متوقف کردن یک کشتی تجاری ایرانی که قصد داشت به بنادر ایران وارد شود خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/123761" target="_blank">📅 19:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123760">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
رضا پهلوی: مردم ایران از هدف قرار گرفتن زیرساخت‌ها خوشحال شدن  ‌
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/123760" target="_blank">📅 19:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123759">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_zt6NovIToKVfjGsA7wTcWV1VaOvWFBIwVI_9J5TEuk2l9WEjeeqeTYENCNkLfuJdyNsSoEGXe3bTuItEcJ64zVjk4cqn2TXUBWVkNsb618sP4CkB-gj-WMSuqRabQ5kO56m7AshcLThjXU_7sqaUfPLIAap6OaTLGr4OpBm1m4vz4fTltGvt8O4q91R6Xm_5wnNX_WfWtYGfFQpuzG9ayqLk6Yl2DDOkVC8WkXoscYCFe5nseZm4h7wAdwKWIMomhjFJYtLGMUxW7LP9cPaCy2b9Hyx_Betnpo3ZfFjBkOgBpZ4O9QjYrdVPPlMUKg4nfi_6CqrUSXG0f_S_FjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی: مردم ایران از هدف قرار گرفتن زیرساخت‌ها خوشحال شدن
‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/123759" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123758">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مدیرعامل آروان کلاد: زمانبر بودن بهبود وضعیت اینترنت از نظر فنی فقط بهانه ست، نت رو گذاشتن رو حالتی که اگر خواستند سریع قطع یا وصل کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/123758" target="_blank">📅 19:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123757">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
مقام آمریکایی به AP :  یه کشتی تجاری که قصد داشت به سمت یکی از بنادر ایران بره، متوقف شده
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/123757" target="_blank">📅 19:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123756">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75424ce9f6.mp4?token=drqVWohNDzeOAXk_2ppttfpDS1pcAmW8DVdjAmvF6OcNtIZN_ZfLtnFIxgDNsYJ0gl7fyWPrusZIFRRSq38mOpzeezgcKqPGFgacAqW4KQKOUvDT9ekTjeDAgQ7B1vJnZhuUFDWHqbKWuLLP1JDqaQ09QrVgvyQpWCREAGp4-Qk4LCKaU0yVvdWUEC62rKdlpPMt9nT9p78N6mCvndhfl-Rut2cVCZf6Il-amE1G5Y1n7DzwcVsVTj5-2UAGo1rqpyD_iVS1GlMfyhQ3hfdXTIZoAQa_tmYM3Nz4H9ZQzCfobfodJkISEbRxUtKXKV88EqedpXp3ajIGLsdi06biOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75424ce9f6.mp4?token=drqVWohNDzeOAXk_2ppttfpDS1pcAmW8DVdjAmvF6OcNtIZN_ZfLtnFIxgDNsYJ0gl7fyWPrusZIFRRSq38mOpzeezgcKqPGFgacAqW4KQKOUvDT9ekTjeDAgQ7B1vJnZhuUFDWHqbKWuLLP1JDqaQ09QrVgvyQpWCREAGp4-Qk4LCKaU0yVvdWUEC62rKdlpPMt9nT9p78N6mCvndhfl-Rut2cVCZf6Il-amE1G5Y1n7DzwcVsVTj5-2UAGo1rqpyD_iVS1GlMfyhQ3hfdXTIZoAQa_tmYM3Nz4H9ZQzCfobfodJkISEbRxUtKXKV88EqedpXp3ajIGLsdi06biOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ بارها جی‌دی ونس را دست انداخته است
🔴
نیویورک تایمز گزارش داد دونالد ترامپ بارها در جلسات و محافل مختلف جی‌دی ونس را درباره مسائل سیاسی و شخصی مورد شوخی و انتقاد قرار داده است.
طبق این گزارش، ترامپ به مخالفت اولیه ونس با حمله به ایران، نتیجه سفر دیپلماتیک او به پاکستان، تعداد مرخصی‌هایش و حتی قطع کردن صحبت دیگران اشاره کرده است.
نیویورک تایمز همچنین نوشت ترامپ بارها ماجرای افتادن جام قهرمانی دانشگاه ایالتی اوهایو از دست ونس در یکی از مراسم‌های کاخ سفید را یادآوری کرده است.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/123756" target="_blank">📅 19:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123755">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نماینده سیستان و بلوچستان در مجلس: برخی از مناطق زاهدان ۲۴ تا ۴۸ ساعت آب ندارند
🔴
ادامه بحران آب، استان را با چالش‌های امنیتی و اجتماعی روبه‌رو می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123755" target="_blank">📅 19:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123754">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
مقام آمریکایی به AP :  یه کشتی تجاری که قصد داشت به سمت یکی از بنادر ایران بره، متوقف شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/123754" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123752">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aadDHheP_iPGSIMX8t-tggOzYGxtx0nGPPLpPAdFPBATI8vVuS7GCszFRLnSb6-xbRGJWXR1H5pcEGR3lgC1ZYFSU4QwwpZhAbWCKRcrE0B-HJ6iTD-JMYGvsYGGJb3rhZFGNeGoH_a9f_aVlP6FiDg9UZTrBcV5kwe284FfZ9f9NMyeaAnOSyEN00Abl3s7_vra-fhssueIreKCxCiAmj8p_fR0MQvi5ouIGFrtHHklo81x1JLzSW6EvRKNnJ98GAq2Ix_YpJDdyQ01RyTYpg8vFaPocKrx1WudIxOwXTNGLy51HFGUaec1YYzz-YH-MnBmDiu-TgQ7oGkqjzxIzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4ojP6jrvB_vFR8uaWH_VLYjdkmLwbNYuA-cWUVRJwvq17qvpXvCiYnMyqdcITVAroKb86U3JfnTmx2eY5wKSfQubdPWiZPT3LIgazv3D30pAuCs1Kv2qfSSvI9GrdS0vPJ_8vyvclfqANgUtM_Hdj0fzuf6jy7ZnxreiXWrvl4u0zf_ZO-bvuW172osckbt3I8CuL-PhqRfozShaEws7VS2JS8rxlg6NPXS-L-hW6F_3G9e609sY_jyT8tDCdMpq5b1xJz_aG-lQ6d8E7SBojofADM6sotyovRJOWI417wKBA9Ld3pM3Iz_owZAM1madr-RHlBjXIKX1TVyQcz0tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سلفی حسین طاهری مداح و یک جان فدا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/123752" target="_blank">📅 19:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123751">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BAbgjsLWmb60T3gLfRNOWZ70fIVjj4MZp8bBUcgHMOarondZhUSIxsY9mZ44jRKtJIYdrS1-XGVUovjaQy1gZbE9lV1UhUQC19seQTZcwq_q8Ung9DoOBfMoI6IEaSOEdZSNto6DP9W1rz-tZS7ghZbZQH1gdQrQsSaqkQA323dzvwyvbQCoxz0NFpAeoyDVGp96Z_l5gvFqpfVEvw_LRFE-x54YLpfux02WakDJ_puBXnL0bbRfJlAzKXZ85t9_SyePFd8HaYrodzLA69Cs5B6Nbh2xaVqFD5pjTn94ph7wFUev8K4Tz2BmZXOYck6zwvOSiihMGTBBnIMciFr7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌الانبیا در بیانیه‌ای اعلام کرد که هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگه هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی قرار خواهد گرفت.
🔴
در این بیانیه آمده: «هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.»
🔴
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفا ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123751" target="_blank">📅 19:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123748">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E1gF9Eulnp7KlNLmyXWOne5cNfl9onF3XCW7UH3uXN4Tbn8omYpjyoCnBHyMLZMjzc0flmW4X_5RzA4JADfP1YlXdEvp9s0gloSEUM89-gEeH7PkSZhZCrN-IMXIgugKQQ7uWA9-Or9shdG2ozPce-8zqyjjS0P-gf6hTf1zoAbk1Cx_BWQnNJ4OwwymwRjHZ2IEmUXfjtdx9pxO_3rgI2el_mT1oixjtYg3z9wyHynaasVDjZis378qT0Lk6nJ26RAF0nghB5V63juolLps_QcbiHapmjdGgzRBbgJO7o9sMWovmo7qDmJdEEce1PeuluEgIMvZIy41qLK1AWGL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hXSxWqSMoc93G0XWM0Udk3V2YwntTz550O3lcDPSi6uFNk2RXq_P0Hm0pZNxD32sKKeLcr78bDhCPqqPdCaVtNMZsHxmipxu8Glxv_6ocxi3DIRshbBpzwLX9vtv7EqWTnzWRNW0iOr0oT4ou_TlOkSLcvRtNZMsu25NTIr5sQKSHn5JtyBy2kJv-8ImaZkBmmIMMTENG4Cr-3-GJb0At2tX1szJx-dTmVkxTtOrQjDJw_xcbgD2an9Dy0o992imQe_Qd4ywhdRz9Jh-jP6RqKKRlRHTaupAN6FyG3U08b50Os7utnwch3xd0bTZfGOywkaSCg3tshPArS2Tg8pTsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a561eadb68.mp4?token=SlyliyK2s5opHpP2nsYPjgVmJZtk8eRcRgCYPc8lln7U5qgiPCnhPdk6HV7oqZhIssLSAitNMZZV0eO9d0G3_XBPW3OVgWLzuxB9AcWM8qc9axFE-DKsdnbWnooPPwno981E1XvR-b1q5Nof0fHLQp6alzeffx1gf3BIE6PlXcimggiSamczAmfAyvLZBd0w4QqM6jwU4MJvVZAlfFtCrjCVwXFYXYrNKmp3HhmXldJUSb2CKielLbkV0rifpUh80lZDoR6R_I-yNqgfCxXfW_22elPS7yxlaCM9OElr-qhQL5u5gacs7HycTg0Hi7MUk59GVQg2h0G5dZs57M99wg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a561eadb68.mp4?token=SlyliyK2s5opHpP2nsYPjgVmJZtk8eRcRgCYPc8lln7U5qgiPCnhPdk6HV7oqZhIssLSAitNMZZV0eO9d0G3_XBPW3OVgWLzuxB9AcWM8qc9axFE-DKsdnbWnooPPwno981E1XvR-b1q5Nof0fHLQp6alzeffx1gf3BIE6PlXcimggiSamczAmfAyvLZBd0w4QqM6jwU4MJvVZAlfFtCrjCVwXFYXYrNKmp3HhmXldJUSb2CKielLbkV0rifpUh80lZDoR6R_I-yNqgfCxXfW_22elPS7yxlaCM9OElr-qhQL5u5gacs7HycTg0Hi7MUk59GVQg2h0G5dZs57M99wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">8 اردیبهشت ماه یه زوج عروسی گرفتن و 20 میلیارد تومن خرج عروسی‌شون شده!! فقط یه میلیارد پول فیلمبردار دادن! اینم فیلم عروسی‌شونه.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/123748" target="_blank">📅 19:13 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
