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
<img src="https://cdn4.telesco.pe/file/EU0qUAghnO4Nz-5Bwf5oc6xFADnAG4o0k5BqW9-n-DUKMU7oYf8y_rbC0uH7okxaUCkKGgfbkOF5h6WBXCcanQRUXstxcc9OXFyxer2KegUlMcRcvYGUoH43KjNp8a5kY8xQ1ULpvP0m2TbWHA7cRcIRoWbS4rXF4ymE-5odQHLKz96J06n6lGb3G2uyvbOE4QX7MYppOsFCA-IS0_gfEqv6tvHA8cUaSAwQKbnY9BC8LgX_n1Omw2YZeTtTb9e7ZrC2gl2SUvCj88cNj6V136eXdgm8OEql3ZItgmwFU081C-mt7PNDQbB-oQ50_J59SCB4qopMYxvBFXMoefjKJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 12:53:21</div>
<hr>

<div class="tg-post" id="msg-435298">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc3f7c8fb7.mp4?token=G4VUSBaBpDynbZCs2c5xnaU-jtaK6RS1T0WoCJih0GqI638SmPdpaocvcYDttJnpNh_rNLjTqDBpMDrTxrbYcfpzvuFnildyL8BgD1bMNj7TseKYFmFSlmBWWOv18-RCWkL15XmF9SXuSFAqdxsQabcIAup7lj-NsDx-WZefyeIyV4rtZgM2IXLb7rGuPuEMKZEvX5WweFeWS9mF7hIZUj1FS-OXNMnDI9uZdm0jakiGGPl5P9P8L2t_N5o8we-wPYQ1qFdSRl567su38LDFGCh-WbpxdCf1FMywdIJqaMq3sMH-TZc9jgvR58JLXM27qmJWn6f1wvAtmn0bJHHPu6a8kMHoqi4M5VUZaZWpI6dNfORubQC2ke7hMHpl7ru3EpXCZjDaBpah9d-CCdvw9QQ_WAvm_A06vhi97zz4EfOWbKcf2JLS0bsrqswzA8xGboLbf8Zebm1SHVJjFAsZv0yoWIMMBOUDErKeT9wmRkRElaZxfvMRa8T9quLXYV5abaWAWfN-YL9OnXAI631vGnBWr42fqmgO2YPlLjT4TAYDheeabGnPSzy0K4esxmE3DoTk9hwFl7KO6tBaY_vHgUgHYANgsvsgKcSZhGOHVu9DEonAd1dj0b3_93KmEv-P7gDps7hizxAhwAsVvBCEesa2kWwvjJ5RwGCzv3g_Wts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc3f7c8fb7.mp4?token=G4VUSBaBpDynbZCs2c5xnaU-jtaK6RS1T0WoCJih0GqI638SmPdpaocvcYDttJnpNh_rNLjTqDBpMDrTxrbYcfpzvuFnildyL8BgD1bMNj7TseKYFmFSlmBWWOv18-RCWkL15XmF9SXuSFAqdxsQabcIAup7lj-NsDx-WZefyeIyV4rtZgM2IXLb7rGuPuEMKZEvX5WweFeWS9mF7hIZUj1FS-OXNMnDI9uZdm0jakiGGPl5P9P8L2t_N5o8we-wPYQ1qFdSRl567su38LDFGCh-WbpxdCf1FMywdIJqaMq3sMH-TZc9jgvR58JLXM27qmJWn6f1wvAtmn0bJHHPu6a8kMHoqi4M5VUZaZWpI6dNfORubQC2ke7hMHpl7ru3EpXCZjDaBpah9d-CCdvw9QQ_WAvm_A06vhi97zz4EfOWbKcf2JLS0bsrqswzA8xGboLbf8Zebm1SHVJjFAsZv0yoWIMMBOUDErKeT9wmRkRElaZxfvMRa8T9quLXYV5abaWAWfN-YL9OnXAI631vGnBWr42fqmgO2YPlLjT4TAYDheeabGnPSzy0K4esxmE3DoTk9hwFl7KO6tBaY_vHgUgHYANgsvsgKcSZhGOHVu9DEonAd1dj0b3_93KmEv-P7gDps7hizxAhwAsVvBCEesa2kWwvjJ5RwGCzv3g_Wts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آنچه آیت‌الله بهجت ۳۰ سال پیش دربارۀ رهبر شهید انقلاب پیش‌بینی کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/farsna/435298" target="_blank">📅 12:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435297">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsld1YkgTx8jspM5HbBbefUHv-vVOwpi0IIJJRfbquGdEiBpGYgXxqIVHlieHUoVydAEq7DoAmzxmFf-zx_pilgjEZr5ZE-2Xsx7iO1BxPOWCmC89bt4OSOpmxiWXeMa-vHZBBSxXOUVWBf7NeIKpQcM7MxvqAcfGSIPueHul1dJ6DGN7uUnPoH4-r9jf-CYdyGJD3Qyzib7rcDsXJVGsLmHYUsvvr6WzBoh4CPzNn8a6AwX57sJRqolYWhFEXyWKvVlrmft0-xyGTdwO9W3iJ6I4I6CD2i2P6KBHhqA11GOm0gIkDIeVe53g9Nh18eX784n-3uW0h9RtUyxIkLaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت اربعین شهادت سردار سیدیزدان میر
🔹
مراسم پاسداشت چهلمین روز شهادت فرماندهٔ گمنام جبههٔ مقاومت اسلامی سردار سرتيپ پاسدار شهید سیدیزدان میر (حاج اصغر باقری) و شهیده دکتر فاطمه‌سادات میر، جمعه از ساعت ۱۷ تا ۱۸:۳۰ در مسجد شهید بهشتی تهران برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/farsna/435297" target="_blank">📅 12:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435296">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9v4bG0UF93QRNqbRzNVIsqn6eDgdqmLjk1P4cqkd7pxRmKxBOIjUVxJJr1cjizoTVslLFEkg2SSKa5Q0ctkujOqUY1L0S1cZDQypWDVqLC94uRT3PiNuTzUAv3Kf8uFDuXW8BVNAySD7TPvviCYLML89rU2EXXg5tmY-fq5puUns6whLi5fJHrbtKXsDa2ofsJkKBorejFxr-QUeiocWpH2Oba7kTC6d3pKHx_0m4mPBXGzmhTMiHjCMC_caqPKmRQEQYjJ-yEhbJQFB1Zy76cIEocWxrtuNPNX7h1xqSOYv5aDgPkb4iDOfXgb16M-0uo3og2cbqUbO3M-wA8iMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای مجلس و مرغداران بر سر مقصر گرانی
🔹
نایب رئیس کمیسیون اصل ۹۰ مجلس، وزارت جهاد کشاورزی را دربارهٔ گرانی مرغ مقصر دانست که با وجود نهادهٔ کافی، جوجه‌ریزی کمتری در فروردین انجام شد و تولید را کم کرد و قیمت‌ها تا ۳۹۰ هزار تومان در هر کیلو بالا رفت.
🔹
این درحالی‌ست که اتحادیهٔ مرغداران، کمبود و گرانی ۵ برابری نهاده‌ها، خوراک،‌ واکسن و دارو را مانع جوجه‌ریزی اعلام کرده که تولید با هزینهٔ گران برای آنها صرفی نداشت.
🔹
بر اساس آمار اتحادیهٔ مرغداران، جوجه‌ریزی مرغداری‌های کشور در فروردین ۱۰۶ و در اردیبهشت ۱۲۶ میلیون قطعه است که این میزان افزایش جوجه‌ریزی ۴۲ هزار تن تولید مرغ را بیشتر می‌کند و نیاز ۱۷ میلیون نفر را در ماه بیشتر از ماه قبل تامین خواهد کرد.
عکس: علی‌حامد حق‌دوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/farsna/435296" target="_blank">📅 12:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435295">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75236b936a.mp4?token=GaSJcHqSoZHVUfFEsbH-bdULutEMlOECyU4P4XN_cccDUMH-vzK2QcQbBnBkxcgWoDzVWxUs6oL-7LwKNUI693dQqhID7luooZECfjBIFvqxUO2m1Jbgm25ZODLm7dwHqNkJII9C57H91WURULVFnOHcTioNh1lwbHZtBjd31_ZFQCyLtLyFoAW_kCnhp8tbFBbD4dKfC2ONew70x7JZ-0dV07d5YgD5ZjOL0TJ1K9RIp790zd_VrQx7-q18DOyhzwFdkxFzPUns98BOV40ttGCzR63oi8fVACa4tTQk_nPeickp2BetYYGMpSaZ6pONADh2P5GRns7di22-E96QSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75236b936a.mp4?token=GaSJcHqSoZHVUfFEsbH-bdULutEMlOECyU4P4XN_cccDUMH-vzK2QcQbBnBkxcgWoDzVWxUs6oL-7LwKNUI693dQqhID7luooZECfjBIFvqxUO2m1Jbgm25ZODLm7dwHqNkJII9C57H91WURULVFnOHcTioNh1lwbHZtBjd31_ZFQCyLtLyFoAW_kCnhp8tbFBbD4dKfC2ONew70x7JZ-0dV07d5YgD5ZjOL0TJ1K9RIp790zd_VrQx7-q18DOyhzwFdkxFzPUns98BOV40ttGCzR63oi8fVACa4tTQk_nPeickp2BetYYGMpSaZ6pONADh2P5GRns7di22-E96QSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجاهد: نگاه چین و روسیه به قدرت ایران ارتقا یافته
🔹
امروز حرف از رد شدن از ابرقدرتی ایران، شعار نیست و دشمنان ما هم به این نتیجه رسیده‌اند، تا جایی که لحن دشمنان و حتی کشورهای حوزه خلیج فارس تغییر کرده است.
🔹
هیچ کشوری یک‌طرفه با ما تعامل نخواهد داشت و کشورها…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/farsna/435295" target="_blank">📅 12:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435294">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b5381a13.mp4?token=NuGzedqRsTrMuyUHxq0u9FnPuREeTtImFISVf7I_5cNoD6W0HmwfmMm0jJGUnXmHxBnie0knY55LAla37Nqlh4QHEpYEoGTMmB-Nlt2txoqW7F0L_1D2WWA_Tgr_5JNE5JDdVtIoSQqK1Yv3jjnYkbeVWJB2ABb3mlqkQZGN5iIEVeMvS3Vpm-1HAMq-XBCwCjgYJhbUDWBVOW5ZVtD4mwSqYU_ffGbC_7H1MdeoFiOokk_BlkgqKZd-bMF46voplu2YV5F4_E7cNqRWJCLsuB0I1cotLLebECcJnKPnyl0-ZfRotdlF0I8FnzlzbvbFc_g7OuQZOrCNosxHp1Bg3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b5381a13.mp4?token=NuGzedqRsTrMuyUHxq0u9FnPuREeTtImFISVf7I_5cNoD6W0HmwfmMm0jJGUnXmHxBnie0knY55LAla37Nqlh4QHEpYEoGTMmB-Nlt2txoqW7F0L_1D2WWA_Tgr_5JNE5JDdVtIoSQqK1Yv3jjnYkbeVWJB2ABb3mlqkQZGN5iIEVeMvS3Vpm-1HAMq-XBCwCjgYJhbUDWBVOW5ZVtD4mwSqYU_ffGbC_7H1MdeoFiOokk_BlkgqKZd-bMF46voplu2YV5F4_E7cNqRWJCLsuB0I1cotLLebECcJnKPnyl0-ZfRotdlF0I8FnzlzbvbFc_g7OuQZOrCNosxHp1Bg3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور در دورهٔ اصلاحات: مدال افتخار موشکی‌شدن ایران را باید به سینهٔ رهبر شهید زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/435294" target="_blank">📅 11:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435293">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
بازی تو وسط ممنوع، بر بی‌طرفا لعنت
🔹
نوحۀ حماسی نوشه‌ور در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/farsna/435293" target="_blank">📅 11:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435292">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مدیرعامل یک مؤسسهٔ‌ مالی با ۱۳ هزار شاکی دستگیر شد
🔹
دادستان مرکز استان کهگیلویه‌وبویراحمد از بازداشت مدیرعامل یک مؤسسهٔ مالی به‌اتهام کلاهبرداری و فعالیت غیرمجاز خبر داد و گفت: در این پرونده بیش از ۱۳ هزار نفر مال‌باخته شناسایی شده است.
🔹
این مؤسسه در ابتدا مجوز بانک مرکزی را داشته اما از سال ۱۴۰۲ بدون تمدید یا دریافت مجوز به فعالیت خود ادامه داده و این تخلف با گزارش پرداخت‌های گزینشی احراز شده است.
🔹
براساس نظریهٔ اولیهٔ کارشناس رسمی، ماندهٔ اصل سپرده‌ها حدود ۱۶۵ میلیارد تومان و مانده تسهیلات پرداختی در اختیار اشخاص حدود ۸۵ میلیارد تومان براورد شده است.
@Farsna</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farsna/435292" target="_blank">📅 11:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435291">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3d84ad80.mp4?token=UBoZjlJXY5WN8Hkp3JusQoai2emT8flj6R8-QB3FVE77fy2KVse5nrHgUD_IXzMWkc5rCKMRu3YCzhqvcIw75vJjqjXmQw3c9WLMxI4uWjYDN6EbMKRaJWC2UfOAbFkSlyBqBkOUyr0yOyvUxVaTEx3CxM2NxCOmUYsZ7LL603G81lga63EuFNRV0Dm4CN0j2Gfg8MQowSwT2Q77iFzGb1KJEZ8u0WlY3KWs1kmoWDpcILROC0C6Tv1l_eRqnrvhw9OzEB1Pm8QqOsvvdL6-cuEpOtkfvMPSDlPfewMPxwKOEHzUZWpg4U8sWYO3dV31WiTm_2DCNhjIGBZOBiEFYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3d84ad80.mp4?token=UBoZjlJXY5WN8Hkp3JusQoai2emT8flj6R8-QB3FVE77fy2KVse5nrHgUD_IXzMWkc5rCKMRu3YCzhqvcIw75vJjqjXmQw3c9WLMxI4uWjYDN6EbMKRaJWC2UfOAbFkSlyBqBkOUyr0yOyvUxVaTEx3CxM2NxCOmUYsZ7LL603G81lga63EuFNRV0Dm4CN0j2Gfg8MQowSwT2Q77iFzGb1KJEZ8u0WlY3KWs1kmoWDpcILROC0C6Tv1l_eRqnrvhw9OzEB1Pm8QqOsvvdL6-cuEpOtkfvMPSDlPfewMPxwKOEHzUZWpg4U8sWYO3dV31WiTm_2DCNhjIGBZOBiEFYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شابلون‌زدن شبانه یک خانم در خیابان‌های تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farsna/435291" target="_blank">📅 11:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435290">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGbaNbDl0BZj2qes-MlIaiPMymj97c3WfN6tyvm1CEvc4U6l4befEZsys9V1sbFI5pVMtXicGtWu4E8OPRBGBBXDKTbDBYVbJ1lMG4jWXHnQThY-amgVf1CWah8j7s8d2MoKXrDjymfOxg1MjorlXI9Vsre_6lsh2V99WlgVAorZjoEOTTnaDooyMMBtAd0m9chqRaac8NwHkcfbRSM0mAzQ7FuYM8EOzfjJjK32R5YoluWYXPISmRHAjpTFF3_jDL7StN0XJ8Rzm9Zp5G3YU5rUGl5UBRrYfZMGnvgQwdcurdqK2G8wacHQZGujrTuXSd7kwclERU8KM9HYmJBAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: هزینه جنگ ایران یک تریلیون دلار است نه ۲۹ میلیارد
🔹
سی‌ان‌ان در گزارشی به نقل از متخصصان ادعای پنتاگون درباره هزینه ۲۹ میلیارد دلاری جنگ ایران را زیر سوال برد و از هزینه یک تریلیون دلاری سخن گفت.
🔹
«لیندا بیلمز»، کارشناس سیاست‌گذاری عمومی در مدرسه کندی هاروارد در یادداشتی نوشت: «جنگ‌ها همیشه بیش از آنچه انتظار می‌رود هزینه دارند. در طول تاریخ، کسانی که وارد جنگ می‌شوند تمایل دارند نسبت به هزینه و مدت زمان آن خوش‌بین باشند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/farsna/435290" target="_blank">📅 11:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435285">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIYt1pUtkvtOCsvGMdR69UXCMQHB-xMR-NYDAIcKMpmO9NcTNqxhsviv25VY8SDAWFlubRUrs8HsoqxQ4UcoTp8sDBx7jkibQ1Upgd1Bz4Miltz3gWxayATa0PXR1MZw01FgOGBDfku_WHg6baMZCWa3wtKlZsxF4vjFFzzuD3uKNpB-LnQjHlKBoK-oX2W9tqTcNsJH0sPUp6tI_AXOKJYXrLr5HSFU9xF9rIfxGIprzSbVKt8GMkB5pa6oCd7k4UnX-ullNzXA_VQ_P_FlFtn_DQVPhPpOJlnRJpb1acAYDeyGDCc2Tag2oPK9uaqbrIE_l_HvXUN7K-ODPUDc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUsqcxO8J4HTBMa8wMdtu_D51z-23zaz4W7soBRnZ75IhvdgGyrjpN8xAI2lB0KPVqYqWcgRl1xV_F-gDdVMck2r48T7f7XmZxSk_Vi1Sk5e9k5PSihrm_vA2vTUlnIAziBtnqZ6CmUsnzvdu3-eDhWvmJCDMhpUV7gXHtv64w2NlDxU4Z-Qq0SmpNkIIFOa4v8rN32jT04mMqIH_QaN1n4gK9GWw9EcUECOnuFEW9-BfmUpq_4NTfKRi6IfBqTakOJR_z7AxYCbm37uwlktf5dSztWFMUUDqUF6P5453OZ9GDL-fQnXNX9MwriWi4X2ilPLXxBWFjXmqqUJorq8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNW63pcrNYORXgbxiJ9k12YpJgvDrCvQCRHH2XCUHgGDwi_WsKayLJ_j4n8qaPUoev0-r2go2cCIyB74VHPWFF50dA9K6yiwcYqHfr-xCFD_3uoxYihmOA720AX2qHveeRzxy2LKveyjwaP9L9QhHnlCVAYM_mBR9rPjcQq0wrsGywcrBHwoy2dpfbY5H3bSfftl4ovTBRmv75erHbSF3K3hojbVcbYA2vWk6sGMJDGO3-3v0Fs4pyiWSaFUW18cTFLONff6kSiJsPlMXDUS1dihRj3jVd9QuE9Yx5TE5IusZ5ZPjklamnj1XkfFUHxXnHFrGORnB0Oz1HuSIMIQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNcM1OFMGXrqEE8mmK-eIPZ5kVjQZZe8M-7Ne5eN_5FwOuGhbhl2KBCfY3BqmepHGrlo4NTquSEPElvQekgF3A7-x3wN3gNlwJaciuoE7RczY2Nhno2UTVAl2rqOpoY_33q0IJzYMNr6CnYLERhNGPxgmE0R9etb1W0e23LvUt-L2HtOt2X25q42wVYyWGe_Cd9Ew6qTM3Ommr3lbVRdgOtYkrR9cNUxZfNW12oS1xxIm5xVxNV5CW7b3GXGgoMjt63eLNxd3VW-VrbUNuxcRmHBwAE_R9bs9PBBjyuqV1lEfIEm6AH-S8JNY4Uhj6cdu1Pa9E1CyKNdsNWwC4rZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDoqzLbBxAJtdAWRQ2dfoXnC-gFiwlt2jeUpaLN8JLZ38g3dz9Zo3GAoHrfJtE4_CF1_uem69t4_LsmYF2kqvBKLlPzctet3wNyFWcqUxsHHD_PWczqSfOjiNaY2a4YpACkdLyMYtG2cDI_nsLsEegFmQn1xpU-20NhpVVFxLb6i4HYHVvvztMBAutHsO_VI1K-D2-gfGV_57ajrj2cvOenxAmeoYPGgTvq2X49BRWGEXGsKvTXU1_37C5cNIQ19VsiE5rfvBF7-dWVNjbGJVtJiwflmZUam8dv_9PUNP3I8xJfL99CqDVKZmEInXZdme08OIWMHFmLSpnChhzXUHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
انتشار فهرستی از وطن‌فروشان خارج‌نشین توسط گروه علاج
🔹
براساس اعلام گروه علاج این افراد از حملات رئیس‌جمهور آمریکا به ایران تشکر کرده و نسبت به جان باختن برخی هموطنان ابراز شادمانی کرده‌اند.
🔹
علاج خواستار اقداماتی از جمله توقیف اموال، تعلیق خدمات کنسولی و سلب تابعیت این افراد شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/farsna/435285" target="_blank">📅 11:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435284">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR0CEnlLZJ1tXmSr1qI4GFNhvpEXP-BX18jIhPHpOnNzuSHzg11cvI5n0LCfrcbh_Pl81vzerX8IYlvY7MES7SRT5wr1HqUVFM2HLzNnpGmgzSr54-laWV49mOnG2I9Ij_krxwDtzi8-GPkB7kc6YgN27UJhdfZ006u37zs4ft4LbU5wPexYRzO6jMpkHzf0-nsimiToBoRJ9b_6jpiLVZVHFgI-srQfFYKwjUHDCPnya2PAwVXGiehpOiCJC-RhIg6KGi1AZaR6rTSPkvsAz1kVlp1qm2XD53UnxqFej_IO6hzbeFmYmuUjvJvxVmyIyzdn29y-SaOXEQA7Ma2f_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آمار ۴۰ روز جنایات آمریکا و اسرائیل در ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/435284" target="_blank">📅 11:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435283">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c18fec5dd.mp4?token=QangHcAaCr87dYh8lwqxftGKw2n4bg4NqL9tDC_bOhhJuj3PLNkMhex8q6Q520pTIKJ7rb-cmriRkWjiyQEmrFhvnyTDBwHbQrhGII-S2fTZMCWzUtAWHgAa2nYqEsgU-kCFU1uRwg8lvLmeSHGYi2VgxuD3AfR3fvpM_cVkRVsWeDGS8Xs5RTbUuCb3vWaZ39OoXx2XZ5b-n2co192L1phtiUJakOYNpZpAz4v4aHBaJFUmNu9pYLneJhY-360QX4degwB9_FCXbKWJ5W2KYiLl8U9uT1hnPacKaLF8ThH5lDTjEBDCOe4KBIVZETHGt2ndwahmhco3v6TuEAfbBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c18fec5dd.mp4?token=QangHcAaCr87dYh8lwqxftGKw2n4bg4NqL9tDC_bOhhJuj3PLNkMhex8q6Q520pTIKJ7rb-cmriRkWjiyQEmrFhvnyTDBwHbQrhGII-S2fTZMCWzUtAWHgAa2nYqEsgU-kCFU1uRwg8lvLmeSHGYi2VgxuD3AfR3fvpM_cVkRVsWeDGS8Xs5RTbUuCb3vWaZ39OoXx2XZ5b-n2co192L1phtiUJakOYNpZpAz4v4aHBaJFUmNu9pYLneJhY-360QX4degwB9_FCXbKWJ5W2KYiLl8U9uT1hnPacKaLF8ThH5lDTjEBDCOe4KBIVZETHGt2ndwahmhco3v6TuEAfbBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسماعیلی: رهبر شهید تقریباً همۀ فیلم‌های مطرح کشور را می‌دیدند
🔹
وزیر ارشاد دولت سیزدهم: رهبر شهید انقلاب تقریباً همۀ فیلم‌های مطرح داخل کشور را وقت می‌گذاشتند و تماشا می‌کردند.
🔹
به‌عنوان نمونه، پس از برگزاری جشنواره‌های فجر، گزارش‌ها جمع‌بندی و از دفتر رهبری توصیه‌های ایشان ابلاغ می‌شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farsna/435283" target="_blank">📅 11:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435282">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e83703317f.mp4?token=WQP-I9LXSB2Jh6-sv85VeY0yF0fee-54I4AFqg35yDfzR_lX14d9O6DTBwRQWdVXxZJoS1Shrmz7yciG-lq_J0TV2LJ0epWD_7OIPa8M5GUlWaujIoT7K-NZERsTXr9EG-j43_O6c2MzDj-keWCUCcivp6gKXVLovHgOJ7u5Fj77blHbpHk6xAYcXmXPVe2AhkuFSKbjA460lkchTkf2vl_lfdVc3puboQHCimE_qeb9XIt06wCI8cYh-h3QysVRvTkkR09962nM0gkNwNxzUQ8E8RgIkofMlrVCrA9pVcY17dcrU1-iSP9N_iqtQ9IhaVtGbvR0CrCP3IM5D0wKOmecufu4aF4P8_uUYGF568VlXs8GcH1g7LMJSlV_MWNVFb9uFMavjY8fu5SwabpclRta37umfTzDzXJzI6ho_kEGkmLBmocr2FldxXF20SiI4JkM-GtuqP9nlw25RX8GUtSnfXVpYxA4n8LyLiqoIxn7AIZVYsJBUQA7GUNs8plHqnDYMKCocAPMiveTiOqHSFTRve9A_nmWto4XPVlusLLVUvcbhAmv6ZgmrkwaDBJo1VqnauGtOR0I5i2dmpa1EPSVE1YrcWyB2fV_mHGGhz6Mv0FV9WJiftALS85dzYDyFM90DysI-LgWKbIbKYNhvlswXbjTl5tdgQrVbVLAq60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e83703317f.mp4?token=WQP-I9LXSB2Jh6-sv85VeY0yF0fee-54I4AFqg35yDfzR_lX14d9O6DTBwRQWdVXxZJoS1Shrmz7yciG-lq_J0TV2LJ0epWD_7OIPa8M5GUlWaujIoT7K-NZERsTXr9EG-j43_O6c2MzDj-keWCUCcivp6gKXVLovHgOJ7u5Fj77blHbpHk6xAYcXmXPVe2AhkuFSKbjA460lkchTkf2vl_lfdVc3puboQHCimE_qeb9XIt06wCI8cYh-h3QysVRvTkkR09962nM0gkNwNxzUQ8E8RgIkofMlrVCrA9pVcY17dcrU1-iSP9N_iqtQ9IhaVtGbvR0CrCP3IM5D0wKOmecufu4aF4P8_uUYGF568VlXs8GcH1g7LMJSlV_MWNVFb9uFMavjY8fu5SwabpclRta37umfTzDzXJzI6ho_kEGkmLBmocr2FldxXF20SiI4JkM-GtuqP9nlw25RX8GUtSnfXVpYxA4n8LyLiqoIxn7AIZVYsJBUQA7GUNs8plHqnDYMKCocAPMiveTiOqHSFTRve9A_nmWto4XPVlusLLVUvcbhAmv6ZgmrkwaDBJo1VqnauGtOR0I5i2dmpa1EPSVE1YrcWyB2fV_mHGGhz6Mv0FV9WJiftALS85dzYDyFM90DysI-LgWKbIbKYNhvlswXbjTl5tdgQrVbVLAq60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی دیگر از لگو انیمیشن ایرانی؛ تاریخ واقعی را اینجا پیدا کنید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farsna/435282" target="_blank">📅 10:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435275">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3c4G78Tf_unWa6_YYkuyJ9dblNmi3J4rFDAWTKIR6YtRwQBEHhdGeMy4NrmX98tN4Vd1HnJR1_P6K_lo0jCmw9JIRCk0CtgWb1abUWsQqm4c6rccVf9gciDJHG3JXmMUh276itCFjdRjdCIkqU1JgDXi7eqF1x8sp_V3PzvPGZNqf3YO2LFDCmvva9YIz4Ff6Jy0aw1PA6Fc3tzyWnTyU0GoAe3DBFchGAuZi5Cm8RRzT4h3fwo9En4gotp4JTeNkTLdYwl-N76hIYCbJemUTIP0kXtQ0CowgbLeym14F5OiyR3mtDCCVgkz_96QVgyPoe20mzcbP2m3sGDNVyRZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bt4rQCc8DSSMimvoYsI4AqMTepzyZFOg0JnjdUWlbJd4AfCAFhYnj9sUZSJTPbsHWHWt_Xxk7S1cvRujQOIoRIApKW3JwOK_gin9sY9Re9CsGGwMUN7MNQPXqtbXazc3A_F_yaJvF7IOECQQlaHAzjxi1IlMggmMTSkDZh1lgwnUyjYblgvH3W7qs7yww-6KVV5B3o-re5YYMwGb4Dv47Kiu6wTlIdkONTSvctnXg-bu43tocwljaEiy-WDSmC7Efd07e9A5IW9RdmZv-nTO6qzjxKylt_NfVmVp1ZYj1gOTteZYxrxDkBfWni_toEdSKNXtnkFO0bw22lKeE3vLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qe6eqPB7euy-0TUjCHHDgLUGvSm8v8yr1MhV4AKQHgHILc0QuyNqfkV7h10vgTA4JDfDn1MsNl6TnoxiPqm-Kq8E64mpt87RJTT2dcV_xPC5hQxX_0WH2Dd5g8uOoI1OJ1dNMfs8egT_ZIUI_PXriWDuZG7tAiVX3JPvbtYGgiE37euMoxpj7KVIVzsaqSggoeRhE2en0UTOOFXUxFr7myIds-Q5SlFCMbuwmMQZsDkzcxbiuL3ioUUlNoIAYoYTVveHeh9Wm7bXvxrTSOdglzv-n4Mt2G7ANqryaycUv_LKtPY0SyJTQ13ymfptg7AfvqRLjN5M_mD-tvnYu6D28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkxRvO75movTjeOOqmSfEsdJTZjGwJGCo-JvXsRn-nUuvBoaWpiHNAon-pMhv6i90gUFF3A7N4g4s4ZN5MOYFhJYaEVhP82JT1mwXIOFCJnfgKHdjz0jKNg0ZVNP1EbTwOiwhIZbbzV-bcyUBx5u8wTzAXK1ka9MfpR98cdXnVS7gBgnOa2Q27jeRmxmIQxPyBswVwvF-kGcamZPz-WHEXg_EmHsAvd9dOIibgxAgq7L_MqGdXryfLZuQQD9u2ozPOTvoFmUB2XTOaUBgsFDx-Omymf6X8PCBKMG1gdPxPEbJG21OfNv37t2RARk3ycyDTNhl-vh523N6ClsBApDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jz77DkEqNa7YrzOVbFLId6aS4MUvtobEkuwgiGhne7oRUDXZpV4kHf7JxzAgY_a1L49TycRcEfMHIiw-30E5is6a9L7cNBg2pRptQTtHAH8eqZEKpzE18Spf1qWs5jxlOaPx43oLb5APd6ibF5eaDdGydn8AP-avNPznLlh28WzdLyFrc_eFffxKXSrXnFGqx-3ibk5kaf3PU-hvYXx1J9YQ_tcHmb6duxJxZghxOcNQqttXcufixWO5uS7s4CbUQ_Cko8hmOIa-NBRWCALmoZSuDweFluS0d_v4CWs02ipQg7qLYSExz9Tyqa1eVG5cHRuwX8vxuSofC2NHuJTsSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeGHUjepnq1C3ILcCLVgGc-ygp8xI-o-1Jbs6FosdtaP_CF5y36G8NOLRe7fyC-FC7GPxlYvhmTfnDjA9JVWdy_ncOYIcoRPGXR5EF3HPgE0qMa2ChjcPRhbTR0h0BdHHxRR8IbMG-tY0mWLsPe6q8rsorLU-7Jd8E4S7c0ivgYvjhow_W-9L3kxNNpGMHT-X8Fiolhv5ZXiVok67nbD7sfdiqyfJl1MUS1HLP6uLgoW-njpb4-ZAGXSL1AVPmP9OBBhu4i3_TPipFG3N2ryutLeS9M4eIl4muoLUNSyG_7-duybjLdf3LrfvmEDI-IRIN5agEkQjPMCgKdw9nSolQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQGLcY8NRlxBjakxcZIAxbpvFHMy69VDTlFOi6fxDpAoBeM3nbmHeqDkXiIwUlTElvqKQERQlTFvFhHdhuTHkiC960s8qs0wBZha_nXuZS577MMKy6hw_9AE8eNHTgJxo1DB4t6NnOmCNkJLYjF2qQu43-rW7j3JcI7NC6Lkug1PQGQ5RQTUNP3sYvtsEPP9bN-HNfiZgd5gU6-K6DGTnqkj6VH8X1q8Uq_E0tUj0zXEQRdIFQ1IrXTzaxGco8q1uQ80wy3_m-o1kJQCe9vUUBjoqL2mJVjEqanlD8Zx6f6RrgUnwdefvbswBwKapU3qJ1g5XFgL90yVKzM3A3Lpxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع دوقلوهای شیرازی در هفتادوسومین شب اقتدار
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/435275" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435274">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">کلانتری: رضا کیانیان از ژاپن پولی نگرفته است
🔹
رئیس سابق سازمان محیط‌زیست در گفت‌وگو با فارس: رضا کیانیان پولی از جایکا نگرفته که به من بدهد، اگر گرفته اثبات کند.
🔹
اصلا او از جایگاه جایکا اطلاعی ندارد و آنها پول به فرد نمی‌دهند، خواستم شکایت کنم اما دیدم از روی بی‌اطلاعی این حرف‌ها را می‌گوید و یا شاید ‌دنبال بزرگ کردن خودش است.
🔸
رضا کیانیان، بازیگر سینما پیش‌تر اعلام کرده: سازمان ملل از طریق دولت ژاپن سه میلیون دلار( معادل هزینۀ آبیاری بارانی یک میلیون هکتار) به‌ حساب او واریز کرده و او این مبلغ را به عیسی کلانتری تحویل داده اما از سرنوشت این پول بی‌اطلاع است.
@farseconomy
-
Link</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/farsna/435274" target="_blank">📅 10:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435273">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0KuTmnC9-fKd5e2GRMOR4fDbP_GTfD0vgNhJBhkts-Hn8ySq1pugbBXJQ3lw_Z5jxZXapbumThToWurzvjWUnMh4G6wtMjEhnH9L01mB-CgegtaOPsqKx_NAsEKmbQiqnqeC4E-MjjtjPOw_l-Pz-sCzpKZNp5RE4LNpj7Rl8_8w7yTkkWm9ZdpvwtTDUWVN0i2fzk0W5yTn_nsOAOuumSqyHYgbBW6DkIlfPYXLGsre36n0vwCERlhHrzFVFfGTRh0_zRlDbhI7UqlTFJQIemtt0h_ynj0rYYYFy1bFK9JiruUH659jpWfwToVlXiTqBkCv2rZyopvzRk8f8eIPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی فوتبال از میدان انقلاب به جام جهانی بدرقه می‌شود
🔹
معاون امنیتی استانداری تهران: در حمایت از تیم ملی فوتبال کشورمان برای حضور در بازی‌های جام جهانی، آیین بدرقه چهارشنبه‌شب ۲۳ اردیبهشت همزمان با اجتماع ملت غیور ایران در میدان انقلاب اسلامی برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/435273" target="_blank">📅 10:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435272">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5acc6517.mp4?token=SjdfP36TO0rzcLeA5OvyrDUKjNdJKbQCiY4_A3my1MHpKwznNkuQ6upa8Q5HhCGkrT9OjKH6i6yYxp73C2DIcvMmOO4aZKY0FF7nEaes1b0QZ2m3dzJJYah5dERZEBr4nFHqteWQKrhR2fJ2rEqHtVbv33ciPYjU0oYUiWv1gR5YxGxVMttciVWUHvdGHzkLVzVn_JlP1hckZ_JIEjKKU_KCOwl2rvHt_AFlqJPShD7I43IPmZuKwYvYcMtrS334et_tL35lR7wk8ZcBUpeSjSMqablEBTFwVwJMOCEmaY306zfHr9rYDg4hU3pFh9GQAjepg7P6XliHc4QiPykz8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5acc6517.mp4?token=SjdfP36TO0rzcLeA5OvyrDUKjNdJKbQCiY4_A3my1MHpKwznNkuQ6upa8Q5HhCGkrT9OjKH6i6yYxp73C2DIcvMmOO4aZKY0FF7nEaes1b0QZ2m3dzJJYah5dERZEBr4nFHqteWQKrhR2fJ2rEqHtVbv33ciPYjU0oYUiWv1gR5YxGxVMttciVWUHvdGHzkLVzVn_JlP1hckZ_JIEjKKU_KCOwl2rvHt_AFlqJPShD7I43IPmZuKwYvYcMtrS334et_tL35lR7wk8ZcBUpeSjSMqablEBTFwVwJMOCEmaY306zfHr9rYDg4hU3pFh9GQAjepg7P6XliHc4QiPykz8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احسان افرشته، جاسوس موساد اعدام شد
🔹
احسان افرشته، فرزند مصطفی که به اتهام جاسوسی و همکاری اطلاعاتی به نفع رژیم صهیونیستی بازداشت و محاکمه شده بود پس از طی فرآیند کامل آیین دادرسی کیفری و تایید و ابرام حکم در دیوان عالی کشور بامداد امروز به سزای اعمالش رسید…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/435272" target="_blank">📅 10:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435271">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccj6ZheJYmEE6_vLx7tqSnr3wUpnYGG6TDAfxHAp1aNCO3Giv7JfSUx9_dGW2CVDyhQK1C8YIDSw0MdS4UInCUqgiMRpkSTm8Hoj2jlBPWMErqyAT5N6iX3dpFciCjCKO_HtlcqGxkhLs4Uk0Rd15b6EZOoOW9l3PmRwgjqWpFGsINEJYMZUCGgB94AAxWtQ7SR_RREDIV3ELx4VzgWs8fk7zE64sTrQQqU7mZrLX9EJW9WLv7P7NVAYl5TQUut_Yji3nxe9VRTnHjhlLWKZXMSy4tJJBRKslZchxmicTjUp9Ov4owJs80odxxfqZFIRa1CnIsm6T1maociXo-KAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ ماموریت ویژۀ رئیس‌جمهور به معاون اول در سِمت جدید
🔹
پزشکیان نظر به ضرورت فوری استقرار حکمرانی یکپارچه، منسجم و کارآمد در فضای مجازی عارف را با حفظ سمت به‌عنوان رئیس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب کرد.
🔹
رئیس‌جمهور همچنین «تدوین و اجرای نقشۀ راه جامع تحول در حکمرانی فضای مجازی»، «بازآرایی ساختارهای تصمیم‌سازی و تصمیم‌گیری از جمله ساماندهی و ارتقای کارآمدی دبیرخانه شورای‌عالی و مرکز ملی فضای مجازی» و نیز «استقرار نظام نظارت راهبردی و پایش مستمر عملکرد دستگاه‌ها در این حوزه» را از جمله مأموریت‌های محوله به عارف در این سمت برشمرده است.
🔹
در حکم پزشکیان آمده: کلیۀ وزارتخانه‌ها، دستگاه‌های اجرایی، نهادها و سازمان‌های عمومی و حاکمیتی، موظف به همکاری کامل و مؤثر با این ستاد در چارچوب قوانین و مقررات و اجرای دقیق هماهنگی‌ها و تصمیمات ابلاغی می‌باشند.
@Farsna</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/435271" target="_blank">📅 10:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435264">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-gojYoXcgc_1dgnzNq2ff4xGt0hBnD8KMPrR9x2f3Wih1J6d4d8CjktqrEt2nnT7VScOyLJjZyYiNh1K2HVbtyyjPYMWRrwx0LbMET4xAYxjCgo_sDB3lqfB_83fOnQ8fu_sgpd1bMUiS3IZC_OTcAp19ll6MHKn1UzAHnO6--kprkPswOZ4GiBXaq-DlXdtB3KcGa5zf5Jb3U8zZdrHC7vWwJeu43vL7quMxQFOuLiNs1jfe8h-a7FED0uvkoANBBn73uyWEc0141Qpcdvxkd34MUuVrNsZd8DBq-pZjF-QhDqHpZzk1M69p0ncH0AOmkC1WW8LWyLP4W9MWZtOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Md4Pd8u65uZs3ZKUZaLZRnmyTnhLC0NwehHtLX6h8t3ieAmz2eB6p0C7roz5UcNU22pGtSwYW4_dxvUYies5gkLCCeZ9oyCFeRCAUrNCF5SRARUYydgO-8skBKEnjly_S2coOulaTHMjAzcsFdF7xRSofZznqUyLZlIR5xykCuxf2X_EdbpDFI5IIxVqvf62dCxfu0gmkr1MIDyB4FtG_7hiboKTrzGQPY_zyZy3kO-uhU83dLmnEO3ZeDddmmomKAydqyi9YpHzHOeh_0NiQVu7WvYiGaT9TGrjGLbPQYU2aHGrc7PF55412vQC-ELoumCw7ZI-iHVJ2P5_nnU6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NOvXGBl3JGimByHtySuLAZm_4FYnKN6lPxxejt33gOdx6kxLOjHEuuAxDsy8xx69InGn9AMj1wrkAEyFa1aw8WWTvzkp4vhrBg66NJnUoCI7IhJDj52EsrrG77ndxpqFu-HzY8klLLHUDpTCxja1vLE-YlSb0NvZpdGsHJHQln9NJw3mc76KxBxSQ_GRxhs955p-CcZaHOc5qSXO5luQOZGUMMcRRFUyPj-CopXnfhcMCSPOdH2Jm9FLq2eLkn4NDnHtMZ5BwJ1MKh7yqznuLL2IDaMAZbXD2xJG1J0TKdqGEbs6Uf-P7kbb04bxIQaiXCSU61F001-B-SzN6PhN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nWqOf3gmYJC5PLO1ckCHo7gRT9vgn-xxBrFS5-jEFI3tC7WfI-KgaRnhRsZ_3tBYmC65tWOoq1ViIenG5-0My7_86l2pTJ11ks_wUzd1HQtUg-cAq-dP-L6JgJfzGju2S8YqYN0gHqTQLE3X9OD1D4it0CfeK0XArH65V-z3BgXb8fD-SetEjku92FN8SxTU88DuH30lA-vXZw3nWLjK-AdiXqnzz-2qZhWBbh02XNi1ybRVheHr2r-zGzpHqGKSJTyKXqB1YnamXRypfVY_wVBoROzO2c4bpy3lgZ7P5-O0qKwPQYPxG0GxPbvZaHFSIFQiiWt_nt3MmtRCpSme8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7-fp1Y8vDVyihkYY3VVAuMB-66T5szHZv5jErmsik2eubZODUYlzUHSpIzVTIklmoLkRzUtL2HCW9Bx9mRXKPDbUQgqMkJxX-48VaOLCqXRa7E7D_DcHlbqc_Yjhi_0UWbdNzxMCQR1I5jPrCBtHi6loPvFg7xOIXbr6Lsi70M8hCh03kMLaM3vNhy5VKnIVQYCJPn_6Ts-AUNjQSXv-6za4TFnLMht5uUeRVWiS7-j9Jb1tjDyuP62Tx63BzeWgbKSqSxlWhodi0tDNjm9Dsr1G0L0wx8WWp8J1Guj29pBlWwgh5v9FxpQK_isdpN0B9BKGDVK4XA-YpcaNDYH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDwm49O66_SggFQCMC--BZeIUN7z1gDKHEM9lRouQoXd6nEnaStkMkEjU9UScME7Am-IMvMuVaJoU55kKyEiJSl_odoZMeCoITVrOOhfqbb04wzlW_8nwGQmU9s1NJjHdIo64WlgECsmZSUACMf2KxyaFige59TowSJiCh-1-OfXDEpKtG6IbFj5Vvo31gBh_GbjhyOBO2mTCH3_2RvQvIhNEWNBQuuJpzom-YUZnZdUts8-sVzjS9Qn9uZP6uhigZClTUiBxzToFFk3C-eVwQMB6kdhIwcgT_-UPxzY9avXc-KUQ1PSBznDeHwy8clAroPOkA1RBt329v015cHQ8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور اعضای تیم ملی کشتی آزاد در چایخانۀ امام رضا (ع)
@Farsna</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/435264" target="_blank">📅 09:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435263">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
ویژه برنامۀ سپاه تهران برای گرامیداشت شهدا
🔹
معاون فرهنگی سپاه محمد رسول‌‌الله تهران: در میادین برنامه‌ریزی انجام داده‌ایم که براساس آن، هر شب به‌نام یک شهید تمثالش در تمامی میادین نصب می‌شود.
🔹
در میادین سیرۀ زندگی شهید، اقداماتی که انجام داده و دستاوردهایی که به‌دست آورده، برای مردم بیان خواهد شد.
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/435263" target="_blank">📅 09:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435262">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcba5805d.mp4?token=NRJRx1IQenAbAtE2TrvY8UbzMC1GTa6SB8kJVb2WO2qkL5WgkPeCqhwFaxhAiIQdIJG_UDqCU5ZoUvGqmuQ3kTqVGIp98fNT2ThkH8Z0XayeL_2uRLG2pnkozoNxHEDaQ2-gbu40fAG96uyqW2UAL8XWP0kTfIl-7WZ_AM_eFk0kyfxHzuf8tjl_0ml_B6vYZIYSAg0O8vD9n35L1Pg3m04OG0pq1x-kKiKIU6s2Ol_H47TLjCXOEwtXSeFn6tTjsz3FEdjsek_9YuBNKUW8gSZH1c0Fc1tlVeFymplWoSFZ_OH34eWszfhNJZJtst2jftsXI_TveRfSDTFvADFtwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcba5805d.mp4?token=NRJRx1IQenAbAtE2TrvY8UbzMC1GTa6SB8kJVb2WO2qkL5WgkPeCqhwFaxhAiIQdIJG_UDqCU5ZoUvGqmuQ3kTqVGIp98fNT2ThkH8Z0XayeL_2uRLG2pnkozoNxHEDaQ2-gbu40fAG96uyqW2UAL8XWP0kTfIl-7WZ_AM_eFk0kyfxHzuf8tjl_0ml_B6vYZIYSAg0O8vD9n35L1Pg3m04OG0pq1x-kKiKIU6s2Ol_H47TLjCXOEwtXSeFn6tTjsz3FEdjsek_9YuBNKUW8gSZH1c0Fc1tlVeFymplWoSFZ_OH34eWszfhNJZJtst2jftsXI_TveRfSDTFvADFtwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد زنی در صورت پهلوی در واشنگتن: شرم بر شما
🔹
یک زن معترض به جنگ آمریکا علیه ایران در جریان نشست روز گذشته نشریه آمریکایی پولتیکو و کارخانه اسلحه‌سازی لاکهید در واشنگتن، که رضا پهلوی در آن سخنرانی می‌کرد، فریاد زد «شرم بر شما!»
🔹
وی در حالیکه فریاد می‌زد، خطاب به پهلوی گفت «شما کجا بودید وقتی مردم ما داشتند فرزندانشان را از زیر آوار بمب‌هایی که شما به کشورمان دعوت کرده‌اید بیرون می‌کشیدند؟ چطور می‌توانید بگویید «مردم من! ایران من!» و بعد‌ آنها را دعوت به بمباران مردم کنید؟ شرم بر شما!»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/435262" target="_blank">📅 08:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435256">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4-iRZXcBpTuJNClaT2S4fcY9dC73DlNnWxxhvCHLojhpv_a63_lKuSnnmdpedsdUuUj5DvWtZ10txvWsVMBKRx8n-TWht9rrMD93co1Y8_9jodgk8fnP0JE--lGTlWNBNUi36_tR1CrstWsc22yL2asxcu26v4Z5sAHsYi1BQZSTMs3z1Tb0sDFlz7CwJ7xoYS3rcNJRRJnDlBUDNhLi5nNAiraRr7n3jdCBnrSjrqMasliZw0QHO8SHbWOdijvpOKxU3xuyYU3Px8i2WNzHXPCbPR-DpyM2I57KBc4zViUKUziQYfDkkoE3yEsz31rRRtu2Wsb7VYhmP2CcIVkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhNmHbh_AKIa9Rn0g8vyMMLU8c5xZFcG2iESANsZG41Sgaaz8ux7sqONuwoUQKXHjGncnWUYZ4dBr-vZ6MurL_5aNcCruamlZAsQq-WNHoUDhr4tU8Drfqjj0bmcrQ4jHDBUCyZZsa4zkns4SWtifbSxU4MrTCI4PJ50SlYLZ188NVlIkXNX2qsLE_l0U5cS3lGHOuLpk8e9Wlz_JHrGMX7zB4SmwMpUNebZBFBK6YjaUpgugclLDuERbil6YhkIWiSuYPHkoC3qForDU8qBDzLw1bE80xcP5KaQY2BPc2jDxp6nklRN6QlyyBD_St-aryQgRWKzGLiRkVU1DrUN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-3dZeiD63yDSQQxVXdZKiHT7tddx0SuUkEQ9rthOcGOqlE4EVE4-Gitn2C13hJ0xJ5JYl1huI1ZQ8KP3jybumgs040r7XTc0a-Xgn8r8lFTeD5EzIvSLdqtHDC4l2yyHz_3kqNEGLyQGxn6KiSXFYzNTOq5Z7m1Aaid2u43Bs-BkBnNZ1Y5j6CHkDUW3wy95VsVHfd1bGbRH920_mvKpZwx2Vkg_vKbKi7dduPe-XgK7J8yG8z6pPnJDj6K6Pst6E-JIMsCLecc_wDaXq4ciQKQS-7nRQRRMDHmXm17NxMFRyH8t3d-tQg0AhG8vI-PDiScfrw-Q3zCkDs5mDj2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYj2ACSJgLY0I_YbVck3s8RB0jKzxD3mlWpVNwAsA_bFdpfbBtyeRjT8bk_ibqP6nDWArB6vDDrpxxZ-pLOvtSUIn5nXbaGA7LcNQ8p_-2KTP7HwVhHk3NVgqftLNgf49MG4a4_gNiGIM6Xx6J9GNsV16cMkEKNLdkHASok3A3dG7oFA6ix2o9UNZUeHRebsrj93ZxRazuq9XH3obPoKnHuYyRahY9GL79xS-pFMb338pmfsI7XO9-DEiU0hvpILuYiQp32g0HDCxxueLTKXWlNTyt0NSwqF-kJmr7t9dU8k8r9tKrdVL7k5Sabo8z3Xn4kslZiv6kQ6uoeT9StwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpSz-Jq_-9H5YoMiAyzCLkmUVMvIrs5-NM8p-seA3I2H8xdlw2h9OfLTxzh82DqLV_E5NGC8Kj-7a4kyv_DvJCCEf2TCiE_eypRT5p9oUAuW8YIwF2pioEwBMT8PYHL_7p6pdsR-ycqd1AZ8cGnltNtWJdP0uIqBZAVHQJzaG2Lv-dfToymmzq8bT8LpQGTH6qJTnmqh9KwLeRXJQdxkvDsaaTv8myXOZV14ftZ2udYYdh3B0JX9CyJ1Gg7M___20XLAYerYrII56pgV9yn1fPnI3bbEqoft4Y9bEOawqLmnufiCZIQHbzN2xmfmkqxtewBffFuGbI__ubO_F_oFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdEsOr6u7_LZanSOhRU-mGGbMsJRJvXkB_9g4evGkb915Ekz1GUF2jFLFGNvUTYdeg0jbjsLfgsiutKrCCmkFEm1kbp8WDB_zce32j8gZn7Iwzp8EOVx-a2xErIkQMuP7cdnvJqhFkBCb59h2hATcxBQSnOZuHwLSNt1hDYw-rv625Afedbssq1u50JPQdNe_cjNYEtJYzSKkYI8cadQHPcbV4aDvOPZ3Wz-OgsIq_-860CTiS6hxYINT4QykF017i3vcjV8cmVZWH6x4XnvDBXqvvcN2Gz25kxHpGIvUVbjsXrNk2hARbvYweNLCjS4o7jbIV2o_JC3u49zq0hkHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احسان افرشته، جاسوس موساد اعدام شد
🔹
احسان افرشته، فرزند مصطفی که به اتهام جاسوسی و همکاری اطلاعاتی به نفع رژیم صهیونیستی بازداشت و محاکمه شده بود پس از طی فرآیند کامل آیین دادرسی کیفری و تایید و ابرام حکم در دیوان عالی کشور بامداد امروز به سزای اعمالش رسید و به دار مجازات آویخته شد.
🔹
او از بدو ارتباط با اولین افسر موساد چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند. افرشته در ابتدا در پوشش راننده تاکسی اینترنتی دستورات افسران موساد را اجرا می‌کرد.
🔹
افرشته در طول همکاری با رژیم صهیونیستی به زبان‌های انگلیسی، فرانسه و عبری مسلط شده و نام سازمانی او نزد سرویس موساد «جیمز» بوده است.
🔹
محکوم در طول همکاری خود با موساد حداقل ماهانه ۴ الی ۵ پست الکترونیک فارغ از تماس‌های صوتی و... با افسران اطلاعاتی موساد داشته و بیش از ۳۰۰ پیام بین آنها رد و بدل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/435256" target="_blank">📅 08:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435255">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSb25O97mVisVf6nq02ok2xSkoXpEmW3VkuBfQmhDmkXgUGP9zds-fQA9Hw0gkQrLACF3w3Gz-k-sC_6YdOpsv3da9rzpCQzLkQMOoVk9-M7j6i1PsT2-d0jttl2J92oWj_CsOVGU8BwhhTR8vlYS9h48eAefTmFTPo6u1H1Q-eyyZ-DEtuyNqOXLwhmm0QCg1I6xTHki0ZMdlM0uS49viYNxr5zQ8w852OegU-8lbVJLeBBQmp5Z01NYXgN529I9F8kSDBENf6CUJ16h0ulogNpV-S3ix3d_tahpREc2xB4EMXIXQ8jgs-R4WGwoVNGAIAyz_Diqip-fUjsSn7A5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظرفیت ۳۰ میلیون تنی که محاصره را دور می‌زند
🔹
در حالی که تنگۀ هرمز به گلوگاه تحریم‌های آمریکایی تبدیل شده، دریای خزر به خط مقدم تاب‌آوری اقتصادی ایران بدل شده است.
🔹
استاندار گیلان می‌گوید که بنادر شمالی ظرفیت واردات ۳۰ میلیون تن کالای اساسی را دارند؛ رقمی که معادل کل نیاز وارداتی کشور در سال گذشته است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/435255" target="_blank">📅 07:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435254">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیش‌بینی رگبار و رعدوبرق در ۱۸ استان
🔹
هواشناسی: امروز چهارشنبه در برخی مناطق استان‌های آذربایجان شرقی، آذربایجان غربی، اردبیل، گیلان، مازندران، ارتفاعات گلستان و سمنان، کردستان، زنجان، قزوین، البرز، تهران، قم، همدان، مرکزی و برخی نقاط واقع در جنوب خراسان رضوی، شمال خراسان جنوبی و شرق یزد، رگبار و رعدوبرق و وزش باد شدید موقت، گاهی همراه با گردوخاک و در نقاط مستعد بارش تگرگ پیش‌بینی می‌شود.
🔸
امروز آسمان تهران قسمتی نیمه ابری همراه با وزش باد، گاهی افزایش ابر، وزش باد شدید و رگبار و رعدوبرق است.
🔹
جمعه با ورود سامانۀ بارشی جدید از شمال‌غرب و غرب کشور، بارش در این مناطق آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/435254" target="_blank">📅 07:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435253">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
روایت مجری ثریا از مدافعان هرمز: در گرمایی که تحملش دشوار است، رزمندگان ما ۲۴ ساعته در جزیرۀ هرمز از وطن پاسداری می‌کنند
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/435253" target="_blank">📅 07:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435252">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmOyVAwA90vNZ--pvCaYhCfMCWZjg0TMe9mzR0hBk9F0CgSUitxXBFASodrThQW6XL7AdPwggmzxBatwlbHqF4tbPBAecXTm7GFylvt-3tpqqrl2HvWtriYPbV4QVEbnkAfdgYY7M459Xrxgl15Smhntp7aD8gR98QNksNWskk9APNjFx6UfRBpy2VVoqMs7--txy4oFqStw7AD5JO_OBi7i0q6cHQVODOUyQlZHYjp_qlE3HuOkohGgt15LDv-w8_gJLHnYINMjOwF8rx6F5pjiLQahpvhmu7sDFXB77v3O2pyP715PW75ndQALQGHSsAYrRiRCsQay3sNngG6o0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری تهران: انبار کالاهای اساسی تا ۶ ماه آینده پر است
🔹
معاون خدمات شهری: مردم اطمینان داشته باشند که با تأمین گسترده کالا در ۳۱۵ میدان میوه‌وتره‌بار، تا شش‌ماه آینده هیچ کمبودی در کالاهای اساسی نخواهیم داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/435252" target="_blank">📅 06:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435251">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXwno-A4gYg3yhBN_3VlqXbl8ctHfXdjYmtBCUH9y2YXqLfMsuXM1Y6HMjMpHyyRFkr8Oj9vVaN3Ig7bCSyFtU8ETcQgcRzzvipyjxrhf6483s5a11IVTSO3gf7SltAYD7YWk1n7ofjAilWkCDQqkoFy7XNFT8Y3c7p_Rfsb63gq6ebe_ikNIq86GyLjghSiR2-5-h6wT8nwhy6w9Stp0OOfibh8XwjB9_PTqbIaYMTCQ8cujuiYTawKv1d0eZG0EmaluoS_iHh2zRz8CCeS8hlBuUYJAZnlDF0-zrnu1Xb1wqZhg9HtkVELPKRtaDoJaTOraGlp4_bESyMI8FocHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف خبر توافقی مهم از سایت دولت آمریکا
🔹
وزارت بازرگانی آمریکا صفحه مربوط به توافق خود با شرکت‌های گوگل، مایکروسافت و ایکس‌ای‌آی برای آزمایش امنیتی مدل‌های جدید هوش مصنوعی را از وب‌سایت خود حذف کرده است.
🔹
لینکی که پیش‌تر جزئیات این همکاری را توضیح می‌داد، اکنون به صفحه «یافت نشد» هدایت می‌شود و بعداً به سایت «مرکز استانداردها و نوآوری هوش مصنوعی» منتقل شده است.
🔹
طبق این توافق که چند روز پیش اعلام شده بود، شرکت‌های فناوری قرار بود مدل‌های پیشرفته خود را پیش از عرضه عمومی در اختیار دولت قرار دهند تا از نظر خطرات و آسیب‌پذیری‌های امنیتی بررسی شوند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/435251" target="_blank">📅 06:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435250">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o93HJNhd73YuNh21LSNzMYb7UXMaTZyj2U6vq3No-pty-oFOSl3DF5XQnfd53aedDR5YWgYSMPR7dskpj4z0U5Q-XuMGp5Ep67XEhVL80keqB4ihvp_wbZazQYFhcOfrUTCyOOqp5QMa4o-9HOPmhL5Hgm3m-6Qz1khIPkANQ9s7EDJu-4T2mnqw2NCy9LmAJFjRgMIMQ15lz9JdtL-UCyMZs2TzhWDlVK9Cekha1eYrWA2OPW-Ref4ZpRh0-6WEX2940wFmREmzwhWNRzpRA91Ov_tRlZxYKhM0pvYlUCPCfkBinYHkv5hFJUhJAI9cGuH7RvkgSQcV2Djv6dou0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای مسدود شدن شبانۀ تونل‌های پایتخت چیست؟
🔹
در ماه‌های اخیر بارها اخباری از مسدود شدن شبانۀ تونل‌های تهران در رسانه‌ها منتشر شده و دلیل بسته شدن شبانه تونل‌های پایتخت سؤال بسیاری از شهروندان تهرانی است.
🔹
مدیرعامل شرکت کنترل ترافیک تهران می‌گوید: انسدادهای موقت تونل‌های شهری عمدتاً با هدف انجام عملیات فنی، نگهداری و ارتقای ایمنی زیرساخت‌های ترافیکی انجام می‌شود تا عملکرد تجهیزات حیاتی این تونل‌ها در سطح مطلوب حفظ شود.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/435250" target="_blank">📅 05:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435249">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2k_GZFeeM5x51cRer4C4efZgeAI0kRix4MIgUikon5P6O8x-cARrHKqp2bRt5hAn0rrMCZxMSfq0mLJAD5tb2j5JIZY_uTqhNE_G7Y-LwiqAjOtNMdG5Y7Tsh11p4j2FXx2VWBQ_9Su-Ov5kKFzhx0EdRODA-fhrzucjWUN_7xkZ942JlsN1wukrZVK_MbcS4bDu1tm6Ed5quTLPYRvVwbE_nLL6b2GVk-RaBmspF9ob_BBr-2j8GDaCw-qe1vS799C0pCQogQ-va_6t7ljC__KEbbiX4ANzKK1lVTVYLklt_KEJa_-_YUSb5nRzvV8b-VUQAv3bg3IH7_g4NaFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پکن: پاکستان میانجی‌گری بین آمریکا و ایران را تشدید کند
🔹
وزیر خارجۀ چین در گفت‌وگو با همتای پاکستانی خود، بر تداوم حمایت پکن از میانجی‌گری بین آمریکا و ایران، و مشارکت در این روند تاکید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/435249" target="_blank">📅 05:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435247">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62277199ed.mp4?token=GXl-qve8g_dueTk1aq4WEJltPEIb8xpaALl2G568PrSdMH6yc3t8WtsSyCunC1FP4zMOmPoAdVyYY1tXyMHNQPqjRIEG2J41rPA8j2verFNlwTBhMokQ38-lSvlprfjOIcYFEsC9KxdSzzJgatUyz7rwJn6NU-ZRSV-tvs1UrjsAfkuDFquiq4PlhFl7X4YM7SeXD2w6xfiXu7t54xvlzWWFE_QSfqIGidvKSlaLvhZoWMJOntduz8ROmv8_RnpnDlZxfDbla_LEDb2mc9_bxG9S49gJlJ-WWx91H5OK3s6IXPA2OO39vvpUtZLgKuFxaxC88x9a0Zet7JJR2zprIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62277199ed.mp4?token=GXl-qve8g_dueTk1aq4WEJltPEIb8xpaALl2G568PrSdMH6yc3t8WtsSyCunC1FP4zMOmPoAdVyYY1tXyMHNQPqjRIEG2J41rPA8j2verFNlwTBhMokQ38-lSvlprfjOIcYFEsC9KxdSzzJgatUyz7rwJn6NU-ZRSV-tvs1UrjsAfkuDFquiq4PlhFl7X4YM7SeXD2w6xfiXu7t54xvlzWWFE_QSfqIGidvKSlaLvhZoWMJOntduz8ROmv8_RnpnDlZxfDbla_LEDb2mc9_bxG9S49gJlJ-WWx91H5OK3s6IXPA2OO39vvpUtZLgKuFxaxC88x9a0Zet7JJR2zprIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
آخرین ایستگاهِ خط هفت مترو تهران افتتاح شد
🔹
ایستگاه مترو ورزشگاه تختی به همراه ۲.۵ کیلومتر مسیر تونلی در خط ۷ متروی تهران، امروز افتتاح شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/435247" target="_blank">📅 05:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435246">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آموزش‌و‌پرورش: احتمال دایر بودن کلاس‌ها در پنج‌شنبه، جمعه ۷ و ۸ خرداد
🔹
معاون آموزش متوسطۀ آموزش‌وپرورش: اگر دبیری احساس کند نیاز به رفع اشکال برای دانش‌آموزان وجود دارد، روزهای پنج‌شنبه و جمعه ٧ و ٨ خرداد، کلاس‌ها برگزار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/435246" target="_blank">📅 04:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435245">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شهریۀ کودکستان‌ها تا قبل از آغاز سال تحصیلی جدید تعیین می‌شود
🔹
به گفتۀ رئیس سازمان تعلیم‌‌وتربیت کودک، تلاش شده که تعیین شهریه کودکستان‌ها مبتنی بر واقعیت‌های موجود باشد و از پرداخت شهریه‌های غیرمتعارف جلوگیری شود.
🔹
این فرایند از ۱۵ خرداد آغاز می‌شود و تا پیش از مهرماه شهریۀ کودکستان‌ها و مراکز تعیین خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/435245" target="_blank">📅 04:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435244">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0BXPtP4MpbJK-vC0ZRNntmM_jCbji06rusq2fP70Mt7y4_7cPY-6PK59SzrW6OuyEfJQ0A9zMyE2YLz8Zezp2Oyssn-BIA8u54fEno6_YjMn15ufciy63MZoPHmo0ogJ0AObZRnOsbp7YPRkYKp5CCOKqB_Nq-9TIPgwQoFhbVu4D2Q83o0TMHepi0V3sOOFWuSi13d5aZEwuqmKjmy045bHPCxqFh65ZzlDXN2X2SAOLh1Qk67PtVllLbP3VoVH8o6YQoUvek5Rzk98isJGv0BHqGvFb7_i5dZsL20X420F6YYQf_lFndCYxmHuC5SQxQkXtHdNMugBR-RBtfIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: اسرائیل نگران توافق بد آمریکا با ایران است
🔹
مقام‌های صهیونیست به شبکه «سی‌ان‌ان» گفتند که تل‌آویو نگران است آمریکا بدون رسیدگی به مسائل مد نظر این رژیم، به توافقی با ایران تن دهد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/435244" target="_blank">📅 03:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435243">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
آبادانی‌ها امشب را با نوای صادق آهنگران به میدان آمدند.
@Farsna</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/435243" target="_blank">📅 03:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435242">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anNcRnCzS_RWLnAVqzUFLWlk3pRI3QUdQsf1o8BY2vhCphGUMpdLaCUtDE0qWkvJcrxmzXWHsfQsBPIjvTM_RuQ4ZkLOeXGN8qIlGhYYE48HJfb5uxTkOZGI0iGD0Apmmj-8Aii4bVRK9oec6KmvPzsYbVw9erBWj4ND8_4-jKYoZTmXJcXF9q_qjyVvTrTC3LrWhkPsdoGZwmrW_5zItpGcOcvV8POg_DpVEWT9gsASw7jpWuEPkrFUAZiw4ybp-tYBQ7GIrYu9UijJ-aV_ZE5oYe2W5QYP0AWkdGxsr7W9QIUlOaVWbF5BaCoUZLuVgPGS04IxNPrOmNW2k0XDiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی ترامپ با رئیس امارات در راه چین
🔹
رئیس‌جمهور آمریکا حین پرواز به سمت چین، به‌صورت تلفنی با «محمد بن زائد» رئیس امارات عربی متحده دربارۀ تحولات منطقۀ غرب آسیا گفت‌وگو کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/435242" target="_blank">📅 03:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435241">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
زمین جایگزین بازار جنت مشخص شد
🔹
شهردار منطقه ۵ تهران: زمینی به مساحت ۱۰ هزار مترمربع در سیمون‌بولیوار، جنب ورزشگاه شهید کاظمی، به‌عنوان جایگزین بازار جنت اختصاص یافته است.
🔹
قرار است در ۴ هزار مترمربع از این زمین ۲۵۴ غرفه احداث و باقی فضا به پارکینگ تبدیل…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/435241" target="_blank">📅 02:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435240">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎥
اجتماع دوقلوهای شیرازی در میدانِ خیابان، به‌مناسبت روز دوقلوها
@Farsna</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/435240" target="_blank">📅 02:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435239">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAZo8x1ErDyE7KnWeTzWcku40WqxUwmQkeeOA4rW5PBxkEaDupoPDBIbqhnRizrBFtq8a0uJDfipNBoGQXAjNk7AKw2ydzdf_WAcz0LOfVSlEjoPL0B9XdTHcIjkCB9I_J0N9Sfz87nkar4jzOu91zr3JHoKpcOnS2-Sz7m7p4LKWoliCmgSkyHEYshueLp2sbUovo_u2YraHOF352u-ZHB-G4mGLtfXDBfJ3vxSqwqpEo3SIxHoBFKQV3l1qRpe1QRLb17ZV0eEYGkuRL1SgGfdgzYRS-ThBorWSOCVIlMCIkTDQoLdh4srL7T1gbGWG8taxugR4OwZnYGDfSDJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: ۱۱۲ کشور به قطعنامه آمریکا درباره تنگه هرمز پیوستند
🔹
منابع دیپلماتیک می‌گویند که ۱۱۲ کشور هم‌اکنون از پیش‌نویس قطعنامه پیشنهادی آمریکا به شورای امنیت سازمان ملل درباره تنگه هرمز حمایت می‌کنند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/435239" target="_blank">📅 02:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435238">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">طوفان امشب تهران ۱۷ مصدوم در پی داشت
🔹
بنابر اعلام اورژانس تهران، در جریان حوادث جوی شامگاه امروز مجموعاً ۱۷ نفر دچار مصدومیت شدند که ۶ نفر در محل حادثه درمان شده و ۱۱ نفر دیگر به مراکز درمانی انتقال یافتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/435238" target="_blank">📅 02:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435237">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2YFr6O5a5ahnZDTCXR7Ss19DFCojVYiRUdQCjHm4mTwkQ0gop9hWjWk5uJ11-8WnLSlCZ_PnTrP4R4FMkNB5xms-JGRq6kNIyx6Y4Jc3Wf7I0jMRk7hKjR8CqQ1Mhk_nMRtppnDGjnO95gFBOz3MbcshOAdnNE1e5jQFO8mqm_a180RR-1T3sCf6pa83DTHtG4ggKLr1wWZT3InvX7ARhNKPQkNAgxGq1Eun2zkMvuEJcy_Fli4d3sV2SiabqDI_BcPCtjBy0Xjz1_wAnenDrh9gx7cBVK3Ybvwwkyv8H_Pd4IxZxvxpcdJ8Mk7DwJV5pl3CNNSav9qb7U98VoFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاهبرداری جدید ترامپ از آمریکایی‌ها با موبایل طلایی!
🔹
۵۹۰ هزار نفر برای خرید گوشی طلایی ترامپ ثبت‌نام کرده‌اند اما هنوز هیچ موبایلی دریافت نکرده‌اند.
🔹
مشتریان برای پیش‌خرید این موبایل ۴۹۹ دلاری، مبلغ ۱۰۰ دلار پیش‌پرداخت کرده‌اند؛ یعنی در مجموع ۵۹ میلیون دلار  پرداخت شده اما با گذشت یک سال، هنوز حتی یک دستگاه هم ارسال نشده است.
🔹
تاریخ‌های عرضه هم مدام به تعویق می‌افتد و منایع آمریکایی می‌گویند که بازپرداخت و تحویل کالا تضمینی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/435237" target="_blank">📅 01:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435236">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اقامۀ نماز آیات برای تهرانی‌ها درپی وقوع زلزله واجب است
🔹
به دنبال وقوع زمین‌لرزه در مرز استان‌های تهران و مازندران، بر اساس موازین فقهی، با وقوع زلزله، اقامۀ نماز آیات بر افرادی که در محدودۀ لرزش حضور داشته‌اند واجب فوری است.
🔹
طبق رسالۀ عملیه و فتوای مراجع عظام تقلید، رعایت نکات زیر حائز اهمیت است:
🔸
محدودۀ جغرافیایی وجوب:
اقامۀ این نماز تنها بر کسانی واجب است که در شهر یا منطقه‌ای حضور دارند که زلزله در آن رخ داده و یا لرزش آن را احساس کرده‌اند.
🔸
زمان اقامه:
نماز آیاتِ زلزله باید در اولین فرصت ممکن و بدون تاخیر (پس از رفع دلهرۀ اولیه و پیدا کردن شرایط ایمن) خوانده شود.
🔸
اطلاع دیرهنگام:
اگر فردی در زمان وقوع زلزله خواب باشد یا به هر دلیلی متوجه آن نشود و بعداً از طریق اخبار یا اطرافیان مطلع شود، همچنان خواندن نماز آیات بر او واجب است.
🔸
تعدد زلزله‌ها (پس‌لرزه‌ها):
با توجه به وقوع پس‌لرزه در ساعات گذشته، برای هر زمین‌لرزه یا پس‌لرزه که به صورت عمومی احساس شده باشد، یک نماز آیات جداگانه بر فرد واجب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/435236" target="_blank">📅 01:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435235">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نیویورک‌تایمز: ایران به اکثر تأسیسات موشکی‌اش دسترسی دارد
🔹
روزنامۀ نیویورک تایمز بر اساس گزارش‌های آژانس‌های اطلاعاتی و امنیتی آمریکا‌ نوشت که بر خلاف ادعاهای ترامپ، ایران به اکثر سایت‌های موشکی خود دسترسی دارد و ۹۰ درصد آن‌ها عملیاتی هستند.
🔹
ایران دسترسی عملیاتی به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگۀ هرمز را احیا کرده، که می‌تواند کشتی‌های جنگی و نفتکش‌های آمریکایی را که از این آبراه باریک عبور می‌کنند، تهدید کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/435235" target="_blank">📅 01:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435232">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t181wTKzMS7GNRPKuwzdyCqQbccA0lC1hSlDAv2Gs0IUgNWKwTKNupqS5tMSj06Gwd0dv69ehv-9QhMdg8cNA4jLKXbKvoSJl858xlhrZfGC0qub5fgzAMd_8uRMhNovsGBhMikf7FCUKFsqAZZy3nXmmwl7vh5v9dGHPEN2q6Yh3Sstq1jmFH1-VIKOwxd2C1PbwmeTafnLtv5JgkhjWC2HmLkQGa5gUi0rRC_zlKwaAPmCHkRyAPwCl-OS-gWY6XSQROqw0Xu4JFh9jFjRurYC77rEHWc0MgenIQ1x_Fnag7_oQCqXqQeTI8eG4oc_BvgBvHcbz4_MQJ8SmyrbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: آنچه بر ملت صلح‌دوست ایران تحمیل شده جنگ متعارف نیست
🔹
سخنگوی وزارت خارجه در شبکۀ اجتماعی ایکس نوشت: در یک سو کسانی ایستاده‌اند که از نقض قواعد حقوق جنگ و زیر پا گذاشتن اصول انسانی لذت می‌برند؛ کسانی که برای تفریح آدم می‌کشند، کودکان را سلاخی می‌کنند تا خانواده‌هایشان را عذاب دهند، و به سالن‌های ورزشی زنان حمله می‌کنند فقط برای آزمایش قدرت تخریب جدیدترین موشک‌هایشان.
🔹
این جنگ میان کسانی است که با افتخار از غرق کردن کشتی‌های غیرمسلح برای «تفریح بیشتر» حرف می‌زنند، و مردمی که حتی در میانۀ تجاوز، برای حفاظت از جان بی‌گناهان نهایت تلاش خود را می‌کنند.
🔹
این جنگ میان دروغگویان حرفه‌ای است که برای خشونت‌شان توجیه جعل می‌کنند، و مردمی شریف که فقط با تکیه بر توان و ارادۀ خود، از وطن و کرامت انسانی‌شان دفاع می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/435232" target="_blank">📅 01:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435231">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316c432ae2.mp4?token=o2HN_A-OMJhKCPBOWmrFZORA2oLnqhZXExS2Uz3p4lawJkFG5Y3GD4WEkUGfJ7PLMHUwSolHIXcsqU7HS3ax0_U419wWWqnel74mBVnz_yksOjMQ6c6DI4eR3AH0WZ1czNrZNc2TYeJ3oneUpvRuO8XJZQnnt01S5WC1HyYXb7iN9kmtVDiQPXwgSQIYK4zpqSPe8VP6h5gEbpW30Wf9dXcbdks8bArbyv5FQCA3WSMGLX6cCA2HjhXbXyOyySDNrHRhPu48t3k5r8Plv1A23qpQ3zMD-v-hzpzHdwPdsuk1eZn5IQOrVh5i1H1aKGk1lSkJv_dfnQpFjT59H_c5w2BgZCT-4OOq2xwxH41EYxu2aYa8IWH6MGsyTtA69dZ9hNgyhxj2hyswjAQCokIgNkvF92zGAXpqvlarBN_8Dr1yiz3fVLdfzkma1f74slqkOjS3hvGVCjaf6XqWZLx1XupU4JxS_D21Nsx7ZPK5uSCOu0cGko7N9TNK-iAmY4rc3GNnrnFgANUa-NZoXGHPjViw8QJpzxMFpnlP9III_1UthrS5v3WomDs1iXjPVkN0a4zfR4tXqBidD5d24cZ8i3LpS1Snzg4RVWFQTnyiasuUYG2Rdlmoj090rGvcFXG9J8dT1pk3HO00USVYlNjOubCo-0O8A6da5rXM8YWE17M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316c432ae2.mp4?token=o2HN_A-OMJhKCPBOWmrFZORA2oLnqhZXExS2Uz3p4lawJkFG5Y3GD4WEkUGfJ7PLMHUwSolHIXcsqU7HS3ax0_U419wWWqnel74mBVnz_yksOjMQ6c6DI4eR3AH0WZ1czNrZNc2TYeJ3oneUpvRuO8XJZQnnt01S5WC1HyYXb7iN9kmtVDiQPXwgSQIYK4zpqSPe8VP6h5gEbpW30Wf9dXcbdks8bArbyv5FQCA3WSMGLX6cCA2HjhXbXyOyySDNrHRhPu48t3k5r8Plv1A23qpQ3zMD-v-hzpzHdwPdsuk1eZn5IQOrVh5i1H1aKGk1lSkJv_dfnQpFjT59H_c5w2BgZCT-4OOq2xwxH41EYxu2aYa8IWH6MGsyTtA69dZ9hNgyhxj2hyswjAQCokIgNkvF92zGAXpqvlarBN_8Dr1yiz3fVLdfzkma1f74slqkOjS3hvGVCjaf6XqWZLx1XupU4JxS_D21Nsx7ZPK5uSCOu0cGko7N9TNK-iAmY4rc3GNnrnFgANUa-NZoXGHPjViw8QJpzxMFpnlP9III_1UthrS5v3WomDs1iXjPVkN0a4zfR4tXqBidD5d24cZ8i3LpS1Snzg4RVWFQTnyiasuUYG2Rdlmoj090rGvcFXG9J8dT1pk3HO00USVYlNjOubCo-0O8A6da5rXM8YWE17M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: امیدواریم که یک روند کاهش قیمتی را داشته باشیم   تیم اقتصادی دولت در تلاش است و این تلاش به‌تدریج آثارش را نشان خواهد داد. بانک مرکزی نیز برای کنترل تورم درحال اقدامات جدی است. @Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/435231" target="_blank">📅 01:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435230">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c74ca1d8b.mp4?token=v4B8Bc2tkTRfMCSyiKLf4vsqcmKi669qbJOjUb5a3w2NjjmwxNZbwK3PgtuXabKGyQjpc8dKV2aa_3yKknJuKSZQ08aPdZgxPxGXldH9WsYgS2LdmFJSdW3ubQ4hrQ7nHU8enHPO5XPHEJvKAG4v9QFqZhzLBg72DmGuhgc95ArM-sBJDHwXi38tjxCPUKSnMcNEBlKHON9OOnQD8PiGM9Za_Kg1zDO-43NHJPyqqS3ts7YT8NbLi1swRk2hF4Sm1ZlXeSyPH-NiOGFwmlHf9olQpg4iNGBxAZ7a2qHQda8Inkake2AOaZRUkRC8DX2fRabp2xxsK7WPr0LWfqXhQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c74ca1d8b.mp4?token=v4B8Bc2tkTRfMCSyiKLf4vsqcmKi669qbJOjUb5a3w2NjjmwxNZbwK3PgtuXabKGyQjpc8dKV2aa_3yKknJuKSZQ08aPdZgxPxGXldH9WsYgS2LdmFJSdW3ubQ4hrQ7nHU8enHPO5XPHEJvKAG4v9QFqZhzLBg72DmGuhgc95ArM-sBJDHwXi38tjxCPUKSnMcNEBlKHON9OOnQD8PiGM9Za_Kg1zDO-43NHJPyqqS3ts7YT8NbLi1swRk2hF4Sm1ZlXeSyPH-NiOGFwmlHf9olQpg4iNGBxAZ7a2qHQda8Inkake2AOaZRUkRC8DX2fRabp2xxsK7WPr0LWfqXhQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انیمیشن طنز «عملیات پروژۀ آزادی»
🔸
دیگه یه راه جدید پیدا کردم که از تنگۀ هرمز رد بشیم!
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/435230" target="_blank">📅 01:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435229">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
ثبت ۲ پس‌لرزهٔ ۴ و ۳.۴ ریشتری در مرز تهران و مازندران
🔸
لرزه‌نگاری: دقایقی پیش ۲ زمین‌لرزهٔ ۴ و ۳.۴ ریشتری مرز استان‌های تهران و مازندران را لرزاند. @Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/435229" target="_blank">📅 00:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435227">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🔴
برخی کاربران از حس‌کردن لرزش خفیف دوباره در تهران خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/435227" target="_blank">📅 00:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435226">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌
🔴
رئیس هلال‌احمر: زلزله در تهران هیچ خسارت مالی و جانی درپی نداشته است.  @Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/435226" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435225">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
لرزه‌نگاری: لحظاتی پیش زلزلهٔ ۴.۶ ریشتری مرز استان‌های تهران و مازندران را لرزاند. @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/435225" target="_blank">📅 00:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435224">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
رجز دختر کردستانی در اجتماع شبانه سنندج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/435224" target="_blank">📅 00:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435222">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKPZsekoGRxXmB8A-GazSBVC2Ifat0casUhrhGlHfeWId-s3bL5aCilF-wgNRLFMqrNAabOIfYH5ODWgIR0wY6VytMvHRZwxyWaXA9O6dWZZ9ucL8ZPwmPSchaR5TY_vfATnNCpWgSQPGP7NRMnpDQajYoJ3zYQlrQGNyZqgIZRmd201Mc_VzGHL5oLZXh469RDMfkNM91J65AYonNT9EAp3JRy_G_64_OkI4oWrSOLiRwAwUHa-aEoIVj4gQDHvq1g6K_ZRd_kzzq5SJACuJxcFNH0-DCTCKiOD1SWT1cYW8sKAGaZ_TvD988nLQ6w_28MFXoY3Du5_mLNa0glT7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: زیاده‌خواهی و عدم صداقت آمریکا مانع حصول توافق است
🔹
وزیر امور خارجه امروز در دیدار معاون وزیر خارجه نروژ رویکرد زیاده‌خواهانه و لفاظی‌های تهدید و تحریک‌آمیز طرف آمریکایی و فقدان حسن‌نیت و عدم صداقت آمریکا را مهمترین مانع برای پایان قطعی جنگ و دستیابی به توافق احتمالی خواند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/435222" target="_blank">📅 00:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435221">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b12b97a7d.mp4?token=hcMB7PGIgxttSG13WtPK4cgTbOmowcc5RrU2v2W0tyTnVldQOYgYfczeGB4dCdRJ3pa1KB6zJ2HXPMymT3QtMyt2ZR17cnU3L8f2_c2aFweLNG_7AnMAnoFdA3LgT87EkaGLydy5MNcPRLVXvPn0kWq2WwtHwtAw_TqKQG0RZ2H6QXgENzkUy4JqUwji1z1lO54LK_uXx4uxbzsmrBWAapXij9TR7SmU5wp2JoMbgwI4IK4V31H85ztxySfyIFbst6Dx8A38rYdl_xn56flsm4NQlmvdxnHoucYSSu6Tiye93mEHQSEHw4IG8KLBaz6QRKi2FdPc4PW5cm9zvOfBV3peIDx5zj8GRW3gNbrOLzblg0QrhOLhLf_Pzj2kDkkai9-H1Mri-nRS2Dhql4Tt56ZoZw2AFjD1MkJWyr7yEVHJfK5_bn9tM0MntlVTW6yGM4Aa_wl2euwQfWkLmvfQkjufJO7JMgZVV_F9sE_K_v_yAjrvhMjfmTr3PMb7eE93EOmmeaDynkjp4zB16OehcdVfkJ6YtX2NtpqGCHaz6u_Fo-5L5mr5jNVF_lfb0f76s938slRVjsoPO-OLj5P-kKouWekewTOCB8h3_A8JgCwjSTi0TltMnC45hWDwypZv-x5VMXnAvVb8iSHoGwjecB8qujD7sjRDSJcOCPKYvVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b12b97a7d.mp4?token=hcMB7PGIgxttSG13WtPK4cgTbOmowcc5RrU2v2W0tyTnVldQOYgYfczeGB4dCdRJ3pa1KB6zJ2HXPMymT3QtMyt2ZR17cnU3L8f2_c2aFweLNG_7AnMAnoFdA3LgT87EkaGLydy5MNcPRLVXvPn0kWq2WwtHwtAw_TqKQG0RZ2H6QXgENzkUy4JqUwji1z1lO54LK_uXx4uxbzsmrBWAapXij9TR7SmU5wp2JoMbgwI4IK4V31H85ztxySfyIFbst6Dx8A38rYdl_xn56flsm4NQlmvdxnHoucYSSu6Tiye93mEHQSEHw4IG8KLBaz6QRKi2FdPc4PW5cm9zvOfBV3peIDx5zj8GRW3gNbrOLzblg0QrhOLhLf_Pzj2kDkkai9-H1Mri-nRS2Dhql4Tt56ZoZw2AFjD1MkJWyr7yEVHJfK5_bn9tM0MntlVTW6yGM4Aa_wl2euwQfWkLmvfQkjufJO7JMgZVV_F9sE_K_v_yAjrvhMjfmTr3PMb7eE93EOmmeaDynkjp4zB16OehcdVfkJ6YtX2NtpqGCHaz6u_Fo-5L5mr5jNVF_lfb0f76s938slRVjsoPO-OLj5P-kKouWekewTOCB8h3_A8JgCwjSTi0TltMnC45hWDwypZv-x5VMXnAvVb8iSHoGwjecB8qujD7sjRDSJcOCPKYvVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها و حماسۀ ۷۳ در خیابان مقاومت
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/435221" target="_blank">📅 00:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435220">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDKUvGPM8TbQS4KXGZPpvvA4tU05DPS6iOVI9eL73De9bikxKuZ0HbKgdButVcwA55Ie2cYIU4LVba2rZYY4uQ31_9T9t027xk-QQSDGVVMGoiie39dZyJKNzW6P6nybzmV8GcngYgQ5n9YdrUktT1N0VcaqFzi91QpanoaOeBh4-w8RVQuIUG097mlclIWwsadEGW6lyg6EWm9AINgV8IhjUdkAYPtD_L8D4JxD6tOmgIDMVznCmkW5fepBFhyeZiI9zPbOsymL_37y9-sXae90RT_WflFkyBg1kmo3TjubprdVCPF5wG0a7XZk_TDP1K8SmB8ALtLjv2rOsPC-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی در آی‌سی‌یو بستری شد
🔹
مهران غفوریان از بستری‌شدن اکبر عبدی در بخش آی‌سی‌یوی بیمارستان خبر داد.
🔹
فرزند اکبر عبدی با تایید این خبر، علت بستری‌شدن پدرش را سکته قلبی عنوان کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/435220" target="_blank">📅 00:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435219">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
دقایقی پیش زلزله تهران و کرج را لرزاند   @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/435219" target="_blank">📅 23:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435216">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
دقایقی پیش زلزله تهران و کرج را لرزاند
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/435216" target="_blank">📅 23:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435215">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjBbDHzzsBQ0Wd8LpsUE7PgJgU8xViuUi9U7BKhRJC0PkNbW7gOK6YqWQbdHi_rX644YSxPj1m3Y2Sl4qpC6yem7bm5bCTZBpTVgxITxwdc38PFhnlVfHFUDly5SE_FH108Z7yU2FO1Y9cKNNZKM9iR2zVWV9IZqute4tdSSbBKCts_8vzcSgLGKUGJ5FfVpV7fYNzJNDWttpXpTvNyjYJHhuxmAKE_tUMdwhMCCHL1wU4CBSSh38U25C168cVLRslGrEJ8ztxFZGlOXFRbYvN4jeKPP1vu5S1C1vY8oAKd6y8KJNH1vj0hhG3g0cZFnUONW7e1Vr8F3A5MBUNgSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای مدیران مایکروسافت
🔹
شعبه اسرائیل مایکروسافت پس از تحقیقات داخلی درباره همکاری این شرکت با نهادهای امنیتی اسرائیل با بحران مدیریتی روبه‌رو شده است.
🔹
«آلون هایموویچ» مدیر مایکروسافت اسرائیل پس از چهار سال از سمت خود کنار رفته و چند مدیر دیگر نیز شرکت را ترک کرده‌اند و تا اطلاع ثانوی مدیریت این شعبه مستقیماً از سوی دفتر مایکروسافت در فرانسه انجام می‌شود.
🔹
این تحقیقات پس از نگرانی‌ها درباره نحوه استفاده ارتش اسرائیل از زیرساخت ابری «اژور» آغاز شد.جایی که طبق گزارش گاردین از سال ۲۰۲۲ حجم زیادی از تماس‌های تلفنی فلسطینیان در غزه و کرانه باختری ذخیره شده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/435215" target="_blank">📅 23:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435209">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHWmTK36WTdf_Q7knYPP-iJn0dvfhGKkQcZ0fr31Qh61tA-jHF6kwv1SBsYNTWb9d45jfoYHSPbE_v7jPbceU2QI73BalLt0xZE6p7fA_iAqmA14k0pWQnAuo-SBN452bAyoxvCk0z9cYMrxpXKzKssF9WZfrWUEUPxGm2AnCKixjLOfkOnAGZCiZYW0rbsBYZj-AfeaqRO6Rp1wzRfdsT-6g09G27lrHMUJnSTyAeY9nIppv6MWcm1SdqTYT4lRvqyGjxAY-0-EgG2SGR5DUr1F0UMoTxduqn6uIigMW3IVdsEqHVCpG5kihrWBF0ib_sGiGaTsMwAfReUjFElHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVtbvrydi8O_uMLUFXXbeP1qLWCl9q81yPY6HiRZPG7zACZen_VW_gGz_M1T9lo8IOz5YMXdJBzXSsdzfpz0eMkM17pFoksscFzmebGdcdBZtN1jYWnY1GMTxiu9mlQqiBDGKNpQasKaBukqQ2vfnNkbAt-5UW2TvhoXQR3nstOlFxP_1w8EMrLGEHfUTdPEHuaPVue61VUd7vlueK5rrFlGq_f3a0Pf6G4iBHyW2HcGp5H5v-EXMhKPuYkHUszOpKVlWJk7mCl3awqwC3YbypB0je-j1JzGPiUKt9e_WMYgmxl6aZNHiEloZMxpy5uilGfj8CR5W9GchbxueH43LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7uc05pXXGkaIAp0_22uZLWy7Puki5tuw3w069eFkxeC12gQt0gQSlhJU64zv33Q5eBrd2pSEYj1aSrPinK8TVCtGBNoKLbx7fYpfze3TFvmau5QcD1_ya4rXk7edWgtxY0MN6VokekGV73hkLswj-nQXXkYGi7WDzl7zynJUlVG0axKEUarhyif7iRW4mmm66VtXJ1_x3U-Fe2QhbISt5LlujL6d3b2UoO7c8yGSsXEWYwts8UXks8abonjYZ1qXzUmonP7UDXOF_XqXG3DA6LvtSs-LcaLxJPiY1QpHSft9l3gFRlqUay2yPmKYfefE2XbIKvevBc8qm2HT-k_Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLWoV5SxsSNG_vyXkMDArprFxbVTMBJjPqrL-IZY2-Xl1_xpBKuGHL3MG7ZYekUL7eCGwIq6T9lOB24FU7Mk9NFFWnrNlORkF9UQVW3MFUy3tNutDvNgvDXzKf7L498eQ2y1BJ9cVebtjsNGD8B03692BlfD8M2kvVxriIGkO9ONDosb9MWovKjfQOvEOput01rt7PwHSXeVrfuHYJmDF_KTnAjLLUABGXZpYMyYXMR4kEszo9Jz58cnKbb_ygO86tqFS0WBGJ2khysSZ-XU31O4DuQuFs_8mBMENycWKFGBO_sDHFuwIXnUtm6aHoQ_Se7HUQ0FAJM1YWb_zFvaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9gpXNx7JfqHHyRVhW5dPCdTQU4CSx8cWeAOIMnXpd6SPTq_Ly5fDJiJ8FtPuVN7W5x8KDspPtrIi28KVo0mCa7pP6pg26JYL9aD99a76vMguWde2bxfRIlnpSHs1qpzc_rhy3Bu2vhqEaLZgLi_D0DXeaASiWN-P1Jh3ZYCzd_tRq9k6iPIvWtBktY5JpOFw07GknUxmMQBUt5gAAPzgNK44MtR5mO_d7sm9nYTEVzlNVj3pro2CFalq_xmd5SqXmNpfDzipjHRUdSrIf-ZUN0yzpmeMj4KZhREfEMQPJZvzbMOWl4nhS7dxWOlKQiLCsGnaDOCg1bLIQRxOA_WSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HgqydFS3BG1ev1N6YAi2hKP-cJJXsLk7qwyeKBxTHMWUTqysny2ynXrcD3gGLRFo9wUKuPJTGFVm09FcWqwhYlI07WkHP0eSpMesuSJ49FpKtsBVKhVweKXUfew92MZ3QZb46w4RMJ3EGOSFntNHbtlxaxwDKjKLHZQ3ViynqKmpcGwKoBAodgcTeIjfubcPu4lVW6NRnBaG2hgcyFSObnZep4fvt9zfUfmGOqVp7bbdu_FTh0lEjPDKonRclFJdTgICnPIFtK_CajcnF6b59xFyCaE_79pQ1-JxPNCyk5apjs5cVmLy2Xbel0KS-Oi_dyhKgNiy-7EE1D4yqLASyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دست نوشته‌های بندرعباسی‌ها در تجمعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/435209" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435208">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beee3a0abd.mp4?token=h31xP7VPtqCh9mb3ZIG51-eapX_6sRz9tpilsrmaFy_g0AYORSucvcPz2jLOkSaVUpHt0_aOj2kLSFcSC_D3XhfY6gs1qQenneRkDuRQ_npYBTv-mnXFphT-uvANhEPocLJU3CA3KJjqeT08DFkkOiYnr9TBBPHSIV3scxvhKqBryyccm1iO9tzmGMwuEs028aHlH69TIvYPnoJqyfrmR-2PVdjmrtvQYP4hwVG5NoKXdx2AP6WygmEGpc8bXUZhDHa1G4QOLqthPoKjrn5hMzyhPKtASGNRhWT9m2oHFg6-90hayi80RX9oViD67eDUdmlidi8bOhcQFe2WLxMFfnPW8i1SZ19gP5AZdsRTrsMa5RpppQzrPNArHe9uqyKdufCEgTCCsRGaDUqiYVFG4O45GxI_RhfCj5SzKQ8E9FXLBAyjdSqeVqh39iE_KKbl5sNRBbDPD1D8VSCs9K1zQ26oSWxN38BjoyuXHe00c1yjwPJsTb292LbXtuMiavVG7aSnj26UADSnT_T6lHITseTjiMApry6inUCEkw03yq5A6fuulG8z8fUd70Hy9IyspdH5KYzboR1aMvEluKH5LrfNa9uLdjhFLuworU1DAyh6biiLEHj75aIPWKUYyO1OI7JMXRrXBvPnEj9RTZS9GvnA_h0gekFqk2aT-ZUQALE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beee3a0abd.mp4?token=h31xP7VPtqCh9mb3ZIG51-eapX_6sRz9tpilsrmaFy_g0AYORSucvcPz2jLOkSaVUpHt0_aOj2kLSFcSC_D3XhfY6gs1qQenneRkDuRQ_npYBTv-mnXFphT-uvANhEPocLJU3CA3KJjqeT08DFkkOiYnr9TBBPHSIV3scxvhKqBryyccm1iO9tzmGMwuEs028aHlH69TIvYPnoJqyfrmR-2PVdjmrtvQYP4hwVG5NoKXdx2AP6WygmEGpc8bXUZhDHa1G4QOLqthPoKjrn5hMzyhPKtASGNRhWT9m2oHFg6-90hayi80RX9oViD67eDUdmlidi8bOhcQFe2WLxMFfnPW8i1SZ19gP5AZdsRTrsMa5RpppQzrPNArHe9uqyKdufCEgTCCsRGaDUqiYVFG4O45GxI_RhfCj5SzKQ8E9FXLBAyjdSqeVqh39iE_KKbl5sNRBbDPD1D8VSCs9K1zQ26oSWxN38BjoyuXHe00c1yjwPJsTb292LbXtuMiavVG7aSnj26UADSnT_T6lHITseTjiMApry6inUCEkw03yq5A6fuulG8z8fUd70Hy9IyspdH5KYzboR1aMvEluKH5LrfNa9uLdjhFLuworU1DAyh6biiLEHj75aIPWKUYyO1OI7JMXRrXBvPnEj9RTZS9GvnA_h0gekFqk2aT-ZUQALE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحهٔ حماسی کریمی در میدان انقلاب: «رهبرمون هرچی بگه همونه»  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/435208" target="_blank">📅 23:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435207">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd2e9a41c.mp4?token=EnXQ9b4PRRushVtCQ3jbN5fz-geVbuGo5DfscQx1lc8sTV8WzTbGlLA5EPMfuf3zklEXsibtUIbN_Lp5i6bG_isy-sXyIpO4jhVrQAgx8Kl8gfQIRG7057Y3mHeWKaVVMKIiEj5df69Hk-Pit2NG4Dzm7hUvX6aLvZts5tJH6jDCXKSfGbgZ3FHdMhdGPJSpxx2wjT905iSZhUMbbZ2LxDsp06zn9H75oD-tl2PtkVDSuqEHLAlm7iQcK-JbdgoFRwesIFOe-qdFI2rKYnCcAdg1OwZWCKPvwqOsxyjezJYUC9oTHtyxz75iQjFCZcbjZ-LAkHH1vnFhTxmTEs7Upw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd2e9a41c.mp4?token=EnXQ9b4PRRushVtCQ3jbN5fz-geVbuGo5DfscQx1lc8sTV8WzTbGlLA5EPMfuf3zklEXsibtUIbN_Lp5i6bG_isy-sXyIpO4jhVrQAgx8Kl8gfQIRG7057Y3mHeWKaVVMKIiEj5df69Hk-Pit2NG4Dzm7hUvX6aLvZts5tJH6jDCXKSfGbgZ3FHdMhdGPJSpxx2wjT905iSZhUMbbZ2LxDsp06zn9H75oD-tl2PtkVDSuqEHLAlm7iQcK-JbdgoFRwesIFOe-qdFI2rKYnCcAdg1OwZWCKPvwqOsxyjezJYUC9oTHtyxz75iQjFCZcbjZ-LAkHH1vnFhTxmTEs7Upw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کودکان ایلامی غزل ایستادگی و ‌مقاومت می‌خوانند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/435207" target="_blank">📅 23:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎥
حماسی خوانی یاسوجی‌ها: «اینجا ایرانِ، کشورِ شیرانِ»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/435204" target="_blank">📅 23:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435203">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4_jT1RnGb9pL1rgwYIlc-o-acJkjl6SSSeJrNUEEAOxLL1-PoAmV-s-T4i2drMLi2hwq4qK5uupHU13x-qEw1rJ7gitgEn0LiKUo0WZTJg0tBCJflXV0zv0A4o1KBrN8G5iIyUiODCwy8Q-wYp5DSRRzlx392AfYNu-EJFvDTcLloLrTV0kpYDbMWuGO9Fmmr_RMuLd9zhBbfrONbyxbaMlIX1EeF8PwmohkSqOgOOs55QiopcMowduIbP-V067y1ZF-wYZecHih9qWDYJ4osxijMvByQHjGydmU10AreNexrPzICXFxtXTzVDG3oR_GxC9Q2USqED8O-uTNccaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کویت سفیر ایران را احضار کرد
🔹
وزارت خارجۀ کویت با ادعای ورود چند نیروی سپاه پاسداران به جزیره بوبیان، از احضار سفیر ایران خبر داد.
🔸
کویت مدعی شده گروهی از نیروهای سپاه با ورود به این جزیره با نظامیان کویتی درگیر شده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/435203" target="_blank">📅 23:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435196">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4THHNgcmUklNz4UmD03QvxoXrW0X929t_OiauftaZBhxlu_4WNFTQI_-TNBKNMe7wVPLo1ElxWdnr6QvdGSxDlRsadJzfagipe-yGHyOsQcBCzbq6Rqvaz-oSgGUfaV8z4wy8QylSTXpzRZh80SM2foh3eqdCRnq6_wHf5OBqj9DTW6_BbAFv5xJBvBkH0eanF2iGSOJ6Dy7OBYxBRpDQc61HvY50BSERdFgIRXlmJoe0YGPbiep56eCATfLctZ5IDrv3NehhDM6lSBO3xjPNXYyOwrX460rr7Uqc2vrPoYqJrIa5ZnZHraCFH4689l6Xd7emlfFAjQPpUPyAACZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3a3Gl5Wn5KYr9QgL8qj_ALiObNIGeFdBd1yjvi7_aTZsMTSbIOWRH5sI6H5y1secCQcXNpzbTLMbtM0fO44ZJSoKLC3QNE8Jelq0LsVdBQSLO_vaS3A7EqZ1tU116os1A4YiFhwDA7dfP0Bgx2oUTCh1qF5PIroY6VHAHrRda7UJtTpupznUWKVzwsa1qE7xRpKZdLnUV9GlSlJ9V8_7A6a5pe3Crhnb76ZmudLj0a6QQJGQSLULwgPbglyQLCRVCLDaV30xVJSyU-MRyTRr-PnHpG_N93rIxuASd5lRWA9OZlH1MsmqewvBGDCjE7AbHy5lrCyR0Hxoq1q5tVxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqNnmuBelJ1fg-qvTDTZjo6-roL0qveCCkmVzg6WSQuD-xeukZJVmqLL88Phj6IyDsNRwUvrrV6Sx5wRA1ms7Qr__0qu4tL2hicnrGlDNNYfZUvWYsyzo1rFRt3q0A5oRDpMIxnk4gI-Jo82JsKUKpVces4Ivj5N-mmYFUAFW9AWaFOnt1kFpKwZ0ueOC5hsJoXY_ap9U51UFP-LIym24UtgTVeeGD_xfzsuq39ODIP1zv7vlBFb2-I4kuRH6EP7wOmzrbI2sKOk7w0o67vdlj7-DuOaZuNAKWLM_JHrWhQ3uSYW79k7F2bejpKAjnqPRL8SBrq6XLKkGkww4da8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoU1zPsbrwqCoHf9kvrAR9zCKnsyfLbl7wsvNAE-KFy1UGu2eqH-gxcpx4M7ZazYuFEOYql2hIJLMnd8SI0lhkvgI_utiDSmpmEs-TqDGNSA4q-P2y-I0kz7bSVga2AorkgqcK44zr1A6PPcBjA_-KRid0wpLA6j7ANnefBQr1EE2J6G-MOztG9IuF_Mh5mPfVGHt6oXwS0UsdvXlCGE7Pf4UKcNFWQctV4AQ1TnBSaDx8f1xKZtHQESffwE2zUrphgUbytVEAE9eCJmv-8pZ72fHlOuuvPAirOT0Eqb2zYwYdQz3FHyIZuJZgqDvJbIKCV0jrZA6Uu7C0M1i9MKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THOmQoNBtDWwfi-ZFdUvpRDDAzLnAVgFbjVUOI-S5drh5-djCWcoGxI13_F-VI6eYN9bJ3LNXDMMre-0FLLE8v4HAxZsUiwQUn_QPpo3_sjEeeYVOoF0euhPgPesQ-chDLG4O0Mn3pl2a-6FC4CneL0jI9ypxDXLujxl-z1eDhFWR00IGHLaLcp-HO0qy97BnLBFb85c8fqjr9zM9uQ7G-rWLPzi2XFW0rSsqnVZYCkwFteFI_6REMby61TNrNsDhKq1wsc0z_S0wFFNfuptYolkX9Q8YbmQDQxPsAYz9mFOYQIfwKHUOalNYE_gyOfcuJeeEXTYMU_y89cCUsth8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sLto07jQ1kQ8pRKbMv88A5a-R-dfMGNzTNIgM2GN47CT9VgHCN87iJv8GOVLyh02VtGQ_gZ2yBqePVoCA3VU4AzC0FHBBlcS49F5AGCF5WBMpTmi2OL8z2WNG1TK5_pJhKyq9G4gPkHgmI0jci9fo39KRthD7Yhj5e3MrUnVi1VYBodtUF1VB_tbQ2bSmQzKvhRRtDQFig8WbfNd_OXEXLNIO3XeDZYpkqmaAIh4ZlHv3x8xR3XwbgzrhZQlTz0jIgc27-sLcS03zMELX5L9tZeVVDMX9sVrMuZZWbrwMOv9pvUo_QYiri9SbBdCHuBnJdgVH8DQG-rqlOQyKENy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bnt4-inlt_T4ZLr5mDQCbV8jOTB2vr4RyB9S_LBdNmV9Z0vsr_u2unmg7Pb-Cc1ZMpzolIqs-HFOM0mOFDYD4rcC-LyY3NGNRUoK8a_dPPrxq9CHFe8JU-WBBxEk4YmvJUhlXU3DcwMdVr0LHhCYshKBVi_qLj6K-3Eh8L-zTe8UkcwGkCeY4QNWZV-6YibUtVWosQrnpZYNUw-JFi8nnf3fpTtBFp6X4VKHk8veTWA8IkdV7SRkI0zPFSgbvPeiC7f73mYqyrMnTgBV6F1qpPFKJSEJwHxhoyvfTY5bVuYuf_tEdCDPooDlR9S2iwYI8X0yo2M5PMrkiQwRrCrxjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برد پر گل تیم سفید ایران مقابل تیم قرمز
⚽️
گلزنان بازی: علیپور، ایری(۲)، یوسفی، حسین‌زاده
⚽️
تیم سفید ۴ - ۱ تیم قرمز  @Sportfars</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/435196" target="_blank">📅 23:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435195">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ceec062a4.mp4?token=s4NZ4ghVNC1UnZl4z-1P2zSPB3QpdNSk558yh19xSBO2Q8I4VjCFta91gTgW8UEGc7F-vU2O9ipCiCl1VVbPKWqX4xE6efRQKZnsV2fmx4D4G-wv2YfujMpq3A3GHaAQdnlvz0ZE1nrwp7XpNJfWq-9QpYVIonwf2IQun9M338MTaiSpH_UN3vdBtkCcu-kXKXQY-QyXCpKSPjW6AZBlXAIBmVn7_QgTaRMXuzv4UVIEP0drj1Xw4SH5ws1s6x7QbRvA-uN7NzBFOmbT-ZGOEpHaE9sJ3hqiru5bQfPH6qIJzWS5ArbTTgNquWVHmKwmP1CU6pNB1twKdBxlxradSJRBRhXBpA70Mve2Bkuu9ZotHzh3tGag5LPQEnorSZnGZ3hBXbFzev42MnP5zybQC8c53lt_4glSzNd1jU-AUPCBm_EWdin-e1i-QEjWnO6FB9QSJX96XkYV00y4rF4hbO0glXKk8f0KEfYq0X8zDZppsG7bitNdSTykOjlX5FRJAxCoN0to3wzdCocPbZFmI9mkeTs9DQjfKbS_fnwf5G685Zl1rndQK4hmUpY1fce43xf3wPD9iSJnNyikmtCcf7lmN4ZI5Yu8L3w0T_xv9RV5Gya4jPu_PxS9ThZr8DjGsn6Zd87fHAXGyEs-4Dauk-46v0mids3J-yYCff4FKoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ceec062a4.mp4?token=s4NZ4ghVNC1UnZl4z-1P2zSPB3QpdNSk558yh19xSBO2Q8I4VjCFta91gTgW8UEGc7F-vU2O9ipCiCl1VVbPKWqX4xE6efRQKZnsV2fmx4D4G-wv2YfujMpq3A3GHaAQdnlvz0ZE1nrwp7XpNJfWq-9QpYVIonwf2IQun9M338MTaiSpH_UN3vdBtkCcu-kXKXQY-QyXCpKSPjW6AZBlXAIBmVn7_QgTaRMXuzv4UVIEP0drj1Xw4SH5ws1s6x7QbRvA-uN7NzBFOmbT-ZGOEpHaE9sJ3hqiru5bQfPH6qIJzWS5ArbTTgNquWVHmKwmP1CU6pNB1twKdBxlxradSJRBRhXBpA70Mve2Bkuu9ZotHzh3tGag5LPQEnorSZnGZ3hBXbFzev42MnP5zybQC8c53lt_4glSzNd1jU-AUPCBm_EWdin-e1i-QEjWnO6FB9QSJX96XkYV00y4rF4hbO0glXKk8f0KEfYq0X8zDZppsG7bitNdSTykOjlX5FRJAxCoN0to3wzdCocPbZFmI9mkeTs9DQjfKbS_fnwf5G685Zl1rndQK4hmUpY1fce43xf3wPD9iSJnNyikmtCcf7lmN4ZI5Yu8L3w0T_xv9RV5Gya4jPu_PxS9ThZr8DjGsn6Zd87fHAXGyEs-4Dauk-46v0mids3J-yYCff4FKoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: تیم اقتصادی دولت با وفاق و همدلی درحال کارکردن هستند و تلاش می‌کنیم مشکلات برطرف شود
🔹
دورهٔ پساجنگ ورود به دورهٔ جهاد اقتصادی است. @Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/435195" target="_blank">📅 23:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435194">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35693b9790.mp4?token=vqgZt1IBgUBsoaRIs5pIH8xQovRYSD1xI0IHOyGAHlsOm_FOjJHeM1-KUUmOoxQMd6HkUSIpdIIgMs049VekDb7DnnNrK2Xtk3jKVvdVI0QyX2_P41_PFFsh9Ec5esZAL1szKPNuE47cn51ghRluggjKJa3jVzVB8aaHzc4F8MelrSeG3vl4MGJHfvgxJpn8XPm-_IaSyOAXjJSSSUSXykk5oVD_9qkEouMO7VlqHYsKNZUDQV9uHoCUbxAjx9-XWgzK8s0SMLdvQACt4_439KCBEKAENaeClpGdES0eocEfiUBXkn2JSXBnc_Uf74BBYm1E167z4r7K8HdPIhBCOyq1gijeu-vnzHUSmO2zuis5MHmhop1mA4p6HUXVUYVeFPRHLpBBZNsUqfRLvXN3HMMDh8MzqtjxWIrh8JDSLh0Lod6uYp67Ykm3n9tAPJuIFDBWOIFaU_VrJVqpWEwIBVNa2oTSeMqBLL5TNnPv1ClHOpWweXgM_zm9ZzCYxXR07c5uue7kn80dy1XeTB9ZmHhnYWMbj-bAWGG8P7QPGsjfVX2abz6EqQYjh7YXZt7852ZxveEFlfF4rXGoUXGPnaRZsRTdZZI1dVxbFXRp7q9eIm6se1sKq2BHG5ZDIKyILe20YzxX76kMkOlZ04aXmpAUJsEe2B1j5kjCWP1fEzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35693b9790.mp4?token=vqgZt1IBgUBsoaRIs5pIH8xQovRYSD1xI0IHOyGAHlsOm_FOjJHeM1-KUUmOoxQMd6HkUSIpdIIgMs049VekDb7DnnNrK2Xtk3jKVvdVI0QyX2_P41_PFFsh9Ec5esZAL1szKPNuE47cn51ghRluggjKJa3jVzVB8aaHzc4F8MelrSeG3vl4MGJHfvgxJpn8XPm-_IaSyOAXjJSSSUSXykk5oVD_9qkEouMO7VlqHYsKNZUDQV9uHoCUbxAjx9-XWgzK8s0SMLdvQACt4_439KCBEKAENaeClpGdES0eocEfiUBXkn2JSXBnc_Uf74BBYm1E167z4r7K8HdPIhBCOyq1gijeu-vnzHUSmO2zuis5MHmhop1mA4p6HUXVUYVeFPRHLpBBZNsUqfRLvXN3HMMDh8MzqtjxWIrh8JDSLh0Lod6uYp67Ykm3n9tAPJuIFDBWOIFaU_VrJVqpWEwIBVNa2oTSeMqBLL5TNnPv1ClHOpWweXgM_zm9ZzCYxXR07c5uue7kn80dy1XeTB9ZmHhnYWMbj-bAWGG8P7QPGsjfVX2abz6EqQYjh7YXZt7852ZxveEFlfF4rXGoUXGPnaRZsRTdZZI1dVxbFXRp7q9eIm6se1sKq2BHG5ZDIKyILe20YzxX76kMkOlZ04aXmpAUJsEe2B1j5kjCWP1fEzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان پرچم‌ها در آسمان رفسنجان در قرار هفتادوسوم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/435194" target="_blank">📅 23:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435193">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca283db5f4.mp4?token=saDX9HgWtiZlij4E7zqMAGdiQCjCanf1WgSh9MQ10Z1lSewuuxVh13t0oMZRLFzYFbnZYS-1O5SAdepSg-WyjJi-s9rjarWX89AIEgOpFHW1EY1u6AtS2L1yfWKUqcKvbZ60jAvVH5vvF8z643wcTKETSXVt_1niXXHAbuZ7S8dATKMDb0Er1gPAspEk8V79Q4bKus6FSvqopLj_JOHBuedsOq3zExi62Mp6bZ2Lr20yBBp860HfqHl4xDrxs1flmdt6E7vTyi3kE_EesDE-8e-z4yJLxkAsv534xUY9cYmlTT8Bw4WsIbB7EqUK3gz1HQScZh90TpKovUj-rEjwQVApyVylgGqkewxO_vnGtap9N2ZgcjX7ZDPBLggJzzgvvRbNYZA5JGqUtNXSX_lZ2EghZclI6Wb8wvQtlxSj8BxUwKPns7TOpbzXof-q1n7_N3UCCPIWts2nSt_BnVbiUVvAmPUvKM4L99EYJ1pmBuBTZOhzBHDrTDZsVVuX_XxfyUV3NDNSOID4xLiPWYCsvgWTGbOdt_rsR-FpGiQFBHPRNCS31fSZwjDKa3bDpWqGesExr2_vpvLW7CDNXRnOE6nDSn9DrP_xs_C7WVvv6gEwo2IdABAtBT8lRU9p33hZDnEFBcx5HmbmaN9YAPAPEzXriqS2lm_uXb-cuFbx2zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca283db5f4.mp4?token=saDX9HgWtiZlij4E7zqMAGdiQCjCanf1WgSh9MQ10Z1lSewuuxVh13t0oMZRLFzYFbnZYS-1O5SAdepSg-WyjJi-s9rjarWX89AIEgOpFHW1EY1u6AtS2L1yfWKUqcKvbZ60jAvVH5vvF8z643wcTKETSXVt_1niXXHAbuZ7S8dATKMDb0Er1gPAspEk8V79Q4bKus6FSvqopLj_JOHBuedsOq3zExi62Mp6bZ2Lr20yBBp860HfqHl4xDrxs1flmdt6E7vTyi3kE_EesDE-8e-z4yJLxkAsv534xUY9cYmlTT8Bw4WsIbB7EqUK3gz1HQScZh90TpKovUj-rEjwQVApyVylgGqkewxO_vnGtap9N2ZgcjX7ZDPBLggJzzgvvRbNYZA5JGqUtNXSX_lZ2EghZclI6Wb8wvQtlxSj8BxUwKPns7TOpbzXof-q1n7_N3UCCPIWts2nSt_BnVbiUVvAmPUvKM4L99EYJ1pmBuBTZOhzBHDrTDZsVVuX_XxfyUV3NDNSOID4xLiPWYCsvgWTGbOdt_rsR-FpGiQFBHPRNCS31fSZwjDKa3bDpWqGesExr2_vpvLW7CDNXRnOE6nDSn9DrP_xs_C7WVvv6gEwo2IdABAtBT8lRU9p33hZDnEFBcx5HmbmaN9YAPAPEzXriqS2lm_uXb-cuFbx2zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۷۳ میدان‌داری عاشقان ایران در قزوین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/435193" target="_blank">📅 22:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435192">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004694a3d9.mp4?token=jTgySsyPbKABSKpoECi3zHp54LYSDGKeEuJtHp367rYofJlaLd3b5ogmtfczyVZQy1pAKjx7ZYBr-Q_srwmUnf8pOEubrK-58a3ICiznWKkheEM6oc7yqoCwFEZnNMvK6NumVLtlBtmC0cfDBqGvt_4k522Durp-G8CmMPyFo1Cwjl6IkwyUlR8OWY28F7lTonw38YwgeAzz848stjue4M-HF5A7AC2j73bA15Clm_mSeA7CPQiKDsrH8aa2y05hF2B5P2oMc9sN2CfmDNfAav7KQyibvJIW3h--77x2JgEWBZgADNu4A0ZPd7mi-nJAUYeCsaFt_PMGgUTmkrrjiH2fYkBFaXluw68EEM59YHGmil3P33FUSrumAmcLjyo92HTqCIOZ3o5AB28CD11vZdOhQYMd62CFs2L7qqHScUOLAv0RDSbeLpFHiQUZhR2cMPEis12WUF7wGVY1i7S8a7izWNuIKz98LILaZmeA4disKchUvWgOs1SRONB6t4IfU6tOJOEAD7j9M8_39yTwu7Q8j7EQJETquMuz_CNSjJgPqIJz2UMxMIAe28V8_wFW_4v9d9xtkK4CtOovum6xwTQ1IRuoqFw1LyEigVi7Cr1WQpvXY2Vp6Uaf-GvxcPpo6XNMAytnY7MLyGcz2gA67f3AOLE-84QmWhujguHXZV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004694a3d9.mp4?token=jTgySsyPbKABSKpoECi3zHp54LYSDGKeEuJtHp367rYofJlaLd3b5ogmtfczyVZQy1pAKjx7ZYBr-Q_srwmUnf8pOEubrK-58a3ICiznWKkheEM6oc7yqoCwFEZnNMvK6NumVLtlBtmC0cfDBqGvt_4k522Durp-G8CmMPyFo1Cwjl6IkwyUlR8OWY28F7lTonw38YwgeAzz848stjue4M-HF5A7AC2j73bA15Clm_mSeA7CPQiKDsrH8aa2y05hF2B5P2oMc9sN2CfmDNfAav7KQyibvJIW3h--77x2JgEWBZgADNu4A0ZPd7mi-nJAUYeCsaFt_PMGgUTmkrrjiH2fYkBFaXluw68EEM59YHGmil3P33FUSrumAmcLjyo92HTqCIOZ3o5AB28CD11vZdOhQYMd62CFs2L7qqHScUOLAv0RDSbeLpFHiQUZhR2cMPEis12WUF7wGVY1i7S8a7izWNuIKz98LILaZmeA4disKchUvWgOs1SRONB6t4IfU6tOJOEAD7j9M8_39yTwu7Q8j7EQJETquMuz_CNSjJgPqIJz2UMxMIAe28V8_wFW_4v9d9xtkK4CtOovum6xwTQ1IRuoqFw1LyEigVi7Cr1WQpvXY2Vp6Uaf-GvxcPpo6XNMAytnY7MLyGcz2gA67f3AOLE-84QmWhujguHXZV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: بحث انتقال کریدورها به بنادر شمالی و مرزهای زمینی در دستورکار ماست.  @Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/435192" target="_blank">📅 22:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435190">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1143c6c122.mp4?token=KZHMly2rHLH-LN2rnXfg5acj0H96GzZzEItfJRnLMv3bo2f7aX1F3n6ZPG0N5uHdgK4n0ip5PAAAr1Ux_oHBb0d3lBM4FVlgQEsBVY8GAkXzHsGrW_JD89sksyOlGnKLTiR9rSmDzXMcg9XaiGOyYOuMRlsjJeeu2HH_0Sh72blC0ODfod5LswuaMOn4RRxMSFnl4YrCYDZ7IjqkqHqB2gJ0vdMaSFkiSiCxwjHYig6e-CSOdepnCuTZRGbfCLNI8epzrYlroZczTFGgGlU8SfCp1z70e_9MZtnVb5xWyLF_fDv76kcMt5_RucrRClZlzw-hF4qBhoSZiVWSbUBzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1143c6c122.mp4?token=KZHMly2rHLH-LN2rnXfg5acj0H96GzZzEItfJRnLMv3bo2f7aX1F3n6ZPG0N5uHdgK4n0ip5PAAAr1Ux_oHBb0d3lBM4FVlgQEsBVY8GAkXzHsGrW_JD89sksyOlGnKLTiR9rSmDzXMcg9XaiGOyYOuMRlsjJeeu2HH_0Sh72blC0ODfod5LswuaMOn4RRxMSFnl4YrCYDZ7IjqkqHqB2gJ0vdMaSFkiSiCxwjHYig6e-CSOdepnCuTZRGbfCLNI8epzrYlroZczTFGgGlU8SfCp1z70e_9MZtnVb5xWyLF_fDv76kcMt5_RucrRClZlzw-hF4qBhoSZiVWSbUBzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: متوسط زمان ترخیص کالاهای اساسی به ۹ روز رسیده و تلاش می‌کنیم آن را به ۳ روز برسانیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/435190" target="_blank">📅 22:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435189">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ed6ad1cc.mp4?token=jFbzq8eh3N85EwkUfcip51on0x8D6fOhq22kGymm9vvmnL1Kp3N2dKvue-yC4Q1orDKeN4Mmm2DSp_JE6PNZErYovFosBL4mLmAVpTcTh0IVYrOtZB1E4X7RnmuxqUFQIPsXXud7zy_U8r-1AxEfyeMB2kimyqbSzQdHcZVShY7E__1gGON7v3onlk9bMMGtvw-g72TE50rKtO0XRgKcrB5IcPk3jt9ONnuYWUZDnCwcqykCPsBwi0z8TXVsRody1mLQcsglSBbeibfQlyNpumcsnQUx7uZouB8LI678nVOuYjvNijEqTrwRJQ8SmWQ_EiOWF2hwkPlYI0rOkaih7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ed6ad1cc.mp4?token=jFbzq8eh3N85EwkUfcip51on0x8D6fOhq22kGymm9vvmnL1Kp3N2dKvue-yC4Q1orDKeN4Mmm2DSp_JE6PNZErYovFosBL4mLmAVpTcTh0IVYrOtZB1E4X7RnmuxqUFQIPsXXud7zy_U8r-1AxEfyeMB2kimyqbSzQdHcZVShY7E__1gGON7v3onlk9bMMGtvw-g72TE50rKtO0XRgKcrB5IcPk3jt9ONnuYWUZDnCwcqykCPsBwi0z8TXVsRody1mLQcsglSBbeibfQlyNpumcsnQUx7uZouB8LI678nVOuYjvNijEqTrwRJQ8SmWQ_EiOWF2hwkPlYI0rOkaih7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: کسب‌وکارهایی که تعدیل نیرو نداشته باشند، از دولت تسهیلات می‌گیرند
🔹
دولت از این واحدهای تولیدی حمایت ۱۰۰ درصدی خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/435189" target="_blank">📅 22:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435188">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">اقدام جدید امارات علیه حزب‌الله لبنان
🔹
دولت امارات متحده عربی خبر داد ۲۱ فرد و نهاد را به دلیل ارتباط با حزب‌الله لبنان در لیست تروریسم قرار دهد.
🔹
ابوظبی مدعی شد این تصمیم در چارچوب تلاش برای «تقویت همکاری‌های بین‌المللی جهت مبارزه با تأمین مالی تروریسم» اتخاذ شده است.
🔹
امارات می‌گوید کلیه نهادهای نظارتی موظفند هر فرد یا نهاد وابسته یا مرتبط با هرگونه رابطه مالی یا تجاری با افراد و نهادهای ذکر شده در این خصوص را شناسایی کرده و اقدامات لازم را مطابق قوانین این کشور، از جمله مسدودسازی دارایی‌ها در کمتر از ۲۴ ساعت، انجام دهند.
🔹
امارات که سابقه طولانی در حمایت از گروه‌های تروریستی دارد، ادعا کرده تلاش‌های گسترده‌ای را برای مقابله با افراط‌گرایی و تروریسم انجام داده است.
🔹
حمایت‌های امارات از تروریست‌ها در سودان و یمن، بسیار چشمگیر بوده است که رسانه‌های غربی هم به آن پرداخته‌اند.
🔹
روزنامه گاردین چندی پیش، در یک گزارش تحقیقی جدید فاش کرد که امارات نه تنها به نیروهای واکنش سریع سودان سلاح می‌دهد، بلکه به فرماندهان متهم به نسل‌کشی اجازه داده ثروت‌های نامشروع خود را در ویلاهای نزدیک باشگاه ترامپ و آپارتمان‌های برج خلیفه دبی پنهان کنند.
🔹
به گفته این روزنامه، فرماندهان نیروهای واکنش سریع که متهم به ارتکاب جنایات نسل‌کشی هستند، از امارات متحده عربی به عنوان «خزانه پشتیبان» و پناهگاهی امن برای پنهان‌سازی ثروت‌های کلان خود و اعضای خانواده‌های خود استفاده می‌کنند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/435188" target="_blank">📅 22:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435187">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58dc4d7e8.mp4?token=LchMulEpz3BS_PecmkMGAkQ5fH-HiVQqeUVckv3ssy9x01FzGWqHcl30eBFJUC2k0_oXwWF4YCNTdIDYE0jJhon0MkYxZrgH6I00b45bcfpG-K3t51AmyEf4BftTsPGWRV9tXnyjq_oStGZgxuJcXwxFZB6Ja2xBZfQht8veiP3FJAFfUlzEwuTvWHJtw5ujpeiaUa5AqLjt6Uz6h4Ml53HPUulIFJaIu2mLLdxUYiw230f4FvxuoDL-9W3N_enuVxhGuGmk335KGmWRSvJlvu4TicAPD077yzFqLxtzRLncR1Z248raxVc2VaY3AYU_YM-7H9NL7bULvrYNY-JEGptD9DblOhB4UG_8jQYKcOFF7FaBSpo2lyGTIDEGfoQY8q84OkBD9A4aMClbbzaDLZ9tPE_FncUJX-7jr5pBVANFTKtDrw4-d5fF4OgxHGnhOjVpZWSg7Owz6o6QRecm2YXDK7rinUEM7lRXYp2tW-za57MALPOTZyAP_fnfMDSnVr_NV6EB5bHle6iIszjpUuBxQHb_NUg8ytEjr60GMNm67IPFZtwyIySAfbtFZfhK15XKZVQVF-YuzvRwFqglBbD0_4G6KeHgJz7tFx53cinJwxOr0YjfsZHxm1_GpyDOrgLNdvv5zOCU50loFVhRl0_n4vJ1Ya_o-oe_QEsq7Qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58dc4d7e8.mp4?token=LchMulEpz3BS_PecmkMGAkQ5fH-HiVQqeUVckv3ssy9x01FzGWqHcl30eBFJUC2k0_oXwWF4YCNTdIDYE0jJhon0MkYxZrgH6I00b45bcfpG-K3t51AmyEf4BftTsPGWRV9tXnyjq_oStGZgxuJcXwxFZB6Ja2xBZfQht8veiP3FJAFfUlzEwuTvWHJtw5ujpeiaUa5AqLjt6Uz6h4Ml53HPUulIFJaIu2mLLdxUYiw230f4FvxuoDL-9W3N_enuVxhGuGmk335KGmWRSvJlvu4TicAPD077yzFqLxtzRLncR1Z248raxVc2VaY3AYU_YM-7H9NL7bULvrYNY-JEGptD9DblOhB4UG_8jQYKcOFF7FaBSpo2lyGTIDEGfoQY8q84OkBD9A4aMClbbzaDLZ9tPE_FncUJX-7jr5pBVANFTKtDrw4-d5fF4OgxHGnhOjVpZWSg7Owz6o6QRecm2YXDK7rinUEM7lRXYp2tW-za57MALPOTZyAP_fnfMDSnVr_NV6EB5bHle6iIszjpUuBxQHb_NUg8ytEjr60GMNm67IPFZtwyIySAfbtFZfhK15XKZVQVF-YuzvRwFqglBbD0_4G6KeHgJz7tFx53cinJwxOr0YjfsZHxm1_GpyDOrgLNdvv5zOCU50loFVhRl0_n4vJ1Ya_o-oe_QEsq7Qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: برآورد خسارات منازل مسکونی آسیب‌دیده در جنگ درحال انجام است و برای تعمیر و بازسازی و لوازم خانه منابعی توسط سازمان برنامه‌وبودجه در نظر گرفته خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/435187" target="_blank">📅 22:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435186">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رویترز: عراق و پاکستان مجوز عبور از تنگه هرمز را از ایران گرفتند
🔹
منابع مطلع به رویترز گفتند بغداد و اسلام‌آباد برای انتقال نفت و LNG از خلیج فارس، مجوز و هماهنگی لازم را از ایران دریافت کرده‌اند.
🔹
به گفته رویترز، این موضوع نشان‌دهنده نقش و نفوذ ایران در مدیریت عبور انرژی از این گذرگاه راهبردی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/435186" target="_blank">📅 22:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435185">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f724386e.mp4?token=pnXefLVBL27qviLgB7jFzoWJm19HOgZscLSXO_QGDVmxfeUY0PLmhK1a8njvgKeo1Rp8JlL_wLmvHlE8hJ3pVIh1hn3okXPjjueH5NQBfMUbcrYMmc34vd56h19sLYb5pozOTONe_GcMZECIKy_IM0yvTkptzaCFBn2Joa9ut-zej3OE3xfKCWwxn233POV5H869Oo_LHN58KoAtnROPEymsDXArZ8NzSqdMRhEu92Rt_Modff0ePoj78TYJlkaXy11_PNCoTWgrpODWnScZ0JMpsb2-le5Q5G_tqRqDlmjWx5Ain8tU0J_HLIaHsiRAUKmerDVbF9mmzNhLjoX4Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f724386e.mp4?token=pnXefLVBL27qviLgB7jFzoWJm19HOgZscLSXO_QGDVmxfeUY0PLmhK1a8njvgKeo1Rp8JlL_wLmvHlE8hJ3pVIh1hn3okXPjjueH5NQBfMUbcrYMmc34vd56h19sLYb5pozOTONe_GcMZECIKy_IM0yvTkptzaCFBn2Joa9ut-zej3OE3xfKCWwxn233POV5H869Oo_LHN58KoAtnROPEymsDXArZ8NzSqdMRhEu92Rt_Modff0ePoj78TYJlkaXy11_PNCoTWgrpODWnScZ0JMpsb2-le5Q5G_tqRqDlmjWx5Ain8tU0J_HLIaHsiRAUKmerDVbF9mmzNhLjoX4Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: در ایام جنگ با تفویض اختیارات، ادارهٔ کشور به‌صورت غیرمتمرکز انجام شد
🔹
بعد از جنگ ۱۲ روزه الگوی ادارهٔ کشور در شرایط جنگی را آماده کرده بودیم و بعد از آغاز جنگ رمضان، سریع روی آرایش جنگی قرار گرفتیم. @Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/435185" target="_blank">📅 22:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435184">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymzVNRfqBALhKbZAYI_K71hpw_ewlwQUa-lcEi0-PVXqlXmgDfZmloosuGBy9hI_InJzvbDaljmmTnhc3My-hHXeBiPzDn9MygyxlSWeFlq2MS0nIxobbnEuj2iQx_vepaBqY14pzP2QSXRBvf4eFUQJksAot0W-GgnkqaWiVimEceif8qzFXs6LO_HpquOYPpRmtDLpwsjVSBN4N76MeQnC8cPA3rRYB_SloK5dsI1KSRgB0RuRPU_0hRyHw9TA4vZFx0Wd3Ivn_0pxh9iVmHZUrVYpDQHEtlri7XZMhsSDBQt73Pk_OYDmEJwe_gv1ibL8-6BTaioiXPip4vmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۱ حادثه در تهران بر اثر طوفان امشب
🔹
قائم‌مقام اورژانس تهران:  تا حالا ۱۱ حادثه ناشی از طوفان تهران به اورژانس اعلام شده که ۴ نفر در محل درمان شده‌اند و هنوز روال درمانی مابقی مصدومان مشخص نیست.
🔹
مصدومان به ۵ بیمارستان امام حسین (ع)، امام خمینی (ره)، شهدای هفتم تیر، رسول اکرم و لقمان منتقل خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/435184" target="_blank">📅 22:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435182">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd2c68828.mp4?token=QcNrNRMcfrKBfc_yx9xEpu4sODCel1Nls_qlEMzwEIP6dc-hKv8T_EKj6d4xlfN9_VRHZN-BO6gGlsLoH85rAlEvXf0u9sJ3PdrLjPZz1FWbeiXxURxXurOCq_R5lAikOSee4SYKxwF1DLi0penTa2JVUt9hIpcffYH-VkUgCk-1q1qr5F5-WzKtrZnJCGfdUVKjgsfL6ddAAxCETxizlX6t30AhtxDPEpWnN1672ihRwV0uhfZ_xeclpqLvm9H1fUxTygqgHtXEkSoSMmTyerEPR4V4IOqraXNkBolAvbZ3Qw6x_QKcWOfn8-QbHNdIM61cjJAYxd652bPzqkWByFdvSNaS2BkjBE8_TPlQSj07wLI840b0C1YSIHvAbHZTO4rXqIVs5AKi2ruBB85KxG-KRpzeqGzjdgYs0F4Ap3juIcSqbg_i-WO3TNOdJnQr4TsKrCCzuoJ4x8rq9Dpc6jYhFj4F8drFHxyEXWiis4pKFIvVqLAV6rHxV451yXMqxv7QnvR60XSE3dIYiFcotBOxr5YUbxpqu_Q7AXtqrMapuozZy0WcCH3spPkT_6mQlozyakhMsZFtF8TkakoxKcO763xrxLBm1mvBrBQ7Z0fiJ5vdUrj7d-UlWA603oiKOCTDZPztdE9ZaFqLxRfisrRuQLgMPBDg-xHEhI3pA5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd2c68828.mp4?token=QcNrNRMcfrKBfc_yx9xEpu4sODCel1Nls_qlEMzwEIP6dc-hKv8T_EKj6d4xlfN9_VRHZN-BO6gGlsLoH85rAlEvXf0u9sJ3PdrLjPZz1FWbeiXxURxXurOCq_R5lAikOSee4SYKxwF1DLi0penTa2JVUt9hIpcffYH-VkUgCk-1q1qr5F5-WzKtrZnJCGfdUVKjgsfL6ddAAxCETxizlX6t30AhtxDPEpWnN1672ihRwV0uhfZ_xeclpqLvm9H1fUxTygqgHtXEkSoSMmTyerEPR4V4IOqraXNkBolAvbZ3Qw6x_QKcWOfn8-QbHNdIM61cjJAYxd652bPzqkWByFdvSNaS2BkjBE8_TPlQSj07wLI840b0C1YSIHvAbHZTO4rXqIVs5AKi2ruBB85KxG-KRpzeqGzjdgYs0F4Ap3juIcSqbg_i-WO3TNOdJnQr4TsKrCCzuoJ4x8rq9Dpc6jYhFj4F8drFHxyEXWiis4pKFIvVqLAV6rHxV451yXMqxv7QnvR60XSE3dIYiFcotBOxr5YUbxpqu_Q7AXtqrMapuozZy0WcCH3spPkT_6mQlozyakhMsZFtF8TkakoxKcO763xrxLBm1mvBrBQ7Z0fiJ5vdUrj7d-UlWA603oiKOCTDZPztdE9ZaFqLxRfisrRuQLgMPBDg-xHEhI3pA5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: در ایام جنگ با تفویض اختیارات، ادارهٔ کشور به‌صورت غیرمتمرکز انجام شد
🔹
بعد از جنگ ۱۲ روزه الگوی ادارهٔ کشور در شرایط جنگی را آماده کرده بودیم و بعد از آغاز جنگ رمضان، سریع روی آرایش جنگی قرار گرفتیم.
@Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/435182" target="_blank">📅 22:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435181">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVWkO2YrstraaClB6RwRJObIErenuLmhRbjodraXh5fyLaHE5ndelmK-x0rt-CnEPxSYB2E2UMewLvwXAcUG2yxGd8xCh6-b13X1N1C8a8tnwKMRh2IsBeW0enVqzfDAJULZ1LK7unfzO4HrgR1zlrZOHlZ4Q4vGDOq-8WMREj4pfKLZrflbT5zQPZ2YOrNsuz-O-PXE3zE0nGuQtMTEH7WE8ywaDRK1vFiDXKHoQEMNvuT2qmhxO2p_XZjGQM0mat5n4FHoXOPkEeG1wm5U0og8hC0j91B5z9ca1JCe7XwAMWBJDJX5Iy-zUW1wE6PG1DWsMwigzWVF7nG_Qr2rfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فولاد مبارکه مامور واردات ورق فولادی شد
🔹
وزارت صمت اختیار واردات ورق مورد نیاز بازار داخل را به فولاد مبارکه سپرد.
🔹
براساس اطلاع فارس از وزارت صمت، ارز مورد نیاز برای واردات ورق نیز تامین شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/435181" target="_blank">📅 22:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435180">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
مشق آمادگی دفاعی مردان و زنان در تجمعات شبانه!
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/435180" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435179">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
هفتادوسومین شب خروش مردمی در مراغه آذربایجان شرقی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/435179" target="_blank">📅 22:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435178">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d473b933bf.mp4?token=Fzg8iVjLDkcaYHjWoSWf3wCnCJXno0euV1eDKXFqUj8PDbxd2Kp5FuRCcajr3Vr1dqRjo5dyvltUu3Jqm5CtIuDdIegUnr4SFxK1IIFpWzHBv87PGlCQV3tNZO44wmzIvwExdKz2fOp7WmPv54GvHhsnjXJJn0ilzy8FNBdb724nJOI9h6N0sIbxEpinBhSncMHAx25qe9kuz-C6_XBoB8m6X6LKSIt_MRXJmPrlaHD9JnON2ERLy14mFo4bHKlSW_L4r2gK10TUWS__IfgreRdZasgZmhf19ievExG6EahQ3oPJGoZ5qJOdvLII7iks1knerm2mfZXeJBWk7u6iFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d473b933bf.mp4?token=Fzg8iVjLDkcaYHjWoSWf3wCnCJXno0euV1eDKXFqUj8PDbxd2Kp5FuRCcajr3Vr1dqRjo5dyvltUu3Jqm5CtIuDdIegUnr4SFxK1IIFpWzHBv87PGlCQV3tNZO44wmzIvwExdKz2fOp7WmPv54GvHhsnjXJJn0ilzy8FNBdb724nJOI9h6N0sIbxEpinBhSncMHAx25qe9kuz-C6_XBoB8m6X6LKSIt_MRXJmPrlaHD9JnON2ERLy14mFo4bHKlSW_L4r2gK10TUWS__IfgreRdZasgZmhf19ievExG6EahQ3oPJGoZ5qJOdvLII7iks1knerm2mfZXeJBWk7u6iFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله ۵ تانک مراکاوای دیگر هم شکار کرد
🔹
مقاومت حزب‌الله لبنان: طی ۲۴ ساعت گذشته  ۵ تانک مرکاوای ارتش صهیونیستی در جنوب لبنان را منهدم کردیم.
🔹
همچنین پایگاه تازه تاسیس اسرائیلی‌ها در منطقه بلاط در جنوب لبنان موشک‌باران شد و محل تجمع نظامیان صهیونیست در شهرک رشاف نیز هدف حملۀ پهپادی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/435178" target="_blank">📅 21:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435177">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07628c1387.mp4?token=vP-BDvxTzN1yly0iJ7i5zqUfGHbGRi1p27GaiphhEP5_2EVuiSuyME_tRx2tdOrMcWVE4VZypqQ3dTepa-W3l5cSXZbAateMDDvGnzgWioZn5syeBFEHCOtmGB2ozvGvOSIIflpHhr33BkTvYkRrrT9vpZIVw85PeI-gq4go-4S-g8tYb_7T-36iyRtRhde6O5aRki8qMxNnVA52IWzsroCEpPtjUjaD_Eqf6sNH4O4FjL_t0wFvuubGfRheLkCQBFOms_Y6gEzoxaTtYzTbCs5YdvIrvRZ4ETxHi8fM6TYJB_nyMqNUrEAle9fj_3hJeWfAf7dA9E9Sym-9xM7INg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07628c1387.mp4?token=vP-BDvxTzN1yly0iJ7i5zqUfGHbGRi1p27GaiphhEP5_2EVuiSuyME_tRx2tdOrMcWVE4VZypqQ3dTepa-W3l5cSXZbAateMDDvGnzgWioZn5syeBFEHCOtmGB2ozvGvOSIIflpHhr33BkTvYkRrrT9vpZIVw85PeI-gq4go-4S-g8tYb_7T-36iyRtRhde6O5aRki8qMxNnVA52IWzsroCEpPtjUjaD_Eqf6sNH4O4FjL_t0wFvuubGfRheLkCQBFOms_Y6gEzoxaTtYzTbCs5YdvIrvRZ4ETxHi8fM6TYJB_nyMqNUrEAle9fj_3hJeWfAf7dA9E9Sym-9xM7INg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تهدید جالب شهید
ناظری که سربازان آمریکایی را به گریه انداخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/435177" target="_blank">📅 21:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435173">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک منبع آگاه به فارس: ایران بدون انجام ۵ شرط اعتمادساز وارد دور دوم مذاکرات با آمریکا نمی‌شود
🔹
یک منبع آگاه تأکید کرد که پیش‌شرط‌های اعلامی ایران، تضامین حداقلی اعتمادساز برای آغاز هرگونه مذاکره با آمریکا است.
🔹
پنج پیش‌شرط ایران برای طرف آمریکایی شامل «پایان جنگ در همه جبهه‌ها به‌ویژه لبنان»، «رفع تحریم‌های ضدایرانی»، «آزادسازی پول‌های بلوکه‌شده ایران»، «جبران خسارات ناشی از جنگ» و «پذیرش حق حاکمیت ایران بر تنگه هرمز» می باشد.
🔹
ایران همچنین به میانجی پاکستانی اعلام کرده است که تداوم محاصره دریایی در محدوده دریای عرب و خلیج عمان پس از برقراری آتش‌بس، گزاره غیرقابل اعتماد بودن مذاکره با آمریکا را بیش از پیش تقویت کرده است.
🔹
بنا بر اعلام این منبع آگاه، مجموعه این شروط صرفاً در چارچوب ایجاد حداقل اعتماد برای بازگشت به روند گفت‌وگوها تعریف شده و تهران معتقد است بدون تحقق عملی این موارد، امکان ورود به مذاکرات جدید وجود نخواهد داشت.
🔹
بر اساس اطلاعات به‌دست‌آمده توسط خبرنگار فارس، ایران این پیش شرطهای ۵ گانه را در پاسخ به پیشنهاد ۱۴بندی آمریکا معین کرده است؛ پیشنهاداتی که به گفته منابع آگاه، کاملاً یک‌طرفه و در راستای تأمین منافع واشنگتن تنظیم شده بود. به گفته این منابع، آمریکایی‌ها در این پیشنهاد تلاش داشتند اهدافی را که در جنگ محقق نکرده بودند، از مسیر مذاکرات به دست آورند.
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/435173" target="_blank">📅 21:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435172">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37dea67a11.mp4?token=LqQV2_yVvCsjdzJfuqd_Z3aYWqNNzIp7ujeVBOQ5w8v-abJzbRHQW1QLL5J8ThjAaLbc3wIHSk7E5gfzKzDabHkIgLjZYHmpPxfjb-6mM1VaW-uIHYGV4-ZfpqYnNXOWN6mUD1XSWxFSuWt5FdI0UswUhfw6oRM4gUZ4PVXvFK4NiCF0WveVXxZ8dW1gPJV35vXmes3LgeBjgwEQumiWobE5eY1izvtYbzUHGmzGLF-wYWuUuupdOgwxkG9sr365UU2SL6N8IgOtvAZN8WAXz9mGUQG-bOaxa9i9Jw8TbgmEmdeD32WFgt8KXu_mVkBdYMjpmKm8Z5LG6uBuqU5G7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37dea67a11.mp4?token=LqQV2_yVvCsjdzJfuqd_Z3aYWqNNzIp7ujeVBOQ5w8v-abJzbRHQW1QLL5J8ThjAaLbc3wIHSk7E5gfzKzDabHkIgLjZYHmpPxfjb-6mM1VaW-uIHYGV4-ZfpqYnNXOWN6mUD1XSWxFSuWt5FdI0UswUhfw6oRM4gUZ4PVXvFK4NiCF0WveVXxZ8dW1gPJV35vXmes3LgeBjgwEQumiWobE5eY1izvtYbzUHGmzGLF-wYWuUuupdOgwxkG9sr365UU2SL6N8IgOtvAZN8WAXz9mGUQG-bOaxa9i9Jw8TbgmEmdeD32WFgt8KXu_mVkBdYMjpmKm8Z5LG6uBuqU5G7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ اصابت موشک حزب‌الله به محل استقرار  نظامیان صهیونیست
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/435172" target="_blank">📅 21:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435171">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تهران طوفانی شد
🔹
هواشناسی: از ساعتی پیش، وزش باد ۵۵ کیلومتر بر ساعت همراه با گردوخاک در تهران آغاز شده است.
🔹
توصیه می‌شود شهروندان از تردد غیرضروری در فضاهای باز و ماندن در مجاورت درختان کهنسال، سازه‌های موقت و تأسیسات ناپایدار خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/435171" target="_blank">📅 21:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435170">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299a972263.mp4?token=MAueGj6R9KdEAwWKJqCrv5qdt2RZyGEQPQT79CxrAUQLqEAJVkcf5KYsILXEFlayR0y355hrSkqhWtb-_k44U5-45f4404y9mMiBUDTeUWbxxwQnRcgC6EJlmA5qS0mpGyK2cVoqfUyGWIkCcWq5svA_nXK1eZcHU5ytNglChWG22v78RKHPySfqYjiaUi6UsOnkDGz98FF58oW0C-vOr2WYLf7HdC0c-q61cTuDYyiwet1j5OcOdZBJ-B8yN6VUFYCJuGhQfZZQVEBisZfh7ZtPTZyfcoPdRKV8vIUrVZ_cUfwsu5JKIXAfKTQ_95B-INXGdx26DiO1IKUwfVS7ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299a972263.mp4?token=MAueGj6R9KdEAwWKJqCrv5qdt2RZyGEQPQT79CxrAUQLqEAJVkcf5KYsILXEFlayR0y355hrSkqhWtb-_k44U5-45f4404y9mMiBUDTeUWbxxwQnRcgC6EJlmA5qS0mpGyK2cVoqfUyGWIkCcWq5svA_nXK1eZcHU5ytNglChWG22v78RKHPySfqYjiaUi6UsOnkDGz98FF58oW0C-vOr2WYLf7HdC0c-q61cTuDYyiwet1j5OcOdZBJ-B8yN6VUFYCJuGhQfZZQVEBisZfh7ZtPTZyfcoPdRKV8vIUrVZ_cUfwsu5JKIXAfKTQ_95B-INXGdx26DiO1IKUwfVS7ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروریست آموزش‌دیدۀ گروهک تروریستی انصارالفرقان اعدام شد
🔹
رئیس دادگستری سیستان‌وبلوچستان: بامداد امروز حکم اعدام عبدالجلیل شه‌بخش فرزند جلال، عنصر آموزش‌دیدۀ گروهک تروریستی انصارالفرقان اجرا شد.
🔹
در پی بازداشت عبدالجلیل شه‌بخش در جریان اقدامات ضدتروریستی…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/435170" target="_blank">📅 21:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435169">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">افزایش حقوق بازنشستگان تأمین اجتماعی امروز تعیین تکلیف می‌شود
🔹
خبرنگار فارس کسب اطلاع کرد، تکلیف افزایش حقوق و زمان پرداخت ۳۰ درصد باقیماندۀ همسان‌سازی بازنشستگان تأمین اجتماعی در سال ۱۴۰۵، احتمالا در نشست مشترک سه‌شنبۀ مدیران سازمان و نمایندگان کانون‌ها…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/435169" target="_blank">📅 21:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435168">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">معاون وزیر خارجه: رویکرد فعلی آمریکا مذاکره نیست، اجبار است
🔹
غریب‌آبادی: تاکید ایران بر اصولی روشن است: توقف دائمی جنگ و عدم تکرار آن، جبران خسارات، رفع محاصره، رفع تحریم‌های غیرقانونی و احترام به حقوق ایران.
🔹
نمی‌توان هم‌زمان از آتش‌بس سخن گفت و محاصره را ادامه داد؛ از دیپلماسی گفت و تحریم را تشدید کرد؛ از ثبات منطقه‌ای حرف زد و به رژیمی که منشأ تجاوز و بی‌ثباتی است، پشتیبانی سیاسی و نظامی ارائه کرد.
🔹
چنین رویکردی، مذاکره نیست؛ ادامه سیاست اجبار با واژگان دیپلماتیک است.
@Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/435168" target="_blank">📅 21:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435166">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682dd68c95.mp4?token=MyWNhvN5NWXBLWlZZyO5ibnZhcxfOVX6POLTuVFym5rzhF6IcqF1dT4GRV11BNwWzVuM5GDD6T2AAaAQ2s3_dBifq8mjusKE2fVR207F9-tG4uyRlfS3aL_uYR1jVbfnDnQdQLVmg2KI4P5ko0NZBXWJvd_a10iN1BCtpO13T7h2sO_7YtRQ8qErV9bkdbwiwCphHc1xK4UipjqQP4hF3CK9jo2eHLlk2qy5GwMPHHnVkfK2TUf_f-Q_ruXoCQZslNePaxck4_u8E6Rm_EzigdN3_4Vi6rVfaGTqu5SqGrut6Ig4Uuv9yNUCbFrOhOtj00lYoN314ao5wxs-CcJmhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682dd68c95.mp4?token=MyWNhvN5NWXBLWlZZyO5ibnZhcxfOVX6POLTuVFym5rzhF6IcqF1dT4GRV11BNwWzVuM5GDD6T2AAaAQ2s3_dBifq8mjusKE2fVR207F9-tG4uyRlfS3aL_uYR1jVbfnDnQdQLVmg2KI4P5ko0NZBXWJvd_a10iN1BCtpO13T7h2sO_7YtRQ8qErV9bkdbwiwCphHc1xK4UipjqQP4hF3CK9jo2eHLlk2qy5GwMPHHnVkfK2TUf_f-Q_ruXoCQZslNePaxck4_u8E6Rm_EzigdN3_4Vi6rVfaGTqu5SqGrut6Ig4Uuv9yNUCbFrOhOtj00lYoN314ao5wxs-CcJmhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کریس کونز، سناتور آمریکایی خطاب به وزیر جنگ آمریکا: شما در جنگ با ایران موفقیت‌های «تاکتیکی» دست یافته‌اید اما در آستانهٔ یک شکست «استراتژیک» هستید، چون ما اکنون درحال مذاکره هستیم تا فقط [تنگه باز شود].
🔹
وزیر جنگ آمریکا: این حرف خیلی احمقانه است!
🔸
کریس…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/435166" target="_blank">📅 20:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435165">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWnDurrsaxRyXcz3GgPPFX6evLusybGwQpr6BNaX1Whqfd7mjdGGGnkaUHPycUxl5B1XTFhjc0ogGMowFABwABRB4kbhFsZHyJ2xJsvMUIBcL8sltfGpdaGPdkskJ9Hqo5pdEei4dHb8rgv_dFFTdFckG4bRD4gt4g00EiebxQy-sz5HvK3U9mbYJMeJZGEdky7BlO1QdJ6GQ5t7_btUokVvbekU5qDDsjscDuNhULmQD-Nmity6sKHgxtFmMEuajX6sJM2mpj56QtVUiUgiU7pzDf7MvtZtVBZOitAVPLrK1S_zTUeKiRfmAhS-BTqRrSdYFJo4EkjlUyPnfxvB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: حاکم بحرین ۲ هزار شیعه را زندانی کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/435165" target="_blank">📅 20:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435164">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/005efbb538.mp4?token=NtzhxvAU8pfcVhrkckF8oWknZNzqByj3ohlzuQ4nDAvODvjHPvEQf6H1IXv7vwqY8fD2va-rIAGOvrkZZIdXGqperJfcn0e0uqfklGHiS4yHyhgpcxvBcSQOhp1wsaa2UImvZIaqgkQwLI50pbfscYgsE_J5Hp84Itcu4iqlxnP4h_v8DDhjL0BqxW8eVFKwzumHuhiCWr1Sk6r1JYelk44sLCBpV2t2lHYg-uRyzcDnB9Qv5Dq1XpL4vwWrHJPTaNQrVR0WgPUxYssUPa5RzPcEvk0fkhg3tEvLR7fxF4yM6iuRxhmGQOGZR5KdM5pPLilR7eq7bs5DCNDv1L2jyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/005efbb538.mp4?token=NtzhxvAU8pfcVhrkckF8oWknZNzqByj3ohlzuQ4nDAvODvjHPvEQf6H1IXv7vwqY8fD2va-rIAGOvrkZZIdXGqperJfcn0e0uqfklGHiS4yHyhgpcxvBcSQOhp1wsaa2UImvZIaqgkQwLI50pbfscYgsE_J5Hp84Itcu4iqlxnP4h_v8DDhjL0BqxW8eVFKwzumHuhiCWr1Sk6r1JYelk44sLCBpV2t2lHYg-uRyzcDnB9Qv5Dq1XpL4vwWrHJPTaNQrVR0WgPUxYssUPa5RzPcEvk0fkhg3tEvLR7fxF4yM6iuRxhmGQOGZR5KdM5pPLilR7eq7bs5DCNDv1L2jyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی خطاب به وزیر جنگ آمریکا: شما ادعای کنترل تنگهٔ هرمز را دارید اما مشخص است که تردد کشتی‌ها در دست ما نیست
🔹
کریس کونز: آقای وزیر، شما همین چند لحظه پیش گفتید که «ما کنترل تنگه را در دست داریم». اما کاملاً مشخص است که بازگشایی تنگه هرمز برای…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/435164" target="_blank">📅 20:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435162">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3953e09c1f.mp4?token=Krr2CP1byjfxduihE3CWkJE7RCHHBNz2-nWbY3sB0aWXmoXf0qbAHcfrMDf9kwjkd5uqIrZvJXK6DhYAKq44-UWs3GsGAwDC-5rHJbZmzUwg9YKRl2ACupFhPn-YdHWSRXX2dZktLl7bhoMwmuvVJ63mR4F-5oNRXgXBrTIwtROa427pl-mNM320tomRrJojbJMzxPPys9dU6sfEtfpXvusRLwlrfcyl0y7yTLSQX7tvmiZYcSalKTbe9c7ro_bdPhf_FSvEtk_HuWriRQ8CgJCAfyXZcT8OveqZ2AaJIcMkv5Amp-27HdkG_fc_JJg2dX11J8GrR_ZBAizDeS-CoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3953e09c1f.mp4?token=Krr2CP1byjfxduihE3CWkJE7RCHHBNz2-nWbY3sB0aWXmoXf0qbAHcfrMDf9kwjkd5uqIrZvJXK6DhYAKq44-UWs3GsGAwDC-5rHJbZmzUwg9YKRl2ACupFhPn-YdHWSRXX2dZktLl7bhoMwmuvVJ63mR4F-5oNRXgXBrTIwtROa427pl-mNM320tomRrJojbJMzxPPys9dU6sfEtfpXvusRLwlrfcyl0y7yTLSQX7tvmiZYcSalKTbe9c7ro_bdPhf_FSvEtk_HuWriRQ8CgJCAfyXZcT8OveqZ2AaJIcMkv5Amp-27HdkG_fc_JJg2dX11J8GrR_ZBAizDeS-CoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی خطاب به وزیر جنگ آمریکا: شما ادعای کنترل تنگهٔ هرمز را دارید اما مشخص است که تردد کشتی‌ها در دست ما نیست
🔹
کریس کونز: آقای وزیر، شما همین چند لحظه پیش گفتید که «ما کنترل تنگه را در دست داریم». اما کاملاً مشخص است که بازگشایی تنگه هرمز برای تردد تجاری همچنان از دسترس ما خارج است؛ و دلیل عمده‌اش این است که ایران ذخیره قابل‌توجهی از پهپادهای ارزان و مرگبار «شاهد» را حفظ کرده و رقبای ما نیز در حال کمک به آن‌ها برای بازسازی این ذخایر هستند. آقای وزیر، برنامه شما برای بازگشایی تنگه هرمز چیست؟
🔸
وزیر جنگ آمریکا: بخش عمده‌ای از سوال شما بسیار غیرمنصفانه است.
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/435162" target="_blank">📅 20:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435161">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675f7d368f.mp4?token=q-xhCi995L8zIGM1ELS9I_6gSn3DAzBS73GIIWmrzYmxlVQDSYaYHM8Hww9utowe4wc3RdYBtev1M707K94WRiLmDmgo-Cx5RDWMs8km_szpB26UQdJdL2rkYmhAmApmEsTJnfXs3mYseHyQzjtFPeBaSY_HVqDUgfLjDrDNBxhVlN_YHBH23WbuXFJHpqT0ySTS8D3bkBvnSgFYtk4zw84LZvTBNAp0pRc-J4-_YqpG-XSKv_VDAiISBSYdeICqRG39kvUtGyOhpPh1uAtqDueeqE-BhnyofwWMbLCFVQajTjSUnHoR9s25B--wzrGcZz-fI0k14jD9bYfVkp25xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675f7d368f.mp4?token=q-xhCi995L8zIGM1ELS9I_6gSn3DAzBS73GIIWmrzYmxlVQDSYaYHM8Hww9utowe4wc3RdYBtev1M707K94WRiLmDmgo-Cx5RDWMs8km_szpB26UQdJdL2rkYmhAmApmEsTJnfXs3mYseHyQzjtFPeBaSY_HVqDUgfLjDrDNBxhVlN_YHBH23WbuXFJHpqT0ySTS8D3bkBvnSgFYtk4zw84LZvTBNAp0pRc-J4-_YqpG-XSKv_VDAiISBSYdeICqRG39kvUtGyOhpPh1uAtqDueeqE-BhnyofwWMbLCFVQajTjSUnHoR9s25B--wzrGcZz-fI0k14jD9bYfVkp25xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری منوتو صدایِ نوجوان ضد جنگ را هم تحمل نکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/435161" target="_blank">📅 20:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435160">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5bb8f93b5.mp4?token=pqGx5MtQs5mi2gTur6xpEAFCMvKBmi0KCvS4BfCrLCcchwvTcJhZv1aPKZa8q9BTzPoD5II6ZA9TCup9xFViVrRDtDYu3s14CjtXCqe3iYpY4NFMYEgW-fDxl-QAxo1Kuvcp8xHiGMCnS1DdCDMZW70dFizj3pwPcT4Or92lb7Njy120fYC1qVOOd6gu1Q4UIjy5J7swEvuuHPoZDMl7LMMwkF_1AXy3VycFR71W_4L8hE2JJy3sPghGEIlnp3tY2_Y9dBpk5Gh8Ib7MGfdoY1aK9UQ3RRSGTxlIPKEaoA4rt6n7Zkw75_2RvCcGr0qBHfGmnyUgF8KCB4XRB6gkqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5bb8f93b5.mp4?token=pqGx5MtQs5mi2gTur6xpEAFCMvKBmi0KCvS4BfCrLCcchwvTcJhZv1aPKZa8q9BTzPoD5II6ZA9TCup9xFViVrRDtDYu3s14CjtXCqe3iYpY4NFMYEgW-fDxl-QAxo1Kuvcp8xHiGMCnS1DdCDMZW70dFizj3pwPcT4Or92lb7Njy120fYC1qVOOd6gu1Q4UIjy5J7swEvuuHPoZDMl7LMMwkF_1AXy3VycFR71W_4L8hE2JJy3sPghGEIlnp3tY2_Y9dBpk5Gh8Ib7MGfdoY1aK9UQ3RRSGTxlIPKEaoA4rt6n7Zkw75_2RvCcGr0qBHfGmnyUgF8KCB4XRB6gkqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس دفتر رئیس‌جمهور از آخرین دیدار شهید لاریجانی با پزشکیان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/435160" target="_blank">📅 20:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435159">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_XhgI648R_tByBDhFJF41qIHThkhocRU8C8BBguB-1sh0dXjg66HWTRTlySWo8GaK6ikKPmqdm9EASEBVHdI2DaQmoWNC5df5GpXdWYpjxdo7iG_JbRJ_GH4fclmlu92Axs4YN36ykiFy6qZfGPJ5NelJaLbno8x7Su_cU_GP0wk0wHrp4ccdrWdGJmC0ZALqXzLeQloEGTTzThj3HLtYs0pCrMo8hxthAjDrs3q06tAkaLGjoUuE1F3jQ9_-xoq3xO-bdpI1lS-b2rOyG4TJAnc9nTWs17pYFZzrokiskjHLL9ESaTPssW6Go4NbN6mPkGy1gw0otWitRN9PEh1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴.۵ همت کالای قاچاق و احتکار شده توسط اطلاعات سپاه
ِ
اصفهان
🔹
اطلاعات سپاه استان اصفهان چندین هزار تن کالاهای اساسی، سوخت، لوازم خانگی و مواد پتروشیمی احتکار شده و قاچاق به ارزش بیش از ۴.۵ هزار میلیارد تومان را کشف کرد.
🔹
همچنین یک انبار بزرگ حاوی ۱۶۸۰ تن الیاف مورد نیاز بازار پوشاک به ارزش حدودی ۱.۷ همت که در سامانه جامع انبارها ثبت نگردیده بود، توقیف شد.
🔹
پرونده مجرمان جهت رسیدگی به مراجع قضایی ارجاع شده‌است.
@Farsna</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/435159" target="_blank">📅 20:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435157">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f0907b65.mp4?token=bWwSnnJTemj9lqGvUedCmUaFIMcapbiLq1DgwzSnH5hRuhdYvt088XZAQFsDAcDdvB93RhPuxIpVWZp7dBEj-AtYIm0dAWtF6xKTfYi4ObXBTIJChlCMQJAibZmZQrFR-G2VpKDxIvepJQBegPGTVw6d58MXqMS6ABOMZNqIIlMfXef_3E9XBR8U1OhsJwbk29_8Kbw24TLfdThu20fDDOOMxYIx9sLSPm-SP6KxEABR3zMQkBFm4A7zQ15YX08PPq6vxaJxutNXzRxwl4eAKWq2R2140BAo48ol5rYN_6_umsaJXU0tMmDcIVUdE1SKlXeuWxJPf0MKllfop1Ug2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f0907b65.mp4?token=bWwSnnJTemj9lqGvUedCmUaFIMcapbiLq1DgwzSnH5hRuhdYvt088XZAQFsDAcDdvB93RhPuxIpVWZp7dBEj-AtYIm0dAWtF6xKTfYi4ObXBTIJChlCMQJAibZmZQrFR-G2VpKDxIvepJQBegPGTVw6d58MXqMS6ABOMZNqIIlMfXef_3E9XBR8U1OhsJwbk29_8Kbw24TLfdThu20fDDOOMxYIx9sLSPm-SP6KxEABR3zMQkBFm4A7zQ15YX08PPq6vxaJxutNXzRxwl4eAKWq2R2140BAo48ol5rYN_6_umsaJXU0tMmDcIVUdE1SKlXeuWxJPf0MKllfop1Ug2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
واشنگتن‌پست: ایران حداقل به ۲۲۸ ساختمان یا تجهیزات در پایگاه‌های آمریکا حمله کرده است
🔹
این حملات شامل آشیانه‌ها، پادگان‌ها، انبارهای سوخت، هواپیماها و تجهیزات کلیدی رادار، مخابرات و پدافند هوایی بوده است.
🔹
میزان تخریب بسیار فراتر از آن چیزی است که دولت…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/435157" target="_blank">📅 20:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435156">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr1pygj68PeRoe_iliZeWqafgmZzll_IvdjKrAu8VOKWUrC6sGTn9RU-lH9W6ZEOYajIODt0DnrdrE43rOFIqbWRgiey7peIEarXIgec6FG-2_sNHRZ3d7wqRSpfJETEx1CA1NC91dFaJp4TO4pvCOUIzRzgQ2qcpAbTCC03qoR30TN5x2tAhnVkq3oelZh7iBj37rGXI0s549hXqTfJ-FoJtJIB-hXEs4rJjEPMm9pRk43nSnfYZJFGJAiM1yT_ynjbPHlqM2CMTiDagTSjZoAEOz1gqRlIjQxTfoD6HFvq4wHywwBr7MIjpR2M6U3gTRAt-b4eC3uLCoSgi7FDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج یک پیمایش ملی از ابعاد پنهان تجمعات شبانه
🔹
یک پیمایشی درباره تجمعات شبانهٔ ایران که با مشارکت ۴۳ هزار و ۳۹۱ نفر در بازه زمانی هفتم تا یازدهم اردیبهشت سال جاری انجام شده، ابعاد مختلف این حضور جمعی را از منظر انگیزه‌ها، تجربه اجتماعی و پیامدهای آن بررسی کرده است:
🔸
۹۴.۸ درصد پاسخ‌دهندگان اعلام کرده‌اند حضور مردم در تجمعات داوطلبانه و خودجوش بوده است.
🔹
۹۳.۱ درصد شرکت‌کنندگان با این گزاره موافقند که نهادهای مردمی نقش اصلی در سازماندهی تجمعات دارند.
🔸
در شاخص «توجه و شکر نعمت وحدت» میانگین امتیاز ۸۷.۵۴ درصد ثبت شده است.
🔹
۹۱.۸ درصد پاسخ‌دهندگان هم معتقدند در تجمعات بر حفظ وحدت اجتماعی تأکید زیادی می‌شود.
🔗
شرح کامل پیمایش را از
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/435156" target="_blank">📅 20:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435155">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TluJEUrjG2D1iwcaoenpuBkZa1KQ72x1dX2HvUPoTz1SaCYUKgII0eQn2nW_-STcMMkJ95AlQfraCQXwwegLw4f6vYriYWSbGeh1E_XDY3VQbOpbnU6cYpC4Lrmo8ypFJ-W2_ye80EtTLlcmsRNAh_Id1APEdex8Ty_hpA7mAdnGJfnYl1kdPPvEep4M3iUZjAVhe2H6_9XMVdWzhPhZhyvx1Y-fv40Oqt3ES2yo_KpQIxv9Dxr6EocMTAhRtZScpAMdbMIvMGH-8Mrnb5MMUABoFodsCneWP2tul3vzUFoEoKoq2RZkhYBl0mXTL3ciMRc3SkkTL4E31Y-XSiML9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد پر گل تیم سفید ایران مقابل تیم قرمز
⚽️
گلزنان بازی:
علیپور، ایری(۲)، یوسفی، حسین‌زاده
⚽️
تیم سفید ۴ - ۱ تیم قرمز
@Sportfars</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/435155" target="_blank">📅 20:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435154">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c11c0a8608.mp4?token=DlBraGikJloX6MxG_TBdERW0eoQlkeMMyWNRLN3RvmDE6py1h6I4O4NHbQLdsMFz9xGmfUHTb2SiYHrygd3GsK1FTqCChbxPG4z83rSv7UrtM3miOAo_KgfO1s2lg6-qhBFgzGeRFCM3yGV2MPY7YlNuXBSRZvlND6LBDfuPvM6O3UANCD4B8GJca0DJwkXQyrkCOUHPrRtFfpvKdp2_p-Rp7nhsgU00RfpwepC4j82z_nz02MfBLsq9PHIFDRS3wQjHj38FOcP_NCkrxpUHlkM0uuzGCiFKcWrRInbW4X8essI12LLPYgxqXEfv4IBE52qcHLG91-tnef85k8w_1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c11c0a8608.mp4?token=DlBraGikJloX6MxG_TBdERW0eoQlkeMMyWNRLN3RvmDE6py1h6I4O4NHbQLdsMFz9xGmfUHTb2SiYHrygd3GsK1FTqCChbxPG4z83rSv7UrtM3miOAo_KgfO1s2lg6-qhBFgzGeRFCM3yGV2MPY7YlNuXBSRZvlND6LBDfuPvM6O3UANCD4B8GJca0DJwkXQyrkCOUHPrRtFfpvKdp2_p-Rp7nhsgU00RfpwepC4j82z_nz02MfBLsq9PHIFDRS3wQjHj38FOcP_NCkrxpUHlkM0uuzGCiFKcWrRInbW4X8essI12LLPYgxqXEfv4IBE52qcHLG91-tnef85k8w_1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحهٔ حماسی کریمی در میدان انقلاب: «رهبرمون هرچی بگه همونه»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/435154" target="_blank">📅 20:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435153">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKZK8QROVSnMY29sYMkTKgizLm-SRmfDNciFsQaj_Pdf9k1RFxEszPugEBkYOnqcNSyYudkX8HTQs7XDiYQCg-YCGWurbLAdJMFtAJbZZKsGwOWJGmh0zON6ZF-I-BNFIbOYoZr9-ApudBLDBkVHT0t1HhXecigeXBK-T7GqpByELDIC3HILrR3Ohl-HvhzMaLe8UXZXF8SJSglbISYfsKM9sTlTNs5q7PeQ-ZNA9-C52TtlTKeQARSloKIa7vIygiR4L5XYSZGXgnNje_vq2xkt7rfiml42oQFaMwPk2HfkEpZ1yauvYoUbQhkCv95RfEGQqE_Qn9VJ1h9nKpPwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افرادی که وسط جنگ هم دست از افزایش قیمت خودرو برنمی‌دارند!
🔹
طاهری، عضو کمیسیون صنایع مجلس: ایران‌خودرو با مدیریت جدید نباید هر اقدامی را بدون توجه به سیاست‌های کلان انجام دهد.
🔹
پیش از این بارهاهشدار داده بودیم که واگذاری‌ شرکت‌های خودروسازی از نظر ما با تعارض منافع همراه خواهد بود.
🔹
انتظار می‌رود قوه قضائیه به‌صورت جدی به این موضوع ورود کند زیرا تصمیمات مدیریتی در حوزه خودرو مستقیماً بر زندگی مردم اثر می‌گذارد.
🔹
الان کشور گرفتار افرادی است که وسط جنگ خودرو را گران می‌کنند.
🔹
حتی در دوره‌ای که مدیریت خودروسازان دولتی بود، اگرچه مردم از وضعیت خودرو رضایت کامل نداشتند، اما سیاست‌های کلان حاکمیت در حوزه قیمت‌گذاری رعایت می‌شد و کم‌تر شاهد تصمیماتی بودیم که در شرایط حساس کشور موجب افزایش قیمت‌ها شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/435153" target="_blank">📅 19:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435152">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db78859303.mp4?token=Agf_mUVlwSyIqYn1N1LbdsYmkeM0AYpEDVQ8vXwlXlF3JfJ4jp4Rmzx1ppAR4eDupxI_ScxUSj4HhboEU7WV0HUkms2SFCBBL5rcaZX_tzZWFc4yA9mepemBLuM4fxFlKC55mJ8l-q9dOWbz8ZWyYoIx-JzineVZ1P0gUJO_CHCdzHLIRXU581bR-iQfLjzZfDNGzuTGmmhM94G6Y1RY4EIWE1AQEFDR9bEcxpuCuEesyCTPnjQ4n-5sPtFDIUdVxyuBl140xGu-sQkMloBdKPUdPebLiR-EJGFQ7Oc8-ZDszzQ5kxaB92GgAVzdCH-_qSD7ZdCLu2aDP0k6DHv7-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db78859303.mp4?token=Agf_mUVlwSyIqYn1N1LbdsYmkeM0AYpEDVQ8vXwlXlF3JfJ4jp4Rmzx1ppAR4eDupxI_ScxUSj4HhboEU7WV0HUkms2SFCBBL5rcaZX_tzZWFc4yA9mepemBLuM4fxFlKC55mJ8l-q9dOWbz8ZWyYoIx-JzineVZ1P0gUJO_CHCdzHLIRXU581bR-iQfLjzZfDNGzuTGmmhM94G6Y1RY4EIWE1AQEFDR9bEcxpuCuEesyCTPnjQ4n-5sPtFDIUdVxyuBl140xGu-sQkMloBdKPUdPebLiR-EJGFQ7Oc8-ZDszzQ5kxaB92GgAVzdCH-_qSD7ZdCLu2aDP0k6DHv7-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هزینهٔ جنگ آمریکا با ایران ۴ میلیارد دلار بیشتر شد
🔹
نماینده پنتاگون: چند روز پیش برآورد هزینهٔ ۲۵ جنگ میلیارد دلار بود اما در حال حاضر فکر می‌کنیم این رقم به ۲۹ میلیارد دلار نزدیک‌تر شده است.
🔸
پیش از این سی‌بی‌اس فاش کرده بود که هزینۀ واقعی آمریکا نزدیک…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/435152" target="_blank">📅 19:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435151">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40069255e.mp4?token=qMnwb2sjNSnN_KRVcQETGkbRhNaGhRLM-PVcH3ZhAzkvxUVmR8EUb1jhRkN2fRhRnLXf4IElw572MYsiO_jNOyinVsYFXQ_xpoIW7V5snmWDyuMUNs-EBiMcrjkqm8ur-UrXrXBABgnk6pykCBqkAxwTpqQyy7Twg3mVUyfFtI_ta7Iu5KuXzXvHeA6Y9GNrxQkaIFOXG1nm5I97Y8BQiai6SK-xsjLJlPd30K_517atYByzJegZB4RkhTyODL_sB7LqTmE8fkCWUvVvFJQatcMQXoFMOiJzxC42NjlDbJj_PbiDGw7g47AJUQQ2fnEtrTpPo4H8OHULMaQKvFUVVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40069255e.mp4?token=qMnwb2sjNSnN_KRVcQETGkbRhNaGhRLM-PVcH3ZhAzkvxUVmR8EUb1jhRkN2fRhRnLXf4IElw572MYsiO_jNOyinVsYFXQ_xpoIW7V5snmWDyuMUNs-EBiMcrjkqm8ur-UrXrXBABgnk6pykCBqkAxwTpqQyy7Twg3mVUyfFtI_ta7Iu5KuXzXvHeA6Y9GNrxQkaIFOXG1nm5I97Y8BQiai6SK-xsjLJlPd30K_517atYByzJegZB4RkhTyODL_sB7LqTmE8fkCWUvVvFJQatcMQXoFMOiJzxC42NjlDbJj_PbiDGw7g47AJUQQ2fnEtrTpPo4H8OHULMaQKvFUVVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده کنگرهٔ آمریکا: طبق گزارش‌ها ما تا یک ماه پیش در جنگ با ایران ۳۹ هواگرد از دست داده‌ایم که برخی از آن‌ها جایگزین ندارد
🔹
اِد کِیس، نماینده کنگره: طبق گزارشی در پایگاه «وار زون»، ما حدود ۳۹ هواگرد از دست داده‌ایم، که البته آن گزارش قدیمی است. متعلق…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/435151" target="_blank">📅 19:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435150">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70a136fd5.mp4?token=qju5tKiaINhie0JAPlzNgS56d4OtjqUcf9ilL9bJxch8VDA5T3GWgl-OCivKOem3K1vTRfvReSG37MKizba3U6nbSiXk1_EJoKdpbZsZRYpyLE6xpwfem7pnzqhqXj9NhJUiVXE0wkdcr3BPKaeIBgAqa4yV6o-Cf89gRF4qfmHg0Fb9Amg3z9W7dvd8iOaFLce2aF68QFZzv474TVUx91U-x7Emmq_kNSVNkLih7qwVkW0AG5yoLpbXozs73GsdG70Duui3BiGq1Bxu2Rj11DRJHOmja11842ybIakfmi8fr8BLXZ80tW5HE24v2G39LkGpEJXWcJjEvSGVtdd0TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70a136fd5.mp4?token=qju5tKiaINhie0JAPlzNgS56d4OtjqUcf9ilL9bJxch8VDA5T3GWgl-OCivKOem3K1vTRfvReSG37MKizba3U6nbSiXk1_EJoKdpbZsZRYpyLE6xpwfem7pnzqhqXj9NhJUiVXE0wkdcr3BPKaeIBgAqa4yV6o-Cf89gRF4qfmHg0Fb9Amg3z9W7dvd8iOaFLce2aF68QFZzv474TVUx91U-x7Emmq_kNSVNkLih7qwVkW0AG5yoLpbXozs73GsdG70Duui3BiGq1Bxu2Rj11DRJHOmja11842ybIakfmi8fr8BLXZ80tW5HE24v2G39LkGpEJXWcJjEvSGVtdd0TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده کنگرهٔ آمریکا: طبق گزارش‌ها ما تا یک ماه پیش در جنگ با ایران ۳۹ هواگرد از دست داده‌ایم که برخی از آن‌ها جایگزین ندارد
🔹
اِد کِیس، نماینده کنگره: طبق گزارشی در پایگاه «وار زون»، ما حدود ۳۹ هواگرد از دست داده‌ایم، که البته آن گزارش قدیمی است. متعلق به تقریباً یک ماه پیش است. آیا هزینۀ جایگزینی تمام آن هواگردها را می‌دانید؟ با این فرض که برخی از آن هواگردها قابل جایگزینی نیستند، اما قاعدتاً باید آن‌ها را با نوعی ظرفیت و توانمندی جایگزین کنید.
🔸
نماینده پنتاگون: هزینه‌هایی در این مورد وجود دارد، اما می‌خواهم جزئیات دقیق آن‌ها را به صورت مکتوب به شما ارائه دهم. چون همان‌طور که می‌توانید تصور کنید، محاسبه هزینهٔ تعمیرات هواگردها کار بسیار دشواری است. ما می‌خواهیم پیش از برآورد هزینه، یک عیب‌یابی کامل از هواگردها انجام دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/435150" target="_blank">📅 19:15 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
