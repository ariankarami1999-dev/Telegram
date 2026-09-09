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
<img src="https://cdn4.telesco.pe/file/QMG8LJBZNzAHxu-odr1Wh9vtowLgAVmEdLF5Std5b6KpTAqDYx0f3W4FvEK-XR6tpI4eXgkk0GeShH3JKmVwCVzeejE1r4IOzh4q9GHAHvXd3TgR8_RGU7gwyM4CBhjQmqDt614TMgEcHU_g9XW_2661nI1VHIPX55RUwDgegMhZ585-JRI-G2uqogmTD4VkQRx7SfonqBWPeZ2GYGhjolBEh4o3FHteHjyMPOp3yM_UINNYjbW1HiT6RXgzaB5prhVpY9NcDl3WH8f0CcCyeN1OgfZIamWriv2K5-8LYSDR166NozTmEuLBCEZz5mQFej_jxlQk--kDIj_FBv7PLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 926K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 02:55:58</div>
<hr>

<div class="tg-post" id="msg-146589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw1WCLPq2J44TRTe9MTO7HZNNgRZTvFcMtjKjRh1b6mxFwBhpDA076Il1IRIDnljoMUN8REnrOdQK2XCZDD65p21PYRoYZsr5xKPRBR0FYMHPjYbVOdBmvrE62vzDSv_usBoMmTUnoJGSeMkx2wrlIuE9f9ix5k_2nAliywDPvsPgt_LSW7Br1RCqcS1hcEGDsCuFrkjG-8pn7ZUVOCe-Fdy2XOgs9kIj5p132RYK0j0wL6rknRGCCh1-l9gEIcjlrOPrUwH2uqkqBtuesDFd33VKmngH4txgLSApMPcUC7GMT8RDvBdXuvhmyd6POISdc3Gsso1vKUfzPrLkejbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
قیمتارو شکوندیم!
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
مولتی هوشمند
لیت
|
۳۰٪ تخفیف
۳۵+ لوکیشن • ۱۳۰+ لینک پرسرعت • IP ثابت
▶️
یوتوب
و
ساندکلاد
بدون تبلیغات
🔥
فیلیمو، فیلم‌نت و نماوا رایگان
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کد تخفیف
:
LIT200K
اول رایگان تست کن، بعد انتخاب کن.
🔥
ربات تست رایگان و کانفیگ:
@
litvpn_bot
❤️
ربات مخصوص
همکاران
:
@litpanel_bot
❤️
پشتیبانی
۲۴ ساعته:
@mahan_lit
.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/146589" target="_blank">📅 01:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz6VKClpvPOca9JSzC8ECX7GYSGn43qzu0xXhadJbP3vx37bEIJi7VSOcrW7HK-sn7Wbwy1d4uOwyQf1PcA6gh4W19KuD9afZFCEQb_T1ZhjzvPJwMXS0JwbU9busMfvCp5iZJEoLBJCu6gP0Q5-GEzEjngkoYEvJcMohqIK1aqc5WLoMeivXABS6CrSbcMcXUNj0_5FZ97Jpx3Z2JsLrAv9QvPDvlIP5-Co5OPsUrDtQCCalGf6KZQ3ncXf0SBSU1j518KHQIrHymbTckYWzPVOo5ijlXRRWp9KKOW_pFuWpHKWAL1PbbrTb39XYGT5JccEThEmOvWpFdk8iCntug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
رویترز خبر داده که پاکستان پیام هشدار عربستان سعودی را به ایران منتقل کرده و از تهران خواسته برای جلوگیری از بحران منطقه‌ای، جلوی حملات حوثی‌ها را بگیرد، درحالی که بقایی اعلام کرده ایران کنترلی بر حوثی ها ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/146588" target="_blank">📅 01:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146587">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdjW81TnJLmQ9ZbLUMvasxyjAmeuck5oA4220SSwBHXjF4BLx8FjaumWIyvnvbD8wtQglvhHXZvDVlMgiEN_UnD_nDJfQm9j40KinhWe4c1UkQjY1GWFGDfd-0Cp6NfeYfBxMJA94kPEK9-bxneVeeXeNtNNebw_BY3Twi7WvILEiMDC8JC20PpCtIjt3Iy9cNNaOxXdy8wZ2WXY_mfT91XT0tpU02RT42465QLztMbpQ9KaUb3EBums_VxGu40xZUG9VCgUE5Yk--IkWenkCpNMxHA-FdMyfcZG0QKMwg7xLDRlbvKFu2F_ZRz-34Q3H960YOOOa5ME-aXlh9w-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعال شدن آژیر های هشدار حمله موشکی در نوار مرزی اسرائیل و لبنان، بدنبال حملات احتمالی از سوی حزب‌الله لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/146587" target="_blank">📅 01:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146586">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e357503b1.mp4?token=k-h1iIZqHuRvDK7pcvHYYl-HYpWsIOD4PGvczHuKOqM0q7d9aX64axlIAlAs5yGRNEdyS2G-ktL0G_h_n0pVmTPdWasGtfvRdalrApp6rjfJF4YQPE-whh5jxHfM1N3g6P7H5cb0P4HjezWREm1NtFbaip6lzADOwP3RNZyt3ZwHSVXmOmJlz8Opf4tO93dJO7Iggg8rw2CCIed5O9r8LMzW1efD47OIViEjGUs3jQOU21WRtdUOHZ6pY_oknYfwHrOKGevg1WhiGGzB7p31F2U8kJXaiynLBB0iDYGzNBOSIBlOJ4SnaSiDZkvE4N37H8VhN4220KtIApb9-DQcSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e357503b1.mp4?token=k-h1iIZqHuRvDK7pcvHYYl-HYpWsIOD4PGvczHuKOqM0q7d9aX64axlIAlAs5yGRNEdyS2G-ktL0G_h_n0pVmTPdWasGtfvRdalrApp6rjfJF4YQPE-whh5jxHfM1N3g6P7H5cb0P4HjezWREm1NtFbaip6lzADOwP3RNZyt3ZwHSVXmOmJlz8Opf4tO93dJO7Iggg8rw2CCIed5O9r8LMzW1efD47OIViEjGUs3jQOU21WRtdUOHZ6pY_oknYfwHrOKGevg1WhiGGzB7p31F2U8kJXaiynLBB0iDYGzNBOSIBlOJ4SnaSiDZkvE4N37H8VhN4220KtIApb9-DQcSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیماهای آمریکایی در آسمان اردن در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/146586" target="_blank">📅 01:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146585">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed07c7137.mp4?token=QEK6w75ASKmuaPbhx3Jcgf1cvEfnLLirJSga1oLzf618-bIQ5k8lGk2EeNxCAnt22PqwSOxOlEsYtxRZFejT_uDeP-exU8E6epVlQbfu8m0HyNpsZCcM7j7yIypNvVOcNb2-FoY-E4TaTUZGqj3D2yQjksPwQixp_zftfni6wVrzcVWXok0PbbcHTyhqDF2rzGlfBEzw0Uvc8C1MT2Ps5iO5p0JY6lmMHk3NFG18UKIvyMR5DAS2eikJ61H-GfBicUksNDM1wzA2g4WNNeI7gvZAZ9Vv1UHF4s1zp6U-DXq5eaYQYQQ4FEpwAfEysqwkPhwbRlGYxJa8dgTyCdtvN66pyHnDUAzzLjkg-l4FZi0iCIHGh9ekK38wtFRuQfNnKHABsonHb7FEAKJoXmwLU99tQsTRZYIoHz3gbgY-COav0OWgbL-dHuSNL3pYdx5GVi2PIJOllE_ftumO5LJi2wTTyROkQCRajpXtpdchmiSQxUPptdDlTBAYbUmnFQXC5-L2cULo2-BVjdeYuM36kMLRPlZ8GrPw9-HvQ8etoA1UXqFc2Mqa9ieKz-CntXkCwyduRzNLSRDVC0EHzue4J2UOFVEUk9VJclW4N5iWf6CUEQLa6nIuUZ5fAWSc8DeeHJ6299dOQOaHnBdc_oT1RhIn74cj9XTIVa9pdt1wP7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed07c7137.mp4?token=QEK6w75ASKmuaPbhx3Jcgf1cvEfnLLirJSga1oLzf618-bIQ5k8lGk2EeNxCAnt22PqwSOxOlEsYtxRZFejT_uDeP-exU8E6epVlQbfu8m0HyNpsZCcM7j7yIypNvVOcNb2-FoY-E4TaTUZGqj3D2yQjksPwQixp_zftfni6wVrzcVWXok0PbbcHTyhqDF2rzGlfBEzw0Uvc8C1MT2Ps5iO5p0JY6lmMHk3NFG18UKIvyMR5DAS2eikJ61H-GfBicUksNDM1wzA2g4WNNeI7gvZAZ9Vv1UHF4s1zp6U-DXq5eaYQYQQ4FEpwAfEysqwkPhwbRlGYxJa8dgTyCdtvN66pyHnDUAzzLjkg-l4FZi0iCIHGh9ekK38wtFRuQfNnKHABsonHb7FEAKJoXmwLU99tQsTRZYIoHz3gbgY-COav0OWgbL-dHuSNL3pYdx5GVi2PIJOllE_ftumO5LJi2wTTyROkQCRajpXtpdchmiSQxUPptdDlTBAYbUmnFQXC5-L2cULo2-BVjdeYuM36kMLRPlZ8GrPw9-HvQ8etoA1UXqFc2Mqa9ieKz-CntXkCwyduRzNLSRDVC0EHzue4J2UOFVEUk9VJclW4N5iWf6CUEQLa6nIuUZ5fAWSc8DeeHJ6299dOQOaHnBdc_oT1RhIn74cj9XTIVa9pdt1wP7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست ترامپ در تروث‌سوشال: این رژیم به‌زودی می‌فهمد که هیچ‌کس نباید قدرت آمریکا را به چالش بکشد.
🔴
ای مردم سربلند ایران، ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/146585" target="_blank">📅 01:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146584">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
شایعه مرگ زلنسکی تکذیب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/146584" target="_blank">📅 00:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146583">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
هم اکنون زلزله ۴.۵ ریشتری اطراف بندر دیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/146583" target="_blank">📅 00:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146582">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوووووری/چند انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/146582" target="_blank">📅 00:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146580">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/نیروی دریایی سپاه موشک‌های کروز ضدکشتی را از منطقه سیریک به سمت تنگه هرمز شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/146580" target="_blank">📅 00:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146578">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری/سیریک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/146578" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146577">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری/گزارش انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/146577" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146576">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OLKgtEYwsFlYQv1YvOJSRcUDHqi8C4R5vSr1ku20W_WXo4zzYbdQm0dpVw7OGo_ewRQSGr6HGwZzHjR7G1asIOiYMNQ7DM4aEBGLPrl58Rtz4bzJGS759oAGQrv1ezn2ZsC891aA0j6kFhp3HAdhnPczLstp4Jd0Z1JhOPXNm6TXpwjh-5KXdB_POPzrr9YYs_LBizOUiWNXgGKSgopoGiSxdD-ZIn04BdKE6cXvk0PuQxKgjsYFbZ0fuGMOGLcjfF3gTic--AbM_5VEiLVHMVIdhfd2N0Ww1A2hzPBMQm-cF86hpkT6LS8L6pIQnAVE4GY3014PfSTnY4o5SqJtEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با اعلام رسمی اپل، میتونین آیفون 18 رو با اقساط ماهانه 35 دلار ( 8 میلیون تومن) خریداری کنید.
البته تو خارج، ایران نمیشه
🖤
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146576" target="_blank">📅 00:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146575">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5q_Pc1NuFrECuqogYQXpTl8v2_G1sBmaKGh4nXYvmaL2dFRMBZuaB9QR2G-EBELkQdf8E5JILHg90xCURMa9T3kZN6Z87ET-OMF5pbVtS2OlgIkCjcqLOO-sqTXWt1wcKdKVdR0S7fef9OH6dWohjfOphpsHnTeiNyCcPlpqSpWl2VtqLzHTeh8iZfxq64awWtTy8NAXjEwwiC1onXBXsHeYp8xHJtA3BLkUI0HRMp6wvKAY8EPm_WHKM53cfwQ1nt6D70CdlIxKX7BHdBl4TR6-3jW4-r9PyG_zT6mgCwrVjqYPyS8zpP16EedUtEA3L5NoLcsm0Kt7yhAER1_xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزشی‌ها که مدعی جمعیت میلیونی هستن خودشونو پاره کردن و تونستن برا محاکمه روحانی فقط ۳۵۰هزار رای جمع کنن
🤣
😂
😂
🕺
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/146575" target="_blank">📅 00:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146573">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7eba47e74.mp4?token=rBi8xjmhK1HDP_7DAubsyLoO_sCBdOBBt4pKeLm6KJVvs4HlT41U0FUEBgZRr67IflmstoUeVtTKTIMID4KpkBr4icAcZAVeeIqW_c7oWEf5846x3i5cKS4LHYLnedPO_mpKZrk3uMK9wmdsTg00v19ChKOlHp40Bc5fb6YeJjEDvCeNdswoad7dO4Wj3SPxC0HbX49cHOWwGrOS5ajAJ2yXnW0vwY6Nzn5_Ew6OPFvkPgESOcad-VxGrGJI_iNm_tWWA_NSVoFhucrW3Ty5i4vetPlp7sNK4m0YyOsoXMAfMyJ2IQJEAdRYqRvDJ5KzMnbEq2mCiy_ufInx37QhOJdEC1gvg7KA9rHnmOEkmRsH_eNsXf8ExiNgIpQakad5jOaKF6dWhuzy58rYgDRssJV4W6E2w9n5HUOYFcRY79rlCKjl2p46QiPPnK_DCEaG0nOU7MSdSu1zcdS8MKUvWzYrHMMyAVLZsG8dXzTTdIJPo8sXtcMbXRQWXWF1yi1ovWPD4FWtHiG4Wi-yduo1iYiiQurk0zHk_V9YXMF86xKxvRmV0VSC2Ei7tf2LAkFsdPnzG2GyhCR_8GL_lF9pCkCvkcZUteviogU66WSAr549qzpDdsytqplrSwLaDNq9McoplHfkY-BVjhLHJF2VZ8AUgnKLuJWCaKZIBQ2xlis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7eba47e74.mp4?token=rBi8xjmhK1HDP_7DAubsyLoO_sCBdOBBt4pKeLm6KJVvs4HlT41U0FUEBgZRr67IflmstoUeVtTKTIMID4KpkBr4icAcZAVeeIqW_c7oWEf5846x3i5cKS4LHYLnedPO_mpKZrk3uMK9wmdsTg00v19ChKOlHp40Bc5fb6YeJjEDvCeNdswoad7dO4Wj3SPxC0HbX49cHOWwGrOS5ajAJ2yXnW0vwY6Nzn5_Ew6OPFvkPgESOcad-VxGrGJI_iNm_tWWA_NSVoFhucrW3Ty5i4vetPlp7sNK4m0YyOsoXMAfMyJ2IQJEAdRYqRvDJ5KzMnbEq2mCiy_ufInx37QhOJdEC1gvg7KA9rHnmOEkmRsH_eNsXf8ExiNgIpQakad5jOaKF6dWhuzy58rYgDRssJV4W6E2w9n5HUOYFcRY79rlCKjl2p46QiPPnK_DCEaG0nOU7MSdSu1zcdS8MKUvWzYrHMMyAVLZsG8dXzTTdIJPo8sXtcMbXRQWXWF1yi1ovWPD4FWtHiG4Wi-yduo1iYiiQurk0zHk_V9YXMF86xKxvRmV0VSC2Ei7tf2LAkFsdPnzG2GyhCR_8GL_lF9pCkCvkcZUteviogU66WSAr549qzpDdsytqplrSwLaDNq9McoplHfkY-BVjhLHJF2VZ8AUgnKLuJWCaKZIBQ2xlis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب عجیب محسن افشانی در پخش زنده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/146573" target="_blank">📅 00:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146572">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0a519258.mp4?token=msV2zQgzeza0WXJTqlc3JD9PuTiKwLHzvdl7JcadjUg-boKrqVuXxANHJP6Qf8Wbr7Kvp9J7P4y1jLzv_mY5DnPvrR7p0nL84O7Qecv3MNCLbNLeMbUGvCvbV6VFXWrbzqxGUCfr29T1tdhmpnU-bDS-TvM-2iTLE0IouB8osipzy6-IVKRQ76rFRASt3jj6XTt6G6teOhpvjSe1mFMKuFLgd7uadGxkzPGfwOfRyufDuJLl9cnr0Ee8VQzo0iKE3F5o9jVENfkziYhT67Cv0nFrAY1ZF-E1I8CUwtiIaHrI0fJZU769Zq_JP9-pdc-7daDivp7xqfVb-me00h13STcI6YVOmwHkreNbmplipwqb73kfNfZQ8qZE_wPSLcZI1D99nnPjKRpZNgqMoygp-3resBNmVlD4G1LKEMX9Ybj9ZQQ72ZzlBwas_jBbbBhPrqhbp9iZrzjQpb0gYoJ1vN-gLMKwAmDbm3MS5jvyYCBkyK-jJsvhPTiiINVHhZBdr5uYsNrrVTpw-eOw8W4hU4_5MJxM-T9DZfceqcokPpuyjdgHske1w4K_SYVy7eRMeUieLBrN6xvFDvMeQLLngXSnYW4Eyv4EmWSWCi3SLEi4uHVwjnKzD8OxHPOaMvw6bc282DTqY_I1MLD5Jeku-i89f06SKLm-JKVcNo8fPmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0a519258.mp4?token=msV2zQgzeza0WXJTqlc3JD9PuTiKwLHzvdl7JcadjUg-boKrqVuXxANHJP6Qf8Wbr7Kvp9J7P4y1jLzv_mY5DnPvrR7p0nL84O7Qecv3MNCLbNLeMbUGvCvbV6VFXWrbzqxGUCfr29T1tdhmpnU-bDS-TvM-2iTLE0IouB8osipzy6-IVKRQ76rFRASt3jj6XTt6G6teOhpvjSe1mFMKuFLgd7uadGxkzPGfwOfRyufDuJLl9cnr0Ee8VQzo0iKE3F5o9jVENfkziYhT67Cv0nFrAY1ZF-E1I8CUwtiIaHrI0fJZU769Zq_JP9-pdc-7daDivp7xqfVb-me00h13STcI6YVOmwHkreNbmplipwqb73kfNfZQ8qZE_wPSLcZI1D99nnPjKRpZNgqMoygp-3resBNmVlD4G1LKEMX9Ybj9ZQQ72ZzlBwas_jBbbBhPrqhbp9iZrzjQpb0gYoJ1vN-gLMKwAmDbm3MS5jvyYCBkyK-jJsvhPTiiINVHhZBdr5uYsNrrVTpw-eOw8W4hU4_5MJxM-T9DZfceqcokPpuyjdgHske1w4K_SYVy7eRMeUieLBrN6xvFDvMeQLLngXSnYW4Eyv4EmWSWCi3SLEi4uHVwjnKzD8OxHPOaMvw6bc282DTqY_I1MLD5Jeku-i89f06SKLm-JKVcNo8fPmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه، درباره کشورهای کمک‌کننده به ایران
:
ما معتقد نیستیم که کسی چیزی به ایران بدهد که پویایی‌ها یا پارامترهای آنچه را که مشاهده می‌کنیم تغییر دهد.
🔴
در نهایت، آن‌ها همچنان به کشتی‌های دریایی شلیک می‌کنند و وقتی به کشتی‌های دریایی ما شلیک می‌کنند، در کشتی‌های تانکر قیمت پرداخت می‌کنند. آن‌ها به کشتی‌های ما اصابت نمی‌کنند، اما پنج تانکر را از دست می‌دهند.
🔴
آن‌ها دیشب پنج تانکر دیگر را از دست دادند. چهار مورد آسیب دیدند. یکی غرق شد.
🔴
آن‌ها به دلیل این کار همچنان قیمت پرداخت خواهند کرد. در همین حال، ما ادامه خواهیم داد که آن‌ها را از نظر اقتصادی خفه کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/146572" target="_blank">📅 23:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146571">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
خبرگزاری CNN: آمریکا قصد داره تاسیسات هسته ای زیرزمینی ایران رو بمباران کنه و داره برای اینکار برنامه ریزی میکنه.
🔴
آمریکا داره یه بمب سنگرشکن جدید برای اینکار تولید میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/146571" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146570">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
فایننشال تایمز: ایران برای دور زدن تحریم‌ها به رمزارز روی آورده
👈
نزدیک به ۱۰ میلیارد دلار رمزارز در سال ۲۰۲۵ از مسیر ایران جابه‌جا شده
🔴
همچنین ایران طی سال‌های گذشته توانسته از طریق استخراج بیت‌کوین نیز رمزارز به دست آورد؛ ۴.۵ درصد از کل استخراج بیت‌کوین جهان در ایران انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/146570" target="_blank">📅 23:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146569">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxrIAHEXqszZgbCV3W0kyPV2_4qtJJqbTAZrhPmPAnOG1xf-mgorUEJtfsfdDPTpx-65shdJ9Gx3l4KxmAmJ14G8MDAMrIgOvFiIK_W1QVu_4LvCS0Ws6RSGV-Lt7N2LrLK3xSzxpIoCpnObDK6iqY-Vj92Pm4ykQD5fEv2PMY8my22U4-z_8Tf1vZZx-oTRvrSEVmT1RoL2_kMo8DOpAM34tiUDp5Lat57F8BX471JEV-LriMzXLivGrZo4yP0d1uAQq8PG7ytUaOnrfpByKTIQDj8FfciSc8iZKygD6Czu526y1N-xkFT-uPv2-lRNl45qzxVuq66eDMrgrHu93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع یمنی از ترور وزیر دفاع  به همراه شماری از فرماندهان انصارالله در حمله هوایی به محل نشست آن‌ها در غرب تعز خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/146569" target="_blank">📅 23:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146568">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an6QueiHhhR5VqRhxuohFJbE-fmsfWaSoCiFYo1wIXglkwPKhlhLKdLwFpEfy4LGVLmfx5CfkhyHuNOYeXzyr7JgFMxZIaBMbhPcc1AvdCH_erCENkC85JjrYATpR2jFCwz2yHSmHrDjuvb4j9PNFG0T3qeRLVs-MDWG8Jmapsuyg2E0wCN8iDb_J1IYsVcbpjzVOaQete2Q59wZ5R3HFnZy3we5v4IWsy6ZtSmNyH2Zqbqmks-EhfDo8NMw4cwH0jCP4qt2-RLaiCkDP5I390cghhWv7x4wHDMkJTQ9IWHyz2NLsQ2lKEtArX3ugY4PUX04ENlJKAbMi0e-THrfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نکته قابل توجه در مراسم امشب اپل٬ حضور مریم عظیمی به عنوان یکی از ارائه دهندگان بود.
🔴
عظیمی از ۵ سال پیش به عنوان مهندس در بخش توسعه دوربین آیفون‌های اپل فعالیت می‌کندو امشب در این رویداد درباره قابلیت‌های فنی جدید دوربین آیفون ۱۸ صحبت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/146568" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146567">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
توپخانه اسرائیلی به ارتفاعات الدبشه در جنوب لبنان حمله توپخانه‌ای انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/146567" target="_blank">📅 22:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146566">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJWiJwH6-vzLrkfqXZKne89RWN4oR8uf1JYMx9GveA3dKNJ3mDGBxSbZfHDEzJp27cu8jdrSmXhnnOQMQtL4LXjbWsrfvHPWQonbq3CN8piHmvaWKfsgs6ppGXItfYrqZQtCtDNHGzisGAFg2wDScP0ttKs8fVcVD3RR1_yg54xVwrE57fe3Qh99QY_tQ-6vpttfDWVgD35IJjh42oAYz6jqezDT6nHwef0s-IhSuiRfdsCEUj4yYM_JQ9j2fckcyi1EaDLZVo86J9lP6AjhzZ2N_zshOEc5MZgTVwprcLY2-8-VsimbKmLiBp4nN8-bCN8DnStpMAPKEG6tWFpN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حمله هوایی اسرائیلی به قنطره در جنوب لبنان رو هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/146566" target="_blank">📅 22:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146565">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgKk79QtqD_XTFYyZjmfXIkZYqf6KwDNfOhSg1_b5YaJwZJNnmZquRA5exoucdz5jMScIkXEhbLm28b9mLCph4DlaBF3vT2Yz9aJJ5-hegWZOWUGxHzVfhwr5hkEDi8-VnqEHP6McJtiSULT5zf2dtzU8PzMyQ9mqfgDobLfuXUwDFH0kK_4XQCzPxSh5VuJQvJ8wNaCJ_wD3nLvrYvYy7EVeablqJTwT3dV3IWnk96JWantKrtDoECzEJB-DVtlhfXRADurpL3JHWEFvSIj2LWRcMO0_WquD26Bh9dt3T16ICuIomLQXxHzfF6dYKeHE-ZdvO5--XIQj1onf0OTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس، ابراهیم عزیزی
:
نیروی دریایی جمهوری اسلامی پیامی روشن فرستاد: امنیت و ثبات خلیج فارس توسط ایران مدیریت می‌شود.
🔴
به نیروهای باقی‌مانده: آنچه از تجهیزات‌تان باقی مانده را نجات دهید و در حالی که هنوز می‌توانید به خانه برگردید و بر دفاع از مرزهای خودتان تمرکز کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/146565" target="_blank">📅 22:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146564">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PtQiUXtPuUTcGHzb1QHbvGKdRxKHyrqexqfQ9wosWH1jEKvLfX2Hl1Elqgxi-Kc8n5YhjAEyxSuxBGeCdbhjfUpYyFMuXK5mm-1tVR5NBa3uwtZCNWRdTzMdhOc-PooxcuBGKEPNM6pSk6oc56Ka_Ct0ptJHYWZGNEWdqweSUGWu4Uiz3Eqswzj-iBquSdX6weE2pNqloLgQyz5ki4opDlk5USHDBkMMKxw45kI3LRMk-IDDG8d_QbsF53qsSB8fUSFKIokiF9CdmpUcjsAAy2oHSQ4RcO6g1732Kj7LG5FUwETKTcVeVFgky8pTqq7YzvLv9VnvkgaUiXg0wDnXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جو ویلسون، نماینده جمهوری‌خواه: ائتلاف دفاعی مکه اعلام کرده است که حمله به یک کشور، به منزله حمله به همه است. اکنون زمان آن است که ترکیه، پاکستان و عربستان سعودی، حوثی‌ها را نابود کنند. یمن آزاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/146564" target="_blank">📅 22:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146563">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccdf5d3613.mp4?token=aJC-YHetxJHtGqowGrw6dfXRMXnEmFYB8Ste4CujnieqwYLseCVYuZFhQlrwXalRUWUljF_ZpdKgReUER37q9QYOHVZxC3To1yhmDDjne65713bb_0NVZ5hW2FF8Ay2RJK4SwpNDz9GnM2SrokvA9UlpavKvT_s7HBTi7GID93WHZZyLhVT4lXac3_Q5LOcKPHO3E-kDypQqr5Yd2FZM-daP8dIKjxw9EPtro7CgF5832s0-qU30A_ASv_MkTBj5DBERBIvm5fHaToo4952DiOCGRue4kll8ZZMP_axnvWXCYQjvgt5Ii7cO3arNNLxZV8gM8m2y4wO7ipu7FYKw_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccdf5d3613.mp4?token=aJC-YHetxJHtGqowGrw6dfXRMXnEmFYB8Ste4CujnieqwYLseCVYuZFhQlrwXalRUWUljF_ZpdKgReUER37q9QYOHVZxC3To1yhmDDjne65713bb_0NVZ5hW2FF8Ay2RJK4SwpNDz9GnM2SrokvA9UlpavKvT_s7HBTi7GID93WHZZyLhVT4lXac3_Q5LOcKPHO3E-kDypQqr5Yd2FZM-daP8dIKjxw9EPtro7CgF5832s0-qU30A_ASv_MkTBj5DBERBIvm5fHaToo4952DiOCGRue4kll8ZZMP_axnvWXCYQjvgt5Ii7cO3arNNLxZV8gM8m2y4wO7ipu7FYKw_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر
:
مشکل در رابطه با روسیه و اوکراین چیست؟
🔴
ترامپ
:
مشکل این است که این دو نفر (پوتین و زلنسکی) از هم متنفرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/146563" target="_blank">📅 22:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146562">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سفیر پاکستان در روسیه گفت: با وجود تشدید اخیر تنش‌ها در منطقه، ما معتقدیم که به‌زودی تفاهم بهتری بین ایالات متحده و ایران حاصل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/146562" target="_blank">📅 22:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9273210828.mp4?token=rxaRs-mLnQAOUQXdreZBey9zPYxJnOYm3reLP5rc64jUBhA37TvIIql791gvUs9YYdAsdXmsL8fU7KbuwV8Nk0ErTTXXxWX0PX9q1zVDPdx6TJFSdcxHF0ZeM5Q31hyBOdlykNkwwcngRh0x0jTqgjuivwYD0g0Aisdos2VMx6CPxSYu8GDA_vIp4EVkS_5GkWtbEPwr1WAWvPNQBVH4gYdFQYqU2XtW6s1EI9y-kJMNwkf-wrbNlv_iuoP4rqBwgNrGKTYRUjUAgKUjWCMom7kAN8SVmy6ZVfdPwisVRu79KZqBvc55C_wYaKIxuxvbY9VyPqDh8WB-rkKfQrSBBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9273210828.mp4?token=rxaRs-mLnQAOUQXdreZBey9zPYxJnOYm3reLP5rc64jUBhA37TvIIql791gvUs9YYdAsdXmsL8fU7KbuwV8Nk0ErTTXXxWX0PX9q1zVDPdx6TJFSdcxHF0ZeM5Q31hyBOdlykNkwwcngRh0x0jTqgjuivwYD0g0Aisdos2VMx6CPxSYu8GDA_vIp4EVkS_5GkWtbEPwr1WAWvPNQBVH4gYdFQYqU2XtW6s1EI9y-kJMNwkf-wrbNlv_iuoP4rqBwgNrGKTYRUjUAgKUjWCMom7kAN8SVmy6ZVfdPwisVRu79KZqBvc55C_wYaKIxuxvbY9VyPqDh8WB-rkKfQrSBBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدراعظم آلمان، مِرتس
:
بدهی‌های افراطی، حاکمیت ما و توانایی عملی ما را تهدید می‌کند.
🔴
بنابراین، وظیفه‌ای که البته دردناک است، به ما سپرده شده تا اولویت‌ها را تعیین کنیم و نمی‌توانیم با پذیرش بدهی‌های جدید اروپایی از این موضوع فرار کنیم.
🔴
بودجه‌ای از قرن بیستم، مشکلات قرن بیست‌ویکم را حل نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/146561" target="_blank">📅 22:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146560">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=vcvHaX7lOEaJ_t-cxjDXzSjURsVckh6aFuB3TYnxHnMUfA_SM98k3UxkBaLAmCce2mCu8WuOaaxu1tT2xbIAMKb88zHGlar9Pp4WmfdNpVbdPVM_HqbroI5AysQBWZ8OZZvqXG_CVxWCc1ErDbmJ8UvnGBiTERbHlE6LHLqSWIeJWZfeBKWBXd9j6CqnQ_xWNkUFtix60ctbj0r2wsqT-buzAAwqt9h1kb4Y1cTLe-yuX-5HweBCzUDa9V_F55kpUrMa17COZDRhGwGYSClWY_W2AeQA5BypfY_eQAK9HUlQelGxh9a7LyMIzTMmF_R3K9JnyyjwtZtxKCSBbggeJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=vcvHaX7lOEaJ_t-cxjDXzSjURsVckh6aFuB3TYnxHnMUfA_SM98k3UxkBaLAmCce2mCu8WuOaaxu1tT2xbIAMKb88zHGlar9Pp4WmfdNpVbdPVM_HqbroI5AysQBWZ8OZZvqXG_CVxWCc1ErDbmJ8UvnGBiTERbHlE6LHLqSWIeJWZfeBKWBXd9j6CqnQ_xWNkUFtix60ctbj0r2wsqT-buzAAwqt9h1kb4Y1cTLe-yuX-5HweBCzUDa9V_F55kpUrMa17COZDRhGwGYSClWY_W2AeQA5BypfY_eQAK9HUlQelGxh9a7LyMIzTMmF_R3K9JnyyjwtZtxKCSBbggeJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهپاد های (قایق‌های بدون سرنشین) اوکراین (USV) در حال حمله به بندر سوتی در استان کراسنودار روسیه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/146560" target="_blank">📅 22:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما به دنبال مذاکره با ایران نیستیم.
🔴
در ابتدا، من می‌خواستم یک توافق به دست آورم. اما وضعیت به جایی رسیده که تقریباً هیچ کشوری از ایران باقی نمانده است.
🔴
احتمالاً مذاکره‌ای ممکن است، اما این چیزی نیست که ما به دنبال آن باشیم.
🔴
این جنگ بلافاصله پس از انتخابات ما به پایان خواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/146559" target="_blank">📅 22:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146558">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=AHmcuXXrpGSBUXUQTguMqNFMziHNZs0VX5i_pO-ZlY_x0YgFbSM80RBR0ulkfgIhc0S9OYuLO869LfIU_mbSCwth9L_VOCkjSlYIfp0OyYM5TkRlXf6TKbZz-VdbmD-bh50_Kl1hHjSTWwHZOVJdMRwCcyyKN09BPt_N8YxQTVEWUAqrzTp6xEHT1vU7xqNXcFIHTRoHzFE5Sn5wckTlGqtqwT2SaBHZ7biFNGHXSje2uqmOfKWaVuPfy73VlicmeA--ZGSM_ukQFCqpnbArZTvNgfxTaOYQYnQkWmU6mZ6PrH2UnU58UPvcn9-feRO7kGeMBDNipJ8KV1S6JmdEvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=AHmcuXXrpGSBUXUQTguMqNFMziHNZs0VX5i_pO-ZlY_x0YgFbSM80RBR0ulkfgIhc0S9OYuLO869LfIU_mbSCwth9L_VOCkjSlYIfp0OyYM5TkRlXf6TKbZz-VdbmD-bh50_Kl1hHjSTWwHZOVJdMRwCcyyKN09BPt_N8YxQTVEWUAqrzTp6xEHT1vU7xqNXcFIHTRoHzFE5Sn5wckTlGqtqwT2SaBHZ7biFNGHXSje2uqmOfKWaVuPfy73VlicmeA--ZGSM_ukQFCqpnbArZTvNgfxTaOYQYnQkWmU6mZ6PrH2UnU58UPvcn9-feRO7kGeMBDNipJ8KV1S6JmdEvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: من کاری بسیار فراتر از یک توافق هسته‌ای انجام می‌دهم. مسائل دیگری نیز وجود خواهند داشت که شش ماه پیش اصلاً مطرح نمی‌شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/146558" target="_blank">📅 22:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/146557" target="_blank">📅 22:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146556">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owmoT1-4hnslljOPDHqBo67RJndwbODn6Da8Zd5vynE7AgZETfqRnNAQSPwZ2ju9kvEoZXBiArVPq1PgVVB0K3Fr7xoazfxNpieO-w0MTR2nTSh1OOPXNV3QPCrTzUvB0NnpqKvVvjdJE52uRfRiTxz7sCnlou6UqXOVUCQvKAC8X5bzdXRcWyoLGvhKhwrsgETMAxKT22a0BPT5us8XOSpUpLuj3rov0O9ZMbkUpa4tMA0d81zNYz82tMcvGoEWog9z6BBkByZYm785ZPM-DuuUM8JDqe1uEZ0ZFk3AKgFUz1hOQu2HSzlok4e6g_AS1YPvPty-SZdk9ZKxqv4ky4zE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owmoT1-4hnslljOPDHqBo67RJndwbODn6Da8Zd5vynE7AgZETfqRnNAQSPwZ2ju9kvEoZXBiArVPq1PgVVB0K3Fr7xoazfxNpieO-w0MTR2nTSh1OOPXNV3QPCrTzUvB0NnpqKvVvjdJE52uRfRiTxz7sCnlou6UqXOVUCQvKAC8X5bzdXRcWyoLGvhKhwrsgETMAxKT22a0BPT5us8XOSpUpLuj3rov0O9ZMbkUpa4tMA0d81zNYz82tMcvGoEWog9z6BBkByZYm785ZPM-DuuUM8JDqe1uEZ0ZFk3AKgFUz1hOQu2HSzlok4e6g_AS1YPvPty-SZdk9ZKxqv4ky4zE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: به نظر من، جنگ بلافاصله پس از انتخابات به پایان خواهد رسید، زیرا آن‌ها دیگر نمی‌توانند مقاومت کنند.
🔴
آن‌ها به شدت تلاش می‌کنند تا بر انتخابات تأثیر بگذارند، به طوری که ما بتوانیم گروهی ضعیف را به قدرت برسانیم و آن‌ها را تنها بگذاریم و به آن‌ها اجازه دهیم که سلاح هسته‌ای خود را داشته باشند.
🔴
تنها چیزی که آن‌ها می‌خواهند، یک سلاح هسته‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/146556" target="_blank">📅 22:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9702dcbc.mp4?token=LbrFaySAsmM2uh9R4sW8Lpyk9FtIgAY4oDC7jnzUXLxIM_Gz2MlyHMCG2l0ggzHaTsT2aYHYhj-i2xqeIP7_plvY7XfRRaCFdm9i3xVosCN4268oWGw0_Io3j_ZE1Wmp8e_odeHHiwjDZBeG2F0DKIqvsdK4gLk_9SUEAiuvIZTjV_-NmZYApnWO40KDa-k1B6zJ4UwAsEzBBRg4jPzrmPMvbQnUXsR0DtCpRTgo8nj8xndXVQ3GXbkTvQIjGq9LDUyRqIhHgvH1c-DF9K_ES6ryhNZnPsRHk9WMaCIxomZ5jvFZFSNByRF3niETcOpBdn0pr-vdDoe2Sunij9bJrUp43hzAtz7Pm6ofYx9XYOodu3N2_eYWnqZOsmvCdV70uragC0pjJdPui9Jq3U-HaypW8CMnxjtAw-2JmrT38RMlcgFdqGoeGTqbBM2Bnve80E_I1-BJIXph-GI9CrfhYpB0mCKq7JmdSjBmvouxPd0xEbVmW0KplOFc4bdPOWwtCUFNKG2OviL5YMKrmAAi_NXlvtA4irjSLE6rWBikzuI9DCL4bPStmxkBu6KlU-mkmTdtJ38YUbnRCtyKTF6rwGTVWi0NpMz9uzVvk6s21OFAMfGa9XFKx9OL8Zh3rGHaCvRqtgRqx31uS2hEsWSHQ2hTKKtAJ32IFb6YVLNUJiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9702dcbc.mp4?token=LbrFaySAsmM2uh9R4sW8Lpyk9FtIgAY4oDC7jnzUXLxIM_Gz2MlyHMCG2l0ggzHaTsT2aYHYhj-i2xqeIP7_plvY7XfRRaCFdm9i3xVosCN4268oWGw0_Io3j_ZE1Wmp8e_odeHHiwjDZBeG2F0DKIqvsdK4gLk_9SUEAiuvIZTjV_-NmZYApnWO40KDa-k1B6zJ4UwAsEzBBRg4jPzrmPMvbQnUXsR0DtCpRTgo8nj8xndXVQ3GXbkTvQIjGq9LDUyRqIhHgvH1c-DF9K_ES6ryhNZnPsRHk9WMaCIxomZ5jvFZFSNByRF3niETcOpBdn0pr-vdDoe2Sunij9bJrUp43hzAtz7Pm6ofYx9XYOodu3N2_eYWnqZOsmvCdV70uragC0pjJdPui9Jq3U-HaypW8CMnxjtAw-2JmrT38RMlcgFdqGoeGTqbBM2Bnve80E_I1-BJIXph-GI9CrfhYpB0mCKq7JmdSjBmvouxPd0xEbVmW0KplOFc4bdPOWwtCUFNKG2OviL5YMKrmAAi_NXlvtA4irjSLE6rWBikzuI9DCL4bPStmxkBu6KlU-mkmTdtJ38YUbnRCtyKTF6rwGTVWi0NpMz9uzVvk6s21OFAMfGa9XFKx9OL8Zh3rGHaCvRqtgRqx31uS2hEsWSHQ2hTKKtAJ32IFb6YVLNUJiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: بریتانیا، فرانسه و کانادا تحریم‌هایی را علیه شهرک‌های اسرائیلی در کرانه باختری اعمال کرده‌اند. واکنش شما چیست؟
🔴
ترامپ: من با اسرائیل و با آن‌ها صحبت خواهم کرد و تلاش می‌کنم بفهمم که نظرشان چیست.
🔴
من دقیقاً می‌دانم چه اتفاقی در حال رخ دادن است، اما می‌خواهم بفهمم چرا این اتفاق ناگهان رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/146555" target="_blank">📅 22:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146554">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cfbdafcf.mp4?token=eLxYjI5J3caUorQbyBl0293Vi-P1N2KaookuCtWLDplBXe61l8R3qwEJdFEttnT_JUuCJWu2FqezxIy6UEgsWOmth-fSUajvddtUCtCXZIdhHRQYEeToVFCbLXjQ06qlQb6BPDN4vrpgFzuEHxVl1L8-TRJh_WYHfsNIZ_FDPXtITo8sF4NPuulw85lp9VMwl0-YEARpK2PTkiWL0XFzsvMzw6SsLqZCiaW0jTk9B2DXyUYHhWTjD2IzowstAqDWjPqRCuObdAxXDz9oS_QPWJvGOMTatK6J-gGyP5IslGJijjpfEgsn3dLNjGEjlBQzyX8LDrL5H4gzm2YxYgammQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cfbdafcf.mp4?token=eLxYjI5J3caUorQbyBl0293Vi-P1N2KaookuCtWLDplBXe61l8R3qwEJdFEttnT_JUuCJWu2FqezxIy6UEgsWOmth-fSUajvddtUCtCXZIdhHRQYEeToVFCbLXjQ06qlQb6BPDN4vrpgFzuEHxVl1L8-TRJh_WYHfsNIZ_FDPXtITo8sF4NPuulw85lp9VMwl0-YEARpK2PTkiWL0XFzsvMzw6SsLqZCiaW0jTk9B2DXyUYHhWTjD2IzowstAqDWjPqRCuObdAxXDz9oS_QPWJvGOMTatK6J-gGyP5IslGJijjpfEgsn3dLNjGEjlBQzyX8LDrL5H4gzm2YxYgammQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی از ترامپ درباره احتمال برگزاری یک نشست سه جانبه بین آمریکا، اوکراین و روسیه سوال شد، او پاسخ داد: «ممکن است این اتفاق بیفتد... افراد زیادی در آن جنگ جان خود را از دست می‌دهند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/146554" target="_blank">📅 22:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146553">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: ۹ نفتکش ایران را نابود کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/146553" target="_blank">📅 22:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=hr-jnyrLRi1wqc4jsLyaLywuoB-wRlz0ZQ_TBaNB384QX6AAFKQX5-_XawGdK-c9lPvAcl4Gv2xMUsofelZrdFcG-ofAscXPiysoQgMMszDnWet8YI-4aRKnYtQWK2trZGjVgsdmnoQkcP_hQTcPfxZxtmv4avKpbcLy8OrxTmPWRtOZ7x0jAnWSi-5visBTVWBzXTscro6bApb71XErQ3wFl3_a1EcbZWVaRwso5OLzXFOL0LC-N9vTMIUt-HQ6A5Ycqab1NZNOT8vfk_IL1rWbdkbjtycTYCGy0wr-CAJvJgttP-_bJ22-k4vqMFPGBpndJZJqsmTKihMVNOTl4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=hr-jnyrLRi1wqc4jsLyaLywuoB-wRlz0ZQ_TBaNB384QX6AAFKQX5-_XawGdK-c9lPvAcl4Gv2xMUsofelZrdFcG-ofAscXPiysoQgMMszDnWet8YI-4aRKnYtQWK2trZGjVgsdmnoQkcP_hQTcPfxZxtmv4avKpbcLy8OrxTmPWRtOZ7x0jAnWSi-5visBTVWBzXTscro6bApb71XErQ3wFl3_a1EcbZWVaRwso5OLzXFOL0LC-N9vTMIUt-HQ6A5Ycqab1NZNOT8vfk_IL1rWbdkbjtycTYCGy0wr-CAJvJgttP-_bJ22-k4vqMFPGBpndJZJqsmTKihMVNOTl4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: بلافاصله پس از انتخابات، قیمت نفت به شدت کاهش خواهد یافت.
🔴
ما قیمت‌ها را پایین خواهیم آورد، به زیر ۲ دلار به ازای هر گالن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/146552" target="_blank">📅 22:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما به دنبال توافق نیستیم... من بسیار بیشتر از یک توافق هسته‌ای انجام می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/146551" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146550">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوووووووووری/ترامپ:
حملات بیشتری علیه ایران انجام خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/146550" target="_blank">📅 22:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146549">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
خبرنگار خطاب به ترامپ: شما گفتید که قیمت نفت و گاز قرار است کاهش پیدا کند. اما قیمت نفت اکنون دوباره به بالای ۱۰۰ دلار رسیده است. این موضوع را چگونه برای مردم آمریکا توضیح می‌دهید؟
🔴
ترامپ:  توضیح آن برای مردم آمریکا بسیار ساده است: فقط کافی است بپرسید، آیا اجازه می‌دهید ایران به سلاح هسته‌ای دست پیدا کند؟ پاسخ، خیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/146549" target="_blank">📅 22:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146548">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ درباره اوکراین: «ما گفت‌وگوی بسیار خوبی با پوتین داشتیم. او می‌خواهد به توافق برسد.
🔴
اگر زلنسکی هم بخواهد به توافق برسد، بسیار خوب خواهد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/146548" target="_blank">📅 22:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146547">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / ترامپ : حملات بیشتری علیه ایران انجام خواهیم داد.
🔴
جنگ ایران بلافاصله پس از انتخابات میان‌دوره‌ای پایان خواهد یافت.
🔴
قیمت نفت پس از انتخابات میان‌دوره‌ای آمریکا به طور قابل توجهی کاهش خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/146547" target="_blank">📅 22:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146546">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بقایی: ارجاع پرونده هسته‌ای ایران به شورای امنیت موضوعیت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/146546" target="_blank">📅 21:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146545">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
خبرگزاری فرانسه (AFP) به نقل از نخست‌وزیر نروژ گزارش داد که یک پهپاد در جریان سفر ولادیمیر زلنسکی، رئیس‌جمهور اوکراین به اسلو، به هواپیمای حامل او بسیار نزدیک شده است
🔴
این حادثه امنیتی که در مسیر پرواز زلنسکی به سمت پایتخت نروژ رخ داده، خطر برخورد پهپاد با هواپیمای حامل رئیس‌جمهور اوکراین را به همراه داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/146545" target="_blank">📅 21:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146544">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فکر کنم منظورت اخبار اولیه اجرای مکانیسم ماشه بود. آره اون زمان میخواستن بگن تاثیر خاصی نداره...   فرداش دلارو از ۱۰۶ ریختن تا ۹۷    الان جواب میدم
👇</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/146544" target="_blank">📅 21:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146543">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ در حال حاضر یک جلسه اضطراری در کاخ سفید درباره ایران برگزار می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/146543" target="_blank">📅 21:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146542">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری /  شبکه12 اسرائیل : اسرائیل تصمیم گرفته است که به هر حمله موشکی جمهوری اسلامی حتی اگر به اشتباه از مرزهای اردن عبور کند، پاسخ دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/146542" target="_blank">📅 21:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146541">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
یک هلیکوپتر یو‌اچ-۶۰ بلک‌هاوک اوکراینی در ۴ سپتامبر، زمانی که در فرودگاه ژولیانای استان کییف مستقر بود، هدف یک پهپاد گران-۴ روسی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/146541" target="_blank">📅 21:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146540">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac518bf53c.mp4?token=AROKK-Q3azoy7JYxgKdUUs54JCEhMa8sKU9bFyq3SfVshmBhKUoULVYMiummJatoVujIsqYqTbVQz_X-x68TvvT5UgAiFGHFnb7kbS6JN1WGSeZbR9EQEfIGq0I7Py7x1LbjQPAsCgGVti62NecE7FhhwqW8CegN0dG00kpeq5SfEquE9yYTtg6BV4yPXx6UCzyOStgwDUC_q5gDvmhs0HYFgpZlpsAcz2pogTDSEj8-7H_P8XHAIzWpNij3yv9jssyqgm_xVypkR9PfxfV9YgVm7fYcY6YQxDi9z8ecgOsFAIDfB4ixYVwJOifDbvv_SNR1227RdbjllRmY8UfXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac518bf53c.mp4?token=AROKK-Q3azoy7JYxgKdUUs54JCEhMa8sKU9bFyq3SfVshmBhKUoULVYMiummJatoVujIsqYqTbVQz_X-x68TvvT5UgAiFGHFnb7kbS6JN1WGSeZbR9EQEfIGq0I7Py7x1LbjQPAsCgGVti62NecE7FhhwqW8CegN0dG00kpeq5SfEquE9yYTtg6BV4yPXx6UCzyOStgwDUC_q5gDvmhs0HYFgpZlpsAcz2pogTDSEj8-7H_P8XHAIzWpNij3yv9jssyqgm_xVypkR9PfxfV9YgVm7fYcY6YQxDi9z8ecgOsFAIDfB4ixYVwJOifDbvv_SNR1227RdbjllRmY8UfXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه حمله هوایی اسرائیل به پایتخت قطر که هدف آن برخی از رهبران جنبش حماس بوده است، برای نخستین بار منتشر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/146540" target="_blank">📅 21:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146539">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_iJnfflPDYKHC1otFg2HeDv0keZVvhwiCcV1Ar5B6KvJb4zBXIMeP43aaUxFbOA9oktM_CL7wKNlCwKgtwGuFTttNHvhMu6xJ1IaiY5jznnQ1scxzkmFOeet5r780jAvRCxeMLJrSunfv7vHJ_pZMPRxabEfJiphbSEUA1McWmux60w6EAnBqg9Cue7IR-ypjqktbwhuy2DcZ-OC4XJZOaTBS-RHUkhnIDD_dJnGkvmI66olda3tveIuruL64tppn9tuNR5gIfVxMFvmHsMKDqHLEhE_PUkoIqVW5STnQ08yCIL0tnw66ocMA_0q6K87y8IRIG4wXKYFuUPxkgmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از آیفون ۱۸ و رنگ هاش رسما رونمایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/146539" target="_blank">📅 21:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146538">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_De418wWNGQOxy1MTrDLIJLlUkCy1YbJH0JJdJ5-IQ57-KoymcN9plVFS-kAQ44TWOkHt44DU8XeQvcbz7Rf3P3NUCb1Ifb4bJbygSXvrobFduAhLso96e6I-rNl91of-thXaiQEw679z5oMMnPZVjePINNTl9sxcp5NLplf7ed30pgJ5ixI7DZhMD3Bup6ruga1haXFa2tZNVfy4JK6rC3S0aLezD_nkqrHYhW4vClFfJ_fsu2A2KdATyxG6MOHsU47lupv0y6C6jiyYnMkzOhOKz4JtcOJatBWf2Zp_aUZA57kytQOrvETMuysV_FVspkXHRUZYRfCK_mVj7WbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش شبکه خبری NewsNation، دونالد ترامپ همچنان در بخش غربی کاخ سفید حضور دارد و هنوز به شهر دالاس ایالت تگزاس، که قرار بود به آن سفر کند، نرفته است
🔴
ترامپ در حال حاضر در حال دریافت گزارش‌های اطلاعاتی است و در این جلسه معاون رئیس‌جمهور، جِی. دی. ونس، وزیر جنگ، پیتر هگست، و ژنرال دان کین حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/146538" target="_blank">📅 21:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146537">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه نیوز نیشن گفت که هیچ حمله‌ای از سوی ایالات متحده در ایران یا تنگه هرمز انجام نمی‌شود: «ما در حال حاضر حمله‌ای انجام نمی‌دهیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/146537" target="_blank">📅 21:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146536">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کانال ۱۴: ایالات متحده آمریکا تأیید کرده است که نیروی دریایی سپاه یک شهپاد زیرآبی آمریکایی از نوع Dive-LD را که دچار خرابی شده بود و رها شده بود، به دست گرفته است؛ با این توضیح که این وسیله نقلیه پیش از آنکه تهران آن را بازیابی کند، عملاً در آب بی‌حرکت و غیرفعال شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/146536" target="_blank">📅 21:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146535">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نتانیاهو‌‌: متعهد به‌ سقوط نظام در ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/146535" target="_blank">📅 20:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146534">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOhnRJh1Tgjbk1xJ4wP-A-seJuSXiKHxPTl6Ux-cGMTekJoB2D6ZgHJgwawuVyGNpRLTr-14WuKJh7njalDELNsQJ7zIIPs9QkL0fsHOJ5uAwkei2pxO5rC6gbHOF_nJ8SerXt4TbAWem_3I8H0ywjcSZ-TwQPxzvLdnwWRqzqzIV2Y9fvJ5Qgh5W6dhdANuOcureuVhAz2pf01GHzdMgyVIaN7QML2KZC8vVwsz5hmqqpCQtp5Ri6HGAp8siF_cKObycLQhIW9AR0sbXlCx7PeUzjgNtxstcL8m1ssr832d0EDaCp2OiVoD2LnIZf14qqKpxYpkMGjA0y3XWzbe0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / وزارت خارجه ترکیه نیز حمایت خود را از عربستان اعلام کرد به نظر پیمان مکه ممکن است بزودی در یمن وارد جنگ شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/146534" target="_blank">📅 20:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146533">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGcqYrUQbPcpQT9mRvCqckOqOvOj9aD5TdhiiyekIqaFo-BBzEvizJUMtJBIh8K267Nz8IOCPyvAwEjVkX-VcEYBCbd5db5RTasoci6JNQXYML1uLAsUnJW8YxkFzE-s4bEZPEmJVXL99nnEcUscM4guKSDePrC-mIzXNZ95wGDNvlC3Wsowhw3MVn7hJzHFnwylnsuUJ5MpDYj5zVpdxcrRSJMH_2n22XGBobScAzvKZ3u0_PivvYsaTrghiI7_1mdupPSINIMj5h_DzwVzkYT6kVQWQX3BG3MgtdBXxguyloW_H9bbwhkoXALq4boNCcJNbcTBeUwIChVlPNItaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا نیز حمایت خود را از شورای ریاست جمهوری یمن در مقابل انصارالله و ایران اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/146533" target="_blank">📅 20:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146532">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsnV8Er0wVqKb1FtVmZODW4aSA8wuDbP-NSZYMX7Ui3tc-MvG7WvlCM3ZWn1KcZdl7NXI9RI2QxmkpwSK1Tge0U0ZSy3XOxWFWGRtoI8csG2XImsBWQi_vZCk9-4AXpSC1q_LQw1Z6OdzaXCXTlET4ajcJhaTPal21W1iEdaUkU814_etgbjAy7ld7D9MmEEqe2LMHH2MSoCdSPo-Gv3CAL8h18V9WsaA3ZhAdyj1TDsZSsrcEi11dqhyY4vuWwBMY4qbTRNJqD05tRzWhex4D_K_v7GUZKtGBxUylsu8tzrGadazL1yX1dG7edXCrGI3ma4uQ5pjEE5aQEVx-N7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش غریب آبادی به تصویب قطعنامه علیه ایران در شورای حکام
معاون وزیر خارجه:
🔴
به تأسیسات هسته‌ای تحت پادمان ایران حمله می‌کنند، روند عادی راستی‌آزمایی را مختل می‌کنند و بعد همان اختلال را دستاویز صدور قطعنامه در شورای حکام قرار می‌دهند.
🔴
با این فضاسازی‌ها نه می توانید شکست سیاست ها و اقدامات خود را جبران کنید و نه می‌توانید در شورای امنیت کاری از پیش ببرید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/146532" target="_blank">📅 20:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146531">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دلار و طلا منفجر شد
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/AlirezaMehrabi_ir
https://t.me/AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/146531" target="_blank">📅 20:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146530">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ایران: در صورت خاتمه شرایط جنگی، زمینه برای فعالیت‌های پادمانی آژانس فراهم می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/146530" target="_blank">📅 20:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146529">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG419-QYMN5Xw5G_ECVoODFTBLQygxOv-2_zdPrWLmxLCj-gR-qte5YZP0jETvxzm3r_z5RuNzoJ4rlWogpih2ZCkYflb1edJaleXeJEIkq3toHzhkqs2yNV9vHgDVJK2sNivFuxZHIF6RzU4s8P8ik-qTnSUtR5ONziwFzKe4cXc82-ap4SZF947pHtaW1_rFYiB1NiCgKTpFFC2SpUcQLfU72uJnfpf2tRVumv7pI6DI-zP0A4rAmzmOQujZi-dkCr8r6huq8gjI15ZhKcANUqgBRNrn1r3vdhaLAL-5Y6M6KNy-bePP5QToLZIl41Jd8laL5cxQX0dU6fM-HXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد شهباز شریف نخست وزیر پاکستان با محکوم کردن حملات انصارالله حمایت خود را از عربستان سعودی اعلام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/146529" target="_blank">📅 20:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146528">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پس از حمایت ترامپ از حزب "AFD"، بر اساس گزارش‌ها، مرتس، صدراعظم آلمان، یک دیدار برنامه‌ریزی‌شده با رئیس‌جمهور ایالات متحده را لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/146528" target="_blank">📅 20:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146527">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
صداوسیما: تو حملات شب گذشته، ۳ نظامی آمریکایی رو کشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/146527" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146526">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فارس : شنیده‌شدن صدای انفجار از سمت دریا در جنوب جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/146526" target="_blank">📅 20:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146525">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YacVtgeGsCn_j78Ikw1jWA3WP7aXHykvZobTYSHz-jyVMXN0p0vTcwZaBvp3EvHCBw-CVKWJfReVS9n3GSLP_557r5BhNQ6kWlXaS6IM722xkxXj4qP704tB1OZSdQD1ntQzYWpKKmGakSeQYK-8CQwrGBRLPQzCVZPLONpq_859I0zrqm35TB2J_s3uZl8os0g1HDMyMxpJ8_qAVScpW7ogJFOIE2ml3f39rncuTxOpoS_8MizHQOS7ffZzIKheKx2VhdP0Pues4U8uh6UmQUuQMFbam3EIcBJWC02tDSSm0Kk9HV-rD5oGpBQ8cuxXxbWXlVaRrUHghYdTj3nT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنتی: ایران در برابر زورگویی سر خم نمی‌کند، برای مقابله با فشار اقتصادی به روحیه جهادی نیاز داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/146525" target="_blank">📅 20:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146524">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری/ قطعنامه آمریکا و اروپا علیه برنامه هسته‌ای ایران در شورای حکام تصویب شد
🔴
این قطعنامه که با ۲۳ رأی موافق، ۸ رأی ممتنع و ۳ رأی مخالف به تصویب رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/146524" target="_blank">📅 20:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146523">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZAJbewoSV9br9-UT3B9_5yLR8_oakcy-wSXUjgjqKnFHqnq0OKcFyJ2ShmK25JVa9rphXYvPoWDNYgJxFl_hIjjHQmNiPh1jjuYLYBdurtbXn4Qg23PdysiHLSH412GwkIAIudpbe7sLkUEbpMUPBf5rN27ZhiinM_lRKPb_h4pC3TGopCqid4R3tUKKCvR5AgstxqS3QW9qnj2a_K05y_XZvDXFqYLLezdireYCYMfIDR_c3Pqz33fHVv6maoXvd_szNq7tyYEwbWW8GVTXFW_XWLm4NDdbnB5lX3jWerY2kJdmQMMCandFxwknxHhmypY9YFwwae-2KFYvAdwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل به تازگی منطقه سِروبین در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/146523" target="_blank">📅 20:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146522">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
بیانیه ایران، روسیه و چین در نشست شورای حکام: ارجاع پروندۀ هسته‌ای ایران به شورای امنیت مبنای حقوقی ندارد
🔴
راه‌حل پایدار برای وضعیت کنونی تنها از طریق توقف فوری و دائمی تمامی حملات و رفع تهدید به تجاوز بیشتر حاصل می‌شود
🔴
همه پرسش‌های مشروع درباره برنامه هسته‌ای ایران باید منحصراً از طریق گفت‌وگو و دیپلماسی بررسی شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/146522" target="_blank">📅 19:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146521">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
بیانیه مشترک ایران، روسیه و چین:  از اعضای شورای حکام آژانس اتمی می‌خواهیم به پیش‌نویس قطعنامه آمریکایی-اروپایی رأی ندهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/146521" target="_blank">📅 19:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146520">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e110a0cad2.mp4?token=Gd12rUSJTjIt6UxP5t0Tqn4yltDSJG-2e3u3YnJhQ0luznMSqLjM9Gc1nW5SQIkv-KRfPxt3yF_NBEQUvAQO0LOD3NwAvchu5AXY5yyhfry8hAeRVV_H5IbR-KVmPAe5Fu99NEy_qPwSlN2jKraePF3hKBcvgckraDeH6U3eqNxTDYHP5eQg6OzAIP49N9rZr6MOs84rTLu7vkFoKHzk5VNXAN_207wVQg31rgasB-BSx6VTrmpcQoqM-kCKkud3fbhqr2rwZQZFwHAsGencUXBLG0ygPfPwH6To_xqsp6uRiQyUNgx6UJtmFvoaOiLYGPh92dG9GHYmqi3IcTDrW29ienQUeBJg74HxKVbB9Zrp4Ou9mz6lmujgzjHFFNv57Y2VQEY7Z05N7mLRHnmJIsSpGdUDtdIjo7Nst5fFuHNdfS88qDcauUsI0RYkc4oAa6wtoseAmrb7lBnJ7z3M09rmm9xxX9LUK4z3pdXolKZpMrEFX7nH4Sb4GaNcXzcF4acr5W3I8NzgSGkd_-f9yi-7gL9k_2aWHaUaZhilO78xZUjsm9VD06mUDmLBzmpDs8Hlc9Y9c1iMRpV8tL_jK8299Pa-EQqC15VKVW-NdYDh5j7qtjwohTUqR48SfYAkuK2i8z5VtR8zRSfDxFWA5THMQa-l8AFQnvOahBvhZKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e110a0cad2.mp4?token=Gd12rUSJTjIt6UxP5t0Tqn4yltDSJG-2e3u3YnJhQ0luznMSqLjM9Gc1nW5SQIkv-KRfPxt3yF_NBEQUvAQO0LOD3NwAvchu5AXY5yyhfry8hAeRVV_H5IbR-KVmPAe5Fu99NEy_qPwSlN2jKraePF3hKBcvgckraDeH6U3eqNxTDYHP5eQg6OzAIP49N9rZr6MOs84rTLu7vkFoKHzk5VNXAN_207wVQg31rgasB-BSx6VTrmpcQoqM-kCKkud3fbhqr2rwZQZFwHAsGencUXBLG0ygPfPwH6To_xqsp6uRiQyUNgx6UJtmFvoaOiLYGPh92dG9GHYmqi3IcTDrW29ienQUeBJg74HxKVbB9Zrp4Ou9mz6lmujgzjHFFNv57Y2VQEY7Z05N7mLRHnmJIsSpGdUDtdIjo7Nst5fFuHNdfS88qDcauUsI0RYkc4oAa6wtoseAmrb7lBnJ7z3M09rmm9xxX9LUK4z3pdXolKZpMrEFX7nH4Sb4GaNcXzcF4acr5W3I8NzgSGkd_-f9yi-7gL9k_2aWHaUaZhilO78xZUjsm9VD06mUDmLBzmpDs8Hlc9Y9c1iMRpV8tL_jK8299Pa-EQqC15VKVW-NdYDh5j7qtjwohTUqR48SfYAkuK2i8z5VtR8zRSfDxFWA5THMQa-l8AFQnvOahBvhZKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه روسیه، سرگئی لاوروف: می‌گویند که روسیه به یک منطقه حائل نیاز دارد. اجازه دهید اوکراین این منطقه حائل باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/146520" target="_blank">📅 19:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146519">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSx1aBQIyl2fb_sI_WitZqH4Po6sx6-eFM8-H2SFceEAVW9Sjfn_FFZ3h3BeiiBGV66YFb_45sY4_nxk2O6B5H2ZIDI_icejw2fhn2SC6KefAw-BXoNDh5QUACJmN3ff-xlGWJgTxPQPE5tS8FU_0eA47fFEq49R51s7E0QAfmBFEtp-EARIXTOgBn07ciKRZ311Ht2UjlhFJoYpSVWrCPm55VgNnwasTn8GbZPS44ivNQZOIiWY08EDWcSpckO-WNQsnk53NSabsz5BPGmsxv_Aab5pLipd6XKkD0xncSQRj-ODRv2G10N7-x7WnjD4CsU5f8LaOBCmYiiXmnqIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیست قیمت انواع موبایل ریجستری در بازار
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/146519" target="_blank">📅 19:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146518">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
بیانیه مشترک ایران، روسیه و چین:
از اعضای شورای حکام آژانس اتمی می‌خواهیم به پیش‌نویس قطعنامه آمریکایی-اروپایی رأی ندهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/146518" target="_blank">📅 19:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146517">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/گزارش‌هایی تایید نشده از شنیده شدن صدای انفجار در جاسک خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/146517" target="_blank">📅 19:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146516">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmAleP4XGJtkgAWwLEgDzkWQjPHPYYtxMG2UqPINYfNP7Bg1FmwGauZ1S_4tWUBrp-mLqzBiogZEHGfCDQ0kG9oL2IjG0_z2MjHLKlEACzTOJ75fVJyN4AHCpIW_NBuByzJAStLDlTMLbmsy5owutcEZatDFrfGwe05bUZ8rYQdozbMsm7ZnQ3kR2CoMKDaqmSrYetMvHYbGj0Q525IkTaunWplN63J_5QAT54GNz9wmyeQIIW0bg2eRuq9K8a_fuS_ZsuY_E6D1Flmzec0SipOCYVPmY2B-S4Fte72PYPHjeYvatsoEJKx7PbFsy6lntLCriT-Wxt283tCpuODwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت 101 دلاری شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/146516" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146515">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
تعدادی از ژنرال‌های پاکستانی در حال حاضر در ترکیه حضور دارند و احتمالاً جلسه‌ای در مورد تحولات یمن برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/146515" target="_blank">📅 18:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146514">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5n7wGoXRbtXQmqq-UDTSVOyQJHpTSxfRSlMj7KQ0jUm-7R3HMgva6L8LZkCCf6nz120MBb6v44z3rqcysGAqm4CyOrt-imDErP_dyxsJCNFZtwfLEtiKlIYTTN_tECYGbc4RiHeT6UoObNVgrBhCpHUYw2ageWzKCYznhLKFaAa6Xf5iYUiW5bm1M9Bz01d7PjiPZbNNS8FWscybadnME-0Watp5ViSqPqk-rhDhH8cxd2OguuQzZHJtUSzK9WLrH14M2CHwBMqQgXLUYUHjVB_zjW0ywuBzE2bh5HmUEyITIsruWkfTzH92cRtobzCXHC5G7c8DtuNQpTOouQkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس گزارش می‌دهد که بسیاری از جمهوری‌خواهان و دستیاران کاخ سفید تا حد زیادی از تلاش برای مهار پرزیدنت ترامپ دست کشیده‌اند، حتی در حالی که به‌طور فزاینده‌ای از شهود سیاسی او تردید دارند.
«
چرا زحمت بکشیم
؟» یک مشاور بلندمدت گفت. «
رئیس اونه
.»
با نگرانی جمهوری‌خواهان درباره انتخابات میانه‌ها، دستیاران به‌طور فزاینده‌ای «
از خواسته‌های او پیروی می‌کنند».
یک اهداکننده این پویایی را این‌گونه خلاصه کرد: «
هرچه بخواهد، به دست می‌آورد
.»
با این حال، افراد درون‌کاره ایده‌ی کمرنگ شدن ترامپ را رد می‌کنند. یک مشاور با استدلال اینکه ترامپ حتی پس از پایان دوره ریاست‌جمهوری‌اش «شخصیت سیاسی غالب» باقی خواهد ماند، گفت: «کاهش ارزش ترامپ را به خطر بیفتید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/146514" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146513">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6836a952.mp4?token=p2W41eDEwydQ8hqqFs6MPN9a2M_4mT_GQnZwfsxEe4TkaiampfNjtAv6dIR2TOlO8fLxw-1LR92erz6ge_-L4XIjpx3ArXb2HSKLL7KGzaq06N8JikZZqn28_ZsZwZ83Z_amyeEY5GvBPDKXZlkY9DdOVU3JIbTlhqaHLbMN6qNpBeljQsUBDwXT2wWvj8vvCF2AdGeeUc8VJFGlQhjGNiGZBX14q5r_a8BzIwK9G5hoN7WgSoLLDSytJ6geIzFtzJNarjXSdDHvrJ-KuLQR67f-b9LKB-jPeK4E0V4iwDTVF_BNwTQQHK-ztgKZhLYgtl17FKWb0D4IRxTXKSV0ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6836a952.mp4?token=p2W41eDEwydQ8hqqFs6MPN9a2M_4mT_GQnZwfsxEe4TkaiampfNjtAv6dIR2TOlO8fLxw-1LR92erz6ge_-L4XIjpx3ArXb2HSKLL7KGzaq06N8JikZZqn28_ZsZwZ83Z_amyeEY5GvBPDKXZlkY9DdOVU3JIbTlhqaHLbMN6qNpBeljQsUBDwXT2wWvj8vvCF2AdGeeUc8VJFGlQhjGNiGZBX14q5r_a8BzIwK9G5hoN7WgSoLLDSytJ6geIzFtzJNarjXSdDHvrJ-KuLQR67f-b9LKB-jPeK4E0V4iwDTVF_BNwTQQHK-ztgKZhLYgtl17FKWb0D4IRxTXKSV0ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعاری که دیشب گروهی از حامیان حکومت‌ تو شب نشینی شبانه می‌دادن :
🔴
تو تاریکی می‌شینیم، ذلت نمی‌پذیریم.
🔴
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
🔴
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
🔴
مهریه کم میگیریم، ذلت نمی پذیریم.
🔴
پ.ن: این جماعت ۱درصدی رو باید صاف فرستاد یمن تا برای میلیون‌ها ایرانی نسخه نپیچن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/146513" target="_blank">📅 18:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146512">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOlv4L2GpttlrVuajrdCdtd5s0S_dD85CzRI1nDrGIS6zdiBa6VJgUg9k4vegns7jVroEoXC1PhDnPJlm3G9bs_pjBvgA87fUEN6QMU4G5O_mqlrRT8zp_DpwAiHSX6bU0cxVrvhfmPlIcpa1cWXqqwIyO9BH7cGbJyWDwbPZvCkJZDdj37JIEs_82sCiRtBFxDDvJAO4itOoYhpNWl-7Hj0t-ZYP6nXvWKxjEaMS1_SpRjRXwzGzWE6MJWakEYplOLkavdVbzbPzAWm8FDymv8EyvEekJ8JYwggVhkyC-guntjZH3P68OidxyPozgVEslA0wNv7du_NimHNWsxvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز :
آمریکا در این دور حملات شش نفتکش ملی ایران و ده نفتکش دیگر مرتبط را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/146512" target="_blank">📅 18:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146511">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IuxgwAq2loJ8nkC49wJNnpX8HO7aacRrjVviOB64jRfsX0mh8WXvTYWmc2qekz2VpBCwdi0eIAlWO8HhZRyjl3Kc-jE1mRD7VvSUCnB3ocqBhnq6LoAquTMRf0q4PjeE3x27j-651lmijdhsiszHnnGQyRfSuo1HwRDVUV75yR-YPay4d_JTpDFRRTUqYHEVDinmSAgLW-nazaY6e2ITaYhmj5tgWhaQ95RWrmlaESMwK06_Y1quonXk_d88S5mJ_TJWPDiuYNsVHbaYkGw5ZwMrmc-sPZOilOKMPfyJvM55Y0oNAJTQ45jGAA2-UV9XU8JqcMZlZT6CeG2WbCwimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل در حرکتی ناگهانی اعلام کرد تونل های کوه علی الطاهر از کار افتاده‌اند و نیاز به انفجار آنها نیست و به پشت خط زرد عقب نشینی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/146511" target="_blank">📅 18:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146510">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">جالبه دیروزم ترامپ میگفت دیگه ایران اصلا نمیتونه با این وضع سلاح هسته ای داشته باشه  یعنی حالا توافق هسته ای هم نکردیم، نکردیم!
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/146510" target="_blank">📅 17:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146509">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNQFD5XYw81kdJHM14lUwKo7DFZRxCKjeSqBkQgvFRePQbz8GDWzhANZPMVLFXhkBHErIaB15CUt8ynM9KVjmBfb6M-pNHvEa55deaTzvS5ioWgJ2V_MFdtD4Gj25h8ihwo6vu3xDWdx6vjHrLGSsubB1j3MeXEKZ3NYkqTF5q9f5Nf3eSXOzRCBA2iNBajnxgaw95pqupx1BqVcKJmdtAVwxyJ511UhvDA-bBMyrwqHYmfFE3kUVekILtddTYAZECJ2z1_WY6kdf2fbWqnMUVTr6ZzXIw_pHzmxvbQl-sI1VX8iPYokj3FC96fGZmT9D110_ovVmwAaPEFkO6quDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعدادی از ژنرال‌های پاکستانی در حال حاضر در ترکیه حضور دارند و احتمالاً جلسه‌ای در مورد تحولات یمن برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/146509" target="_blank">📅 17:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146508">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رویترز: در پی حمله به نفتکش «هرکولس استار» در نزدیکی دبی، یک نفر کشته و یک نفر دیگر مفقود شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/146508" target="_blank">📅 17:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146507">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اعزام سوخت رسان های آمریکایی به عربستان!
🔴
طبق گزارش ها چندین هواپیمای سوخت رسان آمریکایی در حال ورود به پایگاه های آمریکا در عربستان سعودی می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/146507" target="_blank">📅 17:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146506">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
روزنامه جروزالم پست:
اسرائیل در حال حاضر خودش رو برای یک حمله چندجانبه از سوی ایران در روزهای آینده، همزمان با سال نو یهودی که برگزار می‌شود، آماده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/146506" target="_blank">📅 17:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146503">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJEvji_jHPO4UT2Ik0cjc1XJMNuyQBXQDGKW9YynY0z_bJomsUnm9x21mnO2wzN4a1Ee6VdoMplBumVnUPaZt-Pu2D_3oIxKUwkwFsiJycrp-3f4d65z8WPsTOKSq12DYrrhm1_EQ0TCUSSsZe1NX3-FpMZn0ZLtmCwz4IAEAnUGD65kD0Tz6nkbCfIzVcsQ6LWN7fUupoa-MeEZeLGSz-a79iycpgHdHgwzcPsffaQFEiL5253rcYSS-780vI-JfhD20v3bybVgV_uA5-EZ5L4oZCQQhJSq66u7tyeM0ImlgljTJdYBe-ROxIWwzvGwwgrKTLigjzSnOZ-zdF7vag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBSvzj7czB-c7Lm03Mp7yaJTxqKbjYLY9G1M-eBpXTawykELZjt09C9t_KxpovuJoKkE4bSO3_aa6HjZ8zc2OHNmNmYNXj3IgJM0qo-foSr4yEuulgAweBvUeqOkC-8f7QBtL8QXkgWNZ71mRf1HStuSycrEKeHYtESZ8udMl2nev3fywy_wW3wFwUZ_8SWFGlyRnexwOBKB1HCLfB_ej9cOsp-WizWt0JJzoialaQ9hQ6Nz-u3MYfb3VKpaM85VP1BuqdNig8Vq9CXepNqOTf7i4_kPzqUCPJkxWm0tySTQ8mGPIE-NAMYKennNFeNxFY7_ur6d3ev2Kkm-MhDBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLTeNoMLgxQdTVQ-RH9E2BQ7C5KaBZg-I2aDancUcgMfARkHcIDYqELpA_RPMzcQfgWarvi_o0psT8RiA-_UHAlZ8oC58zV6qop-Cdt9UgvScRyfuUqvbzZlUWk7SOyGOEnbA1hE4nEvUNJh9MSk_aBV6h00BOSHETJ1cCrALRKyxkjcgx0nxrvLhXxWTMAQLOqRhXVWlzBfnyZb2zE7gp6bZleRT6E1spbBrmtr7MG4aBb6EeDsHrYL4RbMvhoNSMxS0Udg8Ie3XTSneiIu-isGkr9T7Xpj_Q25P6CkoFnoSPrLfL9jUGzI_tmZVno29AOLYWfMD8YR3M_S3-kYkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نتانیاهو و کاتز، وزیر دفاع، از قله کوه هرمون در سوریه بازدید کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/146503" target="_blank">📅 17:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146502">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/guQAvN8Nxy-p9wfUJTkYaLfPPaLPJfrdre84NCwc9dNcELGhRhkSiTqflcEXKujvQo7pRLg_nsoiGGjjxsc9VDSLSOk9bWhdqw9LKBvnHb_EOPFwkExOnWIehjwDwOabI8WfuwISLB2ZpzjHjJMq7ieZ_CeeB6GK_9Se5Upl3LFDCpCvR_tqkLBQ1uN6EeK5NJb1zR4KF9d4-v6zi9niRlHk8KYXlKDiAap_CP2KQ0SvsmSXuJ6U7SDAN0ON0jAH1jrhHF5zHO4rVXAfF7p6NGqfcH7RHnGQ7A4mapM9ZwViGAXATq49E6IzqW8BDH6rJ22N6cL8_5mevjfTdc4-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قبل از رونمایی رسمی، مشخصات آیفون ۱۸ لو رفت!
نکته قابل توجه اینه که رسما از آیفون فولد(تاشو) رونمایی شد.
آیفون ۱۸ پرو توی چهار رنگ گیلاسی، خاکستری، سفید و مشکی معرفی میشه.
قیمت پایه آیفون ۱۸ پرو: ۱۱۹۹ دلار(۲۸۰ میلیون)
قیمت پایه آیفون ۱۸ پرومکس: ۱۲۹۹ دلار
(۳۰۵ میلیون)
این قیمتا بدون گمرک و... هست، وقتی وارد ایران باشه حداقل ۳ـ۴ برابر این قیمتا خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/146502" target="_blank">📅 17:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146501">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
مجتبی یوسفی، نماینده مجلس: خودروی چینی بی‌کیفیت رو دو برابر قیمت به مردم فروختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/146501" target="_blank">📅 17:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146500">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
🔴
https://t.me/AlirezaMehrabi_ir
🔴
https://t.me/AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/146500" target="_blank">📅 16:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146499">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ارم نیوز: آمریکا در حال بررسی حضور تفنگداران دریایی خود در برخی جزایر خالی از سکنه ایران در اطراف تنگه هرمز است
🔴
در صورت اجرای این طرح، جنگنده‌های اف‌ـ۳۵بی مستقر در ناو تریپولی وظیفه پشتیبانی هوایی از تفنگداران را بر عهده خواهند داشت.
🔴
هدف این طرح، ایجاد نقاط دیده‌بانی و پایگاه‌های لجستیکی برای نظارت بر تنگه و حفاظت از کشتی‌های تجاری عنوان شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/146499" target="_blank">📅 16:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146498">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
شرکت نفت کویت، این امکان را به خریداران ارائه می‌دهد که انتقال بار از یک کشتی به کشتی دیگر در خارج از تنگه هرمز انجام شود تا حمل و نقل ایمن‌تری به مقاصد نهایی تضمین گردد.
🔴
این شرکت اعلام کرده است که برخی از کشتی‌ها همچنان در شرایطی که ایمن است، از طریق این تنگه عبور می‌کنند، در حالی که انتقال بار از یک کشتی به کشتی دیگر به عنوان یک گزینه جایگزین ارائه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/146498" target="_blank">📅 16:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146497">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
اوکراین در حال عقد قرارداد برای دریافت حدود هزار موشک رهگیر پاتریوت با تأمین مالی اتحادیه اروپا است.
🔴
با این حال، تحویل این موشک‌ها در کوتاه‌مدت انجام نخواهد شد و کی‌یف به همین دلیل از کشورهای غربی خواسته بخشی از ذخایر فعلی خود را فوراً در اختیار اوکراین قرار دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/146497" target="_blank">📅 16:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146496">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
روزنامه جروزالم پست: اسرائیل در حال حاضر خود را برای یک حمله چندجانبه از سوی ایران در روزهای آینده، همزمان با سال نو یهودی که برگزار می‌شود، آماده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/146496" target="_blank">📅 16:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146495">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزیر امور خارجه اسرائیل، گیدئون ساعار: اسرائیل تنها کشور دموکراتیک در خاورمیانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/146495" target="_blank">📅 16:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146494">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6573f5e81.mp4?token=S-PdGMr9JHqOyDRJzrqAmWbbrWZUdCcIXZN8lyPk_YRQOjf3nrtiFhHJNJzY2xoYgdPizqIFNRRByTaaGW12L2At0wDnBqgJmS6j04wXHxJiPT0nHbNehVMRS6MiX5TMiAVQNuPqU-ezO5yWU-YHqG7hoWyKRWYaFjLuLEBGyn7PGSEufsFCYmTZ8rRoGYVybeaVmDxU-mMelrKdE5uKXD5b1U9lmH3RDgjg_uuzrdkRwXV2e247B5EfDxIsDM3KXwqBXCBISq0dj9qDyLiW0gfSl-i0eqhjz4BWLBkD2d9-SWFqExe4vBvfjVGo5N5A2w021nBocGAs9pfx40NHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6573f5e81.mp4?token=S-PdGMr9JHqOyDRJzrqAmWbbrWZUdCcIXZN8lyPk_YRQOjf3nrtiFhHJNJzY2xoYgdPizqIFNRRByTaaGW12L2At0wDnBqgJmS6j04wXHxJiPT0nHbNehVMRS6MiX5TMiAVQNuPqU-ezO5yWU-YHqG7hoWyKRWYaFjLuLEBGyn7PGSEufsFCYmTZ8rRoGYVybeaVmDxU-mMelrKdE5uKXD5b1U9lmH3RDgjg_uuzrdkRwXV2e247B5EfDxIsDM3KXwqBXCBISq0dj9qDyLiW0gfSl-i0eqhjz4BWLBkD2d9-SWFqExe4vBvfjVGo5N5A2w021nBocGAs9pfx40NHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای ائتلاف جنوب، نزدیک به امارات، سعی کردند طاهر العقیلی وزیر دفاع یمن را که مورد حمایت عربستان است، گروگان بگیرند
🔴
این دو نیرو علیه انصارالله یمن با همدیگر متحد شده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/146494" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146493">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJdQFNns8vwlNAcvaXm-Kr8dR1-DZWTNGDN-3j4Ae0D7TpSQtGcQLu-_8PvVvLrOwhzBT0ySakJg307YmK-P2IJnTr9mTpkeA6MS0xjolX6dPECMkiot2uIzX1khL-gxWsnJLTCbfOOd-56r07MbzbD9NncGWMGiBjUdps_FmZHNzlOPc-4PBWrltWBcteYsAIJA1KoqKTb5HDJwlcPn1IEdcKW5rBD4I7M93YEGcoDfJHvDqX2pqC5rawm-MX5Hhd6nxHVuWdbHWNrMqClDbIwgpFbO9JgufTzZVbdBWRm76BkvWEdcfMhVws8v0T-TUbJ0h-JTIX0HGu0NT6cmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه ایران، چاپ شهریور ۱۳۸۲
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/146493" target="_blank">📅 16:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146492">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
شعار در شب نشینی‌های شبانه
دلار بشه یه میلیون
تسلیم نمیشه ایرون
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/146492" target="_blank">📅 16:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146491">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رویترز: در پی حمله به یک تانکر حامل محصولات نفتی به نام "هرکولِس استار" در نزدیکی دبی، یک نفر کشته و یک نفر مفقود شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/146491" target="_blank">📅 16:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146490">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=JIvodwS650VCPRGrnlB3GShAXA6GiFGH-v4rgH9ZNmD2JfG8A1ry7gVyrc53Wmft-LpMyMYj4TyV-dqvTq-YecXjOSnYYShv9yZJtKtkgKXFyhsJMxVH-CT3WtkDe-vp5lWLYlM4DKzztd2v9-fr_hkHQQGTJfpXwiIzCJ5jI7nskYuhf_bgc66w3wJ4Va_OIq7c2VPlhHC6cpHuMwPi3We_NE49x5YSX_YU6fXVVn9k1ZlAtPqZ1jnbyaYGygj4E_-EMhpESPT9s4UG_sH4nJ-QzqGxkd3i4skKaynuhJX3PCVLBmIHUvXLjdbMJCLBoVIdDqGXxI1RG8e416BARQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=JIvodwS650VCPRGrnlB3GShAXA6GiFGH-v4rgH9ZNmD2JfG8A1ry7gVyrc53Wmft-LpMyMYj4TyV-dqvTq-YecXjOSnYYShv9yZJtKtkgKXFyhsJMxVH-CT3WtkDe-vp5lWLYlM4DKzztd2v9-fr_hkHQQGTJfpXwiIzCJ5jI7nskYuhf_bgc66w3wJ4Va_OIq7c2VPlhHC6cpHuMwPi3We_NE49x5YSX_YU6fXVVn9k1ZlAtPqZ1jnbyaYGygj4E_-EMhpESPT9s4UG_sH4nJ-QzqGxkd3i4skKaynuhJX3PCVLBmIHUvXLjdbMJCLBoVIdDqGXxI1RG8e416BARQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز، چندین حمله هوایی عربستان سعودی، مواضع حوثی‌ها (انصارالله) را در جبهه مریب در یمن هدف قرار داد، این اقدام به منظور حمایت از عملیات شورای انتقالی جنوب (PLC) انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/146490" target="_blank">📅 16:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146489">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تتر توی برخی صرافی های ایرانی تا ۲۴۰ هزار تومن هم معامله شد
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/146489" target="_blank">📅 16:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146488">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
الجزیره به نقل از یک منبع عراقی: هدف قرار دادن نفتکش در آب‌های سرزمینی عراق، در نزدیکی بندر العمیه در بصره، رخ داده است.
🔴
نفتکش هدف قرارگرفته حامل ۲ میلیون بشکه نفت عراق بوده و در منطقه بارگیری قرار داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/146488" target="_blank">📅 15:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146487">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که یک جنگنده سعودی از نوع F-15SA در تاریخ 7 سپتامبر، دو بار به زندان مرکزی در شهر ال‌حزم، واقع در استان الجوف، حمله کرد و در نتیجه، تعداد زیادی از زندانیان و بازدیدکنندگان، از جمله زنان و کودکان، کشته شدند.
🔴
آنها گفتند که این هواپیما ساعت 16:30 از پایگاه هوایی خالد در خمیس مشیت برخاست، حملات را انجام داد و ساعت 16:45 به پایگاه بازگشت.
🔴
این گروه هشدار داد که عربستان سعودی به دلیل این حمله مرگبار، با عواقب روبرو خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/146487" target="_blank">📅 15:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146486">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
👈
سی‌ان‌ان به نقل از منابع آگاه: تلاش‌های آمریکا برای تدوین برنامه‌هایی برای حملات قاطع علیه تأسیسات هسته‌ای زیرزمینی ایران ادامه دارد.
🔴
‏این تأسیسات زیرزمینی احتمالاً به عنوان پناهگاهی امن برای برنامه هسته‌ای ایران طراحی شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/146486" target="_blank">📅 15:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146485">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
آیدیش:
@khabar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/146485" target="_blank">📅 15:34 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
