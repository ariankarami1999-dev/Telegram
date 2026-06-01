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
<img src="https://cdn4.telesco.pe/file/laAKNE_p4yaKYZSjCUOmJ3eHF5zWKTmnHslrGdPDpQPly5ytgmbGh-R3V_l5asTXjesJgvV6b7MxJkPcCTvbnHx3BqZlInrJWTQdRbop1DzY0GYT_fzWTpgfYPRROQBaVs9FiVEcf0xlV7G-9xOX3SvZ-fP4prt-MrKmho5pZ2xBv2rP3y7vGMccBLSn_e4nmJf7mBcPbGg3fNdxE_jyedu4Xqc6ooKIYPmkN9KQSBmZX9scyf0lKMnQuEJhMRmC9X0baoi499Z2zfqI4jKmlX72Q9Y-sjgVLcmo_xL_FdaTu-3_WPE6RFKqAo1EBvRkNDpAnXpY73oQlMhvHeGIFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-655309">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSBObIkW0qkZ0UBYyG3atzCtToEP5pXpJ0jDBx9xu9-HFVOgVXUDAQcy0kaRO_JULzPLIm7sVgYgglme4qXUGSeBFhi40hcxVtNTjR1taFlTV69mPSZwwjVthCQv3_nQyBYEG0FghkUl4vUrPRFrrzZeP0_Od_aZBYX37S4AoXQT2v92LQdikpe2WkDuI3927L_ewAYW_rOBuGP_Dfv7A0YV1PSTFsO1DI4Qi7fzOw4zniLWQ5NiDnEiV7vPITnA3MGH_sQnfHyvYwuBPAMVixJBwZCEF4ZIGerPqsvtlU7ztyEcnAWGIOEO8XRsLUV9ppEZa1zXH4oSiswVhR-Fpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حساب سازمان اطلاعات سپاه: هرکه باد بکارد، طوفان درو می‌کند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/655309" target="_blank">📅 19:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655308">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FivfXs0NLR8yS5zoL9vjZZJjJiTFl8P1Ccpi6DDYwSF5zhLfCBq8kHhx5UQF6YZybncQJIIGl_cHjnhmtwJ9N714JQs8XLkwJnPS2G0YxvAouk6yQYUHj0a2sC8UKRDTYqAQu2a-nhzfEmZliTiubwsy_rl3aRJhnX2o3rLz6uHoN0gsvVRFoGvPOl9rY4qJ7vjCcyPx5-oaFS-INekQojNSddlbzcNBMZWYznwLwKfFrWKJT_MXWmOba4NkN6v2ESiIwXWK6xbPSILJK8Yh8O9dsa7GrW71knDZep1IMhIIWTJhe1i6Byt-snm-AYtz1jMKo3bVDaoE9AbA1x9naQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضایی: صبر ایران حدی دارد/ ‏تنگه هرمز تحت مدیریت ایران است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/655308" target="_blank">📅 19:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655304">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8qazJoglHK4eBxV5BWJxpwdN6nJcEoOD5iub8K-wdF60cBeA9pzFXD0Jotqjt2c_HzK_9YBUkWvpODzy2V1rURWIsopVpka89evCQa27ZjYwgYZg6StkP_6s_3XvUbwjmQWbGLQ4Fsfyo1CipaLvf9z_2XUZyzc5oUCNu5JC98H4dwB3vanJCQI04xhcbeKFRkhgEPxUcRDuF7bZgrHxN1Jl1sUqhdVb1wi6bEZLIHCZc51rJUUVFsrzlhYf6BkKKXYyuY_E2i9ozcNIrlIahnOcNGUUvT2m50NGTsrLRFRJS7MsmemnOKNEM7nRk0uaD4DEbYtq__eXwlvXhQsCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf574d3d4a.mp4?token=iTADf2YQ2OkYAW6PW9SSiQfHCe7p-pWH34NiyS2AO2ETpvTEVwzyakbnZDS1vXWt9yYWAZp5FSwZhcvtmLzeJ5SXT21f52CPvrTRqS9HSUa2P-PTAw90kMnTqu5rTyPuiUhnStSIOuwzDXCEDNHAngRfHsKV2-iZmFGCYS6H-hY8SpbgPxL4Lvy-f33WLbizhHNdePFosS3myE7mMfdUMJu8yKHTzvWfxFTo6IaANuSxuHA6ciH5wDHKtchb_k35SMR0ODL3KgJU6oa-i4ksRGI6PP6m-po3K18A0_DD7GtPJ6usU1cX8bIgY_baMufTA6Xz6kCZj3d-Jw_N-p2Mcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf574d3d4a.mp4?token=iTADf2YQ2OkYAW6PW9SSiQfHCe7p-pWH34NiyS2AO2ETpvTEVwzyakbnZDS1vXWt9yYWAZp5FSwZhcvtmLzeJ5SXT21f52CPvrTRqS9HSUa2P-PTAw90kMnTqu5rTyPuiUhnStSIOuwzDXCEDNHAngRfHsKV2-iZmFGCYS6H-hY8SpbgPxL4Lvy-f33WLbizhHNdePFosS3myE7mMfdUMJu8yKHTzvWfxFTo6IaANuSxuHA6ciH5wDHKtchb_k35SMR0ODL3KgJU6oa-i4ksRGI6PP6m-po3K18A0_DD7GtPJ6usU1cX8bIgY_baMufTA6Xz6kCZj3d-Jw_N-p2Mcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله وحشیانه ارتش اسرائیل به ساختمانی در نزدیکی بیمارستان جبل عامل در صور هدف گرفت که باعث تلفات و خسارت به بیمارستان و اطراف آن شده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/655304" target="_blank">📅 19:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655302">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">امکان سرمایه‌گذاری در صندوق طلای «ریتون» به ویپاد اضافه شد
ویپاد، دیجیتال‌بانک پاسارگاد، در ادامه مسیر توسعه فراگیری مالی، امکان سرمایه‌گذاری در صندوق طلای ریتون (با نماد بورسی ریتون)  را فراهم کرده است.
صندوق طلای ریتون، گزینه‌ای مناسب برای سرمایه‌گذارانی است که با ریسک‌پذیری متوسط و نگاه بلندمدت، به دنبال بهره‌مندی از ظرفیت‌های بازار طلا با هزینه کمتر و به‌صورت غیرمستقیم هستند.
مشتریان ویپاد می‌توانند پس از ثبت‌نام در سجام و دریافت کد بورسی، از بخش خدمات پیشنهادی وارد گزینه «صندوق طلای ریتون» شوند و «صندوق سرمایه‌گذاری طلای ریتون» را انتخاب کنند.
ویپاد که توسط داتین توسعه یافته، تلاش می‌کند دسترسی به فرصت‌های سرمایه‌گذاری را برای طیف گسترده‌تری از هم‌وطنان تسهیل کند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/655302" target="_blank">📅 19:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655301">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان سرزمین‌های اشغالی
سرلشکر خلبان علی عبداللهی:
🔹
نتانیاهو در ادامه شرارت‌های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔹
با توجه به نقض مکرر آتش بس توسط رژیم، در صورت عملی شدن این تهدید به ساکنان بخش‌های شمالی و شهرک‌های نظامی در سرزمین‌های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک نمایند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/655301" target="_blank">📅 19:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655300">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZqfMtSkl0dprZjNcPEG10p-XEHpk5_GGFxZLprIvxixL38E_MkPcc7dGoI9EHLKHlSyGNhouxfy0Oj59gOlfL5845L_7nYMDll44Y69yWKuuPeJoApTjbPVguef05-tmWK1w-5F-O0mvgpr0ttK-1ZHi_HWBKnPWi5iRNzXc9yKkRlqYvi81o6w2Lc9hzI-T9iW_MsjCxyRnPiGNvSYc_tLCcK6k-A9NdAyMM2wdCTJ1iUAS6CRHGlF9GJI_fYMsNgWLtPRNTIzViG9rSp805CNufTnUAOQ6gK1l8T0TKpivPlLbkNSXznGBnIyhgUIKb2w6_XbHbiXiCelKnvE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/655300" target="_blank">📅 19:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655299">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزرای امور خارجه جمهوری اسلامی ایران با ترکیه و قطر درباره آخرین روندهای تحولات منطقه ناشی از حملات تجاوزکارانه رژیم صهیونیستی به لبنان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/655299" target="_blank">📅 18:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655298">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزرای امور خارجه ایران و فرانسه
🔹
وزیر امور خارجه جمهوری اسلامی ایران طی تماسی عصر امروز دوشنبه با وزیر امور فرانسه در خصوص آخرین تحولات منطقه ای، تجاوزات رژیم صهیونیستی به لبنان و پیامدهای این اقدامات تجاوزکارانه گفتگو و رایزنی کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/655298" target="_blank">📅 18:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655297">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe9be0f41.mp4?token=dcYoOWIIAEGIF_LMVzGsp7ctwbbojUBnGXwGj3XPopYQ3HQRf_Xbrm4G4N32NbJsTCQgLw65If3jO5jrWGNWukCHxcsh4HxQ05I7vYS-qHb567KbqnG2ii3Ogv87UU2939QH8f15UqHvyp3hivULH_Af7-G94md9XPEbeqmOMYs7P4VBcI7m27DrvE5oSL1Tq8-f111XvnQLMD93My-Q2mJnts1TVFrn3i2LiwUIXjP66AIWrd0_JJ8-Ctg0Ox3x8MXm_fb5liV_f_rfmjV5Mc6_zLaUYqF6ImM46LuG5WgxKpZNIaFcYtLPx9IFmHdhsX2Fsq6gdcrm44yOK7KLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe9be0f41.mp4?token=dcYoOWIIAEGIF_LMVzGsp7ctwbbojUBnGXwGj3XPopYQ3HQRf_Xbrm4G4N32NbJsTCQgLw65If3jO5jrWGNWukCHxcsh4HxQ05I7vYS-qHb567KbqnG2ii3Ogv87UU2939QH8f15UqHvyp3hivULH_Af7-G94md9XPEbeqmOMYs7P4VBcI7m27DrvE5oSL1Tq8-f111XvnQLMD93My-Q2mJnts1TVFrn3i2LiwUIXjP66AIWrd0_JJ8-Ctg0Ox3x8MXm_fb5liV_f_rfmjV5Mc6_zLaUYqF6ImM46LuG5WgxKpZNIaFcYtLPx9IFmHdhsX2Fsq6gdcrm44yOK7KLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیما پس از ظاهر شدن کلمه «بمب» روی بلوتوث، در میانه پرواز بازگشت
🔹
در پرواز یونایتد ایرلاینز به اسپانیا، یک نوجوان دستگاه فیت‌بیت خود را «بمب» نام‌گذاری کرده بود که باعث هشدار امنیتی شد. هواپیما به نیویورک بازگشت، مسافران دوباره بازرسی شدند و پرواز بعداً با خدمه جدید ادامه یافت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/akhbarefori/655297" target="_blank">📅 18:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655296">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c5ca40c9.mp4?token=u63pRXEYX_SWhqIJjVWv1ODOZOZogZN_GdHUEr15u2M0Ej6QWSFHJ3xVblh76ULijOW1nwJQCi2Sh96Fx6f2WlNO3mLDxIgjfL-_Oqb8Jz8Dnc2EPOW8sUnKHfJCsw8DQ5PpV8rBClbKjdEZcAaqjapXateGDlfUEwAhCCGJ6EENC8yt1_AdwqZgg4fM2SRiF4LBqck2QzvJ8wiF8L55rpA8OljZSP5U420C4N951sop3u3XQHCHWuPqwLrdpx_fF6dE36ZTUtA7XpDSDEdJym1xdf_JYQADBIZ-xDw9AiEMAbKAEK-ekz-6odb0fYGjhfx6MnLiyyH4asR9pWIdDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c5ca40c9.mp4?token=u63pRXEYX_SWhqIJjVWv1ODOZOZogZN_GdHUEr15u2M0Ej6QWSFHJ3xVblh76ULijOW1nwJQCi2Sh96Fx6f2WlNO3mLDxIgjfL-_Oqb8Jz8Dnc2EPOW8sUnKHfJCsw8DQ5PpV8rBClbKjdEZcAaqjapXateGDlfUEwAhCCGJ6EENC8yt1_AdwqZgg4fM2SRiF4LBqck2QzvJ8wiF8L55rpA8OljZSP5U420C4N951sop3u3XQHCHWuPqwLrdpx_fF6dE36ZTUtA7XpDSDEdJym1xdf_JYQADBIZ-xDw9AiEMAbKAEK-ekz-6odb0fYGjhfx6MnLiyyH4asR9pWIdDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعاتی پیش، جنگنده‌های اسرائیل بیمارستان جبل عامل در شهر صور در جنوب لبنان را هدف قرار دادند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/akhbarefori/655296" target="_blank">📅 18:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655295">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328f576871.mp4?token=o31haD21_SK0cqRFcJpm8ScK3OdhLrsKZ_NGW_kQmIU4kSZzv3YSJVp2WYy4S1dy49JUQg_97-zdW9qxD_MJv-Co0xwtTRc66Y20EqwBlEeBZd74y4DvCRSRi5N_S-dO304AeqinOO7Bi1TTZDvaxey93sRqcRICEEiv6_de-IS7qXGWYcaBhFMteSpjqmWug0sChXzuir5AfzulV_YIuuy-Mgp6BX9PNpWvsVS31HBLwB2Ltr2jD_q_21XLxQmbSABKqEEtqh4VdjRPAlo22kc0hmcZCXZ8OYRGwkP7shrGJnQj6QORebKi6Yz8qHJLOWqJ17KMMKaw-ogb_Ml9nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328f576871.mp4?token=o31haD21_SK0cqRFcJpm8ScK3OdhLrsKZ_NGW_kQmIU4kSZzv3YSJVp2WYy4S1dy49JUQg_97-zdW9qxD_MJv-Co0xwtTRc66Y20EqwBlEeBZd74y4DvCRSRi5N_S-dO304AeqinOO7Bi1TTZDvaxey93sRqcRICEEiv6_de-IS7qXGWYcaBhFMteSpjqmWug0sChXzuir5AfzulV_YIuuy-Mgp6BX9PNpWvsVS31HBLwB2Ltr2jD_q_21XLxQmbSABKqEEtqh4VdjRPAlo22kc0hmcZCXZ8OYRGwkP7shrGJnQj6QORebKi6Yz8qHJLOWqJ17KMMKaw-ogb_Ml9nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروتئین‌های کوچک کینزین عامل ایجاد شادی شما
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/akhbarefori/655295" target="_blank">📅 18:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655294">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f56rBLsEffiKZ6H4bOm567oMahE3dpU3BvCr1UdGQykv82m3v8DboQ6Lx2ydRmNWh9ndlYKmCNyemCKE1BWGlr11xQzyfqt5fE7zksqTv_gku0NvuFm4xNErrRe94ZsKrI2-h9hMpKSCNS-PudGRSBD_dhIrDb5CcZEoUIQlvSx92WOFKzNyBNbn-F6idOROOup1_LqO-lptyjDIC2Qi0jmSaRluNNTDRsNgJCVRUv8Ul8dERwRTRd3SX_RwpNCiRl7QKARAGzKsYcmKqQPjBNiYiDMnm6QX_9V3CZlJa5x9DOldgUYn1WdbLj8-EdPv9xtVkc6Iua84pGehio7Abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش‌مصنوعی معمای ۸۰ ساله‌ای را حل کرد که ریاضیدانان نتوانستند آن را حل کنند!
🔹
برای اولین بار، مدل‌های محرمانه OpenAI معمایی را حل کردند که ۸۰ سال ذهن بزرگ‌ترین ریاضیدانان جهان را عذاب داده بود.
🔹
ریاضیدانان پس از دیدن راه‌حل پیشنهادی هوش مصنوعی، از همان ایده الهام گرفتند و گام‌های بلندی در مسیر حل مسائل بزرگ‌تر و فراتر برداشته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/655294" target="_blank">📅 18:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655293">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شبکه ۱۲ تلویزیون اسرائیل: مسئول روابط خارجی سازمان جاسوسی موساد در پی تغییرات مدیریتی
🔹
سقوط بازار سهام آمریکا از بیم از سرگیری جنگ
🔹
پرداخت ۵۰ درصد از مطالبات گندمکاران به زودی
🔹
گفتگوی تلفنی وزرای امور خارجه ایران و بلژیک در مرود مورد مسائل منطقه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/655293" target="_blank">📅 18:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655292">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKinTYxbCYqKlVcjRc7lLOll0UniVHjZGwqLcK1WsZPYvOZ-UPCWL1FuSKRmaKI7qyx-w15UF-b6YYa869wbuQU7xiIpCLCOcgms7XYzzbxWcYSyZ-8rF3es9yIq73nnWx9jqmcffxDlt5DfA4Evb5PmdTpB5j-uC6oG0CiGc_FN4l_WyuPV4le9XnOcaNXoFARm6Z3ljzEn9i3HMfV-bWB4x5V0Q4eArkYNh-nJfClHXwRhA6n0ewneA3B09-6bTrH7drXYV6EOQnpnOaXNNRCZhmOY8a41kUGLX52ZG951kfmtQh2zAc4Xb0v8ANosRt1n2YBNiThVUKZJMhcK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با پیگیری استاندار آذربایجان شرقی محقق شد؛
افزایش محدوده تردد خودروهای ارس‌پلاک به استان‌های شمال و شمال‌غرب کشور
با پیگیری استاندار آذربایجان شرقی و طی امضای یک تفاهم‌نامه، محدوده تردد خودروهای دارای پلاک دائم و موقت منطقه آزاد ارس، علاوه بر استان آذربایجان شرقی به سطح استان‌های اردبیل، گیلان و مازندران افزایش یافت.
متن کامل خبر
👇🏻
https://t.me/araspres</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/655292" target="_blank">📅 18:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655291">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5hD37MpOjTWww7FcacfEgELIS511aBybEcU61KRK7worNzU7mq_hs5K5H66pw_jNA65YHwLA0wmtyKl0ru-SUDYp2Cpu2WjA_oyyVWeW3-zyFtoMNdnVQorE_JrfbF_jU6-fj_ABu1c5v_Ek2GgTLkFJHY9KGzOOYYKoXyB3hI8lhb3bOzm1wDkaGxRSTg-3aMsD7Zxi8HKCyvNG1nSc36tAJOsbMiIL9PkWrOGUt9bBC1wBAI35HWSwPivSwlpYiB9MAESyh6wGbNmab8RhDdme8mLveihDPyBCtUMXK0RZ0vwpGojY_fqaU9pMCf3DiydX4eHBUyeX7hJ4R89EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنکور الکترونیکی می‌شود؟ / بهای شکستن مدادها؛ زنگ خطر تجربه ۳ کشور در برگزاری آزمون‌های مجازی
🔹
در سال‌های اخیر قدم برداشتن به سمت کنکوهای الکترونیکی در برخی کشورها آغاز شده است. اما آیا ایران شرایط برگزاری کنکور الکترونیکی را دارد؟
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3219186</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/655291" target="_blank">📅 18:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655290">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTDBIAxPeyqkgSJZgMfKJeQn7C1zh8ZH-Mj8OvUsJOAC7xI27sP9jXP-D8A2UMDxPrMRwjuGwKn32djU8z1zKSO9R3xESeduGKmIX_qQKVlEnfd130fcbLA4fy3J67_hGhU1qmwogBfQPLLXBmZDu4ZbDHRCMdrTVxzcAQ2B9MfFQK4gCxWt8Nk-bZe6-Oao0JLJdwhM4Dcz1X8IPcbnsgyhhKQExlSN11KGSp4t9suoYHKup0GtGD2A_kGNydlAmdL4Dy_7ABWh-XTLu8n44msUNuMsLl-Nx0e-qinKc5R3g_BrhpMHihCwxOMZtzJgqoNiNUz2oiiZmz5ITSpYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت پرتابه ناشناس به یک کشتی باری در خلیج فارس
🔹
مرکز عملیات تجارت دریایی بریتانیا مدعی شد که یک کشتی باری در حین عبور از خلیج فارس، هدف یک پرتابه ناشناس قرار گرفته است. این حادثه در فاصله حدود ۷۴ کیلومتری (۴۰ مایل دریایی) جنوب‌شرقی بندر ام‌قصر در عراق رخ داده است.
🔹
بر اساس این گزارش، پرتابه به سمت راست (سمت بندر) کشتی اصابت کرده و باعث انفجار بزرگی روی عرشه شده است.
🔹
مرکز عملیات تجارت دریایی بریتانیا برای
دریافت جزئیات بیشتر درباره تلفات احتمالی یا میزان خسارت، با کشتی در تماس است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/655290" target="_blank">📅 18:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655289">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTp_KsV-IUokfrQphSddC5ZmKN9oNLcAeu2E7N6XCX2I4MvzbEAUTt7cxaQM1bzOkGrGSopFc48f3LSh_tuLF3LV3cj7G-GvQfihUIQImdXchEyrju9LoHRc2uv7MrbwBoa_s3kK0GQ47zsbkjgttGXkdl56HpaxPReZLfPdAo_ELZ0EMFoZHVVM2Wn8del0jhVMj2dj-J5Te5nyMPlO6copdj8HJ17mw4Adsf2a6bU16ANYkqFG73xl5UMmgFYibx_-hzEjl55PHz3fiHFFWVD4kdpucgb4Ry70MNB5xmQcEwcmHUDB8Zhnun-BJLX6F-o6h7TwLP9zWBMQv1Ymbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوهرشاد بیگم؛ بانوی دانش، معمار فرهنگ
🔹
گوهرشاد بیگم، بانوی نامدار تیموری و همسر شاهرخ، از تأثیرگذارترین زنان تاریخ ایران بود. او فراتر از یک ملکه، سیاستمداری هوشمند و حامی بزرگ فرهنگ، دانش و هنر به شمار می‌رفت. با پشتیبانی از عالمان، هنرمندان و معماران…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/655289" target="_blank">📅 18:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655288">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDQugKOLkAXT_K3_1Up_qlajr8itou2Vcxd4IBtR6cbYojoMc6_bFnyYH2OULxEcmLFy5DP-twCdvscG-XnU4IviMRiIdGo36HpNlLC0_a2T0ID-TGfWDaXpLWySIoXeRYCq_POyeWvRHjYlBmiJMkTEZohlyrtNBSMUYceQKDBEXJko7eYjZ5Z0o-d4cA5DnEBtM5bvphTw97yJlVrlSBwkGacEGOI4mbIUotf5yX386w1LXnEmJi9SDF1HhjwL4Dxs4b6AYEAsVK1CtTwE4yKzdb-xWqGkT0iZR1KUnzFGdE1f4bkNJH0aSz9mTAaP-bqf8WbKz4u5lY3MgIzhGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
اشتراک اسنپ‌پرو
یه انتخاب هوشمندانه برای
صرفه‌جویی بیشتر توی هزینه‌های ماهانه‌
است. تخفیف‌های هیجان‌انگیز و ارسال رایگان سرویس‌های «درخواست خودرو»، «غذا»، «سوپرمارکت»، «فروشگاه» و «دکتر و دارو» از مزایای این اشتراکه.
🔥
🎯
اگه هنوز اسنپ‌پرو نداری، کافیه وارد سوپراپلیکیشن اسنپ بشی، روی سرویس اسنپ‌پرو بزنی و با خرید اشتراک مورد نظرت هوشمندانه سود کنی.
🔗
خرید اشتراک
@Snappofficial
✅</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/655288" target="_blank">📅 18:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655285">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سخنگوی ارتش رژیم صهیونیستی: ما به حمله در سراسر لبنان از حومه جنوبی بیروت تا صور ادامه خواهیم داد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/655285" target="_blank">📅 17:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655284">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سوء‌تغذیه در کودکان؛ ۳۰۰ هزار نفر مشمول حمایت می‌شوند
احمد اسماعیل‌زاده، مدیرکل دفتر بهبود تغذیه جامعه وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
طرح امنیت غذایی کودکان سه سال است که انجام می‌شود و امسال بودجه این طرح حدود ۲.۵ برابر شده و حدود هشت همت برای این کار از طرف دولت بودجه گذاشته است.
🔹
براساس این طرح کودکان مبتلا به سوءتغذیه که دارای پرونده در مراکز بهداشتی هستند یا به مراکز بهداشتی مراجعه می‌کنند، شناسایی می‌شوند. یارانه امنیت غذایی برای این کودکان به حساب سرپرستان خانوار واریز می‌شود.
🔹
این عدد سال گذشته چون بودجه کمتر بود برای دهک یک تا پنج یک میلیون و ۳۰۰ هزار تومان و برای دهک‌های شش و هفت فکر می‌کنم ۶۵۰ یا ۸۰۰ هزار تومان بود که امسال این مقادیر افزایش یافته است.
🔹
تعداد کودکان تحت پوشش با توجه به افزایش بودجه نیز افزایش یافته است. امسال قرار بود که تعداد آنها به ۳۰۰ هزار نفر برسد؛ درحالی که سال گذشته ۱۸۰ هزار نفر تحت پوشش این طرح بودند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/655284" target="_blank">📅 17:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655282">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol1d_J5nXjgn_J3204jhJwRwC1qabcEUxyxt-KiVv9vLJSJvBsY7ro7dMsiSRvLRR75iI3KwKu1S8YmindhVaS-iV0BetgSI-yxhYz2Tmtt5Ji4VC3QxcrqKVNF4igSw2tgia-hTZnSa8w14G-cgnYbExen9920JaTjtBCM2wA8W-NtxQmV-ax0yWocfC4Bg5OrDS82VO7ould4saXwQY0L_5R2NFrsuACUwosnmlHxHij9qpQNl1yybTDY9RA5XwssC-PuwCMg7Cd7d615xuxkEXpLQu4HmgM24XC9QgzCsgHyf69YZd2bn6c1QITksdYxDLTy-_Yb7DrMpw8T-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
در پناه ِ غدیر، در کنار یکدیگر هستیم
🔹
در یازدهمین جشنواره مردمی اطعام عید غدیر همراه ما باشید...
🔸
با اجرای: مژده لواسانی و امیر مهدی باقری
🔸
با کلام: حجت الاسلام برمایی
🔸
با حضور: حسین حقیقی
🔸
با نوای: کربلایی علی اکبر حائری
✨
وعده ما: ۱۴ خردادماه از ساعت ۱۹ هم‌زمان با شام عید سعید غدیر در خیابان فدائیان اسلام(بین چهارراه نخریسی و چمن)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/655282" target="_blank">📅 17:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655281">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
برافراشته شدن پرچم عید غدیر در حرم مطهر امام علی(ع)
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/655281" target="_blank">📅 17:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655280">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ارتش اسرائیل برای ضاحیه بیروت هشدار تخلیه صادر کرد
🔹
ارتش رژیم صهیونیستی در فرار رو به جلو، مدعی شده اگر حزب‌الله به حملات خود ادامه دهد، صهیونیست‌ها هم ضاحیه بیروت را بمباران خواهند کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/655280" target="_blank">📅 17:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655279">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: امتحانات نهایی احتمالا بین ۱۳ تا ۲۱ تیر برگزار می‌شود
🔹
تاریخ قطعی برگزاری این امتحانات بعد از تایید مراجع ذی صلاح اطلاع رسانی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/655279" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655278">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
نماد کشورهای مختلف در جام جهانی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/655278" target="_blank">📅 17:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655277">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIuGbD3D-Jke6G4JMHIZgoBbkLoc03Jp0qaJAhwlYbdvGT45VHjeajVSYPXskyN1b_cNi-4vHUHSUPP4VmaZhYAioixwe-vJZrKIY8l6XLT9MZqsNGN9CcL_ywHnHYeulZ6m_Uvk04Fi1FTWpvX98LGVGbR29seZgVAwzhebc7j8m0AFekpfQ2xQzv52XPrt1AvRSjaFyEwd8Dpzig5ktDBhz0CmlLPfrD4XopzNUAXfkk0z7nzdlpcbKsLrBsejYQgl0bXJ2u0dm_39oWd_Zeuflk-UgAfXmAJybSdNve34m8gkZenR8Vtq8Bmvwf26futC8_AzPe4k_BX2RuL7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای فاکس‌نیوز از آخرین مطالبات ترامپ از ایران
🔹
ایران باید بپذیرد که هرگز سلاح هسته‌ای یا بمب نخواهد داشت.
🔹
اورانیوم‌های غنی شده توسط ایالات متحده شناسایی و نابود خواهد شد.
🔹
تنگه هرمز باید فوراً و بدون دریافت عوارض باز شود.
🔹
ایران باید همه مین‌های دریایی را جمع‌آوری یا منفجر کند.
🔹
محاصره دریایی ایالات متحده برداشته خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/655277" target="_blank">📅 17:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655276">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b1982b32.mp4?token=M_uSqUE40YymWAkJF2cN3T3Lg7kWAFpiodzL2mt4a3Z-FZDN8L-m9du9acP27mtqerVgbC1NVoBGzsFbBOadh1DlZvBBplkGSNKmCgIA6gq46l4uv1MoWctuFqJwiaNWPXmsrGWPAuIGFu8QAarq4jIJFljnNCYNIBWFdsqFyjpJRcBoQrz4Tb2SxeFPknlb3GZb3FH_bfki2pELn1pGt_-SvX3Cwi0RzV6e-nrl-x8l_r-7hEdGAihQraAr1L1PIst26Q6lczZhavybtpR7HyyYiL7xFqem5dnjjIBj3ZQbeJkG0k2tqo1_bk3UAwTMPHa5KbDgZ9wD_2lSaY_WpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b1982b32.mp4?token=M_uSqUE40YymWAkJF2cN3T3Lg7kWAFpiodzL2mt4a3Z-FZDN8L-m9du9acP27mtqerVgbC1NVoBGzsFbBOadh1DlZvBBplkGSNKmCgIA6gq46l4uv1MoWctuFqJwiaNWPXmsrGWPAuIGFu8QAarq4jIJFljnNCYNIBWFdsqFyjpJRcBoQrz4Tb2SxeFPknlb3GZb3FH_bfki2pELn1pGt_-SvX3Cwi0RzV6e-nrl-x8l_r-7hEdGAihQraAr1L1PIst26Q6lczZhavybtpR7HyyYiL7xFqem5dnjjIBj3ZQbeJkG0k2tqo1_bk3UAwTMPHa5KbDgZ9wD_2lSaY_WpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارخانه تولید مواد آتش‌بازی، خود صحنه آتش‌بازی شد
🔹
منطقه ساحلی سالینا در کشور اروپایی مالت امروز صبح بر اثر انفجاری مهیب در یک کارخانه تولید مواد آتش‌بازی لرزید؛ انفجاری که ستون‌های متراکم دود را به آسمان فرستاد و به املاک،‌ ساختمان‌های اطراف و خودروها خسارت وارد کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/655276" target="_blank">📅 17:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655275">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69515842e1.mp4?token=ctIzZe405wRx3WI_Y4xPNTaBnu2AoSTaGe7TH2_SDu-DLaixf2mV0eU2-uwVJE4doZmzl9aTTLdjN_ZLQW5IXMIpoVg3nFAGO0V4uvOYNfjLBmmcmkLMRUkWIz5JuVOLhvChJu8hkZ8iR7im1QIvSWtlhAX8IEj-CY3unVIHJ4IGMHrQDQvLHQ9NWAuY314OzUaPMoqcGdDePjE-SX2OlNbm7OtxhTVq8FHRmmx6oVPDnwENoXOEbyr5pJmG2rZWl1IMZlCS-XnYuw29cVLEuSknyrrjy5grJyTlPdNcOxdsSmZl9AzgVYpDQXi_ZYZ97OL9U09E4s9YGtwJmJGUlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69515842e1.mp4?token=ctIzZe405wRx3WI_Y4xPNTaBnu2AoSTaGe7TH2_SDu-DLaixf2mV0eU2-uwVJE4doZmzl9aTTLdjN_ZLQW5IXMIpoVg3nFAGO0V4uvOYNfjLBmmcmkLMRUkWIz5JuVOLhvChJu8hkZ8iR7im1QIvSWtlhAX8IEj-CY3unVIHJ4IGMHrQDQvLHQ9NWAuY314OzUaPMoqcGdDePjE-SX2OlNbm7OtxhTVq8FHRmmx6oVPDnwENoXOEbyr5pJmG2rZWl1IMZlCS-XnYuw29cVLEuSknyrrjy5grJyTlPdNcOxdsSmZl9AzgVYpDQXi_ZYZ97OL9U09E4s9YGtwJmJGUlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در جنوب تل‌آویو
🔹
یک حریق گسترده در منطقه‌ای واقع در شهر ریشون لتسیون در جنوب تل‌آویو به وقوع پیوسته است.
🔹
تاکنون جزئیاتی از علت بروز این حادثه یا میزان خسارات احتمالی منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/655275" target="_blank">📅 17:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655274">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMTr04A7eqjVJkTXjoIwo46i50MyEREVUxISxghWE1kvlrWCYAT8JepLAWfQHu1MCeGiK7JvRyfZPSA8hk1H_fJcXouM8f7-WC3Ae-_pdZ7_dY9oe4FiEeI_WLN7lyAwE9Mgz7vw14hkQchr8go7cW1jIJgRCGGZHsfvrUeFBfrvlWIL171zKn1JoDZ5J9nllPX0xDaIc-QTks-XlnF3wfRJ6KNuflHtZDDnMpXnYerWU-B1Rj0BUIQ4EAu-62pAWS8MFwCnUBu8hlXXPd3380g1goFJCM4k0kMXZpuvPX9uuM3nvMvQo-z138_ULicVyDJ9bCLw5uUDxDX5zQpF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوری/ ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند
🔹
با توجه به تداوم جنایات رژیم صهیونستی در لبنان و با عنایت به اینکه لبنان جزو پیش‌شرط‌های آتش‌بس بوده است و هم اینک این آتش‌بس در همه جبهه‌ها از جمله لبنان نقض شده است، تیم…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/655274" target="_blank">📅 17:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
داروهای حیاتی و کمیاب را از کجا تهیه کنیم؟
محمد هاشمی، سخنگوی سازمان غذا و دارو در
#گفتگو
با خبرفوری:
🔹
در اجرای سیاست‌های کلان نظام مبنی بر تسهیل واردات و پایداری تأمین دارو، کارگروه ویژه تأمین کالا با هدف مدیریت فرآیند واردات هماهنگی با گمرک و بهبود حمل‌ونقل تشکیل شده است تا موانع موجود در مسیر ورود داروها به کشور برطرف شود.
🔹
در شرایط حاضر داروخانه‌های منتخب دولتی و بیمارستانی به عنوان کانال‌های مطمئن و جایگزین برای توزیع داروهای حیاتی فعالیت می‌کنند.
🔹
همچنین شهروندان می‌توانند برای استعلام لحظه‌ای موجودی دارو و یافتن نزدیک‌ترین داروخانه دارای اقلام مورد نیاز از اپلیکیشن تیتک استفاده کنند که این سامانه حتی در زمان‌های اختلال فنی نیز به عنوان راهکار جایگزین عمل می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/655273" target="_blank">📅 17:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwkmyKRdcFMdX3zmwAPJ249OyJlMGXVIYxOst31cJZu6rvQX0rVLYvki82-pC7LjKGTP7hrgPxFxFr-WJe7_uBt_OKjXa3YtsMAx88lROAOsltZVXwqp8asrKZhz2R1labNO1g79gM-HmQMRLfbl2q17hPZ7xl-7BTgxrsV6X1MWMfN5gQh1KNP7CuTKynkgx-6X1tA09p8TFwbmGQqs27FKoZYkjZh8t7HQTfCE96t5bAsQk61vM8947tFiMGQK28IL92hJQDZYLDQiY25DoSg8nUK8RL-71Y0Vkf8fUL8DnVNjT55TDbh00oCEUDBtunWREdvDZMZnnlNr-02jTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانال ۱۲ رژیم: دادگاه عالی اسرائیل به اختلافات پایان داد و به‌طور نهایی انتصاب "رومان گوفمن" را به عنوان رئیس آینده سازمان موساد تصویب کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/655272" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06ff15d4f.mp4?token=stLO-1jJI62xgjK_GwW3hdg4nV8y0JUj3EWvOv2hnkZpRVprK8Ep5oBtQnLaUyjDlZm_zItdm3QuTB6fV6EjforThrKjMzZVaVyHe_xwRiFMZs_RwOuaktdV1K9Mp7sgR7hIX4tlmCj_7t3P1vB__bEaaJtBuNaeqmx7NnQBCIfgBF3PfHups5YKjh5tVI7pjUrQ8ooBedsLEm5qCN2VnYHWcElBamKQjYItUf1IcwnWkgJtIPm6qgJNSC0TbUuwsg4cg3i2BIL8uWttuVXnduDji-SPlUIgPHGBUk3WHbm4fvoffLOLazqegg_iydjov7bdlbMeHudzR_BYYmdK_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06ff15d4f.mp4?token=stLO-1jJI62xgjK_GwW3hdg4nV8y0JUj3EWvOv2hnkZpRVprK8Ep5oBtQnLaUyjDlZm_zItdm3QuTB6fV6EjforThrKjMzZVaVyHe_xwRiFMZs_RwOuaktdV1K9Mp7sgR7hIX4tlmCj_7t3P1vB__bEaaJtBuNaeqmx7NnQBCIfgBF3PfHups5YKjh5tVI7pjUrQ8ooBedsLEm5qCN2VnYHWcElBamKQjYItUf1IcwnWkgJtIPm6qgJNSC0TbUuwsg4cg3i2BIL8uWttuVXnduDji-SPlUIgPHGBUk3WHbm4fvoffLOLazqegg_iydjov7bdlbMeHudzR_BYYmdK_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: مردم آمریکا برای گذران زندگی، پلاسمای خون خود را می‌فروشند
الیزابت وارن:
🔹
مراکز اهدای پلاسما در سراسر آمریکا شاهد صف‌های طولانی از شهروندانی است که از طبقه متوسط هستند و تنها برای بقا به این کار روی آورده‌اند.
🔹
بسیاری از این افراد درآمدهای حاصل از فروش پلاسما را صرف هزینه‌های حیاتی مثل خرید خواربار، سوخت خودرو و بیمه اتومبیل می‌کنند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/655271" target="_blank">📅 16:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede4f9d1e7.mp4?token=Ca3rmb1rLPBeXpefKmbKvV8iES0qgwl0KTREPifheidlrpGYeKKAqXPeqJpSyc3VJwHCrHp3A0UJghfPoSF_uFMGhXnX1Wycu62E8loZHLs8KQ93MniThfXIOY0ZoYkWH_DXlPe98qmcXx3GdAQZdhodrkmvrI6K9lBIFpein8yJ7n1Pm0bxXmZv0NI_17mwIIKqRakJ4TqP7EyGny9QC0rGgCJJzhhPx4JwRv0gilFLTiZy4WEH_BT9xcaA3jxD4o5KgYYbn1BHQUpp9Qk2c3bo9QRVijnGm-acLjBDmqsQkTAQ-npBltZRH1nhfMqtuSro5IQFU1H7IeWaQ-0-PjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede4f9d1e7.mp4?token=Ca3rmb1rLPBeXpefKmbKvV8iES0qgwl0KTREPifheidlrpGYeKKAqXPeqJpSyc3VJwHCrHp3A0UJghfPoSF_uFMGhXnX1Wycu62E8loZHLs8KQ93MniThfXIOY0ZoYkWH_DXlPe98qmcXx3GdAQZdhodrkmvrI6K9lBIFpein8yJ7n1Pm0bxXmZv0NI_17mwIIKqRakJ4TqP7EyGny9QC0rGgCJJzhhPx4JwRv0gilFLTiZy4WEH_BT9xcaA3jxD4o5KgYYbn1BHQUpp9Qk2c3bo9QRVijnGm-acLjBDmqsQkTAQ-npBltZRH1nhfMqtuSro5IQFU1H7IeWaQ-0-PjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راشاتودی: آمریکا سوخت‌رسان‌های خود را تا پایان سال ۲۰۲۷ در بن گوریون نگه می‌دارد
راشاتودی:
🔹
۶۰ فروند سوخت‌رسان نیروی هوایی آمریکا در فرودگاه بن گوریون و ۱۶ تا ۱۸ فروند دیگر در ایلات، رامون پارک شده‌اند. آمریکا قصد دارد آنها را تا پایان سال ۲۰۲۷ در آنجا نگه دارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/655270" target="_blank">📅 16:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655269">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y204ofiDKIUixYivhRBnyXIpl3lphdallBZzsS6AU_20NrEL58jfWw9gjhQQRS247jVePbxI8kSHggdkyiMwq6UQG-y8--QbH_P_MWCTKkEOg3a5Iao4H9bC_TSSC-MSEDM0RA3thGIU3tXKbxPkrlkc0oSPT2GPzoaQ93stAcc2Bg5aeQ19H9hSCHWn8tvkoSa2JYTfdlwk3pYwDhpQ980WyAwHaQiOGRDWM6zfG1CfzZHDBDgqqmSvSbfrJFgJiJC6nRvOYDWCZrmB_llwEppQYmtFnARQSJe7WFwUkJtBrmrOsAdLShDl76WZWhFReOxCVbrlb3OBySQ0IVbeag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای باراک رواید: اسرائیل، آمریکا را مجبور به پذیرش حمله به بیروت کرد
آکسیوس، به نقل از یک مقام آمریکایی:
🔹
تلاش ناموفق روبیو برای آتش‌بس در لبنان می‌تواند واشنگتن را وادار کند تا به اسرائیل اجازه دهد به اهدافی در بیروت حمله کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/655269" target="_blank">📅 16:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655267">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
فوری/ ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند
🔹
با توجه به تداوم جنایات رژیم صهیونستی در لبنان و با عنایت به اینکه لبنان جزو پیش‌شرط‌های آتش‌بس بوده است و هم اینک این آتش‌بس در همه جبهه‌ها از جمله لبنان نقض شده است، تیم مذاکره‌کننده ایرانی «گفتگوها و تبادل متون از طریق میانجی» را متوقف می‌کند.
🔹
توقف فوری عملیات تجاوزکارانه و وحشیانه ارتش رژیم صهیونیستی در غزه و لبنان و ضرورت عقب‌نشینی کامل رژیم از مناطق اشغال شده در لبنان توسط مسئولان و مذاکره‌کنندگان ایرانی مورد تاکید قرار گرفته و تا زمانی که نظر ایران و مقاومت در این زمینه تامین نشود، گفتگویی در کار نخواهد بود.
🔹
همچنین، جبهه مقاومت و ایران عزم خود را برای انسداد کامل تنگه هرمز، و فعال کردن سایر جبهه‌ها از جمله تنگه باب‌المندب، به منظور تنبیه صهیونیستها و حامیانش در دستور کار قرار داده‌اند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/655267" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655266">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249ee45c8a.mp4?token=WWOSyOMNbZuRhVi48Hz7M6WGlwgAJT7VK2BlC1cB3nxBJsaQQ5DOfbtvC50g3iWc0r-MQ4tgd_H5cpSqmfPNkCgMCTU3W4hrc9pTkVNPXZPXSkSZKfBv6-fV0jqAdTZ2cE5VO8L558RgWBXyHbtFoJvJOr0jqjr77mUOGTm58gPpRMGENQP5SJ2OCHaFoI6aroAJ1ELvcue7z6nCJzkIWK-9LuIzEBdRFmwwEAlv7bIsSzawqeXjQqqFCP8ptAynO2sn_3PVXfrb_8F546E_m3w5ROW7kd6NLUyDdvZFihvTb6XKfw150HgcMpqaTBwc-YvhT-ZHjVZeGdw7yzHQgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249ee45c8a.mp4?token=WWOSyOMNbZuRhVi48Hz7M6WGlwgAJT7VK2BlC1cB3nxBJsaQQ5DOfbtvC50g3iWc0r-MQ4tgd_H5cpSqmfPNkCgMCTU3W4hrc9pTkVNPXZPXSkSZKfBv6-fV0jqAdTZ2cE5VO8L558RgWBXyHbtFoJvJOr0jqjr77mUOGTm58gPpRMGENQP5SJ2OCHaFoI6aroAJ1ELvcue7z6nCJzkIWK-9LuIzEBdRFmwwEAlv7bIsSzawqeXjQqqFCP8ptAynO2sn_3PVXfrb_8F546E_m3w5ROW7kd6NLUyDdvZFihvTb6XKfw150HgcMpqaTBwc-YvhT-ZHjVZeGdw7yzHQgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در یک نفتکش با پرچم پاناما در آب‌های سرزمینی عراق
🔹
سی جی تی ان از انفجار در یک فروند نفتکش غول‌پیکر با پرچم پاناما در آب‌های سرزمینی عراق خبر داد.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/655266" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655265">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
انفجار در یک نفتکش با پرچم پاناما در آب‌های سرزمینی عراق
🔹
سی جی تی ان از انفجار در یک فروند نفتکش غول‌پیکر با پرچم پاناما در آب‌های سرزمینی عراق خبر داد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655265" target="_blank">📅 16:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655264">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
قیمت کله پاچه پرواز کرد/ هر پرس پاچه گوسفندی ۳۸۰ تا ۴۰۰ هزار تومان
🔹
بهای یک دست کله پاچه در بازار به دو میلیون و چهارصد هزار تومان رسیده است؛ در حالی که فقط پنج ماه پیش، هر دست کله پاچه یک میلیون و چهارصد هزار تومان قیمت داشت. هر پرس پاچه گوسفندی (شامل دو پاچه) بین ۳۸۰ تا ۴۰۰ هزار تومان، مغز گوسفندی ۳۰۰ هزار تومان، بناگوش ۳۴۰ هزار تومان و زبان ۴۴۰ هزار تومان قیمت دارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/655264" target="_blank">📅 16:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655263">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4902b84e17.mp4?token=H4iTPUAGzPIkbzOmiCq8KcavmKa2CQ4g36aRxJJblW19qJ1OvaO8DthkcRqZVBvxJvdjTqOgkf9DoAqe9DfwcfEwNlbutFQ8A0rvqT3JrCVEeUYpyNB872YUZ9pM9TtTtUs-8i1m-bLpKSr1ciYGzgYi4BsRmNvym3hsTksbcBGxk0tHe74N_golc5z3Detu6UEl1fNmue8Meuhxk9QSnzQ60Ph8yHDL_P629R20HETwl-emQPEN-Iqm7bz1HRQsUuC-_xiqvCCNbM-kRwjZcv0rIDV6f1L0W9VUTsyHmzlWh4QmAVt52vo9wqhZ10QUzaDm004gAE5-RulYPN-dbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4902b84e17.mp4?token=H4iTPUAGzPIkbzOmiCq8KcavmKa2CQ4g36aRxJJblW19qJ1OvaO8DthkcRqZVBvxJvdjTqOgkf9DoAqe9DfwcfEwNlbutFQ8A0rvqT3JrCVEeUYpyNB872YUZ9pM9TtTtUs-8i1m-bLpKSr1ciYGzgYi4BsRmNvym3hsTksbcBGxk0tHe74N_golc5z3Detu6UEl1fNmue8Meuhxk9QSnzQ60Ph8yHDL_P629R20HETwl-emQPEN-Iqm7bz1HRQsUuC-_xiqvCCNbM-kRwjZcv0rIDV6f1L0W9VUTsyHmzlWh4QmAVt52vo9wqhZ10QUzaDm004gAE5-RulYPN-dbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی عجیب ماشین
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/655263" target="_blank">📅 16:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655262">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7FAHOwhNe8UD_qKy1zZWXyuJnj67o97eauyaei6395dLbCgJt4zc1fZ8p51A8jp3OoYCB0gl_vhpaBHjYP48Fi6oHIDFPBJVEIoLZD54ye-29QSP7gBGMKSOwIwFGUgrIHL65aIwKhAIxnYsD9iHQNhtIzV1wMBNjLTQOhd-bE-bdXxslIMvcPkNKm-qH9oVxfpKCXulH24CTZg8nVlwheSnh-oGFJPWsosK_GXEPkus-1LfjyIvm2f_h1dsM4ntui0xhZk2xmYQu91qfLXM_rUMU1PIaW5x2SvnVYMl3cJstinXztFOdAysfVUXSeyljFti1sEmsXtoUP2tcduOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو هیات‌مدیره و معاون فناوری اطلاعات تاکید کرد:
✅
«ردبانک» محصول نوآورانه بانک شهر برای ورود به نسل جدید خدمات مالی و هواداری
🔀
حسام حبیب‌اله، عضو هیات‌مدیره و معاون فناوری اطلاعات بانک شهر، از ورود رسمی «ردبانک» به بازار خدمات مالی دیجیتال خبر داد و این محصول را گامی نوآورانه در مسیر توسعه بانکداری هوشمند، یکپارچه و متناسب با سبک زندگی کاربران توصیف کرد.
🔀
به گزارش روابط عمومی بانک شهر، به گفته حبیب‌اله، صنعت بانکداری در سال‌های اخیر با تحولی جدی در انتظارات کاربران مواجه شده است؛ به‌گونه‌ای که دیگر نمی‌توان بانکداری دیجیتال را صرفاً به ارائه نسخه الکترونیکی خدمات سنتی محدود کرد. آنچه امروز اهمیت دارد، طراحی تجربه‌هایی است که در عین برخورداری از دقت، امنیت و کارآمدی، با نیازهای واقعی، الگوهای رفتاری و حتی علایق کاربران نیز هم‌راستا باشد. در همین چارچوب، بانک شهر با تکیه بر ظرفیت‌های فناورانه خود، «ردبانک» را به‌عنوان یک نئوبانک هواداری با رویکردی متفاوت طراحی و به بازار عرضه کرده است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/655262" target="_blank">📅 16:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUHnRcbjYRdUt6gFfbpFk6PC58g9wfRv0cRZbj4UcgGgtmhc9bQiaoyocVAyUJxZzUq-vGTN9qBhfGLYNWYMS7AMmLJDxAIBfEDSDzC-51e564uW5DuMzir2oj0t7ZhDPsOeCA0WSFjUG89TOWdRF3xl6doPXxxg6b8meD5kC6V6Wd5MhivcEc19WGkbmGENKtHN-7-mV2Z88fAjWXusRhSkJ5CNh3OM646j3GLieOPL2O8TuAmrHAvD-5XF5WjJBSHJqbh3xRaZ4Y3lmuwjS4AIp5VrfStGpwofaH4lvIizOKfWAIHVz_QGLIKsFtfjjdg4n99L6pstPm0ZtadQrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وزارت امور خارجه عمان: ما هدف قرار دادن کویت را محکوم می‌کنیم و حمایت خود را از اقداماتی که این کشور برای حفظ امنیت خود انجام می‌دهد، ابراز می‌کنیم
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/655261" target="_blank">📅 16:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
پزشکیان: نقض مکرر آتش‌بس در لبنان، تداوم آوارگی شهروندان لبنانی و حمایت‌های سیاسی و نظامی آمریکا از اقدامات رژیم صهیونیستی نگران‌کننده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/655260" target="_blank">📅 16:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تامین اجتماعی ۵۰ تا ۷۰ هزار میلیارد کسری بودجه دارد
فضل‌الله رنجبر، سخنگوی کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
اصلاح ۱۲ ماده از قانون تامین اجتماعی در دست پیگیری است که برخی از مواد مرتبط با تقویت بنیه مالی سازمان تامین اجتماعی در کمیسیون مصوب شده و برخی هم به کمیته‌های تخصصی ارجاع شده است.
🔹
۵۰۰ تا ۶۰۰ هزار نفر از بازنشتگان کشوری از مزایا یا بهره متناسب‌سازی حقوق ناامید شده‌اند و بی‌بهره مانده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/655259" target="_blank">📅 16:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655258">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZVTgejgTIiJSwQu1T0MAsO0uF_rP_IBHU3zXutwJ3ExporBqi70_GKN5QePzfHgS-PBLleXlm8M8fWRfnQf6aiGVa6iy_lXXgKIAxEBYAcBiGkYzAUQ1qjdhkXrgujUoVmpRdRCS9U6jiVp-D-WY1tuvAmon8O3z9I5H7KMaeRCV8XEvL9lILTaMkM7Oo83XKA6PLlUFWbWLvuokeUhgC8ZV9AcDmKgCtzSu-8BM27TOFhykP12Z--P670pROcEbUQ-zyKT1W_MzcRRNgKTA1iCr-NV_pexhan6PWbawBfmH3FuOxdNkqaO2ec0jWNkrUP8g1iAuEUv-WjZEObWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سنتکام: ایران پایگاه آمریکا در کویت را هدف قرار داد
🔹
شب گذشته در ساعت ۱۱ شب به وقت شرق آمریکا (صبح به وقت تهران)، نیروهای ایالات متحده با موفقیت دو موشک بالستیک ایرانی را که نیروهای آمریکایی مستقر در کویت را هدف قرار داده بودند، رهگیری و منهدم کردند. همچنین هیچ‌یک از نیروهای آمریکایی در جریان این حمله آسیب ندیدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/655258" target="_blank">📅 16:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655257">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03336c5a7f.mp4?token=Y2WK-DR_DAGJzuAQ0GFeOUv33nXxj20C-jVSVqVS85opIGEz_D9wYew_z_MZBBUVuy_4sZXU7rmgBIa2z_tkxQjXMWgu9IiB1YSD_2rcMCdPh_vraugMhRa0NsiOQF29aof4Rha6c9ghvxLJ4hVicL9obUzV-MTx0QkDINHOBMAZLqjO8xn4Zjghd69hcGARMSoG6v8NHfpM7mwbU99oTikLUlBCJ25rvaVWjFxhnhfy7cfkC5tC2NRaWjF4AkQoThburyOc0eWj-R7PrOPr7XpOXL3ajm4VIF-bYL7a0xxTNvz6KtX-c2IOkJD0Dr3f3YVJKfPYewcANwpDPKFd7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03336c5a7f.mp4?token=Y2WK-DR_DAGJzuAQ0GFeOUv33nXxj20C-jVSVqVS85opIGEz_D9wYew_z_MZBBUVuy_4sZXU7rmgBIa2z_tkxQjXMWgu9IiB1YSD_2rcMCdPh_vraugMhRa0NsiOQF29aof4Rha6c9ghvxLJ4hVicL9obUzV-MTx0QkDINHOBMAZLqjO8xn4Zjghd69hcGARMSoG6v8NHfpM7mwbU99oTikLUlBCJ25rvaVWjFxhnhfy7cfkC5tC2NRaWjF4AkQoThburyOc0eWj-R7PrOPr7XpOXL3ajm4VIF-bYL7a0xxTNvz6KtX-c2IOkJD0Dr3f3YVJKfPYewcANwpDPKFd7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور سرمایه‌گذاری حرفه‌ای انجام بدیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/655257" target="_blank">📅 16:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655256">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIB5jKnWkdThs-liWv-oN3n6-mlFK1-7k3gL3griX5BXrdVo8X1024ZVnYrk7krdNsN8oHtFANWDjbVCA3J5RsXICQY2B7iPGNXmlem6_vy5-LS2DH5VlY750iLzn3gdX6XWv7ta0ZH5S6JknzUed3gaG5C4VsVgcLFi1Y9Fab2TnKeKCxz3dXDc8R_mPGjjcZE86fnCx_2klbnDywGwbQsOJOrvJUHcUqi8fDCW2gsZWTQhVCXXCzE0YyZNW1Vu8dyosfSxSntZy5dWUkVflqdZflwv_Hs3ssW1gB-VAwiNiWy-rXt7ryOHXXn4CAvlATO8W7AD6R76rFBA6YcFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
چرا رقبایتان همیشه جلوترند؟
چون از قدرت خبرفوری استفاده می‌کنند.
✅
تبلیغات در پربازدیدترین کانال‌های خبری
✅
پوشش همزمان سراسر کشور و استان‌ها
جای شما خالی نباشد.
همین حالا پیام دهید
👇
👇
👇
@newsadmin</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655256" target="_blank">📅 16:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655255">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMp6s-kCaHJDoaWmj8GfKTcCuXIZ1R23KvQi3ZSzzBQwQKsWED6dlkPvshf-GyxqsxzhFXbEhH8vdiAFItIAsaQ8tErlT--bfEevqxd3OChJqfk98WdicZuOnEFJYxhSye2cqQfoXw1HRNMDlYV4u8M-echbefeBXLM4NP_SEyQsR0f0FlYnR_4OmfAJ_-VhRnaQ-63RyBgzkoluuN2001t9rWZmF1IP2M0ycZlJM-I6buQqTIWq2d3E2rUAMs3xIGVabdV5bMYEY33JJPCUBPWugvl67YOTJNfICtpB8tNWNWGfxSa3C_LXchtWZO4y4lBaTdVK0n5gLUNropnDGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۲۳ درصدی هزینه‌های درمان و ۲۰ درصدی لوازم خانگی
🔹
بررسی جزئیات تغییرات ماهانه قیمت‌ها در اردیبهشت نشان می‌دهد گروه «بهداشت و درمان» با ثبت تورم ماهانه ۲۳.۱ درصدی در صدر جدول افزایش قیمت‌ها قرار گرفته است.
🔹
پس از آن، گروه «اثاث، لوازم و خدمات مورد استفاده در خانه» با تورم ۲۰.۳ درصدی بیشترین رشد قیمت را در میان گروه‌های اصلی کالاها و خدمات مصرفی به خود اختصاص داده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655255" target="_blank">📅 15:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655254">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350197d19c.mp4?token=fEa5On1AEf2-G1BGhjb81rhHa7I19Loj233CsiwkWOH0Mpc7m1m2wjwVqB-hJo1nV_cNpX_SVLJbypj-9FmCeNDIOmeY-lVrMFQ5spZXCym9sn2OPs9nvfFzmzgCjTpwcPkYoy5TdVU1HLxoXIrrU789yz4pSzTyqvAKd0iqXb0acHnPojKQ28G-Gb5fUNTNFGfcgE1W2TJGOJ1sVgVqcWL1jkquFl7S_-en-kIFsUIoN5JQPQl_L2IPonUX_e7K6jgMu1iQHEegi6F85TGkyQiJmcMBZGa-A5qYKxxZ_FuVpVyQX7SuZxGmotzVWI-3F0NMmbfRRE6NHov_noGGkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350197d19c.mp4?token=fEa5On1AEf2-G1BGhjb81rhHa7I19Loj233CsiwkWOH0Mpc7m1m2wjwVqB-hJo1nV_cNpX_SVLJbypj-9FmCeNDIOmeY-lVrMFQ5spZXCym9sn2OPs9nvfFzmzgCjTpwcPkYoy5TdVU1HLxoXIrrU789yz4pSzTyqvAKd0iqXb0acHnPojKQ28G-Gb5fUNTNFGfcgE1W2TJGOJ1sVgVqcWL1jkquFl7S_-en-kIFsUIoN5JQPQl_L2IPonUX_e7K6jgMu1iQHEegi6F85TGkyQiJmcMBZGa-A5qYKxxZ_FuVpVyQX7SuZxGmotzVWI-3F0NMmbfRRE6NHov_noGGkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس خیره‌کننده آرتمیس ۲؛ غروب زمین از پشت ماه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/655254" target="_blank">📅 15:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655252">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmo9h1ctN4HB46VN_k_KiHaLMqNEeGoDVrdOgatEie7qgqo2GJNv1gMmbjNQLFfEgaJ8fMq4yoBQBgxR5pMpdHXwgfSxEmj2-hfWHbNjwfkDB998VhiJ1PJ3Vj3Ws23yWmPw3M37KYioADsYX_BLv3Y1z6qv2_Qh4QYUwmps7TtAacsISwAG7v3YpOzA2Hh96vPf9TUtlWFfwI6VfPIbD6dwbJHohBWGD9kYFsPUaefBSaOYoOnL6bB9llDeFY230bNdvzmkAppya7Us3SKnENYmNtSEMhE_mrTTUZlF-4sA7F1Dqs9nHg4JMmrqsnvGxBYFI_XTIrHvtdBJkFyRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فهرست تیم ملی ایران برای جام جهانی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/655252" target="_blank">📅 15:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655251">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYuRfsoy28KB733EhqzZvfPsUFSEr2QYnsssgOgBBmVGV-VA4jCcP9b9abtqR05nqrhcjqZLldPTAvmzVXgZvgWBwveWKEu3NrttMOQGUmVUYeK9Jaou7Dj5kB8p3VHuPOAi6RgXRebemTxkP-dlFdVZ3hPQASdTPr_2vhwfKkh553MthS4DZm_DSQjfms-I263RMJKZAyc_9hP35OMOHghqCW9d35aWZ85ATDUimL8A1JYGy1icpJglldavEPDhG4RU3UOArDnWaSmZuuEx490IxEJIF2R3sRt5TTa2YFBYC8K2uk5qJK006FnZ9Ktwu4LUrAL4W19Fcvb-5PT-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانگین قیمت بنزین در آمریکا ۴.۳ دلار شد
🔹
جدیدترین داده‌های انجمن خودروی آمریکا (AAA) نشان می‌دهد میانگین قیمت خرده‌فروشی بنزین در سراسر آمریکا به ۴.۳۳۶ دلار برای هر گالن رسیده است.
🔹
بر اساس نقشه منتشر شده، ایالت‌های غربی آمریکا از جمله کالیفرنیا، واشنگتن و اورگن همچنان بالاترین قیمت‌های بنزین را تجربه می‌کنند.
🔹
در حالی که بخش عمده‌ای از ایالت‌های جنوبی و مرکزی مانند تگزاس، اوکلاهما و لوئیزیانا در زمره ارزان‌ترین بازارهای سوخت قرار دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/655251" target="_blank">📅 15:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655250">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYxVi-ThRkBqZqMVM15EdDAVVYVjTKa7whKehKqFFDKMt-vtnLy-wwcexuOzUa4JfA8b01Qm2OCCFFKpjQKc7XlWCDqycT7Eh0TNqHjtSxzLCRwTyE2hYz8XZMb-8AEaeIspN9Cpx8Udi9aJjsW4yY-srxStDHiYKLcEP3tmt9libcrYZuOz_v-28DpxH1OEi6NiAUWrIMwAjHjvViDoewVkxpFR1TeON6OBgWWQXiJP2wObzZxmKWbBrP3oplEcaR4SxiLdKjof8GocNLfVoqIz09kTATk0Q_CDbYVPl4_hgg_jrkX9woOhoSD7vUsqsZvBf-nfEsiJVTG6qWYoaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گنج پنهان در کشوی خانه‌ها؛ موبایل‌های قدیمی از معدن طلا ارزشمندترند | یک موبایل چقدر طلا دارد؟
🔹
گزارش تازه‌ای که با استناد به داده‌های سازمان ملل منتشر شده، نشان می‌دهد تلفن‌های همراه قدیمی و وسایل الکترونیکی بلااستفاده می‌توانند به منبعی بسیار ارزشمندتر از معادن سنتی طلا تبدیل شوند.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3218959</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/655250" target="_blank">📅 15:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655249">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b90681b9.mp4?token=RLjjeGhrdJuXZ6wa1qmhYygtzzPoAam8okeEMlRV_FHX5jYCDDeDGB_yffbyoKuMO9cdDG6Z3_jK9RVob9afJiN9YZvYVMLb3wCxUTxXTg8JzbNN3es8fXY5Cg1oFAzrpcRWv3IZvAROcGMS7OFFX-QzFMN_R8TJBMToW5eR2Ng0D5VoOuvmpNday6LkM4pgxhntMI689HIs7zaRLnJkrnC_SmItTf1n1vqBn-ykM0F9dGEPh6qGDBqRwtkeP6J8PqjOF697UJa5koRpFztOKD8XLh-JDwReeiN9Yf_DWv0Sq0Oa5ll6WUkW6DXnL-bxoWCUsFOR3Z77SqQ-YM5wCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b90681b9.mp4?token=RLjjeGhrdJuXZ6wa1qmhYygtzzPoAam8okeEMlRV_FHX5jYCDDeDGB_yffbyoKuMO9cdDG6Z3_jK9RVob9afJiN9YZvYVMLb3wCxUTxXTg8JzbNN3es8fXY5Cg1oFAzrpcRWv3IZvAROcGMS7OFFX-QzFMN_R8TJBMToW5eR2Ng0D5VoOuvmpNday6LkM4pgxhntMI689HIs7zaRLnJkrnC_SmItTf1n1vqBn-ykM0F9dGEPh6qGDBqRwtkeP6J8PqjOF697UJa5koRpFztOKD8XLh-JDwReeiN9Yf_DWv0Sq0Oa5ll6WUkW6DXnL-bxoWCUsFOR3Z77SqQ-YM5wCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین با موفقیت مجموعه‌ای از ماهواره‌های شبکه چیان‌فان را به مدار پرتاب کرد
🔹
این پرتاب، ششصد و چهل و هفتمین پرتاب برای موشک‌های سری لانگ مارچ بود. برنامه چیان‌فان شامل استقرار یک مجموعه ماهواره برای ارائه ارتباطات پهن‌باند و انتقال داده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/655249" target="_blank">📅 15:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655248">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اسرائیل‌الیوم: قانون انحلال کنست در جلسه عمومی تصویب شد
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/655248" target="_blank">📅 15:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655247">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaba8e3b0c.mp4?token=tlmcDClPVxGLHfVmxvbfBpRWUx-3rOd4_0PTyqge0b50r2ruvRNq1oyD6e-5v2AGv5LXs6-OV_d-UV452xrtF4NDgnDxy833S7hOP9FOLCNRVIvUsU774mVpEytGammacxM5UEoOEnfBC9McFpJl7739TsHBye_WEGM15xZBPlW-0FU3Cpkgvj72gB3fWD8YVbZu6T_iwkGYKsdNL84vCjX1fB50qx48w0V4KZ-F6VR4OKt3s8tcgpqQmTx97d194w9CcSwAd1eE_qsrabyrzXZKvc2Ptob5Nsqmdcr5yHgxoQ2q2LB52EtQZKXv2eJpAuRZJg-ofnHJMyQR9q3hIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaba8e3b0c.mp4?token=tlmcDClPVxGLHfVmxvbfBpRWUx-3rOd4_0PTyqge0b50r2ruvRNq1oyD6e-5v2AGv5LXs6-OV_d-UV452xrtF4NDgnDxy833S7hOP9FOLCNRVIvUsU774mVpEytGammacxM5UEoOEnfBC9McFpJl7739TsHBye_WEGM15xZBPlW-0FU3Cpkgvj72gB3fWD8YVbZu6T_iwkGYKsdNL84vCjX1fB50qx48w0V4KZ-F6VR4OKt3s8tcgpqQmTx97d194w9CcSwAd1eE_qsrabyrzXZKvc2Ptob5Nsqmdcr5yHgxoQ2q2LB52EtQZKXv2eJpAuRZJg-ofnHJMyQR9q3hIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهگیری و انهدام یک فروند پهپاد دشمن در آب‌های سرزمینی ایران   سپاه پاسداران:
🔹
بامداد امروز یک فروند پهپاد MQ1 ارتش متجاوز آمریکا که با ورود به آب‌های سرزمینی ایران قصد انجام عملیات خصمانه داشت، بلافاصله در رصد و هدف موشک‌های پدافند سپاه قرار گرفت و سرنگون…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/655247" target="_blank">📅 15:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655246">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
نرخ تورم اردیبهشت ماه ۵۳.۹ درصد شد
بانک مرکزی:
🔹
نرخ تورم در ۱۲ ماه منتهی به اردیبهشت ماه ۱۴۰۵ نسبت به ۱۲ ماه منتهی به اردیبهشت ماه ۱۴۰۴ معادل ۵۳.۹ درصد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/655246" target="_blank">📅 15:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655245">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
رسانه‌های عبری از شنیده‌شدن صدای انفجار در حیفا خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/655245" target="_blank">📅 15:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655244">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بسته‌ شدن تنگه هرمز با دنیا چه کرد؟
🔹
بسته شدن تنگه‌ هرمز زنجیره‌ای از شوک‌های غیرقابل باوری را به اقتصاد دنیا وارد کرد که از خاورمیانه شروع شد و به تمام جهان رسید.
🔹
همانطور که در این ویدئو خواهید دید کسی فکر نمی‌کرد که این تنگه کوچک بتواند این‌گونه نفس اقتصاد دنیا را بگیرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/655244" target="_blank">📅 15:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655243">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e03864b8.mp4?token=kbcoK4Yjyi8WdCKtGc54Zo9AXEp80Jw1nxk0plr4cf2xGRQFq2xUzIHcNjMVithFB0Pz6q9EUwb6F4rMbJA6oGcGR8CZGcLYJBxcen1H9MmRrsFDIO4NZXiALMc2y_eXwsra2flHN_1gLEuwEYx0N3YIMLB6UQuu9GjsXL-nHaHY8SXgEUovKRNjOLm3vQQE752OdcF4legKYvvyWXj798q0GPQ5csibgAh_xdr5cN-xfs70XRIvTOyS6SrTYByDlJMuQULH7BTBcFkgQYVz3M2j4lTWiiMsvQUXmhvlSaOJ54y6gwAzcf4mvWlvpxlrcvRWxBpOFGy42xT0A6jWgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e03864b8.mp4?token=kbcoK4Yjyi8WdCKtGc54Zo9AXEp80Jw1nxk0plr4cf2xGRQFq2xUzIHcNjMVithFB0Pz6q9EUwb6F4rMbJA6oGcGR8CZGcLYJBxcen1H9MmRrsFDIO4NZXiALMc2y_eXwsra2flHN_1gLEuwEYx0N3YIMLB6UQuu9GjsXL-nHaHY8SXgEUovKRNjOLm3vQQE752OdcF4legKYvvyWXj798q0GPQ5csibgAh_xdr5cN-xfs70XRIvTOyS6SrTYByDlJMuQULH7BTBcFkgQYVz3M2j4lTWiiMsvQUXmhvlSaOJ54y6gwAzcf4mvWlvpxlrcvRWxBpOFGy42xT0A6jWgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از یادبود شهدای میناب امروز در آرت گالری ونکوور
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/655243" target="_blank">📅 15:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655242">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
تیزر قسمت چهارم، فصل چهارم
🔹
سید ابوالقاسم احمدی از تجربه‌ای نزدیک به مرگ روایت می‌کند که پس از ورود به کما برایش رخ داده بود. او توضیح می‌دهد که در آن وضعیت، احساس جدایی از جسم، مشاهده صحنه‌هایی از زندگی خود و مواجهه با فضایی متفاوت از دنیای مادی را تجربه کرده است.
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید ابوالقاسم احمدی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/655242" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655241">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqosHYIZ0jRNZz2yAqNbt-hFr4sRj51QnT3WSVb-nrsFdyBodHkPcuQhtuJUzjuegPEG0SrCX3hVWZzN7U_h5aUroHBY5356blaLvByzdA6QP-2rei0zF5_fGa2Gd2kr0lVOBbis5IZ0-Ck9erudMFXvvK4UcyrybSa-quxp2yuHLJyfeALKyOPfrzM5yF_Fi_4H9Zhaqs7J7l57giYlqWEX2P6ps6urkIUL8H689RTMLxj0OhkATDGD6Qwk0vITibcyTJQrEslrlNqcrmmQ5Nz06YRfqhmGNiIhVzz8qOM5H3DOz8oZHQUJyEDqn63bZ67o8ULlpPufgDyw6toiwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی، عضو تیم مذاکره کننده: خیلی مهم. صبر ایران دارد تمام می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/655241" target="_blank">📅 14:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655240">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix2s019ddFGdSJSYc7JqDU27SuuTlkjk-Zgp1MYRqsp_u_0512z1GFO_MYkdFBRr3_7lk1yWgcFa2MFnU7aKzKVKuck2xft9kG3O4NausXhdPNOwd0ho4WYpzp4OJAiJAtsBYyoR24hBss9J5lV5NBZYD4TTGXBL52gnnkeIjQV8DPDjcqkUU0wmjwaneIH6epcA9qxSKp79CI70Wu6_pTWQF2cv5Zl9QAHdYeVspft-Q2SlQIPD5J5RKhb20TtdHYuisCjiP5T9sKPMMmdJBf-87YE-Bfdi7bmko_8VvrpMydeIuqewB0LO_cRVMqPg7MJjIyielA-M_1WovQS5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ بهره ۴۰ درصدی شد
🔹
نرخ بهره در بازار بدهی به کانال ۴۰ درصد رسید. در تازه‌ترین عملیات بازار باز، بانک مرکزی تنها به ۱۳۰ همت از ۳۱۰ همت تقاضای نقدینگی بانک‌ها پاسخ داد.
🔹
هرچند تقاضای پول نسبت به اوج ۶۰۰ همتی هفته‌های ابتدایی جنگ تقریباً نصف شده، اما عرضه نقدینگی نیز از محدوده ۲۲۰ تا ۲۴۰ همت پیش از جنگ به حدود ۱۳۰ تا ۱۴۰ همت کاهش یافته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/655240" target="_blank">📅 14:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655239">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwuSdjiT-0KHDwVkbHakLblVw2nH6fu-IcPnJB3YI0AWnP0etrc3-zRl3h_35SDF7GfsXLK_yjYv8T-mK6jiAMSHUOFkVcbnS0mb_v_5MnQFfocxF4enzsCWdmfxkjFsUUJYww9_D88FcIRrUWbw6JHCNqatDdMxrcZgaFdotoKqZMS1x94lLTL-ZvDH3Vc_Bl0c1dvcKVoCJVPmJr-0h7EQEDSQuCkYoU1D4fDNw7hHKgPFD8hRm4uJySwT9sGMjdBVlk4qXU0Rz6Wni3If24u30PK4TU6_NUf82v_T2AviovAEXottwj30VTAm3rlFQozAkRmoLHyFunM9TL-8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک چریک بیخ گوش ترامپ | مردی در آستانه قدرت؛ چهره‌ای میان امید و تردید | ایوان سپدا کیست؟
🔹
ایوان سپدا هرقدر هم آرام و شمرده صحبت کند، از یک اتهام قدیمی رهایی پیدا نمی‌کند؛ اتهام نزدیکی به گروه‌های چریکی.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219294</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/655239" target="_blank">📅 14:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655238">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOk0fV4kYEpU6KyfzGm-Oh69SthSzeJUQJzvdhgqi2sGbExZSsZamSan8S_VWuWBPCMzUkdr9y6YUrQQPOFF9PUPw6afXQVmUhYcn8GNbYz14szpnjIEa77FQwvlX2RUOLGMYnF0XLzrh4S0Vwo73f4UoeM8q5-0PY8i_k2uroPNV7AEawt263qJnUPuiXDKxEQUwoL36ctQgrTF_O-o8lCsj8amptaqyDSPH_n5F3_S3uXf_9m4Q1p1OZ7qtogwkUchcqeP4V_vKLE-MRE-BXhzalbwycq6nuz55mGa4GanP6Fw4t3PyeKEwMb1gzFB7sjWFNek0N5qYGRnuIY1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: نقض آتش بس در یک جبهه، نقض آتش بس در تمام جبهه هاست
وزیر خارجه:
🔹
آتش‌بس میان ایران و ایالات متحده، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.
🔹
نقض این آتش‌بس در هر یک از جبهه‌ها، به منزله نقض آن در تمامی جبهه‌ها است.
🔹
ایالات متحده و اسرائیل مسئول پیامدهای هرگونه نقض این آتش‌بس خواهند بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/655238" target="_blank">📅 14:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655237">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
رئیس کمیسیون اصل نود: افزایش حقوق کارگران ابلاغ شد
پژمانفر:
🔹
این افزایش بر اساس مصوبه شورای‌عالی کار است و با ابلاغ وزیر وارد مرحله اجرا می‌شود؛ امیدوارند اثر آن در حقوق و مزایای خردادماه دیده شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/655237" target="_blank">📅 14:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655236">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b189c11abb.mp4?token=uyHCKcjfktrFCWRRWSHb178qmljlEi3_WR1dQ3RV3usjzMNAjcpuzNzvMI5-c__Al-LFMaGJrTA8swCFXci6g5fd1mqYlojQK9JYxwAZQne1refvivRS-G6pOfMUoru3-kKZblQDDjdXIu_6w2oeEO8BeoC8AMJYu-I-72Rq_H4lTmjkx313v4k-r0BlZND378cZF9EKPluvjvN8_QtcPFZaossfqhkM0XKtp-DS2jnlCT5BmCsu0TNn5ei9ebDyEWpBwJWPK4yWhXbLdSLUpkDYVArgCLcnuos1SrfiqnbGSfTxcZbI-lTRrJDhFkPcqH23mQXePw_Yd4DDJckD_I9PHFXjVKaw-1EYR1SDjasHgrqZj9s3XJwZIGreJTUwovqgx_TtppZo_kYhne5hoHaLXTDibaVhwSU0CMDWd0r6Jq_wAdph4r3C4VJeIxOiCaxjVntDudi2goGOVoN614IlCSpagIoW-tayK221f08c1Wq6ZVuxr6yB5YauJr-8rvGen2cu5E1-pY2KJq34BvXltMV5nf2FuGKpnDpnpAwUEObLC0iToPmWaoxNxFgNwhbV-p5MD871SKbC7enXiahc7eJLd5EysYsYVFuIQ1sxfSooE4akEQ1CHTcpR_myidFzpCtawoJdjyIu7ftN2DGmNvLuwWKZPoCEFNVOVU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b189c11abb.mp4?token=uyHCKcjfktrFCWRRWSHb178qmljlEi3_WR1dQ3RV3usjzMNAjcpuzNzvMI5-c__Al-LFMaGJrTA8swCFXci6g5fd1mqYlojQK9JYxwAZQne1refvivRS-G6pOfMUoru3-kKZblQDDjdXIu_6w2oeEO8BeoC8AMJYu-I-72Rq_H4lTmjkx313v4k-r0BlZND378cZF9EKPluvjvN8_QtcPFZaossfqhkM0XKtp-DS2jnlCT5BmCsu0TNn5ei9ebDyEWpBwJWPK4yWhXbLdSLUpkDYVArgCLcnuos1SrfiqnbGSfTxcZbI-lTRrJDhFkPcqH23mQXePw_Yd4DDJckD_I9PHFXjVKaw-1EYR1SDjasHgrqZj9s3XJwZIGreJTUwovqgx_TtppZo_kYhne5hoHaLXTDibaVhwSU0CMDWd0r6Jq_wAdph4r3C4VJeIxOiCaxjVntDudi2goGOVoN614IlCSpagIoW-tayK221f08c1Wq6ZVuxr6yB5YauJr-8rvGen2cu5E1-pY2KJq34BvXltMV5nf2FuGKpnDpnpAwUEObLC0iToPmWaoxNxFgNwhbV-p5MD871SKbC7enXiahc7eJLd5EysYsYVFuIQ1sxfSooE4akEQ1CHTcpR_myidFzpCtawoJdjyIu7ftN2DGmNvLuwWKZPoCEFNVOVU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده از فک‌های بازیگوش که روی کایاک‌های گردشگران در نزدیکی نامیبیا می‌پرند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/655236" target="_blank">📅 14:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655235">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SW39GLE-WvRKsQC1DVyvYM4DdCuSAoigyjDkf0hL51KAy5q1NldImMiJl6qsEwPAmXOI569bHg43jL8kvRLCDHfoJhfdAi3JmkHVonfg2aHttO7Tj3Ya5Hwv-DQJiDo4VxbqIMFffamdbpZy7lnxba9pCyO-Ky4mQKmY_KPiSdrH7uhh2s7qP7xvKRn0B3jDQkmoCyzdcCnddvhT--8vZsEuVC2cPW99C-BYsNEaR2D20sTf8j3oUiiFJaKVIurh7Gz-BS0lFnkDKJoX-IThTadIeJ6WtgbIYP7R0iHt7lPHYyWcOyE_AfrFOyL4Xb4qkb3et9rcnhl2Y9lJSkRnGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شماره تلفن‌ها و راهنمای تماس‌های مهم و ضروری در سفر
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/655235" target="_blank">📅 14:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655234">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سردار شکارچی: تداوم جنایات در لبنان برای نیروهای مسلح ایران قابل تحمل نخواهد بود
سخنگوی ارشد نیروهای مسلح:
🔹
رژیم متجاوز و کودک‌کش صهیونیستی با سوءاستفاده از فرصت آتش‌بس و تجاوز آشکار به خاک لبنان، بیش از ۳ هزار نفر از مردم بی‌گناه، از جمله زنان و کودکان را به خاک و خون کشیده است.
🔹
درحالی که حکام کشورهای غربی، راهکار سکوت یا حمایت از این جنایات ضد بشری را در پیش گرفته‌اند.
🔹
به سران رژیم ددمنش صهیونیستی و حامیان آن، هشدار داده می‌شود تداوم جنایات وحشیانه علیه لبنان، برای نیروهای مسلح ایران قابل تحمل نخواهد بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/655234" target="_blank">📅 14:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655233">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
دیدار تدارکاتی ایران و مالی؛ ساعت ۲۰:۳۰ پنجشنبه ۱۴ خرداد
🔹
تیم ملی در ادامه برنامه‌های خود در اردوی آنتالیا برای آماده‌سازی حضور در جام جهانی ۲۰۲۶، دومین بازی تدارکاتی‌اش را مقابل مالی برگزار می‌کند. برهمین اساس طبق هماهنگی‌های به عمل آمده، این مسابقه پنجشنبه ۱۴ خرداد از ساعت ۲۰:۳۰ به وقت تهران در ورزشگاه مردان انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/655233" target="_blank">📅 14:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655231">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCR-lCXE7pfW_GKqr5vTiJR_Sx99q9gcI7wPYrDAc3JOcPFJHWZxN82mbEkLxOz1RwV1NAmFm_Tko8RU8EKp2TFYx1AAN9aVkXewOJa3wOW2QNO9J9gGtp6um4IrD5x3w3Ir2G32tmdDsVNQu91kBB4VU6TWEYUikEt0PtJvrjJcmoWnTghBfnNZtlWg9hnlTfqTuajS2rlfIYjjB_PfbcfRl88F0EE2Zmgah1tL6XU9haAB0y0Cs9CMxdDsnSDeWHhDhypFvqsj_P8UfBNTdJwt65IrgLjzFMN8ihwkvaa1vRYKoz4zGnPs-jKHy34oph79SGxBGSqi6xHy6SeTsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e3f095e7.mp4?token=RGe5IpnuJ4BoYovb09NpBc7SOWIphjWMDhTpikEvsvviv-2Oa66tMF4a1YNuCZ0LUVk198Xxtddzs58VHbw2eQoIUBSoMsSdL07l2RpEqX26s9ocWO-ahJgKndt0eL2BTshHCALmR3xxZk0tp9q1qzaYZepb0-Q31YtTPHkCxwy-Hjg04T0Hwdoy_rWbAEfnl9nkW-nB5uTrUbEikJY8YE0HzP7YvOapdFAqIYlfxuqlijTGX77u3i8bwGfjG-vIj1r_VT3bsNa0UEnVyzCDzqRNxnbCtCsoXW5jwqr14B5hphs_8drEdo1Re8NUeDIQ9Zhu5ou-gdYgq5D5sLyIcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e3f095e7.mp4?token=RGe5IpnuJ4BoYovb09NpBc7SOWIphjWMDhTpikEvsvviv-2Oa66tMF4a1YNuCZ0LUVk198Xxtddzs58VHbw2eQoIUBSoMsSdL07l2RpEqX26s9ocWO-ahJgKndt0eL2BTshHCALmR3xxZk0tp9q1qzaYZepb0-Q31YtTPHkCxwy-Hjg04T0Hwdoy_rWbAEfnl9nkW-nB5uTrUbEikJY8YE0HzP7YvOapdFAqIYlfxuqlijTGX77u3i8bwGfjG-vIj1r_VT3bsNa0UEnVyzCDzqRNxnbCtCsoXW5jwqr14B5hphs_8drEdo1Re8NUeDIQ9Zhu5ou-gdYgq5D5sLyIcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش بقایی به  حمله پلیس هلند به یک خانم باردار
سخنگوی وزارت خارجه:
🔹
اروپا که برای هر ادعای تاییدنشده‌ای دربارهٔ زنان در ایران، خشم جهانی به راه می‌اندازد و حمله‌کنندگان به پلیس را «معترض» می‌نامد در قبال خشونت پلیس هلند با یک زن باردار سکوت کرده است.
🔹
همین چندی پیش در هلند، یک زن باردار را با خشونت به زمین کوبید و او را از موهایش روی زمین کشید.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/655231" target="_blank">📅 13:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655230">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رشد ۶۳ هزار واحدی شاخص کل بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۶۴ هزار واحدی به ۴ میلیون و ۳۰۰ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/655230" target="_blank">📅 13:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655229">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
عبور ۱۵ فروند کشتی از تنگه هرمز طی شبانه روز گذشته با مجوز سپاه
روابط عمومی نیروی دریایی سپاه:
🔹
طی شبانه روز گذشته ۱۵ فروند کشتی که ۴ فروند از آن نفتکش بود پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/655229" target="_blank">📅 13:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655228">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی تلخ؛ یک بانک چند هزار میلیارد تومان به افراد خانواده خود تسهیلات داد
فتح‌الله توسلی، عضو کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
برخی بانک‌ها هیچ نقشی برای خود در اقتصاد ملی و کمک به اداره کشور قائل نیستند و برای اعطای وام مردم را به شعبات ارجاع می‌دهند ولی وقتی به شعبه مراجعه می‌شود، وامی مشاهده نمی‌شود.
🔹
منابعی که قرار است برای پرداخت وام‌های مختلف در نظر گرفته شود، به سمت و سویی دیگر سوق داده می‌شود و فساد رخ می‌دهد. مثال دیگر می‌توان به موسسه ملل اشاره کرد که چندین هزار میلیارد تومان برای افراد خانواده خود تسهیلات پرداخت کرده بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/655228" target="_blank">📅 13:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655227">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202555d32c.mp4?token=YpLQBP0eMnwMxTThrJx13j-5UPbs41X1T9IpQ_wHJEzM69neOG1sX98NuCXIWVT8-_5bDgcRUgdQQS0TEvuvOQIkOk3CXHPKknvWiK6rwXvn8P09bketVvoCee_d0eZU8DKu_BPJ8y3oZcht-2S0rCI1xvSEds33HDbiKeKp1XzMJ1GN0rmsZDASqk--7LD94sLPF4MtQSdwuecG_eVKGsmZNVNe8i340ePwF59p14V4M27evEXFgziPAngrSxAAvExzGrixBHHr77hLWjOLP8GPIwvMEtL3wDiQjtQ_RGEf3BE1Z0Xls7rhyJdVWBlMP41VTM8X6uASe9IsolU9nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202555d32c.mp4?token=YpLQBP0eMnwMxTThrJx13j-5UPbs41X1T9IpQ_wHJEzM69neOG1sX98NuCXIWVT8-_5bDgcRUgdQQS0TEvuvOQIkOk3CXHPKknvWiK6rwXvn8P09bketVvoCee_d0eZU8DKu_BPJ8y3oZcht-2S0rCI1xvSEds33HDbiKeKp1XzMJ1GN0rmsZDASqk--7LD94sLPF4MtQSdwuecG_eVKGsmZNVNe8i340ePwF59p14V4M27evEXFgziPAngrSxAAvExzGrixBHHr77hLWjOLP8GPIwvMEtL3wDiQjtQ_RGEf3BE1Z0Xls7rhyJdVWBlMP41VTM8X6uASe9IsolU9nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوچه دو طبقه در کاشان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/655227" target="_blank">📅 13:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655226">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjcOo8Qe__RIlphYSezjALA7q7uDy_8YsnZRDYekaxb5L-ddUv7HHMEzi4taqc29iXzrviJNYXk8RoECFclUhwkVDIICQrxWcFiQ5_YR4tgSTXK11gb-FR-FeJ0WCHyTTCAw8Qtr_Xo58PshHeORPkoiTMWqnecRDNQ9z5iwZxrxbr1A7bI8glW1M1wFEkpjCXD6Gt7wzDc-hjY94aoG2bBwALXla70Cz5Zaa-yMqYr8JPT_inpB46LkisybvoL4BjeUwX1tiFaq0dGm2KuPikW05r19M-8rgFPXqLxZ8bjGKr6-6dQMPDxr3NJY_TL5sLvuQdaRHyrxE31KALkUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فروش طلا به قیمت عمده و استثنایی و اقتصادی
💰
🎁
🎁
ویژه همراهان و سروران گرامی کانال
🎁
🎁
🌸
اهدای سکه طلا به مناسبت اعیاد قربان تا غدیر
🌸
🏆
ولیعصرسبزایران
در قلب بازار تهران
🔸
طلا بخر، بدون مالیات، بدون هزینه اضافی
💥
تا
یک درصد تخفیف
هرخرید به مناسبت عید سعید قربان
💳
فقط ۳ تا ۷ درصد اجرت و سود
💰
خرید طلا طبق نرخ تابلو با تسویه آنی
🔸
فروش آبشده با نیم درصد سود
📍
بازار بزرگ تهران دورسبزه میدان ضلع غربی پلاک ۸۵۶
⏳
ساعت کاری: ۸ صبح تا ۸ شب (یکسره)
👤
📞
مشاوره و تماس:
📲
0938 436 9323 | 0910 480 1538
☎️
021 55 1500 50 | 021 55 1500 60
🆔
آیدی ما:
@valieasar
🏆
بیش از نیم قرن سابقه و ۵ شعبه فعال در تهران</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/655226" target="_blank">📅 13:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655224">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تیراندازی در دانشگاه علوم‌پزشکی قزوین با یک کشته!  دانشگاه علوم پزشکی قزوین:
🔹
در پی بروز حادثه در دانشکده دندانپزشکی،  بررسی‌های اولیه حاکی از آن است که انگیزه این واقعه، مسائل شخصی و خانوادگی بوده.
🔹
در حال حاضر دستگاه‌های ذی‌ربط در حال بررسی ابعاد دقیق…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/655224" target="_blank">📅 13:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655223">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksf2QA-Oqv_x2IVFRXVlHpMnRbrGyHCPv_KzrPK9IbmUZ-W3DKwXRuIrNa7-_ahDTMGx5Cohk5ofWSRB6HLoYkQnTFXZVagUJ0kXIYIu-OChe8RyT7xUdAb-lD51_os-vRiBOHjlDGmySCAd1Uq866MO5HdF5reMwNKM6Elwb1tYPY5Vda0sHMQLvgRTZ6yLRC0kqHFRP1AkZU61ub3oQNnLPvEFqCXLIoVViedE_Tl5yO6TweA8pGMXNTkyqc6GN0kd2C_GT0dDvQO13BVK6OI9wgMdSyUkvpltoq7ot3DDXTRHqn5ycn-DxwMz1oTHxokrgsNRKW4vPsgRcDEMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علت اصلی ترس و هراس جهان از جنگ ایران
🔹
تورم مصرف‌کننده در آمریکا به ۳.۰۸ درصد، در فیلیپین به ۷.۰۲ درصد و در ترکیه به ۳۲.۰۴ درصد رسیده است.
آماری که از تشدید فشارهای تورمی در اقتصاد جهان به دلیل افزایش قیمت‌های انرژی حکایت دارد.
🔹
کارشناسان، شرایط فعلی را به شوک‌های نفتی ۱۹۷۳ و ۱۹۷۹ تشبیه می‌کنند؛ دوره‌ای که تورم آمریکا تا ۱۵ درصد اوج گرفت و فدرال رزرو برای مهار آن، نرخ بهره را به ۲۰ درصد رساند.
🔹
تداوم جنگ و افزایش بهای انرژی، به بزرگ‌ترین نگرانی اقتصاد جهانی تبدیل شده است؛ ترسی که می‌تواند بار دیگر جهان را با موجی از تورم مواجه کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/655223" target="_blank">📅 13:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655222">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8vYLHJ13oXu2AgNiCKIDxKytjJHCZGz1v6ZxYF7zUnDKHAN9bfGjV-VUtgenrk0zsH6IRScvFBdtt_ZJ87QlgdIpnteLYUfoY3AUbzITQG-THfRfnybywueuz64fuCqv7SQQdy5OTf-tNK1T0HYho7VCw6ycdCNlwUPMGmGksgLYD1jfXRjW0KxU7BwcUg1oADssyGQDneVpl5_ke8V8u4V1IhkFuMu0lWMO9bPucD0N4-BTWF7n3nrgRA2ez1s5YAL8iXJ96cLQoWkpZYCdVkkoVdjvxRSuEtiWGeyLw-ECz8LyBDKFwANmYoR8u4zDxlRa7KvqtUUDq-qnMNhnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف به پزشکیان: ابهام در حساب کالابرگ مغایر قانون است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/655222" target="_blank">📅 13:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655221">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ee313a03d.mp4?token=cyJLFEFHNeCuK4mhlmYL-sfthYebX9WxTM1DN5pEbEY0689YSbU8bTOOzAnIN9ppXJdK8s2Kak6N4_eQWkY4qXT8jrFqn6rYI7pkq5IK_eq6Fo6sFoRI3y4X6NYeoYQ4a1iSXP2hqPbF_gaFwyqbfNx0uXOrShy473hCg7wnqZJxi1yczN5I-dCTI4sVcQa7WsmZjq-YZdOs-KS2X4hHfdiOvuwwYQgLN8nTdaPMGplcrYUyazDT5pLssycHG_WFEtl0ZGdKV3wIZJHzyNmP5Mo2uhbJBrBFLqapzPAVCB32RCoEJp0W2ivkdeFPSFDP1okI7kDJnY-WIysiEvtJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ee313a03d.mp4?token=cyJLFEFHNeCuK4mhlmYL-sfthYebX9WxTM1DN5pEbEY0689YSbU8bTOOzAnIN9ppXJdK8s2Kak6N4_eQWkY4qXT8jrFqn6rYI7pkq5IK_eq6Fo6sFoRI3y4X6NYeoYQ4a1iSXP2hqPbF_gaFwyqbfNx0uXOrShy473hCg7wnqZJxi1yczN5I-dCTI4sVcQa7WsmZjq-YZdOs-KS2X4hHfdiOvuwwYQgLN8nTdaPMGplcrYUyazDT5pLssycHG_WFEtl0ZGdKV3wIZJHzyNmP5Mo2uhbJBrBFLqapzPAVCB32RCoEJp0W2ivkdeFPSFDP1okI7kDJnY-WIysiEvtJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"قرار در بی قراری"؛ از کیت آرامش تا دسترسی به بهداشت پریود در شهر
🔹
۲۸ می، روز جهانی بهداشت پریود بود؛ روزی برای یادآوری اهمیت آگاهی،دسترسی و بهبود کیفیت تجربه پریود برای تمامی زنان.
🔹
مای لیدی همزمان با روز جهانی بهداشت پریود، کمپین «قرار در بی قراری» را با تمرکز بر این تجربه در روزهای پراسترس و ناپایدار اجرا کرده است. بخش اصلی این کمپین، «کیت آرامش در اضطرار» است؛ مجموعه ای از محتوای آموزشی، کتاب، موسیقی و خدمات مرتبط با سلامت و آرامش بدن و روان، مانند حرکات ورزشی و مشاوره با روانشناسان که با همکاری پلتفرم هایی مثل فیدیبو، خنیاگر و دکترتو در اختیار مخاطبان قرار گرفته است.
مشاهده کیت آرامش در اضطرار
🔹
در کنار این کیت، مای لیدی باکس های دسترسی به نوار بهداشتی را نیز در چند کافه قرار داده؛ اقدامی در ادامه مسیر این برند برای بهبود دسترس پذیری محصولات بهداشت پریود.
🔹
مـای لـیدی پـیش از ایـن نـیز بـا نـصب بـیش از ۵۰ ونـدیـنگ مـاشـین(دسـتگاه ارائـه پـد بهـداشـتی رایـگان)در مـراکـز عـمومـی، بـیش از ۳۴۳ بــاکــس در ۱۲۱ محــل کــار، تــوزیــع رایــگان مــحصولات بهــداشــتی در مــدارس شــبانــه روزی مــناطــق کــم بــرخــوردار و اهــدای محصولات به کانون هموفیلی، تلاش کرده دسترسی به بهداشت پریود را ساده تر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/655221" target="_blank">📅 13:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655220">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
نحوه برگزاری امتحانات پایان ترم دانشجویان تعیین تکلیف شد
قائم مقام وزیر علوم:
🔹
امتحانات پایان ترم دانشجویان دوره های کارشناسی ارشد و دکتری دانشگاه‌ها کشور بجز چند دانشگاه فوق در نیمسال جاری به صورت کاملا حضوری برگزار می شود.
🔹
دانشجویان کارشناسی برای سال جاری آموزش باقی مانده خود را به صورت مجازی ادامه خواهند داد و آموزش حضوری نخواهند داشت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/655220" target="_blank">📅 12:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655219">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
تیراندازی در دانشگاه علوم‌پزشکی قزوین با یک کشته!
دانشگاه علوم پزشکی قزوین:
🔹
در پی بروز حادثه در دانشکده دندانپزشکی،  بررسی‌های اولیه حاکی از آن است که انگیزه این واقعه، مسائل شخصی و خانوادگی بوده.
🔹
در حال حاضر دستگاه‌های ذی‌ربط در حال بررسی ابعاد دقیق موضوع هستند و اطلاعات تکمیلی و دقیق متعاقباً از طریق درگاه‌های اطلاع‌رسانی رسمی دانشگاه به اطلاع عموم خواهد رسید.
🔹
گفتنی است در ساعات اخیر اخباری درباره وقوع حادثه تیراندازی در دانشکده دندانپزشکی دانشگاه علوم پزشکی قزوین و قتل یک نفر در فضای مجازی منتشر شده است.
#اخبار_قزوین
در فضای مجازی
👇
@akhbarghazvin</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/655219" target="_blank">📅 12:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655218">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iks7NV5ujTrIGzWm1KNXztoSzyO73qFMqzN2-bmB29wzx5GxuDzjRBaHeJ-Eufb302X4D8oWM2KpSdhY_pt0ef9hfts3-7O0YKSrGZmpShHGq_oDDKitDEDlejwuu4OUq6sz05n4K2eZ9FOS7Y5lnmJfS9zHS7Wia1352HVQrWsnxHlTjdJavHx5c8J7RhhDC87yr1qPPdxch5Llna-uo9-ca1jqGreWyfh4Evmtp2qFExyQ-AGTuXGsMTccuR3YnywfdOV6U2kdcKSHvxFfAP14wdy8zVBXEFxQiO5lycFQUEZaNpadkVZg1X7VzF2iNler4qBS76xcHmCs5y09fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاهکارها و منتخبی از آثار برجسته ادبی کشورهای مختلف
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/655218" target="_blank">📅 12:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655217">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f695ea1873.mp4?token=s1s5socvA_xeaG7CPgVsZX-LLdvkQsxVXLquBRZ1NMp4kuSs545Ji8buFx2RnADLqNIctgH14o2eZo1dvhvTjE2-K-XGGTmW8CUbMiV1n-1Wb6Q6G5Zb85Fckahh2PZTu-E6aEvQ09vzPiUZ3zXwOYQ-74Ui9jpUDjDpHD5YpePNrjLrLsPeUzTsJ16DqMDfg7vupz_4erTw1iOZcenZNuH17Zv6QGgREIyZ_eRZwOcyFxcLiI0y9tttSMN1ZMlSaaQ2tDmePE8Yp73iU8mQxTFNnQ_DP0vJ_1WVGvmAiP5tjmJI2p8XC3_2CInf3UY5xprnAih0zGUBwf4bNPFgnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f695ea1873.mp4?token=s1s5socvA_xeaG7CPgVsZX-LLdvkQsxVXLquBRZ1NMp4kuSs545Ji8buFx2RnADLqNIctgH14o2eZo1dvhvTjE2-K-XGGTmW8CUbMiV1n-1Wb6Q6G5Zb85Fckahh2PZTu-E6aEvQ09vzPiUZ3zXwOYQ-74Ui9jpUDjDpHD5YpePNrjLrLsPeUzTsJ16DqMDfg7vupz_4erTw1iOZcenZNuH17Zv6QGgREIyZ_eRZwOcyFxcLiI0y9tttSMN1ZMlSaaQ2tDmePE8Yp73iU8mQxTFNnQ_DP0vJ_1WVGvmAiP5tjmJI2p8XC3_2CInf3UY5xprnAih0zGUBwf4bNPFgnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس قوه‌قضائیه: گرانی‌ها باید برطرف شود
اژه‌ای:
🔹
اختلاف نظرها در کشور نباید به تنازع  تبدیل شود؛ در زمین دشمن بازی نکنیم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/655217" target="_blank">📅 12:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655216">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChpBCfun9I1FrxtBROUn2dVzgJAQ8Z18tVUsV5Fhm94ajl0MPTaiqCYgGLIrUBPPTn6WMeb90L7FHLxsYmnOW-oFIoAz1ts9e4RzHL3PXwTfqwmsTmToffKzeobGcpEymqvJbV1bJzvbjHpzxVsFDOCLKQ9Jqp4GWA_23m6rmIuhTwv1qfQ54qjemg_2p-jEYA9U4ING6f-QeCBxCeh_PeWjViVdM8sziyfyGJtw36gqD0npMUO9RBlKvkmRP2KjWj_cpL0z8wmjUKKdnDhbBwJGpApd-u9zJr4d_J6A4rtp6Fh7j2Ou8KAPeVv38MkiefUQfu-ANp_kqUu8GPCM_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمامی استادیوم‌های جام جهانی ۲۰۲۶
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/655216" target="_blank">📅 12:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655210">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/771bcfe756.mp4?token=JRsGCaO_C05UdzunF8z8KYHuy8yjrZMXThVTsyur78UBR3u5B8TuHYg7gzUIDt6uFx7QnPgMM9-e69IClWbEnukzR1HyAPkwaAxDf1v0avKnfc0o628F7Ms9DVPyunjwuZiifc7NAAyT7X-MkQoj-LeDOcCP9XD9UNsdRZHtS8umFel6xc4g5VXwpPW8VqmlOpnXgbimLiy2Gc6AlL4vaIhsMJNA8p6pZS-AgWSqiqeyBXby9khylJRibrE4wzX1mAOOGkNnX9sQD2IH-uGEKipgYlLQ7os_loZOZHnG96f7oxcRrca9cLhxUAwRMpsQeGzOt36mMCZGkLEpWy7vsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/771bcfe756.mp4?token=JRsGCaO_C05UdzunF8z8KYHuy8yjrZMXThVTsyur78UBR3u5B8TuHYg7gzUIDt6uFx7QnPgMM9-e69IClWbEnukzR1HyAPkwaAxDf1v0avKnfc0o628F7Ms9DVPyunjwuZiifc7NAAyT7X-MkQoj-LeDOcCP9XD9UNsdRZHtS8umFel6xc4g5VXwpPW8VqmlOpnXgbimLiy2Gc6AlL4vaIhsMJNA8p6pZS-AgWSqiqeyBXby9khylJRibrE4wzX1mAOOGkNnX9sQD2IH-uGEKipgYlLQ7os_loZOZHnG96f7oxcRrca9cLhxUAwRMpsQeGzOt36mMCZGkLEpWy7vsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آثار حملات ایران به پایگاه الظفره امارات
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/655210" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655209">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEl8eZ5LP9qLHibxwU_gWDS3ThO6T8QROXDjJVKhheOpIgjswoHDk24NbJHaMuKAauI_kYAmpiVh09jGKJkbOClI1aemV-LB66tXc2Hi1BfZo8-yWiRT4rhARLjOMJN2qIsqZn_IZJB0gP0XXpGEtkWi_5Wlmsaxcab3_bTxzd4pdnUYzeSsHizQdajrfvXiXIZfQX4pSBmJuDImegs5dhYCD4TAAL8eDAo3AKCJgyB65bc4eAw8TvJQJtXexngjiTOadjWTX-Kzi_Xskj5Q7rWsmdailS5dD5eMeoi8TYVdpzUOvq01ovhxJK_s3vsEroABeesDxqDDNUuDDkrDDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: ترس ترامپ از ضعیف دیده شدن، سد توافق با ایران است
گاردین:
🔹
«هنر معامله» ترامپ در برابر ایران شکست خورده و او در مذاکرات نتوانسته از خرابکاری در روند گفت‌وگوها دست بردارد.
🔹
ترامپ از نشان دادن هرگونه نشانه ضعف بیزار است و همین مسئله او را از رسیدن به توافقی که ممکن است او را ضعیف نشان دهد، بازمی‌دارد.
🔹
ترامپ همچنین به شدت نسبت به این انتقاد حساس است که هر توافق احتمالی او برای آمریکا بدتر از برجام باشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/655209" target="_blank">📅 12:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655208">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF2JJ3IB043s0tt2k6IumCY7d_P6CctrFndG4g4sICy5_GkSm9i2bh8RE2Wi4ihRiVbyg2h5cPyiWEI57qkUK35-gwyhXCdMCdQZO13W_zzuLOqgwkIXrpf0YOZSBu251DvP1oQNR21oWGo1qdtKK5Q-tbMcxkEiFL2jsVgKQdxrqvubmuDjVtLotmJ8I4bzs_SCC2SzrYa6EzDadHiLjuR39yRqGHZ9ajq_gsX3rQDO-Cdor8Bi3RD7-edrWYSBNjb9F8yNpS_p-nm0Yyt38kNEY8zzPDGsrnAn_XKpmyDlYyw47_SLfpQQ_DpIgq1SalZWFPwsx1nnSygkAFeBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاوضه لوازم خانگی با خودرو در بازار!
🔹
با افزایش قیمت‌ها در بازار خودرو و لوازم خانگی، شیوه جدیدی از معامله در بازار شکل گرفته و برخی افراد لوازم خانگی را با خودرو معاوضه می‌کنند.
🔹
در یکی از آگهی‌ها نیز کولر گازی و فرش برای معاوضه با خودرو عرضه شده و کف قیمت کولر گازی حدود ۶۰ تا ۱۰۰ میلیون تومان اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/655208" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655207">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
انصاری: پیام مقام معظم رهبری در ۱۴ خرداد قرائت می‌شود
دبیر ستاد مرکزی بزرگداشت امام خمینی (س):
🔹
مراسم رسمی ۱۴ خرداد از ساعت ۹ صبح با تلاوت قرآن و مداحی مداحان اهل‌بیت آغاز خواهد شد و در ادامه، پیام مهم مقام معظم رهبری قرائت می‌شود.
🔹
امسال امکان حضور گسترده زائران همانند سال‌های گذشته فراهم نیست.
🔹
یادگار امام در مراسم امسال سخنرانی نمی‌کند.
🔹
نماز جمعه ۱۵ خرداد در مرقد امام برگزار می‌شود.
🔹
امسال مهمانان خارجی در مراسم حضور نخواهند داشت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/655207" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655206">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i09xlkYa8rwlI4ZYBWad_z_KGWFk-vauLUpisNj41VkrV96qj9O9LRxRvxwNvtBHabllX_6Fx6hYDETVEWP1_UBL2bkkOTDiNWMasMIG4fYWeIK4kIk4uz_S1MYjWueqY0HpdukxXyLpQfAUnapb14wqMXaY7Fo4MuqtK6jd1mm1kgp-VMuTmRrDTGay-HiRTUVwPUw5BwR3xHkkqKHlhPS69_woFQ8OGXimc0HafCOchTq7clkVXTbc9oTXrgeNZKNi7yqfbzYhwy6UwKZ8YqxJ5XqA_U3NDSEipH_kuSL8EGqhU1N9CP2zSSAUfzRyx6Ma8otCpJ3oSEOF1nu2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: باید هزینهٔ جنایات رژیم صهیونیستی در لبنان را پرداخت کنید، همه چیز سر جای خودش قرار خواهد گرفت
🔹
اعمال محاصره دریایی و تشدید جنایات جنگی در لبنان توسط رژیم نسل کش صهیونیستی، شواهد روشن عدم پایبندی آمریکا به آتش بس است.
🔹
هر انتخابی، هزینه‌ای دارد و صورتحساب آن هم از راه میرسد؛ همه چیز سر جای خودش قرار خواهد گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/655206" target="_blank">📅 12:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655205">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XS_gkrbQqOJgxNXNVVl-8NGDKX3nEvHCiqsr57c8zMLexFbXa8-Bj_JlL_tEyLr-DRvnW0wP64WWTZs21531mEyPS3154E2etJjR-NH_ITPoVGvDNPyidWkqSKkSglR6u4StFSYCc0OZTNARh5LixqeLKKzM1AsUE3bSW2gPAb4xiwXUwq6lvw6SbAZPrkrInACWhyAP1gw7ZB4JMQ0eJXwyLQJyvBGlmP8_aLczyDY6AAvLkU4AQSCCtVENJLzfpojlRom4fxMvJ3M_HF6PrkxHRJQLib6bwe_R-27qWGH0mY0BiOc8yKd7mNiNMEhAleXzIJ_l0P40la1N-hqDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت درهای بسته چه گذشت؟ | طعنه‌های تند ترامپ به ونس فاش شد | مذاکره‌کننده اصلی با ایران کنار گذاشته می‌شود؟
🔹
بر اساس گزارشی که به نقل از منابع داخلی کاخ سفید و تحقیقات روزنامه‌نگاران منتشر شده، تنش‌هایی پشت پرده میان دونالد ترامپ و معاونش جی‌دی ونس وجود دارد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219292</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/655205" target="_blank">📅 12:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655204">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edc35d9fc.mp4?token=TylDtJbNOGWOzQKc9mp6cjp36a0E5GgPNiiuxze-9ycA3w34IiG32IIT1okpzKCONcaTrCjIviQXwtWBD_hJaSY4c6RS_kK3IWbN3h0VYBS7n7DNdSXI_5TfLAWjDgmHiKKAfYJBAWdReDR7oYBWXw3n7kk9vsyHSLiqM5zzv3j9PA87pBBc3q4Q4GT3id2InYfbGSD9PupsgCK31akwxutaR_9V3JPmTV0_q-GulZPKxuM9tVFf47ukSWwDygc41ZncwhrYt9UVHff7eJi-9E7iAZFB_fqX0KsaGwIcn_3sGT_gNQlq0xpjqXC4Dii38EBcPoIreAkim2QcPi_QaDINxO6RqW8p1oG_RENZY9-Pkmdhozn5ViXHt_wA19Egy10Y5-aeU97S0ceHax8eIr7uqBouKqjKUKGblfkizcIWzeXq0bSyvhPWZPB-AbK9UDlWMGLjhTrbOwqAtuRMENSVSS_sizRx_hR-Vlip-RZ1ACxJix3xcv0C-uV6r_eA-sK8JRwpEzwnN-LaukodJVaszejnu_Vc16bmzGbCTf59e7RFEqdltfJMneVgRG-A7sQk0P0IoSpTSA_XBUIQeoNAIbocKHDYPrK-EiBkXXYYJZvHJGw8FPXDM7Hnifa7M778jtvA1I_VnhKVXYVmf1mVNfcaKVv8SlVaFKNCjbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edc35d9fc.mp4?token=TylDtJbNOGWOzQKc9mp6cjp36a0E5GgPNiiuxze-9ycA3w34IiG32IIT1okpzKCONcaTrCjIviQXwtWBD_hJaSY4c6RS_kK3IWbN3h0VYBS7n7DNdSXI_5TfLAWjDgmHiKKAfYJBAWdReDR7oYBWXw3n7kk9vsyHSLiqM5zzv3j9PA87pBBc3q4Q4GT3id2InYfbGSD9PupsgCK31akwxutaR_9V3JPmTV0_q-GulZPKxuM9tVFf47ukSWwDygc41ZncwhrYt9UVHff7eJi-9E7iAZFB_fqX0KsaGwIcn_3sGT_gNQlq0xpjqXC4Dii38EBcPoIreAkim2QcPi_QaDINxO6RqW8p1oG_RENZY9-Pkmdhozn5ViXHt_wA19Egy10Y5-aeU97S0ceHax8eIr7uqBouKqjKUKGblfkizcIWzeXq0bSyvhPWZPB-AbK9UDlWMGLjhTrbOwqAtuRMENSVSS_sizRx_hR-Vlip-RZ1ACxJix3xcv0C-uV6r_eA-sK8JRwpEzwnN-LaukodJVaszejnu_Vc16bmzGbCTf59e7RFEqdltfJMneVgRG-A7sQk0P0IoSpTSA_XBUIQeoNAIbocKHDYPrK-EiBkXXYYJZvHJGw8FPXDM7Hnifa7M778jtvA1I_VnhKVXYVmf1mVNfcaKVv8SlVaFKNCjbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر یکی از عملیات های گشت و کنترل تنگه هرمز توسط شناورهای تندور نیروی دریایی سپاه طی روزهای گذشته
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/655204" target="_blank">📅 12:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655203">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbNq3YUOmVuriUhKOTrSkNkDa2pMM0AmE6z9QEdHCYORLB_ergCu3nfyVDCK_KiXIVeSIOpwjbVDp51I1rXJGGua3-SgjwdTvH6wLzQ-I1WMh0-b_ySW2HpGQSMmeDQQ0UFzz7ifX0_7uw-gN9_KK3IZ6wheNInGnO_r9XPH0Qi5OKW-Fz6wDaJL87wwq2kn2hrfnEKzEVZKE9oCDGdBh6puVg2w5bXDyTTo8A1BrQtl0BADZXW4unXAJDy-LFZfnI0sRJi5QEMvIngfMURXIln5sZ-vBuXo5W2u4p7tCF3uoe25ykS6ODqwFl_8k3Eaj2rLCJWiqpqw5hQTU4IThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار رسمی حج ۲۰۲۶ منتشر شد!
🔸
تعداد کل زائران حج ۲۰۲۶ به ۱ میلیون و ۷۰۷ هزار و ۳۰۱ نفر رسید که حدود ۹۱٪ کل زائران از خارج عربستان و از ۱۶۵ ملیت مختلف بودند.
🔸
زائران ایرانی با حدود ۳۰ هزار نفر، نزدیک به ۱.۸٪ از کل زائران حج امسال را تشکیل دادند.
@amarfact</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/655203" target="_blank">📅 12:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655197">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ag7Gi15nNf18QWgRTir5kNZZqRGRW5Ai83vjx-OOtq_BTxMKorkrozxgTf13076fjXGqsPk_-jFaQts-Zf6QRyGgVx9K5P9Hr8pNhcoud2lzEaOJFw1Tt6gbsIGhMSN44UnofXS7qvoEgmfxerTXmwljOZRWNFZH6oOmoi34yjJMUK7zmO9vMPEgWB-l_ogkiDeHFqV1iR5Ft8UFf8szLi5izBsBKYtfQQxAGlja1J-9ZP-9JbTBibBfRR0wbIMK2KXZFM1NVb4CJKFZbvV6IqcnJ9jnpn3Cj9hCbyFYRvPGUwmuX2e-5T1i_a8RVmyQN_zIU-Fo4ouexl86yy81YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czxwOg1kHx5peGHIqHn4-7QtRROt7z-WlWYwQOgtVJWxIUrfO7fN9OK7_Gr0X56CU457l50aIBsFVNCtat2mUGLMrkehG31uDmUWvPq8VReaLo2RCgNNA41V3kPYM2CcObCQwgzaX5O9BcLHPtnbvklB8WM-YfcuBMwJDztA-LQOAvVPOzk26-_lY3cmsTv6Su6ot5Xzu2N73YCwMsTuavNFXeADxPWXBrOhzEiyzoSdxesNVKjiktm_ZB32PsnZj17O2zHJ1myTENaaE6j5lraMDYKRK_XaaSiQGylAB6KtDhMaF5zUM06wMn50R2j_IbUv-dKziYcBtNzps-PPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUiRw2DwrDyIzsUU1LPSllGOTgcs5l2HNpm8Ht6hVMMs9_FQvAmo_-naImTrj0UFgOX2Ga7sRw_LteRoyEc6WrcJfHcrdDn_I83XonosXwwtjB7LmKfHrIOjrmiSPdyKXXn87lJ-m5lxKsf5mW1ax44JkydNnyRrEXvy3BmTGdLRs1t-0ig8IgZ5pavijO3fNPQsZPSqtcm-4y37zhvkJ60CSx_bBFjugNTf9AALxYPLpIEMPBpJHUhw2A-krpWRbgjrzWFKgfuUAduXg7_7XvKsM1LBozH7JESq8my4mDZbGcBXm6urMzrMaS6BXXXbIeQShJEq3rg2votG5EyWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlB4VyGS5rn_kTuMCHmpDZkKwCvgVsvQM-l9I-xYbMtuHEdIy6VmUOXBEwCgvBReA6N0lPplt747xqP6lAcxEiPTKnhheBPHyahKpKNa21b5VhkFmhwbD-w6ax8NDEH3tnnArTxYQCGLsavbdqBPlTQK8GnYdt0u4_jnDhA-QdTjkmU0lMAopha8Zq-aAV879WFwly5mbXw9QvhdCjY4ik2BOYyvgk-cTNHOzPwq-wN4G2bNDN8kGlCEpjAOrcWfFF9QFk6G3rJbvlm0SHJvIojSMj5IGxGVjPFM6Vuo1o_f12qfERfX4ElD2T67UG_lgBQoBAA77pY3_IL9eaXVzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITtYZE-YgF-QzoOunBqOvfpzXSOhznqW6Jeiyn-7hptiaVsQgWTd4pICVBhkMIatdTi1qQ6g0LES9cSIWy0WTu7MX-zW_uBz1l_5SAjFU9_qKrrsbZfy_Me6gGMkv-ni_lRShSxbn_MwJgtGodi4MBsZqkrulFiLegtMwOGyN29hVDCMpyZRhmyb0AweHqLAxKVf42sBEnsZylT4XFHRVcJoUyvUzAeZLDppPnGVoXBZmnqPaBYRiGw5Iruez33iEPYdCGGg2UD_VxdwR9Z5YGPAgiCMeVGc8mh5OvlFR4qFZtN7ZVW9en4u53mqc-fpORQJkL8xkJ9PHiBmo5_ahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k35-ljf5bn2Ka4OgoigUD2ikXFJc69XWksqTsaLg6hE4juq4_vPzWy_KSoyOtzoBGq7DFX70KpGXCuMLx-5VGO2At7lFMjheWH_LVgLSRat_0g0aqvEx_wpZwz0hx6TblpcCRTfXHNAObQqN87nMat2F4tpgjTwigdnVlq9FcDCoTDBM9TYNa0KWa242YAvm-E6wMslPQYfIQpWGlP4iD2M-G_Qi3uzmU8FtDbFwjX-DyfHHi_tuLt_lbLZCcNipvdSa_FRtA8YYHDOhOo0makiyZQiZcoB_2woLol4kaaCWkkZn7il1JIThInGcix4-kV2u2WJ1yFu0c-6CShj7mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نصف سد طالقان خالی است!
🔹
سد طالقان با ظرفیت ۴۲۰ میلیون مترمکعبی بزرگ ترین سد تأمین آب شرب تهران است و هم اکنون نیمی از ظرفیت آن خالی است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/655197" target="_blank">📅 12:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655196">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05b04c632.mp4?token=VT5YT1iiFzqdJtvnE_ox93mV1P1x1KeuwFOBuRsB_Su_BlZctwp5n_2Ex4gSH-w4XfvncW1RruAdfa9AvYlwRDaUmBE8O28BYc9qw6apMRn2mQplCfQiJ4a7uiXhVg7TDNM50KnZEXYXnpu7UylyCCUS4mWYvpVzUatTyEIHH4kpAkRFI68zwoZR8U6Vp-vuqncF6fvJjjmagOE_5K8ifHXS8ArJbcbaVXEBDeM_cXTPAt1QNjHUuc9tpKlIsLRxcS9Z3dRaEeCh2hMQSgj7IgDExOhIrA68t_GAR4mVgQa8zyhzk2eLR5xBW0gILSvX5hajFCwFfZIUgnshmK44wZuov_hdD5PRqeGgkHZ3Hzm-mfwDBbcwX6M9G8cOABtG6v6WldcmAwNu1pu-9_MaqnM4HuiXZLaIldyMJVEt92omBXW2xn4I6-klPg35NSG2dmte06j0Ujvr4es9ltOz27BtBix8SD7a4qeNOsbZemX7fQ6hXxYdcfA4xlPa4deRTq6KJgtH6zHbnspXyi484hCVDDFyufmWdfzfEL5rCzonOYhqvCbZZyq6Ew2g5xcufqqVn3_56Tkb3KmjVqSsZFVRb7uBDZflsELyqfWAzfXRP6evYV6gOi4uGHSQCxjgaFZT1vituZf_8rri-3pk9op_fjSdSJKOGNj3hZAKdbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05b04c632.mp4?token=VT5YT1iiFzqdJtvnE_ox93mV1P1x1KeuwFOBuRsB_Su_BlZctwp5n_2Ex4gSH-w4XfvncW1RruAdfa9AvYlwRDaUmBE8O28BYc9qw6apMRn2mQplCfQiJ4a7uiXhVg7TDNM50KnZEXYXnpu7UylyCCUS4mWYvpVzUatTyEIHH4kpAkRFI68zwoZR8U6Vp-vuqncF6fvJjjmagOE_5K8ifHXS8ArJbcbaVXEBDeM_cXTPAt1QNjHUuc9tpKlIsLRxcS9Z3dRaEeCh2hMQSgj7IgDExOhIrA68t_GAR4mVgQa8zyhzk2eLR5xBW0gILSvX5hajFCwFfZIUgnshmK44wZuov_hdD5PRqeGgkHZ3Hzm-mfwDBbcwX6M9G8cOABtG6v6WldcmAwNu1pu-9_MaqnM4HuiXZLaIldyMJVEt92omBXW2xn4I6-klPg35NSG2dmte06j0Ujvr4es9ltOz27BtBix8SD7a4qeNOsbZemX7fQ6hXxYdcfA4xlPa4deRTq6KJgtH6zHbnspXyi484hCVDDFyufmWdfzfEL5rCzonOYhqvCbZZyq6Ew2g5xcufqqVn3_56Tkb3KmjVqSsZFVRb7uBDZflsELyqfWAzfXRP6evYV6gOi4uGHSQCxjgaFZT1vituZf_8rri-3pk9op_fjSdSJKOGNj3hZAKdbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایسلند اولین قربانی قانون جدید داوری فیفا شد
🔹
طبق قانون جدید داوری فیفا که قرار است از جام جهانی ۲۰۲۶ اجرا شود، اگر خروج بازیکن تعویضی بیش از ۱۰ ثانیه طول بکشد، بازیکن جانشین تا اولین توقف بعدی بازی (حداقل یک دقیقه) اجازه ورود ندارد.
🔹
این قانون در دیدار دوستانه ژاپن ـ ایسلند برای نخستین بار اجرا شد و به گل پیروزی ژاپن انجامید.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/655196" target="_blank">📅 12:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655195">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صف وام ازدواج و فرزندآوری از یک میلیون‌ نفر عبور کرد
محبی نجم‌آبادی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
متاسفانه در سال گذشته وام فرزندآوری و ازدواج بیش از یک میلیون‌ نفر محقق نشد. در سال ۱۴۰۴ بودجه ۲۷۰ هزار میلیاردی داشتیم و در سال ۱۴۰۵ این بودجه به ۴۷۰ همت ارتقا پیدا کرد. اولویت پرداخت با وام ازدواج می‌باشد.
🔹
قانون تامین مالی روش‌های جدید از ضمانت مانند خودرو، طلا، ملک و همه چیزهایی که نقد می‌شوند را در نظر گرفته و امیدواریم این سامانه هر چه زودتر راه بیوفتد.
🔹
براساس گزارشات، در شش‌ ماهه اول سال جدید قول داده شده تا آن یک میلیون نفر وام‌شان پرداخت شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/655195" target="_blank">📅 12:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655194">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1N1LjXCaAwMigp25Jn3EMSa7an_qGfqht1UOLevUfUHpPyZUCOU5VLMztTEmZTHMUdrJGs_IQIGpJpAm5yakX5TPhu_rmCUM2TdVDCedrwt6_EHnOgPnmvqdT3W8Z9m4fX203ftSmmJOtZWTCcp38BbyGnagYdJMEKFG-sWl9sznXnfhiRVvNIHDKLTWCCoKtKi1CFRPs0uzYWdEdxeXRwE89Z1Am5A2v5dK6oinz-umHq6LL7F1xluXkhmVoZp2m_PdUxHMeaIoNTr14eDYM2etINUO-O31TK-ok28eWI95D9SWibDEuB2f58VMMoE6m8cey7inTNihCTLB7spgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای سریع برای شناخت بات‌ها و اکانت‌های جعلی #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/655194" target="_blank">📅 12:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655192">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانال ۱۴ رژیم صهیونیستی: امروز رأی‌گیری برای انحلال کنست انجام خواهد شد</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/655192" target="_blank">📅 12:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1aef0067.mp4?token=kJBWiZ7te0Pcuip1FrXeAFhd3OnZKSLDtlP_EDz8MGYICxTN45u2TFBL3bOZyAK2E-2GlcLrZoea2BtgsfmuXRDPgFTYMCZZqIDTC96kkT6QgsDdqyXXmXNnJzgimjtERKZn8eGwImEuwpIVR7ITTIuk2n2fvPwG5nREwm_qCmCtx5o5OrWG_RY4mdz-jSzB21wo2xjgFchxYycxLMElCUZL6AuDrPCQuR-WtZjnRVfSq8QJ_Wj5wQZaiEQaXYMhJp_i5GjAqBATUb3bEkvYyyLDc5n_L2B4RLFxV--o3yBfwg1MjZaJozizxNzv6eomFadKbOOg_HlO6N01TGzBLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1aef0067.mp4?token=kJBWiZ7te0Pcuip1FrXeAFhd3OnZKSLDtlP_EDz8MGYICxTN45u2TFBL3bOZyAK2E-2GlcLrZoea2BtgsfmuXRDPgFTYMCZZqIDTC96kkT6QgsDdqyXXmXNnJzgimjtERKZn8eGwImEuwpIVR7ITTIuk2n2fvPwG5nREwm_qCmCtx5o5OrWG_RY4mdz-jSzB21wo2xjgFchxYycxLMElCUZL6AuDrPCQuR-WtZjnRVfSq8QJ_Wj5wQZaiEQaXYMhJp_i5GjAqBATUb3bEkvYyyLDc5n_L2B4RLFxV--o3yBfwg1MjZaJozizxNzv6eomFadKbOOg_HlO6N01TGzBLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان ملخ در مشهد
🔹
تصاویری از هجوم ملخ‌ها به مشهد مقدس که در فضای مجازی وایرال شده.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/655191" target="_blank">📅 11:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قطعنامه شورای امنیت برای ما تضمین نیست
🔹
در تفاهم اولیه یک بند دربارهٔ صدور قطعنامهٔ شورای امنیت در صورت توافق وجود دارد اما معنایش این نیست که ما قطعنامهٔ شورای امنیت را تضمین می‌بینیم.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/655190" target="_blank">📅 11:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655189">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6732ddafe.mp4?token=VztK70elQZffJQrcBeGCNxkUOFDNQZegC41gbkG1a2-x1BtjLBY7QLWU8BCknn5QcFgATRZkBVCbhb6ksze9TKkAAXpF9IaSKTZb2k7GX2TkmkOq_UUt6lPXF4JTfJsCeOWg5KzAYPm4IK4fAHJe1p1wujWi3J1VrPpNnfjg3T8mpjdN1SMd37Q7afBNJKNwU6q1p84ZgRSLAftog_EtOnmC6LDz-2UdlHU3Ia2YSucd3i9XaVmMOTAV81xC-bXDB8P5vkR26RLcdC2NlDkyAB45KchftnVtrnHFFZ5bzI2x58kltD1jmgysu312kQa0gFfrjYTshjPv5t4l9Bid1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6732ddafe.mp4?token=VztK70elQZffJQrcBeGCNxkUOFDNQZegC41gbkG1a2-x1BtjLBY7QLWU8BCknn5QcFgATRZkBVCbhb6ksze9TKkAAXpF9IaSKTZb2k7GX2TkmkOq_UUt6lPXF4JTfJsCeOWg5KzAYPm4IK4fAHJe1p1wujWi3J1VrPpNnfjg3T8mpjdN1SMd37Q7afBNJKNwU6q1p84ZgRSLAftog_EtOnmC6LDz-2UdlHU3Ia2YSucd3i9XaVmMOTAV81xC-bXDB8P5vkR26RLcdC2NlDkyAB45KchftnVtrnHFFZ5bzI2x58kltD1jmgysu312kQa0gFfrjYTshjPv5t4l9Bid1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: حاضر نیستیم راجع به موضاعاتی که به دفاع از کیان ایران است صحبت کنیم   سخنگوی وزارت امورخارجه:
🔹
مدت‌هاست که گفته ایم حتی در سطح رسانه هم حاضر نیستیم راجع به موضوعاتی که به دفاع از کیان ایران مربوط می شود صحبت کنیم.
🔹
تکرار این گزاره که ایران نباید…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/655189" target="_blank">📅 11:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655188">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
بقایی: آنچه را که ایران در توافق برجام دریافت کرد، اموال مسدودشده و حق مردم ایران بود
🔹
حالا هم به‌دنبال احقاق حقوق مردم ایران هستیم.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/655188" target="_blank">📅 11:42 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
