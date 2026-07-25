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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 11:01:25</div>
<hr>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFxZdgIdZ3nhqzQyv9ZjtssKeSkYorsYemlYgybOQ1wlfiMi-pupIOsFsRVx5wKAv2hOghHdTw1G-IhxY-7MgWA4sr3T5_ejKWxSOndGG7N9VdGrOJub-Nrfsclhy_a6FDZMaNtPvvCF2ybGwkc1SbNrKUtN4PB_8hJW4ZjDgf_9la-DEGAyopdPNR4YA4rGrkdPG8SH-GU1FJBdC0Vk_qOv6PYcqqeuTPutoQ6dopuqMPx4pZlzwwJwseau0V-NN9bzh8yZuZ8PoePRANyv0-T61lBjyHVhSD90ROeN6-uHQ6T51TtNM9_Fxgd4TrQlGrPk3zjJMfgc7RT085YJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFX74a6nsStoFi_KitK4iAhz0dtkBtd2r4JhvNDxvW7yt81r7YPOTVMT2ABqCiTIxEWUhDdt2V1sbTtTx4ibwP7jl29ujqeo3JUozzbXM27h3S6lSW8NB9alT8KY9f1K6V25OIkitHbYn58j07rQqfcIHWFmeFF2kkz3eC_mUnIEYhMa587qV6dOEGmhavkVUuvzEOO4n9s1IisZZWccxBhs7hu2PCxQtTSv6coBbLX0JsMXJ4Vrxa-KB-AqpWc71x5k_X--BSVRNQvq3H3-gfFBNZBGBVVssPEdelyVxJki9RRXJbddR6Qz1KVEXTYXiRcFdRKKj5TcDO3BNhqCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqWa70UuXvYgm82q4WeB5gldwDWB5ClQHPmwXBrE9yLirAFDO8IRtphWIuQnI-DJlGJgio9FCHztlSkzIGlwzwDFYTgCTOZktFtBnPJhUSyN0bQXatKmqFJIZ7cHOhW7MJAQBkR86PBrhtq2H2d0HtfqehXRFmrudeDVfLoX0x0Lh_C5m5ACEMTa4Pligf8NTyC6iwKGWkRiBCOMNI1J6wDvvZ7EedzqBR4dpQpZr5ks6Gja87kAQYgyroQJ2NWD2HEcsehKynWin5It9wU7gW9jJRipjlAhzPR1nx7H0gSFvbXFB-FkxpIFXStH49YPNAKP-AbUWCovJ1ScAqaseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbcaFRE6JbgCs4AeEp1IkKA1x3gRIXfuDlrrW_3-lDB1swXEAtNql7hTuiYNguKK3asYnyFfgoD_uJIIMwXLjyvLnpEEG5BM0NTvH5kOemS8eZDUcWs0Gws64SCa8C1cqq8Dt_vCQ2nU2DhjXopRRpaarnw3jUy_byDWm1JSYtj6z9hvW6OAom3UqfMzkFnPfkCxEKCX7MkE1Ua4w3rUA4AhF1Qua8eR6PofXRxBtUsSkEH4Yd3CVzrLfXT8iSUUFnSBg3UxL2aKSgh6b5tCrTpEam4OI8_uS_PAD1ieM8ocJTuCjCCK9NNhGYmLWRympV9z9gtVY5UGlGD5foJQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=jQVwvBt-Gg36-ImaRhFkJG19AoF5GId86iTJQicWMttR4Lo4fPfDyg-qG6YR6hwF3-WorPCmpbP5tjxsohTRe5SdXWu4M0o4f-Q89fOvPZAHU_BW8qspxMbO3bJk-mFfvhiKDfvwQms5Gd5thxNmwElZ-W8GVJuhbBnyBUhN-eUHnZbUIMP62Rn5rBgxf8wkNaiO59Q0eecC_EM_a2gfbOkopzNv-MSnspIICWKlWIVuLZcjBbKVKjVobUfD3gDgPgennwFPUpWBmtMD1UBLjaapDW_OItAZj_k3-AmH2w83mnhciuon9uttn1Z96Le7Rw8KafJouVPkQldo-mcR-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=jQVwvBt-Gg36-ImaRhFkJG19AoF5GId86iTJQicWMttR4Lo4fPfDyg-qG6YR6hwF3-WorPCmpbP5tjxsohTRe5SdXWu4M0o4f-Q89fOvPZAHU_BW8qspxMbO3bJk-mFfvhiKDfvwQms5Gd5thxNmwElZ-W8GVJuhbBnyBUhN-eUHnZbUIMP62Rn5rBgxf8wkNaiO59Q0eecC_EM_a2gfbOkopzNv-MSnspIICWKlWIVuLZcjBbKVKjVobUfD3gDgPgennwFPUpWBmtMD1UBLjaapDW_OItAZj_k3-AmH2w83mnhciuon9uttn1Z96Le7Rw8KafJouVPkQldo-mcR-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzWj-RHZcQYNuZhc6T5HSsYm9HMfRp9bPL51m_SxFRKW2BYnEnWpZ37TpPxZ5JsRBtZR7egTrulWoCFlTZlLN1k8L5hXHU5ClfTavw5T9kjaEekOYOGwVzyS22GneLpDR5zoqXxqY1LBC_DaD_6QRKssMlqfN3byCqf_jJRJgM7rd34UunS8MiY6Ql_PYWWuspShadOJLwFLFbwBRl1ovm_h_im-qcvpcg_yIXnd2zxwefRIIJfLjzcj3x2d6IhRIBCPXE0yjOtonxshRabg06s5mMFAUwztxoqn1rLuSwyO6cN4hLq4bMG1t1rna3cXFjOj5cQajqvCx97xQaGMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn9dKMR5fvO-ZWasFVV_OK6igM-n0w6wX1OpSzI48_9QIoIen65pjxBjJiihTePxpwbPVveeVwqyzIclJCOUX19f0pfVQrGJHKFk06NJmFAushBiClWeu671ijcb71tHvXBQ6jaQLNjMj0fDr1e0BL8pLnZAkpJqCQzSMkAyTcnoDFD2tlvRx61mpk2g3oGl6m9q9M9d5GP6Tppno5BujExI3MJjjqpXhasILhUE_fwtg08Z28UNSM6i7p2Etp8fmI2MFt_ExcRu_hl2GHUt4No43rRpWPZKVzxJFTKBsbIF_RdTzSNdI_DYZb1WDSUFItlLmUfi177tELCd-l7ElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_hUx6gbujC3qprdCt_6yC_b_CSMG6P-1sFP4dQpKW1CBMD5UtFXrQvNYkIg3MaHL9_pfH6lyMvxH0bVbgf3ajT6Nnz4tEwxeMaimbWGiw6NEoaqMJTG2ongqb1lFDn2PwUu8X3G7NKJDBHCSxUnCdiFCgIZuvGQKtPvWQJsTvhOdDL08GL4lRtnPP9x50JaheMvmkr4vJhsO5KBqWtbZf0MVoRB429qaoOKVHm_zKn0D6Avy_wa6-rCzMs9bUK5Z7XbA_b5CWvZ_ybXEYc1avItcosduJkz1eTk6f7Xaq0dw7szeOmaqSIlVqCrwW0J2Qt5BbElHSHnmR6nVXjSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpDfhuwUVA7D_vukw--punel5VYWFSWuPlGiBExSYEj--tTFv4eUzPBUX0LQiX_fcPh8G6V9z2nEac9WJzaC-FmE6hFPbLv43Yiz958Qjro4DN7VGFAjTLJh_m8JyODFYYmxAs7Ndio3phyQMKwfIaVFo0lPOpakaRQHWbniwzOfmhex0vrgFyLGvu78C3MAiXupDtA3e6yVXnIQBemQInE5mcqzH3YzNUVZD_CDhL8rHsNCw5YvKr_1CHbf5ul3PDzMktrqT8yKnXB1auS38vTfuLTb8DhGMTPAl9U3pCZCAGfh6NTHF8O5OxL_cAKFcZvZo6m3fU6jmjZQZDl0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfKoV0gTyaCZcUulO6eoMt__181eK1aDzHb7BK9cGQS99Dg907jlT9LXBT2HG0ku32WOusIa_Pj6dOzPabVq0SfCCFquY8ER9KrYh324K6YBX5lYyOKj1HW1lWw_7FEn0AMO4JDzgK7cl5GEUfqMbOGfeVT950G2Psl81WBmNQKy46XVCzBREiCoZfDQ6MmCBPATf_YeGfNcCo6ZvsTK47L9NQG_udQkI37tJ58L1Dk1963XZFgpe1B43bixT7i3WLbQ3efeJBeJlNkR4GhgNJoudo35qIxr7QOSJTo3tdK_D9i6QF-1ZxU09Fig_NlegPDytC2Gz2ULTFlUicMwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwXa9iUMlN-q7hM1IcNe1la2OzoB_pN0HVPwrukkvOm0_0da7dftCGn21pxlXsgVGfBkA2AGQQOaIQktLt9whYODABq66kzCNepfaaiblQ_rU2UceWsbfFV32XJMN9eXQ6145EW-zCsjA3GZDgxgDiouC61ZO0QkEz1rpOWEXXbNhUF3n3wTG0lNimh48Je93aOyQKkwe61h4YM9REblDLvxFmvbZbpWG24IsGnVAsIvxsP77bG4HdBTvHqZzaDDR0ksenxBf32XkbCKSFOzbW1aim4BH-NSWcd6E23LcjhsPd8Sq2FdPxtjZMPoo5Ij2YCXL_jl0hsH01bA9zcBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVISdUPgUwdx_eekRtNcjUJ9jQnnkLoaBE9uJtWXEfsHZ-w2SKNRbHIv5e4aA95PZOQV6qR3r0Oz-NrzLcHdf369SyRNy92XrAngYm6S0bVDDpDfhcny_u9Y0rREK5PHJ9UCpDM853B1EmrWaUPirBq6ogkUWvGutTWHA79zJ9DTPsIC2WY988fKysnjX2gK_WOY22gBZtBqzIIcoQeiNf18MjrkqyxY3msOIIZIiuEDCEDQ1qmtkUH0qXxiAacQx0_QvYYFev-wJk7BBICU2fW45f2lwZWD1ug54ZzbNTH1KggEYhDWc6au-Vaw0vajBKMLj0pFwOdF6agfaGH00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=MgEX6_bH5RzNPVZUIR5vGtv1Irvd7tsHgkrdi4XkGh9nAdst0JHm5Ri5WhIfjVHBxAoKbFRPlUdaNQgVxftsrZH0JbeH8fu7i84cYVc5pivJDSqUWwMPpweLCa-IRpyMa_Rrb2ThnGyC2BF-iFqHiUfM2GOvbCGzmtVXO7WaFvAO6QkqXrs1DRB-3RhH421N0MPsm2wOwo-kiiztyx1Z1FTZnOSHl8m-N46N_SglgKOSli87FxCuPdWkx3-WD26rSz2BBzv_Xerqe4bM-Aa4OgKuGmLu2he1E9QHIWOlflPfP_mjBJWjqmMIvjKGfQP9y1x9bXuaaBm0ckuhHOE-RXXahr-pVM2D-bspjCIhmc7DRXgtrFej-nlRmoUpudmNjbkJ973UvQw5qpV_fVsic92IV3JPfB70e3afvT6zKTi-nIPUpPOpP65JDEq0-MUc8KWEBANmDYSm6JETaxzxhjOEHP87Ayvwl_WsAEeMjGF6iB-nFsixOMLbfxnIBmv5wYxoQ9im28cfhuSLr_Jj4BquaPzsLX__Hc0f86R4H0_Yk3a0ExlIBxOrmZaFuxg2xobIMp3QGg8VIXeiPaZHzs28Z3h_w2QBCcZwIzaSQPZfBduaSxYuv26yWuvB6Nz4ns5o9ilVqKIyV8sD4Jp2WGbJXiaUMEVOrbtpnQX0Rno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=MgEX6_bH5RzNPVZUIR5vGtv1Irvd7tsHgkrdi4XkGh9nAdst0JHm5Ri5WhIfjVHBxAoKbFRPlUdaNQgVxftsrZH0JbeH8fu7i84cYVc5pivJDSqUWwMPpweLCa-IRpyMa_Rrb2ThnGyC2BF-iFqHiUfM2GOvbCGzmtVXO7WaFvAO6QkqXrs1DRB-3RhH421N0MPsm2wOwo-kiiztyx1Z1FTZnOSHl8m-N46N_SglgKOSli87FxCuPdWkx3-WD26rSz2BBzv_Xerqe4bM-Aa4OgKuGmLu2he1E9QHIWOlflPfP_mjBJWjqmMIvjKGfQP9y1x9bXuaaBm0ckuhHOE-RXXahr-pVM2D-bspjCIhmc7DRXgtrFej-nlRmoUpudmNjbkJ973UvQw5qpV_fVsic92IV3JPfB70e3afvT6zKTi-nIPUpPOpP65JDEq0-MUc8KWEBANmDYSm6JETaxzxhjOEHP87Ayvwl_WsAEeMjGF6iB-nFsixOMLbfxnIBmv5wYxoQ9im28cfhuSLr_Jj4BquaPzsLX__Hc0f86R4H0_Yk3a0ExlIBxOrmZaFuxg2xobIMp3QGg8VIXeiPaZHzs28Z3h_w2QBCcZwIzaSQPZfBduaSxYuv26yWuvB6Nz4ns5o9ilVqKIyV8sD4Jp2WGbJXiaUMEVOrbtpnQX0Rno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt8RrGXrsRfw6f7nJ5qN9bWqYDBTz3z7BWt-3KGUu-ySpOsT7pSVXPz0KxRdEn0upAzptyZpDt2TYyueb7jE7b-r-Z7RJWO1lgFmuEXc3EAEsKfudpLPiXGoixidYQvEIxef7R1A8rbcmuhm8XWraKercWTAtRpQNuoN-qWbnucmFtrAoZ3jw_0_xciVo5NNjXaA59nh0jKu03WGg9N7hibigKcRvJOlVXD_nFWOf0Xf2mLm1REwxxvCJFwuLBBylD-IZk_azqs2DzaF_mbcoxdj0h71ROn3rUmJuSzN9ehMZrXd2gixz5qj8ha1ZmOkwtUamTAKzmSApG-8zv_ezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrubPnnOpmlpFoOvz726AwgaP6tBRqT8LcnuFLueMf5iLTTj7cAnqGl4LD6GNxRpLK7bp65ilMIPdsVFny2nL6Ci6fweTYfEVfMGm4Z8TYEOfNCLK8qXirLMNlbfws3m6ROxGIpbDFjCpy7gjRdKN-8R6zJLsNwe_Dqac8QBfr88owGaTuVjLQQYzYqsLiREie5fTXJv2PT29EzEear20YiYh1hMuPQxVWwA4YlR0At5w4_Z2E5X1Y3T8Wcr1KNQJPuzZJe8JH_gdq93ydQ03toUm0k9nJRyYkq1hWXfMIarA5BjfWYZh1-K7Varb-ELZn1A4EYahJjatuSCbF59hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2WefPb2phj4cmgZCTIaWuLTbNrADB4JvCwWCqpINSTojTaE0erCFjnM5kqdJ6BtDT79808hCkTDMZKVquREc7V-GWLqeBde1viBma2ZCcxSkHwraXPASjkbULQO4dLos1XYFbW2eR2yhhRzxmS1pD5M-npCprehE_nI__jku8l3V6_7GbnAykfInFuEVwUiExVJlJrR__kLii1OR2H4DGecn4Ot8Pfp9wDp_LNynF8Kmir-4oBPpgC1d7vue-p_aHVkKSD2Ex1GX5IkDX0tDp34Vcv-nEXj7fXL7lquTUIZfY4Gf013xZaS6I01kk2I0mEERkJiH7Hl_z4XvLkRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=QI1nAQT6G1Bqj_tUK_g4xSij3S6mwvOFLjVIIK9_pid_0T8pfvUGKu5wE7G2NWqK4B6PVQYn0rvfSs2c3KDNdyV8G0qW_kavdxLFDAolWNrMc7unzEndGwJ-PVXLq_wx5-rjmGU5e95QFFzhV8BREmcXtvMMVX33Cs3Qwb7yB2CLGDc-WBMdz_yZxEtpGuaTDaTQ30pqwZGY68ny7b1q3tT4KoNxr1E3PGa9re5rL34AQOcn07ox6gl19_GtMjJvbIZ90uIJ2U2wU3sV2omvp2X3zW2Wxx80e_sWKGmi52cEPGq4yrzyN1iZHsmUk0uALhRuo8JRoqGC8b6taehXQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=QI1nAQT6G1Bqj_tUK_g4xSij3S6mwvOFLjVIIK9_pid_0T8pfvUGKu5wE7G2NWqK4B6PVQYn0rvfSs2c3KDNdyV8G0qW_kavdxLFDAolWNrMc7unzEndGwJ-PVXLq_wx5-rjmGU5e95QFFzhV8BREmcXtvMMVX33Cs3Qwb7yB2CLGDc-WBMdz_yZxEtpGuaTDaTQ30pqwZGY68ny7b1q3tT4KoNxr1E3PGa9re5rL34AQOcn07ox6gl19_GtMjJvbIZ90uIJ2U2wU3sV2omvp2X3zW2Wxx80e_sWKGmi52cEPGq4yrzyN1iZHsmUk0uALhRuo8JRoqGC8b6taehXQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw1WPk6o297T5LMaoi_v_ce0IwJQa4zfwuXmnfeJK1FqGqUAjZcXFRVkhsLnG4c8XdPv6hbPVJAPoAAKQ3wVViVUSbOn3S9meetKwC1QxMG4_N10vt0DwNwbnf25XQYeAgdSxx1I3tGpXR4vCPd8SaeqODb7XNTi8UeR3STGpIdT8ypFpdJvPwliBGYTn_sGzY3Q0aTnvGqBRRqfEkDF7OVjPS42QGcCjnlohX14lB6yKOKjg5X4LE_8MoGC6vdPp8rS2broCgH9kdtmF-pjLFrH4PskFEXNZ2dYSoJXinVzWNHcT_IaiRVBsv56LgH0Z-NRuk9GGremNYUpxATdKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-VKxPTjO2figZ7HRhJ4MmHxb8pV1FOGgsoVzLwe9WdPzG7QMTl4AkHZp-bRM4UWSzb5HEi0IdhHfluedbSRrSgS8dQ_L4EvWMW01bUlbsWoKrShcLaUBohuhfB-oFoYFiFbOfYc24qNS8SgWHt6XBIY0d2QoojEgbxtXowSw7o0FIUo7sjQlBOELP_99w3My3F-w-dcX8WRI8ANxYGJI_3teoHDkpSlDy7_kSJiO3WqlXvEXrv_F9QYUKH80b_E0svBe4CWYog5YGHLEmlO06U_vtWwvfcbGRSlTcf1zUQLPyN0gYNF4vZI_7wuyGtHr-y8nRgKbGXxIjfD28FfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdLVxnQG-iQ-vBwlD4pgVksP5OmT_pxX9hZ2zcoXVR0k0XeoncXaFAJ55NsTR_6xqYQm9NfaSSFC-A1uqeKleApaqDYdwWt-vkjhxA6AKbyTKAv243xG2M4ow70-KUpqX0eneCB-Q8JCl0p-0BJmoEOUTi80UuT79LHN7jdgohD3-3zX39ZB-zamGOkoh7N7tmJNIgcCYOgDgxg6iinqdAkpAYreIZzAjv7axxSEOOfE-ltaHv4U5B0wfOjmh_wLcrVkIZ-q9MAqcJBUKbMZu9ZxAxzD-LiCXNr1Hv9WMF5diic4Mn9wPcbcxmzwv1C5Vlu7EwpT7DTBd2NjI9K2tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js2Kp8mqCXHQ-GetM1JfDE9jfBgyHbRc_NCFBg8lSYRieLVNBlSMzmZmj5q5ITX6hkT_TOZaBRQvEIvUN6O0NCIIdIBQl-y-69rLMf26t3Y1LfaaRT1-QcJhdPdFKGKoyvehAj_oVdU-QRrwXOP2NcHbBqat152b2_ZAeRiFfwXXHLBJkCm8GNv-sJZb2xYLD3i4J3wppJ9UTkBNgKomg-t2at4ANcbLhMLnITce39tsk6EtnlVdftolfWBHTK4LfxiKlvbeLFOTI0RJCwtc-gogzt_leU9Wjd6zYeMtcdWCMwOkRAf9hPjbfUYCemzhlrlGsh87E1TRqJaGTGrVOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Eu5PD9QqYGN0KTpV8sfLfyYDilfxdibBNwC_ZU6c953mPFzf6iYSEdaAz3S74qjS1X4GJazQtXxdmz-OnUgu6lxikURgM-VEaQVror6xVVFP5ozhPMdyhRcHs_qdQZaFqiCF-WePaeUjlgJ8vIhimb-UsRa0JEDPMmOkMopHnrGdurSgWTb43XLpFQpyKLp8NKvrFLMLSKBNGHSgkIBo-HJxYYdnLsGt13FvrYt8c0DZ0N6PA7Edf8Ig8qWKkRXp-8O6FJHwfWm25Ko18fljynzzR-pEOQdHXo4OETNrA2_ZaFTZvl-RfQD1z4DmmA1_cspG2Topn4XyIePk1Z4g2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Eu5PD9QqYGN0KTpV8sfLfyYDilfxdibBNwC_ZU6c953mPFzf6iYSEdaAz3S74qjS1X4GJazQtXxdmz-OnUgu6lxikURgM-VEaQVror6xVVFP5ozhPMdyhRcHs_qdQZaFqiCF-WePaeUjlgJ8vIhimb-UsRa0JEDPMmOkMopHnrGdurSgWTb43XLpFQpyKLp8NKvrFLMLSKBNGHSgkIBo-HJxYYdnLsGt13FvrYt8c0DZ0N6PA7Edf8Ig8qWKkRXp-8O6FJHwfWm25Ko18fljynzzR-pEOQdHXo4OETNrA2_ZaFTZvl-RfQD1z4DmmA1_cspG2Topn4XyIePk1Z4g2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=tnHp4Yzsgb_kAdzsWQwP06zdXQ_O4sTbeRHhEclMK1lYUitP8SXQLUrBqCyMKI7hCwEfhD_7K1ImIDi8MctZXoqS33h_EanXFnMgodoERNK2a1OsCa4POmbYL1BFPlFldvmvPML7efIL11HotapjxifUq_HQHlr3MR3H_QCYH_9OSHLgC85LElUGTZ1GXTrhq-rc75tdJTNKracKWio3T5B4kWHDwsl9Xocxs4gNJ6SCS6umFTxJIaIoyyaiFyiD7EvuObfRbT14cmRfjpIohMHUfrugc1-ej_88PNL-F1_Er55I6E8OX9aZ9S8ZzGmExzOw_xKkaNrCg3mxXvn47w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=tnHp4Yzsgb_kAdzsWQwP06zdXQ_O4sTbeRHhEclMK1lYUitP8SXQLUrBqCyMKI7hCwEfhD_7K1ImIDi8MctZXoqS33h_EanXFnMgodoERNK2a1OsCa4POmbYL1BFPlFldvmvPML7efIL11HotapjxifUq_HQHlr3MR3H_QCYH_9OSHLgC85LElUGTZ1GXTrhq-rc75tdJTNKracKWio3T5B4kWHDwsl9Xocxs4gNJ6SCS6umFTxJIaIoyyaiFyiD7EvuObfRbT14cmRfjpIohMHUfrugc1-ej_88PNL-F1_Er55I6E8OX9aZ9S8ZzGmExzOw_xKkaNrCg3mxXvn47w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbUJvZX67pDuJ2s1w-mQ4qxBDFp8Cg0UmETWt22OXuLnslxXh4kZYGPdYLfkwJsEDmCUaNs_xBo8312HFjJno1YH8UdZPT5rSAAKAhSuCRZUGx1XL8qqx75v8bX59YQ03xNa6GTnzNRv1qnl4A7PM7BK8CUZrdZKvn7a6r4dIzUQ5D9SxuXHM-gBARwX1MzOsy_wgrB1ERKCvKgn2nzeib9ykduBjSgFJPWM1xQJ1SEbOocXnFL52QerWTUsGB9nWxTL-SeP5ZgqPWXS82DHPYlWR-EsjmS7wsL600oU6R3_4lmfz8q6_rEl5UM_nxHHo-Aaks8-EJUgRXL8SDkqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=p7gIs9MuBLBc5M9u2KVk2I-dKfBOt3Lhf68Zz-_fB0hvNXUSdlOmAmMOvhtBZMdaIvXZCPI8edVPzG71RJSsYPTgMybSAs89fzOHATJPLTrllMHlBeYuPrXddrJTm4cdmVPnYdQQkoxVBHVGBr-fSdxxweJ1GRHO-zjyy8IDTwXKAmhCgDDYIoyoBj0FIpmwKKTF9X54YUWGcnTTpRgbMyQU_MRcs36QVFu-VGGX9PwfKpWLPrFVssqYxM2v-GV1lASIitQpIZz_niNkYH_v4Kad9dIEMOegXBiq-bcvkX2KgZbuPND-7F7ZOkT9d2tf3Bd3LQez91RtuX3H9nl_jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=p7gIs9MuBLBc5M9u2KVk2I-dKfBOt3Lhf68Zz-_fB0hvNXUSdlOmAmMOvhtBZMdaIvXZCPI8edVPzG71RJSsYPTgMybSAs89fzOHATJPLTrllMHlBeYuPrXddrJTm4cdmVPnYdQQkoxVBHVGBr-fSdxxweJ1GRHO-zjyy8IDTwXKAmhCgDDYIoyoBj0FIpmwKKTF9X54YUWGcnTTpRgbMyQU_MRcs36QVFu-VGGX9PwfKpWLPrFVssqYxM2v-GV1lASIitQpIZz_niNkYH_v4Kad9dIEMOegXBiq-bcvkX2KgZbuPND-7F7ZOkT9d2tf3Bd3LQez91RtuX3H9nl_jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=McMsfWc8kQ3elRJ_dRCUwhdsf4jdHSlWTrw22sh48pVDdP1VAqqpRHX0T8NU_EXWJ83KUdpTM6c3Ct1cG-11g1SLbP4c42Ft6r1MfFId-mImU6XJwHbQYQC4kIZk8dsIMnAEVciX7qFh9SWzgbYRrWyHttpZ8YTADTXvD-SHUzT8ra-bEJfqcGPGCOE7dzj7AOUYRGSPo53dOc3gvJmQZgR_Iv8aFuI2r_KatvE4GJtHjd9HFdOoQvUalzXX5vgWdt7cS7blq2GSmbB6fUKlW416IFg0XRUvDOJyUXty5rjcvogjlF4K2LVORLmFSY5wG9EbqzPoNeEcqglrxqlemg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=McMsfWc8kQ3elRJ_dRCUwhdsf4jdHSlWTrw22sh48pVDdP1VAqqpRHX0T8NU_EXWJ83KUdpTM6c3Ct1cG-11g1SLbP4c42Ft6r1MfFId-mImU6XJwHbQYQC4kIZk8dsIMnAEVciX7qFh9SWzgbYRrWyHttpZ8YTADTXvD-SHUzT8ra-bEJfqcGPGCOE7dzj7AOUYRGSPo53dOc3gvJmQZgR_Iv8aFuI2r_KatvE4GJtHjd9HFdOoQvUalzXX5vgWdt7cS7blq2GSmbB6fUKlW416IFg0XRUvDOJyUXty5rjcvogjlF4K2LVORLmFSY5wG9EbqzPoNeEcqglrxqlemg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=OMhRDHEWlkYu-m9wrNPK69nXbY6xzdlLB-t9V9dzl0BaU117v8t1ackxpiXxg14IkkZhX78FTronIxbp75jwoRu9xURyHCjZBcVPA1dRuG0ZcmWWZiAcUI34V_yXJzXJzP8AtEpbKJo_nXOAJb0eNpq_fy1lP9xh4U1LGJfhECVku_oiv_xSO1bKny2vTdNreYSV7yROXrTtq6aQf0cXB1Pg-EW2nj9YMpgKFg5hNFMVEkYjgAd3eSOtiELMM2f6DEaBZCzb_HwyhoGMJUnG7a-Rz4Qe6q9DAHKYonZBYNILY1Mxfo_MBe2OIAicoynpMOb7KIKNfqpsOc7m1tBGjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=OMhRDHEWlkYu-m9wrNPK69nXbY6xzdlLB-t9V9dzl0BaU117v8t1ackxpiXxg14IkkZhX78FTronIxbp75jwoRu9xURyHCjZBcVPA1dRuG0ZcmWWZiAcUI34V_yXJzXJzP8AtEpbKJo_nXOAJb0eNpq_fy1lP9xh4U1LGJfhECVku_oiv_xSO1bKny2vTdNreYSV7yROXrTtq6aQf0cXB1Pg-EW2nj9YMpgKFg5hNFMVEkYjgAd3eSOtiELMM2f6DEaBZCzb_HwyhoGMJUnG7a-Rz4Qe6q9DAHKYonZBYNILY1Mxfo_MBe2OIAicoynpMOb7KIKNfqpsOc7m1tBGjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Ps9aaMIrHDayJYUyixEqGBZWZG9DDmv3eXudw9KjDFv9n4J_U4OC8Dtaz2XQdyz3Abl3_vOgB7f6VvTNWWwVMmwhNoujsBZAjjUs7x5qxJ9Sx4OF-KQylFm_WPtoRque3inZqpoGJLqbb4ABd1GS-y6Eum_a4uZHzTeWaDrgZ7FZpqMdVPHF-m_usqktBHDLFcMQcB83v6enN0uJVviAwjsLOmzy-5hDRsDHJ9uol_xAvddDvgCTX9lGqCd9VLYpi9UqsJ2ZeooE02x79tUWOWZzM0Z42spt9B3S4BADo17PryrXSmVxlfV_kZy105jb0NQjbRUl865jRvgNO0pPzQTPpAlqCyl8C8SQy3Q_oRzj7pJJNHHXR5cMy6sz3mbnfN2RFS55wOltQQAWS6uDC75qhIp0y0QBg1Ahb0q4Ls9A3WVzPjLU8ToBK-WfdLGm46Telrf4KN6QTtMpxizN7Ds8IPgT4TLrcZI6Q-PXB2DKL7-9uoI_VudUcyrVYdognuSX-SXGEd8SWmO3I0n-6CNgYbIo8trhrEm8myIVZagZpKfKhas-HET9VIYxlXJXsavvfqA6DhY26QK7dDm3Kswi0oKV1BE6dJdxixJCassEk9G3uMER-yy_izFJVhl4YtfDeDDXdBq3CgCBwNlvAq6RuZQ9GLVl1eW08SqLNLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Ps9aaMIrHDayJYUyixEqGBZWZG9DDmv3eXudw9KjDFv9n4J_U4OC8Dtaz2XQdyz3Abl3_vOgB7f6VvTNWWwVMmwhNoujsBZAjjUs7x5qxJ9Sx4OF-KQylFm_WPtoRque3inZqpoGJLqbb4ABd1GS-y6Eum_a4uZHzTeWaDrgZ7FZpqMdVPHF-m_usqktBHDLFcMQcB83v6enN0uJVviAwjsLOmzy-5hDRsDHJ9uol_xAvddDvgCTX9lGqCd9VLYpi9UqsJ2ZeooE02x79tUWOWZzM0Z42spt9B3S4BADo17PryrXSmVxlfV_kZy105jb0NQjbRUl865jRvgNO0pPzQTPpAlqCyl8C8SQy3Q_oRzj7pJJNHHXR5cMy6sz3mbnfN2RFS55wOltQQAWS6uDC75qhIp0y0QBg1Ahb0q4Ls9A3WVzPjLU8ToBK-WfdLGm46Telrf4KN6QTtMpxizN7Ds8IPgT4TLrcZI6Q-PXB2DKL7-9uoI_VudUcyrVYdognuSX-SXGEd8SWmO3I0n-6CNgYbIo8trhrEm8myIVZagZpKfKhas-HET9VIYxlXJXsavvfqA6DhY26QK7dDm3Kswi0oKV1BE6dJdxixJCassEk9G3uMER-yy_izFJVhl4YtfDeDDXdBq3CgCBwNlvAq6RuZQ9GLVl1eW08SqLNLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Ap55-qE_2C6GE0ZfcmXdA09ithXiajx3ZoaLi2AdMVnrhUrdFjQJpicT6G-Gm28NX6GDrI1CW2lyS2gY3u1wGVQBGl1tPg50MRl4uAlPQq718fLaNsoK-W67vFRiaTSzCrbmLMWKBAO68CqaoO-CCNCPIAOMcA9YJSEmPRAcUINTWZZVH1g3ufycWBiEA8ptsEq3ylr43mTNhTDHWEKHd72JmpYWJ146HxbdxxMvNXamEhix0rx4DcB9rVUy_W92qB6AjIZ7mRcJCTh7MeTR1Oki_4dilcXTE6QhWMjLzvDITTgskxCinmQB9D_kZh8PgFpwls-Lqh3_PQWfURVFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Ap55-qE_2C6GE0ZfcmXdA09ithXiajx3ZoaLi2AdMVnrhUrdFjQJpicT6G-Gm28NX6GDrI1CW2lyS2gY3u1wGVQBGl1tPg50MRl4uAlPQq718fLaNsoK-W67vFRiaTSzCrbmLMWKBAO68CqaoO-CCNCPIAOMcA9YJSEmPRAcUINTWZZVH1g3ufycWBiEA8ptsEq3ylr43mTNhTDHWEKHd72JmpYWJ146HxbdxxMvNXamEhix0rx4DcB9rVUy_W92qB6AjIZ7mRcJCTh7MeTR1Oki_4dilcXTE6QhWMjLzvDITTgskxCinmQB9D_kZh8PgFpwls-Lqh3_PQWfURVFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=rfjhLJeCrnT6GaDo0z19otABmpI6EZrIrjqMUOSR6e7k5rAqWQnmNChq23FdOlsAMDNV-1CxAWnahNIQNvxeICIj473iJUpqRzd44KQm1SY_kIwBjhtXcTQLT88vwhAUmneKfuLOlTo__PPl0nkvlkal55rrObTF_m1Snp5sI5SfZfn6YRcmYljcNQLAui0jMwfGIjE2JfCwrizWs-oFAHehIOZoSD7Y7tTXP1SS8j69Xx802bJH9GDEmYSMc4VLXjr8oo5l9muO71vGnukW2_6uEN05dq_qDwDfq4RFRm_Ss_byGzXS0uxja8OfERCvkzDWXijZSDNjwsCbDlubLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=rfjhLJeCrnT6GaDo0z19otABmpI6EZrIrjqMUOSR6e7k5rAqWQnmNChq23FdOlsAMDNV-1CxAWnahNIQNvxeICIj473iJUpqRzd44KQm1SY_kIwBjhtXcTQLT88vwhAUmneKfuLOlTo__PPl0nkvlkal55rrObTF_m1Snp5sI5SfZfn6YRcmYljcNQLAui0jMwfGIjE2JfCwrizWs-oFAHehIOZoSD7Y7tTXP1SS8j69Xx802bJH9GDEmYSMc4VLXjr8oo5l9muO71vGnukW2_6uEN05dq_qDwDfq4RFRm_Ss_byGzXS0uxja8OfERCvkzDWXijZSDNjwsCbDlubLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTzKnzqoa0Bt2GrF5HVEwT9XWzn7pV3xSYTzGpri0V1ljrJ5_s8odagTzvP8YURj_NTzIReVYLsi5lxxc7DqbmRpmDBluaiv4vtulrsehTO54V2hzaEy1iK1xtXnHIjVVG5fFuB43w9FGlaP-8b0Z7B42hu5zHyIeCZFrPbhGNQkl9liLhy1XrBOd7_habprPgoh7mkrxbg-IoypUqCQD4U5H7s8aDydGPjj97h8k81cJJDnlO6xAs6zpd4TF0PI8u5ac3tXy7AJvKndYHYns-o6opCqSmsHRkNiJdQqZ2TtQfGSEHUGoaa1U-PA8nk1S5lGsMz_aM04h-L1XRHgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wcr7Gnbyrr17TvybOjVEtTk26qZbmx1eyHpnALQgWQPFx5882juDXrYD8-xHxrQo4rqhDdYHO5nOYAgOfPg4ujH2T-2YQ90FfSHL19L_EZXdD99AypgIkuhWBG62-ewYkhWDCgPZf-lRfaTkVcRjq1SiTJeIFIRIfDA-Ir04E9eta078a1UOB0yDydVJKrhfnJQV4-VHz657lc9oitqUoKWY_hFDomLfWAlAAfWKCXSnln2p_aFxoGK-hcgik4skPXdU562uQfVBg2GE9XYADhOjccDSP1y7H6TgyG_FnxWuX4QUxvgBYLx0iuMxJLhUFcqPWg70l_wRG8FsDgIYbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=eCDVcdoy1ZRGQDrP7DIx3ceZTpIpJgD83pgXhI4ap7BHBwJhQshKVKrlG22pIvOKpMjVe6vsqfM5aQ_WKHUBn5RivQnwUobbnbpOhioDdcD_KvmXH1HdSsxQQWUcQwMnOA-GFbEpjmLmGsrzsNbQs9EC28TVv2KjEUy4nlIpwkleyM1z469ZDp-HmKNt_tEl-lQ0134UkIwVhuvzGY_BQAPsnu3HdIVjR77FxGDWYsYwPF5EKoBYH7uvTCfr7avVDed0V3_ulKPmjlECN7GCy06viDc7veMIO4NWZNEVIDSbk3PDBAmkKlBYVGBuxJOFQS87qz5BT1yCKpb7H0itWzQdj0lgdVwW7ylm8HLsSXA0WKXTM8HBpQTlGBpfPoT5b_kbp6krduSo2gKdVOMu5v2m5idozE4NmjWGNfR_1hlnw6IEOEIZwAs6adH84nEIzdgIk2P1KBm5Z0ayxCh2gWGrYG3kdq2XdngxGzIlKnkT5JsLwvo1yTNuAyvon2Ee9l64xC60APDkQc--f5ShtQ49Va6EPDWt1lrShLbTxQZ4OG1VB8CQm2Pl5sex53RpDjLUrVvTPerO21gq4XSSpOqgXhcjAIZZE5mdl8VsSR6inHcCVrnjo3c3n2OUFrUtuEsrfDBpym5Vn08yMBt5ej4WYKDAVUzVrC1284eVWgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=eCDVcdoy1ZRGQDrP7DIx3ceZTpIpJgD83pgXhI4ap7BHBwJhQshKVKrlG22pIvOKpMjVe6vsqfM5aQ_WKHUBn5RivQnwUobbnbpOhioDdcD_KvmXH1HdSsxQQWUcQwMnOA-GFbEpjmLmGsrzsNbQs9EC28TVv2KjEUy4nlIpwkleyM1z469ZDp-HmKNt_tEl-lQ0134UkIwVhuvzGY_BQAPsnu3HdIVjR77FxGDWYsYwPF5EKoBYH7uvTCfr7avVDed0V3_ulKPmjlECN7GCy06viDc7veMIO4NWZNEVIDSbk3PDBAmkKlBYVGBuxJOFQS87qz5BT1yCKpb7H0itWzQdj0lgdVwW7ylm8HLsSXA0WKXTM8HBpQTlGBpfPoT5b_kbp6krduSo2gKdVOMu5v2m5idozE4NmjWGNfR_1hlnw6IEOEIZwAs6adH84nEIzdgIk2P1KBm5Z0ayxCh2gWGrYG3kdq2XdngxGzIlKnkT5JsLwvo1yTNuAyvon2Ee9l64xC60APDkQc--f5ShtQ49Va6EPDWt1lrShLbTxQZ4OG1VB8CQm2Pl5sex53RpDjLUrVvTPerO21gq4XSSpOqgXhcjAIZZE5mdl8VsSR6inHcCVrnjo3c3n2OUFrUtuEsrfDBpym5Vn08yMBt5ej4WYKDAVUzVrC1284eVWgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqkT1pCrRBxMOm6MvYxMKSzWkVsPO_iDKVixVihAoOXGkFx-VjaJP0VMjxPg6h_F7XRkmZMOLOaeEwFHNr0zZuhbuEMfWAUTG3ue0ivZFvnjamV384Fj9vCT-lx81L6S_phOtCzIMutjKcFYGPanLd5IYViODa-vVrOM8KMkOgQs5bZd2zgzDBr0aAvBAP3UDM1WAwh7wJPmd7i3acMoPbe4fG3Jf7X1de6oTBqzBn1euC369SIRdlaaJCbYJKYjqqxFXnXzwBSLReYXNM6uR2Udp5RwG8r6C9-PNXajMsaCxqMJqdefdlm1O0q2COqqaKbwWbPn51iInAP1fWq88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Shuk1cLZbsUjqZJpDychTPtgOfVdQGvXG7FulmyBxGfiC8wfPY3FGgmdaSy9pSpt4WB_7TYoyBcig2_Z-O2U6Un2ZG01v8G4gpPktJjQFBw3MpNb9pCfZDR8J_9YHDYP03rc-T80cT9JRO1Tj8KQe3w8cVdeEM3UyUyU0HQwpXooQKrLv4D24NwRDIh8xdHjINT2ikxCw60l3uz3U2ZIBmHypozASEiKT6hkpcoVbI9VazW3BWtsZM3REMt5F3wM8IGzkwNCeprCzAL8In7y3j8zvlLDqdOCf-IRJyQmwFt1VdLrIVTU1iOWZBy_bW1cFSwQIfrt2X9ikVNvX3Xd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIaqi606YbwA825PCHE5lrr8YQXs9H0UQctfk_CmlMm-M2-MmIfZmY3kpTXFbaL4ny8zlrWyVG3jrEBcc7vdDjp1z8rOIG1mfjA5oNvK2io8HaABfuxRnVRFiCmnwesJqN89YPEe69HAxWHVbvDsQ6zCTkcbQmD0PW239MtxlfXFlJ7Yo931srV7kEwwA6tZ1PJ7MnpN9zR-cilcf1UfKyEZrCCqY_zZoSLYQ637_RTXjAV7VWomPwWZASAHN4OH9u89eYCSJ97ZZswf-A9-k4Js5BTejBNDafhDXBIvlxE3G6nkK_NNBvO2SjSBpD3NLkqv2RQAu8OdiRyCDbCHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2VN5SXjSmNMH6VuLPiy7FyRP7Gf1TFP1UKgBAUoQlC6lW9_i_b7HaHYxHl0tfa1iJ69CTxCByASoM-WsfhbjavfKo7KqtGckFWF0tfiIJBjCxpwV_qMrElfp40PSgw03H0H6Pr71kgWXeG0iHUCZyNWJVsbkBG3J-n1SVT4yl4VxNw9_3Pw3pfn6OAlSf1mDH0RhZNPNkH3VSCvil-rl7AIGPlCaBcu2481QOrOTSc5Eb5kMPKxFAtiX0RKN071VSprxQlCJzlZeH-qOPQhmy-RJc1Z5yNokE_1IiXy_jPhTX8zgLquD7HRbNBq0hqwv8YfxnADnBBLHIjU9tAtdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=MSW7FZc8qxxJ8urqnJA8OrJCBGBd9SccbxIniu2yf00ZxKW0zgFhiipl93SyOvQBQXcKf9y0LL5GYGMYiNNIfWewKO_emhEjH2XTRY7OlwGpsGsTK3iVGhnyYt5to6nNRACRfvLEjHVPqSUP4v1KSgW2eJTxsUfN7Dpru8XXQQy9r7OStLhx1114KDP7JYfRbKJUH8YKhMwjaBEHTEtIP_gLAvKMSwclgIScMRCpEHuUzbDPw6nreCwmynfNF7du0DqzXsWX-iCvYFEeR4QVnxE9nP_23mh12P-BHA-94EHmslbTCxFo_ep8KX_Fn-15ZJNRCBfvn9x7jcKVOnU26GAPjkmnmRF2p12zeMzaY6LaHK5q8VeZkZPLxlNTzD79RtqYTS0X2OLyApejFwVj-sxGkNehoG0gTuQvL1WAr0-vySb8qT3n077neNUuz1OJlBYGiZ9oN_MphYEOa2R6c1fEDUnVVQqLSILhoMY0X-zZkg4cr-x5DlwJuvd0iSwmXH3vLKR2m0FvkJc-Sqcbktp-DAskis31hiIG2nOp5qZBN3eDnvay9VEzITiMImGzhqUjoFshdsVhICgcD9El7n8fqW_OZnKRazjmimiPtjhuluim45nCeW9WOv9pBagAwWzWD2tdc4juYpAiV5SY0t9OOnfLpFa5B-GADOBB5XU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=MSW7FZc8qxxJ8urqnJA8OrJCBGBd9SccbxIniu2yf00ZxKW0zgFhiipl93SyOvQBQXcKf9y0LL5GYGMYiNNIfWewKO_emhEjH2XTRY7OlwGpsGsTK3iVGhnyYt5to6nNRACRfvLEjHVPqSUP4v1KSgW2eJTxsUfN7Dpru8XXQQy9r7OStLhx1114KDP7JYfRbKJUH8YKhMwjaBEHTEtIP_gLAvKMSwclgIScMRCpEHuUzbDPw6nreCwmynfNF7du0DqzXsWX-iCvYFEeR4QVnxE9nP_23mh12P-BHA-94EHmslbTCxFo_ep8KX_Fn-15ZJNRCBfvn9x7jcKVOnU26GAPjkmnmRF2p12zeMzaY6LaHK5q8VeZkZPLxlNTzD79RtqYTS0X2OLyApejFwVj-sxGkNehoG0gTuQvL1WAr0-vySb8qT3n077neNUuz1OJlBYGiZ9oN_MphYEOa2R6c1fEDUnVVQqLSILhoMY0X-zZkg4cr-x5DlwJuvd0iSwmXH3vLKR2m0FvkJc-Sqcbktp-DAskis31hiIG2nOp5qZBN3eDnvay9VEzITiMImGzhqUjoFshdsVhICgcD9El7n8fqW_OZnKRazjmimiPtjhuluim45nCeW9WOv9pBagAwWzWD2tdc4juYpAiV5SY0t9OOnfLpFa5B-GADOBB5XU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=oOMwOeVP1XS8ygG1jUvfJBPS5uQ4OTZeuhJvVuQdRNoENloAIV2MBdF4hvE2J49XO2eUaxmisTnI43Q2HICZEb1By0UMIz6u--dNQYkaY2yWr_7zs0M2QBOL2__jl3cxVSL4sUIK3QPjhYCqY_j7QPrBTi8WMwk9qmK9rKMdodk-qglY1lZi1EMMpz93ACmV4Ko3M8wQDYttnBatNUqWboNo7_POYqIs4nuFkEwNtq9qoIWCV5rVczYITIzo3KLvz6SEccCHcGhH9eOEu8UgkvB3TzSdlHRyp-dDZkhKu6PyenGXkMfD-crLSHL3jkvm696BzaEo-XZTPhvIJCdd0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=oOMwOeVP1XS8ygG1jUvfJBPS5uQ4OTZeuhJvVuQdRNoENloAIV2MBdF4hvE2J49XO2eUaxmisTnI43Q2HICZEb1By0UMIz6u--dNQYkaY2yWr_7zs0M2QBOL2__jl3cxVSL4sUIK3QPjhYCqY_j7QPrBTi8WMwk9qmK9rKMdodk-qglY1lZi1EMMpz93ACmV4Ko3M8wQDYttnBatNUqWboNo7_POYqIs4nuFkEwNtq9qoIWCV5rVczYITIzo3KLvz6SEccCHcGhH9eOEu8UgkvB3TzSdlHRyp-dDZkhKu6PyenGXkMfD-crLSHL3jkvm696BzaEo-XZTPhvIJCdd0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtyYjuEBpFRa_Q4ie15bzNQLGhZ24_mPTuq6tniO6UlE4Zti5jcvOPHiKwI_UfB5BdNYGXxvJP56eOMDq-mxer1dRiU35jmrFismfDXTqeJShe_-ZBRwBZKepDH49mqowo2Rw_NMmgcn7V3YQClgf9saRP6_Uysih5fxC06vw5GjVrm22Vt5J8fdTw0HJGqr2yPGX46Q2nPa4dtTNhwiFK1W9I1muzWsbuB-T8sBKsKIZ2tMnsF0Z7YOLM9BEMBhpOwFJXLWzNJI0h7Y0AqNnQ8NlzZlEQRpHh9zoMtkRH2tdGHp4LAJO4fjuxgmJcmhHaMhiaxpsVvF0-8SiYfO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pswmbeVOJDbJKDEp97pkBgcBmMKIjo5HpiWMlVqsksc3XIfbRMSAEEktc8qSCZ4dfotpLnjq2y-gMNYgWaxmnkfhmTUpnRggQs9aVz0TPT2v_x_3uaGNrf6PdUxheKv9HlvHCEJiQ2aNVeLOI6Gmm2raj99QzINOnf89AuAMU1JiE0QfW1_5Xxq6y_egde3jGCABSUWwIbU6OiYbue1iLEOJwdOFt0X96O6yY35vhgQbrCc5KfRGSxpb46t8CC8yBlV_QncARdPtu5Ha1hwzijVJjOuQy0JlEnjMrFz7FPLbe4Mr7xqvzcXRVJd5lW37XuigACGq1xQdILlKBSstiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4oNSXvy4hi4quHzgNx761dhXwoy5bS_GwuUyOvcvoYjGPvA9cJBEw19EVyUlIJrec8XJZNJ75ck3hpsfdnvhO8rmPMF83TUHwXdtyU-QdM3K2G3s-u_GAir4c6Lrk--axcjj2FSRiRkFkJsr5rY2vd4m76XrK2meeFDBT49ri5WxIgvrWv7u6RRt9XjAPyoywZaDkceEbARi_-s6pQyT4jaKcWrFCcp9bvqh7S5uO6QEFsvHRMMaVttsv2KFnUlwb3rC1cXIk9S3wxv3r5UHUcccyo285GcJbsUXWJjXzCqp7x_d7P6qXDmC5y6BB0Tnn8pGAt4O3xIZv-eFb6FAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbIX_mXAsItKD5yEftGEWgxDThUeHvZTU1oLoQ9TLMhnM_F2XyLbTDI3sgzlbscx_5EDGUB896rnwVHo_e2rIBHjorkSchO8wzV99988jYCZ9bfkkpSrKcNXN_T2bFPzcLhBL0Zx1Rvtc730iRjPYoZkx-QkhvEtjQ9ohwy1vaneFFLk3mc6rgV3Ru3ZyyUYDjzkf_99c9Xt2cDN_1LnOr44QolFjayfzqFAnsmzZGz-1oRxF6V_BmW7GhSs8knt2xUwfE6VP6zp20_kQ7BqQE6nDTYumes1dE4NvSktJ5QhX8nrlmSg7b1MdOvW7bsCtfWH0ThnrrPmrxCqAnmIsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDwniCiVpCbtHFVRHiBpVviymsL3ezz3H_6e85SuR4Q0OmWZP5NVANDtfex1b2HtGApLfG2uZWr3uP3h-NPdzn6DCL3TihSp0XmXndqbKNa7q2GhVXAyVc_BwEayNKWZ9LUaqeMXeocjzrWzJ2A84xvMdlDKg_-PSXzOPzbvkHmvm9cDzvZr3EmQ9DBrjmTJkb3fqoxF483Jk7EocPzXnec8vIUPWb7Z-9SYRWTKvX_l5ChXMc9Fh0UFGJ22E_fMvKPSxi3WkCcutV97YK_iZOfdETR-H4CqMJ5Aso6Nd6-ssy_Yze6MIUA3gkcNZ9X7RUC46zWMTtviE1OopKECkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obq4BFsYiX40LftbvcgBEpJ4w2XFxtIhoUDKn2uRdLGbWOWKYe3g5LCpCwPMeqRaAxp8TyvPY3IXd4HcTGr86HS-Y8rZBzTn8pIwv1T9Cu6fPvhZ5k0T6izEqR6q1Yks8axGnuC3vy2Bv6PVwCEKUgPRmRCSakYExXkhOLntxX_NTeIEB00zMdpwvFvQePGQPAlqcMw9Irwg073u4aY6M3hbjpqeOU8Yc4GtZqiK_hpjOrdkKLV4_IQuo5k2GLcHdb-8ooXazDWH3QHfxo0hSTkegE198FhvdsVGMonwk2YFxtS0oFVFUoPsVPFJn7bOjy14vCioWauG2E4u3urUbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIesK_DEFTFKQj-lnoY1RKxKcFplUWjdgWg637hdiofstblDgNhMIOzi9gtsyC1Q0QAehVcw8qajt1cPm0Gbs7iT87gzj9I8RZLVLVqG0c8CjoEn37gbQz2sknSeIEUG1VBCuo3VwRoGXVNXXWMfYeshiYN_-7Uma-4RUZiHVcqyeC60Ku3BmSifIJGcxU-p5GUwmZvAm6isJptZVKhsbAer8leLiXgpDHtH9GMk3fFtKMPqdfvMCnaAngK_PPCn5MdsnhID7fVf860viL-fysS9gznsk_NPZ9WibEBuWBEqNUzXW5_GvZS_6sniFgLXkVXyipj_96LB5f5uY6By1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=h7q1tQwb5gO2sk6oSiqr129aZcWT893s6KWuWW_pCkKUOYwJzh7XP-p-YeEp_RZ3Yhgd4EgF03iitSalbTcgeMMAq_UdcJrwy7--jx--wUKzjuZQsuX5X-Pq_6r7yuiVOZwOsJYaTBui75QlOTYJ4zZ4hFuUGMT7ANn-_lfWgDpRu7v_-SkUIn8hYVZUIH_I_BlGFFm8abAuqf78FMAIhoreZ6N0wCHut4ulEohv8M8zG1tRsu5wfvbuUUl2bXleCDdVuEIuwlsVhLjzQ8r47wOxccf4xHRKFuyLN3udn0Kbs3zieg-cUiNT39h4XbwFr5Q8ohz8xODUapP9eZ58yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=h7q1tQwb5gO2sk6oSiqr129aZcWT893s6KWuWW_pCkKUOYwJzh7XP-p-YeEp_RZ3Yhgd4EgF03iitSalbTcgeMMAq_UdcJrwy7--jx--wUKzjuZQsuX5X-Pq_6r7yuiVOZwOsJYaTBui75QlOTYJ4zZ4hFuUGMT7ANn-_lfWgDpRu7v_-SkUIn8hYVZUIH_I_BlGFFm8abAuqf78FMAIhoreZ6N0wCHut4ulEohv8M8zG1tRsu5wfvbuUUl2bXleCDdVuEIuwlsVhLjzQ8r47wOxccf4xHRKFuyLN3udn0Kbs3zieg-cUiNT39h4XbwFr5Q8ohz8xODUapP9eZ58yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eflVq6gJK_9-2U00nsKMhzzo7VJhb0PgWQwwTOP4goIzRAi8_bFX50V2tIJW_izVk9sETxdAxwZlGykf2XFxAZvBaY31J8_tvO49bOiIhr3tcofZPOCWp-Br1RmI-UDI8Fe594ZuhLC1UyVSbECHc30_AZ1HTmCcoYZIXFWJQ29s406z3kB-TKwfeK5he6-TBEzsh6zMFkft0ny7wy5emm2oNoXoul72o9ETwq4nBzBpOhzlgneX_PXGhPRTABWlAybH4bHRu3gqeJ45jDBg0vTcYOCjv4X4GmkIxTlOef25zIsVMlvZU55ZCNb78pOZVe-a_fF2GMYvz_1_SOQSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=QmjCeX9fqfEZiatzyTHKWs4vAo210Po-Imfi1PCDYLzAob9WCllQq3aQ4l4yMuT5a2MIkSHr3aBwIj4EfjHftAB1FuwoGR_de1uV6a67xDMk5CuIfC4EHTL80xePjW5Fg8EvUaOsMpmDiAbdRx3sWx76REwhX-AsPbWkPSr8XrzxxRUq4HXzq_guMTO-53Ola4-L52t-BomS9GrYnXcQkpHXBxoALDo4-rQuCVYlSqoIaVrOHZF5go5E-IOVHTYO6MsaFoDqWqR1keM13sFdW6Fb2_2C2_aFNDsCOP1FLONeo2unSL0rNod8grcqcorCBkNAop_p6UIfS7v08iREaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=QmjCeX9fqfEZiatzyTHKWs4vAo210Po-Imfi1PCDYLzAob9WCllQq3aQ4l4yMuT5a2MIkSHr3aBwIj4EfjHftAB1FuwoGR_de1uV6a67xDMk5CuIfC4EHTL80xePjW5Fg8EvUaOsMpmDiAbdRx3sWx76REwhX-AsPbWkPSr8XrzxxRUq4HXzq_guMTO-53Ola4-L52t-BomS9GrYnXcQkpHXBxoALDo4-rQuCVYlSqoIaVrOHZF5go5E-IOVHTYO6MsaFoDqWqR1keM13sFdW6Fb2_2C2_aFNDsCOP1FLONeo2unSL0rNod8grcqcorCBkNAop_p6UIfS7v08iREaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdQH_1ce_-_ggRaCIWjMaaQvGKhxcYK_wC_3hYe5cBleWPxBbk9z0IGCX09IZ9NvOLECEOoZQ0XHF_ivV3mwM5Vg6Dcpf9gTM2DrRQOsjmBXr41O9R1fuHgZ8RZKxLA-1vXJVNClGapg2I3119Yil37e0jTfjss-O1AyBx4bywzMG-gvgI7QKoNzneLbNlsuGX4TRnnoP8zbviL6bjDBGiL4LhwOSXqejhusa50PPTT0T0lF1jA2PlwHshmgAH9tVMEQB0CIueoNu8kWDr4UROCR3DQb-txQr8D2En2dX3aZFDmkTNCiU87qA4ijiLg9uOwyj1e36G_vWZSdIWRpNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGHn5I72bF2WDMh7uctMa5Ka7mT0WW7vIOwP_7jC8WwfT5BopAXzoYS67COl_AIcFa3XDRC9XSR0WdT0LVx0N7cZRCKh36WSuxi3HK11LiXjJZUOWwLlJfNyHbKeFZe8zLW4vhmghn1EpqNZ-tN86ijPiDdZVSfZvltbev_DP3B83nXtTlNQGcJb4PagDPp0WGTZzdjQsqQecQbGxQq8k0unWDh1Rj3ww_R4da0pap29UPBwJo50zJtGAceIL2HXc__8F23KUarr7asLvTiGe9nZ7gqJoRZLucdpHrJgpSfn9lmuj8qy2WHywo4WT4J6UFJfxwPfweXL--k4YCOTAXIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGHn5I72bF2WDMh7uctMa5Ka7mT0WW7vIOwP_7jC8WwfT5BopAXzoYS67COl_AIcFa3XDRC9XSR0WdT0LVx0N7cZRCKh36WSuxi3HK11LiXjJZUOWwLlJfNyHbKeFZe8zLW4vhmghn1EpqNZ-tN86ijPiDdZVSfZvltbev_DP3B83nXtTlNQGcJb4PagDPp0WGTZzdjQsqQecQbGxQq8k0unWDh1Rj3ww_R4da0pap29UPBwJo50zJtGAceIL2HXc__8F23KUarr7asLvTiGe9nZ7gqJoRZLucdpHrJgpSfn9lmuj8qy2WHywo4WT4J6UFJfxwPfweXL--k4YCOTAXIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=uosa_3AsRIlbep8x8PXvk2Y-G3uULCW8eqoQPW0svn2ICC0J53nDv2qFGYumn1LzUcOfsS14da0xG183wPOm5cBd42ymAlN6fPqqai0syJJ3qXD3Tb-HuNDpaj1zU4pYBNC2C4ovlTo6fNIz48QtHG6qGquqZKlG2CHf5OeXgGER1YBVRcgclruOj-Kdhb-PaIhvSrzkio04WqsgRuG22A84v__FpbQ9VMfcPN6e7hhvUOTqhJaCtzqS2Wb8yqBZOHKLlCuHTMpklC71sdQa0FdanybIuf739Ua_QZes0w_3x3gUKdPbvUJgp_XzTbqucER6_VrHOwo7z-C9_S7Qmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=uosa_3AsRIlbep8x8PXvk2Y-G3uULCW8eqoQPW0svn2ICC0J53nDv2qFGYumn1LzUcOfsS14da0xG183wPOm5cBd42ymAlN6fPqqai0syJJ3qXD3Tb-HuNDpaj1zU4pYBNC2C4ovlTo6fNIz48QtHG6qGquqZKlG2CHf5OeXgGER1YBVRcgclruOj-Kdhb-PaIhvSrzkio04WqsgRuG22A84v__FpbQ9VMfcPN6e7hhvUOTqhJaCtzqS2Wb8yqBZOHKLlCuHTMpklC71sdQa0FdanybIuf739Ua_QZes0w_3x3gUKdPbvUJgp_XzTbqucER6_VrHOwo7z-C9_S7Qmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BVx9rxUfyiRAVPWlWLlKIbivJr_psv7lmp7F8H1ASaXYMWSY1QcwPY0HfcvuqF1iur6nTV92ugAYGZfrEL2JIKLfG9Rq-bkfA9-nV6vYTdxzQvJz_v2aWTV4evGj8WCy_gE0R8V2-4O5TXR2qCM86M4UbjpxZJpj8PTUiz2fC0Y-oCGDBnV80ghun7F80Fc0a4gGZKwC79QppF4IhfnRhm5IToA3KRrfhZEwINyFaqfW_zLtlFAfg6p5opCBRXebYpGfCKhKwAPl8hdsM8fViLt1aVwrMZH-m3d6smRvLbvzAM5rXjQ3w3XylLC61UxzMegc130T_hvM2faU0jk19qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BVx9rxUfyiRAVPWlWLlKIbivJr_psv7lmp7F8H1ASaXYMWSY1QcwPY0HfcvuqF1iur6nTV92ugAYGZfrEL2JIKLfG9Rq-bkfA9-nV6vYTdxzQvJz_v2aWTV4evGj8WCy_gE0R8V2-4O5TXR2qCM86M4UbjpxZJpj8PTUiz2fC0Y-oCGDBnV80ghun7F80Fc0a4gGZKwC79QppF4IhfnRhm5IToA3KRrfhZEwINyFaqfW_zLtlFAfg6p5opCBRXebYpGfCKhKwAPl8hdsM8fViLt1aVwrMZH-m3d6smRvLbvzAM5rXjQ3w3XylLC61UxzMegc130T_hvM2faU0jk19qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxfavJr7bG7oFx2evaR-A6KtzcWIhokAISZD_IgKZYWTlbWiBKoNu3SmVVnjswkaAxHmoxVUs4eQ9dzWF5xJsnUXKR7XBwpgSzXkW3jBmCb6qPCMw0goGco9O7ofpdDDvkxrO586T4gt9Yajn0FfETweMdNuL31RCu7htLcUdVwEfTSUcWcRUtigRDiLbeXn4HlJBZLSl27HJjfjQ2qnl_Ra08j9TMxfwmaRkDfvXiwvZqNko82C-1y_6BegWLhGrZ1GKZbQQnPwiAbZJjcjBj_WEr2b1qWmgx9EnTf5pGmX98Sn9ndaUt0pcy3_RPykeb8n3G_t9aeknZQ-Q4xRQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWKWRnaL5cNiC3TJTKfhsLC4T9EahNjdD-tGhEAxplPfZYfxDYsDxgCEaX9e6h4zOKQxUNKMIyWPjA0c19tH4-0g5L01Jw6putzEGl1v2gWoDshXG1SUPlnFZXguF1894ooknffEqWIVAujlckebRWEiOlo4kE4DqEQIb9HWGelYoas3MtIQ0uQKsgwzWAKpdz_RsO4JfpiWNVeL_Kb1YQRoTW8hk0pS0BZAK0Q4nxEYb_T-0aXEiRrMUktcqLAWYa8CH8NjvzPxCuKv9wvrzFyW_aFRYXXLhU6J1JmhP9pUAnqWJBpxvF17E3FqTCcl0pzlqepElaFw2N48ef0Rmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwxLSm7uKuP4CsRZypBczRmY_G-iNWdFAw1LCOlfS-efxLxTqPQX5DW1E1MR9fv9l1r2ouzVs4VA2B7JNhMq_ZqI1qVmcbWljflNgC89YiJw3UybqS4muNPHV1Aege6gTI2Nf6u-XbZg8mgfbpEVTKZIoRlpCgo5AbNS4lmrYt7BPWF_t0o-J7MegoDV4xitF3SsamwcY56O94TW8Fvi0eqzjwZH5lxgNj0eH9o5uSh-xUOYJ3ZHEVf_9hrCLG3Pzj5evj3cvcl1CRLhItxbFZgzGAVEkNCHTd36WZaHs_H3XlQtpwPlP4surW1NCSd5f0OTTiC6nO3ogPTF_SUDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
