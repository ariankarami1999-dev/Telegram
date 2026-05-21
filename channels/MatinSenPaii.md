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
<img src="https://cdn1.telesco.pe/file/YLuACXfpLfvLAJ7WVJjmanb6C0prLYZNY1i2JDOGNn96w8d7Xj9ud8Ll0fNaD7E69XKw8qsrKl0d6pS_39YO7340qSwaUd8CJrqBrjVWsAes9jgAkbVc6Jf51-5AVRHkoA_GNrFiJtrwuqsBzvgsGsVuA1xU6GhJ7lEoBmuqj30ISOV40GDGrI4osoutTvuoHNoMhaWzWWSBRzEnR5lAiX_sV31SJCHaU7PecLFFSEUhMJE7sPlQtSfWZWH9wem_bvn5uyvqpfYAAyP40MRqzL4G7UjU1CfrRz1GZlA4w_MQztyFOoHsPI6cvhGE_mBaj37122jAMVELTEufQsi6GA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 143K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 01:43:23</div>
<hr>

<div class="tg-post" id="msg-3288">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qlXSTBNvHcUYOzfQGmpRKDp4Nj8AWqRtEZLuHaCixVnXoz8BAU3pVsyZftjW1KOhoNNjkFVMNUw6abRf3KyPiyieAoEhmpNiNJAplk0Xm-W2-H5fVqnftJIoOVe0PinZvstvIwto2WsdAKb2E3UQv2oDke_MNFPf3xmOxwrjDLJS45gOyLZUpXpXh4VOR0FxBOywNp1E_t47gbE5d2c9wbB652C-GnXb-eEmDFHelXlZyAhHBu-Xn1PnxjssN3JhoGjo70_IyF2vEaQHDh5Y2Lp5EE18Qq-Lk4bHTYQtplFkbv-hGqXi3Xqnjk3dfMGuw256qGBTv0yFOLpjZ2Rvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنین بود، افسانه‌ی شیر و خورشید
🫠</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/3288" target="_blank">📅 23:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3287">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2RKbgGYAOEeVFdbW5ZOz5Mt4OulkUeMCKIiuWDbOgFAeSlWW2r6VVxNWPS5eDufPVOBU5_lnAujvNUsCiT6JbK8BQ2vRy_R5F_45qR0nhS5ZCgOOXvvVPYPAJHmpIk-6CFRPAUq8Z1o9V46SsCpikRtXB5G9fKVzydiHZe0Rng2Q11er2fxusHx1zEbIKMLyAc6UPbHmVvMexGovEXL2WUBhXvGO9_UCBzYU3bVZkD_-KQvecEv_W6uCxjf5JTpbWOOMiV4RMcvvGwRvW0jX8SRHX4plrCM7qJ183L0GLfUu5Bu0t6KmJ1FbWOKqCBHst0GJjiiKiqtW3THTEXUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/3287" target="_blank">📅 22:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3286">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نکته‌ی مهم راجب سرورهای StormDNS و MasterDNS که روی WhiteDNS استفاده می‌کنیم:
هر سرور و پورت 53، فقط ظرفیت 255 کانکشن رو داره و دامنه برای تعداد بالاتر باید لودبالانس(توزیع بار) بشه.
خلاصه اینکه اگر با سرورهای رایگان سرعت نسبتا پایینی رو تجربه می‌کنید، به خاطر تعداد بالای کانکشن روی اون سرور هستش. اگر سرور شخصی خودتون رو راه‌اندازی کنید(که آموزشش رو ضبط می‌کنم واستون) به هیچ وجه سرعت پایینی نخواهید داشت</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3286" target="_blank">📅 19:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3285">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیاز داشتم روی هاست X ایرانی که اسمشو نمی‌برم یه سرویس بخرم
می‌گه دامنه می‌خواد
رفتم دامنه گرفتم
میگه فقط دامنه .ir قبوله
حالا رفتم از خودش دامنه گرفتم
میگه احراز هویت سطح 3 نداری توی ایرنیک
رفتم ایرنیک میگه سامانه هدا نصب کن داخلش احراز کن
سامانه هدا نصب کردم عکس قیافه الان منو با عکس ۱۵ سالگیم که روی کارت ملیم هست می‌خواد تطبیق بده و نمیتونه
میرم میبینم نوشته شماره پشتیبانی ۱۵۱۰ هست. حالا هرچی زنگ میزنیم هیچکس جواب نمیده
و دیدم هرچی دامین داشتم هم پریده نمیتونم تمدید کنم با اینکه پولشو ازم گرفتن
رسما دیوونه خونست</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/3285" target="_blank">📅 19:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3284">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ورژن جدید WhiteDNS Desktop واقعا خفنه. الانم با سرور رایگان وصلم هر سؤالی هم دارید توی کانال تیم جواب داده شده: @WhiteDNS</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3284" target="_blank">📅 16:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3282">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dZ2Ehde-TdmOyjDY6veRa6TtGxRIu0llq_9Mgv4f4UmDW7t4BIorJVijR5X1ywUMiuM8MWvsY9rsRPtZuNluOQGqhmWvu1zrcBNrJxYMzTp0HJinKqzWheTyp2VP1s_oBh-WKBO7fijjv8fkWtg-5UNmsOCF8EY7xYRj1xZkbloX4Eox0RRLqBqMNDu1Yq9I2ID2MagQn-7owAkIlHN0FAAuafYhIc2Ng9wpUjiLzLyoBl6jJp3y70Zfl3K_n-JxLwoF5aPjAFn5zPytojlRiotZ7J7ivKHrLOTW5MPqtocGkyh5UeQ8PdlkpORDhv6Er4EcJwYzm7P8G_a8Kys-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tYKs8DhrK2TdT-WZ5bShpxlJswl3rlIsTa1kuC3OdLYz55M8wkkTaUzAETRGNHYfcJUPzD2j00Ik6uFu3piwnOmGJZtDEscij-Y8PdtH5nYUeabbQoLsgk36AThIo0RCCrQA0OR1Bs0WtUUjw7NYggnsAlQ-F-J9NfI1E-kuZE-i5GoTAwG3rZXiSG3r4A0h5fCvpwYHgiCvkmKlu7AhPAkQv_M-X9v5LeBeLQ1g-syF0RxQH659uK4sxTLmzrSw88yTAPUY2g5I-qkmMBqEWpo3jbR7YcImVfSu6g1PjxP0q6oD9Em-kT0v6OF86KQ_c9d6yR6YWDq64W9wDhQZew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن جدید WhiteDNS Desktop واقعا خفنه. الانم با سرور رایگان وصلم
هر سؤالی هم دارید توی کانال تیم جواب داده شده:
@WhiteDNS</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3282" target="_blank">📅 16:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3281">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگر رایتل دارید و کسب کار ندارید با این حال اس ام اس پرو اومده جدی نگیریدش چون اول ازتون پول میگیرن، بسته فعال میشه و بعد از دوروز بسته قطع میشه با این بهانه که شما صاحب کسب و کار نیستید و پیامک اشتباهی اومده.
پولتونم برنمیگردونن.
این عین دیالوگی بود که با کارمند رایتل داشتم
✍️
شیوان</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3281" target="_blank">📅 16:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3280">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NO73q44TvT5N8JqGm_hZbfGVem92YMWtp2X-S3iDH70lFOmzQ8FwL7siGadAQbhsxgsCf8ixPxDxh01FNt2Zhh_p3NcnfKe7GCk0eoIBL8gJ5KAlkanrZEkO0Q58Hm8I8EriYrWT9_p76_9FwX5VwuFnBr8T2MIJ2yl1WdSNL7JioDXMhHAOdLauRCWEvfHXDKwC3XPB0V7t6sSLMP2AMzgMY-hyuIDPm6uJlPpuL6a0gGXLBJT64g91OtUqyWPTIQuKMsNlmb0Z4_iWbRUIoLPBi-3xIrMtWRyr80MY94sEwV_OPod968Xz1swUPpMeJVUdtblbrajlkL42-nvGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنل‌های این چنینی هم دنبال گرفتن ویو هستن و مدام در حال نشر دادن اطلاعات غلطن. به حرفشون توجه نکنید.
الکی برگشته میگه حتما قبل از اتصال به یه اپلیکیشن IP های اپ رو چک کنید
😂
انگار مردم متخصص شبکه‌ان بشینن Wireshark بزنن پکت‌های شبکه رو رصد کنن. جمع کنید مسخره بازیهاتون رو
"از ابزارهای معتبر استفاده کنید"
چشم الان میرم اینترنت پرو میخرم جناب</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3280" target="_blank">📅 15:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NrGscy63a_qhF_AiFA5Hr_A8Fmw3pF-zPjGyiFFmKM7p11Gz3iiDVjJOAjdnGxEaqL_9oCKn3K7YhLLw23ijyHzXl7W4ZZha9cYKjrUSZ_H9PCsKuW0QUNK-qeE5wEQTEr843903KJTW10JVt9LPWkazpmTxCYsib6pCt3MWO6K0nwjXLYn6HB81X-VUZZe0FNJVVeoM8YpxkAjiEwP-ozxOrYhOqDeQtU4-mlBmShG-06IHnNqmR8YqPUXQiLH2iK9sqwLyEAtTriBUYUqAKWeNmaXuglwH-vYhkLy0aD67MZmCKUSgaGK5QFbV2Aodhy_gtzgkqYjEx64ZBYHlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها پروپاگاندای حکومته طبیعتا. یه مدتی هم ریخته بودن میگفتن SNI Spoofing امن نیست یه مدت هم میگفتن Npv امن نیست و...
کلا ما از این چیزا زیاد دیدیم. توجه نکنید.
اگر به من اعتماد دارید، حرف من رو گوش کنید و با خیال راحت استفاده کنید.</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3279" target="_blank">📅 15:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hWKD6Gk3bBc2CyP3wsPLlYh9cqvhOSqqdXFaUNvcpoUqN6V5FcEP6dd7MK3Ajducd0MdsqTX6SfN1R0oIg6hcDVuh2OxFtIHknuQuzeTt8TSPYvH9Wqxb8Es3BsCW171QUpj17RjffxKtL69Otxcf6Nwv0ojrRtQM5lV_oe9u4v0QZbUq6cVc_t8FZkFAw4PC0_xROlKnrrmziozxJRIDGt4MY2OmgYXO-bvUjSY7agyEyqWV5MYL9zBEH_Vjp_7q_gnJcTueVoospbRb20rujeW1qGJj_FM9NrEmEIrCCBN5RzXbyroRRM2cT2Hcym6ntkK3uSOCRkFS6ad36mylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیر و خورشید توسط یکی از افراد مورد اعتماد بنده نوشته شده و کدهاش هم به صورت متن‌باز، روی گیتهاب هست و میتونید برید مطالعه کنید:
https://github.com/shirokhorshid/shirokhorshid-android
این اپ هیچ چیز ناامنی نداره و یه فورک از سایفون هستش. اگر این اپ ناامن باشه، طبیعتا یعنی سایفون ناامنه. که خب درست نیست</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3278" target="_blank">📅 15:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fOm0qRapNAvWPymnQ6oLWHPkOdZGfn5GQAwfrafI-N89bxztG-IexBBkcRBKZ24svJpZ2t8d-p3hngGjYStYuaW6c1PpEvrrVVs1fGRfkrbJkBIL2ozgutosCWlfD1jb6QuCF-hCfikPWQlknzyP8hdYj-_wqF1NS7hlRhV5R0LtlsBTkUv5-kF5NCBVdFF2ABZtlP6qYI93JWqr0I1XXN9vQJJcFK9HcQPxaIfkDjlx4zrvT7JI14BDY0fF6naTVsGVCKus2ZkZhmyegZw1HbmnDyqtIFanWaDHVXUtG1Hpik72xXZUbOY4vHBfN0moCaeND4IcpFU53LhBylXFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتباطات زیرساخت و سیستم DPI تمام ترافیک شما رو رصد میکنه. در این مقیاس شما نمیتونی بدون رانت و پارتی سروری پیدا کنی که بشه این حجم ترافیک از روش رد کرد. متد خاصی هم پیدا کنی، درجا میفهمن سرورتو به یک طریقی وصل کردی به خارج. کلا تانل زدن و سرور خریدن رو از سرتون بیرون کنید و با WhiteDNS و MHR و Goose و Skirk و مابقی متدهای رایگان وصل بشید. به محض اینکه بشه تانل زد یا روش کم هزینه‌ای پیدا بشه من بهتون آموزش میدم</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3277" target="_blank">📅 14:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3276">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اکثر وی‌پی‌ان فروش‌هایی که شما می‌بینید عمده میخرن به عنوان واسطه و مجدد به شما میفروشن. خودشون کاره‌ای نیستن. منظور من کسایی بودش که مستقیم سرورشون رو وایت می‌کنن از بالا و ترابایت ترابایت ترافیک رد می‌کنن</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3276" target="_blank">📅 14:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">Matin SenPai
pinned «
متدهایی که در حال حاضر متصل هستن:  برای وقتی که گوگل وصله:  متد دانلود از یوتوب و رفع تحریم سرویس‌های گوگل پارت 1: https://t.me/MatinSenPaii/3151 پارت 2:  https://t.me/MatinSenPaii/3230   MHR-CFW: https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG  MHRV-RUST:…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3275" target="_blank">📅 13:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3274">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3274" target="_blank">📅 13:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3271">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZLO30vj3IsTxNc1sjQfrg217ZKm72CGzCsB5fppEHis6XfA-WnJ6Z0pnvJCd-u6JDKo2zKfEMNAXb1a7Tk_wcy2KvsxVEJJUWKyE9T_zsBnL_gDziLS5yHsLc98Cu-l4tdtkcOVndEHijD_htZ72RbYGPxijsfjxchKGlzaBzjDAjixs0Z4EyW5JfgW58RmJEa6uB_ODnzOEaY7oNzSBkBMXH5IYbgBxD-kg4gB2WQV4GTtlNA-JKNUgrjN81cDL6vavKq5mCUjDqaaGxmXr20FDO8wnUWo83uRXVZq3-MKGQg8XbX61tKBIMFHKNqyxe4zQTZSKcoC-U_PJ-6XFtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J3jVAzTc0vSBGGTTz1otul5OJ2I-NyHF_FA12lCYednwZwwqGl8aPOs1UHOQe4zmDIMUaEk4kLGgX01i9Hszzar4PmyTG_sIUtxcIDqxTnX25yMAjOzxNC32vZK_jFYlU2UT4ZBP30pULcjZpBE12mMetgI-2_Wz3o_AuoQNWHPdjTWdzxaOSxdg5Vxlyw9hPxg4oVJ1SRHEvQ0QJcKg2V6XEuhtaANuBItxk-KIg5o2NSnVsvddgOx_5yK4OaAtDJt6fVdI6DqwwUYGYBnBx3moZsNKKcG7nKeTqazkETGK5VWewx8Jz34Af-226TkuhvWbk7mMcQLBXXZW8Wjj-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M6qD0xdTmxNjK2XcrVGgkQtfHfaWz1Uet0fkSnbFPdRLfjCm9HCDHqZWV8q5DOz5aije7dQNkQdV7w5ybaHRg-OC4D6gpxWlaxZxcMmdEXgl1bf0rXAeoT7awK7QlELPZDbIHmgI2C80EXhrpGHBkAEsFv-sqnpONyhAcQ5f8VaUeIq5CiMQ4xtC-L3_q6f7VrCVfb5EDnQD4SUsGVcXbaq0pmMkq90HYPuAdnswrFs1ug6f4cYEqyeLdN0crFi081EuEb8-Fmwji2hJHXTLQKV82xXnsIvOmXnV_r3POL8B60g8Lb8dO2soCBTIVK-488eEdecNhCTn4AOWHjmuzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان mitivpn این SNI Spoofing رو توی ده دقیقه از کار انداخت که VPN خودش رو بفروشه. کارشو تموم کنید
🔴</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/3271" target="_blank">📅 12:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3270">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن. دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه، تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
✍️
آمینواسید</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3270" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3269">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ighe1tuS8TJPwSWS7lafq1xHrxOzk4FMMJi8camhmHaQFH4VtB1xdlElGTmHG9U8X9ikqLQMqJi_eVXUoO7JgYUU__OBwpQ2D8uSWUFuT4seKT1nEsdM4w2-0i_1DirkMRzTB1hKMr7FnxMp2HcyzxXc49NOoQbUlsIvpdJgDyuhMC_znbf3v3AWSSOeNqNwu9ldTH1uMAAguqEsJoD52mvY0y2TZIVvKRHq6P08c7xUnIwFEAvB4O3EV67-GLW8iw14iYe28llKD32jOfcTvRw3w2hzlrwd-NbixQ717o5vLsx98PaToKP9569PX9vQjHUvaSs44z9d3d3VRWTqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر خرافات راجب شیر و خورشید شکل گرفت این یک هفته که فکر کنم کم کم یه فرقه‌ی جدید راه بیفته.
عزیزان تنها نکته‌ی مهم، اینه که چندتا از آیپی‌های CDN رو بذارید، و انقدر بزنید هواپیما و بردارید که روی Range شما باز بشه و بتونید متصل بشید به اپ.
اگر هم وصل میشه در حال حاضر، به هیچ وجه گوشی رو ری‌استارت نکنید یا حالت هواپیما نزنید</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3269" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3268">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YNyrphcvVsGNbfDm3HwEjCJnlmhTLgSiKOBhhN3-LVVhWoBnDCfWY6RqjiG9VWRh1Wi_czkwbE9dewkVWbwlfDmvuYaMx007MGkk2TWEuD__qQa4-LGunLiOLL-w9_EIstXQw5Eip9K2kYPTkm-Cr13ZkDCAL90MVMZQHtQAH5nwMEy0sqfE_trdQ0njG_rSjpwnjmFggfx9JagjO2H1Q-ksValj56NtUKF8iWWe2CFY2QY18NNghoTa4_fD0PDWDGsrfa0UQaqiHKMxSS1C5PQfvRo6vrSwqyWzjyzE2tElrWEFm9YbMSOYxzRDI44jLXzfJYjN70EoDVoUMnwwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت Spoof</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/3268" target="_blank">📅 12:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3267">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">☠️
آموزش ساخت متد MHR با گوشی + کاهش مصرف ریکوئست های گوگل
⚡️
لینک‌های داخلی جهت دانلود: https://t.me/MatinSenPaii/2969  لینک پروژه اصلی: https://github.com/therealaleph/MasterHttpRelayVPN-RUST
⭐️
توی این ویدئو بهتون یاد میدم که چطوری متد MHR رو صفر تا صد…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3267" target="_blank">📅 11:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3266">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یک سری از گروه‌های ارسال کانفیگ و کمک و اینهایی که از سرتاسر تلگرام دیدم و خب نمیدونم مال کی هستن اکثرا، می‌ذارم خدمتتون توی پست بعد</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3266" target="_blank">📅 11:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3265">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک سری از گروه‌های ارسال کانفیگ و کمک و اینهایی که از سرتاسر تلگرام دیدم و خب نمیدونم مال کی هستن اکثرا، می‌ذارم خدمتتون توی پست بعد</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/MatinSenPaii/3265" target="_blank">📅 10:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3264">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فقط چون علی جان تهدید کرد</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3264" target="_blank">📅 09:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3263">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWlta0zI2xT0ogvLTVBj2pw3dA6tegZpu0xLiGMJ0KiAVd3GSXitYmvhoC29t_a2389PZUdYGlkaF_FcRgvAso157JOwmJjCgjDSmL6jf61_PpX1eeMv_fE8gPOtbGevFXUFECmW-jbCqbZ4PoQ9ffkB4j7f2mTUp-74aurXLhBPZ6NkLJv7XMkfMa9QFRLA0dU0Oz5BP9MkZcsS8EBr0mOZTZpCp0Ta3mEtaIgR-oLmLf7lKXNI01w56qQ-UHLA3_NymGsxkFpzhTXsRSx_iVj7xqfQ_jYDciImsYW4dJ_ukKDxXFbG8EgoZctCwV1UqE0X4g75XpcnEXR3HnXEOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کانال من نیست عزیزان من هم تبلیغش نمیکنم و تلگرام خودش اینها رو می‌ذاره. خواهش میکنم اسکم نشید</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/3263" target="_blank">📅 09:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3262">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f0b6810cc.mp4?token=DGU6SRK1OYA_Y91_eY34fIf1SbF-xaurfWhm869bL5XIoLMwAt67TQUw48CbaqVEZbjHRMtWGzfpyKfny9sXcVKzA572qHCTzjrI2iWVS4fKS5dxnCVAxj-WzIFxPRdx8c4l2P9XRkwYYrkt1kDIb0CbEClFDjcJYW8GyT4f1ScjkwnKEpmXcD7pymHpS4EGnrt0lwrU3Nbb9S7tPKw2FNLGnv-GfR89DAbwDIyDFyZLXugB-DOjsONyOd2y6OrhO4fKiaqifMDsflD6FGWJj2KWXKPAvs41ymyDKRtVmVieGkEyQGsjVHxa6vXrOP9GuI6c8OMSmG-qKqLf_70ZSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f0b6810cc.mp4?token=DGU6SRK1OYA_Y91_eY34fIf1SbF-xaurfWhm869bL5XIoLMwAt67TQUw48CbaqVEZbjHRMtWGzfpyKfny9sXcVKzA572qHCTzjrI2iWVS4fKS5dxnCVAxj-WzIFxPRdx8c4l2P9XRkwYYrkt1kDIb0CbEClFDjcJYW8GyT4f1ScjkwnKEpmXcD7pymHpS4EGnrt0lwrU3Nbb9S7tPKw2FNLGnv-GfR89DAbwDIyDFyZLXugB-DOjsONyOd2y6OrhO4fKiaqifMDsflD6FGWJj2KWXKPAvs41ymyDKRtVmVieGkEyQGsjVHxa6vXrOP9GuI6c8OMSmG-qKqLf_70ZSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط چون علی جان تهدید کرد</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/3262" target="_blank">📅 09:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3261">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SaYgxab4OSfJ6OrIUCzv0Ho6zi__ZLbJYXKBc6XFtXnAeiHJuVq2iCTkw5mnhuOAyaF2fSAoyztrdGIaA5Ls-WvHTCifgy9PJbTXCoYaw_B3SX67ogJPuRR2lj4Fj8T24QBZI6auuDioqlXp6sniK8RTbsaDbThT7ILwdDUJtRuK82Wmp54zc1tfDxKyV8Wt92TZ0SwsbpIeWZChNYlINXXpzmxDU1yX7s_6Gd_-y3IQskM2mKJqoVZAdIN75KKq5v1qDVtjCwzCiTiDQbSmCECSojhJPS2-53q5EW6Ai0gelc8AljqZyWVz2c1Veizt128DRBoMoBZcTuYIL25trA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3261" target="_blank">📅 09:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبر بد اینکه hcaptcha.com رو بستن کلا.  خبر خوب اینکه مشخص شد متد هنوز در بسیاری از isp ها بسته نشده و صرفا کلودفلرو کلا قطعش میکنن یا میبرن پشت reverse-proxy.</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3259" target="_blank">📅 08:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">خبر بد اینکه
hcaptcha.com
رو بستن کلا.
خبر خوب اینکه مشخص شد متد هنوز در بسیاری از isp ها بسته نشده و صرفا کلودفلرو کلا قطعش میکنن یا میبرن پشت reverse-proxy.</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3258" target="_blank">📅 08:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">متدهایی که در حال حاضر متصل هستن:
برای وقتی که گوگل وصله:
متد دانلود از یوتوب و رفع تحریم سرویس‌های گوگل پارت 1:
https://t.me/MatinSenPaii/3151
پارت 2:
https://t.me/MatinSenPaii/3230
MHR-CFW:
https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG
MHRV-RUST:
https://youtu.be/7YdJIJloIxY?si=WJgiFKDcCmISyDdB
شیر و خورشید همچنان وصلن با آیپی‌ها:
https://t.me/MatinSenPaii/3247
متد اسکریک که شبیه به گوگل درایوه اما اون نیست:
https://t.me/ShahabSL/9223
برای وقتی گوگل هم قطعه:
WhiteDNS(برپایه MasterDNS و Storm):
https://t.me/MatinSenPaii/3130?single
کلا دیگه سمت dnstt و اسلیپ نرید مقابل Master و Storm به شدت اذیت میکنن سر ریزالور</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/3257" target="_blank">📅 07:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vwfumSryeuto3E_r58eCb-0uELSGc4cXRt6gSht_uQV2nKAnBbcRyWBPJM-jJC0gLpqwIyhR47YIiEJvm2Oz53pfchetAFCpjJe-JqP8Atjf3h3cfCDcndzXHIJ2OKNcoTtzgl2gR9MXvfhYXSa9eJ1coayJPRHuOU6wL6VTgv-yHem9ZAACDx5wN-dOKohtmRbvkeHE1pKFFu48QJswBH3UtxYXKBEFCLgnFGdaJs_l5XPTmZrAmPJzYEKcc7kWOp0i5I4jzia_HI1PnnMpiwdSgBV021JrMagJvk0sIuFwlDdUqllWGKnyRT7oPwv38bQY3RXBsx1RBgnvEIbPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه از شوخی گذشت
😑</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3256" target="_blank">📅 07:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">و اینکه دوستم عزیزی ران‌تایم‌های برنامه‌نویسی مثل پایتون و راست و گولنگ و  تمام نسخه‌های ادیتور VScode و Notepad++ رو گذاشته اینجا برای هر سیستم عاملی:
https://dlhub.465978.ir.cdn.ir</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3255" target="_blank">📅 00:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">☠️
دانلود از یوتوب و Torrent با اینترنت ملی، به صورت نامحدود!(پارت2)  توجه: ابتدا باید قسمت اول این ویدئو(https://t.me/MatinSenPaii/3151) رو دیده باشید.  لینک داخلی: به زودی قرار میگیرد
⚡️
لینک پروژه عزیزی: https://github.com/TheGreatAzizi/AzuDL-GC2GD (با استار…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3254" target="_blank">📅 00:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3253">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">و اینکه اگر Spoof واستون وصله و نتتون اوکیه، حتما متدهای جایگزین رو ستاپ کنید واسه‌ی خودتون. از جمله:  برای وقتی گوگل وصله:   MHR-CFW: https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG  MHRV-RUST: https://youtu.be/7YdJIJloIxY?si=WJgiFKDcCmISyDdB  برای وقتی…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3253" target="_blank">📅 00:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb36e0d0.mp4?token=VBLhXVLrIUDpyCZtnHol4Vph06q0WocEe1ISVkpoaHizejadlu7fbURcKZtf1A-9pScKKSqhkFHS9SI7YMtKalVUtle5KQSXkWfQH28-M3CLJ1YP1ZXRIMn_MyNTvDnJX_Gt_6MuO4OyUf4f_72gzgdSDFxsKhSRrz-ojR247_Ip69oym9-HBIbY3EZdIPThQXWeoQ35bC4GfKHOS062w-MGTlETb7Jhuv8d93VD96PailL8cVVgs7kP3GAXZL1Kj3W7RZmY5fQbXRejON6Z7vzHlH6vvffsACrhL7OHjRq7rpijHf932fwCzpxQgUpNxispS8kGg7w_S_ktrnt6Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb36e0d0.mp4?token=VBLhXVLrIUDpyCZtnHol4Vph06q0WocEe1ISVkpoaHizejadlu7fbURcKZtf1A-9pScKKSqhkFHS9SI7YMtKalVUtle5KQSXkWfQH28-M3CLJ1YP1ZXRIMn_MyNTvDnJX_Gt_6MuO4OyUf4f_72gzgdSDFxsKhSRrz-ojR247_Ip69oym9-HBIbY3EZdIPThQXWeoQ35bC4GfKHOS062w-MGTlETb7Jhuv8d93VD96PailL8cVVgs7kP3GAXZL1Kj3W7RZmY5fQbXRejON6Z7vzHlH6vvffsACrhL7OHjRq7rpijHf932fwCzpxQgUpNxispS8kGg7w_S_ktrnt6Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3252" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p1hdX8wAO_unCTsdwzyyAoVLObSMBo7VDvAynNO60q_OJYz97N3hQ9SluvY9CiPOKoRUvowo8_Dh7UcwYLwhf63jy3lWfYDimHa-Bvw7F9zA4faOEXJwUZEg6daZFCf9oV-okXG9rwJK-PcRSZBun5XABklBTPDwxRwcDsKNeWMIWZGJx9c0UmchczoYTgomCpfpH1bcUOx4CY35uNZY1KOGD6mcdczpvc8OBkk4FnxmkhK0xT46cRVt5hZiFf1gQwTmnupxljhqhH80mhcuAdN4hdBkxtIaSnjDf-1Xfx73MKrtQogJ1PlaeushgOlYYvLjuEHnkciqAeWSJP0P2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدود کردن دسترسی اینترنت به اپلیکیشن‌های خاص بر روی ویندوز
این زخم رو من وقتی خوردم که با کانفیگ گیگی ۷۰۰ تومن اوایل جنگ ویندوزم تصمیم گرفت خودش رو آپدیت کنه و من وقتی فهمیدم که خیلی دیر شده بود:))
از طریق اپلیکیشن TunnelX، می‌تونید انتخاب کنید که به چه مسیرهایی روی ویندوزتون اینترنت بدید
با پشتیبانی از:
- WireGuard
- V2Ray / Xray
- OpenVPN
- l2tp
- SOCKS / HTTP Proxy
از اینجا می‌تونید این نرم‌افزار متن‌باز رو دانلود کنید:
https://github.com/MaxiFan/TunnelX/releases/latest
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3251" target="_blank">📅 23:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">و اینکه اگر Spoof واستون وصله و نتتون اوکیه، حتما متدهای جایگزین رو ستاپ کنید واسه‌ی خودتون. از جمله:
برای وقتی گوگل وصله:
MHR-CFW:
https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG
MHRV-RUST:
https://youtu.be/7YdJIJloIxY?si=WJgiFKDcCmISyDdB
برای وقتی گوگل هم قطعه:
WhiteDNS:
https://t.me/MatinSenPaii/3130?single
theFeed:
https://t.me/MatinSenPaii/3109</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3250" target="_blank">📅 21:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">این متد ناامن نیست دوستان، بلکه امنیتش کاملاً کنترل‌شده و لوکاله. شاید توضیحات من باعث شده که فکر کنید ناامنه، و نگرانی شما از کلمه‌ی «MITM» منطقیه، چون خب MITM حمله‌ایه که هکر وسط ارتباط می‌شینه و ترافیک رو می‌خونه و یا تغییر می‌ده. اما اینجا MITM داخل دستگاه خود ما و با سرتیفیکیت خود شما انجام می‌شه، نه توسط شخص ثالث.</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3249" target="_blank">📅 21:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/heEL11A9uPD_7ZwXP5ubDm7y885chWVo9JpgcqgwgKYcICzqdEOs38fOfx0vPvaINcMFpqCESpRv2qr-viXT33rntzh-KmQghF8oGs1xw3bOa4VlWduBiPMHQHR85ZIy1OrqdEMfekL2NLfULEWtfySrHG-PMaNBcSUmQubEZuPCE_hOnxwHcc4iKnDMi4Nl7MERCMwsPvQHBELxalSPTv9scwPO2bhqKLPpDtgt7FfjyDK7NAaG5l84JxFEOlEIFWsbaMZzNzlC6Nyc8L9EeQYqQHEPNwd0oZPnMpGo4BT5OVnVHxwL7q0wlkriMmBNS7Z_fQSB7prOZEDdPm8V3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">kharabam
:
[موقت]
شیروخورشید یا سایفون MahsaNG برید Connection Protocol رو بذارید رو Direct یا Normal تست کنید ببینید براتون وصل میشه یا نه.</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3248" target="_blank">📅 19:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یکی از دوستان فرستادن، برای شیر و خورشید بخش edge ip:
2.23.168.7
2.23.168.47
2.23.168.96
2.23.168.144
2.23.168.174
2.23.168.213
2.23.168.254
2.23.170.80
5.160.13.85
5.160.128.142
31.214.169.244
37.191.76.110
37.191.95.70
37.255.133.30
46.32.31.30
63.141.252.203
65.109.34.234
78.39.234.140
78.157.41.60
80.191.243.226
81.12.72.218
81.91.145.2
94.130.13.19
109.72.197.1
142.54.178.211
178.252.128.66
185.109.61.27
185.137.25.214
185.141.106.238
185.208.175.228
185.255.91.60</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3247" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3245">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03524e951f.mp4?token=epAQqdKUgazEBBmdTtTFpail7DPMaj-sWZTBusq7Q3rtega8fDqxj01yreeTXaoipA-cpU-v9NqpG7fvHxiSFck9Mb1FzW9r0UzpnioXx984JVqOsp_vuZ49QI14DpXqGGD-UJCeraArXhnDK_vP1bCabHy_NruLhz8Lg8lFZrihRdIIKaKcHXRm-5o_TSeuUce78zclRns1X64W-zwrFomwKBL-4Z1A_QoOeS9MpIFqcYGjWm6MTKV8K1fj9U6b5Yc8BdUh9z2A3tBnjV3hF-aaWRN8BghjYbE8SnoQgCoB3yoifrQs_9aaMU3wvxI5MlL-nXuM79K72qKkNIsL9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03524e951f.mp4?token=epAQqdKUgazEBBmdTtTFpail7DPMaj-sWZTBusq7Q3rtega8fDqxj01yreeTXaoipA-cpU-v9NqpG7fvHxiSFck9Mb1FzW9r0UzpnioXx984JVqOsp_vuZ49QI14DpXqGGD-UJCeraArXhnDK_vP1bCabHy_NruLhz8Lg8lFZrihRdIIKaKcHXRm-5o_TSeuUce78zclRns1X64W-zwrFomwKBL-4Z1A_QoOeS9MpIFqcYGjWm6MTKV8K1fj9U6b5Yc8BdUh9z2A3tBnjV3hF-aaWRN8BghjYbE8SnoQgCoB3yoifrQs_9aaMU3wvxI5MlL-nXuM79K72qKkNIsL9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون مقدار sni که دادم آموزشش برای شما که چطور وارد کنید
✅
(مقدار sni hostname کاملا متفاوته با ip)
نکته:ip حتما باید پیدا کنید hostname فقط واسه افزایش سرعت و پایداری هست
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/MatinSenPaii/3245" target="_blank">📅 19:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3241">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">31.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3241" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ویژه گوشی‌های 2020 به بالا</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3241" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3240">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromali</strong></div>
<div class="tg-text">شیر و خورشید هر ایپی اسکن میکردم نمیشد واقعا هر کاری میکردم وصل نمیشد
ولی نمیدونم چجوری از network checker ایپی اسکن کردم ۷ تا در اومد کار کرد واقعا</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3240" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3238">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g02inFxjVcK05Xpym-FidFMeAC6VpjVZP-jCM4nG8cRoASCXt6OpxM_Glm96sr4fE_5RCe2MJPFT4dXIwdtbosVCt4QLCdG7n38A0Fvkt5rkLabqThkQk8Tt_Smbtl67b-6sA4Chz1_jmP5FKtIrRIoS-Bv6dmKW_xn0NO7tFt3rHmF7ci4y7qPPaJZwxBWz4VfnGiytVwOw2y3eOzzhCicdaTDjtqCg202CghV3EIOgzXoxegE4DAy0UrmZzJ1RzLiQ6tSurEjHf-e3C86-YJKcapavsQLKKvBYQFjin4G2zmfZltTeEYKbm4jCyx9gkaK0RSqSVd_Qs2Pp1m_CYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GwTzMnEFNrqFR6Xo31HIZt2QBofZFKFiN2dNUvtG3kPc8m5xjjAXAVQ-UmsGSrSgoPSX3LsTTeweImyGJRbcZfrBP7Btb8hUyZZnM87ZX0Di-JVbmolkGYgjn0Rax5Ho3I4kIJJOL4vYoJ-r28E9SeCt3FeuecdfF5WSX1zoWrtwcGnFe_-jCtKwdInlscfpURuJ77g7zciFpNpP6Yropbv5UXGRMsdIkjacR6YhOChjdsMc6J8iGrwxTqzXK7f9eXJts4up219gl11FBTyRmdThzCr-jan1w9k8tzSnPljcxytLQSqWD8nlS3xIcQ0blLEWJua-EsO4bO6WK--aRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👑
داخل اپلیکیشن شیر و خورشید با sni های زیر که ir هستند میتونید متصل شید و شرایط نت رو بهینه تر کنید:  snapp.ir  varzesh3.com  digikala.com  telewebion.com  bmi.ir  aparat.com  لیست بروز میشه
✅
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3238" target="_blank">📅 19:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3237">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-text">👑
داخل اپلیکیشن شیر و خورشید با sni های زیر که ir هستند میتونید متصل شید و شرایط نت رو بهینه تر کنید:
snapp.ir
varzesh3.com
digikala.com
telewebion.com
bmi.ir
aparat.com
لیست بروز میشه
✅
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3237" target="_blank">📅 19:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3236">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mx3L6eR5OSEQW9pzq8HybZBnpPig0XXbhONXYDx2Y7I5LXgST4o5i_DU1B4PwsWaPwBJZlMBhV6bAa1CK2uFgz0Rly8TmMoGG_KwdQ_FwxKdQ-JH0jxjAxOjRpUEG-A37Lh5O5mF1BLd8kOJjqc0wv9gfcmLvl_2gaxwp2UE5CcgX5TJWjVY-3AvYpsAhhA030Kz1k_-WI-dqLPzytXyL6p0MdJum1TVRA_GX2S0HNat0-8OxnsnXztm6Os8ij6cEKmJLM8adyCwVPGy6E6YcAg7qEUfnOivFcKIVh0Qwvp4RWd9xMC14gfOzVlt2_YmISpQGE8hrahLcD6m92o08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان من هیچکسی رو توی تلگرامم معرفی نکردم و این کانال‌ها خودشون پول میدن به تلگرام تبلیغ میذارن زیر کانال من توی توییتر هم اینجوری میان میگن
😭
😭
😭</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3236" target="_blank">📅 19:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3235">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3235" target="_blank">📅 19:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3234">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I1y0rHQOiSD_yKgrisNLSy9jYzY5-jNUUtGpKM9CWcU6JYCuBbMTcKGYAJtZ-Fr-iTMoVsGkvxQLNHkISVSBbiZynJzcarOTsgiv57dPJE97JFU58JJx6Hs_saMK3cFEAkEJ3ozrFKMBchpdHwMAWkflpcRWoN2NSyqhpnVum29_iYIK7O5gA0ouo3bLy_qEDGTECutofo2HenpzFzrZ0PN7kcOHreDRsR4sJXoFVG8b0gNIR35NXIXBjQ33jp-sFVom74e8CcuaUOLoYxQUA7fXTJg21RsB0HQdqhygki4FMNGKnZJHSjW74mIGjGjBXm-DLd7fqAuDiQ9g2WntFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعریف ساده MITM:  در یک حمله MITM، مهاجم خودش را بین دو طرف ارتباط (مثلاً شما و سرور بانک یا سایت مورد نظر) قرار می‌دهد. دو طرف فکر می‌کنند مستقیم با هم در ارتباط هستند، اما در واقع تمام ترافیک از دست مهاجم رد می‌شود. مهاجم می‌تواند: 1- شنود کند (ببیند چه…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/3234" target="_blank">📅 18:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3233">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دلیل اینکه این ویدئو و ویدئوی پارت 1 اش رو توی یوتوب نذاشتم این بودش که MITM(Man In The Middle) یک نوع حمله‌ی سایبری هستش(که ما ازش داریم برای اتصال استفاده میکنیم) و دانلود از تورنت و یوتوب هم که غیرقانونیه
😂</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3233" target="_blank">📅 18:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دلیل اینکه این ویدئو و ویدئوی پارت 1 اش رو توی یوتوب نذاشتم این بودش که MITM(Man In The Middle) یک نوع حمله‌ی سایبری هستش(که ما ازش داریم برای اتصال استفاده میکنیم) و دانلود از تورنت و یوتوب هم که غیرقانونیه
😂</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3232" target="_blank">📅 18:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3231">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">چنان انرژی‌ای برد از من توی یه روز دوتا ویدئوی سنگین دادن که الان جنازه شدم</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/3231" target="_blank">📅 18:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3230">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">☠️
دانلود از یوتوب و Torrent با اینترنت ملی، به صورت نامحدود!
(پارت2)
توجه: ابتدا باید قسمت اول این ویدئو(
https://t.me/MatinSenPaii/3151
) رو دیده باشید.
لینک داخلی: به زودی قرار میگیرد
⚡️
لینک پروژه عزیزی:
https://github.com/TheGreatAzizi/AzuDL-GC2GD
(با استار دادن بهش ازش حمایت کنید)
و روی گیت شخصی خودش(اگر گیتهاب در دسترس نبود):
https://git.theazizi.ir/TheAzizi/AzuDL-GC2GD/
لینک وبسایت RiceDrive(بخش ساده):
https://ricedrive.com/
لینک وبسایت کولب(بخش سخت):
https://colab.research.google.com/
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از دوتا وبسایت خاص، به طور نامحدود با ترکیب روش MITM از یوتوب و سایت‌های دیگه، دانلود کنید.
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
بخش اول
رو دیده باشید
✉️
تماشا در تلگرام
💰
دونیت</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3230" target="_blank">📅 18:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3229">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3229" target="_blank">📅 18:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3228">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ویدئوی بعدی دانلود با نت ملی از یوتوب هم در حال ادیته. امیدوارم که به کارتون بیادش اگر اسپوف قطع شد</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3228" target="_blank">📅 17:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3227">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این نسخه، با نسخه دسکتاپ قبلی کلا فرق میکنه و بازنویسی شده. نسخه‌ی قبلی رو حذف، و این نسخه رو نصب کنید.
ویژه‌ی مک و ویندوز</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3227" target="_blank">📅 16:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3223">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه WhiteDNS Desktop V1.0.0-beta2
✅
حل مشکل باز کردن در ورژن های قدیمی مک
✅
حل مشکل وصل نشدن و خطا بعد از ۴۵ ثانیه
✅
حل مشکل وارد کردن کانفیگ به صورت گروهی
✅
حل اضافه شدن دگه ذخیره برای ریزالور های سالم و. فعال به صورت جداگانه
✅
حل مشکل مشکی شدن صفحه در ویندوز
✅
اضافه شدن نسخه های لینوکس</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3223" target="_blank">📅 16:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3222">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">☠️
آموزش روش جدید و قدرتمند SNI Spoofing - اتصال رایگان و بدون هزینه به اینترنت آزاد!  لینک داخلی(30 اردیبهشت): https://guardts.ir/f/9e2486ea4d04  دانلود فایل نرم افزار: https://t.me/MatinSenPaii/2617 آموزش edge tunnel روی کلودفلر: https://youtu.be/svYBcv4bSzo…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/MatinSenPaii/3222" target="_blank">📅 16:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3221">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UA_f6syZt7L0KtVGpC5e4YJuDvm7debfD8oHvaGZqH-CUo_O_dlB9vLeoMMjIEhO3j7UOMnWVZfJfkd_IHa4U9dlI13VSZPbYuVgezkY8-7xAybnw2SX1FfkN1mQcsdWUJTgg7RfsfduIdoEZArUT2hqv-rLM0lbFEtj7hhMOf11-EZ2KXIlNl40uSU7O5nukCWLOGT2Jgmh9PPoVss_Bm4W7r40NErkSFNuIzj--PIosDTPxLvZW5Ai7qVO-xO_YciEV0qlam9opt_FBt6iuxP4xoSJU01dWx82_tXJfLfWD7Hkkl3GZIYLWzNFPJdq0zN88GTQ64qmtencO2QCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭
😭
😭
😭
😭
😭
😭
😭</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/3221" target="_blank">📅 16:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3220">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترسناک‌ترین اسکرین‌شات ممکن</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/MatinSenPaii/3220" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3219">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CTW8JqsJlEjsfrXPpOBL8z2NUEAn82kKH2yBvV5SzEreSoVIuJmtyOFPeEUGrFRuMjifH21rdOzK9VFrpKiiW9XJpFjunvT9hoOAUGPqfbST6EX7FoFPESlAFCdmgfSfTSMRU-n8xTZxQjhNUaBjfDpKmROk8CXmEPDaiYB4dxbLy4pBGAMedh3FQB9xEOYYAOnDtUWDqtT1D26a6NewS8SVERAewbWzi9CQ2Fhrd5dgxLuwCpolh87iMVQPwMFRiP0OT3zKpIrg4XCdY8OeSlse98OatTCtZPddeeI77_m3zD2YGjnQUiJooRlLkebjU3RoUhIO8ZfulLQh7xXyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترسناک‌ترین اسکرین‌شات ممکن</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3219" target="_blank">📅 16:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3218">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">آموزش اپلیکیشن Cloak برای کانکت شدن به کانفیگ‌های SNI Spoofing روی مک
با این روش هیچ نیازی به استفاده از ترمینال ندارید و خیلی ساده‌تر هست
و همچنین توضیحات راجع به شیر کردن کانفیگ‌ها با دیوایس‌های دیگه‌تون
این ویدیو باید تقریبا تمام مشکلات دوستان مک‌دار رو حل کنه
لینک دانلود داخلی ویدیو
گیت‌هاب اپلیکیشن Cloak
لینک دانلود داخلی اپلیکیشن Cloak
لیست کانفیگای جمع آوری شده توسط متین عزیز
نکته: برای اپلیکیشن‌هایی مثل تلگرام که سیستم پروکسی رو اتوماتیک نمی‌گیرن شاید لازم باشه یه پراکسی ساکس دستی روی پورتی که اپلیکیشن توی ویدیو بهتون می‌گه اضافه کنید
نکته ۲: متاسفانه این اپلیکیشن هنوز تانل نداره و ممکنه یه سری اپ‌ها که سیستم پروکسی رو نمی‌گیرن باهاش کار نکنن.  برای تانل پیشنهادمون همون استفاده از
Throne
هست
پی‌نوشت: عذرخواهی می‌کنم بخاطر کیفیت فوق‌العاده میکروفون :)))
@khosrow_v2ray</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3218" target="_blank">📅 15:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3217">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔭
خب گویا GitHub دیروز یه بمب سنگرشکن(
😂
) امنیتی خورده. خودشون تو توییترشون اومدن جزئیات رو دادن. خلاصه‌ش اینه:
⚠️
یه اکستنشن آلوده‌ی VS Code نصب شده بوده رو دستگاه یه کارمندشون. این افزونه مثل یه تروجان عمل کرده و دسترسی به ریپازیتوری‌های داخلی گیت‌هاب داده. هکرها ادعا کردن حدود ۳۸۰۰ تا ریپو دزدیدن که گیت‌هاب هم می‌گه "تقریباً درسته". اما عمق فاجعه اینه که هکرها تونسته باشن به ریپوهای سازمانی و API key ها و غیره شرکت‌هایی که از گیتهاب استفاده میکنن، دسترسی پیدا کنن.
و خود کارمندهای گیت‌هاب هم در مقابل:
- سریع اکستنشن رو از marketplace وی‌اس کد برداشتن.
- دستگاه رو ایزوله کردن.
- کلیدها و سیکرت‌های مهم رو همون روز عوض کردن (rotate کردن).
- الان دارن لاگ‌ها رو می‌گردن، چک می‌کنن چیزی مونده باشه یا نه، و منتظر فعالیت بعدی هکرها هستن.
گیت‌هاب گفته فعلاً فقط ریپوهای داخلی لو رفته، نه کد مردم. قول دادن گزارش کامل‌تری رو بعداً ارائه بدن.
👋
چرا این خبر حسابی وایرال شده؟
- طنز تلخ: مایکروسافت/گیت‌هاب که خودشون VS Code و marketplace رو مدیریت می‌کنن، با یه افزونه مسموم هک شدن! و برنامه‌نویس‌ها توی توییتر و Reddit دارن می‌گن "ما سال‌هاست التماس می‌کردیم marketplace رو درست کنید، حالا خودتون خوردید!"
- ترس عمومی: نشون می‌ده حمله به supply chain developer tools چقدر خطرناکه. تو دیگه کدت رو هرچقدر امن نگه داری، اگه اکستنشن VS Codeت هک بشه، همه چی تمومه.
- مردم دارن می‌گن: "دیگه به هیچ اکستنشنی اعتماد نمی‌کنم"، "device protection لازمه"، "Self-Host و گیت‌لب بهتره تا گیتهاب" و اینها.
و نکته‌ی جالب توجه اینه که این جور حمله‌ها دارن تبدیل به یه روند می‌شن چون هکرها می‌دونن توسعه‌دهنده‌ها ابزارهای زیادی نصب می‌کنن و permission دسترسی‌شون به افزونه‌ها هم معمولاً بالاست.
این نشون می‌ده که حتی توی دنیای امروز، هیچ چیزی ۱۰۰٪ امن نیست
📚</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/MatinSenPaii/3217" target="_blank">📅 14:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3216">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سؤال: چرا نمیشه روی اندروید به تنهایی این متد رو راه انداخت؟
جواب: دقیقا مثل روش Paqet، اگر خاطرتون باشه متد SNI spoofing هم نیاز به دسترسی ادمین داره و برای همین باید گوشی اندروید، طی یه فرآیند پیچیده‌ای(که جز ضرر هیچی برای گوشی من و شما مردم عادی نداره)، Root بشه.
سر همین تا قطع نشده یه لپ تاپ ویندوزی‌ای گیر بیارید و انجامش بدید و استفاده کنید</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/MatinSenPaii/3216" target="_blank">📅 14:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3215">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو: https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/MatinSenPaii/3215" target="_blank">📅 13:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3214">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو:
https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری تنظیمات خاص، لوکیشن ثابت آمریکا بگیرید.
با تشکر از کاربر توییتر
Kharabam
که اون قضیه‌ی رجیستری رو یاد داد(توی ویدئو توضیح دادم)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
ابتدا ویدئوی اصلی SNI-Spoof رو باید دیده باشید و راه‌اندازی کرده باشید:
https://t.me/MatinSenPaii/3186
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/MatinSenPaii/3214" target="_blank">📅 13:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3213">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شاید دوستانی که تازه اومدن ندونن. اما رفقا من بارها از دی‌ماه که فعالیتم رو شروع کردم این قضیه گفتم.
من برنامه‌نویس بکند هستم اما متخصص شبکه نیستم. صرفا کامپیوتر رو دوست دارم و متدهایی که خودم یاد میگیرم رو سعی میکنم به زبان ساده واسه‌ی شما هم قرار بدم.
کار اصلی رو هم توسعه دهنده‌هایی که متخصص شبکه هستن و اون پشت دارن زحمت میکشن انجام میدن و من کوچیک همه‌شون هستم و تشکر بسیار زیاد دارم ازشون.
یک سری چیزها رو هم صرفا از سر کنجکاوی یاد میگیرم یا ترکیب کردن یه سری چیزا با همدیگه و صرفا محتواش رو ضبط میکنم و می‌ذارم
❤️
کانال یوتوبم هم قبل از دی‌ماه موضوعش انیمه و مانگا ژاپنی بود
😕</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/MatinSenPaii/3213" target="_blank">📅 13:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3212">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هردوتا ویدئو(دانلود با نت ملی از یوتوب(بدون روبیکا و بله) و ارورهای رایج و ثابت کردن لوکیشن sni-spoof) رو ضبط کردم، منتها چون گفتم SNI ممکنه قطع بشه، اونو زودتر ادیت میکنم و میذارم. ویدئو یوتوب هم بعدش ادیت میکنم و قرار میدم واستون(همون که دنباله‌ی روش MITM بود)</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3212" target="_blank">📅 12:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر اینترنت نداشتیم الان که اسپوف وصل شده موندیم با اینهمه اینترنت چیکار بکنیم:))</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/MatinSenPaii/3211" target="_blank">📅 12:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3208">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امروز اگر برسم هم ویدئوی ادامه‌ی MITM رو داریم(سر یوتوب) و هم ویدئوی تغییر آیپی اسپوف برای گیم زدن</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/MatinSenPaii/3208" target="_blank">📅 09:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3207">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رفقا اسپوف همچنان وصل؟</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/MatinSenPaii/3207" target="_blank">📅 07:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3206">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDI5l7ziyIO75gFTztbHG2NKyBD-HoHsLZa43JvbmNhnEkLCG0bxa-l9csTdGGibt8IcuslFc6p6yXx_h_sZjs4XbYxh3Py1wFVwmXGmSxIWp49xHJHfeL-He20w8WxFj3ma8VvSvklqrzWWAn2JL49Yz2Zot8kdOhIn7P6Y6-EZ2Bm3C9We9FDvGSFqAMVNDvSMHHhZkhj47eeJtLl6kHpHb5yY-giXb0ixk3WD90v6ruwu-T1LmSzByGQpWk6wnKXg0Q9uSWW_xa0u5ly3mPVDtEf9lODgmkPEjjdin2LYeNLGvAPbLtKWuomP0Vbn9s3LmuWRnGmz2C3tQwL8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت رایگان برای یادگیری باگ بانتی :
vulnweb.inst.lk
@Linuxor</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/MatinSenPaii/3206" target="_blank">📅 23:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3205">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">خب این هم آموزش SNI Spoof برای مک.
فرآیندش برای ویندوز و لینوکس کاملاً مشابه هم هستش. فقط باید فایل اجرایی‌ای که برای sni spoof هستش رو مطابق سیستم‌عاملتون دانلود کنین.
فرقی هم نداره که از چه برنامه‌ای برای کانفیگ‌ها استفاده کنین.
لینک دانلود برنامه SNI Spoof برای مک و لینوکس
برنامه آپلود شده در تلگرام
لیست کانفیگای جمع آوری شده توسط متین عزیز.
کانفیگ JSON
لینک دانلود ویدئو بالا برای اینترنت ایران.
@khosrow_v2ray</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/3205" target="_blank">📅 22:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3204">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/MatinSenPaii/3204" target="_blank">📅 22:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3203">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VilrbtJaZmCBTDraOEtYD4fqM61psXu-8JIHzhSdvYOLAzQttFn84p2rQIL-Sbnfe_9tbl0fQmv8U5GaEe-bIWZeEXJFtPMRfxRjnpqKTFc4qNgY2Y7hUyilbrts6DH2mMSl13wA8Tls6dER8le3KekHhj03z_HObnOln-IgL0JCaNv0Jc9w7I-D72y3t2PEMcUEkFiC0pTZG0S6dp2DmK0JThOMTBLTUfqHM8q14HhEvn8_kS58pK-HqGe2fIKKpR-haYq9uNZ00WkHLkv0Sq9l3ZLFh1ViZGDxbQSS29v5rbs-h1RJ9ZBADygcHUKTy-jg4kXeAQERDClK_KU9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ارور به علت پایین بودن ورژن ویندوزه</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/MatinSenPaii/3203" target="_blank">📅 21:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3202">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یک سری آیپی‌های کلودفلر وایت شدن گویا.
اما اختلال زیاد دارن
میرن و میان
اسکنرها رو روشن کنید، با تایم‌اوت بالا. ببینم چه می‌کنید</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/MatinSenPaii/3202" target="_blank">📅 20:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3201">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یه حسی بهم میگه حکومت یهو باز میکنه این متدها رو که ملت بپرن بسته اینترنت بخرن و مجدد قطع بشه، نمیدونم واقعا. قشنگ یه الگو شده
هر دو سه هفته یک بار یهو اسپوف یا یه متد خیلی راحت برای اتصال باز میشه و مجدداً بسته میشه. اعصاب خورد کن شده. نه دارن باز میکنن نه دارن میبندن</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/MatinSenPaii/3201" target="_blank">📅 20:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3200">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dfN1C3kdNSJDW8QJh4AagzGiwC-Sx8jv_JJg270wOuV4yJKWuNFYEV8Ja2c9ldzhi3XwFVWXNroN9MBE6-VfdcTEhjVrND5cUfWKnGlMzBruUWYEXJYUakHOLYGQAoUFd0AsDJMgDOM7PvkXOQAkrJM-zx4RBgAmNSiXKq9ZmrFNflgMK7DwWjrRnzV6EI290WE97vpv144eEWsyR5bZGBfIAYRoTGug2jb5gMvGria7MnV0p9QJOGqBTbVWIvLDQRvzxHa6ext9c43GO5gV9Ubln38qHDIxalg3hzVR0jX8E8NRSqg9-DbMj6Rqqum_cknWsVIjVKpc8lMlnyrY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر پنجره باز شد، و از کانفیگتون پینگ گرفتید، و -1 داد و اینجا هیچی ننوشت،
یا مجدد، WinError6 داد و بازم -1 گرفتید، یعنی اسپوف با این کانفیگ json(hcaptcha) روی اپراتور سرویس‌دهنده‌ی اینترنت شما بسته هستش</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/MatinSenPaii/3200" target="_blank">📅 20:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3199">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آیپی‌ای که اینجا بهتون میده، صد درصد کار میکنه روی شیر و خورشید و MahsaNG
❤️</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/MatinSenPaii/3199" target="_blank">📅 17:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3198">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eSUxLX15Z7QqUG7fF4gveUMPB_Vd0hogHlJW8Cu2QqPs8coEYs2rfp79DXU2z1pqUcpV2Ssfrr7v9gvgJ2Pk5bCJck66ds4AOg8Mzkw4HxWF3u9G0VJpyNZaF-Yp9xfuCznAA8bEZfBxjdi7T2UDtUb9fdpPG0u_qvVi5TM8YgzmHqDU2xbLBc1uoe5Ycc0Z_elwhhB7fLSghRpCr5LYopZOgCbsomiDFlY8Gv4zaJoUu3KuHcTbg5JxzCZAYG8ZbYYls6uOM-btPHdJ5R0YXyS5RXnAYCKdV0GfP8Iolr8wB3Z9NrgEYeVyH_dxI4dlkA83NPkjuRLYqdgdyh5SJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ رو هم چک کنید، اسکنر برای Akamai و کاربردی برای شیر و خورشیده https://github.com/mirarr-app/network-checker</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/MatinSenPaii/3198" target="_blank">📅 17:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3195">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P13WUStA7wY-TB68dKMyo6yujmVnrPz9WNbH_XvdjYudphBBNnRaTfPoShU2x6lK9xt43QDQPBBdwzQRME--_8FHxvjf-9pVnzLTeON0zNRogZ6ag-qh8xTjDcgWcLsNj8ZXnYN4tKQS9hQ_ZzTCWFuc9SIIwW1zCU6G0EeTKG_mJ-1IBkfhl-cTAQzFnOsuqnU2D2gOAonRpvHsbFZ1BnoTiBMqvmrNvqk2tAlhgf-PR6u4rjTCQMx2sXt1MoP0g2djepVN_c5UeqB6TxehUymaaiD0-gx9Ug6NLs6h0erjvsuLNOFyJ1b65OvA9vO0g1WtigzydDaGIBChx0wwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/MatinSenPaii/3195" target="_blank">📅 15:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3194">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دقت کنید، اگر خود Spoof لاگ داره
و V2ray هم لاگ داره اما پینگا -1 هستن همچنان
یعنی مشکل از اپراتوره. اپراتورتون رو عوض کنید و با هرچی سیمکارت توی خونه دارید تست کنید. روی اینترنت خونگی هم به کرات دیدم توی طیف وسیع‌تری پاسخگو هستش</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/MatinSenPaii/3194" target="_blank">📅 15:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3193">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/MatinSenPaii/3193" target="_blank">📅 14:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3192">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qKmVywq1pPsdurw-1o7YcB9fk6VWhY4TEnfnzSy5ZvjHrqYfWOk5LdExSKNqRF-YWR6_NrkGVLNQvz7AnLbRD5JXM7yDFF6eK1hAbP7gh4QQtjMj9EIlfEW9jMH9RkJebskWJCcR-6kcswIjtm1Vd6fAK8S_eX3_i60fWDZgif-4VfUvft3gazhwdRNtY0T8RoOvE575Is71lFlJcs3ejl9NgngRA8K-yqQCqTtM_91vrJSLzIZDVKuqemJwh60bECVOdi6RJJnHPAtOhRaozUXZx8Z8FKFCP1CyXdvO2K8iFaT1D6TFjE_lJiZ22gnlKm6bqYt8PQ0Y4SmyNin9Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا داریم قله‌های پیشرفت رو فتح میکنیم</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/MatinSenPaii/3192" target="_blank">📅 13:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3191">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یکی از دوستان گفتش که روی آسیاتک، خود hcaptcha پینگ نمیده اما کانفیگ‌ها وصلن روی Spoof
یعنی json شما باید همون hcaptcha باشه، خیلی عادی ران میکنید و پینگ میگیرید و بعدش کانفیگ‌ها بهتون پینگ میدن.
راهنمای کامل</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/MatinSenPaii/3191" target="_blank">📅 12:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3190">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9a90f10d4b.mp4?token=AjAIVeHvRKg3_vdPhVHD2Q20yW3BPiDNvUpD1t21Krvxqs25X3sdDHAeIkA65T7WNYJhtPY1NgCDaWaxXqkh2yRh7h_N7fUJeJt3OCJNoF85oZUQMyUEDdelhGA8vCJ4IKTs4WS0bdc808_5kYXchH5bnuK4SR06-fpk8AuHWPNvFRoG24oZ2bcxsHjboH6sijToYAEqkKhaKmA4LyWeDMJC-80CqkCC-MSQWGFgsGwHP_NKGkGb2w_f5DMMyH5Dub5aTud7fn9tOgPAjxzMpozqCbozDuv6iPpQV5m4NGc9z2NNbXq8ZKVTgAbjiAlxY2vX9QHB_bE4nCCJNdUTHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9a90f10d4b.mp4?token=AjAIVeHvRKg3_vdPhVHD2Q20yW3BPiDNvUpD1t21Krvxqs25X3sdDHAeIkA65T7WNYJhtPY1NgCDaWaxXqkh2yRh7h_N7fUJeJt3OCJNoF85oZUQMyUEDdelhGA8vCJ4IKTs4WS0bdc808_5kYXchH5bnuK4SR06-fpk8AuHWPNvFRoG24oZ2bcxsHjboH6sijToYAEqkKhaKmA4LyWeDMJC-80CqkCC-MSQWGFgsGwHP_NKGkGb2w_f5DMMyH5Dub5aTud7fn9tOgPAjxzMpozqCbozDuv6iPpQV5m4NGc9z2NNbXq8ZKVTgAbjiAlxY2vX9QHB_bE4nCCJNdUTHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/MatinSenPaii/3190" target="_blank">📅 11:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3189">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✍️
سؤالات متداول راجب SNI-Spoof:
1- ارور WinError2 میگیرم توی اپ؟
این ارور به این معنیه که شما نرم‌افزار رو با Run as Administor ران نکردید. اگر مطمئنید که این کار رو کردید و باز هم این اروره رو میگیرید، به سادگی یک بار ببندید و مجددا باز کنید.
2- ارور WinError6 میگیرم توی اپ؟
این طبیعیه کاملا. باید هم بگیرید. اصلا اگر این رو نگیرید یعنی کانفیگتون کار نمیکنه. همینجوری پشت سر هم تکرار میشه و این اوکیه. مشکلی هم نیست
3- پس اگر ارور WinError6 میگیرم یعنی وصله؟
نه لزوما. ممکنه همچنان Hcaptcha روی اپراتورتون بسته باشه. پینگ هم بده اما کانفیگا -1 بدن بهتون با اینکه WinError6 هم میگیرید. با اپراتور دیگه‌ای امتحان کنید.
4- اگر
Hcaptcha.com
بهم پینگ بده توی ترمینال یعنی وصله قطعا؟
نه لزوما. توی سؤال قبلی عرض کردم
5- اگر
Hcaptcha.com
بهم پینگ نده توی ترمینال یعنی قطعه و کار نمیکنه؟
نه لزوما. توی یه برهه‌ای Hcaptcha پینگ هم نمیداد اما وقتی با اپ پترنیها ران میکردیم، کانفیگ‌هامون پینگ میداد
6- با چه اپراتوری بهتر جواب میگیرم؟
منطقه به منطقه فرق داره. همراه اول به طور مثال یه جا وصله، یه جا قطع. اکثر اپراتورهایی که دیدم وصل باشن، ایرانسل و سامانتل و رایتل و فیبر مخابرات و مبین نت بودش و adsl خونگی
7- کی این متد رو میبندن؟
به قول یکی از بچه‌ها هروقت ثبت نام ایران‌خودرو تموم شد:))
اصلا مشخص نیست کی میبندن و چرا باز شده و...
اما تا وصل هستش کارهای ضروریتون رو برسید لطفا. آپدیت‌های سیستم عامل و...
فقط روی اندروید حواستون باشه سیستم عاملتون نیاز به لاگین نداشته باشه بعد از آپدیت
8- دقت کنید، اگر خود Spoof لاگ داره
و V2ray هم لاگ داره اما پینگا -1 هستن همچنان
یعنی مشکل از اپراتوره. اپراتورتون رو عوض کنید و با هرچی سیمکارت توی خونه دارید تست کنید. روی اینترنت خونگی هم به کرات دیدم توی طیف وسیع‌تری پاسخگو هستش
9- چرا نمیشه روی اندروید به تنهایی این متد رو راه انداخت؟
دقیقا مثل روش Paqet، اگر خاطرتون باشه متد SNI spoofing هم نیاز به دسترسی ادمین داره و برای همین باید گوشی اندروید، طی یه فرآیند پیچیده‌ای(که جز ضرر هیچی برای گوشی من و شما مردم عادی نداره)، Root بشه.
سر همین تا قطع نشده یه لپ تاپ ویندوزی‌ای گیر بیارید و انجامش بدید و استفاده کنید</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/MatinSenPaii/3189" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3188">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HDRnPa-hUWPrH70iXlUvVENO8tb77uvlP2e85RJwQehnO536kumilmZk4CQdNO29Kv7LYu1PJtzZ7Ck-YGa_c17q3zFS8DNl0_naV0fhGJg2Wxnf3xTCQaj7KPuljRORecMtlg0n-Cp28JWoZWfud_j4ULyy-EIsLgwrIWLGCfRqI7x-eOtoXX_jvQBZ9paOtlb1lwTACsNXYOR8xpNrwX9f6Ieb-KrTNRCzQ2Bg0rIsKwf8HZn0avdLAa4xrQiKHpeg31cywrEEeGGa5RWyvpitQzyxk_bafogsNQrfV8WiFxh_9E4NelpJpb7NMmKCaznleWsDzR1eRHJ1UKn0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)))))))))))))))))))</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/MatinSenPaii/3188" target="_blank">📅 10:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3187">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">Matin SenPai
pinned «
⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:  1- آموزش پایه: https://t.me/MatinSenPaii/2627 2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید: https://t.me/MatinSenPaii/3168 3- و کانفیگ‌های این پست: https://t.me/MatinSenPaii/3183…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3187" target="_blank">📅 10:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3186">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شاید شبیه کلاهبردارا به نظر برسم اما می‌خوای نامحدود به اینترنت آزاد وصل بشیییییییی؟
😂</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/MatinSenPaii/3186" target="_blank">📅 10:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3184">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qJXdFAX-56QA1wTozfEpD9VMNlAfqk9JBGNSfCJQ54KHCk6VpLPHnVYWZ2CgWe1LkpHGcY5waLSIGDMCmD24Uwi77KD3WLljQ8BVPMQmsQIlQYM-Tp5e9K4cfOXHcvvLj7gvEmfCNSFh_-4HOkGMZo020IBlddY9_vJWJjj09zjqb-6iIOFM3312lTL4JDn9GdovIorjcdx4tjkBj5Gu3xP7q8Ifmq-SLHoGlLK4xfWubhO4Ic1-GEz8QEWR6n203x2ugBM5VUWp5k5MZHtd6lCA9ZO9XpWiu-Ywnmj5vU7K1DmRoR_ViotMEFGCqSFy_6sQlPpIJ_oP-iYD3gPxgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KeW06Vk2YPL6XpEmNLh6jTzklwkdy3JqVGytWcjUFwVs0wN-e3bb_Z2YqfHTekRDwt-O7WBseaq_1gOcgi_RLWSISihZh63li8PFJB4J8dIOib7paAmLOXpWcXWB0Q9Z_OjABzhMSFC6pMq74eFCdvqB7dx-RZlJNKPkFCZ03KBA86a9Kdhd1lTAzjfU5r5XuUjpjROhACCwu0oqbOI-CVPyoUGy3d-wTr7Sj5GmiXKYEca72lm8az62SAfid8IZgnNIGMHzkV3rAIluU_-aNuWnrdNhG5PeUne8zk8UxiuAa1CTIMZH9pWsF7180S4-_mXjrKu82PvOUB2--FRW4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاید شبیه کلاهبردارا به نظر برسم اما می‌خوای نامحدود به اینترنت آزاد وصل بشیییییییی؟
😂</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/MatinSenPaii/3184" target="_blank">📅 10:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3183">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/MatinSenPaii/3183" target="_blank">📅 10:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3182">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اگه spoof وصل بمونه یه هفته قیمت کانفیگ به زیر گیگی 10 هزار تومن سقوط میکنه
😂
این خط و این نشون</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/MatinSenPaii/3182" target="_blank">📅 10:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3181">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خب دوستان نتم رو کردم ایرانسل مجددا متصل شد
همراه اول و شاتل برای منطقه من جواب نمیده</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/MatinSenPaii/3181" target="_blank">📅 09:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3180">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">☠️
آموزش روش جدید و قدرتمند SNI Spoofing - اتصال رایگان و بدون هزینه به اینترنت آزاد!  لینک داخلی(30 اردیبهشت): https://guardts.ir/f/9e2486ea4d04  دانلود فایل نرم افزار: https://t.me/MatinSenPaii/2617 آموزش edge tunnel روی کلودفلر: https://youtu.be/svYBcv4bSzo…</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/MatinSenPaii/3180" target="_blank">📅 09:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3179">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vJ_I8E4ewQjOgEIanWD3LFqiXRShlBfpxuWz9s2Uj0VBk1NdIqTT7N8-zOXWgR2eRFKHO-HMlUEXUzQCEEYeDgzWa_osqcBquiNxuUQcgxfJ1cnJF0qmCr9-3bUzd1RqROmzJbC1Nn4AMbKSrmgKpvRj5h6v6iijyYcp3wfkihTeZ8p8PJGigYuCP-cMx0afyaKVDOmXRUiXtxjpsnRiKoTUYMivzN_KHeSEEtP8kGe8o7YtxC452MLsAtxGAw1W-pZxTZp-WXGjZN6_gobCVKl-E_a0C2MGgED5kJnVPcQMUarU60Jlm_v1QIHsfQ4-iLiCU2muNtdmooB9VeHdjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
اگر hcaptcha بهتون پینگ میده اما هیچ کانفیگی هیچ جوره وصل نمیشه، علتش اینه که هنوز پشت NAT هستید.
حالا چطوری مطمئن بشیم؟
اینو چک کنید اگه IP خودتون رو نوشته بود یعنی باید وصل بشه و مشکل یه جا دیگس
hcaptcha.com/cdn-cgi/trace
‎
و اگه IP خودتون نبود یعنی هنوز پشت NAT هستید.</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3179" target="_blank">📅 08:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3178">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">همچنان وصلید؟</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/MatinSenPaii/3178" target="_blank">📅 03:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3177">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اینور کلا تعطیل شد آپدیتی چیزی دارید سریع انجام بدید</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3177" target="_blank">📅 03:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3176">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o-BuWHqY2Y1goTr-Dgm_kGL-k6WcKoF_N2AyFNjDpvhW70R4LlSZL8TgZ7Ydf7s5VUyk8J0_SV387gJ_427NxUVUi_158fzY64FD748PNrYVxzwHUsagrl1QAbEWuKxzCqooD3UsuzRmFa9a4DItgKvus4JKOv10hy6qZ4dQHZ7bgFT-SgoiJx8QW7pO6VKIuoi-7ZjfIHh0udeQa4v-iC04Cl50nOpPeH9EAX77qTo6vDnWxeb6m-b0IfZp_DrK9dDGeMOdM8-qJHTy1sps9b2lJ9-cHblpAjBw_3rfDG5cK8rWYNtZZCLQJ41DO1z8NVrvaGrzDdqFHCeUdS3ENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینور کلا تعطیل شد
آپدیتی چیزی دارید سریع انجام بدید</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/MatinSenPaii/3176" target="_blank">📅 02:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3174">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Spoof-SNI-Configs-List-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">12.5 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3174" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">هرچی کانفیگ ویژه‌ی SNI Spoof با پورت 40443 بود واستون جمع کردم از کانفیگای خودم و بچه‌ها و هرچیزی که توی کانال‌ها گذاشتن، توی این فایل txt واستون قرار دادم</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/MatinSenPaii/3174" target="_blank">📅 02:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3173">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">با این کانفیگ‌ها تست کنید:
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&type=ws&host=www.creationlong.org&path=%2Fassignment#1
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?encryption=none&security=tls&sni=sni.111000.indevs.in&fp=chrome&type=ws&host=sni.111000.indevs.in&path=%2F#2</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/MatinSenPaii/3173" target="_blank">📅 02:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3172">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یکی از دوستان توییتر گفته تامکت به قید وثیقه سنگین آزاد شده. امیدوارم که درست باشه این خبر
🔥</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/3172" target="_blank">📅 02:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3171">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Matin SenPai
pinned «
انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست: https://t.me/MatinSenPaii/2627 جیسونش هم این: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "104.19.229.21",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com"…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3171" target="_blank">📅 02:06 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
