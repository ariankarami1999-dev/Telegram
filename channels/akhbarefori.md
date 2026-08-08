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
<img src="https://cdn4.telesco.pe/file/J8IxcF3Zwm8Ojarnvm1ae3xWLf7VlzbJI4GjVPXIa7HQTnX_Neqzi-e81tS4mjBc0z7tcdd5KWI8qHe_IBjqQWn9CSmKHjvXIWcDBqW0tyjI4hdrmk2KWTc5jhmZL9yOoqaszYK6lk30l8LhAAfPdaOXEbb7EhslnxsENDBxKf2STBT80Ic_WMggLwe6Tw6JR0-fHvlHNSuqefa22gDa2tcDJby0SYBfSx5f5SLHRcRVHsjq3NOWn2bfoULKGBsaWdlKPPyLBBoHl5lb-bZ1RBNHe0givbeMe4LLABBrr7ybd7n7W7dDy4SJ94nmc73du9d5YfNzRO7EJxmnta6iYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 23:20:29</div>
<hr>

<div class="tg-post" id="msg-679540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
عراقچی: تعیین مسیر جدید دریایی میان ایران و عمان به معنای باز شدن تنگه هرمز نیست
وزیر امور خارجه:
🔹
وضعیت فعلی نتیجه نقض یادداشت تفاهم از سوی آمریکاست و این کشور باید موارد نقض را به‌طور کامل جبران کند.
🔹
دخالت آمریکا در خدشه‌دار کردن حاکمیت ایران بر تنگه هرمز، خلاف مفاد یادداشت تفاهم بود.
🔹
ما تحمل نمی‌کنیم نقض یادداشت تفاهم بدون پاسخ بماند یا حاکمیت ایران بر تنگه هرمز به چالش کشیده شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/679540" target="_blank">📅 23:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35bd9022f8.mp4?token=uO5_vsfRcq3rgD-v1vSqn9mOxvLUbe0GSl2Qt66gXcOCHm3IQNEKVnl8Hw1nlHaHpA07kGfYSqlb3J0zwjZ6pSiFUP2YxahRYEOivVRgb4zFXzK4tS628_B_GNzmySfPTony06b5C1EHZtVEZ4DfLynriiyYHjEeeDBGFxTew80hOTx23xHIH_jAr7LFD2NKnW82ojibFIJAcUfMxX5wNwjwNgdQbzPkObFo9HMdgHBYSS_ngrmnGJIvqNx9w5cVLio4yeqXrnF6aR15ymf_mKt-_sqrHY9n5L5mg5ean3IUq1hRgOajZJ0TNRXlxHkDEEU3rM3Jr_TuIQKhiX_U6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35bd9022f8.mp4?token=uO5_vsfRcq3rgD-v1vSqn9mOxvLUbe0GSl2Qt66gXcOCHm3IQNEKVnl8Hw1nlHaHpA07kGfYSqlb3J0zwjZ6pSiFUP2YxahRYEOivVRgb4zFXzK4tS628_B_GNzmySfPTony06b5C1EHZtVEZ4DfLynriiyYHjEeeDBGFxTew80hOTx23xHIH_jAr7LFD2NKnW82ojibFIJAcUfMxX5wNwjwNgdQbzPkObFo9HMdgHBYSS_ngrmnGJIvqNx9w5cVLio4yeqXrnF6aR15ymf_mKt-_sqrHY9n5L5mg5ean3IUq1hRgOajZJ0TNRXlxHkDEEU3rM3Jr_TuIQKhiX_U6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: برخی توقع دارند در آمریکا و اروپا گرانی باشد اما در کشور ما که در جنگ هستیم گرانی نباشد؛ این در ذهن من نمی‌گنجد
🔹
وقتی در جنگ باشیم کمبود پیدا می‌کنیم و باید برای مقابله با سختی‌های آن آماده باشیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/679539" target="_blank">📅 23:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
واشنگتن‌پست: هزینه هر آمریکایی برای جنگ با ایران ۱۰۰۰ دلار شد
واشنگتن‌پست:
🔹
ارتش آمریکا میلیاردها دلار هزینه می‌کند و هر خانواده معمولی آمریکایی به خاطر این درگیری ۱۰۰۰ دلار پرداخت خواهد کرد.
🔹
هزینه‌هایی که بر دوش مالیات‌دهندگان و مصرف‌کنندگان گذاشته می‌شود، همچنان در حال افزایش است و فراتر از آن چیزی‌ست که تاکنون به طور کامل محاسبه شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/679538" target="_blank">📅 23:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
از قتل حمیدرضا رجب‌زاده، مداح معروف، چه می‌دانیم؟
👇
khabarfoori.com/fa/tiny/news-3236375
🔹
قوه قضائیه به دنبال بازداشت خرازی است؟
👇
khabarfoori.com/fa/tiny/news-3236278
🔹
سایه‌های نامرئی در آسمان تنگه هرمز | ترامپ سری تازه اسرار یوفوها را منتشر کرد
👇
khabarfoori.com/fa/tiny/news-3236311
🔹
سهمیه بنزین خودروهای تولید ۱۳۸۵ به قبل حذف خواهد شد؟
👇
khabarfoori.com/fa/tiny/news-3236401
🔹
ویدئویی جدید از آیت الله سید مجتبی خامنه‌ای، رهبر انقلاب
👇
khabarfoori.com/fa/tiny/news-3236321
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/679537" target="_blank">📅 23:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679536">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای سنتکام: اجازه دادیم حدود ۳۰ کشتی از منطقه تحت تحریم عبور کنند تا کمک‌های بشردوستانه به ايران منتقل شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/akhbarefori/679536" target="_blank">📅 23:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679535">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aacc3c703e.mp4?token=Dfz9ov5TN9oqSPwdC_GghNfPOGCmxtuzGhsAIsYBd5HwidBmPc9vQQQESzoEe7wnCBtEKZO2rki54B3hTOiqfb0PJsqWyrSmBEiqSnA8H8McPgE33zb0IzI_2b5oMqtKMPEF9mXWFKxdyl1V4-Btm6VMEt76MZfT1APOkid7mjBagoo0oYhAvPb_6Kaze_-c04jgfdOX4GfCA6-fDr591G2IaxZB2h02_7YOLf46Svm96FqRjw8oTmSI8xcA4zc5Qb0tOcHLoEcJzFNDO1wzlNIvoXhnsS4uuLlv8PoOFsR-R30QDejbmJUsC5Aldh9DFNHxli3Gksmx9dbCLqxZWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aacc3c703e.mp4?token=Dfz9ov5TN9oqSPwdC_GghNfPOGCmxtuzGhsAIsYBd5HwidBmPc9vQQQESzoEe7wnCBtEKZO2rki54B3hTOiqfb0PJsqWyrSmBEiqSnA8H8McPgE33zb0IzI_2b5oMqtKMPEF9mXWFKxdyl1V4-Btm6VMEt76MZfT1APOkid7mjBagoo0oYhAvPb_6Kaze_-c04jgfdOX4GfCA6-fDr591G2IaxZB2h02_7YOLf46Svm96FqRjw8oTmSI8xcA4zc5Qb0tOcHLoEcJzFNDO1wzlNIvoXhnsS4uuLlv8PoOFsR-R30QDejbmJUsC5Aldh9DFNHxli3Gksmx9dbCLqxZWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ما می‌جنگیم و سختی آن را هم می‌پذیریم؛ رهبر انقلاب هر تصمیمی بگیرند ما تا آخر پای آن هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/679535" target="_blank">📅 23:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679534">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/790c7567bb.mp4?token=iGgxtGwRMhw0OttJxOePVc-TnaNAvkFdyG4UFLIBK60A-qlVKCcRHKiupmPi4v6sSBne_-D9OwNRFAgTY8Kr6pWKTo4L2BtKme32UHgP4C0AQHBInx7BF7lOuw8-OZ0Riwqn_8xVTdSdP1pTBO4wtbMVvDZmrn_49HrgccYbELewsLPeYvTFZ0Bj_s0CI7Ch0b3z3tHvTBGMExn2bjxO6lAin3qzPk3CT4fR5JY9XjP3wG7mDL6_IuPvL4U7qXdqKgVhLF75IpbyfiVI_UBnIhMiOg68Jjimvq_30XCAwTPyKRiEyivFj1ZEgLZCUqxbAhZvsIP0Uo4aUTw9MRFQzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/790c7567bb.mp4?token=iGgxtGwRMhw0OttJxOePVc-TnaNAvkFdyG4UFLIBK60A-qlVKCcRHKiupmPi4v6sSBne_-D9OwNRFAgTY8Kr6pWKTo4L2BtKme32UHgP4C0AQHBInx7BF7lOuw8-OZ0Riwqn_8xVTdSdP1pTBO4wtbMVvDZmrn_49HrgccYbELewsLPeYvTFZ0Bj_s0CI7Ch0b3z3tHvTBGMExn2bjxO6lAin3qzPk3CT4fR5JY9XjP3wG7mDL6_IuPvL4U7qXdqKgVhLF75IpbyfiVI_UBnIhMiOg68Jjimvq_30XCAwTPyKRiEyivFj1ZEgLZCUqxbAhZvsIP0Uo4aUTw9MRFQzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران را با عدد و آمار نمی‌شود سنجید؛ آنچه می‌ماند، ایستادگی مردمی است که وطن را انتخاب کرده‌اند #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/akhbarefori/679534" target="_blank">📅 23:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679533">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
اشپیگل: تنگه هرمز منطقه ممنوعه شده است
🔹
پیش از جنگ علیه ایران، تا ۱۴۰ نفت‌کش از تنگه هرمز عبور می‌کردند.
🔹
اکنون این آبراه برای کشتیرانی تجاری بین‌المللی به منطقه ممنوعه تبدیل شده است.
🔹
ایران بازگشایی این آبراه را منوط به تحقق شرایط خود می‌داند. سپاه پاسداران انقلاب اسلامی ایران اعلام کرد که آزادسازی تنگه به موافقت آمریکا با خواسته‌های ایران بستگی دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/679533" target="_blank">📅 23:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679532">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سن تجرد مطلق نسبت به دو دهه قبل، هفت برابر شد
رضا سعیدی، رئیس مرکز جوانی جمعیت، سلامت خانواده و مدارس وزارت بهداشت و فوق‌تخصص نوزادان، در
#گفتگو
با خبرفوری:
🔹
میانگین سن ازدواج در خانم‌ها حدود ۲۹ سال و در آقایان حدود ۳۲ سال است و همچنین میانگین سن افراد در تولد اولین فرزند به حدود ۳۵ تا ۴۰ سالگی رسیده است.
🔹
در حال حاضر ۱۲ میلیون دختر و پسر بالای ۲۰ سال مجرد هستند. همچنین بیش از یک میلیون و ۲۰۰ هزار نفر از افراد بالای ۴۵ تا ۵۰ سال، در سن تجرد مطلق قرار دارند که نسبت به دو دهه قبل هفت برابر افزایش داشته است.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/679532" target="_blank">📅 23:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679531">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi6EfJUYpShbXyGyiUKTn0X8WUJ2MqJ_UFc6D02kR0LbFPPVnRQBE3CMAO9ZSYdvDUblX7QLq52Ix35utEXIqncX3iMtP9_JdcCUje595FPS5Zbvb0pPymz2t3D_dEujBzSuIjiIjtHOJwA5SH82nixOqqGhwSKYIMhEmXLA4CHYQP3ogTFk_VKrpBBHG7eZkrUclxXsRDvepJLNdo4oJ0xCtzq9F1U3jndK-pbAtLyQQuKTMVhKf7tamcg6CcCjzsFP5utBJdo1pJ-6k3AUZm_YItgLxA9JVe9joGanv1__7mHU1vZM7NobrDCzzfWpaaiD1lSuZov5yBlA2v6UCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیگپ و سازمان نوسازی مدارس برای ساخت مدرسه‌ای هوشمندتر دست به دست هم دادند
🔹
این تفاهم‌نامه با هدف توسعه زیرساخت‌های ارتباطی و آموزشی، تسهیل مشارکت مردمی در ساخت مدارس و تقویت ارتباط میان مدرسه و خانواده امضا شد و مدیرعامل آیگپ تأکید دارد که این همکاری گامی مؤثر برای ارائه خدمات سریع، امن و آسان به کاربران و ذی‌نفعان است.
🔹
مشروح این خبر را در سایت خبرفوری بخوانید:
https://www.khabarfoori.com/fa/tiny/news-3236413
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/679531" target="_blank">📅 23:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679530">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa6bda659.mp4?token=vNGaCYbCtMcLiY2X5iZ99yWDQe852BYCovp0NNrEbGNyVnl7fZWF9-UVFUmFCPXE3Ga6LdBRV81m6ThozPsaRwXTvrdosh0MonohO_sznszezL1VEGpN0DRvopNHYhzUjpCW8m2fFYyC02jmV9TiprJt_9s5U5uGBjnqvKfcroKOjwcHxoxPrm1HWcpcrWNk_uDttZDd76tVRCePVFK5GSvsTqvAg91IJjYSVVPpAb5Rg_-S6Pmf5IxRPa4UpiBNiSW10RNe-u2ZhAtSQ27WPEpMixWnd6mUrsD0svPD1-b9u5ywPa0gZX6dWcH_C93sBx4RZxacG3-Ai2UgmN36NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa6bda659.mp4?token=vNGaCYbCtMcLiY2X5iZ99yWDQe852BYCovp0NNrEbGNyVnl7fZWF9-UVFUmFCPXE3Ga6LdBRV81m6ThozPsaRwXTvrdosh0MonohO_sznszezL1VEGpN0DRvopNHYhzUjpCW8m2fFYyC02jmV9TiprJt_9s5U5uGBjnqvKfcroKOjwcHxoxPrm1HWcpcrWNk_uDttZDd76tVRCePVFK5GSvsTqvAg91IJjYSVVPpAb5Rg_-S6Pmf5IxRPa4UpiBNiSW10RNe-u2ZhAtSQ27WPEpMixWnd6mUrsD0svPD1-b9u5ywPa0gZX6dWcH_C93sBx4RZxacG3-Ai2UgmN36NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: من از جنگیدن نمی‌ترسم
🔹
شهادت شیرین‌ترین آرزوی ماست و تا پای جان ایستاده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/679530" target="_blank">📅 23:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679529">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWqz1ufHzI7hfPrTeXYsuqGWmu7gOT2V-mNK1LPedDRvVjfDZx1GHcT5iWOEZThaZ_7IS0m-acoEVO_MuKgXbhnQaVkwtphfwiyy8KFFK3atQmyngXq4l6fwxSS8EE87VhkSkL9sERE7MxWV28kmzVN_6JDlSyNCZWBtta7OOtL_3KA3cv4MQP8HWr7mgLAUzte9NYT6pYNo6PxABAMNxwp4mZERUjB5TUj3QstPjRZ4FhP8TpakEpRJVkpSTulUvPaPwDXcEBddYB6yXVNeCwYL0P4QlSqW6rt65DB6bOKKRykp9lf6VHbbMgv89hMouFqt6n7rrL6Hmmis1iuT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محله‌های «محبوب» و «نامحبوب» تهران کدام‌اند؟
🔹
نتایج یک بررسی درباره کیفیت زندگی شهری در تهران، تصویر متفاوتی از ۳۳۵ محله پایتخت ارائه می‌دهد. در این نقشه، محله‌ها بر اساس میزان رضایت و محبوبیت شهروندان، در پنج طیف رنگی از سبز تا قرمز دسته‌بندی شده‌اند.
🔹
محله‌های «داغ» مناطقی هستند که شهروندان از کیفیت زندگی شهری بالا و بسیار بالا در آنها رضایت دارند. در مقابل، محله‌های «سرد» با امتیاز پایین در نظرسنجی‌ها، به‌ صورت لکه‌های قرمز روی نقشه مشخص شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/679529" target="_blank">📅 23:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679528">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1Y559e0g8tPgmBZOxMgQyfu2n1maPlztAANxUfsIMYaY4EABjdaecI16kLlIESULRqzQ9gNALNy9Vdbo4oZXxk4QSKByBMNj-pW-tkifUg4FbogLYDx-WEuf6x5GoZP0qIERPS5M58OuIsRsZDmy2HCfyESPaOmxNL5Jdntv0e1-3mfxgIzliWiL3ZCGGZt4YntmGywKgVb_dokpg58tqmsGKrzsewws62KTPEMSnePbG8uI0B_4oZEnxmPKHFW8Ji-iZLwEF3L3tciVJi4_IhLkcYPjiMCzOyb5XZeb3NdchdmlinBVSUUL8ekrirY12WiL6iRyb2J0Fdo6Nm6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کسی که بر نفس خود مسلط باشد، از بسیاری از لغزش‌ها نجات می‌یابد
🔹
امام علی(ع) در حکمت ۳۲۸ نهج‌البلاغه، انسان را به شناخت و کنترل خواسته‌های درونی دعوت می‌کند. کسی که بتواند خشم، غرور و تمایلات نادرست خود را مهار کند، کمتر گرفتار تصمیم‌های عجولانه و اشتباهات…</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/679528" target="_blank">📅 23:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679527">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b829c766.mp4?token=NwnuhXwj2AV6vAVf5K9j9Z1ri9YRNZDpX54uy_tsgFTceHqCUmwAXl72fSmZAcwLgLgF3B6FezwjxW2r_hpzTHH5QQbB8zuZFYqQOTUKJmLp3_S_MNZ48_XKUpMp0WHccUayAu1HoKb1GThTBgWU5kGbDeSQVHBlKP-OA41yLJH3XKOvVFyQGIwHJAiiNOVtOqIROmue2MkxuMHJjKatg52WNCUfxgHkEzXnFfLX5Y3FaLTi5VhK6IZRh1WtDxo1KxwNaPmcvMdJ8dPMmZyBSXdJHQ6uSkp1xvkXxgoTjXawzCq09teDJ19CIqz6o3QvVrWGxytOJ0ZdPewuxJZ7Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b829c766.mp4?token=NwnuhXwj2AV6vAVf5K9j9Z1ri9YRNZDpX54uy_tsgFTceHqCUmwAXl72fSmZAcwLgLgF3B6FezwjxW2r_hpzTHH5QQbB8zuZFYqQOTUKJmLp3_S_MNZ48_XKUpMp0WHccUayAu1HoKb1GThTBgWU5kGbDeSQVHBlKP-OA41yLJH3XKOvVFyQGIwHJAiiNOVtOqIROmue2MkxuMHJjKatg52WNCUfxgHkEzXnFfLX5Y3FaLTi5VhK6IZRh1WtDxo1KxwNaPmcvMdJ8dPMmZyBSXdJHQ6uSkp1xvkXxgoTjXawzCq09teDJ19CIqz6o3QvVrWGxytOJ0ZdPewuxJZ7Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: یک تیم باید تشکیل می‌شد تا نقض تفاهم‌نامه را بررسی و حل کند نه این که دعوا کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/679527" target="_blank">📅 22:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679526">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde312c519.mp4?token=on_kyLYSkkk_zLAhNsuuW7s9rbIft4jxip3ppfAsxKTcITiJdT9-2bQNsP7kyZw6eTkVeeL7zMBckxJJJsl5rkwdmt7UUQMqDWI-gWuZzOTsT6GM4UT541IgWDaZciRi4ZfUD-66LGSuPBROG1TY3aHs_pEWwQk1xoGOxZMHgyI_KHo3EvnARsT4JSBlW3bghfNY_Rb_pXjgSawvQhZa5CweRMPV0F10Zn5OKSBZJai7qX_d7aXHrtrUIYoTFHPCl4NBHLT5GwSCbpnLxwSmf6Y-X2wd4s8iIE8jm2_TcUDXEsPYlGk86IgymwO6F19NRzzPUUWZfaoEXZqdbwwIZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde312c519.mp4?token=on_kyLYSkkk_zLAhNsuuW7s9rbIft4jxip3ppfAsxKTcITiJdT9-2bQNsP7kyZw6eTkVeeL7zMBckxJJJsl5rkwdmt7UUQMqDWI-gWuZzOTsT6GM4UT541IgWDaZciRi4ZfUD-66LGSuPBROG1TY3aHs_pEWwQk1xoGOxZMHgyI_KHo3EvnARsT4JSBlW3bghfNY_Rb_pXjgSawvQhZa5CweRMPV0F10Zn5OKSBZJai7qX_d7aXHrtrUIYoTFHPCl4NBHLT5GwSCbpnLxwSmf6Y-X2wd4s8iIE8jm2_TcUDXEsPYlGk86IgymwO6F19NRzzPUUWZfaoEXZqdbwwIZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: برای باز نشدن اینترنت فشارهایی وجود داشت و می‌گفتند اینترنت دوباره باز نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/679526" target="_blank">📅 22:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679525">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پی‌بی‌اس: بن‌سلمان به ترامپ گفت تشدید تنش با ایران کابوس‌وار است
🔹
یک مقام ارشد منطقه‌ای به پی‌بی‌اس گفت که در تماسی بین محمد بن سلمان و ترامپ، ولیعهد «سناریوی کابوس‌وار» را در مورد خطر تشدید تنش برای منطقه و انرژی جهانی ترسیم کرد.
🔹
این موضوع به ترامپ کمک کرد تا اواسط هفته خواستار این توافق شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/679525" target="_blank">📅 22:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679524">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
خبرهایی درباره حملات یمن به مواضع مزدوران سعودی
🔹
منابع یمنی گزارش دادند در این حملات، مقرهای عناصر وابسته به عربستان سعودی در مأرب، هدف حملات موشکی قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/679524" target="_blank">📅 22:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679523">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبرنگار؛ عجیب‌ترین تناقض‌های این روزگار!
🔹
خبرنگار، یکی از عجیب‌ترین تناقض‌های این روزگار است.
کسی که درد مردم را از نزدیک لمس می‌کند، واقعیت‌ها را می‌بیند و روایت‌هایی را با خود حمل می‌کند که گاه هرگز به صفحه روزنامه، سایت یا قاب دوربین راه پیدا نمی‌کنند.
نه از آن رو که حقیقت را نمی‌داند، بلکه چون هر حقیقتی الزاماً گفتنی نیست و هر آنچه دیده می‌شود، همیشه مجال انتشار پیدا نمی‌کند.
🔹
خبرنگار، همیشه آن کسی نیست که پشت دوربین ایستاده یا نامش پایین یک خبر آمده است. گاهی همان آدمی است که ساعت‌ها در انتظار یک پاسخ می‌ماند، بارها یک واقعیت را بررسی می‌کند و سرانجام، بخشی از آنچه فهمیده را نمی‌نویسد، نه از سر بی‌خبری، بلکه چون می‌داند میان «دانستن» و «گفتن»، فاصله‌ای به وسعت تمام مصلحت‌های جهان وجود دارد.
🔹
او باید بی‌طرف بماند، در حالی که انسان است و نمی‌تواند چشم بر همه چیز ببندد. باید محکم بایستد، وقتی خودش گاهی از درون فرو می‌ریزد. باید از امید بنویسد، حتی آن روزهایی که امید، در زندگی خودش کم‌رنگ شده است.
🔹
و شاید آمارها، سرد و بی‌احساس به نظر برسند اما این عددها روایت پشت صحنه همین خبرنگاران است.
🔹
بیش از ۵۶ درصد خبرنگاران، امنیت شغلی خود را کم یا خیلی کم می‌دانند. حدود ۵۴ درصد احتمال ترک این حرفه را زیاد یا بسیار زیاد ارزیابی کرده‌اند و تنها ۳۳ درصد گفته‌اند اگر به گذشته بازگردند، با اطمینان دوباره خبرنگاری را انتخاب می‌کنند.
🔹
این‌ها فقط عدد نیستند؛ تکه‌هایی از زندگی آدم‌هایی‌اند که هر روز برای ماندن در حرفه‌ای می‌جنگند که خود، سال‌هاست با ناامنی دست‌وپنجه نرم می‌کند.
🔹
روز خبرنگار، شاید بیش از آنکه روز تبریک باشد، روز دیدن باشد؛ دیدن آدم‌هایی که همیشه دیگران را دیده‌اند.
🔹
آدم‌هایی که خسته‌اند، اما هنوز می‌نویسند،
زخمی‌اند، اما هنوز می‌پرسند و گاهی شکسته‌اند، اما هنوز ایستاده‌اند.
#سرمقاله
@TV_Fori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/679523" target="_blank">📅 22:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679522">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVlr1Yf6boPUDtp8WPexh70vwlfNP03haCqOMNkZPuIF1ZtWxmc65oVFaOdKBouOg_JmdbAZQ8UhIeKw9n-I7KRoHIWC5hKfXeVJXlT0NZb2JTlS9FkHjCrQNRz2shCAlr5aGdt-NasoaiS9sOP0m6SMnE3F-5mbOPRQH2is5e3tirp4cvgCEZ0ooE05AVpY-sxnxOYHRUp2bvajWGcCC2QI1z1iciOqKB-sHTYAxyVd1fx1wyTLXdFZ-xMHmAll7EP2BA-r0KbH4MfNlsu0I-5bbb3LlxLHUH3Nv6WAhqocvsPCvIGGAN40gBTZc7TG1APYO_cKlhB0cn7hc5bh_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرانس‌۲۴: ایران هنر جنگ دارد
فرانس‌۲۴:
🔹
دیوارهای تهران فقط مجموعه‌ای از تصاویر نامرتبط نیستند؛ آن‌ها در کنار هم، یک متن بصری اصیل را تشکیل می‌دهند. با حرکت در شهر، از داستانی به داستان دیگر، از شهیدی به شهید دیگر، از یک مقطع تاریخی به مقطع تاریخی دیگر عبور می‌کنید.
🔹
شهر دائماً داستان تاریخ ملی خود را روایت می‌کند. این تصاویر به طور گسترده توسط رسانه‌های بین‌المللی در رسانه‌های اجتماعی به اشتراک گذاشته می‌شوند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/679522" target="_blank">📅 22:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679520">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a941f36f3c.mp4?token=CvyWiosjptmZ0BnzVPCN0P47nsMgCQUTW4WvRWnwaOPQUcL63Zxh57NgTF6bNcZU2G4JJiQLwYRxwlgZO8b7ke1SAPNx665QzGTfjJiRxlDi-sQhdcxyhjtqworSRXJq9Y4ZzjkocsNwtcZCMLhWaaSRUJk84Yt_3MyPOgYf9B58wgjzfkCQ4MhmVM9P3k8XILDv2R6KIrsFlkbG_4fliisMq6MA0jRpv1VaTtVpuseXfWRO44LoI5WdO42jpiWjFSzDP8asVb4uL-pMrbRQotgeqCpVqdIBjKE3-Mzum7cmCD_2Xa0o8a3QbFpdde2pnWWDoUUhdWuZZdwinmOV5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f36f3c.mp4?token=CvyWiosjptmZ0BnzVPCN0P47nsMgCQUTW4WvRWnwaOPQUcL63Zxh57NgTF6bNcZU2G4JJiQLwYRxwlgZO8b7ke1SAPNx665QzGTfjJiRxlDi-sQhdcxyhjtqworSRXJq9Y4ZzjkocsNwtcZCMLhWaaSRUJk84Yt_3MyPOgYf9B58wgjzfkCQ4MhmVM9P3k8XILDv2R6KIrsFlkbG_4fliisMq6MA0jRpv1VaTtVpuseXfWRO44LoI5WdO42jpiWjFSzDP8asVb4uL-pMrbRQotgeqCpVqdIBjKE3-Mzum7cmCD_2Xa0o8a3QbFpdde2pnWWDoUUhdWuZZdwinmOV5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ما تصمیم گرفتیم اینترنت باز شود/ دستگاه‌های امنیتی تهدیداتی را در این رابطه ملاحظه می‌کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/679520" target="_blank">📅 22:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679519">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36c106117.mp4?token=iSffSZR4eKgbfM1OaIn3vlIqM6R97w_YJbthpiZQvnjmlEW5tSQCADY72IELs_PDB2wUGaPZ1SXDmaynoKdLa9YgssgO-rjBqav0JsuA9lCuVBSY0RRSkLj_GL8dXK_tlIXV4DAz_NdN9klZUc1DO3YxUwQl3uZMHbm8wBrYDiradAp324FfS978XEI1opT2JeLIqZHSsQjqcEwNTOUDBUe8RPJ0y5xEjy2lapmytT0n_1QkLKYVjI7f3KKKd_xzEmpJqBfQ34HlPPF-GLl0R3O8mM3Pm_M0IWWhIsV4pYyq9t4lhK0TTSR9bNJTvpGslNicBwbcYmjEqpva7uAn1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36c106117.mp4?token=iSffSZR4eKgbfM1OaIn3vlIqM6R97w_YJbthpiZQvnjmlEW5tSQCADY72IELs_PDB2wUGaPZ1SXDmaynoKdLa9YgssgO-rjBqav0JsuA9lCuVBSY0RRSkLj_GL8dXK_tlIXV4DAz_NdN9klZUc1DO3YxUwQl3uZMHbm8wBrYDiradAp324FfS978XEI1opT2JeLIqZHSsQjqcEwNTOUDBUe8RPJ0y5xEjy2lapmytT0n_1QkLKYVjI7f3KKKd_xzEmpJqBfQ34HlPPF-GLl0R3O8mM3Pm_M0IWWhIsV4pYyq9t4lhK0TTSR9bNJTvpGslNicBwbcYmjEqpva7uAn1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: راه ما را بسته‌اند و کالاهایی که ارزان می‌آوردیم را حالا باید از چند راه و مسیر مختلف بیاوریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/679519" target="_blank">📅 22:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679518">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9442ae746.mp4?token=jF8D1K0-Fd0PQlhwJSgXtO16YE5w5PfKmIcvB1Aj7kPokGZjduIhXUioXRfhQ76Yud8JVcFxGU4_WZ9Hf1Ltmrlhr7uEt6yzmU3hoGrmJu71Jd88zSccFgiJopixkpbBv-5V-PAH1SWOonh9VA2jMiLjWdwKcYbMufSur2oH-IqsMcyFz3uMRZ4Ue2p-UwYOErfPqwF4nvDS0vCRz5ZaCe9J_YCvZGddZAxCpagBdXoR5myfQgtjoc2M3q4gSbv_QYRCg-kdvLuoClVRPAMEoussI-m25LTazeQ_MSMuGoiTAIow3iDHFN8vk_KoNspiNYskJ71mkIOkKdw9OvK1t4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9442ae746.mp4?token=jF8D1K0-Fd0PQlhwJSgXtO16YE5w5PfKmIcvB1Aj7kPokGZjduIhXUioXRfhQ76Yud8JVcFxGU4_WZ9Hf1Ltmrlhr7uEt6yzmU3hoGrmJu71Jd88zSccFgiJopixkpbBv-5V-PAH1SWOonh9VA2jMiLjWdwKcYbMufSur2oH-IqsMcyFz3uMRZ4Ue2p-UwYOErfPqwF4nvDS0vCRz5ZaCe9J_YCvZGddZAxCpagBdXoR5myfQgtjoc2M3q4gSbv_QYRCg-kdvLuoClVRPAMEoussI-m25LTazeQ_MSMuGoiTAIow3iDHFN8vk_KoNspiNYskJ71mkIOkKdw9OvK1t4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برندهای تلفن همراه بر اساس کشور سازنده‌
آن‌ها
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/679518" target="_blank">📅 22:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679517">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دفتر سخنگوی پلیس: تشکیل تیم کارآگاهانِ زبده برای دستگیری عاملانِ قتل حمیدرضا رجب‌زاده
🔹
بسته اینترنت رایگان برای خبرنگاران فعال شد
🔹
رئیس سازمان تروریستی سنتکام وارد تل‌آویو شد
🔹
روسیه: پایان درگیری آمریکا و ایران تنها از مسیر دیپلماسی ممکن است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/679517" target="_blank">📅 22:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679516">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7f7b0e195.mp4?token=uPbXQiJUMc_cDB4WcXFKy-OTAcU1wWfbUktierLpIrKyFUwq9uvULZNZuzoVlXJK5oHREu3w7gFuK2C5Qy3IwVwixIdlMxlZ1pt68URnf1gMlxq6L_oLrJESOBu0HuLKtNN7FPlBurnfMvXn8O4yFWze5J16Lmjfa8NPUaFRin3gN4A1I-F0ByadpBfyCjesFLBlaUBR_Bl6ZZNz8_cOQPjIxPc-i9IVNUCJ_zMl6Ye8Y31StRbQaWTHbg5GjLjMlFI3l2DLEsnas-QwAm6zNydTbwoFcTq6b7AGZtRRcZwsaIFQf1UthU6Ix9mU21BbJg3hSaBKkUqaXeh-IrKg5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7f7b0e195.mp4?token=uPbXQiJUMc_cDB4WcXFKy-OTAcU1wWfbUktierLpIrKyFUwq9uvULZNZuzoVlXJK5oHREu3w7gFuK2C5Qy3IwVwixIdlMxlZ1pt68URnf1gMlxq6L_oLrJESOBu0HuLKtNN7FPlBurnfMvXn8O4yFWze5J16Lmjfa8NPUaFRin3gN4A1I-F0ByadpBfyCjesFLBlaUBR_Bl6ZZNz8_cOQPjIxPc-i9IVNUCJ_zMl6Ye8Y31StRbQaWTHbg5GjLjMlFI3l2DLEsnas-QwAm6zNydTbwoFcTq6b7AGZtRRcZwsaIFQf1UthU6Ix9mU21BbJg3hSaBKkUqaXeh-IrKg5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پورجمشیدیان، معاون امنیتی و انتظامی وزیر کشور: ابعاد مختلف قتل آقای رجب‌زاده در دست بررسی است و نتیجه در اولین فرصت اطلاع‌رسانی خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/679516" target="_blank">📅 22:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679515">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
روش عجیب سرقت از منازل تهران؛ ورود از پنجره با موتورسیکلت
🔹
دو سارق با استفاده از یک موتورسیکلت طرح باکسر، به شیوه‌ای متفاوت وارد منازل شهروندان می‌شدند و دست به سرقت می‌زدند.
🔹
با تجمیع پرونده‌های مشابه و انجام تحقیقات میدانی، کارآگاهان اداره هفدهم پلیس آگاهی مخفیگاه متهمان را در استان‌های غربی کشور شناسایی و طی دو عملیات جداگانه آنها را دستگیر کردند.
🔹
متهمان در جریان تحقیقات به ۱۵ فقره سرقت مشابه اعتراف کردند و محل وقوع سرقت‌ها را نیز به پلیس نشان دادند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/679515" target="_blank">📅 22:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679514">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIGmlZZ2BPqA9kKMtbgqchLF9-1Ccg7OUkgabuXwd6yGq3KMVFvmijum2hVwHi9JngZhac5pL6z5sGYWrPtOP4KVfUSQ326z2A-WmkXN-Snf_cs8uk_BigQT-1uoygbjIJWKEVPy0Er4oQ8_z0l-VTvQaRsEGBxC60GwAw8IY-fInfI3fdHtMAcVDxr9YmBMJ0VIXdJzjIx3BJ0wfdZbrEEEQswyrrC9Vmg2H5tY9cd32QNprPMIS03t1mR12lYCyPgaPQBeFBvj0Y0lHSa9oC9EfSLvC2cN39CyIBzBoQGsXQRFUbPehHAPOB57H0ZZD0Kq0Tr-_Z7mAv6Gx2XvKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت پرسرعت رسپینا
هر آنچه از یک سرویس اینترنت انتظار دارید!
✅
سرعت بالا
✅
پینگ پایین
✅
بدون قطعی
✅
بدون نیاز به خط تلفن
✅
امکان اتصال هم‌زمان چند دستگاه
✅
انتقال ترافیک مصرف‌نشده به ماه بعد
🔎
بررسی پوشش و ثبت درخواست:
https://isp.respina.net/LTE-b
📞
021-9222</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/679514" target="_blank">📅 22:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679513">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
وزارت خارجه یمن: تشکیل ائتلاف هرگز مانع مجازات عربستان به خاطر جنایاتش علیه ملت یمن نخواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/679513" target="_blank">📅 22:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679512">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
حضرتی: سال گذشته، سال سختی برای خبرنگاران بود
رئیس شورای اطلاع رسانی دولت:
🔹
ملت ایران نیز تاب‌آوری را به زیباترین شکل ممکن تصویر و زیبایی سرزمین ایران را بر همه نمایان کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/679512" target="_blank">📅 21:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679511">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
دفاع از حزب الله لبنان؛ سیاست راهبردی جمهوری اسلامی ایران
رهبر معظم انقلاب:
🔹
جمهوری اسلامی ایران دفاع از مجاهدان مظلوم و مقتدر [حزب‌الله لبنان] را سیاست راهبردی خود تعیین کرده است.
🔹
بخشی از پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/679511" target="_blank">📅 21:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679510">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
احتمال پیوستن مصر به توافقنامه سه جانبه عربستان، ترکیه و پاکستان
🔹
هاکان فیدان، وزیر خارجه ترکیه مدعی شد که مصر ممکن است به این توافقنامه مشترک به محض حل و فصل برخی مسائل فنی بپیوندد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/679510" target="_blank">📅 21:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679509">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون آموزش: آمریکا و اسرائیل، دانشگاه‌های ایران را از رتبه‌بندی جهانی حذف کردند
ابوالحسن مصطفوی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
آمریکا و اسرائیل با نفوذی که دارند، نام دانشگاه‌های ایران را به دلایل سیاسی و جنگ، از جمع رتبه‌بندی دانشگاه‌های تاثیرگذار حذف کرده‌اند.
🔹
تا قبل از جنگ دانشگاه‌های ایران، حتی دانشگاه آزاد هم بخشی از این آمار بودند، اما اکنون رتبه‌بندی دانشگاه‌ها از حالت علمی خارج شده و سیاسی شده است. این اقدام نوعی تحریم علمی است و می‌خواهند با این کار فشار بیشتری بر ایران وارد کنند.
@TV_Fori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/679509" target="_blank">📅 21:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679508">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
مقام آمریکایی به رویترز: با پیشرفت بین عمان و ایران در تنگه هرمز، انتظار می‌رود به زودی توافق حاصل شود. در صورت اعلام توافق، ایالات متحده محاصره بنادر ایران را لغو خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/679508" target="_blank">📅 21:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679505">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-KfBzjkjFgIFaSRs9B1c3YUQMBlxupooEs6if4MW3Feqky1wR2Lb31lGjrc0O8fGK9sBP6L1oXz_GUYLfi_UfavB6fY0983BMWrYbS5fw6ZGgsTnNrWsUizTMrjZDafsR2NtDg4-fAAIV_wK1uq8I7UvidSAjGItQ-3ef2vRsFoSYWRYTWA2Makp0EoCDv6IQS7JUDQPd-MU_K51IWFwfeqGmuJrzJgApCnzstYcu-5PF_ovDhIMoJy6x5o9duD7ggbzTd_Ps11V89v7RoIc-9qFxJX2U77Us3d6ULx_xBEXj17MHuEJbB9E9vmefKv6RrqlQgeswFW08GshX_oOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XU0wqz-CT5pIMqkJDEFV0dRsAB44j3RoNO_K_6k0CRnTm7vSfoPqu_ZLrYDxgrTpIEJIJGmmfU_R8b9GmEU32M8hggXMMdbXfKHDPjlFZWMcjhVIRY9aoNVgaNYQCddigpgFsVx1sti7AmveEPHd3uGv_GRd9Ybxmk8kRq1GJJCf8vMAgSwMDNBJ5qAyPu7UraDdfMV1OthVrmvYhion14EItrwQkLJNxTBr5J5D5EczlWwcpJCEBASte_EFsMo1uGujIuLW3Jqs2TngsOBzNq96y9xSjOmlnry_X6a9knGNKj2QYqQwSTdCAcUaaiL2Js8LaMEB53TtxExgb_v7bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2050d29406.mp4?token=eSuRsSwy84ubdv0eBL4fGY0kvSSm4SIp4clGRmh5Yn1cAChZ1IUFOMIKgErpd0CfTEV9dvK3FyNlMeDqGj5iT7OPgt6DEYgEOQTrW34-yJe6SMXHc1x1fHdcbMgXKy3RtxQcnJvr6BORH6oRxJphwULMZgqdGNwdopW2Tv4dChW_PgGG436TW8KaDgHZ2Oj7TqEEI0AohTFRgyU4mU6L4wPiCZLGTeB28UtTz1D9__rrJwIel_Tzy8nTuRzDfgOYTwm0QlvY2NNkfCNxgDxrRXsOvpez_OtPEVEo4O7HtqkHVOVVtKUps6s_IZEtq5T4SMYpJtHzKc5N5xtxnlt-Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2050d29406.mp4?token=eSuRsSwy84ubdv0eBL4fGY0kvSSm4SIp4clGRmh5Yn1cAChZ1IUFOMIKgErpd0CfTEV9dvK3FyNlMeDqGj5iT7OPgt6DEYgEOQTrW34-yJe6SMXHc1x1fHdcbMgXKy3RtxQcnJvr6BORH6oRxJphwULMZgqdGNwdopW2Tv4dChW_PgGG436TW8KaDgHZ2Oj7TqEEI0AohTFRgyU4mU6L4wPiCZLGTeB28UtTz1D9__rrJwIel_Tzy8nTuRzDfgOYTwm0QlvY2NNkfCNxgDxrRXsOvpez_OtPEVEo4O7HtqkHVOVVtKUps6s_IZEtq5T4SMYpJtHzKc5N5xtxnlt-Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ریـکاوری فضاپیمای Starship در اقیانوس هند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/679505" target="_blank">📅 21:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679504">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf75ef521.mp4?token=tOoHEGgn1dmgm5VUx6IjRq8hOKju9KLAmFMiwdE3Dq0GAIUZAZ9letd_v2lcSa05w4etufZqJTJOrdDvZVd_hu1SAWuR691Uz87g5Tx7M1EDZ-OQ5X41XjnkWniZ1lJuWATJYRsKoRmWJRQSMAVuHILSN1LXvTyKCSw50e9BvG2whHBXT_IEm3Huw64gdGq_ewCf1_HUO1gXFsuFoZShVSHFtP0EqHo7uSLf7rkMqNL-7OmfEfnNy0LMgw6XcRMUIsKA2tPlgOhhVjtgT2IC4RM8kwF4fsXAGeLMwwKt6aLLhxk3ieI7bCKNXqKshaEJzOQFBipwoFNylg3hxKW9_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf75ef521.mp4?token=tOoHEGgn1dmgm5VUx6IjRq8hOKju9KLAmFMiwdE3Dq0GAIUZAZ9letd_v2lcSa05w4etufZqJTJOrdDvZVd_hu1SAWuR691Uz87g5Tx7M1EDZ-OQ5X41XjnkWniZ1lJuWATJYRsKoRmWJRQSMAVuHILSN1LXvTyKCSw50e9BvG2whHBXT_IEm3Huw64gdGq_ewCf1_HUO1gXFsuFoZShVSHFtP0EqHo7uSLf7rkMqNL-7OmfEfnNy0LMgw6XcRMUIsKA2tPlgOhhVjtgT2IC4RM8kwF4fsXAGeLMwwKt6aLLhxk3ieI7bCKNXqKshaEJzOQFBipwoFNylg3hxKW9_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ به سوژه قدیمی فوتسال ایران: وحید شمسایی برنج نمی‌خورد اما...
/ تلویزیون اینترنتی مدار
مدار ورزش را در یوتیوب تماشا کنید
👇
https://youtu.be/-mkGvm-uJ2w?si=oN8NML-TG1LuhM0a
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/679504" target="_blank">📅 21:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679503">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF5zYQUv3D1hrsEiDBSdqc68TS2w7ZGef8paryfXOWIsSQHdgTg1jIILQdoWay0FG7JgVOAMFuW6Qo5r1ekWs_us8RvC-bAeRdsGJ2C5TXvPHYjKMxHYjoKeqe50o1W74AvXj7P858jt2I0tcsjBQNOKhVnVlp7qroO0D-hLvY_daDBcakaxlHVJQk95SyLunJtDpOFOyIJnSMGlwHDacfCqjHk9WWBfWZTTLPet3wdaTJAylWAkQIf8zkIW-lS3Q8erd6Qy4yOANZL4Ob57KMmqQPOo0IqD3TO6B8YAp4tBLEMiYADrXgJE-CUH9uPydibPU6AokGjFb6deGq1WIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت صحنه، یک راز پنهان است
🔹
ژانر:درام اجتماعی|جنایی
🔹
«صحنه‌زنی» قصه‌ای پرتنش از دروغ، خیانت و بازی‌هایی است که مرز میان حقیقت و نمایش را از بین می‌برد.هر شخصیت چیزی را پنهان می‌کند و هر تصمیم، ماجرا را خطرناک‌تر از قبل پیش می‌برد. فیلمی برای دوستداران…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/679503" target="_blank">📅 21:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679502">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7fswiPfwE2ifKxdc0BHZDb9uwdCxifgUn5BW2IhJRQcPHNdMXyDE1H5giniej_On-IELMH88A5SyrAcDabJ9EYv0mnzvnvwfeGStlQjDLacBy7CddUgcwz856sM0xV-WWWqSIXl1MCpPsDMZziN5Mg8QQGaYlTCPk8z9Gpbg7NkCczehdDF5UFyJiSQqHXHb29ZEuBT1t0TtJyRgGbpOYYxadXGyTB8ZqM5SPP7MC4FdIZGv-U8r_BLeyVu9C2Pqq7CXne0uOnZxALZN2WKKDVDeigkEUVvJbRfj6kcR8rlFvQXFg1QMaQ55xZLs0Z-iErOE9Y3y4qzYMd8g0C7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
قبل از اینکه بیمه بخری، این ۵ سوال رو از خودت بپرس!
۱. آیا شرکت تحت نظارت بیمه
مرکزیه
؟
۲. می‌تونی همه شرکت‌های بیمه رو با هم
مقایسه
کنی؟
۳. اگه سوالی داشتی،
کارشناس
پاسخگو هست؟
۴. امکان
خرید قسطی
(بدون پیش‌پرداخت) وجود داره؟
۵. بعد از خرید هم کسی هست که توی مسیر
خسارت
کنارت باشه؟
✅
اگر پاسخ همه‌ی این‌ها
بله
است، یعنی جای درستی اومدی.
ما در
بیمه‌بازار
، همراه شماییم تا تجربه خوبی داشته باشید.
👈
برای مقایسه بیمه ها وارد شو
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/679502" target="_blank">📅 21:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679500">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cx5tlMlEiezyA7s0Woq4uSqGWEAS6nHHw0Ely1BvgU88Ry_h6qL3nRHs2AJevFf3xMqEyDoOQLbXjt2DLwodppmZ2_3_Ffh54ZtaF0WOhiHM8nJiLALgbKtJNYZiy57GD4k_orPyhnE7xXybV031GPSkiVq03wGWvz8R4pTGq-BGIEKepNl5pyl24V6QjlNqAMEi08NgwgUN7VQvSNfHrg5X7jgxbCOGNfHDlbaNE7S_HdEwpPer6d2I2axQtAtrJuPQngYHoxRSida7bvr4lHDivlF4YpWTPqSY8M7-BvvnF4lQGdzkO1TaLPpasxt02OOQMBSgissr1AdMPk1Q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محبوب‌ترین بازی‌های ویدیویی در جهان کدام‌اند؟
🔹
ماینکرفت در بخش بزرگی از آمریکا، اروپا و استرالیا محبوب‌ترین بازی است، در حالی که پابجی در غرب آسیا و جنوب آسیا جایگاه پررنگ‌تری دارد.
🔹
همچنین بازی‌هایی مانند گنشین ایمپکت در چین، جی‌تی‌ای ۵ و فیفا ۲۱ در بخش‌هایی از آفریقا و لیگ آف لجندز در کره جنوبی بیشترین میزان محبوبیت را دارا هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/679500" target="_blank">📅 20:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679499">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
وزارت اطلاعات به مناسبت روز خبرنگار: خبرنگاران در جنگ تحمیلی اخیر، نقش بارزی در حفظ و افزایش تاب‌آوری و انسجام جامعه و ناکامی دشمن آمریکایی _ صهیونیستی و سربازان رسانه‌ای آن داشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/679499" target="_blank">📅 20:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679498">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
خشم خانواده نظامیان آمریکایی از شرایط ناو اعزام‌شده به جنگ ایران
🔹
به گزارش ام‌اس‌ناو، خانواده ملوانان مستقر در ناو ابراهام لینکلن در روزهای اخیر دو جلسه حضوری و مجازی با فرماندهان ارتش از جمله سرپرست موقف نیروی دریایی آمریکا هانگ کائو داشته‌اند.
🔹
در این جلسات پرتنش، آن‌ها درباره سلامت روان ملوانان، ایمنی در عرشه، کمبود تجهیزات، کمبود مواد غذایی، آلودگی در ناو و اختلال در سیستم پُست ابراز نگرانی کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/679498" target="_blank">📅 20:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679497">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoUeO73MmqF9M5jsTsUnw9B4mBrEWkAjLpxIodVxPtpxC1J45BYteF9RhwSdrsdt-j5I1Ve6XhGnjYfiQZwWEv9qkvt4Rj-VNc50Z7bBt_8XVU3Kgn3YPdWf2yV7hTIRF197ntKBB_Gk6qntEOuty8ojmdTL4M_SntRou7B8uByQIEwy12vEisUfXhG5y4ghaePd4RxpMYJbdXQOU7Lb_ajTXR9etYmRU-xSwRHCnf5B6or16Qu5pNN7ch9e2nmW6B7HtROGuqOSQ7VApqHix_UUA-hihivDS2QxGdmXFRe3Z0IsP0o_NdVXAWV5d8NMg3Hl00v8-_EdXeaKQN8Kvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش رئیس کمیسیون امنیت ملی به توافق مکه: هیچ اشتباهی بی پاسخ نخواهد ماند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/679497" target="_blank">📅 20:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679496">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
پزشکیان با تأکید بر اصل رفتار متقابل در مذاکرات: هر مقدار که آنها جلو بیایند، ما نیز جلو می‌رویم و هر مقدار که جلو نیایند، ما نیز آن را نمی‌پذیریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679496" target="_blank">📅 20:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
موج خوش‌بینی در بازارها
🔹
امیدواری به بازگشایی تنگه هرمز موجی از خوش‌بینی را به بازارهای جهانی تزریق کرد؛ به‌طوری‌که هفت بازار مهم از مرزهای روانی تازه‌ای عبور کردند.
🔹
طلای جهانی از ۴۳۰۰ دلار، نقره از ۶۰ دلار و مس از ۱۴ هزار دلار فراتر رفتند؛ هم‌زمان شاخص S&P ۵۰۰ از محدوده ۷۷۰۰ واحد گذشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/679495" target="_blank">📅 20:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679493">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
روایت تجربه نزدیک به مرگ؛ گفتگوی دو روح پس از یک سانحه تصادف
🔹
00:06:00 جدایی روح از بدن دو همسفر به طور هم زمان
🔹
00:10:40 تأثیر نور تونل برزخی بر گندم‌زار دنیوی
🔹
00:29:45 ارزشمندی جایگاه کمک‌رسانی به ایتام
🔹
00:33:40 اثرات رفتار پرستاران برای بیماران در کما
🔹
00:40:40 رنج و عذاب روح از شیون و ناله بازماندگان
🔹
01:04:00 آسیب‌های جسمی، آغاز نگاهی تازه به زندگی شد
🔹
01:12:00 شفا یافتن در کما توسط امام رضا(ع) با توسل برادرم در حرم مطهر
🔹
قسمت بیست‌وپنجم (طعم زندگی)، فصل پنجم
🔹
#تجربه‌گر
: هادی عباسی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/679493" target="_blank">📅 20:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679492">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f444f4949b.mp4?token=ZzBfTBnYVmHzkyAls6ktdpc8lxphPIICtqLOKhka3DJYwY3YrvOmA12P7Qug7pGlIR1SluMonMj4TG7v_M9xgmJA8YTq-g3Msj_H0DadvKxWLUNpNS5qLBwPoRT1R56AWy0JL9ECApbP7LL46SPwdZCP-SoyIBkSBNAoTFv4lu3E5-IIOzgmY4ot_XCnOcM82diUeIFDcOs8tCnbtqPZPiRmNO5_rj7q5hMHw0Xnct-gwOYY3vU8Gf90PaHzNp4QJTS_Ls9-bUi9_eBin3UQ2aApssNbyOgyxbR1pYthMB58K6yJhhDzPe5yisFOGRbo1Wy5-DLb3nvRuBQUyxlzH0_pijnPusAIsDX_SPVoPGyW76wcGSWsmeUUG7aJ3amBZeMMrs-TAk17r7mSOFLHkV5NJOnZ0OVKHd2qrNPJ5no8jk0HalNNZc06k1p5ZQ_kClCIxSGMGH5pFehOU0uULzKbDes1w2NPD-esHCDz0QTTiwt5tbi7IMXIHZkogQBmwEgY13FCRXdPOp4aCgIGFYueH_BUMibC9zZ3Gwmm7-X5bgLqSg6bZBSq-rKHS8SWF2d-eDdh5Xiiq5oRhM1ThQbGiZ6Vpwtf5FLZwnLeEM43fAsQbWLdVLS72h_KhVJUNusXk_sGaJ_do9ehgund_CjckLz8_-Ot9-yK_lUk0M8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f444f4949b.mp4?token=ZzBfTBnYVmHzkyAls6ktdpc8lxphPIICtqLOKhka3DJYwY3YrvOmA12P7Qug7pGlIR1SluMonMj4TG7v_M9xgmJA8YTq-g3Msj_H0DadvKxWLUNpNS5qLBwPoRT1R56AWy0JL9ECApbP7LL46SPwdZCP-SoyIBkSBNAoTFv4lu3E5-IIOzgmY4ot_XCnOcM82diUeIFDcOs8tCnbtqPZPiRmNO5_rj7q5hMHw0Xnct-gwOYY3vU8Gf90PaHzNp4QJTS_Ls9-bUi9_eBin3UQ2aApssNbyOgyxbR1pYthMB58K6yJhhDzPe5yisFOGRbo1Wy5-DLb3nvRuBQUyxlzH0_pijnPusAIsDX_SPVoPGyW76wcGSWsmeUUG7aJ3amBZeMMrs-TAk17r7mSOFLHkV5NJOnZ0OVKHd2qrNPJ5no8jk0HalNNZc06k1p5ZQ_kClCIxSGMGH5pFehOU0uULzKbDes1w2NPD-esHCDz0QTTiwt5tbi7IMXIHZkogQBmwEgY13FCRXdPOp4aCgIGFYueH_BUMibC9zZ3Gwmm7-X5bgLqSg6bZBSq-rKHS8SWF2d-eDdh5Xiiq5oRhM1ThQbGiZ6Vpwtf5FLZwnLeEM43fAsQbWLdVLS72h_KhVJUNusXk_sGaJ_do9ehgund_CjckLz8_-Ot9-yK_lUk0M8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکید صریح همتی بر تشدید نظارت بر بانک‌ها
🔹
عبدالناصر همتی، رئیس‌کل بانک مرکزی در بازدید از موسسه مطبوعاتی پول و ارز و تحریریه ایبنا در روز خبرنگار با تأکید بر نقش اضافه‌برداشت بانک‌ها و خلق نقدینگی در افزایش تورم گفت: کنترل مقداری ترازنامه بانک‌ها با جدیت دنبال می‌شود و اجازه داده نخواهد شد بانک‌ها بدون پشتوانه و خارج از اراده سیاست‌گذار پولی اقدام به خلق پول کنند. به گفته او، در ماه‌های اخیر اضافه‌برداشت بانک‌ها تغییر محسوسی نداشته و نظارت بر این موضوع در سال جاری با جدیت بیشتری ادامه خواهد داشت.
🔹
رئیس‌کل بانک مرکزی همچنین از برخورد با شناسایی سودهای موهومی در بانک‌ها خبر داد و گفت: بانک‌ها نباید مطالباتی را که سال‌هاست وصول نشده، صرفاً روی کاغذ به‌عنوان سود شناسایی کنند. این سیاست به‌صورت تدریجی اجرا می‌شود تا شوکی به شبکه بانکی وارد نشود، اما در نهایت بانک‌ها برای مطالبات و دارایی‌هایی که امکان وصول آن‌ها وجود ندارد، اجازه شناسایی سود نخواهند داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/679492" target="_blank">📅 20:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679489">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ5O7jIlxL_36Hul1RwSXA0NIKcZIjaBfVwjE2G7CCEUgmuPFllRy_j4MrTm9eoc5DAUCaHRpLY16BdGkVrPMH1eCcsRb31nvEw-iOM9oi5DeU_UM0hi3y6pVYbOEk_iOhgzVTDepP3anZhzGHeoDRdZs5N_EVCt1vk_jPEjWoPe8krifcqr3z5RlriKP-y1Kt6mjWi4Owh3Dw9Y6ddsv2P7Qnq6A7pm2e4W4p1hL6g9IL8G0DGxMBJetyx0cB99AMNvW_TDiR_OyZMRNzWVH0kOqpV71nvF3LGmQnKx2M93ZNzTw9UP42VbWs0HzAK6HDLq0WivbE5qvgmrzYV22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a871cc9019.mp4?token=fFn3f38E6nDTE9Nv6GHCEcy-M9FVJund57pZ3tUseNUUNT8rGVVKQhTn14n9brDfoGmcnSgC30ivmdi2BrRGngNzi7DrVWn9GLsmE9FGGhXEWLYGnjFeXDixWcS0iUvweJHXz-naeJvnZaO2eXEMnz2lg5oDWF7t0vVghSWIcu6UQ00jMGBNLK0hlXFyqB03HPU16TppJQfkTDzP_7gpqnYCnHg8isIUo3z96oMJenOlpRan3stUmcThb8cBEPAculjsSC_SpBEsOWJY8XxGAnvYmfRLVleEzthq-8UlM_LN-aQ-0ignvaO29BbP3hrFlo6-wE3SeQFxQgLPIimwjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a871cc9019.mp4?token=fFn3f38E6nDTE9Nv6GHCEcy-M9FVJund57pZ3tUseNUUNT8rGVVKQhTn14n9brDfoGmcnSgC30ivmdi2BrRGngNzi7DrVWn9GLsmE9FGGhXEWLYGnjFeXDixWcS0iUvweJHXz-naeJvnZaO2eXEMnz2lg5oDWF7t0vVghSWIcu6UQ00jMGBNLK0hlXFyqB03HPU16TppJQfkTDzP_7gpqnYCnHg8isIUo3z96oMJenOlpRan3stUmcThb8cBEPAculjsSC_SpBEsOWJY8XxGAnvYmfRLVleEzthq-8UlM_LN-aQ-0ignvaO29BbP3hrFlo6-wE3SeQFxQgLPIimwjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واژگونی تانکر سوخت در بغداد
🔹
در پی واژگونی تانکر حمل سوخت، آتش‌سوزی گسترده‌ای در منطقه الشعله بغداد روی داده که در نتیجه آن چندین خودرو هم دچار حریق شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/679489" target="_blank">📅 20:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679488">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
پزشکیان: دشمن آمریکایی ادعا کرده بود که در کوتاه‌ترین زمان ممکن، نظام مقدس ما سقوط خواهد کرد؛ اما دفاع جانانه رزمندگان ما و حضور استثنایی مردم اجازه ندادند دشمن به اهدافش برسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/679488" target="_blank">📅 20:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679487">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
پزشکیان: کشورهای همسایه با جدیت در مقابل افرادی که قصد ورود از خاک آنها به ایران و ایجاد آشوب داشتند، ایستادند
🔹
افغانستان و پاکستان از سوی دولت‌های خود گروه‌هایی را برای کنترل این وضعیت مستقر کرده بودند و اعلام کرده بودند هیچ‌کس حق ندارد از خاک آنها وارد…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/679487" target="_blank">📅 20:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679486">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3PxdRp8so1kvbRVeBsEyaxwr7uNEbMyESvOPSmd4EnoUbYxtL9zf2QdgwjQtkqq8RJRSj9aonfGPIf8BwFhAhaeCMkVcwzZJVuUtDNFHzzFmct6Tka7YvBQ2r0k0WewVJGb1zFBTBMOKLXkAW5ONcPA8Sd6bx6FbMGVG_3IO9UinyvW1X8AFaBQppvbPOPburhyAaBl2sU8_YEaVy1NyvMfecoABDJvfFUpjoJi9ortGJh5x-xk3sRMHTS_YUDmMsU4zQH8J-fQXrcEDdI74UgBSPU4IQKOao4Ort29_UdTji9gHLUs49cLhXUrfs4JkjlkzPdBxnW6_O04JE62Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرداران بی نگار
🔹
خبرنگار، الزاماً بی‌خبر نیست؛ گاهی بیش از هر کسی درد مردم را می‌فهمد و واقعیت‌ها را می‌بیند، اما همه آنچه می‌داند گفتنی و هر آنچه می‌بیند قابل انتشار نیست. او میان حقیقت و مصلحت، میان رنج مردم و محدودیت‌های گفتن ایستاده است. قشری که گاه نه نزد مردم محبوب است و نه نزد مسئولان، و در بزنگاه‌ها، دیواری کوتاه‌تر از او پیدا نمی‌شود. کسانی که خود زیر فشار معیشت‌اند و به لحاظ روانی درگیر یکی از سخت‌ترین مشاغل هستند. روز خبرنگار، فرصتی است برای یادآوری این حقیقت که خبرنگاران، آن چیزی نیستند که می‌بینید؛ پشت این سکوت‌ها، انسان‌هایی ایستاده‌اند که شاید بیش از همه، خسته و مظلوم‌اند.
🔹
هشتصدوسی‌امین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/679486" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679485">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
آغاز تحقیقات سازمان ملل درباره جاسوسی کارمندش برای اسرائیل
🔹
مقام سازمان ملل گفت که یونیسف در حال رسیدگی به گزارش‌ها علیه یک کارمند ارشدِ خود بوده که متهم به اشتراک‌گذاری اطلاعات محرمانه سازمان ملل با دیپلمات‌های اسرائیلی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/679485" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679484">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بلایی اومده سرم</div>
  <div class="tg-doc-extra">کربلایی حمیدرضا رجب زاده</div>
