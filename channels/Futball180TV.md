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
<img src="https://cdn4.telesco.pe/file/sji9SiE5wsGTNeelQ8Q9JKA8Gc6TOrFE67U7HIX51fofm727SMgGXIV3lcWkDdxdIikfDytfHPeW7cZKWzzPrbcXUfnvSImc5J5Dz9ucey-flJygwz1IMVmznAGp5FomtgXUX7c4lfHqatvzAVwSamE0w8VlSrtPCUMZQbosOg2bb8fRWM1AhbQ9tCoJpCvWVJsuQUGTGU3Wj0O8q-0Ps7K9XtqYOohqqt-ll7VjD5cx48v1Fu-OB2C87njGKjagSdB1E5fVO7f-Tc0qnlspm61-VgxkqV9kUu3qhuLnu1j868j0BAQ6wu-HtwMuYpgTrfdim0KJlQX8ZDBTayd33A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 130K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 22:06:34</div>
<hr>

<div class="tg-post" id="msg-90497">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
⚽️
⚽️
⚽️
اخبار داغ حواشی فوتبالی و تحلیل‌های لحظه‌ای جام جهانی را از این کانال دنبال کنید
👀
اگه می‌خوای جا نمونی، همین الان بیا داخل�،
👇
👇
👇
👇
👇
👇
👇
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
✨
اخبار داغ  و کانال معتبر
👌
👆
👆</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/Futball180TV/90497" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90496">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDBl6DlbbQbn_Az4IZ9ZeQw5V5RFPb1GKH__xybD1kRRqdwh_wuz4UPPC73lJ_1iJUKPzgX4PmnicEv9rzb3m6oNgpmZZ9aTeowkqu7V5e-CPhGyCaslcjfbjv1rz0vyY7ucpXAG_EOeYZQbNLgbYvxXYDOlOta4fj0K-rYlBWsTANQhkVGV0i0qVLG9J4Lum_69vHkMMPBqYbJ28JiZZdpCd9aiTjZGnj1jGDspHlxxhi87OejEFTSY3iXodSS6NxUCdfsGBMXPgzhfb27KJbNmb7-O2Ety5d4mMP6VuMyTYmkgr3EmfI2tihQgpw3aLOfmZ9stHw81wGrTNzJ6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید یاسر آسانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/Futball180TV/90496" target="_blank">📅 21:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90495">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">موقعیت های مشکوک به پنالتی جذاب تر از خود بازی بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/Futball180TV/90495" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90494">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پایان ۹۰ دقیقه
پاریس ۱_۱ آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/Futball180TV/90494" target="_blank">📅 21:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90493">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/375a1431bc.mp4?token=Fl3kFqDe9OequnrEJIvsTwm6ywqJc3zDt1FqutY3dwsrD_Neye6xFxl2oMorlN4JXDK5-TuZg-8sb8yPVDW8WIP3o9JYkCOdlMQ1H2f_sVg-1-Q8oyoeBnWJAkbcpWQHN6gJgI-0CDsxF31sDXa-Gz-_D5G11I2tCfh1_C4Fb4kEr4a3mPwM1pDBbm813SHLq7ZqakZ9v_9LMxPqO7UiUH06bllYkN0LHyDWJgg8dXs0yRPH8yqvTcZ_JehT9ya3cdt9sGIziTf39xtAyawVTqZqkg_roezx5qqLVytzC5h7-7a5UHYeR8YfCUYD2jH8X1sjH8jvMfXEjETbheBZHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/375a1431bc.mp4?token=Fl3kFqDe9OequnrEJIvsTwm6ywqJc3zDt1FqutY3dwsrD_Neye6xFxl2oMorlN4JXDK5-TuZg-8sb8yPVDW8WIP3o9JYkCOdlMQ1H2f_sVg-1-Q8oyoeBnWJAkbcpWQHN6gJgI-0CDsxF31sDXa-Gz-_D5G11I2tCfh1_C4Fb4kEr4a3mPwM1pDBbm813SHLq7ZqakZ9v_9LMxPqO7UiUH06bllYkN0LHyDWJgg8dXs0yRPH8yqvTcZ_JehT9ya3cdt9sGIziTf39xtAyawVTqZqkg_roezx5qqLVytzC5h7-7a5UHYeR8YfCUYD2jH8X1sjH8jvMfXEjETbheBZHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل‌اول پاری‌سن‌ژرمن به آرسنال توسط دمبله
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/Futball180TV/90493" target="_blank">📅 21:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90492">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گلگللگگلگل برای پاریس توسط دمبله از روی نقطه پنالتییی</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/90492" target="_blank">📅 20:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90491">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پایان نیمه اول| آرسنال 1_0 پاریس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/90491" target="_blank">📅 20:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90490">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">چییی خراب کرد پاریسسسس</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/90490" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90489">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asa5CulCveMH50O4vJdLzIzmEUengE3JqHAN7d6rVKS5Ze86ykT-Kj6UuYWjQPlVDdKQmpQgeQLWRFIfG0s34LTHosQ3u8U0i0e7t6xwkF5XAaBfdoaGjWxVI8WNZzLq11Dd9aPIWlwtJv7yvB7FbSMWwD8qUnIj3eZQcPjD0S6vZnV4uvh3bjer239iiuId0ds-1JrkOuFHddujOhIBPe_ljZFtykj7b7HqtrcIJe5EAbNjUET4GtlnEkZ_lmNNbiymFC4QPkY1TsdaJXsVlZcOJNVnDPBBxaBJjGq3I4nEstQtfUGCsDq6cEMPXZ20-ljdG15jCERBHJntaoD9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرنه اسلوت گزینه اصلی مربیگری میلان در فصل آینده است!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/90489" target="_blank">📅 20:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90488">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNUZWDgXMwoNCYYtZcFsSa6dcwz4Vs2qzNFYbNPVgKEV5R8Lj15kjs0ioVliNdCb8qH0u9QkS6WHKxGqn-c6pzP50WIHZGyhPHApHq15n--LOAZAAiDSfihteRysr6YrjmhbxHVvFb58B6b4YGywZXtKDyrmOCcz1N690Wa2dWN5Rm9whvcixLO_XoBOYe-qPG1qcsQAMCL5-dQatHZaoYe0xK-KIyofKvTxluGFuR6uxo41fbhbUlZB6h6a9FhnVvu5d1Ij682b2OABk-kjW-EbT-2kWGwHY9MCDYyNjp98CWjOoTpGQTxhVaELLh2z6i662AW9fN-kpXYfajL4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی پاریس گرفته نشد!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/Futball180TV/90488" target="_blank">📅 19:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90487">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90487" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/90487" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUSQzErxtqwFl29vKeqpu-CHr_8TGvWP3JiUhQVRPqctgKQJdOQ9xC6P58ffe-Xfs8kBF__6foON0z5meo_IXxgCh8cQ8X9EBykmFLgghHWK9r8p0DRilb1dcvpfpF3ogZFD-MNjnSYh1NEwg3CgbyLBiexykCxZBN1uGcrVpjYQOv4lGZ-t1s2gowZ3nTU-DFi6M_0hd3YSx8YFU-wx5dZWzAt9TtiRQUU-eClDJ81ZzjCmEnp1C2EJ4Q9YukeWCCW5njDo8lrUsCG8QApPt0g9ZJ4zSpVPePQCgstF_lRRONBdRXvtCcI3IA8WduKiBHdmiaDCrBae8lZFFfRJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت G9:
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/90486" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90485">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFWhTnOTjCMTvFNOhCH_m_emTfXI02jZpa0AmteH5qTwiM4mA-T4ppdf5nZviMX9s1OMt4u1zvuUyGe0r8vym9iHkgTbZrQaSSAP-emrx9w82x1ZtxE03WvMMaQO-ECLJNGsjjjBZ-zHSKt_sj_rrsITGJ4p45TZm4jpV4hrrsZVssNsrC5Blw7ydjooI-j0dBd6V-xDZhe9VGMia3AehLOH8ajqetrmfOHZE5uT3XFc5zqoGSwJx5JbHzNYp0aNwmOTh-dn4rOwkbHx1SngfxdBtd5RxEG5TdqZN3ocpWpBdYsASMErHo8DP_t3extCECjtbipEYQrosma8v8mWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی پاریس گرفته نشد!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/90485" target="_blank">📅 19:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90484">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/71e697023e.mp4?token=RRvSBSAcur-SOGrEP5WaG4apj0SNhjPldFEY1oeIFkDvjbOI0BLUYvdaaoo1jaegGRWqbsd83i-TSx2frd_JH6wkq84yFGIbOmeBHVQqeMsIpJnP_1uL1sCVScVpHtfton5iR_V8U8uw0CepJ1xJu4TlK6R063Mgy2FKkPTTuMB-HNqvOlcxtIlPlN9Tp93LbOXMrzZY__UR60Z8pl8HwuuZo6YHUncQUeqA2ldAI7WDJrIdJ7KSs7TvNHqeb8fuW4eo4RF_B63MIUVYrVsupi5EbDvoZSFCl1dmJzXnepU8oqrqJdljOrlVX1ulP8nNT4FHWHoZn35xOdsooG1Dfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/71e697023e.mp4?token=RRvSBSAcur-SOGrEP5WaG4apj0SNhjPldFEY1oeIFkDvjbOI0BLUYvdaaoo1jaegGRWqbsd83i-TSx2frd_JH6wkq84yFGIbOmeBHVQqeMsIpJnP_1uL1sCVScVpHtfton5iR_V8U8uw0CepJ1xJu4TlK6R063Mgy2FKkPTTuMB-HNqvOlcxtIlPlN9Tp93LbOXMrzZY__UR60Z8pl8HwuuZo6YHUncQUeqA2ldAI7WDJrIdJ7KSs7TvNHqeb8fuW4eo4RF_B63MIUVYrVsupi5EbDvoZSFCl1dmJzXnepU8oqrqJdljOrlVX1ulP8nNT4FHWHoZn35xOdsooG1Dfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول آرسنال به پاری‌سن‌ژرمن توسط هاورتز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/90484" target="_blank">📅 19:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90483">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سوپرررررررگلللللل کای هاورتززززززززز
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/90483" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90482">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آرسنااااااللللللل
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/Futball180TV/90482" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90481">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گلگلگللگگلگلگلگلگلگل اوپوپوپوووللللل</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/Futball180TV/90481" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90480">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvgDtCyBjsjLhIohtJ__Zn073IZxxCvtStX3wxj-l97iyq6uSkm95WGfS1qIiMfh4VQBfUre2PYdmrLnWzk5wXHRmvLhdkILlqC_boovCcuXECE_RBp8Gr9B9S3HSM5a6932SsUYbD8m4gvptrUPonaVRIWiY04tHlznQR1DtGTlIYn1qs1bN6tT5-YzIa1SbkvjJRnV0y3YzNV78zEKgbtQpcLSTFVt21Cpvkk95mzQZpaz_vI0phhuVKEeWqwuNLEf9Xj2umej4AcZfyj_4oZiZOGoePBdvquYtAV0iFQqL7WsyDWqx1WwUx1Yw8wNVF3KG6YZCOmswSl3cCZUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتوی یک هوادار آرسنالی از پیشبینیش از بازی امشب سی ال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/Futball180TV/90480" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90478">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pb-9OAGue9OcoYG4tY1SIUU7GRbjzMqixWLgc2X602pb6feSeZUEPbCgFkOQUa_H3rh5ms0RF26YJSg3P9qqDExp5zKmQKcs5c-Z4z9LVLvplOozgztoeDH88ieZOPxZPlktOY0MihSF2pOvolkv06Ioj8m9RVN-OmXp0uDovZOGs0fDnhKVLsjVEa-UojnBLcKrZr1iZB-3-7hZ_Mt39--23R_20FNzU7hjvafdHtHUlhdAFhhf8nNE_5u_eOkkwbz4PNSrlVIE1KsUaxXiTx38GOedJrYLFD1LLKncCt819zdtUvXguS9gTYE3Ziiv-G64dudKfrK5wwy77mz7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuuoF5xZSqH3xRaemvyV_9UoszaJZqaPXZH0F5W-pg5QOKGF9NravdYOCEjrpw7A46JMkBzX1BrrNV1XfiP6DiLP4HIN0ctbcQhEC6ys2Dk0oc7e5acbs4S0GZKERr4FFkdutwDBpijJHE-yy7CyQdxrvPe5SxetmvUqDL8UxXQsZ9kI6AIl1AmnUz7tfl4dugJptaizMKBIU2d_AYaZMX0EWWd-ONwWJ5LRPmv6kxlmDTLBfqXrO0vxZNFOsg9zCWDd_pk2sxUlSnAimFY9dhDfR-TKUS6qM-VhVJD79kXQVIMWUHgn4etpkhI5VUdlSakPb28CEQMe7YeH95Rb4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسکواد دو فینالیست ج.ج قبلی و مدعی های ج.ج امسال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/Futball180TV/90478" target="_blank">📅 18:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90476">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhgMv-B73FDLNWiXM3hZ2jCArF54UU9zeHkmXA3r4C9PEfKUpn1EQlTNMUkqmsNxdAN1Q-uMaVOu2R4OAezhzyo-gfg-sFdv7mc8C3etw6EIHU7B8CGdXIy3dCRhXKFpSfrFpJ7FONuVhq0uzNOQvT6ojortoqKjxfzr6C1kMEGldq-s0Jbp6E_LXTjCb0jSudrLG2ZWdQEBxpQobcE7dqDyB-AhMKeQn35ghMfz0X-uCL-TVLxrc9tSIkdAqMCPELvvdHdPwmBD48sxmLTNI2C87S3nTqtxyC93Tgl8C6Op0KQGQ9R1kOvnFA_y1ODn3BD7UrgdgAuIkg39t8nd4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1MhvFcXu5Lggbm9jH0npklyNTPiFC1HXOOQvf3ruvaUtx0zmzP-ckznUoU7_EusCWKjhpd7fGZJTgdq2HCcXSNXifeGWfXeqX30LLZQxbCqUjqxuPrpVlwKwFq30E6OFHXRb8_FiqGPgcCGgv36cce6zvuwuPUL5_aovu5oho3jgY-4yGZEfQFSO0sZQ3M-ylYS7UB7AwKggyP5UapVTniFq-2neYQKh8e8UhYsu6NjiDcniHpZ8AvSw0wsAMDncCVD1WuGbo9T2xcHSJUPjhGGkMKpyTHvOj2KHv4r9AtOO_WM3zKmgQqHz6NlorWIumxFYQQytDkg9IG3fVEIQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
ترکیب دوتیم پاریس و آرسنال برای فیناللل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/Futball180TV/90476" target="_blank">📅 18:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90475">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
❌
🇪🇺
با اعلام دبیرکل فدراسیون فوتبال، لیگ‌برتر رسما به پایان رسید و نمایندگان ایران در آسیا مطابق جدول فعلی معرفی خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/Futball180TV/90475" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90474">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoL2CRZ3rUshR8tz3_S7LtP2Y0-e_P3MGeqUBoKZXk49br7EsLCGEBCUOIHWsbiwUUIq1frterAXqz8IUBTeTgXh0hG69L0DZlBO6yr7uurFZthyKz2kjNLa6BBq-I0FxtwYPMbmqwtS7ympFo6Mok99D71HO7cfvEmKtv9JPeK9Le73TGXiQVhCkyOoS-qycUJm9glMXjkV3IxwUVDc07GMciMWZWPzy1Nc-kux96LgOUUcuKyrjTA32irdOlTf8i5FxBPV5_GHIpJnBEJeIvPLZBv66_BcPMQ5kplb980H4F9lUJ807VFfu1O-THIg78Cks6P04HEcJrTFhVHNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتک
#FreeJulian
ترند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/Futball180TV/90474" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90473">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a387H6Ej5MfN8wZ68wFXWoF31kDIVo-hK_C_fZeTVgXUvAH-ZSvW4ug9pqdUMKCjOCsVU4JbnxLWK88-TYaofkrYY5iIxgjQzi01DT9xdpDVYHprSZ7kxybicdx5CVQn6MWF6vjAz9iyr4JEx5oBzwvsohCoym-Y2zJL4WKd-UmPYOQui7r5mPKwAxwok5sNZ8fKizKERpJm_K2DtflqcRlFMlzkkSTWRZNUoLM3dHYmqLE0xNVuh_RvRdEq2TeHeBxjTmef1DEyBdpgtgl0eAk1_nkKwRB2zMo4VCAUYDPAkoIIdh-5KbOmLC5BZvySVrXX6kEnDuilYv9GSUAEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
کوپه :
بارسلونا درحال مذاکره برای خرید گواردیول است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/90473" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90472">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=plELs9vaWvZFyadNz0IU4RyWOSON_jRk1_tLanagD5O3eav86IFieI0IimDSebKjpdHGG-YyddLXggwzE8vUDzbGWMIn1bdQHbl6cQDnKRQ6yDf8QjyKmpZ_oGVEVjgddAYHtvFBb2aFvgJG-kvo9PifhArLRWdPJp0W6QhZMatdpFfsI6cwRBslC5DDTtCOTttfrmtH86ByoT6Mn2SCwMAaaH39AWmcTUba_uv5UyB7fvSNmbtjQm-oQWH9uNo2tBryXquk4X2Pg1-luXMlOFKG2GF6cmtpVEiECzu8U5ltvAmNC3v-7inrdDjYBTWZ1xPiyXirmUXsXGxjI_KqhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=plELs9vaWvZFyadNz0IU4RyWOSON_jRk1_tLanagD5O3eav86IFieI0IimDSebKjpdHGG-YyddLXggwzE8vUDzbGWMIn1bdQHbl6cQDnKRQ6yDf8QjyKmpZ_oGVEVjgddAYHtvFBb2aFvgJG-kvo9PifhArLRWdPJp0W6QhZMatdpFfsI6cwRBslC5DDTtCOTttfrmtH86ByoT6Mn2SCwMAaaH39AWmcTUba_uv5UyB7fvSNmbtjQm-oQWH9uNo2tBryXquk4X2Pg1-luXMlOFKG2GF6cmtpVEiECzu8U5ltvAmNC3v-7inrdDjYBTWZ1xPiyXirmUXsXGxjI_KqhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای اینکه بدونید دعوای بارسلونا و اتلتیکو سر آلوارز دقیقا بخاطر چیه فقط این ویدیو رو ببینید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/90472" target="_blank">📅 16:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90471">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6ScJ2Jehb0756X9uAMXJntoVfvkNKj9NUEtzQVardKxgmij2OStl-qU4-PSPWFzlVtEvW-qgLGfIMhs4P6b_tMCCElzkqA40RJF53zT6dYv6AcidLDjmz_CNun3MkxwKjeZLZsTLAiRRAOMWhuG59Ma49UsYQdZyDp-oW00gLe7b9wrEN8TbuXPd1P4z449G2HZbxOrgB-zJjQdqlJcjqfoWNxqAJ2nAzU2B7qTikkeHAjx9_f0XW060tNtI9Q52z3wjE7pASFd2XQUDdGrfEY6llaXBqcoZ6AqYvEDMPUDGbAIjXE7Er3iJIE4jyi_aDjTLzpQYSUVtAbRQbg8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی افتخارات ملی لیونل‌مسی در آرژانتین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/Futball180TV/90471" target="_blank">📅 16:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90470">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=F697EZOUg9gtZ0bGoMBZPfXCjvNSFxDpM8rtE_QzyYYq-vEQ1dTDnpEU5kBneaVwGsNWgSwyzFoWah8EvNqq9MwRQv6AM2MEEF_ASuMaOTTG2qQgUXYsbX7JX4vNBlEl35zcIh77HrkuyQWBCIiyIFcHClxs5NgoQknJL6N7RyUVVw7nUQFKvVlm7PJk7NqPZvfrQ2Vo3-KaDN9KAOVmoB4SRB6frX82XR4VsFFpPFgW_TyFdb04-eAsoDEGGtD2q59f8kVltKNKwovFsoPdG02_IsEGMd_bK3Os2RhhVzYRFDLYduFi1tYx00xsWAV7Dh2ZDdoOzePvfRpCxP0V_ISrjptM3KcgvC86-yp-EzSE5HYJng9QR_MCUOTuQAlVrXP69tRdEXcESPXwijok_Q7t9skz2DrvPljDzvqp8MGbCWYvW5cAFnn0-e7ePwbXB-MZiQCqVKeNN_kvhlPuQuvK6x9fVTIl0ebZhRZ_dhPfDCGB7ggtAbyLeVChPwH7phWcT9oYywL4tIAvrtANgBY6CfayR91auyd3W63QNxuOUvp5lv6fgw3dxV7VLWDki5BEhambtxvlCVm_kSB-gnyHvs4iAlUK03pzHtUJqJs3lC1mWrmcL3EuiN-wWuj6X546TfqJ5t2WUyh7FGJw5eb2TMWRkQvZesHV6voJ3wY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=F697EZOUg9gtZ0bGoMBZPfXCjvNSFxDpM8rtE_QzyYYq-vEQ1dTDnpEU5kBneaVwGsNWgSwyzFoWah8EvNqq9MwRQv6AM2MEEF_ASuMaOTTG2qQgUXYsbX7JX4vNBlEl35zcIh77HrkuyQWBCIiyIFcHClxs5NgoQknJL6N7RyUVVw7nUQFKvVlm7PJk7NqPZvfrQ2Vo3-KaDN9KAOVmoB4SRB6frX82XR4VsFFpPFgW_TyFdb04-eAsoDEGGtD2q59f8kVltKNKwovFsoPdG02_IsEGMd_bK3Os2RhhVzYRFDLYduFi1tYx00xsWAV7Dh2ZDdoOzePvfRpCxP0V_ISrjptM3KcgvC86-yp-EzSE5HYJng9QR_MCUOTuQAlVrXP69tRdEXcESPXwijok_Q7t9skz2DrvPljDzvqp8MGbCWYvW5cAFnn0-e7ePwbXB-MZiQCqVKeNN_kvhlPuQuvK6x9fVTIl0ebZhRZ_dhPfDCGB7ggtAbyLeVChPwH7phWcT9oYywL4tIAvrtANgBY6CfayR91auyd3W63QNxuOUvp5lv6fgw3dxV7VLWDki5BEhambtxvlCVm_kSB-gnyHvs4iAlUK03pzHtUJqJs3lC1mWrmcL3EuiN-wWuj6X546TfqJ5t2WUyh7FGJw5eb2TMWRkQvZesHV6voJ3wY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر پورحیدری: روز عروسی من و منصور، داریوش زندان بود، ستار برای ما خواند!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/90470" target="_blank">📅 16:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90469">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=RSzJkw1K9qqcoGDrgOZEyV7ONLYbSB0EpekX2p6FcVgApBAZS93v9hAWT5nkeUvsk-n-BJYqv_K-9cf_shktidAA8P8f3MLsgiw_cQTZHfwnUTdWSUK8rigTd_9HTeA6u4uWJD6c-uyX6MNfVWqz_7UuYWMZ1mIYa37Cv5uYn7yj4Vc1TyDgGUzeXGn2qPBkf20UMUatACNNmzB1V6KNlLc-deNKOL996yYKuYKJve8mtM7P1TVQobXaE8i5elVlz2RC040ILSVP-SR1Mp9tBxS7ULvtB4xj-NCi0HpYWwMvp9VvdIis5GpKK2SQpekLa0hvvihF_mMQ9DDA1eaD4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=RSzJkw1K9qqcoGDrgOZEyV7ONLYbSB0EpekX2p6FcVgApBAZS93v9hAWT5nkeUvsk-n-BJYqv_K-9cf_shktidAA8P8f3MLsgiw_cQTZHfwnUTdWSUK8rigTd_9HTeA6u4uWJD6c-uyX6MNfVWqz_7UuYWMZ1mIYa37Cv5uYn7yj4Vc1TyDgGUzeXGn2qPBkf20UMUatACNNmzB1V6KNlLc-deNKOL996yYKuYKJve8mtM7P1TVQobXaE8i5elVlz2RC040ILSVP-SR1Mp9tBxS7ULvtB4xj-NCi0HpYWwMvp9VvdIis5GpKK2SQpekLa0hvvihF_mMQ9DDA1eaD4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
و تا ساعاتی دیگر، فینال جذاب و نفس‌گیر لیگ‌قهرمانان اروپا به میزبانی مجارستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/Futball180TV/90469" target="_blank">📅 15:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90468">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهترین‌گل‌های فصل‌گذشته پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/90468" target="_blank">📅 15:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90467">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/90467" target="_blank">📅 14:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90466">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDGVkjS8fq9T8yMqE9X1YTC5NUNEuOE0-Vlm8vI3o6nEYqiGpVj9Bso5AHUqGKn3-Wrz6ThUObExIPJiK4u8J1Rym1LNXAnVUro-Fa2gQcp8zL4YO8yMyLLWmZQrfEdekfUkAnTteQSyYu2Yd70gy9_ISAmpuNiXp0STUYhtnrCf26nIERUDBa28r8cddnCC7GtE0QpLV0ogRx80TucDt-jM11bs-ZvHhxXqlOJaSNhEBTui1egueSRjrKdRdQs5dUMS1n4JsSiXcNoy9esprkTOP77kgNMyQqMwPVhWbTNpKqzDnzuUbw5CeVuH2f8pe_TwObp8d4ddxUjwzUyhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/Futball180TV/90466" target="_blank">📅 14:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90465">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyyf1Gbr80TAJ6mYjB18-AzqRNalXaYh-IYoFRMY53PjQFSi0yXcv07xlX5gVYP2QA5_6uTI5CXmDTYkkKRiGy2Lz9fDtCJ2klh0xLBNB0O0q5kEgWSyGR5U6pkWMqxJKGHNdNSG1R42lf8bleAk3Ecvxjs4kMq7iOcsqcU_oncxUOYGijS-qrbGs_PXyNOyxAxNSgszruD_VdhHvBBky8tbqnVXGxdPOsLkOJSiSixzrujo7_rJu_iQAzXryxkvF-1gAu4Xwy8sqlkxxoE9gjWW6AEHpgD7O95ORiAvV5-LSgymnR6wfsA89DSmiVOvVyZLYuH64IFQUTos-5ZsxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/90465" target="_blank">📅 14:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90463">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7iZPrUO8S-vEgKGmdh6PHdLfxY_IGqpWM0Yygcdh4iP0q6qsKa0bwWxACesXiwO_hza-HsUDPd0eW41wOJuIJH893RKCdmRwNDjOwrYU5g5dL4FhYDXFoUs3t80-zt6Zpp4op6xfHVrMxulDO7Gf0hDB5M9mT1aCHW859PDsVb4AS5_gbrExmx7pm70t9ntlRECXGMOXy3-mrOUqsKpHydEUBouIAyAyuy8b2sWuGKUySaJJbteuLMU2zh9aQE-NrABedmrP8-Jc1HqP9_TcYMf6apKv-cfZKuRvPNd4tjYq5lmpwPkaX4tCTazLfqICP2upfLq3YbOTBKPzC83sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ljx9bnZ5MBq1o15qtmJGj4Tmgjhv3D-kk7NMxwFj_m_IQbf8lalJLWmQHkxJRoTSmr9EM2Mkd07B69WcN0lpi88HONRIoGpqs7cf3DVBxrfLdibcv5gmirQ-JPACMJqXQcF5aNxbs99ZFCCbkloByoieDSzpJHB1SDHHku7ZNhvFRFGrWawngTUeaSDchsVAcqKL5f7NLYUcNv-jj4i_UTB8bmRxC9u2dXOJzGqznFCJdJy5C9LKB02U3ury5OO_t2wbTJnkHsW0LOuSlFh19PPPFnVS7q6bF1PcBpcC7HDlLt54wzobcQbK0TN_5md0uw3UHmHpTcOe3U0fxw_z1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
ترکیب احتمالی پاری‌سن‌ژرمن و آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/90463" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90462">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=ft6WRD3TknpYo2rT14TIty1a5WtCNmRN7bBjORrE_Qw9iLU79bVCypVHjBPQ9k4-_JN5bOokvBThlyTBse_DDMaSvY3QgKBMLXFuJ822nZjhncjSU5yselBIZxOtFCBXF-yoXDZ17qrczkcguzLT7rsiNo_dQYd107dmWbDvJ5RQbTgVgXpzmZK-Q2Xe4jOU5j9TDm5HgnZCKEM-3asXw7KAW4KX_oOXWCXXGlb9TE6SiObpuPuVbk5eq2zxd-bGXYFmB1kEhfgMtYzE5NFAjAaFSHEb-D5FTwrue2Efot3pIg7vJlJLc1q-dCBUkQQP8Jq03SrYgXUu4kdt3F-GjiZ5UaEAJfWw1K5zuX32DrW2wg6Nwlr5EFROtRcEDJUzpUQWASSrW_oHZMSffRUmN0jXqXU3mdkMnmJfrfB_r6R57hxEolnYM4H2qWdSrfFCtS84-lX_-WBQCr17iZ3qhzV3RePCeo-lghN4PQKooMWJciKBnQrQJGXG0QSCbuNA4vhpR-lpyvX3awsewvNkH3e1C2X5YdVcLnRel4XmRD294uoI6bQ9YWd2opTbxx7Jc5jGJ3S11AVaUY1KVw_NuzCar3K-mRoSKQep_2_pt50NUlhe8J1DRbKkztw2OFdC6v2C7Thb7L3Tg6-jCBcMC4d_x8Xc-Vy-omhpl02IjTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=ft6WRD3TknpYo2rT14TIty1a5WtCNmRN7bBjORrE_Qw9iLU79bVCypVHjBPQ9k4-_JN5bOokvBThlyTBse_DDMaSvY3QgKBMLXFuJ822nZjhncjSU5yselBIZxOtFCBXF-yoXDZ17qrczkcguzLT7rsiNo_dQYd107dmWbDvJ5RQbTgVgXpzmZK-Q2Xe4jOU5j9TDm5HgnZCKEM-3asXw7KAW4KX_oOXWCXXGlb9TE6SiObpuPuVbk5eq2zxd-bGXYFmB1kEhfgMtYzE5NFAjAaFSHEb-D5FTwrue2Efot3pIg7vJlJLc1q-dCBUkQQP8Jq03SrYgXUu4kdt3F-GjiZ5UaEAJfWw1K5zuX32DrW2wg6Nwlr5EFROtRcEDJUzpUQWASSrW_oHZMSffRUmN0jXqXU3mdkMnmJfrfB_r6R57hxEolnYM4H2qWdSrfFCtS84-lX_-WBQCr17iZ3qhzV3RePCeo-lghN4PQKooMWJciKBnQrQJGXG0QSCbuNA4vhpR-lpyvX3awsewvNkH3e1C2X5YdVcLnRel4XmRD294uoI6bQ9YWd2opTbxx7Jc5jGJ3S11AVaUY1KVw_NuzCar3K-mRoSKQep_2_pt50NUlhe8J1DRbKkztw2OFdC6v2C7Thb7L3Tg6-jCBcMC4d_x8Xc-Vy-omhpl02IjTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
به چالش كشيدن اردلان آشتيانى از حميد استيلى تا مچ پايى كه در دوران فوتبالش شكست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/90462" target="_blank">📅 14:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90461">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xduqks8hYdGuONE7vanm1gB0wZCD2iJ1TVq-gTxuu0h9FNf-qCvl3T2Miu09OSFdaO4aqAmh4AAbUDaS9JGej8nMI9epHkdCT5UuHwW6XKAA-N8U2T_FGhythyrotByW3EN2tkfsDS-DmdDfbo-JXdW7WOo5dOQ5e_XWlFWZo0k0iMY5XI6v0OeAzeunCIiBjZDx95nr2JvXeUPvMwf7CprhB67FMXOBSLq14x-9ChqzRWLTBGPuTBdT2XE7cQpKf-5fZBom6G-oBEc7Ubsm4UzG93BjFYwVtFQuIUQBIbX6mm9oydRLAWNjurenhjb7hOjBHvY8ow4RfONzTQIuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توییت جدید باشگاه کادیز اسپانیا
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/Futball180TV/90461" target="_blank">📅 14:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90460">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAPnXsdpK96idtRpuluDBkuvNoG2n94CenmhSEO4jlaCWh4AMzbe53yWkLUHLdIlnQGk8SJ30rke50M0dCQfBahefoG0vW8-TYL_oQ7In_7-UXmiZmBt2jQTvwToBbeV1zQBSVvebq5i20wCWOqyCXMzLEuuDOn_zA4CNs5I92PhGDlWEo45Dq5WpQvBhzqePkeAL4vtlE_GFa2f59NI17hROChdpVCvdHo1jk6NfgT_zZnjHme10XVrWdc6YkV4SGDhJ0KiGftAQIZ-QGCKbZUcZFfACpCouS7DGYOMtk-dkJA5QYjZKQtIIQX14Oo1FXUSfeWBfVOtoTbyhQzGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد فوق‌العاده داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان اروپا؛ رایا در صورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/90460" target="_blank">📅 14:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90459">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emVepJW_-MOMj9nLIMT0M4lCkhcp4YgYEdbDlbdVQrb-XinC0UZDy3-4On4nUCEDdKVilX9qDgoZnvwWACw6xX9GuFJAOQ_mBUxb0OaFSWlZcDjDyCXobWqWTTUSG0glCRoT1DMRpjdTIj9Ujb8ukRUNUkYz_dFFmygc3RiEJ0789wq-HQt0O50MmGs7CZM4A5f7P5k2di7oEj2YWr3T4oJBpGC3egAbPJpN0H2FT2-QFlj_sWg34zo1PPOw4JeD6eI9NEsZbyBw3Z4H4nZkiJRysLVRUcyXZNmQ8yJNA2ofHy8Ca3sS5hTA8RCa6FV_F1VJcjAs5EINPWyOfKaw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇪🇸
آخرین شایعات نقل‌وانتقالات بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/90459" target="_blank">📅 13:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90458">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🔵
با حکم دادگاه تجدیدنظر، شکایت شرکت امین‌سیمای کیش از باشگاه استقلال برای دریافت غرامت ۳۸۰ میلیارد تومانی مردود و آبی‌ها تبرئه شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/Futball180TV/90458" target="_blank">📅 13:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90457">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180
؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار دقیق و کاملی ارائه خواهیم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90457" target="_blank">📅 13:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90456">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXUJ350gLc9KtttlunSphgIKhqPM9uGz9fa3RTL2qm5prncOUfh2pfU7Wjm2WlStNq57plL3l_FNlBREXsHemA-8zl9AUalwLUKBkpFvPNfNCtEEyVXmBXnehCF8c_k8gzAA-65ZH2reKpaVV-1bCsAJ_T5fGi1DuZiPrSrMQIV9PmyvHk9uMyB75P4KvJ0KhBHYUzx8--XRx1kTWJh7yLZtH2QlQPNJu6XT4hKxi7sEPF4X7gGdzhD4rlVmP8Is52GHzNnZl7jOfRRlLG5H9L4UzAhSdwx-5G5__tirraMDhwbKGc1hJAc0J-BBTtjMNuNHBDlob7C2IMnRR61_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید چلسی خواستار جذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن را غیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/Futball180TV/90456" target="_blank">📅 13:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90455">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh2tiXxgvLjPmWKYQmRCFC5oH63Lv4BQryCMl_SeG4jpP6cJuatFNn3cZd11HUXEkXPFiXnRbBNXuaNgRwa29x86Y6V8fiFoLj9rZV1R0AxenDJC9dGvFmj-pd_ZqRC_7YabKJ0AJRnBE6UM5RugfU4ZlDUNQNxpIpKhsaL_WChCN_Knhr3FpkRzk8KXhYXjV29Tg4BChyMG43q4L9hNWcZlLxrDIHs2H7s1IcDcvncYBqGtwzs4JJP4572XkDeyvv050HH5X6mHW7M9EI9Z4wkOlTYXXbaZfR7Or0FFVhCeFYcDszr44mn0BwAUE3l3AonmuwX8u2U4e_SEZ8y2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
|به گزارش منابع اسپانیا، باشگاه بارسلونا در صورت جدایی ژولزکونده به سراغ جذب کوکوریا مدافع تیم‌فوتبال چلسی خواهد رفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/Futball180TV/90455" target="_blank">📅 13:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90454">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFx28MFBJrypr0UpaxCJBjvYySjwCFxdkWG8HR5-38iob2IjbKynK1WvM70MQOww1m84sLxJJRmm8zi5ipPS8taWrzQ5W2Ykp_pSo2an9CioeyEbigKdHea3zdDIq5eTsMl-OIu_5GumlZFu_rEXjNFemjUk1qhEoaa-AMVlA5aW8zy7eKJiA04mAWitNAnLxIDouUb7UaaVvy26-kPVy2673PYJTl8G7pfKplgDSIts_bBhqEpJHDpGq3cf040nKDg_4mUxlUanMf64h9SDnxLyE8C7wBKmMBvV1sQ2PFDh3VRVBC0yfU8x5eNCrfzXGIUtUYi92w0f_DWfSfZEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد آردا گولر و لامین‌یامال در بازی‌های‌ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/90454" target="_blank">📅 13:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90453">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH5LYGenwZZ32P98JdTzIp03MBr-AbIQwhMDra5Zo2aa85TjnPo9qoJhgae25ZCVhbCSzhtBNnCsHZ6rmUzWltt1fcC7ZGfAQpCM2hkmsCidzfcdvTE5UtXGeL0Rh4Tk5esORiiH3TLP2r41-AQTPP_yUh5EHliypamVSasuI-t7qXdfFW0dVPW-4aY6diWr49hpwESR4bGQVD-02Jf3-b1Fj-WJIxnD9QK7-5WZz8HjRW7TcnJm3-BasZA7UIBjF5kLmwa60TmjIxyu9XcfcvFVrj51XjUIqaoY3JAaMjzz8ybx6SKIIQkEtkF63T86eMpTh2vKG0ll0qqL7_h_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ ژوزه مورینیو به سران رئال‌مادرید درخواست کرده که یک‌بازیکن بزرگ در خط دفاعی را جذب کنند. از کوناته فرانسوی تا گابریل ستاره برزیلی آرسنال، گزینه‌های اصلی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90453" target="_blank">📅 12:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90452">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIvOHFCwFq6GjtFeQDLb9_YR0_0XVXQRlbkHvJxAvDaIs2PbOfHObgFDZ2OI8he_bWVmzs0zF2NZnuYE48_MFZTlgsoEPdESSGUfXmsTFQ3FlsX-UGGSqcYZtY-_uQFjBfRJyGHiXqolYctCrdwq3qg2GwrgpJAzCKF9fRGXdSffmJxhobJ7DlQiao2eC8Q0LrUKFwLVnbv8x4ZWqyoVzDzbTfWX1A2y445jn8eB7F941CztZ7huadKzaFqWyhGpc__fi1FHK_kAl1SB181F-sA_oJ8evL8Y2ejkuNkcCMkP0C_HbM5qfXrlsspC7SN6HHl7h_k16id371tYOE5pEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد گوردون و رشفورد در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/90452" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90451">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90451" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/90451" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90450">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W9BKryufdm0Qk-2EIOpmBq3pV9ntcLAVrXqIyjGsmvsvcdaiZ5Gm96JyMYDwc-PeXlQzAC_Nd24zk7vhEgdn8ERSxNgFYwjB9Ax6hylvMHkJ2TdtZty7pOsSlvwQpCWWPiXysF-1Q3a9p_AZbNS-VIVcjp4Cgs2r7zlYOtK_TTzPNnF78zp16dyuIBvJadFSb39uMgdcS5SC01XljkBWR81gVg5Cl8Bynlf7EoCsz7YjvVZDgIUpTxxrnuL5QeWY3qCU4wydONxW778JS8psmpurfd0GiorDk2yQW8WB6M-dhp1k7aGaWzuRN6iubXv83Hco2FN5UApYbJribmMFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
فینال لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
😍
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/Futball180TV/90450" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90449">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=iOBy4yW-bUtoeXlmI-Bt_913Q6p5ATZij-X-0puqORXwb9Dg0FA0XjjajYHBJiiBg4UTeVGdEzzChyQkzZ8s4fIYUPupz8biJ1-M3oGHSTL7aF4_M4y1IjOfYLBQcsSrDxOnMpnlptXQKKhyDMWZogEURR3y5G4Yp6N7CuwHHcSKtvyMCkABP2eN5B1cVlSuDCpnN-VXZRc_D35B52vgDNWECiNa3r7cxdbFJD64p408TT6G43XKCxsU8YR7YwCCfPQnISwC97M_M5ZX54OguWLHN_hm6F8OQoaYpbJzQ-agmvAoXSvIFV8PK18ytVuiFkWsWh1wisO_5t5rNidrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=iOBy4yW-bUtoeXlmI-Bt_913Q6p5ATZij-X-0puqORXwb9Dg0FA0XjjajYHBJiiBg4UTeVGdEzzChyQkzZ8s4fIYUPupz8biJ1-M3oGHSTL7aF4_M4y1IjOfYLBQcsSrDxOnMpnlptXQKKhyDMWZogEURR3y5G4Yp6N7CuwHHcSKtvyMCkABP2eN5B1cVlSuDCpnN-VXZRc_D35B52vgDNWECiNa3r7cxdbFJD64p408TT6G43XKCxsU8YR7YwCCfPQnISwC97M_M5ZX54OguWLHN_hm6F8OQoaYpbJzQ-agmvAoXSvIFV8PK18ytVuiFkWsWh1wisO_5t5rNidrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🇪🇸
وقتی سال ۲۰۱۱ از خولیان آلوارز درباره رویاهاش پرسیدن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/90449" target="_blank">📅 12:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90448">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/628ff40327.mp4?token=p87SMkknMQ03DSWBRiBEo38360Lm0Wy6-f_dDMknQUk--dJMehwjjKCB825DAtpQtm3VPeb1PdPYGJdoEPBGPUUqvJ4wVT9qdYaM4fpyCJQzKjYrwi0N31NzxLxydjYuWkOl2L3uWASvGfItV14XELtbFTQQBduLO99m3BBKulikR0bAEAxhSY7akr4swpDc2mZgWL-nVGW8mU_AvOHGjJLL-mhzFbP5SnLakbw4NYvRGCgtxDvPMeDHkQg4valYoFnbCo9q-jdZni62tjR95iNGvfL1p7hcBDtXrLkMrNPbmZw0tFXiiWBiIuSaHzcqgpdyDSmlFDAB8SA3WDudqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/628ff40327.mp4?token=p87SMkknMQ03DSWBRiBEo38360Lm0Wy6-f_dDMknQUk--dJMehwjjKCB825DAtpQtm3VPeb1PdPYGJdoEPBGPUUqvJ4wVT9qdYaM4fpyCJQzKjYrwi0N31NzxLxydjYuWkOl2L3uWASvGfItV14XELtbFTQQBduLO99m3BBKulikR0bAEAxhSY7akr4swpDc2mZgWL-nVGW8mU_AvOHGjJLL-mhzFbP5SnLakbw4NYvRGCgtxDvPMeDHkQg4valYoFnbCo9q-jdZni62tjR95iNGvfL1p7hcBDtXrLkMrNPbmZw0tFXiiWBiIuSaHzcqgpdyDSmlFDAB8SA3WDudqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مجسمه‌ لیونل مسی، با ارتفاع ۲۱ متر که در کلکته هند برپا شده، قرار است پایین آورده شود. این تصمیم پس از آن گرفته شد که مهندسان اعلام کردند این مجسمه در برابر وزش باد تکان می‌خورد و «به‌طور خطرناکی ناپایدار است.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/90448" target="_blank">📅 11:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90447">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=n9lBBYWmQEkvK7JTiVMkAKnMN4sy9AYSPwy5BZj1PJPFJwU9S3gsNcbL6Ib-lr4AfaGqL0OdTnY2lI6963MGTzXZzTPiIEYOWRZYeYQlcnRl8Z5VFde7f5kCxr00fFKwjVnWrvCwYuRQGeUzxaeMfr7GpWkxZrcNdGVzf45ICKQg8-QC4Qs3LpDt_gFZo-FBjI88h2Sn2EOizpVSHvveGgOTnG-PW1UaWbrUSAAfxrRmyAlXwpQudTS9cBJCNGsSMh8KrkBsswHQsa74vpUM2t5k8OOyS6-StAJ-RDyqmZiis0TopFq9QOf8cE6uYzEDlXuPV6xhe16lV1fDdPW9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=n9lBBYWmQEkvK7JTiVMkAKnMN4sy9AYSPwy5BZj1PJPFJwU9S3gsNcbL6Ib-lr4AfaGqL0OdTnY2lI6963MGTzXZzTPiIEYOWRZYeYQlcnRl8Z5VFde7f5kCxr00fFKwjVnWrvCwYuRQGeUzxaeMfr7GpWkxZrcNdGVzf45ICKQg8-QC4Qs3LpDt_gFZo-FBjI88h2Sn2EOizpVSHvveGgOTnG-PW1UaWbrUSAAfxrRmyAlXwpQudTS9cBJCNGsSMh8KrkBsswHQsa74vpUM2t5k8OOyS6-StAJ-RDyqmZiis0TopFq9QOf8cE6uYzEDlXuPV6xhe16lV1fDdPW9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
آخرش کی برنده میشه؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/90447" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90446">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=sVyCB0AgD__uQjncilmASWlrQZwQANE6um94kwffg6Z_mAAl17WavjZ_AXlAwPHTPstHdSYTGZOzQHbUF7sALt3baC9F-tH8kiAMi6ZF0URfV6u3JOr3b9ilBNGS59a0c2bpnQyOMQCJEPHG_bdVs7400pLYRKJ3QE_O5GGEHUCpqEL_OMWUVwMetpIGzzjB294cJf44KmyEBeFGV74qTsqW68WrVfoLrrzF7XO6LYgqhXREx2gpjvzhiQJ-Imc8WOrVEwB3cQdjpqcVqx7MmWP4FPjSIE0AdR-3m-ssAxtFAubWsbp0uHDC9-3H-dmnKYhhIbKsBHavbd3OJD0jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=sVyCB0AgD__uQjncilmASWlrQZwQANE6um94kwffg6Z_mAAl17WavjZ_AXlAwPHTPstHdSYTGZOzQHbUF7sALt3baC9F-tH8kiAMi6ZF0URfV6u3JOr3b9ilBNGS59a0c2bpnQyOMQCJEPHG_bdVs7400pLYRKJ3QE_O5GGEHUCpqEL_OMWUVwMetpIGzzjB294cJf44KmyEBeFGV74qTsqW68WrVfoLrrzF7XO6LYgqhXREx2gpjvzhiQJ-Imc8WOrVEwB3cQdjpqcVqx7MmWP4FPjSIE0AdR-3m-ssAxtFAubWsbp0uHDC9-3H-dmnKYhhIbKsBHavbd3OJD0jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇿
مدافع نیوزلند رقیب ایران، در ۴۸ ساعت ۱.۵ میلیون فالوور گرفت!
یک اینفلوئنسر آرژانتینی پس از بررسی تمام تیم‌های جام جهانی ۲۰۲۶، "تیم پِین" مدافع نیوزیلند را بعنوان کم فالوورترین بازیکن جام معرفی کرد. اما حالا پس از چند روز، تعداد فالوورها این بازیکن نیوزیلندی از  ۴ هزار به ۱.۵ میلیون نفر رسیده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/90446" target="_blank">📅 11:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90445">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKb6Nkwv6lAFs7N2f3J26ouPEVn0SkEzqQxNdmNbOY-c4_q-2A7BjSg86YzuxobodPgT0dANwj0-8PdDAuFniSzgSj4zfnRgbwAkXKUPpFAmlPr7U6k9I48yHctkLqk07DUo8k4Uv8GbKvhnEYNt-STHKMxxDZtot5k_kawSNPlRssPjBn1Qhz9Y84Kl33mp4gf1LhTd5kau0x5Pr05pD8aU4E4UQOq0JCPwhtD3xRliAQXReg5iEmQQigYufFSBcErBx3NOqABlREPgx_hLoo_KMQUTWezDsdFkYR8__nwkAPXwEHGOr7r7We5EoubmUck4TiVpsg9a24WkDWF7-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کونده با پلی‌استیشن‌وان در اردوی تیم‌ملی فرانسه!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90445" target="_blank">📅 11:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90444">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
⭕️
کنکور سراسری ۱۴۰۵ در روزهای ۲۹ و ۳۰ مرداد برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/90444" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90443">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPQ1ulunq108Zum4ktxhU8OFYdZPdIuLx-FoLpqBnaVJOKtK__myxXaxXpbGN5mFmN2TpIxc9cEzuoZFjFsxQbHkc_zPeM39WHs1LJBSnlJcU3-J6socU1ctHwF5LlzbQmkk6vLvF6ejK-LsCEeKatld-RSjpMylI2z-fqEUkWgqQFDXdCV0ruZvOLlyqN6Zu1YvSJttq8rEP4lkNYTKpFjTuG9B8J4_Ot66_Z12jnvssFHR_6pOrwiWQh_tHGID1LP_vI7KW3FKJ0nvpNIklESgpuWjlRv3EjNrYdJMNHzmCjT15ZiOwg8gx3pcz91EGMYEkXfADZwR_NAcYJ_8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🏆
باشگاه‌های
قهرمان UCL بدون شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90443" target="_blank">📅 10:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90442">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=R6LqmYslyu74hWZgFhsrgrsxsWux0_cs7Auv6M2WqYPoGLOPKhY1_ru-RjAMDweNsvyGEtuGo1udgolX_v1E7MYv99IQ_G6sKoQLJLK_YD3M0mYmeU9CPd_VEqwWC_fXj6HQR-_6pCJ4wCfBva5k5OkaK7QH7ngNVGA2YSLkftt5lXjE_vX9vmwMqSJW6Cs8iYwa6cqU48QcqHSBhDUDFN11-MoCUX4y_o70vZ_6mTIZLn-McV2enxr3_Vcl_N2TRd80Krx5II6qIn4t8wTil7LmZNcXPQ7tBQWAEexgmOWeZBDKeGQvj45m-pB_GeU0kuXGN986YD_V3_6kQ1NvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=R6LqmYslyu74hWZgFhsrgrsxsWux0_cs7Auv6M2WqYPoGLOPKhY1_ru-RjAMDweNsvyGEtuGo1udgolX_v1E7MYv99IQ_G6sKoQLJLK_YD3M0mYmeU9CPd_VEqwWC_fXj6HQR-_6pCJ4wCfBva5k5OkaK7QH7ngNVGA2YSLkftt5lXjE_vX9vmwMqSJW6Cs8iYwa6cqU48QcqHSBhDUDFN11-MoCUX4y_o70vZ_6mTIZLn-McV2enxr3_Vcl_N2TRd80Krx5II6qIn4t8wTil7LmZNcXPQ7tBQWAEexgmOWeZBDKeGQvj45m-pB_GeU0kuXGN986YD_V3_6kQ1NvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
اردلان‌آشتیانی کارشناس فوتبال: سن و سال تيم ملى خيلى بالاست و ريكاورى سخته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90442" target="_blank">📅 10:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90441">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLrqzCZABlAsEgHurk38trN8c36IyOTxpDAYbcr8VsShFTg-jT_FY9BN-Mmec0dtRcqX3roS7O24GolesTd1vMMD556UK35o12SUqLmj_qxTOtDwwyCw_xma72sNud53XKp3dOtFebSzF-ObrmZLr9iPwmM5eTiAWIzTMzNkaJZtdRfyVxTKARfWzJ7A0s8AWSBNTxyAZN7YQjMXZ1WXRtQhwPCCZrGeL4_mneYA6JraVrDP1Zi1oQmUyEpkRKW4K7KFDIudkiFjxmfY1_m-wTRf8en6KshLFNq2aPVTgPfxm5VHs2D5miJHFi7u4msVmK_S42aMFKYDG2cTklxegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90441" target="_blank">📅 10:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90440">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=Q_m7TnAoVil0_p_EYJETjpX-0zVR2cmY039BmMZm8OdVFAgQdd_l_PrTe1bUsZ71ZLb_5EuaqRDeIixX1g3kCdbxuF2ZT1ioYWSycE8B4nf1FkQrKcMdST43kDW4cQRd9NCNsTL8O9vs0uIxysPYhWC5MJDA-AjzktzuaLZ_Ao04qoR3sW55xfvzk0bu-mFAPUYKl0f-pBEGrLoufpsQJtXGI4MXkU7RkEYCL6RysKLJuqgnOO9NLuhFQeQMt1y9iW0CjxGArf8TVdWCbu1SMkV746J-ZZEc9NlitmlKm5Kw8pwKW-D2vrTvef6uD4GrVPp1y0C1GWnnvQxXE-9pkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=Q_m7TnAoVil0_p_EYJETjpX-0zVR2cmY039BmMZm8OdVFAgQdd_l_PrTe1bUsZ71ZLb_5EuaqRDeIixX1g3kCdbxuF2ZT1ioYWSycE8B4nf1FkQrKcMdST43kDW4cQRd9NCNsTL8O9vs0uIxysPYhWC5MJDA-AjzktzuaLZ_Ao04qoR3sW55xfvzk0bu-mFAPUYKl0f-pBEGrLoufpsQJtXGI4MXkU7RkEYCL6RysKLJuqgnOO9NLuhFQeQMt1y9iW0CjxGArf8TVdWCbu1SMkV746J-ZZEc9NlitmlKm5Kw8pwKW-D2vrTvef6uD4GrVPp1y0C1GWnnvQxXE-9pkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
تمرینات فوق‌تاکتیکی آرسنال برای فینال امشب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90440" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90439">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwcip0_qm6shz58rRCa4I0da6_bTWBn7Odn4BNZBClf5GD864GuJXjw6WfQeiC9QzrPK4QaxqWkflvHcMorLyKqEM5D9ZHWX-t69XcEo0PdYdcy4ONn2u0KIwT4a4emb7Ohz9Ax4HLzSb_VLnB3N3ivR2lgiqRBfvmS1dHBQLmHcNPEbCIMsqWqKuevu6n2w4MpsS8wMd_oaMtmpDsKCrhxHsplZNyT8xqZ4PcRQhREqEgM_uU3rLllpWVKficnadn4i1BlfN32u0nPn1stXThdMx8ADo1BEGSrVaKv6tbVoTSq0U3bcTULcffsmDEa-zrJysJw1s5AK0onnUIxrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار یامال و دمبله در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90439" target="_blank">📅 09:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90438">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0qd4y0Il4EifVhYBdK7Z0dIAUSHZQB30o6GgVtlITqzNysY3qZdqzEJZnr0xEF0PRCjr8pT5fUcEzXEuh8f32g8YTbVN36CYRlqJlgroFudEh3NuWl-0rSdYal6IOBQWZpZ6RaPcAVDVdTIV1JZE5FNYgM3fVoaMZdY5OTHjALbtCxhDRY2y6iEhMyc1dFPmGgeFwvwkIeWUpjEA83U6ET9CL-S2ztdgbIkEL8vnCF9hibLJKT1CvwBiJce8N4F2CnzH1Ap-6qbwAGkP32bYF2Q3I56WI-3td-Ng4c1GD23BTKMQ5MO5T6pY_aaUh-ywmwP1ml1jJ_3mrDgDSRQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آمار تقابل‌های دوران مربیگری فلیک‌و مورینیو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90438" target="_blank">📅 08:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90437">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIQkGOQ5s5t83WMaFuyYbuUBKTxo-DvJryzzr2hm9l2mx4YKHXZtU4KQ5ZHLOfS5wlL_wh_D5q6oeb9E4JkDRkBxEbGeDSMNvQwB6TdVGqKJT5KlSygkpAKAMjsHNw2Jfp_uLdlkECKTmkykh5xIELoHn-mKFhuLv5Ud_5ub3aO4YqKIebo8seb9On0GeCHjl048YRtvMyIZ2ajUPhygmKJFPUYaMHTjxgWrp_d1PfmMnAIzo_rwvup8Qk6jJ8x9MdGtljlVa3RHpt8Pd-bBMYdYwxyeqlcWUJuuU6Z9H5jrS4MKdShzCGCzoTZuXZJCNk_1mnOOiBfwSQH5N-JPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و عملکرد رافینیا در دوران فوتبالش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90437" target="_blank">📅 08:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90436">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90436" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90435">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_iSDQaNz0h0DAqU4Tj_rtxMcrOZMXmzL_0Wsz2_CGhF0pkkdctQEeBIGAKykVprcLvWXZHlO6bRoWFnVu3yq0X-YX557n8BUz_XWuQXdOmC7SCjYZCYlsbQr5MKANMLc-isNVTcAKFi2PD1XrkZdgsHLhn-nILje3uZHKuYa8Jbk7kkubVxcmhUQrBYnOqfy2hsd1MjbY7dQuf3aYbNPIUBDeJAxgG_WI590OV3EVDOS7MDAn0dC3yKiYuWdz-SP70dFAyhVgwxKSORJ5gpb_Ik-MmmSqYVzywHoCFkdvUGdSzRwNI-KCcSrZdUTmA8NaDJHDK-V0guyczCUiXUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90435" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90434">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evDO2Jv5SPH6uj6jMK9dSF_PfjzDEIWEy1xCuUIkLQG0T-zAr0mII8XzxvGzipjXVMx-Zif-qhgnv6kVYb46MDf1p0sjGMa39wltQUmkm2P_0MYwU6gNyQXuUmXaP5Jaj01yL_0DrRID_a2mrAuk67pnzIZBYk3OiCNPsrZy3H2RAneuLd-reu7qCTgaPUR0iEum7IgBGgqtNlkoqY6Ln8Nwm-Jpk_P4m8U7lBswasd87_JKBSyl_e1pKiz4NToy2MPisxqIGbv_EFDsHj3zF1JKEN6rDjau1wh_CcbUfF6fKx0qMamXzlwyGpKKtVsMFzdEBRXz1TOQtNVc1eUqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساپینتو با پافوس قبرس قهرمان جام حذفی شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90434" target="_blank">📅 00:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90433">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مجوز حرفه ای سپاهان صادر شد و فردا اعلام میشود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90433" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90432">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_xhHqXpFIovzN8gWPWk4SPEbkenTnljETNE-FV5nXDHsc6DgKK7CRh6EsvDZ11cgdZyRaYvX4HZJSWPj1msTzm-U8mf6Hsy8eKEDb5AJGKsHo6NAHBcZAZrUNZ-yPjzYomAPiVFNGCa4ERQ_uQaJe7cHg13DVYbWeQuoSDVg-3n6pfq7FUtcMkpmY4oM3zbDgKJ8zYTwL2K6LhCBWWpSeQlGg9yc2Udy3O8dHdvePkvRN9z6vcq2phgZjWrcONySBmDl8c5F2BWViggDH7opLs_UavTVkaQx6BGxc2RUZ-qDqSa6rEwWaQrUo4BLpxb2jCajsLISQanp5SsjDiB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری و رسمی
گوردون با قرادادی تا سال ۲۰۳۱ به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90432" target="_blank">📅 22:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90431">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzfutsDja_ahcN3jTHhKTng7zEf8mm-nfeotqQPK4_1cGyt6JosmlKoMqykSr7yWGkUCawy3uL1TsudkpZSN66ANDu6mDTMcGu5kvTrjtRHZ86ill3Qim6y-SjL_uvW7JGej99I33ZSuXIeTQ-BG97kdyCLHGm6s-w5wtXb6vwwRnvbJ4hlPHhP58Ty6HqQqV9nwO0Y3xSPqg6lkrUveqLb0cqvj11WTL4rr2cu1JgRDsHwAsmhzeAU98D9NILEKsSPB0TaI2cyX1b0u-8EGwgQbcDqJGXDwM9A-MZM8qA_OEubf7Mb45Wi-dU-11mc0JzVDhbE_gEKkAFRGzkqcYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست دورتمند
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90431" target="_blank">📅 22:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90430">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pevUXZMxh2oyBxzZR4dYWFOqyl2z2fhchTVtdlVAElZhfWUMSZjEbTgATD8GzHJdCoGBIA0b0GPFUkxSi72j5q95wL-FYWeogZ5mjkazP69lHQQLSFC9AOPmvnwiLWWYVo-9J3PqQ70dy0vB54lIUdba8CLJDon-Hjlgs8L84wQsY3gdNjRb3kCAaJU8V-FTfOEJd9ScwqsqZI-j5rOKrYep6wFOXRHzkmUfn-Lv-v1OMzSE9_6csAjHrsCg3rkUn8mwatthL2VRt3HSAw8oB3qySbMxY774uRz3PUHTir7knvNT6Y4j9RSb-O5Se6IdG9W9nH8z3NPL-uBqbZZ9tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتلتیکو مادرید بیانیه ای طولانی را برای روزنامه های اسپانیایی ارسال کرد:
خلاصه این بیانیه این است که اتلتیکو مادرید به دلیل نحوه رسیدگی به پرونده جولیان آلوارز از بارسلونا بسیار عصبانی است و معتقد است که بارسلونا به جای مذاکره رسمی با باشگاه، از رسانه ها، افشاگری ها و فشار از طریق خبرنگاران و عوامل استفاده کرده است. اتلتیکو تأیید می کند که این بازیکن برای فروش نیست مگر اینکه بند آزادسازی کامل را بپردازد: 500 میلیون یورو نقد، و او تا سال 2030 قرارداد دارد و بخشی از برنامه های تیم در فصل آینده خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90430" target="_blank">📅 22:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90429">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎙
لوئیس انریکه:
به آرتتا می‌گویم تو هنوز جوانی، پس بذار این پیرمرد دوباره قهرمان سی‌ال بشه، چون آینده بزرگی در پیش روی توست
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90429" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90428">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsukUYov7H_v4I2VlLaKQtixoVDBNb1sz-t4JJamyXIISWNA_UIo94qVPy9buoJxWLrCJCppNWVHl1MJyxMW9PlGV9WMV6pDNdqKVuaDz_5Lg3NRIsxbL-Q0LvydwlZUvNj7Hg1mkOjiJLcFeLFsetwRg0e9t5d3FfhPVyMZ1UDYsnKcWT3aAk_WAVyicLno_bcpuTQNzBzoRqExUviR-ElMbn7phIIFBvtIO6_esQuXNtA5fcFxL3qPym4uOd8uRt72j9cATAPPQh775Jpm-Q-Q-MC4vdPyvB4sTHRJAn7CRH8DFw25-4vFtx1G5EzuXTTb4t_QE0mNY_Ds_yGBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاری سن ژرمن
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🏆
فینال لیگ قهرمانان اروپا‌
🇪🇺
⏰
شنبه ساعت ۱۹:۳۰
🏟
ورزشگاه پوشکاش آرنا، بوداپست
🎲
با بیش از ۶۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی و بیمه صد درصدی
💯
📊
نگاهی به آمار دو تیم:
✅
پاری سن ژرمن در ۹ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
✅
آرسنال در ۱۴ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پاری سن ژرمن در لیگ قهرمانان ۲.۹ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر آرسنال در لیگ قهرمانان ۲.۴ گل در هر بازی بوده است.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
⏩
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/CH100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90428" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90427">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=miDpONsHAonNTFnJt2XJUZ_lHqY_t4C1EKFsL8Eg2T-ddbQdwt7w7b0_-BeK6J2_SdHRIPBwQPm1xESbP6TvNYqCRhXDoRGJ0JpRJhXdJrwfGG2hA_M9WiR_4Pt5K3IPNuR1Ju9AMoGKNnuSWehcUjLE0JX7K9K4CX3DQ40jSmkI88IbVCTgSC6LZmWNgLxN6vri9SqJJu7HxAeEvJmagkfPd3p0cBD-HNRXeF475_BCAlCB5ki9ELct9KVkZodlKMMStSVgMjcVshXm55tk1hR_1uFTuDrVVZYalI9VZ-aLdJg0vFvji7Pz1tXgjLQ0RK_0S6-WVkSijyanNG-Cdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=miDpONsHAonNTFnJt2XJUZ_lHqY_t4C1EKFsL8Eg2T-ddbQdwt7w7b0_-BeK6J2_SdHRIPBwQPm1xESbP6TvNYqCRhXDoRGJ0JpRJhXdJrwfGG2hA_M9WiR_4Pt5K3IPNuR1Ju9AMoGKNnuSWehcUjLE0JX7K9K4CX3DQ40jSmkI88IbVCTgSC6LZmWNgLxN6vri9SqJJu7HxAeEvJmagkfPd3p0cBD-HNRXeF475_BCAlCB5ki9ELct9KVkZodlKMMStSVgMjcVshXm55tk1hR_1uFTuDrVVZYalI9VZ-aLdJg0vFvji7Pz1tXgjLQ0RK_0S6-WVkSijyanNG-Cdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو جدید اتلتیکومادرید علیه بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90427" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90426">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3n7kxjpf3v225dkNeu-Ik8jhEDNuzpAkF28CwkT_nWbFpTfNtyuA5zQNAQvDNoG9HBWanXmcPVJCv21A1jDXEoxrzfGEq_UG6lJqo7DQXRZWZHXbOJ3t6wYlrL0ih5zxIJyFVA3Dmr531RBUR4P-8YYuPr60bp8IFULl2ikj_ygPEI6rjqze178huP-xzfaos-jYU_l77Es-GGA8AdGIle9nS9Deco8xtqdar3IG2mkBr9PrAFmxuEjYlePsL1A_OWKPvvE7tZ4y6H1KmdoCNYZpItbfXqBFmZY2CI3rlSqwRVU8JRy6nSbY8baZllQw1g8taEloWtrwGLvMxVzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:  برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90426" target="_blank">📅 21:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90425">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تیم ملی ایران موفق شد در یک بازی دوستان ۳_۱ گامبیا رو شکست بده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90425" target="_blank">📅 20:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90424">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=LAz01kq-nec2CqTh305UWlLw0BmZm8HhPcgS4yF16IwiqSjMngGrElW3M-F7YbEFqrFhs5ZvNOY7hD6Tsfn-KBImNsseAIhm_J8X4AYFHKXqki1QOb1SCeZAwp1dJw1ChDeH1fxwNqu7sBgDAonNjto33NlPIGcNKD6_T-PRgIhL53W9j4N01opVeFTh6WsRu3k1m1gBKLEXva5uwxSai7tq7LDcdUohV6fLf16DD6Q57cApilkUUlQ19okaZKGTYkl1_FoMAWbcPmrdR3pF3zKd7n-JDuv4jh7zyc67JJ5S7F1L-7wzOqFng4QfgdQj7YlOtnid6dVZ9T_wP50DTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=LAz01kq-nec2CqTh305UWlLw0BmZm8HhPcgS4yF16IwiqSjMngGrElW3M-F7YbEFqrFhs5ZvNOY7hD6Tsfn-KBImNsseAIhm_J8X4AYFHKXqki1QOb1SCeZAwp1dJw1ChDeH1fxwNqu7sBgDAonNjto33NlPIGcNKD6_T-PRgIhL53W9j4N01opVeFTh6WsRu3k1m1gBKLEXva5uwxSai7tq7LDcdUohV6fLf16DD6Q57cApilkUUlQ19okaZKGTYkl1_FoMAWbcPmrdR3pF3zKd7n-JDuv4jh7zyc67JJ5S7F1L-7wzOqFng4QfgdQj7YlOtnid6dVZ9T_wP50DTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم ایران به گامبیا توسط طارمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90424" target="_blank">📅 20:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90423">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=EIFLSmqS9HIiToZeiG3B69sF0-YcBp_oPshdlwB-JS01UrlADDvFzvhiogHb5aXaeQ-dOq60naMnLSTRT8sM0SqjIvAF2ElQ1tqMr4n3SEujMCe99Jiboq1Dr1apamLodlWCUAKgspmLQNu2Txvx_f-DldpXhCjLdakKuEyUf5OVkeSKiBeY11_Dztvo3IAhhZ6Suk-jSA2SrTxBLFnL2OzPs4uTwiFzhD3UZjahz5WXuEiwr_YEhoEUOLaVQAtfpYuswD4qo_YPkVa3OZEo36AS2HD5sutcw28axpjEmW100y_rdN9ZyeiMd8Z-84a3XH26OdTodhlDdvYqcty50A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=EIFLSmqS9HIiToZeiG3B69sF0-YcBp_oPshdlwB-JS01UrlADDvFzvhiogHb5aXaeQ-dOq60naMnLSTRT8sM0SqjIvAF2ElQ1tqMr4n3SEujMCe99Jiboq1Dr1apamLodlWCUAKgspmLQNu2Txvx_f-DldpXhCjLdakKuEyUf5OVkeSKiBeY11_Dztvo3IAhhZ6Suk-jSA2SrTxBLFnL2OzPs4uTwiFzhD3UZjahz5WXuEiwr_YEhoEUOLaVQAtfpYuswD4qo_YPkVa3OZEo36AS2HD5sutcw28axpjEmW100y_rdN9ZyeiMd8Z-84a3XH26OdTodhlDdvYqcty50A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ایران توسط رامین رضاییان در دقیقه 59
ایران 2 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90423" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90422">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7455525379.mp4?token=vhyQxnv7htkLqeRu6GfyY3tpqka7sNbX_PVWYO_S0h-jS6mXh2ynxwf3mFuceVx9KTBh0ui-e8RRioBWVcKaYxlQKZvaTSskyDtYepP3x5WELfR49RmKCrDpqHMcWcfFJUYRwOva53E4eWd3kODBg5P7r5UEx7_E6eLVZrC1AAc_hL4xiiQon7uc9fxxcmbzRgEGd6nb4BoCUz4pR7_0DGm1OKfJrWh46xw96W88uX24LN3dQrBdN2X4eIb--JssJ_4iW64IyoELzNWRgw2UtJnJB6C-jkKyB5RShq1_WaP3bH9MhpEhDUmvtfsSSwGLUoqnB-TbjrMRowW6ZdFHtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7455525379.mp4?token=vhyQxnv7htkLqeRu6GfyY3tpqka7sNbX_PVWYO_S0h-jS6mXh2ynxwf3mFuceVx9KTBh0ui-e8RRioBWVcKaYxlQKZvaTSskyDtYepP3x5WELfR49RmKCrDpqHMcWcfFJUYRwOva53E4eWd3kODBg5P7r5UEx7_E6eLVZrC1AAc_hL4xiiQon7uc9fxxcmbzRgEGd6nb4BoCUz4pR7_0DGm1OKfJrWh46xw96W88uX24LN3dQrBdN2X4eIb--JssJ_4iW64IyoELzNWRgw2UtJnJB6C-jkKyB5RShq1_WaP3bH9MhpEhDUmvtfsSSwGLUoqnB-TbjrMRowW6ZdFHtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول ایران توسط آریا یوسفی در دقیقه 47
ایران 1 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90422" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90421">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90421" target="_blank">📅 19:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=RIuvJj35oii2CUjbSC5szEKQ6nmG4xH2hmJrotgqKGiq-Cv2nNlM1HEtwjaqEzQ1NlkHC1iKVImfauyPY4bsov-Qv4AW5p7HRGyMP0xGFxtCNkKUC69c0hNhdVrZQf4pSnxmRwcihaUz7W6d2DVSaG6iy730FpeW7h_gK-QeNh4GHNEfRUMmQmoPo2Wbm6Vo5xXIYqmnL_kvmu1IbwZpZ0WvQY4meBO8SgaLdbP2RnlsMnmomR0aERY-I80JsvuGY3EjraldGIHxobpQY3HutIGfE9TrDuCbAlZ8r6vMKzl4_Cpf7NxGe7rP9Jptq8p_brW2A3hmEWbPAaC4hDq7Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=RIuvJj35oii2CUjbSC5szEKQ6nmG4xH2hmJrotgqKGiq-Cv2nNlM1HEtwjaqEzQ1NlkHC1iKVImfauyPY4bsov-Qv4AW5p7HRGyMP0xGFxtCNkKUC69c0hNhdVrZQf4pSnxmRwcihaUz7W6d2DVSaG6iy730FpeW7h_gK-QeNh4GHNEfRUMmQmoPo2Wbm6Vo5xXIYqmnL_kvmu1IbwZpZ0WvQY4meBO8SgaLdbP2RnlsMnmomR0aERY-I80JsvuGY3EjraldGIHxobpQY3HutIGfE9TrDuCbAlZ8r6vMKzl4_Cpf7NxGe7rP9Jptq8p_brW2A3hmEWbPAaC4hDq7Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول تیم‌ فلک‌زده گامبیا به تیم فلک‌زده تر قلعه‌نویی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90420" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boEd3Ph33M7SHqMJ7iCqvO6uEsKtGiuTcFoxYRaWQ8NOwdh2iXEGgIAQk5jvjrYgu_FFYv5Acglkfmtye-ksFb43fp-g8ulyeCRE_APN9sAg2_-hq-ooQVFVI9E7zaHeCSPgduLHnJod8Ruo7SNx_aqqlUwG3K_2BSmO3t58QBwn07s9ibHU_bATA7CWnrP-p1NstYMA4a12bFEf85L05cLnki7sJrPo9-r0uBG2eEStnp4VdG-6ut70QdNLLg3b5S5zJgP36eRRiau0y12B4O9kIKj8VvHnzhJkNAkLrRtPApUEb6JvF7SvgPCfV8fZH8mukPjgUAVqDp8ueZXkOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:
برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90419" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90418">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90418" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90417">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKa38wiCMitp79DOG8I6EIIfKpmbE8nY9aPF00OHpEk6tXN0tI6JazpllGlj1mlgoj7cx5_t8vF7ge2kQqo8f8ATzI7VyrrR4Mf04TvHkSTv3uk_V1mSFD0nmzU23JTlZNQj0KGazo_yXgZFy5572VSWGxAIw4O8XHrKU36TQRoWrSUEm2JHpva48YzxzZwpAKkxXr1fETCKwOJlbgHovNDARqdrc7nEgw71RFn2s9Egt-aRsLtbwFtriMSUbT7uHmc_zpEOnMU4IJ0eSWMFTVhOnkrj4ZK9_ecsP6YIkERWltvWwX65Nl7TH5bur69XgkFNriDWl1FLXQTplGrKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g8
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90417" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90416">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awGiSKuCPev_oCRmv4lCHfqVWE2YF93tSxkiEoYVOHZ6aoV5VyPW0c7jLBDf9c8dT_-2uBXND8Vgb0O5ZA2oZ3jwh8gZFIC_5Xq_y88eH7e-84y6Ci9fCVGDSqyTrTJdPNfyr-i2F5TEAUVILQ5FZclIB_eEm8EdUTm0cPpy-AC9y3iPI4MnIFOVJFL7PLNz55MczLKMksAR68rQbyjzSAgVLyt_MAxOA3ptsIeoSK5R8OX4ftldBuvfl8us7T6xaq1tE84VhuyJtlXiG5BGvz9gOLwDQn2K5sH21YQryOMQVsSDrjL-NWglaEL730hyAx4Hp8fdJFDDc6XqxiG96Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
حساب‌رسمی اتلتیکومادرید دست‌بردار بارسا نیست
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90416" target="_blank">📅 19:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90415">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTgMC8PjzShm4bFrLa1JFpE7sY3-Dw3cM_xbk_xlad8-_Ps6wmUKqXKEYqHYv_PqDzJG6YWW2oZYe89hGy4KNcOL_VuaHFgPMrAh4ZRjMqomWzvEd3Ic2tTzpr96uc_ieBHB4sA1vIGRtY3ovHG7Vmv3E9atdsI4xEuYu_tb-BnrVbHS-MDh1UrSmwgzE857cm2nUD6-wj0K6717d4WwGytESXu4WeeuSTVub-_EM1eXpqHln53AZp2D8teXQYPC_hwZX8SQbk9hFaDf_c6xaNJo03955rlsBdy-iDItLLTBj3r4g3RFhvGqaCcyEiNCW4vPeHnLdynPP8hwn65xWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90415" target="_blank">📅 19:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90414">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE-mu2zWia1yZB_OXVJ8v5VY2mrancZ7dS4CCOALa7ZTuD9dvc9CD81cWFRTDj1QmHUnl71R0WhlM4o-j_vt8JbTuMH3s8BzpR1ZjbXRPril1-UGwIkyyqokOelgkdEO0fddK_XICuYNrkzhHldpjWiIKEC6uSLvq_HAfj0irj_x1wluo6UcTQbcIXiIp1qfewPh6TAnxVDIpIaAsfPRCH1rHr7au1zTqmQ6MA2hLCVMMTFKdg58BitoAlm3xgJrDr0-DwjJtsWSL0d5DvIinO0kBZ_gy5cjh0lsvK444JpeGyJd7Si4j5UfXn0E3Jo6gFvZ1AZ7pqfCT6f1xbJfgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90414" target="_blank">📅 19:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90413">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
دونالد ترامپ اعلام کرد که محاصره دریایی ایران از این لحظه به پایان می‌رسد. همچنین اعلام کرد که تا ساعاتی دیگر تصمیم نهایی درباره ایران اتخاذ خواهد شد. به گفته رئیس جمهور ترامپ، مواد هسته‌ای ایران بزودی از مکان مورد نظر خارج یا نابود خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90413" target="_blank">📅 18:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90412">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ایجنت الهیار صیادمنش اعلام کرده در صورت تصمیم این بازیکن مبنی بر بازگشت به لیگ ایران، اولویت او بازی برای باشگاه استقلال خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90412" target="_blank">📅 17:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90411">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ite2takOfq67QhsTrYUY1hMJONjOdSPtXWraMns8PcBohIEMr_VLTxoKRgrjtZ_A8J-_fmo57UZZbXR-oHur06e0I713xbdy86Z-jZ6lcHSt40CFM15cdlZz4ivjJsCCGmr9QpFRqOh_HYEYTrutJlOt9WLLgFMqHYhtguvlBbKrDi9m9d3-5fBOlz_f0iv1pvZkZJPOajvfIXim9uPbbQPLMVHLVyRiY83ZTgx8421yJiP9BFSm9rqFfFIwn0k3AKpELM2tCTX2QV00s40CS2O1jBu76UQCjrG0IqZ6j5eVWoXAcnJvlSGmP1IhLYhe24GgJJSI1j_jXmrO5o13Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر آقای‌گل‌های تاریخ ادوار این مسابقات
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90411" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90410">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">Barko VPN_v2.2.apk</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90410" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90409">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90409" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90409" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90408">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97be903d17.mp4?token=oTNgMRKqHWDIfihcCY2SwuQv2XZwcfa9F3eAE05ev_bqM1vWcaGng6m0ye6awQpYb8QRn9Ma9l7u4dM6hezYNym4dTwW9yyeFe0vmdJKhcJm3K8ErAXbJQj2q1P7kRA_yTDaj5EoW2IVw7G8L9AJ9xIBL02bpOzx_2rECgpEYTm99VD6bsiJ6Yqp2mYHX-ax4vqYHc4AgU3ob2_Qr4X3aveviAnbpV0_BN2-OEExY_P4LAwMD1ulAvuKrtIKQDUv1jXjTod2NKK3ZISadm4xHMC33Ijo_nalsZT54DW2MIhQ6g9lcyCMH1jMsbF9ZBEqQ6AEG-ND_y3zPNhMigO7QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97be903d17.mp4?token=oTNgMRKqHWDIfihcCY2SwuQv2XZwcfa9F3eAE05ev_bqM1vWcaGng6m0ye6awQpYb8QRn9Ma9l7u4dM6hezYNym4dTwW9yyeFe0vmdJKhcJm3K8ErAXbJQj2q1P7kRA_yTDaj5EoW2IVw7G8L9AJ9xIBL02bpOzx_2rECgpEYTm99VD6bsiJ6Yqp2mYHX-ax4vqYHc4AgU3ob2_Qr4X3aveviAnbpV0_BN2-OEExY_P4LAwMD1ulAvuKrtIKQDUv1jXjTod2NKK3ZISadm4xHMC33Ijo_nalsZT54DW2MIhQ6g9lcyCMH1jMsbF9ZBEqQ6AEG-ND_y3zPNhMigO7QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل یاسر آسانی هافبک استقلال به الحسین نامزد بهترین گل مسابقات لیگ قهرمانان آسیا 2 شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90408" target="_blank">📅 16:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90407">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8mjw84kHQdhmLe3_Ux2a-2iYPCY4_58x2xa3LdDs37af6K1khtODyKZ4XVi_Ftjf79QR1Zw97zVFlfkzNFgnor-Z87I1vjjqgHB9pqF8VTrfSmuC0HTZERv552F2nZ2hA33uiLNX4k7OWAcwNScXNNg4aM3ECSYLLKewFS10dKNJ0ekJjdGxDEeMNCHzwoUPqUZB1k0HF9j19PpGPcmo8DieMjx5DcRQUna8PwAXRKco1aWGjD9EH59fAwo2CNsvZT16cl9wrRPKd3ZorX5cQpbpGw4glGziih9vx3yzd0eDXXPib0mJhhJojg2LTNgiwZUYnA2zQdMvwmy-cGPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تریپیر مدافع فصل‌قبل تیم نیوکاسل با عقد قراردادی به ولورهمپتون پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90407" target="_blank">📅 16:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSjIYIw2uapdDsSP8PbNmEhnG2pJJvxlh5a8qAF2fLNzW15jD4MJi6XUOzDr_OCX2qr3-5OWu4JDN2-7X3AILSLWf-AiAQFO8vPsCDl8XI1MDx5szCe0RMl3vAlNXJuRfFZ0BUdegjXw0z5IdtrXn0xJi9T9LRoxU1wDuCJYAKbtWP61b8LEUqh8plMw3M_e7SYzRd9grV7zvRCOJgNUxnA3eFcvruJvPpoQt37YitzTNlqN_dZeBwUrbFUK7e4e2NvF2alxfYnzcRAuvPh9miC_0axy7MnMtRkJVSjG4M0Jbbcnlt4nLNNPV-OEsVwCC2wYOiWLI_vbnq2bbrCdIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مثلث‌های هجومی آرژانتین در ۶ دوره اخیر جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90406" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90405">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhzhR_v87GXvdtYb3i0d1SLd9NmLnd1KBhNuKDfVMZpQ1NPVhKuYqUfO4zYEt0c2DGp0cWhMV2XMbSYhqnpYqgayH89_kiWKF6NElFSm0NwEDySA7agG8ldgcsLGWwQcjWuie6_lkx2xb21da1jLsbMgbE_kgm7rLaEd9NS6f52gYApmrE7mwYWgl2u5ikacL3-VyEDpGNJqtZgi6bhfucy7wYzIsnDi5ick7wkXMx6hdVD7KFh6XNtpnaWKSqxIJ3PLevBBsRaNC31NgfBBToMI6jFEe8mglRhn9VK4TvVQojlM-TwtrOSguxQVKP1R-Hw4ML_Zn4ZYiWhi_n3Xyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↪️
🏀
سوفی رین، مدل OnlyFans، ادعا کرد که یک بازیکن بسکتبال NBA مبلغ هنگفتی را در ازای بکارت او پیشنهاد داده است.
🔍
اکنون کاربران در شبکه‌های اجتماعی تلاش می‌کنند هویت فردی که این پیشنهاد را داده پیدا کنند و تصاویر جنجالی این دختر به‌ سرعت در فضای مجازی در حال پخش شدن است.
1️⃣
داغ‌ترین عکس‌های سوفی رین در کانال ما!</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90405" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90404">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKUk9VNsuVXYy6O0dmHMZ-GlOyrg1skdjBB_zdTt8J5iHBpabAvtFshjU0ZqyPZNz7_H5uYFThQ65QZU7jh9JFb3BcKItwNQKZxbP1gjEo9yBORrgVRk8NzFChJB6wcCMqlPYZQhKsXCbC_e7nifamCeF8sQFRQX_r06QNo9BvoEqhkpjv9K7mj4UyMl9UoIUb0XeetXKGUiV8gKQHLdplaYDHfo_KJ_lPy7xnu6WjcJ2PknN1SNgP7UajgmAyIdo4MiCduCVGgI9KRxkmHnWKgi4yn-dMloLOZgEZXY0RttdfMkKVBnexeA-hK47LSXsXNBFJbCfNQLxwPQEG82ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شانس‌های اصلی کسب عنوان سوپر توپ‌طلا که قرار است در سال ۲۰۲۹ اهدا شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90404" target="_blank">📅 16:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90403">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=dfQ4ACPrUrZyctRwi1_FFuHVjXvh3S99ztn85LYmHhmCGP4EXvc2tbvC2qFL68MsgcMV3Z3aGCPEH6Kr3Ma8xq1LB636aUoWPAcSHJXtPFCBXNJ6WHxYtU_FAUq6PZbG-FuHCnZBxoTbZeSC_k-iTyDrQkPfUusG4P6LQu_2vjLEDaOHlCW41NADRq1CBhxCdyih39j4H1yQP02ePbXH785dQHO-PAtpqMHeQCnhZ6wpU6jufh-WWfvhIq41BP-yPVfA6SKwTJUKV9Tp8E6cbjr7kXlRbCPUutGVLB7bv0pVjDWkqJNKMmxuk6Oy7HjBrMMp6MZSS3mfIib_ZWKWQBHu7WAcKRh9_V8CrpXESghCViLuHTBU4RAa57KQl5jqGAlRiMM1YOHqLOE_MEZdLdhwrskWRP1CfxP61G2tgQvQG-aU04HswLDmOGO-mKZj-L7oXcy9IGU6S9OEYR2aTq6Gtu9pdAgJaY-zp6wjPq2BnqyJKpXVL_k8WdYsX1qxxNAT473pLwmhLqkPG1w5VrfSyvRhFXvSXuLFCV5kVlByWCAxFTQPPAfLZkX98-TqMQqX-pD-fsamyR-7QXqXducYX6_4AGRlHS5p0y3TdNdH22bWow8SMPSl-OopZmgO84sU-OdIG0SzIfaMdrCl14w7pnkeJ5eYnOKrVeIn2GM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=dfQ4ACPrUrZyctRwi1_FFuHVjXvh3S99ztn85LYmHhmCGP4EXvc2tbvC2qFL68MsgcMV3Z3aGCPEH6Kr3Ma8xq1LB636aUoWPAcSHJXtPFCBXNJ6WHxYtU_FAUq6PZbG-FuHCnZBxoTbZeSC_k-iTyDrQkPfUusG4P6LQu_2vjLEDaOHlCW41NADRq1CBhxCdyih39j4H1yQP02ePbXH785dQHO-PAtpqMHeQCnhZ6wpU6jufh-WWfvhIq41BP-yPVfA6SKwTJUKV9Tp8E6cbjr7kXlRbCPUutGVLB7bv0pVjDWkqJNKMmxuk6Oy7HjBrMMp6MZSS3mfIib_ZWKWQBHu7WAcKRh9_V8CrpXESghCViLuHTBU4RAa57KQl5jqGAlRiMM1YOHqLOE_MEZdLdhwrskWRP1CfxP61G2tgQvQG-aU04HswLDmOGO-mKZj-L7oXcy9IGU6S9OEYR2aTq6Gtu9pdAgJaY-zp6wjPq2BnqyJKpXVL_k8WdYsX1qxxNAT473pLwmhLqkPG1w5VrfSyvRhFXvSXuLFCV5kVlByWCAxFTQPPAfLZkX98-TqMQqX-pD-fsamyR-7QXqXducYX6_4AGRlHS5p0y3TdNdH22bWow8SMPSl-OopZmgO84sU-OdIG0SzIfaMdrCl14w7pnkeJ5eYnOKrVeIn2GM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روایتی عجیب از کمپ تیم‌ملی ایران در مکزیک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90403" target="_blank">📅 16:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90402">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koPQRxq3TUmNRi1e9JQdZs3HQ1BFQdtLOh6qcARY6joivbkog8nIFJxg_IVqd_WQKODxYfwtI4Tc1NtUPMehRBBQ6g-lQY2I10U73SYwTnNbNC2dGQ3obMtwNZwGs702alLb4rszprbibqp6cVQ8sqG7WGiu_aHwwnBd7kDp5250bJO8mHrcNUXRkTNYjF7e9KIkcCJE68gRiWouNnM7ChEhjGKehaxVsebFFmmdEBt9Duub55Xc1zlFSv8CbTOy_Jw4POpfSylWvQIHH436fyJiFgHu8G7MbaDeSpT3fP_8dEcHttKWhpNUytGNncMHzcoLrLEtKllJnlF3uY00NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی با بیشترین پاس‌گل در قرن بیست‌ویک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90402" target="_blank">📅 15:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90401">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=qdeZmjMJkCshXJZ3d3-dC7tUzNZorYF-Wx7enXURsEBAk1k4fAqzxUKZ3nFG5hr1ut_WqxvtdMrOtg1WLhvJsptGUFL9oMjV9ZxpC7xGADa08cO_KCTd76PZGe6I1y44kB0lAGbdEFgg-yPNiJRf_OJJ5zFx9KFnIFnvQ3T7_v7rd_3YMCABQLp3kiSe60RH_cOB0fvI0t6n5W3D70ozMpEImc_S-yqNlifUOrMIOLRUhopYTrXkMgQsXrm0WeelX84UOvvUMSGwb0tqrNSYxU02wza7u9WUUH6Pz2ZH-_Gw198Swj4rlL_XZibPVr5Epl-20NFB0omn5FtWbNs0Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=qdeZmjMJkCshXJZ3d3-dC7tUzNZorYF-Wx7enXURsEBAk1k4fAqzxUKZ3nFG5hr1ut_WqxvtdMrOtg1WLhvJsptGUFL9oMjV9ZxpC7xGADa08cO_KCTd76PZGe6I1y44kB0lAGbdEFgg-yPNiJRf_OJJ5zFx9KFnIFnvQ3T7_v7rd_3YMCABQLp3kiSe60RH_cOB0fvI0t6n5W3D70ozMpEImc_S-yqNlifUOrMIOLRUhopYTrXkMgQsXrm0WeelX84UOvvUMSGwb0tqrNSYxU02wza7u9WUUH6Pz2ZH-_Gw198Swj4rlL_XZibPVr5Epl-20NFB0omn5FtWbNs0Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت لاپورتا رئیس بارسا در ساعات اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90401" target="_blank">📅 15:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90400">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8HpQvrLrb-A21fOQmN5EHkW2pvDan89j5ViKUHSm3s4OBPU4uawYRcCSMdL7N_ekE3YTJ_wLnX19nBSNTqNTz7U9eTYS3eBP_wdIt4D0-J-2t1hpH9U9SR_imCZFUNKw-NGfH3hR5pk6ixmGxhMs3pman6oZQBT8TnhJ4F6Unk2YKSRJ5fUXXbZQvtAMJ2H4hQcTV7_wjDk6Wr1wXPubgbBGxa-6DSddAooBtiec7gIUs1qzBrwKusFrjocmPhHcQz81NiBDGYoAoBLoxs8zZr_Vgy9PezPwN6cAL3A3gky07-THNjbY1LS1hLyW38BTMXnVdtfVUBEBdQmDu9T5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
ترکیب احتمالی بارسلونا در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90400" target="_blank">📅 14:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=hCp9a2mBMLaSPdUo42cxGrm8ZeCgPp4zdUJ1gJGKPU8zgOlZS0Po8Zal8qHRvSwriBm9LzWaymSn4eGpKOmAbit64o1eTk01k41xdX7eX27X3cHIff00aMidDDT050MJrluk5WhCgWNLLssJX1ZJzlqONm687ebYXaoCEfjnS6s7-iVnaK0psJe7RtLRntB8081ZNZMWrYRAKqy6MELU2enYKo-pcGI-hE8mtZ4y_6jpu4q6WTUhPt4U0-YmACq2tXGby1gpw-61gYl8RUK3CAFXsVEmL1p0lAovpSF-pJ5few_tKkJushqPneLMmVOS6ll8Qdy8iLZZaYMD3iTnZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=hCp9a2mBMLaSPdUo42cxGrm8ZeCgPp4zdUJ1gJGKPU8zgOlZS0Po8Zal8qHRvSwriBm9LzWaymSn4eGpKOmAbit64o1eTk01k41xdX7eX27X3cHIff00aMidDDT050MJrluk5WhCgWNLLssJX1ZJzlqONm687ebYXaoCEfjnS6s7-iVnaK0psJe7RtLRntB8081ZNZMWrYRAKqy6MELU2enYKo-pcGI-hE8mtZ4y_6jpu4q6WTUhPt4U0-YmACq2tXGby1gpw-61gYl8RUK3CAFXsVEmL1p0lAovpSF-pJ5few_tKkJushqPneLMmVOS6ll8Qdy8iLZZaYMD3iTnZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
حضور کریس‌رونالدو با جت‌شخصی خودش در پرتغال برای حضور در تمرینات کشورش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90399" target="_blank">📅 14:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O1jz7UrKMKiG906SLh8TPLJjB0ObWSWzEFo089DJ2SZGncVCzDvEpiPjF35pOAS5GSYT7iWKrqK7FQ3hobuZGlLeEGBgPPLR2HHH6UCA9Ym-9TUEh-gHNf_QNQY0nkIond5Ag5SP5icCy1vNsDZcsJyzZ-R_X89zvuGX2WPvStUTSHWf73Y6DyNUVUmTTX8DxR4SLOvrb_ecC3eHC798Xeg7MG-rXXc_6DG6inEZyQiGliM5QQsz6a8YUaE6drOv0Zfz1vmPWZA49rkgAaFVpRM1-zwttLopihxiZ7hzH9FhLrnilTArdCKR9G9LZFm46i1YegmKBwutzY-W_zhimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ نیکولا شیرا خبرنگار مشهور ورزشی ایتالیا اعلام کرد که قرارداد احتمالی خولیان آلوارز با بارسلونا تا سال 2031 خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90398" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HogIQcmifTilfHYOuYjXaH3lUBiD1zI9D0qNlUsaL7eN7p72Djg3m8AhIjhh3dcz5bwGN-mTnGf_MrTq-kqaDv4V0Tku3xS4jFdTwInjEJw5d7jbRJaR5diT1E5_pDhYSMcQYGcUdVa7G1OZWfdRxJIez76dsByBjVEgO94INzI7pepuVtIxS-8dgG1t45fvGwsLip8T3uDKPBaTQ5AqnRxZvJGYnyTYTf2rkwocsWHQiH8tBVWJBGWk0N1LdqgHbQBCW2umgxonxODvuTXuP7WPcm_fv1IykFwqzJxYOoKVmrDH6FPiw_Blh1aMxQXupBRLd_49JV4MLrhDM8anvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
به نقل از مارکا، ژوزه مورینیو اعلام کرده که با توجه به نقل‌وانتقالات پربار بارسلونا، رئال‌مادرید برای رقابت با تیم هانسی‌فلیک نیاز به جذب حداقل دو ستاره تراز اول جهانی دارد و برنده انتخابات رئال‌مادرید باید در این مسیر اقدامات لازم را انجام دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90397" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90396">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری از رومانو: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90396" target="_blank">📅 13:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90395">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-1QTIKV0tay3dSqCydnkobWVj-wkErZNbPVzeLohNA3JSG25e_zNmnR91FLp-XArFL_H7_T6gOE0isSdm-cVw3MSrXV9hB0iI2EUH9mVpbHWqXFmnEbvaf50o1q5nyZj2Offk2NcZvb_YaotkXIzQIQjr981HszgBwB5kklkwABi-yf0tFL7VuKxojXc94Pr5rSRTkvVFBV_6GiC_anXn7e4EY9BBDaB_tdsBf6LLadPvKP2JqkPCcBGxRYKakrVQqSDcOEAZxjaX2EBCx5RLMQ5ji_XiTfJxQ2PoBULiHpSSnnA7wigFT6r5SHAxgWPQpBM8jC3FmV5w3LVQfrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90395" target="_blank">📅 13:45 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
