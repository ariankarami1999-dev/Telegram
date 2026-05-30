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
<img src="https://cdn4.telesco.pe/file/sKFWNxPpngTFxR8rB8D1vP4VGx5HkIUknD6dxQBBnXsT_e_dj15kE8TIJoYX8qj8flqB3ROIrIAC7ZMc0LFMVjPHZmBsJozjLF4xb_t-DELs5u9t9Po1mGFdTC60oDxbxeyFcW92urjOmeALcF5RPn_nI34629G6bN3_MRkCVMyT5rPeilLSWb32q-VVsFpWJUeiiqNDZeQK51WDfq00V8PuZvieuJBssJtaMT7hQUsn_e5EKytVq4oRIULn804WiITMH1keKiVxLCNbogW_ZXC0uwUSAhqZ2xvoLc4q-vMgZHVR-nDdQ6jzWmY1Am1yJLpAB6NY6O9CZ-WL0eCAsA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 179K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 13:51:29</div>
<hr>

<div class="tg-post" id="msg-76322">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">برا مثال شاهی به هیپهاپولوژیست دیس ناموسی میده
بعد کاگان میاد باهاش کار می‌بنده الان
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 311 · <a href="https://t.me/funhiphop/76322" target="_blank">📅 13:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76321">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حاجی شاید نداشته بنده خدا مسخرش نکنین</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/funhiphop/76321" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76320">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3rdEBpujToiluGWOgB5Heob1SNhuKJtwOvx6oxOjbemjYjKmkdhPb1IT9WHXjFtitHnf0e9tpHU9djTLfF7R3pRbCGna0DXpAjyPDY2pTKcw_bh4DLF3N8UrwhwmRieiTBKkmzh-gTeZsLIHj-lNmmUizkXONptyAHhTCUKYHC_QIOpvegUVhaBRdZFaFCr4M8f5FxfeVc-QblEu-uAL6J7Kk9llrrQce-hSOMT8IRhkpbqbPvxZPdIGQSOmX_v6eckohhYuoTXCMTKrjJ1ZAfm3v-YpYzouxTZ-1tDacoqTgzMWmnjmJyl7NsEn_NZjZ3Xm4vt2MWlLpxh44Q9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیو نمیفهمن پوبون جان؟
اینکه چرا کصشو تو میکنی بعد پول بیمارستانشو ما باید بدیم؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/funhiphop/76320" target="_blank">📅 13:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76319">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نتیجه بازی امشب رو پیش‌بینی کنید، دو نفر اولی که پیش بینیشون درست در بیاد باید نفری صد هزار تومن به کارت من بزنن.
@FunHipHop
| محمدرضا ناصری آزاد</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/funhiphop/76319" target="_blank">📅 13:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76318">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJrFsukjKO1TJRBFkwXLgftpvZJHQK7kUg2TVeHVqXOeVY33n_NSDxKYjhlqnIAbUgoDfvLov7GUFx3Ezuc7zFbAjUEDc5bSodo7J9_YqLWN47LAcn23LhsHLUchKXe_ya0IYRTrBOoMu30Iuc9QiM5uCJO18kQBwkHMg5SfofxDxWDT9eDZ0UeJr9lVQFez0kka2gwwMy9GDww4P9QAhjrVckB6evh9NDTi3a-mOYwHkJREgcT85DYrkQFtHdPWmwh6tawOnZ20hZbKMaGyVcmh1xe7J-SkYa8kuifUgOuf7JlSx4BPFqD81Wqy7DThJS4Mqg7Ae-4F8je2CwZTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/76318" target="_blank">📅 12:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76317">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خداشاهده ۳ ماهه تو ضعیف ترین نقطه ی ایران توی روستا توی نت ملی و قطعی کامل اینترنت من وصل بودم
تا پزشکیان نتو بازکرده نصف روز قطعم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/funhiphop/76317" target="_blank">📅 12:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76316">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کنکور سراسری به همراه آزمون پذیرش دانشجو معلم پنجشنبه و جمعه ۲۹ و ۳۰ مرداد ماه برگزار میشه، البته اگه باز نزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/funhiphop/76316" target="_blank">📅 11:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76315">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پولاتونو جمع کنید ببندید رو پاریس، دریک رو آرسنال بسته</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/76315" target="_blank">📅 11:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76313">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-r71Fi9t5WYacAPycOc06tN3vPbKir-42TZvymNBwYCvY4cOpV_nFgaa3JOge6kdlTMcVLS_b5ZBzLKDhgNhgQKe5NMTJygMR2ezomwpZMuAOEH-wudigVHN6V3H4g4J0an4gWNb6H5kOvVOriq6HNk-73Z9FXbv-E10Hf36sDmiUixP3NcXvv_pHvMis70s3QjoZghYtxrZ33q98js3M8CxYG4LmtLii0wZdrxIko017V_IBwrGBLBz4jCaaAi_hGXmtEhE0fef4VBJ5v08bIqC9nfYNXxQhiWMgdgrBLrYEGMRj5E81Msbpcu24uRF-vR_C7BLyTzIFL6rPK7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس تهران
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/76313" target="_blank">📅 11:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76312">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خدایا خودت امشب به سگ و گربه های مشهد رحم کن.
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/76312" target="_blank">📅 10:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76311">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdJJSW1-g9skIl_h3F06qo9nolc52JfIq6FhMzvmWlnQOr0zOrT3hSShIyTpBbPAbGNuQnRTd4aYjdL3xiERUWRJhEgb-BwYlAdpdzx7xZBGdta_IqSLJ36eH-z5m3tThOTS26CQM4WC3FvVO1OwklFMziUPwlytw4N8ZYT_tqLmeoB8fwNQUz9LOXErs_COtYYnd994Ja79Tzt4Hmp8FymScoUhUjYR-F-vu1pTmJn9nt51Hd0Dbd34r9j9Npf-lcRkPJ-rpUV6t-XhkpJpd4Od2dQTRwrd-aj-UnaLXQA5I7bwgPBVQ-k1XNBUXDitqxnqmajnsqtDF8D34bfv5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب فینال لیگ قهرمانان داریم.
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/funhiphop/76311" target="_blank">📅 10:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76310">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/funhiphop/76310" target="_blank">📅 10:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76309">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1CKH6_u-D1EBENpcLXdFE32_DwEkmK2DMvdnVzhZ6DSze0XV57XdnRNPzwRvS6GVnay7nYthjd4-7azmJR1NzCJZKu5t2xFu7oLUeiYEalVAoYwRSpvsQOpQp2oau2yeorh6YHKyA3F9-gX1n6drqox_YC505BvUX2VxukWTnyPeSgL_Slr0l4l6Eta62IOI4I5dMHDpPWQUfaMBy3K_VdVB1iPDrOG6EsorN2EHb4V3RYZXm0RzAJHc_i9AtHC36cqfv6CUWpZpSCJPvP48dvGV6soyFM4s5jTFU6R5B4Xu7z_tKClToCKyjbaWdutj4DvO8ErH4LqqAmylFF7_w.jpg" alt="photo" loading="lazy"/></div>
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
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r9
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/funhiphop/76309" target="_blank">📅 10:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76308">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b21fcfedbc.mp4?token=uUo3DWqe5zaHbLC1WWXKYkj_EO2tuBs38RByGTXD_ElO5vAjjqZ7hh2JMr3otmiZqeIrXMAVJuRZNVeUovwrRRYkjXdFeo9HJZk8Nr3AlmoCjhBCCigi707kUiDTo4phqsO3JZ1uV-QAXNlMHz9TYmtTf8bYFQIisDy_xzwIde470t4nRP_EKp9k3Hg7w7Crxz-OP4KlHDbtWtCilBazWBh2T-WG_jEy178ZruLDOhWf-qXOQxjMtEz4vOXqo-l-BPbSdSeNWUGc2btPlVOt4Bjkj8nb16ru7uzrsJY1puJ6vUGj41Vz7lmYqyqqAwa1a4g4kQ5nO74vlQIAhHKOXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b21fcfedbc.mp4?token=uUo3DWqe5zaHbLC1WWXKYkj_EO2tuBs38RByGTXD_ElO5vAjjqZ7hh2JMr3otmiZqeIrXMAVJuRZNVeUovwrRRYkjXdFeo9HJZk8Nr3AlmoCjhBCCigi707kUiDTo4phqsO3JZ1uV-QAXNlMHz9TYmtTf8bYFQIisDy_xzwIde470t4nRP_EKp9k3Hg7w7Crxz-OP4KlHDbtWtCilBazWBh2T-WG_jEy178ZruLDOhWf-qXOQxjMtEz4vOXqo-l-BPbSdSeNWUGc2btPlVOt4Bjkj8nb16ru7uzrsJY1puJ6vUGj41Vz7lmYqyqqAwa1a4g4kQ5nO74vlQIAhHKOXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/funhiphop/76308" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76307">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310846887a.mp4?token=USkKe31WBRnrhu2kceilzmvO7hGGBJpdppamOIn5Be2cEYX7otTNxweJmGDs3vGwHl6SKt-NdLUPfAMBt_aWUNzay60-PM33H_Y6ZC1fu7GPXonRLGXTAeZYDLHlgQdEtA1Uj1aSmbMyPchd8mDo4Rj-BdwxfJVmdmUCN2n3Tyof4xlHT4bMu2eMh7FqoIp3rx50m43Qv_dcemTn3x7EIolwQ0KO9z3Zz7W89_B64I-BCly3Ivo2STIEfWYUZanaN-60FQkQ6KrxIQpZW5nQpG5ygX5uQFsXHC0dPgtFj6yLaRR55K8VzH-I_Lyv42GQ_J26gd_2ITds_FiAk0EWiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310846887a.mp4?token=USkKe31WBRnrhu2kceilzmvO7hGGBJpdppamOIn5Be2cEYX7otTNxweJmGDs3vGwHl6SKt-NdLUPfAMBt_aWUNzay60-PM33H_Y6ZC1fu7GPXonRLGXTAeZYDLHlgQdEtA1Uj1aSmbMyPchd8mDo4Rj-BdwxfJVmdmUCN2n3Tyof4xlHT4bMu2eMh7FqoIp3rx50m43Qv_dcemTn3x7EIolwQ0KO9z3Zz7W89_B64I-BCly3Ivo2STIEfWYUZanaN-60FQkQ6KrxIQpZW5nQpG5ygX5uQFsXHC0dPgtFj6yLaRR55K8VzH-I_Lyv42GQ_J26gd_2ITds_FiAk0EWiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست:
همین چند روز پیش در جلسه کابینه بودیم و رئیس جمهور گفت: "هی، این یک معامله عالی خواهد بود، و اگر ایران نمیخواد توافق بزرگی انجام بده که تضمین کنه به سلاح هسته ای دست پیدا نمی کنه، میتونه با مرد سمت چپ من برخورد کنه."
و این تنها باری بود که به چپ بودن متهم شدم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/76307" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76305">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ca4GME08dCXYfg6TgqaN2gnKwgdiGU4xgFMKGGMWde3385RK2Yv4_KNwzbodcN4o08_4BZwB0GZ-vJOzRDN--bRxji48IZLQPqH7Q48GqNj-Wpj9f6rJEXK5qxMPsjsQEc1hntneN10ZfY_Hsp3Jqloi-bVEfmiDEOepMj7m9MAyaLyH86jpTUIlaR8t5lnWFb7mCrd51GRVyOWPVIHrpGV6TTGYEsqKDk3soKyixhi9MCkJXHVs7VCPIkXmzzC8OeoA2aKzsTkzI6ceF1nHprYIOlUfUfowR7aZ9rfpUYjYmfJTW5XlCXUmCp4HwFieAKdUTbJOGIvgtbydor3VWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c9COqWvliQ1tZnEB5IgwtuifC6WqjDsnxIAhnvmMFh0QJHy_SsnELk5HFaUNk8-NkRbucd6JX6gFTYP4VHLIFFhuwPTf0zl07pfDpK3y_Hq3UKEU2lTfkYcQoye6ZahgG02Tn97faPzLuB59EJwAi-YmorV9jja0PosLX4zxpGVA-_G821QrLIzgjmwloXx4YCOOXCHr7l0o4b8YDqH4Lmo-Q5dgLbNVkcUWMl5mJuHJFDt5HZWUUfCdkR2LEk--xhf-tCioqTRy3hD41qXXJkRE8Z2Oje67c4I5ZLMJQY8gkc6kG64Mi31OPDxYbNp6NhxLOMYOdZcRlSn1YCrl1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی نیروی دریایی ایالات متحده به دریانوردان و خلبانان هشدار داده است که سنتکام عملیات نظامی در تنگه هرمز، شمال شبه‌جزیره مسندم عمان که در وسط تنگه قرار دارد، انجام خواهد داد.
طبق هشدار USNAVCENT به دریانوردان توصیه کرده است که هنگام عبور از تنگه هرمز با ایالات متحده همکاری کنند. همچنین USNAVCENT اعلام کرده است که هر شناوری که در فعالیت‌های مین‌گذاری شرکت کند یا از آن حمایت کند، هدف ایالات متحده قرار خواهد گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/76305" target="_blank">📅 09:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76304">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromInfected</strong></div>
<div class="tg-text">سلام فربد جان ساعت 00:23 است از خونه همسایه بغلی صدا آهو ناله میاد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76304" target="_blank">📅 00:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76303">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سلام فرید جان امشب نزدیک میناب ۵ تا صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76303" target="_blank">📅 00:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76302">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حوصلمون سر رفت بیاید فینال فردا رو پیشبینی کنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76302" target="_blank">📅 00:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76301">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVuaqMbyNwOmPIo7rMeTFYK5SfIeJduRIL2Nfp58sE8X0i7aRO35zDHhT1QLbcUtbWMImfbV_H8nwoVUZRaCkzgCx5q7CPqZe7BNlYfjSyUSf5FN70xLPx4jqVntJs58Q3UdCmGFaqczU_B7aBtA9NkpLdb7m4qM10b8DR1rgmX_snKErmBjxW4p3nv_M1RHHsodo-7er-8xeonmWcmuSMVwZNHMREbh52VnxDLMRZZ6idHo35yJdzzUbfTg1wJpek4SHRGy41Y22yw1XFdejqohlq0HdAxVkHIzYkKsENFpeK1KycM9J5QPrbcfCpvH1wW6dilLoBTCVRcyHZD4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا 1411 با پزشکیان
✌🏻
@FunHiphop
| ALI</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76301" target="_blank">📅 23:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLLMwdOp622uO9kopY8oPWYEZQe_gYe2uN9acHDoyZbuFnXi9KZSiuKvUepgwtAIFot0EREl6UKWsUqErxLpaH4VEjWABcCF30NyXG4l2zEnyqQQICgUQyGzF9nXBxWt13ifB6KYUh62UuWfhWIY2_6XegTy9N5E2FYmNZvK8F6kc7lKJ86OrU3gdlboBuMw5pwbdGGhDdkzNDhqcWThyqqzu6r5DKpAulrKklwB-CGxVwMc6yaEA_hQYe5j3Jp9VeSASZyGpYOVtHClrhe1E9_dShOLraZohDoJsA-Gp47dMEnWrUU9fYQQGnTVWGdH0pFcADEH5xEr_83YciVI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکش شبیه شوالیه هاس</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76300" target="_blank">📅 23:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNoah</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUKRd5FDHuMqAhlRTKLFyFpDPfBhauzhEbVd8nRsKupABP7qMI4-GOeCT7MS60VMsWpVEek6b6vYCEJ4WGdCFRWyjzXsiCVm8EuHpZdSx_UvLKraXSC4rbi93_2mO-1aKHWPQQW98cr48jY7st8S2C33mc26GNoHXXCevWckzONNEj2-qYT4PAU6AL_XTgRceemy5XEfpuJskbA1DmVbZd_BerlBNu1ONFp0Ok3awXCu6ZKddRyZo45AZcTV4DTyREWuH9E_PNS6MntIwgL1pXk_Uh89242VbX7vwOi8Bed9OKy-78slJeyyF1Hewq5Yu269xJEPjjjnFBUcU-QfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس قدیمی گوردون با لیونل مسی
یادش بخیر</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76299" target="_blank">📅 23:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">از گوردون پرسیدن تو که انگلیسی هستی چطوری اسپانیایی بلدی، گفته چون از بچگی میخواستم بیام بارسا یاد گرفتم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76298" target="_blank">📅 23:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پست جدید کاخ سفید: اونا بین ما راه میرن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76297" target="_blank">📅 22:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95e3a0cee.mp4?token=rLd67zUyUthFgA5td6spwk_U2ndgqrADy1BVVTl3SLQuhd8eKUuj3_yUMmgYaNoQg1HxWPYFN5Yk7X9qdIMNTfFWpm45Ijd7i9c4wDJke55epRZN0PG8msT6lmELhJHfTZ8RmYu1a0dpDbNXJ3Qi6umuvcdoLq3MVCS9b_O24QCl1I7p1s1NjF3RLslM5rh1Z2edHixh85gxfJ4JQ7W3rAQNdCla88CQ8TnM9Qw4W8mU0v4i5MsdtDh2QUoDignS6Kqa_f-0T6ciaQDKmr_r05yhhGb0ydrtZUCqNXIch2zZ5camEdSMuPrIflKKzgCgS7O-uA9sX9GYAntv49z76w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95e3a0cee.mp4?token=rLd67zUyUthFgA5td6spwk_U2ndgqrADy1BVVTl3SLQuhd8eKUuj3_yUMmgYaNoQg1HxWPYFN5Yk7X9qdIMNTfFWpm45Ijd7i9c4wDJke55epRZN0PG8msT6lmELhJHfTZ8RmYu1a0dpDbNXJ3Qi6umuvcdoLq3MVCS9b_O24QCl1I7p1s1NjF3RLslM5rh1Z2edHixh85gxfJ4JQ7W3rAQNdCla88CQ8TnM9Qw4W8mU0v4i5MsdtDh2QUoDignS6Kqa_f-0T6ciaQDKmr_r05yhhGb0ydrtZUCqNXIch2zZ5camEdSMuPrIflKKzgCgS7O-uA9sX9GYAntv49z76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید کاخ سفید
:
اونا بین ما راه میرن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76296" target="_blank">📅 22:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ تو پستش گفت تصمیم نهایی درمورد توافق و برداشتن محاصره رو تو جلسه امروز می‌گیرم.
الان نیویورک تایمز گزارش داد:
ترامپ حدود دو ساعت در اتاق وضعیت جلسه برگزار کرد اما هیچ تصمیمی درباره توافق با ایران نگرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76295" target="_blank">📅 22:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76294">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سلام وحید جان قشم ساعت ۲۱:۲۵ تاریخ جمعه ۸ خرداد پدافند فعال شد من در محدوده قلعه پرتغالی‌ها شهر قشمم و شلیک پدافند کاملا قابل دیدن و شنیدن بود  @FunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76294" target="_blank">📅 22:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158dd2ae98.mp4?token=gecGtB8Bg9I-iT3OBtUDSKuKXZXXaj2bGhmxj560Aqkf2exAnQG9sBfP-nof8ARByUTUE3UDi0D7DOEI8w_XzbEzwTFl1pKhAsxdNhcbG06fhda8ckFZgMjsVWkj_btuOB_xjc6v-jv5lzXIDnuN533Is8PtjxbRWXFejtWACKLcNpY0NC_GBprhB7TJJLcq-a3u4lwtkWtGnyS5boYhxQjRp3iW4Pun6XcWEfLtYnMfBO80sgVr6GWmdYtvzB1J9ILamkBbtTYV2QT_ZlODd7TW86zETFx_JZKS0Oomajm8TLIid8u3quCAXs9XshjlvgZHUdC_GsEp-V0l4cy4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158dd2ae98.mp4?token=gecGtB8Bg9I-iT3OBtUDSKuKXZXXaj2bGhmxj560Aqkf2exAnQG9sBfP-nof8ARByUTUE3UDi0D7DOEI8w_XzbEzwTFl1pKhAsxdNhcbG06fhda8ckFZgMjsVWkj_btuOB_xjc6v-jv5lzXIDnuN533Is8PtjxbRWXFejtWACKLcNpY0NC_GBprhB7TJJLcq-a3u4lwtkWtGnyS5boYhxQjRp3iW4Pun6XcWEfLtYnMfBO80sgVr6GWmdYtvzB1J9ILamkBbtTYV2QT_ZlODd7TW86zETFx_JZKS0Oomajm8TLIid8u3quCAXs9XshjlvgZHUdC_GsEp-V0l4cy4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشم
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76293" target="_blank">📅 21:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سلام وحید جان
قشم ساعت ۲۱:۲۵ تاریخ جمعه ۸ خرداد
پدافند فعال شد من در محدوده قلعه پرتغالی‌ها شهر قشمم و شلیک پدافند کاملا قابل دیدن و شنیدن بود
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76292" target="_blank">📅 21:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76291">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اگه نمیاید بگید باغ و بیم و فدایی پست کنیم اینو  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76291" target="_blank">📅 21:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xr9pAsucseWooCcSwnDoywvuGAGghB5UBl5ZvU3iOQYxOIKP8L0bgewVqxCs2CG8tFIW9uVAPYcrzz9YD65V4sE4bkfYrFNbv05qVXf_NlUk8I57yfiwCQz4JAduE7ZIGlv-OMK0MBVOlWhmWeGQDmgWQJHpTT-H2LHEiOBmaKsjvQ2DcImKhffC1PzCJlO5FK4Ieo3qMt30uqmt7sqUoy2CCGBmWKGiWASLBieXwhtpmNpnGlb1qdangSks4ZSUaX2eIrKv8reBVpQvRpD27ti7H77Kpy2_Alx0pfL9sX7Ch001FrOPpGYd0bYLAvg5Wa73UHh8LrA3LEBg2MEcXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نمیاید بگید باغ و بیم و فدایی پست کنیم اینو
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76290" target="_blank">📅 21:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هیشکی خایه نداره موزیکای اصلیشو بندازه بالا، همه دارن هرچی موزیک کصشر که رو دستشون مونده رو میدن بیرون مارکت زنده شه بعد شروع کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76289" target="_blank">📅 21:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76286">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تا حالا شده در پی پیدا کردن یه پورن استار خوب ساعت‌ها سایت های فیلم سوپرو جابجا کنی و اینترنتتو بگا بدی؟ یه چنل داشته باش که اطلاعاتتو در زمینه پورن‌استار ها ببره بالا تا بتونی یه جق باکیفیت بزنی :)))
👇🏻
•
@PornHubCom</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76286" target="_blank">📅 21:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سلام بیدارید؟</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76285" target="_blank">📅 21:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpFL1a19OZiIprDwz6D2P4mzhHX5twNheXZ7-IRNkb5ScRK59RBujeEy8THpkfpLe6gOhMzU5aCwZfEgmuWCrrqeBGDFC4FAhbrJ7Tw_VcgT9l-Rjx-7v_k3CTPhoxOOZW7ONr6UujmJTlBh76lr7GoHc85PJyzWyzw2GCR6sCe-UE000UvSrtmSsmAOFi8NhBmSZxpAJVA-r_78M3peUEAKtCziYUNtADBqOcQDIRgIXZUux-23g2TYiBfTwfGQnmM1EFrz-5bwmQkDD_ex9C1SSZptQM1d8jppYkIkxQUi0WjWRTJtdHT5IgWgEqIxSOlG8TxK436IIIDZ07_Dvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشن خنده دار
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76284" target="_blank">📅 20:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تیم ملی جمهوری اسلامی از تیم قدرتمند گامبیا گل خورده   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76282" target="_blank">📅 20:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرگزاری مهر به نقل از یک منبع بسیار دقیق و بلند پایه درمورد پست ترامپ:
هنوز اختلافاتی در مذاکرات وجود دارد و ترامپ آرزوهای خود را بیان کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76281" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76280">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تیم ملی جمهوری اسلامی از تیم قدرتمند گامبیا گل خورده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76280" target="_blank">📅 19:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76277">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tcNZnY3VV6D4fcNe2gMo-nJaejJK6fIJyMucsW4cCGlrUsPEHAxIKhExB0oGEuJtvMqtpi7iGo7eSDQVp1IYtBS7yk2EUSGDs_EJ7CKjqRLHBQYlMRo8ZW9y2iRYm7Muw_FQ2_szHNoRFkdrvi_9LMiAS541q9OSYJTpboMoh1blEWpN-mt7q3y5lvCYbOW_PMsnMKz_fZ9UYr-8uD73dNYmWWawkzB3FlDJyJzvMNl83rbhxrERvM6-tvcJFSt3qz0oh_Y9K7A_0hAeKoFA0PAnxE281YypAExpqRYu5pza907QPyJldNjCxnJKx-FY-J5qiTXEl4Bd3Fe9hPF5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfKX8ENdybU3TL0YSrMkWZXpXlZmQHWh256IEk529RE2P_lXz3kESBpfWvnQDYMRJ67itvyTd6texYEmHw3IDfeIZ9D2Q7ZvxI6WU6vouQToq0iKeytAhLhLqF41AUU1uDTZu8j8xXQXainGxUHyIsTrndrNLvhnHNRPH1_ewJ92LPdk2gL-38finc3bC99uUzeTR-IoQd0fsxbD-qmRrlVNpewhHsSgy7Fa3KOCy7Vm2-rHIf6KzFAvV3dLDb39mWYHJPIo6dgJ4l55wrVf-zQQFkktZip8DcOCnv9eB2Ku-BETULRC4xx080RNxgt_RsSbIjfdyr1JVuVukPAx3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه اتلتیکو مادرید : بفرمایید! ما همین الان ایمیل پیشنهاد انتقال‌مون رو برای بارسلونا فرستادیم :  4 تا بلیت کنسرت بد بانی برای فردا اشتراک یک‌ساله روزنامه ABC 1 بسته تخمه! الان هم با اشتیاق منتظر جواب بارسا هستیم تا ویدیوی معارفه انتقال رو آماده کنیم. …</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76277" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76276">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH89Hu9dzRL7Y3puCHEd41qwgcENMqpNQGJ8NoEKV-9xETgJW1MO3QGTtNQAfLAadX1LVAh3ZpyvBSMGnJ-kLdpvupmaDZUJQARS6HG5DVPGryvhGdztX8IPA47haI1KGABh741-ftYD9SkDkwI4iBIb6W5e-CWNJQFsvQo5EydfdY9-PBxcY4hESyU3fS4KkCxJRx3OqC_OgPJFVl5vJ_O48uQbvGdbqO9qG6KFAd3Yni9CETYtJOBNz03JWiJFchDsbqeUeqHcboO6mZAFHAKKSNFVnZX1yDx7xbkNGmjArnG12mZ4Wa3pw6itnly0H6NzF2hW0qwthmHlvtuIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه اتلتیکو مادرید :
بفرمایید! ما همین الان ایمیل پیشنهاد انتقال‌مون رو برای بارسلونا فرستادیم :
4 تا بلیت کنسرت بد بانی برای فردا
اشتراک یک‌ساله روزنامه ABC
1 بسته تخمه!
الان هم با اشتیاق منتظر جواب بارسا هستیم تا ویدیوی معارفه انتقال رو آماده کنیم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76276" target="_blank">📅 19:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76275">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">غیر منتظرانه ترین اتفاق ممکنننن
فارس و تسنیم:
منابع آگاه جدیدترین ادعاهای ترامپ را رد کردند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76275" target="_blank">📅 19:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76274">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حرفای مانوک خدابخشیان رو گوش کردید؟</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76274" target="_blank">📅 18:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76273">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حیف از خون هایی که ریخته شد و خانواده هایی که تا آخر عمرشون باید با این داغ بزرگ زندگی کنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76273" target="_blank">📅 18:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کل هدف ترامپ کبریت بی خطر کردن جمهوری اسلامی بود که به هدفش رسید و تموم شد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76271" target="_blank">📅 18:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: توافق انجام شده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76270" target="_blank">📅 18:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ:
محاصره دریایی ایران از همین حالا برداشته خواهد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76269" target="_blank">📅 18:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76268">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: با همکاری چین و امارات اورانیوم های ایرانو منهدم میکنیم و هیچ پولی هم بهشون نمیدم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76268" target="_blank">📅 18:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76267">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رسایی با اینکاراش میخاد بگه من طرف حکومت نیستم درحالی که نمیدونه روزای آخر عمرش رو داره سپری میکنه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76267" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76265">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خوش چشم، کارشناس ارشد صدا و سیما: ایندفعه دیگه جنگی نمیشه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76265" target="_blank">📅 18:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76264">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2qbCVsvl0ZA_BXxUmhyAeDsqcAhCahrM6-0OwYvw9qLUnvr952Bv66iEtTPRWC1LrQtMQp3wWyGXqCwk_m4Sqki-SbU2ZWBGM7vAe-BZy08JyGJjjHZahVrAWvTwf0b2z1d22vSIoR0zc0PZLOHJ1uCzoysEi7jFOcprZw2QPkQUc_GUF7u3HbYtDc_bKAJz9yqjTICmopTjVI0I3gE90Jwk4pmQKf8U7zYWu6-KSB8_DoQWVBqtZ7MZHXOOF-slhGmzmhcn3D_p_dTdLhMFtExjv_o-Sob6xxujHjHGAwXM25ehMYqedeJV0bjyp1ky3SDvoardqAGpl9EGNLj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی مواد میزد تو وحشی واقعی بود پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76264" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76263">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1Xe6ImMXv3u_cIlREnD8WMN5X5WYwb_ApwwnhZAslOzPo5DPzsmvXXN9E1VaybkbOm_vKxX-kRlg1PQpAy_M9sTh_pWzcZPCD6qElozorZ-mFgNPtWYz16LF0ybyZadNlEy_oe31b00aiQuKk4qkXCxibFoOWBMcSEdFxrSX1JxcoDzmcT2MNprNqHBwj_vsshLL4lMxUgngfXI2riaHA1P8a3r-oJVPHZlgkv9fJEozDVusvt6kXYo9frS2F7kz1ZfH4xzG0h2sY4YeJDFlWnTGN723BiJVetPS5slI4o5E7s5xXGVee0i3UMkchxS9Ljs3iMRlZouzChTLuDd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g8
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76263" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76261">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">به شخصه حاضرم ۵ بار ترک تیجی و ۳ دقیقه از ترک باغ یاس رو گوش بدم ولی ترک پیشرو رو پلی نکنم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76261" target="_blank">📅 17:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76260">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عمان هم باید مثل همه رفتار کند و اینکار را نکند، وگرنه مجبوریم آن‌ها را منفجر کنیم.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76260" target="_blank">📅 17:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76259">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یجور میگید برگردیم بله انگار من از اول بله رفتم که برگردم
جمع نبندید بابا</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76259" target="_blank">📅 17:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76256">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">واقعا تلگرام ریده، میبندی بازش میکنی ۲۰ تا پیوی میپره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76256" target="_blank">📅 17:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76255">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینارو خودش لیک کرد که کسی لیک نکنه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76255" target="_blank">📅 17:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76254">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قبلیو نمی‌فهمیدم چی میگه اینو میفهمم چی میگه و کصشره</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76254" target="_blank">📅 16:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76253">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وایستید یکی دیگه انداخت بالا</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76253" target="_blank">📅 16:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76252">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">Demo
Amin Tijay _ Members Only
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76252" target="_blank">📅 16:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یکی تیجیو نجات بده</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76249" target="_blank">📅 16:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">محسن رضایی: محاصره آمریکا رو می‌شکنیم؛ حالا چه با جنگ و چه با مذاکره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76248" target="_blank">📅 16:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزیر امور خارجه عمان: امروز با معاون رئیس‌جمهور جی‌دی ونس دیدار کردم و جزئیات مذاکرات جاری بین ایالات متحده و ایران و پیشرفت‌های حاصل شده تاکنون را به اشتراک گذاشتم. از مشارکت آن‌ها سپاسگزارم و منتظر پیشرفت‌های بیشتر و قاطع در روزهای آینده هستم. صلح در دسترس…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76247" target="_blank">📅 16:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shT6-YE19RUAmV8i5qNsIFDdst5QaxqCzKY--8GUfD33rGKv5TjryJ0qXphTIa52KfzqQts1WFUJZMWHBaoLNmWqGYs9wBJlObtqMng1RD2DOSkbRlunFZKv1MBj3nIrzGpzC6hE1P4ohXWFe98JrxvfP12SKiipvSBdvSWdv6nILNvqMll9SSofwsIRT6wkHhGeS_hfZN-LkcJ3wc5H9K3xyxcs6XWtVDjRrWK2Y6Fn7k56tngxJchzvbeA8V27LQfRvSEw9P7ONzSINqZnKIUTG_iLEqgJM_VLPbI_U5DlhO90u9RBmgmaz2M4BSaFC1t3A4REj_U8ePdnSrFOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه کاملا آماده مذاکره و امتیاز دادنه:
۱-ما امتیازات را نه با گفت وگو، بلکه با موشک‌‌ها می‌گیریم، در مذاکره فقط آن‌ها را تفهیم می‌کنیم.
۲-اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است. هیچ اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد.
۳-پیروز هر توافقی کسی است که از فردای آن، بهتر برای جنگ آماده شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76246" target="_blank">📅 16:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟ هوش مصنوعی میگه برمیگرده  @funhiphop | reza</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76245" target="_blank">📅 16:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟ هوش مصنوعی میگه برمیگرده  @funhiphop | reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76244" target="_blank">📅 16:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟
هوش مصنوعی میگه برمیگرده
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76243" target="_blank">📅 16:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بارسا هر خریدی که میکنه فناش فرمین و اولمو رو میندازن نیمکت، تهشم این دوتا از همشون بیشتر بازی میکنن</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76241" target="_blank">📅 15:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گرمه خوارکصده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76240" target="_blank">📅 15:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUbYqkkGOW6v-fQN0i-yLgn_z1SEcgxOejnRhrKb8W1an8gzUsKyHxlZkIYStf33L9c6L6mZ8CU-_sjo3gtJgNnKSZfI4RSQpFqKrhcUR_0Rql34-IufdwATBI8V_fnGuB2jcDQhKDTp_EH7J0z2oBM9TxgJVHq6Lwq6QBfI-52autrnZjOkkPMIpg5pEZj-h6Qdw4TRZ7SEoqS4tkwGESIhpoLL6k0paKpe_0rqnw_55xuKQaKObOjW8nIBRHfvt2YGBlgiCSs5tf98O1Waid0Hnux7kOapmXd9iedfr1nSPEc4xzcWYSVHm2vdNvQR8kY2p_y0QLU5PNb3msBosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده: مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم جدیدی در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده. شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76239" target="_blank">📅 14:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده: مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم جدیدی در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده. شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76238" target="_blank">📅 14:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده:
مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم
جدیدی
در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده.
شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق سرمایه‌گذاری پیشنهادی برای ایران است - که طبق گزارش‌ها حجمی معادل ۳۰۰ میلیارد دلار آمریکا دارد.
ایران در ابتدا این را به عنوان غرامت خسارات جنگ (که بین ۳۰۰ میلیارد تا ۱ تریلیون دلار آمریکا برآورد می‌شود) طبقه‌بندی کرد. طرف آمریکایی آن را به عنوان «صندوق سرمایه‌گذاری» بین‌المللی که به تسهیل آن کمک خواهد کرد، بازنامی کرده است - چارچوبی نرم‌تر که از کلمه غرامت اجتناب می‌کند.
به نظر می‌رسد این ایده از سوی استیو ویتکوف و جرد کوشنر مطرح شده است، کسانی که پیشنهاد دادند پروژه‌های املاک در تهران و مکانیزم سرمایه‌گذاری گسترده‌تر به عنوان مشوق‌هایی برای این معامله تقویت شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76237" target="_blank">📅 14:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مدیران اتلتیکو:
خولیان نخواهد رفت
مذاکره نخواهیم کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76236" target="_blank">📅 14:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ناتو: روسیه شب گذشته یه ساختمون تو رومانی رو هدف حمله قرار داده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76235" target="_blank">📅 13:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آه رسایی اینترنت و گرفته
هر لحظه داره ضعیف تر میشه
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76234" target="_blank">📅 13:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رسایی آقا مجتبی رو به پسر نوح تشبیه کرد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/76233" target="_blank">📅 12:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKgnfPk4KKbxkywq35zgHahP-42uykO-MJaMucgpe6JIpKZMYH35g00NB4h4IGl7Cr5dUrRAr03nGfd9gF861KKcdhmh9BKlCwPCVnMXJcmFkW1qQXOYSfk45MwsN878AbjFi2o6Fs3Sh7hlgfEwZ00okzPXn2gLiZVmkHZMKqWv0drIxbfNw2m2wwqO7KYSf5qDWrlx4M727IWJILnDCY9MX5RbcHfjnps9vcDtLl5mlAoVYcEH8Wu93-8R0lMVf7DOpdlJw6fPrFkCK03wTaNxpy09RbyM_6w5YDvggV_OWSHCQx2QUEzO6ffhOPgNhasq1D1mOjfKJCXOwQhTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی آقا مجتبی رو به پسر نوح تشبیه کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/76228" target="_blank">📅 11:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8334aba596.mp4?token=Mdo9fx1cEjIRIP5En4qJDmiQBy1kg-0tc5WxirVUk7cj8r_CY6JNSqIZ5uhE80AeFv5DiqKuMB-SUqbxDhCxqhaaMDfMt8DqZDf_YZTFmUmMCbdDeT7acbInqZmaeHgwSA4M5pu_hraTr40CexL1ZGYEbdPUZucTbZhxcIeLsTl5z2UudYwL2fw-YqKW4DgYChE_sfhBi87BAZtTADWt48xz7LVG3t47hg-iCNxqfgTBehrToBIwWguAlLKrObGxUSrib-xKjUZLhJ7YgBSppw5Ud5oVF4ksHgbkAICJP-LJgNQFdLKsq4BDuK-KxqYKGaBW9pvdb9gwc_pE7_GYww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8334aba596.mp4?token=Mdo9fx1cEjIRIP5En4qJDmiQBy1kg-0tc5WxirVUk7cj8r_CY6JNSqIZ5uhE80AeFv5DiqKuMB-SUqbxDhCxqhaaMDfMt8DqZDf_YZTFmUmMCbdDeT7acbInqZmaeHgwSA4M5pu_hraTr40CexL1ZGYEbdPUZucTbZhxcIeLsTl5z2UudYwL2fw-YqKW4DgYChE_sfhBi87BAZtTADWt48xz7LVG3t47hg-iCNxqfgTBehrToBIwWguAlLKrObGxUSrib-xKjUZLhJ7YgBSppw5Ud5oVF4ksHgbkAICJP-LJgNQFdLKsq4BDuK-KxqYKGaBW9pvdb9gwc_pE7_GYww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب ایران ۱۲ شب به بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76227" target="_blank">📅 11:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">چرا وقتی اینترنت وصل شد انگار قطع شدیم؟
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76226" target="_blank">📅 11:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4MXO3HzJcvoJS09dFWvTimvaGLXlpELjLO0E08X-Lm3CM-jwOzTrywuoRfz_rOY-Bv33xVXHtztsbRa7ke0PiT1jFMC-XerwaiHp_iB22z4JVJWX4jQK9sJer1eQxX9O_MTGccKWyKs1TianDRyEFhauG5X5L7Q6sFVzqZiVmbQSwrDFBUTBD2eZdkH7JIQndmHVnooR5kvnRQOm8ss32JftKAB_Ry2zgTRot6QrxHpmTs8RmBB7DYxqAC3u7W93SBbgce3bqpmUKg1H9TNHdpLHWE5YfkeOOxXIkdR_dULYUk0OVb83q2ZU5lJV591HJ34aek-8ow4r1q-wonU0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت کتاب پاور آف نگوشییشن، امروز به دلیل تخفیف، ۵ درصد افت قیمت و تجربه کرد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76225" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76224">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک جنگ آمریکا و رژیم اسرائیل علیه ایران را تجاوزکارانه خواند و اون رو بشدت محکوم کرد، او تاکید کرد آمریکا هرچه سریعتر باید از این جنگ خارج بشه  @funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76224" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76223">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_9xnnEwlTqLNGWJv9GXMESLHeJzQFCCM391SCX76kjz85gpgrgEqCYiuKP4tiwnCvR3YKFWioDajm62Ep5hI_8m_P15KZuhlF2BSYjQbXd1WzgLs22-7lpMb-FKfT3dnu26B7uERJ3DerHHIgsit3_bMxOBCjAXS0-Nz-ONJERfmIZahqrnvlA__NmrViFifY2V3-dDg2BMEfX4cdek2gjnyRP4aJlT0HfoBY0J6FiUMUc7k6OZq_UkRn0GPoJJ27avxC1uah_-oHGY9us3WpnWlrnWdBTpoziWMpZRcC6tS6uGVEPKcxkL7Q6slqamcuS7K61RPAzfTl1G36vp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک جنگ آمریکا و رژیم اسرائیل علیه ایران را تجاوزکارانه خواند و اون رو بشدت محکوم کرد، او تاکید کرد آمریکا هرچه سریعتر باید از این جنگ خارج بشه
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76223" target="_blank">📅 10:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76222">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeVW9JSSvuFlnnO5uW-N785ew9kmiz61OHx_Ev2SEksfslr6R2OQlV4SqvXtcScEqMFOCo12Jxpyu5l5QiLoirMZHI9mYVS7R31c7tq0suuzxMYgSHSbFqSDJR08h1fwp5u3dAUDFKWmmJbhSqatt7QsbGXcxObtSI3b9Zr0zZmfH4Tsk-LYoMfrbJrMeom1AbDBCB_bB5lZWYUABrS-L7XPhU2-NOXTnc2QXPFVDav3C_Bwa33b3jRW3wOs_D3dVlL9PZJw9enfEByHK8-RHJ3n9WTRdIDwlHil4D8oNDgPU3gtbJP9vBCloZssQne41BYcU_gcuSfIAIFABVqcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا افتاده دنبال گواردیول میخواد باهاش قراداد ببنده.
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76222" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76221">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76221" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76220">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKPoyUwteOBAqfsyUdvyOPnEgP7J3_FaJbMQ4LZBajHuw97GqrjY9qgz4kYAOl7TnT3_iOQxNo2fQQCRWhyPxcHLRtfNluUbFaLAuhVpPVi2tlkE017SB29wb9ABfaRXbRVboDx1nQ0IZLc3SZyfgYs5tXz2-rgXAc7kC2xrK7fU3x_LT2TWLLQo4C5Nmxroy44CYc-kk9rl5Rq5FK6-8ywqFQRRS2JN24px2A9HQP-tDX0Gf7fDJsjl3aYI7znGN-lRY9RtTXFqFNNmv7ko4OteWNpt49oqbK3VKcmT5RsiR1iyheVW4nOouQ9S7EnWuUh9Bzep7leOYr921A69pA.jpg" alt="photo" loading="lazy"/></div>
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
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r8
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76220" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76219">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سی‌ان‌ان:
حداقل 50 تونل دسترسی به شهرهای موشکی در ایران پس از حملات اسرائیل که آنها را مسدود کرده بود، پاکسازی و تعمیر شدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76219" target="_blank">📅 09:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76218">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبرگزاری مهر: هنوز مطمئن نیستیما ولی فکر می‌کنیم یه پهپاد MQ9 دیگه از آمریکا رو امشب نابود کردیم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/76218" target="_blank">📅 02:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76216">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دکی واقن دکتره؟</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/76216" target="_blank">📅 01:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76215">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اینم گذاشت چنلش گفت بگم اینایی که باهاشون عکس گرفتی شغلشون چیه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/76215" target="_blank">📅 01:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">۹۰ روز از تـرور سید علی خامنه ای توسط اسرائیل و آمریکا گذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/76214" target="_blank">📅 00:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امشب وحید جان خبر از چند انفجار مهیب و لانچ موشک تو جنوب کشور مخصوصا بندرعباس داد و تسنیم هم الان گفته به سمت ناوهای آمریکا و کشتی‌های تجاری‌ای می‌خواستن از تنگه رد شن چندتا موشک و پهپاد شلیک کردیم که خب چیز خاصی نیست خاورمیانه‌ست دیگه.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/76212" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=WWm95yaLfDs0nFDiJh_Qqy_dvBeX4qskTuBt_0yilwzK1Wj5QWyLzbTCDil9L_Vj6i-dykyz8VvfYQ-KxGL3J05F_kpfsoDCW51kLITGn9vBYpsLlJVP824WnCp3lblBLsNTs5Gpo1hThvDNmgkfNhD1MkNlzcoBSLWs8RbomgmoDEEK91iiFaY91kVIGVwD9Y6njbdVi6Q7pzGr7WgOufV1qP7SBivebsmZ4jQbYxT8ubU53InYMNcNUL82RQkLus0rYHSWOGMvGtuKkQzHdcZ_n2WOchoa7mjS7_6pVQxY8Lm_ExlSAjVwHUVhgJn7QErOX_LxTZ2ORmwJpBrJcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=WWm95yaLfDs0nFDiJh_Qqy_dvBeX4qskTuBt_0yilwzK1Wj5QWyLzbTCDil9L_Vj6i-dykyz8VvfYQ-KxGL3J05F_kpfsoDCW51kLITGn9vBYpsLlJVP824WnCp3lblBLsNTs5Gpo1hThvDNmgkfNhD1MkNlzcoBSLWs8RbomgmoDEEK91iiFaY91kVIGVwD9Y6njbdVi6Q7pzGr7WgOufV1qP7SBivebsmZ4jQbYxT8ubU53InYMNcNUL82RQkLus0rYHSWOGMvGtuKkQzHdcZ_n2WOchoa7mjS7_6pVQxY8Lm_ExlSAjVwHUVhgJn7QErOX_LxTZ2ORmwJpBrJcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هنوز مطمئن نیستیما ولی فکر می‌کنیم یه پهپاد MQ9 دیگه از آمریکا رو امشب نابود کردیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/76211" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">امشب وحید جان خبر از چند انفجار مهیب و لانچ موشک تو جنوب کشور مخصوصا بندرعباس داد و تسنیم هم الان گفته به سمت ناوهای آمریکا و کشتی‌های تجاری‌ای می‌خواستن از تنگه رد شن چندتا موشک و پهپاد شلیک کردیم که خب چیز خاصی نیست خاورمیانه‌ست دیگه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76207" target="_blank">📅 23:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1FbYcW67woeGgHGMx6pqpS3hRyNj6VVAgW0aH7YYAeJOVC1GmmEycfklFQkyBxGwklubE99WRmSceLZmHvnfhaYNaDAyKDACJQPC6bx3U49DB7ciNO_8_xHh829l23Jn4DoLeZlJwFDLxgnJXLkP-vdJnpDZbKi9PCCKQKZiFYJSpG8Nrv-bLG_l0_SVpa_ydBsd40eUHNJ3PuPv7r_AUUqMU6EcziuwrurpQ4qUGO1xaoBHj4bTxORQ-j1qsfK4CT2gtnpGXIpvZg6Ns4-2JIjo87bQEhz67OlPkhYlxuZg4eanaMvXR-xCRdfigmeShGR5jLrjIjCpaff9agjwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه داداش بخدا من خوشحالم از این که اینترنت برگشته و مردم میتونن وصل شن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76206" target="_blank">📅 23:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76205">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این گروهو زدیم که فقط میشه موزیک فرستاد
بیاید موزیکاتونو ول بدید و ی پلی لیست خفن درست کنیم
(فقط میشه موزیک فرستاد نمیشه پیام داد)
@Hiphopiplaylist</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76205" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76204">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نیمار:
حتی اگه جام جهانی رو از دست بدم خیالم راحته چون برزیل وینیسیوس رو داره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76204" target="_blank">📅 22:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76203">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK7lkFMMsnU77TwpIQj-VmKU0Y9PGOEjuNnzRe1JuHpQqZzOXAB3hBi9ZrbcWocpSEOFcIivyD4uQa-Z1Ys1tpV5q4moeu9mHiHP9_VCuMWeC9yV37fVEHRzGjk1jqNiVI0j1ilvpVit-dc8TqYr9uwjUWRE85RnnVVynM3wk-_7R_Bve2X3v4MYvYuiBAgPnfR9awm8pX8g1H8RNrEXISO9QtyXA2ZJtGbf0rUrJXhVN7BSNZoRXrAe8wdSw_fmM7exD9Hv3WivmTC9b5zBriu8lBbBOqMOpVSbAT_hBztveDN6lvaB7y5XSKSvgU4h7EKRDH6SGR9GRiHeoSdhtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی انقد کصخلید یه توییتی رو باور میکنید حتی بدون این که به تاریخش نگاه کنید یا ادا در میارید
یا واقعا با این شوخی کصشر خندتون میگیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76203" target="_blank">📅 22:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76202">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیمار تو تمرینات برزیل مصدوم شده و معلوم نیست به جام جهانی میرسه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76202" target="_blank">📅 22:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76201">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/76201" target="_blank">📅 21:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76200">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پرزیدنت پزشکیان:
ما مذاکرات را برای تحقیر و تسلیم انجام نمی‌دهیم، برای این انجام می‌دهیم که از اول هم گفته‌ایم که به دنبال داشتن سلاح هسته‌ای نیستیم.
ناآرامی‌ها در منطقه تقصیر اسرائیل است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/76200" target="_blank">📅 20:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرید رومانو:
برناردو سیلوا به بارسلونا
هیر وی گووووو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76198" target="_blank">📅 20:11 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