</div>
<a href="https://t.me/akhbarefori/679484" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
مداحی از شهید رجب زاده
بلایی اومده سرم...
😭
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/679484" target="_blank">📅 20:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igC5k5sljQ9z9JKoj60x2UF8O6zx8C0cJr1K-pT5vEzd4Non8JGtj4kjxsoqdhEWxfd9Orakf3Lva1ag6WFaZV6V4MKYQGdG9dOfBf4WKkJ43n0fjm7CczY5sy3tNvgOIBI7JbhT44NVc58Cwk-bROdltrClOZFkFD2ngDKQrEyblqX4v90WN-c9n13eyExRa_XhF1UH_bRttSepy3LbxGKSPigEJC9o2V3HRapR5DbECj7joCVvSZxpkBpO3-wmVt_Xs2Sd56QkD2KFo4rgn29zZkV0gNDFhEL_etFj5LNlAtCZXRMQKqBPR4ixHgsS9CIp24uDg3Fo0k4c3bnjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/679482" target="_blank">📅 20:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
پزشکیان: دشمن آمریکایی ادعا کرده بود که در کوتاه‌ترین زمان ممکن، نظام مقدس ما سقوط خواهد کرد؛ اما دفاع جانانه رزمندگان ما و حضور استثنایی مردم اجازه ندادند دشمن به اهدافش برسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/679481" target="_blank">📅 20:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8eb2c02e.mp4?token=elKoRZVYGiqPdwfaK_5_J06uxVmnxDJEAh8NAZL-PeT1zP8ZZ1JP6PtZ4qrJM4IeNpjtRPO9vY87lU4fbsO-YfPTWnMrxU7lWFQogYemWDxkN7IoY9qNS4SzvtwQUQnw70QxZhT6raBA298yTZcqkIq3FcXxHv3b7paacccZ4Q11o-H2Zc1f_XGfhiwPOwG2_Es6SPu9l3JeQUlXsNdF48qGoeesQIRDYqDG2KjLZapTdfU2aRTU61yYNc3AJ7-dhuTnCs22_4qZI0iO6SfNedP_kB-JkcTIAdibPO6mrNi-Iub_nsET2NLrf_ics-QpAPD04XYU3r4kSvdbK9boWhs3LJXxYQsfNMKSMs6HPcekpOu1tbE4n24e8Tqs7IKornuW_e-j2FKuL4wCp1H4Yf3M1eK1iqXGpVRdXPegoVg4tNEe2xvbUMsvQeGoEAbvv3IFWtG2BpqlWxg6QhYKkgqE8cFFrzIoXzlmLHICpGUWM5HmZWO72xo-g0swsmW2RB7Xzkk9t1YppITLbdw_d6TJTMJvEa3qBv5lQRUJ6c-9-shUeb0RdPEFURSq9uKi9t8ZU2cFXjHCqRFPDDpUxAJU7asbYvLnMa3fdY5qbvzZG_7pMrwnVRNWvOzBpWjQBDobDR-Kikhgsu0Y9W_5rtZXXIFqYmU48o_9C_lbKH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8eb2c02e.mp4?token=elKoRZVYGiqPdwfaK_5_J06uxVmnxDJEAh8NAZL-PeT1zP8ZZ1JP6PtZ4qrJM4IeNpjtRPO9vY87lU4fbsO-YfPTWnMrxU7lWFQogYemWDxkN7IoY9qNS4SzvtwQUQnw70QxZhT6raBA298yTZcqkIq3FcXxHv3b7paacccZ4Q11o-H2Zc1f_XGfhiwPOwG2_Es6SPu9l3JeQUlXsNdF48qGoeesQIRDYqDG2KjLZapTdfU2aRTU61yYNc3AJ7-dhuTnCs22_4qZI0iO6SfNedP_kB-JkcTIAdibPO6mrNi-Iub_nsET2NLrf_ics-QpAPD04XYU3r4kSvdbK9boWhs3LJXxYQsfNMKSMs6HPcekpOu1tbE4n24e8Tqs7IKornuW_e-j2FKuL4wCp1H4Yf3M1eK1iqXGpVRdXPegoVg4tNEe2xvbUMsvQeGoEAbvv3IFWtG2BpqlWxg6QhYKkgqE8cFFrzIoXzlmLHICpGUWM5HmZWO72xo-g0swsmW2RB7Xzkk9t1YppITLbdw_d6TJTMJvEa3qBv5lQRUJ6c-9-shUeb0RdPEFURSq9uKi9t8ZU2cFXjHCqRFPDDpUxAJU7asbYvLnMa3fdY5qbvzZG_7pMrwnVRNWvOzBpWjQBDobDR-Kikhgsu0Y9W_5rtZXXIFqYmU48o_9C_lbKH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شارژت زود تموم میشه؟
🔋
این تنظیم‌ها رو فعال کن تا باتریت بیشتر دوام بیاره
⚡️
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/679480" target="_blank">📅 20:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
محدودیت جدیدی متوجه کاربران و فعالیت صرافی آبان‎تتر نیست
🔹
در پی انتشار اطلاعیه اخیر دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا درباره آبان‌تتر، ابهاماتی درباره تأثیر این اطلاعیه بر فعالیت صرافی و دارایی کاربران مطرح شده است.
🔹
آبان‌تتر در واکنش به این موضوع اعلام کرد که
این اطلاعیه محدودیت جدیدی برای فعالیت این مجموعه ایجاد نمی‌کند و فعالیت صرافی همچون گذشته ادامه خواهد داشت.
🔹
بر اساس توضیحات آبان‌تتر، خزانه‌داری آمریکا در اطلاعیه خود به انجام تراکنش با برخی صرافی‌های ایرانی که پیش‌تر مشمول تحریم شده‌اند و همچنین فعالیت آبان‌تتر در بخش مالی اقتصاد ایران اشاره کرده است.
🔹
آبان‌تتر تأکید کرده که انجام تراکنش میان صرافی‌های داخلی، بخشی از تبادلات معمول این بازار است.
🔹
همچنین
فرمان اجرایی E.O. 13902
که در این اطلاعیه به آن استناد شده، یک چارچوب عمومی مرتبط با بخش مالی اقتصاد ایران است و با تحریم‌های مبتنی بر
E.O. 13224
تفاوت دارد.
🔹
بر این اساس، آبان‌تتر اعلام کرده است که این اتفاق
محدودیت تازه‌ای برای فعالیت صرافی یا دارایی کاربران ایجاد نمی‌کند
و فعالیت مجموعه طبق روال گذشته ادامه خواهد داشت.
🔹
این صرافی همچنین با تأکید بر اینکه امنیت و شفافیت دارایی کاربران همواره از اولویت‌های آن بوده، اعلام کرده است که کاربران از بابت امنیت دارایی‌های خود اطمینان داشته باشند. تیم پشتیبانی آبان‌تتر نیز برای پاسخ‌گویی به پرسش‌ها و ابهامات کاربران در دسترس است.
متن اطلاعیه وزارت خزانه‌داری آمریکا
Aban Tether is another Iran-based digital asset exchange. It has processed millions of dollars’ worth of transactions involving previously designated Iranian digital asset exchanges, including Nobitex, Wallex, Bitpin, and Ramzinex. OFAC is designating Aban Tether pursuant to E.O. 13902 for operating in the financial sector of the Iranian economy.
ترجمه
«آبان‌تتر یکی دیگر از صرافی‌های دارایی دیجیتال مستقر در ایران است. این صرافی میلیون‌ها دلار تراکنش مرتبط با صرافی‌های دارایی دیجیتال ایرانی که پیش‌تر تحریم شده‌اند، از جمله نوبیتکس، والکس، بیت‌پین و رمزینکس، پردازش کرده است. OFAC آبان‌تتر را بر اساس فرمان اجرایی E.O. 13902 به دلیل فعالیت در بخش مالی اقتصاد ایران، تحریم می‌کند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/679479" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
واکنش پزشکیان به ادعای استعفای ذوالقدر از دبیری شورای عالی امنیت ملی: یک سری اختلافات مطرح است که تلاش می‌کنیم برطرف شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/679478" target="_blank">📅 19:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تصادف موتورسوارها فقط اعداد و ارقام نیست؛ اینجا صحبت از جانِ آدم هاست....
🔹
این قبیل گزارش‌ها زیاد گرفته شده، اما هر حادثه جراحت و داغی بر پیکر افراد و خانواده آنها می‌گذارد که شاید برگشت‌ناپذیر است. ای کاش هم مسئولان و هم موتورسوارها کمی جدی‌تر به این اعداد نگاه کنند.
@TV_Fori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/679477" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
واکنش پزشکیان به ادعای استعفای ذوالقدر از دبیری شورای عالی امنیت ملی: یک سری اختلافات مطرح است که تلاش می‌کنیم برطرف شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/679476" target="_blank">📅 19:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">طرح جدید برای زائران عتبات؛ مردم آسانتر و با هزینه کمتر راهی عراق می‌شوند
محمد جواد فائض پور، مجری پروژه زائرکارت اربعین در گفتگو با خبرفوری:
🔹
در پروژه زائر کارت اربعین تمام نیازهای زوار دیده شده است.
🔹
تلاش داریم که هزینه سفر به عراق در ایام اربعین را به صفر یا حداقل برسانیم.
با ۱۶ هزار فروشگاه قرارداد بستیم و در صورت خرید مایحتاج روزانه، کیف پول اربعین شارژ می‌شود.
🔹
در این طرح و طرح‌های آتی بسیار تردد آسان تر می‌شود و قرار هست این موارد توسعه یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/679475" target="_blank">📅 19:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679474">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6IYadTV0yMgdRNibAbYfAfcXjPTTdhQIoFsl8xAF7k0DV4QZ9o716wi58uVeZv7u21a_dfW_D_Witu60ea8VmG-qKoyLSF6sy9lNNW3fSVsTTG3GuyvfBQ2MxLSuiAg-IUNy1XE_wnXnXLk9Ao895pKA23-i0BeuAdYZeroAgcB8xj5-H53dI-Cg6Q-tfEh-XgxyeQYoslLqUpvpawjcznHDYFVT65zRrhZayFYvBA8yxQfQsstXCqiIDiw9kXhdKJsKmNwzAHTl_Q-OAzlzWoNj0LfNcs3fAKvC-dHDSj1mRR2yCTGpjKbZYSXy6figGtgrWcmeENp6QiTCfhWoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه اینترنت را برای کودکان امن کنیم؟
🔹
این روزها اینترنت به بخشی از آموزش و سرگرمی کودکان تبدیل شده است، اما در عین حال احتمال سوءاستفاده از آن‌ها در این فضا وجود دارد.
🔹
زمان‌بندی مشخص برای استفاده از اینترنت و تشویق کودکان به فعالیت‌های غیرآنلاین، از راهکارهای اصلی ایجاد امنیت دیجیتال است.
🔹
همچنین استفاده از نرم‌افزارهای کنترل والدین و آموزش عدم انتشار اطلاعات و تصاویر شخصی، نقش مهمی در حفاظت از فرزندان در فضای مجازی دارد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/679474" target="_blank">📅 19:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679472">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4Oxbrm0MkAnN9jEh8Ge1AejVjnaKrMkH8W7F_vvR-X4y20VPoU1pcKra81Kt9QZ2wpKVXyjnXdLdgX4PxVV8lPZT281PmD9du2DEu3_ct3jcBaXxoNgzeKmZ2eKd-aN06_tpF8xdovedjh49w16e0fWpl7rxwM5mi-F8YLMiB4tQbKvdGamlqtSld7tjJTbUOKv2BlRD3huJP_QOEapwKB7pqAygM4HvrUeyAZL9mHbL-uWcQeKEi8s1gQQaIp_cNUPtudn5HD35MWWwGcryUCjTxnx1VqGEh4bp0XLi1Bgd9hqbwMiY3rEC44vWPWj5naCZ1GapnfZWcYXJBOGsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر امروز ماهواره کوپرنیک از وضعیت دریاچه ارومیه و مقایسه با زمان مشابه سال قبل
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/679472" target="_blank">📅 19:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679471">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XicNffLvn1zpgCd0Qy3f73E4iLpJ6pfi2Wkf9NZbKT4YMgIhhm5_CO9iX-7r7g0KM5gJQW8BlAyaP8fBye9VyOOwPZvrA8cAhilaWwEepAh4jwmKVgx3qN1REIb9ZcMr9lSrYRUpysmRz6JcB4ZjO2O44mQhKIvM26KUiFmNvSJZlv_yjMrDYMGa95MLqLhgMj88vZTyWh47fLnSVLXJR2AwCK2V7QAyCJANVGBPAO_SXc6I__6pAzvYxU8ck4xMM8_8tuqp1ncHXeBhpumW9z47Z7yXRlHNBt7Wj961Wn7lQsew_FQ7RonQxu0x2esc_P6T5wMIHO57GgjOxK30SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/679471" target="_blank">📅 19:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679469">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
بانک ملی ایران؛ همراه آغاز زندگی‌های تازه
🔹
بانک ملی ایران در چهار ماه نخست سال ۱۴۰۵، بیش از ۸ هزار میلیارد تومان تسهیلات قرض‌الحسنه ازدواج در قالب ۲۵ هزار و ۶۸۴ فقره وام پرداخت کرده است؛ یعنی به‌طور میانگین روزانه ۲۱۴ وام ازدواج.
🔹
این میزان پرداخت، نسبت به مدت مشابه سال گذشته بیش از دو برابر رشد داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/679469" target="_blank">📅 19:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679467">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای ونس: ایران گفته عوارضی دریافت نخواهد کرد  معاون رئیس‌جمهور آمریکا، درباره ایران:
🔹
در میانه بازی با ایران هستیم؛ هنوز به پایان نرسیده‌ایم؛ واشنگتن از ابزارهای دیپلماتیک، اقتصادی و نظامی استفاده می‌کند و هنوز تا رسیدن به نتیجه نهایی فاصله دارد.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/679467" target="_blank">📅 18:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679466">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRzkpmCG0CLPMhKOcetuLOegP8FhlxKHUM37rhIkWcw8QkXUb1oXAjJQFYgdHSwBt2yAPoxlHwIeynxk5Dp4brF2OPFH_Mryu0msR4sSztGeweLM55CLSuGgRRTji4ZrAqBldV9kTVfusFwOUSw5QXJ3eew5GrJ7xgyUYpJwpBuCRrPAdEQVisMsd73X0roBbZdLKNr9b9DTvvU0ZB3itPDMbJoHFSJwgRY8rUmQkYrV0vGADHrzkSDRActJEbmPbnaGhKxS-PfwGf4N_R7rYQAPCRR_I13KD967ts7PukEad6BxlNPM6uLgrLwm_dwoJzS9-ETas8eAh4iz1VVQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۵
اشتباه رایج در پخت کیک
🍰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/679466" target="_blank">📅 18:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679465">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
نگاهداری، رییس مرکز پژوهش‌های مجلس: در مقطع تاریخی حساس فعلی، نباید رویکردهای ملی را با نگاه سیاسی و جناحی ببینیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/679465" target="_blank">📅 18:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679464">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MloSzdB5priYWWnr9kpNC893dAI8WGXD_w5qq9RS4PGTCHCg6m4bXX6iSgR_8mcSW0vVKNbDkQ0seiSOfVlL-2JcRpzLdGIP2Uk7CC_E4M6xOynvfRLCaNizCmU7dNZPAArKIe2Axikhen6utE8MpZmT5Do6VZ9MjyGS0oTugZgnSB2CFj3nMWFwmEzqGUks6WIlTjs0kMtm_AKlFMbxLeWwF0utDKoErkfJh_IeMhJ2Y1-__fGBjYtZFdHvPvEFz0xL9qL4w0AkkWMlgmTvLWbh7hdsr2PbMOgtCk-vUFfH0oRczK0Ro2RY7ISkPKj4IDCkQK-CdCAiphMaZ23uRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشترین جنگل‌زدایی را داشته‌اند؟
🔸
بر اساس آمار سازمان غذا و کشاورزی ملل متحد (FAO)، طی یک دهه اخیر حدود ۴۱.۱ میلیون هکتار از جنگل‌های جهان تخریب شده‌اند.
🔸
در این میان، برزیل با تخریب بیش از ۲.۹ میلیون هکتار، بیشترین سهم را در نابودی جنگل‌ها داشته و کشورهایی نظیر آنگولا، تانزانیا و میانمار در رتبه‌های بعدی قرار دارند.
🔸
توسعه غیراصولی کشاورزی، قطع غیرقانونی درختان و تغییرات اقلیمی، از دلایل اصلی سرعت گرفتن روند جنگل‌زدایی در این مناطق است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/679464" target="_blank">📅 18:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای ونس: ایران به ما اطلاع داده است که اجازه می‌دهد نفت با حداکثر ظرفیت از تنگه هرمز جریان یابد، اما تا زمانی که این موضوع ثابت نشود، به آن اعتماد نمی‌کنیم
🔹
ایرانی‌ها می‌خواهند این وضعیت را تمام کنند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/679462" target="_blank">📅 18:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcIV2DDvHaep4Q3IFzi_TUrMa7y6FLc-B33sso8_RjtwUHmIfRzyfuSVvPhVVVXQp84SHIA06y9ga3tkbjEfeM3dYTDq564qUu6Mp4L2Qk3jVI83l9DHuTQk57yQ2JG1HROmc1nCeJ_ki7RCiEc10Jn361oYTJTmJP9cUW52N5P2p2xnvbr_yonji2vynk4VRxZh4OWKkahO6CqiY_H6bS1MMfDc8noQEhhS-TjhdWRwcESDxJyQl-GkI5H5HqGWzMAr5hE8SmPgRS5uwNg0dVrlEIT3Y2Os5LfLPYkUNtBBs1Xfqn9l81g27cVQBDvQ-J6lrZkorKSQoWtoXr5Qzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهرمانی که با یک تیر، مرز ایران را جاودانه کرد؛ آرش کمانگیر
🔹
آرش کمانگیر تنها یک تیرانداز نبود؛ او نماد فداکاری، شجاعت و عشق به میهن بود. در روایت‌های کهن، آرش تمام توان و جان خود را در تیری گذاشت تا مرز ایران را مشخص کند؛ تیری که از دل کوه رها شد و نام…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/679461" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCw5bqf2WDW8vPJHbOQ1ec2jvtukndhD0M3As3vKZ82efBhU-630SMaeD-4r7If9HHBHdLe58GFcpHy07zIa22sdCkzTgh3NvDIIJ3keiuIEv4JynO8Z_fos1breY4IczVdfTqU808xpVUNHAdlyTQNISSruzH2soZDNy0qmBlbXBAfExsg5cpKvykyWvhS6PeSfj5KZl0zsEnwnoALaYp2U-pJ9PhwWwftmSiVeE6yI7wf1WkDPcEyd9F8fp4ZJGUI_iBW8Jqr-MKCojV7zJPy7aRlFMEqbOo-BFp6idEypfUFdKcBIy0cICzSEszsaZ1DH92_jmEXw3UDvscJKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۱
🔹
پیشی گرفتن رشد سپرده‌های بانک کشاورزی از شبکه بانکی / ورود به باشگاه هزار همتی‌ها
🔻
روند افزایش سپرده‌های بانک کشاورزی در دوره پنج ساله منتهی به پایان تیرماه ۱۴۰۵ برای نخستین بار میانگین رشد کل سپرده‌ها در شبکه بانکی را پشت سر گذاشت و با ۴۵۰ درصد افزایش به مرز هزار همت رسید.
🔻
حجم سپرده‌های این بانک از پایان تیرماه ۱۴۰۰ تا پایان اسفندماه ۱۴۰۴ بیش از چهار و نیم برابر شده و با رشد حدود ۳۵۰ درصدی از سطح ۱۷۹ هزار میلیارد تومان به ۸۰۶ هزار میلیارد تومان رسیده است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/679460" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA8Z9aHy7MxXpMU1KqAFOyYbYHwFVN7lCUccmwxcY1io2rK_uS5WqlWHFDui-5KrwujtbC4Gkw4HTnKjXq6Xi7AefrbYCD0LBdhj2vsQ5H5KmJoaLb6yY-4WeKdfxOdgJG236gDOHACwSO46KejnMY_REOoMZsf-EDWvnfoozzTjcN7yGyXWGRIQHYGuPW_f-rwO2yzaUQ-G88Btd3MVJCh8r6CqlE58MsC8cGW1t-2t-jd9Ut9fDgOb53q_mgNtsSdQHLvxQN7I5WMqXpVIl1KYqBB0ny1twAKsL3vuvYsybcCwXAG1q7sqvLOBHuE1v0hUBKW81rGtHeR07_hggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ متهم قتل حمیدرضا رجب‌زاده دستگیر شدند
🔹
پس از اعلام ربایش و قتل «حمیدرضا رجب‌زاده» تحقیقات قضائی و انتظامی برای شناسایی عاملان قتل او آغاز شد.
🔹
پس از ارائه اطلاعات جزئی از سوی خانواده وی درباره آخرین برنامه رجب‌زاده و مسیری که قرار بود طی کند، پیگیری‌های…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/679459" target="_blank">📅 18:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679457">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
قتل یک مداح پس از ۱۵ روز بی‌خبری از او
🔹
حمیدرضا رجب‌زاده حدود ۱۵ روز پیش ناپدید شد. خانوادۀ او آن زمان در کربلا بودند و پس از بازگشت به کشور پیگیرش شدند.
🔹
مسئول هیئتی که رجب‌زاده در آن مداحی می‌کرد: ۲ روز پیش ویدیویی از پیکر آسیب‌دیدۀ حمیدرضا در شبکه‌های…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/679457" target="_blank">📅 18:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679456">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای ونس: ایران به ما اطلاع داده است که اجازه می‌دهد نفت با حداکثر ظرفیت از تنگه هرمز جریان یابد، اما تا زمانی که این موضوع ثابت نشود، به آن اعتماد نمی‌کنیم
🔹
ایرانی‌ها می‌خواهند این وضعیت را تمام کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/679456" target="_blank">📅 18:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b36d3061b.mp4?token=qvmafQy2UEiAPrCgXJQsONGYIEwQb3Kj5qMmbtid1CkixMSk88WezIgiesGtC-PG0S2rz59vl8Vlt2nqXge4A_mNlFBuXjiJooILznW78C85DWVPXdBAAZoF4FXw6EaYszNmNGPAiHzWTp9ERX7aSvE4IhSnT4NlGK7RoXSdp922ybREy5VrCWVzJo-FIDDVgiV2_2h6ubbu6X-RpVvEwqIxRio9qZZCb2Xms3DvPcYBzi-GSEhYVumy1k-58CwUD3yI8B2sSa47Fb_CB9TDLrbIR79faSBpiJVNfIGGAdZ1wqk2mgbV7-X-zAB3D7dGz4n71PqGuV7CbPs19lIScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b36d3061b.mp4?token=qvmafQy2UEiAPrCgXJQsONGYIEwQb3Kj5qMmbtid1CkixMSk88WezIgiesGtC-PG0S2rz59vl8Vlt2nqXge4A_mNlFBuXjiJooILznW78C85DWVPXdBAAZoF4FXw6EaYszNmNGPAiHzWTp9ERX7aSvE4IhSnT4NlGK7RoXSdp922ybREy5VrCWVzJo-FIDDVgiV2_2h6ubbu6X-RpVvEwqIxRio9qZZCb2Xms3DvPcYBzi-GSEhYVumy1k-58CwUD3yI8B2sSa47Fb_CB9TDLrbIR79faSBpiJVNfIGGAdZ1wqk2mgbV7-X-zAB3D7dGz4n71PqGuV7CbPs19lIScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این آقا پسر سوت پلاستیکی رو قورت داده، بعد بردنش دکتر
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/679453" target="_blank">📅 17:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمرکز اطلاع رسانی بانک صنعت و معدن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16f26c9352.mp4?token=H1kP-IRf0SrblIaW91Zpa8R0H3BqLp4rW9JbarRzEsdI_Aly12mgdPRFrontNSROVAUObOOG9IC4ovll5xRLldzs7WraxlJdsKqCQdoz3t40Ww9p9_Pk4sjLFRFCU1mxWZBCAy_NFSj0qy0WWlsxa-6ybeI11QwLevjUEbfpJL67RpuRgcywg1u175O6zkNCkrr_omgL3A5mSnEOCmiGFbnD2Emgsn7lW0VqJMdkuL-KleT3_tsgxAAc5fVGoNDpA3wdkw1owDpL3YHalqH57JQaT_-m0yol4wGeAi9akl3QpYct_9qVwU2u3_BdMRG6vAEWM2cX7D-hgq-1TQ8Ing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16f26c9352.mp4?token=H1kP-IRf0SrblIaW91Zpa8R0H3BqLp4rW9JbarRzEsdI_Aly12mgdPRFrontNSROVAUObOOG9IC4ovll5xRLldzs7WraxlJdsKqCQdoz3t40Ww9p9_Pk4sjLFRFCU1mxWZBCAy_NFSj0qy0WWlsxa-6ybeI11QwLevjUEbfpJL67RpuRgcywg1u175O6zkNCkrr_omgL3A5mSnEOCmiGFbnD2Emgsn7lW0VqJMdkuL-KleT3_tsgxAAc5fVGoNDpA3wdkw1owDpL3YHalqH57JQaT_-m0yol4wGeAi9akl3QpYct_9qVwU2u3_BdMRG6vAEWM2cX7D-hgq-1TQ8Ing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✍🏻
توسعه تنها در کارخانه‌ها، معادن و پروژه‌های عمرانی شکل نمی‌گیرد؛ بخشی از آن، در روایت مسئولانه واقعیت، تبیین دستاوردها و انعکاس تلاش کسانی رقم می‌خورد که برای پیشرفت این سرزمین گام برمی‌دارند.
خبرنگاران، با تعهد به حقیقت، دقت در اطلاع‌رسانی و مسئولیت‌پذیری حرفه‌ای، پلی میان رویدادها و افکار عمومی می‌سازند. روایت آنان، فراتر از انتقال خبر، زمینه‌ساز شکل‌گیری اعتماد، افزایش آگاهی و همراهی جامعه با مسیر توسعه است.
بانک صنعت و معدن، به‌عنوان بانکی توسعه‌ای، نقش رسانه را در بازتاب ظرفیت‌های تولید، صنعت، معدن و سرمایه‌گذاری کشور ارزشمند می‌داند و باور دارد که توسعه، زمانی ماندگار خواهد شد که با نگاهی حرفه‌ای، دقیق و صادقانه روایت شود.
با سپاس از تمامی خبرنگاران و فعالان رسانه‌ای که با قلم، اندیشه و مسئولیت‌پذیری، روایتگر حقیقت و همراه مسیر توسعه‌ی ایران هستند.
روز خبرنگار گرامی باد
سایت
|
بله
|
تلگرام
|
اینستاگرام</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/679452" target="_blank">📅 17:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679450">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
۵ تا ۱۰ هزار کشنده وارداتی پشت مرز ترکیه بلاتکلیف ماندند
عضو کمیسیون عمران مجلس:
🔹
حدود ۵ تا ۱۰ هزار کشنده با مجوز کلی دولت قبل برای نوسازی ناوگان وارد شده‌اند، اما به‌دلیل نداشتن ثبت سفارش در مرز ترکیه متوقف و در آستانه مصادره هستند.
🔹
وی خواستار تصمیم فوری دولت برای ترخیص این خودروها شد./ تجارت‌نیوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/679450" target="_blank">📅 17:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679449">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls_TJVeRyIXWfLL660zh3RusNTxCfgYu1_W0f9wRiJfaCPLCCQB2rNhNButZqiYllOX3I0J-B79BMghO5vU5SHvkrIneddPjqrA1YAjLOvBTvzcLYduFpzhEHSykd39bg1zb2hbu0PjxY7NPb_dLp_2iJmO2erugqwyPSkdkmnsv5B0G6CoWre_l5t288OAMnWdD3ki4ciGH78fH60muHt_5bQ6F7l1xuCKz8y3wZWPM8NAHeV5ZlgALtqgd6YuUGyhiATPACgp6JC48yzb4aG8d26ADEVOCU7x7WbHoOzNyYUHDPWqh8btleKNkXYmEhpwXSnRBCYGaDWMNbxwb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعلام کشته شدن رئیس ستاد مشترک مزدوران سعودی در مأرب یمن
🔹
وزارت دفاع دولت مزدور و سرسپرده عدن از کشته شدن صغیر بن عزیز رئیس ستاد مشترک مزدوران سعودی در حملات موشکی دقیق اخیر نیروهای مسلح یمن به اردوگاه مزدوران خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/679449" target="_blank">📅 17:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679448">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0cc564f9.mp4?token=gDTCVOwnKoly03m5fMmzKseuuPsh06CIeD2xsG4zaoELbgJSuR980hXZwDKzFWQpBbPIN-pBPyiXhIYRtA_8K3BoGBulAfv4kC7PNm7kStvYfTfSq96jSxDyraxhdl3ALzhyALi9Mn2QjNsAomQKJmoGfGdGkyyTBn-u05f4c04LxGIsn7-Y1QfvEywlRTpHLhBdcDed3emqQAw9BCM_55093hREfYd0MqDck2Ajo74Bsm3kZldI4twuVywr45hNFSpvbQZPysvU83GcZf7_b2aaBs8TbphyLOb94Jdqkx-un2v8aFcd7y4P17AoKedYElH3_xkSQ9lr9MF84C0eqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0cc564f9.mp4?token=gDTCVOwnKoly03m5fMmzKseuuPsh06CIeD2xsG4zaoELbgJSuR980hXZwDKzFWQpBbPIN-pBPyiXhIYRtA_8K3BoGBulAfv4kC7PNm7kStvYfTfSq96jSxDyraxhdl3ALzhyALi9Mn2QjNsAomQKJmoGfGdGkyyTBn-u05f4c04LxGIsn7-Y1QfvEywlRTpHLhBdcDed3emqQAw9BCM_55093hREfYd0MqDck2Ajo74Bsm3kZldI4twuVywr45hNFSpvbQZPysvU83GcZf7_b2aaBs8TbphyLOb94Jdqkx-un2v8aFcd7y4P17AoKedYElH3_xkSQ9lr9MF84C0eqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین سخت جراحی با بادکنک
🔹
جراح با دقتی بالا، بادکنک را بدون ترکاندن بخیه می‌زند؛ تمرینی برای تقویت مهارت‌های ظریف جراحی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/679448" target="_blank">📅 17:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679447">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
سرنوشت تجمعات شبانه بعد از ماه صفر چیست؟
قائم مقام سازمان تبلیغات:
🔹
ادعای تعطیلی تجمعات بعد از ماه صفر صحت ندارد؛ همه ساعت‌مان را با ولی‌فقیه تنظیم‌ کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/679447" target="_blank">📅 17:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679446">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Asy0_ymxvMkFfzpDNrIKKgi73OHSBc_f5Lky5ow_jgzdWQqR38zhgFCSw_6azxS62ZSMDx7yNwQ1sBQwLTShL42_zTHBzLE2_uXcdRQh_Yit5tvPEhTNd9E2ZwEC59jDIdKZ282bMbLU85eKB3MIbjQAQPyrgkDy6uwTyNnzLd_Mm1PJqvernGH9lAE3eHHz4xNWsnZaxogiweD76YC4V7cSXo7st_PIqcUWU9ASWek2e09-lXx_x4SO3VdRBDXsnt-VGv7T3JKi_CDELvscfg-xOyE2_N3rP1iHX--KaYgNyArHxog9ZYlXOMrQM9HJ2sNit0XaH41VYP87cr0BMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: تا آمریکا رفتارش را تصحیح نکند، تنگه هرمز باز نخواهد شد
🔹
شورای عالی امنیت ملی هرگز کوتاه نخواهد آمد؛ چه در جنگ و چه در مذاکره.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/679446" target="_blank">📅 17:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679444">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ju1i9J7w5DEe49eT8D2i9IQA-U50JXL5J3bdOqrKvOoGvcQukvdnOBjkPQJRY5Eru5-4Uf694fZsr_6t5ea43DvmkhLrrdnbaMsyAodiH-YX5m871a7VOncnCIP0aM3OSmwR8BDj3jzebGzjuMKUxVPOT17kSWbbEjfAvULLSj8Qe4cEeprb7z0CaMaBgZV9namIAsCVdTXkSRkPsofqBh08Odd9GgpRnww7buQV0OtUemDN1Ku5fs_s0qsicdMf8ZB95SPvmEBGbiMg6CGJs0gMscgUVR6GgZfOaMrPXrTFakqa40L2AEB8RoT7EEQJkpYtornapxu5MtOQas9sHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عامل افزایش قبوض برخی مشترکان، عبور از الگوی مصرف در تابستان است/ افزایش تعرفه نداشتیم
🔸
مدیرکل دفتر مدیریت انرژی و برنامه‌ریزی امور مشتریان شرکت توانیر با تشریح دلایل افزایش محسوس قبض برق برخی مشترکان در روزهای اخیر اعلام کرد: در شرایط عادی، برای مشترکانی که الگوی مصرف را رعایت کرده‌اند، افزایش نرخ برق نسبت به سال گذشته افزایش محسوسی نداشته و آنچه موجب افزایش چشمگیر مبلغ قبض شده، عبور از الگوی مصرف است.
🔗
‌
مشروح خبر
🆔
@tavanironline
🆔️
@tvedc</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/679444" target="_blank">📅 17:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679443">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNeG3EWKBSUjSy7mpz9c_C5ul-XjA1WMrj0SrvaE8AVFgqJfs1Td8RetUDmGZPlX7dkxdzKT1zL5GN8v3SXhc0-PrT3iHoVnzvPpoJkExTFnK85DxrkWEkodRlvcFaOhhi_qOP9O2fOlzdJcQnuTEbINddBufwVz4DGorJD5azgLlhhcGDaRVwDHEyKlf9eZ-i5LKGLfmRy1s1hvDOtIRUZDm9WsMcNkqV3e4M3vr4tvu8tDpAuALzVufz6FDFB6Xx4y5PbkNyGpmFi-BXofT3P-FDLTjTgH5byCy89OGcf-4hIMpC6RtJOvQyYE4JTTHsemFq0Qdbh1N1qf0pgj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از قتل «حمیدرضا رجب‌زاده» چه می‌دانیم؟
🔹
جست‌وجو در میان پست‌های منتشرشده در توییتر نشان می‌دهد، حداقل از روز ۸ مرداد اکانت‌هایی مربوط به جریان هوادار رضا پهلوی و سلطنت‌طلبان، از انجام قتل یک مداح خبر داده و از مقتول نام برده بودند. ماجرا چیست؟
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3236375</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/679443" target="_blank">📅 16:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679441">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toP8epTuIvmxp_41KkOLcFji2nD6BuoLhZxSDOP0ZsoMUOkYkJIeLKCYOI3JqHugOqhXrGMunuavTYl05pbNqfXO_xAxrcDuY8Fomy89sraF8ss5rZ_c2LAyRzvC06ZaP115IXdkoMZ4t4kQME1NGqdIGFRGb6cr1fst2D_dst1NIOkztNVbRL2_jcTlS9LTzRy5-YC0-nWmlYyLp9-qrPbxR2nH0_weJC_ugrpQ7Z5jMjTq_l9qYpi3qgz72AgKFL4YGOmhzglBxX1-Ox68AV-Vq3hC7GkS2B3rMBPmGmEFD702Bk6xsCg9b6H_300OnoxhP5_XBCm5i5HpUmdv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به یک کشتی در سواحل عمان
سازمان عملیات تجارت دریایی انگلیس:
🔹
یک کشتی در ۱۸ مایلی خصب عمان هدف یک پرتابه قرار گرفته و این حمله باعث آتش‌سوزی در داخل کشتی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/679441" target="_blank">📅 16:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679440">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7815beadc2.mp4?token=n7L5OOu81nkytbxBki6kB_UMMl017YqxVqyGYlkiLnN3HQrIPM7TyPCM18bGnW3nlJGpoZ7qHbSX0PcJkO1Ohhcd7U-wQmXoqfQTeNp5tCZPL-5UFvAt74FjVfm4AhZxgyK77mVhei8zHrI8Rptvh4o9-k2NPN3cK7fZoiKX87qV04sywGiYHRk5fN-pnTzmmayUkIdpS9xxVYzY_5L9aFImahjzHEXyqQ7hQUbLsWU1ygqoH05ZBJ4Ap-qXNGGWvT9kPR-0k2PXnZVrTinDB3bTi7L2pSDIBJFZnLGbbACuAjJNOM64lP9JSIREdNb-4Z62_Xo1kLpaoO9yERSNFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7815beadc2.mp4?token=n7L5OOu81nkytbxBki6kB_UMMl017YqxVqyGYlkiLnN3HQrIPM7TyPCM18bGnW3nlJGpoZ7qHbSX0PcJkO1Ohhcd7U-wQmXoqfQTeNp5tCZPL-5UFvAt74FjVfm4AhZxgyK77mVhei8zHrI8Rptvh4o9-k2NPN3cK7fZoiKX87qV04sywGiYHRk5fN-pnTzmmayUkIdpS9xxVYzY_5L9aFImahjzHEXyqQ7hQUbLsWU1ygqoH05ZBJ4Ap-qXNGGWvT9kPR-0k2PXnZVrTinDB3bTi7L2pSDIBJFZnLGbbACuAjJNOM64lP9JSIREdNb-4Z62_Xo1kLpaoO9yERSNFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور بعضی از خرید‌های ساده به‌جای این که پولدار نشون‌مون بده، تبدیل به یک سقوط مالی میشه؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/679440" target="_blank">📅 16:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679438">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تصاویری از عرشۀ کشتی متخلف که توسط نیروی دریایی سپاه پاسداران متوقف شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/679438" target="_blank">📅 16:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679437">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
پزشکیان: نمی‌شود شعار بدهیم که می‌جنگیم، اما فردا در بازار همه‌چیز هم باشد و گرانی هم نباشد
🔹
ما با این پیمانی که بسته بودیم و توافقی که انجام شده بود، قرار بود تحریم‌ها را بردارند و بخشی از آنها را برداشتند.
🔹
اما صهیونیست‌ها هم نمی‌خواهند کشور ما آرام باشد، وحدت داشته باشد و انسجام داشته باشد.
🔹
از سوی دیگر نمی‌شود شعار بدهیم که می‌جنگیم، اما فردا در بازار همه‌چیز هم باشد و گرانی هم نباشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/679437" target="_blank">📅 16:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679436">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/956bb4711e.mp4?token=akrBWN4vYoAXF6_uQZ5-B7T4IIGVgObh3lNCJMR_eAJZcdFoQ4t78HUfRvCLtrwWku0sG1yaUrdGfvpiablx39g5P-OcUOvRkVV65cVOd6VAhPd-JjrLsfjlQVlQIgxRLwKL5rGngjJQ1v1oF-jnpQOZMEHQs8mW90m0f34IO45r5e27VtE9YCgmbwbrxkyt9ZDUk0uS_CznK7si9xof0sPCGs2Q2DYrZAhNx_Pi4lNuenmb_Zz24M_hrxtk_ReQwmzgk6OAnPiysXzBGg1s6tnHoSY0ni38ttHtBMCFenKVdkC82za6QkGdMFu9oTSNkSFiNGThQ_Gn9cUV8UxReg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/956bb4711e.mp4?token=akrBWN4vYoAXF6_uQZ5-B7T4IIGVgObh3lNCJMR_eAJZcdFoQ4t78HUfRvCLtrwWku0sG1yaUrdGfvpiablx39g5P-OcUOvRkVV65cVOd6VAhPd-JjrLsfjlQVlQIgxRLwKL5rGngjJQ1v1oF-jnpQOZMEHQs8mW90m0f34IO45r5e27VtE9YCgmbwbrxkyt9ZDUk0uS_CznK7si9xof0sPCGs2Q2DYrZAhNx_Pi4lNuenmb_Zz24M_hrxtk_ReQwmzgk6OAnPiysXzBGg1s6tnHoSY0ni38ttHtBMCFenKVdkC82za6QkGdMFu9oTSNkSFiNGThQ_Gn9cUV8UxReg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان بولتون: پوتین احساس می‌کند ترامپ در جنگ با ایران ضعیف و ترسیده شده است،روسیه آماده حمله به ناتو است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/679436" target="_blank">📅 16:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679433">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
پزشکیان: رهبری هر تصمیمی بگیرد، ما تا آخر ایستاده‌ایم
رئیس‌جمهور:
🔹
تصمیم درباره جنگ با فرماندهان و رهبری است و دولت وظیفه تأمین تدارکات را دارد.
🔹
هر تصمیمی ایشان بگیرد، ما تا آخر ایستاده‌ایم و از جنگیدن و ماندن نمی‌ترسیم و تا پای جان ایستاده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/679433" target="_blank">📅 16:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679432">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
اعلام کشته شدن رئیس ستاد مشترک مزدوران سعودی در مأرب یمن
🔹
وزارت دفاع دولت مزدور و سرسپرده عدن از کشته شدن صغیر بن عزیز رئیس ستاد مشترک مزدوران سعودی در حملات موشکی دقیق اخیر نیروهای مسلح یمن به اردوگاه مزدوران خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/679432" target="_blank">📅 16:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679430">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پزشکیان درباره آینده قیمت بنزین: هرگونه تصمیم مهم اقتصادی و اصلاحی باید با اطلاع‌رسانی و همراهی مردم انجام شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/679430" target="_blank">📅 16:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679429">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
جهانگیر: خرازی به دادگاه ویژه روحانیت احضار شد  سخنگوی قوه قضائیه:
🔹
با توجه به روحانی‌بودن باقر خرازی، پرونده او در صلاحیت دادگاه ویژه روحانیت است و اقدامات قانونی برای تعقیب کیفری وی آغاز شده است.
🔹
خرازی امروز به این دادگاه احضار شده و جزئیات پرونده پس…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/679429" target="_blank">📅 16:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679428">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پزشکیان: ما تصمیم گرفتیم اینترنت باز شود/ دستگاه‌های امنیتی تهدیداتی را در این رابطه ملاحظه می‌کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/679428" target="_blank">📅 16:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679427">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
پزشکیان: راه ما را بسته‌اند. ما کالا را ارزان می‌آوردیم و از مسیرهای راحت وارد می‌کردیم، اما اکنون باید مسیرهای مختلف را طی کنیم و از راه‌های گوناگون کالا را وارد کشور کنیم و به این سادگی نمی‌توان این کالاها را وارد کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/679427" target="_blank">📅 15:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679426">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
پزشکیان: راه ما را بسته‌اند. ما کالا را ارزان می‌آوردیم و از مسیرهای راحت وارد می‌کردیم، اما اکنون باید مسیرهای مختلف را طی کنیم و از راه‌های گوناگون کالا را وارد کشور کنیم و به این سادگی نمی‌توان این کالاها را وارد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/679426" target="_blank">📅 15:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679424">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5yXy82pbnajFBRD5q95fhh9sWJcusHBboFMueo1G_Zarjq6jaJCx7qrRMYZmpcqncyoSNnNdHUlbda3wvDLxmRlbYGZgI-4M2li4gzCVadWbWj21hXbaPnCuSygHv6M7gK-mnJMH5a2wz1Xa8rnw0uV7de2yJ5TqGmNzx3TjmsWLvUts8GAcm_ClhINpE3IA5ZN8uG-pHFjaDYTakblvIkerdIihqAlp8JrcgQS-QgaEJiYT1xK-T1JeRF-1loHVDvyfg4B7S9QDLmxyxHlnRg2JFaGsFklUZdt3888sTtthTs3_7jPxgEO0vVtZ5gP0mdm9R9zmyXCnWNmgZ2djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم بودجه نظامی جهان از GDP
اوکراین با تخصیص ۴۰ درصد از تولید ناخالص داخلی خود به بودجه نظامی، در صدر رده‌بندی جهانی قرار دارد و پس از آن الجزائر با حدود ۹ درصد و رژیم صهیونیستی با حدود ۸ درصد در رتبه‌های بعدی ایستاده‌اند.
ایران نیز با تخصیص ۲.۱ درصد از GDP به بودجه نظامی، سهمی مشابه اسپانیا دارد و پایین‌تر از کشورهایی چون بریتانیا، آلمان و هند  قرار گرفته است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/679424" target="_blank">📅 15:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679423">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/679423" target="_blank">📅 15:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679422">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5L2wjPhxi-zS5fQpid6o9PkeW98HFTMJ0ogAA5jM7UYMVT_YIRTy8zGSk20A7yXDhln9lzQU45x7XiBl3BTqRyFo1S4ROTmWZRxsg4d789B0-N6yP9dNoyKFhwYTA0hFNgLFFl5Bv_iSZnPDAIdph-vSPX4tGRKDw9vQ09vTTf2wfsN3onbSRzW89qeNGJC_GcNqx4X2KpvyMb5NpkK36L5zWnDRG1k0DOWaV4WXAZ-4JnJHSqjxsk1vbPhsQLXLAFVk-hdydDrmKvQUWkqvZWBfwf3SsvuIeG8u0FmMkxEh8I4ARvHDSABFu3ejWQEnTeXkAf5-NNLpIJI-IBr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای الگوی عملیاتی شب رسانه‌های زرد علیه بانک مرکزی
🔹
صیانت از مرجعیت و ثبات نهاد بانک مرکزی، خط قرمز نظام پولی و اعتباری کشور است. هرگونه هجمه به ارکان این نهاد نه صرفاً نقد عملکردی، بلکه تلاش برای مخدوش‌سازی اعتماد عمومی و اختلال در ثبات اقتصادی تلقی می‌شود.
🔹
جریان‌سازی‌های اخیر در برخی رسانه‌های زرد، از یک الگوی تکراری و مهندسی‌شده پیروی می‌کند. تکنیک اصلی این جریان، مهندسی اخبار و جعل پیوندهای غیرواقعی با هدف وارونه‌نمایی عملکرد نهاد بانک مرکزی و گمراهی افکار عمومی است.
🔹
تحلیل تاکتیک‌های به‌کاررفته در این گزارش‌ها، هویت ذینفعان این عملیات را برای رسانه ها کاملاً شفاف ساخته است.
🔹
بانک مرکزی جمهوری اسلامی ایران، فارغ از حاشیه‌سازی‌های هدفمند، بر تداوم مأموریت‌های استراتژیک خود متمرکز است. استراتژی این نهاد در مواجهه با این‌گونه عملیات‌های روانی، بی‌اعتنایی به حواشی زرد و تمرکز بر دستاوردهای عملیاتی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/679422" target="_blank">📅 15:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ماهنشان؛ جایی که کوه‌ها رنگی‌اند و لک‌لک‌ها بر فراز قلعه‌ها زندگی می‌کنند
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/679420" target="_blank">📅 15:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679419">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPwkY_gv_oOBugN55srksGZ7SALg3ozigCPhAjQxrFuLmiUOD4cayjRpNcmwPVGZCW7t_9_lrk4wiA76EkNZNmg2FkLHqu1cVb6sauoBaJW9gNyIzvQ5lY1AUi0vjrse9CnybheFMz0UBRUo0USQVQAuMiPZyiw0PngH0N6ULbo78WfBmZDhWkYW6l0iN396WI1oGiHsZNOZ_gGm8hNzDdLErbNqmyRlTNn1Bhc-n_Y3MdoO68u70-BdGIgqBKmkMPHrT2R6dCMDOQBKljTS-qm1dNDwrwP-fQrRcPLXVejV0N14VaI67XbHA_txJJaa7v7ogdcffR4_wrVj8kIZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایه‌های نامرئی در آسمان تنگه هرمز | ترامپ سری تازه اسرار یوفوها را منتشر کرد | چرا همه پرونده‌ها در زمان مذاکرات با ایران منتشر می‌شود؟
🔹
انتشار پنجمین مرحله از اسناد طبقه‌بندی‌شده دولت ایالات متحده درباره «پدیده‌های هوایی ناشناس»، بار دیگر توجه افکار عمومی و محافل امنیتی جهان را به معمای حل‌نشده اشیای پرنده ناشناس جلب کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3236311</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/679419" target="_blank">📅 15:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679417">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896ee6a0a0.mp4?token=e10AKv2NUqexs5EB-RTi5O_-iYtbGZSEl-gEwTEaerXJ0XT2sy6hv53D13w4wAQRVfYP_H7gXYezNCSY7ERe_Iu-qkpe75JlXuZE4I4Yt69MnJAzYgDOrPXAMn88StCZ4KFg4Zfgb5sBBm1Eu3jL7nJ9lazTQa74WDtGqXWiFaEmpiYpFAnupt_JKgaiPCb1eRty56sS9q6fzyPkgxu_Qmb18_N8G6ML92xUSlF-GuNNVVBEZKtdkntemO1asNopzOyT6nHwCEGbeSkXkoJ3rqUJGOV5gU8258KX-JNiaZUr_z93SgJn_sVj4g3vNhS4FLl7JR3-hfC0V1enL3DBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896ee6a0a0.mp4?token=e10AKv2NUqexs5EB-RTi5O_-iYtbGZSEl-gEwTEaerXJ0XT2sy6hv53D13w4wAQRVfYP_H7gXYezNCSY7ERe_Iu-qkpe75JlXuZE4I4Yt69MnJAzYgDOrPXAMn88StCZ4KFg4Zfgb5sBBm1Eu3jL7nJ9lazTQa74WDtGqXWiFaEmpiYpFAnupt_JKgaiPCb1eRty56sS9q6fzyPkgxu_Qmb18_N8G6ML92xUSlF-GuNNVVBEZKtdkntemO1asNopzOyT6nHwCEGbeSkXkoJ3rqUJGOV5gU8258KX-JNiaZUr_z93SgJn_sVj4g3vNhS4FLl7JR3-hfC0V1enL3DBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف زلنسکی: موشک‌های آمریکا به پایان رسیده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/679417" target="_blank">📅 15:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679416">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1797f66576.mp4?token=jEJ9NVY_h-uJwStMRypXS9ZrKIhERs4l5gBlV5XTg2ULjOl_7SyS3UCMuZXt_c9dYBOWaevh7NSExOAMlCGteCGIUksvC7Q7cQcsuEW4XlTHWLyY6KakgPMyrjo6FZvtbzQLRKet6XPUUoSQqGg-xkLaxz3YHOkD1a4o2HKmjJVUL4GD6ShzTLwykV9HBS9ox4MmOP5NyfLZOaO_tAzRNFQ8tlRGefkQzkTj3CTVzoL99hJ_5q115q2hgfi9VAdvyL3sOjJu7OTSfreE_FxRK94UkDHa0LvCTU7j_UoB8e7XnyH5hHGVPhgTLJ5w2QqudBe-p9r-RtcvuAttKKst2W6CGVX0kaU0g2ixud81Mo4Q0ap6LsJh3UvzTLHKiRsEEpbgoZaYg1aa6hNSgBxy7btbl04gp7p5Lo0K3pbKyI3tCbkVfTqnzfRLujJ7z81bEOIP0UeaB_1ylTcu1rOlug0zCX9gphKi-RLdSbcMou5moZaWcVqfNfuJcojwMfWnSr_bSbXv_PBja-OXVw-A73O-xaxx4FpGcN0rp7d6Mswvou2eqOssVWF6dY0eClRdHFlidg-qYFMa_3SbEQfV3HIT2fm36yf-uqIJvrbW4_yEjF0MrboWx79W0392MzmSHQXFUBqtpKfg1QtG4eS2JEQpxifI1YWM7E6S7Cp2mxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1797f66576.mp4?token=jEJ9NVY_h-uJwStMRypXS9ZrKIhERs4l5gBlV5XTg2ULjOl_7SyS3UCMuZXt_c9dYBOWaevh7NSExOAMlCGteCGIUksvC7Q7cQcsuEW4XlTHWLyY6KakgPMyrjo6FZvtbzQLRKet6XPUUoSQqGg-xkLaxz3YHOkD1a4o2HKmjJVUL4GD6ShzTLwykV9HBS9ox4MmOP5NyfLZOaO_tAzRNFQ8tlRGefkQzkTj3CTVzoL99hJ_5q115q2hgfi9VAdvyL3sOjJu7OTSfreE_FxRK94UkDHa0LvCTU7j_UoB8e7XnyH5hHGVPhgTLJ5w2QqudBe-p9r-RtcvuAttKKst2W6CGVX0kaU0g2ixud81Mo4Q0ap6LsJh3UvzTLHKiRsEEpbgoZaYg1aa6hNSgBxy7btbl04gp7p5Lo0K3pbKyI3tCbkVfTqnzfRLujJ7z81bEOIP0UeaB_1ylTcu1rOlug0zCX9gphKi-RLdSbcMou5moZaWcVqfNfuJcojwMfWnSr_bSbXv_PBja-OXVw-A73O-xaxx4FpGcN0rp7d6Mswvou2eqOssVWF6dY0eClRdHFlidg-qYFMa_3SbEQfV3HIT2fm36yf-uqIJvrbW4_yEjF0MrboWx79W0392MzmSHQXFUBqtpKfg1QtG4eS2JEQpxifI1YWM7E6S7Cp2mxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
عملیات ویژه آغاز شد
✨
وقتی یک دختر کنجکاو تصمیم می‌گیرد از خانه خودش شروع کند، یک مأموریت بزرگ شکل می‌گیرد؛ مأموریتی برای حفظ برق پایدار، کمک به خانواده و همراهی با همسایه‌ها.
💙
⚡
این فقط یک انیمیشن نیست؛ داستانی از مسئولیت‌پذیری، همدلی و نقش هر کدام از ما در مدیریت مصرف انرژی است.
🌍
💡
🆔️
@tehran_roshan
#تهران_روشن</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/679416" target="_blank">📅 15:08 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
