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
<img src="https://cdn4.telesco.pe/file/Ndhhce3dJbQNgk54-8hnYP35qtbxE0BO76V8B7GE58wipUrYlnWLc1ixetFslxzA-_VdYGMzz8QDF8d5ksNtPm4UlKqB66ZRUVYH3Ny1DlK-gEP6E1RCRxbP_4HVg_ADmsgfIH7gyiOf8FDS7fiHFrsz3t5LVA1IK9lD7yutUHUWHJzxGs-lI8k_47omJBTSVabrIdZM0_isru86vgalRoWJgny8MaqFO9UGRM8v6ivF5bHNCJGDxYyOvYibs36bMgRg_HcvckY7iSF-oOb5D9MtBbeaMw6A5dnyPNZlYTnPuzZwhKrD3CpBaCcZAYUxB0RotS68XRjKD4GKtlh-_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-151948">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوووووری / معاریو: ترامپ از اسرائیل خواست پیش از انتخابات میان‌دوره‌ای بدون مشارکت آمریکا به ایران حمله کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/151948" target="_blank">📅 16:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151947">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWD-MO4l1k_qOgkeejhCaDI-t5ctSoqf3_Yfz4Y4or4mMrgC3T0anNuZYtiImJnqhApmOA9yFtoH0-KCDFKZoeJRnuPvXYPe8W2lqqCVICw0Dw0jlvZ9SPLGTKm8kMquwWVs0RFYaCkPsXxZDTViuYcsWgWKP2GLpz2MTSFLvEDeAudRMQWMkJDUMhszzZ3XE8asCqGH3pOqnK26Rcm_mDYugya4_NHAayyh9zBgOhe-CBuaE9hkxX6OBQ7P3I7zAltBlJ6ZfO7N5xcw2aZ4275NzpPjtybcAGR3q0ArzkziT-FC50Fv1rph_LXpT_3sIHC6RthOWT5o303ChxLvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ویرال شده از یکی از فروشگاه‌های قم که به جای کلمه «کاندوم» از کلمه «تنظیم خانواده» استفاده کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/alonews/151947" target="_blank">📅 16:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151946">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جان سینا از دومین ایرانی هم لب گرفت؛  تو فیلم جدید Matchbox (2026)  | مچ‌باکس با بازی جان سینا، یهو گلشیفته وارد میشه و اينجوری لب‌های سینا جان رو می‌خوره  این فیلم اکشن و ماجراجوییه، داستان هم درباره «شان واکر»، مأمور مخفی سازمان سیا با بازی جان سیناست که…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/151946" target="_blank">📅 16:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151945">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65fe6ddfb6.mp4?token=sn8fvZ_RT8BykfZ1aXyUX93Tyhu7Kmj2atauTNLJxWzvKUouh-YlymguZgzp8vjzkbt_6gom--r4VQrqEjIlzaIL6QIl30sp3i7M-VMtORmZhonHe-0NGFOAfNW8-tus6F3Q6mNV7jfu3MApT9dj--SexTxuaaUGF5JOhn96dFgiTLNaRgo286BB0QkWEXRVbywEptX0IQZt4Zg2agFoG9YjYqfKOK5lB5WiXkx61AqcLOs6anfRD0K1o3FhAsVaKzEQ5rgDXAi6M3Dt9gaURuv_rvBv1FKvEBfgcdvtDrGt5M-THSld181pu53bFBIdpGGMEf8JSbTY_8oj1R0n3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65fe6ddfb6.mp4?token=sn8fvZ_RT8BykfZ1aXyUX93Tyhu7Kmj2atauTNLJxWzvKUouh-YlymguZgzp8vjzkbt_6gom--r4VQrqEjIlzaIL6QIl30sp3i7M-VMtORmZhonHe-0NGFOAfNW8-tus6F3Q6mNV7jfu3MApT9dj--SexTxuaaUGF5JOhn96dFgiTLNaRgo286BB0QkWEXRVbywEptX0IQZt4Zg2agFoG9YjYqfKOK5lB5WiXkx61AqcLOs6anfRD0K1o3FhAsVaKzEQ5rgDXAi6M3Dt9gaURuv_rvBv1FKvEBfgcdvtDrGt5M-THSld181pu53bFBIdpGGMEf8JSbTY_8oj1R0n3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد علی اکبر رائفی پور تو این ویدیو یه جورایی از
خاک فروشی
حمایت میکنه و میگه چون ایران خیلی بزرگه آسیب پذیره
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/151945" target="_blank">📅 16:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151943">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رئیس جمهور موقت ونزوئلا، دلسی رودریگز، مجوز فعالیت شرکت اینترنتی ماهواره‌ای استارلینک، که توسط شرکت اسپیس‌ایکس متعلق به ایلان ماسک اداره می‌شود، را در این کشور صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/151943" target="_blank">📅 16:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151942">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6EFMr6z_RLAFewe88csJd_sVOialw2mVEHNM7MSCi4FmHWQJwYIwJ8YdgW_myjgX62a7PyKT3LA5oyqnogtwLaEtDO_Ig_bQwXonzHcYkW3u11cV5mmqpM09dHkCm9GLNHrMbY_H1nwNhmULldfINksGvQ6eFUgqSvBICcE3vajL50sz5CBWjk8qu2NdUSA6-L2dYr9aHuh-9IYvJGtj_1nnE6b7-YGpCqjfzjmVm1gJzHe0W1Lt6A5xfP4mdYtBmkXxqEhayuCa18BwBZK6rwTGa3dXzxk4eHRcvkb1AozEPmjERiVEYlpwvfMl5GYxxYkEHEfLt1II6W7zpPQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حشمت الله فلاحت پیشه: آقای پزشکیان! رایزنی با قاتل احیای برجام۱۴۰۱ و تفاهم اسلام آباد ۱۴۰۵، رفتن پی نخود سیاه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/151942" target="_blank">📅 15:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151941">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رهبر حوثی ها: از آغاز تاریخ عربستان سعودی تا امروز، شمشیر نقش‌بسته بر پرچم این کشور هیچ‌گاه جز علیه مسلمانان به کار گرفته نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/151941" target="_blank">📅 15:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151940">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP3Vf7oXUOc8zMN0CHqX-z3T4AItUqug3qOjssFEZjyGbTRfcXWBxW_YiSHSqsWeWVEn6UO0qShQg1tZHhcehgJSZXuoolxTylf2RguWss5gwPBOAGmR82odyLL6RgQDOr-oUN3ZaSVrjvqj2MisTOY7DapeK18y6H_KMfBwA9ShRl29stlXyUICM3BrqFpTK8-FQMZ0y00gMS_qZ1Uj-R3thlbyI-2dvVNsiJLxaie0GlhTJRkyY4jxpPWyBDQCClYhBUuUxm7qDZvOs3Zgwnf8yUU8oeWCqKhcW7y_LLtNZFuB4pAAAhMVI71pBk4TooWspNn1pitoplfrGb9uHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : من 8 جنگ را خاتمه دادم، و به پایان رساندن یا حل کردن 2 جنگ دیگر نیز در شرف تحقق است. تمام گروگان‌های اسرائیلی را آزاد کردم، از جمله 28 نفر آخر، هم کسانی که زنده بودند و هم کسانی که فوت کرده بودند. صدها گروگان را از کشورهای مختلف جهان آزاد کرده و به خانه بازگرداندم.
🔴
در ونزوئلا پیروزمندانه جنگیدم و دیکتاتور خشن آن کشور را دستگیر کردم. همچنین، مانع از دستیابی جمهوری اسلامی ایران، بزرگترین حامی تروریسم، به سلاح هسته‌ای شدم — و موارد بسیار دیگری وجود دارد!
🔴
با وجود تمام این دستاوردها، من یا ایالات متحده آمریکا، جایزه صلح نوبل را دریافت نکردیم. چه شگفت‌انگیز!
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/151940" target="_blank">📅 15:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151938">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGYlaGJhNYstRU6l9ibnDI5bOrkuIMguv1H1Ku8pKzV65981-2RkmGyNtwiFDDgT5r6gJz-3ULjWGdL-VbTHsyLJKLwX_FOIKqmYNMCc-dpJyrvo3vxQLFVwxWBdZyD9K0XCgwg8vKqCE8bHAPsb82vmTJ_bAmkgwG2NquQRTk8HDMrtscwfFjIrXQ4yZSVd94uz0JD0eJgsGCnasq0ZnTvZS8Q1TezYT_uZ--FPdNZsCN_0S1l1D6c9I_swwAl6oLGkQAl5eWuxYncZ-qLSe1UiVej092XqiPhSMI86j6ZPEDAXp3Lhn-NGJOwM7RAtGHlOq-4B7Q_UQqAzSCN3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، چندین کشور آفریقایی در حال حاضر در مذاکره با اوکراین هستند تا شهروندان خود را که پیش از این در کنار روسیه می‌جنگیدند، به کشورشان بازگردانند
🔴
کنیا در حال حاضر تلاش می‌کند تا آزادی پنج تن از شهروندان خود را به دست آورد، در حالی که دولت بوتسوانا در تلاش است تا یکی از شهروندان خود را آزاد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/151938" target="_blank">📅 15:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151937">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ram VPN_v3.1.apk</div>
  <div class="tg-doc-extra">55.1 MB</div>
