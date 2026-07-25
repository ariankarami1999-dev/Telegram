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
<img src="https://cdn4.telesco.pe/file/iFySZc54mpNiRi6w9AM91ZX_zH9AqvZAobhQi9pe9pANt9CYhF4uG2QbAuKvvs_8w839wjMkyU68lzDEaXHoQOiOBJy9Gjh--9S11PHqOjMV3Md8oJCAmK6nKdPfNOsuspC0E_VOA6uElpMOC_FfpnXQauNBMaQLrYK2GJ59n7_Xe6zLqHUlA2bFGpU2uMrWxF7uRTuX69fawxjoSFzKCzCEzIBxe_N1ob1RITj_gqXHfG4ofR2Jw4LIHbEBJ-dxK4QP5TLTQ2IOolXLUlElo0qeirn7fuVntElIkKwp8Mql6AsqoSanZ2a1AY61XLpPDUWG9lDKioCLGW_Sx3InrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 08:56:46</div>
<hr>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=Q6CXGZnjn2KI5q9SEU-v89Ae7-dXLHQCiXQLDMaJwdGKmsKUMT7mwmuYMNvapNrEJEI87CM1pEjQJaxhHaBGiOfJi9GeuqXDjQxEIZ_bcUlUZGfhi_ynxQiJi3LKR2Htom5x2TLa6Z56PX5nSsEGja37pGCrxYsMihCaATM22JT_JyCxNiqmzqBMXzEe2SgCVMS6ktxD_56qI6IJFZmF9DoH6gu6_IdqNV6DDSXYVQyJv2uq_OIhig_YalVRtApTlg2C5Yt9p4RHLw4zbn3lSccLliWf4vuAlIUSQ3rbdhHFgiP5SAhXdru178-TBXLoQHMfsd53D4D4ory_yJt7rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=Q6CXGZnjn2KI5q9SEU-v89Ae7-dXLHQCiXQLDMaJwdGKmsKUMT7mwmuYMNvapNrEJEI87CM1pEjQJaxhHaBGiOfJi9GeuqXDjQxEIZ_bcUlUZGfhi_ynxQiJi3LKR2Htom5x2TLa6Z56PX5nSsEGja37pGCrxYsMihCaATM22JT_JyCxNiqmzqBMXzEe2SgCVMS6ktxD_56qI6IJFZmF9DoH6gu6_IdqNV6DDSXYVQyJv2uq_OIhig_YalVRtApTlg2C5Yt9p4RHLw4zbn3lSccLliWf4vuAlIUSQ3rbdhHFgiP5SAhXdru178-TBXLoQHMfsd53D4D4ory_yJt7rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFX74a6nsStoFi_KitK4iAhz0dtkBtd2r4JhvNDxvW7yt81r7YPOTVMT2ABqCiTIxEWUhDdt2V1sbTtTx4ibwP7jl29ujqeo3JUozzbXM27h3S6lSW8NB9alT8KY9f1K6V25OIkitHbYn58j07rQqfcIHWFmeFF2kkz3eC_mUnIEYhMa587qV6dOEGmhavkVUuvzEOO4n9s1IisZZWccxBhs7hu2PCxQtTSv6coBbLX0JsMXJ4Vrxa-KB-AqpWc71x5k_X--BSVRNQvq3H3-gfFBNZBGBVVssPEdelyVxJki9RRXJbddR6Qz1KVEXTYXiRcFdRKKj5TcDO3BNhqCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqWa70UuXvYgm82q4WeB5gldwDWB5ClQHPmwXBrE9yLirAFDO8IRtphWIuQnI-DJlGJgio9FCHztlSkzIGlwzwDFYTgCTOZktFtBnPJhUSyN0bQXatKmqFJIZ7cHOhW7MJAQBkR86PBrhtq2H2d0HtfqehXRFmrudeDVfLoX0x0Lh_C5m5ACEMTa4Pligf8NTyC6iwKGWkRiBCOMNI1J6wDvvZ7EedzqBR4dpQpZr5ks6Gja87kAQYgyroQJ2NWD2HEcsehKynWin5It9wU7gW9jJRipjlAhzPR1nx7H0gSFvbXFB-FkxpIFXStH49YPNAKP-AbUWCovJ1ScAqaseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=bwKIFT6rHv7h7wMZ0HcyUVJwO30hmfuqheis4NOTjIyGH8SlqenOQS2Z-YVkcB2vaQ6tQ_xK_OGfbM8icGcoAfHBcKXgIE_1BfJv8dIuQHi62J9OgWbTJ8Fi3cZebngmj7xyAVCgb6NBsAzRFoLpCy65DmnpZmHSOOsfKPTfoNAAQuD2nR19bIYLCumA_DO4eC1vkCO3M_lJe-yIBsirCT_VjGPBMs3_kNtsSZq_jb0YHFGxZeLBiKA_OFvqgBKnNA3Lx2nZrv2mcEK7Fv4JtwIDWCnuX0uU4vBM6vAakQrwZ65WGeVtM6b38tPyKas3-ABLB3BrO_P8Im3Ceye3FESsxUv5ZAvSxh-nJRlNmrrU-o81T7wb5945ep-B0uIC8UWoqAjQCHdX4sUwdGysSk50kJJ4OOOETCdiHeIV5D2b1ZoKFGJw-BEsoku3X8_U82vtkdOs8SSV3Ep9EKNh_l9OWNYoS2I9FtcmWgAxxUCwcUTqvcsNer540MLOlYCzDfMglJ1jhVk4itiMOd89-_j4iRGlZ2sOzrdx2AUQCfCC4wmndMnhwS2OzN-HdPbJpEfomxj3C_CjsCrCt2naW_i_Spp519BarMwhWJc9NLCqZBtkC_XVeKQDBPdd0Pl4rB5YGv_EiErPwuWglK7nahYsoygnQBpotyE6cF_uIBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=bwKIFT6rHv7h7wMZ0HcyUVJwO30hmfuqheis4NOTjIyGH8SlqenOQS2Z-YVkcB2vaQ6tQ_xK_OGfbM8icGcoAfHBcKXgIE_1BfJv8dIuQHi62J9OgWbTJ8Fi3cZebngmj7xyAVCgb6NBsAzRFoLpCy65DmnpZmHSOOsfKPTfoNAAQuD2nR19bIYLCumA_DO4eC1vkCO3M_lJe-yIBsirCT_VjGPBMs3_kNtsSZq_jb0YHFGxZeLBiKA_OFvqgBKnNA3Lx2nZrv2mcEK7Fv4JtwIDWCnuX0uU4vBM6vAakQrwZ65WGeVtM6b38tPyKas3-ABLB3BrO_P8Im3Ceye3FESsxUv5ZAvSxh-nJRlNmrrU-o81T7wb5945ep-B0uIC8UWoqAjQCHdX4sUwdGysSk50kJJ4OOOETCdiHeIV5D2b1ZoKFGJw-BEsoku3X8_U82vtkdOs8SSV3Ep9EKNh_l9OWNYoS2I9FtcmWgAxxUCwcUTqvcsNer540MLOlYCzDfMglJ1jhVk4itiMOd89-_j4iRGlZ2sOzrdx2AUQCfCC4wmndMnhwS2OzN-HdPbJpEfomxj3C_CjsCrCt2naW_i_Spp519BarMwhWJc9NLCqZBtkC_XVeKQDBPdd0Pl4rB5YGv_EiErPwuWglK7nahYsoygnQBpotyE6cF_uIBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbcaFRE6JbgCs4AeEp1IkKA1x3gRIXfuDlrrW_3-lDB1swXEAtNql7hTuiYNguKK3asYnyFfgoD_uJIIMwXLjyvLnpEEG5BM0NTvH5kOemS8eZDUcWs0Gws64SCa8C1cqq8Dt_vCQ2nU2DhjXopRRpaarnw3jUy_byDWm1JSYtj6z9hvW6OAom3UqfMzkFnPfkCxEKCX7MkE1Ua4w3rUA4AhF1Qua8eR6PofXRxBtUsSkEH4Yd3CVzrLfXT8iSUUFnSBg3UxL2aKSgh6b5tCrTpEam4OI8_uS_PAD1ieM8ocJTuCjCCK9NNhGYmLWRympV9z9gtVY5UGlGD5foJQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=jQVwvBt-Gg36-ImaRhFkJG19AoF5GId86iTJQicWMttR4Lo4fPfDyg-qG6YR6hwF3-WorPCmpbP5tjxsohTRe5SdXWu4M0o4f-Q89fOvPZAHU_BW8qspxMbO3bJk-mFfvhiKDfvwQms5Gd5thxNmwElZ-W8GVJuhbBnyBUhN-eUHnZbUIMP62Rn5rBgxf8wkNaiO59Q0eecC_EM_a2gfbOkopzNv-MSnspIICWKlWIVuLZcjBbKVKjVobUfD3gDgPgennwFPUpWBmtMD1UBLjaapDW_OItAZj_k3-AmH2w83mnhciuon9uttn1Z96Le7Rw8KafJouVPkQldo-mcR-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=jQVwvBt-Gg36-ImaRhFkJG19AoF5GId86iTJQicWMttR4Lo4fPfDyg-qG6YR6hwF3-WorPCmpbP5tjxsohTRe5SdXWu4M0o4f-Q89fOvPZAHU_BW8qspxMbO3bJk-mFfvhiKDfvwQms5Gd5thxNmwElZ-W8GVJuhbBnyBUhN-eUHnZbUIMP62Rn5rBgxf8wkNaiO59Q0eecC_EM_a2gfbOkopzNv-MSnspIICWKlWIVuLZcjBbKVKjVobUfD3gDgPgennwFPUpWBmtMD1UBLjaapDW_OItAZj_k3-AmH2w83mnhciuon9uttn1Z96Le7Rw8KafJouVPkQldo-mcR-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzWj-RHZcQYNuZhc6T5HSsYm9HMfRp9bPL51m_SxFRKW2BYnEnWpZ37TpPxZ5JsRBtZR7egTrulWoCFlTZlLN1k8L5hXHU5ClfTavw5T9kjaEekOYOGwVzyS22GneLpDR5zoqXxqY1LBC_DaD_6QRKssMlqfN3byCqf_jJRJgM7rd34UunS8MiY6Ql_PYWWuspShadOJLwFLFbwBRl1ovm_h_im-qcvpcg_yIXnd2zxwefRIIJfLjzcj3x2d6IhRIBCPXE0yjOtonxshRabg06s5mMFAUwztxoqn1rLuSwyO6cN4hLq4bMG1t1rna3cXFjOj5cQajqvCx97xQaGMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn9dKMR5fvO-ZWasFVV_OK6igM-n0w6wX1OpSzI48_9QIoIen65pjxBjJiihTePxpwbPVveeVwqyzIclJCOUX19f0pfVQrGJHKFk06NJmFAushBiClWeu671ijcb71tHvXBQ6jaQLNjMj0fDr1e0BL8pLnZAkpJqCQzSMkAyTcnoDFD2tlvRx61mpk2g3oGl6m9q9M9d5GP6Tppno5BujExI3MJjjqpXhasILhUE_fwtg08Z28UNSM6i7p2Etp8fmI2MFt_ExcRu_hl2GHUt4No43rRpWPZKVzxJFTKBsbIF_RdTzSNdI_DYZb1WDSUFItlLmUfi177tELCd-l7ElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_hUx6gbujC3qprdCt_6yC_b_CSMG6P-1sFP4dQpKW1CBMD5UtFXrQvNYkIg3MaHL9_pfH6lyMvxH0bVbgf3ajT6Nnz4tEwxeMaimbWGiw6NEoaqMJTG2ongqb1lFDn2PwUu8X3G7NKJDBHCSxUnCdiFCgIZuvGQKtPvWQJsTvhOdDL08GL4lRtnPP9x50JaheMvmkr4vJhsO5KBqWtbZf0MVoRB429qaoOKVHm_zKn0D6Avy_wa6-rCzMs9bUK5Z7XbA_b5CWvZ_ybXEYc1avItcosduJkz1eTk6f7Xaq0dw7szeOmaqSIlVqCrwW0J2Qt5BbElHSHnmR6nVXjSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpDfhuwUVA7D_vukw--punel5VYWFSWuPlGiBExSYEj--tTFv4eUzPBUX0LQiX_fcPh8G6V9z2nEac9WJzaC-FmE6hFPbLv43Yiz958Qjro4DN7VGFAjTLJh_m8JyODFYYmxAs7Ndio3phyQMKwfIaVFo0lPOpakaRQHWbniwzOfmhex0vrgFyLGvu78C3MAiXupDtA3e6yVXnIQBemQInE5mcqzH3YzNUVZD_CDhL8rHsNCw5YvKr_1CHbf5ul3PDzMktrqT8yKnXB1auS38vTfuLTb8DhGMTPAl9U3pCZCAGfh6NTHF8O5OxL_cAKFcZvZo6m3fU6jmjZQZDl0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfKoV0gTyaCZcUulO6eoMt__181eK1aDzHb7BK9cGQS99Dg907jlT9LXBT2HG0ku32WOusIa_Pj6dOzPabVq0SfCCFquY8ER9KrYh324K6YBX5lYyOKj1HW1lWw_7FEn0AMO4JDzgK7cl5GEUfqMbOGfeVT950G2Psl81WBmNQKy46XVCzBREiCoZfDQ6MmCBPATf_YeGfNcCo6ZvsTK47L9NQG_udQkI37tJ58L1Dk1963XZFgpe1B43bixT7i3WLbQ3efeJBeJlNkR4GhgNJoudo35qIxr7QOSJTo3tdK_D9i6QF-1ZxU09Fig_NlegPDytC2Gz2ULTFlUicMwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=IHrIS2j9oi-GDX6x7kQMPO2zOsrv_dA8E1Nta0ZMkxTIVFFQB-sO-CjlMFIfoiyXS67LUuRmbeNzkkJh2lmxs3X-zhzchkngVYq501P5lGN4WDYFbqCqQDCCbFfoYJuVWvv5iQmc5eE8NOFqADL6sIGUgfF57pfRWxXDZzhaO7lzKGbyCz2Uw_nFaCFeSDQ90nmJLG-AjfkcB2eOXhbvO9XFCT8724TxT4qPlBPNfeGMUSTZAf-86xi_4aZmeEjsnmMmrMKgwO_d0dSmd61hFSJgWitr3Wn8NZw1kWpLl05E4JikLgZKb6fYeFH0gOiNxguEu2nWp6n_VDD80F4LqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=IHrIS2j9oi-GDX6x7kQMPO2zOsrv_dA8E1Nta0ZMkxTIVFFQB-sO-CjlMFIfoiyXS67LUuRmbeNzkkJh2lmxs3X-zhzchkngVYq501P5lGN4WDYFbqCqQDCCbFfoYJuVWvv5iQmc5eE8NOFqADL6sIGUgfF57pfRWxXDZzhaO7lzKGbyCz2Uw_nFaCFeSDQ90nmJLG-AjfkcB2eOXhbvO9XFCT8724TxT4qPlBPNfeGMUSTZAf-86xi_4aZmeEjsnmMmrMKgwO_d0dSmd61hFSJgWitr3Wn8NZw1kWpLl05E4JikLgZKb6fYeFH0gOiNxguEu2nWp6n_VDD80F4LqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwXa9iUMlN-q7hM1IcNe1la2OzoB_pN0HVPwrukkvOm0_0da7dftCGn21pxlXsgVGfBkA2AGQQOaIQktLt9whYODABq66kzCNepfaaiblQ_rU2UceWsbfFV32XJMN9eXQ6145EW-zCsjA3GZDgxgDiouC61ZO0QkEz1rpOWEXXbNhUF3n3wTG0lNimh48Je93aOyQKkwe61h4YM9REblDLvxFmvbZbpWG24IsGnVAsIvxsP77bG4HdBTvHqZzaDDR0ksenxBf32XkbCKSFOzbW1aim4BH-NSWcd6E23LcjhsPd8Sq2FdPxtjZMPoo5Ij2YCXL_jl0hsH01bA9zcBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVISdUPgUwdx_eekRtNcjUJ9jQnnkLoaBE9uJtWXEfsHZ-w2SKNRbHIv5e4aA95PZOQV6qR3r0Oz-NrzLcHdf369SyRNy92XrAngYm6S0bVDDpDfhcny_u9Y0rREK5PHJ9UCpDM853B1EmrWaUPirBq6ogkUWvGutTWHA79zJ9DTPsIC2WY988fKysnjX2gK_WOY22gBZtBqzIIcoQeiNf18MjrkqyxY3msOIIZIiuEDCEDQ1qmtkUH0qXxiAacQx0_QvYYFev-wJk7BBICU2fW45f2lwZWD1ug54ZzbNTH1KggEYhDWc6au-Vaw0vajBKMLj0pFwOdF6agfaGH00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=HdA5HeKvaOCxbZMqgaoOFJW-mUng9lF0-xgjxYfmHyJPp83ODRvJDlitdpeQ3x_hoJbEkacHZBlcxCkSDtNYdeHr0O13NJ-2dO0FtsWjS7n6p_91rJDCxuj8bkmtJdR6U917eF1PpkfsspDZHDRvoFyY0TNEKZkaQqSufKJeIk7B82BpA6ZWFUW6lModuO3GlDpVkimJPBhT0iv_WRKn1_fVUXCromxftYe99YB8DlCoHhtJ16Q5acTnA-T8PK5BDU8-7oThcQVTKGg83IMfWkhBS1Q5klBTTezpkwAyoCtUygy0xWA3fBmZJ8e2lRS0o2RcDB_CK3dAWIT824EGNHM6qRz7mq2QcmdeeXTwhZd9YmQWphwdf9bjx754-e_pMPh1vPLlj0XABjQJs_cOSPTivfiXIU-FZgkp6svZkqGna2KqtLYxJ25J19GHXuVOzAkOYfUR9k5Mb2scurECn8ptwRvtBy8JLzDWKDW22jwtUZY36pJQjbJqBW5ku16cSzK7HJfkJuywt5Zq1VOoLpwO-b3x0Jk5_Z7r6QeG15dPKJLwOmP8UjUJKD70i1JlExdfd7WeuwarxJ50F_OvW_Cu4Sx10vqAp-TEcXBG5aK3bMxRQan7wFARaxZLUoH-_-3NWzWueQ0tZFpsahieFOOVwBp8MpbY7rt4BfSnrWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=HdA5HeKvaOCxbZMqgaoOFJW-mUng9lF0-xgjxYfmHyJPp83ODRvJDlitdpeQ3x_hoJbEkacHZBlcxCkSDtNYdeHr0O13NJ-2dO0FtsWjS7n6p_91rJDCxuj8bkmtJdR6U917eF1PpkfsspDZHDRvoFyY0TNEKZkaQqSufKJeIk7B82BpA6ZWFUW6lModuO3GlDpVkimJPBhT0iv_WRKn1_fVUXCromxftYe99YB8DlCoHhtJ16Q5acTnA-T8PK5BDU8-7oThcQVTKGg83IMfWkhBS1Q5klBTTezpkwAyoCtUygy0xWA3fBmZJ8e2lRS0o2RcDB_CK3dAWIT824EGNHM6qRz7mq2QcmdeeXTwhZd9YmQWphwdf9bjx754-e_pMPh1vPLlj0XABjQJs_cOSPTivfiXIU-FZgkp6svZkqGna2KqtLYxJ25J19GHXuVOzAkOYfUR9k5Mb2scurECn8ptwRvtBy8JLzDWKDW22jwtUZY36pJQjbJqBW5ku16cSzK7HJfkJuywt5Zq1VOoLpwO-b3x0Jk5_Z7r6QeG15dPKJLwOmP8UjUJKD70i1JlExdfd7WeuwarxJ50F_OvW_Cu4Sx10vqAp-TEcXBG5aK3bMxRQan7wFARaxZLUoH-_-3NWzWueQ0tZFpsahieFOOVwBp8MpbY7rt4BfSnrWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=ilpmlQg1ztkVxfA8VgbMWDzEYqINwTDskETUmtdsKRztTyM00eg1mAb_vibvB5UVF7_au_bf1BWQLUlx7w9xTCN8yRsEavyDmAKaJDOhtigg-OrmBCFb5lZOqZrBm7zZXQyv0rmdFQ1V4cpIYyTHxRyqtsOSrFEX32zo23DrCkgrOYlu-haOuW6xiuvnqIM6W1vuOi9vKuZtdXRPZOMGoS7WXG4fZ6QRorNuqtoNswrJHk6noswswq-g-Ky5UHjQV1e-1FVdUKgv7Ph2MoGLi8cIvE5GqzKPcYHQq3QqLJQgEOFjFPCz7ArVTs-B1UBgIm3qcvw-55Apt-zRVg_iNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=ilpmlQg1ztkVxfA8VgbMWDzEYqINwTDskETUmtdsKRztTyM00eg1mAb_vibvB5UVF7_au_bf1BWQLUlx7w9xTCN8yRsEavyDmAKaJDOhtigg-OrmBCFb5lZOqZrBm7zZXQyv0rmdFQ1V4cpIYyTHxRyqtsOSrFEX32zo23DrCkgrOYlu-haOuW6xiuvnqIM6W1vuOi9vKuZtdXRPZOMGoS7WXG4fZ6QRorNuqtoNswrJHk6noswswq-g-Ky5UHjQV1e-1FVdUKgv7Ph2MoGLi8cIvE5GqzKPcYHQq3QqLJQgEOFjFPCz7ArVTs-B1UBgIm3qcvw-55Apt-zRVg_iNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCiXCOt_Hj9BfeMxyUxyLG2Hro9pKv3sJ0Xf53Bw3hiss91g-4GTw0_ZQ9uutHwEF8Ars9n0lSlS43Y8TiPBhavLG9HXXFLuE3lWrRi22146jMhgpTZZgOUTrkszcrnwJ9UEQY7-lvQR8bVbVQoCo2gsfltv5iDMj_Sy3hJLGTG8QOnkzSmQo91v5X640hi6uze3ArX8_v6FKENNTC-L5U1sibceRThISZqfWQ5YPsNL6OpnXvA0zIhxGR_uqs4Gho5xifFROebQ8t_UE6j9gS_ObraidvW_kWmRVRnDjKIKi5flAxjTlOPT09g6EWNpykMLWxNtOwYEHfcoKR4nSG5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCiXCOt_Hj9BfeMxyUxyLG2Hro9pKv3sJ0Xf53Bw3hiss91g-4GTw0_ZQ9uutHwEF8Ars9n0lSlS43Y8TiPBhavLG9HXXFLuE3lWrRi22146jMhgpTZZgOUTrkszcrnwJ9UEQY7-lvQR8bVbVQoCo2gsfltv5iDMj_Sy3hJLGTG8QOnkzSmQo91v5X640hi6uze3ArX8_v6FKENNTC-L5U1sibceRThISZqfWQ5YPsNL6OpnXvA0zIhxGR_uqs4Gho5xifFROebQ8t_UE6j9gS_ObraidvW_kWmRVRnDjKIKi5flAxjTlOPT09g6EWNpykMLWxNtOwYEHfcoKR4nSG5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pmq59oR2bKo9peHkDuFc7axXklPFmgKPBVV9x3SUZfWECvsaJT3uRPNJrZ7hiWX1A5l9UehWDwMkInn6AyVRly7pxSQHAbnzI_N5PVsKbK22w4z9rNfEQWWbZtfaBJa74zIdQBNnFKkW0pul8Y0CHr5e2uuSkUVjXsuYW17dnyVXzZClxhLl9RrGsZdi5YowEWkNCid5nWBse9HsgI5N2DkdTg5qqhJGmppV2CC633yU4qkbW-nu7V9GqJS85FIXm7S6NiXjCpEIdUrHr8wZ33CcTYjBn7Ws1z6EYVZ4twmhqHE-v8D5Jr8H9kPoBt1hLqtePsrXVDoFxUU4hymQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVpYMkplWp6dtx4dFq52cnkRbB6t_eLiRH-MminF2zbZowN9fng43vt2K5Yf4PFqgf6ARVp8Xk8O-PiCmzWzw8jl7217yj0yH_aUmUc45YaDYYLl3ajRtIxP9Akk6TSJGbK0YxV-m6O7M8xT7naF2n2GL1TZNNd9FVwwT7l62AsvyVY1zYsDev0WPsYE_6UKRqR0O4fsixRRytySC7X850ir4i4vyxbHl_XUuHJIvEji6E-FyajTTp147Pc_3QDfOf6QD4QxEX1yS6edbYd8pJg510BFb4bY1OMKFrms-KQc1s31UakB5LqF91Lw4gKM350nCC4yvVZDtR2Z6dKdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh6Bmse18pM4WSDY6qkUBxbPARXmbfcxK2imTSkNCCNMDVXisrHCxKuZPUYHfyxVWqmF8Y07rHglPZxKCJDd_4qKwwl8bp2Byb3NBFoDcVfXh_lUQkLVWdeirp8rf9mk9wo5GhoR0Tm2Sp_uWMAXSmJAe62D_Xb5a-UXXXPPpxiM0fyHb4mwsGtTYQMM2-i10pE4wUcv7Wc0IlR9t1_UCg_VYuuiFuDSZsyni4vY124HC-D66fPee-7D4535865F7t3UQ2o7w5XpIxYtsb4ThW4OzvdCe99ihJ6vYOqaJjN1u0Mwl6j_ev9SMmLuteyyGGiqmBG8gsXQmv3k--UwxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=WcJz46VrhmFiya0lFT2Yhp4KjrTaJaoIXA5-MMzyYNpEEaOHTe-t6Ul4Gjlcg-BKx5lEZ9s_6wzmFT7Xt81TAl4Ve6wtzbBFzUovgxaaijQnekp8Uqqs7FFvdPZW2NsGnwP327wPx-BquRsFr1JnbBDhoDcAx62NgRCTwmrEIgSJFFSc6dWNwgEbz_v3c0eFs2XSVHl9zDU_jhjkms8J7h9_IylOxuk7wPFzYtD2lExO74UH_gtGXeFqHChSFrK4cPRIk0xVz-Z7O5J-vEh5fEGc4xpSh1lb4MiXmX9LMDV2S-0iG4Bh6Tg6LfMYTuPnLvEicVv28Gul_n49QmgSEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=WcJz46VrhmFiya0lFT2Yhp4KjrTaJaoIXA5-MMzyYNpEEaOHTe-t6Ul4Gjlcg-BKx5lEZ9s_6wzmFT7Xt81TAl4Ve6wtzbBFzUovgxaaijQnekp8Uqqs7FFvdPZW2NsGnwP327wPx-BquRsFr1JnbBDhoDcAx62NgRCTwmrEIgSJFFSc6dWNwgEbz_v3c0eFs2XSVHl9zDU_jhjkms8J7h9_IylOxuk7wPFzYtD2lExO74UH_gtGXeFqHChSFrK4cPRIk0xVz-Z7O5J-vEh5fEGc4xpSh1lb4MiXmX9LMDV2S-0iG4Bh6Tg6LfMYTuPnLvEicVv28Gul_n49QmgSEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw1WPk6o297T5LMaoi_v_ce0IwJQa4zfwuXmnfeJK1FqGqUAjZcXFRVkhsLnG4c8XdPv6hbPVJAPoAAKQ3wVViVUSbOn3S9meetKwC1QxMG4_N10vt0DwNwbnf25XQYeAgdSxx1I3tGpXR4vCPd8SaeqODb7XNTi8UeR3STGpIdT8ypFpdJvPwliBGYTn_sGzY3Q0aTnvGqBRRqfEkDF7OVjPS42QGcCjnlohX14lB6yKOKjg5X4LE_8MoGC6vdPp8rS2broCgH9kdtmF-pjLFrH4PskFEXNZ2dYSoJXinVzWNHcT_IaiRVBsv56LgH0Z-NRuk9GGremNYUpxATdKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGN4nLPuIdFRYM06Wgy4ICm0CTeX1ltyeTJOO2bAOGxEGdPZU5mk5xrpG9vaiQ5DaFkpYVZWv4LFmyRSS8nLB6-P8sSOgZuve9t5cyKiAlP_I7kzptRt5qtNcc9Fcw03kdE1XDbqVbNqa9Iux7QlC9ipeoVKoYNk8nqtuW1hvVoDje6Z6xnYfWktpCbYebAu3bdX6SXrbqhdT7krBLoCtO9RsEf2_OMm8XzwRmaLCXI3AELQcNIRtijQD-6S7ib3tox2iFmOMoKaP0c3pXM5pso6_wavIJazVoJOVOibmHWqaBghyKOG1-kK-bemqZqfJDgFe63VuA647AKx6Oo1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FaISjj0hO1DK0GDHL1HOM2PIQjieGZPGnpQk9hNK3F5PSSwL76d48Pu_9EF8JC_RHD4sa5kzr2fES5qgv_mNSrLO9xdyFnNdvg_iZaNfhJXfrGimuLmIoHkACfTjwrgIArAV8lgPUlIeNUdplDI16DA6Ksnudjjy5bCyyvSzedChWEhDzSv5EZupV-MNi3lLGlwBAlmVLaDWH8wL-kgnTAmw6-PugQuVDWitSdpIuo3fYn5dqA4xgF6d87OclMuiwE6c1kDp24-sh7FkWI1GMkyIY1abOTqrNOE5Q20Yg4AhfjGsNFyTcVpOtkSu5GjtR23OgqzKDXU4yjo1eVybNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0Dj3ACMHPUjMIwuaTnVIeQiESIiakgp0vjYO-3sWPHCXgwWjj2cT-ofWtKTmU0C8bE-F9CpiGC6AuuLxhvWdmPgszp7ohEs9iQNJcD9YR0Rk2gKLK5SkjYaASnsP9SWGIb_m3NfSZmlyG6GyrmH6_JnnXvEcS1307N0IYhaA7q545MJyRzuXzYhTq2aMaphOYndwPrIsZoMxCeHsItT-fvZ4nMMAIx5ppyxj9vAlzgPBueQOj95eRBzl5ZPJ309wCg6gDINcxCUrUdUDfiXtFiW5ZkOEkIoVgKIT6-80f7mCgvEwCIEEqfMs2f1zHpXIfDHeK4RbxwKjZqEyhYfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=nl8bUhJ8gQDuuI0N_8cLK4QOxGUTnkMCi0m5Vv6EKOmk3imtgrHMTxmSQsIu6O9TJLUrC1WtTI6rig8utlEcSHS4i76u31bW1fAR9dluL9FKQaxqhGGV08ofiGo7SIe_PaOpCksb7RdxXnTu4isIM2a-eQEBckvB8EgLJtbscXwBqhXbAKPVRK4SGoOi8uh1-VdTFmQ0Z5HnKdLxfNWbnEBISEjyM-zYJyGZ1GYTQ1ivisE-tyrEe5qmz6q0P3yl3bTre5ub1h8tcw96E_kdxuoahhFq7_DaU5HUtXKLH8U-2Ty7qQaQiqJ0QHTiRSotOmMYKQPGG4CheBUflYCYA4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=nl8bUhJ8gQDuuI0N_8cLK4QOxGUTnkMCi0m5Vv6EKOmk3imtgrHMTxmSQsIu6O9TJLUrC1WtTI6rig8utlEcSHS4i76u31bW1fAR9dluL9FKQaxqhGGV08ofiGo7SIe_PaOpCksb7RdxXnTu4isIM2a-eQEBckvB8EgLJtbscXwBqhXbAKPVRK4SGoOi8uh1-VdTFmQ0Z5HnKdLxfNWbnEBISEjyM-zYJyGZ1GYTQ1ivisE-tyrEe5qmz6q0P3yl3bTre5ub1h8tcw96E_kdxuoahhFq7_DaU5HUtXKLH8U-2Ty7qQaQiqJ0QHTiRSotOmMYKQPGG4CheBUflYCYA4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=kQumopr-xgq5F0S28Vgd_bzoVdwEwwKpbr5LjL2Z8o2Na7zzYNO6mdruqTwotHPummO9hZgHXT4Zc-OaYP-UpuB3KukQElFY7Y7ed0p64Ycyq7NGVA3jEDonz67aF_C5F00FbvWH_0bgZJF-lyqEUVKqhy0tS13Oj_ZiqTy32OLd_ezoebR45itBMlFAN1BWgi_aQmx8gIgzOaok20xndTBDZXm_c7B2d9sbRnNWwWq8Qdj0fPajTly4Li5zLRcf5prk7K4WdPqQXkoGqwxcMtrdY-AaGyAxyH11L9xGTcscxXQx_-Qepht9Ab8WRrW7zOoEfKmC9KZZWPJcYCPN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=kQumopr-xgq5F0S28Vgd_bzoVdwEwwKpbr5LjL2Z8o2Na7zzYNO6mdruqTwotHPummO9hZgHXT4Zc-OaYP-UpuB3KukQElFY7Y7ed0p64Ycyq7NGVA3jEDonz67aF_C5F00FbvWH_0bgZJF-lyqEUVKqhy0tS13Oj_ZiqTy32OLd_ezoebR45itBMlFAN1BWgi_aQmx8gIgzOaok20xndTBDZXm_c7B2d9sbRnNWwWq8Qdj0fPajTly4Li5zLRcf5prk7K4WdPqQXkoGqwxcMtrdY-AaGyAxyH11L9xGTcscxXQx_-Qepht9Ab8WRrW7zOoEfKmC9KZZWPJcYCPN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=gqHs5bMSly4BgctZG73SKoZMJtWvwXZGE8efZQZvtJgdGCt8KKIL-SOE7IghzlXAsZXSNcTnlRW-QUfb-Zb0Zvh90g9dBsY-DM8GOpebCBx5fO_g_o8qi7zbe82kPs9MqmFnbr7ioldPI6f2dzO2pzaW9kPNCUxjxsUqYDx-x5taMuglLyQJl7_D4kgmmh2dvO0_olBIYLKZ6EEfVWYbXbV_Yr61X8NL8jlhcaOb4ivtSehAelBigDpsj9TDrIlcoxW5ds11KIEt04CmWBZqifZ-qqu6qvVbi3_QDLg9MafbVhluc2FYpP-xwtIBt0QtKjhs78H4lyMG79C_M4z8UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=gqHs5bMSly4BgctZG73SKoZMJtWvwXZGE8efZQZvtJgdGCt8KKIL-SOE7IghzlXAsZXSNcTnlRW-QUfb-Zb0Zvh90g9dBsY-DM8GOpebCBx5fO_g_o8qi7zbe82kPs9MqmFnbr7ioldPI6f2dzO2pzaW9kPNCUxjxsUqYDx-x5taMuglLyQJl7_D4kgmmh2dvO0_olBIYLKZ6EEfVWYbXbV_Yr61X8NL8jlhcaOb4ivtSehAelBigDpsj9TDrIlcoxW5ds11KIEt04CmWBZqifZ-qqu6qvVbi3_QDLg9MafbVhluc2FYpP-xwtIBt0QtKjhs78H4lyMG79C_M4z8UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnpxagxkcR2cuWRRDpksNPEu7C0H-TOQ0jaFMP2MMSP9ftBo1Dj361w7TbWG9MR7ZpoBEgKsUdy8LjDE41WW867OpfDRD77rH-DnOde4wwfqEcmQqIUL1F92QfgM9ucZ_MtP1tJmMth9r9l84IcE7Q93srdrNGaZUq10N5nIk8ECqIOOaZQguRdvEVFYJYLfD9Ckg3R_Jd7h4SUWGhrO4SJy5glnk2qtplteGc-CCwM1BkAifbR9MGwBBK0erD21os6C_pr9Tgp5fK73Qn-FpSVBRpGAOQsCgbXUXyLocBFG_lXz0Xjw8n_igwg8Nt9TGTV8442R4jBGnR_nBOA26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=kpqGiU91w7UcIwEzLC2X7BJx3SGkKck3pnmN5QicUFCDMzkFE3Ht4rhQtJwrbHkPkXQSSee1GQOAdTyddBg8k9Y8S4Du492tGtZSkOEJ_Rp55NsH5pEU8ojKSd52JDrHwL83yRKW_t7NyBLYLFbULxkGGJoss8NrLIYjdli7nbphKw3zVQwYQYN4It0-D1Yd_jjhqNVQ05nLNPQiBM63Ne_oKay0-NnEt9bUJseytbgbD51ORhdyhS2mNSBB1KYOigTXyqSTcvaWHFoqyI1MqM2tlg2GS_BnglE4NdDzCysQ2Ut9bysg4srwqVQkJsaJADn8HTlNcyNnAFLwZ61E9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=kpqGiU91w7UcIwEzLC2X7BJx3SGkKck3pnmN5QicUFCDMzkFE3Ht4rhQtJwrbHkPkXQSSee1GQOAdTyddBg8k9Y8S4Du492tGtZSkOEJ_Rp55NsH5pEU8ojKSd52JDrHwL83yRKW_t7NyBLYLFbULxkGGJoss8NrLIYjdli7nbphKw3zVQwYQYN4It0-D1Yd_jjhqNVQ05nLNPQiBM63Ne_oKay0-NnEt9bUJseytbgbD51ORhdyhS2mNSBB1KYOigTXyqSTcvaWHFoqyI1MqM2tlg2GS_BnglE4NdDzCysQ2Ut9bysg4srwqVQkJsaJADn8HTlNcyNnAFLwZ61E9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Nhte-l9_cfsrkx2jOUdWchTpekoJTGXDJg1q8vRDVA8_EX3wE9D4BnS_hXOl8QVo4Xnj8aqpdJwypwrzWGAoWX10IOv9hcHXszEdo0BvHfh8OmaN2uOvG9NdAyxpT-Qr3p4dBK9rASL3u1EElEgcFaBL_rOdFgIokArJHj1PiJwrqQLvpZEAhbbQ-PGB_tcUo6nkSjT-hp5wa6za9jxDzDWIPk8rU0RL1uo7F1VUMw-uLVVVftOwquxdAEtGf4rTfywolhS4aoTBnXVcyXfilrvAdy3iOZDn_G4zVLpWZHD-xYtZGhCkGrWzEaXieXN7HIaydv72mKPTR8KTOm0lnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Nhte-l9_cfsrkx2jOUdWchTpekoJTGXDJg1q8vRDVA8_EX3wE9D4BnS_hXOl8QVo4Xnj8aqpdJwypwrzWGAoWX10IOv9hcHXszEdo0BvHfh8OmaN2uOvG9NdAyxpT-Qr3p4dBK9rASL3u1EElEgcFaBL_rOdFgIokArJHj1PiJwrqQLvpZEAhbbQ-PGB_tcUo6nkSjT-hp5wa6za9jxDzDWIPk8rU0RL1uo7F1VUMw-uLVVVftOwquxdAEtGf4rTfywolhS4aoTBnXVcyXfilrvAdy3iOZDn_G4zVLpWZHD-xYtZGhCkGrWzEaXieXN7HIaydv72mKPTR8KTOm0lnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=vuqlvy3DgQ1cGDXpdaUxAsKzSL8OXWiuEyJHKGeaNMuJBVkyIombJArXqeuSydPEi_N2lrjU1KqRcGVzQDGv_pJO2hkZv26XKZjvxXW9p2-ouOPCANfxukW17RV0SBfja6F-zcjReE3RklY-cfFNd5pJgoZTKSkZ-3CLgJTOXDsug9jYNt6kwiRYaVHZ5Fl_C9w8mBLhxAOkkgqAtyp8oFM1ceAIYMMzNlTXzL2eEvqapYaZ_7dKG8rZA6CJtsOP3STXHTK7tHLIDfxc4U7nQJV9gGXBxBR0OaAdmcUnBQG6hamz8wKwq_D1KYg3fI979KM2sjy4MfZxDNQYiAN-UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=vuqlvy3DgQ1cGDXpdaUxAsKzSL8OXWiuEyJHKGeaNMuJBVkyIombJArXqeuSydPEi_N2lrjU1KqRcGVzQDGv_pJO2hkZv26XKZjvxXW9p2-ouOPCANfxukW17RV0SBfja6F-zcjReE3RklY-cfFNd5pJgoZTKSkZ-3CLgJTOXDsug9jYNt6kwiRYaVHZ5Fl_C9w8mBLhxAOkkgqAtyp8oFM1ceAIYMMzNlTXzL2eEvqapYaZ_7dKG8rZA6CJtsOP3STXHTK7tHLIDfxc4U7nQJV9gGXBxBR0OaAdmcUnBQG6hamz8wKwq_D1KYg3fI979KM2sjy4MfZxDNQYiAN-UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=eoZcjvlytnoA68DfAHKBuubed_AYxIvl-8awuI-n3TCSHUn13JK22D6kJFP4q5fyr77EjljwSP3oSP3ymtQCvYfMZcMMlAjB0OCK5QPrm9-05UCslgj6ZSq_57hpGKg2dh0JY6r240EMvoeyd2mdE6LZBptSM18QHNuFeSw9qKEoXGszrdToi6UjirYQMNDn6VH41_Yk9eCJ0EaKNeiAOedlo4jl8o9Ny2Kh6mELa1PZ6Nn8fMh_QxJdQkMAO-_pLPAeJZuycz6PV_egKBangHDLIjBrU1HEKfRLX0NBx9mgvdHKDBdXnrYXlN6GsRucSwr-ts8AHYgDqEgL41kJHIei0T9Tbl3ScxQDwh57loxiQHlAPyT5Tj8-U6xtRKK1VRbZ6w7n4KBfpo94XCac_TcSfu7idfOaonTt9MiD6azg00bXNqUFn_WFwCZGQs4OsJjX2e98oZ1b7dCRtq5DhjGqM9Fd2kNmhRNQkKWbRWfN0b2LeDLMUqzrP5OLx5mb8TSmwPRrZpdp2h2hjkEVkOo_VzoiTBabLqNHNp4QJiFF9REaAEfnNveA0AyX-Y0yIsN62VqNX15AcKIK-49gMHfFRtXDNCt4QGJLCSMZGonxjPf_vyWUt_n8Qj7CHfxfJ7pJmTCPKqoQdc9iUD1Ws5vDZUs3Fr77jN6D_eCUg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=eoZcjvlytnoA68DfAHKBuubed_AYxIvl-8awuI-n3TCSHUn13JK22D6kJFP4q5fyr77EjljwSP3oSP3ymtQCvYfMZcMMlAjB0OCK5QPrm9-05UCslgj6ZSq_57hpGKg2dh0JY6r240EMvoeyd2mdE6LZBptSM18QHNuFeSw9qKEoXGszrdToi6UjirYQMNDn6VH41_Yk9eCJ0EaKNeiAOedlo4jl8o9Ny2Kh6mELa1PZ6Nn8fMh_QxJdQkMAO-_pLPAeJZuycz6PV_egKBangHDLIjBrU1HEKfRLX0NBx9mgvdHKDBdXnrYXlN6GsRucSwr-ts8AHYgDqEgL41kJHIei0T9Tbl3ScxQDwh57loxiQHlAPyT5Tj8-U6xtRKK1VRbZ6w7n4KBfpo94XCac_TcSfu7idfOaonTt9MiD6azg00bXNqUFn_WFwCZGQs4OsJjX2e98oZ1b7dCRtq5DhjGqM9Fd2kNmhRNQkKWbRWfN0b2LeDLMUqzrP5OLx5mb8TSmwPRrZpdp2h2hjkEVkOo_VzoiTBabLqNHNp4QJiFF9REaAEfnNveA0AyX-Y0yIsN62VqNX15AcKIK-49gMHfFRtXDNCt4QGJLCSMZGonxjPf_vyWUt_n8Qj7CHfxfJ7pJmTCPKqoQdc9iUD1Ws5vDZUs3Fr77jN6D_eCUg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=gbmlF5-pxL6ZoNHdvhx_8qhxqZMcHs4l4e_VZ5aFbUdqek7iLfA9DyqyBohdjXSAve6HM7R6uY6Er5_ihkYrsxcPgJtXW1jbB5ZEvz7TzzK85ChmFe_TsunrMttDLqYWgOyQr6ELdajvagTPwUGzX_SJOBqdodSL-jzmeWTfZO-iOy67UWWnTuqo4kJ8CmHoMjz8uTtBbO0KvCv2dE8rHfGa9LXUQznX2-G0mmRFg8aWuL9wNY7P1BxioABecKJpsw6ZDfYXy1tmomebCvb7Uz1Alcd_ZbyB1jDYBTSP5_aaFzdfkHyymllnP_7LNozTegKO05ZCXUPB_DJlsUnVOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=gbmlF5-pxL6ZoNHdvhx_8qhxqZMcHs4l4e_VZ5aFbUdqek7iLfA9DyqyBohdjXSAve6HM7R6uY6Er5_ihkYrsxcPgJtXW1jbB5ZEvz7TzzK85ChmFe_TsunrMttDLqYWgOyQr6ELdajvagTPwUGzX_SJOBqdodSL-jzmeWTfZO-iOy67UWWnTuqo4kJ8CmHoMjz8uTtBbO0KvCv2dE8rHfGa9LXUQznX2-G0mmRFg8aWuL9wNY7P1BxioABecKJpsw6ZDfYXy1tmomebCvb7Uz1Alcd_ZbyB1jDYBTSP5_aaFzdfkHyymllnP_7LNozTegKO05ZCXUPB_DJlsUnVOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=CP4M7UQ2bGyLPus5pVab9nQGI7V4lMebnlVJ7jpbETTuwiI4jQTDhzTIuPm7GuDa8po-NeXQWGXPkaJfrReqVcBx5UWsgxwWILbW2a0GedRGqkkqFYx7jwcsSu8wJ5z5DLTJPtm0ITxaYEI_0ncqFzvPhH3_RG_soYiTwK1sK--avHOU9FXhQtunTFvt24RiTCQXKCV9PLBM1hndCTcfwggX3WwrvKRdY2bUCdbgefFBFh-ZJ3luGY8shJzeaicar6PIWOsmsF81PLbS9d-WrviLzdcLnl0q0F1kOmqflNbv64yqfY8FbVqvQGGP_8WumhZViMbxjXVPv4rkVMQ-pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=CP4M7UQ2bGyLPus5pVab9nQGI7V4lMebnlVJ7jpbETTuwiI4jQTDhzTIuPm7GuDa8po-NeXQWGXPkaJfrReqVcBx5UWsgxwWILbW2a0GedRGqkkqFYx7jwcsSu8wJ5z5DLTJPtm0ITxaYEI_0ncqFzvPhH3_RG_soYiTwK1sK--avHOU9FXhQtunTFvt24RiTCQXKCV9PLBM1hndCTcfwggX3WwrvKRdY2bUCdbgefFBFh-ZJ3luGY8shJzeaicar6PIWOsmsF81PLbS9d-WrviLzdcLnl0q0F1kOmqflNbv64yqfY8FbVqvQGGP_8WumhZViMbxjXVPv4rkVMQ-pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idi1k-8W6Ge0QOcftpJW4N-qzLoR42-2d_D1jMjQTY_M5SiI7JU8gpqwy3kQFnlTIJnUlo1KvDvfCAwhh6jQvgHzuq_lcwfxghB608LYSLFqgcOy0JqtLfIWCKe975tber4gWVnJ41UmEa0ZyfhGm-fCfwj05uOmPftngmqUhTV-j5DHjnDPJ9NtweiC9cjtShsKq1f4VVUHtSR15nfrAOApyIYPrq_Dfal4HAGZhnM9r3m42ylg2PfVq93y5w5-QBvl3mR00xgtgVhZzFy4iLNevzIFv5VkvzuU8A4Nc4FYGONqFw0WrxPcOK0plI0t-JynEB-JcE8lPg9jN-A1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvGn7_rzUWQlpWThbThqDK0mx4XxmgdWzUysE8R9do_32LMdFFnvR45z126x5al-WUKMRfweT06KLn0s5t9D5ICj3rCzux8u2vPqFjWzqDGwWDz5oUaY_annhliWvGYGvE7KiRDMugKGo0qmE7VK_QmNFcaDgPI-7Zss7wu8wN73hNLc9jm0yN5WxcDUC4-k9lLZWYsv7q1c-plY3wpGU8alT8m8EuPnwRWG8piPPNSwtlWv9OuLqUOD472s0zUYahXZqobVyBVmq3LdHB97KfdEJufQ8CsVgjryvb7N0svUmFR4tg2pHEgrgEIHqXI3zYdBP_LgEmh-rqD11U9gTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=etu5RAV-sJjXYveTT0Auje17_i87lV8kysFWzDPDyl3S7O89ys4w-3XlR8ii8Ci0VbgiWuI3E84Uf8m3Wh_b6xyiMPREIJKrmvfI_SjjxoKhmliZmR_T1J63rfedexiD0GudOZdLZ-3rI7PuA2J5nQsFBxl8T9O4b03gnEHkOObBOE4hyI_hGYO-ofOH5JpZI7D_N7gQm6cP4Ks1CF-KDmAjGLVDkFm0aENjQRmZkBdXIUbIRLTcc24ouJ3VeJrr2zHbGd2OjasHVJPFrCXbHklxPPKqgUGHvRzR09do_XY6ROTRN_KGlPf9dDE-5DTUVUlrR-ePwjHWolF4YhVdlHm-cyrRK0rsGddphnWWOS34uMA7BbWQKiD5hxfoXYq1ic29ihJpAq5Al4I7tdTOpEKMPGqnjzuWmtAOR5NleuOaHKwzUhD_Qak2UhNviSXmW8S3GUk7Z_oYMpZ8TBXEXkfJ8wwk5kAtTsGWkvechZFmP7dXM0NfmfCPIheKHaHsM6MLtdH-LcIYFfu1aENufjd6RUHyQAkpkIAcOEU1Gp9mkNul6Ybil4nvra78MOc8loGKI0VwkJxQxG3Sat67OeK3h4QTyskSON1qcGzeaRokLq-ucNYrH3FnvwnYkjNacpnrc7QG9ejxfIEz-c4my0pDg34HE9NtqKICT-bkIu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=etu5RAV-sJjXYveTT0Auje17_i87lV8kysFWzDPDyl3S7O89ys4w-3XlR8ii8Ci0VbgiWuI3E84Uf8m3Wh_b6xyiMPREIJKrmvfI_SjjxoKhmliZmR_T1J63rfedexiD0GudOZdLZ-3rI7PuA2J5nQsFBxl8T9O4b03gnEHkOObBOE4hyI_hGYO-ofOH5JpZI7D_N7gQm6cP4Ks1CF-KDmAjGLVDkFm0aENjQRmZkBdXIUbIRLTcc24ouJ3VeJrr2zHbGd2OjasHVJPFrCXbHklxPPKqgUGHvRzR09do_XY6ROTRN_KGlPf9dDE-5DTUVUlrR-ePwjHWolF4YhVdlHm-cyrRK0rsGddphnWWOS34uMA7BbWQKiD5hxfoXYq1ic29ihJpAq5Al4I7tdTOpEKMPGqnjzuWmtAOR5NleuOaHKwzUhD_Qak2UhNviSXmW8S3GUk7Z_oYMpZ8TBXEXkfJ8wwk5kAtTsGWkvechZFmP7dXM0NfmfCPIheKHaHsM6MLtdH-LcIYFfu1aENufjd6RUHyQAkpkIAcOEU1Gp9mkNul6Ybil4nvra78MOc8loGKI0VwkJxQxG3Sat67OeK3h4QTyskSON1qcGzeaRokLq-ucNYrH3FnvwnYkjNacpnrc7QG9ejxfIEz-c4my0pDg34HE9NtqKICT-bkIu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdlaSQv7n6NrZrpkImTRFteso2lB_Yxl96sxdIPhiND0wvygU_v0sX3CDBZgWqEX6vgDSqq8uGYKi0XVJE511QVrWH4g1xmKPaMLjY4CU1YyIxC9xDW0GTWsZW6ua5nWk4UnGKCbqblMXBBIaoK6sXk49oso3LYiumwWs6NTa3LnzkqNjzGU_A73dXFwqyzCY39wklaexv_15h8Ym2b05dfDSjs-RqirnvgjdYnBxxEiTGR9AV7R3Te2D1UbCcED6L82i_2YRknWN3vZ4EglAK83u0AiHCn1N_739UEePAS60-D7ocCyenotFwntraKX3A-_H0iE6PC0A_OnFop1ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mvg342OAzuYHl5m2ToC82U6FjqFX18poyLO4QCAQeg27krU4t35JHBywHnW5lgRXOqvMZTv0KjNV44Ff8QYw-nvZhvA0-LgREqVZ6YQIwzdkZzZPwWSs4r24uJgsY8AksW6tL_Nb2lHTtptPprE0yrl5KKztVkestcCm3h29chBvU1mPwS2rS_QGKtqABDreS7BeO5rJUjf2r-kqMXF9oPwOeJcbw3AC4OL11IHMRNINuCb_sYHHp85NjMJQ2_M6v66rdkGV7j2u9KlXXVKGt6fTaMv_6ZMdxbdIj17GKr2MSgLjLAv-tdF3CDFww9Uia_SmodG80eiykP4DfjPvHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAXj3t8ZimDHZQqirs00S1jPpjgL84BwzVcT_BIYvsyLFtg5sWf_DMAavHeUBQK8vWzPPMUlOGSFlfdrgiMAycvFTyQDXFflRDK9-GR1xe-6DfV4klikaUo0Jla7xq2gqOmbw9qYlwnWxbJ0tPmKppmNQiOpbPEgWH_glMe18NAeorveCwRh8TvN549o1HwF8kTFZ2-_JzrFg4uK0GmxLgq8ooI6-fDbBnRAhuqVbDfMKLqE2gmwzI-HFoi15wijW4e7o8yS8q07iBhZHpTAzxWnfJJAi0l46M4NFFF3WY4c9jrnJgCKuwiGQodZnn3FuosastldANIpjita73wBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmU38UBAfpVwv2qX7DvEwdC_2JRt_FEAkeKb3HA2Io1yjWkC3TnyvzfkarNB8Nbzj5IOReyUfD5N-KKSibL-pIzJNoL3E1KGvVCModVH-_sQ3zVpOoQj0AOXRdi5oljs9S0Q6QGAZeQt6j-Pw0irdCzBf9MyWwycoYSO1UPaY1kzXSFH6tFIXIODIUtpgnTqnYuO_3-SzZWXsNn7qQAziOIzhKlHItL1qrKUF246vKBOB58FfoiV1xt0XEX-iuPm_Q4vG1az-_aiLwhW0EmJQwb-rY6uy_V8yJD5YS-5i_HhIgOxXggCgYgupjFiptp0sJ430hskM5_C3XG0SPmjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=gHphpaTqQoAG0OC_FABqI5kSRfvCohgaXgihyxN3TEgy6iMXRGq2EF6reRCi-etBEfosJ_xD89ZwDNMw80P132OKo1_sQ3Kd1uQ_F2RdyHcc7MT0yYUECvscOHDVZPNzCzt8HUERtuNl_7qgah_TDMsF9D-PnLYaAb80R3TvNAznzOMD7wZ4N2DPx_3ol24j_bTUY_7cmyo6FCzzv-zq8sZIj2tU3naIv5Tbjcv5y5RITTpCUwqAvvCWiPu7a6aIbQTCFxwzkgAZKtqWIAT5j9K_t5RhZ5edWSecfSvBcsV3ZuFuCmB_78hj72LxiCmeBz5qRS6KlranSD9tK_CMfT4TRVlkjIBVi6EkU0jyv2IRspe9omK-gwq9hbyRqCeLc9ZSTciW3IXwENLqrT2oUz_VeVGYAiRng-ILCFnh8a8uxLpV6-lUuiMWB2_ynz_9IUpwpGFNGnbyr--nwBdQhzho6gdjs3EkOiZuiiZ5f5rtkxNFn9RD0FkKbsSahc1XVI8C9pk5MsqjeflohRP2RHxAvwQ8e6BYQACYUjEBzlnGgtqk6qQJqaovWUPuFp-Vd0s3SD3vpZnAX1QQyqftWUTPE8qdpyd7hmoJKEMVpDsBbFMFZrxDYr4BKh-PuDYC0LJU2qEiglQuxpimh3_nHQBVLI-lSI641JzAklC0UPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=gHphpaTqQoAG0OC_FABqI5kSRfvCohgaXgihyxN3TEgy6iMXRGq2EF6reRCi-etBEfosJ_xD89ZwDNMw80P132OKo1_sQ3Kd1uQ_F2RdyHcc7MT0yYUECvscOHDVZPNzCzt8HUERtuNl_7qgah_TDMsF9D-PnLYaAb80R3TvNAznzOMD7wZ4N2DPx_3ol24j_bTUY_7cmyo6FCzzv-zq8sZIj2tU3naIv5Tbjcv5y5RITTpCUwqAvvCWiPu7a6aIbQTCFxwzkgAZKtqWIAT5j9K_t5RhZ5edWSecfSvBcsV3ZuFuCmB_78hj72LxiCmeBz5qRS6KlranSD9tK_CMfT4TRVlkjIBVi6EkU0jyv2IRspe9omK-gwq9hbyRqCeLc9ZSTciW3IXwENLqrT2oUz_VeVGYAiRng-ILCFnh8a8uxLpV6-lUuiMWB2_ynz_9IUpwpGFNGnbyr--nwBdQhzho6gdjs3EkOiZuiiZ5f5rtkxNFn9RD0FkKbsSahc1XVI8C9pk5MsqjeflohRP2RHxAvwQ8e6BYQACYUjEBzlnGgtqk6qQJqaovWUPuFp-Vd0s3SD3vpZnAX1QQyqftWUTPE8qdpyd7hmoJKEMVpDsBbFMFZrxDYr4BKh-PuDYC0LJU2qEiglQuxpimh3_nHQBVLI-lSI641JzAklC0UPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=tpEUVwAkXu5WJd_jfWBubvRu2V9NYYB-VUbxjaKj_ubkjVjsytEA2LfQwR9lxOfUhQc7G5jVMZAh0u1gaS9VsW7OFl1UBqkCtW6GtOz3UdE5VH8TtDGhmt4r1-BTcTrJAOjU4T_9LB39e_0nXoV2jcEOTIw2wHT8sEj2vbZSQ18JZ-Y6XH82wWBmq-ZUAlkENYf58YKJbR01A883nJn7i7d5k1kP3qAIadFlajgMWZsvA-_2z0pL5G0qsZPCr9n8ZFLy60Um02aggR40KyWMPqhHosG-77QuNX4YQ-1nZtGYRo3qHzYHY2NAMWWhFxUiT1gGl3HM2YEKIM0ih4H_Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=tpEUVwAkXu5WJd_jfWBubvRu2V9NYYB-VUbxjaKj_ubkjVjsytEA2LfQwR9lxOfUhQc7G5jVMZAh0u1gaS9VsW7OFl1UBqkCtW6GtOz3UdE5VH8TtDGhmt4r1-BTcTrJAOjU4T_9LB39e_0nXoV2jcEOTIw2wHT8sEj2vbZSQ18JZ-Y6XH82wWBmq-ZUAlkENYf58YKJbR01A883nJn7i7d5k1kP3qAIadFlajgMWZsvA-_2z0pL5G0qsZPCr9n8ZFLy60Um02aggR40KyWMPqhHosG-77QuNX4YQ-1nZtGYRo3qHzYHY2NAMWWhFxUiT1gGl3HM2YEKIM0ih4H_Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTr36MrBK3NordlU5zxM4FDLw2mSQ-vxD39krEzRpR6qwpn3yU3Fg4XqxfcEOeEjZxLN3nrfWsNb1E6zTTN391YqD1wHbEINSCFA0MBqJrKqA7jf7JwAK4PTtPmY1I31ZKzWEzvzxn77RRjcmhqttuxG54vBM745kAwBbouZYZvIMa6YHDhGm83dX8-wqkTJDVoOw_A_gpZ5SLzNGT44fhRnozE270ggtu6SmxEMXJP0Ctmqk6-hh0gWo-JT199-sgANo41i6TPcGOmun-UhXZBHJ0X2R0CTqXUnFtbeEvYwu5j3mw1rS0R3LAUmj48xmJNfneevC5d8Za3ikkntFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOSFedvnUGbWcNVaoNq7FBsTrYxaJrCcT7B-nBHm0VHsygaXkTeg14LuUSsmTnwbXbnZLmVM_V9xF9GtDQ1flM4qvFMcRiu48SPVTqriiPk634jeuRjsnT2JWi5rcGPXzOSKBZd0qfvWqnQgXVxFqQV6zrQ44wj3jMEwXi-MnxW45uE8LseCBXB4fdslS-U6jJYYja0mqmELTkVnuJWLL87Myx7bt9p-fsY39DRcc0_JHq_YaU16I8v1PzZ3pBosoQk4qAUIc98FkKGQ-aL13oL6m7VQ8GtihWEdoAxcXCnXOcDH-n51QjUHRscFO_l3jN12HhjMxQqvnljdUVlPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQx2kt2v-VWeUVSxrYbeORT04v_WkhNxrqLlk4lrDXE_Xw2S-avFC47wnO3148zQ2-MVx5dnPNFfoQNzvdl7UuALhAeEIamubFr_C9ay6AkvhZ-21rDhrvveNjgFt5Ucev_cBG598SI_xdbNBGdnn0lTNwkAJUUgg8cxu6IOm3ohGLvHRORo806b3xVKVhCoSgM-AoDTgCtqYvLDcYILR8RwIlOAT7yHCM1BCt6k0Bsv30EidT_NHfe0K1PRfPjKX10S0c-1WMeeIOwgxj0ZjemQYOENvppURc8XaA1eyqT4MIH6kIYRN0661NFyi-_ve6_0ngHnjhelRwzTxPYCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMjNHGSw_JDAPQWroLTfPFdD_IqudF_SRqJV5dLC8Xc9xfpv-rd5rRq-G-xbnlcXjgtWtSqxJ4MnlnN_aj4wwbkrVdVYGlTy3KrNa3tmKmDOq7NscE7wIGCfXc4K1sgykGtUcPdZw1Dx_lvLILc8C1CakLi3d3qTlCYkFUS9a__BWdxirG5AmSGw7RnOB4uka7gu3NVLYU9fkIZaiBgtr2vqLegtaiUusYoTZWuCYK-p4HK_9uGgbCfDtz2x-Ns2j_Ma4lbcLl3tffJPK3ZHa-cqSjNyMhredqkwOc3dgxF9lyhM0_e84xNQ18I92_ZwyGGOXOxOwt8FeWWiD9fzuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK4WdYitUCKZARuzjiOhw4QuxdiliYDMtvzLzrgh1gm-t0OaB_d42JB5IVSgWewqpxFFwfDmyus65s8ueQ9l3d-tzu-kwR0ke4PVsDhL8VTEcyyRrCSWPAgown1pP7vlipoqmyaWd-Y-KXVylBfPtqBPjMsWPgVgyTg13IxjHw5UV8jps_jS5x-QK1vt_RPD7W9mx3WSgkEReKxI0AFXoBtCD4JgMvcMlu8ANEO3B6D6RAq92vEBoQTQlHHBTF9Z17EuMRXOFrq2eMv7e_zAOAlono0TV-jCRfwZdFf4g8rTvz9P7rncj8Rw32LXgJozdU4nzucwcUzaTk-Pj4X9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFVesvzxr2txN2hkhpXStY5s1KqMozCV-k1iPwOn2NnOSdhocbQehD-EVDH1ZghTbK8Lc05t61eM5_gsO0rzUzzdtaXTvrCCjTN-D1Vn7hZBAf61hG_S1zoUsADyGjWgXHmtcXVceFIkrB4zxG438EGli-VwAsXl8mr5sN7TQ8RmxiZaGDBf6UTJxLrAWd5SPnrUQmTDyyn2zK24HBbd4tYdyDajnDk20PS-_gjNkR5-lJEykVvR-hao0Xve7MB0vpahd3_tg59oPuMRdWLqtb8xvFcVlgMZU8mwDCAi2gQdbJKSYs-yW8IWXI1-kMQt0fR_CmSL6VWEQFyvN5zB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuwWFu24lo_Tm8eguX9KMZzoBLNHZB-BM2wN1L7vbmm3ov-D91vjuzIs9Hv04Kb3xU7BnC4nphwL0pRaRjlIcJhDN6KWa91JWhruSgZOkx94-0UR-86ubfI4RlAMwKyWJ0v80oJBelL8Vt1paWLCTsXVPrHu6aK7ZIZg7s12MDL3O9Js0jWGPaHyA0jHAujGzGMDvLMmTIoZWSygOruL6PEU8xPM7Xm0Ifa4_ShA5p3G8R1bQH9XBqh-y8UIi1qsD9Kwc_KABVCtoBOVYgIJr2JOIP9-3f9x7HAONR6NfOHyG_hb_51EuaBsoyGE1-kCoyhvKWOzEnG2M_j9-ARduA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=qPnBc2oi3MQyY4IYeyy4q8e-6TglLzOjDPNWCwA_lv2FTzmWCHQtWaoKpyuWeFf2wwXwU9zyqxvKFfI6Zh3_vlWwMk_O9eV14t13RL04jtcfHHT0wmYoGNyeNJFPnMOV5ydGQapa4_YQD6r69Tnx5YpWTaDxN06LBJEL5rzFjAkZLeAEsSOl4Uukaz6BymnSaYpe1d4WAFTX16Fu6Ipg_Od8mjUIEc8llFMNUYxHPpunMOzJFu5f0s3ZVRGnQH7uqXSTVPJXF9JiCLHZJ803KBwLGWeUZpqw6BX_L4Ro0nZqEiIutsrI_aAy06LSmIqlVxuWzTJPJt0Y6iUheFoDxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=qPnBc2oi3MQyY4IYeyy4q8e-6TglLzOjDPNWCwA_lv2FTzmWCHQtWaoKpyuWeFf2wwXwU9zyqxvKFfI6Zh3_vlWwMk_O9eV14t13RL04jtcfHHT0wmYoGNyeNJFPnMOV5ydGQapa4_YQD6r69Tnx5YpWTaDxN06LBJEL5rzFjAkZLeAEsSOl4Uukaz6BymnSaYpe1d4WAFTX16Fu6Ipg_Od8mjUIEc8llFMNUYxHPpunMOzJFu5f0s3ZVRGnQH7uqXSTVPJXF9JiCLHZJ803KBwLGWeUZpqw6BX_L4Ro0nZqEiIutsrI_aAy06LSmIqlVxuWzTJPJt0Y6iUheFoDxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HM9Di441Y_gNepyzp3ux6N_zlhOnoux4GEQimhlZuhBBYA0T2hMPTjD-ML5M6KkcQYg4zgXFs-2WCUI0gBnL36V7JcCQ3F_SRKvpQi2sWa28FjbTa4XDJhioatyI5qMnRORbRLV2ktPAIBWYPfHr3mVSF6cL6d3CDlXD2puDxdyt-wulRrhACXFPnWfZTdiroB1O-ujbpvT7tGHbOj-wTXUVWktiZGo-WdSnSwvb8pkPqKFNXEoMawIuqL-NQf1kHsnZSGxEPT3b7kYue_EPESwcl0Zc0WPrVF5QILVt6ItK0KTpwBnI5A6VNzy8NhK0j32a5T1l9Xt7tUmhJ7D4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=F_ypB8nRcbRwI6JKXLaTL5eH6zXIdan6RS9Y7Z6iaJWrmn_L1HW5qUkzyftyzMOwYcGMJ6StmE-62l3OgQTHOOqG-MIstDAwWyd_wJZX-DJHwB28azCUJW-n0e9iUWyKtpQVfYU_9Jcz2FHY9uY-qLrNvc9RiQbd6ztrTHUezIkQAiOyhJdfwrXv4gg65v0LCEiKKM-EOVYnD4Lte_9Y4i_r3MR-xctKJjQPSR8mnvV2IQMYVQG8PgYfwQKgLkci1eSyZkawklvScwHzqKPcXfnpG0WIxrZWyhOlcwr3POJgpLyrqwt0JcB4km5GnmT4tMztgdS-TpgXe3MpyxIxmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=F_ypB8nRcbRwI6JKXLaTL5eH6zXIdan6RS9Y7Z6iaJWrmn_L1HW5qUkzyftyzMOwYcGMJ6StmE-62l3OgQTHOOqG-MIstDAwWyd_wJZX-DJHwB28azCUJW-n0e9iUWyKtpQVfYU_9Jcz2FHY9uY-qLrNvc9RiQbd6ztrTHUezIkQAiOyhJdfwrXv4gg65v0LCEiKKM-EOVYnD4Lte_9Y4i_r3MR-xctKJjQPSR8mnvV2IQMYVQG8PgYfwQKgLkci1eSyZkawklvScwHzqKPcXfnpG0WIxrZWyhOlcwr3POJgpLyrqwt0JcB4km5GnmT4tMztgdS-TpgXe3MpyxIxmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ0WT3Ja9j0JXdv-uH61M7H4TUoTB9-Q1ollBQhnVtMKvQ9a2z7XzXgknsP6xmt09WlUqFGwM4lKbR9nxH7ZLMcpBvmVaGrqDXIodGludF6yNsOo4gVIcTdgzKdBtjMNTe5Xjd1DKDboxcqjsRS4PFb9Z3G9ON7frlZ7G2-1TR8FZeplNKf5nJgUA8gEZTr1zxqvUliZLEPdZ-iwin5c1WPmiXaC2ApWEWKdeBKE7H_Kuh43TMQi4bVYYt9J3hKgqI_2ZFbLiKUBCVYTeSRSTY3fLOK58NTQ3BDwpvKqjid3qhYmdXpl186sqxOSbF_p0pnOuoaCGQlFYsAYZqapPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGKZR3Su5rg6iNl5OkzqGcJP7t59yoBkaezopj3tFHe_tPaJWlITDbHlQxivRfVUi2qQx9TRRcTjeGbrCb63nrxiW9cTld-3yX0oaZQZt47P0jHDLg-5dILtJsS8w45g2WYIkVLR7F9OVeklRUR-I71Ng3GsPLZltcqHsEhTqOH5xGU_Lm5WlF38Bn7vskamGnc7yNfB5-ikd8lWyLKP7LAD8l5toJQFUWdwP2pUsjTBJdcS0GvWrTrA99dt2U_oM4hqNsSQYJpzjU5cEDRiwh71ZZGiaQ4PoSjZ7Kp5GQo8uS-kkYhFWJ9iqGaKU5jo816HsJ8ofVxxffb90qhVOlJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGKZR3Su5rg6iNl5OkzqGcJP7t59yoBkaezopj3tFHe_tPaJWlITDbHlQxivRfVUi2qQx9TRRcTjeGbrCb63nrxiW9cTld-3yX0oaZQZt47P0jHDLg-5dILtJsS8w45g2WYIkVLR7F9OVeklRUR-I71Ng3GsPLZltcqHsEhTqOH5xGU_Lm5WlF38Bn7vskamGnc7yNfB5-ikd8lWyLKP7LAD8l5toJQFUWdwP2pUsjTBJdcS0GvWrTrA99dt2U_oM4hqNsSQYJpzjU5cEDRiwh71ZZGiaQ4PoSjZ7Kp5GQo8uS-kkYhFWJ9iqGaKU5jo816HsJ8ofVxxffb90qhVOlJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=srE-M4a7fRBoZEI6Nz1pADdmQnqlhj4qaF-aScbmZY1C8Ib88Qd1KVI1YSBGIpKRy4Av4iueDMjUaUw3-xFvU4wVbIglEN_jq0VPvZnr5fWGFl23aupb9jr5qIOOfAyBgqBpne8X4l3OGk4ARDcSxN0n5DoBPMEpXCqRAu6lQySttMO_MfZgkKIVQUaNf7-5hnTrSKqcKb1UMvIy5W5j4rA6_B_qkN5cCyiYrPxsPtLcqd0mFGJkf6ZU4hbSyno8_BXVaRnfuNuCO2KJG6HUeO1uR9GIo64Gom_QECQhXfXutWNX07sJUoh5D-YMvSTmGlXQF9MsF1ubn4iCXqXFnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=srE-M4a7fRBoZEI6Nz1pADdmQnqlhj4qaF-aScbmZY1C8Ib88Qd1KVI1YSBGIpKRy4Av4iueDMjUaUw3-xFvU4wVbIglEN_jq0VPvZnr5fWGFl23aupb9jr5qIOOfAyBgqBpne8X4l3OGk4ARDcSxN0n5DoBPMEpXCqRAu6lQySttMO_MfZgkKIVQUaNf7-5hnTrSKqcKb1UMvIy5W5j4rA6_B_qkN5cCyiYrPxsPtLcqd0mFGJkf6ZU4hbSyno8_BXVaRnfuNuCO2KJG6HUeO1uR9GIo64Gom_QECQhXfXutWNX07sJUoh5D-YMvSTmGlXQF9MsF1ubn4iCXqXFnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BSAUr_kXDxTigTDFQtkLxmZPXZPBEq481UYa_xcA9NnRdM2Myy3KSwmzppfuAr4KG55CWJ5dvPbUyrCpXH53l9zGcyI01KhQcoqt5jy_trrbjh3-Dkmvbs2FjrhIOVFBA6tonmfrZKDYVQFO6OroVxG3hZVKKk7RGIhlp1v0MdPvaVMctNnn1CMTamwMER_4pWUIQqGa0Cr1rbMtQvGyGWuXdu8Uxx1O3U3bQgG3k_96Vu26VNGqKt-l8EgMSOSLBaghP-5Tfyni2VxoS2q-cuP81Ljnf1H0MLUXmT6sLGsMMU8Y4YNZEPJtwu54yK95ZqP73zofSUP52r5QXL7mriE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BSAUr_kXDxTigTDFQtkLxmZPXZPBEq481UYa_xcA9NnRdM2Myy3KSwmzppfuAr4KG55CWJ5dvPbUyrCpXH53l9zGcyI01KhQcoqt5jy_trrbjh3-Dkmvbs2FjrhIOVFBA6tonmfrZKDYVQFO6OroVxG3hZVKKk7RGIhlp1v0MdPvaVMctNnn1CMTamwMER_4pWUIQqGa0Cr1rbMtQvGyGWuXdu8Uxx1O3U3bQgG3k_96Vu26VNGqKt-l8EgMSOSLBaghP-5Tfyni2VxoS2q-cuP81Ljnf1H0MLUXmT6sLGsMMU8Y4YNZEPJtwu54yK95ZqP73zofSUP52r5QXL7mriE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEtvZT3LmUzA9zL6cazJ7EtNXjkWb-9CeWmGRzuESs8WRbHBbMPNX3pohYPnLBIs3z7qUaaz93BT9AqTOfhe0PDASJA6zo8j2XCOBFScXzJ6n1byrnrRG0U4ihhyxduF-6DnbLj3IwpWRci0iqkshNPTkk5ihg9uaAkt3xvcv-BIQq6RqgOlH25Rp7IlzgN2CdKiIqVWTABFT4j-CQ7Xo_HBKZT3MNaXq25BpO9V-uvZpq0yZqt4eg0K1wfaqXG8vdxzIN6wfz7lo_2Jc1LvRyZQWduItSWJYGY_Fm9DmLgD7Q5k1xLbVQ6mRwKzVGmzKfTRhkZhXgvqB2jaefcniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbFVUHvVqlrzQoArlTPDGJ72IiCSnCGqUI2gCaZVAO57uUon2VidQiG0QYIpStuc9Z6tqeRVMMJn4evX7ceQ-syThQqNez-xLUynkUriKWVVVMzynxUDZVePuV8inOnCDLyAD9zxg55UJJpwBFY7zL5TO5yMnQzxABPLuFtdX58eeaUlsfhrnzOxfuRIv6C_PoIcUDcJMA84btbEfI7yNJQPu1U1ZIzgjO3du2vHNDiOyl8XeOhddoSxaUAlo7pMbtk316G5kS902TT4G3q6cJMaNj7aHNMzyZ82Sgp0f-V3MFVqtSVu990DIie6Qp4dcST6KRC4q-m75gil8GNQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlhudWi2PEu-55AURuLF2GwZTysB-QMKOsfHmxXq2CntPHyQpkIZ6wE0TwIPkQhphwQycZJa0Ip3cNhIyZsJfvtMgtpBK7jriwtGnsXepG7l75PWFX7ygT8iWrHR6Tvg6PvQw4KeBqHyfaHUpsANz6DkMOn4OuASNkbaPgsxDYwGGCqLcB51wFCwL-_pfXnPesuprrUbobSTuZ116tdT-3cjEsBvZQYySsvwuHDMiGjj0aZb62SB1enGZUdgUdkedq-ssG_E4UKahmr3YBqKBUe1wqnTMS_Hg8qgzy-0wTMkLOFsV0jSwMxjaDj1sVa-UYY9wyE91dq-UO6LWRujPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
