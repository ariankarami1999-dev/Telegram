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
<img src="https://cdn4.telesco.pe/file/LKUcJOMXwon0mKhbhlO5EuKDeiQnQUbLK71hd4w0xXNyZkC42PpXKYogpOmJRmq-Y4oA9SNmbty7xOX4JxsbAoJdaeJQ4tOzj7pMoPl4fKqckU19PYWCPuDgE-PxSNZk-D-FAlyXKhTbyhIoYORKLRPKNq1UxjrkJIEHE6Ym3bYVQgl8OTXcFTBoVw1R5iwV8NhMvuy9xHZavcgdxgmeIa6qjpL5h9F-RCWkdp9pUiRlexj-q9ts2XdcOGAOnhiLkNiiErULk6uhnutyXQVXc6ksF_thUIItdfbnx4AibW7enpBFPZYzf1B4ngbZzijzpxJh54C41bPe-YVhrcz9og.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 09:45:22</div>
<hr>

<div class="tg-post" id="msg-150346">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل:
من هیچ هشداری را قبل از ۷ اکتبر نادیده نگرفتم، زیرا هیچ هشداری دریافت نکردم. من منظورم این است که این یک دروغ کامل است
🔴
این موضوع توسط برخی کشورها یا برخی عناصر خارجی به صورت سیاسی مطرح می‌شود و کاملاً نادرست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/150346" target="_blank">📅 09:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150345">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51dfc1507f.mp4?token=W_zwQUa5FiV_YO6UWxgVTOq4PVP62cpU6oyH_r1nRODuRWb1zo9rxOF4zYOLEcqX_z7inlMS8xP5pRmWIdZLvP3yQJZamIOmbmgNSZWTomwExcYDIUFr7PE6jDbTtrX_3VEI5sc32e6oruKmoRftz0wyzHp8CE7lbuUhuP2KyCjsVz7FfHLbAx7oXFUVqkz2Zl-BGvUozSVF1jyuBFKA2OkXLcsAZoSA2oJvHDvuKAlq4WjIwqQBWa9ZvfV8rmDtho0L2URxV8J-1gcSz-16FAkd-a3nknJvoIT2P3jmS19XxBrNmJnnBKW7zmfCXMABybZgIcY0uOhqbFoxqEKIIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51dfc1507f.mp4?token=W_zwQUa5FiV_YO6UWxgVTOq4PVP62cpU6oyH_r1nRODuRWb1zo9rxOF4zYOLEcqX_z7inlMS8xP5pRmWIdZLvP3yQJZamIOmbmgNSZWTomwExcYDIUFr7PE6jDbTtrX_3VEI5sc32e6oruKmoRftz0wyzHp8CE7lbuUhuP2KyCjsVz7FfHLbAx7oXFUVqkz2Zl-BGvUozSVF1jyuBFKA2OkXLcsAZoSA2oJvHDvuKAlq4WjIwqQBWa9ZvfV8rmDtho0L2URxV8J-1gcSz-16FAkd-a3nknJvoIT2P3jmS19XxBrNmJnnBKW7zmfCXMABybZgIcY0uOhqbFoxqEKIIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، درباره ایران:
آن‌ها در تلاش هستند تا سلاح‌های هسته‌ای را توسعه دهند و روش‌هایی را برای انتقال آن‌ها به هر شهر در ایالات متحده پیدا کنند.
🔴
این کار مدتی طول خواهد کشید، اما آن‌ها روی این موضوع کار می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/150345" target="_blank">📅 09:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150344">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نتانیاهو، درباره ایران:
این یک راز نیست که ایران خواهان هدف قرار دادن اسرائیلی‌ها در خارج از کشور و همچنین در داخل اسرائیل است. ما این موضوع را درک می‌کنیم.
🔴
و در واقع، ما نشانه‌هایی را نه تنها از خود آن‌ها، بلکه از گروه‌های نیابتی‌شان می‌بینیم که نشان می‌دهد آن‌ها علاقه‌مند به انجام حملات هستند، به طور قطع توسط حماس و حزب‌الله، درست قبل از انتخابات. ما شواهد روشنی در این زمینه داریم.
🔴
اما فکر می‌کنم که هنوز نمی‌دانیم آیا این اقدام به عنوان بخشی از آن طرح انجام شده است یا خیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/150344" target="_blank">📅 09:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150343">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31728f2cf9.mp4?token=exLggXBpknhXwdu1JvdEjNfJk6Xq6917TmZperAUW9qh_99sC6s6yX-mSiQ-GsydfH-Pf1bzaFGBGUbXPHbQjPZy-LzEuLnVRKCsi2mh5iyzn0SEtIQ_OUx5Z6mokuSwrd5t-WHjuv9TnJ96Z75fxeCn0AHOEXODNLstG-r0lLT_AN8T5m__a2lfd7kicAP62S94ImBqy0MdAT2pv-oDC4sR4HjNml59BGS_GFGNDTWHG18eXFfaiqdac4zRC7Ijo6Ryo5ZYW43mXGKccuMtQ9Dh8yGsc3XaES3YDFqvQ6N-vmtGnUvG-yktcdh2WER6ev43mYl4fh4yXEEHSuLUT2oulVgM07yW8aU-b5nSgcSPBmabpaC-hn1Tq61UmfSWhQjkEPdI-e-d2q3J_3a9twXfh356-K5ps6Fda35GLvR4uvPic7DTTD2D7D5vGV0r4URzrH_C2fdpkPLmVCFaKXf4TmDAB1ExmEIQpv-nrBBAXmS6Uw83oHJuaoJ3BGYq4EvYaTb9x-Cl5tn6MywwYPYw7rHMZv_2PP1SDlL_3V7SawSBXDI58_km36GbsB9SD4ejDf-jvnNAFZjQ6WZAbEfHBTS5ykPq3mHn575KQ7sT3S96d6Zw8EE3x8GrLsq0uKe2J8zrX1Ivit7BUYx-4gcQ7wFkd2hq26dipTvmzGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31728f2cf9.mp4?token=exLggXBpknhXwdu1JvdEjNfJk6Xq6917TmZperAUW9qh_99sC6s6yX-mSiQ-GsydfH-Pf1bzaFGBGUbXPHbQjPZy-LzEuLnVRKCsi2mh5iyzn0SEtIQ_OUx5Z6mokuSwrd5t-WHjuv9TnJ96Z75fxeCn0AHOEXODNLstG-r0lLT_AN8T5m__a2lfd7kicAP62S94ImBqy0MdAT2pv-oDC4sR4HjNml59BGS_GFGNDTWHG18eXFfaiqdac4zRC7Ijo6Ryo5ZYW43mXGKccuMtQ9Dh8yGsc3XaES3YDFqvQ6N-vmtGnUvG-yktcdh2WER6ev43mYl4fh4yXEEHSuLUT2oulVgM07yW8aU-b5nSgcSPBmabpaC-hn1Tq61UmfSWhQjkEPdI-e-d2q3J_3a9twXfh356-K5ps6Fda35GLvR4uvPic7DTTD2D7D5vGV0r4URzrH_C2fdpkPLmVCFaKXf4TmDAB1ExmEIQpv-nrBBAXmS6Uw83oHJuaoJ3BGYq4EvYaTb9x-Cl5tn6MywwYPYw7rHMZv_2PP1SDlL_3V7SawSBXDI58_km36GbsB9SD4ejDf-jvnNAFZjQ6WZAbEfHBTS5ykPq3mHn575KQ7sT3S96d6Zw8EE3x8GrLsq0uKe2J8zrX1Ivit7BUYx-4gcQ7wFkd2hq26dipTvmzGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران: ببینید، ما فقط مانع آن‌ها هستیم. ما مانع تسخیر کل خاورمیانه توسط آن‌ها هستیم، اما هدف اصلی، شما، آمریکا، هستید.
🔴
به همین دلیل است که آن‌ها این شعارها را سر می‌دهند - آن‌ها ما را "شیطان کوچک" و شما را "شیطان بزرگ" می‌نامند، و آن‌ها قصد دارند "شیطان بزرگ" را از بین ببرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/150343" target="_blank">📅 09:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150342">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3319ed1ca5.mp4?token=MvziqQ_PSTqYD0bF0nbNXyhOXOjP0Z5ngIHUUfwDO5BJCQBpnsvZsn4HzzDbyMw9jgaN2OxQmAvFtcS7FHaxIYrgSx8q51iRsVR9SoF7hkD-2cidO6YEWj_UqE79NpyHoyAlZ2jIhBQB40edMa_MBDv92BLCeiRQAAsC4_XxOp708Gk8mZRxbTQ8vB3TEKihWy9atMS3fsxImR-H-7oKmHaNqALDY1zfTqev12YBxfYk5UHnftPECui8nuOFjKI7tyAMjpD1qgHJHGjfqd1FTmKnwVZhhMlIFODjZ8o7xGhcgCIZdhbH7OuY6HiR3cl95Lwbsi2F0Al3lKXVok0OLGgvnaS_R0eUxvMYoq-KaxDz6_GUeiHG46j9d2OFXC35rUfWi3_6_CsRwMU2dlMUJHK3vWEV0dwihmVpc8OyaSZJfhOyXl70bXk1hE9dZTU4tVPb-GgVsHsRGldth0S3Wi-zWS548cJIm6FuCYgbnhTxizU0WYVuhYcMNiEAgvDsLh5_LZJRhfrh0j60m6S3qVC6ri-GM1XJ0uGJAG2eI8OMilexUesJQxgzbQzSGIMh73ITal5e9c0IdVVQYjG9mPklHdZzeOMXmmb-Io_GrlvUxaClHdzoq45OpdGH90VjDFz33_S5M0oo2liRhYER6v1n_VQCZEBCDbXan9j5THw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3319ed1ca5.mp4?token=MvziqQ_PSTqYD0bF0nbNXyhOXOjP0Z5ngIHUUfwDO5BJCQBpnsvZsn4HzzDbyMw9jgaN2OxQmAvFtcS7FHaxIYrgSx8q51iRsVR9SoF7hkD-2cidO6YEWj_UqE79NpyHoyAlZ2jIhBQB40edMa_MBDv92BLCeiRQAAsC4_XxOp708Gk8mZRxbTQ8vB3TEKihWy9atMS3fsxImR-H-7oKmHaNqALDY1zfTqev12YBxfYk5UHnftPECui8nuOFjKI7tyAMjpD1qgHJHGjfqd1FTmKnwVZhhMlIFODjZ8o7xGhcgCIZdhbH7OuY6HiR3cl95Lwbsi2F0Al3lKXVok0OLGgvnaS_R0eUxvMYoq-KaxDz6_GUeiHG46j9d2OFXC35rUfWi3_6_CsRwMU2dlMUJHK3vWEV0dwihmVpc8OyaSZJfhOyXl70bXk1hE9dZTU4tVPb-GgVsHsRGldth0S3Wi-zWS548cJIm6FuCYgbnhTxizU0WYVuhYcMNiEAgvDsLh5_LZJRhfrh0j60m6S3qVC6ri-GM1XJ0uGJAG2eI8OMilexUesJQxgzbQzSGIMh73ITal5e9c0IdVVQYjG9mPklHdZzeOMXmmb-Io_GrlvUxaClHdzoq45OpdGH90VjDFz33_S5M0oo2liRhYER6v1n_VQCZEBCDbXan9j5THw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل:
برخی افراد فریب این تبلیغات را خورده‌اند، تبلیغاتی که عمدتاً از طریق شبکه‌های اجتماعی انجام می‌شود و هدف آن بدنام کردن اسرائیل است.
🔴
اسرائیل در اینجا، داوود است که در برابر جالوت بنیادگرایی اسلامی جهانی می‌جنگد، جالبتی که خواهان نابودی اسرائیل، نابودی آمریکا و نابودی همه چیز در میان این دو است. این چیزی است که آن‌ها فریاد می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/150342" target="_blank">📅 09:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150341">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نتانیاهو: اطلاعاتی را در اختیار انگلیس قرار دادیم که نشان می‌دهد حمله‌ای رخ خواهد داد و از سوی ایران حمایت می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/150341" target="_blank">📅 09:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150340">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8882baca16.mp4?token=mCI76XUC-CWypPlaPy1sIe_l6XQwALoOHWrCllZMste_nC23mnmJVaXZK_3CEmbmh9UYrBeO9YH4KBffxEJ3n3xmCUVjUJMJ45HoDyHUWtxBG5TvqSrhntR5G5Sw5eIGcCEZtxHzHS7idUXZ84gjFDcMLG6avSEQmOEhEw7Qbi1-blKPN7pS07qx9VwFy1k6De7dLK83T5PxC2htsifyDf_VUbxr7A6wZkKFr-rQPh_GAKDwHLP_h0UCGFkFzqITuvOSriEd4o_zvpCFMRrBD5UgPiABpsazMnpJ3V-XyBU25lphEh5gIjSUVJlRQkegJp8XUYU3RhyvHyMLxKBuxbD1Nh4YzMtFALIiV9xRUOeEG7X_SpPZECZ3BEys7Un0tkBLBPpw-wPu7W3SqKcaTLTV0t9q9pdBBVuKpg-oq8u5ZEJQzerAenkKkhhbEKGuJ7JTseuMEg_KbV7S8161d41966fiC7k4-pAPxGGlhu3Ngs3OnWmh-hsEsulGhVcdTw5GoplQEKm4Q3q7bumiqiYgCkyL_KzdqwieujwhNr-GjvD_sCX8PoeImmW0LCv3VYmV81mcYGM2QJmisr1Mu7O41w7MIALVmseBH8f8OSVUES7r-pvvD83EZl2Hxtf_PTZcyewIxg20_mIVnbD6pCa_vQJpAI5QnPvcEZLboQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8882baca16.mp4?token=mCI76XUC-CWypPlaPy1sIe_l6XQwALoOHWrCllZMste_nC23mnmJVaXZK_3CEmbmh9UYrBeO9YH4KBffxEJ3n3xmCUVjUJMJ45HoDyHUWtxBG5TvqSrhntR5G5Sw5eIGcCEZtxHzHS7idUXZ84gjFDcMLG6avSEQmOEhEw7Qbi1-blKPN7pS07qx9VwFy1k6De7dLK83T5PxC2htsifyDf_VUbxr7A6wZkKFr-rQPh_GAKDwHLP_h0UCGFkFzqITuvOSriEd4o_zvpCFMRrBD5UgPiABpsazMnpJ3V-XyBU25lphEh5gIjSUVJlRQkegJp8XUYU3RhyvHyMLxKBuxbD1Nh4YzMtFALIiV9xRUOeEG7X_SpPZECZ3BEys7Un0tkBLBPpw-wPu7W3SqKcaTLTV0t9q9pdBBVuKpg-oq8u5ZEJQzerAenkKkhhbEKGuJ7JTseuMEg_KbV7S8161d41966fiC7k4-pAPxGGlhu3Ngs3OnWmh-hsEsulGhVcdTw5GoplQEKm4Q3q7bumiqiYgCkyL_KzdqwieujwhNr-GjvD_sCX8PoeImmW0LCv3VYmV81mcYGM2QJmisr1Mu7O41w7MIALVmseBH8f8OSVUES7r-pvvD83EZl2Hxtf_PTZcyewIxg20_mIVnbD6pCa_vQJpAI5QnPvcEZLboQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا اطلاعاتی در مورد یک حمله برنامه‌ریزی‌شده به سبک یازده سپتامبر علیه اسرائیل دارید؟
🔴
نخست‌وزیر اسرائیل، نتانیاهو: نه، یک حمله خاص به سبک یازده سپتامبر. این موضوع نیست.
🔴
موضوع، حملات تروریستی علیه اسرائیلی‌ها در خارج از کشور، در اسرائیل و داخل اسرائیل است.
🔴
ما اطلاعاتی داریم که نشان می‌دهد عوامل ایران، به ویژه حماس و حزب‌الله، در حال برنامه‌ریزی برای حملات علیه ما قبل از انتخابات هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/150340" target="_blank">📅 09:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150339">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66334306bd.mp4?token=TTTWHI_S52YkqA4XCfU4pEl2Ewv-5Gv5RTWI7Jafo3ktHJ88qjVcM9iUuUkD-vzLKKu7ff8aJr4zJyyD2_Gy4IA5gPv9lDKFDRgkJZ41G2gwPaLSbdxVeP-eY-TkzU4efI2X2MVerxAtb3RkrajaOaLCgAuB404ZR4YrLYdhY3lCfYAQGhBR032L7HU58OmS59rXzeahbC2kk9gmqedn7Md0GD30UriUrpHI9u98acGJUakSmLmOa9eLgPIyZsZZ_dpvCJNmNouw-iILZba39ebF5xXfSO_Zk23v6h2peAARzF9tRGHcozeoVaCyNFyL9hC2LI-kEuLxu0HHEgi4NFw8PPw8tG8lP3AZCmekPNS-_1tTqdGcRlnqJ9Pv-lGAtb3Xv9nKAkKti_-i3iMyfM6dgEW5g17EFJmGH3ikHdSdAKULSECL0iRHmZloLBHiLlU8B4Z7yFBBDb8UzVFKXIOR0bnGV9HdeosSrQdPkY6i8FryqfwUAw07Nh2-nnyReDK6VOInODDAc4gvYpxZ9u9RJuF83axMA5-2H5VoqeBvq2Hr-9-AzXvkdFTzcXkUhzUWAkJZg86KgHN_2vcqWbUjzzpWdoDctvAKNKktoiB3LsdAVSAcPNLJAjwgnrXa5ksiR-KqXQtHLj7Slm7nV5AtD4i-aMxRa247UGAHZhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66334306bd.mp4?token=TTTWHI_S52YkqA4XCfU4pEl2Ewv-5Gv5RTWI7Jafo3ktHJ88qjVcM9iUuUkD-vzLKKu7ff8aJr4zJyyD2_Gy4IA5gPv9lDKFDRgkJZ41G2gwPaLSbdxVeP-eY-TkzU4efI2X2MVerxAtb3RkrajaOaLCgAuB404ZR4YrLYdhY3lCfYAQGhBR032L7HU58OmS59rXzeahbC2kk9gmqedn7Md0GD30UriUrpHI9u98acGJUakSmLmOa9eLgPIyZsZZ_dpvCJNmNouw-iILZba39ebF5xXfSO_Zk23v6h2peAARzF9tRGHcozeoVaCyNFyL9hC2LI-kEuLxu0HHEgi4NFw8PPw8tG8lP3AZCmekPNS-_1tTqdGcRlnqJ9Pv-lGAtb3Xv9nKAkKti_-i3iMyfM6dgEW5g17EFJmGH3ikHdSdAKULSECL0iRHmZloLBHiLlU8B4Z7yFBBDb8UzVFKXIOR0bnGV9HdeosSrQdPkY6i8FryqfwUAw07Nh2-nnyReDK6VOInODDAc4gvYpxZ9u9RJuF83axMA5-2H5VoqeBvq2Hr-9-AzXvkdFTzcXkUhzUWAkJZg86KgHN_2vcqWbUjzzpWdoDctvAKNKktoiB3LsdAVSAcPNLJAjwgnrXa5ksiR-KqXQtHLj7Slm7nV5AtD4i-aMxRa247UGAHZhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، نتانیاهو:
فقط یک میلیون اسرائیلی از امارات متحده عربی بازدید کرده‌اند. فکر نمی‌کنم مردم از این موضوع اطلاع داشته باشند.
🔴
و این موضوع در طول جنگ نیز صادق بود. جنگ مانع از این اتفاق نشد.
🔴
این اتحاد یا این رابطه، جنگ با ایران را نیز پشت سر گذاشت. و اکنون ما باید برخی از اسرائیلی‌هایی که در آنجا هستند را ساماندهی کنیم، تغییراتی ایجاد کنیم و تدابیر امنیتی را تقویت کنیم.
🔴
من بسیار خوشحالم که امارات با ما همکاری می‌کند. ما در کنار هم کار می‌کنیم تا مطمئن شویم که این [حادثه Flydubai] دیگر تکرار نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/150339" target="_blank">📅 09:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150338">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ :  دیروز یه لوله‌کشِ اسرائیلی که اصلا نمی‌دونست هواپیما چطوری کار می‌کنه، هواپیمای فلای‌دبی رو نجات داد؛ فقط با بالا کشیدن یه دسته
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/150338" target="_blank">📅 09:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150337">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKRnpRAidMlMdG06Madu7HfVOUqL0rbMa-xcCmvbipJHPu6LaANQhHhEbw1kKwZmnHNjXJBnVLuz5pWTzP0xRFwdto4VyA33TcjarAEL4tSailZauwxNh-TzHH4aOZGtcJH9xd0wQfHHmAJltWqcTsiATz3wwfTznUNudjtNzwgDnQWtyWqzVcZuO3LiV8TFrUg3HoFJV_yjQ19iqmnInpQVcVktcVOsbkUVdHsTzFLIg9W3v9uHAtk4Jsgkx_6pKJTR6O63VNHzvUDcsUHvci94ymnBPuWg-ZvbucQZF0D4ohbjsWgGa9njkr-K2y4b3Cq-lGIu8Xk-kWvZbnkeMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،از طریق شبکه Truth Social:
تبریک به شرکت بزرگ بوئینگ به خاطر تولید هواپیمایی به نام 737 Max که توانست در برابر نیروهای گرانشی و فشارها، عملکردی بسیار فراتر از آنچه که برای آن طراحی و انتظار می‌رفت، از خود نشان دهد.
🔴
این، نمایش شگفت‌انگیزی از برنامه‌ریزی و طراحی دقیق و قدرتمند سازه‌ای بود.
🔴
این زمان آن رسیده است که به شرکت بوئینگ، که در حال حاضر بهترین هواپیماهای مسافربری را تولید می‌کند، به خاطر "هوشمندی" فوق‌العاده این هواپیما، اعتبار لازم داده شود.
🔴
به کلی اورتبرگ و تمام مسئولین و همکارانش در شرکت بوئینگ، تبریک می‌گویم به خاطر انجام یک کار عالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/150337" target="_blank">📅 08:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150336">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
روسیه اروپا را تهدید کرد: اگر جنگی آغاز شود، کوتاه و برق‌آسا خواهد بود
🔴
ماریا زاخاروا، سخنگوی وزارت خارجه روسیه، گفت مسکو قصد تهدید کشورهای اروپایی را ندارد، اما در برابر هرگونه اقدام نظامی از تمامی توانمندی‌های خود استفاده خواهد کرد.
🔴
او تأکید کرد روسیه ابزار لازم برای مقابله با هرگونه تجاوز را در اختیار دارد و می‌تواند مهاجم را شکست دهد.
🔴
زاخاروا هشدار داد اگر کشورهای اروپایی به روسیه حمله کنند، جنگ «کاملاً متفاوت و بسیار کوتاه» خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/150336" target="_blank">📅 08:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2owFrsAU6MZjot6fXfdVnkvW4PfrZMQEfLuLZG7_mLmmhrgLzdKEAyzHpU7kJw5Y6xfr3iNBFrYf4dJQhg7_jfAkMsDP6zv5DgD3oH-XlKAr0KTiqs5kVSPYKVOwyYV4xj9nFuuWS6jO1QHmZo8BjdWq_haNPrTRe2pMoFFc4H_fl8XVgBdIYVjFx5OT6bzM7QvAwAtm_hcCrCgFs8-0GnGWAwie8UI7iSBXwEfM7OXk8vaX_8PpXg7c9uMJpabdme5ohr8wgMP5DvZiVO_0wicL6aGMMad3xiGaQCRtgQgd_htCMLq9LRP5baE89KiIUKgGNp6EgogfvsqlasRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران شلیک موشک به سمت اردن را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/150335" target="_blank">📅 08:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150334">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb52ef312.mp4?token=o13p04HQPfzFpRwQoDJDwvrtBq5RclBoVF4f3nLA-7hGeMBN1hQuCh5s-tWzQ6Tm4qgmTBTlGW_3TZHcHgbF_azPpWFjbxa6FF3F-YElhGHBwHdlreGKNYebiy1cKEEPL96vtbOnJp-BKauAOXenINjzm2s8AD1_K7EftpS1Z1QpHcfYo_813UO9iUTDtzQQNax__IW53D7hq8I7hD-hQEl9_mamIu_zEmUzQ4FDNxG5aDtnESvawRCrZEOLbDluLe727sWY_Z7hkPFBT3cdnXxIwKq3M-i-Bo7fYauPxIgHJTg9HZhZiC8RAJW-n8w8R-PBfgGgKPMjxiMhNZ8j7ZKxxwCf4I1DgNYfq6uoZ48ttVwbimC7jRC-DH5Fz7yY9sBqeF-3_nV8DUzTFE6x8vE3yn-y8RyWiSWPbkGeOa0UgvKbVO3eH2Vvrqj6UGq2cK_wU0RsVFGCgjwZHbg1uy6MDgrUuGkl6K-qDj8dOkxsKfj0lIm4yTnACqftCiWJuRnkc9fNqn1ZptU-yoI50qbJnggcWk24DllaABBk7pL7K9OJD7nG4hk011rxqJ0pjCDl7qZ_aBG2t5iOkG3_5Gpw4OC9LzNNCdqMSNwBrNcZI_vPT3XHxdMSPzyNVkssWY2pFe8HkkvlaO4LoZixd_pMlb565xAfe5yi-vEOUEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb52ef312.mp4?token=o13p04HQPfzFpRwQoDJDwvrtBq5RclBoVF4f3nLA-7hGeMBN1hQuCh5s-tWzQ6Tm4qgmTBTlGW_3TZHcHgbF_azPpWFjbxa6FF3F-YElhGHBwHdlreGKNYebiy1cKEEPL96vtbOnJp-BKauAOXenINjzm2s8AD1_K7EftpS1Z1QpHcfYo_813UO9iUTDtzQQNax__IW53D7hq8I7hD-hQEl9_mamIu_zEmUzQ4FDNxG5aDtnESvawRCrZEOLbDluLe727sWY_Z7hkPFBT3cdnXxIwKq3M-i-Bo7fYauPxIgHJTg9HZhZiC8RAJW-n8w8R-PBfgGgKPMjxiMhNZ8j7ZKxxwCf4I1DgNYfq6uoZ48ttVwbimC7jRC-DH5Fz7yY9sBqeF-3_nV8DUzTFE6x8vE3yn-y8RyWiSWPbkGeOa0UgvKbVO3eH2Vvrqj6UGq2cK_wU0RsVFGCgjwZHbg1uy6MDgrUuGkl6K-qDj8dOkxsKfj0lIm4yTnACqftCiWJuRnkc9fNqn1ZptU-yoI50qbJnggcWk24DllaABBk7pL7K9OJD7nG4hk011rxqJ0pjCDl7qZ_aBG2t5iOkG3_5Gpw4OC9LzNNCdqMSNwBrNcZI_vPT3XHxdMSPzyNVkssWY2pFe8HkkvlaO4LoZixd_pMlb565xAfe5yi-vEOUEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چه چیزی شما را مطمئن می‌کند که حادثه Flydubai یک اقدام تروریستی بوده است و نه یک مشکل روانی؟
🔴
نخست‌وزیر اسرائیل، نتانیاهو: خب، ممکن است اینطور باشد. من نمی‌دانم. به زودی متوجه خواهیم شد.
🔴
ما نشانه‌هایی داشتیم که ایران، و به ویژه از طریق عوامل خود، قصد داشت حملات تروریستی علیه اسرائیل و شهروندان اسرائیلی در خارج از کشور را افزایش دهد.
🔴
اما فکر می‌کنم که هنوز خیلی زود است که بگوییم آیا در این ماجرا همدستی ایرانی وجود داشته است یا خیر. فکر می‌کنم به زودی متوجه خواهیم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/150334" target="_blank">📅 08:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150333">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63f751ae8.mp4?token=DLDzyNjv5a9Z_F3wHT8D_Yf4w3oVBPu_MTeVYPOqAevcujRyZAIeHJHbDu_wZOfdTLaOn7kRE5gA7cIHt76Tz5CwiP883n50GJGoB6CsU4wSb1IHOol6uY1bc9mXVy1gn6I7lsNd_E88R_lODFWysyPW7BIcuDrLbOzYYK35_eb5M_KMtXi6Ijv7bsev0HomFg6CwNSgUngmR_sSpmkv4FyQnnHQH2_8tlLM88dR48Qjt4pBw3v1UsDntO9BC0jiaje8mk_Gtj9Llh-mSd8ZKuLlWkHsTozda9CYFjjI_k76e2sUKC6jYi5aY_DH2EYdQkkVJqGQCBNI_gU6dMIQ-IG0lyH5lyFtNtA2vdNZ46xSGIBsY5HXqL1lTeX-KP4uXt3YOFMp7a7TO1xwtoXzg8YtM1AavUGB3y7815v7jFP-itFrxVpNxnsqfWfIt6fhcnxqf0FSDtStFq73Vmt-d2aZ_nf-AdMucjqDSYDlAnkP4A3cDc19_k8OtuJZs5KUTiiRWHje0RJp2XU_HGtDKaIF99BON2UlZ9KtXFi_yOLCY5x5-tYl4zgMmNTmedIucBom5Dk6KlMv2pS_vAMSxk98QR4Bt_2sIljzM1EFpWol4h-IZQux0OXfNTy3iD9bVyEX0XYlxgpG692cSbky9oTCl3Ianxh05tgKQLof9XU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63f751ae8.mp4?token=DLDzyNjv5a9Z_F3wHT8D_Yf4w3oVBPu_MTeVYPOqAevcujRyZAIeHJHbDu_wZOfdTLaOn7kRE5gA7cIHt76Tz5CwiP883n50GJGoB6CsU4wSb1IHOol6uY1bc9mXVy1gn6I7lsNd_E88R_lODFWysyPW7BIcuDrLbOzYYK35_eb5M_KMtXi6Ijv7bsev0HomFg6CwNSgUngmR_sSpmkv4FyQnnHQH2_8tlLM88dR48Qjt4pBw3v1UsDntO9BC0jiaje8mk_Gtj9Llh-mSd8ZKuLlWkHsTozda9CYFjjI_k76e2sUKC6jYi5aY_DH2EYdQkkVJqGQCBNI_gU6dMIQ-IG0lyH5lyFtNtA2vdNZ46xSGIBsY5HXqL1lTeX-KP4uXt3YOFMp7a7TO1xwtoXzg8YtM1AavUGB3y7815v7jFP-itFrxVpNxnsqfWfIt6fhcnxqf0FSDtStFq73Vmt-d2aZ_nf-AdMucjqDSYDlAnkP4A3cDc19_k8OtuJZs5KUTiiRWHje0RJp2XU_HGtDKaIF99BON2UlZ9KtXFi_yOLCY5x5-tYl4zgMmNTmedIucBom5Dk6KlMv2pS_vAMSxk98QR4Bt_2sIljzM1EFpWol4h-IZQux0OXfNTy3iD9bVyEX0XYlxgpG692cSbky9oTCl3Ianxh05tgKQLof9XU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا در حال حاضر نگران پروازهای دیگری هستید که مقصدشان اسرائیل است؟
🔴
نخست‌وزیر اسرائیل، نتانیاهو: بله، ما نگران هستیم
🔴
من با رئیس‌جمهور امارات متحده عربی، شیخ محمد بن زاید، صحبت کردم و ما توافق کردیم که پروازهای شرکت هواپیمایی FlyDubai را به مدت چند روز متوقف کنیم، تمام شرایط را بررسی کنیم و تعدیلات امنیتی لازم را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/150333" target="_blank">📅 08:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150332">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: از زمان روی کار آمدن ترامپ بیش از ۲۵۰ هزار روادید لغو  شده
🔴
افرادی را که مرتکب جرم می‌شوند، از تروریسم حمایت می‌کنند، آمریکایی‌ ها را فریب می‌دهند یا از نظام مهاجرتی ما سوءاستفاده می‌کنند، شناسایی و روادید آن‌ها را لغو می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/150332" target="_blank">📅 08:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150331">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
اکسیوس: روبیو پس از بن‌بست در مذاکرات، روز دوشنبه از هیئت ایرانی حاضر در سازمان ملل خواست آمریکا را ترک کنند
🔴
منبع آگاه: عراقچی از قبل قرار بود دوشنبه به تهران برگردد
🔴
قطر همچنان در حال گفت‌وگو با هر دو طرف درباره پیشنهاد مصالحه‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/alonews/150331" target="_blank">📅 08:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150330">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
آتش‌سوزی مهیب در گمرک اسلام قلعه؛ ۲۰ کامیون در آتش سوختند
🔴
یک حادثه در گمرک اسلام قلعه به‌سرعت به حریقی گسترده تبدیل شد و ده‌ها خودروی سنگین را درگیر کرد؛ آتش از یک تانکر حامل سوخت آغاز شد و در ادامه حدود ۲۰ کامیون طعمه حریق شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150330" target="_blank">📅 02:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150329">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
یک جانفدا: اصلااااا مهم نیست گرونیا، گشنگی هم مهم نیست، رهبرمون هرچی بگه همونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/150329" target="_blank">📅 01:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150328">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: ایران نباید سلاح هسته‌ای داشته باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/150328" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150327">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ : الان تنگه هرمز را در دستمونه، عملاً اونو اداره می‌کنیم و کنترل کامل در دست ماست؛ البته می‌دانم که این وضعیت همیشه می‌تواند تغییر کند. کافی است یک مین بندازند؛بنابراین اگر واقعاً مین باشه، شرکتها حاضر نیستند کشتی‌های یک میلیارد دلاری خودشونو از تنگه هرمز عبور بدن. اما دوباره تأکید می‌کنم ، الان نفت بیشتری از تنگه در حال خروج است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/150327" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150326">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM7OQiRBFmX8jeE50Kx3-cx0xZbL7w313D11E0jujGGpAIBddRthG2BSlSBlvRgiyi58X8GcNbOnovJDbciopHSX2RmD_97zEODQt494SwRscPGQnAe-svJEka35p2FB-2Knv5BraG112XDo9QH0tk3Fqa6la1UlXi7UyjssdjymuJtnHviEuDW3rLcOJCeiEKmcS0P2sWKjUdlNDrrRvEem73rH824roMaLPT8cF9KNPWrVR6L9Rbr2gRGfolx3lTwS5Rf8ohvSkJKsL4peBvLefQbofTLlAmQHPn7utWXazTFW_O2JCPNWqm4SOWMHePkOAIhiwlwonmncA_z7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حکیمی: اگه استارلینک فراگیر بشه، برق رو قطع می‌کنیم
🔴
معاون وزیر ارتباطات گفته اگه استارلینک بین مردم جا بیفته، تو بحران نمی‌تونن اینترنت رو قطع کنن. برای همین مجبور می‌شن برق رو کامل قطع کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/150326" target="_blank">📅 01:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150325">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🤫
اگه توام دنبال کد تخفیف
🆓
📌
دیجی کالا و اسنپ و ..... هستی بیا
👇
🛍
https://t.me/off_khooneh
🛍
https://t.me/off_khooneh</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/150325" target="_blank">📅 01:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150324">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: رهبران آنها به شدت برای کنترل مبارزه می‌کنند، اما کنترل چه چیزی؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150324" target="_blank">📅 00:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150323">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed59a70323.mp4?token=Bw7DcePfIxNcZyRn6wSt44J57Y_wnhv_cgP8S2dBr5_Es4Ts_X8NAbBQMcex2DsiMEm_k-lCxkvL19WgwpE1UJdKN26kbz1HB9bLEfiT45Hr-eDAJ4oE5Ux-K6cLlYO1_PEjsp6W3s4C4TV3ji4qTnMerDT1pAABwqiWqM-S2rNf6vCs1JBZcrHyY5GMvjsmWDRh3iRGaeF7JdWjGCnY6fDib3dqzsDEV7EqWjBCOznTKwlrFSt83u39zj6W_VGswNFZC9yGmZNfGAFeVyjX1z5cv8Gl4by6JPiXkQNXnXC_LiVX9itKlTiMZhP5muQh-mvyEY1C98BJQ9PCqWtyQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed59a70323.mp4?token=Bw7DcePfIxNcZyRn6wSt44J57Y_wnhv_cgP8S2dBr5_Es4Ts_X8NAbBQMcex2DsiMEm_k-lCxkvL19WgwpE1UJdKN26kbz1HB9bLEfiT45Hr-eDAJ4oE5Ux-K6cLlYO1_PEjsp6W3s4C4TV3ji4qTnMerDT1pAABwqiWqM-S2rNf6vCs1JBZcrHyY5GMvjsmWDRh3iRGaeF7JdWjGCnY6fDib3dqzsDEV7EqWjBCOznTKwlrFSt83u39zj6W_VGswNFZC9yGmZNfGAFeVyjX1z5cv8Gl4by6JPiXkQNXnXC_LiVX9itKlTiMZhP5muQh-mvyEY1C98BJQ9PCqWtyQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
ترامپ درباره نقش ایران در حادثه فرفورد: موضوع را به‌طور جدی بررسی می‌کنیم
‏
🔴
از دونالد ترامپ درباره اظهارات اندی برنهام، نخست‌وزیر بریتانیا، مبنی بر وجود «نشانه‌های قوی» از احتمال نقش ایران در حادثه نزدیک پایگاه هوایی RAF Fairford سؤال شد. برنهام گفته تحقیقات درباره این پرونده همچنان ادامه دارد.
‏
🔴
ترامپ در پاسخ گفت: «ما در حال بررسی این موضوع هستیم؛ آن را به‌طور جدی بررسی می‌کنیم. ایران در حال حاضر مشکلات زیادی دارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/150323" target="_blank">📅 00:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150322">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=IPQu9w5DQ8MgBxpo5N2tgiVEKI6T0DUynl5eeBaL5UwoBYRom_SPxT0URGU1E72GwCshLJygAxf3DtjFQm8OlWRY4NRKJ7LC-ppuJam9h4tUAfIRBjvp7dI55wxeedSzJGM_-9edVtuY53oSQswxlpUeKG9oX4C4UmVOlPnHLQsl8XgingT0C_E7Lyh5V_ynFCR1XLAkGkg3ahfiaT4TtryrxSGJnfD8xKFAl74yi23H1krzPZSXyNCkuvvRASOOvwOEoK4V_RvGqNOGFkRRpNKRc14JdEcuG7unk4RoJ2bA8HQfuIAnqQkspSuCzXThHeLJywbREMb-ba8-1T0vig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=IPQu9w5DQ8MgBxpo5N2tgiVEKI6T0DUynl5eeBaL5UwoBYRom_SPxT0URGU1E72GwCshLJygAxf3DtjFQm8OlWRY4NRKJ7LC-ppuJam9h4tUAfIRBjvp7dI55wxeedSzJGM_-9edVtuY53oSQswxlpUeKG9oX4C4UmVOlPnHLQsl8XgingT0C_E7Lyh5V_ynFCR1XLAkGkg3ahfiaT4TtryrxSGJnfD8xKFAl74yi23H1krzPZSXyNCkuvvRASOOvwOEoK4V_RvGqNOGFkRRpNKRc14JdEcuG7unk4RoJ2bA8HQfuIAnqQkspSuCzXThHeLJywbREMb-ba8-1T0vig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شما ایرانی‌ها را «دیوانه» توصیف می‌کنید. چطور می‌توان با افراد «دیوانه» به توافق رسید؟
🔴
ترامپ: شاید آنها را بمباران کنیم. باید درباره این موضوع تصمیم بگیریم؛ یا آنها را بمباران می‌کنیم یا به توافق می‌رسیم. زمان تصمیم‌گیری نزدیک است. این ماجرا خیلی زود به پایان خواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/150322" target="_blank">📅 00:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150321">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
به قله رسیدیم
‼️
🔴
رئیس کمیسیون لوازم خانگی اتاق اصناف در تلویزیون : خانواده‌ها برای جهیزیه به جای ۲۰ قلم فقط می‌توانند ۳ یا ۴ قلم جنس بخرند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/150321" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150320">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مهلت ۴۵روزه شعام تموم شد
🚨</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/150320" target="_blank">📅 00:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150318">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ei8FR1xffKGpcmj_u_X-1CTX_2t0Kqt_47C5Nn8Y7vEEgeSHcn64KTQoeTN7BIidw4Wh_xmnsoJtF1onPqfImBXEymwDtYUaKRLqSGzrArV-7lmmFm3kqhAjdPS1DPYQW8qRl7sbQFSuu7xT647NDWi7136GbzQQSoHGNaUT3mGNU29OVwCgWbNRjojzkW62TBcq-5FfjZYCsUTimj3lSLqvx-JGQCDXgGpyXFj4m8MY53aYCASQygJ-fHSLjkn704jJvb1qpkeOiySwHMhzxdcqPEMpUxpE268j_5J0yPTLC20u2jKnOC8tOZ7R3XQ6m7UjXPsRwMILK-ZCoeYRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImlyNXTncMeHeIs5pgjXuPL62-KF3dt8cI5Q-sKwrAeH5D62zbvTMJjM0SUaMg-TsMEKkzq9baRa5wjpkfE46dfJoUNRKHu2iziNhR8eelO0ay8IHpe3UR2Jvqa0FrcMd7nBA0kOjMoFsCfFXJlhzQTDpbYJ3AaB9PKs5X54R4Xc2EIByEb9iyNAT5W5GlcW-GeDYeF0bdpNOterDC3FMkSZmF3H3clEO20l9CPod3yRIW7vhuX_3vYUg7MHfWsuXktarSv7PNJH-WJxac6a1aLVPCxXd1lUNCr_z5MTm7nfPDokUKkzZEVpzxpNInwL2zGPkTCcR1btwapw8E9Lzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یعنی رسایی الان تو زندان از اینا میپوشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/150318" target="_blank">📅 00:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150317">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
امشب مهلت ۴۵ روزه شورای عالی امنیت ملی برای برداشتن محاصره دریایی تمام میشه، شعام اعلام کرده بود اگر در پایان ۴۵ روز محاصره برداشته نشه بصورت نظامی و با زور محاصره رو میشکنیم.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/150317" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150316">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
خبرنگار حوادث:
امشب تو تهران یه مرد جوون بخاطر اینکه زنش قصد داشته ازش طلاق بگیره با یه گالن بنزین وارد پاگرد طبقه اول شده و آتیش بپا کرده
تو این اتیش سوزی، خودش و خانمش و مادر زنش کشته شدن...
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/150316" target="_blank">📅 00:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150315">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8de0ac9b.mp4?token=u9eFznJEL0XiQnAbc-GTuFbta5RpEzAtbUmUjS3uAzUOKX7jzL03rDtTglxdpNbXpQ5kvxAMciV7733PXwW4QNryVg88KumREZphF6s2f3HEW5wvgwjqOMuxE_Z190QbpHh9KHCwsE1H1Pn7vlcPPXO65w3J7PoF9WOIE3skazvC3ABJf-ME8botZCtFAXz43FKkiAlLYUbROhy--UdTFfE7Ga4GUCJb8hL0NSxs5xdrD_sxTgQCA_K5RSZldGnNh3zWdd1v3diPdl0s6-7SIvd71pnpIzZiZkSZrjUaQhwI9C9qElp0d4DvpNfCni1Ok7WEadwr8DliVDhV0ZW5Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8de0ac9b.mp4?token=u9eFznJEL0XiQnAbc-GTuFbta5RpEzAtbUmUjS3uAzUOKX7jzL03rDtTglxdpNbXpQ5kvxAMciV7733PXwW4QNryVg88KumREZphF6s2f3HEW5wvgwjqOMuxE_Z190QbpHh9KHCwsE1H1Pn7vlcPPXO65w3J7PoF9WOIE3skazvC3ABJf-ME8botZCtFAXz43FKkiAlLYUbROhy--UdTFfE7Ga4GUCJb8hL0NSxs5xdrD_sxTgQCA_K5RSZldGnNh3zWdd1v3diPdl0s6-7SIvd71pnpIzZiZkSZrjUaQhwI9C9qElp0d4DvpNfCni1Ok7WEadwr8DliVDhV0ZW5Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست خطاب به فرماندهان نظامی:
دروغ‌های رسانه‌ها درباره ذخایر مهمات، جان شما را به خطر می‌اندازد
🔴
این جان شماست که وقتی رسانه‌ها درباره ذخایر مهمات دروغ می‌گویند، مستقیماً به خطر می‌افتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/150315" target="_blank">📅 00:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af73c34e9e.mp4?token=FPnhi6H7UYO2_qRwcMBzxTFqGYD7nmjeemV77CS17nsKWo-b8NqDdMRKpS2BiGIn7bftUn-YX6hxelNSm93QFjnj0COraFMDS8PenPBca8wJAZcG49i0Us798Og-4JN3qHhGax0BZOYnWbMWoZihGouXfXJon6SUXZXorKDNp-Izmf_6d-Rxm-QEM6v0R5N7AEpFcV7luXiW4EPQV9GvLOFuNvPaTQZqb1MjRXKvQOGM8oYQDN4TDvOwGm0sEqNRZjl-dG8WuaTKm_glda_xiS0fFsTwdJupIlLxZg-ZCD_kB8e0YS4lvzku5r_thY5iPyAw98oBHm51behfzSgUPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af73c34e9e.mp4?token=FPnhi6H7UYO2_qRwcMBzxTFqGYD7nmjeemV77CS17nsKWo-b8NqDdMRKpS2BiGIn7bftUn-YX6hxelNSm93QFjnj0COraFMDS8PenPBca8wJAZcG49i0Us798Og-4JN3qHhGax0BZOYnWbMWoZihGouXfXJon6SUXZXorKDNp-Izmf_6d-Rxm-QEM6v0R5N7AEpFcV7luXiW4EPQV9GvLOFuNvPaTQZqb1MjRXKvQOGM8oYQDN4TDvOwGm0sEqNRZjl-dG8WuaTKm_glda_xiS0fFsTwdJupIlLxZg-ZCD_kB8e0YS4lvzku5r_thY5iPyAw98oBHm51behfzSgUPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت آخر‌الزمانی در مرز ایران و افغانستان که تانکرهای ایرانی درحال سوختن هستن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/150312" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb577d26a.mp4?token=gLQrSSJjTB6tkKRE2DXeXCE1c-aO3ZoOgNFO0PjU8SmEh-B_l-8LfOa3m4nVefj3OC-U3d2EWHclpX3mTysPG44WnQTfSq62PKGGx9XD7F1RO-VDfQrR20CyeNZap3U0HxyYOZDlV1t8ok7q2nVIbKh_d_ECChxH0Uj-ejKINLK-RVVg-41ApaPqg6tRdZ8xadMwFtRAfvqwIqqZK_NU3t5VTiMfZkujYS0yZ8tGQOnTyx-J6xIVwd-f_NNDjv-nYNx71KW1XoJOdn6bcrMHNlU8gOqwJnW4mpwdMn1WDcGcGH_-SRLUONSsn4nm9k3ALZGNF5OlhLzGWW9kwJhSIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb577d26a.mp4?token=gLQrSSJjTB6tkKRE2DXeXCE1c-aO3ZoOgNFO0PjU8SmEh-B_l-8LfOa3m4nVefj3OC-U3d2EWHclpX3mTysPG44WnQTfSq62PKGGx9XD7F1RO-VDfQrR20CyeNZap3U0HxyYOZDlV1t8ok7q2nVIbKh_d_ECChxH0Uj-ejKINLK-RVVg-41ApaPqg6tRdZ8xadMwFtRAfvqwIqqZK_NU3t5VTiMfZkujYS0yZ8tGQOnTyx-J6xIVwd-f_NNDjv-nYNx71KW1XoJOdn6bcrMHNlU8gOqwJnW4mpwdMn1WDcGcGH_-SRLUONSsn4nm9k3ALZGNF5OlhLzGWW9kwJhSIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست: رسانه‌های ما باعث می‌شوند رسانه دولتی ایران منطقی به نظر برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/150311" target="_blank">📅 23:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: پروردگارا، من اینجام. مرا بفرست. مرا بفرست تا با کت قرمزها بجنگم، مرا بفرست تا با کمونیست‌ها بجنگم، مرا بفرست تا با اسلام‌گرایان بجنگم. مرا بفرست
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/150310" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150309">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
توقف موقت پروازهای شرکت فلای دبی به تل‌آویو
🔴
منابع خبری از توقف موقت پروازهای شرکت هواپیمایی فلای دبی به اسرائیل خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/150309" target="_blank">📅 23:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150308">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آهنگ جدید گلزار منتشر شد.  [@AloTweet]</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/150308" target="_blank">📅 23:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150307">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرگزاری رسمی سوریه: در پی هدف قرار گرفتن یک خودرو در جاده پل مصیاف در حومه حمص، ۷ نفر کشته و ۴ نفر دیگر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/150307" target="_blank">📅 23:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150306">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ درباره کوبا: ببینید مارکو روبیو با کوبا چه کار می‌کند. ببینید با کوبا چه خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/150306" target="_blank">📅 23:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150305">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRLrNaCiXaqaTHdJTVMheBgktTCEpiYly_wdikYcdhu0U4ts7H4u6RkVx_HPF-Fs8_oEIvZoxvBeZcXEZHDDsssTHHzaOqVpfwx4KpNbUw9Ldhowofu2QsDDxGbuPMJuURMVFV8gg-q6Ny4ISpqN7Jz1zCL5RhkeJjKgMuAlhf_sYiS2DA9LiVuZvui0pBXIglQgM1-Yt2nlER7skZL9b8NwhceqPtfR9SPAfR7wQmffPvaWCqHBm2FKRVM_gnRVSGcK93t83AjSfZ1IkhwbGa-zbLYCXwKyuGM9dh2bNNySOAwjnakIV3mdDRl6C2eiP98bR7SNpxQD4srQDnKWDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حدود یک دلار میخوان بزارن رو چُس تومن کالابرگ، اینقدر کصشعر درموردش میگن،  چجوری خجالت نمیکشید؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/150305" target="_blank">📅 23:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150304">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbaf3d64e.mp4?token=r66nOnxCSoQ1a4mTw97cxxE4TBggiBUgTlcroCSHauEtokNwtrrPW7dmiX_zj8ED0R3Xev2QZQjHOujg90-R-Sy0d2slv6IHxnIHDvZ5ShGNeM8jRqUNJJWRE22iNBCaZSl-1oaZQIWBoLmH4WPjKcuqKz_u77rAd_zeKGZsTpeAbCinywd3y7QsiDa8CMrGvOojGhY9A6L4Kug8tO3OdoPzO2YpVwFxczwaMilZx2H5UsXlrMXFMpnH17_JgaxcSgLChXr1TWfqQL3ZOXh6nuYcOMLX8MC3qaBSSXrbId7qPLxKq066LS6e_Wmylr6CEL9r3OzaLg9lHmpOHHt9VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbaf3d64e.mp4?token=r66nOnxCSoQ1a4mTw97cxxE4TBggiBUgTlcroCSHauEtokNwtrrPW7dmiX_zj8ED0R3Xev2QZQjHOujg90-R-Sy0d2slv6IHxnIHDvZ5ShGNeM8jRqUNJJWRE22iNBCaZSl-1oaZQIWBoLmH4WPjKcuqKz_u77rAd_zeKGZsTpeAbCinywd3y7QsiDa8CMrGvOojGhY9A6L4Kug8tO3OdoPzO2YpVwFxczwaMilZx2H5UsXlrMXFMpnH17_JgaxcSgLChXr1TWfqQL3ZOXh6nuYcOMLX8MC3qaBSSXrbId7qPLxKq066LS6e_Wmylr6CEL9r3OzaLg9lHmpOHHt9VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پخش شیرینی در شب نشینی میدان انقلاب به مناسبت خروج آمریکا از عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/150304" target="_blank">📅 23:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150303">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
نیوزنیشن: ایالات متحده درحال آماده کردن یک طرح ۶بندی جهت ارائه به ایران است
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/150303" target="_blank">📅 23:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150302">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سردار نقدی: تمام توان آمریکا همین بود که تو این ۷ ماه انجام داد و شکست خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/150302" target="_blank">📅 23:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93aa1cd1d.mp4?token=Y5rmofsEgr5d8d9zp1kC6jMM8-bFAB8AEO26n9KIQVgVrzfjDE1JFyHVR_q8AsJ-Bp21qFB4sEKoHC63C7ZSOnjhlOkhaqn1UQ0jrM0wkBqgqeHZ8hieBUypSSXNZ7CRpxa5ijWRFBy_b8Xn0euLq1VWG50XOuRHkc8GYaJIE5RQJx5UoXfxWaHqq1FmaYlwzA7EoRMyBV6opiOS3Eh0JkXoKuGiamukdTz-jROC5yKkIf3DbmWTqhNTCGz8JWrTPHOc0AAb2XLhpsZNl4q2eN5E0-uYPZVPKkb4NcE_UJnwOMNzkEPCn_3NhvFFk4m9s6zUrlSwZlQxqHJ9RwXkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93aa1cd1d.mp4?token=Y5rmofsEgr5d8d9zp1kC6jMM8-bFAB8AEO26n9KIQVgVrzfjDE1JFyHVR_q8AsJ-Bp21qFB4sEKoHC63C7ZSOnjhlOkhaqn1UQ0jrM0wkBqgqeHZ8hieBUypSSXNZ7CRpxa5ijWRFBy_b8Xn0euLq1VWG50XOuRHkc8GYaJIE5RQJx5UoXfxWaHqq1FmaYlwzA7EoRMyBV6opiOS3Eh0JkXoKuGiamukdTz-jROC5yKkIf3DbmWTqhNTCGz8JWrTPHOc0AAb2XLhpsZNl4q2eN5E0-uYPZVPKkb4NcE_UJnwOMNzkEPCn_3NhvFFk4m9s6zUrlSwZlQxqHJ9RwXkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر هگ‌ست، وزیر جنگ:
مادورو گفت: "من اینجام، بیایید و من را بگیرید"، و ما هم همین کار را کردیم. اجرای اصل "FAF" (Fuck Around and Find Out)
✅
@AloNewd</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/150300" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
دبیرکل ناتو: «اروپا قادر نبود توانمندی هسته‌ای ایران را از بین ببرد. ما نتوانستیم. اما ظرف ۱۰ سال آینده این توانمندی را خواهیم داشت؛ می‌توانیم و باید این کار را انجام دهیم
🔴
‏همچنین باید این خود ما باشیم که در دریای سرخ با حوثی‌ها مقابله می‌کنیم، نه آمریکایی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/150299" target="_blank">📅 23:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRU9uFu25qfaM0AATmaRCnTYflkOmfpI1HL30pGPBT03pgIEbvXCY-2-oWUWTAb6ewP5dNtycHKEoe3eEGXixWZhfBosN-gMkDV9vA_pKSuBWwKZL5kcwmW4N-L1atrUuBiPl0xr5kgeBLlg_DohZ2lpQPyQMIOAorHUCz-h8z8L-GwQ4nRpO77e8lqnUXfFOAewAC5a1VaB2B-RHAd4oNci_iviYVYEndmmebNjD5R1jpoS_VMZVY68vEtoQ2l2AbgrWaPMpFK5U57OWEo-otnHHKqL2nhMKcXDH5Rv7EUn3guXNqbOz2RPqMdgBNaMKky7khuj7MWWg2RI99eryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه های اسرائیلی جمهوری اسلامی رو دلیل چاقو خوردن خلبان میدونن و میگن اسرائیل آماده انتقام خیلی سخت از جمهوری اسلامیه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/150298" target="_blank">📅 22:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
پیتر هگست : ما دیگر یک بخش "آگاه" یا "ضعیف" نیستیم.
🔴
نه افراد چاق، نه افراد ترنس، نه مردانی با سبیل پرپشت، نه افراد عجیب و غریب، نه افراد ضعیف، نه افراد رادیکال. فقط جنگجوها
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/150297" target="_blank">📅 22:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
پیتر هگست : ما دیگر یک بخش "آگاه" یا "ضعیف" نیستیم.
🔴
نه افراد چاق، نه افراد ترنس، نه مردانی با سبیل پرپشت، نه افراد عجیب و غریب، نه افراد ضعیف، نه افراد رادیکال. فقط جنگجوها
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/150296" target="_blank">📅 22:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پیتر هیگست، وزیر جنگ:
بله، یک کاهش 20 درصدی در تمام بخش‌ها اعمال خواهد شد. رسانه‌ها این را "پاکسازی" می‌نامند.
🔴
من این را "مسئولیت‌پذیری" و "اقدام بسیار دیر انجام شده" می‌دانم، و صراحتاً، کمترین کاری است که می‌توان انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/150295" target="_blank">📅 22:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
فارس: آیت الله مجتبی خامنه ای فردا پیام مهمی برای مردم داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/150294" target="_blank">📅 22:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرگزاری رسمی سوریه: سه نیروگاه برق در پی انفجار خط لوله گاز از مدار خدمت خارج شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/150293" target="_blank">📅 22:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
تام باراک، فرستاده ویژه ترامپ به عراق:
پس از ۲۳ سال از ورود نخستین نیروهای آمریکایی به عراق، ترامپ روند بازگرداندن نیروها را تکمیل کرد؛ اقدامی که به‌گفته او نه عقب‌نشینی، بلکه یکپارچه‌سازی ملاحظات راهبردی بغداد، اربیل، متحدان منطقه‌ای و منافع آمریکا بود.
🔴
این تحول فرصتی برای نخست‌وزیر الزیدی و مردم عراق فراهم می‌کند تا همه نیروهای مسلح عراق زیر فرمان یک دولت واحد قرار گیرند و آمریکا در جایگاه متحد، نه صرفاً حامی نظامی، دیده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/150292" target="_blank">📅 22:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150290">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0920eaa1.mp4?token=WXbF9PUBK8sjrsFU32dOw69v0mVodsw1VSD9lWEljIdUwUEEobRvqjXVD8ChDB7ssKAwyPqSaJQdXY6YnPaFdJXPQqQ5zuCQWxfI1mvOs4RgluJ9UPlvu4jRyHUJirFygXDV6YcS8naGT8qROgk4HThPnEfl9_Tm8j8wyn0Z1lZy1iQl_8zUgUMYK_BTteMQxTcJnILrEu7eKjx6GGaFg0RLe8lBWYwztv3f3p_m1JzoWkEKJ2U14O5PUnQF0kLWmek_TC0MXNvPUwTTYIEnNol7z-HpbZr7iaxZMMpBnh3CTI-5AKZJkMSJ4HllWGCfzNegs5M-RhqyjikyZhG0bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0920eaa1.mp4?token=WXbF9PUBK8sjrsFU32dOw69v0mVodsw1VSD9lWEljIdUwUEEobRvqjXVD8ChDB7ssKAwyPqSaJQdXY6YnPaFdJXPQqQ5zuCQWxfI1mvOs4RgluJ9UPlvu4jRyHUJirFygXDV6YcS8naGT8qROgk4HThPnEfl9_Tm8j8wyn0Z1lZy1iQl_8zUgUMYK_BTteMQxTcJnILrEu7eKjx6GGaFg0RLe8lBWYwztv3f3p_m1JzoWkEKJ2U14O5PUnQF0kLWmek_TC0MXNvPUwTTYIEnNol7z-HpbZr7iaxZMMpBnh3CTI-5AKZJkMSJ4HllWGCfzNegs5M-RhqyjikyZhG0bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع انفجار در دومین خط لوله انتقال گاز در سوریه ظرف دو روز گذشته، پس از انفجار خط لوله عبوری از دیرالزور
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/150290" target="_blank">📅 22:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150288">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خبرگزاری فارس:ترامپ هم تلویحا از برنامه‌ریزی برای آشوب در ایران گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/150288" target="_blank">📅 22:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فارس: ترامپ دروغ میگه! خیلی از سربازاشون تو جنگ کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/150287" target="_blank">📅 21:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: ما از نظر اقتصادی از هر کشور دیگری در جهان عملکرد بهتری داریم.
🔴
شما باید اروپا را ببینید. اروپا در وضعیت نابسامانی قرار دارد. سایر کشورها عملکرد بهتری ندارند
🔴
اولین جمله‌ای که رئیس‌جمهور شی به من گفت این بود: «واو، شما کار بسیار خوبی انجام داده‌اید.» البته، ایشان این را به زبان چینی گفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/150286" target="_blank">📅 21:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
کا گ ب ( اطلاعات روسیه) گفته اسرائیل و آمریکا میخوان خیلی سریع حمله مشترکی علیه ایران انجام بدن!
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/150285" target="_blank">📅 21:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ: من تنها رئیس‌جمهوری هستم که حقوق خود را اهدا کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/150284" target="_blank">📅 21:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ : آنها همه را در عراق اخراج کردند: سربازان، ژنرال‌ها، پلیس‌ها
🔴
آنها هیچ‌کس را برای اداره عراق نداشتند. و می‌دانید چه اتفاقی افتاد؟ گروه داعش شکل گرفت.
🔴
ما کارها را بسیار متفاوت انجام می‌دهیم. ما از حماقت‌هایی که آنها در عراق مرتکب شدند، درس گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/150283" target="_blank">📅 21:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما ۱۸ نفر را از دست دادیم، اما آن‌ها ۴۵۰۰ نفر را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/150282" target="_blank">📅 21:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ :  آمریکا در جنگ ایران به پیروزی کامل نظامی دست یافته است. خیلی زود شاهد اتفاقاتی خواهید بود؛ خیلی زود.
🔴
اما با کشوری روبه‌رو هستیم که عملا ویران شده است. اقتصادشان وضع خوبی ندارد. تورم آنها بیش از ۳۰۰ درصد است.
🔴
نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته و تجهیزات ضدهوایی آنها نیز از بین رفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/150281" target="_blank">📅 21:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / ترامپ درباره ایران: «به‌زودی شاهد اتفاقاتی خواهید بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/150280" target="_blank">📅 21:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / ترامپ درباره ایران: «به‌زودی شاهد اتفاقاتی خواهید بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/150279" target="_blank">📅 21:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ درباره عراق:
عملیات "عزم راسخ"، که آن‌ها این نام را برای آن انتخاب کردند، در سال 2026 و تحت رهبری رئیس جمهور دونالد ترامپ به پایان خواهد رسید.
🔴
ما به سرعت از آنجا خارج می‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/150278" target="_blank">📅 21:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b3d6d265.mp4?token=VBIDnmYSJQZTaEq4PDr8lABBIFfZ4Hcbri7GLABLLLSM4B2pw8nc-LenJwwB9s_4UqR90HaOlSQ2oi0mEhdHExbS1Qe4omLzVLhYT3QYNC4rnV9HBu6uPmpRRdAHlXtOm8H3u6EdYa7BWfNlsdHXTOKhGAMMY-dQ5Wb3tdQJJ0z_fZ96r-k45b0URAq_iw7n_1FypDVU1FiJHR5Wwf1AhTx8hCy6Oi6LziDWH5xHMB0VqCXFm0Z3rRuA-r5cTWFZ8R6KM7X8mnDpn-9bS8IpkmBhGQiRGOH2k-CfFO7aEC6mbNp0eau5bzCGrccaCgutfwJ_yLVgo0mrMhAqWzeWdbVtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b3d6d265.mp4?token=VBIDnmYSJQZTaEq4PDr8lABBIFfZ4Hcbri7GLABLLLSM4B2pw8nc-LenJwwB9s_4UqR90HaOlSQ2oi0mEhdHExbS1Qe4omLzVLhYT3QYNC4rnV9HBu6uPmpRRdAHlXtOm8H3u6EdYa7BWfNlsdHXTOKhGAMMY-dQ5Wb3tdQJJ0z_fZ96r-k45b0URAq_iw7n_1FypDVU1FiJHR5Wwf1AhTx8hCy6Oi6LziDWH5xHMB0VqCXFm0Z3rRuA-r5cTWFZ8R6KM7X8mnDpn-9bS8IpkmBhGQiRGOH2k-CfFO7aEC6mbNp0eau5bzCGrccaCgutfwJ_yLVgo0mrMhAqWzeWdbVtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره عراق:
امروز، با خوشحالی اعلام می‌کنم که آخرین نیروهای آمریکایی عراق را ترک می‌کنند.
🔴
مدتی طولانی گذشت و تصمیمات بسیار نادرستی اتخاذ شد که ما را در این بحران گرفتار کرد.
🔴
این وضعیت سال‌ها ادامه داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/150277" target="_blank">📅 21:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
آغاز محاصره زمینی؟؟
🔴
انفجار و آتش‌سوزی بزرگ در گمرک اسلام قلعه که ایران از آن به عنوان یک راه تنفسی برای دور زدن محاصره دریایی و هوایی استفاده می‌کرد احتمال خرابکاری عوامل اسرائیل و آمریکا را افزایش داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/150276" target="_blank">📅 21:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
شنیده شدن صدای چندین انفجار در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/150275" target="_blank">📅 21:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBP-DrBwNTwGBarbo5Xe3Ev_DBcJap3doKvTCPr4UYGEgcsrL7bXq8q3lRolnJg4bKQu1p9SKCKHnnGf-QLS5oNwBfDXK6kgrUGwUVP38cDS5ASOq8WCgh6lbRAiLGqIIT3Iz35rGgQIeVxb_kSAdYWFVNaXo-rKDAdqRpU2nb0L-faP9AJ9xh9L51VGBAcMrofpKPwC8P_Y4alvj96pe_uZRWbMTGW7iVPUH-m-tmmKS6jO-vVLyL2G5zcwr5lA-YHGTnt5gJC_Ft0Gvj164RZaC2HSlkB7BtW1T-vhdwz9jNGazyNIRrr2nScH7Crjoua70SQC3LEF6Yt7BINnow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: امروز، با خوشحالی اعلام می‌کنم که آخرین نیروهای آمریکایی عراق را ترک می‌کنند! مدت زیادی سپری شد، با تصمیمات بسیار نادرستی که ما را در این بحران گرفتار کرد، اما به زودی، این موضوع به بخشی از تاریخ تبدیل خواهد شد
🔴
امروز روز بزرگی برای آمریکاست و نکته مهم اینکه ما در حالی عراق را ترک می‌کنیم که این کشور از نخست‌وزیری فوق‌العاده و جدید به نام «علی الزیدی» برخوردار است؛ کسی که من از همان ابتدا حامی او بودم و تمام‌قد از او پشتیبانی کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/150274" target="_blank">📅 20:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
بلومبرگ: تخفیف ۳۷ دلاری عراق برای خریداران که در داخل خلیج فارس نفت را بارگیری می‌کنند
🔴
برای کسانی که جسارت به خرج می‌دهند یا دیوانه‌اند، این می‌تواند یک فرصت بی سابقه برای کسب سود باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/150273" target="_blank">📅 20:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150271">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYyAT950JqP0liTj2KyzepRJjyi1eKKSwQwGvP8gCqg3NbSmGfedJZLjX0mz-sHzGQ_mytluuEO-_GtK-WeI9hAtlL7b25_l9TXTPh5wGT-P72Ai_zSeO2Yl1zvwHLqZ8o1_OUneeUTzKJ_xbf6Uhm5J2bI1gubQKCgNkvcYLl8S4ZuLQ7tf5GPta7Bxjuc2gED2UZY_ruebGH8Vs7jfAE4VFmLIv7RS7CPtO6JbdcaD35LKHv9hzt3P-eLVmqMS2MiTMvuxUOZe3HRiWPoAsABOvUcls2PK-uTT74o5W1qJxfs4tzkRlfPCxhkCM6g5R8tmWCITiAxDJACKIHU58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۹۸ دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/150271" target="_blank">📅 20:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150270">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_BS09_ecvCVP8Y4p1KxTXHyV0ibQiASeVqrX1N9_FOmlXClUdTyS7GJwZnJSoqQ0jJSuVVJuCpFA-UlfRQyg7Ik_B9i4XUHeHKj4pmE2oPdtbM9yfs_-bK4RdDki4H-fCXCA3Ici9Du8EXpnLj34u1jaGAkQ4eYgMtmu9PNsX-Lgq9Kc1sisJ8JSO6eGotDslpBuv6ow3SC5Cp-MOatGkoYhyxzsn4bKWd2tDK-xOOp6uVnsTNknCKTGu-BNf-g15ga7Sf1uYUDj8FE7YmgWAfa7vC84FBalqN5NpxgIc0abh81TH-0Nfu7oXpgpYkVrOUdK_yfaMF8k9FuFLnhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : کشور ما در بسیاری از زمینه‌ها، عملکرد بسیار خوبی دارد، بهتر از هر زمان دیگری، اما مردم به طور کامل از میزان پیشرفت ما آگاه نیستند.
🔴
رسانه‌های خبری دروغگو از انتشار آمار بی‌نظیر ما خودداری می‌کنند، بنابراین من تمام تلاش خود را می‌کنم تا این کار را شخصاً انجام دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/150270" target="_blank">📅 20:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150269">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p244I_vbS09OSsF5QrbvJbObfyaG3tRcnVhBzJz9cyvrRE7wAmaa62fkxnaVF9wwvX3gTcYt2i7Y9IfGUPOW2JmyH21_UR4zMq8jGpJwC5j4X319q65pOnlfd8MfGN-b4up8tTmPfB_7oToywvzoCPG2V2gT-Kr3zkwzurWxyoA2ifBL2dgE1aAj_e72VDIDXYVR9OrJKpN8EwsIDCzOTUFzaIWMa54sWRNAlWp25Z_OOaNO4vXK1VO4lyuOKfsQI44pSJ-CYXKrqVQqaz94bdOyGhX9Z5Maq4ZCp3kG2KBgve_LZ_1VgClvsuZrnq4agFCUJcsVPObZ4TI0oxJefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد اسرائیلی منطقه جارموک در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150269" target="_blank">📅 20:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150268">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXOru75eXGk0DVNclsWrkeDWfBzHX3G2pFDq35cJlpXMJ5ccSVQlQJ1ZILHlmg-qsHpCX8mjRmDPazzOR9Fw7NbQZOODtj_-mHHeYYlX4Ib-xw6XG4A8F5NeKikuyBOmy58YG3vxbxuRu0pwgEFYgUc9MZelejVX7krx7e-_Xvw_r8xEZnjZsFQ5TLJ9nCPQ6NaEv_j-KKC5zx8jiExm035PzfPPHx-xb8VKqAaZIHXj--0C-RwKjDH2FHJGIBv3pktVb8mi7cfPyQtnDMu5OlZ33V7TwTpvFvlhS8iAvdrID5e-8-qt8lHRF115vr14RNfh1jq3IYyFc-eMzLfcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار ان بی سی: یک منبع آگاه به من گفت که عباس عراقچی، وزیر امور خارجه ایران، سه‌شنبه در دوحه بود، جایی که میانجیگران قطری نظرات ایالات متحده را در مورد طرح هفت روزه پیشنهادی با هدف اعتمادسازی بین ایالات متحده و ایران به او ارائه کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/150268" target="_blank">📅 20:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150267">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nbyH84lQM8AN-GIhtm3vL77HTNhZPnMw1DKCT_ieytrvYOksFTJd3yOnjMqTtIblkUcPCokPmgUK8Tm5D0B3sIrmUfHliSdzJ_PtZdXvz3-hrsSdA2JTH1s_a7jnV_B4W7V1KLbB6v3QzNinwuoISsarRuf62wx7xQEiRkMgWhJBOmhse19Xluv4nvk2QdaUrWOCx0icy6HH8ryui0FfCDqtW3bwiwz5O7vlo45Pa74DhL040BbAnZt3QT6dIKhPGdKbeQhbJg5_I69XFdI4iB5KKEc0k7ThVRNzVmaDBbGtLlcQ8xdXaRZB_hR9-p4Mxlmg6IgzO92hxvgDP06uWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این توئیت برای ۸ سال پیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/150267" target="_blank">📅 20:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150266">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی ترامپ و نتانیاهو در پی حادثه پرواز فلای‌دبی
🔴
شبکه ۱۴ عبری گزارش داد که قرار است در ساعات آینده، تماسی تلفنی میان «دونالد ترامپ» و «بنیامین نتانیاهو» در خصوص حادثه پرواز فلای‌دبی برگزار شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/150266" target="_blank">📅 20:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150265">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFHWM4CkuMb7luTFTkBD2A9k4U5KE0SJKvQ8ZNGXA6c-z4oTVNjEvfX7v_M5XZXKPI1hfMuhpCEy6oHoG0jXW7IOTP2peycgc3TWvaympj902bIpAyhT7mfa-E-aIi0FBaHt_RkJ1N7DCNqe7autpn1H-3DarbJAXlL6dgGV0AtrAhQ9JyE5FjrNTW5Rhgivr6SFTSCtYJ7HXx4Dh7tgRc1Tl6BFIKvlWBoEYASgtU4fpS0T7n_Y1y3SfWMDkM3LNkZYEnbuiTlcj0DbHTcda3h4q2zjBU35tX0kTzCPWbk_b8BLzFCqK2yoT6t4BScTDCbpEUPYXoJj35kD1a3gvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای ترابری نظامی آمریکایی اکنون وارد اسرائیل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150265" target="_blank">📅 20:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150264">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg8i2L9AhsZA8eoU8EbQDTn8Z0kQi_oV4ai_cg393iEWKBCwFpyA74pVIv6QMYS4ccs_xzKL7qxi2SX8MPba6LK37sZHNCaA_Qjh052Ocivmvu-2QMS5hGhLq_g_-4eki-lhlm-K6vpnXhqzyhSHXcgm0Irk8RureKg5HI-UmW3hVyBsmZGIC-PhGwkSaPtYvD-xUZ4yfitmVMxRf5JVN6ovzEPjlJPaGAZgXAgCu0hDtrZSYzosj6H4YvejnqDfveb5-eKpYz5o_zEjxJbpk_OJ_6PMMiMbljWs9WOic0LsQRY1zL8wYeb4zz6BVpyxUplV2i_SCDJiH1VHAxfIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادای احترام پزشکیان به روحانی در مراسم ختم «احمد ناطق نوری»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/150264" target="_blank">📅 20:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150263">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e800e50ff8.mp4?token=vXQQKJ0nZ4RZUrW8BireETDbQkDVDE7-sPoxChXQ83oTxELC4FjkHq8SsbcOltIsiMWlEp6LFpX1rGTyyqkmm2oOAM5zPUCXbWgsnkoc3ImgFr3Zk3SEOdFxvdGAP_7as8pP_xfBd_5QleVoyeeH9oh7gnQPgj3MtoYVGsHKwFFvSFSt4J5hEnwtWNhK6lNHXizLO1qeXhPzTX5cCBPMT2ajq9fXr_b2Q7kbTjk9tbFbt_jgX_K76bw4oZd_aKObQTNHyNK-Q9de215WBV8F6ZWYz8akww0XGvfirunV2ORkxbYPkhOWopmrbxivruyAw14CI1HVPNm08MCnKJaDpBawKKJYnn0Fcv_eLIj9hvsbd-TVP4uVqGnv06XQGfoqk0jnttTSBPkObJpXb5dzqrqsowfbbou71Xy95vNozaJ8kr-Ow0_ExdxVdGtEeJ_fV_tUrVfbFn6D12tvQO3urvnjJF61Bz3C3uk-1Jk9PHS1GKr2IoO76enUN1pGSl07pzQYOnQzY6HMHguTTR57syLhntf8z_eEcQYP31XPZTunyJ1i4Zz9Iy2m6O4skixjKJN4gq3GRyKbuD9cg9XWPIr9OyBUf5Azjr25DWNuDiwJT3Kh_r1H9oxIRUDCs2eeGM2sZGCAdDQKG_dZJsDAbnYN5sWmKQKcuB0U_T9jcOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e800e50ff8.mp4?token=vXQQKJ0nZ4RZUrW8BireETDbQkDVDE7-sPoxChXQ83oTxELC4FjkHq8SsbcOltIsiMWlEp6LFpX1rGTyyqkmm2oOAM5zPUCXbWgsnkoc3ImgFr3Zk3SEOdFxvdGAP_7as8pP_xfBd_5QleVoyeeH9oh7gnQPgj3MtoYVGsHKwFFvSFSt4J5hEnwtWNhK6lNHXizLO1qeXhPzTX5cCBPMT2ajq9fXr_b2Q7kbTjk9tbFbt_jgX_K76bw4oZd_aKObQTNHyNK-Q9de215WBV8F6ZWYz8akww0XGvfirunV2ORkxbYPkhOWopmrbxivruyAw14CI1HVPNm08MCnKJaDpBawKKJYnn0Fcv_eLIj9hvsbd-TVP4uVqGnv06XQGfoqk0jnttTSBPkObJpXb5dzqrqsowfbbou71Xy95vNozaJ8kr-Ow0_ExdxVdGtEeJ_fV_tUrVfbFn6D12tvQO3urvnjJF61Bz3C3uk-1Jk9PHS1GKr2IoO76enUN1pGSl07pzQYOnQzY6HMHguTTR57syLhntf8z_eEcQYP31XPZTunyJ1i4Zz9Iy2m6O4skixjKJN4gq3GRyKbuD9cg9XWPIr9OyBUf5Azjr25DWNuDiwJT3Kh_r1H9oxIRUDCs2eeGM2sZGCAdDQKG_dZJsDAbnYN5sWmKQKcuB0U_T9jcOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بلاگر یونانی در تهران: میگن حجاب تو ایران اجباریه، ولی این ادعا دروغه؛ من الان اینجام و می‌بینم که خیلی‌ها حجاب ندارن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/150263" target="_blank">📅 19:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150262">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE0Fn6uw7r_M_gSVPThfmDqPkvn2e7gUXaMboSRxYoaWi3i4IzBKd4QJH8gBzd_Iakm-bSr1n6vDq9jbCOG0DYpu1smBPJ5Mocx73DEDFWl0YjV3k9ZuqYS87LW20SBBkaf-B7XxDQcF8tBY0OU99fCF2b_RngQbnS545g-2ZGmtZTc6P0K-AOw2iIPH-JMq-LalzB20ZrIaT7X946OSAgBCM84gjBu0RNUhDAbr-P8lQWfacRzr_8afEVLCqpGOiKxhbWyhTJ3m93qUwBTapqOokiSvuy-UQzt06a2tj1jETxLQO1tviVSIUKo7C8WOjhlEDH43UliSNXoO0rzOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صف‌آرایی علیه وزیر اقتصاد در سازمان بورس معاون اول پشت تحرکات در سازمان بورس است؟
🔴
با نزدیک شدن به پایان دوره ریاست حجت‌الله صیدی در سازمان بورس، تلاش‌ها برای حفظ او و مقابله با تغییرات مدیریتی، به شکل‌های مختلف شدت گرفته است؛ از مخالفت با برخی تصمیمات وزیر…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/150262" target="_blank">📅 19:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150261">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ایلان ماسک: کمتر از یک سال دیگر ایمپلنت‌های نورالینک قرار است داخل سر انسان‌ها قرار بگیرد؛ حتی افرادی که از بدو تولد مشکل بینایی داشتند می‌توانند با این فناوری ببینند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150261" target="_blank">📅 19:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150260">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اندی برنهام، نخست‌وزیر بریتانیا، گفت «نشانه‌های بسیار قوی» وجود دارد که نشان می‌دهد ایران در حادثه پایگاه هوایی فیر‌فورد نیروی هوایی سلطنتی بریتانیا (RAF) دخیل بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150260" target="_blank">📅 19:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150256">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXoQRFRuzsqh2G72vF00bC16h_eYa25p_YU-RXKSIbi_za39Q62YrSXCpMS0G0erI3S8lCjLy9Ds2ZpmGTcNQWn0zwUpf1DxmhsCsIPsKj1_o9Xf4C-9RUCSnL7vnVLxwAm_sDXMP9PjU_UTygRyd7nd0Rps1HelGiIsB4GQUiHdn8Xce9ZihPIMU30g56mbu9gzmjP3KYI7BLNxeWbh6tNKn442QXSb-EIJ8fr5T5JAaHT_dve8W1yu_O6x622Z3Cbg7_wldcV7zpFF1ysF5fO-bpqjrA-V6wKivTus9493SATs3a5TwZ51kFgdHVKkzNGv_Ii7eK2EDsXeJLUREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyXL2OI_YUePC6z83D4JlFAkjYsExD7mL4CZ_uNg0kE0aFy7vioTfHPZDr70UsHQGtsBeBdq46QV-BK77z8gJlPJohbtf2ReCmOrZMqiTzqt8KKkwUQkoGbrR7jPNSYTmiEqCRYvNrkNofUVIYUFVTeXCf_5KFmO4vOD_zsV821GjO9P6KF_zZYNjCkkcEMHhkK-A_OFmDrqgyKVqwvcfXsMNJ7Wg2rf_x17tiostvCQ2w42qKdoqSTQhiWH41UuRcNirAQFC_SaJfTriXM53brUj81-EBI37LgRI1ubDWbRS7zo-AOYtxDnVCjuCTwzDDj3BYhd_jdEv46PmaYWjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e068cf4205.mp4?token=Uo5s81K4tynhkU67xyeUfl74PF4vSiOR9RsslhNenOVg7a9EFW6hry90ZzWKjM5xpiHwmXeJH0NHsM8pD_EAuiaOhzNiT7fymtqxmCy20lbbPM4OtsecFQ8TYkqA9VAlMG4pfIcN7wYg8vPGFVduLtfDkO78DJAbfiSW6u1Vx9YgtQaAbH1pY1J8kdVtcvgyYtitWpZ9e3FxfNGYVk0FAErLC8tIjIJgjErjdzwZW8cKLAZpNqoYYdfoebSdbWeYbimE9uPvF0I8-3O8IX6shEMenFfXua7Ql8g8vwVRAYip0RBBV_TmdhsLYMT5XstWSbilZ7oskxltnKq4BJHqIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e068cf4205.mp4?token=Uo5s81K4tynhkU67xyeUfl74PF4vSiOR9RsslhNenOVg7a9EFW6hry90ZzWKjM5xpiHwmXeJH0NHsM8pD_EAuiaOhzNiT7fymtqxmCy20lbbPM4OtsecFQ8TYkqA9VAlMG4pfIcN7wYg8vPGFVduLtfDkO78DJAbfiSW6u1Vx9YgtQaAbH1pY1J8kdVtcvgyYtitWpZ9e3FxfNGYVk0FAErLC8tIjIJgjErjdzwZW8cKLAZpNqoYYdfoebSdbWeYbimE9uPvF0I8-3O8IX6shEMenFfXua7Ql8g8vwVRAYip0RBBV_TmdhsLYMT5XstWSbilZ7oskxltnKq4BJHqIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسافران پرواز FZ1073 شرکت هواپیمایی فلاي‌دبي، پس از انتقال از فرودگاه طبوق در عربستان سعودی توسط یک فروند دیگر از هواپیماهای این شرکت، به فرودگاه بن گوریون رسیدند
🔴
جت‌های جنگنده F-15 نیروی هوایی اسرائیل، این هواپیما را پس از ورود به حریم هوایی اسرائیل اسکورت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/150256" target="_blank">📅 19:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150255">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فووووری
🔴
طبق اعلام بانک مرکزی اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/150255" target="_blank">📅 19:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150254">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
منابع عربی: ایالات متحده دوباره شروع به انتقال هواپیماهای نظامی از قطر کرده است. تعداد هواپیماها نسبت به ۱۰ روز پیش، ۱۰ فروند کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/150254" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150251">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddd1e8f01a.mp4?token=WNtiWGqJX9bqczfX9JCxPU8qvNaPE30Da-L1KQQ-RYRYnjVq6NTwbQvN_gxg_TiUMHhOGziuDPxax0IoMjCHLrUcRppm0bBV0e13H1UAnelqy344I_P6e3TIISJgxWsTG8VSl7ulWqOHfrx7P1W2WjbvwVJIcnShDLAj_Pl2gzK0rF1EgEjRqnF_Kj_DnLkcsPWqTQAhf8tUjmFC1_giR8c9VZMcnEpT8W3jxmg3INjCqU50O7JNs6SxrY2i-RWWZLMBDZQYH7UZUoEe2KESYGeyurPyKwnty74RdK_V15j7eLBZJy6KrDL3LAfFC8GWKzvaknqyq8gqkNb-GJmU7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddd1e8f01a.mp4?token=WNtiWGqJX9bqczfX9JCxPU8qvNaPE30Da-L1KQQ-RYRYnjVq6NTwbQvN_gxg_TiUMHhOGziuDPxax0IoMjCHLrUcRppm0bBV0e13H1UAnelqy344I_P6e3TIISJgxWsTG8VSl7ulWqOHfrx7P1W2WjbvwVJIcnShDLAj_Pl2gzK0rF1EgEjRqnF_Kj_DnLkcsPWqTQAhf8tUjmFC1_giR8c9VZMcnEpT8W3jxmg3INjCqU50O7JNs6SxrY2i-RWWZLMBDZQYH7UZUoEe2KESYGeyurPyKwnty74RdK_V15j7eLBZJy6KrDL3LAfFC8GWKzvaknqyq8gqkNb-GJmU7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی‌های مداوم در تأسیسات نفتی بقیق در عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/150251" target="_blank">📅 19:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وام برای خرید طلا و دلار ممنوع شد!  بانک مرکزی:  اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.  بانک‌ها باید متقاضیان وام را اعتبارسنجی کنند و منابع بانکی را بیشتر به بنگاه‌های…</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/150250" target="_blank">📅 19:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وام برای خرید طلا و دلار ممنوع شد
!
بانک مرکزی:
اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
بانک‌ها باید متقاضیان وام را اعتبارسنجی کنند و منابع بانکی را بیشتر به بنگاه‌های اقتصادی مولد اختصاص دهند و بر نحوه مصرف وام نظارت داشته باشند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/150249" target="_blank">📅 19:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نامه بانک مرکزی به تمام صرافی های دیجیتال : هر کاربر فقط روزانه اجازه خرید ۲۰۰۰ تتر را دارد
🔴
تسنیم: صرافی های رمز ارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/150248" target="_blank">📅 19:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
خبرنگار الجزیره: در مذاکرات، هیچ‌کس به‌طور صریح «نه» نمی‌گوید، بلکه بیشتر با ارائه اصلاحات و پیشنهادهای جدید پاسخ می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/150247" target="_blank">📅 19:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIcbXC05g22HOmz7jDBkQpvqsMpHagdehgeoIDpvBbgHDh6PHRykmAN1pZhula4FXmc8cjpZZMshw99qWBLDyzS-hDzenxO-CS2b2OTG-m0McISkiaVnrcfAHNM0210gtOAfWWZnjrJ8QvYAWvx9VHTzO2NVmuH6BiI_swqDeJ2iNsiNZHzWpqlBpcFIpwCrftmd7YXTKgRWBX8CpriyQ7k4OqHlyJ6uD9RrgnkgCmfamPPho8zazNI97oPvRZfmHofM3ZOoUbImjYh-rZhM8ATKiMA1tEloBUF-z8mAJcB4eeui8YD6pNn8-T3qkuku3CpqMSOe2aLJiuINhkGt1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: ایران اکنون در موقعیت ممتازی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/150246" target="_blank">📅 19:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150245">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
معاملات شبانه تتر متوقف شد
🔸
صرافی های رمز ارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کردند
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150245" target="_blank">📅 19:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150244">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
استاد خوش چشم: جنگ قطعی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/150244" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPDVnxYHpeBYactP_hdd3SqkroFxI6TbjkWt3H1iVLRcTa4Hy_midvCxB_PgOTlwg6C78XWJbkPGm85JisrPPIM0IRYe4DNlcsFuM35wf74eKTka0XUvOyn1XtrhKc_74HREfgAXMn6XLw49UgsjKga0An_H1gzQlU2z_lmQWFm_F6tlALYEzVAX47MImgGFsxH1cf5TekHAsElHL-bxiPczzn_rx_Q6gcZu6jcV1gcvN3R4OPFizg9N_YGwGN62Du5JLdBee7JzZ5JEMUIMtbBYCSl05UbJ1QENHZvlfYejKK0I37K8w0BATD8DTXPqRNX94_6yPw7UdDdiLwhjzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماچ و بوسه پزشکیان و کروبی در‌ مراسم ختم احمد ناطق نوری
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/150243" target="_blank">📅 18:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10869c87f.mp4?token=DK06qydIGnPnH0xGPT_gCe_RleuIbpdIZAjFdNwhq6Ym3xJqAkNFscUw5YkfzlICo7HAxwGt33u5Wk1ibeIdAL222Sf1373ydoiLv_DiBpim4zgGlae20Bn9bF-TbbsAa2UTtp8R0fTXgdUFaRpqE71RNfXPdoHFyC4zjTfBMsYpBP9Y7Zs6Imn6ZuVTOln_Q56vmBV_Tkf_DiWOenN-iDUi7WYwWLB3hdN2nkeD_4KLmYQeu94Iqv5oe5Xf5xBsbY1x94MJXQj9_Gxz12h5_bVJ5i_e7Wr6jzBhetrOzFPZoEvUA5DOIm2I7RTI8Ur975XI3j7p2iRfcAl0SceTZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10869c87f.mp4?token=DK06qydIGnPnH0xGPT_gCe_RleuIbpdIZAjFdNwhq6Ym3xJqAkNFscUw5YkfzlICo7HAxwGt33u5Wk1ibeIdAL222Sf1373ydoiLv_DiBpim4zgGlae20Bn9bF-TbbsAa2UTtp8R0fTXgdUFaRpqE71RNfXPdoHFyC4zjTfBMsYpBP9Y7Zs6Imn6ZuVTOln_Q56vmBV_Tkf_DiWOenN-iDUi7WYwWLB3hdN2nkeD_4KLmYQeu94Iqv5oe5Xf5xBsbY1x94MJXQj9_Gxz12h5_bVJ5i_e7Wr6jzBhetrOzFPZoEvUA5DOIm2I7RTI8Ur975XI3j7p2iRfcAl0SceTZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی مخاطبان از شلیک موشک در فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/150242" target="_blank">📅 18:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری/شلیک موشک از فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/150241" target="_blank">📅 18:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری/شلیک موشک از فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/150240" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
الجزیره: آمریکا احتمالا پیشنهاد ترتیب‌بندی جدید برای توافق با ایران ارائه کرده است.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/150239" target="_blank">📅 18:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bd09c687.mp4?token=CnKg3Ay7X2Mg7DpsokLE6uz1oAHbGDMIjEA2ZE5aQRavB38MfTNGjo2V2f7DhxBSuIOeGzuKgk6Fai5DVQI0hlunshS0s5j_G-YKTC_wXOCnial9bgaUBHQzUIpp1JnWUXn3sPCSIXjHQWkXHTK2HrXi-h2OmdPYYK3B2PYaA3Gj7KgSZxLSOWRGM1xTxmZxl5mwyuUI9CrAkq-9U-dLL1Zf3_nONAKzpW1uyPyyx5A0MArHH1wsKJivLluVtyG69FHfmMjbcnr1q9V6epbw5IjjkBVBC4B-BPwwi5JLaLzvZr-1oDAvAxGqDxny4b0kWb2q9BJNn91uC7HUp61Pww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bd09c687.mp4?token=CnKg3Ay7X2Mg7DpsokLE6uz1oAHbGDMIjEA2ZE5aQRavB38MfTNGjo2V2f7DhxBSuIOeGzuKgk6Fai5DVQI0hlunshS0s5j_G-YKTC_wXOCnial9bgaUBHQzUIpp1JnWUXn3sPCSIXjHQWkXHTK2HrXi-h2OmdPYYK3B2PYaA3Gj7KgSZxLSOWRGM1xTxmZxl5mwyuUI9CrAkq-9U-dLL1Zf3_nONAKzpW1uyPyyx5A0MArHH1wsKJivLluVtyG69FHfmMjbcnr1q9V6epbw5IjjkBVBC4B-BPwwi5JLaLzvZr-1oDAvAxGqDxny4b0kWb2q9BJNn91uC7HUp61Pww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدالحمید: به تخت جمشید رفتم آنجا محل سکونت ظالمان بود به همراهانم گفتم زود برگردیم
🔴
جوابتون چیه بهش؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/150238" target="_blank">📅 18:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150237">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا از هدف قرار گرفتن چند کشتی در هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/150237" target="_blank">📅 18:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150235">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9kt5HTylAhggY3MBFxUXOc0syg1Gaybx2Q4yTRj6jdbvRgeQcMEx08E_vaGnBfAvjqrhz5w1kUEANCadeiG4_n-_mlK9AELKVNja7EiazhLFWuMxwnH6ohLX3t1ivKIRRP4gfY7d7BPVr_uTrSHoRyUdmMVkqSZJ83U5Pw-HduOVaFDvCvV0lt7fhsdKCrihcpls6pRi4pUa-o_wkEhyRJeFidMILWDAjqPPwmg7G9OekvYz2xzfvW5VuaDv1Qe6qA5CCuTbHN39bkS8VKT_xlVhs-ZFDE5cgjGvrKv388TASWg6KClzdmQ9wuw4daVWRULsadG_vx-YDv38KiZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن‌پست:
نیروهای نظامی آمریکا از پایگاه‌های خود در عراق خارج شدند. این خروج پس از دو دهه حضور آمریکا در این کشور صورت گرفت که به مرگ صدها هزار غیرنظامی عراقی و هزاران سرباز آمریکایی منجر شده بود و اکنون ایران آسیب‌دیده اما با نفوذ رو به افزایش را در مرکز آینده منطقه قرار داده است.
🔴
نیروهای آمریکایی عملیات ضدداعش را از مقرهای خود در اردن ادامه خواهند داد. این خروج که روز چهارشنبه ۳۰ سپتامبر ۲۰۲۶ تکمیل شد، پایان ماموریت ۱۲ساله ائتلاف به رهبری آمریکا علیه داعش را رقم زد. آخرین نیروها از پایگاه هوایی اربیل در منطقه کردنشین شمال عراق خارج شدند.
🔴
این توافق در سال ۲۰۲۴ در دوران بایدن امضا و در دولت ترامپ اجرا شد. نخست‌وزیر عراق، علی الزیدی، آن را آغاز فاز جدید حاکمیت ملی توصیف کرد. ایران و گروه‌های وابسته آن این خروج را پیروزی دانستند، در حالی که برخی کارشناسان نسبت به افزایش نفوذ ایران و احتمال احیای داعش هشدار داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/150235" target="_blank">📅 18:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150233">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0d82bb00.mp4?token=M_jVW3cCCnchuk47pL4MMYlj87v8AzQCay-Bp3IDD8jpv7jWrpZwCJRzCjhotPfYHWqH5jrfwExmTeHeSu2xiO41_alxUrNaPTFsvXwNFtLy7g5AyoHzLZdsUlEe48ffyTcjMeSwrA2Pzr23D1BVZxgFQGbOdrKzS2srP6fHzSsCD2Xgke9ilR73jGYH5NheloCehHqqpt7oobOGWWIpR-vNDLTz7ZCZ8fuuMNtEHagv5yvHXTA-yJ8AWxBWsPNEIS9r5EDKJKtdM7ff11MrxwlkLW-G0zdr7C3aqzN6rUofFof8YE06vC3PleKK7NmzId-l8GhpBlShiXHlVTmjmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0d82bb00.mp4?token=M_jVW3cCCnchuk47pL4MMYlj87v8AzQCay-Bp3IDD8jpv7jWrpZwCJRzCjhotPfYHWqH5jrfwExmTeHeSu2xiO41_alxUrNaPTFsvXwNFtLy7g5AyoHzLZdsUlEe48ffyTcjMeSwrA2Pzr23D1BVZxgFQGbOdrKzS2srP6fHzSsCD2Xgke9ilR73jGYH5NheloCehHqqpt7oobOGWWIpR-vNDLTz7ZCZ8fuuMNtEHagv5yvHXTA-yJ8AWxBWsPNEIS9r5EDKJKtdM7ff11MrxwlkLW-G0zdr7C3aqzN6rUofFof8YE06vC3PleKK7NmzId-l8GhpBlShiXHlVTmjmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی تحلیلگر صداوسیما:
دفعه قبل ترامپ اجازه داد تیم جمهوری اسلامی از پاکستان برگرده بعدش محاصره دریایی رو شروع کرد
اما ایندفعه قبل از اینکه تیم جمهوری اسلامی از نیویورک برگرده محاصره هوایی رو شروع کرده و اصلا ترامپ دنبال توافق نیست بلکه میخواد حکومت رو سرنگون کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/150233" target="_blank">📅 17:47 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
