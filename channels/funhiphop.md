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
<img src="https://cdn4.telesco.pe/file/V1vEagIvlliBZ8AqabnI9k1mZUCiSQojMQhovJoH61r9NwcVSWRLQ6BRlp1hlzEB3iba_mSE8577es9496VtLQQuTAMSKN6cKkajkzUsOLzYHVXVu1ppZK3U_ELhfenVm042rL6u81GsUmRsllk8wjzfFz12_pLPJWjyUmaXdu16i9eghci4cFt-qsDwugN7FxVMn_ze8ZqAn55Yy-Y5RV9iyPuN_R-5S7y2KfkzyzudY5xpWFkIfFHHFwzDavvsYD3k6sEZKuNbCRwi9K-Y1D5u0x37yx8oJ16A8_6C8xqUxfnnSsgyUd0qfpiiNKqCbuRXbjYMMLfvTz69Sb_ADQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 13:46:11</div>
<hr>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی ترکیه با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید
✉️
:
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 94 · <a href="https://t.me/funhiphop/75748" target="_blank">📅 13:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTAqACOxp2qrPfp9VJGxmFgJbRnK6falk_6pP3AZIBVUfqdsuCYpo2_jYOhyazlOw5KuOli5oUu34KEKNq82_TB1MWidZdyoRgOfNMjKHuko7RYAncG20Z1fNwnUOk-qE9zEPzr-AcjGOQHs2BUyWlGHjS2DZMAUNwRUejQ_HQ0eeAKAE-dN4jrA2D1s9tKzWmalCFCOYUBlKDCAXv2NTKQzlAL7huf2-rvlJZXIbeZPVOG0fTEj6AG3qhPTJ9cbQkTia8nYiv9c2WnodvMyD2sNusGZ6Z3fhk5KJ9nYASCzBktPx93GcttOUebLabQwxvsdJds1etuiaPI9iBfeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 374 · <a href="https://t.me/funhiphop/75747" target="_blank">📅 13:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کان نیوز:
نتانیاهو در گفت‌وگوی دیشب با ترامپ، نخست‌وزیر تأکید کرد که اسرائیل آزادی عمل خود را در مقابله با تهدیدها در همه جبهه‌ها حفظ خواهد کرد و این جدا از توافق ترامپ با ایران خواهد بود و ترامپ هم این را مجدداً تأیید کرد.
ترامپ تاکید کرد که در مذاکرات بر خواسته مستمر خود برای خلع سلاح برنامه هسته‌ای ایران و خارج کردن تمام اورانیوم غنی‌شده از خاک این کشور پایبند خواهد بود و بدون پذیرش این شرایط، توافق نهایی را امضا نخواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/funhiphop/75746" target="_blank">📅 13:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک منبع خیلی آگاه ایرانی در گفت‌وگو با خبرگزاری رویترز:
در صورت موافقت و تصویب توافق میان تهران و واشینگتن در شورای عالی امنیت ملی ایران، متن سند جهت تصمیم‌گیری نهایی برای آیت الله مجتبی خامنه‌ای، رهبر جمهوری اسلامی ارسال خواهد شد تا به تایید ایشان هم برسد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/funhiphop/75745" target="_blank">📅 13:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75744">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پروفسور امیرحسین ثابتی، نماینده مجلس و عشق من:
در هر حال چه توافقی در کار باشد و چه نباشد، اولا؛
جنگ در عرصه نظامی ادامه دار خواهد بود. چون هدف دشمن نابودی ماست نه مذاکره و حل مسئله.
خصوصا که جمع بندی دشمن بر این است که باید "مخالفان تسلیم ایران مقابل دشمن" در همه سطوح ترور شوند که گزینه اول‌شان رهبر انقلاب و گزینه‌های بعدی‌شان فرماندهان نظامی و سپس سیاستمداران ضدامریکایی ماست.
ثانیا؛ اگر توافقی در کار باشد آن را با خطوط قرمز رهبری می‌سنجیم. چنانچه توافق با آن معیارها تطابق داشت از مذاکره کنندگان حمایت میکنیم و چنانچه نداشت، با آنها رفتار دیگری خواهیم داشت.
کنترل تنگه هرمز به دست ایران، عدم گفتگو درباره مساله هسته‌ای، گرفتن غرامت از دشمن، لغو تحریمها، آزادسازی پولهای بلوکه شده و... بخشی اصلی خطوط قرمز است که باید در هر توافقی رعایت شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/funhiphop/75744" target="_blank">📅 13:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75742">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شمارو نمیدونم ولی سر سمتی که امید دانا باشه، من ترجیح میدم برم سمت مخالفش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/funhiphop/75742" target="_blank">📅 13:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75741">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تنها کسی که تو اپوزیسیون اونور کصخل نیست خود رضا پهلویه
@FunHipHip
| Constantine</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/funhiphop/75741" target="_blank">📅 13:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75740">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کاش اپوزیسیون امام خمینی هم دست شاهین و علی کریمی بود واقعاً
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/funhiphop/75740" target="_blank">📅 12:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75738">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc-ZcV9CWGGI9BHwNq8sHRmdgdQmcyIHE18W7_-400j5RjQxzCi77xIuhoT-mHon5auqJkkTuCDbJb11tlRjAGj-MpndKbg-CUmuW9KNZpe_vHVrNfyCZiuFmfi-kJjNFuN4U0OmwPy11_OBlt6L8nlmbUHQ_BBqnfjqnbZ8Rr505m0FXyAymhglTjhRiZ6hyEO1bkwgSUdPgmVCUzY7gFCTZ1Aci9vq74Di_LdFwTtMf1xQqejVPG6owx1g3I3Ji7FWTbmoMl0khIBIRKReQhQ7qtQMxq67f3bV8jFH04VMADWsgwYbDDkL48RYm2wzVLHb7TAEpLY4E5-dJy8rPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی بنده خدا چرا کاور شده   @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/funhiphop/75738" target="_blank">📅 12:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75736">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W67yz-y09htOIKeNY6rV6_MTvD0MJ4G49UGj79imz29CscnGk-QWR9L6xcI7TMdQaIDL480JQsL6JhELSb1a3bZu8yBH3vPT6fBTBiQ7z_14yPb95RuTUdZBVi6g3LMnm0gYPjuDFHqqHmKKQzcXnlwYUJfdeQdwGJPn3TtB_2Fqp4hwDirNSMV5EK8TfgkDlDHyFNN5bHh4BZQWOekKSjUi9nJKrO8ONTM-rs5AethZCZK3BwHdY0ks72MdZKO0MHzljd5VxAmN4yZhJoIekiJ5zJu6u2nEgNgRmNksYZbpR8Iqmm995kaIdm0qR-ttjllQOgfWYBkXb6OnAc9cpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfQXcN1Zneamt3oG6E57jekVr7UPhledQrZN_91bMQ4LLrI01Q4KFhlVio5EjwQpQss9CpjETqK3BT1jYZXbq5V11NmEnsIhizv6J9-b1mHTDOBbXaG7QlXFcRbiwjF6l8FjVATHd4t9ssF5p05HV4OJUEi0UxH19Rw74v5hS_z93gLdj_K-Vk_nGbNH6QW8DLaeE1iC-45T3KPMc4AYY_wKR8q4plnfAuUhwgIb8cdU1vU9dF1NxD3LmPwu5AxEeS69xQMA4WfOLDoe5jKkjn3fXo5R9cxm-C6AFNztKSr1AlslYGgyu1Z6Rw_GdjXk0cVdhH2WFuWVi-JKUR-cfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رضا پهلوی بنده خدا چرا کاور شده
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/funhiphop/75736" target="_blank">📅 12:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75735">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بمب جدید تسنیم به نقل از یک منبع به شدت مطلع و آگاه:  اختلاف میان ایران و آمریکا بر سر یکی دو بند از تفاهم نامه احتمالی همچنان ادامه دارد و به دلیل مانع‌تراشی‌های آمریکا هنوز موضوع نهایی نشده است. ایران بر احقاق خود مردم خود تاکید دارد و این موضوع به میانجی…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/funhiphop/75735" target="_blank">📅 12:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75734">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بمب جدید تسنیم به نقل از یک منبع به شدت مطلع و آگاه:
اختلاف میان ایران و آمریکا بر سر یکی دو بند از تفاهم نامه احتمالی همچنان ادامه دارد و به دلیل مانع‌تراشی‌های آمریکا هنوز موضوع نهایی نشده است.
ایران بر احقاق خود مردم خود تاکید دارد و این موضوع به میانجی پاکستانی اعلام شده است که در صورت ادامه مانع‌تراشی‌های آمریکا، امکان نهایی شدن تفاهم نامه وجود ندارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/funhiphop/75734" target="_blank">📅 12:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75733">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مارکو روبیو درمورد توافق احتمالی:
پیشرفت‌هایی حاصل شده است. پیشرفت‌های قابل توجه، اگرچه نه پیشرفت نهایی.
شاید در چند ساعت آینده جهان حداقل در مورد تنگه‌ها و روندی که در نهایت ما را به جایی که رئیس‌جمهور می‌خواهد برساند، خبرهای خوبی بشنود.
این ایده که به نوعی این رئیس‌جمهور قرار است با توافقی موافقت کند که در نهایت ایران را در موقعیت قوی‌تری در زمینه جاه‌طلبی‌های هسته‌ای قرار دهد، مضحک است. این اتفاق نخواهد افتاد.
درباره تنگه هرمز، آنها مالک آن نیستند. این یک مسیر آبی بین‌المللی است.
کاری که آنها اکنون انجام می‌دهند تهدید به نابودی کشتی‌های تجاری است که از یک مسیر آبی بین‌المللی استفاده می‌کنند.
اگر اجازه دهیم این موضوع عادی شود، ما یک الگوی خطرناک ایجاد خواهیم کرد که می‌تواند در نقاط مختلف جهان توسط افراد مختلف تکرار شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/funhiphop/75733" target="_blank">📅 11:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75732">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رویترز به نقل از یک مقام ارشد ایرانی:
برخلاف ادعای رسانه‌ها، تهران با تحویل ذخیره اورانیوم با غنای بالا موافقت نکرده است.
این مرحله از مذاکرات فقط بر پایان جنگ متمرکز بوده و هست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/funhiphop/75732" target="_blank">📅 11:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75731">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قوه قضاییه: امروز صبح مجتبی کیان به جرم ارسال مختصاف صنایع نظامی به شبکه های ماهواره ای معاند (ایران اینترنشنال) اعدام شد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/funhiphop/75731" target="_blank">📅 10:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75730">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ان وای پی: نصیره بست ۲۱ ساله، مهاجم تیراندازی نزدیک کاخ سفید، طبق گزارش‌ها خود را «عیسی مسیح» معرفی می‌کرد.
او پس از شلیک ده‌ها گلوله توسط نیروهای فدرال هدف قرار گرفت و کشته شد. گفته می‌شود وی سابقه مشکلات روانی و نقض محدودیت نزدیک شدن به کاخ سفید را داشته است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/funhiphop/75730" target="_blank">📅 08:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیویورک‌تایمز: مقام‌های آمریکایی مدعی شدند ایران در توافق پیشنهادی ترامپ با کنار گذاشتن ذخایر اورانیوم غنی‌شده موافقت کرده است. جزئیات این موضوع در مذاکرات آینده بررسی خواهد شد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/75729" target="_blank">📅 07:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75728">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8mCZP6gCXC8FL_WnFTBMz3_eOJCicj5cWtUgXc47CtDH70u12I6LzOvbZjCamfbKI_bZzfURmCAaSmJgUHU3A5mE_52jBWr177r0HzthLyXX0AN8-QHATvNMXoiAOJNQhq6ODgM1OzKcDqIfD7DRNZeG-G5Or2RpndNlNgc-X9_bqAbuoHHgS7pUQuxDI3hBKxEC4xaBgief8stD3CpyJcho7uOyvro6p6aRsamOHfMk_K59tpbRYmVrIy_tEgAcDVNEmuBDlTnvBu-x9-V5G5smzY9et9EARBloa7vRHeCyWiq3wmB0gBOZb7cB2HHcgIgzkPkptNUGh98nLdUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جا قحطی بود برا اون عکس پسر؟
باید سعی کنی تا انتهای مسیر نیش ترمز نزنی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/funhiphop/75728" target="_blank">📅 05:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75724">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikURi3GNgThs-8qiDbtLFh_p8daSmgOi2_hRD3_R8T9lNvkUyDQeGuak8qY1vXsMhBpKhbFyv9xAAy1A42B-R1pm8UajAoIPU6ot9353sBQoXYsp8Lvq39gQvBWFpq8IbGq5vWxwqN0Vbku5XCUFr73naL4nzez3BPhW3stKUZA25_oelb6pfV4DbnW-Vm9XDs1TzHCNASeNcsQt-WRrhLUXwe41-CQGpnL5B4nhbFuPn55PA8DLE8verZ8CCpw0iZ11I74baS10I9xWK31qamvu-mQwDZj4uWgpbyjHbqi7xp476M7gvVehKVo8YW30DaiuBw9QrFUYZGpsnVb-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه یه سری حرومزاده برای چس تومن پول، اقدام به تبلیغ بدافزار در قالب vpn کردن. روش کار به این صورته که با عنوان “نسخه فلان مود شده / رایگان” یا “قیمت vpn خیلی خیلی ارزون” شما رو توی تله میندازن و میگن برای اجرا باید فلان فایل رو نصب کنید.
از نصب هرگونه فایل تحت عنوان vpn از منابع مشکوک در تلگرام، جدا پرهیز کنید.
گوشیتون کاملا بگا میره و میشه منبع تبلیغات برای قشر حرومزاده دزد.
الان همه وی پی ان پولیا با همون نرم افزارهای عادی v2ray کار‌ میکنه و نیازی به نصب چیز جدیدی نیست.
@Funhiphop
| Comentive</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/75724" target="_blank">📅 01:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
نیلی افشار بلاگر اینستا رو یادتونه که بعد قطعی اینترنت بی پولی بهش فشار آورد و اومد سمت Only fans ؟!
👀
برای ورود به چنلش صد دلار هزینه کردیم تا عکس و فیلمای جدیدشو برای شما بزاریم توی رباتمون
💵
‌‌ مشاهده عکس و فیلمای نیلی  ارزش دانلود 85 از 100
🍒</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/funhiphop/75723" target="_blank">📅 01:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75722">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcKqjzQh3SsbFrefLtCliu1BcaFSgNmCCTUqj48VyivXSLsPn8MBQlAw_vqgIES18Ew3MnDqP0YELuUlpNxyukiLk1bFpq0Gx9i4CByKojocnaZnvxWhUse6Uueglr-SnFR1pRVev5bncFyk_xdEyqb6Pf36OhfSDGfgKWxwbzeiUy8iZ7PZAK7etLMom-Jrgd_3DoRZbVvAwwLmWwDrPGF3-iq6Sx4IHM-TZk_xo7hhCsUbPuAWYLCMScYsKehK3r6V9t6ItwG0ntQPZFAcf5qhEnBEJU5Fhgh_2QvARNvuIBQn47rO_bdS3d2CAEaKaBPyJyFIqOwrsDGIfk64Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیلی افشار
بلاگر اینستا رو یادتونه که بعد قطعی اینترنت بی پولی بهش فشار آورد و اومد سمت
Only fans
؟!
👀
برای ورود به چنلش
صد دلار
هزینه کردیم تا عکس و فیلمای جدیدشو برای شما بزاریم توی
رباتمون
💵
‌‌
مشاهده عکس و فیلمای نیلی
ارزش دانلود 85 از 100
🍒</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/funhiphop/75722" target="_blank">📅 01:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الجزیره: توافق موقت بین ایران و آمریکا به مراحل نهایی نزدیک شده و احتمال کاهش تنش و باز شدن نسبی تنگه هرمز وجود داره.
فارس: برخلاف ادعای ترامپ، تنگه هرمز کاملاً به شرایط قبل برنمی‌گرده و کنترلش همچنان در اختیار ایران باقی می‌مونه.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/funhiphop/75721" target="_blank">📅 00:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjcFobkTaTJLrL-fjNiPJcikiAj_03W-tDXPYaTGC8BSLrjtYSPJZDAdEGzvbySiC3hBhseqNK4Wb84UuURQDRwEzhK6SnRyi9W3bZp80W-oSvaYEgOHEKOAUWH_9J5OsGSixucpX81qHl8gpyUkdc6vpBu6Eccg6Tqn73eEo5QYKFckQ3xBIsuTDn2eIl5PsAKsYUQfea421CzPVMTiD6A_Jg207wKief-3HK4y3dU7lEnkoaZ91smuDbFLxzVXzx-Ww3kLnR9hzl4dSnYqvunfBr6S_CcTgzgv6mOSc4BNPLbGp2wAUY9T6UoULC-Sj4kx-Joz45ZtOw-1ceN0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/funhiphop/75720" target="_blank">📅 00:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75719">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ کصکش من که میدونم داری دروغ میگی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/75719" target="_blank">📅 00:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75718">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه:
«در نگاه رومیان، روم بی‌همتا و مرکز بلامنازع جهان بود. اما ایرانیان این تصور را در هم شکستند؛ زمانی که مارکوس یولیوس فیلیپوس (فیلیپ عرب) برای جنگ با ایران به شرق لشکر کشید، نبرد نه با پیروزی روم، بلکه با صلحی بر اساس شروط ساسانیان پایان یافت؛ تا جایی که امپراتور روم ناچار شد شرایط صلح با ایران را بپذیرد و در برابر آن تسلیم شود.»
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/funhiphop/75718" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVtpdDxlCQpWweaOeVc7OAaUKaULAKWoijAvkmdDyDhGTbML7_u1Qe4ivYsJ6oZkAkFacxNxRKbOSkk2Dejg4SYtjEpJdvz56O171zVQq1BA2DaMcIpUSHya-4rC5FcBqWjAU--1j-8eP5EWnzkchBsd7y0TtovXvP9yLM7XLfpx7-uLOWas0EyCz5r6VihVpykKbFpd2Dkited3H5YKcOL-nLLnjBXE0Q9Ei8jHSmXWZTnnKZmDjoPGivbuVeyy5ai8VQ98Fvvid3OcNFe5n4oCgFqch2FCXhZ8iRtT4qpcTQ2ThyTC9fnhK0q01pERmlKeJRXQ6yEyWunWG3z-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش اتریوم به خبر های مثبت مذاکرات
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/funhiphop/75714" target="_blank">📅 00:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قبل جنگ دوازده روزه قیمت تتر ریخت و بعدش زدن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/funhiphop/75713" target="_blank">📅 00:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75711">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">از من به شما یادگاری، هروقت دیدین یه جمهوری خواه آمریکایی داره از صلح و مذاکره صحبت میکنه، دقیقا همونجاست که مطمئن باشید قراره دیر یا زود عملیات نظامی رخ بده، و البته این عملیاتم فقط در راستای منافع خودشون و منافع آمریکا انجام میدن، نه کمک به کسی.  @FunHipHop…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/funhiphop/75711" target="_blank">📅 00:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](ChamanDarKhak)</strong></div>
<div class="tg-text">از من به شما یادگاری، هروقت دیدین یه جمهوری خواه آمریکایی داره از صلح و مذاکره صحبت میکنه، دقیقا همونجاست که مطمئن باشید قراره دیر یا زود عملیات نظامی رخ بده، و البته این عملیاتم فقط در راستای منافع خودشون و منافع آمریکا انجام میدن، نه کمک به کسی.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/funhiphop/75710" target="_blank">📅 00:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دفعه اول جمعه زدن دفعه دوم شنبه زدن  قطعا دفعه سوم یکشنبه(فردا) میزنن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/funhiphop/75709" target="_blank">📅 00:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75708">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
ترامپ:  من در دفتر بیضی شکل کاخ سفید هستم، جایی که همین الان تماس تلفنی بسیار خوبی با محمد بن سلمان آل سعود، رئیس جمهور عربستان سعودی، محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست وزیر محمد بن عبدالرحمن بن جاسم…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/funhiphop/75708" target="_blank">📅 00:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
ترامپ:
من در دفتر بیضی شکل کاخ سفید هستم، جایی که همین الان تماس تلفنی بسیار خوبی با محمد بن سلمان آل سعود، رئیس جمهور عربستان سعودی، محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الذوادی از قطر، فیلد مارشال سید عاصم منیر احمد شاه از پاکستان، رجب طیب اردوغان، رئیس جمهور ترکیه، عبدالفتاح السیسی، رئیس جمهور مصر، ملک عبدالله دوم، پادشاه اردن و ملک حمد بن عیسی آل خلیفه، پادشاه بحرین، در مورد جمهوری اسلامی ایران و همه موارد مربوط به یادداشت تفاهم مربوط به صلح داشتیم. توافقی تا حد زیادی مورد مذاکره قرار گرفته است که منوط به نهایی شدن بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همانطور که ذکر شد، می‌باشد. جداگانه، من با بی‌بی نتانیاهو، نخست‌وزیر اسرائیل، تماس تلفنی داشتم که آن هم خیلی خوب پیش رفت. جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بررسی است و به زودی اعلام خواهد شد. علاوه بر بسیاری از عناصر دیگر توافق، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/funhiphop/75707" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75706">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سلام وحید
‏تعداد زیادی جت جنگنده با سرعت بالا از اسراییل بر خواستند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/funhiphop/75706" target="_blank">📅 23:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75704">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دفعه اول جمعه زدن دفعه دوم شنبه زدن  قطعا دفعه سوم یکشنبه(فردا) میزنن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/funhiphop/75704" target="_blank">📅 23:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دفعه اول جمعه زدن
دفعه دوم شنبه زدن
قطعا دفعه سوم یکشنبه(فردا) میزنن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/75703" target="_blank">📅 23:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75702">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdHr5OxQ5Jd0w-otx4_WpU-GSJ5YMWCWs98gy462Ir2QANs9EudV8YXX09BN91tKOTb_Tnagez-vo7G1TuW_hhHr5QoUOwAseXGijgRdeJMNMFKkLfhV7sWuaLm5xIVfUNXutXfZNF1xKIIW5j2kUL5PKx9xQr2F2LrlPjItIbTeRhF2S1JCzlM6NOePYCdQHn3nW1IWtgrtI_hJVfWq1jRC-YvIE5AwBaSq1lzJ5Rw4dWXRoMm6kPapbHSYzQP2EneM8W4VwKovsSH9XjPxy91n22dBoQRx9FBT_l1Re0ts6gTzt1rbmbB2F-ABLP7jqmivP0toaOsoQlGeFpkUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه: تنها چندساعت تا نهایی شدن توافق میان ایران و آمریکا فاصله داریم.</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/funhiphop/75702" target="_blank">📅 22:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فاکس نیوز: هیچ توافق بین ایران و آمریکا صورت نگرفته است.
یک دیپلمات منطقه ای گفت تماس دونالد ترامپ با رهبران منطقه ای بسیار مثبت بوده است و رهبران منطقه ای از شتاب جدید گفت و گو ها استقبال کردند.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/funhiphop/75701" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چه توافق بشه چه توافق نشه چه جنگ بشه چه جنگ نشه
ایرانی ساده فرقی به حال تو نمیکنه چون تو جفت حالتش برای اینکه نشون بدی زرنگی پامیشی میری باک 30 لیتریت رو پر میکنی برمیگردی خونه
دلار و تورم پایین نمیاد که هیچ چندبرابر هم میشه صدات رو هم نمیتونی در بیاری
جلوچشمات رانت خوری میکنن بازم کاری از دستت برنمیاد
پس توی هیچکدوم از این حالت ها اوضاع و احوال ایرانی تغییری نمیکنه
اینه سیاست آخوند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/funhiphop/75700" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نیوزسیتی پرو: جلسه اضطراری امنیت ملی دولت ترامپ در اتاق جنگ کاخ سفید در حال برگزاری است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/funhiphop/75699" target="_blank">📅 22:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">48 ساله توافق نشده نکنه انتظار دارید توافق شه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/funhiphop/75698" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75693">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الحدث به نقل از منبع عالی‌رتبه: ظرف چندساعت آینده توافق میان ایران و آمریکا اعلام می‌شه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/funhiphop/75693" target="_blank">📅 21:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75692">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0l8iIQZ41Me8TBDXB4F6DsPIu3ZbqJJGLX7AVilQMjtuwcJLQbOuvBcI2QhikVxNYINwA9EreiYE3UlXzhiejgjd2zt89sbh_C2FHb3WDNcCu3Ir9nYa7mjUTh9YrSl66onHCmnn9d-1KK4zOoKE6mIp9hXvnOlYlc9FKWAJCdi4HFW136eht5DQEq8Z6EFa0aVGWRvKSjhbvXPl4sRwWwgcn7a7-oorl3MS1fYjPxGSbtZPbAO23vOleiiaNtErl_LZxIrNlstSfi4r4hPTW2jnqOgvSV2WGZjX_Fmcjytjilw6EypwTcia4I5FW_gwn9ytsHgRXUPOI2sDbw2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار عکس نقشه ایران با پرچم آمریکا: آمریکای خاورمیانه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/funhiphop/75692" target="_blank">📅 21:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75691">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نمودار محبوبیت ترامپ بشدت کاهشی گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/funhiphop/75691" target="_blank">📅 21:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75690">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مقام آمریکایی به آکسیوس:
توافق میان ایران و آمریکا برای پایان جنگ، نزدیک و در آستانهٔ نهایی شدنه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/funhiphop/75690" target="_blank">📅 21:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75689">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الحدث به نقل از منبع عالی‌رتبه: ظرف چندساعت آینده توافق میان ایران و آمریکا اعلام می‌شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/funhiphop/75689" target="_blank">📅 21:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75687">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!   دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
( فقط 300 گیگابایت موجوده! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/75687" target="_blank">📅 21:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75686">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuBc9r4PXXOMk26N_B7JOfHxMv3DgagLwmCnUI9XEdonktXlch8ZbOfAJ7UIMH_I2LaOEGkSZuQxpMZJ5MlwQyFBFy7iMdTrJ1mXE4Z1A7eUd0urUO_dt75mhXAljWXAF5H5_Jx1f7jfOm927bZDzaPQiahLwNWQxxK6ZzCNdLm7w7kHG5ldheGnkwyHkhqsUcKYvTxzIiTYjsKaP5RMec2GGLtMB-_blZUKDv-d3kfZ_KF8jGFceHKlI_Y0B6bireJgBDVrzlR-ZJ3KufoUDpN-nDwN3iQYqmTyoah6FMGphTAF6OOCiWm_ClKhHiNXKLEJ08kxM_CnPlsZQyjdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/75686" target="_blank">📅 21:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75684">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حمله کنسله   منابع آگاه می‌گویند به ایران ۲۴ ساعت فرصت داده شده تا چارچوب توافق را برای ۳۰ روز مذاکرات بیشتر بپذیرد، در غیر این صورت حملات از سر گرفته خواهد شد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/75684" target="_blank">📅 21:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حمله کنسله
منابع آگاه می‌گویند به ایران ۲۴ ساعت فرصت داده شده تا چارچوب توافق را برای ۳۰ روز مذاکرات بیشتر بپذیرد، در غیر این صورت حملات از سر گرفته خواهد شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/75683" target="_blank">📅 21:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">لیندسی گراهام: تو منطقه بعضی از قدرت‌ها ترامپ رو تحت فشار میذارن که جنگ با ایران رو از سر بگیره (امارات و کویت و بحرین و عربستان احتمالا) و بعضیا اون رو تحت فشار گذاشتن تا توافق صلح فعلی رو قبول کنه (قطر و عمان و پاکستان).
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/funhiphop/75682" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نهادهای حکومتی در تهران در حال تخلیه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/75681" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75680">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: اگر برای اسرائیل خوب نبود، معامله‌ای انجام نمی‌دادم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/funhiphop/75680" target="_blank">📅 20:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75678">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آکسیوس: نتانیاهو از ترامپ خواسته دور جدیدی از حملات رو آغاز کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/funhiphop/75678" target="_blank">📅 20:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75677">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپو پوشش نمیدم من، خستم کرد</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/75677" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75676">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556efd3c71.mp4?token=Iep3NPpv39l0_Ms2dGaen1dHiHnKLVKVczhKFJs4M14ShU_qoCtqqc5zs3t3FTQl8fsxqnHPERwFGWRC3HpIcCOQ1S31WPa6sf-bBNsWEz3S8ZItEul_pq2oka2yhCnbne5_27Tu_lQCjpFlwZBO15WWBem4uoOBi9_jL22EL__Lok8mqaBQWOqV38O8eo-vbvJt_b4jk_yTMtuCB61kYBrsBtWNK_EdEjRGs2VprlglnRmYnNWoNQ8h6j5bzdV_FzpQL-AI31fjq_F9b29pRaaLcDIE_C31WUsHh1rBggGKw_wDpiuiFJyq6fvvk0xZun3jHzehRB2Z3gySclH0kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556efd3c71.mp4?token=Iep3NPpv39l0_Ms2dGaen1dHiHnKLVKVczhKFJs4M14ShU_qoCtqqc5zs3t3FTQl8fsxqnHPERwFGWRC3HpIcCOQ1S31WPa6sf-bBNsWEz3S8ZItEul_pq2oka2yhCnbne5_27Tu_lQCjpFlwZBO15WWBem4uoOBi9_jL22EL__Lok8mqaBQWOqV38O8eo-vbvJt_b4jk_yTMtuCB61kYBrsBtWNK_EdEjRGs2VprlglnRmYnNWoNQ8h6j5bzdV_FzpQL-AI31fjq_F9b29pRaaLcDIE_C31WUsHh1rBggGKw_wDpiuiFJyq6fvvk0xZun3jHzehRB2Z3gySclH0kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخدا من هزینه نمیکنم برم اینستا اینارو ببینم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/75676" target="_blank">📅 19:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
(
فقط 300 گیگابایت موجوده!
)
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/funhiphop/75675" target="_blank">📅 19:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75674">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j41sglQtxJrbai-wJaeD31ppSySzWwtIDOkPXZpcy81KOn_1qVBsVluq5ZsJ_ZJRkOOkmnUYeH3KF64y9GlaUqFOB5nf9s46mEzp5Ls18AtIhYWkI3P3VaOCxsYoaIMB68gb3ufVijSJJs9S4jMZs_NrUDzPbGoNIsAfKA-xvsgmGPnBrc__NV6Gp_kD_uVgM1oqm6N48INLOOdF2ugLKUa4gcjVNGF98Lqw-N5c8r-jYL6_-kyB3b6tjq0N2a-CBUj66jMcIzrK2fo4r436uP1pHokPR8JI3NF95aYhvtIR3KP_Xbx3TfzVGTgCVGifSQbN8EmG__94skI1ZF8ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/funhiphop/75674" target="_blank">📅 19:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرنگار اکسیوس در توییتر: ترامپ میگوید پیش نویس جدید توافق با ایران را با مشاورانش بررسی میکند و احتمالا تصمیم نهایی را روز یکشنبه میگیرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/funhiphop/75673" target="_blank">📅 19:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیویورک تایمز: فیفا قصد دارد بار دیگر ورود پرچم شیر و خورشید و پوشاک مرتبط با آن را به استادیوم‌های جام جهانی در مسابقات ۲۰۲۶ ممنوع کند. این پرچم همچنین در جام جهانی قطر ۲۰۲۲ محدود شده بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/75672" target="_blank">📅 19:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75671">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فایننشال تایمز:
میانجی‌ها معتقدند که آمریکا و ایران به تمدید آتش‌بس به مدت ۶۰ روز و فراهم کردن زمینه برای مذاکرات هسته‌ای نزدیک شده‌اند.
توافق پیشنهادی شامل بازگشایی تدریجی تنگه هرمز، بحث درباره رقیق‌سازی یا تحویل ذخیره اورانیوم غنی‌شده بسیار ایران، و تسهیل محاصره آمریکا بر بنادر ایران، همراه با رفع تحریم‌ها و آزادسازی مرحله‌ای دارایی‌های خارجی تهران است.
یک مانع بزرگ همچنان درخواست رئیس‌جمهور ترامپ است که ایران ذخیره ۴۴۰ کیلوگرمی اورانیوم نزدیک به درجه تسلیحاتی خود را تحویل دهد و سه سایت اصلی هسته‌ای خود – نطنز، فردو و اصفهان – را از کار بیندازد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/75671" target="_blank">📅 18:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من خودم بتمنم ولی الان بحث، بحث وطنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/funhiphop/75670" target="_blank">📅 17:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLRaAG1uBSO8I_B4Fd_ZOzMTwl5OKyE-LRssUqAE8i5NI4gVA5NaIXMMFh8PSL6fM6DYc09Ifu8DmXbSMX4Ak8e2nBgN_ZLifnOtleustI8S6IeYjDQTBkGIP7nalw975tO-l5MZB1SNzTvYRnRBp_K1ijJ_ma1-9LfA3loOnlQIZpUYgWvO_L4AKTbrDRJd0r13x-id8XJZdekpCJIfUJHio0lNU14oEDavAl1Nn5WPHJ4FOPRdqrfg4RPUhOJShRBqUvG48q54jotHyziedQIdpCBxNzjcYMnK9XuIe6I-cIPDRLCnAcEROgowwoEXlFsuQVqlSZdN8JJEEwmVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور پررنگ بتمن در تجمع اعتراضی دانش‌ آموزان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/75669" target="_blank">📅 17:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آخرین باری که اتابکی گفت میزنن ۸ روز بعدش زدن امیدوار شو ایرانی   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/funhiphop/75668" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75667">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اتابکی که سری پیش هم زودتر گفته بود آمریکا حمله میکنه بازم اومد گفت چند روز دیگه میزنن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/funhiphop/75667" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75666">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یک مقام ایرانی به الجزیره:
ما به یک تفاهم‌نامه با میانجی پاکستانی دست یافته‌ایم و در انتظار پاسخ آمریکایی‌ها هستیم.
تفاهم‌نامه شامل پایان جنگ، رفع محاصره، باز کردن تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
تفاهم‌نامه شامل مسائل هسته‌ای نمی‌شود زیرا این مسائل پیچیده‌اند و نیاز به زمان کافی برای مذاکره دارند.
پس از ۳۰ روز از امضای تفاهم‌نامه، ممکن است درِ مذاکرات هسته‌ای باز شود.
قرار بود رئیس ارتش پاکستان [عاصم منیر] تفاهم‌نامه را در تهران اعلام کند، اما برای هماهنگی به واشنگتن رفت.
برای ایران امکان دادن امتیازات بیشتر از آنچه در تفاهم‌نامه آمده، وجود ندارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/funhiphop/75666" target="_blank">📅 17:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75665">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ با انتشار عکس نقشه ایران با پرچم آمریکا: آمریکای خاورمیانه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/funhiphop/75665" target="_blank">📅 16:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75664">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUIIsVN5Qemijzoj7T8Ynm84x0W4dLalBALcTezTMHCGxT5SaNgpnahJXlfJusoRqy9tI9uGlQ5F0r31mKVNpJjnD4DjWePWRbGxjaZWCxY8w1NU_J-zBGskMyrRIHzOi4pbiYEUxXqtrenJiApQdBotDYEJu7C4FxBfOjJ_DgfYgluY9-sf6QZ9Xoac1QzFU6vbHoxv43IE6o9aLBx43rSE8YLeJFl0xBxBH3VlyjvrQT4iX_E4GrSO589wFjqVl9ha3Ov71gSQAeVmqpZhRNG1EUlmDs4U8MaAA26YqhgarHJd20DuTAbaLkMX5U8XC433OCDQZbVFbGA1F3ixvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار عکس نقشه ایران با پرچم آمریکا:
آمریکای خاورمیانه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/75664" target="_blank">📅 16:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75663">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b026396695.mp4?token=OuhzMt3aR1MOMEK7B-FzkkN0mcouy52N0leXu9V_cIBvriG5_6WSeWzp_nH4d5tiZBpDqN20B3JRyEpqybVfyLJpOQ3p56G6kmB2Ru-LJAvt71BO_eg5O6SQIEsDHhZxKXE24UZDqalz5XH54kk_EPH-sbm65i1WrbWxGVzhyyX4JuCBJ2eLZy_K5R398kiuPNG9n3-7cA79wNaIKQq-RSayM5PPBlgbQqH4_0eOrskRtxDBF6VNmPpH4exRRP0m4cG2lZcljPTVbXXXurePWuLlVKJ3HHQWurxy_0IY72aT7XRSCYS9a8lMxdxtcRWKulAbLnO5gpAo5uX6Gggxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b026396695.mp4?token=OuhzMt3aR1MOMEK7B-FzkkN0mcouy52N0leXu9V_cIBvriG5_6WSeWzp_nH4d5tiZBpDqN20B3JRyEpqybVfyLJpOQ3p56G6kmB2Ru-LJAvt71BO_eg5O6SQIEsDHhZxKXE24UZDqalz5XH54kk_EPH-sbm65i1WrbWxGVzhyyX4JuCBJ2eLZy_K5R398kiuPNG9n3-7cA79wNaIKQq-RSayM5PPBlgbQqH4_0eOrskRtxDBF6VNmPpH4exRRP0m4cG2lZcljPTVbXXXurePWuLlVKJ3HHQWurxy_0IY72aT7XRSCYS9a8lMxdxtcRWKulAbLnO5gpAo5uX6Gggxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتابکی که سری پیش هم زودتر گفته بود آمریکا حمله میکنه بازم اومد گفت چند روز دیگه میزنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/funhiphop/75663" target="_blank">📅 16:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75662">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی:…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/funhiphop/75662" target="_blank">📅 16:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75661">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دیدار عاصم منیر با پزشکیبان و قالیباف در تهران   @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/funhiphop/75661" target="_blank">📅 16:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75660">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiAOA_Ejwfk0NCsIjKgpzRbFcgr_gDE1-ju8Sgdyx07XHQ1ViZNl9rZk6g3RYxnFWW96Jw2g54XPkThJ2MJZaqt7_FUHePoCDEPj8bFSC-i3opwvfiKT06OEAOvfZHNldzpbEFsC9NvRYpKn7kxAZBtYaf9okobDJzeHMdeYaIpoqhCvRlmWvKRdEAZp1UmZTkkVfympzlZKvsa94wG2oPIGMhQ0B32gqryko56wUCazYVNdvU7ioYHuBKnkJ8VimVJqMqzbLel0cmvYIIUddJGfYYSZrAdFTRDmeDe7kwBu8UQg1pmEgf-wCJ2XUexw1rhru7J65y2nN9qY6EdIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا واقعا</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/funhiphop/75660" target="_blank">📅 15:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75659">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49046a9f4e.mp4?token=SGzdqc7_O1wlo3qQR3c4gR8mEfBzQHuu5bJYEC2GQaACjpuByxPhQI1cceOmLebxl_e8PwuOKr2hkL-zPFts4wX6-ZR-cluu-uFxa1GqvbkQasaLeEmNeX9ks9_3mbDBDieP8BcDbBmts_9Of1g1UhIxqKzTYAHk7H3e-nB0hSk2A_XEV804aEFoYvUtAHg5U-P_B8kHR8WESbsoXiqyvz5wZSLGVgvFfqlzvnt08S3uFPggilu33B-IeAm-kNbKULnRLLEF_ggO0w4tF3WAFc0OOXkbDG-a3xzP_pIOFwDCxSNvPXlbX2IXcX9kT1or3pCiA-c7_syP7rq_q53tDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49046a9f4e.mp4?token=SGzdqc7_O1wlo3qQR3c4gR8mEfBzQHuu5bJYEC2GQaACjpuByxPhQI1cceOmLebxl_e8PwuOKr2hkL-zPFts4wX6-ZR-cluu-uFxa1GqvbkQasaLeEmNeX9ks9_3mbDBDieP8BcDbBmts_9Of1g1UhIxqKzTYAHk7H3e-nB0hSk2A_XEV804aEFoYvUtAHg5U-P_B8kHR8WESbsoXiqyvz5wZSLGVgvFfqlzvnt08S3uFPggilu33B-IeAm-kNbKULnRLLEF_ggO0w4tF3WAFc0OOXkbDG-a3xzP_pIOFwDCxSNvPXlbX2IXcX9kT1or3pCiA-c7_syP7rq_q53tDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ توی توییتر که با هوش مصنوعی یه مجری که مخالفش هستو میندازه توی سطل آشغال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/funhiphop/75659" target="_blank">📅 14:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75657">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تنها کلاینتی که تیم فان هیپ هاپ با بیش از ۷ سال فعالیت از لحاظ امنیت تأیید می‌کنه، کلاینت فاطمیون هست. به صورت رسمی از گارد جاویدان  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/75657" target="_blank">📅 14:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75656">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این همه پست زدم شرایط رو محیا کردم برا تبلیغ کانفیگ
ولی مهدی تبلیغی نزد
رسانه ی مردمی رو بشناسید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75656" target="_blank">📅 14:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75655">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etM6_8Ud1woBhEUH33gZeQBy5rl9WsDVgUvIG-Yoc5UP5bIjRNk-9EFj_ryzKnYRiujAgPuRZHtCAv-8SS23UcF7P-OVgL76L09gohcE0HYfy90h-e8-0aWkrHTtMfJKPwtFSjxPbm1ZnHh2WQw05FGAf-VAlQYGZvLK25465UN92bnVh2RG8Yqz-LfwY6lmHG5RyU9mpjwU4tzv6EG8hZBFtGDwzMDXXUk_dG7Z6ab8m2xp-JdbBnDNCKeA293MFWsC-oCqZ2l4t9xsdt3p1jcesxwudQwklui32XGESe5KPCqmN-2LdttkryLqMIP5BRkBnKLnvHIosGaACmGg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کلاینتی که تیم فان هیپ هاپ با بیش از ۷ سال فعالیت از لحاظ امنیت تأیید می‌کنه، کلاینت فاطمیون هست.
به صورت رسمی از گارد جاویدان
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/funhiphop/75655" target="_blank">📅 14:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75653">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوستان این بحثا برا کساییه که اطلاعات مهمی رو گوشیشون هست و آدم مهمین، شما به کیر هیچکس نیستید به راحتی میتونید از شیر و خورشید استفاده کنید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/funhiphop/75653" target="_blank">📅 14:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75651">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این اکانت داشت تبلیغ کلاینت شیر و خورشید رو میکرد  صرف نظر از حرفایی که قبلاً از شیر و خورشید زدیم، خواستم در جریان بزارمتون.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/funhiphop/75651" target="_blank">📅 14:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75650">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui7PqB2ALqg-26SqCI08yp-ZW8hN69O4Zpy97WH_GCiBvdw5dCyWM-oJhGz4LkFcwDg_sbpWdBhvrTKShKtkaf6_B8j08XUIOI0dHu1s7bjzAAvK08nTwlR-mAKFG7yqS-5pzaof0l9uCB5mPZoJWrVXtUOLIn7BX5l5AwRupRUTIOYTrPoUQjNJ6LupW3JF-yXoIxvTpmJ2-CO2TfaM0wOQQtmVDa1vHCTioix1PkALVg1GhYLrm__QJ1SELlEjfpuRXrtLiO7VwUz4kkyfTBfOjbN0JWy8NjRqKT0omwbZ_5A3winuwleNrmtsoSFW45sapufqoqJ5Ba64QBvFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اکانت داشت تبلیغ کلاینت شیر و خورشید رو میکرد
صرف نظر از حرفایی که قبلاً از شیر و خورشید زدیم، خواستم در جریان بزارمتون.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/funhiphop/75650" target="_blank">📅 14:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیدار عاصم منیر با پزشکیبان و قالیباف در تهران   @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/funhiphop/75648" target="_blank">📅 14:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75644">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxj0snOZHv_fMfDrqqXEhPxqRi2j585xEe2VPGi2n1Hy8kopEkd1XI9quZA-4L0vrT006qsLVEfSbSRD4c762CqZzdv3vztFqZD4cpMg2uoODMslE1oepn9C6d1qdW6nFTI5os6d1RRA5CY3vIyo-newOI8IcCCMimus-S5tCcdkKveg8EZ_bP34WGCTGtjkVm80yQYO9BrpvKhmsjtaG3XL-0DpElwRiV44DYNpOT8UYOTJEE_g3TUqUM9_-NhB1QbVUHxbvPnqkpSS2doHygH3PxZ-XzKS-yz8KWPBwiT2zn2fVT6jwUDUOUbrYq4cScbSDEYkwSDMjBEwDgs39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EpViqndXKP4XD8tHck6-tQqUpUVjsFEJPtJic2ad88sc1WXI1PaBSOPmENyGQPNp3EITmSxTnRtO9GQDr2Ijj65zFybWbTPjkgrc25Z62-b6pgELk9TrE1F5HrhJMOo9g4njhnvIiAVr87HZ6y7OD3SAdtLd6RUPB_aY5mckRjYRQwh5nrvkn5MyeBN8Mopa7jHZzc5SgglQDWMJZUaalSRbjBf885daaJqA21XLvUAyQgky4AozUOBNXab0gjkTCFeoFMQ_fqVTM3MFQO3dwACyZs4od_-toLdJK0rUbnuQvl2xCWdHyc_o-plw_eBGnnFiozvHacSU1wMtfUV-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJ9IstAUuQD4ixTA7TSmW8DzFdjY8_aqknCy5K9sXs7j-BUEgNc2zO7x30FpH8Nb02iP0PRstltt-qprACt0at9rDMXlnSl4GbbRSNbFmSP6HBE3gMRNlm5RZ4xaYAn4JEHMUOSAvNROktu6ZFLpocIOs9g1fyCB61cao04Ds7wk9YFM_EvUFvKiG4xKRoJ8QEy6QDVCBhaCG-yjGcxE7tBFSpWPInQw5h69Tt0SfSIK27T5_G1TCFDR8wIYNfn33jbg6eyW54jhj92eCfD28z9g6TnPZrNlNuHeACikUCYZ4f7antVi7CCuZyxGzI9b7z2FEOf3xRwMAVt-h8pWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfF-rS0RvhgC3g08E3Q4RTaPtqtMXJzeNLELF59RzD4n5_Q7T8NfhjVIk5KQ1JuWzHAiva7L5Cz9EXjUELxjRio-nK-VIaJJ_3N3lAt63ZTTwmAjnzc5VoMJE-FKSRl0gIOrj7i5NyGD_sgtPmmptI0yjZPXxKOjbu6MAuxTpXKK_N8WJVMYBZ8hN63KzcjPPPqxWF6_yZj8dl9ixq78jOnPPtyHFvjp0RFTjnLB5zSNYLpaNNV4uvMLysbjVJTFCL2iJFIwt26os3DtbJql39OmT4e6Kw-qiUUosxvCZxV5Oiy6lRHykDIbxnOOFvms-N0RDUAJ7U2vA_XAYw20Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبر سفر عاصم منیر به ایران تکذیب شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/75644" target="_blank">📅 14:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75643">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">العربیه بمب دراپ کرد:  کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران دیدار کند. ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/funhiphop/75643" target="_blank">📅 13:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75642">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVwXgsYkiTGhyix0kxUWoo5ztWszbg763ZktKofSd3YpZJYQ5iWMFSKH5oXZUAncGGS5n9beIK7Ry-uz1QV_SdJL8mh7HsxUl2hDAIT9-ki7JNZo627iioy5OpgJYIxPsBbYcp-oYQ1rLVcmUrPOy7YiZDSLrA-Rpaa91Yy2etciTdTEXilwgsFwvXHYjzvnADKj5CZYkaVeE4nvvDQHAS3G4aoTUnNdpFoQIJDg_u-JJj5esElhVaB0JeZhNl_a0bvKH7x8BxyzvgtNozsqBne43tmZM0uZJ5kkpF-BE5mZ1UmRA2qLD4wB2gmYXoZqY8hP_y7znl4kyGs-4Cg7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعریف از خود نباشه ولی من تو چنین اقلیمی هنوز خودکشی نکردم. 4  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/funhiphop/75642" target="_blank">📅 13:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75640">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvrQfOrb1tK9BSoweLO2g88gHrAPz2-pCgRt_BrRYx6L8mNoZxIosEridwXFf1n3kCVLcHY-ycGnp9kk1dHOigHzfnA78q6YXE9YA2DhoXkEEk9CrwHyLIs9aH66U2GsK4WsAm-ceQK2tSPFQ18WkyOON347pSj6v3vT3kLRCnL7rcAZyf-aCyRPOMowl5OrE7pqX6PdrL7IK7CjlrDcrg03y0HiMqpE0usZSp1p8g2PqibCQrWTIReSVN_mpMGS7RHtQ-TNQhNC70jY4V_xD2RiUKNCDPBjFTsV0t5R7L0y6Wef4KnAoI7_HvlkbEHLjuN8pelwcLPSKUMepQTpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد بی ادبید
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/75640" target="_blank">📅 12:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75639">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی:…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/funhiphop/75639" target="_blank">📅 12:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75638">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-YONB41ltLVOsuWgioWcoRkJeYSs4bGROiQq5uGndPf_xLMH7yyJMuy72sTbiXSsovr2rbWkFwUaZz7ZbpSv1TogkVFlmoINy16rMK1qkISqje2BFIyzbPOmRh-4iAvToQKzWfGKiMIy8PEe4pj-r4pdDsjnfK0jDz0r9wjXfCkovwPpLwQ-RbBeuVgZN07v3wYS4J4v54HwxFiiOQ6O_8nODcGS2wU95u39mFwEuRH5kkpPfo52XP165d1nCDhqUelmwLtSADAjCUMl2idqryotyELron-9UlCClj1YJgrWKUQwL2O8f0bi88PjA4sv70T1cEkxINY9Gg0N9Ld6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت
گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی: 5GB | 950T
10GB | 1800T
20GB | 3500T
50GB | 7500T
100GB | 13,000T
📩
خرید و پشتیبانی:
@VeloraSupports</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/funhiphop/75638" target="_blank">📅 12:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75636">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WV3Yb0fdk-wYdL0YJtXKwgfmVfx1JaPHz1daD0w-jXFS18ZWHCufOKdA5NE1FjLVZ-QP2eKpf09GrziAQ4l8cTxFs93cXJOLULHxHkqwP9i-vQiKLd8Id-jOR45K3aBVYSI0kRF6lSH4zK853oFUmTFtw8Uc0MPqpp7zhFef6ScBnRSZdh8a-ZDtR0SNH7tQ579Bnkh8poEg978WMA5g5snS0HJeEGWwSqucBo6-hDIZDIenwNrpOZZBjJKx_zGQOoZDooaXJ7DioYujurexWa4zyMr5r64JmkxPHDV6g60Y83mUdHxLKgpRQv2Grpy3-vU9eUbwVKq17ej2F402_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز اکانت اتاق جنگ اسرائیل دلقک بازیش گل کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/funhiphop/75636" target="_blank">📅 12:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75635">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش رویترز از شکست استراتژیک ترامپ:
سه ماه پس از جنگی که قرار بود در شش هفته با پیروزی قاطع به پایان برسد، ترامپ در باتلاق ایران گیر کرده است و قادر به یافتن راه خروجی حفظ آبرو یا گسترش حملات نیست.
با وجود حملات نظامی آمریکا، ایران فرو نپاشیده است؛ کنترل مداوم آن بر تنگه هرمز — که یک پنجم نفت جهان از آن عبور می‌کند — همچنان اهرم اصلی آن است.
تحلیلگران می‌گویند رئیس‌جمهوری که به پیروزی‌های خود می‌بالد اکنون با چالشی روبرو است که می‌تواند جایگاه جهانی آمریکا را بیشتر از هر درگیری در دهه‌های اخیر تضعیف کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/75635" target="_blank">📅 12:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75633">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سازمان هواپیمایی کشوری با صدور نوتام جدید، محدودیت پروازها و فعالیت فرودگاه‌های غرب کشور را تا صبح دوشنبه اعلام کرد.  @Funhiphop | ALI</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/funhiphop/75633" target="_blank">📅 12:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75632">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssFr94AHuPgrt2wY31ISL7RPlumOamF_9NpNMf0b7Xvgq5ZrPFHBJtWQRxt27zVsvrwBWAN8MQya3y4FBPh_Hbl3iSSuMGfCH98z9Nm0yr5ti6pmJtUi8HgZ-7iQ4mCTr4ek3TM5Mn4vstzyLE6ZzSGgRhHoeTqvn7eurpkZCEKwaax6XJNSs55MpUHgNhql1PDYUFBurnQ3m15ex7aBFccoluGPV8LPwf1s43FC6Q4htJGUm6e5gkBz8NweQ--zBi16QJpGkaNSbkzigiEXLya4m5UzqwfUfF4EXa-t8KPVv3GXKUHvvE0Wreu8_mPYuksMdi72cLVUumXpcPpI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو سیناب ازت میخواد که همین الان سهم ناهارتو بهش ببخشی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/75632" target="_blank">📅 11:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75627">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPv-idmHB6tjCEkH5pT3hRyTs4nGeGe2iAvYSRECzhN6Gl1dqE9nwMHlflnnQaub3Xwm7vTgbq_oVJM4pGDOUy-ro6i57eJFODT3krFuPZQPG1AGCxY6976smVPv7o1l4J82LkODyx4yNwOZj0CfleNKHBV9w8aUCIUSRHOEHILTFa9xFXT0YMmbXGh8J8h5hndK9CQkuB2y-sXluUJiir9BLLwH3yrObhVuAScQzCfje1ubaSZp3bRu_djowQ8yLObAuYTgPDgDRUA6FT3c3HJGa-9uB-5BF3Ph-2wp8wtYHs7QMMJhpaZbM__rb5DDp4_LqJwT6_3Cwd4rwqCcnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه در جهان یکیست</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/funhiphop/75627" target="_blank">📅 11:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75626">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بخت و اقبالتو گاییدم پسر  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/75626" target="_blank">📅 11:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75625">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSBSnm9oEEQef9U05nIgrgMDVCIfOKkHTyW01h4tOewnQH84arSnH5FU_tEZ0DH63brkGe5D6NMkdXTGDiyPuYywpCfpl3mKxO6v596w_Nkq32Qi5965qhjkRySO6r97337vtzn66LdHoKm2YON-03MksvqXMAqYJda2-tMmKJ016smtoVA-ttdQCb9uDQVNxuwlyNvuqJOKx6oBM-jtgL_MOE3GNHNq2NGJclQoHDi29jjGTubh8_Fu25ajfhi4CQAvM4z5Y5fsRCp-yVT5XBZ2PA5qnqnzlLDzLOpPSae2siiFz8Ea4wMPbR1UmwjGjznIfzo_gIepCwWV_bz8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخت و اقبالتو گاییدم پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/75625" target="_blank">📅 11:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75624">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">غیررسمی: آمریکا درخواست ویزای شجاع خلیل‌زاده، مهدی طارمی و احسان حاج‌صفی رو رد کرد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/funhiphop/75624" target="_blank">📅 10:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75623">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">غیررسمی: آمریکا درخواست ویزای شجاع خلیل‌زاده، مهدی طارمی و احسان حاج‌صفی رو رد کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/75623" target="_blank">📅 10:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75622">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سازمان هواپیمایی کشوری با صدور نوتام جدید، محدودیت پروازها و فعالیت فرودگاه‌های غرب کشور را تا صبح دوشنبه اعلام کرد.
@Funhiphop
| ALI</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/75622" target="_blank">📅 10:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75621">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الان رئیس صدا سیما داره فک میکنه چطوری جنگنده وارد استودیو بکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/funhiphop/75621" target="_blank">📅 10:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75620">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMD8Dvov_wCnrblyyibq9yt6Z_hNjitskrhEL53PE-DtIavaLe2i-IhvroNyWItoFD16wsDNXJ1DcqZdbFg6_dbOyCE6_lKEteAyZYrP2sIQ5VnR8cV3DR-jP3PAjSqlONR_YEPQ1ZfZ9IQtrNqvOisf7nMsqXlpob6ZZFLcorUT6On13xChafFKj-ODDi3YdYGnttTRcJceoLvr7mNr7T91fgnIW5-qiSdtMkLXoGu-ibzzC38CKW3dfJbnUwpvy4NHrZ4vVThJFVCYpthDUo8lW9om-C6TDO_zVJHCTMgL0jjB5Y5x977pYpWVOJJCRb5pUTepZ3FvNuFNTDLFzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعریف از خود نباشه تو چنین کشوری هنوز روانی نشدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/funhiphop/75620" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75619">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulpzHDkVrrGYx9NOe_uvieJ2bz5t9NJ0Nv4pxOJChivrfWpGd0JuF--Rq7QBTNJ7JjpGiLAf3u7n6EpF7eSWY9dIuokRisKkQirmztEHbA00HZhFa9wrke3qJhtfCRIwiA7N7qFkovfPHqjYO7_iZkHRERlfriBE1i-vlQXCIWAvYCZW0RP1ICkNDzhEX65vjtpVAQITLTHudDC548AAUHdscj76tpWqnTznEmAsApdXLDkBzQUF_5Z3vFACVk6IMpWoU-8dR_CffiL3cek8tNwiWmyiRR2eyqAX9xkN9ka2e4oHgPBFdM47WXRKz7cJlXQnJQ0CqM4RGnyyRiMgWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه مادری از این دراز بد قواره‌ گاییده شد</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/funhiphop/75619" target="_blank">📅 10:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75618">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrzcDE3aAGN6VfpRTDKXf18OA2TI0uC9Br41aqgm7DsHkuuJlFspof41S5sKZCkLlwPzpkpxY3c67K_aOM8es2eeeg2zzE2LbFtzmUaOrGOBk7izo2XPQFtbiuiw_U-GbF3jfhD0DpxEuA7qoQNXs2WpgsNJe5NhKzDqoqSpzNLQTpKXdOtsZZ2INrvjbvA_z8WZ7O5ADw-LVfHsN-XjkSHU0g7mPYqLsfZUnpJPb91zQVi8tHmyNZ0M4SWx20RAp1De-RtWsZL5m8C-UABlKj8_O6JE_pxCjg4aTyR6BLwsH1TM-iQfCQSSqbnEIj1Toh-sx4BZRrz6mWIKhDy6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/funhiphop/75618" target="_blank">📅 10:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75615">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سخنگوی وزارت دفاع و پشتیبانی نیروهای مسلح، سردار طلایی‌نیک:
ترامپ چاره‌ای جز پذیرش خواسته‌های مردم ایران و احترام به حقوق کشور ما ندارد.
عدم احترام حقوق ایران منجر به شکست‌های بیشتر برای ترامپ خواهد شد.
در میدان نبرد و دیپلماسی به یک اندازه، برآورده کردن خواسته‌های مردم ایران تنها راه خروج از جنگ سوم تحمیلی بر دشمن آمریکایی صهیونیستی است.
همچنین ترامپ باید با پذیرش پیشنهاد ایرانی، مراقب جلوگیری از خسارات و هزینه‌های بیشتر ناشی از ادامه جنگ باشد، چه برای مردم آمریکا و چه برای جامعه بین‌المللی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/funhiphop/75615" target="_blank">📅 09:16 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
