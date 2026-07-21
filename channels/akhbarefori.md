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
<img src="https://cdn4.telesco.pe/file/kmqVdmv_W0POiirb7oTCLSt75G3UT-bHbk_Ek4AO566FNcRNq3KbQu7-HFZVIiFupW8mwzsROQJ0aQNxrsesJxYOaLfuH4GExlDV8Qk0SPtcFbDR37sT7p1sBT6GD5MWgFymVroJBtRA-ZFj3sTmWtERcAkWJ1YHmqd_qUQk1dDldrkXrj_VpJtVnpbf06ZmFKtO3OsB_qt4z-z2dxSGLGECp-3S0YgYnIVJlOGRbWM0BRbDCUJsG-N3lCLkcHkZZ0GMltNZRhiTINpLDIu0RThW4XVVfRzFLe_6kYHiAYzeJApr_8wyDzAHrkmrf2l1OaUYFypft3xSmW7umG9m-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 15:36:11</div>
<hr>

<div class="tg-post" id="msg-673773">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تکذیب تجاوز دشمن به خرم آباد
🔹
معاون سیاسی، امنیتی و اجتماعی استاندار لرستان با تکذیب برخی اخبار منتشر شده در خصوص تجاوز دشمن به خرم‌آباد گفت: هیچ حمله ای امروز سه‌شنبه به هیچ نقطه‌ای از استان صورت نگرفته است.
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/673773" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673772">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار هرمزگان(Admin)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2VdsOzbB1WED2iHFX9MzbS3nf8-wJBbUOLHWAyBDu7CtcQG1O7YPPQPit-nps-EbcwBKQdVHcV08JMHNoXklLBjgfz8kn8E0EhrNWMlnNSdDF9Z_k93TAZ757b06kMdqbI9NrW0hw9yStTvMOkhUj6U_yAHydg3dqyIn7s0p4piXB7kqEbULUxfxVoKcoAgu1IOiVnkTdyy2bBndQrrYnOlYKs8AKQFANd1uwcX6q_lym-IAf7mIpUEciIOgMRB-xXId6_97P_BB2bHGcKIdUqmqXK4W-_XvS4MdEi_fZHOKwQZFkW6aGRLpUx-aRy7o5JscEdQ7ZiawufDkM7-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام آب شیرین کن ها درجنگ آسیب دیدند؟
#همه_باهم_برای_ایران
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/673772" target="_blank">📅 15:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673771">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aecdbd5f84.mp4?token=SLCMVuCJo3680--Y9Sv8kdsknwaZQOd5jH2AHROCB74KHvb7apNSaJDWkTWJbuVdXXdVCSCmNj3yOq-s8A_ION2OzgwVWytfgmvSwx0Yc9yEA8MUuAIWpdV5wHj4Blhgxq4Dm2IkQnKHf60jRVOa1i7yXfbW0kU-q4d3AsMKdlVCEzH_Ces9Pe1FxC2hnaVdaiKu2B_IvPeXd7J4ZW4-oogrMVT05s8Xwo77MzQYIoj7kSqe5ywyaijCxx8Oly4EPcNHb-kpSt85wr8Tk3je85-Cm3RO9xOyWUhYshiJDeHC14cNe-3UXjgHPnO99ucowmJVSt6o4BwhWd6pTMHqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aecdbd5f84.mp4?token=SLCMVuCJo3680--Y9Sv8kdsknwaZQOd5jH2AHROCB74KHvb7apNSaJDWkTWJbuVdXXdVCSCmNj3yOq-s8A_ION2OzgwVWytfgmvSwx0Yc9yEA8MUuAIWpdV5wHj4Blhgxq4Dm2IkQnKHf60jRVOa1i7yXfbW0kU-q4d3AsMKdlVCEzH_Ces9Pe1FxC2hnaVdaiKu2B_IvPeXd7J4ZW4-oogrMVT05s8Xwo77MzQYIoj7kSqe5ywyaijCxx8Oly4EPcNHb-kpSt85wr8Tk3je85-Cm3RO9xOyWUhYshiJDeHC14cNe-3UXjgHPnO99ucowmJVSt6o4BwhWd6pTMHqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خسارت گسترده به پایانهٔ صادرات نفت بندر الاحمدی کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/673771" target="_blank">📅 15:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673770">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6d90750a.mp4?token=NqzOHkJcqK9cD3XzYf2rIMmi192qqFI2v1vNORfKIJQMe9QT7hIUWWZgsUTmML3jNDCLmrZpmiqoFnwb8eJbMfvTmyICi3HGqQ9xBEnX59DbJNn9ufQGJuOUoLo2dwGactkLs_PBfGVoqSg8Ku3blk_aDRWCj9rD9jD0UPdPTMqnAlKWOHRinZ0zBv3s3kWoWZByS0OSSTwf0Br__O2CpR0YgjtZjKdx8y-BwWMXUTJxot-YM4XM8XdQxSsonduc8EjVSLMwz91RwHxF9DuB_199TWTfdGXvligbm-whlBMOmqpvDi2xlbsV6rWXKmb-mWITR8Du6pYmBOA-w3QbMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6d90750a.mp4?token=NqzOHkJcqK9cD3XzYf2rIMmi192qqFI2v1vNORfKIJQMe9QT7hIUWWZgsUTmML3jNDCLmrZpmiqoFnwb8eJbMfvTmyICi3HGqQ9xBEnX59DbJNn9ufQGJuOUoLo2dwGactkLs_PBfGVoqSg8Ku3blk_aDRWCj9rD9jD0UPdPTMqnAlKWOHRinZ0zBv3s3kWoWZByS0OSSTwf0Br__O2CpR0YgjtZjKdx8y-BwWMXUTJxot-YM4XM8XdQxSsonduc8EjVSLMwz91RwHxF9DuB_199TWTfdGXvligbm-whlBMOmqpvDi2xlbsV6rWXKmb-mWITR8Du6pYmBOA-w3QbMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی دل از غم مالامال میشود اما عزم و اراده باید راسخ بماند
❤️
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/673770" target="_blank">📅 15:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673769">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
یارانۀ ۳۰۰ هزار تومانی تیر به حساب سرپرستان خانوار دهک‌های ۴ تا ۹ واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/673769" target="_blank">📅 15:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673768">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOSjmHuHGGqa5oM1ch19eOmoDvD0LhwIB-IwXPIJTlcFI3N5LuGA2R9cKdAREJ-S8bQh0oe6YpP97R2JDj102wVQNWi5ZI_ZErMbX0RbV-6OJruuobFTcnYcvWnn_9jvWGxCEzUBYeH4t2v0CIUYnhTIFgtstyIJu5cY-1cizI7iD3VBmSsn4EYpXa7Rb73urd0MfmxugMbeqoQY_atHB_L34R6pE3pcyX4JPo4ZKOLxLJScnYCu-yYQ2_yi6kU4SGyj8_YwZQUbYbTdRMt02_Fk7PjAiZpPrc7n9ckYiieZUC6rgLNnMcBZPX9dIy6aCNA51wcDccDhFVXlBUYwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه العربیة: دیدار عاصم منیر با وزیر کشور ایران
🔹
فیلدمارشال عاصم منیر فرمانده ارتش پاکستان در حال حاضر با وزیر کشور ایران در اسلام آباد دیدار می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/673768" target="_blank">📅 15:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673767">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر اقتصاد: اختلالات بانکی در اعتبارسنجی فعالان اقتصادی اثر ندارد.
🔹
سپاه ابهر: ارسال‌کنندهٔ فیلم پرتاب موشک به شبکهٔ معاند دستگیر شد.
🔹
تولید نفت شرکت شاماران پترولیوم در اقلیم کردستان عراق بدلیل جنگ تعلیق شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/673767" target="_blank">📅 15:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673766">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
حمله موشکی به الزرقاء اردن؛ جزئیات و تلفات احتمالی هنوز مشخص نیست
🔹
بر اساس گزارش‌های اولیه، چند موشک به‌طور مستقیم به شهر الزرقاء در شمال‌شرق اَمان، پایتخت اردن، اصابت کرده است.
🔹
تاکنون مقام‌های اردنی درباره علت انفجارها، منشأ موشک‌ها، میزان خسارت‌ها یا…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/673766" target="_blank">📅 14:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673763">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IBTVVu0kcZmyLN0-li7UtInnIXL7xA_CM6E3LU4yULc6q3_5bEjlwKnsFXtEqAmR45yaGTXVR9fnfSuESsgQRTTzTvM9v4im4bzbsd-ERcwXUA3Yz7Q3ntG_TcZZpwJy47V8cEE2t93qTqsWalwv6O6DKbpHeBR5zl3wq-sGgcZyf0pz6np20y2AfFNJrdhyymvH2MgdYRI1K8oPR66h3aaWFuJ9lVgAd_wLq1RRPD0OYWrvjh7snZ4ATc31jPiBeDBqgTPYVT0xx06MN4BQaYil-GrtM1v8SXlr_HJBOCDj7-K_d4PMOBONURdJbaR9PkClHTR1PsPDfb5iGsV9Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c8_RDvjPJ5hlf9wwS767Plf7877dqjzv9Pdkmb4OXNk5mZIBDX2OT1Ghi-xzkSvxGY9hYU6K68PZy6BYkp1xBqgX7izghQzubKAZ3zlwtXzAktTqkKNehJ1Fxsah7DHexgyhBDfnhpJgJkixegTySxh7NVe9MVW5IW1Q2hjrAhty7dMZNmIfM0w7JQkIAfkyYSGtb0m7HPMBXaUBZOG3fK-NaUYh4dt50C4Oc-N1b5vu3421Nra8hcthK0nMJU-Faw1tqd2snRTY9XQB_vRZx6zlq69hmzB9YmlLvjmkzGVx7IFOqr6nWJbz1ZVV9FS8QVJIUhnmW67bhzvgHagLZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/570c5d9e43.mp4?token=CWn6L79x-b9X192OTWMrZCofzg45FCYdM4kNUgsBbtShH8WIt2nTgCqjhvevmxE9jYuHifn562Y8L3f5UzET4TEmQOqIv73d6r7Md_qTeUpZgeN4XyIi6B4RWN5W8hkOBz1Ig6CXkaPMamLgJ6kWTrdpK2X53vA2w1Oqruqt-jxDuo9oPUkp-1gT_3OqT-R8dXSyhE275GyhBKttjJZfBfFbOLwSqxcHsxIBngKulfxBtq_iNIvWdKjDSmnRkN-wyTHvlrX5I92YmVos9DcUCf34gCGuVtLOYa3BwHmSXtkx7Pvi8UY8LZpIosc2FDkDceggglB1NqivTVkKmVS3xyUlcohK9x9qo83xlHzEycwq-prCTrNPuJs9agQZK0MlSnJPdBnOVETBOOtiVbfun_UpMrRn2NofvbGZnY8F-IqVLX0Sty0cMfRY46dNgxVGSE7oe1Ne5ATKgMf7PSnWdDEtpYntcaRH4GLO3VfRxq9611cqm_gYvbes_yFFnqmM8NDAdgbogKz9k-GO4XVWZUotKL7D_dZYfIs3_b1uXTltX846hO0ZwqfgGSU9uM1hTZMD6DNvcue9pkdMgRahlSJVkBiJPBens79L6xFPko5EL3OMgpQyYPrcge8N2xdy-v_A7bccg-vxrVOCT5j6QVAlJt4lQOsF_tyIrBUXg3I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/570c5d9e43.mp4?token=CWn6L79x-b9X192OTWMrZCofzg45FCYdM4kNUgsBbtShH8WIt2nTgCqjhvevmxE9jYuHifn562Y8L3f5UzET4TEmQOqIv73d6r7Md_qTeUpZgeN4XyIi6B4RWN5W8hkOBz1Ig6CXkaPMamLgJ6kWTrdpK2X53vA2w1Oqruqt-jxDuo9oPUkp-1gT_3OqT-R8dXSyhE275GyhBKttjJZfBfFbOLwSqxcHsxIBngKulfxBtq_iNIvWdKjDSmnRkN-wyTHvlrX5I92YmVos9DcUCf34gCGuVtLOYa3BwHmSXtkx7Pvi8UY8LZpIosc2FDkDceggglB1NqivTVkKmVS3xyUlcohK9x9qo83xlHzEycwq-prCTrNPuJs9agQZK0MlSnJPdBnOVETBOOtiVbfun_UpMrRn2NofvbGZnY8F-IqVLX0Sty0cMfRY46dNgxVGSE7oe1Ne5ATKgMf7PSnWdDEtpYntcaRH4GLO3VfRxq9611cqm_gYvbes_yFFnqmM8NDAdgbogKz9k-GO4XVWZUotKL7D_dZYfIs3_b1uXTltX846hO0ZwqfgGSU9uM1hTZMD6DNvcue9pkdMgRahlSJVkBiJPBens79L6xFPko5EL3OMgpQyYPrcge8N2xdy-v_A7bccg-vxrVOCT5j6QVAlJt4lQOsF_tyIrBUXg3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشر شده از خسارات وارده به یک پایگاه آمریکایی در اردن در پی حملات ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/673763" target="_blank">📅 14:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673762">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aba3d2697.mp4?token=UtQsJHvER0uIqoNdLwUzVdpIJTTQukgmRAd8dLxNKYv7mi0PBtImMOYMtNGgQSMgEhacldSrxCthhuuJGZrkoiPpOK48h9NSe_FQamTCiC50NZ-pAOUQgQvBXZB6oJsabHAC5KcWw8hUjvI90GoETT7GIcRMkSOYOjSb8eRY72yZ1K59C1zAFGRM0iG5JVbWa4jXia5JhWCNepZ94hZurlOIkxftHc0xe0FS4CHFZiyOq3Znlze6C3haLLvDwT2HmtJ0VDjptjcfRGtcxUwidzqJcJwz5Biz7ypsiPH0USihyKhTTKmGVSjWW-yq7Gc60oZ4Uw73h1cNaEJTNcNBVDYcJVvGeNsy3mSgDo60w9vexPVN5_a3YeeJ4MGP4tUmKXA4yGPHu6Xvfbds4BaIc9RCKR6OB0iOnh2yvZuxMiErf44fFs0va8B1S1sgi3eeWMvQSbwyFqzuVRCvpZNJ_a_GVXykC1j7CiAheNc7A0qYafJkFHyl4kSLe5tUvTqdeG72Dx1EmlWcUrjw90nyIoDBt01HO9inne8S75JJ4Ps8r9NeS8ggbX_ZWVvryzaoKA2_Smy88TIrGAtjkxd1mHNh_I5zoMtNwN0WMZ6Zi8ZtO92yh8o63Ut_XRJn53on3E7u3QEEAoHEI8dPCGt96kO1aZE5ozW6NwbcGcyG-Ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aba3d2697.mp4?token=UtQsJHvER0uIqoNdLwUzVdpIJTTQukgmRAd8dLxNKYv7mi0PBtImMOYMtNGgQSMgEhacldSrxCthhuuJGZrkoiPpOK48h9NSe_FQamTCiC50NZ-pAOUQgQvBXZB6oJsabHAC5KcWw8hUjvI90GoETT7GIcRMkSOYOjSb8eRY72yZ1K59C1zAFGRM0iG5JVbWa4jXia5JhWCNepZ94hZurlOIkxftHc0xe0FS4CHFZiyOq3Znlze6C3haLLvDwT2HmtJ0VDjptjcfRGtcxUwidzqJcJwz5Biz7ypsiPH0USihyKhTTKmGVSjWW-yq7Gc60oZ4Uw73h1cNaEJTNcNBVDYcJVvGeNsy3mSgDo60w9vexPVN5_a3YeeJ4MGP4tUmKXA4yGPHu6Xvfbds4BaIc9RCKR6OB0iOnh2yvZuxMiErf44fFs0va8B1S1sgi3eeWMvQSbwyFqzuVRCvpZNJ_a_GVXykC1j7CiAheNc7A0qYafJkFHyl4kSLe5tUvTqdeG72Dx1EmlWcUrjw90nyIoDBt01HO9inne8S75JJ4Ps8r9NeS8ggbX_ZWVvryzaoKA2_Smy88TIrGAtjkxd1mHNh_I5zoMtNwN0WMZ6Zi8ZtO92yh8o63Ut_XRJn53on3E7u3QEEAoHEI8dPCGt96kO1aZE5ozW6NwbcGcyG-Ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازخوانی نامه احساسی سردار ایرانی، میرزا کوچک خان جنگلی از گیلان قبل از شهادت در برنامه محفل ستاره‌ها
🔹
ابتکاری متفاوت و اثرگذار برای آشنایی نسل جدید با قهرمانان و مشاهیر ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/673762" target="_blank">📅 14:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673761">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olENsoqLVHwDfxhTKeJXqvaedJ28Chce9g7NbynbPooM417Ph6k5k1b12Zdtoy6fT0wQTJUOrFjGbxWUl1TkEOI6Ef4IsicPUCHWzjmFYGp-iEBVzFXCZhsTzLRlTqJMZpsNzZn2-0pxKbOXcpkLd7R06LyqzbNR3O3tcqXYERctOOmxMXkm9oSeWQFmqbmFybo9JRQ0TtOzxAXoOICS6so0soLAlAN_jf_MF19WvWo1GBSrVT7L6ZWVHFj6_4AeB0bjAkZWx1paN5zuAC0n1OZbuq9FzviFDbweBLozvmfxgX4lP4F2CelaKEFIF3_QgJid3WQoSkBGtZgH5dew1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ مدل لیموناد خنک، سالم و خوش طعم
🥤
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/673761" target="_blank">📅 14:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673760">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HinoIPC79bW-z6ksst5-r40CQ-6qGL3c664jGrpbpLpQwW2w8t7_nQFx3YnTu9_0tsCYA7AWKZuazxjt4xSbuhyGC512xdGMsk1yAAwbAKt4Wcew3R_yCxfhTzMQB46axoZgC8id8aAXsmfvisiwct8sOq60QmWpK6yv1TJFagcnZ7kIG32S8sG-EO66Ow0uri7LLF5oNkXQSUJnG_So0f4_gPkr-ioqumsmkXYwUpfB4KLjY3Yro5lr0f7mC_dmLdvGw3F7yg15k_EHQjpErcvl7EcM9W3oPK_LJ3YXAXJpeo_372Cw93qb6VG8p1zpaweD-ulIkm2yL4EP-N6wGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام چادر تجهیزات بالون شناسایی ارتش آمریکا در اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/673760" target="_blank">📅 14:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673759">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6945763e.mp4?token=WHqUnkCKPm-LP0QwOq604AL1hLAfflbzZVkGcFi0s8prkRYagsHHIGJoe4RDEisebaL6UaW9pfiYZeLJuA8GK_BOaqXMXezIoIUqgWjJQlEw01x0GHlklU6JSY984KworSZHRi9YxYU_bim5dBrUMQW0LYavSk7JJXLFzoT99GBA-bKQdEUNQinTjzYc9mpIrFcHVUG7U8mCgBztNkIb-vvs_tmuEeocBXcHobwuOWZ12_nmlFntJFIcrusH3wTphbSp62oCo96WuA4H1p5u9Hm95HeoX6U24ihw3jxN1IpegeVLM1QjGGMPTBo31rv2J__3-CwfTGFQthHMU6THtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6945763e.mp4?token=WHqUnkCKPm-LP0QwOq604AL1hLAfflbzZVkGcFi0s8prkRYagsHHIGJoe4RDEisebaL6UaW9pfiYZeLJuA8GK_BOaqXMXezIoIUqgWjJQlEw01x0GHlklU6JSY984KworSZHRi9YxYU_bim5dBrUMQW0LYavSk7JJXLFzoT99GBA-bKQdEUNQinTjzYc9mpIrFcHVUG7U8mCgBztNkIb-vvs_tmuEeocBXcHobwuOWZ12_nmlFntJFIcrusH3wTphbSp62oCo96WuA4H1p5u9Hm95HeoX6U24ihw3jxN1IpegeVLM1QjGGMPTBo31rv2J__3-CwfTGFQthHMU6THtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ارتباط ما با رهبر عزیز روزبه‌روز درحال افزایش است تا بتوانیم با رهنمودهای ایشان مشکلاتمان را حل کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/673759" target="_blank">📅 14:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673758">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
انفجارهای شدیدی شمال کویت را لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/673758" target="_blank">📅 14:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673756">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUkplhbyya31yCWuiAvvluFHjttTm-0-ptyJRPY3gSgUQBW95TpemOoBmAgEIMMc8KjcQnsfZ2QYMMz-XgDCPrE1O243M5R_pN4IgMv6K6vC1WjQOmUBBCS-IhSM903fr4nVMdKkgbr4bCnmcBvw5-4G4MoNtoBDwnSIzRP96DGgBMDxoB9MCFycHUp6NvSjUknY26WosW5F2A2s7hGOlaEySO6dWS094GIB0R2zjfhDQBSVVDVoY4BfcSiC-m_-Flf2MOzXchMNeU2W7wdINCIdWa-J8cnxGqrXZ2vqcrTYnhdK9uwPcDukkWBYsQLp5dUkoROpz5_3VXGBG9cs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FyUkARKt3w6R-n0GFRIyhr0dCZgHCrhbdO_9VaioS0dWv2kDuYuz0x95ItzkYzhMl9PBySPNFDiTqWdtTMIb00wEJl50bmlOdamghiuxSAGX3ltxDhS_nvFDSSwa00RuxLo_IxVV6D3_kInGbM0uxsu8EW1H2hnP-SQR2ugHAxR9nNsTIZiVfnVI_D7GzOgXljGid7crSPtLBEClVoqP1vkoVEir4gG-fmslEcxQ_kBPEpdCYiYq4if1paan5Hdz_T2_sVvsW1NUuQHBjLSPJtDwU8t1qPZ4Kum_qq95gXoU7XcPxWDrd-1afd4RCF3WizM9EM_2v0AR2yYdtr7uFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر ماهواره‌ای جدید از انهدام محل اسکان نیروهای آمریکا در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/673756" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673755">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای شبکه اسرائیلی: تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود
وای نت عبری:
🔹
مقامات ارشد اسرائیلی مدعی‌اند تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/673755" target="_blank">📅 14:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673754">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR2mvTwfU_HqTy9t4TKVD8LcbT2tXShYbrfWKToHEli8rO6xfl_fTOCIR7qNDm8jsEr6X5ApxRA6JEvwU_xoj1xiLGXwNUlEF49B5VIJh1B1cAEzNHr2VSm_0sW-2q7LXN1_Yw-R1fmt3e7jTFjtYfcogOX5AoxDL0VVXN8HcEnSR-PPN-9mvVZHZOsx7UqRE0C5EIrdWd4VKsWRJ8yU5IZQR-eXtm1psjLYGuKFnTcWe22E3eB0_xdSg1EHV1WnBVsfGIOL3ayEtdmoqaa37vpwuCVJtN0JAGO89E77FruLFyWk3yijqxYYOZhF0UMxGODjVWKBYvsa-9KLO4RORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خودرو ۴۵ کارمزد فروش خودرو را در استان‌های درگیر جنگ حذف کرد
🔹
در روزهای سخت، همدلی زمانی معنا پیدا می‌کند که به عمل تبدیل شود.
🤝
🔹
خودرو ۴۵ در راستای مسئولیت اجتماعی و حمایت از هموطنانی که این روزها به همراهی بیشتری نیاز دارند، از
۲۷ تیرماه
به مدت
دو ماه
، کارمزد فروش خودرو را در شعب استان‌های آسیب‌دیده از جنگ حذف کرده است.
در این طرح، فروشندگان می‌توانند
بدون پرداخت هیچ‌گونه کارمزدی
، از تمامی خدمات خودرو۴۵ شامل:
🔹
کارشناسی تخصصی خودرو
🔹
انجام مراحل اداری
🔹
تسویه آنی وجه
🔹
بهره‌مند شوند تا در صورت نیاز به نقد کردن دارایی خود، این مسیر با
سرعت، امنیت و سهولت
بیشتری طی شود.
📍
کسب اطلاعات بیشتر درباره شعب مشمول طرح
🚗
ثبت درخواست فروش خودرو
🔗
khodro45.com
📞
۱۴۸۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/673754" target="_blank">📅 14:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673753">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تعطیلی ادارات استان کرمان در روز چهارشنبه
استانداری کرمان:
🔹
به‌دلیل افزایش دمای هوا و موج گرما، کلیه ادارات و مؤسسات دولتی در این استان در روز چهارشنبه ۳۱ تیرماه ۱۴۰۵ تعطیل خواهند بود. این تصمیم به منظور پایداری شبکه انرژی و حفظ سلامت عمومی اتخاذ شده است و شامل مراکز امدادی، درمانی، خدماتی، نظامی و انتظامی و همچنین شعب منتخب بانک‌ها و بیمه‌ها نمی‌شود.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/673753" target="_blank">📅 14:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673752">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تیزر قسمت هشتم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سید حسین موسوی که به دلیل ابتلا به بیماری کرونا، روح از بدن جدا شده و به خاطر گران فروشی‌های دنیایی، در برزخ متوجه اشتباه خود می‌شود و همچنین عذاب انسان‌هایی با گناه خودکشی و رباخواری و زنان بدکاره را درک کرده و در نهایت با بردن نام خداوند، فرصت دوباره زندگی کردن به او داده می‌شود و بعد از تجربه تغییرات محسوسی از جمله رفتار با خانواده و اعتقاد به وجود ائمه در ایشان پیدا می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سیدحسین موسوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/673752" target="_blank">📅 14:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673751">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سخنگوی دولت در جریان سفر به هرمزگان: لنج‌های تجاری بدون فعالیت نظامی هدف حمله آمریکا قرار گرفتند
🔹
انبار بازرگانان که محل نگهداری کالاهای تجاری و مصرفی مردم بوده نیز در این حملات آسیب دیده‌اند.
🔹
مطمئن هستیم که با تدبیر و پایداری موجود، می‌توانیم پیروز این جنگ باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/673751" target="_blank">📅 14:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673750">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره مالی اتاق تهران همراه بنگاه‌ها در دوران بحران
🔺
اتاق تهران با ارائه مشاوره تخصصی و رایگان در حوزه مالی، به بنگاه‌های اقتصادی کمک می‌کند با بهره‌گیری از روش‌های متنوع تأمین منابع، استفاده از ظرفیت‌های حمایتی و تصمیم‌گیری مالی هوشمندانه، تاب‌آوری خود را افزایش دهند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/673750" target="_blank">📅 14:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673749">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ممدانی: جای نتانیاهو در دادگاه لاهه است
🔹
شهردار نیویورک، زهران ممدانی در مصاحبه‌ای با روزنامه نیویورک‌تایمز گفت که درباره این موضوع که آیا اختیار قانونی برای بازداشت نخست‌وزیر اسرائیل را دارد یا نه، در حال «رایزنی و گفت‌وگویی فعال» با اداره حقوقی شهر نیویورک…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/673749" target="_blank">📅 14:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673748">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f2a5a7eb.mp4?token=sMYGgxHipe1caFrHnqwOqC1XTTi4Gm1fpy8XFPoJUw7Wu3Isiab1tD6nEjJusCLpl_hYaMzewNudHiHD3Ehf-4wqK4ZbxxajFRrfHIs0dhnmfyco7t-JOuqgKLr7J_n13IDfTOjo-8kq3LyHkrkIy94hq_TZXXGCCBDPSyLFGbWElY-BlYwFtYA2bt8flwS7fIzEV2C0jNPVGSaPY_4cPPmcBbjjj8zfCarQ93nBSGj0_KlOVpqlDKXUhlvbFLGTvqMCfZVizWhLA4VlMQCxVnL8C_YDH7Y-HTDVaV9tVljZdBgKl9y2NPfAA91OJxFPibiD4wNoNMxonivyqQsHuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f2a5a7eb.mp4?token=sMYGgxHipe1caFrHnqwOqC1XTTi4Gm1fpy8XFPoJUw7Wu3Isiab1tD6nEjJusCLpl_hYaMzewNudHiHD3Ehf-4wqK4ZbxxajFRrfHIs0dhnmfyco7t-JOuqgKLr7J_n13IDfTOjo-8kq3LyHkrkIy94hq_TZXXGCCBDPSyLFGbWElY-BlYwFtYA2bt8flwS7fIzEV2C0jNPVGSaPY_4cPPmcBbjjj8zfCarQ93nBSGj0_KlOVpqlDKXUhlvbFLGTvqMCfZVizWhLA4VlMQCxVnL8C_YDH7Y-HTDVaV9tVljZdBgKl9y2NPfAA91OJxFPibiD4wNoNMxonivyqQsHuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یادت باشه که ما نمیجنگیم از خونه زندگیمون دفاع میکنیم، این دو تا با همدیگه فرق دارن...
🇮🇷
❤️‍🩹
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/673748" target="_blank">📅 13:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673747">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان: دولت متعهد به رفع موانع تولید و حمایت از صنعتگران است.
🔹
شورای شهر تهران: رایگان شدن مترو و بی‌آرتی فعلاً به مدت دو ماه ادامه دارد.
🔹
قطع برق ۴۸۳ اداره در مشهد به دلیل عدم رعایت الگوی مصرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/673747" target="_blank">📅 13:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673745">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjsKPaAXcaOsL76a7-86KsyX_imCThL6mCukR1cTen9DtI8LdyZP-gS357tD4AYHa1eTcBZ5T6fQotXX9UWJV2mprxeBEZInMdEUBsPpC3UqRX_IKO8kx29gFjVHsjQ4LLakBFCCj6rwMWNwEwScJqXcRYlJuU1qPWiYE2bjdm54M-73OyKVN3sSP-YeWeyO_3WHjHaSaKb4cPmFz-0-8uRZHq7X1Gx_abYpvuvJ4ts8dEnVb9nZVQhv6br5eD5pKWwHthMHT7sSfCw4Zld4lwzhL9UF6GI8_wuRh8H556JnRtbpZurjwdWo52m3LNCJ-VPSe3hWaFSCjRnjjOi5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmUaJw_spWWsmOxbK7vowyV-A6SGoYEuwVjJnkZfHRPEjrzpNHbDn8XUvyZv-OHmIZgPRyqtoQ3zA9x6JyDsLbI_o-jeLQuEy3Mc_Isq9UR4KpzBXZId_8Bx9xPqVKBpUk-6o0kLZXxMmaBg5_Of4n1cSVqlVTFRkSd9YDg0O5MPWSj7iDcq93_AAtgotJ_t3wbFerenrgMCn9SW6ANfqnIT6gmcn7xRubwqg2UAfiBEB6UmDHHSSfHKdKqRfmg0WxSDUkc-LGzzS8FHY7b3XyE9RO6vAacTvkW09KdiRkIeQoaEtQ0HbkaaMlrypld4zNdo6iiWmo7QBtdIDwoXQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تکذیب وزارت نیرو درباره ادعای جنجالی فردی با عنوان «مشاور وزیر»
🔹
رحیم زاهدی در یک استوری مدعی شده بود که به دلیل بی‌حجابی مادرش از ورود به فروشگاه وزارت دفاع جلوگیری شده و پس از تماس با معاون وزیر دفاع، از او عذرخواهی شده است.
🔹
در واکنش به این ادعا، وزارت نیرو اعلام کرد زاهدی هیچ‌گونه سمت یا ارتباطی با این وزارتخانه و وزیر نیرو ندارد و عنوان «مشاور وزیر» را به‌صورت جعلی استفاده کرده است. این وزارتخانه از پیگیری قانونی موضوع خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/673745" target="_blank">📅 13:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673743">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حمله به نقطه ای در ارتفاعات خرم آباد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/673743" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673742">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mki0w3XvBS2qU_9cJZf_h9aU3TxMCEdQ9Dl5Nt7zAwNrCUQgOJ6mewyb8ZcrDQjdMO7TKduOO32Zqail-xiJGGiDV94BAe2gPRXsURetB66ncG6wAHdx3jBziJyz2YODaV_7HzzsEOxhnWw8ho4VD3BJi5LZmzf0RLC_0-hawTY7Krx6RxR7C_dpJb5tlpfCpVN1NGrjpFxvZq24kBeDSprY7sZXCEN5thP_6ziXmVz4zcJvERY-2Tj68TIGL6YFn0IqjSnny21vCwbaJyv-c_5qXUlIdPOg2XsGs7r9PxY4nMSWK4u5ui8nrMH_o70aBO63otXGNindH2RnHOWbrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس شورای اطلاع‌رسانی دولت: ما منتقم خون رهبر شهید هستیم
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/673742" target="_blank">📅 13:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673741">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx_Wkqcn3Y7q_7SDCOcF_onzO5vIInFU1x6Uv9NAqpRGgE15Iid5nVlSzeiwNmknDNWC1P496CYYS2OMS1TOLVuQxyJqwqVYEeOEGhe5N3ClRUOjEYUyqZ9Dn_v4qlVOGlzm816mVyWpxiTb8P43goZLGJkCtmODyvNTzna-rKidt8llqAOLwPDASd3_m7UZh5-KI2mjHSmO7alzSBvrNBb5XZaJ1x_GngzvvHdiw7goH7lCwysiEvbQYOjDdssxWX6BuqzYwdg_q4PEBTbhL2XZhLGQPromahqBN6I9VCUjpBICbWpgn3JMhjsUnYq5hnH-t51Hd8bzpqA7_qs1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از اتمام جام جهانی در آمریکا صحنه جنگ تغییر می‌کند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/673741" target="_blank">📅 13:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673740">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
انفجارهای شدیدی شمال کویت را لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/673740" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673739">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRLAVWIEDKTFfQxMgj8-YjnJ6eEaPrCpkJVFaFLBwJr5gRI7feZdXuK-yT4UhUYj1QbSVSR0qptkkAkX1-if2TKKKmRzbLMthjZXw832M88NJkFdvkd7Su69vcAGRRJ9249QFtZqqlKQq0QnqCVLTDpgU7iaoc42DL5T6q2ciqGi_6FlhUbX130qYG4GK20ucD0at5dTGxzaxhsuAjruNsZoaEmYliYXVlLBD783DXopLvN1Bzh_RJsL8V1qEvb5TK85RPTIat2Oc0_EVuVTXPq89Nk8CPC800zzAL3NX4aUxRPnWFo-GJLZvLtSqjgnqA9cV2ny9IsSspeBiU7bpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جایزه‌ای که مسیر زندگی یک نفر را عوض کرد!
🔹
گاهی یک قرعه‌کشی فقط به اعلام یک اسم ختم نمی‌شود؛ بلکه می‌تواند نقطه شروع فصل تازه‌ای در زندگی یک نفر باشد.
🔹
در مراسم اختتامیه یکی از بزرگ‌ترین کمپین‌های بیت‌پین، خودروی تمام‌برقی Volkswagen ID.4 با ارزش ۷ میلیارد تومان، به برنده این کمپین تحویل داده شد؛ مراسمی که با حضور ناظران و فعالان حوزه فناوری در باشگاه انقلاب برگزار شد.
🔹
این کمپین با تحویل رسمی جایزه پرونده خود را بست؛ جایزه‌ای که برای برنده آن تنها یک خودرو نبود، بلکه اتفاقی تأثیرگذار در زندگی محسوب می‌شد.
🔹
بیت‌پین که یکی از پلتفرم‌های برتر تبادل رمزارز در ایران است، پیش از این نیز کمپین‌هایی با جوایز بزرگ از جمله اهدای یک بیت‌کوین کامل برگزار کرده بود. اهدای خودروی برقی در این دوره نیز ادامه همان رویکردی است که بر جوایز واقعی و تحویل شفاف آن‌ها به برندگان تأکید دارد.
🔹
گزارش ویدیویی مراسم، فرایند قرعه‌کشی و جزئیات تحویل جایزه در لینک زیر قابل مشاهده است.
[مشاهده گزارش تصویری و مستندات ویدیویی رویداد اهدای جایزه]
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/673739" target="_blank">📅 13:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673738">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سازمان انتقال خون: الکی خون ندهید
بابک یکتاپرست، معاون اجتماعی سازمان انتقال خون در
#گفتگو
با خبرفوری:
🔹
مردم فراخوان‌های اهدای‌ خون که در فضای مجازی منتشر می‌شود را جدی نگیرند و تنها فراخوان‌های رسمی سازمان انتقال خون را دنبال کنند.
🔹
خون ماده‌ای است که تاریخ مصرف دارد. فرآورده حیاتی مانند پلاکت تنها ۳ روز و گلبول قرمز تا یک ماه قابلیت نگهداری دارد.
🔹
در بهترین شرایط افراد هر ۳ ماه یک‌بار می‌توانند خون اهدا کنند. زمانی که فراخوان می‌دهیم می‌دانیم در کدام نقطه نیاز یا شرایط بحرانی وجود دارد و فرایند اهدای خون را تنظیم می‌کنیم.
@TV_Fori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/673738" target="_blank">📅 13:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673736">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFm5Y8yy4nXXn1BEOcQ3t38Or5-WnAamARNXN37kZom9Zi4tg9E3x_MzieZ21Ey6l78Ye-eolj6YT-JZviH2oM56bKEWXyA1ITrCiVcO-ZRdQu0XFtz_SuHci8iJMr5_L8m7_w4KTSZ9jytePyG4g6JcTzodytRsbjCFHz1H9A6i-VZKmom98BWBFcryWZk1vKTGKTy5YD6oruS1LT76Tu-5TwJqk48LD-z_FZEel-h1GdLjyd_8BE8ZES5haS1RQLn2AcdRqeOISd8sIaX5M14qUM8s-3FWEqLBK6ScPoWrRwRZ8UT8Ag__nzEEN1muU6Z8Gu70xJq-rBx_rK71Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvOHUHRbvYFRyRbmyixKYfQ234SBgamXAQ-owK4rQqCH-KjY9JzjNvQo3Vk92aEjvUxbZu3FebuUm_EssTLZFleAc3TcVQxu9oW8-W0RGkVcMTM8qZNJzQdZmljN8evQcZRt9WBR4vwW5SvJ7PFHD3xtwOc6YZ_reiXKMC1iwENCnCSsDWnpsnNm2TQKFajFmU0FppV_7lpVRGM4QDgTurhfOyeTGoskUl7_zOEonEmEIhDoWtbGkyXBcU1mAxlacDm7fpE44drmhlb4p8VRrCvxtQNci13R_tX0pZyCNUeN7cF1Fj5aAT7x5gD5Q2VZ7cbWUSHqZ747CvM_dTPjFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
جایزه ملی انرژی‌های تجدیدپذیر ایران به بانک تجارت اعطا شد
🏛
🇮🇷
🙏
بانک تجارت در دهمین کنفرانس و نمایشگاه بین‌المللی انرژی‌های تجدیدپذیر، به‌عنوان بانک برتر موفق به کسب جایزه ملی انرژی‌های تجدیدپذیر شد.
✨
محسن طرزطلب معاون وزیر نیرو و مدیرعامل ساتبا، این جایزه را به دکتر اخلاقی مدیرعامل بانک تجارت اعطا کرد.
✅
جایزه ملی انرژی‌های تجدیدپذیر با توجه به فعالیت‌های اثرگذار بانک تجارت، به‌عنوان حامی و تامین‌کننده مالی پیشرو در زمینه انرژی‌های تجدیدپذیر به این بانک اعطا شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/673736" target="_blank">📅 13:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673735">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
آژیرهای هشدار در قطر به صدا درآمد
🔹
همزمان با تشدید تنش‌های نظامی در منطقه و حملات موشکی و پهپادی ایران به پایگاه‌های آمریکا در بحرین و کویت ، منابع خبری از فعال شدن آژیرهای هشدار در قطر خبر داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/673735" target="_blank">📅 13:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673734">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
نیویورک تایمز به نقل از شرکت ردیابی کشتی کپلر: تنها ۱۲ کشتی روز دوشنبه از تنگه هرمز عبور کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/673734" target="_blank">📅 13:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673733">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیرهای هشدار به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/673733" target="_blank">📅 13:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673732">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شنیده شدن صدای چندین انفجار در بحرین
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/673732" target="_blank">📅 13:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673731">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
حمله موشکی به الزرقاء اردن؛ جزئیات و تلفات احتمالی هنوز مشخص نیست
🔹
بر اساس گزارش‌های اولیه، چند موشک به‌طور مستقیم به شهر الزرقاء در شمال‌شرق اَمان، پایتخت اردن، اصابت کرده است.
🔹
تاکنون مقام‌های اردنی درباره علت انفجارها، منشأ موشک‌ها، میزان خسارت‌ها یا…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/673731" target="_blank">📅 13:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673730">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
شنیده شدن صدای چندین انفجار در بحرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/673730" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673729">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
امتحانات نهایی ۳۱ تیرماه در همه استان ها غیر از هرمزگان برگزار می شود
🔹
ستاد عالی آزمون‌های آموزش و پرورش با صدور اطلاعیه‌ای  در خصوص برگزاری امتحانات نهایی پایه یازدهم و دوازدهم، اعلام کرد: امتحانات نهایی پایه یازدهم تمامی رشته های تحصیلی، در روز چهارشنبه ۳۱ تیرماه ۱۴۰۵ در همه استان های کشور غیر از هرمزگان، مطابق برنامه ابلاغی، برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/673729" target="_blank">📅 12:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673728">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
تجاوز هوایی رژیم صهیونیستی به جنوب لبنان
🔹
منابع لبنانی اعلام کردند که پهپادهای رژیم صهیونیستی به سوی شهرک المنصوری در جنوب لبنان بمب‌های صوتی پرتاب کردند که موجب ایجاد وحشت و هراس در میان ساکنان این منطقه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/673728" target="_blank">📅 12:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673724">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcA7Opo00WRnzMRfyEwWC9endW0B1cfUByPZXFLJb-plFzzP7uvLTG5Zof10WuDsEIe0UedLY9nCiPbQHX5p3XuTmtzcGu8RlDlVFQAi8OBJvKUjk4LZQIFbd-8CJ9bLq3-rixZouxoLWSpz4Mly4awT2lE_Wu81FmuWU8Ap5BmVLM2V0JJV6Bkv9SMXX8waZ3EeBkkfkBJIqsY8WgP610ws0bpsm6OfvOZMr_lsWYTw6k5c0_jidX4EmQjgwAqqMpxqMOkB1v2m2uEnB8qfU8IFmDpS0b1fXiTALTHsW0WdNlNIVtWRx6pbPmPqf-G8oCdLeMXVpwzb2dJZnzJf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_-Zd68BHv2jP4KJUd20pJtehniM8I8JMsmpAauNBeMx-a85v_9A-pqHYjNUXnu6156T6kngSPhh4Nm5A8g7mLd_nb8LcfpUluaLdH-rL7Fdw6b0teeG23mSCuSwM6eWf7x1k6Vg6PpIOgRx6I_6W4iGKYttVBHgNV4ONHc7M3y0OHrc0LX20hE5SYmpaMiy90_zve6j9Ku4UPplRwwpv3Y9gtZSwzJiJuhk7xRF7t82hB2fPGuM1tGddLBncmWjFiUimw6BT3MrkQ_Y_AQm9TdGxpgpQDYj7V3-2j-gR0rnJPzSLFJJIZ6vGkvaVnCyzPe2yG-1ZdRDfvNZ_hAu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryYeBoqLLjw9tLMzGd-NycMLfO7CdKPevnSMkfo7S4EmU63RT4HUSFM9dWr2WXyWT2Gk5z5qwSjSCom-dtzHj2RGOVF92WGFnMIadQBOtXg1_KXb4Ya4yyWn2NcThJog37ZFt52wHcmEVQhBKe0Qcn8DiXGqUIL4_IMHSPnVmvO2BAtSkV_hFJiInMCpo_TXck0nJDFRvTrqbXj4GaSDBqm2vc_31G0JoLtbVVJT01xmTb_5agBhXGKsmwPZPQ3xqdP9R9gUECVrZyd6Ppj2VL8jofXBRozah5Sta6Kph8h5woxkl-CmartyNT2ry_IQvVuOKM6JQqgB9zsNY3j0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SP9BkNKhkCqpuMAWeuQ93SEZkLYXbao5edaMrBsMdbCYkVQ550voCejK-EIzYOrnoE_I45Bh71fld94cHdDiGY5rdlUSqApf4iqpe2NQRqtIcM3bwTAn-5zyzXgcP9I5CqGJUR_m58lKOfhyqpzBDxV9QxcZJVhcwA60SO16Hw_syIGCV7HSTAU3CGK02FB41HscP3TKFgencs23FfJKoG3UZ3NrOP5XcPVQjp7iWBx-Vo29iqSi8BsE7y32ohonoloV1M_vCaio04AbuDR4qJ3U_ZaSliBI5leKUpNHsQh6g9LLjgYmq9wm5k7J7FhkfrsRNV3ExIV5v5u3K7W7WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هر قطره آب ارزشمند است
🔹
با چند عادت ساده، می‌توانیم کودکان را به قهرمانان حفظ آب تبدیل کنیم و آینده‌ای سبزتر برای ایران بسازیم. #همه_باهم_برای_ایران #صرفه_جویی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/673724" target="_blank">📅 12:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673723">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
جان‌باختن کودک سه‌ساله بر اثر حمله سگ‌های بلاصاحب در سنندج
🔹
جان‌باختن دلخراش یک کودک سه‌ساله بر اثر حمله سگ‌های بلاصاحب در سنندج، بار دیگر مطالبه دیرینه شهروندان برای ساماندهی این را به صدر مطالبات عمومی بازگردانده است.
🔹
این حادثه در حالی رخ داده که هفته…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/673723" target="_blank">📅 12:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673722">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
توقف کامل پروازها در تمامی فرودگاه‌های اردن در پی حمله موشکی ایران به منافع آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/673722" target="_blank">📅 12:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFPcisstGwJQZ-mOxpPcBMEZBriJSaDqHc0nvqH1jDOtsQVd4YS1XlipDhEb95pk4MYwnQAxoG0kTneTaun0tbwdfDAp0z91f6e7cr6qxWr4ZzUwosoecLCWW83CcO1vN8WYPFn-8R20iGC05rPKskZ62uqWNpqgzYwlyozl1oi_yCwSfaQ1BzzjuUuqFX4Jzv6mP763zXg_9EF_ETEs2RJucrNmM4SsWB7lYN1to0KrITxaIvDWTCLIl1VMRI8IwGQpP5Ffv7WU7P7kQ3iGeGkfIV7psWy3LQZgR7WNRBob9JlYrJr42W4gfoPPepZfFvmoykreTLoxL3sXTXznFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجارها اردن را لرزاند
🔹
همزمان با گزارش وقوع چند انفجار، آژیرهای هشدار در مناطق مختلف اردن به صدا درآمده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/673721" target="_blank">📅 12:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673720">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAZKrLhy-2xv3Alelii5ywu-0Ze7JrzgQJOZhialVO2XGvebNHEhC8KS5f4NEgNTwxyYBJ5uYWtqzjCz-oNttgtc8Kjzho76Rb7sWiLv9O4KQGvlQCWfjNzPZS9dM42L9whTN3K07Px9MkrUzOTu3MZV78Bg3ooxTND94eG5QnL8m9e6hOTPzz8cCv7ERq9d0TBKe6NV5BAkXm0xids8TCYx-zdvFLywfS75jnzumKe4TPN7Zh4fdtxq6YxFwOUXpaDSmfZjZdDKjj-vJ2idC1fXICeVrAPlAaNH669nZQ-8-My09epIPDRtdi5b1fiR2eb0AOKQ2jjbhQJ5SIMIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۷۴ هزار واحدی شاخص بورس
🔹
شاخص کل بورس با رشد ۷۴ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۸۸۷ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/673720" target="_blank">📅 12:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkaV4kLLOMaPt3BBYccHZL0eEJzv-PAMPfkRFhFlkJ8XTjZrRul4J6dp7jkNqRq5VTslaZadhCUH0zkcLfbLEQG95J8BAZSpEYUE_FyWufdgo1Lyz2vSpycn7H9eE-R4bUIxLKkEYFtvT0V3JDmwnh882KMJfG_fFoc9fr-ShnC0dS1-DrFAvYenUO0R0Sex1s0ySKBQiMkEPMQamumZbHh7p3CuYw_2HBipM1oPHSe4a-zNQf-C9s6wb5SmPkzldfz8v3w95GNiJnc1rLJDQvTVXYgkOoi0qIt7BXrrdoUbTBNLCNC2DDWlTfBqr6Lg_PA--z3ddXkqpnENXMjCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیدبندی فصل بعد لیگ نخبگان آسیا با حضور استقلال در سید یک و تراکتور در سید سه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/673719" target="_blank">📅 12:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
شبکه العربیة:
دیدار عاصم منیر با وزیر کشور ایران
🔹
فیلدمارشال عاصم منیر فرمانده ارتش پاکستان در حال حاضر با وزیر کشور ایران در اسلام آباد دیدار می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/673718" target="_blank">📅 12:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673717">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایران را از هم نگیریم ...
🔹
در روزهایی که آتش جنگ بر سر این سرزمین سایه انداخته و قدرت‌های بزرگ از سر منافع و هراس خود در برابر حملات آمریکا سکوت یا همراهی کرده‌اند، دردناک‌تر از هر تهدید خارجی، زخمی است که خودمان بر پیکر یکدیگر می‌زنیم.
🔹
برای چند اختلاف سیاسی، برای چند عقیده متفاوت، برای چند جمله در فضای مجازی، آن‌چنان به جان هم افتاده‌ایم که انگار فراموش کرده‌ایم همه ما روی یک خاک و با یک نام زندگی می‌کنیم؛ ایران.
🔹
دشمن اگر بتواند ساختمان پل و یا برجی را ویران کند، شاید بتوان آن را دوباره ساخت. اما اگر بتواند دل‌های یک ملت را از هم جدا کند، بازسازی آن سال‌ها زمان می‌برد.
🔹
حقیقت این است که هیچ موشکی به اندازه نفرت، یک کشور را ویران نمی‌کند و هیچ تحریمی به اندازه تفرقه، آینده یک ملت را به گروگان نمی‌گیرد. این جنگ بالاخره تمام می‌شود. دودها کنار می‌روند. اما آن روز، نه آمریکا کنار ما خواهد بود، نه هیچ قدرت دیگری.
🔹
آن روز، این من و تو هستیم که باید دوباره در همین خیابان‌ها کنار هم قدم بزنیم، همین شهرها را بسازیم، دست فرزندانمان را بگیریم و به آن‌ها یاد بدهیم وطن یعنی خانه‌ای که همه در آن سهم داریم.
🔹
ایران فقط خاک نیست؛ صدای لالایی مادری است که فرزندش را در آغوش گرفته، دستان پینه‌بسته پدری است که برای فردای خانواده‌اش جنگیده، خاطرات کودکی ماست، مزار عزیزانی است که دیگر میانمان نیستند و رؤیای کودکانی است که هنوز آینده را ندیده‌اند.
🔹
نگذاریم هیچ‌کس، هیچ قدرتی و هیچ اختلافی، ما را از هم بگیرد. ما شاید در سیاست هم‌نظر نباشیم، اما در عشق به این خاک نباید رقیب هم باشیم. باور کنید هیچ اختلافی، آن‌قدر بزرگ نیست که ایران را کوچک کند و هیچ پیروزی سیاسی، ارزش شکست یک ملت را ندارد.
🔹
اگر این خانه فرو بریزد، آوارش بر سر همه ما خواهد نشست. ایران، امروز بیش از همیشه، به قلب‌هایی نیاز دارد که برای هم بتپند، نه علیه هم.
#سرمقاله
#همه_باهم_برای_ایران
@TV_Fori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/673717" target="_blank">📅 12:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673716">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
جان‌باختن کودک سه‌ساله بر اثر حمله سگ‌های بلاصاحب در سنندج
🔹
جان‌باختن دلخراش یک کودک سه‌ساله بر اثر حمله سگ‌های بلاصاحب در سنندج، بار دیگر مطالبه دیرینه شهروندان برای ساماندهی این را به صدر مطالبات عمومی بازگردانده است.
🔹
این حادثه در حالی رخ داده که هفته گذشته نیز یک دختر ۱۲ ساله در شهرک سعدی سنندج هدف حمله سگ‌های بلاصاحب قرار گرفت و مجروح شد./ ایسنا
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/673716" target="_blank">📅 12:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673712">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyRY17fwsUVjgsUC052HdLtAbrWtXc-3HRTIFF8ZobcDR4hYIEKZbqOUhzsVJhZLm1qYhvA8zih33l2S_twa2I_sK2ELln9jNUmeMVWPRPiAgqUnwInu2KsnqObh-bjX0zUsetYSo9vug9lYcnOt3wZW0PwHmNncLN31Pne4SHWy06v4GWvPyCan9cteP58tmT8p9DCyiGabVNyokgQ-Wbfrc2FrvmVS9U8uu1RgRzu7k4P3M0_Nph22yj78cvroUUQ-anSmMzIwiBa-Q8P3sni77kz4ttrMOhOFrRr5Vg-8CBn02AI3dE8iRj04k3noNtph_4RGBw1PbPrrESCFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZ4jv_y02QILyCE164pvdnCXNT8Cx9Bu8ZEYwcbrdmfMEHtlEcQoNV7247-kqIxOm6x8fmaOOifb6Yamce1yU-vQetMCKQ4CRbGgw8YVAtjG_CyplnK4LA9DNe8Qksp6gKsK1toFQJ8uP-Gkv0_rY458QgVkXQczLYtl2gEgzVoxhA75lQrl0FioZqvOBNA5EYIrB8AZ4GhnPYGnwoUDf5vIvIfeb26blAlKYqtPCMds6pmrEr2cgbOV-uWZEUmzht7w5uEjyMuN-c3QKtTKvFaBDDtXLOjAUqHhcGRZnzE9FX-2BAsAjpqmCTj6M15iRTkEUdO8BNgoyo1gYNmoDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rf1wOYi088SvjDk_2Us-WEQM_kI4ZWBjlfIjmER7zPNubgdih9zE4VENjDsOPou8ovkfs2MVhIhCd-6NJnZcKY1OXLOxtALnIG-talpXlgDw7ihMQvu_-Hqu-v76yW5o5fCZ3Vk1rYMh5ca1QJ_CAzd6aUyEEr-qVZjoLVPgRWO2ZjR4eLsPdp0iKnJ9gkozayi8E3y5V2ZnkixfKH9I2fEwmc8jglcrLZqqPE3ejSXWkXhJhqaMGEGXYH2gQT5gXMTFnKlqmv47jYVCWXXvk7xPV2w-W-oxOxBzzEggssGiWxy3nTNz60Uue_e6krBymt4SHzUSRZKgdfW4cFcgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDRuvsVfgAdRZRd4U_FlbDdZ7AG8E6ULX6Ytjla4SnHHRvtHxwrNk8gIacjuEDIbRIMcymhZtkrvAZIRNZMUXtr2FzxrFUp43MSBM2KT7sScVhfVJ9pU13M-rG6uWcjr_Zfo1kFis6S4rvmQtMcGu5hxRWKM_TgE6ZascnRMtg5cghsseqzdsRwZ2uCSRH67jR6OZInvKCArV9dxxaKmZV8iwzdsNG0WceG2CUuyDNPokUnoWXiIkJ7hPcoocOjFB77UUAzl2463K4xsJ0j1MZKkgtxhJwRgaFvxjbGOXHZnuYJWsgMobSqBSGZb-SFGCPi3ft_hScyZYUPKTMyE1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا آدم‌هایی که بیشترین مهربونی رو دارن، بیشترین ضربه رو می‌خورن؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/673712" target="_blank">📅 12:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673711">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfe2305ba.mp4?token=OseXxBrqTgaEdbw2ECiqe78HyYSfnx4n0JuKxYqNaJAmg6nzg9W-Dqi2ezMe0ZDARDMP4dou9oHsA4MvH5Um6aH5P1D1lbAXZHDkboio1aOICOAPQBgFT5pXCw9V5qhWo4iIWhi0Z71BCeC6KDVQOKSegVzu4FPQavL7M6gTXlyyQ8IbbwdXf4gfWp_AjitXlUbKAGHPuBl8O5Vn-bFhanLUbarF1PgfRoSgak85kXHecYeh5hGe0en2pT9eq8H-N8hriWoE39FhayPMcRVh09yB-TiGDNG10KtDKLp2Kogx405rOVSwXMkH9JnUbo4yQq-zND_B60TToqg2obtctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfe2305ba.mp4?token=OseXxBrqTgaEdbw2ECiqe78HyYSfnx4n0JuKxYqNaJAmg6nzg9W-Dqi2ezMe0ZDARDMP4dou9oHsA4MvH5Um6aH5P1D1lbAXZHDkboio1aOICOAPQBgFT5pXCw9V5qhWo4iIWhi0Z71BCeC6KDVQOKSegVzu4FPQavL7M6gTXlyyQ8IbbwdXf4gfWp_AjitXlUbKAGHPuBl8O5Vn-bFhanLUbarF1PgfRoSgak85kXHecYeh5hGe0en2pT9eq8H-N8hriWoE39FhayPMcRVh09yB-TiGDNG10KtDKLp2Kogx405rOVSwXMkH9JnUbo4yQq-zND_B60TToqg2obtctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔋
این روزها که قطعی برق بیشتر شده، داشتن یه پاوربانک از واجباته!
با پاوربانک K62 ظرفیت 10000 میلی‌آمپر خیالت از شارژ وسایل ضروری راحت باشه. از گوشی موبایل گرفته تا چراغ‌های USB، چراغ کمپینگ، هندزفری، ساعت هوشمند و سایر گجت‌های شارژی.
✨
ویژگی‌ها:
✅
ظرفیت 10000mAh
✅
دارای 3 پورت USB (دو خروجی 2 آمپر و یک خروجی 1 آمپر)
✅
مجهز به نمایشگر LED برای نمایش میزان شارژ
✅
دارای چراغ LED؛ کاربردی برای زمان قطعی برق و مواقع اضطراری
✅
سبک و قابل حمل، مناسب خانه، محل کار و سفر
💥
تخفیف ویژه
قیمت قبل: ۱,۹۹۸,۰۰۰ تومان
🔥
قیمت امروز: ۱,۳۹۸,۰۰۰ تومان
⚠️
ارسال رنگ و برند (سامسونگ یا لنوو) به‌صورت رندوم انجام می‌شود.
🛒
همین حالا سفارش بده و نذار خاموشی، ارتباطت با دنیای اطرافت رو قطع کنه.
خرید از سایت
👇
https://memarket24.ir/product/brief/34644/180124/</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/673711" target="_blank">📅 12:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673710">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
انفجارها اردن را لرزاند
🔹
همزمان با گزارش وقوع چند انفجار، آژیرهای هشدار در مناطق مختلف اردن به صدا درآمده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/673710" target="_blank">📅 12:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673709">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
هدف قرار گرفتن ۱۰۰ شناور مردمی در حملات اخیر آمریکا به بندر جاسک
فرماندار جاسک:
🔹
به واسطه اصابتی که در روزهای ابتدای حمله به جاسک انجام شد، ۱۰۰ فروند شناور
متعلق به مردم
و بخش خصوصی که هیچ فعالیت نظامی نداشتند مورد اصابت قرار گرفتند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/673709" target="_blank">📅 12:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673708">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvMUK-1iZPQVzAyg6IF-EAN21SDz9QrZqchkj73wtecLig446yLBb6HF8hOxlajgRJdWJSJSKIm3-gLrM1fGYk1M-hQL1_BnnTzxdYwe9JxgvrdaoidooJIeGfEF9k-82KPZO9eUxyT3evrFNWIcYk32YOiFp1PNVhm2LmHbq9i3sHCL_RrV2W1IuQIew6ktYNyjXxqRb4pOzqj85G4MjpsURkdzCG-IpvtNyEHZ_NuKQqB_TcK-_CX3OSODCfXZzfOtKKKsVI-N9DVg8fNlCafzhuBxQ_YHt4P4xmWb6kVHNxA8_s6vLXtfWqPeitX7jfn5E6B3YZPR5R3GqEX9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه داور ایرانی در لیگ قهرمانان بانوان آسیا قضاوت می‌کنند
🔹
کنفدراسیون فوتبال آسیا، مهناز ذکایی را به‌عنوان داور و ریحانه شیرازی و آتنا لشنی را به‌عنوان کمک‌داور برای قضاوت در مسابقات گروه F لیگ قهرمانان بانوان آسیا ۲۰۲۷-۲۰۲۶ انتخاب کرد.
🔹
این رقابت‌ها از ۲۶ مرداد تا اول شهریور برگزار خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/673708" target="_blank">📅 12:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673707">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNbhHOsTgfvEttEGv32kv5iWDwi1LPQzUOoctx53Z9TGlAmnrCPpmBowIDgIHLgMup2lwR67Gh7IF_GANO8oOnx52ZhV98rUES9iPnoaqsbBFHYnt7HBDszjDQLtMEdQmEKS29qMisI5NNHd9HTL4lu76cdUXEwO9RiPIGhaayOr1kJMuXvcaQ-3a8DRiM1VzsL96M8rnlzuZwqPKOUUcmCXWZ3qTihHpEAUiAs1rPd8V3kwfppFu1m2XCb5tVgsQFJw1-3c3VMHLIX5o1GNv3oI-GY3nH9ynWAIcFK25rskBOkOuHOYMxv1LZMf51_f0mW3kZUYA4j9e1cFxwo_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوشته روی موشک‌های ایران: مرگ آرام در رختخواب و خواب راحت بر دشمن مردم ایران حرام است؛ تمام!!!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/673707" target="_blank">📅 11:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673705">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCBFT6k2VepWOXfRTX1kNDTWjTMEntIV4cSm70ftAni6G530Ixm9qsRa5Fh3yySG6m0vyp0FrZvxLhsedcvPvO5Pfo0kd1nm47wi_zpqM3I2hwGmcxGd6VSbBd3YqzyjyoWlfuOEK8WrL0ZgFVxlHI1uhis5PUkTMXRj_BrODyTKBnBFiGz3LkhADfz3h9zE8Okn5BhY-hOOy7dUjQf67hs42lQG3kU_lOGQfFCNaFHg7LAKdc-MkcZPhU6ScX87jlbqpjoafqhy-gg_ocNxtv_1CUcCPT9qpCaynB-9g7ycZmJ_CgrGw5SouNnV8xoUaQl8HM4DL7ITK9PBJ1XphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر اساس نظرسنجی منتشر شده توسط فاکس‌نیوز؛ ۶۹% مردم آمریکا از عملکرد ترامپ در موضوع جنگ با ایران رضایت ندارند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/673705" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673701">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تنگه هرمز بازار آلومینیوم را منفجر کرد
🔹
جنگ ایران و اختلال در تردد کشتی‌ها از تنگه هرمز، یکی از بزرگ‌ترین شوک‌های عرضه در بازار جهانی آلومینیوم را رقم زد. شوکی که حدود ۱۰ درصد از عرضه جهانی این فلز را تحت تأثیر قرار داد و قیمت‌ها را تا مرز ۴ هزار دلار به ازای هر تن رساند.
🔹
جی‌پی مورگان اعلام کرده هرچه بازگشایی تنگه هرمز طولانی‌تر شود، کمبود عرضه در سال ۲۰۲۶ عمیق‌تر خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/673701" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
نمونه اولیه «گواهینامه موتورسواری زنان» چاپ شد
معاون امور زنان و خانواده رئیس‌جمهور:
🔹
به هیچ عنوان موضوع موتورسواری زنان، حرام ذاتی نیست.
🔹
نمونه اولیه گواهینامه موتورسواری زنان چاپ شده است./ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/673698" target="_blank">📅 11:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJ1oYF-9cxmiG-E-WyBkwwabH7ri9iki7XXsDdTo_Zd4X2WvSTd8TRdj_RuPtRCh-dom5ilgPGm9u6fmohoETaAzCEGfFNO25vX3QH4TkIqegPYP47dNvT1jS95nq6Wv9hSn1j8K71vsr_26HaPVIY25eiFJ5S_ondKkQ-H2dGQVPqGJH_6ehk3QQTpHI2q9I0SHXMEQhXOOAvTYDkjl7sskTKdGDHenyimbEGt44MxzU4xUEHsrHP-6YvOYcn7-XqC_zjGBUIOiscDXpDwzSfg7Nmu6LMFtNhwDqEt-NROtXrpRISUZx-xbUbzB7YFMHrUPZWU0pboFDU0AHKn3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک جسد در خانه نماینده کنگره آمریکا پیدا شد |‌ ماجرا چیست؟‌
🔹
پلیس بوستون تحقیقات خود را درباره پیدا شدن جسد یک فرد در خانه‌ای متعلق به کانن هریس، همسر آیانا پرسلی، نماینده دموکرات مجلس نمایندگان آمریکا، آغاز کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3232013</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/673697" target="_blank">📅 11:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3s_Uu-gN9TACF5YlCJ64mcLK0Ulq8krvCEftbnGchhCUBamdFhAij-kn9srMgB2BqE1XH2bRJYQ0fUlvs7P-pxrpArtOlIPmXJqii1znTgphIjawjP3jhriS0OqkYMMRShYq3LeGXP1wMBvCvj53lnDPwoBKhliEvitXhClEPG-jTS_H1ZpT3S7_QwiBW_q19BR_wKbcvA8UyrC0B_T697jZkm-r4x6INezg7Eb9Q5Q4Zoh4n9FlZPbZasuHw5CR5hXrmZREA59rLmB8Qt_dh6dkKjOiIv32r5T_REpkBgx6JcsBtm4bcVR89AI5SM2-Bw7JZ7v2M_4pLDBzcmVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار برای اولین بار| تصویری از رهبر معظم انقلاب حضرت آیت الله سید مجتبی خامنه‌ای که مربوط به قبل از جنگ است
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/673696" target="_blank">📅 11:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0eba85d.mp4?token=FyLOV1d4VGvsi5sCaTKXGi4mhJxNV88X4xhQoLFS94N4v2OyP5oASd87_tpcXX2flFlGJxksHp6726EhS6aANHgd-Q8wkVxqdWsO10nANW3UYMZsEPcSNpkIdZJuWAywRtaAxdYmSknDZ42ZV5t7qoEPAH1OzWuMIY7WFm4JctvNHLcTVCcsTbsbR4q0dQg4Yeo90DtLJ-xRqPnkkYiWd7cjj1rz9wkUDfQhj4MnVKH_uxSFO_ULUkI0jcg7W96ScN5y08H2QTGSYG2VJAVgup2jVCgUleONAuC11th0kK8dWrA-3V2JnPlCPjt7F8FzExSV_PkUgFn6KZEFfAVhOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0eba85d.mp4?token=FyLOV1d4VGvsi5sCaTKXGi4mhJxNV88X4xhQoLFS94N4v2OyP5oASd87_tpcXX2flFlGJxksHp6726EhS6aANHgd-Q8wkVxqdWsO10nANW3UYMZsEPcSNpkIdZJuWAywRtaAxdYmSknDZ42ZV5t7qoEPAH1OzWuMIY7WFm4JctvNHLcTVCcsTbsbR4q0dQg4Yeo90DtLJ-xRqPnkkYiWd7cjj1rz9wkUDfQhj4MnVKH_uxSFO_ULUkI0jcg7W96ScN5y08H2QTGSYG2VJAVgup2jVCgUleONAuC11th0kK8dWrA-3V2JnPlCPjt7F8FzExSV_PkUgFn6KZEFfAVhOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معبد کارنی ماتا در دشنوک (راجستان، هند) یکی از شگفت‌ انگیزترین مکان‌های مقدس جهان است
🔹
این معبد محل زندگی بیش از ۲۵ هزار موش است که به باور مردم، تجسم دوباره (تناسخ) پیروان الهه کارنی ماتا هستند.
🔹
زائران و عبادت‌کنندگان با پای برهنه در میان آن‌ها قدم می‌زنند؛ این کار نمادی از احترام و طلب برکت است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/673695" target="_blank">📅 11:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673692">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef36935c70.mp4?token=TTHm25EP4vxziRFGGL2vBPKvDoMIo8D935I87TjlHD8YvfiaxxCfKFcRAyBN1vNjqmJmNbdzxvLNYoOxsgzKuSRdi0aK00maHykz5_9UzsW7Ku_JQeLljpRlLLugIp31DBJ8QeGAJ1UOZ9MwV1sLeXRQpdJEi5h9HgpRgIQ2a7EUqKkcQ82XFz24eJ8UYTZMEyOLFpimF_6xxq6imxdTxj5ekwJ4dXVvRdwtdaoV69Fou2YP68E8xuFeBaNgLSCO8RjZ3fG4Vaq7JItwqj_J4ieSDjigkYEUewWPcnnGZTb29hAhf2J2LCV40LVeVhQv64M7ZAqLMZf_76PsIkJFibaxw9E1BOK_LSEq2qudFZHYvrdrqd1sGpG2DxEiAXgtcGjlIUyBrHYvvTVY0G61DIFA-VspjqJECf1CxPIi_Nqal2dp1JVeuKhZZBdM2O7uEJpzFAasDcbJB2AZ3JOBd1BsHvI5NG3Zp8yyCE0k9B6fGq22d1Yo4mIzuf_KcfHNT7jh60BdU6h07DXf7k_yc7WKz5YeqAVVFgjlPmWTLFiTXmHe19Dp8rBrYGZRFcYd97kvZC3iYUDZMXtIHNXul522JCnU5nAYOxjpmUWHmvjVXJ5XxxVSoc7LT6MQtU07WgnoQo7FfVMgw1bQHyLZQWPA5_JaqCRjn5JK8f0iswM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef36935c70.mp4?token=TTHm25EP4vxziRFGGL2vBPKvDoMIo8D935I87TjlHD8YvfiaxxCfKFcRAyBN1vNjqmJmNbdzxvLNYoOxsgzKuSRdi0aK00maHykz5_9UzsW7Ku_JQeLljpRlLLugIp31DBJ8QeGAJ1UOZ9MwV1sLeXRQpdJEi5h9HgpRgIQ2a7EUqKkcQ82XFz24eJ8UYTZMEyOLFpimF_6xxq6imxdTxj5ekwJ4dXVvRdwtdaoV69Fou2YP68E8xuFeBaNgLSCO8RjZ3fG4Vaq7JItwqj_J4ieSDjigkYEUewWPcnnGZTb29hAhf2J2LCV40LVeVhQv64M7ZAqLMZf_76PsIkJFibaxw9E1BOK_LSEq2qudFZHYvrdrqd1sGpG2DxEiAXgtcGjlIUyBrHYvvTVY0G61DIFA-VspjqJECf1CxPIi_Nqal2dp1JVeuKhZZBdM2O7uEJpzFAasDcbJB2AZ3JOBd1BsHvI5NG3Zp8yyCE0k9B6fGq22d1Yo4mIzuf_KcfHNT7jh60BdU6h07DXf7k_yc7WKz5YeqAVVFgjlPmWTLFiTXmHe19Dp8rBrYGZRFcYd97kvZC3iYUDZMXtIHNXul522JCnU5nAYOxjpmUWHmvjVXJ5XxxVSoc7LT6MQtU07WgnoQo7FfVMgw1bQHyLZQWPA5_JaqCRjn5JK8f0iswM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای یک تصمیم ناگوار برای ایران
🔹
گاهی بزرگ‌ترین تصمیم‌ها، فقط یک ساعت اختلاف دارن! داستان حذف تغییر ساعت، اون چیزی نیست که فکر می‌کنید.
🔹
پشت این تصمیم، پای هزار مگاوات برق، صدها میلیون دلار صرفه‌جویی و مطالعات چندین نهاد تخصصی در میونه. ماجرای حذف تغییر ساعت را از زاویه‌ای ببین که کمتر درباره‌اش صحبت شده.
@TV_Fori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/673692" target="_blank">📅 11:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673689">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb5d21c.mp4?token=btMAG-BBluBwpXocCtgN2QzUkU55vPbkU3XERn7Iqb8V8PQ4_zuoLjIDgbBL9U7Troa622GfpvF2ulFm91kT2t-hiOdwJioDYM4tJRTZiUAJDFs_nWiAxQ8TsU80V7auyLnu3t7qJwGsddSuANuvVIidQdULc7nw_1lDiPEB7hhLTMzfGU3afW5Qszo_9mHgdFc76cxzyPRAadEbm_zo_uGOqxd7Q6919baYuM0xnkW7Yl_F3OwYsjngMKudzLAbZ6l9lWg-6wU3dsafCUEyMnuT2_2J95kVhOuV5bUodp52rDq7jGS7YevrT_vE4SjquSeaD664prNIr6adx0hg-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb5d21c.mp4?token=btMAG-BBluBwpXocCtgN2QzUkU55vPbkU3XERn7Iqb8V8PQ4_zuoLjIDgbBL9U7Troa622GfpvF2ulFm91kT2t-hiOdwJioDYM4tJRTZiUAJDFs_nWiAxQ8TsU80V7auyLnu3t7qJwGsddSuANuvVIidQdULc7nw_1lDiPEB7hhLTMzfGU3afW5Qszo_9mHgdFc76cxzyPRAadEbm_zo_uGOqxd7Q6919baYuM0xnkW7Yl_F3OwYsjngMKudzLAbZ6l9lWg-6wU3dsafCUEyMnuT2_2J95kVhOuV5bUodp52rDq7jGS7YevrT_vE4SjquSeaD664prNIr6adx0hg-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتحاد مردم در پویش «قرار همدلی» برای پایداری برق نتیجه داد
اکبر حسن‌بکلو، معاون هماهنگی توزیع توانیر، اعلام کرد:
🔹
مردم به پویش «قرار همدلی» پیوستند و با کاهش مصرف، بیش از هزار مگاوات کاهش مصرف برق را در روزهای گذشته شاهد بودیم. این کاهش موجب رفع محدودیت تأمین برق در استان‌های جنوبی شد.
🔹
ادامه همراهی مردم می‌تواند به تأمین برق پایدار برای استان‌های جنوبی کمک کند.
#مدیریت_مصرف
#پویش_۲۵درجه_قرار_همدلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/673689" target="_blank">📅 10:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673688">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
مرگ ۵ نفر بر اثر تب کریمه کنگو در کشور/ بیشترین موارد ابتلا در فصل گرم
وزارت بهداشت:
🔹
بیماری تب خونریزی‌دهنده کریمه کنگو از طریق کنه «هیالوما» که در مراتع به وفور وجود دارد یا تماس با خون دام آلوده منتقل می‌شود.
🔹
به هموطنان توصیه می‌شود از ذبح غیر بهداشتی پرهیز و خرید دام و گوشت را فقط از مراکز مجاز و تحت نظارت دامپزشکی انجام دهند.
🔹
همچنین گوشت تازه حداقل ۲۴ ساعت و احشاء (مانند جگر) ۴۸ ساعت در یخچال قبل از مصرف نگهداری شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/673688" target="_blank">📅 10:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673687">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6YfC36mRjICJQFwM28UOyFdot6yFgrxEubT2q0QQyNfhP4_u6VV3Irh85UVXExprxkfsGjbgSK5hkcu-KotyXzFFo3p2LajPiTksVMtQ4ReTR1BoU5gcwlL-h5dGSWIlTmQBidjAH8WnSBU4rdDyULpTW9sc4DSIYLaSWGlgoJ-wg4Oe2-FQFJu4RuuopZD4RZpz6Znzrwklug3F91yAwRrd13wwbl6YbnVrUsXkz2T2392vjLhB1zw2mROS8YAAdWYXK6gLv3wtB6eQRQBToJXwxyqenWkWiPPUuyFbLYAu5I2oy971Q8MjqMRlkwkDRe5gKP1oqfP631bQa_6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برندهایی که لباس ۴۸ تیم حاضر در جام جهانی ۲۰۲۶ را تامین کردند
🔹
آدیداس(۱۴ تیم) مانند آرژانتین، آلمان، اسپانیا، ژاپن، مکزیک، نایکی(۱۲ تیم) مانند برزیل، انگلیس، فرانسه، هلند، آمریکا، کانادا و پوما(۱۱ تیم) مانند پرتغال، مراکش، سنگال، سوئیس، اروگوئه
🔹
۱۱ تیم باقی‌مانده از ۱۰ برند دیگر استفاده می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/673687" target="_blank">📅 10:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673686">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30cb476e8d.mp4?token=pcWDfDBS5wzfoBng25BPAN6cfk6G8dnypkqf5vPLzZYNMgt_HvtjNcEF6YKJR7eXgHEGYlt9krm6zN_oDmE-F8z2V7yoXeCaRUha3MGzrQnLZSbOw-ngRQDpHz0y6BO84T2JRWvzArEJheEliuoCxg5fiMMQB9kpOL2j4sO6QdA3423tzSsM7By_47ELWYy39TqjNuzFPgCq3hmVXj3GsU9NuU6ONHwc8Mo-jF9N93P2RcojZWL14FMu_DMGbcXDxv6EEtcxeHG3V8OkD3jNI7TeJsIiolxm9i4Hyk-d1EbR3YwNkK6U5P8YPrayzvlzv56QUYdnMFd5k05JC_cm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30cb476e8d.mp4?token=pcWDfDBS5wzfoBng25BPAN6cfk6G8dnypkqf5vPLzZYNMgt_HvtjNcEF6YKJR7eXgHEGYlt9krm6zN_oDmE-F8z2V7yoXeCaRUha3MGzrQnLZSbOw-ngRQDpHz0y6BO84T2JRWvzArEJheEliuoCxg5fiMMQB9kpOL2j4sO6QdA3423tzSsM7By_47ELWYy39TqjNuzFPgCq3hmVXj3GsU9NuU6ONHwc8Mo-jF9N93P2RcojZWL14FMu_DMGbcXDxv6EEtcxeHG3V8OkD3jNI7TeJsIiolxm9i4Hyk-d1EbR3YwNkK6U5P8YPrayzvlzv56QUYdnMFd5k05JC_cm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تیم ملی اسپانیا روی پهپادی که به سمت مواضع دشمن پرتاب شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/673686" target="_blank">📅 10:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673684">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای آکسیوس: میانجی‌ها پیشنهاد آتش‌بس را به ایران و آمریکا ارائه کردند
🔹
پایگاه خبری آکسیوس به نقل از منابع آگاه ادعا کرد که قطر، مصر، پاکستان و چند میانجی منطقه‌ای دیگر، پیشنهادی برای آتش‌بس ۱۰ روزه را به ایران و ایالات متحده ارائه کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/673684" target="_blank">📅 10:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673683">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
مرحله بیستم عملیات صاعقه ارتش؛ ادامه حملات پهپادی ارتش به پایگاه های آمریکا در منطقه
ارتش:
🔹
از بامداد امروز و در مرحله بیستم عملیات صاعقه، پهپادهای انهدامی آرش در چند مرحله محل اسکان و استقرار نیروهای ارتش تروریستی آمریکا در پایگاه شیخ عیسی بحرین را آماج حملات خود قرار دادند.
🔹
پایگاه شیخ عیسی از کلیدی ترین تاسیسات ناوگان پنجم نیروی دریایی آمریکا و مرکز عملیات ارتش متجاوز این کشور است که عملیات هوایی و کنترل پهپادها از این پایگاه هدایت می شوند.
🔹
ارتش جمهوری اسلامی ایران تاکید کرد، عملیات های تهاجمی  تا بازداشتن دشمن از  ادامه تجاوز به کشور با قدرت ادامه خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/673683" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673681">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngTJItB8ND-1ybbU3IZ40_fBgSEj2QdfYRPRPBcQF6T0ClTTGI0D5DlrovzBLo8E9ssVNibmgfH7O6JZR7uRowG-ujSUeaOMKQFu10OmN7boD8gHFyI2CAocQx8oQoxFEw_-bVCZJW7rxmDyKn5CaIByMvQiF_q9ziMrCJShTn-i8jQPqaATf_hA5_BgZK805l2qsmFRG_7LFRWe4MnQIpd4ziwQjfqY5xyMNB7iedsvsGxtHPymG5GnmnGgOWeP8ui3T4dCFNx-wwO_N5urgMgojKoPxLGjkluL9qzMYDZi2lVJtLvNNjaPVoT43a7dRhIeZ0QFbf16XntlLBgQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی آژانس‌های اطلاعاتی آمریکا از نبرد تهران و واشنگتن
واشنگتن‌پست:
🔹
آژانس‌های اطلاعاتی آمریکا یک بن‌بست طولانی بین تهران و واشنگتن را پیش‌بینی می‌کنند و معتقدند که بعید است دولت ایران تحت تأثیر قابل‌توجه دور جدید حملات نظامی آمریکا قرار گیرد یا موضع خود در مذاکرات را نرم کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/673681" target="_blank">📅 10:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673679">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای اسرائیل درباره انتقال هزاران سانتریفیوژ ایران به اعماق کوه کلنگ
وال‌استریت ژورنال:
🔹
ایران هزاران سانتریفیوژ غنی‌سازی را به اعماق کوه «کلنگ» منتقل کرده؛ اقدامی که هدف قرار دادن آن‌ها را حتی با پیشرفته‌ترین بمب‌های سنگرشکن آمریکا نیز بسیار دشوار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/673679" target="_blank">📅 10:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673678">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NifxisOj3JsBE0NXVtVAHB5TV1yOjNea3-Mid5kwVwk3apde2SxmU4yxuxXo9pG0I8b-wyZK1KD8sRlOWQc-I1p1X6fPxdUzXszNug1URr_xBpVdq61ObN7oNdVcJOq4yvIn1UjeD6FfROyj2iVSwtU8xWh_Q_YkkAqBLmXKxXPRLQCoHIfIqGOk_D4iYVAnzMAyerudsHYGvgx2j9intT4QH--TOqaWh_OhT6SaDp01jBgRYGcgDyvkN5sD2HFOYDu1xlE0wf_frBEsoqBw3zTW0_nNp9JkDvjz4_rXSxYd-zKnlcfEMZHNhexVvCKi-Q7fTyqjfwnB84BLSzaWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه پاسداران: به تجاوز دشمن پاسخی فراموش نشدنی می‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/673678" target="_blank">📅 10:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673677">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35e1dd9ca.mp4?token=ZeelFJRzT3TL1zqUM4df0xQMpqfL1JxgKbtKLHKzwIpGeW37R72A0ovH8_HlBt9aMFx2N84S_hhhxY4FpvwkE9Qe9KPjcmIS8mWjus0lh_ztPoI5RDi8HNTdhHUGVAmtdRsHGijhcIXeNzqd2a9kGkbo7lj6KUDbdYVnam4G-gIDDrYg2pWjwe4GZ39fsY9XqjGle2c3R6xpMa1CtCyIy0oL_Obb9GJo1dafQhtPH5VZtzNvDvoNL9MCP-9py9xW_7tZDytVsyBVZ-JwcV3-CCiMx1r3NZzIxcTjPAXY6L3AU76WJXLj83x0d9mO841PDB-cF6Pn5gtQEVOonUkIrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35e1dd9ca.mp4?token=ZeelFJRzT3TL1zqUM4df0xQMpqfL1JxgKbtKLHKzwIpGeW37R72A0ovH8_HlBt9aMFx2N84S_hhhxY4FpvwkE9Qe9KPjcmIS8mWjus0lh_ztPoI5RDi8HNTdhHUGVAmtdRsHGijhcIXeNzqd2a9kGkbo7lj6KUDbdYVnam4G-gIDDrYg2pWjwe4GZ39fsY9XqjGle2c3R6xpMa1CtCyIy0oL_Obb9GJo1dafQhtPH5VZtzNvDvoNL9MCP-9py9xW_7tZDytVsyBVZ-JwcV3-CCiMx1r3NZzIxcTjPAXY6L3AU76WJXLj83x0d9mO841PDB-cF6Pn5gtQEVOonUkIrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدون کثیف‌کردن حتی یک ظرف، خیلی فوری سیب‌زمینی متری و ترد درست کن
🍟
مواد لازم:
🔹
سیب‌زمینی
🔹
نمک،فلفل‌سیاه
🔹
پودر کره
🔹
پولبیبر
🔹
آویشن
🔹
به‌ازای هر سیب‌زمینی یه قاشق نشاسته‌ذرت #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/673677" target="_blank">📅 10:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673676">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین | فصل‌دو،قسمت‌نهم</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/akhbarefori/673676" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
♦️
حسین بن منصور حلاج
🗓
در این قسمت، بزرگترین کلاس درس تاریخ را برای «شجاعتِ متمایز بودن در اقیانوس شباهت‌ها» و پرداختِ «هزینه‌ی سنگینِ وفاداری به خود در سیستم‌های سنتی» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/673676" target="_blank">📅 10:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673675">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f4d14622.mp4?token=E9Jn6t5pwvY-JoHzdnEI_2g0K0AkYwraPUb-DLTs31E7CYWH-iHtGtHsj5f1lH5vIFQg8iwlPM5TAkGiF9ra2zlJG5HZf9-PWbh7FFFNb8ZYP1Vb09aULhIev1ZzGwiwsHaZ-647jvqiNRfOkDYghXl5spG3p-hWa1XBCGL3CjHwTo7d8A9Pfk8hBJ6spZDxxxtR6b7jgTu-EvuVHfyvok03byChKp_VDgBRQXRU1YQ1DvD7yyxLK9Q1Uq9z4apxJCDM6JclelkeNvFgFd53e52TD0UjbVO1ljzqfvUO3VXua9Z_RrT3Ju94OZxszdC3XcU1AlAe_xBnQnI-KQu8rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f4d14622.mp4?token=E9Jn6t5pwvY-JoHzdnEI_2g0K0AkYwraPUb-DLTs31E7CYWH-iHtGtHsj5f1lH5vIFQg8iwlPM5TAkGiF9ra2zlJG5HZf9-PWbh7FFFNb8ZYP1Vb09aULhIev1ZzGwiwsHaZ-647jvqiNRfOkDYghXl5spG3p-hWa1XBCGL3CjHwTo7d8A9Pfk8hBJ6spZDxxxtR6b7jgTu-EvuVHfyvok03byChKp_VDgBRQXRU1YQ1DvD7yyxLK9Q1Uq9z4apxJCDM6JclelkeNvFgFd53e52TD0UjbVO1ljzqfvUO3VXua9Z_RrT3Ju94OZxszdC3XcU1AlAe_xBnQnI-KQu8rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منصور حلاج و بهای سنگینِ بیان حقیقت
#پادکست_کافئین
| فصل‌دو، قسمت‌دهم
☕️
🔹
ابرعارفی که نشان داد چطور یک متمایزِ تراز اول، می‌تواند با زیرِ سؤال بردنِ پیش‌فرض‌هایِ صلبِ زمانه و اتکا به دکترینِ «اصالت و صداقتِ محض»، انحصارهای فکری و عقیدتی را بشکند و معنای جدیدی از شجاعت خلق کند.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/wJ9efEuEMdQ?si=UDDU6UoYCcmUvX5s
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/673675" target="_blank">📅 10:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673673">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs-xMc4uI_LXCB6hkBo2Q1AZtNGwbbQGpY4S2oNJPQAbJ4rquK3yW3Iv7ENt2p1RmU8K4dBoLL6TeubPayhohD9Tt6Faiwhu5D_fmrPRUwO6jlmHvf3sbv8Ua0BS6e9KU63QgF5NWxIQ1hab_-aknHQEojNNdJ3a-hvbdLZfhIBhz5j59hAFVxLX_zqHdZUucvjmnsnyxw8iXxFk0d3jTYl15YCkDntQExEVy06DIPeC6RYBfQ1CT-kRgX22ET61O62yABtqtJyGKsWFzMngQ5aR_2p-ao4EPmAHeU-rJ0cWhAWw_oUSPPqo2e4fX01HXe854SVt-a3NfPSd3r2Ljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
فروش انواع موتور برق بنزینی و دوگانه سوز
⚡
🔴
انواع مدل های سایلنت
💤
و معمولی
👍
کم صدا، کم مصرف، دائم کار
⛽
دوگانه سوز بنزینی و گازشهری
‌
💯
از برندهای اسلانگ و هوندا با موتور اصل Honda
‌
✅
گارانتی و خدمات پس از فروش
‌
🌇
مناسب برای مصارف خانگی، تجاری و کارگاهی ، دفاتر اداری و مغازه ، باغ و ویلا
✅
امکان بازدید حضوری در تهران و خرید آنلاین
☎️
تماس با ما
021-45537
📲
لینک کانال تلگرام :
@i9groupir
📲
اینستاگرام:
@i9groupir
🌐
وبسایت
https://i-9.ir</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/673673" target="_blank">📅 10:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673672">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c1fc1cf2.mp4?token=ebov4OqCbaeaKbyjl0gYFpPNIKj55QkqaVgY1uvlk3N9Mo8vFqzSi7wZHcw4g8oEUtyGh0cgvldvaLjvv3JaqaYkAF0yJZq1hGXbFqkze6DDPhXLZraHuj4ghyvJtE8hs0NMfhpeGOTKj54sKH16RTbQKkACTjN_BO2OXCYUw9rWOQzgcgatT9012lIRaxhc2zxh6OWaqyEp5Ugq4m6-4nmXJ1KuAfPxc5jjGNgpvJx20eIe4Mk-URJ738NhbFSthkCRg_imVakmJj1SeotoQhNloEIuyfMtWQ7N1i1oRSZO2_j3E3nLMPzfyfCR6yrRgByH9FMoX34tAtmXgjqeIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c1fc1cf2.mp4?token=ebov4OqCbaeaKbyjl0gYFpPNIKj55QkqaVgY1uvlk3N9Mo8vFqzSi7wZHcw4g8oEUtyGh0cgvldvaLjvv3JaqaYkAF0yJZq1hGXbFqkze6DDPhXLZraHuj4ghyvJtE8hs0NMfhpeGOTKj54sKH16RTbQKkACTjN_BO2OXCYUw9rWOQzgcgatT9012lIRaxhc2zxh6OWaqyEp5Ugq4m6-4nmXJ1KuAfPxc5jjGNgpvJx20eIe4Mk-URJ738NhbFSthkCRg_imVakmJj1SeotoQhNloEIuyfMtWQ7N1i1oRSZO2_j3E3nLMPzfyfCR6yrRgByH9FMoX34tAtmXgjqeIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محاصره کامل منطقه حادثه در نیویورک  پلیس نیویورک:
🔹
عامل حمله مسلحانه و انفجار مقابل «فدرال پلازا» را بازداشت کردیم.
🔹
پلیس نیویورک انفجار یک شیء آتش‌زا مقابل ساختمان نهادهای امنیتی (از جمله اف‌بی‌آی) در منهتن را تأیید و شایعات تیراندازی را رد کرد.
📲
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/673672" target="_blank">📅 09:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673667">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳۹/ زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین با چند فروند موشک کروز مورد هجوم قرار گرفت   روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت قهرمان و شجاع ایران اسلامی؛  با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/673667" target="_blank">📅 09:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673665">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳۸: تخریب سامانه راداری دفاع موشکی و انهدام یک فروند هواپیمای اف ۱۵ در داخل شیلتر در اردن   روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت عظیم الشأن ایران اسلامی، با استعانت از خدای متعال، در ادامه عملیات پاکسازی منطقه از رادارها و سامانه های…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/673665" target="_blank">📅 09:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673664">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳۸: تخریب سامانه راداری دفاع موشکی و انهدام یک فروند هواپیمای اف ۱۵ در داخل شیلتر در اردن
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت عظیم الشأن ایران اسلامی،
با استعانت از خدای متعال، در ادامه عملیات پاکسازی منطقه از رادارها و سامانه های پدافندی و هموار کردن مسیر حملات موشکی و پهپادی گسترده‌تر و تکمیل شب سیاه راداری دشمن آمریکایی، رزمندگان غیرتمند نیروی هوافضای سپاه در ادامه موج ۲۴ عملیات نصر ۲ در حمله موشکی به پایگاه آمریکایی در اردن یک سامانه راداری دفاع موشکی را تخریب و یک فروند هواپیمای اف ۱۵ را در داخل شیلتر مربوط منهدم کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/673664" target="_blank">📅 09:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSe69JwP245XKfmPOMc4Jp2peNDPr1vQVxswYqqTHtJZXuk5KbtQzJ75AQuGFF0C98ZM4CjLCEmpw3HKyFdDSSRCTj0BhVE18Tzta-LBvWWi9FoBUIqy_o-gIp9-HdFMGttl9lxc9dHNiZVsT07aDa_g9_2jMVIKYopSGgdBjTL_1XvuUCN-saYzfPu8v1VwDRDmzcv8QPiLIt9WN0vwhDMQS6wGVhqk0p5rTlXKDFoK4n8vk9JK7uxus1Lc8kU0gaHNWztMqcClLdB6kIUcuj_ENSkhJSm4Dq1a9ho9cEwt5PI_ueKmTqBYKBfHJjcAVRA65fusaj7oVsqyf1yJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳ تکنیک طلایی؛ برای گرفتن پاسخ حرفه ای از هوش مصنوعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/673660" target="_blank">📅 08:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/175a88f491.mp4?token=At-LN5VmXme4y5-Bjsxt0fF-WiWJ6bj6kwSoLXIxXVtLpx4PElIGLXtBq0UPe2ePBIbPB0DlDyB-1sp5ZNE6LHtg-whKrgF1Z4z6m3iT1DVMlfg1Rga0T68MFFFI_SMsP3bO3vw-IgMgY0RN3POMKuYxvWphR8WTDxnAZoXXjbIRJ_zb1-S2PqlZVueh6gRusLDPk5Qo2XYcqnX3Wa4hXO4e0cGkPTq86oKEnZu5rqZhP7sf2JTiA53t1DgbC2FHMk-YmB7g_L-IAZWzOH8fYCbjzOjok9yXGU6AUW30YfrD8ysNUnMxt4suVp_ejJYXmsUHpPJoQdkcFTcSQStqxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/175a88f491.mp4?token=At-LN5VmXme4y5-Bjsxt0fF-WiWJ6bj6kwSoLXIxXVtLpx4PElIGLXtBq0UPe2ePBIbPB0DlDyB-1sp5ZNE6LHtg-whKrgF1Z4z6m3iT1DVMlfg1Rga0T68MFFFI_SMsP3bO3vw-IgMgY0RN3POMKuYxvWphR8WTDxnAZoXXjbIRJ_zb1-S2PqlZVueh6gRusLDPk5Qo2XYcqnX3Wa4hXO4e0cGkPTq86oKEnZu5rqZhP7sf2JTiA53t1DgbC2FHMk-YmB7g_L-IAZWzOH8fYCbjzOjok9yXGU6AUW30YfrD8ysNUnMxt4suVp_ejJYXmsUHpPJoQdkcFTcSQStqxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیبایی‌ها در اعماق دریا
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/673659" target="_blank">📅 08:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673658">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2eae916e0.mp4?token=l0AiLNEe0b7J1PLacPrkjSeg7LaRsH561Q3ZSMm290gxvXXDB1SMiSuhidDelZRwcqAAinEA2XkpCFJzGT_m06Wsl7boKeRgV3aGYYN3Q87HhpnXZU3QLQTFz3jAmBxLDHTkp06HC2ZzIW2IM2vKyRhEA_odtFqMV5Iibkv5nhssTf-8aZP_2OpHP5aEjMXxhY95AlMH5KvI6lWeV3eLRR2NylTZcAvqwlnjE--plykxWCNvRyZluGUcg3JAK4nTXLFSlhUHSIS-pn7EaT1u5egXQpk7fiHUWyZjp6K4pQPpo2x558vrAxwjPpqwU-Yfpmbrzs6w_ohmlG8hk84caQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2eae916e0.mp4?token=l0AiLNEe0b7J1PLacPrkjSeg7LaRsH561Q3ZSMm290gxvXXDB1SMiSuhidDelZRwcqAAinEA2XkpCFJzGT_m06Wsl7boKeRgV3aGYYN3Q87HhpnXZU3QLQTFz3jAmBxLDHTkp06HC2ZzIW2IM2vKyRhEA_odtFqMV5Iibkv5nhssTf-8aZP_2OpHP5aEjMXxhY95AlMH5KvI6lWeV3eLRR2NylTZcAvqwlnjE--plykxWCNvRyZluGUcg3JAK4nTXLFSlhUHSIS-pn7EaT1u5egXQpk7fiHUWyZjp6K4pQPpo2x558vrAxwjPpqwU-Yfpmbrzs6w_ohmlG8hk84caQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه قدرت و استقامت پاهات کمه این تمرین‌ها رو انجام بده #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/673658" target="_blank">📅 07:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673655">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfO5F-arJyp7E3c43I8p8UY5F7fAPNQrFQC2mYs5X1x-KuQNgJ0_FOTCR3W8QVE7css8h7mBYPmeMtRlZE7fhZqN1MKkAKZ-lgoa5tJsoA2bosvAGPRcge9j-dAAglduQY9u4-h-f6k7KZcG7kZLq6lZ39jbu2OXJ7cUt4JlVpPbXg0k-xIEderuV0zForg-ckjf-6_q30F2aBaWI6BXw9-HEvtHIhaOwybIzt8A9ZGLM9HKFKrtPKIRoGhddxc8QMrY4liZgLS-aEKDwo1n4sLFq4TFXOzHgO9NwzYBcwuKVr3QOMAPajSsfCNXKQDGODuZY2ixwgXZFwagSQPwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۳۰ تیر ماه
۶ صفر ‌۱۴۴۸
۲۱ جولای ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/673655" target="_blank">📅 07:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673652">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای آکسیوس: میانجی‌ها پیشنهاد آتش‌بس را به ایران و آمریکا ارائه کردند
🔹
پایگاه خبری آکسیوس به نقل از منابع آگاه ادعا کرد که قطر، مصر، پاکستان و چند میانجی منطقه‌ای دیگر، پیشنهادی برای آتش‌بس ۱۰ روزه را به ایران و ایالات متحده ارائه کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/673652" target="_blank">📅 06:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673649">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
هشدار آمریکا به اتباعش در سراسر جهان
🔹
وزارت خارجه آمریکا بامداد سه‌شنبه از شهروندان این کشور در سراسر جهان خواست که به دلیل درگیری‌ها در منطقه غرب آسیا، هوشیار و مراقب باشند.
🔹
این وزارتخانه همچنین به اتباع آمریکایی در کشورهای غرب آسیا هشدار داد که برای لغو پروازها و بسته‌شدن حریم هوایی منطقه آماده باشند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/akhbarefori/673649" target="_blank">📅 06:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673644">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30f0f3faf1.mp4?token=cNH_UM5xYV02XenJP8Pa-mgvR7NScEaVC9Vyt2E9f53Qop9gGBLIcaF6i9NB9KQzfjZ62HOh6dlDafUqGndU1jYFvsuAdN_KzEuqUUe93_h4wKrKIwfLfbMT3jtgEB0e2mMvLv0KsP4agLpy4b94_4POdqqDpV_gwADkTneENmCxSggb4T20HeLuWpl49KE7AShc984xnXz_srlwaM7PCuTrCws0Vila2oQdp-rQMngBadpbje3AxSrv-qIif1zBHTBT99R6c1yth8aHUiVQsyKkG5Ki_aAuSCmbogycoV2xh2vxctGoBNXPwBps1l-KNyDuHe-PbcGq2QSwGemoPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30f0f3faf1.mp4?token=cNH_UM5xYV02XenJP8Pa-mgvR7NScEaVC9Vyt2E9f53Qop9gGBLIcaF6i9NB9KQzfjZ62HOh6dlDafUqGndU1jYFvsuAdN_KzEuqUUe93_h4wKrKIwfLfbMT3jtgEB0e2mMvLv0KsP4agLpy4b94_4POdqqDpV_gwADkTneENmCxSggb4T20HeLuWpl49KE7AShc984xnXz_srlwaM7PCuTrCws0Vila2oQdp-rQMngBadpbje3AxSrv-qIif1zBHTBT99R6c1yth8aHUiVQsyKkG5Ki_aAuSCmbogycoV2xh2vxctGoBNXPwBps1l-KNyDuHe-PbcGq2QSwGemoPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع تصویری ماهواره‌ای نشان می‌دهد که حملات اخیر به پایگاه سالتی اردن، تأسیسات مسکونی مورد استفاده نیروهای آمریکایی را با خاک یکسان کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/673644" target="_blank">📅 04:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673643">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
شب سیاه رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه
سپاه:
🔹
ساعاتی پیش عملیات بزرگ رزمندگان اسلام برای تنبیه ارتش کودک کش آمریکا به خاطر برهم زدن امنیت تنگه هرمز و تجاوز به نقاطی از میهن عزیزمان آغاز شد.
🔹
فرزندان شما در نیروی هوا فضای سپاه شب سیاهی برای رادارها و سامانه های پدافند هوایی آمریکا در منطقه رقم زدند و در موج ۲۴ عملیات نصر۲ با رمز مبارک یا رقیه (س)، به منظور هموار کردن راه عملیات گسترده آینده و از میان برداشتن موانع اصابت دقیق اهداف یک سامانه پدافندی و یک رادار آمریکایی در المحرق بحرین به طور کامل تخریب شد و از مدار عملیاتی خارج گردید و همچنین یک سامانه پدافند هوایی پاتریوت آمریکا در اَلرفاع بحرین هدف حمله همزمان موشکی و پهپادی قرار گرفت و نابود شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/673643" target="_blank">📅 04:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673636">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
زیاده‌گویی وزیر انرژی آمریکا: تنگه هرمز را با یا بدون همکاری ایران باز نگه می‌داریم
🔹
کریس رایت تأکید کرد ایالات متحده برای تضمین جریان انرژی در تنگه هرمز متعهد است.
🔹
ترامپ خواهان توافق صلح است، اما در صورت عدم تمایل تهران به مذاکره، آمریکا رأساً امنیت کشتیرانی را تأمین خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/akhbarefori/673636" target="_blank">📅 02:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673635">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
نفتکش هدف قرار گرفته، کویتی است
رسانه عراقی «صابرین‌نیوز»:
🔹
نفتکشی که در نزدیکی سواحل عمان مورد حمله قرار گرفت، متعلق به کویت است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/673635" target="_blank">📅 02:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673633">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
فاکس‌نیوز: احتمال بازگشت آمریکا به جنگ گسترده با ایران
ادعای مقام‌های ارشد آمریکایی در مصاحبه با شبکه «فاکس‌نیوز»:
🔹
رئیس جمهور این کشور در چند روز آتی برای گسترش عملیات نظامی علیه ایران و بازگشت به جنگ تمام عیار تصمیم می‌گیرد./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/673633" target="_blank">📅 02:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673631">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/211c6f0622.mp4?token=sGQ-rGUuTsGxqTYYBzJ7sq3g0JRxu_7jhTs-OVbFZ8F5iRhSxgzxhp8q0wpMeiWz6MrtinQ-7_Vs-rUHfN9rWDoAl9H-loQkp1Eu_VKGj5ozVt_JDHfbByu3fXl0zOfqx7RRmRqne0f7KqlGdGrB8V51RgCmHJX5jgTl4htEVGSx-BhtlkkDc0L0L9jP3RZ-sHrAabvQjjgtfH7YIoRKE60poEg0Vy6JIzfbCJfouk-mrZQVNUsRxHI1mvIsn1AH51IdrjQPU_2wK0NV-Xn8GUoJTVVEh8tch_EAcmaOXFCSRteb7BEprZfF--gB4jz34Ehv5XbeWDy95ejmdehAkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/211c6f0622.mp4?token=sGQ-rGUuTsGxqTYYBzJ7sq3g0JRxu_7jhTs-OVbFZ8F5iRhSxgzxhp8q0wpMeiWz6MrtinQ-7_Vs-rUHfN9rWDoAl9H-loQkp1Eu_VKGj5ozVt_JDHfbByu3fXl0zOfqx7RRmRqne0f7KqlGdGrB8V51RgCmHJX5jgTl4htEVGSx-BhtlkkDc0L0L9jP3RZ-sHrAabvQjjgtfH7YIoRKE60poEg0Vy6JIzfbCJfouk-mrZQVNUsRxHI1mvIsn1AH51IdrjQPU_2wK0NV-Xn8GUoJTVVEh8tch_EAcmaOXFCSRteb7BEprZfF--gB4jz34Ehv5XbeWDy95ejmdehAkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله هجدهم عملیات صاعقه ارتش
؛
سامانه‌های موشکی هیمارس در کویت هدف موشک‌های زمین به زمین ارتش قرار گرفت
روابط عمومی ارتش:
🔹
در پاسخ به حملات موشکی شیطان بزرگ به مناطقی از کشورمان، ساعتی قبل و در مرحله هجدهم عملیات صاعقه، نیروی زمینی ارتش با موشک‌های زمین به زمین، سامانه‌های موشکی هیمارس ارتش تروریستی آمریکا مستقر در پایگاه عریفجان کویت را هدف قرار داد.
🔹
هیمارس یک سامانه موشکی متحرک با امکان جابجایی سریع علیه اهداف زمینی است که هدف قرار گرفتن آن‌ها، موجب  آسیب به لایه‌های آفندی و پدافندی و کاهش قدرت موشکی دشمن در جنایت‌های تجاوزکارانه می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/akhbarefori/673631" target="_blank">📅 01:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673628">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
حمله آمریکا به سایت نیروگاه دارخوین  سازمان انرژی اتمی ایران:
🔹
آمریکا روز یکشنبه ۲۸ تیر ۱۴۰۵ حوالی ساعت ۳:۳۹ بامداد، با تعدادی پرتابه به سایت در حال ساخت نیروگاه دارخوین حمله کرده است./ میزان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/akhbarefori/673628" target="_blank">📅 01:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673626">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e469e9d2b0.mp4?token=hau9DOrqHF3WpGk56Qir_tHI5QQ961ZAP4QOr-u-sY8OsXXDoQJXiHQQKZEtM8asaPI2Bw8ie64yan_sDV5abulCtMGAOPC2q2Cgpt9ccb3OwBChcbjqtq_gXafmzVtLTYUAI6AbmsMh_gjd3I8JOV8dWvhdiHUrmju4m_FkVkAbiVxSjn4TaFVz7DuaFM-hs42uJMgTF-5dh96OGgYkijAhhN4GQuZPq7k0CTrPTWODcUZzx-LAFnx2AjqC2LsCVVTVBFrc1anyhjXp8hkzcaRwE0E6CjhpKFFv6jhTYODJ1DP5XHFaU3xkBMkz2G4r7lVupNxrSkw-_tbXGL-_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e469e9d2b0.mp4?token=hau9DOrqHF3WpGk56Qir_tHI5QQ961ZAP4QOr-u-sY8OsXXDoQJXiHQQKZEtM8asaPI2Bw8ie64yan_sDV5abulCtMGAOPC2q2Cgpt9ccb3OwBChcbjqtq_gXafmzVtLTYUAI6AbmsMh_gjd3I8JOV8dWvhdiHUrmju4m_FkVkAbiVxSjn4TaFVz7DuaFM-hs42uJMgTF-5dh96OGgYkijAhhN4GQuZPq7k0CTrPTWODcUZzx-LAFnx2AjqC2LsCVVTVBFrc1anyhjXp8hkzcaRwE0E6CjhpKFFv6jhTYODJ1DP5XHFaU3xkBMkz2G4r7lVupNxrSkw-_tbXGL-_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محاصره دریایی یمن علیه عربستان؛ صنعا معادله «محاصره در برابر محاصره» را اجرایی کرد
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای رسمی در پاسخ به محاصره ۱۲ ساله این کشور، از آغاز تحریم و محاصره کامل ناوبری دریایی علیه عربستان سعودی خبر دادند.
🔹
صنعا با تأکید بر آمادگی…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/akhbarefori/673626" target="_blank">📅 01:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673624">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
شنیده شدن صدای ۲ انفجار در اصفهان
🔹
دقایقی پیش صدای ۲ انفجار در شهر اصفهان شنیده شد.
🔹
هنوز علت دقیق و منشأ این صدای بلند مشخص نشده و تا این لحظه هیچ‌کدام از نهادهای رسمی و مسئولان استانی در این باره اطلاع‌رسانی نکرده‌اند/ مهر  #اخبار_اصفهان در فضای مجازی…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/akhbarefori/673624" target="_blank">📅 01:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673615">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
شنیده شدن انفجاراتی در شیراز
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/akhbarefori/673615" target="_blank">📅 00:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673613">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00e162db2.mp4?token=KzqKUVameh21VjAGzwWhKZ-Jf90LpYkLdUKy6m6yxocaw2mBJw3oix5g5saoFUOqk5JUi7RR2SwrN0gDw09SADqq-U6w1YNyKc1Umc57lYOqcTKZZYcT5KDXL6ldZWSMb8x7Oelpt8mo9WBoADVCyeZzlX-NlB_VWANVmGdKmxM-dBPPvQJffssvTtJuE_MxeEfscgcnz2_OQR0HSQHMxy_f0siYoUDWq0o1vGeS3SZD0OnN9vXapX1ybKNgV14tbBgHkvqyKMIbsslM4TQnI0H3dAsMMxAJmKnBsClttHeNRHSTi0AfOu8nTTUmaY6lxZZmUV84UadTgTyY8OhUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00e162db2.mp4?token=KzqKUVameh21VjAGzwWhKZ-Jf90LpYkLdUKy6m6yxocaw2mBJw3oix5g5saoFUOqk5JUi7RR2SwrN0gDw09SADqq-U6w1YNyKc1Umc57lYOqcTKZZYcT5KDXL6ldZWSMb8x7Oelpt8mo9WBoADVCyeZzlX-NlB_VWANVmGdKmxM-dBPPvQJffssvTtJuE_MxeEfscgcnz2_OQR0HSQHMxy_f0siYoUDWq0o1vGeS3SZD0OnN9vXapX1ybKNgV14tbBgHkvqyKMIbsslM4TQnI0H3dAsMMxAJmKnBsClttHeNRHSTi0AfOu8nTTUmaY6lxZZmUV84UadTgTyY8OhUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انصارالله: موشک‌های ضدکشتی آماده هستند تا هر کشتی‌ای را که محاصره را نقض کند، مجازات کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/akhbarefori/673613" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673612">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
شنیده شدن صدای ۲ انفجار در اصفهان
🔹
دقایقی پیش صدای ۲ انفجار در شهر اصفهان شنیده شد.
🔹
هنوز علت دقیق و منشأ این صدای بلند مشخص نشده و تا این لحظه هیچ‌کدام از نهادهای رسمی و مسئولان استانی در این باره اطلاع‌رسانی نکرده‌اند/ مهر
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/akhbarefori/673612" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673608">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است/ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/akhbarefori/673608" target="_blank">📅 00:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
وال استریت ژورنال: آژیرهای هشدار برابر موشک‌های ایران جاماندند
🔹
موشک بالستیک ایران به واحدهای پیش‌ساخته در پایگاه هوایی موفق السلطییط اردن برخورد کرد.
🔹
آژیرهای هشدار قبل از هر حمله به صدا در می‌آمدند، اما اینبار پرسنل به پناهگاه نرسیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/673603" target="_blank">📅 00:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673601">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
همه سناریو‌های حمله زمینی به کشور و نتایج آن/ نیروی زمینی آمریکا احتمالا از کجا وارد خاک ایران خواهد شد؟
👇
khabarfoori.com/fa/tiny/news-3231685
🔹
آغاز جنگ تمام عیار یمن و عربستان / انصارالله محاصره دریایی عربستان را کلید زد / چه بر سر ریاض می‌آید؟
👇
khabarfoori.com/fa/tiny/news-3231838
🔹
آخرین گمانه زنی ها در مورد احتمال مذاکره جدید ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3231846
🔹
حاشیه‌های یک عکس در مراسم بزرگداشت داماد رهبر شهید؛ این نوجوان کیست؟
khabarfoori.com/fa/tiny/news-3231705
🔹
جنیفر لوپز فاش کرد چه چیزی یک مرد را برایش جذاب می‌کند
👇
khabarfoori.com/fa/tiny/news-3231848
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/akhbarefori/673601" target="_blank">📅 00:16 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
