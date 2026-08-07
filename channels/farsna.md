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
<img src="https://cdn4.telesco.pe/file/pmDEUltDaIQ_A1uE3U3rxos1c1H-kkNCg9iG3Ec9EahRfP5VRzk0bhW030oVuz0m0ul86l1oR-FejW6sO8xa_o9ik7OTxXX1-CX5FCVGMhKCoM3LiOq5Fzsrhcj4jHBV2qrsyCJUfPeIP2Jc1dMrTYN_LwgNFL7lmCuJ-I6nbamWRjlKmJQXrxBICix6eJv01oWdCzt5xF9ovx07xd-2KI3G4qOUzcobEqS7FOhiEkPauk3tC49AuJQ3BB023V2ARWotVLqN3eEazz9M1SXTAq30ANPQSi0F0kC2vrSBw8qqSzfItVCfCG9fL1FC0NP-A4jynkRZ06jlInqjNNSiJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 06:54:02</div>
<hr>

<div class="tg-post" id="msg-454812">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX5G0jXv-hYoC-dEIKSKWnRVb2K44lwWa1IeADLwLznIkujDana7jfWEc8-GKuCK1TBxOS4n2pXG1kt-tkg19DB1iTTgcFnQfU_OX_kJpEHgDQqiO1Nvm0NxPxS5wxWDbiZLeuWkrBgGl0ArP62szVCPMxx1jxOOfruiCT7-dCViHGQFCzRu4wzJMTFXksxGyyIUAekyRnY6vxnqk8-bTQCUAVOcpwOfEwZkh4neiX7KQ_xqyN-wUb_4AolpjmgdD8mrVppEvvVHxPPpHHqPXvE4iRp6jUmUcjDnI1ZLfTkD1NL3vbnFzWh5ysD0-CmRWS2_a1u51f63njS0FULaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظارت سه سالۀ دولت آمریکا بر خالق چت‌جی‌پی‌تی
🔹
وزارت دادگستری آمریکا اعلام کرد اپن‌ای‌آی و شرکت استاتسیگ با توافقی حقوقی موافقت کرده‌اند که بر اساس آن، شیوه‌های استخدامی این دو شرکت به مدت سه سال تحت نظارت قرار می‌گیرد.
🔹
این توافق پس از ادعای مقام‌های آمریکایی دربار۸ محدود کردن فرصت‌های شغلی برای شهروندان این کشور و تسهیل مسیر اقامت دائم برخی کارکنان مهاجر انجام شد. هرچند دو شرکت تخلف را نپذیرفته‌اند، اما پذیرفته‌اند در مجموع ۳.۲ میلیون دلار پرداخت کنند که شامل جریمه و جبران خسارت احتمالی است.
🔹
طبق این توافق، اپن‌ای‌آی و استاتسیگ باید سیاست‌های استخدامی خود را اصلاح کرده و گزارش‌های دوره‌ای دربارۀ روند جذب نیروی داخلی و خارجی به وزارت دادگستری ارائه دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/454812" target="_blank">📅 05:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454811">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e4d1033f.mp4?token=pFqF-0hmPgY7N8hyaE9JDBoHEFMBINntrwL82jcq2ix7ipki_jfoKoBJPBP-r5Ac5G1ZxeaxIwci44SYS2a9JGq2O2aXjDNOPzgu5_tnDw7jY5GPvqOupSSG6TmvLVjBRIyI4vb5XlnKta_wGiXWeW6n0h0_MDsBpvXwX7FXqZehCgW7x4bV5QdBdQts6P5cfI3PVGo8mTZYlu6TUIjZdzxKvikBYdrEnlpqEf9jTqpa1OfTdFQYpy7NbgHbNUwyhfffgJ2wwEnJM38neWqaNU1lrPE9WU92Y2ZMPAUSoAPKZluHensc7tT4lhkvDAZiACEMTMeA6CwxgWsxSv2J6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e4d1033f.mp4?token=pFqF-0hmPgY7N8hyaE9JDBoHEFMBINntrwL82jcq2ix7ipki_jfoKoBJPBP-r5Ac5G1ZxeaxIwci44SYS2a9JGq2O2aXjDNOPzgu5_tnDw7jY5GPvqOupSSG6TmvLVjBRIyI4vb5XlnKta_wGiXWeW6n0h0_MDsBpvXwX7FXqZehCgW7x4bV5QdBdQts6P5cfI3PVGo8mTZYlu6TUIjZdzxKvikBYdrEnlpqEf9jTqpa1OfTdFQYpy7NbgHbNUwyhfffgJ2wwEnJM38neWqaNU1lrPE9WU92Y2ZMPAUSoAPKZluHensc7tT4lhkvDAZiACEMTMeA6CwxgWsxSv2J6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانواده مستحکم می‌خواهی با همسرت مؤدب صحبت کن
🎙
آیت‌الله جاودان
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/454811" target="_blank">📅 04:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454810">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دستور ترامپ برای تحقیق دربارۀ عاملان افشای کمبود ذخایر تسلیحاتی آمریکا
🔹
روزنامۀ وال‌استریت‌ژورنال به نقل از منابع آگاه گزارش داد ترامپ دستور انجام تحقیقاتی دربارۀ افشای اطلاعات مربوط به ذخایر تسلیحاتی آمریکا را صادر کرده است.
🔹
در روزهای گذشته رسانه‌های آمریکا گزارش‌های متعددی دربارۀ کاهش ذخایر موشک‌های رهگیر این کشور منتشر کرده‌اند.
🔸
پیش از آغاز جنگ توسط ترامپ در پنج ماه پیش، رئیس ستاد مشترک ارتش آمریکا و دیگر مقامات ارشد به ترامپ اطلاع داده بودند که کارزار نظامی علیه ایران می‌تواند ذخایر موشک‌های پدافند هوایی و موشک‌های تهاجمی را به‌شدت کاهش دهد.
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/454810" target="_blank">📅 03:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454809">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ادعای سعودی‌ها درباره حملۀ انصارالله به نجران
🔹
ائتلاف عربستان سعودی مدعی شد بر اثر حملۀ انصارالله یمن به منطقه نجران ۱۱ غیرنظامی زخمی شده‌اند.
🔹
شبکۀ المسیره به نقل از یک منبع گزارش داد نیروهای مسلح یمن عملیاتی را علیه مراکز فرماندهی استقرارهای نظامی عربستان در مناطق الرویک، العبر و الثنیه انجام دادند.
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/454809" target="_blank">📅 03:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454808">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عربستان، ترکیه و پاکستان توافق دفاعی امضا می‌کنند
🔹
خبرگزاری رویترز به نقل از یک منبع آگاه گزارش داد که ترکیه، عربستان سعودی و پاکستان امروز در ریاض یک توافق مشترک دفاعی امضا خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454808" target="_blank">📅 02:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454807">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjRBR3brWBMMB-NRC2O72SJo8g45EQVcSfHpfqHXGePtCvFrZGd8G9NYli0WQNwBMgzmWlNBVfmO2YG6UAizzY3h-ThBe8zJ6RiZbfX34nckcBOYwA_Brl5c14Pt-JeWbRN3GgCOG0IUsx-ardzhxEDKVvOBvj11iJ39x5howsceaMdb_BpgEwsZhCgLg8g_lVh937eJSz0k5-Bgf7VXJlGrfKeWp3ELKABfctvWWuUH98TlBC5iUd4rwcE_LkjGqvTSk1JIxHK2cFd_vgA9QpTCtJVY3W5y1GyCc0y5RvFjsrn6hqMWrBrsHXeBm8iUxa4ij2BH3Zt2KsClRN7ADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رد پای موساد در بحران مهاجرتی اخیر اسپانیا
🔹
محافل اطلاعاتی و دانشگاهی چین گمانه‌زنی می‌کنند که اسرائیل بحران اخیر مهاجرت دسته‌جمعی در منطقهٔ خودمختار سئوتای اسپانیا را طراحی کرده است.
🔹
به گزارش روزنامهٔ ال موندو، در پکن گزارش‌هایی در دست است که بر اساس آن‌ها، هجوم مرزی یک عملیات حساب‌شدهٔ جنگ ترکیبی به رهبری موساد بوده که با همکاری مراکش برای بی‌ثبات‌سازی دولت اسپانیا اجرا شده است.
🔹
این ارزیابی راهبردی بحران مذکور را به طور مستقیم به تیره‌تر شدن روابط دیپلماتیک میان اسپانیا و اسرائیل مرتبط می‌داند.
🔹
اسپانیا به صراحت از نسل‌کشی اسرائیل در غزه انتقاد کرده و به صورت رسمی دولت فلسطین را به رسمیت شناخته است. این موضوع واکنش تند تل‌آویو را به همراه داشته.
🔹
«نادیا حلمی»، دانشمند علوم سیاسی اهل مصر و متخصص روابط چین و اسرائیل، گفت که تحلیلگران امنیتی پکن رویدادهای سئوتا را به‌عنوان یک کارزار فشار عمدی علیه دولت «پدرو سانچز»، نخست‌وزیر اسپانیا، ارزیابی می‌کنند.
🔹
نظریهٔ اطلاعاتی مطرح‌شده در پکن، در میان دیپلمات‌ها و تحلیلگران سیاسی نزدیک به نهادهای حکومتی چین به‌طور فعال مورد بحث است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454807" target="_blank">📅 01:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454806">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تهدید یمن به سرنگونی نظام حاکم بر عربستان
🔹
وزارت امور خارجۀ یمن به مسئولان عربستان سعودی هشدار داد که اگر به سیاست‌های استعماری خود ادامه دهند، باید منتظر نابودی نظام حاکم بر این کشور باشند.
🔹
یمن تأکید کرد عربستان با فعالیت‌های استعماری خود به سمت مسیر بی‌بازگشتی حرکت می‌کند که ممکن است صفحۀ تاریخ جنایتکارانۀ آن را ببندد.
🔹
این نهاد یمنی مجدد هشدار داد که میل به استعمار، فقط به نابودی رژیم سعودی منجر خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454806" target="_blank">📅 01:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454805">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a338c308bc.mp4?token=k9D0wFeNCL5bRbq4Yb9aF4mDA_ixWpPfghL8CTqcbX-C-zTs77_a60jf8h9MEdxm3pkkGADXJurXoE239hAYL87z4DRnyuLBSRWaHn0jMKWodJMiJS7rQDoEa-CP96wLPKv-OPBu02MzlEWCVY_NRIA3qRJb74ix7DLrJXHwvyYuVy-91lbOibkUtLOZLJkowTu7M6EF1TTH-rlOyTrlr5N6tiMJQeMPwiMK1JqBM_Q-yMuTVuutfDi6m-L5dzp3xfqRwDZ60qxTf_3bEqyoowglJw20aWdwrjrtFdBA0cp1vI7Qg8tAZZf6vb11MFgKty-MsopgWxekbC0UXDn0x3vP5gMO7S2GTdqBh08qK1Ci_o44BFeQwdMw3ZK-RvnHUOWIItytkuewJIlmpNexULUj_9UyvuSb0_xEVQC6Hgv7AGSu5cv4sUjJo2pbXxtGf6wtqfSw07aNDcuWxSB6TtSBhYGbeFovUaff_vvM0v1WrL0hl6UnFXwTKhA_g60Ki5jKsyO-UlhesCMn8ttLgRHF6B6gnzFSanq7j9KVwb9LhEphrozrK7o5lV8OjNqathOE5avgrVRv_U4OTKc-KvzJklVihKjoFqUYIbDpKjz09PZrpkcXAIJLsAfA9DIYtVer3T8TsuNHoaZhyyqXUkyURRrr4Xd9hUFv3QhcstU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a338c308bc.mp4?token=k9D0wFeNCL5bRbq4Yb9aF4mDA_ixWpPfghL8CTqcbX-C-zTs77_a60jf8h9MEdxm3pkkGADXJurXoE239hAYL87z4DRnyuLBSRWaHn0jMKWodJMiJS7rQDoEa-CP96wLPKv-OPBu02MzlEWCVY_NRIA3qRJb74ix7DLrJXHwvyYuVy-91lbOibkUtLOZLJkowTu7M6EF1TTH-rlOyTrlr5N6tiMJQeMPwiMK1JqBM_Q-yMuTVuutfDi6m-L5dzp3xfqRwDZ60qxTf_3bEqyoowglJw20aWdwrjrtFdBA0cp1vI7Qg8tAZZf6vb11MFgKty-MsopgWxekbC0UXDn0x3vP5gMO7S2GTdqBh08qK1Ci_o44BFeQwdMw3ZK-RvnHUOWIItytkuewJIlmpNexULUj_9UyvuSb0_xEVQC6Hgv7AGSu5cv4sUjJo2pbXxtGf6wtqfSw07aNDcuWxSB6TtSBhYGbeFovUaff_vvM0v1WrL0hl6UnFXwTKhA_g60Ki5jKsyO-UlhesCMn8ttLgRHF6B6gnzFSanq7j9KVwb9LhEphrozrK7o5lV8OjNqathOE5avgrVRv_U4OTKc-KvzJklVihKjoFqUYIbDpKjz09PZrpkcXAIJLsAfA9DIYtVer3T8TsuNHoaZhyyqXUkyURRrr4Xd9hUFv3QhcstU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرۀ شنیدنی سردار شهید ایزدی (حاج رمضان) از حاج قاسم
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454805" target="_blank">📅 01:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454804">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254b28154f.mp4?token=tOAwFqJE3TKUXIZ0gaPDUPLEG8oUZZN6rmI7wKt7IgW7OY3kw7ETy4hzq7HUQw8T3gLbNbBUE3ID742lJoz9ifeC8_da5nOwm5EkFAtbg9g_Tcaj4CXeG3d6jfa-O0HZ1nFSdvVFJ1rHgccG-DjIE2AKMQDRmdeDyUso1kzdvlIOou_fQZy2EsrFubLeOoHC_isQp8g4MaRzoSbULg1Vex-28nWvb07M4zuYldwG-x9V88YBH7rrOIbvYwfPzZY-XlwyH4hAc_6_-8dCAXHu8_V9lsNLa6arH-5KrSEkEsZYn_kUUYJgqqd1OT-pb76_sbVTuSLjfaf9vcOpUOM6_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254b28154f.mp4?token=tOAwFqJE3TKUXIZ0gaPDUPLEG8oUZZN6rmI7wKt7IgW7OY3kw7ETy4hzq7HUQw8T3gLbNbBUE3ID742lJoz9ifeC8_da5nOwm5EkFAtbg9g_Tcaj4CXeG3d6jfa-O0HZ1nFSdvVFJ1rHgccG-DjIE2AKMQDRmdeDyUso1kzdvlIOou_fQZy2EsrFubLeOoHC_isQp8g4MaRzoSbULg1Vex-28nWvb07M4zuYldwG-x9V88YBH7rrOIbvYwfPzZY-XlwyH4hAc_6_-8dCAXHu8_V9lsNLa6arH-5KrSEkEsZYn_kUUYJgqqd1OT-pb76_sbVTuSLjfaf9vcOpUOM6_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید حاج قاسم سلیمانی: ما در زندگی خودمان باید به الگوهای بزرگ نگاه کنیم؛ عمر ما می‌گذرد، تمام می‌شود، همه می‌میریم؛ اما انتخاب راه درست خیلی مهم است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454804" target="_blank">📅 01:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454803">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترفند سادۀ هکرها، غول‌های مالی آمریکا را غافلگیر کرد
🔹
گزارش جدید پژوهشگران امنیتی گوگل نشان می‌دهد گروهی از هکرها موفق شده‌اند به چندین شرکت بزرگ مالی و سرمایه‌گذاری در آمریکا نفوذ کنند و پس از سرقت اطلاعات حساس، قربانیان را با تهدید به انتشار عمومی داده‌ها تحت فشار قرار دهند.
🔹
به گفتۀ محققان، هدف اصلی این حملات دستیابی به اطلاعات محرمانه و سپس اخاذی از شرکت‌ها در ازای عدم افشای آن‌ها بوده است.
🔸
هکرها با تماس تلفنی با تلفن‌همراه شخصی کارکنان و جازدن خود به‌عنوان همکار یا کارشناس فناوری اطلاعات آن‌ها را فریب داده‌اند تا اطلاعات ورود و کدهای احراز هویت چندمرحله‌ای خود را در وب‌سایت‌های جعلی وارد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454803" target="_blank">📅 01:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454802">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بمباران غزه توسط رژیم صهیونیستی
🔹
المیادین: توپخانه اسرائیل شمال شرق شهر غزه را بمباران کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454802" target="_blank">📅 00:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454801">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoQdak9GynG0lI93PbxfTJRzhpd0Vn3zy70OG3FqOJQB0Jf_Dv0uPByDHMuCUmIcdzh3PrZYWP6teARZHebtCL1QhpkOrMJdyKi_jrnMxtBvZPrKOEQwDwGd2S5043S9HkvjbsAnq7bGHZ8Q-LLtnpPetLvJd2qkk7zBKw7RG8Rr8T9SFKZ42j_lKKh3ud5H2mrBS9wYXCPdzxCZy1uaNk2L5peZZdyrEkuBVUxZAds-CQMR8N2fk7TAxzL7i_vXIRASYqnQlxrie_0w5UVWlJcXUhjRtbdMhCkKcU_-IoPVAdS6vcQy68GvP_H76eYrhO1JvYBlrKd8rIqhrODp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف بی‌سابقۀ صادرات نفت عربستان به آمریکا
🔹
در ماه جولای سال جاری صادرات نفت عربستان به آمریکا به صفر رسید؛ اتفاقی که در ۴۰ سال گذشته بی‌سابقه بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454801" target="_blank">📅 00:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454800">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: ایرانی‌ها علی‌رغم محاصرۀ دریایی آمریکا، قادر به کاشت مین در تنگۀ هرمز هستند
🔹
رئیس‌جمهور تروریست آمریکا مدعی شد که جنگ با ایران به زودی به اتمام می‌رسد.
🔹
او گفت هیچ‌کس نمی‌خواهد کشتی چند میلیارد دلاری‌اش را به خطر بیندازد و در تنگۀ هرمز به مین برخورد کند.
🔹
ترامپ بار دیگر با اظهاراتی متناقض گفت کنترل تنگۀ هرمز دست آمریکا است، اما اندکی بعدتر مدعی شد توافق بر سر بازگشایی تنگۀ هرمز به‌زودی حاصل خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454800" target="_blank">📅 00:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454799">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ydtxjff2A8Jd9lrzYL4pk6FHa9uCoOSZjQHctcfLUD7IfHS5_Ynt3Qva_n__1XY_g8RvABbIU6l6Hp8xjOJcndic74WO2yopCMysL1mL3C3QuuZuiykVLV3JnAywVIuNGIUlmJe4Us3yULMVliIWllozHjjIdXwxsNXKR4Zi8YsUs7tCZsD0wf7TV1rh9dgdELiS5jRo3XZjKSdzkkVQpqwKECGTILDDnIBvy_dC5KoB_IKtT3YwS4dGT1sRvBnThIf5WTP2N_SUpfBqTjwcIJd-kkHdtL8YlAbJ6gZ0e7dcD-zeo-Y4aipOiCB-Jbnm4JVnQtafu4s0hJXHp1W5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل در دورۀ آتش‌بس غزه، ۳۰۰ کودک را به شهادت رساند
🔹
یونیسف اعلام کرد از زمان اعلام آتش‌بس در اکتبر ۲۰۲۵، حداقل ۳۰۰ کودک در نوار غزه به شهادت رسیده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454799" target="_blank">📅 00:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454798">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGc9RNdbZWFJfucrVMV7_CVOuCs8AJ1IZJHo2UmTL_-OINwWkkx4CR9uoJAzQUhRTrUcCWmtVAzLMu4ZhAi4Yb0a8niVW6X_O29QYjco7Zy9BKmmqnZJy0rX9L5twvegWSyvF9fAXln3754rFzaI-gSXtgy_nbQRzyYt01ygOQaesxsc38jA_pzUbk2dFtOVV7DpGzHLE_NUS2Aoo-Dnm-ydrINbY2ZEwn4yx5XCOo81CqUCfgxdXKxSvVZ2xOT_dUDdPiNjW6-6Q7YUC_fEZMqp1qWNLf1wniT1PLSWnMnhgpjNNCjcnVwGhxVqKOtmb1ANXv0b-oxpTtzpPYHIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویۀ ۱۰ کشور در دریافت هزینۀ‌ خدمات دریایی از کشتی‌ها
🔹
در هفته‌های اخیر، هم‌زمان با مطرح شدن ایده دریافت هزینه از کشتی‌های عبوری از تنگه هرمز در ازای ارائه خدمات ایمنی، مدیریت ترافیک دریایی و راهنمایی ناوبری، برخی دولت‌های غربی و شماری از رسانه‌های بین‌المللی این اقدام را مغایر با حقوق بین‌الملل توصیف کرده‌اند.
🔹
با این حال، بررسی رویه‌های موجود در مهم‌ترین آبراه‌های جهان نشان می‌دهد که دریافت پول از کشتی‌های عبوری در ازای ارائه خدمات پدیده‌ای رایج و پذیرفته‌شده در بسیاری از کشورهاست.
🔹
گزارش اخیر روزنامه فایننشال تایمز نیز با استناد به تحلیل بانک JPMorgan تأکید می‌کند که اگر ایران و عمان دریافت هزینه را در قالب «هزینه خدمات ناوبری، ایمنی و مدیریت ترافیک دریایی» تعریف کنند، چنین سازوکاری می‌تواند از منظر حقوق بین‌الملل قابل دفاع باشد؛ الگویی که پیش‌تر در نقاط مختلف جهان نیز اجرا شده است.
🔗
مهم‌ترین نمونه‌های شناخته‌شده این رویه را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454798" target="_blank">📅 23:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454797">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a322b4c6ed.mp4?token=UcdLQgi0RD2nt8BrtzVMSwyTjNdwNd-2sSPQD2kp-fukBVZ9hTsk5hB3SO0TiiIGUNUKkWv7IMskgmAPC9_1YQGrVnm6ExNRQwybSx_Lv9MbfsvbeDS2aDN87mAIfp4wiOBZ3ZGrrMvdiFYi3tEmBfto61vUT6e3IAKVeTMCcpS0_Q_mK-Hl555uRqWFgwniKTgbjoc2Ow5esWOgZisls2_eIhTR0zWj-CksExeCTaEVWTse9RjFnL2tDjDqfVxL-n6JP4XZIhA2c4yvoVaFVPELmmgWS-D3VcS1b62aC6e51ZYP0UM3RYPPgomIHxeDRTDoBYJ19HOCkLA7eEN7yzpsUmmnSVH1S3jjJi34Ay7CU_jjUS2-5RufiICxfub49GRWTmLZ6KYKxMDBEDGH_u-rTo1_lpbMYNjFg3ieQRZpn4XOWBcervoHNggZkoN3ARRUs28CZf-8KmtiyPZhQS9sIhhnY2-e49nGMxL7tBZ9OhiHlt97a47_KLUtQYebHNLDu4UqViGcSf9yqhHRG1yRs2skSXxr9rU5wIl2aVXeoj8pJllnTiQI4bZC4fA_uxCKrwJFKq5tTa4bayieJzwa3el-2m_YF84FtowZcVEaE0XCJispy6iZhUgtp-XoTZ94vB1pE30KmykkUvNTrZxs7mhMVSBTvQsagFP8EUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a322b4c6ed.mp4?token=UcdLQgi0RD2nt8BrtzVMSwyTjNdwNd-2sSPQD2kp-fukBVZ9hTsk5hB3SO0TiiIGUNUKkWv7IMskgmAPC9_1YQGrVnm6ExNRQwybSx_Lv9MbfsvbeDS2aDN87mAIfp4wiOBZ3ZGrrMvdiFYi3tEmBfto61vUT6e3IAKVeTMCcpS0_Q_mK-Hl555uRqWFgwniKTgbjoc2Ow5esWOgZisls2_eIhTR0zWj-CksExeCTaEVWTse9RjFnL2tDjDqfVxL-n6JP4XZIhA2c4yvoVaFVPELmmgWS-D3VcS1b62aC6e51ZYP0UM3RYPPgomIHxeDRTDoBYJ19HOCkLA7eEN7yzpsUmmnSVH1S3jjJi34Ay7CU_jjUS2-5RufiICxfub49GRWTmLZ6KYKxMDBEDGH_u-rTo1_lpbMYNjFg3ieQRZpn4XOWBcervoHNggZkoN3ARRUs28CZf-8KmtiyPZhQS9sIhhnY2-e49nGMxL7tBZ9OhiHlt97a47_KLUtQYebHNLDu4UqViGcSf9yqhHRG1yRs2skSXxr9rU5wIl2aVXeoj8pJllnTiQI4bZC4fA_uxCKrwJFKq5tTa4bayieJzwa3el-2m_YF84FtowZcVEaE0XCJispy6iZhUgtp-XoTZ94vB1pE30KmykkUvNTrZxs7mhMVSBTvQsagFP8EUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش پزشکیان به اقدام مادر کردستانی که پول دیه دخترش را خرج مدرسه‌سازی کرد
🔹
این که شما پول و سرمایه داشته باشی و ببخشی، یک موضوع معمولی است.
🔹
افرادی مثل این مادر عزیز وقتی که این عمل را انجام می‌دهند، در واقع همه چیزی که دارند را خرج می‌کنند و این مصداق…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454797" target="_blank">📅 22:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454796">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5e24131d.mp4?token=EopVjwEWli0atoJ134LNRBYI7_-LFPuf3yA2n5ww2P8v5PJGMxcz5iFcPKW3b6KlpYFmEPslwU0_NM2RwXU7MU0AD6aW4NjolpTVGUILUvT1AYwwccgxlFLFhqkZuuFxEYKp86ycHjoiI7JB5OpBBjSvT7F-iyqDAXKJxQ7LZPInpZTnASAqQxV262OYVS4Agc64XvGCtuBT5xAmvWViLQCBg6VFaIUXnX_r6KiiQATVDDUOb-gOWS0VxTA0rjkum3Kmg72RS448gZy0VimjmOWAEggRe7TCy5KMqy3J3-3HKgmcQ6t0OfYGcT-tTSiRdTueFooyCGduLcW-rH7fJzAIu5-xVBQX2bRCxmprBxi9GsZzVcWj3Slfbjg2M_L74wI3ivIaq_kN8BF0ec_7s9ant2kdGoXRuPtoccgTlq33podgiUj-OkloH3OxDnjLeOWdZxRrDGQFO65SkG44bqMIY7NRnzT4hM_WUF57RdrqIdA-JDfCsmFslMj0NWDHn5wPnF2qA8pIF__h2hlwjtb-Esa9z0joANc_IHHa139WFflDNM4iItC49JqOb2L_OfIMVfgbOkLGPQLSJgKsdp4cSWBKxEb7xFh6-pC_cyDbOmqCDkbJlWt45lzcAyBagVzMzzsDOqcYctW7PrAs7gp8DPwWHsvP4lKtU4HmMbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5e24131d.mp4?token=EopVjwEWli0atoJ134LNRBYI7_-LFPuf3yA2n5ww2P8v5PJGMxcz5iFcPKW3b6KlpYFmEPslwU0_NM2RwXU7MU0AD6aW4NjolpTVGUILUvT1AYwwccgxlFLFhqkZuuFxEYKp86ycHjoiI7JB5OpBBjSvT7F-iyqDAXKJxQ7LZPInpZTnASAqQxV262OYVS4Agc64XvGCtuBT5xAmvWViLQCBg6VFaIUXnX_r6KiiQATVDDUOb-gOWS0VxTA0rjkum3Kmg72RS448gZy0VimjmOWAEggRe7TCy5KMqy3J3-3HKgmcQ6t0OfYGcT-tTSiRdTueFooyCGduLcW-rH7fJzAIu5-xVBQX2bRCxmprBxi9GsZzVcWj3Slfbjg2M_L74wI3ivIaq_kN8BF0ec_7s9ant2kdGoXRuPtoccgTlq33podgiUj-OkloH3OxDnjLeOWdZxRrDGQFO65SkG44bqMIY7NRnzT4hM_WUF57RdrqIdA-JDfCsmFslMj0NWDHn5wPnF2qA8pIF__h2hlwjtb-Esa9z0joANc_IHHa139WFflDNM4iItC49JqOb2L_OfIMVfgbOkLGPQLSJgKsdp4cSWBKxEb7xFh6-pC_cyDbOmqCDkbJlWt45lzcAyBagVzMzzsDOqcYctW7PrAs7gp8DPwWHsvP4lKtU4HmMbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: بهترین روش آموزشی دنیا را باید مستقر کنیم
🔹
باید بهترین روش آموزشی موجود در دنیا را در کشورمان پیاده‌سازی کنیم.
🔹
باید هر روزمان بهتر از دیروزمان باشد، اگر این نگاه را در فرزندان خود ایجاد کنیم، قطعاً پیشرفت خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454796" target="_blank">📅 22:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454795">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12df7e45c8.mp4?token=i2xzPdg1wSoBI4mPi6WwAxYw_pmvticXVI1fPSZyzDZBhVha-ayfnG0rWuLIL2q4a_nKVkVkQbQ4QRqFetj-Kv4F1bsLURj4ffMgoLaHyCjTru5taJQI8wKSEoWell0dhs94G8hz4HccrNozr0Esa2jTCZLRgtLOXWkWIx466X7CaCCe_7nOLda7WyhssZU4RFVB5UQxpFduUmnTmX9Tw28btjjzhsd9WaLM2h2GxQQ5iyi44qBbWsqjiLfiFe4W6nNoyjBHENUGwamdJVPCUcV81e36pBW1Av9k8r1TchOjUnMOf_L36LamhhpdaHOhTZLxTntiUX6BnZ2RrmsTOWYQaUW6sh7k5YW8KKjCaY4KaV14Q8ziN7GeFyeRG24cVmNTQl0Hr-YLxZWbLaI5JOqfRiwGzkoBN-xMzdL-oixv_KwYif5TqnSxMWarrM0JW9fjHDaJDFy2T12q7H5q30WZoeYNfXj8Sc2AECCtigr_nk8K_FpbABqfxUYwqjpApSCIy3xvWftrDbiZ95gp7mSJ4xRSha-pRlzDbrt1UO2IQxGxBQSywX1vlWof69EuARUTDTg2MJjHqZtoz7I1avaeT-UEVrYyy2HK9xY4eIZTo21PHdtydOvwNWuY_g7GBAnGBF-6kq92cd5SfN6w2D8pgP8r9Xg6O_Wt3SX6GQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12df7e45c8.mp4?token=i2xzPdg1wSoBI4mPi6WwAxYw_pmvticXVI1fPSZyzDZBhVha-ayfnG0rWuLIL2q4a_nKVkVkQbQ4QRqFetj-Kv4F1bsLURj4ffMgoLaHyCjTru5taJQI8wKSEoWell0dhs94G8hz4HccrNozr0Esa2jTCZLRgtLOXWkWIx466X7CaCCe_7nOLda7WyhssZU4RFVB5UQxpFduUmnTmX9Tw28btjjzhsd9WaLM2h2GxQQ5iyi44qBbWsqjiLfiFe4W6nNoyjBHENUGwamdJVPCUcV81e36pBW1Av9k8r1TchOjUnMOf_L36LamhhpdaHOhTZLxTntiUX6BnZ2RrmsTOWYQaUW6sh7k5YW8KKjCaY4KaV14Q8ziN7GeFyeRG24cVmNTQl0Hr-YLxZWbLaI5JOqfRiwGzkoBN-xMzdL-oixv_KwYif5TqnSxMWarrM0JW9fjHDaJDFy2T12q7H5q30WZoeYNfXj8Sc2AECCtigr_nk8K_FpbABqfxUYwqjpApSCIy3xvWftrDbiZ95gp7mSJ4xRSha-pRlzDbrt1UO2IQxGxBQSywX1vlWof69EuARUTDTg2MJjHqZtoz7I1avaeT-UEVrYyy2HK9xY4eIZTo21PHdtydOvwNWuY_g7GBAnGBF-6kq92cd5SfN6w2D8pgP8r9Xg6O_Wt3SX6GQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور: آموزش‌وپرورش است که آیندۀ کشور را می‌سازد
🔹
بزرگ‌ترین سرمایه کشور آموزش‌وپرورش است؛ تنش‌ها و ناملایمات اجتماعی ناشی از مشکلات آموزشی در آموزش‌وپرورش است.  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454795" target="_blank">📅 22:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454794">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb3b83202.mp4?token=PJZhw_wNjylYg3O8Sq_2ZI1a68m8DMNUm2CE0ontj9XC0DFI_IO7KRqOGurMujs1vdS5IbdkNJLL4T1DIPxW1B0fx2t_nviSGWJLpj1BN41uVxod2I7n8hNNDO7FgSJYbeJ-5rfX1sbFUmIdqmLUW8FV_P_VMm-mem0lHmacSDRF4LSpZXYsOv_oLFEp3NOmpSBmrm5pxJkAE9s9LamfYsWUOeBk92W_dI2l9kXxUHSYKF37km1Ood1fHIWVv4NeipbPdzhxZ-gTDPCubi29FKmCgAD983osrnh9m60Lb7hFUueDQe1aAFXx02w_0vyVx9BCKogul05xsUiV7IEWiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb3b83202.mp4?token=PJZhw_wNjylYg3O8Sq_2ZI1a68m8DMNUm2CE0ontj9XC0DFI_IO7KRqOGurMujs1vdS5IbdkNJLL4T1DIPxW1B0fx2t_nviSGWJLpj1BN41uVxod2I7n8hNNDO7FgSJYbeJ-5rfX1sbFUmIdqmLUW8FV_P_VMm-mem0lHmacSDRF4LSpZXYsOv_oLFEp3NOmpSBmrm5pxJkAE9s9LamfYsWUOeBk92W_dI2l9kXxUHSYKF37km1Ood1fHIWVv4NeipbPdzhxZ-gTDPCubi29FKmCgAD983osrnh9m60Lb7hFUueDQe1aAFXx02w_0vyVx9BCKogul05xsUiV7IEWiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آموزش حق همۀ مردم است؛ نه فقط پول‌دارها
🔹
حاکمیت باید بستر آموزش مناسب برای همه مردم را فراهم کند.
🔹
اگر امروز جوان ما مشکل دارد؛ مقصر ماییم، نه جوان مملکت. ما نتوانسته‌ایم درست آموزش بدهیم و آن‌‌ها را توانمند کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454794" target="_blank">📅 22:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454793">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bad38317d.mp4?token=p2J44vu3q9Rq8RhFaMTOS4eD84yykrsqno6LRM7wmhVc92yyGStLW2Wb_dSbgXQ-1FZUvdd9kJfPgchTBHsN7YyRB5fgOdkZzihhYTVpFe8zAcudoqI-pXsXzpzZY1cDGIv5ejrqWzvAC-hNgNcPc68qsl_z18FsEw_Qnroq-O1tYx2KEg1i-KORXq_QeQPbXebud2YiO9lcBdsUDVkds-dj9KmoMbtforoIiwdBFtNCv-l9dvYVBZhAsDAF6CaD7jIgwetZz4JKRq-t8hxSf2W_q8l_JlGcZL-5F8H410ysyIFCgxWwh-YN2EpjMUm64WceDrZAz2CxWWPzW_s5KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bad38317d.mp4?token=p2J44vu3q9Rq8RhFaMTOS4eD84yykrsqno6LRM7wmhVc92yyGStLW2Wb_dSbgXQ-1FZUvdd9kJfPgchTBHsN7YyRB5fgOdkZzihhYTVpFe8zAcudoqI-pXsXzpzZY1cDGIv5ejrqWzvAC-hNgNcPc68qsl_z18FsEw_Qnroq-O1tYx2KEg1i-KORXq_QeQPbXebud2YiO9lcBdsUDVkds-dj9KmoMbtforoIiwdBFtNCv-l9dvYVBZhAsDAF6CaD7jIgwetZz4JKRq-t8hxSf2W_q8l_JlGcZL-5F8H410ysyIFCgxWwh-YN2EpjMUm64WceDrZAz2CxWWPzW_s5KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر امروز در جامعه مشکل داریم به این دلیل است که درست آموزش نداده‌ایم
🔹
اگر امروز فارغ‌التحصیلانی داریم که نمی‌توانند مشکلات را حل کنند، چون یاد گرفته‌اند که نمی‌شود مشکل را حل کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454793" target="_blank">📅 22:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454792">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fc0827b4.mp4?token=iAZDJGsVw2IOJdGK36ua_9n9KV-zGg3v9C8Lq67VlKGKi8_tjUhmV3gkiEoncACnocuD9JGwb990rP-L4QoUWqvey54gthUiUpfHo6DerpUR-mMqmI_IEL-ULE5NqvhGEoDD-ogoZTpufLmpX22-DyQygCBFNYqZo8--dpVkrLlMY9bjVPRVZUoxvg_Xdq6H8BYJ0JJaigIW5BKiQdIW8bR2ZECEEucOZIXuaOh23Mka4_ClbHqWc9AXrtIIUPCXCuJuBzigC2PMXs40NCmEXzs4shrIGt9HGsOZX21PSN6lbTY4Is5vkADqES3UfwkyqkLcf9rajxp0pwPJ5PIbFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fc0827b4.mp4?token=iAZDJGsVw2IOJdGK36ua_9n9KV-zGg3v9C8Lq67VlKGKi8_tjUhmV3gkiEoncACnocuD9JGwb990rP-L4QoUWqvey54gthUiUpfHo6DerpUR-mMqmI_IEL-ULE5NqvhGEoDD-ogoZTpufLmpX22-DyQygCBFNYqZo8--dpVkrLlMY9bjVPRVZUoxvg_Xdq6H8BYJ0JJaigIW5BKiQdIW8bR2ZECEEucOZIXuaOh23Mka4_ClbHqWc9AXrtIIUPCXCuJuBzigC2PMXs40NCmEXzs4shrIGt9HGsOZX21PSN6lbTY4Is5vkADqES3UfwkyqkLcf9rajxp0pwPJ5PIbFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: واگذاری اختیارات به استانداران باعث شد در جنگ کمبودی نداشته باشیم  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454792" target="_blank">📅 22:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454791">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98628bd77.mp4?token=C6-_D5EOG3cVOLbqdMCaY55LmNN2w6g5PhfDdTpXCk__fiKSFkMVKmchQt0Zm3VyrYfByo3bCwaTjBWlngyiGGpM5-b3B-2LzX438XavFBzLeWV87aHELDsKRhzgk7Zi4a3-zH9PlFKdxWvPd2BSmo9NCAqyEJFUm3_UH4dBrGYOI3WL-mB_zi5R1MtLspNHcjTDn71ev00s0e0_CbPVKARC-d0em89CPiteO1Lpgm_Ls0x8wC6IEarrLmFk2b7L4FVaBX9dYL_EXYCDrXxdSVl28QmizYQo9LmcXkjp6sqPP3j29zglQH4RsRZWvbTX6n6cG5C2CdN0-muKR5SMQBKPJs8tLSycmnJSryNv324xArnq3eRWOEk_vApWt1OhLlwQOZfT50SWF9YM7SFK7hxVjpkZQ0oemUddz3cHXbgGCCQijfM77HDhx0XRQ4cxnv3AseHwnPPezsNlSVX8MAHWPOCyye8uEV8mEZ57MY-Pv1H_77PNMFUNsauchhvhE3SUAZ4OGgO13E0BZx8fISwB6vimrWeirq02A4-nkpsDiv3YL3KgvPNjE_1Yxadnwiv5Ncu7vCHtFVMDJNZzyOLJGDi96k1ipOT5uI3yLc3LZlft4isU35asLO8nE8-d17550bGXm7St4tQKr4efn4YEjtwFwdpqSDyo-Ri-cNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98628bd77.mp4?token=C6-_D5EOG3cVOLbqdMCaY55LmNN2w6g5PhfDdTpXCk__fiKSFkMVKmchQt0Zm3VyrYfByo3bCwaTjBWlngyiGGpM5-b3B-2LzX438XavFBzLeWV87aHELDsKRhzgk7Zi4a3-zH9PlFKdxWvPd2BSmo9NCAqyEJFUm3_UH4dBrGYOI3WL-mB_zi5R1MtLspNHcjTDn71ev00s0e0_CbPVKARC-d0em89CPiteO1Lpgm_Ls0x8wC6IEarrLmFk2b7L4FVaBX9dYL_EXYCDrXxdSVl28QmizYQo9LmcXkjp6sqPP3j29zglQH4RsRZWvbTX6n6cG5C2CdN0-muKR5SMQBKPJs8tLSycmnJSryNv324xArnq3eRWOEk_vApWt1OhLlwQOZfT50SWF9YM7SFK7hxVjpkZQ0oemUddz3cHXbgGCCQijfM77HDhx0XRQ4cxnv3AseHwnPPezsNlSVX8MAHWPOCyye8uEV8mEZ57MY-Pv1H_77PNMFUNsauchhvhE3SUAZ4OGgO13E0BZx8fISwB6vimrWeirq02A4-nkpsDiv3YL3KgvPNjE_1Yxadnwiv5Ncu7vCHtFVMDJNZzyOLJGDi96k1ipOT5uI3yLc3LZlft4isU35asLO8nE8-d17550bGXm7St4tQKr4efn4YEjtwFwdpqSDyo-Ri-cNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اتصال شهرهای اطراف تهران به مترو در دستور کار است.
🔹
شریان‌های اطراف تهران مثل اسلامشهر، شهر قدس، رباط کریم و شهریار اگر به مترو متصل شوند حتماً زمان سفر و آلودگی هوا کاهش پیدا خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454791" target="_blank">📅 22:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454790">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
هیچ‌گونه اصابتی در قشم و بندرعباس گزارش نشده
🔹
معاون امنیتی استانداری هرمزگان،: تاکنون هیچ‌گونه اصابت یا حادثه‌ای در جزیرۀ قشم و شهر بندرعباس گزارش نشده است.
🔹
بررسی‌های لازم توسط دستگاه‌های مسئول برای شناسایی منشأ صدای شنیده‌شده درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454790" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454789">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/094247db5e.mp4?token=DIRmNJTn666MpkfprqlAcH50LdodJQuwbYvcPTIzzczAwUtQn0pvuMHkzMrWl68C67A0JNzvhv1s7MuGeL2H1reInj2ajXtCozbJ83hHqlsQmmzMfZAD-SVMVXo0QYJSn-2g2Hs5OWfPjC-XtnTMJdowFma7PysxoGABV_8j7UWhgboM0q_LO7img6ks99U8rswaF6keuUA43nkAsANPwJdf4qgAC8IodlzIpmJiBo09zS2XLRKMjlGR9ErGz2iSur_YElnHEil4Vc30BcEfyL84vvp5n5C2jEs-bds9qRre6QP_Uc7tutVokyHB9pCG13CT5Z1qX-tWYn7vekShUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/094247db5e.mp4?token=DIRmNJTn666MpkfprqlAcH50LdodJQuwbYvcPTIzzczAwUtQn0pvuMHkzMrWl68C67A0JNzvhv1s7MuGeL2H1reInj2ajXtCozbJ83hHqlsQmmzMfZAD-SVMVXo0QYJSn-2g2Hs5OWfPjC-XtnTMJdowFma7PysxoGABV_8j7UWhgboM0q_LO7img6ks99U8rswaF6keuUA43nkAsANPwJdf4qgAC8IodlzIpmJiBo09zS2XLRKMjlGR9ErGz2iSur_YElnHEil4Vc30BcEfyL84vvp5n5C2jEs-bds9qRre6QP_Uc7tutVokyHB9pCG13CT5Z1qX-tWYn7vekShUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور: راه‌آهن چابهار به زاهدان را باید در هفتۀ دولت افتتاح کنیم  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454789" target="_blank">📅 22:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454788">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cd37e203.mp4?token=iLM5wlbaITvchVClk2bvq3Vi8rOYyewb-mUpfTf5NSRub6-pz0Y-6BC5UdgoB3l9uArrE_eNfRPzg3f4XyQHCUW1FQ19bYnVu1On4K9zy-Ts2W913Fjko19pbOykOGFZa4QQHh9gwxwCjU8qHUKyodnchlMlPpnIr4b1JI40ohI16IJUJMGTj4iRTQZYpNGnfNO2fgvZgvg8XUZffFLyR1K_wYAIr12neBy9vOwkdgLJZCtdSqQT-zRD63q1vFu8AeeecSfY_JzwRLlzoaUiUbWMI1Lsc7zXM_YdJ_zuWWqXo5SZ_ZiR3PfY5CYAC9mvdpBHwiR-RN83P1U11RPg4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cd37e203.mp4?token=iLM5wlbaITvchVClk2bvq3Vi8rOYyewb-mUpfTf5NSRub6-pz0Y-6BC5UdgoB3l9uArrE_eNfRPzg3f4XyQHCUW1FQ19bYnVu1On4K9zy-Ts2W913Fjko19pbOykOGFZa4QQHh9gwxwCjU8qHUKyodnchlMlPpnIr4b1JI40ohI16IJUJMGTj4iRTQZYpNGnfNO2fgvZgvg8XUZffFLyR1K_wYAIr12neBy9vOwkdgLJZCtdSqQT-zRD63q1vFu8AeeecSfY_JzwRLlzoaUiUbWMI1Lsc7zXM_YdJ_zuWWqXo5SZ_ZiR3PfY5CYAC9mvdpBHwiR-RN83P1U11RPg4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: چرا به مدیران شرکت‌های زیان‌ده، فوق‌العادهِ مدیریت می‌دهیم؟!
🔹
کارخانه‌ها و شرکت‌های ما باید توسط بخش خصوصی هدایت شوند؛ امروز مدیر برای دولت ضرر ایجاد می‌کند و فوق‌العادهِ مدیریت هم می‌گیرد!
🔹
در یکی از کشورها یک کارخانه به اندازه پول یک کشور درآمد…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454788" target="_blank">📅 22:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454787">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce1574c0d9.mp4?token=pxLPap_JtanZrqBPCi2zo_n-F56WnaLDWtQuH_76ICm0hzZwwqbj0qdB3ltEheHpQcVF9Rj0sgJbGAja_BXN29fsA0LszgPL7bOr6pftAzTMpJJabU7DMipiAJwtnOdRQfbRjZRmJDVCfTLybIpmJkVeU-o8tGq8C6WH9V4_G9LdUlYXFPR5W8z-Wzv_lVjRozC6KuG1g2sNvd9kc-9mNLXorX9UHpmnGzqShCRSLFAzNgO5BFOBUhGyi9tCluoOZ0bjkhTrJopF-J7D8b9Jwu4fa30rUx-20VCWaP8HV0lXlPWC5tV_nhT5wUM87CNal1ysaTdTYiLaqlgbD25qIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce1574c0d9.mp4?token=pxLPap_JtanZrqBPCi2zo_n-F56WnaLDWtQuH_76ICm0hzZwwqbj0qdB3ltEheHpQcVF9Rj0sgJbGAja_BXN29fsA0LszgPL7bOr6pftAzTMpJJabU7DMipiAJwtnOdRQfbRjZRmJDVCfTLybIpmJkVeU-o8tGq8C6WH9V4_G9LdUlYXFPR5W8z-Wzv_lVjRozC6KuG1g2sNvd9kc-9mNLXorX9UHpmnGzqShCRSLFAzNgO5BFOBUhGyi9tCluoOZ0bjkhTrJopF-J7D8b9Jwu4fa30rUx-20VCWaP8HV0lXlPWC5tV_nhT5wUM87CNal1ysaTdTYiLaqlgbD25qIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: سایپا و چند شرکت دیگر هم مثل ایران‌خودرو واگذار خواهند شد
🔹
کارخانه ایران‌خودرو را که واگذار کردیم، وزیر اقتصاد دولت استیضاح شد!
🔹
وقتی اعلام می‌کنم که ما هر کاری می‌کنیم، یک مقاومتی بر علیه آن وجود دارد دقیقاً همین موضوع است.
🔹
شرکت‌های دیگری هم…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454787" target="_blank">📅 22:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454786">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/604f0bb294.mp4?token=ia6te56tzy5Bc5FCNlJG2xo8JfrzlW_7kk2s-lfvNvAd1FhgU4YoxN-LGB9FeeiMPwwGpzYxLiJAmiiXNoFTQVB0IQES2-vkwVNPffL9kcMBIv93lQ7-xfxSbnbavJa1-od6whVWgDIn8KbIecKS54JkAK8pEjA3nyx3byQvkzeA0X94Y9bC00pHnH4GugdDrof81c5ZSJPgpZGQW0W1gFQiW3QovDwFb9YKHGcAYZyQ4S59ZXHmJIaB1gKgEkH7NfOLV7hXJ3XDJ2zX2aEFeYCNJtbzTb4qQ40bKdhp2vMmkusKII75I0ka-FFAVUb8FNSNFg0U3fHVwZZcMrep0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/604f0bb294.mp4?token=ia6te56tzy5Bc5FCNlJG2xo8JfrzlW_7kk2s-lfvNvAd1FhgU4YoxN-LGB9FeeiMPwwGpzYxLiJAmiiXNoFTQVB0IQES2-vkwVNPffL9kcMBIv93lQ7-xfxSbnbavJa1-od6whVWgDIn8KbIecKS54JkAK8pEjA3nyx3byQvkzeA0X94Y9bC00pHnH4GugdDrof81c5ZSJPgpZGQW0W1gFQiW3QovDwFb9YKHGcAYZyQ4S59ZXHmJIaB1gKgEkH7NfOLV7hXJ3XDJ2zX2aEFeYCNJtbzTb4qQ40bKdhp2vMmkusKII75I0ka-FFAVUb8FNSNFg0U3fHVwZZcMrep0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر ارز ترجیحی را حذف نمی‌کردیم، قطعاً در زمان جنگ قحطی پیش می‌آمد
🔹
امروز برنامه داریم تا زمینه‌های فساد را از بین ببریم، این فساد می‌تواند رانت، رشوه یا قاچاق باشد.
🔹
تا زمانی که زمینه فساد وجود دارد؛ نمی‌شود جلوی فساد را گرفت. وقتی زمینه فساد…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454786" target="_blank">📅 22:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454785">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c89460b4.mp4?token=l7uFuu5SmZlqVeynoNdxMmuCa9hgJk8pLVZrT-mPbG5r0r_1m9ZadB11b_OHq3u4Jy7hj1ldV1cxTerCbSkhXNNB0m2-c99GXli73i8e9_w9KLvThbyliMmwpLO0FRL6omc7AD-4uqG3C6zeDLx3Yo4xb7tiCAzwYq_C3V3JUi2iNh1FpKg_W7OdMPQw5dP3CmPsLRru0V0PyCgwn6sNHMCUwaOVFiX0svN6SiaEGt8DClh8dfpu81ZvMhXPj1zQ3r2xJt7o0ITQsXkijItsJQO7mrBREhm5a3Wv2Y0ExvVLLWQURz0xBHwj3aSw7XaLSLOEsa-Sw3DoHK0ZxT2e6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c89460b4.mp4?token=l7uFuu5SmZlqVeynoNdxMmuCa9hgJk8pLVZrT-mPbG5r0r_1m9ZadB11b_OHq3u4Jy7hj1ldV1cxTerCbSkhXNNB0m2-c99GXli73i8e9_w9KLvThbyliMmwpLO0FRL6omc7AD-4uqG3C6zeDLx3Yo4xb7tiCAzwYq_C3V3JUi2iNh1FpKg_W7OdMPQw5dP3CmPsLRru0V0PyCgwn6sNHMCUwaOVFiX0svN6SiaEGt8DClh8dfpu81ZvMhXPj1zQ3r2xJt7o0ITQsXkijItsJQO7mrBREhm5a3Wv2Y0ExvVLLWQURz0xBHwj3aSw7XaLSLOEsa-Sw3DoHK0ZxT2e6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور: باید به‌سمتی برویم که یارانه‌های دهک‌های بالا کمتر و به دهک‌های پایین پرداخت شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454785" target="_blank">📅 22:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454784">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0398b26711.mp4?token=oLxGTo1a2xTOsDl8h2dcUpVWf_mDshZ3jLv0H1D0bnQGouh2g5LVr5cAj3Fa9qE1BikpFihi4dMY-CkqrztuZIyOeIRKCSkJA7KNdQ3i_Gard5QWPxCycpGM0FTngZYacLmrIDU3KlDysdnyu-cuivGw-eh3bhdQiTLttd7lf7tngvEanKIhrlVOGgknLw0a317nUTtE-EeTU4n08n4P16nncM1eAZ53lUNYFl7KbJzx6LHyqYvWqQJhjnvDDuizjujXBmuXlYNeFqO4gRb00NiUdb6nI7Um-3F99krMWcO-OWe0WZTqACaSMnxiDhTV72GA3NL_HNQkScrPlMw42g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0398b26711.mp4?token=oLxGTo1a2xTOsDl8h2dcUpVWf_mDshZ3jLv0H1D0bnQGouh2g5LVr5cAj3Fa9qE1BikpFihi4dMY-CkqrztuZIyOeIRKCSkJA7KNdQ3i_Gard5QWPxCycpGM0FTngZYacLmrIDU3KlDysdnyu-cuivGw-eh3bhdQiTLttd7lf7tngvEanKIhrlVOGgknLw0a317nUTtE-EeTU4n08n4P16nncM1eAZ53lUNYFl7KbJzx6LHyqYvWqQJhjnvDDuizjujXBmuXlYNeFqO4gRb00NiUdb6nI7Um-3F99krMWcO-OWe0WZTqACaSMnxiDhTV72GA3NL_HNQkScrPlMw42g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مبلغ کالابرگ افزایش می‌یابد  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/454784" target="_blank">📅 22:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454783">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2dcd5833.mp4?token=lZ2Y8rLdKYZfgUMplTnz4abLkbUBJLOfe_Bm1JsZMFuOqwRvmszmLWdkn4wmdZZL4Svt-C-S7p6xjRG8p6IX-qSgmXL7oOZmFogXbK040EGUHdA5qadyXuJ-OXimMOmRmEqxUIFxR8fgQ4frx9J6llZn7xC1IrWVac83dgyu8CfUWUV2-6kCK454l2eeWl9yHWXh6zvPxA5saZJSMa9P7KSk-fCvhK6F8KUwqZmreTtK4S8j5skUCEICpJPSmOD6qQVfH3QPj5KjDSg5JmKZH40aWOVNnvdqHMM8egpgfDy8mhvVDULYqWbsTimusG-2mxc_IvNe6-FMg_6ajZNy1x5sK1kT1PjgM0yrHQvq8dgRxL2TKcb6GvU55YAxfK3YBk4rwv3i6HkvaOdyEXtiIIX4VorUd3ZKcWOLX43RyRaWNtFqu54P4UCXdbeaOkwKutkygSTyUWLhg4Hu-hGDim2kozD_kfef2I4V6TJh-u1wFnX3qX4f4PvDh6I6YovthhZq6OjRpc3kCfhm3WgjNVfN3kOWw7f4DU9ng7spMlUZqEG3_-ob602_-oscjSEonVy-kTgpWEpsDFSW1a4IvXxmnR12QDMGPET_jSoSarz1rlnMI78607g6I3YaA9b5bzK1aOHU9tyfBD9bk16BkCXwYIAWXswCFt2TWEhLuDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2dcd5833.mp4?token=lZ2Y8rLdKYZfgUMplTnz4abLkbUBJLOfe_Bm1JsZMFuOqwRvmszmLWdkn4wmdZZL4Svt-C-S7p6xjRG8p6IX-qSgmXL7oOZmFogXbK040EGUHdA5qadyXuJ-OXimMOmRmEqxUIFxR8fgQ4frx9J6llZn7xC1IrWVac83dgyu8CfUWUV2-6kCK454l2eeWl9yHWXh6zvPxA5saZJSMa9P7KSk-fCvhK6F8KUwqZmreTtK4S8j5skUCEICpJPSmOD6qQVfH3QPj5KjDSg5JmKZH40aWOVNnvdqHMM8egpgfDy8mhvVDULYqWbsTimusG-2mxc_IvNe6-FMg_6ajZNy1x5sK1kT1PjgM0yrHQvq8dgRxL2TKcb6GvU55YAxfK3YBk4rwv3i6HkvaOdyEXtiIIX4VorUd3ZKcWOLX43RyRaWNtFqu54P4UCXdbeaOkwKutkygSTyUWLhg4Hu-hGDim2kozD_kfef2I4V6TJh-u1wFnX3qX4f4PvDh6I6YovthhZq6OjRpc3kCfhm3WgjNVfN3kOWw7f4DU9ng7spMlUZqEG3_-ob602_-oscjSEonVy-kTgpWEpsDFSW1a4IvXxmnR12QDMGPET_jSoSarz1rlnMI78607g6I3YaA9b5bzK1aOHU9tyfBD9bk16BkCXwYIAWXswCFt2TWEhLuDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس‌جمهور از انحلال بانک آینده
🔹
یکی از اصلی‌ترین روش‌های کنترل تورم؛ اصلاح نظام بانکی است.
🔹
امروز با کمک وزارت اقتصاد و بانک‌ها برنامه‌هایی برای کنترل تورم وجود دارد و روند اصلاح ادامه خواهد داشت.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454783" target="_blank">📅 22:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454782">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953ea341f0.mp4?token=G-y55_W29kW6pTPzr57_oMwjNtWucjPMl9WIAWxUrvZ8ww_0HWQDYfkV6dh9SAb8qniR0lEGc7BU6u1-Bt0olCEYudpUD-OfDs_CKxJmbvkY9wX7TQqT-_mkujsFvg6OjuHyCUpEUMuMiRz1fQ-LL3AkfbDNBNApoU5Q0kFZWFuEL7rHtO59qrmtE8_bP0fnVjgXpJLgSiOSGLo_MHGlaQgvbmw6IgNVLqsA00f-ADmQFs8N0en65ljGVYfFoh5_YqLTus9dszDKhlnonXuOthznxqY6uoUAv88-q_oEI7poUqbTpbi-hiEhJ9SCl52VXH0ydAyF1o2WF11u46M9yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953ea341f0.mp4?token=G-y55_W29kW6pTPzr57_oMwjNtWucjPMl9WIAWxUrvZ8ww_0HWQDYfkV6dh9SAb8qniR0lEGc7BU6u1-Bt0olCEYudpUD-OfDs_CKxJmbvkY9wX7TQqT-_mkujsFvg6OjuHyCUpEUMuMiRz1fQ-LL3AkfbDNBNApoU5Q0kFZWFuEL7rHtO59qrmtE8_bP0fnVjgXpJLgSiOSGLo_MHGlaQgvbmw6IgNVLqsA00f-ADmQFs8N0en65ljGVYfFoh5_YqLTus9dszDKhlnonXuOthznxqY6uoUAv88-q_oEI7poUqbTpbi-hiEhJ9SCl52VXH0ydAyF1o2WF11u46M9yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کشورهای همسایه اجازه ندادند ضدانقلاب وارد کشور شوند
🔹
پس از اعمال محاصره، راه‌های تجاری با همسایگان را ایجاد کرده و گسترش داده‌ایم.
🔹
امروز ارتباط با همسایگان بسیار بهتر از گذشته است؛ همسایگان اجازه ندادند عناصر ضدانقلاب وارد کشور شوند.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454782" target="_blank">📅 22:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454781">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfd43cd35.mp4?token=Kmw5KpbjZI7NU4JqzdAJuUW0lieUbymz_Y26JvQqN2YxFgBgWk7jTgOg8l7CZiVY3Sd7jEZU1I7HCmTgrar4EvL-fBCwvn8vLoiLKVJBiXl3nrKyayGqBwwTPxvRbpcjSAjRYR8ulnzRd0oJ3cTT34pEKkkbnz4OH0zHxu90BNbNM6lLJIuO_-apSc1THTRY6TIEqeh56MccximMr-QPcUVCBABoch6LILoMZ3q0HcjFgCj9XaAFY3yRQIByhoWdwd7HOVg7sJ3HCexNwUa9hBGIWMelb312vbix1K-r_i_2GGWmpL9FyBTYGyMmuyk5-_2f3CImK_TEpfzLVk5dx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfd43cd35.mp4?token=Kmw5KpbjZI7NU4JqzdAJuUW0lieUbymz_Y26JvQqN2YxFgBgWk7jTgOg8l7CZiVY3Sd7jEZU1I7HCmTgrar4EvL-fBCwvn8vLoiLKVJBiXl3nrKyayGqBwwTPxvRbpcjSAjRYR8ulnzRd0oJ3cTT34pEKkkbnz4OH0zHxu90BNbNM6lLJIuO_-apSc1THTRY6TIEqeh56MccximMr-QPcUVCBABoch6LILoMZ3q0HcjFgCj9XaAFY3yRQIByhoWdwd7HOVg7sJ3HCexNwUa9hBGIWMelb312vbix1K-r_i_2GGWmpL9FyBTYGyMmuyk5-_2f3CImK_TEpfzLVk5dx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: فشار خارجی در دولت چهاردهم به بیشترین حد خود رسیده
🔹
دشمن به‌دلیل فشارهایی که آورد و تحریم‌هایی که به‌کار بست، انتظار داشت کشور سقوط کند.
🔹
فشار خارجی به کشور در همه دولت‌ها بوده اما در دولت چهاردهم این فشار به حداکثر خودش رسیده است.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/454781" target="_blank">📅 22:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454780">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3255ac29a1.mp4?token=aadi9OykUIjhLSlm1w1zLCydaUhHA3zhMvAYrKaZo6tyLSS9VY2tqrU7SXzWZFykGFXjfODGzVx70nGpXPYccciiEDowyqEjaUYU2lBBEwbpBvYZAmoVKvS1oj4P61SCEzpvDCpTcIMuy-fVOdmQdAO_Q2RLtPMhAou8SFbM2vCK0zjaTTQi-pfmNAPKW0iZ9_rRN0Zjp7pzEWvlbByUu4BzdcYpoVzLTD2jt_aD3RRfQXkDHGL1rL8zk-9g8g7KMihgQwQqMebvIcJZjtlofpTNdLmetSrvm35JV6IlrK1k_EMGm550nbTNbPSjBn86cNJ_2g2kx2TCy6tfES1nNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3255ac29a1.mp4?token=aadi9OykUIjhLSlm1w1zLCydaUhHA3zhMvAYrKaZo6tyLSS9VY2tqrU7SXzWZFykGFXjfODGzVx70nGpXPYccciiEDowyqEjaUYU2lBBEwbpBvYZAmoVKvS1oj4P61SCEzpvDCpTcIMuy-fVOdmQdAO_Q2RLtPMhAou8SFbM2vCK0zjaTTQi-pfmNAPKW0iZ9_rRN0Zjp7pzEWvlbByUu4BzdcYpoVzLTD2jt_aD3RRfQXkDHGL1rL8zk-9g8g7KMihgQwQqMebvIcJZjtlofpTNdLmetSrvm35JV6IlrK1k_EMGm550nbTNbPSjBn86cNJ_2g2kx2TCy6tfES1nNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: امروز حدود ۷ هزار مگاوات از پنل‌های خورشیدی وارد مدار شده و این یعنی ۷ میلیارد دلار صرفه‌جویی پول
🔹
سوخت کشور را ارزان هدر می‌دهیم و با همین هدررفت هوا را هم آلوده می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454780" target="_blank">📅 22:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454779">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_nLPgZ-vk7rQL3gLx5JAlHz-LEl2gmZyEyLcxOjq6HL3fUQ_OpM115z0ByqAEJuHrghg-hnCbSsWG6pgaGOdHXM5S8WXuF39GySd5fcuxL_tXqkAAwXyQC8AJwWzTWirsaiUHtutrghnpydUYa49OObvAX_tMh2zIAqAGWn3CWoE1n2JHfEAxl2hwiUA-FuHA8yguj1VMW3NwmKB7xGQ8qk_WUsaeKHLW35pQUzxQwoCO-WD1liWEuewz2hQu8Ad9BvMuqMEd4hrCltj7dG2fl7tK1_c8gZ65RLn1utnwTRCdniuE9dMnTuD9Udh0m-bUKNBeHorMqboXL5UP45Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
بررسی صورت‌های مالی ۳ ماهه نخست ۱۴۰۵ نشان داد
✅
تغییر مثبت در عملکرد مالی بانک صادرات ایران/ درآمد عملیاتی ۸۰ درصد رشد کرد
🔹
بانک صادرات ایران با هدف بهبود عملکرد خود در خدمت‌رسانی به مشتریان، فرآیند اصلاح ساختار درآمدی را سرعت بخشید و طی ۳ ماهه نخست سال جاری موفق به افزایش ۸۰ درصدی درآمد عملیاتی و ۲۶ درصدی سود خالص شد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/454779" target="_blank">📅 22:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454778">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⁨ ⁨
✨
شهرآسا؛ جایی که هر تراکنش، یک فرصت تازه می‌سازه…
اگر صاحب کسب‌وکار هستید، وقتش رسیده از تراکنش‌های روزانه‌تون بیشتر از همیشه بهره ببرید.
✨
با استفاده از خدمات آسان پرداخت و اتصال پایانه های فروشگاهی و یا درگاه های پرداخت اینترنتی به حساب بانک شهر، وارد دنیایی از مزایای ویژه «شهرآسا» شوید:
💳
تسهیلات ویژه با نرخ‌های متنوع و اقساط بلند مدت
🎁
جوایز نقدی، هدایای ارزشمند و تجهیزات جانبی ویژه اصناف
📈
امکان بهره‌مندی از تسهیلات برای پذیرندگان آسان‌پرداخت با میانگین یک‌ماهه و سایر پذیرندگان با میانگین سه‌ماهه تا ۷ برابر میانگین حساب و سقف ۱۰۰ میلیارد ریال تسهیلات
🏆
تقدیر از پذیرندگان برتر
✨
و هیجان‌انگیزتر از همه…
هر ماه با هر ۱۰ میلیون ریال تراکنش، یک امتیاز دریافت کنید و شانس خود را برای برنده شدن در قرعه‌کشی جوایز ارزشمند افزایش دهید.
💫
شهرآسا؛ فرصتی برای رشد کسب‌وکار، دریافت تسهیلات و کسب امتیاز، با هر تراکنش.</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/454778" target="_blank">📅 22:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454777">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/454777" target="_blank">📅 22:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454776">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a81f8753f.mp4?token=s4UR4qIeBL_wIPyTh3XCNOFC_mlYgcCq2W_HAMQAQEIeSofuYHWhLVa5hCqJ8k4VPihsxbXMrJFzTHHnlSpX3iyLblgmhQzLsmP977iHxl8cgccQnmZvDNrESDRTQR0wSj6EYl0Le7S8YNeZ8BcH6Kw_OV-3EDkOmUKOPqBOFE_H690PuRKL7IR8H6HqNUGks3OWblTHXgjRlA3vjCxKP6IHxtRCAWBfd8Nn7hX8eNvsJjgrtFCGm_0S2DufdN2LzfzCqD9xCbBwf09M84WRYxRSXRKJLCuT10yXB2XW4cMXyLtKZ9nC0AHO_R_Y-UTpeMivfZLCd1rJmNLo7e3VNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a81f8753f.mp4?token=s4UR4qIeBL_wIPyTh3XCNOFC_mlYgcCq2W_HAMQAQEIeSofuYHWhLVa5hCqJ8k4VPihsxbXMrJFzTHHnlSpX3iyLblgmhQzLsmP977iHxl8cgccQnmZvDNrESDRTQR0wSj6EYl0Le7S8YNeZ8BcH6Kw_OV-3EDkOmUKOPqBOFE_H690PuRKL7IR8H6HqNUGks3OWblTHXgjRlA3vjCxKP6IHxtRCAWBfd8Nn7hX8eNvsJjgrtFCGm_0S2DufdN2LzfzCqD9xCbBwf09M84WRYxRSXRKJLCuT10yXB2XW4cMXyLtKZ9nC0AHO_R_Y-UTpeMivfZLCd1rJmNLo7e3VNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: زمانی که دولت را تحویل گرفتیم با قطعی آب، گاز و برق مواجه بودیم
🔹
اعلام شده بود که ذخایر انرژی کشور فقط تا آبان کفاف می‌دهد و از این تاریخ به بعد سوخت برای چرخاندن نیروگاه‌ها نخواهیم داشت؛ اما با همیاری و مدیریت این مشکل برطرف شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454776" target="_blank">📅 22:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454775">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842fec8e10.mp4?token=gwKglMmxpVJPZj_ZGI_tYI_YkJiksEy4ew3gDh8OnLWfKkp6CFIUa_E14r9u_Vg8_GKPF7trQ-uZ34whf2NizB8VE_v2b7e_NU_IKE4G-RolNlhX1PLPqJ2F1TfsCaPRlXHS_9rNJwRZbfkknoDqzmbtexFeuFbwWHKCnhthwAkNb7rZcNzLnZ3_PoqVDsPZIr9aNmpA9x1gUh3GmV1MeRcjSMQCwEvj6exbXEHBexFX07TKfRZNvjW0dyRnTBZGra3yqiPrH2Q-4ox4Tcf1XFROPmPKDy6X1kUx4VrHm9I8wNnlBGAJlRcoNS7a54AetnXfwERmM4XLA4TrW0VKQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842fec8e10.mp4?token=gwKglMmxpVJPZj_ZGI_tYI_YkJiksEy4ew3gDh8OnLWfKkp6CFIUa_E14r9u_Vg8_GKPF7trQ-uZ34whf2NizB8VE_v2b7e_NU_IKE4G-RolNlhX1PLPqJ2F1TfsCaPRlXHS_9rNJwRZbfkknoDqzmbtexFeuFbwWHKCnhthwAkNb7rZcNzLnZ3_PoqVDsPZIr9aNmpA9x1gUh3GmV1MeRcjSMQCwEvj6exbXEHBexFX07TKfRZNvjW0dyRnTBZGra3yqiPrH2Q-4ox4Tcf1XFROPmPKDy6X1kUx4VrHm9I8wNnlBGAJlRcoNS7a54AetnXfwERmM4XLA4TrW0VKQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: روایت دوم پزشکیان با موضوع اقتصاد و معیشت مردم امشب پخش می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/454775" target="_blank">📅 22:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454774">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7HMC6hYkt_AyVmfd5g1YO8Y9B1vsDO3dXDiaTkHs1yNjIr1AZetfOocdJdqSvg3rnDxbKvL2ZXzi1jQy_Gv-BCDeOa7NFgRbfRq_5k38l0Cp2COzHIsNKfq61l_Z1b7br8Ojr99rIHaNTaoh3gG904OByTrrJN8kokQCdTulEY8tNjxBHoE_XiAGBVX6dktp5OuWIDss9WpN_OK71GwtfN4HKK6aM0Ot-76Inc_Xp_QRZ_yDBg7XDP3bJbpNBz_UyWY9aWWdTn9DWCVOjJ1xiUPNNjm5gkoMxmSOU95Jl8iqi8YePHi70yEUs2xx5gfrlT83Ji0D7K6Q4djSjdpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پاسخ قالیباف به ترامپ: این دیپلماسی نمایشی، شکست خورده است
🔹
«حملهٔ بزرگی تو راهه… صبر کنید، بی‌خیال، اونها می‌خوان مذاکره کنن.» این حرف‌ها چیزی جز یک دیپلماسی نمایشی تکراری نیست.
🔹
استفاده از قلدری + وعده‌های عمل‌نشده + اخبار جعلی به‌عنوان اهرم فشار برای مذاکره، یک استراتژی شکست‌خورده است.
🔹
واقعیت‌ها را بپذیرید و به تعهدات‌تان عمل کنید. ما به نمایش‌های بیشتر نیازی نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454774" target="_blank">📅 22:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454773">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce7b964c9.mp4?token=i5GtAEvScUN85mABx_db_CO5ByiAxuowWONGL14ezUmKnv5O_-Djs8ljzPqNVkxBYDuK-yFhWGSH3qZ7gscZSEbGJeeii9AI6BMzC6NoGtcAPAFt9dRaaV0ziJw5TcLLuRBnhibS0-0Ao7mQ6QNVF5XssI56QcoASbadfuFQQjri1F8urJJ48wCVgl0OgVgnth24a2tw4zlN3KltyZfyDQdVQ3RSAzNImHHYv8NTsEDk854dWkOYBn2TVh4eo2LCqxr6_sdF2YaolU4b4zaEhjymThur1ZUaYMdZNrwnhBMMqltZQ6eF-MRCv_RwcTibdZ3pOxakEqQ4y0mA8-Ce3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce7b964c9.mp4?token=i5GtAEvScUN85mABx_db_CO5ByiAxuowWONGL14ezUmKnv5O_-Djs8ljzPqNVkxBYDuK-yFhWGSH3qZ7gscZSEbGJeeii9AI6BMzC6NoGtcAPAFt9dRaaV0ziJw5TcLLuRBnhibS0-0Ao7mQ6QNVF5XssI56QcoASbadfuFQQjri1F8urJJ48wCVgl0OgVgnth24a2tw4zlN3KltyZfyDQdVQ3RSAzNImHHYv8NTsEDk854dWkOYBn2TVh4eo2LCqxr6_sdF2YaolU4b4zaEhjymThur1ZUaYMdZNrwnhBMMqltZQ6eF-MRCv_RwcTibdZ3pOxakEqQ4y0mA8-Ce3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اتوبوس بمب‌گذاری شده در منطقه دروزی‌نشین دمشق
🔹
منابع خبری گزارش دادند در پی این انفجار، چندین نفر کشته و زخمی شده‌اند، ولی مسئولان دولت «الجولانی» آمار دقیقی در این باره منتشر نکرده‌اند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454773" target="_blank">📅 21:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454772">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoKU4hgJvy88mSY-N9w0Kbreg5ByrHjvIF7To-cGcueI8TDDkFZ85II6cEkgDr2D_WY6UbU_D7cLW6Le-Tu45s3wZa3TXKHYTPp2qU79vN--Yg8q-QOiFKB7NXED1OwwtCBH6tb1tBJxXtqP1lfHDJdj9hAbbZIew-3USxKC2tgnnrdno85XRJMN0hbCYr3wGrvnNShvKUNn3R9XcwnDgGr_SHnQZMPUizY4fxDcDhwqSPjX8ok2dq46e-nnjZ-lRyeNnyCo-EgIMwpusLYhyX6dG4uzPEyQ6L5CjReKaI-uXr0km6H3My5rQCTZ8TgszT8WeyGXo85R_4sqldlNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیومانده گران‌ترین خرید تاریخ رئال‌مادرید
⚽️
رئال‌مادرید به‌صورت رسمی از جذب یان دیومانده خبر داد. این وینگر ساحل‌عاجی با انتقالی بزرگ از لایپزیش راهی سانتیاگو برنابئو شد.
⚽️
ارزش این انتقال ۱۲۵ میلیون یورو به‌همراه ۱۵ میلیون یورو بندهای پاداش اعلام شده…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454772" target="_blank">📅 21:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454771">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef8d84e289.mp4?token=WaQ8-hlk3aljEzx9vKwRXpfhNdCoN02mQBtWxwSiKuDz4kXogaqkXKYd3KEfMkvcfEM3ed3UHILYARcfcsGeiApFmrIq3q7oyHONLDkvkmEJ1leeMkKLN8aSyisGWeTMNgD-LWltbdIxTdDkYTdjTsu155ZV-o-1oe-VYQtijB81SC2hBk3ZzepCIdErn-fM9LSngVyGoWX8fXbGrmOeczx4x7kXhrL2_JYGfpVVGGnYDz0KmQ0PzxdWN_hcasyO0kl9gRakjbXrVuddK8nvwWtha3IbxhYzl9NM0H7YMWZu_kQdwHQp8_dri7gtahzPysVdbi83Hd374ZHRHNOC4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef8d84e289.mp4?token=WaQ8-hlk3aljEzx9vKwRXpfhNdCoN02mQBtWxwSiKuDz4kXogaqkXKYd3KEfMkvcfEM3ed3UHILYARcfcsGeiApFmrIq3q7oyHONLDkvkmEJ1leeMkKLN8aSyisGWeTMNgD-LWltbdIxTdDkYTdjTsu155ZV-o-1oe-VYQtijB81SC2hBk3ZzepCIdErn-fM9LSngVyGoWX8fXbGrmOeczx4x7kXhrL2_JYGfpVVGGnYDz0KmQ0PzxdWN_hcasyO0kl9gRakjbXrVuddK8nvwWtha3IbxhYzl9NM0H7YMWZu_kQdwHQp8_dri7gtahzPysVdbi83Hd374ZHRHNOC4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت زائر استرالیایی که به کمپین نظافت مسیر اربعین پیوست در برنامۀ پرچمدار
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454771" target="_blank">📅 21:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454770">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815aa180ab.mp4?token=E0VJInF9PmKXA5A9Qo2q-jztNzgy7B5tejBrbygR4L712kUnm8Z-aN8M2u5e9mkYhsg05De9lTj3AmSFAwrGXwDjkYJ6rB2TddoXrUsQjpBjseu9QRt1PzMVM_s0729WUitR75dOc68pIv1U5SsTZvX6lkOs18C8tLsc8xx6fgsnulMWJkk56cECi_m1CSV9_wFx0LL5VpMy0q2p74p6zXqA0M-PKuil6XtlZsaO1yStKG3AOdaX7O85-RwMojLDw9QBU2HaDt0WSg_aocncclL-FQi4d83k0r9c5nkgGy3UojTzDAowYcYHNanS-bOihD3uzb75WUUTo5-D647vsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815aa180ab.mp4?token=E0VJInF9PmKXA5A9Qo2q-jztNzgy7B5tejBrbygR4L712kUnm8Z-aN8M2u5e9mkYhsg05De9lTj3AmSFAwrGXwDjkYJ6rB2TddoXrUsQjpBjseu9QRt1PzMVM_s0729WUitR75dOc68pIv1U5SsTZvX6lkOs18C8tLsc8xx6fgsnulMWJkk56cECi_m1CSV9_wFx0LL5VpMy0q2p74p6zXqA0M-PKuil6XtlZsaO1yStKG3AOdaX7O85-RwMojLDw9QBU2HaDt0WSg_aocncclL-FQi4d83k0r9c5nkgGy3UojTzDAowYcYHNanS-bOihD3uzb75WUUTo5-D647vsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رئیس دادگستری تهران: ۶ متهم پروندهٔ کینگ‌مانی به حبس‌های طولانی محکوم شدند
🔹
القاصی‌مهر: ۶ نفر از متهمان حقیقی پروندهٔ کثیرالشاکی موسوم به کینگ‌مانی به‌اتهام اخلال در نظام اقتصادی کشور از طریق مشارکت در کلاهبرداری شبکه‌ای و ایجاد رمزارز جعلی به‌نام «کینگ‌مانی»…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454770" target="_blank">📅 21:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454769">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/755b6ac5f8.mp4?token=ffjl3c12iEXQztrRPCUNvdmTs8oDYrlEIFe-u5v6hbZPHFZngUh1Q2F1ICBb10-VZByVPScbSxXTFrJs7p2RcH3ZOvF22UxsRXX9O6Z83A72TYtgdTbLiNroT_5V4kdnay1-vJFRzIS8eolOU9BrhtqyTjR69wH5NLR0KLnhJDWQxjZZYVcDjvA3YTkQgUAOQStatQtFVFdLkY8MQjILhm7s2ri8BEbz9ycERVMIriPuWrzZ5RMNFeleWbIN6iwFklF7HSEUxM5yM0lQADQcLf59zV4VzfTFrm2eQ6AUVPADIxGIj80J6MvWQ_0Ncx1xcs7h0iIUxBnUI-pSRuhHCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/755b6ac5f8.mp4?token=ffjl3c12iEXQztrRPCUNvdmTs8oDYrlEIFe-u5v6hbZPHFZngUh1Q2F1ICBb10-VZByVPScbSxXTFrJs7p2RcH3ZOvF22UxsRXX9O6Z83A72TYtgdTbLiNroT_5V4kdnay1-vJFRzIS8eolOU9BrhtqyTjR69wH5NLR0KLnhJDWQxjZZYVcDjvA3YTkQgUAOQStatQtFVFdLkY8MQjILhm7s2ri8BEbz9ycERVMIriPuWrzZ5RMNFeleWbIN6iwFklF7HSEUxM5yM0lQADQcLf59zV4VzfTFrm2eQ6AUVPADIxGIj80J6MvWQ_0Ncx1xcs7h0iIUxBnUI-pSRuhHCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در رویای تسلیم؛ اینجا با همه‌جا فرق دارد
🔹
معاون ترامپ: تسلیم ایران واقع‌بینانه نبود.
🔹
نشریۀ آمریکایی آتلانتیک: تاب‌آوری
ایران
دولت ترامپ را غافل‌گیر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454769" target="_blank">📅 21:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454768">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adbfa05438.mp4?token=tEAc0RqQ-u85Hb-kJT-Vpr0kNfV4_QUr_eWxsfh7yOyGfhw6Orx37uKgP8EiEvsj9YR84hmTm7j6tNEEH38hfiMafM9d8wzYXCYG4m_smI_pmFDAEFzazm08CJJNDbia88sZqgVF3CjLP8fNon_D3l0qJtZx9FX-N4vWOouVJTtr8EFHr7UQqcRSTRFibYBKu93fbefOM2num5hJlzaISCgnPZddrX8BXxNMysoqg0jk1nTTuHnYIKq4Jy1ok_uqd2SS8maWsZV8wuxzvjph1af4TuCDZg8aKkZqA6-wlYBJlB4UfHk_0CdjLt0ECYJBWnVDZ2Fme90GdPtJfWzsRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adbfa05438.mp4?token=tEAc0RqQ-u85Hb-kJT-Vpr0kNfV4_QUr_eWxsfh7yOyGfhw6Orx37uKgP8EiEvsj9YR84hmTm7j6tNEEH38hfiMafM9d8wzYXCYG4m_smI_pmFDAEFzazm08CJJNDbia88sZqgVF3CjLP8fNon_D3l0qJtZx9FX-N4vWOouVJTtr8EFHr7UQqcRSTRFibYBKu93fbefOM2num5hJlzaISCgnPZddrX8BXxNMysoqg0jk1nTTuHnYIKq4Jy1ok_uqd2SS8maWsZV8wuxzvjph1af4TuCDZg8aKkZqA6-wlYBJlB4UfHk_0CdjLt0ECYJBWnVDZ2Fme90GdPtJfWzsRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این شبه‌کودتا را نه می‌توان فراموش کرد و نه می‌توان بخشید!
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454768" target="_blank">📅 21:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454767">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3876fd02d.mp4?token=TIZTtHYJZbQBz0i0Ks-4Q0_JiJzyDV0u8akalNY2lZJhqm7Z-v_COLGSEsIktm32FwBcsLTEX7NRjd1wCfgPKdfvQ7HNDBa88d6eg9P7KDbCNiIMRb-Wo4TnDWDtnxYngFkAvU45e8oF6J6pmE2U50DKgR07JsqPF1a_dyDJPPaRpDJzYqw3qweXXEJiGupZ6D8CQ4CnK4krd_JBQ3_uHcZZOw7GNlTpWkIcvcX7q9IJEr_tUghRsUCUjx7zPWo4ms3O3mQ5WlTM-WKRhkyoxlbAB_Gf7VULIdNGaUTmRixfa53I50rKEZixwUWbUbn1LgHfhuNfLV6Kvnm-mST4KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3876fd02d.mp4?token=TIZTtHYJZbQBz0i0Ks-4Q0_JiJzyDV0u8akalNY2lZJhqm7Z-v_COLGSEsIktm32FwBcsLTEX7NRjd1wCfgPKdfvQ7HNDBa88d6eg9P7KDbCNiIMRb-Wo4TnDWDtnxYngFkAvU45e8oF6J6pmE2U50DKgR07JsqPF1a_dyDJPPaRpDJzYqw3qweXXEJiGupZ6D8CQ4CnK4krd_JBQ3_uHcZZOw7GNlTpWkIcvcX7q9IJEr_tUghRsUCUjx7zPWo4ms3O3mQ5WlTM-WKRhkyoxlbAB_Gf7VULIdNGaUTmRixfa53I50rKEZixwUWbUbn1LgHfhuNfLV6Kvnm-mST4KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت اطلاعات: ۲۱ مزدور موساد و ۴ شرور مسلح در کرمان بازداشت شدند
🔹
وزارت اطلاعات اعلام کرد ۲۱ نفر از عوامل مرتبط با سرویس جاسوسی و تروریستی رژیم صهیونیستی (موساد) در عملیات‌های اطلاعاتی در استان کرمان شناسایی و بازداشت شدند.
🔹
این افراد اطلاعات مراکز حساس…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454767" target="_blank">📅 21:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454766">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ece69941e8.mp4?token=BbR3ZdUrZWPfxnVo41bHt9Sdt1HF-gOq0S3__KusOREnfkO3Q6uGdAQQ7N--BGcwEF_66fdO8wu9Qq26OrpkCTZyZGInErJTjOU4fjO8m5rdbSeICU85Nk1zLrWwDbcQF-twCh9Nq_qi3mkzpukmXRac1zKQIFJ5GkulmwlOW-kRNiQLwTugLZVSVTEJKkANP9MqjhwBDZnfBZMlKH8nutBIUL8iV_VIXPnLjGKa8r0TD_0DttIR8yMWk7U-WAm5f2Lc6rrlzkERtcq9TzJn43XAuBAajVhEpbFclWUeaDhm3B6KKzs7P0JTXQYcHWYPJ4fAXJcIbuAP6iASQNTNcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ece69941e8.mp4?token=BbR3ZdUrZWPfxnVo41bHt9Sdt1HF-gOq0S3__KusOREnfkO3Q6uGdAQQ7N--BGcwEF_66fdO8wu9Qq26OrpkCTZyZGInErJTjOU4fjO8m5rdbSeICU85Nk1zLrWwDbcQF-twCh9Nq_qi3mkzpukmXRac1zKQIFJ5GkulmwlOW-kRNiQLwTugLZVSVTEJKkANP9MqjhwBDZnfBZMlKH8nutBIUL8iV_VIXPnLjGKa8r0TD_0DttIR8yMWk7U-WAm5f2Lc6rrlzkERtcq9TzJn43XAuBAajVhEpbFclWUeaDhm3B6KKzs7P0JTXQYcHWYPJ4fAXJcIbuAP6iASQNTNcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پشت‌پردۀ یک ویدیوی هالیوودی تا عموی جدید براندازان
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454766" target="_blank">📅 20:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454765">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">برکناری دو مقام اطلاعاتی در موساد به‌دلیل شکست مقابل ایران
🔹
کانال ۱۲ تلویزیون رژیم صهیونیستی گزارش داد «گوفمن» رئیس موساد، در پی ناکامی تلاش برای سرنگونی نظام جمهوری اسلامی ایران، دو تن از مقامات ارشد این سازمان اطلاعاتی را برکنار کرده است.
🔹
براساس این گزارش،
رئیس اداره اطلاعات
و
رئیس بخش ایران
در موساد از سمت‌های خود عزل شده‌اند.
🔹
این تصمیم در پی ارزیابی عملکرد موساد در جریان عملیات مربوط به ایران و شکست در تحقق هدف تغییر نظام سیاسی در این کشور اتخاذ شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454765" target="_blank">📅 20:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454763">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ldz4_DcKP8mBcMWcSfCQ6XYWdPDj89qiuVT8LDvF_IRaBN3xCDAaONoG0tt5HXkKuyX9k1RvEmLqa0bgDPJuSKNtxe8UZTKHK1_euGMxIjGwb7YV29tDXOIY8xoWAPX0tY431qka2avXr4yvJlAUk4lCJCl3PcjAGsVNZA18fyjqTWT0JlcYdMu1EuftvuLH0HGluG8_QuaRPXoULfsh2T7uNcWQmZqOKdJr57b2LjInD_HB7evPcrwwu1NwRaJIwMqcSQNXGyv90_aBBzlnkZvNu05PqHzsgu8D9DrPPv4OZzF-LB7BzxdRiLoDgA5iXPycN0AEjCMHeuH6Sb0fCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011041439e.mp4?token=JNAYvkkcq3B8iHrllXJxOPCYofe3DyooxhF1pSIeilKtsj_gmvyhHGZxBWPt7mNaKtX4rY2lABlqdM4g3LUyTIxi6DEjZUau0Eqb3odoFaz9aXp2-6pQfQTAcd8wQeE0sSBWCaahN3vUKV6GzrhfWK5BM2WcFNacSwade3LRr9zz0CQc2l3K_nWw47aDX-oKWche88p_-6Y_tJqFMVEQ3nryq_nVgB_l_ECQdD_JgAXBoD5FPRVYxKViM9dhbUCD0XuI0pPJsJumY8ZmkbLQWdFD_G4-SNarWXFfIO4XxvGGpJg7c9Vc4bZXsGPKN_sf7_e1SnXgQ9i-l7YunzOrEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011041439e.mp4?token=JNAYvkkcq3B8iHrllXJxOPCYofe3DyooxhF1pSIeilKtsj_gmvyhHGZxBWPt7mNaKtX4rY2lABlqdM4g3LUyTIxi6DEjZUau0Eqb3odoFaz9aXp2-6pQfQTAcd8wQeE0sSBWCaahN3vUKV6GzrhfWK5BM2WcFNacSwade3LRr9zz0CQc2l3K_nWw47aDX-oKWche88p_-6Y_tJqFMVEQ3nryq_nVgB_l_ECQdD_JgAXBoD5FPRVYxKViM9dhbUCD0XuI0pPJsJumY8ZmkbLQWdFD_G4-SNarWXFfIO4XxvGGpJg7c9Vc4bZXsGPKN_sf7_e1SnXgQ9i-l7YunzOrEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اتوبوس بمب‌گذاری شده در منطقه دروزی‌نشین دمشق
🔹
منابع خبری گزارش دادند در پی این انفجار، چندین نفر کشته و زخمی شده‌اند، ولی مسئولان دولت «الجولانی» آمار دقیقی در این باره منتشر نکرده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454763" target="_blank">📅 20:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454762">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f182f8aae.mp4?token=gGO3nKchXau5CmaObSDlaovV1x2vu9jsXuZkVMY5-jtDvRXOZPgdY1i4RlOkmHoWtIziFS45aX1gU11TqJly897-s-tkGFtjwjKmYSPaOCVowZnox5yVK5vqg1DpV3P1lCH89CFxIX9IxPC4OSUzimsf8A2M7Lulpl-nff9zdwjFAIjTGp5v0mFfJ9RTNPtKiORJVsuGM2PAMy_jkxnNQQ6YckDmMyJ3i4S-TDKl5fonXg4sS7xLYyaNodIuDamyn3CaT2JgaunjRLsg8C6XdMZIEh9tepbWXga-FjW8yLgeME4S2Bk-TYxMPVkRb2py6mcDUfQEzSdjtWqBgbiyCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f182f8aae.mp4?token=gGO3nKchXau5CmaObSDlaovV1x2vu9jsXuZkVMY5-jtDvRXOZPgdY1i4RlOkmHoWtIziFS45aX1gU11TqJly897-s-tkGFtjwjKmYSPaOCVowZnox5yVK5vqg1DpV3P1lCH89CFxIX9IxPC4OSUzimsf8A2M7Lulpl-nff9zdwjFAIjTGp5v0mFfJ9RTNPtKiORJVsuGM2PAMy_jkxnNQQ6YckDmMyJ3i4S-TDKl5fonXg4sS7xLYyaNodIuDamyn3CaT2JgaunjRLsg8C6XdMZIEh9tepbWXga-FjW8yLgeME4S2Bk-TYxMPVkRb2py6mcDUfQEzSdjtWqBgbiyCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت جدید و تکان‌دهندۀ دانش‌آموز مینابی از لحظات حملۀ موشکی به مدرسه شجرۀ طیبه در محفل ستاره‌ها
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/454762" target="_blank">📅 19:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454760">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بقایی: بیانیۀ مشترک ایران و عمان در مرحلۀ تدوین نهایی است
🔹
مختصات جغرافیایی مسیر مدنظر ایران و عمان در تنگهٔ هرمز، موردتفاهم قرار گرفته و چنانچه برخی طرف‌های ثالث در این زمینه کارشکنی نکنند، بیانیه مشترک ۲ کشور در مرحله بررسی و تدوین نهایی است.
🔹
تفاهم ایران…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/454760" target="_blank">📅 19:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454759">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">جزئیات متن اولیۀ طرح راهبردی مدیریت تنگه هرمز
🔹
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.
براساس این طرح:
🔸
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی و سایر کشورهای متخاصم از تنگه هرمز ممنوع می‌شود.
🔸
محموله‌های مرتبط با رژیم صهیونیستی، اعم از نظامی و غیرنظامی، حق تردد از این منطقه را نخواهند داشت.
🔸
شناورها یا محموله‌هایی که در اقدامات علیه جبهه مقاومت نقش داشته باشند نیز مشمول ممنوعیت خواهند بود.
🔸
کشورها و اشخاصی که به ایران خسارت وارد کرده‌اند، تا زمان جبران خسارت، مجوز عبور از تنگه هرمز و خلیج فارس را دریافت نخواهند کرد.
🔸
برای قانون‌شکنان، جریمه‌های سنگین از جمله تا ۲۰ درصد ارزش محموله، پیش‌بینی شده است.
🔸
دولت موظف خواهد شد با همکاری نیروهای مسلح، مسئولیت‌هایی مانند هدایت ناوبری، نظارت بر تردد شناورها و حفاظت از امنیت و محیط زیست خلیج فارس را برعهده بگیرد.
🔹
این طرح همچنان در مرحله بررسی کارشناسی قرار دارد و مجلس از صاحب‌نظران خواسته پیشنهادهای خود را برای تکمیل آن ارائه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/454759" target="_blank">📅 19:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454758">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8919b3d826.mp4?token=VoVVS4NBFmNsW7EagSLYOPkP3W9_leSHWI-HoyrwnokunSGF1lOq_um96ori61AqCTPKiEM-NL-qPY9_FUtBfq6RH3SeIdTt7Tw6KNa4PhHxNaeAmBn_YtGVU9GbZB4rn5X4aDVNDmJgdXijvfrF5ltyjLLX7w-ef6LKB0MLjs_PahkDiANuyq3NCD2U804VnPhpkQBPvaUx-qP2Y3dGTu-VWx4-oqa5k6AQLtzEL446w61qJqm-T568MMK9e-iGjgGOXiiXPtF-pHNwfZBRIeGsdR-x27A59Vo3U0FnIG4Qn2PwQB4Fuc6mbxzRx1KuRclQXYkA75wnlal84EnJrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8919b3d826.mp4?token=VoVVS4NBFmNsW7EagSLYOPkP3W9_leSHWI-HoyrwnokunSGF1lOq_um96ori61AqCTPKiEM-NL-qPY9_FUtBfq6RH3SeIdTt7Tw6KNa4PhHxNaeAmBn_YtGVU9GbZB4rn5X4aDVNDmJgdXijvfrF5ltyjLLX7w-ef6LKB0MLjs_PahkDiANuyq3NCD2U804VnPhpkQBPvaUx-qP2Y3dGTu-VWx4-oqa5k6AQLtzEL446w61qJqm-T568MMK9e-iGjgGOXiiXPtF-pHNwfZBRIeGsdR-x27A59Vo3U0FnIG4Qn2PwQB4Fuc6mbxzRx1KuRclQXYkA75wnlal84EnJrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مستندساز آمریکایی از فرهنگ عزاداری و پرچم‌های قرمز خون‌خواهی رهبر شهید در اربعین امسال عراق
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454758" target="_blank">📅 19:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454757">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-text">🎬
#تماشا_کنید
✅
حضور فعال بانک تجارت در قلب عسلویه
💫
پروژه بازسازی فازهای ۴ و ۵ پارس جنوبی با بازدید میدانی دکتر اخلاقی مدیرعامل بانک تجارت کلید خورد.
📌
گامی بلند برای تأمین مالی، بازسازی و بازگشت سریع‌تر این پروژه ملی به مدار تولید.
⬅️
دکتر اخلاقی: ما در بانک تجارت، نه فقط یک تأمین‌کننده، بلکه همراهِ عملیاتیِ صنعت نفت، گاز و پتروشیمی برای حفظ اقتدار انرژی کشور هستیم.
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454757" target="_blank">📅 19:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454756">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454756" target="_blank">📅 19:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454755">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-text">پشت پرده تلاش‌ها برای نشاندن گزینه نادره رضایی در دفتر موسیقی
🔹
در روزهای اخیر، زمزمه‌هایی مبنی‌ بر پایان کار بابک رضایی، مدیرکل دفتر موسیقی وزارت فرهنگ و ارشاد اسلامی به گوش می‌رسد و به‌رغم آنکه هنوز حکم مدیرکل جدید صادر نشده، اما شنیده‌ها از افزایش احتمال انتصاب گزینه‌ای به نام احمدحسین فتایی حکایت دارد. فردی که نه به واسطه سوابق تخصصی و تجارب موفق مدیریتی در حوزه موسیقی، بلکه به دلیل نزدیکی به نادره رضایی، معاون معزول امور هنری وزارت فرهنگ و ارشاد اسلامی مورد توجه قرار گرفته است.
🔹
نادره رضایی از بدو حضور در مسند معاونت هنری حاشیه‌های فراوانی را به وجود آورد و عملکرد او با انتقادات بسیاری همراه بود؛ حواشی و انتقاداتی که در نهایت سبب شد وی از معاونت امور هنری برکنار شود.
🔹
فتایی در دوران مسندنشینی نادره رضایی، پس از خداحافظی ناگهانی و پرسش‌برانگیز بهروز فتحی از سمت مشاور اجرایی معاونت، به شکلی کاملا بی سر و صدا جایگزین او شد و تا واپسین روز برکناری معاون سابق، از نزدیک‌ترین چهر‌ه‌ها به وی محسوب می‌شد. همین سابقه سبب شده است که گمانه‌ها درباره انتصاب او، صرفاً به‌مثابه یک جابه‌جایی ساده مدیریتی تلقی نشود، بلکه متضمن این پرسش مهم نیز باشد که آیا به‌رغم انفصال نادره رضایی از مجموعه وزارت فرهنگ و ارشاد اسلامی، حلقه مدیران نزدیک به او همچنان در معادلات کلیدی وزارتخانه نقش داشته و از نفوذ قابل توجهی برخوردارند؟
🔹
فتایی اگرچه در دوره معاونت نادره رضایی، کمتر در معرض افکار عمومی قرار داشت، اما در بسیاری از اقدامات و مأموریت‌های معاون معزول ازجمله بازسازی میلیاردی دفتر نادره رضایی، نقشی کلیدی را عهده‌دار بود. از همین‌رو در صورت نهایی شدن انتصاب او، این شائبه تقویت خواهد شد که خروج یک فرد از رأس هرم مدیریتی وزارت فرهنگ، الزاماً به معنای پایان نفوذ او در وزارتخانه نیست.
🔹
وزارت فرهنگ و ارشاد اسلامی حالا این فرصت را پیش‌رو دارد تا با انتخابی شفاف و اقناع‌ساز، مبتنی بر مولفه‌هایی چون تخصص، تجربه، شایستگی و توانمندی، ابهامات موصوف را برطرف و اعتماد از دست رفته بخشی از جامعه موسیقی را ترمیم کند؛ چرا که اگر قرار باشد انتصاب‌ها بر پایه روابط و پیوندهای مدیریتی با مدیران کنار رفته از مسند صورت پذیرند، پرسشی کلیدی نزد افکار عمومی ایجاد می‌شود و آن؛ اینکه آیا نادره رضایی واقعا از معاونت هنری رفته است یا صرفا جایگاه رسمی خود را از دست داده و همچنان در بدنه وزارتخانه نفوذ دارد؟
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454755" target="_blank">📅 18:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454754">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">زیان ۱۰۰ همتی صندوق‌ نفت از واگذاری سهام خلیج فارس
🔹
رئیس هیئت‌رئیسۀ صندوق‌های بازنشستگی صنعت‌نفت: واگذاری نزدیک به ۳۰ درصد از سهام هلدینگ خلیج‌فارس در سنوات قبل بیش از ۱۰۰ هزار میلیارد تومان به صندوق‌های بازنشستگی صنعت‌نفت زیان وارد کرده است.
🔹
با توجه به مطالبۀ حدود ۸۳ هزار نیروی رسمی و حدود ۱۱۰ هزار بازنشستۀ عضو این صندوق، احقاق حقوق این افراد در دستور کار جدی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454754" target="_blank">📅 18:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454751">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vf8jhW9CRJSweIbuFQOqwkUTBBxAjbDgdhv8Y7Aex5g4YQxVkvIqeABvPJMafvm5ELuctpsDVUsT5AbGXezsKHar2kaXmfQAC-oa6H5D-0dddXY50ouspaChDlu2NZHnwW53TvZqzF1NeW-H4vJtSR7KfYbm-mhvyGdPHhvmWtGNGqUSEfUPlKzw_phuYjf1oChBTFgzF8TLaz1A4dGSsECFbp6QoerDgds1Xe72N3fZsO0u4PnR2zRKor40k4bHLN5CKJ7gGw09JDe3urJOAF3F8Z7sIFuiCKuxFDFBM0geR0XqSweIndLqIJPNUikDXCywQvk-Xp1BjiRc_ge6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDcCQ1hgStlLAyKUwrdpiRAtgLaP2LGw5z-tKbF9qeSXdZCmxQU6NXPXXe0jyv8jhc0QL0IGg8lb-E1lKYWJbtvCM391QDn3ESz0KNu8tVzYaQzrfRP8ok0l0YldPPYsIepu22bg3anys2QkN-PPjD-4B9Rpge8QBVJT0-McFy9LjMSYTlH9fD_iEvcGPWWv_tn2s8hctIitpLGoxnnOtiJSSmLJE6s1R9cgs8ajd7gC9InOTtMeEeGx8Z1nY-kTP4f0P59DGdkU6jNQBPwInKmLvnkBuvjrZX4SJ5ZqjzlTcKcQwJVueEDqehc1-5uXcU6VAcTtyqEKHSzIvkglSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrJKHbA4JcI0-XNvSAnd2zylda3uutEr0IeXWdH_pR_WxH-dN0XgHv4QQElkeypNEsm3MWk-xD9Mpo7F9pXJGDgZ5ackDDwhhHvHTbkaSzMwZXvQpzxKaZW41hEMIQr1Ic57QHdLB4iHAeu5Q8mrNqmFfyTEil7XJyMDXGHGsOD_NZ27RvrUwBuWNdM3CJegeu2xyy8IFhPndpBDpXNifjldszvE5NUwZ-HeIduUl8D5hKIgishqBaIVQC7XS8kd_gxFDYPnd8-fKVu_tUPtELf0v-qO-XXNY_134VtMMLhk0s_rNFf6sk3KoRvDxH-HVwUcvybekKAkOL7qZiEnCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیومانده گران‌ترین خرید تاریخ رئال‌مادرید
⚽️
رئال‌مادرید به‌صورت رسمی از جذب یان دیومانده خبر داد. این وینگر ساحل‌عاجی با انتقالی بزرگ از لایپزیش راهی سانتیاگو برنابئو شد.
⚽️
ارزش این انتقال ۱۲۵ میلیون یورو به‌همراه ۱۵ میلیون یورو بندهای پاداش اعلام شده تا دیومانده به یکی از گران‌ترین خریدهای تاریخ رئال تبدیل شود.
⚽️
انتقال دیومانده به رئال گران‌ترین انتقال تاریخ یک بازیکن آفریقایی است.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454751" target="_blank">📅 18:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454750">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807aa726f1.mp4?token=QE55LHZMsscVEV8JAlg1_i0xqa4ojZHY336eflOfYNUXK1fTlJmOegAEpVSIwYRPKK8aVE8McaYRFYA74CdTGFA2ZXfLNx1oPMGiXShOm_0bd9f38D9nHjB5qIqqEyH2qiyf7VK56iJD4Odfcp8sbYK7vbrzu18zxTqPvRjr7VhscyNcRPKYsJoyLv_qgdEplzgEn_kNeBJEmhcuxwXm4ORZDDG0uoDlgHjf4FYuo_d9_eKnHsjRFhOjitVsrborkzSBz66pGdKqBSYX6Qs4yxx6z1qiTASq6j5HauFUlrEbykfEp7SuK_1FgjRhovseWGaKLeq61m_8qsLMAcVwTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807aa726f1.mp4?token=QE55LHZMsscVEV8JAlg1_i0xqa4ojZHY336eflOfYNUXK1fTlJmOegAEpVSIwYRPKK8aVE8McaYRFYA74CdTGFA2ZXfLNx1oPMGiXShOm_0bd9f38D9nHjB5qIqqEyH2qiyf7VK56iJD4Odfcp8sbYK7vbrzu18zxTqPvRjr7VhscyNcRPKYsJoyLv_qgdEplzgEn_kNeBJEmhcuxwXm4ORZDDG0uoDlgHjf4FYuo_d9_eKnHsjRFhOjitVsrborkzSBz66pGdKqBSYX6Qs4yxx6z1qiTASq6j5HauFUlrEbykfEp7SuK_1FgjRhovseWGaKLeq61m_8qsLMAcVwTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یوتیوبر آمریکایی از ۲۲ میلیون زائر امسال اربعین و تعجب او از موج خون‌خواهی رهبر شهید ایران در بین زائران اربعین امسال
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454750" target="_blank">📅 18:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454749">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ضربۀ کوبنده انصارالله به مزدوران سعودی در یمن
🔹
منابع رسانه‌ای از حملات موشکی و پهپادی انصارالله به مواضع نیروهای وابسته به عربستان در چند استان یمن خبر دادند. براساس گزارش‌ها، دست‌کم ۴۵ نفر کشته شده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454749" target="_blank">📅 18:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454748">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfff69d92.mp4?token=McoAHKnJva4LoIoHzNmAwkJ3tUtn188sjDIbqcrM1j43Ol0EpADzLgoWm3KJnCUE-brDxekdWAkRxQyUtYKMtotSqgjlWh1KVk5HTyeXVJrgzd1bs-Qt8Oon1nP9tsOtAk86ccoCuWUJYWNXkS1OpCG85LT3_bHLWcHB75OzrPBivvTGUhcv8bdGUEr52J4fPVXXVUEdiKrXIpeSpbRdcmCFX76GlHQoQZ3KG153FN8ONyFl4h4KSlS-O5tPpTiCmpXomb4tykiBZwUwCo1ycLjP5B31RvSTgkF8Mv5cSY9MgV2lmu7fG1pKAACx1gLHGO53mFpqB063oO03LipFGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfff69d92.mp4?token=McoAHKnJva4LoIoHzNmAwkJ3tUtn188sjDIbqcrM1j43Ol0EpADzLgoWm3KJnCUE-brDxekdWAkRxQyUtYKMtotSqgjlWh1KVk5HTyeXVJrgzd1bs-Qt8Oon1nP9tsOtAk86ccoCuWUJYWNXkS1OpCG85LT3_bHLWcHB75OzrPBivvTGUhcv8bdGUEr52J4fPVXXVUEdiKrXIpeSpbRdcmCFX76GlHQoQZ3KG153FN8ONyFl4h4KSlS-O5tPpTiCmpXomb4tykiBZwUwCo1ycLjP5B31RvSTgkF8Mv5cSY9MgV2lmu7fG1pKAACx1gLHGO53mFpqB063oO03LipFGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان انتظار کلزاکاران شهرستان صحنه کرمانشاه
🔹
در پی پیگیری پویش «
پرداخت مطالبات کلزاکاران صحنه را بیش از این به تأخیر نیندازید
»،
مدیر تعاون روستایی استان کرمانشاه
از تسویه کامل باقی‌مانده مطالبات کلزاکاران شهرستان صحنه تا ۲۵ مردادماه خبر داد.
@Farsnews_My</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454748" target="_blank">📅 17:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454747">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24b709c29.mp4?token=sBWBu6ttlYjcCM0w38U_rhypiLj7jpyUedRWXNkG0ZHbsGb_h62c_npIwZ5CC_TjpqiMgh-jqcR-i_tIba_zWkuNkuv6CAFEe0cLcriRB9c9BTAKSvIBJtPS7g93cbMjG4zYikcKJ_bNKR8BiDeNnkr7z9mYSwHi0NiuRm7PD81hsgcPh11QLzEtGbGOtwwRUdJIsJnYXxCSEbvEGQFhCpyId9a_h5lV206pBqJ39UvNuGc53A_yvtdAzCE29b1cVTGJCM3eoIDoYfQW309CbyfUnFWC93L4-jYqUG2_aVLqXyyFva2nL02llILYo3DLva5bsKyVynOoTKz4ohn8gDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24b709c29.mp4?token=sBWBu6ttlYjcCM0w38U_rhypiLj7jpyUedRWXNkG0ZHbsGb_h62c_npIwZ5CC_TjpqiMgh-jqcR-i_tIba_zWkuNkuv6CAFEe0cLcriRB9c9BTAKSvIBJtPS7g93cbMjG4zYikcKJ_bNKR8BiDeNnkr7z9mYSwHi0NiuRm7PD81hsgcPh11QLzEtGbGOtwwRUdJIsJnYXxCSEbvEGQFhCpyId9a_h5lV206pBqJ39UvNuGc53A_yvtdAzCE29b1cVTGJCM3eoIDoYfQW309CbyfUnFWC93L4-jYqUG2_aVLqXyyFva2nL02llILYo3DLva5bsKyVynOoTKz4ohn8gDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاک‌ترین بانک جهان اینجاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454747" target="_blank">📅 17:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454746">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9758b875b.mp4?token=nXStCVaPI49A3Cx9FgU4pRv6qHio9y5r8VKjwm4tr2ZjSg2_1hNyQ17vQG3Hxz9KIHE9CEBNlIx9WOS8vZJdgdOjv1dUqBV_-GJRXFIKZrTKsZoOE-0UuLq5_H-tPRBldNe2F6hbqq3gPyCl2UupjIS_Kecz4fKk4OUQGvYALvbLa--8K7JDtmB6vmdgO7H64XqBlradnmKHEg02_NT7zLyjaJBJIQLtWJm_jHTyYce0MgX-IUaKHW5LVow-ouf8y6lbrT5PcSk7eaQ4Gyu4M_Fwz56DSBqJfu1g23JVlK0SvD-kbkORjqL2Dq7zaRNiSwYJHUgOvAXvp9G-WEwR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9758b875b.mp4?token=nXStCVaPI49A3Cx9FgU4pRv6qHio9y5r8VKjwm4tr2ZjSg2_1hNyQ17vQG3Hxz9KIHE9CEBNlIx9WOS8vZJdgdOjv1dUqBV_-GJRXFIKZrTKsZoOE-0UuLq5_H-tPRBldNe2F6hbqq3gPyCl2UupjIS_Kecz4fKk4OUQGvYALvbLa--8K7JDtmB6vmdgO7H64XqBlradnmKHEg02_NT7zLyjaJBJIQLtWJm_jHTyYce0MgX-IUaKHW5LVow-ouf8y6lbrT5PcSk7eaQ4Gyu4M_Fwz56DSBqJfu1g23JVlK0SvD-kbkORjqL2Dq7zaRNiSwYJHUgOvAXvp9G-WEwR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترس کارشناس کویتی از تسلط ایران بر تنگۀ هرمز: شاه که رابطۀ خوبی با آمریکا داشت و ژاندارم منطقه نامیده می‌شد چنین اختیاراتی در هرمز نداشت اما ایران اکنون می‌تواند کلیددار امنیتی تنگه نام بگیرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454746" target="_blank">📅 17:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454745">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌ وال‌استریت‌ژورنال: بحرین و کویت در حمله به ایران مشارکت مستقیم داشته‌اند
🔹
وال‌استریت‌ژورنال به‌نقل از منابع آگاه نوشت: کشورهای بحرین و کویت در اقدامی مخفیانه، جنگنده‌های خود را برای حمله به اهدافی در داخل خاک ایران اعزام کرده‌اند.
🔹
امارات نیز با ارائه…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454745" target="_blank">📅 17:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454744">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fg-LG8QW2Q3JSGBN2Hsw0HFTT-8L1QQT8M_TGFDyDz4AH6yxPPMe0CxkMqk71IrcfndIK-_9yueur00IxsJXaGFOQInJ1eZ1qTF-ceYksLM-heaDnHwwfo6t9-P9SlS9uO32lay-T0jCxtRsqhYIHzK7ZNAEDpSE0ju9kp9nPVcedR57RXtFE7lgT_nqpYzZaL_40HUTBR5IpCw_HpcryjyCvbvHpatl7uJNV5faZpSRtdXdSkLkx-QDwFj27fOmOVNEPLY9tOhO-h299Xv6QMy8LpF1AZmHm557dje45OTK9mOGTj-ZnioTztS5wFvNIiNoEP7KYI4xwicykHyjZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل سازمان ملل در سالگرد جنایت اتمی هیروشیما از آمریکا نام نبرد
🔹
آنتونیو گوترش در پیام خود به مناسبت هشتادویکمین سالگرد بمباران اتمی هیروشیما، بار دیگر بدون اشاره به نام آمریکا، درباره خطر جنگ هسته‌ای، تشدید شکاف‌های ژئوپلیتیکی و لزوم درس‌گرفتن از فاجعه…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454744" target="_blank">📅 17:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454742">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgwKW6rKzrUPQq-xAORExJdGDsjOUAAqOI0Jp-JsrYlcLWVdnYM5WIs_Do8gJ9MBWSYpbbQYkGBtyHGw4xcIDJ6xijjDfQmEjQ9o4Xs25spCWcjVPJTIv6u1TSJLXyY40vrlPp_HneFhdx7ZjsoaY7SPadoBtAYbgMQIDVVUqJPZPRb4SVRALt4uq9sCEWSMh5yNlL0P9RZnNc2cX898SAF7dJBpJ3Q2WmOnFBL3ApTzZY4U3tqSpeMofWH_PGjnavGi_eNwZ0B-XWZHjGoIf620uD6qCzbOHGOxoDTJDjnQlUNdRe4KyVUUG-FsUYcRi_sr6vKW1Q9eDf1on-NTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مشروطه نقطه عطف بیداری و آزادی‌خواهی ملت ایران بود
🔹
یکصدوبیست سال از فرازِ تاریخیِ انقلاب مشروطه می‌گذرد؛ آرمانی ملی که با همبستگی و وفاق اجتماعی به ثمر نشست؛ رویدادی که نقطه‌عطفی شکوهمند در تاریخ معاصر و نشانه‌ای روشن از بیداری، هوشمندی و آزادی‌خواهی ملت بزرگ ایران است.
🔹
این جنبش پیشگام که نخستین تجربه نظام پارلمانی و قانون‌گرایی را در خاورمیانه رقم زد، نشان داد که مردم‌سالاری و شورا، ریشه در اندیشه و معارف دینی این مرزوبوم دارد؛ حقیقت والایی که با تمسک به تعبیر شریف قرآن که می‌فرماید «وَشَاوِرْهُمْ فِي الْأَمْرِ»، زینت‌بخش نهاد قانون‌گذاری در ایران شد و الگویی ماندگار از حکمرانی متکی بر خواست مردم را پیش ‌روی ملت‌های منطقه نهاد.
🔹
مشروطه نه یک حادثه محصور در گذشته، بلکه سرآغازِ فرایندی است که در طول یک قرن اخیر، با فرازونشيب‌های گوناگون تعمیق یافته و با پیروزی انقلاب اسلامی و استقرار نظام جمهوری اسلامی به مرحله‌ای نو و بومی از مردم‌سالاری دینی رسید.
🔹
امروز، ایران اسلامی با اتکا به نهادهای قانونی، حضور آگاهانه مردم در عرصه تصمیم‌گیری و ظرفیت‌های باشکوه علمی و ملی خود، راه دستیابی به پیشرفت و آبادانی را با صلابت ادامه می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454742" target="_blank">📅 16:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454741">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5rTwzeQzT7CNz8Q3AHokOBejtc8jzrTSxNKRgPbQPqOw15dFFiAlwYL7FyM_7ur93sUVOdwdYgO93TtcVoXCH5iRh8XZX80qbDW7rfPmoPOgeTutXbPXF_XOTvgBUTnGksoRBGo-W-GcLHhPZt9NIYxEZ_0_obaPhNLSDg9vIZlEDRu_1j0rKtctkOYgdJUvDmNvkjKP4GE1wgwHjJtdV2eswjGoaKVoOaF6_rolB3WlzgDu8EcutpbPmBaGjcLose0FClcg53To51XDH7F5ll5dGAokMmDkcuRZ4W1Pa-cwr7BL-LG1vR-fBT-3MxbgB88BmQL-w7GiBOxEfsTwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز را ببخشیم تا صلح شود؟
🔹
ناصر هادیان، استاد دانشگاه تهران، معتقد است ایران می‌تواند در ازای رفع تحریم‌ها از دریافت عوارض تنگۀ هرمز صرف‌نظر کند؛ زیرا به‌گفتۀ او درآمد این آبراه سالانه بیش از ۷ تا ۸ میلیارد دلار نیست و اصرار بر آن می‌تواند به تداوم درگیری‌ها منجر شود. او حتی رقم درآمد ادعایی‌اش را با تخفیف نفتی ایران به چین برابر دانسته است.
این دیدگاه با انتقاد کارشناسان اقتصادی و راهبردی مواجه شده است. منتقدان ۴ ایراد اصلی را مطرح می‌کنند:
🔸
۱. وعدۀ رفع تحریم‌ها تضمین‌شده نیست و تجربه برجام خلاف آن را نشان داده است.
🔸
۲. برآورد تخفیف نفتی ایران به چین بیش از واقعیت اعلام شده و طبق برخی گزارش‌ها حدود ۱.۲ میلیارد دلار در سال است.
🔸
۳. درآمد بالقوۀ تنگه هرمز با دریافت عوارض می‌تواند تا حدود ۴۰ میلیارد دلار در سال برسد.
🔸
۴. کنار گذاشتن اهرم اقتصادی تنگه، به‌جای کاهش تنش، ممکن است هزینه اقدامات نظامی علیه ایران را کاهش و احتمال تکرار آن را افزایش دهد.
🔹
به‌باور منتقدان، در معادلۀ تنگه هرمز، بازدارندگی و منافع ژئوپلیتیکی در کنار منافع اقتصادی باید در محاسبات لحاظ شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454741" target="_blank">📅 16:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454739">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370904d528.mp4?token=gAxAJupXdZPlXYvfgR_PBhx_2nfMHX5aecmF9eM8aX5NqXQmvMf0X88SqR6WtdAQGd6aw_yASEOKqqTtlqIkoxjoqahDZa5O9zbfaQPW6iWV_4sVZQIz7XplwceYAYWE_ygdWE190PZHca0mvmEd3QgnT2VoDPD89j13zdWRmQAsg7fhbtZgAzKoZxrzWqi6PLk3npleOP1T4jUpk124FrDd-szRguueZEJX0o8yMg_XkwCWEGTm4OlkvN-sjmaqgNKQkSiryFWTuZf4lvPBtIKlzjhXW1lpOQECcJ8l5nBimz2HVXKSDkHxjqainyaLSKAHa0StZQRUdw9D-x-Zrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370904d528.mp4?token=gAxAJupXdZPlXYvfgR_PBhx_2nfMHX5aecmF9eM8aX5NqXQmvMf0X88SqR6WtdAQGd6aw_yASEOKqqTtlqIkoxjoqahDZa5O9zbfaQPW6iWV_4sVZQIz7XplwceYAYWE_ygdWE190PZHca0mvmEd3QgnT2VoDPD89j13zdWRmQAsg7fhbtZgAzKoZxrzWqi6PLk3npleOP1T4jUpk124FrDd-szRguueZEJX0o8yMg_XkwCWEGTm4OlkvN-sjmaqgNKQkSiryFWTuZf4lvPBtIKlzjhXW1lpOQECcJ8l5nBimz2HVXKSDkHxjqainyaLSKAHa0StZQRUdw9D-x-Zrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع یمنی اعلام کردند تا دقایقی دیگر، نیروهای مسلح یمن با انتشار بیانیه‌ای از یک عملیات نظامی گسترده و ویژه خبر خواهند داد.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454739" target="_blank">📅 16:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454738">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed2183872.mp4?token=rVJSewuXMB_JMLPX5ttWDMSNMJVAqi7VfvSRE_0OabPlwsrGM49c9mcx6dkD3YpkqqmxjePHUf-yL-fhEtYlo9pOfoLOjiPI8_YGWU9kJ0fqv0OwZWvJQGHOWiCnb1iJQ-BOwGTev8yRh3qYB86QQLwcbAY0Ohtm3gx3pZvNbrhFGaKvICrIicYTsb6la4-74lcZ4acfMDu_n5OUev1fu0wLmEJFRIzXMQ-qJbJSNmvO6WgVpwaZI1XhTD0pjINFjEIKRLOV8dEnAJadjF4Qblbfco0RIodgOqlu11FXGewmMDPnvxm4S1ECLsLMygh8Bw7GY448m1dvD46gXtrRzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed2183872.mp4?token=rVJSewuXMB_JMLPX5ttWDMSNMJVAqi7VfvSRE_0OabPlwsrGM49c9mcx6dkD3YpkqqmxjePHUf-yL-fhEtYlo9pOfoLOjiPI8_YGWU9kJ0fqv0OwZWvJQGHOWiCnb1iJQ-BOwGTev8yRh3qYB86QQLwcbAY0Ohtm3gx3pZvNbrhFGaKvICrIicYTsb6la4-74lcZ4acfMDu_n5OUev1fu0wLmEJFRIzXMQ-qJbJSNmvO6WgVpwaZI1XhTD0pjINFjEIKRLOV8dEnAJadjF4Qblbfco0RIodgOqlu11FXGewmMDPnvxm4S1ECLsLMygh8Bw7GY448m1dvD46gXtrRzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشکر موشکیِ رزمندگان پای لانچر از مردم عراق
🔹
رزمندگان هوافضای سپاه برای تشکر از مردم عراق، جملات درخواستی‌شان را روی موشک نوشتند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454738" target="_blank">📅 16:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454737">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-text">افسار غول‌های فناوری در دست ژنرال‌های نظامی
🔹
حضور مدیران ارشد امنیتی و ژنرال‌های سابق پنتاگون در شرکت‌های پیشرو هوش مصنوعی، نشان می‌دهد این فناوری از یک محصول تجاری به ابزاری در حوزه زیرساخت‌های حیاتی و نظامی تغییر ماهیت داده است.
🔹
اما این تغییر ساختاری تنها به یک شرکت محدود نماند؛ انتصاب دریاسالار پاول ناکاسونی، فرمانده سابق سازمان امنیت ملی آمریکا در اوپن‌ای‌آی و پیوستن قائم‌مقام سابق سی‌آی‌ای به آنتروپیک، نشان داد غول‌های فناوری رسماً لباس رزم به تن کرده‌اند.
🔹
ورود این چهره‌های امنیتی به اتاق تصمیم‌گیری سیلیکون‌ولی، ابعاد جدیدی از تسلط نظامی بر آینده الگوریتم‌ها را فاش کرده است.
اینجا
بخوانید
@FarsnaTech</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454737" target="_blank">📅 16:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454736">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سرنوشت تلخ تولیدکننده خراسانی؛ ۱۷ ماه انتظار برای ارز استحقاقی
🔹
امین ویسی، بنیان‌گذار و مدیرعامل شرکت سپهر ترخیص راه سبز ضمن انتقاد از بروکراسی‌های اداری و عدم حمایت‌های لازم از صنعت تولید برنج در خراسان رضوی، از بلاتکلیفی ۱۷ ماهه ارزی و تبعات آن برای اشتغال‌زایی در استان خبر داد.
این گفت‌وگو را
اینجا
مطالعه کنید</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454736" target="_blank">📅 16:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454735">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVRytxxEvMsGyx-fozrpghx4mq79svJwTLr-7Y4ot5zg-kXdYxj3MXNHLEVHmzrB82MqaNFbFGMbkpcRRFg3NKVh3Q5YFVcOPl4bgjM3me8DdpEy0-cUfPCqxzoQRSdfTPTfwXRCKwiIFpsaVgYnhFlcLj-6O_mh1KaSSoOZboc3w78LX0FEBPkOyKlMVC_FiYeUsvSjknPHpxJVUEeKTwkRNSCT88E5PMPADifd3OLsguLjqEtYL1AKsDp479QaKRWzkJH0frigWxdkl6e562afSzPTyivKVNDjeLHng9tf8JyrMamQgEhi0RDZ4ZemMLUn-t2rvxtCbmiydUeBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست مدیریت عامل بانک سرمایه در نشست منطقه هفت تأکید کرد؛
✅
اجرای برنامه تحول بانک با تمرکز بر منابع پایدار، درآمدهای کارمزدی و بازسازی اعتماد مشتریان
🔹
به گزارش روابط عمومی بانک سرمایه، نشست بررسی و ارزیابی عملکرد شعب منطقه هفت و تبیین برنامه‌های عملیاتی بانک سرمایه با هدف بررسی وضعیت عملکردی شعب، پایش منابع و مصارف، مرور برنامه‌های اجرایی بانک در سال جاری و تبیین اولویت‌های منطقه هفت با مرکزیت ساری برگزار شد.
🔸
دکتر موسی اسلامیان در این نشست، ضمن تسلیت فرارسیدن ایام اربعین حسینی، مباحث خود را در چهار محور وضعیت گذشته بانک، مقایسه آن با شرایط فعلی، اقدامات انجام‌شده و تبیین اهداف کوتاه‌مدت و بلندمدت بانک در سال جاری تشریح کرد و گفت: بانک سرمایه با تدوین برنامه‌های عملیاتی چهارماهه از آذر تا اسفند ۱۴۰۴، پیگیری افزایش سرمایه، برگزاری مزایده املاک و اموال مازاد و تدوین استراتژی بلندمدت پنج‌ساله طرح تحول، احیا و بازآفرینی، مسیر تازه‌ای را برای تقویت ساختار مالی و عملیاتی خود دنبال کرده است.
🔗
[
متن کامل خبر
]</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454735" target="_blank">📅 16:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454734">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454734" target="_blank">📅 16:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454733">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
منابع یمنی اعلام کردند تا دقایقی دیگر، نیروهای مسلح یمن با انتشار بیانیه‌ای از یک عملیات نظامی گسترده و ویژه خبر خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454733" target="_blank">📅 16:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454732">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7a4bf4c40.mp4?token=fgOY0Ore5INUPoe6Y0LHMJPVtkYeUVAIkrsl2wxSe-zVcrMhkJk3b8R_TPhsHZk2BRHLt7ZfwQNKnEhawbarC91rRgimfsUEG9tRxOZnfZoNPllMJ-ElJNstDbtN3wtu5Zq_7nkz4FYiJUFfaBktnsM2mQv3IXGyLTAr2hrSvHGXrPWroxvQvXzeIxWA5g6BOjuyHOK_cVH_s9mT1-W7TPz0V3rryNhd16jyX_FqQrxJFx5xQXBbpVhLDxu24s25T5EAQPCvGo-vUe8WuPaglAjsqJRqbVXnylhZhGiTJXskvWcFqyFlbZp8eFDdDfSR4lasolnMWUn7h2kdE8vLyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7a4bf4c40.mp4?token=fgOY0Ore5INUPoe6Y0LHMJPVtkYeUVAIkrsl2wxSe-zVcrMhkJk3b8R_TPhsHZk2BRHLt7ZfwQNKnEhawbarC91rRgimfsUEG9tRxOZnfZoNPllMJ-ElJNstDbtN3wtu5Zq_7nkz4FYiJUFfaBktnsM2mQv3IXGyLTAr2hrSvHGXrPWroxvQvXzeIxWA5g6BOjuyHOK_cVH_s9mT1-W7TPz0V3rryNhd16jyX_FqQrxJFx5xQXBbpVhLDxu24s25T5EAQPCvGo-vUe8WuPaglAjsqJRqbVXnylhZhGiTJXskvWcFqyFlbZp8eFDdDfSR4lasolnMWUn7h2kdE8vLyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری یک دهه نودی در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454732" target="_blank">📅 16:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454730">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh173LhYUUQFZ0GP0hPHRSfa37Cgxxl-IW4NnAMxXzHZwqC3BughU6ttDNK0xWSiUiBdXY-PpMh5GvLgwg1fJoT5uoZxH4D1WkJgNSX0_AR7m2KA4ov1MR-iv6djBml58MeTHMd_UhA_qExIBZzS_n1ceZUaq7TcRenVX5UA5g3Rer_cwQDDUtv8vao2-lsyfdAa_zSVmZwr7oL2Ak6Q6CwfnVAX3Jz0Smxs78E8mU4sy0Gd8m_StjKRPTubd-T_oDicWq33KFxCUZr_bM5iCfyR0fdu-fIjwMXHa_3fomEG1ieXZIBx_2TLmA5FJV9qkbvSVpR9PewQ7a1_5eMsFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد حساب‌های بانکی‌تان را اینجا ببینید
🔹
تارنمای بانک‌مرکزی برای نمایش حساب‌های بانکی هر شخص حقیقی فعال شد. افراد می‌توانند با مراجعه به
my.cbi.ir
تعداد حساب‌های بانکی فعالشان را چک کنند.
🔹
طبق اعلام بانک‌مرکزی در آینده امکان غیرفعال‌کردن حساب‌های بانکی از این سامانه مهیا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454730" target="_blank">📅 16:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454729">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f383cf50aa.mp4?token=Lrgyk6bt2yNZtSK3PQsCdj1T0HqwB9jQoyzJ4TOosdXZhuQGxxacwp3qt7M9N2K80MJiGasBKkBHeNjdbuxtCY3ikGl8dZ50MJwrjN2Y4CpgDPL_X_dvgjQw0jBma7Siy3lwuLP9I7HMdl0T0Bc5Os_LC9H_JMrBDgs0EnQna2hhe8cCg_YfYUPQ-PJ9d81hnGC6ZWfYjZHw6Vohi2FQx_1gEhIoZrajHDgyT3TmQYHObc3tmmwmjqE_bKBhr5iHeYcTDn_0MRPfuJf-_KGxoqVgC5SXxr6KxBOWkgWGCkHiwHxuLB7K8cnG24C0hMClCyQmSw8TCeSnviinS7NPdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f383cf50aa.mp4?token=Lrgyk6bt2yNZtSK3PQsCdj1T0HqwB9jQoyzJ4TOosdXZhuQGxxacwp3qt7M9N2K80MJiGasBKkBHeNjdbuxtCY3ikGl8dZ50MJwrjN2Y4CpgDPL_X_dvgjQw0jBma7Siy3lwuLP9I7HMdl0T0Bc5Os_LC9H_JMrBDgs0EnQna2hhe8cCg_YfYUPQ-PJ9d81hnGC6ZWfYjZHw6Vohi2FQx_1gEhIoZrajHDgyT3TmQYHObc3tmmwmjqE_bKBhr5iHeYcTDn_0MRPfuJf-_KGxoqVgC5SXxr6KxBOWkgWGCkHiwHxuLB7K8cnG24C0hMClCyQmSw8TCeSnviinS7NPdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ‌کسی در دنیا نمی‌تواند این میهمانی را مدیریت کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454729" target="_blank">📅 15:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454728">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هلاکت اعضای تیم تروریستی در سیستان‌وبلوچستان
🔹
روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه: یک تیم تروریستی که قصد داشت در جنوب سیستان‌وبلوچستان اقدام به عملیات تروریستی کند پیش از اجرای عملیات تروریستی متلاشی شد.
🔹
این تیم با داشتن سلاح و مهمات به قصد انجام…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/454728" target="_blank">📅 15:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454727">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72cdbc7cdf.mp4?token=PdqrOc6N47NR6UUU2mzMBwFS3RW32pAzdsHiuY-5P7FxAmUHoercKbIOl_F-RHmu7KqXc4G1RMhGfIJHUEbUVG3Gto1k9zf9qrObaBaDKaePLqLJGHd6pGPxI9mH7sScxtwBGkILyodf0neaJ7IqW9FWQEXjuRs73XQI_2ppjJgjZed4Fq-WTRUcBxoNOFqR-nlceuv61uT8_xBA27zJgST-O-XXBmQyGRFQDQMtNMx4Wz0C-kER14XE1Rja9lXuFep3Nu0NWLxluhAER7Gqb3U3sYoKDTEFDJ_sOE-Z-_n45ihl7tdKpT7yni6MkMLF-zpnLPdP4MdbcKPoR5EbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72cdbc7cdf.mp4?token=PdqrOc6N47NR6UUU2mzMBwFS3RW32pAzdsHiuY-5P7FxAmUHoercKbIOl_F-RHmu7KqXc4G1RMhGfIJHUEbUVG3Gto1k9zf9qrObaBaDKaePLqLJGHd6pGPxI9mH7sScxtwBGkILyodf0neaJ7IqW9FWQEXjuRs73XQI_2ppjJgjZed4Fq-WTRUcBxoNOFqR-nlceuv61uT8_xBA27zJgST-O-XXBmQyGRFQDQMtNMx4Wz0C-kER14XE1Rja9lXuFep3Nu0NWLxluhAER7Gqb3U3sYoKDTEFDJ_sOE-Z-_n45ihl7tdKpT7yni6MkMLF-zpnLPdP4MdbcKPoR5EbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگاه الکل‌سنج تنفسی بومی‌سازی شد
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/454727" target="_blank">📅 14:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454726">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هلاکت اعضای تیم تروریستی در سیستان‌وبلوچستان
🔹
روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه: یک تیم تروریستی که قصد داشت در جنوب سیستان‌وبلوچستان اقدام به عملیات تروریستی کند پیش از اجرای عملیات تروریستی متلاشی شد.
🔹
این تیم با داشتن سلاح و مهمات به قصد انجام عملیات تروریستی از کشورهای همسایه وارد کشور شده که در کمین رزمندگان سپاه قرار گرفته و در درگیری مسلحانه  اعضای این تیم تروریستی به هلاکت رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454726" target="_blank">📅 14:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454725">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXiG07veC7KsaVIyMTkC-oJj503BX2u_Jlx_bCLnq4YDouzEs2t8oGtQB4G4e0uJVZ9q4axjqToRMSnXyMA8AKpMWW9cbR9_Pnopf1Um8gmEEYVma_nT_Hoo-w2SGKnH9iGT6zIQYWwyH8LyEkucdvW9EM6DyxBmC_hKN2qv7rlbB8d5kX_s_U6dga1fkDKA-3R_JDHAPbVINor2XAQobPDPew_z79Nhv4F_ZDGAklN2UrREcskT2B5IezepoQZKRDCg6BWMgNCTMZW3WiELDREI0SzsR07cvyUPsN1gboeJU6rcSkLF-7fY_6IuzbouYboK0EAJqCWiqZ76SeRUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه‌قضائیه: ادعای ردزنی محل استقرار شهید لاریجانی از طریق تماس تلفنی صحت ندارد
🔹
خبرگزاری قوه‌قضائیه: پیگیری‌ها از پروندۀ قضایی مربوط به شهادت علی لاریجانی نشان می‌دهد ادعای یکی از نمایندگان مجلس مبنی بر شناسایی محل استقرار شهید لاریجانی از طریق تماس تلفنی…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/454725" target="_blank">📅 14:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454723">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb4bb875c.mp4?token=KQTNOsIhOBSaddhqjdNqtQThXKAMQby70z2G89GoYaNrP8bUVoR4sJAF-PAyxozKZqESddLDnlqPWcgM8xJDmAMprAD_NEIvwaNsf90K_6Q_QpVVlKvgQLOtAtG-gpI8DtXsITB0Avsqt6hVtct3toO4EbOfmpCoK3V14055aqh8ksaiQHZMvUVf0F-NZBVVeRL3legYEogmE9IzD2j7JwNWtEuXTJB-bw9feLFrUnibAH2y5-x5VstKRV3BxftT5aD2CksJ-L7PrsunsNVziGWvA59keEv-oq-4NbuCWpWMFR9NL1NXgjINf8gt1dRJQHipPEGr8be_4QbY3Vecyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb4bb875c.mp4?token=KQTNOsIhOBSaddhqjdNqtQThXKAMQby70z2G89GoYaNrP8bUVoR4sJAF-PAyxozKZqESddLDnlqPWcgM8xJDmAMprAD_NEIvwaNsf90K_6Q_QpVVlKvgQLOtAtG-gpI8DtXsITB0Avsqt6hVtct3toO4EbOfmpCoK3V14055aqh8ksaiQHZMvUVf0F-NZBVVeRL3legYEogmE9IzD2j7JwNWtEuXTJB-bw9feLFrUnibAH2y5-x5VstKRV3BxftT5aD2CksJ-L7PrsunsNVziGWvA59keEv-oq-4NbuCWpWMFR9NL1NXgjINf8gt1dRJQHipPEGr8be_4QbY3Vecyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پالایشگاه بزرگ نفت روسیه هدف حمله قرار گرفت
🔹
درپی حملهٔ چندین پهپاد اوکراینی، پالایشگاه نفت یاروسلاول روسیه دچار انفجار و آتش‌سوزی شد.
🔹
این پالایشگاه، یکی از ۵ پالایشگاه بزرگ روسیه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454723" target="_blank">📅 14:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454722">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شرط جدید برای بازنشستگی اعلام شد
🔹
مدیرکل امور فنی صندوق بازنشستگی کشوری: میزان سابقۀ خدمت الزامی برای بازنشستگی برخی گروه‌ها با توجه به سابقۀ خدمت قابل‌قبول آنان در تاریخ لازم‌الاجرا شدن قانون، سوم مرداد ۱۴۰۳ افزایش یافته؛ با این حال افرادی که در این تاریخ بیش از ۲۸ سال سابقۀ خدمت برای بازنشستگی داشته‌اند، مشمول نخواهند بود.
🔹
میزان افزایش سابقۀ خدمت برای سایر کارکنان نیز متناسب با سابقۀ خدمت آنان تعیین شده:
🔹
۲۵ تا ۲۸ سال سابقه، به ازای هر سال تا بازنشستگی ۲ ماه
🔹
۲۰ تا ۲۵ سال سابقه ۳ ماه
🔹
۱۵ تا ۲۰ سال سابقه ۴ ماه به سنوات الزامی بازنشستگی اضافه می‌شود.
🔹
افزایش سابقۀ خدمت با رسیدن آقایان به ۶۲ سالگی و خانم‌ها به ۵۵ سالگی متوقف می‌شود.
🔹
همچنین ایثارگران، معلولان، شاغلان مشاغل سخت و زیان‌آور و برخی از بانوانی که پیش از لازم‌الاجرا شدن قانون شرایط قانونی بازنشستگی را احراز کرده‌اند، مشمول نخواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/454722" target="_blank">📅 14:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454721">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قوه‌قضائیه: ادعای ردزنی محل استقرار شهید لاریجانی از طریق تماس تلفنی صحت ندارد
🔹
خبرگزاری قوه‌قضائیه: پیگیری‌ها از پروندۀ قضایی مربوط به شهادت علی لاریجانی نشان می‌دهد ادعای یکی از نمایندگان مجلس مبنی بر شناسایی محل استقرار شهید لاریجانی از طریق تماس تلفنی فرزندش با خانواده، صحت ندارد.
🔹
بررسی‌های انجام‌شده و پروندۀ تشکیل‌شده در این باره، این ادعا را تأیید نمی‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/454721" target="_blank">📅 14:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454720">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBEQs0cvhki4Qzx7HjgVntjxHg8j5qQMJpqQUSmAD-JxE1E3kC1FL1qYTYGSu_2SoJ6G925MR6BOII7V2hTZV6HLb9AsxFfp_-XzTriOmTH5PP08GdJx2QeTHR_PHRojfNh2eX7BjhlBBOYOraWwvHfgPR8D5kIb4zFpyJIRWg-9UE8iVtCekfET8MAj0NnbcF3vj2Fd4wodFJQdDqidmjP0JEyvzGsBFv2TF_YMisajuSft8PtOtkIKImZLMpETtPuw5ums_KhqM1GWGYhsdBxp53-qAUXuHGmHay1yZlYlJlcA8mBE3VdruciykuGwlkxomtqNmReDZJY8IEMZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تقدیر فرمانده هوا فضای سپاه از بسیجیان دریا دل کاشان
بسیجیان دریا دل کاشان سلام‌علیکم
🔹
افتخار خدمت‌گذاری خالصانه و صادقانه به‌طور قطع و یقین زیبندۀ شما و مصداق تلاش جهادگرانه شما عزیزان است .
🔹
از اینکه در سخت‌ترین شرایط همگامی و همراهی شما را در کنار رزمندگان هوافضا داریم برخود می‌بالیم و به‌وجود شما مباهات می‌کنیم. انشاالله سربلند و پیروز باشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/454720" target="_blank">📅 13:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454719">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزارت اطلاعات: ۲۱ مزدور موساد و ۴ شرور مسلح در کرمان بازداشت شدند
🔹
وزارت اطلاعات اعلام کرد ۲۱ نفر از عوامل مرتبط با سرویس جاسوسی و تروریستی رژیم صهیونیستی (موساد) در عملیات‌های اطلاعاتی در استان کرمان شناسایی و بازداشت شدند.
🔹
این افراد اطلاعات مراکز حساس و طبقه‌بندی‌شدۀ نظامی و پدافندی را جمع‌آوری و برای موساد ارسال می‌کردند.
🔹
همچنین ۴ نفر از اعضای باندهای مسلح شرارت در استان کرمان بازداشت شدند که از آن‌ها سلاح و مهمات جنگی و شکاری کشف و ضبط شده است.
🔹
وزارت اطلاعات همچنین از کشف و ضبط ۴ سلاح جنگی از ۵ نفر از عناصر مسلح بازداشت‌شدۀ مرتبط با کودتای دی‌ماه ۱۴۰۴ و تحویل آن‌ها به دستگاه قضایی خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454719" target="_blank">📅 13:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454718">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">۲۲ متهم پرونده‌های ارزی بازداشت شدند
🔹
دادستان تهران: تاکنون برای مدیران شرکت‌های تراستی ۵۹ پرونده تشکیل شده که در ۴۳ پرونده، قرار جلب دادرسی صادر شده است.
🔹
۲۲ نفر از متهمان این پرونده‌ها به زندان معرفی شده‌اند و برای ۱۵ نفر از آنان اعلان قرمز (اخطار بین‌المللی…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454718" target="_blank">📅 13:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454717">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVh_ABKvP3VWK_rRJzMSuIqSDgsWSGUNedZ0KhY8NUboZ_vvHozeLVmcjOdpXkMJnrInsBavvTaWiLnt1FS8r5fIXGRiZ8nY13u0kYWUrO5CtV8USM5R98_wGfJyxDgrEEAgOat1qyDZCv1o1amTJpW9azMcXeqADPnw9YBsdGie_8MJWJLurPSY2_dsLhH7bcqKcDQx-JQeKrAJ0Xg9PVSBAcvROTzy6yZS3AZe9Oh2IsGOYKCGndRtuvXwrmTRPEqncuLhN0WMsBcuZQmhyMW_aV16sf0r7cR8HHueq_VgjDAkf2-HLM8KQ_2OHFpCXjpbV_QEHmDQAXiozXEILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تنظیم مقررات: اعمال ضریب ۲.۷ برای اینترنت بین‌الملل صحت ندارد
🔹
در روزهای اخیر برخی کاربران در فضای مجازی مدعی شده‌اند که مصرف هر یک گیگابایت اینترنت بین‌الملل، معادل ۲.۷ گیگابایت از حجم بسته محاسبه می‌شود و همین موضوع را عامل زودتر تمام‌شدن بسته‌های اینترنتی نامیده‌اند.
🔸
سازمان تنظیم مقررات و ارتباطات رادیویی این ادعا را تکذیب و اعلام کرد هیچ ضریب افزایشی برای اینترنت بین‌الملل اعمال نمی‌شود و حجم بسته‌های اینترنتی نیز تغییری نکرده و یک بسته ۱۰ گیگابایتی همچنان معادل ۱۰ گیگابایت اینترنت بین‌الملل است.
🔸
به‌گفتۀ سازمان تنظیم مقررات، منشأ این برداشت، تعرفه ترجیحی ترافیک داخلی است؛ به این معنا که با همان اعتبار بسته، هنگام استفاده از برخی خدمات داخلی، به‌دلیل تعرفه ارزان‌تر، امکان مصرف حجم بیشتری از اینترنت داخلی وجود دارد و این موضوع ارتباطی با کاهش حجم اینترنت بین‌الملل ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454717" target="_blank">📅 13:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454716">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sccH9AqPxjtnwKzQ6NKE0nrm5Ccspv-F3fj3f6V7_kIJdE_nFzEJuCSAbwBPRd50kyDr05kPLRnQ5RUWqv3wytXnDlS8M2eg_nOJ7fwykqHFjzeQ7c043kUqqrnxKX26fGVwfdke6ofS0Lcm2mHnuJ44s3cQCYQJCBnQoyXf-PjERsD0eRVmmrf8WqtK28lQB0D7RhDITU6h6Cod18ri6siRgCfiS3qed8GRjIkZzad4WTKbrotT8ktawOjetr3-Dv8u2593_FPfAUHIyz7xerO5yGVsGHCb6C4T_zqvxC9nYY8R2Ki4xUDi5Ubo3-rvsOlWL0i-OOnPJUGWZN5iSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل سازمان ملل در سالگرد جنایت اتمی هیروشیما از آمریکا نام نبرد
🔹
آنتونیو گوترش در پیام خود به مناسبت هشتادویکمین سالگرد بمباران اتمی هیروشیما، بار دیگر بدون اشاره به نام آمریکا، درباره خطر جنگ هسته‌ای، تشدید شکاف‌های ژئوپلیتیکی و لزوم درس‌گرفتن از فاجعه هیروشیما سخن گفت.
🔹
گوترش در حالی از نام بردن از عامل این حمله خودداری کرد که در سال‌های گذشته نیز رویکرد مشابهی داشته است. همزمان، نخست‌وزیر ژاپن و شهردار هیروشیما نیز در مراسم یادبود، نامی از آمریکا نبردند.
🔹
آمریکا در سال ۱۹۴۵ با بمباران اتمی هیروشیما و ناگازاکی، تنها حملات هسته‌ای تاریخ جنگ را رقم زد. این حملات صدها هزار قربانی برجای گذاشت. با این حال، واشنگتن تاکنون مسئولیت اخلاقی این جنایت را نپذیرفته و هیچ‌یک از رؤسای‌جمهور آمریکا نیز بابت آن عذرخواهی نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454716" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454715">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3229ff6f33.mp4?token=pLGnNmv2PTISnFqimO9G6g2JMY4LNfHNCxUrpi9bGo6BHyWYBgDEQMnBpLddzTAymykb_bSroKJtDIBcXzH0DoGhV30gXQlgAT7FFJVV6UnonL8_B8V180-ubzCZjKQwggqDMIQEuGorR52ZXtf0dAj4HCH7NNRjKlXJ3Z3_aHC7sneXh8mEdcZm0OJa-mTdxvRKd-yRktR2REdDLcGz5htUBjfgPK0Om2lJQ90mW0V0pHeOe8DmXWW9WQEc6twtD-3HzHdad8-1-DeDCyy_1uA4JsvUElNo3OQrXohtTpeDfJRUfbQ-G0U7FH5Ibui-e2FPyT5Fi2Aqr6MEI5tuGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3229ff6f33.mp4?token=pLGnNmv2PTISnFqimO9G6g2JMY4LNfHNCxUrpi9bGo6BHyWYBgDEQMnBpLddzTAymykb_bSroKJtDIBcXzH0DoGhV30gXQlgAT7FFJVV6UnonL8_B8V180-ubzCZjKQwggqDMIQEuGorR52ZXtf0dAj4HCH7NNRjKlXJ3Z3_aHC7sneXh8mEdcZm0OJa-mTdxvRKd-yRktR2REdDLcGz5htUBjfgPK0Om2lJQ90mW0V0pHeOe8DmXWW9WQEc6twtD-3HzHdad8-1-DeDCyy_1uA4JsvUElNo3OQrXohtTpeDfJRUfbQ-G0U7FH5Ibui-e2FPyT5Fi2Aqr6MEI5tuGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راه جدید انتقال پول را بشناسید
🔹
«کیف پول ایران» یک ابزار پرداخت الکترونیکی است که امکان شارژ کیف پول، انتقال وجه، مشاهده موجودی، برداشت وجه و خرید حضوری و آنلاین را فراهم خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454715" target="_blank">📅 12:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454714">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار لرستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8b9829e0.mp4?token=fqAOz3sfd-dJLK6wSNMy2c-xUYjy_vyDQ_7kOKTU4nzkhLF_J_ie_IldqXd-MvHKeFT1dUrkwxLC-kGHH27g5zTXkirCasc3ymLIA2MbNF0xuhI80NlgZ3ETTL9KPUn7lCxsYGSEBuKzy65Su_rtQCXTGlXfk6yqrZbhuY1Fm9f0_MbEfaxw9mMF311Ad5fMhrUbPwwYlFeDE0ckzJeACvnuHokTFBWOYHrE57fPUjZNiXTRZGco-o1Oq-aYkSTq3oV5qy_M5frRiE1TvcEK4LHbbR9VQxpddST0W4lf_6k4016yQfP0RKJB9yCOQFzMESsI1NpqMtXkAVlUKRTZHkhKs6da_6i2wk0wxNF3DZTEcSTJAhrjPmsoukNxlcQmUFfly_4xaJGa2PhwuKWxBZ0j9n1X-EJQCYMPu9S2bvXPylID5Gx-KhVFWx5eHCKhB_izn9oV9-wTybP_h2oVQT9NJB3binNsOL3YWjp83rV8_6GuMDMP3dVF0eoIW0CIEOtuvD1AHrIQkkXyMfQz7UG316s-hzSVAK5SY0-lZos6mnaAVVqBIJodFpVNe5HE5clLKog8tAKZUCF7h7dtxkJlkEk1k3Nzo-AeNqtv3P-c-OCwGZiWNCRD3_p2VH_XiEIwEv7a7gHprDHKU_n9_icSZlW3IQzlYmHR1B9opRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8b9829e0.mp4?token=fqAOz3sfd-dJLK6wSNMy2c-xUYjy_vyDQ_7kOKTU4nzkhLF_J_ie_IldqXd-MvHKeFT1dUrkwxLC-kGHH27g5zTXkirCasc3ymLIA2MbNF0xuhI80NlgZ3ETTL9KPUn7lCxsYGSEBuKzy65Su_rtQCXTGlXfk6yqrZbhuY1Fm9f0_MbEfaxw9mMF311Ad5fMhrUbPwwYlFeDE0ckzJeACvnuHokTFBWOYHrE57fPUjZNiXTRZGco-o1Oq-aYkSTq3oV5qy_M5frRiE1TvcEK4LHbbR9VQxpddST0W4lf_6k4016yQfP0RKJB9yCOQFzMESsI1NpqMtXkAVlUKRTZHkhKs6da_6i2wk0wxNF3DZTEcSTJAhrjPmsoukNxlcQmUFfly_4xaJGa2PhwuKWxBZ0j9n1X-EJQCYMPu9S2bvXPylID5Gx-KhVFWx5eHCKhB_izn9oV9-wTybP_h2oVQT9NJB3binNsOL3YWjp83rV8_6GuMDMP3dVF0eoIW0CIEOtuvD1AHrIQkkXyMfQz7UG316s-hzSVAK5SY0-lZos6mnaAVVqBIJodFpVNe5HE5clLKog8tAKZUCF7h7dtxkJlkEk1k3Nzo-AeNqtv3P-c-OCwGZiWNCRD3_p2VH_XiEIwEv7a7gHprDHKU_n9_icSZlW3IQzlYmHR1B9opRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل توانیر: ۲۷ میلیارد تومان، پاداش گزارش ماینر پرداخت کرده‌ایم
.
@LorestanFars
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454714" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454712">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/626e29a2c6.mp4?token=R_lCuR4xZEYpczyQM14_M9T9Mvsn12PrxF140yrcSrssPMLzlOH3Mnw-UDrjTdDkJeISsmOkCWhrEkJxd2e-_q0CdB7dHXdQt7DfGVVxSCAoE7hrHxqqkDSJx9zEvdWXdhVhP6-__AtdAwM2D47fAsfKHpxFPQZJfEkMSV73JgspcI2OwbL5kDo9eEV2LqtzfuYc4koashnqCWKEdeakVwtQXXf2XjT3JRLkBXz4kGs5a1I_ugNUacMHviv3I6DOcFs8Vk3egjpL-2FC3OGDJZ7k0hiUZS1uCPGfSMMxdGxfOjodJO71wWiGkTodXBx-AIWL1XRi36YERPifGqMl-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/626e29a2c6.mp4?token=R_lCuR4xZEYpczyQM14_M9T9Mvsn12PrxF140yrcSrssPMLzlOH3Mnw-UDrjTdDkJeISsmOkCWhrEkJxd2e-_q0CdB7dHXdQt7DfGVVxSCAoE7hrHxqqkDSJx9zEvdWXdhVhP6-__AtdAwM2D47fAsfKHpxFPQZJfEkMSV73JgspcI2OwbL5kDo9eEV2LqtzfuYc4koashnqCWKEdeakVwtQXXf2XjT3JRLkBXz4kGs5a1I_ugNUacMHviv3I6DOcFs8Vk3egjpL-2FC3OGDJZ7k0hiUZS1uCPGfSMMxdGxfOjodJO71wWiGkTodXBx-AIWL1XRi36YERPifGqMl-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انفجار در منطقۀ صنعتی «جبل‌علی» در دبی
🔴
منابع محلی از شنیده‌شدن صدای ۳ انفجار در سواحل امارات عربی متحده و آتش گرفتن یک انبار یا مخزن سوخت خبر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454712" target="_blank">📅 12:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454711">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4ed34881.mp4?token=XVnlrmkWjM-VbbtJcQjTEyndfxi-0YV0k4yPUFHhJX1bgLpUXO3VOHKqr_fBhtio8IKjgXcyzYCA-2qJxDD6AbNBULNIT00xC1AQn-DFA3Cix5NISc6l3F5c_oSqRlaKlNFBXP9QyL55ly56Wideg73H7iMpGQBIMMIdF9LNeiBH_9mIueY-Devrg8Gfo9MHn3Q6XMHDKy7tF4vjVqGk6CF5Q4ISzeqvuceWk4Y8mqBZ14JmjEKqE-FEqMAsR_OTTIJq_9U4GtBHxxrA9vvrs77TPUfqTzEgAE3y4pdrcMsFKSmjXrKPtDFKIkyEajyaZcnQvQ9ghh4-UutA7nYrDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4ed34881.mp4?token=XVnlrmkWjM-VbbtJcQjTEyndfxi-0YV0k4yPUFHhJX1bgLpUXO3VOHKqr_fBhtio8IKjgXcyzYCA-2qJxDD6AbNBULNIT00xC1AQn-DFA3Cix5NISc6l3F5c_oSqRlaKlNFBXP9QyL55ly56Wideg73H7iMpGQBIMMIdF9LNeiBH_9mIueY-Devrg8Gfo9MHn3Q6XMHDKy7tF4vjVqGk6CF5Q4ISzeqvuceWk4Y8mqBZ14JmjEKqE-FEqMAsR_OTTIJq_9U4GtBHxxrA9vvrs77TPUfqTzEgAE3y4pdrcMsFKSmjXrKPtDFKIkyEajyaZcnQvQ9ghh4-UutA7nYrDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داداشم گمشده، شما ندیدینش؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454711" target="_blank">📅 12:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454710">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw_4ofSekNzEkrqlF7Uda5FohJrc3hNOeBuBYGscDdepRcyGDaQ3d7y6bdgFt8SHz5spGamX8ERKFpbZBFqqdbIHdBgtiF9blLAdfMAIlRHWH_uqL4sQQjRtM0Jzf6ZnY3fmvypE6dkcj6Cq8IhX4KN7gRPUD3HPzAQlV4l5QXIgzWJWn8SaNnXeKTUVka_7Zzq7EHzdv40f2KLqqEpjAnF1Dlt_vMxfhxJpdl4tJjEHkCRdTyICCwq_oCfJI3Btow0Oi3hbDG1DXI5sXYFFduFprS5sbtPhnyR2q2Di904hyCGaen9NlbaL6dTFbTixkLIDGvJfPa70_7fO4udVsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: دست نیروهای مسلح ما برای پاسخ به هر تهدیدی پُر است.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454710" target="_blank">📅 12:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454709">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سخنگوی ارتش: توان رزم ارتش بی‌وقفه درحال ارتقاست
🔹
امیر اكرمی‌نیا: با گذشت ۲ جنگ تحمیل‌شده از سوی دشمن، امروز ارتش در آمادگی کامل قرار دارد و با نوسازی سامانه‌های آسیب‌دیده، ورود تجهیزات جدید و تکیه بر توان داخلی، بی‌وقفه مسیر افزایش آمادگی عملیاتی را دنبال می‌کند.
🔹
ورود تجهیزات جدید به یگان‌ها، موجب شده تا ادوات و تجهیزات رزمی ارتش متناسب با نیازهای روز بازآرایی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454709" target="_blank">📅 11:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454708">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ons_9as3foT57pVm7rlJK_30Ev9li_BysGP-QaQzosACyjQPnkc1sdtbkgLlFagG2BvFvFHMO3KAhDmitGYrRdEOpfNaDOhXnvIxDZsSXfsbBbLr2FZnOHh7GwAUg3oZKwtTGBbhkAjVv7DLRGxRhdzMoyTafW6cBOfggUEVd6zQZZsglqYWF-e6jfljizV7IvjBxy-FIVdXUZnuQhLWR_0YAabT87i1CfOjXNvs7mGJRLbbxIFIwmfqHKrbvwjHUU3dnfjxcBN6Alck1Vl-GV6-XsvxU03w4SV7Wv9qeAj_C_z6K9MrYsqT-OZYc-jbdvQR4QUc94uoi7Lj2ThGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان: شخصیت آیت‌الله سیدمجتبی خامنه‌ای استثنائی است
🔹
این حرف‌هایی که برخی افراد درباره برخورد رهبر انقلاب با ما می‌گویند، هیچ نسبتی با شخصیت ایشان ندارد. @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454708" target="_blank">📅 11:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454707">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8jCbVgymNo7ITjwM4wlqA9FbGki03cNb9mp-GRLXtu5KR7TJ4m4ANkpe4Qa_NJGm2lgHlOaWMWSCNKK4NqvdYWiFRgwQxQpfhKRSwRGvzRbvvM-HUJ18qvEizFHwvJrk3tZiY0DcdMWc2Vle0XZjjXJMUlzvYtdP0mUUlvJk7TSyT2h3VaNin6oJg1MmNugL32_DtXLBU8dGM8GU-j0q5QYF-iD0hb1fr90eKvltt8SXNCMb5tgejXx1mh6hme-biYvuZAkVDHFwWjJ_aMO8jjgSwfx_jnJvMrgi90rABV6Y9HbOrzyk7nA9AEo2nY2PN7Sa8HvZiezFM1Y3crGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاییز پرباران در راه ایران
🔹
سازمان جهانی هواشناسی به‌تازگی اعلام کرده احتمال شکل‌گیری پدیدۀ النینو در تابستان ۲۰۲۶ حدود ۸۰ درصد است و این احتمال تا پاییز و زمستان به بیش از ۹۰ درصد می‌رسد.
🔹
النینو که با گرم شدن غیرعادی آب اقیانوس آرام شناخته می‌شود، معمولاً بارش پاییز و زمستان ایران را افزایش می‌دهد.
🔹
براساس پیش‌بینی‌های موجود، تمام ماه‌های پاییز از بارش بالاتر از نرمال برخوردار خواهند بود، اما اوج این بارش‌ها در ماه اکتبر (۱۰ مهر تا ۱۰ آبان) متمرکز شده است.
🔹
در این بازۀ زمانی، انتظار می‌رود سامانه‌های بارشی متعددی وارد کشور شوند و بخش‌های وسیعی از ایران، به‌ویژه نیمه شمالی، غربی و مناطق زاگرس را تحت تأثیر قرار دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454707" target="_blank">📅 11:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454706">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJakqV5eQOlPkruAXg9g0T3AxenKgyvSYFVBBu-b04xlYzeoGi9lhWbKKZEJB4DtWFYa9rF-6iRzwM-a4wQ59stK0Lbg7veBIaPUTdNsKe1WYhjoz1phEyyJDwEseqhhQmaAaTWUt9d-6tDsgVDd18OqQ_8zs8vScyqLbVJJZgQcxnr0F35Imi_Kb8P3EGs0LLCCEwbl5djilEWsLQwivg5V6SjmBuOsqIETgXTfS36DiTmc4xKmp6ulcjdBv1HSL_QU_xIPkc6skedL62uF0l0IVv2jI08mmricws1Gqew36IMjTUUoYg5XCrghbzWTaHl7OUr1RquVmfzE-dvLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی هوایی ارتش: در دفاع از ملت ایران جان برکف خواهیم بود
🔹
پیام امیر سرتیپ خلبان بهمرد به‌مناسبت سالگرد شهیدان بابایی و لشکری: محال است تاریخ ایران سربلند، سر به زیری و خشوع و تواضع نابغۀ جنگ، سرلشکر خلبان عباس بابایی را از یاد ببرد و چه دور از ذهن است فرزندان این آب و خاک، نام سیدالاسرای ایران، سرلشکر خلبان شهید حسین لشکری را مترادف با واژۀ آزادی ندانند.
🔹
در مسیر اطاعت از ولایت و دفاع از ملت بزرگ ایران در برابر تجاوز دشمنان قسم‌خوردۀ این بوم‌وبر، میراث‌دارانی خلف و رهروانی جان برکف خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454706" target="_blank">📅 11:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454705">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUvpzmR3aVDWHo7Rsg1TqMNcq3At4-O6wd3i8kFnU55HFC-_Jd4lbIrzY3xY8MSRI2vAT9wCK2t4ubZPn_02vPmLON7__E4KKsWDTh5qRNhMiRvJtwje646Avvb_oUpNIm4t3jfh76IQ_xhqcWDZL6mR_enwgyRzsV4fXI_az6-enyd2621K_VPX5lz6H6ojEracrWt7ODX9WObumfZzATr4Uq4lk_htDlWDFkNyA_smkscT2qoxIo_gZIpSdoOBN2jum6ileEmHzoMoWdfNOjCrhusFEnO5WUCE-PpMOSy9prVSHnAT-2pbocGlljvmO6b4W6frTbd52XElhrn5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا فاتح جام‌جهانی فوتبال شد
⚽️
اسپانیا ۱ - ۰ آرژانتین  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454705" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454704">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تمدید فرصت ثبت درخواست معافیت سربازی برای مشمولان دارای ۳ فرزند و بیشتر
🔹
سازمان وظیفهٔ عمومی اعلام کرد مهلت استفاده از معافیت خدمت سربازی برای مشمولان دارای ۳ و ۴ فرزند تا پایان سال ۱۴۰۷ تمدید شده است.  شرط سنی استفاده از این معافیت چیست؟
🔸
مشمولان دارای ۳…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454704" target="_blank">📅 10:49 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
