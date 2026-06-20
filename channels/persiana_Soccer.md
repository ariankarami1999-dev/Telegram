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
<img src="https://cdn4.telesco.pe/file/VKu9A8sneObxPkHUzJ-kWjwrk8uFxltL1gYWfVlv8Hvfat8EetXMgHu6rq_d30OMSeNsDFjDKeHcREfoh0Oo6xmw2_SA1-tpNauuoN_QwbZRGWiuzA4524T8fbMgNGA2IPk8w7i8Jr2M4vuzSnVooLR519ErL1hc6AJamMqL5Bk6ZP1ArED64DotO2v1KY5FcmBx6XXRzNbhp_t-tPs1CbwGs8-M6lxPY7N8XYK-5-aUTnO71njNNqangil5CNRdupWDles2wBRuCN7f5M1p_kqkYSK15unpYqYse01P5iHd8MfHDleXSChci2VT7UAe4S_Ng9W5HG02EtDeMxwSTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 310K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 22:41:32</div>
<hr>

<div class="tg-post" id="msg-23934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/persiana_Soccer/23934" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJAftfsek8qyM61wD4YEVG_0traQYCQ46Qo_1A3qZfV7Q6W1vNoxtjUmeMt60Cz5G1zouR5RE5vh1NDv4Y5oi5ht8aPGY4mIaQpAh-QWpS_LIY79qYztvm1xAOfi0_hvYuDqhvAsZcrbljbXLQRknfUdWKItaBehmUQIwsjjyvSrASBIlCFC0dWDseEnX5KTtP0FMkUT1iQIEKM6OxbncQXOZNuLB9CNjS1PZtkZ2Q-i56YcGt3D22TGPVshLErauHA68kURCHGyiyMVq1Ur9U98veCWK92XUEgfyaRa7TdA1dsIp1MCLzucvxGpjUCz4AG3I1iCH2ytcRJnt3tDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/23933" target="_blank">📅 22:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ad4RxPTvFipaYEvPZrQBkbnFQIwJxPyB9SRipN1iJz_T4iuroQCxW0xhEh6SjcKfoc0l9FCTGLEracaaoce9rAfaCn3pYk6SRoPQwIYSCtZswfDO_C8KOIfd10xh8szGLivCM1uPmLc5fF00-RTc0JWbz69dGUZ-GR8W_OIh7gY3QM5dh9ff7hywnYfCU5FMEt37ZEQdKjWawhfnTpzT4hkb7GiLsEzvZp1sXItKwk7pc-NnrFZ49lvdQO4ShkAowtxHnJ5YuZOR4TXSGazS_EAOKbFpDFK-OzYSKGKDktLxnLjulapXp6orzw_NiYwKJ9gJzdF4g1nrrj6N3ehAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fR1cHDxyRN5vojxhZxQ4HKSha4k3A5OJMZ6lbj9X0nvClup96LAZYz9sDc4rkf-EWwXiAnRhttbeyljNMIHHb-3fg152wP5WAw0HAls9vEKZ-hX0hUFg9Ke600bKzUkaQPPJ1O1KV8MpVmct_WbOhkj5FBvWLfoFQ50cWJh97tr-kYzcGf70D2_3b06s4aEZOE72513R04Bq_gpiwBbNk8MNGKb27PNBReS4TwOOHKOMd0NjlIVhckOlY7iwM93cBVzJu7rBLg_zg-iYGUQ9dS_bdYy9GFrlnAS2lmCkp5HGt0NDObyUcBHm0kSnN4OFZ5fJexRHOcvNrbS3hPtlIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026
؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/23931" target="_blank">📅 22:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKWJGzB8F_Llkta3fIVYsEMWG5iodbDW7gnn4-dqN6su_CkqG0TZNpYn6pyzbC8Tm4ktcwJD4Y3B88qcs-N-Xv7a-KOdB6iU6F2QzLSa-D-bjkfqYMubk-zOCA-o-NZn6ASGnz_NfZL7gfq9l0MsktZERyTVZkOWp7g2aaT5pXTHsi_63EBN2So97ud4DYihbr8dAhMv_3EhL2K611_Y3SJXa8pZIorQ7ZrMXR-IiGcsQUDzgjZumLzQhFuDbuDWEW9NZoqSzUHZygVtXf4JvXw3P34Nw08bC4TE_8zAqa2J_3Zt1RiT7TXYFBxXc0sTfWXqzuRk-zl3wf_ogCGotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/23930" target="_blank">📅 22:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3537466720.mp4?token=RwMlJW529uUSV29n_UE3rtfKE9xvstd_bCDQw2js3Iu15TlJhPB5Ut98hl9FIugkTU6iZt6k9T-XEfoSomKku1nozq2gbFxx8cCbcGLhTjPtThE_iE6wI020Gu_VqHMSnH-sgq5RIfRqL2z7nI3T06lyqzQgbNOY_dTMDfYMKC2cT0pfNiOnX64VIBxfrh0nTveEwpotfknzVyEeE5bDjeiS42py2Fok0yXZlLutS20Vaf73Sda_oBpVPCc5vHJoYSeLXzjnkMxFaOrORdl_PVw07DrC-qDv3unQrfhgHXApaxnpdADJx8w1x3v4KiNE1Z7PG4urn7RQhWXB_ZrvSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3537466720.mp4?token=RwMlJW529uUSV29n_UE3rtfKE9xvstd_bCDQw2js3Iu15TlJhPB5Ut98hl9FIugkTU6iZt6k9T-XEfoSomKku1nozq2gbFxx8cCbcGLhTjPtThE_iE6wI020Gu_VqHMSnH-sgq5RIfRqL2z7nI3T06lyqzQgbNOY_dTMDfYMKC2cT0pfNiOnX64VIBxfrh0nTveEwpotfknzVyEeE5bDjeiS42py2Fok0yXZlLutS20Vaf73Sda_oBpVPCc5vHJoYSeLXzjnkMxFaOrORdl_PVw07DrC-qDv3unQrfhgHXApaxnpdADJx8w1x3v4KiNE1Z7PG4urn7RQhWXB_ZrvSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سعید دقیقی امشب‌ مهمون‌برنامه عادل بود بنده خدا داشت‌راجب‌برادراش‌میگفت‌عادل برگشته میگه خودتم سفید مفیدی؛ عالی بود ببینید
😂
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/23929" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش از گفتگو دیشب عادل و اوسمار ویرا تامل برانگیزه؛ زندگی‌سخت و تلخ اوسمار در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/23928" target="_blank">📅 21:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇳🇴
هوادارای‌نروژ وتشویق‌وایکینگی‌شون‌کف آمریکا؛ چه عشق و حالی‌میکنن، چه تابستونی رو میگذرونن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/23927" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh5qfau8cfehzgHe2oaFZo--wdq2UZZsH2nGUYHd8jetvCyjgh8QR5L7iQ9znCnqVi7CyTliwO2DHMR1grYzon3tP85fUaa7rLe-cdLUhkdmVOMUdkURr8gUQkeNHu8D40mT7cYzywHZknAyfCC_bNmjflz6Z7_yzHjBG4Xd3W5nhNQDeINXpYxpGG-839mfcFlGJrdthFYtfG3DhWTLCJcyQ4u0yxhMT3T7j7mhscCslgtM8rrvpYer4o036Dqvq9Lo5a3-DlkgaaDJjs1TKjRaZuMpl__l6J31ucZpreZHIJjdQHv8q4oH3wsc7hDny0S84a2AAkfaMgMxupnJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛دقایقی‌قبل با یکی ازمسئولان‌باشگاه‌پرسپولیس ارتباط گرفتیم که ایشان اعلام‌ کرد بزودی قرارداد اوسمار ویرا با باشگاه فسخ خواهد شد و او فصل بعد درپرسپولیس نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/23926" target="_blank">📅 21:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwavZm3Xtqk8Rn37bM7I5G-6Zi5fESNHB8k1dDUYKoh0PRU2btbserOeojxLff59mG95pPV-N00jPUeGZW9zX10Gqmlp791w-7wSjD3t6Vpc80ojHfDpJX2VdRGc9bOPchrQ3APybJlrQ59uRKuzsg1b_sS5Blh3vn2up797M11pBpn0FdRucYhYwkCxXszHG67ZGNylkZS65CAEPDW-sqL0CMzYFVSQot31KxZCVWyBuJIae_2X6vtkt8FJ2KjTcbI5ui48IvxoeqeKuz1utxYRyn11yIxp1THKEU2YjnCW9c4EkVo_prlPUFvg5qJSgF60zJ9R0f5dxLETyjRITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇹🇷
تیم‌ملی فوتبال ترکیه با ترکیب 300 میلیون یورویی و لژیونرای مطرح بادوباخت بدون گل مقابل استرالیا و پاراگوئه از جام جهانی 2026 حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/23925" target="_blank">📅 21:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
محمدجواد حسین‌نژاد ستاره سابق سپاهان: من خیلی میتونستم به‌تیم‌ملی کمک کنم و خیلی ناراحتم که در جام جهانی حضور ندارم.از لیگ ایران پیشنهاد دارم و احتمالا برای فصل پیش رو برگردم ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/23924" target="_blank">📅 20:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1Qq5b2cAIlS3Fm3xsoUxrK-FLlJnr17ns5J7csDipGP3boV3Pfy8vSqoG29E2jKy8gY0xHTV3GAH2C06Pw7F5k8ZE_0KrkzUB-guQBoQHI52isrQf8XmAaUaZhKeNs-fMkENFE-4cyKvUaodAOJm8ba_cwJi_esfBjDZk2VzxK2QjkmzgS02ghXNVIJmzNHJUyrO6voM9nJ58Ip5FJKcw3Hcd459r06jhzTy1JQ2chfeLvrp7cA_28d6c-zdZzPwUjuR2psy5UXsuDYZ8EnJ7ouldD8rRpj0fFvxfFuTB73HtIzleCuPFTU7wuy1lBRdILd3hApuFSpvJsN5D6Dxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23923" target="_blank">📅 20:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gX9SHj23mJRUZLTZeojjx9OFQf5cNDMUBRsGe5X9H2uKbHqYahmHytoUCXUgOkqWSoxEH7zRTmv7DTORJqzR42EUnb04D8hySOiidIBB3CV_Hm7lgMPWebtKkkPbhyEKPt-2Nz_mlBfCNAbjyxfFL1NiVO3PNqRJbjO8nm0oBqqC65qWHpS_VmZ81aBjmpEl_AjHZ49r-ALpPx5frSkAZz9mviV_xnMnOnDJYPzMFx9Ya_KKW-lvkjd7iB0C79suDU4RIQxERRhNdafZ4TWB9YJ1CndwGSBHIqZ4sVxq3tCcjncW5mOYWrB1r35zOo26mJqzffDY5Ge_ipegs7FTuto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gX9SHj23mJRUZLTZeojjx9OFQf5cNDMUBRsGe5X9H2uKbHqYahmHytoUCXUgOkqWSoxEH7zRTmv7DTORJqzR42EUnb04D8hySOiidIBB3CV_Hm7lgMPWebtKkkPbhyEKPt-2Nz_mlBfCNAbjyxfFL1NiVO3PNqRJbjO8nm0oBqqC65qWHpS_VmZ81aBjmpEl_AjHZ49r-ALpPx5frSkAZz9mviV_xnMnOnDJYPzMFx9Ya_KKW-lvkjd7iB0C79suDU4RIQxERRhNdafZ4TWB9YJ1CndwGSBHIqZ4sVxq3tCcjncW5mOYWrB1r35zOo26mJqzffDY5Ge_ipegs7FTuto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
‏یسری‌از آمریکایی‌هاازهمچین‌جایی‌شاهد گل دوم تیمشون مقابل استرالیا درهفته‌دوم‌جام جهانی بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/23922" target="_blank">📅 19:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUopnUl1RvUT3_oKEzlaxwLG35tbLU_crEB8LIZg9zFeNz7HHjJQ1ke-MjS2Cb644-qUz4gn9j0vqvJDi7GTb2uKNQbDMk0mrnunzbnkpxc7uXPSD20LzXftk5E2TXejIFdVD8zz7Kxh99qPL_DWcUXWkiWXqh_k3jHeZv6KyV_M-x_A404Rmtu47POz5FDtndghou7NW2kj7Bds4OULzIYln8NL0o_UVv1X6Yo7JbCYP9jeM8pdPX6mYhxMA-g0abSWQyU6T5e_nABb20twh9g9k6PtxZjEpNMun-iF5qCuxrTcI3uJHa_YAwcxtzjbUOTXmN8wQl5b0egLJudRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟢
طبق شنیده‌های رسانه پرشیانا؛
سید مهدی رحمتی در روزهای اخیر مذاکراتی با مدیران باشگاه پیکان و ذوب آهن داشته و احتمال اینکه با یکی از این‌دو باشگاه قرارداد امضا کنه بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23921" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gr_0fC5TXdCEZEvb_dJXn-HxMrjz1SFJNQiKc7uULzUSE90wLSqVI0IJjhc8Fg25hltLkOWpED_euaSC1azAkpef0JaToNvQKvJdMEwiFSdpbfCibccO24ZqNN2niDsvJHJTNjgK0X0eA-6kgRSImW9nxF9X65M98Juv7LSGSqD0uyo55TMt7SECvUKu0Mv2Bya-ugXZbvfBKe5OjwORyLSWq2s9JCL2s9MiLCyygF-w8EQvUeMfMQ3Y9FZ3NKIvWuurS_9OYFh0y5EEx7yzRGXbXmp1gSDHJL0RXnenhGwzOZA9l1FxPQg5Ks1SlCrqfcDHSFqoQ7u4xvSu9Cp2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHO-KiOm5DwLnzQsY2x-8UGlEGZppSa_idpueb4OFkn8_Yp2mm2v69pX9W0hZK5MaIJdShBMI5d_QgmAG4MCAVzpverge31n4BbZo6_GVPySJ4J3NeD5U2rLhNh78eySkrF-7eOsHdnD195fG77pKEq7e4H5COR687o0bNDuQOg6Lxk4MUtdPm0381KfGaUX776YcnEMicXyPr5GXgJ43nHJuCIqFarYAxLRy3lnDg2SotpOxY2GrTHwKXCGctjWTluay7_VCDAyJck82ULWtVwZtPGhPS59LE5Z0ZJIGLOu2-ggs4HeOb4fHHNaVM6z-aNlm0y0I6Ni2lYVXLAR_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/23919" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413165ef88.mp4?token=fhNyB-KgMUYobCvtlzBtUU6G3jWCX_SEvFLsGuVNKYLLbd_Fj9WDs78FwNX0Qa5rcqPDFZJQEzZjy7KimsDcNt4vu_MEr_SWikvztScbwNJ3Vf4cbi_0paq6SxhJxejH-0dGa_AxqP9GsYOwoZD_cjRJXZlLUPF-iYRPmHwsH1Txa-EifK_hyrjq92JhwI4BAKatkXtG6hVH8DBk6wrZ5LbEJJDCv0m2A47F8syvwcT5CBKvmljjzDLqvp7RqNriX3lEvQZXRj3xfrI8JxsZcjuT6IgHqaOC1OEhy1a-DWRpjzGZU9HvTT9dxCnZ81zfCcufFvddU9EMTExxHV0kQqE7TQPwIIx-wq3HoDnYwPxb0GyuBKeEZ3zM1z1ZtXEfRfVivTDeBcZpa2H5LrYijRC0wZD83ITCnJbrczgHFST-j9KrqVf26lBSYihWgN33ZMK2w-eIejcRdn2UUlhNwFZkxHx1xyrGXp7QImNjHxn92KB7v2oO23MO9KKLocZ_YQK4SMUbZi0wqlH451TsWg3R8MYeZWU5-HWHwpwpB48Ygb2b00Pr3qXqqeU5dQ9hG5WJ3-6bwgxMl8pENPOBfwvG0WaDSL_jULKA6hf2SBfNYEBfzXs5V1UB0N1hWuaeG7F0PgrzfO4yxAEFJcmwaICS8MQCHVFdyqrM-hokZP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413165ef88.mp4?token=fhNyB-KgMUYobCvtlzBtUU6G3jWCX_SEvFLsGuVNKYLLbd_Fj9WDs78FwNX0Qa5rcqPDFZJQEzZjy7KimsDcNt4vu_MEr_SWikvztScbwNJ3Vf4cbi_0paq6SxhJxejH-0dGa_AxqP9GsYOwoZD_cjRJXZlLUPF-iYRPmHwsH1Txa-EifK_hyrjq92JhwI4BAKatkXtG6hVH8DBk6wrZ5LbEJJDCv0m2A47F8syvwcT5CBKvmljjzDLqvp7RqNriX3lEvQZXRj3xfrI8JxsZcjuT6IgHqaOC1OEhy1a-DWRpjzGZU9HvTT9dxCnZ81zfCcufFvddU9EMTExxHV0kQqE7TQPwIIx-wq3HoDnYwPxb0GyuBKeEZ3zM1z1ZtXEfRfVivTDeBcZpa2H5LrYijRC0wZD83ITCnJbrczgHFST-j9KrqVf26lBSYihWgN33ZMK2w-eIejcRdn2UUlhNwFZkxHx1xyrGXp7QImNjHxn92KB7v2oO23MO9KKLocZ_YQK4SMUbZi0wqlH451TsWg3R8MYeZWU5-HWHwpwpB48Ygb2b00Pr3qXqqeU5dQ9hG5WJ3-6bwgxMl8pENPOBfwvG0WaDSL_jULKA6hf2SBfNYEBfzXs5V1UB0N1hWuaeG7F0PgrzfO4yxAEFJcmwaICS8MQCHVFdyqrM-hokZP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی کنیم از این صحبت‌های علی دایی عزیز اسطوره مردم ایران درباره رونالدو اسطوره جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23918" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7b4hWZxC2w3fSqL147NDxVy3SlY6LwqV4GwzrhQVn0dK2k5XZUk6vpIDiEMBV-hk_Cwu4HNvvhFYg1LdKJwQ0hkSjU2j3yDXgTXTgY4gCXA-Ra9eKGPxD917Vgyiap6nYdMDYZVKy0fzL-fvctDwsOSIfgAjOm_dNg4e4JJD372Sp7zkiB4xtlX1ua-RiDxwnda12kU0jr6amd0_LpBYv2lOXSWjNjC_adD4Ls6i8knXc9OZxQWCUEGuWK9DEnLhRk7PbGMofklWPjjH90db6KRlk6TZvxMx_AszHkJzgfGFoeO7Jw7e2XYeOsZ70YV9EkY-KlCtBXkx_mdUr2ycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیاز جمع‌کنید و برای‌سهمی‌از جایزه بزرگ ۲.۵
#میلیارد
تومانی رقابت کنید
😍
🏆
هر پیش‌بینی شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود eg30:
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23917" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQzpxksQS0H64lv1hJnvbkfaoEnYeJmKU8A9LpTdU0P9c5els1mKpow7VXrdbOJiqHeaAgfpWw8D7qBenzwSS5Osr-eBrR-0w5wIYrGaElj5h9xHwFYs43qxWPYqS9S3lNPS6paR0nnVv_wG9WnZCXV3X5JXBk4tHssyBmsa3-dKBrZHo_j7WNP0TCoUAuICPElOu88ulXgKJSTC81m-0-F5r1c0OuEHgrRglU2fXKnd7klZNAA1ooAOl3b8qqfgZE4aFvERu7_VeIPGzWvKIY6IyqLyh3PXTQx9eSFRHEiIoURA5H-ptKRNy8rnMdBm_DjKLzQx-sRl6303uW4DXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک: تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23916" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQnjuLbspeIMTdQG5d1QWiqVPPuw5SxPVEeWU4nk_g6qI8P0v-jp752Pi23LZDg-98oUxBD4CzpNnQR1sk0OWO_9cmvuZ7bzLef6ORbC0aih0eE33GrYEe1hdIIFESVxAiTPJIKH2zzH7Ls7UO72KkPrs2F0IE6vbXDxP7_b8j0h1pvT-PwBt4mYNWLvXYLU6mcagb0CfOF1BIt-HRLZIcrnQcTcrubMng-6lRXXeJGrsKmCgwULmoxHgBgWWxe2NJ_E7nCfPovg0Z8arTaafCiKAvscIYmlBDTtCpG-ziZF3rXgpglB3KT75jXcuiC-hSIJ0liT5qrBJuNzTup75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیش‌بینی اپتا از نتیجه بازی ایران و بلژیک
‼️
سایت‌اپتابراساس۱۰۰۰۰شبیه‌سازی‌نتیجه‌بازی ایران - بلژیک را پیش‌بینی‌کرده که درآن شانس برد شاگردان قلعه نویی ۱۵.۱ درصد است.  در این پیش‌بینی شانس برد بلژیک ۶۶ درصد و تساوی ۱۸.۹ درصد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23915" target="_blank">📅 18:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=u_JlP75LTtaTqPAzFdRSgWvVjhJYxO1vFyXGqzqDOGHrIwHvx7HnhxtEDUC91HkIeFwx1vNN1orb6oLDNwiLFq-dkAU4KyGSsC_IY-aXkKa2v1E30Zbcx4dPMsYqsAa8dVIg2GOZ1qBgvAqq-2BQCfTOu5r24ptNAS7j1ypbcXozupEOyJ7dtpJLozHJ9wUf3201-bmN7VfpKY9vV84E-mOxDWJ2FtCFZ-5pbBh_lqZv6s1uch9kuxRp2Gfx3S8KWQwOA7zJGMz8YQ6zuILrPADZaQxGlsIV43KrbAGOnpHWmemho5j551BqyC0N4tb3LMzfANgM44ZnAChG8SG4tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=u_JlP75LTtaTqPAzFdRSgWvVjhJYxO1vFyXGqzqDOGHrIwHvx7HnhxtEDUC91HkIeFwx1vNN1orb6oLDNwiLFq-dkAU4KyGSsC_IY-aXkKa2v1E30Zbcx4dPMsYqsAa8dVIg2GOZ1qBgvAqq-2BQCfTOu5r24ptNAS7j1ypbcXozupEOyJ7dtpJLozHJ9wUf3201-bmN7VfpKY9vV84E-mOxDWJ2FtCFZ-5pbBh_lqZv6s1uch9kuxRp2Gfx3S8KWQwOA7zJGMz8YQ6zuILrPADZaQxGlsIV43KrbAGOnpHWmemho5j551BqyC0N4tb3LMzfANgM44ZnAChG8SG4tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخراج‌المیرون‌ بخاطرتوهین به ترک‌ها:
آلمیرون بازیکن پاراگوئه به‌دلیل توهین‌قومی به بازیکن ترکیه اخراج شد! تو قانون‌ جدید اگر دست‌جلوی‌دهان بیاد و مشکل پیش‌بیاد بازیکن اخراج خواهد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23913" target="_blank">📅 16:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=cYL0vGmonC4xJ3_W1LPEON54YbkZ3sxntXMb1cpcfTJV-cOAZh-_I7-mACEZU_wqLv6jQ4pbU2isiALtN8NWSyA2W3grlNn9H3FkEUagzl4wVPKTQHe-omcmwjK2PywS9waDTsA9OdbL7gqZW-SfyIrIFI0zDYuUPS_wbXgswXKJqTE_9NbKliIS7Vbcmkshkc8JZZNFwvudX4oGpSqnUrAYVu0y6-LfTamnxBzCe8EsR2WjeApmjUq0hVku-x30EGr2j5CJ4RBagWn6_gRwiGjDseQq8iX5gj0kmD7OR9QOpMKcWtXMOWDkB0CvlPedO6cR6IFwQ_Qg1hFgU1FYqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=cYL0vGmonC4xJ3_W1LPEON54YbkZ3sxntXMb1cpcfTJV-cOAZh-_I7-mACEZU_wqLv6jQ4pbU2isiALtN8NWSyA2W3grlNn9H3FkEUagzl4wVPKTQHe-omcmwjK2PywS9waDTsA9OdbL7gqZW-SfyIrIFI0zDYuUPS_wbXgswXKJqTE_9NbKliIS7Vbcmkshkc8JZZNFwvudX4oGpSqnUrAYVu0y6-LfTamnxBzCe8EsR2WjeApmjUq0hVku-x30EGr2j5CJ4RBagWn6_gRwiGjDseQq8iX5gj0kmD7OR9QOpMKcWtXMOWDkB0CvlPedO6cR6IFwQ_Qg1hFgU1FYqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گرفتگی یهویی عضلات پای عادل در ویژه برنامه پریشب جام جهانی؛ سه تایی غش کردند از خنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23912" target="_blank">📅 16:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsV_DEs6mJATN-XRnGnkUj-qTWd9mxfv4D-RZz6Dl5UolhoORP83GNR4xCK7DKr6XFOA7OQNR14MaqEaPLeaYe0Wnvxb5ms67TZlWI4eBY0xpVmiRB8YESq9MIyLwI1nhmqGt3NqbC2sX6eMlx3wBgD4xbKU14gXPcwqzkHiiQsZ5v0nKzs5w9WkqpqhHs3MgSsYbAgIu1G52mD9eyNzbXAIERS_OYCtweqV6XEk4TuKqPJ-yghVYn_alNv9lZdnBLpz1hrPlf3rxasmFkuj_iuAJ4Kt7ngAB2ITSXNeAnUKR4wLyyTizub13QmkT8HAeSQSUky2pkvb3X7NbbwsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23911" target="_blank">📅 15:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLxa4iEGD08MZPvyIW98AKsA7bAO9NScgtjuTb6WK4XWV6I42vrCzw9hpmb8b35Upy8OWCoCfUv23fLj2oRboLtq6NdgRWi1YB5AxWrEU2mGTcgYp6WVtKlLLaqXKUnXOtVjKdBQ2EfG3TqT1ryMt1JtMV48IyUJtiIQhvyuMLsBFz6lWHUe_AHwtI3OmnYIIo4XVJyQGoNDD41a0ocz0kKQ38qpJDJe60leLKjHuOEJREXVjAOdDVTmiZgnRijO1bMmLYI5_SvVV45rwo1g05KIw5BxVuX6vswsetcrlTlzpWQv_rHtrKEFQK5CeF8U1vkGv2-zELPzD93qW_stIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23910" target="_blank">📅 15:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=AFavA2eFhHTqiZsWd8Iqy8Nzkdx3QDy2Syn9UNgnC45AMA04aW_w1eRRGp7si-HPTPiQAlPe_oP2e9EwzM4y6fb9lHYZn7wmGaM3RTc7nCNIvw9EGPsDpQ5mZLD-Vaa2_g7MJhHfWJKSkN7Nqsgp3M2X-2Lu1HSJ9dt1rOLYvYjWM6-vPQcE3Hu3mdZ4sK0cmMrVKiD58KYmFRs8BPHajyIMriVvdwYslLGJMv8gI4qV4ot0jm5SIME9wC4pkz03TBg3E9_iLjvTw9VzmMS2n3x2vGVhARhCUSsTtLWm_o0zG2fZ5-F7uTbbjGGfpSErzlRF4d--WuDj0d6bOngoRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=AFavA2eFhHTqiZsWd8Iqy8Nzkdx3QDy2Syn9UNgnC45AMA04aW_w1eRRGp7si-HPTPiQAlPe_oP2e9EwzM4y6fb9lHYZn7wmGaM3RTc7nCNIvw9EGPsDpQ5mZLD-Vaa2_g7MJhHfWJKSkN7Nqsgp3M2X-2Lu1HSJ9dt1rOLYvYjWM6-vPQcE3Hu3mdZ4sK0cmMrVKiD58KYmFRs8BPHajyIMriVvdwYslLGJMv8gI4qV4ot0jm5SIME9wC4pkz03TBg3E9_iLjvTw9VzmMS2n3x2vGVhARhCUSsTtLWm_o0zG2fZ5-F7uTbbjGGfpSErzlRF4d--WuDj0d6bOngoRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ لحظه ماچ کردن خبرنگار کره‌ای توسط یه‌خبرنگارمکزیکی؛ حالا خبرنگاره اگه ایرانی میبود تا از خانومه لب نمیگرفت ول نمیکرد! این خجالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23908" target="_blank">📅 15:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23907">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYZHF2v5D_k8QlClRyfCy2dyx_2Gx_xeQnbBrDW6Pnp4WqAe9SW0UlpOrbahwrKknMsjYclaII7c-54wv6kAy6CmCZuYl4V2JwMncPkVds59LqmaxWohRbwiLtVkjn0wOlxa8shh2NajY9P0Qy9oH9yqQSJ7dAUwH9D4fiIN8BjozlnrAJRfSpXRtj4WfU3c29YY5avPiGL8k08H66rk0yWr_hDikSFz4zsDXymyGHcB_fi2Ij4mljuk70jJjvv7JwdGBzSQ7Pe-cZfQQnGDhNu6uyL73daHsemwDkaE9M54xWeQmp8uLHLNMH-aJ5PuAAmJ3uLdl9aUNji-ssTyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23907" target="_blank">📅 15:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23906">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkHypx4JSvY3Hthpy4QbOPSSndWJWv7PLjbujmmufyX5QP8Ie-EooIJuqFpO7l4PHWgdU-gzVUTbu_zcxaqSoOh9MCMmHI5HeD-ZAEJRmz7O6yXCYK06DQovS1rBxqLVPgDoX3ruKMRXNEiyTAALRBvCUdx2r42DhmWs6j7vO06JhhDjLK7dIFUQaKDB37lMPj9RH4Xs8eXAP9M_qGq9Zmdf6sY5pywasG5flGdUXnN5qaAcBo0zNAIsEYxzXEfSCMCodYVpk6jVl6MEOA7dKaH1WSS4BPnEgyKHE_PvjzqKirVCQe8wINRYXO9ss4lfPWb3WCislip_MIngKPzj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23906" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23905">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl--t_ujsnkzdg2QumfNs6wFJDwLZ_I5wT8BNfzmIwHWwCLEUYlUBNw8OFJHY9de6d0Al0I5zEa5VqcnKVDioUfqaQ34_wDpeDsQEiEGUusk76Gju4Kd5MHbwXIj4HJADN6eb68ym_te_7xlxE8f4cVHx64s1J0QGG2SbQkhBovouPe8-558bcaMQJvo5v1UnNil2zKKgpUsinvdaRaxhKWKPAK3VQ9zF_E2uVMDBijUtfA7EdQEeP0EzxIfhOvpdFypdf5gIqCszWQqhh-wRjeH61z8eaxrTLbadk3f9h8qhjLxDIWbNc-XanspDymYpSCb0Ae0TxQgYemiAZq0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاسمیرو ستاره‌خط‌هافبک تیم‌ملی برزیل و سابق رئال‌مادرید و منچستریونایتد برای‌عقد قرار دادی دو ساله با باشگاه اینترمیامی به توافق نهایی رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23905" target="_blank">📅 15:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23904">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4fNl0pwje9QdvmgVRKDF4bSfCM4RUkKF9SoKj2ki-zzhh230vjNL8Cce5uBSFEev5l5YtQRoFgXjD2hjA8muMb7wxvLRWDx6tvPX4fUz7AvHDKZ9F_O-jdyjLy-dVpnZMs2k-uqfKvFCXuiykZwMOZXfoefwcbXndlCuQWN0gCr9LLicwuq2WnyAZh3YOAIKmFTc3BVBrorNTrdap0E7o5LgGbDYoqyyd1Ta6KsMWu9HbggvsWw1NWKSOjWurq3qrPiT0p3DhWVmCqYtc_0ibxysl7nje9-NDeHKyEDkat-Nacc8TGP7DZaG3eA61_F5cBjgGyNT9rpbvM0h1MixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویژه برنامه پیمان یوسفی برای جام جهانی بدلیل این که علی فتح الله زاده به میثاقی مجری سبکه سه تیکه انداخت متوقف شد و به او اعلام شده که دیگر حق ادامه تولید این برنامه رو نداره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23904" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23903">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=PJMvRNc6vBBqRXKCmxPmPgwQMtM4r8-hVw4DjANmC9a19GPThwOo28fXbtM-flAfPhIm7v_ukx9h8ufHfc5UZ7u2ahizdArJy8jRB4S072CMzSbXJkqSlnj5w9fWUugHNG5pC2NPFlHzo5z2joU0ig_8X2HR7_3LBcm4q5aOW_-hsdNzjm1HRpkGeVZcmoTWfSXFBp98fP94_EJFyyTSxDWuAW_NQycV-52nR6hHztZ__ZbRqupThniDRIvCbBoP2d79d9vL6Hf3PdAYK_Qb5_JovK7ieTspisS4PZDar3qBrSE_yGZuYRzi0dESS_NoocN3t7NPL0Mno88ibxPr9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=PJMvRNc6vBBqRXKCmxPmPgwQMtM4r8-hVw4DjANmC9a19GPThwOo28fXbtM-flAfPhIm7v_ukx9h8ufHfc5UZ7u2ahizdArJy8jRB4S072CMzSbXJkqSlnj5w9fWUugHNG5pC2NPFlHzo5z2joU0ig_8X2HR7_3LBcm4q5aOW_-hsdNzjm1HRpkGeVZcmoTWfSXFBp98fP94_EJFyyTSxDWuAW_NQycV-52nR6hHztZ__ZbRqupThniDRIvCbBoP2d79d9vL6Hf3PdAYK_Qb5_JovK7ieTspisS4PZDar3qBrSE_yGZuYRzi0dESS_NoocN3t7NPL0Mno88ibxPr9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی پور:
یه زمانی من و محرم خیلی بدمون ازهم میومد ولی الان من خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23903" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23902">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpSMPc5bqTLdb2BNvjXb8kn6nr7PxEX5A89vx03lPQE2AnXOpQxpwyEgw31jgs4n8owUdXXyNSzZCrmUR9pGNKkLvs76ES-vLZiNqZstCPemHCAI8-oDM2lFzSOlvD0BP78ui-dlecXNV15XuBdO9O_u3MxBPaYuY1mh7kL3ijG7cNIhjxKjtUAC_B54YfV0kPAgH8b1Yb_sN8ofRFhRoiCjKUBoBX2bPw11E3DVhd-tRPqUdkdTLYt0FMH8Wy7zbhkbRuK0eyu--hK43nMJ5v5zQvfb5kX7uxNv_TN8F9mnS5WVJ640wtww-Jr1KtzEfMOWOMT1h2T-0ltufCA7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23902" target="_blank">📅 14:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23901">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzm1WrQrfP6RHpoGERwekZwgpHukWj-ZjhkHObUIchQiGh0m6ZOglCS2gZtvJymthRoKujHmjxVjzWljJg0Pggk4GoWgPIru-vlVGrJRQx48qT6mngYqWhAIP60hBKXRdjsZn1IdNa5PkJbSaYFgfSe7LZOETZ2rtTMfffsdOVbb8biz8z04GhuluOOsJB_EQ53ygBrsRDuiV9qP5cfj_dJrQUy3zNYck5zFtTjb46dcbZQKLY40R8UlPjim18wDrk877ovR_CRmlIobB8rQcG8e6Yp8CoVwW9S9OjyD-5ARFYvx_urBGm44NLcDLdXrPBon1NV3nVNJdvbZUHJ9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
عملکردشاهکار ارلینگ‌هالند در لیگ‌ها و تورنمنت‌ هایی که تا امروز بازی کرده: 279 بازی و 260 گل!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23901" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJPLDV1JdQJHZhfogcFaf2poSGYglFcpkj4SdoQBsGYZOCw17Qh16vTPwbFV4p2wRitULCINt5cEZcD91DwC5xJiQGBb1aKAdA79tJA84WoXObVtRqXhjGcI1SpXsvx_MSWFO0TyC8UKjxyQVNyrnloX8dHMdkCbRV094sV_MWdRIYKiHLfbzV_I0WNnLocVLZN-UJ0w3qXa7eHiV2_FKibDDJ8pEUwkrj36p80R60pTlW3yrbM9aKwbhZ_zOOR639mk9EOoaxxPy0tMaTMxXRG7XvrqbVWtr92kqEIxHuMKjR5qon3hZ3q0IiOjp2URcvq81WEOPQfxS7YYLQ_ZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال؛ سهمیه خارجی باشگاه‌ های لیگ برتر درفصل جدید چهار عدد خواهد بود که یکیشون حتما باید آسیایی باشه. به این شکل 3+1.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23900" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23899">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuabUtGAQk117PZ94MGcVua33YwJLdY_ENPs8biQt2JLZx4OYoq7nDzsHAP9hzyBxRZubxd4jAskKOD1TeidEVu5iue9AUqkLg6CPl4nzGO5zpBApiw5SrBU_x-eIW9b8keB79ZsJbBKRfp9DslGCHsuL4gOx27fOT-5kG_xChUrmwPVepPc_UwjjWRLXDyVFyscxS-SpnXZX6TsKQXfjRxZzqBnuJ1_OUplyE7umMNwtXyWo1gnCqO4i7NuGR_qWxlEoandwHKLnaHz9GUBeIuzdrlKmXUZ6RcOrDeL0IPi9yQdQX31gnz_EpSUxOdFRJeM3ngVxSack8b6KccjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23899" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23898">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=fxVA4AzG6CVVOUiIm6pr_Xde_-ZJKkJY5CP1eSAbwnxqxb3aze9PbnZPS_7vI2siDfwA_jGgMZp5X7nAdsVWj_xHij5XLt6_Z_pAFlD8lDGzq519ek4jl23qK5z5Fses7WpynyMzQSPFVJMbcHoQhUlfaQXJjy6FPi19POU6MFi528UEtKBfFDXbqRZXB0FNz-YO4wyhQktP8hRzr7AMfei2kSJBZgh9OB33nKdYhH3-i43LX42WvrbLsY9UpK936WEoRVufHQuWljdrmqw1bzGZGIJjvPOgSDOfELDAeMVFHEJEkilW5ybnijxI1UGWdyzXWdT0SE5Su7ou_ENC6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=fxVA4AzG6CVVOUiIm6pr_Xde_-ZJKkJY5CP1eSAbwnxqxb3aze9PbnZPS_7vI2siDfwA_jGgMZp5X7nAdsVWj_xHij5XLt6_Z_pAFlD8lDGzq519ek4jl23qK5z5Fses7WpynyMzQSPFVJMbcHoQhUlfaQXJjy6FPi19POU6MFi528UEtKBfFDXbqRZXB0FNz-YO4wyhQktP8hRzr7AMfei2kSJBZgh9OB33nKdYhH3-i43LX42WvrbLsY9UpK936WEoRVufHQuWljdrmqw1bzGZGIJjvPOgSDOfELDAeMVFHEJEkilW5ybnijxI1UGWdyzXWdT0SE5Su7ou_ENC6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23898" target="_blank">📅 13:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23897">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=iG4p1b_Zdg7YnmnbnPTI4mdRblz7p7zXDjykA5rT6QHzonsWXjcset5BU6q_Yq2rpMjTP5uLuNxoBIOUwKOgyTDfbFpi4t5zG7SedlaUctU3OAMt-UfajHdtUX_tV3_BzZeAAdpnIwUl4tXN2jBIDL_Lj_L9j1NYOJZvlNMOgNSLOh3zxeQPBFaA5pH_jnA2PN8UWQaZ8WBCJB_wz46R_MFaLGtFbKJxgLyV6P2EqDMnb7xTjdgx3abEuMfv1DHkEfSZOlYfTCLmrdhuBytlLr8A8oFNfC3tNa9xpsMjRIdrqNa0kyyvlf_zv0znqfmUffM0U5PhvG_pnkX-J86W2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=iG4p1b_Zdg7YnmnbnPTI4mdRblz7p7zXDjykA5rT6QHzonsWXjcset5BU6q_Yq2rpMjTP5uLuNxoBIOUwKOgyTDfbFpi4t5zG7SedlaUctU3OAMt-UfajHdtUX_tV3_BzZeAAdpnIwUl4tXN2jBIDL_Lj_L9j1NYOJZvlNMOgNSLOh3zxeQPBFaA5pH_jnA2PN8UWQaZ8WBCJB_wz46R_MFaLGtFbKJxgLyV6P2EqDMnb7xTjdgx3abEuMfv1DHkEfSZOlYfTCLmrdhuBytlLr8A8oFNfC3tNa9xpsMjRIdrqNa0kyyvlf_zv0znqfmUffM0U5PhvG_pnkX-J86W2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی مهمون ویژه برنامه جام جهانی یه لحظه از دست جواد خیابانی عصبی شد پا شد زد تو سر خودش و نشست گفت من استعفا میدم.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23897" target="_blank">📅 13:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23896">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc9m9S2Z_jI_BS9LJCpbqfWmEf7rCWgY-xC90NN3lg-FE9_GmrNz7qCKgUsfXfhPtxNnWlTu571bPBgHmz72hDKn8VrWyZcdp7xUY1ZHipt8PGIYeWswvZ-TPP9wlcLY3lwUky2ufshyXp-Dr63usIEmDg9a3GqUdzvOVDQMvHoQbE-1elZFOZPPW1GYaECAJJ9m7sIHXJcOhiOXpApEXkKg7SHeLz7-VP_LHMPjJiSjcfVma-8iNXkFvhb5dj_ZM2ItOYsy-5p6LwI1dkZUeuic1h0LzAKLnGi-ngwpVtVsF1jj9EtvGlNep6oVUZn886kXhZX_p7Ml6ZoDrOOlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23896" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23895">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1DdSHGZh9Y4NVnSp_ls-LLDIbZ4X0FDuhA-3UafiZox71xtEMZ9jLHC9maq09gookL0AmI8u8eu1nuaXj9cyAcLW4PmT_UG2IclioTcjegG9XH0rFc05Pjz89He27drIENvwa_OCUsd6xohPi5GboAkI5vC5oIceSFfWPWmSYl7IFX2UZ6orFn9w1D3uwQIxMP98JswB3OL3Ku-AjyAkva2xcv2WWyZqx87cVyh9S6HBnJHue5LnxKWWf8cC5f28Da1gSKChO5a6FcB0X0mmu1L88GkktgZ6FsvdTpJMHgFhnESVqvaxWD3H-EfE4DLZKUWf_tbkw6XOtZhIzJ_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23895" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23894">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td3mXa_lEZXAiSPRnxVIlNMZrhxd_yHjMVT-mqGeFFcFc3y2rDRvE8c2oibZArCqTYsLS7oLl4K0ay_h7Pg2V24UxULz3SB_l5CFu8FZxwQK_lFxhq3iGsUysVHGpK1mPBiWbDfEPTbT1Yl3Ugx5P0WXQ4uUuYOCz2omPC2Y1XpXcrkRZh4EtKVgEjVW_S7BdDZGyP6Yhh5ZA-Aj8hNRqIDC62f-V4__67P0ykFookL76rca9Ldtegyua6IeSXmPEg9LxBqlRGT8NCW_mqhF7NUiclw4Y-XhiumqUQ8w1xuLZbIi4IS9xHFjgX1bVDiCFjRQoViYctIWnGi34T5eX0nE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td3mXa_lEZXAiSPRnxVIlNMZrhxd_yHjMVT-mqGeFFcFc3y2rDRvE8c2oibZArCqTYsLS7oLl4K0ay_h7Pg2V24UxULz3SB_l5CFu8FZxwQK_lFxhq3iGsUysVHGpK1mPBiWbDfEPTbT1Yl3Ugx5P0WXQ4uUuYOCz2omPC2Y1XpXcrkRZh4EtKVgEjVW_S7BdDZGyP6Yhh5ZA-Aj8hNRqIDC62f-V4__67P0ykFookL76rca9Ldtegyua6IeSXmPEg9LxBqlRGT8NCW_mqhF7NUiclw4Y-XhiumqUQ8w1xuLZbIi4IS9xHFjgX1bVDiCFjRQoViYctIWnGi34T5eX0nE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلچینی از صحبت‌های جواد خیابانی در گفتگو با امیر حسین قیاسی؛ مجری برنامه هنگ کرد قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23894" target="_blank">📅 12:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23893">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqqLu7js0EJl-TcfT3kiPyzemML-50DAw9YFS56JCeF5EBQ-s-KCCKg2LRWR6PkaA7Y93FT42Ppqjtv2GN4nSTqkHxuTwCigPxd4Q_PIj3S8zYnMkgW12HWbBJel7ePFMbuK_QyKb3PMa_2RDNvW7EqrtA33XfWYpYNBe44EjPTSUdBWZK_SBMp1WeCN8Q2V_yenstMIXIMuAlfPT4SnJv0sS_qfneNz8PHVeGrriKtDINYFu6VYNLgC5luw_v3YSz92DWQRg-Bgrj_UnLamc4gPemK2i37TQ0RItkUWhvXBILbrzYktC1bhA7fYNiGiK38EpFtXk_kQKuFK9o3QOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23893" target="_blank">📅 12:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiR0Z21Z1yJQ5JTzWrF0CDNIhX9uPw4vSGR5ijJEWSZ3yVhjKLkOwHRdlCNSCDhFQ7_sG5WwWzK1gQAyOloJ5EWtTJpM55QtrvdW1PWVdHTAZuSAiAf5GnklSYLaEy1q2m6wOd-1s3dC0wa2Uzh6gyLV5_GrlbgBIiuCXsynmSjgnKk4qdbAfMq39hHhaMNHjnOjDDYM2-D0UtwazkuEKuB_W7NJB23kMPJx2uuS7cc9EkD7rk91_3OOoxwNoGY6oBbGD1jZ549is7VSEnicseOXvojCyaSFiMtV5SblShkKkXlhfus7jrH0Q8vJLPeCmB9hq1p73fVxHipmWemcPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی پرشیانا؛ دراگان اسکوچیچ ظرف 72 ساااعت آینده به تهران خواهد آمد تا مذاکرات نهایی رو حضوری با مدیران باشگاه پرسپولیس داشته باشد. هیچ چیزی قطعی نشده. اوسمار 50 درصدشانس داره. اسکوم 50 درصد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23892" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23891">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=DWtE6acoCBVhrE3kG_sODbbKM9tAH0ez465biGEj3mLKzghPNEzVzUhYCnS_tKHwz5XkMxmoSj2ZC3cjYZRLfTeo1RZDDPulk3NK6JzR22Vt4uFpRHgr9KuYvxI783Hexi--O-Yqeq4OflMdtMR4S0E8dK5QAoczICP6r5ae-FZb6h-wE9dPDMwBECjqaDXaFaUn0NQGD37BDrh6gc8taWMWU2rPQM4Eoz_qtIupyngjTPmhjjbpOYDI31mTYYawhvKTicHgKWHtwrlLEH4p44ZWAJzyBWGO8On-QkFq0WOjVsLFZpZyE_sD-VjxdMzcrO_wTOouP0XrbOqyI-OYDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=DWtE6acoCBVhrE3kG_sODbbKM9tAH0ez465biGEj3mLKzghPNEzVzUhYCnS_tKHwz5XkMxmoSj2ZC3cjYZRLfTeo1RZDDPulk3NK6JzR22Vt4uFpRHgr9KuYvxI783Hexi--O-Yqeq4OflMdtMR4S0E8dK5QAoczICP6r5ae-FZb6h-wE9dPDMwBECjqaDXaFaUn0NQGD37BDrh6gc8taWMWU2rPQM4Eoz_qtIupyngjTPmhjjbpOYDI31mTYYawhvKTicHgKWHtwrlLEH4p44ZWAJzyBWGO8On-QkFq0WOjVsLFZpZyE_sD-VjxdMzcrO_wTOouP0XrbOqyI-OYDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
واکنش‌طرفداران تیم‌ملی فرانسه وقتی بعد چک کردن وار فکر کردن علیرضا فغانی براشون تو بازی مقابل تیم ملی سنگال پنالتی گرفته ولی...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23891" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBr7_7czQ5vKhyKX_UMqVUt3lFODUFgaB9BxfURMnIUw5urH6u6yxAV6BgOXCc6Qxn-2XRgjYYQKXrQd-7AYD6P0wH5ejp9yys8r7CBVfcg1ts5InwdfyQP0i3cSmouszDu-Vsb_VNF4SiepoMBn5yS4T3qYCBrOQS8El9HMdg9TMrlFxwv4ZHBcJbMowoOKb6wrcmCw1NioL3HTRxOxnVwrgmcr2Snj0uI4E48JYF7Pv2Yppi54jL0CrvXw4_X6ub7pZEn912PWpClRFR_Wvo1AI_xPwCiLy83-AlEJo_zDxpFG_QX_j_srPcyFUpSy4zpf_7h3HF4kV-jX4WQBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌فابریزیورومانو؛نیمارجونیور ستاره برزیل که به دلیل مصدومیت دیدار با مراکش رو از دست داده بود حالا در حال ریکاوریه اما ‌کادر فنی نخواسته روش ریسک کنه و او رو برای دیدار مقابل تیم ملی هائیتی خط زده که به آمادگی کامل برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23890" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=dUXCXV2BVlR36luqsgwptxfUy-7J844WmRbz7ir2uZYSEa8IQp87gTTc1bpAMNosxc_E53fGmkf-GDjOoaY6ZFdgpTpIZbJi5PFtrWatH4Dv9bMMLDLDOSOHEtOsLX4eJCHY6hpeqm_VzTpEUz-Wfe1J8NGjhpPzlzTZ6BEH_UcMUAaPrG-D6wN8d17ls6CaEcwI8Jb9SyiTEiQ3wmVvjWDWTOArbvdg9hTMU4rGy27U7WB8hBpnRBV0BnbAEXrwedbUxzp8x4uI8rX1OKELIAwB7LyIvEsJDAG6EMk_M-S91FTMPQZFDmTq9kEq4WU6Z8oMPZFEpt4_9vvg2ghLbr6v7n2Xscz17DX-Cqg-hM8WBKJGQof5MwlGIWNm9jfX_OTcdR9m-EjDI4-ZXdJfILP5OyQBEVS6wcIzV_6rAMYacYuLGiAp6YQ-HS8ngtBv91vyc28OhdTOSoQXGnMrq1FNB6zXyImLV3q9OfTiE93HtWksxMKJUsJP6_J1OsxFoX98g0ZHuDBzMRnU5Vc0iWkm4Gin8xMjuNYWzeeTt4N11A2m5PaBKfUZDbLqmKVX0vZyn6ktrS0li4ubfxcKr1kOo1xKOuiXFkOOWUnETi9j52t47k0-EnQwLjbgrvy92CvkVy6UMrd9cDapBAK1Dt-8jGnXHz3Y1hsbNuUOOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=dUXCXV2BVlR36luqsgwptxfUy-7J844WmRbz7ir2uZYSEa8IQp87gTTc1bpAMNosxc_E53fGmkf-GDjOoaY6ZFdgpTpIZbJi5PFtrWatH4Dv9bMMLDLDOSOHEtOsLX4eJCHY6hpeqm_VzTpEUz-Wfe1J8NGjhpPzlzTZ6BEH_UcMUAaPrG-D6wN8d17ls6CaEcwI8Jb9SyiTEiQ3wmVvjWDWTOArbvdg9hTMU4rGy27U7WB8hBpnRBV0BnbAEXrwedbUxzp8x4uI8rX1OKELIAwB7LyIvEsJDAG6EMk_M-S91FTMPQZFDmTq9kEq4WU6Z8oMPZFEpt4_9vvg2ghLbr6v7n2Xscz17DX-Cqg-hM8WBKJGQof5MwlGIWNm9jfX_OTcdR9m-EjDI4-ZXdJfILP5OyQBEVS6wcIzV_6rAMYacYuLGiAp6YQ-HS8ngtBv91vyc28OhdTOSoQXGnMrq1FNB6zXyImLV3q9OfTiE93HtWksxMKJUsJP6_J1OsxFoX98g0ZHuDBzMRnU5Vc0iWkm4Gin8xMjuNYWzeeTt4N11A2m5PaBKfUZDbLqmKVX0vZyn6ktrS0li4ubfxcKr1kOo1xKOuiXFkOOWUnETi9j52t47k0-EnQwLjbgrvy92CvkVy6UMrd9cDapBAK1Dt-8jGnXHz3Y1hsbNuUOOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تماس‌تلفنی امیرحسین‌قیاسی با «سردار آزمون» وسط برنامه بفرماییدجام: من ایـرانی الاصل هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23889" target="_blank">📅 11:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGraSaI-9Fcst90tlBJaTvqEfl5EUyvhzphcvR1QKQCDH6Xqg-FYM68BnMbEK-zhY93x2Qg4xFJFmNNzsY7vahoOzKZryibyY2XLTmMnNAiyPuRVTZEx9Z0_Ij7BSd61f_seH4IOXneExisd0G7ub4F3P4Po3tzNSquZflsGwT0qv9mZ9zxgHUkR18rbLWwmQJvbaNVA3KJ6MSbsoFgc63jnSSUPoqWCpQwt1Aphj8L_BuDur_TFND6k-ADSQktoO2zxPWbY7lZ1kugckFdKMZZrewlXrgFvgP8oNJTm9XTdwHa13DJV6dqpCh_gpN9Git5yhQanyAoK1LX1BA47jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک:
تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23888" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55029334cb.mp4?token=quBC_UIEFjCV7mQv_e0TDyKQ5c1DhNaotp1_BvuYKydVioQzl1WdLrhHTUTHXIjQjI2ZMIlsLsyPxMgzEZQ3NiURRsi4U3WVJeh5-ZYgnMJEYk2BNzpiSoQqf4U88GquDMoA8Xli_uDHR8nUjeBzHh9YpYBvRmhJDUQmyVShEHBRSW-i1dEscrYgFc-zZRtLepZEWMN_2vFyah68laNG8Dott0umxKJ0E5cJxg2dORtFDC27YB2oE694js2FASpQTzhHcT_qBM2zUQWWabbVNKixWaaJ3xJ6R4-dK4fiqvEPN0pZD7kTZ95imtABuwhW4XEWpeTME6h9nrkOgiD_Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55029334cb.mp4?token=quBC_UIEFjCV7mQv_e0TDyKQ5c1DhNaotp1_BvuYKydVioQzl1WdLrhHTUTHXIjQjI2ZMIlsLsyPxMgzEZQ3NiURRsi4U3WVJeh5-ZYgnMJEYk2BNzpiSoQqf4U88GquDMoA8Xli_uDHR8nUjeBzHh9YpYBvRmhJDUQmyVShEHBRSW-i1dEscrYgFc-zZRtLepZEWMN_2vFyah68laNG8Dott0umxKJ0E5cJxg2dORtFDC27YB2oE694js2FASpQTzhHcT_qBM2zUQWWabbVNKixWaaJ3xJ6R4-dK4fiqvEPN0pZD7kTZ95imtABuwhW4XEWpeTME6h9nrkOgiD_Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#فکت
؛گل‌اول‌تیم‌قهرمان‌درجام‌جهانی در 3 دوره اخیر این رقابت از روی نقطه پنالتی به ثمر رسیده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23887" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O1uSboyGPbOStG5EiwczjbvcihBc6_I1huxguqzU4_buVUQm9TUb9Me5BP-toMJcI0tunYJu6Q2cKRJAFXVHjHKVTO_bGQPUPLVbO4V-nUihEsx3M-AELqmCM4iaBKs486IFTt6LXz_nS3HO5Gtl2Xlkeo1P-7pN-O9JHba6P6h6mVY-sZd1mWEVZVH5vUY_UvlF75QhSmIpLM1wV8SC7GSVxObBtrQjoJXBQtUFYrmSnzSyA6BAYd6daz8zygGvHCUPiO0GZQg3xT92K724IgH5d8F4JlMyJbcEO4lpnmIG6ry0E-ZWIX0GKTmTrBeAW2NMtIEyi8jU84oepCBqvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
بدلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🌐
MelBet1.net
🌐
MelBet1.net</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23886" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQJnvbW4PdHV4hyCnfbL8avtOxw7Z6297cMHzV3_L8tpW8tIU1RaGkxjCIVy7m21CX4ltjQGIY3Tk5TrfPILIuPKPZPM6Cf64IWOuTJDSIfmiwzL863cgUDdC8ih2YWQPswcW_iPXajK4uPBzBgnp4eEEEevFyhxwmnVYBzIB7nKgcn-Hf5q0dlaciqcn-iyoag5U_uExMxpjB-X5C9XGgYK_F1FSPBYAljxHsLpF4EpvfsXea-7xjjDPYXJGwMfWeXEikJxC3-qAllNCiBsBUKyHx-IQoeB6AEqFSU7wdqyThGQQQGw8_RKgKergJfDvH4LJDJCgUlpAY7TZx9JVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23885" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=oM-xOesnNoUp2EZrXQgofdXDiub2f8hlTzjCehCpWrAecJKj1e6bFUCR3D4rq_GcBfmgPDZB4z-y39BPya291K4ms641YH5dS4pzbRhoFdZBQkxgKWDlJ-wb8XfWmXaLwxh6oBd18N6iQbJJD3TG42hv1Ts0YPOLNo2G1I-86FrRaLSNN2_hIisT6y-DSDWn9kGqgjakCZgQwMwMKVEfLBDCan2FM6m_AkOUXdkRFgmb7OK6K0mTAwJ7VO3JjB4BtyZMD1HcFRPtYEugZW15VIvwQc6q6_-RG6oDlIuluAX1U_DDMxmoGUOGXCvgGk3oK148YbIZdv9TISYR0mc6nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=oM-xOesnNoUp2EZrXQgofdXDiub2f8hlTzjCehCpWrAecJKj1e6bFUCR3D4rq_GcBfmgPDZB4z-y39BPya291K4ms641YH5dS4pzbRhoFdZBQkxgKWDlJ-wb8XfWmXaLwxh6oBd18N6iQbJJD3TG42hv1Ts0YPOLNo2G1I-86FrRaLSNN2_hIisT6y-DSDWn9kGqgjakCZgQwMwMKVEfLBDCan2FM6m_AkOUXdkRFgmb7OK6K0mTAwJ7VO3JjB4BtyZMD1HcFRPtYEugZW15VIvwQc6q6_-RG6oDlIuluAX1U_DDMxmoGUOGXCvgGk3oK148YbIZdv9TISYR0mc6nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
بعضی حرفاوجملات هستن که ارزش داره روزی چند بار بشنوی؛ جمله‌ای که این داداشمون تو برنامه دیشب ابوطالب گفت واقعا باید با آب طلا نوشتش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23884" target="_blank">📅 09:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4i9YMBOLEZbuPfU9zt8UM5omuDDXl7m82S0jsxT72mUT5U0nfUeqW1AbYnoSrjLrGZk1lwbnKUmap9Iydge0DoOCUDMrSr8OPFCbyLMzvpptiH_Q4jAkl4PoNESaBQM2MJTv0AZ8GfqtBEWl3IXLK4NP-oPgFIrER8N7t_whtQbP7T6CUqcp7Ppc4n41EsP_AjJIgX04bsADwsnb0HjnCpUz_BdxoMqx2e3dLO6FcOYKkr0SI3WLJe-iLyzWrwc7K8WpdZMv3YMhm4R2ARwewunocrFxNmwrn8g2L6mUeSu-bvHdnUTKD46ODfb9mO7n9NYnC4nWt4-e-pBdr216A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یادی‌کنیم‌از واکنش‌کریس‌رونالدو وقتی مسی بعد از کوپا آمریکا 2016 از فوتبال‌ملی خدا حافظی کرد: دیدن مسی درحال‌گریه کردن واقعاً ناراحتم میکنه و امیدوارم به‌تیم‌ملی برگرده چون‌اونا بهش نیاز دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23883" target="_blank">📅 09:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUGPbd6oqt2VdnYq7xvUCccHVwe9-ODyfKFdigOSFgW0YKUIY9y9I1Gzx16XfNleobbEhFRRrVFQv1tkgram4iwmPAwK2_irPU7MYUOj6dLeuj4cZTGcp1Gm0-MWPDqvOA3VJaY8CS534ePsHhD4i0IO6g8AQbXLgU8VRgBHdZYU4QTanXSWYjYpJnLXjo4ZSQpm22woPoOUu2iptLUchS_fcPfChlHTucbqxZMHcsX3U8Ix336WQKO5mriQ1CcnsqgBRJM9xtDhp4VPEYnWJA1qcMddJlpnKW6jzOjHy2RmXso2MVYfIxtFgECJcprQnaGfTeDSSEg4bzlByZJS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23882" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCF7RGurFKaQ8gWBWL_JlBGpII6JNidSuHKKByWB2GATJrUVMvxcgcu1lGOHSdapQjM0nuRSE8TqMVBbj-9GObAqO3dskNlFxi317E0eJvJpo9qIE8WYmdXQkz2NucVssRZqc2i82Vg-glrqOhxr3ZQuZOrF81m4LaB1yxFI4kjUBHj2aO9OPNAK_Zvnzs0f2prw5gBzurlEMYrHKryTzYrW9oi2laxgFBRtBAXO5NezM3_tNepP8Z0LG0M76etjWjxIjRG718BlmtEim6kCEEMKdX8MCm6Y7tOI4kUYqy1LDKouIfh1pzaI12k4PodYxOizwf3rJJ7QgR-HZAmRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دوم ایران در ادوار مختلف جام جهانی؛ پبروزی دو بد صفر شاگردان کی روش مقابل ولز بهترین نتیجه در هفته های دوم جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23880" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23879">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23879" target="_blank">📅 08:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23878">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu-ds9iLQ-1L4T9i5a9PTVr-fqZ9narnEyzAq8DmjEy7VhSbE1p2VY1oH1W9f3jp7km2e1_SUE1F1ofOotCheE9zeT_8QHIygRnmouL2YOHG0EDNW0oIY4SjW3xKThvhkTRedd35rW2zKLVgrS3OvGEKmv_UotdShQ5bnKRZtuq5GFrrX_U0xi0Nquy_Cp8y9i_S1vU8nU0ItJd28rz8sLP2BI9zxDP5xWhBqVifLIgIoQmXU05S7eQB9yFVK0kBja7qQEXRopO3IFiv-O5SHPMUw262LS9hmXDY7M7l1VE3o6ciHyyO7mUVDAwkcoNOUfzf4uv_x7vCjJHcw_Ykgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23878" target="_blank">📅 07:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOkuLkMa8djLHtL0TKobt53Ho2_fR8ZJwuvjJexqFVFTzExUBMHMRX83grAkU8s3CC1rBi_U9aAqvBiuSRnAbd8E7GWa8XlgRgAg2Nkw3BsmYr5vTgLMvepIPBWCmTa9eN40BTEg8YaXYNcKrZMBeVxoB--Ve1wprk91gPbdC3vy94Z1jc5nnbInb9wFz3cTystWc_RnQkBVgrms04ArXkuBhJJUBi6sFjt-fjmcUsvFZV9RT4BLrgx2Ws4i6UEddBbiUJROmQk2x20ojsJc9essx1tDC4HI40REjDsD4eDvqclf7lR42AGYaP-wcU2bos3DPdqGOCGLQ_dhoCzHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت خانه در محله‌های مختلف تهران در سال ۱۳۴۶ چقدر بوده است؟
جالب اینجاست که در متن آگهی ذکر شده مردم قدرت خرید مسکن ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23875" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gxkx-1ZYzbOfWMvgTBueQDUd-xlUgCma8FzJrMboHSXfFIEoO1QkDQUdpCnNm4OH0PNJRDVc3cCemBXxS_NwJswsTK7LWCZcBWGSJ2Vg2USvgtNnwfWa5rUn8UCLJGVt1RBRe9QqwT1W9TLMiCvZU6jNlhNztk1cWKvHHL6fPP-KntoNQq99RxYiR4EWYqHpLLJ-Yu7PGP9NF99Pwo3Yk0B_YMBEp3Q9pdZ6pla3329nPVXdYbpppuOFgU3msyYr9EsB4TfJ3za2rAwFB_i0RgDy9w7QglcEaaqBs3qEcineZ7jb2tgLDc37sa2wr_N6OB_AcunbQAdBfw9M04h3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23874" target="_blank">📅 01:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">▶️
قسمت‌‌‌ نهم‌ ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23873" target="_blank">📅 01:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlhqQQDxUqAkqTnvWvkhuRypnWPXg8uJjcxHKNQxFPRbm_0AbnUCrO1jMl0tvSVW0_jSkncHgA-QgfLO6P-2luu5E24g5mEdxZEKo9b-vzxT2U0-GsHZxyWY5d0bf-7wcdfBGLEyK0ASFl0cbi_2Z_Uo4G09P7QFO8Oltq7ona0B1bCMo10QelpPuYRSfbfC78MH1s2qADv_k7k5ZqeBHgiyu4ga3tmkGTog4N5cn0aV23hwcxs9px0lqbLY0bXRyKNrSj3s29HVym6wV7D8chKKL9r9yJsVH3acERFtYfF6as26zO0CkibHji4QXJm7Xmb2n1QHdBcv17ceWqFn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با درخواست نیکو پاز برای‌ حضور در کومو به مدت یک فصل دیگر و بازگشت به رئال درتابستان‌سال‌بعد موافقت کرده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23872" target="_blank">📅 01:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRpM8LXnpdsqhA3Hby6VAW6lsedDGbu3M6O88lumMEOD5sfkyjf91fh_3LcQXnaRyJ5gBytVkalRlcavvygq5n8E1ZQ6woumljnyGdcmdqOws-4KR5LYYovQWQ4wXTOR-7fnSo8R5GXSKLXOGOxxwpPDVZKXj5ZLdrCkkDYalwu7t_x1jyFXAxBd9uoIiaGoCcY9ueGMex1AgG5UwWQsBVgyMS8UDccQSPZcokDva4bs_tTsPv1fwtni8_lENnyRGw5Fzy_jKmf9e5CiLG_JPBi8cI1a7mjt73qdti8Mr1A-jCse_RqY6E_b9gyMMbI0yeogdDISoiexrXifcwIKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23871" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_JLe_3-Ue6cRlGCBWv4HilaJOZzn27XT9qN7Jb-f01TpXaYvAtglAcq5fNWmQTYGt_5vQ5xYCaBvarKcYOg1FsjMYvJTabNfpPzYNkvYfVASf2Q4GRF24ySDhNa3grO6tD_LPgqdT2Rg9ff7YeMy0Wz9YYDDuAMGyWQvDNjXwcTVAvBEfGAUNMhX99V4xSR9MvHZsPZp_by3KXrRu0MjGTDuJweQSWUxMzt_YHMn-b2KHonh10S-ts6xCgKdU2iD5fkNJsuID7a5MjiqE0JCGDgFaZMK-7Y6lNvaQKjRbnPmRJFhP8a3RImxSHNuj4rJXqWNzqHE7_SKPUZfVD85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
از باخت سنگین قطری‌ها برابر کانادا تا صعود مکزیک و آمریکا به دور حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23870" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23868">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚽️
ویدیوکامل‌ویژه‌برنامه‌امشب‌عادل‌برای جام جهانی 2026 با حضور اوسمار ویرا سرمربی پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23868" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIWSmeugkPCo2h3mCeex_fIVp9oTZuU8pQLB9S_qVKFDqwjZJ8M5KzmCPqUyeB3MvmOK19VF8cEaOv6Dry6PQz1Pb5cMvPETe1f-efHpJHaLCjpRceLXc5pFLbZZa9VWB5tE10JvkNQryA7UblPvnOFlnYmOdr67UtFvfpBNlpojB7mqnghgzpvqLaHaRKFahgYaiOO1FJvgbMzo3Ys_G_2luc_37QfoM27ILsfbhUM7Y56Jsdxf6DJsJ1SGs1ZJsxUZs2kfrwlL2YlGP5jRx6OnLc2ULmo3Jiw4AjPa5dOaFKOoN0oaafE90NlDX4Xhuw5xiaj2fJyM2z680z1_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛پیروخبر اخیررسانه پرشیانا؛ حالا خبر رسیده که‌مدیریت‌باشگاه‌استقلال برای عقد قرار دادی‌ چهارساله‌با پوریا شهرآبادی مهاجم 20 ساله گل گهر به توافق‌کامل و نهایی رسیده و درصورت توافق بامدیران تیم گل گهر این انتقال انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23867" target="_blank">📅 00:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23866" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNtIyBDRegWPxweoyi0_J08AvzK5W9UAXv5rfOLjoZPiXugHIkQhSSDkc2P4_fxdTJ29Dq2uoVlMkaC1Eo1NL7bkueKHvAgCngqZJIDvig2axM_kSZFWe-gpSsTvdpOxMOmFaLcm3FO1wFVo0bcEBzTN3POydrbiPakBhYqgb5KL58DaTN4FLEuw-tp7ThWm3Tu-5BhAQwLwbx9ZKXmoCYl-Ge8PVOpOJCmzh0go2Ocy2ac158MhYqcBayXqKkTnBHxUEoza0lzT4zWA_c7-MgBrYN7krJHKYrVSRMKyvpWvwWMmQ3JTz2bsELjhczhMPz-85jqukDcieui2SVHtww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026
؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23865" target="_blank">📅 00:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tnm5xXg-snF3w-blThEWcCFj8_vckYMeLIZWNnY5ZVeAOmvO0zJXDhAraBlnYafqbuqTWh8COj36pJPxau0daH6Hre8VRr8cv8AsMvPBjv-3g5Mo2O7gcwck1ihldGglcvn-cF9-MZEi1Ph84qWgVHWoYSflBcQMU_DSy84D7DjYglM0OqiiFHimySBT7oDdHdpV6xBj4Ak06mJrOLvQ7Zx_bd1SL2Z9NaIl9AioQYziy8BSdHWCcf3RCRnctl6gokEvLIWqP9dxlOYF5eDdR8Jg79P4El37iADhDjKQUg5z8qb2RgopQuSkX62JO6Q9Xwpt5kDrUpL07ltKt6ycSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران باشگاه اتحادکلبا امارات اعلام کرده که اماده است که رضایت نامه محمد مهدی محبی وینگر 26 ساله خود را با دریافت 1.2 میلیون یورو صادر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23864" target="_blank">📅 00:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU5dmbHPjHUfpDC9myG7fSPwDHgep__jq2Qv1tGJEZHXtDbjdfT1lgxbqp-GjGZ4r5jR6DBqc9Lu06Mx9IMFOgxEIRelUeBxkdvQk7NoZE8HclRfWuOy53QxogRRBN1pjQDPoVpaPIbt6W9Zwlg9fw11Pp9_rm-QKvxY2KYZskONYPFG-fdlVOtE47jXWDaVpP0Vr-he3nEJ3dIl6IpZIg7xq4h-9ZZmgvWRCF6V3UA_25aDHTOPckn1LCZ8eRDVrW18F_HQl74WtkejrsRRjdJp1ewDWd3jeg1E5Sw3e7XlqyPkuUZxSTEGStKHNFJmsEQ2-E3EHuu7Ln7ZBgTaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام رضایت پرسپولیس، چادرملو و گل‌گهر؛ برگزاری تورنمنت 3 جانبه برای سهمیه آسیایی قطعی شد! و جزییات آن از سوی فدراسیون اعلام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23863" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_IWqTqjxcrDBo4laHOTHLZItMGhNRSuEMpng_cV2UkL0iUw3b-OQphYW5xtTIPLsKPVDmvtAYv1603FPoPN0uwJlNe70dYPcKNBS75rM0R7dUKcqRII8hwTKp_Ku6ZWv52uUKfE8ABmziuy1c6-OSHW5bt0mv_3hHVfm2Gnzu0BBh0WCND70jTegquuDS7l5psz-6yEeWLt55gbw6hddGh2qv4JmiYU7FWM3OqShCpjWKc38Okokb5idk5RdlbqHeKob-lNlQmDNp1Q2pCHGdNu9syEQGRGKivfz8Md-9xnnioYHn7fkwbKhUk1wjiVfnH0fj4Usq2GS1Bg6uxcsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران‌دوباشگاه‌چادرملو و گل‌گهر سیرجان امروز به فدراسیون فوتبال اعلام کرده که در هییچ تورنمنت سه گانه‌ای برای تعیین‌تیم راه یافته به سطح دوم لیگ قهرمانان آسیا شرکت نخواهیم‌کرد. مدیرعامل گل‌گهر گفته حق مسلم باشگاه ماست که راهی آسیا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23862" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3AtZUBa5TOaA0SmFWXqN64_9obqaDv1kqMFn68PyfK9d6sSD-P4vlKJxgnod93mC61Nekle91DEBi_d04J_WXjdgvhJNqlY_Wdxt5Nml44IiTvdEUVdSQrOfzUMZIy4YmaqS85h4RrGYa12FWrGE_eYT08dTsIkRXpLSztGPWz5wd1Gbnt2jBeY3Rd_7lq9EAs01SDW7CeEWkeOYpLVsOtMy59nb9HMKZOBP8JQi4KbSjxpiDYOiDVJNQ7d5az4tJfOR1lLEhnFwe1RYu6D5dejdsjP9Xw_YUimzSWSNBBfy3RFbEIZhlXW_I9QHMJz5mTcZ3_63SZGlngpJpiI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23861" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23860">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsNoTcdFlMNDkKwij0wixGoGkeDScNKHq8DERtv4rKBbnAFwDwh_1QGaKs5G8GPkXrFOWU6yHlt6A-QVCOJ3v-QvyQqnOkLQVSv7mD7eh6ejYsjtvBMz6oWZFBqirodd4IKwRCRe5d7Z8ilMBRmaxWjT3jX61MoR_8FONgMvbx03nmuXdPqhUTCH5wQNgPrRg_xw_SzgWai8wrlt3HgwWK4eJwrgOmU4JZn8LamWtQ-kRMtBlzRQOGUjw6hFUXbrIxmjRz6G1DmX7K52XPOlWLt_sGIzmawnwaNf-wcSVuIXCPKFVsdxUhOuX6zL08rq36yokTYml8Ceb_8Xi_IVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23860" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0tAaI3YEeZ5WLENC9yChjMYzUkfgjXGMGn1EIIcLFrs-oopdr1DxkvZ8lK3Qezo3BAJ8g-YDFs8KnTUFD7QGW_BfoZuNrX-iTVm_-uK3MoF3Ix8k1N99jdDBi06p7CXLRAh9OmTNGtKs-U23mitp1ij0SHXV0Ks13ejnVPb2aE7ubMpc2KzN8hy7IfAEDRh3B-mED2cNI9peMk2d-A7jtaLSoEapllV9VDOfH77MGfm-_RiiobYLQsYeqnBojwVzkP0MN9_sFEiw74VcbfLLUgHsYDT5BkWm7c8WT1CVA2prIrEJjk68Kmwrbjw8MlWs-yG74V0cpNiSCTgQKInWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23859" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psy-cZcYiM_UZ2K-vg_rAIJAIJWhnu3BOk-OvXUEtDg1ggmrbd0iJPtnNTKl-Byyf9X454Po_2rAAIrioIr1QEJ6wN5_Fl6EgH8k0hYxdzHefQTeMhr5UQq4--c3vUuT675JcSApcCAgYqwRruzc2NApAP_Ix4MYEek9aOmZS_oUg-iru95lvi1ap967s61JKkv2fGjp_0dleGI2RS_TOmxSEmJDVogbZvI6vHccuDqWmldrdtBJg2CoUIlpCRzSQQGEeGuJRoCoq7Y9n92nZJqBvyEP-jv6dMNtKfhzJDOmNUMv8_PKW2uXLXMaOzK_P4rimwP2KZkIlfLDZRkRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23858" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTFp8uyuBzD-DAI3XH0QfJtwLR7g5_JPSjxU8sO4j1Vwdwul1k4g4a24kvM1vNKjZRrQg2TMWpDHW-SOghazCgSTLE6At41NiN0x2UnvQ5LOOUN7GIHHWp13f2Kf7RGkcYBwAvMRhA-25hH1OzNeC_qzeWfCIP5VDkEmgrKKb4O97uCwn-T0Mc9jlWWW9miKwosRf_rwodeDFTjVwyw_at36u2TPP_XJnvyltYXLS8BS2h4ApV4odOsRNYTu2C7bjFRV6e1a3sJ81TT60nNDamm2X5YOMahetKNA5cXbRZNw8dnQpaO0FkZ1emc2Qd2WN0-_TYL_WsplG3q1jActdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران بانک‌شهر معتقدن که پرسپولیس در فصل جدید باتاکتیک‌های‌اوسمار ویرا بجایی نمیرسه و قصد داره توافقی باویرا فسخ‌کنن و سرمربی سابق تراکتور رو به جمع سرخپوشان پایتخت بیاورند. باشگاه بخواد قرارداد اوسمار رو یک‌طرفه‌فسخ‌کنه باید 1.5 میلیون دلار به او پرداخت…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23857" target="_blank">📅 22:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsF7d7NFutu7VwwOmM5P-EH09rjYVwdZ-dHBQzCy1GaQI6_P2FX_fk9fpyIsm-g2dn5t7NaLey1th41gQVXC-eJDqyUzps5yUjnziXJAyTW9YTNnKCIC8xEEkuJ0zUctdTJ20GSv03h0sG8LLd0BUCQL-zK_7rDQ-9K8Ef3T-3-XAw09-yoCEqHqmtNzLJclwmRvUCjcGPIJ-q3ls1-0oiSLC87MWpsw_6uJ3F-rbiRsPX-bNuk5un6xI2pQfxNzVBCN-tACf-G1QXYQ_zg97A1Xu0Nwh1rkG44k-eHQcIHyjAV4yDGMS8zL52YVmT8jyhUs7QXDJLF5lwONdPyWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23856" target="_blank">📅 21:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfcVHyjFbEMFatuAOhBqqa-4AY7rLzHqtFSMTL7eFrKc0c9NfYU4nwcLOdJe2yp-_EU7Z_PawZsmiZ_Pa4HL3Z36rc9Oksq0XgHaWZGRes2_YiqmNXdieCZmdsZln6GaQBnGubOjC6jpLKhtpzfpf_Ibnc_wW7To03U5msaVke4hSDCeXc7yX7qk7Na5idC1dOAsQTVZRzvkA90bUNSf-A3pBDAYhh8iB6GqzxRLjRYwxZxuy_rdz3SJji7N72p3a6zNpxQO7efgQrj2tJFcloia9qmac9eBH9mG58t2u_s_YjLam-hX8FphjGUo94UBFzAIay4yRR6kOe58jqtOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZN8ycGI1u3X5kP4ukiTHMP2Bh3GAuc2VtXjjMqG8if2e_e5aB7kJ1qZ449JSsu4lA33pR1HNHlx6bhaWc4j9rZZwYpmcoik4mbj3n2xCd3A91JCdFG4iwwWzsijEDzxi1XHltllz_TLES-5bFnOQu6tqF1jwpK_qIpUddGaHft2oSZvHWusDyuwcA5p0YBC1gFP4jbR7KbBqMFhcjxUiTS-mkHPdizMig5RhvszD7zBHPua4pRQq0u2qIU3THVX0o6Ah3FXCctRmYUIPoHaxG9OOwFWlht0hmuiVUpGUf_dQyCqqDbkViY-5jyNNFwKxWuyAXLJC9qU4uaV4xsckg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دو تیم آمریکا استرالیا؛ ساعت 22:30 از پرشیانا اسپورت؛ هردوتیم‌بازی اولشون رو قاطعانه بردن این مسابقه امشب دیدن داره از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23854" target="_blank">📅 21:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nznqQ6FKVum8DJF0xIsobVY9KQdHF43iDg_RorHwQdNM1UhlNJAy-0n5DhSFBX6DTAQVC_yu-ghtZpk7OioOPtjRt_l376ML8lcOLTu-FKt3feo3XRPk2MGHhfuS_8AT60UikyxEDuD1qEJPYDEX2SZ7B_1AfnplSeQ4U5_hl4r6GhDMMu1DY_b9DFahYP4fN9URMXefaXEDwbEv5SCS454M4qG3ve2RzsWb_3UdXtTE7NWKlKcR7QdEJbmDJOPlKQ_nXFqPE4iNLQ-g164wKNxusZXnOfQHuTDBtmYEmy0zn-enaIAueo0oFRc6ytBo5Rus7TRxI7_kKuWw3rehiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23853" target="_blank">📅 21:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkxWpVuGvoxXK122K-BOhAVhHJsnFKhopUkFvxbZ2AiGJdjDz1YmpAxeZVLRtGDGfmQjVxSGL6H0CNMVUeW1cG_vOsPYyJpzj-EYZ0RCbnypQhX0z6b8jokCvP90X95LLiqZY8CvwOiDNYa8OzrYGn0iKMSOvH_-3aKdaasfEeuGZkOA1SnfbOs0HWcVfb7TdYhOODU8ulw9gCoWWqIfMcl1HqsAECKMXVfKY-dW120EEZrsKX5hrcV7z62ri8Q3-ROxdJ0JrcilEF-HhDcUR5UbxP-xgAXkdv3sZifH-UwQA2zi5b0aUvXslvzrAy9mdbAQS4Ydp_fvrNQI1IA26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعیدعزت‌اللهی‌بازیکن‌ایران‌باثبت‌حداکثر سرعت ۲۶.۴، پنجمین بازیکن کند هفته اول جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23852" target="_blank">📅 20:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7648c46620.mp4?token=QP230Fgv1xV33iVrKUaAg60VyIye_Zl-6ryV6rOnvMvZQZiqnqpg2LA4yrB_-oMYgjEac0ZYLQi8OcAbGzIPC9pJ9Htcx3o83DmNACyuwDHsxh5KzSRpH3T8yVktSOFrm6zjvvf74O3qb__cx_WZU9cBYID8xiEPAvqLtnr89OlEZvAhXQ_gVXEgFOYGkRbm1-flIqYISfHOZsAHoV1SMGvH5iIpvhpkB4w28a67ZLYwL3gxZMNejoN6gQ4VXSazXEQCrK6gnYUfUW7nr53iXtALmSHzMkz0FeDlbGpcWkm7D9u_stajsi93V0mHTv0FLigzauaRgH9NWc9N0cgW2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7648c46620.mp4?token=QP230Fgv1xV33iVrKUaAg60VyIye_Zl-6ryV6rOnvMvZQZiqnqpg2LA4yrB_-oMYgjEac0ZYLQi8OcAbGzIPC9pJ9Htcx3o83DmNACyuwDHsxh5KzSRpH3T8yVktSOFrm6zjvvf74O3qb__cx_WZU9cBYID8xiEPAvqLtnr89OlEZvAhXQ_gVXEgFOYGkRbm1-flIqYISfHOZsAHoV1SMGvH5iIpvhpkB4w28a67ZLYwL3gxZMNejoN6gQ4VXSazXEQCrK6gnYUfUW7nr53iXtALmSHzMkz0FeDlbGpcWkm7D9u_stajsi93V0mHTv0FLigzauaRgH9NWc9N0cgW2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23851" target="_blank">📅 20:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-KdGi6yagTl4ZlGbgwmoWRwoqjwTtyCxlZqW_nIJ7-SuGogLpMUT_ylLyVGswvzKrZnA6xMlLO5YeYRrqh5pm3sSR6I07EShErWVM3dfXD8ZnONMwyl_YDHkFxFih5V-tQABvpu6AqVxC2SGTxCHg-lO3l4sxmw0xi_hMI82lI5NmzaNqWkPgsZ59Efa8NLlcZAZk_3D2oQlPet9c-4HnX2s2xL27jBhiARX0-ZyykzIEdYEBVn_k3BHkizMoW-8YTVtfe-GNMDfrI2aspNouPAtiGe5eUhjn-uDTMQAFnkeoPWNa77VdWr_tmCylriaWT-XUxHzNHzt5E5LOvG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23850" target="_blank">📅 19:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amccH4HoOSGkoRwZF_-rN8CGdxdOpgD89tmU2u3yRseCGKCXX4RyPEQmuRM_gF1CtbWGgu7oz0moxh0o5IxLkcj7zFcAiW_M_FT3JAgQ84-sIXWMoTYAjHn-8y9RlvNTsh7c8L6NfXc_pWR_w7ag28yo0roO0pKaPoltQH2UX1OiPoluB10vnZr9hKmRFJwfd2evyN_1OYr2k45J5eSpEXeSou-RoQNnQaydJ_LSqxLJOGZyqnp5O7TKMqLsjbIpLeHuqBpJcxBYyXZsGwK2duFaw8llmNmJ8P9T8-WJD51swbfTKY1SXrPx_vvH_5VrZkKF4INUUrj8fClXFykEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد محبی ستاره فوتبال ایران در واکنش به حواشی اخیر: من هیچوقت همچین کاری نکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23849" target="_blank">📅 19:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2RdexsmUfmWgGZuTuBvGV-X3EVcb00g8-zHggRJAH5CaXERoOSIucrVCi0D7PCvvtLHSdwLpNQjxxfh7oMXWsQT8_zhgi3Y6l7qoBzog2CAWggj5VKrUTlzcpfKfeEsTJQf24nyIALFx6TX41mUJ03ce_u_UeYeoYPUuZf_AxLa-fAS6Ln7KPjr__NDOtZsTbUG82BdbWa8w8Ck7TXJBkmnBT2L_d4fOVGS8v5ttnpkUcAxNyQtJAF4kXsl4mb4S3YehL6rWnm5fBhQMRNEOOHcnTs21FkbwYlU9w9xRJKMCvjZL9K2Lu4XgHjrrHb1EZVa_JT6sRt7FoJgX2NqqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23848" target="_blank">📅 19:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCMVlKqXd9yka6QqfK6sqUWn6rkQ4DaoGGbINqhlk07P4Yxn1XfbRMUgJL92-R6dmag0hp9vw7Y6WfL1l_iX9T5qbDmQdEzWXGizhXDbICatmJqHfuqJc8ncvRy-p-9njpCNkcIJK9aJV204kydWl1XrXVKxCTp353stjKoPo3OF7F1TPXKwRwQ6FBA5aAQfUXyjkC392hl6jBZWoRzY1VgKxKSJwY74V3qZ-2C0qYpYCybUFWzzQaaZsj4coDhPuXSKjl_go1OUw8f0p73UT696Lxsdn7kaxTVTtuwC70x0yL0VjdeT-yKzZLqX6mv00_vNY2RhbgaGP1WNtUr19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پدر رامین رضاییان: خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23847" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1TzdEduK83B4GALDF5obszHmU-S-7P_EbfwGUrA4S3MJjmw8dOs87Q5uqa48Q96t8bOvMVt98qnZOJVYSTlypHwXcBJB88-fUfZM5QeCYwE6188LWO9EmUmVmgKq9KW698o3-SP15HRoQN6qF8I4aojOFzHUqin2Irbal7mJOFcuqsFMVZfW5oGjappe5Z_clJI7mjLsH3c6zW-U19RoeAvBig6rs5zNfVTfFzk2m3gMivWE4WW9gkzhJ2GQm6dKUiFOXs8wsWu0bOhW4slDoL9aetWyKV0_MUsD_29EUmrsiJDHjl7Q4Lspgq0FwbVytmMEGHvM4889VtjDSSACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
طبق شنیده‌های پرشیانا؛ علی تاجرنیا رئیس هیات مدیره باشگاه استقلال شب گذشته با مدیریت گل گهر سیرجان برای جذب پوریا شهر آبادی مهاجم بلند قامت و 20 ساله این باشگاه تماس تلفنی داشته و احتمال عقد قرارداد 4 ساله با بازیکن وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23845" target="_blank">📅 18:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDQ5RUrjXPv5Mx5bK_5Z9ReuNuUEI27yUQwQYfAwOGQe3PpqDms55nnkkTtcQ5jSYAoJ3bB1X_DPNygrY23xv8FjJTb58WmvDqmatooxa7blTjHS7eSZv-t-77jkG_DOjHF5fA-HyXm66-RMh2Y7nNPkvBnRhGoSkjBZQnlhaTkEYoL99-HWhXywzPgnTiczFGivNTA8mVE7NNjnrM9mfFK42FDmMBy-fYL3DKEQry471239EP2-IxSycGxRnRVEecDhKL2j5tFu4eS7Plw0hx1T1ci-hz5GEhT88ZUSEy9RLGnVT_pkp_DURra0kvLcoUILXtK2f25pWaC8P4pCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ باشگاه تراکتور تبریز پیشنهادی دو ساله به ارزش 90 میلیارد تومان به شهریار معانلو مهاجم ملی پوش سابق اتحاد کلبا امارات داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23844" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZmPSt4ggPiFueH6h5p0EwMIeohFINfnIgkrOenQtth4E9YHQMhHcu77WLIgMX2lKTiK4ldbl4050OdNywxR53FWLQlYH6kSOl-tCxZFysqAt9i4ap9KkH0owBmV9tKUmiPI70ML2Gewr62Q2xsdzsc0bBlI-pn12xeFAJ0OzYl3EukGqgo9fbj0dfL-VPOD2ivC-pLlxiTteRE8jqU2IxYAy0JG_TCt_BpqP1Hb5AXkjtJTzL9I5aBiwvM8QkXyN3n2TbYMXdgRsuwi77FNEvalQ9FYZuBubKiIBKYdmnJZIGV22zcwM3KJ70h98OdCL1wqETGHdF3BDPLpRls_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23843" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23841">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhwYuHzpy7UsgkuAI6oBZIBQ2nL7j1iXbleeOIuwS25kljLBrnI1hvkrbCMSOSWbvoXoccb1mMRhFY1GLl_g7sg4ubOnGmgOzE3MtJTklAMOC37ZTaOZfGUJkYtdbL2YOw4DpKgwy1JWvhxN1fI5O5Xmx2d4HUMDDE5t2Oa39UipOBKAdaHWTFPwnTNWRkdvcu5kF1oPtCuuYq-_mKpmNG4rCccfCHlOytBffWIxBAfj5Adda6JgKKp8KyytateNzTsyurzBBT6xfe09ySLmqiPREE2x8eriRNIgGazSuNfiVnxUkQccahYNt-W0iQrDtA8wFsndGPR1wQTF2PGq4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شش تا از سنگین‌ترین باخت تیم‌های آسیایی در تاریخ رقابت های جام جهانی؛ کره در صدر جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23841" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23840">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te2Rx3GmtTFCJfD0OtyEC5QvCogu7MEgNSep15FlmK8lYoEry4RrgkkU7UuDfPeRorTs1ffPDnnFpXqPn-T1k9zMhyfyIbvanMtXewagkZy6ElkmngR8oKI54w1sPKQf-lzmlwmEWJvL4eyWLF_0TX1VkvzJDNmorKCjxc9XeflYENK4dW7PV7rh4E0bB7hCdLlhvbHUFclS9yVH_LCK_VluylMYW6XiEXfUvJMbsSCpC0WlndTBLsT9Ay90U5gzjtbkiAEY9rM6jFbX_TkxrjRHVkhpDpDa6RfXWTUMls_uNywQbOE8qbhFje3RcQN_3PgX3YDH7UuB8JhxzYGpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
لیونل مسی به عنوان بهترین بازیکن هجومی دور نخست مرحله گروهی جام جهانی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23840" target="_blank">📅 17:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23839">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbsIN7EFafaGhEZQe0MiIEmV7CA30UJAKrQ7FtAIn4365GP3GZDY-rNSXYak3nRpG2rge2J3T3UfngO9_6f5SOQZAHYLK15U8O9Eip-OfOJ9hehZwxszjUUBTN0d7t0C8KDyodXNK5MPqktgp2hljGVYsGzmY6MyrFRc_EpDbu0cwJ8srus2TuGjK-urtGxbAb8F5eXuXZEBFdZQ_87YaEp8aZqGpK9Ydi-Bai2cWSoTuDKThni3YvYJ5nngtqowKMNRh9hwUClOmBBn9QKY6P0CAGEjsbI0An2hCtSRtpvbsYzVJIIq6LGAOPY8oa2HH2rn86PM_44870sNVMonFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات
؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23839" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23838">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=fTIZ0yktQiT4e_ziDpcQi6LBDSwCAi-k5UIefU1VuPFmVjqf1Z3nRnKVImKl6zN_DqpcP-zHB0Zg7nl7wFAL-SxfBEU-vxOrViWL6U-0qjU06HyyyKKBu7MjFTQwapnMmy_VblJnE6pcOEFyoYCibel1Ac1gAjuJrhH57dgWs_rBG9AeDED4ulLUclBQEFo1iSisN-nps2Z7m2VAOaVgk8VSZyZZZJ_dUkYGCX9ovREl3tSeNeIQE-kYD5rSeCABaHQD9NFw-LbFJn_jhzMkoVyrIAub6bvSLAcFesROF29SlpWGkibkE-F1yAyB5s96lqLJpWS4OOJhlAMraWFR7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=fTIZ0yktQiT4e_ziDpcQi6LBDSwCAi-k5UIefU1VuPFmVjqf1Z3nRnKVImKl6zN_DqpcP-zHB0Zg7nl7wFAL-SxfBEU-vxOrViWL6U-0qjU06HyyyKKBu7MjFTQwapnMmy_VblJnE6pcOEFyoYCibel1Ac1gAjuJrhH57dgWs_rBG9AeDED4ulLUclBQEFo1iSisN-nps2Z7m2VAOaVgk8VSZyZZZJ_dUkYGCX9ovREl3tSeNeIQE-kYD5rSeCABaHQD9NFw-LbFJn_jhzMkoVyrIAub6bvSLAcFesROF29SlpWGkibkE-F1yAyB5s96lqLJpWS4OOJhlAMraWFR7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23838" target="_blank">📅 17:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23837">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
اگه‌ایران‌میزبان جام جهانی می‌شد...مگه اینکه با تصاویر ساخته‌شده‌توسط Ai بتونیم همچین چیزایی ببینیم وگرنه که تا حداقل ۲۰ ۳۰ سال دیگه هم قفله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23837" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9gyvjYJj3XqWLW9cg8aSx4Elg5wSUm-8VxdmvQhaKgc7SncnkyxDNOuqfCIPx-I8Wmd0_uR_lxa0VYEcxlqezcD4Yd41SiWf42Fu0ztIJQ-Y7jvpXIG4AyeKHj-ewHaFFyesARxMTo0_wtixkXNuZQB5S3Mq6k94N6KGuFvE6SX6IRjl7EFMjmGJ8PF5blGE-gzHz_-FP6kIARu9YHVH69d-3P35fGxKGXGbkDZrwdCZj51y2-vrQ-gcdGnJ3N1hE79voUjx6j37UbJfX3PJeMdA8fF70kY-Z5OAUdMGDqUDZsTZuYiFg6MS6mKna3-R-HgT1HfzYvM4QRM4zikTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23836" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXBWQ-mHVNWW1IDj6mprZNQ2W-7OdxcjA3vLIADllxK6sGubXjFbnIBvr00f6iW0c7BPLsufaa8PqtpWCU_0E8fV4kfPJArGtgnuPcXl2s6e0RX5EXXmB442vd2p2e_jRtMQq-i73Mo--PNi_QK3KUxCHoDX4wy4UqlyuCBNULXbLUFybW-mzrv9tLFRKUWIg2MAYOPLodHITBsIiucrFLsPiLuLZIvV4g_Z78wMcinxem23MW8VQzPFgdaFVmn2k4S9gkyYkdG8kSn0W_0Nga1wOzlGg8WoxAgXgroKI8JubuoxDMqi-k5xo1LBmtLiK6Sxtw-cvQJe1_NR_ouJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
باشگاه اینترمیلان رقم فروش آلساندرو باستونی مدافع 27 ساله خود را 70 میلیون یورو اعلام کرد. مورینیو بشدت به سبک بازی باستونی علاقمنده و به فلورنتینو پرز گفته لطفا اگه میشه جذبش کن برام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23835" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17a904766.mp4?token=fH-la7_BKdXjDI8X4vXLrXYA35dp3Q3Ts_xzAlJmijqywEh_klUuNMldV5m0G4vM6MIxdiEMa1jwEjpcadHiOqweYaYbiAO67hYZkTf3AUXY980PmkEnADSD4CHpjosN8A6etYfoGX_gjXjek7jdNrlTpMLME2kqpORtI_sDLpeePbNYRRZC9bjA6nrKB01lrIsaPy_v6YcF5pZpdbn5DxmaNQ_G9qLkXTz09z50OKqd-EnPLY41KQgWjQ7sQddsTLsdLMmQCbtTPt7yzSWa5xbW04Gn5CMyZaAGCtP7HXf5MgDnU271LXvECQBFAgiIfhrDFVZLgheK5DQUXEWXZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17a904766.mp4?token=fH-la7_BKdXjDI8X4vXLrXYA35dp3Q3Ts_xzAlJmijqywEh_klUuNMldV5m0G4vM6MIxdiEMa1jwEjpcadHiOqweYaYbiAO67hYZkTf3AUXY980PmkEnADSD4CHpjosN8A6etYfoGX_gjXjek7jdNrlTpMLME2kqpORtI_sDLpeePbNYRRZC9bjA6nrKB01lrIsaPy_v6YcF5pZpdbn5DxmaNQ_G9qLkXTz09z50OKqd-EnPLY41KQgWjQ7sQddsTLsdLMmQCbtTPt7yzSWa5xbW04Gn5CMyZaAGCtP7HXf5MgDnU271LXvECQBFAgiIfhrDFVZLgheK5DQUXEWXZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23834" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB3TfecMKrUwKwsa9OWJx_EnjIidEfMR7j5Cq2aAmduBye9ar_kfVzrTRvxegyVh88PUCwAm11DuJg1xF2l0YK_XIQh2XFpQsDCRlyMgev-P1lLCd1-ioRzSPxZbrMUGSP4q2twXsS56Hd9c9ytOkTuBfASwFivmCoCume4RWGDKXdfi3Tx-nGGAQlTmi-iE0aHwAdV8SpHpfDFbbWxeANVP7dS7NinO8hYgYscKgvLHEuDyr2_ctdcUGs3NlggCLPVu5To7fkLfpCH0RiaJMTxqa2t7BWxGYtomh38S19zWMNFgCl4N9c1IHfnHjFzv_6CKfH7WCTl6xVRpsBkneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛طبق‌گفته‌رسانه‌‌لهستانی؛ قرارداد الهیار با لخ‌ پوزنان سه ساله به ارزش 5.5 میلیون یوروعه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23833" target="_blank">📅 15:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f57nWEpTJ9ovjAmEWcxkPnRw_LP8I8g9cVhEpxHPnTn5T90YRg5ZGmeOiW5bm3GYK3fucKn0CWxApSe43gbXxRSw5p7n4z4855JF0Pc7KvnbEd7j-zIuN19nL_IsEef949QyEPRvvmSlydVaxHAxOK9EGZRNtZjeMRUOfDkagsVNGo88EqPmrjLNdStV4b6EwaLXt8mfw6fkApCppE4VlZhSItD-GYTj5BX0YXCYPP76McuFOufiCHKxUEmmuXAJN-r_1AKW9to4UUuKPhePeOVHvI4C7JJl0iqZwcVta396uskimrO4n7iFxSivgRsxrhX9AXJbTCs15H3HKhU2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/23832" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=Y6Rort2pVqn4bnNTleJWLKFDjwnvadHhUjLxk3svLrL8D--S4qoU3HNbhlisNc0EjGHmLNt8t3EBuFz2B6MzZ61J36b3K5_llKLk8XBZBumaeaFPR3dQYxvaMJyQcfXRfEq0TLIFwaJ0GhivfRQN7W_lqktX4BdiHjqMKnafwU5UuWwmY7lolOYSmTwuF23XW8UK7-Ox8pzjrV5EBwHgXPf5zGxcK29mQ1Zz7HAf8FSRhzaNJbra-QRDMadLsrbUD50ElinZxXopehnEjgsUFbGz2z42Idww1mjUthpxx_RSZbOeD3ZRJ3bsTzrsTbEpZBawEJiFkBeu-GSo3IagUz8AG9i2XBqcZMtUJ9qnTDbt-Aib1x1r6ureRg7vp5NE4tyN-6-Txn_BYrFbimoj9x-no_i1a3vZyha6HeSf_swzBlEeLJxIcEg1j85uG_oQZFdYFhSX4Dj2gTshZobqrGt9l8KkjqaiYwaMMB9N7EZkge1KSHp_NYUL3CIT_kaObwjYNZechvHBXYj9d3UMn5arMm--SCA-L6_U03VNeJkCT11jpTd5WzpTCLtN2Fa_A4hUkuutMrFpLP5WmZ4uwVCP1Ofl35RxEXuwipBtmMXNOuh9F3u8X_ag8O2ihKhpB-4In_kvbHiXlURPgYQmCPb1wBiphEm8yZWvxWDGVJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=Y6Rort2pVqn4bnNTleJWLKFDjwnvadHhUjLxk3svLrL8D--S4qoU3HNbhlisNc0EjGHmLNt8t3EBuFz2B6MzZ61J36b3K5_llKLk8XBZBumaeaFPR3dQYxvaMJyQcfXRfEq0TLIFwaJ0GhivfRQN7W_lqktX4BdiHjqMKnafwU5UuWwmY7lolOYSmTwuF23XW8UK7-Ox8pzjrV5EBwHgXPf5zGxcK29mQ1Zz7HAf8FSRhzaNJbra-QRDMadLsrbUD50ElinZxXopehnEjgsUFbGz2z42Idww1mjUthpxx_RSZbOeD3ZRJ3bsTzrsTbEpZBawEJiFkBeu-GSo3IagUz8AG9i2XBqcZMtUJ9qnTDbt-Aib1x1r6ureRg7vp5NE4tyN-6-Txn_BYrFbimoj9x-no_i1a3vZyha6HeSf_swzBlEeLJxIcEg1j85uG_oQZFdYFhSX4Dj2gTshZobqrGt9l8KkjqaiYwaMMB9N7EZkge1KSHp_NYUL3CIT_kaObwjYNZechvHBXYj9d3UMn5arMm--SCA-L6_U03VNeJkCT11jpTd5WzpTCLtN2Fa_A4hUkuutMrFpLP5WmZ4uwVCP1Ofl35RxEXuwipBtmMXNOuh9F3u8X_ag8O2ihKhpB-4In_kvbHiXlURPgYQmCPb1wBiphEm8yZWvxWDGVJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هوادار ایرانی تیم برزیل در جام جهانی 2026.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/23831" target="_blank">📅 14:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=KvJOANF4tMlynSk9sGamziv_-V3KjYes18jfzUKs8nfIY7CEAkCDvLJAiGX_ukqabBlJXukWogfLvqhHWyiSBWXyjjGr8F8J8MG-_GzfFGLxdN-VnCctbdCtcKkSft7HpWkFGfSuGLVm7vagKkq_SJv8GiSVMPHj_SAJX5jX11dDXm8l2yILold7wIbsAelizel69YeBsryljCPJLHIP82_hjmfao_RmD7OZmW1EK55YD7DCcUAZ0mgF8qNpfQkD0bCLXokunMzlQNcYG5pTnLa9uzmsZY0gb5Gswtchoaimuvq3QtARTUIQg0fSzn_Iyona0Mmk5EVisKd-PKRPXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=KvJOANF4tMlynSk9sGamziv_-V3KjYes18jfzUKs8nfIY7CEAkCDvLJAiGX_ukqabBlJXukWogfLvqhHWyiSBWXyjjGr8F8J8MG-_GzfFGLxdN-VnCctbdCtcKkSft7HpWkFGfSuGLVm7vagKkq_SJv8GiSVMPHj_SAJX5jX11dDXm8l2yILold7wIbsAelizel69YeBsryljCPJLHIP82_hjmfao_RmD7OZmW1EK55YD7DCcUAZ0mgF8qNpfQkD0bCLXokunMzlQNcYG5pTnLa9uzmsZY0gb5Gswtchoaimuvq3QtARTUIQg0fSzn_Iyona0Mmk5EVisKd-PKRPXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
صحبت‌های الهام‌بخش مارک کارنی نخست‌وزیر کانادا در رختکن این تیم بعدِ پیروزی قاطع ۶ بر ۰ در برابر قطر و سایه مصدومیت شدید اسماعیل کونه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23830" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pljhifo5o9sFPx_jpaxGTrdBU-vm1T141YLi6Yr1jel1p-zLgulQ2MhZEx3HUX1K3k_yWu3Mty8f0l6o9sfp0hal-H0EXYhg5NglTVfXYqeDN1PNFrtZaDFG-ndsQFMNWLSmEg0CTrHRmfe6maxn1hw88wwd1sZwb5jNdKhHL5PX30cbvVmXt8EeckdrxnKrRsNw9OkGD-dkWGMDsWfqGBPoQ1uU_MfonOr-gvZFYB-3muNSWMpZkgrBWNHHhizZXeF9DgGX7TSMthWSRvFF2QEMt0VrtAb_pZC3wPXHjt90sBD_JxZmgLAaMYFAIuX3oFxc0VrcpQj1bopo9uv1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
این ویویو مربوط به سال 1401 عه که محمد محبی به احترام‌مهساامینی‌مچ‌بند مشکی به دستش بسته بود و بعداز گلزنی‌اون رو بوسید و حتی به هم تیمی‌هاش‌گفت‌خوشحالی نکنید. به حواشی چرت و پرت و فتوشاپ‌های یه عده مغز مریض توجه نکنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23829" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23827">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nidkneVdGOnOcvER-f_TkD53TTrCk6BOSFjrygLofAEbOgKgldxFQIlVy4OhUQYiMV2RJslDbgn5F7JuevvXfjzk1I2a-NaVNAl7s7tMUzRBFTw15jC8Q82u-cAbkiOI8UYyQfXsoZ2MplEkaKLhT1ogqeOoASTnKYX_V9mTa_B95Mqz3Vf6R5uF8DICOSzbLarlhwEy_nfkav0ztbgu57JwVQP3OXqbaScqmRRH7kK51h7F0sBan_PuS8r_6BvOo1AkjEnqdOOb-SJlbQ8-RMrCZ_4SRnHNkzYgkt7BedrJnZynpWbvBYVorW9bL6SY__qMTPdtMAEYwf5FQa6Ayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3fOMRlsBaZjn9_FM4W8qbX33ZI0WwWx3K5JGoNibBG4C3GzTcQT2IBtg4sr5X09nLbqlZLcYhWo6qAlOLlQgmmUeh6Bzz2kyrEvvxtgp6n6HXo7DfmcQBhLsLJTlLk1RGTYS_1XWAnMMag5AbU22rE4H2VCjNoPnFNxuzf8PVLcl9jlL0MsrIehwh7On71TnvHuAKjYULOHCnLDnPISwR2BtrEwZSW_cmOM_TTD5tMlh4deZfZrWpKVfDoF97-xqtZzcZSJAjA5Pskv5B3t1Wz_ZTFrXednPfqS338Ymscs12QfcX4-QzUkuiRN-ymLiRqy4cKJ2Ai2hfBBRBeiOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه هفته اول لیگ جزیره در فصل جدید اعلام شد + برنامه‌کامل‌ پنج بازی ابتدایی شش باشگاه بزرگ انگلیس در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/23827" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23826">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-MSbXZviavTVR1K86dMicZ6QxR9eFpP5qB3DOe3ete8Z1WXKAcuF-2i6aR8Aiqxq_i_zcfdwLWfakf1Tiw6WQxsvQfZt1tWA_6xaMP4it_MQOXv-ZarqrzikcpqmgsZDa_FnGGPd7YGbHxvIrWC-xF9Ey-7FUPbdYCuQv0emG0QwYTRqvP6Rp_3arXbGDqPyIHbS8Wl9qcsC3cGHIBa5RtIEQQHGkxnn5PFtbkGs7rp4TsKJxLm05LzjS5HN_itD3chdwq7aC0TmVZgBV5WgT6U8ksiHzVtKfM8TzOG8Yxhfh59zjjfTB3thPgXtN_dLHwh-lMBg4JPFE2fhkfI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/23826" target="_blank">📅 13:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=RvYcG0UTdnBjcTDb88J3GLuJRTINfyCa0qCUonAHFHaPebRzjSGw_wJEsOd8YiIuQ1cIpaESqvLs6c--KaTCkfI170Fs_bZxRb8xPnLtjPDagN4ymnJdlRSdKXu4c4IpWZbxhU4ijc28ABJx2Sf9f8eQKufSElBo224alEuau7NUE9LCEIw2xWoBFFJrNw_rIxwWadFloViyYOlNTGlnEVOW8Xvuey_1j6iO0VO7vkDoJ-6xR9D8n6PtDNvFKSdFFsQpSctqmWuRoSt-dyEtzpR9DM0lJRl-CvsPr4kgyF8q71zte-ZSt57mhdqOa3CP4OgwZJq44EZxmY8fjt5Xfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=RvYcG0UTdnBjcTDb88J3GLuJRTINfyCa0qCUonAHFHaPebRzjSGw_wJEsOd8YiIuQ1cIpaESqvLs6c--KaTCkfI170Fs_bZxRb8xPnLtjPDagN4ymnJdlRSdKXu4c4IpWZbxhU4ijc28ABJx2Sf9f8eQKufSElBo224alEuau7NUE9LCEIw2xWoBFFJrNw_rIxwWadFloViyYOlNTGlnEVOW8Xvuey_1j6iO0VO7vkDoJ-6xR9D8n6PtDNvFKSdFFsQpSctqmWuRoSt-dyEtzpR9DM0lJRl-CvsPr4kgyF8q71zte-ZSt57mhdqOa3CP4OgwZJq44EZxmY8fjt5Xfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌دلخراش‌ازبازی‌دیشب‌قطر
🆚
کانادا؛
خطا مادیبو بازیکن‌قطری‌ها روی‌کونه‌بازیکن تیم ملی کانادا که موجب شکستگی استخوان پای این بازیکن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/23825" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_VMre8kgmLDhl9r60SRaSziHFAiq9yyOwev37n-CavCwFk26mfWrjZc_G5jBm0E4iG5uX3RdOCtgA0BeKW0SEMyic6eHHS0pYVG0PhsJ8_-5Xrvc9IeEsMdDnTyoUe3IzzRTlQgmzFUJm7bYXpMkVZTaoaP-WMcdFiQkbsK-4nkrlzci208mQbZiKJO64qmiE35Wa6I6uuXOmEjD1ISE1sYP7IOjIO0DByHR3MtdHh45zvxXnXHpZGRTOUsT4zaydZGWuagjKDJltSs1NXnUMEoyRuWgmQJKnOomON_bTzw3-Bqc2niQTPBwhdae_I2gH_K3xm1mwFCSl1Wfo0qCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/23824" target="_blank">📅 12:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15564d6447.mp4?token=dUAK-u_wlSkpymRzCN-Roqb4shufEsBVzWTOmFs2GKB9-cuvupHQzkYdOBDrwBxEzFFWJCf0qdkCelhauW6grV12W5rJ8PBWPBGX1Fk7vYzlgc5sWafWeIP3P7OTUNhSGHMbKyytm7TC3smbubEEMMsPoZaudfS1U-gkxVRAXL5aGC5lpNRnFwVqIBQpVvfXCKdX5Im3aqZPBQtBQvsrNbTDoCWR7KssszF3iqRvPkq8f5gys_V3kUsUKg5fTfE1dBlYCaWeucYrsVVD4KI5TKjuELdMSpS1wFmMjUhRmwzrSZCu3sILryUoyekbP_twgc0bhRtZgPzS8iVwDInk-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15564d6447.mp4?token=dUAK-u_wlSkpymRzCN-Roqb4shufEsBVzWTOmFs2GKB9-cuvupHQzkYdOBDrwBxEzFFWJCf0qdkCelhauW6grV12W5rJ8PBWPBGX1Fk7vYzlgc5sWafWeIP3P7OTUNhSGHMbKyytm7TC3smbubEEMMsPoZaudfS1U-gkxVRAXL5aGC5lpNRnFwVqIBQpVvfXCKdX5Im3aqZPBQtBQvsrNbTDoCWR7KssszF3iqRvPkq8f5gys_V3kUsUKg5fTfE1dBlYCaWeucYrsVVD4KI5TKjuELdMSpS1wFmMjUhRmwzrSZCu3sILryUoyekbP_twgc0bhRtZgPzS8iVwDInk-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پدر رامین رضاییان:
خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23823" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
