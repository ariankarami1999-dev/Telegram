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
<img src="https://cdn4.telesco.pe/file/EqFI2UokJEolmIbK9pNbdtcJ1NZQQurgw03JUc5bzQVSn_7Zw_QFba2wIJaBfJ4Dv0k93QsTHbAUtxGlBPqQVt_3WYlG7Xi7sUmGrNWCYv6NTq6nIJk6N3eCwif8MSSwIUQTHeUQMsmzP7OQtVLvzlCVg0REnEWNabnNRfu6mwB3l9HNUZnogGONSsTN8RrhNI11N0J-I3HRGz7ouemnTT_TLadha9vbVlJHoXtU000ed42pKxxQWhs9hibs1eOyvTN7i_kri4jx4xX28LHZDSerfA9IUY8TJKQG6xVJlUFnos2CmCmGHNIuOiOMbkTnnAWuI6eo5mvl9-jDZf5aqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 925K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 13:38:29</div>
<hr>

<div class="tg-post" id="msg-132468">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اروپا: شرکت‌‌های هواپیمایی باید به دلیل تنش‌ها از حریم هوایی ایران، عراق و لبنان اجتناب کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/132468" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132467">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ: اگر ایرانی ها سلاح هسته ای داشتند استفاده می کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/132467" target="_blank">📅 13:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132466">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d24ddfc6.mp4?token=jJYMhngI-gu5jUYmha9yVxB-zgHy-SXOjQf9PuGTyPp_JasR7B75a8CzASouPi61rdmUMvyTZRz4XQaLjlq57mksZ5lDFoQr6yoNL_-sgb_IAxUzbaffkIvU6fWfRFKojEfgwlDMqYmBrZzmnR1NWTKLRgVfCS7pOSrtTZZtDfR_qllJaUlF91XdARPXMjAG6lER3g-eKI_6nTfs26mIhCuOoJerSAZxEFKwKMv_HMd59nA39Fwu6tZHd7jHEEjKEKEgfpeqb9SU2a1yGZoaDgdwKaduWA1M3SZOGJfVreaH1693Qm5-pUEs5UDrKCx-ufiKDHnB7rAvuiCAhyLVLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d24ddfc6.mp4?token=jJYMhngI-gu5jUYmha9yVxB-zgHy-SXOjQf9PuGTyPp_JasR7B75a8CzASouPi61rdmUMvyTZRz4XQaLjlq57mksZ5lDFoQr6yoNL_-sgb_IAxUzbaffkIvU6fWfRFKojEfgwlDMqYmBrZzmnR1NWTKLRgVfCS7pOSrtTZZtDfR_qllJaUlF91XdARPXMjAG6lER3g-eKI_6nTfs26mIhCuOoJerSAZxEFKwKMv_HMd59nA39Fwu6tZHd7jHEEjKEKEgfpeqb9SU2a1yGZoaDgdwKaduWA1M3SZOGJfVreaH1693Qm5-pUEs5UDrKCx-ufiKDHnB7rAvuiCAhyLVLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخبه دانشگاه شریف: تنگه هرمز عملا از دست ایران خارج شده و ایران دیگه کارتی نداره، اگه شروط ترامپ رو نپذیره کارش تمومه
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/132466" target="_blank">📅 13:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132465">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
والا نیوز عبری : ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/132465" target="_blank">📅 13:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132464">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
اتحادیه اروپا: درگیری‌های آمریکا و ایران مذاکرات پایان جنگ را پیچیده‌تر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/132464" target="_blank">📅 13:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132463">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
اردوغان : با وجود کارشکنی‌ها از ترامپ بابت مدیریت قاطع بحران ایران و پیش بردن آن به سمت حل‌وفصل تشکر می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/132463" target="_blank">📅 13:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132462">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزارت برق کویت: خطوط انتقال برق به دلیل ترکش‌های ناشی از پاسخ به حملات به این کشور از سرویس خارج شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/132462" target="_blank">📅 13:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132461">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
اردوغان : تو غزه و لبنان، همه ما مسئولیت داریم
🔴
همچنین باید با تروریسم، در هر شکل و هر جایی که باشه، قاطعانه مقابله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/132461" target="_blank">📅 13:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132460">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نتیجه نشست ترامپ با اعضا ناتو / ترکیه هم وارد شد !
🔴
اردوغان: ما برای یک عملیات احتمالی پاکسازی مین در تنگه هرمز آماده هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/132460" target="_blank">📅 13:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132459">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
اردوغان در جریان نشست ناتو: «ما تلاشهای دیپلماتیک خود را دربارهٔ ایران و بازگشت کشتیرانی در تنگه هرمز ادامه می‌دهیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/132459" target="_blank">📅 13:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132458">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPUkha_7aKdg2tsPlv2H_BZdXDrzzIcHjY1kPQ72Ovp6-E6OZOj8TizAFr8q0qaNu7bm6zavs5ndOPri98hNJQy7_v3uIMkqf_73VyTOtxnTv0k3V-_cR-3aXA5VInnqHL963Cqm9-9FO3kDfrLZ-xN9p_Uzv5WAFBlIbl83YZHhtlroifbGcurJRw-L0HK2y9-ebOkX6gQ62focpWDOMzmWVafK4duacIjKeAPevlJpVtXUT-tGj1wgJ6ox8THrV--BfEomJKEPMbK_3sZncaiFtahf1C0UEl8LWFeZrKtSfNJ9L-ThHUxMqpMlooP4zTGAwipUtm-Mc3WSSAkSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت تتر در پی تنش های ۲۴ ساعت اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/132458" target="_blank">📅 12:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132457">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef22ccab1.mp4?token=WwO19oreYj0T6g1yvBvjOpy0vdfV258gZhLkzM2qJhzNe84S9rRsfn6cJWqQEkZLHtf_TUKEvRp4vsrR9E4HLlPYzKrPVD5187j6M1s049zLyzpsxFnjDf75FpMJkI-gO-xhL44Ye5gG8DHDzaHp2vARfCFwZqQapsMRelJNs4wtx8o3q2Wz6eponRCtOVU5SYGmadrCie8R_ZaTEmYEHKC_UjiImQElPSZs38Tz9xnzVmkWN9_zWLBWJhWgdm9OvSexrwlq2S_41xWdaKea3iKMtdJQq90ZAMG7TdmUMfZV-SQ0Wn1wgyUojWnUKTo9u5rW3O8MAJ0ffcZefR2HcBo4cFTwfcUUBYggdgJilKLfsAF9mzhe74Xilf04URQ5XT1lOZv_RgE9TBdhqiJdeR05NmMxdxdYloVS0R9_zsBUQX_nkYqo0f1w3DAphz36Y0gqDHwG1Few2jh1pnhnJlvdbqHVP7NG9MK90kCOO08U0dhAOKUZHN17dTRy6Apvqn6uAvHMhPM8sIFLDgJXqiUFtAUBoXZmEgfqJiXcBOsh2N8-3ijoSndmLyrq7y48IXQ4uOSKU2vg_jQVFD99ltBS9QYoNtMxkSgvQQ-bCgkS7_Z3_GSk7oQl4QcbVgu5gKFByZkaLzhBnSMbrv-aEqAqtgX0mJWvXQBNKDKsNbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef22ccab1.mp4?token=WwO19oreYj0T6g1yvBvjOpy0vdfV258gZhLkzM2qJhzNe84S9rRsfn6cJWqQEkZLHtf_TUKEvRp4vsrR9E4HLlPYzKrPVD5187j6M1s049zLyzpsxFnjDf75FpMJkI-gO-xhL44Ye5gG8DHDzaHp2vARfCFwZqQapsMRelJNs4wtx8o3q2Wz6eponRCtOVU5SYGmadrCie8R_ZaTEmYEHKC_UjiImQElPSZs38Tz9xnzVmkWN9_zWLBWJhWgdm9OvSexrwlq2S_41xWdaKea3iKMtdJQq90ZAMG7TdmUMfZV-SQ0Wn1wgyUojWnUKTo9u5rW3O8MAJ0ffcZefR2HcBo4cFTwfcUUBYggdgJilKLfsAF9mzhe74Xilf04URQ5XT1lOZv_RgE9TBdhqiJdeR05NmMxdxdYloVS0R9_zsBUQX_nkYqo0f1w3DAphz36Y0gqDHwG1Few2jh1pnhnJlvdbqHVP7NG9MK90kCOO08U0dhAOKUZHN17dTRy6Apvqn6uAvHMhPM8sIFLDgJXqiUFtAUBoXZmEgfqJiXcBOsh2N8-3ijoSndmLyrq7y48IXQ4uOSKU2vg_jQVFD99ltBS9QYoNtMxkSgvQQ-bCgkS7_Z3_GSk7oQl4QcbVgu5gKFByZkaLzhBnSMbrv-aEqAqtgX0mJWvXQBNKDKsNbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سران ناتو در یک عکس خانوادگی در جریان اجلاس در آنکارا، ترکیه، حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/132457" target="_blank">📅 12:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132456">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZD12wwMtjnXcltZ6rP-ybbUyIyVNUIfi5oR6ag_LyI7_iko9bRUuowVr2EK9EaSbxcHQ_U4GBqGkkzLaWngXnr9oravf1uYuUJcIi9IXVl9XySBObHKyUUtkF_Z-OiuMzMvr-elVEmSDPHuEjb3s0kixVfSwdN1SRvCRwGXWkLqYsVQwuU3Ktm4LP8GRvF5ISiAyrpsFfbdbvACRasdsxulEB2YQjwJ_U7TsgDntFg1u0mx8jFg49jQ6o77shoe72S_zPcTHTBxx_xFQOJnc0C3BQ5Ontemvlnf2iEMZJt51JtxjNhwCQjbA4uJZIlEfz1RfTAmOuS2W60cIzcIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:باید حملات رو شروع کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132456" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132455">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb87e8e96.mp4?token=KrhHHgC8PGKhaSiAHzo5OuoqCCdkLxOhKL06YVG30D47GoH57j6we6K9yIQ4tSrc1XAlFb1VpucRqJt8semIlQATvPuqOY0V0DftQV-0L139hqPESErFxYVfL7G-SGK8QQOTjstY0Y-RlHuS5l4ArxeTdjt9B21aO02HliflTt0fl4eju8TAe1MI-UJFQZGc9oFTi-v-ZlWuaqvoT3PS1B-T256Vfi1Ccdqb-kUqwqxMbo-_5jsPlzH5NwWFZ5iSSrJLWqW8bvoCyokAIf24rf9rREiRPjOMw72eJv6KRUC-d2XQ0d8WrBk6pEOZSeodBaGdZcV1vWx1-wfRQaDO_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb87e8e96.mp4?token=KrhHHgC8PGKhaSiAHzo5OuoqCCdkLxOhKL06YVG30D47GoH57j6we6K9yIQ4tSrc1XAlFb1VpucRqJt8semIlQATvPuqOY0V0DftQV-0L139hqPESErFxYVfL7G-SGK8QQOTjstY0Y-RlHuS5l4ArxeTdjt9B21aO02HliflTt0fl4eju8TAe1MI-UJFQZGc9oFTi-v-ZlWuaqvoT3PS1B-T256Vfi1Ccdqb-kUqwqxMbo-_5jsPlzH5NwWFZ5iSSrJLWqW8bvoCyokAIf24rf9rREiRPjOMw72eJv6KRUC-d2XQ0d8WrBk6pEOZSeodBaGdZcV1vWx1-wfRQaDO_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به نظر من، اردوغان هم از ایران خوشش نمی‌آید.
🔴
اردوغان شخصاً فردی عاقل است، در حالی که ایرانی‌ها (به طور کلی) رفتارهای عجیب و غریبی دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132455" target="_blank">📅 12:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132454">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
عمان: حملات ایران علیه نفتکش ها در تنگه هرمز را محکوم می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132454" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132453">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
العربیه: قیمت نفت حدوداً ۶ درصد افزایش یافت و به بالاترین سطح در دو هفته اخیر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132453" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132452">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: "من از بیبی (نتانیاهو) خوشم می آید، او دیروز حرف های بدی درباره ترکیه گفت. اردوغان عالی است - او به دلیل من به جنگ نپیوست."
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132452" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132451">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
کویت اعلام کرد که نیروهای مسلح این کشور، دو موشک بالستیک و ۱۳ پهپاد را در فضای هوایی کویت، بامداد امروز، مورد اصابت قرار داده و ساقط کرده‌اند.
🔴
وزارت دفاع کویت همچنین افزود که این عملیات هیچ‌گونه خسارت مادی یا جراحت انسانی به همراه نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/132451" target="_blank">📅 12:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132450">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرگزاری آسوشیتدپرس امروز نوشت که رئیس جمهوری آمریکا، رهبران ناتو را که برای حضور در اجلاس ۲ روزه آنکار در ترکیه حضور دارند با انجام مجموعه‌ای از حملات علیه ایران و لغو مجوزی فروش نفت این کشور غافلگیر کرد.
🔴
در ادامه گزارشگزاری آمریکایی آمده است: این حملات متقابل پس از حمله به سه کشتی تجاری در تنگه هرمز رخ داد و شکنندگی توافق موقت برای پایان دادن به ماه‌ها جنگ بین دو تهران و واشنگتن را برجسته کرد.
🔴
ترامپ این حملات را اندکی پس از ترک ضیافت شام به میزبانی رجب طیب اردوغان رئیس جمهور ترکیه، انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/132450" target="_blank">📅 12:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132449">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBx5Xy2bA4TnNNaCnctKqc0VvgDj4m3R7-9VPw4xCJHYmVqixHMe0BGxzpZwCNnhKQTSIJwT5Iq7pWIXXSaijH0A0kNWn3p9mu5fp35zPOODqlw9e3F8wbYr0GdkTZAGUac37bWx3iwbXBUZla8lKUQDC1KQSGCJqyeRhmZcn8Ozf9aeaYSaIeUtdBRorubLZCWPOqrEJD0OWpvRRbsCwmly9pPebgoNdnGzv6jUUQ2PClcE7ztgQSmJw5vKqVWCpAcHoMmZ8AcqMylGPAyvru60PS99xncNAMZuVy7l_lNV0MUl8FwJKn5ohO7JUx8-9SgFkzBIJq-SGX5gv835-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور سوریه، احمد الشعار، به آنکارا سفر کرده است تا در جلساتی که در حاشیه اجلاس ناتو برگزار می‌شود، شرکت کند.
🔴
قرار است او امروز با ترامپ دیدار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/132449" target="_blank">📅 12:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132448">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fopi1yRYOBpD1m9Ny9-_l7W1yhJoHTikit735xGSL6tCuEbVwkT5ySpkE4p_jftELEvnix1kQTH1lcE01WDXwvtHP62yfuCYZ6SSU-qE6VvU2hVGMQ7byAqfxliF2ZeohTbeJBvLE0BQVy-laISVPrxvo2yGcNtd5QqJa3MZ6xFAwLbpmTZU2s9-vJI_Rq91XHBBQxTSXQq663COvLJkLq9ysd4V4w1Gaxcr0SnKbFETBrIixT675A6knIE0owBEYbcSpo2GGMHEAHEgRTTX5DteTa3vfiR0S0H9iLPoCETS2wVc2taxsd-xvupRMsAsjKE-4uvUcxoa4GXb_bZH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان : رفتار دولت آمریکا به عنوان میزبان جام جهانی، نشان‌دهنده سیاست خارجی همیشگی آن است: زیر پا گذاشتن قوانین، زورگویی با رقبای خود، ایجاد موانع و تقلب.
🔴
این همان روش "اول آمریکا" (MAGA) آن‌هاست. ایران از چنین بازی‌هایی امتناع می‌کند. ما به طور قاطع از حقوق خود دفاع خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/132448" target="_blank">📅 12:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132447">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ: ما دیشب به آن افراد بسیار خطرناکِ وابسته به ایران، با قدرتی بسیار زیاد حمله کردیم... یک مشکلی در آن‌ها هست.
🔴
ما می‌گوییم: "بروید مراسم عزاداری‌تان را برگزار کنید"، اما آن‌ها به‌جای این کار، دیروز شروع کردند به شلیک موشک به سمت کشتی‌ها. دیشب خیلی سخت به آن‌ها ضربه زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/132447" target="_blank">📅 12:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132446">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
دبیرکل ناتو: ۵ هزار هواپیما برای حمایت از عملیات نظامی علیه ایران از اروپا پرواز کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/132446" target="_blank">📅 12:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132445">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / جروزالم پست: وزیر جنگ آمریکا، به دنبال حملات علیه ایران، سفر خود به اسرائیل را لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/132445" target="_blank">📅 12:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132444">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ درباره ایران: «ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً.»
🔴
او ادامه داد: «من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.
🔴
چون اوضاع همین‌طور پیش می‌رود، اما ما آدم‌های فوق‌العاده‌ای داریم.
🔴
اما این‌ها آدم‌های شرور و مریضی هستند، و ما باید سرطان‌شان را ریشه‌کن کنیم. سرطان را باید زود از بدن بیرون کشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132444" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132443">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ : فکر می‌کنم مقام‌های ایران بی‌کفایت هستن
🔴
اگه کاربلد بودن، ۴۷ سال پیش توافق کرده بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/132443" target="_blank">📅 12:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132442">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffb99aef2c.mp4?token=rKCR5haWzjyNeFQEM4Nja5-H9Ru-Iyhzgei0-vRXGK9YEX2bWkE4i9mAI57FwlJUfzTzPwIkKPiLISLqQxalS_4OwksWmQAoPUuVVHYkI8-kZvRk3Kuqjj9FokcknIjhyDyvJoDP5dB0vTk9qgXBncY3ZY8SvLagIy9A9W1h_gM-KRwxUndCBeiw3J76Fr6MdtrfNDGqMdQ6R9manpZqrV4nD5TBUQ-XoAQZGNUROLTFS2O12eF97duRIZnlVcHavqPMWn6SqX8DiIszzJOJyFRei7Vxb38Wr0W_cTEJH3qhWYxpC0Hja7nNTKX_Ops3Yz8tSQamjLZQ09as1KBwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffb99aef2c.mp4?token=rKCR5haWzjyNeFQEM4Nja5-H9Ru-Iyhzgei0-vRXGK9YEX2bWkE4i9mAI57FwlJUfzTzPwIkKPiLISLqQxalS_4OwksWmQAoPUuVVHYkI8-kZvRk3Kuqjj9FokcknIjhyDyvJoDP5dB0vTk9qgXBncY3ZY8SvLagIy9A9W1h_gM-KRwxUndCBeiw3J76Fr6MdtrfNDGqMdQ6R9manpZqrV4nD5TBUQ-XoAQZGNUROLTFS2O12eF97duRIZnlVcHavqPMWn6SqX8DiIszzJOJyFRei7Vxb38Wr0W_cTEJH3qhWYxpC0Hja7nNTKX_Ops3Yz8tSQamjLZQ09as1KBwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ آخرین آمار کشته های دی ماه رو 54 هزار نفر اعلام کرد!
ترامپ: رژیم جمهوری اسلامیه، درغگوعه، کلاهبرداره و آدم‌های مریضی هستن.
اونا توی اعتراضات دی ماه ۵۴ هزار نفر از مردم بی گناه رو کشتن‌.
مردم دست خالی بودن و اونا با مسلسل بهشون شلیک میکردن.
از نظر من مذاکرات و توافق با ایران تموم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/132442" target="_blank">📅 12:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132441">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ: رهبران ایران، بی شرف و رذل هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132441" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132440">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما دیشب خیلی قدرتمندانه به ایران حمله کردیم.
🔴
آنها «تفاله» هستند.
🔴
ایرانی‌ها رهبران آمریکایی، از جمله خود من را هدف قرار دادند.
🔴
ایرانی‌ها دیوانه‌اند، ما از آنها خوشمان نمی‌آید.
🔴
فکر نمی‌کنم ایران بداند چه می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132440" target="_blank">📅 12:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132439">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFAmDqYlhaWNvl8bjYsKc5MMXJcoBX4w1zM6fXM6Z_fmgnWhrLam2Ldk8ZGWjQRne5duWKTQ1ZPuyQs45vyqAe1DwGtpFo2B8dzm4WzezJxxrKci-5w7Ln80xeCpq41INB8t0ZJIxDTMxCof6lFUCHuBiLoLQ5GTgQBBiVLIYutQq0wSeZIh7HCBIus4xkiZ18gMi-_t_iGfjucfjKqWe1wgL31dRAiWuSqLGkhMZGOaqe5JAuVtdIoODnucqk7vXZzminMLdcDtzy5kcpL454Fb9AKz4Wznav-nxea65pdzJe2HbviMR_iTsHDiVQlrcgXyff0EGtFVk4bO6FVZLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از حرف‌های ترامپ، قیمت نفت ۵ درصد افزایش پیدا کرد و به بشکه‌ای ۷۷.۴۰ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132439" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132438">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ : شی جین‌پینگ هم وارد جنگ نشد و هیچ تجهیزات نظامی به اون‌ها نداد
🔴
کارش درست بود، من هم به رئیس‌جمهور شی احترام زیادی می‌ذارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132438" target="_blank">📅 12:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132437">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d804ebbfd.mp4?token=okY4QWE19ug7cBImJPOp7tGMZEReeXzx4z-tZLU7XgMjjbg5d5LucbaQNfkc9UoXFA7j8QbpQyh9HrYc4-8DRkOu2kzfj2uhmKq_Y1zgg-SDkaK4BPlZLVaH6yo3IFl5eq2gCAcd-MmI3etd2CfJAaUHB0ZM0yUE_QZPll0LFYylRUDd2gEqtHrjLtotL7nMlAipcfc7g1ZN9pdlrAvbWyUHOgmTX-ETIicJQfZp6lW8x9bbWSHBiAUhR6_CVIW54aTawLMbqzxKvGfESZ65hSI-mfr9R2soQL_rnKmLBcM25f0fwU4KwMTMjwr-1Qux-0yDgEa1LHvWN5M8bWW1Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d804ebbfd.mp4?token=okY4QWE19ug7cBImJPOp7tGMZEReeXzx4z-tZLU7XgMjjbg5d5LucbaQNfkc9UoXFA7j8QbpQyh9HrYc4-8DRkOu2kzfj2uhmKq_Y1zgg-SDkaK4BPlZLVaH6yo3IFl5eq2gCAcd-MmI3etd2CfJAaUHB0ZM0yUE_QZPll0LFYylRUDd2gEqtHrjLtotL7nMlAipcfc7g1ZN9pdlrAvbWyUHOgmTX-ETIicJQfZp6lW8x9bbWSHBiAUhR6_CVIW54aTawLMbqzxKvGfESZ65hSI-mfr9R2soQL_rnKmLBcM25f0fwU4KwMTMjwr-1Qux-0yDgEa1LHvWN5M8bWW1Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ناتو: من از عملکرد ناتو راضی نیستم، به دلیل آنچه که در مورد گرینلند و ایران انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132437" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132436">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری / ترامپ: من فکر می‌کنم توافق‌نامه همکاری با ایران به پایان رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132436" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132435">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: من به مذاکره‌کنندگان عالی‌رتبه‌مان اجازه خواهم داد که در صورت تمایل به صحبت ادامه دهند، اما من این موضوع را بعید می‌دانم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132435" target="_blank">📅 11:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132434">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ درباره رهبری ایران: آنها دروغگو هستند. ما یک توافق می‌ کنیم. همه موافق هستند. هیچ سلاح هسته‌ای. ما یک توافق می‌ کنیم.
🔴
آنها به بیرون می‌ روند، با رسانه‌ها صحبت می‌ کنند و می‌ گویند که ما اصلاً درباره این موضوع صحبت نکرده‌ایم.
🔴
مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132434" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132433">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ: هیچکس آن قاتل‌ها را دوست ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132433" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132432">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: مقامات جمهوری اسلامی آشغال هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/132432" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132431">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فووووری/ترامپ: وقت تمام شد، آنها پست فطرت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132431" target="_blank">📅 11:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132430">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ : برام مهم نیست می‌خوان مذاکره کنن، بکنن
🔴
ولی به نظرم فقط وقتشون رو تلف می‌کنن. اینا یه مشت دروغگو و حقه‌بازن
🔴
من تمام عمرم معامله کردم و موفق بودم. اما وقتی با اینا طرف می‌شی، می‌بینی از یه جنس دیگه‌ان؛
🔴
دروغ می‌گن، فریب می‌دن و آدم‌های خطرناکی هستن. به مردم خودشون هم آسیب زدن و تا الان ده‌ها هزار نفر از معترضان کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132430" target="_blank">📅 11:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132429">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: ما نیازی به رابطه تجاری با اسپانیا نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132429" target="_blank">📅 11:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132428">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ: ایران، بازیگران غیراخلاقی هستند، آنها "بی ارزش" هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/132428" target="_blank">📅 11:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132427">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: ایران موشک‌هایی به سمت کشتی‌ها شلیک کرد، به همین دلیل آمریکا پاسخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132427" target="_blank">📅 11:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132426">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ: گرینلند یک مشکل بزرگ برای آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132426" target="_blank">📅 11:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132425">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ: ما نیازی به رابطه تجاری با اسپانیا نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132425" target="_blank">📅 11:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132424">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ در حضور دبیرکلّ ناتو اعلام کرد که دیشب حملات سنگینی را به مواضع ایرانی انجام داده‌ند
🔴
او گفت که ایرانیان را دوست ندارد و مقامات ایرانی را بی‌لیاقت توصیف کرد چون توافق نمی‌کنند!
🔴
ترامپ ساختار فعلی ایران را "سرطان شوم" توصیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132424" target="_blank">📅 11:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132423">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: ایران سران آمریکا از جمله من را مورد هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/132423" target="_blank">📅 11:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132422">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: ما اجازه نخواهیم داد ایران به سلاح هسته‌ای دست یابد؛ آنها دیوانه هستند و هزاران نفر را کشته‌اند.
🔴
ما وقت زیادی را با ایران تلف کردیم و باید کار خودمان را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/132422" target="_blank">📅 11:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132421">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF9YQZe8XCc1be-q1n3X_k_DTZ-tHBx0-pXBEBzzqFt25ROKl5ir8ipkRj9RFNJW7s6ma5KIvmsBORpAOhubyG8HmLwwOlwENRMBW76oM0d44hGm7nfvYNoZS7BGWA_sNfYYocvKS4ZGq0v4FS6pss1OdM_J9hUvRs7gVR5g1qzzWmsymrTaqkMJCAfqaJ5zAniiTQeCAg6JaQ0oWNdoaUx-zOCYDyLuDMV9WgJ2c7q8F2VkIPAqZ_srl59omyVa2fRXVWB5s_y3dyoVg7oa-8mUeIkJUonWVjMXPggAw1VYiDZNaHtYUPW9LnqzBAO-OR05xrIYPmejAYbnrRXlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گفته‌های سازمان فرودگاه‌های هرمزگان به خبرگزاری ایرنا، در حملات شب گذشته، هیچ خسارتی به فرودگاه بندرعباس وارد نشد.
🔴
در حمله شب گذشته به این شهر، هیچ خسارتی به زیرساخت‌ها یا تجهیزات فرودگاه بین‌المللی شهدای پرواز ۶۵۵ بندرعباس وارد نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132421" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132420">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کویت: مجدد بر حق خود برای پاسخ به حملات ایران تأکید می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/132420" target="_blank">📅 11:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132419">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرگزاری فرانسه: چین، آمریکا و ایران را به خاطر تشدید تنش‌ها و احیای دوباره جنگ مورد انتقاد قرار داد و خواستار گفت‌وگو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132419" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132418">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
قیمت نفت در پی تحولات جدید خاورمیانه و لغو مجوز فروش نفت ایران از سوی آمریکا، بیش از ۲.۵ درصد افزایش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132418" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132417">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkRzksq9yfkJFHbjXHooEdwKZa5fed9IxXoSf_9R20wm4fEFbkPbc2SZcUgxcYqA7CvYjbHhYOW9Y9T5xFSQYhzYykrms-dv-twniNggBaxn7twRakkKJRJTKt9QAfstcrAzr0IV0bu7H7SljS24KByiiBwHg_UDqcrYUFeNdwVCDlHdOZUIywMoDs6HW4N0Q0pIV_24X3z30XQo00FxHrNVEu7hr4N-8nefTxO-zHcwSnJbDZW45Uh0qdtrZvy795kKpdPU1Ld5oXV8pKiPaIKeqIos9iZ1SUhzCWOFdRtCwYrMSBjRKXsPkc0bUBbSrSeXLeHK7_OSiqDyS4Nx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو به نیوز مکس: خطر ایران همچنان پابرجا است و تهران همچنان قادر به بازسازی برنامه هسته‌ای خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132417" target="_blank">📅 11:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132416">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس:
نظم جدید و ایرانی را در تنگه هرمز به رسمیت بشناسید؛ تنها راه همین است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132416" target="_blank">📅 11:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132415">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اولیانوف: حضور کامل آژانس بین‌المللی انرژی اتمی در ایران در آینده نزدیک امکان‌پذیر نخواهد بود
🔴
میخائیل اولیانوف، نماینده دائم روسیه نزد سازمان‌های بین‌المللی در وین به ریانووستی گفت، در آینده نزدیک نباید انتظار حضور کامل بازرسان آژانس بین‌المللی انرژی اتمی در ایران را داشت.
🔴
وی افزود: ممکن است بازدیدهایی از برخی تأسیسات، مانند نیروگاه هسته‌ای بوشهر، که از حملات آمریکا و اسرائیل آسیب ندیده‌اند، انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132415" target="_blank">📅 11:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132414">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از آژانس ایمنی هوانوردی اروپا: اپراتورهای هوایی نباید در حریم هوایی ایران پرواز کنند.
🔴
تعلیق پروازها از طریق حریم هوایی ایران و عراق تا پایان ماه اوت ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132414" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132413">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdFwYQx9VE_bpe1gnGE18buYwgYwoAUMtqHum3YyVSxBHNocnwXZD6tZUNoOzrCyHdnij_gw8-wWCSTdlnT7FD4qqN8u401u9FLI91mi3Ya4tNqh38UBNmJTkfjsb9LSgNb0CqkrjN0AYv4zg2zfAtnXHTnlIYgSSh339PVaBfRWhbf8mqHWx20a6ClLGEatVvjqvWH7zNXNEgk9gJSesT2GHWaKvh70w9H8Iy0H78cxfhkSJa4w8BNCb1iHAiKUvWZcAYMNRYwAISZX06n86QA45YcjSDEWXa-lmmvH2_WDIgSdVObOuVkPPZiNKYWbUn4M_mgop2tQZNjS0U1QdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گابریل ادواردز، فرمانده اسکادران هلیکوپتر نیروی دریایی آمریکا پس از ناپدید شدن در هنگام فرود اضطراری هلیکوپتر در دریای عرب، کشته شد.
🔴
با وجود گشت چهار روزه برای پیدا کردن جنازه او ، تلاش نیروی دریایی با شکست مواجه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132413" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132412">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d638495cb.mp4?token=Tk0OOiA69Qg0LVWFJBJo6TMPoLWGx8jzXHNUIqpvHV_Q6houOhI3H_IWnR1DqRYD9i8LfKlCjGhOHGvvBncZoKjKx633rUvNTGHwJqQLSfAsL54SklznSmlTZY5ndzIxWBFbvidsXMODAQEQK7oyeOZQ0W-pLvjl7tgwpx3lRxSy2u2GY_HBb4ZCNSQbOxxFtcbp6dOQ6j5JpGi52Kg_WKmXo5rbJciOpSEyzFRpdaxfzwcw6MYvZxDw1FFoRiToDNu-rt-X5A6GXBOCeoPeqIyMfaYGVS2I_YXVOUYXK0-5Y6w-RNf35kP9sG-PsqfQPfrqYbt1e3mm5zOUHI3f9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d638495cb.mp4?token=Tk0OOiA69Qg0LVWFJBJo6TMPoLWGx8jzXHNUIqpvHV_Q6houOhI3H_IWnR1DqRYD9i8LfKlCjGhOHGvvBncZoKjKx633rUvNTGHwJqQLSfAsL54SklznSmlTZY5ndzIxWBFbvidsXMODAQEQK7oyeOZQ0W-pLvjl7tgwpx3lRxSy2u2GY_HBb4ZCNSQbOxxFtcbp6dOQ6j5JpGi52Kg_WKmXo5rbJciOpSEyzFRpdaxfzwcw6MYvZxDw1FFoRiToDNu-rt-X5A6GXBOCeoPeqIyMfaYGVS2I_YXVOUYXK0-5Y6w-RNf35kP9sG-PsqfQPfrqYbt1e3mm5zOUHI3f9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردم عراق میان دست میکشن رو سره عراقچی بعد میمالن به صورتشون
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132412" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132411">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
معاون امنیتی استاندار بوشهر: امروز یک مقر نظامی در شهرستان دشتی و یک مقر نظامی در حوالی شهر چغادک از توابع بوشهر مورد اصابت پرتابه‌های دشمن قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132411" target="_blank">📅 10:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132410">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سی‌ان‌ان: پیت هگست برای اولین بار به عنوان وزیر جنگ به اسرائیل سفر کند
🔴
انتظار می‌رود این سفر امروز انجام شود و  هگست با بنیامین نتانیاهو و اسرائیل کاتز (وزیر جنگ اسراییل) دیدار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132410" target="_blank">📅 10:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132409">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCPJCgbhUZd6s8QTTDQUbqz0gzsRt3ZILJwaV8U-I_bDR9U2nOjhgNQPZgzsz6GeeLiDPwttUhcMKt6z_beu0tfqJlSVv6DIJvXvIyQnQI6dWKp2EW9gWgADkzhe0R2__K-BJHfFLKG2yoky6Ona1oTku-5-LKiOXcWgQ_SP7IZsCnxxuvEbcGMM9CCYlNMCZlanC7YKh5by4anpjLo5946VfoMSNKi94uLZaWOpaPBXGdyM6nCyBik_1ooQLUS7Vh-_TvLEB8Nxg66c8AUOEpFtQJBe8O33hECC-P9CMatlvoH85tjAXduiJCkDAR1cFP2Df3xbfdUrJA_owBrBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه وزارت خارجه درباره حملات آمریکا و نقض يادداشت تفاهم خاتمه جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132409" target="_blank">📅 10:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132408">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ارتش کویت مدعی شد ساعاتی پیش چند موشک بالستیک و پهپاد شلیک شده از سمت ایران را منهدم کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/132408" target="_blank">📅 10:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132407">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3ZUIArX71RbcZ_ZcsfK2PN7cC9jOAGw5T_dzxBTKFY-uHKnfIqswyA-YhbStoLIp5qY9lc05aI74CkDwTfBINKc0E0UmFI1N0xMj1EN-eBVjX2GSdVxTdj9fZu4-43l5GCrN3WJl2nzAYdrAHR6D9jrt0dOG50iKxxPGFh4PnaOkiQffX-EDd8vD-5JQ9Ynn4wkRV5uk2xPu-U6lqODq8SC7lnu8x66Rmyxuq_b3rCgPMbj6OysmFqDt3IHhpqTsZPZgiKf-DJVu1l7GkYxC2Yovq3kUMab_ChyZuky2g-gH9Q0GQ1WCSKEsVZ7hibAUSzefVFcKc5naNc1Oy5mBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسام الدین آشنا در واکنش حمله سوپر تندروها به عراقچی: همان که سنگش می‌ز‌نید؛ سنگتان را به سینه می‌زند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/132407" target="_blank">📅 10:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132406">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0X0xeL9XzjgY7bhaA6nTm86-S4jqwbfqTFugNjX0vetpkyIAVLF7hm9ZH4p2-8P2wYBjEZNbv6HdmSGfILgRDIGbafit4jujg_McdmIt6_oV5DEzrXaMZX61UaPu1ZPzBtLwmnfTvqzMdniCwTzChyOUxi9NIMNGf-GHg9wbl4kv8m1LmFWTEZAqv3KJu9ibaA0-51wGP_jbv4DHx3xzI9UkSzhfZ4iLUJa7I9Cp7XWEuRuAwHqfozay69KXqbxzHumDg_AHxirPfrSrdrN-eMxCZ-R5iW9_XGd8A0UjGYPERQ_cEfiwCcbw99Y4Hbyx7oZy5GBaMcGZ33-eY_r8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۱ اسرائیل
🔴
ایران: روزنامه «کیهان» که سردبیر آن از سوی دفتر رهبر معظم منصوب می‌شود، به‌طور علنی خواستار ترور دونالد ترامپ و بنیامین نتانیابو شد.
🔴
در این روزنامه همچنین آمده است که بیش از ۱۰۰ میلیون دلار از مردم جمع‌آوری شده و قرار است به‌عنوان جایزه به فردی که ترامپ را ترور کند، پرداخت شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/132406" target="_blank">📅 10:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132405">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Urv9Sick-rRDDOqCKQl__vgboUN4CONZ7t69PrjoZh0RNKmeFghp08l6Y7nmSHdRSyOfwiQhNHr4rYtMqM-o2Vb9P1kKRVXH-gKylM8XKpjLTFr47OBRffMPM6DwC6nwaz_VVayUIyRs7s_6YdEWBwKeahGjFYgyGNb9fEGQFZzqf-mPP-rNkFU4VerHU_lboqMT1McySwSM6Yn8_PM5gwb-2NH285W_UenH1FfAmTaBjXAz8rLHeLkA4RaHduASNbhCIwkpIBCJylSatiPmRF3g3XrhCWC5SzFgPlfcVv3IY1WagmhCj1RTfdu_F6xXBGG_I2bdxM-hU76IsJ4SdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لارا روزن  :از منظر تهران، اهمیت راهبردی و بلندمدت تنگه هرمز بر هرگونه منفعت اقتصادی که ممکن است از توافق با آمریکا یا بهبود روابط با کشورهای خلیج فارس حاصل شود، برتری دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/132405" target="_blank">📅 09:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132404">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
آژیرهای هشدار در بحرین برای بار چهارم به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/132404" target="_blank">📅 09:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132403">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک مقام آمریکایی: ما مذاکرات خود با ایران را ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/132403" target="_blank">📅 09:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132402">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
صدای چند انفجار در شهر بوشهر و مناطق پیرامونی شهر شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132402" target="_blank">📅 09:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132401">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سپاه : پاسخ ما به حملات آمریکایی، در ابتدا از طریق عملیات مشترکی بود که توسط نیروهای دریایی و هوایی ما انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/132401" target="_blank">📅 09:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132400">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
داده‌های ردیابی کشتی‌ها: ۴ نفت‌کش و گازکش از تلاش برای عبور از تنگه هرمز منصرف شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/132400" target="_blank">📅 09:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132399">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8-n14UoMsXiv76oK-xRq7iXZKuk1nsaXCsAQHGB42e6CIA5KXqne-xHcGw8jEdJt5Yf5o5fCd7gbTFNF2pafirS1Hqadwueld2dzODHhokKb3RQNdmhZHYuoLrBxp5W8eiDfd1-cR7jM5mOAwPC0x3xukM0lwXgFRGT1IvryKQbYsloR7GUsxJGCdYA4oEe-aSaeI4FZCSBpTjgEQfiFQzFbdO5pg4AmewSHK2YJ6wxkdJ8v70l6fvlhF9CX9D_Jmb26IW2W5FespL7Ww7fd0wHzfr2o6OVbnUi1k86bwU1BqRVVyBVEiIBwYdS221SUMrXT7IDEIphWt4-TOQF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت تتر ۱۷۷،۴۴۵ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/132399" target="_blank">📅 09:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132398">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وضعیت در بحرین به حالت عادی بازگشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/132398" target="_blank">📅 09:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132397">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سفارت لبنان در واشنگتن خبر داد که کاخ سفید برای رئیس جمهور لبنان برای سفر به واشنگتن دعوتنامه‌ای ارسال  کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/132397" target="_blank">📅 09:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132396">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
خبرنگار:واکنش شما به حملات اخیر آمریکا به ایران چیست؟
🔴
ادعای روت، نماینده ناتو:به نظر من، این اقدام کاملا ضروری بود. ایران، آتش‌بس را نقض می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/132396" target="_blank">📅 09:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132395">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
عربستان سعودی نقل و انتقالات بانکی از حساب‌های سعودی به حساب‌های دریافت‌کنندگان در امارات متحده عربی، به ویژه در دبی، را به تأخیر انداخته یا مسدود کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/132395" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132394">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
انفجارهای شدیدی در منطقه بندری کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/132394" target="_blank">📅 08:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132393">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
پاکستان سقوط هواپیمای ترابری خود در دریای عرب را تایید کرد
🔴
سازمان هواپیمایی کشوری پاکستان (پی آی ای) صبح روز چهارشنبه سانحه سقوط هواپیمای باری از نوع بوئینگ ۷۳۷ متعلق به شرکت کی-۲ در دریا عرب را تایید کرد
🔴
پنج‌ خدمه هواپیمای باری پاکستان از قربانیان این سانحه هوایی هستند.
🔴
مسئولان پاکستانی اعلام کردند: ما به عملیات جستجو و نجات سریع و موفقیت‌آمیز امیدواریم و در این زمینه تمام حمایت‌های ممکن را ارائه داده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/132393" target="_blank">📅 08:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132392">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL6KJfZrkDNxFC8J2paZPv_G3zdEtsN3j180xEWa3TYBKjxsYoQgJaBq_8CzMcFyv-vOgdch2HiL_YU8DkjJpKmNPUx8JvHBMZ-6ICtcjxlxOtaeNvlPLxjJSpVka3sihxCXTBx_nn828baRA_H2ytjC12twJUi776Z8tZPqJp_5c8HMPY6j1QPPCD_FWOTu35xj_YceMM-3eprKjLfy7KgN79uyVSXhJMTEU01PPj60gTV0bvKtauPj16EpsQLHQZoQRkUDfOFh7eX4Wo_QgGj3q4CQOObakN9jLgwa_lYDgpH3oEJzcWoMvajevgW4YQpVt3Rhq3jm6yLGG9IJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسمیت، خبرنگار ارشد نیویورک تایمز به نقل از یک منبع نظامی
:
حملات هوایی علیه ایران فعلاً ادامه دارد و قرار است تا مدتی ادامه پیدا کند، تمرکز حملات روی چندین هدف نظامی ایران خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/132392" target="_blank">📅 08:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132391">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQQoaQ-ZCMz8HMonU9A99kQqYtb-tii8sNeiIZ2qgmFMMlNiohgpMSnz55b1_GZPzuhVH3_W7hsd1ewVLXI46NMyepgoW5qJ_TRsy12wjFXQDqLls3osNS7GIznfOf85xnUmL3ehC8C_u3t9MYHatwfE4CE9afvNVLGjD9fslB-cwN7bIYLmjrmsZXnwoK1Sl4UsVmwtlpnrtDIJuJdPgV6FYMk87uky4dWOFfbkTCewu302RaiaK2iPCeCcQ6XVccsHEAv6MZB-9Di55j_GhtOSGouPJ8wMxD-CQqfFhEpqwygG_eBAkk7ryh__3og4Laj-2vTVgLMfuijStq5lUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب پالایشگاه نفت ساراتوف در روسیه مورد حمله اوکراین قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/132391" target="_blank">📅 08:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
خبرگزاری رسمی کویت: آژیرهای هشدار در سراسر کشور به صدا درآمدند
🔴
برخی منابع خبری از شنیده شدن صدای چند انفجار مهیب در کویت و بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/132390" target="_blank">📅 08:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132389">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/132389" target="_blank">📅 03:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/حمله مجدد به بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/alonews/132388" target="_blank">📅 03:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
عرافی، مدیر حوزه علمیه :
عدم حضور مجتبی خامنه‌ای توی مراسم وداع با پدر، فرضیه غیبت کبری رو تقویت کرده؛ ایشون احتمالا به امام زمان پیوستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/132387" target="_blank">📅 03:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
روزنامه نیویورک تایمز به نقل از یک مسئول نظامی آمریکایی: حملات به ايران برای مدتی ادامه خواهد داشت و بر روی مجموعه‌ای از اهداف نظامی متمرکز خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/alonews/132386" target="_blank">📅 03:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرگزاری آکسیوس به نقل از یک مسئول آمریکایی: ترامپ با طرح حمله به ایران موافقت کرد و دستور اجرای آن را در زمان حضورش در تركيه حین شرکت در اجلاس ناتو صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/132385" target="_blank">📅 03:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132384">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرگزاری آکسیوس به نقل از یک مسئول آمریکایی: ترامپ با طرح حمله به ایران موافقت کرد و دستور اجرای آن را در زمان حضورش در تركيه حین شرکت در اجلاس ناتو صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/132384" target="_blank">📅 03:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132383">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سی‌ان‌ان: وزیر جنگ آمریکا روز چهارشنبه به اسرائیل سفر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/alonews/132383" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132382">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پزشکیان بعد از شنیدن خبر حمله از عراق به سمت تهران حرکت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/132382" target="_blank">📅 02:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132381">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e73648ed.mp4?token=vtw0lQLnf-__xo6KSauyAumia6TMUO9mxBmIuT076MJkdrIEXE1_hsswnkK3J-AhGZ-gPPc4ZGXevYCQQhKXZifZyc47SuVcG6AKBuQEjldsQXExtNvXCN7LU8YoGjb9S2xxC8Od4ALyDwDGpMUZMkeBElw3zgIMVeqxMylXClvtrA1sjplbqSbmb2PYAJjMCJHkJYKLwYH9_8dDyskGe3aqk5bC8n5gX6iyejaD4MhMnzK7sLwr-eTyWKxK5C5Ow19ZA7W5sKpK48uFq1-PJjLBvdWGrNpwM2_Q4CwUWXRHvuz_Brt52BxC1xwOZUSJBF-30TR9y6mxpK2dZub2CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e73648ed.mp4?token=vtw0lQLnf-__xo6KSauyAumia6TMUO9mxBmIuT076MJkdrIEXE1_hsswnkK3J-AhGZ-gPPc4ZGXevYCQQhKXZifZyc47SuVcG6AKBuQEjldsQXExtNvXCN7LU8YoGjb9S2xxC8Od4ALyDwDGpMUZMkeBElw3zgIMVeqxMylXClvtrA1sjplbqSbmb2PYAJjMCJHkJYKLwYH9_8dDyskGe3aqk5bC8n5gX6iyejaD4MhMnzK7sLwr-eTyWKxK5C5Ow19ZA7W5sKpK48uFq1-PJjLBvdWGrNpwM2_Q4CwUWXRHvuz_Brt52BxC1xwOZUSJBF-30TR9y6mxpK2dZub2CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات هوایی آمریکا به جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/alonews/132381" target="_blank">📅 02:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132380">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
انفجار مجدد در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/132380" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132379">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw7NPEWAj08nx_J6bEqZf_UmD00vc_ON-1vM8CeYoEJoW5FMSO47kYFz-zZbVGdttQBDJp5Y12h2Cx2Wijfp3FAMcW3wZMRRvDSB6t893BLSyByN9oGpXit7SJ-D28JRxwMtsIxbHr_DoXxK23iwBScL7Gpr7Ked3_zp5Vl6jPMB47cLqdVTBASggwhOyZPAZHfCfGyVqZ_ptO3EP-CBoYfGJv-LJmW1Y8CB3Z-u1R3aY_WaV8SAf0GTjGoguA08hK91_PAkuN_FCgpQk9OhMGAf-GBDHQ1eYMALopoa7Li32HB9qvv_OS_R2NS5CPXs7hCEQQCbVwgV8ai6xOm50w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت خبرگزاری معتبر فارس همزمان با حملات کم سابقه آمریکا به بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/132379" target="_blank">📅 02:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132378">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
اکسیوس به نقل از مقام آمریکایی: حملات آمریکا علیه ایران از نظر گستره و قدرت، چهار یا پنج برابر بزرگ‌تر از حملات قبلی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/132378" target="_blank">📅 02:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132377">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIt4uzxxCCL-Vhy0xurSK6f8L7-Iuj5YO7niUSacplIjM90J0WbXQqSWU_YazccUywuOko7CB8xFvUI1UnHoOB48Vc3CMTIVVP8uOye_EJ2kEi7Dw-dsYlfa_0W7yyIWgD-DbnIWX07j2P4gD1hIvPetYAx8V712gwumQ621jau9AXPTHbrLW2sZVDhoBjEuJiqu401DnlXTeGe91p141-TgNf4QjNujtjZdBPbe7NDEmRR_k8FUtmxlpOlVu8raceORIc5ltC9dfRlDqqHofHGaYlcY2lHzE1EQt-x5HWiky6nIZZQz5eKlZ1wOIjuDAWggO8Gc8D4Qdtf5mx52eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
🤪
💦
🫠
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/alonews/132377" target="_blank">📅 02:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132376">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری/گزارشات از بسته شدن تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/132376" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132375">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/alonews/132375" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132374">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مقام آمریکایی به رویترز: حملات ما در ایران سیستم‌های پدافند هوایی، سیستم‌های نظارت ساحلی و سایت‌های پرتاب پهپاد را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/132374" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132373">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
اسرائیل هیوم: اگر ایران تلاش برای جلوگیری از عبور نفتکش‌ها از تنگه هرمز را متوقف نکند، آتش‌بس در خطر فروپاشی قرار خواهد گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/132373" target="_blank">📅 01:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132372">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">اگه جنگ شه و حریم هوایی بسته بشه، مجبور میشن سیدعلی خامنه‌ای رو عراق نگه دارن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/132372" target="_blank">📅 01:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132371">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوووووری/سپاه امشب پاسخ خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/132371" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132370">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=PmZQF7SuXJo8ZxWEH4pk7zNIiDNhMr3JJfYe2TKK3N3ctySCeM18VPje7oP_pPhCSrIQPuJ8TsEKFpum0OmQ1_BkVY7Sy-BxiLQdSo4XMBWX-OKM1ZVbVeaoAGrWHC8vnxBxSZzJFg-VPLBu52yNmf9zwDLmiev5KJvGZ_8_xFeviV5LG5QmH-LPvK-Tg-IR-krpjgneje272a3c4EhaYJ25mG0xizrzUxQwG8GyYZoNNjPoHE3gN9hkW2RXNKCBmkp0jl2MYpa7Xwjn4LbYulyJABHdD_4wAFVaMMGGtbhAxf3Nh5gO-lGlv9v__fE5Gddb9Jenxht9SZQOCNaB_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=PmZQF7SuXJo8ZxWEH4pk7zNIiDNhMr3JJfYe2TKK3N3ctySCeM18VPje7oP_pPhCSrIQPuJ8TsEKFpum0OmQ1_BkVY7Sy-BxiLQdSo4XMBWX-OKM1ZVbVeaoAGrWHC8vnxBxSZzJFg-VPLBu52yNmf9zwDLmiev5KJvGZ_8_xFeviV5LG5QmH-LPvK-Tg-IR-krpjgneje272a3c4EhaYJ25mG0xizrzUxQwG8GyYZoNNjPoHE3gN9hkW2RXNKCBmkp0jl2MYpa7Xwjn4LbYulyJABHdD_4wAFVaMMGGtbhAxf3Nh5gO-lGlv9v__fE5Gddb9Jenxht9SZQOCNaB_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو لحظه انفجار ها در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/132370" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132369">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فووووووری/کان نیوز: در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/132369" target="_blank">📅 01:44 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
