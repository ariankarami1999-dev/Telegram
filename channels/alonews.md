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
<img src="https://cdn4.telesco.pe/file/dwZbFyAdL54vlTBLUUxV0mghyeE0dOLbv4XHH1_Xn9lDEwb1L5yhzv_wRnHqPIUeyhwzm6zpPthsNI7CFw6_XDqJRb8wux9jU7TVh3DxkptjTWRGIWr0Td_fFn_F1_QCIHNoz8fF3KDaGSVH2aL0hfJAdZH-rLqyrnrnN2bEk1yYRmNSnGNmd-xdEcrruSd5d-I0ARstqwRkSI-R33_jmQb-neA9CxYGiFuSy5d2_sgXA8hPXa1-Ko7f0fjTCvgh2evvfTTlzlsjt0gewOaM4uCabowKDnxwpMVgOSWmqeMmQIXdwfgmIzYDuvGcorpwJqHrjEBZSHUGASY9YDiFvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 10:05:15</div>
<hr>

<div class="tg-post" id="msg-134315">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635b715ae7.mp4?token=e2tmpAD0gIu93NCGCcaEvCvZEQPSGGWqlKToaG8RnhdoNGLuc8Q4LPKprRN2-vsnOQDAO_7UPCZbdohg4dkt-_-K8jgBaSjdqzCxeyK4_c54ztQVGZs8n15yeRQHthD3NiuCjYFSjI7v5kTI6TrU1pX9HYceA4M9sTWOZHEPSISwW6kUAZz0dz4PIrf0Zr1HSUgq_a47l8NVHk7WId8ngSYuZ5e4cGS8kWeZDv4fCRPp_uRKFQpl8S3iHRMlQjqqQryD8w0zx7VotP6AenZ4AdUbREDLOnN0zfn3gHUHe4G3LqddnCUHobhg3Tu3z9Mw3BmJhcWJQFB3IMyU6IftFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635b715ae7.mp4?token=e2tmpAD0gIu93NCGCcaEvCvZEQPSGGWqlKToaG8RnhdoNGLuc8Q4LPKprRN2-vsnOQDAO_7UPCZbdohg4dkt-_-K8jgBaSjdqzCxeyK4_c54ztQVGZs8n15yeRQHthD3NiuCjYFSjI7v5kTI6TrU1pX9HYceA4M9sTWOZHEPSISwW6kUAZz0dz4PIrf0Zr1HSUgq_a47l8NVHk7WId8ngSYuZ5e4cGS8kWeZDv4fCRPp_uRKFQpl8S3iHRMlQjqqQryD8w0zx7VotP6AenZ4AdUbREDLOnN0zfn3gHUHe4G3LqddnCUHobhg3Tu3z9Mw3BmJhcWJQFB3IMyU6IftFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از انهدام دقیق مرکز تعمیر و نگهداری جنگنده‌های پایگاه العدید قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/134315" target="_blank">📅 10:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134314">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCEJpIpoP2gu7sWAyaLzMatRUhbobIY38e5nlnBXb0tK5Pmv9aGdFmGhhjMnENlLil_o7aJn0Yp5RnuA0FS32L2i8PWCH0P_BbkwTneb3CmsRL1dxPIb2dJttUOzIi5IJT27hXeg-UYWWSRK0vC2ZqYR56Z2Rr7Z8BlCqpR_my5SFh4TOELiIe49wBvystGa5KYW-RQvZ7SnHC97nxt-3txnjVmcCqLmO3xR9BUtT0YOjFYsgs7YLPXXUstVYIpL9SUX5BYrTs2BAuMq0RoIu5S8yQTXGP5QiwYF4AAphDctfJ9BVzxnITSaYxQ0eXDoGyi3Gh0F792t6PkpD8IHOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به حملات آمریکا به چابهار، صبح امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/alonews/134314" target="_blank">📅 10:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134313">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
رویترز: بر اساس داده‌های شرکت ردیابی کشتی‌ها، تعداد شناور‌هایی که روز سه‌شنبه از تنگه هرمز عبور کردند، افزایش یافت که بیشتر آن‌ها به تجارت ایران مرتبط بودند
🔴
هیچ تردد قابل مشاهده‌ای برای تانکر‌های حامل نفت و گاز از سایر تولیدکنندگان خلیج فارس ثبت نشد
🔴
۹ فروند از ۱۱ شناوری که روز سه‌شنبه از این آبراه عبور کردند، از مسیر ایران حرکت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/134313" target="_blank">📅 09:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134312">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
استاد روابط بین‌الملل دانشگاه شیکاگو ، مرشایمر: جنگ با ایران وارد مرحله «اقدام در برابر اقدام» شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/134312" target="_blank">📅 09:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134311">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21e369331.mp4?token=Cw6m6Uk2iqmULyimSJ15jabVLZVhSnRfhAwS0LrbOpaax909TnnfTNq3yrpOWeLvjIUCVkL_HxZCBwRkGWi_DzNU_zBLhUgDEOKj2OLZ_1jNNkOy8DcvAR_v0J3-lmeMvV4DRI-tzFQNuNmye2DDfqRpdkiOSOA_imLej91hIS_4Ne6jY0VUUbVRpneI6FBdcK9zaywg5zhNe5sh9iYUJt5xVp1Sq91_lUS5-R-ksa-QFA7S8IfTBciJLx-fnJHMKJvvQha01VH3J5XQpv-PCgGFh_Ymuy7bMU7siwFcwq3qr3Bvz3pOdonvKSJru9b7yyq-ilKxTvEexwCluEz8t4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21e369331.mp4?token=Cw6m6Uk2iqmULyimSJ15jabVLZVhSnRfhAwS0LrbOpaax909TnnfTNq3yrpOWeLvjIUCVkL_HxZCBwRkGWi_DzNU_zBLhUgDEOKj2OLZ_1jNNkOy8DcvAR_v0J3-lmeMvV4DRI-tzFQNuNmye2DDfqRpdkiOSOA_imLej91hIS_4Ne6jY0VUUbVRpneI6FBdcK9zaywg5zhNe5sh9iYUJt5xVp1Sq91_lUS5-R-ksa-QFA7S8IfTBciJLx-fnJHMKJvvQha01VH3J5XQpv-PCgGFh_Ymuy7bMU7siwFcwq3qr3Bvz3pOdonvKSJru9b7yyq-ilKxTvEexwCluEz8t4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منوچهر متکی: باید برویم زمینی، پایگاه‌های نظامی آمریکا را تصرف کنیم و صدها و هزاران سرباز آمریکایی اسیر بگیریم
#تریاک
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/134311" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134310">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
الجزیره: افزایش قیمت نفت
🔴
قیمت نفت با ازسرگیری اعمال محاصره دریایی بر تمام بنادر ایران توسط دونالد ترامپ و پاسخ ایران با انجام حملات در منطقه، افزایش یافت.
🔴
برای دومین جلسه متوالی، نفت برنت در بالاترین سطح از ۱۲ ژوئن و نفت وست تگزاس اینترمدیت در بالاترین سطح از ۱۵ ژوئن بسته شدند و در معاملات صبح امروز چهارشنبه نیز به روند صعودی خود ادامه دادند.
🔴
نفت برنت با ۱.۴۶ دلار (معادل ۱.۷۲ درصد) افزایش به ۸۶.۱۹ دلار در هر بشکه رسید و نفت وست تگزاس اینترمدیت با ۱.۱۱ دلار (معادل ۱.۴ درصد) افزایش به ۸۰.۴۰ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/134310" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134309">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ارتش اسرائیل امروز صبح عملیات تخریب گسترده‌ای را در چندین دره و خانه در شهر بیت یاحون انجام داد، و همچنین جاده‌هایی را که شهر بنت جبیل را به شهر مارون الرأس متصل می‌کرد، تخریب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/134309" target="_blank">📅 09:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134308">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مهر: برج مراقبت دریایی چابهار برای دومین بار طی روزهای اخیر مورد اصابت موشکهای دشمن آمریکایی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/134308" target="_blank">📅 09:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134307">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کیهان: دولت رسماً و علناً از تفاهم نامه خارج شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/134307" target="_blank">📅 09:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134306">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a9d2a5de4.mp4?token=B_AS7Fug_aUkNUibSPfqYomnMWFgpNwtgOfvu2a06rkXKhzByacetHTefPO8TiAXLS169paDy5s_gDVHf8k9KLSO6Afba3ckoEGmAJv0lPVbOOHLxADGEXZ1wxb_p-HL0n3W-tG9LafKrQ6vTaeGUCyvdQTKEzh6KkSf161DIsZO69DIqqh-POfVzaUzJpR9VE823jS1vobefrWvckh05cZdTl1IvQYuMiWDL9PtLTAaBHHOfAOhAQ4rqIr5RXgSYeN05jhW4vZb_bOkgO8zlNO48u4n7ANESd28XdgjW0Nqxmd9RqANt8ebCV6oUhpv6Deid7QyjPyJJ8I2QrmkEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a9d2a5de4.mp4?token=B_AS7Fug_aUkNUibSPfqYomnMWFgpNwtgOfvu2a06rkXKhzByacetHTefPO8TiAXLS169paDy5s_gDVHf8k9KLSO6Afba3ckoEGmAJv0lPVbOOHLxADGEXZ1wxb_p-HL0n3W-tG9LafKrQ6vTaeGUCyvdQTKEzh6KkSf161DIsZO69DIqqh-POfVzaUzJpR9VE823jS1vobefrWvckh05cZdTl1IvQYuMiWDL9PtLTAaBHHOfAOhAQ4rqIr5RXgSYeN05jhW4vZb_bOkgO8zlNO48u4n7ANESd28XdgjW0Nqxmd9RqANt8ebCV6oUhpv6Deid7QyjPyJJ8I2QrmkEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از بمباران صبح امروز در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/134306" target="_blank">📅 08:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134305">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
آکسیوس: ترامپ روز سه‌شنبه جلسه‌ای در اتاق وضعیت برگزار کرد تا در مورد حمله‌ای گسترده‌تر از حملات فعلی به ایران بحث کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/134305" target="_blank">📅 08:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134304">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سوال فاکس نیوز از ترامپ: ردیاب‌های داده‌های کشتیرانی نشان می‌دهند که روز دوشنبه تنها ۱۰ شناور از تنگه هرمز عبور کردند؛ کمتر از ۱۰ درصد میزان معمول عبور و مرور از این آبراه حیاتی. وقتی می‌گویید تنگه باز است، منظورتان چیست؟
🔴
ترامپ: اگر مردم بخواهند از آن عبور کنند، باز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/134304" target="_blank">📅 08:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134303">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
یک کارخانه تولید آب معدنی در استان ایلام اوایل صبح امروز مورد هدف موشک های آمریکایی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/134303" target="_blank">📅 08:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134301">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqybb-ol-Er11TVAADBjXzfg6Pw5irpmdkv5kK0P3zsHlU3rGs1gJA-xFEWfZrc137o4wV76aLC-7Vs4ELX295rC_KCqN2qYunEjXs-tlOtpBUYadqldm_DNzMlkcNn6ksaPBeQfIJtGrbCfKmmQDWU_IvSwR2PQheDu65MSaxcKcvRAM588KRVfj9K7bXrn5T6HvuSUlrdBMNxaZ3ijx93mw_XQeVmlaavvOU2Fqdmm-yUaQ_BNNpo91fyXIZVPNb6e_GD72k3G4vCrY9yvKnrFO5tLrAyOVO8tPYZcGUqBCuBscrz4t2yLPrYBqz5EFFBe8YKXywS1AG2gTdgMJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKgwrze--tvQb5m7rmlt8Gy9rB6OQuLB5HQ-qN9jcCMhAm7d0EQdFHqvx3nhBICGYiIsgD77DpAJCOdacSXroWyoPQ4GzpU9cyGbGqs0K0FbOA_uJxQ6hAZyec7ozRkU9sb347IFvuyVj0FMkl_7szVWP4WQX5gE3HeYZSPlRoyKnm3tFEu8kmHk7F0AX7nmZeVKM8EBEKVgjwIUTyuhJHpKDZaKgNrsVmUllWIqaGLn14nbXMRJYlY4tildNZhbthZsFc20nSfgmzbe3goqhZvMpm1rVNkWrTrit3B7jlT_aPUgo-yIjPqoA2UTpHrHiSKYYV5XN0i_WjX75pHWIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره ای از یک انبار متعلق به شرکت «کویت و گلف لینک هلدینگ» (KGL) در منطقه «مینا عبدالله» که مورد هدف قرار گرفته و به طور کامل تخریب شده است
🔴
این انبار، مرکز اصلی لجستیک و پشتیبانی ارتش ایالات متحده در غرب آسیا بوده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/134301" target="_blank">📅 08:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134300">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ایندیپندنت: ترامپ ۳۲ بار اعلام پیروزی کرده، اما امکان پیروزی ندارد
🔴
روزنامه انگلیسی در مطلبی با اشاره به اینکه آمریکا توان لازم برای پیروزی در جنگ علیه ایران را ندارد، گزارش داد ترامپ آمریکا و جهان را وارد بحرانی کرده که خروج از آن دشوار است.
🔴
ترامپ پس از حدود ۳۲ بار اعلام پیروزی علیه ایران، از جمله پنج بار در یک ویدئوی ۱۳ ثانیه‌ای در اواسط ماه مارس، اکنون عملاً بار دیگر وارد جنگ شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134300" target="_blank">📅 08:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBKyyJJtSHj-d5StT89EwpAhn8z9GfcJnu_cEo-476lFw0M1gGhbmOS2J7WBsp5EBx1LBhH_lqvOKfnfd4D4sKO8Gi5qqiyehGpD8a4Ld9tFkgf9uHRyd6dTgOjcMrxN38XZ-wqJfncrgFsclqSpVA1DEanup0zrsIa30jhKyvEXl-T-hJJmdMaqkdSb43kVM-oCbfMuf80n4L-IpYHPw89qhyN98WfFA3JyMkFFqa67L-X9DtRPEwq3gOMdQTzkfZ3zgdb36Nl0idAPZYBARt0-5njbA9yHr5YgCaSyhfHDz7XIaG-BunIAq42ICedG1Mpp0bSQ43nBbvO2e4LdXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که یک موج هفت‌ساعته از حملات علیه ایران را به انجام رسانده و طی آن، ده‌ها هدف نظامی در نزدیکی تنگه هرمز و در امتداد سواحل ایران را هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134299" target="_blank">📅 08:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e63b2cfb.mp4?token=wCQSWXehEsuRWfnZq7j_s9H9x6lUJgpnh_ZlwOTocfYrUhaPav_IIF_o1LI4SmRkpdNe_d4pVdNLoXRGxS4itde-ocBGfc-SLcfSAeSuU9-F-d4W0Inko3eBZawCNho9QWUekgqB7JP9ZtwMN93bYBe_kL7uxty3UzzeG48zqTNxpJDRIrHpgH2hm_lC4sujXBoGI3ie7ay44vekHHTECTGVnDGiT_hv2rcqA-BmnDBaNCy4smDDM7TuxzHDlx4OvOFd8UoFpa0X9hMtnr7q2FTt7iobVDJbYn1c8f97J7meYadrTn_zd2OZ3KxH3GUbXRDHzygIg-ByzdOjVCL1bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e63b2cfb.mp4?token=wCQSWXehEsuRWfnZq7j_s9H9x6lUJgpnh_ZlwOTocfYrUhaPav_IIF_o1LI4SmRkpdNe_d4pVdNLoXRGxS4itde-ocBGfc-SLcfSAeSuU9-F-d4W0Inko3eBZawCNho9QWUekgqB7JP9ZtwMN93bYBe_kL7uxty3UzzeG48zqTNxpJDRIrHpgH2hm_lC4sujXBoGI3ie7ay44vekHHTECTGVnDGiT_hv2rcqA-BmnDBaNCy4smDDM7TuxzHDlx4OvOFd8UoFpa0X9hMtnr7q2FTt7iobVDJbYn1c8f97J7meYadrTn_zd2OZ3KxH3GUbXRDHzygIg-ByzdOjVCL1bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات پهپادی امشب به کویت و بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/134297" target="_blank">📅 04:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
استقرار ایست‌های نظامی در مسیرهای منتهی به بیمارستان خاتم‌الانبیا ایرانشهر همزمان با انتقال کشته ها و مجروحان حمله به تیپ ۳۸۸ ارتش
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/134296" target="_blank">📅 04:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/134295" target="_blank">📅 04:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
اونوقت 4 تا جاکش مثل ا.ث و ح.ر و س.ج زیر کولر تو تهران خوابیدن و توییت میزنن میگن انتقام انتقام. بدبخت مردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/134294" target="_blank">📅 04:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وقتی پدافند نداری و نمیتونی دفاع کنی، نباید سربازای بدبخت رو تو پادگان نگه داری
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134293" target="_blank">📅 03:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک زده شده است تعداد زیادی از سربازان وظیفه جونشونو از دست دادن و امار مجروحین هم بالاست
🔴
همچنین درخواست فوری از مرکز انتقال خون ایرانشهر برای اهدای خون در شهر بمپور برای مجروحین ثبت شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/134292" target="_blank">📅 03:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134291">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/563dcb40c1.mp4?token=Tj8t4GcMyMRXD2hPqhkHj0KqO5_zX8onpXAwPOGK3UcP5YfMckOjKj7CTIzMrYBNE87sQsk6_lSHkhFmA-sK65JIh72bnZ-K2C1TZHNm4Lf4A5jVqv6-h2nfkyVk-wDcOzdFKHMX6-2GF6PbDDPC-7M7urgU4aRNtRQ4WCvMYjR4d5F7nVYyXgIOGymwEgHmJIghRxcjQjLqDt-uVxmaQYzHVn6TpEpihvUD9yW7jJwwoR2qDjzw_TIUejY4kS4TUOB9NEgpxR-JrqpUz6ePCvuCGXe36GipYVWWFPyPEOnpN1hAF1nrgpt1uMv4svgH0LLxHH9thdUy-nc1F8kPBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/563dcb40c1.mp4?token=Tj8t4GcMyMRXD2hPqhkHj0KqO5_zX8onpXAwPOGK3UcP5YfMckOjKj7CTIzMrYBNE87sQsk6_lSHkhFmA-sK65JIh72bnZ-K2C1TZHNm4Lf4A5jVqv6-h2nfkyVk-wDcOzdFKHMX6-2GF6PbDDPC-7M7urgU4aRNtRQ4WCvMYjR4d5F7nVYyXgIOGymwEgHmJIghRxcjQjLqDt-uVxmaQYzHVn6TpEpihvUD9yW7jJwwoR2qDjzw_TIUejY4kS4TUOB9NEgpxR-JrqpUz6ePCvuCGXe36GipYVWWFPyPEOnpN1hAF1nrgpt1uMv4svgH0LLxHH9thdUy-nc1F8kPBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقرار ایست‌های نظامی در مسیرهای منتهی به بیمارستان خاتم‌الانبیا ایرانشهر همزمان با انتقال کشته ها و مجروحان حمله به تیپ ۳۸۸ ارتش
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/134291" target="_blank">📅 03:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134290">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پادگان ارتش و سپاه شهر بمپور که کوچیک ترین شهر ایران حساب میشه کلا ۶ کیلومتره با ۱۰ موشک فوق العاده قوی منهدم شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/134290" target="_blank">📅 03:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134289">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
۴ماهه دارن میگن پایگاه پنجم آمریکا تو بحرین موشکباران شد، مگه وسعتش چقدره تموم نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/134289" target="_blank">📅 03:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134288">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
حمله هوایی به دهلران
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134288" target="_blank">📅 02:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134287">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: همون‌طور که میدونید ما در قبال غیرنظامی‌ها خیلی محتاطیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/134287" target="_blank">📅 02:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134285">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ویدیویی از پرتاب موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/134285" target="_blank">📅 02:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134284">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf2e032d2b.mp4?token=XkRCXzA380rPlt5Z6R_H5YTuxv_rXJRftYBSg_p6JTnJNpK6vZPD--OjT9w3Wy2X0igMPOBkfoki6-rxYWPMtEGsTxNI6upAgdMBjAw6k-VM-TFIf7_DDK5VxInCZWTj02kAT-Dy8jgeAeGh8u6WizaN88wKErXhsqIwApUq5k2QPLiMbOPv9LOfwiu1v752ps0naw2i2h0JOx-3ZcptfQ960ze_tp2s6Q43VCJfpmvCgQeVUouD-efkAwBWSC53se9tI6Fiq-IUUwfHwEOrpT-GEbzF4hFF6mq84dU5XwJjkWsscYOT9oDyGJENoLE8vYDb5U1NtBTaZmqK1TpPEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf2e032d2b.mp4?token=XkRCXzA380rPlt5Z6R_H5YTuxv_rXJRftYBSg_p6JTnJNpK6vZPD--OjT9w3Wy2X0igMPOBkfoki6-rxYWPMtEGsTxNI6upAgdMBjAw6k-VM-TFIf7_DDK5VxInCZWTj02kAT-Dy8jgeAeGh8u6WizaN88wKErXhsqIwApUq5k2QPLiMbOPv9LOfwiu1v752ps0naw2i2h0JOx-3ZcptfQ960ze_tp2s6Q43VCJfpmvCgQeVUouD-efkAwBWSC53se9tI6Fiq-IUUwfHwEOrpT-GEbzF4hFF6mq84dU5XwJjkWsscYOT9oDyGJENoLE8vYDb5U1NtBTaZmqK1TpPEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از پرتاب موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/134284" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134283">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ: رهبران ایران شیاد هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134283" target="_blank">📅 02:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134282">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a85771210.mp4?token=kQbAfSzqyUr6FEXFSFkY_LoG3u_0kPq5RuS-V96NgRthZKgL7BfMYvTEVqn6h45cbzAeUJOER6EefpFqglIjUvfMMRy00-0S-gFclUEChAPSrfMjosDKwir13Uc3TNhDmggCtxyiTzV4nkXBBbYmE2BHqjNC3blVgXofSdf4DHn8SQZFlCsEclVviQsQvNJw9EE1OztKrd3yrknDX0uGJETlU4YdSmyzfUIg60mlMn3xjHN6gqWBONRV-jA0TTT2MXVtgFJf8n-TcaCOuFVGAxVl2f0fLpWVV2dJUxkcK8D5vabNAbhj1hh1ikU-xkGVRIaW6TTF9VuPcOWddkQ4Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a85771210.mp4?token=kQbAfSzqyUr6FEXFSFkY_LoG3u_0kPq5RuS-V96NgRthZKgL7BfMYvTEVqn6h45cbzAeUJOER6EefpFqglIjUvfMMRy00-0S-gFclUEChAPSrfMjosDKwir13Uc3TNhDmggCtxyiTzV4nkXBBbYmE2BHqjNC3blVgXofSdf4DHn8SQZFlCsEclVviQsQvNJw9EE1OztKrd3yrknDX0uGJETlU4YdSmyzfUIg60mlMn3xjHN6gqWBONRV-jA0TTT2MXVtgFJf8n-TcaCOuFVGAxVl2f0fLpWVV2dJUxkcK8D5vabNAbhj1hh1ikU-xkGVRIaW6TTF9VuPcOWddkQ4Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :من در حال حاضر نمی‌خوام مذاکره کنم بیایید که مذاکره نکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/134282" target="_blank">📅 02:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گزارش شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/134281" target="_blank">📅 02:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134280">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=LJ46IGH4yBMWLier9tNT-HcqWpFouV_uk9WAaK7pTns7iz1Nqjepjnkpzbf6Z42tXjy6N8lpDccRKHdA-pdiS3pLWZ39Hd7WfUl0z4IFkbVS7-Vdom3BhIt1Iu-W68aBao2mqLaag3ctei1zcszmgJeccFC171QvQ_4LPhAoFL6TCXWDcy1Q5b0sAy_qYo9851bs-pvxeYelpiWHC-xPQL47l23YIxrM3xFz_A3o0l5nw2Qn7lQSQa4BnahWHV-SlYCUphjFnkP1dH-b6B6Y6fxv7jsA0lUQNuJ1HQvq0nL3QtQoh3L8LD-Q9ilruxTXAw13F-JkiwgfgLTV6UuB2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=LJ46IGH4yBMWLier9tNT-HcqWpFouV_uk9WAaK7pTns7iz1Nqjepjnkpzbf6Z42tXjy6N8lpDccRKHdA-pdiS3pLWZ39Hd7WfUl0z4IFkbVS7-Vdom3BhIt1Iu-W68aBao2mqLaag3ctei1zcszmgJeccFC171QvQ_4LPhAoFL6TCXWDcy1Q5b0sAy_qYo9851bs-pvxeYelpiWHC-xPQL47l23YIxrM3xFz_A3o0l5nw2Qn7lQSQa4BnahWHV-SlYCUphjFnkP1dH-b6B6Y6fxv7jsA0lUQNuJ1HQvq0nL3QtQoh3L8LD-Q9ilruxTXAw13F-JkiwgfgLTV6UuB2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در حال رصد «کوه پیک‌اکس» هستیم، چونکه گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کردیم.
🔴
ما دوربین‌هایی در اختیار داریم که قادر هستن نام و نشان شناسایی افراد رو حتی از فضا تشخیص بدن؛ این دوربین‌ها تمام بخش‌های پیک‌اکسررو پوشش میدن. اگر اونا کوچک‌ترین حرکتی انجام بدن، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشه رو انجام خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/134280" target="_blank">📅 02:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134279">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: آنها هنوز مقداری قدرت دارند، اما خیلی زیاد نیست. و میزان تضعیف سلاح‌هایشان فوق‌العاده بوده است. هیچ‌کس فکر نمی‌کرد که این کار را بتوان اینقدر سریع انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/134279" target="_blank">📅 02:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134278">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز گفت: من روی توافقی امضا نخواهم کرد که تضمین نکند ايران سلاح هسته‌ای نداشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/134278" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134277">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d738632e11.mp4?token=hv2KN15yc09EUXvYFQhEpY8Jtw9PUm2aMLj8-2pDhUtIPd6tev3W8Ej3hfxYUtXm-slNH78GlCpsL_TpGsIHmVkIDIBarppkTKvpzZI9LVC1Z1n_nM4WC59RzOKkHsM0ySUbrZKnlDI-Pc22rTsldvW4ya8fo13zNeX0QL3FK-k-w-0YBt0Z9T3V86PmU2P-9CUf96pj6V1FqHrsW3cGIrVxRsZyNUpGbBemp37b7Jml2AeEm8NxHNqYkoYLSAikgrbRlQaVFjfnZC_gdi3-B4Y_E1suwQJuw5qQB_P2ndnijgaWLzkGFaVvglugHPgA3TUYdPs0siI7KR45DltKFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d738632e11.mp4?token=hv2KN15yc09EUXvYFQhEpY8Jtw9PUm2aMLj8-2pDhUtIPd6tev3W8Ej3hfxYUtXm-slNH78GlCpsL_TpGsIHmVkIDIBarppkTKvpzZI9LVC1Z1n_nM4WC59RzOKkHsM0ySUbrZKnlDI-Pc22rTsldvW4ya8fo13zNeX0QL3FK-k-w-0YBt0Z9T3V86PmU2P-9CUf96pj6V1FqHrsW3cGIrVxRsZyNUpGbBemp37b7Jml2AeEm8NxHNqYkoYLSAikgrbRlQaVFjfnZC_gdi3-B4Y_E1suwQJuw5qQB_P2ndnijgaWLzkGFaVvglugHPgA3TUYdPs0siI7KR45DltKFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره ایران
:
‌اگر به تنگه هرمز نگاه کنید، پیدا کردن جایی که آنها چیزی دارند برای ما سخت است. باید جلویش را بگیریم.
ما باید آن را باز نگه داریم. من قصد داشتم هزینه ای دریافت کنم، اما در عوض آنها ترجیح می دهند پول زیادی را در ایالات متحده خرج کنند، که صراحتاً بهتر است، زیرا من ایده هزینه را دوست ندارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/134277" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134276">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ به شبکه فاکس نیوز گفت: ایران دو هفته دیگر از دستیابی به سلاح هسته‌ای فاصله داشت و اگر مراکز هسته‌ای آن بمباران نمی‌شد، این امر از وقوع آن جلوگیری نمی‌شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/134276" target="_blank">📅 02:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: آنها دیوانه هستند ولی ما دیوانه‌تر و قویتر هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/134275" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">گرفتار قومی شدیم که اگر نزاع کنند مزرعه را به آتش میکشند
و اگر صلح کنند محصول را به تاراج میبرند
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/134274" target="_blank">📅 02:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: تمام زیرساخت‌ها رو میزنیم و ایندفعه هیچ رحمی نمیکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134273" target="_blank">📅 01:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134272">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/ترامپ: نمایندگان من یک ساعت پیش با ایرانی ها صحبت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/134272" target="_blank">📅 01:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134271">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90678a516.mp4?token=ZU0svw6fkJoPXVpCjolXOTirlfSRYvihhMzFqd_l1UDaga0zsGns4CovsmQARtngTCjv7IcrSvgkQrS_pV6kH9vj_TnLR4mvBOlp88Nzb_8sTOI5xYC7qMmug7sczkw_5gXorOLYOQLZk4_DKRCN8J9O-St3b2XRRZXbqLgTym1ZsykvqG8nOIyhiqqrKz4MQsJhgFSRV7Xg9Vmmdx40jOBUvg3g9PXHsZD5Y4dnzfoP-ucBcqZEMsheII6i7IC7b6R3l8tKwnrN_ZMqUwvk_8DYaDebdCpyIhJsCzclUxxSQEmx7nsE51dahIMKBBpYG8MXmeavi0YokCF38rNHEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90678a516.mp4?token=ZU0svw6fkJoPXVpCjolXOTirlfSRYvihhMzFqd_l1UDaga0zsGns4CovsmQARtngTCjv7IcrSvgkQrS_pV6kH9vj_TnLR4mvBOlp88Nzb_8sTOI5xYC7qMmug7sczkw_5gXorOLYOQLZk4_DKRCN8J9O-St3b2XRRZXbqLgTym1ZsykvqG8nOIyhiqqrKz4MQsJhgFSRV7Xg9Vmmdx40jOBUvg3g9PXHsZD5Y4dnzfoP-ucBcqZEMsheII6i7IC7b6R3l8tKwnrN_ZMqUwvk_8DYaDebdCpyIhJsCzclUxxSQEmx7nsE51dahIMKBBpYG8MXmeavi0YokCF38rNHEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : بهتره تسلیم بشید، چون چیزی براتون باقی نمی‌مونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/134271" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134269">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوووووری/ترامپ: هفته آینده نوبت پل‌ها است! تمام آنها را نابود میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/134269" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134268">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فووووووری/ترامپ به فاکس نیوز:
امشب، فردا و پس‌فردا به ایران حمله سختی خواهیم کرد و در مرحله آخر نیروگاه‌ها و پل‌ها را هدف قرار خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/134268" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134267">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری/فاکس نیوز: آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
🔴
ادعای ترامپ: «نه. گاهی اوقات به عملیات زمینی نیاز است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/134267" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134266">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: اگر آن‌ها با بازگشت به میز مذاکره موافقت نکنند، تمامی پل‌هایشان را هدف قرار خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/134266" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134265">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/ترامپ:
حملات به ایران تا زمانی که من بگویم دیگر کافی است، ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/134265" target="_blank">📅 01:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134264">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8222026cf9.mp4?token=bTgVks_fWJftyl4gpeb1T_mDZbnaYcvfXqTOlDQMYhtDoEAWq9zux4sjs9Cl9DpqsjsO14b5wB7pKjoS1soBgMyxHgasmYt7ZxlwpmxfrBm7YpmOdDvnlt5uKVcjGT70l_vrO8JH_MCliWX8Aw6JYHJNnGCC7la_338-IYJqFB6OeSyDe08Xn1oo4CW2DrOmFiykONEUDZ5q7oEeTrvajOsPTAvqq1aPIG333jdTZPykWYTVlSMLc7sNW8yNMK23dsbWvh5urNyEOq0tjjv3E6eGkUYdh52hkkxhS6nZeoxmne6aQYYhdZMDT_rJ_44qFAGPArZRnKNxQ2cYhtSZBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8222026cf9.mp4?token=bTgVks_fWJftyl4gpeb1T_mDZbnaYcvfXqTOlDQMYhtDoEAWq9zux4sjs9Cl9DpqsjsO14b5wB7pKjoS1soBgMyxHgasmYt7ZxlwpmxfrBm7YpmOdDvnlt5uKVcjGT70l_vrO8JH_MCliWX8Aw6JYHJNnGCC7la_338-IYJqFB6OeSyDe08Xn1oo4CW2DrOmFiykONEUDZ5q7oEeTrvajOsPTAvqq1aPIG333jdTZPykWYTVlSMLc7sNW8yNMK23dsbWvh5urNyEOq0tjjv3E6eGkUYdh52hkkxhS6nZeoxmne6aQYYhdZMDT_rJ_44qFAGPArZRnKNxQ2cYhtSZBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستار هدایت‌خواه، نماینده ادوارد مجلس:
اگر هر ایرانی ماهی 1 دلار بده بعد از 12 ماه میشه یه میلیارد دلار؛ یک آمریکایی پیدا می‌کنیم ترامپ رو بکشه.
🔴
بعد کلاهش رو درمیاره میگه خانوما طلا بریزین تو کلاه من!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/134264" target="_blank">📅 01:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134262">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2joaz8GPtBXCWYUaex9sHeDuonIHjv-lrFshayeZDrid2PYtwGDZ6SWnhBh5W7DBjtwq0wglmzdk-iySFy4S3b6-aQEZx6iVw3PJz8pYmogYgQJnaoSihheeUPucs0RUUZj-4ibCEkmLyENSn2ztlngpBFdxzFy6v5O7Z-BikbNZ_-l8xBc7EVD1TU3G87-_OtdVdNRmYjNpvgIA82sLAnoB7FmaWBy_1e8avWtlh619hrDOnV51pMddjY-fzvg97J9qthTC1vIgnbh1DNeBNdpL4VOSM6KbtDW_7XfJSfQPvpIQluT8Q-CpJrhff-KaibfEqXY7lXlW9BTTy59cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مغز عرزشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/134262" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134261">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شلیک موشک به سمت تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/134261" target="_blank">📅 01:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134260">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
انفجار مجدد در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/134260" target="_blank">📅 01:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134259">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی ارتش: تو موج هفتم عملیات «صاعقه» محل استقرار جنگنده‌های اف۱۸ در پایگاه الازرق اردن رو هدف حملات پهپادی قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/134259" target="_blank">📅 01:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134258">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/134258" target="_blank">📅 01:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134257">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4784c0afa9.mp4?token=piMDef5cXJXp5GSBY_9zT-NWgeW2BrsEg8Zq4a3LUK276OrlWENh4ucDyE3cZHLWc72UaoXEDCWHdmM2QJ1-PcyUvmi0ATWcp7OOIZghXUnYcvtxl9nhCjaAkA9fxDXvqMvIcui9keKTcjnmDIt5svsAO-J5inrX5TceRfyG_8OBnkmuLaU7F9R9K3UqPe5ZoPI6yO6X-Ubxx0LHHvQRyC7f4y6laten66aR8owBUETmwmLgSwBaXYdSqwy-owULHxDqFvfqwfD85Ks9-1Jm4KTqIS4kNxl2VpU0K4sf9mj2k2DXvH8PcbuqRsABTDfiQGKqpEdgCH1mIYL2VgonnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4784c0afa9.mp4?token=piMDef5cXJXp5GSBY_9zT-NWgeW2BrsEg8Zq4a3LUK276OrlWENh4ucDyE3cZHLWc72UaoXEDCWHdmM2QJ1-PcyUvmi0ATWcp7OOIZghXUnYcvtxl9nhCjaAkA9fxDXvqMvIcui9keKTcjnmDIt5svsAO-J5inrX5TceRfyG_8OBnkmuLaU7F9R9K3UqPe5ZoPI6yO6X-Ubxx0LHHvQRyC7f4y6laten66aR8owBUETmwmLgSwBaXYdSqwy-owULHxDqFvfqwfD85Ks9-1Jm4KTqIS4kNxl2VpU0K4sf9mj2k2DXvH8PcbuqRsABTDfiQGKqpEdgCH1mIYL2VgonnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دریابانی سیریک بمباران شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/134257" target="_blank">📅 01:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134256">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
طبق گزارشات تو چیتگر پدافند فعال شده و پشت سر هم صداش میاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/134256" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134255">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پادگان ارتش و سپاه شهر بمپور که کوچیک ترین شهر ایران حساب میشه کلا ۶ کیلومتره با ۱۰ موشک فوق العاده قوی منهدم شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/134255" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134254">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نکته جالب اینه آمریکا این روزها فقط داره پادگان‌ها میزنه و گویا داره شرایط رو برای یه سری کارا و تحرکات آماده میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/134254" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134253">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
گزارش انفجار در تفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/134253" target="_blank">📅 00:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134252">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
انفجار در جزیره هنگام
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/134252" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134251">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
گزارش ها از فعال شدن پدافند پارچین
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/134251" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134250">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فرانسه هم باخت و تنها ۴تیم تا الان نباختن
آرژانتین، انگلیس، اسپانیا و ایران
🔥
🔴
باز بگید قلعه نویی بد هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/alonews/134250" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134249">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FALG6lZ5Ov21I8yX_bR0khsKkH8amlJjNZ9YfhEfNRLIEkr6Mt6D39GzRDI5UY-EzDqIYv8qSVCxwGXJsVTOPgcxgejQC9_79zOiZj7psySTgvt2lVByZBeUz-VmsUPmvMOnMaDrNSbFmUJuNW_rvhrdnf1NXN0l3m-4xzmn9e6DJ6ROubpLkDRwaqrSLAyaUPLYmAafngOQqOZlRndYQ4hyR8_gQrkLCfyqhQ_7mHG_SUtlVGHveJkqo4_vh92R_ClpkFKXR4Q_UNEWnS1k6BloobhGxFmFQRivltrmuFYopwXnp515s1K-OGOaNmXDnTpuFXzs2orcdh2fIJqv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانالای ایتا نوشتند که دست خدا عیان شد و این عکس باعث صعود اسپانیا به فینال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/134249" target="_blank">📅 00:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134248">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/alonews/134248" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134247">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vw5TsS3WefnJMRNKXAUgmQPrYuSwNFjJm-Ama7jinlqtV7LvLVRBuiC4k_36wOnRCFzUu_aTYNX2CEoulEC2_LQpT-rAAtuxHQyElN5q2LR0iFkpPyo0uDU59mcboChfjY8ycHSYd6Kr6ZMUJaZDkTTKD4SQhcVy7C9nOD1nwKq4SxMHHVAuHsqk5IW83md2ddfgniAjpvESbX6mvhD8nBNWNTX1Aeru4UgIUsJb8tsjlTIgpYY5yBATWpDgtyeR6FutaOCN-iSa_wN6N3AbIY6Z9kSr9oN-do7YPl1sQINVW49JHniIU1Kso8MRDF0XQWgz__NI1tkXQ67QcyFaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اما بشنوید از کشوری که در جنگ پشت جمهوری اسلامی بود و به فینال جام جهانی صعود کرد.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/134247" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134246">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx29CJhHuoGEgNpdj0JEDaujwhBYjoJ2nYi_uSMp3d8gzQ6B9gRVRyOt_-YEElCEyPI-_9Hvw5QgpYNmzOqF4cRfG7mVtmJcI2RIHHPaUNicEEd8pzxkfADGQwkiK960_2TWz60rLrkw2WPRLqbmMUydGJp-C39YNxyuXGetOPXRQAVyY_3SQ2CzA76DklPqhQredm_SvXGatYLGhV_CYFTnhAEbjn2d_ZuTb3m3dk_RR-gYpgsM0zVBwc71euGH0EOJNkW8IkZbBa_wNzx2MwZctKGGnBcUalqy4DbO9fcGlNb76ZiJbnPA0cC3HDlN96iWydWjhMqIedgo8ZzT-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا
2️⃣
➖
0️⃣
فرانسه
🇫🇷
اسپانیا رفت فینال
🔼
@AloSport</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/134246" target="_blank">📅 00:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134245">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn5PTZ2pBSRrMHQCMe9LQrbXxgOAwp28-5NBHylQ8NBL3T676p-23CZYHqzxVvd2U0Hpvcnj85PPMMktnvaojcgAJqnKCW8evZjvFbNYsWPgcwQ78zDAcFKSRQt-Gel_4UbLLGdbUT4t-Rdldb9M60MW5wfP6PZ7qbHDlwvd-P41lh6KnEg-aT2XLPk5ey0hL_tfs72eDMYPqzLhcArQ8QI8lhtvIcosQss-ogQGRcBZaXZxbJJAFB-Go193QVTtqL_mHiWEIJHgCE0FDcNOMjkrLbuFiG7OEv3Qt0bSJCCP-XYjEHStJoQIJ0ws8-YGenKaa8N5toPo1tLvlYIdRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سربازان ارتش اسرائیل (IDF) مستقر در قلعه تاریخی بوفورت در جنوب لبنان در حال تماشای جام جهانی فوتبال فیلمبرداری شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134245" target="_blank">📅 00:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134244">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ4-I8Ec_J5kRbuA-SAomh-VoYvM7y6gu0rqio4zXlRY2MRhKt4T_vmBhJv0NsY0YbS0kkKR9pBhlGz2V86Tq_yw-VyQBMxsIYILml9kSALs-3Dp8pVm5vi2sYQBenX6PrFU5_4urgUC695g4e5MasyZiHgkAY9ViPpDY1tepw9T48BsgSkb_tC68ftFBzOUBRi09yQZFV3CakDQjomUdWfsstiaj2xg_xFq24NHvPZ1mWiXmYf1cCAcWwDAUZ-VlfOJZEgWoi2jwZFxlWfNibe5dKvsmb_noaLzwOcdJT4vhEx-3HjjHzMD4N671E0PJfVwNxXI3hY0qmNzz9uwEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید: در حال حاضر دیدار نتانیاهو با ترامپ تو برنامه هفته آینده رئیس‌جمهور نیست، ولی باید دید چی پیش میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/134244" target="_blank">📅 00:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134243">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/134243" target="_blank">📅 00:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134242">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
آمریکا شش فرد، ۲۴ نهاد و ۲۰ شناور مرتبط با محمدحسین شمخانی رو تحریم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/134242" target="_blank">📅 00:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134241">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGUEG0fw6gfBNoUZXxYKyHE-KKjsX7fyCxSog9U-zqARFeIu-4l9AnONHhwitRo2S4aQLN56xcd1XwQ6bJ3rr26kf95FEoEo9KuNuGalvoCse7qXm3SAoSCMMypylyCU8I4W9-b7FZzCInNa0iXsG_K2yPNO8mKQ5lGbUx2iLiVMk8R7vAtrj2ZyIyhY4AAFWH3iX8lRSLoUDjrgTRIafhH-VwspT9DnX-0YoSytWhNkIiPPbs3av7PuXmb9OoocP74L1bSOO1so3WIoSxlyk8zcUSDIDBiebcS0-ZsgTH7g_Dfgt29d4pS0jOQiyZLSnfmE2eVjm1Z4N2D0mh-FDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت ، وزیر خزانه داری:
رژیم ایران با فریب زنده می ماند و شبکه شمخانی یکی از سودآورترین موتورهای آن است.
🔴
وزارت خزانه داری زیرساخت های مالی را که به رژیم اجازه می دهد تهدیدات خود را به امنیت ملی ایالات متحده و حمل و نقل جهانی ادامه دهد ، تعطیل می کند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/134241" target="_blank">📅 00:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134240">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw9lYtEYezsvQkB5UvoLpqRpZhw22igL1vTMvAYIVw4P-4gKNZXKFq6zjSsoDpsIYuN8_LpkyzlH07693YQ_KH1mays1eG-sMV3k8up31KHpsvR9aYxXXgeV_4YBLvOwS9UvBziRv7Y90oCNhjGCKi_11pqO0FIYiklj9L8i56G_oJ2VrlC6NOzPtvhlc0x7vDClFmsY1t9dmAdrUq-tgXKyr9lmMHuTaF1QTkHYO-ENp8dX8RBW9G3T-GnzJM2nAbJF_BydKwvF47Ewf7UnKwAsBlEgaePaxUSPzt5X6KQBSrdgkuCICd-rrlgEA0vx8_39EphFbOT4jEsFrL1lKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‌
کان نیوز: نخست‌وزیر اسرائیل بنیامین نتانیاهو قصد دارد در روزهای آینده به ایالات متحده سفر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/134240" target="_blank">📅 23:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134239">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5a29b67a.mp4?token=jLdHA69EKYJP7hJOrMjN_ERUfl26SLTgOWGdpt_ZKDjS9yiuUI_r9mdMiTUP8iPLdhWnCFkpFdFpOasiCSNg42wp_l3t_xQDFqRoqXAOaka6ZvoeVCQq5JMFM19mwDQtfIQgd1oe7IptSwaMdownAGABscpnBikcT9op3HWhBY82tZGYAEzzc9f9sxqdyAhrIBGQdh764WaPaY2Z0gxkM5hVSZZXDH2cuDIFVeqN1q0Xoh4f0YcV3ywvqgWuNyMKFi9hmnmiW3MF4oW29TNhAtshXUo1qE6wdY2ezef2uZKk9w-ylKlgJ92dv-QVEkQy63tlC5wBhDGBjhQCdt9xig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5a29b67a.mp4?token=jLdHA69EKYJP7hJOrMjN_ERUfl26SLTgOWGdpt_ZKDjS9yiuUI_r9mdMiTUP8iPLdhWnCFkpFdFpOasiCSNg42wp_l3t_xQDFqRoqXAOaka6ZvoeVCQq5JMFM19mwDQtfIQgd1oe7IptSwaMdownAGABscpnBikcT9op3HWhBY82tZGYAEzzc9f9sxqdyAhrIBGQdh764WaPaY2Z0gxkM5hVSZZXDH2cuDIFVeqN1q0Xoh4f0YcV3ywvqgWuNyMKFi9hmnmiW3MF4oW29TNhAtshXUo1qE6wdY2ezef2uZKk9w-ylKlgJ92dv-QVEkQy63tlC5wBhDGBjhQCdt9xig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل سوم اسپانیا به فرانسه توسط یامال که آفساید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/134239" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134238">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5a541186.mp4?token=kbeGERXWXrc5hY2nKGERs058tgzkmTz3n1YHqAE0ZwmE0yis9RinHyd-oQxTtRKDEK-7GrCxCymzmET4nVVct76G_831dryemTsytCVAFekP_b8F6iIjQLtVMfDpDXT9yZT0FC8FCgl_5bZ0BRs1z_6dU3JGaEOLK8aGfdR2v34AxKvEXzvA4Wkxs5r5WSlwu8xH4fEqm9cv6M_QPXiQVn5TN6PlHojCLPARl24LQ7Ut2iBcJOmpPrwLV3QUaDMraqZ23MrNp_oBQNcar92ZcJcCWKbru95qgmoLTQUJ_cOLXanY4sgKURze9rSp-WI9E6Wf4-EKLfK9jyIm7KRmjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5a541186.mp4?token=kbeGERXWXrc5hY2nKGERs058tgzkmTz3n1YHqAE0ZwmE0yis9RinHyd-oQxTtRKDEK-7GrCxCymzmET4nVVct76G_831dryemTsytCVAFekP_b8F6iIjQLtVMfDpDXT9yZT0FC8FCgl_5bZ0BRs1z_6dU3JGaEOLK8aGfdR2v34AxKvEXzvA4Wkxs5r5WSlwu8xH4fEqm9cv6M_QPXiQVn5TN6PlHojCLPARl24LQ7Ut2iBcJOmpPrwLV3QUaDMraqZ23MrNp_oBQNcar92ZcJcCWKbru95qgmoLTQUJ_cOLXanY4sgKURze9rSp-WI9E6Wf4-EKLfK9jyIm7KRmjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/134238" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134237">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc7SrDhrESBcHWpyJTSPq85z8neNUou6utf4F3eT3VEVtNIhduf6nOXjcaRfCpKc6gQNe076FL3i0X1jy27OjGX73TdsYMH-dzf3Jv-331eUeVH1Vkp61ZtXh9C6stkXfbfgcwwixoAqV-QujzKwv2b9otRBTl05ZCrwBq64oWREmmilqr44uYpPnBUcb1v0pZY-H_uo8XM0rDmTf63UQoTP3203YGWCmCUafKvRShfqx6lqZ1TreppZdrCfpuw15xpkRsyLY9qzFW5rO6yMQRV5IrBtUGSN_7THDUEg31rHZK97KxJL1pacpQ42NGyt2lLPl1sJRWrTp3DGkB5cXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعضای بدن یک جوان کورد در بیمارستان تهران
🔴
سمکو گلچینی ، جوان ۲۲ ساله اهل بوکان که چندی پیش بر اثر سانحه رانندگی در محور بوكان سقز دچار آسیب دیدگی شدید شده بود، پس از بستری در بیمارستان مسیح دانشوری تهران جان خود را از دست داد.
🔴
با رضایت خانواده این جوان اعضای قابل اهدای وی شامل ریه کبد و کلیه ها به سه بیمار نیازمند پیوند اهدا شد تا آنان فرصت دوباره ای برای ادامه زندگی پیدا کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/134237" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134236">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: پیش‌بینی می‌شود که نخست‌وزیر اسرائیل، نتانیاهو، هفته آینده به واشنگتن سفر کند، البته این برنامه ممکن است تغییر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/134236" target="_blank">📅 23:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134235">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
دقایقی پیش صدای انفجار مجدد در اهواز شنیده شد
🔴
در قشم هم صدای چند انفجار شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/134235" target="_blank">📅 23:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
گزارش شلیک موشک از کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/134234" target="_blank">📅 23:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alWBpG1t8QnpJwPyDWRVMjQPIMWONIZ8pxnL50Bfkv4KtAzzN-7O_yKznh8DpiRp1gdTMbdCZlVdTJruAQy9iEYwXpD0RfD1F2EZKQo-yEhzpmtiGyhWR9k2JNt502o1M692JbqcTQe2t3vOUwVKu4bCIHNUdw5dsKU9I41bNUSEEPKiFtdn3HY5DkYDGf_KdTLmyUUuvHAb5bOJe8paNLzSL6yCPHkpU_kyfTYFfUXH8M7UwykmpugmtglsRvtI9lEEbLQ2psApoVDXmYZWW3deUqPMN_NQeRqWZvzP64vEpKWIaZ3y2VcuHcaJI0g4T449aaM-NcjawCkpWzhMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی: ترامپ برای هفته‌ها مخفیانه در حال برنامه‌ریزی حملات هوایی گسترده و تهاجم زمینی با حمایت دولت‌های عربی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/134233" target="_blank">📅 23:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
انفجار مجدد در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134232" target="_blank">📅 23:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLLbDvJLJSQ3ixzWV5C0rttgz3UnqSvsLD_nAnNViD4YCb4rFfwTUJBOMeIGqkdevozb1wfMKZfIbf0YM6BD3ZrBu80Ma00dQDQsWmPC79pRepN0BaGedC-E0Ta9su1od7ivp3D43hKRHEYS5W7jjue-jyulMXEhegFJLFbUn72YpyvtOseFGdAWnrcxAoF2iY-lStwhVRzg7G3lvlOrBbYQiur9LWGC9M3-jnriXAMTYDAqmPWutuAAzzad3aFX-WnWhoG-773F6I9kPrt16wDFhkk39DdWyhTXsRBCW1pLbkHuGaKuebZR8Dbs1U5WczqXKZFeYG7XtqHzuji4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134231" target="_blank">📅 23:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
هم اکنون تمام واردات و صادرات ایران از راه دریا متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/134230" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری/محاصره دریایی هم اکنون آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/134229" target="_blank">📅 23:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134228">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ایرنا: همین الان بندرعباس رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/134228" target="_blank">📅 23:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134227">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ13OXkECVriFbSnJd-nnp6az0Wnv1rKo-12ACMUV-PVRiNVBPY6B_DU0IK0DSLlJkG4Bdr3SntkufNbvFol6Yc9S_jN0HcqrrcrsWr-TMKonXmIjo2VJJu-uqzsaI1mRw8on1wahIC3UUkYLYo-W3fL0vHSCBktBYB_92NzD2jfNV2LJpnVY1zViSXysmlDZ0M8KLSP6ZX8QkrFZu4PYDMs2aPzb2FKJkrv7NzXxQKbKXxEaLGpEyHJfptkdtcpIVtUQD0fHTum7GIbJiG4mDOuPfQGASICTNOsL3GB-dEPZLBGvGkt_L21Is2ljrOJ1h1jTCOkzAKRpRKX5xckGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا تحریم‌های جدید علیه ایران وضع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/134227" target="_blank">📅 23:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvMoPwTgR-G7IkAroH4qNAK8RClGkovwZFGj0Dz_j_mgIfB13VnT2yuWI1F3BEpgTE3kQa1SIzJtE57NEOC-GwhKI_bx5-AJrf8Q_bnP904SiMVXEsQ9DlfG2f9ga0_AYEjdj6tQvwZfw66qKPKUj_AS32a3GUyu-lCQaQMo7A2gzoJ8FoTs9lN-wN9sPeCuEME8W_4sALMxBRXq5G1-CuaaeCheLcoevTdViuxEn1hnQ9eWa9u_vT7ovttCCQJruL5t8YrGKydrZsIkUl9ZIsnivqD6LEHFHfJhiORfPbF-UAWgtk5l-OT1N8pTU_kUUzjxITdD2W-fkfT1SPDLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/134226" target="_blank">📅 23:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
آی‌۲۴نیوز
: مقامات اسرائیلی معتقدند که ایالات متحده در حال افزایش آمادگی‌ها برای یک درگیری تمام‌عیار احتمالی با ایران است، با منابعی که با واشنگتن در تماس هستند و برنامه‌ریزی گسترده‌ای برای بازگشت به درگیری‌های با شدت بالا را توصیف می‌کنند که ممکن است در عرض چند هفته رخ دهد.
🔴
یک منبع اسرائیلی گفت: «یک جنگ وجود خواهد داشت. تنها سوال این است که چه زمانی.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/134225" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✊
عرزشی‌ حرام زاده، مگر ۴۷ سال شعار «مرگ بر آمریکا» ندادید؟
🔴
حالا چرا نون رو به نرخ روز می‌خورین و سکوت کردین؟
🔴
اگر می‌تونین و اگر به شما اجازه می‌دن، یک تجمع ۱۰ هزار نفری برگزار کنین؛ میلیونی هم نخواستیم. بعد همان‌جا شعار «مرگ بر آمریکا» بدین.
🤔
البته بعید میدونم چنین مجوزی به شما بدن، چون این روزها شعار مرگ بر آمریکا دیگه به نفع حکومت نیست. همینقدر ترسو و بزدل هستین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/134224" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134223">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گزارش فعالیت و قدرتنمایی جنگنده های نیروهوایی ارتش برفراز تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/134223" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134222">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/134222" target="_blank">📅 23:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134221">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
انفجار در بوشهر و بهبهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/134221" target="_blank">📅 23:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134220">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK18YI3iP7t4TWwyEZRDCCEfWHkiSrF562yie2tHYKOu4UnQW_7VJPKh1YFMkJW5auM7B-d5wORfpKnbH5NvG8c82jFYLCO9gQW75Om-tV5prMmM2Lb5XclA4X0tXWxSmGZ4xzaBAofNwt95_G4muNP0WKCNsPS8dJVrzorc2FLRoDTy94b1gGOWXRnyKMxBif4b9c2mIcbon5iMp_xK2YeLSX75q_Uo-lOoGQyb2Rw7bF9MyY5LVA8ls8IQwVrOw2YihFYZHcKx4BFNTr5UHOXYEcrlam0uDsOFgRIkV1IbGYvVX6fwvNrGZtRNzrK_z4rLb2S5021SfHOsbAkyEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
عکسی قابل تامل از زباله گردی یک هم وطن
🔴
اما دغدغه یه سریا انتقام یه نفر به قیمت نابودی زندگی ۹۰میلیون نفر
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134220" target="_blank">📅 23:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134219">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
دقایقی پیش حداقل ۲۰ انفجار در جزیره سیریک در جنوب ایران شنیده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/134219" target="_blank">📅 23:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134218">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
غریب‌آبادی:
یک روز پیش از سفر به عمان، حدود سه ساعت با فرماندهان عالی‌رتبه نظامی جلسه داشتیم
🔴
در عمان درخواست ما این بود که مسیر جنوبی عبور شناورها به حالت تعلیق درآمده و موقتاً بسته شود
. در مقابل، با مشورت فرماندهان نظامی که مسئول کنترل تنگه هرمز هستند،
پیشنهاد یک مسیر جدید برای ورود و خروج شناورها را به طرف عمانی ارائه کردیم.
🔴
پیشنهاد ما این بود که نه از مسیر شمالی و نه از مسیر جنوبی استفاده شود، بلکه شناورها از این مسیر جدید عبور کنند تا هم امنیت تأمین شود، هم از بروز تنش و درگیری جلوگیری گردد و در نهایت، همه طرف‌ها به اجرای تعهدات خود بازگردند.
🔴
در واقع، جمهوری اسلامی ایران در این مذاکرات نهایت حسن نیت خود را نشان داد؛ اما در عین حال تأکید کرد که
استفاده از مسیر جنوبی، تحت هیچ شرایطی، برای ما قابل قبول نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/134218" target="_blank">📅 23:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134217">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvCRejVX64WcRs_5m7-12Entk5S5JU-7FUrCFu9w9Pq_Sk2o2D1JxxDIWZecG0PSg6xrKMpTaW_G-DLyYbvEEm8olKrCMTGDansrHQGDZzfNVv_zDq_Rei8NpHXY-vCZ_Dg5zvLUNttCsfNSElhviZMXz6vY7gAcZI3fWe6nnI3P7LrBniwxhnxg2kSLRzpl9S6-DfThXcCziLuqcvUGjyPbxdvWZC4CjDyNzThvMQINkACniISxAww02WltW-O-P7TA4yS_k4qs-72vkZ98tNnfTN7wNDmjluAcOc94_iK_BcZNzk_lYkQH8ZULJmIYgelX78o7HulepXZaGjVn4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: محاصره دریایی ایران تا ساعاتی دیگر آغاز می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/134217" target="_blank">📅 23:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134216">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/134216" target="_blank">📅 23:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134215">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VxWeeeiCbTGR4wq-IpPdp0VgI7dyLUoK1honRHed7mZGQggxE8psRmt-iwze0239Rj3giMPs_L8motGN2xPdodcGFOeOw3M8-Ie4xipfmGRdZYqTOsrQGa7rNFEWsXtm8nN3LfjeGB4_QrqxxqvWmlo98LTdgylmfxJV0oMjVAgzSimjYEzHjOwSKDjvosqvLvI0M5C_jCQAsVGaLs9J2NqNceAJDZGwmjHOoEpTJ1jht8sVAB50n7TZdwR0q1iQrZ0sm3-zAh4JSsq5JO2bosBzs81YwZZnGsiuz7TDQpgisKQFzm0rM7BVOFtGvRsm2YU8Soh5OcTP7Vq-uqILZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پخش زنده جام جهانی ۲۰۲۶
🇫🇷
👊
🇪🇸
▶️
کیفیت FULL HD
▶️
رایگان
▶️
بدون سانسور
🎥
شروع پخش زنده</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/134215" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134214">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
صدای انفجار در اندیمشک
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/134214" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134213">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
صدا و سیما: دقایقی پیش صدای شش انفجار در بندرعباس شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134213" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134212">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAhJNYUqxvPT5QxXLuslFqmZV9eoIzJzc1Z3XE1mSkAjAHs3Bb8qwH8Lv1ZTAK2kTPK_r6oW_wMurMYvPd6uw9IaLOLzYlEFjoHiYdFjGoPtpufrc2eqSe1P3L8qoK4L3Tb3c3JecFlB_x8oRXni51mCUZW9jaFaHr-3I5LJ-qIPlgoTD_Y0w4opOuLIUOG58c9Vf9wHK7ftcsgKolgT24rsJqjL36hgRPzIn2Dxnqxl47KU62vKiSNvUMhYV8AyahuBs6KnUImw6FvSKs-9PTp5TQuFT4o-pn2QpZHfu_e9JlEjSCfJkctPyS0b-77iDfVxN_DZwVBIa0o2biRVtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طالبان نماینده ی بوکس زنان افغانستان رو با این وضعیت به مسابقات جهانی بوکس فرستاد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/134212" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134211">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✊
عقل عرزشی حرام زاده
🔴
18 و 19 دی تروریست ها مردم معترض رو کشتن.
🔴
یکی نیست بگه اخه بیشرف پس چرا 47 ساله مدعی امنیت بودی. کدوم امنیت دقیقا!!
🤔
یه مشت دروغگو وحشی ان که فقط بلدن پیشونیشون رو با مُهر بسوزونن تا رانت بیشتری از حق بیت المال بگیرن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/134211" target="_blank">📅 23:11 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
