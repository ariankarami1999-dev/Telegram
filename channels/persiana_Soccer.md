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
<img src="https://cdn4.telesco.pe/file/ONWm_RBiQtHKKk4qpirnmPYnSDcPFu7acWTLAJ-_JCScXByFAjIZZjfKsKSQuUAFsPhFObPTrGNIVvUVArI2ninB2Jr-CEj5ejdOCkpirJUwvTPo5TAb67guXSPSWh_-Hge2T2DQNkYAY2-pt-7alXRP0K4fgsaD-j_wS7yCYqeptJmfMh8ZlR0CaXJjgd2oWqx0tg16n-ZaH4ZnYOKegg2olLM4oQhzro4kRT_N4A0Rwkzh-rLJ-UTuFumakpUhe7Kk786Vb_4iu8xYrYF-aaGtlFwOBQe3cG6IxJNaCRbhR-Nso_ERh_P8eXLoOEX2Yxf8Z9ShZg-a0dG7E5k7Ig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 316K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 22:38:16</div>
<hr>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXPcsVlQMUqYJRBdlxDntJELEJTzPZkvF40w_HAiVft0AYN30UicK3JFODJByibLNC2WKNoCHeqNfc_50rjlDjYTLZjysENcOM0AHlu6mChvSSGJRaSXVuf8ZLBJI0xJkYcIUtcnd8mDwru5eHfNP7jlHE-KtK3kL9URxQ7QKSTHWqHvlkoMsvnZsq_AGpAM8MEwQQ1JkbDUi4-NBp1tsWosYS6-suFTtzkF7gRPbgvuLbbz6qij8fRQh1AndSbGB3RgmP5KrEluWUs2FG5DvU30vhjlE-htWCU-0IPg2kFV3OvaTAhkqXy4WH-s_N4hvqbafXaGsLNOMzAdJrDRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSQlAM9Eu17ycwtFMx0dFXWfnEOJJ79kuBzwiKmm3gzaAb8F0m9-rb35WeXZCSjJ2OE5P2quxfIUsJVRCFsLot2n5HraJ16KFizq5O9FixusfJ2GGL6NFlJDQZCBWFWVhsQ22vQZlf_fsNEDcSGsL9jVGNHC8qpIcChLTVa6HHIUSvEncWIsNP_twxQkWQUgiHj63Ge_tkmT19IisqiEbcUcMUnAjoNU0W7E9ym1fvf3mM3H2t8zZl-dQM7xXxScJFpRT7t1oKe9EcI6wkLmx-0wKu_wBHMaqasdD2X6VN9eV8Ge5M_td2mbCwzvUL0rOEwLzBif4Bs9U-jkU2deGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/24239" target="_blank">📅 22:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=rRbza2iQ5sQPIs8P-Xg87QOIFlCRkIojuJVN4GCzvZGjzBtVMTf443NwFFkaJMCZlUvmxILVnrN4AIIrzGlYOD1ITwkZ--aWiwqQFvrangygjIJRBF1Y6U96hZkWOM-UzVq08vVs-Czoxo80jHkkZqsAGwFzlgXYTxN5kH_f5Fo_n6oNVlwH6-1D-kkggAXK8cUH-LecLRZCCj7r8gGRr6KXY0JWg4es0mAb-O7sZ9KAmO4OBURMCUwKoLz8qo8IuS9QfZFxu-fhQvxMrmR4TurgnghzUMtmV8L8P4Zj-AJFtFjkAOOyHp7WTTmzBCOU-wJqPWUUGLAVLGrGaZJ7JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=rRbza2iQ5sQPIs8P-Xg87QOIFlCRkIojuJVN4GCzvZGjzBtVMTf443NwFFkaJMCZlUvmxILVnrN4AIIrzGlYOD1ITwkZ--aWiwqQFvrangygjIJRBF1Y6U96hZkWOM-UzVq08vVs-Czoxo80jHkkZqsAGwFzlgXYTxN5kH_f5Fo_n6oNVlwH6-1D-kkggAXK8cUH-LecLRZCCj7r8gGRr6KXY0JWg4es0mAb-O7sZ9KAmO4OBURMCUwKoLz8qo8IuS9QfZFxu-fhQvxMrmR4TurgnghzUMtmV8L8P4Zj-AJFtFjkAOOyHp7WTTmzBCOU-wJqPWUUGLAVLGrGaZJ7JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب که لامین یامال ستاره اسپانیایی باشگاه‌بارسا امروز داداش کوچیک ترش منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/persiana_Soccer/24238" target="_blank">📅 22:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP8LbxfzNgwrOUSuxHgI-oj7ItIPDvuElQWdDMI7sU5YSaYTa9Wk1UbhA3kgQyVbYS9I0TlTFlFvDQNTZXrcRKNoWTZOHfG8qwpQ6ELCRSzGmhs-17Smpgp2ciykIbTF7ly6gCaj675f3Un52KwxwcgYojEPNCrpqVff2aDrCbXqKTNm_sgEP27yCv8otrwp5ICkqFjWqdvW4r7nLIDHOvT-4AtMFLY0fHeFAj8vl_dUc6vG_mNBta_mJxIRgGmmeYDHY4tCG9qycS4ynBFneFhC49WQDkKlD7wB3W45GSN82loTrJIol_yCC53sxSvtzfj7OED0uHbnOa6NSpprYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/24237" target="_blank">📅 21:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tw3nROEmaPiYjvWZotSdH1pEUPy9qiBisDjVpwg4BtwMlMZfe0aNtALiOECjLJlMkc66evJ2UmC5hl1t0kPQNbX3HfF027io5VbHBPTJXxebQ3rz4Rzj80nDE7e9QVs54cndAxsJowHsi421eOZ9BD_8RzdW6p5uzesufXVzQOWiyA-EhirLPvv66asRaq-tzNFeBiNxtnGN9iVsIEOUQbn_ksNd8eCkfGhhJOH9YW7xDu0IHkONWyv_2tb9ldiMw31f35s9B7-JhdrjA8-8Zcpl9EAb29Qs-OokS8Wf0O3YyJIU18XBq1-GjTHjLgi6AaovEFq9oDW7p94EeAC5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌طارمی و سعیدالهویی، مربی تیم ایران به محض ورود به فرودگاه سیاتل آمریکا توسط پلیس بازداشت شده و هم‌اکنون در حال بازجویی هستند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/24236" target="_blank">📅 21:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLhKfDF-hLrpHkc0DsFPoGRmTw2-r2bt2Ku55cw3zmBqZlAdYNXuK7uuTALe8m4Zlv1kzbfRZWVn1GQxeYF57Q4YUpDkidb3ChAT1RzRkMvmHTE-_6gEytDLeYkRoXaakM-mXyTfb2R7tfIcBGXMV2da7LiZtWRqdcKSiGGT907JUxm5AyuYcjAmg7AculINwafP5QWD_Ot2EKaX9l_55Jv1J2TUr0EDljrbewQqO6ty1jfcqatEvEBGJz3vBN_7GY3bDK8Kf29d4WtkFOXIpR2GDbYzwIKfrj3u00AWTeRMdegxReTge5bwR857TyzXFDyG3nfe2tVvtVqv-euWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق‌ شنیده‌های‌رسانه‌ پرشیانا؛ مدیریت باشگاه استقلال ساعتی‌قبل به مدیربرنامه سید مجید حسینی اعلام‌کرده‌که درصورتیکه‌خودِ بازیکن رضایت نامه‌اش رو از کایسری‌اسپور بگیره و بازیکن آزاد بشه بااو قراردادی به مدت سه سال امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24235" target="_blank">📅 21:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuEvkyq826BJjrbpUtG_FDdx6p0-mvU_3Tg_CVwGdee6bvUbJk_Gkn_Nh95k4EPSkByrq2hGON8ev2FXQA19SZwxfK8lYJY1v-o0qlRkB-qlBDSKhnTucC2ZLZ8sg3RcfoXLc0fzhPH2wFVI5-F8KrONVkjfXoMnM1uR0h0i2Yn9d1IjtZT4IxuvOQoaSd5orp4aEY8w1h-pHLxCX6QVkZyYRKTMOn9nTwa_71nY3inNU-lolJbUemTPUaH9klA_xsMywKH4KWJhglJ1S_UUX3GjDn9eGz2f4Vr50_KxTmraUfH0CNZS1Rsj4wmxE0Gzgpfe5o_nhwdegAONLHskoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇵🇹
ژوزه مورینیو سرمربی جدید رئال مادرید:
رئال‌مادریدبهترین‌باشگاه‌دنیاست و بارسلونا هم بعد از باشگاه‌رئال‌مادرید یکی از بهترین باشگاه‌های دنیاست. درباره کریس رونالدو بارها گفته ام اگه از او متنفرید دوحالت بیشتر نداره یا او تیمتون رو به شدت تحقیر کرده یا از بازیکن مورد علاقه شما خیلی بهتره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/24233" target="_blank">📅 20:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roo-JRyO0F8lCahydBzk5JFeKXcOW6jex-I52oivVRZd3TtzUEJp3Tw23vRtKJYiAKRdPZ0dyiFqmANihFt3kBAWflOfVGA1d69uB_ewe_HUtu4zlfUCgg1kc9dn5V9WqTVodBBfVHiWhWVDmEFM5OP8Sqx_GVqS2YRtLqXELhfQEQmpUggQCWZWUatA8zdMhFQtRmjepYDek6IWICiQ5uWQlNpwQSPvjIbj5E0ayp1NwY1R8Mc8soJvzgvjsMCwZKjcCSvyeYHNOVyKugXK2EvwRvIyUOl8gIRnV5egYEmBN3Hg97bwiPHGNxMdUr-c7Vl_IISUrqQ5nNP_zTjweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قاب زیبا از دواسطوره تاریخ فوتبال؛ واقعا هر دو بشدت دوست‌داشتنی و محبوبن. حداقل تو کانال خودمون برای این‌دو و تموم هواداران شون به شدت احترام‌قائلیم و تموم امار و ارقام و ویدیوهاشون رو به‌یک اندازه پوشش میدیم که سوتفاهمی پیش نیاد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24232" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV97mUvuBGNDuhqrHCVFx3Q9USCv78RywBJvJGTxqfEaOUaSwIQigj6euHDe_kf5h3NgnM5qXeg3MJw1QGcZjxRQGD3VTqU-cgUd5EC1CGHCl2IqKJHf56RZUa4VxylJuCV5XcVqjO9BrNTyXQ-VAQ6DntGE37Uc9l09B1VTeITsFAZHHmeU0sg_oefj70WH0rjhZU0dWV1JnC2Lb3x6prgjLj81Xb9piBNUaBZY5EzVtofgKZ8OMzuO9etof0ZVsB02MFDDZy-YGjY-muQQPXyCJc3N7OPN-lHd1BEpD-5qzILS8vtq0Snm0fqtXOoXpWfPHqFPyuSOQsi3QWMtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌کامل‌دیدارهای هفته سوم رقابت های جام جهانی؛ عین برق و باد دو هفته گذشت. یه چشم بهم بزنیم میرسیم به بازی فینال و اتمام رقابت ها.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/24231" target="_blank">📅 19:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ab_dq4oCteske_wVVqmcV64T9zMxK485luf7aptUznfunATrz8Ig92on5lkywbiZLogtgU7wuqGOgDqafNOL3ba32sE3ExT-3iIgYGiZq1mTNuAjOrFX_d_4-Elt0gM8uDLOOWTlY99bLnTg4Wfy6oJDulFdye-qr9sxxjUWMIfCpagPVwkZXfkhi1q97fbz10hvMWUTGgqU26hnrfy88tEHKZT01v-yXXNg7EnHnJPDjHvC3wpAdy5N3IIzhFWu9m2mBcnk7bnoEG84xlqq0sU2foadWVUm4pFvwEDUrA9Ol5aQ6U7756c_kV1KbQgjSGKWvC01K5Sso4mtm8CiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24230" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkZW4EIAPGtMBAJdk60RAjxDsm5Knc57yhWEhh10EvH6BgVhKNpW7CZGk2KUFP4gRjafWdf3f2E0ODcKH10VM6Gk_EQ6y0hO5cdP49FCCt9ESzLOe8WW1t_opWSSRsPxIRekG-fNQjtHct84CjDsnkTWMyvtNutV9cnxXm7taLSRcpYscjzglRI026bRPdI0IhVdSJy6eTMUQ41uFmZ36bgPj9VOfnEAmcnwbxzO54QEzFdNojSNba3Pxwq_s6sOS0cqRYv8i40mgBzBLWOkXL4NQgE2wfoSh0bFmxVIZG94_6KTG7j2JNUh8XqOSu9F1LuDysURw7ilu3VEZOLdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/24229" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDws9Ln96Sj8HbuXvbEQQDKx1rHLtYVcgR_DkyoajcSiqTD7ZG4TD9jQKaTCt1zvIiM9EluBYUP20PIjWtvGlVQnwV1AmQhAtrQpuYqIyjiQ8bsnxfzwIk1L7VpjnmpyjhuQebL4W_qqodsj1WcB0kJIkhJlW3YyMnnttvnwlwUDXd_KSmY5UVN5BYC5kP8uHcnCce_G4LNkCfkK2LyU42_LSfNlDlJlY97Sn7ZkL_R5N4rk1XCMLyw6rDuK4FVUWPzYUOKzVFU0kkXoCup4fQSbBOxNnHI8IVzGnkYn6t91RXjWOkr97OueI5cWy36Otk4YHa0KcsKYogphHyiCvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/24228" target="_blank">📅 19:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9yso_zKFB_RI_aUW2k2rtA1Z5Nd7dkQJ_bgk48DNbnW8IbvOemmiWNBSI-RGlr6AF6SfObEdUoiRCpims7BNhUUYT4j2V-S_O0mX5sWI-ejPDur-hNatUZI5K7thQuM6QRnPmN2eLfwt0oH4l3vmHAluOdA_RdDMkQMXQJOs1nHYQOhoGrjVJgEFtdM8gSOkZfZDMlROGfjpbxy1TKwmVEg3xDFA-Jq6NcDeGgONNSPKVNHUMrpDt-3uJDVHgjHcy_zWxEQJMTbao7XG4H7e4YIezZBheLVL77Foak5Dynd85_Ntj3FyZu5JBHDWgf7YcZ0ETrJvqsBzJ-toN0x-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/24227" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38571967.mp4?token=k62wvJXr2VFACmC1Nc2KNvt7XraUxkPEYux5CLlw417ulD_WXYFvF-0eDUksntN0Hex8H3yx3v6oaPyTPIcb-fO0PUbShCEIB2V9NiF1DFfplxPTRBSrzxDc88cTM5Zqs8V5-yXlohSGzp7ipXeX3o3wh6kBSaB3VUAWMQk_MlN1gbgE-J9hj5O-826meScycP6jTvnw5AFSodueNkTm4Ary-ec-MwKgBLcLd2W26KEHZfvs8ASWp6L_qmLJVgEploBAYbqIdi2QoFs2qFVkAz_Bm4lZX88LgVM0maWsL8JG2WN0KWwaDEnf5j1Fw-UO2mLkMN-rXuMibo3Ok1Qmjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38571967.mp4?token=k62wvJXr2VFACmC1Nc2KNvt7XraUxkPEYux5CLlw417ulD_WXYFvF-0eDUksntN0Hex8H3yx3v6oaPyTPIcb-fO0PUbShCEIB2V9NiF1DFfplxPTRBSrzxDc88cTM5Zqs8V5-yXlohSGzp7ipXeX3o3wh6kBSaB3VUAWMQk_MlN1gbgE-J9hj5O-826meScycP6jTvnw5AFSodueNkTm4Ary-ec-MwKgBLcLd2W26KEHZfvs8ASWp6L_qmLJVgEploBAYbqIdi2QoFs2qFVkAz_Bm4lZX88LgVM0maWsL8JG2WN0KWwaDEnf5j1Fw-UO2mLkMN-rXuMibo3Ok1Qmjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۹ فکت‌شگفت‌انگیز ازکشور‌های‌جهانکه‌کمتر کسی میدونه؛
دوست داشتید تو کدوم کشور میبودید؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24226" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24225">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tCVLWRMK8GStN0BGfi7hbOq7TudBOuTDxrFkxaNVVoomFkx-B3JHe1nvaCDzcT1OnSJVN1fV5jT8YPA3lKHuZFAuWReh2iyCMyz4r45pIWuRsarQ951xUCwQDdccAE_FOxz6QJUh1KIV-RKLRfr4O15nzw8hzBacNW8BAL-TCdXXXRecQcwJeswWP5t46rhZfmITRmkfkON_YbkAkDDQWOgnKSWy02kF8Fq0XEGsPyC3k2I-PKmJoK5ZSzowwDeAgWs39alpLcRB0mWIqjFQzmK4P5DkiNPeIpN9vCZfvy_5PENh-_vBXJZIXL5Ouo9ugp7rkRpkEdVyiG4iTAwdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
جذابیت‌پیشبینی‌مسابقات‌جام‌جهانی را با بونوس های لنز بت تجربه کن
🔄
☄️
بونوس خوش آمدگویی
🔤
0️⃣
0️⃣
2️⃣
💯
بونوس روزانه ورزشی
🔣
0️⃣
0️⃣
1️⃣
💯
بونوس کازینو
🔤
0️⃣
0️⃣
1️⃣
🔒
کد هدیه چرخش رایگان بعد از اولین واریز
🎁
📣
بونوسهای‌باورنکردنی‌لویالتی امتیاز وفاداری برای کاربران فعال سایت
💱
کش بک هفتگی
🔤
0️⃣
3️⃣
💳
کارت به کارت آنلاین و تمامی ارزهای دیجیتال
💬
🪙
واریز و برداشت آنی جوایز 3
👛
📱
@
lenzbet_official
🌐
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/24225" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=i-mHdhIKqr-vZXrbRJfrhFoCTRA0cK0Pzua3LEQtH3y_6J4ofyPRgENRBG4HFrc_oRIN91bc52ccRn2SjEgckAOq-HDaCU_Qq7aFWbdVNG1Hx5EkUfTZ8gduupESj4Nh6IzcohKz26jnNTVfiWFGGVuM015XTa7zngTHqpix8tEVRME_FisnNCCm3fwHtef7JvWVHRqh5nPRXPtSmTKr5BMZWp-EDuogkOVNTLdA5BY57TdCr_JcdyLRZKWfnlTMvqwUuf600KneaNpBq_pMnC6RddymdvNpCEki66d7YRdadbpB0jg8lJFr5kDWJGJgWm5WV9vJold4g_OYo6fxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=i-mHdhIKqr-vZXrbRJfrhFoCTRA0cK0Pzua3LEQtH3y_6J4ofyPRgENRBG4HFrc_oRIN91bc52ccRn2SjEgckAOq-HDaCU_Qq7aFWbdVNG1Hx5EkUfTZ8gduupESj4Nh6IzcohKz26jnNTVfiWFGGVuM015XTa7zngTHqpix8tEVRME_FisnNCCm3fwHtef7JvWVHRqh5nPRXPtSmTKr5BMZWp-EDuogkOVNTLdA5BY57TdCr_JcdyLRZKWfnlTMvqwUuf600KneaNpBq_pMnC6RddymdvNpCEki66d7YRdadbpB0jg8lJFr5kDWJGJgWm5WV9vJold4g_OYo6fxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/24224" target="_blank">📅 18:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8GrtOrmmygCDvXfbFSknnmOjzHcmCo3piyQoo5D4l4gr1-ZZQ6owHGtKj5uSfywAnm18D3D_P-nF1t7rqESbOm6AToq_6tTD_vKbaZBbjEXzFD5Vmv7hpUziNJpGESI5-yykAGXtg2gGh5RTkPNNmyE3klVLiY7EL0lhAuJ0ga7Ih8zK_m6lOkJSKFvt99X7yssdtZMiYc9m48i0zi8nDM6tl8tuk68TU3TtHGW_N-llVuROJHiAM09F5L1J1s-yT1Vztw8kYi19KUgJWhk4rF20a5bCXxHsaKYr11_1cFQg-1KNhnb8D5bWaxaMeBol-wze3PjivZs1UAj9FGlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpj57wUDhukG5myY9N-7mFR6CI9M7r0pqypDGFArMTQDZ_f3wNGOCNS8tfs1KYSI40WjLSsZvNk0rYRdyIqcBfBhxI8xkKgr4WNbqEE8mjIFzq3pqbfR9wuo_9mENU19oOWJTU69u86oCLZ_XxiJRGUknNMzDaM3L6p8CPGGnzRo4FX20fdMDXM06SWwCB1nquiTYNzHwckmy7eH5zSZerJCGeR9c9Hu_o0WbKOvgVKEXMYBOyL5P9-SEhXd3ORNlQYRhlUMb9ZH3i7JrdWpUc6eXLKVjxRjvZDzLMF15PeGFBaU9i4GDAtO74nst5vkmuTOCXKge_EmaOL4MFjEqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/24222" target="_blank">📅 18:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoXiUonUqq7Tw5x7Qv4NHCJ5b9AvXv-G5y0t6snTZKxJp40Gw2fC9Yf2w6Wu_ldSbJsIcxyzhGznTXvEEd94RPVF3e6L3m_kVKNawF16pLJgZmkT8f-Nyh4bWapXP9BXxgk8mmnjkQspzDYk0tNdL0V4q1cdr42Q7yoEjjdgeV9A9uuFSXsmZFlYePi6NpC7QFFavY5ttvvlwnJO2J8_TRKhhVbhdmq7aBjzToliKoTGxD0wQiHUszDFb0TD2DRvg2utn55PZb5d2cWqYI-KtV5BOWDkaD-adAgQvmBqD1BD5DmfIULtUJcra5f4OzSACL1PH1Yn0vIW-jdDuSD2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
باشگاه چلسی: انزو فرناندز بارها اعلام کرده که قصد داره بعد از جام جهانی به رئال مارید بره. ما مشکلی برای این انتقال نداریم. با باشگاه رئال مادرید به توافق برسیم بند فسخ انزو رو فعال میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/24221" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbZpHEBQ8Lj4YNuGvBLWQda8JoOwjnigYObl4VPA7vZ76G9viBF467gAwFsXKfezTDGA_lzDYPFG77dcjcFHWV7Y0mM29tMN2Nd2Y0Rx3wuArSV7eBmcWBMCnbkvw_LjL4qMPMLNljes8_2kLhxBv2lLVy4Hm_xMKg-h7Jw9Jx6kopRnePXOCkT-rcckiY9fITQWnoGS8i_MXpXBOnKy2swl2jNi1DwvguAL8a99IsMgy65wp8BY6OK3ZffUR5YNdGLxO6qi2g6h7juOKBGWTSyzdesn4ZHspwcvlPFZhhLX14PTLaQpaDiFuaOJFe56RnU63iCw8HPDEfBfK3JGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24220" target="_blank">📅 17:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZAsBT8e8tKq7xca5aLd4R_k4YOU18nd4rusKnqHN3INSt9tZIqvksWkLKSIw47KUD8rg0r1LgymgmjBra-6Nx5mct8qyhOJqmV27atl8Yl2R_8-zQygLUl9SXwKnuXDEsOT9jDYjp3_jq_TyBn1TlKlwvcmjgQTOWQTLk--aU0LB-zZGTwy2OgnkHnMqiUQrvAlrTMh0djV1EaJu3n0omISefrsnI8DWuSxws3MWmBuM_2j1DQZJVn_-1G750axnb-84xbttWOb5Vpkyn7cYhnoxdm1EXmo9Q2rNTpsFgNYoOoIYjZvK615-csjHUEHjv2qRhkzrKUHqfV8KMubSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/24219" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0kWPW5LJKzNWzi0gjx0MitJQvu-dQ5DRPjKXJLnu0FZ3htpQlO8gYGODfe58Cs7q6Gz8aPpFxjMqo0VKXyLNLYfRdocG77zcZnR-wiIjKfXKSvTES_eoRq93bw57dQ8LORFGKtUt4jfo_lIlLET9zgJGZ8HwVVPwPcyDy4INY0Lc-6yJO8i_jRSmaO_WLk4OZqS_bixaBL6GUjWkPAajaa6wWUaDHt_FZI06G3cgeV-s_8Z-RfUc8n5ENG72_hSrUI4GGJfHJ5BIVAQVKmxtq1-m7peYNsM15Z6GcbHVJZxkbV1yxUwPHvpa861ySIsr22HDeI0Fr7bGYOwxUtM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
علیرضا فغانی اسطوره‌داوری‌فوتبال ایران به عنوان داور بازی جذاب کلمبیا و پرتغال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/24218" target="_blank">📅 17:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgCAQ-wPtJxCvjn1_lgeQWMr7i5tEV3iCENyORXAXR4ZRo4hldWltUa2iPV7Nh7EKcavYRdb2yKZOGNTW2bhGqgdhAEBCra7K8uwK4cBSUVdmTem1CXUbv5i8xPoYK2xPQUUYCyj4cCtWlNCYLRpjvmgUiT4iOpaBPpgfNjVPMTsI_6tkOpNk8UR19ARunP6eLBchposmQ1-QVkIj56nMcq0cFCmtKzqrDaQsVlboRmsRq1GdrSIHXtB5hOZrizyd5S1KGxbdzlQofELPd9FffcqmdDWdtv9Ebnqx2qXCMb42b8hC03aORW1hBynF6bDcJea2u6qtH1sDA7l3MGCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24217" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbI1WHaTqhYNt2Dm8bsuy_fBi_gx9G9vxCGirUbXTzzzDq_ozpSrfCw69VTMiNzy8MQHBeIvgvCzSg17nxQEeN5vUID5dGSYFLga5JPsJLDGKp3YY8ph8_i65z-OwEZ9z70yXrS26rtW6unBFfHxj6rX2S8vVIPvkiKkxqiHawlXdLtiqzXNhf1grPouuDolNs14JRCpWjBseUEwLq6NIQOFCBwK5QJYb0GFQggX9aO5TJgPVrnSoy3lYq7hTTEMA1_9NSngKny-BFB0J7kggVeqQpia14dlV7u_Kk6AEl9cbwredlLSDn9YZPyEflRyZnOQ731MD1UJXzaIyaeNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_FV4DWPlzNX5NY0K1OankD44Cr88eC6QsDlZEbtx0IVTFo5kpTNVV1OnuJa_Hb_JcmDPzXCjk9GqFxhFjdlB-AwPMysYmbsi8RKCDCahEB1s7dom84UJ0SIjUk3-IifYpLCI-upmM7redMDrBJWR3gjk-hS29fhhXjrneW3Z6eTLO8tMxYOpfk2jH1Znq3BeAT14UKQ97q0YvZjTBUjmT1r0VxGFbiV-OMurI0TWrCAUWe4bZ-Q9vVVxZEQg0iPJVy0zq1T4jPTCgUvjhZrMDDIwADxER_1c8otaTV90tpHFuGvN7mlVcwYVUGC6nxMGJktyQ4ZBrBPAiu8DpkTuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24215" target="_blank">📅 16:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79050b237.mp4?token=Rde3rlYL8mbxvrOX2hjWFnnvgcJ0ckcJ-F4YEhbtDYC3m-EWK2ZRsRS8R0qglV3pRHKZ-1mqfz_1z0-vGQcnSzerHdRHhVWD9GfwhI2PsLzTXZ-JhzUC6LjSRAnaI-5sxY4QBr0W7c9413-a6jGeX1d3Ljo6UP50c4-idhR9scbjmGIBAb6kT-_Bk6e-nW5q4ejwmfA0Hfu8aUj5Le1h8RoLappy6iHOJw5L0G5aeq-miEZPFtqxXwZh6A7gsiLaNf_PcVnpCJGB4ke9-MNSrYfa8RMqQRFzsfEAJwXYAPkz2KNaqWgxJ0AL8ZLh-z3OEHYSD2FK1k4TcYOlARuQ_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79050b237.mp4?token=Rde3rlYL8mbxvrOX2hjWFnnvgcJ0ckcJ-F4YEhbtDYC3m-EWK2ZRsRS8R0qglV3pRHKZ-1mqfz_1z0-vGQcnSzerHdRHhVWD9GfwhI2PsLzTXZ-JhzUC6LjSRAnaI-5sxY4QBr0W7c9413-a6jGeX1d3Ljo6UP50c4-idhR9scbjmGIBAb6kT-_Bk6e-nW5q4ejwmfA0Hfu8aUj5Le1h8RoLappy6iHOJw5L0G5aeq-miEZPFtqxXwZh6A7gsiLaNf_PcVnpCJGB4ke9-MNSrYfa8RMqQRFzsfEAJwXYAPkz2KNaqWgxJ0AL8ZLh-z3OEHYSD2FK1k4TcYOlARuQ_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی از تمرینات لیونل مسی 39 ساله
؛ نکته جالب ویدیواینه که تو هر بخش آقای رودریگو دی‌پائول فقط چند قدم با لئو فاصله داره.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/24214" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFXCZFagW1CX8tl2caZiJhgUQyx2tubYEauQvyVFrtmvyT32w7I5Z_CIX83nh3gN3yVQha1nnXy1575CcyOmtlcfYvJ1UyzuhLlh3CiY6IHYlpuuIFULz3N4BLW8LQ34Vump_6xUZi2DaCwzrMhv1cAJbdp-Cj-jMuUbhCA7igSdJOQiDn8zN5-K2Xdxg9IRfaF6SAlqrHpXX0bFs9Kiwv7eJG9HaFwDw19a45hYfWz3Q-tULUDoERIkeYAR_hHMaFa8AnlINBWk8Bteu2MOQzBuJ0aamt_xXubL6orx8nA_hiIPd_G9t6LNHcv8uz89d3hiWBS2W1vMbFvzBp9FEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/24213" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbk0q_hkmFCfA8IgnjreQYfK3BgXyaCwMF_aDqUC2-mLF4i6P3vcfpwL8lDDQOrGKiCesOs3iunfWSc0X0Uhh3tRRueW70X_Rkygf6J3mLI0SIUCbfCM_aQiHVS7uTVMk_dC4OAV1pQ6Wa9IKPWXRy89zSAy1VB1wR-fMQ0f5lGkNZcvDifePoYm-zisCoSJYSP5AiIW4OPL7PmoGhUxMivAzK3FQFIAn0AJtJxt7gqOS-gMOSkLwWJJ0SUoDf5sP2EwiBshZ5vWWvHS6bw_DJdphipB0LPTBYo6Y11qKovPd9qKebjYhfNxBEDO37zlOwqUknor1o51wCjiXb2QxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24212" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHU7uzk-fxyo5Vvgs3i8LxYllApVw-tYQ8jGt_G5tGLySlZb9FB73pX96Vyo-sqQ1wn_c28HKoDjXx9cQ752gHB4i0pUjyMaql3i7_s8TtPs_mmSs9vMKtepq0QsglpP3rpAdPn0ofpWVOmBzivOMr2QlOfxK9ys5LipWuaDm8tWLfUd0EIbNLQzOb4LKGZ1Qdn94v1VllCp_vDmjUrbBeS_lE4DMXl2SYNwVbkXI9d03kRnpln1FyXJOFI_uLerHMqLcbUxHkDIzycHliKwzqkSprdy7Ux9tNd9Q2s0cx7IeGeWsO-bWfuWj8k8PI_jA70GxfaiDlwEWC5MPlZIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی‌که‌تاالان بازیکناشون دوبار بهترین بازیکن زمین انتخاب شدند؛ از ایران رضاییان و علی بیرانوند نفری یک بار جایزه بهترین بازیکن زمین رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24211" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24210">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahQY7CBiioKzeqAtdep9Yp19ra2ZxWPKOa3uWs3WkfYBI5IdXjTUw3qZ1nZL6HF1PH2d79LJy3rorx8h9a7IDZJrmYWONw_7LoSYP_iQy01upNnczmlu9cMso4nmtwlKC4gfVsgScjT5KIiZZo2Oo3Hwoat69DLH_7DR0r03A5OKGAnglguOMC9muw4o9m2egDjIby7UWtV3jbGOVNCag-utj8U4RJSZz88awkFQCwi75jIbfzvL2xWwye1mP0gfjnPG4N6V7mj25AgU1meGpx6cYVcxBVZy8wh7dYHlvYlSF4_XZFRlZlOFG5U8lswx-SCiyyRQt61jIocwoAmMYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه بین مدیران باشگاه پرسپولیس و اوسمار ویرا برگزار خواهد شد. تابرای فسخ قرارداد دوطرفه به توافق کامل برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24210" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24209">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tar-3hgazk4MAXgVwojBvrQWwK4zwg5lihl88AnsZufcixVICfL1TS8k74uUhnbvOjiXs-CmNDmd4tu8yzL-MPHCykrf7HjcV6XAlZQKxE2zpHKVTgR64N20cA5Lf01eGvgkM86qBe46kOKA7cTi314LwScJ49D41dmPixDQxt8HLj7nYp4TUKEqxhTER0CflXq91-wg7lg863sSRFfli-Qh5Qemr0oLTU-asrY_AFW0n9d-UEJhcNtkgv1K1Efb_baw2cisd9QDlLpJOTrbL7FIAHvMjr4ztZHVR3L-BSxgYUIUmDPz7mTRo5_jX_MolNBdjyJWb6ECYmb7kTEgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی کاپیتان‌تیم ایران:
بزرگ‌ ترین شادی صعود به‌ مرحله‌ حذفی جام‌جهانی این‌ست که مردم ایران به هم نزدیک‌تر می‌شوند. اتحاد و همدلی بین مردم داخل و خارج از کشور برای من از هر چیز دیگری مهم‌تر است برای رسیدن به یک هدف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/24209" target="_blank">📅 14:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vT3xU9e2Vi-1MrNKKREBXYTWE3xGNa18IN1lPyt5wvnt29Sv8YfFXSfej4yWo8eI54B9IXsuhUbDlZswEnJKKQu3yclxb3m-YEKGTwvrDzlfSQqO7ugo6aeyjScEeK_MHd2aAgiOXjtu9n1urskzSxO5aD7yJNCUYkuoGitqpf_3xlO0b7RCvKDuHuTeOyVP-QHh1KcXtvLF970Q_VLII4by8frycMKtLvfIfpYH-mDuRhcwBQiOTM9gXJ6RcwUO9YWcXBWJAg_YCy0573SkMV4UYdW_p2ul5NJwZXpv8NXCNbqcjduEuViCRnQgnr5oxjcBxoHFigWWAmo-vT50-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24208" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=BeHr4jdzDHcFoQdrrKlCB2hP9rsYNsIJAOuNQ2RJBLK2ZRboFehzclBdIk0u8hKW5eBbB7ZA5daL5pC-WUYIfoNhLmZYWUmfQrAq7O3VqPzpL23ev33XnBUsMHS5T_dfnWbAAR7zOVUf_Wf00zpiSR5b-43z3ptf08jUaPGzSve2EuTG9tDJegt2eVMsdOHw_MHYCJ-Xc6OaNY3k0OD1sMLzhC9vbuojKWUgeh5ZpLLQE4w6gIp5v59M0Bz0GpMmO5duxAAdMaotjA9yaIg__z80O0bV5GvqnDBJlbKbnhnFJuQCO-1Yog8suL2a85lQ12Fww_JdGQe5VkGWNHtigg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=BeHr4jdzDHcFoQdrrKlCB2hP9rsYNsIJAOuNQ2RJBLK2ZRboFehzclBdIk0u8hKW5eBbB7ZA5daL5pC-WUYIfoNhLmZYWUmfQrAq7O3VqPzpL23ev33XnBUsMHS5T_dfnWbAAR7zOVUf_Wf00zpiSR5b-43z3ptf08jUaPGzSve2EuTG9tDJegt2eVMsdOHw_MHYCJ-Xc6OaNY3k0OD1sMLzhC9vbuojKWUgeh5ZpLLQE4w6gIp5v59M0Bz0GpMmO5duxAAdMaotjA9yaIg__z80O0bV5GvqnDBJlbKbnhnFJuQCO-1Yog8suL2a85lQ12Fww_JdGQe5VkGWNHtigg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌مکزیکی‌انگار خیلی با پسرای کره‌‌ای حال میکنند؛ هر کدومشون یه پسر کره‌ ای پیدا میکنه یه ماچش میکنه. ببینید چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24206" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=IpBIME00sgklUb1L0QQPOtvWnDErWpG8q-XsgW3DgZNSmg--hNlcKsiMnv-crqfHG_jiRPupIXbUGrl4OJt_5Ppfd8EwVaaoZnPaWSUuSMXy6m4LvrzhPHNKyjDJdHJ7DMoMtdp7XAk_wo22TiJxykOBSncmqZ8YcQb7EZvnGUUqDPCUyTobOLdGnaboAnVWucUvxYmm5tNH7NCpCjRLJSjd_U1w1ausscW3x-ogrrI88XjSeg3v4WVz9eqyxljGu10aNX8BslymVGlcVbRA95hMr1CytFQepwXqeokAUNt4MkdChTID3StlmmHCHX90MYWdAp2cWJ-FZtC0sm4iGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=IpBIME00sgklUb1L0QQPOtvWnDErWpG8q-XsgW3DgZNSmg--hNlcKsiMnv-crqfHG_jiRPupIXbUGrl4OJt_5Ppfd8EwVaaoZnPaWSUuSMXy6m4LvrzhPHNKyjDJdHJ7DMoMtdp7XAk_wo22TiJxykOBSncmqZ8YcQb7EZvnGUUqDPCUyTobOLdGnaboAnVWucUvxYmm5tNH7NCpCjRLJSjd_U1w1ausscW3x-ogrrI88XjSeg3v4WVz9eqyxljGu10aNX8BslymVGlcVbRA95hMr1CytFQepwXqeokAUNt4MkdChTID3StlmmHCHX90MYWdAp2cWJ-FZtC0sm4iGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن
🔴
مستقیم به قلب دروازه ی دشمن میرن
🔴
ترابی دریبل زنه، نعمتی هم حامیشه!!!!
🔴
مثل هایپرسونیک از لای دفاع رد میشه
🔴
یه طرف میلاد و از یه طرفم جهانبخش
🔴
پهپاد شاهینو رو دروازه ها میکنن پخش
🔴
حاج صفی، حردانی و یوسفی مثل شیرن
🔴
توپای علیپور از پاتریوت هم درمیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24205" target="_blank">📅 13:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24204">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyVpxY-f-Nix80VJpiVwWLAlbui7Z6A6WR-E1iNnXPCmvQd42FHFLH8ENzI3_fFGFZbt9TbsE9ihEURp_g8i74jdlQ0uaWGWwuu3UeSBQVVLjKi-1Ed06MMNRry0wjXPEjU4P8-sDCMDSu5hgg65GxJhXiIbIxb-VD8IuuaxnFOX1lxkuinvhtsxiGQovz_0fiByUnGwSNZm27aHR2CQdQb2ZPuBCL_xqWfCoesAMZgOAsSEAZbBk4NuB057LrHsxyMUIlNKeYBarFhX8XOE-aie4Oi6kID5DZGBSRRlXPuGCXCtTfKg2Ao0Eply0mLgjfEnzUFAa5B4jwR36PfBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پس از پیروزی پرگل 5 بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی 2026؛ پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در هشت دقیقه دو میلیون لایک گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24204" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kadub8rLVAzcMdqQPVDOCYtGsHDiq4QeQnD-01dF4afT7qoDLlJzZaG-jk21sYPaV3cBNBR8jCvx0hGm7lUxAxBsdkpp3PDMTUZaZJqomKR5f5HvUdLqQlqnQrL9yZLMNHC9SBAkPk3WveUJq_aqpvv64l78dZLdGRnVNy3kY9YTnKGaGeK5wONsBPKlYITM7FP-tCy8RctL1hTaCdXbaGmyHd4XexwHW2BVFhj0QPUysqsNnHYOC8y8WbPGoP66ltsFlgn5kOZtkb9YXndn4ytlG_q7nyG4xwxFKDbE2ilEBcGKr264DbC3NZe602Kafcs2yK_s1jHD_eImCBZdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24203" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azC7gtryPOWI5CoGkTdym2kOT33i2_V6mqbi6o_dZUwiEq8kON0XiNikSIuy96pL3eTrZX2SNO9l5GqZy_wsRlmarpJRuWEjBWDWErFXFMmqWlla6DKNh-svD7mgxnXQvV3YR41IJb7mvePG-FbqqbRP01Cp4LJIjixbIrX9T5S_hjmyC6FAzNd8OQYmBVmtHD5pmfEjrVoUyIIfL1MiazdLbFnDPQi6aoI7x-4GGvfIF6yLRZepc_b6FK9QNud9cZpxcZa7xPBcA7-khSJSN6ecAMC-z1SvyCSEHMnHZjRvUauDG9N-oNxQmkjBwN9kPGv-OonJRZeVtZj-Eyu__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24202" target="_blank">📅 12:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMq8fTS0qgBOmtGiXOTbDuU8W6svCfjfQgXalCAgSd2onGo38OKeEzJT9_pHTX9yRwHgMKEv8d0hKn889UZcrOMN-r48gb7N2riIUJl60mfOZFmvPSZ6gfmuqmTPiwkMAUiRs8lL1ZbC_sCBLO_J_-fxWQz0YQ1R1uxcUvH7_W8hUe8IoURHyvc7k1aIEc-Hr706agyJyfrrHKshNsGLHPxBEi7EoHNrTAA1wl5EbCGux3jc-qCd8upRiYQu2pLlH_KXP7p8Lj1HeV8FVSiL0CxZ4uW5xx05NsdcjU4My2zaxGSHDKKtS0tCMPbYq_NXSoLbhKG7oTB3o4FsAlX8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=ocXe0Y2G6D7pzv1jo1irB2ZIHGedGgHLepO15g4oJsnhgC8P21BKx0qWaJuCjeZK3rG5rV1PcDpho8GWRiwSSC9d-T6tliJ7cHo2oUmrb2PRefb8Wv6ynZIYXIimo-Moy-Ys2HmHpuwdHzl5MG_aAR-0lDXto4pEEvEBJbPF6smgWb2mYlqgDbCOrmMjAqZAQVWAn8xRr4p2mnySWy_HcidUmyOzhO_FjTG3IDbI7OGFzMDgGut6JqgaX84RzuUAlj6I6Os1uZi8zpQJ5SEtOs2pUyDwV_tYafY1uAzpHcMxJyM1-Qo_-OdEe9PRuXvi2-TKQbT3X8sliEx-ZbRxwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=ocXe0Y2G6D7pzv1jo1irB2ZIHGedGgHLepO15g4oJsnhgC8P21BKx0qWaJuCjeZK3rG5rV1PcDpho8GWRiwSSC9d-T6tliJ7cHo2oUmrb2PRefb8Wv6ynZIYXIimo-Moy-Ys2HmHpuwdHzl5MG_aAR-0lDXto4pEEvEBJbPF6smgWb2mYlqgDbCOrmMjAqZAQVWAn8xRr4p2mnySWy_HcidUmyOzhO_FjTG3IDbI7OGFzMDgGut6JqgaX84RzuUAlj6I6Os1uZi8zpQJ5SEtOs2pUyDwV_tYafY1uAzpHcMxJyM1-Qo_-OdEe9PRuXvi2-TKQbT3X8sliEx-ZbRxwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اگه جدول رقابت‌ها همینجوری بمونه؛ پرتعال
🆚
آرژانتین در یک چهارم نهایی بهم خواهند خورد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24200" target="_blank">📅 12:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIsVfwQn6AIqMGSKqe6f_MKPT50gIZM4sfdOWdjNoerZ8mff9O2uX3xf2WpXaWgLw2-uU0aq7k_tJE2z7I9Se84kpbumT2_2Q5Vgsm_NK7Ib2TYe3Vl6poAb--FeeqV5talqPro4GvvXQZtw3flBaorBU137gAhIwptxwpkuiDBp21EHsYtivs1DWy3rUUVdhEEBYOb0qSktwqe7ZxDuGTSbFTQOTDAKAgRMW66vkhtzA9FmJh1De0QBsvd9dZr2jGSVViN4oI6BuVDTMGBU88ltSIszEnuCW1XL_3ppk_QL3ylGrVudT39hh1uzZa9hIyWKrCRB-kBKEKQ3JAYqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24199" target="_blank">📅 11:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2111536884.mp4?token=F3Hu3mdaJ-HnZjP_AR7XkLhSgICTB4SdWE3kobRm0KbXafXSHKswsvpt2t_g9RBknLBXuM4J1Eyduwo5wUkk7_RdwWC-MYbOXugv4shmUNMT-Swresogxc9WgCWex59ucy4OOPW5xRdyZQ0X3ZlfpCLz57DGK-kXEZwKzMkethzDpKLlDUz0FVUlMdJzpGd0OkEg-nbhpSwsk4HSbuozCaU4xhAXVmHEtLn5OtucAjHN7uxJsWbaGqoZsNo-ytVULNbf0r56-7Sz2rOj4QDB7NyL6Ei2Zv9gDTYuLw8UltglxUwxwQ_to9lUvkqNNcTHR65nQ53qrrHzftVeXVSPNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2111536884.mp4?token=F3Hu3mdaJ-HnZjP_AR7XkLhSgICTB4SdWE3kobRm0KbXafXSHKswsvpt2t_g9RBknLBXuM4J1Eyduwo5wUkk7_RdwWC-MYbOXugv4shmUNMT-Swresogxc9WgCWex59ucy4OOPW5xRdyZQ0X3ZlfpCLz57DGK-kXEZwKzMkethzDpKLlDUz0FVUlMdJzpGd0OkEg-nbhpSwsk4HSbuozCaU4xhAXVmHEtLn5OtucAjHN7uxJsWbaGqoZsNo-ytVULNbf0r56-7Sz2rOj4QDB7NyL6Ei2Zv9gDTYuLw8UltglxUwxwQ_to9lUvkqNNcTHR65nQ53qrrHzftVeXVSPNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ابوطالب‌حسینی‌شاهکاره؛
میگه تا بازی بعدی یه 6 7 سانت کم کنیم تا قهرمانی جام‌جهانی میریم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24198" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👤
👤
جواد خیابانی محمد جواد رو گیر اورده بنده خدا دهنش رو سرویس کرده؛ عالیه ببینید
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24197" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D74VP_Jj8ri1U0UXlh_Y0fC_Szjt72FCltsd0_2VVn8qNv9VNHnVpL-zK1S1_RogITcNqPIUD8x1UZdFGr17xAeMXFRe8ln4YPYU3qFIq3zBELPnhUhBjiqEgPEbt6loAqN9KVhakA6s0AFINw_JdfWJ40Gk_OUYgX5FgCI9bxv_u5ns-1w4ulmjnD_-kmQJV4DetugJ7W--Er4VKgLKMAAmw5PfVrtzsBCKjuppheSkT-XldbvACQ4hoY8Hvpvh1CXcT5lUppdT5jXU5B18rb-sNGQdsAJn27Xx6rmdB9xH24FTYlergBUg_YtYo3_DLYC9Toxqo6C9kIO39x251A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی اسطوره‌آرژانتینی فوتبال دنیا و باشگاه بارسلونا امشب 39 ساله شد؛ 1158 مسابقه، 916 گل زده، 414 پاس‌گل، هشت توپ طلا فوتبال جهان، قهرمانی ارزشمند در جام جهانی 2022.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24196" target="_blank">📅 11:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=HNYvkOwKfZGjvJq6zWaGdaDR5d8KthvsLnGweZk74Fn-iPuVZMf7tBXswbwYfdWtA3XhhAuC1y0S1pn9fN0_kTJumTOHiZetGJCsD6B9pfSKkAaYfbL6G8wX-aN6HoqRM6_6U8Xq1uheyWYRw6sG2LCo4u4jQY_WDyyOOycRUnh9H8Jalw-w6TLm0rVpA_1LUgFUIo0P5D3MSNBQduVDL0XfDcuWDmwUlCY1qavwqvO5NFkAnYvxkvqcvG8d9TQYiXyf1yp75ec-XbloaAmq67x8XzhNRR0UNdY_XGh2G2sah2v7OWDOqiKrSj_oPx1K83K0ZpxbCqr_7joA-nT7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=HNYvkOwKfZGjvJq6zWaGdaDR5d8KthvsLnGweZk74Fn-iPuVZMf7tBXswbwYfdWtA3XhhAuC1y0S1pn9fN0_kTJumTOHiZetGJCsD6B9pfSKkAaYfbL6G8wX-aN6HoqRM6_6U8Xq1uheyWYRw6sG2LCo4u4jQY_WDyyOOycRUnh9H8Jalw-w6TLm0rVpA_1LUgFUIo0P5D3MSNBQduVDL0XfDcuWDmwUlCY1qavwqvO5NFkAnYvxkvqcvG8d9TQYiXyf1yp75ec-XbloaAmq67x8XzhNRR0UNdY_XGh2G2sah2v7OWDOqiKrSj_oPx1K83K0ZpxbCqr_7joA-nT7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های انگیزشی و زیبای کریس رونالدو اسطوره پرتغالی فوتبال درباره زندگی ورزشی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24195" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYeKaGV_xgsGKyDSIe2l_JceflSVbgXESbOFxiqhxmC-8axDhK4PKTgYvf4Ddu-EFsxvVUydtZIwdC2FgOcSHvpivG4-toR7asTBP8R6O4woO4yzVhJ4GtBJUnyAQMGYkEJeCgdgse6T1nzF0SzfDncY9W_JGmJh3r54xzMIR-GkJVEccVi86yLWpkyBib6SXbYPZ7PjeBHAvLMLYjm6AsC05_9UwROn7Ug0HB1GH2x_L7BrxzFAtMVSwyf6mPThIKqbshI99JIcqY-lUNjOb2S58478VqYX4IXlvMnQRw2M-icqPNkx6c4cQsgZg0z2KgYLAp-t2NBIkeUpUBHNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه نهایی بین مدیریت‌پرسپولیس و اوسمارویرابرزیلی برای جدایی توافقی برگزار خواهد شد. باشگاه با اسکوچیچ تموم کرده و فقط باید اوسمار فسخ کنه سپس از سرمربی جدید سرخپوشان پایتخت رونمایی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24194" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=NKS9vsKzp2AU6Nm2fvMnUG6q9rrApJdn5grbzh5tk3Gv2tecji67PPjapFLqWlTirn6eIg7-jJxg-NAHeFPM7WwVFy6Ei1htF1jIivXBqyGo-xgwaQrOV2KCLRhM1902Q6CgzasAnv2TqKjDCvJmZM8GZsJky8FqLaS08iWcpVaqaMn4TCVCJzl3UkzSDLpflxdV_q80cVjwNNeAFofAhvVh5Ga0E4K3e2dns510eymZ8L99MbqdaerM_U9NzQMz9w3lfx7f5EMnalFUdrh0fo4y-UHRPpb0RmRvReeb1IfvYCsGcsIJb3YhkqglPFxID0yAEtGPNutBeCshCvE3Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=NKS9vsKzp2AU6Nm2fvMnUG6q9rrApJdn5grbzh5tk3Gv2tecji67PPjapFLqWlTirn6eIg7-jJxg-NAHeFPM7WwVFy6Ei1htF1jIivXBqyGo-xgwaQrOV2KCLRhM1902Q6CgzasAnv2TqKjDCvJmZM8GZsJky8FqLaS08iWcpVaqaMn4TCVCJzl3UkzSDLpflxdV_q80cVjwNNeAFofAhvVh5Ga0E4K3e2dns510eymZ8L99MbqdaerM_U9NzQMz9w3lfx7f5EMnalFUdrh0fo4y-UHRPpb0RmRvReeb1IfvYCsGcsIJb3YhkqglPFxID0yAEtGPNutBeCshCvE3Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌ابوطالب؛
رونالدینیواسطوره‌برزیلی‌فوتبال جهان در سن 46 سالگی به دنیای فوتبال برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24193" target="_blank">📅 10:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=uhsAil1oWjniWBTkY615ust0lFcIC9NODvRzCFyerYzl4L1t-Jv9h_LMpyaQ1FFpsy-hMKaoqizfhN-JSwCmV9M3LwadlCcHkwk-VB3A_ua387fdFMVepNCwMYZJ2fMqXWQrKTaTpEHlZlPwaI14Q6xOoK88QBA2fTZQDDxjJnEp5CfgXKwdOjcSI3S-l8AZktjtspfuosL0rNjbRPsw6dPNQSAHVD58lpnVyGK59dmRK7GKpH2NHqQSlBY9IF3rLgx18P_DG4fAvws2A0iTqeAPdtkfMBuHetOXYxq8HTkFGdJuGj8wr0cgT6UanbPBsIVdouCne1KoQuL2AabHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=uhsAil1oWjniWBTkY615ust0lFcIC9NODvRzCFyerYzl4L1t-Jv9h_LMpyaQ1FFpsy-hMKaoqizfhN-JSwCmV9M3LwadlCcHkwk-VB3A_ua387fdFMVepNCwMYZJ2fMqXWQrKTaTpEHlZlPwaI14Q6xOoK88QBA2fTZQDDxjJnEp5CfgXKwdOjcSI3S-l8AZktjtspfuosL0rNjbRPsw6dPNQSAHVD58lpnVyGK59dmRK7GKpH2NHqQSlBY9IF3rLgx18P_DG4fAvws2A0iTqeAPdtkfMBuHetOXYxq8HTkFGdJuGj8wr0cgT6UanbPBsIVdouCne1KoQuL2AabHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24192" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0zh3xQeI8-cl1GagOty8LiYugxE08c10KMd9V0uGU59VHE0S1nCa6Mfs1mZYBpBEYu_SQ4favkkTjXvviTcz4IB5csXPVutVeE7NvwW1hUdPi49bFPr7lD8yZ-aVCWDX50f4bADYxkOuscK45GsJcmCyPAWnuNFmdlEjv7XvPDWHl2msFKd_9UqKbFZCxhIn1wVUqqxx0gSTC9B_q4NC4biqR6NZUFSK9OjiLCd30lY_cVKxMXekK111OVu7s_9Mbzm5lmKTZrBrJJ1B0OPWK3_4t7T3ppXT7njghc1iIo4iBSBukG-DSxaQ3UXpuc_avDJi9llu5nwkz__p9SAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جداول12گانه مرحله گروهی جام جهانی 2026 پس‌از پایان‌هفته‌دوم؛ تاکنون‌صعود تیم های مکزیک، آمریکا، کلمبیا، آرژانتین، فرانسه آلمان قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24191" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24190">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROpuWXrcCe9_aTW_AvWKnGCBfTSNKUsTKKwR_sxg9QhbxeRwDwyIzFEBPZyqMltl5z7eTRg3wwxKjdjYBWS6iw0mO6iLdCI6QTGKUxhnJQ9fmfC3H3e0GMA4ANaMcK7aJnN264Kq6NM8D15TDJ_5n7Puezi8t_ASPKjt04sWt3ktBfC46l2kHwpEB_kvI6FFxrj8URMsrGcq-BVT7TVdCBZCOcAXJmL5TfXRR6rPnbu5jnEljV0kGl-h2CBZmo0MtTRS2TJA68uoNiqljxoFDCvvPrKJyxHH28uB92CcD82cXeFcZihNIBefDrdnD6EpIqIGy1x4n1s_tndL9JSPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دیگه بازنده مطلق نباش
🅰️
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
💵
با بت اینجا همیشه به سمت سود حرکت کن
🔼
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r3
@betinjabet</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24190" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mxENHsXZsx77_iQ6Y8o1ose6RD_rpTSlO2tg-RrOoeGHiYuhTRIEEJxZh76GumKL522MfsuIfG5f3d6dwqnvuUI96KQxCFtU85QVyVal8R5RuZyCoT-J3SU1N-4IRxUanNY-jewBocIPCV9mlccZqg592lvVPbagtrKAlxw9j0rG25IsKuhmaNCYBwOy-aJ1r08C4cem0JbNAikmEHdZbFQ2Df1X3j49nFuvMDkiU9ehzRgXpHLB9Y2aEAGYD449P4x0wldmyXHrHuDSoK3pSHXgLfsEFKAKWk0yO01dG5KoOYAyEK4z_I1Jsw4D3LSgSlbykP_2lkU6Bp0eIeO_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OozH7FNpaAYuBYwWzB-sOpiete92f9y7nM1zHXN5g0yjODf0HNqlOe_Lv-XlJ5i7k7ujcr6LxPr4m98VKdd40fbH318liM9xp3mVigpch0aLTVUbhXPeDgc8uUPs1Jf1cf0t7XtrZfeDtALSuiy2X3_lqXCurOHncXpihwliDWARYmPxohQXqcTVFmOJ1LbgOCkisKy-o4ofbWbtqbK8ezu4VXtx2XgpCt-316DJYrvxlkV-teOglQxTjK_TkEWHSV2Jsl2V1TGDug99_ufF9HuX72ydJuKpBCjBGBb5eCZCrQBZiyW6U47z2hUxUJ7xdbpvUAvu2PptdARCeWzycA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
هانده‌ارچل‌بازیگرمعروف‌ترکیه‌ای:
فقط بازی های پرتغال درجام‌جهانی رو دنبال میکنم و برای این تیم و کریس رونالدو آرزوی قهرمانی دارم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24188" target="_blank">📅 09:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=PteCXK50uDk5ctv-AGL2baVgl3oyloLlib4CKuwwlcwJu87cZzQotj05wjDx9sNXGuIPBvmsmqRBmAnpDyUUOy1TmeLCZRwYkzAmZmWdPY_y_eJqoBgvU-6MQBqaOGr64RzRryookxJ7t5v-ozRVC0vYt4rWUCUoR_cAI8qW1EiwjuOeIeIr4D_jLSS1TYhNOuJS7SP26jJarBFhxQ30ZIIIe8uU9nTse2Z19O40cTWO6_plhCoB8SoolJV_3wBwbO6pKxuNY-_Ec5t4kLokfclZQCwyS61ENG0gRwpiX8iG8NM_TJ4yObgAhEUOgGmK4NzDusAWgHOiOQmD6rIn-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=PteCXK50uDk5ctv-AGL2baVgl3oyloLlib4CKuwwlcwJu87cZzQotj05wjDx9sNXGuIPBvmsmqRBmAnpDyUUOy1TmeLCZRwYkzAmZmWdPY_y_eJqoBgvU-6MQBqaOGr64RzRryookxJ7t5v-ozRVC0vYt4rWUCUoR_cAI8qW1EiwjuOeIeIr4D_jLSS1TYhNOuJS7SP26jJarBFhxQ30ZIIIe8uU9nTse2Z19O40cTWO6_plhCoB8SoolJV_3wBwbO6pKxuNY-_Ec5t4kLokfclZQCwyS61ENG0gRwpiX8iG8NM_TJ4yObgAhEUOgGmK4NzDusAWgHOiOQmD6rIn-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🇳🇴
واکنش‌جالب‌ارلینگ برات هالند به دیدار بعد با تیم ملی فرانسه و امباپه: «فکر می‌کنم فرانسه ما رو شکست میده و احتمالاً قهرمان هم میشه!»
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24187" target="_blank">📅 09:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNAVSn5GDoTa90qAhwPyrACJ2EILD3YihT3hwIp3y3pDSXG_shkZUzbhe5ZXtXPipiF4zNuFvTwP-3EckuSWpM13P3mJa7iYYI_xVjH0BDwHUlYAl05iQtCm6VQQwEScixwj-oFOqvsbp0aW28aBRGCHJhaRm-D6V9DZy-pX9IJuH4LAg8Pckv8SWEhVlAz5Hx3hpQQ37lxC4VkDURbw4N1PTPVkGC0BnD9VNpNupAFxJXzwp37AnaW3bbheTVu5DJznDG9iK_kYVleyWLKAdxOueslGJyeyKhzzxbHrTlu5_0cHMFTt3qfgFW17D1KFX4AVGXYXImr8Uv6wWPXUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! کارلوس کی روش درنشست خبری بعد از بازی امشب از نانا کوآکو بونسام جادوگرغنایی تشکر کرده. جادوگره گفته که کارخیلی سختیه ولی تلاش میکنم که غنارو چند مرحله بالاتر ببریم. فعلا با این اسکواد شخمی و در گروهی انگلیس و کرواسین صعود کرد‌
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24186" target="_blank">📅 09:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdxaCRcGkFu6Ifx8Ja-oPSM0Oho9CD8nefHBr9nbh-D-CRxkRaTKaNXHSm1xYWkJRGg8fPzz4GduMpxgy8aHH7I-JteS9UavKHHRDraTtNtDaPGBNp6XL7m1aNkkbXdMA5ZnhY0AN8TMylT_XLYxoXKPxLnaGqftHp6HmlEq2Ec44A2CRkd76QgNjjHqdLgOQ4HhxbA8l3MWoFypLPukGjjFCUfUM1z_z8IedsdJ8eoZ_9vgbujYNTRmO6wtFnn9J8nWWNrF9-jnBn7DDsRICb6HZ3ajWtEfRmSk9RT8PtB_VeAzZEfP5PWM_XuL6TzGGfnZMmQPrjP7kjd0E8HGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌دو دیدار بامداد امروز جام جهانی؛ دومین پیروزی کلمبیا و صعود به مرحله حذفی؛ اولین پیروزی کروات‌ها در جام جهانی و امید به صعود بمرحله‌حذفی درگام آخر مرحله گروهی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24185" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUiSJ6Ut3_xmprcKjfXGlbS_M_EDJWrqgk8d7rFGkmuE9ISwxwpFlhZdrfakfUmK9c0slM3MYzU9FR2JKjjoFEmBIY0HjJHyv7jGOCJGt9slqesMfhIL6JPsxnOzLm1oVuQISHXC4tt6Tu39GjZfGx8l6kfRzYBdMifREzvjJ21pfMXWBBZtDa406RIZ8iCUtr1FVa-ZDPcf43KALFvUGMxv_RveKTZeV6FVkLZ1IKM-CL5M6Z2u2cjJvc36Y5BWWgflsZyaOjDx1vf5Oyl5RxMNRLGcUqhrCZ5ccJnoK_b2_1BvW6jcSi2J0y-CwxgLy0IxrHor1mrEkd5toueEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QCG_PFrIUc4ODlJlGn_W5xpIMPhVrI6JEgs7Tmr6lOnZYltRKiwNv9l2gxKNnyAjl8l1RFnhmkkqEOFKF0yLaoG3oVIXvW9WV1ytqKkVlFE1UULOnpxTXIyhiLiC0_kyCIQb3aQwqqq8BXvpj87UhP3_ZlvrvV7P3tRtRhgvHu1lpB796sxC156HHco7Itw7W4HlPV6cDGo4IQslBr3hq8IHwXIzV7MXFEvcihLUSu471FOOzJUnyFrarlOpyW3sfqtpdCw2eyLgA2A3WaH0nZF3seNHCHtEJl7ygrT6PccEUlLgZ2c7xcJTiql0ukQtBO8DRu01BeF6xTmolFMwPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24183" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSAy9AtGpdRxQlIa68rah7rcJIz-XOihhL_Qed-k8h2F2vdxnFSX28yaZ9UW4t4EmMIbNMWANX3wfo0NKHEvGZwCzhYUVeiNNjtH4mGIZrsrSCghtFby1Ves7HRs_WlCdTZlSn4XxHZijaZmZm78UdzTuGCWmZBJtDFGmBx6ctwOiCNvvMMsVIhIPMilDYTmrioP81J0C-ZCGVoOQVc6Meg2TT_hQ90qRIQ4vUMGl2V_oh_t8531StJqemNJi0u4XjddB8EvlFLIlo0DdG6AdHtOhlnoHDiSTvGqunDozmV7yR7mUUjvGAtqFBQlVPLKs7GM74gyD67f7r_Kb6GKhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24181" target="_blank">📅 02:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpJPLCVVuWiLhiQQB-bYAAA2M3U3JYoteb3yGQcPRqVPUhKJvEdh8oszaWomKlCwlazoBpQ35lwqgn1bTLGIKPlTq8ov_L_WYV4ikhshoNVQ14YsiWQ4ThulBZqKQz3Phcvq5qrB8fSiwunwr9fXoqrD-3dU5pFXsi0gOyt9Fna6XsYRgWx7R_MOEPark4s86_BzzAIl6aqMNk52k6bQzfWlT2YMap2tI4mbTWSFlTxAsmX5UqxXqyzKIys9ygM02nwHRK2s5hFEFm2Vfr9XEgcmIWc7N1M-6VuEjI2kO4vWI7DiK3Pt4voy4d3NV8Y2F_QAJ9J4TjLDJBAP6eTESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24180" target="_blank">📅 02:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2R8CdBrGohrB9Wp6sQYJfLUCYCdAwBnQu-jUvU0PDjKsb_Oxfg8cmcM2OuA6HRexhLH6j0q5SqKgAoIHKkxKSriaub2uzNhiTTL6tixUXXRkmzF9oqu--S9eInKnLOUda6RcVgyhoLipLBlR-xmqdWPH4wyfnTivENZCcl5tD1BRL4mPF078Kjyd_jzHb-OnWW0jPiJJFXiGchLz9GVj-PWcdwdht8cW1DNmg25YlXUpnF0-tdgVOAJA5SvwpXiDonn1344YkXyzokYdDwsvuZsNLxa0WuGaVtJeNYw0NTlRmLzDI-VJSZV_7rOlzj1losG0OKgqQboE4VPjkLS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از بردبی‌دردسریاران امباپه تاآتش‌بازی پرتغالی‌ها با دبل رونالدو و توقف انگلیس.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24179" target="_blank">📅 02:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=Qsdhlu8cd5zOwgg9iegs0U5bbGQGLrE9MkfoAbtP4uNr3ZLkFZeoNz4WgD5kuprYG2-NX2D3_9fYnefPZ3XVYn--T8zpl-tMtGGG0pyPo-r8OOmuW8gbYJzMdDFEZiYe_FPh_Rmm2dBBwpzYSi36BWaH4SpVorkaMsGscofdtzkiaP9BU3VX98nlWJjVo_XQJ0_uFSQWt_O5GhVIu2Wzjuj1-2DYiSjoxHkz5A6HyjVMKbak2rnpCh06c76NZAmGtUE0PDVYbQSItCeqP2LGPjWi9cU2Cigb7ROoeBfP9JkHnGmmiLFM49tRQ6ZznOlMAZcmgWIAZHfHaWnYq_9uYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=Qsdhlu8cd5zOwgg9iegs0U5bbGQGLrE9MkfoAbtP4uNr3ZLkFZeoNz4WgD5kuprYG2-NX2D3_9fYnefPZ3XVYn--T8zpl-tMtGGG0pyPo-r8OOmuW8gbYJzMdDFEZiYe_FPh_Rmm2dBBwpzYSi36BWaH4SpVorkaMsGscofdtzkiaP9BU3VX98nlWJjVo_XQJ0_uFSQWt_O5GhVIu2Wzjuj1-2DYiSjoxHkz5A6HyjVMKbak2rnpCh06c76NZAmGtUE0PDVYbQSItCeqP2LGPjWi9cU2Cigb7ROoeBfP9JkHnGmmiLFM49tRQ6ZznOlMAZcmgWIAZHfHaWnYq_9uYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس رو باز کنید ببینید هری کین که سه فصله داره چشم‌بسته‌برای بایرن و انگلیس پشت سر هم گل میزنه چی رو خراب کرد. تازه سه چهارتا هم زد یا گلر میگرفت یا مدافعان از روی خط برمیگردوندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24178" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZ-MviBlkQYjuZEGvt0xErQP8CAnbxj3L3yiGenFHYUpw6wJfQqtfYRxlkwl3xjhyFfAQToHlXffbnDKzJP7VWJtQpLXH_bGBL9crHD9Me2LPY4DVB1iuw2awG6atcUO1mmZjSmRj_j-GXxNrMg4PKs-54cVBvyqRdM3roeuPyfsfYjqeci_vG18fn3gPA974B691UqTlOKufLJFO4sZp2PqW8X29XuOxTbQwBLKYGCnI1UPJDcNph2he4vY2gjtOD-s258zWOOuwqJ4qcVQtUX6DW2jhtyWfrKv2U4kQAtchnUiKBQj8PU7yABVxCGfM-yFmgVG3AH1-YCWO_smWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24177" target="_blank">📅 01:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMtkY8s0CfjW8xt-71dXcfHqiRYomrp_Yub8Pd_nClmbFZapNB7iJif4ueC-SHphRw7mNapvzF7Uudu8S4icKfjrI1oekv18a5BSwC4Ey1atZjSGyOUsMlrJ12Tgk5VVTPezT0aAwP6Nn5r7ecwp9izr7wQ8LRcCL6v95sCtydpJiKqW4QkaOyyGbYc6nnmegbQToyPAH_MMDv3SoJz3xDrCcVILjPsMr5W9b1cjAqwW5_Hk1ouhbenJ3PvlYnuR9lyBxB5P5xKYxYyLZQrOi7_oOK0nPqlvVbEOYDhPVg0SzE2HObsScDbrfEdwrDuvL7LYS5d-VmD72JmzfGVXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24176" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=a_vexNX1miHN9Xn-FQ5J3HNNUP7fkKmOJ7DY38ekh3uN9PbI18zEPf4F9xi87FWNZgMBBvf5SucgeLkVEoHS_o6P7xZz8wGBBtLX5IQcss1H_qfA5MufGO2-vihVLhPe7rV1TBtmUreGBj4bJJOpahM2qyjZFrExggy6euMFYeohLfdCbdEZyzxdhVB50OIjB7xO6co6lthVPpqYjT3rG_dolnhu0sZSrhVdFU6NniOtEReItyiCOIy9T3XHDdjnScILmy55pwFTjXsLirXXh-egf5CrZHjVJEEDj78-HOEvq8ZhzPTau_0Zm81YT2P5Vja00xHsfSwCwkri0UeI3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=a_vexNX1miHN9Xn-FQ5J3HNNUP7fkKmOJ7DY38ekh3uN9PbI18zEPf4F9xi87FWNZgMBBvf5SucgeLkVEoHS_o6P7xZz8wGBBtLX5IQcss1H_qfA5MufGO2-vihVLhPe7rV1TBtmUreGBj4bJJOpahM2qyjZFrExggy6euMFYeohLfdCbdEZyzxdhVB50OIjB7xO6co6lthVPpqYjT3rG_dolnhu0sZSrhVdFU6NniOtEReItyiCOIy9T3XHDdjnScILmy55pwFTjXsLirXXh-egf5CrZHjVJEEDj78-HOEvq8ZhzPTau_0Zm81YT2P5Vja00xHsfSwCwkri0UeI3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24175" target="_blank">📅 01:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3nocAd0agV6xM6SXwmRmCJv_LjPz_I_JZBu_Lh3gAykm5wFcoJ0XUd1bkrFenb9n9OG7LN2E_6BMx4JyIQyL5mbtFG-FG3v8SxIHlldpOpuTw3tPc7ro7WwfrJSZwp3ouqBhSVnExeefZ7vkKC3B75m6v4J0hZtt_vFOrYCyVPY3X-5vjanJRpeZ7iIfC4tcG3xCzj-PlPnOvjmkudybwBQKZ-KEkBcS5ZTjD-JDJa3_JRfprdurBXCxf8916lybwyjR-X3ZyZDjwDkto4gkSLRud5NEpnW-Mja14xGeJynG4OUZNv0Th0Q28vVz9C4fRF5dn2LvQG4iUZ68Zc3nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24174" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=TcsiD2J1QPrJkwTfbp0hSUDef2wqX7c2TpqIt7qhilHV7-gNOnibR9cVGkSouBLMWIAYSvn6Ry6bUy0xsaDyrYPePUUse5ceCZ0-ajbdAUPRxwrQ2kb62DwMVjeJ2CFIobfcQHcgaukvMe89rr6rejfsSBRgqEcfi0-yEs-fAlpPP9xH3dF16QkucqM9_zmo37r9mgfdCi9-d9e5AWBdSQvC5NqsB8hY__hBbIHSoFjPpfywGlGVuR-b4OgvSr8eby24eiNDGjA9ngXKYLfeYkon9oN5kt3Gpfx8mwDLuv0IMEMdXJK6nCdTdEByuJ2tMaR0cbU09H1_Hz3OXTe97g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=TcsiD2J1QPrJkwTfbp0hSUDef2wqX7c2TpqIt7qhilHV7-gNOnibR9cVGkSouBLMWIAYSvn6Ry6bUy0xsaDyrYPePUUse5ceCZ0-ajbdAUPRxwrQ2kb62DwMVjeJ2CFIobfcQHcgaukvMe89rr6rejfsSBRgqEcfi0-yEs-fAlpPP9xH3dF16QkucqM9_zmo37r9mgfdCi9-d9e5AWBdSQvC5NqsB8hY__hBbIHSoFjPpfywGlGVuR-b4OgvSr8eby24eiNDGjA9ngXKYLfeYkon9oN5kt3Gpfx8mwDLuv0IMEMdXJK6nCdTdEByuJ2tMaR0cbU09H1_Hz3OXTe97g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE36ObDiHvn8fn-WmBNjr2HcJQVLi6U3DLUITGg5HTwJJNZHL7w14l8InirHayxvPkwsI3DhAKMfl2dw3nBDdkHHnQlo7bVrFh7Rl43so2ChoYB3_5ryNLI8ZkqpR18KxHUP_2Fpk8BjfImVNpdbua8RUzgMhuaq61imWlMvDXpT7wiFQhSpqqdUmFLm-LI35rJjWLTtE7YetmGlcLgGiuzjDJvvT52KwNak7S36qkKOvB5PRbWY0Y1on08nPeJLQS7woOWyqPKCg2mLyrOcCfVhdM7jjzJjhkLP2MEI_XpXEtF5JEkDIEAp_-f18Yh7l1UCs2A07TJQu6tDBWlHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=BuphvpO981Gen02UHBrzbN-n1G-bWpRs0qGnjGbNvXuRQ4mfYTTMbWPjPJAJkQF1iE7HvKCpeg9D9pak5fkG6QqNLJThqoTpBbG3mGszUlkdszTwRolowpybYiWaOfRFgQJgxADCerEu-22pEb22QfoaIBGSIDt_z7FMLXFJkxr9yjrpfcRWquLyStX30GOrEDxk2etyXDBzYIvAjWZ_h1BtNtcfbKw7IpYeXPfgBh7ZMGy5jyYhQBQEPkK3LVt-Vf6-3RANfQsjFHLOL0DpKa6Bw9OTKyer_JPjsimLrm71-E69UvLdmtLds1sz0ex8Z_sSCjqEA6s47aculI6MBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=BuphvpO981Gen02UHBrzbN-n1G-bWpRs0qGnjGbNvXuRQ4mfYTTMbWPjPJAJkQF1iE7HvKCpeg9D9pak5fkG6QqNLJThqoTpBbG3mGszUlkdszTwRolowpybYiWaOfRFgQJgxADCerEu-22pEb22QfoaIBGSIDt_z7FMLXFJkxr9yjrpfcRWquLyStX30GOrEDxk2etyXDBzYIvAjWZ_h1BtNtcfbKw7IpYeXPfgBh7ZMGy5jyYhQBQEPkK3LVt-Vf6-3RANfQsjFHLOL0DpKa6Bw9OTKyer_JPjsimLrm71-E69UvLdmtLds1sz0ex8Z_sSCjqEA6s47aculI6MBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOb1pb4heFQxtljJHPfBRYdj78PGxg1BSTVC9_trjZIEXPQwhyQ6TL1MMEuyguCb_jLo7w_Y2VLR6iLE-Z2iShgme5KPK7TFDEIfPOLBnU9nEOuXxkPb88uR7BIHqz4Sxy70rpQ1NwqWh-6zz0jCvDXJ5wdYJjc303nyiJrL8a_ybjcCqRNijE-HgPaa4IvWOxmNR0ebwYWR-V96N8ugsUEo2h9GOGMDtNt2yQGQ-7_FnB6qlMI9VY19s4s0preYs5spIJZmdTNUX7uPf_790xvqz0PhPi4hgkJKNI4LgZmMMVvEyQum3dCY8mrw7vM36BYRdcJH6q7NUo1j68M6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بادبل‌دربازی‌امشب‌وکسب‌نمره9.1 درسن 41 سالگی بعنوان بهترین بازیکن زمین انتخاب شد. رونالدو در پایان بازی گفت من برگشتم به بازی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24168" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0DzNzPGl725UOg8A_kyFhhwHK6wfnxdEuR-lYwyLHT1qveaBI_0t19eYJ5UtOqbAYYW5-oqqVtLO3cyzFZWulv_vgUdayQJYaYG7bkHTdQofluSHZb6h3iHYD3awNO9AC9Zr6-WVcx0mUdg0RZGUNzz5zkAB4olIOkZ9E3x92PdR2jY3Wvlzfx9-g7TJzeExSEVyfeNeZPlgtMn9GaVYs18NeL1V2fvQcrc8LgPtpY9gyIFAOzGa8OcMyQxnI8_KLO5BT9QYJoxPhgv5dOYnqnDrHS_Yf6ndK4y3fv4ktKY8u-l6ur7Hx-dSY5HairRRg-bXDkXBR1FzD9X5VvD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
چندساعت‌پیش‌مادر دیدیه‌دشان سرمربی فرانسه فوت شده و این‌سرمربی‌برای‌مراسم خاکسپاری قراره به‌ فرانسه برگرده و در بازی روز جمعه مقابل نروژ در هفته سوم روی نیمکت خروس ها نیست.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24167" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=sXJrBo_68oFp4VxsZtp_MFs-Fx7htJH-umq45G2BLlVRxuVpfeKaDk0-cgOJzCskMvSksD21pzo0usWjcN8dU7O3sp1Lro-hKgpEEei4V61XT6p0BUqn9vS5wM4oQYg6VEDTH5LkH0w0m8PabcVc9Z7l_HlnCXYLOpDZUZY-v75dgrma0dbsjfoG7qWHHFbVcRbOsf7wlAu-KmzQSDnlgbvWYqT46oyj9CCjBIY7HxuReiXB6LElSdHSo0zVRyHiMyozw9zvDaceWaYWncoztpgf3J-jfp_oM7H-YzdTw3c-8hhjiBtoa9iDI7i9xFkTPjY6T9Gyye9jlLFF55y9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=sXJrBo_68oFp4VxsZtp_MFs-Fx7htJH-umq45G2BLlVRxuVpfeKaDk0-cgOJzCskMvSksD21pzo0usWjcN8dU7O3sp1Lro-hKgpEEei4V61XT6p0BUqn9vS5wM4oQYg6VEDTH5LkH0w0m8PabcVc9Z7l_HlnCXYLOpDZUZY-v75dgrma0dbsjfoG7qWHHFbVcRbOsf7wlAu-KmzQSDnlgbvWYqT46oyj9CCjBIY7HxuReiXB6LElSdHSo0zVRyHiMyozw9zvDaceWaYWncoztpgf3J-jfp_oM7H-YzdTw3c-8hhjiBtoa9iDI7i9xFkTPjY6T9Gyye9jlLFF55y9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی تشویق تا حالا دیدی فراموش کن، دیشب نروژی‌ها به سبک وایکینگ‌ها کل استادیوم رو به وجد آوردن؛ هر کجا هم فرصت بشه تو کوچه و خیابون این تشویق‌شونو انجام میدن
😍
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24165" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIjEb6DpCJyRF-TVRAKjT_43lHyMeRuW9n6Qy3bvYSOrT0Td8_zXWuFanS7t8_B11NfRIfU4b7tRD_DAC6Q8GQQzMcptu2gJcQne3waDBDSFZikfGRXv9n2pfIzgwgvdvVK6R4FNQIsmcWzaG6131g4N06giwpZco8NfAIW_9gCoD6KJHQ5pj_Cg0jHr6n5Lm_v8m1YGqnUaYEzbyU2uFMRrsFvx5gxDLQewt6QQ__30T8wD9hdlYcIosKl_LTii002cbYLgMVwip1N9dS9WW0e5IOqFQKokLVdbHNLxUVHhiuyW5t02PCcQpfE5GsNp8GkPn61jWwWkUagYnEFHtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24164" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=WOcEQ6AjEHvEX4z5V3VksVMGplYoHKZD_HEOZlbMTiveIZA7kKMW4yAG_isUbcoyzkYp0jqf-ZNhNf9ugIyxktt56NfbbzEgnbMRG965Jd3SqR47fFFt9Q30_VuVRDLlRgb1RRR336JC_FcC8bAfXrI6lO8g45jVALQcrHXQkeDqwQItxyFivUWdqozfspmrj8IgipTfBZqKEI7cmjZc8-2n19KoSCGOhXf6_6M8jgaa9SdMC5NJx9DDh13vJ9DqpwlNrRBmgLd0UCiodnqCOiMICzBr6I3e6on1i3hpC3Oujp-w4DLlKxXlJXhhy59p6z11vpQvGxYBtLunLgoELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=WOcEQ6AjEHvEX4z5V3VksVMGplYoHKZD_HEOZlbMTiveIZA7kKMW4yAG_isUbcoyzkYp0jqf-ZNhNf9ugIyxktt56NfbbzEgnbMRG965Jd3SqR47fFFt9Q30_VuVRDLlRgb1RRR336JC_FcC8bAfXrI6lO8g45jVALQcrHXQkeDqwQItxyFivUWdqozfspmrj8IgipTfBZqKEI7cmjZc8-2n19KoSCGOhXf6_6M8jgaa9SdMC5NJx9DDh13vJ9DqpwlNrRBmgLd0UCiodnqCOiMICzBr6I3e6on1i3hpC3Oujp-w4DLlKxXlJXhhy59p6z11vpQvGxYBtLunLgoELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24163" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIfalTbMuMH-fgzc3zRAN5ApKn2mGNl2zN5jUXubk8eWnGqMLX78ceEXqLYunJ6DTKCAB3lLEDTo0PtF51M48sbUwGxN1U6Sgg1fYHJrnTzBEz2oYhtOB3fWjOk61wZtLi3-L-OhvauB-BLa7btftByoCw-nLjkIvLfhAJHD68Y1v4By465NdZb0emMtXkO5TmoWb_9LHTN2AVYdYhnazZuKAqZ9aJQhlRXqHH9kSMwWhaHoUzcK8qk8UMVNuImhW91EzoQe3P94X7mZXRs1kFQYFRUuQokUE7YNahpNE0DigGrblsQDy0K1J09t2eYE1IkSRSR1USPPe43wHp1PnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24162" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HStBqIwWwsMSWd6Tb8mOoIb-EA2UOQgNH5Hx7qgzG44MtaC45AdqR69Agg8KcGE3dbbmCkhRTePCG9CMclGWuE-0s5BXZUf5cv_7mgLNl7e9-neeDWtYNgvI68Nfqp8vQJ5mJuxQXoVWXT4EUsA9-jYaFuxGADgw2eShgqH90L5q2-ujzfkU4zhOzgIVdtIK3XoiQKwJheWWx9eZbU1ys1GsWEpgzk8Fj44eALIZ1ucAedb-EOuHjbfzXwvUMhY8tkWPWKsEgQCt-9XFQPXeRdcE6QlPVH9aSlX5Z2CTVDIktal9bf0HWYoc-C2YM5wMBN_awVgcy9xvJHgejuQIow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24161" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHBpostHjYrHBKMv2Ee3ldsuy3H9O0w-VkB3906YYXKWblHsEWD1vvur-Fj6kQaptw_nIqf0-0zNUAjs7K-iIP0PaPrVvRz4o1NI5Ajhl6aSHwZqf1zY25pMG72X66jTQQhUBzqBoDRkhlVmORpof-Njt60AehzDEAjCbsXIMsoCV6CSB5-FO5IBZ69ONJuff0HuX867bDuws0mpXj1S-zOVtAwfXWeu9qW9buodd3QslmDD_vEBeD_T4daJuNizD0YM8aL07PrPXmNYYPhcd-lyvp7wQApWC2IlFhV3GpNfBsI7PM7gUyQ7ulZ2J1GxTXxJzqZ_68rmzdR-wWumvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
👤
#فوری
؛ ادعای رسانه‌های روسیه‌ای:
بعد از درخشش دربازی‌مقابل بلژیک؛ باشگاه زنیت روسیه به دنبال عقدقرارداد دوساله‌با علیرضا بیرانونده و قراره بزودی با مدیر برنامه هاش مذاکراتی داشته باشد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24160" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0AJti1_daiTJrEkiBTZOOjXvEiB0YiOenXExsSZvXbCx34e6hsOXg19Sc7Ibxg8rVaTO437ptnTknyGIfb1R5D6-1qjIjwzUnYn8Z2zuhMmbc7ShF5VD0vZV_4PEKDTl8rpo1NtWdYX--bFDaUNJdDiu-hO-r8N6oJiUpY41dprXXukYlDTyo1lA7gkXERPhv3JC4QMSCBh6lQhIfT9siLssSTvJVM54qtvnYUXwtg7qQUJarhPhE_w0uwSphUmONzebByPRTSG3yuvDACjmn5QEB9CjXvvjcddU0YauYpbEXlKfKpwVh40HseobCebDjN-i9y4fP8Jti-vbjQUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24159" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0g0rstMRw6y-U74Y2Thim6F44L1Jh8WCM2xoz0rsiPe2xq-GPzYvIWX4PCgIDM3xRpPz8Tuo6KyOrYPrZX8WqWpoxe7EOyNnk9ExUhQc179p0a9OGw3F1uBW96cL8mJOqWW4Q2BL-REWOWkOqFEMbxqItcPnG_w-kE4qU_UdIQkNvekpEoEqvhMdapGDe39Zdedd6yBOlP48Cf-a3WuL4-wnR1D2X0LmkALyBgFOSHshtTJE0czH1btJ5ig6xRuQcIp72Z6k0GzQbr4ybCJ0vvf47sc-hGoZWQDTu6qQejSFwHYFD4DixOlk1_2kYRsuV3_AltuexQSwSZpBsF8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24158" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bu3AvPzM-T28q2xMkwXtyb3ueS5nc2ED6di6tXKAWbyohcNqZMN8WX2iMRJyZN7re6mBQ8uClpvzYVOup_zggyKcE4ruADBZavBYwginGtdK8NJYpMiZGmYU199bpH5bA1bX2hOiFz84x7mKjqLwBOS89aMAnqSF9acc44wqd_NH-HlLgSNx-fpd_6RPHokz5ZnNSmAZNvzRcghCqPtf_JU79Ni9BeQz4CT1dxh4IICH7HRLBz4Zl6fnFKrok9cY6Z_V4K8WfHHq5-UALspUroTpDaa1wuF-LbFDGBoibJFbub6Ri-SUi5GpebnssPihYolFQLa_de5fjlnuvyF79A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueoik4Jcv-Pj3e-Kz8bPK1Ry-8QXiqvCejBFTjekvZr_JPAgoTPy7nfYlW23mODhwnP4685ogK2p7V_XzjJPfUpV0mu6HPzr9mowHe8U0F90oBjUA48t8yn-kgvH-qqKSvSSN-qr95zgOMRGEaesRG4qCjFdSGdVO2hOd7ywWA8FLuFvTAYM0701WuhTCYP08K7VrbylwtleoRdtPozoFzOn8qKHPWIwfNzGSXM0o9DbrDTukByEG7w1rPo3UQ7GRa4GAwZ3IphQNAnvUXu6E12fhdAUomsKYl32qGJRVdjsGqCQUp1lHQb1OURMD1IYwTTBW3Ysup0MChcno_t6Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جادوگر تیم ملی غنا: کار بسیار سختیه اما تمام تلاشم رو بکار خواهم برد که با طلسم هایم غنا رو به جمع هشتم برتر جام جهانی 2026 برسونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24156" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2nHhyKRWacesOSRetu6utIDtYUxF7coWHhpREuUrAYc3IBLiArxOKYwqpNCeOEujNfotM1fqD0n7bg5I0X3BDstfrBTPMEmV093R-5BHGqre2mpiCmSvp9VUiBFnZeu5ciUhzO8vKyQUtVgbBUurIu6Nk04vAyDSgUnIh2o8pSn5QCnp4AAFLvDdYIvH0cyjkj7JrnxyV5rUquPfvFOUGh3y_w35MjMSSjhq3K5LPeLHxFTKD2EmiOJ6Jdb_zG91ot2isjV_zl2AqjSNvHZm6lXs_zFeg94HFXWEB2OOK5oeJJqmZ0juuJipESNoN7eh1kr7F28PaC0bks8-Xfmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24155" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=GYg3OgbTsnc3CKqYIm1kLxUxlQN3xQvomj2xtDHOiOW2gyhrbFAojUux_2I5sUcYslHOKhXequQva_nG-Xx_EvsHaSfFmeOPZj7ilJTEEAEYLJsMYqxyLvJlwJ5VWSve2L8nhInXsKrPOfc0FPQDZWegmikk8qUHvS4yBxbpQHuUI89eAvZ_EbWjR6_XY5myfBm8bYdA40Hmg0K1PQ6WMHMiH366iI190v-NfCJzs8zHSvheG8zUJI2UlcBxNGgmPjjqZtwm3fsLLC_LRmNe_6ZKF22Bw5d1mO8IzrHk8vluY5ai-7C1sqPmbOQNtFGp0YQX_P3NuNBarH1zyu962Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=GYg3OgbTsnc3CKqYIm1kLxUxlQN3xQvomj2xtDHOiOW2gyhrbFAojUux_2I5sUcYslHOKhXequQva_nG-Xx_EvsHaSfFmeOPZj7ilJTEEAEYLJsMYqxyLvJlwJ5VWSve2L8nhInXsKrPOfc0FPQDZWegmikk8qUHvS4yBxbpQHuUI89eAvZ_EbWjR6_XY5myfBm8bYdA40Hmg0K1PQ6WMHMiH366iI190v-NfCJzs8zHSvheG8zUJI2UlcBxNGgmPjjqZtwm3fsLLC_LRmNe_6ZKF22Bw5d1mO8IzrHk8vluY5ai-7C1sqPmbOQNtFGp0YQX_P3NuNBarH1zyu962Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ کریس رونالدو به جوان‌ترین و مسن ترین بازیکن تاریخ پرتعال تبدیل‌شد که برای این تیم دررقابت های جام جهانی موفق به گلزنی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24154" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QN58BjPG5TDeehp_bWn_jQDbZt5LrAlZiuAtZKQ8qETs0ZIn1whuAiH03RY5S29nj_x2VKI3DJjF00dIbwSB9uquNH-oI5Gq7SDfD1aoyDYTMviWpdnXqPk7KeHpPsmcaGKBTiGusyUR7E35Ej0yV9kOWl9mlkDLkO52mI9LyXSUc5Qu6tu8kfut5xn4jhNg8aWjsfXoDpKoz6Gdn_m0LfDocFYhSk072XW4ujJuBGjWOuA8R3jhAgmbTpgHaPhTj-Wq6DcYLl2aOQDP6J1Er0vfzizdoCjroe2R3v7aCOwor7X-6VdcKfOD_tF-L6SD-j78raz5FY5maF3DfuH9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
دبل کریس رونالدو در بازی امشب تیم ملی پرتعال مقابل ازبکستان؛ این‌دهمین‌گل کریس رونالدو درتاریخ‌جام‌جهانی‌بود. یخورده بازیکن بهش کمک کنن قشنگ‌میتونه‌برای‌آقای گلی رقابت‌کنه. این 975 امین گل‌تاریخ کریس رونالدو در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24152" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=OZTDrooaND6xsepZH_mpao0iOWWt0Ze2H-DoZHqBa4tKcGg5-cxCc27l4mOjCQ2-J8BIQTvr1MrqRinhiH8ot7plDeDSoN9iH3ptTj6AATuUvFBf6dmE4wymBm1dHywFhl6FemzX23tPg4AvC6HgisPfdC2Qt1zvLPTfOIOK3oQOeBlR43QsZy80K0DYyb7HYWv8UxygsnwWwvIDydVa66m1V133ZvbJsVI25zCQN0PzO_sYPtbBLsfV4PlPSBJA0U7wyjDQdFKHTZZ5whRKMF2WVIHkCHX0jgHt_yew4mtf3GS-0tnocSZSglghGlrKeLtNn53up3HuXgUaOztaVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=OZTDrooaND6xsepZH_mpao0iOWWt0Ze2H-DoZHqBa4tKcGg5-cxCc27l4mOjCQ2-J8BIQTvr1MrqRinhiH8ot7plDeDSoN9iH3ptTj6AATuUvFBf6dmE4wymBm1dHywFhl6FemzX23tPg4AvC6HgisPfdC2Qt1zvLPTfOIOK3oQOeBlR43QsZy80K0DYyb7HYWv8UxygsnwWwvIDydVa66m1V133ZvbJsVI25zCQN0PzO_sYPtbBLsfV4PlPSBJA0U7wyjDQdFKHTZZ5whRKMF2WVIHkCHX0jgHt_yew4mtf3GS-0tnocSZSglghGlrKeLtNn53up3HuXgUaOztaVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24151" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c38410752.mp4?token=IcqTkpADHTNTQBmR0n11Euu88_IlZn86sV-zX6PfVAgTeOepFWC1_Bz3dgsAPqE-sznHkumTMALCh887WnoTT8PCCaZnaB4_k_z86BgAbMXNVKg2ErfWMez44UCP1u3lD_LCw-ha9X51DUPO5o2S-Kv5MGomIsvQOzTijNJwJZz-YaXyrNNJTAZoG36p26sNSWhXJpT9V1RVSYdRiGXZrl3lWwBJW1U0wER5vXMAecNcgIeY4ArY9GZoLZeRj-gx7Mnn87gPhs-qwzHCqZ5oRxBt9cUXekt84KTvGqhY-c1ZGXCH5q2ZIltw1_D0QbE7XRgiT1r19O_fDzwM3P5y0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c38410752.mp4?token=IcqTkpADHTNTQBmR0n11Euu88_IlZn86sV-zX6PfVAgTeOepFWC1_Bz3dgsAPqE-sznHkumTMALCh887WnoTT8PCCaZnaB4_k_z86BgAbMXNVKg2ErfWMez44UCP1u3lD_LCw-ha9X51DUPO5o2S-Kv5MGomIsvQOzTijNJwJZz-YaXyrNNJTAZoG36p26sNSWhXJpT9V1RVSYdRiGXZrl3lWwBJW1U0wER5vXMAecNcgIeY4ArY9GZoLZeRj-gx7Mnn87gPhs-qwzHCqZ5oRxBt9cUXekt84KTvGqhY-c1ZGXCH5q2ZIltw1_D0QbE7XRgiT1r19O_fDzwM3P5y0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24150" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=StKN2FI-lC6HM0f4o3_7563UjgBGXjyJaf_1bN5UTqkxTw-FvkO8OHn0Wno3oWGva9noNBW3VFGZPGLTnV_Folanm_3JKF84Bk01SADko1wutz_oKjI_nIOqPcBTTADZ223yMm7mEdYWS8nBY5boapNsxj2rUyAo_UyVVr_1PaeJSNhOIzlyTWXUC5ADvydJFbUJQsdD5NOKULo3Q3p3qgrUu9OgHZOd2pysuMchNB-SWDKqdAql7DgdIlN96xw1tYrk8AXpnb5dssA8w_kAxKR20NcB99ywI24nvtf3H2LOl3gyCLY4rkq6Gw2JE-C6HcO0iq5JZb-raPriIvvLLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=StKN2FI-lC6HM0f4o3_7563UjgBGXjyJaf_1bN5UTqkxTw-FvkO8OHn0Wno3oWGva9noNBW3VFGZPGLTnV_Folanm_3JKF84Bk01SADko1wutz_oKjI_nIOqPcBTTADZ223yMm7mEdYWS8nBY5boapNsxj2rUyAo_UyVVr_1PaeJSNhOIzlyTWXUC5ADvydJFbUJQsdD5NOKULo3Q3p3qgrUu9OgHZOd2pysuMchNB-SWDKqdAql7DgdIlN96xw1tYrk8AXpnb5dssA8w_kAxKR20NcB99ywI24nvtf3H2LOl3gyCLY4rkq6Gw2JE-C6HcO0iq5JZb-raPriIvvLLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24148" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzxE7oXvs80YI04v2HMj-WHYcOStyR5Th2DqW0iB_qIWbTN4nCyMQXoYqXff3iA873U0jURv9bIiQLGaPAjXwUbUen1w_LQloh63_nm5sWhD1ZL_0S3BqkljyaH-HA3glxwpGn9zD2t6lCsI9fSCoO5FLZg5CT7bu7at3x7b8aYne6pZ8eTw-MnM6ovFfUBd6eVTFq8uBtxh3vcwzdgcwFvYp7jzvA6REoudNRjk_AchM_EQzf2EMioDDZKvFNzVSWQoKLN7Tj5vUQQpfpEhsa7YGLFFzP2CyuANvvqzHnr4eEAhX0XG27gHDaW7TlzCSzEujye6ZQEonGn6F8gH1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24147" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SW9tCfltJS_QFEp7jsPCaP6Bo2NV5abSeu2Nbp6g5zLgDXjpYanAL7W0GpCMXB8uiOxqfvGbiNNZG-wkhDjazp_uMpLNzlSaFtV3ZD8BWvbX9vy__NgJpSddJdFgkrh6ynNmV_OzJl0umFi6zFodnv2bY2XUh3GvtsZwoay8CLLcbQsGbgxhc2TylA5R0QZelcQxjgvcgyRhsI0SqXHoCg2cTL1LYvUvegMcGls_WEAPxFkideUYFldWRomFHNTFVr3nrfdghevxGiRc5kzSTvLDSu2S6qbMuOLglpCVSuEQrq6JBQ0qCDirrjSY74nG3n-cCBYFpuDG7H68TeF3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس دقایقی پیش نویس قرارداد رو رسما برای دراگان اسکوچیچ ارسال‌کرد تا باامضای آن اسکوچیچ باعقد قرار دادی دو ساله سرمربی سرخپوشان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24146" target="_blank">📅 20:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAVXvkPY5u0dgrGoUoJ7MBFmLO_jD9VQZzBszMWg6cJpRN2JUgK9NJTrL4-V7RQO9uzawKHl6PVsmIEQktT02xHVXtz3U2-5-XE515n19FitluXw7148OgawgtM156wzlswKtF8rN25FJ6hBfAcrfZWWhO8mqL6PXefw2qtdOJnRzDgafWhHANv87iJCPszNgtpJF04wTSbDpp1pRlsUAXLVQNQbbPs-tazTh9uHb5OyudCmXgmOaOwRlwMkC53hmlt6C8QoebNRWCA73yzS69vBrc_OKHdqCFBpIZwfvKHwSVXtAtghemXKnyaK2HmwS8hzqP74xMGkCU6hYaPBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا؛ باشگاه استقلال امروز باارسال‌نامه‌ای به باشگاه شباب الاهلی امارات خواستار جذب قطعی رضا غندی پور شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24145" target="_blank">📅 19:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jB-1NnY01y_JLgjfWoc-0mLIUOrenBwI7kutdkwg4P7BzVrQEGpGOaFXpTWzBY3ofBSNI0hen3QnUH2UAPfFml2cezEWB6pYNHNrRiSZbTTb18G47zUKh4H5DwF-cQQsC5ympfv8lQXakjNlqnMmvi--21tME6kWRAbuDdsd13L8aYLRxVrMlXs3th0FJXtBGYFDNH16y4J1INPNrMVxpOqCmyEgmlhJvPuopcsTw8TtcZVLR-78mvH_OMdyRtbKutS9UffIAaaUscpX4gpD6IHeerMDBHzwr8P8NvuxPLKgH2Robfn1FE4ibwotjgu9kHe8jdKP65qff1QCpOytCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vf_zmA4kA7a0f8gPsUaB83dkHjL7v2vJpSXFgq47Eysx6TZ1uDbsMLMllm0yKJLdq6N6w1bQTg_d5-WUOLk00JUTKgnrEIrMtQjDAIZIS5PGt-9_09CCspPOBoU3XhSuNcUb-IGH7vpXYUveO-wKnthDc9ae1RnVyXzG_0ua_8ChKMZa6gI6NIGkh3ZiMk7fFiUInfTHfm4z_ywQjE4GEINDxcld-jUPx_PRSOx1CvFjnqv3lrMmn_tNb9jLta3IeuP62PQSQS2wXp85VOd7BWnxOeElWByAUZn8kgOenjKa8qPJmB0SVs1TVv9KYR-h_bT3yGnZt29GwXYCY5j_UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24143" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJZnkhN9YDlvqSN8OGEVOIxZYT7m3ruqYHtxDyii7MiwLKG6eQV-M9veApQneMSyLlf_gOG57H5xNnUMtEppp2CINpPtMpdjjnZMNKuFLiAu8TJFPH785xHBm8MuDZ6p0e3Nv5KVC7drt6WYEBRJecEr2lazEY9YuZpXqEMRteUgf48jUmJO6gPEGO3djm0VY4z_X3n2qwsRIlu6envw9VP_Ezx4enGwMGO-nXnCIxWyh3pquMlJTmAWrwYQ1rvTUhT-gxoiro4YS4gw2y7_t6rCCTKDXBDNgiClFJgFgNJBq6kzzjsS7YbGPLHrfb0mTzWRK0wXsPQiJyh4t5MF1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24142" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=jJzO8PII9AKaTMFpS8YEUK4AhyX6mOgZwMzAv-_NjArXevlpI3Tg9L5l_YFHrAIVjMrAH_rLMumoNXdOWQ54J4zEbGhe-b5UiNano7JKSZu65zAOt-ly7Fr1pXwe0QPwxuieu-SojR76X2Dt8psKj-mpsodgdBCA-lHxI5Pk4_EZUNRZ-FilNWufnlDDhkv0USVRYFeBzGreXr5sScot2PRvxwIfwBEXSM-4xJ3ggkhQgtxXrzPzM1xaK3Gd8t7qS-fEndkr1OtFjhYP78L0S2U3tWBUr4th_CI2o8R0b7-8unHQ-fLUwP1AzvjRm6AmehyEAwdd5AL2pxheBR0GrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=jJzO8PII9AKaTMFpS8YEUK4AhyX6mOgZwMzAv-_NjArXevlpI3Tg9L5l_YFHrAIVjMrAH_rLMumoNXdOWQ54J4zEbGhe-b5UiNano7JKSZu65zAOt-ly7Fr1pXwe0QPwxuieu-SojR76X2Dt8psKj-mpsodgdBCA-lHxI5Pk4_EZUNRZ-FilNWufnlDDhkv0USVRYFeBzGreXr5sScot2PRvxwIfwBEXSM-4xJ3ggkhQgtxXrzPzM1xaK3Gd8t7qS-fEndkr1OtFjhYP78L0S2U3tWBUr4th_CI2o8R0b7-8unHQ-fLUwP1AzvjRm6AmehyEAwdd5AL2pxheBR0GrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه ابوطالب حسینی به مجری شبکه افق که به مهمون‌هاش کفن‌هدیه‌میداد؛ فقط خنده پشت صحنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24140" target="_blank">📅 19:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMDmOxaCbv46-uIVCd2ZydxsXDum8haCDyGbMEhUOH_n-cH1sA4I2sqabDeRzAH4pk7J48twDK06csad2gkpj1u3L7V8PokMsyYeIolsi0VWB_iPFgnuCFAKug89c9uQlYVwE22mZWXA87I8aG1X8FzWx-HM2mvriU7xf6z4ejMgT1qJOlD0TQVXHYMqLwXsKjfvXoKui0P_KWdpUolCvCJ9r5I3dCU0S0481LEIRr6rBwtoX5rDoSOEfMzCoFqWvdkbTCshjp3w-FiGev37i20QEeONDcG7sTOPKHg-YTQ5Dht-nqXPL-Rly_IWuaEqLk0Us1wjFxZWPTi-YWDMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24139" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3-gQRBXCgiCDtDAcSiWg388gPmC0gfQ3f05Oal2wM5AMX__RO09hke_zSNdO1qMw8Tlv13glTHRhduwQrsTKxOO8Zer5tIPOkILpR5DjhiPBkVxEP6X9OZ4ivNdAICWMmFdG94p3L8WcpBRyKFhLblA1oOrZzp9but3q9yduORC_vbzS0VUzAa6lNKYWtM-1RNCXuBIuaXxWjZ9E5Dhdlj2RTQlbl7ZrHyM876YrzVtCB-Az4ExgEFBEzKF33Zy8SJ-J2fEbJZN84AkI9H7heg78KQcAt0H3HG-WxuBR6JNZLBmYJcNvbS5sNBCnJ8zBQDihXGHjgDS3AIAFtnISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
بازیکنان‌تیم‌ملی آرژانتین اینجوری از گلزنی لیونل مسی خوشحالی وذوق‌میکنه. از اونور کریس رونالدو گیر یه عده‌آدم اسکل و احمق و تازه به دوران رسیده مثل ژائو نوس افتاده. وقتی رونالدو داشت تو رئال و منچستر آقایی میکرد تو دهنت‌ بوی شیر میداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24138" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSJl-NDo0nVg0pdhlRgYk16JsOmtJEwW3i-QWCTNbPjBz6BJudRDgD2NaL2cFCRsnklKGDzXyTv5NsvQA31fbTaoc2ewVT5S1ko63bi5SEhgefUuunYUJAmPc0di0vV51knXC6xvpRAwfLR2u-_11z3Ctw4XOcxz8JAfBL7_93yK4A9AMpJoXqz6SqBWiPHwN-gaW_CEp7r9LQV_-ZPtIJvtAcQEPeUSEnYLqavmq9wGA94JvH7s72aZAObewJuxKi3gGXCop0zQrpW5tVtNv3OEp4STG5Py1BXClJX_K9bqNr4OTL9TqBOBLUF2cdUC8Vtfc4C0s4lZd7olu9spUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال دیروز با ارسال‌نامه‌ای خواستار جذب یوسف مزرعه وینگرچپ تکنیکی 21 ساله فولا خوزستان شده بود که‌مدیران باشگاه فولاد رقم رضایت نامه این بازیکن رو35 میلیارد تومان به آبی پوشان اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24137" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUeV1KEqEDtgkDr_QOHxJ8ZDxUssq1MkyOWNjyjiTLyqaaznzzPR8xYiN3F7TL1JBaLY7vG4WktVodcEAijeWjupO5ILli82TGTe_-I0GNNvlrcDv0vuBDLCmmpU5nc5eCZ7EWPxhqdAqG81U5yIpNLPRdROoLQ23Zs0VI8HNHbiKoxvf-U0LuhLZcmq5TbkPtqqIZSl3cURepU9juV7ZBbYJmVR3rSe1dVqOymfKc7C8cBw9fB4TuDBUoBhh0wgT01-IC9CViyNnUg7IrhrmU-w3YnBTpgYQ3FqGsG_cH9suYBQRGiRETNiO5EvlNcJKLHxFqEhTMq-QvRzNqm9KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24136" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBeBclUPJrQp5hPcTXlfmep_1yT2hJccqzkt0y4KgXJLF-cdrwznkiDJ0YtcJ4ZxG1P86-8cXO8HEkfj085Kl2N2dXxWE2857TLMyfYkFyGGYIx4P43De1R2uI618V8v2ZH8GZtz4guDFczJiNJ4G7CmmzX3Vn85ok7ex1NjrHxBjVMQjcS7gJM0aPXbudSKykCmLUXjV1N21oA-GgXzvJVv4p9fMg7HFTmZS3TWHAGX8XD77oTTBj3Sj_noxCYq-3ZNQ3-natBbtgbR00AGHAwKHqOvZVM1kjARmDaOsTRor8i0R4BD7HdwFTAR_AMSEDXBP6AqUIOOSDo9zDxi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24135" target="_blank">📅 17:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml7p_Xx5yBIqyAT0IruJ8YxFEtTk0v0DxlWafO_LByVqPF7fCb9r-N9KXEBzaKenas3IZ-cswgDkPaqt0BP1cxkxTgng2DIi0gW5NQClExFqssvSGYl3bTRR6LZe_Jr0WZoH5dYjRLg9fWcBeippKgmp08slM8_ipk5jO74nfCUSwnAZXcuk8W7kV8pu-y3DbUuwnkayZIcmLxc41zxNEJpaYYJa6qU5CttAgmyzFQlzEjjsYm6LWcVbEPVyIotT3sdquiaObS2w1kb740HlzJPBUwN-mOQkn5TED-Uu15rT0D6-bRu_KuIvKQuRDwrKBGGURWnWSj0K8NeMXw9Uig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24134" target="_blank">📅 16:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇦🇷
🇦🇷
تمام18گل لیونل‌آندرس‌مسی فوق ستاره 39 ساله تیم ملی آرژانتین در ادوار مختلف جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24133" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚽️
تمام گل‌های روز گذشته رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24132" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=vJe9CN5gDGVNGaKAjC3_UNiOTx0VI3XbL20IpsMUH-ryQWXNoMSKeQ3QOFc5YkpIpp5y56TUJ-WiEFxvV09jOUMFwbWl9uCUy_ACWs-v85YAoHLNH1Kb_fOp8xf_v-aqkeiapoYJwtwb7g6KpAAwAdLcmE1jc-7Mk9oov0BLFS5-w1u9aXVrZDx-qfe5OuWpCKKrcOLfTqVLDortGHFMBAFbh7-SHbfzuxL1NSGPUJhpKyz_mjweBfhjDHJ8ATq6td-zJH-VHqZoEzUiNHIAw6sM8Ab7ruStPtQk-qw5M1oPNBlvQF_0TGb5SH4bB0qgySfw45n_ceLElrHgGxApaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=vJe9CN5gDGVNGaKAjC3_UNiOTx0VI3XbL20IpsMUH-ryQWXNoMSKeQ3QOFc5YkpIpp5y56TUJ-WiEFxvV09jOUMFwbWl9uCUy_ACWs-v85YAoHLNH1Kb_fOp8xf_v-aqkeiapoYJwtwb7g6KpAAwAdLcmE1jc-7Mk9oov0BLFS5-w1u9aXVrZDx-qfe5OuWpCKKrcOLfTqVLDortGHFMBAFbh7-SHbfzuxL1NSGPUJhpKyz_mjweBfhjDHJ8ATq6td-zJH-VHqZoEzUiNHIAw6sM8Ab7ruStPtQk-qw5M1oPNBlvQF_0TGb5SH4bB0qgySfw45n_ceLElrHgGxApaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
زلاتان‌درخصوص‌لئومسی:
من تو دو تا جام جهانی هیچ گلی نزدم ولی مسی تو دو بازی پنج گل زده! براش‌خوشحالم‌امیدوارم همینجوری‌ادامه بده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24131" target="_blank">📅 15:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KknbJbnBUkCTvfOlXJeRaenzyacp4g0I5M5kXLputEC1_4HVit9dwhUtVSU7ViUpvgpGRA_aLjch1DW_YYKXYKg_mBGSGL6ft0cm5ldrHzgSH6LyTrQvP0q_QZcRWUo6WB34qSr7R9zmsGgyAQdysM5p3Lh0JGSpwUoqyo7N-471lZ-d9-y9a_Wlt6Oxd2bvd8Q5Y7kRByECckCihhpDMZwZo4kMZA9cJqxgibfb3WrNGvoilecEDB-BT74_UPM5Ya-wyHstGGNx6ZSPPebiy6JGpBKqBTAotbJbL3WECLETGOo6_OESpvZ4Br_o2tB2vwcWSqvRqeA2r28GRPxXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
فرمانده روبرتو پیاتزا درتمرینات تیم‌ملی والیبال باقدرت هدف گیری 100000 از 10؛ عالیه ببیتید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24130" target="_blank">📅 14:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrZhBmY2TMiAyuVML8LJcI6vJdptqCA15mwy_rWy0CJKUlTqBIFXx5a68lw-g1af3xnDoZS31qLTmNqCX-LRoZKI1Z240qRwvPzM7GwQhPgsTDLhLiiyALDDvscOijDNUIZbtzjVNqBKk4Py4Fue-4EmXxFNm6VINcTkYEAsvFZNBy8j3lW1wKNvgtsroSwpqp-TMTByofQVDyzx_-XEBnj5qI9CrybfFazObsOXen-1BVKM29HeBCsCz319oh3DeivO7YOLvHipHZKJ1fXNI8Zt2SOytzWlM2MwG0U4BECR4EPueUahz2ehkzpTB-qVn1PO5M9sgkniytvSp-A11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24129" target="_blank">📅 14:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_W1NoZf84CMb6-qySOE1d4sf_wkBkm1OMOnbA2Ag9WvxHj1Wg0uL0w8Inuttw3ZLNdYl4cEH7xo0_jcB32c6Gi0ovyi8XvvVW3RvA_lGqQ_AIudFClvGesWd34KprI2JXplhLO7L3Z40st10hy-5ozlPwPWBBtwhq-qF7PsJgL7JGf69fNTsOskysaeW1O7JnFRkPuPqXVkpcYMQbQaAn-LXD1YUzIG1kZsOTjf2ssO41yY_4G6b4eKCwHE-9pzl8gZLsvT31Ecr3f0VTJEZb96YSgdGGDvFLqxXptz6q422bwsq9WlFLFnLuAOy_J9GwBtPoVHvK4GGi3wcELQHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24128" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=Nx5lt8zJ4O3tMnBp43Z_03RF4tMwB6ID8J0Ic8nIslRA7emlAADzXxog55uLCqrdSJB9Bmb09ypLOszgDdQcJw3KsFxEL9PXexfbzKNLeC4fM7833vuVzyiHGr4ZNSzlwBqNtvNybW6oCsfqFrzi64axfzov7XwwBYa-NCxFDfx3hESddfnEizhgcubkWnrnXAiNehLFcoTz2g5jNwtDp0_5BGkVH8T0kFfd5xUS30BEgn-2_QEK2mfzjDZoiwqPFerjz1tZ_dG8MiEX5_cLqAnxkyyLGQzjvJaLnBf0t1bcxdqbVjR5wCpTJ2VoVOxKamHxIENpj1o-uu5VKDUWFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=Nx5lt8zJ4O3tMnBp43Z_03RF4tMwB6ID8J0Ic8nIslRA7emlAADzXxog55uLCqrdSJB9Bmb09ypLOszgDdQcJw3KsFxEL9PXexfbzKNLeC4fM7833vuVzyiHGr4ZNSzlwBqNtvNybW6oCsfqFrzi64axfzov7XwwBYa-NCxFDfx3hESddfnEizhgcubkWnrnXAiNehLFcoTz2g5jNwtDp0_5BGkVH8T0kFfd5xUS30BEgn-2_QEK2mfzjDZoiwqPFerjz1tZ_dG8MiEX5_cLqAnxkyyLGQzjvJaLnBf0t1bcxdqbVjR5wCpTJ2VoVOxKamHxIENpj1o-uu5VKDUWFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جادوگر غنایی: هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24127" target="_blank">📅 13:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RldB-qBIv2HDwY-5T1RN5DZx2Lf4HqnKgu1heJt8j5xb1mHmFPY7cUMdwnnZitgV4-5t7KbrfHILWVN2WzexPqRGqfLK7psCeiL3L7XuVjyre9SQbspmmPcaE_WtpNkwScjb7d4EmIo4MPueCiWtUiohdAhG51cZr4jVG6p3A5rKtAQNdSN3uShwM4rPVcDwz4xeLAGyScTLr-6Pg_3_VFnJKE6xvmPlPItD0KbHBznWtygZvJH31--9VQVeKDtaFfEtZy8rryQjMMPq_jei7UtI94e6ecHsf7zh0HpmJRO9smMAXRTuyQbVDkBvwmYdTudYJoXk7Z5ZjftFF2swhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سه ستاره جام جهانی 2026 تا اینجای کار؛ رقابت برگ ریزون لیونل مسی 38 ساله با دو فوق ستاره جوان فوتبال جهان این بار در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24126" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8jI0bWFHbswv9cNNn7R9jJixqw4wAMB6W46xerHgO_ugC7ntKbc0ZvB0fVSK5fLJesIvgXrlkka7B3wUMu5Cl_8iV438snbrv6bk0QWLupSHLFrEg2fTFAS1PC0n7Jce08GYW7SkctDn3eotHPwsuONrIebkC16r8pY6spbWvE7Cd0kA9_kY6vyNt3Yb-AvPaNVLBT_wTrLLu0bmIEXjUv4zMpqd7Fa8OEsmCeBZQN2N4BpfzcNBrBRt5KdRZlpbbKFtDN3nmIqt2SXG1Iqt9U8w8wXcwp5Issy3UgGRlI17k_ezivMzEw37pn0JYoat-kNF7tw9bVPKmgKabrdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از خبرنگاران در نشست خبری قبل از بازی انگلیس-غنا از کارلوس کی روش راجب باخت سنگین با ایران به انگلیس درجام جهانی 2026 پرسیده گفته اصلا یادم نمیاد. مطمئنید که من سرمربی اون تیم بودم؟ من یادم نمیاد به انگلیس باخته باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24125" target="_blank">📅 12:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwyEt9lUIo3GA7ao-kGm6KVFWVsl024hxgKsSbSK8k9mL3ivgbq1mYYBkCeyKSEgEJE5dndkdzoR395EIPtuMu60Tu6pXxYCuDq5IkJaz0HXvN-2jrBsemeyVfJ9Ozn_ndcW-jDZpm7j_Tqd7SaUot1eBgy39IAqBaPi9m7B-WYFvDklr0v9H3GCdGt1muG3Jnrf0dDYrfvqwBWgsdSh7sRpWNFHZA93EB12cWYC353db8cOySk12nvyRE3vGfqYwaJPZIFjYr8D4rzdN_Yd-SvSD_yC0fk4wWz5GSpuFc4HvB5d6fUmPkYreSZr35HnOkGgBhhT9dnak2-fm2NNiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24124" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
