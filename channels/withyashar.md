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
<img src="https://cdn4.telesco.pe/file/J6r9tZxRO4eNbrP2lPqKH-RUN99cSDkWzpkN8GgCVLOJiefheeaat28s9bS-1dmjsem5Emjxwc4wlfNI51Ah_WL5hb_bj5NtpktWV3UgSnTy0-PsVcevBK219D19kueDwUQlL1xOfoMYCioomekLqJWdulzToze98Nq1Y8qeUHoWQENGOmbSfNdHOb8R-9MP9R-qpPjAjtFtmQuTeM76RmpA2x7AMUkVpdad0PaR1U12EpJDW1VGsvMTtluTlCSiisWGa18r3_-tdClU0_VBsmhJqBSuXD9Ko93jLV7jOfEQZhN1T838wEDkkk0zQhPjBhPhSUt_zwBrboWVjuAKDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 442K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 23:45:18</div>
<hr>

<div class="tg-post" id="msg-21300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رویترز : فرسودگی پایانه‌های نفتی ونزوئلا نفتکش‌ها را تا یک ماه معطل می‌کند
پایانه‌های فرسوده بنادر نفتی ونزوئلا عملاً باعث محدودیت صادرات نفت خام این کشور شده‌اند و نفتکش‌ها به دلیل زیرساخت‌های فرسوده، قطعی برق و مشکلات کیفی، مجبورند تا ۳۰ روز برای بارگیری منتظر بمانند.
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/21300" target="_blank">📅 23:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21299">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">همکنون
موج شدیدحمله هوایی اسرائیل و بمباران در جنوب لبنان کوه علی الطاهر
@WarRoom</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/21299" target="_blank">📅 23:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21298">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شما هر صدای که بگی‌ در تهران داره گزارش میشه
🤠
@WarRoom</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/withyashar/21298" target="_blank">📅 23:28 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21297">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">به گزارش گاردین ترامپ برای هرگونه اقدام اقتصادی جدید علیه ایران، ناگزیر خواهد شد شرکای تجاری ایران، به‌ویژه چین، را هدف قرار دهد؛ همین مسئله رویکرد آمریکا را دشوار می‌کند
سفر رئیس‌جمهور چین به آمریکا در ماه آینده نیز ممکن است تلاش‌ها برای اعمال فشار بر پکن درباره واردات نفت ایران را پیچیده‌تر کند
@WarRoom</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/withyashar/21297" target="_blank">📅 23:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21296">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چند گزارش از صدای تیراندازی در غرب تهران
@WarRoom</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/21296" target="_blank">📅 22:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21295">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جی دی
ونس به اسکای نیوز : حضور ارتش آمریکا در خاورمیانه ادامه دارد!
واشنگتن ابزارهای فشار لازم برای مقابله با ایران را دارد
@WarRoom</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/21295" target="_blank">📅 21:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21294">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbc6763df7.mp4?token=KoxOMHO2kK9CNYKH2bgrGABU2grl9VH_aNovY5cbZ2Om_FxUIQeAcCeA-l48HODUJZqYlloXamZvo0qSWWPCjGKCfLryWzG5CXKyrC3NNbMkTiZ7vtJyHKOgbZwuZ41A07seFGLdXTpusOnvNyKM-t0bipfzGXlYBb27TSvLJTq24Ky5uKnlamjSul8z2cKoJ8snwrH3PP__dhlhUeiskrP3Jhv0q3eBFIn4MKSVeDcR9CnV1mca0Wqq8cyl47laqzmn7b8mFJ3YhBXroSfcDSl_zAyncYfu0Ov5r8hlsv29MoKMzBkhqWsht9i22Pka7pJHJH9OVZiHUHb1Zci6vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbc6763df7.mp4?token=KoxOMHO2kK9CNYKH2bgrGABU2grl9VH_aNovY5cbZ2Om_FxUIQeAcCeA-l48HODUJZqYlloXamZvo0qSWWPCjGKCfLryWzG5CXKyrC3NNbMkTiZ7vtJyHKOgbZwuZ41A07seFGLdXTpusOnvNyKM-t0bipfzGXlYBb27TSvLJTq24Ky5uKnlamjSul8z2cKoJ8snwrH3PP__dhlhUeiskrP3Jhv0q3eBFIn4MKSVeDcR9CnV1mca0Wqq8cyl47laqzmn7b8mFJ3YhBXroSfcDSl_zAyncYfu0Ov5r8hlsv29MoKMzBkhqWsht9i22Pka7pJHJH9OVZiHUHb1Zci6vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشت صحنه فوتوشوت از ترامپ
@WarRoom
😁</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/21294" target="_blank">📅 21:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21293">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0YIDzqrexkdrTOWh7W90JvcUk4FNAJ30OVPk19ve8tZN1yQY9c0SGNqivTwUNzudwxD4O8MMiegQzPzW7IsaI9jbHWKyZcL9_o1bua3ZgHzds1MpAZ7XCaGrRxNEtMDPCtz9IgZv1dO3gDhJ1mNpDA7VVtXr16yJOlhRbcRNUI_HE0fHgZGI5iKvD4a5e7uqZKRlsRu8eypHUQUtMEhQ2IXGNZyIp7Lho1exKRLbUETy-d5JooEnXuCgaolBwVOP-E8Vea_5iLXKuoF9etAXYG43f3MxRwj9NzRWu2StNmiBKD7OMp-A8Emgat6Xq-XvbBNmpiqX5WRf7siQlSdKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث این مقاله را بازنشر کرد :
ترامپ از فشار همه‌جانبه بر ایران می‌گوید: «الحمدلله!»
دونالد ترامپ مدعی شد آمریکا
کنترل کامل تنگه هرمز
را در دست دارد و محاصره دریایی این کشور به یک «
دیوار فولادی
» تبدیل شده است. او گفت ایران دیگر
نیروی دریایی و نیروی هوایی مؤثری ندارد، بخشی از نیروهایش حقوق نمی‌گیرند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است
و رهبری جمهوری اسلامی نیز در وضعیت نامشخصی قرار دارد. ترامپ همچنین از
بی‌پولی و تورم ۳۰۰ درصدی
ایران گفت و مدعی شد جمهوری اسلامی دیگر «قلدر خاورمیانه» نیست و فقط حرف می‌زند. او تأکید کرد
آخرین کسی است که به ایران اعتماد می‌کند
و گفت اگر ایران اقدامی انجام دهد، با واکنش بسیار شدید آمریکا روبه‌رو خواهد شد. ترامپ در پایان گفت آمریکا اکنون در
«موقعیت بسیار خوبی»
قرار دارد و ایران پس از حدود ۵۰ سال دیگر «قلدر خاورمیانه» نیست و پیام خود را با عبارت
«الحمدلله!»
به پایان رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/21293" target="_blank">📅 20:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21292">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس:
به زودی با قدرت به محاصره دریایی آمریکا علیه ایران پاسخ خواهیم داد و آمریکا منطقه را ترک خواهد کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/21292" target="_blank">📅 19:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21291">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آکسیوس:
بازار نفت دیگر صرفاً با تهدید، وعده یا پست ترامپ معامله نمی‌کند؛
واقعیت میدانی تنگه هرمز، میزان واقعی اختلال در صادرات و عبور نفتکش‌ها اکنون تعیین‌کننده‌تر شده‌اند.
این موضوع همچنین برای ترامپ از نظر سیاسی اهمیت دارد، چون کاهش واکنش بازار به اظهاراتش می‌تواند توان او برای تأثیرگذاری فوری بر انتظارات انرژی را کاهش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/21291" target="_blank">📅 19:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21290">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07a22b837.mp4?token=F6m5ZiOcQU3oZsa2DpGQfqPGE2VxsKnpWBjS8t2__VlVFD0-pxBb-d_6FMDq4bKRpPxu-fMjsue2lDm0QSYoxFy1r9Tri_neb0dqZKuoIP5No8k2OSWm9zIQAq7f2KG5NvKqXKKs2VDGNDFMsDYqe5lNEdwt3dtncDySaJ4J8Huis9zfBG7iuX5CiZGfDyzI4Q-iSUeyqf144s6PNNO5gl_xGCkyb9h7pQ_WEoOOzGLhvEwWFgL124giR7a7lpndd8ObYp9owoXA-P1nbC9Rc0gPd73dpsDG1Q8okwrWOkIstv2c8cfTRqic7xdDiNK28kYEaCod78VhX6lGtqfMY3i5Er0xaCbUDbfAM_68tCPLsDd80Uomp4odysWnZ-xF4wjM0ubRiiQAX4dUh6q67dmo1XAuRiHc7C1UGCaRCOw-hAWBAf0kiEoTL7qOxRVV0HSl1ZVmPC3fRmsNeXOIddI_t4sYEcskP-PYrBLpjtLgDCzbFaxLhDRMjVV6WhTJbEwQJNGIaFJuvIeyrJGKGCb1NJsFVFyf2e4RZoL2TL8GvMs9bHmlpy_nl6jqhxke4SSX5cT6CoR1OO8Bb-gqTHDcE_pUuUioiV0SzX3amLYJsHsyeIL-MNwpp5yrXHHoUEh7WZcAMFkXIRSNQLm4xdK0usT6K1QA91gfv-PLECQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07a22b837.mp4?token=F6m5ZiOcQU3oZsa2DpGQfqPGE2VxsKnpWBjS8t2__VlVFD0-pxBb-d_6FMDq4bKRpPxu-fMjsue2lDm0QSYoxFy1r9Tri_neb0dqZKuoIP5No8k2OSWm9zIQAq7f2KG5NvKqXKKs2VDGNDFMsDYqe5lNEdwt3dtncDySaJ4J8Huis9zfBG7iuX5CiZGfDyzI4Q-iSUeyqf144s6PNNO5gl_xGCkyb9h7pQ_WEoOOzGLhvEwWFgL124giR7a7lpndd8ObYp9owoXA-P1nbC9Rc0gPd73dpsDG1Q8okwrWOkIstv2c8cfTRqic7xdDiNK28kYEaCod78VhX6lGtqfMY3i5Er0xaCbUDbfAM_68tCPLsDd80Uomp4odysWnZ-xF4wjM0ubRiiQAX4dUh6q67dmo1XAuRiHc7C1UGCaRCOw-hAWBAf0kiEoTL7qOxRVV0HSl1ZVmPC3fRmsNeXOIddI_t4sYEcskP-PYrBLpjtLgDCzbFaxLhDRMjVV6WhTJbEwQJNGIaFJuvIeyrJGKGCb1NJsFVFyf2e4RZoL2TL8GvMs9bHmlpy_nl6jqhxke4SSX5cT6CoR1OO8Bb-gqTHDcE_pUuUioiV0SzX3amLYJsHsyeIL-MNwpp5yrXHHoUEh7WZcAMFkXIRSNQLm4xdK0usT6K1QA91gfv-PLECQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوندی در تجمعات شبانه: هنوز که از بغل بیت رهبری رد میشیم بوی گوشت سوخته آقا میاد!
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/21290" target="_blank">📅 18:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21289">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دفتر نخست‌وزیری اسرائیل:
اردوغان یک دیکتاتور یهودی ستیز است که کردها را قتل عام کرده، تروریست های حماس را در خود جای داده است، نیمی از قبرس را اشغال کرده است، و تعداد روزنامه نگاران و سیاستمداران مخالف خود را به زندان انداخته است.
او اکنون به دنبال گسترش تجاوزات خود به اسرائیل به سوریه است. اسرائیل آن را تحمل نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/21289" target="_blank">📅 18:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21288">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLau5sI7AUZOrknBw-K-PS9A-ncTT65XLr3yUUTSrlvmjAqeuzwU8gsfg_vhZylv82FsSLheV4djfc8UagnUzHU5MHpgAO1ievbGy1bIFJXl3Mm7KkaxNP0B-odNBuVGn8p79OoD15toIE2KJPJa-WqYVW5Ea2TBuj6CPGkARp-iC4PtJUvVpJtDhQMcVqZ2SEPu13FlFTp2alh_p_ZFcTHnYqm3ftVPtV3k0nb3W1LP6gW7Lem42jEgbYNFAOmly_zNI-CcNW_aUB4oecLdgBvJ3XA2OmAbRJhYqASrNcA_ywMFbvlgJaolDyEnR5ruuHaS8JKiQ5V-iMAM77UYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحرکات جدید در العدید؛ ۴ سوخت‌رسان آمریکایی و ۵ فروند C-17 قطر در پایگاه
تصاویر ماهواره‌ای Sentinel-2 که امروز ثبت شده، حضور چهار هواپیمای سوخت‌رسان نیروی هوایی آمریکا در پایگاه هوایی العدید قطر را نشان می‌دهد.همچنین پنج فروند هواپیمای ترابری راهبردی C-17 گلوبمستر III نیروی هوایی قطر به العدید بازگشته‌اند؛
این نخستین بار از ۱۲ ژوئیه است که حضور این هواپیماها در پایگاه مشاهده می‌شود.
بازگشت همزمان هواپیماهای ترابری قطری و تداوم حضور سوخت‌رسان‌های آمریکایی، از ادامه فعالیت‌های هوایی در العدید حکایت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/21288" target="_blank">📅 17:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21287">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امام جمعه رشت : برای افزایش جمعیت از مردم میخوام دست به دست هم بدن و به همدیگه کمک کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/21287" target="_blank">📅 16:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21286">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7e5ce77a.mp4?token=laY5b_ehKAg0qBRq1CI_ZUSkPXFpKE64DArJwgYXVOK6XvaDbXNqggxpt2zzF0_Aew7XgnINq5PlX_ON1xkTloeLDHWD7NWgxcjsOFPx_M0LrH9b3ezYR2YOSspYIc-xVQtnmr5d-MLRZgXHTVH9vwMt3yGsY3W0TfWETmiCCq0k--YKRyaVXb2Y_06jU_I-oPS2-GnyUBu5DacG5a72JowCwU1mc-0XHu0eSsTVftttlB2aCtCQTJs4zZf1fJzDbJUkiEW01o7_g5mspCVfbNFpkQfOMw9btcQ1N76zZD4BMxv40YL2Lt3YexPrAFAi47SB9NwpQbkD7Z0111IklEr31g43kgBV6nmjiadbeEIKNUfWVbwPsgjVmJ-Dm2XHqsqbwOXd56oi3t6JAS3VxM_OCvprtldVWS402HhKpHTxvQphHPeCU5JRWk-OWpucgsfMhWb6AFCZQtZ66hcin0NKKI1K6mGaNtGPFrDWrEumk0WRvhHduEFuKRfjx6Lax6XNtCYS1mXW4PtjbwowH3SHuPYuT9S71za0LuG8QR9oZ75yCdrb3Ipok6phF3rO5IcDwLWQ4UvQaYySdz0jjSnQPBng4gzsjQhiP_P7XsQQonA_odvL_LJK7vSxHMGLwlIZAyrC3n3CWLvqlzAFd1BJcHX_p9fYEW0hbwRZBSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7e5ce77a.mp4?token=laY5b_ehKAg0qBRq1CI_ZUSkPXFpKE64DArJwgYXVOK6XvaDbXNqggxpt2zzF0_Aew7XgnINq5PlX_ON1xkTloeLDHWD7NWgxcjsOFPx_M0LrH9b3ezYR2YOSspYIc-xVQtnmr5d-MLRZgXHTVH9vwMt3yGsY3W0TfWETmiCCq0k--YKRyaVXb2Y_06jU_I-oPS2-GnyUBu5DacG5a72JowCwU1mc-0XHu0eSsTVftttlB2aCtCQTJs4zZf1fJzDbJUkiEW01o7_g5mspCVfbNFpkQfOMw9btcQ1N76zZD4BMxv40YL2Lt3YexPrAFAi47SB9NwpQbkD7Z0111IklEr31g43kgBV6nmjiadbeEIKNUfWVbwPsgjVmJ-Dm2XHqsqbwOXd56oi3t6JAS3VxM_OCvprtldVWS402HhKpHTxvQphHPeCU5JRWk-OWpucgsfMhWb6AFCZQtZ66hcin0NKKI1K6mGaNtGPFrDWrEumk0WRvhHduEFuKRfjx6Lax6XNtCYS1mXW4PtjbwowH3SHuPYuT9S71za0LuG8QR9oZ75yCdrb3Ipok6phF3rO5IcDwLWQ4UvQaYySdz0jjSnQPBng4gzsjQhiP_P7XsQQonA_odvL_LJK7vSxHMGLwlIZAyrC3n3CWLvqlzAFd1BJcHX_p9fYEW0hbwRZBSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما: نتانیاهو خیلی مرده؛ نه خسته شده از جنگ با ما، نه پشیمونه و هرآن ممکنه بهمون حمله کنه و بنظرم خیلی مرده.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21286" target="_blank">📅 15:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21285">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترکیه، حکم بازداشت اینترپل قرمز برای  نتانیاهو صادر کرد و او را به عنوان متهم در ارتباط با حادثه "ناوگان مقاومت" عنوان کرد
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21285" target="_blank">📅 15:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21284">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba907831b.mp4?token=Kmhs4clyMbDnwYswN7DdE4993gH9wCzDHRljWHMVt6lFctJmL4idqBe6T4F1J1zSEtGb28p0_6ReAQX_wakO95U-sF1hoIM1rALPePlqLVbzT1UPvfGuoE4fKn-BCi6GAB27KmXZN1s7sDyX47k6IY2_gkSupLAfJcftHSdyoHgbFs8wDeAzR8tKxV2wkRwq2b-Sfzy52p2oVEntc7UJDAZBzxmmIIxb0iJcYENQzS390tYH24Rk8Gm-PS5MZSmQrp7OxDtNqTVcGVCFEBuF_-D82dC-2i4b-i_rkSgmXJxw5SKjy9Dhk2zmUZunKOsMx9Ty0NNjA0bTdhe1JfiwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba907831b.mp4?token=Kmhs4clyMbDnwYswN7DdE4993gH9wCzDHRljWHMVt6lFctJmL4idqBe6T4F1J1zSEtGb28p0_6ReAQX_wakO95U-sF1hoIM1rALPePlqLVbzT1UPvfGuoE4fKn-BCi6GAB27KmXZN1s7sDyX47k6IY2_gkSupLAfJcftHSdyoHgbFs8wDeAzR8tKxV2wkRwq2b-Sfzy52p2oVEntc7UJDAZBzxmmIIxb0iJcYENQzS390tYH24Rk8Gm-PS5MZSmQrp7OxDtNqTVcGVCFEBuF_-D82dC-2i4b-i_rkSgmXJxw5SKjy9Dhk2zmUZunKOsMx9Ty0NNjA0bTdhe1JfiwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز : ایران کم‌کم متوجه می‌شود که رئیس‌جمهور ترامپ و ارتش آمریکا در خارج کردن مخفیانه نفت از تنگه هرمز تا سقف ۱۰ میلیون بشکه موفق هستند.
بعضی شب‌ها به ۱۵ تا ۲۰ میلیون بشکه می‌رسد... این جریان قبل از جنگ است!
حتی سی‌ان‌ان هم مجبور شد اعتراف کند: ایران در حال از دست دادن کنترل خود است
همچنین رئیس‌جمهور ترامپ جبهه دیگری را باز می‌کند و کشورهایی را که به تهران کمک کردند تا سرپا بماند، تهدید می‌کند.
چیزی از ایران باقی نخواهد ماند.
ملاها این را خواستند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21284" target="_blank">📅 14:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21283">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ای‌بی‌سی‌نیوز: FBI از احتمال حمله پهپادی ایران به کالیفرنیا خبر داد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21283" target="_blank">📅 13:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21282">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کارشناس صداوسیما:
علی خامنه‌ای یک پله از امام علی پایین‌تر بود و معجزه هم میکرد.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21282" target="_blank">📅 12:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بیتکوین 77,000$ را شکست و در چند روز 15000$ گران شد @WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21281" target="_blank">📅 12:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21279">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfUUQ04jf6tN0muTtiT8KuU7oDhg-w6ohKlkftwLvY93MMzOMGP_1APwV_eSfss8SsNSUp4dO-3AfT6SNREJ_8xJL_5dHasK12ZMXSw9KKQfL2BQhpjI_E5v1hOJDfrqcBo76hszu1jeVuvFEwaSrnDIyz927k1FDAFPZnEQeeShEGGE1h0Fi5vdFxseOYwnujzigAq_fkRyMdXnCjSO5u5o7ZCvdWKls7FVXOp-9tf7VBSE9PATsA0gEoVWKCpH1fCEssqrnAkwXZKeZIux_j1K1ABQNkZ8F7Gl_zHeAUR1egUPehok4_UUvsE_vy9fzuTi1jNjRxGAkB3vSutkFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3MSWIurcaXzRgKjEkwpBkEVZ3i4wN829D54JN_1HR6ZyD3OtX3stAYpw86ABVl8mj8EZtjHX30q-nrgbO1vl0HWJyXBjwYERNl8C0mkK8SqnW8gFEOFya8v6uEVS9DTXcERTegU01S_vpEAB9FuGyZnsm1cvrhQm1nzyA-hM-8BRoWqF7g3FhZ23DgaP1mw_6zVhF_a9IofMNa0Lv04o-b4acEi3--OFWEnHmTq8t1GW5veKeDDP8SoaWB6ywnqvf9YqbvgjNe_igr28_5kqYj6N1nv0g9X33CIjJf9JwubaI8I4e5uCtyzPbEfe3reBYOFg83k89wTU-gqJRRzjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیشب یک هواپیمای بویینگ E-3B سنتری  AWACS آلارم 7700 وضعیت اضطراری روشن کرد. ولی اکنون یک هواپیمای دیگر با همان مدل و مشخصات به پرواز در آمده که نشان می‌دهد که آمریکا تجهیزات کافی پشتیبانی در منطقه بسیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21279" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21278">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بیتکوین 77,000$ را شکست و در چند روز 15000$ گران شد
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21278" target="_blank">📅 11:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21277">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce_U_sMlafUnrSkE7QUL413vONFtYOqyXYNQJvliB5WaplaEy4_QkKoagt1BGHKUwRtNJOLe6sKz95-1SGqqRE2oLaWZqCdf_ZNhoKsdbrS3DvVCReMSMXFwRj4TTYZVgbcIeU0Sr0kL-llFoY0q0TsPDS7sMLyzlh_zg6eVn5K_m4ieS6o3EPeFxAKauT2VWQpj8dcj5W7PAENaYVnUM16ggFa4m215GRJ95GjI75zoOFUQQe6W2FzVhpS_wPsaZQ75JZpDkGuUXWg2rd1416v3WoEtM71Fh6eMv1IJScXGUn8M-fihKY_OUmwFg2zGknfPkkR49XXYPP1iHLi3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده، دومین هواپیمای تانکر سوخت‌رسان را از مجموع شش فروند هواپیمای جدید، به نیروی هوایی اسرائیل تحویل داد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21277" target="_blank">📅 11:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21276">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش های بسیار از چندین صدای پرتاب از سیریک ، خونه ها لرزیدن و صدای انفجار از تنگه و صدای جنگنده ، همون فرمولی که گفتم جمهوری اسلامی میزنه نفت بره بالا  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21276" target="_blank">📅 11:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21275">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏سقوط چشمگیر تردد در تنگه هرمز؛ تنها ۷ کشتی باری در روز پنجشنبه عبور کردند.
‏داده‌های شرکت ردیابی دریایی کپلر نشان می‌دهد تردد کشتی‌ها در تنگه هرمز روز پنجشنبه به نصف روز چهارشنبه کاهش یافت و تنها ۷ کشتی باری، شامل ۴ کشتی ورودی و ۳ کشتی خروجی، از این گذرگاه راهبردی عبور کردند. هیچ‌یک از این شناورها نفتکش یا حامل گاز طبیعی مایع نبودند، هرچند یک کشتی بسیار بزرگ حامل پروپان و بوتان از مسیر ایران از تنگه خارج شد. پرزیدنت ترامپ نیز طی روزهای اخیر بارها تأکید کرده است که ایالات متحده کنترل تنگه هرمز را در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21275" target="_blank">📅 10:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21274">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏کانال ۱۴ اسرائیل: ترکیه با وجود هشدارهای نتانیاهو، محموله نظامی دیگری به سوریه فرستاد.
‏بر اساس این گزارش، ترکیه محموله تازه‌ای شامل حدود ۲۰۰ خودروی نظامی، از جمله ۲۰ تانک، به سوریه اعزام کرده است؛ اقدامی که با وجود هشدارهای نتانیاهو درباره تحرکات نظامی ترکیه در سوریه انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21274" target="_blank">📅 10:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21273">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رویترز: در تهدید ترامپ علیه کسانی که به ایران کمک می‌کنند، حتی متحدان واشنگتن که در میانجیگری مذاکرات صلح نقش داشته‌اند هم ممکن است در این دایره قرار بگیرند و آن را شامل هر کشور یا نهادی کرده است که به تهران آنچه را او «شریان حیاتی» توصیف کرده، ارائه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21273" target="_blank">📅 10:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21272">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21272" target="_blank">📅 09:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21271">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDr.t</strong></div>
<div class="tg-text">کجایی ؟ داشتم نگران میشدم</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/21271" target="_blank">📅 09:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21270">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ : ما گزینه دیگه‌ای جز جنگ با جمهوری اسلامی نداشتیم و اگه لازم باشه ۱۰۰ بار دیگه‌ هم اینکارو تکرار میکنم چون آنها نباید به سلاح هسته‌ای برسند!
جمهوری اسلامی به کشورهای بی‌طرف مثل عربستان، قطر، امارات، کویت و بحرین حمله کرده!
اگه برجام رو پاره نمیکردم، الان سلاح هسته‌ای داشتند و ازش علیه همه کشورها استفاده میکرد!
رسیدن به توافق با آنها اصلا آسون نیست چون درحال حاضر هیچکس نمیدونه دقیقا چه کسی داره رهبری میکنه!
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21270" target="_blank">📅 09:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21269">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سخنگوی پنتاگون به وال استریت ژورنال: ما تمام امکانات لازم را برای شروع حملات به ایران  را در زمان و مکانی که رئیس جمهور تعیین می‌کند، در اختیار داریم و هیچ کمبودی نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21269" target="_blank">📅 09:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21268">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_R43Rrd4jAVqw7IOi0bZqgI-7cQJ3HpR7ET-DpfbJsvVG3-YBidRAP0CTQ4_imylWjk3SaqGFhTJta6li0gD2ngsVtVeVCc_Sx2Pn2uKoNx2DV66D8H30oiKRiIp6difLRTgTUTb4NSQ7brJUV8329P6PHfSuxoE4dc3n3Ac4nsu5ArxmF2EyDub_DrV37bzDsymOiu7A32Nv6zONujKEwmb9--iZyDF33Ij-cissNhHEVq6OftC9rl6wwZmkQUUGBHcDyLqL5zKYkGKSUhsDTrJTn2IQEId59Vr0q2wUmTtKXaMVsMNBGkziy9G1RYVHsniKzGCeD3jwTIEDxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزند مرفه رژیم جنایتکار ایران برای فرار از بازداشت ICE و بازگشت به زندگی لوکس در لس‌آنجلس پول جمع می‌کنند.
یک فعال ایرانی‌تبار که در جریان اعتراضات ایران بر اثر شلیک سپاه یک چشم خود را از دست داده، از
سید عیسی هاشمی، پسر معصومه ابتکار، معروف به «مریم جیغ‌زن»
، انتقاد کرده است. هاشمی ۴۳ ساله که از سال ۲۰۱۰ در آمریکا زندگی می‌کند، چند ماه پیش توسط
ICE
در کالیفرنیا بازداشت شده و روند لغو گرین‌کارت و اخراج او در جریان است؛ اقدامی که بنا بر گزارش با دستور
مارکو روبیو
انجام شده است. او اکنون با راه‌اندازی کمپین
GoFundMe
از مردم آمریکا کمک مالی می‌خواهد تا بتواند در این کشور بماند و به زندگی خود در لس‌آنجلس ادامه دهد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21268" target="_blank">📅 09:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21267">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ در تروث بازنشر صحبتهای مقام ارشد کاخ سفید ، استفن میلر: او (ترامپ) ناامن‌ترین مرز تاریخ آمریکا را تحویل گرفت و ۱۵ ماه پیاپی، ورود غیرقانونی به کشور را به صفر رساند؛ برای انرژی و زنجیره‌های تأمین آمریکا دستاوردی تاریخی رقم زد، با کارتل‌های مواد مخدر مقابله کرد و آن‌ها را سازمان‌های تروریستی خارجی اعلام کرد؛ مانع دستیابی ایران به سلاح هسته‌ای شد؛ با ساخت خطوط لوله و افزایش تولید انرژی، قیمت بنزین را کاهش داد؛ تورم را به ۲ درصد رساند و با تصویب بزرگ‌ترین کاهش مالیاتی تاریخ آمریکا، مالیات بر انعام، تأمین اجتماعی و اضافه‌کاری را لغو کرد؛ یک پیروزی بزرگ و تمام‌عیار.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21267" target="_blank">📅 00:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21266">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک مسئول دولت ترامپ به واشنگتن پست:
ایران "کاملاً ورشکسته" است و ترامپ ابزارهای متعددی در اختیار دارد که می‌تواند در هفته‌ها و ماه‌های آینده از آن‌ها به شکلی قوی‌تر استفاده کند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21266" target="_blank">📅 00:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21265">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حملۀ هوایی اسرائیل به ارتفاعات علی‌الطاهر در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21265" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21264">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کانال 14 اسرائیل: مجتبی خامنه‌ای «
ایزوله
» شده و سپاه کشور را اداره می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21264" target="_blank">📅 00:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21263">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ارسالی تایید نشده : یاشار همین الان اهواز صدای شلیک موشک میومد قشنگ ی دودی توی هوا معلوم بود ولی دوربین گوشی اینقدر قوی نیست که بتونه دود رو بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21263" target="_blank">📅 23:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21261">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cf8ca15a.mp4?token=rW5zPafrKOpCK-H1cpIFQxMXC4rMFDQxV5K5wtBVCycpa7Pg8lH6GsMWsPAdvzthCtm86pNxEd8HGIJNfm6ffbQTRXZrV4M6s1jB31YSf-VqsGclkdU887WPzYtuuKeEJAA6FqLc-q6xJH17FaPq5PRhx_N-TLxs-eysJnl7vpKKPSzBGXKvQsQbCkb21RQSgoVXohcLPqBdgTo76Rv9O7zKaigTbH5_BWQLvsxs9A1rglmWa6XhbEWDjXKWpneuplBaGZMDLKD5zZ2RRcIjzj432ekvwXVJv8VS8zJy2y9P_bAccOuZxpprzExdBtfZ5Qdxlgx7uVHrzBFDzAMRhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cf8ca15a.mp4?token=rW5zPafrKOpCK-H1cpIFQxMXC4rMFDQxV5K5wtBVCycpa7Pg8lH6GsMWsPAdvzthCtm86pNxEd8HGIJNfm6ffbQTRXZrV4M6s1jB31YSf-VqsGclkdU887WPzYtuuKeEJAA6FqLc-q6xJH17FaPq5PRhx_N-TLxs-eysJnl7vpKKPSzBGXKvQsQbCkb21RQSgoVXohcLPqBdgTo76Rv9O7zKaigTbH5_BWQLvsxs9A1rglmWa6XhbEWDjXKWpneuplBaGZMDLKD5zZ2RRcIjzj432ekvwXVJv8VS8zJy2y9P_bAccOuZxpprzExdBtfZ5Qdxlgx7uVHrzBFDzAMRhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملانیا ترامپ، بانوی اول: شنیدم دلتان برایم تنگ شده بود. من اینجا هستم.به کاخ سفید خوش آمدید
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21261" target="_blank">📅 23:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21260">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏تانکر ترکرز:‏ دلیل اینکه دیگر در خارک شاهد بارگیری‌های زیادی نیستیم، این است که تولید نفت خام ایران در ماه‌های اخیر به سطحی کاهش یافته که فقط اندکی بالاتر از میزان مصرف پالایش داخلی این کشور است. این یعنی ایران در حال حاضر فشار چندانی برای صادرات نفت ندارد.
‎
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21260" target="_blank">📅 23:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21259">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/471bef475d.mp4?token=uoMGAt73FOgbjG2bz-Fg8B2ps9Z9NUvKM02lOozh5babYOY3vdB5sFqhvKj3LzWBP2HtkMzMHkWtGRL9frtTQrbp5ct_KG3Dna8rstIR3yaoQNgz40ewFGT1_GgKBy8OMhTNbE9Ndytsjl_Fhl2fgWX2ynBlywzoQ7Yv4K3PnfV_gUcrG5VccTOJLmZvFql4WS5QUhyU1J_66T275TDeO2Mhe2W4c_nItFT4tVP65rdSPCP7iY9A0_aG72QiHtGfvmwsuVe4CXIqSY7B86TB4zItRJzxaRmgyy5AtymLoKQl1enUip4MMap2Mw8T4Yw2J7dth3T5Vww-VLQfYGG7cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/471bef475d.mp4?token=uoMGAt73FOgbjG2bz-Fg8B2ps9Z9NUvKM02lOozh5babYOY3vdB5sFqhvKj3LzWBP2HtkMzMHkWtGRL9frtTQrbp5ct_KG3Dna8rstIR3yaoQNgz40ewFGT1_GgKBy8OMhTNbE9Ndytsjl_Fhl2fgWX2ynBlywzoQ7Yv4K3PnfV_gUcrG5VccTOJLmZvFql4WS5QUhyU1J_66T275TDeO2Mhe2W4c_nItFT4tVP65rdSPCP7iY9A0_aG72QiHtGfvmwsuVe4CXIqSY7B86TB4zItRJzxaRmgyy5AtymLoKQl1enUip4MMap2Mw8T4Yw2J7dth3T5Vww-VLQfYGG7cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن وارد مرحله جدیدی در قبال ایران شده که در آن
فشار اقتصادی مؤثرترین ابزار آمریکا
است. ونس گفت ایران در دو هفته گذشته فشار اقتصادی بیشتری نسبت به آمریکا متحمل شده و واشینگتن قصد دارد این فشار را ادامه دهد. او تأکید کرد تأسیسات هسته‌ای ایران نابود شده‌اند، اما هدف آمریکا ایجاد
«واقعیتی جدید»
است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21259" target="_blank">📅 23:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21258">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c77add985.mp4?token=Zw9Xn0gn5eH-QZxJ2hMwKb4gbV72fH0_-HZgSC_BE1qxpr7srbi3zVNuq1F7FWEV4d5k8pbBC7uGHwPtwwjUbE3EG1lBoCeMnpHHc3HsPEsmjxDkgJzvCV_ipiOe7JPi4KLKBweJibSJocpQadtKAWQi4KoVvxbtsfpm4-KGquiWKK2NMqcIMzJPb7WVdGMBSyPeNKasmnGEOuodA-OYae7jckzg4sP8Gz9QbaHgjTqBQ0ZNrnMcPZ4OIlh4wkQvvyVPKb_VoEfavCRdbQDGbS4lRa3CNyPkraSfp-oMP0jAZty0h6alsql_Xu1lPozFXBKAvuVIy4fqjN-4ojlI2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c77add985.mp4?token=Zw9Xn0gn5eH-QZxJ2hMwKb4gbV72fH0_-HZgSC_BE1qxpr7srbi3zVNuq1F7FWEV4d5k8pbBC7uGHwPtwwjUbE3EG1lBoCeMnpHHc3HsPEsmjxDkgJzvCV_ipiOe7JPi4KLKBweJibSJocpQadtKAWQi4KoVvxbtsfpm4-KGquiWKK2NMqcIMzJPb7WVdGMBSyPeNKasmnGEOuodA-OYae7jckzg4sP8Gz9QbaHgjTqBQ0ZNrnMcPZ4OIlh4wkQvvyVPKb_VoEfavCRdbQDGbS4lRa3CNyPkraSfp-oMP0jAZty0h6alsql_Xu1lPozFXBKAvuVIy4fqjN-4ojlI2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل و شاباک فاش می کنند: سازمان تروریستی حماس در بیمارستان «ناصر» در خان‌یونس بازجویی‌های امنیتی و شکنجه انجام می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21258" target="_blank">📅 23:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21257">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ادعای نیویورک تایمز :
ناو هواپیمابر
آبراهام لینکلن
پس از حدود
۹ ماه استقرار و ۲۷۲ روز مأموریت
در خاورمیانه، که بخش قابل‌توجهی از آن در پشتیبانی از عملیات آمریکا علیه ایران گذشت،
منطقه را ترک کرده و در مسیر بازگشت به سن‌دیگو قرار دارد
. این ناو در
۲۱ نوامبر ۲۰۲۵
از سن‌دیگو حرکت کرده بود و هزاران ملوان آن تقریباً تمام این مدت را در دریا سپری کردند.
ناو هواپیمابر جورج واشینگتن
که از ژاپن به سمت غرب حرکت کرده بود، اکنون وارد منطقه سنتکام شده و قرار است جایگزین لینکلن شود.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21257" target="_blank">📅 23:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21256">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش های بسیار از چندین صدای پرتاب از سیریک ، خونه ها لرزیدن و صدای انفجار از تنگه و صدای جنگنده ، همون فرمولی که گفتم جمهوری اسلامی میزنه نفت بره بالا
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21256" target="_blank">📅 22:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21255">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تنگه بدجور دعواشده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21255" target="_blank">📅 22:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21254">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اد
میلیبند وزیر خارجه بریتانیا دیروز
از طرح اسرائیل برای ساخت‌وساز در منطقه
E1 در کرانه باختری
انتقاد کرد و آن را اقدامی «غیرقابل‌قبول و مخرب» خواند. او از اسرائیل خواست طرح را پس بگیرد و گفت بریتانیا در واکنش به گسترش شهرک‌سازی، اقدامات و تحریم‌های هدفمند بیشتری را بررسی می‌کند.
در پاسخ،
ایتامار بن‌گویر امروز،
در شبکه اجتماعی ایکس خطاب به او نوشت: «کسی باید اد را به‌روز کند که قیمومیت بریتانیا بر سرزمین اسرائیل در سال ۱۹۴۸ پایان یافت و اسرائیل کشوری مستقل است» و سپس با کنایه به میلیبند گفت به جای «بازی با دوران قیمومیت»، به لندن نگاه کند که به گفته او «به‌سرعت در حال تبدیل شدن به یک خلافت اسلامی است».
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21254" target="_blank">📅 22:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21253">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncNN9Tkh24BA2PLslH6JcvQepiFNNcgaD8KAa_-8ZVi34pHRhYwIBxzMoJSYi8aVSGpKMGtXNY4mKtzw6wl8cvAb3ViI7QUHOtArbLanbImff126L8cUYrAdCioAh-6IBqWlHzAh6JVXTF1rfR-AWYYWn9hs2-Up5IM9GZdAV5xXKGRZmdUjIL6QKj9GkpJyJwHlHJ1YpadVE2CDk3uqBw2fQLYmTD1kB0oyr-DuwQnspeYkVarXNY7zve0-7NyAmjZ_9eIYOKXAP-O4oz5bJI-oVQLwdmXRkx-lwNPl3n5w_iWb9iGUaU9E-ylJGskcX3T-nIXsr1tVZxzCOGWyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظر یک کاربر اتاق جنگ
🫱🏼‍🫲🏽
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21253" target="_blank">📅 21:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21252">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بر اساس بیانیه‌ای که دقایقی پیش در وبسایت وزارت خزانه‌داری ایالات متحده منتشر شد، ۹ شهروند با پاسپرت ترکیه و یک شهروند ایرانی با نام مسعود مسافر به‌ظن ارتباط با حزب‌الله لبنان یا نیروی قدس سپاه به فهرست تحریم‌های ایالات متحده افزوده شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21252" target="_blank">📅 21:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21251">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کانال 15 عبری : نتانیاهو در حال حاضر جلسه‌ای خصوصی با حضور روسای سازمان‌های امنیتی، از جمله سازمان‌های اطلاعاتی، برگزار می‌کند تا در مورد تمام تحولات آتی، به ویژه در سوریه و در روابط با ترکیه، بحث و تبادل نظر کنند. این اقدام در پی اعلام ترک‌ها مبنی بر ادامه فعالیت‌هایشان در سوریه صورت می‌گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21251" target="_blank">📅 20:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21250">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
دوشنبه جزئیات اقدامات جدید را اعلام می‌کنم. اگر سیاست
حداکثر فشار اقتصادی
ادامه یابد، فعلاً احتمال آغاز دوباره عملیات نظامی گسترده کم است. آمریکا در عین حال کنترل تنگه را در اختیار دارد و می‌تواند جریان انرژی را مدیریت کند. ما در حال اجرای
بزرگ‌ترین عملیات هماهنگ انزوای اقتصادی در تاریخ جهان
هستیم و به کشورها هشدار می‌دهیم که اگر به تجارت، انتقال پول، خرید نفت یا انتقال کشتی‌به‌کشتی با ایران ادامه دهند، با تمام توان تحریمی آمریکا مواجه خواهند شد. هدف،
درهم‌کوبیدن اقتصاد این رژیم جنایتکار، قطع توان مالی آن برای حمایت از نیروهای نیابتی و تأمین هزینه‌های نظامی
است. بسنت تأکید کرد: «این روش در همه جا جواب داده؛ ما یک ضربه دوگانه شامل
محاصره و سخت‌ترین تحریم‌های تاریخ
وارد می‌کنیم و
در ایران نیز موفق خواهد شد. ما این رژیم را فرو خواهیم ریخت.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21250" target="_blank">📅 20:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21249">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بسنت ، وزیر خزانه‌داری آمریکا:  ما نظام ایران را سرنگون خواهیم کرد @WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21249" target="_blank">📅 20:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21248">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏وزارت جنگ ایالات متحده در حال بررسی برکناری مکس لدرر، ناشر باسابقه روزنامه نظامی «استارز اند استرایپس»، پیش از موعد بازنشستگی اوست. این اقدام پس از انتشار گزارش‌های انتقادی فیک این روزنامه درباره وضعیت خدمه ناو هواپیمابر «آبراهام لینکلن» در جریان جنگ علیه جمهوری اسلامی و همزمان با تشدید اختلاف میان این رسانه و مقام‌های نظامی آمریکا مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21248" target="_blank">📅 20:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21247">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_bm4ZG9_aLqbcOspG7oEpurX18X7rvP3ife6xx-8dAAMval1sQz81vqx1SBl70iWE9r9L3syhKS8ebAlnrYPq_EcNwF8UKOMQtuG6FU30R0Pa_fJTpCUDInmD6Rq5jsNDDOFbJMYv91-Rg51QBnMcw5QYv6jVYIBsLmhKC3J7LbP2QVDHh-lpG8Q4WCWrA8wnvySCIswzlelw65QTqPdoDIWgbb8SuPOqglbp_SXmjZKSF1ADalGQnVD5U9dXIJaHiRh2tMjgG3guIr-WsuaNc-NuPqBpcE4ndSMAGzoux4i2f0k9dcae89pRRLxMrGmHFC58ExdPGmQXWrcj29LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنت‌کام : نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۶۷ کشتی تجاری را تغییر مسیر داده‌اند، ۳ کشتی را غیرفعال کرده‌اند و ۲ کشتی را برای اطمینان از رعایت مقررات به بازجویی و بازرسی برده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21247" target="_blank">📅 19:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21246">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانادین پرس :
پیر پویلیور،
رهبر حزب محافظه‌کار کانادا و رهبر اپوزیسیون رسمی این کشور
، از رضا پهلوی، ولیعهد ایران، دعوت کرده است به کانادا سفر کند. پویلیور روز شنبه در مراسمی در بریتیش کلمبیا اعلام کرد که علاوه بر این دعوت، قرار است به‌صورت مجازی با رضا پهلوی دیدار کند. او در این مراسم گفت این دیدار فرصتی برای گفت‌وگو درباره
دموکراسی و امنیت ایرانیان خارج از کشور
است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21246" target="_blank">📅 19:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21245">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بسنت درباره ایران: ما از این وضعیت مناقشه با ایران عبور خواهیم کرد. نمی‌دانیم چه زمانی. @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21245" target="_blank">📅 18:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21244">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3286979e.mp4?token=AcY5MJuFVwK0wXtQYGhGCiBosCHyIho7MHdqJJCC-HPVbzR6SmbI5ZY8G0PgR_A736npFsaDQBQYKoiajmHpIxbePmlyi6UTS0CfDf8Pby7EaFQ4VKa9EjmtgJFNCqii3KRGVcdP2hoTpAVdrTBNQzHE1Ru2A4ViSC-Rp9CVHzxxIweIMO_RxeJIDQ5uilU-5HrbzWCZplMYuYcsDGpz-t5YGy64bB7tfdaTKM4N3RRtPOn0UAR40IoLB4hlBX2c6Sp9oUU1moi9jAn5NNFPJEr29HyrC4-l7jAESVNZh9NXLj_It-ox0tLTnDugEr4xssrpiGw7xGU0UV6BcqK-FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3286979e.mp4?token=AcY5MJuFVwK0wXtQYGhGCiBosCHyIho7MHdqJJCC-HPVbzR6SmbI5ZY8G0PgR_A736npFsaDQBQYKoiajmHpIxbePmlyi6UTS0CfDf8Pby7EaFQ4VKa9EjmtgJFNCqii3KRGVcdP2hoTpAVdrTBNQzHE1Ru2A4ViSC-Rp9CVHzxxIweIMO_RxeJIDQ5uilU-5HrbzWCZplMYuYcsDGpz-t5YGy64bB7tfdaTKM4N3RRtPOn0UAR40IoLB4hlBX2c6Sp9oUU1moi9jAn5NNFPJEr29HyrC4-l7jAESVNZh9NXLj_It-ox0tLTnDugEr4xssrpiGw7xGU0UV6BcqK-FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت درباره ایران: ما از این وضعیت مناقشه با ایران عبور خواهیم کرد. نمی‌دانیم چه زمانی.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21244" target="_blank">📅 18:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21243">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مسرور بارزانی، نخست‌وزیر اقلیم کردستان عراق به المانیتور با اشاره به بیش از
۱۰۰۰ حمله موشکی و پهپادی
علیه اقلیم از زمان آغاز جنگ آمریکا و اسرائیل با ایران در ۲۸ فوریه، خواستار تقویت پدافند هوایی شد. او هشدار داد خروج سامانه‌های
پاتریوت و نیروهای آمریکایی
، اقلیم را آسیب‌پذیرتر می‌کند و از آمریکا و متحدانش خواست برای تأمین پدافند هوایی، سامانه‌های هشدار زودهنگام و تجهیزات مقابله با پهپاد کمک کنند. بارزانی همچنین گفت حملات اخیر به دفتر شخصی او و خانه رئیس شورای امنیت اقلیم با هدف
ارعاب و کشاندن اقلیم به درگیری
انجام شده است. او مدعی شد پهپادهای استفاده‌شده در این حملات
ایرانی و از نوع حدید-۱۱۰
بوده‌اند و هیچ کس دیگری ندارد؛ ادعایی که ایران آن را رد کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21243" target="_blank">📅 17:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21242">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : فلورا جون ۲ @WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21242" target="_blank">📅 15:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21241">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">العربیه : ۳ نفر از نیروهای سپاه در حملات به مواضع حوثی های یمن کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21241" target="_blank">📅 15:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21240">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک مقام آمریکایی و یک مقام کاخ سفید به خبررگزاری سمافور گفته‌اند که دولت آمریکا معتقد است
مذاکرات ایران و عمان از چند هفته قبل عملاً شکست خورده است
. احتمال دریافت عوارض از کشتی‌ها برای عبور از تنگه هرمز و پیشبرد سازوکاری جدا از مذاکرات مستقیم تهران و واشنگتن از دلایل اصلی نارضایتی دولت ترامپ عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21240" target="_blank">📅 14:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21239">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو: بازسازی نوار غزه تنها در صورتی امکان‌پذیر خواهد بود که حماس به طور کامل از سلاح‌های خود محروم شود.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21239" target="_blank">📅 13:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21238">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو : شما سورپرایز خواهید شد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21238" target="_blank">📅 12:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21237">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cd8ea5eb.mp4?token=IXprD0R_qmIruvAu0dPe6rr86-xzW1qdmChthPR7qrk-CTVmIUTQWC9cl2BcjkN9RVUln7Zd_kPfklIz0dwrlAMexOyKkOBG_P6SmDxgwKbgiLUGfiIQNaXkmAVRpg2hiHLodo9xyjPIXQxDWHRecBtdfc0oYUL1E-YA0uCsVeuRSEOPFz0o0eae3vNiPsSKfftdNYpt665EELjapA9JpRNUHeuG8UhZb592GpKYAvcQojlLKwHGnKTlWRh9enO_5qiPslhaIqGsdWuTu1HbzntZmJ7AmmmFKzX58I5MrnV1T6frJHZ6Pi4JjHqpaLNplKPAft3JBHXXdNYmMcrxsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cd8ea5eb.mp4?token=IXprD0R_qmIruvAu0dPe6rr86-xzW1qdmChthPR7qrk-CTVmIUTQWC9cl2BcjkN9RVUln7Zd_kPfklIz0dwrlAMexOyKkOBG_P6SmDxgwKbgiLUGfiIQNaXkmAVRpg2hiHLodo9xyjPIXQxDWHRecBtdfc0oYUL1E-YA0uCsVeuRSEOPFz0o0eae3vNiPsSKfftdNYpt665EELjapA9JpRNUHeuG8UhZb592GpKYAvcQojlLKwHGnKTlWRh9enO_5qiPslhaIqGsdWuTu1HbzntZmJ7AmmmFKzX58I5MrnV1T6frJHZ6Pi4JjHqpaLNplKPAft3JBHXXdNYmMcrxsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روابط عمومی پالایشگاه نفت تهران:
ستون‌های دود در آسمان تهران، ناشی از آتش‌سوزی در دو مخزن مربوط به بسته‌بندی و انتقال محصولات نفتی، در محوطه پالایشگاه نفت در پایتخت تهران است. هیچ آتش‌سوزی در داخل خود پالایشگاه رخ نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21237" target="_blank">📅 12:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21236">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رسانه‌های سعودی به نقل از منابع گزارش دادند:
دولت ترامپ از اطلاعاتی درباره یک طرح ایرانی برای عملیات‌هایی که فراتر از هدف قرار دادن کشتی‌ها است، و همچنین طرح نیروهای یمنی برای افزایش هدف قرار دادن کشتی‌ها در تنگه باب‌المندب، مطلع شده است.
ترامپ به تیم خود اطلاع داده است که در صورت ناکارآمدی تحریم‌های اقتصادی، احتمال انجام حملات گسترده علیه ایران وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21236" target="_blank">📅 12:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21235">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بیتکوین در حال پرواز است و با قدرت از مرز ۷۱،۰۰۰ دلار هم عبور کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21235" target="_blank">📅 11:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21234">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e050dd4cf1.mp4?token=CfXFokdN_zRmiSS74QsKxJISX9G71-nPLImkYx4oUQExHo2PtNLLmZRbqlKDywGKvD_tWNFH3xcOd5BTcQN6KD4SciNyY8Zi9MLuhq82Sl4XVi0oABtyClMLLLgJL9VB_MHvcP3SCWqdQmtWzR8Kh7IQTZgr1_0-TTn2RD4yDtEr5Kag-ap7wnxwS-aJ7zn3hexO-3P1l8zZeN_lEJVO8xv-rhDAevtpW-bbV4BOBaSap21ptJemGvPFHvxq9t4gOgzyZIIRyeJQbHM9la56G1p-R9OB9t6BhHMcB4DRq7MA8dlr1TZ2BEDw8Y72VVwNOB69JmHByXBJDvhc-8AWRaGdt7uO_Vfw_FtjMOkY66hTPwBqIfM4XeWgppeMctc8G8y6SN7fdtDOtT2JzkSsyPHapBpAYp3InXxwTllTq86yAsMtuy91OqHgBkGrM0FrIYF50HPdugmxOaX8HslHa1q59RAvv7tKzZ0PgjJJUtgNAQkpcORXDhnvYs7LLsx03WaIkRDShqSYkY_BdZ_Thh3BOKYcXHUVKlZHj6eowlTNZW862hOn1eTYeOEzM3MIJo7puh5k1yev7CYGifpwjSIPHlU8olLzi9pgsr91eoNxzHTbAJcyotwvFXcZyei76F2PBVPI09kTHHvZFmjgbRrMguO27rws9ehIFs8GA9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e050dd4cf1.mp4?token=CfXFokdN_zRmiSS74QsKxJISX9G71-nPLImkYx4oUQExHo2PtNLLmZRbqlKDywGKvD_tWNFH3xcOd5BTcQN6KD4SciNyY8Zi9MLuhq82Sl4XVi0oABtyClMLLLgJL9VB_MHvcP3SCWqdQmtWzR8Kh7IQTZgr1_0-TTn2RD4yDtEr5Kag-ap7wnxwS-aJ7zn3hexO-3P1l8zZeN_lEJVO8xv-rhDAevtpW-bbV4BOBaSap21ptJemGvPFHvxq9t4gOgzyZIIRyeJQbHM9la56G1p-R9OB9t6BhHMcB4DRq7MA8dlr1TZ2BEDw8Y72VVwNOB69JmHByXBJDvhc-8AWRaGdt7uO_Vfw_FtjMOkY66hTPwBqIfM4XeWgppeMctc8G8y6SN7fdtDOtT2JzkSsyPHapBpAYp3InXxwTllTq86yAsMtuy91OqHgBkGrM0FrIYF50HPdugmxOaX8HslHa1q59RAvv7tKzZ0PgjJJUtgNAQkpcORXDhnvYs7LLsx03WaIkRDShqSYkY_BdZ_Thh3BOKYcXHUVKlZHj6eowlTNZW862hOn1eTYeOEzM3MIJo7puh5k1yev7CYGifpwjSIPHlU8olLzi9pgsr91eoNxzHTbAJcyotwvFXcZyei76F2PBVPI09kTHHvZFmjgbRrMguO27rws9ehIFs8GA9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : فلورا جون ۲
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21234" target="_blank">📅 10:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21233">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoPxul1u_qyLLQmyx-S6pFBx8HEilhixPd3DibcAstca0Sb4grIYYMN_ht3ZS5ugfHWgcUbFV1W6ADJfrxn02_sMkcq8Pbm2phrGfSh0e7deeisBMguNaBovWUXpJ9gkUyeQFxgR2erh24vyxwo-Bm8MoMkSb9DdFLKmfd8diMSmTT41v8AZHqmj7LNdh_eV8CPl0w7waxTGY09iCo8R4mzl-vDzEk8zGR-q5R3hxW-uzd6jBIGpJSyX0jx4T3Le6LWmwR9LmGzozuHhGEoP_GSy7j2-kOogKGeZn79r6GRuJcas5VL2J0y-CSUJK9kPrfEdwbUkik8SKsQumGEgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه اعلام کرد: حکم قائم حسینی معروف به آرین ، تبعه خارجی و از متهمان پرونده موسوم به «میدان علیخانی» اصفهان، اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21233" target="_blank">📅 10:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21232">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اکسیوس گزارش داد که ارتش آمریکا در اقدامی محرمانه، یک کریدور دریایی در مسیر ورود و خروج کشتی‌ها از تنگه هرمز ایجاد کرده است
تا روزانه میلیون‌ها بشکه نفت از این مسیر عبور کند؛ اقدامی که به گفته دو مقام آمریکایی، با وجود بن‌بست در جنگ، موفقیتی قابل توجه برای واشنگتن محسوب می‌شود.
بر اساس این گزارش، این عملیات طی چند هفته گذشته در جریان بوده و هر شب حدود ۱۵ تا ۲۰ نفتکش از طریق یک مسیر جنوبی در امتداد سواحل عمان وارد تنگه هرمز شده یا از آن خارج می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21232" target="_blank">📅 08:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21231">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsTigAtWNVEIBuUDmIyL8KECt7DFU1QmoJPOxH_z97vX8Rjt2wsMDGpYIaA67vGYSKkV4wBSGxO-1QUzhEJ6e-3TEMj8m10QcLhabv18uOUmeND4w2IGA6vopgMMsH70BcE9PBVtDCe2LBZBoYAjwPfXPC-OEC987MKuHVwiKEsn9jihIHwREeX8876LYzWYWzvZJGiOUXl10naYQ1aAuJ8AvwzIvpCtQyPtjdLOQTXLjG0kcrQyqPVijhu7MrVRgFjlNXCWhQ9PsYF7WPvIH4MLbO6gMqtQK4EceqPxgjxmlSXrYJl2n7hmLuWrkRj0Vk2h8j9OggFRBMCBvkW9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : هیچ‌کس به‌اندازه من به جمهوری اسلامی ایران فرصت نداده است تا به یک توافق برسد. متأسفانه، آنها از این فرصت استفاده نکردند. بنابراین، امروز اعلام می‌کنم که
کمرشکن‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است
را آغاز خواهیم کرد! این عملیات، جنگ اقتصادی و انزوایی در مقیاسی بی‌سابقه خواهد بود. نیروی دریایی آنها از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان به ویرانه تبدیل شده و ارزش پولشان از بین رفته است؛ کشورشان نیز به تار مویی بند است. امروز همچنین اعلام می‌کنم که
هر کشوری که به مؤسسات مالی، شرکت‌ها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هرگونه کمک حیاتی به ایران برسانند، خودش با پیامدهای اقتصادی بسیار سنگینی روبه‌رو خواهد شد.
قاچاق نفت، خطوط مبادله ارزی، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها و شرکت‌های پوششی —
همه اینها باید همین حالا متوقف شوند.
خودتان می‌دانید چه کسانی هستید. این یک
«روز دی اقتصادی»
خواهد بود و ما نیاز داریم همه متحدانمان در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند. این دیوانگان در آخرین نفس‌های خود هستند و این اقدامات تاریخی، آنها و توانایی‌شان برای گسترش تروریسم در سراسر جهان را فلج خواهد کرد.
ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21231" target="_blank">📅 07:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21230">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بامداد نیک و خجسته ، پیج اینستاگرام رو برگرگردوندم ، خواب بودم
instagram.com/yashar
پیج دوم پشتیبان :
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21230" target="_blank">📅 07:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21229">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17a03cc01.mp4?token=V97PMqM_N3hosT91z7Tvxg30V8S3pCvnSF1JF38sl2Xw5K-koIqEnraxjJjAjCF_6l47VLsE2GrNiyvT7hSudqhO1LK-sw2Mf6nzPSVcTsGugDub2IsoEDKYxSsu7gppOovcEaqsRFdnft52xl6CCAx7wCv1EtUyI-9IxhR0SJkWtnDzRnBfa9vfv3PoyS4BWqGzk-GiV0z78knlQYH5CQqBSWdYv8ePFsbXfE_TsOAeinVld96llnaZguaKvsYK3rqFe3Ju_H_gYjEqutaktbsFc0gpI8s9xSpIdVv6qfYBKlUfI14sKYyO0PZCD3BPZKDHgelGKMTi4qXUUUt1C72TM25EJM0yEhWCFvce36p4WPOHRcX1C-3Cm-954pljWAoAo1s72Vi7ZTRie_MJpptb2d5U8QTmipAEZJ-hhT3fToGcF__ltyAj6wLDv4thXQu8RFzQdAvAu7iQF1itIpN-8P3pdJBHxrHZeKq0DwUdXVQjR6BcU8NSRtQ7S6Iet_LUKWb8rSFR9pSJXQ8wNeh-ZzCidZ9_Jkpj-FlTwp2x6hZWxSEUvi5cF4Cggu5Npp7rK9GIoyCTfPbx0pgvj_xGwyKdSOJ3SZ_t0S1XFZLDOdj3HyZlKP7tLp13iowJPvFaFpsvN8cegNwYY8Jyj7MPb9T4Hx1jU9R58nKvPJY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17a03cc01.mp4?token=V97PMqM_N3hosT91z7Tvxg30V8S3pCvnSF1JF38sl2Xw5K-koIqEnraxjJjAjCF_6l47VLsE2GrNiyvT7hSudqhO1LK-sw2Mf6nzPSVcTsGugDub2IsoEDKYxSsu7gppOovcEaqsRFdnft52xl6CCAx7wCv1EtUyI-9IxhR0SJkWtnDzRnBfa9vfv3PoyS4BWqGzk-GiV0z78knlQYH5CQqBSWdYv8ePFsbXfE_TsOAeinVld96llnaZguaKvsYK3rqFe3Ju_H_gYjEqutaktbsFc0gpI8s9xSpIdVv6qfYBKlUfI14sKYyO0PZCD3BPZKDHgelGKMTi4qXUUUt1C72TM25EJM0yEhWCFvce36p4WPOHRcX1C-3Cm-954pljWAoAo1s72Vi7ZTRie_MJpptb2d5U8QTmipAEZJ-hhT3fToGcF__ltyAj6wLDv4thXQu8RFzQdAvAu7iQF1itIpN-8P3pdJBHxrHZeKq0DwUdXVQjR6BcU8NSRtQ7S6Iet_LUKWb8rSFR9pSJXQ8wNeh-ZzCidZ9_Jkpj-FlTwp2x6hZWxSEUvi5cF4Cggu5Npp7rK9GIoyCTfPbx0pgvj_xGwyKdSOJ3SZ_t0S1XFZLDOdj3HyZlKP7tLp13iowJPvFaFpsvN8cegNwYY8Jyj7MPb9T4Hx1jU9R58nKvPJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : خونثانیاهو
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21229" target="_blank">📅 00:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21227">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KmRDObielKIjF7RHLFAEdMJjqy0RX3KopIDGekz2V-CX3donnM-8l0nL_pAbnNkpJyJ9gs8VqpzIpUKUGR-X1R4UoUnWvAcKlxSOwWB4mtdgaVJ1uAJ28qu4_O3frOtQvuH6dH7orS-Nh09kt5xXEu1OrWcSzlXSefsmjOQCxZk90I1_-mRW7aQP-9oYDgoznAywer9Wm9BwCOwzRt9IR0S5udxJOU_xL-9Wu6BrJOZ3bF49z6oh5-tENH4GlRUnajoEqzPDukxtf9zlc1q4HSWZcYNjR004Q4Bg2dZGr6wZrv2yq5OICdovo4h9n4JmdLNrGqWEf4QOjaznTldaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PsdNBGEmCKZLyCDV3FhANZiPcLg6l4xj_RXJ_6zSZDzzKhqM9SbXyDCIOxl_eMNeC-Gv7en9Fzzp9aSu6EUku-nfpjBNKdOsMcOe50W2UQPQxnh-yYBHSZIghOuzDPu1_OZdL_ZbwZms5ubXGohRYAOKE0A7XrwzEGQAFN_LSmXVm9RJY2y86l0F8syImQ9Mw6YffMKO4KMDo7yYvykQk6qg0z7dwFzw8G6xEHRYWTLsidOR7E8Hhm22GOKjrLWAZ2B3Qb4r1LDuqFtCWQB-U-Z2k9v3fig1ZvaQLY-zh-CAH_A8onjGfpCuzFnGrUdT_oRrl1lGog1lyMyQuSaLiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تویت جدید مم باقر که با سرش تنگه هرمز رو بسته نگه داشته
🤣
@WarRoom
یاشار : خودش داره میگه تنها راش اینه سرم بره</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21227" target="_blank">📅 23:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21226">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25637c93b.mp4?token=BXyWJG_c-z4DBzd-fexWG6s0cQlobrn7QKQHvUZSnCSYtnp3YYMBb-PnUfBHAmiN9VTrX7d-xnOMi7Vr6J8u7G8sEq3vp9S5WcyDQBiXC1ceYNKIxK7NV115NKPG478zWMkVqgtulmutglkROyASVerao58fwDGUYR6DgXLK4Lafdy8bZHvlwpTesc7ONkYQ9vcT2vYf4S8mUrRx0aYz2a5PPirahInxIZ8e6fAyi0OuFc-dW3AFQy7T3b7SmKc-KCncQb08qDSu8_6t22oJoIoLUYmJ4in3Fij332pHuZTqfV_RrPhOtmRbDdQawO0SEgwF8WMCQ35xw8OQBv-BmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25637c93b.mp4?token=BXyWJG_c-z4DBzd-fexWG6s0cQlobrn7QKQHvUZSnCSYtnp3YYMBb-PnUfBHAmiN9VTrX7d-xnOMi7Vr6J8u7G8sEq3vp9S5WcyDQBiXC1ceYNKIxK7NV115NKPG478zWMkVqgtulmutglkROyASVerao58fwDGUYR6DgXLK4Lafdy8bZHvlwpTesc7ONkYQ9vcT2vYf4S8mUrRx0aYz2a5PPirahInxIZ8e6fAyi0OuFc-dW3AFQy7T3b7SmKc-KCncQb08qDSu8_6t22oJoIoLUYmJ4in3Fij332pHuZTqfV_RrPhOtmRbDdQawO0SEgwF8WMCQ35xw8OQBv-BmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما چیزهایی داریم که می‌توانیم علیه ایران تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21226" target="_blank">📅 23:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21225">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0003edd740.mp4?token=LgSYxr5od57TvLytqyTefpaegxlboyQFSsXLUV3q9O7pfY1yZ0qkzq_hLmS96plccdCfckJUZ_I97hZEC3Rg-oYqQiiFT_PEIZBKT6OdRGzKkzAtx1NL-AU2wbJtRHMaVlMl6rz0Yhj3FVCHxiMTPi8zXhQ-bwfIedAhRQ6o6f18_O4iscc3ekc2_Rr9RMyQny_MefO6l455hmqK8QY8SZnaUI0ZlGss6gBMGwj9ReKFgV1a45vjYMGmV6GD_M5jQG-GFEj1H19KAZ-wMtYD6iA_CpPhKQmeMMzlpaNZqitwpwbLP_FrdIKj-s12r-TDVCDx5D6HCTVJGqUOpkylQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0003edd740.mp4?token=LgSYxr5od57TvLytqyTefpaegxlboyQFSsXLUV3q9O7pfY1yZ0qkzq_hLmS96plccdCfckJUZ_I97hZEC3Rg-oYqQiiFT_PEIZBKT6OdRGzKkzAtx1NL-AU2wbJtRHMaVlMl6rz0Yhj3FVCHxiMTPi8zXhQ-bwfIedAhRQ6o6f18_O4iscc3ekc2_Rr9RMyQny_MefO6l455hmqK8QY8SZnaUI0ZlGss6gBMGwj9ReKFgV1a45vjYMGmV6GD_M5jQG-GFEj1H19KAZ-wMtYD6iA_CpPhKQmeMMzlpaNZqitwpwbLP_FrdIKj-s12r-TDVCDx5D6HCTVJGqUOpkylQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
خطوط لوله زیادی در حال ساخت هستند. من فکر می‌کنم تنگه هرمز به اندازه گذشته مهم نخواهد بود.
در حال حاضر، تنگه باز است. قایق‌های زیادی از آن عبور می‌کنند. مردم این را گزارش نمی‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21225" target="_blank">📅 23:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21224">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: در حال حاضر با ايران مذاکره نمی‌کنیم، زیرا مذاکره با آن‌ها اتلاف وقت است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21224" target="_blank">📅 23:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21223">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrXj0NyTlz8jeBSaCXE13pjUtzX1KunUULKuFiLpcBzABNzCw-DsKeW_zglRK793RhfQwdwcQAldcBfJfqvX4sDyfKTAD0WUPxjHqwuzdO3lsvaQ1pbNnvAgIfBGmhoJ-_bcsXk5Y_Qhx_W8cStmBO6ci_dvxNpmTxQEneQGS4Jva0SoRMWRXADs4oY1VGJUKu6is0rgAyCwDuRV603rs6vzyXZb8NXA8xN95LUtUl2MBtuHH_xo9WAAQxDuBTIBy1m4vhQKbT7xJlOGPpAWftbhvS6Sh7WCiPGJe4w3QX5dss0wPVrGxFsL6tXoJXgLoC5BGIiWJ8exQbz_0M__eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه نیلوفر شادمهری، رایزن فرهنگی جمهوری اسلامی را از این کشور اخراج کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21223" target="_blank">📅 22:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21222">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">زلزله ۴.۲ ریشتری حوالی گیلانغرب در استان کرمانشاه را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21222" target="_blank">📅 22:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21221">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال 13 اسرائیل به نقل از یک منبع نظامی: آخرین چیزی که به آن نیاز داریم، یک جنگ تمام‌عیار با ترکیه است. ما از میدان‌های درگیری کافی در حال حاضر برخورداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21221" target="_blank">📅 22:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21220">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو: ما توضیح دادیم که با حضور نظامی ترکیه در سوریه مخالفیم، و به نظر می‌رسد که آنها به خوبی به ما گوش ندادند، بنابراین تلاش کردیم تا آنها بهتر درک کنند.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21220" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21219">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ممرضا نقدی : ما باید به بازدارندگی دست پیدا کنیم. برای ما خوب نیست که کسی بتواند تصمیم بگیرد به ایران حمله کند، و سپس، در صورت شکست، عقب‌نشینی کند، خود را سازماندهی کند و شش ماه بعد دوباره بازگردد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21219" target="_blank">📅 20:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21218">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مارک لوین : من با ویکتور دیویس هنسون (مورخ، نویسنده و تحلیلگر سیاسی آمریکایی) موافقم؛ او در برنامه من در فاکس نیوز استدلال کرد که ما باید از تشکیل یک دولت در تبعید ایران با رهبری شاهزاده رضا پهلوی حمایت کنیم. و اگر رژیم ایران فروبپاشد، او می‌تواند در دوران گذار، به‌عنوان یک رهبر موقت ایفای نقش کند.
به مردم ایران سلاح بدهید!
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21218" target="_blank">📅 20:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21217">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رویترز: بریتانیا امروز ۷ فرد و نهاد جدید مرتبط با ایران را به فهرست تحریم‌های خود اضافه کرد. این تحریم‌ها در چارچوب تحریم‌های رژیم ایران اعمال شده
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21217" target="_blank">📅 20:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21216">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش اسرائیل: ما دیروز در منطقه ساحلی، یک فرمانده گردان و سه فرمانده گروه را از نیروهای نخبه در گردان بیت لاهیا وابسته به حماس به هلاکت رساندیم.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21216" target="_blank">📅 20:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21215">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ امروز در کاخ سفید با شماری از مدیران و چهره‌های بزرگ صنعت رمزارز دیدار می‌کند. در این نشست، مقررات جدید بازار کریپتو، قانون CLARITY و تعیین حدود اختیارات SEC و CFTC بررسی خواهد شد. رؤسای SEC و CFTC و مدیران شرکت‌هایی از جمله Coinbase و Ripple نیز در این نشست حضور خواهند داشت
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21215" target="_blank">📅 19:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21214">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab2cd42e14.mp4?token=bedTuSJvgS4hPjmBbydwXZdcof5pSp4shfgCbOoZSrNS2Un5DmkcslwOW035Q7y6uZGRxFAcr6_y2SxrZxHSdf9y0V9BR4TXGKJsAa-J6yKy2wKmJ7ad6hhLPvA3-2nhiPc4EM8ZRAzBWaDoompOqOMWDpGPMj1XX5qwPNY5vKZxBmJrTjmJ3_q1Q7-mn3Ts4kcy73iKh4zbS5YEiume8sAKVa3dNGj-dGrClg4jSUcYAQOroK5yMOY0jn83tQbSq_f50u_sn7hfogAZrcz66Hwx8sOjiRb6EiqrcHPCOZYRExmiMWROc-hFyO4-x1PeBJdCCwqi1fXSwLHpysgQbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab2cd42e14.mp4?token=bedTuSJvgS4hPjmBbydwXZdcof5pSp4shfgCbOoZSrNS2Un5DmkcslwOW035Q7y6uZGRxFAcr6_y2SxrZxHSdf9y0V9BR4TXGKJsAa-J6yKy2wKmJ7ad6hhLPvA3-2nhiPc4EM8ZRAzBWaDoompOqOMWDpGPMj1XX5qwPNY5vKZxBmJrTjmJ3_q1Q7-mn3Ts4kcy73iKh4zbS5YEiume8sAKVa3dNGj-dGrClg4jSUcYAQOroK5yMOY0jn83tQbSq_f50u_sn7hfogAZrcz66Hwx8sOjiRb6EiqrcHPCOZYRExmiMWROc-hFyO4-x1PeBJdCCwqi1fXSwLHpysgQbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : مردم دارند جایگزینی برای تنگه هرمز پیدا می‌کنند. می‌دانید جایگزین‌ها چیست: تگزاس، آلاسکا، لوئیزیانا.
مردم برای نفت دارند به آمریکا می‌آیند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21214" target="_blank">📅 19:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21213">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce66acfb3.mp4?token=j3rAQ18oMn-OGW1DyovJQXWx9QJ3iZiw_FQSQRk7kuGHwAnAclg_oA0xWc0BbkWwCj2ZVaZM4dY_tgyPFDlGDh1sZEU-hVx1woF-PWNW9azr9sj2J7TOE4OdX72PZY4mmOyWQhvfCWilIqf3rwjt2dzMB5nNtLqnONmVX9pIFfawufhk5lmDJBoVSWwVpOTZDSeDNLYWZjkYc7AITNJyx1EO4aKGYKhrhMI0cRTb4N4pFOsdX5xdLEJiNhi8w9U7k_NKOk0CsvdP7NZl6Cz6g5pPtVEkcBkeutvavIAcvlS-lzwAmCwiPbiHPj3LlI6YeR047yTKEodY0cN8CFtnkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce66acfb3.mp4?token=j3rAQ18oMn-OGW1DyovJQXWx9QJ3iZiw_FQSQRk7kuGHwAnAclg_oA0xWc0BbkWwCj2ZVaZM4dY_tgyPFDlGDh1sZEU-hVx1woF-PWNW9azr9sj2J7TOE4OdX72PZY4mmOyWQhvfCWilIqf3rwjt2dzMB5nNtLqnONmVX9pIFfawufhk5lmDJBoVSWwVpOTZDSeDNLYWZjkYc7AITNJyx1EO4aKGYKhrhMI0cRTb4N4pFOsdX5xdLEJiNhi8w9U7k_NKOk0CsvdP7NZl6Cz6g5pPtVEkcBkeutvavIAcvlS-lzwAmCwiPbiHPj3LlI6YeR047yTKEodY0cN8CFtnkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما تنگه هرمز را کاملاً در اختیار داریم و کنترل آن را در دست داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21213" target="_blank">📅 19:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21212">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. می‌دانید چرا؟ چون از آن استفاده خواهند کرد.
ما اجازه نمی‌دهیم از آن استفاده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21212" target="_blank">📅 19:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21211">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d548b77d.mp4?token=VRsATYt8bJi1D-SVGgLZrsG_z4OscUQK1_6ZnnsdxN1S5uL9RUOKiyxk2JfRQMC9F3GHwA8-hRJmJIAhdjK7_q8mDz7zQKgFee2zsuJccVh-VW8tVBO2-RPPGFLHlcTsGLRejkUiCRYoxMh-lbWk3ffA54xn6AK6ev6Dj4Q18KpQQiCJ0ZsSwGc1hXpIgUuekqoJ1_eOxbpYs7TtdZ4b_UmBirk65v1bBWoRSS8D1B9iOmsVnntEjD19Phtf8-NUVkP88iLzyBQIAAuDh4BB-uxYGd5TexwbBg6BFpEpmuFhU5ri4U5oPg5Tky4bjLsEeu37stJIxP38LJniqwmAFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d548b77d.mp4?token=VRsATYt8bJi1D-SVGgLZrsG_z4OscUQK1_6ZnnsdxN1S5uL9RUOKiyxk2JfRQMC9F3GHwA8-hRJmJIAhdjK7_q8mDz7zQKgFee2zsuJccVh-VW8tVBO2-RPPGFLHlcTsGLRejkUiCRYoxMh-lbWk3ffA54xn6AK6ev6Dj4Q18KpQQiCJ0ZsSwGc1hXpIgUuekqoJ1_eOxbpYs7TtdZ4b_UmBirk65v1bBWoRSS8D1B9iOmsVnntEjD19Phtf8-NUVkP88iLzyBQIAAuDh4BB-uxYGd5TexwbBg6BFpEpmuFhU5ri4U5oPg5Tky4bjLsEeu37stJIxP38LJniqwmAFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا شما دوباره با ایران مذاکره خواهید کرد؟
ترامپ: شاید در مقطعی، اما الان به همین حالت اوضاع خیلی خوب است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21211" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21210">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2b72a973.mp4?token=kzVd_zGqvO44ErSUwFYDYcd0FdA7voVnCE0xZGFoj3qv3YAXwReLxBqL1_Kejfm3E0rLN7fUSkplBb4b9XLvlCp7JuxGCLcZfyUId9d89SaAx8YUKQNZbSGsUGkRKmXqC5pozVWlgcFGUMr1chGQCBC4S8NF_52jGdn09hRUU9s7TyH9DPtqKbrRqIplT5S8AbgDTx7YAtvP71TmjvQBU_-UlqDMYeX99iiACBbAbxstOze0rGbqt-uTq7hX9132JwWLFdwExF9_glNZmTxPsDqXbxZp2wKzp7Mb7-aPvEanhkqzhcZOMi0JnvfxpnaucYAL6-iWmhzOziBvCfFdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2b72a973.mp4?token=kzVd_zGqvO44ErSUwFYDYcd0FdA7voVnCE0xZGFoj3qv3YAXwReLxBqL1_Kejfm3E0rLN7fUSkplBb4b9XLvlCp7JuxGCLcZfyUId9d89SaAx8YUKQNZbSGsUGkRKmXqC5pozVWlgcFGUMr1chGQCBC4S8NF_52jGdn09hRUU9s7TyH9DPtqKbrRqIplT5S8AbgDTx7YAtvP71TmjvQBU_-UlqDMYeX99iiACBbAbxstOze0rGbqt-uTq7hX9132JwWLFdwExF9_glNZmTxPsDqXbxZp2wKzp7Mb7-aPvEanhkqzhcZOMi0JnvfxpnaucYAL6-iWmhzOziBvCfFdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره تنگه هرمز:
قرار نیست کارمان بی‌نقص باشد، اما نفت زیادی از آن خارج می‌شود، خیلی زیاد.
مردم شگفت‌زده هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21210" target="_blank">📅 19:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21209">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca74a36348.mp4?token=lU1bF2MpDQ6m3s2OSqpE7IUlfvth122pVw4dGvUHx9p2zY6zAkPdWFpIW3SYAbZmoUSU_zV7b5veCvFwqQ4Q-aA2ew37TKh4LXENMdJRsg9mgLDJecptXzSVaUvmOd7wPTmb016szNXwMcDeK_5PGYT36c55F7OH1WmhSv28tmYGUnptUmYxN6wDny3j3OWxTsUHAJskwNctadL61HfJlVxHftelxaLN6Oeq5yellUUlKERRIRQMZIKdfKj_YEd2IWD9dV2DHyysUZfWA4hzrjFiwJ2yT1h_J_n9iyOrqScfznDc3v72v2Yatytlci67s2TYrcMIsOFkOoi0jLhlvYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca74a36348.mp4?token=lU1bF2MpDQ6m3s2OSqpE7IUlfvth122pVw4dGvUHx9p2zY6zAkPdWFpIW3SYAbZmoUSU_zV7b5veCvFwqQ4Q-aA2ew37TKh4LXENMdJRsg9mgLDJecptXzSVaUvmOd7wPTmb016szNXwMcDeK_5PGYT36c55F7OH1WmhSv28tmYGUnptUmYxN6wDny3j3OWxTsUHAJskwNctadL61HfJlVxHftelxaLN6Oeq5yellUUlKERRIRQMZIKdfKj_YEd2IWD9dV2DHyysUZfWA4hzrjFiwJ2yT1h_J_n9iyOrqScfznDc3v72v2Yatytlci67s2TYrcMIsOFkOoi0jLhlvYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد کیم جونگ اون:
این واقعیت که من با کیم جونگ اون خوب کنار می‌آیم چیز خوبی است.او ۵۷ سلاح هسته‌ای بسیار قدرتمند دارد. هرگز نباید اجازه می‌داد این اتفاق بیفتد، اما او آنها را دارد.من با او خیلی خوب کنار می‌آییم. من کیم جونگ اون را خیلی خوب می‌شناسم. او خوب خواهد بود.تا زمانی که یک رئیس جمهور باهوش داشته باشیم، او خوب خواهد بود. اگر یک رئیس جمهور احمق داشته باشیم، احتمالاً او خوب نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21209" target="_blank">📅 19:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21208">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پولیتیکو : ایران و آمریکا وارد فاز صبر و انتظار شده‌اند؛ هر یک منتظرند تاب‌آوری دیگری زودتر تمام شود
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21208" target="_blank">📅 17:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21207">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ60R3-f1VL1AZ4wqEaydQw5hEfBiRhug_bSPBDA2bh4cpWK_uK-DiXXmwlrpknC4USwA1z9698E95F6pA31NoeHxs95koAgjyWk9BuXnLxoPz6U6CHcNxA1ML95bJ508raPRYyEHUjPxalmdVeDv7OBfUnLeDPjD-nEMaAEZcYapQANS5g8MghKj8Y320LwBhVLuT6Sqxf94MXkxU37z8pw597ZYK1jWEsCtwd_fMz0C4euu1kYvsvnP5dzsRDGxwv73NAEQ1oUERLkN6cNnMpfQUQReNVJoh-nqpvFo-HSdCx5ZsC8LGm93QUhW4C5PN0SnZa9RtaFzwpvrPOD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: یک فروند جنگ الکترونیک EA-18G Growler نیروی دریایی آمریکا، هنگام انجام گشت‌زنی بر فراز خاورمیانه، از یک فروند KC-135 Stratotanker نیروی هوایی آمریکا سوخت‌گیری می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21207" target="_blank">📅 16:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21206">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مرندی مشاور تیم مذاکره کننده : دیروز، کاخ سفید گفت که مذاکراتِ وجود نداشته با ایران را «به حالت تعلیق درآورده» است؛ ظاهراً با این هدف که فشار اقتصادی را افزایش دهد. اما چیزی که کاخ سفید نمی‌گوید این است که آن‌ها تا همین امروز همچنان در حال ارسال پیام به تهران هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21206" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21205">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یک مقام ناتو در واکنش به گزارش‌ها درباره احتمال تهدید اهداف آمریکایی در اروپا از سوی ایران گفت:
ناتو آماده مقابله با هرگونه تهدید علیه کشورهای عضو است و برای دفاع از همه متحدان خود هر اقدام لازم را انجام خواهد داد.
این مقام تأکید کرد که وضعیت بازدارندگی و دفاعی ناتو «قوی و مؤثر» است و یادآوری کرد که سامانه‌های پدافند هوایی ناتو پیش‌تر نیز موشک‌های بالستیک شلیک‌شده از ایران به سمت ترکیه را در چهار مورد رهگیری کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21205" target="_blank">📅 14:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21204">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ناو هواپیمابر یواس‌اس جورج واشنگتن به عنوان بخشی از عملیات خود در منطقه عملیاتی ناوگان هفتم ایالات متحده، از تنگه سنگاپور و تنگه مالاکا عبور می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21204" target="_blank">📅 14:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21203">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وال استریت ژورنال: مقام‌های عرب می‌گویند ما «بین ایران و آمریکا گیر افتاده‌ایم»
آن‌ها معتقدند جمهوری اسلامی در نهایت به افزایش فشار اقتصادی، واکنش نظامی نشان خواهد داد، در نتیجه، جنگ دوباره می‌تواند شدت بگیرد
حملات اخیر جمهوری اسلامی در تنگه هرمز، روشی را که برای حفظ صادرات و تولید نفت به کار گرفته شده ، تهدید می‌کند , در این روش که «سفرهای شاتل» نامیده می‌شود، نفت خام و فرآورده‌های نفتی از داخل خلیج فارس به کشتی‌هایی منتقل می‌شوند که در خارج از منطقه منتظر هستند تا محموله را به بازارهای جهانی منتقل کنند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21203" target="_blank">📅 14:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21202">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ارتش اسرائیل : ما در چارچوب خنثی کردن شبکه تونل‌های سازمان‌های تروریستی، دو تونل زیرزمینی حماس در شرق خط زرد در نوار غزه را مسدود کردیم که در مجموع بیش از دو کیلومتر طول داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21202" target="_blank">📅 12:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21201">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47b2eca4.mp4?token=iyQxSi5b6lz3xLXP3mdrMvdpBjxh5SsHzPV-G0RKZ9YKxwnCYWSOuz3TJO2E24II219JCTpoabx8AAAwoUEO0ozWXpJL2cHQ4oaINECTObrFXBA6G7Ni_SKsuuFi1SnOQ4Xi5g9tzhsrH8OuAHI_U465wg3ZFA7wBuvRwCJ4Vo8geTbYNW6oBu8SJ1Fu4vQKFrpXaC89ZAhePe811ifXar140E0d-Lm7oI4C55NyXzmWmUpdliwLP4WwRAmxoG503gqs1BkD0wCAzXVlSdXixxTyTpAEwxug9dHbY5UgJvs8cI-dw9uYKDxT2LuiipqZi6hZrXhWcgqjuy81-z55KYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47b2eca4.mp4?token=iyQxSi5b6lz3xLXP3mdrMvdpBjxh5SsHzPV-G0RKZ9YKxwnCYWSOuz3TJO2E24II219JCTpoabx8AAAwoUEO0ozWXpJL2cHQ4oaINECTObrFXBA6G7Ni_SKsuuFi1SnOQ4Xi5g9tzhsrH8OuAHI_U465wg3ZFA7wBuvRwCJ4Vo8geTbYNW6oBu8SJ1Fu4vQKFrpXaC89ZAhePe811ifXar140E0d-Lm7oI4C55NyXzmWmUpdliwLP4WwRAmxoG503gqs1BkD0wCAzXVlSdXixxTyTpAEwxug9dHbY5UgJvs8cI-dw9uYKDxT2LuiipqZi6hZrXhWcgqjuy81-z55KYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممباقر در عراق…
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21201" target="_blank">📅 11:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21200">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سی‌ان‌ان: ایران بخش قابل‌توجهی از کنترل خود بر تنگه هرمز را از دست داده است.
بر اساس داده‌های شرکت کپلر، در دو هفته گذشته
بیش از ۸۰ درصد کشتی‌های عبوری از مسیر تحت نظارت عمان
در بخش جنوبی تنگه عبور کرده‌اند؛ مسیری که ایران با آن مخالف است. برخی کشتی‌ها نیز با وجود تهدیدهای ایران، با اتکا به حضور نیروی دریایی آمریکا از این مسیر عبور کرده‌اند. یک تحلیلگر کپلر گفته است که به نظر می‌رسد ایران
دست‌کم بخشی از کنترل تنگه را از دست داده است
؛ هرچند ایران همچنان با تهدید حمله و ایجاد بازدارندگی، توان تأثیرگذاری بر رفت‌وآمد دریایی را حفظ کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21200" target="_blank">📅 11:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21199">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الجزیره : این ترامپ نیست که مانع عبور کشتی‌ها از تنگه هرمز می‌شود، بلکه شرکت‌های بیمه این کار را می کنند
تا زمانی که تهدید فیزیکی علیه تردد دریایی وجود داشته باشد، این شرکت‌ها از قدرت مالی خود برای جلوگیری از عبور کشتی‌ها استفاده خواهند کرد
بدون تضمین‌های قاطع مبنی بر اینکه کشتی‌ها از حملات ایران در امان خواهند بود، مالکان حاضر نمی‌شوند که در تنگه تردد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21199" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21198">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اورشلیم پست: تام باراک، نماینده ویژه آمریکا، هشدار داد که حمله اسرائیل به پایگاه هوایی ابو الظهور در نزدیکی ادلب در سوریه، می‌توانست منجر به تشدید تنش‌ها و یک رویارویی نظامی مستقیم، احتمالاً با ترکیه، شود.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21198" target="_blank">📅 10:56 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
