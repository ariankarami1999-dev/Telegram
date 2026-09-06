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
<img src="https://cdn4.telesco.pe/file/iTlvKHoaHmCU_0YdDnUHUscsOCcq1E1HBRv7UKT9sQvuk1qwy8EkI4gp70CZgvm6q4U9wE2F57MLDYSOAQ4ewhct-C2FbFUdZeNO1l9cmZNh2rMiH83L3AiP-w3U8stC7K6rV5lgeNeLPmB5QHUS83r0ghJRN1MnnBhe-HjCJ9alMA8AsE0dC0iG-0LPVUT0rJo6qGmhx43UkQo_Y8PhdL8i7-QYYREni1esZy510zG9ppNuOZpMhHdEW4A8Jm1F2SFwOHxgUMa1hEyqr9o3OYuxRbBODJ1J-o04Ze58J7xI0XsGyd6_29W4essNzn2-8lt8njDTAYaUOWx-D6-bEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 593K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 12:33:46</div>
<hr>

<div class="tg-post" id="msg-29165">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQGSh6JyEpXqnB05IDpW6jaIAkg-19IvHwMJ51XUNgqxcnpWKRX3Y4G2yqSDBaHSC7ce9NpAK3Y01s76hqwQQBBXP35UQG1Uy84fftZ6SNLz_NrLokDOGyC06ctSVMyxRpzuMJKdBazTDUPEfqER6VFvEsMp6--UIiTLVHbDv8tFobofAG_kLaoVDtJFdPevwMVNFvz18S0XYfIdaj9hUMhiLOVSVdJ_Rjwlxy1FpGfP--yAqQ7X6a5J9uOvAXbr7A4xIXQbVYon69R9lv-QWyNfggRPvIA5B2sf4P5I7zvAQqRPhACBOJYkEZhbnANNKHq0JKQ6lYkNKvWJ1jCNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/29165" target="_blank">📅 12:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29163">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYTS-trzNgmpJGZduooqZI0l0JNZa0_Q3MkYdqZRUZBi9cflu7RfCguzwF6B4a4b8U4DB3fKfcpfheb-Jk5TC_3GweVMsTwrEe6CSdoXtu6pbMaDiYi5VPbI-8kjGTLJbVEFhVSWxx2x8R2bs_nLsTfJSy8aquxoii8fcVJZBq4ivSaaoqtFUboJHzxB0WPh6YX2JuLpKAhLmlfEDBc_G3Z2PgKHb87OgkKdY8gxfWnnpdvTBLxBvBN4Ae4XDZcIl4D05AFshqfTvYw2fA2fKIccPf7wQE493fDpvKGSquyUcRzGqUO2DRxh7IhRjRVc_ZwDu_Y6TkjHgijcqZ5Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBJr2PKSzj4T2iY7bscNFHw7DqlTYzi8fD783Gho7PAIg5MHotohmr_HrFPmxCBsAmvLFBhNqKQX9_lo6MVrQx5VzOqHtlhQn0ePCkcSk1uQhXqLu-YMFczx94Rqxyo61G7FzwodE8Fg1IfocZUJKAvM3RyeydxK__4FbjjqzEHwHL429xEv2NLBPENrnZEIbPcub_pjadVtw4Fm1Z-OY1XrnIF9nAr1Q3AF3CPKt_mA9A6kjKpGmQ01dx6UxP-12x9YHvIhc9bk0Qww29MnVjFou66A2zqyLdIDP_g2VS7yUrQVV-nXPuYQV6QRN1E9T4cCTQhlZZzDmPF_6dIYvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
همسرگابریل‌مارتینلی‌سوژه‌عکاسای عربستانی در جریان بازی این هفته الهلال در لیگ برتر که از گابریل مارتینلی ستاره جدید خود رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/29163" target="_blank">📅 11:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29162">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chBLtNctKhUyaE-NiIfNq0pkCc_Xo5YUHzzQ3h9lUhQ-2Y0VvR9XhGWMGaLHh1orBhSKYLZmFexFeUPRjgG1Dh93oHpwQLt3JCau-WBndi3oqxndl_GMG_CnzlrrG_xdf2xLxLCM2bUrwPx4kOvlTSlwo__cDYPEDmcOr67aG5KWdbsPYbNJL2cOPel2_VKqDkSk1b-o4HnfcdDfOMVoabmsOoSAkPbLZAY3A8GMsIQfUtQFwyMtlTbpz0S68grzkvdnilIFdimvQyT6ek277IhJxxARxT-JFxiS95Ccv_IeRZk5-CRE2D3aez3d0fOB6anNYNmHZHcG7-RB7RkYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت‌دردناک و تلخ ایوب الکعبی مهاجم 33 ساله المپیاکوس پس‌از برخورد با دروازه‌بان حریف در بازی شب گذشته تیمش در سوپرلیگ یونان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/29162" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29161">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇪🇬
10 گل‌تماشایی و فوق‌العاده محمد صلاح ستاره مصری سابق لیورپول در دوران حضور در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/29161" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29160">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCx4lNZHQscYGCzI_Va5Yo0FR0ycnOEMRrio8sIxZbQ3vl-VOZN8qBqOPNuaXtONrkWguQzqHX_gUVuy2QURRa77oAAf2PSB3xJju3lzwZBR8Wfvp8Get6cFXJaHz97PeZjyQFLdaOXAUwhZIKA_xDR0Gpzf0zG7vwo2zWRtL5M-XUymiLKwutvOdfRWYturZs_-sNKeO21kEVqMkxs5KUFUvVRG9rqf_r8bf1ML6xmtxtk0tJNqB0E5rky4TW_nE8n8_BCjV_7jX1whVQ4IW-Wrmjar5HHSDarYYRbdCV4xglst3cWmswW09geea2V5GDBXeHAxphOGJkxTGVm3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/29160" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29159">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/29159" target="_blank">📅 10:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29158">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=UjAyuNXoUcnoIVcS-kPJMdJ0LcHSI45CDukZDQiBXY46U4vA1HHeiCQKCgKnyhuRPLL9X453MPIKFcwhw8gG9i2hCj40QODbqsreSvTJmlUgVmqvQn1OTSP7AUjx6HEIgN2VTkcUUCWsBND0HOhwt3jDJ4Kub_BRR0C5fu17wTtXqV3BhXP4wKUTPnTEfo0VuwS_tL2m_t63hm1QGTnftIifR_D5DVylzOUmgIsoWI9BrmmTOALsth71199KgDXyll8EjyGHLfcwr8C_i1dL1uGdxhzoqcVue82Z1CarkaIVB8TMLHU2rdknlXKC9OiwO17XMDtIkO2yH60fYcyhgA21S482oCCVx2GyUTbHeo_Dj6vM5LpDCV1MESpm_P6vhk7KPYz7lVk3AjEJa4nBKr37CCQbPy_qbDnRURcUFn3K21RGS0nr2Va6lFWutiBfveixOhABnGb2UWKeoKfQfzUXGMdBz_I9ibulBB_1pLiPfTMtSxZJiPb8l2n7uwUpjIVrXZ0e0c46fOsMa3Sx8o-1A_Uk_QRNL0JzHGkhGI5S6e2bDXArZZZA4h50j5IXqdOn_xLZDtsDfPtG2UsjAlDanOU_jiwa4yL4KISOooQwgwjVLhGCU05x_G-qySa9X9ZM618nDbo50DEF3hIWtfsjozD5K8u97JejaZaFfC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=UjAyuNXoUcnoIVcS-kPJMdJ0LcHSI45CDukZDQiBXY46U4vA1HHeiCQKCgKnyhuRPLL9X453MPIKFcwhw8gG9i2hCj40QODbqsreSvTJmlUgVmqvQn1OTSP7AUjx6HEIgN2VTkcUUCWsBND0HOhwt3jDJ4Kub_BRR0C5fu17wTtXqV3BhXP4wKUTPnTEfo0VuwS_tL2m_t63hm1QGTnftIifR_D5DVylzOUmgIsoWI9BrmmTOALsth71199KgDXyll8EjyGHLfcwr8C_i1dL1uGdxhzoqcVue82Z1CarkaIVB8TMLHU2rdknlXKC9OiwO17XMDtIkO2yH60fYcyhgA21S482oCCVx2GyUTbHeo_Dj6vM5LpDCV1MESpm_P6vhk7KPYz7lVk3AjEJa4nBKr37CCQbPy_qbDnRURcUFn3K21RGS0nr2Va6lFWutiBfveixOhABnGb2UWKeoKfQfzUXGMdBz_I9ibulBB_1pLiPfTMtSxZJiPb8l2n7uwUpjIVrXZ0e0c46fOsMa3Sx8o-1A_Uk_QRNL0JzHGkhGI5S6e2bDXArZZZA4h50j5IXqdOn_xLZDtsDfPtG2UsjAlDanOU_jiwa4yL4KISOooQwgwjVLhGCU05x_G-qySa9X9ZM618nDbo50DEF3hIWtfsjozD5K8u97JejaZaFfC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/29158" target="_blank">📅 10:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29157">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IICJlb-L9bGKAdY6_qkK7dgwm2HcGW5zvwmhyc8caApLbVVM_k2GWGsGaPaTXP_Rq5HVEmgfizT1rL-S6sHIW_LZyAN4IKtiw28tnoAel_GvOGFJhu-r9qLV2Za3fwrjp0wPNAI--O49GZ-C4U_jQ473wnJau014Z9_dMVmEtCzbajH2usUqMbN1EFn5BBRJqzniIUlRvTDMUfvTilGdhGAnoECbaw4uoScLBJi9QJtM4egjJzaMIEuMkl2AHuxGOOxFtWZePcmj1VI33Fm0Hmbp3AZVgU_p3PGzQuA3O4iTZvyQclLwOIlh8JQu00UgahZY-7J9GDIDn-YSdy5bBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/29157" target="_blank">📅 10:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29156">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO1mmWWe0o3qQBStYF8rlTTF3HW6nUDgxsesBHfOm91UXpwfPtFAIn47vN3uztaCzcQgv73wpyu7eK-r15UC_jkGirJ9dsacS-hLhrcgQI5WcxVgzp2TstUrMV-zgekqTSHSiYcXOT-hTIPTJGD8433LWhWtpteY8xdsW2fgAXt8XxE5V6d11Fmrzp0Er94FOKWAPqfPC-Rcw3uD38GvCXRn0sRN4eJGoRzr7xOq3ddWL4jQfCYHCfD6Z1q3fwAJInLhq7s2z8Sp_mCr41F7nfmqsyPpEf8E-yYtHEAH5WpdG_OW7clDeYCVt-d8G_owNqLmlFfx9aFUkFKx2njhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/29156" target="_blank">📅 10:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29155">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/29155" target="_blank">📅 09:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29154">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3xhSZbgJB11VjrLXYRD-KRLiyQxlFc59ct8BvjJFRt9zbyIdyZ1PAiI0iW6vppIzeFhSzRENSQ7rqMnY4caDbCJ_3z4bPaEoRAtwi_vF16kzY399DgKWjstpjSCOMhr5JZQsbTFopzU6KwXIxYn6JdZBRQlz4vBxM1JLMulRMuIahBJsKVKOF5g9YotP1PrLvFC8hjmo9DGIlC8IJtB_4bfCwqCSGk_ZwsL28QXCWQ3q7vDZeOZsAmjtXZSHnH8jxBvFdoywqLYm-2sYS9ApQTPm6h3tYhcUuNvu_OAO7Wx2FA5exmjW4Be1NK_PkX5tt5rGk7SybwzcKQ4dHKJ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/29154" target="_blank">📅 09:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29153">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29153" target="_blank">📅 02:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29152">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=vtgU5jYeJ20rPDnPSjpBh0KXWfq-ycj4As0SFafbvezMsxx6ls04i2fnOqcffr7G_lQy7Na5V428gyNilLMf57LvL4ewrijUakPT0ZBBQRt8EojrCRRlc2DE-e0FHJxO0Jlv6URsjsAcmzpy5UN3SV_CHOScRT7SpbMu3DqlNmJHB_8450cXpsxmrdF4DWlhWc8CLk4zphbeBm1_SuEZtXbFiBhv5TvTsWJsT7WI1JGQn9JEwZzmn_gOpgTUVmJDPV02FyMd-x8-c3Z1MYivFAagL2hexfeTq8E8kpLC0AE3aqYdwa8_jMhVAnbA8FfUC8GT0_3KzdbRVq3XmV2DIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=vtgU5jYeJ20rPDnPSjpBh0KXWfq-ycj4As0SFafbvezMsxx6ls04i2fnOqcffr7G_lQy7Na5V428gyNilLMf57LvL4ewrijUakPT0ZBBQRt8EojrCRRlc2DE-e0FHJxO0Jlv6URsjsAcmzpy5UN3SV_CHOScRT7SpbMu3DqlNmJHB_8450cXpsxmrdF4DWlhWc8CLk4zphbeBm1_SuEZtXbFiBhv5TvTsWJsT7WI1JGQn9JEwZzmn_gOpgTUVmJDPV02FyMd-x8-c3Z1MYivFAagL2hexfeTq8E8kpLC0AE3aqYdwa8_jMhVAnbA8FfUC8GT0_3KzdbRVq3XmV2DIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
رونالدو دربازی‌امشب تو اینصحنه داره تلاش میکنه ببینه رو برگه دست بازیکن الاتحاد چی نوشته شده اونم بالا میاره برگه رو میگه هیچی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29152" target="_blank">📅 01:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29151">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6zhiesy1spcnHhzmDkJVOf2zVwFkuXroufn3QyD9HzhvgYDAv1gGsU-b-w59u2ODokNlZwhXvOQYKj7cL9IlKBSv91bbmazoOTCJwfHonC0Xs1ZAGUWkNzX4Q7IX9aJDoqW5QzJ1wi_RNrZVEDwYDjoSTFq6miCKFwMOSfciqYKBrYlf9Z1el5InlQhCgicksxNyB5ZuFe6x-oBQzvDVRNs0w0OKrlh6qsnn-kyzkjgnIJIMyxBBRNYlWx1p4w5SZ0NCJ8aFP4AOSwIR6wiHpKJuNamzfAB_ybWJN8VnyybhCj9p4Bfv-QwCmh1mPJMl5kzZXlYWVhFC44WUMl89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29151" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29149">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7TWOftEc0n1E8Nty8X4kJ24aZUoDwG9O64vMIyr13JAUUvYIEBqOOlOQYZzD9ZptxkVQe5IRBFtv0srKg4bUfgLszjBW8ew5DcxlMEhJXAUBKZtEeyxWfxfzcf1lDi8Ex4U8hdQK3IR3ZyuI86s5pxKVQO5kzqYRE9uNzHtUd1Yf2FW1wY-gbjy-iLj-tHa5FvFMBi3J7KlioRU_p7pdvhJTQfezfn08ePQZzHMARq6CvKtSdak2IDkpYiKaSPcgVFo3jWu2V6TGrnuW9TCRh31WJd777ER6O6j5IPe-K8UcMqJKnmPjBt5VVxdiQ7iZ-OPjS5_-64I_hInDbo9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از جدال استقلال با ایرالکو تا دوئل شاگردان آرتتا و آلونسو در استادیوم امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29149" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29148">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ_rLt_kmrALv8RPve3vUGEXTqxQw0Awu3KNnYoPDImABt0Xu7RVFoAD37D0rI1gld7fYMxlCdMvzW5eweFWDCull66n749aLfxJz_q-LWiPOxUOjappLPBMR7i12vpVNzzzFq-F371_N2HIxFxb_CbNlrZZ1twdohpdP3UqYgqMpWcA8wO2Z0hmc4lrfkVpgqLvKV0caGiaA7yWjSdvw0X4stMPoEn5mlGrbq1cjwkwfYPjUQZTCbI9llMVEYYw_wFf4Ghn95VR5uo6Hcwf3mbCcFPNRojpDt0dcCy19-mJZJBpAX9r4MvxwassfCHp_S27ilLmylHe2-NgX07CMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از شکست یاران ال‌چولو تا کامبک‌های تماشایی دورتموند و آ.اس. رم مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/29148" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xktb6J9A3CUCfTEZ0FlNmqJ9nl79qC_ir2lGssIaQQdEXIb7IxARkniqmmgtTSoprOt4JbOuSki2GHQH1q_tyicmcSBkW3bWBYTiRBAbF01qOJhnQMJQhFRDu9rqMHsF-7V1Urbt_JexbnnUJv_bBzF24WvAMa5ZV-WSWuP2C8eIuGG-AGwyj7S3R0kaXBoAVW35mLCfZp3DMC-dVxl3wRvwKCfDt_7Z74Ca2pEbzpBc_zqP1K3jGNxx-03sU43D1ySW3wI_5tg6mb_6P-fHR2rVzOfRY_6dYXJUoa9QYAbrHejFAbwuP6ZpFgsb4s0ebCajLIIWBU9xdzta--CFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29147" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pLeCtRfEpFyBcI4B0wlcDpNZ-9wODDf9jIm2o0QNzDjHFr0KtOAo4uy6iU48p0CCHpwGFO_6Sh-lxGZya30FZ257WcxWAzICuAZ6mZUGa7MzG1X341fuY0hmuX4UbTIgzjlMAGXIjmH-oKPf1igEZ6IGSzFy0e7mP0YgqCyWzboGAG1uNV-58azUjhELpI7V0C6fsX1mqxkSEoeHubq9KIXN-uTp9WRQt2S-9QCA4sgstGhK0gXC8Vxd9Ews6Jt9EYvm_YW5CUpZDuRdRl7O0UMEYBMQWl2uLyw_njMkP-_nuVghSxRZWve-y3YNQPPhzN8BSRUavYJvWfByGYnSYbk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pLeCtRfEpFyBcI4B0wlcDpNZ-9wODDf9jIm2o0QNzDjHFr0KtOAo4uy6iU48p0CCHpwGFO_6Sh-lxGZya30FZ257WcxWAzICuAZ6mZUGa7MzG1X341fuY0hmuX4UbTIgzjlMAGXIjmH-oKPf1igEZ6IGSzFy0e7mP0YgqCyWzboGAG1uNV-58azUjhELpI7V0C6fsX1mqxkSEoeHubq9KIXN-uTp9WRQt2S-9QCA4sgstGhK0gXC8Vxd9Ews6Jt9EYvm_YW5CUpZDuRdRl7O0UMEYBMQWl2uLyw_njMkP-_nuVghSxRZWve-y3YNQPPhzN8BSRUavYJvWfByGYnSYbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29146" target="_blank">📅 01:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29145">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/persiana_Soccer/29145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‼️
باشگاه گل‌گهر: خداداد عزیزی امروز الفاظ رکیکی رو برای امید عالیشاه بکاربرده و صداشم هست که او به این بازیکن ما فحش خار مادر و مثبت 18 داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29145" target="_blank">📅 00:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt4P-VEHNRlG1Bla8dJmnrPmyXJs6Q1jFKptx2XOGZgUMus971WwnK8us50y7JK4rux_8F1j5Gjq9yFrRSuxzRrAqnxKMMNZZyRC2EhsazcBCQbSKI8GH_DMpVpuiBlBa_2HOXdEilPTnYLrlHSCAi1MYrjZ9WdhDQKMqbq3DHBmd4iYVE57HG3hasSb67TnzhXM5FoAQnWXyhR9c4bvKCnJ4XesbIGthJ2MfiDeieu-hgoI9NPzvJ9Ht-Q_bWvzr0oFCtTzF9aQkWto9lgMoikl1vMq_FOGQNzDrRbdauh6CS9iJXH0I-v_uLNePmsD_WvvJwzqYdib4yPHACR1CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیای‌عجیبی‌ شده؛
یه مرد تایلندی که از فن‌های باشگاه بوریرام نیزبوده دراقدامی عجیب بیضه‌‌هاش رو به 2.7 میلیون دلار فروخته تاماشینش ارتقا بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29144" target="_blank">📅 00:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcAQozp5n4WaSOADLtAVvxSCq3YFMEvNBv8GCIGCbVBVv7fqgN4rUqYQYdUPoLWJ8w2byeSzdcaSFncE-T4ung3TaLTLHZgKWsWcqKC2r1-zXHLC6b7qrxr1HezKLAqVaA-9R3rYshHujOkrcz6ZVyQ7gbsR7oQ8LYgmRRdYL66I6lzZSzK0vr7JCSOwtKgr4iANjNfuNEB2Krl96IQ3fNuo9oudLEtBzb7bRC2byWLRqpQPhDYgGxw-aVXcg5AgIWjlupquR5OCg62QmejWqxdwp5VQlOmjWArE_VxR-IOvPYVbjSpxMYY8KM2cw7j0xlI6WjVfE-C5zAKu2q7XOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29143" target="_blank">📅 00:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29142">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=e-nd1tEEExfL099oqwNbBUufS1BxoIfEqhFVEPcYmaJTTTwI2Q628ceeJ5q6iOCklGTcNArwFHypcJ6iFd504c0BXnvGWuKJv3iboEbQjKQNHJMeDNMyTX5nuQq_yBPLzGFq4NsrXf47RcQb0SvYsygSkCp5g0vv2qe48HBSnUOER2cIDjBpzwQiwMFc4nI_0h_X7580v2hahD0n2_baJxjCirB5ixL3jucOGPPVDhz1looBH95I27U0D-YlvseyD6rzi8yWq-lKaJmA6S4tQvBInDsrA4Q1KH4bs4k0yuGD4wfbgvYzwNE9Q0Qk-tHCPEp7SDYPJpjhg8Cp_Tu55Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=e-nd1tEEExfL099oqwNbBUufS1BxoIfEqhFVEPcYmaJTTTwI2Q628ceeJ5q6iOCklGTcNArwFHypcJ6iFd504c0BXnvGWuKJv3iboEbQjKQNHJMeDNMyTX5nuQq_yBPLzGFq4NsrXf47RcQb0SvYsygSkCp5g0vv2qe48HBSnUOER2cIDjBpzwQiwMFc4nI_0h_X7580v2hahD0n2_baJxjCirB5ixL3jucOGPPVDhz1looBH95I27U0D-YlvseyD6rzi8yWq-lKaJmA6S4tQvBInDsrA4Q1KH4bs4k0yuGD4wfbgvYzwNE9Q0Qk-tHCPEp7SDYPJpjhg8Cp_Tu55Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29142" target="_blank">📅 00:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29141">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNzb07PK6bqqOILnDvKMvxisPKpcYdyJrm9Tm1fE3n-ID3tIBudqRrMGm4PtziIZZIQuVEQe5v33FbqeOuUy3vV22G_OuT6J_JUjBQEWeVDiRr4SPYDSOi1GNMI0m02-6CGYiUA7DFH_cfTRH5Lo7KhgWHegQMlpn-XUUOMQuY4Oy7msacwHzBCZGNnGkvDOonMqLDGRfRHS5SUPTo6VGtLgUmzGkOxe40oZb-ynpKqQn21g2q4Jx-xJRaiwdiYRzj9bwPm-nDCBHrWtID-4CN7jP2JMaJRBi3OaUMaBcFVNMl3AnxXnntgfKz4-ChjuOXJrl8_DvErlGrsm8udhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امیدعالیشاه درجواب‌صحبت‌های خداداد عزیزی: اگر سابقه‌ملی این‌گونه است خدا را شکر که من بازی ملی ندارم؛ نان بازوی‌خودم را میخورم نه چیز دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29141" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29140">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbTxZW1CtHvk798qaprIPq4VO6SiOPHH0dLKjTOUsnEDI4Kz0jSkMsqnusFxDgFzbKIcDCd4jLoFNGHTKI4vrkbpGUHm8RdNAfZD2LuFy5sHbeDVjAf3pMUVSprh9VwB3L0f_d7HFZZiZdX42VJ4yu3q1esQUfa0ZVS0X5LjfhXR7VUVUHb96jaB7zxZCxO3OvcIZZ_R2N-DdYVTpXOfz2SG6Q_ROhJf_IMvu8sV_7OBmXXIkfB2tsVfG364zsfHIMcV--pTz6wcRrJB3OVSF11nR5t255oaOeJydnf9Xz_-We0vZXAViCrOKC6n2LAuAkAXBw_IzCBSLIkGGK_zVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29140" target="_blank">📅 23:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdQsboB7rMHY0sIiMqs1j0_5zt31PgLmfceK3vQ_7vBTF9N2w3eDQbtfC9mRB4DRUF0NPNvcEFxXibza8dQhufNOAmJJ1c2z0KDfdSwpOMnUqq2erZAIyIt0078MvzQTCQ3_Ld160VlHw0GOFv-LX9130w5e8JP6rQbRtlucDomMYGScSp66xkbaXfqeMpDllMZNDVi8YRneQJ4jQll1sQDXNWNxABiZa9JhsVChcApsuL8sKESnh5CafV73s9eq4EYVHNW10_WStyJCnq74pSa_V0bB-VdRf7O0G43kLu3Cqld6xE8xaOEI1zC-Gf9otk4LJjt5o7M4xyhy0JGtzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29139" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtlSu7trYMJ9d19U8n1pL1PTEHkleLct8Rrj62GfxV7ow8JOlokZ8KEI5as4Vff3YBrJqcwPGmXSzWjnREwTRnSm3SVPw6Q9F9gOjt8kOS-s1LtHuy5MfP4gcR4VGSzeEW4Z11re6oWxWjx2XE8_0bMoKx8X7vi-tLORjrOhm-jsVDPrmem1gm2v6stnoaKiaxFI8bzflx1mGmskkUgoUJI6SUGlNw3K6dhyl7FDit8SQOa5GrHMDGncvrxvgvrGsOk9gjKqnqqgx-0liqWWneUKidAGlSBBYSkvFUbXaktJ75hOvIcWCNGZ1hxWmFuGJwp9YT07mjjH6rY4uSnPI8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtlSu7trYMJ9d19U8n1pL1PTEHkleLct8Rrj62GfxV7ow8JOlokZ8KEI5as4Vff3YBrJqcwPGmXSzWjnREwTRnSm3SVPw6Q9F9gOjt8kOS-s1LtHuy5MfP4gcR4VGSzeEW4Z11re6oWxWjx2XE8_0bMoKx8X7vi-tLORjrOhm-jsVDPrmem1gm2v6stnoaKiaxFI8bzflx1mGmskkUgoUJI6SUGlNw3K6dhyl7FDit8SQOa5GrHMDGncvrxvgvrGsOk9gjKqnqqgx-0liqWWneUKidAGlSBBYSkvFUbXaktJ75hOvIcWCNGZ1hxWmFuGJwp9YT07mjjH6rY4uSnPI8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29138" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy0mE0gHIgpuQC3Od16gGsCGXJFLw2fbBjiPt6BarhPxkUUz7yduoromjWA18PP5xnALv1QwDEi5LdEyzGTqloqkrwZ-PI05I7w57DKBZkwS4C5a5CpR7JGrwC2v_fBhG3tgmlOt3goz9Uoo0MUoyn52r5ncN_ynVNRuuHqrwoe9K_C-Adx0p9HKlbp6ocBzsk9DuAT_T_5-azuv8X_Zboi6N8nnIURiMs8m0UrTSiea-8dC2KRRFSt9LC9s1AJV7Ph4LoNCdsybYPnSzzqrLHCPaC0pQV64hrvgnBhKFznUsOiaVHEo-M-N63XzvTrtRCBW7ZpD8t80zZABeBvF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی تیم آلومینیوم اراک: آلومینیوم تا حالا استقلال روشکست نداده؟ خب نده، اگه‌ اینجوری‌بخوایم نگاه‌ کنیم باشگاه ما تا حالا بایرن مونیخ و پاری سن ژرمن رو هم شکست نداده‌ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29137" target="_blank">📅 23:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29135">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZy3bb_hWm7J5tx4JoV5tum6N5Y9Bz0CDN4lVpf3DEgidAtXQmWQwKcDX6_TZmZochdpcsu_NwccmCB22kTWD5NJOZH4yyQwiA0sI3kXkANu6MR7wRR7neyep6xiHCvf8rlxmgJLYxgI6aZof5UfajIOOHvZGFZlJ_vFGzsUpLKis14qTM5P3jw-KCyETjNdrYbixjtO0jRvlKhb20gyj0rAu3QC8i6csJXu3eDKwMHAK6nhSTxJsqOjwxmSJr2RfCrlTLjN4OViJirdgowrrRCfvpdd_QCUc_CGzRA7bohCEiN4vahFU8y9wp2G1dQnoUrlUpQbBVXbJ-35fyDN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUebRUzK8OaPIkFVDMBZRNxjp6YXqqOQctUBqDeurq56S3IR3uaibe9R-MYylTCMFumndpI9mDZkuXa30sbhDZVaVqwaJXAuGlKbbOFVL8U0y3sFZXKc60BXnYmEUdR_P7AOBC5SqVQUnDhyMsPuJOVDsbq-nXmaFjzxS8zj0-M3GbXAtMOFR66J5qj3XTKesiLByhyC86DGQhXL6z0Lw7m0DdjasGbq2MEhUOO2M_BI71ciCtu41u8N6kAkdRvCEaAQlSxxvp9Y22oHcrL88MMyHKHs2RXtURViICdDx4PhRQHgD8xjN1AZggalLQKOw_vaKd4NHhOhdte-9F521A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در لیگ نخبگان آسیا دیروز عین آب خوردن دو هیچ کلبا رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29135" target="_blank">📅 22:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29133">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXIauOqpONpe-hxerj-sBquKqmdZADGNHhPOrBZ4Q_wu0AVTKUvIHarpSdTKUpXrydskEjqQxB5kQ4RZgJz9YU4_WwGbtvMC1MumX8WxFLsL3Gb1EDAygSuD80h6NGFvgt3nEWWVeKPgHYw2hv9dZYmC17jyC_U2FVlA6tIKy-X4eSuujmOKlBAkqv7oi2MJ6RJOi_hz5ZeYbmFEzc_hXmS_w1mcFJTLxDyyqtfSd7K-HWpaaUNf-1I2kqn4qGFiyIzDrb41y1Cy8L-XRAhHbgtOVkfR07BwKP6IkCUC4X0fQzjt_CSqBxS40gnegGFjkTEt4ikoBr3M_upJv9H0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWC-VIiXDE76ZJmy9Ujp62yaHbTv1pi031dDINf_zpgx17p-pmM4L-WSa3_-125P-S_iMobGWk4fmrx_dQSbuBwzsheaWJwsgJs1xM1Chuj3QlI5Dujcl3KYPO9zu28BZ1f3lVr5DReaePf8VJM4OCk0PVibIeKGJF5iGGvgVxn7RzY1MCZPrdKDzVDpE6gRAtJiNnyzP9yccQnGJflSbMize2DRwwLhI976ZPcM0ydg-nTCU9d39sgeDyEpZ284jM_mLlAApciJhEF2ubKJGSIrN_UYDHsILSqF_Ec5jdxAWObgfq9v2ssE_EFP-3fX_rKJhb7FL3fM-d9UwZ71XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29133" target="_blank">📅 22:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29132">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29132" target="_blank">📅 22:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29131">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=LNCLMkBCQMnJCaOAZX68IUptbWAk2pYXbwDue7eWZPZUUKjctyrddsWysnSwzejNh14khzPPSqHwPrQmOLZ6KuYO9vINd_OmNsJmfZRCjctZhODllzGv8KQxVWzXc8V_o-YfNUNK0O1Ca1rCsAbwU3M8ObGjjYwMFJZGCe0d4XzUNumsG3f6TwmWZGRrB5kFJ5r-kxazeE6UgafBEA6JA851lgMrINihnhRX86QjrJaxuktRU9Q0ndG9rrHiQal8dejlmuy-RfopmGk38XstcgUQDUykby3DoYVRtYIQ25fZYXGk_BSNPNxAlPPM8CWPAUfYKQNsEirRnMOaNpFhtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=LNCLMkBCQMnJCaOAZX68IUptbWAk2pYXbwDue7eWZPZUUKjctyrddsWysnSwzejNh14khzPPSqHwPrQmOLZ6KuYO9vINd_OmNsJmfZRCjctZhODllzGv8KQxVWzXc8V_o-YfNUNK0O1Ca1rCsAbwU3M8ObGjjYwMFJZGCe0d4XzUNumsG3f6TwmWZGRrB5kFJ5r-kxazeE6UgafBEA6JA851lgMrINihnhRX86QjrJaxuktRU9Q0ndG9rrHiQal8dejlmuy-RfopmGk38XstcgUQDUykby3DoYVRtYIQ25fZYXGk_BSNPNxAlPPM8CWPAUfYKQNsEirRnMOaNpFhtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سهراب بختیاری زاده سرمربی استقلال: صالح حردانی بارها ازش بی انضباطی سر زد و بهش تذکر میدادم اما توجهی نمیکرد. برخورد من فقط بخاطر رفتار حردانی در مسابقه دربی نبود. تا زمانیکه من دراستقلالم او دیگر در این تیم جایگاهی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29131" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29130">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnHZaJ64ATF9kzONk3Ck1LUpnt9RCKPYKSv3KgWrZHKMjJaCan4DAOcD5jNxOwSLMP25NQcNIgV23Nj9NoauS6-wZx46MTpcbv0jFMHPvLjz6M9U6QUCtOZkPDRudYqY2-2bhsKJnSqDXpFrpZlzvTldPmxq0-WSLw3Hpd_O_-CGaHoa71V6SVm_PbwHIU09Lz0cnvp2uQXwE43l2rt-LBAHrgsCyENbGd9iBKyA0cGhmvBrqYpcOFGFJ8QQjwDOCE2benEhHeD6hg6qQC4U2R1kAlzk3VLVI9-VaPhn2wfLyvjLhUU-OwkmuKXTzptDOTFYXdOpRhznHUxDyummMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29130" target="_blank">📅 21:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29129">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwvgUdaQLB47huEDjWHBasqgFLVLvOn0pl4G_Sh8FGjQzvRc3BGJamvYOh33gd1EnrBD7aC00YaNbBrzlA5IihgUD8s-bRKjv3fCt8pcy0paD6DGrA9WJ1634hIO7MSDDJb-9uWDJ5-f4h4u3kgvxzs_9zPEjvUgd9wmAmqfu-VWA8QcjFTLzp1gtnIMebfckW4TY8X1A2c1rnwUmKx2Qyq7Nc7pAy9cfWv4C1qkNgg_tDRHD1qF7gDnTiVN0jAEpJVKduPSm5e01Lre_8oNU6_--FDjVJ5GwI57fz1j9tL2YRqm4ibOkWAm1REO3YxofUVH_3trKQsqKEWJvMm_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛
اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29129" target="_blank">📅 21:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29128">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29128" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=j5xcIltAidjp56eyE4nccj-Lxct1lG3m4TYsnLdD_FLJgS1CQALDKfaGHdHucTrrHxsjTltqFJh0f7a-xg4ZOEJAtP5_SH4UuNrF5-Py9QPu9f36-C0bAmmeHppu-unocIE4Jv590OjQK95k00ho8HrRKSQWlLXLrN0pwGnLQVaPH5Ijibu0tIh_UBReRQcXn3l_3V2gEnnmaIZn7Ogm588iBp-g9UBu9ZBiKTRK33xTNKcVyYbSjEIZrIz4JOz6nCsU6gbB0_W6rIFbf_vh0yljk1RWFpZVf-GfhrkdGxfAgi3sivWH8cI7XPFXukYZC82kpkPyDQZ8XQTnW1oWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=j5xcIltAidjp56eyE4nccj-Lxct1lG3m4TYsnLdD_FLJgS1CQALDKfaGHdHucTrrHxsjTltqFJh0f7a-xg4ZOEJAtP5_SH4UuNrF5-Py9QPu9f36-C0bAmmeHppu-unocIE4Jv590OjQK95k00ho8HrRKSQWlLXLrN0pwGnLQVaPH5Ijibu0tIh_UBReRQcXn3l_3V2gEnnmaIZn7Ogm588iBp-g9UBu9ZBiKTRK33xTNKcVyYbSjEIZrIz4JOz6nCsU6gbB0_W6rIFbf_vh0yljk1RWFpZVf-GfhrkdGxfAgi3sivWH8cI7XPFXukYZC82kpkPyDQZ8XQTnW1oWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29127" target="_blank">📅 21:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJKMq5MBB8Oo6-xtiCmEEh88TtZvZGFESZ4Fgtpz2IhXMNxwWXnZu3e-XnPIMRfN5pwWlYxtH283bMgo3RYmnjNx8xG267N1XEVuh3PyCDaNhUloEkaO6iQPNiZRk6JsXhw4_RkQpVpl939Sp5LrTDuBnLwvS4qlAcp9KvYzksW-fRQS1WdwLgm_ELaAcVNq3iPg384QlDRGCIkVl12gw8JPXY16viIG7HMGeD7ZNZszWMNOw2XRpq8vA70Fvn01jP5jxOfaBuY21X8shoYhY1sSJ5ksqRvh6A4E0higQpJc7MGj6CeizafHQAj7otILvPGROLs7c1gds5ThrHaB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29126" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoB1OqMz16KKwAmY1fRYX5FAtsHYpHZFDTa99AOPMdZF524bEGFDrahTfwOtThuFDTs-_7wcvxj-zu2mas6FtP-SQJ8TdZZRow9VwlOGEJhiw9TQ3vRRggHByz6KjvFkXQwWXGnA2z1r3srRGoPelkS-X3NtHMFRndcBnifsRdkorQIBCWaq-NwlxQgje8M5T0IWIUMW1AY3Nbcnp22UQRoGjCrO7rEK7CK9lX23GGifafoUYafWIH8OpszAlefu5eg0sTVR5u7aTxmMU9633aKawHVPiDaW1QZIZjq84uow_i88P0eV6TvsinkrthO3zNXNwJHMH-T9XjPkXlRsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیغام‌سهراب‌بختیاری‌زاده به بازیکنان استقلال با خط‌زدن صالح حردانی در بازی با آلومینیوم: کاپیتان تیم هم باشید اما نظم و انضباط تیمی نداشته باشید جایی در تیم استقلال نخواهید داشت. از هیچ نامی نمیترسم و به راحتی کنارتون خواهم گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29125" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29124">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZPt2mIiOiii9SfGn1V0cDAx2kFk0n0iZkuOo7W0rWBsfpklfR7YsgXF1tJnxOEz6sWULSl1OkFE6t7tUvfsQ03keJ6kxQFDIf18bjTQsRZgw_mQrhnsRLv1FEDvwTRZljHbu7rh43B7tsLTbgcY8nLxOWSZ7YrYENWkPeZDfHd0gCSgT-TGJ7rnhhlS38u6RAI_Xh5nCkZE2KlfLjzOh9orA5MLIB33gIerl9e5wUbrpzgaC_JbZgjM-0hACbNSqqAv7_0v8saEtiR2i3-h-HF3lvwTUAe8LKYHBtCcaMf2KabsQeTrUzZ5r8gnS6XeysMN404xoQ_R3S7TIlsJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ اعتراض شدید بازیکنان گل گهر به تصمیم جنجالی داوربازی‌امروز با تراکتور؛ در حالیکه بازیکنان گل‌ گهر برای ضربه کرنر در محوطه جریمه تیم‌تراکتور بودند داورکرنر را به ضربه دروازه تغییر داد و بیرانوند سریعا حسین‌زاده را تک به تک کرد. بیرانوند در حالی مسابقه…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29124" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29123">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=dpJW6g5Rjux4UW_z44MDQq6mscylka6YnuGCfvj6GTtMks-M1eXzow-IAProOsFsBveI6N85XKsJwBIo0RJz1DYCFlf_HrqagfuwLRI_KKdgRXPKBHHgu23bQOdhkpeieH4DdhuSDAGP-EmtyVLN3EMuGLhcqsPFYAEhg95ViXs0Obgh19tWZaSOQyPXiCJmKARdwHnEEuSgKEKhxtF_H4zjq597eynS6DrH-Cz01m-yYOnzHPPvobzyslhujvZ4efSz6vf3Ayfl5Rb7aPqW1r2DsyEcoCCZshNXHaDklI6LQfCaDlqyoOqcwZKQraeFGZjDbXxG78uOIf-vSWt5-pFON0zaRFv64E8Q8tAEtJEqBhWkl_pLqe_CzIDLNdI8bq1I4qBddNCt4GeUPIgVTG-8JuCTcukdoiuW7zdTHPDK2P0xIEJnASWHC5Hme5PJk1y0T9tSEjbp0zRfJGYVfR10hDT0WInQ6OmdGbq5V1AV1V-BI9Csm_GOl0jvtWy4f3oOFpkCJmjoYBOg9GV1w0d1Fg3r1kW9C33R_rVxdiH4o3nec0eHrP5c4djk8jBGignSI9unRSyNNGsWMO6lUGXKZxy7JCAkAPNwbxJ2H_IaFIqHHSMX_YFM94zkstSX_7GqfYRDJQeyFdz2gWpNwJCIqBOyq8cPt6yu0cug2mI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=dpJW6g5Rjux4UW_z44MDQq6mscylka6YnuGCfvj6GTtMks-M1eXzow-IAProOsFsBveI6N85XKsJwBIo0RJz1DYCFlf_HrqagfuwLRI_KKdgRXPKBHHgu23bQOdhkpeieH4DdhuSDAGP-EmtyVLN3EMuGLhcqsPFYAEhg95ViXs0Obgh19tWZaSOQyPXiCJmKARdwHnEEuSgKEKhxtF_H4zjq597eynS6DrH-Cz01m-yYOnzHPPvobzyslhujvZ4efSz6vf3Ayfl5Rb7aPqW1r2DsyEcoCCZshNXHaDklI6LQfCaDlqyoOqcwZKQraeFGZjDbXxG78uOIf-vSWt5-pFON0zaRFv64E8Q8tAEtJEqBhWkl_pLqe_CzIDLNdI8bq1I4qBddNCt4GeUPIgVTG-8JuCTcukdoiuW7zdTHPDK2P0xIEJnASWHC5Hme5PJk1y0T9tSEjbp0zRfJGYVfR10hDT0WInQ6OmdGbq5V1AV1V-BI9Csm_GOl0jvtWy4f3oOFpkCJmjoYBOg9GV1w0d1Fg3r1kW9C33R_rVxdiH4o3nec0eHrP5c4djk8jBGignSI9unRSyNNGsWMO6lUGXKZxy7JCAkAPNwbxJ2H_IaFIqHHSMX_YFM94zkstSX_7GqfYRDJQeyFdz2gWpNwJCIqBOyq8cPt6yu0cug2mI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
چهارمین گل حسین‌زاده؛ گل اول تراکتور به گل‌گهر توسط امیرحسین حسین زاده در دقیقه 43
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29123" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29122">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3u7zN2tjDQzp1DPz_FKwiaMetFl-LS4p149dHZL4DASuVc7Kw4-bc8jYZvIfW9kepv0Ym8S-gVvN2uxtniTBYlClUe-zR7-X58QUWhcijoZjddXROdgOpVTPxBgqOrrAARKL4oQvbNUw9Eqf29qKGTi0TgOOcT05CgJYw8r9ByAf5ducG7OG9zYi301KtdMb1g2flvqOi01UvyR41VwtjPCqeCe4BdETW6PMvAH7qU9vkplZH5nJt4HGW6CqW0V8YmZllDvkgbPXHIMb1VeJrygTNwvbOxuTPalD8OcPKlBqNlM3c7T9qhBw_ynod5PTQdUUlJorC2a9KLgS-Bwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29122" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfokdBVAU6grW5pAAh0wsu8bKTJFn3S-oswTJbJESxCIpWHim0HVdZPEApj6yX5DQoXS-dA4g0wCyVQ3Nzzmm5qBqJ0jsAwCs1yM9wJZxTliTlasQKxLbAu8l2iNu6rXxzs8n_xRnqOJ_DHY7mb4gyhyWnJhOduB5DR-0MNNVEAr9xwaUcKidsMcSXLCP3Fba9azOksZwWwJdMkhtlFwcyCoEuXU3xKtnf6RlGq96nS8unQ4r1ZPC6JQZPrjI_xvYP2-6MYYsblrtHqLNodqhyMNqN0wt5YiqNTUwkpvwP4IOVxXKLNPxOgFBJ4u-13KU8f9JkivZ2iT7O5fEfdhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
هفته پنجم لیگ عربستان
🇸🇦
الاتحاد
🆚
النصر
🇸🇦
⏰
ساعت ۲۱:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29121" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fedqSG8yGwum-Y49iHJDlOoaGV5azJym7WmEyOIdXKajHhejboNYG2MqJWDo217QndVGS_QA2dQMwz6BZgJtV25oOlVeRWvknFmG4IELFVhX7RzL--22tj-5z_uqPZSY-X6jfFKqgeTwMvYhyn9yvWKuh3uC2qXvsVy7B0mDMPCSR5qrPIncPazQbI99YnhLSI5aRXRf11atY7rUQ01y34vpbNaPvxt2FAfduKtN7WPhmc2MZh-km4nO8-nFwtGVoDK-Aiwu06BXGgSNMYMQGhwwTXxir_p6ZER8arzTNYuQgAyeQJrQbMrD3xiWwboNrZQnO0LD1DX_heOSXiJMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDzUGwconhZO35XvDTlMzraXzb--yicwbjvby9SElzQCBxtqO7LZeQlngwZYdDt3pgAq28MAxbZo5bqlBdtZR9SaKPwCkHpkX--e9toJsAfDkAXD2w4273ZPqahxf6pH2CMLuF-4mrWVH2Wzp0ASknyYOhishjdsrMymEEXFTl5phR7-J6GFunQw5JfxwNMwZkfhiv6FpZnHHuGaoRgFu1hNo5vHUBfKuKZX-AESZO14Xtj_rKcZgmr9gsfQODIkOsD3gBnIQXZfXImo2kFf_P1-MV03Fm1YyLePnaa3pOljBBLopcOFOFVksHAvyojGQQ-VRoSIckp4_Pqmd7fxxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
خبرنگار باشگاه گالاتاسرای ترکیه هستن که میگن امسال گالا قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29119" target="_blank">📅 19:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DARHFybZGpY54D9fP342nFE-N5G8jM_SXz7oXq7BnNPRfOkjldt-TlZvdY9dTpYexrH8F5PftGWQofDZCqH8rki7PGFmk0bQnNE71i8N2Enx9nYT2dme6PbvjAbits8wrre3lu1X4vMQe6dIFm_qzRLNOfyU-HPmZEF3-c2d3v6cLQAO7O1QnrvNtBPKRfGKzQUYUbjuoAH5ISK2fqFhT5Adhmli5wFAapBgqnKWkYwWG7ZCHbL3hazG_dBQs3pS2NE6p7RsAR8ywzbDm0tx8R36tuO57XwBcRifo6cRVtatMDFdDAprpKpWD8Op_OoxhhVG4ja7rJKmuzUHCCbWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب کهکشانی و پرستاره بورسیا دورتموند اگه در سال های اخیر‌ ستاره هاش رو نمیفروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29118" target="_blank">📅 19:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=QA2-oUbJOg4C-FIiRJTWYA5m7F6ZZMIhv7ordwXYEGXDbjMUJ3m5fYWdd9t6erDfQOE4boMH05PejmyJ6p-C4FiC73Vh7wb1DmR0PuSG8kaeKvXaHfpZPDzkj6sZFHFEGoBEkEZjJbPOO_Y6xoF0S7IaTy2v84cXR3MxBct4zTOwGwSxKTKDHglXJCu1CbHg6Rg2RDiio5Xcds8zqDMQSpHxvHFE8j7DgqD62qnwf6H7JRKOyyyKb3aYspPN87K2NIsWiT3Jp-hztJHVu-x-lYCar7ZgZpCZDi-HmhzDLLigdrmM6alvmuijhvR7U1cxkXZAjkmiVDjtfY5NSJmcMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=QA2-oUbJOg4C-FIiRJTWYA5m7F6ZZMIhv7ordwXYEGXDbjMUJ3m5fYWdd9t6erDfQOE4boMH05PejmyJ6p-C4FiC73Vh7wb1DmR0PuSG8kaeKvXaHfpZPDzkj6sZFHFEGoBEkEZjJbPOO_Y6xoF0S7IaTy2v84cXR3MxBct4zTOwGwSxKTKDHglXJCu1CbHg6Rg2RDiio5Xcds8zqDMQSpHxvHFE8j7DgqD62qnwf6H7JRKOyyyKb3aYspPN87K2NIsWiT3Jp-hztJHVu-x-lYCar7ZgZpCZDi-HmhzDLLigdrmM6alvmuijhvR7U1cxkXZAjkmiVDjtfY5NSJmcMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
برترین‌های لیگ برتر پیش از شروع هفته ششم رقابت های لیگ برتر؛ حسین زاده، بابایی و بیرانوند بهترین گلزن پاسور و گلر در این فصل لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29117" target="_blank">📅 19:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29116">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoiWKp42l_CwiIC1V5Zk4HqLTygiXmn53DMrR6JtKF4CCCsDbinEXnUJYqsqnyzP90S8ImW58DvKUWIVr0uD6WLF5wXqRSgZMYbt5poNwb1yzWM13xGqBsXsHFSdaYviv8gxBtR4e9kkvBaks0_VLGipmby8G2oH4CjplSWnGoX_QSDSdjjO3XAIUj7BpOeuTmS4hfTe2Sl4ikcHeOli7RTJjhsmEhDng30YTtyjFpg6D-MZ2LoX8IHJsj3LeJDMhIFLG4guCl0HDqpW2Ufm_1CNO1PTL58wVOhjYjNPIf-ambFKgfCgb-WGXLuOgtFFAKmDIcxqzz3hblurcVLz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29116" target="_blank">📅 18:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29115">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-j7ycENhCGR9LX0oLrNVLpPEUBwAHyhPsgqvdjD_dZWY3XvRQWH2M2rpBpE4SsQe-1nnWwIvsfZPkd5H1wN-4NNy3UjCuy5v2k4sBPH2-Vq0zKjhJ0BZcezHqNJsHhmYYRI8RPnou4nnbAKUn5G99xHtBtCm4pCwH8bNy2mCMng_MODrIHfCc7topb4rSHsMXm9DeB93JUCn_9xQ3QCf9WwQWHmYUAI-Q2pZfh-Y5axrCFTVzMRTQ2ntkw9dDCZTxYUDffivCzkHVBewSkJ-lccDhjgW6WKNVrcIgc_drKkq8zH7vjRQWmijoTXsRQY_710j_V0u594H6hHvYEtIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا: هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29115" target="_blank">📅 18:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29114">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=fhxpKIcT1BN-QDMExbkJGLL9OeotVhjUQlpQ50OCiJ8XvT-VJ8bin3J57ihWP-ea2LmluD1puHT36aUZLfmdOp2P7FvJ9LEjsJmnxCfQWIPuFk0gKh4ek4ObK-jjmHOc0pqjziQo7fnmd2f1tRdSQywi_wMoQpqmQVZ4XvGkXLLNahCyKKxxKnLPdL-9SMC0BTs87m0dozZ3EpRupLlnhgOngHge4CGK022EhmLHa1ZGvy34CdVYgpEXiDDLrq3l4dYHge_rhsk_KEB5D-kFeLpvjzVZfyv208mV8MixDh1qWstrFnzz2vOjGJv0J5vlYOAL-GPWRVM3FLXiyQUJNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=fhxpKIcT1BN-QDMExbkJGLL9OeotVhjUQlpQ50OCiJ8XvT-VJ8bin3J57ihWP-ea2LmluD1puHT36aUZLfmdOp2P7FvJ9LEjsJmnxCfQWIPuFk0gKh4ek4ObK-jjmHOc0pqjziQo7fnmd2f1tRdSQywi_wMoQpqmQVZ4XvGkXLLNahCyKKxxKnLPdL-9SMC0BTs87m0dozZ3EpRupLlnhgOngHge4CGK022EhmLHa1ZGvy34CdVYgpEXiDDLrq3l4dYHge_rhsk_KEB5D-kFeLpvjzVZfyv208mV8MixDh1qWstrFnzz2vOjGJv0J5vlYOAL-GPWRVM3FLXiyQUJNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزی‌های‌عجیب و غریب وینیسیوس و امباپه در بازی شب گذشته مقابل بتیس که منجر به اولین باخت کهکشانی‌ها درفصل‌جدید شد باعث شد دل هواداران رئال برای یه بازیکن بشدت تنگ شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29114" target="_blank">📅 17:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29113">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af7cW4kx53kIb6dj3OIdEZrnej4jpot2jILifG0iw9a__qox0pwnskpuI_2k8Ya2kSBJVAtcIOwBZQY_ejf-6HpLSZcumSbxQZNF_bMjbteQ4KUdWgPg5ac3mFjDr9__MH3JH4RFEto_oq-GOzgWByL7LLq2t-YBpOSP24Rh4gUS_xflCMEYil7FSqfT6niTFmkjPh3xtQ5M2atdRa9gGIHeZBXeSga3y39096KWUHyX2K6K1a1nxkmdFeACugdm-HgZgjOUen-krdBhUBVC830LTcW1JFCgTGLs2d82u_z1pbBBHYg9P009ynPFu66gkqDj8eIVzW5u_VzUSxA35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه‌آلومینیوم‌قرارداد مهدی مهدوی مدافع راست 20 ساله این‌تیم روچهارساله تمدید کرد. هدف باشگاه اراکی درامد زایی از این بازیکن در نیم فصله. رقم فروش این بازیکن 450 هزار دلار تعیین شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29113" target="_blank">📅 17:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29111">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=r-zn_AKsEuaHfnkxtFwd6bnqIprXX3LH8nye5BIwjEyGNS3awZ0vvrF-BQHwf2sge0tgN1oM_al5UouP77QXcHhsiAdDeCykfbNlfh9wWBBPNtARKiqWiEMZKI8crUdBFVHaYMjLzQpRBRiq-8muS2Uqz_V1eollTPrdgh9nMLF0z8i6QIANGQmceyY58XE9QzYCshkGckvd7noPDuR3FQ5AuJ7gyh9M_SXekliK1FJ-U-lqGHuaXRfe8FbvBDPdw8qAX6-0Wa9yN5n3o2A-JINTj4O6RE56BRPESXNdOzoUzAfmRLp-dYM2VUPHZR3cNdCG6nPU6cmrOm0cAjRJnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=r-zn_AKsEuaHfnkxtFwd6bnqIprXX3LH8nye5BIwjEyGNS3awZ0vvrF-BQHwf2sge0tgN1oM_al5UouP77QXcHhsiAdDeCykfbNlfh9wWBBPNtARKiqWiEMZKI8crUdBFVHaYMjLzQpRBRiq-8muS2Uqz_V1eollTPrdgh9nMLF0z8i6QIANGQmceyY58XE9QzYCshkGckvd7noPDuR3FQ5AuJ7gyh9M_SXekliK1FJ-U-lqGHuaXRfe8FbvBDPdw8qAX6-0Wa9yN5n3o2A-JINTj4O6RE56BRPESXNdOzoUzAfmRLp-dYM2VUPHZR3cNdCG6nPU6cmrOm0cAjRJnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خنده‌های‌تلخ‌ومعنادار ایسکو کاپیتان تیم رئال بتیس پیش از دیدار شب گذشته با تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29111" target="_blank">📅 17:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29110">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-CBrMhhrhuSuk9cq7IWqqTmCXVJKMRhClKjDRWl0zfvAw1BjTrIqkaWGlkJ8niaJHZdwwBJScSthA35MefR3ZAo2LyygBlfDFIZQgvLfakg_q5KNbLDZCVK5zGTaNEAz4XIb-tLegGTcL2xrIemXrKc01sKbCJyqUvBwuqYOlh11ZoDuJoygbZF1DKfGazRuhZ8zgtjogGnbrQ_Il_-fLDEb_KrSeS-REejDkwRXSR3JC6e8pCMynjd_2yXttpxR8fQFYPCnm70wD2OgBU7DHypTvA7rrAkhW7zDGMQRChKtUXetzckLOgvRkU-Y6isy6dbEGe0wvYtDk1_spqZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت؛ درپایان‌دیدارهای هفته‌ پنجم تنها تیم تراکتورِ جوادنکونامه که‌موفق به‌ثبت پنج کلین شیت متوالی شده و هیچ‌تیمی‌دروازه این تیم روباز نکرده.
‼️
همچنین تیم‌ های استقلال، تراکتور، آلومینیوم و فجر تیم‌هایی هستند که شکستی متحمل نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29110" target="_blank">📅 17:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29109">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7G6W66oxu8vUQIYWg-tHUEOZlb5GNw0hmTPkty4wg7-QGzzY4SxKQ67VnyDOi4a-oxJVJ0CbiIDrq8N5dSsSr4u_IFmj1JuzdOoVfMg5R3NmzAm_nUXMNUoA4YTigz8u-bB_erjQwM0GXqan1c4-2t7iHOb1_jYANV7ip8zYQjJy1Gky2I092lpNMNdkGVzW3wnrIdjn-x1LgM1hOs6rHM2inkvjeHY_9dZSOprUQekZ0S9amVh__D5rNRR_Z9ePgXcReB6aC2-CGoq3ctKOEdbrElDbxyE_TASspsh1LZ-f6jLQHPetrrIyp_q6GyHjOuOIR0FxzKgkvej5gS0wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد خلیفه گلر قرضی آلومینیوم اراک علی رغم تلاشی که کرد دروازه‌اش مقابل شمس‌آذر باز شد و در واقع گل بخودی بنام محمد خلیفه ثبت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29109" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29108">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5QAlBrHEQkXkxkkLtr4haHvsFFHHXaH-WXupaNXyU_9vL_jTj8eGeOVwiD_53AOR7rj6JJEaH3X2um2vbgPSluc2Y8xHY_OvdUUtmSl30cRx4iM9BzzkyeJtPNEngqO400g60yCCFauaRxCizciqyRwp8iUlGibi--dKkov4bj8CwAUv2bMAlULU2o4MvUJlGZ8lj9F90feWyygvJK6YzrRMozke4JKjFt1wJx5tm6q5Nz0TVXY-FqoJ8GvbZdbyuMDJBquNT05ivSD3oIgKfeVHXAhmlXg_5dgdIv978C0LQ66mulv9Mdn4xyE_fKAWNQQFZe_8VDK86yBTi9png.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ عارف آقاسی مدافع میانی استقلال مشکلی برای دیدار با آلومینیوم اراک نداره و فردا برای آبی‌ها به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29108" target="_blank">📅 16:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29107">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUA5t9jXJJUly3j69UEeeXYQd5oGhMgat3dr78NPPt7XSRhVzzcG7koJLRP-b3_ASnhT6y8AYiMY_MpG44hI8vnwQEmFWqw6VhBMSTMpk4yMmyC5wkNxUqpIIt9cFkv5NARbfYoqcb_hzMQBk5C8qwBx0lpPdOET-yvbvx426ToMIJQP1fjulMAVVDbyjwMs6FO_0aCgjBdHR0MipnaUeGLIj1wu0_EnzGEb1YEUFomDdu3DgQsoAU0Si0_LSPfVqToJkYScj0fqxLrCmFSt5NND4sBEcrAYVNx3_x0roT8DuhA-xltdoFrbJFHggE0ZKxKqlm3RIWYRGDskxTS6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه DAZN ایتالیا که گفته اون اوایلی که بعنوان خبرنگار مشغول به کار شده ماریو بالوتلی مهاجم ایتالیایی سابق میلان بهش پیشنهاد رابطه جنسی بامبلغ‌بالا داده که او رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29107" target="_blank">📅 16:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29106">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=V7Waa8OLfUNOFDGaqRf3cT7BhSfpPGqgtyhWian1bksnVu0XkeKi9pfftuMQWzzg4BmI1hg8EOHHXfJuwNVrUs_nt4cQjmZ140hoswrp35X-A-loP2nhZYEPCKjQ2qOnFPiYHCuVNJQfIqAByS02haWiKTZbOqavVgfv9V3Ke2WBbulVCSefSLpw_KJ1lb_wYlsQwoAITRaRTXBQtXycv88KlF-HZcd-OZhAhs75pGW6zvjNPdxPq_MGvw0jGY4fFsRmh2fQ5rhVVE5EldVpzpw5-JwUw4AV-ET2k1gj4QRXDZ8r2UETnYyGlQ65gfz2j-4mj20JOrhGInf4c9IUnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=V7Waa8OLfUNOFDGaqRf3cT7BhSfpPGqgtyhWian1bksnVu0XkeKi9pfftuMQWzzg4BmI1hg8EOHHXfJuwNVrUs_nt4cQjmZ140hoswrp35X-A-loP2nhZYEPCKjQ2qOnFPiYHCuVNJQfIqAByS02haWiKTZbOqavVgfv9V3Ke2WBbulVCSefSLpw_KJ1lb_wYlsQwoAITRaRTXBQtXycv88KlF-HZcd-OZhAhs75pGW6zvjNPdxPq_MGvw0jGY4fFsRmh2fQ5rhVVE5EldVpzpw5-JwUw4AV-ET2k1gj4QRXDZ8r2UETnYyGlQ65gfz2j-4mj20JOrhGInf4c9IUnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوگبا:
فوتبال‌خیلی‌قشنگه ولی‌خب نامرده. ممکنه امروز عاشقت‌باشن ولی‌فرداکلاً فراموشت کنن. امروز میتونی یه‌کارخفن بکنی، فرداش دیگه هیچی نیستی. من دیگه‌تمومم‌میفهمی؟مُردم. پوگبادیگه وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29106" target="_blank">📅 16:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29105">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE8l8WGmdu-xIOMtEcYV9HfiWsbZT4BGpwVNFZQOTHC5b-VaHRWpCxodksvPkOk1JVULXNxcz4Qn1fDVtC57bkAQENMvHa7rI-3s9HEmkXyx79Io67aGMTkqlQ5u3I2nWMmOJYjCuTiq7QQOn07VMUpze91SO3QhfaUKFdVeIy_DEfwAh-F3VWRLrAS676dnB1g0x6BixqrXLlOB9YMkJkajl8YNJvSXmWZt6v6jifhmfrWeyzYPfTadOCGgKsQ4oqUkyBfhB8CHt647wPC1ae0l7siADp3f5PX_KUQv-Tm0k82SMUPx4JnQTE5MjqjxktJasLr2phf11vt7OgHxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌ ادعای‌ خبرنگار ازبکستانی؛ طبق پیگیری‌های پرشیانا از ایجنت خواجه اکبر علیجانوف انتقال او به پرسپولیس منتفی‌نشده است ولی باشگاه پرسپولیس باید همانطوری که با رقم مدنظر سرگیف موافقت کرد با رقم علیجانوف نیز موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29105" target="_blank">📅 16:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29104">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk4XPpUom7j2nF7cFMVhB9gBVeMZmWagiG8rw4pGjpjR-LzH91tQoNwDIRb2VaxIXt6yL3cM6rigHlJ9qsezLUqC5NLVf7OwUDIrf79erx45le3Kbqw7HnfbzuTcY8Si4x8ytUZt38X2McKuEWh8HEGu55MY2e8p6ShAtjHqAuSaAVgbnuDHoBOABz1Kf7MR52D_-IqT4gYnQ-mIMxtjPAlwj90Ql8jMv1vI03KMzqoAwTDfe6bqdivg0SFPUqduwSUTSRB2RNg6aB3o0COyOnz5Igf9a85AP4oTClz2l83agSP9nVquV5c-lBa2GH0XcVmHgBthTYv_FCqQ_7xEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آنتونلا همسرلیونل‌مسی:ممکنه درپایان فصل لیگ ‌MLS؛ لئو مسی تصمیمی بگیره که همه رو شوکه کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29104" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29103">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pApxLtYPms89kS0Os5YKmoh59pCqKJDypNwxLPV2IAV_oKxZV1I5OppWCIuvA3FWX2SxnNl1T-UoMBnshC0htKo2_xxsi_VXNQ_U8B1AZy0FZhmut6jw4mKc6RtatpJr8aHxYEjRryEiF-wiRO7Q615PJ9yC8szw5yAJ_ghfsKNcx3DO_nA5V7bABrfnM95be4jnepExxut8YtTsE2mJHKUGVLm0fZD3BjdiBoqOsDHxVy1fwtDtGoeql7wC2rnPF_4wHA-37LTxDz0oWhAnyPCvOOz1V2Gwa6liO5S9L3MHXisTptDjZpvpITb-nZ_GnWGyeX4PG89cI9JvUvcynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادر محمدی باز هم روی پرتاب‌ هایش پاس گل ساخت؛ هرچقدر تو لیگ ایران قدر این پرتاب‌هاش رو نمیدونستن و مسخره اش میکردند تو لیگ روسیه هر هفته داره پاس گل میده. چقدر هم خوب انداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29103" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29102">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoW2G_0lazk1NhDNC4HpXKGf92w9IwWNAa9YQ6ftUeodbBxcifRg6q73LVkWo-depRBBOUwP5gc2Ykk26mcGnrv_EFNb2NbxVuQilKQMF0z3aFpMSX5kcRKwMD2Dv-Y_4oUDIV3dVbwC_LIj8m9EQPp9JGrkrk_BHGaMU7oQx5Etw1rPaNFqzTeWaKYvu_Fr3iSZ6SZpH6GAOrF8UNzo9OGLXpvLyuivA_9wIwDpQPAN-sQkXZehZqDe0txqLvZ8zSAYwyES61R9Ku-nB2muSSNk9uKwpqWW9bK1GwoAv31iZXykPbrQfnxy8b9cQe5ITiZgolapGlB5BBiV9FziSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🔴
تراکتور
🆚
گل گهر
⚪️
⏰
ساعت ۱۸:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29102" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29101">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWRuDeK_pFcH69dAEgJNZwRVaQvl0qwcd6xB-fQYMO6k0MxUE6cUlYSXuBY7TvRAyyZK4-_t0mWZWqrE6MKVDk0mcxt7DeN1nD8RnTTGoPo_axcLQp4NBYCGog2errcJNnboh4lO9fN9Zcd2s5DP6OgZnrz3Cnuy8-7W8hvy7fyKfy8rVgRz2oxRztn87hAnKI37i1QVfbiMDL_DTwEHegr16HYVFUkZrz1SQ-jeuyRdK4XrB0x2-ziGl0HM6ltZ4MEv4b_KolvywUijYm_oFAJe4IiEHDKTnUrDSZu0St-yOc5rcByq82LRIhQjIRNifee6jxCBCKZaOqSTuMCt4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29101" target="_blank">📅 14:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29100">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNcfOIQWOJyAHrGSDERpeqasEFiTX9rHBVaYnBVZPKBA-Pw2Q9zfMuC30a7KcCdphdykLhYfcGXwXVgZePZ0aS5rKwLUZYO30czjzS4cUfgLmSzyRB8Qo68Bv_pdZXCd26r2DFIRtPOPB5ZMFhbRZ9xmXWqLCNDMzleIb7Au7vlZls1xzKdkv2_HZeP-QWbW0R4GdOgbeODXPL_kvpLDJzj4lRBjm9nckHs_aNTTtNMidhPOZ0IXDHtvsN0hWqC40enPJXX9cnWWUtrghDykjrCoGYMGrxz3a0opRrcNwIDMk08m_MZf3kAAHk-yv3CpC7MKe78mzzv0sbnhmEYstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29100" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29098">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuFaQlz5CsAFRfpin_jVGEWIs3sNVk_TdLHFVyZ7yksadaEgP0vPypa7WaUHJu743nYmE_BxOK_75-zv_HhgIRkKB8NZAI5iPdBdGooUc4AQ46LHi6oWdd7jwzPz9SgneUYBNctIckmdPDdPs5XPZsgsg7tQ55VU2bYdOBIZg3OwqnimjSm2xm8Pvzta9rTqMpLR7oNwsJFkFBzSartSnFSnpuRoKWSpVLUON4st1aJKGuFg8-R6e6-8DY_JX5qrFbfSTxFLfSGF1H6ELk7-t4mkgpHIROd-ZfNxdTBgPGAjP9socVxy0LuhJdmqdixjmRU1UazaXIxB8m7SIHylZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29098" target="_blank">📅 13:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLINNfh-JPgZL2P2Pta6YVJBfm7kiQW0Lq9Ihn6MfkJFZqD_WUF8Cp7fF4ci3Ojs_Rb33qVC_DhnmWvuN7gh3yVD7xEDYudLXlWQXrDMcvDavNDfdZDxWI65XN3p_cVGHlVkUzMYuz0wueXeL248mvVtv7RjEjo5W7rmWDv3puMEoCy7P47FFFxQ4zwfyUJY1VwxWXOMvRLWJx6JBcjOQp_H9E-pT5M34qHRaXlp6Khn5q5bAeK6Lx0E7dLc87gxmAdskxOSpOXZ8o3_cPagualdfyVNL3_gSlqiqAo1iHa-4uM-lz2FlPIPYAo1QOuf9BwpWlvMWgFgOiapv0-Rlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwKsb5v_nADl66gCoW81A_da-r2IvCx9tQMFW4zwxnDZQ-sEYEfS05j4iIv8xd5Np9F1FTv1nRwoPFzWpQ16Riqmfi50tttkQNU_n3Y9RMWlfbY-qQrgLVLbDrEfY8XPb9BEJF8rNoP95PQbDIKBwJPLsgmfx9NIrN1ed0RafaVCc94VHio52XoG0NqbiJUIIdGQ09xBu96MzndwQkbt64AWRvyMP8YNGAnYBAluCzib3ViiH2ODMQuh4SXjkm9KvhVUpomqAnL_TiJ21MlN3-0d0qSMYxlm0WuHSeYEoWU4aJL6THaKb0rK5vBW-g-gOIocEjAIImitNrl4c3F2QQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوترکیب‌متفاوت از تیم منتخب هفته پنجم لیگ برتر بر اساس نمرات سایت متریکا و سایر رسانه‌ها. بازیای‌هفته‌پنجم امروز شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29096" target="_blank">📅 13:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLMrf5QpURftYqX7Zdcb1V69D9906tsfYo5ctUL4HlIcw43u7twdbY0jQiu88GysCfyANBvcgfwt1Ds-tvfsOOs2PnDY69HVgVwYphTQXlOGh8nsrQCbvN6Cf5U7crQwpqlkWnXmatf82WK4Anu1Kj19460P2JZVIVcvNnmdqbBD86mZgraigUdnUTk34NDikMlHdH9EM3YHqDDhTAq46HqcYkqB9TKvmEP6RGAm9KFf_2lT5aE1LyAKkUb1yDkEi2uHKoOy6NuDQvzyUAzFZf99p215hJ-CE3FDzH5r66MBPtAPwmOmZEvTbxQV28F-bowR3pxi1w_pvGC_eD7khg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول سریال جدید "مرد سه هزار چهره" برای دوستانیکه علاقمند به دیدن این سریالند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/29095" target="_blank">📅 12:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=M0NEh4W3qOfrZyp76TjWEfN6nS--51gNzr2Vbv7WT_-7MPuxvqE1QF_WviRKGzrKwUsYxhS2R-vsDAjFsSxPl_YXNmGZGBM4Hm06jYYPWSmGi0ZRRLCQzk7ppJ_24ppLOf6vBg0fS9Ue_z-zksVehqo7BFlnMciiMDSr1psYl4e4QOkiVa_gN47fiMeEsoiifF14230FteIM1PJSekYhCmyw7vQuTy76bkyiyMCu3CLhJ6aQ2QuRUadpt_WHkpSJfXFmK2RGcWEiSjQ3qRUVG4fOlMI1MaKAykuUu6GiEGI0RqwM_D5xaxoIN8cYTc0dMCi7CziK_y786A_ePjjcCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=M0NEh4W3qOfrZyp76TjWEfN6nS--51gNzr2Vbv7WT_-7MPuxvqE1QF_WviRKGzrKwUsYxhS2R-vsDAjFsSxPl_YXNmGZGBM4Hm06jYYPWSmGi0ZRRLCQzk7ppJ_24ppLOf6vBg0fS9Ue_z-zksVehqo7BFlnMciiMDSr1psYl4e4QOkiVa_gN47fiMeEsoiifF14230FteIM1PJSekYhCmyw7vQuTy76bkyiyMCu3CLhJ6aQ2QuRUadpt_WHkpSJfXFmK2RGcWEiSjQ3qRUVG4fOlMI1MaKAykuUu6GiEGI0RqwM_D5xaxoIN8cYTc0dMCi7CziK_y786A_ePjjcCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
والنتینا با اجرای سه حرکت یک‌ضرب قدرتمند و تماشایی با وزنه ۷۸ کیلوگرمی در رشته وزنه‌برداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/29094" target="_blank">📅 12:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPmHR5IkGHHkAQC63X3zbSuHriWOY3GMzymEFPGAQLGjia7ckJ2-x5DHPmj0h4NG4W4oNEvVB9scTpgcIATfEfqAAqV6WQPEdBVAqGZjx_rdhCatAOwxQ8xXVGrJ1KfbtXTecanf2nXU9U0StQlIKoPsLj9YlmuxEkLDdwIhPSP1kl3FyHhQkPmZNpjsiJYufds3_UCxS9jUdjXdh-qALp76oJHvvIWFCSPfGNlHAyKgaBvXlHEBKjixxmGTOUjFa5Wtbm7JBOJ7pEgwnp8AlTtTs9KR0UG3JFRNfFp6ATo68ya5MIKh1G3emlbDP7z76XxmPSeQ4PSiXE2Va9cVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29093" target="_blank">📅 12:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYpg8BcWSg5NE1IR6ReDDGZ-dcr8HreQAFYt2o8DZ-4ps4DYRavkcAiKGf7AGeinzf8cqWYoOJVDW5rQhMP_DfvkaC5QTe_OjQctzVAdnnShrKiVT5LgY5tLDtUwP0LsEzZlIpRaEFJgalXb5tB_v4cbq40mZIivRy2azB0pD0ky4FsJSnTOb9_ci920AK_cf-umkPv1J7G4ykItROzCuJw-j8kL9EQA7Lst4RFMQ2I1EvwBa3o0F0JTwbj07N64yi3ByIyffaHwKseSI4i8ig_mIx7PV7VgZ8NnHfig2xsX2VvC3EKJbpBmnul1f9vG26J-lZIRP039V1Qd7GfyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/29092" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29091">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-TNwr_lWO_q3IDwXSKY1BlX-nSeeNtGKHTOyON3l0-q2ZQbRx5JrJuWoIJJ8vePrYk78Fml4ROKswhf5gdysvVn0zU7y3e9RZMvwJoX1KMGwojS2cd87G0OBti2jwIzmzzhxhlryJ6y1uV6mfU5NIpfHDYz7PWHv324H40iuACv8EarkhQ3X138a-4NRm417Ybwb2lf9nnfVMlqtkw1iYUX1GGGC41fBRmA_vNzs9_8Ctez_lWEnpFJPjPBPhRBftSGVa2KQZ7K_YBlIHlVjWp0LkV_j43A1SM_lg0KICdgEQLcFxvFuVzXXOj_w977AkAea-saU18Zfyn3Xjk1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ محمدحسین صادقی وینگر پرسپولیس اصرار به جدایی و گرفتن رضایت نامه‌اش از این تیم داره اما مدیریت باشگاه به نماینده او اعلام کرده تنها اجازه جدایی قرضی به او رو خواهیم داد. ظرف 24 ساعت آینده تکلیف صادقی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29091" target="_blank">📅 11:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29090">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29090" target="_blank">📅 11:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29089">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoPJ4nsVdyum_aFfucWoIeEdiXjVDzxw634am4JLK4kQKKp2pJey-mGI_OM10I1wzp8naUIxRxn0E1o--gwl-jaFG-hTd3In1kUUOJxza7JB6rg8e8c7c4S5PE5615MSz2celC1QDt_1edvSOssX6JRpl6cjJcF_f2Yh00Rst9wbbCaok6xvBDg1yVv31o5sjwaxSYQUyUEzIwPKjM042HEDy1fgyiGRHG8Di8nDX9sGGXQWwMlVHWjncIGbxUnL2sQEq75iFf6XY2reIRJZUYcBrbULIzgIfzmSfwWMpROPD2ga039i3vBNegnKgPgRDQ4OlIsAgq6_Kcs_6U_65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/29089" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29088">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=Atd8_la7P_VPQb1g5hiXj_jAsADj_p_JCGC_bse7WV5LzOegFycA8tOcjglrNmv9EZu0nMdxooFBBJiHiv33iwneRGqPTK7rglZAndPj05IG_wySg9lQkInMp5_smJjFim00SSRMiKXaS6XqUGcH0vhupO9L4BJur8wiJCR-K3nALH7IX1gXRGAAK0KylGhOLH3QicA-dIpMJymPyPCrCOId0XRD_tGRxH3crYkDkgxJypW3p6eic7MwVU03W7jPw2U5nDM3G3Ly0W2VInCEps8vBiaokB0zCSkvZqyfNk3HZjKA5EiU8lsF2K0S1KQYNuIe83rTb8Waj0JpTcy6uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=Atd8_la7P_VPQb1g5hiXj_jAsADj_p_JCGC_bse7WV5LzOegFycA8tOcjglrNmv9EZu0nMdxooFBBJiHiv33iwneRGqPTK7rglZAndPj05IG_wySg9lQkInMp5_smJjFim00SSRMiKXaS6XqUGcH0vhupO9L4BJur8wiJCR-K3nALH7IX1gXRGAAK0KylGhOLH3QicA-dIpMJymPyPCrCOId0XRD_tGRxH3crYkDkgxJypW3p6eic7MwVU03W7jPw2U5nDM3G3Ly0W2VInCEps8vBiaokB0zCSkvZqyfNk3HZjKA5EiU8lsF2K0S1KQYNuIe83rTb8Waj0JpTcy6uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/29088" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29086">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW9l8ELN3XoGKjDmVplf_WA23iCwkkaZIuFZEc83vF6aMn03lzLtAFuFKGETlYSl7Ptg5rhBYApfTedCFifswWbwCcGP4UUHn_e5Su6KPfwTNhKibD_-UQBAu-EVuTfEA1JgFYqiH0Q1kXTwwEj-lxVl8d2z1pMimuGZhxaNQN3Cy3eYrved3UJ-ngMq8XKDC9cPB3_E3jdk2TMjudLZV1vltOZqa-hmhF0UoxtwVLjrvvT9MgaY_zVRybWFJfsiFwvzxYmwWXI0bNIpLf_SiivCpDZRF0yNR_pZpIeCTrQ_06c7DMF-TbWVwATmlY_jjelDSK_i8_Dbz8lY-8k-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد رافینیا ستاره برزیلی بارسلونا در این باشگاه وقتی بازوبند کاپیتانی روی بازوش بسته شده: 29 مسابقه، 25 گل زده، 12 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/29086" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwpkMwihm_QySS8JKPYfDte9IL32MliF33_ucoLxqRvc-KGIHf-hXbvovOgHS-zKqZ32s_n5cVHNXK1uE1rtD6SkdR26nZy7CdKYTSiw8-6CLCGyFza-Mkcczg02FJ9wzHkQWVl6cuiNPWvcesb4kCi9KA1aZIYWN5pR-PhNfm_BLvorq5V_YdwBb0SvKXNUcoUJ_vBIMF8LlJf1HSZOqhi3X92v2MBBCKMUQRy5oU5TvazrKGMO1bP4lm8jCH4s0Gqc7FT4PAHuIbBgC1oXY-8WrYjw2DOjYT6rAa5-qWyBnAtR8DqaV4ZnuVkxjYJ6w9eUi9ORAB4aBwnGk3xALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص فرهان‌جعفری هافبک‌تهاجمی 20 ساله ملوان همانطور درروزهای‌اخیرگفتیم هم مدنظر کادر فنی پرسپولیس هم مدنظر کادرفنی استقلال؛ درصورتیکه حسین نژاد رسما قرار دادش رو به استقلال امضا کنه به احتمال فراوان فرهان جعفری راهی پرسپولیس خواهد…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/29085" target="_blank">📅 10:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29084">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeplLeovqsfL9iggF4gn0uOtwFg4JL8l5o0vBY4UieqD-mypVlwRHrU9oed0XyICVDBJNk5ChQYF-IY51DOiy3Nw-Qn2UbJgEbVBsdBE5wFhNkEoGQoBYPLFvlCaY8tXsIAauBgwDQk0bNDEYvcGVBSEEN41n1XolM970bJrGzItMNenyz9yhL7N1gEtfei2O3FprbCAD-p_kE0TkfOi7wF_Ti2lhw6SIS3Lmf3wf8x0FAVoltStw5VPiwy2XO2FgxUXv3h20b8MAwkYIiV1Zr2b65f5JWVlQUGA6h_loVZwOTLwGZPxGIX7sAZs8oHyMHZLXlQtO9ZMG_M7Ub7eAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته ششم لیگ برتر؛
پیام حیدری داوردیدار استقلال‌شد. میثم حیدری هم داور بازی پرسپولیس. بازیایکشنبه و دوشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/29084" target="_blank">📅 10:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29083">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH7934e0rVDon5l4OIXhMstfa_GHUau--Bzo4y_d9j09XZ5xQ9RgWw1MtrvOaMa2DhUGHMapMlFCTuvOgJTj6YJVwK6rUkQy4x0obp1Mxg0boS7Vjg9Ne5emU1bJiR2PfKaQK-jSIrZS_7VwLGpBTCQk3jR7aSQKfznDBlD4ACzfIfHPbqMHGW5qgT_Sj3zjWCm26buivcK_0Fu23DsjxjAkQ_d3l9hhK9pHhbOfxeVwNVVWss4Zh4iiAg_T8ReM1Jq1W2rSRYkCEEXS7a2EHmCQeKMVRweT6gPvij_wFW8xGbc6e_hRDz0QrV_NsNNoN8OSgI0NY0scniROmP9dog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌وزارت‌ارتباطات خبر داد: حتی اگه جنگ بشه هم اینترنتمون‌قراره‌برقرار بمونه و همین که الان اینترنت وصله‌نشون‌میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/persiana_Soccer/29083" target="_blank">📅 01:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29082">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4XxGx1wLsmFjpDVR3vffflwxh12PlgaQjjgDXNX0A-ms9z_XfIdRAI422hJg2xHTGz0q_kKfNS1SJY9cCwPRcPoszsWgnfnLfrj3pnJ3AzV-mpa0dosSBjDYKdUrOjsXRM-XREanfpoVfKaKJZ0Of3d6Ltby-WLxFVI3pkYk9TgOJS60o7sypgCEeF6VjGWddPXK-9oSiyNcJ9HAVqvBRHBeuS6QsxXIw88gxakKTsnWvEM43_LM0N8DgRQGN7pWKyZCeyWqq5PtzKASocm_U73t4TGNQwEDxcGeskJ_c4VSgf1Da-ZHJUZGHjhXF-CXouxiaR4It1wdZXRdTt2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/persiana_Soccer/29082" target="_blank">📅 01:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29081">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmQHNV-pIAnLBdinUeNLYooJd0HDLn8QkmmD45bCK6evDW8SQVO6pyDjcpXs1T9sKn4eup8xcZY2DcWuZSyRp8Itz6DiGYW9oaRezUEaYRX9yRZq3a-fYwWwUKYkhqC9Za8-Ldw0CUlMnFgcGEwPcZ3bO4cJZYmQJw83bl8GKXbuW1i_PVINwbvmXETKcyTuBpusio3GL7FnWE6OhNsHFeLtEZjLEQZJBRBIUdxXjrBiUBVERCHf_hEUGP2PTUioAFEgE1u8E6TR6Zhy6veoGE28J4-Oq1A_Y01_J_eJRwPArB3PZQM9RSi7nx0QV-WvlLNpgSGZeO8SMr-elkhbkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/persiana_Soccer/29081" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29080">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPb5XUQ1dgcqS0uWPPYi-yjRBp_6dAS5HUOaPOUILk37pkdKO5z55l_FQqNB96VhY0oo_lHxWaj-BbCaoT9TJL2htRQqKvbsBam5T7xNvY_AXPOzsCA_JXUt8eqdas4QYN7xdylTzKmeXYKUf8ml_fhf-ssKtqBnMOCZlU0274pxzpmb44qu1Yb5ijloJlvNgwHNHyNzzCH9cHGozvFMet9vaERn7JekQQHKsWlRWSbuIqWQEzxQ-kZlJ4S7G0417S58tms5Mj1FdhjvaZdYPbaNbq3vna3zZNanBA0VZdNXIpspaQF2WjqGSrfPaduNd9QWp6ldSNi_iLvMaATYRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/persiana_Soccer/29080" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29078">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYBIBr523--gpHmJCXIXF34SY5NdtAckO77DEXWSoXxRLc0jsTbB3qw4lzG1vH79jdJUDR5KGs_CWbRX2sZqNRFsupgOioKQAa8GCTCBSaGGzyr7vpHwgvDplyJ4H-KKoB50n4onVQtSG1pTp29RrIQKEUeKeSIpEPsFkiZerk6ksjzufH57M7wVSj_w2q-xB_3psBQNSxynhRnyviQM_8fKRsP_XCXl6QIjWYTRzH7DNOCBENHry6FXqtDxr3VVYtLEELsj6rGDBRtNkO6mwHDg6o-ON573vaKAfB001P6ctyQ2Ruh0odvrd3MVnkKTB7iQTnb2SBDwgMGoWaQhiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/persiana_Soccer/29078" target="_blank">📅 01:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29077">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGrpJMbJrAopqBb0qoHKK7NhfvQ0PRz-29QMh0x5sAhmEjK7KgmvvPXCHStHIUSKgvNaBw0E5ZEdxN-m8uU-c27kCvGUGI9iFfe8sjUOSDVEtsakvwV3rOSDGvuALtmj_nuvY5P4E2wcUPboxKNxsKzIKnmizEDhM80u_j4B3CaND-odFeSSLG5vPGhIrAuf7Jy6pssRL055NrsZGBHaZJyImLBJHE_eN8YKMaVPRqDOIOhHERD_sfzQkeX7WZTvpTyr-2f-EoMC_qfKMGEVFDqQegu-EKl8TsWu2hRszAXFruw6mg80fry1BygxzWQZoWO9NeBwexaRjlb4mLC2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ از جدال مهم سیتیزن‌ها با کاونتری تا دوئل شاگردان نکونام و رحمتی در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/persiana_Soccer/29077" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29076">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhOq4yzsjQz2M3KXEhwDjeCLz8gArqqAIIMSaUGSx1IHPU3AvyR2EjruxYhJ8fiG5CaynQYKcVYZdVpeqEeOAuXNtYT3_OIyA9kxpm7sU-7zWBI5UGTPA2GnuppZHc0D6EDMG8SG3mrq9YQ5yNKEz9YdzytjOvPsoQTHYLnn-4yQzVrEPyABVCJ8nhY0rWwv9t5ewuCuDq9VGnI6hCyYld6z9QKbXkjV6eeMKW_Jh7IfmmvJi2RaXUrPUIz3Fx-KBpd_A_HHTwI70hWNaNugZR0-hOhgvfogxRRca5gVIcANoh5sdHKqCGwX_hfi8u2n4Hi3sSdY2OBYX8hnEOdr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردلک‌لک‌ها با دبل ایساک تا شکست همزمان و عجیب رئال مادرید و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/29076" target="_blank">📅 01:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29074">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faVKn8rP6ml8TdYFaOL6b_Hca5nTqPTErXQIngDOViB8YjWj_pSTClQJ-xTJb1aPqSELAaYxek2fDDKdODAKpHKM7KH2oz0NDkw5M3sbDQ2zDV6g0B4FEjwzi-h1D585TQPjJSUlmzzIskBQ3hgvcmIZjBs11Bkw3Jm12xA37aN_bDXlJcXtjuvqDolCGUPeSnwa5RiPIUncS5AMrDXqPJVV5p0P7cR5t489AwbXUNVJO42sXn8GTtFqtKbgiNhqPGr2E913o2jk3tj1rl53wwKR_2sYGsOZpZVBG3_qgAi9eXqnlFR3_rZHvFDzOwE4y1BaHBNmdo4EFUhkUHKW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/29074" target="_blank">📅 00:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29073">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leEER9Q-Mv-8cW5Yz0KowpA4rlVufA1JrNZ6zjAySOs0xItWMPm78wQH4x4GTGyvH3DFojMtkvtJShUFsfRxM_5kjzVKVr3AJHbkERLAESc9kFmgeffeRUmyZKUtNlqBnRMyVN7tqYFX108iKcnAm1E_QldulVzgXb9fiTK7mW15Tkn7L9szW_D60ewFskHornEgRxCuSbuRV1Lu9uu9VAuIowqKsfkIy8fXOhR51C58V3A8bkpp93W6PvK1xdm9hyxqLxyn_xCvXB7YFQHSymuaqwqABMHWuC0Xu2YYpxi-FA1RRNNwKpvYxuT4hNS6f04fESlXdldjNH47_8J9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29073" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhaQgqihKocEnQ67UoVSJ5k5Y2mM3IucGcx-5HcJxtMcljY02rYD5VAh_nWWxeGQwMlBMsT_GuaKF1vG6A3fzbcThpBFU6E9xZ4XW3Y2RNF18qIZcDGcVeI8wRi7AHJWu_SMY0U4oSkLfeCIXtz68gaxUBR0My9VAFL4MkBCjB6TXm7DXdI18ShpFgeMXQU0DpPPEXAXojQp4m6CMQosCY0WATRUb8-kG7qwgPyhfuv_ES38teT4XzrpKo1WKRnAy1JoonNpzvXkxeFDUeK4dbRkjBDRfdagFa0SdaKIySQsZweF4eeaURY4XvMAfe1uUUlyCLx926fGULI3fYjIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شاگردان آقای خاص بالاخره طلسم شکنی میکنند؟! رئال‌مادرید از آگوست سال 2021 تا به الان نتونسته تو ورزشگاه بنیتو ویامارین، ورزشگاه خانگی رئال‌بتیس این‌تیم رو در رقابت‌های لالیگا شکست بده و امشب هم تو همین ورزشگاه با بتیس بازی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29071" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29070">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtHNijaK0EfokLPj-ARK-TAeZaoOXqoCqIMbh1PSfmn9JiNYmgyoPQXemIsuWTcuLePpvZQfSQMkRqdmQ-DYX6zErDw1-Oupgac-BuQbuoKR4gniBAMl_vH5NKACQeD3hRQge_gS_ZpUyGB1d7NObMGV5CrJUIDyD1AsW9zeQWgvEV5-75vZ_Kq6H0cyq6p1E9rddefIPsVVrrOFl2R8gH9_Pt09ZyDAqL2vmPY9vwaXeM8vnvugdFsqhYb70OmNasXPIgtjF025j9syDpMPKodUZTIQ2NKdqhTCyw4_UmVB_v1l7eYVQaEj8YXJHsmy1hJ-ZhSxARQaoV00bUBpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/29070" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29069">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
سوپرگل‌دیدنی‌عبدالکریم حسن مدافع چپ قطری سابق پرسپولیس در بازی امشب تیمش الشمال مقابل الشحانیه در هفته اول رقابت های لیگ ستارگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/29069" target="_blank">📅 23:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29068">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kagtwuAN1oOLyt9aOISkVQWtl-SuiTWGhLeynMkwB9V-B8Wwngc0MqAoGwp5_nV3QSOFetkJpmUOrDcw7c6WT66yODytlVGW954nmRiCoD5u4_f95WTXePPvIOZDJj1-o0682fJyu1_II3nXFrP7ssYIA5VbJ7rjr2u3wfQvVd6JBxe14cW459z3AlQ35rUQC4aRUYd0RjJKp69q5s0-8IvRy4b7hCLEanN4vn54EG4yG-MrSnEypX79XJ0Kz6ZEmTKen9iTOLHc0ng639mIQfUZjL80nFEGKENOikBSR1w8cTZb7r7zEwUlFcJPPIi_H_JAlNI-M0z8GyixAZupsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پاداشی باورنکردنی برای نمرات خوب؛ یه پدر مادر کرمانی به پسر ۱۸ سالشون قول داده بودن اگه امتحاناش روخردادقبول بشه دوس دختر ۱۷ سالش رو براش میگیرند. ماشالا پسره هم کم کاری نکرده و تاتونسته‌درس‌خونده و همه درسارو با نمره بالا قبول شده و همین چند روزپیش‌رفتن…</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/29068" target="_blank">📅 23:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29067">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb_J5qnRaM3a5_LxpPiVEQKpubcvpe-wE50plIPANDCeB0dYKlclRHwvmgL3OEvP6-_aGEAHfKFpHx4Z25bd6Ql3l50L8PEJTM93PYE8ecBXt-X9LKXJGIFj_n29YX3YYjyYhxSudT7F9K9NsjzZItbGMOdZ1b5oTSRZnO1l5WUhY7H4liDB48x4H8Pc-xIcZGEf2wZZgGxaTr6769oA3FilYZdUKirb0dV-N_tIG56eXe4hxsYypvxw8X5cFqmDr0BU2dkwKK_6f-zq1ubL79o38HERz6KNyg_5onpYgz_uN7FylPTYXQ1-dP2JmH625SMmO89ICtfJY8MKjElavw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
پرافتخارترین باشگاه‌های ایتالیایی از حیث گرفتن انواع اقسام‌جام‌ها؛ یوونتوسی‌ها با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29067" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29066">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCzyrGSUIyryH0CJpxbDfR65Ezh9C52IiGCS59abvl4DagKllBDoxDGWAbeP12Zkd-YKZibXOc2uis98YtMGlrQ99PDfzQAcrs7idFd7R-94J8xfkCnu-8RdLWHa9LoWlwiqU8dkBVdjUoDBNJmVnpMrE2jZepYqMPwzs16oD8VweXc-uGNxkcuGVUKA6pjXCuxc182f0YvUlMlEC2Jll7gsH-ewuP7W508SrY1dmPDiBDxgwL7y5HrzrDurLuhapHAiJ15Gky8CemZj9L2edwh6QjvBkf1GrjRnf8rTupHDBXdRM_dlEbDMH4grB3tAeEkU23UM2hVIFFFLaVY3OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رگی لوشکیا ستاره فصل گذشته تراکتور که با قراردادی دو ساله به این تیم اومده بود بعد از جنگ قراردادش رو فسخ کرد و با عقد قراردادی رسما به الظفره امارات پیوست.  این هافبک آلبانیایی در ۲۵ بازی برای تیم فوتبال تراکتور ۶ گل به ثمر رساند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29066" target="_blank">📅 23:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29065">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DodMPmcm8s7CT7EwFUjcdr_ddpdmNbckEdMr-c9ZmQMT-mW2x0UBOHFuVt5I21HPaHALwmJTuw7F_5TAnUVhbhSkor6fMMnnvmiwN2xFAfKdxKb456_NeijroUJXzEIA8T0Xt_SGiY1U7tEEr01UrkqKd_WuK_Lxeoz_A17zorRdnbxwfJI9Z0_3HU2kVO_8xnByaJtkGMniq78H7ahAug2x5RElbgDo3U-Vxh_LjrzrsWWJ0-BxFrDQerrA-tcfSJPCGk7PVQkvRdFjbv_JdFQMQ0C4-bcmQ6vM8Wdqw1yM9FyOOhIcp5rH3haK4tdEcqIQpWq72oycR2DxDn-DUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/29065" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irkFhTyENi74yYTCjbhjDO7mW6l7EVPtlTMoqA88I-HVhbPZKX8nuYAoM13NF1BLTpHIhEjfcuOx8YwNcSsO1YhpTwePTofE5KGh34AhUUHF-6Z3p5bbkxnUBy5UjICcReGr4rzg1cfS0mVIa7SugTuJzW5Uvi_8ooWJXFKu20ygMOpbuA_YsXTkEmfF96zXkzXNDLG_Nk5S4NGF_LrPN-4g3Tzq8esTD4Z3beXZR2UTt0vksfrcFIVHKblEYKXgZNt0JP8IQCxhg8QjvPzQTm0ro5jtFzfj1B7hf3PLrE9vV0c9xdLCx9gheYJRqXrJ_uxbz7vJkh0A5LUC3wJL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/29064" target="_blank">📅 22:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29063">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxbJSvzuu_cLXOJMr4DVu3lOJ9EDftwwSEVuop1puDc_k3HKn-KYWmpZ5bLAbOqS2unIlIT6qWHn5VewJLDcUVREdVNU1HBkZHG5_KAJmFMzhIDkEsUhWIQiITAQl8anQ0uxPN0nMb57ERM3_gp6wBTmCNTJJPRPp8Kz6Pw_VXwQFDo4pcZRBy_NQp30ULYs0qys8OU2XF5zRdyPSsV08QZyQ595PzSlmibf1_NQ68dIOXWXK1ub-HSgAGHk5SXrGG6IOoahfuKQF5WYh1JMOhMDiCJIlozKr5iKZGRCha3AvXLM39mOE01a6uBqIkg1Q3zAyrJnIuFQM4lqsvRzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیو صحنه‌ای صالح حردانی در بازی با پرسپولیس اصرار داشت کاشته بزنه اما به توصیه سهراب بختیاری زاده یاسر آسانی پشت توپ وایساد وباعث اعتراض‌کاپیتان آبی‌‌پوشان به کادرفنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29063" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29062">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpSO3a8FGxjPmfNesnDu9FqBAykGtYryqddn8lJjn59OWUtM_zpKqUIXKZljr944JkYCnNEAjZoTcYsEePzIPiM7Z8hDKO-TrdrIPTQAWxqzh9vLAtPRtpUB1pv87e65xNArRIcwUBUGEuamZNzx33_j_vA7FHniZABABC_kRfJqvKQJymWiDngcQNlSXmbR0Vnk6F272gCKvxtmxZ96IgOCWl1q5omEOSe8p0VZqnPdgvl-wCpvQsdwGHPiihqMLgkh_6vXMij6u-1ME4mkSCwZngcpa-Q-f1wesdvRKMvh_Xw25oN0Dyr0RxhEjIOV6ludZqkp0ybnqYPbfPXlZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29062" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29061">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAIP3oJZME4EZmBS7ruVF9FtKSBSlNg78xLpOGrq0-IdfYeW6SH1IFbMmylXdvGk973FZehz8-NEvWccMHtO7-ihNP6A_9PE7-XtJWvaT4t3-lz_LD2Fz6d3YfG_t8pFai6mF4_yAWGbt0cGJh--F9T-AQbgrBEDNbD2poeGLIwDTguDUXV-p3VioB3bFxI_-WsRfRyvUgONrUh-2g0MtaYysxZw7nUwhVWMo9zic5fMJv34b8Tv7aKAiKFOjvVGhZzOrTzwA_Pst7wX2S70fW2yPR4O4d7dQudjh6xVSeABJIu661lkpDblf5lvFumAGVB62Xi0vT74rjY2l70rNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29061" target="_blank">📅 22:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29060">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=R1ooUAz3XrjlNi-qaZey6eFaZYBRa2WukWCT34l2EU7KucbCjJp9hUVdipxSvONzJy70v5J0HEx-AcipnrZVvz5hFXdEp0Ss81cpcgZpYupjtS8BZpso226BYgRXrMN7aOXFok06tPJXjoDrD0hcNF9Fxvp9JKaMnef-EqBAwglJ-msQAVUBGZm4CTgPag3oNHkTbyJcgHnVTpr_XTi1CBxneMnGVGCuFBZMOg_NYZ43fRRN1j_dJEhwLH-Wyp3qVuId8dMuOxyOS8XB9d3j5Ro541GUBPVVBsWGj9Kp-bzm2-gf17jxZ9vB4htYg2QcB0HxKJVeujcDDQayz4RHDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=R1ooUAz3XrjlNi-qaZey6eFaZYBRa2WukWCT34l2EU7KucbCjJp9hUVdipxSvONzJy70v5J0HEx-AcipnrZVvz5hFXdEp0Ss81cpcgZpYupjtS8BZpso226BYgRXrMN7aOXFok06tPJXjoDrD0hcNF9Fxvp9JKaMnef-EqBAwglJ-msQAVUBGZm4CTgPag3oNHkTbyJcgHnVTpr_XTi1CBxneMnGVGCuFBZMOg_NYZ43fRRN1j_dJEhwLH-Wyp3qVuId8dMuOxyOS8XB9d3j5Ro541GUBPVVBsWGj9Kp-bzm2-gf17jxZ9vB4htYg2QcB0HxKJVeujcDDQayz4RHDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس کامل مخ زنی به سبک مهران مدیری در سریال جدید او بنام مردسه هزار چهره که از امشب فقط جمعه‌ها از شبکه سه پخش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29060" target="_blank">📅 21:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29059">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auYqMQbibN0grn0xK7yon8RtIBiN1mbscO-XHlq3gNO3OUxq2K2yXz_PageVnEWL7LwCAMHFVaSfEhNV76oEQPFnyPREgNQ6UwalInXA2Y1zJNmQr3l0q5wc4qx--pKLsh9ejqBvhUTrEcFAKB9C5pSR1UkRFkc72dvlk_tJY3YcwX-S33RqON-XCRSr9aklitUpsSqcpI-uQMku5eD6T2s9ajiZ-_oL_0gDgggT4N7YvT5t3CcQ4mcOg2p3Qpd0jTjubagjhNz0GbFBWR4UfgRFJ3EPBnfb73Mx-Qlila4mgzc9rZNQbbCNffLHWiwJj9Fss0pHOO8ssHX1_Vwt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29059" target="_blank">📅 21:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29058">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=OA4hY4Tu9SpzRyvMhYIEH2GcNunURPfnZnZfWqyGFEjMdKjeKktBoadPCbmXybgEJoYO0bf65Ixj63udBOpQ0QYURHib6Cvh7r81QHri8Io844NLkueEBt2-oK4ckScLWL9lV-xw_LXWuYAFnPkkIXNt-JsVFgNS2JSq3GVgh-Tg7h6hfV5orf0Ryn9b_WLBn1XhQFMYjr6PpPOxRpYyvYrO_WzY5wY2eO9kqp2EdworK-huK8tq2yCHFGJAPLkxMOmeaGODD4BsragW5uSo6g6r-0EFpNxo3cMtV-_EG4mZ24ILLoW45TlDAQYGu1-8lTYgVnSrY2LfF53hpeZscA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=OA4hY4Tu9SpzRyvMhYIEH2GcNunURPfnZnZfWqyGFEjMdKjeKktBoadPCbmXybgEJoYO0bf65Ixj63udBOpQ0QYURHib6Cvh7r81QHri8Io844NLkueEBt2-oK4ckScLWL9lV-xw_LXWuYAFnPkkIXNt-JsVFgNS2JSq3GVgh-Tg7h6hfV5orf0Ryn9b_WLBn1XhQFMYjr6PpPOxRpYyvYrO_WzY5wY2eO9kqp2EdworK-huK8tq2yCHFGJAPLkxMOmeaGODD4BsragW5uSo6g6r-0EFpNxo3cMtV-_EG4mZ24ILLoW45TlDAQYGu1-8lTYgVnSrY2LfF53hpeZscA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استامپ‌من‌کیه؟ بریده‌ای جذاب از سریال مرد سه هزار چهره. امشب‌اولین قسمت این سریال پخش شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29058" target="_blank">📅 20:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29057">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=R0dSwW_lTjYcBc2BKXtQbMAPJrtpRBJTpe5jqLf1UszzkUADa1Qm-_St0SMAaA8wXXbgpL2z-JyyJSUPjhUMdn0WSJiuCSyd5UXsHV0J0Qs6qbSPdZtQjdH8giAbkepdIem1ExLtpYdeFRifjjE_6JIac7gMLMhDiv9Ja2mjtKX0Li4AZ_qB1Z_ygl12S7bWbdpojCfsmzJMZ7cunki7OTbiZdOZ_6o7vjugyuMoirYOKISTnfW6HOLVfbxRF9EGeUB7Q0iU5ZI372rcrvNlcgtQd1DxfHQMg-J9NUkbkrjb9mzJXOzYI1ff-7vLHEw6EWpPeszNkjQBw-O8qdIPSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=R0dSwW_lTjYcBc2BKXtQbMAPJrtpRBJTpe5jqLf1UszzkUADa1Qm-_St0SMAaA8wXXbgpL2z-JyyJSUPjhUMdn0WSJiuCSyd5UXsHV0J0Qs6qbSPdZtQjdH8giAbkepdIem1ExLtpYdeFRifjjE_6JIac7gMLMhDiv9Ja2mjtKX0Li4AZ_qB1Z_ygl12S7bWbdpojCfsmzJMZ7cunki7OTbiZdOZ_6o7vjugyuMoirYOKISTnfW6HOLVfbxRF9EGeUB7Q0iU5ZI372rcrvNlcgtQd1DxfHQMg-J9NUkbkrjb9mzJXOzYI1ff-7vLHEw6EWpPeszNkjQBw-O8qdIPSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
🇰🇷
سون هیونگ مین کاپیتان کره جنوبی:
من همیشه‌گفتم‌که‌کریستیانو رونالدو الگوی تموم زندگی منه اما بنظرم لیونل مسی بهترین بازیکن تاریخه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29057" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29056">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt-ylZ6on6He96XbpTdpQCQXWoF1ACWz20vCOxHWxrxoYHhI1g-Q1uNJHa16Fd1eUdI9-f0_rCJ5BaILzzyZuC4xpVuVB6bdGBOp9aDBuIqSDk3hgJYBFAxoAyYFAxhp84NPszUCCSH2dJaxLVExGcSCnV-peAff1-5TTusDCVPuIA-MKdNUTqJX1k14BUjrODijKEC3h7NnfMxHaPh_-_1g_FYE1axt4F3cB_454I6tuLi1Mbaz2uB9xvuAf5EMTJfWgDZayGLwbCZHbanwuzdJ__BbIrEtl2P9P7iHn0XdEmOeieg8b64BQOzw3CbKnsPelP02gTrQTXJQfAPa9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29056" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29054">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCgZPosEmEVh03WX8YQbDh4XTbjmruiqeIPsRDzelT3m3xP3hGYv-zsZ7hew8CqRbTe7rKwFEMvmwvHDjZjJ8MHpFG-kFYf60GHn3dQws6T2RT7LWwWxy_IJKF3ZURymYqntQdB-byzQl3KtkiBDNlezLFKYeYcES2XVN5nFfVm0du4p_ympEiQbeexIhtEjkCwA34vTxfnP0zaRgoZ1X2zIDWjv_jSbwzIpaXBCu0OveXW-1WkY4ZtbM3DzX5-2lg_HhiAQgHLUUAbx9zKQ4jXWTy8dnCXAQnzShdKreL2fV7e6Fw_wt0z1Pdw6mC7iZ4_9VwNqAunB4S7xG1BEBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDNEu5cLh7bDZIT6946PZRQC-3Aa2DfRl1KBDDxFAQd3ZTVnxuFS-rWOO7Fc9X0CNofCn44qB2LEs8_8BsEt2zeWunQLB9V0cjV188Y36icCRlgGrcp-ERrFrr80BSSHbB3J7IrV7v3Syyo8uh3Zpxdzyc5i3p6MezO2jnuMKNctWRNMrtjeM2bGIP4flAek17QfAMhj79jQc3r1zrpXarO50PzDIVwId9BJfKMVs8UV6Y3_h-78uVv8ok4UWKJf5XEoTbH1vKUK-o5cV0GrMcpH1VnbWapTPdCBvngVkm6Hy1oUG2ncs0KjZYz4BSI3SRHVJr5iREhw8VPR9sgxfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکو خمز و شوهرش برای ماه عسل رفتن توکیو ژاپن؛ تو کامنت‌ ها ازش خواستن یسرم به شمال ایران بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29054" target="_blank">📅 19:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29053">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTltS6HG4GtRERQMXlCuEUYVV0_LzC4_83hNrMEiiajMwjldyY5o_gEnSFOf_vShVNShGGTcNv32KhosV7OU6YETCz1Nsc2xQpSbHUnDx1iele3j5_RIlpvzhabllXlgN-dfoEEzNztH2JZQYDUqsDUKm0iIb_LN781W6Z1_gOqG0mbjZ4JiOUTaGhpByA4hNAjOFlAGRpKwyU9uL3DXUeM6tWuypK76vaIaB8ToYEwmSXNG3pSY1RXiBwuVZkaAbLP--I1wPq9uW8xgGyNM2-jvAgM_IZv9dDUtfiVq9cCZS_qsHCdRFy7V-eryZgHgo9H3AYhke45KxXZEilFjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29053" target="_blank">📅 19:09 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
