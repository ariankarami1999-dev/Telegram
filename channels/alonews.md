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
<img src="https://cdn4.telesco.pe/file/tGzl99DTxpMYOc03avwktwhPr1Ug2QqI8isfIt_NvNRFPWdSn-5pI4b80idjKbnsm7U2HOBnF-ipKQ-UNWctSL5lbCN2qB3KTcge1uw-SGV3uvXT5uIeYRI0lDVO8Q37AnUwPSJDuccTqXS1mr6SdYkjeQungtc2LOL5V1PK9eGbRGX-g8gyId3SU_gggTzhu_M8Zzc1rk1GH0UYhORFRxJk-juR-G8omp2B8i4c_zgAkMH5Wr1RZlSFhijyUBohqCXk4Uqq2aSErseUpXh7aQoPpF2q9IVsUNaGb8JWJot_keM2MMyzXogK26DabfbRnQAaI_-bsOVik3AaxZ-P0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 983K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 18:16:28</div>
<hr>

<div class="tg-post" id="msg-143383">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-7eW3fAa5LJ9VTF5_pcPkGQYyX8_sGOr2Ugf7_Baj-2SitgWx6nsFWF7Gxh8yy4J_lCaXSx2zGw7-z72HVWZdC05ngZ3ru6_lWiM2Fo7WaU5bmIHha-f6uOnVvg12og-pnUhtVCsr3jvztTchGIpgOwU-bzY2LQ_E55vkIHeLRmLPuPlbGQOJ24VwwG4vFNb2OhAo30xAL3I-FncvkJ4Af5Q9UGecAiAxy53GPrAowR5OAt2qJccNudh1moEXQRmOldWZkh2CoR7UI6D8zvcrnfCrE2bZbYfm-1a388X8SWa-WlaEm2-LAy6udSLPG2U9wq56S3yCa0SmmuI4fcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خضریان:
آقایون حواستون هست وضع حجاب خرابه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/143383" target="_blank">📅 18:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143382">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نیویورک پست: تسلط ایران بر تنگه هرمز درحال از بین رفتن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/143382" target="_blank">📅 18:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143381">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):
کمی پیش، گزارشی مبنی بر تلاش یک تروریست برای سرقت سلاح از یک سرباز ارتش اسرائیل در محدوده میدان ریمونیم دریافت شد.
🔴
سرباز به سمت تروریست شلی کرد و وی خنثی شد. سربازان ارتش اسرائیل به محل حادثه اعزام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/143381" target="_blank">📅 17:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143380">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏
👈
آسوشیتدپرس: سفر عاصم منیر به تهران با هدف کاهش تنش میان آمریکا و ایران و ترغیب دو کشور به بازگشت به میز مذاکرات انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/143380" target="_blank">📅 17:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143379">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
قیمت یک اسپرسو تک در کافه بابک زنجانی 800 هزار تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/143379" target="_blank">📅 17:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143378">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZepV2ozYyrao106qScXrmD1QE78fVApaO17GCuP6UYtJVPVthKkrdONfaMekfXdhdKI1ekL1dbrKMS8YahTVWsBvncgoW2M4saeBxb4ic2tENdyRGI8khroWGjRE1ru9imB_abzNeO-e_jvRVtCqOERstNtxT8T3gaKM2aKvUi1KXI5qocDJ3usmSi7Qto1NVxJiJUCBeN5VR3CiTto4URcIHQ46BsnRvzVrdkwHbgeq-I3P1HZftXhHtpxaNyazFLvfcbu7Zq83dLq-y1T_vy_fslfN_K0fV03-znLfmHdK4h4dCzyfDjOo1aXNNIcSShyeecVUbhZkDYUUfnMDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی؛ تحلیلگر نزدیک به حکومت:
تغییر قیمت بنزین منتفی شده و قرار تا آخر سال قیمت بنزین همین باشه ولی قرار سهمیه ها کم بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/143378" target="_blank">📅 17:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143377">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe7bef062.mp4?token=BhTjowCCaIR_ajmMBcH1eYsIu5dAn04h45GxMm9rhuF7bbUzvV1PE3F90FxLeekKYakSfXRjt1ffQ7rQfpKrSWL_FGqQrNZoOtzL7vJeuT1V3L06z1wAIHQEFOW5KY3-y4h2jQXM60waKq4NkpvIdwUjwHdcjQBf05tBucFHrHKnauXWEqlp91gxEI5UCnoKQIFLATE8K4VEYsrcKgguTymXTe3AimZm4nE1WuxXDaI2wy9eGrUd4K8HTAaB36i5c7oeG4kCGL1pLP91SfQ_CKtBohvi5qSlCgnWyLI6xoXobFmMfHLc3jz-Ujrf6t9pa6jGe56Ti0llSaJZ3UojVT_Kb4mDktIrr9cwvbgekJWexH-aPr7cvy7jwZ0pb_42QHAifkT70yMfnDVZsv2kFVkL_FnB99fKv1LFy1JJaN7D8lO4PDpPYd_s8R95UHWcUkI0pueQNzA_Mdubn4-06gSK3F5v5it2p3IDiCGbjiTdmz0YNucRT6r29PZInguY6FKa5jLDdcQA_8SHiyB0hjucHQi6QHSD6v_s9KCSvZ5dLXXprXAGjXtmNdB_8axOLc6Wn1HACknLqJLbypVzntrApEBmpJvZGHbf6pqmSHoryfriBlpnwzb7SULdD0Svve97ddf9iqPIQMGitaazRF88JMj1TiUj3UGk83cCtQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe7bef062.mp4?token=BhTjowCCaIR_ajmMBcH1eYsIu5dAn04h45GxMm9rhuF7bbUzvV1PE3F90FxLeekKYakSfXRjt1ffQ7rQfpKrSWL_FGqQrNZoOtzL7vJeuT1V3L06z1wAIHQEFOW5KY3-y4h2jQXM60waKq4NkpvIdwUjwHdcjQBf05tBucFHrHKnauXWEqlp91gxEI5UCnoKQIFLATE8K4VEYsrcKgguTymXTe3AimZm4nE1WuxXDaI2wy9eGrUd4K8HTAaB36i5c7oeG4kCGL1pLP91SfQ_CKtBohvi5qSlCgnWyLI6xoXobFmMfHLc3jz-Ujrf6t9pa6jGe56Ti0llSaJZ3UojVT_Kb4mDktIrr9cwvbgekJWexH-aPr7cvy7jwZ0pb_42QHAifkT70yMfnDVZsv2kFVkL_FnB99fKv1LFy1JJaN7D8lO4PDpPYd_s8R95UHWcUkI0pueQNzA_Mdubn4-06gSK3F5v5it2p3IDiCGbjiTdmz0YNucRT6r29PZInguY6FKa5jLDdcQA_8SHiyB0hjucHQi6QHSD6v_s9KCSvZ5dLXXprXAGjXtmNdB_8axOLc6Wn1HACknLqJLbypVzntrApEBmpJvZGHbf6pqmSHoryfriBlpnwzb7SULdD0Svve97ddf9iqPIQMGitaazRF88JMj1TiUj3UGk83cCtQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو حاوی غم بسیار زیاد
🖤
🔴
پدری که خرج عمل بچه‌‌اش رو نداره به بیمارستان پرداخت کنه و دنبال اینه که گوشیِ تو دستش رو بفروشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/143377" target="_blank">📅 17:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143376">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سنتکام:تا۲۰ اوت نیروهای آمریکایی ۶۷ کشتی تجاری را تغییر مسیر داده، ۳ شناور را از کار انداخته و ۲ شناور را بازرسی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/143376" target="_blank">📅 17:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143375">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
برخی رسانه ها از کشف ۷.۵ تریلیون متر مکعب گاز طبیعی در جنوب استان فارس خبر دادند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/143375" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143374">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVRezwmQkHpk7Km3s8Hy-ejgCJ0PoqJB57-GiTV3lSbTyWriEhLtze2uWv3WxC65xlK9pR461IjgIzBLAMFlfRgLNBQtQGj8K9tIX9XYwUER3jeiiqh65zQtuGP1BnER4xWRXr7bXYsYwgrI4-AOaxK5JlGR2jsV-0HMGvLP1eAzP-uU0fSiZoWJ93HZ-XBSrTPhCOCUFa15TeBMfjAFtpSypVWmtkIAl3m5H90prz2i6Fx6_7M8qwtgC2S2XmnroggHelQByJKNo1pA42TV1OcSW3NSFx0skIkCpVKEdBJRWktEurDDb_dcvD7XeGQP0tbHYsQ_hoeb_Zh8HucoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فواد ایزدی: آمریکا از ما میترسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/143374" target="_blank">📅 16:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143371">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
میدل ایست آی: ده‌ها پایگاه اروپایی از عملیات آمریکا علیه ایران در جنگ ۴۰ روزه، پشتیبانی کردند
🔴
انگلیس احتمالاً مهم‌ترین حمایت را در میان کشور‌های اروپایی ارائه کرده
🔴
فرانسه نیز اجازه داد هواپیما‌های نظامی پشتیبانی ایالات متحده در پایگاه‌های این کشور فرود بیایند
🔴
بلغارستان هم که از نظر جغرافیایی تنها به واسطه ترکیه از ایران جدا است، به واشنگتن اجازه استفاده از پایگاه‌های نظامی خود را داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143371" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143370">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
الجزیره گزارش داده نخستین کشتی کانتینری کره جنوبی در یک سفر آزمایشی از مسیر قطب شمال به سمت اروپا حرکت کرده است.
🔴
این اقدام در شرایطی انجام شده که برخی کشورهای آسیایی به‌دنبال مسیرهای جایگزین برای کاهش وابستگی به مسیرهای پرریسک خاورمیانه از جمله هرمز و باب‌المندب هستند.
🔴
تحولات امنیتی در آبراه‌های راهبردی، کشورها را به سمت بازطراحی مسیرهای تجارت دریایی سوق داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143370" target="_blank">📅 16:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143369">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3a41e39b9.mp4?token=nTmS__vI1LqqgFUnK54sQXM7ulV5equClQWxPC_RtRJOz4uOIt2HUJAXupdFNOcPQNoj3iB7vAFAXY4nmoEKIxG1SmsTyyFk5WHg9r9ZNkleKhtnOnXPwAPWQRKJ5lQsTLulFhf503kzzqQVewz5nRTGS5YNszaJiD3sdTYOQ03_sX0xYKzf9ymN3sQmDcCrrLdP_U-uttP4HRAqqqt0E1YC4UaO-wpu89Y7iAz9cdk8DnwCDDxz7f3sKF9C0QtEhjkNFR7712IkfbebMS4SlI90yP1bFO-O9FuKiZDUyLxkhIQ0sLvzedkcTEmL2X4U13W0QBclI6jaTFVKIxCIkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3a41e39b9.mp4?token=nTmS__vI1LqqgFUnK54sQXM7ulV5equClQWxPC_RtRJOz4uOIt2HUJAXupdFNOcPQNoj3iB7vAFAXY4nmoEKIxG1SmsTyyFk5WHg9r9ZNkleKhtnOnXPwAPWQRKJ5lQsTLulFhf503kzzqQVewz5nRTGS5YNszaJiD3sdTYOQ03_sX0xYKzf9ymN3sQmDcCrrLdP_U-uttP4HRAqqqt0E1YC4UaO-wpu89Y7iAz9cdk8DnwCDDxz7f3sKF9C0QtEhjkNFR7712IkfbebMS4SlI90yP1bFO-O9FuKiZDUyLxkhIQ0sLvzedkcTEmL2X4U13W0QBclI6jaTFVKIxCIkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
الزیدی، نخست‌وزیر عراق: دولت ما به یاری خدا عاری از فساد خواهد بود... چرا که به‌هرحال پولی در کار نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143369" target="_blank">📅 16:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143368">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THvlE8UuLmCofchHDYDw7yOK3Mk6tLklhHv6G_5s7t7LNT-X6ieszlCFybshlFrep6O6XlQLGsgUUz6vSLDahtuyIGbT_IEJB9hj14CsBeYZ6J0CSE4mz1CfKpnDj9861GB4_0MQ6CrUmBRZ6SSDrayjMVW1KsHPDUHSC1K_Nt18cdMcTdQQ46IDWMU6rkdUnTznUm843v7MuVGDSLB6ViVB2N5gdNgRBe5KgGXiAaLusoJ47sFatXhvGca2pNw_6wzKiWAwcl7cOGIxxNhczyKpjCIFxlfuZwoMW-Bs_WC594NMWWz4RaHJBTmbTWImNZUfcL-rLxREUhKwPyhvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گوشی موبایل هم برای ایرانی آرزو شد!
🔴
لیست قیمت انواع موبایل ریجستری در بازار
🔴
یکشنبه 1 شهریور 1405
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143368" target="_blank">📅 16:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143367">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6f5402ef.mp4?token=dIrA__c5e6OrJZmCSkOHXwllwVQpmWdhtZFzLeiABfHhDvVT2EDS17fzU5dj2WhfH56oAjBCE4EML7WO95LEIHGoueWS2Slkg2IKY9pBb5ABcLe-VJ7nmJ9tLHlCrx2eKiYUzGFCMZfr_GMfDS-UoZIgROuRhGR1Xxt92MchRuL1z1KyQsb_3jCLe2gj2hsj_wzbdWI09sRSQ23ZO1c0S_cKHZyVOMqHBkHKo0Jvbma0_v9ON11FCmNejn5KyUUjDcwVOUubNowhGUPDk7t300YP7ZUUuCg0Pu0EZQnnK7TjtEMQr6tToUSGVCy_yaGCLe8roFFLLi9mes1CVpvi2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6f5402ef.mp4?token=dIrA__c5e6OrJZmCSkOHXwllwVQpmWdhtZFzLeiABfHhDvVT2EDS17fzU5dj2WhfH56oAjBCE4EML7WO95LEIHGoueWS2Slkg2IKY9pBb5ABcLe-VJ7nmJ9tLHlCrx2eKiYUzGFCMZfr_GMfDS-UoZIgROuRhGR1Xxt92MchRuL1z1KyQsb_3jCLe2gj2hsj_wzbdWI09sRSQ23ZO1c0S_cKHZyVOMqHBkHKo0Jvbma0_v9ON11FCmNejn5KyUUjDcwVOUubNowhGUPDk7t300YP7ZUUuCg0Pu0EZQnnK7TjtEMQr6tToUSGVCy_yaGCLe8roFFLLi9mes1CVpvi2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
متکی: ۹۰ روز اینده بسیار مهم است، ترامپ می‌خواهد ایران را مشغول تفاهم اسلام‌آباد نگه دارد تا انتخابات را ببرد و بعد به سراغ ما بیاید!
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143367" target="_blank">📅 16:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143366">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyUPreHR76eDXbSKm6mFhngo4rmLVO6SjG7952hv0I6gYJQibj545ACVDporpbPfIdHUDYFUErhTzamDibkLHbyTtFtKuYETOlUd6VlVKJIlPrSI3oserT0U4MvdQBf4rKjCCVw2tuMQltVwmCqTqvTjEMwgyFEDd__dXfFm-Kqoekwv4u_YfxcU4JvHMHHvrBAsEa6YRQIMLosDmh7emKw-doUMXnDfQbhdG5-Vu51MhYUMMhCGSDsrDoO1n86i436tYoP31hkgc0J9By3xoF3gn8ys3xiRztRw5-VVYPVPLjxpbp2gmK09mjBHOqgWq1PD1Z0QdLqCCdFJ89NNAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
مقصر گرونیا دولت هست نه نظام مقدس
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143366" target="_blank">📅 16:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143365">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kciextJbLto_FEYatiafoyNxsFNvXkIckIHUaDrQ2_M8oEUrY21SAy20_LJnLXg42HHoH8fGTSlDuiTqmw_3XcFDxvK_aQ2r8miekmO1xtvRymiQERQ5HtLTsU4JFcY8USRZKN0SMzqeMHbT5WsEBM6VKxiWCSXJhYhszrbGdEHH6mgpFe56Wj9FLnBjYNwTR7ptVZQ-WYWAh3S-4xexCCbGz0G61tV8IYRh7Ru5cUKY4k37KQcsHwu9P_dWtJKvP4XML1L6C6wroHEV1TfuN6FIv-5k88-QG64gVb14KpD1I-nuDEifAyx-j_1GJFYJ3awPw74cls-sMNzBvSQUdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور محسن رضایی در پاسخ به یک مخاطب: حتی گل(وید) هم‌میتونید تو خونه پرورش بدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143365" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143364">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85fea5882.webm?token=W3VL3RrRaM0IVdZU78xzdntKqO1fUtsIBtesZCT2ojIB-JC-KfYREcblsR59ATpr8mQb-oTIOp6n-7qZc_5D-6jZV-LOzx7TPSgAf3zMgUF5acCCq5uceKNEzC-qb-4BOY9aGzLPlk1t0Hs09zIPUfykCfaCz_ivdAKMd536i0lKGfat5I0TxPROewktpzqNX67BwzVAjiIAJpyP8DAA3aGmUb96KaAshikAGh29TW2dVlmATeBuyppMDJpSzDK23JVYMJvr88ICoM4480Gwt5Q3e_814z4cmGs2CxYUXLjh5OH0tNgaPntuAikXqTeT_4ZU-HghhAW0gVC-F-sXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85fea5882.webm?token=W3VL3RrRaM0IVdZU78xzdntKqO1fUtsIBtesZCT2ojIB-JC-KfYREcblsR59ATpr8mQb-oTIOp6n-7qZc_5D-6jZV-LOzx7TPSgAf3zMgUF5acCCq5uceKNEzC-qb-4BOY9aGzLPlk1t0Hs09zIPUfykCfaCz_ivdAKMd536i0lKGfat5I0TxPROewktpzqNX67BwzVAjiIAJpyP8DAA3aGmUb96KaAshikAGh29TW2dVlmATeBuyppMDJpSzDK23JVYMJvr88ICoM4480Gwt5Q3e_814z4cmGs2CxYUXLjh5OH0tNgaPntuAikXqTeT_4ZU-HghhAW0gVC-F-sXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طلای ۱۸ عیار، ده دقیقه قبل:  ۲۲ میلیون تومان
🔴
هم‌اکنون ۲۲,۲۰۰,۰۰۰ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143364" target="_blank">📅 16:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143363">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
طلای ۱۸ عیار، ده دقیقه قبل:  ۲۲ میلیون تومان
🔴
هم‌اکنون ۲۲,۲۰۰,۰۰۰ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/143363" target="_blank">📅 16:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143362">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0pApW5iDQCJmpYHdnHaHj3KVKdl7Ng2c_P-ahPI3fciM7k_-bx1qn2exRMX5IZgiKGR6SyskyxHuE9NTB-beKB-2XbemQwwqCH6zfpFDovONXMuCVnmBMung8es-LA1tuJafbtm1RL6S6JikMBxfy20PkvM2SA6R4T1IkcuJyQJ9zuhjJT32mOQoRLx4mkzN4zg0DGa8yZBRcn29MGCSYe3dehRZ93uBAI5UZKvL2AhPxoHZ8ioWRa7cpUZ5kd4yT-CmUDQ44GcUlSqiYK4Keoypv01jPJsLNYK6GP_8axXq9fzN7hCFfmzcYNxtK93gsRfMjSwYjUgOzYtGIQfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک‌تایمز: یک شرکت آمریکایی در حال تولید روزانه ۳۰ رهگیر ۵ هزار دلاری در امارات برای مقابله با پهپاد‌های ایرانی است
🔴
نیویورک‌تایمز مدعی شد: یک انبار کوچک در امارات متحده عربی، کارگران روزانه تا ۱۲ ساعت مشغول سرهم‌کردن قطعات چاپ سه‌بعدی هستند تا رهگیرهایی بسازند که قادرند پهپادهای ایرانی را با سرعتی تا ۲۰۰ مایل در ساعت (حدود ۳۲۲ کیلومتر در ساعت) از آسمان ساقط کنند.
🔴
کارگران این کارخانه که عمدتاً فیلیپینی و چینی هستند، روزانه حدود ۳۰ رهگیر تولید می‌کنند و هدف این است که این رقم به‌زودی به ۱۰۰ فروند در روز برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/143362" target="_blank">📅 16:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143361">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
الحدث: پیشنهاد توقف فعالیت گروه‌های مسلح در عراق
🔴
الحدث به نقل از منابع عراقی مدعی شده کمیته چارچوب هماهنگی مذاکرات با گروه‌های مسلح مخالف تحویل سلاح در عراق را ادامه می‌دهد.
🔴
بر اساس این گزارش، پیشنهاد شده فعالیت این گروه‌ها به مدت دو سال متوقف شود.
🔴
این طرح در شرایطی مطرح شده که موضوع کنترل سلاح‌های خارج از چارچوب دولت، همچنان یکی از چالش‌های اصلی عراق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143361" target="_blank">📅 16:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143360">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b3500bdf7c.mp4?token=iboi_qZeXP0MGnVuKiJ1EgoxgS1B8CPb0fhCRzdxvIGuC10-LcAdgBW2dKWXwAfB34cj4yKds2mS7qszK1z7J1sHHO9jwtX4_-4wsPkEXLtHCkF-xiDffEjqcCGDJP_apdsBjI-cxi3kkSQ6IU1epYt_m-nXXFBPcsXHgzFi_6Pbj_8w_lfGsb3XjjiKhRffK8IKkUgrGvv81zO7zTkS-n4oeVFwbZbyVxbATKy1kAUicWKddH6zf-4UtN5I93Qnd2disrJMA6S9C3mk5mmhCBWcSvAQiyZWyh5_AanpDmcQrlpfpNZcV_q--p_gP_G-RHSwDRr9UAzUKUVGnKMN3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b3500bdf7c.mp4?token=iboi_qZeXP0MGnVuKiJ1EgoxgS1B8CPb0fhCRzdxvIGuC10-LcAdgBW2dKWXwAfB34cj4yKds2mS7qszK1z7J1sHHO9jwtX4_-4wsPkEXLtHCkF-xiDffEjqcCGDJP_apdsBjI-cxi3kkSQ6IU1epYt_m-nXXFBPcsXHgzFi_6Pbj_8w_lfGsb3XjjiKhRffK8IKkUgrGvv81zO7zTkS-n4oeVFwbZbyVxbATKy1kAUicWKddH6zf-4UtN5I93Qnd2disrJMA6S9C3mk5mmhCBWcSvAQiyZWyh5_AanpDmcQrlpfpNZcV_q--p_gP_G-RHSwDRr9UAzUKUVGnKMN3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خرس معروف تبریز که با کوهنوردای کوه سبلان هم سفره میشد و باهاشون غذا میخورد و کوهنوردا خیلی دوسش داشتن،صبح امروز جنازش پیدا شد در حالی که توسط چند شکارچی کشته شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/143360" target="_blank">📅 16:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143358">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rB7gDib3JLeW4Qt56rz0ft5X_wPd0K0xS0auzikaidlR3sYjnnhueamw_dZgisoxi5m8l8AJcZU_vw4K0rZQ6bY05Yi55X3ELbwqeWRBdsZ2u1vMuv5x2t7gQTxZVAzSv2L-ZoVQPxI6F-A6xOxTVm8-T7HfapGH0YCd2ctEwC53hvpMohnl2_gymInid4Q-DkOBYfpICDAj33ocVFafzWKEgjejnj6GXpgm73bSVuPOhhfT8Fw7N5HR87vON2u0LW2Lug0zrW_9fMZEwq3lUVnxrt12S3UWAYddPkVJPtR7WN1ZHyOkX10ughtTnTjtwZI6D8PJ2sR040ey2GtDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WBTt7Jt9qp7oVm0mFrkbqfqoCFRcp56a_S0Vi9bTSlc3NZz6kO6hV9P4eHYTFNZf3CB_17-wPPXjxds93zcdL1OGOwiP86FZKl2K7_XHbISuXrEzkmBT9Ysi_E-ugPpHmsbL3D8BnSXNxsVu3aGHvGbeDSzJLDBsw36NjzQeZ1WdvY0k-oX7AokIDupaxGlaTmvaeWL8JqNp-3lwBjG4NJA1JHi-5_CcW6uCWyy0k3pbipb6hamr_Lp9INeQkpvE2tz8nJ19sm69T7aev7-m4X5RrnTll2I_tBWNM9LDcuFLyNo3fBgBf2PjEDp-3j1zJKHhhYOe1vFiEB_lyIYhDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
برخاستن ستون‌های دود پس از حمله هوایی جنگنده‌های ارتش اسرائیل به شهرک الزوایده در مرکز نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/143358" target="_blank">📅 15:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143357">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزارت خارجه پاکستان اعلام کرد «محمد اسحاق دار»، معاون نخست‌وزیر و وزیر خارجه پاکستان، از ۲۴ تا ۲۸ آگوست (۲ تا ۶ شهریور) در سفری رسمی عازم انگلیس خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143357" target="_blank">📅 15:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143356">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کان نیوز به نقل از مقام ارشد اسرائیلی: مقامات اسرائیل و ترکیه برای کاهش تنش ها بین دو کشور مذاکرات محرمانه‌ای را داشته اند. اسرائیل هیچ علاقه ای ندارد تا ترکیه را به دشمن اصلی خودش تبدیل کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143356" target="_blank">📅 15:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143355">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287230e822.mp4?token=BvPteFHUIWOSzbNivMwbNJBHCez1Pqi1oQAiY4VrNWc6I5AYyTdF9G-shFTEPFl8QnMZrVQHMkuca9ZWZ2KPVgH3pj9_akt9KVtEstA-QY1DdYyYEt8BnA6S0EBRb7Sgg3wZ30nUcO5fFVdSC65yAm6di4V0c1zy1aedUrSCAqS21207UPvaZ2oDzj4dN7aU4uVXxsHVMgtPIj460nIMaoYvRaMZBe7-Xcedzp_4NJsuNNPNT7AISUAaTHLD7MOy3dlgHYyoBYM5X6AzbgPynI46BSJZlYUySA9j09WDORaEt12Hjkf1jIX6eI2ZJ9APN_YLzwE1o_RFwe9Hhtog0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287230e822.mp4?token=BvPteFHUIWOSzbNivMwbNJBHCez1Pqi1oQAiY4VrNWc6I5AYyTdF9G-shFTEPFl8QnMZrVQHMkuca9ZWZ2KPVgH3pj9_akt9KVtEstA-QY1DdYyYEt8BnA6S0EBRb7Sgg3wZ30nUcO5fFVdSC65yAm6di4V0c1zy1aedUrSCAqS21207UPvaZ2oDzj4dN7aU4uVXxsHVMgtPIj460nIMaoYvRaMZBe7-Xcedzp_4NJsuNNPNT7AISUAaTHLD7MOy3dlgHYyoBYM5X6AzbgPynI46BSJZlYUySA9j09WDORaEt12Hjkf1jIX6eI2ZJ9APN_YLzwE1o_RFwe9Hhtog0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آتش‌سوزی بزرگ در پالایشگاه الدوره در پایتخت عراق، بغداد، رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/143355" target="_blank">📅 15:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143354">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دیحی کالا از دسترس خارج شد تا قیمتا رو ببره بالا و فرو کنه به ملت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143354" target="_blank">📅 15:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143353">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
افزایش شدید قیمت خودرو در اولین روز از ماه شهریور
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143353" target="_blank">📅 15:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143352">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=K-zdz02QwHTkCdcU-bMduuIh8n4CygIkiKHQnp0zGtdm3zoS_4Xt2SA-cG3NVO8-twdxAVBj0CmWmh9adySXT3GP0mADqklJwEa3mxCQy2t81jF-_qSDpYOp08PbVfY0xes_ZhEdFdRCL6FKQdwsgtoL6w-ocxXqiPeJdp9FTx2X8Jw05Ss7ARtSvSxP4JXJgniOBfZullelZkT0EEq2py6bznlkHeELdOMluQA7wiY_Zyn5GNXw5Cd1pyJFDmfMYLUp2qJQaDmlFFTNNGzZq-d2xvXcgHA-f0d5XF6lYdRMjlfP23UFoE9SQsRCRBk0KQxSY7AEAfMyND1f0Rz-Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=K-zdz02QwHTkCdcU-bMduuIh8n4CygIkiKHQnp0zGtdm3zoS_4Xt2SA-cG3NVO8-twdxAVBj0CmWmh9adySXT3GP0mADqklJwEa3mxCQy2t81jF-_qSDpYOp08PbVfY0xes_ZhEdFdRCL6FKQdwsgtoL6w-ocxXqiPeJdp9FTx2X8Jw05Ss7ARtSvSxP4JXJgniOBfZullelZkT0EEq2py6bznlkHeELdOMluQA7wiY_Zyn5GNXw5Cd1pyJFDmfMYLUp2qJQaDmlFFTNNGzZq-d2xvXcgHA-f0d5XF6lYdRMjlfP23UFoE9SQsRCRBk0KQxSY7AEAfMyND1f0Rz-Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همزمان با پیروزی‌های پی در پی و غیرقابل شمارش جمهوری اسلامی، دلار ۲۰۰هزار رو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143352" target="_blank">📅 15:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143351">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
کارشناس صدا و سیما: الکل قاطی بنزین میکنیم و مشکلی نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143351" target="_blank">📅 15:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143350">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143350" target="_blank">📅 15:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143349">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
پوتین: ما در حال حل کردن مشکل سوخت در روسیه هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143349" target="_blank">📅 15:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143348">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee3b1ebd9.mp4?token=fCXGmROLE7SJ-WYmaRXPVz_Fisg2hsO8yR4kcjJLBK3kYxM24R93V4uIDIj5IP-JtjKOH4KIa1ZPZ2PdfxBlRyfDQVwL931--2aT0J5iWZNF9ReQNb5wvo4qYd8xUFshfJpxsTLqkd6lF8xjefm7llp8Ni7xckw8qtsyvYJJvcUGCnte8LNLGQ2Hjoa2xpM4V6YfkVO-XQWQMN-bNVPNdPqx5n1XKFFBr7ftfEZOLg4FDZM0Pn3k4-EImt05kA3U4Ct-ytQNge1CJ657YArFdkqFsHGVDrgs-XBVGNQ7OMcA3aX80SbZZS0iqsWtPrNkaThmP6dLPO6iJW4BIgk7T0NXppDbZ115arLC5g9upjyR3xpV4qyXuxch-w6MD3IERrss11h0pkJ4MPzl8Nxf442qZ-VZqlQ6bDVvdXV1QBX28Mi8KvJ7lSYGzQTClfXBo8ndYQvWZKnkRr-bMkU2U8QsJ_6DFUDTb3AmOIj-g7YypR9vyTv8GP539R2Wu-juGiS-o6NOLxnXX5rWK3jUS9DNiu__FKzX3G2S816Tf6oQz8wQyKD8FGdeCZQFKj7x7GnLnIjcNpcZ7sPKvGyQ8nOYGu0aXl2dG6q-7PRn0ILBH6N4ou9HvpvJ2gB_M63DTD4Rue65bhqu2sXzfEyyQvdjMCzuGyj9h23ILXhUYR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee3b1ebd9.mp4?token=fCXGmROLE7SJ-WYmaRXPVz_Fisg2hsO8yR4kcjJLBK3kYxM24R93V4uIDIj5IP-JtjKOH4KIa1ZPZ2PdfxBlRyfDQVwL931--2aT0J5iWZNF9ReQNb5wvo4qYd8xUFshfJpxsTLqkd6lF8xjefm7llp8Ni7xckw8qtsyvYJJvcUGCnte8LNLGQ2Hjoa2xpM4V6YfkVO-XQWQMN-bNVPNdPqx5n1XKFFBr7ftfEZOLg4FDZM0Pn3k4-EImt05kA3U4Ct-ytQNge1CJ657YArFdkqFsHGVDrgs-XBVGNQ7OMcA3aX80SbZZS0iqsWtPrNkaThmP6dLPO6iJW4BIgk7T0NXppDbZ115arLC5g9upjyR3xpV4qyXuxch-w6MD3IERrss11h0pkJ4MPzl8Nxf442qZ-VZqlQ6bDVvdXV1QBX28Mi8KvJ7lSYGzQTClfXBo8ndYQvWZKnkRr-bMkU2U8QsJ_6DFUDTb3AmOIj-g7YypR9vyTv8GP539R2Wu-juGiS-o6NOLxnXX5rWK3jUS9DNiu__FKzX3G2S816Tf6oQz8wQyKD8FGdeCZQFKj7x7GnLnIjcNpcZ7sPKvGyQ8nOYGu0aXl2dG6q-7PRn0ILBH6N4ou9HvpvJ2gB_M63DTD4Rue65bhqu2sXzfEyyQvdjMCzuGyj9h23ILXhUYR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک کارنی، نخست‌وزیر کانادا:
ما آماده بودیم و به توافقی جامع نزدیک شده بودیم که برای هر دو کشور منصفانه باشد.
🔴
اما آن‌ها تغییراتی ایجاد کردند، از جمله تهدیدهایی علیه زبان فرانسوی، فرهنگ کبک و فرهنگ کانادا.
🔴
این قابل قبول نیست. این هرگز قابل قبول نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143348" target="_blank">📅 14:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143347">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
عارف در مورد قیمت بنزین: اگر مردم مخالف باشند اقدامی نخواهیم کرد/ ما ملاحظه زمان جنگ را می‌کنیم/ بعضی اقدامات خوب باید با تاخیر انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143347" target="_blank">📅 14:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143345">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35f6e38e93.mp4?token=rnE9eKmnoWr8y7yUq78X0GDU34_xw143BrWsHy4yplAoqeDqInRaRyRFijTuvHAaPn5_CkUz_KYDd1Rpv3t-a2vetBRb_9AKdEKG3aFpDdMJ9KRS57ieQI1E2SN4GersakCHwWySvWhMXPIUVi20FGtxD4Gzd3xatVeyOp2uJGY4DpEqzos1PDQwHiHkW0l1aAspli0oMCUUO5f1S8Jbmq-DKVViYfH1YZ0AMj_Dh-qL7zp8Xt2Ca5bssP8YFzA_kbPiMz9B4LRlyO7P9bhXI7RBcx4UQ13TqvWUOMgojCsktvdnoAJJzJb8J-TmjfLmb882oUuL3pGar40geaAa0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35f6e38e93.mp4?token=rnE9eKmnoWr8y7yUq78X0GDU34_xw143BrWsHy4yplAoqeDqInRaRyRFijTuvHAaPn5_CkUz_KYDd1Rpv3t-a2vetBRb_9AKdEKG3aFpDdMJ9KRS57ieQI1E2SN4GersakCHwWySvWhMXPIUVi20FGtxD4Gzd3xatVeyOp2uJGY4DpEqzos1PDQwHiHkW0l1aAspli0oMCUUO5f1S8Jbmq-DKVViYfH1YZ0AMj_Dh-qL7zp8Xt2Ca5bssP8YFzA_kbPiMz9B4LRlyO7P9bhXI7RBcx4UQ13TqvWUOMgojCsktvdnoAJJzJb8J-TmjfLmb882oUuL3pGar40geaAa0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نفت: برای قیمت بنزین تصمیمی گرفته نشده است­
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143345" target="_blank">📅 14:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143343">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XkX4iVr5D5Fd8UQpkYJHKRzKYhlMJVYlMVYCqa9JB6V9-lonJCndK6TAPmI_f35sB604jEZl-w-jpyaXqNhGd3w6UzK395VQagCRPoEc0W3EJs7mY8aZX-B9kaUInfb8KtwqPzZxpdgoEiPVZR1ZTBp8WDTngZqwdsp-uVLHc-WwpkWziEiNEH7YDHAFkqLT3lwjl61UtAi9sgVniZGhMnpWSxOOGQMWuRpCj1QxrdQbh8X_Uw8HRh2KKZOAXFODoEqEH7pfohqWfEtjSYLqBYrcGpHxe0701g0C3xmu5M52UKHFUyuc83TqoQaGm2vut28gu8WkrLY8Cp1Nqh92DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFz50aYxDjQ884uCrO7_mGnXJ1scw8lXWxrUvjmrMSGMeUO3b35Ev56xp4g_DSKYJdSoKTT5Pa8Smfh1D_Jvl8bOo_F5v6S8_dBzuBFHVtk5uo2VSe20Udvot8PXnWX1GMRSmpaFQoywwvVmmH-Aohdfd2IWg0ew5ZYFYJRvyeVwq_gY3-dgoAfaCSNU6y-hTFsmeUr052ZuFnDc_AwtWV6bo5Z7hNj9FrMwANNByOpRHRBy-FUsY42ms5VyJenynCTecFZB4omChFNt6x6ixPFPdgizMSZbPgWj4cDlmfMf-FD0JIbtXBMLngoC4ygx_pklACej4yAgO_ebK13a2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که همان سه کشتی متوقف شده در تنگه هرمز حضور دارند، و نشت نفت از کشتی Minoan Dignity همچنان ادامه دارد. به نظر می‌رسد ترافیک کشتی‌ها در تنگه هرمز نسبت به دیروز کاهش یافته است. همچنین، تعداد کشتی‌های موجود در نزدیکی فجیره حدود 10 کشتی کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143343" target="_blank">📅 14:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143342">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoWOmVvKE08ZrWOrH3ek__3v5QC5FShxpqM0ZshTkLWAoaHGootxSPWciK-Hw3HT5556lxRaIZYWgfu9u3Q4B_g2rqlrA9-pRcIIPP_OLv9vyCMIrO16whUhXyG0TOkjH5Nx1RWXcC1nsBEGdsvuzcvB8KbTQOA3BUwwN5KTq67D8eoc2dXMwU8kATB-FpRjQMOAqYA20XaXB0xkR88mxqRqU6Ti9MhQlH2VWqHybeWLn5dSMvo_vKbymC8oPiQrj8jWurf9hqJ-iQZXuFBDTCcrbfx722PpmEXtpEXEUaq1afZViFbTOfxCCJubAtQoeQUmI_gsP-035XwwHgmmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آبفای تهران: ذخایر سدهای تهران ۲۶ درصد است
‏
🔴
ذخایر سدهای پنجگانه تهران حدود ۲۲۰ میلیون مترمکعب کمتر از شرایط ایده‌آل است و میزان ذخیره سدها که در ابتدای تابستان حدود ۳۰ درصد بود، اکنون به حدود ۲۶ درصد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143342" target="_blank">📅 14:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143341">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عباس عراقچی، وزیر امور خارجه: آمریکا راهی جز صحبت با احترام و مذاکره عدالت محور با ایران ندارد.
🔴
اینکه بعد حمله نظامی دوباره رسیدند به همان راه قدیمی یعنی تحریم های اقتصادی، نشان از استیصال آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/143341" target="_blank">📅 14:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143340">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
روزنامه شرق الوسط: قالیباف در سفرش به عراق از دولت عراق خواسته تا بدهی ۱۲ میلیارد دلاری بابت گاز و برقی که ایران بهش داده بود رو پرداخت کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143340" target="_blank">📅 14:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143339">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
هر یک دلار رسما 200,000 تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143339" target="_blank">📅 14:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143338">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: رسما گفتیم دو دیپلمات متخلف فرانسوی باید ایران را ترک کنند
🔴
سخنگوی وزارت امور خارجه امروز با بیان اینکه رسماً اعلام کردیم که دو دیپلمات فرانسوی که مرتکب اعمال خلاف شدند، هم باید ایران را ترک کنند و هم امکان بازگشت به ایران را نخواهند داشت، گفت:‌ اقدام فرانسوی‌ها قابل توجیه نیست و برای تداوم روابط ایران و فرانسه مخرب خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143338" target="_blank">📅 14:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143337">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaG4nanxh3tXv7xSwaO4KSNQi_vOWpSm8TJAnvv2j8ZbYiA9L51yqV2nzlcZS3emvGnH0JIPdVC7kCm8kEPsK9ATAX5e1NiXbHJ9PrCUxg6y--cRZDhcaMdeSXlEAbtNiGdJ0vN4sn8Bb8GQBW4XyBp-DLP0Q4AfkQaZzMSgi4q8YtpgWW6eUL5MyFR6xqM-evXQ5G7ZXeUvLDXfYxPXYTQRmUF1jykJQh5zxIVdQYacVAfbzThisBqUjX5buvTUNo0sfgtikPe-Vgcwiqu05YqlESYqFP4h8V82d1Wmt5UkBPHpdNWuda1eKf_p7y534I4_TfFdoUy5IX3z-hpEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق پیش‌بینی این دانشمند در سال ۱۹۶۰، دنیا ۱۳ نوامبر ۲۰۲۶ (۸۲ روز دیگه) به پایان می‌رسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143337" target="_blank">📅 14:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143332">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1rGx7MQxpB4sCg6ruCAyGb0XmAV1iWS3mi77VB3IcAnPFynmmBoOQqwQWnuKj8egGPy2QWu7z7JnApbdUag00tLN7l5GSbe4fBLYpdt0brXJYQvhIal0B5X7TKouTphLozmivJ5Xf_RoC6mRvGXYG7PJ43SMBP2oJUhBlOVzuSXJQsaVbQMAPv0sONF3yoFBTmpCZp94v4omLdk7uKXyiht560753sgimCj_VigwN2YaA4SJqwREfHQE3yFMARLH0lW3zPCha7RDgYGJXHGSe9NxcQXgJYhukwXCLlAtewqLjUdq0KzbVeoJML__zTvS0tmMKStS-CFXZlOjgVzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rp0vFXBlWJ_0CAZGVwh7EmeyT3KQDjN337PvWQnYlaK3XgvIG9c_5cKhohtRrsk8fraPIa2NrTPyXJ3ZytJ9lYtGy_sJppTpt00uevVJ6oW6pNLdhQvVsOmbRzcKuraQAXP-SU1q10h-vDEiM1CgwdygMTP0wAbqBJmxBhBmn8MmgCDSrbYcD2JZSLS1DDFdtfoSyJCKdo0ks123_F2PDub-WgJoP0zWChruvYqVF-umAbj9TK11VmLfTg2MGfPfjAigARPQzl6Zj3S4IGX9tBWav23P3K0wQTSHwZRJ3TDhGsLYqjA0HZRxFYKdDPX1nQNXiNcRTHByE80TeAghkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oK4Vj_7G3-6DT9ZcrlnoH754Xx_3yzS0TmC_0rUJSOZeg2roGUf-OZUxbew60w6_WqBgu5RoVOkqK-KaZ-k9oS6Tmh9fGqz6sfr-hzdzkwQIE0htfD4DCWYWOL5zF3ttUine23XS-s8yJXSFFnGHIBnwhacMWYczv_SFE9UbP2XkCgxwkgwfKNEaU4yNy13fRKivDT-Bljpc3TDRV281qTbO3-U5DarRDxrJ5G7fpbYbHnk3y7mcMgIW46d8Ccwx7_72s1TyryTx8TwLxi43_PgmklLH0VMT8KI1DLbMPtyE7R_kvQt1Sr3x2q23MsRes3OpE1jxDeQfzMdX_sM4fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDmqLEmg4m7G4VoylKnnMxwF_Q14nbzTkT2HY4-Bmx4_CbBrEzYxLyNPbE5yDjXL4vhjalT6UQpH4Vo1H3nB_b1a-9eEfzl0F-mkjJhOvt9hGVU_97CaMzHcc0ybgO_btN8fgdm2hg0cI5qOBlgE7HCA2qDAVkY8fJyXYgjto5YODsFzOQ2nkbaYEx_ZdWyehHOjOcKnJoAm_nIl4ARzBbNvxeGaqWMgIjWUUBJrzzq-3ExcIewldANghLK12-aEMw4AhryDLbvTZLRtd0lTBYccpnXpVlXRYSgH49d1kwN7F7GnJGWyu5czKL_1NtXreuT1yr1Z27A4bEjH78h24A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569812a8b5.mp4?token=YWhtecANFouJOro7sohJ0HFFAr6tdXfR3D-0XtNLFpO5S6PMktj20gpLlYvmPZR6RauNccoLYoZjWVrupLdNaW_ow1Bczhy2DX9ZAhSJMepPeFwmQ82DMRIDp6IYlMU6dy1c__nUZbkUigWmzFUQIElgphti0vSOVkIVR_y2sjevb-DO0KMTgfYDbvTD5J65MY1L3Kq6y2QW_6dHrbSX5CrZycKqaLSAHXiRFlFjzppKOSaujKq9FTlUMVZEYjMzjLCXMTHCnnhWrd1X5BmDR1qg8TeeI_3Q5-48Sds6u3AOYcrXPJVFZEP2XVM8QSLU3SvygxlPNVeRsVOwq-Y1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569812a8b5.mp4?token=YWhtecANFouJOro7sohJ0HFFAr6tdXfR3D-0XtNLFpO5S6PMktj20gpLlYvmPZR6RauNccoLYoZjWVrupLdNaW_ow1Bczhy2DX9ZAhSJMepPeFwmQ82DMRIDp6IYlMU6dy1c__nUZbkUigWmzFUQIElgphti0vSOVkIVR_y2sjevb-DO0KMTgfYDbvTD5J65MY1L3Kq6y2QW_6dHrbSX5CrZycKqaLSAHXiRFlFjzppKOSaujKq9FTlUMVZEYjMzjLCXMTHCnnhWrd1X5BmDR1qg8TeeI_3Q5-48Sds6u3AOYcrXPJVFZEP2XVM8QSLU3SvygxlPNVeRsVOwq-Y1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به مرکز نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143332" target="_blank">📅 14:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143331">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHtaKQnDqxpeKV6wFAFoDOkK05YBHzsQ9yxIFdeKsOznVuJgXYqJEjDkZc5vO-5CpITF3iNg3ADw4TjwCujXPiLlf1DEibgGfaWrzqOZwlWbSMvsNu_KX5SuFwprAZnH5xYFC_m5NtE3k6f_brdvWtzSlGmyzo2U0FRZ4iiQ8ANPO0i3xP8x8n6jrVeZqwkbFxEQ1doCj3NnRf75slevmCyHaLG9XbuA0lHqNuRHVG3Vg7uRIsvcxvbrdPecyl6VS3jXAWldSf8xzRQtkzH1W6n26eTmQ86XLYD5cD-Bi9CSpYJd6pTUaJhLqogBEsUjKpInsAo8ucfpsX1TdblWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هر بار که صفحه رو آپدیت میکنی، دلار میره بالاتر...
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143331" target="_blank">📅 13:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143330">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
زلنسکی: پوتین نمی‌خواهد جنگ را پایان دهد؛ او منتظر زمستان است
🔴
ولودیمیر زلنسکی رئیس جمهور اوکراین گفت: وزارت دفاع اوکراین از کسری بودجه ۲۷ میلیارد دلاری رنج می‌برد.
🔴
وی گفت: پوتین نمی‌خواهد جنگ را پایان دهد، بلکه دامنه حملات خود را گسترش می‌دهد و منتظر فرا رسیدن زمستان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143330" target="_blank">📅 13:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143329">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سازمان هواپیمایی کشوری اعلام کرده به درخواست عمان و شرکت فلای‌دبی، ایجاد یک مسیر هوایی جدید در جنوب کشور در حال بررسی است.
🔴
هدف از این مسیر، بهبود مدیریت ترافیک هوایی، افزایش بهره‌وری شبکه پروازی و پاسخ به نیازهای عملیاتی پروازهای منطقه‌ای عنوان شده است.
🔴
این طرح در صورت اجرا می‌تواند مسیرهای عبور هوایی در جنوب ایران را گسترده‌تر و روان‌تر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143329" target="_blank">📅 13:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143328">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23dfb6270.mp4?token=U1ohkb8P__FIw0c-41iL4I0MxefffXciJlGRvd2Ak3ijXgzejRsibUV5K60O5vYfECemFypkLmvQJPTQNboSDk9ZF2v2yhDuT9qj_3smvqBq5L0J4Wm_E53OAjRZfbcNveWokHSZLBnp6p4ntGDebyBKhmm40w_LOpdPj3IWgyZH0UJTVClxDoDaif0GrjbOvbPQ21ZlssTpNJWc4lzv3dlAMrFkgQqTtg_9K03ul-WaIpuSVuJmpothMeH1fb3NhvBTE2uwBilI0k0RSZuyEa1PkVNqE-YtFsmmitEzCqgVWLL9kkf-jYo7LZMU47x-ZsZRxGs1d1MlgkhKX0IkP57YoJc6Z484wQgJFgGYumfRpHTzjneRHua9d6uj82H4SBNbLnyQf6KUSLVoP-iT2ulyr8q5zrusenTDpEa72RLYQ2agr_-Tc8XJxF5uaL73825qptuStPRuZTOHyoPkbnF_pqtXNq1VOBsIbaXeV874rUplXS7ct0kS2NWCLEmHOiqXDH9CZ0QxoA5JW6nNn9NVj35AKfBxHbL2djT7FU7VzPhRlrWJB8UFRG6v17CwhKS3MIQh5oLSca8X_-5kPSREcWOPGmFpCAVYZ_R6VfFNqgi9YXZLiK7celXcUdn__qDOW_i1nYAze4GhTONRTImwnPZNI9hZnof_JCyCMCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23dfb6270.mp4?token=U1ohkb8P__FIw0c-41iL4I0MxefffXciJlGRvd2Ak3ijXgzejRsibUV5K60O5vYfECemFypkLmvQJPTQNboSDk9ZF2v2yhDuT9qj_3smvqBq5L0J4Wm_E53OAjRZfbcNveWokHSZLBnp6p4ntGDebyBKhmm40w_LOpdPj3IWgyZH0UJTVClxDoDaif0GrjbOvbPQ21ZlssTpNJWc4lzv3dlAMrFkgQqTtg_9K03ul-WaIpuSVuJmpothMeH1fb3NhvBTE2uwBilI0k0RSZuyEa1PkVNqE-YtFsmmitEzCqgVWLL9kkf-jYo7LZMU47x-ZsZRxGs1d1MlgkhKX0IkP57YoJc6Z484wQgJFgGYumfRpHTzjneRHua9d6uj82H4SBNbLnyQf6KUSLVoP-iT2ulyr8q5zrusenTDpEa72RLYQ2agr_-Tc8XJxF5uaL73825qptuStPRuZTOHyoPkbnF_pqtXNq1VOBsIbaXeV874rUplXS7ct0kS2NWCLEmHOiqXDH9CZ0QxoA5JW6nNn9NVj35AKfBxHbL2djT7FU7VzPhRlrWJB8UFRG6v17CwhKS3MIQh5oLSca8X_-5kPSREcWOPGmFpCAVYZ_R6VfFNqgi9YXZLiK7celXcUdn__qDOW_i1nYAze4GhTONRTImwnPZNI9hZnof_JCyCMCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید آجورلو: چین با کاهش تقاضای نفت، مانع افزایش قیمت جهانی شد
🔴
چین بر کاهش قیمت جهانی نفت موثر بود؛ چین در نظام جهانی نمی‌خواهد ساختارشکنی کند و اصلاح‌طلب است
🔴
چین می‌گوید جنگ آمریکا و ایران برایش بد نبود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143328" target="_blank">📅 13:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143327">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نایب رئیس مجلس: هر کسی به اقتصاد ایران حمله کند، اقتصادش در منطقه هدف قرار می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143327" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143326">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
حبس مهریه بالای ۱۴ سکه حذف شد
🔴
نماینده نجف‌آباد در مجلس اعلام کرده طرح اصلاح نحوه اجرای محکومیت‌های مالی در صحن علنی تصویب شده و بر اساس آن، مجازات حبس برای مهریه‌های بالای ۱۴ سکه حذف می‌شود.
🔴
برای مهریه‌های زیر ۱۴ سکه نیز امکان اجرای حکم با استفاده از پابند الکترونیک پیش‌بینی شده است.
🔴
این مصوبه برای بررسی و تأیید نهایی به شورای نگهبان ارسال شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143326" target="_blank">📅 13:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143325">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرگزاری فارس: احتمال اینکه ترامپ پوشک میپوشه وجود داره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143325" target="_blank">📅 13:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143324">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlhfs89j9or1C7zFMIBs9lfH_-3179LlYshlfnmBxIu5tYlgsMpaKXYMus1FUpkVL13zubrj96ATuS6Xg1iF-YlRTTMcp6wBjZVGC9wUIzIhZwis2YeheFc0QSvazUFJWRJf5C9RjtU_l5Wb_hmbJGqzC-5PKU0SAA_b163OS5H_EmBv-q-VQdkAQFc3Trv0vcSHqSvgRm6HPYLJknPXxesHGHTSyn4NEMJuAmEZEv5cX4qS6nw2Jl5_ErMLQLEvyeGIk8pL06eTg2jvN26CY1DAgKI_aJ1JGaRdzbtbc3RN1dSBIcu1JHVafIEaDbSawd9YH2MDXs5TvGnsUQvC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با رشد ۸ هزار واحدی به ۶ میلیون و ۷۰ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143324" target="_blank">📅 13:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143323">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مصرف خانگی گوشت بوفالو مجاز اعلام شد!
🔴
‏مدیرکل دامپزشکی استان تهران: گوشت بوفالو از کشور هند وارد می‌شود و فرایند کشتار آن در مبدأ، تحت نظارت‌های شرعی و بهداشتی انجام می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143323" target="_blank">📅 13:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143322">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فایننشال تایمز:شرکت‌های انرژی بریتانیا در حالت آماده‌باش قرار دارند، زیرا هکرهایی که با ایران مرتبط هستند، یک نیروگاه برق را از کار انداخته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143322" target="_blank">📅 12:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143321">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
گزارشات از اعتصاب برخی کسبه بازار
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143321" target="_blank">📅 12:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143320">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سعید آجورلو: آمریکا از مسیر جنوب تنگه هرمز تا روزی ۹ میلیون بشکه نفت عبور می‌دهد
🔴
مسیر جنوب تنگه هرمز همین الان دارد کار می‌کند
🔴
عمان محافظه کار است و با انگلیس، عراق و آمریکا طرف است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143320" target="_blank">📅 12:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143319">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeTD4PTkYv_rAZhj_54QMmarqbGTA0w3wqMb_ez0tgNcDGnA358WM9_mGwpUhAJXiNfoW6dgejpeIUVZi9-GplXP6rOcp4Xct4il_HutZqUM2WMpRaOSbmhnKLLGjmeZnHNNAnuMO41sR338wV3MsoqGxXODvPWFz0qHfXPjPdVrz_ivo9gXz4c6bE74ZmihznHmpLuyolRcPrA_V6gsbHbsQNbh_k-82jNyB88nGz75izZVtXOMJDJM52GnrVvmikketqpJdjaUJlFFCNKDuiCEaE7Pekb9fzAojKxccjUQxC71xdV6-E7EWZWa1pEfvPcNOwAL_bTwhKgv3aPauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موسسه HFI: بررسی ۲۱ روز اخیر نشان می‌دهد نفتکش‌ها همچنان از مسیر عمانی برای عبور از تنگه هرمز استفاده می‌کنند و ۵ میلیون بشکه نفت در روز از این مسیر عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143319" target="_blank">📅 12:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143318">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaEw_puR_y-1qsjeKf0YZe3j0mCM-TKKU65U9BZ4Pei6SL6MVfqOZp7QVF0Oa6Z8JeWAzZnIQ8ewLPUOWoBVJzlercUzN8qT9-bpW5QaPXOtbv-EZ3ou6GC_w1a9WL8i0jMHLE5d5fBeC8SxILcwHapQEkuzFFzc9MWKuOhNJdUDdxd6ikxUhrFQMJ3V1qRbBS6kaidUVEBH8sqbSyD53f94W16NZxpSTOndqP89mMhjvgOqv3Tvlv0Dw_CEvoB6g2JCkOLXWebDAvZXy-STKBzsgwnJklOzIPtAVmlx2eWVLFs-vXutSwDAfNX3cOsUAdXJ7MJHI6hcCR7P78QydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران و روسیه در آستانه امضای توافق‌نامه‌ای برای اجرای پروژه ساخت خط راه‌آهن رشت-آستارا توسط جمهوری آذربایجان هستند. این پروژه، یکی از پروژه‌های کلیدی کریدور حمل‌ونقل شمال-جنوب بین‌المللی است. طبق گزارش خبرگزاری ایرنا، انتظار می‌رود که نمایندگان تهران و مسکو به زودی این سند را امضا کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143318" target="_blank">📅 12:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143317">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_Aee3PzPhgaeeZ4WXpb0VuDEHaY5RGB7kedBzi9f__y36sjE6OanxmCGPDleiE31zNE1IjtMFM1Jmz0qycsz_EjLPTDRi0C1pwFPRiUKFxq3tB1Gj-jwyttDPkMX3LcP-ywTTvylbFgiiUJLn1zu8YvK-_YW2As6AMtKA8-bgBe3UxETGQejlAHRIbOSGXGfME_3y-zj6HX-YXFEW_xvnTAg9dtrrZoUrvrB5oTzJEXYr_aoCPttolH-CCMgT8tSTAy0a28iVT9LxslTf9vWvudIU3zewjyJK_aGS1Pu7L_wyhxYH7o6pHE2UZ-_ulJTei3EQ5nEHwfJmDzeLP5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات ارتش اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143317" target="_blank">📅 12:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143316">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عوستاد خوش چشم: اگه بخوایم توانایی ساخت گروه نیابتی تو آمریکا رو داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143316" target="_blank">📅 12:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143315">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558651d0c3.mp4?token=N8SfQzlTH7O4QSBH6CaK26dEDCvzGGJxmNCBx5fOngdySfTlTLpMofHOfBXQsgiegtrNtLQPcnA_cGUmlmaDF_G-R4sDojmD4v_U8trn-LVYPhsm-2NjSw3w9_ZQsMYZlFiVbSXCthHFAcPU6_gzf1g_Ce2T8DsAXhvSlpMv25CsAmVtzVnmgxKhydC6z3mc-THQOFytqVCBkMqIrpJGn7BAxqjrIBPw8EJ2uiQ3HHCh1YuDSOJvttqDruW7pa9Dr9zCSHsuV3OHhTd6SBR3olkuwe95n1LuTmmenf-F8OmHgTUUIX2doElvZJMaFUsIbc3APIBeH-3TdZ4_mra5WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558651d0c3.mp4?token=N8SfQzlTH7O4QSBH6CaK26dEDCvzGGJxmNCBx5fOngdySfTlTLpMofHOfBXQsgiegtrNtLQPcnA_cGUmlmaDF_G-R4sDojmD4v_U8trn-LVYPhsm-2NjSw3w9_ZQsMYZlFiVbSXCthHFAcPU6_gzf1g_Ce2T8DsAXhvSlpMv25CsAmVtzVnmgxKhydC6z3mc-THQOFytqVCBkMqIrpJGn7BAxqjrIBPw8EJ2uiQ3HHCh1YuDSOJvttqDruW7pa9Dr9zCSHsuV3OHhTd6SBR3olkuwe95n1LuTmmenf-F8OmHgTUUIX2doElvZJMaFUsIbc3APIBeH-3TdZ4_mra5WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی جنجالی صداوسیما؛ نقشه ترور بارون ترامپ!
🔴
صداوسیما در اقدامی بی‌سابقه، اطلاعات محرمانه و مکان‌های دقیق تردد پسر ترامپ و نقاطی که در تیررس است را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/143315" target="_blank">📅 12:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143314">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7qcgbVLKserbo1YEBqEiN3zmKZ3wm6qllTfvpW1BdCGUGxQImXGN2g65qJZtFMqyThIsJy6WH41Zss3c2zbu_ViuXIEUgBB9T2H1-VbSmXJgcwwmZVhbYLgCjAEGhWJN4sz019_-IN5xF5Pmphti1v-4IUstTdOPIu_OUGvIhUcLxBwMSo4D_6YVwueljc57Kidab_1UuM0Tod-guJeaaNOE68dMfTU-A8r1rxAVpgFu87vwThhdEScWnWykfNpg-7bXfxhaFXDF4lzgXhiyiv6Ruu1689MZLSKCTSlW9YbBuUBwp9RLifoFXrGSNzplxcw2iC9i8MKqBX3UKBMyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک‌تایمز: نخست‌وزیر کانادا مقابل ترامپ ایستاد/ تداوم روند کاهش وابستگی به آمریکا
🔴
نیویورک‌تایمز در گزارشی نوشت: نخست‌وزیر کانادا در حالی از ادامه مذاکرات صرف‌نظر کرد که کمتر از یک ساعت تا ضرب‌الاجل اعمال تعرفه‌های جدید آمریکا باقی مانده بود.
🔴
پس از اعمال تعرفه ۵۰ درصدی آمریکا بر ۲۰ میلیارد دلار از کالاهای کانادایی، او نیز از اعمال تعرفه‌های تلافی‌جویانه «دلار مقابل دلار» خبر داد.
🔴
کارنی با این تصمیم مسیری متفاوت از دیگر متحدان اصلی آمریکا در پیش گرفته و حاضر نشده توافقی را بپذیرد که تعرفه‌ها را به‌طور دائمی وارد روابط تجاری دو کشور می‌کند.
🔴
او همچنین تأکید کرده کانادا در حال کاهش وابستگی خود به آمریکا است و این روند را ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143314" target="_blank">📅 12:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143313">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=nAva8siPwPrdvMgljeH0bO_IC3Yi_BBov_OXfJTfRUQ1XsEO363L3mUnZJdRVCGmxFYf4yKHTLqvRWy-wLsrVv-J1M8lR6e0d08nDhaRQuxNMskf0rwicP2-ygiQs283-zaKvcaI8YmXOnIvoe7qxAgHWMtTMKHC5IocvX4Z1mgAJWZTO-Acc2wjFIlXQK_muX6DHXfZcmEfYzBDNCxqDsg8QApJ1HnvWwR5ivxgnaoI1yKsQfYNzUahRf_oH4pemdskzMjXnoldJdZvCuG3_UM439PEuAGAUHbp3-NeVZ8Z2Sn6cIDSE4a5U6FLi1vbvQ8sQSNW4zz0gPGD87CkTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=nAva8siPwPrdvMgljeH0bO_IC3Yi_BBov_OXfJTfRUQ1XsEO363L3mUnZJdRVCGmxFYf4yKHTLqvRWy-wLsrVv-J1M8lR6e0d08nDhaRQuxNMskf0rwicP2-ygiQs283-zaKvcaI8YmXOnIvoe7qxAgHWMtTMKHC5IocvX4Z1mgAJWZTO-Acc2wjFIlXQK_muX6DHXfZcmEfYzBDNCxqDsg8QApJ1HnvWwR5ivxgnaoI1yKsQfYNzUahRf_oH4pemdskzMjXnoldJdZvCuG3_UM439PEuAGAUHbp3-NeVZ8Z2Sn6cIDSE4a5U6FLi1vbvQ8sQSNW4zz0gPGD87CkTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هر گرم طلا در آستانه 22میلیون تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143313" target="_blank">📅 12:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143312">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=EI7GGwFH5v15MJtMXmGGEVsnuH5zn8TbaDWIv9ehIk2pVfUiRC18VARzNdWiUyL9IxhKbICzwtakhAz3ujIID2ckUHCbBQZ30-0Es-GiozFGSqUMcCOxu1ybMBLmlg_lWqah2XhPk99N9xBUPbII6xQLzTd6H424iZ1LJpySz8LxZyRWbVtE7uKZ-Yft_uWg8mEsI2rTJ2lzIFRfX4cPkz54UAOxqELNLmE4KFh5t8lRRUoODC0e4jU9ybwbW0TTfIj1SspDVPI-azRG9N1XHZtAYIlr-DgFRJz17ywon2Az1NhQ2fM-Cmf_8CtIe5MdKkcPriRA1eFrjhmfM4og_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=EI7GGwFH5v15MJtMXmGGEVsnuH5zn8TbaDWIv9ehIk2pVfUiRC18VARzNdWiUyL9IxhKbICzwtakhAz3ujIID2ckUHCbBQZ30-0Es-GiozFGSqUMcCOxu1ybMBLmlg_lWqah2XhPk99N9xBUPbII6xQLzTd6H424iZ1LJpySz8LxZyRWbVtE7uKZ-Yft_uWg8mEsI2rTJ2lzIFRfX4cPkz54UAOxqELNLmE4KFh5t8lRRUoODC0e4jU9ybwbW0TTfIj1SspDVPI-azRG9N1XHZtAYIlr-DgFRJz17ywon2Az1NhQ2fM-Cmf_8CtIe5MdKkcPriRA1eFrjhmfM4og_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 198هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143312" target="_blank">📅 12:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143310">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8loA-qecLRRMGWIw_ANGVlb-KbqNuv266XuDS7Ls--0wtKnsyfEsA3cIfaHazn5fHjUjN49WT_E9yzDyg2Z5BauEq7E--VFCFIKfVnLalZ7UNzazvy7BnrV7Q_-0sVc8HyAPJo4lC58moFXn95sD7MutPMcXKTs8AjANrM3v4B74-HBUP8XEew-_JLBhVWs6K0zswQKGa5XWUwTeMZ5q-hN2paQOlv9hGfLpiAp0eMrv2Kxk0VBoVC1eiyth7Wvyg9Nh0hsRhF5f4JA3icRZN2QN89l72p0b7iH0_u-wdy2hDMdtOWrgog9TV73F6ACvtP94WdM9t8a5-YASJHUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMtelmVaOmO4GjjgbrUUoebSgQSw8-WG_1S2Ho9jFcd7-jP3Hp_5VYqGrDm1UlPo9q59n8uDy2-64XixPExPq8uBk6SNs8HzMLcPJrxhVwIUNBxq2N2STL3o3LGUh3gauMESxirVEaJ8A7Mrl02h9NXE5qrSNNANECtc2p-SNoZ7WT1OiW40yVXW5GpqwOlI9hrV-IIsGGUQ7rdq5aqu459ylj03Fb_R6YcfFipeMqmVMuuGvAzxLnpbbVZal44j45ZKQZpbZoIXFTXWOh901OutLnKQ0VaK6y1YFB9fhnyXqWcE0BlU-UgmdtIHg44AX61k9vxwfz_9EBptCJW_aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در طول شب، نیروهای اوکراینی به یک مرکز لجستیکی در کلپینو، سن پترزبورگ حمله کردند.
🔴
بر اساس گزارش وزارت بحران‌های فوری روسیه، آتشی در ۸۲,۰۰۰ متر مربع از انبار ۶۸۰ در ۱۲۰ متری رخ داد. همچنین سیستم FIRMS ناسا نیز نقاط داغ بزرگ آتش در این مجموعه را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143310" target="_blank">📅 12:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143308">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
زلنسکی هشدار داد که برگزاری انتخابات در دوران جنگ کشور را از هم می‌پاشد و آن را یک «تسونامی» بالقوه برای دولت می‌نامد.
🔴
هیچ شریک غربی تضمین‌های امنیتی مشخصی برای برگزاری انتخابات امن در سراسر کشور ارائه نکرده است.
🔴
این بیانیه زمانی مطرح شد که فدرور، وزیر دفاع سابق، به‌طور عمومی خواستار برگزاری انتخابات شد و استدلال کرد که دموکراسی «نمی‌تواند گروگان روسیه باشد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143308" target="_blank">📅 12:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143307">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">تو ایران حتی نمیشه مُرد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143307" target="_blank">📅 11:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143306">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143306" target="_blank">📅 11:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143305">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
قیمت هر سکه طلا با افزایش ۸ میلیون تومانی نسبت به روز گذشته به بیش از ۲۱۷ میلیون تومان رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143305" target="_blank">📅 11:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143304">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a338f70a64.mp4?token=dxEp_rInFA8xOPnhnYJa-Y6dlrKWl8bopsKVNokCLrsDXa87urrG7gpXqunvbtSjJf6ThP1ZilvMEmmR9YTtoQMKcFcVYQhQTcbEbACzVnH3N4y4tNhmcRvwqrJ3hUC69YMco-CxmyAEoxes5fE40V4EMAQdDweUSjPk2AataSNc1cZtX5QJQxIfAWBAwF9vAVjrXT63pZ_AXWFlFj2E3xa-eBldf33_--HibgukGGO4aMeEt-FDzucgO11T3HHyN2Ae_5HjeUuJqzBRwSYZwhREbHKaLxxsngh-9rnA7kEQf7pIhA16QsuJjju92D-j0dNjJO9pYVxrPiQ_QtchsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a338f70a64.mp4?token=dxEp_rInFA8xOPnhnYJa-Y6dlrKWl8bopsKVNokCLrsDXa87urrG7gpXqunvbtSjJf6ThP1ZilvMEmmR9YTtoQMKcFcVYQhQTcbEbACzVnH3N4y4tNhmcRvwqrJ3hUC69YMco-CxmyAEoxes5fE40V4EMAQdDweUSjPk2AataSNc1cZtX5QJQxIfAWBAwF9vAVjrXT63pZ_AXWFlFj2E3xa-eBldf33_--HibgukGGO4aMeEt-FDzucgO11T3HHyN2Ae_5HjeUuJqzBRwSYZwhREbHKaLxxsngh-9rnA7kEQf7pIhA16QsuJjju92D-j0dNjJO9pYVxrPiQ_QtchsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی گسترده‌ای موسوم به «هاوک» که در کوهپایه‌های شمال شهر «رینو» در ایالت نوادای آمریکا شعله‌ور شده، تا ساعاتی پیش بیش از چهار هزار هکتار را سوزانده و همچنان در حال گسترش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143304" target="_blank">📅 11:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143303">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr_TecFvid0xfxkDi-OyGN3ZVepbPWLiP5LPeapU8jsCjU7LOeBn9PUZkfaEYfdg351vO5QzXLt5JpI2VIaixomYyf_UiAB-y6eCp4IwdqbaCEJlCOcXtdzN5WoJh_lvtupAEYkEh5zvPsQ8F9bgr2iGU4Q6qGoahuNZ_tZKhf96ObrDyKBFP_a3QxSZzjNbHaK7HbX2JzB1rUGRur8aRa3fJ0JnujBdATZEAleoM3D-mZk_PrCTZGCDIk7C1SbxvvC3yXyaYX7jTJ6iut93YD3sKLuThUu-BKZamKVm0Zz60EHPEa6WLtLS9jLDHLa0MA7f-yqrK75C9Jxqi1W6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
مشاهده دایناسور در مناطق بیابانی خراسان رضوی تکذیب شد
‏
🔴
دبیر شورای اطلاع رسانی اداره کل حفاظت محیط زیست خراسان رضوی:طی روزهای اخیر تصویری در شبکه‌های اجتماعی دست ‌به‌ دست می‌شود که موجودی شبیه دایناسور را در محیطی بیابانی در شهرستان بینالود نشان می‌دهد.
‏
🔴
تصویر مذکور کاملاً مصنوعی، تولید شده توسط هوش مصنوعی و فاقد هرگونه واقعیت میدانی است.
‏
🔴
هیچ گزارش رسمی، مستند یا مشاهده میدانی از سوی محیط‌بانان، کارشناسان و نیروهای حفاظتی این اداره کل مبنی بر وجود چنین موجودی در طبیعت استان وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143303" target="_blank">📅 11:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143302">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
خبرگزاری فرانسه: ۳۳ هزار مورد مرگ اضافی یا مرگ‌هایی که مستقیما با گرما ارتباط داشته‌اند، تنها در هشت کشور آلمان، اتریش، بلژیک، بریتانیا، فرانسه، هلند، پرتغال و اسپانیا ثبت شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143302" target="_blank">📅 11:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143301">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d7bcbd95.mp4?token=KdYsdVEjUlaAUzlUiKbu4QGp4_qB-krLQUcaIZXMa8xqdlXpCl-cPbzr-MLNN3Y-SGENZUdMMbrthamE9qR6F1cQj9EtWPgDY8-zts71DToUSAXxiWQM3igVkEW9mZhjh35uHoWJSfYvuNkglJfKvboOjTaP0qPMd9FFvunKTOwu1JxOP9BPnS1IxS5GyDFl77IcFZ8qracIyO2qQj3TE5VgdQPr2NMuz2lhTF7fu-o3Ut_1I4k9U1qTTwypPbyxae1qPrjUFCwxyLylPWgC1Uw3x8Jcw2fhHtnj42xjv72QVp8FUrBwDE5TEKKiQodEPvtDxTQ_eocZ6n5dqaQuHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d7bcbd95.mp4?token=KdYsdVEjUlaAUzlUiKbu4QGp4_qB-krLQUcaIZXMa8xqdlXpCl-cPbzr-MLNN3Y-SGENZUdMMbrthamE9qR6F1cQj9EtWPgDY8-zts71DToUSAXxiWQM3igVkEW9mZhjh35uHoWJSfYvuNkglJfKvboOjTaP0qPMd9FFvunKTOwu1JxOP9BPnS1IxS5GyDFl77IcFZ8qracIyO2qQj3TE5VgdQPr2NMuz2lhTF7fu-o3Ut_1I4k9U1qTTwypPbyxae1qPrjUFCwxyLylPWgC1Uw3x8Jcw2fhHtnj42xjv72QVp8FUrBwDE5TEKKiQodEPvtDxTQ_eocZ6n5dqaQuHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آناتولی: طوفان از روز جمعه در این نواحی شدت گرفت و سرعت تندبادها در «فورلی» به حدود ۱۲۰ کیلومتر در ساعت رسید.
🔴
تصاویر ویدئویی نشان می‌دهد که هواپیماها در اثر تندبادهای شدید از محوطه فرودگاه رانده و سپس واژگون می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143301" target="_blank">📅 11:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143300">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: فیلد مارشال عاصم منیر روز دوشنبه در راس یک هیات رسمی به تهران سفر خواهد کرد
🔴
این سفر در راستای تقویت همکاری‌های دوجانبه ایران-پاکستان و نیز ادامه مساعی جمیله پاکستان برای کمک به تقویت صلح و امنیت در منطقه صورت می‌گیرد.
🔴
عاصم منیر در…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143300" target="_blank">📅 11:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143299">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر امور خارجه سوریه:پیش‌بینی می‌کنم که به زودی مذاکرات با اسرائیل در مورد یک توافق امنیتی از سر گرفته شود. ما دست دوستی دراز می‌کنیم و از اسرائیل می‌خواهیم که از این فرصت تاریخی استفاده کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143299" target="_blank">📅 11:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143298">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رئیس کمیسیون فناوری اطلاعات و ارتباطات اتاق بازرگانی ایران: ارزیابی معماری زیرساختی شبکه پس از تجربه قطعی اینترنت بین‌الملل ضروری است.
🔴
دولت انگیزه رفع فیلترینگ را دارد، اما این موضوع باید با بررسی همه جوانب و رعایت شرایط موجود دنبال شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143298" target="_blank">📅 11:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143297">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
دلار هم اکنون 198,450 تومان ...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/143297" target="_blank">📅 10:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143296">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: فیلد مارشال عاصم منیر روز دوشنبه در راس یک هیات رسمی به تهران سفر خواهد کرد
🔴
این سفر در راستای تقویت همکاری‌های دوجانبه ایران-پاکستان و نیز ادامه مساعی جمیله پاکستان برای کمک به تقویت صلح و امنیت در منطقه صورت می‌گیرد.
🔴
عاصم منیر در این سفر با مقام‌های ارشد ایران دیدار و گفتگو خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143296" target="_blank">📅 10:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143295">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0a5G_AxQutR9p8Q00cABtWrHVEgGiAeJtpgAX5KK3muChxlBcafUsZaqBibiSxM-QeO1rD48DvFSLuIjNNtmfpfDaPatcMdMfH_STb-tocEyS81gLzAKobhfvy0CRUGtn-WO2U1fR2kepd3jeVugkqu52c6w0tFkBsqlYTPY1mN1mlNjgDSUk55LCQ-OqXFHUD8keZZ53_EAcssyXCYRNOObCSkVVwa3H6l_Z1b72xQr_gJX6hU_-Jrugaiy5-mzOEw20B-5gL55XDVJwxEhWuuU6ISE9ZANqthslUTqT2SUtXHTHBBnb1UBOtbsVw2JlSbP5PbLHncslA4s8lRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده مجلس: اگر وزیر پیشنهادی اطلاعات، برنامه ای برای انتقام ارائه ندهد، به او رای اعتماد نمی دهیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143295" target="_blank">📅 10:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143294">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
واکنش مردم به خودروهای برخی گردشگران عراقی، بار دیگر فاصله بازار خودروی ایران با بازارهای جهانی را برجسته کرده است.
🔴
محدودیت واردات، هزینه بالای ورود خودرو و پایین‌تر بودن قدرت خرید مردم باعث شده خودروهایی که در بسیاری از کشورها معمولی هستند، در ایران لوکس و دور از دسترس به نظر برسند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143294" target="_blank">📅 10:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143293">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHlghNUJMUUZVuXowOzWla9uP8bA6OBUsfPywYo2NcPYhrCO7gm4oHjRcTFKTTACMFZpF2Kque495kjzEr1HO4tIsqrFSi6nJxi57dNzj47z5Nx_C6RoO0nUkQ-nbshA8YJNDUvQoQe7mlRJOEVOFZ2_tSg32WLBpmRqs9kiC9LK2v6kNRCeZCBdNqa-iaI_pUQ-9W8i1wEVZlsVBgRsgtH2lG9Yr-Ry7zufL6Y7Umt7tOUBXyyfm8O_RQ5qPCdQ0xvu0JE2ToPNjkTlmNy3pt0BuKwO5-mKbPWp9Mk87RBiEYj_djCnqx6i58hNsmX7w5xHEBN1HjqGJhThU3rcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بامداد امروز یک شهریور، کارخانه‌ نوشابه‌سازی ایرانشهر طی حادثه‌ای در آتش سوخت.
🔴
هنوز از میزان خسارت‌های مالی اطلاعات دقیقی منتشر نشده است.
🔴
مسئولین این واحد تولیدی در حال پیگیری این ماجرا هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143293" target="_blank">📅 10:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143290">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBzdC7J62YSfKJUZqP4nfOAYwEK90MEinSBio9ThoxjChQGUoJJ99pbxGvwrTtjyK2bDpPHkjG9OEAj9T4_16sHCH-jkgEsA6dQ67RygC250gTyFit4Ipmzhse6O6JMAFcevWg3cEqMOFM5sY87UvHt_QYWzrhiCCc9o8Z08PUgSb8fCfvyjMH6PYO400ghd-pDevXi5_a1jEMS2zajNSw36uW_B2eWEdhdIfXlHjavKUjwG6uWTUx_i_it-N6ZBNC0GOOSbNWU8JJ57ujUrF2mQ98ufnaTl2_zIlFzgOSsvYsQHbqBZpO2fIPpPm3wbFPhBSnwGZ1NknD5NuWTMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rHx8eHdPNS-aVYPgKBmDRgtQVVXe5CQnLWoEY3UNcYM9uwwunJhhTWU5gbgJRws1e7n7ZHqZFl8NuR32NkQkYsd4JgZhdpNwlhtV_qlHFtimneAdiKBNtN_F-hIwTQ7sWOqFKfBdFwizF-Wd1bzRlpvs-xhDAOhDuhVulGIElF6luy0agRjxXqSNRRDW3Zsr4cUwk5077pnzWaAGAaL9gB_uzz645hvAGPJCxc7bLB8xbfVtAdh1rBekEIrl8M5aP3IzwSRmJPH0LglS8RGGjlaDOsGi2piFApsBcv00JA2uF4laSOr2H6S8Y-gaiBs6DBti3OPXdBckwxq2dNoQNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
۲۵۶ میلیون دلار خط تولید BYD یکی از بهترین خودروسازان دنیا راه‌اندازی میشه ولی اینجا ۶ میلیارد دلار به ... میدن بره زباله‌های MVM رو بیاره چند برابر قیمت به مردم بیچاره بفروشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143290" target="_blank">📅 10:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143289">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نماینده مجلس: امارات باید سرزمینش را بابت خسارت در اختیار ایران قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143289" target="_blank">📅 10:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143288">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoThCTQ9arsmX7s5FXA14Mq791GoDOMOQ0-tSuy0aIiCepUxHgvZqNLvpglvjSC4C_ISHii10siKvOrA1tzzDH16PPBzJEdFJPEpEdlyJ8icZAwokWEgJsM_AJyzyUq4_xmz178xO_afhRn4F1N6tpLzSn1M9Eadl2gOFtjKIBezt-YpDtPd5Us5rzJ6nfDtNmPZLuatJWlhKUkamENj1qRPBSlAN2GuSe8ckFz-wuOD_bOOQGkMJt1B3hhHu97gCxhjy8qbzXtmSBUhqELGh0jHfy42tB0k57b5jCTzB2B2XtOHVt8S47_6V-ef810dikkv65-RQUN349yHX7Ww-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه تلگراف بریتانیا: هکرهای ایرانی یک حمله سایبری بی‌سابقه به یک نیروگاه در بریتانیا انجام دادند که منجر به از کار افتادن آن به مدت ۴ روز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143288" target="_blank">📅 10:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143287">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhoRpqfBpBlw1QQFh2I22Jsqr-suFeSP9AIRGxHvDe4ZQZaXAKYi1EKslZRZb37lgAARO0h6FD26K55ieNhGTSfxSMV0OSo3O-GO1AS2A8o5gEZ-Mc_kU-dqJrrtF3QI2jNwfldowgRxDPQQFj816ssNK1HVs9TTTzltGU1oyH5acgvuz4FAEYZkbgU7oJNJdyQyiqtq6Ge_KWvgifOVEFlulehibm4b6nQ-k5oJHdigVdlFSDnlZmRyR7sh4acTuV3LHJ5WxZRn2CI7YvAogTzOE8isHSz9sP7DPEEblFOA1PGaGkKSiDXQ82XTAJqJZ09LYpDvFsxQ6WKNZqRnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
علی قلهکی: تصمیمِ فعلی دولت بر «عدم تغییر قیمت بنزین تا آخر سال» در ازای « تغییر در میزان سهمیه بنزین هر ایرانی» متمرکز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143287" target="_blank">📅 10:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143286">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaiaI9ZNNIUfTfPmHpu8cDlibpa7Tq6NFW6tAnOAGa_Xasx6hxkAnv0v3GUxPWsaOz8rPaN-ku_i7nPnkY34KFzE3YmDlmOWIUKxbLhJyrKpCRP-o6KS0ZoSNMAwDC_SJxikSjcujjC-hWv1TJ26T26a665kFISLApaBMglP5zF05qaaEeBmUzm4Fc82GnvWBi2H5tF5pdyBpE863uQcBBBDxgxrAi1ctiINRkP_HtGz7DgufcD2ZOc94uYLbDZqV58_Hws6qrU-u32G5XqPe5F-F78F5cC73PJi7swJ2-hR43kprufqKhlCsi4zzhEAblRMvYf0O62pc_vOy_5Izg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی که به نام چین ثبت شده بود، از امارات متحده عربی به سمت ایران در حرکت بود و از تنگه هرمز با استفاده از مسیر تعیین‌شده توسط ایران عبور کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143286" target="_blank">📅 10:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143285">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سپاه اصفهان : احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و مناطق اطراف تا ساعت ۱۳ امروز وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/143285" target="_blank">📅 10:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143284">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
به اعتقاد کانال ۱۲ تلویزیون اسرائیل، ترامپ سبب شده است تا فرصت چندانی برای عربستانی‌ها باقی نماند.
🔴
چه ترامپ این موضوع را درک کند و چه نکند، استراتژی او مبنی بر فرسایش، کار را برای متحدانش در منطقه دشوار می‌کند.
🔴
عربستان سعودی ممکن است تحت فشارهای رو به افزایش اقتصادی و امنیتی، به دنبال دستیابی به توافقی با تهران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143284" target="_blank">📅 09:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143283">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e169546d5.mp4?token=HlGpkBdPYvSHrYhbL-b-tnolnVDISy9zefKVLlf8_Lmmq9d1yJxKufZKtP_1yM-y1PVOadc0qvoVTYdaLhevioy9MgRSlLaoK8Kgm2zGr2NrZ-bhpmeMZKN7BSZabrm8UwtlOL6qSbbHxSiPT8X0HC5yXgBxFg2hCZrf8bUaATtxx6AGDtr1YbaU7vhJnzJvZLs1Ae51BsLLJd7RIbxVHkfq0yi8TXQS8qW9-TRgT9VtXAOMJyEJYZl3dtqD8FrtbrezWMt-xvZZVQDXAvM44x-IHJMUGIMxUHHjip5Z7nMsvROLvt_1z5r7OIy9_BhdfTijAMZyZpLMjYYQ4AcQTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e169546d5.mp4?token=HlGpkBdPYvSHrYhbL-b-tnolnVDISy9zefKVLlf8_Lmmq9d1yJxKufZKtP_1yM-y1PVOadc0qvoVTYdaLhevioy9MgRSlLaoK8Kgm2zGr2NrZ-bhpmeMZKN7BSZabrm8UwtlOL6qSbbHxSiPT8X0HC5yXgBxFg2hCZrf8bUaATtxx6AGDtr1YbaU7vhJnzJvZLs1Ae51BsLLJd7RIbxVHkfq0yi8TXQS8qW9-TRgT9VtXAOMJyEJYZl3dtqD8FrtbrezWMt-xvZZVQDXAvM44x-IHJMUGIMxUHHjip5Z7nMsvROLvt_1z5r7OIy9_BhdfTijAMZyZpLMjYYQ4AcQTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: کنار گود ایستادن و حرف زدن خیلی راحت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143283" target="_blank">📅 09:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143282">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN4FLG5MuU-wEVaXxwEyNWRVHFpbPkOEtrH_HN-Y5QRb2aYzMPazkYHKZ_AXHWfB-pUs66IvgNo2-cwYxa5er5jqNKuuuZ6pABPDBBuag9ME5adezcJyEpAFdMGKk0btVs54wecR8mpQ0ghjRjPpCbUGR0zcMfKRqrJoKBCBR_M-Q4f6AKkX8WwnJbvzjnX7_HS_0Ch-i1cPVnls6wf9MLGTM8_xAXvIqTPjjyPeu4zEXUxFrFlOATu5sC1SnLxRpQfvkGoDncdiLprNN8saFNSMCiUCpBIic3maMu4yiUzrDjW3idML2OXQbalmEygWvblVKo9tlQkKP4VRyYfjZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست: در هفته گذشته حدود ۲۰۰ کشتی از تنگه هرمز عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143282" target="_blank">📅 09:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143281">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2_Id-ZLSRVyACFDRGt7JDAPTie5QQPzrkaatBItLOWXwMRroQ-OIhr2oN-A19QcoUcZRkD4hZ7CrQSi1pFAH29uVSEIXaid-UDaZx969WQWy4uxO7ym3VClBpas9DFhe3V8TugVOfaBPuhyw5E8TZ-wwnMWuVLc-gOoHRI8zVLgNzS9iBy8ebqDNozjgY4QpBZeyTz2DdNCF-CDsNbFQLa8Mg8J39z6XSB6nfXfKwd3SOFaUzsCUT3GcJ_egVFT08dAHlewCcv47AxFatPrNToD_yxKrr-bOPtqNPZUt_ByHoF8SsF-hkp6qUsc4BakuYeGXBkYkI-vMdcii4OTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، یک مطلب را دوباره منتشر کرد: ما بیش از ۱۰۰۰ کشتی را از تنگه هرمز عبور داده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143281" target="_blank">📅 09:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFjrNd-Wh2qXnLg95qahsFLeioMDB-gQztXTVWBU5ci8kR7ngaRKF-S7YApWNg6KoAxSoe0_BmPMgrtThkSa_ioHw_pv5E2MdZhilv0WiSzRLtqYReVNZkh3BZnrofaa3DyMOiG749YRAtt8LjFMI6Q9FTdzt3wSpIRtYQ0PsGzSZj91LYo9VBVqBlOVHgMEnlcj9laI47Csaa3ivTClkeyvbGvvyLwDE03g3f_R6j32vYYTlHdtk1v1GioGDw9FQ5L9AkKa9HqeBiJa6gkfb0squt9kiZp2PtBzf20fxuKx3GoFdTXCOMJlGMcEax_5G2y_hNsDGcpLtKj067zEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش الجزیره، انتظار می‌رود اسیم منیر، رئیس ستاد ارتش پاکستان و فیلدمارشال، در چند روز آینده به تهران بازگردد.
🔴
هدف از این سفر، احیای تلاش‌های میانجی‌گری پاکستان میان ایالات متحده و ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/143280" target="_blank">📅 09:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سی‌ان‌ان: عبور چراغ‌خاموش برخی نفتکش‌‌های اعراب از تنگه با اسکورت آمریکا
🔴
سی‌ان‌ان‌ مدعی شد: با کمک نیروی دریایی آمریکا، شرکت‌های نفتی عربستان سعودی، کویت، قطر و امارات، نفتکش‌هایی را اجاره کرده‌اند که فرستنده‌های خود را خاموش می‌کنند و نفت را از خلیج فارس، از طریق تنگه هرمز، به دریای عمان منتقل می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/143279" target="_blank">📅 09:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143278">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نماینده آمریکا در امور سوریه: حمله اسرائیل به پایگاه هوایی «ابوالظهور» در سوریه، ممکن است اقدامی برای «تحریک ترکیه» باشد؛ این بخش جدی و نگران‌ کننده ماجرا است
🔴
نماینده ویژه آمریکا در امور سوریه گفت اسرائیل پیش از حمله اخیر به یک پایگاه هوایی در شمال سوریه، واشنگتن را از این حمله مطلع نکرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/143278" target="_blank">📅 09:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ff2cc3a8.mp4?token=CECq4xKpCcwhxOvKJluzRWtDwg81VIhT-S1meliXnNDZOfwj5hBy6de2x3U-9vJBL86Er31ug9h1RB-wG0hU_sIAKiuwie_0k-2HzyRo8L9CllOBczDX32hFHam3ZjmFjGU2K406V0mq_74r1tUiEkRke95-ULIx42VhtS64Q6yNF8XBE1b0P1w1Lyn8k3-ZjN_FjBSMUE6uuDCZlikNtzZ1fQhULed9p4-Z9Y8XfVbjOOCwpVTh6cGiHuZ9b5u1JkKxVRwy54hAICwHyBvtavwCfOv55BoNGMI3ZYwqoZjvM1DzLyhVSZfS_Ehg838bFYxTgibyxIdkvdA5egkZrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ff2cc3a8.mp4?token=CECq4xKpCcwhxOvKJluzRWtDwg81VIhT-S1meliXnNDZOfwj5hBy6de2x3U-9vJBL86Er31ug9h1RB-wG0hU_sIAKiuwie_0k-2HzyRo8L9CllOBczDX32hFHam3ZjmFjGU2K406V0mq_74r1tUiEkRke95-ULIx42VhtS64Q6yNF8XBE1b0P1w1Lyn8k3-ZjN_FjBSMUE6uuDCZlikNtzZ1fQhULed9p4-Z9Y8XfVbjOOCwpVTh6cGiHuZ9b5u1JkKxVRwy54hAICwHyBvtavwCfOv55BoNGMI3ZYwqoZjvM1DzLyhVSZfS_Ehg838bFYxTgibyxIdkvdA5egkZrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: وقتی تصمیم گرفتیم و تفاهم کردیم، همه باید پشت سر آن بایستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/143277" target="_blank">📅 08:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143276">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV1M-p6UQCtTTc_nyv9fDRdxPn96pIdSeJnqAjoi9NIyUSydWo9kl1MW2u1XKljO2_5Y-AmpVGVVUei7eo_azxWQW6othmvPnYNio516C-enSuXLAiMu8LusoOX8cjDtmH1iobZ3dfgI_I0JWW5gmQb8cZbkEDe7eDIZ9-WTJSMx4YtYqZxGKUz6AA4lwkn5bMsi5sqnC5cLaTLTTHZOamehnMu_1bWqWZI0fpjCp3tPAlZach9iZRqLgcAkwJofn_QaHY5xL5ZF3BpW6ow64You55eqwqM3lRVMXVRMUEMdQGWfBF8EXIispB_OWmcXzXR6wpK4Dm5f4gBwaWehsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:  «کانادا می‌خواهد از مزایای یک ایالت بودن بهره‌مند شود، بدون اینکه یکی از آن‌ها باشد!!! آن‌ها همچنین برای سالیان متمادی، مقادیر زیادی تعرفه از کشاورزان بزرگ ما دریافت کرده‌اند.
دیگر بس است!!!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/143276" target="_blank">📅 08:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143275">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e8b6d915.mp4?token=n3veBSrZW53lg9yrYsRNsNLyRjWlheVVXXmxMnkTa7AQo32EDa0cvCPt2fzUNWOBBrfCLPLomU86XLIaASVP45pGDmXlkx3Z45d3aBp59D5xbmzUZyire5aTbJGm4q5F0Lzzn_hszBFGUrNbvglF2RKunjkxZVQeY5F3bknBvdRiDGdEhQ81RPpl2qWVVXVapGrlS-Azv2HaZkaGd-JtfKcN_bg5g2BsoSCws8skH1RAEN1rvolYh9oGe4WDhnQwcicu2XGT371KHHigFmn_TjDNBAO0AgmNDmtXrIQSkq1NSfCUVwQnaxre99nVgOq7kEhH6eEWRSHc8UKosa2osCtRMuGCRwgyuI1f59gaVvBVQ8fNzTdtPclhV60dNUYl1ge-eAtY75ojzoa_QSvFOhDA3_qfXH8LYBruSHeS4tVsJTg_iT2HsR-OYtOOtLv4GiH_6nJ-INMKMOtNe6_7iMZOCZIChSBfiY-HfH9DrRLSjuZQ-HdEs_6_mWbGW43OYNIm-IrClphVVF0TV5napW6NpdqyUbT8aLtRU5PDLkOLtRGFez6KbvPp35pAXua797x1XYinsT9hQGRjKaf83nuGDUj45Se-Zd9gTOgoZ-EWb7RHNB4AmNVx9C368S7kADxoCNvutu-cN1l4XmHkWwhQzX_Hv0IyuQRmL8bGTFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e8b6d915.mp4?token=n3veBSrZW53lg9yrYsRNsNLyRjWlheVVXXmxMnkTa7AQo32EDa0cvCPt2fzUNWOBBrfCLPLomU86XLIaASVP45pGDmXlkx3Z45d3aBp59D5xbmzUZyire5aTbJGm4q5F0Lzzn_hszBFGUrNbvglF2RKunjkxZVQeY5F3bknBvdRiDGdEhQ81RPpl2qWVVXVapGrlS-Azv2HaZkaGd-JtfKcN_bg5g2BsoSCws8skH1RAEN1rvolYh9oGe4WDhnQwcicu2XGT371KHHigFmn_TjDNBAO0AgmNDmtXrIQSkq1NSfCUVwQnaxre99nVgOq7kEhH6eEWRSHc8UKosa2osCtRMuGCRwgyuI1f59gaVvBVQ8fNzTdtPclhV60dNUYl1ge-eAtY75ojzoa_QSvFOhDA3_qfXH8LYBruSHeS4tVsJTg_iT2HsR-OYtOOtLv4GiH_6nJ-INMKMOtNe6_7iMZOCZIChSBfiY-HfH9DrRLSjuZQ-HdEs_6_mWbGW43OYNIm-IrClphVVF0TV5napW6NpdqyUbT8aLtRU5PDLkOLtRGFez6KbvPp35pAXua797x1XYinsT9hQGRjKaf83nuGDUj45Se-Zd9gTOgoZ-EWb7RHNB4AmNVx9C368S7kADxoCNvutu-cN1l4XmHkWwhQzX_Hv0IyuQRmL8bGTFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: نه تنها ایران ونزوئلا نشد بلکه دنیا در برابر قدرت ایران حیرت کرد
🔴
شرمنده‌ایم که مشکلاتی وجود دارد. ما در جنگ تمام‌عیار اقتصادی، نظامی و امنیتی قرار گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/143275" target="_blank">📅 08:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143274">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پزشکیان:با تمام وجود به دنبال این هستیم که تورم و معیشت مردم را حل کنیم/ می‌فهمم مشکلات زیادی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/143274" target="_blank">📅 08:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143273">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcefa0d663.mp4?token=JXWZiuv9SbKzs6-ymF9wgpRz7ciRXdQg3zyiNUgmol-7p8AwuopVEeHxBCKj3nHAMlpKOToG4airN3M_cwD13Rbp-w2p_VEs9Z5hnEswd5QZGCcnnqWqoHq_IcSfIVr2wn2InsbXA4dcVbN6f86Y9suuczFtPkeqc1W_UmazobbGLbMI1pnUg9Stdn3DFb2zPDNXbcbxh5XMOwpZ0S6Rm6nD9p2ewf8MiU1lRlfu1_G75a0qL7moz7XXF5V6X14EMh3Vy4jX9aZC_IO_W4s1cBXDHr3OfQ7RbHnnHR9K7MlTiRnVB-eyYcXO2r09z8gTEQQO-SjZ94JfUWU46pDktQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcefa0d663.mp4?token=JXWZiuv9SbKzs6-ymF9wgpRz7ciRXdQg3zyiNUgmol-7p8AwuopVEeHxBCKj3nHAMlpKOToG4airN3M_cwD13Rbp-w2p_VEs9Z5hnEswd5QZGCcnnqWqoHq_IcSfIVr2wn2InsbXA4dcVbN6f86Y9suuczFtPkeqc1W_UmazobbGLbMI1pnUg9Stdn3DFb2zPDNXbcbxh5XMOwpZ0S6Rm6nD9p2ewf8MiU1lRlfu1_G75a0qL7moz7XXF5V6X14EMh3Vy4jX9aZC_IO_W4s1cBXDHr3OfQ7RbHnnHR9K7MlTiRnVB-eyYcXO2r09z8gTEQQO-SjZ94JfUWU46pDktQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور پزشکیان: تفاهم‌نامه نتیجه بحث‌ها و گفتگوهای طولانی همه کسانی بود که دستی در آتش داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/143273" target="_blank">📅 08:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143272">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af847fdbd.mp4?token=e-CTqxlGvm7uew3BYT6pQyKqqIj2zKBEy92mRclJlAtBX-Sh9QlwJMSPwskV7VknWyDr3NJ5P5NmzbQCeAu5su9iMSrw2joCVKK3btVWcVxJBNTTwE0KawO9E-QM6IYRqNFNs9X0eYu8ANGiH-DQ-qvhGX6EUh0FJTJDTHKC74YFD0LI9RtEAkVfZz6jCfx7mEqDT387qseMI7MzIJNxSyYTJhj8iKWm2Suix5NqY4z-iuTiCqX0d1LJYAZLLdRnyo-gXeit724BhZZinnztk4S6hWE-AqFYbJRjn_hrRzjBrWyhfU1X57DKutIZOr67YlTwPaeZToFYz-P99A9q4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af847fdbd.mp4?token=e-CTqxlGvm7uew3BYT6pQyKqqIj2zKBEy92mRclJlAtBX-Sh9QlwJMSPwskV7VknWyDr3NJ5P5NmzbQCeAu5su9iMSrw2joCVKK3btVWcVxJBNTTwE0KawO9E-QM6IYRqNFNs9X0eYu8ANGiH-DQ-qvhGX6EUh0FJTJDTHKC74YFD0LI9RtEAkVfZz6jCfx7mEqDT387qseMI7MzIJNxSyYTJhj8iKWm2Suix5NqY4z-iuTiCqX0d1LJYAZLLdRnyo-gXeit724BhZZinnztk4S6hWE-AqFYbJRjn_hrRzjBrWyhfU1X57DKutIZOr67YlTwPaeZToFYz-P99A9q4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: تا جان در بدن داریم خدمتگزار مردم خواهیم بود/ امیدوارم بتوانیم با قدرت از بحران‌ها عبور کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143272" target="_blank">📅 08:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143271">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رویترز گزارش داده است که عبور محموله‌ های نفتی از تنگه هرمز به‌شدت کاهش یافته و در روزهای اخیر به سطح بسیار پایینی رسیده است.
🔴
‌بر اساس داده‌های ردیابی کشتی‌ها، در روز پنجشنبه تنها هفت کشتی حامل کالا از این تنگه عبور کردند و هیچ نفتکش بزرگ حامل نفت خام یا کشتی حمل LNG در میان آنها نبود.
🔴
تنگه هرمز پیش از آغاز درگیری‌ها مسیر انتقال حدود ۲۰ درصد نفت خام و گاز طبیعی مایع جهان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/143271" target="_blank">📅 08:49 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
