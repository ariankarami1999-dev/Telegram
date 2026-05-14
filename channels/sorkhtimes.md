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
<img src="https://cdn4.telesco.pe/file/SkWsWR_w18HmEbxi8rC6iUTA6XQqOYa02PrQ8e970rNRdqHmPenyUtYzhsCCh2KtQOvBDzN17Y4me2BztKP0ZFHip-By4Uxe0gAZZmdU5OLH7wFEaZsYYoOz4aMF-tCrCPuvxhQNC2p6IiwucWCBh-rGiZnms3_ccGDZxkYAHpRIeC1srvQf5qMNnR6TIimjVi4FtXpPr34mmhFzIb27epws9PhuXGj5ULthaTtVkVlt8fR4qnACxDhKz9SdO19YfzpUjoNF7dRrW3h_r3T36MzZwkcuyNAvCKvYCS1egRtZt2eITNcRJ-WvgUIjKdWRtn0wYQQrXTulVFQRXSlC1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 00:23:32</div>
<hr>

<div class="tg-post" id="msg-131653">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 1.4T
10 گیگ 2.4T
20 گیگ 3.6T
40 گیگ 5.7T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 21 · <a href="https://t.me/SorkhTimes/131653" target="_blank">📅 00:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131652">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
با اعلام مهدی تاج، باشگاه استقلال مجوز حرفه ای گرفت تا حضور این تیم در فصل آینده رقابت های آسیایی به نوعی قطعی شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 225 · <a href="https://t.me/SorkhTimes/131652" target="_blank">📅 23:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131651">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚡️
⚡️
قلعه نویی ستاره پرسپولیس را خط می‌زند!؟
❌
در تیم ملی به هدایت امیر قلعه‌نویی، رقابت در خط حمله خیلی شدید شده. حضور سردار آزمون و مهدی طارمی تقریباً قطعی است و بازیکنانی مثل شهریار مغانلو و امیرحسین حسین‌زاده هم شانس بالایی دارند.  به همین دلیل احتمال دارد…</div>
<div class="tg-footer">👁️ 277 · <a href="https://t.me/SorkhTimes/131651" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131650">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
فووووووووووووری
🔴
به دلیل پیش رو بودن جام ملت‌های آسیا در دی ماه و برنامه آماده سازی تیم ملی برگزاری ادامه لیگ برتر پس از جام جهانی منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 322 · <a href="https://t.me/SorkhTimes/131650" target="_blank">📅 23:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131649">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
معامله‌گری: تنها با برگزاری مجدد لیگ عدالت در فوتبال ما برگزار میشه و قهرمان باید با بازی کردن مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 419 · <a href="https://t.me/SorkhTimes/131649" target="_blank">📅 23:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131648">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 1.4T
10 گیگ 2.4T
20 گیگ 3.6T
40 گیگ 5.7T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 452 · <a href="https://t.me/SorkhTimes/131648" target="_blank">📅 22:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131647">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
پیغام عجیب بیرانوند به حدادی، مرا به پرسپولیس برگردانید!
🔴
به گزارش شهرآرانیوز، علیرضا بیرانوند که خودش را برای جام جهانی آماده می‌کند، نیم نگاهی هم به آینده خودش بعد از این مسابقات دارد. او از چند ماه پیش به دنبال بازگشت به پرسپولیس بوده و در شرایط فعلی…</div>
<div class="tg-footer">👁️ 534 · <a href="https://t.me/SorkhTimes/131647" target="_blank">📅 22:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131646">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔺
بخشش جریمه خداداد عزیزی توسط کمیته استیناف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 636 · <a href="https://t.me/SorkhTimes/131646" target="_blank">📅 21:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131644">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚪️
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/SorkhTimes/131644" target="_blank">📅 20:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131643">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
معامله‌گری: تنها با برگزاری مجدد لیگ عدالت در فوتبال ما برگزار میشه و قهرمان باید با بازی کردن مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/SorkhTimes/131643" target="_blank">📅 20:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131642">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">💬
🔴
امیرحسین اصلانیان، پیشکسوت پرسپولیس :
◽️
تعویق لیگ باعث شده باشگاه‌ها از شرایط آرمانی دور شوند و به اعتقاد من هیچ تیمی با آمادگی کامل وارد مسابقات نخواهد شد. حتی این احتمال وجود دارد که لیگ بعد از جام جهانی هم برگزار نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 652 · <a href="https://t.me/SorkhTimes/131642" target="_blank">📅 20:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131641">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
حمید رسایی: دولت میخواد قیمت بنزین رو تا ۲۰ هزار تومان افزایش بده
.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 733 · <a href="https://t.me/SorkhTimes/131641" target="_blank">📅 19:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131640">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ5nzC2dizdU79XDCSnsPGYZfr2K7dwRLky2KqzcetU25kF2Dve7ak9tVfe_eqw5st4p53PQk9G8d_f5vgMvkxSmt32EbeHxuIAPQ3TtxHWmQZXN7h6mAseljjRlnlDrtci645be-7_wip8SdOgdAvV6ZvvP6X5yaGGo2zTh6iqm9RribxLIlqcM_sV_RDw3sPW74aRpIWoG-ixsxO1nxi0vBjgVq3Kj2N5fSkZ0yMOzOwYOCXXJDTvC2STMmhBJZKtsvGWZX-kaolAAhDkiksDW5W_HYu3boKWfJSTXZ2FHQwV3WW2N3qUKShkIVNSPh7mr61LVLLYjI0l_-JgIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روزنامه اعتماد آنلاین:
🔺
اینترنت بین الملل خرداد ماه وصل میشه
🔺
هفته آینده به ریاست عارف معاون پزشکیان قراره زمینه‌های لازم برای رفع قطعی اینترنتی فراهم بشه تا حداکثر تا وسطای خردادماه اینترنت وصل بشه
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 758 · <a href="https://t.me/SorkhTimes/131640" target="_blank">📅 19:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131639">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt2NxjNbUJHySWqepjG3w5Unz9xe_jWrPCyXg28S8C285irb6eeQa1zCaUHevNFMtR_EiIl9WJHSLl5qFdUASodEYT33hsqVKZ8bFKr3SL4UvMkrJApsV1GyDuJbpjb6N2XCEptL17McD8k6mvnkZIeX1xkEJQwfsuspWN1QcNH9JeCuIHUNZU5RIJw3rKTjHSYTlIfkdGgq5loNWIn09WIB0FVDYoZxfj3rJfQfdKLQSCWncIL66KlLFC1vhPkaNpqzcjWYt9wfOgBGmPt3I8e5cfvxz_JZbMCKCHfvubF46FuTe-6eHWBdNZXWbnAWal-7Z4ywyn2FEZTkQhTeRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دنیس اکرت، بازیکن دورگه ایرانی که برادرزاده آناهیتا درگاهی، بازیگر سینما است، نام خانوادگی خود را در سامانه فیفا به دنیس درگاهی تغییر داد و مشکل او برای حضور در تیم ملی ایران حل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 845 · <a href="https://t.me/SorkhTimes/131639" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131638">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🛜
دو
عدد سرور نامحدود ۲۱ روزه Anyconnect موجود شده فقط 4.5T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/SorkhTimes/131638" target="_blank">📅 15:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131637">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
خبرهای اولیه از توافقات میان چین و آمریکا میاد شامل مواردی :
🔺
خرید بیشتر سویا از آمریکا
🔺
خرید نفت بیشتر از آمریکا
🔺
خرید بیشتر گاز مایع ( LNG )
🔺
خرید 200 جت بوئینگ
🔺
ترغیب ایران به اعطای هرچیزی که ترامپ نیاز دارد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/SorkhTimes/131637" target="_blank">📅 15:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131635">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔵
تاجرنیا خبر داد: هزینه‌های استقلال در فصل آینده به خصوص در جذب بازیکن به شدت کاهش پیدا خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/SorkhTimes/131635" target="_blank">📅 14:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131634">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⚪️
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/SorkhTimes/131634" target="_blank">📅 14:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131633">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO-4t_NoFdXOuVUGnAfKHynYE2OviM_4xTqpBW_3BCqhsAkUknH1ifjO2fFUIKTjNWcoUIR7DgDUyck0dgdT3ePb-GqSzHH1dq9yzfyAYDzrgjqaD0ZEDqSVqRhH_pTDwEogmIBvvG0oHhE4rsDNkSA2VFmqKAgJQutzu-wQQzDTxNWFeUhlog3T2EZ-J1F6IyLDMH013CYtSafB38qbJeXZkglbSYQ90_EZKD6YW1iyeRGpv_HLrA0ND9dTF2Pt3urxym8gmDqm1lEe27JijF4EgZm0mZlN76jZygaCN1j0K9Id-ZwzK71l38oJK8uqNQ_F39bRiX5HCmbq7A56Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
🔴
امیرحسین اصلانیان، پیشکسوت پرسپولیس :
◽️
تعویق لیگ باعث شده باشگاه‌ها از شرایط آرمانی دور شوند و به اعتقاد من هیچ تیمی با آمادگی کامل وارد مسابقات نخواهد شد. حتی این احتمال وجود دارد که لیگ بعد از جام جهانی هم برگزار نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 851 · <a href="https://t.me/SorkhTimes/131633" target="_blank">📅 14:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131631">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
پاتک بزرگ پرسپولیس به تراکتور؛ اوسمار ستاره‌های سابق خود را می‌خواهد!
🔺
تیم مدیریتی جدید پرسپولیس به شدت در تلاش است تا دو ستاره سابق خود را برای لیگ بیست و ششم به تهران بازگرداند. به ویژه حالا که اوسمار دوباره هدایت پرسپولیس را برعهده گرفته است؛ این سرمربی برزیلی در گفت‌وگو با مدیران پرسپولیس در چندین نوبت اعلام کرده که خواهان جذب این دو بازیکن است. ترابی و اسماعیلی‌فر گفت‌وگوهای با مدیران پرسپولیس در این زمینه داشته‌اند و به آنها چراغ سبز نشان داده‌اند!
🔺
این در شرایطی‌ست که از تبریز خبر رسیده باشگاه تراکتور به محمد ربیعی سرمربی جوان خود تضمین داده است که ترابی و اسماعیلی‌فر دست کم یک فصل دیگر نیز در تبریز خواهند بود و برای پرشورها به میدان خواهند رفت. باید منتظر ماند و دید آیا انتقال این دو بازیکن از تبریز به تهران انجام خواهد شد یا خیر؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/SorkhTimes/131631" target="_blank">📅 13:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131630">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdkZupdOYVvu5ybO8oXLjljxJ_Ez3SZ2EgjrdEcOaBZ145UUtKDyBVpJ767aHhQDkAO96BhvVfPl0QkxXcrSn87C6yBtD3z5R2hkgtVs-__t-7_Ee74boXOXGjw5dLBjOI1tmHsbCl52EBwP57NIU6TFPZP1N6vQKSWYtkp0JYX1fzNDM_7t_j5wsQg18W78QVqG2yyw5MOraND5lcxNd-3QHeRoxtqsUMikznB3bFi79kUmSxU8Lhrdw7oEQdUhWzoYd-ojLdAEW4um6o47iLse_5YqhTnLpWrYrn6KlqM3AMXzNSoWEv4lsuVXFIszKshInFKwlcARnPNCjBYG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
هنوز داری دنبال لینک می‌گردی؟
✅
حرفه‌ای‌ها مستقیم وارد میشن!
با ربات وینکوبت، ورود به سایت فقط چند ثانیه زمان می‌بره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡
بدون فیلتر و دردسر
⚡
بدون لینک‌های الکی
⚡
فقط یه کلیک تا ورود
🎁
اگه سریع و راحت میخوای وارد شی، این همون چیزیه که دنبالش بودی!
🤖
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال وینکوبت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/SorkhTimes/131630" target="_blank">📅 13:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131629">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⚪️
سخنگوی فدراسیون فوتبال:
۱۴ باشگاه گفتند بازی‌های ما را ۳-۰ کنید!
🔺
سازمان لیگ مصمم بود لیگ برتر را برگزار کند و روز ۸ فروردین به باشگاه‌ها گفته شد که تمرینات را آغاز کنند. با این حال ۱۴ باشگاه گفتند که در لیگ برتر شرکت نمی‌کنیم و بازی‌های ما را ۳-۰ کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 712 · <a href="https://t.me/SorkhTimes/131629" target="_blank">📅 13:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131628">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
قرارداد علیپور دوساله دیگه تمدید شد
❌
✍️
باشگاه پرسپولیس مبلغ قرارداد علیپور رو افزایش داد و با این بازیکن برای دوفصل دیگه به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 743 · <a href="https://t.me/SorkhTimes/131628" target="_blank">📅 13:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131627">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdYLmgumIu5t62xHh7OUcWoLd3NQUFDMsx_7ZCt0IpWEQB1A2aOFROUs6NJOHhAXjf7iOx80cKZF2ed0DvCfnHVYFlGOHJrUD4HJfcWLqljJksi64Jx7tidOrZms2MQ_H7P8c3RTfFJ8M3hU37Ueg4srLjaDos32NwdN_HzkAZ2oc-4ylbhY3rLoaBpDrKyMwgROE_-Y1nxceXUdQt8TZIS-6XR3T44BDOoKaqX3Y2bvi_1uSF1yL7WZ_-hhsivV9dsKsIoQPrt43KlZ7DBiN8RcvofNLC_Mz4yEGjY3iK5z5hNbSRgcSTxMTSygDo3Y20SWaPM42O2OKHEXnxYl0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیغام عجیب بیرانوند به حدادی، مرا به پرسپولیس برگردانید!
🔴
به گزارش شهرآرانیوز، علیرضا بیرانوند که خودش را برای جام جهانی آماده می‌کند، نیم نگاهی هم به آینده خودش بعد از این مسابقات دارد. او از چند ماه پیش به دنبال بازگشت به پرسپولیس بوده و در شرایط فعلی که لیگ تعطیل شده است، او سعی کرده تماس‌هایی را با مسئولان باشگاه سابقش داشته باشد.
🔴
حتی با خبر شدیم که بیرو با محسن خلیلی رسما مذاکره کرده و آمادگی خود را برای بازگشت به جمع سرخپوشان مطرح کرده است.
❗️
پیمان حدادی هم در جریان این موضوع قرار گرفته و حتی به دنبال این است تا اگر پیام نیازمند قرارداد سنگشنش را پایین نیاورد، به موضوع بازگشت بیرو به طور جدی فکر کند.
✅
جالب اینکه بیرو به حدادی پیغام داده که حاضر است با نصف قرارداد فعلی پیام که ۸۰ میلیارد تومان است، دوباره سرخپوش شود در مورد این موضوع در آینده خبر‌های بیشتری خواهید شنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 847 · <a href="https://t.me/SorkhTimes/131627" target="_blank">📅 12:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131625">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMNBgeaY7EFKdLBkK4T01PcXs8nMrvvKlgxitOSYYape5aVducl590ehXjLQSlU1xMk1Ls7IMY2o-O7-QLYKxrNLwUWF3A-6Cu1O6RLr6C1naoYD-L0Nwd3qud60jUOSAy9sKz5Vu3Bag4VVFxw_9vLEi2M3zdEgQTtPuACZnaX-uL6gRqDXj8DI6MXWGd5PeWNXg55viEzGkgonVqt3OmLUGoli_1rZD-mNAyfHsnzb7mJCLS92Qfep_f_fMCNiVtfloThUeTII6OgmI3xWg62MnhDA3WDMGLU0fJLf05oSZ4PZ48OXqbghjAx3ZZ1h0XPO6kXwHdvqo0ZkbEzetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
معین
: قرار نیست واسه تیم ملی آهنگ بخونم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 799 · <a href="https://t.me/SorkhTimes/131625" target="_blank">📅 11:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131624">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imnd06OGd9hjAReiUTSE_SblGValyMjHtcEeYKnHFq6-I8IMMWR6jsl_G9PvSI4Va_QjT-DqpLkIQG3iTvuF_LriflUoYg4BH2CJJ-O6v-u6qLLaHzagZPqivGJqc-R24TIh7Vkxfg-KGMo_7QA34bHbTbg4C969sWrj3WdPjfK28nvjRtmKVWOkkBgVYHB6TFrmcBJ0OOUG6UHZfBBsEX2YyrrpZa_xwRJWNaaTg9gVjW9IfVcJBrjY_Boz60Nei41vkNL2Zgjcxb6b_24sGN29bO53CxLlL4xMvFtWOMqDbCY2OLI95BD4wBPIbNs041I_8spB0_hfDqOr-wNL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت اینکه مدیران پرسپولیس بتوانند از لحاظ مبلغ قرارداد میلاد محمدی را راضی نگه دارند وی به مدت دو فصل دیگر با پرسپولیس تمدید خواهد کرد و درغیر اینصورت به لیگ ترکیه یا لیگ یونان سفر خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/SorkhTimes/131624" target="_blank">📅 11:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131623">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD8D1haQ2OFY1aM6lw4sInqPGv0nWTEQQp-k5JyNMqdT7bmi8WfnP0b3whze7Ljrf2_CFW9HMORwhOuHfsRAAZKmOS9MYt4fCnFX9QF8-IQqtN54ueo6siSfL-PxmcK0UnROUiiVuYIKjaaw3uXTNrB4usSTI2VKMjLnok52Frph2LFOi-T-1QK4Qo2miOPOvoLbOwEKl72_R4uEN96jBCNRS4FHsl65ENyluvlB0ddbQXhRJnmTSaQvW37cpdUAOY3Emmijs1LHE_oDLDoca10t326xijFkejtYHppshQAHjJu6PhvrrAM-jtfsKIDQePrXeUmN84p_iCq8qTa7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تسنیم: قرارداد باکیچ به طور خودکار تمدید میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 749 · <a href="https://t.me/SorkhTimes/131623" target="_blank">📅 11:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131622">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx9-v-rv58_CEAARuj4zWQUagAz0sWkobXbZfiZF9C3J3WxiW3JpN5IRtqzuNXlokCl1VysoAVaiXwfVLjtp4Ug5JRiyUHXq4D4k0MW8i5Bn-6B_kcuxGzsDcqYeIc4NZYGgeRzhBC85h88Zx2hnSDQKklO9obE6aTgXaui1ASMTtEK8hdgmA0p-iJB9zAX0GeHkQ5_hk8dcbFbCxRjjZC-_Ogo6PCV9OhVOTngRKEzpLqUK92YIlctxXqHcOUaJxOjuQOYot-fyba5IJdjUU6uz65yfvifS5_UcrhZd6o-MOFqRNrwL1tY_vPchAXzv9cqyE2AbTCNBApdd7APS8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
۹۰٪ کاربرا هنوز اشتباه وارد سایت میشن!
تو جزو اونایی یا میخوای حرفه‌ای عمل کنی؟
✅
ورود سریع به وینکوبت فقط با یک کلیک ساده:
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
نه لینک اضافی
📌
نه سردرگمی
📌
نه اتلاف وقت
📌
مستقیم، سریع، بدون دردسر وارد شو!
⏳
دیر بجنبی، از بقیه عقب می‌مونی.
🔗
الان وقتشه مسیر درستو انتخاب کنی:
🤖
@Wincobet_bot
📌
برای تحلیل بازی‌ها و آخرین اخبار سایت جوین بدید:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/SorkhTimes/131622" target="_blank">📅 02:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131621">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🛜
یک عدد سرور نامحدود ۲۱ روزه Anyconnect موجود شده فقط 4.5T  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/SorkhTimes/131621" target="_blank">📅 01:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131620">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🛜
یک عدد سرور نامحدود ۲۱ روزه Anyconnect موجود شده فقط 4.5T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/SorkhTimes/131620" target="_blank">📅 01:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131618">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToqT7fBiO-FV3qXSOhKvliGhjoqlA7ktGxbRRnwuX-uPM0yZSdB4PqQXmR3xb88ErzRiX8LP1wqQ6jrq7BO1xZRPbVgFTCAp01iDH4n1igqxiq_IiCRGIoMfrDOFdoWPmww2kjohjrn7pZKo7X0Bc6hzyhXF_8M1FzqptBzstcV8hHhDd_pCysqcTVJnxo3h8qlGU7X0N7Y7vhkKo9AtZuRIYcsf1PnI1Ib4KgngdwENbtB5bnb90c5uFYJWdTOfgLMlvW1ueesFCqfYLwykj0IJH_MBkChWiUU22Ze7QimiaD9GItJKxEZwWiJ4voo7by5L1pkttuV0WcMM89QPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مهدی تاج: شنیده ایم معین برای تیم ملی تو جام جهانی قراره موزیک بخونه، ما دخالتی در این موزیک نداشتیم ولی ازش حمایت می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/SorkhTimes/131618" target="_blank">📅 23:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131617">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK9QmQan4BPjEqSiN41QSk6Hs4gqxlf_ZNgyFLId-CnVRCDKv7C1zDlB7YxNQS8JALcyPU-GUddj3cfJbLZlcQFv7EnQzvASmlAw3sEcm4-mqmXqb27oSQcbbLUZ2e3sqnLGgDftVhHkKsfuwRjuKsb1Y77jOqQgQX5SJLMmTcDSbVhF6mXMO75nzXR6Mf1sfqkPbjO3Bm6_WXcn5TF63KpZL4doWAjJbgab5egkG7sjmnaFOGcwVGPBaR0t1DvVfwfkcvDDaklA9bWiaki568G14cdpXSbTIbIV6yPTIHHmEa9AaF3s4Ti8RcU8TRJqKSlByyDXBUguOSE2ctSSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
از کیت جدید تیم ملی جام جهانی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/SorkhTimes/131617" target="_blank">📅 22:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131616">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⏺
خیلی شیک و‌ مجلسی روی شیشه دفاتر پیشخوان آگهی فروش اینترنت پرو میزنن که تلگرام هم روش بدون فیلتره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/SorkhTimes/131616" target="_blank">📅 21:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131615">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siZBlXWL390Yk1tVA1ov7NCSi9fH3F1jd4jHtnqBaPhErJU42hjlNVQphVJ1cJ-uCiFkBxgnHfESrnnwXZHFtNfwnA-xRvvoGR81q5fLLSqnozJoC3w7tfZyG7Ht3L7BzSyMIzhQ34hmy8D27MlEGbpEefvaODLgpsT3dgS7wXaNEvhJ7el05FbCaQuJn7rDYjE6HlMArtNj0IYxLI4eHKQ4aszXQCQhajmdwGZi99q7n1fPH869uSUmZYsk1xzjHebJPBMKQplhEyYfz3E8_U6m_HfARrGnoPmxTMA7Y7NYp9ShJtoRLKrGgNueHZHkhL5YnzfcV52yhPBIdWRp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
خیلی شیک و‌ مجلسی روی شیشه دفاتر پیشخوان آگهی فروش اینترنت پرو میزنن که تلگرام هم روش بدون فیلتره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 920 · <a href="https://t.me/SorkhTimes/131615" target="_blank">📅 21:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131613">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2QIS2bpQ-eXA-I051h_0tvpImOOrJKPTscPyX5oALQb10Y0Ey_RqUM-AIGvRZI8zgrPnP_bwPqgHenjRLMhO2TM0Bs7BPYH4ayLMLm6uRQ9Dp7gTVNITpf1r_BYAsLxEEIoWtTBIE88POyuX0qJW-WECYZgD2dZybnKFwMLWodepX9qv9yUviP8N1Tw4PUDRM2Lrn341qCzGzGPaYeNIoxKsxRpPSyNWTnMxbHYfIJrVs-AS9pDZPesSB1LxbjlOTmH0xMEad0vnoSiiIPLZbFej70O89RIcAPYvjA95eB_ROsHKZGdH3IxSi_1lBnS17xiHppudOWDVQe-bs_q5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنای تیم میلی کنار پزشکیان عکس یادگاری گرفتن و راهی جام جهانی شدن!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/SorkhTimes/131613" target="_blank">📅 21:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131612">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
معاون اداری و پشتیبانی وزارت ورزش و جوانان اعلام کرد که برای حضور قدرتمندانه تیم ملی در جام جهانی ۲۰۲۶، مبلغ ۴۰۰ میلیارد تومان بودجه در نظر گرفته شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/SorkhTimes/131612" target="_blank">📅 20:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131609">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
توافق پرسپولیس با مهاجم تیم ملی فوتبال ایران/امضا قرارداد قبل از اعزام
🔻
پیمان حدادی مدیرعامل باشگاه پرسپولیس پس از تعلیق برگزاری ادامه رقابت های فصل جاری لیگ برتر با اوسمار ویه را سرمربی برزیلی سرخپوشان پایتخت برای فصل آینده به توافق های لازم برای تمدید و جذب بازیکن در پست های مهم رسید.
🔻
حدادی در نخستین گام برای حفظ یکی از مهم ترین عناضر خط حمله این تیم پای میز مذاکره با علی علیپور نشست تا مهاجم تیم ملی ایران را که از مبلغ قرارداد فصل جاری خود با سرخپوشان ناراضی بود به تمدید آن برای دو فصل دیگر متقاعد کند. نشست هایی که بالاخره نتیجه داد تا علیپور راضی به عقد قرارداد فصل آینده نیز شود.
🔻
مدیرعامل باشگاه پرسپولیس تصمیم دارد تمدید قرارداد این بازیکن را قبل از اعزام تیم ملی فوتبال به اردوی ترکیه که هفته آینده خواهد بود، انجام دهد تا اینگونه نقل و انتقالات تابستانی سرخ ها را آغاز کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/SorkhTimes/131609" target="_blank">📅 19:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131607">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/SorkhTimes/131607" target="_blank">📅 19:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131606">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/SorkhTimes/131606" target="_blank">📅 19:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131605">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRH9UbNngyJwggIwzex6vYlzcXena5QOsaAdq8IeNKhYnCmgkVQ2kWs6yUz1hQMr3MXyjqHPHTBAURAUwHST7ZrR6PZgc25u_xwNNHGHInD00yd__xLh9UrQmaKxY6Qn1TKDJNnsgRYzMTkWPfkjdR650IzMJrHDa5xxM2snEE0Deej0hntZKt4FLuTDixNRLPcXPnICafviIfop_fwjGoMvOSVC7hWMfTcUMzhxGs9-Ad3cHp5uaBCGQtGcHQOXCE0yvj2SuRVaPC_Q8Jc92Lp7qXaaQAgu_CAk3UQMVMJciReYk_C9kQZ_le1R56pSvMcFE2MrrUppQOtFKSlglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت علی بازگشا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/SorkhTimes/131605" target="_blank">📅 17:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131603">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♨️
🚨
نیویورک تایمز:
قصد ترامپ از تغییر نام عملیات «خشم حماسی» به «چکش سنگین» این است که یک عملیات جدید 60 روزه حمله به ایران شروع کند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 865 · <a href="https://t.me/SorkhTimes/131603" target="_blank">📅 16:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131600">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D08rQxvubThYkVGPYCdPRGLCE1MOSgn9KPyYqYwWKKkR1l3eKXWG40OUITECe5r_MvVx60UxtSEtUuXM7GXEJFbqZQtGwKKeqLs33og8nJBv5bXYLHM7wQ8xwo4vcnbIdrvpogmzVyTDgBDKa27PZRBOncO92YS0ikHNNSVnXufMye1sQvd3kz3wft_cK9QB47w2wvaztVIabg-1nN-fcsgdCopp8Th9TjrtIerEDnUyjhRcJx21dj5Z1nvqVOa6a93hkwZxTVu2ESc1hwuUfXPV0d5rHVVHjc4kfiSiubL91mEvLuAkMQmJ969j6N21cdilYMOZnJHR08YMKrHiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
قرارداد علی قلی‌زاده تا سال ۲۰۲۷ با لخ پوزنان تمدید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/SorkhTimes/131600" target="_blank">📅 15:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131599">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3YWwhu2funH7Cv91m_PmZHPI-aU8SdB9jyg-9uemLLlN7vC9R5lZWwjWQ6U_-XU6rrffI_zkJmsIh-THzgWI4PHijhNkeMdUsYMplAr4i5KxvPDW-RWJdyl-2Hys2wN3sasnPCHjNvJLbp7Orf6Xhe2_qXiNtPCKpFVvmouqCk8VFdhn8TJPFGI9Sn7m7XHUci0XflHg5fzhnJMgczSJQIhamcfiuRR-85kjwVqdUHEDKErKNSgrjZkjuh6GBL0kAbNzHCgZufxczmhVz7QlsteUbFsvIUVh6yyWmdmEuc5L50sMDbr9UqP-23LpWARwvN6CtD8B6J3Ycal5dfLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن مسلمان به کادرفنی تیم امید پرسپولیس پیوست
مسلمان با پیشنهاد بهادر عبدی و بعد از جلسه با ادموند بزیک مدیریت آکادمی پرسپولیس به عنوان مربی به عضویت کادرفنی این تیم درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/SorkhTimes/131599" target="_blank">📅 15:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131598">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzvYHd-tGKXlIUBzWtNfodFTz_TLjngpKq00ll_bpc7gkEsv7jx8kB4mBd6w0EXGZ02yKIrGHOFcNs62AFadMYQBXdpsN_EEhbZqH2IVjVSV-Xhlcmrl8Aus47TeYWBfLc4Gcti-8Vg1nRSws8umznFY8Ypq19vuNuHbOC9oOF7uVVo_GkD8aTPI8whNIais2WF3w4C46bg51Jg1dE88QCl2rvL0qWduKMGEW4iB_6ZHq1gCyVrOi7Dir3qgU-tXwqYZw6zmwS5bFNZaDZRfsth48Ay2yv6HKLC3_r8iqtwsC8jHbtwS-_lwXOpZBc9Zg4OgZA__9xRhmwyDj-lIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیگه لازم نیست دنبال لینک سایت بگردی!
📌
فقط با یه کلیک از داخل ربات وارد وینکوبت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
سریع، مستقیم، بدون دردسر
📌
بدون نیاز به جستجو یا لینک‌های پراکنده
📌
همه چیز داخل ربات آماده‌ست:
▪️
ورود فوری به سایت
▪️
دسترسی راحت از تلگرام
▪️
بدون مراحل پیچیده
🔗
ساده‌ترین راه ورود به وینکوبت همینجاست:
🤖
@Wincobet_bot
📌
میخوای با تحلیل جلوتر از بقیه باشی؟
برای دریافت آنالیز بازی‌ها و ورود به کانال وینکوبت همین الان جوین شو:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/SorkhTimes/131598" target="_blank">📅 15:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131596">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❗️
کامران غضنفری، نماینده مجلس: شواهد و قرائن نشان می‌دهد که آمریکا و اسرائیل قصد انجام یک عملیات گسترده برای تصرف برخی از جزایر جنوب را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/SorkhTimes/131596" target="_blank">📅 13:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131595">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
ترامپ رسما اومد گفت انقدر صبر میکنیم تا ایران تحت فشار مجبور به توافق بشه.
❗️
یعنی ممکنه تا شهریور تو همین وضعیت بموییم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 948 · <a href="https://t.me/SorkhTimes/131595" target="_blank">📅 12:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131594">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/SorkhTimes/131594" target="_blank">📅 12:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131593">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🔴
شنیده‌میشود محسن‌مسلمان فوق ستاره سال‌ های نچندان دورباشگاه پرسپولیس بزودی به کادرفنی این تیم برای فصل بعد رقابت‌ها اضافه خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 974 · <a href="https://t.me/SorkhTimes/131593" target="_blank">📅 11:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131592">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHM13vUBscPmMqRcDBYZNw6vaQVST5uleaRp_ew25S7sgLIU29Rr01f4_hjjo9VRG35MbjPcHjRtv1dGBQwJmsTZ2_IJVsyL1N8iobLoGVCX9JgBTOYqpu2neW7fpLS4OPKeQaTUd8OlPn_yypfVTl-UHXyPZcAv_00NV8OvTVuW_UVYAcSXoRLR38ghz1VUi_TSVroP7q58lCzj3-OWPcBH6q22YHA1IVzYKN5UqjMpYA41nu3WeaXKKl1mgj65H0wwGkxaJwHbLOyzYP6IQU4kGT9Bqbo3sOib8zLX42bNyPyFeu_Wcgb0YAdHmKZ1Tcco8nUUCqKToFKib7cyCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پپ گواردیولا:
من بی طرف نیستم من طرفدار فلسطین هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 956 · <a href="https://t.me/SorkhTimes/131592" target="_blank">📅 11:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131590">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
🔴
مارکو باکیچ تابستان گذشته با قراردادی «۱+۱» به پرسپولیس پیوست که طبق بند الحاقی قرارداد، فعال شدن سال دوم منوط به حضور او در ۶۰ درصد مسابقات رسمی فصل اول بود. با وجود مصدومیت این بازیکن در اواسط فصل، طبق ماده ۵ آیین‌نامه نقل‌وانتقالات فیفا، مدت زمان مصدومیت از مجموع مسابقات قابل محاسبه کسر می‌شود؛ به همین دلیل باکیچ از نظر حقوقی به حدنصاب ۶۰ درصد رسیده و قرارداد فصل دوم او به‌صورت خودکار فعال شده است.
🟥
در نتیجه، قرارداد دوساله این هافبک مونته‌نگرویی قطعی و لازم‌الاجرا محسوب می‌شود و ادامه همکاری او نیازی به تمدید یا توافق جدید ندارد. همچنین اگر پرسپولیس قصد کنار گذاشتن این بازیکن را داشته باشد، احتمال محکومیت باشگاه در دادگاه CAS بسیار بالاست و باشگاه باید کل مبلغ قرارداد را پرداخت کند. از سوی دیگر، تاکنون هیچ نوتیس فسخی از سوی باکیچ به باشگاه ارسال نشده و تمام بحث‌های مربوط به «مشروط بودن» قرارداد، با مفاد توافق و استانداردهای فیفا همخوانی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/SorkhTimes/131590" target="_blank">📅 09:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131589">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FthPax5d4ymQ8YsyX_Fl_HUzelloNKHWNKvDgdUzvw1YOklg2HICb9bgMFBiKrr40LyMosqQdOUnx-SYJ_rl7fe0H-_Np18XG4F7NRsGLgctu2oX92cKcrFcQ2QkxwPIqU0sWEsvjNRgduXfBMcKBIsYp35ygPvt9yxwLsWd7avSgXEY5_wuP79MLIhxrcpTLoeeaKVAE0nyna1Ns2zBmzeZSp7oP4C5pNco9b4cAAeIHvLYFmo2q1wuw9DS5ENYucCgFORNdedGDISH9RO67Ft64Z9t1dkpdbRRYLLtiTRCIh-OUVpDGDjmIVdk3cFRIDAF0cnm-7oPQqL7XYV06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/SorkhTimes/131589" target="_blank">📅 01:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131588">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
همین زلزله رو کم داشتیم وسط این همه تورم،جنگ‌ و بدبختی، فیلترینگ و قطعی اینترنت!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/SorkhTimes/131588" target="_blank">📅 00:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131587">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
جزییاتی از زلزله شدید تهران   بزرگی و شدت: ۴.۶   محل وقوع: مرز استان‌های تهران و مازندران، حوالی پرديس   زمان وقوع: ۲۳:۴۶ عمق زمین‌لرزه: ۱۰ کیلومتر ۸ کیلومتری پرديس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 948 · <a href="https://t.me/SorkhTimes/131587" target="_blank">📅 00:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131586">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GmQd6HxE2jO5U_UFfnugLljS0I13sL_h-R3i7YTkTR3oy4Cf_tqjEc3Oj2qETGOOygy87qr9vlhvCDTNgsbhTJtVIu47sYwmhmQ7yTMeAwPY5EJHQjlijJZYkqpLlxz6xUMdFGdS5B8QFJuKnLz0AU_wFDdOx7lXX4v0aVcsG8tOttsaPxk_v3yzKN-IPmuksadaz_OB0OJR7bsdIZRRg-98GQ9TZejL3HI4FlmI6Rd5umNV229pDW10OJS-mg40CrEvu4TsdNwyGuzeJnB6CiO5jznRP16utnMvAm5_InRUJiyO1872rFzXd2sNXlmdg09oPH03xe8mZSCqkmelrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جزییاتی از زلزله شدید تهران
بزرگی و شدت: ۴.۶
محل وقوع: مرز استان‌های تهران و مازندران، حوالی پرديس
زمان وقوع: ۲۳:۴۶
عمق زمین‌لرزه: ۱۰ کیلومتر
۸ کیلومتری پرديس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/SorkhTimes/131586" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131585">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
کانال ۱۲ اسرائیل:
🔴
انتظار می‌ره که ترامپ بعد از بازگشتش از چین در پایان هفته، تصمیمات نهایی و جدیش رو درباره ایران بگیره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 946 · <a href="https://t.me/SorkhTimes/131585" target="_blank">📅 22:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131584">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/SorkhTimes/131584" target="_blank">📅 22:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131583">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
درگیری لفظی چندین خبرنگار با فاطمه مهاجرانی بر سر قطعی اینترنت
🔕
مهاجرانی: ترامپ گفته آتش‌بس به تنفس مصنوعی وصل است، کشور در جنگ است! امنیت مردم مهم است و تا وقتی سایه جنگ از کشور دور نشود وضعیت اینترنت به حالت عادی بر نمی‌گردد!
💬
وقتی مردم اینترنت ندارن…</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/SorkhTimes/131583" target="_blank">📅 22:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131582">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=JTAjPlezYVnDda462mra1Q_8oSs_XUzvXyjPwEUnP2i3OVnDguSgDfLaRQn1xg5HlBU1CkJ8ga_QkYlJvCTl7eqpRnOl3L3mhq7wrpyBzImW2JXKUf5HKyyo83xaTgRJJRXKy6VUpyiaWrmnM09Ec13CDXyS_Zrwcor3QN65dc1_qTqOPA3XTqnmgw2c_5_0vsZHu3XyhMoUrb_MeJSKZypbgrrLNeLvZiLb1QLUm24m_M796Rkr7REc4HNstgCoTT-VJ-qVAE19iAxacC1soI4Ta-7oyy6dL8mzoRF-pRNc36QYV6jJkpJL_MY5uDwYFX5OT-oTlBlKoTp1VOkP4K88vSUhX5thB4tftroHIyvvwLB6RyWDW5vKc4KCurIcjGpzPyCIcIyVWWHszgyEao4I5mgWzosueJvTcd5ioCIVQ3NuJdPvFSMNDA0qIG3i4PMLj27wZd4J23TZaoq0LGbILUWpZBcfGrRDZGGaYij9EIDsiU0CtxD3fL7rNyH5W3e6Q4Me8Yi0IHvvBtAwB52vfpqj7dhzBROQ8wjoWmHe7MofcOBRXJUK6ut1kHwAO9dSQO7zGe8HjmXVYnXh9QStFbYxWQvrZzAhADodWCoeMoDklHKPm14wPoxBpTVoSKPOTwisN8y7_lMUDwpdeRVXfiImgjksxhvXQ5b6whw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=JTAjPlezYVnDda462mra1Q_8oSs_XUzvXyjPwEUnP2i3OVnDguSgDfLaRQn1xg5HlBU1CkJ8ga_QkYlJvCTl7eqpRnOl3L3mhq7wrpyBzImW2JXKUf5HKyyo83xaTgRJJRXKy6VUpyiaWrmnM09Ec13CDXyS_Zrwcor3QN65dc1_qTqOPA3XTqnmgw2c_5_0vsZHu3XyhMoUrb_MeJSKZypbgrrLNeLvZiLb1QLUm24m_M796Rkr7REc4HNstgCoTT-VJ-qVAE19iAxacC1soI4Ta-7oyy6dL8mzoRF-pRNc36QYV6jJkpJL_MY5uDwYFX5OT-oTlBlKoTp1VOkP4K88vSUhX5thB4tftroHIyvvwLB6RyWDW5vKc4KCurIcjGpzPyCIcIyVWWHszgyEao4I5mgWzosueJvTcd5ioCIVQ3NuJdPvFSMNDA0qIG3i4PMLj27wZd4J23TZaoq0LGbILUWpZBcfGrRDZGGaYij9EIDsiU0CtxD3fL7rNyH5W3e6Q4Me8Yi0IHvvBtAwB52vfpqj7dhzBROQ8wjoWmHe7MofcOBRXJUK6ut1kHwAO9dSQO7zGe8HjmXVYnXh9QStFbYxWQvrZzAhADodWCoeMoDklHKPm14wPoxBpTVoSKPOTwisN8y7_lMUDwpdeRVXfiImgjksxhvXQ5b6whw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صالح حردانی میگه ملی‌پوش‌ها از سربازی معاف بشن تا با روحیه بهتر فوتبال بازی کنند!!!!
◀️
شما چه گلی به سر کشور و مردم زدید که درخواست معافیت دارین؟ کدوم قهرمانی رو آوردین که اینقدر وقیحانه درخواست معافیت دارین؟ چرا یکبار درخواست شما، رویکرد مردم نیست؟ چرا همه چی رو فقط برای خودتون می‌خواهید؟
❌
جز اینه که هیچ جای دنیا چنین پولی رو به شما نمیدن؟ هیچ جای دنیا به چنین ثروتی نمی‌رسیدید جز ایران!!! باز درخواست معافیت سربازی دارین؟
🔴
چه تفاوتی با یک جوان کارگر ۲۵ ساله داری که اون باید بره سربازی و تو نباید بری؟
⚠️
تازه سربازی شما که مثل بقیه مردم نیست، میرید تیم ملوان یا فجر و بازهم فوتبالتون رو بازی می‌کنید. خبری از پادگان نیست. چرا همیشه طلبکارین و سیرمونی هم ندارین؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/SorkhTimes/131582" target="_blank">📅 21:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131581">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/SorkhTimes/131581" target="_blank">📅 21:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131580">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/SorkhTimes/131580" target="_blank">📅 21:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131579">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f2cd4206.mp4?token=INQRTbqEzDrAHGTY5xjSxAFmEpiq_lepvu2gT3LJyWDUGKsesmwgWmx8lWSt_Ul3pRsDlpkZJMObrVFqcQGVq-ck_ue7uckF4fK6LOqvEwVQZTH746fI2pight_CNU5PBGZ2v93e8tRqqBX9JN4OikcNVZPJff6-AyiTDpfeYf1nqS8w_GAQFLHtcWjy10WOPda8MpujMoImILtj0XO_MYgSuH1BzG9rhpX9MmydmZQNQ-Fw2STSnLTrDVlOXhiw6OaARANKJvBu-8ndIoyxfO2pEZaUC-k30fILVMdAE7nppNxM6pMBbToMNn9CMYqksrM2t-Di9wTSa33PzIppzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f2cd4206.mp4?token=INQRTbqEzDrAHGTY5xjSxAFmEpiq_lepvu2gT3LJyWDUGKsesmwgWmx8lWSt_Ul3pRsDlpkZJMObrVFqcQGVq-ck_ue7uckF4fK6LOqvEwVQZTH746fI2pight_CNU5PBGZ2v93e8tRqqBX9JN4OikcNVZPJff6-AyiTDpfeYf1nqS8w_GAQFLHtcWjy10WOPda8MpujMoImILtj0XO_MYgSuH1BzG9rhpX9MmydmZQNQ-Fw2STSnLTrDVlOXhiw6OaARANKJvBu-8ndIoyxfO2pEZaUC-k30fILVMdAE7nppNxM6pMBbToMNn9CMYqksrM2t-Di9wTSa33PzIppzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/SorkhTimes/131579" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131578">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🔻
فیفا یه قانون تصویب کرده که بازیکنای خارجی که ۳ سال سابقه حضور تو لیگ یه کشور رو داشته باشن، میتونن واسه تیم ملی اون کشور بازی کنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 923 · <a href="https://t.me/SorkhTimes/131578" target="_blank">📅 20:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131577">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3nVw2kUPyxd9-g-3eTg7vcFyL7YKOBDeDMGO3hS-Kf3TPJ5fFvbechHy9bN5jmvS5VQfQSDu5axmxxDdtB9APPaVcjUJ5C7LOC0lEoS-N1v3C3pcgiuzWJWP182WUTYOnISLE6_YSn9WseD4nui-iexYlN4ix2jqKEDi9HON2DcPrX8W_3Vb77LlFu11p8NffleR4-mG9fKb-Px-AN-EWtimSUxOuu_R1-VFrGuzizJD0XPe0hlde7Bsu45EsHiZ11FVsbZJAU5PaZk98mTYchQzHyMfGpl8R0EhKiyqTi6fznbpPI850uoB5tRAkxxeAjRTjGzIz4L54WjeUX53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
پزشکیان توییت زده قول داده اینترنتو وصل کنن
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 919 · <a href="https://t.me/SorkhTimes/131577" target="_blank">📅 20:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131575">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
باشگاه پرسپولیس کارهای تشکیل تیم دوم خود را انجام داده و «پرسپولیس ب» در لیگ دسته دوم فعالیت می‌کند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/SorkhTimes/131575" target="_blank">📅 18:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131574">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚪️
تاج: تیم‌های راه‌یافته به لیگ نخبگان و لیگ قهرمانان را انتخاب خواهیم کرد
🔺
شاید بتوانیم مهلت معرفی تیم‌ها را یک ماه عقب بیندازیم.
🔺
۱۴ تیم مخالف برگزاری ادامهٔ لیگ‌اند؛ موافقان پرسپولیس و گل‌گهر هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/SorkhTimes/131574" target="_blank">📅 17:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131573">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dalVW2AxaAjyDh6PZGmgrE09MhMwajQ3OlXFvhNtO_bGrGvlWrVAkzTFHFuXxwyY8Lk6qeu5KKaVYFlJIx7MP95AGCo-XeVoIwyVlFzFMEaU5qmi21nMbqDcDLfzDDxrH8jNsQN2EPbgcoH_n6bNUbNJ01yQVJERJOljydEtjDb-TVJrBzz8y2j9wrcNIVlg4VbKLN-Blh9Ab7qH9zZhAw87DSNseAH52-umUMrzIXgC1yIXOL5WZvD7fkKa8gNJxuddxmzymUsho7X0OG7FmeIi9cthRsBMA52ExH8HrKzf_P7rQFVtsIO_rwOEhINfBV6u89G6WOZcOAJqHq71xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اختلاف میلاد محمدی با مدیران باشگاه پرسپولیس تنها 3 میلیارد تومن است و مدیران باشگاه پرسپولیس قصد دارند با پرداخت این مبلغ قرارداد محمدی را تمدید کنند
/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/SorkhTimes/131573" target="_blank">📅 17:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131572">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس خواهد ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/SorkhTimes/131572" target="_blank">📅 17:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131571">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/SorkhTimes/131571" target="_blank">📅 17:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131570">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5Ym1yrY3vf3vvA9QOPHf-sKvcd0w4vfFvWCbcpokpCWhuB2lvXpHREeS5Au1NqSaNwJFYdOXuQWqgrTWRvC1cpY4eYycWNb1T1otSWMfaRIMZD0V_nm_ZD2KgaOxHlxgLjoKLdwfSTCADpB6tlYSLxYpzWnQeLCnOW5wjNFWNgvGK_ULRhj7yQGucPb6P50kQXGkUGij-qovuxhuA94EE122PBxTryslMGiM09o0PtHOkCmzATachlVZTP9JfKjqqCy0kmR951inNhe3udto_rey3cqDZQoAw_5uGY_N4pCjeEFXBwKIvukGPHBwUvCtdZCiQclNIhbyL65q7wxJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شباهت عجیب لوکاس برالدو و محمد خدابنده لو ستاره های خط هافبک پرسپولیس و پاریسن ژرمن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/SorkhTimes/131570" target="_blank">📅 17:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131569">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/SorkhTimes/131569" target="_blank">📅 17:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131568">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/SorkhTimes/131568" target="_blank">📅 17:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131565">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⚪️
ترکیب دو تیم تیم‌ملی برای بازی درون تیمی
◽️
تیم سفید: علیرضا بیرانوند، دانیال ایری، حسین کنعانی، علی نعمتی‌، رامین رضاییان، روزبه چشمی، امید نورافکن، هادی حبیبی‌نژاد، مهدی محبی، آریا یوسفی و علی علی‌پور
🔻
تیم قرمز: محمد خلیفه،‌ شجاع‌ خلیل‌زاده، عارف آقاسی، صالح حردانی، احسان حاج صفی، عارف حاجی عیدی، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، امیرحسین محمودی و کسری طاهری
⏰
ساعت ۱۸:۰۰
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/SorkhTimes/131565" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131564">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
درگیری لفظی چندین خبرنگار با فاطمه مهاجرانی بر سر قطعی اینترنت
🔕
مهاجرانی:
ترامپ گفته آتش‌بس به تنفس مصنوعی وصل است، کشور در جنگ است! امنیت مردم مهم است و تا وقتی سایه جنگ از کشور دور نشود وضعیت اینترنت به حالت عادی بر نمی‌گردد!
💬
وقتی مردم اینترنت ندارن کسب و کار ها با اینترنت پرو چیکار میخوان بکنن رونق کسب و کار اینترنتی به مردمه.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/SorkhTimes/131564" target="_blank">📅 16:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131563">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
شهبازی مجری شبکه 2 : اگه اینترنت،تلگرام بدون فیلتر و مستر کارت میخواید و این چیزا براتون مهمه،برید همون سوریه،عراق و افغانستان
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/SorkhTimes/131563" target="_blank">📅 16:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131562">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
پزشکیان: نمیذاریم بعضیا از وضعیت جنگی کشور سواستفاده کنن و برای مردم مشکلات اقتصادی و معیشتی به وجود بیارن!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/SorkhTimes/131562" target="_blank">📅 16:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131561">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🚨
وزیر جنگ آمریکا: اگر لازم باشد، ما برنامه‌ای برای تشدید اوضاع در ایران داریم!!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/SorkhTimes/131561" target="_blank">📅 16:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131559">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJQJFm70TvNI5Kbl0YC3Ho04v2ToLCeegQGJX4CSNLipd5rGMtTvQ9_Q79BrWtc5PAy4ULUyMq5LLpL4aFENkoaPJYTuBBXPMXVviosRr6UOyclEY9vkR33r7f_46_lk-WRQeHv7eUjZlZoq4ifl0CxmElDq1SwQ5P57z95gIighyA4asEyMF3g85ArOeKiAV6iFUs-1yp5pAde2H6aHPod74aIGXh2_6fNDgHW1NUlPAFIKsYXAivOszfFsPDCGgC2ZtrqYTO8Hi2YyMWwEOG-Si-fJH1fHyiipFdNkRId0yjCFgrKYmVYbC9ITfbCDvq3VOUjCCCB0fyQH5YqW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/SorkhTimes/131559" target="_blank">📅 01:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnrHjDLpNcHC8fXMjUNOOwn2w4TM9OhuKO5K2ikHyZKuIqut40BUZ38d3XRuoRh2Fy295g1URDJkZEjtE0WlhgOjDjbTOuS0dAxlZoCHg6Y5tDa4FwH0_BuwPiyWxFz9X_pbYCWjXUvvhmy982vAFqZDYYH1HptyuxjrfSo4euqfZ5WRwql5-RbifsOsc3SJbgHdWM7bHpf6Lj3VqeOqNgY-2_pmmHha_VVU8KJBN9cOzmKxOaNhjxCMdSKWQ2xPXR5iynvt1631541IBP6J7fvj4S4soa9YKnenrRE5QGgFijwD2ac46lScrT-2pTk_OYcDoSHerK8lIvoREZr6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سپاهان مجوز حرفه‌ای می‌گیرد؟
🔺
کنفدراسیون فوتبال آسیا (AFC) به درخواست فدراسیون فوتبال ایران برای تعویق در معرفی نمایندگان این کشور در رقابت‌های آسیایی پاسخ منفی داده است. این موضوع به شدت بر وضعیت نمایندگان ایران در لیگ قهرمانان آسیا تأثیر خواهد گذاشت. سپاهان،…</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/SorkhTimes/131557" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131556">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🟡
سپاهان مجوز حرفه‌ای می‌گیرد؟
🔺
کنفدراسیون فوتبال آسیا (AFC) به درخواست فدراسیون فوتبال ایران برای تعویق در معرفی نمایندگان این کشور در رقابت‌های آسیایی پاسخ منفی داده است. این موضوع به شدت بر وضعیت نمایندگان ایران در لیگ قهرمانان آسیا تأثیر خواهد گذاشت. سپاهان، یکی از باشگاه‌های مطرح کشور، به دلیل مشکلات مالی و عدم توانایی در تأمین شرایط لازم برای دریافت مجوز حرفه‌ای، در معرض خطر قرار دارد.
🔺
بعد از آسیب جدی به کارخانه فولاد مبارکه، سپاهان با مشکلات مالی جدی رو به رو است و هنوز نتوانسته مطالبات این فصل بازیکنانش را تسویه کند و احتمالا هم با توجه به میزان خسارات وارده، حداقل تا پایان سال بعد، قادر به تسویه طلب مربیان و بازیکنان داخلی و خارجی اش نخواهد بود که همین موضوع قطعا بر روند مجوز حرفه این تیم تاثیر منفی خواهد داشت.
🔺
از سوی دیگر شرایط اقتصادی صنایع مادر باعث شده وزارت صمت نیز محدودیت‌هایی برای هزینه‌کرد باشگاه‌های صنعتی در نظر بگیرد؛ موضوعی که می‌تواند برای سپاهان، گل‌گهر و چادرملو دردسرساز شود.
🔺
نکته قابل توجه دیگر هم این است که با توجه به وضعیت منطقه و کارشکنی مسبوق به سابقه از سوی کشور های حاشیه خلیج فارس
،
قطعا بازی ها به سمتی خواهد رفت که رنگ بوی ورزشی نخواهد داشت و این بازی ها یک میدان است برای دفاع از نام و اعتبار ایران و حفظ ابروی ایران بسیار مهم است.
🔺
در این شرایط، انتخاب نمایندگان مناسب برای حفظ اعتبار فوتبال ملی اهمیت ویژه‌ای دارد، تصمیمات فدراسیون، در روزهای آینده می‌تواند سرنوشت فوتبال ایران را رقم بزند و بر روند آینده باشگاه‌ها تأثیرگذار باشد/ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/SorkhTimes/131556" target="_blank">📅 00:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131555">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فوری ؛ ایران به شورای امنیت سازمان ملل اطلاع داده است که در صورت اعزام زیردریایی هسته‌ای آمریکا به خاورمیانه، سطح غنی سازی ۱۰ تن اورانیوم باقی مانده را به ۶۰ درصد خواهد رساند
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/SorkhTimes/131555" target="_blank">📅 00:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131553">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
🎙
میثاقی: امیرحسین محمودی با 5 بازی لیگ برتری جوری درخشیده که الان داره میره جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131553" target="_blank">📅 00:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131552">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
محمد انصاری که در تیم جوانان ایران به عنوان یکی از دستیاران حسین عبدی فعالیت می‌کرد هم اکنون یکی از گزینه‌های جانشینی او در این تیم هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131552" target="_blank">📅 23:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131551">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
میثاقی: کارهای اعزام تیم ملی به آمریکا برای حضور در جام جهانی در حال انجام شدن است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/SorkhTimes/131551" target="_blank">📅 23:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131549">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🛜
معاون رئیس‌جمهور: نظر دولت بازگشت اینترنت به وضعیت عادی است
🔹
حتی در شرایط جنگی هم بستن اینترنت راهکار درستی نیست، چرا که دیدیم وقتی اینترنت کامل بسته بود هم ترورها ادامه داشت
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/SorkhTimes/131549" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131548">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
ترامپ:آنها تسلیم خواهند شد... من با آنها معامله خواهم کرد تا زمانی که به توافق برسند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/SorkhTimes/131548" target="_blank">📅 18:32 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131547">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
ترامپ:
آنها تسلیم خواهند شد... من با آنها معامله خواهم کرد تا زمانی که به توافق برسند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/SorkhTimes/131547" target="_blank">📅 18:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131544">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJIcaohlBLVGfGrZfwJnqiLLw4sTWyj7dnxR1-z50i76OJSwJmjF4nCA5M85llj_3vzW-2h0BMvwgJpE88xRF6kw3GvI7YfDTc6WZ1l0SZlhSibyx5CEfIpYRIVT9s0mqVktsQwGJXG3R5eGbRRsT_2iuKHk_iVbeq74zAdIoxskIczkns5tiYvuMhtmH2MYqnSexCDgySt608fJC3GHxz8bfBsCr_YE4ZTtcA4m1xOrWaI2Aq7FlobV7wLmcofymMBke8blTNCsP4wqTPlUuQOn1Ald-wipLwUJaht0qsCVCdF6STcGG2ie-QrGO4V6XvsNvuIwzvunsINEiNB-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/SorkhTimes/131544" target="_blank">📅 17:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131543">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/SorkhTimes/131543" target="_blank">📅 16:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131542">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/SorkhTimes/131542" target="_blank">📅 16:32 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
سپاهان  اصفهان دچار کمبود بودجه برای فصل آینده شده و از این رو قصد دارد آریا یوسفی را به فروش برساند تا بخشی از هزینه‌های فصل آینده را تأمین کند. ///خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 750 · <a href="https://t.me/SorkhTimes/131541" target="_blank">📅 16:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131540">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
سپاهان  اصفهان دچار کمبود بودجه برای فصل آینده شده و از این رو قصد دارد آریا یوسفی را به فروش برساند تا بخشی از هزینه‌های فصل آینده را تأمین کند. ///خرمی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/SorkhTimes/131540" target="_blank">📅 16:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131539">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
هیچ فردی به کادرفنی اضافه نمی شود/ محمدی و رفیعی بازیکنان ما هستند
🎙
لیست مازاد در پرسپولیس شایعه است چون ما هنوز ۸ بازی دیگر داریم. میلاد محمدی و سروش رفیعی بازیکنان ما هستند و چون در تمرین غایب بودند جریمه شدند
🎙
با شروع تمرین در خدمت آنها هستیم. سروش رفیعی یکی از کاپیتان های ماست و حتما مسئولیت پذیری او باعث می شود در تمرین شرکت کند
🎙
از یک ماه قبل از شروع مسابقات تمرین را شروع می کنیم. در حال حاضر هیچ فردی به کادرفنی اضافه نمی شود. برای مجوز حرفه ای شرایط خوبی داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 755 · <a href="https://t.me/SorkhTimes/131539" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131538">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
🟡
نتیجه‌ای تصادفی یا سناریویی از پیش طراحی‌شده؟
▪️
سپاهان در دیدارهای اخیر خود نتایج عجیبی را ثبت کرده است: تساوی برابر گل‌گهر (دو بار)، شکست مقابل تراکتور و پرسپولیس، و بردهای حداقلی برابر چادرملو و دیگر تیم‌ها. این آمار بیش از آنکه تابع منطق فنی باشد، روایتی متفاوت از لیگ برتر را به تصویر می‌کشد.
▪️
در پشت پرده، پرسپولیس سیاستی شفاف اما بحث‌برانگیز را دنبال می‌کند،تثبیت سهمیه آسیایی خود، به شکل ممکن فوتبالی. برخی فعالان فوتبالی بر این باورند که هدف اصلی از برگزاری لیگ چیزی جز این نیست و نتایج اخیر تیم‌های مدعی در برابر سپاهان، نشانه‌هایی از یک طراحی نانوشته را به هواداران نشان می‌دهد.
▪️
اکنون باید پرسید: تکلیف معرفی نمایندگان آسیا چه خواهد شد؟ اگر قرار باشد تیمی با لابی و سیاست‌گذاری راهی قاره شود، احترام به ماهیت رقابت‌پذیری فوتبال کجا خواهد رفت؟ فوتبال ایران سزاوار شفافیت است، نه سناریوهایی که اعتبار مسابقات را زیر سوال می‌برند.
🔺
سپاهان ۱ استقلال ۲
🔺
سپاهان ۱ تراکتور ۲
🔺
تراکتور ۱ سپاهان ۰
🔺
گل گهر ۱ سپاهان ۱
🔺
سپاهان ۱ گل گهر ۱
🔺
سپاهان ۱ چادرملو ۰
🔺
سپاهان ۰ پرسپولیس ۱
🔺
پرسپولیس ۲ سپاهان ۱
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/SorkhTimes/131538" target="_blank">📅 16:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131536">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
بزیک، مدیرآکادمی باشگاه پرسپولیس و سوال در مورد همکاری با مهدی مهدوی کیا: من با مهدوی کیا مثل برادر هستیم و شروع کار ما در کیا با هم بودیم/ او اکنون با تیم بزرگسالان در امارات کار می کند/ لازم باشد حتما با مهدی مهدوی کیا کار می کنم و از تجربیات او استفاده می کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/SorkhTimes/131536" target="_blank">📅 15:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131535">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
🟡
حذف سپاهان و سفر پرسپولیس به آسیا
🔺
فرمول جدیدی که از سوی مسئولان چند باشگاه ارایه شده، احتمال حذف سپاهان از بین نمایندگان فصل آینده فوتبال ایران را تقویت کرده و استقلال، پرسپولیس و تراکتور را راهی لیگ‌های آسیایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 727 · <a href="https://t.me/SorkhTimes/131535" target="_blank">📅 15:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131534">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
محسن خلیلی: پرسپولیس
همیشه خواهان جذب
علی قلی زاده
بوده اما خودش نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 743 · <a href="https://t.me/SorkhTimes/131534" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131533">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
دیگه لازم نیست دنبال لینک سایت بگردی!
📌
فقط با یه کلیک از داخل ربات وارد وینکوبت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
سریع، مستقیم، بدون دردسر
📌
بدون نیاز به جستجو یا لینک‌های پراکنده
📌
همه چیز داخل ربات آماده‌ست:
▪️
ورود فوری به سایت
▪️
دسترسی راحت از تلگرام
▪️
بدون مراحل پیچیده
🔗
ساده‌ترین راه ورود به وینکوبت همینجاست:
🤖
@Wincobet_bot
📌
میخوای با تحلیل جلوتر از بقیه باشی؟
برای دریافت آنالیز بازی‌ها همین الان جوین شو
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/SorkhTimes/131533" target="_blank">📅 15:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131530">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
🎙
باشگاه برای توسعه آکادمی برنامه بلند مدت دارد. از شاهرودی بابت زحماتی که کشیده تشکر می کنیم. امیدواریم ریل گذاری که در آکادمی شکل گرفته ادامه دهیم
🎙
امیدواریم بازیکنی مثل امیرحسین محمودی را پرورش دهیم. سرپرستی در پرسپولیس؟ فعلا تا پایان فصل در خدمت هستم. برای پایان فصل و فصل جدید حتما در مورد سرپرستی تصمیم گیری می شود
🎙
جلسات ما با اوسمار هر چند روز انجام می شود. چهار روز قبل تماس تصویری با اوسمار داشتیم که در مورد شرایط جدید با او حرف زدیم. در مورد مصدومیت براجعه با هم حرف زدیم. اوسمار منتظر تصمیم سازمان لیگ است
🎙
او گفته در صورت شروع لیگ از اواخر تیر تمرینات از هفته اول خرداد شروع شود. جلساتی خوبی با سازمان لیگ داشتیم تا ببینیم بازی ها چه زمانی آغاز می شود. حضورم در معاونت ورزشی و سرپرستی وظیفه ای است که مدیریت به عهده من گذاشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/SorkhTimes/131530" target="_blank">📅 13:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131529">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
🎙
در مورد نیم فصل که بازیکن خوب جذب نشده باید بگویم که سرگیف را جذب کردیم. وقتی نیم فصل بازیکنی جذب می شود اکثرا قرارداد دارند. بازیکن آزاد در نیم فصل کم است
🎙
یکی از شروط ما برای جذب بازیکن این بود که در فصل گذشته حداکثر بازی ها را کرده باشد. مذاکرات خوبی برای پرسپولیس داشتیم اما شرایط کشور باعث شد تا نتوانیم لیست اولیه خود را جذب کنیم. فرزین معامله گری بازیکن با استعداد است و در سه پست می توانیم از او استفاده کنیم
🎙
دنیل گرا را هم با توجه به موجودی های بازار و تایید اوسمار جذب کردیم. بارها گفتیم نقل و انتقالات با هماهنگی کادرفنی انجام شده است. در مورد نیم فصل که بازیکن خوب جذب نشده باید بگویم که سرگیف را جذب کردیم
🎙
وقتی نیم فصل بازیکنی جذب می شود اکثرا قرارداد دارند. بازیکن آزاد در نیم فصل کم است. یکی از شروط ما برای جذب بازیکن این بود که در فصل گذشته حداکثر بازی ها را کرده باشد
🎙
فرزین معامله گری بازیکن با استعداد است و در سه پست می توانیم از او استفاده کنیم. دنیل گرا را هم با توجه به موجودی های بازار و تایید اوسمار جذب کردیم
🎙
بارها گفتیم نقل و انتقالات با هماهنگی کادرفنی انجام شده است. ما همیشه گفتیم عدالت باید در بحث قهرمان این فصل رعایت شود. ما به سازمان لیگ گفتیم از کجا میدانید پرسپولیس تا آخر فصل در رده ششم باقی می ماند؟
🎙
اگر گفتم عدالت را می خواهیم باید جدول نیم فصل اول لحاظ شود که همه تیم ها با هم بازی کردند. امیدواریم تصمیمی گرفته شود که به نفع تیم هایی باشد که شانس حضور در آسیا را دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/SorkhTimes/131529" target="_blank">📅 13:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🟢
هنوز برای ورود به سایت دنبال لینک می‌گردی؟!
✅
دیگه وقتشه ساده‌تر وارد شی و با ربات وینکوبت، فقط با یه کلیک مستقیم وارد سایت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡️
بدون دردسر و اتلاف وقت
⚡️
بدون لینک‌های پراکنده
⚡️
ورود سریع از داخل تلگرام
⚡️
همه چیز داخل ربات برات آماده‌ست؛ سریع، راحت و بدون پیچیدگی.
🔗
اگر میخوای بدون معطلی وارد سایت بشی، از اینجا شروع کن:
👇
🤖
@Wincobet_bot
🟢
تحلیل بازی‌ها و آپدیت‌های مهم رو از دست نده:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/SorkhTimes/131527" target="_blank">📅 04:02 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
