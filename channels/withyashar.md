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
<img src="https://cdn4.telesco.pe/file/Kur9L0vrNAXFgtttimB4nxvWTdqu7_YFY4v7DwJv3g8LsNrIk9ofG-dEtzX66Cmcb6Y3QyZDMUNivp8FfYcCJaqd4GJrz7qdodHriM7LiWfLJ_UeHG9HHWm328aOwXxlbIOav0_RK9Zqpbg475m194WqM0o8w5mlM-btLUxDABNg68dxE9a4OOnEhm04w1jApgawQUG2VOdfe-0HJy4ncUEhLo51l2eBWys48N_sj3AICFaQ6_173gJ16lqjLqR65MccV0XyIb1Esj-3t-rX3ey5EIrHAimLmsrr356V7cgfJVwLd8_GBSlRz4EKOzjsaiKQGte2sWRwj4Dg__G0IQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 477K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 05:55:29</div>
<hr>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تتر: حدود ۵۵۰ میلیون دلار USDT مرتبط با ایران را مسدود کردیم.
شرکت تتر امروز اعلام کرد در سال ۲۰۲۶ و در همکاری با مقام‌های آمریکایی، حدود
۵۵۰ میلیون دلار از دارایی‌های USDT مرتبط با بانک مرکزی ایران و شبکه‌های دور زدن تحریم‌ها
در کیف پول‌های مختلف مسدود شده است. تتر همچنین اعلام کرد با بیش از ۳۴۰ نهاد انتظامی در ۶۷ کشور همکاری دارد و تاکنون از بیش از
۲۹۰۰ تحقیقات و پرونده در سراسر جهان
پشتیبانی کرده که بیش از
۱۶۰۰ مورد آن مربوط به نهادهای آمریکایی
بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/withyashar/24463" target="_blank">📅 02:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">روبیو: من با وزیر امور خارجه عربستان سعودی درباره امنیت و ثبات منطقه‌ای، از جمله موضوعات مربوط به ایران، غزه، سودان و یمن، گفتگو کردم.
@WarRoom</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/withyashar/24462" target="_blank">📅 02:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزارت خزانه آمریکا : بسند در‌ دیداری از دولت لبنان خواست تا اقداماتی را برای مختل کردن شبکه‌های مالی مرتبط با ایران و حزب‌الله انجام دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/withyashar/24461" target="_blank">📅 02:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6ac7d7f6.mp4?token=BM-ZAcX7Uv-oy_tU71vGO_qNGMCcLQNFzX9njUogequNClu-VYVDT4jk16IESjjB76bK1JbZ5QThdopbeSC8w-dg8CsCCcWHwvWUlu6P_8MIpbIl3rBlADVoBcqumBOaBtWvCUxB3v8xU2EbhGp6ezvb9ZVaWhKXZfIdVCWnEDwOiL0WjTAbXMgpRlVaLUxZ_4rStn8dNsA5w11avtHPYxA_VbJ3n_zOPXH1z5KAk2-oCJtiFAHCFHYh5xjw1T7BEqjhh7AMQFrJUK5i8a2AiZej9pdJTUtO3WMyTGGQ3IPO2F5AcOnQSVJAkTjjyMhBnW69GbkyWl92ztM9M-SvG2ZE2dMBHXSp_CXcDx5EbCFrE6e5ETmeOM3pw7H_-4sQisPHfqMR6fHKNEvobkKjzco07-K7R5jviJ8cit7pLw6A-5qAbIUk64tui_XAwrWpnB8OWsKvDVt-CCMT4L3yxsZvNQcpbTs6e1emG2RYdSOKMlm5OBBT_FT-IFL4PJ1sv-fdCZdqQXxEeUjaig6upMIm6gCkv9wmU47nDGgCqnNJ2fnho2U8zECEyhtX7uO42qujBW4w49vcCLH2PYtR9hniOtNA7bUm_Pdh-7pwT49aq7pG2Yrx9DUwAkwQ5Cm399XXQ_OddV18IrISe6BpGpQq87VEQAckZD1TyOaKnMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6ac7d7f6.mp4?token=BM-ZAcX7Uv-oy_tU71vGO_qNGMCcLQNFzX9njUogequNClu-VYVDT4jk16IESjjB76bK1JbZ5QThdopbeSC8w-dg8CsCCcWHwvWUlu6P_8MIpbIl3rBlADVoBcqumBOaBtWvCUxB3v8xU2EbhGp6ezvb9ZVaWhKXZfIdVCWnEDwOiL0WjTAbXMgpRlVaLUxZ_4rStn8dNsA5w11avtHPYxA_VbJ3n_zOPXH1z5KAk2-oCJtiFAHCFHYh5xjw1T7BEqjhh7AMQFrJUK5i8a2AiZej9pdJTUtO3WMyTGGQ3IPO2F5AcOnQSVJAkTjjyMhBnW69GbkyWl92ztM9M-SvG2ZE2dMBHXSp_CXcDx5EbCFrE6e5ETmeOM3pw7H_-4sQisPHfqMR6fHKNEvobkKjzco07-K7R5jviJ8cit7pLw6A-5qAbIUk64tui_XAwrWpnB8OWsKvDVt-CCMT4L3yxsZvNQcpbTs6e1emG2RYdSOKMlm5OBBT_FT-IFL4PJ1sv-fdCZdqQXxEeUjaig6upMIm6gCkv9wmU47nDGgCqnNJ2fnho2U8zECEyhtX7uO42qujBW4w49vcCLH2PYtR9hniOtNA7bUm_Pdh-7pwT49aq7pG2Yrx9DUwAkwQ5Cm399XXQ_OddV18IrISe6BpGpQq87VEQAckZD1TyOaKnMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بن سبطی (یگال سبطی) پژوهشگر، روزنامه‌نگار و سخنگوی سابق فارسی‌زبان دولت اسرائیل: مجتبی خامنه‌ای زنده‌ست ولی هرچیزی میگه برعکسش انجام میشه ، اسرائیل منتظر درگیری بین رهبران رژیم مانند آخرای شوروی یا قیام مردمه.
@WarRoom</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/withyashar/24460" target="_blank">📅 02:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عراقچی: من پس از چند ساعت به تهران باز خواهم گشت و امیدواریم که سه شنبه پاسخ نهایی را از طرف آمریکایی‌ها دریافت کنیم.
هیچ تغییری در مواضع ما در رابطه با برنامه هسته‌ای ایجاد نشده است و شرایط ما برای بازگشایی تنگه هرمز کاملاً مشخص است.باید حرف رهبر اجرا شود
ما همیشه برای جنگ آماده هستیم و همچنین چیزهایی برای گفتن در عرصه دیپلماسی داریم. موضوع فعلی که مطرح است، صرفاً تنگه هرمز است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/withyashar/24459" target="_blank">📅 01:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عراقچی داره برمیگرده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/withyashar/24458" target="_blank">📅 01:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/24457" target="_blank">📅 01:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی ) @WarRoom
🚨</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/24456" target="_blank">📅 01:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyij6qEHRTx5HOhXhYSPLtMlAx-zMFxmNlopjvZYu_GO5M7kkYNyjkmXv2R3n8y0hpvHfgzmVmOZn1o4KscRdmp69h8E2SJwBdQ-_RPwLcgfOs8xAtG_mM91hEWsQ9CwN2SfxY6z9Q50ols79k2Mz0Ttdk1vDP54TyOXYCPwz_ZB7x_KP4v3uGVbrvCX1lWg5Jh8gbgKqroV1NoSQ5obdOP9W4eg1x6uUcgfjWkMGUBfiP7MQus2ZwQsqT6Ji6NwSuBj1KE6sVFBaZmttNN8TXQcUDvg0dmesQrJcapj975DbtyX-e7W3fIKNA9FWsE8aw1EZqTeRQgeZJ37WvmVYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «آکسیوس به‌تازگی گزارشی منتشر کرده که در آن ادعا شده من به ایران
رفع تحریم‌ها و دسترسی به دارایی‌های مسدودشده
پیشنهاد داده‌ام. این ادعا نادرست است. من
هیچ چیزی به ایران پیشنهاد ندادم!
گزارش آکسیوس، مانند بسیاری از گزارش‌های دیگر، یک
جعل
است که صرفاً برای اهداف سیاسی منتشر شده است. آنها باید
فوراً این گزارش جعلی را پس بگیرند!
»
@WarRoom</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/24455" target="_blank">📅 01:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/24454" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی ) @WarRoom
🚨</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/24453" target="_blank">📅 01:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXVGdxYaW6O1DG0B5y10o3HYjC-vI6zKHRGhFuAfTXfkwolyBh594hKOGqvxBj48ZpUXElVM0LDBrbHlU16ji-mYXX1Lt76S8-tOm5Hc9JModbct6f8fWvfdqGM22FNN9yNAQTqNi4UO6SaSnWfeCQTPP3efW4cd2V4-vMfdTe_rlx2IQQtMD9rwdVcCjk6IQonZQNziTsGUKry4rCOHl1BjaNT74Zn7s8AopUPVTofAn0HcWzR06hTawfLw-Q80sbWE5omPM-bGaaTf2egrLtMUb1Qm6VkMfoI3bWsZ-EWvRkrbC7lCqYXfmSu5rnJgGQz3qwRClMsHg286qHkzcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوی باشید ، تمام دایرکت شده نا امیدی غر نزنید ، بله اجماع شکل گرفته !
@WarRoom</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/24452" target="_blank">📅 00:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24451">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">داداش یاشار کی مث قبل لایو میذاری بگی تا صبح بیداریم امشب شب خطرناکیه  چرا نمیان پیر شدیم</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/24451" target="_blank">📅 00:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from....</strong></div>
<div class="tg-text">داداش یاشار کی مث قبل لایو میذاری بگی تا صبح بیداریم امشب شب خطرناکیه
چرا نمیان پیر شدیم</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/24450" target="_blank">📅 00:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزارت دفاع عربستان سعودی: خالد بن سلمان، وزیر دفاع عربستان، از شیخ منصور بن زاید آل نهیان، معاون رئیس امارات و رئیس دفتر ریاست‌جمهوری، برای سفر به عربستان در روز سه‌شنبه ۲۹ سپتامبر ۲۰۲۶ دعوت کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/24449" target="_blank">📅 00:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پرتاب موشک هم اکنون از هرمزگان بندرکنگ به سمت تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/24448" target="_blank">📅 00:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دفتر نتانیاهو : بنیامین نتانیاهو و همسرش روز گذشته به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، به امارات سفر کردند. نتانیاهو در این سفر توسط رئیس شورای امنیت ملی، رئیس موساد، دبیر نظامی و مشاور سیاست خارجی همراهی می‌شد.  @WarRoom</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/24447" target="_blank">📅 00:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دفتر نتانیاهو : بنیامین نتانیاهو و همسرش روز گذشته به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، به امارات سفر کردند. نتانیاهو در این سفر توسط رئیس شورای امنیت ملی، رئیس موساد، دبیر نظامی و مشاور سیاست خارجی همراهی می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/24446" target="_blank">📅 00:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آکسیوس: پیت هگست، وزیر دفاع آمریکا، در یادداشتی به تاریخ ۲۲ سپتامبر، به پنتاگون دستور داده از
توانمندی‌های اطلاعاتی و سایبری برای مقابله با مداخله خارجی در انتخابات آمریکا
استفاده کند. این دستور شامل جمع‌آوری اطلاعات درباره تهدیدهای خارجی علیه انتخابات و انجام عملیات مشترک سایبری با وزارت امنیت داخلی است. با این حال، این دستور
شامل حضور نیروهای نظامی در محل‌های رأی‌گیری یا توقیف تجهیزات رأی‌گیری نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/24445" target="_blank">📅 00:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نتایج یک نظرسنجی جدید در «کانال ۱۴» نشان می‌دهد که اکثریت اسرائیلی‌ها در مورد هشدارهای پیش از ۷ اکتبر، به روایت بنیامین نتانیاهو، بیش از تحقیقات روزنامه‌نگاران اعتماد دارند؛ به‌طوری که ۵۴ درصد معتقدند این گزارش‌ها با انگیزه‌های انتخاباتی منتشر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/24444" target="_blank">📅 00:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شکایت «شین‌بت» از شبکه ۱۲ به دلیل افشای خبر سفر به امارات
سازمان امنیت داخلی اسرائیل این شبکه را متهم کرد که با افشای خبر سفر نخست‌وزیر به امارات در زمانی که هواپیمای او هنوز خارج از حریم هوایی اسرائیل بود, یعنی حدود ۵۰ دقیقه پیش از فرود , جان او را به خطر انداخته است.
@WarRoom</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/24443" target="_blank">📅 00:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-zecgd33Z3d-zMe7VkQ3wJOin_-O52rN6MNTUkfp93EhG0yxQ_lKPl9rl42TWxTcqDO24n0tkp0UTNcc5PLvFw3jKZX-zuU0GExu53irFE4urc3hX9Rkh_73O0q8_g3krp3ognIchJx0ZesFI2sHTTGyLTRA7I650EbWooShc4Cy2p5xxX-2CEveAudrtaRomPP6f5bqaAXoiXoF-CrID_krpYuFjcB7X8tHLp1bOFqZppRn4BPbvLuvfpEqdqLrz5V-m6g4j0W4uhBzjTys9AexElS4ZnGN5uwMPaarejx6ScGeDcG7GUIA9YiDskScITo5DeNJIN-w5mJLei7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت توییتر کاخ سفید: ظرف دو هفته چیزی از اقتصاد ایران باقی نخواهد ماند
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/24442" target="_blank">📅 00:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4109be46a.mp4?token=rUXtsrLQHY-wMrKCEmw4801yQBolhIcAY_AqD_goVJg51LcKCkBcyfnZub0sqipBmXt9sRe-hPGh1tx6bwEh7BtXGrk5sagrhKSq2DBW9DA5yCQ51u6Ekn73j-Smn4v0jwqEl3hXMidmiGH1BlaGG5XMyMEkMAYcgyci0rjgdArUG13-2G7uKij_YuMRJPlhYPuFamoSzQQfm6yg6quzemkupwFYhlHdT90jYkP-_xOmFqlDKVz2QaFNbtoivfw_F5hDuWZJzYikB06ZF6v5HjWkvwI2kTrE8o-TsRri6b875LoqPERr_U3BencRsj1z6HxSkADkmTI3nyDnbp67jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4109be46a.mp4?token=rUXtsrLQHY-wMrKCEmw4801yQBolhIcAY_AqD_goVJg51LcKCkBcyfnZub0sqipBmXt9sRe-hPGh1tx6bwEh7BtXGrk5sagrhKSq2DBW9DA5yCQ51u6Ekn73j-Smn4v0jwqEl3hXMidmiGH1BlaGG5XMyMEkMAYcgyci0rjgdArUG13-2G7uKij_YuMRJPlhYPuFamoSzQQfm6yg6quzemkupwFYhlHdT90jYkP-_xOmFqlDKVz2QaFNbtoivfw_F5hDuWZJzYikB06ZF6v5HjWkvwI2kTrE8o-TsRri6b875LoqPERr_U3BencRsj1z6HxSkADkmTI3nyDnbp67jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا تیم شما امروز با ایران صحبت کرده است؟
ترامپ: بله.
خبرنگار: با میانجی‌ها؟
ترامپ: بله.
خبرنگار: چیز دیگری هست که بتوانید با ما در میان بگذارید؟
ترامپ: ما پیروز خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/24441" target="_blank">📅 23:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تنگه صدای ناله های حسن خرسی میاد</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/24440" target="_blank">📅 23:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قشم صدا میاد</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/24439" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24438">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نیویورک پست: به نقل از یک مسئول آمریکایی، دیدار مقامات ایرانی با کوشنر و ویتک در نیویورک، منجر به مذاکراتی از طریق واسطه‌ها درباره امکان باز شدن تنگه هرمز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/24438" target="_blank">📅 23:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8EQKd6ekgezZFQYUW4z95vqXEIrjWvrCoQ7ZR4XM0YCQEJjpzoEhC1h_HoYZORMOmUOzPXHvJTyNi-8JPmscl0xcG6z1EMwyPAxjvwRbScF6GwK8WrdOyWgvVtZF1OYLS_cqxedWRHCvllkaYGf1McsjTWvU4zPj_xyU5zRsVtMSGyx3_zeyeWcIU-ikZtuG7VlEFBMhbsV5QnxW1Y4gVGwMXzRU3eHa2Av3SwXwXdp4d8QtnHT71HCUrk-hCgahoSPbWEIkv_FjIHCiKVQya5lh79yRylLRMIWTnddfxJwSLUBBfMt-dZqxC4fHNYmkvlP4tVwCHJsfpZaokwVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : حضور
پنج فروند هواپیمای سوخت‌رسان، یک فروند T-38A Talon (هواپیمای آموزشی جت مافوق‌صوت)، یک فروند پهپاد MQ-4C (پهپاد شناسایی و مراقبت دریایی دوربرد) و یک فروند E-3B Sentry (هواپیمای هشدار زودهنگام و کنترل هوایی)
در محدوده تنگه هرمز و خلیج فارس رصد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24437" target="_blank">📅 23:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37e38e4cc.mp4?token=d1kIEQc9wGiN0zTyOug0VBcHPjmtSyeRkDZXaLFvOSklQRgG6m8rqpnEJgic4TM55Jl7r63Yxy-uEjAarOr62o7p32WLkpRf-8O1lsTeA10AEkr6p-ubBo0q9IaKU-yTwdT6vZ3hnIuR_liuIoUCkhnQfjcMBKClO9ne_-55CpuFeBjN93pAL9XxlT-ihAe5RTiHA7umLO000E4iCg6_Tt2-1CfX8M2zEHWiOxwwBfwn-0x_rEqHq7SGwa63_azDsIhNAKiHsOMKfMI7SvCc1fhE4ju__s1iRxV1QdqXavS1UuEFE5RM9o0q__GzO_9ivNwfbg2Im2Y4qLne60eg1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37e38e4cc.mp4?token=d1kIEQc9wGiN0zTyOug0VBcHPjmtSyeRkDZXaLFvOSklQRgG6m8rqpnEJgic4TM55Jl7r63Yxy-uEjAarOr62o7p32WLkpRf-8O1lsTeA10AEkr6p-ubBo0q9IaKU-yTwdT6vZ3hnIuR_liuIoUCkhnQfjcMBKClO9ne_-55CpuFeBjN93pAL9XxlT-ihAe5RTiHA7umLO000E4iCg6_Tt2-1CfX8M2zEHWiOxwwBfwn-0x_rEqHq7SGwa63_azDsIhNAKiHsOMKfMI7SvCc1fhE4ju__s1iRxV1QdqXavS1UuEFE5RM9o0q__GzO_9ivNwfbg2Im2Y4qLne60eg1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «من وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاقاتی باشد که تا به حال برای جهان رخ داده؛ برای ما، اما در درجه اول برای جهان. اسرائیل همین حالا از بین رفته بود. دیگر اسرائیلی وجود نداشت، خاورمیانه‌ای وجود نداشت و بعد موشک‌ها و بمب‌ها به سمت ما و اروپا روانه می‌شدند. و من جلوی آن را گرفتم.»
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/24436" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcbc9a39f.mp4?token=JXL9JSPZxgKmv1CawvTl4aAjdSJnhZeoLKZG8IiHZ5JKjbDROd1sx0KSWkU2zabtQaqPbgdONhzztQvvYXJz8opTUyCyI7fQ4wooEnaPAwzzEUpDHadkr5iB_a6-1pMNNRCn8TyIc8iqPWe2XwlTNgedDnbyN6nfe8eaK35zS71mTDYiWjAjn138OpY84rf8AiJ7EkJtBM-EZjZqRPQE620DSgu4KzmMJazQhWQLd5ALT7Vx7_sgreLHeRuVIfZGBxpzt3jkObhcn1Z203ToP_fdrm-m6YMBrPYtNq78_-fAoo-h25KaI_VKjO68IwqhLf9Pk-IXiNPBa2vRSz-apQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcbc9a39f.mp4?token=JXL9JSPZxgKmv1CawvTl4aAjdSJnhZeoLKZG8IiHZ5JKjbDROd1sx0KSWkU2zabtQaqPbgdONhzztQvvYXJz8opTUyCyI7fQ4wooEnaPAwzzEUpDHadkr5iB_a6-1pMNNRCn8TyIc8iqPWe2XwlTNgedDnbyN6nfe8eaK35zS71mTDYiWjAjn138OpY84rf8AiJ7EkJtBM-EZjZqRPQE620DSgu4KzmMJazQhWQLd5ALT7Vx7_sgreLHeRuVIfZGBxpzt3jkObhcn1Z203ToP_fdrm-m6YMBrPYtNq78_-fAoo-h25KaI_VKjO68IwqhLf9Pk-IXiNPBa2vRSz-apQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «به‌محض اینکه این جنگ تمام شود، تورم به‌طور کامل از بین خواهد رفت. کاملاً. هیچ‌کس درباره این موضوع صحبت نمی‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/24435" target="_blank">📅 22:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24434">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd292496.mp4?token=UTLjHKrnESUO0xMdcpc4NuYAq3cJkkPNIOguktECpudsE_Dk-uUCkKQ0Ie6VKNPQRRV2yGD3-mRqEUhtFOA6sIfqoLH_oAtV6femXX_sAVV6rB3bygPaRBphU67rr2phPaToAO6N7LDOP2TFEAD9V6IwbQ0Gv6k7xZ3Qn7bZTtDo3INk0moiPBZgXhLx3_si2nMAN0Oc1arjOVNPdUAWbZyVFzivFSW2pEdwmDVsgncNhQQvxzIFOQMkwtFPQ8RsY55t4T19Y8-sC3gh8YNytAF8FKFJA23l24NZjDfoaD-m1JjLCEX5bd3muyZP74LfYb49tRrUYLamhPOIE9RyZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd292496.mp4?token=UTLjHKrnESUO0xMdcpc4NuYAq3cJkkPNIOguktECpudsE_Dk-uUCkKQ0Ie6VKNPQRRV2yGD3-mRqEUhtFOA6sIfqoLH_oAtV6femXX_sAVV6rB3bygPaRBphU67rr2phPaToAO6N7LDOP2TFEAD9V6IwbQ0Gv6k7xZ3Qn7bZTtDo3INk0moiPBZgXhLx3_si2nMAN0Oc1arjOVNPdUAWbZyVFzivFSW2pEdwmDVsgncNhQQvxzIFOQMkwtFPQ8RsY55t4T19Y8-sC3gh8YNytAF8FKFJA23l24NZjDfoaD-m1JjLCEX5bd3muyZP74LfYb49tRrUYLamhPOIE9RyZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «اگر می‌خواهید شاهد آشوب و یک فاجعه باشید، بگذارید آنها یک شهر را با سلاح هسته‌ای هدف قرار دهند. من فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم. بگذارید آنها با یک سلاح هسته‌ای به خود ما حمله کنند؛ خطاب به تمام آن آدم‌های احمقی که فکر می‌کنند چنین چیزی اشکالی ندارد. آنها دیوانه‌اند. هیچ شکی در این باره نیست. آنها واقعاً آدم‌های دیوانه‌ای هستند. من همیشه این را به آنها می‌گویم. می‌گویم: «مرد، تو دیوانه‌ای.»
@WarRoom</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/24434" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec45ce4fdf.mp4?token=FzyoJdIc-3Re6E1-QYUHvS3SQpH3-uv-F9yNy_D1qdkU_VK5LnSnVA6RCHoBs49TJ5dUwTtgAFpEARL-Pb1EY-yr4ZEAWibpIx33hoeVRiyeA7O5_UXB7AFMjb95anb8MJb5Dp-M_C_F3SNdshQT-tDLbH_gYzLnuPrm10mZWRZq2ifp6u7VQh-nHI8pltKeLi9d1EsHQ2Xi0vtxvuMyA1BjAQrQlJ80axoa11o_Lbfia7CldLZK-l2--y7zQtYsmRNfj91lYC4zDopG0nOjFzyQML2tQD6hrjqY5gaAWj7R4JIVjikE8JU2Y7LiORPSQlanBkpGQKewDB_LCHZvbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec45ce4fdf.mp4?token=FzyoJdIc-3Re6E1-QYUHvS3SQpH3-uv-F9yNy_D1qdkU_VK5LnSnVA6RCHoBs49TJ5dUwTtgAFpEARL-Pb1EY-yr4ZEAWibpIx33hoeVRiyeA7O5_UXB7AFMjb95anb8MJb5Dp-M_C_F3SNdshQT-tDLbH_gYzLnuPrm10mZWRZq2ifp6u7VQh-nHI8pltKeLi9d1EsHQ2Xi0vtxvuMyA1BjAQrQlJ80axoa11o_Lbfia7CldLZK-l2--y7zQtYsmRNfj91lYC4zDopG0nOjFzyQML2tQD6hrjqY5gaAWj7R4JIVjikE8JU2Y7LiORPSQlanBkpGQKewDB_LCHZvbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا حادثه پایگاه RAF Fairford به ایران مرتبط است؟
ترامپ:
«ممکن است مرتبط باشد، اما باید بگویم از اینکه آنها [افراد بازداشت‌شده] را آزاد کردند،
متعجب شدم. من این کار را نمی‌کردم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/24433" target="_blank">📅 22:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24432">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ: امروز از طریق واسطه‌ها با ایران گفتگو داشته‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/24432" target="_blank">📅 22:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24431">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6885716a79.mp4?token=KbqJ_ttG8QKPloiw2zqiI7ioQ0Q4F-NWGRYWSsjehl6nvV3Oxh3uFfZmb5ny3Aj93X6uuD-uPuO3g-6Gatr4C37NhuXdFrrKungu7EGf4G22928g0OIyO-fYrhkPKU-UYf_7wV-GcJN4PxG97cVnGwGrwKuzWhU0GmO0YfEbvfW4aM3qHntitWqtMm7D97ypEckuK_KFr9kgyZDEi95mSfaUsWS3pHcdtUa-tNoTvYT0GTUj6WEyZbT1DoKa6DbB7tSIZyqIFgtn84v1GDnktdSlemyEKV8kifasgtLZ6I5JadGccHjcpb7l2zMG7N6T4QtVIgQD_meLZYqwuehXoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6885716a79.mp4?token=KbqJ_ttG8QKPloiw2zqiI7ioQ0Q4F-NWGRYWSsjehl6nvV3Oxh3uFfZmb5ny3Aj93X6uuD-uPuO3g-6Gatr4C37NhuXdFrrKungu7EGf4G22928g0OIyO-fYrhkPKU-UYf_7wV-GcJN4PxG97cVnGwGrwKuzWhU0GmO0YfEbvfW4aM3qHntitWqtMm7D97ypEckuK_KFr9kgyZDEi95mSfaUsWS3pHcdtUa-tNoTvYT0GTUj6WEyZbT1DoKa6DbB7tSIZyqIFgtn84v1GDnktdSlemyEKV8kifasgtLZ6I5JadGccHjcpb7l2zMG7N6T4QtVIgQD_meLZYqwuehXoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما
خیلی زود در این جنگ پیروز خواهیم شد.
این جنگ تمام خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/24431" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24430">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e7e5f951.mp4?token=neWnzBYCNLn5-Xa8uCdztSUcLZQRxiANV3vBYmp218V84BfFeuigQO8mrPXDiZvyTkV_QwSArqK25dc1AwmOxW-ZzT1NbStO6_-Cn2MkQN3sx1WFGUBObGlf_xCnI1vv7Tf9nXAxKSkTvrOR7TXBOE8kMUZ0sb0VOTVeyRyDkhUn4x4vV64ANzJ7MPiD8Jdmbh44nGeqhSGPSexWx3DmrVs02qoRimFWwS64n93VSeguuLO3O9IDDq-Ra5WvSxZ6s94xBZ0Hg271ZtHQgT8BUJPYZCTeuDaYug_f-Z2GOi-IzrzVlA52xhY4kHOgnaNFi-PCwjS66xGpP9_Re5e5ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e7e5f951.mp4?token=neWnzBYCNLn5-Xa8uCdztSUcLZQRxiANV3vBYmp218V84BfFeuigQO8mrPXDiZvyTkV_QwSArqK25dc1AwmOxW-ZzT1NbStO6_-Cn2MkQN3sx1WFGUBObGlf_xCnI1vv7Tf9nXAxKSkTvrOR7TXBOE8kMUZ0sb0VOTVeyRyDkhUn4x4vV64ANzJ7MPiD8Jdmbh44nGeqhSGPSexWx3DmrVs02qoRimFWwS64n93VSeguuLO3O9IDDq-Ra5WvSxZ6s94xBZ0Hg271ZtHQgT8BUJPYZCTeuDaYug_f-Z2GOi-IzrzVlA52xhY4kHOgnaNFi-PCwjS66xGpP9_Re5e5ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ:«اگر جمهوری‌خواهان در مجلس نمایندگان و سنا پیروز شوند، به هر فرد بزرگسال ۵ هزار دلار پرداخت خواهیم کرد. و ما می‌توانیم این کار را انجام دهیم.
دموکرات‌ها نمی‌توانند، چون هیچ درآمدی ندارند و کشور را به سمت رکود اقتصادی خواهند برد. آنها هیچ پولی نخواهند داشت.»
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24430" target="_blank">📅 22:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z91Jf79jszxtoW6G7tkUbnzwzHuUBgCIHQNzVjpxJlw2WoaYyBElrLyMYDktFCJALFgt2-6YViPwo13hJ6kWD2j3QO0ivh1Dwq9LX-FYAvp-T9v3wwensRytdBobJeo7qhmhkPN0I-7y9_unT6D5813c4SdFjiL1vJvH0QSXQK_jqCx4wJgemse_J5B6YrgskXQ5yY4qHWovEA0nnRyCSOPBC7oSaYvZO1y5q7-qFFeSqlpW9PmhmYH_dre6D82Ap4jz5cg3lRPaFOsRpbFjm_KYmTHqg9bb-41m-u6b4rfRbvRRozHfVcncLIo7d0xlySCbSmk-5o_xD6CehwVjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: بزرگترین کارخانه فولاد در آیووا ساخته خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/24429" target="_blank">📅 22:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">باراک راوید ، آکسیوس :به گمانم ایالات متحده می‌خواهد شاهد آن باشد که ایران بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کند؛ کاری که در جریان مذاکرات سوئیس متعهد به انجام آن شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24428" target="_blank">📅 21:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24427">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امارات متحده عربی سفر نخست وزیر اسرائیل به این کشور را تکذیب کرد</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24427" target="_blank">📅 21:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70875dba60.mp4?token=klj3-saBtLau__PdzTcfqkrbeEcNajObOgOe37qyv12jKbJQ9buDN4Rbu6m9eMH_6pIduyFZsW1RyOPkwKcvY8c1tssu1OnjQ4fweqIAKCNfNQbXAPUgVt_kJWZB2hg-iCwGQDgkfrkuX0Y3hksKwvtbDABFUqI7wq-QWPnmcWHtgJvD0WGQpal4k3qbwuk5KMaUqy4kzUByA_h82V57LmQT534qPRQ4ntqTuypaBaXJ1_-aXx-VfZNU61kDH1x7BDL7OPQj1jFpUQjJ4x1d8cTRUrs6c8Eff6gx38qLWNXQg1_Om6017a13tda1OUX4z57cz0NfzmgYVV0EcxGwY0GgTBccUY1KSDCqie-3TKzowp73Rc68-C2qO-DW5dx7iTS_Yg0hKQyDfoHyU79MCXRCfV6_BqIGvb-zvoydRV08UMFw6SqyETbS9R8hm6YDe3AijLhzOQX7OhaS4NW8Niv6EMHVXN95BA8-fV8F2tiodXfGCfz2yPMx4BJ3e47De8Dqk-oO71jOJDjxWvude7yDflIgwvmLqcpO0Y9SMPnWm-cTt_aoSXchYJ8VmEbZ9gwdhhvrs1TTY7I8G4JWDdO0JzQ8ZJGPYNwr-b-xKd2ylUZzsPLDMgb0ERwQavHCl7CMeVFZTL4vJnODU9Mp_-GJ13SF0-C6w73dU85tZbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70875dba60.mp4?token=klj3-saBtLau__PdzTcfqkrbeEcNajObOgOe37qyv12jKbJQ9buDN4Rbu6m9eMH_6pIduyFZsW1RyOPkwKcvY8c1tssu1OnjQ4fweqIAKCNfNQbXAPUgVt_kJWZB2hg-iCwGQDgkfrkuX0Y3hksKwvtbDABFUqI7wq-QWPnmcWHtgJvD0WGQpal4k3qbwuk5KMaUqy4kzUByA_h82V57LmQT534qPRQ4ntqTuypaBaXJ1_-aXx-VfZNU61kDH1x7BDL7OPQj1jFpUQjJ4x1d8cTRUrs6c8Eff6gx38qLWNXQg1_Om6017a13tda1OUX4z57cz0NfzmgYVV0EcxGwY0GgTBccUY1KSDCqie-3TKzowp73Rc68-C2qO-DW5dx7iTS_Yg0hKQyDfoHyU79MCXRCfV6_BqIGvb-zvoydRV08UMFw6SqyETbS9R8hm6YDe3AijLhzOQX7OhaS4NW8Niv6EMHVXN95BA8-fV8F2tiodXfGCfz2yPMx4BJ3e47De8Dqk-oO71jOJDjxWvude7yDflIgwvmLqcpO0Y9SMPnWm-cTt_aoSXchYJ8VmEbZ9gwdhhvrs1TTY7I8G4JWDdO0JzQ8ZJGPYNwr-b-xKd2ylUZzsPLDMgb0ERwQavHCl7CMeVFZTL4vJnODU9Mp_-GJ13SF0-C6w73dU85tZbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وس استریتینگ، وزیر دفاع بریتانیا، درباره ایران:
«فکر می‌کنم حمایت از اقدام دفاعی آمریکا، کار درستی بود.
کاملاً درست است که بگوییم جنگ در ایران، جنگی نبود که ما انتخاب کرده باشیم؛ اما در عین حال، هیچ شکی نیست که ایران نیرویی شرور و مخرب است که بریتانیا، منافع ما و متحدانمان را تهدید می‌کند.»
پلیس گلاسترشر گفت ساکنانی که به‌دلیل احتمال وجود توطئه‌ای برای حمله به پایگاه هوایی سلطنتی فیرفورد (RAF Fairford)، از حدود ۸۵ خانه در اطراف این پایگاه تخلیه شده بودند، اکنون می‌توانند به خانه‌های خود بازگردند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24426" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یک منبع آمریکایی به شبکه العربیه گفت: اختلافات و موانع بزرگی بین تیم‌های مذاکره‌کننده آمریکایی و ایرانی وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24425" target="_blank">📅 21:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMj0_5mSIpyJDyrs14sbXIRo-uE1hUirDeqeDr_7l-p1HdYvwym6AQ-heqdk4QhYbLS0LGhvofmaxiD4Ww_vqRBA9wQTiKnTouglv5V8CONunPgCkktRLeiEPU0TWJVWvPzZWkrjuvu_hYsgQnL6f8TI9Fn7W9MM-vjaqY55F3m9Xfw85L1pXG7e1JDV9483KMNbRDZ-KlW_eotLDKXaJ05tCTXNhkFUFoTiOXNHPN_25AuHCzzhnvY62Ja0xHTLK2XLQUGB7r3ll4gpzXeQbK-GSB92UBEEpRuRiZWQhLiF0oSBnz_JS8iVN9MZPp2EIMU3nEk7LRSp2KzJf6uskA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
عملیات طرد اقتصادی باعث شده که ریال به رکورد‌های پایین‌تری برسد.
ما به تخریب توانایی رژیم ایران برای تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24424" target="_blank">📅 21:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ارتش اسرائیل : لحظاتی پیش، یک موشک رهگیر به سمت یک هدف هوایی مشکوک در منطقه‌ المطلة  که سربازان  ما در جنوب لبنان در حال عملیات هستند شناسایی شده بود، شلیک شد.جزئیات در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24423" target="_blank">📅 21:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کانال ۱۲ اسرائیلی:
نهادهای امنیتی اسرائیل در حال آماده‌سازی برای احتمال از سرگیری درگیری‌ها با ایران هستند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24422" target="_blank">📅 21:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vH1XJAeInntSUcewDyiss0wSzYDd94n-Hv6xxnBB7_ejRZ3M36R0_tlUVMc8MxRRq4T2Ca3JRO5gcoSuumUDkSlsEb8pHsUYDxI4IlC12xZEFMsUCpsP2IJtcMhoX7BCZhQnH0GUPkbyqVySli6TKJZRP3JJQDFC-5qN_B7BpKJSImGDQk9ioSckSkue8NPivG4rqEGkxhVJpeVGUHWtIUdrrdz7nellkzplkSQl62vF2Kd8wrBclKPdwW6D3-HrhbmMKCPJiXKptywCQaXsl_s529tuNzD10KBOA3EjiTI1tuoNGgyAMHKADu8ObMEMtTc_FaljbYtUHO0Kwl7wYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل:
شَدی ابوحطیرا، از تأمین‌کنندگان مالی حماس که شبکه انتقال پول «ژنو» را هدایت می‌کرد، در یک حمله هوایی دقیق در غزه کشته شد. ارتش اسرائیل مدعی است او
ده‌ها میلیون شِکِل ارز خارجی
را برای شاخه نظامی حماس منتقل کرده
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24421" target="_blank">📅 18:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مورگان اورتگاس، معاون فرستاده ویژه آمریکا در امور خاورمیانه: «سناتور لیندزی گراهام هرگز از باور به شما (مردم ایران)دست نکشید. او باور داشت که شما دوباره آزاد خواهید شد. او هرگز از تشویق رئیس‌جمهور ترامپ و وزیر خارجه روبیو برای حمایت از آنها (مردم ایران) دست نکشید.»
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24420" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n40AMJDp9lRiWw4IJg7LzZL0GzHzO1XVg690pHCbbqk7pi5cnXE8rI3_78N1Ol2JZzx07rogJtyisjKzCylXCTJtRx-uCOitLoYKIT1x6V0ugQeQNpg2gfaYCNu-T1Wr4rHqgvpCZHn0H4GNQ2Rucv2tM7kSYfPKeFfKQhB0Zu8LCNBhgmGeTK3seYQD1pvMfF50-LmFBYbGzX8kT0ylj_UdH4ppEtKyCYJbRLZphVisnXdAe8Fch5uMGR2n3VZ3c5teZ-5JxfvXdcGGkNmK7fcALATP3erM-9GkfSdhY2T8jTmnXLKgFgigGr9faIf3ilWApdR9wsDts2bby2Q7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا این لحظه عراقچی موفق شده یه ناو جدید اعزام کنه ۳ دسته هر کدام ۵ فروند هرکولس و ۱ اسکادران اف-۲۲ ، این است «قدرت مذاکره»
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24419" target="_blank">📅 18:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24418">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تسنیم : عراقچی امروز با میانجی‌گران در نیویورک دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24418" target="_blank">📅 17:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">برنامه امروز دونالد ترامپ به وقت تهران: کاخ سفید اعلام کرده ترامپ امروز دوشنبه ۲۸ سپتامبر، ساعت ۱۸:۳۰ یک جلسه سیاست‌گذاری در کاخ سفید و ساعت ۲۰:۰۰ و ۲۰:۳۰ دو جلسه دیگر در دفتر بیضی خواهد داشت. سپس ساعت ۲۱:۳۰ ترامپ در دفتر بیضی مقابل خبرنگاران حاضر می‌شود و…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24417" target="_blank">📅 17:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارشهای بسیار‌ از دو انفجار سنگین در تنگه هرمز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24416" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyxmXIicaiUN6X3VhmuFAQuYxIXftWwCrRKoGVguTfXH5Nn6QO1OeUfxkqUlZ5pll07NmvZhhJTI9RMTjp89bAOCQ3t9O6UtARx-EJMEiWv_uu9P2Vd6Ggm5JUpoWy5DtpzEOatQXgun4mezbS_nh4pY1_VHRR8HiIb-RC_jgB6_YG9_oSuhUPwliTXAUJ_KQs08PQ96e2ptTe_LFqSzH19MNjtxyPRW-HlHHuUL33lc5Z3-8SVLW06h3EIphg9NzZCpkXyfsQF5K3FnwZQamxPw0lMUF_mKJe5AfglFBvbDTT1Z-O-1fMZkbXK4VdF3qoQOfbqR8VXs_JSTcxK-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : فلکه دوم فردیس لانچر و موشک آوردن
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24415" target="_blank">📅 17:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">برنامه امروز دونالد ترامپ به وقت تهران:
کاخ سفید اعلام کرده ترامپ امروز دوشنبه ۲۸ سپتامبر، ساعت
۱۸:۳۰
یک جلسه سیاست‌گذاری در کاخ سفید و ساعت
۲۰:۰۰
و
۲۰:۳۰
دو جلسه دیگر در دفتر بیضی خواهد داشت. سپس ساعت
۲۱:۳۰
ترامپ در دفتر بیضی مقابل خبرنگاران حاضر می‌شود و
یک اعلام رسمی مهم
خواهد داشت؛ موضوع این اعلام هنوز رسماً اعلام نشده، اما گزارش‌های منتشرشده آن را مرتبط با
هوش مصنوعی
می‌دانند. ترامپ ساعت
۲۳:۰۰
نیز با خبرنگاران رسانه‌های چاپی دیدار و گفت‌وگو خواهد کرد. شام خصوصی ترامپ با
داریو آمودی، مدیرعامل Anthropic و سازنده Claude
مربوط به شب گذشته بوده است. همچنین فردا ترامپ و مایک جانسون قرار است با مدیران شرکت‌های بزرگ هوش مصنوعی دیدار کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24414" target="_blank">📅 17:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">امروز ترامپ بیانیه ویژه ای ارائه خواهد داد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24413" target="_blank">📅 16:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24412" target="_blank">📅 16:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYkW3gwAjZPS86Qcl0PTTAZN1hg8RsHAOrE1Iz-S757pgdf8a6On6C7-v3lohDr5DqmwFSYL1DFkty0lODX1hiiaUIgegPPJKDgDJDpJrLRD3nhOHl9Z1uwriyWRmPBk0tWgXmrmjCXiqEecHNxcEXrM7dul9c0LZ5jlrhgPkJaaaR-Te1jU07xHtXAfDtBkF2v10ZiSnVFbIjR0PIFZXKQKAW7E_ajJZ3UO0Ak3ej-C0taZOXZletCaCxH-w7fsGRatnjGkyULJ_HF_dwGuGNrbObx_DGjMImnjGLWGtTR5IHws1DLTjoVva7BvVpm-EfnP6hOISeCSfhL5UBOEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092268a67d.mp4?token=YKUL5TsibO--UHVClYzMpSreh0fd2tQ2RUpKyHg4xFSuDaREeqRbchuwulghAehDie0Imu_nLuf1agNF7zRc1HftlyoaTeO1f0RbyR-zOGuT1piwWCIL-gqLME84ke8hTnYuf0HYZntx28JeO6hN8Lcw4SrLeJ4PDSz7Be2n3CmbbitZrky61EB_jhunf5knL-LmmxhGCKOwQS0GCl5ZYY6JIU9gU2q2bthyueYBf73GnY-tY6Rhi-3o0dD72OYxtNtkb4FuXybZmAZZwj0G3vl32SVS4sbHjYkDtV0Dooks_3Fn0gzY6gG6UvWbV-9BpUaX8FNgmKye1BJUySyXbV-bD5__eb_VBW94wKM5Ha2SFUixjc_OzFbEMFBZScHVNbIFOy0SadMW2CDCUJOE8w4Wmx51MJQxlvMi_di5grwJboWBvmoYWRiR1V8Q796OBNcxvANQm2dKhrqvDIGGO2jdHhdrrCN5xbw_fQhuKH_n05YXbKuDQV7Sms6q5zyhCbYzGj_OC22UDITyw1KHm8Yv6763dXQF7tmmazA9B9FG2xTJ8pyp6tPopHY-7Sol_cHF6eWltknSVvO3I8snn2JZTQjcIBqfezG-R9XsTVHJev4k7nwLoFo2GtSngA9wLb5jo9EwwDSWVnc5B3XMv9wO7t-jNLBboMFEzWeJhZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092268a67d.mp4?token=YKUL5TsibO--UHVClYzMpSreh0fd2tQ2RUpKyHg4xFSuDaREeqRbchuwulghAehDie0Imu_nLuf1agNF7zRc1HftlyoaTeO1f0RbyR-zOGuT1piwWCIL-gqLME84ke8hTnYuf0HYZntx28JeO6hN8Lcw4SrLeJ4PDSz7Be2n3CmbbitZrky61EB_jhunf5knL-LmmxhGCKOwQS0GCl5ZYY6JIU9gU2q2bthyueYBf73GnY-tY6Rhi-3o0dD72OYxtNtkb4FuXybZmAZZwj0G3vl32SVS4sbHjYkDtV0Dooks_3Fn0gzY6gG6UvWbV-9BpUaX8FNgmKye1BJUySyXbV-bD5__eb_VBW94wKM5Ha2SFUixjc_OzFbEMFBZScHVNbIFOy0SadMW2CDCUJOE8w4Wmx51MJQxlvMi_di5grwJboWBvmoYWRiR1V8Q796OBNcxvANQm2dKhrqvDIGGO2jdHhdrrCN5xbw_fQhuKH_n05YXbKuDQV7Sms6q5zyhCbYzGj_OC22UDITyw1KHm8Yv6763dXQF7tmmazA9B9FG2xTJ8pyp6tPopHY-7Sol_cHF6eWltknSVvO3I8snn2JZTQjcIBqfezG-R9XsTVHJev4k7nwLoFo2GtSngA9wLb5jo9EwwDSWVnc5B3XMv9wO7t-jNLBboMFEzWeJhZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : چند فروند جنگنده اف-۲۲ رپتور طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی لنگلی به پرواز درآمده‌اند.علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی آمریکا با نام عملیاتی CORONET نیز به پرواز درآمده‌اند که احتمالاً در حال پشتیبانی از انتقال جنگنده‌های رپتور به خاورمیانه هستند:
GOLD21: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 17-46034)
GOLD22: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 16-46021)
GOLD31: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 18-46051)
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24410" target="_blank">📅 16:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efe2963dc.mp4?token=ie8IsElWD9FUgncZ-sBsAkBoeyz6a8jQofiulo7YEjEEioG1AgD-9cVEHcQrA5TdIqAf5u6In5GQIdRSLikYuWfaks3oUnG6wVEwxpet0vA9383ZNpFSzfitKG0Z5ZVL839KR5A5dnCwJaVbGFcwvW9ioTtz6eJi34FnRcO4ZKAJU9nUk7sijTDDCxrkItIFuLYaA-DJlALjetUD8IJ9xt2WTx7PAOfdGxLOcXEc2rTa7RNN34oUTZcD29EqHdm7pPakbnL1YW0ZovQ__kTUVnApBZmru5cxXUf__nPMv-L22a6UAKOr9OGdwVPPQern8w0PeA9HH0mZjU8o-Wxnhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efe2963dc.mp4?token=ie8IsElWD9FUgncZ-sBsAkBoeyz6a8jQofiulo7YEjEEioG1AgD-9cVEHcQrA5TdIqAf5u6In5GQIdRSLikYuWfaks3oUnG6wVEwxpet0vA9383ZNpFSzfitKG0Z5ZVL839KR5A5dnCwJaVbGFcwvW9ioTtz6eJi34FnRcO4ZKAJU9nUk7sijTDDCxrkItIFuLYaA-DJlALjetUD8IJ9xt2WTx7PAOfdGxLOcXEc2rTa7RNN34oUTZcD29EqHdm7pPakbnL1YW0ZovQ__kTUVnApBZmru5cxXUf__nPMv-L22a6UAKOr9OGdwVPPQern8w0PeA9HH0mZjU8o-Wxnhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراضات به گرانی دانشگاه علامه طباطبایی
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24407" target="_blank">📅 16:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNeqSIwCkhzXvwl3NLBJlmWEZWmgm8jzS19HdlkWJGVGjPK8Kn5mbvt9D18NT0pBrG6JvHxM_SNg_-mOQ_Sy74q__99RQUHHMia98xvJbVVeb7bFgL-lqIQHpG7UUSz0hbGBA-UtxhL1RAfGIbwTeODNjKcUU4k45ZcFD9SDhs_MaOrbamWZRTePspUPbDZAEsIsFncZz299rj5A3xu-ASa-1qMQk2X4mXBpu7WZAYqgApcY7TTn87ViXFxy37yqQRwAsFWwv9iWWaEhiZtDfhOP7pI3WivbQsHvD57Vj5k_dZqDzfYBDA5bwv37XUMnPx4Q0236OO1Y6Yzh5uNX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی )
تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی )
دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی )
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24406" target="_blank">📅 15:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWhCO4pwnWy9JsjoiYBwv0R2hQ6lrrWhvy8mk3TIh6HtXBm95XQy4YN66_aNnuz6L3U43vJD9tjm3PVZLDTe_6kR9hYLcu-_7jS4MOQVqSmj7rFQXOCk3nFHsrJCKuyWi8tD_24tWtW1ZWuIgwBtV0vjMB-E7yMLDHeCOHN1WmzHaNwqrTePmtS8R4w3tTYQli6cjlE_uN_pgELzOUmUr19TNhfqrvxHl3F0trk4gEFaJ5dkw3PVlyZLF3AnaCuqAq1XWaGTi73tRkLsDSjMnxvgyQnR2KNMZeZSkNqKlSK_KJ4hiaxZIkvln_an45hudAVpPktjc92vl24vw8xLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب سنتکام:
ادعا رژیم :
یک فرمانده ارشد سپاه پاسداران امروز گفته است ایران از طریق «نیروی دریایی» خود
کنترل کامل تنگه هرمز
را در اختیار دارد. این ادعا
نادرست
است.
واقعیت:
ایران نیروی دریایی ندارد، زیرا
نیروهای آمریکایی آن را غرق کردند.
ایران همچنین کنترل تنگه هرمز را در اختیار ندارد؛ همان‌طور که
هزاران کشتی آزادانه از این تنگه عبور کرده‌اند
و تنها طی چند ماه گذشته،
بیش از یک میلیارد بشکه نفت
از این مسیر عبور کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24405" target="_blank">📅 15:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEQ3</strong></div>
<div class="tg-text">یاشار بندر عباس طرف پارک شهدا صدای دو تا انفجار اومد با فاصله 3 دقیقه از هم</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24404" target="_blank">📅 15:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش صدای انفجار بندر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24403" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترکیه تودی :
پروازهای باقی‌مانده شرکت‌های هواپیمایی ایران به ترکیه نیز ممکن است
از اوایل اکتبر ۲۰۲۶ / اواسط مهر ۱۴۰۵ متوقف شود
. این رسانه به نقل از
دو منبع مطلع
گزارش داده که به‌دلیل تشدید تحریم‌های آمریکا علیه صنعت هوانوردی ایران، انتظار می‌رود تمام پروازهای شرکت‌های ایرانی به ترکیه لغو شوند. یک منبع نزدیک به صنعت هوانوردی ایران نیز این موضوع را تأیید کرده است. با این حال،
مقامات ترکیه هنوز چنین تصمیمی را رسماً اعلام نکرده‌اند
و یک منبع دیگر نیز نتوانسته این خبر را تأیید کند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24402" target="_blank">📅 14:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اینوستینگ :
بیت‌کوین امروز تا حدود
۸۳ هزار دلار
عقب‌نشینی کرد و حدود ۱.۷ درصد کاهش داشت. افزایش بازده اوراق خزانه آمریکا و نبود پیشرفت محسوس در مذاکرات ایران و آمریکا، اشتهای سرمایه‌گذاران برای دارایی‌های پرریسک را کاهش داده است. اتریوم نیز حدود ۲ درصد افت کرد و آلت‌کوین‌ها عمدتاً در مسیر نزولی قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24401" target="_blank">📅 14:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رویترز:
طلا امروز حدود
۳ درصد سقوط کرد و به پایین‌ترین سطح بیش از هفت هفته اخیر رسید
؛ علت اصلی، افزایش قیمت نفت و بالا رفتن انتظارات برای افزایش نرخ بهره عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24400" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اورشلیم پست:
منابع حوثی مدعی شده‌اند حملات عربستان به مناطقی در تعز تلفات سنگینی برجای گذاشته و حوثی‌ها تهدید کرده‌اند در واکنش،
پل‌های داخل عربستان
را هدف قرار دهند. اصل حمله و میزان تلفات هنوز از سوی منابع مستقل تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24399" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مقوا ای آی : انقلاب اسلامی
سلطه و وابستگی ایران به قدرت‌های خارجی را پایان داد
و ایران را به کشوری مستقل تبدیل کرد. او سیدحسن نصرالله را شخصیتی کم‌نظیر دانست و گفت
پرچم او اکنون در دستان شیخ نعیم قاسم
است. وی مخالفان مقاومت لبنان را به
بی‌تدبیری و حتی خیانت
متهم کرد. خامنه‌ای ایران را
قدرت اول جهان بر اساس «محاسبات الهی»
خواند و مدعی شد دشمنان ایران پس از ضربات رزمندگان، دیگر حتی از
دریای عرب جلوتر نمی‌آیند و به‌زودی از این منطقه نیز خارج خواهند شد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24398" target="_blank">📅 14:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خبرگزاری
NBC:
در جزئیات تازه‌ای که امروز منتشر شده، اعلام شد در
۲۳ شهریور ۱۴۰۵ (۱۴ سپتامبر ۲۰۲۶)
، یک موشک کروز ضدکشتی ایران در
تنگه هرمز
به یک شناور حامل نیروهای آمریکایی اصابت کرده و
۸ تفنگدار دریایی آمریکا
زخمی شده‌اند. به گفته سه مقام آمریکایی، هر ۸ نفر دچار
آسیب ناشی از استنشاق دود
شده‌اند و برخی نیز علائم
ضربه مغزی و احتمال آسیب ناشی از موج انفجار
داشته‌اند. این افراد شامل ۷ سرباز و یک افسر از نیروهای تفنگدار دریایی بودند. هیچ‌یک از مجروحان وضعیت وخیمی نداشتند و هر ۸ نفر پس از مدت کوتاهی به خدمت بازگشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24397" target="_blank">📅 14:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وحیدی :  اشتراک چت جی‌پی‌تی مون رو تمدید کردیم ، یه پیغام از مقوا براتون میزارم تا ساعاتی دیگه
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24396" target="_blank">📅 13:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دلار ۲۴۴،۰۰۰ تومان (رکورد تاریخی)
تتر ۲۴۴،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24395" target="_blank">📅 13:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24393">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">در فرودگاه بین‌المللی مهرآباد تهران طی ساعات گذشته، یک فروند هواپیمای C-130 هرکولس متعلق به نیروی هوایی ارتش جمهوری اسلامی و یک فروند هواپیمای ایلیوشین-۷۶ (Il-76) متعلق به نیروی هوایی ارتش یا نیروی هوافضای سپاه پاسداران در این فرودگاه به زمین نشسته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24393" target="_blank">📅 13:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رئیس سازمان هواپیمایی کشوری با اشاره به تلاش‌های مستمر این سازمان برای احیای مسیرهای پروازی، از رایزنی با وزارت امور خارجه و ثبت شکایت رسمی نزد سازمان بین‌المللی هوانوردی غیرنظامی (ایکائو) در واکنش به محدودیت‌های اعمال‌شده علیه صنعت هوانوردی ایران خبر داد.
@WarRoom
یاشار : بدجور دارن تو باتلاق دستو پا میزنند ولی هی میرن پایین تر</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24392" target="_blank">📅 13:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نرخ دلار ۲۴۱،۰۰۰ تومان (رکورد تاریخی)  تتر  ۲۴۰،۰۰۰ تومان(رکورد تاریخی)  بیتکوین ۸۳،۱۵۸ $ انس جهانی طلا ۴،۱۶۳ $ نفت برنت ۹۸،۷۳$ @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24391" target="_blank">📅 12:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43823eee78.mp4?token=U4cLxMHaM6cdtULypTPaLm-OogckYV93B1hk2OijRLZiZ10GWh0nxoGmHMUEv_D6D10rSzDphd9LTNs8VZ2Hisg-ORL8ksNssT9Cc1lH4M9le_WJPayFzspB-1gHoMFQCeMG1ZQpqWHyqibHYM09_BuyzbtGf7PdQsORHFF6GQOXV0LD8DmjUZUQpIcrmATBz5cBvZXsHYLBM7g_dg27cFWenT5JVSZ1Cyg7Tuh0B7Hy27sPai9rVAB-TwkODUWolRAfHsCV5Lj5e_NEeidDbi5hiq9Wnn-7-l98kaNdiUjo-zN8UHuhwLqqpYlaw2H4vA88bfzjF4rb-MtQIaG2Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43823eee78.mp4?token=U4cLxMHaM6cdtULypTPaLm-OogckYV93B1hk2OijRLZiZ10GWh0nxoGmHMUEv_D6D10rSzDphd9LTNs8VZ2Hisg-ORL8ksNssT9Cc1lH4M9le_WJPayFzspB-1gHoMFQCeMG1ZQpqWHyqibHYM09_BuyzbtGf7PdQsORHFF6GQOXV0LD8DmjUZUQpIcrmATBz5cBvZXsHYLBM7g_dg27cFWenT5JVSZ1Cyg7Tuh0B7Hy27sPai9rVAB-TwkODUWolRAfHsCV5Lj5e_NEeidDbi5hiq9Wnn-7-l98kaNdiUjo-zN8UHuhwLqqpYlaw2H4vA88bfzjF4rb-MtQIaG2Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏دیوید پردو، سفیر ایالات متحده در چین: شی جین پینگ در ماه مه موافقت کرد و در اینجا نیز آن را تکرار کرد که آنها از عدم وجود سلاح هسته‌ای در ایران حمایت می‌کنند، این بسیار مهم است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24390" target="_blank">📅 12:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دریادار سیاری، از فرماندهان ارشد ارتش: «غرب تنگه هرمز و خلیج فارس تحت کنترل کامل نیروی دریایی سپاه پاسداران قرار دارد. در شرق تنگه نیز کنترل کامل در اختیار نیروی دریایی ارتش ایران است.»
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24389" target="_blank">📅 12:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رسانه های رژیم : بیژن مرتضوی به ایران بازگشت
@WarRoom
تکذیب کرد</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24388" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عراقچی : من جام خوبه نمیام ، مرسی اه @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24387" target="_blank">📅 12:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سفیر آمریکا در اسرائیل : واشنگتن به‌زودی ساخت سفارت خود در اورشلیم را آغاز می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24386" target="_blank">📅 12:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24385">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b880b3de21.mp4?token=FR7w-Ex9g7yLVZew4E9E1fjeyfqAGm79UxO4sqF4DjGWw_bHfh8UDEQYepudmCMf3BOwzXDqoebt88mLbw0-jJAPQQqXDX77Au8uhd5xpLO_PWWQtB8dNm2HwnY-gOPZ0fW7naOHq5R3Y_WSpZvdmdeOFaKSTfK075N1a99FHR0M6NDT7bBmaRB1saehcNTyBpmAw4n0gU8o6J5iKEzNItdePTojbCEQnuPcpgA4Rn3cg45rRzY0SZYHoXET-v88ZMbpCby0YaOxDBxFBNmbbXNm7Wfc9ezyvn8MWOfdtd-lRFOI9ndJpJSl9fDzopvSx1sG3-mtnaGLVOv0e5fVdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b880b3de21.mp4?token=FR7w-Ex9g7yLVZew4E9E1fjeyfqAGm79UxO4sqF4DjGWw_bHfh8UDEQYepudmCMf3BOwzXDqoebt88mLbw0-jJAPQQqXDX77Au8uhd5xpLO_PWWQtB8dNm2HwnY-gOPZ0fW7naOHq5R3Y_WSpZvdmdeOFaKSTfK075N1a99FHR0M6NDT7bBmaRB1saehcNTyBpmAw4n0gU8o6J5iKEzNItdePTojbCEQnuPcpgA4Rn3cg45rRzY0SZYHoXET-v88ZMbpCby0YaOxDBxFBNmbbXNm7Wfc9ezyvn8MWOfdtd-lRFOI9ndJpJSl9fDzopvSx1sG3-mtnaGLVOv0e5fVdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحرکات نظامی امریکا در عمان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24385" target="_blank">📅 11:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز : اسرائیل اعلام کرده پس از پرتاب یک
پهپاد انفجاری حزب‌الله
به سمت نیروهایش، مواضع حزب‌الله را در جنوب لبنان هدف قرار داده است.
حملات اسرائیل در مناطق مختلف جنوب لبنان از جمله
صور، نبطیه، مرجعیون و بنت جبیل
ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24384" target="_blank">📅 11:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ارتش اسرائیل اعلام کرده یک
تک‌تیرانداز حماس
را که به گفته ارتش در حال برنامه‌ریزی حملات بود، در جنوب غزه هدف قرار داده و کشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24383" target="_blank">📅 11:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رویترز:
ایران همچنان بر
طرح هفت‌روزه بازگشایی تنگه هرمز
پافشاری می‌کند و می‌گوید حاضر نیست شروط خود را کاهش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24382" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نرخ دلار ۲۴۱،۰۰۰ تومان (رکورد تاریخی)
تتر  ۲۴۰،۰۰۰ تومان(رکورد تاریخی)
بیتکوین ۸۳،۱۵۸ $
انس جهانی طلا ۴،۱۶۳ $
نفت برنت ۹۸،۷۳$
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24381" target="_blank">📅 10:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb747ba428.mp4?token=bRa4AKf9bVVaYwijD38US27AmOoziY29dBBU_IVnrAVUq9bzqR8I19Dpp-pdccfIBOj8VB9R79PXW4WeoDtoFac2DkcDPC2bRazHivomOdzP_Mq_hA9F0j_Q5YbXkJkuMLiXTRbbvSWPwfNCWukzkGkRds4VJb05aBZig8BaOyrG53p2nWwuQOnXXYfgGzBL_AwvOlLZHLPGxgMyVwCf-hiib5iv5xpPJSyhEGSN54ZyIHV-fTVjsr5Dv5lWV0HH2o2f-BencuNO9U33NoondnXiBGXocE2KDqd5MXivcOD1sCe41WcolLD-bygb307h-JEBK0rAPDKrpKOp_L5wRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb747ba428.mp4?token=bRa4AKf9bVVaYwijD38US27AmOoziY29dBBU_IVnrAVUq9bzqR8I19Dpp-pdccfIBOj8VB9R79PXW4WeoDtoFac2DkcDPC2bRazHivomOdzP_Mq_hA9F0j_Q5YbXkJkuMLiXTRbbvSWPwfNCWukzkGkRds4VJb05aBZig8BaOyrG53p2nWwuQOnXXYfgGzBL_AwvOlLZHLPGxgMyVwCf-hiib5iv5xpPJSyhEGSN54ZyIHV-fTVjsr5Dv5lWV0HH2o2f-BencuNO9U33NoondnXiBGXocE2KDqd5MXivcOD1sCe41WcolLD-bygb307h-JEBK0rAPDKrpKOp_L5wRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون پل ستار‌خان شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24380" target="_blank">📅 10:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007a727a10.webm?token=Tc8zJzj8hqjbjAUO3AXKOiKLcCkxJVXFLHwzVoStlp_JqIOYr15RL7IOMEhR4bQzh_IabnGrteF9P3Olcma7Tz39sVltAkBW5E3IklGkSdlY3Swx9bFGezyuqyjY9dI0-ea1w9YyQCxndrofxUmrqSYRuLR91fTyRWbsjwzlMQSi01ArcClcaHSjTKTeWpuScomsBz5Bj2_Q81rdMw2vswTPJuZc2IWq3ZKGgeBPIhstdjKoifCnKLJTqEIANXyVmI-4QOPcdvcre7AbTLaim1Ucg5dIf2VuWagK6wFve-RRe_2QbNtLWyQqyEO3W2N89CE8E8fcCmTmRi3gRXuWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007a727a10.webm?token=Tc8zJzj8hqjbjAUO3AXKOiKLcCkxJVXFLHwzVoStlp_JqIOYr15RL7IOMEhR4bQzh_IabnGrteF9P3Olcma7Tz39sVltAkBW5E3IklGkSdlY3Swx9bFGezyuqyjY9dI0-ea1w9YyQCxndrofxUmrqSYRuLR91fTyRWbsjwzlMQSi01ArcClcaHSjTKTeWpuScomsBz5Bj2_Q81rdMw2vswTPJuZc2IWq3ZKGgeBPIhstdjKoifCnKLJTqEIANXyVmI-4QOPcdvcre7AbTLaim1Ucg5dIf2VuWagK6wFve-RRe_2QbNtLWyQqyEO3W2N89CE8E8fcCmTmRi3gRXuWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24379" target="_blank">📅 10:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1529c155.mp4?token=JRrYrw-PtSkUU_3MQwyERVhWOkmuD9v11Rkc2MtoIqVf84OEVf101pNAinGnwavlQdTngh0Y3S_3Uf91IcUvOQwV0tLuW-rv9m_dZmIOJb8zjH7F2zFW5WJe-MuJvd2dDXNXcLfTkrm5k9eeU1TES5WtDJOajp2ws9785bzIPwUMcEBbQhHyZhbz3YuBdL-v72rzNGI4RgdhCGyuKoONKQYzmtGMVjg9hxcfOsgibCu8MlHHGXRjqi6wusUF91G8Pf0Yf68isHoj9gvSgapspBW8hmkqP0xYI_M3eax5APr9Ri0M9GJaKfPhyxi2WUOym2H3m60k_KwIXu4GL7dyAxqJk7T9xqLvevaQ0639c_9nXrVbsAa1C86vwHKqcjLBUPoa7FxcECsvItJwWI7GTcPzFoTJz-Ah5TqUVBi9dpcgalFoZeGd3jOVHDuzWMUysGuEnz3cfh52dMInGtoFEanyTxFFxslhnX25q8esSWDhby22SO4RTqRdeWqERl2tKxrVaV_oFy2xWQAPYQgtPrzt5Hn4zo64pjirLgA2NGCit3-CZgFcou-SEZsvezrs5T0mWMmaGKEyI4g22nKd5ctvqjyQSJWrDsbIuP95zOOqvR2EYKALC0YzsefEDfBk4goDCz_07fbqP9JbzXtEikNMo2QHkeqnOLRfZNRWAcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1529c155.mp4?token=JRrYrw-PtSkUU_3MQwyERVhWOkmuD9v11Rkc2MtoIqVf84OEVf101pNAinGnwavlQdTngh0Y3S_3Uf91IcUvOQwV0tLuW-rv9m_dZmIOJb8zjH7F2zFW5WJe-MuJvd2dDXNXcLfTkrm5k9eeU1TES5WtDJOajp2ws9785bzIPwUMcEBbQhHyZhbz3YuBdL-v72rzNGI4RgdhCGyuKoONKQYzmtGMVjg9hxcfOsgibCu8MlHHGXRjqi6wusUF91G8Pf0Yf68isHoj9gvSgapspBW8hmkqP0xYI_M3eax5APr9Ri0M9GJaKfPhyxi2WUOym2H3m60k_KwIXu4GL7dyAxqJk7T9xqLvevaQ0639c_9nXrVbsAa1C86vwHKqcjLBUPoa7FxcECsvItJwWI7GTcPzFoTJz-Ah5TqUVBi9dpcgalFoZeGd3jOVHDuzWMUysGuEnz3cfh52dMInGtoFEanyTxFFxslhnX25q8esSWDhby22SO4RTqRdeWqERl2tKxrVaV_oFy2xWQAPYQgtPrzt5Hn4zo64pjirLgA2NGCit3-CZgFcou-SEZsvezrs5T0mWMmaGKEyI4g22nKd5ctvqjyQSJWrDsbIuP95zOOqvR2EYKALC0YzsefEDfBk4goDCz_07fbqP9JbzXtEikNMo2QHkeqnOLRfZNRWAcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
به‌جز نفت، که قیمت آن از دوران دولت بایدن پایین‌تر است، دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم، چون آنها کاملاً نابود شده‌اند.
اما به‌جز نفت، قیمت همه‌چیز در حال کاهش است و روند کاهش ادامه دارد. ما بدترین تورم تاریخ کشورمان را به ارث بردیم، اما تورم اکنون به‌سرعت در حال کاهش است. کشورمان وضعیت بسیار خوبی دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24378" target="_blank">📅 05:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e4b6efa2.mp4?token=PxXj-Dt5Hcp7zXv8H68aapWEgb9ubpljUd2ld6Esp-cAoN2kZj4FQOfsafHlUXM2SVdTsjAn4WWEgkTIG6kcknRvLweaPQRlj0Eh-dwB_jQ_U8WY6ThEi3pjkrCEJQrgWIcIt3rM_ONhaM9hOOC3esPDW5Ml-a84RXwXx5THTGn6Z7XPLj0SCUjSDFPhokaQBl-CVtp6nVkQzXWPuOqo4H1e3MjziR-CTUyWL23E6A0AOL3ZNBr4SS7p_PfUt6FklpmltDgMiv7r3Qi4VmQBwT4Dul0FjTbLJ2E3Og64k_Lzl8sSe7fKfH5Pf32bH0n5NpZudaW4-2UH-u7LhD5fiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e4b6efa2.mp4?token=PxXj-Dt5Hcp7zXv8H68aapWEgb9ubpljUd2ld6Esp-cAoN2kZj4FQOfsafHlUXM2SVdTsjAn4WWEgkTIG6kcknRvLweaPQRlj0Eh-dwB_jQ_U8WY6ThEi3pjkrCEJQrgWIcIt3rM_ONhaM9hOOC3esPDW5Ml-a84RXwXx5THTGn6Z7XPLj0SCUjSDFPhokaQBl-CVtp6nVkQzXWPuOqo4H1e3MjziR-CTUyWL23E6A0AOL3ZNBr4SS7p_PfUt6FklpmltDgMiv7r3Qi4VmQBwT4Dul0FjTbLJ2E3Og64k_Lzl8sSe7fKfH5Pf32bH0n5NpZudaW4-2UH-u7LhD5fiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
می‌توانید درباره حملاتی که در بریتانیا رخ داده و مظنون مهاجری که در این ارتباط بازداشت شده، اطلاعات بیشتری بدهید؟ آیا ارتباطی با ایران وجود دارد؟
دونالد ترامپ:
ما همه چیز را درباره او می‌دانیم و به‌زودی اطلاعات بیشتری درباره این موضوع خواهید شنید.
ما آنها را گرفتیم.
@WarRoom
یاشار ، تکمیلی: تمام رسانه های جهان به اتفاق میگن کاره ایران بوده حتمأ سر نخ های پیدا شده و  عملیات توسط یک زن کشاورز که به ۳ ون مشکوک میشه و گزارش میکنه لو میره</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24377" target="_blank">📅 05:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74dac714cd.mp4?token=a6LOkijv9xQNxJyO3M2Q-jAWtfvcXfGB0KpNuE9KYF_t6RAKh-ABPAqZtU-1wCIUGqrLakONDgGV2dYqbQP2L1qXSVW_2k_tGKUgB2uwir_uWE2Np3YictPsGLRokYVbpHmMAiigEV-69lNA6ddqFv42x9tSCXz4fBH6QwQb1vWsQq5yJtZax5U1khDy_qjflKgPmnMtx5wyVeqXxaN2XIrRkIJu4DrATeDjet_tfrt8VXiLpphbJLKhDPFFXEN7hlmKKDLRmctyjhwXh6byGZHWjOgt4Ht_5U6DBDa3bE48SCTAzjGLlaSkuFwONrgGQ3BXvqUbTqPIpAAMo5tjIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74dac714cd.mp4?token=a6LOkijv9xQNxJyO3M2Q-jAWtfvcXfGB0KpNuE9KYF_t6RAKh-ABPAqZtU-1wCIUGqrLakONDgGV2dYqbQP2L1qXSVW_2k_tGKUgB2uwir_uWE2Np3YictPsGLRokYVbpHmMAiigEV-69lNA6ddqFv42x9tSCXz4fBH6QwQb1vWsQq5yJtZax5U1khDy_qjflKgPmnMtx5wyVeqXxaN2XIrRkIJu4DrATeDjet_tfrt8VXiLpphbJLKhDPFFXEN7hlmKKDLRmctyjhwXh6byGZHWjOgt4Ht_5U6DBDa3bE48SCTAzjGLlaSkuFwONrgGQ3BXvqUbTqPIpAAMo5tjIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ژنرال جک کین به مارک لوین در فاکس نیوز:
آمریکا و اسرائیل همین حالا
توان هوایی لازم برای تغییر چشمگیر روند درگیری در داخل ایران
را در اختیار دارند.
او پیشنهاد می‌کند معترضان ایرانی علیه
مراکز سپاه پاسداران
دست به اقدام مسلحانه بزنند و همزمان هواپیماهای آمریکایی و اسرائیلی نیز از آسمان از آنها پشتیبانی کرده و
نیروهای کمکی حکومت
را هدف قرار دهند. او می‌گوید: «
ما داریم این کار را سخت‌تر از چیزی که هست می‌کنیم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24376" target="_blank">📅 04:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrXdAwe7l-NtsIoxwzWzI2tsFKeq-mk40S3FJuNfv_kT5MFwRbCrbiejS7DGLcL23LXkXMaKIbUyBpVpS4vkNHtva6nNS-APgUC3LFT0vB0Lb-QrXb18qJkTjis05kBCKVjduXPqKr0AbC6ZHQhCQV9vfRKBdh1MIZmaCbgGtq0epV1pGdajCD6KdxefFRMBZTBZqymQkbaBCoyXc8Zg6WGzXUnIpDC-nr7aMkOXI0iGlsE13TTBOKhqQhQDJTQAFUBO3B1Y-M0OPxWwZnv8rTsAOEsReHOJQY9sN4ehLeouw10I8Y6rF2bvSqR6XPXOCzWTeMOPUohi-s-hqzIWbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : بمب‌افکن‌های راهبردی بی‌-۱بی آمریکا در پایگاه فیرفورد بریتانیا؛ در انتظار فرمان احتمالی ترامپ برای دور جدید حملات به ایران! یک بالگرد رسانه‌ای که برای پوشش عملیات تیم‌های خنثی‌سازی مهمات انفجاری در منطقه ولفورد به پرواز درآمده بود، بمب‌افکن‌های…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24375" target="_blank">📅 04:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24374">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">از تبریز دارن موشک/پهپاد میزنند اربیل عراق  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24374" target="_blank">📅 02:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">از تبریز دارن موشک/پهپاد میزنند اربیل عراق
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24373" target="_blank">📅 02:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24372" target="_blank">📅 02:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24371">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a7eec46a.mp4?token=NARDOvGrWU0n7TJNtI_6GsTguODHrORZNz4noOZR8YgHgpRckOu1WOmXcCQy1LPohZAIIHDJ9GvQWHdBL379UrISc2ohoRU9IjHVFDczI-87rVrXiCIveG6F3Wvg41_lShTwKUu1V0ysR-v7AlqHwMB5wB0dCLd71wsfT7IMJ-4d7IH3_J7Pp0B12sb5s0Yy-ucrogTHTMPmCArtrL_qa6yXWD4c2Z83OjUTOOTgK-ZSMLwZcDUzkH4wqtbT9j0t8_DZEA7k3-k0z1V9KrWegfgnSweyJ6XB8Ijv9Kif06W_2XT8RxxK2G_7L9zoHuPL4ebgtKJluZmvYFjmS5Yjk5qqzyQmkY21PZ7cgPhZA_XNMNuc-F3ujQUCYihPabui64vAHRhRSgZmTfdPn0QctWo1aHAF3ZXcF9gyQkNWy1OLlIG6rklanlqnPBurZJT6WpjA9_LwABfIKplmFg6PChQxu8XYYFQly9kKlqspm7YELYvowqenkqX3Am7GyAx96bg6_OwuKWg1W8TKJ5MiBiAA2GvNBDmRbq9jpHIQc3-AAxHbtia_D9VDsZvSXo_yJqlMDIURVHIZLAGH6RuIks4J0V7VP34fnCPGPr-WRrLxOooJKv2QMvVso031Emc9c4aN4XP2tb0So931shzLZy6lTzhopdZ7lYHXRXWqa_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a7eec46a.mp4?token=NARDOvGrWU0n7TJNtI_6GsTguODHrORZNz4noOZR8YgHgpRckOu1WOmXcCQy1LPohZAIIHDJ9GvQWHdBL379UrISc2ohoRU9IjHVFDczI-87rVrXiCIveG6F3Wvg41_lShTwKUu1V0ysR-v7AlqHwMB5wB0dCLd71wsfT7IMJ-4d7IH3_J7Pp0B12sb5s0Yy-ucrogTHTMPmCArtrL_qa6yXWD4c2Z83OjUTOOTgK-ZSMLwZcDUzkH4wqtbT9j0t8_DZEA7k3-k0z1V9KrWegfgnSweyJ6XB8Ijv9Kif06W_2XT8RxxK2G_7L9zoHuPL4ebgtKJluZmvYFjmS5Yjk5qqzyQmkY21PZ7cgPhZA_XNMNuc-F3ujQUCYihPabui64vAHRhRSgZmTfdPn0QctWo1aHAF3ZXcF9gyQkNWy1OLlIG6rklanlqnPBurZJT6WpjA9_LwABfIKplmFg6PChQxu8XYYFQly9kKlqspm7YELYvowqenkqX3Am7GyAx96bg6_OwuKWg1W8TKJ5MiBiAA2GvNBDmRbq9jpHIQc3-AAxHbtia_D9VDsZvSXo_yJqlMDIURVHIZLAGH6RuIks4J0V7VP34fnCPGPr-WRrLxOooJKv2QMvVso031Emc9c4aN4XP2tb0So931shzLZy6lTzhopdZ7lYHXRXWqa_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">WarRoom with Yashar : Winter is Coming
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24371" target="_blank">📅 01:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc92790f11.mp4?token=eO16Oxtl71pStj87hTf-_MxiayFZ2lH1dNBNNDusDip612TQRCCSlzl2HsyIC6ajkjpzlTdPghoj-ZQldmhHwEfKlRy2JB7Wj7JCLm6TAoRIckHOXGN9svuP_2dUEOjQOLJmDalpEBQn-FL45yiPMp7_YEBKo-yBmFrXRRdlUotkbkxQ6iPmRR8-utkKUMfcWxYaI4SAXLuyXZEE89WcjYQ-AVs0jEThkr2XVEpo_oSIzVfsvM9mPc1rk-9GIkRcj4P2HzcD4zrTVOU4kkyAgklv3nVj4PwZh-_5FAgiru-RAd5sAykkfsb0n_kBGD3F2RetSOgH2YQRY_CCse6sxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc92790f11.mp4?token=eO16Oxtl71pStj87hTf-_MxiayFZ2lH1dNBNNDusDip612TQRCCSlzl2HsyIC6ajkjpzlTdPghoj-ZQldmhHwEfKlRy2JB7Wj7JCLm6TAoRIckHOXGN9svuP_2dUEOjQOLJmDalpEBQn-FL45yiPMp7_YEBKo-yBmFrXRRdlUotkbkxQ6iPmRR8-utkKUMfcWxYaI4SAXLuyXZEE89WcjYQ-AVs0jEThkr2XVEpo_oSIzVfsvM9mPc1rk-9GIkRcj4P2HzcD4zrTVOU4kkyAgklv3nVj4PwZh-_5FAgiru-RAd5sAykkfsb0n_kBGD3F2RetSOgH2YQRY_CCse6sxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریاسالار Daryl Caudle، رئیس عملیات نیروی دریایی: ناو هواپیمابر یو‌اس‌اس تئودور روزولت (CVN-71)، از ناوهای اتمی کلاس نیمیتز، در حال ترک سن‌دیگو برای اعزام به خاورمیانه است. این ناو به همراه گروه رزمی خود و بال هوایی یازدهم ناوگان، قرار است برای یک مأموریت طولانی‌مدت به منطقه سنتکام اعزام شود؛ مدت این مأموریت دست‌کم حدود ۷ ماه برآورد شده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24370" target="_blank">📅 01:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo1WdGHa4POBnT6gbpeDiUmn0ZCgHIyIeIfg5Dhi8lGoVjQXrZ-4v5jg-NbiFXrce5PeIuh4oUGUgTKN79uL3UgEphbU3oOR6gt1QG6s7Z9cvtsZbAV9z53yjz_EhD7Jnem_h_xBzMmo3AtMTl1a_SfM5ZzPvT-Zg7VA6smfDjXIgoCSkA4WkdPj0tPGrCtETUfv0fT4VC2O1cPLXrid1bFIsoWGG88BEMwRs-B-boKqTZHlWxaGa6SjxgNYPjBlhXI0ehyX2zvj7VYkaK0DDuysA6QkJrbv-Iitp7fFijb21FP-INbESewcIWLwHnHmWm-FhgpeBORD1UnJisbBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با خرافات : تمام دایرکت پیغام اینه که ترامپ کلاه جنگ سرشه ( البته واقعا هم ترامپ اکثرا اتاق جنگ
مارالاگو
میره این کلاه سرشه و روز اول جنگ هم بود )
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24369" target="_blank">📅 01:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52b1b75b8.mp4?token=SYLXfbm-4DAzZRs0HEBBjQ40Qak5OPyoxckVCNTeO4_UWrfurr3Z6omU41F44p1GI8j_-RyS6Q0cbIrMPaTuI8tYqmKrx3AykSovtLphh_9auFntYjF0exI_I8K-1O_0IzBjgTsIj_286aki2UdXwvI1DYhylMb-iKRR5T79t0tcNSIMZ6pJsbReKSDDvSZSv6_i01MDHciPPlfzUvfVfbriUJ_P6gcs03WHh2lbd2bSHuGZb0SwIeU09pPke_Y46QGGP4B_zcqeDeibt3a2L6GGDdUfecgO_7imK8nfmlw8jTH04RFGr-THFs-0e0lusi77IC6qztvEDMKidDPwJLhXkgY-u86lyNNsaLz2QYC-uq35uMlTSds7u7j3qx8O9s2SeftDRruwutVB9o9qNb6_rIQ5uXkTEL9wCrVmSbmb6VcDpN7j6_rWH_6Mx_FMxJ-f-Hd5pxMpqWNCiebblPESrWGzbQiFZVwawHxqM2xRJVAXijb5ueGiN8iiCflkEcRH4-jSkYPzGGsWEBXBUlQ4KAz5OnwRI87bIV7YK-m2o55FUooB8Yp_sRbiW4k2uVz71A6nP3uU4W71_E9ngl_i0CG9wVexLYm018Sq3sOHvPC4mXMyq0LfcnDUjTpygb2RizbdbYmDToC_eHr7HMVCr5yn69QOMmqQFCsSw9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52b1b75b8.mp4?token=SYLXfbm-4DAzZRs0HEBBjQ40Qak5OPyoxckVCNTeO4_UWrfurr3Z6omU41F44p1GI8j_-RyS6Q0cbIrMPaTuI8tYqmKrx3AykSovtLphh_9auFntYjF0exI_I8K-1O_0IzBjgTsIj_286aki2UdXwvI1DYhylMb-iKRR5T79t0tcNSIMZ6pJsbReKSDDvSZSv6_i01MDHciPPlfzUvfVfbriUJ_P6gcs03WHh2lbd2bSHuGZb0SwIeU09pPke_Y46QGGP4B_zcqeDeibt3a2L6GGDdUfecgO_7imK8nfmlw8jTH04RFGr-THFs-0e0lusi77IC6qztvEDMKidDPwJLhXkgY-u86lyNNsaLz2QYC-uq35uMlTSds7u7j3qx8O9s2SeftDRruwutVB9o9qNb6_rIQ5uXkTEL9wCrVmSbmb6VcDpN7j6_rWH_6Mx_FMxJ-f-Hd5pxMpqWNCiebblPESrWGzbQiFZVwawHxqM2xRJVAXijb5ueGiN8iiCflkEcRH4-jSkYPzGGsWEBXBUlQ4KAz5OnwRI87bIV7YK-m2o55FUooB8Yp_sRbiW4k2uVz71A6nP3uU4W71_E9ngl_i0CG9wVexLYm018Sq3sOHvPC4mXMyq0LfcnDUjTpygb2RizbdbYmDToC_eHr7HMVCr5yn69QOMmqQFCsSw9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«مشکل بزرگ این است که
پالایشگاه‌های روسیه در حال منفجر شدن هستند.
این در واقع یک مشکل خاورمیانه نیست؛ بیشتر مربوط به
روسیه و اوکراین
است که با یکدیگر درگیرند.
اوکراین در حال
هدف قرار دادن پالایشگاه‌های گازوئیل روسیه
است، چون روسیه بخش زیادی از فرآوری و پالایش را انجام می‌دهد. بنابراین این موضوع واقعاً جالب است.
من با رئیس‌جمهور زلنسکی صحبت کردم و گفتم:
«باید در مورد حمله به پالایشگاه‌ها کمی دست نگه داری.»
او هم گفت:
«احتمالاً همین کار را خواهیم کرد.»
»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24368" target="_blank">📅 01:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5f4fc33c.mp4?token=OsK1EmWB4eKcisi9XfY48XTNPChZRoasZ4kg3Rb3IbfWNloiwWKY49LhVDfyxsOPdQHSA57BFCwtMAuOndNZUyKOBYhXZXAI1tn44vpP1NaYrwsTh5RCOVQBZDJSb76_yPuv62oNyRxZbCjQ4Rab5ONJGzbkt3h13GVA4HkodttPbRQbC9Pod61anHzRAo4q_wMuxSkYoZZKpg8NIKiddZbB4CHElW6SUY_bkE1Jzjcxp87NPkcJ88bLHbm1UsHuyOqQQrw44tJolqqzbKVJ5-vaKa7ShsxQxlXc27zNzfH2_gMyZVkf2DZSq2xO3UCOHcwxpK2opBkhB5rdfRFOSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5f4fc33c.mp4?token=OsK1EmWB4eKcisi9XfY48XTNPChZRoasZ4kg3Rb3IbfWNloiwWKY49LhVDfyxsOPdQHSA57BFCwtMAuOndNZUyKOBYhXZXAI1tn44vpP1NaYrwsTh5RCOVQBZDJSb76_yPuv62oNyRxZbCjQ4Rab5ONJGzbkt3h13GVA4HkodttPbRQbC9Pod61anHzRAo4q_wMuxSkYoZZKpg8NIKiddZbB4CHElW6SUY_bkE1Jzjcxp87NPkcJ88bLHbm1UsHuyOqQQrw44tJolqqzbKVJ5-vaKa7ShsxQxlXc27zNzfH2_gMyZVkf2DZSq2xO3UCOHcwxpK2opBkhB5rdfRFOSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
آیا انجام حملات پیش از انتخابات میان‌دوره‌ای هنوز روی میز شماست؟
ترامپ:
«نمی‌خواهم درباره آن چیزی بگویم. منظورم این است که
ممکن است چنین اتفاقی بیفتد
، اما نمی‌خواهم بیشتر از این درباره‌اش صحبت کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24367" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc59060499.mp4?token=SSK4uODOe9Q2lQASXGYkCvR1SEDqq6Y7P2PMhhYpSqorF0QKkIx_LcQym0wQBzcv7RTQYwaRuIYZswd4Of409rDLIhiIcCnlv2e6WSzbb1g4sqGH65Mide6xlZ2KY2tjDZUOPUtA2MEHsEyfJlKOM9gj1nBXnY-WYCSoU2epRWLJ8OPSEEL2NHHxSUXXEI_R5D3Lz1DES6YuU30qHYlHDDFDr0AHLbfQvJjVZNcXg7LTVHzMOk4nCZ2Czg-voLi-v9nnf7MRVPGEn4iC1WHqteHqPVm932cCgSdTtN4jt9Fquq2kxihN30MKwGFG_BGnRFqdLvJFkb8H7Ylxd8Cong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc59060499.mp4?token=SSK4uODOe9Q2lQASXGYkCvR1SEDqq6Y7P2PMhhYpSqorF0QKkIx_LcQym0wQBzcv7RTQYwaRuIYZswd4Of409rDLIhiIcCnlv2e6WSzbb1g4sqGH65Mide6xlZ2KY2tjDZUOPUtA2MEHsEyfJlKOM9gj1nBXnY-WYCSoU2epRWLJ8OPSEEL2NHHxSUXXEI_R5D3Lz1DES6YuU30qHYlHDDFDr0AHLbfQvJjVZNcXg7LTVHzMOk4nCZ2Czg-voLi-v9nnf7MRVPGEn4iC1WHqteHqPVm932cCgSdTtN4jt9Fquq2kxihN30MKwGFG_BGnRFqdLvJFkb8H7Ylxd8Cong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
درباره ممنوعیت صادرات گازوئیل چطور؟
ترامپ:
«ما این موضوع را
خیلی جدی در حال بررسی
هستیم. چنین اقدامی گاهی می‌تواند باعث
افزایش جزئی قیمت بنزین خودروها
شود.
بنابراین با جدیت در حال بررسی آن هستیم و
ممکن است این کار را انجام دهیم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24366" target="_blank">📅 01:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آکسیوس: تحرکات و آماده‌سازی‌های نظامی آمریکا در منطقه، احتمال اقدام نظامی جدید علیه ایران را افزایش داده است.
ترامپ نیز گفته همچنان گزینه ازسرگیری حملات علیه ایران را در نظر دارد
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24365" target="_blank">📅 01:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f7397463.mp4?token=oUW84VoocoveZwzcEFFH3BWCHAQEVXJSSq36oKo1EwOZFdtYhgiffc99QxTSbPfCbOJNTe8ERzOdSWMTOGD303BPKR9SMh6GoPXsSTO_r4DQnV6C3uU6H_Ej8zCmvvIhTfGw9qfhM_J6GtFUTz5ab00Vj2ywtgOepdzpYEsBz7VTb0LFeMqxscE5u2AUJRGTqYjsVIT986F99eS4sSQ3rzOEUPgCDLajy_vfodrMYXP4FmajPDjL8MWR1YXIoNWPnYAAZp5cZHRlgjN9Nm5HKy4gCfsPsmdWOAYHrNa9EtjkW2XusoOKrB8_4OxChhHVbVcBRzPxr9-m9c9wljgbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f7397463.mp4?token=oUW84VoocoveZwzcEFFH3BWCHAQEVXJSSq36oKo1EwOZFdtYhgiffc99QxTSbPfCbOJNTe8ERzOdSWMTOGD303BPKR9SMh6GoPXsSTO_r4DQnV6C3uU6H_Ej8zCmvvIhTfGw9qfhM_J6GtFUTz5ab00Vj2ywtgOepdzpYEsBz7VTb0LFeMqxscE5u2AUJRGTqYjsVIT986F99eS4sSQ3rzOEUPgCDLajy_vfodrMYXP4FmajPDjL8MWR1YXIoNWPnYAAZp5cZHRlgjN9Nm5HKy4gCfsPsmdWOAYHrNa9EtjkW2XusoOKrB8_4OxChhHVbVcBRzPxr9-m9c9wljgbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار فاکس‌نیوز:
فکر می‌کنید این جنگ با ایران را از طریق
جنگ اقتصادی
که وزارت خزانه‌داری به راه انداخته پیروز می‌شویم یا از طریق حملات نظامی؟
ترامپ:
فکر می‌کنم
هر دو
. از هر دو طریق پیروز خواهیم شد. از نظر نظامی، واقعاً
تا حد زیادی پیروز شده‌ایم
، اما این به این معنا نیست که حملات را متوقف کرده‌ایم.
ما قطعاً
با اختلاف زیادی در حال پیروز شدن هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24364" target="_blank">📅 00:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852e1be8f8.mp4?token=MNewnfIvaw4L9VJYX65rR3UAGqC0JK8L4aBAkQtp3uuzAn4vDQQz7rYX04ipXdmeSgt_SkiNtZKYLV2IoCrsA9pRjGE4MxwenHqogthY02Qy9yWGrDsMRmAgpEBR2qa9edYcxVdEPwZ0bm0WRn6SPNzbRGLPwiU7CXqaPoOWslw4lA2Gtlf-AgB8jpVIxN0wlefj5GZISz-ZKYbYJJjEpWHfQ4YfS7IV_grJ0OXrlzxzWEvP9Tv27rro0cbOOWs0OIgmC5CLLiat3Dz3q0BOevPMET2oarxsI-QyFmFaFkGntCrtshcVJcsqPCpfUXwLUJFy4GPSBwCV0N98UAlX-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852e1be8f8.mp4?token=MNewnfIvaw4L9VJYX65rR3UAGqC0JK8L4aBAkQtp3uuzAn4vDQQz7rYX04ipXdmeSgt_SkiNtZKYLV2IoCrsA9pRjGE4MxwenHqogthY02Qy9yWGrDsMRmAgpEBR2qa9edYcxVdEPwZ0bm0WRn6SPNzbRGLPwiU7CXqaPoOWslw4lA2Gtlf-AgB8jpVIxN0wlefj5GZISz-ZKYbYJJjEpWHfQ4YfS7IV_grJ0OXrlzxzWEvP9Tv27rro0cbOOWs0OIgmC5CLLiat3Dz3q0BOevPMET2oarxsI-QyFmFaFkGntCrtshcVJcsqPCpfUXwLUJFy4GPSBwCV0N98UAlX-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«فکر می‌کنم اتفاقی که خواهد افتاد این است که
خیلی زود در این جنگ پیروز خواهیم شد
و به‌محض اینکه پیروز شویم، قیمت نفت
به‌شدت کاهش پیدا می‌کند
و به سطحی که پیش از جنگ داشت، برمی‌گردد.
و نکته کلیدی این است که
ایران سلاح هسته‌ای نخواهد داشت.
این، کلید حل این مسئله است.»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24363" target="_blank">📅 00:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">معاون پزشکیان: برای عبور از زمستان به همراهی مردم نیاز داریم.
@WarRoom
Yashar : Winter is coming</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24362" target="_blank">📅 23:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الجزیره : تنش در تنگه هرمز پس از رد پیشنهاد ایران ادامه دارد.
الجزیره گزارش داده پس از رد طرح تهران، نگرانی‌ها درباره ازسرگیری درگیری مستقیم افزایش یافته است. همچنین
گزارش‌هایی از انفجار در
محدوده
تنگه هرمز
خبر میدهد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24361" target="_blank">📅 23:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">صدای انفجار در تنگه  @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24360" target="_blank">📅 23:10 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
