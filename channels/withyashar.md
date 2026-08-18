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
<img src="https://cdn4.telesco.pe/file/F-SGYdIGiiwuCQU0fLQ65rX84GkT9Z69kfbu4EscahQXjuZUgEj8eUGfEIjBufSyGZ2POu7svTMdXrDP6gK2fu2F7ZZkDzZjTLBGsiKI2AhEE5ZnHv53OB4E0mkM9T2zujZTUh11ZK1nA_9i8c4n9RdAhqENsFU_l4x3RZ724lpAgDZjwQez-msEDP0e4haZWH8XY0ojo04KM-rRCD3ixoecWLlc0E_TQ9ateStcBWXzIuU_T-YeOfjqzo5qSwg38WX3yOLgbgNA86wHsl2eYn2h9jsBnfDsPkGKmyvgFHCMDiXj3oX0T7Ychbvr25KcIcIaJPkKlTF9FwB9yCOrRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 11:30:13</div>
<hr>

<div class="tg-post" id="msg-21149">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بوشهری های عزیز خنثی‌سازی هست اعلام شده
@WarRoom</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/withyashar/21149" target="_blank">📅 11:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21148">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بلومبرگ : با اعلام عدم تمایل دونالد ترامپ، رئیس جمهور آمریکا به تمدید توافق رو به پایان با ایران و تشدید تنش‌ها در تنگه هرمز، چشم‌انداز صلح در خاورمیانه با رکود تازه‌ای مواجه شد.
@WarRoom</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/21148" target="_blank">📅 10:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21147">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">العربیه : منابع ارشد کورد عراقی می‌گویند نیچروان بارزانی، رئیس اقلیم کردستان، طی دو ماه گذشته دو بار در بغداد با اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، دیدار کرده و در چارچوب میانجی‌گری محرمانه میان آمریکا و ایران، پیام‌هایی را رد و بدل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/21147" target="_blank">📅 10:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21146">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عراقچی ، وزیر امور خارجه: اسرائیل تمام تلاش خود را برای جلوگیری از دستیابی به توافق‌نامه و عدم اجرای آن به کار بست و این تلاش‌ها همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/withyashar/21146" target="_blank">📅 10:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21145">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1PBNy7mSwdtv21Gem4Aqxkldpl-JWCI4955wMLFhHu4GTn585YWwi7zbLZaQ-Ip1aoHQa0WXfZwzubnGXdN-sf8p45BQsKd4ey6vsoF3UcJdOhfqJBrIBtZeyV9P4mglL1G_lY72rw0hTO-fd5Rr6KTlfNAgp8nB-AzEfNpVelfdmqrPo6YaMGneULRjsyvwrfVU-0bGfarrEdcIM4wZgHabfa8FElAVxIIkv_iIMeWT1uK2Xs_uhsUiTPhy7iu1q7VmsMWoFMhTBqNX__NCdhxBMpFPUbB3lkbFH7fWBnABqok7vYxYDxXibKS6Txrj7GA5X0oawbwNHWIDHzdgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش UKMTO یک کشتی هنگام عبور از تنگه هرمز به سمت بیرون، توسط یک موشک/پهپاد مورد اصابت قرار گرفت.
برخورد باعث آسیب به موتورخانه و زخمی شدن یک عضو خدمه شد، در حالی که سایر اعضای خدمه توسط گارد ساحلی عمان کمک رسانی می‌شوند.
تاکنون هیچ تأثیر زیست‌محیطی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/21145" target="_blank">📅 09:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21144">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مایک جانسون، رئیس جمهوری‌خواه مجلس نمایندگان آمریکا امروز در گفت‌وگو با خبرنگاران گفت جنگ با جمهوری اسلامی یکی از عوامل افزایش قیمت بنزین بوده است، اما مردم قدردان این موضوع هستند که آمریکا با برخورداری از «بزرگ‌ترین نیروی نظامی» در تاریخ جهان، توانست
«سر مار را قطع کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/21144" target="_blank">📅 04:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21142">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/21142" target="_blank">📅 03:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21141">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkp_xYQKA4dH5wHO-ybofpowhDZMfW-FcHAz1N1kc4dRYzAO24k4xrZytrXYvy24mgz6Yv1MVWDkhAed7y3TdSu4gvarIa6vVNb-U-mOARO_3-vwJaHoZU6hMzAoUwvskPJwBBnPQBwXUnnuTRlyrtG7IAiXJDTLjFhZ49jZiAM_RUmswVHsPNsb1Ii0YaBz_uUE2jxCBmPVpxs-Qhks6GjnD0Nn9Rkyk3pqqV5Q6dlwe2TtgUEudJn9ivxxLFsuJyluCRd0VWbsPBGkqHO2kDGL4DQOunHFENndGK3urr1zbUfpI-xn6szf_bOuk9DjI3cK9hv6P6ld1WIvbpS1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@WarRoom
🕰️</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/21141" target="_blank">📅 02:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21140">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/21140" target="_blank">📅 02:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21139">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromali</strong></div>
<div class="tg-text">اقا یاشار خسته شدیم بخدا بگو کی میزنن</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/21139" target="_blank">📅 02:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21138">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">العربیه: ممباقر قالیباف، رئیس مجلس ایران چهارشنبه آینده به بغداد سفر خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/21138" target="_blank">📅 01:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21137">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دفتر ریاست جمهوری ترکیه: اردوغان در تماس تلفنی با ترامپ بر اهمیت ادامه گفت‌وگوها با ایران ابراز داشت و بر آمادگی ترکیه برای مشارکت تأکید کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21137" target="_blank">📅 01:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21136">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آتش‌سوزی میدان شهرداری گرگان
این حادثه ساعت ۱۹:۱۵ دقیقۀ شامگاه دوشنبه رخ داد که بالغ بر ۲۰ باب مغازه در این حادثه آسیب دیده و دچار آتش‌سوزی شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21136" target="_blank">📅 00:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21135">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چند گزارش تایید نشده از پرواز یک اسکادران جنگنده از سمت مازندران به تهران مشابه با زمان جنگ @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21135" target="_blank">📅 00:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21134">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چند گزارش تایید نشده از پرواز یک اسکادران جنگنده از سمت مازندران به تهران مشابه با زمان جنگ
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21134" target="_blank">📅 00:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21133">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIGJjS7V2d1sDt62VzSJPEjatS6KBwUY5ZpI9A2CQryO7s1bvSfIs0harTK8NfId__a2WHGO39SDEE_s7-yHKtwCf0yN54twFCytTnLcPGuvl0rYsZ4KBCDNEo7TPqPJF6WK0VCfeLWiS0Mky04R5-re50wNHP6P6vfbzW3i5UuEVaqLFK7Ix1ormqFIjz-5Tu244MUxmXmQeXp1jFEv40BSOseg4xwcFNZmKGnVBxA8TO0EGt3QUtvJTjsCZDeXRcQ0s7NmJIE8bV14kb2KXkZFLWewaeLtGMVamP6MtK94P2vMFTDGSk5Oqz0yPloAjjcAUvuFWVDZsFMhnQVqnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث شوخی با رهبر کره شمالی:
کیم : هی دونالد، با هم اوکی‌ایم… مگه نه؟
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21133" target="_blank">📅 00:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21132">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مدیرعامل مخابرات : سرعت اینترنت بزودی با مهاجرت از کابل مسی به فیبر نوری تا 8 برابر زیاد میشه!
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21132" target="_blank">📅 00:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21131">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اکسیوس به نقل از یک مسئول آمریکایی: کوشنر به نتانیاهو اطلاع داده است که واشنگتن می‌خواهد اسرائیل اقداماتی کوچک در غزه انجام دهد تا جدیت حماس را بسنجد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21131" target="_blank">📅 22:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21130">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کوشنر به فاکس‌نیوز: اگر ایران حاضر باشد توافقی را که تاکنون با ما درباره آن مذاکره کرده‌ایم نهایی کند و توانایی ساخت سلاح‌های هسته‌ای را کنار بگذارد، طبیعتاً ترامپ هم آماده توافق است. اما در حال حاضر، ایران هیچ نشانه‌ای از تمایل به انجام کاری که از نظر ما منطقی باشد، نشان نمی‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21130" target="_blank">📅 22:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21129">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کوشنر به فاکس نیوز: اسرائیل نگرانی‌های موجهی را ایجاد کرده بود که ما توانستیم به آنها رسیدگی کنیم و برخی از ابهامات مربوط به طرح را برطرف کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21129" target="_blank">📅 22:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21128">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کان نیوز اسرائیل : احتمال شروع مجدد جنگ بسیار بالاست
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21128" target="_blank">📅 22:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21127">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2bdcb1f8.mp4?token=SHdpl3bo89G1Xx_PA_mEi9OGz-JY0ZJfapC_1Eda4lIjhdTHzF49p4_rsQ0JjVyNiwyHHpIYJ9BIOuyb_IBp3gPOPocntT3u_MNvp0xkq6Sv35nSp0Nz9v_hwJUW67fvHBM08ImUkYPSTnVg3_De40LPBgEXhN-q_kFJU7YjVeKE2ezEvboGE3-m0WndZM5cbdAPY5kbYPhQp258EQmDKlGTd0c8kr2mAPDDyQRD8FLZUdDuxPeg2Rq_yKXIPbCLirEMzgZMsQheLEw7dHp5s8A5m780NWnPBo6De1bQkWTNV_kjB0DJDT1wGSW_10X8R3OUrp3VNXaODvGU9XByBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2bdcb1f8.mp4?token=SHdpl3bo89G1Xx_PA_mEi9OGz-JY0ZJfapC_1Eda4lIjhdTHzF49p4_rsQ0JjVyNiwyHHpIYJ9BIOuyb_IBp3gPOPocntT3u_MNvp0xkq6Sv35nSp0Nz9v_hwJUW67fvHBM08ImUkYPSTnVg3_De40LPBgEXhN-q_kFJU7YjVeKE2ezEvboGE3-m0WndZM5cbdAPY5kbYPhQp258EQmDKlGTd0c8kr2mAPDDyQRD8FLZUdDuxPeg2Rq_yKXIPbCLirEMzgZMsQheLEw7dHp5s8A5m780NWnPBo6De1bQkWTNV_kjB0DJDT1wGSW_10X8R3OUrp3VNXaODvGU9XByBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : ایالات متحده به دنبال تمدید تفاهم‌نامه با ایران نیست
ایران در دردسر بزرگی افتاده است. کشورشان آشفته است.
ارتش آنها کاملاً شکست خورده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21127" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21126">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ در مورد ایران:
من ایده اعلام تنگه هرمز به عنوان قلمرو ایالات متحده را دوست دارم.
ما کنترل کامل بر تنگه داریم.
ما در حال خارج کردن میلیون‌ها بشکه نفت در هفته هستیم - شاید این متوقف شود، یا شاید حتی بیشتر باز شود.
تنگه باز است و قیمت نفت در حال کاهش است و این روند همچنان ادامه خواهد داشت مگر اینکه تصمیم بگیریم کاری بسیار شدیدتر از آنچه انجام می‌دهیم انجام دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21126" target="_blank">📅 21:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21125">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa62990739.mp4?token=nG8TaKJpCV8Dv2-ngO7omAz8cwTouxxeyCY_JZhwxIttu6wp9X0GHOybkckWma3IwBCfNd7DU12ZMq6ega5KRKHmrIA7BAjkef1Hp8a_ZgpugO09uJqqSnnMns54NXEE1wYHfhIDe7n2QRds0EsYnMZ2GbovO0AfxTaOm8wtzi7wMYzGHvhbqVxZxZ0IC9K5yJ45xKd_zkk37jUeVnS-e-uCV638KLSSitc2nCr791YHV7ibeHQaYslSh7JO7WrpItaN-1GFH-DugydFOJ_XceVPI5tRHmWC4Ptjwd93st2oc-v6vDfbuakYXT6zoMYbwpc5grVJfAZDuspB9iydojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa62990739.mp4?token=nG8TaKJpCV8Dv2-ngO7omAz8cwTouxxeyCY_JZhwxIttu6wp9X0GHOybkckWma3IwBCfNd7DU12ZMq6ega5KRKHmrIA7BAjkef1Hp8a_ZgpugO09uJqqSnnMns54NXEE1wYHfhIDe7n2QRds0EsYnMZ2GbovO0AfxTaOm8wtzi7wMYzGHvhbqVxZxZ0IC9K5yJ45xKd_zkk37jUeVnS-e-uCV638KLSSitc2nCr791YHV7ibeHQaYslSh7JO7WrpItaN-1GFH-DugydFOJ_XceVPI5tRHmWC4Ptjwd93st2oc-v6vDfbuakYXT6zoMYbwpc5grVJfAZDuspB9iydojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا غذای کافی در ناو یو اس اس لینکلن وجود دارد؟
ترامپ: وجود دارد. آن یک گزارش جعلی سی ان ان بود.
در طول این سال‌ها، ما آنها را خیلی بیشتر آنجا نگه داشته‌ایم.
یک دریاسالار به من گفت: «من خیلی بیشتر از این روی کشتی‌ها بوده‌ام، قربان.» و افراد حاضر در ناو لینکلن می‌گویند که به خوبی از آن مراقبت می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21125" target="_blank">📅 21:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21124">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef700568c.mp4?token=ofrshEBB7j27QQdHV_6VqgIrOHWwHp25spxRnc0fEYMA-4o61RkJs2YuH_IsVlSDiIO6JBle1cZFfrWrgNE4vNdrEUGDu8DfgGPBFZ9bL0SMw4mmuNjFNkXJBxqBTreOVRaSBcMjeqZ-LACR61xGGuKRALJTHX30q2cyheDrv93cECxl8kkdZ2wRdOdcdRDi0gjWJ0-L8gU-5vR_owCi8dos--Eu9hvnO4R31fehVKBOt4cuvRQyLyzGpIs6Q6GmX9imwKi04YoyBErPEUmBR719qfOXYETaUUC2_PyorwrbLqnBD56qUkU9vlPWaTWlCcLMZZI3ld3U8w88dBJiT30kXYbJ--mQt-bvP4RwdzFNxxHKWmw_mR_kXkO6s-oajQmY4VxaGwyDVERBIUlDEWuOdQW44uWL5zysf4Kgz6-E0dEgpWf8dbT_M5Qq4vHdrRgDI-1TDtxnOL8rfMhzl4MYQ_j2QtDn2OUoP9oMHGSbOPVbv77f1RGgBNb-9wtVYP16mE6lYHvbatzizWWT-FnEmoUSKwYnoHLW8l2AH5ca-u2yoPaNVqc40993OlF6XklQBx6HvHK_pcPYSCTOLQw-malAjAJbmtAdRHpCb8tK8oASpJBuMniZk4_21PP9c2n0Exu4xOD6a48BA20qmL_OvJ-F7Js-z-X2NQTrPI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef700568c.mp4?token=ofrshEBB7j27QQdHV_6VqgIrOHWwHp25spxRnc0fEYMA-4o61RkJs2YuH_IsVlSDiIO6JBle1cZFfrWrgNE4vNdrEUGDu8DfgGPBFZ9bL0SMw4mmuNjFNkXJBxqBTreOVRaSBcMjeqZ-LACR61xGGuKRALJTHX30q2cyheDrv93cECxl8kkdZ2wRdOdcdRDi0gjWJ0-L8gU-5vR_owCi8dos--Eu9hvnO4R31fehVKBOt4cuvRQyLyzGpIs6Q6GmX9imwKi04YoyBErPEUmBR719qfOXYETaUUC2_PyorwrbLqnBD56qUkU9vlPWaTWlCcLMZZI3ld3U8w88dBJiT30kXYbJ--mQt-bvP4RwdzFNxxHKWmw_mR_kXkO6s-oajQmY4VxaGwyDVERBIUlDEWuOdQW44uWL5zysf4Kgz6-E0dEgpWf8dbT_M5Qq4vHdrRgDI-1TDtxnOL8rfMhzl4MYQ_j2QtDn2OUoP9oMHGSbOPVbv77f1RGgBNb-9wtVYP16mE6lYHvbatzizWWT-FnEmoUSKwYnoHLW8l2AH5ca-u2yoPaNVqc40993OlF6XklQBx6HvHK_pcPYSCTOLQw-malAjAJbmtAdRHpCb8tK8oASpJBuMniZk4_21PP9c2n0Exu4xOD6a48BA20qmL_OvJ-F7Js-z-X2NQTrPI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با رئیس جمهور کره جنوبی تماس گرفتم. گفتم: «آیا در مورد ایران کمک می‌کنید؟ اگر مایل باشید، ما به کمک نیاز نداریم.» او گفت: «نه، ممنون.»
گفتم: «منظورت چیست؟ ما ۳۹۰۰۰ سرباز آنجا داریم که از شما در برابر کیم جونگ اون محافظت می‌کنند، و شما قرار نیست در مورد ایران به ما کمک کنید؟ این عجیب است.»
پس چرا ما درگیر کمک به شما هستیم؟ محافظت از کره جنوبی میلیاردها دلار برای ما هزینه دارد.
ایرانی ها می‌خواهند به توافق برسند، اما قرار نیست آن نوع توافقی را که من احساس می‌کنم لازم است، انجام دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/21124" target="_blank">📅 21:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21123">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حمله پهپادی ایران به دفتر بارزانی مسعود بارزانی: در پی تحقیقات واحد ضدتروریسم کردستان، دفتر شخصی من و منزل رئیس سازمان امنیت و اطلاعات، امروز هدف حملات پهپادی ایران قرار گرفتند. من این حملات بی‌پروا و غیرقابل‌قبول را به شدیدترین شکل ممکن محکوم می‌کنم. این…</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/21123" target="_blank">📅 21:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21122">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d960334267.mp4?token=DL6unB-fvWI4s1kvTkG1KN6cw37AOmJaMRYBQXc7bMzxCbiUmUbnMxC5LmwOymHB3cf3IxacO5D__JS2QvdpxrLTXWtyqri60MfowJmZ80syK5qdzmQmCwCXWGPqL1HdUAZgFElOYmh3XFz1GvceWrHfs_jOPeYJXqC9O48-DK2ohpmOlXgRhyaV968uEud4VHqNyBaZvrM3zQU7MnwiJnQVxJ5HKwgZ0MVHKA_RDanur1tRQl0pqYvoFY62max2AnQNC_K3vinJK76cjnGuamj2dTuvsxzA3SIP8fSLMgpvty-a2rM_bTzjlZMdxfFbdnt6GwwfgfV1G63AxMTpiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d960334267.mp4?token=DL6unB-fvWI4s1kvTkG1KN6cw37AOmJaMRYBQXc7bMzxCbiUmUbnMxC5LmwOymHB3cf3IxacO5D__JS2QvdpxrLTXWtyqri60MfowJmZ80syK5qdzmQmCwCXWGPqL1HdUAZgFElOYmh3XFz1GvceWrHfs_jOPeYJXqC9O48-DK2ohpmOlXgRhyaV968uEud4VHqNyBaZvrM3zQU7MnwiJnQVxJ5HKwgZ0MVHKA_RDanur1tRQl0pqYvoFY62max2AnQNC_K3vinJK76cjnGuamj2dTuvsxzA3SIP8fSLMgpvty-a2rM_bTzjlZMdxfFbdnt6GwwfgfV1G63AxMTpiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: امروز صبح گفتی اگه عمان سر راهت قرار بگیره، تا خرخره بمبارانش می‌کنی.
ترامپ: فکر نمی‌کنم رفتارشون خیلی خوب باشه، اما ما باهاشون کنار می‌آییم.
@WarRoom</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/21122" target="_blank">📅 21:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21121">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بررسی داده‌های پرواز فعالیت همزمان دو فروند هواپیمای E6B-Mercury فرماندهی و کنترل راهبردی آمریکا در آسمان خبر می‌دهند.این هواپیما ها بخشی از سامانه ارتباطی آمریکا برای حفظ ارتباط با زیردریایی‌های حامل موشک و نیروهای راهبردی است و لزوماً به معنی آغاز حمله هسته‌ای…</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/21121" target="_blank">📅 21:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21120">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89161c6b5.mp4?token=C4NPhDTRutttRpXPjzQEh9zv-81Z7KAVy7cCZRdC8mHl5n4BToF0tUMbBAZS5QS-mgV_Ttv-1HudxjYxhmFJBZDk6x-S9VmKoPcw6Nz92aPRev_gvaBsV6atnP_CbXq2A0XWKl0D2ZrDk9se53j8xSPaqtZSNZyykm5EcH5EUfkS5in-0wvdpX23rYoUHyQdkUr1qXcr3Yw-53BZ5-pLldfduUaRI6bKg-Rz_vSFw4hbScHEFOih8PEVldYv5E8W9P_WNYNXnHJ-GKqGZjf83H59vhzWDCw9fhaWnltVjLl_MgT0fcQnocRXbIug-X5OghEQl7moI8g10HnEk0T41w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89161c6b5.mp4?token=C4NPhDTRutttRpXPjzQEh9zv-81Z7KAVy7cCZRdC8mHl5n4BToF0tUMbBAZS5QS-mgV_Ttv-1HudxjYxhmFJBZDk6x-S9VmKoPcw6Nz92aPRev_gvaBsV6atnP_CbXq2A0XWKl0D2ZrDk9se53j8xSPaqtZSNZyykm5EcH5EUfkS5in-0wvdpX23rYoUHyQdkUr1qXcr3Yw-53BZ5-pLldfduUaRI6bKg-Rz_vSFw4hbScHEFOih8PEVldYv5E8W9P_WNYNXnHJ-GKqGZjf83H59vhzWDCw9fhaWnltVjLl_MgT0fcQnocRXbIug-X5OghEQl7moI8g10HnEk0T41w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا به دستیابی به توافق نهایی درباره ایران نزدیک‌تر شده‌اید؟
ترامپ:
بگذارید ابتدا برنامه‌مان با رایدر را تمام کنیم؛ بعد از آن به چند سؤال از این دست پاسخ خواهیم داد
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/21120" target="_blank">📅 21:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21119">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سنتکام : تا امروز، نیروهای ما ۶۴ کشتی تجاری را تغییر مسیر داده، ۳ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده‌اند تا از رعایت مقررات اطمینان حاصل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/21119" target="_blank">📅 20:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21118">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اتاق جنگ با یاشار : یک سر اگه به لایک های دو پست اخر نوید محمدزاده بزنید و ببینید چه کسانی ‌لایک کردن ، کمی بهتر با آدمهای اطرافتون آشنا میشوید.
@WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/21118" target="_blank">📅 20:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21117">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مارک لوین : رژیم ایران قصد تسلیم شدن نداره؛ ما قبلا هم با دشمنانی مثل ژاپن روبه‌رو شدیم که حاضر به تسلیم نبودن و مجبور شدیم برای تسلیم‌شدنشون از دو بمب اتم استفاده کنیم. البته الان قصد چنین کاری رو نداریم، اما رژیم ایران هم حاضر به تسلیم نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21117" target="_blank">📅 20:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21116">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f0c900572.mp4?token=gCe2svM8wVU9FlQNFSg76LCbyAG4mnkgpU_6t9BVuHkSwyaPMqZ4hQzr-D2xiTSiQlF5RX1XVMSRacWyyJM3OYVqm71xY9DU4Z52K6ov3rCyryBX2uqMSFaNVw-UpSZ-vDvfA07gA-zFbtnIch6pXSJrFNZPUhBgYJ1-jBupcTnPONwWPMd-tIldAkmb4kzrOqq9bCp6CMyADUFMPljK3_1TcMQPWA-hWq9uQsUJQlM97O6tTRpTB7Hy1Vjh9XnhKQGE1qwRBEybapjuJiRSJYtAvncU0TJazgA86Ukv840cd7uPieHWzwn--ardeTfnZKvwhTV7zBIAzTMEBrxMuaPJ_Z537ijCo8kUlLUtS67Zi1qMSPOhbbLobzIAwNbv-MTshrMuJScYSfVyi0R0kx-emPvn0N84bXCM0aQ6cgNDFQIuXcNmeE004eqsGgvMxMiDQWV9R1NkGiazlTxK1zn7Qeb-Asew-YSWDBIgdvUDgkPDiNiGy_SSBXbV-W_BRcff3nRSMoU6o5Pu4P9I4LjOhz1FOIjmt8CqQR3THIuYBZ_KpZ3NvCnIoN_Vg2j4ZXFoxizRWxSuzr0CB0WydhnS7wrRiQ4xLY7qoi19oovEo6DWbp1OURc0ASYQpDZDGHZbcSelx2-wjzTRdu9pUgHGfOB3RFnJUf57H1FLyiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f0c900572.mp4?token=gCe2svM8wVU9FlQNFSg76LCbyAG4mnkgpU_6t9BVuHkSwyaPMqZ4hQzr-D2xiTSiQlF5RX1XVMSRacWyyJM3OYVqm71xY9DU4Z52K6ov3rCyryBX2uqMSFaNVw-UpSZ-vDvfA07gA-zFbtnIch6pXSJrFNZPUhBgYJ1-jBupcTnPONwWPMd-tIldAkmb4kzrOqq9bCp6CMyADUFMPljK3_1TcMQPWA-hWq9uQsUJQlM97O6tTRpTB7Hy1Vjh9XnhKQGE1qwRBEybapjuJiRSJYtAvncU0TJazgA86Ukv840cd7uPieHWzwn--ardeTfnZKvwhTV7zBIAzTMEBrxMuaPJ_Z537ijCo8kUlLUtS67Zi1qMSPOhbbLobzIAwNbv-MTshrMuJScYSfVyi0R0kx-emPvn0N84bXCM0aQ6cgNDFQIuXcNmeE004eqsGgvMxMiDQWV9R1NkGiazlTxK1zn7Qeb-Asew-YSWDBIgdvUDgkPDiNiGy_SSBXbV-W_BRcff3nRSMoU6o5Pu4P9I4LjOhz1FOIjmt8CqQR3THIuYBZ_KpZ3NvCnIoN_Vg2j4ZXFoxizRWxSuzr0CB0WydhnS7wrRiQ4xLY7qoi19oovEo6DWbp1OURc0ASYQpDZDGHZbcSelx2-wjzTRdu9pUgHGfOB3RFnJUf57H1FLyiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما رژیم اومده یه برنامه تلویزیونی طنز ساخته که ترامپ رو توش مسخره میکنن
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21116" target="_blank">📅 20:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21115">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فارس: یک نفتکش با مالکیت یکی از کشور های حوزه خلیج فارس در تنگه هرمز در نزدیکی قشم توقیف شد
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/21115" target="_blank">📅 19:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21114">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اتاق جنگ با یاشار : در جریان جنگ ایران و عراق، اسرائیل برخلاف مواضع علنی جمهوری اسلامی، به‌صورت محرمانه به ایران سلاح و تجهیزات نظامی می‌فروخت؛ از جمله
موشک‌های ضدتانک تاو، موشک‌های هاوک، موشک‌های لنس، مهمات و قطعات یدکی هواپیما و تانک
. در سال ۱۹۸۱ نیز یک قرارداد
۱۳۶ میلیون دلاری
شامل موشک‌های لنس، هاوک و مهمات هدایت‌شونده
کوپرهد
میان طرفین انجام شد ، حسین شیخ‌الاسلام، قائم‌مقام وقت وزارت امور خارجه و از افراد درگیر در مذاکرات ایران با هیئت آمریکایی مک‌فارلین در یک مصاحبه درباره کمک‌های تسلیحاتی اسرائیل به ایران گفت :
فتح فاو بدون موشک‌های تاو و هاوکِ به‌دست‌آمده از این معاملات ممکن نبود.
هم‌زمان، اسرائیل برای تضعیف عراق مستقیماً وارد عمل شد؛ یکی از مهم‌ترین اهداف،
راکتور هسته‌ای اوسیراک در نزدیکی بغداد
بود. ابتدا
ایران به این تأسیسات حمله کرد
و در ۳۰ سپتامبر ۱۹۸۰ جنگنده‌های ایرانی راکتور را هدف قرار دادند، اما آن حمله نتوانست تأسیسات را به‌طور کامل نابود کند. حدود هشت ماه بعد، در ۷ ژوئن ۱۹۸۱، اسرائیل در
عملیات اپرا
با جنگنده‌های F-16 و F-15 به اوسیراک حمله کرد و راکتور را به‌طور کامل منهدم کرد؛ به این ترتیب، حمله اسرائیل عملاً کار نیمه‌تمام حمله ایران را به پایان رساند. بعدها ابعاد همکاری محرمانه تسلیحاتی ایران و اسرائیل با انتشار گزارش‌ها و اسناد و سپس در جریان
ماجرای ایران-کنترا
آشکارتر شد. به خمینی گفته شد محموله سلاحی که ایران به آن دست یافته اسرائیلی است، خمینی پس از مکثی گفت :
«اگر این سلاح‌ها را به دست آورده ایم ، آیا لازم است بپرسید فروشنده چه کسی است؟»
و وقتی پاسخ شنید «نه»، گفت :
«پس مشکل حل شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21114" target="_blank">📅 19:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21113">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Flower 3
@WarRoom</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/21113" target="_blank">📅 19:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21112">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پروژه
فلاور (Project Flower)
در سال ۱۹۷۷ میان ایران و اسرائیل آغاز شد؛ یک همکاری محرمانه موشکی که ایران هزینه و نفت پروژه را تأمین می‌کرد و اسرائیل فناوری و دانش فنی را در اختیار ایران می‌گذاشت.
در فاز نخست، توسعه یک موشک پیشرفته دریابه‌دریا با برد حدود ۲۰۰ کیلومتر
دنبال می‌شد و در
فاز دوم، توسعه موشک بالستیک جریکو-۲ با برد حدود ۱٬۵۰۰ کیلومتر
در برنامه قرار داشت. برای اجرای پروژه، ایران در نزدیکی
سیرجان
تأسیسات مونتاژ موشک و در حوالی
رفسنجان
محل آزمایش در نظر گرفته بود و بخش‌هایی از زیرساخت و همکاری فنی نیز ایجاد شده بود. ایران همچنین در سال ۱۹۷۸ حدود
۲۸۰ میلیون دلار نفت
به‌عنوان پیش‌پرداخت پروژه در اختیار اسرائیل قرار داد. با وقوع انقلاب ۱۳۵۷، پروژه متوقف شد و متخصصان و کارشناسان اسرائیلی ایران را ترک کردند؛ در نتیجه بخش قابل‌توجهی از تأسیسات و زیرساخت‌های ایجادشده برای پروژه، بدون تکمیل نهایی برنامه باقی ماند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21112" target="_blank">📅 19:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21111">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Flower 2
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/21111" target="_blank">📅 19:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21110">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Flower 1
@WarRoom</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/21110" target="_blank">📅 19:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21109">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اتاق جنگ با یاشار : در ماه‌های پایانی اتحاد شوروی، جورج اچ. دبلیو. بوش برخلاف انتظار، نه‌تنها از شوروی و گورباچف با ادبیات تهاجمی سخن نمی‌گفت، بلکه از اصلاحات او، شجاعت سیاسی‌اش و دستاوردهایش تمجید می‌کرد و تأکید داشت که آمریکا خواهان حفظ روابط نزدیک با دولت شوروی است. بوش حتی در اوت ۱۹۹۱ در کی‌یف، استقلال‌طلبان اوکراینی را از جدایی شتاب‌زده برحذر داشت و از ادامه اتحاد اصلاح‌شده شوروی حمایت کرد؛ تنها ۱۴۵ روز بعد، اتحاد شوروی برای همیشه فروپاشید. این همان نقطه‌ای است که مفهوم «فریب راهبردی» اهمیت پیدا می‌کند: قدرت بزرگ لزوماً قدرت واقعی خود را به رخ نمی‌کشد؛ گاهی با تعریف از رقیب، اطمینان‌بخشی، مذاکره و ایجاد احساس امنیت، او را از درک کامل موازنه واقعی بازمی‌دارد. امروز نیز می‌توان همین الگو را در برابر جمهوری اسلامی مشاهده کرد؛ آمریکا از مذاکره و توافق سخن می‌گوید، اما هم‌زمان فشار اقتصادی و نظامی خود را حفظ می‌کند. اگر این یک راهبرد آگاهانه باشد، هدف این نیست که تهران صرفاً تصور کند آمریکا ضعیف است؛ هدف این است که
نتواند بفهمد آمریکا واقعاً چه مقدار قدرت، صبر و گزینه‌های پنهان برای مرحله بعد در اختیار دارد.
همان بازی‌ای که در ماه‌های پایانی شوروی، با خویشتن‌داری و اطمینان‌بخشی پیش رفت و سرانجام جهان را با فروپاشی یکی از دو ابرقدرت آن دوره روبه‌رو کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21109" target="_blank">📅 18:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21108">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">متکی ,نماینده تهران در مجلس :
۹۰ روز آینده بسیار مهم است
نظم آینده منطقه به نتیجه این جنگ بستگی دارد چون نتیجه جنگ مشخص می‌کند آرایش منطقه‌ای چگونه خواهد بود.بنای آمریکا اجرای تفاهم‌نامه نیست و قرار است ما فقط مشغول مذاکره باشیم تا آنها انتخابات را ببرند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/21108" target="_blank">📅 18:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21107">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ادعای سی‌ان‌ان : کوشنر بیش از چهار ساعت نتانیاهو را تحت فشار قرار داد تا طرح آتش‌بس ترامپ برای غزه را پیش ببرد،  اما نتانیاهو در برابر این فشار مقاومت کرد و با اشاره به انتخابات اکتبر، تأکید کرد که پیش از هرگونه عقب‌نشینی اسرائیل، حماس باید به‌طور کامل خلع…</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/21107" target="_blank">📅 18:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21106">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یک منبع دیپلماتیک پس از ملاقات کوشنر و نتانیاهو: در این ملاقات، به طور مشخص توافق شد که بازسازی نوار غزه قبل از خلع سلاح کامل حماس آغاز نشود. همچنین، تاکید شد که سیاست پیشگیری (حمله پیش از وقوع) در مواردی که خطر آسیب رساندن به نیروهای ارتش اسرائیل وجود داشته…</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/21106" target="_blank">📅 18:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21105">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کلودفلر :
ترافیک اینترنت بین الملل ایران از ۹۰ درصد به ۵۹ درصد رسیده ،وضعیت الان اینترنت ایران دقیقا مثل روزای قبل از قطعی ۸۸ روزه ی اینترنته و با اختلالات بسیار سنگین همراه شده.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21105" target="_blank">📅 17:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21104">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ظریف : قرار بود بعد رفتن آمریکا از افغانستان، نظام شاهنشاهی اونجا مجدد برگرده اما ما نزاشتیم و کمک کردیم طالبان قدرت بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/21104" target="_blank">📅 17:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21103">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/21103" target="_blank">📅 17:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21102">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رویترز : ایران به آمریکا ضرب‌الاجل داد
ایران از طریق پاکستان به آمریکا وقت داده که در عرض یک یا حداکثر دو هفته محاصره دریایی رو رفع و سر دیپلماسی برنگرده وضعیت براشون بد میشه
سپاه گفته در صورت تمام شدن ضرب‌الاجل جنگ رو گسترده و تمامی منافع نظامی و سیاسی و اقتصادی آمریکا در کل منطقه موشک باران میشن
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21102" target="_blank">📅 17:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21101">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک منبع دیپلماتیک پس از ملاقات کوشنر و نتانیاهو:
در این ملاقات، به طور مشخص توافق شد که بازسازی نوار غزه قبل از خلع سلاح کامل حماس آغاز نشود.
همچنین، تاکید شد که سیاست پیشگیری (حمله پیش از وقوع) در مواردی که خطر آسیب رساندن به نیروهای ارتش اسرائیل وجود داشته باشد علیه تروریست‌ها ، ادامه داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21101" target="_blank">📅 17:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21100">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رسوایی برای نخست‌وزیر جدید بریتانیا: او با فردی که خود را به عنوان یک مقام ارشد در کاخ سفید جا زده بود، مکاتبه کرد
@WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/21100" target="_blank">📅 17:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21099">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نیروی دریایی ایالات متحده قراردادی به ارزش 22.9 میلیارد دلار با شرکت "RTX" بست تا موشک‌های "تاماهاک" تولید کند
@WarRoom</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/21099" target="_blank">📅 16:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21098">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبرگزاری ولت آلمان: اگر ترامپ بیشتر از این برای حمله معطل کند، ایران رسما برنده جنگ می شود
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21098" target="_blank">📅 16:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21097">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ: محاصره دریایی آمریکا همچنان فشار اقتصادی جدیدی بر نظام ایران وارد می‌کند.
ما انباری بزرگی از سلاح‌های میان‌برد داریم که می‌توان در آینده، در صورت لزوم، از آن‌ها استفاده کرد.
مقداری از سلاح‌هایی که تا کنون از ذخایر موجود استفاده کرده‌ایم، ناچیز است.
انتخابات میان دوره‌ای آمریکا کوچکترین اثری در مورد دیدگاه و نظر من در مورد ایران ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21097" target="_blank">📅 16:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21096">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حوثی‌های یمن اعلام کردند که با موشک، «یک کشتی نظامی سعودی و چهار شناور همراه آن» را در دریای سرخ هدف قرار داده‌اند.
عربستان سعودی هنوز واکنشی نشان نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/21096" target="_blank">📅 16:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21095">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سخنگوی سپاه: ادعای امروز ترامپ درباره گفتگوی پشت‌پرده با سپاه، توهمات ناشی از شکست است
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21095" target="_blank">📅 16:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21094">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رویترز:
یک مقام ارشد ایرانی اعلام کرد ایران از موضع دفاعی به سیاستی «کاملاً تهاجمی» تغییر مسیر داده است. تهران چند هفته به واشنگتن فرصت داده تا تفاهم‌نامه موجود را به‌طور کامل اجرا کند. این مقام هشدار داد ایران محاصره دریایی نامحدود آمریکا را تحمل نخواهد کرد و در صورت شکست دیپلماسی، برای تشدید تنش‌ها در تنگه هرمز و سراسر منطقه آماده است. قرار است این ضرب‌الاجل از طریق میانجی‌ها به آمریکا و دولت‌های منطقه منتقل شود؛ موضوعی که در صورت نرسیدن به توافق، خطر تشدید درگیری نظامی را افزایش می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21094" target="_blank">📅 16:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21093">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یک مقام ارشد ایرانی : ایران تا ابد منتظر ماندن زیر محاصره دریایی آمریکا نخواهد ماند
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21093" target="_blank">📅 16:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21092">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: من عجله‌ای برای مذاکره با ایران ندارم و جدول زمانی مشخصی برای این کار تعیین نکرده‌ام.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21092" target="_blank">📅 15:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21090">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: ایران باید پرچم تسلیم را برافرازد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21090" target="_blank">📅 15:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21089">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ در مورد حماس : ما یک کانال ارتباطی متفاوت با حماس داریم و در نهایت آن‌ها سلاح‌های خود را زمین می‌گذارند
اسرائیلی‌ها نباید در غزه حمله کنند، زیرا حماس موافقت کرده است که سلاح‌های خود را زمین بگذارد!
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21089" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21088">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143fd65f66.mp4?token=KuTIrbYOYaAwMhovBoE-2tSXiUyY51VD9FL0x3qrqwPOc_rpztzSJbiRern6orh_xn6IVBOjrf_fCGou6VsYSXH_bgF6gQ82y9crTUvzc9IcVrprlMXtuVYtMyLLTM2rFvWsHrN1KASabG-1yp6ZCyc7EvnmcyxHZs_PUF7OUlfxUxroyEllnKqiWQ4vJ7D5BZdz4X5yv-9dsOFTEt4E-qG-X-DgWTyZq6WQOXlaakw7GgC1sUjMmNYunVPL6mQiig4nxxt_X6I9PsKmatAeszi-2ECPzwipKziGhdRJuz7xberixPyCKmV42dYTU0wdQJEysBU-OENsn2ar5mbLJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143fd65f66.mp4?token=KuTIrbYOYaAwMhovBoE-2tSXiUyY51VD9FL0x3qrqwPOc_rpztzSJbiRern6orh_xn6IVBOjrf_fCGou6VsYSXH_bgF6gQ82y9crTUvzc9IcVrprlMXtuVYtMyLLTM2rFvWsHrN1KASabG-1yp6ZCyc7EvnmcyxHZs_PUF7OUlfxUxroyEllnKqiWQ4vJ7D5BZdz4X5yv-9dsOFTEt4E-qG-X-DgWTyZq6WQOXlaakw7GgC1sUjMmNYunVPL6mQiig4nxxt_X6I9PsKmatAeszi-2ECPzwipKziGhdRJuz7xberixPyCKmV42dYTU0wdQJEysBU-OENsn2ar5mbLJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما با سپاه پاسداران انقلاب اسلامی یک کانال ارتباطی داریم.
ما مستقیماً با مقامات سپاه در ایران صحبت می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21088" target="_blank">📅 14:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21087">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ممکن است در انتخابات اسرائیل از شخص خاصی حمایت کنم
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21087" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21086">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ در فاکس‌نیوز هشدار داد که اگر عمان مانع منافع آمریکا شود، این کشور را بمباران خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21086" target="_blank">📅 14:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21085">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ به فاکس نیوز:
یک کانال ارتباطی محرمانه با مقام‌های سپاه پاسداران ایران داریم
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21085" target="_blank">📅 14:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21084">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادعای العربیه : گزارش‌ها حاکی از آن است که با تمدید دوره ۶۰ روزه بین ایران و آمریکا موافقت شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21084" target="_blank">📅 14:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21083">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نیروهای مسلح یمن با شلیک ده‌ها موشک بالستیک و پهپاد، مواضع نظامی و انبارهای تسلیحاتی نیروهای وابسته به عربستان را در المخا و مأرب هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21083" target="_blank">📅 14:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21082">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyORjRoTjt_lqDkvlSUC-nq7Td4ZOg3pfvS1ZXJZD-XpfGQwEf4OM98M2Lns06DdANgFRIfmsNOQJHmcrVSMRUesIaiyW8UNVoyLSj_Q1TjWDF0XI_HJ4xnOS_rgC2Edyd4FDVNpZqq52iUYXKBPwe6ytt5aHV9ke66k5kAM3ehBtd-ECR7oJz5RlrTR_1zdqPEvne2aiB2UjGZoI-7AWODcacKaVGvJNauRyVXFzwGDS89ceimZQuYH_5Gg2POnxXwP7iHCwzL47udk7bbOxc0s0icxQgCWi3Vv8Vlben0ktUS598AkbwHvoiWG9ROWc8v3jhIjGVhvxwFbYQI0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : هدف شماره یک، و همیشه همین خواهد بود، این است که ایران تحت هیچ شرایطی، به هیچ شکل و صورتی، نتواند سلاح هسته‌ای داشته باشد. از توجه شما به این موضوع سپاسگزارم!
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21082" target="_blank">📅 14:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21081">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حمله پهپادی ایران به دفتر بارزانی
مسعود بارزانی: در پی تحقیقات واحد ضدتروریسم کردستان، دفتر شخصی من و منزل رئیس سازمان امنیت و اطلاعات، امروز هدف حملات پهپادی ایران قرار گرفتند. من این حملات بی‌پروا و غیرقابل‌قبول را به شدیدترین شکل ممکن محکوم می‌کنم. این یک تشدید خطرناک و تهدیدی مستقیم علیه امنیت و ثبات اقلیم کردستان است. این حملات ما را از انجام وظایفمان و حفاظت از شهروندانمان بازنخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21081" target="_blank">📅 13:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21080">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سخنگوی وزارت خارجه ایران:
تفاهم‌نامه‌ای که با طرف آمریکایی امضا کردیم، هیچ مهلت ۶۰ روزه‌ای را تعیین نکرده است.  آمریکا چند هفته پس از امضای تفاهم‌نامه، مفاد آن را نقض کرد.
گفتگوها با عمان به دلیل پیچیدگی موضوع، دخالت بازیگران متعدد و کشورهایی که به دنبال تضعیف این روند هستند، مدت زیادی است که به تعویق افتاده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21080" target="_blank">📅 12:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21079">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وال‌ااستریت ژورنال به نقل از مقام‌های ایرانی و عرب گزارش داده است که تهران در وقفه دوماهه اخیر به‌جای کاهش تنش، برای
گسترش جنگ و درگیری طولانی‌تر
آماده شده است. طبق این گزارش، سپاه هماهنگی با نیروهای همسو در
یمن، عراق و لبنان
را افزایش داده، تولید موشک و پهپاد را بالا برده و همزمان فشار بر کشتیرانی در تنگه هرمز و دریای سرخ را تشدید کرده است. مقام‌های عرب نگران‌اند که در صورت آغاز دور جدید درگیری، این نیروها علیه
نیروهای آمریکایی، اسرائیل و زیرساخت‌های انرژی منطقه
وارد عمل شوند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21079" target="_blank">📅 11:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21078">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7LWAzPYF2tRA97yhQviBJgZEikiGiAPD24kEKfZDXBBnBrxjYQ24QOnB1GJWEme-MYxjeFE6R7iPMLuCBwgPMs6GCCZ7xXnpvvD1HPg7-k-5EtuerUzB1CrG9cr6j_BfxHEduyknVoVXFhZBSvj3T3pvNzUQ_Uk-B6rEcO_h4dQZSjd2Q4xQHP2k-NF8Z1SE6sDGMYqCO58VNFn7H0Ox8aR_uWl1mgQ85Z-6OZW1CXSbQMj06QVd5bWkXKJjNSRE9s2iQBodriSXMP0cPXtlnbOyWJsL4wVqN6C2dAHD0aVMVxhfW6BB5d_hw9aVPY2aQ8iQT4HfOOjW6J2Tptk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بررسی داده‌های پرواز فعالیت همزمان دو فروند هواپیمای E6B-Mercury فرماندهی و کنترل راهبردی آمریکا در آسمان خبر می‌دهند.این هواپیما ها بخشی از سامانه ارتباطی آمریکا برای حفظ ارتباط با زیردریایی‌های حامل موشک و نیروهای راهبردی است و لزوماً به معنی آغاز حمله هسته‌ای نیست. اما ولی حضور همزمان دو فروند می‌تواند نشان‌دهنده
فعالیت یا آمادگی بالاتر
از معمول و
در سطح فرماندهی راهبردی
باشد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21078" target="_blank">📅 11:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21077">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وای نت : حوزه‌های رأی‌گیری در سراسر اسرائیل برای انتخابات مقدماتی حزب لیکود باز شده‌اند. حدود ۱۴۰ هزار رأی‌دهنده از بین ۱۲۴ نامزد، که ۷۹ نفر از آنها در فهرست ملی و ۴۵ نفر در حوزه‌های انتخابیه هستند، انتخاب خواهند کرد. حدود ۸۰ حوزه رأی‌گیری حزبی در شهرهای بزرگ و همچنین در مناطق حاشیه‌ای، از جمله در هیخال شلومو در تل‌آویو، حیفا، ریشون لتصیون، ایلات، اوفاکیم و بنیامین هائوما در اورشلیم، جایی که بنیامین نتانیاهو، نخست وزیر، نیز رأی خواهد داد، برپا شده است. حوزه‌های رأی‌گیری ساعت ۱۰ شب بسته خواهند شد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21077" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21076">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وال‌استریت ژورنال: به نظر می‌رسد رهبران ایران به‌جای تکیه بر دیپلماسی با آمریکا، خود را برای یک درگیری گسترده‌تر و طولانی‌تر آماده می‌کنند. تهران در فاصله آرامش پس از توافق ژوئن، توان موشکی و پهپادی خود را بازسازی، سپاه را تقویت و نیروهای نیابتی منطقه‌ای را برای عملیات تهاجمی هماهنگ کرده است. فشار بر کشتیرانی در تنگه هرمز و دریای سرخ و تهدید زیرساخت‌های انرژی خلیج فارس نیز افزایش یافته است. هم‌زمان، تندروها کنترل بیشتری بر ساختار نظامی و امنیت داخلی پیدا کرده‌اند. هدف این راهبرد، بالا بردن هزینه حمله به ایران و بازدارندگی آمریکا، اسرائیل و کشورهای خلیج فارس از حملات آینده است؛ به‌طوری‌که تهران ظاهراً موقعیت کنونی را پایان جنگ نمی‌داند، بلکه آن را آماده‌سازی برای رویارویی بزرگ‌تر می‌بیند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21076" target="_blank">📅 10:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21075">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نیویورک تایمز به نقل از منابع آگاه:مهلت ۶۰ روزه توافق اسلام‌آباد بدون نتیجه پایان یافت و جنگ وارد مرحله فرسایشی اقتصادی شده است.
واشنگتن خواستار بازگشایی هرمز است و ایران آزادسازی دارایی‌هایش را شرط آن می‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21075" target="_blank">📅 10:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e2168088.mp4?token=XC_kvoynzWQxJ1O7Jhfmpee4PR_utiX7v9Qkz5F5N9GM3prccPDyG2HoyxqQdMoVccSGE9sSIYl1P6iX1w_pPG7IDRKwyvkbNYQJH1_8Y9_5Boa1-vLTBqSdUIQvL7s36GxK2tuQPMa_Py_wWmNwXjS2D6_CzFLKz_nmaUXmhEoZ58ei_JZU2361EzPOWmJfPDDrdEdBzA1_stEuxMJPhPiqSx85e9C_Q9ygC23QJUCWmUy6KDA4NnzQyKjvrMvmv4XYnqxUjO4OTQPSlrRi0QohuSb2eGcPW4B0bD3b75EKx9iT_E5EWiVjNM3bTjboBUEivMcgux2EF4QCRLn643h--5-tc9OYtYdQgohoO_2TqOtJXWT4FHzVDchXFupW-HyupuPv2Fo5IrR47fI5CFPg6HZP80SySmGtHyVpprjFazqYN-Jy431BvzxDkz28xWjSCKIZbaUpW3Q3ZxJXonT7vhdh9BKALbG-uJ6jiyzEP9_5344OH7i7qt3jA0qBXRgbb-4H9BWl5StIcX3S3pQ9Sc0vlPN1Q3iypLyjWv3Hp0yO57-mjpuDwb7TvQxnw_Y_TNreJ6OMeCsyLeM3jzqI-C8anP0wGI0ifweCqbvzVOdo27a0XFhTWgiisuuctfJDMhHYXoyIpvdqEqMAlT4Lymx1LPjtf3kS6Y6Syzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e2168088.mp4?token=XC_kvoynzWQxJ1O7Jhfmpee4PR_utiX7v9Qkz5F5N9GM3prccPDyG2HoyxqQdMoVccSGE9sSIYl1P6iX1w_pPG7IDRKwyvkbNYQJH1_8Y9_5Boa1-vLTBqSdUIQvL7s36GxK2tuQPMa_Py_wWmNwXjS2D6_CzFLKz_nmaUXmhEoZ58ei_JZU2361EzPOWmJfPDDrdEdBzA1_stEuxMJPhPiqSx85e9C_Q9ygC23QJUCWmUy6KDA4NnzQyKjvrMvmv4XYnqxUjO4OTQPSlrRi0QohuSb2eGcPW4B0bD3b75EKx9iT_E5EWiVjNM3bTjboBUEivMcgux2EF4QCRLn643h--5-tc9OYtYdQgohoO_2TqOtJXWT4FHzVDchXFupW-HyupuPv2Fo5IrR47fI5CFPg6HZP80SySmGtHyVpprjFazqYN-Jy431BvzxDkz28xWjSCKIZbaUpW3Q3ZxJXonT7vhdh9BKALbG-uJ6jiyzEP9_5344OH7i7qt3jA0qBXRgbb-4H9BWl5StIcX3S3pQ9Sc0vlPN1Q3iypLyjWv3Hp0yO57-mjpuDwb7TvQxnw_Y_TNreJ6OMeCsyLeM3jzqI-C8anP0wGI0ifweCqbvzVOdo27a0XFhTWgiisuuctfJDMhHYXoyIpvdqEqMAlT4Lymx1LPjtf3kS6Y6Syzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران شد: اتفاقات خوبی خیلی زود رخ خواهد داد. در واقع، آنها همین حالا هم رخ داده‌اند، چون یک کاری هست که ما نمی‌توانیم اجازه دهیم انجام شود: ما نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21074" target="_blank">📅 02:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da8Lzrim96g253w0RF3cqYdDlLaDKSZ0su3NRa9_-qLYFtLE1yRiIurPrgOdQBt4wkc_6Nx6ZGKir9wNTp7tKyZfwGflRPr1G9avyPKH1RXmuRpICTqPk27zwcLBFIPez1MxbGdSEKoY2u1TaHENpiIYZi5c1VBLPdoXsSq9jW1vVf8H5IMcPI6-_Wv-CGd5nGAR8ZWnkTomm4m8OizhGKKPf1RcRKkFQGP7-avNDfmMXje_z4nOUTAY1SmNE3S_JttjFwp7WJrcTlOWk8ZdfYvezskZ23VQgMY858rsh9g5K7DBR7DnlDH_JJ2-Szxe0a_ggmvvH5095eMykbG8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :با توجه به رابطه بسیار خوبی که با کیم جونگ اون، رهبر کره شمالی، دارم، از اینکه ایالات متحده مدت‌ها پیش با برگزاری رزمایش‌های نظامی مشترک با کره جنوبی موافقت کرده، خوشحال نیستم. این رزمایش‌ها نه‌تنها پرهزینه هستند و بخش زیادی از هزینه‌هایشان، مثل همیشه، بر عهده آمریکا است، بلکه پیامی کاملاً نامناسب و خصمانه به کشوری ارسال می‌کنند که تا زمانی که دونالد جی. ترامپ رئیس‌جمهور بوده، رفتاری تهدیدآمیز نداشته و محترمانه رفتار کرده است. بنابراین، و با توجه به اینکه دیگر برای لغو آنها خیلی دیر شده است، به پیت هگست، وزیر جنگ، دستور داده‌ام رزمایش‌های نظامی مشترک را به میزان قابل‌توجهی کاهش دهد! البته این موضوع تا حدی بی‌ارتباط است (؟)، اما اخیراً از رئیس‌جمهور کره جنوبی پرسیدم که آیا مایل هستند به ما در خلع سلاح هسته‌ای جمهوری اسلامی ایران بپیوندند و آنها گفتند: «نه، ممنون!» از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21073" target="_blank">📅 02:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ از نیوجرسی پرواز کرده و در راه واشنگتن است. او به طور خلاصه به خبرنگاران گفت: «آخر هفته فوق‌العاده‌ای بود. جلسات زیادی داشتیم.» وقتی خبرنگاران از او پرسیدند که آیا این جلسات درباره ایران بوده است، پاسخی نداد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21072" target="_blank">📅 01:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ در تروث‌ :بسیار خوشحالم که عربستان سعودی، ترکیه و پاکستان سرانجام و اخیراً توافق دفاعی مشترک مکه را امضا کرده‌اند. این نشان می‌دهد که خاورمیانه در حال متحد شدن است و کشورها سرانجام خواهند توانست به شکلی مؤثرتر و معنادارتر از خود دفاع کنند.به رهبران بزرگ این سه کشور تبریک می‌گویم. این یک گام نخست بزرگ، جسورانه و مهم است , واو!
@WarRoom
واکنش بی بی : فقط کسی توضیح بده دقیقاً قرار است از چه کسی در برابر چه کسی دفاع کنند!
😂</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21071" target="_blank">📅 00:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ در تروث به‌شدت از برنامه شنون بیم در فاکس‌نیوز انتقاد کرده و آن را هم‌سطح «بدترین بخش‌های سی‌ان‌ان» دانسته است. او می‌گوید این برنامه دائماً مهمان‌ها و نظرسنجی‌های منفی علیه دولتش انتخاب می‌کند و دستاوردهای دولتش را نادیده می‌گیرد. ترامپ همچنین از خوان ویلیامز و جسیکا تارلوف انتقاد کرده و پیش‌بینی کرده رتبه بینندگان برنامه شنون سقوط خواهد کرد. او در پایان تأکید کرده که خودش در دفتر بیضی مشغول ادامه کار برای «پیروزی‌ها و موفقیت‌های بیشتر» است
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21070" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21069" target="_blank">📅 00:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21068">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21068" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21067">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21067" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21066">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سیریک موشک بلند شد
🤠
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21066" target="_blank">📅 00:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21065">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سیریک موشک بلند شد
🤠
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21065" target="_blank">📅 23:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21064">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">داریوش اقبالی با انتشار ترانه جدیدی به نام «توهم توطئه» و کنایه به شاهزاده رضا پهلوی به کمپین آنفالو توسط مردم پیوست. در صدر این جدول نوید محمدزاده با نزدیک به یک میلیون آنفالو قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/21064" target="_blank">📅 23:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21063">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رویترز : جرد کوشنر، فرستاده ویژه ترامپ، فردا دوشنبه ۱۷ اوت با بنیامین نتانیاهو دیدار خواهد کرد. این دیدار در چارچوب تلاش واشنگتن برای پیشبرد طرح صلح غزه انجام می‌شود؛ طرحی که شامل خلع سلاح حماس، توقف عملیات نظامی و خروج تدریجی نیروهای اسرائیلی از غزه است.…</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21063" target="_blank">📅 23:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21062">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کانال 12 اسرائیل: اعضای حزب الله و سپاه در زیر زمین در ارتفاعات علی الطاهر گیر افتاده اند و تعداد آنهابیش از ده هانفر تخمین زده می شود.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21062" target="_blank">📅 22:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام به وال استریت ژورنال: گروه ضربت ناو هواپیمابر لینکلن تیمی قوی از آمریکایی‌های با دستاوردهای بالا است که با غرور فراوان و موجه به هر آنچه که به دست آورده‌اند، ایستاده‌اند.
تاریخ این استقرار را به عنوان یکی از فشرده‌ترین و مهم‌ترین استقرارهای دوران مدرن ثبت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21061" target="_blank">📅 22:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21060">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8429c9c845.mp4?token=iypi_2Pfu9iAQZoTliZTxIYcyfL-7eioNHwUFHBPHFdwhsgsrJMmbDVwIA-Yx21G1fpx0ehqSjJFf3J08TgwxYPylFoqgBjoOuqUckICOm0tIKZlchf0bscQ-25g3Lqa3o5OyeYIYCa6idlJWHX53ZmPzY17iXJKvTq20NZz7T45cWAWNXvqvT88C2pq6DQSfgArdUXknTsnUMOfelzt9x8Nnh6Yr7TipGNUbXSg5p_vCJiGS98J7jNS8zQEDvuHvrfjZPTwe0lszJ_p1WnSzrfOKuomRnXH4hFYl_wPwEWBzwr438XlgSGiUbTn0sl54WE_niU6MhLibcOYW8qNEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8429c9c845.mp4?token=iypi_2Pfu9iAQZoTliZTxIYcyfL-7eioNHwUFHBPHFdwhsgsrJMmbDVwIA-Yx21G1fpx0ehqSjJFf3J08TgwxYPylFoqgBjoOuqUckICOm0tIKZlchf0bscQ-25g3Lqa3o5OyeYIYCa6idlJWHX53ZmPzY17iXJKvTq20NZz7T45cWAWNXvqvT88C2pq6DQSfgArdUXknTsnUMOfelzt9x8Nnh6Yr7TipGNUbXSg5p_vCJiGS98J7jNS8zQEDvuHvrfjZPTwe0lszJ_p1WnSzrfOKuomRnXH4hFYl_wPwEWBzwr438XlgSGiUbTn0sl54WE_niU6MhLibcOYW8qNEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ‌ درباره سخنگوی ‌کاخ سفید:
من متوجه شدم که کارولین لیویت فرزندانش را بیشتر از ترامپ دوست دارد، من از این بابت بسیار نگران هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21060" target="_blank">📅 21:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اورشلیم پست :
حماس بخش مهمی از فعالیت‌های خود را از قطر به ترکیه منتقل کرده است.
بر اساس گزارش‌های تازه، بخش عمده فعالیت‌های محرمانه حماس، از جمله واحدهای برنامه‌ریزی و سایبری، به ترکیه منتقل شده و بسیاری از رهبران این گروه نیز بیشتر در ترکیه حضور دارند. با این حال،
دفتر سیاسی و فعالیت‌های علنی حماس همچنان در قطر ادامه دارد
و هنوز انتقال کامل دفتر سیاسی به ترکیه تأیید نشده است. این جابه‌جایی در حالی انجام شده که حماس همزمان برای مذاکرات مربوط به آینده غزه، از کانال‌های قطر، ترکیه و مصر استفاده می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21058" target="_blank">📅 21:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش پرتاب موشک از قشم
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21057" target="_blank">📅 20:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21056">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رویترز : جرد کوشنر، فرستاده ویژه ترامپ، فردا دوشنبه ۱۷ اوت با بنیامین نتانیاهو دیدار خواهد کرد. این دیدار در چارچوب تلاش واشنگتن برای پیشبرد طرح صلح غزه انجام می‌شود؛ طرحی که شامل
خلع سلاح حماس، توقف عملیات نظامی و خروج تدریجی نیروهای اسرائیلی از غزه
است. نتانیاهو پیش‌تر با بخش‌هایی از این طرح مخالفت کرده بود و کوشنر برای نزدیک‌کردن مواضع دو طرف به اسرائیل سفر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21056" target="_blank">📅 20:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21055">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c8cf686.mp4?token=Njxy1XIQcHqt0i3H0FfSC7ZkR3yeGzafGq2fKi8qLOV_DNEseA-jPcmWLlCM1knltI-X_iap4aHdJGgnX0LBpUFQfTVJ4i_l8F2UsLx2aNODnW7_nOBf5iPPbI--MQVkuJWBhzc44jQYaXKUakJiOQEcTRe793zF7D1wotvyY5vqRD6u1J7NMF8cYk2CjsS4TrftTtzCdR-UTWyl3-DFPA0y4fF81DVJLgmOAYmRLFly7DMA2ttfPzJLyXZdCtdiF3C0KwGpwGBALnBT_oBCNlQfYGMes1yw2oFUn00Zv6rlozxwF22ydD8lwNXIBzwsuxF5elSCYsRl8Bz9whogRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c8cf686.mp4?token=Njxy1XIQcHqt0i3H0FfSC7ZkR3yeGzafGq2fKi8qLOV_DNEseA-jPcmWLlCM1knltI-X_iap4aHdJGgnX0LBpUFQfTVJ4i_l8F2UsLx2aNODnW7_nOBf5iPPbI--MQVkuJWBhzc44jQYaXKUakJiOQEcTRe793zF7D1wotvyY5vqRD6u1J7NMF8cYk2CjsS4TrftTtzCdR-UTWyl3-DFPA0y4fF81DVJLgmOAYmRLFly7DMA2ttfPzJLyXZdCtdiF3C0KwGpwGBALnBT_oBCNlQfYGMes1yw2oFUn00Zv6rlozxwF22ydD8lwNXIBzwsuxF5elSCYsRl8Bz9whogRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرش دعوا شد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21055" target="_blank">📅 20:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21054">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏کارزار انتخاباتی جدید نتانیاهو؛ «آنها می‌خواهند نتانیاهو شکست بخورد، اجازه ندهید پیروز شوند» مجتبی خامنه ای، زهران ممدانی ، اردوغان ، نعیم قاسم @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21054" target="_blank">📅 19:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21053">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDR0AnUa-YBOIxSZfeEbg-V250ZofCkLNCfzbihS6ld4cFvGnh0lO7zG7ND0w5-x4P1B1iGEU5cbmse5LtWIn8he0n0C-jji8VKRhPX83H6gdEhDhxgtpqqijYeeOJdsIz6nap-uJ9PV8GRZ4CKLBRBLIm2IBidsGeKoNXxb339NZ7ouK04W-tgT0ELG1oY3xRwz6120yt2Q-rLtGk2BJ1GQ2_2aEcFSVqMlSGRYlPolBdGeEGIIq1XGlwFhLyOWWn7CNAuDoicBy_rJNfTVy4ABbo2uYdUvk0TWy6v78ztQV836BQnSgGdXuOsALqiKicY6n1tYihqb7ARoROHymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏کارزار انتخاباتی جدید نتانیاهو؛ «آنها می‌خواهند نتانیاهو شکست بخورد، اجازه ندهید پیروز شوند»
مجتبی خامنه ای، زهران ممدانی ، اردوغان ، نعیم قاسم
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21053" target="_blank">📅 19:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فاکس‌نیوز: مهلت ۶۰ روزه تفاهم‌نامه آمریکا و ایران فردا به پایان می‌رسد.
بر اساس گزارش فاکس‌نیوز، تفاهم‌نامه ۱۷ ژوئن میان واشنگتن و تهران یک بازه ۶۰ روزه برای مذاکره درباره برنامه هسته‌ای و موشکی ایران، تحریم‌ها و آزادی کشتیرانی در تنگه هرمز تعیین کرده بود که مهلت آن
۱۷ اوت
است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21052" target="_blank">📅 17:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21051">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">افسر قطری در گفت‌وگو با الجزیره درباره خلبانان ایرانی اظهارنظر کرده است.
در این گفت‌وگو، سرهنگ دوم
ناصر محمد الکبیسی
از وزارت دفاع قطر درباره سرنگونی دو فروند سوخو-۲۴ ایرانی گفت که هواپیماها بمب حمل می‌کردند و در توضیح منبع اطلاعات، به «تأیید خلبان» اشاره کرد؛ در حالی که قطر پیش‌تر گفته بود خلبانان به تماس‌های رادیویی پاسخ نداده‌اند. این اظهارات دوپهلو اکنون در کنار ادعای ایران درباره زنده‌بودن و اسارت سه خلبان ایرانی، مورد توجه قرار گرفته است، زیرا قطر می‌گوید هیچ خلبان ایرانی زنده‌ای را در اختیار ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21051" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آکسیوس: پیام‌ها میان تهران و واشنگتن همچنان ردوبدل می‌شود، اما مذاکرات در بن‌بست است.
آکسیوس گزارش داده آمریکا و ایران از طریق
پاکستان و قطر
همچنان پیام‌هایی را ردوبدل می‌کنند، اما تاکنون پیشرفت قابل‌توجهی حاصل نشده است. در پشت پرده نیز دولت ترامپ برای ارتباط مستقیم‌تر با
سپاه
یک کانال محرمانه از طریق
بارزانی
ایجاد کرده بود و چند پیشنهاد و پاسخ میان دو طرف ردوبدل شد؛ حتی یک تفاهم اولیه شکل گرفت، اما خیلی زود فروپاشید. اکنون میانجی‌ها همچنان فعال‌اند و بارزانی نیز اخیراً به کاخ سفید پیشنهاد داده برای ازسرگیری مذاکرات آمریکا و ایران کمک کند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21050" target="_blank">📅 17:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21049">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رویترز: ترامپ به دنبال تشدید فشار اقتصادی بر ایران است؛ محاصره زمینی هم به‌عنوان یک گزینه مطرح شده است.
رویترز گزارش داده آمریکا علاوه بر محاصره دریایی و تحریم‌های گسترده، گزینه
محاصره زمینی ایران
را نیز بررسی کرده؛ اقدامی که به همکاری عراق، ترکیه، پاکستان، افغانستان، ترکمنستان، جمهوری آذربایجان و ارمنستان نیاز دارد و به‌دلیل دشواری‌های جغرافیایی و سیاسی، اجرای آن بسیار سخت ارزیابی می‌شود. واشنگتن همچنین در حال بررسی تحریم پالایشگاه‌ها و بانک‌های چینیِ مرتبط با نفت ایران و اعمال فشار بر کشورهایی است که به تجارت یا تأمین تسلیحات ایران کمک می‌کنند. رویترز می‌گوید از آغاز دور دوم ریاست‌جمهوری ترامپ،
بیش از ۱۰۰۰ فرد، کشتی و هواپیما
تحریم شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21049" target="_blank">📅 17:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21048">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd67bb941.mp4?token=AGkoXMd_dJQELdkJZFFt_kgq7pfBOGwP6eQvXN8GdbyhrwSsAz-_jilUAky7VADpotJqAtFhRpbS6UXFuQgjSqdM7Ki0zuqTqDLVeUknTPjEkN2HMoGoDLubMI5ZvFUheHdqD_1XPWNIv-U7ZlFWZxZFcThYSzB8sdI7dUoYfNexmm2lMXUuJT5RmBk3DujBfhkeAAqJGl1HFG6wUveCZbfR4sak8NDDN-5Rv3c2tDIVaBlduP0n9SqSw5Q9hj-a1_FeZb2cug9lNxNinKH7Wed-BT4OoEEaxdfSHJZc33dLOlM17aB66bg1a5I-hCA2X4q2CSxerv0VpS1OwO40ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd67bb941.mp4?token=AGkoXMd_dJQELdkJZFFt_kgq7pfBOGwP6eQvXN8GdbyhrwSsAz-_jilUAky7VADpotJqAtFhRpbS6UXFuQgjSqdM7Ki0zuqTqDLVeUknTPjEkN2HMoGoDLubMI5ZvFUheHdqD_1XPWNIv-U7ZlFWZxZFcThYSzB8sdI7dUoYfNexmm2lMXUuJT5RmBk3DujBfhkeAAqJGl1HFG6wUveCZbfR4sak8NDDN-5Rv3c2tDIVaBlduP0n9SqSw5Q9hj-a1_FeZb2cug9lNxNinKH7Wed-BT4OoEEaxdfSHJZc33dLOlM17aB66bg1a5I-hCA2X4q2CSxerv0VpS1OwO40ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه اصلی ویدی منتشر شد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21048" target="_blank">📅 16:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21047">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/057d64cb85.mp4?token=CMe8Lq3CTaS78TdeRgkG9zBOdkjNDJSZMIew_0uuJK4w_G6AiPeU608u-RbqWoS4YKaSVo-RQIm2mj8a5UNlNRUCEljzkdKPxGicT2jnm25uPj-0WnJwv6kGygrAcERWqP-QtIxX6yDbAfpKZAy0KI4bDBcsUehlUDxQMBFBHaaLvoszrzl1MlzDZnYzWHcOY4QMbkJxTU_pVr2t47ZR1x38N05Ug2qbxdUSbfEm8n8xBWfe1lnbVDxEGZrGMvU3w3G4u2hXlPd3tdr2iKPFU5qHaIk8-pwT9ySXrWrDUOJ8owE9S5ubRJA4XjttvXXNKE595WWKszqvws2grG_avw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/057d64cb85.mp4?token=CMe8Lq3CTaS78TdeRgkG9zBOdkjNDJSZMIew_0uuJK4w_G6AiPeU608u-RbqWoS4YKaSVo-RQIm2mj8a5UNlNRUCEljzkdKPxGicT2jnm25uPj-0WnJwv6kGygrAcERWqP-QtIxX6yDbAfpKZAy0KI4bDBcsUehlUDxQMBFBHaaLvoszrzl1MlzDZnYzWHcOY4QMbkJxTU_pVr2t47ZR1x38N05Ug2qbxdUSbfEm8n8xBWfe1lnbVDxEGZrGMvU3w3G4u2hXlPd3tdr2iKPFU5qHaIk8-pwT9ySXrWrDUOJ8owE9S5ubRJA4XjttvXXNKE595WWKszqvws2grG_avw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان رژیم ویدئویی با عنوان «دیدار رئیس جمهور مسعود پزشکیان و مجتبی خامنه‌ای»، رهبر ایران منتشر کردند.
@WarRoom
یاشار : شک نکنید فیکه اگه اصل‌ بود فارس اینا میدادن بیرون نه اینکه یه پیج مداحی تا الان منبع اصلی باشه !</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21047" target="_blank">📅 16:45 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
