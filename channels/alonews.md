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
<img src="https://cdn4.telesco.pe/file/mztGlRduPcyRrBtusGH3aFM4QE7rNKfGZjDoFiqsmdhof-GTreXVrleH02dbLeAXBcTbYvEsjpiMxAjY65qdRVzC-wy2tsPngoLZdkKBnpXg7XdOS0mRRJ-NHk0xXK_xETHnUYlFZ-isTGKtc2Wh9eDWZpkLSXcG22-QpOuVxWk--L5VaHLTLPS1x6yycXU-yLkpPIW-EG9sMSsCNa5cQYM4BQFn7rxxa8mfmHLbZGZH3hRUsCqrhnkHZrx6VCHnvyTAFFYrXSnUz3WfmY68Q2u1PgCNg7xC4nNW4Tj5Y6Il1Q4pCfuqpLZWlm9PeykVnWKxbaWe8TKM4CNFNzmTXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 20:29:13</div>
<hr>

<div class="tg-post" id="msg-130552">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjJMQKCGyFEVk1Ae1QiIkFtE98POGAEGiu2XcYQmLi86GhoYadJCHrkVkKF8i03GqSiE1RT1e7UYqef9N8K7c6ouUBIfNTJiZYHDSL8fiovyE24dB-FWOErBRsqm3jDpYuxQ-AxKVci4JjIbNi9437Z_n47kGN9KaUrELP8KkIENOnYxp5hYYsT7F3l1k4dQXFzEb0MENilhUSfOTTJSwDIXqQxaG7UExojrsHA3h6fRTU8ajZM-2LkZ-aa_shvOupT2oPznUN08yT1B5rtu-hALggJyPHw7MeRgdXdDmqNwQei1DLsQuXwX8EjPun8MQkM9KLcS4kjqFgVj5J4QiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره:اختلاف تهران واشنگتن بر سر تنگه هرمز بالا گرفت
🔴
اکنون شاهد آن هستیم که ایران و ایالات متحده در تفسیر مفاد یادداشت تفاهم با یکدیگر اختلاف دارند؛ اختلافی که به‌طور فزاینده تنگه هرمز را به اصلی‌ترین نقطه اختلاف میان دو طرف تبدیل کرده است.
🔴
دو بیانیه اخیر ازجمله بیانیه سپاه مبنی بر نقض ماده ۵ یادداشت تفاهم درباره بازگشایی تنگه هرمز و همچنین بیانیه وزارت خارجه مبنی بر نقض ماده ۱ یادداشت تفاهم درباره توقف فوری درگیری‌ها، شواهد این مدعا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/130552" target="_blank">📅 20:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130551">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a598c8e4.mp4?token=BxgxzdQLX1pd5EKxG1ePAi7CiFSDCeH2y_Uv8OZvWm1jyWGiVHoBQgx090FZ-JTDpXxKaQSVLoezkYDjnRKhy0FNuC4b4UnUYvPnQFEde2W9Wt8p-qOZ0BENYgS8Gy3zdgZBA1TmVeu20XWWCNamzQ-GW4U2OR6LilTH2qTzh0kW9K3qzjWommc2oycFRKWSYC5gLkAguMERjXw4wLqA627xwlGMhE0Ndo7FWOZno7yjyz9DNgpBQbsEItd2nKRBSIlcy4J-jzsBuBOWrd9nTeVzzueDEcxBaFIHfIcZooJhTbC6ZRF_lkRXQxDew5gSp2GdQk3oZEjB6g8YoYiDSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a598c8e4.mp4?token=BxgxzdQLX1pd5EKxG1ePAi7CiFSDCeH2y_Uv8OZvWm1jyWGiVHoBQgx090FZ-JTDpXxKaQSVLoezkYDjnRKhy0FNuC4b4UnUYvPnQFEde2W9Wt8p-qOZ0BENYgS8Gy3zdgZBA1TmVeu20XWWCNamzQ-GW4U2OR6LilTH2qTzh0kW9K3qzjWommc2oycFRKWSYC5gLkAguMERjXw4wLqA627xwlGMhE0Ndo7FWOZno7yjyz9DNgpBQbsEItd2nKRBSIlcy4J-jzsBuBOWrd9nTeVzzueDEcxBaFIHfIcZooJhTbC6ZRF_lkRXQxDew5gSp2GdQk3oZEjB6g8YoYiDSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیامدها در نبطیه الفوقا، جنوب لبنان، پس از حملات هوایی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/alonews/130551" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130550">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKd5bnGbw_hSYiauWjtKuj8qNM4pnrvP_mlAf4q07-TrcwBamc-bKF4Z-iBevWliM6woiTn1wBfRUXtZp3oVSPrSdEfc0vcCDCDoNBo1tw-L3dj0gb-MiJ0yIy1XakymWQFrAxuIWT-44YsBDl0KCxTfJPVkBV_GZazEFYmsaQMXGx4uFTUqxmNDFLxsy_oemue344xv7dx-qDL4KgWZaJtZcxrs9YI2_Z715nBlc-OGz1DpxPm_Ql5sES9xD9BVZP7Iv1I6yTMccfSA-T7kBtM9mgM1nLyjLtADuIj_L-xeYISm57EfdY3D5hVAJE0H_wzyZ0R5rzp_8xlg1w82Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/alonews/130550" target="_blank">📅 20:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130549">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8nDJ-fvoi8xAYRBlKfo4Gv6fbu2E1_1o1m2cqPtI9DhWOQm0oS42kJe5vGneEY-oJOHsw9_zW83ABUC0tTpZxacAQwkpQmMYOjIiKhqD4EJUxEWV-C20N1S2EZkH2MT6DaleTx4XR2jLo1mq2IUcIGnpqk4Ssgh-aLDRPO2BMeynpWKOlpB1TohP6tl-0pOY1gPqfvEAxu4BBGstxecHO-Vr88eFvZTjq8zDu9XEM7lDSiqdfqIrFhBf5mYcCdCawb6G8KuzKKRWNgpgLNh5_OUpoXm5kQI6D_xd6HN3sBbISXLGNzvk5WUxUXCwwAUrkAXKPcgMLp59W-ZQhs3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پلاکارد در تجمعات شبانه که نوشته ما گشنه میمونیم و یه نون رو ۹۰میلیون نفری میخوریم
🔴
پ.ن: شما از جانب ۹۰میلیون نفر شکر نخور آدم توهمی
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/130549" target="_blank">📅 20:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130548">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T46HV2brET9hkcuRaJPr-Sk1tjtyzlZruZ5dpmXHFpyPHSp9KBut4Lu5d3j8qm-4uLIdKZtuAfuYi_gxLMlPqPUy63DeKsQzYHv72nNpFLmRjZR_fm-2PI8U_X0c7GD9FxozsquJsXv9Vhf9hsuSt2nASEHfj1tjzbp1Kbn9WdJ1j5GIbKR8h7Nt-u-wIdWvYEMZv4iA0VVmXHQJyRwjHZTlksG-8QgqSO8LuBpGbBxoS_Ck12hWCZnlARsGQUhQjTmImTytYCAkd0Aya0KmnMT6aApbto-ydj0NfGnTkYUwO5SVOrxVYDHZh_smnUlzG0xaA6rIGWcZtWhtcFU0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب صداوسیما کلی تلاش و سانسور کرد که پرچم رنگارنگ LGBT رو‌نشون نده، بعد رنگارنگ برای اولین بار تبلیغ تلویزیونیش رو دقیقا توی این بازی پخش کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/130548" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130547">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
پروازهای رامسر به شیراز، مشهد و بغداد برقرار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/130547" target="_blank">📅 20:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130546">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449c854e01.mp4?token=qz1AL1meo8nyb0UHHUAYS0tw5-TFY1RrmnysqNm3aZrpsQtZ7UYWqK0c2nQL7FbTNbi1CgomFTRkqXiMg3qC9XqwIRlMyOvYxQh2le7cNHb__6DCu94tL7vzNO2qCnisz1RFcIl3yfUIM25a_M6NBggyUtJiKxb1x0aazlRiSAGbzml8Z77vDNnPy5NDCB2E3n2ZFZUqgFIniadX3XNbqpke2ozeD2kULiajUOF5A58EgaR7kQzCwxR8cBPE-hkqaa5xgdV6CKPCYNRitPA9x9KLgRtHfqM36OGbn3YUPPrdmZ2OwP7pnVw0wbrgetG5pxH0BEIJh_-CZu9ucpPbFwaUEUshVvPmptAjDOU7X1zGKtDHrfn0tdb53_uEX1OswnZ_cfdjYTD5BcyKgZWJxzxhyXKtBIw9-nLVBgeU6FFeWBFwJrwpMXqeQaqZrHftAhAdahUfn4zbl8IJ07nrwXjXAeTX5HXV5O9d7hXYe5_AURf1ttV1nvqLPOwnpwr3CxWriDkKnFeYigYN-0VuwF4yacP3TN5nKwueTxvXQHq_V6m62ispMRVT3b1g-EL2qlFs-lmogw2HfqXSjHKqNel_FztOAYhKsJ5p7eHzbIzOTtxJSwbWUzrSD0BYpLR1ef5qxQkc3p_M8G47u_xdFff1efw0j2dGASeYtsquRxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449c854e01.mp4?token=qz1AL1meo8nyb0UHHUAYS0tw5-TFY1RrmnysqNm3aZrpsQtZ7UYWqK0c2nQL7FbTNbi1CgomFTRkqXiMg3qC9XqwIRlMyOvYxQh2le7cNHb__6DCu94tL7vzNO2qCnisz1RFcIl3yfUIM25a_M6NBggyUtJiKxb1x0aazlRiSAGbzml8Z77vDNnPy5NDCB2E3n2ZFZUqgFIniadX3XNbqpke2ozeD2kULiajUOF5A58EgaR7kQzCwxR8cBPE-hkqaa5xgdV6CKPCYNRitPA9x9KLgRtHfqM36OGbn3YUPPrdmZ2OwP7pnVw0wbrgetG5pxH0BEIJh_-CZu9ucpPbFwaUEUshVvPmptAjDOU7X1zGKtDHrfn0tdb53_uEX1OswnZ_cfdjYTD5BcyKgZWJxzxhyXKtBIw9-nLVBgeU6FFeWBFwJrwpMXqeQaqZrHftAhAdahUfn4zbl8IJ07nrwXjXAeTX5HXV5O9d7hXYe5_AURf1ttV1nvqLPOwnpwr3CxWriDkKnFeYigYN-0VuwF4yacP3TN5nKwueTxvXQHq_V6m62ispMRVT3b1g-EL2qlFs-lmogw2HfqXSjHKqNel_FztOAYhKsJ5p7eHzbIzOTtxJSwbWUzrSD0BYpLR1ef5qxQkc3p_M8G47u_xdFff1efw0j2dGASeYtsquRxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندتا از هوادارای ایران و مصر به این شکل پرچم رنگین کمونی رو پاره کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/130546" target="_blank">📅 20:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130545">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سازمان دریایی بریتانیا: خدمه نفتکشِ هدف قرار گرفته‌شده در تنگهٔ هرمز در سلامت هستند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/130545" target="_blank">📅 19:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130544">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: توافق در حال شکل‌گیری با لبنان، به اسرائیل اجازه می‌دهد تا زمان خلع سلاح حزب‌الله، حضور نظامی خود را در خاک لبنان حفظ کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/130544" target="_blank">📅 19:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130543">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
برگزاری امتحانات نهایی در زمان‌های اعلام‌شده
🔴
وزیر آموزش‌وپرورش: امتحانات نهایی مطابق برنامه زمان‌بندی اعلام‌شده، برگزار خواهد شد.
🔴
جزئیات دقیق زمان‌بندی و اطلاعیه‌های تکمیلی از سوی وزارت آموزش‌وپرورش اعلام می شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/130543" target="_blank">📅 19:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130542">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
طی 24 ساعت گذشته،109 نفر دیگر از شهروندان پاریس بر اثر موج گرمای 35 درجه ای جان خود را از دست داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/130542" target="_blank">📅 19:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130541">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عراقچی: ایران همچنان پرچمدار مبارزه با سلاح‌های کشتار جمعی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/130541" target="_blank">📅 19:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130540">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر اقتصاد قزاقستان: قزاقستان در بندرشهید رجایی بندرعباس ترمینال باربری احداث می کند
🔴
این پروژه با هدف توسعه صادرات قزاقستان به بازار‌های جنوب و جنوب شرق آسیا اجرا خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/130540" target="_blank">📅 19:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130539">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
رئیس سازمان بازرسی: گرانی خودرو فقط تقصیر خودروسازان نبود
🔴
بخشی از گرانی‌ها ناشی از افزایش هزینه خدمات دولتی و تصمیمات برخی دستگاه‌های اجرایی بوده است
🔴
بخش دیگری از افزایش قیمت‌ها نیز به تخلفات برخی خودروسازان و واردکنندگان مربوط می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/130539" target="_blank">📅 19:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130538">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رویترز: از فروردین ۱۴۰۵ با معافیت ۳۰ روزه آمریکا، هند خرید نفت از ایران را پس از ۷ سال ازسرگرفت.
🔴
سهم ایران از گاز مایع هند از ۱.۶ به ۶.۵ درصد رسید و روزانه ۷۳ هزار بشکه نفت وارد این کشور می‌شود.
🔴
شرکت ملی نفت ایران از طریق کارگزاران و واسطه‌های مستقر در سنگاپور و دبی، با پالایشگاه‌های هندی وارد مذاکره شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/130538" target="_blank">📅 19:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130537">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQxt6UgQfqULGcmaEbmLsqHUtROsoLeM7Ld4z9m_9KJXQlqAGjuZPAJEbLY6FbYr5uFUJLBHrJqrNI1yd-kCkcjYZjiZLPZpnld-3MoMnsHJ8kpPLTt1TY28b3FsNxzcH6w78G9JD82XNCoX5scDYDA_9LaY1yJi6aRon_AlemXCVjZKYJ6xsvddQ7-lqA0AF2K5rdOHf6jIXExgmWywq4547v4eziTik5xld-DT2cbdns7LK7uzZszzPg-ftEkL-Kn6FPPOKhJx54OZHxWL0rU8E5eS8IybJ8JV6FqYZJvm8s92czOmjnKXKS5fjrbZCPAYQMue6Y17Brzjo1TfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین حمله پهپادی اسرائیل چند لحظه پیش به نبطیه الفوقا در جنوب لبنان انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/130537" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130536">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ایندیاتودی
:
وزیر خارجه پاکستان، پس از حملات جدید آمریکا و ایران که تنش‌ها را در منطقه خلیج‌فارس افزایش داد، تلفنی با عباس عراقچی صحبت کرد.
🔴
این تماس پس از آن صورت گرفت که تلاش اخیر برای برقراری صلح در غرب آسیا با شکست مواجه شد.
🔴
اسلام‌آباد اعلام کرد که در جریان این تماس تلفنی، اسحاق‌دار بر تعهد اسلام‌آباد برای ایفای «نقش سازنده» خود در دستیابی به صلح و ثبات پایدار در منطقه تأکید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/130536" target="_blank">📅 19:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130535">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از یک مقام آمریکایی: دو پهپاد ایرانی بحرین را هدف قرار دادند. یکی از آن‌ها رهگیری و منهدم شد و دیگری در منطقه‌ای دورافتاده در محدوده فرودگاه سقوط کرد. همچنین یک پهپاد دیگر یک نفتکش حامل دو میلیون بشکه نفت را در نزدیکی تنگه هرمز هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/130535" target="_blank">📅 18:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130534">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر خارجه ایتالیا: آماده ارائه حمایت دیپلماتیک از توافق لبنان و اسرائیل هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130534" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130533">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFiGOFpwMpTg6NST9intF2oDPqg410XVRqaq2yVBMsztcw8h-Xv4u5sp92Q5ekSl5WjpFbU-ZzYGqnSYmRe6zBHg2ZpqPW4zdWVf4cIe_ylcpNVw2pKWqydaVO9dEqstsGAzQSkG5iDbB5hqlxTi-4x3xcHpZ-mTYGkEDkG67hxsyXS4CEicMFNVyqX3ONgVw_K7MY3WaZpxvMoFBMsZeibJaw9WkEIoT-hu0tdbWQ0FA5CZzd_2jcdPTp7PKphhuFBkvt_Q0y_xQsJ6-tOicEyfPXNdLouT1RaGx5iCp1RJlrXd5qRW9ykLu6ir_EEoPonGZS1l0N6jxuZTbrzmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع شلیلزاده تبدیل به سوژه جهانی شده
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@AloSport</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/130533" target="_blank">📅 18:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130532">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک مقام آمریکایی: یک پهپاد ایرانی به یک نفتکش حامل دو میلیون بشکه نفت خام در نزدیکی تنگه هرمز حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/130532" target="_blank">📅 18:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130531">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سفیر روسیه: نیروگاه هسته‌ای جدیدی در ایران احداث می‌کنیم
🔴
الکسی دِدوف: نمایندگان صنایع هسته‌ای ایران و روسیه به زودی در مسکو مذاکراتی برگزار خواهند کرد که طی آن، ساخت نیروگاه هسته‌ای جدید «هرمز» در جمهوری اسلامی ایران مورد بحث قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130531" target="_blank">📅 18:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130530">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7f1f3eb7.mp4?token=rB2HDfAe19kamjw6yhIuj6_NLpTyTfvWsKq7sjL55KlPhjLDmHV8F2hQL5VXNvtgscNKHW2AL9d7SGwOu74q8FLO_SSyoyWq2kE0CaUKCePu4-f-51cEg4NY2q0pTGjwjhpHOHCEjnNAWiyO17CB872LrLtbfukkEpBImKBswhdB8x4_-6OKyLHPJ4mR1BbfX62TFMgf_ggu7rEzRtbUJrfCwKprGISzvQenD41LHE4g466xuneFfnOi8WAbRM67NIo1zO5B5ymJA2piBRZC76vfnRnSt9ySXpdhKpFhXoizCbNeRvxEAQi2GtM3KgTefQEAmpM-1VjUWOlaEQOoXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7f1f3eb7.mp4?token=rB2HDfAe19kamjw6yhIuj6_NLpTyTfvWsKq7sjL55KlPhjLDmHV8F2hQL5VXNvtgscNKHW2AL9d7SGwOu74q8FLO_SSyoyWq2kE0CaUKCePu4-f-51cEg4NY2q0pTGjwjhpHOHCEjnNAWiyO17CB872LrLtbfukkEpBImKBswhdB8x4_-6OKyLHPJ4mR1BbfX62TFMgf_ggu7rEzRtbUJrfCwKprGISzvQenD41LHE4g466xuneFfnOi8WAbRM67NIo1zO5B5ymJA2piBRZC76vfnRnSt9ySXpdhKpFhXoizCbNeRvxEAQi2GtM3KgTefQEAmpM-1VjUWOlaEQOoXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهروندان ونزوئلایی در حال جستجو در میان آوار خانه‌هایشان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130530" target="_blank">📅 18:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130529">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2cc36462f.mp4?token=K2J1Yw7_aoSIAPVDhCAi6pRwCzVXnWqO7XanNTTSD-QFteG3akW7yb1q1AQ-G6HuBC6IEqWYfmE2TdehFJX_aBMQraZ49regy6NFrKHm7B-r4TNvsROv2jRxZ00ARFrx_IdaU8Qq9w-RBrvFFW1CqYMDeeKfXnVmPWAK5a2q90zFMEXbOtdl9V8XlUZDPEEtM231fKrCWkTsVrreR2RyZVM5RrOdWKnQqc6DMo_3emwZdnVkyYB0a8jR9-8X4ORnXut-W0sc4MbC0Hc5NerLQt8CNEbEm7olHV_d4plOw9d7dX1f2xB-H4qeywX6bqvwgFZj9EJ5v0ZVLnRjpGjNWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2cc36462f.mp4?token=K2J1Yw7_aoSIAPVDhCAi6pRwCzVXnWqO7XanNTTSD-QFteG3akW7yb1q1AQ-G6HuBC6IEqWYfmE2TdehFJX_aBMQraZ49regy6NFrKHm7B-r4TNvsROv2jRxZ00ARFrx_IdaU8Qq9w-RBrvFFW1CqYMDeeKfXnVmPWAK5a2q90zFMEXbOtdl9V8XlUZDPEEtM231fKrCWkTsVrreR2RyZVM5RrOdWKnQqc6DMo_3emwZdnVkyYB0a8jR9-8X4ORnXut-W0sc4MbC0Hc5NerLQt8CNEbEm7olHV_d4plOw9d7dX1f2xB-H4qeywX6bqvwgFZj9EJ5v0ZVLnRjpGjNWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون دود غلیظ ناشی از آتش‌سوزی لندینگ‌کرافت حامل خودرو از مقابل پارک آفتاب ۲ قشم به‌وضوح قابل مشاهده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130529" target="_blank">📅 18:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130528">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رایزنی وزرای خارجه عمان و مصر درباره دریانوردی در تنگه هرمز و تلاش‌های دیپلماتیک برای پایان تنش و تثبیت آتش‌بس در منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130528" target="_blank">📅 18:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130527">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ارتش روسیه ویدیویی از انهدام کامل یک فروند جنگنده Mig-29 اوکراینی توسط نسخه هدایت شونده پهپاد گران 2 در پایگاهی هوایی در استان میکولائیف اوکراین منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130527" target="_blank">📅 18:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130526">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
بانک مرکزی: ذخایر ارزی بانک مرکزی ۴.۵ میلیارد دلار افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130526" target="_blank">📅 17:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130525">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDE_HV2jzUbTGKkGlz_Ygo43N23no5PPpB5AIZFVZskcc7lET5abMkdP0xnfhl8Ip-b2VP8esbyzmOIEcNlkLNKggHIgHmCB-d3_kDEz_1nkHWyYs2eLimajHRrFtbA_xk_A8pmnU6EWO_2-ozCDmcuptrsR4uEwmhwjFPjdxXP_UleFiJL0JjdMzXnzXisWspj2IxFd5EdqFMNR_XPsEPAMiPw28feCe4CXgjRkUpXjdNAE3UezE42hGfwjb3KdZIACt9jFa6U0HOZ43X4e0X3zIKS9cJ9W5nC8fJG2aGXQ0ud_GLjrEY0qAOEwVnDYV7Y0ysgIOnplILc0ZaJFYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اوکراین اعلام کرد یک فروند جنگنده Mig-29 خود در حین ماموریت رزمی بر فراز خاک این کشور سرنگون شده است/منابع روس مدعی هستند پدافند آنها این جنگنده را سرنگون کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130525" target="_blank">📅 17:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130524">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1RLm4RmBeboR0ooqmQML-LX5JcS2ZyLjTva0jwDhgOfkW0bQTNYtE4kG7zPrslOnQQwRnyyWcUmO3PE4wu4K84VKdd6v9RCEAqqeF0qo2dJT9eq3EXR7dsjZ-y9hDskONt_iPeDWmhkH9I6izSx7JP2usBUOzSnOSAZk4a9Y8Vm4fL5UgCRYG0zv_Y_uUg017ExHlpYgue2l82pgi7iAqoZZAvr_RfRBH3U4-_PB7OooTwNyL10RGCJT3eicr--_7SYtUnJUiHIy-Vy31zisll_Kx3edXxMlXC3Lg94t0DQVJJAxurcW_SlvD5loiF180-ViQwBj7tWfZ-NhX39hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گلشهر کرج : گویا آتش سوزی بزرگی رخ داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130524" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130523">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سی‌ان‌ان: مرکز اطلاعات مشترک نیروی دریایی آمریکا امروز سطح تهدید در تنگه هرمز را به میزان قابل توجهی افزایش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/130523" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130522">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
گزارش رسانه تلگراف: حمله به بانک‌های ایرانی کار گروه هکری «گنجشک درنده» است
🔴
رسانه تلگراف در گزارش ۲۳ ژوئن خود مدعی شد حمله سایبری به چهار بانک ایرانی از سوی اسرائیل انجام شده باشد.
🔴
طبق اعلام این گزارش، این حمله بلافاصله پس از اعلام دونالد ترامپ درباره دسترسی ایران به بخش اولیه ۶ میلیارد دلار دارایی نفتی مسدودشده در قطر انجام شده است.
🔴
کارشناسان امنیتی در اسرائیل به تلگراف گفته‌اند گروه هکری «گنجشک درنده» که یک گروه منتسب به عملیات سایبری اسرائیل است، احتمالا مسئول این حمله باشد..
🔴
یک منبع امنیتی دیگر نیز به تلگراف گفته زمان‌بندی عملیات نشان می‌دهد هدف احتمالی، خرابکاری در توافق بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130522" target="_blank">📅 17:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130521">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۶ ریشتر افغانستان و شمال پاکستان را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130521" target="_blank">📅 17:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130520">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=NMXW386EEUwCMseTUuYWhBO6Eqhy_IWf-dBvRRLNvGSncGXr0TbQPGXYeqb0hOJjmunjKzQ7hU_rcg7aOZJ2H4G5Nf7jgfzMHPWkinmcJihiG_MiRJHcDVM7C69OEqFEVjS4Ntv0IWPkOCoId-Loj4PsFgnwg5tq0HnUxdOTEiZrxbCCyZiiLiApQr0IRJKn_6XHz-fCm-lch8bqdqitfhOeoIOnVXQA3f3AP3lpz3A4bYu1HOYov8sJBqKJCXHcU2T40e4BTo01yU-x_e0m38Kb2sfG8teG1fuLgSPd2rUn4icRWW5Nb9AlmjEBFkj_VRzsrCUu66kp1nmtZYEY4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=NMXW386EEUwCMseTUuYWhBO6Eqhy_IWf-dBvRRLNvGSncGXr0TbQPGXYeqb0hOJjmunjKzQ7hU_rcg7aOZJ2H4G5Nf7jgfzMHPWkinmcJihiG_MiRJHcDVM7C69OEqFEVjS4Ntv0IWPkOCoId-Loj4PsFgnwg5tq0HnUxdOTEiZrxbCCyZiiLiApQr0IRJKn_6XHz-fCm-lch8bqdqitfhOeoIOnVXQA3f3AP3lpz3A4bYu1HOYov8sJBqKJCXHcU2T40e4BTo01yU-x_e0m38Kb2sfG8teG1fuLgSPd2rUn4icRWW5Nb9AlmjEBFkj_VRzsrCUu66kp1nmtZYEY4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو پخش زنده ورزش سه از خیابانی انتقاد کردن گفتن چرا اینقدر از تیم ملی انتقاد کردی؟
🔴
خیابانی ام عصبانی شد برنامه رو ول کرد رفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130520" target="_blank">📅 17:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130519">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
الجزیره : نتانیاهو رسماً اعلام کرده؛
تا وقتی که حزب‌الله خلع سلاح نشه، نیروهای اسرائیلی از جنوب لبنان عقب‌نشینی نمی‌کنن.
🔴
یکی از بندهای مهم توافق ایران و آمریکا؛ عقب نشینی اسرائیل از جنوب لبنانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130519" target="_blank">📅 17:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130518">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: سلاح مقاومت هرگز برچیده نخواهد شد.
🔴
توافق دولت لبنان با اسرائیل، مایهٔ ذلت، ننگ و واگذاری حاکمیت لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/130518" target="_blank">📅 17:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130517">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a3a560aea.mp4?token=hZJqoDJV4-rT4b48tosw5fMrPLmmqe8eEFqEiHRatN9b6vg5KHn7njRLU7OsFKCxv0wrhkveQqan4VG4eaK6bV5FNHafPrRz-lbXINJCJqrMxPSRjZY_wJSF-xdYWBGvsCJtmi0uFLpLqnBlaxrQ3xiDFW4CE8ED_wSNWOSZSQrcCmq1fdRkCKt5Ugkq0zBtTzSzr16HffGYJHFnglZW-QlC4V8sn55sqIm8e8MSCDlhDQmAxy7E_aeJ16XhgospoYCgIXB4ivppyrKy27VGLgzvPBal2T6_fzTWo6aVhhYEXExScPyv6uPiwRClkIrqFCTfT4yM6AGsMta25Yd1qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a3a560aea.mp4?token=hZJqoDJV4-rT4b48tosw5fMrPLmmqe8eEFqEiHRatN9b6vg5KHn7njRLU7OsFKCxv0wrhkveQqan4VG4eaK6bV5FNHafPrRz-lbXINJCJqrMxPSRjZY_wJSF-xdYWBGvsCJtmi0uFLpLqnBlaxrQ3xiDFW4CE8ED_wSNWOSZSQrcCmq1fdRkCKt5Ugkq0zBtTzSzr16HffGYJHFnglZW-QlC4V8sn55sqIm8e8MSCDlhDQmAxy7E_aeJ16XhgospoYCgIXB4ivppyrKy27VGLgzvPBal2T6_fzTWo6aVhhYEXExScPyv6uPiwRClkIrqFCTfT4yM6AGsMta25Yd1qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی طارمی:
ما به همه آدم های LGBT احترام میزاریم اون انتخاب و نظر خودشونه به ما ربطی نداره ما اینجا هستیم تا فوتبال بازی کنیم.
@AloSport</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130517" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130516">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: سلاح مقاومت هرگز برچیده نخواهد شد.
🔴
توافق دولت لبنان با اسرائیل، مایهٔ ذلت، ننگ و واگذاری حاکمیت لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130516" target="_blank">📅 16:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130515">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
العربیه به نقل از منابع آگاه: دور جدید مذاکرات آمریکا و ایران در ماه ژوئیه در دوحه برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130515" target="_blank">📅 16:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130514">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISbU0KtAzz8bI8RseqEvASNGFm8c9a2bmbkBy9mXItDnsEazF4S9rLc7Grz-z7GGzXuzay1cIMUdPpgqKyPWmt-1FFB6kh65v0y-RPmts9wHkuyP5yiHou8x7TGEZ57eaqlQ9uhWay8mkNBGys1CtLoyxgG2Y4Q4oamtpJwZ7E28whKwwdH7lwZRfc0-7x4ibVZ-kjSmQ1Bh5TtBiqpLOYhaM1wEKnEWzD35Vvk5RRsW5DuW8I6oVU5HnXVTe1tfIwEFB_IHyszfidx6gScCAyoRUU4MSaESQv_7ewZIUJ2D8d7ICxpjcfzBR1oQAm7J7taNvyD_4CT4eU4atWksPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عباس اصلانی خبرنگار تیم مذاکره کننده:
مذاکره‌کنندگان ایرانی پس از حمله بامداد امروز آمریکا به سیریک، در جنوب ایران، در حال بررسی تعلیق مذاکرات فنی با آمریکا در سوئیس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/130514" target="_blank">📅 16:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130513">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نتانیاهو: هنوز ماموریت‌های زیادی برای انجام دادن وجود دارد، هنوز کارهای زیادی در برابر ایران باقی مانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/130513" target="_blank">📅 16:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سنتکام: حملات ایران به کشتی‌های تجاری را نادیده نخواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/130512" target="_blank">📅 16:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=bp4VFPYfKM1DHuyWIN8vFjZZvxljT_Q1QmlS1NZeIG2LvX-AH5peSy8IRvdt1zEBT-qwtGxl_BmCm2Gj4FeKrIeVvLvpvxid-bsVzi8K5nDfbRWE32fN1L0Ps1s48WfuLRZCpwKhL-9r13nSRYTS0GR85bRvKaqFSP1eGaKIfocV8n5urhZ3zwBFUZ1h0uyxoLxlSLN1Gl6QDc-Xff_dhY3tQrcMF1HXgPBPqYY1CD1BfNAhjNmbdX5eFfRft8n6v94EbGN1NgnYczOD-UjckpqKIt3hsmWbH3JOHq3n2eXhbpMAssfFYynkdl4GG7VfgEA3DZT2Qp8w09vLUqAwCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=bp4VFPYfKM1DHuyWIN8vFjZZvxljT_Q1QmlS1NZeIG2LvX-AH5peSy8IRvdt1zEBT-qwtGxl_BmCm2Gj4FeKrIeVvLvpvxid-bsVzi8K5nDfbRWE32fN1L0Ps1s48WfuLRZCpwKhL-9r13nSRYTS0GR85bRvKaqFSP1eGaKIfocV8n5urhZ3zwBFUZ1h0uyxoLxlSLN1Gl6QDc-Xff_dhY3tQrcMF1HXgPBPqYY1CD1BfNAhjNmbdX5eFfRft8n6v94EbGN1NgnYczOD-UjckpqKIt3hsmWbH3JOHq3n2eXhbpMAssfFYynkdl4GG7VfgEA3DZT2Qp8w09vLUqAwCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش تلویزیون الجزیره از خوشحالی مردم غزه بعد از گل مصر به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/130511" target="_blank">📅 15:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
منابع العربیه: پاکستان میزبان دور جدیدی از مذاکرات هسته‌ای ایران و آمریکا خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130510" target="_blank">📅 15:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4819f7ba.mp4?token=afL96Or49biCkL7KPsvMJF2WGBWP09QUc4aWJFxaooUGR5-hMlM8KjTGiQRxitE32HOdpTT71WOETgGoghutwxJsE5HFH72aRRzZsanFhJjS1GaQu393eT2KP9e6MR-jOjxNo7NBNc1E5Wny0FpbFPjOKrtNZWFN1sNdQPecter-5ZnvYemqhQ90l37L2b7i4EwQ4KE3ujChM-e6PjJlQkcu8exn8Jf5gK5yfSTpwyEpyV7lM0v_9maqishuLb2nmF2SGT6p_8F2FBW1jm5sqCQvFRoSQAuGwFzVy-jRA3Utst2ay_j0pRdUjWtznK0CEm32lPHXKXKsPb-rGv3Hpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4819f7ba.mp4?token=afL96Or49biCkL7KPsvMJF2WGBWP09QUc4aWJFxaooUGR5-hMlM8KjTGiQRxitE32HOdpTT71WOETgGoghutwxJsE5HFH72aRRzZsanFhJjS1GaQu393eT2KP9e6MR-jOjxNo7NBNc1E5Wny0FpbFPjOKrtNZWFN1sNdQPecter-5ZnvYemqhQ90l37L2b7i4EwQ4KE3ujChM-e6PjJlQkcu8exn8Jf5gK5yfSTpwyEpyV7lM0v_9maqishuLb2nmF2SGT6p_8F2FBW1jm5sqCQvFRoSQAuGwFzVy-jRA3Utst2ay_j0pRdUjWtznK0CEm32lPHXKXKsPb-rGv3Hpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی:
سناریوی بسیار خطرناک اسرائیل علیه ایران، سناریوی «قورباغه‌پز» است
🔴
تجویز نخست اسرائیلی‌ها این است که آمریکا را متقاعد به حمله تمام عیار با هدف نابودی تمامی زیرساخت‌های ایران بکنند و هر جوری هم ایران دوست دارد جواب بدهد، چون به زعم آن‌ها بعد از آن، می‌تواند با مرگ تدریجی روبرو شود
🔴
سناریوی دوم اسرائیلی‌ها این است که ایران را وارد یک فرایند مرگ تدریجی بکنند، یعنی حلقه محاصره را تنگ تر کنند و مدام به صورت متناوب درگیرش بکنند
🔴
عقل حکم می‌کند که سناریوی اصلی ما فرسایش‌گریزی از طریق «توافق بزرگ» باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130509" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBAPHFYMKnoVn3F0KvFtSMsCI95FPnQBvQ-wO5wV2hlvPcXq4DUHgnbuK8CDgwdjELv_wKdRqn6oOz5aOIHZ7aPxBjq5SoNE-SoS_Pn9AKDcwXe5nh6nrfDkmAD_MsXqbRYRXfscu9Kt65hi6gurSuDCwdb2mpfMN3i1hOhmUzuci5uNHlET6sAMxBw9JurWbxJsryL2fn_YTDoc9OkQA2WsEMiRmlf4bVYCmjgtdPcRcaBDpFZoK3Nx6YEiXco-eAmEtdtweCGVs0vrYbt6faXYaeefVMpjqurnp0U22H0ZokOO0R7WtG3AL7MpwRDMzXppMJyChlnFSDGF0-lVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روی دیوار ماهی فروشی‌های بوشهر نوشتن خدایا همه ما را ببخش جز مهدی طارمی
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130508" target="_blank">📅 15:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130507">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
خدمات کارت بانکی ملی و صادرات دوباره مختل شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/130507" target="_blank">📅 15:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWZdACL8iqkthchQH1IPNBkC4itQSeSn7rIqnDOluukTyBbTcwn7x0LVDy14hx5CZTHpX5KIhgYEep1tz9l73XeLrKUZRQ4zhV9cwU0F52wyjokHJ5nXy91N9DYxt8PnSJif_zGUGeOx2vi_Uy0s9YGgZO6zcpMBxyuXRoh-PaJKPArAhYOVlrv8r2GbXsWDCPhGHQTwF_1S3hqwyg3DFbWXc5y6q8oke7Fy45ItdYe0lMQVk8Yy9jJSHG6AdiLOi3fkWjrp2LZd0t_CiYz8OwQjW5tlQRpP1ja8djWZsSkc9sfWkcPzkXSGsnlZZnqij9kP_zmeiDqAPHEBI67MqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع خلیلزاده: دوست داشتم گلم رو به آقای شهیدمون تقدیم کنم اما حیف آفساید شد
@AloSport</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130506" target="_blank">📅 15:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kL1z6mNwOo5dcpLmuaduhyjRDoovlggmInPT1xloNxko4kBc4sEXuGG80iVDCX7hfhi2shlMXjbuwdLQYnzD3pba19P9a3_xut91EaQC1cjZEP6-aDWh-oPMhdemIq5r6PHeFIeqOY1FSYOPkDz-_XG-1Sw3dwfH5vAIG6f74HQiinJksiM_U9iiocDpw8oDRDmTa5RuD_PQcQYfnovOBH-mGrQAY56gsj_auBOlw2eL6ZjGCzJgb3xw603Qjef3zgLqXau4MYQIj-w5y3hVOYyu-q2Peg7_Lpf_Ansbb94KdVwslk4ZqiNVdXWsNLMHfuIqZZeSfU_ekPDAM5OYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر رولکس: با ۵سانت عدالت نیست، شاید خدا داره منو میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130505" target="_blank">📅 15:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loMVdYVzcTfownXgoCaKLDjLGSlUKWcm3CC2eK_7uhcWhY7HchEn3Kma7FdhzahBZ__C2S_kjUuv8AhFlqDDtb6QimrEY3arOl5DqxFwm5E8tHbPn-a2MZA54_wAr3yge7IDeAdqGIuZHGTpEfadhIdsxWbsDorag27a2jNOgqlYqld0J9ZvqmeXFrz_Q7xgmPu_TRWhEGyc-nEkdzhlXDlXWxU--sJB997c8_wC131IDPMEB07sXaluF7pCg7u4raIs1sGSx_wUFC1v2UfJkTOP0V_7SWMHBAJ-17rhFtn0-HlaASOK2Q1tfh4-EVOeDlQr50VaKzrxBPDCxKbMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: من و بچه‌ها ۷ تیر میریم مجلس اگه بسته باشه وسط خیابون جلسه میزاریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/130504" target="_blank">📅 15:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4936499a.mp4?token=jhI6wyug7psZYC6g3ErBnX6V6kdkPTMzaqyIIZZXZHKi3TmsKabq7fuJoIc2jjAmRKLoDTa31SGOoMaxrVFsmsGXEIHYElJTVq8vJWOnOsicmPq7HEjAwyotHV4MbxKkL7XX0j4T4_zd7tC_ZzaKS3tc4uXtKLV_iFE-YQ0nXFFI-pp4rOr2Q7p1gN1zxIfmAvakZg4ymCUv66MG5M6iU5jpE7_JDCc-IfDUxvW1xI3BMPzO-yLQSXs4SzVU8GQQTLSxgeSMyhSWu1LCcldPI78NUZNvUdXBitMIpjI3kfxbnuvNAmkGDvqsYG5rUF4amqqJsbYsqGnCX3zVAnDKDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4936499a.mp4?token=jhI6wyug7psZYC6g3ErBnX6V6kdkPTMzaqyIIZZXZHKi3TmsKabq7fuJoIc2jjAmRKLoDTa31SGOoMaxrVFsmsGXEIHYElJTVq8vJWOnOsicmPq7HEjAwyotHV4MbxKkL7XX0j4T4_zd7tC_ZzaKS3tc4uXtKLV_iFE-YQ0nXFFI-pp4rOr2Q7p1gN1zxIfmAvakZg4ymCUv66MG5M6iU5jpE7_JDCc-IfDUxvW1xI3BMPzO-yLQSXs4SzVU8GQQTLSxgeSMyhSWu1LCcldPI78NUZNvUdXBitMIpjI3kfxbnuvNAmkGDvqsYG5rUF4amqqJsbYsqGnCX3zVAnDKDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا سیما : با هشدار سپاه تقاضای کشتی‌ها برای تردد در تنگهٔ هرمز افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/130503" target="_blank">📅 14:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
لحظه عبور سیل سنگین در مرند آذربایجان شرقی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130502" target="_blank">📅 14:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رئیس پلیس راهور منطقه ۱۲ تهران: با اعلام آماده‌باش صددرصدی از بامداد جمعه تا صبح سه‌شنبه، از بسته شدن کامل تمامی ورودی‌های تهران از روز جمعه خبر داد و گفت: با پیش‌بینی حضور ۱۵ تا ۲۰ میلیون نفری، هیچ خودرویی از شهرستان‌ها اجازه ورود به پایتخت را نخواهد داشت و زائران فقط با مترو وارد شهر می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130501" target="_blank">📅 14:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وبسایت انگلیسی شبکه Aaj پاکستان امروز گزارش داد که شهباز شریف، نخست‌وزیر این کشور، سوم ژوئیه (جمعه ۱۲ تیر) به ایران سفر می‌کند تا در مراسم تشییع پیکر رهبر سابق ایران شرکت کند و پیام تسلیت دولت و مردم پاکستان را به مقام‌های ایرانی ابلاغ کند.
🔴
بر اساس این گزارش، شهباز شریف در جریان این سفر با مقام‌های ارشد ایران دیدار خواهد کرد و قرار است یک هیأت عالی‌رتبه او را همراهی کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/130500" target="_blank">📅 14:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رئیس‌کل دادگستری تهران: حکم ضبط اموال ۲۰۰ همتی برای مؤسسهٔ مولی‌الموحدین صادر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/130499" target="_blank">📅 14:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
یک هواپیمای سوخت رسان آمریکایی از پایگاهی در انگلستان به بن گوریون آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/130498" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
الحدث: وزیر خارجهٔ ایران فردا به بغداد سفر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130497" target="_blank">📅 14:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سخنگوی سازمان هواپیمایی کشوری: پروازهای تهران - دبی از ۱۰ تیرماه با مجوزهای سازمان هواپیمایی کشوری و همچنین سازمان هواپیمایی امارات برقرار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130496" target="_blank">📅 14:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شهباز شریف: آزادی دریانوردی یک کالای لوکس نیست بلکه ضرورتی مطلق برای کل جهان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/130495" target="_blank">📅 14:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb4f7a6ed.mp4?token=T5xPEoQhKgr8fS9uK-82PiJZW_wqyFLt88MdJD1ilZ9eK5YqM_rcfHMKYbXxshmwr0rpkwHPDeHIeBh1IgvHtvq7LocHVZMDArA9AEZS8exoDAyvVOK7IJ5si4hmpFp5_nfUEYU6GTeMYDc9IYZf-f32xP21RBBgmwXB8MBjKYfyHyQfph6WFzfSVvCA1QXG8URd75Vi6fASdcrUgoEtD7HTvRhKyeYFveRmrgXfvVGh1vTIF5OV3vEN732Y5Snn6MiXjtkkcfyu9lAL7sySLad54RU8zDTYJhJtoKtY79PWF9m6NqDY8sPpnz_3kdvyzteybc61pOrqdkxXC3i0sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb4f7a6ed.mp4?token=T5xPEoQhKgr8fS9uK-82PiJZW_wqyFLt88MdJD1ilZ9eK5YqM_rcfHMKYbXxshmwr0rpkwHPDeHIeBh1IgvHtvq7LocHVZMDArA9AEZS8exoDAyvVOK7IJ5si4hmpFp5_nfUEYU6GTeMYDc9IYZf-f32xP21RBBgmwXB8MBjKYfyHyQfph6WFzfSVvCA1QXG8URd75Vi6fASdcrUgoEtD7HTvRhKyeYFveRmrgXfvVGh1vTIF5OV3vEN732Y5Snn6MiXjtkkcfyu9lAL7sySLad54RU8zDTYJhJtoKtY79PWF9m6NqDY8sPpnz_3kdvyzteybc61pOrqdkxXC3i0sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سلیمی، نماینده مجلس: اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130494" target="_blank">📅 14:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thh1rA7hU96kgavXh4AE78UuqyH5Za5mVPAV1HezuFyT-fGCi0mOU05JquzthRbu3EhOMDivu6G5Hg-80YTFwAXQdctfjohuxFnBS2XV-MdJjjirD_GGQJiOMlesq_yXuki2LMzwan4Lm23xm9_LTStd-osopsaovxupZg0eS1YIjz9N5PNgs3lQmChMqA0ch4UgXDomXVD3EkW90TrAqudYLiqu22P7QkslSeYcKEuClrMazZg9Bsc3oH6LsCJ24GJ2Ci7k3ZLPpvzLF5F85e-UMmUY2E_vttlyYweMKAHqmQux8i8EKTa-jsl4PeWIcI4XSvuxbFSnkm0gRaMoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حداقل 5 سوخت رسان آمریکایی در منطقه خلیج فارس فعالیت می کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/130493" target="_blank">📅 13:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
باهنر: اینکه عده‌ای جلوی وزارت خارجه تجمع کنند و بگویند چرا مذاکره می‌کنیم، قابل قبول نیست
🔴
کار‌ها تحت نظارت و رهنمود‌های رهبری پیش می‌روند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130492" target="_blank">📅 13:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ3pgp5jgYpqiIiOGtsK2HFBr4ZVbW0zgqk7-JU3IMJXlHKtVw8a8sE3_v0cXMCiZS2Z3V-XvH-VbHuhNKzdrKzCalkEQGKd2lwSc_a3teuiFcUQ7JaO5p4xp5rhFdd5Aaz44J7_dwFj9tpcUhoAEcxx8ZLRVwY91cF4qm9fAAleq9go1jti3c4TQj0Qow1vo339jDUrBUZF37wOesRvq5GyeMfkufK4jT8Hjmz0Cx9162uI3DExPQl0ZdU3u-sKZ2n_jf1Gs5Fowe2sMrfZb3P73fUFHBZzuBP3C0n4PE9-ji9vphjOXIk8MaA92Du8MF8vBioNMr6-dELTKizj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: پاسخ سریع و کوبنده‌ای در انتظار ناقضان تفاهم‌نامه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130491" target="_blank">📅 13:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130486">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/677cb04ce4.mp4?token=VUewZZ736eqRyHW7tI4LbrofQBhfdOrGiLRGpNaTrE38s3qtTuILkl-GrrGWchcpscfZDZyTb6iMTDTbgWyL-naOeUSP3jDl4irlP3XfqTxAJ9l3osTjzFMntKYWoWXKzxIuI22QKa-SABdapTfWt2KMFMk_yfkQTLZzbe9N542sFhmejq8ob7WlUB-7zoIj4pVLgsn8qR3WyUjwriwM3ZB8aAqrstjaZAf_wmUNW7SojXn3ibZPgHAkh73u6GorGE-obX-OFzoTbmPFAT9INgOjJDPkfry0kw5hpZcnUAKWapV08-Ea6BeS1hx6WA2pfrupnmd0KH-ALb8iRNCE4I_L-MYKJJxrPsdpHgw1eC6MLNN-HwAfPn1lxOHvO6tkWlRlghG2Qtw7WbrYV1PAd9yHEzY7i1ZUvqE5i7H2uxY-C2shNxOUCNRDd1ZnqL4vAG_2v48iwGj8jVEkVzixr63e9ZIK-1G-V7jTIFmGrWvfrqG95CsxL-h4oO1RZ-L8wG0zEIlAGLbu7_5cQ7CNLvlFHucYlHMjVk7478Yy4jeTFse6GjvMeOyuWzY2Y3ouWWWRcvJLGqhdN1rNC0dxI3OXPgCFkeUEnSQ4PAnq-sypv3cahWEzevLuKX94Q7JY9x7YN6EbbsXGcJvqfz5QRe80BXiiuyhH51AJItzZr3I" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/677cb04ce4.mp4?token=VUewZZ736eqRyHW7tI4LbrofQBhfdOrGiLRGpNaTrE38s3qtTuILkl-GrrGWchcpscfZDZyTb6iMTDTbgWyL-naOeUSP3jDl4irlP3XfqTxAJ9l3osTjzFMntKYWoWXKzxIuI22QKa-SABdapTfWt2KMFMk_yfkQTLZzbe9N542sFhmejq8ob7WlUB-7zoIj4pVLgsn8qR3WyUjwriwM3ZB8aAqrstjaZAf_wmUNW7SojXn3ibZPgHAkh73u6GorGE-obX-OFzoTbmPFAT9INgOjJDPkfry0kw5hpZcnUAKWapV08-Ea6BeS1hx6WA2pfrupnmd0KH-ALb8iRNCE4I_L-MYKJJxrPsdpHgw1eC6MLNN-HwAfPn1lxOHvO6tkWlRlghG2Qtw7WbrYV1PAd9yHEzY7i1ZUvqE5i7H2uxY-C2shNxOUCNRDd1ZnqL4vAG_2v48iwGj8jVEkVzixr63e9ZIK-1G-V7jTIFmGrWvfrqG95CsxL-h4oO1RZ-L8wG0zEIlAGLbu7_5cQ7CNLvlFHucYlHMjVk7478Yy4jeTFse6GjvMeOyuWzY2Y3ouWWWRcvJLGqhdN1rNC0dxI3OXPgCFkeUEnSQ4PAnq-sypv3cahWEzevLuKX94Q7JY9x7YN6EbbsXGcJvqfz5QRe80BXiiuyhH51AJItzZr3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز شنبه 6تیر 1405
تجمع بچه های دوازدهمی و یازدهمی جلوی سازمان سنجش تجمع کردن از ساعت 12به بعد و قراره تا ساعت 4ظهر جلوی سازمان سنجش تحصن کنن برای موافقت سازمان سنجش با تعویق امتحانات نهایی به بعد از اربعین چونکه سازمان سنجش مخالف تغییر تایم امتحانات نهایی و کنکور هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/130486" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130485">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnhdTIF4fFrV336Mo1kq3yHP807XXhZzQ-8i8e5OAzKxOLMQDSmuuV9NgIVlIweOe19qPp-Rt-NxmiDuUDmCpiy_k9Y_22O0yvGZcT6t4qBnC6NumEELzvF547blmcTJ9r7ntW5lusJ6yEBK3n8dxnSPzgg0ceaj9YN74FauyRY3uUcM-PFD0iC32sAbGwE6-k6aWuGptT47kaqxVF1aFlOychv26yrnR1X29hsdaBqopGlgWJSzQziiOYJY7tdH8ZAUGajbiUJt18Yf2Tw0GYJ-unZH8euZjZPvTZrj65emLPyo_8-zR58946FoBK5CDR96KfrB6GfEYznBo0OBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مولوی عبدالحمید:ایران نباید سرنوشت خود را به لبنان گره بزند، گره زدن سرنوشت کشور و منافع آن به مسائل کشورهای دیگر با منافع ملی ایران سازگار نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/130485" target="_blank">📅 13:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130484">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
برقراری رسمی تجارت ایران و امارات پس از توقف چند ماهه به علت جنگ
🔴
معاون خدمات تجاری سازمان توسعه تجارت ایران از فعال‌سازی مجدد مراودات تجاری میان ایران و امارات از مسیر بندر جبل‌علی به عنوان یکی از مهمترین بنادر جنوب خلیج فارس خبر داد.
🔴
این بندر یکی از مهمترین بنادر ترانزیتی جنوبی کشور امارات با ایران است که عمده تجارت با ایران از این طریق انجام می شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130484" target="_blank">📅 13:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130483">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مقامات دریایی بریتانیا: یک نفتکش در تنگه هرمز مورد حمله یک پرتابه ناشناس قرار گرفته است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130483" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130482">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
صدای انفجار در تنگه هرمز
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130482" target="_blank">📅 13:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130481">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2if0Wou-VQLO2a3pumx-rexaL8M87-Gt4QTl39RExR10GLxs7UEGEDk0xm3P2Y6wmSShxZ2MYs-SVtPi5msCzjQh-6bmwtfLxOLdBANIzYH29M0hwqTSrFBmeGHP9gdm4cqyBxnpvxdNhBJgh6C0q5K2DhOCCRb1Z9DFuW0DoqINxp2yBM0kf6aiI8_RcBxLL4db1nk7N9aLjVg2JXI7jyG5zSDFz5MLH_VX3Hacf9sW4pVmtwm6e7zEWWpWiUJ4Yr7MDV6J8YzNhYtlp2Og70bme-tvn5xMiC_9fU6WbXNzguJqCkMjoQt_9nkRgk9HgmGiMhVy-lIUls2ZzEBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردوغان: برای بقاء ترکیه با اسرائیل مقابله می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130481" target="_blank">📅 13:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130480">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
صدای انفجار در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130480" target="_blank">📅 13:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130479">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سازمان مدیریت بحران: استان‌های آذربایجان‌غربی، آذربایجان‌شرقی، اردبیل، گیلان، مازندران، گلستان، سیستان‌وبلوچستان، کرمان و هرمزگان در معرض بارش‌های شدید و خطر سیلاب قرار دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130479" target="_blank">📅 13:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130478">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
منامه: ایران صبح امروز به بحرین حمله پهپادی داشت
🔴
وزارت خارجه بحرین این حملات را محکوم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130478" target="_blank">📅 12:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130477">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
حمیدرضا رستگار، رئیس اتاق اصناف تهران از تعیین نرخ های جدید نان در واحدهای یارانه‌ ای و آزادپز خبر داد و گفت: این نرخ ها از روز شنبه - ۶ تیر - اجرایی می شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130477" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130476">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ستاد مبارزه با مواد مخدر: رصد ماهواره‌ای کشت غیرقانونی مخدر از سال آینده راه میندازیم تا دیگه خشخاش نکارید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130476" target="_blank">📅 12:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130475">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
المانیتور گزارش داد؛ عصبانیت در اسرائیل بر سر رویکرد ونس در مذاکرات با ایران
🔴
منبع نزدیک به نتانیاهو: ونس به آرامی دارد ما را به کیسه بوکس خود تبدیل می‌کند؛ آنچه اینجا اتفاق می‌افتد، پیروزی ونس بر چهره‌های طرفدار اسرائیل مانند مارکو روبیو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/130475" target="_blank">📅 12:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130474">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
منان رئیسی؛ نماینده مجلس: شماها از پشت‌پرده خبر ندارید ولی من خبر دارم.
🔴
یه شخصیت خیلی مهم تو جلسات به فرمانده‌های نظامی گفته بود اگه با آمریکا توافق نکنید؛ من استعفا میدم و میرم.
🔴
فرمانده‌ها هم سر یه دوراهی سخت گیر کرده بودن و اگه با نظر اون شخص مخالفت میکردن ممکن بود اون کنار بکشه و کشور وارد یه خلأ سیاسی بشه. آخرش هم بین بد و بدتر تصمیم گرفتن همون گزینه بد (توافق و آتش بس) رو انتخاب کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130474" target="_blank">📅 12:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130473">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رویترز: یک پهپاد اردوگاه یکی از گروه‌های مخالف کُرد ایرانی را در استان اربیل در شمال عراق هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/130473" target="_blank">📅 12:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130472">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دبیرکل شورای همکاری خلیج فارس گفت که موضوع اختصاص ۳۰۰ میلیارد دلار برای بازسازی ایران در جلسات بین وزیر امور خارجه آمریکا و وزرای کشورهای خلیج فارس در منامه مطرح نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/130472" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130471">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین: با موشک‌های «فلامینگو» یک کارخانه تولید سلاح در منطقه ولگوگراد در عمق خاک روسیه را هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130471" target="_blank">📅 12:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130470">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=F9G_omQwlqhIvz0ecz6D62MbLEpG0WTAbx1viZKPr5d2ONKC6Wq7bpHWdOGz9C6db_OutwrBUWrjQVCc3tJ1h2Sp5YYKnAzzUSiR7OOqqxjEdOcspKvHELt8cAxu2F1QhjdoF0C6HG_dv2Cniq9iGDl3vbvjbSjC7R3a8cItBrVxw76x972BhkI61nAv0nB9wrjTyVxRAxhehzCoWJylAMUT5x0X3Ag2wOUfby2cLuMqjSyV5b0N27VaX5LWSXgpCajiUxxc9OUbQzYZWVt2vQ_nzgfQhDZUG9RmNhu0-L0mU0G0Pxh79IlCNo_ZmpbiF-2rnAm9YDmSfLNdm2jYkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=F9G_omQwlqhIvz0ecz6D62MbLEpG0WTAbx1viZKPr5d2ONKC6Wq7bpHWdOGz9C6db_OutwrBUWrjQVCc3tJ1h2Sp5YYKnAzzUSiR7OOqqxjEdOcspKvHELt8cAxu2F1QhjdoF0C6HG_dv2Cniq9iGDl3vbvjbSjC7R3a8cItBrVxw76x972BhkI61nAv0nB9wrjTyVxRAxhehzCoWJylAMUT5x0X3Ag2wOUfby2cLuMqjSyV5b0N27VaX5LWSXgpCajiUxxc9OUbQzYZWVt2vQ_nzgfQhDZUG9RmNhu0-L0mU0G0Pxh79IlCNo_ZmpbiF-2rnAm9YDmSfLNdm2jYkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130470" target="_blank">📅 11:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130469">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
صحن علنی مجلس هفته پس از تشییع پیکر آیت الله خامنه ای برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130469" target="_blank">📅 11:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130468">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkBp2CicbLbzlWiOIUnOBa08Ujs4HLUgFXtJhGngFmg680apaIa11ikZbXt9B67wG7Jqn8H5XdXOYHS9pOCoRom0Ninrb0QvS11YNtCTXepLU-yAxDM6sby8G431rZYKpKyeuJQz8GZ5L-37P_9-8v5KlWaflUzx3hP_au9D0WtcPnsspCEdA4e1MarOW5RRo7sSCr79xHaB8-fz_IhX5hKDz5bq1xXYfIbuYkl5eErXngB1N41Is0qH9xMdkpzUPfN_B4D8UfCCeVNNEIm1B8qCA-87GG7kx9K8pVFtIiidiz7v0PqwKbEKZJNKrB3y2Q0aj9uFbWgTPPUxCpTEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم استان های بالای 100 درصد:
▪
آذربایجان غربی: 106 درصد
▪
ایلام: 114 درصد
▪
چهارمحال و بختیاری: 103 درصد
▪
خراسان شمالی: 103 درصد
▪
کردستان: 111 درصد
▪
کرمانشاه: 105 درصد
▪
کهگیلویه و بویراحمد: 100 درصد
▪
گلستان: 103 درصد
▪
لرستان: 109 درصد
▪
مرکزی: 101 درصد
▪
هرمزگان: 101 درصد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130468" target="_blank">📅 11:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130467">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh8LfW09T9o-azPlUdys9xtrD9kpgIYuPvzkAxCqTAnoxQwowAqcYYEUZHEST15zA9p9hWF4M0tbE2GqxSz63eH-WjxIo7Z374m7DHX3vGSvhXTp3a-vCRn-Mt_vX7tlYn2J2-F5euL6ZUmnxOknlSVKP0Sj3ukh5Nx86VNFFFbM0XwdBmEu5S1bWElFdm9389cVcMnTTmO-DJLS4u8jqedIf7sx0TSMyRC3q-Th9mGVa5OaOkTHILIhTP1CqvxPR5Nyla8O_E2KvxmJZEuQ_FMybUvEyxsbTXZxfaW5Okczr1__uejIkCOYUQJ0dyg9Gy5VDb13JOKiM_A8rgTLkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره جان بولتون: جان بولتون، نماینده سابق بسیار احمق، نامتعادل و بی‌مهارت ایالات متحده آمریکا، به تازگی به گناه خود اعتراف کرده!
🔴
او فردی وحشتناک، دیوانه‌ای است که فقط می‌خواست دردسر و جنگ راه بیندازد و هر جا که می‌رفت، بی‌جهت مرگ و ویرانی را به ارمغان می‌آورد
🔴
امیدواریم با او به شدت برخورد شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/130467" target="_blank">📅 11:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130466">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
با وجود اعلام برخی بانک‌ها مبنی بر رفع مشکلات، گزارش‌های مردمی‌همچنان از ادامه اختلال در خدماتی مانند کارت‌به‌کارت و دسترسی به حساب‌های بانکی حکایت دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130466" target="_blank">📅 11:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130465">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf31c890a.mp4?token=q2pNqKuKzz8SNoA_cqR0LXTmxzOrNrunBFFet3zh_wsY7rTZaMshRAY6UYMR977sSgU1eOn_95eeJl0NbsHtzv0RZvnO_y-Cw2lx1kuI16Dmrbkg4IspCNzhr5upKWKN2UNGnTdT7wpuTNWDhMIF3kD-dX0UAp62A9RtvOMa_NEBx9N31sb_RsjatA0vUDKgCuxjJXudo_fHiDFwbAt21wVEERrnV-ixIcJrA6UQYT854rRnTZAm6XC3KPdYMtWcA_RLSXfnCibxJ1YToQbGsYeT75nm63H3CLOm0FAJ1oEo712KlZL6J1zx-eEwcmm9ngcQCwZuSHNbqIa3du8Zeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf31c890a.mp4?token=q2pNqKuKzz8SNoA_cqR0LXTmxzOrNrunBFFet3zh_wsY7rTZaMshRAY6UYMR977sSgU1eOn_95eeJl0NbsHtzv0RZvnO_y-Cw2lx1kuI16Dmrbkg4IspCNzhr5upKWKN2UNGnTdT7wpuTNWDhMIF3kD-dX0UAp62A9RtvOMa_NEBx9N31sb_RsjatA0vUDKgCuxjJXudo_fHiDFwbAt21wVEERrnV-ixIcJrA6UQYT854rRnTZAm6XC3KPdYMtWcA_RLSXfnCibxJ1YToQbGsYeT75nm63H3CLOm0FAJ1oEo712KlZL6J1zx-eEwcmm9ngcQCwZuSHNbqIa3du8Zeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!
🔴
کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/130465" target="_blank">📅 11:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130464">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سازمان حمایت: قیمت جدید خودروساز اصلاح نمی‌شود !
🔴
در شرایطی قائم‌مقام وزیر صمت با اعلام مخالفت این وزارتخانه با افزایش قیمت اخیر خودروساز، خواستار حذف نرخ‌های جدید از سایت‌ فروش شده که سازمان حمایت به‌عنوان مرجع قیمت‌گذار در توضیح اظهارات این مقام وزارت صمت اعلام کرد که «منظور قائم‌مقام وزیر صمت از اظهارات اخیر، اصلاح شیوه قیمت‌گذاری خودرو بوده و این سخنان به معنای اصلاح قیمت‌های اخیر ایران‌خودرو نیست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130464" target="_blank">📅 11:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130463">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: ارتش اسرائیل بخشی از نیروهای رزمی مستقر در جنوب لبنان را خارج خواهد کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/130463" target="_blank">📅 11:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130462">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2rHbfB8rgVFh0LkooK3E7_tA8WiO2JIOmODAvMzaNbp8l_7cu38UnptpWdSajwVAwAv5ArGIG3k5aXVSyrfhPvJuYciSdFuLH88_wulawaBlCFalCaA2xG12E4GMZ_TjLhiDveOZTcndMeczUYt8favFbHC-RCLiMVxzfeoeRAo6HEF6vYBj4WfuEh8qWc4JPMtz7Y812VttTVLm1uUrTygywcktKnLtz9yd2-EgXcMe6hzeLusacMAwn2-zfzImkuuwroUfnB_HseMhuRupMsXQGpMseUil19sA_cYIjSd8QvEPtPJKIa0pSUDui5MO7ca0ByD8l4xn_Z4APNRgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: بعد از حمله دیشب، هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود
🔴
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/130462" target="_blank">📅 11:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130460">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULFCw38VcYOSH1bicGLgCA4k1mxbk1j_gPBJVMLGlWI2-U7NkJMtWTmfaJMEOb3-SylGLQGGuN71cfDANPcQ6mfsUdbVMU7rnY8DrwBE-13LMrGQM2yuUdHhWdhuHj97zJXQeoDb9NQZOf4DqRlVPwZoBm6VHk4sSfXATjD-Bsma_VKqHi_9zqO-p2P_qQWiPFMRoUzl_O7s_7oF3TjIv3DjLO41dei3h_DNGdquCy61yAsY395sfxK8z8u-2PqSPt4b8fzwaWEcnubVz3kq-h67iBlJQtVv7JoFlptIRu3bT7sOkvOmLnCG83xGl7qTWUv3-00EdLU1Ypf_EKhuqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq65GUsDnpC2S-WgshvHqnJavG6fAMYJ4XugpRXKP4blfqH81t_zC4tAhP_1uuK_5BlEhP-CkTCNxeh8TUdDGYxRprCy9H40nhhGVa_zjOVMHCwTRwCkR53QRyQI9xXL3KY83jH9g0I1N494sPn3iT1Wgw-TY_KEX2qJehOMW6E6zlvE0IzuxmwV23O6fHsrvGai3ERyO9zawESvNSAJOhp2Xj20SCkbc1I01ypkjOKVe4Yv0NBL2O03N309PRJuHRxZfGLBDqKN_JAutQ9CHZvCNLxLty9PcrrLvMw-O87nXkeKuVYuDDPF_0EpuWknqRTwm5qrhzrj6z3duekPig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شباهت عجیب سرمربی مصر به یکی از کائنان معبد آمون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130460" target="_blank">📅 11:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130459">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/806fc925bb.mp4?token=PNzPA_W0nqjhJQvHSGaFTh6v6lhSXDi7FpwIcwHKq9UvE6bd_Z_Gv2QgWD8I_0llF-4OhJ7pME-5fAbnPs5bLrTmE1Z2nq4tQKYJaNIj2CEqLGeLcz9G8GXyX0Sc1E3zeXNBd4j2N-20HiLbaksHCdSWvuy5IF2cWnU8-2_aM2-piuffRlyoncPj78-yVvMoKKSkONvq2A0Ct-nizNo1Lx-Hqn6VUZ1SZnr83e1Qm0v_j0ATYupsXHvRtAIA03DlkfkVgZUCoidxMkOLoFrBXe1oD_F54iyTDf4wRY1DXiRGqd9CBGtyriLeFHpzLQTPhwYU3voVbfEq2uTJm3U5nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/806fc925bb.mp4?token=PNzPA_W0nqjhJQvHSGaFTh6v6lhSXDi7FpwIcwHKq9UvE6bd_Z_Gv2QgWD8I_0llF-4OhJ7pME-5fAbnPs5bLrTmE1Z2nq4tQKYJaNIj2CEqLGeLcz9G8GXyX0Sc1E3zeXNBd4j2N-20HiLbaksHCdSWvuy5IF2cWnU8-2_aM2-piuffRlyoncPj78-yVvMoKKSkONvq2A0Ct-nizNo1Lx-Hqn6VUZ1SZnr83e1Qm0v_j0ATYupsXHvRtAIA03DlkfkVgZUCoidxMkOLoFrBXe1oD_F54iyTDf4wRY1DXiRGqd9CBGtyriLeFHpzLQTPhwYU3voVbfEq2uTJm3U5nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدئویی از حملات دیشب به ایران را منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130459" target="_blank">📅 11:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130458">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزارت خارجه ایران مدعی شد آمریکا با هدف قرار دادن چند نقطه در سواحل جنوبی این کشور، مفاد یادداشت تفاهم را نقض کرده است.
🔴
این وزارتخانه همچنین اعلام کرد حملات ایران ماهیتی «دفاعی» داشته و مواضع مرتبط با نیروهای آمریکایی را هدف گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130458" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130456">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8NuMdWoGvXk_McXhSK-G_ZCqWUAoNeDoVVo3Dy3RSttgyHCKC8z03FBRAQRMXFPJUbvPXhCyU5DCMbLV0PF33Pcx466tI0abIEBIxeI2eEX6kzxtY7FzDOTrjzzROWbOfU_mZsDoiniip398G_kgj7GkLpC_uz2ViVLOs-zRp4tiAxYEO5ZhVqC7psCertovGsyzLj9O0-Y6omNwN0M6klnZB70sw5Ubfa4qY9QoPgFoHHClSDEcHfD8jaqsqYusPRjQ_GlwIvj4KOfIqFe7TafrOtxUYZ14y5L486_S1308POMi8dXdqi2oNv7sYoMLrGV0UcrQib_RRImdGCNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHndB_jbEdMWQQz3LEVSMsnePxxmbEZ0hKKPsmvx6Kxa3v1-EUqbVSVS6o9zvm0NNdQBJhpC6VfebVJSAj3advhziMkCS7cVKmTXOjaH0A4AAPd2aqpawE4CUep2y-EDhv1-7PYnUzGfOb74zTwGrrRhJDsJkjpZoYVrNYdTwH10Tq95jkWDK1pSoYvLB4Hfplkbm6m263nqZIQRj7WlIZdXHM1GF0Q46EL9xt5c9ypQlD-ddVzGB1rMmz70hwWCUbHnruPiCtB89RhAJtpMllbdKclcL6SSYdtys4kQ688rffwsAUPaRPGD3ykUpRfIgOfTvizxe0uLqfYClAuoWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شانس ۹۲ درصدی ایران برای صعود از نگاه سایت اتلتیک و ۸۵ درصدی از نگاه سایت اپتا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130456" target="_blank">📅 10:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130455">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
خبرگزاری ملی لبنان (NNA) گزارش داده است که نیروهای اسرائیلی بامداد امروز اطراف شهر مرقبا را که در فاصله حدود ۱٫۵ کیلومتری (یک مایلی) از مرز لبنان و اسرائیل قرار دارد، بمباران کرده‌اند.
🔴
این گزارش پس از آن منتشر شد که اسرائیل و لبنان در واشنگتن یک «توافق چارچوبی» را امضا کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130455" target="_blank">📅 10:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130454">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q30sMcoL0pBtE7iupjoRAZ_WJ2uuNPmEZ4i7b1S1UhTBaujc8YQB4lhFqjwGhATI8WkK3fHpyJkajkr_Hchfr1KmqxgqkAm9Of8XG0nPMo2sxQH6m_BCeMsttXasqADWJGIo9ORUuqvWC04mS6Px48GHMHbQJ0Eftm7OMuW-mpYLKYWv0j5OglLlDMCbM1BYpImNWufYCjmClqT87N_LbEsPkHgYBFc2wSwgKL5xdvNLYR_Tl1no10IO75zfoSbkuBsfkLmBkID0PWS0iuy9cLT7S5f5moKBjPXR_PBJnxdveMDuUt1x3dm34xMiLCCw8mURgYbuWPhupWjTpTiGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده دیشب به انبار پهپادی در جنوب کشور حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130454" target="_blank">📅 10:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130453">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
به گفته مدیر بنادر شرق هرمزگان، پس از حمله آمریکا در اواخر روز جمعه، هیچ خسارتی در بندر سیریک در جنوب ایران گزارش نشده است.
🔴
این مقام مسئول با بیان اینکه این بندر به طور کامل عملیاتی است و هیچ آسیبی به تأسیسات یا تجهیزات آن وارد نشده است، افزود: وضعیت در بندر سیریک عادی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130453" target="_blank">📅 10:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130452">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: ارتش اسرائیل بخشی از نیروهای رزمی مستقر در جنوب لبنان را خارج خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130452" target="_blank">📅 10:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130451">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozJZTxz4CH7-LZzKqVfs7cDY08DxoxuKVlV7L5LOUD25ZnGRkgO1AY640F-wW1cyz_rgLViD8BhhtTXm9BVvV7v2LOFf8F08eKlmKrS7Ow7NMa1ORRxqNkHZTCVPBxL4XxTqe68ucHpSG_VSdgu177PltV3ytIvXrGxFaVqhZcpFXJOhD7JPQD9HtqLEwwLqY9aURQb3hfGa-OQDuO8i_xsD_5S2VKPuR_PTB8eHaU9A6duLvrZk1vWxPcj6M6DMKzLp-y6EcB7pvSGrKO6VOvOLoBtQ9TrszarKkYDsx9vAkwjbHeYGvs4_DiF0rb7Xpk9atbpzOewD6DHNNJVD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز آمار:‌ تورم نقطه به نقطه خرداد ماه به ۸۸.۶ درصد رسید
🔴
تورم مناطق روستایی در خرداد ماه نیز به ۱۰۸ درصد رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130451" target="_blank">📅 10:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130450">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG4RdHq3cPmTxz7BW_pZjugOn-Fd9LM0IgrGKsltrCaXMV5Zb3JHBRm3JYOdI3Ml6gPT8cjSmTJcL4iWVEcsawVLLyJC2jyT6QyyGf9XT62Ez3-Oo0phBPEmObywqiLGsp5QfC_VG2nXtQou7zfEtemFuO2O4mMncdjuMUgyY5B0a6gn3U0AoG544Cawi5OsBR_7hpWbbA9gaJqWlOg4yTx8RVO60TakNqMgfN-aWLGpqDgEgBjY6AXG7Bq2pSoexsrBX3r4Pr9gjIHP9oF44NdNBD3EZS9n--mKbNxnYI0DmUByN0LVH9riBHFyf1bXnZjCBriU-gv7BkokiRzOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش آمریکا با قراردادی به ارزش 36 میلیارد دلار خط تولید موشک های رهگیر THAAD را 4 برابر کرد
🔴
این قرارداد در ژانویه سال جاری امضا شده است و بزودی لاکهید مارتین آن را اجرا خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130450" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130449">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3293127d1f.mp4?token=aHwKoW0kZItrlpnXJOHby21O1-MU6lx2YpT4vAn2nybQlG8_0A0KmVbKMeBaF0a8GBn9VLwGG6Pm5dZyQfjN2G57HBfkjDSSYP1N1kyAd1_JxjaruaZ5EgCS1re3E4Qxa3m5eFYtNw4c4TyaoDP3b90rIra6ErbtRilUf2XJSRp01S38rmFuOFhm9kXtZfwEb2PU6Qef7T7ulbu3LjAsixSLrN-D84FI4IG-vAq1anyYTAknLWeAbVdIDBFh7iCK2wzJvzMmIaFEk0IcAC7EwuAOHq8iwTTXjNwUCooMg-ws8V9NRiIOP7TCZMh2qXOSCzr2_h_fs9R2aOBNejSqEol6UfYCM6NiCHFXHwoq-G1jVmm1gcDZN0hMPjkuyevMqQ-pC1CWpE2Ix8oRcQexO0cvCeMuaiGkSfWz2jAT44fV7aXE_c_ogZIeeQHf7nyrjPQL-27CaEcwCYI41MkoXJIOr32DNNktxy1JR78gGG5fgSRyuLqyap8yP7XyXY0sgMvJLfPVe35y-XBFfK0zeDEw54FxQA1uUjiGDvdR1Tskg7epwqLYsrKrqPktQ6ENkV-WGUYp6DYP0tfeBYArvwROd0M_B1-hQz1FXf7YVmfOge0Q3Y0E3Gfn0RTzAp88OR2wAo2jbyKuD19PpRAxzrGwzYSxOBOwxgYcYCXZdjs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3293127d1f.mp4?token=aHwKoW0kZItrlpnXJOHby21O1-MU6lx2YpT4vAn2nybQlG8_0A0KmVbKMeBaF0a8GBn9VLwGG6Pm5dZyQfjN2G57HBfkjDSSYP1N1kyAd1_JxjaruaZ5EgCS1re3E4Qxa3m5eFYtNw4c4TyaoDP3b90rIra6ErbtRilUf2XJSRp01S38rmFuOFhm9kXtZfwEb2PU6Qef7T7ulbu3LjAsixSLrN-D84FI4IG-vAq1anyYTAknLWeAbVdIDBFh7iCK2wzJvzMmIaFEk0IcAC7EwuAOHq8iwTTXjNwUCooMg-ws8V9NRiIOP7TCZMh2qXOSCzr2_h_fs9R2aOBNejSqEol6UfYCM6NiCHFXHwoq-G1jVmm1gcDZN0hMPjkuyevMqQ-pC1CWpE2Ix8oRcQexO0cvCeMuaiGkSfWz2jAT44fV7aXE_c_ogZIeeQHf7nyrjPQL-27CaEcwCYI41MkoXJIOr32DNNktxy1JR78gGG5fgSRyuLqyap8yP7XyXY0sgMvJLfPVe35y-XBFfK0zeDEw54FxQA1uUjiGDvdR1Tskg7epwqLYsrKrqPktQ6ENkV-WGUYp6DYP0tfeBYArvwROd0M_B1-hQz1FXf7YVmfOge0Q3Y0E3Gfn0RTzAp88OR2wAo2jbyKuD19PpRAxzrGwzYSxOBOwxgYcYCXZdjs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیل ماهر: برنامه هسته‌ای ایران نابود نشده است.
🔴
جی دی ونس: کدام بخش نابود نشده است؟
🔴
ماهر: ما به آنجا نرفتیم. کل ماجرا این بود که باید به آنجا می‌رفتیم و بررسی می‌کردیم؛ در غیر این صورت، این کار را نمی‌کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130449" target="_blank">📅 10:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130448">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پی‌بی‌اس (PBS News) به نقل از یک مقام آمریکایی: ۶ فروند هواپیمای نظامی ایالات متحده، چهار هدف ایرانی از جمله تأسیسات راداری و انبارهای موشک و پهپاد را در منطقهٔ سیریک در ایران مورد حمله قرار داده‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130448" target="_blank">📅 10:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130447">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
مرکز لرزه‌نگاری اروپایی مدیترانه: زمین‌لرزه‌ای به بزرگی 5.4 پاکستان را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130447" target="_blank">📅 09:59 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
