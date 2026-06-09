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
<img src="https://cdn4.telesco.pe/file/WaIisjjQRvtJP1DajXDstszTfTRPLKR4X8fQf9fJ5EnPMvBY97-C01z0C0_7slXrTk5fAmPmlzff651eV_Rqikq0CPN4umyDoRlxKU0mujeJrTN16nisPHESGFUIWArJzqtoMhDaUpvL8iIxxxmIcIVjwj6jKDHsBHgug0rD8-C90saEmHAEVoRNVrLrlhRISXPwoxR6CcnujSdQcGf6sMkNcZSJdqXm-fGCHB2VMANqHb8wdnlXg6MLJXGSiuZdtoMoA1T3jf20-4SFa7rj9LGKXH4Py9A-os4xiJPr92bSm2izwv4l6-u-jcYj8z2ue8JJjNBwDXnJxEF5v0-Eyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.42M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 21:58:03</div>
<hr>

<div class="tg-post" id="msg-657742">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cX5nH2ugsNvFqTlYZP43ExtuFrW7NI7d286FFuUeMsImPaEKhaIgX5NQudUTPbh36tr8Qxan0eKySwxEUbKQN0i-zBMXuWjRtW_kyJPZbX6Et2z0tc5zP6JLMfv05M3UZ9aWO4DIJcGGce03fnbtC_cnd2Hhy4S2i35KlY9DZ2G0Tc-Jh3qiYuEHtXaZJztB2M0-6kVirS__DIXP-9IKDXAFGwo5OJvHGNEmzW4Ak4Pcn3tWvZpV2G_RFEkBOjM0xgEUrRaHtYfpFZaoUc5ioS7trkHb_BkcZL2zIYAs0IJ9EWyQpQd27zmzEv-UtWW0G4uDQ-fROolrGrAWERvx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWPUAJGKxRDP6xPCnIsEGh6ll_Di09tR48rchri-3gn1pIpN-OjMxXzsC70DUwcXjMq1U5nQ5zkKHqaP-xON3pOqiaJibnC0u0YCACOlhTMiJtUQBCbmWUJ2WVYwwvwYhtid9TynHcj5ICGFm3ZLwt7yL8Zy50GVLtdyFt4Wuo_M2cBMBUNliYtQFYnk1pEWJgQs4sLlLifip-X6i4RkcXOfUjvHLHuwy6f2hmkK-aQv23_0soy6AgypxbRDEEx_eW0dklL8XYsNqtSwfG9oer5GoeNlRHtrfcTMLMTEmk5seP_kU9o1tXlZYlxUc6t2wTERxkb7uhrmB-uXBxWbcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هشدار عراقچی نسبت به هرگونه خطای احتمالی دشمن در خلیج فارس، دیپلماسی را ترجیح می دهیم اما سخن گفتن به زبان های دیگر را نیز می دانیم
وزیر امور خارجه:
🔹
تنگه هرمز در آب‌های بین‌المللی قرار ندارد، بلکه میان ایران و عمان مشترک است و هزاران مایل از سواحل ایالات متحده فاصله دارد. مرزهای دریایی کاملاً روشن و بدون ابهام هستند.
🔹
نیروهای مسلح قدرتمند ما به‌طور مستمر در حالت آماده‌باش قرار دارند تا با هرگونه نقض حریم هوایی، زمینی یا دریایی ایران مقابله کنند.
🔹
نیروهای خارجی که در نزدیکی قلمرو ما قرار دارند، همواره در معرض خطر هستند؛ چه به‌سبب خطاهای انسانی خود، چه حوادث ساده، و چه احتمال گرفتار شدن در تبادل آتش.
🔹
برای کاهش این خطرات، بهترین راه آن است که نیروهای خارجی هرچه سریع‌تر این منطقه را ترک کنند؛ منطقه‌ای که هرگز پذیرای حضور دشمنان نخواهد بود.
🔹
ایران زبان دیپلماسی را ترجیح می‌دهد؛ با این حال، همان‌گونه که رزمندگان شجاع ما به جهانیان نشان داده‌اند، ما به زبان‌های دیگر نیز سخن گفتن را به‌خوبی می‌دانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/akhbarefori/657742" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657741">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از یک مقام آمریکایی: تحقیقات مشخص کرده است یک پهپاد ایرانی به بالگرد ما اصابت کرده و باعث سقوط آن شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/akhbarefori/657741" target="_blank">📅 21:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867a5b5908.mp4?token=GY4aG_avKTh6aT5TngCaN-sEqsU4m4ktJEH7JHPlfqxUI8TzPeYz9sxxOZr7EAMcdY427Y5SMYCYU3QyKMYUoSLNe8MHzuk8SwzL9EcTjfj-D6SVN9s50iT7q69k-ePEM0V78wGZtCPgEEAo7HbOnOMIz6AlaqNwv-Od0qiD_WZ3xbAUStxgUu6iA2VEedp0aflTzTOsq3KJpwt_hzCeDxbg6IrOkO4s7T97gl2FF8Zlq9tGZpYRX6lQrjw-ki3qMOFn0HxEXyBtO6zzYTk0Dc5oGkyXLYIgph02gyJ163RAigeM8aPRxQO8QGoITKS62IFbD-8HZniokj9Bb5aWnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867a5b5908.mp4?token=GY4aG_avKTh6aT5TngCaN-sEqsU4m4ktJEH7JHPlfqxUI8TzPeYz9sxxOZr7EAMcdY427Y5SMYCYU3QyKMYUoSLNe8MHzuk8SwzL9EcTjfj-D6SVN9s50iT7q69k-ePEM0V78wGZtCPgEEAo7HbOnOMIz6AlaqNwv-Od0qiD_WZ3xbAUStxgUu6iA2VEedp0aflTzTOsq3KJpwt_hzCeDxbg6IrOkO4s7T97gl2FF8Zlq9tGZpYRX6lQrjw-ki3qMOFn0HxEXyBtO6zzYTk0Dc5oGkyXLYIgph02gyJ163RAigeM8aPRxQO8QGoITKS62IFbD-8HZniokj9Bb5aWnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراسم وداع و تشییع رهبر شهید انقلاب پس از دهه اول محرم برگزار می‌شود    ستاد بزرگداشت عروج رهبر شهید انقلاب:
🔹
زمان و جزئیات منتشرشده درباره مراسم وداع، تشییع و تدفین رهبر شهید انقلاب و شهدای خانواده ایشان در فضای رسانه‌ای معتبر نیست.
🔹
با توجه به ایام…</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/akhbarefori/657740" target="_blank">📅 21:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657739">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
چگونگی ترمیم نمره سوابق تحصیلی اعلام شد
‌
دبیرکل شورای عالی آموزش و پرورش:
🔹
از سال تحصیلی ۱۴۰۵ - ۱۴۰۴ ترمیم نمره برای اولین مرتبه به صورت تک درس و یا تمامی دروس مجاز است.
🔹
متقاضیان ترمیم مجدد نمرات دروس آزمون نهایی به شرط انتخاب تمامی دروس نهایی پایه مورد نظر می‌توانند بدون محدودیت دفعات نسبت به ترمیم نمرات آن پایه اقدام کنند.
🔹
نمرات اخذ شده در این آزمون ملاک محاسبه نمره کل سابقه تحصیلی خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/657739" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657738">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf8g5kdJ85a0AzNLgtdM-nUiyINq-KGYBbamjAphDCsOLiLZidciLcAITe9aBiOxWBXZl9jwec_MP_VpEKuu7aMCHfL7Ts6Hpia6TUhq8IsLCC9WsaTD5srDAo_Ym6MdngTEFTbceqMwCbW-JYvUycyt9O99Gd_f9P_UgY2boiivdYPs7RkRFll2dgw83NI1TtRlmu7SHaiNIfz3SXcS_mctJ7zotcojiv-qcTvM1WhXakrAM6XZAOoG6mUPAmJeQM8g6TUqErtNczvrGdgxk6ksVOK3keGo1Sa-RJBad33wYHXV3wuQlTzMEW0aCndVcm5TJR3eA_I5Ke_atNZvrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام تقدیر و تشکر دکتر محمد مخبر مشاور و دستیار مقام معظم رهبری از ملت ایران به مناسبت بیش از ۱۰۰ شب ایستادگی تاریخی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/657738" target="_blank">📅 21:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awUaRLR_QzhJpwB1vyjOi_fOP5qjbDlaJQDSt3VMQoc4h8DHZruNYxn8mB6VQ6Opfta1R58REVJWz0EBCL9sdAD4PerlF9PwluY809DOoPNmIKMIGOC9JvGTePxJq9ZfsGTYY7rnHJouoXRK4ict6DR1ptHFgkVfiMMlz6Aq1FZO9qiXrqMBSM23FlowgJed_A6kRwS8FnJLX1V0FYAvXU304Y_8AEB0goTF6TPZ7y3a6x0Xd4evPmb738duZlxMceDlzYxBYaqQ_C5BtVPxXtBMEEYHA11v-7H6AEr84lzHSPydQ_kHgSx80TaYs6QoNfPSiTX0YEVicARU2RZYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هند از استارلینک به خاطر جنگ ایران ترسید
ایندیاتودی:
🔹
طبق گزارش‌ها، ورود استارلینک به هند با مانع مواجه شده است و سازمان‌های امنیتی به دلیل نگرانی‌های مرتبط با عملیات جهانی آن و استفاده گزارش‌ شده از پایانه‌های آن در طول جنگ ایران، مجوز نهایی را به حالت تعلیق درآورده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/657737" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657736">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
کنسرسیوم رویه‌های استثنائات تجاری ایران: ممنوعیت واردات لوازم خانگی تورمی و قاچاق‌زا است
🔹
کنسرسیوم رویه‌های استثنائات تجاری ایران نسبت به مصوبه محدودکننده واردات یخچال، ماشین لباس‌شویی و ظرف‌شویی از مسیر رویه‌های استثنائات تجاری هشدار داد و آن را فاقد بررسی کارشناسی اقتصادی و اجتماعی کافی دانست.
🔹
به گفته این کنسرسیوم، انسداد این مسیر واردات نه تنها به افزایش فشار تورمی دامن زده، بلکه توان پاسخگویی به تقاضای بازار را مختل کرده و زمینه را برای گسترش قاچاق کالا فراهم آورده است. همچنین این تصمیم بدون بازنگری، باعث اختلال در ساختار رقابتی بازار، افزایش قیمت تمام‌شده کالا و آسیب به زنجیره تأمین و مصرف‌کنندگان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/657736" target="_blank">📅 21:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657735">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای رسانه غربی: هواپیمای اماراتی دیروز ۳ میلیارد دلار پول برای ایران برد تا از جنگ جلوگیری کند ‌
🔹
رسانه اینتل‌واچ مدعی شده هواپیمایی که روز گذشته از ابوظبی به تهران آمد، حامل ۳ میلیارد دلار پول بوده که از امارات به تهران داده شده تا اعتماد ایران را جلب…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/657735" target="_blank">📅 21:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657734">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شرکت کشتیرانی سی‌ام‌ای سی‌جی‌ام: هزینه دور زدن تنگه هرمز در سال ۲۰۲۶ به ۳۰۰ میلیون دلار رسیده است
🔹
چین صادرات کالاهای دو منظوره به ژاپن را ممنوع کرد
‌
🔹
وزیر انرژی دولت تروریستی آمریکا: بازگشت جریان انرژی به حالت عادی ماه‌ها طول خواهد کشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/657734" target="_blank">📅 21:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657733">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
هواپیمای اماراتی در مهر‌آباد فرود آمد
🔹
داده‌های ناوبری پروازها، تردد یک فروند هواپیما از مبدا امارات به مقصد تهران را در آسمان ایران رصد کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/657733" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657728">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PxDt86o4RQ2cCZEEMQewggENMogwmvpdWqBKohRN8p6Bu1A8N0Cs4PEDJPKt55b0_lzub1ewvRJiUK1n18a5FzbF09ujI9gLSTIeNlQbaAwWTC30CCT1guAGbiVK6E5DqSQw685YGEMb5nWxLds8MsWOt81gXJ74h59xk8gBimjqDcacZwilfRh_hlMKFa76zJfRd41P9gRFO_ohK8vjg1PIY1j8oG2JL4x1cfHiHyPBiBleIgYRi-ssp_t55P_h6EpeFjnHQLIkDjDmk_SaqlSRxCgxSLz9Gtf-foxPJ1yn6lyHyvBlMacuXibuc_7y40Y3ii6xxN25hn8iBVTVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugBxcrFMmiVVSqinZCNvUgPPBQ-3zYaeCuwVcec3RwdsZ_5ydO5XHDwBNSiCAtQpJNz7kIdl_OZfnZqhFwkF0lZjqVjpSpt3YXkLNkv-HYsNv0TbTw54XCC8Bx6xGFRJfWWaJlGoYU2IM9aYU24B9vQVsRbdATKVcziwgKtkFpCwLrJnmSx_7_yhgPcu6ds0djfO3JrT1JS_KDTlZX_2lQ4ETvKY_UnOcHaGe67YJEjs68gGFgvEeoLFwuuS2cYDcJGSkEBygXeju8Tohn4PjkySTGp5aaqWGwNx7RJGUXePNLXun8oQiX-VwtlY5miqrg5srGxVD10AAk4lFS1T9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzR6YYWuFde11K-GBznRuJCeypsMt76ZL5sduuMFmF83pfEKtYAuL1xUstKMULoqlG6FdXKpvIzNu0H688-RTr1PGzV2w8DZFnYGMweWU1jk7Dg3X8KZ1AXCEvyEJsBvCq4QmxJS2_oZWFvnQkgN52VDdXTC9EpICsg0U4shKdjOjVs6iC3y-6BH9GuZru-Eolq_63RmiN4M_Hcbke2W0lnokt-94h5fO_9Ob4WAzPnTt9a4kSikF8qZr3LkjtYKodDC-kxt5IWrakImboASOP92q4XvcazJvGubRBQrYABjdMMuQKWGIrnPVt5JQnslD0_3_jGM-fKR5gdDwtNaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGWTdGeFyO3EOGZzU72--x_Xo8srStPAwZkYUBeIUGhSZIxT9LGebQA4YOjp37ca2chG5jZoZC9P28QORXp1YKvXAfLt0W-VHKMSUkQUcbMct8FSP7reb1r44USvdm685riG0DlsNpywBWQRC137wiDK-StlhqyeRpRBcCq5bU0nGIzm_WXg788uzfet_xYRPLj7SDsAtsjcM1cdHsfDg7awsrxCloq3Bd97NrHn3aj9D9s8lfKQAwO2XkL8wC-TL5uIMjwEcu6zMq9uZ5bH3Recr5j5UbvKj38-CV6OqVNkP8SFdF1ml3MRr_kBM9MiRp2PtwfqRnbm9Gm6gegbwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ss1zQhQXJDhl8-WgJZwmVEZm9HHHs-3WEjJ6Gy54-kH3gyxti-i9ROsXhYPY8xuVeipJvNL_KvfLNHaOlXlk3_2iNG2TsKY-x9I6lEbuHKXRaaenSaf0hYW52B-CAzkwiJi99v-fgME59zdVMgtkTI9YV_IcGA4NEdLq0L1H9srXozBqPRJ-KppdyN7X-pLVK27B5MEIuYqRLXxgLFFYaihFOleQpR_PHB3Qv1Qi2CYjH63gCl6N7AbGORj-D5JjKEctVX80UJiT8hXqntO2RoIRCRxZt0cNIt7BJ6UjoboAf85MpPAuIamkdd5p9bh_1W9usOwj1NQ4YwlfrqJxIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی درگیری دوباره با ایران را چگونه تفسیر کردند؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/657728" target="_blank">📅 20:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657727">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
هلند سفارت خود را در تهران باز کرد
🔹
سفارت هلند در ایران در پستی در X اعلام کرد که فعالیت‌های خود را از سر گرفته است. به گزارش apa، سفارت پادشاهی هلند در ایران که موقتاً از آذربایجان فعالیت می‌کرد، از ۷ ژوئن ۲۰۲۶ فعالیت خود را در تهران از سر گرفت./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/657727" target="_blank">📅 20:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657725">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ایران هلیکوپتر آمریکایی را سرنگون کرده است ‌ ترامپ:
🔹
ارتش بزرگ ما به من اطلاع داده است که دیشب ایرانی‌ها یکی از هلیکوپترهای آپاچی بسیار پیشرفته ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند.
🔹
دو خلبان در این حادثه دخیل بودند که…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/657725" target="_blank">📅 20:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657724">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7xjjWlfhVRYsNOU1SsZBv23dMW7hcajNSljddtfOhofFSWdtxA6KvBtq4NF1jnmoTpmy-HqGvryccLsIg_P3-JzlZoRoWEEOSV539lPZVKVUc8xjRiiKYkPbd0wgD7eMGmLsUfbaOLM_5zej9WHruqj-9nKsmJxi120Id4Z986ALDr31onOc23z8vZEdbqX9wpCGD163kY-rOQDMr9A0HFIimhV1iSM2KI6VlDkmpfUZsOOo1VY7_tHvdQ0V_K170Him4pGcK9sRJQpVa23UyBtcJkl5c-DAi0No7oI_WTjy-mA5xKyyG6wB0qq9eTZ5kj0DhQ4WW23m-bZ4akCRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: یک عملیات پرچم دروغین، مبنایی برای یک معامله سودآور شد
‌
🔹
تکه‌های جورچین خیلی سریع، در جای خود قرار گرفت!
🔹
ابتدا طی یک عملیات پرچم دروغین، با استفاده از پهپاد کپی‌شده «لوکاس» به فرودگاه کویت حمله کردند و سپس از آن بهانه‌ای ساختند برای اینکه پدافند دفاع هوایی ضدپهپاد شرکت «پاوروس» را برای دفاع در برابر حملات ادعایی ایران، بفروشند!
‌
🔹
عجب معامله سودآوری!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/657724" target="_blank">📅 20:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657722">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
از غرق شدن در زاینده‌رود تا منع از خوردن سیب از درخت
🔹
00:05:00 اتفاق شنیدنی لحظه غرق شدن در زاینده‌رود
🔹
00:09:20  آگاهی روح قبل از حادثه  همراهی نکردن جسم در آن اتفاق
🔹
00:27:50 باز شدن راهی با نور سبز رنگ زیبا در زیر آب
🔹
00:33:10 بازداشتن من از برداشتن و خوردن سیب از درخت
🔹
00:49:10  روئیت جاماندن شیشه در قسمتی از سر حین عمل جراحی توسط روح
🔹
00:51:40 تغییرات رفتاری تجربه‌گر بعد از تجربه
🔹
قسمت دهم (در ، گذشت)، فصل چهارم
🔹
#تجربه‌گر
: زینب حیدریان
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/657722" target="_blank">📅 20:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657720">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMb9Z0X7RgGx9rIC_wQ3k927jpc5T0vlNfcbl0-yexmKNLk_Vd8WTqFZNp_FHvhGxwLdxA4-o6n23aU5nuOZ5CnRLGyAQIxiXJwHnXgEoCkSIbXrD5mi06uBO8HSCgbqVIGQ5_Cxj3p7sf1SzH0gS5F5wJOKvsIgYPL2WnLZ-nCCQ4WgVX2CHJM3tknEJTCuiDR2r8GGFW3ukbxHfAy8vzDlK9Vr7J4VgrIjb7HsPgZw80qKOPlp3ex8ZKBlUqFqXyHm78JEiDHUklR2Nuavw3kljJVFpgxsS561SpLbKHNcnEYJIySGjVdB-0hJuH3pxizZrjSg2p4Vh6A32EuaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mt9O5HX93td6-mpLMwbbyR8IgcP9Eeicd8ywsLA_V7YeoDfbKKyZztSZwmX1Z50P2wgxTONCT0B0PC4FVG5XvKNqfSLpj51hUngC_DCE8aGBU1go5LKrQZ72xlcmO5i5oYjLB4p5Raq0kCA0vW2PaeqDP8bb44WFGJ7JtvKgCrCBTI6ru8vnJbJ7f52UrtYFmPPlDuBm9jk93eOwFa3QBA2XUPcB3oCj_kQgoq_BzLBnGOytT4FXXTfsY0MZOkBPoK7XrgTxZBZXFOfiKJu6VMTsNgsrk_FpsVzfDWNCY1xuT1Hdc0dREdbVQfw2fn4ZjyugaVqoysMKP5doP1GRxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: من و کتاب
🖋
نویسنده: سید علی خامنه‌ای (ره)
🔹
کتاب «من و کتاب» اثری الهام‌بخش از سخنان مقتدرترین رهبر جهان درباره نقش کتاب در رشد فکری و معنوی انسان است که نشان می‌دهد مطالعه چگونه زندگی، اندیشه و نگاه انسان به جهان را دگرگون می‌کند.
🔹
این کتاب مناسب…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/657720" target="_blank">📅 20:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657719">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gILrrsb0p0CsgYpF3rOZFglgm72-wevvljmmDjAmEX8V8Wx_Nw47qLTa04cbqQyWGr026HK5lkrnkBe6B578QlhAEJ22SZbCFgx6-wys3wjSbMxHXe9K8UijBGx88mIB8GyovVw23KxmaG5HLCm7Nc2_xLfvYZMDk_SLs7ouIzeTdjlpqoFyh0uQBaySmHZ6y28Q37agm3ZabgiJ5ZTks582ANcb_qyJxyhI97KM71JQeSpZNorpQCVIg_TBHLVUv7r6x96KNvGOV1vd18M_JXCTas0a8V5i_9WhK0p9dw8NZFGVJaTkcaACw9cGEPuF1tUXGLsYJIGWRE6q6A-mCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا سقوط هلیکوپتر خود‌را در تنگه هرمز تایید کرد  سنتکام:
🔹
ما دو خدمه یک بالگرد آپاچی را پس از سقوط آن در نزدیکی سواحل عمان در حین گشت‌زنی نجات دادیم./ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/657719" target="_blank">📅 20:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657718">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتاپ تورز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlglKg3mWGRaJ5uWcHDewghO4qs5ZDXNN1UBn-OlAWS-NpcsX3YP4C7shLybEEy3xt1JNfwiOsaN9u8_DpAy-hc0v6Rm_0uwX9eMIl70VCvqvOSxK1YZ6M_y5daUsMgtQ4VhiNWpOBJWKAu5rLaq8G1wm5icigOxV0T7-a3L86HFatDjulQcKQ7kWSG38tmHQi0tLg5aclG0t6ZeVoDKKgNM0PXX7YdkS5AtXciBN6sO0rVM0kTWuhp577rFwUYHy8GeVAmyet7LRAo3ULLRRWlvKuMbLXqM8pqAmPvQEt_IfdpmWgut14symtjs7vZHPP9KNehWhi_hDao6UiIpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آغاز فروش پروازهای هواپیمایی سروش
📍
در مسیر تهران - مشهد - تهران
✈️
ایرباس پهن پیکر 310
💺
صندلی بیزینس
🛫
پروازهای منظم روزانه
🥙
بهترین کترینگ
⏳
بهترین ساعت پروازی
خرید آنلاین از :
www.Booking.ir
📞
+98 21 8586</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/657718" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657714">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIe3JtUuics7s-njk5Wd3SOIU-HqfUvLNHs72n_aZyp4wZo9XVcSYS3QFTBRE_g1XfM56i4BYvF2AyRdvdXGJdtjaaUyPTOSsJ5dDOOQJS_nCcrQQB_cWJ3oxSmiN53cj9acMAdigkDJ7parxRm0T17I5dww0JKnXOuPlRsaUJMAkyw3YCADbs7suHxOolqyzyYTKtg-jT4ta41ZgLz4Aqs8rYZT8zvYfro6MagDpNNj8-sDVFzsxSa0z4xzr5eKrhrtHwgqmW0Q44oX59vryYDLu_fVXUpjk1mfYmJAavoCaM7-q6V1b0vTMNIe2uwOhZD1p9qUedD8hPv33xCoNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iE7uchrcRyeFQ5xgUqAtJmXQWe6zVd4q7xYJvf3frGnpvxTGDu44I31Pc7x21QwQYgTeu0eaTz_AQYyIFy5IKJ9T4R_DCFUWrVo6OVxY3zUQK3o_nMbrMRO88hHkeAnEAGyTTgWhqX4RJZUUVg4aaaivqJjHVj5Xg1gCVx0EgQyGAnmJE_au3kuK4oCDECij2E9wgg855p46ycoyn4C8sWG_nfHdlk1klXR1d0ag8C-jhmZhJ4nioUlVhlB2sp4D2YxR1yLQ37zsixcRaLEFAAUkEkH6bOTH6Y0lsoaDJ9IrZXnvTVV2TGgTCzuM5bf2RCDVjEzjFNVCRJIMH9OWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wo5_H8GY5m1RM-jWFMFoV2Xd8dDnORoIaC3eyXee0gXKnWJl61mPOydOB8ZqE1YSD9DUleMGEw9ZQdL_ynKWm31YDVwWjihByXYE5ing1aOkcnF7Gtsph67UxdNMrDoBZz__U3D5I0QnP0tc810kOwkgUVkXyDb_5vvT3UvcSvDDO6CsE3zO-QsOccORGGqT2-vGGNf8wFLh0Q6W7EwdIlwRpcLPpHk4BWcW5EbC-AyBgDxMaRyZftKJ9SZIUdV6MWQBxrSAM8Sfw4yytKuDVPOtnQszUCUejtgaGxDQegNidAkzTW0z_3wRySsEl1_bC97kGs1ZZNqQUA0tRCk1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QI6yqOblkw1biYaVyIfQcOa7DO-P8Eh4cOERLy9MQF0ac0eriClmkcrIWGqQaRURJH-hu48-XWfr5XmkOA6nPpDy4_88xiQu81ALkwd8VWVRnbvgtoZWtmn8Y49fg6-bWUEh5eb_ojBRiTvzOI_Amn58DzvwOpB4Ym2yDFH2jjQGDLf1LyD7wnrWIGR0pyTpSnyzs8VMbgIe6zU7ziAB30CWiTY3Wz7Mo34Y7IQadLypHKHo3K6oy_TqPvK4F0uY2SATMm_7yVYs-iWjLkfMRt2u5dl_yAalquNDlheDLtMJEWOkQpK6oZXL2XYvIrx4-J2El4w-uFW7e9hAxG0JdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
اعمال روز مباهله
▫️
روز بیست وچهارم ذی الحجه بنابر مشهور روزی است که مباهله حضرت رسول با مسیحیان نجران در آن اتفاق افتاده است و نیز در این روز بود که حضرت امیرالمؤمنین (ع) در حال رکوع انگشتر خود را به سائل داد و آیه «انما ولیّکم الله» در شأن ايشان نازل شد.
▫️
در این روز چند عمل وارد شده است:
غسل
روزه
دو رکعت نماز و آن مثل روز عید غدیر است - (دو رکعت است در هر رکعت، یک مرتبه سوره حمد و ده مرتبه سوره توحید، ده مرتبه آیة الکرسی و ده مرتبه سوره قدر خوانده می شود و بهتر است پیش از اذان ظهر خوانده شود)
خواندن دعای مباهله
صدقه دادن به فقرا
زیارت حضرت امیرالمومنین علیه السلام
خواندن زیارت جامعه کبیره
#مباهله
@Heyate_gharar</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/657714" target="_blank">📅 20:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657712">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
بحران تنگه هرمز برای دنیا خطرناک‌تر است یا جنگ اوکراین؟
🔹
در حالی که جنگ روسیه و اوکراین عرضه غلات و کود را مختل کرد، افزایش قیمت محصولات کشاورزی بخشی از فشار هزینه‌ها را جبران کرد. اما بحران تنگه هرمز تهدیدی جدی برای بازار جهانی کود است؛ زیرا کشورهای خلیج فارس از صادرکنندگان اصلی اوره، آمونیاک و فسفات هستند.
🔹
تداوم این بحران می‌تواند با افزایش هزینه نهاده‌های کشاورزی و کاهش تولید، ریسک ناامنی غذایی جهان را افزایش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/657712" target="_blank">📅 20:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657711">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
آمریکا: انتظار نداریم ترافیک تنگه هرمز تا اوایل سال ۲۰۲۷ به سطح قبل از جنگ بازگردد
اداره اطلاعات انرژی آمریکا:
🔹
انتظار داریم بخشی از تولید نفت در خاورمیانه تا پایان سال ۲۰۲۷ همچنان مختل باقی بماند.
🔹
انتظار نداریم ترافیک تنگه هرمز تا اوایل سال ۲۰۲۷ به سطح قبل از جنگ بازگردد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/657711" target="_blank">📅 19:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657710">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688a2b1e8b.mp4?token=VQV4oxLvfIEMoMOEU0Y_9njyzmDdCUnqt_2U1dyBPz6ZW92cPvtp6-XygFX5WN5tlWT6Ge2o0YouY3aNQpZH-pBZ4D8636TJWMlgpHhAEPuxtREQWlwAOmcZXzgrlCsLmh1NC9d13PEu-PT4_VacxDu8C1QZFR43FnhgF4NO26zRHb6s0VOu3rMDPiUkjgTAq5rH9zQ_Mhf7r_QIok85Q4YcBttTre1FAxpb3MDL5yXMZV_Xpr9Mur1rbounzIMapkBWWyptdfsG0_mrkwAr1ZehkqRa12eYUk3CId3KdtJahXAbxaFJaTd2uvSUjgqjDihYMHl8OPQUssAXTfO3MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688a2b1e8b.mp4?token=VQV4oxLvfIEMoMOEU0Y_9njyzmDdCUnqt_2U1dyBPz6ZW92cPvtp6-XygFX5WN5tlWT6Ge2o0YouY3aNQpZH-pBZ4D8636TJWMlgpHhAEPuxtREQWlwAOmcZXzgrlCsLmh1NC9d13PEu-PT4_VacxDu8C1QZFR43FnhgF4NO26zRHb6s0VOu3rMDPiUkjgTAq5rH9zQ_Mhf7r_QIok85Q4YcBttTre1FAxpb3MDL5yXMZV_Xpr9Mur1rbounzIMapkBWWyptdfsG0_mrkwAr1ZehkqRa12eYUk3CId3KdtJahXAbxaFJaTd2uvSUjgqjDihYMHl8OPQUssAXTfO3MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💡
ایران روشن می‌ماند با همراهی شما
💡
✨
با مصرف بهینه برق آینده‌ای روشن برای ایران بسازیم...
🇮🇷
همه ایران
برای قرار همدلی ...
۲۵ درجه؛ قرار همدلی ماست
#تهران_روشن
🆔
@tehran_roshan
✅
https://ba25.ir/</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/657710" target="_blank">📅 19:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657708">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
چین از دل دریا اورانیوم استخراج کرد
‌
🔹
چین اعلام کرد با دستیابی به فناوری استخراج اورانیوم از آب دریا، موفق شده چندین کیلوگرم اورانیوم را از محیط‌های واقعی دریایی استخراج کند؛ دستاوردی که می‌تواند مسیر تجاری‌سازی این فناوری را هموار کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/657708" target="_blank">📅 19:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657707">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: آمریکا نباشد؛ اسرائیل را به توبره خواهیم کشید
احمد عجم، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
اگر ادعای آمریکا واقعاً درست است که از اقدامات اسرائیل حمایت نکرده و این اتفاقات با نظر آن‌ها نبوده، کافی است یک هفته دخالت نکند، آن‌وقت ایران، خاک آن‌ها را به توبره خواهد کشید.
🔹
تا زمانی که رژیم سلطه‌جو و قلدر آمریکا پشت آن‌ها ایستاده است، ممکن است شرایط را دشوارتر کند، اما نیروهای نظامی و مردم عزیز و مقاوم ما پای کار ایران هستند. ما پاسخ آن‌ها را محکم داده‌ایم و از این پس نیز محکم‌تر پاسخ خواهیم داد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/657707" target="_blank">📅 19:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIsQiR2ksgFJdAcV9v3WI1Cg3dAuuqiZrDY9-IA3LCyd4ul-N9eb9MUsORvB02nWBlZrw42z9MB0h1vPG8rttOirYdT1GelJDbKr_a6Q7K2X1JqTlDVvVGBQk_VeZVW12N4mq8AnL_MS-8QstdqpG1d-n5dQYXz_DhH4iEO4WeFrbYyhRQt2qatv5m4TW8XMBH97b6eQ1T1R68GHMwx2qBnvyQXb4c2lwukqjqGtjhDklMKom2SYcmOZAMRNCwUIXBinaoEkr-s_cq2xpicvhgm_9flxsyi3lKhuS8x2u5vD_KFJGjIY2CWXNryz-KvWpsYG2IT_M4S3DOFUHeGxEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانگین سال‌های انتظار برای خرید خانه در دولت‌های مختلف
🔹
بررسی‌های تاریخی از تورم مسکن در ایران نشان می‌دهد که انتظار برای خرید خانه، تحت تأثیر سه عامل کلیدی نرخ تورم، بیماری هلندی و تسهیلات بانکی نوسانات شدیدی داشته است.
🔹
در دولت خاتمی این شاخص زیر ۱۰ سال، در دولت احمدی‌نژاد با میانگین ۱۴ سال (تحت تأثیر درآمدهای نفتی و بیماری هلندی) و در دولت اول روحانی به دلیل افزایش نسبت وام به قیمت، کمتر از ۱۱ سال ثبت شده است.
🔹
اما اوج بحران در سال ۱۳۹۹ رقم خورد؛ جایی که مسکن به پناهگاه اصلی سرمایه در برابر تورم تبدیل شد و میانگین سن انتظار برای خرید خانه به ۲۲ سال رسید. پس از آن، این عدد تا حدود ۱۶ سال کاهش یافت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/657706" target="_blank">📅 19:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tivbwaB6VPHMnpKH6xC1_yMJsrm_B97Oh4a3OtwRPIr7svMjgapeW8dcr8jaSWaYZcufvWH2SkAR0YtYWaBBjA-V0ANzSDDFEYZOj8anZRYT4YZ2HZILxo_vT-ZgJxnF8Lm2xzO3F1CaNP6HGyf_dRkPIMZZ7BtvTxVXAIAJC3NKD1d7wjOi4EY4CQrLa74Zb7HWj3Isw1IhgywMdkcA61jGqp7KKnAr8PDYuY2nCDrYKC1_fLlNMANx04NmuzfXaHHyPtVv_TgIRMWpM0bRWKEkzPyrYZ2CKiIGABNC_vxcZOEGw9Y7YRnjkIm9mJq-EWOGXu7O_MHSA7mMRGqjGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکوربورد رسمی پخش تلویزیونی مسابقات جام جهانی در دوره های مختلف
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/657705" target="_blank">📅 19:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
وزرای کشور عضو شانگهای چه واکنشی در قبال جنگ علیه ایران داشتند؟
🔹
در پنجمین نشست وزرای کشور عضو سازمان همکاری شانگهای، رؤسای هیئت‌ها در بیانیه پایانی، نگرانی جدی خود را در مورد تحولات خاورمیانه و حملات نظامی به خاک جمهوری اسلامی ایران، از جمله به زیرساخت‌های تحت نظارت وزارت کشور (اماکن انتظامی)، ابراز داشتند.
🔹
همچنین وزرا و رؤسای هیئت‌ها با تاکید بر لزوم حفظ حاکمیت، امنیت و تمامیت ارضی ایران، به خانواده‌های قربانیان حمله تسلیت صمیمانه گفته و اعلام همبستگی و حمایت خود را از دولت و مردم ایران ابراز داشتند.
🔹
پنجمین نشست وزرای کشور عضو سازمان همکاری شانگهای در بیشکک پایتخت قرقیزستان برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/657704" target="_blank">📅 19:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657702">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ3bAt6MGqHa99UFOmeJW7m313CSDsa1qe6liFcIlg9evB53WHzEq6p5LOTJBRCei9mFJVNdhAWhnpUoDfcneY8o5mq1YArN4F_-ACK7lhAsTlM3UZ6QYJB512Zqi48I1I1Csqso0L4PA4jxUKj_aXB3UOkM5YenxgTHHBUvGgXLIFHFHlgwcbvkzcpOumGAdbPCSFv43bVZFSfCwoLxhrsf69RVjPltM_voBSv2IoaMPel3G92_0H7HlKlrBc4Brj-yPqnlBgK5C9cEoJZOQFtm1IYV97O_Gm2lp557wuotq_GYkf5xnInCOetw380BC88tbEtmCIn5kIAOBf-juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: بند ارجاع ایران به شورای امنیت از قطعنامه آمریکا حذف شد  لارنس نورمن، خبرنگار وال‌استریت‌ژورنال:
🔹
پیش‌نویس قطعنامه آمریکا در نشست شورای حکام آژانس پس از اصلاح، به قطعنامه مشترک آمریکا و سه کشور اروپایی تبدیل شده است.
🔹
در قالب یک مصالحه،…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/657702" target="_blank">📅 19:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657701">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
برنامه حضور تیم‌ملی در آمریکا مشخص شد
سخنگوی فدراسیون فوتبال:
🔹
کاروان تیم براساس برنامه فیفا، با پرواز چارتر به آمریکا می‌رود؛ یک روز قبل بازی مقابل نیوزیلند تیم به محل می‌رود و در دو بازی بعد، دو روز قبل مسابقه در محل میزبانی حضور پیدا خواهیم کرد.
🔹
بجای بازی با گرنادا، مسئولان فدراسیون در تلاش هستند تا یک دیدار هماهنگ کنند که این بازی پشت درهای بسته برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/657701" target="_blank">📅 19:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657699">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ccda94394.mp4?token=Y70pacFVyaNfLq_3USRWJl3789fRVmFlx3mbA07aSPo3cS_rGYz3FcNcMT0ERTEncozD2jep2nE3rc0IK6peRGqGCNY1vaUrIpvwHKQPXqHLxxo6B0pp1IvbK8Fx_Dw9CWrmvicJySmEbUTsGknxm7w-KeHz2aK12IhaO16LFKZKjH4uVn7VR_BQtNd063OaFXsI74PgWh6cOQOLSJqZpk3Gnv1Jxe7-iyDoLrwoXg5pdAj_-ZUgPOeJUXR62gMe8CGMmIYmXv95OJ9XEq2RcjNzObq0-JY3uyrSfHXKBZ9Bfb9JvZdEPiwD9Gh2owI_ygb9ic9L9u1eFX9_XK6Pjb2z7Hk9XOfXGo_z9FBsmgdpzIO1GxV3v5H6ISYnbmFPrtB_SUAZHNB3VzMmbRYuPgpjiSrmmugWT--d_gHTEfA_qPYC0brjNC6yI-WVgcy0LWlK_VXd76vOodbnomAl4KC5xrZck9lLIVEBbxa3_6KGPos2xedfsLzJcpsr0-wF-OrZgf-irUaV5IwXmmadDs11G8CQwDc5RV5-rm8PD96MrkMYGpNQyRuxGOFjoJuJ2TqNvv14H3MEHKZg5nSOhgUwodTUh_kC1Iao0csK3Co8-AXKACOPY1DGGpSA1Oqqc2YToBr7B7yMzOwXcDaOcK4zRImenQJe4-jqxtQEYrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ccda94394.mp4?token=Y70pacFVyaNfLq_3USRWJl3789fRVmFlx3mbA07aSPo3cS_rGYz3FcNcMT0ERTEncozD2jep2nE3rc0IK6peRGqGCNY1vaUrIpvwHKQPXqHLxxo6B0pp1IvbK8Fx_Dw9CWrmvicJySmEbUTsGknxm7w-KeHz2aK12IhaO16LFKZKjH4uVn7VR_BQtNd063OaFXsI74PgWh6cOQOLSJqZpk3Gnv1Jxe7-iyDoLrwoXg5pdAj_-ZUgPOeJUXR62gMe8CGMmIYmXv95OJ9XEq2RcjNzObq0-JY3uyrSfHXKBZ9Bfb9JvZdEPiwD9Gh2owI_ygb9ic9L9u1eFX9_XK6Pjb2z7Hk9XOfXGo_z9FBsmgdpzIO1GxV3v5H6ISYnbmFPrtB_SUAZHNB3VzMmbRYuPgpjiSrmmugWT--d_gHTEfA_qPYC0brjNC6yI-WVgcy0LWlK_VXd76vOodbnomAl4KC5xrZck9lLIVEBbxa3_6KGPos2xedfsLzJcpsr0-wF-OrZgf-irUaV5IwXmmadDs11G8CQwDc5RV5-rm8PD96MrkMYGpNQyRuxGOFjoJuJ2TqNvv14H3MEHKZg5nSOhgUwodTUh_kC1Iao0csK3Co8-AXKACOPY1DGGpSA1Oqqc2YToBr7B7yMzOwXcDaOcK4zRImenQJe4-jqxtQEYrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندی جذاب و کاربردی برای پیدا کردن گوشی‌های دزدیده شده!
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/657699" target="_blank">📅 18:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657698">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تاثیر معدل دوره یازدهم در کنکور مثبت شد
🔹
بر اساس تصمیم امروز شورای عالی انقلاب فرهنگی تأثیر معدل دوره یازدهم در کنکور ۱۴۰۵ مثبت شد
🔹
متقاضیانی که تمامی دروس نهایی یک پایه را انتخاب کنند، بدون محدودیت در تعداد دفعات امکان ترمیم نمرات همان پایه را خواهند…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/657698" target="_blank">📅 18:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657697">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
مدیرکل فرودگاه کرمانشاه از لغو محدودیت‌های پروازی در غرب کشور و بازگشایی آسمان کرمانشاه خبر داد
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/657697" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657696">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-text">🔸
روایت مخاطبان خبرفوری از افزایش رهن و اجاره‌بها
🔹
باسلام. ممنون از اینکه به موضوع اجاره پرداختین.
متاسفانه بازار اجاره را هیچ کار نمیتوان کرد. باید این موضوع رو یاد اور شد که بحث اجاره فقط مربوط به تابستان نیست که مسئولین این موقع از سال بهش رسیدگی میکنند  و موضوعی برای تمام ماه ها است.
🔹
آیا از جهش وحشتناک قیمت مسکن مطلع هستید؟؟
قيمت ها حداقل دو برابر قبل از آغاز جنگ شده است؟؟!!
متأسفانه وقتی صحبت از تورم می‌شود ، بیشتر مباحث در حول محور مصارف روزمره مطرح می‌شود ، که البته آنهم مهم است .
امروز دیگر داشتن مسکن برای بخش اعظمی از مردم به رویای دست نیافتنی تبدیل شده است.؟
و ما ادراک اجاره بهای منزل ؟؟
بداد اجاره نشینان برسید!!
🔹
از شما اصحاب رسانه خواهش می کنیم اطلاع رسانی و به جد از مسئولین مربوطه پیگیری کنید فکری بحال این وضعیت خیلی بدگرانی مسکن و مامستاجرها بکنند.
🔹
سلام از مشهد پیام میدم قیمت رهن و اجاره واقعا زیاد شده و بیداد میکنه اگر ممکنه توی رسانه بگید صاحب خانه ها مقداری انصاف به خرج بدهد.
🔹
توروخدا صدای ما مردمو برسونید به مسئولان
زیر قسط اجاره خونه له شدیم به مولا  کسی نیست نظارت کنه
🔹
آقا چرا هیچکی به فکر ما مستاجرا نیست ما کجا باید بریم اعتراض کنیم؟؟؟
مگه با این اجاره ها میشه خونه گرفت مگه ما بدبختا چقدر حقوق داریم که نصفشم بدیم اجاره
#ارسالی_شما
الوفوری را دنبال کنید
👇
@Alo_forii</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/657696" target="_blank">📅 18:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657695">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
شهادت دو تن از رزمندگان پدافند هوایی ارتش در دفاع از آسمان کشور
🔹
شهیدان والامقام «سید بهمن حسینی» و «علیرضا عبیری» از کارکنان نیروی پدافند هوایی ارتش، در جریان مأموریت دفاع از مرزهای هوایی ایران و مقابله با تجاوز رژیم صهیونیستی دیروز به فیض شهادت رسیدند.…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/657695" target="_blank">📅 18:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657694">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0TufPJQdOVXQQDl3yHy6JFWTFgSzT1ZgC8BM77sHCevJze2Enk8W-YTrPIdQ5fhBOuG1UdtoSYn8xDzm5F3fgIAtHrCKkaa_LjXDvOtT6Qod3_DSWbpg6R4bKgek-MoTtuClUt1YGIVDCshfrGLbj34AIPqB11rcg_Cd3IQ7jIQ1EP1nVCOTt9gQoz8VByEFimc5Mww8aw0vW8eG61-ulMj_dK1xH-M2Wa4xiyD7W7AFOlbLsveS46c59uI6a8rMKy4umZrHLGpEc9fyawG1u_SGkAqXFP_0uf-oCFfWhmx28WIms1Wqbwbn7_GC_bQbyUiXIQ46TnVI4jUP3U4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/657694" target="_blank">📅 18:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657693">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای اسرائیل درباره بازداشت «جاسوس ایران»  پلیس و شین‌بت رژیم صهیونیستی:
🔹
فردی را که برای ایران در اسرائیل جاسوسی می‌کرده بازداشت کرده‌اند.
🔹
به گزارش تایمز اسرائیل، مظنون مردی حدود ۳۰ ساله است که گفته می‌شود حدود پنج ماه با یک مأمور ایرانی به‌صورت آنلاین…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/657693" target="_blank">📅 18:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJlPHa7KNOJczZ3RAGGwARvH6UV1oe5vjNBHVDu-GD-skNRxIUZdd7-O8qF-MEDr6P-fm9GDNbNyCVptQssZ_Uc_gY31Xoh9d3RwXvYZQNXe6vdzESHVoEWyZ-XJuzwBAhjiJVFOleHZYCUr_KOFLKwESbkNBHglQqEzG772xnf6tNSxQNJ3D039q-Y6G4N6fQbAjIJzJOrKsNzm9vxcAhxmWKMlg4qoqHvUknZ6xp9HNK2b423BboHdecU1MkUcdjAsT70LN5zRGlzNhvOAJOuuAgveTXIehNnVfkKcs_PMUIAnES87t106Z-EvDZeRa2R3fDyNo6jS97YlMHpT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خشم عمان از تهدید ترامپ به بمباران؛ او آشغال است!
🔹
به گزارش میمری، با تهدید ترامپ به بمباران عمان واکنش‌های بسیاری در عمان برانگیخت. منتقدان با تأکید بر حق عمان و ایران برای دریافت هزینه خدمات در تنگه، اعلام کردند که مسقط در برابر تهدیدها سکوت نخواهد کرد و تسلیم نمی‌شود.
🔹
بسیاری از آنها به ترامپ طعنه زدند و او را «دیوانه»، «احمق»، «تروریست»، «آشغال در کاخ سفید» و «برده صهیونیسم» خواندند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/657691" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niO5CPWEv_vZmpaHEdHwVedtQV46bv4RyKba6LGRjgp2RTx1tQ9QiWyCsXU2CnTwSC3VNE7uUcOT2AOYgt3gDWt0LISu56__VkxXqeOBq5EoGCy0aCYFerDQ0_l9o-RZmmXhZCrBSIncwJtFsAGhtAEKRnaeNdiu1rcmh-GLiw-ppTTO61qm9z7-Yx0RMCW3zW1-HYYfwNkVV4BqUKkDRVwuiAYl54kMY2JjieZvCMzB97bXq0voEteFqEt4oIlYTevEN_bhv3zKYCTpp2FmYnrqtnnCK0ceW5LUQgJqHHTBPnJybyFBz8Jtv-OIna_8A7y8CywaY-oWPXhWTKUijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفاوت تعداد بازی‌های جام جهانی که در سه کشور میزبان برگزار می‌شود
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657690" target="_blank">📅 18:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFaiIzdxpulRvlVw0QC16OzwlRHbmI1rg6JWV7e9n1EX69XGAbA5ei6nP5JOfcMWRpMmZPgzYtVWWk6tLKxodujj2eYi7WHgRD1tWDhHSQfgoLLR93XwiIXYkW8ZINg5C3FEEBJ8I9SqZ9s4N8ideH4P2hQXVa-avTPmRkWTvdL7lVmYVz2lXtfgF6oCcnrSD8GrADjMHUHZGSQiX2Or3PaX4qmdcMugVJZniGnq_roNeUQ5fVZb17rYz3wrOl6ZwPV2pm7T-E0ewliw2L8rnFfsgNC9fAqTVEo3KlLd2ogSdsKaJiZfztL8ONQaZ3X5KquUdxgsHRCyPvNkcBzhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکان خاتون، یکی از قدرتمندترین زنان تاریخ در جهان اسلام
🔹
ترکان‌خاتون همسر سلطان تکش و مادر سلطان محمد خوارزمشاه، زنی قدرتمند از قبایل ترک قپچاق بود که در سیاست و اداره حکومت نفوذی کم‌نظیر داشت. در خوارزم حاکم مطلق بود و فرمان او در سراسر پادشاهی مانند…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/657689" target="_blank">📅 18:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657687">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
مقارنه زهره و مشتری در آسمان امشب
سخنگوی کمیته نجوم آماتوری انجمن نجوم ایران:
🔹
امشب سیاره‌های زهره و مشتری با فاصله ظاهری حدود ۱.۶ درجه در کنار هم دیده می‌شوند؛ دو جرم درخشان که پس از خورشید و ماه، پرنورترین اجرام آسمان شب‌اند.
🔹
این نزدیکی تنها ظاهری است و فاصله واقعی آن‌ها از زمین به‌ترتیب حدود ۱۸۰ و ۹۰۶ میلیون کیلومتر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/657687" target="_blank">📅 18:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657685">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rannHfWnfvjhxFZz7Frb62y6MrGproUr96QC7HsIJSUcgoClCtAAWMlCCVGnF43TbtO-IbjPjq7Llam5r_Vr6TTCAKYVtUTwsyLVszI0YR8TAzGb4Bq-LVBKGqZSSN8XlZVYmVENXdky-wSFSCqhdau9RKBCzdx1rduIkHVn10VUu4XfeGipgjQFT8jOUqxnRVy-bHVe7rqgeefFacH6ae_eboON1wFRB4w5IATvdwCAdAycJJeiI0cSzk16q8QWnz9RQFvQISYEW94ZHwQl_1Gbrt5PVyjsfzeNaUUPucFk9TPKU3EYw3Sog_X_SWxOdSxhPgH_52rcAO952LyRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همکاری ترکیه و عربستان برای دور زدن تنگه هرمز؟
میدل ایست آی:
🔹
ترکیه و عربستان سعودی امروز در جریان دیدارهایی در ریاض، قراردادی را در مورد همکاری ریلی و اتصال راه‌آهن امضا کردند.
🔹
این قرارداد یک یادداشت تفاهم است که می‌تواند برنامه‌های احیای راه‌آهن تاریخی حجاز را پوشش دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/657685" target="_blank">📅 18:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657684">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqqf0jfZzBmpTvrgER7Uw59v2Gk3L0T5JoWSUlFELyfvouN57tytv6fHfzgXh9swhBlphCzuUkvlcLh2i5yeopQhihXD_-uS3hEnS9aLhfm3VRhxYm0pX1S8oSMI41p80Wk8a5pWbhMiLg1PfHw9tYX4M7ef8SbpH2t0LeckmeNknQIkgylLBKwoloa-ibhy2LTwzYAGba7TZLna-he8_KtAZUAxXaOfYyrX4OsRA14fhTG_XaDG_ldezs0B3IghmfznaOew41il417YT8iyOwL6u2HJCX2SysVFbw1DGqg9F0mh7gcwBbhn3444_auCQh2iAZR6jVU4tMDr9g2VMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه‌های مربوط به مالک و مستاجر در ساختمان
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/657684" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657683">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
تاثیر معدل دوره یازدهم در کنکور مثبت شد
🔹
بر اساس تصمیم امروز شورای عالی انقلاب فرهنگی تأثیر معدل دوره یازدهم در کنکور ۱۴۰۵ مثبت شد
🔹
متقاضیانی که تمامی دروس نهایی یک پایه را انتخاب کنند، بدون محدودیت در تعداد دفعات امکان ترمیم نمرات همان پایه را خواهند داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/657683" target="_blank">📅 17:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657681">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaW_ALlSYO0rc6uxZjUR5kVWJJ1nLrAnjiNTnzC1BQmJQgg_soJ0Ke7OUYrAKNbYmEVRFZKn3PwRGv_ZJ9r0mc1PFNUKtLhRSFyNr7Fqle06IBlgOpNszPnTySJj9dy4Y-7sVckf9xm_kLF0T4_wG6zEmILbXga6H8KhuQU93mFtOHz235bjVO3L7jXlouvgzGgyTEfc-gyK9CDK_3ZbaPJaTXry6wTq5zZFaFPpcK91Dsvr3HDxYTcwzshAD0atth44R_YSZoNewYUZDBaIaeEaMQzZw6eLBewS3BQg0AffdZEFjurfKiyxUP9lxMbmvkKj_6VJ4OQcAH7ycoS5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/657681" target="_blank">📅 17:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657680">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تعطیلی ۹۴ مدرسه در ژاپن در پی رویت یک خرس وحشی
🔹
ورود یک خرس وحشی به شهر اوتسونومیا در شمال توکیو باعث تعطیلی ۹۴ مدرسه و آغاز جست‌وجویی چندروزه شد؛ این خرس سرانجام بی‌حس و گرفتار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/657680" target="_blank">📅 17:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657679">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ec04e6d6.mp4?token=cXLgWiMux2iqgOgrw0DxwyH93JnxQZRYyrC9kz6qBFw_5_ULVNwC_ioHRmNVwNRsU7ZAdm53RJE27aIhY1lstudDGF50wowqumcRdM6ELNAVfPP2VO0X_2nPmU4rpXtJha3leIeMhPzmoo5DNpfhJIKVBHT51k-tyrf8VXCAbmCaxljV151vdB_5STM-RtDSNPPVILby6RWqr0UvH1bDfpKYrSe9NQcZZ3Of_K6nbz3Svw69ZViMfXqIGOcYtM_5ErD7KOL-WSIYcCR1qQuDa187vLBSJKF5HoHOY2TdWsGsifwBnEUVym8itdPm9_meLS2mEs2oFE35aDNk70Syzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ec04e6d6.mp4?token=cXLgWiMux2iqgOgrw0DxwyH93JnxQZRYyrC9kz6qBFw_5_ULVNwC_ioHRmNVwNRsU7ZAdm53RJE27aIhY1lstudDGF50wowqumcRdM6ELNAVfPP2VO0X_2nPmU4rpXtJha3leIeMhPzmoo5DNpfhJIKVBHT51k-tyrf8VXCAbmCaxljV151vdB_5STM-RtDSNPPVILby6RWqr0UvH1bDfpKYrSe9NQcZZ3Of_K6nbz3Svw69ZViMfXqIGOcYtM_5ErD7KOL-WSIYcCR1qQuDa187vLBSJKF5HoHOY2TdWsGsifwBnEUVym8itdPm9_meLS2mEs2oFE35aDNk70Syzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعضای طالبان گوشی‌های هوشمند خود را شکستند!
🔹
اعضای طالبان در ملأعام گوشی‌های خود را برای اعلام حمایت از ممنوعیت گسترده‌تر تلفن‌های هوشمند شکستند؛ در حالی‌که گفته می‌شود بخش زیادی از امورات دولت طالبان با واتساپ انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/657679" target="_blank">📅 17:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657678">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وضعیت در ارمنستان به نفع ایران نیست!
منصوریان، نماینده ارامنه جنوب ایران در مجلس در
#گفتگو
با خبرفوری:
🔹
نتایج انتخابات پارلمانی ارمنستان نشان می‌دهد جریان نزدیک به نیکول پاشینیان که رویکردی متمایل به غرب دارد، دست بالا را در پارلمان خواهد داشت و حدود ۵۰ درصد آرای پارلمان ارمنستان را کسب کرده.
🔹
ائتلاف نزدیک به ایران و روسیه تنها حدود ۳۰ درصد کرسی‌ها را کسب می‌کند و این وضعیت می‌تواند از منظر امنیتی و ژئوپلیتیکی به ضرر منافع ایران و روسیه در منطقه باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/657678" target="_blank">📅 17:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657677">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzNa_fsl2ixqNi5auLDTAON6TUBF4FZhY3k-9QD24Yxoio75YCihB-acdVRC9oFACNXIvje-5hiXiptsi4KpqzQ4bEEjVo0Go876dZNT9y93O6KNshWnap6AMks0bMlhMmWtdJuCEYTMKrzoMYXYZTsdScrxSM0y36DUjRVmbvJ2Dmr44Q2tOWBTwQhz20b3-eWwhIxELtIAyqU0l4RZNXPXdy6ybPm8S8jgSOqr7-fKGlzAOjRfkCUsF0w5gkn0REsPLvWY6YIzNJLPQVXzy-bABaeXiOCPo9OEB-RE4QORzlmoT-MW6ThLtrcFYpkUGx41Iryo-B9Vvv4TNkFtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سریعترین گل‌های زده شده در تاریخ جام‌ جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/657677" target="_blank">📅 17:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657675">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2hxAznyl7I8dvb6MstrLEUTfe7dBly9rz96nG8z76INNFEIJp4iQQJD8C8VdplmgTZbyJ-1k9ziBBA8scE61HyIGo_6u-gttbpeAXA9sjX5yPjXER4KePuQawOEL04pKCN59Bwt_fZtp3I8IHJhu9v_ehMb3mHlKOGxyzuQVDtBDeQcyKCmNVExMhd4Lv51uLoUp-digx22O30GhX0k1s2Iic2mGL_vFamiAehETszZcbaBj35Tca5w82unR4KuwWCWd7-lG6Nq0amfp8PRGpwaP1LvqzlOfv-HPTB3XHJROl2DEk0ESpSZGHtU62lIyRhNJhsBNRo6kKuEOGqxHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام رئیس مجلس به مناسبت صد روز جهاد ملت ایران: درود خدا بر شما مردم که پشت ایران را گرم کردید و کشور را از دهان گرگ‌های درّنده‌ بیرون کشیدید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/657675" target="_blank">📅 17:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657674">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10f45b40c.mp4?token=sNPwc7ufc9vMSRyTAN61t4dJ7Aczv3iu6k_D3FtNQzPbNNgR_crgz-Q7-yFi7rZXzZfPGmd-2HF2LCtDrdWXA4jPEpeeLlQGSGWQgyhJrJJPIMNYQnwTOSedX3cYuclsvyFoHUY5VgdCoTroWRScXyIJ9G3jXyRDP4LI7YO22g3qRDRZcviuHDuLZuS4MOy8JuXYLgUgiAjICCSLrypN2YuZRQsjjC_b4FPXBfroMRHohVWCNjd_KW2xqxraQK5aUbLerDhxUtVkn-bx6EmbOLAVXWRbT4ibr2RfBhOW_IMLZxpV43bygPYfgh233O9oynGGp5jEp60a7uaRKatd2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10f45b40c.mp4?token=sNPwc7ufc9vMSRyTAN61t4dJ7Aczv3iu6k_D3FtNQzPbNNgR_crgz-Q7-yFi7rZXzZfPGmd-2HF2LCtDrdWXA4jPEpeeLlQGSGWQgyhJrJJPIMNYQnwTOSedX3cYuclsvyFoHUY5VgdCoTroWRScXyIJ9G3jXyRDP4LI7YO22g3qRDRZcviuHDuLZuS4MOy8JuXYLgUgiAjICCSLrypN2YuZRQsjjC_b4FPXBfroMRHohVWCNjd_KW2xqxraQK5aUbLerDhxUtVkn-bx6EmbOLAVXWRbT4ibr2RfBhOW_IMLZxpV43bygPYfgh233O9oynGGp5jEp60a7uaRKatd2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ییلاقات رؤیایی گیلان
🔹
حمزه توکلی
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/657674" target="_blank">📅 17:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657673">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
هزینهٔ طرح ترافیک امسال اعلام شد
🔹
امسال هزینهٔ رزرو روزانهٔ طرح ترافیک برای خودروهای دارای معاینه فنی برتر ۲۷۸۴۰۰ تومان و برای خودروهای دارای معاینه فنی عادی ۳۴۸ هزار تومان است. همچنین جریمهٔ ورود به محدوده بدون رزرو قبلی ۵۲۲ هزار تومان خواهد بود.
🔹
خودروهای برقی مشمول ۹۵ و خودروهای هیبرید مشمول ۹۰ درصد تخفیف هستند. ساکنان محدودهٔ طرح ترافیک می‌توانند پس‌از ثبت مشخصات واحد مسکونی در دفتر خدمات الکترونیک شهر، روزانه یک تردد رایگان قبل‌از ساعت ۹ و پس‌از ساعت ۱۶ داشته باشند. همچنین تردد بین ساعات ۹ تا ۱۶ برای این افراد با ۵۰ درصد تخفیف محاسبه می‌شود.
🔹
خودروهای دارای پلاک تهران در هر فصل ۲۰ روز سهمیهٔ تردد رایگان در محدودهٔ کنترل آلودگی هوا دارند. این سهمیه برای خودروهای پلاک شهرستان ۱۵ روز در هر فصل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/657673" target="_blank">📅 17:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657672">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq-D1imCIjXis0beibgrjdrEmCXIfvui1UYeLKwku0iTESzeF9ShZ00VSIZskcopwU7az8gtmKRz-8uNTSi5Rl2sula0wti6CVDlVFuelnRRQ9Gq55RzB_JCiES-PuKG1hKXrCJ1T1VezjhJw8X1vcPrmpKtJF-0FpZLmhSI3pGeLXY4FRxEfpjCxU1okrDXAUXsn3fxSY4a8TxTpxZzJO5WtivnLScRkNWHC2T2V9IvcRV_ACObCqFHS3xWIGKSE-2r49O-s-259D_ygjSMgNt2dWBeHGLP37hyO19gCSVFK7LnErKMr43ZLNgBRJ58mfLrBjB-AL4_NIRVKM1xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موج مخالفت با جنگ ایران در نظرسنجی‌های جدید
🔹
بر اساس داده‌های نظرسنجی‌های منتشر شده درباره حمایت از جنگ ایران، اکثر افکارسنجی‌های انجام‌ شده نشان می‌دهد میزان مخالفت افکار عمومی به‌طور قابل توجهی بیشتر از حمایت است.
🔹
در این نظرسنجی‌ها که توسط مؤسسات مختلفی مانند YouGov، Ipsos، Rasmussen و New York Times/Siena College انجام شده، سطح حمایت از جنگ عمدتاً بین ۲۸ تا ۴۰ درصد و میزان مخالفت بین ۵۱ تا ۶۴ درصد گزارش شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/657672" target="_blank">📅 17:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657671">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a5b99280b.mp4?token=BYgeu-58B4tRl7fA_aSg4GZt7jm5Fy6hMDyAe0oS0wF8KGME3_h9GqOZ0fDXZCERobRZQ8TqbCzNEB8AzjfKon9FcAq4z_Hli60BITRXXoO6KDmR2Cz4Rhf_veCPjvqimDeMJ4otZkJ3QXMypBKRsFYGkcNLgcokIXTrwyaRBjlVtmvfs8fm3Y8tCl9b87RG6oB-q0_4JLgu1KSwRghikql4Kme6kSdyKwL8gBAaUIlrOP4IPgTVBs4OP-OCPOokvxY1GJiAU5M34bRFgjoF9CAaGfi2oQtHb54h1YEzvqpPEO2QPZbj6zXvxC9dwJvQiyBOya1VRsAgSLT7zMd7Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a5b99280b.mp4?token=BYgeu-58B4tRl7fA_aSg4GZt7jm5Fy6hMDyAe0oS0wF8KGME3_h9GqOZ0fDXZCERobRZQ8TqbCzNEB8AzjfKon9FcAq4z_Hli60BITRXXoO6KDmR2Cz4Rhf_veCPjvqimDeMJ4otZkJ3QXMypBKRsFYGkcNLgcokIXTrwyaRBjlVtmvfs8fm3Y8tCl9b87RG6oB-q0_4JLgu1KSwRghikql4Kme6kSdyKwL8gBAaUIlrOP4IPgTVBs4OP-OCPOokvxY1GJiAU5M34bRFgjoF9CAaGfi2oQtHb54h1YEzvqpPEO2QPZbj6zXvxC9dwJvQiyBOya1VRsAgSLT7zMd7Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواداران برزیلی هنگام پخش سرود ملی آمریکا در بازی تیم فوتبال زنان برزیل مقابل آمریکا در سائو پائولو، شعار «هی ترامپ، گم شو» سر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/657671" target="_blank">📅 17:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657670">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e8918431.mp4?token=ctWn4GST0X9k2fl3ZBAzJSEA7MiWq6Tl0uB-TiVXOLvEj-EC_crVTw74LNjDvlJH1Jt1R4WmDQfti3T5Zi8zrmt2YgSim2f07m1lwAwIAaZiRTNQTsgGa7f6rnJuN7cdjRWwhEfbOsLi1ohf75VA6XBKwBc7o4aWQYNLqgbbbBC-pV38KSBt5TqbFRZuH_d-fa0kXHlPANvG5inUX7UdhuRBjViuaBR9MygwY_nWvtw1Vc76ipvOXUsjv3iF71wNC3wxC8YDiaOHUih5C-ww208f_Y4w311JE-Jn__T1cIogh1o0_vFAO1DmTfDtVlw6vlyK2eBPbZz1lnWGSF1fnxobXs5-bncNiSRYaPDKswpOTnkTLZQL83uVP330NdQzer86WTUj48QENq-bQ39g4Xqnn4i3x5hgkLpAPD79h5sjITUskjR5ZpjHTU80L6HY5G6ZLr_HhGbxbzxaXq4J-bgRDCbbEuL_VsNRwUBwhcbUVMfBUNrMAlZXtRmz00GAR1_inyyqNXxQplEYM-v23aAgQiXoulLlDs92U6OveWwMyx8euUM3SbS8MB2J5Y3JLcfJXhSu3Ap55tIxZD_jpvCwYNRWPc1kP-K7YpQG_yWsHwC6LZ2pcv4j5U7wDytNTjJFx5XYU1orxlakjaeMZSqEg-Abjy2K6sPV7DIpIOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e8918431.mp4?token=ctWn4GST0X9k2fl3ZBAzJSEA7MiWq6Tl0uB-TiVXOLvEj-EC_crVTw74LNjDvlJH1Jt1R4WmDQfti3T5Zi8zrmt2YgSim2f07m1lwAwIAaZiRTNQTsgGa7f6rnJuN7cdjRWwhEfbOsLi1ohf75VA6XBKwBc7o4aWQYNLqgbbbBC-pV38KSBt5TqbFRZuH_d-fa0kXHlPANvG5inUX7UdhuRBjViuaBR9MygwY_nWvtw1Vc76ipvOXUsjv3iF71wNC3wxC8YDiaOHUih5C-ww208f_Y4w311JE-Jn__T1cIogh1o0_vFAO1DmTfDtVlw6vlyK2eBPbZz1lnWGSF1fnxobXs5-bncNiSRYaPDKswpOTnkTLZQL83uVP330NdQzer86WTUj48QENq-bQ39g4Xqnn4i3x5hgkLpAPD79h5sjITUskjR5ZpjHTU80L6HY5G6ZLr_HhGbxbzxaXq4J-bgRDCbbEuL_VsNRwUBwhcbUVMfBUNrMAlZXtRmz00GAR1_inyyqNXxQplEYM-v23aAgQiXoulLlDs92U6OveWwMyx8euUM3SbS8MB2J5Y3JLcfJXhSu3Ap55tIxZD_jpvCwYNRWPc1kP-K7YpQG_yWsHwC6LZ2pcv4j5U7wDytNTjJFx5XYU1orxlakjaeMZSqEg-Abjy2K6sPV7DIpIOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
ترامپ قمارباز: یک یا دو روز آینده شاید به نتیجه‌ای با ایران برسیم
🔹
ما مذاکرات مداومی با ایران داریم و این مذاکرات متوقف نشده است. ما می‌توانیم حداقل تا یک یا دو روز آینده به ایده‌ای برسیم. فکر می‌کنم اوضاع خوب پیش می‌رود.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/657670" target="_blank">📅 16:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657669">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxXLLd01ZHhzXKZWkOAfdKgCBTXOHwtyg_dMO9NVf1C5T6K-Fc8M2OmO2iCi-eoMX0vzpkqgKIiA9y5g4Iil7t7LNC9izX_NT8d-jDWcA8-w_zHwpfK860xgUUsT2K2P0aB0nOqS8KXthazL_SWDfGGvQIH_p2qqyg3d06G4kBbw0s9FYMDpfTtygDMMWN-447NmP-MfxIcqTKbKmApRKqEei62dB3tt9Up4ftpmUZhFJdVlTojKMR_8qUXueCpycuk1Bo-BusbZ03DVbloJDlIcinmjZ0A2Tjvm-atChBSfcrh8Oawg0ueu2RNwlORTeFpSyOnBRx_d-58_IpkvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای کامل خرید طلای آب‌شده
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/657669" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657668">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRU6Q0XMErDS2VhAlmOL67Qwh4CzKnsnsFjpZzhiTNmuzg20k929arrtMbMmcmN9rdXcEymyADKTyAt4x58KFzhcdI5IqVI8B1plRwP36fibP7F9ccPx-e5Aa0oT_ZHrqiukXSSUK8ElPkaOZoRVJ-BxGtHhaDdCUucQdmUnJp_WadEtpd1OWAAYDC4jSwL7exavhQHEdPTvWWl6q5F5eLbT6z5OeEWnc-mEt0wBUbKZ-R9Ave4DgEFp7HQ2JRMdpsz0dJUYb4Etc2ToKlyhL7IG6Z7t54qFsvLDURYJDNOGr05IFpGmT_nQonj_v2_adhLla9My10LztptvT1nuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رِد بانک؛ با ارائه مجموعه‌ای جامع از سرویس‌های بانکی، سرمایه‌گذاری و هواداری فوتبال، تجربه‌ای متفاوت و یکپارچه را برای کاربران سراسر کشور فراهم آورده است.
🟢
در قالب طرح «رِدبانکی شو»، کاربران جدید پس از دانلود اپلیکیشن(دریافت از آدرس:
https://red-bank.ir/download
) انجام احراز هویت و افتتاح حساب، مبلغ ۱۰۰ هزار تومان هدیه افتتاح حساب دریافت می‌کنند.
🟡
همچنین هر کاربر می‌تواند با دعوت از دوستان خود از طریق لینک اختصاصی، به ازای هر افتتاح حساب موفق، ۱۰۰ هزار تومان پاداش دریافت کند.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/657668" target="_blank">📅 16:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657667">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سامانه کنترل قیمت مسکن به تصویب هیئت وزیران رسید
علیرضا نثاری، رییس کمیته مسکن کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
وزیر راه و شهرسازی در جلسه‌ای اعلام کردند این سامانه در هیئت وزیران تصویب شده و کارهای پایانی آن انجام شده است و به زودی آغز به کار سامانه شروع خواهد شد.
🔹
در این سامانه قرار است سقف افزایش قیمت‌ها مشخص و قیمت‌ها کنترل شود. اگر کسی از این قیمت‌ها عدول کند نیز از مراجع قضایی و حقوقی قابلیت پیگیری داشته باشد. سامانه به این شکل است که هرگونه قرارداد رهن، اجاره، خرید و فروش در آن ثبت می‌شود و قیمت‌گذاری در آن فرایند تعریف شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/657667" target="_blank">📅 16:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657664">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای اسکای نیوز: پیشنهاد جدید ایران برای آمریکا ارسال شده است
اسکای نیوز:
🔹
ایران پیش‌نویس پیشنهاد جدیدی را به ایالات متحده ارسال کرده است. این رسانه همچنین ادعا کرده که طرف آمریکایی این پیشنهاد را «قابل قبول» می‌داند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/657664" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWVmsqV9JBH_HHrD7OQCeE5Ll7zfHfdrLnPBEdSYxukliKWWwsgkKCLFS1xXK3Mmnxvlf_oaCNVaRJjUxktUWYh4DjIZkuIcub_nuisCNVPNpcplavdUeNG49ofvz-WNsiDMZUjYR7nfKT4DiEMidPImA91k7qBszsxuDMb_VABmz0x336ZFOOln4L_sAhASjwFtxG_c_HTcqQlVQWX67Ks--_CRjs1sqEP9vScI45z9qKMeqaGYG9VKLrud96Dod6ZrOgQl8uRa6N3j06pa5kqyWWfSUe7-yMQpuitNO3G-rkt_hPBOmjosi05gDTT9HyWAHuoH-gTZBnrvMiX4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6aad3ad89.mp4?token=TNxmCJh__i2dg5zTvDIDjfdCBg94opKlRdtlp-puVtVB-2oiu0K4EGYcWH_1dmos2GGl4K9R72LvC5od3-RfDN0jZDFhlkDQG3mQVmYxREMa3TvtEXSzaGiv85_ZZsCBjubklHrDzp5ydN-3yfh8mSggHVL2LSwxrKlOxqHAAns-pF0jg0M47F2oaHW_C8mAYNvJz51SKiNisPcTO2u6_nMqziJLQRmfWyc3siEkp4vCtgDhPcPar8dc3gwKdl8eN44URofn4E4lk7kn2uEqIbdYBFiP-tm6DVVJ9WboLuge28dXsxYjqoiIa7FM3Lcq5zR2hH6_UiZ99RC50vFL9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6aad3ad89.mp4?token=TNxmCJh__i2dg5zTvDIDjfdCBg94opKlRdtlp-puVtVB-2oiu0K4EGYcWH_1dmos2GGl4K9R72LvC5od3-RfDN0jZDFhlkDQG3mQVmYxREMa3TvtEXSzaGiv85_ZZsCBjubklHrDzp5ydN-3yfh8mSggHVL2LSwxrKlOxqHAAns-pF0jg0M47F2oaHW_C8mAYNvJz51SKiNisPcTO2u6_nMqziJLQRmfWyc3siEkp4vCtgDhPcPar8dc3gwKdl8eN44URofn4E4lk7kn2uEqIbdYBFiP-tm6DVVJ9WboLuge28dXsxYjqoiIa7FM3Lcq5zR2hH6_UiZ99RC50vFL9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش احساسی پاندا «فو بائو» به صدای مراقبش منتشر شد
🔹
این پاندا پس از حدود سه ماه دوری از مراقبی که از بدو تولد کنار او بوده، با شنیدن صدای او واکنشی قابل‌توجه نشان می‌دهد؛ لحظه‌ای که توجه کاربران فضای مجازی را به خود جلب کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/657661" target="_blank">📅 16:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657659">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سه نجات یافته از حوادثی که هیچ کس فکرش را نمی‌کرد
​​
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/657659" target="_blank">📅 16:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657658">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
قیمت‌ مصوب ۴ قلم محصول لبنی اعلام شد
🔹
شیر نایلونی کم چرب ۹۰۰ گرمی ۸۴ هزار تومان
🔹
شیر بطری کم چرب یک لیتری ۹۸ هزار تومان
🔹
پنیر یواف ۴۰۰ گرمی نسبتا چرب ۲۰۳ هزار تومان
🔹
ماست دبه‌ای کم چرب ۲ کیلوگرمی ۲۲۸ هزار تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/657658" target="_blank">📅 16:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657657">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
قیر ۴ برابر طلا سود داد!
🔹
از ابتدای مهر سال گذشته، برخی دارایی‌های قابل معامله در بورس کالا بازدهی چشمگیری فراتر از طلا و سکه ثبت کرده‌اند.
🔹
قیر با ۲۵۱ درصد سود در صدر بازدهی‌ها قرار گرفته که ۳.۷ برابر بیشتر از طلا سود داشته است. پس از آن، شمش نقره با ۱۵۰ درصد و مس کاتد با ۱۱۴ درصد رشد، عملکردی بسیار قوی داشته‌اند. در ادامه، شمش طلا با ۶۸ و شمش روی با ۶۴ درصد سود در رتبه‌های بعدی قرار گرفته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/657657" target="_blank">📅 16:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657655">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llnabQUP5UAmOg9mCR5aSztGUgA4lQbxabRsS3ItgZkdQ6jCvcwj4EFIUTdc6ylmlVfr7CfKhYu4RyBkn-YsHAbYbhy4PRAaBVNL3YzK7DdMWs5ZZKudToquK9ISklL3KZ5_ckODZI5yK_3Q8bPjuO2RlH7KcbUF54z1hHg6X7YUlAmnOyBEtmCwiybOhesfChVRN1tgUkQu6gU7xyOnFSVOdOf2WthOiu5GOe-6QsNNwdfCgtQRUkBIPGD-mm6xtOLMkKq85pzsKpH4RdpIZYIU2Y5JxX7ixSkpRROxLvur-yIUtyjr6lxLMOEIH8z4GCSV8V1qQHigKrFXvuvyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قانون عجیب جام جهانی ۲۰۲۶؛ نیمکت‌نشین‌ها در رختکن آماده می‌شوند!
🔹
به‌ دلیل گرمای شدید در برخی میزبان‌ها، احتمال دارد بازیکنان ذخیره تا لحظه نیاز در رختکن بمانند و فقط هنگام تعویض برای گرم‌کردن فراخوانده شوند.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/657655" target="_blank">📅 16:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657653">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJtlxpwMOixTOAQtSZdSvbP09vh4cFoDdYrd1PzODZUsclpQ6rchCvgxxSrCmxrxc2fCGflDtdAmXvb5lijgULwauZjRb-XSvMk3VQjJrN0m2Lk9ku_r1IlLq2biLNkLylSXS0kcEObFXfhsqAEAebHGTmh_VtaC5KarRKus2NfN28JQ_2a2DSt3jUmQNxFpOkwNIT86RUV_n3FT7_fPYjj3TNVqJBH4WPbWiP4EnjnN_2kxzzGTDsfXLZTUo_4UQUpHhjOf6T9ivwtkx27YhllGYeBbdWlK1IKG978jEL8UpEhomAeJsJwS3tQlU-YXIhyBGdk29AORdnGo5eRkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا سقوط هلیکوپتر خود‌را در تنگه هرمز تایید کرد  سنتکام:
🔹
ما دو خدمه یک بالگرد آپاچی را پس از سقوط آن در نزدیکی سواحل عمان در حین گشت‌زنی نجات دادیم./ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/657653" target="_blank">📅 16:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657651">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c267b4079.mp4?token=rGz8iGvqBujxcHd1keNFBSx26AxLjIS_8wkzSkRSE1gvWIxnMVtTCz37pmpiUvxS3mJ3_KOJ__ctEFn3V5pJZ1cOfxGT9i4vjGJv2OeEcKPkmXLaqEqUdJ6TfzL5cAJtnV7BUsy0XrzqID7lcZbKfQFIpQmQxO8mxaaHx3EjjXsEA3POSiHp8dINJ5GQC_U8XZZAm3zdnR3e_myZuR80nTANM42-h9iRrZsM1J7Pi0DCx4hVsOTD9SF2NLCsJyKRreFy9YsKNTTq5ZK49FPrQJjrXskE8Yn7rlmdE9eowLFfJ_Y5wR1YBcmrdvnSljshpaxOJ_Yw5eyqTe8i50WaFxCN0jwDduEbyJmy12vE3PuFubOc6S9HJm3x7VmRvYyZmmnQNaBaTROOa051M7l_5pUPBx_hOmVirKbtLSOOk67DBhj1yUhecRR_LGUXc2BpQeL_UA18KX97Xferx0OkEVvk-iI7QceY4o4RZziRkcWr8aQ-7J1dHl9AOxP6jQonubsGs1d58iJ0rutBcz0g5efkS9Lx5kqPcDt8zSFNO5N3GE2v87cGeuhFxynDGszFGvshB8nnFo_xvwRmlccssd4ecnJIJxlh6oua2m0ST6E0lCM9Jpxpk5wVworXm2pa4394XrRElPrL2qddGE0a9iYTI7Ww9XtHVnjXIDhV_kI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c267b4079.mp4?token=rGz8iGvqBujxcHd1keNFBSx26AxLjIS_8wkzSkRSE1gvWIxnMVtTCz37pmpiUvxS3mJ3_KOJ__ctEFn3V5pJZ1cOfxGT9i4vjGJv2OeEcKPkmXLaqEqUdJ6TfzL5cAJtnV7BUsy0XrzqID7lcZbKfQFIpQmQxO8mxaaHx3EjjXsEA3POSiHp8dINJ5GQC_U8XZZAm3zdnR3e_myZuR80nTANM42-h9iRrZsM1J7Pi0DCx4hVsOTD9SF2NLCsJyKRreFy9YsKNTTq5ZK49FPrQJjrXskE8Yn7rlmdE9eowLFfJ_Y5wR1YBcmrdvnSljshpaxOJ_Yw5eyqTe8i50WaFxCN0jwDduEbyJmy12vE3PuFubOc6S9HJm3x7VmRvYyZmmnQNaBaTROOa051M7l_5pUPBx_hOmVirKbtLSOOk67DBhj1yUhecRR_LGUXc2BpQeL_UA18KX97Xferx0OkEVvk-iI7QceY4o4RZziRkcWr8aQ-7J1dHl9AOxP6jQonubsGs1d58iJ0rutBcz0g5efkS9Lx5kqPcDt8zSFNO5N3GE2v87cGeuhFxynDGszFGvshB8nnFo_xvwRmlccssd4ecnJIJxlh6oua2m0ST6E0lCM9Jpxpk5wVworXm2pa4394XrRElPrL2qddGE0a9iYTI7Ww9XtHVnjXIDhV_kI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در فینال بسکتبال آمریکا چرت هم می‌زد
🔹
رئیس‌جهور آمریکا علاوه بر هو شدن توسط مردم، در میانه‌ی بازی فیتال لیگ بسکتبال حرفه‌ای کشورش، با چرت زدن خود توانست برای بار دوم به فاصله چند دقیقه، تبدیل به سوژه‌ی داغ رسانه‌ها شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657651" target="_blank">📅 15:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657650">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXtf18BHDBaIBXIuUQnWA9ftfUEs8MEtX1IAOeNqE2isHSAyj1_5b8YX6OiKZ8cKmiTPejzC265kleKaOamHbt_2YAZJLzOEAQkHHcCXvCYSqjikCaZNkgaurz5TkHbJc2IjA4KSJGKncO1nqRYeaZg9kcyyMkcBFHNdBdp0fZdTdiHY7h3thRUKMRgMmyg1HxHj2EVAsmZpqum1LECeTuhpKIC4XWBeIL_wcYfs8pNi9g2Y6rboKqrLKjAY7PHnQjsADxX9C_ZoSs5E9IfHYs2gvHgnwpo1dJEB5G0ZXK8XWXgN2d8KmMPIYp0yEY4pkbRVcopsl3tf1bV7z3inWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطالبات معیشتی در صدر خواسته‌های بازنشستگان
🔸
در این نظرسنجی حدود ۳۰ هزار نفر شرکت کردند که سهم روبیکا ۵۸ درصد، بله ۳۰ درصد و تلگرام ۱۲ درصد بوده است.
🔸
بیش از سه‌چهارم شرکت‌کنندگان، افزایش و همسان‌سازی حقوق متناسب با تورم را مهم‌ترین مطالبه بازنشستگان کشور دانسته‌اند و حدود ۱۰ درصد نیز پوشش کامل هزینه‌های درمان را در اولویت قرار داده‌اند.
🔸
مطالبات بازنشستگان بیش از هر چیز بر حفظ کیفیت زندگی و تأمین امنیت اقتصادی و رفاهی در دوران سالمندی متمرکز است.
@amarfact</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/657650" target="_blank">📅 15:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657649">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkHv6FNhREOtORemuMG2LwNTBP_Ty5GvqR25V6uel2NBc_ccQ_uNg82BKPWRfMeGrFj-2OGbHkNNhw1yu0FVJzLIcbTjEV6veH-kSRYXtqHCzrlc3OiYueb8EcH2lhpjni7Uf_BTBXYW_04mjuWpq_yqO65XhxL5OMS0VM5mjiBxeFPMk1NTr1CurFW04r-iazeRGLFToiK3bphuifjgi3fuFAAIBWAxI2AAh1NmYl4gM7GXaydKanSWYHlcSeugaj6pMAU8tKVzjHShzrevZeOHkb3bRmgnS7uKqUTQIR5BU_JTPymrjGrmR-WA2EWqRVIdVEKFtinA6tXlJxD8Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونس: ایران برای ما یک باتلاق طولانی نخواهد بود
جی‌دی‌ونس، معاون ترامپ در گفتگو با یو‌اس‌ای تودی:
🔹
مطمئنم که دخالت آمریکا در جنگ ایران ظرف یک سال پایان خواهد یافت و به یک باتلاق طولانی تبدیل نخواهد شد. آمریکا یک سال دیگر درباره جنگ ایران صحبت نخواهد کرد.
🔹
کمپین آمریکا در ایران مانند جنگ‌های طولانی مدت در عراق و افغانستان نخواهد بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/657649" target="_blank">📅 15:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
پیش‌بینی مقام اسرائیلی از درگیری دوباره با ایران در روزهای آینده
🔹
یک مقام ارشد امنیتی اسرائیل در گفت‌وگو با شبکه کانال ۱۴ اعلام کرده است که بازگشت به درگیری‌های گسترده با ایران تنها مسئله زمان است و احتمال وقوع آن در روزهای آینده نیز وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/657647" target="_blank">📅 15:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657645">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594890a614.mp4?token=Nim0Zq6xofudHIAnciNn2wpJmbLgakgbPHTwbBn3X5bn8HpDfouPrFYuMfYiJeGKm-3lRp2Msp_IYoxCF94rKY-PUrz6wdO3Lkuw8CFY_x7T0w-u4lEYf8JH3QvvG3RtU5fSuMN5uqBO9NciT8tvvi6S3nJoWOXKLUuz0kBPP4w5yy2wM6QSrtVGXfAJmvjcpQzAblZYG_PriWpPbOKxgd7zZw0Hu-H06GJwPicbZaV8FUcfn6Ik9-SXpRVVZBoshVJ2SdlA6B9tgVTutsm7SMpSpArylmsC41Tuyg23XCJMxvYngqJoEye_c1aIylqjZuL6TnxcSNtquQ_aK7tGBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594890a614.mp4?token=Nim0Zq6xofudHIAnciNn2wpJmbLgakgbPHTwbBn3X5bn8HpDfouPrFYuMfYiJeGKm-3lRp2Msp_IYoxCF94rKY-PUrz6wdO3Lkuw8CFY_x7T0w-u4lEYf8JH3QvvG3RtU5fSuMN5uqBO9NciT8tvvi6S3nJoWOXKLUuz0kBPP4w5yy2wM6QSrtVGXfAJmvjcpQzAblZYG_PriWpPbOKxgd7zZw0Hu-H06GJwPicbZaV8FUcfn6Ik9-SXpRVVZBoshVJ2SdlA6B9tgVTutsm7SMpSpArylmsC41Tuyg23XCJMxvYngqJoEye_c1aIylqjZuL6TnxcSNtquQ_aK7tGBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت ۳۷ وعده ترامپ درباره توافق با ایران
🔹
ترامپ بار دیگر گفت توافق با ایران «ظرف دو هفته» انجام می‌شود
🔹
ادعایی که در ادامه ۳۷ نوبت اظهارنظر مشابه او در سه ماه گذشته است. در این ویدئو خواهید دید
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/657645" target="_blank">📅 15:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657641">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0439452658.mp4?token=EJa4Pc1Fj5bgVMbxKUEdK1_GvXsiT10QtfK48J1QbRYlFApcXgKQmWx9j_qxeylDggbZ9uxGTJNJ3h0GFLUS4SMsbxZzn-JKHD-VrmSGbZwKZrNmbXP_0ZZ50GwUO2DA8aTDK0zBDjjW4Par6KsMe7KMJOm4jbJ3Coy9A-REN-syCCRl2u-EYeesGkvFHlKgzs9pUnFe8t46iLCmuzqIUZQfSJgNDeUx-Mo2bYi401d1_hBMHJuDI5a-_Rp8F3EfKYqMZmay2WAFpxtpoBrXwqDpd5JCm6AHZBUz3gncKhmgp2sZ8OffXFCWs2abLboVnx_mwxcKRPw5vnz_-sOr-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0439452658.mp4?token=EJa4Pc1Fj5bgVMbxKUEdK1_GvXsiT10QtfK48J1QbRYlFApcXgKQmWx9j_qxeylDggbZ9uxGTJNJ3h0GFLUS4SMsbxZzn-JKHD-VrmSGbZwKZrNmbXP_0ZZ50GwUO2DA8aTDK0zBDjjW4Par6KsMe7KMJOm4jbJ3Coy9A-REN-syCCRl2u-EYeesGkvFHlKgzs9pUnFe8t46iLCmuzqIUZQfSJgNDeUx-Mo2bYi401d1_hBMHJuDI5a-_Rp8F3EfKYqMZmay2WAFpxtpoBrXwqDpd5JCm6AHZBUz3gncKhmgp2sZ8OffXFCWs2abLboVnx_mwxcKRPw5vnz_-sOr-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مناظره داغ و جنجالی رسانه آمریکایی سی‌ان‌ان درباره ایران
🔹
ایران چند آمریکایی را در خاک آمریکا کشته است؟ جواب صفر؛ چرا سربازان ما در خاورمیانه بودند؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/657641" target="_blank">📅 15:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657638">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWw_LornMC8qrLAxmPmAZWNhsE9oNk7fsVu1Jb875AAqfdtXDDCBuot-sMPlLZ2NKuPxtqiq1Mb3j7dBA7No_e3xhaCQKtIDxH3AVQjQNFhhT3MuKmLXD0OpubKn-5RjAsEGUaj5bafbKqHnlzdskSnZWOSvK1u6q6OCyGESWvzYYCZf6Z7ROX4mxnh-J1VXf-Us6cpt3y9L2ubagAH-a4RE_losZJHOXml6dPJTxpa4Ecgi9dlbktYxV1jDkB05mJwnKzRvxHbpot8QUSCX8kcJ33sg6Bq-Rm7UxgkLH-1Ho29d-5Lk2HKZZW7GtVVKr8JInppVGyFtz2SQoRkDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یدیعوت آحرونوت: تصاویر ماهواره‌ای نشان می‌دهد که دو روز پیش یک موشک ایرانی با دقت به یک آشیانه در داخل پایگاه هوایی رامات دیوید اسرائیل اصابت کرده است
/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/657638" target="_blank">📅 15:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657636">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
اسرائیل مدعی ترور ۲ فرمانده جهاد اسلامی شد
🔹
ارتش اسرائیل مدعی شد دو فرمانده ارشد وابسته به جنبش جهاد اسلامی فلسطین را در حمله‌ای هوایی در جنوب غزه هدف قرار داده و عملیات موفقیت آمیز بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/657636" target="_blank">📅 14:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657633">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bbab9bb2.mp4?token=PlavUTIVmCv3uMdjv7eb6vz9vnAndvxBG1TRwxHiJ-bxjqgFALRd88sdw3z39zfgdMeqpHPQUO7xje6PPx_5V31z-y6GKjQl4WyPuHUuUC7VGX0vncCE15bS5I67ORtCALsUy9fcCAFlarYtMYFunnx9cIlerGa1olKZNSoCJXx1yORDnoPSiH7GPyWOnSy6CamhQRDKbcVueIKrVE6mOp8hBP34nbZUgRxDv0IxEYovxRw7xBKw5oDJglrJEm_v4KQRX-7ZU1cMVEIi_j5M4qBmyD9wuDKMa3qYtrn_9Cp5jM8ccu0daxEge8295GtlWYryAGZJ897q6aqRjTvZDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bbab9bb2.mp4?token=PlavUTIVmCv3uMdjv7eb6vz9vnAndvxBG1TRwxHiJ-bxjqgFALRd88sdw3z39zfgdMeqpHPQUO7xje6PPx_5V31z-y6GKjQl4WyPuHUuUC7VGX0vncCE15bS5I67ORtCALsUy9fcCAFlarYtMYFunnx9cIlerGa1olKZNSoCJXx1yORDnoPSiH7GPyWOnSy6CamhQRDKbcVueIKrVE6mOp8hBP34nbZUgRxDv0IxEYovxRw7xBKw5oDJglrJEm_v4KQRX-7ZU1cMVEIi_j5M4qBmyD9wuDKMa3qYtrn_9Cp5jM8ccu0daxEge8295GtlWYryAGZJ897q6aqRjTvZDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات سخنگوی دولت درباره حذف یارانه برخی دهک‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/657633" target="_blank">📅 14:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657632">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde5aa2c4e.mp4?token=oTMZh2HXMJ6TFhBSNOG_IMp0WogmBHFgu3k0BUEugHQG5DropsuZ4D619N-tzRM5dOJ84C8V2coCza0tI9m_mT9KS1JDmFdTNrl40ICw-hPj6WXWe9BZW2IrJDxdG-dFeuWnHyehqolQU9Me_086tBegfoeVvaxzQshSRaYTOcbahzcQJYvW1uDxsNPtHfx6vX8eDrGs5EPCJo0d5ZT2M9c4bwMiT-ZRH1KiL0q8oRFMkwssbaZS1eLmJL-G_x7qUsOAnt6wOYANmoPRLc77qWaB6QengVrdsZx-WfPmdck3eC0ryi2L9Qf1Cu-8mPRio0_s9KW5SNc2t84GSOb31w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde5aa2c4e.mp4?token=oTMZh2HXMJ6TFhBSNOG_IMp0WogmBHFgu3k0BUEugHQG5DropsuZ4D619N-tzRM5dOJ84C8V2coCza0tI9m_mT9KS1JDmFdTNrl40ICw-hPj6WXWe9BZW2IrJDxdG-dFeuWnHyehqolQU9Me_086tBegfoeVvaxzQshSRaYTOcbahzcQJYvW1uDxsNPtHfx6vX8eDrGs5EPCJo0d5ZT2M9c4bwMiT-ZRH1KiL0q8oRFMkwssbaZS1eLmJL-G_x7qUsOAnt6wOYANmoPRLc77qWaB6QengVrdsZx-WfPmdck3eC0ryi2L9Qf1Cu-8mPRio0_s9KW5SNc2t84GSOb31w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کپلر: تردد در تنگۀ هرمز به‌شدت کاهش یافته است
مؤسسۀ رهیابی دریایی کپلر:
🔹
داده‌های ماهواره‌ای از محدود شدن قابل‌ توجه تردد کشتی‌ها در تنگۀ هرمز حکایت دارد. در ۳ روز جمعه، شنبه و یکشنبه تنها ۸ شناور تجاری و غیرتجاری از تنگۀ هرمز عبور کرده‌اند؛ رقمی که تقریباً نصف میزان تردد در آخرهفتۀ قبل است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/657632" target="_blank">📅 14:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657631">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
بورس در چند قدمی قله؛ حقیقی‌ها خریدند، حقوقی‌ها فروختند!
🔹
امروز در بازار بورس، حقیقی‌ها ۷.۹ همت پول وارد بازار کردند و ارزش معاملات خرد حدود ۱۶ همت ثبت شد. در سمت فروش، ۶۷ درصد توسط حقوقی‌ها انجام شده، در حالی که حقیقی‌ها فقط ۳۳ درصد فروشنده بودند.
🔹
شاخص کل با جهشی خیره‌کننده‌ ۱۱۴ هزار واحدی به ارتفاع ۴,۵۴۰,۸۷۴ صعود کرد. یعنی چند قدمی قله تاریخ! مهم‌تر از همه، ۹۵ درصد نمادها مثبت بسته شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/657631" target="_blank">📅 14:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657630">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd4f1e481.mp4?token=bL6ebIrcv8FvHNw6GlBe1F0TSZAT0UFt0eeD4zJnrGCnAm6xBEKWnnvnHAKbsv1nj0j7LZeZrieDyu1Aik-hyAWpCkBBDDMXpkR1C55VwGwE0ddO2XlnJQRQol6_6M-NBsiBJ77Za9sz2HUPSoYvo5Jcmh0B3nNgUmkl5AUiB6832Fpo_vDokCa52l9UVE98Q3btJ4KEg7YWlRDYrvaGvlvbaBFtm_ZflCDe3MxovfMoXKKS1mkmU3NeDEflE3ZxFAsLxXo9dulYAvsEGnKbqOWt6kn7zwK7sbTKnZFB8iyNSP6uRYJJf3vrt5ZrMyLKFnSJgT6gm1JqiOMV_nTFgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd4f1e481.mp4?token=bL6ebIrcv8FvHNw6GlBe1F0TSZAT0UFt0eeD4zJnrGCnAm6xBEKWnnvnHAKbsv1nj0j7LZeZrieDyu1Aik-hyAWpCkBBDDMXpkR1C55VwGwE0ddO2XlnJQRQol6_6M-NBsiBJ77Za9sz2HUPSoYvo5Jcmh0B3nNgUmkl5AUiB6832Fpo_vDokCa52l9UVE98Q3btJ4KEg7YWlRDYrvaGvlvbaBFtm_ZflCDe3MxovfMoXKKS1mkmU3NeDEflE3ZxFAsLxXo9dulYAvsEGnKbqOWt6kn7zwK7sbTKnZFB8iyNSP6uRYJJf3vrt5ZrMyLKFnSJgT6gm1JqiOMV_nTFgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک نظامی عالی‌رتبه ارتش روسیه در مسکو ترور شد
🔹
کمیته ارشد تحقیقاتی روسیه اعلام کرد که در نتیجه انفجار امروز راننده یک خودرو جراحات متعددی برداشته و در محل انفجار که حدود ساعت ۵:۳۰ صبح به وقت محلی رخ داد، جان خود را از دست داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/657630" target="_blank">📅 14:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTfvoSqiIzK_l6PbO3DOtTR4kuxG1CyEYHFbDFGZ-3sAH9dxNwAKxgZdHjobkVj6XjTzvvqezN8-utjbz2VBQHmnRqmhO68-1VWb3WTb7oX-QegR7trqFtTGJxRWtWwlxK0w-cNty64ivIzsVwYXntManegpa-u6HNOEclFew8yb0z8lxhhvDdJeBlHL-bQVRHgnaC2QUxjfuWwTBY2ecWv1nFJ4-SVoCkPjSBf8ZBi1vYF8i_myhwMq6a_Bh8AxtECrd2G27yL-BeQ3xxPBiKcWxRR32_TXABnzethgdB-3xjm0fj_3sZJfAJ1oqdlxXYvJuQn7uXP8blSoyjADVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از پوستر تیم ملی والیبال ایران در لیگ ملت‌های ۲۰۲۶
🔹
استادیوم ۱۲ هزار نفری آزادی در جریان جنگ رمضان مورد هدف موشک‌های رژیم صهیونسیتی و آمریکا قرار گرفت.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/657628" target="_blank">📅 14:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtQFXAObQ9lgbPMmP2EV2q8p9r5lsgIhGYStIothqouse_mp5XT3nPplSzYxQpY3Lb9mi2PMVSMLE7N2fU3wo8-H5O2X6bGsXaXgS8B0q6BWjwnouyc4DlYtO2z0sgOEj4z-mOL8Ck_KZsi_amzazdNgBO6WagMs1ivRetSgrfm-8YjHRcoJeNmB4rsAcjud3o_TDNXXPR9ZXUkJOUbdjdwvZFNQByJDRI6qJXLEf7zR-9udmjsT3DyXo4AYibEqK_4lremE2iG0_Y5zq7Hn9PFGUWhXmUKzh_0IyCWTM1-6m4NdghGGVyoq9jXuFU4EwHKdTZ7JWzWVhuPyuhmAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران برای تحقیر ترامپ، بازی ۱۹۷۹ را آغاز کرد!
سایت تحلیلی Conversation:
🔹
ایران بحران گروگانگیری ۱۹۷۹ را کش داد تا آمریکا را تحقیر کند. ایران نقش کلیدی در شکست جیمی کارتر، از رونالد ریگان در انتخابات ریاست جمهوری ۱۹۸۰ ایالات متحده داشت. آنها ۵۲ گروگان باقی مانده را تنها چند دقیقه پس از مراسم تحلیف ریگان در ژانویه ۱۹۸۱ آزاد کرد.
🔹
بن‌بست فعلی با ایران تنها ۱۰۰ روز قدمت دارد و به نظر می‌رسد ایران اکنون آماده است تا از استراتژی مشابهی برای تنبیه ترامپ و نتانیاهو به خاطر حمله به ایران استفاده کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/657626" target="_blank">📅 14:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657624">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5fb5c1a7.mp4?token=O9Ir__wIKmPs4eAfhtRQ5zgfdJFWNjQ1zyQSeLBEQiORYRDG6KPpp0ejAv_AcpnKeZppiBs5E7ivyRuWt97a81ZCbKowHj6fNU_aN08xj94hXaCA9g2w8DdEQRE3SmEL7x2ziiorjFK_J7YMv6l1XyvBjLUk1K6k1IiZjQqPCgWvg7XDcjcRZ_M-rWZvBR5BwEMJMcZH_fpVhMn5-slbEcqsdiJa317yXPePwfrjReX_TyhimjTr9t-9uWfXj0tDF3DTGBO2izUKN6igcQoznPr49SasqHwZhGJrUnRILGLBdUgt5ryURO1DxTHYUIOjJd9SOXhgypZm3vod5A9AvasuJHBamvv65rJ51sDjqwK5V9gMI_U97iQkiaEdYSRdBI92__o8NQlNHvi6TXecOy1Hu1y4dq5TXMs2CyR6JFw75bB9Z0SoXy4ccwkK6hrC09lKEbc-6FSBdjeIYjnIC10ffuG7GKt29p7J3mUeaztk7YYt8P0u1rYFvPXTmO2xqg9jvLDc61L6khdnb-5OS6VUJ1iUw68Q4L62qzOlMzsm3Ss9JRoTYkBWnnPqiEE82tDa512o9BvlkJ41PWKz-NDDab5PY7WoPx2rYM1HF0KlShT4WPBsVqBuLFDs0eXbLRjY3T6jkKRfuZGnio8z7M8JmQB5AnjJIx4uJiPRp9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5fb5c1a7.mp4?token=O9Ir__wIKmPs4eAfhtRQ5zgfdJFWNjQ1zyQSeLBEQiORYRDG6KPpp0ejAv_AcpnKeZppiBs5E7ivyRuWt97a81ZCbKowHj6fNU_aN08xj94hXaCA9g2w8DdEQRE3SmEL7x2ziiorjFK_J7YMv6l1XyvBjLUk1K6k1IiZjQqPCgWvg7XDcjcRZ_M-rWZvBR5BwEMJMcZH_fpVhMn5-slbEcqsdiJa317yXPePwfrjReX_TyhimjTr9t-9uWfXj0tDF3DTGBO2izUKN6igcQoznPr49SasqHwZhGJrUnRILGLBdUgt5ryURO1DxTHYUIOjJd9SOXhgypZm3vod5A9AvasuJHBamvv65rJ51sDjqwK5V9gMI_U97iQkiaEdYSRdBI92__o8NQlNHvi6TXecOy1Hu1y4dq5TXMs2CyR6JFw75bB9Z0SoXy4ccwkK6hrC09lKEbc-6FSBdjeIYjnIC10ffuG7GKt29p7J3mUeaztk7YYt8P0u1rYFvPXTmO2xqg9jvLDc61L6khdnb-5OS6VUJ1iUw68Q4L62qzOlMzsm3Ss9JRoTYkBWnnPqiEE82tDa512o9BvlkJ41PWKz-NDDab5PY7WoPx2rYM1HF0KlShT4WPBsVqBuLFDs0eXbLRjY3T6jkKRfuZGnio8z7M8JmQB5AnjJIx4uJiPRp9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احیا و حقیقت | قسمت سوم: سرمایه مردم
🔹
روایت محمد جامعی از حمله ناجوانمردانه دشمنان آمریکایی‌صهیونیستی به زیرساخت‌های غیرنظامی ایران اسلامی در شرکت فولاد خوزستان
🔹
در آن یک دقیقه، فقط آهن و فولاد نسوخت. رؤیاهای هزاران نفر زیر آوار دود و آتش ماند. پشت هر سهم، یک زندگی بود؛ پس‌اندازی که قطره‌قطره جمع شده بود، امیدی که سال‌ها برایش صبر کرده بودند، آینده‌ای که قرار بود امن‌تر باشد.
🔹
فولاد خوزستان تنها یک مجتمع صنعتی نبود؛ بخشی از سرمایه مردم بود. سرمایه کسانی که به ساختن ایمان داشتند و سهمی از آینده این سرزمین خریده بودند.
و آن سوی ماجرا، هزاران کارگر ایستاده بودند؛ مردان و زنانی که چرخ زندگی‌شان با چرخ تولید می‌چرخید. با هر شعله‌ای که زبانه می‌کشید، نگرانی برای نان، آینده و امنیت خانواده‌ها نیز بزرگ‌تر می‌شد.
🔹
«احیا و حقیقت» روایت خسارت یک کارخانه نیست؛ روایت مردمی است که دارایی، امید و معیشتشان در دل این مجموعه جریان داشت.
روایت این حقیقت که وقتی یک صنعت هدف قرار می‌گیرد، آسیب تنها به سازه‌ها و تجهیزات نمی‌رسد؛ بلکه به زندگی انسان‌ها گره می‌خورد.
#از_نو_تو_را_آباد_خواهم_کرد
!
📱
@khouzestan_steel_co</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/657624" target="_blank">📅 14:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657622">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6tXIBmZMVuMH5pOKULIscW78mgAUcQi1vzQ9o4gr2mzCJArfCrMm0Zq4DDk7A_DHORU7jC-TQo5oklW6J8XWGW8wQVDatj5r2D3t2YjlF5V9A_sp1gUk9V4Igq1nuRQ7XLEDdFOkC30fHAn8np0p2puLTCiphO6Lfe_GW3MA42u3hhjJQnPgA6IkfD8ihpEiVGIWIUoHYB5m1uc_FDM3djED9LVdgmSkCzHHnsNmNrZs0Or5AozvMiBcpKwwR0TRzBeKUu4AZcykmKtyXXKvIelaYDLUOhy0EHmZQOtf52jbH-OU8lleuoSYGForU-FTBupIXzU956qmI3qOxCMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران‌چک جدید ۱۰۰ هزار تومانی با تصویر مدرسه میناب
🔹
بعد از جنایات امریکا در مدرسه میناب و شهادت ۱۶۸ کودک دختر و پسر دانش‌آموز به همراه جمعی از معلمان، کارکنان مدرسه و والدین حاضر در محل، بانک مرکزی سری جدید ایران چک های ۱۰۰ هزار تومانی را با تصویر مدرسه میناب چاپ کرد.
🔹
این ایران‌چک‌ها به‌تدریج وارد شبکه بانکی و چرخه مبادلات پولی کشور می‌شود و از نظر ویژگی‌های امنیتی نیز مشابه نمونه های قبلی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/657622" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657621">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
تیزر قسمت دهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم زینب حیدریان که ماجرای زمان کودکی و زیر آب رفتن در زاینده‌رود و رفتن در مسیری با نور سبز و ورود به جنگلی با درختان پر از میوه که اجازه خوردن از آن میوه‌ها را نداشت را نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: زینب حیدریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/657621" target="_blank">📅 14:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2YH2aQErSo-6ya5aWgvE3L4NHAn6MIPSjI1BO10vX0uEvbXYVp7KW5RueTyizZcBIW0zvz8GKH5CIO9r1rLuoeRY0IsKXqKonDIWMvR8sxC95jpk3I0-ft4E1A6BcKTOxfUAAileP7wXFT-qM1LGaDhh13eZbRTnQYTKwcNYkKGsAMMYEfbjCndthdq5sNJ08iJUYwNKqivYCALcI09-gOAJ3s5Yi2ZLGZzGJXb_D06LDV-XIrIwejN7khpWmXG-BUWQ3R-Dc9lle7nvVRlcxkCOGaRPuSfdZVXbAYXz72ZDpeYsKalwufmhSBc7SC3cTE5ZEcCp_ydH3QXRqb3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط بالگرد نظامی آمریکا در نزدیکی تنگۀ هرمز
🔹
طبق گزارش نیویورک تایمز، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند./ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/657619" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657617">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIqpqE4fsWCdjypQHWWCfcRG9X-1WiQI3RGNNbdBOvbvfmGfozDAGOWgAiwKqlyzKVNyUfAhWWdEWPM_lDl39iiLWjHV6nxozQolnQk4wfrCkOn7paQocBTukmZvWzyl5omdm86W4HgsiPC65GCujuN96je3Ri8v0AWiRJ6Wn2RWYAHHvVw2jOCG3JFJtMUi0c_car1kPsAqzuV2njFVCBSfkPnNehZoOSygDtNYggno7ghp5gJXXRvJZHTOxpGfuu54XSOhlZj5Qbaj52AyymRTjmgouuAxDugIBdGK8iqCY3Tf1IY5xsBgTmFVo5aTPeoiH1h1fZg-8GK_D6TwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول مسابقات هفته اول مرحله گروهی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/657617" target="_blank">📅 13:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657615">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy6-ThwUF6iI1PUEQvgPx1GIZk1UAk2Zn6YLs55H7_ueo5E8_MemODN3TG_P_6gHmDUQcZI5QrhrfypkG4qbkrwBaQ6TGRIBrGY0O-HRezkbmMYLsMEHYoYykaT9sgx-QEYQpoyZEXfmGztbpqsCXpxVFkYo1UgZf5CYLBI3vwV9Ej43HW85LUy8NcDSr94326wOgVYcrUeF2CyghlqmrJIH0r2TimcFB-16nfJ2VmWYf9MD42Gdv9RmruVFAJZIxcGoNBvGH-2uquk1-oSBVan7Y1CuSM_gJl8rKlc8gzdT5mVuUGAx-FPrK2_lFzJGKYlGChAYv35hyhLf1aFdGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ بقائی به نخست‌وزیر آلبانی: برای شعور مردم خودتان احترام قائل باشید!
‌
🔹
آرام باشید آقای نخست‌وزیر! شما آغازگر این ماجرا بودید و باید پیامدهای آن را بپذیرید.
🔹
به شعور و درک مردم خود احترام بگذارید؛ آنها حقیقت را از دروغ تشخیص می‌دهند. اگر با اعتراض افکار عمومی مواجه هستید، برای فرار از پاسخگویی ایران را مقصر جلوه ندهید.
🔹
نخست وزیر آلبانی در پاسخ به واکنش بقایی به تظاهرات مردم آلبانی علیه داماد ترامپ گفته بود ایران حق ندارد از مردم آلبانی سخن بگوید و به ناحق تهران را پشت حملات سایبری علیه زیرساخت‌های آلبانی دانسته بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/657615" target="_blank">📅 13:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657614">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
پروازهای فرودگاه امام(ره) طبق برنامه انجام می‌شود
مدیر روابط عمومی فرودگاه امام خمینی(ره):
🔹
با صدور اطلاعیه هوانوردی توسط سازمان هواپیمایی کشور در شب گذشته پروازها در فرودگاه امام(ره) به حالت عادی بازگشت و طبق برنامه انجام می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/657614" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657613">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIMunG7UH--pLa51_AKBF99YfAL-AsxpMAFVCrkpvINsTxU2asC9E6y6gpH4QxmDme-zoS8YQRtP_V2VjLxnlVZVOzGM-l17WfxuueRss76860cOSxHk2Dd-Gq_HA_GNhNjQKMbTlGmXTAFTNlvlguL76XMhhn7VZQK4wnBoY0BX-7YnnDTr3yqaCghXZaoHy4DHxGOPjrhxMOFSxzp6v4GbEhgy4_HI1Qc49IEDjLE337RzHr0VKc7NQrGgz_vGe8FJT98XqNmYSDRnBJimyiun64zsimXrnE5oEfFiyCXv3RCQ5hc8EV4V4CMk309I-eIM_k7BITqJvS9-K-cdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبدالله گنجی: روایت منتشرشده دربارهٔ جراحت پای رهبر انقلاب غیر واقعی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657613" target="_blank">📅 13:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
پروازهای فرودگاه شهید هاشمی‌نژاد مشهد به روال عادی بازگشت
مدیر روابط عمومی فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد:
🔹
با فراهم شدن شرایط ایمن و انجام هماهنگی‌های لازم با نهادهای ذی‌ربط، محدودیت‌های پروازی رفع شده و فعالیت‌های هوانوردی در فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد طبق برنامه به روال عادی بازگشته است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/657609" target="_blank">📅 13:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
تصاویر اولیه از کشتی مورد هدف قرار گرفته
🔹
بر اساس اعلام اتحادیه ملوانان فوروارد هند، تعدادی از خدمه این کشتی را شهروندان هندی تشکیل می‌دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/657608" target="_blank">📅 12:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657607">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmOjuzZ1uMgtbBnuanDeZ1ljHZN3ApPbV16z1Ib1rMey4lXrRyzPUZOw4e0A6grvZ_cD5SIMiKs2HuJlT0N58mlbMHQC6_oQCkXy5mv8k6gIBaChFBrC7iEyDFr7WMOOuwC8Ub56lKMZdGfa9BHasxaYEG_3_hoAn59E_dq5tRE822afG0-SrRUAH2Mn6q7eRGzXhQlkhL22aQl-0LzRNnQc6FUsUFm7VZWPDOeSeI5FJw7axoG76ENJq8-0qw7qbGL1l6RTkLnIKHPVfkC4G3ukubR1xg4LFlNdfSdtX7_atU_I6MTZqOQuv8SbyNBt-tOsefLNCmiamRHHxV6MQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقیقت پشت اعداد؛ چگونه آمار و نقل‌قول‌های جعلی را شناسایی کنیم؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/657607" target="_blank">📅 12:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یوتیوب رفع فیلتر می‌شود
مصطفی پوردهقان، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
وزیر ارتباطات در کمیسیون قول دادند که فضا را به شرایط عادی برگردانند و بعد از رفع فیلتر واتساپ، رفع فیلتر یوتیوب هم در دستور کار بود. منتظر هستیم گزارش وزیر را در یکشنبه آینده داشته باشیم که به چه نحوی پیش می‌رود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/657606" target="_blank">📅 12:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm2noI5aoECLi4K8wv-EdiK2EmHtE4o6Ku_eH2h__5uUp5e5bEPyGd1VM7mEqAtuH7oc6eWST45EretFv_g_wOsu9A8xj-WDXshlTSdxL7tB1NPf6RejaIOdjADPWOKjWGO98f3DuViNx3lkP6QZeYqsZvLbU0ikc6CLUhu2tda92rugKBfCypThl9lX2B58xw1F5gmGjUp0jyLhrMbgIQsrpcgseV-fdy3sNysvFcqE1Cmiwgn3Tr--A7Q7PvxsivGiNKd50DeoKZqNK4tkBTBtbzmVVN3Ke4mwbRRgxYtBn4U37AJaYn42gvGJSG29sm_UWNncpD1eBKIUFJFwPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت دو تن از رزمندگان پدافند هوایی ارتش در دفاع از آسمان کشور
🔹
شهیدان والامقام «سید بهمن حسینی» و «علیرضا عبیری» از کارکنان نیروی پدافند هوایی ارتش، در جریان مأموریت دفاع از مرزهای هوایی ایران و مقابله با تجاوز رژیم صهیونیستی دیروز به فیض شهادت رسیدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/657605" target="_blank">📅 12:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsdGNJ58JzRT7NLeTSVzJJo3tq61Rx1C-VGJEmJG4W7pqNZLP9jQb5z4Q7mj4elap0r4L--eW9GzmU4UG6U4lHyGYz1Kq4FwYGnVoYZ4Gf6GSbq4P74r5XtouSaH8dRe7TqwudxaJaEum_VHSlekP90mG9z0BrmAYOhIpj596WMx5pCy-lfkSntndxNa8vH4Wtbq_9dQOrO_mLkLh2QaOJyPiStfQzUxo06rMjKGOI3bOOfOY0rLMLzGrmOI5HGojnarypgtS1J3b5mJ-GUzlIISrzXiSM7CUYY-inQHHlyh4HFESDtxMI3gH-0rPOA47vEugCzBavRry1vV9A-d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس با جهش سه‌رقمی ۴.۵ میلیونی شد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۱۵ هزار واحدی به ۴ میلیون و ۵۴۱ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/657604" target="_blank">📅 12:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a9998b2c.mp4?token=CJA85mnm3X4-UPEz2M7tVvx-WjGwPt2xVASCHjSGbyfxQP3tnI3SJbCchcMSRunIBaIr33ck2yxW1un1EHS3-rVWZrzGA_6VTbPLJc2lCCLoz8dH8AqeeWJdeMDtF47ghEYr_L7Nio8bbaIa_wI1zA7QoknRSL95j7crFVU47q5O-bVUyF-OYK3uqCDlfmxuPj2BsnK2Cwvg19MMIW4DD59BOr1QCiric4x5MscBJv2m6tUG1hYTUxUtdHLgIRuwOwH9SvPyHmr0V27uUaKSMaksfJy3Kh7hCqsvxbY5AOMJ_Rga-iTkIr6kRL_fTUNgbH_Of1ZlxLsdh3C0wefHxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a9998b2c.mp4?token=CJA85mnm3X4-UPEz2M7tVvx-WjGwPt2xVASCHjSGbyfxQP3tnI3SJbCchcMSRunIBaIr33ck2yxW1un1EHS3-rVWZrzGA_6VTbPLJc2lCCLoz8dH8AqeeWJdeMDtF47ghEYr_L7Nio8bbaIa_wI1zA7QoknRSL95j7crFVU47q5O-bVUyF-OYK3uqCDlfmxuPj2BsnK2Cwvg19MMIW4DD59BOr1QCiric4x5MscBJv2m6tUG1hYTUxUtdHLgIRuwOwH9SvPyHmr0V27uUaKSMaksfJy3Kh7hCqsvxbY5AOMJ_Rga-iTkIr6kRL_fTUNgbH_Of1ZlxLsdh3C0wefHxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی دیدنی تیم ملی نروژ برای جام‌جهانی به تقلید از وایکینگ‌ها
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/657603" target="_blank">📅 12:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657600">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsUMn0OYlrSUdVTUx1wFxO3gRcGO0onF6drcD4R7AysriQN_3Gtdor8trLEQ201Xiu9iAA6kQcyFTeNOCcNwXqZuHrAi1B9gnNRwYa4C4G4TytTnoElJ_ppC16Pcpu7Hphdn05G7d_iBRvGTPScc7JhzwDAtzAG3G7JcvkRe39pd5uJaI-rEoOpM4-gIASiE_WUWY_broLr1taaVTx3HRogA5F05oTRYwrogqD75t3gcOwpLXkGlp5VVEZn2BT8GKntE-cUuZoyhi7_bU4H4YQG_cKGlKwJRV-Lw-8pxykg857Zs79L3TVfrJR4GP7aUNzDQyb_J42jy_csPvBHUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازیکنان حاضر در جام جهانی ۲۰۲۶ با سابقه قهرمانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/657600" target="_blank">📅 12:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657598">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt6Eit1Nc4QwaACtSsEAR5vGF814x24z-PMvz3xEf5v8018AUOanVlOcMcThl4azwxiIVIfDeyQ_TNuWa8z9nYtLZvaoyIv5YXRu8xBIV0ws8A4Tc20rsLQvc6Jq5vQgz1zUpynyoDmNCw5r5rXf4_BjzXoxwLqVpEwAM_vob9Lsaw3mPZIPhnH-LMWFOp0TTn4kZlV6C2-XGpzrD5ozw-DN32e-byDG0loSgNFk37bmPu_vkAVRzCS6MwL-nFqMtAMD5qNeRyzyu5YBkxybLJB1CNqtoWRHpLbpwXjG7fXNTHTfZSbYsSa09DLDhBwlr7Mu3v2RP8CAarwGIzdZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ گیگ اینترنت هدیه بدون قرعه‌کشی منتظرته!
🎁
با پیش‌بینی بازی‌های جام جهانی در اپلیکیشن «همراه من»، ۵ گیگ اینترنت رایگان هدیه بگیر؛ به همین راحتی.
اما این فقط شروع بازیه…
با ادامه پیش‌بینی مسابقه‌ها می‌تونی شانس بردن میلیاردها جایزه هیجان‌انگیز دیگه رو هم داشته باشی.
🏆
زمین بازی در «همراه من» منتظر توئه!
⚽️
👇
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/657598" target="_blank">📅 12:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657596">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S02-06ulBGUSYAowcf9Q7xo4I2fiJGS8L02F0Rpj0j0DEkSdsHY1Ni4A1RuQca1rFJEw92QFg6xdZBXwDuVtZIA9ypfzwQ3bbml-4pydMvWJi1IcjQy-NI3HrFiDfGvVbCjgdPhFsVTEPGxgGEQvjE32y8Z131WJS9RrF1kpy44C0t3IPNUft0tum7YlNIfMhfIJDENm6FGSkkuCik0Jj1lhMJvLejxmzMr97mmun5KtuJd6Kq0ZH3Z4ZyMCkhcqgXyzn0r6ZB7NaIRLVYNwhZ3wA_FilUZmOZEeBQe4wlCW58GYSVEpTbrLpnqW7bfHtdwZIDFtfJHcM1kedLezGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلعه میران، گلستان
🇮🇷
#ایران_زیبا
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/657596" target="_blank">📅 11:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657594">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/757ddf32fc.mp4?token=ABiMFp6i5wgaNq7u0LvoKp5NnSAMkbdSZoq6RPtjotutqcLT3Rpjj-G5jAE8Kvw9nl4IuDzWNZmRGfaDmtHcrRtO4RiwupLZ5OlPs4CCmEx6bNPZgRFTUwejGvHcdzf9QjucCqUQIq1FAaup_Oqk9wWd2d_5bUta1rco-wgvQSZDmLneWS6Ivw8XnQY5fhdgYpnV_U_F0dHT4h9GYI20XdRIVs-_IndCZow59xEyKjZUQDVp5J3z5G8DEaDAeMJWjlgAMPuNNfezxPQuNg3AqmfHCgyqHd76WqzvzndXlHL5G9G7d0VYgdvBM4uBBmwh9OtPVJKJfQrK7A8-8x4AEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/757ddf32fc.mp4?token=ABiMFp6i5wgaNq7u0LvoKp5NnSAMkbdSZoq6RPtjotutqcLT3Rpjj-G5jAE8Kvw9nl4IuDzWNZmRGfaDmtHcrRtO4RiwupLZ5OlPs4CCmEx6bNPZgRFTUwejGvHcdzf9QjucCqUQIq1FAaup_Oqk9wWd2d_5bUta1rco-wgvQSZDmLneWS6Ivw8XnQY5fhdgYpnV_U_F0dHT4h9GYI20XdRIVs-_IndCZow59xEyKjZUQDVp5J3z5G8DEaDAeMJWjlgAMPuNNfezxPQuNg3AqmfHCgyqHd76WqzvzndXlHL5G9G7d0VYgdvBM4uBBmwh9OtPVJKJfQrK7A8-8x4AEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر ارتباطات: ترافیک استارلینک با اینترنت بین‌الملل در مرزها برابری می‌کرد
هاشمی:
🔹
ترافیک اینترنت بین‌الملل قبل از ۴ خرداد با ترافیکی که از مسیر استارلینک از شبکه‌های مرزی خارج می‌شد، برابری می‌کرد؛ این تهدید جدی برای امنیت نظام حکمرانی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/657594" target="_blank">📅 11:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657593">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG3_NsJCyyyOLCo3MuItN3jXbxqVvPyxKxY-RJLSEU2U2Zz8vWo6IZn1fdnuID7P3SI-_QA_u8dk1W2_cOmeE6tjkdUUohVY0KuM5tPOp_9XrLZFoq5N7WVvpL88-wt6SGrHmqJgC-4QKgy552INFLVFKR2qet28pOQIJXhLysk5_F-4-cvELBEudw8YnP4Q0rypaa7C4ZMm0Vdozfso34JjvzcXBh5Nbq3DDxzTaG7YQdD9sbYgkeOCyyKIBKYOJKblAZ-Uzw_x5PkPsXEPaxFG9ao5kufLHjw3VhLerDGsDDwU2sHkj5caemceNL69tWrmJeHZflOwWyYW8znCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: ترامپ ۳۷ بار از «نزدیکی توافق با ایران» سخن گفته است
سی‌ان‌ان:
🔹
دونالد ترامپ از آغاز تنش‌ها با ایران دست‌کم ۳۷ بار مدعی نزدیک بودن توافق شده، اما این اظهارات تاکنون به نتیجه ملموسی نرسیده است.
🔹
تحلیلگران می‌گویند تکرار این وعده‌ها به اعتبار دیپلماتیک او آسیب زده و موجب افزایش تردید ناظران شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/657593" target="_blank">📅 11:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657592">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
مراسم وداع و تشییع رهبر شهید انقلاب پس از دهه اول محرم برگزار می‌شود
ستاد بزرگداشت عروج رهبر شهید انقلاب:
🔹
زمان و جزئیات منتشرشده درباره مراسم وداع، تشییع و تدفین رهبر شهید انقلاب و شهدای خانواده ایشان در فضای رسانه‌ای معتبر نیست.
🔹
با توجه به ایام عزاداری محرم، این مراسم پس از دهه اول محرم و پس از هماهنگی نهایی دستگاه‌های مسئول برگزار خواهد شد و جزئیات آن متعاقباً اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/657592" target="_blank">📅 11:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657591">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyzhUi6maudcW6Kgj2axgA6DE87sH8w7aMCB_VrOCw6Jpaew4Bwz_cRFQGc0cAX6qCaMwLKE0HKir-bt3xNwPfeEx87veU1r74tlXJrcK6DRIval7HJs_pv4Zet5FR94EIE0Pcc6bCJZThFSI1QC1Vv2rk-YA-88rcypUimwf-oDE5wNw168apyd25ZlYoQEQwJNU_4HlVmlsahIFiFg3Mrv4A2cpzdJA8lhjPAMP06ZKMErL_NZp4W6VLYNrMWcDMFtkcvtVgtdfPRTsZenp9S-V07nH9CthItGSKolUxnsgMXjkHH5bSnecnnL3CbXX9IQLvJrAwrWlxehdnse8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ خطای وحشتناک در جام جهانی که فوتبال را فراتر از یک بازی کردند | از تکل‌های مرگبار تا جنجال‌های فراموش‌نشدنی
🔹
جام جهانی فوتبال فقط میدان نمایش مهارت نیست؛ بلکه صحنه‌ای است که در آن فشار روانی، غرور ملی و رقابت شدید می‌تواند منجر به برخوردهایی شود که گاهی از مرز ورزش فراتر می‌روند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3221244</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/657591" target="_blank">📅 11:20 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
