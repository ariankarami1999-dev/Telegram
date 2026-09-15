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
<img src="https://cdn4.telesco.pe/file/XlybhMHHXus_8rIZ9HXFN1RiU_E-J-r8TScup7v0Xgmid0t2eurvIziNoKfToJckJ1dR6FoVdkudzRmJkNpIiH-WE06cSJaoQM4pflNZtC7yL3hUZmoxiDIjoBR7bmyK_vZom8zxz4t6grmO2XcOV-458Oo0t6Npv7hQ_3JiE7M1vtkCdVw0rgO_6ZpSrVLMKxjcK-ARPMVYviZb4s0UZ1lEAeKxGqoalf0HnSN793cOgUnKsYUXm6zQ2aIIx2aC1YCIJdsckVMM0bl6dJFGF7--ldlAPd6lyw2vjXxTodKLAQyQ3Pd85Zkw81bAAv2vy6zq7xxDK0WRTRKMwciY-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 19:33:43</div>
<hr>

<div class="tg-post" id="msg-462266">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89efe83b5.mp4?token=k66PJk7QnzGYdC8fTqvPcD8M3el3PK2fpUUvGIhAfPbCQxNg_Wcy4TFAbsEXquJC2QZAT7QsSV8gE8NYJQBXDvKfkR8KKfUjXjQSGPhV6g-tnonNB-4QH5XYROwMy1Y74OZbT8L8Lcu0A7i9vJYV15WOGm_QV4NxSu4F1CKmqeFFo8_YXYtHtqbt5c_TOyq9DXBGxXXxu0FlPSUJUuFPXXvSPSn8hFiMkZmcwP4r13CiUgCmtd41qy2JBlkkV79M48igLep7kUjbz9K7ffPjJAOjB36nmEP2qOxmUqByiOQZYNwGoRAMj_xQ2v92s3GRoPUL7nfjZzymwN-nMbocWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89efe83b5.mp4?token=k66PJk7QnzGYdC8fTqvPcD8M3el3PK2fpUUvGIhAfPbCQxNg_Wcy4TFAbsEXquJC2QZAT7QsSV8gE8NYJQBXDvKfkR8KKfUjXjQSGPhV6g-tnonNB-4QH5XYROwMy1Y74OZbT8L8Lcu0A7i9vJYV15WOGm_QV4NxSu4F1CKmqeFFo8_YXYtHtqbt5c_TOyq9DXBGxXXxu0FlPSUJUuFPXXvSPSn8hFiMkZmcwP4r13CiUgCmtd41qy2JBlkkV79M48igLep7kUjbz9K7ffPjJAOjB36nmEP2qOxmUqByiOQZYNwGoRAMj_xQ2v92s3GRoPUL7nfjZzymwN-nMbocWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات
:
بیش از ۵۰۰ سایت ارتباطی در جنگ رمضان آسیب دید اما ارتباطات مردم حفظ شد
@Farsna</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/farsna/462266" target="_blank">📅 19:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462265">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFC21iUVdkEthGkWjKfu3kkaheGlSPB2PF-LGlHpr5fAbBOLi3bDXVBfChCeRNgS89ZF3Huz1By3YQrds6ti7DpXhCamrdn7iUgwRgkIaDk2RWZc4g_W2p53lUxNcoV17u0wdI8msnGrS43_GlVdh1yIwlix4-8IDDc3wnvNalidqqqlzazL5Me8R8EzHiNlFw8gpZIRj5Q82uByysPHE17giaFrzanO0TdkWlatPgFB1fUCB5TprCU16Z9UL_EfoozZmkAo74d0nSWyd7iar0T4YSJZjxiP2lO7RdAM5Mw5zlkpRe5-YFdzFcjRe1XqcwNUMGcrrQ6-3CliIRmtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار عظمایی: گلوی جهان‌خواران را رها نمی‌کنیم
فرماندۀ نیروی دریایی سپاه در پیامی نوشت:
بسم الله الرحمن الرحیم
﴿وَنُرِیدُ أَن نَّمُنَّ عَلَى الَّذِینَ اسْتُضْعِفُوا فِی الْأَرْضِ وَنَجْعَلَهُمْ أَئِمَّةً وَنَجْعَلَهُمُ الْوَارِثِینَ﴾ (قصص، ۵)
🔹
ای ملت شجاع و تاریخ‌ساز ایران عزیز؛ سلام و صلوات و رحمت الهی بر شما بندگان برگزیده‌ی خداوند، که در این برهه‌ی تاریخی، چون موج‌های خروشان، با حضوری حماسی و حیرت‌انگیز، برای دویستمین شب پی‌درپی، در خون‌خواهیِ رهبر شهید امت اسلام و در حمایت از مظلومیت مردم ستم‌دیده، قیام کرده‌اید.
🔹
ای مردم نصرت‌یافته‌ی خدا، اقامه‌ی خون‌خواهیِ شبانه‌ی شما که برگرفته از مکتب عاشوراست، اوج حقیقت را بر پرده‌ی سیاه ظلم در این عالم به نمایش گذاشته و چون توفانی، کاخ ظالمان را در هم شکسته و جهانیان را متحیر ساخته است.
🔹
امروز دویست روز است که در کنار قیام شما، خلیج فارس و تنگه‌ی هرمز از حضور پلید ارتش تروریستی آمریکا و دشمنان اسلام پاک شده و تنگه‌ی هرمز در مشت‌های پولادین رزمندگان اسلام است. به اذن‌الله، گلوی جهان‌خواران را رها نکرده و اجازه‌ی تکرار و حضور مجدد و ظالمانه‌ی آنان را نخواهیم داد.
🔹
دلاورمردی رزمندگان اسلام در جبهه‌ی جنوب و در دریاها، وامدار استقامت و حضور باصلابت شماست؛ شما که تمام رنج‌ها را بر خود خریدید و در برابر همه‌ی حوادث، بصیر و آگاه بوده‌اید.
🔹
بنده سلام همه‌ی رزمندگان در جبهه‌ی جنوب و در سنگرها و خط مقدم را به شما می‌رسانم و ضمن طلب دعا برای نصرت و پیروزی رزمندگان اسلام، خاضعانه توصیه می‌کنم «این حضور مقدس را با اتحاد مقدس گره بزنید» تا ان‌شاءالله، با هوشیاری و حمایت از رزمندگان، دولتمردان و فعالان جبهه و جهاد، از این گردنه نیز با به‌کار بستن رهنمودهای حکیمانه‌ی مقام معظم رهبری، حضرت آیت‌الله سید مجتبی خامنه‌ای عزیز، عبور کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/farsna/462265" target="_blank">📅 19:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462264">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6gqgy6VtyBhJUVNEgKq1Y7pfxw80duUwJXjxxXsbOix8mYmn58rix5erSoEyeTtOpQbs8xCMBG2eqxPGIqj3K8LE68PLxdSj9qlKiXazMMkC5nTw2AXqxVBnUPdJsjEkofEBhq1DTUIdFHrvnK-uopdx29gSbbhrGdkpsbSBU9HsBUlOAXOSWQYMb8KqTQA9JGo-Ps47BzDRWeMbNQ4f4I4Dl0L1a7kGZJFNu2AvvuWGQQjr-mUJDpuMd0Ez8jse2y6y3BFxs4euS_RfzWyHQVL-_zOZKH7C362Do2E51tHo2_uTX0BCXboE3TnOTarbUn0qDUhYJtFxaZ_IDWHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم صهیونیستی خبرنگار پرس‌تی‎وی را ربود
🔹
پرس‌تی‌وی: نیروهای نظامی رژیم صهیونیستی خبرنگار نقا حامد را در یک ایست بازرسی نزدیک به بیت‌لحم در قدس اشغالی ربودند.
@Farsna</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/farsna/462264" target="_blank">📅 19:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462261">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCpdLM0KmEi8MXwAhYwCyuof5jLSaayikMxGvroqx4y78v0QiFQw-8w3vBUzMeD0xSNPBKO7bdog3P5TGUrtmOKz2MeTyUypvxHcoJ0olr9tOhfaacoD2L2Yh2Lex87RleTbjBBo9sGcNEGeLxrNMzKTykYyYaPkXrh5nMld_6md1ihC_STgjZkV5XlBjB-ceKthbaCapM1R7vd9IKMsbC5asMpQovVuoEuToYSO2xXEWFhedLU4k_QGzH8cas80NYiKwNtpf_igCx9aJD91uhsNFmCrB4VlnptOAlAJQtzZXuhA8xfONd8Su9NXL3St33SKC3HvGOTYavDP6kosSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: جوان با اراده ایرانی می‌تواند موضوع بهینه‌سازی انرژی را نیز حل کند
🔹
سردار ابن‌الرضا: همان‌گونه که جوانان ما در وزارت دفاع و نیروهای مسلح در برابر هجمه بالاترین سطح فناوری دنیا ایستادگی کردند، برای مقابله با آن راهکار پیدا کردند، و موفق شدند و همان جوان ایرانی و همان اراده می‌تواند موضوع بهره‌وری و بهینه‌سازی انرژی را نیز به بهترین شکل حل کند.
🔹
در کنار اقدامات فناورانه، باید به موضوعات فرهنگی و رفتاری نیز توجه کرد و این اقدام را به یک نهضت برای بهبود بهره‌وری و یک مطالبه بسیار پراهمیت تبدیل کرد.
🔹
در جنگ ترکیبی، یکی از شقوق این جنگ، تحریم‌ها به‌ویژه در حوزه انرژی است و اقدام در این زمینه را بخشی از جنگ و دفاع از کشور می‌دانیم.
@Farsna</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/farsna/462261" target="_blank">📅 19:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462260">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af96054db5.mp4?token=B8fwYX9J1-3kaDCeJaHi78-_JGyIunx36sdf2AjuSVZV4oqhzaxadDNtt75H1j7kqbkUEwo7Xf2-NheJjMU8HKr9L_eDwbowJ4pqn6OkmH8fqXWFh8vZIaPyITM9UHj3D4jviBsmfxfQqylv_bzsXIU_KOOhZBYw__5SFCfpl4DAjXwL2hngF5GMc3r-E8fQwXHuwv0dCoeWp6v8nejmAlsxKTN2PQMqOIPBJ7RuDl10nYHLWuN8jqzI5csLS1vG6zXSBW4-Ng_mVBXZfM2QzWxFI1gbfM6LRMv9XECkQR4R7RQgY_Ko5uYLhkhpaLPcSg4V9DMfGm8CzinLuqi3VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af96054db5.mp4?token=B8fwYX9J1-3kaDCeJaHi78-_JGyIunx36sdf2AjuSVZV4oqhzaxadDNtt75H1j7kqbkUEwo7Xf2-NheJjMU8HKr9L_eDwbowJ4pqn6OkmH8fqXWFh8vZIaPyITM9UHj3D4jviBsmfxfQqylv_bzsXIU_KOOhZBYw__5SFCfpl4DAjXwL2hngF5GMc3r-E8fQwXHuwv0dCoeWp6v8nejmAlsxKTN2PQMqOIPBJ7RuDl10nYHLWuN8jqzI5csLS1vG6zXSBW4-Ng_mVBXZfM2QzWxFI1gbfM6LRMv9XECkQR4R7RQgY_Ko5uYLhkhpaLPcSg4V9DMfGm8CzinLuqi3VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون برق و انرژی وزیر نیرو: با کاهش ۳ درصدی مصرف برق، حدود ۶ میلیارد یورو صرفه‌جویی شد
@Farsna</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/farsna/462260" target="_blank">📅 19:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462259">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8aa349978.mp4?token=SPMIF8zkzbBAfSzlyhDXpFmi18kibH0WXHMkotDgjGzBUiXKhxTq9iz1DcHUHVeqRA8KpgG_0zt1fqkp9UqJAPi5UQSFzPmO0Nfa37resxOFGx4_JjiXLSXRIJcmmOCtsV319XUkYoH3thtUbl5kO51nNbARSU-hvVlQUfxfqehMrMoNDbJlSH4nDjBfbb8giigsIqAlFvX6u1e2buHyIHGr2TSaZFp5AWd--GoDE88c7lk7uVepwj9_-qSyrkhrGnzlVcqP5tU7ArnstIbTPxZ1iToYu_LJCGewXe-CztHsxhOfeI-ppE13QbCHSd6uIbOXrw4tprJ22HomgJUvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8aa349978.mp4?token=SPMIF8zkzbBAfSzlyhDXpFmi18kibH0WXHMkotDgjGzBUiXKhxTq9iz1DcHUHVeqRA8KpgG_0zt1fqkp9UqJAPi5UQSFzPmO0Nfa37resxOFGx4_JjiXLSXRIJcmmOCtsV319XUkYoH3thtUbl5kO51nNbARSU-hvVlQUfxfqehMrMoNDbJlSH4nDjBfbb8giigsIqAlFvX6u1e2buHyIHGr2TSaZFp5AWd--GoDE88c7lk7uVepwj9_-qSyrkhrGnzlVcqP5tU7ArnstIbTPxZ1iToYu_LJCGewXe-CztHsxhOfeI-ppE13QbCHSd6uIbOXrw4tprJ22HomgJUvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بحران مسکن زیر سایهٔ خانه‌های خالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/farsna/462259" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462257">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f75bf3da.mp4?token=UgsR3JcW_ncpEke1OFao9uR7-wJLJQ2oeyFLC-2TBq6BlsKkyuUP8x1-EmjlXgLjjR5ByJad59BzL3LTebyAHaVUlNyyVHDUzT1LlcUEEVU_CGnEfM8J70iIIFcQmSMiyRHKxVcCL7n_zl1sgwWGhwcimpt1YipKOCgCdo0CnLOeXo5sAAmscozI_9LECk8_umUtgjdyQMj0nNmR3vsaZguNxwyk7IW2fr-KBcCXZQ1bRuanEUlt60VWkYAqet_nrJXWghWEbISA7zy317cd4ucj8o_bd-aQYQ3gRqI0yE_AxUhfL4UZVz8NYf4tqYWu1Uz5wm600K_09K0a9mnOK4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f75bf3da.mp4?token=UgsR3JcW_ncpEke1OFao9uR7-wJLJQ2oeyFLC-2TBq6BlsKkyuUP8x1-EmjlXgLjjR5ByJad59BzL3LTebyAHaVUlNyyVHDUzT1LlcUEEVU_CGnEfM8J70iIIFcQmSMiyRHKxVcCL7n_zl1sgwWGhwcimpt1YipKOCgCdo0CnLOeXo5sAAmscozI_9LECk8_umUtgjdyQMj0nNmR3vsaZguNxwyk7IW2fr-KBcCXZQ1bRuanEUlt60VWkYAqet_nrJXWghWEbISA7zy317cd4ucj8o_bd-aQYQ3gRqI0yE_AxUhfL4UZVz8NYf4tqYWu1Uz5wm600K_09K0a9mnOK4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
برخورد یک سوپرنفتکش متخلف به مین‌های ایرانی تنگۀ هرمز
🔹
نیروی دریایی سپاه: سوپر نفتکش «الگایا» به شماره دریانوردی 9325336 که قصد عبور از منطقۀ ممنوعه در جنوب تنگه هرمز را داشت، بر اثر برخورد با مین‌های دریایی منفجر شد؛ تلاش برای مهار آتش بی نتیجه بوده و…</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farsna/462257" target="_blank">📅 19:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462256">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-8Ckya-KurFl6J4wyBmiHmTUW783LCB7xCDg4B-mjc17iUXYkvRUfK5TWGH1d-JGyLXogh9-l75BcEoGvQpm1ZnSZO2sRMkPV3hVnufAdntGOqMHiNGUlTja5kppiONbtlqnlLtzTQamuO9r4a_XIQsPuAmjFFJm3FrjbGud2GO268Dx8ofVG8S37QNaM2sHy06-f3XIAlHXzg9XlSWEMT7PlMkQceUYte07vZctV-MbkHBbdnyUpBA5uqvw0IS-cfiiVFf_euaNC2TkYf-V75g6vegbXRDNXE4rTY0SZPXPlfIU8XA5kPjsBkX3lJF2qNlKxGeEPKLPp_KJ5H_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: توطئهٔ‌ آمریکا در مرزهای غربی ایران شکست خورد
🔹
رئیس مجلس در دیدار رئیس اتحادیه میهنی کردستان عراق: در جنگ ۴۰ روزه آمریکایی‌ها طمع داشتند که از سمت اقلیم کردستان عراق اقدام امنیتی و نظامی علیه ایران انجام دهند.
🔹
اما با کمک دوستان شما در اقلیم و عکس‌العمل به موقع نیروهای مسلح ایران این توطئه دشمن شکست خورد.
🔹
آمریکایی‌ها و رژیم صهیونیستی همیشه به دنبال این هستند بین همسایگان مخصوصاً بین ایران و عراق اختلاف ایجاد کنند؛ به‌ویژه در شرایط حاضر که مجبور شدند هم سرزمین و هم آسمان عراق را ترک کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/462256" target="_blank">📅 18:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462255">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVer5aNuq0Mu__CrsdjEtOj3MmU2-a35MOtT8iS4lR_EePMimc3mZHKKG0yp5kTFlXFirlY-e-VvkdH-rGNAcuEFnsS26ksRCTqUQZDVRl90svoH9upoioT4D9-mjerOmaiLecdhXGRkta7vMp32yfOD-YXVElhc8wKENMS6qF3dNvXTQ0Fhr2LdliG9wDp0pscoYDJ9-qlmq8qgVNXU0TtBp0IGxQ1q7VBw7J-VneeQHhm6ug7zbJaXilBUyccNOtAE9K9LLTLl1mrYii0gfsLmn65dd8Tjz9igKciu4RZBxYjCPSrzVfXCTtX_NfJ5f6gWtQ9i7aB2CaWGddsK4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: ۲۰۰ شب است که پاسداران کیان ایران‌مان، زیر باران بمب و گلوله و در میانه‌ جنگی تمام‌عیار، استوار ایستاده‌اند. آنان که دیروز همراه نبودند، امروز با آغوشی گشوده به صف ملت پیوسته‌اند.
🔹
پرچم عزت و فتح برافراشته است و امیدهمچنان درجان این مردم زنده. ملت مبعوث عزیزند و عزیز خواهند ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/farsna/462255" target="_blank">📅 18:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462254">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎥
ابرپروژهٔ عربستان تکه‌تکه شد
🔹
تصاویر ماهواره‌ای جدید نشان می‌دهد حملات اخیر یمن به زیرساخت نفتی عربستان به چند نقطه از خط لولهٔ شرق–غرب سرایت کرده و ایستگاه‌های پمپاژ این شریان ۷ میلیون بشکه‌ای را از مدار خارج کرده است.
🔹
در تصاویر آثار سوختگی در حوالی…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/462254" target="_blank">📅 18:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462253">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0qFRbIv2CEWwuYxC1u48QyytchytPK2WIVnwJUFY1QT3jYsFR5JsaqsSMfvIaWjijyShqfaHyII7fImcIdf4lyArLn8kghxSU3rJLPKvvLmxSGhi-CLFiFzCk8WWXjPgUF5SB0l4uty1oaJnxKzMj5IonSoR7NevdJcFYdZB64o9YznAk99p6mktpM7CZxeLed0i0WwW-sjJwB43bYzpFhNri_TyoZVo0jMEC7qYOriASA-MUcFZmSNorFAVedVhLn07DGB1SxlTczAUgOM5B7BWvIBd-gBTBo8AViHd_4aUHdtOZ2lgcwJAxvybhzVR4jvqAwlerhyzQGiua_DFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای اف‌بی‌آی دربارهٔ خنثی‌سازی حمله عضو داعش در آمریکا
🔹
اف‌بی‌آی اعلام کرد که یک مرد ۲۱ سالهٔ اهل پنسیلوانیا که در حال طراحی «یک حملهٔ خشونت‌آمیز» در آمریکا بود را بازداشت کرده است.
🔹
جاناتان هانتر کرِیمر، ۲۱ ساله، اهل والنسیا در ایالت پنسیلوانیا، با نام «حمزه الرشید» شناخته می‌شد و براساس شکایت کیفری فدرال وزارت دادگستری، وابستگی خود به داعش را اعلام کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/462253" target="_blank">📅 18:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462252">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11785309b0.mp4?token=Frk9EGYrrx0D6hivkmP2O3bTCCWEqGZmQUneUhFZM5scu7eRn2fqxWqjarDA_GJ8qMSKU05aeg53wgfsj0Z3ja7XLsEmX4osco5DzPPMGcZRgJ_IApM6R_CXeG-ZmGh8Kxpapfpr2RjvVmICauS4vBqpW1CS06vutQQNq0FiLI4QJkdD0wzMiFzL8p1um02fII6LYgDip8rAPbmmeQnc02CO_hlEBmHIcD54qGV87wPBh9jBJF1NMRlXp3jz3AjW_uBnrdYZ001gKV5NB4gKkYYu2lbhB0YoY59tl5NEd3AzquFphsUd2bXwn3IsQqkUJvbxC302s9YjoRRbjiOn6Lg13HloFiYKu0P-p0Z0eteH47xpexSfZmiUXQNv8VA9xPc9fYls8kGvzS613_xrWgAgbvTzSUr3uk7boHmXl-38V3Wwg2e2aPe3aVwFqdMhBLdbioqP0clw4M1KlRMvLNvSLzOzLHlhGI4Z_wZFGEO71coicqxiMHVcuZLvo7N2Jpks1FYXOlw1l9zlG3wlgsoAV8uIT8zYehQ7YsqV7cGXURuul7shnNxgVr_EqEGB1c85DqSt-8mDuWqEic08mLF6d2k5Su2eycm3KYFNBSbXGc6Oj3TBkRv1H4zGWNOp-MCRnDnrs1T6juNr-prSkoxwbmncI5Nb129Qw928WiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11785309b0.mp4?token=Frk9EGYrrx0D6hivkmP2O3bTCCWEqGZmQUneUhFZM5scu7eRn2fqxWqjarDA_GJ8qMSKU05aeg53wgfsj0Z3ja7XLsEmX4osco5DzPPMGcZRgJ_IApM6R_CXeG-ZmGh8Kxpapfpr2RjvVmICauS4vBqpW1CS06vutQQNq0FiLI4QJkdD0wzMiFzL8p1um02fII6LYgDip8rAPbmmeQnc02CO_hlEBmHIcD54qGV87wPBh9jBJF1NMRlXp3jz3AjW_uBnrdYZ001gKV5NB4gKkYYu2lbhB0YoY59tl5NEd3AzquFphsUd2bXwn3IsQqkUJvbxC302s9YjoRRbjiOn6Lg13HloFiYKu0P-p0Z0eteH47xpexSfZmiUXQNv8VA9xPc9fYls8kGvzS613_xrWgAgbvTzSUr3uk7boHmXl-38V3Wwg2e2aPe3aVwFqdMhBLdbioqP0clw4M1KlRMvLNvSLzOzLHlhGI4Z_wZFGEO71coicqxiMHVcuZLvo7N2Jpks1FYXOlw1l9zlG3wlgsoAV8uIT8zYehQ7YsqV7cGXURuul7shnNxgVr_EqEGB1c85DqSt-8mDuWqEic08mLF6d2k5Su2eycm3KYFNBSbXGc6Oj3TBkRv1H4zGWNOp-MCRnDnrs1T6juNr-prSkoxwbmncI5Nb129Qw928WiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد مردمی جان‌فدای ایران: تاکنون ثبت‌نام در ۵۸۲ گردان از مجموع یک هزار گردان کامل شده است
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/462252" target="_blank">📅 18:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462251">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌ انهدام یک فروند پهپاد پیشرفتۀ MQ1 در تنگۀ هرمز
🔹
سپاه: لحظاتی قبل چهارمین MQ-1 در چند روز گذشته به وسیلهء آتش سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان شرق تنگه هرمز رهگیری و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/462251" target="_blank">📅 18:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462246">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S28MsoNylIAYOjESI6DXQDOO6lulcPUvXB4aJA11L7rpD3zwx83huCDN9NE06DEZzOE0TEw79wpUsUPy_O39HezdRkJzGbkA9mRci-uUytuiprNwQ8wOArFJUBFaHXdGpqrN0GT0RZoglfTtt8Zng8aelK9oHd5SAW3LiRvBvQVqbUlLP-Lh33Xj4yt7n73Cp-zJgfugQvgvk4gON9p1QEzFjPkkJWiwBkplc2SUojtVIG3s1GEfR6w8ZUWXmTR3vaCuhBU7z0CDgVoGVxMDnW-bOIwGOFjMrfmG6ePBGDNYxS_sSbXiHYpYWuGdesFwsu6k7fsEy_K3xUrtbCLESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5ePqZD-UiBm5vuKn85ycM_XQJCIe_aKUzsWljV6HHTT8Xqo3drj-SaC3Sy6UUIbGIlyJ0K0v-YPbdzVrS8Y0NwvwZXtitVNtIk5aI-wX1jPJrhqNJjnzoxkuB-kM4fPFNuLFUPQIDl8S1FQL4EC1X2qfxY0qYUOm0wAcf309tK6uNP9_TlCpSSIUnw8ej41jPcJAzSl2ePu2rauEmmn9MmnU-H3m45PToCaizINAdEDoFsP2tlq_J2tjcq4lSQUkvro9XW-TmSTAyblPrWbKRzN4fxkgGNnQeQFGRKN246Wjf4Yz0OkKjmmwJjt0fazldw84Niw-d34F7LzTbzgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsO-e_NNypjCjUAKnQn1_-NKz1gz-KXs9UDHSdQPBqNMYJB53cMAsh66HQQqAg55_ZAmJwNX-4-rDlZFCEITmuPR_ovdZvHHerFPplXUnhowhySROV-j4zRoKUHc8dUobFyAB5o8pryupkm8BYkwyLnuHSQAekyuZXyhA_6LOXfNOzL2aqYQM4YTVEW7HkP620-Gb0IO5vVR5lSuA5mjozAh-96tOkLtdw_rPNzzBUJEwhZ_DfjleDzoSpomZUUkEEReX8htaeea8sN32WkljwpREf7wiUYLOZqkAw8hp3HptT0DGsYvMMad7OcJO3gVvHficoQKG6aav-6xT0nMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhQzW7ESaA2WCZmtJddYZO7ALG9y0i8yRV6_Qlgm5GP4n2gFC7bSN8OC4RsUJiikijugSGsmxPB3biFV-n63GQMWKve1HC_5BJWjT0pf0duGjkD_s3OEAMlbsofDhq9LePaswjI9dVEHLXhq3OTHfypYtZIqMHnfeqQ4etnMRggoRHAT8WBKfQWURwXUwKBA9-oFssIzGbPWdlSLrRaaWfJSEImgzjnZkTk5QscAfU1n62NAyOVIs97II4KAQRIn6bUXvNNQZflAVZLQFOLYJCR-WztjtUE7Ysx-ygcxdeMQ3LT2PKELWm8EcQIWvEXs5geQ2cSKm-0O0dtfQyG2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsOOnWYd7Ywzd_VcS41uiHyZk6G10IXLY7TfXEJLEMQVsnbgr01YUpGGHLWwfTywlAP0EJ6C-38XuWHTpeKQ7-6hHCoGWQgTptLuiu7al4Gf-JgecD4YwG-zfFNPm0rUCM_mAxaYoz14uyjEWRGa3BuH8grR7rOLHKii5fvVT_rLgxf5bVR6Wf9P1SNVwzIZzVXuFmPoipLhZFUymBBXRHb1_WP4RrAMmIpj-jyUkhe2VnciazAGgEFtC19VxbQQM7jLBP8gtYT4t2HvxsIK6v2U9rpRRt1ud1b9vFPhRWH5Zb723HxLQU7qaZq6hzyMVlxFxI8uD-tXUSPuGU3eBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار رئیس اتحادیهٔ میهنی کردستان عراق با قالیباف
@Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/462246" target="_blank">📅 18:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462245">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYGtWtuBVU4U-BGJ-Av3L8l6z58zOWVETHHfzkcifU2W8wYGNZl1mh7IIQJtV6Jfgs8TsPpP8UNkfMKbjSSSGnZDVWA7biR-mgh6S3eSh7icanC0BsbcoW3ccSpnoPf3IvdVgiCQe4X1VrrGwXZSm_mcnT_zPULiAUlt23RitK9_icTaWxIsakyAalfFe-xx6dj188PiSs-zT6dSbrQyZLfMRnp2zv9H5uhcsGZt0ehLr4Nd6wiH-_PoTBJHVXUgyX0atO2-svoinNZl1-kzk3msNk4RIaEQLv4fmCtApmdva0MNIebZVqPaGRlZMG68_TrYqhbBxLWQMGg-xnw-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل از دریای سرخ حذف شد
🔹
روزنامهٔ اقتصادی عبری کالکالیست:  تسلط نیروهای یمنی بر تنگهٔ باب‌المندب، تجارت دریایی اسرائیل را از هرگونه بهبود احتمالی در حمل‌ونقل دریایی جهانی حذف می‌کند و این رژیم را وادار می‌سازد به استفاده از مسیرهای جایگزین پرهزینه ادامه دهد.
🔹
این در حالی است که اسرائیل در ماه‌های گذشته جنگ غزه، تحت شدیدترین محاصرهٔ دریایی تاریخ خود از سوی یمن قرار داشت و خسارات سنگینی متحمل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/462245" target="_blank">📅 18:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAQvIkP2DALQBbulgLkwN9B_I_yt3jxGX0OYWxfbebtgcgmXWsybqwHaDtRRm1_q-_u67eVAoQNnBd_DZLXOsK_kVV0pMpKnwNd_Ik_O7m8ajygYq9Qh0QSIDs6lyQrSL7KukThV2rUWov1nFRMRLSTqvzsMv4C5x2CuC5rJQkjTxy18MGW28bpqf1qFxhtUMyOmKjJTP9fVAVROVfT6lH5NaQllpr7Te4i7XEY8eEn3WKj5If8AmDd-ZJbAdXpT8fVVKmSHjeV9zow2TUt6NiP2kw2Xen2ib1881deP0i0VHbkIDr0r-Dzg3t8R02HS_lBxfq6AuZsOOURpxyEzCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا «نسل زد» پیر به نظر می‌رسند؟
🔹
نسل زد، متولدین ۱۳۷۵ تا ۱۳۹۱ ، بیش‌از نسل‌های قبل در معرض فشارهای مرتبط با زیبایی و مراقبت‌های پوستی قرار گرفته‌اند و برخی رفتارهای رایج می‌تواند باعث شود جوانان این نسل پیرتر از سن واقعی خود به نظر برسند.
🔹
مصرف زودهنگام رتینول و محصولات ضدپیری، استفاده از بوتاکس پیشگیرانه، استرس مزمن، کم‌خوابی، کم‌تحرکی، مصرف ویپ و بلوغ زودرس از جمله عواملی هستند که شادابی چهرهٔ نسل زد را تحت تأثیر قرار می‌دهند.
🔹
فشار ناشی‌از مقایسهٔ چهرهٔ واقعی با تصاویر فیلترشده در فضای مجازی نیز می‌تواند استرس و نارضایتی از ظاهر را افزایش دهد.
🔹
داشتن روتین سادهٔ پوستی، خواب ۷ تا ۹ ساعته، مدیریت استرس، فعالیت بدنی منظم، ترک ویپ و تغذیهٔ سالم از راهکارهای حفظ سلامت و شادابی پوست هستند.
🔹
پذیرش روند طبیعی تغییرات چهره و پرهیز از استفاده افراطی از محصولات و روش‌های زیبایی نیز می‌تواند به حفظ سلامت پوست و روان جوانان نسل زد کمک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/462244" target="_blank">📅 17:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462243">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">صدور کیفرخواست پروندۀ کثیرالشاکی گلباران
🔹
دادستان شهرستان دزفول: پروندۀ شرکت نیوساد گستر ایرانیان موسوم به گلباران که بیش از ۸۰۰۰ شاکی دارد، طی ماه‌های گذشته در دستور کار مراجع قضایی قرار داشته و در روز‌های آینده برای رسیدگی به دادگاه صالح ارسال خواهد شد.…</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/462243" target="_blank">📅 17:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462242">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHzizlvWQ-_6WS-fzru3BYPzpzRPLrE5tHzZ-E_wG0A0St_2q7oXHIelRRUmv2q1mEtLtruSqMRs0yoOnxw8eH8L8LLht0wmvhxjcMM4VbwaAnRsd-n-DZ0mHrocNOJrMKWkWdw2dHeShaJ9Typ1xzrS2KaIFLywIcYwzLyco1B5FpduJUHaVP9SqRorm3ZuseLXIO2G_GEodZtJuDHthjXdboGYo3So-C_FpB_JyPE9oikC4TVamiM1g01xd0ZwMdveU8YAJsTV2Xsp7gh_JDlO6yQmzoTBlrZROQEIXPRctsEXjHH-FTAGJbKhD3CgsVfxgN6eFh9k8jCsNcXLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرایهٔ نفتکش‌ها تاریخ‌ساز شد
🔹
بلومبرگ: داده‌های بورس بالتیک لندن نشان می‌دهد کرایهٔ روزانهٔ یک ابرنفتکش در مسیر خلیج فارس به چین روز دوشنبه به یک میلیون و ۳۵ هزار دلار رسید؛ در حالی که پیش از جنگ این رقم حدود ۱۱۲ هزار دلار بود.
🔹
این رکورد شکنی قیمت در شرایطی ثبت شده که تنش‌های نظامی در تنگهٔ هرمز شمار کشتی‌های حاضر برای عبور از این آبراه را به شدت کاهش داده است.
🔹
کرایهٔ ۱۵ روز سفر یک ابرنفتکش از خلیج فارس به چین حدود ۱۵ میلیون دلار می‌شود که نسبت به ارزش ۲۱۶ میلیون دلاری محموله ۲ میلیون بشکه‌ای، حدود ۷ درصد از پول نفت را می‌خورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/462242" target="_blank">📅 17:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462241">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665377c745.mp4?token=ik6K0DGPhOpK5vPekhr6RgSVezY1XvWk-WohP541_AA2vKMQgbQ_4m3p8qopr7gQ77xPMDCOL4ItT4wDGHdN5b7PgfiyphNCd-5awgZwsnrbmU8x9ji_ZxVnPZalipa_G1-jjbNQSzl0cUTBTwUOdGP3tvLLia2MLRvqpzStY6HDk7KO9jzLd0ytRzTInbAKDYhVSqzSmBgnvabJS2yNEhoP9cwL-FU8aX1O8293EqoO50hce7PogcyjYlq98cayzb_ttCID1J89mHrRcMIA3b1x0LdnnBPdKn4jdXEjMszWpyr7mBWdC5DIowLLV4asMqVowB4mJLQub2qKFA-UFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665377c745.mp4?token=ik6K0DGPhOpK5vPekhr6RgSVezY1XvWk-WohP541_AA2vKMQgbQ_4m3p8qopr7gQ77xPMDCOL4ItT4wDGHdN5b7PgfiyphNCd-5awgZwsnrbmU8x9ji_ZxVnPZalipa_G1-jjbNQSzl0cUTBTwUOdGP3tvLLia2MLRvqpzStY6HDk7KO9jzLd0ytRzTInbAKDYhVSqzSmBgnvabJS2yNEhoP9cwL-FU8aX1O8293EqoO50hce7PogcyjYlq98cayzb_ttCID1J89mHrRcMIA3b1x0LdnnBPdKn4jdXEjMszWpyr7mBWdC5DIowLLV4asMqVowB4mJLQub2qKFA-UFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عامل پرتاب دیشب کوکتل‌مولوتوف در پونک تهران با شلیک پلیس دستگیر شد
🔹
پلیس تهران از شناسایی و دستگیری عامل پرتاب ۳ کوکتل‌مولوتوف به‌سمت جمعیت حاضر در میدان پونک در شب گذشته خبر داد.
🔹
دیشب حوالی ساعت ۲۱:۳۰ فردی از بالای ساختمانی در محدودهٔ بلوار میرزابابایی…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/462241" target="_blank">📅 17:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462240">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-MmUgBQoBRcHTiDE2iVzpsYIQrkcGMsAJFJUo-TaMWJhba0IT4T3VAWM6des9_hCcfZbrNwAHxN5PaUulex_WKXBn0ArVbbOtKI6HbAnmdArLTtToestSAgfyRPOnSAobhwzg2AZ6a8Y6swy7uzuEWq3ZZItpB1Yi-8hNO732m2Xiuol91cNuku994L386vTTcjNELgrntuOCOOb05TaQ7KmSAVl6GvTOC_fk97aSNkNMR7csJoFO-2Ox1AdBfEJq-M7-rtDWivmwrDCczv2pTMeWIIKsCItVwRNaEFcXotEGvrxITREoOl94BHZbMZ0etGQPjiYTadWakJpcsifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکایی‌ها بلیت بی‌بازگشت می‌خرند
🔹
داده‌های تازه دربارهٔ شهروندی آمریکا و شمار کسانی که این کشور را ترک می‌کنند، تردیدهای جدی دربارهٔ چهرهٔ دیگر «رؤیای آمریکایی شدن» ایجاد کرده است.
🔹
آمار مهاجرت نشان می‌دهد معادله در حال وارونه شدن است؛ نه تنها شمار خروجی‌ها از خاک آمریکا افزایش یافته، بلکه هزاران نفر نیز شهروندی خود را به‌طور کامل کنار گذاشته‌اند.
🔹
بر پایهٔ جدیدترین داده‌های دفتر فدرال که مجلهٔ نیوزویک منتشر کرده، شمار آمریکایی‌هایی که شهروندی خود را ترک کرده‌اند، همراه با دارندگان کارت سبز که اقامت دائم خود را پایان داده‌اند، به بالاترین سطح از سال ۲۰۲۰ رسیده است.
🔹
بررسی‌های مراکز پژوهشی نشان می‌دهد فشارهای مالیاتی، فرصت‌های شغلی، شرایط بازنشستگی، کیفیت زندگی و حقوق باروری از جمله عواملی هستند که باعث مهاجرت شده‌اند.
🔹
همچنین تحولات سیاسی آمریکا از دوران نخست ریاست‌جمهوری ترامپ، به یکی از عوامل مهاجرت آمریکایی‌ها تبدیل شده است.
🔹
نظرسنجی شرکت «اکسپتسی» نشان می‌دهد ۸۹ درصد افرادی که قصد مهاجرت به مکزیک دارند، دلایل سیاسی را عامل رفتن خود عنوان کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/462240" target="_blank">📅 17:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462239">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f9b252d2.mp4?token=s-HLwb6aUXN-5hc5JcII04Kz5kpX0tVZtiv-MkmjkO6YNOXq-dD_1PDoM78uyVwb7DthQfadeBV_CXn8Sunj9A8iXbebO2RwAkxmEmR8aMSjpawZ7uSHzRqRdEWnbLjFvq5hITmVBPSLcwE9VVcLEsgX_IBtF8FaVse9Pn-j5qpLm2BW35K-9CDvFAgTvX4F78dxXVonzcUoMVOxrxQ6Pb4OCTGNBdLBl5mTXFMugorum4NHZa6s0i0Xsr526s89RRgtreRwRJY7FaKmmAtVkfaZljqMN7eq6PONSxDNFd6fqpXzTqsOjwgyFmmrTAvmTKW_1GazIFIhKsOfTAf5nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f9b252d2.mp4?token=s-HLwb6aUXN-5hc5JcII04Kz5kpX0tVZtiv-MkmjkO6YNOXq-dD_1PDoM78uyVwb7DthQfadeBV_CXn8Sunj9A8iXbebO2RwAkxmEmR8aMSjpawZ7uSHzRqRdEWnbLjFvq5hITmVBPSLcwE9VVcLEsgX_IBtF8FaVse9Pn-j5qpLm2BW35K-9CDvFAgTvX4F78dxXVonzcUoMVOxrxQ6Pb4OCTGNBdLBl5mTXFMugorum4NHZa6s0i0Xsr526s89RRgtreRwRJY7FaKmmAtVkfaZljqMN7eq6PONSxDNFd6fqpXzTqsOjwgyFmmrTAvmTKW_1GazIFIhKsOfTAf5nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش اختصاصی شبکه ۳ از نفتکش هدف قرارگرفته‌شده در نزدیکی سواحل عمان
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/462239" target="_blank">📅 17:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462238">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تلفات مزدوران سعودی در حملات یمن به صحرای الجوف
🔹
رسانه‌های یمنی به نقل از یک منبع نظامی یمن: محل تجمع مزدوران سعودی در صحرای الجوف در شمال یمن مورد هدف قرار گرفته است.
🔹
این منبع با اشاره به اینکه در حمله مذکور، تجهیزات نظامی سعودی‌ها منهدم شد، خبر داد در…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/462238" target="_blank">📅 16:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462236">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f896bb57d2.mp4?token=cc7MCJ2dF0lqaz8HJjYuMR9VGUSNddMBQDgxa5My9bBtZzBAbOMsK4TdhJY4JI9MZC25IhZPq-DNCHrujPnnlFb5n1LdNR4L-KbqI2WCmQbTMk4AyOxQOuGXC2v_LrjwJDagMK2ViaoDgUaO4t855Pi4MjPF2w1ge2jcQiB7oomijpoUDnih4VdYOaeMqOeoRFZCNfwN8_Vr4fm9g2lCltSA3DARgMb7BA5Tik6VWZNm15pz8zFe-EsHPW9ORvQ_IqOvSjQMIcKfebAyu6kVYbPew7MZGuQ3hNjm2j7CS3wrLge7KBV2B5rnlmMMaczdvwnIVzxhWGkINclyWGUaIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f896bb57d2.mp4?token=cc7MCJ2dF0lqaz8HJjYuMR9VGUSNddMBQDgxa5My9bBtZzBAbOMsK4TdhJY4JI9MZC25IhZPq-DNCHrujPnnlFb5n1LdNR4L-KbqI2WCmQbTMk4AyOxQOuGXC2v_LrjwJDagMK2ViaoDgUaO4t855Pi4MjPF2w1ge2jcQiB7oomijpoUDnih4VdYOaeMqOeoRFZCNfwN8_Vr4fm9g2lCltSA3DARgMb7BA5Tik6VWZNm15pz8zFe-EsHPW9ORvQ_IqOvSjQMIcKfebAyu6kVYbPew7MZGuQ3hNjm2j7CS3wrLge7KBV2B5rnlmMMaczdvwnIVzxhWGkINclyWGUaIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: تمهیدات لازم برای تامین سوخت مایع نیروگاه‌ها در فصل سرد سال اندیشیده شده است.
🔹
تا ابتدای آبان‌ حدود ۳.۵ میلیارد لیتر ظرفیت ذخیره‌سازی گازوئیل برای تأمین سوخت مورد نیاز پیش‌بینی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/462236" target="_blank">📅 16:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462235">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf1ecf6fe.mp4?token=styJnxlpoIHl0mmphmNCyCwtd4AuwNGkneCvu2AvrIpMMptA-ATiwjwK5qdnjheTO6lNeuwUJWE5E3JL9jwQIPCPJ4M1NyKfzP8-WGK9X73IaHXZNv4ubHUW6XeJY9c-KSBH75OBQh-NSN8ungrK509-L7WZ0W3asaKV4Z1dpm65GMUD5SNjbo5SASj6d62XJzymaUpKAFqFOuV4I1Btxho95p68FssBb42ARAV9ngRmPSQd4H5D8AsVu0G6Z17OSr17fabjnBzLnUdvMDeKvOJjY21DeywdEsxxmtlOt8cLEKOj2am3d7KnFEetxO220ss5q9T1Y1qr5UAsIX13fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf1ecf6fe.mp4?token=styJnxlpoIHl0mmphmNCyCwtd4AuwNGkneCvu2AvrIpMMptA-ATiwjwK5qdnjheTO6lNeuwUJWE5E3JL9jwQIPCPJ4M1NyKfzP8-WGK9X73IaHXZNv4ubHUW6XeJY9c-KSBH75OBQh-NSN8ungrK509-L7WZ0W3asaKV4Z1dpm65GMUD5SNjbo5SASj6d62XJzymaUpKAFqFOuV4I1Btxho95p68FssBb42ARAV9ngRmPSQd4H5D8AsVu0G6Z17OSr17fabjnBzLnUdvMDeKvOJjY21DeywdEsxxmtlOt8cLEKOj2am3d7KnFEetxO220ss5q9T1Y1qr5UAsIX13fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضدایرانی‌ترین ایرانی‌ها!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/462235" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462234">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgdzZl3j2irZYW8wZbk_hOJX2bCjno6KnuapMirK8ng6D65sEAj3PS99t9bsoSiCtNFKB3wF5dxkNRdM4OpNO1Y9T8DgfYFflcSzKE6WV8i5EiEfGikutnQANswCyGeTUYoFn2tRNxn-p-Zw9is7i4hNhuctTlNUU4faEVRw3jFyYE7ezDxVJTBSV532Izyg7tFeTasxFpSZ2BD3sVBHhQZh9RzmIonIRK8a4ITEHqAvJO_K0ExbOkvurYJMmxAWPp44kqvoSAqqwDBvW29h_FhCyPK9_UicwaErYFEM5BHMhGQlzV3Shf6pz4kRbh8fVCgnnrrFop6Vr830hy0P2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حزام الاسد عضو ارشد انصارالله خطاب به کشورهای عربی: گاو شیردۀ ترامپ را هرطور که دوست دارید بدوشید.
🔹
از عربستان حمایت کنید اما در سکوت! حمایت خود را پنهانی انجام دهید تا مردم محاصره‌شده و مظلوم ما بیش‌ازاین رنج نبرند.
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/462234" target="_blank">📅 16:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462233">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec91e0dc7.mp4?token=s62OISI0EtLba3ZelYNrKeMDtyXGOoFbg9y6xEAqNE98CjptyFGXRGGFmfisb6LxB505pco6Bizwh6IaCcdOFRnnxH-BXFicc6Q6E7x67I3TLkG1MJGZ4ve5wrROlZd3tMRKmFVFNOPOx3w3Oerwbf8RDkQAO1xyZh0WUZzD4QvAXvd6h1w82FO31KdMiXIgR36uId6Hi7EaBlEBF3x63BBWctISE2N76uRvLMccUypimMQCLF64kC_uFaqt8bKAtJHR74CI2V0BwCRMTyAN7iHFx0mKJqk1SyhPHtx_rIKuyZWzTTVUuG_uTtNoZCq7hTT1wdl3YlEtLuCshAwJ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec91e0dc7.mp4?token=s62OISI0EtLba3ZelYNrKeMDtyXGOoFbg9y6xEAqNE98CjptyFGXRGGFmfisb6LxB505pco6Bizwh6IaCcdOFRnnxH-BXFicc6Q6E7x67I3TLkG1MJGZ4ve5wrROlZd3tMRKmFVFNOPOx3w3Oerwbf8RDkQAO1xyZh0WUZzD4QvAXvd6h1w82FO31KdMiXIgR36uId6Hi7EaBlEBF3x63BBWctISE2N76uRvLMccUypimMQCLF64kC_uFaqt8bKAtJHR74CI2V0BwCRMTyAN7iHFx0mKJqk1SyhPHtx_rIKuyZWzTTVUuG_uTtNoZCq7hTT1wdl3YlEtLuCshAwJ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نامۀ سردار سید مجید موسوی، فرمانده هوافضای سپاه در پاسخ به نوجوانی که با پویش حفظ جزء ۳۰ محفل ستاره‌ها شروع به حفظ قرآن کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/462233" target="_blank">📅 16:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462232">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">استقلال لرزه بر تن رقبای آسیایی انداخت
⚽️
استقلال ایران ۳ - ۰  السد قطر @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/462232" target="_blank">📅 16:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462231">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HriC1mZ2rDJdqCieFcy2cAq7EUCfzNnrJpkGZxL705-nKNDtsyC0zmppOCMVDpVrixahoaGnf9eWmriLvXWAD0Hi2NhwV3nfq_SwKTtgfg5yQRWRhqwPXGUPC3qdEEM1s-O6_5SdZayLcJdnCQD1cZNNpMH40_-JU2NdGzy0bN_e5OWnicYoi4VMgcxCRIhWaGm1DP_N9o0r0g28vNDuttEy98HrEXzlWqxcuRclbXz0UWDAH5BHgPdGBt4gXgZfEC-ZgL-tlAR3zRkfjxLAgaQgTi5p08G472fcCCYi8MP0HCIhilOvHyTYt2LedVR1bgkYwCFWapiUSrhCX--fcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی دولت: امیدوایم از نیمۀ مهرماه رقم کالابرگ را لااقل برای گروه‌های آسیب‌پذیر افزایش دهیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/462231" target="_blank">📅 16:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462230">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">امروز در بهمئیِ کهگیلویه‌وبویراحمد صدای انفجار شنیده می‌شود
🔹
سپاه بهمئی: از ساعت ۱۷ تا ۲۰ امروز انهدام مهمات عمل‌نکرده در شهرستان انجام می‌شود و احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/462230" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462229">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFXxCg_yq91Vgzcp5A4suErn6spQusD89HlxzPv1al3gBMczTCODsx48kk35u4tIvXMjON-qAKAj_PJLfBH_y5FR9k1wpwqVTiXNb24fdiGinMhtiPigAwQGRSOQhbNYUFELkkCibzf-Idq_BqBJX_CFyXIIq2nZi30VpWLdH7H19OttlV9H0Eh5HmBGaHvJAoktGBq9VoPVgxCP4bdTJR_BfJG6oA6JkZE16tnjEPR6Fazgh-WaFlNwG34eT8mf-Fy7QyAif2TjfC0ZyBe7PayGWMhoTgAnrrkc__70DWSk2tGMZqG-UyxMbEChpBHv0C6Bf4UPzkzA99g8_E6wMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بافل طالبانی، رئیس اتحادیهٔ میهنی کردستان عراق با عراقچی دیدار و گفت‌وگو کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/462229" target="_blank">📅 15:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462228">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9161e60a.mp4?token=rnAvimsDkaH0HnszQ9HBExXDdnWuEolidCLjToiY3BelhJIpzii5-2qYkU-HheBVQ1wZxqwY7j4j5M3Vn3yJgDsUaBLx-IACttjy1L9rsyUn71qWsvrR-KqflAexU0VTx6yiDn-p8XXMeA_sTuAjgMUiIfUQzTE_VI_j51nAuh9vcDAc7d3vaFtqi3J4-HDQOEDkoU2XDxoPQlXu9C4DEH8_-YinuuPOIJn278uS_N9MC5378y6sUbQPxU2KQ2CXvx92fZ80VLU2wEvKLH_eghHMjBCc5RwB-lm2jAaLl7GhYp6LAUfhAxyFMf8UVWXlRbVZxrdCGJMEUhhcUaY5DFlqJUjflpnvBmqcfEeuTdw4qXeyDkN2dT7DR9nI8cbvricc6I4w7mtBWcmdVHJH3v6EVYHzglqY3vwDjt0wD3iHCc1oJoDRcyhPqdHoQ4NT5PRolPuwBUkBV3cq_XohLLiPGiZ48TpQekJHAmm6TktmbpDoV05fn9upjUPdOO0eZq_-9IESxV95nWv6HbF5kqZxwrn4-oovF9I3jtpBOx5_r5VhcyhMShbUls1RjYoPBcM-8iTv0kEjZWQYOmbsoH72Pe20RIjOmpgJ0MB7RriL6DjwhLf5gwDnwuNLwaHVlP1wLCAC8OrDGpVs7Pt4VlCAAo3FKdz9cN70u8XPxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9161e60a.mp4?token=rnAvimsDkaH0HnszQ9HBExXDdnWuEolidCLjToiY3BelhJIpzii5-2qYkU-HheBVQ1wZxqwY7j4j5M3Vn3yJgDsUaBLx-IACttjy1L9rsyUn71qWsvrR-KqflAexU0VTx6yiDn-p8XXMeA_sTuAjgMUiIfUQzTE_VI_j51nAuh9vcDAc7d3vaFtqi3J4-HDQOEDkoU2XDxoPQlXu9C4DEH8_-YinuuPOIJn278uS_N9MC5378y6sUbQPxU2KQ2CXvx92fZ80VLU2wEvKLH_eghHMjBCc5RwB-lm2jAaLl7GhYp6LAUfhAxyFMf8UVWXlRbVZxrdCGJMEUhhcUaY5DFlqJUjflpnvBmqcfEeuTdw4qXeyDkN2dT7DR9nI8cbvricc6I4w7mtBWcmdVHJH3v6EVYHzglqY3vwDjt0wD3iHCc1oJoDRcyhPqdHoQ4NT5PRolPuwBUkBV3cq_XohLLiPGiZ48TpQekJHAmm6TktmbpDoV05fn9upjUPdOO0eZq_-9IESxV95nWv6HbF5kqZxwrn4-oovF9I3jtpBOx5_r5VhcyhMShbUls1RjYoPBcM-8iTv0kEjZWQYOmbsoH72Pe20RIjOmpgJ0MB7RriL6DjwhLf5gwDnwuNLwaHVlP1wLCAC8OrDGpVs7Pt4VlCAAo3FKdz9cN70u8XPxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتفاقی که مرزهای فیزیک را جا‌به‌جا کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/462228" target="_blank">📅 15:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462227">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlKmowr9P0-z9mwP2KFCykTnUC4h6BckLDc08lRM1vpO7lmEn5hwRLxzSJ-_uwB8rrGGVcdibRZ2wgqMVnOCwktNenWfz4L38EbOxOCPetZMyAfFJrEFYZ6vgN1qPLj4rk5CNNqyBvYr5kI9DQEuiu00Bs_LUpMvxx6dSMAIu3RPvQkBRBQlFT2U_lOTSwXbCBrWzSxrlsLaWJUV7TFLai6OQABmVzjrPXxA3X-Hw6ghpHjy0J7qzE2ny2wYhRZfxLhSgfP0Dw8d23_mNfIRY0AHY7pPliHp4B8eHGsVUwHicTfk8SlRwQ5AtwBs7JUgcRE5ZwP0Tk1yd_FgEhgWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز بحران بزرگ سوخت در جهان
🔹
مدیران غول‌های نفتی آمریکا که در زمان آغاز حمله به ایران به ترامپ دربارهٔ پیامدهای کاهش ذخایر نفت هشدار داده بودند، حالا از آغاز بحران جهانی سوخت خبر می‌دهند.
🔹
قیمت نفت خام آمریکا نیز از ۱۰۴ دلار عبور کرده، قیمت بنزین نسبت به سال گذشته بیش‌از یک دلار در هر گالن افزایش یافته و قیمت گازوئیل نیز در آمریکا رکورد تاریخی زده است.
🔹
ذخایر راهبردی نفت آمریکا پس‌از برداشت ۱۸۰ میلیون بشکه در دورهٔ بایدن و ۱۷۲ میلیون بشکهٔ دیگر پس‌از حمله به ایران و بسته‌شدن تنگهٔ هرمز، به سطح بحرانی نزدیک شده و در آستانهٔ رسیدن به کف عملیاتی ۲۵۰ میلیون بشکه قرار گرفته است.
🔹
مدیرعامل شورون با اشاره به از بین رفتن بخش زیادی از حاشیهٔ اطمینان بازار گفت که دلیل روشنی برای بهبود شرایط نمی‌بیند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/462227" target="_blank">📅 15:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462226">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7-nn0vqiaxn7GtwwVftG65gocCkAfjkZQsz9QQHxonz5YrqcxPb3b7vW7-CT_wtt3VR4CSzaLO8Um3FsgNlVCOojCbCHkErNOvFb1q9gb7mrhFIqxanuF9kHFqB08bJMidf9EnSRAd9ocku5qOLtdpSDUSzEjHek03SYPfbEn2Qm8rrFzWWONHLFDpcZOlLDv_DTyAPOgx2Jx7CQMv2ybkZDgE9rX2RM6V96snImMiCmrffeG59FWBhWan1S0M7tcE_iEBN_d3stP_KfYF6PeTDiiaRB4R1HCRGonW0lpmzdA7KidSQMyIgyQZj_1auQ7DPt26TE6LO_FXuB5jSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بالاخره رهگیری اف-۳۵ خود با «آتش ایران» را تأیید کرد
🔹
پنتاگون برای نخستین بار به‌طور رسمی تأیید کرد که یک جنگنده رادارگریز اف-۳۵ این کشور هنگام مأموریت بر فراز ایران، «هدف آتش دشمن» قرار گرفته و آسیب دیده است؛ موضوعی که پیش‌از این تنها به‌عنوان «فرود…</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/462226" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462225">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATr7S8jee_EVSRh06zzTXG_X5Tx3NoIdqWC_T4mIEakhuyfimEKIw-Yf_OB2yOXpis0Vd8kbO1OpiR-c65Jg16J3OADJ2D1QnnYRdYWt-oY28rQuLKXsBlr5nQqEkjN2JSDeRNKIkZJLZ6WAJ-g8qfDHsBAPHIUHbFIPtv_2FzKTX3wTvj295PgXXVZ1WpxlA2VSe_rsgp356AnD1jUk-XNHk6pRlqKgWgQKDd_bkon5YCKreaZtq6hA_uCH0VOoNEbgCWaeITnumx1Q9i-TklZ5mhJkH6byD1Ky2ugXrLeCiJb_H1Qt5m1cutwDIkOZQ6O09M6EEovIbU6DNxfNSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره نفت گران شد و ترامپ یاد توافق با ایران افتاد
🔹
هم‌زمان با نزدیک‌شدن قیمت نفت به ۱۱۰ دلار، ترامپ باز هم در پستی در تروث سوشال از توافق با ایران نوشت.
🔹
تاکنون ۶ بار پس از افزایش قیمت نفت در بازارهای جهانی ترامپ محتوایی با مضمون مذاکره و توافق با ایران…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/462225" target="_blank">📅 15:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462224">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlFvpyKeq0w5k0pevegHqB1-z2mhUyJKN2KVII6DEItIK3mexG4e1TZk8I7XQxudAGrWfaW1NGHeSo42NH1T52TvFL6z0BEmJyqcY33pG5En027-p3fjTK_zHTJ2AEF5IhNqSKcqbdNu3xbkzLk1wQfVKWCFezyR6khMaabCV6Pohu2CJdwc9zPHnXXUBbDGi2gpYRnogBNUnJZcUXdQvDk7MMJgQJdHExw2giOmU_51CbbxaZAHZbbuz3psqsBy8uiUgsO0BMZtzI8eJ20KK_lqLliQevR5bHjvVIbHPPjympvQGz4C8lk4nBaUr619uswuimggiSCT5tLiDWR_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ویدیوی کامل گفت‌وگو با افسر شکارچی جنگنده اف-۳۵  @Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/462224" target="_blank">📅 15:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462223">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvXTlG0zd0eE1eakfqsApVCPiXox17EXQMgW2t_mpNr93ZV5_DWmgdU1rWgUDAIj-Kf9G9Z7qKNpHCD5DcbwqubiSmSVVNRNIkGiQ1cJ0q6Ti2exULNSdT7TAbAdysz9iRLdzOMabfFd0Do_YIznwwAwVkhQ2Q8ivQgJx-zPeg3FxgrIgAxHmLDwAXN1aMWCcEvMPq20sNnoeB-f18-cbcdmQp06WbXYmSVk2xCTgspqWbiico-gU9qdGIF26hMJRearS95YARCRAuwrPq7JfGd31LLkpuZ41Oqzya9bnbmfk6TDMwirmZE2F3XKmAGIilMHaQw2PYdYAeM6EXZFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تأسیسات نفتی جیزان هدف قرار گرفت
🔹
همزمان با عملیات موشکی و پهپادی گستردۀ ارتش یمن علیه مواضع رژیم سعودی، تأسیسات نفتی جیزان هم مورد اصابت قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/462223" target="_blank">📅 15:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462220">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxL0CEYffmGZ3sEYT2UzQqATA_bf1alpWQXRYQpcDFxX6FIYE8E5bc26nOLqTMGpOvBTqkN2U5LkL4DQKhOp7EVA4brx8dum71X-E8kDEuuIijMehPKC4g9I4a0fVMPRTRdWLKScNIm9qyFs3I51cKHekWwSk7_2Mnk4aEgT7dcg0wKWbndUIzAGllqrY-MZcGCH2kzJ2tHe6yVsiRiVkWgCOuv926hHlnIa_9kl8t9via8zcDxTG99JHUpXnbwXSTfxB1_RPG4prGo6PFkXLQx91wRSSoHyKjKiaI3XdpSe4KufHzInhpFmcDrRejT8HwFKyK31ZewCrn_kjotRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pflW6o345wypM65uGeeJMvIUBD_TLmYcSjPmQKZZA9phDigd71pE0zyo3JbsJTwNmk-UnhEXJyWXUE1kURFmxLjbtQT7TW67RfO3xDqvHEy8uvxVU5ZIFDJtdZrBDVDWguQhqnn7Ib25CatFSMYvlCR2kylQzVWP1NrdFBJO5Z70z3TcMv5fep4JCgTJlxh9-2SvJXchGsx2nFxSqmA_5PTGukkwIydT09lxpuLANM_lOpmX88eGWUAAeGYLMNZc9TpTQdggIuuEZizs23Vk1z1P9xsvf_6F7Cem69VPV-711Mz1astdwvE3TwikVc76M9Odl-2jNo6YpIJNsKXaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_FScmgyeIOlEHJEDQoql2w0pgKmfShKg0LKrCIh97epryg3ZT1cURWD_uUonIq2fJwQmhEvn3hrkrDHmvYN6dvbFbmhIVZ1AnjWeLhRYLujJ84Ag55I92gjBMqpFD5C-ZepHc-GJlmiij1Amcp2BgsfV-f3NaA7wEryc9wXG0Iauzgcocwuo1Qegwcmne_7iqTXx0-2LHGCtlGkz8mni1vYw9Y7WNK7qTV-4afYbBH94P5qZ7a-rwdxhyiGvWzWPGRRMVV5wqq9JYLhIFWQ1kCe9Bf-47W-NiCSlEtTYVI1iS_OteawfaU6TNXFZ5F8qjSmu6DyrcfVsL9SlcZ3pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هویت خلبان آمریکایی لو رفت
🔹
پنتاگون هویت خلبان اف‌-۱۵ سرنگون‌شده بر فراز ایران را به دلایل امنیتی مخفی نگه داشت، اما نمایش چهره او در مصاحبه با شبکه سی‌بی‌اس، عملاً شناسایی این نظامی را ممکن کرد؛ اقدامی که کاربران و کارشناسان نظامی آن را یک تناقض و بی‌احتیاطی امنیتی دانسته‌اند.
🔹
پس از انتشار این مصاحبه، یک کاربر در شبکه اجتماعی ایکس اعلام کرد که با بررسی سوابق و تصاویر آرشیوی، هویت واقعی این نظامی را شناسایی کرده است. بر اساس این ادعا، فرد معرفی‌شده با نام مستعار «براوو»، سرهنگ «جاناتان بات» با نام عملیاتی «ویپر» است. این کاربر همچنین تصاویری آرشیوی از وی منتشر کرد و مدعی شد که هویت او را از طریق تطبیق چهره و سوابق موجود شناسایی کرده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/462220" target="_blank">📅 15:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462219">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622356c043.mp4?token=jk2JxE8ECiEQOcZQuJlqu9t-3REu60ci8xdbB41Mpv5bo4vXentftSRIxzA7AGPTvWE1wSUxIa1f5Io5TnGv3hP-tx4uD6knR64JBRUUYRFCqwfTHbJQzC5t487NO0ll1P4mqjyzclBtec66Rk44Aqfx8p9-IBhvtXvrsln0cl3oee7mALzxMMxlW2SAI9FfQHNHV98wLk0sxIuFHNRvcRBYPmJYqgkfsNek9ZcWlyj_lmcnFMwReHrCEmX_nnkbR66zlzJs0ZnIA3iIdXzx4hqpxtQQXfuQHNBXQdWFK5QGS9t4r69by3X2zZwSoUf2m6gWaqNbjuqLAeCj_V0pbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622356c043.mp4?token=jk2JxE8ECiEQOcZQuJlqu9t-3REu60ci8xdbB41Mpv5bo4vXentftSRIxzA7AGPTvWE1wSUxIa1f5Io5TnGv3hP-tx4uD6knR64JBRUUYRFCqwfTHbJQzC5t487NO0ll1P4mqjyzclBtec66Rk44Aqfx8p9-IBhvtXvrsln0cl3oee7mALzxMMxlW2SAI9FfQHNHV98wLk0sxIuFHNRvcRBYPmJYqgkfsNek9ZcWlyj_lmcnFMwReHrCEmX_nnkbR66zlzJs0ZnIA3iIdXzx4hqpxtQQXfuQHNBXQdWFK5QGS9t4r69by3X2zZwSoUf2m6gWaqNbjuqLAeCj_V0pbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: اگر گاز، برق، گازوئیل و بنزین را به قیمت ارزانترین کشور همسایه توزیع کنیم، ۷۲۰ همت در سال درآمد کسب می‌کنیم.
🔹
در این صورت دیگر قاچاقی هم صورت نمی‌گیرد و به هر ایرانی می‌توان ماهانه ۷ میلیون تومان داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/462219" target="_blank">📅 15:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462218">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpawPE0wFBobuAa4ncr6aee5FIAe4h1Z1v6aiT60nmSA7srORXGkcGKNDU2RHBO0Bz2a_61UFfzsot-2d5HM0sl8LEe9CvpQtNugMNt8mj6nZyXci5dzweuiMjwwwemiJ9HHV1ra_y1tTf2aCNzVARC0442BkSKn8G7g8YlPzdj_pTF56ii65xcxUk2y95P2evEw7YubTQYoX6QmK3JBR13l4KgTX35mWEVce5s1k9ZMuT0COUtp2NVbAj_zkCU1I05SVG3MCBfw6GKet35sS4M24wcRrs5X-Eddb1TnurIuG-XUxOcuPr2IJvmtoOveqUxDh2VZVfY7hP2-6UVNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❓
چرا دانشکده خبرگزاری فارس؟
🚀
اینجا فقط درس نمی‌خوانی؛ کار می‌کنی، تجربه می‌کنی و حرفه‌ای می‌شوی!
✅
آینده‌ات را از همین امروز بساز!
📞
ارسال
عدد ۱۴
را به شماره
۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/462218" target="_blank">📅 14:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462217">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ce570b7d.mp4?token=P4xkXvLeSLdIDeli-1QYFKgCI59OOlHcmlFQ8543ilYgxUv7uCzdNGabb7BgccQ07Al28Pkdwq8zp5k6U2RANrhGpt7-iQQStm3PZZp3uLRAAHleGcgXSfL2GSX-RwEUWBvQpfbl7ROlIlaYSrHVTHW6QvVuS4uRUJkVrRkjO37imFTaRgdRPhAOGgFj4plKmSIaUOTZb8aGFgotkZXns3Y9KC31Cy3pvT0O4shduuPlE741IoBDzIeddbl7R8DcO6aDsw_mW1m45kp3NSHHGUqlk4Di5zXZ1_4svNeWKMjQQIZUmQqYzkTbs4bwPMXQL6ULXMvIc1fT5z_1DRFoew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ce570b7d.mp4?token=P4xkXvLeSLdIDeli-1QYFKgCI59OOlHcmlFQ8543ilYgxUv7uCzdNGabb7BgccQ07Al28Pkdwq8zp5k6U2RANrhGpt7-iQQStm3PZZp3uLRAAHleGcgXSfL2GSX-RwEUWBvQpfbl7ROlIlaYSrHVTHW6QvVuS4uRUJkVrRkjO37imFTaRgdRPhAOGgFj4plKmSIaUOTZb8aGFgotkZXns3Y9KC31Cy3pvT0O4shduuPlE741IoBDzIeddbl7R8DcO6aDsw_mW1m45kp3NSHHGUqlk4Di5zXZ1_4svNeWKMjQQIZUmQqYzkTbs4bwPMXQL6ULXMvIc1fT5z_1DRFoew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازار لوازم‌التحریر در آستانهٔ مهر داغ شد
@Farsna</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/462217" target="_blank">📅 14:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462216">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k40R-neinMMrgmLEHYpdOku2qiphkZj0jX4551mqtIS_6jQuodk5m3erlYw9LfusLSIOjdjHaYduaGas4h-JgN-E1E-fhkxYVmGbQhWoJofCpOq4o_NIGqAKrNSc85M37qyVB04SgmW8C1C6GkY9J8dZ3xCDMx2Va6h3LeFJ7P9zgGDc25afdGguRJ2m8ukFRd-NuEww088pgtbRKGrfPcq_nRL_1L8A3Q9VulCDrPUCsuRxaIG6I-5xUHHn6fHM20KH9q5yq6JsHw2tytN0Z-P_uyipvpHtSaW9uHjAc9xCSPuW9fXiTDFn3uRfpsm4-V6Oo78-dFmmzZ8YQFk3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گودرزی: مجلس مدافع افزایش حقوق نیروهای مسلح است
🔹
سخنگوی هیئت‌رئیسۀ مجلس: رئیس‌جمهور و معاون برنامه‌وبودجه درخصوص افزایش حقوق نیروهای مسلح و کمک به معیشت این قشر فداکار و جان‌فدا تصمیم بگیرند.
🔹
هر کجا موافقت و حمایت مجلس نیاز است لایحه بدهند مجلس با اعتقاد و تمام‌قد حمایت و پشتیبانی می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/462216" target="_blank">📅 14:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462215">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635fcb4f29.mp4?token=OMZ1qZXP5lVstLakalMpOK9iWzK3Mzr4mUflnzZwBbkJNREWI67H5XPV9SOb9GYZ2qvI6oDdyDbsJ-cijm1vQVJyITVX99gSw2fazSX439g0qI1POu2FkFl3BVYur7jVJeGZCk-y6GXNNubsoMLsxZHVKkAi4Z9TaFcqv7f_-q_ngOTZ1Rz2c2buYvfAtZWxhV7ngpfg4L3ahURUZAY9ELuRcY21YyccYlfYGA_uqGZiyXTJzscSP3BDWdwQENcauYmpmXy3RTqHYYKjzXCAi0oYUMpgIeY24C-ZrgyHD7BPsFlqVqjm8AHwlLwMtYC3AfKp4l_mBAdUk1tYcbRYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635fcb4f29.mp4?token=OMZ1qZXP5lVstLakalMpOK9iWzK3Mzr4mUflnzZwBbkJNREWI67H5XPV9SOb9GYZ2qvI6oDdyDbsJ-cijm1vQVJyITVX99gSw2fazSX439g0qI1POu2FkFl3BVYur7jVJeGZCk-y6GXNNubsoMLsxZHVKkAi4Z9TaFcqv7f_-q_ngOTZ1Rz2c2buYvfAtZWxhV7ngpfg4L3ahURUZAY9ELuRcY21YyccYlfYGA_uqGZiyXTJzscSP3BDWdwQENcauYmpmXy3RTqHYYKjzXCAi0oYUMpgIeY24C-ZrgyHD7BPsFlqVqjm8AHwlLwMtYC3AfKp4l_mBAdUk1tYcbRYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عکس جولانی زیر پای مردم سوریه رفت
🔹
در روزهای اخیر چند منطقه در سوریه در اعتراض به عملکرد اقتصادی دولت جولانی شاهد گسترده‌ترین اعتراضات مردمی طی نزدیک به ۲ ساله گذشته است.
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/462215" target="_blank">📅 14:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462214">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKAk79nbqhPbctrzL2avdOx0tmx0JIIvEx_1UQHc50zqkUKr4L0DXJvnysNMesWZtdjv8E0e5Rkv_wGRz-83mkaYiPABtjWh3tbUMP4uvgQAivCG9EkqHQ4JImvox8Eveg-rvmHOQfYLmd-TwGkXri4U5R5xT7srv7EBOxxNU3DvMhqGaI90L0IhPddjH7wkrUqoMs9QAqSpTGtRy_SZVqGkVmzq4WOf7_sCdZ2HVpzEYQ4aOnfFBmywq04VFfzEa740T2XgnFnFoAsRKXOkvGJqcvnCLRxeSVYY7SgD3If5VDfwuYm4IFKX_J_EsXcc56ySzKzJOCjYv7sg_Aj8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اژه‌ای: بیش از ۳۰۰ شرکت وابسته به دولت بودجه‌هایی دریافت می‌کنند که مجموع آن بیش از بودجهٔ دولت است.
🔹
برخی از این شرکت‌ها زیان‌ده بوده‌اند اما پاداش می‌گرفتند. حتی یک نفر در چند شرکت عضو هیئت‌مدیره بوده است.
🔹
سازمان بازرسی گزارش کرده که ۱۵۳۵ نفر به صورت…</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/462214" target="_blank">📅 14:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462213">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGHb6ZLeVpLU_WFNKvdbf6B7qEQAOrJIFIosJlZsHQ4MW-VLZzxcVPSmdzF3GlsFFmKWubJfyHsq4xs--9wU1F8RgQWwc5UT8jL6uSAZnalxwDAHBsDKar_UeNpKJ-gig47cGkvVoJbGue993oApoDJ70SnJn0qYoAqTD61P_cFY2zCrue-I99jhebsGLJernq-FPZbNnlrtYX-gJNIZLUPU3zUDXDgzH4Se8ubl9iHJOFLJGBlyi_VcI6iCcATZh5zXHHJ3VdZPSn69RiUHihE5DAdEIFBNJBTm6dtxZDAb41F5MOrxhH-ROvfFZrqjQyfq1u1nIva58IKyhgJUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالیوود هم به کمک آمریکا آمد
🔹
ادعاهای مطرح‌شده از سوی خلبان آمریکایی بانام عملیاتی «Dude 44 Bravo» در برنامۀ «۶۰ دقیقه» شبکۀ CBS با واکنش و توجه گسترده تحلیل‌گران، کارشناسان و کاربران فضای مجازی همراه شده است.
🔹
بسیاری از ناظران معتقدند انتشار این مستند…</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/462213" target="_blank">📅 14:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462212">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انتقال ۴۹ زندانی ایرانی از عراق به ایران
🔹
وزارت دادگستری: ۴۹ ایرانی محبوس در زندان‌های عراق امروز از طریق مرز مهران به کشور منتقل می‌شوند.
🔹
بیشتر این افراد به‌دلیل حمل موادمخدر، قرص‌ها و اقلام ممنوعه یا جابه‌جایی بسته‌های امانی متعلق به دیگران در عراق بازداشت و به حبس‌های طولانی‌مدت محکوم شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/462212" target="_blank">📅 14:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462211">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ece9592e4.mp4?token=h39Mvda6xnPbxW6p5v4_X8n-07p1M4fSvLKLmWWcoDeQeB7n2yrpNFE-E5dZKTjtPZJVaXVn8mEG-FnrIoTKFrH8WWj9goomYrIraWJpyNu3w38O0iSTnLvk-CoGjL5d9Wjb6T0IHs6NBTOQwGGB3Y4ujLFqD2-8IpcnXt8f41sWqsc5sf5bFt6cnBdz5sG3L9xAn66J73-B9ryVEgjAsURpLS_x6r-enQZT9-sAUyKaKgd-F9F7Xkw46bf2OcaeIHVuox-xnzQm4aEcx2kvjl-TbL_GGvnhV7SeQ2pfo3VTmwZfywd99dSngPk1encRWpiqPTmu86TsIiDOioS0Roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ece9592e4.mp4?token=h39Mvda6xnPbxW6p5v4_X8n-07p1M4fSvLKLmWWcoDeQeB7n2yrpNFE-E5dZKTjtPZJVaXVn8mEG-FnrIoTKFrH8WWj9goomYrIraWJpyNu3w38O0iSTnLvk-CoGjL5d9Wjb6T0IHs6NBTOQwGGB3Y4ujLFqD2-8IpcnXt8f41sWqsc5sf5bFt6cnBdz5sG3L9xAn66J73-B9ryVEgjAsURpLS_x6r-enQZT9-sAUyKaKgd-F9F7Xkw46bf2OcaeIHVuox-xnzQm4aEcx2kvjl-TbL_GGvnhV7SeQ2pfo3VTmwZfywd99dSngPk1encRWpiqPTmu86TsIiDOioS0Roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتاق جنگی که بیش‌از هر زمان دیگری در آستانهٔ فروپاشی قرار گرفته است
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/462211" target="_blank">📅 14:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462210">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2l3La6-1bBOiGhuWyRME7rQj4bdoZax2iVhNW4dfDFRRu-guGiX_YZDnGK0_dID62laBAZk6iuetWXx1mRUdFpaEKy5V3ans_T6InzF_xLLyD_e3spl4f0Wk7fNmx3irhXXMLOLBGfQY7Iyi4HW5NJQ5ObSt-i8g5D8o47KA7-taeFtB-5KGuuxcDbFQjVK5tSvFl071DDijRF4ChP3dA5pAiJsFGID1Je6xKNHw6J_accEzqSoKgLkkU0x7tOzeSVH37kYnU82LnLAua0D_WOPqVQGLT_2nX7aB-ayIi1QUH6yeGfTRs8Rvoif8HWXIuabs9xGwJ3NJ9aa6DDNsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن داروسازان: بدهی ۷۷ همتی بیمه‌ ریشهٔ کمبودهای دارویی است
🔹
رئیس انجمن داروسازان ایران: کمبودهای دارویی کشور ناشی‌از مشکلات اقتصادی و اختلال در گردش نقدینگی است، نه شرایط جنگی.
🔹
بدهی بیمه‌ها به داروخانه‌ها در یک سال گذشته به‌شدت افزایش یافته؛ بدهی تأمین…</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/462210" target="_blank">📅 14:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462209">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d9290255.mp4?token=fT6X9k0FKM_qVzwPB9uGzw5ZfEmTLWirIIIxOFaxDlvsgQbkYBJWNZ1Ad6nE-stW1OCzbFdy1r6dRKNRvLopLweiwmFwtSlRCFwwy_JDzzYTf8MpJ7aL4WYcg90SHVrwxDDz3nNZEilmAoaEnueo6SBPHg64Ajl0IgZl20dvUpai5pwejYcGmxAXZB52jBrQyjEYt5glOVTXKACETlOLNgJRZzp_ASun39Y-YReQsBH_wAuKFhqJYKh2eMPTWk5M8Nai4h8UdLnIh7mxeTWJAZ4t23BFGZnY3bADtS1Bzs_m8qve2m00CJ9ZWFvpmJ5BBofsIhiY81usDB0ad4WXBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d9290255.mp4?token=fT6X9k0FKM_qVzwPB9uGzw5ZfEmTLWirIIIxOFaxDlvsgQbkYBJWNZ1Ad6nE-stW1OCzbFdy1r6dRKNRvLopLweiwmFwtSlRCFwwy_JDzzYTf8MpJ7aL4WYcg90SHVrwxDDz3nNZEilmAoaEnueo6SBPHg64Ajl0IgZl20dvUpai5pwejYcGmxAXZB52jBrQyjEYt5glOVTXKACETlOLNgJRZzp_ASun39Y-YReQsBH_wAuKFhqJYKh2eMPTWk5M8Nai4h8UdLnIh7mxeTWJAZ4t23BFGZnY3bADtS1Bzs_m8qve2m00CJ9ZWFvpmJ5BBofsIhiY81usDB0ad4WXBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیم ملی مهارت آمادهٔ مسابقات جهانی شانگهای شد
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/462209" target="_blank">📅 14:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462208">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">عامل پرتاب دیشب کوکتل‌مولوتوف در پونک تهران با شلیک پلیس دستگیر شد
🔹
پلیس تهران از شناسایی و دستگیری عامل پرتاب ۳ کوکتل‌مولوتوف به‌سمت جمعیت حاضر در میدان پونک در شب گذشته خبر داد.
🔹
دیشب حوالی ساعت ۲۱:۳۰ فردی از بالای ساختمانی در محدودهٔ بلوار میرزابابایی تهران ۳ کوکتل‌مولوتوف به‌سمت شهروندان حاضر در میدان پونک پرتاب کرد و بلافاصله از محل گریخت.
🔹
مأموران با شناسایی متهم فهمیدند که قصد دارد به‌صورت غیرقانونی از مرزهای غربی کشور خارج شود. مأموران در ساعات اولیهٔ بامداد با شلیک گلوله از ناحیهٔ پای راست متهم را دستگیر و برای مداوا به بیمارستان منتقل کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/462208" target="_blank">📅 14:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462207">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edaEaDXxSvmpJU_zEhcpGAiiRNLT80FaOP526ysM8WoPPPw5T4MMQkPavIIx5Dl6qX117f5lrwnfo_GmIu9b-wD0LaN-y5u--d3ylcPBsgUaQM_wayRryZg78ErQ96o3DH3ZE0dkN828Z5fPXpZZykqQn0MjpwMbnwTjfnIM1QlDD-WJlCWJEt7Rway7TkdWIYnELrJa7e1_-kQhh6iLK4QPryDgLWdSfGrMVLdgU_NpFLpMCGyYTQZHNvuGRzKpn2J6sYVuRZO8AHy-37yRAW1KwIAJ-MuUqGhu0w_tt6ndZRDQeAHXzSZ0kEHGJQJastQK9cBxwkSFIX7TG5QnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور جدید وزیر اقتصاد برای شرکت‌های دولتی زیان‌ده
🔹
وزیر اقتصاد: زیانده‌بودن شرکت‌های دولتی، با وجود تنگناها و محدودیت‌های موجود، موضوعی است که باید با جدیت مورد بررسی قرار گرفته و برای اصلاح آن اقدام شود.
🔹
گزارش ارائه‌شده دربارهٔ تحلیل عملکرد و حسابرسی این شرکت‌ها و ارائهٔ آن همراه با پیشنهادهای اصلاحی به رئیس‌جمهور تقویت و جمع‌بندی شود تا موضوع با استفاده از ظرفیت‌های قانونی، با جدیت بیشتری پیگیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/462207" target="_blank">📅 13:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462206">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TImtGain7UnpMUdZGcNB3_ThvtGUdIOruPsj9T29HsFE3S4Mfc9DECqzgyZNbuNVln0cblRBcl4TV4KfdxfIzaoCQDSnpUc8PcgOnkDsvWo9wQM3CueB3fglyVUbwpXb0p5tJuCoFHa8NIAxq1wD2WCltAvi0HWU5_NImciqcB7y9OIJERZcsnXgpSUPIGYYnrKut20TlbCFqCMgp3fk1bk8ehkd2FKgYAEeGzXwsl-ChAwUggU7G8NOmi0e_b8LWbORaakOuo7URJLcdSbc_wjg-oKZETGMbZyTsLEgvss0YTQ5ST5wis8kXQh_kfinoRQIc4iDeXzC6Xli-0YZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان غذا و دارو: ارز ترجیحی دارو را ۹۰۰ میلیون دلار کاهش داده‌ایم و همین باعث افزایش قیمت شده است
🔹
پیرصالحی: پارسال حدود ۳.۵ میلیارد دلار ارز ترجیحی برای حوزهٔ دارو و تجهیزات اختصاص می‌یافت که امسال این رقم در بودجه به ۳ میلیارد دلار کاهش یافته؛ حدود ۴۰۰ میلیون دلار دیگر هم از ابتدای سال با پیشنهاد سازمان غذا و دارو از ارز ترجیحی خارج شده است.
🔹
پارسال حدود ۱.۵ میلیارد دلار ارز غیرترجیحی با نرخ حدود ۶۰ تا ۷۰ هزار تومان دریافت می‌کردیم، اما این نرخ به حدود ۱۷۰ هزار تومان رسیده است.
🔹
در مجموع، نسبت به پارسال حدود ۹۰۰ میلیون دلار ارز ترجیحی کمتری در حوزهٔ دارو و تجهیزات پزشکی استفاده می‌کنیم و اختلاف نرخ این ارز با نرخ فعلی، طبیعتاً روی قیمت دارو اثر می‌گذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/462206" target="_blank">📅 13:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462205">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHRPsaEwJ50It58Fzgr-niGX1fOhXt58RssbANKRtIZ6enIm-zll59dWV6VMUl2_nAtRa5O5485zCYQX-_NhK2eahLxXXGhJI88PNNO_eYXR2-PFM3gbNlDCy4cI6dloYbSi-fpvvoELdTd1U-yQLcDcifxeD2yEdWoTv0EOAfm7nchqi2_LfLhvHgyO96EcRcBSoQGURTf_F3eK3S_5_4SpSiQd1vQlotpAIYeSMXPeuM3-lokf4IpwmARKbfX4EDR4VUT_DxjBMt__8O0ek4tze2ERZtxrSuZc1g2waWlNsuoA7GuqDCKODSvt_-ld1UG_V5BszEQRc-d7ZkIz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تراکتور از روی پرسپولیس پرواز کرد
⚽️
سایت footballdatabase: در جدیدترین رده‌بندی بهترین باشگاه‌های فوتبال، تراکتور با صعود ۳۰ پله‌ای در جهان از پرسپولیس عبور کرد و بهترین تیم ایران شناخته شد.
⚽️
تراکتور در ردۀ ۲۲۱ جهان ایستاد و به ردۀ هفتم آسیا صعود کرد. پرسپولیس هم با سقوط ۵۳ پله‌ای در جهان و ۵ پله‌ای در آسیا در ردۀ ۲۲۵ و دهم قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/462205" target="_blank">📅 13:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462204">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f032eb3f6.mp4?token=VWaL6jSVn3jXa_HLJ0TpykqPXlRG5BxPf9hF9wuojnV6zrMP_uT7lOl_3d9_fNA726DumhP0qGVhZVJz9V7KgeFniPTUmEFLXiOWLyATI3dOOP5JvxvtBL-i47_1FuGL3HDYr_yiEeDDWoxNh8JfkmS_vnIO8b8fJf-WJHs0fkr--1EXs57b4MFhKxqvl_uAjHjiwLAiyRS7sgXGY5y79nkLzgXNd0oRdL3gtNZWll_oZU3kGdmG2DwOQYsyYbfz530jPXDLMjWDsd_y6cw3cmYPpz-IYpzwpFigaOUFN-y924A4Y1j7G203IDGtWILFBeI5S1fMENY5qZwLDoYvng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f032eb3f6.mp4?token=VWaL6jSVn3jXa_HLJ0TpykqPXlRG5BxPf9hF9wuojnV6zrMP_uT7lOl_3d9_fNA726DumhP0qGVhZVJz9V7KgeFniPTUmEFLXiOWLyATI3dOOP5JvxvtBL-i47_1FuGL3HDYr_yiEeDDWoxNh8JfkmS_vnIO8b8fJf-WJHs0fkr--1EXs57b4MFhKxqvl_uAjHjiwLAiyRS7sgXGY5y79nkLzgXNd0oRdL3gtNZWll_oZU3kGdmG2DwOQYsyYbfz530jPXDLMjWDsd_y6cw3cmYPpz-IYpzwpFigaOUFN-y924A4Y1j7G203IDGtWILFBeI5S1fMENY5qZwLDoYvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیح دبیر دربارۀ معدن‌داری کشتی: مجوز داریم
🔹
رئیس فدراسیون کشتی: ما مجوز کار اقتصادی داریم و شاید این خبری که بیرون رفته جاسوس بوده که منتشر کرده است.
🔹
خیلی جاها هستند که کارهای اقتصادی می‌کنند؛ حالا اساسنامه ما به ما این اجازه را می‌دهد. اساسنامه‌ای که مصوبه اتحادیه جهانی کشتی کمیته بین‌المللی المپیک وزارت ورزش و کمیته ملی المپیک خودمان را هم دارد.
🔹
ما در شورا آنقدر کتک خورده‌ایم که حالا کمی کار سیاسی را یاد گرفته‌ایم؛ از کسی که خبر را بیرون داده شکایت کرده‌ایم اما می‌خواهم که مردم در بازی این‌ها نیفتند.
🔹
ممکن است این خبر که یک ورق هم است از وزارت صمت بیرون رفته باشد. ۳ سال دویده‌ و مو به مو هر چه لازم بوده اجرا کرده‌ایم.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/462204" target="_blank">📅 13:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462203">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ2BWq9olhV2UhhIv2vaPQ4PihO4FBXOLbiB6nLRSaoQS3uWIKfH33MwFtLHcK0n6CoIAs7kdIq0C6O40lxYkPpKpKwVT7x-HxzYkAduhx94bFUpKYUl_SO1r9VIgQzONu2v-V2p9VI_dJoG5ipOzbYFKrI3O5FOiskxwdedsKKQ6nbWXmEw3MBPnKtB9LWlj19L_3O23DDKGvZf7ehftNWsLpSnarfushK7PGRlKo-Yga_BPEC4wbW-mwyW-raBNalS6I6B6ZGD1UB5s9RygJl1yRVxn_v___g3QFCmD53-15SKO9AyRxVqZWmGD46-_GKavIEDoIcpv1YAcfYuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم به ریاض رفت
🔹
وزیر علوم برای شرکت در مجمع جهانی یونسکو دربارهٔ اخلاق هوش مصنوعی، به ریاض عربستان رفت.
🔸
ساعتی پیش برخی رسانه‌ها از فرود یک هواپیمای ایرانی در ریاض خبر داده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/462203" target="_blank">📅 13:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462202">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aykIOAYEVmt-yhT8NxYnXKDJUuXBr6fSbPnNChjBfvfE3y2nrg29KK_KkZaHHzXscPx9654nwd8a1NlH7fSOCL2QQUn6mgmOxH9O1OLUw9DauluAocbND0IJCrdh1YxISre7dyhaQ0uWtHc4y1uopMqTLq71RgwXKaryruUDzK-DWqwXxl4lO8H7Nzjqx9VtW2LgBMKczDV-DDl_mgyvZen7f2ZO0shQInRfeEfO5y4iPhhdiPTSkHZS0jm2ugRb0W4zgmLa4Zdul2d1T89llhqIq9ErrT7N5XcmmfnCuqYkDUn9_mDoCgJxENyls3h_AZj3_KTLq1YyCRna4Cq-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپارتمان ۸۰ متری پاداش طلای آسیا
🔹
براساس مصوبه فدراسیون بوکس، مدال‌آوران طلا، نقره و برنز در بازی‌های آسیایی ناگویا به‌ترتیب
یک میلیارد، ۴۰۰ میلیون و ۲۰۰ میلیون تومان
پاداش نقدی دریافت خواهند کرد.
🔹
رئیس فدراسیون بوکس همچنین اعلام کرده در صورت کسب مدال طلا، علاوه‌بر پاداش یک میلیارد تومانی، یک واحد آپارتمان
۸۰ متری در تهران
را از حساب شخصی خود به مدال‌آور اهدا خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/462202" target="_blank">📅 13:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462201">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پروندۀ تأخیر پروازها به دادستانی رسید
🔹
قوه‌قضائیه: درپی تاخیر در تعدادی از پرواز‌های روز گذشته و نارضایتی مسافران، دادستانی تهران در راستای حفظ حقوق عامه به موضوع ورود کرد و در همین رابطه برای این موضوع پروندۀ قضایی تشکیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/462201" target="_blank">📅 13:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462200">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKbEfKfaj62ryNqPfMhDePOk7qij6VzupleRlOLUcIBqrUtShioDq3ZlCqoexCBn-S4Gd-k5dfYnUekjJWOa2VX6Fy4Bi6AYFalmDesLVAXmALJCKkRuT51XVLTU2Z2bUIoq29UnZTJ_24sm83f2tcR5cndnhGv7mTNZqF4r8cYIRMDYgRyB8hOwQvP49z8Imh5LZZ5WDnylp1qYr-hVXQ4NiuKyNf4jpjTablZoxLktQfNB-cILmhVjMrOzswPuO0fk-Cb1gRushDKjQjkymzIuZwfQvugNVU2LygmCD4xqzWxNqejuD1SIFYfi5A3ttoyk8pdBIgAKZTA72zuTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی انگلیس: یک منبع موثق گزارش کرد که دیروز یک کشتی در تنگهٔ هرمز هدف اصابت پرتابه قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462200" target="_blank">📅 12:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462199">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
هشدارهای حملهٔ هوایی در مکه، طائف و جدهٔ عربستان فعال شد.
🔸
یک منبع نظامی یمنی در گفت‌وگو با خبرگزاری سبا یمن ادعاهای عربستان دربارۀ حمله به مکه را «جعل، فریب و تلاش برای گمراه‌سازی» خواند.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/462199" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462198">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE-WSqLQ7syH_nu7UDyLHId7JbW-Us9ZHLQKhX_Eb5ianay78ieRUIV-9J4TR442yIS-jqRZW_PE7u4zB6LjVS9OafCZF7RvMFy9JEoe_WdGj0YfBRPeHZQCeEuwJu6KU1sGjaXyH4WxA2CUPiUh0T6dAkyqDNP2l3rPDFMrok47v7FQa9Aayz74dNqVI_010YZ6PAb-jkg4JtyfoackzCgRZtKP9EBVm7iVPbq9BmBRUCUtZvyiKkzQCgzvNuCvL4t80R39frxPiC15ZrmB-Eo6-zh5Zb0NyURm_8--dIlIw5SaXRXVaUQhUACZ-9hecgCmIeTk0o_pnS59bJtXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۷.۵ میلیونی شد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۸ هزار واحدی به رکورد ۷ میلیون و ۵۲۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462198" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462197">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f565b55999.mp4?token=uNP5qXrqMRlQDJ-V_Brf-uSeRrGzuPUa7tU3uEGZTLs3w8OvJa2lzQOLYcHXvSiwZOGdJDBcUwkxJg2PA8BgfqzulhYTAhCMthNEdpoNUHL1rhjHQUfDWjJ0fvgmfviKuedx3XoK8eUK3GghogP4wzcAr5UjbA4jhlGXhx0r2GRQK1HSoJWrDUOFsbnbpEUsgfKtO5jSFp8zLnnADGatV1TEXzrpo_v4iUulaILkS0VnTPJ5O1KuK8DC5KRojX9PvAbkAC9JB6CKnVPQlZxp5AIL9b6rFyMBWmKfFlw8tAQ3q1gMCTwU9n1v8u8L0JPjpMMEABlxlyJwWO_jG8dNrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f565b55999.mp4?token=uNP5qXrqMRlQDJ-V_Brf-uSeRrGzuPUa7tU3uEGZTLs3w8OvJa2lzQOLYcHXvSiwZOGdJDBcUwkxJg2PA8BgfqzulhYTAhCMthNEdpoNUHL1rhjHQUfDWjJ0fvgmfviKuedx3XoK8eUK3GghogP4wzcAr5UjbA4jhlGXhx0r2GRQK1HSoJWrDUOFsbnbpEUsgfKtO5jSFp8zLnnADGatV1TEXzrpo_v4iUulaILkS0VnTPJ5O1KuK8DC5KRojX9PvAbkAC9JB6CKnVPQlZxp5AIL9b6rFyMBWmKfFlw8tAQ3q1gMCTwU9n1v8u8L0JPjpMMEABlxlyJwWO_jG8dNrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر سابق علوم: قانون‌مداری را نمی‌توان به بهانه خطای دانشجو کنار گذاشت
🔹
محمدمهدی زاهدی، عضو شورای مرکزی جبهه مردمی ایران قوی و وزیر سابق علوم در واکنش به برخی مواضع پیرامون عدم برخورد با دانشجویان هتاک: باید کاری کنیم که قانون‌مداری در کشور حاکم باشد؛ چراکه در هیچ کشوری، مسائل ملی خارج از چارچوب قانون اداره نمی‌شود.
🔹
با بی‌قانونی نمی‌توان کشور را اداره کرد و این مسئله در بلندمدت به کشور آسیب می‌زند.
🔹
ممکن است کنار گذاشتن قانون در کوتاه‌مدت مانند یک مسکن عمل کند، اما آثار و تبعاتی که این رویکرد در بلندمدت به دنبال دارد، بسیار مهم و زیان‌بار است.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462197" target="_blank">📅 12:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462196">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiAQIcRIrAvt7LEDHnnRZon68AbEzSd6an3pLE-YUEgPZGPFs2admIOaYd9ZCCDU8f9fI_patk9RBExLfzbG1JlZ7B1f7ACPxUvLY2ZzUJf_IZ3dsVWjfpOnL8WBFZF5jCuE1qobnDTvgGPLcAzbSKAbbMIRQExEy4cU9fEu-wtB8OzpmKTHIC-jw3zrwKZOUbcsTVl9L-ytBLgJ11sh_JAjjd_Nq4472dXnjenGyTKlN6inydRPb_4jlO6qjCXnCCLDqLC4jGJThwsDJFYZnyjjXyAklm8ClKSQiOuMrxEnLPvqChPMgA2Z3k6QWxJQUwlQZ9TgC9yk1f-4f5Q42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پکن: عراقچی فردا به چین سفر می‌کند
🔹
سخنگوی وزارت خارجهٔ چین: وزیر امور خارجهٔ ایران فردا به چین سفر خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462196" target="_blank">📅 11:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462195">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc729cdf9.mp4?token=U4Egk5JFfrzDRkwz6zPmsfjF0Ir5lAGZJ0wnD7ZSSCNEbKvWAaxjCw2YvdUVZK8yc14pXN460n4mtLXoVlbVachyreyUbuaqrQoxtDOlgUcM7p0DGRGa5uz-h9OQfy1DMj1IjYlYTyZMCNR98uoZoyBujwhlKee4MrKn5QNoncMzmg2b34fyRy0JySzd4pETyHlz2EVEEedolxy26P6XT4jMKuKsllMTkqA9L1w1kldV1r3v1UlMHCne-BBMzp0tCE6GIwfwMF4PMkI-vKlU4aAoMZtjB1a0WUvYoIhBbgYWYM_0zkwugQC7heJeMRi01d5S0GzVyOj2LpQhpkH3tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc729cdf9.mp4?token=U4Egk5JFfrzDRkwz6zPmsfjF0Ir5lAGZJ0wnD7ZSSCNEbKvWAaxjCw2YvdUVZK8yc14pXN460n4mtLXoVlbVachyreyUbuaqrQoxtDOlgUcM7p0DGRGa5uz-h9OQfy1DMj1IjYlYTyZMCNR98uoZoyBujwhlKee4MrKn5QNoncMzmg2b34fyRy0JySzd4pETyHlz2EVEEedolxy26P6XT4jMKuKsllMTkqA9L1w1kldV1r3v1UlMHCne-BBMzp0tCE6GIwfwMF4PMkI-vKlU4aAoMZtjB1a0WUvYoIhBbgYWYM_0zkwugQC7heJeMRi01d5S0GzVyOj2LpQhpkH3tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربۀ کاری ایران به گره‌های حیاتی شبکۀ عملیاتی آمریکا  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462195" target="_blank">📅 11:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462194">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ruj2BfrdwukkzaPdsgLYALuXDbr5HK4ZiMpfgjGdm6EmfE9soCcnmXpKjxH7MLQrabfka2RR1UWf3CHBCcuWjyz0aDJ4GYxZJ7ZtB1RbCQJO3t8vPgKF3tvod0vxKiu6pjBr9Kg5fPCLvsx_ZDdSRp98pxwjwuSlobL53KFh9xmYic4bKDXg919-OX8Kk1kCqJa4WP11LeN3XHnQupXlodWV-MG0R5c4rP4VJI2nW3qgyvpqlpGuNgE6P_yIC5BLezHEQI3XLh-hC3jMMbJG79EqmoSb16o5j5gZXbaWj2-9kYazMY2oRy78rfjQVIZq9IlgE0WDVfiJveUQZIwMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سالگرد عروج «رضا سراج»
سردار جهادی و عاشورایی
🔹
زمان: پنجشنبه ۲۶ شهریور، ساعت ۱۶
🔹
مکان: مقبرة‌الشهدای شهرک محلاتی تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462194" target="_blank">📅 11:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462193">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
حمله پهپادی به اربیل عراق
🔹
منابع عراقی از حملهٔ پهپادهای ناشناس در شهرستان رواندوز واقع در استان اربیل خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462193" target="_blank">📅 11:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462192">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekQg-s93nLb2l29_3XLBAjmT26jnXKCF5uFN3V1_sb7F0aIEH93TSOpgkmIRWaSeHLBmB-IOFs42jyQz_8LXI2XuM45a-5eIdEFDT5rEDPB90a_1PWDgyXrcd3mQD-6oswg3zbca5VUygr-wtJPR8wxgdtjdtyma3vqkEzzN_JV0ABgymDakKEUDUccGG3GdkBdBfb5zrmFo_g3BBCQdBr4pcatMWo6HMDF4Ftc9RkHjBHKqXMABZGBoli33oGkDrfstnrunh9mzsGyFIH1irEtYs81fvJ5hW1Y40sLuMPgm13toJmM9IxiqTO4KlTJ_iQ7y7WQVPAobqCRbELIKDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بافل طالبانی، رئیس اتحادیهٔ میهنی کردستان عراق با عراقچی دیدار و گفت‌وگو کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462192" target="_blank">📅 11:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462191">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjbxdxYPPmIBycgg-_owJfXsgYpPx--0nab74INwNMx3so5jdJwPqDBsNmQRh1QQqMMkEUKcnCmb_9v4_oXrG518LIwxm5wEMoimmmeDa4Izfe9j34DVyaxwcZr0R5YvgPlpNEPVSLYQVEGJWlQOtpVhT0q5DPuQkh8kQWyTzmWHo3kuAPlCerRPGaK2psp2CHMFv48xmhYGRocQPQWhFki_1gFbG2hDULMxKBqMRFmQ6huJDxxekF1cK4WKaSL5KNPYBSDv2IWdV6IPUspQB7_q4Nl093Yh5W-axa7x8bzHOMHcP85InBw7CHaDudBUhrvMYi0zzS24cU08h8htrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۵۳ سکهٔ باستانی متعلق به دورهٔ اشکانی در لرستان
🔹
فرمانده انتظامی لرستان: در بازرسی از یک خودرو در سلسله، ۴ سرنیزه، ۲ شمعدان قدیمی و ۵۳ سکهٔ باستانی کشف و ۳ نفر دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462191" target="_blank">📅 11:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462190">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab10f633d6.mp4?token=qpWXjOfhjFJ87qyf4YFXrCB1G8fwigwlvMiBqy5ty4B5qXYwqr6eUdCGGBhLEJmaD_SmSR_SdPrE7ouLMMPPTPQIS-iOnfDpm67idgiQp23iBL1MmwAjl5SmWrytxuSsWEImDza7Wy-LE3z_AhpOUKorxu6dg0AoytDavuRwNOi0Fdfx38s010HC3El53jkP7vYM8akAdICZw8fI3Iu7m1EGuEtEw2TQGcRk7gFiYvpSm-gpFP-rtni7JWVusaxdgpeqN2yqAv68HWTfUTKS9JadZ0bkufwWAk3OvKkQAnpxI1dReZTko3jjijBnoKby760kQj9pyF9oEEdT-FmXLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab10f633d6.mp4?token=qpWXjOfhjFJ87qyf4YFXrCB1G8fwigwlvMiBqy5ty4B5qXYwqr6eUdCGGBhLEJmaD_SmSR_SdPrE7ouLMMPPTPQIS-iOnfDpm67idgiQp23iBL1MmwAjl5SmWrytxuSsWEImDza7Wy-LE3z_AhpOUKorxu6dg0AoytDavuRwNOi0Fdfx38s010HC3El53jkP7vYM8akAdICZw8fI3Iu7m1EGuEtEw2TQGcRk7gFiYvpSm-gpFP-rtni7JWVusaxdgpeqN2yqAv68HWTfUTKS9JadZ0bkufwWAk3OvKkQAnpxI1dReZTko3jjijBnoKby760kQj9pyF9oEEdT-FmXLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر ماهواره‌ای از خسارت یک ایستگاه پمپاژ دیگر در خط لولۀ نفت شرقی-غربی عربستان سعودی در اثر حملات اخیر @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462190" target="_blank">📅 11:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462189">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDuMxAictzRaX7A0xD0Gdbe2-1j9404q_C23c12IUYk-GXaoZQH1SXBhSKx63lTSvE-3Cnlr3K5zA9UlemqrFtXhb5ow35JX8TrWKr2qNYnKNvk65FLhlQhiC0aNVmDsxe84I9iVnvV_Jl9tFVJyNiJwAuKwukjUwbo9RcGyHdq0InTwDGCC1BHF6vGNvKzRj2hYwvq8jMN1u961n55bYkIuP2xmt5-kna5k70xSP2vypi2k6wDpBrZxDpnWN0_z-U796V0AbjS-kDYEzuaBFg_9AnnXfJhI4eCW7LyNucjeFCsGLZ30xb4W6VbNHNVsz-RTSg4m19LA8Bxh0LoFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاندوزی رئیس کارگروه بررسی‌های اقتصادی دفتر رهبر انقلاب شد
🔹
مراسم معارفهٔ احسان خاندوزی به‌عنوان رئیس جدید کارگروه بررسی‌های اقتصادی معاونت بررسی دفتر رهبر انقلاب و تودیع علی آقامحمدی، صبح امروز برگزار شد.
🔹
خاندوزی عضو هیئت علمی دانشگاه علامه طباطبایی است که در دولت شهید رئیسی مسئولیت وزارت اقتصاد را داشت.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462189" target="_blank">📅 10:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462188">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec6b71e3d.mp4?token=CL3l1SGxnOcLrlix2EVvHd0-xkF8IwFiIdN1i2FCtIbleI58wBILMlaW9SRhS4Efy5OHLQNc22ROEZ4_GkAZSaWtIROgiiVktA-ntKp14qvxsvL-nQyLy-_XS7WngABPW_r4ma1kYa6vfni9h6reH3pd4NYFljpkHK50JmRxsS5xHTTK1DqgC9zhpZHSgxWn5fP1XT9nlhM1w_dhflZgLV4KEXWix43RNpGsAbTj8XXHsMHDmktJ2FV_0jmFmGEWXjiORw5o_98ED-ctXyyQo1ZPUOPYb6hHUV--4jh00Gv8ILtugsyK_Pw3DTs19Mrz_0qMQdEltXbR_jo66VR1_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec6b71e3d.mp4?token=CL3l1SGxnOcLrlix2EVvHd0-xkF8IwFiIdN1i2FCtIbleI58wBILMlaW9SRhS4Efy5OHLQNc22ROEZ4_GkAZSaWtIROgiiVktA-ntKp14qvxsvL-nQyLy-_XS7WngABPW_r4ma1kYa6vfni9h6reH3pd4NYFljpkHK50JmRxsS5xHTTK1DqgC9zhpZHSgxWn5fP1XT9nlhM1w_dhflZgLV4KEXWix43RNpGsAbTj8XXHsMHDmktJ2FV_0jmFmGEWXjiORw5o_98ED-ctXyyQo1ZPUOPYb6hHUV--4jh00Gv8ILtugsyK_Pw3DTs19Mrz_0qMQdEltXbR_jo66VR1_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: رقم کالابرگ قطعاً افزایش خواهد یافت
🔹
حتماً در حوزهٔ بهداشت و درمان بازنشستگان و معیشت، تصمیمات سازنده‌ای گرفته خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/462188" target="_blank">📅 10:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462187">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84312e9cf7.mp4?token=A6spwNFfsX4EFi5wCNhYtAKJopWNVBwYRIr06rSlHqzdBCbh2X-z9gjXrjHWrNikCQMSuhA_SdDU5GYkzYz0NTnwYCr8VlX49PP-wO_MeipgQBDH8pWLrEZBFXFfhz0u1gOuZ7JrRDm9xZDlGzY0EF7wRWVHjD6iKVYXhe6j6IjOfxCZmMVhDuvc3rg9RK6zQgYNwtpqdHNWlJCCTKz_voUd0hFCkcBf01pluPJnlJ5vW1sfid3I8a7cUbhc0bjNgrSoh6o7EajWJzP1dOi_RXi4QbCeQYh8bR36oGy-GTAzXzHRj10pQy_MFgGYOdtJ3GwZ5WvIe94EnJej7APkyradWdKHQwdsmB1QS_qODPsx96sXzurr_0PETmI6S1UvSUPOPAwUu2z4dER-9BnRcyv7k5imxrt2QlGtkhIJbUv1Fd0uqOighBL1otAG1VyPXbTIeo2yyeOufBzrouF3slvkbUq0lV9XV3NcbQvtw17KZqHxOYBcAkWSgYBh7YKp7KUlEbne8VKkFWDH5XRk1xyPodubNBej3kbjJkQhcIYz7AUYij2x2xgHFTMOQ6SE0XRWhJTIWnsATjto1ZIk2d050hFsNVk7GH35OiiEa3JYGbEk9xZfoncnKgZAqzww7CMC0-8Q6dpw2LezmH7ZWEtlMJUd4tSOWRs6nn9s_Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84312e9cf7.mp4?token=A6spwNFfsX4EFi5wCNhYtAKJopWNVBwYRIr06rSlHqzdBCbh2X-z9gjXrjHWrNikCQMSuhA_SdDU5GYkzYz0NTnwYCr8VlX49PP-wO_MeipgQBDH8pWLrEZBFXFfhz0u1gOuZ7JrRDm9xZDlGzY0EF7wRWVHjD6iKVYXhe6j6IjOfxCZmMVhDuvc3rg9RK6zQgYNwtpqdHNWlJCCTKz_voUd0hFCkcBf01pluPJnlJ5vW1sfid3I8a7cUbhc0bjNgrSoh6o7EajWJzP1dOi_RXi4QbCeQYh8bR36oGy-GTAzXzHRj10pQy_MFgGYOdtJ3GwZ5WvIe94EnJej7APkyradWdKHQwdsmB1QS_qODPsx96sXzurr_0PETmI6S1UvSUPOPAwUu2z4dER-9BnRcyv7k5imxrt2QlGtkhIJbUv1Fd0uqOighBL1otAG1VyPXbTIeo2yyeOufBzrouF3slvkbUq0lV9XV3NcbQvtw17KZqHxOYBcAkWSgYBh7YKp7KUlEbne8VKkFWDH5XRk1xyPodubNBej3kbjJkQhcIYz7AUYij2x2xgHFTMOQ6SE0XRWhJTIWnsATjto1ZIk2d050hFsNVk7GH35OiiEa3JYGbEk9xZfoncnKgZAqzww7CMC0-8Q6dpw2LezmH7ZWEtlMJUd4tSOWRs6nn9s_Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرورت هم افزایی و مدیریت منابع برای توسعه پروژه های هلدینگ خلیج فارس
روایت حسن عباس زاده مدیرعامل پیشین شرکت ملی صنایع پتروشیمی از وضعیت این روزهای هلدینگ خلیج فارس
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/462187" target="_blank">📅 10:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462186">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVCwxWkIHH2IA52_8EDKOQMlSiI65Ez_wvIxVspGuPg7qQXQ-LKgxfBMnkDaPYZN3Ttt0Np-THw0zcRZ2Y-1KGAprmidte0MhKSFOU3EGB1mQK8QcLV_XaofwkUIi2FCCxEybLiEnHaVZLbTBI-w7LrnCOOPJ3ASUAVc2hOZD1x4j5dNoSHo2KrmT7ZJsOY0xjZXlFCSuXetLf7NF9isCS5sr7-9CSHFUdS477CPjgbNYOAkman4-gQ-2zkuFICOu2ya3nsFrFCcRGgxD0733eTeUnhoyJq6ICvWfSthgnQ9V0m2JsjrW1te69U1v4gUnZda6v0gsTnqrM0deMlhag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/462186" target="_blank">📅 10:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462185">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/462185" target="_blank">📅 10:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462184">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b36daf3ec.mp4?token=hs56eUzxwXMbRRu1PBWP5eCdKrCkD_zZm-bkL0DahYdyz9mfoufWFfS41rqAtx8n-cvKJ2fHASmkVeG8B6zlo4_vPqTIdiU_xh2jw5-75oQq31eZQLnS-8J0Q6zoJZSMUL-jZHgMitQbrs0ijEN_KvxrFL-Fxt5GenOy9TztPqZzLx3lyPVG8urWWnyocm-w4R6qnieFbUzBte5kUeMOpeh8CcInb096MuSqQmjv7LecvHqqNOh8JnWIGb42I2lyK6_PbtmWjclK1BPQCFvhRgtU_IaLZ69rDId72PhZ1zWBFmOjJG-kBeMf_P2JHLAn6nntEtoO6fQ7q8JK6xGn8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b36daf3ec.mp4?token=hs56eUzxwXMbRRu1PBWP5eCdKrCkD_zZm-bkL0DahYdyz9mfoufWFfS41rqAtx8n-cvKJ2fHASmkVeG8B6zlo4_vPqTIdiU_xh2jw5-75oQq31eZQLnS-8J0Q6zoJZSMUL-jZHgMitQbrs0ijEN_KvxrFL-Fxt5GenOy9TztPqZzLx3lyPVG8urWWnyocm-w4R6qnieFbUzBte5kUeMOpeh8CcInb096MuSqQmjv7LecvHqqNOh8JnWIGb42I2lyK6_PbtmWjclK1BPQCFvhRgtU_IaLZ69rDId72PhZ1zWBFmOjJG-kBeMf_P2JHLAn6nntEtoO6fQ7q8JK6xGn8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از ایران خودرو، سایپا هم گران کرد
🔹
براساس آیین‌نامه اصلاحی ماده ۱۰ قانون ساماندهی صنعت خودرو و افزایش هزینه‌های جانبی بهای گواهی اسقاط خودرو از ۳۵ به ۶۰ میلیون تومان رسیده است.
🔹
حالا قیمت چانگان CS۵۵ پلاس، سیتروئن C۳-XR (تیپ V۱)، کوییک S و سهند دوگانه‌سوز…</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/462184" target="_blank">📅 10:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462183">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aba330e26.mp4?token=XekFx5liI82s8j1cRpD1jhp6Fa8krMfRSeJUZUvCd_wT-fupYqjaMNhTHORA4MPMarReQjRICzbPkrGuRVSbmxg7GpSaF2lRgcJBOyWJomuvlpGGcgFrKAI7l-tXrstgZks7z7o8npjycOgyEQZ5RP8WKE2YoOOECCTRFUkbxN7Dv2-wfHoqPI1zlmpyucu4aAPnLRucT8pu4UNK6y5r_3AA8-OZrqayVkoLdeqOcrKC-vTuT8Ui63rUgYUVg8VmuySzpKstbAhq6VO87zjf2tXnIbOkkPCl-ETwvmbmSkwe_aF8kR-MtIcWDHsfhhjarc9IF2gLXKff_yAArUkidw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aba330e26.mp4?token=XekFx5liI82s8j1cRpD1jhp6Fa8krMfRSeJUZUvCd_wT-fupYqjaMNhTHORA4MPMarReQjRICzbPkrGuRVSbmxg7GpSaF2lRgcJBOyWJomuvlpGGcgFrKAI7l-tXrstgZks7z7o8npjycOgyEQZ5RP8WKE2YoOOECCTRFUkbxN7Dv2-wfHoqPI1zlmpyucu4aAPnLRucT8pu4UNK6y5r_3AA8-OZrqayVkoLdeqOcrKC-vTuT8Ui63rUgYUVg8VmuySzpKstbAhq6VO87zjf2tXnIbOkkPCl-ETwvmbmSkwe_aF8kR-MtIcWDHsfhhjarc9IF2gLXKff_yAArUkidw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دولت ۴۵ روز برای معرفی وزرای اطلاعات و دفاع فرصت دارد
🔹
سخنگوی هیئت‌رئیسه مجلس: با دریافت اجازه از رهبر انقلاب، دولت از ۲۹ مرداد به‌مدت یک‌ونیم ماه فرصت دارد وزرای پیشنهادی اطلاعات و دفاع را به مجلس معرفی کند.
🔹
ایدۀ حذف شرط اجتهاد برای وزیر اطلاعات مطرح شده؛…</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/462183" target="_blank">📅 10:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462182">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
عربستان از صدور هشدارهای خطر در شهر ابها خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/462182" target="_blank">📅 10:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462181">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انهدام یک فروند پهپاد پیشرفتۀ MQ1 در تنگۀ هرمز
🔹
روابط عمومی سپاه: بامداد امروز یک فروند پهپاد پیشرفتۀ MQ1 در آسمان غرب تنگۀ هرمز رهگیری و منهدم شد. @Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/462181" target="_blank">📅 10:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462180">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
حملهٔ موشکی عربستان به صعده
🔹
المسیرهٔ یمن از حملهٔ موشکی عربستان سعودی به منطقه العصاید در استان صعده در شمال یمن خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/462180" target="_blank">📅 10:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462179">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crf_qWsdWrVRo1kYiDDOrbUWo8HaCsuWhKp4cHwmpRbWX-IiBAair1iwH74qIGmecZgn2BqFvgip2XTN-ltWj-sN84Qjz1Y7jZ5G_kWhc8L7IpdGXodA0VJ0saRTT7ZVMyzAJSHyFInl5_ksI2Hb9ITQq9RxiLCaNieu-6qzIYnPehhcA9mk5mm9mD8Kx4ddqWEdsbRJQedL0g-7TbFZV4d_Dd2_XrSGyvCjTvyeHDz78FXPP3h09HzRpVvtPAWTAT3zkDFbzI-F5Rtl1TvQwJ8_c-TIXz9afOwBhUxW5DwzLReoYDJFfVgTy7G_mg0WkOdIGN14FDbgpTkKHYyT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تزریق سنگین پول صندوق توسعه به دولت
🔹
طبق سند رویت‌شده توسط خبرنگار فارس، برداشت دولت از صندوق توسعه در ۴ ماههٔ امسال از ۳۴۰ همت فراتر رفت که براساس قانون بودجه این رقم ۱۰ همت بیشتر از سقف تعیین‌شده بود.
🔸
گفتنی است سال گذشته در ۴ ماههٔ اول برداشت دولت از صندوق توسعه فقط ۱۰۳ همت بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/462179" target="_blank">📅 10:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462178">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3cf2998c.mp4?token=SHfF6_27EX3Q_dNXz3ug-FAmEW-JoYKeFdzEKQ13gsBg_A6asgWKTZ3QOBhuUdt0fACyWLVOQs72ZakuWq7SzfU95_-613RG4GgaY1Tp2-zYhR1PN3fjLTENkV_pUehSQDZD5o66MTeD_0--N4_Df4pL_5-79FumpecKdqQ3bnnEvil_fLR27CaJ2rQO6TIFYwuJvbKIlO8PKZP-vHB6h81qQdmguO3trXcCVnaWvZ6DbbSwvs24KHLz_ZuG5oq-ZskGI7NGtSb_Rs_fn0wgQFgqBHIMSUuQg0NEOvsMKho8mg6W3v3RZ86PGsky2dfBG0mQY253d1raupy79jLqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3cf2998c.mp4?token=SHfF6_27EX3Q_dNXz3ug-FAmEW-JoYKeFdzEKQ13gsBg_A6asgWKTZ3QOBhuUdt0fACyWLVOQs72ZakuWq7SzfU95_-613RG4GgaY1Tp2-zYhR1PN3fjLTENkV_pUehSQDZD5o66MTeD_0--N4_Df4pL_5-79FumpecKdqQ3bnnEvil_fLR27CaJ2rQO6TIFYwuJvbKIlO8PKZP-vHB6h81qQdmguO3trXcCVnaWvZ6DbbSwvs24KHLz_ZuG5oq-ZskGI7NGtSb_Rs_fn0wgQFgqBHIMSUuQg0NEOvsMKho8mg6W3v3RZ86PGsky2dfBG0mQY253d1raupy79jLqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چه شد که پس از ۶ ماه، مصاحبۀ جنجالی خلبان آمریکایی منتشر شد؟
🔹
روز گذشته، شبکه آمریکایی «CBS» در مستندی مدعی شد با خلبان جنگنده‌ای که در ایران بود، مصاحبه کرده است؛ یکی از بخش‌هایی که در این مصاحبه مورد توجه کاربران خارجی قرار گرفت، این است که فرد مصاحبه‌شونده…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/462178" target="_blank">📅 10:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462177">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fce12fb8a.mp4?token=jW-RwTlDkYTj_lhtjfg5aZI21V34oGECux2qq8EkQkhcSJgrvt-Rd3gchm85ktZCnMrVBv79jxKI--FzdnbzOZlGKWQFybWxbBu1szInm1dTTlujh-6Cmr4ObbgLUZAGdzGRP-fhwXbCWF6244S-M9mPzulrQuRMnFfOg1np3qU6bYJnRJJCLEWS5asNhe-lJ_VnT7T8TUZyKyHE2vIwFRnB_d67GM4XNrwDMRaeuORWeHxIUKDyv-sXa5CtHF6MS747X-Rq-XMlslXmRPaBqLThNoWCuuDpw0gSciHkgP4Xou6upRrN84fApQvBFGoYTHqN3YUvK-rcCiGyoN5JuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fce12fb8a.mp4?token=jW-RwTlDkYTj_lhtjfg5aZI21V34oGECux2qq8EkQkhcSJgrvt-Rd3gchm85ktZCnMrVBv79jxKI--FzdnbzOZlGKWQFybWxbBu1szInm1dTTlujh-6Cmr4ObbgLUZAGdzGRP-fhwXbCWF6244S-M9mPzulrQuRMnFfOg1np3qU6bYJnRJJCLEWS5asNhe-lJ_VnT7T8TUZyKyHE2vIwFRnB_d67GM4XNrwDMRaeuORWeHxIUKDyv-sXa5CtHF6MS747X-Rq-XMlslXmRPaBqLThNoWCuuDpw0gSciHkgP4Xou6upRrN84fApQvBFGoYTHqN3YUvK-rcCiGyoN5JuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
🔸
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند. @Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/462177" target="_blank">📅 10:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462176">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d761ffc99.mp4?token=tJQeHuoD_fUk2_qXyWdbDAGR1ekfVzMJDzkFFcMvIb-rp9wCPO83GXKR6b7l0gt6NdKIgJVLDHsO4CClKRn7fnsGfIcTkw1xPX7qz7ysWkZC1QHAXALI2YqYnytqcbwGPETDxvYCXvpKFX1K4GRkVl2cB1cPCeuEwHfGeyuC3qSWYE78iJ-JAXugz1gJIY3kunzPLwLjcgriyPVC6WhAPiITiVjJaWIsocrfme9Lr60E0Y1vA82EtiUws34Iz05tXzZlElh93pYHBNnUtuDwi2-5K-bX2qxw_tkF_buRQPp_R7Gdv4e3jZeqdvPlr3lzEQCBj6gTKBAVeSr74X17tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d761ffc99.mp4?token=tJQeHuoD_fUk2_qXyWdbDAGR1ekfVzMJDzkFFcMvIb-rp9wCPO83GXKR6b7l0gt6NdKIgJVLDHsO4CClKRn7fnsGfIcTkw1xPX7qz7ysWkZC1QHAXALI2YqYnytqcbwGPETDxvYCXvpKFX1K4GRkVl2cB1cPCeuEwHfGeyuC3qSWYE78iJ-JAXugz1gJIY3kunzPLwLjcgriyPVC6WhAPiITiVjJaWIsocrfme9Lr60E0Y1vA82EtiUws34Iz05tXzZlElh93pYHBNnUtuDwi2-5K-bX2qxw_tkF_buRQPp_R7Gdv4e3jZeqdvPlr3lzEQCBj6gTKBAVeSr74X17tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: رقم حاصل‌شده از افزایش نرخ سوم بنزین تماما صرف معیشت مردم می‌شود
🔹
به‌هیچ عنوان گرانی‌ها را انکار نمی‌کنیم و می‌دانیم که گرانی‌ها هست.  @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/462176" target="_blank">📅 10:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462175">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76abeb4452.mp4?token=GQMHiBIylN-dVv5D8ciNINnx6UgN-V4IgogwXZyNyQSEhAWV3pU7HyOzbI8ob74ts9FJUgZdGu3DwAoqlBjiFHvFvIpBCxHZ68YEJzysXSTY7nYucZtOQHjqZ0dZxTj4ETbPvLhsKa2vSidkdnKSFp7e1HcKYhQNBnsn_9eq2e-ASRvXqFQVPJgJ_3i6tIYwLBAHqc3Hfcq2KM0S_611XN-xuNknUaMlpAu9_-0y03cE7VYKgAB0cCS3nedFrbKAXhNtMsXV6itCkmf4fFWIyPRf5RrLX8mN6iJmwDtkBMbhsyyNFvSWB3msip6Ssy8WbUp3DH9nZaXyQsk0uH9jrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76abeb4452.mp4?token=GQMHiBIylN-dVv5D8ciNINnx6UgN-V4IgogwXZyNyQSEhAWV3pU7HyOzbI8ob74ts9FJUgZdGu3DwAoqlBjiFHvFvIpBCxHZ68YEJzysXSTY7nYucZtOQHjqZ0dZxTj4ETbPvLhsKa2vSidkdnKSFp7e1HcKYhQNBnsn_9eq2e-ASRvXqFQVPJgJ_3i6tIYwLBAHqc3Hfcq2KM0S_611XN-xuNknUaMlpAu9_-0y03cE7VYKgAB0cCS3nedFrbKAXhNtMsXV6itCkmf4fFWIyPRf5RrLX8mN6iJmwDtkBMbhsyyNFvSWB3msip6Ssy8WbUp3DH9nZaXyQsk0uH9jrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف دولت از افزایش نرخ سوم بنزین چیست؟  @Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/462175" target="_blank">📅 10:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462174">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfxxWdtzdjqQ0jed0EEv--wWPJ5ET6-pUCuMniy7iopwq-TSRLbTfH49dZnjkg9vi21KZ-aBDklRRCU_ixDP1rAcgrzhlGQpRDlxlwsYTbt6tNwFI3Dg1F5Dr274KF0SztfM9Si3EzqDoPorh_el9in3NPbjXtu07C_ljR5tYikQ0nfOA5bpMb9kgXU5BgzUnTLdENdcptzBNN3-3DUvulN9kes8WhKg2uE1rXuLKjOcDQKTjYtThy7fGG9eJvnxLYDUJ8b8Nu_wAH9lHs8pfi-F8oaw1UOevmYmjDG5TZTwvAhm_HRA6uZzEF-K4DGC8Gwaueg4SCYTIhPjZ9rCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف
محمولهٔ یک تُنی مخدر در ارومیه
🔹
فرمانده مرزبانی فراجا: یک تن مواد مخدر روانگردان توسط مرزبانان هنگ مرزی ارومیه کشف و یک قاچاقچی دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/462174" target="_blank">📅 10:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462173">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سپاه اصفهان: احتمال شنیدن صدای انفجار کنترل‌شده در جنوب استان تا ساعت ۱۳ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/462173" target="_blank">📅 09:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462172">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6XHOHG4IHq0v-58JfFtHcgpppm-TKPgV6C8WvMT0ofKel8JCrIyKKOHOrIlG19weJTtxCa75QNlVUxL0Xb6XY4N73xaPIlU9hwQHa-UVsaDN8_iPrOrXEyXRHYlz_sLRaMTZvwXwy3lyBRBrMjtAE4NTacjWpUUiOT0laSeQUMMsi_EI2JpN3PeVMM7bQG3eh0HVntIXfL_ibjtATVHIBfIRuIVEc8ft7jz1VTHXImbRs9NnV6ke68O8BDfsLttLycnUrZLZyFabJ0_dHk7wI9AgdR-I8c613QHnhv0izntg2BtzTWt0rjw4qt540r8F36MULzK2Fjnp6ZmeGaCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ارتش مایۀ افتخار ایران است
🔹
سردار محبی در دیدار امیر اکرمی‌نیا: ارتش مایۀ افتخار ایران اسلامی و سازمانی قوی، مردمی و دشمن‌ستیز است؛ در تاریخ ایران، هرگز ارتشی این‌چنین قدرتمند، مردمی، آرمان‌خواه و پای کار وجود نداشته است.
🔹
همدلی و همراهی موجود…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/462172" target="_blank">📅 09:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462171">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDLWh6L0xInEnpyjq_joG4fC4-jFEBU3hD1w2sf5lO2aJLWsMkjGWd8FBMgJkwl9m1LJOSMozbOM1Ucc4aAOxvXcvBZDw-5-ZW7_GtJ0-PxN9iTkk5alFMdchnpt61iYN9VsNxVUsgmpQ1pJBVOJ87YzLp6Z4mu1akQzvdPWgahqEiVLeZc2YcrQG749IauTNv4E8l-Xv5lh6FjSXTOBQ-fXR9TsZdCeXlTqjFv_yBGi4EQxzmxBJZaUXFzBXL_MGJvjOfLYJ_1UI1BcxaxWNklwVv9e7HA8m1iBbr8ACrf6OHs8VDd7BxuMMOAK_0Z6oOfX09s1Op51Xuq4JeB-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ارتش مایۀ افتخار ایران است
🔹
سردار محبی در دیدار امیر اکرمی‌نیا: ارتش مایۀ افتخار ایران اسلامی و سازمانی قوی، مردمی و دشمن‌ستیز است؛ در تاریخ ایران، هرگز ارتشی این‌چنین قدرتمند، مردمی، آرمان‌خواه و پای کار وجود نداشته است.
🔹
همدلی و همراهی موجود میان ارتش و سپاه و مجموعه نیروهای مسلح با یکدیگر، نیروهای مسلح با دولت و مردم و همچنین همراهی و وحدت مردم در میدان و خیابان، باید در تاریخ ثبت و ماندگار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/462171" target="_blank">📅 09:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462170">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtAeS0UrkQM0Uff4snyNxFotCmHy91exD9ptNSrnijvbMDKvZfgczGPLdgvwDU99kHgdvny2P9f1Vuu9GlpvonPZCP8Smvf4BhNAOaDSfYgBX7h6ppjiyaN-dGwXWFyIkM0BNxWm-I_n2AEFSm4BBGRU-Rzl8YrTyxhvL-ejEea6jtQf4TmD9SZiuqprS9MB-8tgnlk3izkzateEjyKpCXo5XGpX54G4P-LkGfA96P7sjlCKSPxhHjNz75CFWPNnlDpDQcM2GYXLNqIrliwNgWVQDJ1qLDlMkXIkWT37TP_htFYuUaLX8BLwW4HurEfdAcFu0AgF4kroPip6va3vwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/462170" target="_blank">📅 09:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462169">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anPlKMrmQnn3tXCRUI9itb-XBrDBAVz07oE-NvDTkrr7iDO0a-kfjYtEU7xPOXBcd2MOalIzYZeH0HvrXGnhsHSqRCyrxv2lHdStxRMjyOVmwk59PlCuTB2QDy7cqKbLcveNu-fUBLd0i-_lbtZpOXfTmd83Knnbg2_BjYUrvtOGWxKPdEUY65I8K88iOpigd2za482MiRzFbw42kEgUj6lVJDLs42jzeT_mJTSvCcP0g6a00-JkLLURwZxNlH3Bd3vR7H0lQI-Uqijid9An2n-f9Kg-5HX_AbW8v4XlpX4P5i9p8m2wmg4j0XrftwvAO-8iMlHrW9Ejm5GgLgK-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلاغ دستورالعمل اجرایی نکوداشت پدافند غیرعامل
🔹
دستورالعمل اجرایی نکوداشت پدافند غیرعامل در سال ۱۴۰۵ در ۳ وضعیت محتمل
🔹
۱- شرایط عادی (خاتمه جنگ)
🔹
۲- شرایط بینابین (نه‌جنگ‌نه‌صلح، مانند آتش‌بس)
🔹
۳- جنگ تمام‌عیار به‌منظور ایجاد وحدت رویه و استفاده از تمامی ظرفیت‌های فرهنگ‌سازی و آموزش عمومی دستگاه‌های کشور
🔹
در ۱۰ ماده از سوی رئیس ستادکل نیروهای مسلح و رئیس کمیته دائمی پدافند غیرعامل کشور ابلاغ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/462169" target="_blank">📅 09:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462168">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af7467f44.mp4?token=NlnnNzCwUeJCAPwcxsO4XRkw9CXJV8hxgSfI4_2F0MDOt5EakIEmdwqlwoOr5PcfyVob9W2ZXHG-pJWvtrkTD8kSIhWiqedru9ReKVgQoGeaoiBQ5LVNgmie7jNfazO45C6oTiawDIPyWvTCVE0WgNw0DSsVljEq7jrS6ihc1nvWETNnPXdD5DK_C1To1mNjKT7tliokfXlrRoRdavIs813rFyhe8qrw2uF7U9bVexpT2UJEi4rD_5uB1hmxZrJ4FSLxgWvThDy-sa_pT7PwEl2VAUhizXoAcOgRrNVQ0uoQpokymFQ_ZPwc3--8fJOvx88qTFxXbcKdlMnYnLrMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af7467f44.mp4?token=NlnnNzCwUeJCAPwcxsO4XRkw9CXJV8hxgSfI4_2F0MDOt5EakIEmdwqlwoOr5PcfyVob9W2ZXHG-pJWvtrkTD8kSIhWiqedru9ReKVgQoGeaoiBQ5LVNgmie7jNfazO45C6oTiawDIPyWvTCVE0WgNw0DSsVljEq7jrS6ihc1nvWETNnPXdD5DK_C1To1mNjKT7tliokfXlrRoRdavIs813rFyhe8qrw2uF7U9bVexpT2UJEi4rD_5uB1hmxZrJ4FSLxgWvThDy-sa_pT7PwEl2VAUhizXoAcOgRrNVQ0uoQpokymFQ_ZPwc3--8fJOvx88qTFxXbcKdlMnYnLrMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
رحیم‌پور ازغدی: ترور شهید گرگیج به‌دست عوامل اسرائیل و تجزیه‌طلبان تکفیری، ادامۀ جنایات جنگی دشمن است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/462168" target="_blank">📅 09:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462167">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7tCsh_-mK19xgS7p8-VAczhcc_kmKdEmlVqed_7PFUBPKGE5pySOERA3KexszJ2tbOzKoDyvLMaY0fE998Podguo59wVBAsBA7OlFV24UEo7TJ6wuTKyu51dR_tFY7WIt8-rohZdS5ytXvGPf4elPhfHnAP3j7_QYsbNnfTEc4OWmACuHjcsa8nG8vc5mQSD75PVGPWyT9fmBb_GPD2Y29eYY_ZtQzs5cLmibNmaKdG--AfuimLyM4XuovFxcIkuZYaMkn4_Zw48Br0bJFR0a1yiSSzIlv0gDVZpmjGoshGArF9AAHKtU9tA5TUs8_d_3EXFjgYJ-Z4SdgU1PM8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آخرین مصاحبهٔ مولوی شهید یوسف گرگیج: راه شهدا با اقتدار ادامه دارد  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462167" target="_blank">📅 09:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462166">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ddab11d0.mp4?token=bMCTyu0wcz_Lf0rh52my0-I5IZp3Ur2nws3Z6Ee_xTP9NlhrM1cJhdI5ryqrL09QboDAVfc8x_DtEstOr93Wnr2LCONQDNwhoQZ_HEcEQqJOIH1l2rl_ifJVQ26i1QkHoAH5C1xmL3siZIhDsLwbM-CAp7Q_uo1hVrmFK3Pw0cWh84Ap8vu6SYtrx2kMbydSx-IumRrzERHsf0LPsPfZ33KLdZU-gZxwbXFpPwThfbxhji0bkGiy7O21iDwAPRPkcytw4a-YUcXsmHFXBIJECIIc6rFOgLKVYhWBbASgpNAFMii_EofnJrBCZgvmRaLMuKM99f8oYU57S_13cIbkBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ddab11d0.mp4?token=bMCTyu0wcz_Lf0rh52my0-I5IZp3Ur2nws3Z6Ee_xTP9NlhrM1cJhdI5ryqrL09QboDAVfc8x_DtEstOr93Wnr2LCONQDNwhoQZ_HEcEQqJOIH1l2rl_ifJVQ26i1QkHoAH5C1xmL3siZIhDsLwbM-CAp7Q_uo1hVrmFK3Pw0cWh84Ap8vu6SYtrx2kMbydSx-IumRrzERHsf0LPsPfZ33KLdZU-gZxwbXFpPwThfbxhji0bkGiy7O21iDwAPRPkcytw4a-YUcXsmHFXBIJECIIc6rFOgLKVYhWBbASgpNAFMii_EofnJrBCZgvmRaLMuKM99f8oYU57S_13cIbkBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارش‌های پراکنده‌ای در بخش‌هایی از کشور طی ساعت‌های آینده خواهیم داشت.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462166" target="_blank">📅 08:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462165">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
پزشکیان: رقم کالابرگ قطعاً افزایش خواهد یافت
🔹
حتماً در حوزهٔ بهداشت و درمان بازنشستگان و معیشت، تصمیمات سازنده‌ای گرفته خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/462165" target="_blank">📅 08:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462164">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNJEZfN8egFOe86zbc7Tt7qE5QQ3aF7ZiSdKT1efZ7ntbTQe5DO5q4wXEE-frvfxfOkIESc92LsZZaBpY41wEewjLk8axyaHvLnZISoyiz6u7rj8DB6C6Pn0ZrOHKPAWHF_ZCvMG3iAZHCsw3cpknwNYY8WUD1Y2abeTt2T0rGAuRn2KqwpLCimsmB0m1gi6Gtb0SWz29g0HT_4LyS7STwA0JOV7cUDLtTlHA66yH7_8Xq18DVOH2DDe9ymFB4QTg-ipEFP9NZ2PDTn92WalG6VxYry7aKm8iCocaog-5juehPQ_qe3K2oY4dnefDnvKROc6XDv-opGLSF0Gk5XU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده هوافضای سپاه: عظمت و شکوه بعثت در خیابان‌ها را با حفظ انسجام و اتحاد مقدس در همۀ ساحات حفظ نمایید
🔹
پیام سردار سید مجید موسوی در آستانۀ دویستمین شب بعثت ملت ایران: ملت غیور و شجاع ایران، امت ولایت‌مدار؛ درود و رحمت الهی نثار شما شایستگان که در عمل به تکلیف دینی و ملی خود، چون کوه‌ها استوار، چون رودها پر خروش و چون تکه‌های گداخته آهن پرحرارت، با حضوری معجزه گون، خستگی‌ناپذیر، حماسی و دشمن‌شکن دویستمین شب بعثت خود را در خیابان‌ها در خونخواهی امام شهید و امتثال امر ولی فقیه حفظ کرده‌اید.
🔹
قیام شبانۀ شما که در دفاع از هویت استقلال و موجودیت کشور تداوم یافته، جهانیان را متحیر نموده و نمایشی از تراز بالای عقلانیت ملی، ارزش‌های والای دینی و فرهنگ و تمدن برجسته ملی، چهره برتری از یک ملت با عظمت را در منظر و مرآی سایر ملل جهان قرار داده است.
🔹
امروز دشمنان متحیر و متعجب از این ایستادگی، عظمت شما را تصدیق و دوستان آزادگان جهان خرسند از این عزتمندی، امیدوار به پیروزی نهایی حق در برابر ظلم و استکبار گشته‌اند.
🔹
این حضور آگاهانه، پشوانه‌ای مطمئن و دلگرم‌کننده برای رزمندگان اسلام در همه سنگرهای دفاعی کشور و پیامی دلنشین برای پایمردی و تاب‌آوری سربازان جان بر کف شما ملت عزیز در نیروی هوافضای سپاه برای محافظت از کیان اسلامی ایران سربلند و خون‌خواهی امام شهیدمان می‌باشد.
🔹
ضمن آرزوی تحقق آخرین وعده آن امام سفر کرده، در چشیدن طعم پیروزی در کام ملت سرافراز، متواضعانه توصیه دارم که عظمت و شکوه این حضور را با حفظ انسجام و اتحاد مقدس در همه ساحات و پشتیبانی از تلاش خادمان خود در دولت مردمی و مقامات فعال در میدان سیاسی و رزمندگان اسلام با سرمشق قرار دادن تدابیر حکیمانه مقام معظم رهبری حضرت آیت الله سید مجتبی خامنه‌ای عزیز حفظ نمایید.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/462164" target="_blank">📅 08:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462163">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کلاهبردار ۱۷۱ میلیاردی بانکی قبل از فرار از کشور دستگیر شد
🔹
دادستان تهران: یکی از کارکنان حفاظت شبکه‌های بانکی که با نفوذ و دسترسی غیرمجاز، اقدام به کلاهبرداری اینترنتی و تحصیل ۱۷۱ میلیارد تومان از اموال بانک کرده و قصد خروج از مرزهای غربی کشور را داشت، با اقدام به‌موقع همکاران دادسرای ویژه رسیدگی به جرایم رایانه‌ای و ضابطان، دستگیر و تحت پیگرد قضایی قرار گرفت.
🔹
متهم پس از تفهیم اتهام، با قرار تأمین کیفری متناسب به زندان معرفی شد و بخش عمده‌ای از اموال تحصیلی نیز توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462163" target="_blank">📅 07:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462162">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2KuZ7SQiwE9KeQ9Q70b_ByFJpllmFVX3FZuNlOHpcK3OcZubDoBgc1vo6X3Qkkir5QU1N1X7MhuZi7hdW70QaFyu_5Yn7MLTpli5csDywxBoovHN6Q7KCLN3db6rbC0RjfBrbvcKRex_A4CQu1v-GbxqSgcVnpVdQTgR4OooBXXejkH-mswcfG87ERipIZ3zZZ_cxKm4lUqJUleIe9KcRvFOoeZp_O6ahUdv5iJmz3UqZ6JXTGXxWBJKZ2hVR0sMqhNm4MVDiomorCB1nhdUbCsdnOq1M_xQ1I5KyOyMsI2mTDXdisurm7NbU-KmM-QZu8LJ6BXYAal_RiVcRgiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: برای بازگشایی حضوری مدارس آماده‌ایم
🔸
برخی خانواده‌ها نسبت به حضوری بودن مدارس از مهر تردید دارند. اما حالا آموزش‌وپرورش اعلام کرد که برنامه‌ریزی‌ها برای بازگشایی مدارس انجام شده است.
🔹
در همین رابطه، وزیر آموزش‌وپرورش از رصد لحظه‌ای وضعیت استان‌ها و تعیین نماینده معین برای هر استان خبر داد و گفت، گزارش نهایی آمادگی استان‌ها برای آغاز سال تحصیلی در نشست مدیران کل استان‌ها بررسی خواهد شد تا مهر امسال با آرامش و آمادگی حداکثری آغاز شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462162" target="_blank">📅 07:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462161">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">درخواست کمک ریاض از لندن برای حمله به یمن
🔹
بعد از مخالفت آمریکا با حملۀ به یمن،‌ عربستان سعودی این‌بار از انگلیس خواست که در این کشور مداخله نظامی انجام دهد.
🔹
بلومبرگ به نقل از منابع مطلع گزارش داد که ریاض از لندن خواسته حملاتی را به نیروهای یمنی انجام دهد اما نخست‌وزیر انگلیس هنوز تصمیم نهایی را نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462161" target="_blank">📅 07:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462160">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هوای تهران امروز هم «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۶، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462160" target="_blank">📅 07:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462159">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اعتراف پنتاگون به خسارت سنگین حملات ایران به آمریکا
🔹
بازرس کل پنتاگون در نخستین گزارش رسمی دربارۀ جنگ علیه ایران، برای اولین ‌بار به خسارات سنگین حملات ایران اذعان کرد و گفت صدها ساختمان و سازۀ آمریکایی در منطقه آسیب دیده یا تخریب شده‌اند.
🔹
این گزارش بازۀ زمانی آغاز جنگ در ۲۸ فوریه تا ۳۰ ژوئن را بررسی کرده و همچنین کاهش شدید ذخایر برخی تسلیحات کلیدی آمریکا را مورد تأیید قرار داده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/462159" target="_blank">📅 07:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462157">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انهدام یک فروند پهپاد پیشرفتۀ MQ1 در تنگۀ هرمز
🔹
روابط عمومی سپاه: بامداد امروز یک فروند پهپاد پیشرفتۀ MQ1 در آسمان غرب تنگۀ هرمز رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462157" target="_blank">📅 06:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462156">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a53af483.mp4?token=ls2ywoIixfjjlGXzd81CHvKo1ScajTFSUBtSGNezXmoGf5aLLl251JuhngQy8qwX8J57KXKXNftctKgk0rtiz76Yk68Of-qQo0DJyHWIs5Zh50cZ6AzQ3vmNyDwCwxVCV53RuziYliYWx6Vs5jmGTxx4buEp8uA3XDDtYzvIdu4Vr4EO2fSnoJN79v_7DMM0RWI8NHuqbWy4QUiEImdjha5UHgsbvhS5sYIGzoSaLxgkH_BU_5UOdj-jQIuD865SAWnhBvUXma1sL_Vtj0fs_WBYgdAnJ5UaaGk2uywVchoF30kPGleWVbwifxYT35Ugt1bf0xXEfka-sa-e-iZh5i1jxuXPekM-qbCaiXKMAInRaPnal_fWDWHUgKhNP8O-Izt7mLD3hiGR4eefV570ZLkGocnD4T8GGtBAnglA0IVGLDOoWGqMY6Xy5A_M_OkX4Bd7cxGC3FUADeMTMfbRpXRT4l83XUBI-WeSdNij-k8XkHRr3EztXk4IzDL-bIrv-W4fiH0P-ZWmbhTS3SJXD3Y3oyJk6zGr9B854X4QZgIAeuT8vnpxFnnyAGb7dfoVz4pJVIVUugVTwszCul41WUIPTSf4RUUUPYwOHaLJ4VMNNynN5TEXGJsExLydlIkumqEVwhEPpKlHrxtUkZ5H89HRzhPAWnG_kzHifCI49iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a53af483.mp4?token=ls2ywoIixfjjlGXzd81CHvKo1ScajTFSUBtSGNezXmoGf5aLLl251JuhngQy8qwX8J57KXKXNftctKgk0rtiz76Yk68Of-qQo0DJyHWIs5Zh50cZ6AzQ3vmNyDwCwxVCV53RuziYliYWx6Vs5jmGTxx4buEp8uA3XDDtYzvIdu4Vr4EO2fSnoJN79v_7DMM0RWI8NHuqbWy4QUiEImdjha5UHgsbvhS5sYIGzoSaLxgkH_BU_5UOdj-jQIuD865SAWnhBvUXma1sL_Vtj0fs_WBYgdAnJ5UaaGk2uywVchoF30kPGleWVbwifxYT35Ugt1bf0xXEfka-sa-e-iZh5i1jxuXPekM-qbCaiXKMAInRaPnal_fWDWHUgKhNP8O-Izt7mLD3hiGR4eefV570ZLkGocnD4T8GGtBAnglA0IVGLDOoWGqMY6Xy5A_M_OkX4Bd7cxGC3FUADeMTMfbRpXRT4l83XUBI-WeSdNij-k8XkHRr3EztXk4IzDL-bIrv-W4fiH0P-ZWmbhTS3SJXD3Y3oyJk6zGr9B854X4QZgIAeuT8vnpxFnnyAGb7dfoVz4pJVIVUugVTwszCul41WUIPTSf4RUUUPYwOHaLJ4VMNNynN5TEXGJsExLydlIkumqEVwhEPpKlHrxtUkZ5H89HRzhPAWnG_kzHifCI49iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت سیدمحمود رضوی، تهیه‌کننده از توجه ویژۀ رهبر شهید انقلاب به دغدغه‌های فرهنگی هنرمندان
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462156" target="_blank">📅 06:39 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
