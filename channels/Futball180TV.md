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
<img src="https://cdn5.telesco.pe/file/UbdZzDUhN6YrwJFWDmoS48VBAiyD__74kPyYOIB9zHvCE1N5WBCYy9QJmW8wHmYgRGpjqaK-iWB1AS_VscG_5bHWjIj32zok8JJXo3RgGKT0A5XkAPsu3YHxyQ2JlWFXljevnhF6gEExAbGf6fvaGAHS3_pGrfoarR7QqKB8GvFL9-e1GaKKMEUbW9ND2G42Vp0vsJzkuNaiTFGVQu6Re-T0MgOEBVr-zkFyx4ExjoU5dRg9NGH1sHJAt94eO6773wnZbonD1qOfQjMqQES6fUt9KtaRsmyoecZSK4Ngo6r-iZveeVb5tL9PTMtxB10lU8OEXSHAfzgCLx-TakQsxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 402K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 04:31:48</div>
<hr>

<div class="tg-post" id="msg-107221">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/107221" target="_blank">📅 01:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107220">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkHl_Y8uhx4GNiD-y3aX3N2dv1QYnW2alHTIowkkvsnwQ-1yoLMKGjA1YfZzN_CNnSsavV_EcD5e9P9mI5MpkY9Daejnu0NcyFGhPl2mMEKFMcbhOWrF8mJnRRihOGwQimPIdN6NhFVFOAx1aTGUgRD0LkHsf6eSMkbkoZ7DAg_HNsMt_oX8soNuMMn-YOG5kopzeE468N8pEemcxk4fSjfXl-6xBrd1QOqlq00IUJFdzOfACjiTSfZMWrCs52xbkQPDB2gw7cRRiQyyxCaWfbKrGsn_FX54W0H62k-S4InQ_kLJaJYCJGdE8ohB0stwsOayBje2-bEpCAivzkh_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/Futball180TV/107220" target="_blank">📅 01:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107219">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrwlR-iDRFHaKuVAcDTsG52TtC_awhFl1KuTwZfL-H84s-QrDBhyicGYyYiVogAyKeewPcvUKtb7JwAdxRxps5jRbksF26GRSWT9YiXZX4Zr8PzCzofRzy1J5XzALXSjPcN85EO0TJRBFOOBykpTweQfaCIbTPAhuzEDGwF7c8s_U7cGdNNkw5FlExuHtNHKaNOGgLcpmoNNOMSQiAGA1VYnCuz2SfOrMzKfBLR5cX4xY_J97ZrTeMNP_IOqVt4scjsIV1LRiOxOUQ9Xk0WrjU8rFW1o2Z94NX_RC32-bIj_E8HctBtWaTjwbpGRPr4hfo522r3G9M6UFiKPUy_nSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
دین‌هویسن مدافع رئال‌مادرید: شکست مقابل اتلتیکو تقصیر من بود و بابت این موضوع متاسفم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/107219" target="_blank">📅 01:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107218">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvlyZcPKLy0bwHfMkV5HgtVhIKDSKCJrUpGYAxPc2nWPupcRc1bUjPmXEHiuwQsG3Vp9no6Tib7lXk4tuMAJyfG6Ip7kTxgn50aMVP7QBBNdWqRFkfZej5oUxm9DavQU7uZl45a_3w39T9S9u9uohbYoc9RQ-vp-NO95eJ6w4P8sqi6mSFffKlMzNOant1n8zQmlaYpR5qq_3NSo-4SqPuPuwDCBiWrqcKX4ByS9YT0CzFjnYPVt51R6qNLe6yzW0DNTrqPjDPJcIkLdUcM5CytllZWWpnrXNQZoBYNmKVwtS1qDlIMAshDIGbwPLO_ovRn2GH2aKj9HwE-R6_dNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
مبین‌دهقان بازیکن تیم‌ملی امید و الوحده امارات مورد توجه سهراب بختیاری‌زاده قرار دارد و در نیم‌فصل قرار است مذاکراتی برای جذب این بازیکن از سوی استقلال آغاز شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/Futball180TV/107218" target="_blank">📅 00:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107217">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c410e310.mp4?token=MnXCeJRtId707CFlFgWun0qjZyzr7zMs_bLKRW5zlfra9LhlbTuXza68DhJS9S6jnOmLryJiRbjvbL-zdq3ImyUJvLKVXNl9HAq9EzHFO-nNWolYrT5AvwQIXbZTaPLrik9JyrVkbNOHahL-NRBohGOqQZrVEFxDDq7EnckdU7br0mm3iKDqQqx8W_p3BhOr8IYYKh0Ro8ponoWzcPzpbraYVp9ltO7B9aJ1lzUJ3ba-JpHwS9aV40V9IIDOlg8ZrlQ_qo86EgYc6_Ujjcj7_e-r-b6AOTyjQpvoy1UpP3a-tABOtgqzIbayOygVySB901y1C7jyBzbv4zoOohWXhzafLWy3iBoQlJFQCddmHKIffzQMZVatS_uT85VDIWy6FbRpHstCW-mIP51pzNckFXciU_TaV1NwODcA5fQO-TBEfBvRpWdD8LIxEQNZI8SpUWJj9xZmpnAXKB_M8nhfgRAQHUDXPoRHiVHzwQQKPWFo7GMnekvDPvsJcjcR9RcKwllgaR7U52IKdZnmXF-hnpoipxOb9KpirKSZZYMcJ2nG7e6wy8Ba_IeyuVNSJh9FNPJ1pCb_zATWb2_nKhK8nfTjOsPxdbArNTSnZSO6mLjBe36A29KnVukiougVfnnGz5_AIWbyoeMPDNttWTB1p2plHEZljOEd63c18Szvqlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c410e310.mp4?token=MnXCeJRtId707CFlFgWun0qjZyzr7zMs_bLKRW5zlfra9LhlbTuXza68DhJS9S6jnOmLryJiRbjvbL-zdq3ImyUJvLKVXNl9HAq9EzHFO-nNWolYrT5AvwQIXbZTaPLrik9JyrVkbNOHahL-NRBohGOqQZrVEFxDDq7EnckdU7br0mm3iKDqQqx8W_p3BhOr8IYYKh0Ro8ponoWzcPzpbraYVp9ltO7B9aJ1lzUJ3ba-JpHwS9aV40V9IIDOlg8ZrlQ_qo86EgYc6_Ujjcj7_e-r-b6AOTyjQpvoy1UpP3a-tABOtgqzIbayOygVySB901y1C7jyBzbv4zoOohWXhzafLWy3iBoQlJFQCddmHKIffzQMZVatS_uT85VDIWy6FbRpHstCW-mIP51pzNckFXciU_TaV1NwODcA5fQO-TBEfBvRpWdD8LIxEQNZI8SpUWJj9xZmpnAXKB_M8nhfgRAQHUDXPoRHiVHzwQQKPWFo7GMnekvDPvsJcjcR9RcKwllgaR7U52IKdZnmXF-hnpoipxOb9KpirKSZZYMcJ2nG7e6wy8Ba_IeyuVNSJh9FNPJ1pCb_zATWb2_nKhK8nfTjOsPxdbArNTSnZSO6mLjBe36A29KnVukiougVfnnGz5_AIWbyoeMPDNttWTB1p2plHEZljOEd63c18Szvqlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بومیان استرالیایی این‌شکلی از بازیکنان برزیل استقبال کردن
👀
💥
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/107217" target="_blank">📅 00:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107216">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb-fnJVh9NeUb2EAptzEdnVa2HTx-OLQSn_e0XDArPM1SNxwE6Sh9UK_sgTki8lKHxrgy97BxXDDATSh55VITM-GAJ3RFnJs_gYxOo4R6MUyvGWB3CyBtFDRmzY6Iha4zW8PQKetsqri5mGGh30tfhet7_-jJzpp6jrJK0Jq7TOiuomVcZOyep3ixXy5wsjOMcd6iyANyh1kdvWsJK3JN6QP4MTDx73YNcdqqzCLmCSnHRV3uYrT9l2Db4E7DpXk4JyFL7h09EK4f85UITvneQVA4muWzE1cg0oP_K9mZA0Psg3_l206QipJ0aJrF2bVIe6kQnqWlOM8YX_nHnp7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
نتایج‌بازی‌های امشب لیگ‌ملت‌های اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/107216" target="_blank">📅 00:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107215">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L627eWA-HUwadwqCJBsHoHFqpsKIIndxfGZ-hwpQjlRtc5r8MEuoIveYfuHhM8R36sIR3pMoxyPWDMT-YB899GwuDjD_qpfXCx4Q33kS_Rhqqfu2nOT3Xshh-ui9ynuVr7dDNE-_K4cDEMdwhxex_dvW-HOZdX81teOb4LFWxHBa9lMT-tP0Ub_sGstM-_6qCsAATvMo8_fRMKlHmmZbIjXafcdqx6JQVgkLtbxXj7MdmAQntKjYLpp-_FHWo03UMf2CL5b60Z3G7_DGJXkYtu_aQeWeeiP7TJ4i-HxYyI4y1At3dCrTxQ5CxTBV_AdZO6xafEdLEybEOX0EfJdLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
🇳🇴
هالند اولین بازیکن تاریخ لیگ‌ملت‌های اروپا شد که به رکورد ۲۰ گل زده می‌رسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/107215" target="_blank">📅 00:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107214">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
⚠️
خداداد عزیزی: چرا همش با ازبکستان بازی میکنیم و میبازیم؟ با این تیم در جام ملت‌ها هیچی نمیشیم. بازیکن جوون هم که نداریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/107214" target="_blank">📅 23:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSeVl4LovukjDZ2wNSz0NLXxsB-NmnCuNQn91ln__Cb52IdSN9sZucqENTEDz4AQaMXvbGI9yM39ObUhsrHS7cMjHm_R9hB28rXKbTNFPV4Xq5Ai44x0R4jpvjVpucGWP4NDglqoi871SSMCF_yo4yeB-CYId1K2F2CK977KattV_daUGzwOzr9g96r3gKYjx5Rw9pj4jlUVokubAe61SGg8Iun7o5cIlIBE3siPUwI67NvSO1RC1J3E_VS5pGQbpJvXjXApADMynEs37t0ULDuZHsRcH7aTa9iajdwCbWtLowjOc7VFHXurxMKm1D-h64o2cd2o6oMJzaygFBitwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدووووو زدددددد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107213" target="_blank">📅 23:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🐐
🤕
اسطوره رونالدو امروز اینو گل نزد تا به روند درخشان‌ خودش ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107212" target="_blank">📅 23:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvvgWnwxQ0TkleIJDk20r6ygahQsvCVqasxB0OPFb_i4OTj0qHvAQRXilV-cXl3UVLMXOOWX__i6kdHuKmATR5I6GjgLYiyawqVwvCODpDtb_paHP5ouFpqTLzcOdWrhANJf7X5c_WssCrzIwvVTK2gQHwnCt7y_MiPuufYW9Vyrf4epvWvL933NslBzIndxMlK4LLyKK4XjVWz9k1Q1IB1CI3j2yWeZ6ZaB1ULnR8D5h_HsQwRNlURCkRzWJve50Lx6Srshu3YVZfDe1nAaIN9vPvKt_6Uq1Hu6Ud92GmA1J4DwW9DVkp4Hke3z0MlR09tkCbMP6NLRjXsGgkdBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
🤕
اسطوره رونالدو امروز اینو گل نزد تا به روند درخشان‌ خودش ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107211" target="_blank">📅 23:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBEtvs52DlowByhAG6RYexlluhZghtYvuxCqRvMO7aJFeLtJak1TU1ZgTV2YOzaKCkVzu7wb5bovqmqW3w2tor-qsO-nrI8u1p6V-YfRMbCPpFg1fgjf4iGb4WVcxS7QYizqprneaRzocVbaC5XiXR2HFwmy2ztMGrU9hk3nWIHYqOOOob6iGrUWd2Ge5ZEYd4OkG9MJWoo2AaamsUY9CWSPDasRE8-PcXv6HPtP-jFl3iV0F5d59_Qkj9W8bW7W108CXCGd5R22Gij2W6V5cOUwQP_yYihDh4EpzH8mzjoSvyaN4pF0yBF69wiIQ9jOiRuwgRu7u0JwvjKM0QKs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
🇳🇴
هالند اولین بازیکن تاریخ لیگ‌ملت‌های اروپا شد که به رکورد ۲۰ گل زده می‌رسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107210" target="_blank">📅 23:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107209">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=lmbARgmBz2U2VnhFYhG64wsqdM3iU-V9S7vwHP7Fldq2VbhP6j7-OsqIuqiC9YnTWeBB74xudBkPbdcnN7h7WGhfWsGu8g_HsnDPHnQH2b-tgYFWmnPP8wk4rbd8TROye90E0e_6aV5qP-yTet_TPrCQEeX6voNXAD6iYW7AYja37SQFRE0d7nBnZXzeahumkOpz2DSHZztKNPLUi5V3CsI8Rwg-YTrn14njhzA6C0VZ9ihQb9SxTNa_69z6TSrQJ3QmdOgEV0CZCBaC7aR1U3EymeALlEbVG1IP3mBBum9gJ6zMGmG4kMC9eh7OE6CMCMoR4bwcsc-K4oxp7O-TZXm7Y_9bsasbiea45A3dnKyVHJIAsyPgrBSNAH9ULGpAZFWLdZXl15rl9nSlv3VLH4gW81oJc5AoIxGLIgcwM82KRhwUZZ1YzSIBHJRJsDt_M-hUiMUQCznbnIru7XOhPMtWeW_--b8N9HxH8Ln7NipswSGq6BafoD7Vgrq5YHDUoxZqDqVJXiuE-mADQEjNKB9babAgqzwiBSH1W8PCn86jT1q3iU3DAoKfVO5WcmSYr6-r2-EhfZWqkcGlAONrxVDAouxs4KYAiqw5nHVMS8Em1y2kZQISv5itnVsKsV8fxMfRPWQIrrCvIiEPWELQf39TsvK8A_jclk99qCCFOTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=lmbARgmBz2U2VnhFYhG64wsqdM3iU-V9S7vwHP7Fldq2VbhP6j7-OsqIuqiC9YnTWeBB74xudBkPbdcnN7h7WGhfWsGu8g_HsnDPHnQH2b-tgYFWmnPP8wk4rbd8TROye90E0e_6aV5qP-yTet_TPrCQEeX6voNXAD6iYW7AYja37SQFRE0d7nBnZXzeahumkOpz2DSHZztKNPLUi5V3CsI8Rwg-YTrn14njhzA6C0VZ9ihQb9SxTNa_69z6TSrQJ3QmdOgEV0CZCBaC7aR1U3EymeALlEbVG1IP3mBBum9gJ6zMGmG4kMC9eh7OE6CMCMoR4bwcsc-K4oxp7O-TZXm7Y_9bsasbiea45A3dnKyVHJIAsyPgrBSNAH9ULGpAZFWLdZXl15rl9nSlv3VLH4gW81oJc5AoIxGLIgcwM82KRhwUZZ1YzSIBHJRJsDt_M-hUiMUQCznbnIru7XOhPMtWeW_--b8N9HxH8Ln7NipswSGq6BafoD7Vgrq5YHDUoxZqDqVJXiuE-mADQEjNKB9babAgqzwiBSH1W8PCn86jT1q3iU3DAoKfVO5WcmSYr6-r2-EhfZWqkcGlAONrxVDAouxs4KYAiqw5nHVMS8Em1y2kZQISv5itnVsKsV8fxMfRPWQIrrCvIiEPWELQf39TsvK8A_jclk99qCCFOTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول آلمان به هلند توسط انمچا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107209" target="_blank">📅 22:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107208">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=emKt2cHldNGwVeEaVZ2hM_2iDx4_FZbweFmNlo67m442rGLrKmZmrlNgFe3r_HdAZ0rhLgnNecyeYLDgyOsp1pOawBW39AD9rL4NkrztPnxyHelnrgeL59yQbpdqk7Rv7zb16rqI_sDQmqeRPck1d5XTGbZuZwXS7vsdJb-CA0MkypXPOtpdtPN-MgNBETjQDbbkO-ku-SWNbfqcioWjFvRHXKqlAv8FLdw7XXXnAZYLxoi0El3Qhf59XNn-T0JCRH7IR-ql_lzbV8i18eGHoCVhttXI6LpLJooKkmDtQB3uySOotOGAKIKpWVrlPkiDPIQfTK8ciWTbtZnpJClz0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=emKt2cHldNGwVeEaVZ2hM_2iDx4_FZbweFmNlo67m442rGLrKmZmrlNgFe3r_HdAZ0rhLgnNecyeYLDgyOsp1pOawBW39AD9rL4NkrztPnxyHelnrgeL59yQbpdqk7Rv7zb16rqI_sDQmqeRPck1d5XTGbZuZwXS7vsdJb-CA0MkypXPOtpdtPN-MgNBETjQDbbkO-ku-SWNbfqcioWjFvRHXKqlAv8FLdw7XXXnAZYLxoi0El3Qhf59XNn-T0JCRH7IR-ql_lzbV8i18eGHoCVhttXI6LpLJooKkmDtQB3uySOotOGAKIKpWVrlPkiDPIQfTK8ciWTbtZnpJClz0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو وسط سخنرانیش یه دفعه پیجر درآورد و گفت اینارو یادتونه؟
اگه یادتون نیست، حزب‌الله خوب یادشه، چون ما با اینا، منفجرشون کردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107208" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107207">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305c017139.mp4?token=vG_HQO55MdDYdczbuIjHjrcIQh89MEeBHp0PAx11Zh6JN9TQaFJX6vZ8rlDv_WSHHhENO8-jWddgNK71M65Ut-iDW99dWCWxzB7nLSeAbIniz9Gzc4W8ukxaHNHiw_J09D4W86wUbQmaskGPwS_abOD_AKAAbvjSGaQ6GAMHZxAwPxD6xhkJirGORGlLpmFwBML3zSNHb9f9FbhZlzhVscLwixpdN289rjeUDGWZi6FfR0Lqjag0PeyIl61yz8HXR-anowdxNLWRmBmo8w0OQzHnsl4qPrU3A_f7_T2pOQwAMGlnFmdOH4LJGnb7eRz4qbuvoHV7SUEvUtfEcD_ghjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305c017139.mp4?token=vG_HQO55MdDYdczbuIjHjrcIQh89MEeBHp0PAx11Zh6JN9TQaFJX6vZ8rlDv_WSHHhENO8-jWddgNK71M65Ut-iDW99dWCWxzB7nLSeAbIniz9Gzc4W8ukxaHNHiw_J09D4W86wUbQmaskGPwS_abOD_AKAAbvjSGaQ6GAMHZxAwPxD6xhkJirGORGlLpmFwBML3zSNHb9f9FbhZlzhVscLwixpdN289rjeUDGWZi6FfR0Lqjag0PeyIl61yz8HXR-anowdxNLWRmBmo8w0OQzHnsl4qPrU3A_f7_T2pOQwAMGlnFmdOH4LJGnb7eRz4qbuvoHV7SUEvUtfEcD_ghjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
نابود کردن تأسیسات هسته‌ای ایران
کار دشواری بود؛ واقعاً بسیار دشوار بود.
اما برای من، این یکی از
آسان‌ترین تصمیم‌هایی بود که در دوران نخست‌وزیری‌ام
گرفتم؛ چون اگر این کار را انجام نمی‌دادیم،
همه ما کشته می‌شدیم!
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107207" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107206">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22263541ab.mp4?token=Wk2mpeRZI1EytheiAtLUPP6HNOuBnXFo74_UmVqO1gOz2c024oALnvHQctfD1M-i5b4gpocyMcpKt7dLxmogN33wlHCNQzTNdiTRQHs_QSb39chyL3nYzyxHUzEqse0t1sf4R9pjta7MVvgXymmYtIG1WF-BfenrFjorOg6UA2Sny9UqIQsI1unRQ8xPU2VovwCEgSj1UbRvVBsmzVO7UyeQEhr0gCv7323zX4bIFu1myNOCTScUcbKPGAjsvuJTvXIlGJQuHivkX1qqSajugM70k2_8EufKRTCeJRU4H8g-vByywXsst9qLiUwvCjcqHhGk3q_eQe5wNN7f7sFtJomnj8ilZPrIIYBczf3o1ldFPppfPTtFBfD_B7d3E4Se5nCyZERUl9aGCMPc2NHD_nwDnDIN3w0WtNV_IX_PN8nQNqeEUuDlArYu1-2Dene9TAnFIaOpTR14j8q3vur4Or-ZWNCeQjTu7mM0rotwrZvz0nrapMYVYWloTkzdLsgE5JIMWU_H8wCpI_KQB_sRGSGAvz6ZKE-dFbq0mit786L0Dad5M5ExIJjXw8Sze5WhMVZMBlSpVLERVPkWzkoIqBhcitnTPdJgy6YjLpRWkaH7AfHuo0zcyX0hV9LxGdEqqr7QM2CCQn2CwK707o17Mguc4-Px_df99GzIO5gtrGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22263541ab.mp4?token=Wk2mpeRZI1EytheiAtLUPP6HNOuBnXFo74_UmVqO1gOz2c024oALnvHQctfD1M-i5b4gpocyMcpKt7dLxmogN33wlHCNQzTNdiTRQHs_QSb39chyL3nYzyxHUzEqse0t1sf4R9pjta7MVvgXymmYtIG1WF-BfenrFjorOg6UA2Sny9UqIQsI1unRQ8xPU2VovwCEgSj1UbRvVBsmzVO7UyeQEhr0gCv7323zX4bIFu1myNOCTScUcbKPGAjsvuJTvXIlGJQuHivkX1qqSajugM70k2_8EufKRTCeJRU4H8g-vByywXsst9qLiUwvCjcqHhGk3q_eQe5wNN7f7sFtJomnj8ilZPrIIYBczf3o1ldFPppfPTtFBfD_B7d3E4Se5nCyZERUl9aGCMPc2NHD_nwDnDIN3w0WtNV_IX_PN8nQNqeEUuDlArYu1-2Dene9TAnFIaOpTR14j8q3vur4Or-ZWNCeQjTu7mM0rotwrZvz0nrapMYVYWloTkzdLsgE5JIMWU_H8wCpI_KQB_sRGSGAvz6ZKE-dFbq0mit786L0Dad5M5ExIJjXw8Sze5WhMVZMBlSpVLERVPkWzkoIqBhcitnTPdJgy6YjLpRWkaH7AfHuo0zcyX0hV9LxGdEqqr7QM2CCQn2CwK707o17Mguc4-Px_df99GzIO5gtrGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
۱۴ سال پیش
، روی همین تریبون ایستادم و یک
خط قرمز
ترسیم کردم. قول دادم مانع از دستیابی
حکومت ایران
به بمب‌های اتمی شوم؛ سلاح‌های هسته‌ای که برای نابودی اسرائیل هدف‌گذاری شده بودند و می‌توانستند
تمام جهان را تهدید کنند
.
ما دقیقاً همین کار را انجام دادیم.
این کار
بسیار دشوار بود.
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107206" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107205">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=ddD7bXWAHVq-rV_WpSzi5y0uUyKgzXdqlzjBGJ8kOI7J6Jm-Ygg_p0yqI9sjI6jYfXR0ZH3cfskg6v2JjR_UBuGNOvoVQDWYnpkpRX8wRftBHUStQA6Pb3VFFNYyDYc3Kd-Gyq6TKpRhsxIrn1coMZWyFJYeEHV5tkkHmNmfao2vhMgvZ_-QVU3yZZWqXXcEPnRE467ktQNuSbtcAj2OEWqo-5wke4U5V_OfFkVmJ7n8tmVKfKeDniQ4YD986-wZpvHhMErq2MZWh5s9v843kyHHJGkxTV07FgjrJKmh2b3fTbYOKqelmwf0hAwhG2DcHUJw3G4EZMhR_wCo0SZ5dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=ddD7bXWAHVq-rV_WpSzi5y0uUyKgzXdqlzjBGJ8kOI7J6Jm-Ygg_p0yqI9sjI6jYfXR0ZH3cfskg6v2JjR_UBuGNOvoVQDWYnpkpRX8wRftBHUStQA6Pb3VFFNYyDYc3Kd-Gyq6TKpRhsxIrn1coMZWyFJYeEHV5tkkHmNmfao2vhMgvZ_-QVU3yZZWqXXcEPnRE467ktQNuSbtcAj2OEWqo-5wke4U5V_OfFkVmJ7n8tmVKfKeDniQ4YD986-wZpvHhMErq2MZWh5s9v843kyHHJGkxTV07FgjrJKmh2b3fTbYOKqelmwf0hAwhG2DcHUJw3G4EZMhR_wCo0SZ5dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سانسورهای تلویزیون که مغز رامبد جوان سوت کشید موقع گفتنش!
🎙
افشاگری باور نکردنی رامبد از سانسورهای صداوسیما: بعضی از افراد آنجا مریض جنسی هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107205" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107204">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VevRKvRoi9jEML0mIIsYfAvCpQ2S-lBNIXVX9n-HoZ4hDkhx6z2CwvnqxXRIYXpnRfdwcX27ct2vllZh-0UtKw8aaeRdI6x-Ioqx5FQFab5sbby4n93F4PyKGVX616mB1qYvCnAsW2dFb_XfGX_5jKlGq0VJQnfqYjWpTUNGT51s7efoEWYEPnNgUGL82DZZpLGErJKIL3lVBx3AUj2GQUS9pE6IyPe4H8TJaqtmFRXLXezZKd72NN9f7E3kZpDDeBpPhSigkm-aO40HFp-tGDSVP8sS1kthufrQWrp5_CHHWBPDSB0ufsu-ymc6wxB4MQS7KyIBX71pFZs3nXov5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
ترکیب هلند و آلمان/ ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107204" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107203">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajcqHa4MXGQPo11tEQJaBMoNqdZeGAaG2V37aP_aAILKzJxjdvlUThLoHWFxh7dHMoPFQSsS78IkWhkDKuhLvImfBIaY4tSLxu32U_c8yo8k4Azq3RtWQw4L_vCxHi0-S6Dl4WYM6Uioc1K1M_89Fw3nt11l9Udfm2cvCtCmSAsSKixpnfEL-mRi8_WO8ZWfublLCHd30Ni12sEXRegSuR-Q37f5-jINm89n9uHqy4V6cHEwoXpEaQIoMCfLqRyVEoBA_yHVd4hba2-ZpDXfdzgdlV7EBND37NlpsyfC375wNhTZtrhgAosUJmX9qZE2lriAE54_1UjIrTZXCQyPHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
ترکیب تیم‌ملی پرتغال مقابل ولز با حضور رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107203" target="_blank">📅 21:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107202">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=SZWYNCsg8_QdGf6XPdQMoFZFWqhMPrB0352GGAnmJyRYiDmLgh-JBd7FBzG1kx4l1cV5J0IvRGsD4vMjA8GwC7vjjQkhwKOfSOTCqQ0ylEsn4uw4Tlxipyw1ei1T45XiYtmyRzNwk78VqB50R4GXyh6k9VdHKPmSwfZdL5xyqij1fe9H2OBXd_pXQ2Req6Q-Fzc0u6Q-2gKeMnbnEFhHxW-jfF3Ln2F29n59MQx31budls6Ofit0-5pm9vxWFvBf4tMJW44_FiC61hv4Lctne897kOzbLkj8hbAVJdd5EoAWS4JmbrnuEpy2PD23uhhUZYKxM5CSL8v58XMms0o9oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=SZWYNCsg8_QdGf6XPdQMoFZFWqhMPrB0352GGAnmJyRYiDmLgh-JBd7FBzG1kx4l1cV5J0IvRGsD4vMjA8GwC7vjjQkhwKOfSOTCqQ0ylEsn4uw4Tlxipyw1ei1T45XiYtmyRzNwk78VqB50R4GXyh6k9VdHKPmSwfZdL5xyqij1fe9H2OBXd_pXQ2Req6Q-Fzc0u6Q-2gKeMnbnEFhHxW-jfF3Ln2F29n59MQx31budls6Ofit0-5pm9vxWFvBf4tMJW44_FiC61hv4Lctne897kOzbLkj8hbAVJdd5EoAWS4JmbrnuEpy2PD23uhhUZYKxM5CSL8v58XMms0o9oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجید جلالی: میلیون‌ها دلار خرج مربی خارجی شده اما برای ایرانی‌ها هزینه نکرده‌ایم به همین دلیل است که می‌گویم قلعه‌نویی از مورینیو بهتر است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107202" target="_blank">📅 20:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107201">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtwCbzLb04FpKGg_laLlz3zUyLvrAakawLjAj3aLp6OB0efRIGRIW5eC6ecS3Zc7eVDEnQOvWoFcem6Kiuf6-uR4Klhl2OeEVVknQ9qG5qJkA0eNBWpaoNDep-tDqtyuKSeOnGMT5WnLW4QuhKjf9xDxc40P3slRneZC0xXMc3nGA5gIPfMkryv_hwzT-4P3CPbKO33IcbaTpoHSvWSwTi4twemZYlC0z71Clvhec17zat81BXGu76epqt3fQEOG001NHnSshaLxvkdGu1dx6jnjRjNCfAV50YYmTLcwjQ1SDt4KqTckNbX4U68uvuhEqCsfBcvFe5YX9ZGL1A6HPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
🇩🇪
اسکای اسپورت: بایرن مونیخ در حال بررسی امکان اقدام برای جذب دنی اولمو از بارسلونا در پنجره نقل‌وانتقالات ژانویه است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107201" target="_blank">📅 20:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107200">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=Ado3XrU9bQp71LdRWylutdzvJmfNgmcSjAJM4x9IPyb_PeBdk0zWo44aqnt7OkXZgA4e12UspJa7GWJXv7Be1GW8tfKmsr_YdlQbiggIe7CxaefXYvsYShAcUnXxmx1IWdqH9xxzsKitizcIpIS89_QEiC-dwY-wYWZM16Yp1Omq3_JSU9duKO6cic0ofdNlPYJ_CX48QZak5SFnF071HdOYYLJ5DYiRgxG7YpzZZBpCSePwQq6-xZ1liDm-YXVv9AXXDKqqELNJP6hnj2Gq_xLhp5UderGgIn0NWnOExBk4ufTALURq_dCEygdfsYcZNSHgzfR_34_S_KGjTUhzmq5b71SgLHxsRbasp6VtjpYrIxI0F7SrTfImbe1TBHAQmqQB1gsg5Ih7wZHpvMwLLnN3c0P21QMAUuXhAvoyth_gZ6SMDH2nYjwQZMady3QXDsyICGMJdOfH2hh7etrO31jkm6T52UeFhoIOsT-ejmeiUdndQW89a3KjzWArNP63cwcgmhnMUZ8rlG8Xv3sVp_7Q-dh5Sr7wh5NKDd25Waa8x6LbcZYcPwEvAgrP0ujo5VxXIv1BZprQpl9_pse1D0wCNj_alvTctWCGKUyQPMEB7044obAP2Qi1DADS8k21CsdOgdC2hSeXxGVMsGrxYYhOgVcgg6AGjTWgBdE8c0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=Ado3XrU9bQp71LdRWylutdzvJmfNgmcSjAJM4x9IPyb_PeBdk0zWo44aqnt7OkXZgA4e12UspJa7GWJXv7Be1GW8tfKmsr_YdlQbiggIe7CxaefXYvsYShAcUnXxmx1IWdqH9xxzsKitizcIpIS89_QEiC-dwY-wYWZM16Yp1Omq3_JSU9duKO6cic0ofdNlPYJ_CX48QZak5SFnF071HdOYYLJ5DYiRgxG7YpzZZBpCSePwQq6-xZ1liDm-YXVv9AXXDKqqELNJP6hnj2Gq_xLhp5UderGgIn0NWnOExBk4ufTALURq_dCEygdfsYcZNSHgzfR_34_S_KGjTUhzmq5b71SgLHxsRbasp6VtjpYrIxI0F7SrTfImbe1TBHAQmqQB1gsg5Ih7wZHpvMwLLnN3c0P21QMAUuXhAvoyth_gZ6SMDH2nYjwQZMady3QXDsyICGMJdOfH2hh7etrO31jkm6T52UeFhoIOsT-ejmeiUdndQW89a3KjzWArNP63cwcgmhnMUZ8rlG8Xv3sVp_7Q-dh5Sr7wh5NKDd25Waa8x6LbcZYcPwEvAgrP0ujo5VxXIv1BZprQpl9_pse1D0wCNj_alvTctWCGKUyQPMEB7044obAP2Qi1DADS8k21CsdOgdC2hSeXxGVMsGrxYYhOgVcgg6AGjTWgBdE8c0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خیابانی: تیم‌ملی با امیر قلعه‌نویی تا دلتان بخواهد به تیم ازبکستان باخته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107200" target="_blank">📅 20:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107199">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=uaY4WGPwnBpq49XNEr3P8aaDYj8-Hrs4APoYIq7vXTyoIiLv3NzNT_rR_P4t1rAmACy-fmyWqebnMJHpcsNfSafFN4CY0qw85nJaDdSM9JzAgxPTee1m9aWatKpzToYLPbQf1k6hh-BtMyVwAfJBbCvn-fVBU1xiyDTRGLDKnemyOsPLAW0jdkkSsKBLxf2FldiyrodL3Fje-9_weeCSXuq3U8rkp6P79iN8_k_i5TC-UpMPXn6ezbvCALtmHqLzll_g9GE26hRTiKUX3qL4X18bLZkhZsbZ589MfcugOyKHpE9UQLTXjLMFe2CK199HxXllMIgk3OgyJNSBv__6vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=uaY4WGPwnBpq49XNEr3P8aaDYj8-Hrs4APoYIq7vXTyoIiLv3NzNT_rR_P4t1rAmACy-fmyWqebnMJHpcsNfSafFN4CY0qw85nJaDdSM9JzAgxPTee1m9aWatKpzToYLPbQf1k6hh-BtMyVwAfJBbCvn-fVBU1xiyDTRGLDKnemyOsPLAW0jdkkSsKBLxf2FldiyrodL3Fje-9_weeCSXuq3U8rkp6P79iN8_k_i5TC-UpMPXn6ezbvCALtmHqLzll_g9GE26hRTiKUX3qL4X18bLZkhZsbZ589MfcugOyKHpE9UQLTXjLMFe2CK199HxXllMIgk3OgyJNSBv__6vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقادات تند جواد خیایانی از بازیکنان تیم ملی امید
: برای کره نه مدل مو مهم بود نه قیافه. بازیکنان میلیاردی دو زار بازی نکردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107199" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107198">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_mX414NWoOK5VVAXxJaVnxaQ1CjOlV5Ofv_Db5DGpSVhdQvMwvV9K3b5gigvaumln1eZZvdo0qOdE4JAeMUHgWZtUMaDzq4fMskJddHyV4iOLaE0ifeHh-HyDZZmP8BMVtWJTiTA5paYg6kQ7sPXlEIlztIm1jBFeOdw8zBZC85XbZg6vCInMw8mngVDeW-tUt7SlBi9iYUVWXTd-crq7wEhbY9FWuS1vZ7tvhMPM4sT5CRCBUGilPManAHL6pUCUe8KC4IoO2O5ZN0TsssnWLQ2yxBa_2LHHL8f9eD62v_8THfSLID9hWuw1Hjh84KHPigvFXXfhrGKzSB8Vhg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
رئال‌مادرید اعلام کرد که ابراهیم کوناته دچار مصدومیت شده و مدتی از میادین دور خواهد بود. به گزارش برخی منابع، این بازیکن به دیدار ۱۰ اکتبر مقابل ویارئال خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107198" target="_blank">📅 19:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107197">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=AU_QrK2UY4JGfu5FknhdbhOoGW7qExvdVVM2acv9CRbGYrdbrV4EValWjPRyw9JS7LCbVmBXUbipsrwAL05SRjpUi3rl9swBkQ7ZdQxWlB0SBQ87GDH-HKCRaa5oZ0KBOGs9cD9G9fPb2QVAJjzx3mOQJZGYZVIeEU6r2Xsg9v8VisvnUVqF8G0abL1qAm_lutckezcmMfSzMis9NfzHRvXzW4wFOMZofbraglemaSAtIEGpOI2TQmHrTN4rug8F5TTRwAkUT1hu8_3uw0zqnw1AP2v9lxkkk8B572hUdQczVkssYxYHT4iWTUFC7Z6q-crgcqSmHRU9UgoVNNoqQ5QcOf4V5JCuN1HBERtoZ9HB5beKBpZ3bioas786AEhkSKkN5gXe25GIm18SNV5vlyPFYYFWQx4eqQib_WCH-tnROX7C106XVZSGBkBQCHuJJ31s-Pqx-Me8XZI8_qC8SR0LFGMZJ8uXquvzloyReGULsO6BhIPaBowJJwOn0yS3X_zUdi-935odeyZGvURNE1CLVnDrsTH-gBOSqZPzF0ajBUwEw2MTU9XQqemNpgTI9thd6kOlguv-bkqW44HkrqxJEKgn8ERqlflYbrtJDr3PpN9LLN16dlhtHeLb0lJ_4GNwPUxtb95wqAzCwdAWkQ78sCPnx1T3EzrC_hkaK8I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=AU_QrK2UY4JGfu5FknhdbhOoGW7qExvdVVM2acv9CRbGYrdbrV4EValWjPRyw9JS7LCbVmBXUbipsrwAL05SRjpUi3rl9swBkQ7ZdQxWlB0SBQ87GDH-HKCRaa5oZ0KBOGs9cD9G9fPb2QVAJjzx3mOQJZGYZVIeEU6r2Xsg9v8VisvnUVqF8G0abL1qAm_lutckezcmMfSzMis9NfzHRvXzW4wFOMZofbraglemaSAtIEGpOI2TQmHrTN4rug8F5TTRwAkUT1hu8_3uw0zqnw1AP2v9lxkkk8B572hUdQczVkssYxYHT4iWTUFC7Z6q-crgcqSmHRU9UgoVNNoqQ5QcOf4V5JCuN1HBERtoZ9HB5beKBpZ3bioas786AEhkSKkN5gXe25GIm18SNV5vlyPFYYFWQx4eqQib_WCH-tnROX7C106XVZSGBkBQCHuJJ31s-Pqx-Me8XZI8_qC8SR0LFGMZJ8uXquvzloyReGULsO6BhIPaBowJJwOn0yS3X_zUdi-935odeyZGvURNE1CLVnDrsTH-gBOSqZPzF0ajBUwEw2MTU9XQqemNpgTI9thd6kOlguv-bkqW44HkrqxJEKgn8ERqlflYbrtJDr3PpN9LLN16dlhtHeLb0lJ_4GNwPUxtb95wqAzCwdAWkQ78sCPnx1T3EzrC_hkaK8I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمله تند خیابانی به فدراسیون: باید چه کار کرد که کادرفنی تغییر کند؟ نتیجه افتضاحی برابر ازبکستان بود. آقای قلعه‌نویی نمی‌توانید تیم را جمع کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107197" target="_blank">📅 19:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107196">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O77XrFq-RmncbTOhM71Jh1YtXAyd-KuYuUfH-ftsKqtGmW5PBR8mcoQsthTl4sAAcLRp5Z3S3h834sbsrZH3dKZs5vzJi7VVKwMFoTU4mA8XDOXT3LSheiJ8ptG9LFaHo-KWseLpXLCdmTS8G0eFm_F0A6n5fyn7Ecw1iWnDmAhuY6axVsR9Z_ey5g7YZ4mr2q_cQkDyuYOJJom-OGWrVxBm6wi1CnNp5D0vZyl2T9jCfxowhAsiaxp4YKj2tL1yVyugNsRWUECGlPVaZYHtkS4wLvPb8epcZsysy51zd_wLrgscyLjjMKbzTu6oPSOn5oSyoagYJUvUPuih94GYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی دوستانه؛ به پیرمردها امیدی نداشته باشید؛ قلعه‌نویی با دستمزد ۱۵ میلیاردی پیش به سوی یک جام‌ملت‌های تاریخی می‌رود!
🇮🇷
ایران
1️⃣
-
3️⃣
ازبکستان
🇺🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107196" target="_blank">📅 19:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107195">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neLDeLNJFmTk3A9j9Cwyyu9RjFKSK2Qfk2WO9VlTeqdzKDD9wwVy7dk2gdKv1RkJ5Qb--r6xhIBl0rO3z9FEHyLfAOmglIS9Y9iU3bss8VUSOzLoUzSXzCXpry_QLUmjcNF7cMtobtt5lWQd5UwqmvDwI7njqtMSPfM-GT5zfTr6Y0qFc5CiTqdaNCfzy0nZSrt3BhqOr7Y3RS7rHy5RneP10lETpidqsZ4EhTsCjYjh29sv7lM4IbSzednKXi95HpGPd8qNSxd5hyBHnMmWee6Aa7lRdAvUhafdgFGFqA08W2jZpnC6s1u0VTisg4M99hO4uVGaB9g8BoUE9gSioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گل سوم ازبکستان به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107195" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107194">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533284b0a.mp4?token=MeCpWK7SBPD1RgsiR3Z0bztSHbnDA-nvg_obJGeYGTQxLUfmcY3U9WWol7m5fX_yFPy8n8PVafOF5ykNtTRs_GWOCNi_Yj4Rm2_b19gLR0Yp4bKn4S_m4g1t6smx3B7pDEfgGdLH25fp72E-bIcklo7q44asC6dPK9o6EwCDEzTe3_rsiNA6PDUTVKwfb4mPrWNl2-RUNiBY6B9op7AAcO1bNTZW2s8-CdSP6aKtMT1Apz1JYyqJJ_81vldrMcHomxc-TRlBC0Z3g5iAw5Q-OQieYOLG0nA2iJZA94umGYS2sjhp0kBA1kRWjpQLtqIU2HMYFOzHy5bNu6YM8Kc2yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533284b0a.mp4?token=MeCpWK7SBPD1RgsiR3Z0bztSHbnDA-nvg_obJGeYGTQxLUfmcY3U9WWol7m5fX_yFPy8n8PVafOF5ykNtTRs_GWOCNi_Yj4Rm2_b19gLR0Yp4bKn4S_m4g1t6smx3B7pDEfgGdLH25fp72E-bIcklo7q44asC6dPK9o6EwCDEzTe3_rsiNA6PDUTVKwfb4mPrWNl2-RUNiBY6B9op7AAcO1bNTZW2s8-CdSP6aKtMT1Apz1JYyqJJ_81vldrMcHomxc-TRlBC0Z3g5iAw5Q-OQieYOLG0nA2iJZA94umGYS2sjhp0kBA1kRWjpQLtqIU2HMYFOzHy5bNu6YM8Kc2yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
گل سوم ازبکستان به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107194" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107193">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=MhzKPh6snCAM4c6_e8faFxCO8TQhF4F73It0RrPvCSI10_t8navketl5hx9a6IOVUN_Yp4cryLGCV3o__Be2dX8gEMALTfKR3O_t_EKj8HRv_lONWSm3Z_J6ULFBAr8bSZvQOhq5hn6L5ziS5jFV4wMQvu6wp7-zdnEX46gbDyDrthFVsjaqzx7x8NcTnVMReYFCRaR0qYrnoBprCtx-X41FImlhLK7znlnE6_FByN-n_vRUxXXMqW6sI7j4GkNSdax6_eNiXFQ7gv4rtyX3f5O3cvx1f6b60dfvQdkFp9UvLZDJ2Jya1kCN4gVC4v3eeMxSH93-iAODopCqDNuGBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=MhzKPh6snCAM4c6_e8faFxCO8TQhF4F73It0RrPvCSI10_t8navketl5hx9a6IOVUN_Yp4cryLGCV3o__Be2dX8gEMALTfKR3O_t_EKj8HRv_lONWSm3Z_J6ULFBAr8bSZvQOhq5hn6L5ziS5jFV4wMQvu6wp7-zdnEX46gbDyDrthFVsjaqzx7x8NcTnVMReYFCRaR0qYrnoBprCtx-X41FImlhLK7znlnE6_FByN-n_vRUxXXMqW6sI7j4GkNSdax6_eNiXFQ7gv4rtyX3f5O3cvx1f6b60dfvQdkFp9UvLZDJ2Jya1kCN4gVC4v3eeMxSH93-iAODopCqDNuGBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌دوم تیم‌ملی ازبکستان مقابل ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107193" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107192">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=P7UZRFp54uuK95P3Izhq8J82BczS2co0LWVt18MtvVtl36b6YuC_5vGsGn9sENHVhps1AGwINMjeW9Xxbv92QhWhhhfFYkagwYnaBHloM3R2WYraLUDQWsg6taLJqMK2f2pf6r0R9aEvbps5W-e_tLSS5fXWRcoP7iUGp1MbBz__xOVWHhbbK9aAgTcgF7dZJmGGu3LIRudahuLU0fnQd-3hbV2UG3RT7sjk4181RRF28ZKZlr8vb3n3jNR5R6Mjxi90dJZ-nq_Fgyj_mwX0ZQn4xpjZYPJdQlsqT_wLvfz-eqqYJwJSdodIkhOqy-VBih8cudB52fiHBCS1-WzJWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=P7UZRFp54uuK95P3Izhq8J82BczS2co0LWVt18MtvVtl36b6YuC_5vGsGn9sENHVhps1AGwINMjeW9Xxbv92QhWhhhfFYkagwYnaBHloM3R2WYraLUDQWsg6taLJqMK2f2pf6r0R9aEvbps5W-e_tLSS5fXWRcoP7iUGp1MbBz__xOVWHhbbK9aAgTcgF7dZJmGGu3LIRudahuLU0fnQd-3hbV2UG3RT7sjk4181RRF28ZKZlr8vb3n3jNR5R6Mjxi90dJZ-nq_Fgyj_mwX0ZQn4xpjZYPJdQlsqT_wLvfz-eqqYJwJSdodIkhOqy-VBih8cudB52fiHBCS1-WzJWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه اعلام پنالتی برای ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107192" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107191">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592ed07452.mp4?token=qdIQ-JHTWNnedxu9-ENa6Mi6U6DEVEXCrofHvNE_YZnw1sUmmy2GHQ3QyjntYhv_u8AMU32FKnHf39y4XUban8VL_yte7VbInc_D3DKdu9n3yeEI_FKko15Y97cuLrhOl8YLqsvOE-8ck6PSiZ64SdYe8YfyR4yTrb8Lbno6dgEdTBKG7OpbILx4Og62yk6F4rRi6yZENRUgUZkaqju8x4huzHtJKYan_h8lUyHdcrI-uuaKzlElmdUkzpFpmsKd0RmeajrlCEreutQ9NKKRb30OzLw89iHPk4KHYWMzKa-Kgq-AcLMixh3CSakT4rAr_e8ROTcJq5MWBw_6f49QDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592ed07452.mp4?token=qdIQ-JHTWNnedxu9-ENa6Mi6U6DEVEXCrofHvNE_YZnw1sUmmy2GHQ3QyjntYhv_u8AMU32FKnHf39y4XUban8VL_yte7VbInc_D3DKdu9n3yeEI_FKko15Y97cuLrhOl8YLqsvOE-8ck6PSiZ64SdYe8YfyR4yTrb8Lbno6dgEdTBKG7OpbILx4Og62yk6F4rRi6yZENRUgUZkaqju8x4huzHtJKYan_h8lUyHdcrI-uuaKzlElmdUkzpFpmsKd0RmeajrlCEreutQ9NKKRb30OzLw89iHPk4KHYWMzKa-Kgq-AcLMixh3CSakT4rAr_e8ROTcJq5MWBw_6f49QDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول ایران توسط رامین رضاییان(49)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107191" target="_blank">📅 18:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107190">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMSNekmPkNe9-cbkgvG3unDZu78KWxMZwNrD3SrWlhgujXfpV_x8XWV28i2PPFSQ3opgU_IoNRVamPUcIj5uLyRCf0waTCM7eqZ7lfOGaPsUha3VnHVFecrpKTKn1ya4mOaY-nCbLIm7XrWBuKQsbv6TJvgbn-RbZtDUsoPEPuHWs4eCYMB0nxT67Cvwr6HKRGV_oIdb0Xz1cT6OeYmbm6b_Tv3r7MkqOhYNTmTf5zO1jrg-euF7LZyKzIG0Yec6kRWSLUufzUZxenc8Uva5A52KKcPRUqNqq4HiJqJTrvuTSDtp6mtr191ZTgPI07QWLZNDv77yib3O7ptR7zmdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا روز ششم مسابقات آسیایی ناگویا کشور چین تونسته ۱۳۰ تا مدال بگیره که ۸۰ تاش طلا بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107190" target="_blank">📅 18:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107189">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyI124zXF8Li1Dua_RRfEq2fFamnI9dHxvXHCEOCjI5qKywx7FM5Rsq9UtN4orWkh0_jfOnSWrUYPoien2td0aUw-1HKDKp4J4BtveNaQTQcuM8U_5TyCOY_Tz_ENzfYfqkcGHsclyELnp4ekgcl3UqwcMMnq6HfHh0_vmbYO0VvJ0EcCEnoRlk4W7oZZBORQ4DUPvhlsyzxVkgxD4r_-O1sDljZh7Aq3mYAdk7kHp9YSv5-Tkm9ONakKoVKpv5Dq6nWMm2k9WOozZBTSZj4D0K5iIcWHRBrvGnpkKgsAnIGvkiVPMJe9gLw1ckG0l7TANt54B_qWwPPCA51yDrpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🙂
واکنش یوز ایرانی وقتی می‌بینه اسمش رو به این قرمزایی که تو زمین هستن لقب دادن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107189" target="_blank">📅 18:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107188">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVOrQYhtvphSiFd_q8aNhcABNUtzT25_T21IbH1NLv6Zin-9Nhm4AUi5KqYcrrjbMbVv0gajDuPES99MAVf_vOrQIt-LBM9CQzF9uuY-c3lFpDzgOtgN6Tm--PuWgMRT5qijuDQQpa3qbnuRI5irNqbXMSUUR0kCp1KVphfYyOxtoMJG8kpGMPwskqM37a91w0uazEK2Ty8dnVnCuzddWQSB8uYu2g32D9JKY6IS1Uf9eVTZtS2wVaJ4nTGEspgsoEOfogu8H3YGM2dxE9l-PWv7Fnz8HmgYAyaFjAzVZ_k_iaEpTqQ9NoFCsYr0T0tHd6p1jiL35g-vRoE3ZvEJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
فلسطین برای ادای احترام به تیم قلعه‌نویی در دیداری دوستانه با نیوزیلند دو-دو مساوی کرد تا یاد و خاطره جام‌جهانی برای ایران زنده شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107188" target="_blank">📅 18:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107187">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz0reSK_lgKex5d6ORxyBXlSRlq4ZXaP_0O3Aeg4wSZlRp_0Dyk9iLfV35JKt8yA9DJJgdU94VjTO8N_wRHrj8RG5RFvYerMAZNrpenNWFwJIPuMEHzF1o5fw0cEi_4Sw7m-fFDgxqocumdyGS-1l33Xvn1DOtBMbsr-HzZdxbolZGGlO_aKlt8Hn7SjQkhyJhKAqO8nRXmFnjdoESc7ykGQ15MQEI0E17os5aYFWOfV3w5fHFuItZtpJi1VuiFi1GQPk5dha2Ej2AOX21RFhbHC1SyPbOJV7clSyFNLmSis1-Xwwnwi8EWnSpV7z4UBuCHECSZP4DPaWLIFkPNVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیب احتمالی برزیل مقابل استرالیا که بالاخره احتمالا شاهد حضور اندریک خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107187" target="_blank">📅 18:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107186">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAglttjaBE3tCxmYoWQN7yDqyDpOEwpm8dWNpBqF8CkCPmSCOWSqudyxYUaRBUhvt3LLyXUQuHTx6h5fexgr-wDKjzX9UQCVP9zw8MVegZ-HwE09bbtXhqsm8RSJWD0FqDZ_QKnWargj0WR_odxN0bPyAhjUHSYFeodiJGueU2lTsB1OU3qUPRJrSpm62IgxT9lPceseBRCsBEBSf6_EDoxJIoOucD_6KoRdotZdIvw4drCKco5pVvuqlJd6CBgwYcQ9-Dvf-09DbGqaIOgM2yfblgHaZwYSzJE2ldayR1yXH0bb0W_COZ1rZd7vYuAeSIor0j2heEEEzADcK28kJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لامین‌یامال: درحال‌حاضر در فوتبال اروپا هیچکس شبیه من فوتبال بازی نمی‌کنه و همین تمایز اصلی باعث میشه که خودم رو مستحق توپ‌طلا ببینم. البته لیونل‌مسی همواره در سطح فوق‌العاده‌ای بازی میکنه‌ و باید احترام زیادی براش گذاشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107186" target="_blank">📅 17:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107185">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=SxrPLWy0FZWb-I-RKK2jd8_Su1_Kz7XZFyBMghvlhFPavse1tkC3Qza701H4Gr5sco0xxJHZUfN7bKaqSsN4WRUc8wslTF-7ANpDUN0ILzzJWBb75dlWKeAw0TC9S2e9Radro5e2V5iysywIGsRAgXd7bwW698o1R2ZNRYnTMGNGQm-KYNAog2-e09GRlYuXNXa4BOGbhlU_-ZzgG7Pst11IJ-e5iZYknv6pbbKtCkn5CWt8uXDQGy9PxUgQ6g_PxokyVpnRsDC02cR_dZvt8YK9y4ly1uv7hWHAM4aEgx5seqepar6TPAYtnJYRnPoCEbdtgIQ4LnQEbSnfquM1dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=SxrPLWy0FZWb-I-RKK2jd8_Su1_Kz7XZFyBMghvlhFPavse1tkC3Qza701H4Gr5sco0xxJHZUfN7bKaqSsN4WRUc8wslTF-7ANpDUN0ILzzJWBb75dlWKeAw0TC9S2e9Radro5e2V5iysywIGsRAgXd7bwW698o1R2ZNRYnTMGNGQm-KYNAog2-e09GRlYuXNXa4BOGbhlU_-ZzgG7Pst11IJ-e5iZYknv6pbbKtCkn5CWt8uXDQGy9PxUgQ6g_PxokyVpnRsDC02cR_dZvt8YK9y4ly1uv7hWHAM4aEgx5seqepar6TPAYtnJYRnPoCEbdtgIQ4LnQEbSnfquM1dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اشتباه عجیب از حاج‌صفی؛
گل اول ازبکستان به ایران توسط شاه‌مرادف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107185" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107184">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107184" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107184" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107183">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egh-fpgP70qDOg-bmO4N5oEnOGUc589W9QOW9Zylnxlu_PyRvF7xvTUETBoPhC5751j-WmXav6ufKnx9MPfY1nFKUm2_4sIRoSTLa6jkwVY72cKB848ncusUnW_Z9qgLJABSZhELXuC60Aj_YhjzTKTza87slEMLQm5uuPl95XbKqj9xHYETaHS0O840erOz8D8UkEXpPHS3zdhqyPUIweZXihWlfHaiywGi5QmYJqBeLJwlyDxiau2lRVd32IuzOyXu2J8ldBMES7A_DYfBqHdaJojf-GdnPOWaUc3UNwcX07H6NnZCYbZ5JujJfaJnEGCvfDKj3qRkSpMooE3GQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
ولز
🆚
پرتغال
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ولز: ۱ برد، ۳ تساوی، ۱ شکست و ۱۱ گل زده
پرتغال: ۲ برد، ۲ تساوی، ۱ شکست و ۸ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107183" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107182">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmAsgtqQ6-9x1ibRo61hJbl0d78XzWc9F90BzQtSoFDhRTeoA1m40M3u5tkxOl57sgh2VjkVb9S4XD_oRUXi5jyibnka5ZbNEUa6qx1j-5yTwje3-6YxiIUwh62ski1aRjPbzpsel5rHiUt5odlOvz0oQdIRqd3fu74_AA23nxkUxnYw7yjhGvs-qWCAJKZoNZ9_jTMFvLhLBpQYkO4_67DgYOKIR9NQmQBYs-0fNOtK5_Evvdt39w5WDAZEk9fs6I1_RSmmMWRv6_tCGLe9VVURBxrQCYOpC8TWLuqgAZNOyJpRo4QxzKKKu46XymHbhl6WIn-6X5kyet5hpm3kMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
بازی دوستانه؛
ترکیب ایران مقابل ازبکستان
علیرضا بیرانوند، سامان فلاح، علی نعمتی، صالح حردانی، احسان حاج‌صفی، سعید عزت‌اللهی، امید نورافکن، محمدمهدی محبی، آریا یوسفی، مهدی طارمی و دنیس اکرت آینسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107182" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107181">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be9bc4836.mp4?token=RAkxAV0OlbBHiPzthZBPKgL1RcB5NHbmp5GCl3yTzokR_8a3RLC2mmI1dY9R8xCsdJDvrXp6jC64zDusLgXDolAhLpOVtpfCfwIb5JVHuNvGS8U57GB_HpCFnZ1vNQ9WRnhL_VNHbpVYGRmoTWDiprLBXLodG690V7HuXHGlpoLTDu6GYpbsnRtueK2W550IL-Aw8aj2CfM_fgG69cQV-JHQ7c13YiAgiz29Qq91K5hG-g-sbf_kHnwMA5G7oTVwoDJRsKFh4FvwhXst7yuvj0tTTkIXJTCEhIkUPBjoCFCnltPcrhuAqSg3gsBWjUBOSVepaikznTCXPWnqaqwtCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be9bc4836.mp4?token=RAkxAV0OlbBHiPzthZBPKgL1RcB5NHbmp5GCl3yTzokR_8a3RLC2mmI1dY9R8xCsdJDvrXp6jC64zDusLgXDolAhLpOVtpfCfwIb5JVHuNvGS8U57GB_HpCFnZ1vNQ9WRnhL_VNHbpVYGRmoTWDiprLBXLodG690V7HuXHGlpoLTDu6GYpbsnRtueK2W550IL-Aw8aj2CfM_fgG69cQV-JHQ7c13YiAgiz29Qq91K5hG-g-sbf_kHnwMA5G7oTVwoDJRsKFh4FvwhXst7yuvj0tTTkIXJTCEhIkUPBjoCFCnltPcrhuAqSg3gsBWjUBOSVepaikznTCXPWnqaqwtCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سوال‌کنایه‌آمیز خبرنگار ازبکستانی از قلعه‌نویی بابت عملکرد ایران در جام‌جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107181" target="_blank">📅 16:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107180">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a2786f81.mp4?token=s4pMswPANz7pXpgjyFomgZUeb3BXevsxUplHTQLAlnXShQ-MSKsobbCyLeRjErpCdBSaO_hzGVkHEq9KWshMgDk7dQ-U0b7jte4DReKVGLgc3xxYsCYbZoVOlsT3MIbPjqoEU-Z5EHXxlXSTPkPRvcDIiDCjASOGVgtHPLk8ZUqKf40o1qQFMFGuAIqRwZ-qUDvgR5_uXenVHwzlbzguMBlnfUtaXEI0tSs5pDXENEmxYHdGcxVGlnlemaUiwpNYLsTcOOev7iqFfF4QwDqGNiJpPqYGJtpdR_5yRsMDHmWwPi9HyB-4hwZz5R69eVYZQ6vR4Vux4ixZgcvi7NWWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a2786f81.mp4?token=s4pMswPANz7pXpgjyFomgZUeb3BXevsxUplHTQLAlnXShQ-MSKsobbCyLeRjErpCdBSaO_hzGVkHEq9KWshMgDk7dQ-U0b7jte4DReKVGLgc3xxYsCYbZoVOlsT3MIbPjqoEU-Z5EHXxlXSTPkPRvcDIiDCjASOGVgtHPLk8ZUqKf40o1qQFMFGuAIqRwZ-qUDvgR5_uXenVHwzlbzguMBlnfUtaXEI0tSs5pDXENEmxYHdGcxVGlnlemaUiwpNYLsTcOOev7iqFfF4QwDqGNiJpPqYGJtpdR_5yRsMDHmWwPi9HyB-4hwZz5R69eVYZQ6vR4Vux4ixZgcvi7NWWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👏
🔥
🔥
صحنه‌جالب از بازی کبدی دیروز بانوان ایران مقابل هند که واقعا محشر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107180" target="_blank">📅 15:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107179">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIwtIH63myBroea_PxGxEX56xiJ3Lcgx8Fo9F1XCIp0JA4GDR9_B05lQA_tVNfpfJwm_rQRqFa8ZsIwjpbvKZaxjY1Dq5QQft58n1kPHtrbU8IY9_HYc1yW0z80KDsN2F9qR2ELVqDHMkDZj6SBeafccYqZqqzNYW0O1Il8JUpmi1_reGjPHRNV0YH8pkg00Du_P3lHwVmGWKvhuHPOnxb7ov_t6R0OvibzVAwyQIzB8I9ahIOKWx0RCbUh44Kox2HKV3v9elmSBsnRl_VfD6NSoJ3umy7IWK8EVgVPeoMIxWPaBCIGjwzTc7RlU468RUaxeKL68RI-lEo6z4eLKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری امیرحسین قیاسی درباره لیست جدید قلعه‌نویی و عدم دعوت از مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107179" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107178">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌟
مروری کنیم بر ادن‌هازارد نسخه جام‌جهانی ۲۰۱۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107178" target="_blank">📅 15:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107177">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773eb10873.mp4?token=Ro8Vxacs8xgOftWp9Yh9_LW4TBdLv7GTmM4Y2e7ye5fodBeC2Y3uRHaJ-4nu-yxopnEHX1eKdGcYNHism_Mwq0CP5w2LJza34eUwMbZzc5seir6h2FHzc_ymK9zDvQ2jeqUy_XwmqoceWgfFjpfsqOgjzDVANvGbjp5oPg2Xlwl0uvAIYaIogHr_nPFwvv-tyTKZkC10oP5X9Zqar4nvt401ygvtkyXC7TG11PXpqmOUpJNDA72hUVugrMGKh1ly8IpnspFBezf1HX7POJuYHzqSgr3PxiAL_bN2sD1IfufVlgRcU2pa5xSXnh0zxtVRbCA9yVHtd5uFf-gSqn2PL4IuuAAKkmrMoGiRV4DnHIvN_VVK8ETWwP1Y_JBLOiL4uRBstM8GmmPrjamVs8HiYeLBpNxPCFNgWeiD0r-NgAl6HTsdmmwFZ2Lpya_0mG0zV8oSfYWpJEcZVgqQaQcf5gdDbzyNrHVVW9Jlmq0XmvswO3Jcf8oRMBeBUSz4IQUW1qGv256MIcZsFN7b_Cr-me7vf4yHYJY5dGt2RWEzVwgeK7Ypb9FZU_uuvzzqWP7I_7s66eAanEAGRHjvIfxeeZV0vlVRmpu1aRXHjiwdh1W9DV8wWuvDnVMzHtJaSHsRYNvex3AST3nJGhoL862xTSoI7URfBUYU7qQS2D5_FfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773eb10873.mp4?token=Ro8Vxacs8xgOftWp9Yh9_LW4TBdLv7GTmM4Y2e7ye5fodBeC2Y3uRHaJ-4nu-yxopnEHX1eKdGcYNHism_Mwq0CP5w2LJza34eUwMbZzc5seir6h2FHzc_ymK9zDvQ2jeqUy_XwmqoceWgfFjpfsqOgjzDVANvGbjp5oPg2Xlwl0uvAIYaIogHr_nPFwvv-tyTKZkC10oP5X9Zqar4nvt401ygvtkyXC7TG11PXpqmOUpJNDA72hUVugrMGKh1ly8IpnspFBezf1HX7POJuYHzqSgr3PxiAL_bN2sD1IfufVlgRcU2pa5xSXnh0zxtVRbCA9yVHtd5uFf-gSqn2PL4IuuAAKkmrMoGiRV4DnHIvN_VVK8ETWwP1Y_JBLOiL4uRBstM8GmmPrjamVs8HiYeLBpNxPCFNgWeiD0r-NgAl6HTsdmmwFZ2Lpya_0mG0zV8oSfYWpJEcZVgqQaQcf5gdDbzyNrHVVW9Jlmq0XmvswO3Jcf8oRMBeBUSz4IQUW1qGv256MIcZsFN7b_Cr-me7vf4yHYJY5dGt2RWEzVwgeK7Ypb9FZU_uuvzzqWP7I_7s66eAanEAGRHjvIfxeeZV0vlVRmpu1aRXHjiwdh1W9DV8wWuvDnVMzHtJaSHsRYNvex3AST3nJGhoL862xTSoI7URfBUYU7qQS2D5_FfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🎬
۵ پاس‌فوق‌العاده بیرون‌پا از لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107177" target="_blank">📅 14:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107176">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c32e4ce.mp4?token=s3dxxDl7CYK8JYTeDFI6FP7CEqgNAo4xSAQvCl3gPXgdD83HsSWj0M5xBxHJli-t5FFkrWYQOAC7k0inEgmko7DWMHClXMEjo0GIzkgEdvCTjFt11tQz_A81UuG5QtsoK4CC0Iw4pY8KvsWJxqAkBEgkTiQNXPM7UNwLGxH3T4iWHjvRV-VhDPaeRLsoZYNKREgiv0W1zDBQatgFZqC_U4Sx2hBWRoe20ADqI1CmKzvYjpQiiMN7gy0gFxTHwtbR3vuSYxKGk7e8GUXa8q_ZgD-ODenuJVfr8YnMUQTJ5xBxQjj41UHPBapGIIOb_xDLDmvngckCE15xFze1z7JetYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c32e4ce.mp4?token=s3dxxDl7CYK8JYTeDFI6FP7CEqgNAo4xSAQvCl3gPXgdD83HsSWj0M5xBxHJli-t5FFkrWYQOAC7k0inEgmko7DWMHClXMEjo0GIzkgEdvCTjFt11tQz_A81UuG5QtsoK4CC0Iw4pY8KvsWJxqAkBEgkTiQNXPM7UNwLGxH3T4iWHjvRV-VhDPaeRLsoZYNKREgiv0W1zDBQatgFZqC_U4Sx2hBWRoe20ADqI1CmKzvYjpQiiMN7gy0gFxTHwtbR3vuSYxKGk7e8GUXa8q_ZgD-ODenuJVfr8YnMUQTJ5xBxQjj41UHPBapGIIOb_xDLDmvngckCE15xFze1z7JetYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🐐
جوری که دیروز ژسوس سرمربی پرتغال از اسطوره فوتبال کریس‌رونالدو تعریف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107176" target="_blank">📅 14:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107175">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_9fDMeU9m9MAIiDfVJZHTheArLCh0xoxAU0tQDUnMKbmbHyWZiE1IInGaMGeo6MAo99xUlA_4E53CXPGtVaL9y_scoqb4An3fAUQFgT2NGt_lyacX5u0qpFcKpo3BQ6Hsdc00IRzx8OSM-lv2CX52reRlA1Joa_E2pSZFjdBe0HVZQtYoYWK9S20YI3ztq4768KviJ8WvQqKqu-y4OQj1_1B_T2vr6tZle4TjpamTy7z684K5dlDrnVb7Dn8dfXtP3xgE6zYCXRGnIcwtDCNFLsDhB1JSfuCrAF2_wmNpV_BVpDWUA141mmZne0UO24XC1TN-MXiquUv2NfPooIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🤩
علیرضا فغانی از استرالیا و موعود بنیادی‌فر از ایران به عنوان داور در جام‌ملت‌های آسیا قضاوت خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107175" target="_blank">📅 14:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107174">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=ZTaB1tWBzbGb66SFqs-LoNK7jfhC-brqPXdzhjbSNgO0D2Lr60i6dUF3fCNcBsKfZOdIpmVvY3sm_20InAep-kozuW5bX7fh2aLsD_PTVc_fMRu6DW2Wdl54V4dme60KbaHZ8Rl0Hum6PoPiGBTMcMKUSeX9r4D9KCeXYA8ADdWvik9JM38HwnCoJd5Nh1AZB3kweTSS2Aw5KaffFkHQDs9sk7I5Coco30JpktyNdyVGpzcuTbZIs6INsg0UDFoLbtoOC_8XrES5dw84hhvSQ5yTrdlpUxrKj-VEMwtS3W3fHQrn1tHAR_NhpLgemUFOMQK-QWil3yW2_B0hAiWlpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=ZTaB1tWBzbGb66SFqs-LoNK7jfhC-brqPXdzhjbSNgO0D2Lr60i6dUF3fCNcBsKfZOdIpmVvY3sm_20InAep-kozuW5bX7fh2aLsD_PTVc_fMRu6DW2Wdl54V4dme60KbaHZ8Rl0Hum6PoPiGBTMcMKUSeX9r4D9KCeXYA8ADdWvik9JM38HwnCoJd5Nh1AZB3kweTSS2Aw5KaffFkHQDs9sk7I5Coco30JpktyNdyVGpzcuTbZIs6INsg0UDFoLbtoOC_8XrES5dw84hhvSQ5yTrdlpUxrKj-VEMwtS3W3fHQrn1tHAR_NhpLgemUFOMQK-QWil3yW2_B0hAiWlpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
شاید حق با پیمان یوسفی بوده باشه
❌
🎙
پیمان یوسفی پیش از شروع لیگ برتر در برنامه تلویزیونی خطاب به سخنگوی فدراسیون فوتبال: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
🎮
دیروز: قهرمانی تاریخی پلی‌استیشن بازان ایران در آسیا و حذف تیم ملی امید از مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107174" target="_blank">📅 14:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107173">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=r85YDsrERmsmGemc8h94yqxLL1AzbhiQyqdZP3C00c71S6qYY0XBTNcMmXoB-VQRCvb7EXLMoqzfWePmXiyGf9c_kDiGtZXOqUG41KTfkQBmjfJ48quwMsk_kS9x3V_O8DZxn7VfZ2nCiPiwMLxtLo_YFY-4UxqJywCv70-Qr1_rUg55GkrLkux43_rCSFCvX1vRN06GBZxQ-j9Nt-NnCU3AqybNN4O4poRdotQvn2klPjtv_Uu0yiLTC5WEvDfP69r2vkY7jpBKVksDUVG3bHBKbNkD8BFI1z9PkRmxkNPan44e8OGDMpI0oJzU_UBC4Z1eFR26CPfMYsS08DEhhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=r85YDsrERmsmGemc8h94yqxLL1AzbhiQyqdZP3C00c71S6qYY0XBTNcMmXoB-VQRCvb7EXLMoqzfWePmXiyGf9c_kDiGtZXOqUG41KTfkQBmjfJ48quwMsk_kS9x3V_O8DZxn7VfZ2nCiPiwMLxtLo_YFY-4UxqJywCv70-Qr1_rUg55GkrLkux43_rCSFCvX1vRN06GBZxQ-j9Nt-NnCU3AqybNN4O4poRdotQvn2klPjtv_Uu0yiLTC5WEvDfP69r2vkY7jpBKVksDUVG3bHBKbNkD8BFI1z9PkRmxkNPan44e8OGDMpI0oJzU_UBC4Z1eFR26CPfMYsS08DEhhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت های جنجالی هاشم بیگ زاده درباره ستارگان تیم امید ایران؛ از انتقال به پرسپولیس، ده میلیارد هم نصیب دانیال ایری نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107173" target="_blank">📅 13:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107172">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی  «پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107172" target="_blank">📅 13:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107171">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=oraqsowHlI7xdYxR4bJe1xadZC3F-HXl1u0g2l9zzq9PAlYLSRREibXVE2u1pYUG8dxtKqtV1UTlSCSr3Pa94E1ceGnekIOyuIqrppdTYDiZB2LzTmN84hU-q0QpFXut_xH6fKc3wKX_tPQ1DQsrYusv_V4X0CpfKSDCoYVZVsRy2_IX7SGWzpQYucm8xEGZSqksVQuuF2ZUY3p7qzQn0tAl20eLO78TZ8pq2_lOglQGfY5_m95fE704OCF7aWz5kbDUX8XxugyQLjWDyRJZ8cseVzQPz3uCq8z6nl4Vugwtx-qsRm81GoInqXpXGFf_Sqz2dBn8OGw1miXoDq1Z0H4EYmmvOPkf4QnvAQX4b_PxLckAUqTyktvM6BZPAD12VxzSl4JozX_ofs1kEynjjywvjbuMTY8P7g2kyFl9FvSc9gOBlSogoCYBor_XVhLfqVxFYEqLfoQBbCQ7a5HDlEJDGDjDqhuRgbuYzjqpTZmW-zuaR2NLDzXntS5TdnOx9DL4uTXys4DyiziQbTrLBtjaS75mLOadp7tKghvx3B95b-5Q_oopXl7Qi5De0ftZ2as-CnRsvt00XofXKwZKX3g4smrwiI0lM30PqJBWBJa9Y7PPExpjiT88TjFwCl_6PfuG4XInElGM2hrdj6_YbvMwKok4zMbeKYUgXHqcf7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=oraqsowHlI7xdYxR4bJe1xadZC3F-HXl1u0g2l9zzq9PAlYLSRREibXVE2u1pYUG8dxtKqtV1UTlSCSr3Pa94E1ceGnekIOyuIqrppdTYDiZB2LzTmN84hU-q0QpFXut_xH6fKc3wKX_tPQ1DQsrYusv_V4X0CpfKSDCoYVZVsRy2_IX7SGWzpQYucm8xEGZSqksVQuuF2ZUY3p7qzQn0tAl20eLO78TZ8pq2_lOglQGfY5_m95fE704OCF7aWz5kbDUX8XxugyQLjWDyRJZ8cseVzQPz3uCq8z6nl4Vugwtx-qsRm81GoInqXpXGFf_Sqz2dBn8OGw1miXoDq1Z0H4EYmmvOPkf4QnvAQX4b_PxLckAUqTyktvM6BZPAD12VxzSl4JozX_ofs1kEynjjywvjbuMTY8P7g2kyFl9FvSc9gOBlSogoCYBor_XVhLfqVxFYEqLfoQBbCQ7a5HDlEJDGDjDqhuRgbuYzjqpTZmW-zuaR2NLDzXntS5TdnOx9DL4uTXys4DyiziQbTrLBtjaS75mLOadp7tKghvx3B95b-5Q_oopXl7Qi5De0ftZ2as-CnRsvt00XofXKwZKX3g4smrwiI0lM30PqJBWBJa9Y7PPExpjiT88TjFwCl_6PfuG4XInElGM2hrdj6_YbvMwKok4zMbeKYUgXHqcf7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107171" target="_blank">📅 13:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107170">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=nLERqcPp9tFoPgn2X9st_jguj_ZhMMhhAzk6qzrE0eNCmvg2p_sTzhXx8-ilk8GT9E5m0FRjubVIAyfBOuEqvrB3F90NCmqfXp81zX2V7U99JbhESCks9jlHT51SuBTVMdnMwQ4CJRA07_Fb99SsmwRaGiFbS4BUbxhpRpJ72Lh_iClQGFP2xRLBqQkdFDzPrrehpgaHKLy2ZkISKMqu6GznU1ntNYFR73ib_lsXfKvkpcbrWPAcA2TKxzeiacevZ5UsLe7LOi9Y6VAjw3lG_pcWKy_LWs-mj1J6s3U4hNu1EBuCpNyyyT2HbLrNSzYzOHSsiN2EbvFYiDZMPlHAboO6IgINvlBvF-Htu9dsk15DX9UUAnPpYqnyttdcxN7DVtXwTZKoduqcXwM1omHypeGI2PNs_D3H6B8cv4t8vrJzlmEoQkVNT0WfPNs414JCbih7JZbAmC835ltdCP1U0AGN8Rf_usNac-unStB6YDCoJ77B-L2Rkw-HeQNYD79axhNxvKZaEV0DZBYKWOYp0xV3zfbyPRy8OikVaoZ9TyolU65HPkyv6Kcv2ENYqynZrW-rKkphdRFz-QYmrvayGjysy9eg6tI_shxdGXtGyUGVR4sSf9gLIrGBLY2h0kyUipNlz48r_ylxHW0-ck4NtsGBfrk25UWwjWiCDLiJ3uE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=nLERqcPp9tFoPgn2X9st_jguj_ZhMMhhAzk6qzrE0eNCmvg2p_sTzhXx8-ilk8GT9E5m0FRjubVIAyfBOuEqvrB3F90NCmqfXp81zX2V7U99JbhESCks9jlHT51SuBTVMdnMwQ4CJRA07_Fb99SsmwRaGiFbS4BUbxhpRpJ72Lh_iClQGFP2xRLBqQkdFDzPrrehpgaHKLy2ZkISKMqu6GznU1ntNYFR73ib_lsXfKvkpcbrWPAcA2TKxzeiacevZ5UsLe7LOi9Y6VAjw3lG_pcWKy_LWs-mj1J6s3U4hNu1EBuCpNyyyT2HbLrNSzYzOHSsiN2EbvFYiDZMPlHAboO6IgINvlBvF-Htu9dsk15DX9UUAnPpYqnyttdcxN7DVtXwTZKoduqcXwM1omHypeGI2PNs_D3H6B8cv4t8vrJzlmEoQkVNT0WfPNs414JCbih7JZbAmC835ltdCP1U0AGN8Rf_usNac-unStB6YDCoJ77B-L2Rkw-HeQNYD79axhNxvKZaEV0DZBYKWOYp0xV3zfbyPRy8OikVaoZ9TyolU65HPkyv6Kcv2ENYqynZrW-rKkphdRFz-QYmrvayGjysy9eg6tI_shxdGXtGyUGVR4sSf9gLIrGBLY2h0kyUipNlz48r_ylxHW0-ck4NtsGBfrk25UWwjWiCDLiJ3uE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🔸
مرگ مغزی فوتبال ایران طی دو دهه...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107170" target="_blank">📅 12:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107169">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261876d28b.mp4?token=NM5mvuSKFjAocWyf-S3QkBNPKglSf5X2Khpy1Q5Z7_ooNqBwnFb7djOFip8xFVRiH2pVPNdSg-djAsxEg8M-wATFz4RsTvSv8ZdJfJ_JHaZMLw1wzaXCpKeKcdEAX3l-MWRsH8wHncQ96rb0-F91KbxUdoNskeGhAfDhcm8wbr_CO8Rnk2ActbXGeayy4vJFgEUvNiyM8qJirOgUx0p-KfHs5g4cPwM7M02vXjS2QqdA4RTVnXPPNZj1MslJIierkGNMpkexmXN3ee-X0tkrsH_onSDXzCwqhJjj3eZ4rsxBsVhkVIgp4BN67y3Wi1k0HQPyO0VsrZdfQCtntt4F7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261876d28b.mp4?token=NM5mvuSKFjAocWyf-S3QkBNPKglSf5X2Khpy1Q5Z7_ooNqBwnFb7djOFip8xFVRiH2pVPNdSg-djAsxEg8M-wATFz4RsTvSv8ZdJfJ_JHaZMLw1wzaXCpKeKcdEAX3l-MWRsH8wHncQ96rb0-F91KbxUdoNskeGhAfDhcm8wbr_CO8Rnk2ActbXGeayy4vJFgEUvNiyM8qJirOgUx0p-KfHs5g4cPwM7M02vXjS2QqdA4RTVnXPPNZj1MslJIierkGNMpkexmXN3ee-X0tkrsH_onSDXzCwqhJjj3eZ4rsxBsVhkVIgp4BN67y3Wi1k0HQPyO0VsrZdfQCtntt4F7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
🇩🇪
هلند - آلمان⁣ امشب ساعت ۲۲:۱۵⁣
🔻
اولین تجربه یورگن کلوپ و ژاوی روی نیمکت دو رقیب سنتی⁣؛ کلوپ: شرایط هر دو تیم مثل همه اما من نسبت به ژاوی بازیکنای بیشتری رو در تیم ملی هلند میشناسم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107169" target="_blank">📅 12:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107168">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=Wc3MG__VJ-YbKxdPlVj-D5WWFjqJB_9zefPT66ue4pzZKe-TY0yjSxYNBXYJOHfig8yOU9AJiJpTAqdnujI221r0SYM3oesmNvcHd0bhhxcaqHlEsmfk-87-L7T5JfTwXRf49CcvbEEBzvTWz4PHPo5c1-RokEIVf6rR1b2sniS408FzPzfTMTBoqscMAA9d75k3FStHsS2jHr38_2uvlaORTrBCNz0wT73-CegXOKwthpDlWiRQHkfYXQQ1uWSZdd1cMHSMKNcUdvAHrH4WBl50tr9mKKevT6NjSYFnOJ5l6LHPI3Sz1EgqvK_i0QOM-oPq64BIGTdNrIv-fLUNTy1OcN7l5K8DWVuWop1z8_S1-Z566LdXd-X0fioyCds1b7P8bSBLuf-Qh-BQ0V5UqTpB5SIRGv9oGr-wfDPEFJp9BRIND8rkCF7XMi6ti-DbXNx-q6FYvZDvFJ5IMkjLluhXk5NqmzX6F627tCHZk_SzT3RUz0unozKyEMKqpbO_C0wfTY5yoOV5XxEaRDcQNFEf1ry6oQuSxlk-lKKnjzb8aDdqi8XzsdaIcvvsh_MRkOOK3LSBgY8v8-aZqjG52SO3IifUSVNHIGxSXh_9LfLjBJ03d_R5Js_uDI7y_-gMbSxa5Mg5VxGsuun8SbSrqv3waVYRIxJ3nS9nwAGNBZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=Wc3MG__VJ-YbKxdPlVj-D5WWFjqJB_9zefPT66ue4pzZKe-TY0yjSxYNBXYJOHfig8yOU9AJiJpTAqdnujI221r0SYM3oesmNvcHd0bhhxcaqHlEsmfk-87-L7T5JfTwXRf49CcvbEEBzvTWz4PHPo5c1-RokEIVf6rR1b2sniS408FzPzfTMTBoqscMAA9d75k3FStHsS2jHr38_2uvlaORTrBCNz0wT73-CegXOKwthpDlWiRQHkfYXQQ1uWSZdd1cMHSMKNcUdvAHrH4WBl50tr9mKKevT6NjSYFnOJ5l6LHPI3Sz1EgqvK_i0QOM-oPq64BIGTdNrIv-fLUNTy1OcN7l5K8DWVuWop1z8_S1-Z566LdXd-X0fioyCds1b7P8bSBLuf-Qh-BQ0V5UqTpB5SIRGv9oGr-wfDPEFJp9BRIND8rkCF7XMi6ti-DbXNx-q6FYvZDvFJ5IMkjLluhXk5NqmzX6F627tCHZk_SzT3RUz0unozKyEMKqpbO_C0wfTY5yoOV5XxEaRDcQNFEf1ry6oQuSxlk-lKKnjzb8aDdqi8XzsdaIcvvsh_MRkOOK3LSBgY8v8-aZqjG52SO3IifUSVNHIGxSXh_9LfLjBJ03d_R5Js_uDI7y_-gMbSxa5Mg5VxGsuun8SbSrqv3waVYRIxJ3nS9nwAGNBZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇪🇸
آنالیز ویژه برای درک قدرت بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107168" target="_blank">📅 11:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107167">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-ehimdCifZ0Ca3RR7ZxGEcX8Ade8_VhPq-NNcXgpKk1gvkrQfARLYt6AZSFRS1-q9j4pcqTivFdGJkh1ckgMhrzB0ManxTqC8MxifSTWEs4Lwi4HaJ_XuYUZBpMZ29QXrHwHwXKK_XfVD7pO8RM5l3CJ_GFB8rHVYbXhhOi_H0DAY9gqVP_IzX64Z9yl9DlhT-EdMuTbIFk0E0Z9fJH4T4ZSummVSglzDkiQiCLM1JWgZiVqJGqvWxw39-trxtxlmjU8SVXjhXt4MHvqQpHeM9G0kzVc9ySrYWvqifMdqj7TSBlemoA7GY_Px9Tjm1Tb33bQb02hSCRFx41mJ_a3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
5 بازیکن برتر از نظر تعداد گل‌ها و پاس گل در لیگ‌های معتبر اروپایی تا به امروز:
🔻
رافینیا دیاز – 17 مشارکت (گل و پاس گل).
🔻
لامین یامال – 14 مشارکت (گل و پاس گل).
🔹
کیلیان امباپه – 10 مشارکت (گل و پاس گل).
🔻
مایکل اولیسه – 8 مشارکت (گل و پاس گل).
🔺
فران تورس – 7 مشارکت (گل و پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107167" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107166">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107166" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107165">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmpyqLS2veDegP46-1rnTKlspx58bd6FkFyXyvOpPBceWM9rMVQV6qoh02XFjuh0dVgS3bd8QySgxl2463GxuO3MwmP9l_ObSPoAdNJWa8CFd8yZ0xQphadpoBYpKxzee44_Adf34OjKDisUFjEAHjZYrw-Hyvzz8omt50Tf_7tltpgW2ypjVCUqE8SVIjc9PthuYUBpIM1X-IRf3WlMmIEdBT5--RCCbx19sK4CBW2Jp3i3wqdxdM-furB4owl5VVIG4y6_uitM5Af7eJ1Hzt6JHcJZiHI1951mL3n0raptEyFXGOdJdPzA_7oa1o3rPguL_kSiiug9H1SfEKmZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
هلند
دانمارک
🆚
نروژ
ولز
🆚
پرتغال
اروگوئه
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107165" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107164">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwpcrcaeaXhCrY7ipgdlHZM6VRO7V027AcXIU1GAKrk90JSTfofyVAyY0MK4hd3-PwKYAR0L6WszizBmTlw0C8y0IkOH5iuzIBMAxnwMzBdiWe7OGXFnKP8Xu4FKVmwFD4F9HwmVu2wp4uZvjss-Haw_3qi3veWuPY5okFzeG-VvF4my49TemEKJakXvjjCm4EgANWErYhHSY3q7GJTrvEwgOsWMHwxFjf8SPUgI9fmqLXXj0jCqcMzcjNjbQbMXrziyld4KrItFjzTECnmJNAxb-OceFD3MrYVseHwKQYE9u7zxv39acwrG3DgYAoTtTv0cmLw9IZpUfugp2-EnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🔥
بیشترین تعداد گل/پاس‌گل در لیگ‌های برتر اروپا از ابتدای سال 2026:
🇪🇸
لامینه یامال - 24
🇩🇪
اولیسه - 24
🇩🇪
کین - 23
🇮🇹
مالن - 22
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز - 22
🇪🇸
رافینیا - 21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107164" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107163">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=sq7DQMhwsI71il9hKXx0Fbeeg6t_O2nhrFsBHwE6kKaG93pGSZI1RDrvtVrhMXZ2Ol9ahcS0p0oqJEVsdWdqiYL7Hq4WqDfAf43KoBaMA1CmpIEOzu9wppnuvIPC_Irm2L6X_YwEMgQ1SBsoxzPPwD0CaRytguoL0qIwnPys8-Ct0vhhxkQ9tNB1IjkAEGovn5offSvm9HU4hDqCm_rSP7dTbnzeUwa7m_mVvuB3JSeysQMoW7kaHiYsBHdaVRjUL4R1F02IGMknAKAz9dH1IKynvu9VTXAzv652WpHE5OWM21PitJ0eGO0rdpzC3Ng0RJcYPXPdzegfdshe1_4pFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=sq7DQMhwsI71il9hKXx0Fbeeg6t_O2nhrFsBHwE6kKaG93pGSZI1RDrvtVrhMXZ2Ol9ahcS0p0oqJEVsdWdqiYL7Hq4WqDfAf43KoBaMA1CmpIEOzu9wppnuvIPC_Irm2L6X_YwEMgQ1SBsoxzPPwD0CaRytguoL0qIwnPys8-Ct0vhhxkQ9tNB1IjkAEGovn5offSvm9HU4hDqCm_rSP7dTbnzeUwa7m_mVvuB3JSeysQMoW7kaHiYsBHdaVRjUL4R1F02IGMknAKAz9dH1IKynvu9VTXAzv652WpHE5OWM21PitJ0eGO0rdpzC3Ng0RJcYPXPdzegfdshe1_4pFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های جالب دکتر محمدحسین پور غریب درباره اهمیت ورزش: ورزش اوقات فراغت نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107163" target="_blank">📅 10:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107162">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=C8ZMOk-jkfSrCcstcYuRDVQvz18qPwvdeW5eewEvWd7j6ZSZitR690WiH_3AVIbQcsWS_x3GC21ETt-DmmmBuK75fZXdpFii3iYsMH5QvTpX_5m_ebL7VWghh94kuvXaAd_9pohMVjcE_3A6t_LVdHT0DLUL77NMnWP6IIPXNW0L4kzucm3mEyj9Ej8AYDVtajcMnV4BMnZbf58q3BkZ8W4D3VsQdgBmvIZ06jQ7f7qtzYYwUtyezga5g3zHSWgeUOe7a_Gu31bHLAs3EqvHl9x-qAlfDjj5Cu19XoT1-NsQPGhJDWUjEE1KYUTWE39uOAo2voCgS_Tu5DdoP1E4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=C8ZMOk-jkfSrCcstcYuRDVQvz18qPwvdeW5eewEvWd7j6ZSZitR690WiH_3AVIbQcsWS_x3GC21ETt-DmmmBuK75fZXdpFii3iYsMH5QvTpX_5m_ebL7VWghh94kuvXaAd_9pohMVjcE_3A6t_LVdHT0DLUL77NMnWP6IIPXNW0L4kzucm3mEyj9Ej8AYDVtajcMnV4BMnZbf58q3BkZ8W4D3VsQdgBmvIZ06jQ7f7qtzYYwUtyezga5g3zHSWgeUOe7a_Gu31bHLAs3EqvHl9x-qAlfDjj5Cu19XoT1-NsQPGhJDWUjEE1KYUTWE39uOAo2voCgS_Tu5DdoP1E4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول مهر به روایت تصویر؛ صادقانه ترین مصاحبه مربوط به سال تحصیلی جدید
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107162" target="_blank">📅 10:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107161">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9544f249c.mp4?token=CX5IAZmLeGeKF9EMrH8HxnoVXStZDgQKcLXilRV8xHkq0zJIkQlkQKoSgrd7omHyWgxVy6n_cm3G0UTq1dtVRLTaC5nWREohN00Oyyg9t53OjELvbuVfsp_nnsGiVW75kkPthgaMRrqWXJOo-JQpYw0ZcgytGZFF91R5T3rToZzEx5jJogydR_2CMf-ReqzMXw0i_4giaV58nCGPbIRVElavzD9jUkR_nLSHLN03JCMJFGb7jWnn_b2BlSEd3FR5j3unpyXkRWn505mFFwECgpjfidLdYCXCdgrOcYkpupfih2DEiT4QDQwzNPrijDdgIF3kNBkq_AjfIrphN6ExGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9544f249c.mp4?token=CX5IAZmLeGeKF9EMrH8HxnoVXStZDgQKcLXilRV8xHkq0zJIkQlkQKoSgrd7omHyWgxVy6n_cm3G0UTq1dtVRLTaC5nWREohN00Oyyg9t53OjELvbuVfsp_nnsGiVW75kkPthgaMRrqWXJOo-JQpYw0ZcgytGZFF91R5T3rToZzEx5jJogydR_2CMf-ReqzMXw0i_4giaV58nCGPbIRVElavzD9jUkR_nLSHLN03JCMJFGb7jWnn_b2BlSEd3FR5j3unpyXkRWn505mFFwECgpjfidLdYCXCdgrOcYkpupfih2DEiT4QDQwzNPrijDdgIF3kNBkq_AjfIrphN6ExGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو از یک‌تئاتر با حضور مهرداد صدیقیان و فاطمه مسعودی که حواشی زیادی داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107161" target="_blank">📅 09:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107160">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5567bbdad8.mp4?token=SdDXXZYw0r2GpGaMJcA2ym6e13aWJBgpWQ6Nzyg1hnkXJWu4WQul7kK8oAFPCD1n4Axp6Y2XgPI9fPpklxILeywdGFgWezhpQ4J7NQcz7I0JhFwGylemWC-jHcq7eIFCCM94xj6olbjm2vOL9IYBFHFuL0pitH65cpU0TErH7w0s70I4bQVhEn2Oad-DpVbBRdvUgjqoObEsV7e1YpkURjgdOMTaSkDc98fv2oaBD2ZEI4Y4nw4MpRBjnxMUBk-B8ez-V-cyKl-eFXusrNHC95NdzXI4lhn5KZurx2gJM2tWY7sY63UldLLaW_Tt0jklLp51jJLkkjZpRKQitoaMEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5567bbdad8.mp4?token=SdDXXZYw0r2GpGaMJcA2ym6e13aWJBgpWQ6Nzyg1hnkXJWu4WQul7kK8oAFPCD1n4Axp6Y2XgPI9fPpklxILeywdGFgWezhpQ4J7NQcz7I0JhFwGylemWC-jHcq7eIFCCM94xj6olbjm2vOL9IYBFHFuL0pitH65cpU0TErH7w0s70I4bQVhEn2Oad-DpVbBRdvUgjqoObEsV7e1YpkURjgdOMTaSkDc98fv2oaBD2ZEI4Y4nw4MpRBjnxMUBk-B8ez-V-cyKl-eFXusrNHC95NdzXI4lhn5KZurx2gJM2tWY7sY63UldLLaW_Tt0jklLp51jJLkkjZpRKQitoaMEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«پسر بد» در روز اول مهر الگوی دانش‌آموزان!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107160" target="_blank">📅 09:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107159">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9d6b05a55.mp4?token=rfmtjYp6BnuAMgSIJCyOO8lTtB5MoMsVk19BZC34GHbJ65MDWl6Rr8FVRiF27dZkxP5H8A6gNpAF21CMzpmbo7QQb_0HyHpRQGUp8_QXvWeQmPEF_QEyOfe7puJw9mHQuK3uKE2EYHozALkRC-1HrvAfmw8UvXku_6PvUJKi-7qWxVJG22nA3p0lh7QHRLTtOQ4gJf8UVIXLsQMocOm2Oe6fsIBbB390kOTkObg_YPAZmp-Y3pC6QBzjYnfO8Eq-cCYQR5gJK86q10pWBVzm5FvbHusbQZpRBLPGNITN10cilzcWSe6IR-t4Fcxm_VdkgPfG2m4PfyaxaYMLOcl8tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9d6b05a55.mp4?token=rfmtjYp6BnuAMgSIJCyOO8lTtB5MoMsVk19BZC34GHbJ65MDWl6Rr8FVRiF27dZkxP5H8A6gNpAF21CMzpmbo7QQb_0HyHpRQGUp8_QXvWeQmPEF_QEyOfe7puJw9mHQuK3uKE2EYHozALkRC-1HrvAfmw8UvXku_6PvUJKi-7qWxVJG22nA3p0lh7QHRLTtOQ4gJf8UVIXLsQMocOm2Oe6fsIBbB390kOTkObg_YPAZmp-Y3pC6QBzjYnfO8Eq-cCYQR5gJK86q10pWBVzm5FvbHusbQZpRBLPGNITN10cilzcWSe6IR-t4Fcxm_VdkgPfG2m4PfyaxaYMLOcl8tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
علت‌احتمالی عدم‌دعوت قایدی به تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107159" target="_blank">📅 09:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107158">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKtX1CnBvLG75i3lVVgmubd05odZE6d2Ab2KBYMzvchu_pFwTFiV7ehd8t6EjsI_qxqA_UKTgIpyJR0r3C7-6NxN8g1OJDretzpBquLn6_k9RgohyfDnVDXJNRsNbcSdewGdyBMomK1dgQKopHBvuC41yLJqCeT3uuF8_VLsnukIrRuu6p0tdpBGv3roscLBjn_IAjLgmHpW92poBtY30inkcqqPJK3KDTkphG3V7x9f4urke3WR4mAZQKYvy5cYPDCoR-IbReYXLo3ziprnKbT8Zm9sQnSW1oAeoNuRAYpOF4ejX4lkhr-dUD7bIU_FJyTlUfTLARZrXZcN7NHX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
آخرین پیراهن آدیداس برای آلمان پس از ۷۲ سال
؛ از ژانویه ۲۰۲۶ کمپانی نایک اسپانسر ژرمن‌ها میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107158" target="_blank">📅 08:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107155">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO-9pJhcvzuL2umLbbrRycauIRjN9Xb2W52D1hvRC9PHNTAuOioWGXE09hJnkmjH59S43P3rnr0snTItbblcQghJa4I-VGwH8FpOlr9koRhnYZGMVC86J4rZ2CutHJCu050ZaXPPlEA2reznNzp3W9oDb2Tly1SyIUAYgGjQ5BjMtmAndJbHJWZYZI_KdTz1_0GHbOmBpUjeCZ9ar-09ZLljolctJugWEge1aEOGtVhTQzVBdg9e-BuCZT7y3oQklfTCdUa5KaIhCEfx25O2vFnNFl06sgsNfW9c25-AsoAXjRYlytRh9o2dDlXre6xCyEpifndsTimcnVM2n_fq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ژوآئو فلیکس: درسته امباپه و کین فصل فوتبالی خوبی رو داشتن ولی به نظرم لامین یامال خود فوتباله و کسیه که مستحق دریافت توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107155" target="_blank">📅 01:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107154">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
دیدار استقلال و تراکتور بجای ۱۶ مهر قرار است روز ۱۵ مهر برگزار شود. این اتفاق احتمالا بزودی از سوی سازمان‌لیگ‌ اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107154" target="_blank">📅 00:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107153">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tavihm13E5E4y2NIBv4Gj2Us_POZrZrYRyu3Q5OLa_bLEAGIMUa7Ns5lR4eK-PYjv-ciLHYhyESFZRe-WlN-FPZe2rqvvpWQ9T6H09DHm21wy84A1SIh152EEyUQjkZ2-WV09Uh3ZNj49ODU7n68c9rGfZKp8Cqq1eDSkHsApfd8VR3vBnBg-sZfIf70xrhikx4rwtyjN7H4UJYhtXsmOp0oLAYwoTE318mtbBsi9hpXlLh178y7MdoU_QnkUfAistKZWj-fZWDFyFRMeY7S3alTjFOAFhRW1pwtKN7kov0K4rh-_YiPRm2GEIdb2gLcK2YsvoNEmTpJYIfwKk5tJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
دیدیه‌اندونگ بازیکن سابق استقلال در لیست خرید جواد نکونام برای تقویت تراکتور قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/107153" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107152">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=cIfMxguRLiFRSklGCv6creitYKlGB0d6uM6GL1Kzj2vO82_l8c5pJxPFhwLoDZE-79YzvUtfkV_v5-mF9RLuHpT2FTkMpCJoPTTp4lYD0vrYq1qLppiaIMLi6yj9mZ8_MZb62RxCWq5gdWRKqluSEGulsuhPA-ru2AA3CP8k6EJdKQddxXlfCCSMOjzqEbfiJBSidoZLNeh1NNH1vs8hqJ1uPw6qpTkiuKDLqsEGS3boyxl6vDEaD0NVWV8xPkg4H4huBFkoy9dwtwdh4tLr0eGeWs76ewUvpWWRSkWgT2Q9I0LBKl-FDbuViAN6ir9-SPewZpPX9bVPy3IwlDfO9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=cIfMxguRLiFRSklGCv6creitYKlGB0d6uM6GL1Kzj2vO82_l8c5pJxPFhwLoDZE-79YzvUtfkV_v5-mF9RLuHpT2FTkMpCJoPTTp4lYD0vrYq1qLppiaIMLi6yj9mZ8_MZb62RxCWq5gdWRKqluSEGulsuhPA-ru2AA3CP8k6EJdKQddxXlfCCSMOjzqEbfiJBSidoZLNeh1NNH1vs8hqJ1uPw6qpTkiuKDLqsEGS3boyxl6vDEaD0NVWV8xPkg4H4huBFkoy9dwtwdh4tLr0eGeWs76ewUvpWWRSkWgT2Q9I0LBKl-FDbuViAN6ir9-SPewZpPX9bVPy3IwlDfO9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسپلور گردی احمدالشرع رئیس دولت سوریه وسط سخنرانی‌ها در سازمان‌ملل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/107152" target="_blank">📅 22:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107151">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpWCRab1A91Nx1W8l50oNJ7uUzvcOZTnCTRqwCy8SroNzL5G0TJ4Wb9TrwxzKsNQVGvWRnyHqObvOH93v6FkYqCT7FI6jnEp5xAhmAXWUe-fk5TxcLHzb-grKlf2sGjbKOhEAsje55fh4xDZ0djQKgFzG_WxCLAELB05uvxRk09AgCL6tVARXDu_iQLYixaW6DZgZ9RqAhSzy5ldUWfduCv7lwY_nEf93jFS24YcxW_NEbJ_TKHiYAvW5fg9TwBnm0xYEqGjcGx8Ngp3opwHnxv-oCpoL_B5Gmn21CYRGGucgBp2Wh0BdHhtaH7a7lPBZhF0H4NtQ9xjbuSK3sNltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
آخرین بخش صحبت رونالدو در کنفرانس خبری خطاب به رسانه‌ها:
بعضی رسانه‌ها عاشق حمله کردن به من هستن؛ اونا سال‌هاست که سعی دارن من رو از پا در بیارن (بکشن)، اما این کار هرگز روی من جواب نمی‌ده. شاید با یک شات‌گان جواب بده، اما حتی در اون صورت هم من می‌تونم از گلوله جاخالی بدم.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/107151" target="_blank">📅 21:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107150">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=HDwD-qf2Jw684NnPTYWeGrKcv9t6nKCHGi8Jp7JwGtsGojpt_y0K4G_PHRgvap9gv9P3e-iraUTu6_OrmxuexhT8I03L5tExQABy76htutNkCKPV9HkJuypskrAw4D4lA-0DTFZIQ_PV8MNR7poztCdlXdlUZ_ncIaHY6-VFB7xJAd2zKhomrfYtrJ8f3h3VFzckhtTXfjsrPsUmsVi2vo_Qygr3PBuM5gVLfmtKFqyCiRiR9_nRg2BNfujWMuit6t1DcVehLt5YeoiSFNGFlt-aLSP8Q8-LC6qeK2Cv9Dnn5ONk4lkOxcSxRt9SsnyLUB4AbuGRRBAei2_GHgPCoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=HDwD-qf2Jw684NnPTYWeGrKcv9t6nKCHGi8Jp7JwGtsGojpt_y0K4G_PHRgvap9gv9P3e-iraUTu6_OrmxuexhT8I03L5tExQABy76htutNkCKPV9HkJuypskrAw4D4lA-0DTFZIQ_PV8MNR7poztCdlXdlUZ_ncIaHY6-VFB7xJAd2zKhomrfYtrJ8f3h3VFzckhtTXfjsrPsUmsVi2vo_Qygr3PBuM5gVLfmtKFqyCiRiR9_nRg2BNfujWMuit6t1DcVehLt5YeoiSFNGFlt-aLSP8Q8-LC6qeK2Cv9Dnn5ONk4lkOxcSxRt9SsnyLUB4AbuGRRBAei2_GHgPCoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
🇮🇷
کنعانی در دربی سامان فلاح رو تهدید کرده بود، حالا خودش به تیم ملی دعوت نشده است: «نمی‌ذارم پاتو بذاری تیم ملی!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/107150" target="_blank">📅 21:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107149">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw2O5F-8AFeQW4fQISdiWhB5QDh_Fc7P4CGhXnWr5Vub5wv0D54j2xsJ4QFlUITs-vVN22DI6fRlgxMI_leubxfaLEhW9RqXsBi4HVTdqQSpCeiw9FuT1EYW_lu8lWuhgCAmo9MQXZsuPDnBsKqpWuPgCjz6JessFt4_WDFM4OtuaFLGwua5JFznTGTQnWh75A_ADJj4hL8HfSxL-o6FWtkaUlgCMaxu5TuJYw-1k_37fYNTFYHFiqhV3bjGyT2kzxfaw9k2jFXHe7VVNHWEOrohgno2PfbrlaUU3YPztnoNlGuICQT7o_rtOIX5UwwYvFeowGrYUpSnmu2oPy7boA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
اپدیت جدید تلگرام از میانگین زمان سین زدن و جواب دادن به پیام پیوی ها !
اینجوریه که مثلا وقتی وارد پروفایل یک شخص میشید اون قسمت بالای  شمارش میزنه بطور میانگین، چقدر سریع به پیام‌ها پاسخ میده مثلا 5 دقیقه، 2 ساعت یا 3 روز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107149" target="_blank">📅 20:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107148">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=jId5jC_iLyQKO5pvsPgjkIZ29XqxUnCnRcj-8SK_CaMOE9pqO4Cywh3CwKsV-fsfo7JlvLGaVwa3aErhhnIpfsyD_3M3Hzsc8Mxfv4gIjJCkhyRl88Jhq1qJFQJQQ0v_6B4tw3_4t_N4YHkwA924rEAZqgpNkH97ikrzgsuSLYVCZFJ0blfb3qMr7C3TdJS3a6rpl6QGwP3b2L8tz9yjjquxYd3F4VUzKZgiZ_JQAYCaF5FIwYy1XGC3CvW2xvfGv3FGo3rmmOt4ibDFrSLZGvQtQNbbWfUb0TBtjuEcHTEBHS7AiW8h2wjx2QYD5Oa1nB_qnY_1HZnu5TdSVP_6iXbwE-1sqwOv0Sflye2yatBYfZPB89bIATOfTwd6jXnhYIbmdiwXoptHyDD1sCFqKVGXTrskeZ8jqHBHpaspI0Y02f4dwKFLOqS87w5NAv-Dk1QsVKnjM2VjB8KnAEa3WU83DHtdMzD_VdDbMLCwqzsmTmAZo3UwkmsjaH3wCQv4CFaqpnIpxp06dDMzWtzvblY_w-6V_IEm37GDIampFZVZzXXvYPoHb4XxguUVi5mNkg6KCjkws0hFPel0HjTj2Hk5H0bGCzwyC5xq-kMEocPY_sC31djtKwqf9CgX8fOChtecLUF-1PC1MjHIv_dMZbum2JotUHdIY2-v_DsjKQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=jId5jC_iLyQKO5pvsPgjkIZ29XqxUnCnRcj-8SK_CaMOE9pqO4Cywh3CwKsV-fsfo7JlvLGaVwa3aErhhnIpfsyD_3M3Hzsc8Mxfv4gIjJCkhyRl88Jhq1qJFQJQQ0v_6B4tw3_4t_N4YHkwA924rEAZqgpNkH97ikrzgsuSLYVCZFJ0blfb3qMr7C3TdJS3a6rpl6QGwP3b2L8tz9yjjquxYd3F4VUzKZgiZ_JQAYCaF5FIwYy1XGC3CvW2xvfGv3FGo3rmmOt4ibDFrSLZGvQtQNbbWfUb0TBtjuEcHTEBHS7AiW8h2wjx2QYD5Oa1nB_qnY_1HZnu5TdSVP_6iXbwE-1sqwOv0Sflye2yatBYfZPB89bIATOfTwd6jXnhYIbmdiwXoptHyDD1sCFqKVGXTrskeZ8jqHBHpaspI0Y02f4dwKFLOqS87w5NAv-Dk1QsVKnjM2VjB8KnAEa3WU83DHtdMzD_VdDbMLCwqzsmTmAZo3UwkmsjaH3wCQv4CFaqpnIpxp06dDMzWtzvblY_w-6V_IEm37GDIampFZVZzXXvYPoHb4XxguUVi5mNkg6KCjkws0hFPel0HjTj2Hk5H0bGCzwyC5xq-kMEocPY_sC31djtKwqf9CgX8fOChtecLUF-1PC1MjHIv_dMZbum2JotUHdIY2-v_DsjKQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
چهار عمل کاربردی در نسل‌جدید گوشی‌های سامسونگ که حسابی به‌دردتون میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107148" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107147">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=QvCTyD1ik6VTwIKFMcocmBmVLK48I2QjKUIl2OfgalWf89AN3hob3IugfoeomHtROCV8byqh8ehXotTr1wbstY434nMisYoHBRbdO1Lv_msCGxFFLZDPqUZvuas1jFtMIjPcZM6F9p-J94KtAFQgqMgc_c-5FJjHY7MT5w0zSfpN9CDXFEiAWoA-HIyNGgCUCfcMcCzcKllg2m7Yobo0SNxqzfYUUKMAqzGJhZXBoT7hyi2IVuWQR3g98HUfNSUUyNabG6Sgdugz14tS_aUytxIfMixNR3xz5QCE5sp79YUmpB0nUXls61OLf7gMpxQp-bdDv5O4dXB1XVi5vTYcRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=QvCTyD1ik6VTwIKFMcocmBmVLK48I2QjKUIl2OfgalWf89AN3hob3IugfoeomHtROCV8byqh8ehXotTr1wbstY434nMisYoHBRbdO1Lv_msCGxFFLZDPqUZvuas1jFtMIjPcZM6F9p-J94KtAFQgqMgc_c-5FJjHY7MT5w0zSfpN9CDXFEiAWoA-HIyNGgCUCfcMcCzcKllg2m7Yobo0SNxqzfYUUKMAqzGJhZXBoT7hyi2IVuWQR3g98HUfNSUUyNabG6Sgdugz14tS_aUytxIfMixNR3xz5QCE5sp79YUmpB0nUXls61OLf7gMpxQp-bdDv5O4dXB1XVi5vTYcRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107147" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107144">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=sd6A9F3xkgNXZhQDt_jJbCLYw44vkcGcQY_K3tYgaIC2-RdPUWryqXPxuiCUxpwJCNw22jLqWxa4GYh5wNhDSYfJX8LLvrCm8Pg8EMoGTHIMw_oXws2I9bot1o4L4IYtM5Avy-awsbeZJx_RXSh4QA4tkEsILiHGHCZi3J8aERMdGATgi5FFLd15N1DNZK_L5c4LO2C4qlGLFVkoa1Y8IiXV-v_NHlj_iahz9TcxUVTZFqIzadWoPLFSk7jljbhesa5bPOfMwWccPqMvmJgfzNkdQZA3zQij0UcWnqLOEKwmd8kLclOrKg-jlwJC2Nv3r4EJMtE9waFRyL1baASbGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=sd6A9F3xkgNXZhQDt_jJbCLYw44vkcGcQY_K3tYgaIC2-RdPUWryqXPxuiCUxpwJCNw22jLqWxa4GYh5wNhDSYfJX8LLvrCm8Pg8EMoGTHIMw_oXws2I9bot1o4L4IYtM5Avy-awsbeZJx_RXSh4QA4tkEsILiHGHCZi3J8aERMdGATgi5FFLd15N1DNZK_L5c4LO2C4qlGLFVkoa1Y8IiXV-v_NHlj_iahz9TcxUVTZFqIzadWoPLFSk7jljbhesa5bPOfMwWccPqMvmJgfzNkdQZA3zQij0UcWnqLOEKwmd8kLclOrKg-jlwJC2Nv3r4EJMtE9waFRyL1baASbGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107144" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107143">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
رپ‌خونی سمی ابوطالب برای تیزر برنامه جدیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107143" target="_blank">📅 20:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107142">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=ZjUwSh2sWVU_PjI2IHBu628jt-Lqkq6tx5FdexZPRPkXguyQwXbKl4nndU7gFlzMV-F4280vh_EiovVcdG7q6yCsuSgtcn5_RR6TvLaX0JpDrSJqyyuwYTJMZUijvvK0Jil-summTBEz-uTGAEa86ZsT7mj0-ZsekLs2BhgG3QQgpq7T4OVJGNG5PRMwCEijQCifAJrHRY_e-e1B5agKOqAmZzpSCt3iAY2_gHQB9WBnMUx0B2lCZWRqUvUslx4ymITF7PlHPy4vM6qB_hdiLVQRd1sxmXLBQVeDmdDTg62HaheD4g8V2JFny_8nVJsHfWt-LI2kmScevzDL2GwoJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=ZjUwSh2sWVU_PjI2IHBu628jt-Lqkq6tx5FdexZPRPkXguyQwXbKl4nndU7gFlzMV-F4280vh_EiovVcdG7q6yCsuSgtcn5_RR6TvLaX0JpDrSJqyyuwYTJMZUijvvK0Jil-summTBEz-uTGAEa86ZsT7mj0-ZsekLs2BhgG3QQgpq7T4OVJGNG5PRMwCEijQCifAJrHRY_e-e1B5agKOqAmZzpSCt3iAY2_gHQB9WBnMUx0B2lCZWRqUvUslx4ymITF7PlHPy4vM6qB_hdiLVQRd1sxmXLBQVeDmdDTg62HaheD4g8V2JFny_8nVJsHfWt-LI2kmScevzDL2GwoJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پیمان طالبی مجری شبکه سه به شکست چهار گله تیم فوتبال امید از کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107142" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107141">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsQD8xPhcCRB2HhC90ZZK5IMzYrYZCwkp91OIXsN2AOGzvTzjh60-uGmicORER5RvPsCP0DrCv1YIJZgD04sJV25iaQQQBK7B5LuyQHf_PpMETHd1bpYMytzdpcSxwG92FpD_cOsOPR-zBSV_UjARfwxJ0AKUMLn15hjDwPxPhOLwLsQZzu-GWf8Zr50M8D3_16LqbdOoxnPpxt7u-L7lQ7mhy6h4omnICpN87EQLDGN4Th5xtCLBRQov3uPnJmUMBmOrz20MgweQYWj00R98Q6DQABFUM-KDz1kZ2SuXkfBp3CUKl_ytIyLc-QhbUrEQ6R27-IRcO2asqBzCsqOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
استوری‌جالب زبیر‌نیک‌نفس بازیکن سابق استقلال به شکست ایران مقابل کره‌شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107141" target="_blank">📅 19:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107140">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFwLzW6yG_hZelJCW7bXJGUnMh-TuIA0olt-4JOgfRPEys6uqpg4tQ7JNBjM45ReZOIkbYa6u4NtpnLoeshA_ArMLJDEt-2h5bLNt5jPsKmW_cce32cX_9SdCCXCz4PjGSAbDd8h1J1qn0osMx21YYxXVW5jUyVv4evwVLkI-xR4LkODAhZ719Kg77HYXx2tz0TBC8D_NMMF4LpSujCe_Yu1bzWkKcD5NtxwtTiyQzQbOsdGNIIyNj6kvqQ0AW5IeqVzwkuFJgICBRUvBFazsvymJ6m6VUWVf6mXoY86JP0jGexfFlfwNJMpg-EtZdu8SNzNv1iYOUvi8taYTVSi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
بهترین استارت یک‌فصل بازیکنان بارسلونا در تاریخ این تیم با صدرنشینی اسطوره ابدی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107140" target="_blank">📅 19:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107139">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
آنالیز جذاب از بازی‌هفته‌قبل برایتون و آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107139" target="_blank">📅 18:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107138">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=LvcSM30F27dgjnZteDEQk1kK4Z55PxSbSlC0DLbox2KgznEUpJQWB7CEPg-Kq-IyOaVuE_NxyLMfeHbAyVZlkXUetKYnxt3d5Q0qHA7rARw-z8STtQzAmV2VxaD4YrrH35KkjXiH08mxOHP3nJqrwO_rE7CW28KJ2-atKF6UXIZ9Gf3YlYiGbsgtX7LodmO912t65OV6-O2AC3JQ-fE8VM8lPdttgtHicjqpU9OI6IpRNNaGlnUUOFKAhTyhaGVIFrGUL6M4StyGwqnxGJqprWDcEeBBMsQHhTRDa18Mb-7CCXW2zxca5bMd86V63d4O1Hhht8Sjxkf9ekuYCM_ZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=LvcSM30F27dgjnZteDEQk1kK4Z55PxSbSlC0DLbox2KgznEUpJQWB7CEPg-Kq-IyOaVuE_NxyLMfeHbAyVZlkXUetKYnxt3d5Q0qHA7rARw-z8STtQzAmV2VxaD4YrrH35KkjXiH08mxOHP3nJqrwO_rE7CW28KJ2-atKF6UXIZ9Gf3YlYiGbsgtX7LodmO912t65OV6-O2AC3JQ-fE8VM8lPdttgtHicjqpU9OI6IpRNNaGlnUUOFKAhTyhaGVIFrGUL6M4StyGwqnxGJqprWDcEeBBMsQHhTRDa18Mb-7CCXW2zxca5bMd86V63d4O1Hhht8Sjxkf9ekuYCM_ZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
تشویق مسعود پزشکیان توسط عباس عراقچی و... پس از پایان سخنرانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107138" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107137">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
⭕️
🇮🇷
پزشکیان: انرژی هسته‌ای حق مسلم ماست و برای درمان و کشاورزی نیاز داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107137" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107136">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=WPPDHleKnbBr_6XQ6YsidajIsiNfgsCRLOIuNfKPaSpvnhjwBtSs3znCJ80fFsK9zCLowu9lEyUSkKaZ61cfMDoaS9fvbgxdXUlcJT5V3KvLYSBVeZ7YTZRgGSXwruTjOQlxdrkFXWZ3HzHz8USzTBDu6evQXOWjlu3ynlqBHMo1kvFkzp3pxoEZ3XLbG8t2VrWjXbzlOtvzvjj2JP0wDLD5WftpQ5DliLQYJ-6dI-tuwdjkpSfpMB2l-KLcvgZ_rxZwh339Av5SH5LCSugCn1LPJfh4kvkeKecxqOx-kTRnhKT1UvT635pigZ9CCbtNHHnN0xRb8YXVP-Zbb4CXOoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=WPPDHleKnbBr_6XQ6YsidajIsiNfgsCRLOIuNfKPaSpvnhjwBtSs3znCJ80fFsK9zCLowu9lEyUSkKaZ61cfMDoaS9fvbgxdXUlcJT5V3KvLYSBVeZ7YTZRgGSXwruTjOQlxdrkFXWZ3HzHz8USzTBDu6evQXOWjlu3ynlqBHMo1kvFkzp3pxoEZ3XLbG8t2VrWjXbzlOtvzvjj2JP0wDLD5WftpQ5DliLQYJ-6dI-tuwdjkpSfpMB2l-KLcvgZ_rxZwh339Av5SH5LCSugCn1LPJfh4kvkeKecxqOx-kTRnhKT1UvT635pigZ9CCbtNHHnN0xRb8YXVP-Zbb4CXOoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
‼️
پزشکیان: اسرائیل هر محله‌ای را در هر شهری و در هر استانی هدف قرار می‌دهد و عملیات ترور انجام می‌دهد، درست مانند گروه‌های تروریستی واقعی. در غزه، بیش از 80 هزار غیرنظامی بی‌گناه به طرز وحشیانه‌ای کشته شده‌اند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107136" target="_blank">📅 17:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107135">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=YtNMcQpDo8eq_J3KbqshxyAS9BRiFEWlxqt7Y6tRTAwRWKEXevEcFaLXijXmrv5TXrEdCWAllbAn03Z-o-N59E2m2lHwJKqVnvX9oV-m0TK4iBU8-vyhEHscfvQX1dQ75bY6gU4aljAS1Sphd8j4t7sMusyRST7kUg8B50I6dMWnbbXbzZA_PUUSBJFL2tnx2bMknJcn2Vkjy6LbA2Sm01a4C_HKHuuVMX4HITq6UZ2yeYMV67cv2WPUcvksH1HBWjcVBsQWN2NOOqvXaJUMHEbNR_IQQqrvTgyk6VfkWKzIVv7tY1heCSF4mM8NDO-nWPaPi4Ws5fGn-N9gbc0lyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=YtNMcQpDo8eq_J3KbqshxyAS9BRiFEWlxqt7Y6tRTAwRWKEXevEcFaLXijXmrv5TXrEdCWAllbAn03Z-o-N59E2m2lHwJKqVnvX9oV-m0TK4iBU8-vyhEHscfvQX1dQ75bY6gU4aljAS1Sphd8j4t7sMusyRST7kUg8B50I6dMWnbbXbzZA_PUUSBJFL2tnx2bMknJcn2Vkjy6LbA2Sm01a4C_HKHuuVMX4HITq6UZ2yeYMV67cv2WPUcvksH1HBWjcVBsQWN2NOOqvXaJUMHEbNR_IQQqrvTgyk6VfkWKzIVv7tY1heCSF4mM8NDO-nWPaPi4Ws5fGn-N9gbc0lyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
خروج هیئت کشور آمریکا حین سخنرانی پزشکیان در سازمان‌ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107135" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107134">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=N3tYl_QvvkmhHCImInxQDFAFBJl--oyMrJz3GV5dYXjU_N91oTjNzmnLJKpgDSVr3_DPuHpAGN8V0m8Wgr5L_rh6MRgH_LNPkutROSA4VO0_iOqkYVENBS8MQn9KBHH1vPbuHX1Zvll-RyGqN_u3Rd_e4qi4bDQiiuwVoSRDXbJE1PPAoBaDgwVXs_MM82nQJ5hWUyz4mcJXoU4qpIVTjTC1MaOI-GMpuIlovT0sbKjHqSYfiCkUx4SBT-cmHBY_x-3-AUqzco0tqr7ytz_eowVwTqvA9VAR4KKuaef6AsV6lDvibetxGDBtcEfPE38K3a877aNFnRjHuGb13VOqnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=N3tYl_QvvkmhHCImInxQDFAFBJl--oyMrJz3GV5dYXjU_N91oTjNzmnLJKpgDSVr3_DPuHpAGN8V0m8Wgr5L_rh6MRgH_LNPkutROSA4VO0_iOqkYVENBS8MQn9KBHH1vPbuHX1Zvll-RyGqN_u3Rd_e4qi4bDQiiuwVoSRDXbJE1PPAoBaDgwVXs_MM82nQJ5hWUyz4mcJXoU4qpIVTjTC1MaOI-GMpuIlovT0sbKjHqSYfiCkUx4SBT-cmHBY_x-3-AUqzco0tqr7ytz_eowVwTqvA9VAR4KKuaef6AsV6lDvibetxGDBtcEfPE38K3a877aNFnRjHuGb13VOqnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پزشکیان: این بچه‌هارو می‌بینید؟ اینارو بمباران کردند و کشتند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107134" target="_blank">📅 17:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107133">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=COBy25R21fzD_-Kplwu3TuNl1prrEoa-jpvoWkIHa2kGIDMmBzEmGrjh-HdUc4t0l17cA1sGBZnptcCLbhzizsP03lE6rutcEQ7bkcWJFAGU9trUzRZX4KzO5t3uzlXFqe8DicHNEgSqEX2wbhpcfcEauCA2Xr8aKD79gg5mlib9A0Gqgyz8cayEVgyIirg9HFreAnbP7yPD9yMXP-2IaDSeEDyqhnuzxAYkY2gc0Vgqe2HwPoF0TqkBrZySuwdMSib2yuofnTOr6XiaPCzIdUrL1sQD5BZ1Az5VlkyqIT1QT1JC4_xLWNyVdXUhhbwRxksaTa8HToRxnXfrPe2eoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=COBy25R21fzD_-Kplwu3TuNl1prrEoa-jpvoWkIHa2kGIDMmBzEmGrjh-HdUc4t0l17cA1sGBZnptcCLbhzizsP03lE6rutcEQ7bkcWJFAGU9trUzRZX4KzO5t3uzlXFqe8DicHNEgSqEX2wbhpcfcEauCA2Xr8aKD79gg5mlib9A0Gqgyz8cayEVgyIirg9HFreAnbP7yPD9yMXP-2IaDSeEDyqhnuzxAYkY2gc0Vgqe2HwPoF0TqkBrZySuwdMSib2yuofnTOr6XiaPCzIdUrL1sQD5BZ1Az5VlkyqIT1QT1JC4_xLWNyVdXUhhbwRxksaTa8HToRxnXfrPe2eoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نشان دادن تصویر خامنه‌ای توسط پزشکیان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107133" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107132">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxoS7cWNNvLhVVkWKia1Xn0c56D-aSIGkfhleX2Oey-F1pe08i-TQ0V8DnXAbilVxVA6Mqs6GToDBWLtaYwPhdjw0wXTe1-aAZXFpgD96iw-G9mu0S_WydEiUOoJYIGO3OgFLGFXbe26_9LlPVBSWy3z8DO3e2DdeHliX4Z4RASLuuqEZoYfA5cDuTiwRUiHertgmbqOr8FZeLgwbzI_b7GB-NkzzVdy0nEUMlXecfAr3nos5tGd6SDe7HVcV8s_IQBWxBd4MKLaeJpNo44FjNweZJ7Xhn26lBzl_uNP7ZJY6ewMK7eWP0QaS6nwiVdG9KCrox3q3H_X-Z76DjnuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مسعود پزشکیان در مقر سازمان ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107132" target="_blank">📅 17:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107131">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=UnmCTEpjvfZtjjH5qsUzpzQIw5YN0aEDWVCFnvyshJxkkF7UIdLA63gjztIN-f9__VfBzWYdqtg8kqLzWimPiSnyGadXOD_53_4xtOJ_Rv0N1n4NlKLfGAvVtu1G_D4gP9W_c_uJ_Dpd9hRc5hCM7q4D48EY8t2aecJLAqkle83-JJX89FIWegw_wlFFAPnjjG1p8PQmmM8dthXaJrlW3e0-tLoauzqgSPR1hhCj2F6APkVs5Z1Z8ibPbmySH12Imoy7j35D6oZEQoW3eQJOi_pnKrSAtPbGCw30s6oSshmL-w-g96I-XaC1LNVzKmY16H_SKMpYIaMU9nWckMLisA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=UnmCTEpjvfZtjjH5qsUzpzQIw5YN0aEDWVCFnvyshJxkkF7UIdLA63gjztIN-f9__VfBzWYdqtg8kqLzWimPiSnyGadXOD_53_4xtOJ_Rv0N1n4NlKLfGAvVtu1G_D4gP9W_c_uJ_Dpd9hRc5hCM7q4D48EY8t2aecJLAqkle83-JJX89FIWegw_wlFFAPnjjG1p8PQmmM8dthXaJrlW3e0-tLoauzqgSPR1hhCj2F6APkVs5Z1Z8ibPbmySH12Imoy7j35D6oZEQoW3eQJOi_pnKrSAtPbGCw30s6oSshmL-w-g96I-XaC1LNVzKmY16H_SKMpYIaMU9nWckMLisA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید عارف‌غلامی مدافع سابق استقلال:
شجاع تر از آنچه ميپنداريم، كمي دورتر برانيد ، زني درحال فتح ترس هايش است ، ١ مهر به ياد تمام دانش آموزان و دانشجوياني كه ميتوانستند در بين ما باشند اما نيستند ، روحشان شاد يادشان گرامي
🖤
🥀
💔
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107131" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107128">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPLhl_O1wUq7rE6uoZud0Y-qVN6LZlsBHNR74TNb9SzHUJNtnfykcNMp9jOl1MhQPMOtrq53_3gDTdwC4Q-3fDDB6QSFGpErhwA-uNhiUS2zXoGAXsKBM0B0Pk3MBuCTlc3A_LVGDeZcqK4N3nc9Xy_MYwv1yoqqSbLROruelEg-ub9_2OMyR6zEhbDSHdLVg0OnPVverSjWIqe-1PcEfWb1P_g3bVRWB6N08PNNHbHBIO7jPS1RWo86IkSGfYDcZ1qDso4Go0xk9E64CQg9_hlAh-yNsGBNLXibO9jizwHRYkJUVmAVvEPgjExFMSRCdqYFfV_8LkYmrivqwv3jJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اسطوره محسن‌رضایی: به لطف تلاش‌های ترامپ، ایران اکنون قدرت چهارم جهان است و بزودی با تلاش‌های خود به قدرت اول تبدیل می‌شویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107128" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107127">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDD5kfF6fJjQDZuEQruccLPLP6cb73Ir5FVvit-o-xngzIZC_oDKPikK4nEdKCBSpW0gJEbBPbFbarqywkhfjXWL9ku_rZGbGk5G3uLFYgncCPoF_1uxf8vFCcCFTqofUxnTz3MyZpdyEJ0iEZAVdV54e03tjigBSezx-B-hOGv12y7ZJb7GsUpPWDPcR09Jn2EVTzzV-OsFDe_uP53elICRZ1fzJXCffl-pLWessW76cGUeW226Amg0U8e8ixqaDnPn33_-VmWXfzc8QhYsTil5trywOFAE7EviqZT9BB_CmoCfvCdXMC1Y23rApBxQEQ3JWWO-9asYOJMFKVGNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
کنایه‌های خداداد عزیزی به فدراسیون فوتبال پس از حذف تیم‌ملی امید از مسابقات ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107127" target="_blank">📅 16:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107126">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh6JOW3-YWvSCGRb0dOhb-qQgdNnEeFmDhdUDsjt9It4ZKk8Kiq8hBhkf15CuLuUxntCP25nsVVvIT0YpLHcTwPSeq-QH9-n0dgFG9qd_FeCt53f02dP8F_A6kzvxcMNIrSA4gRIup2YzPWyzDWk_kr5OMrSlhkOfWsQvY7HwjEtyUIgDzLjyPhljaiLbdZ62Hs71eNQlJjbPoBsMmZrb2pClmj_0qruyrkrnPuwtnw9nwo6rbwCyCyj-7AUFOVWEWB9NlFCD5_TAdq0EvmM4Y5oKS49QL1E5TbQz3v5R85R5t-aJKbesSmQEETm1WHe-K0Zjj2WOJknCCdRys3lRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🙂
در فیفادی فعلی و از اسکواد بارسلونا، فقط ۵ بازیکن برای تمرینات در دسترس فلیک هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107126" target="_blank">📅 16:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107125">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=KbaEH1FIUfi5AmqlLIBtLEbO5IAmZWE2fcStMLoVuIMfbwDKvRbKgAAng8bQzUpg_mTm5gqXXJY3WMCLW1q3UYJr0WrPsORwv0dylKYNEwNZjwFyyLvlZhDZ3aDKXifltTCb1h-TUQ6soLm2EOIRUF6-Iku-29LuIfuSxF-3e6rXTGeDV3YlyrfDsCLi2TwIM0BV4nvybMTJuCnBrBb4YLb9RlHjh7RFYEPe9OQgSYRixrnQA7gi1x2D7RHMy9JN5ZMKhsMFFztehYHpRJmXnBgJlL3AW6SV4V6IeN0x1nZ--c6aL7q5gbYmJ_1AKEQR_OWUUcZc77QLD6dG9yFMESrRfu-tiH5aPf97l1anarxkxVtgY5anMu1h6hBNfAhDaE6ROxSwgZhOGskoPbgQAIfp0WrL3R1uwFMRCJgM08_7SPUp5J4FMyETWX_jE0MiRgLodQCVTOz79URSJOI7G6VHjG7pS7Ds8bnSWOS8hsxnhaNNrbmjtwVPnDxWBemceKnAWdA-Ranh7z6UvYVyidPK9YZDjS39OB5kYePZCId909P8q6FJj0F3K5RnlpvIZSB_q4CewFWtQPJpXAIfgubqUxAQQFtZuvlephrEMAxtWRrZdO4IPRsatFeo0ZDoLWRQx4wxSDOnfNhy2pOW4TxSgT15ZzNh6Ds0r1rkG40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=KbaEH1FIUfi5AmqlLIBtLEbO5IAmZWE2fcStMLoVuIMfbwDKvRbKgAAng8bQzUpg_mTm5gqXXJY3WMCLW1q3UYJr0WrPsORwv0dylKYNEwNZjwFyyLvlZhDZ3aDKXifltTCb1h-TUQ6soLm2EOIRUF6-Iku-29LuIfuSxF-3e6rXTGeDV3YlyrfDsCLi2TwIM0BV4nvybMTJuCnBrBb4YLb9RlHjh7RFYEPe9OQgSYRixrnQA7gi1x2D7RHMy9JN5ZMKhsMFFztehYHpRJmXnBgJlL3AW6SV4V6IeN0x1nZ--c6aL7q5gbYmJ_1AKEQR_OWUUcZc77QLD6dG9yFMESrRfu-tiH5aPf97l1anarxkxVtgY5anMu1h6hBNfAhDaE6ROxSwgZhOGskoPbgQAIfp0WrL3R1uwFMRCJgM08_7SPUp5J4FMyETWX_jE0MiRgLodQCVTOz79URSJOI7G6VHjG7pS7Ds8bnSWOS8hsxnhaNNrbmjtwVPnDxWBemceKnAWdA-Ranh7z6UvYVyidPK9YZDjS39OB5kYePZCId909P8q6FJj0F3K5RnlpvIZSB_q4CewFWtQPJpXAIfgubqUxAQQFtZuvlephrEMAxtWRrZdO4IPRsatFeo0ZDoLWRQx4wxSDOnfNhy2pOW4TxSgT15ZzNh6Ds0r1rkG40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امان از دست رامین رضاییان و اداهاش
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107125" target="_blank">📅 16:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107124">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9325345835.mp4?token=GDmFNpgYfzgk0eQy8NQuKQBb3gsg0yCH0a7aAUWkShN4W42IssL1zWZBED4Vhu53KHXXxRV_IAfIsvZRZfVyeywMprlvk5ewynpfXL-2FhCNNpHNVF4xxOaIb6gjd1FJNg5EF8faufWvMq1HEAjXbDeV-DGPfUfGRFLA3yC3wijWVdKNXnFRVWs28apcYVdAUFEFXk3KIlzpOesb4LHitrptDqRSDjOArpMK8VTwEO0Sk5XYxKYJqoRrn3a7D-hQN-Xa4U4-ACUAncGMuQWw2dgU7Op2F9Ab61nwDc06nN-gpZQiFTg-vNDR-MSDWZKkLlXbsTyf3RUczVLrROpiSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9325345835.mp4?token=GDmFNpgYfzgk0eQy8NQuKQBb3gsg0yCH0a7aAUWkShN4W42IssL1zWZBED4Vhu53KHXXxRV_IAfIsvZRZfVyeywMprlvk5ewynpfXL-2FhCNNpHNVF4xxOaIb6gjd1FJNg5EF8faufWvMq1HEAjXbDeV-DGPfUfGRFLA3yC3wijWVdKNXnFRVWs28apcYVdAUFEFXk3KIlzpOesb4LHitrptDqRSDjOArpMK8VTwEO0Sk5XYxKYJqoRrn3a7D-hQN-Xa4U4-ACUAncGMuQWw2dgU7Op2F9Ab61nwDc06nN-gpZQiFTg-vNDR-MSDWZKkLlXbsTyf3RUczVLrROpiSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شوخی‌های بامزه ابوطالب با پرسپولیسی‌ها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107124" target="_blank">📅 15:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107123">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=lWshkVHHgwDBkyLkrtg0pf1daxylbzWZ_LUxowoJgy-1Qh4QRvBq-2gC9aBv4_xzXawGvq2lbQPsnpA3LFaFVjWmusJbKkYD6nUuZaBu2Cz3gnlw3icTVgmTlutkS-gn7YfZrbiY3GRqcB5OkFEuumCTR3jfoR5YJ5xq3Z4KFI7DuOpZ21V2GTr-bWy66LEU0t8aXbQniMbA5OgIodNBAg3w0JgN48BEsDVEZd-aAjkPuBeam-KC80WqKexDiQKH9RN9VIKWzI9Gbx4sVR70dlBi7HD-oolkWHoEnOUo7PS82T-tfdkS6cgZsCu5dgEezE4Cbj3JhZhBFxN4RDx_pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=lWshkVHHgwDBkyLkrtg0pf1daxylbzWZ_LUxowoJgy-1Qh4QRvBq-2gC9aBv4_xzXawGvq2lbQPsnpA3LFaFVjWmusJbKkYD6nUuZaBu2Cz3gnlw3icTVgmTlutkS-gn7YfZrbiY3GRqcB5OkFEuumCTR3jfoR5YJ5xq3Z4KFI7DuOpZ21V2GTr-bWy66LEU0t8aXbQniMbA5OgIodNBAg3w0JgN48BEsDVEZd-aAjkPuBeam-KC80WqKexDiQKH9RN9VIKWzI9Gbx4sVR70dlBi7HD-oolkWHoEnOUo7PS82T-tfdkS6cgZsCu5dgEezE4Cbj3JhZhBFxN4RDx_pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
جدیدترین صحبت‌های رامین‌رضاییان درباره عشق‌وحال با توصیه به بازیکنان رده‌های پایه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107123" target="_blank">📅 15:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107122">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=S0ilv8mzLE9QVvrpeC0doK_8flbcccnqIItacO3meBCAkQ0nnDSRlTqusDd6pCPiP_r2A3bmu73Mr1800eC1WXyWfajtUrhj1vLBaZgvfinblBFU4DVxc9OhT11oN_wjpxWrmrkixTLhMF83FToIXRW7_eDzR79HqBJji8gabVJemDE2T8hI1EpuZ1sGTiEjF57KBQ0aP6dYCoAUB9SLaSPyZSgl5rhksr-PGwlYsP6LCiEEDkTKhtumCtKiuhvyK6XSLikZ_EPdGq-t2nqJYbLtYytFKQrU-6g_fPYlHhNKyeU_zu3XdCaUCuzRfv5N8k3gFEjUpqgpTerlzdKEYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=S0ilv8mzLE9QVvrpeC0doK_8flbcccnqIItacO3meBCAkQ0nnDSRlTqusDd6pCPiP_r2A3bmu73Mr1800eC1WXyWfajtUrhj1vLBaZgvfinblBFU4DVxc9OhT11oN_wjpxWrmrkixTLhMF83FToIXRW7_eDzR79HqBJji8gabVJemDE2T8hI1EpuZ1sGTiEjF57KBQ0aP6dYCoAUB9SLaSPyZSgl5rhksr-PGwlYsP6LCiEEDkTKhtumCtKiuhvyK6XSLikZ_EPdGq-t2nqJYbLtYytFKQrU-6g_fPYlHhNKyeU_zu3XdCaUCuzRfv5N8k3gFEjUpqgpTerlzdKEYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
مقایسه فوق‌العاده سمی ابوطالب حسینی از فحاشی تاریخی مرتضی فنونی‌زاده و خداداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107122" target="_blank">📅 14:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107121">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=a2HY6bnBnHjbzqRi9BqB3V33b7ljX6zTyfBHJZ27NELrfMJZ0tzT7l8noIObvjij6aSF_8YY-lfqqK8asanWXJSgmFUDYAHmDqG6MdLazJ946WNMi9qHjHIvY7e87GoiyqC8fHvFvbm1pDP7VfSSxEgP6Rz3yatNfvpKmx96d4NBQLOMxvOXx8k4mCrJtCqQJyakj32z1tO0yrZPaMgkzirMAihqO23hLDZr87hp5QrHxnVJbUgJltCpgO8cmyX5lBIJwZVp2PSFf08oO83i6Y-hrrjQ_dZYiv5SMvL8vvGgQioxLv0SptU40rsXYlZ9uuSjG4ybhck8tDXa4nlapQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=a2HY6bnBnHjbzqRi9BqB3V33b7ljX6zTyfBHJZ27NELrfMJZ0tzT7l8noIObvjij6aSF_8YY-lfqqK8asanWXJSgmFUDYAHmDqG6MdLazJ946WNMi9qHjHIvY7e87GoiyqC8fHvFvbm1pDP7VfSSxEgP6Rz3yatNfvpKmx96d4NBQLOMxvOXx8k4mCrJtCqQJyakj32z1tO0yrZPaMgkzirMAihqO23hLDZr87hp5QrHxnVJbUgJltCpgO8cmyX5lBIJwZVp2PSFf08oO83i6Y-hrrjQ_dZYiv5SMvL8vvGgQioxLv0SptU40rsXYlZ9uuSjG4ybhck8tDXa4nlapQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
خداداد عزیزی مدعی شده که یک‌سری افراد میخوان این یابو‌ رو حذف کنن ولی حذف شدنی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107121" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107120">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=l8w7jPee7yeDwzpca3MkAIfrLTijWFX8U6VTbo8MOtBqvNa_MAF1VZLbJ0y7YsfTjod0aaQyzbFtGZCx27bESUTbX-TwUeesoana7J8LCFvHFyssDwdUj26CoSNDbK9853BLluLKZe2sG_FSnXb94SD0URFaDa96STfN_yIldMjG3__zQQ_Fi3gFKEOnlcGHRHp793zXOesS0V_Kp2RX4l75HU14JfXfJt761MsUNDn0mpbVbwloZHxK-QggeA2yKs47UfbemiHhq9bZpAndXkRz5F32fgl7KoodbD4MEjf0Ep45-tgP4V1-gLKxFm4exCQcA8TORBdykhPUyiY6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=l8w7jPee7yeDwzpca3MkAIfrLTijWFX8U6VTbo8MOtBqvNa_MAF1VZLbJ0y7YsfTjod0aaQyzbFtGZCx27bESUTbX-TwUeesoana7J8LCFvHFyssDwdUj26CoSNDbK9853BLluLKZe2sG_FSnXb94SD0URFaDa96STfN_yIldMjG3__zQQ_Fi3gFKEOnlcGHRHp793zXOesS0V_Kp2RX4l75HU14JfXfJt761MsUNDn0mpbVbwloZHxK-QggeA2yKs47UfbemiHhq9bZpAndXkRz5F32fgl7KoodbD4MEjf0Ep45-tgP4V1-gLKxFm4exCQcA8TORBdykhPUyiY6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لحظه‌ای که سیمئونه شورت امباپه رو کشید پایین؛ سیمئونه گفته اگه قوانین اجازه می‌داد حتی اون‌شورت دومیش هم پایین میکشیدم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107120" target="_blank">📅 14:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107119">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=gEync7An24dbzJLQ8VUGomTLWmHhgMMEhSoHthffNP1flMdWhctbCdu6EGgAZe6kZ2ZQ4jgNE0cSgqT8n_ZgN1ITPsG_59zxhqCQSUo6BWKxraPXpu6r9alx_lKKBMw3Y1rdgCDA-_H4692OPqjp2X8hSnfO_fkZnN3oe-foYtoMeQVjpFFJ3skCMrlOl56IkmgTeUoIubDq5CV5cSH8_YdHhX5JtBzlV5h9qKTcQdFOXN368FdDKXbILFeBCuRgzADsf4Z9W8ajKtUNrQo7y9dcSc7l1CY745VMklwfSmGm__AXypN0yjoCMdYPMmuym0CGcpMmYHKMpezwdSvLnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=gEync7An24dbzJLQ8VUGomTLWmHhgMMEhSoHthffNP1flMdWhctbCdu6EGgAZe6kZ2ZQ4jgNE0cSgqT8n_ZgN1ITPsG_59zxhqCQSUo6BWKxraPXpu6r9alx_lKKBMw3Y1rdgCDA-_H4692OPqjp2X8hSnfO_fkZnN3oe-foYtoMeQVjpFFJ3skCMrlOl56IkmgTeUoIubDq5CV5cSH8_YdHhX5JtBzlV5h9qKTcQdFOXN368FdDKXbILFeBCuRgzADsf4Z9W8ajKtUNrQo7y9dcSc7l1CY745VMklwfSmGm__AXypN0yjoCMdYPMmuym0CGcpMmYHKMpezwdSvLnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه دردناک سرقت تلفن‌همراه پاکبان در مشهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107119" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107118">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyfZvawIeG_xJoEs3M-A7dfkDTrX-qe4C_RY-p7oKE96xVKgSV2hs4_nf2pcjMDajzai1wGQYMpH2r1VhVlnJwOoYEjGOEixPavFYi4Ai2IVQSPvYVXlqCCWUrM7RSf_HtxDJS9C-Z3Img379BPAFVFzehvQBPS8AmLpRhYdDMWbdf1agZFxKL7OAbBV7_Ao2Hb7pEQaEVh6BIuC0qGLYVUAaOi1Oh-ISCno33rRpCp4Wf648UE_3z856KZ-IYAAvEgqvNekXXlpUpJ5l2NBZQVV-75n0qAXS_gZuEv4U2u2juwiIBjjvd_UoewELrjpaY4cdLnPp3ps9GgPY2lwZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
📊
5 بازیکن برتر در زمینه خلق موقعیت گلزنی در لیگ‌های معتبر اروپایی تا به امروز:
🇪🇸
لامین یامال – 6 پاس گل.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز – 5 پاس گل.
🇫🇷
خاویر هرناندز – 4 پاس گل.
🇮🇹
پائولو دیبالا – 4 پاس گل.
🇪🇸
آنتونی گوردون – 4 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107118" target="_blank">📅 13:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107117">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZdHXqS5sgIQsK3d3WRt9S8iZCjsCb3-ttVpdk3dg9ET6gpXUWi6zpAId98-XNNftvfxCucAvNxdx8HO-S8bDI-3VMKztOJ5C_APswV0siQY3aFQkg0ZWJjjYha_GVq4v2x0qX-Vcf8nf4Iu2AZvbEUM9ep5IU3fAmrIux8nghuWpTKHEjvAfUpSpJN1ZAwV0pxKyBz9a3q7syUPelWH_UWFZsv9BnKct9T8Pi936lhp3EK-PM7W5LmQothb1k4Q9uD3fbUk1JnO87JngVARwyITX8NQ9teAzTW-1VUJaaPrFyfSspNgYvfOEBV0jHoOaHZZfA3arPs5V5042BwGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خاویر آگیره سرمربی تیم والنسیا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107117" target="_blank">📅 12:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107116">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxTeW2w4Gv5aJaToL9CoKyOFq0q6v22Cw6IeR0f-8b4pt0fXD2h6cVQWZwz0ZyakmkUM9KFS2DfHQoBlusnsD3lKSsoQG2jdZpCSnc8z_uL0GOzfefsCaLROxpquURtOvW0a1QB0hv4MwDGEEZRPtQTo8oaQrzDpTeShtT7N5d-X_07RFCbXsVje7u_Ey2otGNTAFzQ-8jxL3SoAFhFFe8PFG77vz29qD417tsrJ9tfIXyD7l1H1XXlBNuzOevhps_kvHku1uLLnLDqbQ26t4VITMbAe9pwda7T2Bx2_2HZwKc0S7_aLExGyZ-hrvIUneJ71KFO_z-BhEnm--Kp_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107116" target="_blank">📅 12:39 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
