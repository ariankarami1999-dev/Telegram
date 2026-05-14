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
<img src="https://cdn4.telesco.pe/file/h3kEKV1g-DBCh1LL5Pn8OoBGPJlLpPtovy2nA-0yvA2oDK4dJgJ2t2prDP3TpJFy8S3I2H8ePkxHQr45HAOJnWsfJMMMpWaeFcPsr0JNL4__twBkQnsfoEh02x7o84jGpB4RVuuyNmKUrPkGbJiOdA9gkbs5so5V2EQ5iLvdfkLQ_c48T_WnvyAsEk0_3QDjGIRkU68YjtWDlgn_BXsnfftkHvz7ZvlSDyJ7Xeu-w_FZVuht5CtmAqXAreA_LI4o0_nPCCGFxTT1OTFA7c3bgoDS3n3wTEH-6u12iMc599nHO9xgWlHaZ3ghwY8TiSXyEAYueJP5pCR62YabZg3wDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 957K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 02:57:01</div>
<hr>

<div class="tg-post" id="msg-120055">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ccpQdgBOSfZYeDPUtt1lXYgznkjfTJi4cjJk2th_86LWuDblMGkOkkXwYCZRv6hX3G56u7QP0uRX3A6sAN1qKlraei7siDRSmKKX_sViyEXln2DbIoD__42u84ph0pWRIfm1Iv3qOdPj4yjgmAeNliV2Eqj-VErEVF5jF-ENasWi-UfI0PdFB1J4WHsDV9hbNdjxc0V_I4KGOatx3hD6MPZq05RNrztswsuPIm5cB1Wffp-9w1tGrZUfuzgHcwYzh7d7Jvg7ALQz5wvqROwzMbCmkuHa0sc2p-gQz16M9OV-vKAeA4w6ACi4qBsydswpZKD-ijM6t0ZdfHnBJoEODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
اینترنت رایگان و آزاد برای همه مردم
⚡
VPN رایگان
⚡
کانفیگ تست‌شده و پرسرعت
⚡
آپدیت روزانه
⚡
بدون قطعی و دردسر
@NetaazaadVPN
@NetaazaadVPN
اینجا فقط وصل میشی و راحت استفاده میکنی
🫡
👇
@NetaazaadVPN
@NetaazaadVPN
@NetaazaadVPN</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/alonews/120055" target="_blank">📅 02:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120054">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOCLlJ4UtZf8pI05mwqZsn5ey9QQRhyEPBi0UtRnhVcTX9vqKVL8gExFo_Q7Nsb2-fFJkxPrON6q5YMHni43oG4MIra4VX2Mv5XI4UKdKINr-QgyKzVA8MZ869fI-MpDWTD0Yb8fH3W5hCOKF6rYC_L1H0S9f_xjIxcasx9cT-aBv5Q4LrLyjo3W6mTe3ld74gGT51nPUiUUlfinOIU2D5GT8UZliViGDpIdhRPeHQfhLRb_Z29PoSSiZr0MCH0kbCYuO95CEZKEAq3qSh9daVW3A-R1ejVELu0Ff983mUkvTPDqdq_dZAgQfqm7U-J11sIkuCabT-yIrUrP0BfGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ویزا مهدی طارمی به علت خدمت در سپاه صادر نشود
‼️
@AloSport</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/alonews/120054" target="_blank">📅 02:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120053">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری/ترامپ:
نابودی نظامی ایران ادامه خواهد یافت‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/alonews/120053" target="_blank">📅 01:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120052">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh1xldRJKTYpYyYk-OWY-4VbUNXZVlaIDhUHLs4bklSkH8Op2U6BluomTEDN36j17AinQR0sUXR2Bi8xQBJOgNqK95gErBqjUlx4cya4bFbj5cfcreXjpfBSVkMWFMjAkTqpQtpQGGkLn_KALTGAzQBCbkcPAXAEp8WTlhNry4oPrUpBTpZrmfvpnHJUHmuNYGJIM7dSPUWh2iI66ovvxvnt90QW58IBhxU_ON-hMuBFwhOclQKd3TtXgjrA0AplXpq9iCwRjdcKKhVRFmiV4MPVYowXXE0lvYaiCYdvXOzXacj6U-hadIkCWjipv3ObhjnhoT33AXGZSn684iaFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت جدید ترامپ:
🔴
وقتی رئیس‌جمهور شی به‌طرز بسیار ظریفی ایالات متحده را کشوری در حال افول نامید، احتمالاً منظورش آسیب عظیمی بود که ما در چهار سال دولت جو خواب‌آلود بایدن و دولت بایدن متحمل شدیم، و در این مورد او صد در صد درست می‌گفت. کشور ما به‌طور غیرقابل اندازه‌گیری از مرزهای باز، مالیات‌های بالا، تراجنسی بودن برای همه، مردان در ورزش زنان، DEI، توافقات تجاری وحشتناک، افزایش جرم و جنایت و خیلی چیزهای دیگر آسیب دیده است!
🔴
رئیس‌جمهور شی منظورش صعود شگفت‌انگیزی نبود که ایالات متحده در 16 ماه چشمگیر دولت ترامپ به جهان نشان داد، از جمله بازارهای سهام رکوردشکن و 401K، پیروزی نظامی و روابط شکوفا در ونزوئلا، شکست نظامی ایران (ادامه دارد!) — قوی‌ترین ارتش روی زمین، دوباره ابرقدرت اقتصادی با رکورد ۱۸ تریلیون دلار سرمایه‌گذاری شده در آمریکا توسط کشورهای دیگر، بهترین بازار کار در تاریخ آمریکا، با تعداد بیشتری از افراد شاغل نسبت به همیشه، پایان دادن به DEI که کشور را تخریب می‌کرد و بسیاری چیزهای دیگر که به‌راحتی نمی‌توان فهرست کرد. در واقع، رئیس‌جمهور شی مرا به خاطر این همه موفقیت بزرگ در مدت زمان کوتاه تبریک گفت.
🔴
دو سال پیش ما واقعاً کشوری در حال افول بودیم. در این مورد کاملاً با رئیس‌جمهور شی موافقم! اما اکنون ایالات متحده داغ‌ترین کشور جهان است و امیدوارم روابط ما با چین قوی‌تر و بهتر از همیشه شود!
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/120052" target="_blank">📅 01:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120051">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e6fd559e.mp4?token=C4ibdRMsx4KE2aQfErOTX2GrUtGJZPY3tNAcI76HQn3DTY2x_8wbDRElXruATQA2SlfyRAEzrlntkC9JGdIS1XPW45lEcjKSf_GEsQ7TSATLbzZpC2wVGr1xB2SW5gms3vgzN39s2OvwfEWuDOHxQk5dyLTsiGII4gR_QZZYhf3g-i_6600KNO__O0LV0XuuLMb0Kp50jVuGXYROMRPlLtkeBYKwp5OqQPCRzmde6o16Muu_EHFgKpouZhfmLD-2v3plBeYBgWuSNvjiIWbASCRWBRUyVu3aYqjOMddNmlnozkIsAIg7FszIpzg07PIMM5QjwjvC4vUNMYsmZi5C1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e6fd559e.mp4?token=C4ibdRMsx4KE2aQfErOTX2GrUtGJZPY3tNAcI76HQn3DTY2x_8wbDRElXruATQA2SlfyRAEzrlntkC9JGdIS1XPW45lEcjKSf_GEsQ7TSATLbzZpC2wVGr1xB2SW5gms3vgzN39s2OvwfEWuDOHxQk5dyLTsiGII4gR_QZZYhf3g-i_6600KNO__O0LV0XuuLMb0Kp50jVuGXYROMRPlLtkeBYKwp5OqQPCRzmde6o16Muu_EHFgKpouZhfmLD-2v3plBeYBgWuSNvjiIWbASCRWBRUyVu3aYqjOMddNmlnozkIsAIg7FszIpzg07PIMM5QjwjvC4vUNMYsmZi5C1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز :تو سفر ترامپ، بین مأموران سرویس مخفی آمریکا و پلیس چین، تنش ایجاد شده و درگیری لفظی و حتی فیزیکی هم پیش اومده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120051" target="_blank">📅 01:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120050">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg6H-43fB6ijkkoOktD_2fcI58WWQ4XcK4CVg2khekaAfEI-oYhEeGbTVv17zeCbG046eg6qVu5_POgp6GHyIFvC2xthYo7UTFMAX3RomFvsVmznLS1U33x_TYv_9gzIrJo5y0Eu6A0_H36fgiN8ZuMixrWy5Sv4x6BYRWW9eWKoMu66V41W4NnKGPmm6N7K5TJ8Akv-Erbn2ScjDD8tbDutm91mzrdgYQFRmP4DaN_a3ckFubcC4ed5CaiYkvsmufasOO2B8z0GKDEVIWXjsXqzQz97PH1HmLtDlMVTVTUuNCtnl8fpEW-M7S1XSqYLLsKrIBe4_VpUY_5n0EP6uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:
آمریکایی‌ها متحد نیستن و بزودی تجزیه میشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/120050" target="_blank">📅 00:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120049">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZAJMi1y7qnpPfVaDs1zyzOBF-qaetRroZfw65ZbPD2ARvNUq8rezJjPx2o9sbVJKmLarDTb3IWgWLrSpBfmZK8Jfjs1dtMPJ10N9DBYRgorE4fH__PrxJhI10C0qkCLIFbF1apdKTdJNsf9kT4otsysamZQ8xAugryyE9qJVmMhtpxrdxjmMK1WUOHc7nh2_5842CECurnjd43ndb9opMJot_LyNjnha42vtCi9ui3LiuC0RJ-Irf77At9oezoHiqHeBsnsSnA7BrwIiRC8RFRHnTmjOeiyomhP8dvGGBPmMWJ4KVfYM92N4a8Pxr38mp7CDkbk74aD5mcQHm0c0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری وایرال شده از گلشیفته فراهانی و امانوئیل مکرون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120049" target="_blank">📅 00:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120048">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3eNtTIHBzoTqstTKPCTuAlzIqzFEOAm6mcavBL9HP_-ysmhqY4mFRufZeFJJaTdt1jKjjwvWKt_JEeqSDa6d8jjRyR8TczOUmAevTN2yQ_Upo9I3bD_9GWadqg8B9VIUIKyiXfIwFt2vU8cuy5D-5r5P5t2p3aQfZrlYvW0lUGo9GIGITgJSQikhHYtM2crGPtt7qz-ByQtHwhhtZ-Qq7wPGMS2O9tDAt5P-IaxUt7MWpdYOQu41KoMRRXegKTlLqLCuZVQxWobkwXz5q2X9jeMw0GX4TGAYvKxIyZ1XvWs1BpF6ZnLfB-G2EYIVnrq1C1ijMcUUuYS1R3EJSsRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یدیعوت آحارونوت: اسرائیل می‌خواد اگه درگیری با ایران دوباره شروع بشه،تمرکزش روی زدن زیرساخت‌ها و اهداف انرژی باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120048" target="_blank">📅 00:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120047">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/سفر هفته آینده رئیس جمهور اسرائیل به آمریکا به طور ناگهانی لغو شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120047" target="_blank">📅 00:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120046">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CZcLEA5ndm-fJQs0n3pNvJ1EfejpQcOuj2W-1Poa18iG73jlVffPUntkLgWh7VNOcdOwjwH0gnbNQRrXI87wZfvdj-ELwRzgJDm7SFKVJ9gQ-zb20EoeXoZ-pSsoY1Ug8-hqxGqDr4h8g_AmWlIdgloxHVqnJ-wSX_SzhvZpRJ2dJDU4VDl6XtmLG6oTpstteOn9AoHqD9Ep-HQHjkEVL_A4tydQAq6CxlCrXJoKUb7tGYY0dK7FLQ0RmV6LfPJzIFrCqiwiz8ylTjZpP235fu_AU2ero4pZmYIpuxARTd3YLE5BpDf4-V93-HTGw8ob3jfcQ-i8DSn87YyrScVJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب ترین توافق نامه ازدواج که توی دوران جنگ رقم خورد:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120046" target="_blank">📅 00:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120045">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تعرفه سرویس های Vip
⭕️
✅
1 گیگابایت
⬅️
235/000 تومان
✅
3 گیگابایت
⬅️
735/000 تومان  استارلینک Vip
💫
🌟
⭐️
5 گیگابایت
⬅️
1/150/000 تومان
⭐️
10 گیگابایت
⬅️
2/350/000 تومان  ویژگی های سرویس های Vip :
❤️‍🔥
✅
متصل در تمامی دستگاه و اپراتور ها
✅
مناسب استفاده…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120045" target="_blank">📅 00:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120044">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سنتکام: از آغاز محاصره دریایی بنادر ایران، 72 کشتی تجاری را منحرف و 4 کشتی را از کار انداختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120044" target="_blank">📅 00:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120043">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزارت خارجه قطر: ما به طور کامل از تلاش‌های پاکستان برای میانجیگری بین آمریکا و ایران حمایت می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120043" target="_blank">📅 23:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120042">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سوپر اپ روبیکا بیش از یک ساعته قطع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120042" target="_blank">📅 23:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120041">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhikVk0EoNy8n7Nmm_jP99CDPEIgIHE-azJPuVzQ__s_UIxDvCl9o4CzBUHMEhVfXj966tkLG99wuqJjbCr6BWWCnb2KxwtXpQWDq8adBqt9XeqOxCbvOT6deinAxFJIpP1CMWnfFD59_jqVmcQBK92z2ytx--Kf45_cgXwgfhAnPTIET1mMm2NYa-raggex8wNyvXOab16oKc8KWlNMXNt2mH1Z7ZHzGbdhuQLQ-C8JLgMhRoYSaRXR0QCJlWJNlyxwEBnK1EAcS5etENFmJmAiPH8R-u-r8jWJGNzYqZlfQDUUeMPAjvjAQ0Y70_H2WtJOMYy0CV5lMLvhYWuVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدباقر قالیباف: پس شما به هگست، مجری تلویزیونی شکست‌خورده، بودجه‌ای می‌دهید که از سال ۲۰۰۷ بی‌سابقه است، تا بتواند در حیاط خلوت ما در هرمز نقش وزیر جنگ را بازی کند؟
🔴
می‌دانی چه چیزی دیوانه‌کننده‌تر از ۳۹ تریلیون دلار بدهی است؟ پرداخت حق بیمه پیش از بحران مالی جهانی برای حمایت از یک بازی نقش‌آفرینی زنده (LARP) و تنها چیزی که به دست می‌آوری یک بحران مالی جهانی جدید است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120041" target="_blank">📅 23:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120040">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ و هیئت همراهش در طول سفر به چین از تلفن‌ها و لپ‌تاپ‌های جایگزین استفاده کردند به دلیل نگرانی‌هایی که داشتند مبنی بر اینکه مقامات چینی ممکن است از آن‌ها برای نصب نرم‌افزار جاسوسی استفاده کنند، طبق گزارش فاکس نیوز.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/120040" target="_blank">📅 23:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120039">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
العربی الجدید: حمله انتحاری، پایگاه نظامی ارتش در منطقه باجور در شمال غربی پاکستان را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120039" target="_blank">📅 23:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120038">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
میدل ایست : ارتش دفاعی اسرائیل از فردا که ترامپ چین رو ترک می‌کنه، به بالاترین حالت آماده‌باش وارد میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/120038" target="_blank">📅 23:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120037">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
طبق گزارش بی‌بی‌سی، شناوری که ایران امروز توقیف کرد، «هوی چوان» نام دارد.
هوی چوان یکی از چندین کشتی شبح نظامی چین است که پکن از آن‌ها برای پشتیبانی از ارتش‌ها و شبه‌نظامیان در سراسر جهان استفاده می‌کند.
🔴
این شناور توسط پیمانکاران نظامی خصوصی چین برای کمک به اسکورت کشتی‌های تجاری در دریای عرب و دور زدن دزدی دریایی، حوثی‌ها و سومالی به کار گرفته می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/120037" target="_blank">📅 23:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120036">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkwC7PYjH3MHJCoYmW2sjzFZiwhV1Fs85DZyEnk9Oi2H2x37Znkhda_7va91SHjf8VYrH6cZWZppiJZuF3pmTHCmLkIxzIOI8G-jxeWszVrlZYxVqtdq66kTbaLwrPLsbe7huuSfsE1wFxEstv0Zjw521LgzWg-W3VykfuCBouMlZqNpcxp9p6E3U_E_79L8VKDvyB3LtZJsQ6vnYDF55lNlQhQRp6xwUYooHCoVY-jLcoBeIVFQlH10KsdN-qSokciGknn-dlh9rZjfFgTzDC2pcISqWj0rSyGmiJn1xXgohFh9PAYErl24jk-JMpH57sVv63a2toN5dPh1u3iPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدل شاه فقید در تهران رویت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120036" target="_blank">📅 23:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120035">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
اعتراضات در کوبا آغاز شده
این اعتراضات در حالی آغاز شد که دولت کوبا برق مناطق شرقی این کشور را به طور نامحدود قطع کرد.
🔴
دولت اعلام کرد که "مطلقاً سوختی باقی نمانده است" و وضعیت اکنون "بحرانی" است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120035" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120034">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ea95d90.mp4?token=kxScCH-VQSeairBgpw6Z9xZMAjget5qZ33rv9w2n5uxt4g_d07v3MlrI8muXxjg-veMWecKbKL1kvSFmbzlu8qmggbyphywGMn242hMmoMXzApYPfEYFy-7vs8ueMY8OxN3pm_PnA5I_J9gbgjeDx8FRJGU-K6IHjeorlQmDnUflqWt8FwvyGQ7kx_G2u0t8bFmRIxzPV-Xz08GkOr5L7RhyBbH_niUTaf-jFcYTruxVB8veNoqUc4SuxgjUXqXEb9MPP_8ML_ezMWHkWV0TgiApMTnYKc6JHYdyQ-QmAEEbBkn810ygeojSD9jMDXdztB7_tV2DCkx8H0Bdl9zsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ea95d90.mp4?token=kxScCH-VQSeairBgpw6Z9xZMAjget5qZ33rv9w2n5uxt4g_d07v3MlrI8muXxjg-veMWecKbKL1kvSFmbzlu8qmggbyphywGMn242hMmoMXzApYPfEYFy-7vs8ueMY8OxN3pm_PnA5I_J9gbgjeDx8FRJGU-K6IHjeorlQmDnUflqWt8FwvyGQ7kx_G2u0t8bFmRIxzPV-Xz08GkOr5L7RhyBbH_niUTaf-jFcYTruxVB8veNoqUc4SuxgjUXqXEb9MPP_8ML_ezMWHkWV0TgiApMTnYKc6JHYdyQ-QmAEEbBkn810ygeojSD9jMDXdztB7_tV2DCkx8H0Bdl9zsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیندسی گراهام، سناتور مطرح آمریکایی با آشغال نامیدن متحدان چین از جمله ایران و روسیه، از این کشور برای باز کردن تنگه هرمز درخواست کمک کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/120034" target="_blank">📅 23:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120033">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZjJMgukOmL9ZCydTP4diX1j9CB5BoDE7jQ4Sqqc9UVmobZS2X2U6tNeX-DjUThspkd4seJxbZDS1aPGilxw2DrbNJpUrX4CT7nQeswpLR3fZev0bR9PDjOjD9AEzhZJlpiW4utOBJzgdz3mxvHcwv9R7KSi11vrxIGvyFJWk4BQoDtZz2gz8aIeu5bQpi37oIHRDtmprhgyq0sGOZqF0Bk0Apabg2Oe2GJdLu-o0h16ri8HPrOVNxhz5zmJ5Vn3hQY-YYEw3L406hNtF3aocCeUPCdNaERhCCD2pKXBoUHHKaiOg5NqGN_vot89bTCNJ9MPBoTLFqJWGV04WkLlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
قالیباف بدون هیچ دلیلی مجلس رو بسته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/120033" target="_blank">📅 23:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120031">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s71ABPB2QIZ6YLB635oR7fwaDHt0zzRaHWCFr6tOK8G8kSD8vcgmas3JZQDM72BhR74pqDvNXeTH3qki2ewJltLeSlgL0uSVe1vOIjIoM8ODyPsOqxsAi6bJc1xNDOHP4h01ac-PXNdOpjGtc2EhPuWQPj0StMLcNpCKYKKBX16s6qJ2KCRL0Q6v_tWluWeGFtoegieTLcuYIGFusLbwTJTpENKpYJbeZRJLpmaAvbik_ob3A5LnLPj3U_eMknl4IQsLhXMyVJ9twWdWjinti3tFQvFxHqTqwACBfds2vcpMs6BXjCU-H0Vc29KP7Pjq2P2ljkWkjaKao2pLfhf1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5H4goIltBDgGl4EoPePjl_4FkYTJ8EMXCKCUM0zUz1E6h2dc-06162NBmXuU1IPtU_Fgq0h308EIpxO8ysm0EE92KGMggDmcpwkDMDvthWsvYme57a4GAIq0R-BLDajzmuLvqWutY_J7g6dx3dQcrvWE1IQxwBBPz46a4Tzc5BkvRHE3xX6GzYYgTciP-7PeoXxqFHNgVKtEHldZXnKTQIG_uCzjNwq3PKdnQwnv30EUGjmTIJooP1EUUck9qOKAKKCbJmo-6FPlPXD_dRd5ZO5vw7OWuG3OgkBgNO8hFEDquOELmN8P8rH5sLT9p3FUvdkGO1LCHd26y3bDGWrVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل کاتز، وزیر دفاع اسرائیل:
لامین یامال تصمیم گرفت با این حرکتش علیه اسرائیل یه جو بزرگ درست کنه و به تنش‌ها دامن بزنه.
کسایی که از این مدل رفتارها حمایت می‌کنن باید از خودشون بپرسن آیا این کار انسانی و اخلاقیه یا نه!؟
من به عنوان وزیر دفاع اسرائیل مقابل توهین به اسرائیل و مردم یهودی سکوت نمی‌کنم.
از باشگاه بارسلونا میخوام از این حواشی فاصله بگیره و اجازه هیچ‌گونه حمایتی از تروریسم رو نده
@AloSport</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120031" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120030">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
تعرفه سرویس های Vip
⭕️
✅
1 گیگابایت
⬅️
235/000 تومان
✅
3 گیگابایت
⬅️
735/000 تومان  استارلینک Vip
💫
🌟
⭐️
5 گیگابایت
⬅️
1/150/000 تومان
⭐️
10 گیگابایت
⬅️
2/350/000 تومان  ویژگی های سرویس های Vip :
❤️‍🔥
✅
متصل در تمامی دستگاه و اپراتور ها
✅
مناسب استفاده…
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/120030" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120029">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۵ ریشتر ساعت ۲۲:۲۹:۴۸ شامگاه پنجشنبه ۲۴ اردیبهشت حوالی قلعه قاضی در استان هرمزگان به وقوع پیوست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120029" target="_blank">📅 23:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120028">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
صاحب کمپانی حمل و نقل در انگلیس، یه ایرانی باشرف و میهن‌پرسته و برداشته تریلی های شرکتش رو با پرچم‌ شیروخورشید ایران مزین کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/120028" target="_blank">📅 23:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120027">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
آژیرها در کریات شمونه و اطراف آن به دلیل شلیک یک رگبار راکتی حزب‌الله از لبنان به صدا درآمده‌اند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120027" target="_blank">📅 23:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120026">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-UuACzudQI_SmOzBbtG2ymJcqmcYRGSbKzYmgNrIsFkIfWtmaeDnrFhLDnk8cNYIavIFVua9f6Lk4Jnw25oXjTqzR3VPK2rI_mqTTnF2UCp5lfX8-IgAjqhlH-O-t5IPuun3e9ETSbBva4Pby4sVSyI7nCC-vTjGvJDN8s2_9WSUBFuj0qMM7lCQtrQfTJgJxSjKBlOZYtBQzmT4aPxfwtxCP_Pywzx-oVqlgobfh_r09AvLVlQow4hRdGZVpuUDKaeLh4TGEri2PkWIhMbARLWRi9hFnGdX_nyNmeWjqa5x3qhRErC_h7O6CKa8L4QHnsPy6nPIVE2zSk2kO_4rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آژیرها در کریات شمونه و اطراف آن به دلیل شلیک یک رگبار راکتی حزب‌الله از لبنان به صدا درآمده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/120026" target="_blank">📅 23:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120025">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc9058515.mp4?token=HhYhFv4EKY7Tx_BXuCL8150QjQzIXXKlBx4bnRA-l3zTOIa1Z0ZjPwrJqKXPgfB27-qvbO9AyWMTQfisXoWLKEBP-IAbDm7DYAYQoDozPsCxsYp4niuGVZCoBEFl-XOtR7odLt4zj6P5SjPYK7fsRoirXskhsQKkFcgEiaev0A-DH_TJrLZh3dwp3C06jdhMPikFmsT2BbBC1VeW6q_d1wd-yXGhWpZUIp-tt_QIujMye_D6suyX7h1mMb5d2YP_zQoa3gwJlhNkw6NTokcelnZbb3o7q7WFdTZhCg2fx9R5K0Y5kOYkR2IHWcyU4BnvKoJqIy8Slvw5mbJ7vXRwCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc9058515.mp4?token=HhYhFv4EKY7Tx_BXuCL8150QjQzIXXKlBx4bnRA-l3zTOIa1Z0ZjPwrJqKXPgfB27-qvbO9AyWMTQfisXoWLKEBP-IAbDm7DYAYQoDozPsCxsYp4niuGVZCoBEFl-XOtR7odLt4zj6P5SjPYK7fsRoirXskhsQKkFcgEiaev0A-DH_TJrLZh3dwp3C06jdhMPikFmsT2BbBC1VeW6q_d1wd-yXGhWpZUIp-tt_QIujMye_D6suyX7h1mMb5d2YP_zQoa3gwJlhNkw6NTokcelnZbb3o7q7WFdTZhCg2fx9R5K0Y5kOYkR2IHWcyU4BnvKoJqIy8Slvw5mbJ7vXRwCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : در واقع، منطقه داره به بلوک اضافه می‌شه، ولی ما ورق رو برگردوندیم
🔴
یران از همیشه ضعیف‌تر شده و دولت اسرائیل از همیشه قوی‌تره
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/120025" target="_blank">📅 22:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120024">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b1f359ac.mp4?token=Qqu07UcqYdG6-CEJaLumrhxRcQnApd3vm3IRIasSi4jqJxkXKDszQJHLxr99rBiY6GeehtV2H_n0VoJN6FHOwLZ20SJtyQNz8mXHpS_dwkBm_FcfuZs55m43N0FRLoH6_chdKesTO5lPti00AlzCtGURYVcYzxjEJz53WyBc0r3iwEimyrqv0fZJfh1AqiLvzyNqC2g83O4PMsgimm0pMw0H8g0EC7KePH3zBk9tM7LVlEFY6JihA9rWWDYvr2RTU8WbF0e0BX9SOtgXaW6QP96QBE5BLyvsi0dVVBrPisClWtxEqJTdH4iXPcdFelDRDGELNezFoGaxaS3SEHewAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b1f359ac.mp4?token=Qqu07UcqYdG6-CEJaLumrhxRcQnApd3vm3IRIasSi4jqJxkXKDszQJHLxr99rBiY6GeehtV2H_n0VoJN6FHOwLZ20SJtyQNz8mXHpS_dwkBm_FcfuZs55m43N0FRLoH6_chdKesTO5lPti00AlzCtGURYVcYzxjEJz53WyBc0r3iwEimyrqv0fZJfh1AqiLvzyNqC2g83O4PMsgimm0pMw0H8g0EC7KePH3zBk9tM7LVlEFY6JihA9rWWDYvr2RTU8WbF0e0BX9SOtgXaW6QP96QBE5BLyvsi0dVVBrPisClWtxEqJTdH4iXPcdFelDRDGELNezFoGaxaS3SEHewAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : در واقع، منطقه داره به بلوک اضافه می‌شه، ولی ما ورق رو برگردوندیم
🔴
یران از همیشه ضعیف‌تر شده و دولت اسرائیل از همیشه قوی‌تره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/120024" target="_blank">📅 22:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120023">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-RpGzAogTN9Vfrg2Aab6lc0eOK2EUFfoJnqQCupUOYlR450n5X36cdkpNM3NGEEbpoynxg_8d52Ji5ivCW0Uxl5NI5UsZptGlswbMJeZL_pGARi9rQIuTofKtuAI_akIxSCC8ga4JKWBSpTAdY9Ap4vRT8uNjCXEjMBZdqIniWyOA84q2cxReoOhVBrK7mPYVVPhiCSR120hJEhHUl4iEA6nAERvfraCglRGvl339OOYTB7vosLJOk6rxzwoOTo3pMiuuev22HutvLMJEFS3Bek6uqjQolZm_2FkFBkb4PFhW94f4_XkBp-cYsQqBaW1qhlDyXp6VRO0pjpwc89sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارفعان نبیان ، جوان ۲۶ ساله اهل اصفهان، در جریان اعتراضات ضدحکومتی بازداشت شد.
🔴
خانواده‌اش بیش از دو ماه است که هیچ خبری از او ندارند، اجازه ملاقات به آنها داده نشده و او از حق دسترسی به وکیل محروم بوده است.
🔴
رژیم او را به اتهاماتی مانند محاربه (دشمنی با خدا) محکوم کرده که مجازات آن اعدام است.
🔴
گزارش‌ها حاکی از آن است که حکم اعدام او صادر شده و خطر اجرای آن با طناب دار بسیار جدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/120023" target="_blank">📅 22:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120022">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
به گزارش Ynet، آیزاک هرتزوگ، رئیس‌جمهور اسرائیل سفر هفته آینده خود به نیویورک را به دلیل «شرایط مانع از این سفر در این زمان» لغو کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/120022" target="_blank">📅 22:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120021">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقب‌های سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120021" target="_blank">📅 22:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120020">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقب‌های سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/120020" target="_blank">📅 22:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120019">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
خروج مرغ زنده از خوزستان ممنوع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/120019" target="_blank">📅 22:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120018">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
عزیزی، رئیس کمیسیون امنیت ملی:
پیش بینی کردیم که هرکس که ترامپ رو به هلاکت برسونه، 50 میلیون یورو پاداش دریافت کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120018" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120017">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⭕️
درک گفته های زنده یاد
فريدون فرخزاد
هنوز برای سه فاسد قابل فهم نيست!!!
🔴
حتما این ویدیو رو ببینید.
🤔
«مردی که ۵۰سال از زمان خودش جلوتر بود»
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/120017" target="_blank">📅 22:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120016">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
شبکه فاکس نیوز از استعفای فرمانده کل گشت مرزی آمریکا خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120016" target="_blank">📅 22:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120015">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل اشاره دارد که تکذیب سفر نتانیاهو از سوی مسئولان اماراتی‌ ناشی از ترس است؛ زیرا ابوظبی می‌ترسد به عنوان یک طرف در محور ضد ایران، ظاهر شود.
🔴
امارات در تلاش است است که سطح حضور خود را در مورد روابط با اسرائیل نسبتا پایین نگه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120015" target="_blank">📅 22:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120014">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ظهوریان، نماینده مجلس: بخش انرژی کشور ۱۴ میلیارد دلار خسارت دیده است
🔴
۸ میلیارد دلار بخش گاز آسیب دیده است
🔴
ظرفیت تولید گاز کاهش پیدا کرده
🔴
پخش پتروشیمی ۶ میلیارد دلار آسیب دیده است
🔴
بخش فولاد ۲.۷ میلیارد دلار آسیب دیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120014" target="_blank">📅 22:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120013">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نتانیاهو: اورشلیم را تحت حاکمیت اسرائیل برای همیشه حفظ خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120013" target="_blank">📅 22:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120012">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea891eb47.mp4?token=Ddh80i6UqmbzVeJj2O6t3g5fmm4oIyhEcprnbikp-j3D_OXsO_Qx6npr42txYsVEGT_1ABNEMU6fpOJVJq5clYU5lCY9zit_IrtRiKq9r2bk8oMsSZLJ5LrJXgMaf14JLCuY3H9VzhYa1NMpLqFUB5BsYYYhJzDCeJ2BboujcP6CtfDHdVWRNj6y3sCsDZWXV92sguTayvcjXFYO-igbjGO8k-ljQhdoutmNwvYbIz6INyI8n4IZLk15IGWa43bvn6O2WPBxnAiAGg89P3ML16U8LTm-u0pZipsjQM0V2BQFfhUuTwQ6sUP9I4-yoDjmJxxe34o0HmKjPtqgqUVXCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea891eb47.mp4?token=Ddh80i6UqmbzVeJj2O6t3g5fmm4oIyhEcprnbikp-j3D_OXsO_Qx6npr42txYsVEGT_1ABNEMU6fpOJVJq5clYU5lCY9zit_IrtRiKq9r2bk8oMsSZLJ5LrJXgMaf14JLCuY3H9VzhYa1NMpLqFUB5BsYYYhJzDCeJ2BboujcP6CtfDHdVWRNj6y3sCsDZWXV92sguTayvcjXFYO-igbjGO8k-ljQhdoutmNwvYbIz6INyI8n4IZLk15IGWa43bvn6O2WPBxnAiAGg89P3ML16U8LTm-u0pZipsjQM0V2BQFfhUuTwQ6sUP9I4-yoDjmJxxe34o0HmKjPtqgqUVXCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: دشمنان ما به دنبال نابودی همه ما هستند. همه ما.
🔴
آنها بین راست و چپ، سکولار و مذهبی، یهودی و عرب تفاوتی قائل نمی‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120012" target="_blank">📅 22:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120011">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تعرفه سرویس های Vip
⭕️
✅
1 گیگابایت
⬅️
235/000 تومان
✅
3 گیگابایت
⬅️
735/000 تومان
استارلینک Vip
💫
🌟
⭐️
5 گیگابایت
⬅️
1/150/000 تومان
⭐️
10 گیگابایت
⬅️
2/350/000 تومان
ویژگی های سرویس های Vip :
❤️‍🔥
✅
متصل در تمامی دستگاه و اپراتور ها
✅
مناسب استفاده روزمره در تمامی برنامه ها
✅
دارای ساب برای اطلاع لحظه ای باقیمانده
✅
تک لینک بدون نیاز به بروزرسانی های متعدد
✉️
پشتیبانی و خرید:
🔤
@safevpn_secureSupport
🤖
خرید فوری از ربات:
🔤
@SafeVPNXBot
📢
کانال اطلاع رسانی:
🔤
@safevpn_suportt
😍
کانال رضایت :
🔤
@safevpn_feedback
╚═════════════════════════╝</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/120011" target="_blank">📅 22:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120010">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
خبرگزاری ایسنا : با قیمت قطعی خودرو باید خداحافظی کنید،چون تو جدیدترین طرح فروش ایران‌خودرو و سایپا،خریداران باید نیمی از مبلغ خودرو رو امروز بپردازن بدون اینکه بدونن در زمان تحویل چه قیمتی در انتظارشونه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/120010" target="_blank">📅 22:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120009">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
اسرائیل معتقد است که رئیس‌جمهور ترامپ پس از بازگشت از سفر به چین تصمیم خواهد گرفت که آیا عملیات نظامی علیه ایران را از سر بگیرد یا خیر، طبق گزارش کان نیوز.
🔴
مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها شامل امکان حملات هدفمند آمریکا به زیرساخت‌های سوخت و انرژی ایران بود که هدف آن فشار آوردن به تهران برای بازگشت به مذاکرات و مجبور کردن به امتیازدهی در برنامه هسته‌ای‌اش است.
🔴
اسرائیل به واشنگتن اعلام کرده است که از از سرگیری عملیات نظامی علیه ایران حمایت می‌کند و معتقد است عملیات «شیر غران» خیلی زود پایان یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120009" target="_blank">📅 22:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120008">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be8ab919.mp4?token=H7s1q3LM9H0BUw2PWERF8Uhe91ZSFUBb6ZrwTT5xncNg5a0Uax4l8lpgBw2itpBjGvazivSHXI5thZGSVi_ya0xeFeR-2npg27lpqAZUJRWc8tvYJHf6YDF6upSFWlHFGoshn0z-S2_if9Qv8FXfqOkS02dlPvVsXuSCXLSX-pvCyby4stMbyVC8gQQpMj5AwgSOeAFiHNB6aHCXDBVXamhxGbz2lqhLIjstcjIuNylyGB_wkCUYvj46fUar49UrBK04k9Op-z_vGS44m8n0rOLU01c-dfOubG7KXFlN-OKlC2OZ26HdDiBTjh2gaHSiMQu886KrcTHRGbKR1KM42Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be8ab919.mp4?token=H7s1q3LM9H0BUw2PWERF8Uhe91ZSFUBb6ZrwTT5xncNg5a0Uax4l8lpgBw2itpBjGvazivSHXI5thZGSVi_ya0xeFeR-2npg27lpqAZUJRWc8tvYJHf6YDF6upSFWlHFGoshn0z-S2_if9Qv8FXfqOkS02dlPvVsXuSCXLSX-pvCyby4stMbyVC8gQQpMj5AwgSOeAFiHNB6aHCXDBVXamhxGbz2lqhLIjstcjIuNylyGB_wkCUYvj46fUar49UrBK04k9Op-z_vGS44m8n0rOLU01c-dfOubG7KXFlN-OKlC2OZ26HdDiBTjh2gaHSiMQu886KrcTHRGbKR1KM42Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید کاخ سفید تو ایکس : بازگشت قدرت آمریکا به صحنه جهانی
🇺🇸
🇨🇳
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/120008" target="_blank">📅 22:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120007">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
عراقچی: دنیا فهمید دیگر نباید سر به سر مردم ایران بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/120007" target="_blank">📅 21:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120006">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رویترز: آرامش فریبنده بازار نفت دوام نخواهد داشت
🔴
تحلیل‌های بازار نشان می‌دهد که ثبات نسبی فعلی در قیمت‌های جهانی نفت تنها سکوتی پیش از طوفان است و ریسک‌های ژئوپلیتیک به‌زودی نوسانات شدیدی را رقم خواهند زد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/120006" target="_blank">📅 21:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120005">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: ایران پنج شرط خود را برای مذاکره با واشنگتن اعلام کرد و میانجی پاکستانی آنها را [به آمریکا] رسانده است تا منتظر پاسخ آمریکا به این شروط باشد.
🔴
ممکن است برداشت اولیهٔ آمریکایی این باشد که اینها حداکثر سقف خواسته‌ها است.
🔴
تهران منتظر است که میانجی پاکستانی پاسخ کاخ سفید را بیاورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/120005" target="_blank">📅 21:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120004">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
تصویری از روسای جمهوری امریکا و چین در ضیافت شام
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/120004" target="_blank">📅 21:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120003">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بلومبرگ: ناامیدی و خشم مقامات سعودی و قطری از سرمایه گذاری در شرکت داماد ترامپ در پی وقوع جنگ و انتخاب گزینه اسرائیل توسط کوشنر
🔴
مشتریان عرب کوشنر همچنان احتمال همکاری‌های بیشتر با او را باز گذاشته‌اند، مشروط بر اینکه جنگ با توافق صلحی پایان یابد که برایشان قابل قبول باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/120003" target="_blank">📅 21:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120002">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajrqxuT0VV2VUGbAY6XQw6HvDrt47ONuIj-Fig3yi7QLuNse28T0QpxaB_87c0ZFTVrOGGxxDy1NuD38p_JPIeD4cbuiWQxNf7QPnbWRMgJ5RJ8DfhZ-a4tRRHdCkZ8W1JiR2uBI5ITJQp5VDTCN6VD62GEnVZOkY8aPqS45nhUxA1nx8cCnudqeRZFwvfxsI-g9ddTbiks2z_cEI5CKqYHC0oyQ2omig5TgWKIV7n2jE7zE_-7lFk5VqzvJaqKk3v7bKsKUftYlD3dupzCIeGr_ozJEuu88vYjSC5QKIf4xfJiq0_ESN3mE3Mv2GOibe2UUup1X4LIbHeOEre3CPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از روسای جمهوری امریکا و چین در ضیافت شام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/120002" target="_blank">📅 21:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120001">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سازمان بهداشت جهانی: نرخ مرگ و میر مرتبط با شیوع ویروس هانتا حدود ۲۷ درصد است و هیچ واکسن یا درمان خاصی برای ویروسی که می‌تواند باعث سندرم حاد تنفسی شدید شود، وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/120001" target="_blank">📅 21:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120000">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
الی کوهن، تو کانال ۱۲ اسرائیل : ایرانی‌ها داشتن سعی می‌کردن مکالمه‌هامون رو شنود کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/120000" target="_blank">📅 21:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119999">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/119999" target="_blank">📅 21:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119998">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/119998" target="_blank">📅 21:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119997">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/alonews/119997" target="_blank">📅 21:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119996">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b70acc0f.mp4?token=TUA_ry5zpY3eli0ZJzmzI8F7bwoppJ3Dcwy0CYX55hNPtOJatJlidDVBALleLj707chgBSgo6qCgZUcppNR8hABIKdJHQ2r4nK9c1Jnc68qLDcbjjLPJa0z_eHglPbsf__6Ev0rJJei6PCvB2BlKpA6OZmImJMo-tZmoDweZwQSkgOumaWlUYoqOpc_n_l2BAnphxGBhbVMLd_0bM2RMaraDA4YUN4l5-dn8o42hsW3IfL5tXVRNd0gvMU2CUG1SyVBYP-gr0ApUKdvN8Kuc0P7Jx7umXCLKBSNk8UFlBKcElPYmaiE-rrZe7sqbPchL7_cAIOgoyxdYyygJ7q_fyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b70acc0f.mp4?token=TUA_ry5zpY3eli0ZJzmzI8F7bwoppJ3Dcwy0CYX55hNPtOJatJlidDVBALleLj707chgBSgo6qCgZUcppNR8hABIKdJHQ2r4nK9c1Jnc68qLDcbjjLPJa0z_eHglPbsf__6Ev0rJJei6PCvB2BlKpA6OZmImJMo-tZmoDweZwQSkgOumaWlUYoqOpc_n_l2BAnphxGBhbVMLd_0bM2RMaraDA4YUN4l5-dn8o42hsW3IfL5tXVRNd0gvMU2CUG1SyVBYP-gr0ApUKdvN8Kuc0P7Jx7umXCLKBSNk8UFlBKcElPYmaiE-rrZe7sqbPchL7_cAIOgoyxdYyygJ7q_fyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس کانال ۱۴ اسرائیل: رژیم ایران به شدت به پول نیاز داره و در حال انجام تماس‌های مخفی و مستقیم با دولت ترامپه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119996" target="_blank">📅 21:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119995">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3TtHg7R614t8H3iK0Y57TzYCi4nn3tWeRWnuNfpt_AAuAdQ1Rb9Wb6hhvbdwlgieehrhm-iQCflrnPApgWBejDNnt-usmoXHLJ5k3WoL-QYwSm-JUzMAnPPk924yZ3_xk1dMm9qhmNmtNq_D-nnDwdIzU8Xcj1svqXszBikkoa7iU9d6w13TzhPAScynVS96RrG_6ecvTanRuY-uwxnqhfFprPuUJnqbUo-1pe8tXhrTaBqDh9iBwnE11qIF9bsudvzV1JH34ptAlOtfIPUUdkQR7pB1DGgdvAWgl-igoLYuKUWiXsfmEhQlU28J-jYoI9tKsixfndepMGZYNYHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: تشکیل دولت جدید به ریاست جناب آقای نخست وزیر علی الزیدی، و ابقای برادرم فواد حسین در جایگاه وزارت خارجه را تبریک می‌گویم
🔴
گسترش روابط برادرانه و دوستانه تهران-بغداد همواره در صدر اولویت‌های سیاست خارجی ما باقی خواهد ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/119995" target="_blank">📅 21:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119994">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8affe9b8.mp4?token=Q1LUsslc0kYWZsCLovtlOH92fJm20JDnfyvVsRLdQmr4Z3xogP1FW9wl1zztOGIgDQK5WWuvEgRt4ipR6OH6Wk3WpnX-UOBHVRtmBw3gwoVQtMq8vA8LsvCwz8JhFBk3MMH9DnnMSoJNyPemeXI-A_FsO9zzTtYf0TK55akUKYtcTcZD98zZNgMMNxSQMvMXqDmZf6pfAnX_OHnVAfW3SJ3hbom5Fgs4WfsVKXJzq-T3u7QWBuoQPqkqhqzD4V_IcrA3LTZkJQjfaWvDayCBOfeWtOPy4jR8ohYre23sJrLMLOiMxN7NVK_cGieQaSbNKhvJsUkFyGNWg0Yu9jTObg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8affe9b8.mp4?token=Q1LUsslc0kYWZsCLovtlOH92fJm20JDnfyvVsRLdQmr4Z3xogP1FW9wl1zztOGIgDQK5WWuvEgRt4ipR6OH6Wk3WpnX-UOBHVRtmBw3gwoVQtMq8vA8LsvCwz8JhFBk3MMH9DnnMSoJNyPemeXI-A_FsO9zzTtYf0TK55akUKYtcTcZD98zZNgMMNxSQMvMXqDmZf6pfAnX_OHnVAfW3SJ3hbom5Fgs4WfsVKXJzq-T3u7QWBuoQPqkqhqzD4V_IcrA3LTZkJQjfaWvDayCBOfeWtOPy4jR8ohYre23sJrLMLOiMxN7NVK_cGieQaSbNKhvJsUkFyGNWg0Yu9jTObg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش عراقچی به دست دراز کردن خانم وزیر خارجه ویتنام در اجلاس وزرای خارجه بریکس در هند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/119994" target="_blank">📅 21:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119993">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
اوکراین پهپادهایی را به مناطق کورسک و بریانسک روسیه به سمت مسکو پرتاب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119993" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119992">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR8pRUUfqyan9PlJAQU2ktICQ1EyzHfkE5lwmxaffo-3lZ3K4tbMofDhEBF9UjL0SYD8jQEbAIVLTfxQBIedxfbPUZKH0eo8osOvUa0PKfdQc5woO-H9U7Y-xe24zBtstngbSmWszD9KzJ5jkN5mmR1fJVWkXFpKpfP6rI13tw3tMkBq_bt7y83o6nw9ZZjX4sdf2XNs81co9DicEw1XFb3laWKT9IwIXaz4uah4_tEe9DuNQTKx1euNNXKHF-yMGFOsMhttptmoAg-OWzID0lWSfjN5Dz_plVE-Br6DBV981ShPT3fsSopKvyxTcR2oNWB0HrJvnCbymWpVz3o8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عراقچی و وزیر خارجه مصر در حاشیه  نشست وزرای امور خارجه بریکس در دهلی‌نو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119992" target="_blank">📅 20:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119988">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGdP7gvau53Vd7BR2MsY_dxRLFh1TvrHNGanf7i9LIIXF9H5entH_sUvPRMSE19vnpixMD-T0w5_3CaUYk6EU8uriIbRR4YtRiNQ4ANPEcWfCBguj-rYIMhsF2ckcBxZXDmw0sJpJUx04TW6dSa2fhm9c9KQR5QtKnQbBvABsorzx78UxCdxqjcM2bOFUnusFU1aaXt9eNcwOF-nzEFTy8vvpdExr6wInUfhnAaGmvH9qB30_s7jZhtIXT5bIJfctaJRj_WChRq4tmWbVxMtClj2N6wFHGxHwlRxdxHbtf-cONIw7toPl6U4mimj0fUCyrAxyr5DovQbL0D0GkFZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ux8gOdCK2RYzSr5PVEI5HnTrgZtgu7qn7JCK0UzK2-stEcF9MxW0H9uYRtoppF89lJzer_PKgilJWvaE2k3_4Ba1gBYH6LFCyPLKDm2HKShyw1apxtGrGkEqryobnVQwPU9spfHb4XoRptcY7kawsPoebaPi2aJi4aC3AbDWw4CmPXpGOXY_8GMp6S7lC0-4qEdi76xrER9WayxqqTqGnTlTBsPuWwQ5C56QfSTUfeg7aYjsisJBW3g7XPE2PqRXIcMLktYFx8rAzooSfzKJn6APQvxLdJGZ9ZId03UcWqSnORGEOCWTLMYG1hF_iPxWMTW7brD-HOW_XXg023CmHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ljnmr1Dg5AK7gEYYmretoGRzNu4LAKIeA0F43cdYg7yGSfLAS0b_f2RpFwWH9-Tj65fsl1FI6zdrt7MKTpxIBqjEGa-BEllBVF7CzMMZ-45An9fAcUQYRC8_CRrJzkZn1PFqZoAUKmXgeI89gxzOb3SMQWOT6NFIY_KAy5akpJwmAcauLJxG2W1YDctoMoQtKK3-QnbJ-vCL0rf0NwXrSXUeCwuVdcKyIOOfs4y5D624VBIP5GDhl5Z-mQk5Whpqdsk2WMnHmhjwZaYlVUF233JjYmpRY1rysQsycy-1KuqLZiXaBKQyycrckzrZBsQ1nLrzoFYBIenWj8A4fBBjPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6WFEgknuStxE_4HmYwvJ6vkM2Xxqt8GYGQCF4v3VIuLaYuVSaf_e8zlzrNNTFUEfhRFeXpNE1_ubreYef_LdtMEy4ODQbKmoOWgGAiuHb7ToljO8jDbXUMggr5FVkjGmVrktAxQTkpRrPzwNqWxwZvo742OEgN3gCA9y_sM2CbBKXPVsJ-lnpwchMHd3vTIuUZCAe0Ct5vCw2-Jhsg95RU3pOi1NOYOLdEnvtswl0bXaP6OPWK4dTqrRG1ChvhsBd_J9H9jNe0fRLZSCFhOpyVSN2C5H2c3knmcPKh9FOnqhiD4B3tjbzBn_LpOQ-hyLmAXBiKvVL1wsKyR5Ah1Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اسرائیل شروع به توزیع توری‌های ضد پهپاد به نیروها در لبنان کرده است، به طوری که تقریباً ۱۵۸٬۰۰۰ متر مربع تاکنون توزیع شده و ۱۸۸٬۰۰۰ متر مربع دیگر در حال خرید است، طبق گزارش کانال ۱۵
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119988" target="_blank">📅 20:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119987">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
کانال 12 عبری: اسرائیل سطح هشدار خود را به بالاترین حد ممکن افزایش می‌دهد تا برای احتمال جنگی تازه با ایران پس از بازگشت ترامپ از چین آماده شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119987" target="_blank">📅 20:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119986">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
واشنگتن پست: چین از جنگ آمریکا علیه ایران برای تقویت روابط با کشورهایی مانند تایلند، استرالیا و فیلیپین، با ارائه سوخت و فناوری سبز، استفاده می‌کند، آن هم در زمانی که به نظر می‌رسد دولت ترامپ علاقه کمتری به رهبری تلاش‌های بین‌المللی برای مقابله با بحران جهانی انرژی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119986" target="_blank">📅 20:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119985">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
روبیو، وزیر امور خارجه آمریکا : ترامپ از رئیس جمهور چین کمکی نخواست، آمریکا به کمک چین نیازی نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/119985" target="_blank">📅 20:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119984">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb1a1c79f8.mp4?token=SMm-VTCSNA1bSqmlDc6_ILBHW0GOxrSevnuCnjot5G7N1WET9wYJecV-Z8tcirI8rj-LWWXWco3rZSRgEEWcWVNxzWRrN11F3NnI3x2u78SSvohuJQjdN4y8Ute2ZnE0orTcrj5fkQRQsJGpDLhkCeyLPUiOOqoMhOBSIRv_fQ2eEp9uSet5BZ_AY_6VL-Ea64AsyqnxX29S7xd-VUZ7GCuv6Lkk_l0AaqFOxFvpLyClpy15kg8BrRxkD_oUWKgw-wc-5bbiRMhOXW6l9KYeOIiayv36xXaIgK5_ZJFdrwsXp-BjmSxQf3akfOqpjm_MFvB5VBtAkjSTgWDMRCNhsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb1a1c79f8.mp4?token=SMm-VTCSNA1bSqmlDc6_ILBHW0GOxrSevnuCnjot5G7N1WET9wYJecV-Z8tcirI8rj-LWWXWco3rZSRgEEWcWVNxzWRrN11F3NnI3x2u78SSvohuJQjdN4y8Ute2ZnE0orTcrj5fkQRQsJGpDLhkCeyLPUiOOqoMhOBSIRv_fQ2eEp9uSet5BZ_AY_6VL-Ea64AsyqnxX29S7xd-VUZ7GCuv6Lkk_l0AaqFOxFvpLyClpy15kg8BrRxkD_oUWKgw-wc-5bbiRMhOXW6l9KYeOIiayv36xXaIgK5_ZJFdrwsXp-BjmSxQf3akfOqpjm_MFvB5VBtAkjSTgWDMRCNhsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله دو سرباز اسرائیلی رو که داشتن فرار میکردن هدف گرفت و با پهپاد کُشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119984" target="_blank">📅 20:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119983">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گزارش واشنگتن پست از یک ارزیابی اطلاعاتی محرمانه ایالات متحده: چین در نتیجه جنگ جاری آمریکا با ایران، در زمینه های نظامی، اقتصادی، دیپلماتیک و رسانه ای، دستاوردهای استراتژیک گسترده‌ای را به هزینه ایالات متحده به دست می آورد ، در حالی که نگرانی فزاینده‌ای در وزارت دفاع ایالات متحده در مورد پیامدهای ژئوپلیتیکی این درگیری وجود دارد
🔴
پکن از جنگ با ایران برای تقویت جایگاه بین‌المللی خود استفاده کرد، در حالی که واشنگتن بخش قابل توجهی از قابلیت‌های نظامی و اقتصادی خود را از بین برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/119983" target="_blank">📅 20:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119982">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119982" target="_blank">📅 20:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119981">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o33P6VihoKkKs2O8gXOiqNgw_mh3soIDoMYQ7GlrFkpJ3P-ZA0Zbzz6G-yaj4O2OgQ30GqaFOC00tKpu1FIafdwsep6ScOcXUz6Lm6vM2CWNfu1JqXl2NYVsHC5Cl8xZEwEjdh6qt_tNNpVWypcnWnvEhYEWRgYt4QrvQRW11lTDwbp7Pe58QKy2ybwUvIiwAKcMSQtVSRAZVU6mND7J5O1bPbYnxwiTNoAASv--EjsdKb91iMxtHfHxxGNnm6xPMS-UpwOfpx3ycU22g8LFNTCWpP6XxqoHgd45wqKQKc0YzfH4vtjPzoLGbO6Tnu4VkPpBp4mjfcn24gZvQ2WbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray استارلینک
🗯
گیگی
150,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید پیام بدین :
@v2safeBot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119981" target="_blank">📅 20:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119980">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان: اسلام‌آباد از نقش چین در میانجی‌گری برای حل‌وفصل تنش‌ها میان ایران و آمریکا حمایت می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/119980" target="_blank">📅 20:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119979">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
واردات نفت خام آمریکا از ونزوئلا در هفته گذشته به بالاترین حد خود در هفت سال گذشته رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119979" target="_blank">📅 20:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119978">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر دفاع بریتانیا : بعد از این‌که روسیه حملات سنگینی به اوکراین کرده
🔴
قراره ارسال سامانه‌های پدافند هوایی به کی‌یف رو سریع‌تر انجام بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119978" target="_blank">📅 20:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119977">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ایالات متحده موفق شد اورانیوم بسیار غنی شده را از رآکتور هسته ای برای اهداف تحقیقاتی در ونزوئلا خارج کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119977" target="_blank">📅 20:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119976">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شبکه MS NOW: شرکت‌های خصوصی چینی در حال بررسی فروش موشک‌های ضدهوایی به ایران هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/119976" target="_blank">📅 19:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119975">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رونگ هوان»، فعال رسانه‌ای و تحلیلگر سیاسی چینی، تأکید کرد که پکن مناسب‌ترین و توانمندترین طرف برای ایفای نقش میانجیگری فعال بین واشنگتن و تهران است
🔴
او اشاره کرد که بهبود روابط چین و آمریکا در ماه‌های اخیر، افق‌های جدیدی را برای ترغیب دو طرف به بازگشت به میز مذاکرات مستقیم گشوده است.
🔴
این تحلیلگر سیاسی توضیح داد که منطقه در وضعیت تنش‌آفرینی متقابلی به سر می‌برد که نیازمند ابتکاری از سوی چین است تا نردبان کاهش تنش را فراهم آورد که آبروی هر دو طرف حفظ شود و به وضعیت بی‌ثباتی که به ضرر منافع همگان است، پایان دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/119975" target="_blank">📅 19:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119974">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
برد کوپر: ما درگیر اقدامات خصمانه علیه ایران نیستیم، بلکه آتش بس داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119974" target="_blank">📅 19:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119973">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر جنگ پیت هگستث: با وجود آنچه ممکن است در رسانه‌ها بشنوید، آمریکا در حال افول نیست. ما همچنان قوی‌ترین قدرت نظامی روی زمین هستیم، اما این قدرت نیاز به تجدید دارد.
🔴
با تهدیدات جهانی که به طور مداوم در حال تحول هستند، زمان آن رسیده است که سرمایه‌گذاری ۱.۵ تریلیون دلاری، یک پیش‌پرداخت نسلی، انجام شود.
🔴
این سرمایه‌گذاری تضمین می‌کند که ایالات متحده برای نسل‌های آینده قدرت غالب و بازدارندگی بی‌نظیر در برابر هر دشمنی را حفظ کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/119973" target="_blank">📅 19:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119972">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ایلان ماسک درباره مذاکرات آمریکا و چین : من حس خوبی نسبت به این مذاکرات دارم. فکر می‌کنم نتیجه خوبی حاصل شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119972" target="_blank">📅 19:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119971">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ : چین موافقت کرده ۲۰۰ هواپیمای بوئینگ خریداری کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119971" target="_blank">📅 19:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119970">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCmDdBgL7eVn4GlcV3cnxW5kwM44n0tpSjNSautCfPJ64M9dbVMaXCx_D5O2JSrkXUNTW44WvijqfIeidkO6AHpE5tqoj1RNlVZNrVVmkQCixZN3TL1XpxtkrXDEMwT_v1XWeEHNKPBKWK1xxp-61mglAQhDGoZjqxHuRncEtNzIFEUql1ZB_s5_B-H9uVtqWAYA84Rs8Pq6LSk8rkEBovBazA3Kt-pnMmjfLNjzhoZgxLOPrUR3EfocquMuW5qScfGU5EWezW3sR-_64k4E2VbLMdW1R_aFmw0SVYBp_TuDdws66of6oahuyDojB5PEKXWKn6gsvWSnBhUvBx8Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برونو رودریگز وزیر امور خارجه کوبا در شبکه ایکس اعلام کرد که آماده است پیشنهاد کمک ۱۰۰ میلیون دلاری ایالات متحده را بررسی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/119970" target="_blank">📅 19:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119969">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
دولت کوبا اعلام کرده است که جزیره رسماً بدون سوخت است و انتظار دارد سیستم انرژی در روزهای آینده فروپاشی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119969" target="_blank">📅 19:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119968">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
مجلس نمایندگان عراق با اکثریت مطلق آرا، فؤاد حسین را به عنوان وزیر خارجه در دولت جدید تأیید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/119968" target="_blank">📅 19:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119967">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6ffb480d.mp4?token=tvIyRJ2sRRvI1luhEQRpeMlhRoEt01wEdmsBa1gH4PNQgsxt6hE0OTVxFPT8c4oR5qP1X0e5V2hSNHoprIFi_9Ulpmc7uGBpYQb8bQyuHbn49LYoPUqvSjjcqTYXIetgK0G3uHypL-zpo8BWRjdUHelG-MX57DDpavCw9ADRdHOpnZ9eltz-FH1b40OT63hh2D8V-m_DPmFkUKsW0TUzFd_fUVN1EtLrFXxWXINfIGzDRlLUyeSo-Gs-BPL7zPT8QPONMfF7l8jclUip-ZZcvKt836iWTN4Nvs0kLJWFiWtLonXmd-Aj0GkIKnh8t6_MqSGV2O2uSixVmLalIlAM9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6ffb480d.mp4?token=tvIyRJ2sRRvI1luhEQRpeMlhRoEt01wEdmsBa1gH4PNQgsxt6hE0OTVxFPT8c4oR5qP1X0e5V2hSNHoprIFi_9Ulpmc7uGBpYQb8bQyuHbn49LYoPUqvSjjcqTYXIetgK0G3uHypL-zpo8BWRjdUHelG-MX57DDpavCw9ADRdHOpnZ9eltz-FH1b40OT63hh2D8V-m_DPmFkUKsW0TUzFd_fUVN1EtLrFXxWXINfIGzDRlLUyeSo-Gs-BPL7zPT8QPONMfF7l8jclUip-ZZcvKt836iWTN4Nvs0kLJWFiWtLonXmd-Aj0GkIKnh8t6_MqSGV2O2uSixVmLalIlAM9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ان‌بی‌سی: آیا رئیس‌جمهور شی از رئیس‌جمهور ترامپ خواسته است که به تایوان سلاح نفروشد؟
🔴
مارکو روبیو: خب، این موضوع قبلاً مورد بحث قرار گرفته است. این موضوع در بحث امروز به طور عمده مطرح نشد. ما قبلاً موضع آن‌ها را در این باره می‌دانیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119967" target="_blank">📅 19:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119966">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
عراقچی: امارات در حملات به ایران شریک فعال بوده است
🔴
ایران در برابر تهدیدها محکم ایستاده و سر خم نمی‌کند. آن‌ها این مسئله را دیده و تجربه کرده‌اند
🔴
در عین حال، کسانی که با زبان احترام با ایران سخن بگویند، با همان زبان پاسخ خواهند گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119966" target="_blank">📅 19:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119965">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سنتکام: امارات، بحرین، عربستان، کویت، اردن و اسرائیل در عملیات آمریکا شرکت کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119965" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119964">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ : هر کشوری که این مقدار نفت بخرد، بدیهی است که نوعی رابطه دارد، اما او دوست دارد تنگه هرمز باز بماند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/119964" target="_blank">📅 19:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119963">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سناتور کنگره خطاب به برد کوپر:
شما میدونستید ایران تنگه هرمز رو میبنده؟
🔴
برد کوپر: همه احتمالات در نظر گرفته شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/119963" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119962">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
میدل ایست نیوز : پارلمان عراق به برنامه دولت علی الزیدی رای داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119962" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119961">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ : رئیس‌جمهور شی علاقه‌منده که درباره ایران به توافق برسه، اون گفت : اگه بتونم کمکی بکنم، حاضرم کمک کنم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119961" target="_blank">📅 18:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119960">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
هانیتی از فاکس: آیا درباره حمایت چین از ایران با شی صحبت کردید؟
🔴
ترامپ: او گفت که تجهیزات نظامی نخواهد داد. این یک بیانیه بزرگ است.
🔴
اما در عین حال، گفت که آنها مقدار زیادی نفت از آنجا می‌خرند و دوست دارند این کار را ادامه دهند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119960" target="_blank">📅 18:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119959">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مارکو روبیو: نیروهای مسلح اوکراین در حال حاضر قوی ترین و قدرتمندترین نیروهای مسلح در تمام اروپا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/119959" target="_blank">📅 18:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119958">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a2ffaa67.mp4?token=RalWm9-86kP83Q8qUdzulyDbvvYHeDnoIeVdHEWFttYlLR76NBrAYn-Cq_pkw1X9ITINxRehtrG3FdbqBmdF-xporS6JCUx2ooz6AAZ8yinufLT_qXSMLemhFM_l3cmmo7BV-BmyZQhlAL64uPJHKWI23vz1AgntIPDBkNCOn_J5tCz2X3HhlDpjUHYSFcLlJ9x1qJI-qsdtuE03NjsE2UeNDwR-BK5rpujymWFLHNMcYT8UA1I545zMuHCU-0PsuxXFxyTttok1RECJr_kcn6cGcVmY7zNA9-_JgIYFHWwBLRLLfDk-PHZC1H7IE0UsCvYqSlM01WJpIkE6fCl1_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a2ffaa67.mp4?token=RalWm9-86kP83Q8qUdzulyDbvvYHeDnoIeVdHEWFttYlLR76NBrAYn-Cq_pkw1X9ITINxRehtrG3FdbqBmdF-xporS6JCUx2ooz6AAZ8yinufLT_qXSMLemhFM_l3cmmo7BV-BmyZQhlAL64uPJHKWI23vz1AgntIPDBkNCOn_J5tCz2X3HhlDpjUHYSFcLlJ9x1qJI-qsdtuE03NjsE2UeNDwR-BK5rpujymWFLHNMcYT8UA1I545zMuHCU-0PsuxXFxyTttok1RECJr_kcn6cGcVmY7zNA9-_JgIYFHWwBLRLLfDk-PHZC1H7IE0UsCvYqSlM01WJpIkE6fCl1_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هانیتی از فاکس: آیا درباره حمایت چین از ایران با شی صحبت کردید؟
🔴
ترامپ: او گفت که تجهیزات نظامی نخواهد داد. این یک بیانیه بزرگ است.
🔴
اما در عین حال، گفت که آنها مقدار زیادی نفت از آنجا می‌خرند و دوست دارند این کار را ادامه دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119958" target="_blank">📅 18:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119957">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
برد کوپر: فرماندهی مرکزی ایالات متحده در پاسخ مستقیم به تهدیدات جمهوری اسلامی ایران ایجاد شد.
🔴
طی ۴۷ سال، رژیم ایران منطقه را به وحشت انداخته و خصومت با آمریکا را به یکی از اصول اصلی حکومت خود تبدیل کرده است.
🔴
سوابق خصمانه و مرگبار آنها علیه آمریکا به خوبی مستند شده است.
🔴
در کمتر از ۴۰ روز، نیروهای سنتکام به اهداف نظامی خود دست یافتند. با نابودی ۹۰٪ از پایه صنعتی دفاعی ایران، این کشور برای سال‌ها قادر به بازسازی آن سلاح‌ها نخواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119957" target="_blank">📅 18:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119956">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
برد کوپر: توانایی ایران به‌طور قابل توجهی ضعیف‌تر شده؛ اگه بخوام از تجربه خودم بگم، تو حدود صدبار عبور از تنگه هرمز معمولاً باید ۲۰ تا ۴۰ قایق تندرو می‌دیدی ولی این روزها فقط ۲ یا ۳ تا می‌بینیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119956" target="_blank">📅 18:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119955">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
برد کوپر فرمانده سنتکام: توانمندی‌های موشکی، دریایی، پهپادی و صنعتی ایران ۹۰ درصد تضعیف شده است. او افزود که نیروی دریایی ایران تا یک نسل دیگر نیز به سطحی که پیش از جنگ در اختیار داشت باز نخواهد گشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/119955" target="_blank">📅 18:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119954">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0lqNCryX_rNnEaBgAg4cjOWDXKmcKTi-hKmhSldgUDH23I_wfD36TrpZNiRqhJQVXe3xfm0EEPhbLimjrX3-SIF0R4Gn7465arESpP5Cc8x8pH_YpxDanErpMm-LMzX87EolzowhZiwaKj7Zmvo39js_T8YiFAQDrqJrZjNh1Wsj96b8nMXCxAr1u-wnPJ50y6HC2LOxhc7gSHZeLPz8DEYVc1sl3pSHl52p1oUtcY1Nr088xfT08Vj3p-EzHshTAN1HhBp8RwRe5keMVvxW1ILPD9WJlQMPel-kEjBy7gxodjm8fQ5LV1wNAmTlk2NKHYDrYR11DkOKwrzXBQiKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: از فداکاری و ایثار مردم سپاسگزارم، با همدیگه ایران رو میسازیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119954" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119953">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فرمانده سنتکام، دریاسالار برد کوپر: امروز، حماس، حزب‌الله و حوثی‌ها همه از تأمین سلاح و حمایت‌های ایران قطع شده‌اند.
🔴
این نتیجه از پیش تعیین‌شده نبود و نه به شانس به دست آمده است. این حاصل ماه‌ها برنامه‌ریزی دقیق و بر پایه دهه‌ها تجربه است. این نتایج همچنین…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119953" target="_blank">📅 18:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119952">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
منابع خبری می‌گویند کشتی باری هندی که روز گذشته به مقصد شارجه در حرکت بوده در تنگه هرمز هدف قرار گرفته و غرق شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119952" target="_blank">📅 18:04 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