</div>
<a href="https://t.me/alonews/151937" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی فیلتر شکن پرسرعت
Ram  VPN v-3.1
بدون تبلیغ و پرسرعت
🔥
رایگان و برای رفع فیلتر شبکه اجتمایی
⚠️
مناسب زمانی که اینترنت ملیه
❤️
🎮
دانلود امن از گوگل پلی
👇
https://play.google.com/store/apps/details?id=com.ramvpn</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/151937" target="_blank">📅 15:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151936">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nieyBgNG5SSA3w9b5wUkuibBu0QW6A1Re2mh-LHFTkmmjaIOFxQoR4bPoqCE6titSVVOAInWQxZCkrIwQ7fgbK0OlEe5ZOKnMaFnLDO-oAV3up1CZQ7lCjDowFIOIdM5bDlqttwPQKMfSdND-pdaSjfSbd8O3kONwm7zOTObaFIGVIZlRH2OqpkItXHgNEr6k2aqmmSdMeJprUrS0keBhEY3-IkoLqK7aFUsj2_nTFCSRA85Du4whUW86GCzkWMbhv5xmXtWiOSIg7G4C3_uNVREHHM7yv7nw-SqXKATHEdOtvcWUGYkQ17EDDrBC03yH_ua5nyieR4xNxyYxqqVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رادوسلاو سیکورسکی"، وزیر امور خارجه لهستان: سفارت ما از کمبود سوخت حتی در مسکو خبر می‌دهد؛ شهری که همواره در اولویت تامین سوخت قرار دارد.
🔴
علاوه بر این، منابع موثق گزارش می‌دهند که اوکراین تاکنون به حدود ۵۰ درصد از ظرفیت پالایشی روسیه آسیب رسانده است. بنابراین، مازاد سوخت( روسیه) برای صادرات( به آمریکا) قرار است از کجا تامین شود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/151936" target="_blank">📅 15:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151935">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341194d3c9.mp4?token=oKBv1g7GhMxuoaVCL82aEXxqX14XBdQh7b22B3Yn52SSl_f5ym3IUqhDd9e3tFv24X6aDS-KyFX0k_L6hQhBRd4-magpBQlT6VvCVnAW5jfZjAN8r6jPu-W7jit461oum2NEKIkyEnF-PamC-pLFL8SkZXAkZMpA3nttvrdpKtqQw2LuPz17ErSGVhZ_aEbwDENDPmJ-Qcr4jiD5ZKdIptvwmHU14jRKRHzYwJAJjdb4epuYYRYJKen1u0rS3K8BXOhCTV1jGsSGHyMUxXLPA7FBD_1J8s1lDa-YlSnd6iipGxlSJNkPz8SUOzG_yoGoBibmj53CQ4M9ojtsEPnyEwJZr_lnh20_8KaI_WIZwsMi4imP0f0P-BMx9XyLvVgUBaV4ADZQyDGLD4sL2KEDK06Sfx8nw-X_Uly_h1ZvS6eqHHJldbm7PCqOOxYMVmWk7EpyCnySuPSorD-n6D7EzXfNnIG00RW-qkwuLXKjyUaS-1u4Y2baK4XzoUOAV1EHcOeNf2yPxy0iSi1WEgbfspKXD_VDgWPib5yYS0t9_8SHRZiCjUrp3q3f0ROxoilgo1XPWGan3tLdtmRSpsqeBOivecLcO-VeTGQQR5LFpSLGjPzk5-RgN6r6Y4R97llwaiRrlMi5_vZeRT68u1yn_ojsqbJGxdtJ3annRuV9z8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341194d3c9.mp4?token=oKBv1g7GhMxuoaVCL82aEXxqX14XBdQh7b22B3Yn52SSl_f5ym3IUqhDd9e3tFv24X6aDS-KyFX0k_L6hQhBRd4-magpBQlT6VvCVnAW5jfZjAN8r6jPu-W7jit461oum2NEKIkyEnF-PamC-pLFL8SkZXAkZMpA3nttvrdpKtqQw2LuPz17ErSGVhZ_aEbwDENDPmJ-Qcr4jiD5ZKdIptvwmHU14jRKRHzYwJAJjdb4epuYYRYJKen1u0rS3K8BXOhCTV1jGsSGHyMUxXLPA7FBD_1J8s1lDa-YlSnd6iipGxlSJNkPz8SUOzG_yoGoBibmj53CQ4M9ojtsEPnyEwJZr_lnh20_8KaI_WIZwsMi4imP0f0P-BMx9XyLvVgUBaV4ADZQyDGLD4sL2KEDK06Sfx8nw-X_Uly_h1ZvS6eqHHJldbm7PCqOOxYMVmWk7EpyCnySuPSorD-n6D7EzXfNnIG00RW-qkwuLXKjyUaS-1u4Y2baK4XzoUOAV1EHcOeNf2yPxy0iSi1WEgbfspKXD_VDgWPib5yYS0t9_8SHRZiCjUrp3q3f0ROxoilgo1XPWGan3tLdtmRSpsqeBOivecLcO-VeTGQQR5LFpSLGjPzk5-RgN6r6Y4R97llwaiRrlMi5_vZeRT68u1yn_ojsqbJGxdtJ3annRuV9z8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویر، وزیر امنیت ملی اسرائیل:
ما هنوز کارمان را در غزه به پایان نرساندیم.
🔴
و همچنین، کارمان را در لبنان نیز به پایان نرساندیم
🔴
این وضعیت چگونه باید به پایان برسد؟ به نظر من، تشویق به مهاجرت و اسکان در سراسر نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/151935" target="_blank">📅 15:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151934">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پزشکیان: جایگاه فعلی زیبندۀ ما نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/151934" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151933">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
فرمانده نیروی زمینی ارتش: بیش از 50 یگان رزمی و پشتیبانی ارتش در مرز های غربی و جنوبی کشور مستقر شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/151933" target="_blank">📅 15:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151932">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وقوع انفجار و قطعی گسترده برق در کی‌یف پس از حملات جدید روسیه
🔴
رسانه‌های اوکراینی از وقوع انفجارهای شدید در کی‌یف، پایتخت اوکراین، در پی حملات موشکی و هوایی جدید روسیه خبر دادند
🔴
وزارت انرژی اوکراین اعلام کرد، این حملات زیرساخت‌های انرژی را هدف قرار داده و منجر به قطعی گسترده برق در بخش‌های وسیعی از کی‌یف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/151932" target="_blank">📅 14:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151931">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89eb24a75c.mp4?token=if34TNsm75u681pHVflX-pz7QAXaEBgEKkv9u4E1yMq_-1vtBETbSx60BlwbtgdjtZ1QAUdJiWlNQbpyQPUrZWf7pT0wgOAKyKRvLsFAEwBzUoRQ-SrMMIGpJyNkBOAGeW5mf34sGajtflQkUOyOVbY-RL-5O5zolC5ha0mn4Bm880OiCVjsg6DT2qV6LLbXja-OMASG8Bm9xGhjxstBDgSmzsbL8ctJ-8L9FzCsTl_IC94rmlbZpYw8tdXOcACytIcp6xJM5bIUkupje8xwKdj7jI346NNaFezPK1eZ8HX9JdpCOJMYDWPAsyVFdXXi5tee5M0uDnWxB-cPoeWcQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89eb24a75c.mp4?token=if34TNsm75u681pHVflX-pz7QAXaEBgEKkv9u4E1yMq_-1vtBETbSx60BlwbtgdjtZ1QAUdJiWlNQbpyQPUrZWf7pT0wgOAKyKRvLsFAEwBzUoRQ-SrMMIGpJyNkBOAGeW5mf34sGajtflQkUOyOVbY-RL-5O5zolC5ha0mn4Bm880OiCVjsg6DT2qV6LLbXja-OMASG8Bm9xGhjxstBDgSmzsbL8ctJ-8L9FzCsTl_IC94rmlbZpYw8tdXOcACytIcp6xJM5bIUkupje8xwKdj7jI346NNaFezPK1eZ8HX9JdpCOJMYDWPAsyVFdXXi5tee5M0uDnWxB-cPoeWcQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه هولناک فرو ریختن یک آپارتمان و زمین خوردن مردم در پی زلزله ۷.۶ ریشتری پاناما
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151931" target="_blank">📅 14:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151930">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlQcxnGiw5cebR_u529KTMKNGo2pLBHa5h0rjQVQuKxgVrQU-tJ_nh8yUoQxd_GalZ2WPKI6FJYIcB-d0YIovgfKA7QN_rFex9VulRBge5zAlu5iux44TWopN8mVBXV5otA2HfMNfNpukB4ibZoOxgqRvMENuQWjJTNuk4c8NHPDgV1VzoFYF5npplNaCP6tg6ZnJ0DBStfLGGrqFSznoKNzgop4vDAITH-UnStEpiqYAs2YtHhMdlKIxV-lwQ-yViq_4Fg0SDR80DMElzmhFdwrorpXDvBRMyN_h8yXOEiBLjDGu3F6P8TGa_uVqug6AEnfVwEGPYzyPHRizuINlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی، خبرنگار: بورس ایران قبل از تاسیس کشور امارات شروع به کار کرد، اما امروز ارزش کل بازار سرمایه ایران حتی به ارزش یک شرکت نفتی عربستان، یعنی آرامکو، نزدیک نیست
🔴
چرا کشوری با این حجم از نفت، گاز، معادن و سرمایه انسانی، نتونسته جایگاهی متناسب با ظرفیت‌هایش تو بازار سرمایه جهان پیدا کنه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/151930" target="_blank">📅 14:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151929">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔝
💯
دنبال کانفیگ ارزون و مورد اعتمادی؟
🖥
کلیک کن</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/151929" target="_blank">📅 14:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151928">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
شمارش معکوس دو انتخابات مهم؛ اسرائیل ۱۸ روز، آمریکا ۲۵ روز
🔴
با احتساب امروز، ۱۸ روز تا انتخابات پارلمانی اسرائیل باقی مانده؛ انتخابات کنست بیست‌وششم قرار است ۲۷ اکتبر برگزار شود.
🔴
در آمریکا نیز ۲۵ روز تا انتخابات میان‌دوره‌ای ۳ نوامبر باقی مانده؛ انتخاباتی که تمامی ۴۳۵ کرسی مجلس نمایندگان و حدود یک‌سوم کرسی‌های سنا را دربر می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/151928" target="_blank">📅 14:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151927">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs6b69IsJXO_gqmqdq0-nReJggbfo0hAeTs90Q__WT6kxHfaVMI4l6P5Jcktm8EhU1EW6uHJnVphz_7IpXRtMze98498pcgbephbIGij-t7hux9HM8d-62j79i-1KzmjxZvCYItBYCbshvQjdIL-xdR_XUqboYQ5IShmoEBfxOQt7kFTbhhQxiAt2yYeztLKVJvWVndQL8IZXkI3V_oDhDY2z7aXvXjNk-2bQZPl2g8tBHw3iavLsJ3kqkrOJjNVt-H43HMqxc9MzUPZz9gWe27d7OHHG2GPuKKiS2sDB86wnyKmmtlt9KV5OLAZ7SyL8VjvVEA0MWyZGv5ZDkRlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم:
چرا باید بنزین ارزون بدیم‌ تا مردم تفریح کنن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151927" target="_blank">📅 14:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151926">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWcPqH5zAWtAHkQ7_czciRUIwMLhHBFlR-DX6gj3OK54PAJ-wENFegCj7_12llJp9LB-uvTX099bBqI02ISxYqy1HOu2QBUDN1SMexRMB2szsYRyPE91SAlGEI6hwzWJXEeTWMpLhjyugoTMYz211muVA4peaXLgmhcAXH_TtjrlSSDE_Tci0pCpJPnTX0my9KtZg18IN07NXRWtdMZaON8JFYTF49DVC0o6qzDwyz935sb427Bi1Gp7zeEEkJ7JTaJ0mDOF5GtisEl1CH3NjMb-9K6uY5vbJ8Akb4_unBtwpbs-4RWr99v5lVhWSteC_PI63jKV4lIZi3pvf4GH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی دولت: بمب اتم در اسرائیل است، اما بازرس‌ها در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/151926" target="_blank">📅 14:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151925">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مقام ارشد روسی: پوتین به ترامپ گفت که پیشنهاد روسیه درباره اورانیوم ایران همچنان روی میز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/151925" target="_blank">📅 14:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151924">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8aa407e2.mp4?token=mxd68eEBvCb1rerKdAjVIVF0Eh_MZhOQUIHXDc3fhQglnEEfHGLBPRmTTQki6s9PxZIMmQUx-jTsar8hWw3OKeCa6UDEDGB8Jr0gaQis4b6YCDN42og1qoIi8Byx027lBH_MMunQNVBYi8NcJv7SAKJ1_LwG7RzS7WwTHooNw-SsagWJnIpRYjWa5iTS01x6MVBb5Jpcxl7frboBBpb7PEFlcS-XMeX5HywCHtOsbZBDaEj0dh9DosS3iHTGC9u7qu1KQGx62CGcArAP5w6FR8m4RippXZCEi72EGuj68ST-j6jWmrsq-DWKgFXZKDMXxtbWK-yHPY7MpWdBn6bkeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8aa407e2.mp4?token=mxd68eEBvCb1rerKdAjVIVF0Eh_MZhOQUIHXDc3fhQglnEEfHGLBPRmTTQki6s9PxZIMmQUx-jTsar8hWw3OKeCa6UDEDGB8Jr0gaQis4b6YCDN42og1qoIi8Byx027lBH_MMunQNVBYi8NcJv7SAKJ1_LwG7RzS7WwTHooNw-SsagWJnIpRYjWa5iTS01x6MVBb5Jpcxl7frboBBpb7PEFlcS-XMeX5HywCHtOsbZBDaEj0dh9DosS3iHTGC9u7qu1KQGx62CGcArAP5w6FR8m4RippXZCEi72EGuj68ST-j6jWmrsq-DWKgFXZKDMXxtbWK-yHPY7MpWdBn6bkeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان این چالش لعنتی رو اعلام میکنم
😂
@AloSport</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/151924" target="_blank">📅 14:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151923">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: شهروندان ایالات متحده در منطقه غرب آسیا، با توجه به وضعیت امنیتی پیچیده، نهایت احتیاط را در پیش بگیرند
🔴
درگیری‌ها در منطقه ممکن است به سرعت تشدید شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/151923" target="_blank">📅 14:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151921">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
قدیری ابیانه: زندگی مردم ایران از اروپا بهتر است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/151921" target="_blank">📅 13:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151920">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ae8c9e28.mp4?token=tv8ewrIhlVVu-nZeRJ5OM-zjGTx0-rvpkehVKkyUVLjSFmHpt3ivNSCCegLebXsuF5cnR9TC3mDda0Io4HmmPLeA7YYhUzDi387b_pvW47yaBh7i9ZGC_sduvkog9-f8zqYgBFjDkR_AR994Lm_mW3tcPLQn7xFmzl-d-TnOiATiuzJMmR6SUafVI21FLVDiUmmtAjHnxmn38u4bj0yVOLcDOhuxPZ7b10AK13ma8fjp1jKFSd_S0zucPo01Kcd1Y4-1Cgz9h_wL-_cQkp1QeMFdCO6k4eT_PVVgQ07MQxq-omOxtpxH5fJvxlYr83ZQghq0_hYfhAUA_sVbkaNmlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ae8c9e28.mp4?token=tv8ewrIhlVVu-nZeRJ5OM-zjGTx0-rvpkehVKkyUVLjSFmHpt3ivNSCCegLebXsuF5cnR9TC3mDda0Io4HmmPLeA7YYhUzDi387b_pvW47yaBh7i9ZGC_sduvkog9-f8zqYgBFjDkR_AR994Lm_mW3tcPLQn7xFmzl-d-TnOiATiuzJMmR6SUafVI21FLVDiUmmtAjHnxmn38u4bj0yVOLcDOhuxPZ7b10AK13ma8fjp1jKFSd_S0zucPo01Kcd1Y4-1Cgz9h_wL-_cQkp1QeMFdCO6k4eT_PVVgQ07MQxq-omOxtpxH5fJvxlYr83ZQghq0_hYfhAUA_sVbkaNmlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۵۰ میلیون تومان طلا در سال ۱۳۹۵ در مقابل ۵۰ میلیون تومان طلا در سال ۱۴۰۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/151920" target="_blank">📅 13:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151919">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUWQ96FtyL-gO1FdxQBIZT__Q-8LlesbRIcixw9W3qx4oPAKZPxDgUu0MW0eA575eLUgebW5VvF9S-fLHeqbb1aZVVyb3Y13QokDybSj2CYwLv4NT5w5nitBlpSVzDkf97IPOrXxmtjayvRUT-0c8gCiKaMmsTRuIkil3PYkJ_FQkaxmxI-eSUzv9Ys5kqW2G9XepCtNiD77t3grw_OtsQbgHZ4HoQ6KhiZuQVHcOPr8GF8kCF0800plc4125JdjxXdZzTn2OXYaAHDLTBkjadvaMsDY-Eny1Oy7JQAaNPDCRK_OiNsVfJ3JDpL0grg8_9JzYGxY2VizMJmUny1KnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجداد آمریکایی‌ها ۶۰میلیون گاومیش رو کشتن که غذای سرخپوست‌ها تموم بشه بعد وزیرشون به هخامنشیان گفته غارتگر متجاوز
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/151919" target="_blank">📅 13:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151918">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سفیر کره جنوبی در اوکراین در اعتراض به افشای اطلاعات انتقال اسرای کره شمالی به سئول از سوی رئیس‌جمهور اوکراین، به کشورش بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/151918" target="_blank">📅 13:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151917">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d6fcd9a1.mp4?token=Gz361hlIDqqfP6I4SSbQg0qD6FzXvEWjCj1mSZyQa9gqRegoMAqU6UweaMPAYQhL3ialR-aWB-9FDLgCE93WETj3VBcEpHKve0dj74mhiojFTQeK-Ec1c7nMRm8Gms8xZZB2pO98d_cuP64eIIofzHzbsBFHxsfmTxnS_oHVEZKwDXhlevVodRom9bYBNV50BPkFHNfRDJzwAmPSQ3kBbD2u-kaCoMhWZupML4i9JwcY5PjGYyr4hQNqXFgg_ybD_wuivV5uCD6m4vNWm7RGKQCEriUow1VAYJUo9lzIFuLGBFiXtB68yLEt-i3qYQNBpfktyYrUiVG57mIS-kVe3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d6fcd9a1.mp4?token=Gz361hlIDqqfP6I4SSbQg0qD6FzXvEWjCj1mSZyQa9gqRegoMAqU6UweaMPAYQhL3ialR-aWB-9FDLgCE93WETj3VBcEpHKve0dj74mhiojFTQeK-Ec1c7nMRm8Gms8xZZB2pO98d_cuP64eIIofzHzbsBFHxsfmTxnS_oHVEZKwDXhlevVodRom9bYBNV50BPkFHNfRDJzwAmPSQ3kBbD2u-kaCoMhWZupML4i9JwcY5PjGYyr4hQNqXFgg_ybD_wuivV5uCD6m4vNWm7RGKQCEriUow1VAYJUo9lzIFuLGBFiXtB68yLEt-i3qYQNBpfktyYrUiVG57mIS-kVe3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ستون‌های دود که از میدان نفتی الغور برخاسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151917" target="_blank">📅 13:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151916">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0ac4560f.mp4?token=jsUXgd28d2AAweSlOzEJpicGhdKn7hbLdxdoI1JDsrflq1hM_cqLQl8qlYnkU6Jv68l69aMBrB5y2-LFwvJtrZObs8zIYKiXsN8StK8EWMAAxOUmWBQ2u3Y28xwp-2gtbUxrVpx3MzDCEed52s-Tom0TGQFGQQXM-Ow3x5tID1yOAeSjntH3--tAX-Qw21ErhVx7lRztQcf905tkfqqXa2dA2aTmxsHl-qhTXTrfrGWNuv7GG7RGGAunropoPJU_zt-Dg0CRpY-Dv0NCgjRe3PxaBAEThiknfIaqL6EKH5sUf7sD3WV_2t1saXrqvvIbqt3hWwmD5xzYizTKjk7v_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0ac4560f.mp4?token=jsUXgd28d2AAweSlOzEJpicGhdKn7hbLdxdoI1JDsrflq1hM_cqLQl8qlYnkU6Jv68l69aMBrB5y2-LFwvJtrZObs8zIYKiXsN8StK8EWMAAxOUmWBQ2u3Y28xwp-2gtbUxrVpx3MzDCEed52s-Tom0TGQFGQQXM-Ow3x5tID1yOAeSjntH3--tAX-Qw21ErhVx7lRztQcf905tkfqqXa2dA2aTmxsHl-qhTXTrfrGWNuv7GG7RGGAunropoPJU_zt-Dg0CRpY-Dv0NCgjRe3PxaBAEThiknfIaqL6EKH5sUf7sD3WV_2t1saXrqvvIbqt3hWwmD5xzYizTKjk7v_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل خطرناک در شهر انگوت گرمی
‏
🔴
اردبیل/صبح امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151916" target="_blank">📅 13:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151915">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
عوستاد رائفی‌پور: روسیه باید پالایشگاه‌های آمریکا را هدف بگیرد تا حملات اوکراین متوقف شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151915" target="_blank">📅 13:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151914">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
هزینه رجیستری خانواده آیفون۱۸ مشخص شد: آیفون ۱۸ پرو مکس ۱۹۷ میلیون تومان، آیفون ۱۸ پرو ۱۵۸ میلیون تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151914" target="_blank">📅 12:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151913">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
العربیه به نقل از کرملین: پوتین با ایران هماهنگی کرد و دیدگاه تهران درباره راه‌حل احتمالی را به ترامپ منتقل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151913" target="_blank">📅 12:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151912">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: شروط هفت‌گانه ایران در مذاکرات با آمریکا، از سوی مراجع عالی نظام ابلاغ شده و قاطع است
🔴
پاسخ طرف مقابل به پیشنهاد هفت روزه این است که ایران ابتدا تنگه هرمز را باز کند و پس از آن، شروط هفت‌گانه به تدریج محقق شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151912" target="_blank">📅 12:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151911">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رئیس سازمان امور دانشجویان: دانشگاه‌ها در هیچ شرایطی تعطیل نمی‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151911" target="_blank">📅 12:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151910">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d2a16f11.mp4?token=uLGpLByNhPz6rDWY5Q3fHnoclrIaKNRoEYReItVxcyZ1tMsrInUXTOnabickXOhANVmgQ3yTvHSV5FknlJC3082sV5jJG6TTw9MJ3jEhGzOQgzZkwixr-w2p0kHm_JVEUBmFhN18M0XPbrWrTLlde3KMkltmCV7HCC0KeWpo7a3-uFwIaeSmQ_lC1YbsATwLCIt9YZOx_FTLRDfWy81PFWl4wuNORrUTEQt89-FJ2JcM_backnBS2c1OpisUD3jUugIHhbIpehyaiVyB3dQrG6SN0WoJ3aZ45VEU5UcvsZ3CjkDRy43Nl_jCvZ2E2og52kDAFRSW2w9NpgYiiTnRJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d2a16f11.mp4?token=uLGpLByNhPz6rDWY5Q3fHnoclrIaKNRoEYReItVxcyZ1tMsrInUXTOnabickXOhANVmgQ3yTvHSV5FknlJC3082sV5jJG6TTw9MJ3jEhGzOQgzZkwixr-w2p0kHm_JVEUBmFhN18M0XPbrWrTLlde3KMkltmCV7HCC0KeWpo7a3-uFwIaeSmQ_lC1YbsATwLCIt9YZOx_FTLRDfWy81PFWl4wuNORrUTEQt89-FJ2JcM_backnBS2c1OpisUD3jUugIHhbIpehyaiVyB3dQrG6SN0WoJ3aZ45VEU5UcvsZ3CjkDRy43Nl_jCvZ2E2og52kDAFRSW2w9NpgYiiTnRJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از دود برخاسته از میدان نفتی الغوار، پس از حمله موشکی یمن به کارخانه گاز شداقم در عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151910" target="_blank">📅 12:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151909">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترکیه دسترسی کودکان به شبکه‌های اجتماعی را ممنوع کرد
‏
🔴
ارائه خدمات شبکه‌های اجتماعی به افراد زیر ۱۵ سال در ترکیه به‌طور کامل ممنوع شد.
‏
🔴
پلتفرم‌ها موظف شدند نسخه‌های اختصاصی با پروتکل‌های امنیتی و حریم خصوصی تقویت‌شده برای کاربران ۱۵ تا ۱۸ سال ایجاد کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151909" target="_blank">📅 12:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151908">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
پزشکیان: قابل قبول نیست که ما به عنوان انسان، ایرانی و مسلمان از بقیه عقب‌تر و ناکارآمدتر باشیم؛ باید ببینیم دیگران چه کرده‌اند که در برخی حوزه‌ها از ما جلوتر هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/151908" target="_blank">📅 12:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151907">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پایگاه آکسیوس به نقل از یک مقام آمریکایی : استیو ویتکاف و جرد کوشنر در حال بررسی امکان سفر به مسکو و کی‌یف در هفته آینده برای گفت‌وگو درباره پیشنهادات صلح هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151907" target="_blank">📅 11:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151906">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
آمریکا: شهروندان ما «همین حالا» ایران را ترک کنند
‏
🔴
وزارت خارجه آمریکا با اشاره به شرایط پیچیده امنیتی در خاورمیانه، نسبت به احتمال لغو پروازها و بسته شدن حریم هوایی هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151906" target="_blank">📅 11:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151905">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sochKFYwO-dFQMjtZ1Cd3u8lzmPX4na-pbqTVfMFp-IA5WCDtFgtUyJkZezSJX5taodeWhDIV2IpAZTxWjU9noKuUyRPMCz0CzLo9y8d6YS-VZfK4yAGV7BM7OU1nvg8bFIlQBeiI5a1lhTnJqrUDczck9R5JYY7N0Ys-mrGE-cD_H7SLQQz494nsvBy3koHi6lSh0H1D6WzejQUa4P4M1bZ2_4ZybcZWdFpS3jVaeRt-n6XnFunI0Ysy-FO1FOA8fL18AnaTkCDbT4Q22Q2a1PeIxFa9TtodUFlQnKFRCSQcRxDwVqhjafgi8_8aI1P-Wb5K6sAYyWXFBqEy51jvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع لبنانی اعلام کردند توپخانه اسرائیل، شهرک المنصوری، وادی زبقین و حومه شهرک زوطر شرقی در مسیر میفدون را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151905" target="_blank">📅 11:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151904">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM0WxbDwQYNWihXXsAo-MNaO3az1qSe867FQo0UdAY9eg7lsTA2UGuPz2vHhKeI7Djz4r78wTGLw0CfrX7Sv4CzBNwCqcysMUNQMPF8q0zsdPLi7ftUAYyzJLQNXmSxzXNKTNnXXDDbC_S7APW0Qyho3LPTu30q17kw0SC0vyibYMy6FsfuxHVeXK2g8ERLFb1h0IMjoX5nTbDe-cSzxeJoH7C9DSmV6QOj_6h6E7SOxMgvGRLuSi6I_Dha0H5sGV_73dUIzp_Vz_MRutvWURG6j7ImI8wxWLJwwMTb5LMRrKVSh8TwtN78DnLyFCdNOZN1qY9KDb7F5zEeC21W7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم: بازنشستگی در اسلام‌ مفهومی نداره و منم کنار نمیکشم و به کسی ربطی نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151904" target="_blank">📅 11:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151903">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
آدام اسمیت، نماینده کنگره آمریکا: توافقی مشابه برجام، تنها راه منطقی پایان جنگ ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151903" target="_blank">📅 11:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151902">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
حداد عادل : هی میگن رضا شاه روحت شاد رضا شاه روحت شاد بخاطر اینکه راه آهن و راه ساخته شد و این مدرن سازی های عامدانه انجام شد، اما در ازاش نمیدونن که آزادی از مردم گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/151902" target="_blank">📅 11:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151901">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
امروز مردی حدود ۲۵ تا ۳۰ ساله با ورود اجباری به یکی از واحدهای تجاری در طبقه چهارم پاساژ سعدی تهران، با سلاح کمری به منشی شرکت شلیک کرده و پس از آن اقدام به خودکشی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151901" target="_blank">📅 11:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151900">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
مشاور سنتکام گفته وقتی میتونیم محاصره اقتصادی و هوایی کنیم چرا نیروی زمینی پیاده کنیم که نیروها بمیرن و ترامپ انتخابات رو ببازه! محاله پیاده کنیم.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151900" target="_blank">📅 11:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151899">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
پنتاگون تعداد تلفات نظامی آمریکا در جنگ علیه ایران را به روز کرد: ۲ کشته و ۴ مصدوم به آمار قبلی اضافه شدند
🔴
شمار نظامیان آمریکایی کشته‌ شده به ۲۱ نفر افزایش یافت و تعداد مجروحان نیز به ۸۶۵ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151899" target="_blank">📅 11:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151898">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
👈
پزشکیان: قابل‌قبول نیست از دیگران عقب بمانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151898" target="_blank">📅 11:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151897">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت دفاع ایتالیا اعلام کرد که عربستان سعودی به منظور تقویت امنیت و دفاع از قلمرو خود، رسماً از این کشور درخواست کمک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151897" target="_blank">📅 11:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151896">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c52c1a8d.mp4?token=v1yiuj7lXwFmSuayMl_9OTm4hbN0Or9rzRJoAmjwKuwSOTPjU2L0904ZrCKbUkb9WrxUEjlNEwDp1hPh0xtBiC3Cgssdt-1ixbk_sR2XgY6Sugin5G6zv0jilErX3g5PRqhFNaD1qYbjZKu_9Zqe7Bs5npluYtvQCxcIrNoZNEOdm6nKIP034GbuhEWfz_iDE8IeVO8j5jfrpKMzpDNluOAfI9CC6q3KHL63659kYnNARDc072dWQx9CgHlGUEhycYUpqE5lKi_nns7qFibZKxhDVZDn3YSVvtCzUR5BcHVa28c7mTZruXAIO7dmqcQvZX9zCjZEwjQDHysFNwI-pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c52c1a8d.mp4?token=v1yiuj7lXwFmSuayMl_9OTm4hbN0Or9rzRJoAmjwKuwSOTPjU2L0904ZrCKbUkb9WrxUEjlNEwDp1hPh0xtBiC3Cgssdt-1ixbk_sR2XgY6Sugin5G6zv0jilErX3g5PRqhFNaD1qYbjZKu_9Zqe7Bs5npluYtvQCxcIrNoZNEOdm6nKIP034GbuhEWfz_iDE8IeVO8j5jfrpKMzpDNluOAfI9CC6q3KHL63659kYnNARDc072dWQx9CgHlGUEhycYUpqE5lKi_nns7qFibZKxhDVZDn3YSVvtCzUR5BcHVa28c7mTZruXAIO7dmqcQvZX9zCjZEwjQDHysFNwI-pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که ستون‌های دود از چندین نقطه نزدیک به کارخانه گاز "شدقم" در عربستان سعودی به آسمان برخاسته است، که این موضوع به شدت به حمله انجام شده توسط نیروهای یمنی در دیروز اشاره دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151896" target="_blank">📅 10:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151895">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6VigUa4LRuDyNhB4Qn-RUgztLRj8EYJV5lh_JHfaHJRyWjm3OQa0kGd-xt0hKN3iIK4Ouu9lyWwgwMVaEl4wv3aTn-STPJA7-AHrmty7jTgsWOc2bVcy_p0odV-Ox3aEGpI5T5DmfB8oTpK0Z7wzn-WMLPRcPxFR3KUaJBeCD3JZfnne6p6ZEbBE6nDot__awZLYntYlM0GljjiI3mHvcB8jyNWtmTP7-gJdHKSmjGY4nDb-dTZoWE-VUVam8yvBCwtZGZFPbpDvjt8qPGl4UxWuPbBKJI5WBVgAs_UaPvtQzmUDrAw-gs4J8iFvXPHDahtomrHW0qTgn05gcx1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزان‌ترین خودرو داخلی یک میلیارد و ۶۶۰ میلیون تومان
!!
🔴
فروشندگان برای کوییک دنده‌ای ساده رقمی نزدیک به یک میلیارد و ۶۶۰ میلیون تومان پیشنهاد می‌دهند.
🔴
ساینا دنده‌ای نیز در بازار به حدود یک میلیارد و ۷۰۰ میلیون تومان رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151895" target="_blank">📅 10:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151894">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات الونیوز</strong></div>
<div class="tg-text">👈
پلن ویژه افزایش ممبر برای کانالهای تحلیلی و اقتصادی داریم جهت اطلاع از شرایط به دایرکت پیام دهید
دایرکت</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/151894" target="_blank">📅 10:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151893">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avrI9paWh9GPe1UcK-vmosnQFQfsweMl_UDs7AxkdmD7z-OIMhRN0H95Y3dt61bGUKdokmTG3k33luIZaQMAv6gb6r2DxHUTm7PnE3Xyo7B_M3chtXbVd1jjjhukjoTMfxi2bcJgz9Y4e3uEqwahtGron-PFItxgKc53w4fzWdQ4t7jPm82GJeQa5g67EqJGjk2nw5DjuAHjo68vbN9N3Rk2vA_l5ADNoKqyikAqjuwpLSRenfrfIFan1ZTlKUt4cZ_vBKD0mnM5SBcFWgygVaAZr-EYS56DGySs6Nmpa94QhOyGGFRyv3oiO1KvYUmOoVf1IWW0-y_8b4hRxJE2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور عارف معاون پزشکیان: ترامپ قبل انتخابات کنگره حمله نمی‌کند، اما باید مراقب آذرماه بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151893" target="_blank">📅 10:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151891">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سازمان مدیریت بحران: ۲۵ الی ۲۷ استان ما درگیر پدیده ال‌نینو خواهند شد ما بدترین وضعیت را در نظر گرفته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151891" target="_blank">📅 10:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151890">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سناتور آمریکایی پس از دیدار با مقام‌های قطر: توافق با ایران قریب‌الوقوع نیست
🔴
خبرنگار المانیتور گزارش داد کریس مورفی، سناتور دموکرات ایالت کنتیکت، پس از دیدارهای جداگانه با امیر قطر و میانجی ارشد این کشور درباره روند مذاکرات ایران و آمریکا اظهارنظر کرده است.
🔴
مورفی گفته توافق با ایران برای پایان‌دادن به جنگ در شرایط فعلی «قریب‌الوقوع به نظر نمی‌رسد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151890" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151888">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f1497899.mp4?token=j6i6-_XM97ZgnXSP0Cwp5Bfr2TDpF03XATKyJPudWqR29puYgc48bJCsoB2L64-LWiT9RhDylpPBxTqBPgrGnQM9oLjZj7ZVdD22yE85NlCloQ4Gr-Gr83CzDwZetaaQX6mPJJSWPRlvoQHBLSFxxIUiFdsfLkM6ezUHFvpeGKHHZXGvIID17YPtshQq5A1HQ7MVLqGuvyPw1rC2w6dwNYB5W9_MMAMuYPKyoGvykIKR62nBbEhtznHMLD3ktbbLwWvMFgi3ccutuz1uUNZ0jdaktfr5HG7Sxsq4pDPg7v9a_7sQeliIRSJbA4VOfivE01awgbW_Szj-yNI4Sl7gDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f1497899.mp4?token=j6i6-_XM97ZgnXSP0Cwp5Bfr2TDpF03XATKyJPudWqR29puYgc48bJCsoB2L64-LWiT9RhDylpPBxTqBPgrGnQM9oLjZj7ZVdD22yE85NlCloQ4Gr-Gr83CzDwZetaaQX6mPJJSWPRlvoQHBLSFxxIUiFdsfLkM6ezUHFvpeGKHHZXGvIID17YPtshQq5A1HQ7MVLqGuvyPw1rC2w6dwNYB5W9_MMAMuYPKyoGvykIKR62nBbEhtznHMLD3ktbbLwWvMFgi3ccutuz1uUNZ0jdaktfr5HG7Sxsq4pDPg7v9a_7sQeliIRSJbA4VOfivE01awgbW_Szj-yNI4Sl7gDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: «این جنگ یا از طریق نبرد پایان می‌یابد، یا آن‌ها توافق‌نامه‌ای را که ما می‌خواهیم، امضا خواهند کرد
🔴
اگر اجازه می‌دادیم آن‌ها به سلاح هسته‌ای دست پیدا کنند، شاهد سطحی از مرگ، آشوب و ویرانی می‌بودید که هرگز مانند آن را ندیده‌اید. و من جلوی آن را گرفتم
🔴
رؤسای‌جمهور قبلی باید مدت‌ها پیش از روی کار آمدن من، جلوی این اتفاق را می‌گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151888" target="_blank">📅 10:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151887">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بلومبرگ به نقل از مقامات آگاه غربی:
ایران کارخانه‌های تولید موشک و پهپادش را حفظ کرده و قادر است زرادخانه‌های خود را دوباره پر کند
🔴
تهران ذخایر قابل توجهی از موشک‌های بالستیک و برخی تسلیحات ضد کشتی را در اختیار دارد
🔴
روسیه هم در حال تأمین موشک برای ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151887" target="_blank">📅 10:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151886">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2637bf759.mp4?token=Lr2xBwd4OWAnMyoWVcS1RPQfC4A3ZHCDap9d2YLPvFgf1tCwsCPokuWBLEAPfqOLoe8DWJdyTN00gYDsVmONW4kC01THS-GpwYfWyNeX0HPYPCzywO9_6qH_0GGyDrxJfI8PIkmkBgvjNNICppEYB_VPKUfHH_Mjs85AbxraKkxwdryrdfoKzX8vfwRQJ7kTQ9MoXb0AaP9c6EFyyNs8JYx0vKqGsobRY137vdB9gzFRAgHTmVhWY_h7wed_gPcxWovezl3aXxxFzMpJhGgRqnkbKzoOvP6NZkVolfYSWjUck2zsV9XtwLuOOD_BJV7C1NY-ywAx3UlPkqBnAmcN4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2637bf759.mp4?token=Lr2xBwd4OWAnMyoWVcS1RPQfC4A3ZHCDap9d2YLPvFgf1tCwsCPokuWBLEAPfqOLoe8DWJdyTN00gYDsVmONW4kC01THS-GpwYfWyNeX0HPYPCzywO9_6qH_0GGyDrxJfI8PIkmkBgvjNNICppEYB_VPKUfHH_Mjs85AbxraKkxwdryrdfoKzX8vfwRQJ7kTQ9MoXb0AaP9c6EFyyNs8JYx0vKqGsobRY137vdB9gzFRAgHTmVhWY_h7wed_gPcxWovezl3aXxxFzMpJhGgRqnkbKzoOvP6NZkVolfYSWjUck2zsV9XtwLuOOD_BJV7C1NY-ywAx3UlPkqBnAmcN4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «با توجه به کارنامه‌ام در برقراری صلح؛ کارنامه‌ای که هیچ‌کس تا به حال مشابه آن را نداشته است. این را برای خودستایی نمی‌گویم؛ فقط می‌خواهم بگویم که کل ماجرای جایزه نوبل چقدر فاسد و ناعادلانه است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151886" target="_blank">📅 10:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151885">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ارزان‌ترین خودرو داخلی یک میلیارد و ۶۶۰ میلیون تومان !!
🔴
فروشندگان برای کوییک دنده‌ای ساده رقمی نزدیک به یک میلیارد و ۶۶۰ میلیون تومان پیشنهاد می‌دهند
🔴
ساینا دنده‌ای نیز در بازار به حدود یک میلیارد و ۷۰۰ میلیون تومان رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151885" target="_blank">📅 10:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151884">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4cUE930F80mIpSQj4cOSt1zgjxyczm1n5qU6fDxpY8rqwDZ7ArtKQix5ZEG8m3NDVVv6tm74TIc95Hx4BNP4mfCf8kVluC5oWZgtqg-ACdtNSxsWeW4P5nv7ob7loOlFxTFwcA9BxT0dOEu4kcPnHybSbH1p2m7ya7mFrB_XKsRYY9vQeTGDhWPMpUY9159QPNpfX_HUE2nuGzdoZLdLQiuJ8A8ddQC2akbpIq4nMDzm2w779ry04W0IZlu7YuLNI3PN_aGHXheShAl69MBLOoUZL5-PUeWMdGfqwkhZi37OleXEv_53KQYn97FBo9i1JLlgVo6_P_erFhvjn4cZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز 10 October، تولد 42 سالگی «پاول دورف» بنیان‌گذار و مالک تلگرامه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151884" target="_blank">📅 10:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151883">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KAurB9qvNLf-xn8WTm4w4ov-U6B5QFtX1GR_A0couYRPr6-ntVKEiO5zI8I2-TL0ah60miBxsKBYxynpwXYsIf1Fx0N6rr7MO1EO_IIJ2GDBOuPB_C0H3tK8Z30OLHrlrxwDwZIcpUTEh7qae4Svx4v97_pggV4fjpqL7Nl0ULYOXJDU3e5ME2PDYhEouCneRVen78clDp1PvjyqzG8Wa3twle0ybPY2Bh6G79Df4OP2HDD5QabfRZkA3qsesbjlQl_OrSIxEUs-xMtjz8qSyGKa87GZV9gk6fX9eI0EBwisqoZXCeUr5njlyQtxMPssKjULwecO_zN-jen0wDy0Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در واکنش به تصمیم کمیته نوبل نروژ برای اعطای جایزه به ناوی پیلای، قاضی پیشین دیوان کیفری بین‌المللی، بیانیه‌ای طولانی در مخالفت با این تصمیم منتشر کرد.
🔴
ترامپ مدعی شد که به‌دلیل پایان دادن به ۸ جنگ، از جمله درگیری‌های کامبوج و تایلند، پاکستان و هند، اسرائیل و ایران و اسرائیل و حماس، باید این جایزه به او تعلق می‌گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151883" target="_blank">📅 09:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151882">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ: «ما گرینلند را با قیمت مناسب به دست آوردیم؛ صفر دلار!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151882" target="_blank">📅 09:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151881">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7o2_UpYUhnsn9xGHrtwAqLLsT-eBf7MZNzkh7rP4Zh1Ei7xeMXGG9j54VY5YUKcXHqb_OOZxY6C5jxHruEBUNjSOEMDgn4aMgn_AAh7_x6AyqZUwAdgRzeJ4Q0LyD_-y4qyC_2CeoklGh7iq7u9XtbBHKYoTgp-YV1dtExKx8wjpxB1SgYwnTldNLr7bKSOLi5KmfeTwWk0fDlM7xiXES0UVSMD4TQGoCdjTIcXp4D5e8L0d07Lw9sse_gCfUYBEGhNN6YD2cRTv4mbL0PN8fikzPffyFsyaOj_7t6GuOtw85DiBpZcR5r6FuFtrdvDxIOpSG8dozWuFKGbKVmewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: آمریکا پس از «محاصره دریایی» و «محاصره هوایی»، بصورت جدی وارد فازِ «محاصره زمینی» شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151881" target="_blank">📅 09:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151880">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2637bf759.mp4?token=i5R0S0Fc1zQo-wW5C56cYJiAQN3DVYIwh9uCaUwUbC_ldjv0T-MFMvllS5T82IY-ym0x59DMFCMeIrwWU04-UNhk_0L6bIUyNjX-sOGpPglng2MOnXejjtPbKokx2VsINAXyb5HYh_5dqretWuSGJuocDgn4-cCpBdfqD2AtZS_DO3T54Y5Kjqx8LPiSl-6eMwoeM4g7-MINafawe93FdSrtbgCLYPwQsqN1_Vpkj088HFKHi5L8othLk0w4jJzmiMuhaNpg-ojtnXZ5y45aXHOu5HURVAgrSsM1_dIgal5lvlxhVc-N3D4IzdhLmJMVhNWDRA1A-Rkn27la2Fyecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2637bf759.mp4?token=i5R0S0Fc1zQo-wW5C56cYJiAQN3DVYIwh9uCaUwUbC_ldjv0T-MFMvllS5T82IY-ym0x59DMFCMeIrwWU04-UNhk_0L6bIUyNjX-sOGpPglng2MOnXejjtPbKokx2VsINAXyb5HYh_5dqretWuSGJuocDgn4-cCpBdfqD2AtZS_DO3T54Y5Kjqx8LPiSl-6eMwoeM4g7-MINafawe93FdSrtbgCLYPwQsqN1_Vpkj088HFKHi5L8othLk0w4jJzmiMuhaNpg-ojtnXZ5y45aXHOu5HURVAgrSsM1_dIgal5lvlxhVc-N3D4IzdhLmJMVhNWDRA1A-Rkn27la2Fyecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «با توجه به کارنامه‌ام در برقراری صلح؛ کارنامه‌ای که هیچ‌کس تا به حال مشابه آن را نداشته است. این را برای خودستایی نمی‌گویم؛ فقط می‌خواهم بگویم که کل ماجرای جایزه نوبل چقدر فاسد و ناعادلانه است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151880" target="_blank">📅 09:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10de82bb22.mp4?token=THvNAex98PNOcPMROgRcFcReyiGYciOSbZfJ85gg3j2Pu2CS1QDI6lInjzPqhPiljH4sjz-UldajcJJCiWZpT3Cjx0myHqg3-NaFHRzNrQbERYZEW6xhgQujmAlw62pGH8-wx01yymUQI0fykBi-5_fTQ9-p9hRmM0HPOt1FPn6SiKhrhAErUItaoBBMzN4mc491q1mk2V9gPL6GVS6DiYtU78HywIaH0QvBN6eROEy_0AU6wvDMxCWEezjS7yTewgabuOtaFnq8NVCrJODY8gaZceI8FauYBBQU_Bz8St_kXb8EfM_OGy6-EnDJGpN5McIq2T5BYE4eg01dz4I8sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10de82bb22.mp4?token=THvNAex98PNOcPMROgRcFcReyiGYciOSbZfJ85gg3j2Pu2CS1QDI6lInjzPqhPiljH4sjz-UldajcJJCiWZpT3Cjx0myHqg3-NaFHRzNrQbERYZEW6xhgQujmAlw62pGH8-wx01yymUQI0fykBi-5_fTQ9-p9hRmM0HPOt1FPn6SiKhrhAErUItaoBBMzN4mc491q1mk2V9gPL6GVS6DiYtU78HywIaH0QvBN6eROEy_0AU6wvDMxCWEezjS7yTewgabuOtaFnq8NVCrJODY8gaZceI8FauYBBQU_Bz8St_kXb8EfM_OGy6-EnDJGpN5McIq2T5BYE4eg01dz4I8sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «من به هشت جنگ پایان دادم و حالا در آستانه پایان دادن به دو جنگ دیگر یا پیروزی در آن‌ها هستم: جنگ ایران و جنگ روسیه و اوکراین.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151879" target="_blank">📅 09:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151878">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d9793433.mp4?token=BrSkE5pFkDt_Orq2g0g2ALEyPYy5I1TJpY--XcW2h5aS6rHGlD5igV85ed8KphAUnZgvyTRcH30dpd4aGIL-Hda-gjnQPF21DtSMkt_rNEhycy44a7ZLEckJ0C4kWppilLxhC-xFJb1Z2RCReGKCqkb74ODB9guMJ-E1h_fEtAzcRMCmv7Vs6gct9pSGVlCLQiSHYusi4o7VUqkiX9nTrElA2k6mL8Am0ZhAtaE4SZg8cdPZc7uTuTYf2xyBcHQJ87sEep0aL20RZ_MVZoI0OuRVEsf3v8AskYs5b86NBQI6F4Kk_EBwMvoRoDuQFODyWrxp-HxpAUaqc1bw0Tt5PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d9793433.mp4?token=BrSkE5pFkDt_Orq2g0g2ALEyPYy5I1TJpY--XcW2h5aS6rHGlD5igV85ed8KphAUnZgvyTRcH30dpd4aGIL-Hda-gjnQPF21DtSMkt_rNEhycy44a7ZLEckJ0C4kWppilLxhC-xFJb1Z2RCReGKCqkb74ODB9guMJ-E1h_fEtAzcRMCmv7Vs6gct9pSGVlCLQiSHYusi4o7VUqkiX9nTrElA2k6mL8Am0ZhAtaE4SZg8cdPZc7uTuTYf2xyBcHQJ87sEep0aL20RZ_MVZoI0OuRVEsf3v8AskYs5b86NBQI6F4Kk_EBwMvoRoDuQFODyWrxp-HxpAUaqc1bw0Tt5PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «راستی، من گرینلند را هم به دست آوردم.
🔴
امیدوارم از این بابت خوشحال باشید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151878" target="_blank">📅 09:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151877">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
گروسی: باید پیش از زمستان ذخایر گازوئیل نیروگاه هسته‌ای زاپوریژیا در اوکراین افزایش یابد؛ ممکن است در آن زمان وضعیت بحرانی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151877" target="_blank">📅 09:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151876">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع: گفت‌وگوی ۶ ساعته مذاکره‌کنندگان آمریکایی، اوکراینی و روسی در میامی
🔴
بررسی امکان ایجاد یک «ساختار امنیتی مشترک» میان اروپا و روسیه
🔴
مذاکره‌کنندگان امیدوار هستند که طی هفته‌های آینده، درباره یک پیشنهاد واحد برای اوکراین به توافق برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151876" target="_blank">📅 09:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151875">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=O6LF9Wcrlz3N9M9yAZNWIMA_yd1m1F1aptoNrcf5xJMmLy2kuGg-49dQecyo_VFdZh6Z5oEZbfCNLl_kxXO_jWcNkvn9_CHd60aNUIXllFr543GyjmVgLWgjqg7HNGS5Plx175dUY0FPZO2EHV-axOErf8zMVgUOvwz8e2o74u3tPAS6BwfhhP9IS3LA1DNsPLMwdQRYSq-TgLT4HodCrAGUbcNLoJruDO1ZGT29sY-1Fu8aLb-kL0O4pVmmsYuV-INOUACPDyss1qDJonBa_hLUzzcnTwF-z9WuLpAEDJcVI0BkpdFJuZF-i3rZpavSxhO2a8zOMpAJHuPjg_UMgYrPXKT-qZ1pVtHUCC0QPe6xh_0dchY9kH0-INAlwVT2BQ7M8WsLauvOQzzbV_oi949NS-R3SbJLl4QOVj4gLIrCOjBaMKhZ3JqeN61K-d1v1v2W3PXAw4RW8DlncimOo6KgYa-UaF7T4UN0waVjt7jsPK157jhlmPjskoSjI4EaKAqu1XL1TysweuhXXw4kc1dpbEt0iKvX5iwQTbQLhI9oZZM5o55kcMa9qfvCalsWtSUcVKGtMp_KuDoKbui3G5ocL24pN9tcGLMSqvZS1I2uJR5Jr-eJBbtzuKUN3CWreTlNiE3_6XDb4owLWB06FKJGfCIRfubE1ckx8VtJcqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=O6LF9Wcrlz3N9M9yAZNWIMA_yd1m1F1aptoNrcf5xJMmLy2kuGg-49dQecyo_VFdZh6Z5oEZbfCNLl_kxXO_jWcNkvn9_CHd60aNUIXllFr543GyjmVgLWgjqg7HNGS5Plx175dUY0FPZO2EHV-axOErf8zMVgUOvwz8e2o74u3tPAS6BwfhhP9IS3LA1DNsPLMwdQRYSq-TgLT4HodCrAGUbcNLoJruDO1ZGT29sY-1Fu8aLb-kL0O4pVmmsYuV-INOUACPDyss1qDJonBa_hLUzzcnTwF-z9WuLpAEDJcVI0BkpdFJuZF-i3rZpavSxhO2a8zOMpAJHuPjg_UMgYrPXKT-qZ1pVtHUCC0QPe6xh_0dchY9kH0-INAlwVT2BQ7M8WsLauvOQzzbV_oi949NS-R3SbJLl4QOVj4gLIrCOjBaMKhZ3JqeN61K-d1v1v2W3PXAw4RW8DlncimOo6KgYa-UaF7T4UN0waVjt7jsPK157jhlmPjskoSjI4EaKAqu1XL1TysweuhXXw4kc1dpbEt0iKvX5iwQTbQLhI9oZZM5o55kcMa9qfvCalsWtSUcVKGtMp_KuDoKbui3G5ocL24pN9tcGLMSqvZS1I2uJR5Jr-eJBbtzuKUN3CWreTlNiE3_6XDb4owLWB06FKJGfCIRfubE1ckx8VtJcqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ملکه تایلند برای نخستین بار به تنهایی هدایت یک جنگنده گریپن سوئدی را بر عهده گرفت و پس از فرود موفق، از پادشاه مدال دریافت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151875" target="_blank">📅 09:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151874">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf368f606.mp4?token=PEQ_G8im_nxW7MkcGvOfnh1C6fm7QArZz9-2Vsv99Af-cexnwquRvWFlTccWIF_GHq9Y3ynTSJywu-9KOsGQ3U-cLOcYL4Gs7e5x5zP3heJ5IxzYGXu6_xkiPBTDWdkRiTFkMm-ixWf3cwjvCOtRhWAmh0czh7wwgRM8iNvXmxUWoldDIcNhM7SwJosJrbJ-vL2jL5uwZUTwhv_lcnkdqs-RZi8Ho7obkSmGwdoIpzORx14vZBVgxe0i1p_rUwMIZM0_JnxSn2eVRWE8bZBdtTCuuTHtyHVYJ9AUPNGxIOKKpTvMwIPsOm0QbQ2MC8zWduiG1Hi46Ru00Oeh6sxSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf368f606.mp4?token=PEQ_G8im_nxW7MkcGvOfnh1C6fm7QArZz9-2Vsv99Af-cexnwquRvWFlTccWIF_GHq9Y3ynTSJywu-9KOsGQ3U-cLOcYL4Gs7e5x5zP3heJ5IxzYGXu6_xkiPBTDWdkRiTFkMm-ixWf3cwjvCOtRhWAmh0czh7wwgRM8iNvXmxUWoldDIcNhM7SwJosJrbJ-vL2jL5uwZUTwhv_lcnkdqs-RZi8Ho7obkSmGwdoIpzORx14vZBVgxe0i1p_rUwMIZM0_JnxSn2eVRWE8bZBdtTCuuTHtyHVYJ9AUPNGxIOKKpTvMwIPsOm0QbQ2MC8zWduiG1Hi46Ru00Oeh6sxSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران یا همه چیز را به ما خواهد داد، یا دیگر وجود نخواهد داشت. آن‌ها این را می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/151874" target="_blank">📅 09:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151873">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d92ba09e.mp4?token=UF_By6INt5JIpDpMq6_j1xYFlvxfkBWr0flzKSaSJbt531FUbIWZSGxSPtHpIiBz87K1P6vy1TPB4iOerohFcew-8FX34JljdEpIIfjbWMg1o1obG1DdrT3sQcXno3v-zmBbsmROQFNvPSEsTIylGt7Is47C_WF-4FjNUmoGxqIc5NRKB4_lPeoZYc5WicEdsw9eVefBSqqZxWeDwt3sx3v9R4G0ArLMJe4Ljrl6H7PZmuEEaoqb_g3M9YMIWtsm7r61pFcr7Uqs_F4-e4brh4G5Uf6Vjo8Ix5ynmlsVVhsKIORFOe1ziJAPJLnHzRVcG-RYD6JXNJGTqFEW2uBb16VfKmA-LH5xRJ6dGEocjDXkL-NyPQn5USeHSqBf6va8XlPyRRdHR7InMRd5rBD9nwEJjC4ee7M_Sp5CzsCgavInpBjyqYKhmB99LjQ9iaWaSpLHyczZkuP6nCqL7YboBWcUeJps2pEQf_6W5Q0p_zmLZLVXDNcsctzQqZy23o1iPmjQj5EgW6u0xOx_rggwof3MfyEVW6d7nLalg_g4vSom2goxbXT0R3bX5zIIARzghxYFb8DxErC1FjsQ9NRI8llk6x1lW4E9P53bdxmMhLtv5I2DuRyDbIEua9vgLwYR3vZOGkLXJNOVJfpHW9ZTYRZXz99Lr_lksHLkDNOH1bM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d92ba09e.mp4?token=UF_By6INt5JIpDpMq6_j1xYFlvxfkBWr0flzKSaSJbt531FUbIWZSGxSPtHpIiBz87K1P6vy1TPB4iOerohFcew-8FX34JljdEpIIfjbWMg1o1obG1DdrT3sQcXno3v-zmBbsmROQFNvPSEsTIylGt7Is47C_WF-4FjNUmoGxqIc5NRKB4_lPeoZYc5WicEdsw9eVefBSqqZxWeDwt3sx3v9R4G0ArLMJe4Ljrl6H7PZmuEEaoqb_g3M9YMIWtsm7r61pFcr7Uqs_F4-e4brh4G5Uf6Vjo8Ix5ynmlsVVhsKIORFOe1ziJAPJLnHzRVcG-RYD6JXNJGTqFEW2uBb16VfKmA-LH5xRJ6dGEocjDXkL-NyPQn5USeHSqBf6va8XlPyRRdHR7InMRd5rBD9nwEJjC4ee7M_Sp5CzsCgavInpBjyqYKhmB99LjQ9iaWaSpLHyczZkuP6nCqL7YboBWcUeJps2pEQf_6W5Q0p_zmLZLVXDNcsctzQqZy23o1iPmjQj5EgW6u0xOx_rggwof3MfyEVW6d7nLalg_g4vSom2goxbXT0R3bX5zIIARzghxYFb8DxErC1FjsQ9NRI8llk6x1lW4E9P53bdxmMhLtv5I2DuRyDbIEua9vgLwYR3vZOGkLXJNOVJfpHW9ZTYRZXz99Lr_lksHLkDNOH1bM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پالایشگاه نفت روسیه ساعاتی پس از توافق با ترامپ هدف حمله اوکراین قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/151873" target="_blank">📅 09:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151872">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I69kzcri7ipm9gnJA_d16C-Qu_gnPMEouDhlW1Yig-e2bWsZqOOpW5q_PTPyHw_AyDvmw7LDdFxNlPMAOhttMDxK9s2YSuLvCWiwR5_rZx9drE1zkniw-He20S-mIvtEGF2DqL65q69Y1AhEKtD4dmlIfvlfyyfnYWSYVx2Qu0Iqy_t-BUkNmAH_E4wR19LS796ZIhpEUf-9UPccQyHez_-AffjCjnTYrKGUqfQ18W51HnZ3xUU0vHS4N1rIN7-1AVAaVhmvVPDZqPUNWrBl8_x6Q1fyRrbnwt9zW6z2Nv8ax23l4ksR0X5FVy8Psvl6J1ISejrVdbkq7_LqhRPvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کرملین:
در جریان تماس تلفنی، نه ولادیمیر پوتین و نه دونالد ترامپ نمی‌خواستند نخستین کسی باشند که تماس را قطع می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/151872" target="_blank">📅 02:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151871">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-jHcfVj-pwfhl0H2CrZBDrRznLUvdW8RCD77fwXYnJcnHC-C1J3MLgJ-jBFEJZbohkRK0n7Fx9RaoYQBoat1dRlzbBlZeU2mS-rEuJSryCLF2V0hRHbG9CvYcEzlU_Rj3lj89dn4YbIqLdquLFwfnryIJPzZflfkiBrQ7RF1vVeG_JTe2nyGpWJVqrwYFckjWcc37yoG2LZiA9IiYyj_aFuVgI5EVMwb6EOD57Kiy7Nih8bqqRvRVxEuVfbovHyGProlsMw4EGET7rlgcyO_9qYTOAHY7VtQ6vWhult_AZPmeRU8awe9FIOYgaSpCLhofm6AIDoO4kpLg7LZpdJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم:
مهسا امینی حقش بود کشته بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/alonews/151871" target="_blank">📅 01:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151870">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
مارکو روبیو :
«ایران تلاش می‌کرد توان نظامی متعارف خود را آن‌قدر گسترش دهد که دیگر نتوان با آن مقابله کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/151870" target="_blank">📅 01:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151869">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExmUPfh2ai3Q75UQYo9hZAxN3P1QQNc0Qm7sULlp972f6DKdP2pvZpOVR3KKD_rhRP3eHCNCMR33HJlgztQ8pTr0exH4uC0zTYFJk_ST7Udj-AOrAvdmzi6ZBkEzGNnVWb5tkIQ_SaVjHHP6BIQzTC1Zciz5Yk5Qs0tywlztXe9f0JOCe7gHk9ytcssuW4m0BUAgXAbGYhNObT6tfrpfPQdtXAwO1i8MANqI3Sidk18_gxjlF7xDOqlTaUhuCekFrIYwiWTWG-l9W3We7kDbIDySWakkI6hR2yCusE7C_aJRYX1fKDicaq56dPkRzBoMjPPxzULN0mS_XFKSQ5DDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو سایت پالی مارکت، احتمال حمله امریکا به طور ناگهانی از ۵ درصد به ۳۰ درصد رشد کرده
🔴
علتشم این بوده که اکانتی که قبل از حمله به ونزوئلا و و جنگ ۴۰روزه شرط بسته بوده و ۴۰۰ هزار دلار برنده شده بود
🔴
اومده روی حمله به ایران شرط بسته
مدیونین اگر فکر کنین که ترامپ بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/151869" target="_blank">📅 01:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151867">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7LepRZ-jThVYvV_PYozQrBr2Kl9U0vuCD6L3ey0ucngtV7Zvno9jY0PMiwYbPdEz-rO7k3b5kMEIY9Fj2tGZ5pYAOvzoWyhVViLZpcJMgxy52QzUSlJnTmjiqHWcZA0AwNw1SbQ5yqi_XgivryRy830QAnjTXp6UDpNHSKlyjmpN7G01oe9iqp88TGbUyCVypv0B7iTIreaq3F-G8R8y8RfOcJ0qOadne_clTLhriHm2PQ2wigeOncM8TOpkRbrr2Wds_xniOP_PF7oDeAg3EGzp-U58IOzf6P9-52zrjpW3EeO6v2_-mQ3vCMolNaQt94vnpdS-ZkzzftQfTNtzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلوزیون اسرائیل:
غلامحسین اژه‌ای تو صدر لیست تروره
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/alonews/151867" target="_blank">📅 01:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0925073180.mp4?token=EYuEssxAYs-rDzuB2qFS7PhD_fu8_vdHOyaOR56Zu6pBs08QRT2dAWUWe3TthViPFGwqOPsnk8r7aUhTXiCDrNWtIB78Cl-KxFwe-oWtpA-ZGEICO-3YgJRGfsvy9KeDgLPXGz1cXVu6a609fgMD7hnrznFDa3n5x49DKICQSIdDAzZe8OApurVQQbRvbJ5uZbCLmPUkdQx_RsCOstom48kk8bRTIyu7H3Hyon2eZnxkT-X-gRxviiYlvNjyEGOikzkhHHy2OTDgJKp-Z3HFbmNSSVURV9qYFUyAlZqsrYBYJ99GhjH6LNHqXQe7mIAVXPL1xl-2ZYFZwprS3FJZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0925073180.mp4?token=EYuEssxAYs-rDzuB2qFS7PhD_fu8_vdHOyaOR56Zu6pBs08QRT2dAWUWe3TthViPFGwqOPsnk8r7aUhTXiCDrNWtIB78Cl-KxFwe-oWtpA-ZGEICO-3YgJRGfsvy9KeDgLPXGz1cXVu6a609fgMD7hnrznFDa3n5x49DKICQSIdDAzZe8OApurVQQbRvbJ5uZbCLmPUkdQx_RsCOstom48kk8bRTIyu7H3Hyon2eZnxkT-X-gRxviiYlvNjyEGOikzkhHHy2OTDgJKp-Z3HFbmNSSVURV9qYFUyAlZqsrYBYJ99GhjH6LNHqXQe7mIAVXPL1xl-2ZYFZwprS3FJZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: زلنسکی گفت که به دلیل توافق نفتی‌تان با پوتین، شما ضعیف هستید.
🔴
ترامپ: چه کسی این را گفت؟
🔴
خبرنگار: زلنسکی
🔴
ترامپ: باشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/151866" target="_blank">📅 01:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151865">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5uo8D2lQMYtpaIB81gl_ePpg-7jZ4bjzStZ_m7k56aF-jlro-Zq-jlPeChvUOdSY5iJUID9UyFVu_MpTrkrzLmxeEDJdAw5MLxxRwbe0gh2TXCrCqqqU7FQ-jpeBavlKIxE5VjbsXxMW-WHl-ccQIj5cL3bU-NrOW8Q94k3mPPAnS5cTntchpDvqjQBPoqPsQoViEJXmk3FP2J3kneXE4Gs7QHby5hEZwjE66cpS0vqfQybzJ1sahGSn11Lh-H12F6ZT3-6xY_PorFO9ODifC7uOg-dsDJqxu9otnrdOc9kFZ2E5cQ2OcUnre_YZmHRae5J5Hng2tdHUtm2Betv0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: جنگ نزدیکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/151865" target="_blank">📅 01:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151864">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
منطق عجیب امت معکوس شده!
قوه قضاییه فاسده
رئیس مجلس فاسده
رئیس جمهور فاسده
وزارتخونه‌ها فاسدن
بانک مرکزی فاسده
جمهوری اسلامی خوبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/151864" target="_blank">📅 01:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151863">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
در اقدامی عجیب پناهگاه‌های شمال اسرائیل باز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/151863" target="_blank">📅 01:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151862">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/شلیک موشک به سوی تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/151862" target="_blank">📅 01:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151861">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceab173908.mp4?token=QCOt9hfQzD6DhIGKwMxjGbJsYXL6VUUqhQlr2AkEu98Wjnqj6wJp5wulN9X5iz09VkDkAOBO0rypWC6MSQHIhCg-bAN6nq3fAbLsw9j99whw3IxhIhQCr0_g7bUbqh3u8Buvz9n5BBmARFjOgS65pcrEo-HLGhrlFANMUqbi5lzyDv7fICWht4bCb-kfQA0ccKKtMUN07MDTr8qtxFSosAn1ajuM8vK5Wb2JIERMMaBwhj6ZQaRQuaxBmt2wrKJsPowh13VJhD5VTwuPlmOYt1TnI8KY0ModujSbXht77D7rTB58aViw-7yQbx4wyKHWCSSsTb2CKcA9a350I9VyeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceab173908.mp4?token=QCOt9hfQzD6DhIGKwMxjGbJsYXL6VUUqhQlr2AkEu98Wjnqj6wJp5wulN9X5iz09VkDkAOBO0rypWC6MSQHIhCg-bAN6nq3fAbLsw9j99whw3IxhIhQCr0_g7bUbqh3u8Buvz9n5BBmARFjOgS65pcrEo-HLGhrlFANMUqbi5lzyDv7fICWht4bCb-kfQA0ccKKtMUN07MDTr8qtxFSosAn1ajuM8vK5Wb2JIERMMaBwhj6ZQaRQuaxBmt2wrKJsPowh13VJhD5VTwuPlmOYt1TnI8KY0ModujSbXht77D7rTB58aViw-7yQbx4wyKHWCSSsTb2CKcA9a350I9VyeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ظریف: اونایی که حجاب رو خاکریز میبینن اصلا عقل ندارن، مسئله مهمی تو زندگی مردم نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/alonews/151861" target="_blank">📅 01:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151860">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آمریکا هشدار تخلیه فوری صادر کرده.
🔴
مدارس جنوب تعطیل شدن.
🔴
امشب توی تهران تست پدافند انجام شد.
🔴
صداوسیما اعلام آمادگی جنگ کرده!
🔴
فردا و پس فردا به شدت احتمال جنگ و حمله بالاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/151860" target="_blank">📅 00:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151859">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiG02H6N3fgiR6Zoi_3C5Xz-SKaSQm78mTnaPGHYYW0fB6N2nlvu_df7wpWjZVtVkId94xkAYAfJQu6I_7GZV1ncB2TYfy1DiYu-_07mJJ17IR6KTmnh3-zOV32b_892oqq4BVdUYQ4G7INsX4zspBa3Z399qolkdeIzFLTidvjJQAAyp0va6TTS3CA1liPgUpzgZ-puuNenVjhOn268viYZ5-Y2HJOdowL1Z8szEfmcUMjSr08bd4qOp7cQzcfERDJVFflV4PD528O_J6zV8BRUra75-lE03d-qOEeic-SuPR40NmnLNoV4pUKrFrv451MjJTnPPbg4auGCP6Ll3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط فیلم...... ساشا سبحانی آقازاده معروف با یه مدل معروف دراومد
‼️
مشاهده</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/151859" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151858">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f4f9a44dd.mp4?token=OVoEjAfXxW3ehvXFamrDSQf3rFIDWQsAtxb0xxI2IuwsSyG0TMakmwGWoqsVbtZUbCBxelspHXgPwkh5TkrSrSfzhgwuJB19rZBfeFUBE3SI953Sc0DrddUv0IYyFdBV5t20S7ut_XBudB-Bt7DiCvp5BVoZPUixFZyJg-37R2gYnDYgpC2LWNFdRHpM8p52jrETcxaD6d4mlNnBfsEuYArwnwCiWz71ML1xyTkRpRIivy95B6dK5fD9GMT8a9hHEpP-xpYzL2gl2M1__9tZwExlGOORxEaM22xLM4IOsaujYd_32ClO0smTKluFg5rWxuV4LR5UYSgcQ5uaVIXi3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f4f9a44dd.mp4?token=OVoEjAfXxW3ehvXFamrDSQf3rFIDWQsAtxb0xxI2IuwsSyG0TMakmwGWoqsVbtZUbCBxelspHXgPwkh5TkrSrSfzhgwuJB19rZBfeFUBE3SI953Sc0DrddUv0IYyFdBV5t20S7ut_XBudB-Bt7DiCvp5BVoZPUixFZyJg-37R2gYnDYgpC2LWNFdRHpM8p52jrETcxaD6d4mlNnBfsEuYArwnwCiWz71ML1xyTkRpRIivy95B6dK5fD9GMT8a9hHEpP-xpYzL2gl2M1__9tZwExlGOORxEaM22xLM4IOsaujYd_32ClO0smTKluFg5rWxuV4LR5UYSgcQ5uaVIXi3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک خبرنگار خاورمیانه‌ای از دونالد ترامپ، رئیس‌جمهور آمریکا، درباره حملات حوثی‌ها (انصارالله) به فرودگاه بین‌المللی ملک خالد در ریاض سؤال کرد؛ اما به نظر می‌رسد ترامپ سؤال را متوجه نشد و پاسخی نداد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/151858" target="_blank">📅 00:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151857">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏
👈
جابجایی پرترافیک نظامی آمریکا در منطقه
🔴
طی ۲۴ ساعت گذشته، ۱۰۴ فروند هواپیمای نظامی در منطقه شناسایی شده‌اند که ۱۲ فروند از آن‌ها هواپیماهای ترابری خارجی بوده‌اند. این پروازها شامل ۸ فروند هواپیمای آمریکایی و هواپیماهایی متعلق به کویت، فرانسه، بریتانیا و آلمان بوده است.
🔴
همچنین، ۲۹ فروند هواپیمای سوخت‌رسان، ۱۵ فروند هواپیمای شناسایی و جاسوسی، ۳ فروند جنگنده و ۵ فروند بالگرد نظامی در کنار سایر هواپیماهای ترابری در منطقه مشاهده شده‌اند.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/151857" target="_blank">📅 00:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151856">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
شبکه خبر: آماده جنگ هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/151856" target="_blank">📅 00:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151855">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
منابع داخلی: موشک ها بسمت اهداف قفل شده اند٫ به ایران حمله شود بدون درنگ شلیک میشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/alonews/151855" target="_blank">📅 00:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151854">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
حرکت گسترده هواپیماهای ترابری و سوخت‌رسانی نیروی هوایی ایالات متحده از شب گذشته آغاز شده و تا کنون ادامه دارد، و این حرکت از نظر وسعت، غیرمعمول است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/151854" target="_blank">📅 00:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151853">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
صفحه فارسی وزارت امور خارجه امریکا
🔴
شهروندان امریکایی همین حالا ایران را ترک کنید !
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/alonews/151853" target="_blank">📅 00:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151851">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO3wUVU5V_qpjun_Oetw8u9QBvO3MPb9zcBwoMyrCTFqlod7y8kkgJ_WCHrAFrJAlc6piD8saPVC52lOJ4RumOlgGopOLwXWP5tIvv-dx17jyDGcahkVmAwIVzGlfin63Wuj78ZEDWuYsAM8oRk2hM6xAdxDqJEdTDjKu05SuH9_WRAeD1yWbK-cBjhKTcdVxv4t2SbTzFpLkUd_HHbGs-NJA02I51DCu5DtzskW75ARS_gDz1n23WuFD1Vsa30qqCorumnCBzfNtN-gVRjfql79tqZxLqHN2MjMoMQCrK6BWL4bUTaQBaA4MBEbxXwlGRf-lPIoqwgulK-kxCi7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، کیتی زکریا رو به‌ عنوان جانشین کارولین لیویت در سمت سخنگوی کاخ سفید انتخاب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/alonews/151851" target="_blank">📅 23:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151850">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/npRY7brwapZMV1EdzhvKJYXpxDbJgkpslyuu_s8GCl7OYftQH_9bsTDwftMQgR9blDWLPXIe1Y77idYfi7X6KW6dsPUIe6o0jDZGkc2P-deMmAXuaggSsaa-vQLW8ukNq6L2Ki3wlJNBKYijEv13RLUjH64R8B7ERDWB8tBIgduUh3kZv1CGftfwe7HHYsHoLw_UcfbdutVvt50kmLzAlexR6YqKNX7_tXqJy8t4d8tzZh8PgrElHpDE93rHSGAVM0OosUF2e-NrL0tF0d6EDz9C-LRNt2b4FktMamCHZ4w7QRpNre1GS9E3VuNJKkOnqIhmlU_N-pPCk6IPi0wp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر فارس از تانکر منفجر شده توسط سپاه تو تنگه هرمز که حامل گاز مایع بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/151850" target="_blank">📅 23:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151849">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RETB48sXWFGN8H1NfWiLtohfs1F23hKzE5exYF-gtidEQG-kLDrAsSV9r16r1xw-gfalDdl3KKbLqbKFv1Y3bkqnyVFdtUS6R5LlCPeNQE5swkfd6UE7PxCobJz2e7IDgMhts6wGwGoaOoLp1tCzBJdtHAc0E3VFibILbQcUSL8T5Rxg3E3ucA5my-dOFN0jVpkgTB5uykMiCYClsKIeITS6qp_M2DZEsScn0iQrBX4Rj7f66Tv5n2tA8ZQALkYlBR7bLhYSthFwurJpSZ4ozd6wdO54hVu59rCOWYh9yLLN4d1XGG9o60F1jD8hF0JNQYixObFHgx1APhhdB3uokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بیرانوند رفته هتل اردوی تراکتور که برای بازی با الشمال آماده بشه ولی مدیرای تراکتور تو هتل راهش ندادن
😂
@AloSport</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/151849" target="_blank">📅 23:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151848">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6JUSpV8QJp8-P_hWXIXFd1MiBYjpEUPgDoqxlM9OPo3Aa4_I4pWgBkArSab73bogyYGfUJKHA4XlYJYZI9PKfFpIir4sUmrx8npgezWQt993jbtmIKywZIB-XGfwGHF-xXLlX4TT4zx52eXlU06QyYvQhmnZpGghLRq6ZctH3d3OLSwYsOHaE6vF63VndbrvyulBqvxVl0qTjo7yLPYYlrx_fBiFKfJ1ywu6DlfQqAnxQ-acHUZiEH6pIvDaVK8KBSzUTCngYtWwXrQviQtpMTO8K7fhhIOJfFvbUvWIdWztnOhTtplXQrTDdn29NEgYg7nqsy6x-JnsgLI__n2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم: مردم حق ندارن راجع به نفت حرف بزنن چون مال اونا نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/alonews/151848" target="_blank">📅 23:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151846">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScskJVGfFXSW6sRavJUGkPN9CiQ6kwaLbnmb78x2QxyOML2uimmIXlwktZqEZAzAaPlH9WJdW-ppY4q8TvtwwKI-YlZXpO0GFQkdqAeiYW_cjnbkaR3TJWbwoZcAPmJi_C_lFOPpLlB4DZraOiJe1mIKcRwR1joCrfia7bnaPanpQlwOHq0IXxouYXamBiagUxk4IsI8IqhWlnTgA89VvfBBrTyjzc6dY0BnJTsNfxmnh5pia-yzEWI5f_kSmtt-hrMMpDXitoYBPL847FWUcJToJTtbrka2cr47CTbe28VvKwlR4UzJKFwkHN0p9diRkM9bcnf4m_39Y7sIRgu5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/151846" target="_blank">📅 23:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151845">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4174043f46.mp4?token=tKSuVlNNw0Z5AJSZtvnmFRkRvE8crwmAq9ozle-F8vuJfBtpuNqsKh3JlOa56x9jMmPnVE4vFgxpPNpeBIpzHCZItBzt6aMch0U1uAwf0Wv8ewacXnprdF5y8flMlE1it7B2mKkwsnz-H7D145DPvwpnv30aUcWfBUBhAnwu7wIZHu2JTt7ySTEg0BwRk1J8huMyz1PdaXCQjNS6b9BDj-hB1j_b21Oxks7ltAxD1EnKYsLn2U-Y6MJFNXlySha9I5tE51LS-N74tZ9mHJ4KVjaHD3nbiv-p_GyOraOS7rfzH0rIyzAlVDzrkynpPNP5BvTYEO74cF6Qi8nuPwD23w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4174043f46.mp4?token=tKSuVlNNw0Z5AJSZtvnmFRkRvE8crwmAq9ozle-F8vuJfBtpuNqsKh3JlOa56x9jMmPnVE4vFgxpPNpeBIpzHCZItBzt6aMch0U1uAwf0Wv8ewacXnprdF5y8flMlE1it7B2mKkwsnz-H7D145DPvwpnv30aUcWfBUBhAnwu7wIZHu2JTt7ySTEg0BwRk1J8huMyz1PdaXCQjNS6b9BDj-hB1j_b21Oxks7ltAxD1EnKYsLn2U-Y6MJFNXlySha9I5tE51LS-N74tZ9mHJ4KVjaHD3nbiv-p_GyOraOS7rfzH0rIyzAlVDzrkynpPNP5BvTYEO74cF6Qi8nuPwD23w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی ها در باب‌المندب
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/151845" target="_blank">📅 22:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151844">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGylcmvWkJr0qZk0d6GpU0TVWr5CDS-H8Bt09Nrpa9-NCIKJ-6NBWPUWBx9y57n01u19mbCN0XZ3iAko4RXE8Msp_HFTlZWIdzoUyRkQ98tTTenvTqZyrOBf94c1jmaiozoq-0vw9CNVBoCO3IswqUVwgXOyfIgoD32lUEDHLBDKenhKjKAag_rnjHvYpitTNgX5AWxbdWmwz3_nUP6qVEPOPwxNb3IqjghxGT0jy-rMNWuZyTWVcuLTfPzmWPa2zM07kWtgWf-kHdvvLLFnYHooUencnyA1hT9hYZpDH0gTYzRpBZ8XPkxQujkWeM6OSXqp1fCdC39gVo0RHsB_Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش قیمت نفت بعد از خبر صادرات گازوییل به آمریکا توسط روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/151844" target="_blank">📅 22:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151843">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
👇
👇
https://t.me/+WqvKmlByMJMyMjA0
https://t.me/+WqvKmlByMJMyMjA0</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/151843" target="_blank">📅 22:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151841">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
میرسلیم: تیبا و کوییک میتونن با خودروهای آمریکایی رقابت کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/151841" target="_blank">📅 22:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151839">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kntwo3GzKQ8-gLcrznlgPQlNY6_bJnfpCMh12bgZfvwyfxopRLwAd-Bwgxqb_Y4eiX-xp8ISrgwW5QcjJ_OmnMCSFkFb05U3XrlBQpfKQzx4bDGcNgG7nLMx6ANyvSDPDk_fp9iqKJ-AQzF2EONGo2irCJhEyHfwrsBB6r0UaEyEs3BITXY7b2D0x9bqz1lZSlyZ1TkDjP4Q4rzB87C9G2LAZPa9oMIO6B1tKlZPWrqHODUz3suSSYVTDZcjTCjpH7yRHel19JYFKJ4m5pLlI6-dAiWizCCQTGLw8CT7p_Za1dsmd_zEnZVT18bxeRvJlk_cVseYiCy-gySUFBoh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنر عجیب در تجمعات شبانه: به یک ۷ اکتبر برای بازپس‌گیری اقتصاد ایران از غرب‌زده‌های اقتصادی نیاز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/151839" target="_blank">📅 22:43 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
