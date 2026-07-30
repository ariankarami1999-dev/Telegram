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
<img src="https://cdn4.telesco.pe/file/tbjgIm84FYLZ5ljdfck2Bf3By61ECFVMj1eR7UtGBLBlycInnDYd8SM0dRVfP07iCLeBYY7CjtCLSB6J3Sj9Fsbf5wEXLxZ5JANcibLvuXRzSsurapbPylad5_TiMrbl8YALRoy_TKmk2GOrQtVJTU7Q9A-AWXH-yqiNyfACR6XZ4atchqGO92CHouE3Q38Be8mkGC_FW8y2Ck0PlLJHgG0qLXpc1GQjI9FDDYH0niLMal5lPGqi-GbFw97eWE43i6GHRREULHL1XtWNmNaL3vvqN8WrTlcpjYj4SiS4cPv5WTASC43kWtyXngqjM6bHqwSTiCsMKpvpH-r5vHt-RA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 19:02:01</div>
<hr>

<div class="tg-post" id="msg-453603">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a375d5668f.mp4?token=oXcK8-2aBqSThaqK0oge3ViybQPYMNMNUpZEa15Nq8A-lIxQgRMJkRzn-hfHpP3JUMW87vHI0R6yV83YuA3s_gtP-wlSGOQFkbeT3K0HgdAdOOdxIDMoNqOfTJqy0Ezaajh97jFfAgv5sCe-2gDF7P4XZAHPoKmDglnQgMrBtteQCcILl9arZL2C7A-8A4yE7pHQC3tAHWo3_ItLXBDyZYZa1Rh3ZtCTNJNjBXOhEuXEoA-1hmphE0hLZrG6zfyDq0KfWm03IQWUqYwTMQAanaJKscLsOK_TA7YgXFUg0peI2Py5AhKEYfs9bkz8E6-vPKw20T-vyvPztwMcv9Mb0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a375d5668f.mp4?token=oXcK8-2aBqSThaqK0oge3ViybQPYMNMNUpZEa15Nq8A-lIxQgRMJkRzn-hfHpP3JUMW87vHI0R6yV83YuA3s_gtP-wlSGOQFkbeT3K0HgdAdOOdxIDMoNqOfTJqy0Ezaajh97jFfAgv5sCe-2gDF7P4XZAHPoKmDglnQgMrBtteQCcILl9arZL2C7A-8A4yE7pHQC3tAHWo3_ItLXBDyZYZa1Rh3ZtCTNJNjBXOhEuXEoA-1hmphE0hLZrG6zfyDq0KfWm03IQWUqYwTMQAanaJKscLsOK_TA7YgXFUg0peI2Py5AhKEYfs9bkz8E6-vPKw20T-vyvPztwMcv9Mb0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ آمار شهدای الحشدالشعبی به ۲۰ نفر رسید
🔹
الحشدالشعبی اعلام کرد: براساس اطلاعات اولیه، در حملهٔ تروریستی ائتلاف متجاوز آمریکا و عربستان سعودی دست‌کم ۲۰ مجاهد شهید و ۳۲ نفر زخمی شدند. @Farsna</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/453603" target="_blank">📅 18:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453602">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1WxK2UBKc79BFTm_Evu2IVEqY6syjCAEPRbBpAFcXrFD5i8aSz22IpoVJg8jgjzEKOmPYg0jJvj-1WAnIn7JiFmDCxB30PUCMm1dZzmESu67N_Fyxb_4ewtR9BlzWsOh0_kSg3BVGgmWkbdEvw5-HRVhCF6YaeVm5PF1A4pL9mBqXIeIPM9r9voqbmgLkMr18s2HAbZg7qL7LOOTXwlStHiLvqkhL3CCbQ8tLpA-LMIrL0c6Wcc7dIEKocbQMT3E7Yr2i123l_OCKA3Fo1_CFR1AV-pnBDbFIPkstL5-BDKIFqeEJ5vwgb4Jwu-jL8EmddTALy7buGUYPlvB82W7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایکس تمام صفحات خبرگزاری تسنیم را بست
🔹
پلتفرم ایکس (توییتر سابق) در اقدامی خصمانه و بدون هرگونه توضیح یا هشدار قبلی، تمام صفحات فارسی، انگلیسی، عربی و عبری خبرگزاری تسنیم را بست.
🔹
دی ماه سال گذشته هم دامنه com. تسنیم توسط دولت تروریست آمریکا از دسترس خارج شد. علاوه بر این، ایالات متحده از سال ۱۴۰۲ این خبرگزاری را در فهرست تحریم‌های خود قرار داده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/453602" target="_blank">📅 18:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453601">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804a06c2f5.mp4?token=XSRjIOFf7RWMuPsqPF1dAIR2cAG5A3OLBe8NkDifDChjirK_CDG8H8SW48DTLOikWmc1AUYArUQ_QLKyE7hfB8Rfs_XowrksKJEpaGOMsbIrcDAtCH9dX0kBVwg-ZXrF5xejJMSYcD8dV34tU2jwDABerXwxGV02h003n9IxcW27lJpaKs-0eV32PMHeK375qhwaRThkIXT3KY9rqyYbJwFFRvi8L10wNhOqVo4jEI7S4LH8X8JhgyH6jnUZw1dCn2gVNZhDWvpbkmMnFOFtHebEOl7r3-jhkxZMjg2UymPsCIqNmfFwvKbiH-lgTutjEGBAMmRDt8F3wOC5OclvHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804a06c2f5.mp4?token=XSRjIOFf7RWMuPsqPF1dAIR2cAG5A3OLBe8NkDifDChjirK_CDG8H8SW48DTLOikWmc1AUYArUQ_QLKyE7hfB8Rfs_XowrksKJEpaGOMsbIrcDAtCH9dX0kBVwg-ZXrF5xejJMSYcD8dV34tU2jwDABerXwxGV02h003n9IxcW27lJpaKs-0eV32PMHeK375qhwaRThkIXT3KY9rqyYbJwFFRvi8L10wNhOqVo4jEI7S4LH8X8JhgyH6jnUZw1dCn2gVNZhDWvpbkmMnFOFtHebEOl7r3-jhkxZMjg2UymPsCIqNmfFwvKbiH-lgTutjEGBAMmRDt8F3wOC5OclvHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الحوثی: رژیم سعودی برای حفاظت از رژیم صهیونیستی برخی پهپادها و موشک‌های شلیک‌شدۀ ما را رهگیری می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/453601" target="_blank">📅 18:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453600">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خبرهای تأیید نشده از حملات عربستان به صنعا
🔹
برخی منابع از شنیده شدن صدای چند انفجار در پایتخت یمن خبر داده و گفتند این انفجارها ناشی از حملات عربستان است.
🔹
هنوز منابع رسمی یمن، صحت این اخبار را تأیید نکرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/453600" target="_blank">📅 18:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453599">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
مسیر پیاده‌روی نجف به کربلا، ۵ روز مانده به اربعین
@Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/453599" target="_blank">📅 18:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453598">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c2e264da.mp4?token=m5XxadwX4-fOghXSHdGFklcaDgPpdXZDhmjf_v1DLhlTGrXicf9yQoXPJtYov85s_zw5_Bdthamzlly3umc8PAUEXlcOJ9yC1I7RfrPkXUtI_Diz1yA_nokHKjp_X2fD_a0fNVQH_pzAX3y8av_hEeM-nkdEQtvgZ8bQ6kFzuO5BuWESPEvJQBdPvDxLFeKlTB1ZIF4I09gHI-ylpBFV7_EZhi5voEBEjwd3-hj6wxjJGoyqpNQGBoPfDrAwimKz7lLflFpZSJ0nYH3VjpHIlxxdj8joPAmGC--E8REvFdf7ZrXSGNrD-63lW77WQ_WwarXm-5yM-NphYFY5m_eY5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c2e264da.mp4?token=m5XxadwX4-fOghXSHdGFklcaDgPpdXZDhmjf_v1DLhlTGrXicf9yQoXPJtYov85s_zw5_Bdthamzlly3umc8PAUEXlcOJ9yC1I7RfrPkXUtI_Diz1yA_nokHKjp_X2fD_a0fNVQH_pzAX3y8av_hEeM-nkdEQtvgZ8bQ6kFzuO5BuWESPEvJQBdPvDxLFeKlTB1ZIF4I09gHI-ylpBFV7_EZhi5voEBEjwd3-hj6wxjJGoyqpNQGBoPfDrAwimKz7lLflFpZSJ0nYH3VjpHIlxxdj8joPAmGC--E8REvFdf7ZrXSGNrD-63lW77WQ_WwarXm-5yM-NphYFY5m_eY5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انصارالله یمن: حتی چهارپایان و الاغ‌ها هم از دست رژیم سعودی در امان نیستند.  @Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/453598" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453597">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شهادت یک مامور در درگیری با سارقان مسلح شادگان
🔹
فرمانده انتظامی شادگان: در پی درگیری مسلحانه میان مأموران و سارقان در شهرستان شادگان، یکی از قاچاقچیان به‌طور ناگهانی به‌سمت ماموران پلیس تیراندازی کرد.
🔹
یکی از کارکنان پلیس در این اقدام ناجوانمردانه به شهادت رسید. اقدامات برای دستگیری ضارب آغاز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/453597" target="_blank">📅 17:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453595">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDLPBcAApJ5KVAosrmC7itTGsBVESqToYsX4f824G1svvYrFrh1xeWlZMdxTTdo6mDzIAhSkOnhNxXNDNA-f8HgF1Mo8xVHwNG5AlRRvJ9Rc4AB2VZiYRisMOub4Vioppifoq62dJ1APLvQ0Fq_WkvseKsJTbc8YibTVYDhpn6T2DCIgZDDhfxOBE4YhMs8KPtOUrhkMaZSBzDx_q4i3Cii2SubgTrsw4WRxjcX-gEIDX1w5hW8n2O7bxz2GvqVAnFEWhkj1ZoXx6wDkaakw1iZ3xrfFd10hbGYKlR7VpnuCA1Qxq1IR4D7DHsTGY5KUgYCq_WAWj4kxcS14mkx3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30beb59350.mp4?token=LZHNjsF-THH-wLdp6I-Hk7--IgPNPqNnCL4JOn253W97q33qiWTIMFMEpPSmFUusCsk8i2-fNG5BHR3XCfbVpH8Aphj16oihjvDT4CETg1UM-IJj5jdL0jUWEyzi_oHNMAuuc-sz-JTucN9n13JtKYLtJK3E_it-nSnYLbBjZf_7yW4a5Q7s4As8vLD8qCha6fp9aBpDWZsVWqQLnVAkQlcTOR0dFAsOOaaAKo1kB2qUGcYZli_ZIlb1iJADWnqE50V3goJsWRGFvrybwIw8id-so5PouoOfdJOlq7fzgvYUAmubaVuEcgIADrV5Wm5zPaIKLPYLA30eyBSk_rGc_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30beb59350.mp4?token=LZHNjsF-THH-wLdp6I-Hk7--IgPNPqNnCL4JOn253W97q33qiWTIMFMEpPSmFUusCsk8i2-fNG5BHR3XCfbVpH8Aphj16oihjvDT4CETg1UM-IJj5jdL0jUWEyzi_oHNMAuuc-sz-JTucN9n13JtKYLtJK3E_it-nSnYLbBjZf_7yW4a5Q7s4As8vLD8qCha6fp9aBpDWZsVWqQLnVAkQlcTOR0dFAsOOaaAKo1kB2qUGcYZli_ZIlb1iJADWnqE50V3goJsWRGFvrybwIw8id-so5PouoOfdJOlq7fzgvYUAmubaVuEcgIADrV5Wm5zPaIKLPYLA30eyBSk_rGc_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌بس اسرائیلی؛ زید ۱.۵ ساله در خواب سوخت
🔹
اسرائیل شب گذشته باز هم مرکز و جنوب نوار غزه را بمباران کرد و شمار دیگری از کودکان غزه را به خاک و خون کشید. یکی از قربانیان، «زید محمد نوفل» یک‌ونیم‌ساله بود که مادرش پیش‌تر سه فرزند دیگرش را از دست داده بود.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/453595" target="_blank">📅 17:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453594">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c33fc1d5.mp4?token=Zlli6HkSr6RqhYVQJ8S0JF3Q9Tb18Ru9MLuHT2vBKbaVOIj5gOU9hzUM6mXI4VfZMBfCoAjLw7PYT7WmQ_-D2cgPXDjQ2-WETlrsRj9Ud8xCktrvw0De94PPrgG8ZdGyfilhDNbyDdFFJfZSuFj5baoOHrk_j56vvN8Il__YJQXpGhjkz22TJ4lkyVDMp5euS3R-vWbYp2HT3PI8oiQroKoZb5GBrWmPOeu0W3TSQ3rctG3lgWV2P-BZ0HQzJ51rfQEX4bKYvEuN6bJRfOTFomf-xoQajEkiIBERVlfgGd7eW46K3xEtWKV5_dEMqGG3431g0b6AnZ2BtxdwHTgGPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c33fc1d5.mp4?token=Zlli6HkSr6RqhYVQJ8S0JF3Q9Tb18Ru9MLuHT2vBKbaVOIj5gOU9hzUM6mXI4VfZMBfCoAjLw7PYT7WmQ_-D2cgPXDjQ2-WETlrsRj9Ud8xCktrvw0De94PPrgG8ZdGyfilhDNbyDdFFJfZSuFj5baoOHrk_j56vvN8Il__YJQXpGhjkz22TJ4lkyVDMp5euS3R-vWbYp2HT3PI8oiQroKoZb5GBrWmPOeu0W3TSQ3rctG3lgWV2P-BZ0HQzJ51rfQEX4bKYvEuN6bJRfOTFomf-xoQajEkiIBERVlfgGd7eW46K3xEtWKV5_dEMqGG3431g0b6AnZ2BtxdwHTgGPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام قنبریان: خون‌خواهی رهبر شهید باعث خیرخواهی برای ملت است.
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/453594" target="_blank">📅 17:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453593">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04131030f2.mp4?token=mXe50RrOVwfvQffjNOmQUB3h7-vBhZyNdR2Qnbl1iqmWpcEpKz3ju7mtSZIZ8yEOd3VkgnG92YptBvCNHL47n2aRdArrisLZxk4lG0SBatMTHcOd4T_BwLz88Cpl8wAZm9ztVqLg2_0LgEoVa7AzYy98qo0XdfXXW4r6ypmEFw7LuGoKUQezgzifBQSRi5cxflni_3cyPIhOJMogrLgbNFNOb41S9AEy59dKExWA_x3M2b6gWj__EJS8sSOlDG3zcPZXSWdH_Nx8RSgS1EsLnCjQAWQ1_Xp0e21sRUovNg6STODSWgzGVYex7Q4862L1VTUnmlsv26TfwPFQJovb6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04131030f2.mp4?token=mXe50RrOVwfvQffjNOmQUB3h7-vBhZyNdR2Qnbl1iqmWpcEpKz3ju7mtSZIZ8yEOd3VkgnG92YptBvCNHL47n2aRdArrisLZxk4lG0SBatMTHcOd4T_BwLz88Cpl8wAZm9ztVqLg2_0LgEoVa7AzYy98qo0XdfXXW4r6ypmEFw7LuGoKUQezgzifBQSRi5cxflni_3cyPIhOJMogrLgbNFNOb41S9AEy59dKExWA_x3M2b6gWj__EJS8sSOlDG3zcPZXSWdH_Nx8RSgS1EsLnCjQAWQ1_Xp0e21sRUovNg6STODSWgzGVYex7Q4862L1VTUnmlsv26TfwPFQJovb6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انصارالله یمن: رژیم سعودی نقشۀ آمریکا، اسرائیل و انگلیس را پیاده می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/453593" target="_blank">📅 17:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453592">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca567ea645.mp4?token=ojNwWmWNxxVQjlBGEuVfboiMqfvBto-1xjDxF2oJf4ZxFxNzlJWChLiYm9EYAfB_Ve_HSnOLvV7cYkIPnIQnoBv9zkjA99dwfVPLvB08UnqjN4LjWtULXBiNxGCNQLt-OnvcBhYUjuhZugKUrGQ-SrS43HLCt40O78_uEtxl4yVcz4eZ9OjxLi1lpgbI6Us3N3iudxMLeVsjgzGCP0c-WvDnmBLQ2TQ4t-dLxEEGSFL2DFfCNk6BJViwVgotJ3ckjiNfW0zov9T6vOGywf4aIwr0WI5h9IBp-U6NXBveHywdq9eDBBnQoFBqoWX5dmjibqDBoEDDwMzJaAlmTP_YNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca567ea645.mp4?token=ojNwWmWNxxVQjlBGEuVfboiMqfvBto-1xjDxF2oJf4ZxFxNzlJWChLiYm9EYAfB_Ve_HSnOLvV7cYkIPnIQnoBv9zkjA99dwfVPLvB08UnqjN4LjWtULXBiNxGCNQLt-OnvcBhYUjuhZugKUrGQ-SrS43HLCt40O78_uEtxl4yVcz4eZ9OjxLi1lpgbI6Us3N3iudxMLeVsjgzGCP0c-WvDnmBLQ2TQ4t-dLxEEGSFL2DFfCNk6BJViwVgotJ3ckjiNfW0zov9T6vOGywf4aIwr0WI5h9IBp-U6NXBveHywdq9eDBBnQoFBqoWX5dmjibqDBoEDDwMzJaAlmTP_YNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد آسان زائران اربعین از مرز خسروی
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/453592" target="_blank">📅 17:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453591">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎥
رهبر انصارالله یمن: رژیم سعودی نقشۀ آمریکا، اسرائیل و انگلیس را پیاده می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/453591" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453590">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e642c32a43.mp4?token=iNAzJJfhBnfMQ71D9CTBJQT52C_K0K-CbnRY0pc9tKaVwVNBR8-ntlMfERkZ_VQ9mCXjdjI2KpyVvMd9SXSZ8GYuH7wr11tnePTdvxNGPWDprPn4DZiyRo7UIu_AdQyU1-Ry8TIcdk4ZRi_Q6Mk_x3c_-IVUxbGjaq1dWAw0DWmNyDb-vQVMil_YzYlA3EPe_aBDvweWKeQob7lPPDHEiuPQNvduLkIlfJKABLg-zwQe7Ko6zdPt942_BcK5GgMqO23OQf_TI50d87fdkc8evDn13DZjBvlb2bZjowfolkeKXaJO8RDj3rbHVfMx2wuSEpSe8Ffe8Ao9EvT2pcbbRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e642c32a43.mp4?token=iNAzJJfhBnfMQ71D9CTBJQT52C_K0K-CbnRY0pc9tKaVwVNBR8-ntlMfERkZ_VQ9mCXjdjI2KpyVvMd9SXSZ8GYuH7wr11tnePTdvxNGPWDprPn4DZiyRo7UIu_AdQyU1-Ry8TIcdk4ZRi_Q6Mk_x3c_-IVUxbGjaq1dWAw0DWmNyDb-vQVMil_YzYlA3EPe_aBDvweWKeQob7lPPDHEiuPQNvduLkIlfJKABLg-zwQe7Ko6zdPt942_BcK5GgMqO23OQf_TI50d87fdkc8evDn13DZjBvlb2bZjowfolkeKXaJO8RDj3rbHVfMx2wuSEpSe8Ffe8Ao9EvT2pcbbRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  رهبر انصارالله یمن: کشورهای سازشکار نیز از گزند طرح خاورمیانه بزرگ اسرائیل در امان نخواهند ماند  ‌
🔹
نگاه آمریکا و صهیونیست‌ها به کشورهایی که به آن‌ها وفادار هستند، تحقیرآمیز و بی‌اعتنا است و آن‌ها ابزاری هستند که دشمن زمانی که به آن‌ها نیاز نداشته باشد…</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/453590" target="_blank">📅 17:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453589">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
🔴
رهبر انصارالله یمن: نشانه‌های خطرناکی وجود دارد که دشمن صهیونیستی در حال آماده‌سازی یک عملیات تخریبی در بخش‌هایی از مسجد الاقصی است.  @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/453589" target="_blank">📅 16:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453588">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رهبر انصارالله: هدف اصلی دشمنان تغییر چهرۀ خاورمیانه و ایجاد اسرائیل بزرگ است
🔹
تجاوزات دشمنان علیه جمهوری اسلامی ایران، لبنان، فلسطین و تمام امت اسلامی در راستای از بین بردن موانع این طرح صهیونیستی در منطقه است.
🔹
دشمن آمریکایی به صراحت نشان داده است که دشمنی…</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/453588" target="_blank">📅 16:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453587">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1JGNiAEGVv0N10XuzJZ2oJ-yOpwfZpXnBZURRBcsuLQim__wFX94rBfz213Rco9iESyaSSORI-V0Z6GH1kOYKcspV0tpOnwCt3Qs_UOjv2WJPbHhHw5A34ibW3VOG_YNc2h-dtj5qwQ9YwExIyOYufZGBO41eKuZ5J5-xeao8ZmJuNhDKXKEwouDsEA763WWhXJThR6h_zlJYSfDIVJUJcYEWVxFBxm19e8ANS4sD-0mlT1z3kzNCmb_RowTE4lV_qiivY8keOxlWI-PWO5EIpfMTG3y0su6i5KfubN03Ujh0qauSysIZ7Zan3RDjXIBdPw0I_1namgqCAuwIwlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله: هدف اصلی دشمنان تغییر چهرۀ خاورمیانه و ایجاد اسرائیل بزرگ است
🔹
تجاوزات دشمنان علیه جمهوری اسلامی ایران، لبنان، فلسطین و تمام امت اسلامی در راستای از بین بردن موانع این طرح صهیونیستی در منطقه است.
🔹
دشمن آمریکایی به صراحت نشان داده است که دشمنی طمع‌کار است که از دوردست‌ها به منطقه ما آمده تا اشغال کند، بکشد، غارت کند، آزادی مردم امت ما را سلب کند و بر آنها مسلط شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/453587" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453586">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
یمن: به مصر حمله نکرده‌ایم؛ فقط عربستان را می‌زنیم
🔹
یک منبع مسئول در وزارت خارجۀ یمن: شایعات دربارۀ حمله به تأسیسات گازی توسط انصارالله در بندر دمیاط مصر را تکذیب می‌کنیم.
🔹
موضع یمن روشن، علنی و صریح است و فقط رژیم سعودی را به‌دلیل محاصره و تجاوز مستمر علیه مردم یمن هدف قرار می‌دهیم.
🔹
عربستان با طرح چنین ادعاهایی در تلاش است خود را از مخمصه نجات دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/453586" target="_blank">📅 16:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453579">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQV30QrppYQPCp8CUN3IMKUgj13p6H4MXeZOQRNnW1Cm_mtHhgLBnfwxOq5ExgkzNzVukH1zpyVg8ls3ja3kh3Xej6siEOcNBe9f7uhd7PaYRLisYf2Y7fHAjgPismgLBIaGM4SBkcWvcjwIH_XMB1VHTOJzORBjjANiUMUOIWaPtsET9v61T2sJ-UNIgDZvl1Didj_2DoZs9Xi-qUumQEOCi7gv9WFrV_jns0--OxUz6Aecf5mTl8ISd-u8RAUGyW08ZHWma9yoiHSfKBSsIrS4CuktyUI7N-tIi54mLUJnTGg-mtdz2KlHozyxJruoebvJN9kWq8XxYGJ72VwpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kMfiKJJPRoHSGLFqCpGkfeymZI6qjmbUtyp0vOrVs-_uT1TbzRrKMpAv0uIC0xWJgywQ4rjTnbYEvv_XWu_IfmyVAlgHo7rLGdqs8WrioPb8_BGl2l3_NLgKnJRHlBkJQEgMK2b0RfaAVfJYQA2Gh8VB1Oxjz-jJQsbuDqnMCbeVpCVKtIzYbYPkxcmEMEoQOP0AftzI4-5_godmN1tf2G4E7CkWLxgskMXG1ONFa6OVhKogO5HorBZEFhmRape7-5wjuwLFjEmBrHef6CwM0hR2ay382xDOm1VZGEG4wh1UT9Zs0Yd11Snkx2q3L4kIKMwv9Y0f5NbD-uew68sOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwjEkZHZX5lAxKDtm1MQHIa1Pc0bzoOFs8qkOWMkMyM_ketOEkqFH-eMwgJMKyf8-RTnrXS7LA7N2SMe89UxSJrvlhUty3WEErFiHtK2wlS_rZ1uf8bMdJE3x8pGLyRerQrxLZG3aoVBGdPNRwC3jMoqRnFD4pQo8cvB1K2xypX1K8nYYMNdxVTrh1o3bI013Nkufp32sbe4u9RFH8Btbmg_OqZonht1VfR66KStb7xOYcDBwnpiwfhRM2J_g1yFn_fG11gvygxCZEH1fuj05HjA7WZcEk7S0v9Z_rao9yrTdMTptdGNivjnnPxj6glzU34Diohv3bKFl0mcCm25tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ia0fekxoiG_cRaW-C5oBMZYqAD9ZL3wWA7K_SqoR31rYg7CQ4qkoFXALkxlqSrq5gLeKUMGGn62mFOtgc72bwFz-rzcIe7Lbij4a4gCsu7xHEUJTN41pcOvTBlY_WOI1OBr9aaCAtQQf9cK6_LUIv77VDBqXzrAiC865pRPjzoWtO8Vjj4OusggEUowePX5OilJZk27Ik1vO52rKJB2mtrdsdkDVPBDU2_1sI_x1QFtPS7Ajg5D0LFHbkHEsGYEtDstbgEmRguNDFZ38i4dYgEuSn6U9PnftJWSvtOG3KFWvGNbrbaKCg-i_KK8ohXynwBMjkFop2VDtxabc7qfl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MMbl-XTUqjDLk067PGaw6PNXM4a8-6TnhedNTs4Pqe09dPvcvBu8kuRqishw22T60l54zK11GEnyFjBBjfdG4CwD4o8G65QOjNYMokbUVF5IEof2J9fT6lynUWUNJK2ddbAjzuTo8VpcB40fHB1HgKgQQFEznXsScGxwqy2jT-vgvB2uUGtJoBUXK3B42ihOFmKt2xaAPQQ7iNXXL46okeBtGufelyZr01zCa-9gPgcpUXh_FvBeuim4YxAeTaNngEW4Kim1pIqXGKP1rheIbi_WfNGdaTsNY7md5pJqdDKwV7p7L4h1sTXkqckhk5YYbBLfk7XBY40xisa4vWkWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fo8-EF9Or7_zbUB02Dvmy42nGtjoY3uVce0uZ3ogxxpTq9SgWyjR4tTOtE3PGEz4kkgO6a5ZIGn58C0fsTDGE6ikwiEnVW9EX-MkV9N92r4LUFRjwKktPF9_GPrnVnX6eYI4e-FodWt1fVOL8ct2UgZa1jaKBRu0XzlBo3rWh9aoi_xXUn_IOWPBxvC9K7OxvJ4k_8tgBELKbHpvPyZkjjbYDQFv6LzYxN3CiMWHQbBDNy1p3wqX2CeVhliZeZ0zWn_K7kXGwB1AVWRw4UoOp9VyPd3dk6DJwTtsGo9e8GH7jrDeWY4qJ9iWlxdFTHyWaG-4cXhPSxXi6NEGAhm3KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2z6k7sEQpBQXM2OmT5KHMWruwQZzu-M9PGRAhkazQYKlyLQSCz2CGggHjovnPYF9itX0AukTs_e7OWcVaIKC9GFYONhO32Yyu4yLrnr25tN4rvAFLxTEAe-e0Ibke7mCMAAP-LneIcEERKjCj0KMaaDwuzBNpPT4CnlDSbrcLHwEO1-Gk8XlRNmg2fduFE6mfiheXWF2Z7E--_8AeJWh2WEq1stIM9zn31Jmn6Ip4LvkrG7gD-HLKW--MVVpQo-KxM1e03I--VmAQNDW1fphFLOmA3bgVB3rzcSqXt9wHt2eGlybMDYqpUWwrMkYtSjf1q9a7ZbdoWqvIDP11oR4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خدمت‌رسانی موکب‌های اربعین در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/453579" target="_blank">📅 16:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453578">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npeE04GFxafFOPe3KrvGT8KgUVl75ZmYXjCc143Z0bx9bHb-X6E3tY1qZiTmLU2DkYA7HcpY1MuKhE4Y3AFNXv1uYTm1hMlid9tJoSD-rnWtnCAFcl1mj_WgBCCOdsrWDjiwOmGOuTvBdvLQtlRp-lQtc6yG_B4Pe0wEfk5p37rt-Y-tq67jvC95ab5fhjx3Yn4wrKyvhnIu7cUH_G5ODUmqgzySWYYVGwbEppD45HeApVZQ1P-cI362kbNxmeI206cWLe74YYQkGDafkhsriTUVdbTcvXGYlslYCTnmwB6p4uIA3s5-7EtUsm9PVhOMoFkG7vceoCVooI3s-lJliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار عراقچی به وزیر خارجه بلغارستان
🔹
سیدعباس عراقچی امروز در پاسخ به تماس تلفنی ولیسلاوا پترووا، وزیر امور خارجه بلغارستان گفت: موافقت دولت بلغارستان با درخواست آمریکا برای استقرار هواپیماهای نظامی این کشور در پایگاه هوایی «بزمر» با هدف پشتیبانی از عملیات نظامی، از نظر ما محکوم، غیرقابل قبول و مغایر با روابط سنتی و دوستانه دو کشور است و مناسب است  دولت بلغارستان با فوریت در تصمیم اتخاذ شده تجدیدنظر کند.
🔹
وی افزود: جمهوری اسلامی ایران در دفاع از منافع و امنیت ملی خود در برابر هرگونه تعرض و اقدام خصمانه تردید نخواهد کرد و قطعاً هر طرفی که به هر نحوی در ارتکاب حمله نظامی علیه ایران مشارکت کند، باید مسئولیت تبعات آن را بپذیرد.
🔹
وزیر خارجه بلغارستان هم گفت: بلغارستان قصد مشارکت در جنگ را ندارد و بر حمایت از دیپلماسی و کاهش تنش در منطقه تاکید می‌کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/453578" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453577">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509315b70a.mp4?token=mIicuuYdzQayAj4p_-4x5CoGeFSHsgZpLpwPFK4eO3Ko0DrnaYFhHkWH6ix0kCuXgzwviYO4v3vaQFuHx0btWU4PEByKgeFYjoWgI3B-ZQ4s-yVNXi4w1bQxkhHOvLNsmA15c7BOKWFKkGtajEeZ2ao266aDp4YrgzyG4Eqtudi9nJYIpuzgmMDdpuzTSnOcjKdDaokZw3tcK2oA0nQgsi_GhjfBW7FZNLxt6j79OLC9pgn2x8fAWI6xoiQScUdy5BFEQ9b7YbQP1LOpt2yCRFx4feGEgmxeV2ANIiBmHhvwmqqT-4xxyUpw8mleQScEHOF305vC7pANHBKlRtzb4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509315b70a.mp4?token=mIicuuYdzQayAj4p_-4x5CoGeFSHsgZpLpwPFK4eO3Ko0DrnaYFhHkWH6ix0kCuXgzwviYO4v3vaQFuHx0btWU4PEByKgeFYjoWgI3B-ZQ4s-yVNXi4w1bQxkhHOvLNsmA15c7BOKWFKkGtajEeZ2ao266aDp4YrgzyG4Eqtudi9nJYIpuzgmMDdpuzTSnOcjKdDaokZw3tcK2oA0nQgsi_GhjfBW7FZNLxt6j79OLC9pgn2x8fAWI6xoiQScUdy5BFEQ9b7YbQP1LOpt2yCRFx4feGEgmxeV2ANIiBmHhvwmqqT-4xxyUpw8mleQScEHOF305vC7pANHBKlRtzb4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: بالگردهای نظامی در پایگاه آمریکایی علی السالم منهدم شدند
🔹
روابط عمومی سپاه پاسداران: مردم شریف و بزرگوار ایران، صد و پنجاه شب متوالی است که شما بدون وقفه تجمعات خود را در سراسر ایران اسلامی ادامه داده و انتقام خون امام شهید و اخراج متجاوزان آمریکایی…</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/453577" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453576">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2fNd3K-aWrPQWD6nqDuHP1_gQrEKvJqfl0rviRWsnERBypFEYjgVKzuQh6tPJBInx_dCZshIEhGZ7tNCIRSI05o6AShq8IgDXpdkxH1HLB2icGNls5Al0jvSp1l6gEFJnaIY6aaW2k9aTykR3MBwtm8ZPDjfLHodfJBGDaz6Qjun_EAAPJNeAHdegElz05P6W1hEYkbnuJZ6_QElNL6BQd3HOAqrL2gnkVVPGjs6XGM0XHZWilGG7EmC462v6ci498trxSwBwmKdHWrCKN3a5Rf6wMec3SyUlu2onPIQSyc7BqO_8mJAXYMbU3EefXtAKS9w2IAqINNWU0m1OmyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: بالگردهای نظامی در پایگاه آمریکایی علی السالم منهدم شدند
🔹
روابط عمومی سپاه پاسداران: مردم شریف و بزرگوار ایران، صد و پنجاه شب متوالی است که شما بدون وقفه تجمعات خود را در سراسر ایران اسلامی ادامه داده و انتقام خون امام شهید و اخراج متجاوزان آمریکایی…</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/453576" target="_blank">📅 16:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453575">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
سپاه: بالگردهای نظامی در پایگاه آمریکایی علی السالم منهدم شدند
🔹
روابط عمومی سپاه پاسداران: مردم شریف و بزرگوار ایران، صد و پنجاه شب متوالی است که شما بدون وقفه تجمعات خود را در سراسر ایران اسلامی ادامه داده و انتقام خون امام شهید و اخراج متجاوزان آمریکایی از منطقه را مطالبه می نمائید. همگام با شما، فرزندانتان در نیروی هوافضا و نیروی زمینی سپاه پاسداران انقلاب اسلامی در میدان، نبرد با دشمن متجاوز را با قدرت و شجاعت ادامه می دهند.
🔹
صبح امروز در ادامه عملیات نصر ۲ و تنبیه متجاوز با حمله به پایگاه هوایی آمریکا در علی السالم، دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی را به آتش کشیده و منهدم کردند.
🔹
مردم مسلمان کویت بدانند، تنبیه متجاوز تا پایان دادن به غارت ثروت‌ها و منابع ملی مسلمانان و اخراج اشغالگران و غارتگران آمریکایی از منطقه ادامه دارد.
و ما النصر الا من عندالله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/453575" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453574">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
قصه ۲ دختری که در یک عروج خانوادگی پرکشیدند و شهید شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/453574" target="_blank">📅 16:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453573">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71bf858467.mp4?token=AV2i2oLLdclbEDC3QQIGgMOebvMCZknxABvzCAsnATowqtPwmkSIFi8jfTo2gZpDSmju67oOCDO97otx6KMeWN8cRPpLPcYoWUinAuDB5ikeasRnsKgvjv9TLFCWkDggylcSvarMAADq0sIu4s7txJb0CJjbSa6PcKP4WCsMIX1rexPaqpmQonf_rmFxa4GvS_nWSmrXNNi0AAXjUBn1ex-6WE2lCzUJknt_Uk0WblwhbHSFIonXbMawfuvpNfAxLFZKK1QPXsINWDwB0ztVREcqy8CwBneSbUwl5WgE0rQ3z0Hkqpxg-1nKf3lWKO59tM8ntJhFnLSHdEfbvPA-bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71bf858467.mp4?token=AV2i2oLLdclbEDC3QQIGgMOebvMCZknxABvzCAsnATowqtPwmkSIFi8jfTo2gZpDSmju67oOCDO97otx6KMeWN8cRPpLPcYoWUinAuDB5ikeasRnsKgvjv9TLFCWkDggylcSvarMAADq0sIu4s7txJb0CJjbSa6PcKP4WCsMIX1rexPaqpmQonf_rmFxa4GvS_nWSmrXNNi0AAXjUBn1ex-6WE2lCzUJknt_Uk0WblwhbHSFIonXbMawfuvpNfAxLFZKK1QPXsINWDwB0ztVREcqy8CwBneSbUwl5WgE0rQ3z0Hkqpxg-1nKf3lWKO59tM8ntJhFnLSHdEfbvPA-bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/453573" target="_blank">📅 15:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453572">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_jWz0FSL3r8itk6rVrTxcq68vPyBmNhdOH9dIkqa1G2lEvaQs4I_O2yUR_-JVupAFmUUU8bAwVywIL5ItBO44kjoVniu9c9cb8RU7pXkfOdMRFfYs1OAaDJYs0SYy7B1dVbEg6fdPe8-iNtj0n2eEAVyfjs84Im7kDAv3p9Qbcbv4RlazPAK3Lyr-A_EjvHImOj1NGzyS_7jDPEBUZ-NTg92JYKluBcwE0KLRjZNv1_dqyA2elZCmT9rsPucivgIwFbS5m67D9jw21x8elnT8LSN5J8SWdFkPvTgCEeSTOyPodqYRghO7dKcQeBgfzHC3Kfk6sLGEGvKBx9pxcowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ خلبان سوخو ۲۴ ارتش چگونه پایگاه العدید آمریکا را به آتش کشیدند؟
🔹
۱۱ اسفند سال گذشته، ۲ فروند بمب‌افکن سوخو ۲۴ نیروی هوایی ارتش ایران، در پاسخ به حملات ارتش آمریکا و رژیم صهیونی، در عملیاتی از پایگاه هوایی شهید دوران شیراز برخاستند و پس از عبور از سد سامانه‌های…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453572" target="_blank">📅 15:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453571">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-text">🎥
ذوق‌زدگی سلطنت‌طلبان از حملات آمریکا علیه مردم جنوب
@Fars_plus</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453571" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453570">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تمدید مهلت ثبت‌نام آزمون‌های علوم پزشکی تا ۲۰ شهریور
🔹
وزارت بهداشت: با توجه به تعویق زمان برگزاری آزمون‌ها، مهلت ثبت‌نام آزمون‌های علوم پایه پزشکی و دندانپزشکی، پیش‌کارورزی و پایان دوره داروسازی تا ۲۰ شهریورماه تمدید شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453570" target="_blank">📅 15:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453569">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌
اسکان اضطراری ۲۰ خانوار آسیب‌دیده حملات دشمن در قشم
🔹
سازمان منطقۀ آزاد قشم: درپی حملۀ سحرگاه امروز به مناطق مسکونی، ۲۰ خانوار آسیب‌دیده از محله چاه‌تنگو در هتل‌آپارتمان‌های قشم اسکان اضطراری یافتند.
🔹
رسیدگی به وضعیت این خانواده‌ها تا بازگشت شرایط به حالت عادی ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/453569" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453568">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIRKUqVZCv1AVnblKe1WcZFOWp9jKXRMeS_DfXN-Zq_BURAYaWfOWS5Lh2BfRVOBHSz3Jc8_i1RlFAdTW59w3mqx09u7p2s2lzhzDYbrZDZv-uPRcf1pUj04kRnz1H9P4S4aUJ0oKz4W0ASvwilsFiVCsTr_8Yieh3UXykb5kNTV5B1ppaxjHOY_HM9rc5XNimzS4mJ1MZwY4-Cq1YXHVY4jplalrRlUi7_o13j_bJX19rVNuPb6wABMh9BO0Qii9_lWxLezym5z1xN0BjffxWRLg5AJoHICEt0U7b36El5R75ziY2nTcFbAMakoUDJ9Bvr-sq8kvjbfCzGhL9-Yzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت عراق به محکوم کردن تجاوزگری آمریکا و عربستان اکتفا کرد
🔹
شورای امنیت ملی عراق در نشستی اضطراری به ریاست فالح الزیدی بدون اعلام اقدامی عملی، صرفا به محکوم کردن تجاوز هوایی آمریکایی-سعودی به مقرهای الحشد الشعبی بسنده کرد.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/453568" target="_blank">📅 15:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453567">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66c62c7834.mp4?token=PgHUqQzICYsxzcZLmT1-kPv0VcSbGA7dqEvC0bKA4yLsKVSSNlq_ms1VXlzPHQGBBqPCrMBRd-xIXUqU96sRpm43rw7wQKNa0ZGMWRUPfFziKK-w1c8DIAtDt3DSJJAkrYN5fO68AKoWIb0U8oTV51PokVG7f4cmI5pgZPfyT510MhUCKbgO1JsTnpt2-eh1kGLIbazfj_1RlM9qqzQAFHNKM54uISk_Dfjho8VR2NRbWgCbHCPEQlCyQbBpBUKEI1CT9QrN0tUq7jtKDOhn37WjIPqTEZP_2DfxsJUQehffsV-8VXIURpZOjw2veGN1U2XYg3-Ab31t8baLyQ5bQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66c62c7834.mp4?token=PgHUqQzICYsxzcZLmT1-kPv0VcSbGA7dqEvC0bKA4yLsKVSSNlq_ms1VXlzPHQGBBqPCrMBRd-xIXUqU96sRpm43rw7wQKNa0ZGMWRUPfFziKK-w1c8DIAtDt3DSJJAkrYN5fO68AKoWIb0U8oTV51PokVG7f4cmI5pgZPfyT510MhUCKbgO1JsTnpt2-eh1kGLIbazfj_1RlM9qqzQAFHNKM54uISk_Dfjho8VR2NRbWgCbHCPEQlCyQbBpBUKEI1CT9QrN0tUq7jtKDOhn37WjIPqTEZP_2DfxsJUQehffsV-8VXIURpZOjw2veGN1U2XYg3-Ab31t8baLyQ5bQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: ۳ فروند F-35 آمریکا را منهدم کردیم
🔹
​روابط‌عمومی سپاه پاسداران: مردم شریف و فهیم اردن؛ همراهی و همکاری صمیمانه شما، به‌ویژه مواضع صریح گروه‌هایی از نخبگان اردن عرصه را بر دشمن تنگ و آن‌ها را مستأصل کرده است.
🔹
​سحرگاه امروز دشمن آمریکایی عاجزانه از…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/453567" target="_blank">📅 14:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453566">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انهدام پهپاد متخاصم در آسمان بندر امام‌خمینی(ره)
🔹
سپاه بندر امام خمینی(ره): بامداد امروز یک پهپاد متخاصم در آسمان شهر بندر امام خمینی(ره) رهگیری و منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/453566" target="_blank">📅 14:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453565">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac1b1dac4.mp4?token=etYT-edscnTBT6d9mAthail8WC_Yl9v7JsLdOaUnJ2T6UGH0_RLOZSnKXzYHFGJbFSwRAt1Z3QNOd0ecRwkup0J7jIxlEBvT3YJYfRk8eLWUnuijl2EjBcM4TeazxTNB9A7RFrwcy6eEwpWHhTxU8wVfaI9nQKzIlCImDaNfZOLVRCdn7VomutJcdyXrlqXp2AL4GKJNzSpGWH7PqAwrOSBG4PvaJUmU6__FZnHmwHuuBAZIRvjlEAZfHrMyEoImRqkKaX1P7MQln6nbbpsYNKZiFP6RPMMlBh2gdNHZwTkPuBHaYV7dLbWtHPHeX9Ge5aWqVkiL0baQZ6vtdBczDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac1b1dac4.mp4?token=etYT-edscnTBT6d9mAthail8WC_Yl9v7JsLdOaUnJ2T6UGH0_RLOZSnKXzYHFGJbFSwRAt1Z3QNOd0ecRwkup0J7jIxlEBvT3YJYfRk8eLWUnuijl2EjBcM4TeazxTNB9A7RFrwcy6eEwpWHhTxU8wVfaI9nQKzIlCImDaNfZOLVRCdn7VomutJcdyXrlqXp2AL4GKJNzSpGWH7PqAwrOSBG4PvaJUmU6__FZnHmwHuuBAZIRvjlEAZfHrMyEoImRqkKaX1P7MQln6nbbpsYNKZiFP6RPMMlBh2gdNHZwTkPuBHaYV7dLbWtHPHeX9Ge5aWqVkiL0baQZ6vtdBczDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم بدرقهٔ زوار حسینی در میدان آزادی تهران برگزار می‌شود
🔸
آیین بدرقه زائران اربعین، امروز با حضور خانواده‌های تهرانی به‌ویژه نوجوانان زائر از میدان آزادی تهران در قالب برنامهٔ «محرم شهر» برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/453565" target="_blank">📅 14:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453558">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJyWS2J4JdNwxXX3GuWvwafoJcu1DOJWJ8sqeIfr-tDevCfd3YybY5PMKkbIxRB9wqkzjKCGR_gISXBXMMgsVBhroPTyRjpND0bXFzp5pd3VVOdnwEMo4Ty4X3JJ08L9l1CyX5aKBIxWzPPu9Af3tKZZnU5hRltSkbjoC-c_XYaAfosDBKmPMm4e69OdrIm5X8FoPzKWAeu61Aq7Ht50GIXxK8-o5sKcu4pXVJ5JwYZKaePb0rpvPul6AtcXNEX99jBPmqrlD_VQr8Gj2eQQ-Lrrf3pLIqBC8yR-7EB8dlG-aocFGvAMy0YHy2AxNEEjf4egvdAoy7H8C3nF78CUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSKvJJ3w9M4x_CL7X3kdAvCIiQPW7jpW8j6iDF8ZI1NE6kf_NLCoIMyw9gVTMuIAlnfG2Grx_GjIjgOD59GgcK4Y-AzCJ1lZamsFPG8-NQHRq-xLgw4NOW6ZgNwZT61ySopvBjy104UcdOqa_FbwxCMwMjRK54SbnAm83Jj8WNxLDst7KU4-26TYhybswDcxOadZPQeaIuxj18LxIeAXM31w4yuA0I4QIn2fj5kdKuTyjk4L2gqe87_nR-h4T959-Fn2k0TABfrfyisyLXMsill39Y5ihS4jpQ2oa0uxwOa-UBiMB7b_BRGdoYoR7Q8dxB4GfDe0wqVTLu9sxoh-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6mRxtPLJs6XBfY7fBROrmxuixJhpOrD0d14t3IjZT3Zt75Vrscc_GahND_nn58PIfBP-vkQUUmyApPpGoLD7GgvD9WzTzFdgCQZAFLqUudmYffCEHqgAixfGWJa7tHwi-IM__pTYy6PlYpRgcwRZeNIRSpmstDNielcVmDISodTphJ3gVN7VzIN4S7Mx4blRV7St-FtycOAtc6IG2GGKZ7ytBmZ3NlVrAuD1GQ8yIUIPyfN4dY7VCTADZSUxRCHfzYsV59JrSjDbBU2P242KZ0l1RGak7YCuz1C0vwQAOw5ICobEohY5ruNM20eIFxNcnh1poh9uhwjBZYNGnJs7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLfOsOTRz0Q8s843kRl_DQaLvW7MEVg2fix0Yfkl2kq2SEae96xQTbqapwg7SfauC___M5ObZPMTjIA0KLtQSL1XtzEjM7vaTyInVFnOytl-fbV7izvT_4kNXMJoBJd96C1hY_0e1GBv8nQTYPIATn1VruhpWwc_xSkG7E80JqaPCwECaNLlwLyi366VA3Eg-Ljad2-_iYfi0j0OvIL26HJkOZd3yriKlyd6cyzW3DT83iXqLGVE9gu-d2aoGNDVkIFp8cj5Ece5vwhQADP9YC1kj3TyaH6_q0w2kgQP7ZUutz8YMA9Sd5O1yMnxzaS8Hyao3ccllV5HWXY_6sXMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/isuXbymHR68LOc8-ANqLiK7yL-3xkyhzUZQ6pgDF0-SmiienLtz4bXfG8JL38LyC-HKKvAt0nPCYpAG8V_zdFFKJymsE4A3n10FNSUhlwkTWIND_fZr6fvzYch9E9HmrpmEbgqV0j9qBzuwK2_G_TsY4ai5Z-oHCoG5A-oWGg5d9Dqrg9epEdKT41N_2IDiVyMIGxSmClrIS9TgtZXrDVmigYGTS3-WH0uyueQDMyqXy-lC9c1uQ4eNmTRGA4Xn9dEDbcnvqo-9ppzSLHn26ueOgnlXjTn4GP-2XCNkESl-961yMa22ezTQ0IIso1AM2m7zMc8TAKXx_qTdB3_qtBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfdLx9DSgFonfmiZOwVtzSSANmf08X6THfUo55A_hxc0MtpKkqaMVB7Rs6dfKRQxTKJ1OhYP0TMunOqou_3Oqt9yaNbU5V9voU3xtwCUXYRDcliUMVEZEbk54lLZW0ScIUqkW-x5N1IKgs6nU7_pArJDq-q-61RaVw44v2wWKdgp55A3fhH8S37LmK23jaq7iuloMBgTTwldaTXae5xPth8UflU4GUXebiu5MLAXwt48gbBClciaGlvB5LhNHot0AGZDXVFJJ5YqUZQrk1sibsU5Qos_qperT80ytLdzmD2ujaocAKE3HMwBmrXAim7lOSYkQti-J7sMfHIsSBp73A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUkuKbPI3SmDmze9ZzbmlqX-hr8xriXEAsg_jaJFkqf1OKHvo9Ql_xGcVID8GNkFrO7PWMe4xq5g0OZZkLbM8SqxbRhpCHOslGKd2NdIAFwYU9tk6GgcAXk_Di-eTx3wFNOX-BK-lMWyymsEx-5EP3sJSWYsOApFvNKM2_d9YLR7JLRTHFNyZzTte-fgDsPG7JCIimRnMeNLyf3waihH1MywEXjIxKp12WiQlHf9CxRKZhvEBIFLR9seJiFvdEjOaASzT867JFDw5khp-xZaPoj-gWHsUvMGJN0yTaHKwcxQyAWl26xv5AgyJKDq_l2vuh4UK1_g2rMWUicCXJ7RXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تردد زائران اربعین از مرز باشماق
عکس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453558" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453557">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
نقاطی در شهر اهواز هدف حملۀ موشکی دشمن آمریکایی قرار گرفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/453557" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453555">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FC7t8OzWMRY9_bwW6euV92a61BtM8vxNcXgwgVDlkoyAajfdrWAr5e-DY7vW83u26xWWRv47BFM7a46XRR7ouerZ7Gxz8XLYVCE3axzszL0pka8Rb-B4ZQPWR5cy6z0DukQqrN1-2w9w9k53Zcgd1icDa8gkiAHWTrRjimzzSCIJeKzPsz5KhyZw9ar7RAH1dbrKLb9j1_YODKb3id1A-2syXfpF1dkeCUL8u9E7x01I9-0oz6sNbZB3TpOzQUv5muPLolJ6lDCJt_QwA7MQBElzlpW4wr_TPcvlb9ciiz5PeH-gdF7wZXJFshQW3tSbAAYzVU_YNvOR7a6fzh85mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی ایرانی خط محاصرۀ آمریکا را شکست
🔹
کشتی کانتینری نورا از خط محاصرۀ آمریکا گذشت و وارد آب‌های آزاد شد؛ این کشتی پیش‌تر در نزدیکی قشم دیده شده بود.
🔸
دور دوم محاصرۀ آمریکا علیه ایران بیش از ۲ هفته است که آغاز شده و دشمن آمریکایی درپی اعمال فشار اقتصادی به ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/453555" target="_blank">📅 14:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453554">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY1XRqM1rGj9XpTTMvk1Ij4RzJsxk4ANt_8reqwm72fOse8W9l3ysKz2vnpBLsLQWoxR4sd8dLV2N2Ue75W4la8ABBs-UPICRGguppQlmrd-PCWWrN8JFVCUOskfRtpNqrKDWvRC1OFawJjRQivJsgnHDGhY5RQ80s0GqQYqnoz4mmui01embf-cpoCZGZrwMNCIg90rfX7OvwIQzZWHKH3j9N7OHDgnIZ-MElwFn1YoJ3dK7KS3zQzwUfvK18LvYnBs5VsajSmaWZim1KcdupuFDTRMs1Djw-Xjv0cENOpRtFj7PKxNVt-3191aqXdH-sgdKm345xkIFS0lxyHlpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه آمریکایی: سناریوی اسرائیل برای فروپاشی ایران شکست خورد
🔹
رسانه آمریکایی «ام‌اس‌نَو» در گزارشی از سفر بنیامین نتانیاهو به واشنگتن نوشت نخست‌وزیر رژیم صهیونیستی بدون دستیابی به راهبردی روشن درباره ایران، کاخ سفید را ترک کرد؛ در حالی که شکست پیش‌بینی‌های تل‌آویو درباره تغییر حاکمیت ایران بیش از گذشته آشکار شده است.
🔹
به نوشته این رسانه، نتانیاهو در شرایطی راهی واشنگتن شد که جنگی که آمریکا و اسرائیل علیه ایران آغاز کرده‌اند، با مخالفت روزافزون افکار عمومی آمریکا و پیچیده‌تر شدن شرایط میدانی روبه‌رو شده است. ام‌اس نَو تأکید می‌کند هر دو رهبر اکنون با پیامدهای جنگی مواجه‌اند که به گفته این گزارش، «از کنترل آن‌ها خارج شده است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453554" target="_blank">📅 14:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453553">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سپاه: ۳ فروند F-35 آمریکا را منهدم کردیم
🔹
​روابط‌عمومی سپاه پاسداران: مردم شریف و فهیم اردن؛ همراهی و همکاری صمیمانه شما، به‌ویژه مواضع صریح گروه‌هایی از نخبگان اردن عرصه را بر دشمن تنگ و آن‌ها را مستأصل کرده است.
🔹
​سحرگاه امروز دشمن آمریکایی عاجزانه از رویارویی جوانمردانه نظامی با استفاده از پایگاه‌های اشغالی در کشور شما و حمله هوایی به دو خانه مسکونی با بمب‌های سنگرشکن خود، ۲ خانهٔ ساده مردم محلی در جزیرهٔ قشم را هدف قرار داد که پدر، مادر و یک فرزند خانواده شهید و دو کودک دیگر مجروح شدند.
🔹
​در پاسخ به این جنایت و کمک به شما برای رهایی سرزمین اسلامی اردن از نکبت اشغالگران آمریکایی، صبح امروز رزمندگان نیروی هوافضای سپاه با حمله به رمپ استقرار و سوله تعمیراتی جنگنده‌های F-35 دشمن آمریکایی در پایگاه هوایی الازرق با چندین فروند موشک بالستیک، ۳ فروند هواپیمای F-35 را به‌کلی تخریب و به ۳ فروند دیگر خسارت سنگینی وارد کردند.
🔹
​در این حمله همچنین چند افسر و کادر فنی و تعمیراتی دشمن نیز به هلاکت رسیدند.
🔹
​منطقه ما جای ارتش کودک‌کشی که این‌گونه با قساوت خانواده‌های بی‌گناه را نیمه‌شب در خواب به خاک و خون می‌کشد، نیست.
🔹
مبارزهٔ ما و شما تا اخراج آخرین اشغالگر آمریکایی از سرزمین‌های اسلامی ادامه خواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453553" target="_blank">📅 14:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453552">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e636e78e72.mp4?token=dksrB2esUT8vjrCXFSE6pzSTDlKX7YOZYrgptjJgg_7POccnTmOvexwKU-0Y8Ljl-YmDSZSQrWHvZdptYMxK3MnCnvNDFUW6o5PROaf7zZIwnNph6_nPL6EM-oHNhvpw7Q6Zab1zfJd__SeUr8zGo4kw87tcyIHcFWXfJDeKXzLWCp6lbnSQ-O-DLLUvjctbp4pvXrZ6hXj8ml2rRNHPFk9IPwSakqDRy6N49gJBbs8IqWqhSHvcCDXpzVo7U-cjH2sW0mq9CyFK9cxBwuZJjHoQ4Z9I4Az1UhBHhKW0GQjG8dwyydmWonE0pDbTUATtnnpv_PoHTSnVpApVXtTdFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e636e78e72.mp4?token=dksrB2esUT8vjrCXFSE6pzSTDlKX7YOZYrgptjJgg_7POccnTmOvexwKU-0Y8Ljl-YmDSZSQrWHvZdptYMxK3MnCnvNDFUW6o5PROaf7zZIwnNph6_nPL6EM-oHNhvpw7Q6Zab1zfJd__SeUr8zGo4kw87tcyIHcFWXfJDeKXzLWCp6lbnSQ-O-DLLUvjctbp4pvXrZ6hXj8ml2rRNHPFk9IPwSakqDRy6N49gJBbs8IqWqhSHvcCDXpzVo7U-cjH2sW0mq9CyFK9cxBwuZJjHoQ4Z9I4Az1UhBHhKW0GQjG8dwyydmWonE0pDbTUATtnnpv_PoHTSnVpApVXtTdFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیۀ رهبر شهید انقلاب به زائران اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453552" target="_blank">📅 14:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453551">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">زلزله ۴.۵ ریشتری در امیریه استان سمنان
🔹
دقایقی قبل زمین‌لرزه‌ای به بزرگی ۴.۵ ریشتر در عمق ۸ کیلومتری امیریه در استان سمنان را لرزاند.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453551" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453550">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شهادت ۳ پاسدار مدافع وطن در استان زنجان
🔹
سپاه استان زنجان: در حمله وحشیانه ارتش تروریستی آمریکای جنایت‌کار در بامداد امروز، ۳ تن از پاسداران سرافراز زنجان به نام‌های «محمود ملاجباری»، «محمدرضا چراغی» و «جمال امیری» در دفاع از مرزوبوم ایران اسلامی و مردم انقلابی و شریف ایران اسلامی به فیض شهادت نائل آمدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453550" target="_blank">📅 13:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453549">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR4BoKKzGz-4KYHfbEMEzQOJbCSMZ8WIM5dRXPi0ByN_JIjsVC6If7ZLYYmhPc4q6CXT2AOI9eME7V0r9nBZm_pKgFBF1fDodDduqySwjagjI9mn9uvXgYAZNHcHA7SXiYyOYiwpfoidhnrK9El7VS_7h6YudTPtaROVj5CGPlELHRkfXQCOMMXuhghNMnX94V2fZHp3x3GAVLqed2KUSvGO6o0WNZzYdqc2KHlp5qo1Zxqov-bYyhWx_TkZmV_os8rMaL7FEwSoryz4oQVgRhXMcMcIuqXu-aF-o6lVcKWNVHqLZBXy-R9k9xq6lfQ1KKpU2VFx7wrw5kD_H5B9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان استقلال آبی‌پوش می‌ماند
🔹
وجود اخبار ضدونقیض پیرامون آینده کاپیتان استقلال، ادامه همکاری روزبه چشمی با آبی‌ها تقریباً به مراحل نهایی رسیده و اگر اتفاق خاصی رخ ندهد، تمدید قرارداد این بازیکن به‌زودی اعلام خواهد شد.
🔸
روزبه چشمی که قرار است برای یازدهمین…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/453549" target="_blank">📅 13:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453548">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw568qkqPSi2kOfGqR-aHiCC-OyuYC0UnVyZmUQ7abE9WO3pdKZVi3Mf3A9zvwZdy_Tc2DK6ml4x8TWW23o9xJAwjPCFt5KY2CQEAK1guDN9BaBUKKikF-0oJUOmfoacQ3hY3ZmjYmnKPq1RzwRxDzKlkcl_bcFzhgsjXJRIuSRSr8XjENF-7WZU3fSmxauNcVZ1bs1JolSANZIx-o9TAVNxB94GPqywXl-1FBaI9mO_IO7vVcrihvHKHxZUFP6a_7WWadRoOJF3h-wYs3FAguCCg56HWldfz0w5TDtjDEOWcMhfhAbiffqWLX1SnpBQNMCBMiD4Il764ss2C0sG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون فروش سایپا: پرداخت جریمۀ دیرکرد در اولویت ما نیست
🔹
معاون فروش و بازاریابی سایپا: اگر نقدینگی داشته باشیم اولویت ما تولید خودرو است و پس از آن جریمه‌های تأخیر را پرداخت می‌کنیم.
🔹
باید ۵ هزار میلیارد تومان جریمه به خریداران بدهیم؛ بنابراین با برخی بانک‌ها…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/453548" target="_blank">📅 13:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453547">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHszNYS8NJdQV1V2A0bBMoGA-oIusJk5h55Cr4YhZ5Vt5Bu3JeEUaFipomzZ8Z112LbFZJpwRAMzQPMB-uwwYT92sn87eb3EtdcHP0y0OJhv-nTWKQ_znDHQac25bbKmjl-EaBBhafR5ZzT__kZriHRD4QA-acW7PvjfNguz1H8PEKDdU3XsexNP2vjfqnRx8rNAAnrJATSpcG9XgB79rEkVdSr_z2mH39EFbY2t2Vvw2kmlEET751ZqqeL5-wy5w_L_NRr8dOnuUcwRKTCpX8SU8vCBc2jWpQRzkqMyPfmCte5nBkXpOO_q8XwUcAPUpUr9NAz9obL75y2FzuKZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت راننده آمبولانس در اسرائیل به اتهام جاسوسی
🔹
یک راننده آمبولانس اسرائیلی به اتهام جاسوسی و انجام مأموریت‌های جمع‌آوری اطلاعات برای ایران دستگیر شد.
🔹
به روایت روزنامه «یدیعوت آحارونوت»، این فرد ۳۴ ساله از دسترسی خود به بیمارستان‌ها برای جمع‌آوری اطلاعات و عکاسی از مکان‌های حساس استفاده کرد.
🔹
گفته می‌شود که او از یک «چهره ارشد اسرائیلی» که در حال بازدید از یک مرکز درمانی شمال اسرائیل بود، عکس گرفته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453547" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453540">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOYtVtGxOZNPYt7K3z7ei03N7c-A8THkcv8goMB6B6V0eYf35u5EGNWal_NGEsihWXzb21F8t3w-qgE2W6xI0oAtbr8S6oXGaOGG4VX_rxgIiSY63AH8jDgxzoaRmYf5dH4VGD9j1izvKbMeByWgROIJTXY12XQrlYE7JT8O4bhPQ4zqaDoI6tQoIz98Rhnnbm8IUtagK9kw0L0x2TcGvOc4dnpy24RX70gO2KAAba_sA3c8uivODkfA2qMuuoDErSdcI-ZbtAXeHSwZOJvWCTunJUEpO2cfeAG9PExSY4UXOgFPx2TzTyzH44pWnV2a-uyGvTXcAmJVxEXMZ7_XNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gaDWOqEs7tAGXNHCDGzwXckwRxlfYHBbEoItPNSC11qg7BgVMHqn3FjVTdRVuUSDYS83JOa9Jz3yYjGuOAN4uT1Ar4YaY5yVWub-jvRHoX-YH8-QHl-TWYDhRRp5oTWsPfclopzpGdmdJc4-AZPWBaq-e5nabHwrzaYD2KqM1bkPoDAVm-KWFzKslkYereG1y9EtVv6bHfghdSuJdyC1O0BdPOv-eRXRKq-PyZv7tak8Zd8Phe0z3m47jtSuLASrJuDkGNXm89fduh6cbA4P9-Mrjz6So5JFtNEdmixXNckQTuWxfW1v4qNPPIRraYvMS6QsYx-2UA3CfEMSdIW27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9AZ80yPoGLiEVmddmiOnc8jQaZ_uJOW-a14HLrOfUvBlvpDlGwn-YxOCV8VDRMJGduuCo762J5TnHIC-9VnE8R_FjWo-7HF6mCQqNPSXhXvQbFk5eeMQRTSxqt1LFGhAMuEF_PSN3n8GYixYVTSo3NQltTOXDkE3sjqTG4_NVqpr_53kFvQ6r4a2UJk2DUXaW3dvJngDtoxuiU3Bx3TdtzKBxizJvhBpevHGun_HV-o7o0feoQCSEe8q_zTiAGCE-tzf9VlHx3jWPHwp9527pNBoHH8W_zw2ezgIXjRomZxp9M-Qg5i8JycAceesBCdgEjd4aY-XIJq1crj8w8ZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCF87gZvBHseRjIcvNL_eFVIWWWzdISOhCisj1oKZbHpsaICQ95rWCFGQq83fGIgX9eEhiLPxjvBymIHjGxeSo9ANWpidlTpw2UfVGpz2RmfBg4Q4o0FqF-0DP-OS2sG-mVZol3pk6tmeBhUnBlZOgD_EwtPY_b1GKvSdBj_6Ks5grmaKoEKSlJywL2pENMoPAtZCSyqVveVtOAblTCFrmrZnBftFNEP2s82lQmJTBTqOToGoP9RHGS22sU81bsKYALbQd47-ZT4yg1dp1XWe2YrXlwB5lcKnQAeVDfD72MRlIzIzbuvJ79h_zag8cFmJu6PI4Dibt2VwsA3NnDUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nv7cv_HaMCbJXJJkg4xm8DL7yKB5wup_hyJxrBwx4AEIkx7kO9iR0g6wN1hSXQux4T5RCYJbzbr3b6yRG1F6UYpGHY2Fxbk8c0IuoffaKv-bEx9LsXaGxkkhQdRfzwm5wNTNVoPP5gUzLgWg8uRR6Ekl8vnsb4Huq351qrZkT9vEUnAC2ImXsTLUxbeIP86SHcDjQHT3NA2Zn7AODhpj1gcKN0hs_U3eN8lRxFxBMU-65_ClMdFlyFvh3WY3HbG_MqzWKEex0cUCVIs88ezpVws4aXfG5gFe7eUgDVmQGxyV9mdsAAG2khsMC3yeQ-DBuAyQ_CECXN-c8PPczDq2OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIGYCqB95yKjuf0QZEERLnZW6Q_WF1uS1VO7wRQtzky1w_CF8sCN1azFNBiYt_6ymfP4Gkfxi5C0uy7QfCEkB1FVaNg3nWrhtqJMBZL3CVVRKz4vuSy4YRWh0DYk_R7TsDLEiq4X6XMxXeRE7kv-sqzlgRS3mZp_O_tXHttklwZTBZ37GJmxayIBMXqz82o2MoeWOEQiby0uS5Kq3dm5hAMTfp2urs1j4cvW68-PKDQ0_i0bfV6dAKnFQ3mdpXYd0NeL_RUjxXnHrxLtzgxPFXTtYy6lrS-yy1lIDywMbJiipXprs1PnFVnkF1H-yMregsPyM97VTw28eYI09qQezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mYeyTXK5mrNbkynEqIpUsrkHq--jATAoGIEDADOmt3oEj4WIhMFX04usbYzk0FQ7Z9F4slTZT27ZZEqx7jb0JWWZ8_wEgNWoXEJBYPTxEC-Z7r7Aom845b4s2BRp2D5wdp-8zthdrkIcQvRLGRhTBxBpcF5Wbd2WALi1cVH02v-gaOMyKXfiSlGOByqEZ5urk7iPthVmL6xtjRtnKWb1eI7P6LYYKRiVqM3MXDx5jWNIVFDdu63v5QTa5NUNnnYuPdJtpvXNPaZu-YwGUKU4zar-BDNgKYtiZfCMKGbZAfSCgbNuisfIVYse0yeG3lcfnk0ZwFDn2nSqsJ5Uksk3LQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پارکینگ‌ مرز خسروی، ۵ روز مانده به اربعین
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/453540" target="_blank">📅 13:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453539">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY25T_C_SVu11LuGt2alUMWDv6EaeV70Jcm9Njdp24ehQmJHoTfpaRWU2N9Ue7LkMUP0Py77z-cY-aWACCmQxoStq5rbtUQuleRosW-QSMQfA6HPJZFkF0z1wnn_BVEWx_pxk9M8Ai8fjakY3gWJUb47yCFSh8o3wxRDrsfcyRX7hmsNV3ounB4d7mod8R-CY2ViHRT_KeH7DxhavkVpr1GC0NMMuWQDB4-fhbo9SEZgnNqFp-PRoaU--_KzK2L9kteMLHWdnKvXrEDdft027DlhuGU36fiGQrx3WwznkrE-OcPeeK8UhsB-VrRxW4YJ5Y0XfRd-GAGCfe5zmmtv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از دو فرمانده شهید سپاه پاسداران انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453539" target="_blank">📅 13:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453538">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh5tTN5WzHhQQcP-PkuPTrDd9skRXWzGacGZ699gMcUFg1sqGAKYaXNiFWSM4UcpwoAYDi-m8L0gVfnsDG3UI51R3zU7zzyXAOX72inzmtXUWL4Rtbj1Y32wf3faDpxfwyvTOuZyH7Uiqg5U1kBNfJB072FP0DnIg3kaU8CKEvM9phOBFPIOrDmR4ilghcg1m4f_13YUaJ0hm8_e7plF4iVHYUjbFPoPxz6Fb324GSuR9VlmCOC2vs89lg3JyJJxcsNFrvg906WYpkmdVRpxW7suTMc0mbs2_Hiax3EnaJzJ2AGjeeAF8R3UAtVUJWNhG5Ki-klbg9JwXgtPFzLDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماز جمعۀ تهران به امامت حجت‌الاسلام ابوترابی‌فرد اقامه می‌شود
🔹
نماز جمعه این هفتۀ تهران به امامت حجت‌الاسلام والمسلمین سیدمحمدحسن ابوترابی‌فرد در مصلای امام خمینی(ره) اقامه می‌شود.
🔹
طبق روال درهای مصلای امام خمینی(ره) ساعت ۱۰:۳۰ برای حضور نمازگزاران بازگشایی می‌شود و برنامه‌ها از ساعت ۱۱ آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453538" target="_blank">📅 13:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453537">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وزیر کار: پروندۀ پتروشیمی مهر و جم با اجرای رأی قضایی مختومه شد
🔹
پرونده ۱۵ ساله میان پتروشیمی مهر و جم پس از پیگیری‌های مستمر و با اجرای رأی قضایی مختومه شد.
🔹
کارگرانی که در پتروشیمی مهر مشغول به‌کار بودند از هفته آینده با پتروشیمی جم قرارداد خواهند بست…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/453537" target="_blank">📅 13:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453536">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس نوجوان‌</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c94f1c7eb.mp4?token=drj0YvbCw5ugySeOmmjBbMC-CEJHTdMdPGNOtPggogKsHwLrCxLC5edFi71OZClzH5yrIyd71jFTtXesu-a3okTq3E2sMEzG9AGhZ5qmtmBEfrxVHPwwSRokafrm2BxxxQK0D2ac0aTOi0BTVfHeStbTD173yFwVqosq0cRI1bv6X78munSGXdTWW7BGh1_5HMsveTccZyCBEAmry0mEqGe1ktHBdbN_Dm8HiLIGhjxzIYWP6D2sy-tgoN45T_GjHUyqwSFKJtW6GbITzxvLxb57qwboN-M-qf2FHtTIEEWz_asLIlMNcQsv7La236MBRj3y0o6hNJ2vDhpeyyY5RqQebFaH36s5hSOeQcVsoP7xjymUju_NYzPM1r0bnIdpMN_sDe9bidF7HzKPcat_14TGtfspCGEFHlB5LUNxGPC7TxpsX5zGjwTQVRS1hEyrCTPzxUz_KPKZRF_ZbMy5LUUPn6uilyT1fPerJ7EzA0B9gZOsfoabfr09E91KKKqx6m6RYKlXPtmSNAlgg8PX3tw3gOpDU9oX8nZbKAJk4bCF-PcteLKEfsQEpKWzfQr6VF-CNrabRmulI8Bs4uuLolHYqzekaZ4pnHMR1rNX1HQ0nr9542Vf2jIhQ6Yo9reAopC-rir64af0MevlRueL7Fip5KMxWq2-2takuid61RI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c94f1c7eb.mp4?token=drj0YvbCw5ugySeOmmjBbMC-CEJHTdMdPGNOtPggogKsHwLrCxLC5edFi71OZClzH5yrIyd71jFTtXesu-a3okTq3E2sMEzG9AGhZ5qmtmBEfrxVHPwwSRokafrm2BxxxQK0D2ac0aTOi0BTVfHeStbTD173yFwVqosq0cRI1bv6X78munSGXdTWW7BGh1_5HMsveTccZyCBEAmry0mEqGe1ktHBdbN_Dm8HiLIGhjxzIYWP6D2sy-tgoN45T_GjHUyqwSFKJtW6GbITzxvLxb57qwboN-M-qf2FHtTIEEWz_asLIlMNcQsv7La236MBRj3y0o6hNJ2vDhpeyyY5RqQebFaH36s5hSOeQcVsoP7xjymUju_NYzPM1r0bnIdpMN_sDe9bidF7HzKPcat_14TGtfspCGEFHlB5LUNxGPC7TxpsX5zGjwTQVRS1hEyrCTPzxUz_KPKZRF_ZbMy5LUUPn6uilyT1fPerJ7EzA0B9gZOsfoabfr09E91KKKqx6m6RYKlXPtmSNAlgg8PX3tw3gOpDU9oX8nZbKAJk4bCF-PcteLKEfsQEpKWzfQr6VF-CNrabRmulI8Bs4uuLolHYqzekaZ4pnHMR1rNX1HQ0nr9542Vf2jIhQ6Yo9reAopC-rir64af0MevlRueL7Fip5KMxWq2-2takuid61RI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لطفا با کفش وارد نشوید!
گاهی یک اشتباه کوچک می‌تواند تصویری اشتباه از یک فرهنگ بسازد؛ حتی اشتباهی به کوچکی یک جفت کفش.
در مسیر اربعین، شناخت همین جزئیات ساده می‌تواند فاصله‌ها را کمتر کند.
@Fars_Nojavan
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453536" target="_blank">📅 13:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453535">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPfQCImQVJZ8Ewcl47jKGfpNcrqnMltsj36hrZCpUXzp-yFIJYG031AfHBmxpmNK6GUXTiY9SNaeYLt_i4w1s-LHXB9nDkZ37WMNCy_hLMamxdOmlArzjvneS-Bq2PmvXNR2GrKhVxZTC6mQ_TAtj5y5Qh2rKW8JyfB-ovgnGvLC8AScIeKe30I6O7xDZRCghWSznWICsdkXBoYJHVEgp_4cWdqjfB5AXuKNNnUxRzaEKHykW50i3fLL9efTZBa-ayfGsH3WU6ge-xOz1LfwkjwXgItjaYGUiUreX6BnX8a5OW99BqSWh1rjtM8I7vMXwhoZKZCdBihYGcgHrkwIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کار: پروندۀ پتروشیمی مهر و جم با اجرای رأی قضایی مختومه شد
🔹
پرونده ۱۵ ساله میان پتروشیمی مهر و جم پس از پیگیری‌های مستمر و با اجرای رأی قضایی مختومه شد.
🔹
کارگرانی که در پتروشیمی مهر مشغول به‌کار بودند از هفته آینده با پتروشیمی جم قرارداد خواهند بست و در روند پرداخت مطالبات و حقوق آنها هیچ‌گونه وقفه‌ای ایجاد نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453535" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453534">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
وزارت بهداشت غزه: در اثر حملات رژیم صهیونسیتی در ۲۴ ساعت گذشته ۶ نفر شهید شده و ۳۴ مجروح به بیمارستان‌ها منتقل شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453534" target="_blank">📅 12:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453533">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f8e62266.mp4?token=Z0oqbgpdvgkt1iD6V1-lOega3E6dz-724wPaQM3cVaNrTMU2CDU25HmOe3y_OWCd14cFFP_XDiU0N_C2X_SLRFKm-m04vsOqqE-rXgkmcsHok2u8zFX0q1borVdbj19CIEeW8oep_K-BsWaSU36C4J340-xR7xMv-Mk1ZzNZss1Lw4vjJj4YDFzyhuUxPco2DLDpqhRPugvJU9yR2Jyo2ZStzNpKSmeHX9CIm5tnpYNrFcjfoJFIR-MOiljdh9VcbP_H31bTuq8UO3XrBPgesmdS06eMNXDYWqShDUo0D75q0dQtmDQe0fixj0jJeio_Q8chh10GcYLJHdExD73W3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f8e62266.mp4?token=Z0oqbgpdvgkt1iD6V1-lOega3E6dz-724wPaQM3cVaNrTMU2CDU25HmOe3y_OWCd14cFFP_XDiU0N_C2X_SLRFKm-m04vsOqqE-rXgkmcsHok2u8zFX0q1borVdbj19CIEeW8oep_K-BsWaSU36C4J340-xR7xMv-Mk1ZzNZss1Lw4vjJj4YDFzyhuUxPco2DLDpqhRPugvJU9yR2Jyo2ZStzNpKSmeHX9CIm5tnpYNrFcjfoJFIR-MOiljdh9VcbP_H31bTuq8UO3XrBPgesmdS06eMNXDYWqShDUo0D75q0dQtmDQe0fixj0jJeio_Q8chh10GcYLJHdExD73W3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر الان کربلا بودی، اولین کاری که می‌کردی چی بود؟
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453533" target="_blank">📅 12:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453532">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc200fd510.mp4?token=KcI95bPPeJhbrJIkbo9q1QQefigXAT-eYYKjXkIm6Z2WzxK-Ge3wll6GV9Js09b0isCQj_GytrAsOS6825WJnw6-KBbjw8PDgyicjkkGEYDHEeZLq6P__UbVT5vKaa_abiizREVBFHBM-KCwMxSnfOUvuH7KuxDGpu3vrNMsroNzoaoJjR_4GGBqDj-TJ0hQok4OYyq0iFxt6OUTOvUYaknmn1fgA6r2WVg42PeP8Q-rO7jhTyrOFgTpmw3gGK_qoKsvb3xAJpcEjZG6l0zYBW1I-rX7UTnr8Ruxpf-wWSvQAMA7JHhQ2m5lCV8MInoiYS04f8gvMYFN9uwWMzOT2hVEebqnbHsAOukWMDWGGTJNlMB3fAkA3MRcxVwARsM7JDxDASaUbujgDHW80JToNKCi1Kove6gkuSJlvIopsgqFa-QjD_-vGNvDeMDPfteNVXDDAG2c6IGKW6XDqHik5EukAT9FqjzZQH5FI2IzyQ_kej1HONuJ9QjZhu-040RCGwRl9tSgXdpR_ksgSjOd2o8R4DWP7KYrPLI7A_E5VXnbKn1PjXW4ViFNXmJBuMmE-jOoTOVTiV3JN9r09nb8OeBy-RBS6Kry7eko5s0tGfqfvYlFpy5AhqU7QfTWQt-xAtjpNusQS8pZkdVW4Xuv9qyywlRPiXjguFq10GkPAwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc200fd510.mp4?token=KcI95bPPeJhbrJIkbo9q1QQefigXAT-eYYKjXkIm6Z2WzxK-Ge3wll6GV9Js09b0isCQj_GytrAsOS6825WJnw6-KBbjw8PDgyicjkkGEYDHEeZLq6P__UbVT5vKaa_abiizREVBFHBM-KCwMxSnfOUvuH7KuxDGpu3vrNMsroNzoaoJjR_4GGBqDj-TJ0hQok4OYyq0iFxt6OUTOvUYaknmn1fgA6r2WVg42PeP8Q-rO7jhTyrOFgTpmw3gGK_qoKsvb3xAJpcEjZG6l0zYBW1I-rX7UTnr8Ruxpf-wWSvQAMA7JHhQ2m5lCV8MInoiYS04f8gvMYFN9uwWMzOT2hVEebqnbHsAOukWMDWGGTJNlMB3fAkA3MRcxVwARsM7JDxDASaUbujgDHW80JToNKCi1Kove6gkuSJlvIopsgqFa-QjD_-vGNvDeMDPfteNVXDDAG2c6IGKW6XDqHik5EukAT9FqjzZQH5FI2IzyQ_kej1HONuJ9QjZhu-040RCGwRl9tSgXdpR_ksgSjOd2o8R4DWP7KYrPLI7A_E5VXnbKn1PjXW4ViFNXmJBuMmE-jOoTOVTiV3JN9r09nb8OeBy-RBS6Kry7eko5s0tGfqfvYlFpy5AhqU7QfTWQt-xAtjpNusQS8pZkdVW4Xuv9qyywlRPiXjguFq10GkPAwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات بازداشت عامل انتشار لایو ضرب‌وجرح دختر جوان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453532" target="_blank">📅 12:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453531">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68ecf9958b.mp4?token=fnpcoYplsKZLHmSSxevCco8u4QKGkEGiMDzZOabWxU4Y5rfITFXYJLTPnqj6ohbbQ8hxKpzV-t22aSTIH0khwTXhyjHqTXwz--zSF3iE_X8pKdzfylKY8pxYrVi83rINZZIYUe0exN-7xLIsCZ6YZK1vOw_t8PNPqi4fKJjvjdTxAxfOHqMAapW-5YgmIO0ccQc8nySfhvNgUQ5l8EpeU3ueaAfI45pGY5u3XFdOaJ3Mrh4hTMAShEoUYzNT1Jr8qI0GbTw_1JXHBYfs1O59uLCZ1CK67KapYTcSmtpujQ93hxgSGRwQZZh-Frs9OZPXL_5arS69NeQnSSpmnkzrWiGJLt6_Qgd5uOIhztusbMbiSTEV_TBsZfp-PTrSSK7gBIjyyJCK-TvoMtJuDgPxVZL0o537hayZJzV7TUKjqVxdMOP3eldrkCjPmgJoxIRx-vyKsY-QPDizMk-YorEHmoYHbsG0MUrAMVYQNdJDj1Qcn9r3PHRmCzEsIhnkc5xFHYxYaZmBD1pMC37YyAdYJILE-pyo7DHMxMJmJeV9D26Qo7iuGd1jmla55fQp9jJJnITx4VE_O0vq9rrRLjIr41h7a73H1wfRCirssx0oIGkzTveOgQ6pclhwWZJ3TRVFLs-_Y2P2N0SIcV3z_sgmcbFzfSfBIb5aBBSl4EytoXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68ecf9958b.mp4?token=fnpcoYplsKZLHmSSxevCco8u4QKGkEGiMDzZOabWxU4Y5rfITFXYJLTPnqj6ohbbQ8hxKpzV-t22aSTIH0khwTXhyjHqTXwz--zSF3iE_X8pKdzfylKY8pxYrVi83rINZZIYUe0exN-7xLIsCZ6YZK1vOw_t8PNPqi4fKJjvjdTxAxfOHqMAapW-5YgmIO0ccQc8nySfhvNgUQ5l8EpeU3ueaAfI45pGY5u3XFdOaJ3Mrh4hTMAShEoUYzNT1Jr8qI0GbTw_1JXHBYfs1O59uLCZ1CK67KapYTcSmtpujQ93hxgSGRwQZZh-Frs9OZPXL_5arS69NeQnSSpmnkzrWiGJLt6_Qgd5uOIhztusbMbiSTEV_TBsZfp-PTrSSK7gBIjyyJCK-TvoMtJuDgPxVZL0o537hayZJzV7TUKjqVxdMOP3eldrkCjPmgJoxIRx-vyKsY-QPDizMk-YorEHmoYHbsG0MUrAMVYQNdJDj1Qcn9r3PHRmCzEsIhnkc5xFHYxYaZmBD1pMC37YyAdYJILE-pyo7DHMxMJmJeV9D26Qo7iuGd1jmla55fQp9jJJnITx4VE_O0vq9rrRLjIr41h7a73H1wfRCirssx0oIGkzTveOgQ6pclhwWZJ3TRVFLs-_Y2P2N0SIcV3z_sgmcbFzfSfBIb5aBBSl4EytoXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی نخ و سوزن، زبان عشق به امام حسین(ع) می‌شود
@Fasrna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453531" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453530">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در کمیجان
🔹
فرماندار شهرستان کمیجان استان مرکزی: در ساعات آینده احتمال شنیده‌شدن صدای انفجار در اثر امحای مهمات عمل نکرده به‌جا مانده از جنگ اخیر وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/453530" target="_blank">📅 12:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453529">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3s_Faz3sj1Fj_BGVLKNrYtTGZf1S4PNUtstSjkZ1Wp0YTyiWTxkY_Jl-QFJCtK4O55A8qxXIoWdXdVLr02Fps0desMUZe6PYal3BGmD1sBdJ6MnW8NTknVclUkAyotIFyU5Ng3rUsNc5c5P6PJ2ebncRrOT9Wf-7xt_N8jnYiBybdyqiSSHrd2meRSYWskkMjnpsxeqD5q83Mr6bQTNKXVAKW9sDZ5VewsFSt8Bl3o7JFVqA8faK2xhKgH6kPbDlCJmZ97aARYx6qv2kHFQgnpmO_cKyA8c4VgyUdSpe_rkwFkBWHk7REF29taAowqpMb-G4q2SdqU9uYmuWB7qbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزله ۴.۵ ریشتری در امیریه استان سمنان
🔹
دقایقی قبل زمین‌لرزه‌ای به بزرگی ۴.۵ ریشتر در عمق ۸ کیلومتری امیریه در استان سمنان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453529" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453528">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36dd50b50f.mp4?token=S4_Tq4N9XQnXVcpRg4fFgQKqXkjwJNNo1EJArMej2hpPb1X4ydDyCKFrABzT0UaxLMYI8s1lw7l7iD0hbwf3S4zovPRbx6wKlHuFdVh5n0jkmi_c7Pf4GcllhX6Vr51XUcfHxkmFszIvOiNi5GRzlWN9Qqp_aglsh_n1SKETI9dDaWjatc_oVNZ5fd_U6WJp7hSDIywP2vhSX8urNwtB06fNPQbR7t0LDWCkf2qanTfqXSF0g5nwWPf4VczLD5aYOmWPq_B8B1BRDQ6Zd39mUWd9POzQ5TnDPdt4hO_9Kd2rljolGYtO7K0wpLq_snRtvaPoqxaSc2W84IkwV5AAng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36dd50b50f.mp4?token=S4_Tq4N9XQnXVcpRg4fFgQKqXkjwJNNo1EJArMej2hpPb1X4ydDyCKFrABzT0UaxLMYI8s1lw7l7iD0hbwf3S4zovPRbx6wKlHuFdVh5n0jkmi_c7Pf4GcllhX6Vr51XUcfHxkmFszIvOiNi5GRzlWN9Qqp_aglsh_n1SKETI9dDaWjatc_oVNZ5fd_U6WJp7hSDIywP2vhSX8urNwtB06fNPQbR7t0LDWCkf2qanTfqXSF0g5nwWPf4VczLD5aYOmWPq_B8B1BRDQ6Zd39mUWd9POzQ5TnDPdt4hO_9Kd2rljolGYtO7K0wpLq_snRtvaPoqxaSc2W84IkwV5AAng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدیۀ فرمانده هوافضای سپاه به کودکی که خرج اربعینش را به رزمندگان بخشیده‌بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453528" target="_blank">📅 11:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453527">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXLgvbo4X4Lantjm_w49CCcALbDIW16JIx2Buo5P2YXFLQhb8rLaH2lhkN4hPebqM2XEQ1ncDMpF2NJbEL_ieFzufYXhSt5Pe_m5Iq2xs1PErdmthfo5T-Qst7tHiDMP1OhJaVdUi2ecV7nOdR0Ph2IXRJ5OEFqUFQy2kDeY6aAwhdHJNhcxVR2bm9qBKnN_U5_WqBlIUbkcJC51aBWMDxe9Bs0dmxsNQ9ntZLBOurgUNnyxvappV6eWb-t32vViOEst7-I5ksl-WF-yYxeXO6lmQInrKcya9TN7f6eR0cfoXtZpzmEET8pvI7v9eiEtsNZYuMWUuNZ6mTGHQuFTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق: تاکنون ۲.۸ میلیون زائر اربعین وارد کشور شده‌اند
🔹
ستاد مرکزی زیارت اربعین کشور عراق: تاکنون ۲.۸۸۷.۳۰۵ زائر از کشورهای مختلف برای زیارت اربعین وارد عراق شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453527" target="_blank">📅 11:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453526">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ed34a262.mp4?token=GVfwLjExTtwKvkTwzlhVWrQBSwY33vLhqI8K3jHDB0xtSvotDh1pfKiTFzNvffSAO8FULRc0AlZhbXLqVvgm0Ct_P8IggWueadKtWPkbYmKrIRlNaCLj31FCxHvTvv9hW9E13iaUEgxRpsTjAA4Mv1k81FCk1UddB6wPxfrcFwvaji42_isGsW5Ta8pLeJZejxiYh0lqmvSeytb2lRBDjyQb6Rk36dn7PAHa1h9Ux2UrJBbedZNll0vzaah-pGqWEDBY1QCpvCWvbKA3gAX-3gJihowKhaiGiRZu88QFhJOWGe0BFusFLQj6LZRNRpWTMlUDLVZXCoCB7bbcGwge40up2n8p2p38GswWAdaPhBGB7coaxa5NzFKLAHXIjP3YoPM-grivfmQwf58z9C_DPyp16QHWTv2tchjeymBC5X4jgLR_DdK14ts07lHJ-NYVVtI7hnSJcPYQrzPLV4KKeCXbJoe2zTCjGKiGqDQgtHTDOMjptYdHkMqmBoeUTTwIqjLY3u-7wkCAjKMB9EHN7uHnjiUuvr06tdqsKdF8udeo85rUcM6jC2DTEoQtOtVnF_WjJ0Z1fskixbUpmgb6YiozQOPqd2DCh1YuY4Mt5k9ZxMlEu9-3ZQ1wQfhYyJU5HzalmVXjE-hz9lyFdnUBI8QFaAAIfq8M2pYgx1Mbwns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ed34a262.mp4?token=GVfwLjExTtwKvkTwzlhVWrQBSwY33vLhqI8K3jHDB0xtSvotDh1pfKiTFzNvffSAO8FULRc0AlZhbXLqVvgm0Ct_P8IggWueadKtWPkbYmKrIRlNaCLj31FCxHvTvv9hW9E13iaUEgxRpsTjAA4Mv1k81FCk1UddB6wPxfrcFwvaji42_isGsW5Ta8pLeJZejxiYh0lqmvSeytb2lRBDjyQb6Rk36dn7PAHa1h9Ux2UrJBbedZNll0vzaah-pGqWEDBY1QCpvCWvbKA3gAX-3gJihowKhaiGiRZu88QFhJOWGe0BFusFLQj6LZRNRpWTMlUDLVZXCoCB7bbcGwge40up2n8p2p38GswWAdaPhBGB7coaxa5NzFKLAHXIjP3YoPM-grivfmQwf58z9C_DPyp16QHWTv2tchjeymBC5X4jgLR_DdK14ts07lHJ-NYVVtI7hnSJcPYQrzPLV4KKeCXbJoe2zTCjGKiGqDQgtHTDOMjptYdHkMqmBoeUTTwIqjLY3u-7wkCAjKMB9EHN7uHnjiUuvr06tdqsKdF8udeo85rUcM6jC2DTEoQtOtVnF_WjJ0Z1fskixbUpmgb6YiozQOPqd2DCh1YuY4Mt5k9ZxMlEu9-3ZQ1wQfhYyJU5HzalmVXjE-hz9lyFdnUBI8QFaAAIfq8M2pYgx1Mbwns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرقۀ باشکوه شهید خلبان سرتیپ‌دوم مجید کاظمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453526" target="_blank">📅 11:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453525">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d83d01baf.mp4?token=QlSKKEEzCx8gT8o_eRvXIcp4OCeLmOmFZSJkICjQ3GuZpFMZN6q945D5I6acf8lbsGDQ3zPqSrVKrHhG72dkUsNs9_-9q25YyX3RQKZK15BVM-KqJBt34q8_i8D5Ni75Iej_wYlMoC9lXj4bP9O-I0ukNtq0GU5claHAduv0ibkCaXNHbEcxNJdqvYRPoV7L7EkoBVXe9RfglZgsnoFP1cxkn46c6h1PQmF3Ch3avNoYW8qHyxOcmaJ_g-I1Brko4uB7shA46Zw_SPJIKqx74rzA8ZWNayTOPvMP4qHoBDBhH3lxe0HMkKhS4ZpvxYkr4AiEFxWqiruLCe-yUq2dlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d83d01baf.mp4?token=QlSKKEEzCx8gT8o_eRvXIcp4OCeLmOmFZSJkICjQ3GuZpFMZN6q945D5I6acf8lbsGDQ3zPqSrVKrHhG72dkUsNs9_-9q25YyX3RQKZK15BVM-KqJBt34q8_i8D5Ni75Iej_wYlMoC9lXj4bP9O-I0ukNtq0GU5claHAduv0ibkCaXNHbEcxNJdqvYRPoV7L7EkoBVXe9RfglZgsnoFP1cxkn46c6h1PQmF3Ch3avNoYW8qHyxOcmaJ_g-I1Brko4uB7shA46Zw_SPJIKqx74rzA8ZWNayTOPvMP4qHoBDBhH3lxe0HMkKhS4ZpvxYkr4AiEFxWqiruLCe-yUq2dlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد امروز ۲ نقطه در استان فارس مورد حمله آمریکا قرار گرفت
🔹
استانداری فارس: بامداد امروز دو نقطه در شهرستان‌های کازرون و فراشبند هدف اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که این حملات هیچ‌گونه تلفات جانی درپی نداشت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453525" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453524">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
روابط‌عمومی سپاه پاسداران: با استعانت از خدای متعال، متجاوز همین امروز تنبیه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/453524" target="_blank">📅 10:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453523">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
کویت از حمله به شمال این کشور خبر داد
🔹
ارتش کویت اعلام کرد درپی حمله به منطقه‌ای در شمال این کشور، یک نفر کشته شده و خسارات سنگینی به محل اصابت وارد شده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/453523" target="_blank">📅 10:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453522">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLsTcV54FoGy8OmBIBGdPjnz9nc8w5S3U5Xv9yMemdY30JTdGBPJgw4ImmkxIxdrBHXSmmHBDyJN2hLg_VCvRcgJdW1FGYUwYWTTLJSYmYRX2qWlaP141-rOc-d9-wrk7So_kwvA7HFWJVwsLHuEtdIgxzT4JVLTXvWj4K3wA6Fh_9SP1408tpOiDh6jV5i0bhpwEMzDfHw3TKLf03HARJSzTj1AbmOASiQNH17g2Kx6rwD2m9qnhWLtwvEgRh5VxHL0Xi9kp7cD57ojzyBpP2rFkqatGsAlYmWPr5-NJbZpNAkKgkZCcTuUZSo-CdE3R-OW668A7hj7RqoqdMd0jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یکی دیگر از مأموران فراجا در ایرانشهر
🔹
پلیس سیستان‌وبلوچستان: ساعتی قبل سرنشینان مسلح سه خودرو سواری به سمت مأموران انتظامی در شهرستان ایرانشهر تیراندازی کردند که متأسفانه گروهبان‌یکم میثم کرمی در این حادثه به شهادت رسید.
🔹
اشرار مسلح تحت تعقیب پلیس…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/453522" target="_blank">📅 10:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453521">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دقایقی قبل، زمین لرزه‌ای به بزرگی ۳.۴ ریشتر لالی در استان خوزستان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453521" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453520">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">محدودیت‌های ترافیکی فردا در جاده کرج_چالوس
🔹
راهداری استان البرز:  تردد انواع وسایل نقلیه از ساعت ١٤ روز جمعه از آزادراه تهران - شمال به سمت مازندران ممنوع می‌شود.
🔹
همچنین فردا از ساعت ١٥ تردد از ابتدای پل زنگوله به سمت چالوس ممنوع خواهد شد.
🔹
تردد از مرزن آباد به سمت کرج و تهران نیز از ساعت ١٦ فردا به صورت یک طرفه خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453520" target="_blank">📅 10:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453519">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOn7qPkUHoOR8j55VIojOFgnMWloRe1hGtTW71YlFOmJHQx9yf4w69wXtERNbx_V1Nek5QsJ7R_kmaEL9Uz8MM7Z_Ewfqp1d7e3IMhgkMW9GP2PA--L8wb85qxyphBWOsX-6224PLWFwuTLtU4FfukL6cgV0CdZjzoaAxOIDBaFg2IMD_vkvUzDujIwUN4Jr4jd-JndzZIAGuXAukp0WcflIYcrlGjTaRp7ZLeU1wPwaLRP9Sh-B0CHNULatLhK6GpsWpo7BvZ6wIUhXyMpqdzNuuEWpKVxXo_FDxjvnOIsiPHvDDvWKjS5xyaGKI1WuZoDg9bYdI1Ug9yn84Nqp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوبیتکس سرمایۀ ایرانی‌ها را به شرکت اپل برد
🔹
در حالی که آمریکا نوبیتکس را تحریم کرده، این صرافی امکان سرمایه‌گذاری کاربران ایرانی در سهام شرکت اپل را از طریق رمزارز فراهم کرده است.
🔹
یک شرکت آمریکایی مستقر در نیویورک که تخصص آن ردیابی رمزارز است خروج سرمایه ایران از طریق رمزارزها را بیش از ۴ میلیارد دلار اعلام کرده است.
🔸
وزارت خزانه‌داری آمریکا تاکنون چندین بار از طریق همکاری با شرکت‌های ارائه‌دهنده رمزارز، کیف پول‌های ایرانی را شناسایی و مسدود کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/453519" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453516">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJqxheC0pPAIOv5cPzF744kGCnBtKmV-Jq_EPNmU_ezhiFdik0ogGcJNwv-Rb6kDftpCU2OTqmVVvSPVviJioOp0rfnZLGuSYv0zlKEGoDfc6Zfo9OY_gJX3muzaCFaDYn4i51BGaBeVHfrJYRbB9klZpW9ikxuPruALXAxwylvgx8CHrmtXpG36HMuqAmLjzA2A99F1hSwywJ67oBYCjYH9lYn-EzfsFSgH-9_BLX0BXBOJI0aK1mQi1O9E5a5LsJeQIIl0kxY_NLle2wT-c7bj39MtdvQsp5xq1NDuItTd0Ma2yx4a9Yas6LAnVfcfdq3w0ndeGJEO1jvnaE3ZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHj15x9Co-xX_7jPF_f7h9X-AvrGXJS1TJksb1iBdFLu9j_SaVVxbGEJRRkTGyjXzFtMUyvA3HLfSmc5hur2zEobLwAR_zQhcEYJXu9RDDzh2wL9xVGJT34SG686rpF5jcty67--9L_kAO6PsOsF2DYhc-rQ5VmAgDoS5EEYVyNE78kaVdZSiMMZPSZFBXbHkSHLWgqh0pnNaWxIiyAN3GMv3Q5qFL_Rha5P-Ig8iH7BM9vHBBadWSVdtaWkxL125o1EvA3QwYRnHDGjEbWAWy-pM_6fAxdQCJFf3mcrJDv3yRJFnbNBxfkvEs8KvKvw1zZlQKWZP42SCpF7MRwNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L33gakBKhWmx2V7s6NKx63bDmfU5xzGJD-iOVNCRyNeOrAqSbccq-_iJeyYlmYhTZdkn-eTRCArPqhUbt966cjgstrcJBKeZSGsmmkHcezS3CEcv4g_VZKuk8bloXEsobg4PLFA1RUSVEgFMmck4v4mQuHmxM9D5F9ZT0gLIaxWJxHwFtj9aCnUcjTmFmKx3A6HAcmA9_WHwESoT_vYcF69yNlQNihNUNG0Y_-Za3eYPQu-EK4K3CRMVGXDMoApe9gnwU506oHjsJermPIQDfnj0UrafhU-rSkPR0TBK8SX4YmF4hKrq1GiqFywJqkhRvaltbhn42ZodG9VEKufVGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هوایی از پارکینگ مرزی مهران
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453516" target="_blank">📅 10:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453513">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8JMe1xWolhxTWsiigAX34WARMg2oIAOesRKgrY1HQOQW5Jyn3VCIzAh3KGqjeGJOY5LO19Do4hsIJ-NEaHCaoKrI8TUS7SYdGk62mMP7jHmBb23BNSm0tjvkgxrhSy6vZ378EWzOpo7R95yrIe33dJ8qc6rE7XiYb-UIqN6IT47DR0auR2Jh1FjxIgIt_6FDKq3-HuifynL1IlRBuHr_-D1BZjF4wc_HS8cQiLi5j4yDnMeQz427T5deXaDCBvq1fHiiee_uUbjWowSQwtUKYX49tXZgkRQjruYKwPcNXjzvhOB-hJTG8En13KH5mnrCYfEKo1Kb5upATTrtJdi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات برگزاری پیاده‌روی جاماندگان اربعین در تهران
🔹
معاون فرهنگی سپاه تهران: پیاده‌روی جاماندگان اربعین امسال ساعت ۶ صبح روز اربعین از میدان آئینی امام حسین(ع) آغاز شده و تا حرم حضرت عبدالعظیم حسنی(ع) ادامه خواهد یافت.
🔹
«اجتماع بزرگ خون‌خواهی رهبر شهید» در ابتدای مسیر برگزار می‌شود و با توجه به اینکه اربعین امسال را در امتداد تشییع قائد شهید امت می‌دانیم، شعار مراسم «باید برخاست؛ یا لثارات الحسین» انتخاب شده است.
عکس: بهار قادری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453513" target="_blank">📅 09:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453512">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b892f32cf.mp4?token=fV9ixEdOQ0PAOfm0b9q5eO2rcab8iTDrvbUnfT1NFC7GXkMqfvHDr6VZ80NmR9KU78mgjqk5CJBYch9KfWd86Uk_9OXEP0P6IhHau58ybUqTmr93L5WUlC5VFSGsq-vynNRnHCQ040rbkgm-5tct_wuOpqDP2hmrtf0BZQsBI0Ml5XZ7wzeCZvCuT6E2_44QEtPFlZrljzta6DkEuP0T4t3tnhoxmoaEsdY7gouj0VvNpZUVZXjsrvKH0xjExbnLuuiNL5zQt3WDSYrnUk68kJtL9MtF8NyIADvhR2VMVZf8BI2C0lF4MBkeUHZ-Hlv7FC-llZCyS7q58Vx2BOPkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b892f32cf.mp4?token=fV9ixEdOQ0PAOfm0b9q5eO2rcab8iTDrvbUnfT1NFC7GXkMqfvHDr6VZ80NmR9KU78mgjqk5CJBYch9KfWd86Uk_9OXEP0P6IhHau58ybUqTmr93L5WUlC5VFSGsq-vynNRnHCQ040rbkgm-5tct_wuOpqDP2hmrtf0BZQsBI0Ml5XZ7wzeCZvCuT6E2_44QEtPFlZrljzta6DkEuP0T4t3tnhoxmoaEsdY7gouj0VvNpZUVZXjsrvKH0xjExbnLuuiNL5zQt3WDSYrnUk68kJtL9MtF8NyIADvhR2VMVZf8BI2C0lF4MBkeUHZ-Hlv7FC-llZCyS7q58Vx2BOPkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس مسائل بین‌الملل: زدن مراکز غیرنظامی از سوی آمریکا بدین معناست که آمریکا در حالت تعلیق طراحی استراتژیک قرار دارد
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453512" target="_blank">📅 09:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453511">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czrJGtgbqWisztGokWMq71HQAOnjKy9BXjRfUTMEw8p7d96rxKouMboMR-aMf4VVEWP7I2XF_l1KwTYhxRUSHDy2oIpG9JJiMAFnu89q2d12ICQ8ctzvrUnvCkPEY-JFNu_OYNL-5XEfUUkcpkI1AinN2V8ltkrSYamR4MdQee3TBEDtvug-7w_MXUYnta0V_YcTVAtEq1-93Wx0PVka9NYXOugM7EX0eZe_ns9tg1Ucdw2Ma0Vhd03S7Hs2qbYjDeF5wizECq4tg7oWtiH_DeHJu4EGrh7Uyww_labAnvdo6H2Qo2l077EeKt0t3-pOfOzlV2cwxnl3XYmfiKdr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد پروازهای مخفی بر فراز اردن
🔹
دادهای ناوبری هوایی نشان می‌دهد پس از ناکامی آمریکا در رهگیری موشک‌ها، هواپیماهای نظامی آلمانی و فرانسوی برای رهگیری موشک‌ها به سمت پایگاه‌های آمریکا در اردن به کمک واشنگتن آمده‌اند.
🔹
ناوبری هوایی فعالیت حداقل ۲ فروند هواپیمای پشتیبانی نظامی در آسمان اردن را تأیید کرده است.
🔸
نقطه‌زنی حملات به اردن و گرفتن تلفات در حملات چند هفته اخیر، مورد تحسین فعالان رسانه‌ای خارج از کشور بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453511" target="_blank">📅 09:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453510">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شهادت یکی دیگر از مأموران فراجا در ایرانشهر
🔹
پلیس سیستان‌وبلوچستان: ساعتی قبل سرنشینان مسلح سه خودرو سواری به سمت مأموران انتظامی در شهرستان ایرانشهر تیراندازی کردند که متأسفانه گروهبان‌یکم میثم کرمی در این حادثه به شهادت رسید.
🔹
اشرار مسلح تحت تعقیب پلیس قرار گرفته و در منطقه پیرامونی طرح امنیتی-انتظامی در حال اجراست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453510" target="_blank">📅 09:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453503">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IH4d_DHtHT_fleqTAQLgu1a9LCmzFj10wOLECmsO27b7CkflGUEXDkmbBsGCL671w_BRgMlboRfUILeqJlc0LSQ_h0FsLKGMLGcn5n_ifTgCWTLxeq0ld1_Xf-r3J3Sx5ZuGjXDhaqzf31QWUhLaTwSmS42EysqOz81ZF6CsIoMFQxPwL3jP8KUWBGkQVwTO-L6vn2ilqYW7PCX7Z57ppXNrY8lZ0TzcIWxc7SFGlQ-FinQgjcfN_s7T-crAY2xRMHbOVeNN5h_7LccRAxHiQ0JeGi2kINQGjEEBdEbl6TqFnm8sL73QtYEMwuvdc7B6RUEtywiMr1CfD3_c9pjeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7-yJSwiBUBDAa0nRyrs6GgZCRR58vSFRmEL54ejD2NeI7z5TWHHRRckBpXbc4RMlDGeoOYsVDRvnI8hAKziQFmBPYG3xoXw2mbZ1YZzLZvirZwNaPW_90zwhafP6QqGIPcE94OJP1Pr0ahEUOmgPaFOG0rl3Iil5m0DQcA9i_zdKYm9o4pJegV4QL6fns7nf102KPd7qAkXltedCEaWAFJiX354OJzStYMmNWdtGuU4MmB7kOaeuzXfqLP9QAuXWRmnTZwGwAWPf7J-uz1hnYxAgiEAGU10-EGDBBHSVlQ78mACUsUi11QDKpgVAZ_PDR8UT0ztFhCtLv-_prEXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oraEwWWtVDmR3FcDUhr0F_Y3I14IRGK7ftf16Duopz8wXoYMyXj6_VK6uDZvGvfsjh9G9kn4i2cbqgKyZPDyrygVfIP83pkJY3cpfRej3HF8ZYXSt6lPc5nyLGk6wZHrbQXMAhLkDjx8uaFhqbOU7MlKLRgz1a9ckknwwCTMpiFkdU3yfkOFJRjB7jSOteykRlWlGgirsXlNe8dhmgvoiZf9gtyDgbi8SmQ_-qs7r2sgJdTRRcwx7z_W4XxgYaZe9FGwywgh21PZqULjwtmePNjNlJZCWndDTsRvNSnEh-k1Jy8YhjwMC8PDvlrgpgbk3xLkWe4OnN2EAmwH2gqxkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TO0NH0mZkVhL8YKm0i8wdVo3Q5zr5FWzvMlkYfc-Y5q-otqapuD0m5a6VH8H7VN0ZxFoKslg-IPMR2B75uRRCtmDlSxuraYcy-o_zNXuz9R7df9X4K6xPULDI87277bzbxtfRsODrIEWqf0XlHSWdrEnxyu3Bd-R2mG4FiRkKwOzC8ps-uvBAa_AFJzV04jTrQ_FuR2sJ84_51yH-h2dtoHlVDN76rfd53N24ssPLivLzRrNDWPotwncJ3IhluHlJfvZbifqqQkr2gV75-DYaoJER0pkouRdlC3rLpyYRDMg31gJKHzJrg0Lj8Mza2n5m-uZw7Yq1sLNF6ia_fpK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8YFfXcylR_QEpDibFGg5LacLMl2HQ-zxHLJ3NxStQwe1gco6Z4pC_82QeryNZBiEursiktGDKDMnoLnt2q-QSm_W4ac6EEsUdh-C9RDCK2h8mTNME_eE2JR2A_9VpQxyhTeV60ydX8fX_ypFOlkz8AZiJPChsTPWmegEloRCa73mAuZHiMljIKscveWi6khy-eDljEYVQed5GIenXZaxhjSC7jJ1yyBG0_FphMSSHZWxnT1sUsHOjLDf8XVbiopWue464KwYkO7iBIQw9e4wpUy8f4MjOFOLZAEc3xTwmJTD91chF_EnlaFmHFnTXrdbBp1m7BJ_OjxWBhft8bj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTI6XbwfU5LgU9fykWKUXC-gne6NJw-4kxuMZDJvtlrN12-MVwWvck2zGgz8zjMeuYqnhdnda7GYHDVZ0QrJCcBAskCWpl40xAWDy4FCzV7Rdv8w5HFoYQ4wiCfGHGVMGKzc0kIX5Zj27VxevdP_ioj35Co0_E4a1nbK-TH2iXif66EOLaKeOSbpGc1Sdw1uOFnLEhOWlz5cFiFoDDNQrDUfDmIvMj7nAR0qVaTKVz4hoC0-13F7kgqWDMih8GgVR4P4bWMmoBBHVrXDib_B1pD0ZrBnQ31DCwC8YTSr8vPV-DRcoMYFeL92E4WdZ2csl_RTRCbKqapHgz1_s2Rn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DiwbgED2F07GorziJDECLQ9lOidQDvela6sRwP8sVgUdA8JysX-m2ccFiBwK1EXswRlbcZ7_cpGC3_XcqJuQWb3yFrJLWKTjCLprntes8k-pkEEAOUTMogTV3C4GDAarrTD0UfSty5jutSSfE3g5IiBQR0Aik7m7jWO7vUFjuyXjUHvYWDvENxdWZX85bV6PlILgo_7SXmemxbfU55EeVuG7PdysNlVKUhSWkyyhrchFCCEL4CFjHyRyVUIj6zTPcQf8mT4gE_35RsYFm9lQNad0DNyZ5K1vH5DJUIYhheK6UWgVKytViqRR3_FX3bYqw_Voormt0G_OBbz2Nkc_wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
توقفگاه ۸۰ هزار خودرویی شلمچه
عکس:
فرید حمودی
@Farana</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453503" target="_blank">📅 09:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453502">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX380HbOjKhj1EJc5PLsw4Ot6-2gzlQd7H4IHy6PAutC9qo2yKqu0Big7MDwua1QcgUiFp-M_vKXyx4c1pOCfb2w0t21wg0fkKnFlr2S78UNKK8IQbMSbPlzn3rsIiWK4jF3-WIFgUAowByllq9zGptxmYBnQuhRPoU4kvo2s9PBNWV5-dWgUwt9OpxD41bqb-xuUG39sf4IDvSLHG90okmutYEENe9Gtd2m7JBIqFUPjoXcN7uNLJ7DOuloS4rPXe5WwAm7gzJRgY0ibjTHwHdIM9-W-wh-MTSbRNwEWsGRRGiFqNwcJzBJyFTwLabLJZq__y0Y0u15Vsu26S5rYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور کشتی قطری از مسیر ایرانی تنگۀ هرمز
🔹
اولین محموله LNG قطر پس از ۳ هفته با اجازۀ ایران از تنگۀ هرمز عبور کرد.
🔹
سه هفته پیش تهران پس از نقض تفاهم‌نامه توسط آمریکا عبور و‌ مرور در تنگۀ هرمز را متوقف به تأیید ایران کرد‌.
🔹
این کشتی قطری با داده روشن و از مسیر تعیین شده توسط ایران گذر کرد و بدون هیچ مشکلی به‌سوی آب‌های آزاد می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453502" target="_blank">📅 09:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453501">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453501" target="_blank">📅 09:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453500">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f116a0b871.mp4?token=AgeDV8QGklsLXRBNsoD0f0g7psY2G23bO8YHdgLpzmLHZaL3pcKvuLOwBf4h5WLkYpAIQQSZWEX9_R4WYs60bsYb7UO4HPDWTQHuTs3NYb4yOr35YDLFHH9CNJrw2r-mkzi-K4OFO4N95ft0LM_nQEQ7vTjGWcZxkVmB6NkUoUKiHLhzjGT6z_yjitBB38xyyaOyTu4ktW5YgZlq4Hs4q-vvIH4TER9e4Y8J_T_VhAkLcipWaO4zi3pyy26tK1srHEG5u-C7tMDWl6RtejCe7WcWFvHjwOBgRFBpytdeRRm1Z4lMPmZCS2mfB6nVzWdh7C1cP3Za0XWVTqXYs7t9_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f116a0b871.mp4?token=AgeDV8QGklsLXRBNsoD0f0g7psY2G23bO8YHdgLpzmLHZaL3pcKvuLOwBf4h5WLkYpAIQQSZWEX9_R4WYs60bsYb7UO4HPDWTQHuTs3NYb4yOr35YDLFHH9CNJrw2r-mkzi-K4OFO4N95ft0LM_nQEQ7vTjGWcZxkVmB6NkUoUKiHLhzjGT6z_yjitBB38xyyaOyTu4ktW5YgZlq4Hs4q-vvIH4TER9e4Y8J_T_VhAkLcipWaO4zi3pyy26tK1srHEG5u-C7tMDWl6RtejCe7WcWFvHjwOBgRFBpytdeRRm1Z4lMPmZCS2mfB6nVzWdh7C1cP3Za0XWVTqXYs7t9_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
استقبال از پیکر شهید سرتیپ‌دوم مجید کاظمی، خلبان قهرمان سوخو ۲۴ در پایگاه هفتم شکاری شیراز  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453500" target="_blank">📅 08:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453499">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بامداد امروز ۲ نقطه در استان فارس مورد حمله آمریکا قرار گرفت
🔹
استانداری فارس: بامداد امروز دو نقطه در شهرستان‌های کازرون و فراشبند هدف اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که این حملات هیچ‌گونه تلفات جانی درپی نداشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453499" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453498">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
سپاه: کشورهایی که در کمک به متجاوز دخالت دارند، اگر رفتار خود را اصلاح نکنند پاسخ سختی دریافت خواهند کرد
🔹
روابط عمومی سپاه پاسداران: مردم غیرتمند و به پاخواسته ایران اسلامی؛ عزم و اراده و ایستادگی شما در صحنه جبهه دشمن را در هم ریخته است و صفوف رزمندگان اسلام را مستحکم تر کرده و روح و جان تازه ای بخشیده ا‌ست.
🔹
شب گذشته دو تانکر نفتکش با تحریک پرنده‌های آمریکایی قصد خروج از مسیر ناایمن جنوب تنگه هرمز را داشتند که پس از وقوع حریق شدید در یکی از آنها هر دو شناور با سرعت به عقب برگشتند.
🔹
تنگه هرمز سرزمین ما است و دریادلان نیروی دریایی سپاه مقتدرانه کنترل آن را در دست دارند و به غریبه‌ای که از هزاران کیلومتر دورتر آمده‌است اجازه دخالت داده نخواهد شد. با استعانت از خدای متعال متجاوز همین امروز تنبیه خواهد شد.
🔹
کشورهایی که در کمک به متجاوز دخالت دارند، اگر رفتار خود را اصلاح نکنند، پاسخ سختی دریافت خواهند کرد.
🔹
تنگه هرمز تا زمانی که زیاده‌گویی‌ها و تهدیدات مقامات آمریکایی و دخالات آنها در حرکات دریایی در منطقه وجود دارد، قابل بازگشایی نیست و تهدید کردن‌ها و مداخلات، شرایط را سخت‌تر و پیچیده‌تر خواهد کرد.
وماالنصر الا من عند الله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453498" target="_blank">📅 08:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453497">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13626a5fd0.mp4?token=C9l-aHvnIVW4x9l_Yvggss_P6XAnPYMda2ygPJlPLGCQJvqDKSi5mWnNC55SNZmf_CVGlrqvcEE7XzS_xhdwjJRCXS489epallp50AIBp-ExlJFxLPTHwYIZP2Ygy6mmQqDIQ4Ql3FjDcKg-hhBuv4IUEGYHKGA67wlVCorVZfZTT4Iw2wDQLZdSsCZ85GmbjWoUAGqIZnDFAZrpXAHOBTidwTqSJUQrqbYoeoeEb_LPFjG1oN0JTvzF5mvCX6YO6fd43gGrqFDGva2AGWEVF6lCQYlyGfhp0XJXyzYxSI5fCUvEEuo2pGghqjqApXGRM5cM77mReix2l4F25BhABxl1kRh__w4fEEG4C1Yydoa7RoiHuAMb1z3g8BFIoQ3gLqovhTdhKpyadLZAe7lnzUHXHj1wWCErurCdLjwSHZVDIe1Wax0ZqoSYkkszADomuxd8GFGVNDhqcRjynLWhRdpad5yWJmxvNOfm-DnWWzDUovDiA1rYqnU3R1k46FJpotXCe_tjmB_yL2grlVlTUJM_q-v00dX9k00rCQFlVii9t0cDgjcIY8SUrDq2FEUwP6xa11pUrnunLuwYvPUCCDUFFhF20yAuVgvcfXTe74yARwO8uHIe83sXmFJzii2zNHMiBSQH9KkPSqo5YwKroBVpJT0Ii4TaBN0BzwjJLFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13626a5fd0.mp4?token=C9l-aHvnIVW4x9l_Yvggss_P6XAnPYMda2ygPJlPLGCQJvqDKSi5mWnNC55SNZmf_CVGlrqvcEE7XzS_xhdwjJRCXS489epallp50AIBp-ExlJFxLPTHwYIZP2Ygy6mmQqDIQ4Ql3FjDcKg-hhBuv4IUEGYHKGA67wlVCorVZfZTT4Iw2wDQLZdSsCZ85GmbjWoUAGqIZnDFAZrpXAHOBTidwTqSJUQrqbYoeoeEb_LPFjG1oN0JTvzF5mvCX6YO6fd43gGrqFDGva2AGWEVF6lCQYlyGfhp0XJXyzYxSI5fCUvEEuo2pGghqjqApXGRM5cM77mReix2l4F25BhABxl1kRh__w4fEEG4C1Yydoa7RoiHuAMb1z3g8BFIoQ3gLqovhTdhKpyadLZAe7lnzUHXHj1wWCErurCdLjwSHZVDIe1Wax0ZqoSYkkszADomuxd8GFGVNDhqcRjynLWhRdpad5yWJmxvNOfm-DnWWzDUovDiA1rYqnU3R1k46FJpotXCe_tjmB_yL2grlVlTUJM_q-v00dX9k00rCQFlVii9t0cDgjcIY8SUrDq2FEUwP6xa11pUrnunLuwYvPUCCDUFFhF20yAuVgvcfXTe74yARwO8uHIe83sXmFJzii2zNHMiBSQH9KkPSqo5YwKroBVpJT0Ii4TaBN0BzwjJLFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری دستۀ بنی‌عامر در بین‌الحرمین
🔹
در آستانۀ اربعین در عراق، دسته عزاداری بزرگ قبیله بنی‌عامر که با پای پیاده از بصره به کربلا رسیده بود، بامداد امروز در بین‌الحرمین به عزاداری پرداخت. @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453497" target="_blank">📅 08:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453496">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
منابع عربی: لحظاتی پیش چند انفجار پایگاه موفق‌السلطی اردن را به لرزه درآورد.  @Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453496" target="_blank">📅 08:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453495">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌ خروج دو کودک از زیر آوار‌ منزل مسکونی در قشم
🔹
مدیریت بحران استانداری هرمزگان: تاکنون دو کودک از زیر آوار خارج و به مراکز درمانی منتقل شده‌اند و تلاش برای نجات سه عضو دیگر این خانواده همچنان ادامه دارد.  @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/453495" target="_blank">📅 08:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453494">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
منابع عربی: لحظاتی پیش چند انفجار پایگاه موفق‌السلطی اردن را به لرزه درآورد.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/453494" target="_blank">📅 07:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453493">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دریای کاسپین فعلا مواج و تعطیل است
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریای‌ کاسپین، تمامی فعالیت‌های تفریحی، صیادی و قایقرانی را تا ظهر دوشنبه ۱۲ مردادماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/453493" target="_blank">📅 06:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453492">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWJpH5_Q7AhoORlsBTY5ItbO4OEag7B0rGcM-4jlcp142ijjt-UPPIMDjXRF_bo0I0w9AqqOxbBCZVatw15YFI-YdH7x7DHUuOoDm0oKktRtYxoBBDDzDqzNu3tgC7irSiih9gpa66sR7PqlxxnRYUusMYutz462ppPK2YXlLXiftdkaUd05EsNbE5s2aSrFwA72OBYBsnRVGXephHOZ-1nZIoVDP0dBBp2M7FlnZZsnpdcaMLBXaiJUxTL-GOg9TUcBAt3DLqZVniHOXTmrM7B68FQN1R-OYIgZnE5zNEFcpREA1UsyLwo2fgezq8i4XDXopI15kUIV819Fz2izSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد ۱.۷ میلیون زائر اربعین از مرزهای کشور
🔹
سردار جاویدان، فرماندۀ مرزبانی کشور: تاکنون بیش از یک میلیون و ۷۰۰ هزار زائر از مرزهای کشور برای شرکت در مراسم اربعین حسینی عبور کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/453492" target="_blank">📅 06:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453491">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📷
تصاویر اولیه از حملۀ دشمن آمریکایی به منزل مسکونی در جزیرۀ قشم  @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/453491" target="_blank">📅 05:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453490">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-jvdjxNc4nBAklqaN9wMGaek1RxhTa9I8HbT7k8jxyGNfgv1M5H2zpZOzBp9zv2J15xNa29tHesgC6uhYiLoMpylSf7kMT6dlEBY42QZVFxMQxAYQKQYsyebA5M23GPSGsgLGZ6nUl6gaEHfxXZZG7kWaSyvgoVwLwcf0VvUKlYh8cEGIjs6v_tITHrT-xfIUApf1udjUUJ3O-ntlyLtDFSHM81nV2F9-A73c0UMHnDRY69M6t9ZbcYyTATp6cunTGtb8pVXqYDD3xOm-0bsbmL2G643_zMPEah5Q-1IGk17mDXDvtgvzrigKcTbHSn41apci5-hlfaymNIrYbSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای آمریکا درباره گسترده‌تر بودن حملات جدید به ایران
🔹
نشریه «وال استریت ژورنال» به نقل از یک مقام آمریکایی گزارش داد: «حملات آمریکا منطقه جغرافیایی وسیع‌تری را پوشش خواهد داد و گسترده‌تر از عملیات‌های هفته‌های اخیر است».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/453490" target="_blank">📅 05:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453488">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5d_M6EeYcn2JiSAYrOqcyaH9ZjXoM0JzEJJH9Hphl24LgsNHQZrHlOQs-qs0qHl3VT4CcVhPcfbqzq2vs61LuT2464UYDBpQ5iZvt5CM4EmXGKcZv6YhlSYasxcV-vbTPoJa_DpqhNBRMNe6FdB6uPx_uH97mq8fN8H9KzhuBLwSy3rF_Tfb6Vets6JvqbnwJ0cx19mxx1pR-Q8h4WnOEGqzkMrP0g-FPvA9DQAYL7rCCKeg4jmU1p0PgrdfoCYN1BScug_LLI5NdF-AH3dkGcPgRxb3P2pwijDr9MigElnn0mzgdYMlzKtAkscUVroGZnj9Rr4OvO2UUy1bvrx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCDd5l2gWiuImxF825anl493vuanapfrK9-83OuTopQaZJz4-mnzQA45lo2PpvrFaXgUXZUpWuKbomjo3I2zzzdRAbDYYCn4kF_ACcQr6deQ4oSvRwMLZzPAPRVJMVDriWrHeN5XnGjpxRYltAbtMksvOq8n-WYdxQCczGIJaTDm7LYpohTAzWpg4D8of5E9LCk158Pe700VAEkD7_uflt8X6mOWaHAajus76v8lq9L07uuubb2sGvIqZRQzN5wVWMEJT-FXWzYJrkO73WghFzYo7T4nqhF19ZzoZ2IapuCCSkEgkvjqCEhhMZagGqwG-oCQLoyAuVL3bCCZIUlOXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حملۀ دشمن به یک منزل مسکونی در محلۀ چاه‌تنگوی قشم
🔹
معاون استانداری هرمزگان: عملیات جست‌وجو برای یافتن اعضای خانواده از زیر آوار ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/453488" target="_blank">📅 05:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453487">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
حملۀ دشمن به یک منزل مسکونی در محلۀ چاه‌تنگوی قشم
🔹
معاون استانداری هرمزگان: عملیات جست‌وجو برای یافتن اعضای خانواده از زیر آوار ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/453487" target="_blank">📅 05:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453486">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
حملۀ موشکی به نقاطی در اطراف شهر اروندکنار
🔹
معاون استانداری خوزستان: نقاطی در اطراف شهر اروندکنار توسط دشمن آمریکایی مورد حملۀ موشکی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/453486" target="_blank">📅 05:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453485">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
نقاطی در شهر اهواز هدف حملۀ موشکی دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/453485" target="_blank">📅 05:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453483">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36195e2362.mp4?token=vMHPnuUAEA1n6VFJt_vnXt3XGK4GHCDwj3a6ImqVtjRk1CsFrNAqwn8ONK2WrhqQIvmODVUX7DJ8YDhu2Q6PU6orPaLYTd3q-D52E3j_DnPnrQbo5kHx2FXexBehVcj_OcvfSf8FcSiABISX854hyhv3r_-kqLU0wruSfGaUTSHzGTGf9p2a-QWiIczkRfyML6DtnRwkDiGYQYAoPu1ErT4ZsiFrwjEYtsxLyrKq6g2D3dB0B2vSA5CuHBYx5AAsxGCyoAD-p1Na2gZbsbBPtsTgqscfI7DeMh6YZa0ZGAhrJOwnkwTp4RorGcHpDN6n6iHUk3AaYdvKDuIkfxhWfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36195e2362.mp4?token=vMHPnuUAEA1n6VFJt_vnXt3XGK4GHCDwj3a6ImqVtjRk1CsFrNAqwn8ONK2WrhqQIvmODVUX7DJ8YDhu2Q6PU6orPaLYTd3q-D52E3j_DnPnrQbo5kHx2FXexBehVcj_OcvfSf8FcSiABISX854hyhv3r_-kqLU0wruSfGaUTSHzGTGf9p2a-QWiIczkRfyML6DtnRwkDiGYQYAoPu1ErT4ZsiFrwjEYtsxLyrKq6g2D3dB0B2vSA5CuHBYx5AAsxGCyoAD-p1Na2gZbsbBPtsTgqscfI7DeMh6YZa0ZGAhrJOwnkwTp4RorGcHpDN6n6iHUk3AaYdvKDuIkfxhWfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌دستی کویت با دشمن آمریکایی؛ شلیک موشک از خاک کویت به ایران
🔹
منابع محلی از شلیک موشک‌هایی از  خاک کویت به مناطقی در جمهوری اسلامی ایران خبر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/453483" target="_blank">📅 05:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453481">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
حملۀ دشمن به یک منزل مسکونی در محلۀ چاه‌تنگوی قشم
🔹
معاون استانداری هرمزگان: عملیات جست‌وجو برای یافتن اعضای خانواده از زیر آوار ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/453481" target="_blank">📅 04:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453480">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
حملۀ موشکی به نقاطی در اطراف شهر شادگان
🔹
معاون استانداری خوزستان: نقاطی در اطراف شهر شادگان توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/453480" target="_blank">📅 04:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار در کیش به گوش رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/453479" target="_blank">📅 04:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453478">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هم‌دستی کویت با دشمن آمریکایی؛ شلیک موشک از خاک کویت به ایران
🔹
منابع محلی از شلیک موشک‌هایی از  خاک کویت به مناطقی در جمهوری اسلامی ایران خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/453478" target="_blank">📅 04:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453477">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بوشهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/453477" target="_blank">📅 04:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
حملۀ هوایی به حوالی قشم
🔹
معاون استانداری هرمزگان: ساعت ۴ بامداد، نقطه‌ای در حوالی قشم مورد حملۀ نظامی دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/453476" target="_blank">📅 04:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453475">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
حمله موشکی به نقاطی در اطراف شهر آبادان
🔹
معاون استانداری خوزستان: نقاطی در اطراف شهر آبادان توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/453475" target="_blank">📅 04:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453466">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDPFRlKxfQAfWj5gHS7MVQOPrFTxMIz3_3KbLIpuD-TIGFP__bPmYVk17zpfH31SY2Xs4-FiJ1Tyjh7m0jP-wvrsHE2FPLNxdTQH0bm9s8zW_5eA3kP2Ij8NL8RpPxAXe-m-_j9IwUQpnTM33a63G99obRWZIFaaRPnsiBoqrARuutoZQxepGJ99YYx55mXrf9MbE-ktlDJXz2nJfhEOPzJ2yiX9lSDcELaI6UZW7QC7scuxQ4jf2suQj3UeSPiQiCBOEKXsSmus4lCjeCBCVNp1gBu74cv1LhE-cTdNNgR3qXaLXKQjEaxCaJQTSTE1CpxRZ_zZWmCi_jrAHncM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEaFqItygf3f_7EX9pCU1yNZ3bz11A-xzGzDg6sCabrXep2E8L3dxg9fQbw7YnPylzDhOt5tQs2HniBNKmGDEMbSihiMlpqVbkoh3MfzuzzwmejJ5nJ1AlmLaOlfqBDEKhijB5P0Tetj6G3C3bilQRETT5egGvjhpP7u0_9IQ5CnNtvSFfPpWaWPA5XifOIQaHmx10KyJ5VUmruyBUsShxaSp7e7XccaX5Nxlg16quI7lSwE_EzctNi7UANbGWNJa4VuSpXUSFDI3KAVtzM6bWT_pcjN4YueWwzHD8yEvkbVaQZ3nnRoyhxKKs1gJ1_8aeLFYyDVOiztDMis5FjdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvU7pNBbJmk4ncpDFBwwgBwYbxnSMKLP0sLy1W1EFgg4YEWzgx_GAo7XLB-jWkBYiIiyNtsK6u27aZ6IS7LYKroA5jkP4N8ODS01qgMTBcuDH4niErLVwdmT2B4LLKjMxxChLbJj_qpuZUd5lOPXtfeWJ4ITslb5vNLSJ1UDdPk0wJeSwTWRHViU7QMVjnh9nqvWRANNp1Sy4gl1Y4G71xr68SmWIOnrOddOiQZ5-Fabx84ECKfOQ3pLoN9XW7iJYen-bVggVOQC0rLjc99DVhW68kSiayzhj6haSrR0inspqQ8fsPF_SmyV5_RbyKIxrhdrQjREJjQEqmOJPrS7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQtVWdWiU0rx2IQzg3qbPu4ek-f0bgjKp_WKgG_cPsgIYidVprqg2xM38GYIBsjLqa3Bh1qmnQb9F10sEg8jIkOX9zVGHtScuLDIX5bWhIBT6N9qRiiy4Geor7iZ9gTk5PVIGMWhzUYp5kxceibFyuWPiNkllOeQDXn57a-wP4IrAeleabgZcJBlE--fesuLuXnurazlhxcRIeDmbLdGxj-k8YJge415LFMGUu-FGawJZ7ojY_F1NT_Q56eukVqeT9z1fHdjIZfkZLKVCzXJVdb71asEfE_atMNnyRNa1h8U9Ix_Rl03UI5oHD-rP3Er-OzOvfrk3V_wl_pyWYs24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNeq4CUytGXx14MqnqzOogwFmOjDp6TVbWcKkpFmWl3cNlHdXVuOlM0h5Xi__rWPxDCWtyIXWxnuZnhi0ySHxxZHDWfKGl8IrJFULMnk-2o7cD43-ccMacsltgBme-t98QpYYguBIeMFc0jHJ38xl4QwBuAzzlPZBnsuUsEIt_ouujHrZ44gRMZInXI5Hk9C_B0kQ9W-1w--yKQWEvtIQbkseP5doPN6LPrxiLpDGFk7riIWRU0ej_7oNfh4CYB_Z9_K3L83kCaHu6TlVvtuwBBIKhvYgT-BIqZ5r8OJGDfSNV2M8vwXokInD__g_bugdVseuhqcaliDU5o7njCLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgs4qTgAvYtFSASfEPUE-zVUNIVaDnlpZEtR3Wx4wEfv688CbwAxbd0N_YKEa0ZPGk1MPtFzQvMIDNqa1D5KbjrDi_wP16rbeQ3uG6ebePrEr240-mSup-NQcNz-OgQA-RfSgos8twfNgk4doJAfTeAXYTOBHpH5-Zzzb7u_DChkQxfxDhrPLWCWcOfzzH4fCID2BnuorEV0bpZGax0uGiQNkOoMYh1N46CFi8u9w4qiRHYIvVLGTMjaWOe96Qd0HtnJdIZWkvPObuuC_iWXo6MBMMOUUNu_s6kw4WiWBcGshIkkH2ErqkhSi9EyZAlJu1LT9B_K10rCT2TcuWDwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ca3FlpKgGnuWkXhVfcJI3OFJrPfd5u0ST3JERFWJDhWRIqhKi4ZvD7x7z_VGOXFSvV3QRe77jDQKnQhEM4tLHymbRfYYzn1auiOlK9n93t-PD_HkThGbCITpoeL6YdTzLo2trXBFHNMe4c6Dn4lqZ9QgJp-LThTGl-iyPj58M9cmeY7ioegf6HQe22x-jxRuPpBUb36ItM44C5y0TqAVzU8SvcLVk5fsjNNca994W2JUDrjLaoEbDpqU68mWVoW5jomeW9hjwGiZx7yJuQDHvCpwSZe5OGLEChZNicExYRjayT5woAw1qgSYyd3K0cAsOvC8CYy2r9q44qSzdu2-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_0rDj8H09cji6xbB1iHWwRY22qSZPysT50NBxd9R7Yaiv2FRjwb5eKStdg7Z50KVBV83og8i1plZB1usuZdeAJRSa5_ujY3PPKNed6-ujyW5rc65kXcRb63V9vclSYD3YbAIRFL4i5paFy9FmCTL0-uyC98sGdcicd-nkpquDS6TYYHbu-_3wNlpsB7zdZ4KxO2la2z9u82AtG4z81DVgHhhdl76TiAHusNutoIyNmrxYaFEKKYx2Yywc5fYiaYXGRqjuAEiFdfjm93UkmncDWzzI4uQnC03Bi4RU3SpkGKqqjeaFeZCF6yo60wjsbLprilH60H51MOof2EGa3bvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJZG3q88y2BkAV6WvNYBRspwzT0hmc4IqxtZy8NvaoQmzzdvs2z4byYHuzMOevWa8pvJ9DhnQFIa5Smt-MrZ_VKXjR1r2kNc-IXbErw68D38My4M_v6kTNswxgTYyHE62aqcWc-OXRv5DZWAc-exulYsDxi5dLYyeUQSU8YkMbPlCj7mUg_vCDM_M13424hdnA56yo1_PsnJ46eNa0H2tiSQO2sil21wafEeNLWGPJONw5zAH9dC1Ez1JVb08jyJpHrVuTBr4p4lTlhbw6mwrWFsJtiMOpKQoXpOcON-hgPpxrGUmELtAqPeIs0ofCkmsxdoHVnPghi2yKFAISl1Ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ویژه‌برنامۀ سالگرد شهید اسماعیل هنیه در میدان آزادی تهران برگزار شد
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/453466" target="_blank">📅 03:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453462">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzrNUj-ypVg_VC35VtzXYMuuZfuZt61ZDVWmor6UCwg9x98OYo1RlTiBLbBmjJ4IJ-oUpOiT96Xsrc7RDNIOMR63CtembgvHpTRBrD0aDpdJWTAGCi8ozXpfNErR5pgNJEpMGcKOUYBqfYP0gpGSf6VMrkPutAPdleQ1YaVE7Z57h4Xz9j2wrsUjXs1h_LxydzEXYm4xeeLIYf7Lr-PoObA9eq4PgvtV0bN9XW5qvdw9mgbjqPAqzmi8oyvdLxVgiGOeeIy1QuvYGvP7GZwIzEML61unnS33Lpxqz42xCCdPykorKWtyZJA9F6VJcVU9XMWgZRJ5s0j4uw0dvYmKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNK3XDpWm3ypv4bWP1uZwvoWFNezDiiL-B-Et6FCktIxZO-dJDCSmA-vAF8BDF4zUtTDUqrNElruvPKW5wCPJmTXYVFYDs3ozyISAOTwITWp9kNV4LWQB_J5XRUC1cVCgYxIUHmT6XGCfMxZnmDSW4PXEp_FmDO02nul2qXSBd8e-777UZyouH5A306Fp0TnIwiOkBkhTGNoTS8bFIoS_pHNy-Hq6LAu1DHK38GLBMPNbX3-nVbwef3j_DjFYQbSVqZvN24EN2acKeXDz2XKETCU9RuRJZ2f1xh7qPZz3YMDuVYnsuhg5k5tYYeCCAkTNUNNU_vdt3C-5yUdz1dDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BU3Ul4LCDl2hPp0C9JgWOlbz77uo8ekNG8Y8bGCEZaAUzjaMJzFYmZFUEo5T-4EPRqMnnoF4-lmDu0psc7vvkyiCgGmyG0fXFkPbUwDs-uIeTfKWFkbTWIew9sSNqrHAFgRIAW9iRH33SfRLemWjAtINUEocwX8yhf-TappjD-BXvcQuLhPsvP8tA7XAmxGhOJL4R5kHFK9cz3N_Gn2UKWH8rkvxeoVUoU5zvsMXMkqlGd_-2qEVE2PTC6-IglITowwp_VPbrp6pmznwmZ1wInrapNw0HPRdLO9UPKkDMrEwMJPCT3MjtUtutv-c_qC4FC4KCe0ohuVBiuqda9bwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHCSKwiF_0PND7-3XMAno4i-epB9ohCtNX0kobQ5fq9Ao7pa8KPySxpuz4hMW-5e_B14nly2iGmzJPVYHLiHnaSnf91M7kQKphhKU3Esq4eb9h7kRbT_BL4m51vacEsdlFAznTfE0JR-A77VneLnDumem7sMGyJ1KUKHtjeJ6YJ2NfZivIb9W8qBnTZ6bQje2tytSgn_zaM9NMIpMDbhavyhRWySXuLmekrOVu2AIX-ywXS0Tcsu6JZm-gTOtX5XemJUo120fNgY4dybho9M5dRtjkCVC4MCNLdRdmvbzPSAdjFAB_gmmcge1VQxoHiqSOUJQRuRQ8RLPNH13ZK-SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۸ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/453462" target="_blank">📅 03:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453452">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZ5_A2445rI16wHvCo_0RUjQzsJ6XyGVCXSxZ2cKppuPb-w7tnhGkiYka4lozvGGqk8Hxps_4_1a2T0fuAqKuoqrRUhz2meiyrzFkly4S6t2pSKcJw8xlqpoY27w-P59OW7PuGvdyXdfLmuh8OY8f4umQt7gFiFWqrBXY_S_uD7jrmlJ_7zeOWUJToePOkx95x0P4VXClXAyxqskikXvDx3duq5sSxYISgW7TYkKvtzID06Lbvni41580zTWWz2xqw_4n-ZnPtjD7S_C9Tr_OT0eDliWYzJpoJY93QJ6T2aS_cgbpInEkhx3IVRe1C06wmV3hUbRseOxdyn3TV2d6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqNf8nmd2qzQe1Fpn8OFzId8s1nSVVde5lAJixJluCWnzOOyFT_UTaFYLc_D82cXB5PANzsUTTCYcYlNKcdVUZjpNShqGwT1q4JPi1tfBnFuYhADalK_O5es5dI26BveFLGMtDKvkIvx5SUqpAZsIohiUDg8tnOS6Ea4WWAZJ4OWmyx_YIzD7zi90lUReW62eDkXDyYkN_3xsdSPUKcP7V5M__4m_YBAwmXtAee38M11F1lYy2ZK7BH153l6eBH_PcHZXkVBskDlPIcMielqLAlqFi5eBPHPdjQtVqQl3xyDGG3NmSLcYxefPEg3TNxrMG2IZQ2wbSi4Z3egfEYPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzKIHxcSO1ATfXou0o6lVhpDv-swOc2lUbk_Xcet6yCfwrd6ClpFu1X8B5exx5ylDfvfB70KfLLAfnmI6J53KI-v8jpVwvOrFWT1uk5UUKWVqqKkQrXe4x7nDBzYqtOVW8BfGAQj0s1bPLCna2GAhNM9Ugo0Th1yfYO-a7PzaxnolP9AGCkqZEpR9ibP8pvzm1YzkVRdRw5M0KLe8-fKsboT-O492QNkBAWoQem2bgCHWAuDhY_k5xS_ocxt6GQerfEQml095tIgTCPwAN0QLNMPgjGqsUioBAeMhm-qir_cHdqUlX1TXQEz5wThWHt2-cDjHGHMbMTGn482bvCZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nut7TwaG9RwrqjUab8E17QxFGFyfLVdogslY4Q_wwr1Emtt3vTyfKi8Zeqo-mllHp42viqEIi3VL1ssaOaqDCBWySn0-Y2kZ7yn_xnD3wm6mlJ2YtzxnegDgP-HfCsKeqaUpIWqWqIho1QqZKHgV6BhZCiFZ18_xoI4xtyAfRMda4GTbCehTAQUuOZchzcwICNqFpKxoTCOtOyIefd3YQP7x9dymN_SRXO5gN-QeVLG9QirtFHeBjZezSRAqBOIm1sEUq29yC96c6TFDXf4lm9SO99sqh0Ch4CJyDz3TjduikVq29hUy8PaoikZjQwLggSCmYcyhsAkt7B-yRXtXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MT12iyVxDKLg196AU49-ETwLiP-T-ghtWYchczDRqXfvST3eTYIkgsFOcsFIz0TnLOfs0SyfyRk9lyPJ5pWhNepTWE5-C81F-GaJmrSgLNzUdYpm1wMHw0xVAWBzKjJ-t3OpqOCiJPVj0F51GsiV68gsekESqxfHBdrOsvMunIw1YcTfro64-jnOUSaznalDDpe8_Kn_Eo9P4gNJcA3j6njTVUFflyekI7IzLMbx1j8Fw2krAH2cCEEzNqQRH16W4Is9LyR-1U-tLYptf6rTyGsB41BsppEb5Lo4SMPKt6vVak8cv_mXCxBPdNf2Kv6WOiC_zQi59_MuWEcoJehdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtAA85D3qK4EEsc6FyZOE3s5BHIaKTsAUnDwgKXsXuHyv3z0Tc673bjJDlbOLXNrXWJv0Cnuz_xW_if_RWpBntYzWHeFJLyqYc455yoZfaSo1je2xQqdBOAWwe4JHUiyEUXA0c9HYwm_WUh-PrJyLApUzZ2g5EWtWo-4KSt5LYjjHC6EqTMGee8rvyWpFjpTXqzhP4yY9PL9ApyyJiAeEnB4amdGtWKEKq9_nHDDUEO-gL3id25j-3Qv2FqNdTbZdZM7nYhyB8fcX3zPfxSLr_jNsYp0kCYGE2fpJlDMJpAx9USDm8earehk_qkQtMHtlVoiXz3vL2AU0qmt_Qmk1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtFrsw3al9KNWHbkFpqTguW2F1q0C3QGv19E_KBw8wN1iuwZYGzESiQ8rEEP8F6KP1cR5uSHDVL0xtpiYhVAj-c0IDtvEaZlYfsnhxaBn5g2U9Dy8c2VPc_7dElP3lhW6OyCBAibf16cBv_I7t8WF2dqlMCC3h7JZzFaxzo6tZlyzqI4Sg3X6D6LIPe_BY8pnPirr7KYenshr3a1Key_SQumisiH_Fr7MZ1K3gUvdaK2sr07Q6ngBl6J-GNCC5hSXDTCVHneSIw1GT1XLHueMD6Es5-3vCGBmmtvUEuCh72duxWt8MouV4GMXkj3TBBvufv01QoC3j-rljU7OxYvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHZur4kvmbAopeeinY4zgFJj35LFWULsi1qB1EkDmlX8abo2S7RdpKgzkHG2UWZcqY8CjU437kTXXB9U8gGN2eelqkobu6eRr3TRrsJGbqEP6O1xwlIXQeIr90aUddbZRUYT21Kgedu5asOt3Q5drHqH7NfanC_9hC5OgI5mQIU04FF9LlZi4bCv-T85MtzqJpyNAlp7ys_UlPC22dVVZbcISxBSxZ_JgtJihKR1gv0ssZzusoi-Y7VQrzaMhlHm696kjGuPsXt0KUnma48fiEbBm6KGRQoKDz2YOeidqG_S4_0d5O4UNLpI9yNvWYj17SvXAgbtw0_qKhhDooV39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gX9iKk89Eicn0Zjr51l4IgzXKPla4ZaG85Uq2B9ixnwAwkwPgqR2-7uFdmT0ddO3xenifa2Ev9z7Ps9TLdAlNfn26FL3VQ7elD6KzL5Gpkm-m5DDq2SLeZHDZNLMaF6FSUX0SZvTQcpQfr00EdQ_HEXmH0ZeDBgkxpe80CnqOXn4ec3gAXlFwUHo6VJVN1V6MAiAqXFI_rTC-YcOcY9bFzQLeFqNwA2pfgLaY6hRu9T5t-aP8HcNnbnlYFnGQc93uxHodVz8SFh0YSu9lvfHgiWKA4legY3G7LJlFv1C0yZITbZpUKkaFattNMKmetLDIjk-7DwUmMS1jldVJNM27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrUTblbgvS9Hv3raeFcmtfuJUt5AbybJD3xGADARd7BRt1r52uJaRdN0OqmiR3n5TlVqFHKyK3htvD-q6FIxNKaynCDfturQ93m8prkYTJ4nxPhcY8JRu330YDZcOZ_bRWXnFIc5VL4INpeMQV1UoWsOYsio4NX1AHULxT1uhSP_w9h_z4eFwqafRplsNV6Cm_hse2ZEnmHZL3fcQqD3uWU6uTvekOwwsrEAYHFeZCPRvulMe7jX6cRbs-AhGU45Pet2FdvbTGitKkivp8vtrPIDE-zTwc1NwYFIWuv21zGKrJ8puHowf1PJW4bBHZDcMRZ_ySFu8aAYZrSYSPENaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/453452" target="_blank">📅 03:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453450">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFW27AaxicVp67BNranCwNQu90Vo8Z0Cjh2gUSlR4Ll6hlA6bRFIhtS2oS_RitoLmolL1n9mfBwdKSrXzHLYTYLinAdMucUVSOwqsnj763GZrbki0WRS4Doj1QNdehRIgkNQyrChdpW2-uVx0kb1m7ATeKPIJUPgs4WSLyjq9ei5D0lTILSYNXTnnnYdMDL7HWDiV7-_S0Ye7MtlQU3YE0Wp5HhBfYtFki4D59RrAvpLkTtmOqgbGMEIksziEHwrMxWkhTual7EqK1Q8c3MSaCBZLstaVZPGfYSHjbfOlE-MxGbAVfK32IXsBZMuOuXvED784-O6Rm4eE3NmjKvQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد سنتکام به ترامپ برای حملات ۲ هفته‌ای به ایران
🔹
نشریۀ وال‌استریت ژورنال نوشت که فرماندۀ سازمان تروریستی سنتکام طرحی را به رئیس‌جمهور آمریکا پیشنهاد داده که ذیل آن، تا دو هفته به زیرساخت‌های موشکی ایران حمله شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/453450" target="_blank">📅 02:38 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
