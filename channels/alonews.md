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
<img src="https://cdn4.telesco.pe/file/vISDtCftnA20Twf5uc23E5YWsvus-NX9Fl1XBt3IuaK-lCAyQgU9itzXAsoZqITAjpCq3hsOexpKSyiQdKV6MTsenEBVnx8t-UMMh3Wr3oE_umV3hyotWM-ImHVDLGsIl7GPpLhrTTgQ6y-Eg3KZ7HQgKnwKruupHC6tyx8Rz03_sh5PHzyofSh2ZpCJazCXOp7Z_OdE40_n0DmoPnQhPCoF8B34YhHA-VsuseOBcn_V2I0P330I1C4lZcQ36KxgmlYmoHeAlQ3jGttBK_SwWoXoTHWtiQrvX2KB8d6lFts4QdUZzQeIM3QAluiRdDKu1laWRP4WPY_uuvaQLdSIvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 995K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 01:50:47</div>
<hr>

<div class="tg-post" id="msg-148871">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/148871" target="_blank">📅 01:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148870">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
یدیعوت آحارانوت: سخنرانی نتانیاهو در سازمان ملل متحد، غافلگیرانه و بر ایران متمرکز خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/alonews/148870" target="_blank">📅 01:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148869">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
چندین انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/148869" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148868">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nsff2OkMSucQdTOf01eOHmAAWnjxZEwZxca4qHnjDNeXNtK8aotafsI3sJVUVR9fmYNyq2JsasYjxPJMQ3N0s24Vz-0UiCmxabErZGvxficgEnR6tMwG1NJAB4p_AGTA2jMUxfFnDNBpDKFN7ybB0JRuelKqflnvkEHWRK1XVwMqB7lr370gtGDkwBbomkKFXdNi7mdhCfjMtIyns8GDLwOji42uw7yeSTgVy4ztR38BGNh215452y3U294YDBx6gLsPicrC58YHwz37MAQ6dGIHRgxJcxkR4m3f7k6CD2hr8VYHkN2-sQNw6csC-cBgbkfBXHDigK6sC_ZG0MhGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان تا دقایقی دیگه وارد نیویورک میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/148868" target="_blank">📅 01:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148867">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxDaBpg8rMnzD0rH8qQqcduIAc55ZDybNzSmwUHmBaS1DXzOxsQHuSJR1xE7KdrPTRk1G_sKuu68vNXRSZjMoHCZEw3ZeL_5QNegRmXRsGib6iIFOzOrum40FzI_GT2vakn0UzxUFJHqQrATH1SwNGTr5JZeTeg6Vx3K0hn9w-60xOUsLbz_VAbXCyCn7fhun7WuB5XcSOq9B7oyd5f78N3GdKXM6ySKQ064Od7LHND4hkITC1bUyjBFa0o-rN5e5a4mg-akJUlFGVrxrP2VU5sp6xQvYhpZcAJWRp8eViEQ1dOYt7daaoibPqcvVvruH8ohVkDKIBVJvJgAcXsdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صف پمپ بنزین کارگر شمالی تهران پس از مثبت ارزیابی شدن مذاکرات
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/148867" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148866">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
باراک راوید: کشورهای عربی در تلاش هستند تا جلسه‌ای بین ترامپ و رئیس‌جمهور ایران در این هفته برگزار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148866" target="_blank">📅 01:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148865">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شلیک موشک به تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/148865" target="_blank">📅 01:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148864">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9VY8B3YgWknt5qZ3I3t-ry_UU5v8SmMLj-kSMrCcsU2iOk1LtO6rAZTfU5G9-iPtShLoduicZkykToeZNWdJypGKggBBGXhgk9TShqpsPMVjO6bDTFpVAL8EiXzYOJcbUfXc_WywczM5KseJ9dbzydbkF3luoHSFEhucpJpAh6k7AfCkw1qYSQ-W_Fvjv21gsWbTjfM4UqT741vk4Np72e9MClHXtY3024yNKxxKBXx7Fp2YtLP9gBdjr2oP4TJ3LuWHV36u286C52oohNW7eI4mC2UKOXL2MU9qRVwrThKPla4jK8BFPFKyf8gmKfFnDcKeVv_zvd8y6DTYH2JzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‌‏این عکس رو یادتونه!؟
🔴
‌‏۶ مهر ۱۴۰۳ ‌‏نتانیاهو بعد از سخنرانی در مجمع عمومی سازمان ملل اومد و از نیویورک دستور حمله به ضاحیه جنوبی بیروت برای ترور نصرالله رو صادر کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/148864" target="_blank">📅 00:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148863">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/لحظاتی پیش یک منبع آمریکایی که در نشست با هیئت ایرانی در نیویورک حضور داشته اعلام کرد:
ترامپ درخواست ایران برای رفع محاصره دریایی و هوایی را نپذیرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148863" target="_blank">📅 00:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148862">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c7961ee3.mp4?token=naruiFfNS8slLxT-G2gs3OZ67yfyFkRZeOcVM6NovrpP7efd6fTwCq6w_h1uXvzt9Nx8FeE80FT0cB7YuAMSsGBh7PO0UZswkRzmBCgx98wj8oI1HtrTMEkxPhvmhyedOpxMlhlZw5kDH0RqC0toOtXiUv1GNs8xb5jr4YzltMpB4OHXIkjnsQpf52OCMkFRrTs9NanpXfSwKDAm4OUokodsNpje5wE-RTpDkdkosXOcWT7lE2ldWKNctTqz6cbeztI6bECFQXQsJmVM2AfG8D9AjygVPjjLoh4vATnUB7sDu3ShjQECURx33IYx6TtOL-zfSyVCO-E7ehH4vYneoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c7961ee3.mp4?token=naruiFfNS8slLxT-G2gs3OZ67yfyFkRZeOcVM6NovrpP7efd6fTwCq6w_h1uXvzt9Nx8FeE80FT0cB7YuAMSsGBh7PO0UZswkRzmBCgx98wj8oI1HtrTMEkxPhvmhyedOpxMlhlZw5kDH0RqC0toOtXiUv1GNs8xb5jr4YzltMpB4OHXIkjnsQpf52OCMkFRrTs9NanpXfSwKDAm4OUokodsNpje5wE-RTpDkdkosXOcWT7lE2ldWKNctTqz6cbeztI6bECFQXQsJmVM2AfG8D9AjygVPjjLoh4vATnUB7sDu3ShjQECURx33IYx6TtOL-zfSyVCO-E7ehH4vYneoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست وزیر قطر پریروز گفت ایران صلح طلب نیست و ... عراقچی هم الان دیدش و اینجوری پرید بغلش
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148862" target="_blank">📅 00:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148861">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
یک منبع آمریکایی که در نشست هیئت ایرانی حضور داشته است به الحدث گفته است:
فرص دستیابی به توافق محدود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/148861" target="_blank">📅 00:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148860">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
تتر وارد کانال 223 هزار تومان شد</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148860" target="_blank">📅 00:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148859">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
تنگه هرمز بزودی از حالت ناامنی توسط ایران خارج میشه و محاصره دریایی هم لغو میشه
🔴
مذاکرات هم شروع میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/148859" target="_blank">📅 00:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148858">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
هم اکنون شاهد هجوم امت معکوس به عراقچی بابت دیدار با ویتکاف هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/148858" target="_blank">📅 00:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148857">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری و رسمی/از همین الان محاصره هوایی ایران اجرایی شد
🔴
هیچ پرواز خارجی‌ای انجام نمیشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148857" target="_blank">📅 00:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148856">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تابستون هم تموم شد، ولی داغ دی ماه هیچوقت تموم نمیشه.  [@AloTweet]</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148856" target="_blank">📅 00:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148855">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رسما وارد پاییز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148855" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148854">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: ما به دنبال جایگزین برای حکومت ایران نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148854" target="_blank">📅 23:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148853">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رسانه MS Now:  به گفته یک مقام آمریکایی، ترامپ اخیراً حکمی را امضا کرده است که به‌طور رسمی و دائمی مارکو روبیو را به‌عنوان مشاور امنیت ملی ایالات متحده منصوب می‌کند.
🔴
روبیو پیش از این به‌صورت سرپرست این سمت را بر عهده داشت، اما اکنون این انتصاب رسمی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148853" target="_blank">📅 23:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148852">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTQ4KY-DnnpcvGSEpG1sr9-rZQ925zlGJn3tA_1WymLTtUD5r8jnunsx_bn1sZSTxJVbH3EwaMSnwlqSOUePpahlcg40-QmnuYTFzDaEvpxnQLPGaM4rkLGdsSV9j20nceeuR5mWe2MEdRcS-eym3cF6e1CSD0aa-SziddALNwZscZdlVe-CFmPA-QVQtAJLXadW89c02AbhjMbRROATBMMZFv8sISFJRgsn3WZ4GzogkLtoFmOsUeDUfy4VZkiKtmFoxFjueTKoz7hDUK5cnjqAcRVw-WsY0EBApVbBQE3bh8lg2scB1PCicwDjZCBdcaRoQwWDVx6wkEyPlpEZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای پزشکیان تا ساعتی دیگر وارد نیویورک می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148852" target="_blank">📅 23:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148851">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نیویورک پست: رژیم ایران پسران ۱۲ ساله را برای آموزش در یگان‌های «ایثار» یه خدمت می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/148851" target="_blank">📅 23:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148850">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
عجیب و ترسناک
‼️
🔴
هر وقت عراقچی فضای مذاکرات را مثبت ارزیابی کرده بود بلافاصله جنگ شروع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/148850" target="_blank">📅 23:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148849">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
الجزیره: فضای دیدار ایران و آمریکا مثبت گزارش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148849" target="_blank">📅 23:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148848">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ: ما ایران را منزوی کردیم
🔴
تمام کشتی های نیروهای دریایی ایران نابود شدند و شرکت های زیرساختی آنها نابود شده است.
🔴
پول ایران بی ارزش شده و تورم بسیار بالایی دارند.
🔴
ما ایران را ایزوله و منزوی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148848" target="_blank">📅 23:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148847">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
واشنگتن پست به نقل از مقامات آمریکایی: پایان دادن به جنگ با ایران اولویت اصلی کاخ سفید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/148847" target="_blank">📅 23:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148846">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری / ترامپ درباره ایران: یا ما به یک توافق خواهیم رسید، یا این موضوع به سرعت و به طور کامل به پایان خواهد رسید.
🔴
این موضوع آنقدر سریع به پایان خواهد رسید که سرتان گیج خواهد رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148846" target="_blank">📅 23:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148845">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: نیروی دریایی ایالات متحده تنگه هرمز را از مین‌ها پاکسازی کرد و ما توانستیم بیش از یک میلیارد بشکه نفت را از آن خارج کنیم!
🔴
نیروی دریایی ما عالی است و محاصره ما عالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148845" target="_blank">📅 23:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148844">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ درباره اردوغان : دوست من از ترکیه، او شخصیتی قوی است. با او شوخی نکنید؛ او فردی سرسخت است.
🔴
او یک شخصیت فوق‌العاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/148844" target="_blank">📅 23:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148843">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبروکر ایکس چیف</strong></div>
<div class="tg-text">🏆
ایکس‌چیف برنده جایزه
«Best FX Service Provider»
شد!
جایزه «Best FX Service Provider» به پاس عملکرد برجسته در ارائه خدمات فارکس، کیفیت تجربه معاملاتی و تمرکز بر نیازهای معامله‌گران به ایکس‌چیف اهدا شد.
🎖
یک دستاورد تازه در مسیر حضور جهانی ایکس‌چیف؛ این بار در Forex Expo Dubai 2026، یکی از مهم‌ترین رویدادهای صنعت مالی جهان.
هر جایزه، داستان یک تفاوت است.
ایکس‌چیف؛ در مسیر بالاترین استاندارد خدمات فارکس.
@xChief_ir</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148843" target="_blank">📅 23:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148842">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ : اقتصاد ایران در وضعیت بسیار بدی قرار دارد. ما ایران را از نظر اقتصادی کاملاً منزوی کرده‌ایم.
🔴
رهبران ایران باید قبل از اینکه خیلی دیر شود از این فرصت استفاده کنند.
🔴
ما معتقدیم بحران با ایران می‌تواند پس از انتخابات میان‌دوره‌ای آمریکا پایان یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/148842" target="_blank">📅 23:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148841">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ درباره تنگه هرمز: ما هر شب 25 تا 30 کشتی را هدف قرار می‌دهیم، گاهی اوقات در طول روز، اما بیشتر این عملیات‌ها در شب انجام می‌شوند.
🔴
این محاصره، قوی‌ترین چیزی است که تا به حال کسی دیده است. ما به آن "دیوار فولادی" می‌گوییم.
🔴
در حال حاضر، حجم نفت بیشتری نسبت به هر زمان دیگری از آغاز این درگیری، از طریق تنگه هرمز جریان دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/148841" target="_blank">📅 23:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148840">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / ترامپ: اگر شاهد فعالیت‌هایی در آنجا باشیم، ممکن است به کوه کلنگ حمله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148840" target="_blank">📅 23:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148839">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148839" target="_blank">📅 23:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148838">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/148838" target="_blank">📅 23:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148837">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما آن‌ها را به شدت تحت فشار قرار داده‌ایم، اما در این باره اغراق نمی‌کنیم.
🔴
امیدوارم آن‌ها کاری انجام دهند که واقعاً به نفع مردمشان باشد، و من فکر می‌کنم که آن‌ها در واقع این کار را انجام خواهند داد، من واقعاً اینطور فکر می‌کنم
🔴
گزینه دیگر، گزینه‌ای قابل قبول برای هیچ‌کس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148837" target="_blank">📅 23:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148836">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26bb6cce1.mp4?token=ilq3bHOJO2XB3470MoxPOGxwhDF-Xn279D8xC8n8h58Ne8sRSKTFUgQdQXc8Xk7PurXitU9qbThV7QbFVi1ZMz9IeBry5mFJ91BhgjY_AxOHf-VaWYdq6QBl4ooY8cpen4fK08t6YFffsV2x2MGpP6BqMCP62mr8b4sxSfxVS9WbwhYOB9cnuRQe4NRGujdVqGJ2fRXCB3QErIDi4OInS12pDqfjbkxlNhooEvtR5B7Dq8vGm5P76phPataTFh92bqjNxe3mzHCDot3XCj17DhF68vCK8jDzbI3dpmcpFRmxZcIIOL0k28mkL2SNfuEggjcotxspAcbARuLxwwThHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26bb6cce1.mp4?token=ilq3bHOJO2XB3470MoxPOGxwhDF-Xn279D8xC8n8h58Ne8sRSKTFUgQdQXc8Xk7PurXitU9qbThV7QbFVi1ZMz9IeBry5mFJ91BhgjY_AxOHf-VaWYdq6QBl4ooY8cpen4fK08t6YFffsV2x2MGpP6BqMCP62mr8b4sxSfxVS9WbwhYOB9cnuRQe4NRGujdVqGJ2fRXCB3QErIDi4OInS12pDqfjbkxlNhooEvtR5B7Dq8vGm5P76phPataTFh92bqjNxe3mzHCDot3XCj17DhF68vCK8jDzbI3dpmcpFRmxZcIIOL0k28mkL2SNfuEggjcotxspAcbARuLxwwThHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره قایق‌های مخدر در جلسه سپر آمریکا: به ما اطلاع دهید و ما آن‌ها را از بین می‌بریم.
🔴
یا خودتان آن‌ها را از بین ببرید. من این را حتی بیشتر دوست دارم.
🔴
اگر نمی‌توانید، ما به جای شما این کار را انجام می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148836" target="_blank">📅 23:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148835">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d942437d.mp4?token=fZE-QMAgou6xhVJsXgiS2h9_m0L_1FRiyYHFoFV9MrdLpCV3HyprGlrrVsMs-mo--BLEtXd1aOGuLYcgO_zgVVZ-1QOfoPPLo3Mk3yig7cg432EIDDdmrMjtAWPfrl9RmG9-RSMv-4QQrq7j4ZdXQu4bG4fWtBFnkRt0J7pSEOn_Vlw15-X-7yqEg2MQnX4KkN41HDDsJmtA_eMIBREjazX-mpZ8mCqBDQG09ed207wbHcbd4gb8sOR7uHK8A93iErE6G3Lx40-HNJKuyxoWZcM6hAgog7hyo1NL7jO8TlJvYt5Y_f6vqGfH4hz6B3WMIWeiJLQXmC-65jGaTI5dIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d942437d.mp4?token=fZE-QMAgou6xhVJsXgiS2h9_m0L_1FRiyYHFoFV9MrdLpCV3HyprGlrrVsMs-mo--BLEtXd1aOGuLYcgO_zgVVZ-1QOfoPPLo3Mk3yig7cg432EIDDdmrMjtAWPfrl9RmG9-RSMv-4QQrq7j4ZdXQu4bG4fWtBFnkRt0J7pSEOn_Vlw15-X-7yqEg2MQnX4KkN41HDDsJmtA_eMIBREjazX-mpZ8mCqBDQG09ed207wbHcbd4gb8sOR7uHK8A93iErE6G3Lx40-HNJKuyxoWZcM6hAgog7hyo1NL7jO8TlJvYt5Y_f6vqGfH4hz6B3WMIWeiJLQXmC-65jGaTI5dIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
استیو و جارِد امروز جلسه‌ای بسیار سازنده با دو میانجی از ایران داشتند. خواهیم دید که نتیجه این جلسه چه خواهد بود.
🔴
به نظر من، یک حرکت قوی برای رسیدن به توافق وجود دارد. این چیزی است که ما از همه می‌شنویم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148835" target="_blank">📅 23:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148834">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری/ترامپ: شتاب قابل‌توجهی برای دستیابی به توافق با ایران وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/148834" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148833">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GQfFtiyZ_GdYYplZy6s3Qbv286zau4CRoo4uTx3DNBLtuO5VSR1DSWZY6OujRW8vU5C-BJjMD07oyhE9ZJPbH41CAG_W2XP8r8xoTAf18wIX0N5XNR7qhc5bGdrOPunuLw385_UiDelNvk8gU7QM-v0aDK4E5Q74GNR4_9ZfdahLPqZQtf4ort7PtsObnxAJHivyQIAHpmCTOuNgpgdsRsOuvVkeW-VfRIMZn568k2WMRLpTdJFCN1muBcBH8j7P4ItwRl-_KiQgczOWIQ3zdDn3k9IQ3gXQ1Xh-ISIOFYomjtxjOP01fY3LbcHl2EeNrSlCrS69SxTQA7pBC8e4Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما
: با خایه مالی آمریکایی‌ها، عراقچی و ویتکاف در حاشیه مجمع عمومی سازمان ملل دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148833" target="_blank">📅 23:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148832">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مدیرعامل شرکت ارتباطات زیرساخت:
۱۰ درصد ترافیک اینترنت ایران به استارلینک رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148832" target="_blank">📅 22:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148831">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ ریاست جلسه‌ای خصوصی را بر عهده گرفت که در آن نمایندگانی از کشورهای عضو شورای همکاری خلیج فارس، مصر، سوریه، ترکیه، عراق، اردن و لبنان شرکت داشتند. این جلسه در حاشیه کارها و فعالیت‌های مجمع عمومی سازمان ملل متحد در نیویورک برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/148831" target="_blank">📅 22:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148830">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
العربیه: ویتکاف به طور مستقیم و بدون واسطه با هیئت ایرانی ۳ ساعت گفتگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/148830" target="_blank">📅 22:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148829">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
اتحادیه اروپا تحریم‌های روسیه را برای سه سال دیگر تمدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148829" target="_blank">📅 22:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148828">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
یوسف بهرامی فعال اقتصادی مدعی شد عباس عراقچی با استیو ویتکاف دیدار ۱۲۰دقیقه ای  داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/148828" target="_blank">📅 22:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148827">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
اسرائیل هیوم به نقل از منابع آمریکایی:
جلسه از پیش برنامه‌ریزی شده آمریکا با تیم ایرانی عراقچی، با حضور نخست وزیر قطر، در مورد از سرگیری مذاکرات و باز کردن تنگه هرمز بحث شد؛ هیچ توافقی در مورد مسائل مورد اختلاف حاصل نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/148827" target="_blank">📅 22:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148826">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
روزنامه نوبنیاد به خاطر حضور عراقچی تو سازمان ملل اونو «بی‌غیرت» خطاب کرد و خواستار استیضاح و برخورد با وی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/148826" target="_blank">📅 22:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148825">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ویتکاف: دیدار با ایرانی‌ها خوب پیش رفت و در حال حاضر احساس بسیار خوبی دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/148825" target="_blank">📅 22:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبرنگار i24: استیو ویتکاف و جرد کوشنر، مقام‌های آمریکایی بودند که امروز با هیئت ایرانی دیدار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/148824" target="_blank">📅 22:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEHnYgUPqlK-1XL7bM3HvoAokNmGaeodKf9QdqmlxJYS2iY-1h7N-TtVh0GmcTO4Tg3lI_9t0NhmblVv4agXMiBBoERO2QyxwHGN-GQsulsy6_WI5_cn6YHhKC7DCMacs9ikxbOl7A6zx8zLWih_FMkxMz1UlrT-WXSyUJe6c0SEkkYHpowwthm3RJPoIn60OWSgQ_vnC8sW-ycS6kZ4CvoH9n-iaK3bPijJTn2tv7WEkbNMQkvUKNBJ32w2Ag4Ao1nSTs2At65WbwI7KpQjp--8aIj_DaA4qJa4VtGa2DahCX6mlttIHOKoRNdXbz30YOSnRRyVnUcm4YD94KiFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش سنگین قیمت نفت بعد از سخنان ترامپ درباره ملاقات با ایرانی ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/148823" target="_blank">📅 21:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کارولین لیویت: گاهی فکر میکنم رئیس‌جمهور ترامپ بیشتر از مردها به حرف زن‌ها گوش میده. اون احترام خیلی زیادی برای زن‌ها قائله
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/148822" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: جلسه کوشنر و ویتکوف با مقامات ایرانی در نیویورک بسیار خوب برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/148821" target="_blank">📅 21:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ویتکاف از ارائه جزئیات درباره دیدار با تیم ایرانی در سازمان ملل امتناع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/148820" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / ترامپ درباره ایران: «آن‌ها قرار است در آینده‌ای بسیار نزدیک، جلسه دیگری داشته باشند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/148819" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148818">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: مقامات آمریکایی پیش‌تر به مدت سه ساعت با یک هیئت ایرانی دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/148818" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
امیر قطر: تهاجم اسرائیل که با غرور و خودخواهی مشخص شده است، به کشورهای همسایه گسترش یافته و بر امنیت کل منطقه تأثیر گذاشته است.
🔴
ویران‌سازی روستاهای کامل در جنوب لبنان در پرتاب روز، یادآور تاریخ آن در فلسطین است.
🔴
مقابله با اسرائیل، پایان دادن به خساراتی که وارد می‌کند و مهار رفتارهای غیرقانونی آن، آزمون واقعی جدیت جامعه جهانی در حفظ ارزش‌ها و حاکمیت قانون است.
🔴
قانون باید به طور مساوی برای همه اعمال شود. زمانی که قانون بر آسیب‌پذیران حاکم است اما قدرتمندان را در امان نگه می‌دارد، معنای خود را از دست می‌دهد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/148817" target="_blank">📅 21:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: صنایع هسته‌ای ایران را بمباران کردیم؛ باید کنترل خود را در منطقه حفظ می‌کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/148816" target="_blank">📅 21:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148815">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCmmWpheS6B8c5OG5Xn6jTHUIr-FgDcXm6YkoATxBkUIfqzoxakvlNa9lKZdALZOu0NTgg_25_gQv-HrNy9QWLo6T_RS65Uizf0SjPQ6sHtO6pEmqGm2lOPjtFUQY3AKTO0nOFWrD1NOGek4s2XxfVSIBF5fidf0d1ptZmRHYpc0ECWrDJ474U36hAYCa6Q9TZ3U81Mb1FO3A7jt5sEjlYbUaSsFiQeYNIpg0CHO2GtSYDa_K25lPIDaGNmWIdKMBHu36b5SokPHsAHylTfi2-MKlaaZrHbv8f0pmqoKnsjAMDW-Vbh5BfE0KPSLE0luFJEToEC1OeMr7L_jJYmBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جمهوری آذربایجان هم رسماً پروازها به ایران را متوقف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/148815" target="_blank">📅 21:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148813">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGWh0MBWRVl5wF_mPQuvmAFtzIBlWtDbSv4ogBCsRxeVbwJatnlJQswZXsQueNYHMmSErnxMcUaKsavdqLJIotRDGvhsGSlHsd4MlLVVTInt6oLrSK4q6j9u2NgHVkymzOSoi6qhzBUcJb8Vo-x_3yUq4QP6iBmA-YQEU5EGZgk3n2B3tIRn4bPj2t21jaKxMqTojJ3SgsQthRYSTWDRQ9WfnY9vu-1Dq6oePwqrTOFuYPE-SJd9sYZgTfKKKX_7bua2ItXpHGZdNQpImktF3WJs_miwdI3Mh2YMq0Z995CfP6rOiN6pVmnvHpy0a3dPPo2XrAYtuvuspPvJ6abhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5d86448edb.mp4?token=S3wVJbfEQotA8VgUg2rytWud67gtg6xg1ZAzYbrf79n4hdi0xRnY3yz2DeqAlMhXgt5GRGOTMO2ufGjfQsro03vDdtQN1EcNc7eK_HdTvQKpvitthXI4PyMS9JdoPfIuDRKNfpN9mkEXgtAkMy_N8Nkn2AxMrudKAEfEm44ijUv2-et8w7IhVTJapstF0LVfHX1XTBTokXSxcHt8_YOh9QSE1oGoc9BVr_yR3MpZyBqp54fKkzFFFbqoSHk5R23s5-JjL1FUddnFatD4GE3w9_ZVokO8gAmdwypcYdyYcqmOHET_-H94aVx1X-xsV06vbvfUuHJSQM4-6CxYf7vNIiyt8yyZA30eWrR_sLAAbk-ofm1_EjYbsVn8j2aXK-NaIBE7f98JcB3eNOyOXAghrfnWnsOx88gS_Wl5m3qCnH4gTMFj8thOL6X0lYJkDTCxd1eNPvTAovu-rp3vNdZGLyPfhLpArpSGoN9mnOixEnNjsIBXtPiWdSFfkO-4V_uyJSsNcJOPrq8-1JAHAttv9tEhnXv0jvg8kZbnJJNdJexdIuj908G_H49BA3i1jprupgoW5kZk2J5hnHdkSvYFDsRNuL6d1zOpsKnygiftFlGNfAT1vxUUmm5rjg0Ryouc5U1wED2CeSQhapXeJvAYhB5Xqu_Dr1q01WfHoQB5nwU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5d86448edb.mp4?token=S3wVJbfEQotA8VgUg2rytWud67gtg6xg1ZAzYbrf79n4hdi0xRnY3yz2DeqAlMhXgt5GRGOTMO2ufGjfQsro03vDdtQN1EcNc7eK_HdTvQKpvitthXI4PyMS9JdoPfIuDRKNfpN9mkEXgtAkMy_N8Nkn2AxMrudKAEfEm44ijUv2-et8w7IhVTJapstF0LVfHX1XTBTokXSxcHt8_YOh9QSE1oGoc9BVr_yR3MpZyBqp54fKkzFFFbqoSHk5R23s5-JjL1FUddnFatD4GE3w9_ZVokO8gAmdwypcYdyYcqmOHET_-H94aVx1X-xsV06vbvfUuHJSQM4-6CxYf7vNIiyt8yyZA30eWrR_sLAAbk-ofm1_EjYbsVn8j2aXK-NaIBE7f98JcB3eNOyOXAghrfnWnsOx88gS_Wl5m3qCnH4gTMFj8thOL6X0lYJkDTCxd1eNPvTAovu-rp3vNdZGLyPfhLpArpSGoN9mnOixEnNjsIBXtPiWdSFfkO-4V_uyJSsNcJOPrq8-1JAHAttv9tEhnXv0jvg8kZbnJJNdJexdIuj908G_H49BA3i1jprupgoW5kZk2J5hnHdkSvYFDsRNuL6d1zOpsKnygiftFlGNfAT1vxUUmm5rjg0Ryouc5U1wED2CeSQhapXeJvAYhB5Xqu_Dr1q01WfHoQB5nwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری جالب از دلسی رودریگز،رئیس جمهور کنونی ونزوئلا و معاون پیشین مادورو هنگامی که ترامپ مادورو را جنایت کار نامید و به عملیات دستگیری وی می‌پرداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148813" target="_blank">📅 21:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148812">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKTE8Nr_LjGnPOEIRQ5Q9EVS7xINGP3h6ZEz-dkFtPt3P5Hyeipr1Ph6yX9vh1fy1nTMkDwsXt2ycJ6xELTnNlHqQBuwYsn5iS4NNKvRLWVVrQOz59T_Xf9biH-txRjghecKasmnEnatcKO-gyXfHSUw6I8cOrlMfIGyBv8fd2rkbx4RRUHdQX6DTrVFOXrIockNxGXKr0c-jcEe-5M2WILdBygDGePJypFO8_YwtrqJnogV668OY33G1He6RSFwcxflwP6F0uko3n5EotN-ERdCVDvFWXfwOu9p4iHPqL5FsAlvv1YxmcxjdK_othc6Y5zDWxZGTxOZIq4n-5a-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قبل از اینکه جایی برای کنکور پول بدی، تحقیق کن!
🔎
پشت پرده کنکور
⚠️
معرفی کلاهبردارهای کنکوری
🎓
ادعاهای «فروش صندلی»
📋
انتخاب رشته
🏫
اخبار تعطیلی مدارس
📚
بررسی مؤسسات و خدمات کنکوری معتبر
🔥
با پشت پرده کنکور؛ قبل از هر تصمیم،
👇
عضو شو: با خبر شو
https://t.me/+2RvDbHy9KPFmNTlk</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/alonews/148812" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148811">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a35031cf1.mp4?token=cQaBlMyjOJi5O22AjkDSwb2E0SVKusf4jAfAQp7zWqFIKHpEWFTcQgs96dZV78oHM9M1ao-nOJ2Hc0J0isQ7yRr9Dloh8gFDpZ64I-jUbKFu1fy1kN4QsqUZwKVeUoKnW_rIXK-xgy73Z5zZmMhefmziZUEgUEU12aaWLbeWT7QhuBgP5RX7BgLK_cHL297yV8vdIQgjFAA_23HFc8mqWCcXDrtmHYGqz4DvGe5BgtQb29vHUA4IVIRjI6EdT-l6Tn2ldr47B9EVIa2VXrmmf04xc5iiqMNzFVu4A-I5jtC_KqPUGgSfE2hcI-3421K_jp1PKBlcJ6poObjFNnBx1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a35031cf1.mp4?token=cQaBlMyjOJi5O22AjkDSwb2E0SVKusf4jAfAQp7zWqFIKHpEWFTcQgs96dZV78oHM9M1ao-nOJ2Hc0J0isQ7yRr9Dloh8gFDpZ64I-jUbKFu1fy1kN4QsqUZwKVeUoKnW_rIXK-xgy73Z5zZmMhefmziZUEgUEU12aaWLbeWT7QhuBgP5RX7BgLK_cHL297yV8vdIQgjFAA_23HFc8mqWCcXDrtmHYGqz4DvGe5BgtQb29vHUA4IVIRjI6EdT-l6Tn2ldr47B9EVIa2VXrmmf04xc5iiqMNzFVu4A-I5jtC_KqPUGgSfE2hcI-3421K_jp1PKBlcJ6poObjFNnBx1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به خبرنگاران: از اتاق خارج شوید
🔴
تاکائیچی،نخست‌وزیر ژاپن:
«مایلم موضوعات زیادی را با ترامپ در دستور کار قرار دهم. چرا از خبرنگاران نخواهیم اتاق را ترک کنند؟»
🔴
ترامپ: «خب، خودتان شنیدید که ایشان چه گفتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148811" target="_blank">📅 20:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148810">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6009e251.mp4?token=GVwFJRByMY7Vn0IZLPn2hRNwfaOaW2K2er2j9cr-RCBA3pUgEZiyJRrgtXPCO8VWIP3RaExzxeXKIhwi5TPsZ3jSPdU4GMfQe4zym2g_Tq4hrlGmjhIZIOB692tpQh5ocSRYJmHV83roXQEhMd8y4nGmAX3GOWB_4SmU2OEO-JPZBYUdKD79IHhx5_fwX7uHbfK7cMVAMr4ey1HP6W92SfGKyUUZpJklpJDsjM9pZYYIkTeAf6zc1h8FBebagk4hP3YVqAxdPe8nDzniUOI1nPjWMAPlUD9ni-BoVHovBuVTbh6ADb7NkhuV2DZ15kqESJDRqP6d3-1FxnTPRhZskg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6009e251.mp4?token=GVwFJRByMY7Vn0IZLPn2hRNwfaOaW2K2er2j9cr-RCBA3pUgEZiyJRrgtXPCO8VWIP3RaExzxeXKIhwi5TPsZ3jSPdU4GMfQe4zym2g_Tq4hrlGmjhIZIOB692tpQh5ocSRYJmHV83roXQEhMd8y4nGmAX3GOWB_4SmU2OEO-JPZBYUdKD79IHhx5_fwX7uHbfK7cMVAMr4ey1HP6W92SfGKyUUZpJklpJDsjM9pZYYIkTeAf6zc1h8FBebagk4hP3YVqAxdPe8nDzniUOI1nPjWMAPlUD9ni-BoVHovBuVTbh6ADb7NkhuV2DZ15kqESJDRqP6d3-1FxnTPRhZskg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اینستاگردی جولانی حین سخنرانی اردوغان در سازمان ملل متحد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/148810" target="_blank">📅 20:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148809">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
تمام پروازهای عمان به ایران و از ایران به عمان از فردا متوقف خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148809" target="_blank">📅 20:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148808">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0abebcd591.mp4?token=XKKq4P9BaKySNSNG5O2yXBOiKY1qWEbU6aAyvb_wSmeat3SiXYeHPBhTasEyxWA5maswoeNn8K3xG6ZaehnZ8hDBc4TRNbUEUluLhr8Sdmm-JOUXwXogMXu1ZYNbRhag4HMv6BoJRaWfeIdsnsPQbr0bhbV-xFPoDvElzK0wXagmHHi2A4z-YChOFkFbrGIkpnml360Ha82GRFRkOoZr-pHhc6cIxu6UeQ4dU-99YFgTwi7L71ztFwu8xrPmNlUyxQfvPJt_YUTOAp1Fr-UpqZeFfJ1QPwP4FRH9MPDh1z2u9DuZhe4kEkU6Es0t3WlNH5DEFYBDYDOT46XdtjlDtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0abebcd591.mp4?token=XKKq4P9BaKySNSNG5O2yXBOiKY1qWEbU6aAyvb_wSmeat3SiXYeHPBhTasEyxWA5maswoeNn8K3xG6ZaehnZ8hDBc4TRNbUEUluLhr8Sdmm-JOUXwXogMXu1ZYNbRhag4HMv6BoJRaWfeIdsnsPQbr0bhbV-xFPoDvElzK0wXagmHHi2A4z-YChOFkFbrGIkpnml360Ha82GRFRkOoZr-pHhc6cIxu6UeQ4dU-99YFgTwi7L71ztFwu8xrPmNlUyxQfvPJt_YUTOAp1Fr-UpqZeFfJ1QPwP4FRH9MPDh1z2u9DuZhe4kEkU6Es0t3WlNH5DEFYBDYDOT46XdtjlDtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: روابط بین ایالات متحده و بریتانیا گاهی اوقات فراز و نشیب داشته است
🔴
ترامپ: نه، من فکر می‌کنم که این روابط در حال بهبود است. به نظر من، این روابط اکنون بهتر از زمانی است که شما نخست‌وزیر قبلی را داشتید، به این شکل بگویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/148808" target="_blank">📅 20:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148807">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf1225327.mp4?token=fjQkrHJAdfU8LEX-wfZY6Stdwc-CrQsDauntuokanMo7KG0gb7JSfsB7WVKfwC-HaJyxhxluIyEdfxEaq3i2wcGpbXGo0mPJyPrCnpmP7NcPfBuwhs1Cgkyfyx00ebFmgMahCRD1TfMEoJCx6w0_VHy7eHWo53ERWeeP5rEbO1c6oOEcqZtgr7yQSy6cEntfHsRR6Y0r3scaOQ-zVti7V1b58mZAjc6x-8FDCEJ-D9mn_zr8DLJb6T9IiLJt1XWIque2TvjeWLH9EAHM3OGP0s3a1re4uLjenfnF95No1bNU2p6TYjuLNl3Me7PKVYmjPzCZsAy-ZreSEfk8VnrM4oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf1225327.mp4?token=fjQkrHJAdfU8LEX-wfZY6Stdwc-CrQsDauntuokanMo7KG0gb7JSfsB7WVKfwC-HaJyxhxluIyEdfxEaq3i2wcGpbXGo0mPJyPrCnpmP7NcPfBuwhs1Cgkyfyx00ebFmgMahCRD1TfMEoJCx6w0_VHy7eHWo53ERWeeP5rEbO1c6oOEcqZtgr7yQSy6cEntfHsRR6Y0r3scaOQ-zVti7V1b58mZAjc6x-8FDCEJ-D9mn_zr8DLJb6T9IiLJt1XWIque2TvjeWLH9EAHM3OGP0s3a1re4uLjenfnF95No1bNU2p6TYjuLNl3Me7PKVYmjPzCZsAy-ZreSEfk8VnrM4oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا شما از توافقی که به موجب آن جزایر چاگوس از بریتانیا به موریتیوس واگذار می‌شود، حمایت می‌کنید؟
🔴
ترامپ: من از آن حمایت نمی‌کنم. فکر می‌کنم این کار فاجعه‌بار است. فکر می‌کنم این کار پوچ و بی‌معنی است. این از نظر استراتژیک بسیار مهم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148807" target="_blank">📅 20:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148806">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8088a12a2.mp4?token=CADuterQnzpnh0AxIAMyJYNdqu0uZ2quSVAoV8MM2SmNz3tqTscZb_WXfjIRB4KbNZIVHrPF3oxi-_sleJJFxfDJpi1H7SjAefoZIzMPe-C0Vos3M9fHlcU8Fn1brC3AJYJRW8XLfg_oZYkdiFzvxaLL8yTs0blxz5jdg0G108v8GVpcR1WwOQ4_vgdwO74deow3Y94YJS8YYTh-DmiFPPzeqJJRjok6cYentUjT7E3svSOtjgiSGoObLXNv-KH5PsFGsDhBTh-iTgaDH6VLqXJjBOC6L-IiE1W32l2JUTkub98HKV6EJ_ksl5mMRVU4KBol15xpvCHh-MMxVzLD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8088a12a2.mp4?token=CADuterQnzpnh0AxIAMyJYNdqu0uZ2quSVAoV8MM2SmNz3tqTscZb_WXfjIRB4KbNZIVHrPF3oxi-_sleJJFxfDJpi1H7SjAefoZIzMPe-C0Vos3M9fHlcU8Fn1brC3AJYJRW8XLfg_oZYkdiFzvxaLL8yTs0blxz5jdg0G108v8GVpcR1WwOQ4_vgdwO74deow3Y94YJS8YYTh-DmiFPPzeqJJRjok6cYentUjT7E3svSOtjgiSGoObLXNv-KH5PsFGsDhBTh-iTgaDH6VLqXJjBOC6L-IiE1W32l2JUTkub98HKV6EJ_ksl5mMRVU4KBol15xpvCHh-MMxVzLD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: اوایل این ماه، بریتانیا تحریم‌هایی را علیه برخی از سازمان‌های مستقر در کرانه باختری اعمال کرد. نظر شما در مورد این اقدام چیست؟
🔴
ترامپ: من در مورد این اقدام اطلاعی ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148806" target="_blank">📅 20:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148805">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ : به نظر من، ما حق داریم اخبار جعلی را از بین ببریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148805" target="_blank">📅 20:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148804">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d689b673f.mp4?token=WOwIn8MUW1zGQtF6FVV32L07suANe4QgYKYsG9DscW1hxUMCV65bthOjDkVduOM7CAE9LH1Y22uLu3xGLFBMyVXc-3PhHQJnlwCP21085v2CQxiG5fl1kHDdlK1xbmYzTmz9YhVFP-rZuKkKG2eqYhEx2p7nEq3xf1r9e6-HYXC9KPwDCm4zCXd_W_4VbR6ySTMaB5Qv3Bul4WzAFFfqXKjp80bFqvd1hedJUHxq7AEiKMdLplqI42DdvFHtsS4l_JBVG7FaUiB5DNrePD0D4uS63AUKz0Rmo_wQ6qbXDTe93vTLKPugJ6xKePryo9wsxsEGo8iTgwBeLcBoBb6Iow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d689b673f.mp4?token=WOwIn8MUW1zGQtF6FVV32L07suANe4QgYKYsG9DscW1hxUMCV65bthOjDkVduOM7CAE9LH1Y22uLu3xGLFBMyVXc-3PhHQJnlwCP21085v2CQxiG5fl1kHDdlK1xbmYzTmz9YhVFP-rZuKkKG2eqYhEx2p7nEq3xf1r9e6-HYXC9KPwDCm4zCXd_W_4VbR6ySTMaB5Qv3Bul4WzAFFfqXKjp80bFqvd1hedJUHxq7AEiKMdLplqI42DdvFHtsS4l_JBVG7FaUiB5DNrePD0D4uS63AUKz0Rmo_wQ6qbXDTe93vTLKPugJ6xKePryo9wsxsEGo8iTgwBeLcBoBb6Iow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما نباید اجازه دهیم که آن‌ها به سلاح هسته‌ای دست پیدا کنند. و برای این کار، هزینه‌ای وجود دارد.
🔴
این کار باید توسط روسای جمهور دیگر، یا به طور صریح، کشورهای دیگر انجام می‌شد. برخی از کشورها می‌توانستند وارد عمل شوند، اما واقعاً تعداد کمی از کشورها بودند که می‌توانستند این کار را انجام دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148804" target="_blank">📅 20:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148803">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ خطاب به اندی برنهام: به نظر من، او نخست‌وزیر بسیار خوبی خواهد بود.
🔴
ما تا انتها از شما حمایت می‌کنیم، آقای نخست‌وزیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148803" target="_blank">📅 20:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148802">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری / ترامپ درباره ایران: «فکر می‌کنم توافقی حاصل خواهد شد.
🔴
آن‌ها حتی امروز هم با ما در حال گفت‌وگو بوده‌اند
🔴
بگذارید بگوییم که این رابطه در حال شکل‌گیری و پیشرفت است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/148802" target="_blank">📅 20:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148801">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
هم اکنون گزارش‌ها از شلیک موشک‌ها از جنوب ایران به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148801" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148800">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
هشدار امیر قطر درباره عبور منطقه از خطرناک‌ترین مراحل تاریخی
🔴
تمیم بن حمد آل ثانی، امیر قطر: منطقه ما هم‌اکنون در حال سپری کردن یکی از خطرناک‌ترین مراحل تاریخی خود است.
🔴
بحران‌های کنونی، حاصل سال‌ها تعلل، بی‌توجهی و تکیه بر راه‌حل‌های غیرواقع‌بینانه است.
🔴
تنها راهکار عملی و مؤثر برای حل اختلافات منطقه‌ای، توسل به گفت‌وگو و مذاکرات سازنده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148800" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148799">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
جِی‌دی ونس: رای‌دهندگان بیشتر بر مسائل محلی که اهمیت دارند تمرکز دارند، نه بر جنگ با ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148799" target="_blank">📅 20:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148798">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804458d4cb.mp4?token=QZoQYcr1I6V3k1niLNL-OKsqFNxh2v2n8lnOmu6m6NUwOitxZ-No9x-vWivsazT_kOWXj8nA1YbCVyFpMxMmqYExEbguYCIr2Wx0u1YQhv7Gi2V1JzxlOXaLGIQBUY91RlhtTMdOFxQxLUsuU-gWj0ZTehJC8t2vCpjJgcq8pEDrrE0UVQhWqhDJjyLja5vrLu04t62VDdrKU9dSgXodo5TwG6OKL2Nc-LbSyrqDfh-WucSFd6xUX07MgMdVjleoeOtTmmmICa5dZ8I1bvhEQSitWR9YrNXtau3tfbpgAVPgB_4MMqNbLJyNfvjzfaKrM0S6xKhvF6vdfvUqj42njQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804458d4cb.mp4?token=QZoQYcr1I6V3k1niLNL-OKsqFNxh2v2n8lnOmu6m6NUwOitxZ-No9x-vWivsazT_kOWXj8nA1YbCVyFpMxMmqYExEbguYCIr2Wx0u1YQhv7Gi2V1JzxlOXaLGIQBUY91RlhtTMdOFxQxLUsuU-gWj0ZTehJC8t2vCpjJgcq8pEDrrE0UVQhWqhDJjyLja5vrLu04t62VDdrKU9dSgXodo5TwG6OKL2Nc-LbSyrqDfh-WucSFd6xUX07MgMdVjleoeOtTmmmICa5dZ8I1bvhEQSitWR9YrNXtau3tfbpgAVPgB_4MMqNbLJyNfvjzfaKrM0S6xKhvF6vdfvUqj42njQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
رأی‌دهندگان بیشتر روی «مسائل محلی و موضوعاتی که مستقیماً برایشان اهمیت دارد» تمرکز دارند، نه جنگ با ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148798" target="_blank">📅 20:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148797">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362dd98739.mp4?token=vx1lXJbDO3SByrFwKf_w1lX96yJndG6kpNkirVCnjh69KziUk7T5lrRyz008IZjR6dVibglLGvSfWyF_-2mypN9v9myViULcAQ0QE24kpEJDcYx_HGHYhr9ka7pQtGQkYGojB9NocU6JijO8HRgUvATDZx-12MJ3bum_fSVdRjmedIFTakzQ6NOqkqubk-C1pYw83skh7nRWyZLaX4vccsC4eu06C2_wpq-OM5aqQK99j2LTQ-unwk_TFrch83RTPyfDcnRnb4XQGA_PXdWJmIxNAjAP2bjAwKlv86pMSCxZZ6cd7v9LqTvpiwxmalhjG_AquHHUzVKmJof-_IugZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362dd98739.mp4?token=vx1lXJbDO3SByrFwKf_w1lX96yJndG6kpNkirVCnjh69KziUk7T5lrRyz008IZjR6dVibglLGvSfWyF_-2mypN9v9myViULcAQ0QE24kpEJDcYx_HGHYhr9ka7pQtGQkYGojB9NocU6JijO8HRgUvATDZx-12MJ3bum_fSVdRjmedIFTakzQ6NOqkqubk-C1pYw83skh7nRWyZLaX4vccsC4eu06C2_wpq-OM5aqQK99j2LTQ-unwk_TFrch83RTPyfDcnRnb4XQGA_PXdWJmIxNAjAP2bjAwKlv86pMSCxZZ6cd7v9LqTvpiwxmalhjG_AquHHUzVKmJof-_IugZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
توی یادداشت‌هام نوشته شده که باید به سؤال‌های خبرنگارهای سی‌ان‌ان و پولیتیکو جواب بدم.
🔴
کسی از سی‌ان‌ان یا پولیتیکو اینجاست؟
🔴
نه؟ خب، باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148797" target="_blank">📅 20:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148796">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb233d3023.mp4?token=KsDh6hK8zRF08QLNNbpnobwOpQ5Jiwvxps8WoxiRe38ujU4he7FUIMD-V5sV1TBkR5Ng3DoGi8xeuYPeyhoS-mwUssIv89ZHyYu3GOd-bZbo-zarVE_nifbZ2QUCZvdi-OX_8aBlYRf_Ot7f07I7qUXRZUbKp9LKQbGzptQXoKhy1cC18Jm3Wc7MTqv5Abw_XAxz42Q57BRgQwBuVWwyXaTPldOs8Q1jTc8slu_NZVWlGmo0nkMGGPUW9oI3_bJS9lRtTwMJ6y5CHeXIeCY1d4EZ8WYXJKVxrlnl6QMb7evuhCjcTyyBimfzsTZJSaU4jK4Q_0-pvWs2ZBcHIdckGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb233d3023.mp4?token=KsDh6hK8zRF08QLNNbpnobwOpQ5Jiwvxps8WoxiRe38ujU4he7FUIMD-V5sV1TBkR5Ng3DoGi8xeuYPeyhoS-mwUssIv89ZHyYu3GOd-bZbo-zarVE_nifbZ2QUCZvdi-OX_8aBlYRf_Ot7f07I7qUXRZUbKp9LKQbGzptQXoKhy1cC18Jm3Wc7MTqv5Abw_XAxz42Q57BRgQwBuVWwyXaTPldOs8Q1jTc8slu_NZVWlGmo0nkMGGPUW9oI3_bJS9lRtTwMJ6y5CHeXIeCY1d4EZ8WYXJKVxrlnl6QMb7evuhCjcTyyBimfzsTZJSaU4jK4Q_0-pvWs2ZBcHIdckGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توافق ترامپ با دانمارک و گرینلند
‏
🔴
آمریکا و دانمارک توافق‌نامه‌ای بدون تاریخ انقضا درباره گرینلند امضا کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148796" target="_blank">📅 20:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148795">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مارک روبیو وزیر امور خارجه آمریکا: تا این لحظه هیچ دیداری با مقامات ایرانی برنامه‌ریزی نشده است، اما این وضعیت ممکن است تغییر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148795" target="_blank">📅 20:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148794">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترکیه همه پروازها به ایران و از ایران را تا مارس ۲۰۲۷ لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148794" target="_blank">📅 19:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148793">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
آکسیوس: تا ساعاتی دیگر جلسه ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148793" target="_blank">📅 19:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148792">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe6c4280f.mp4?token=iJo0e7dV7Eir-qCf-PqL409uGpe2lIYMrzGNhMkHhO7JJqxdV4hGJ_1nitQV2dWWd3plhwJpDt9yX-cHFmBzpKsaOktQp-G7bMfHNWsnu-Rw2f8yzScT1GZRSWQR7ClMTWkFNSKg2niumUYYl1n2kECyBx1jC-6KmkP-4Zczd-zZjSR8z4mBcMB7Akij73kZgqJyEPBrmbVKQxRBzvlb00w6fVYCdviwxjgrIuCs_1ZcVptTMY-93CT34UAU6iXR3rDimAimAzKaCvwEZk7-DUKWQv_gOU2fG44qdh1DAHt4HCbgCfl2FAnZcyh0rSiGRqDRGJW_EVTtCZAvSZDwXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe6c4280f.mp4?token=iJo0e7dV7Eir-qCf-PqL409uGpe2lIYMrzGNhMkHhO7JJqxdV4hGJ_1nitQV2dWWd3plhwJpDt9yX-cHFmBzpKsaOktQp-G7bMfHNWsnu-Rw2f8yzScT1GZRSWQR7ClMTWkFNSKg2niumUYYl1n2kECyBx1jC-6KmkP-4Zczd-zZjSR8z4mBcMB7Akij73kZgqJyEPBrmbVKQxRBzvlb00w6fVYCdviwxjgrIuCs_1ZcVptTMY-93CT34UAU6iXR3rDimAimAzKaCvwEZk7-DUKWQv_gOU2fG44qdh1DAHt4HCbgCfl2FAnZcyh0rSiGRqDRGJW_EVTtCZAvSZDwXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیئت اسرائیلی در جریان سخنرانی اردوغان، رئیس‌جمهور ترکیه در مجمع عمومی سازمان ملل، سالن را ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148792" target="_blank">📅 19:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148791">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlPkFLzCPbh8Yl3tr0ncWqfxaIL8fFSJKBv-ENethQW7WCeIhsLQREklIZqKD6L0qg-mbCp2K2J0Mc2HrCTPsdktbf86_W_geF5kO2shOr6MkXWZsVSR5stTqXZHBQdpL9TerUgQF3exVi0Th1TH82UF3Lc_HSZALTaXZ2hcVMFKmpHmobiT_w-skuumcKLHAqlGFVk6gbwTQp7tVeDa6Ba3oYiXK71331oQImZd2voRnGqCozrwQmmn_JuWUNYogbg9Ovt9Fzb-E8ileDzkNJ6cMC9RnHuAMsHVZ5sYetWxCLeiosJPg7jD93oMJ3zowhPhSMiK0vzPquJ0-oK4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عراقچی و کایا کالاس مسئول سیاست خارجی اتحادیه اروپا در حاشیه هشتاد و‌یکمین نشست مجمع عمومی سازمان ملل متحد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148791" target="_blank">📅 19:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148790">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/imN9Wu4nKmTHN93ZCo71UBadCN2Y_ohrdnJp3DbgEo2KuNrSzmoWI78m2NSqGHxMRmQaHQVYysK-7qQVbyuurJI_fcnja4BZQO5bafGhRjtKNyexiuP3fOePX8z7NQUdfJdGz7EZZ5o5abkeIHouenP-mj4VoJLlU1yHRi96o8tecURA0QFMKKQioX_h0vzBN5Ie_-IefMj_0j1_zg_-GD5E7_gW1zNmippezKUqDXzbh0cxC4hUoFHepRUpYuohaNW4-336WUq1izbPnMtSevNbYWeEkBZsC0CRXCyoO5sr_G21sCw1thtd_OpAwR8Bj3_xg_r2LDUWt2AVu3HSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی هم برای دیدار با نمایندگان کشورهای حاضر در نشست سازمان ملل وارد نیویورک شد.
🔴
در یه اتفاق عجیب، ترامپ، نتانیاهو، پزشکیان و رضا پهلوی همزمان توی نیویورک هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/148790" target="_blank">📅 19:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148789">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
عربستان، مصر، پاکستان و ترکیه:
تفاهم‌نامه اسلام‌آباد، تنها مسیر دستیابی به صلح پایدار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148789" target="_blank">📅 19:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148788">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgwgMysO-lGgtFtoUrxRMR_4h0-pAnBmeIvXdm0kNQ5ZcBe0VPRGDUNWUb5IduEZgXOEufbFHQE9MAgjH5BxPfxI-l9NmFD2hOT_lSe01KrSxic7418sWfQ5C3qBnQ7HQOQatEY19qdp4qZmem3JpD-iHRheitCyiePTsmQAkdhwyvoZLeCWS07sQP3ExsWaRNUoiw_K137D9oVMagnd3ZEjcuo68zd6E-ZCZEWSSQci9VRzVJ3CxKagSqkxVwFfFG8KQ-dzEc-QD-bTFyoA5t--q64v-4eMHTkDfm8eAPNII8_T0abMK3l2Qo63hrQfT4OM6h-SpJ3yBIxUUrQjgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در حین سخنرانی ترامپ، هیئت ایرانی سالن را ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148788" target="_blank">📅 19:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148787">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر خارجه سوئیس پس از دیدار با عراقچی: آماده تسهیل راه‌حل دیپلماتیک هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148787" target="_blank">📅 19:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148786">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12949eaa58.mp4?token=mxfy3vDAle1UL2FUyAgQ_2HnMWBAEo1FYAqE4irKrN7UpsVs3HCrZoPAQmvaSNfn-c1IiU_-9scSuPqwJOeSbtUx6qZ9ACL9mUcC-WrdYuR0tkxNIk9MRIVjuyA3di9dFqHvWsePAy40eQA-8uHjGOcyN8j3c7WkFmaTn-xuHrVk8LmHOBtxU1Mx9SlfOrXyCr2_BEPemoYtziNP5378EHwuE2sg3GDQfP10em9iBeBVSwWCDc1GBMwkcgX2Eb9kQRRD0mvnrQDI2wJQpDdxcMystSlxBXLdxIH-bCvJAEUq-1m6_kI-xez7XaPnyTYEE_Kyd5kPju4JEo2Iqt-n8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12949eaa58.mp4?token=mxfy3vDAle1UL2FUyAgQ_2HnMWBAEo1FYAqE4irKrN7UpsVs3HCrZoPAQmvaSNfn-c1IiU_-9scSuPqwJOeSbtUx6qZ9ACL9mUcC-WrdYuR0tkxNIk9MRIVjuyA3di9dFqHvWsePAy40eQA-8uHjGOcyN8j3c7WkFmaTn-xuHrVk8LmHOBtxU1Mx9SlfOrXyCr2_BEPemoYtziNP5378EHwuE2sg3GDQfP10em9iBeBVSwWCDc1GBMwkcgX2Eb9kQRRD0mvnrQDI2wJQpDdxcMystSlxBXLdxIH-bCvJAEUq-1m6_kI-xez7XaPnyTYEE_Kyd5kPju4JEo2Iqt-n8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جمعیت ایرانیان برای رد شدن از مرز زمینی رازی.
🔴
شهرستان خوی- مرز زمینی بین ایران - ترکیه. میرن اونجا شهر "وان" فرودگاه داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/148786" target="_blank">📅 19:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148785">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b140f553.mp4?token=uiRm6pYKb58qHjcxPGV7EnvY60dGm2F1qWHo-SZqkj8NGDm85kmLbB_hkSn8U-BeD2ZMvdpHsJy6kdYoHADvyqfxFT91MFQ_OIk7HhxOXhlM0AlwM144GAYHOsipDpjsLWsyhAmXNzvYlnq0-ceVu3ggbuddHjwzOu2OKPrmabJnCphwPug2ZwESfMpT1UOAJX22Ub53z8Zfio5P9KCGpYlsgRLMeWRvho4mracYoGHCQd9B7EBRrpvHIkePW_KzQRlsHzp8pSmMIzAf_zSjrRh2TwgovkfVgigRZuZ3okgLZTPIvow2C0nBlE78Ccf3l7ZcQM3Qk_Nqv7KzfZqTIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b140f553.mp4?token=uiRm6pYKb58qHjcxPGV7EnvY60dGm2F1qWHo-SZqkj8NGDm85kmLbB_hkSn8U-BeD2ZMvdpHsJy6kdYoHADvyqfxFT91MFQ_OIk7HhxOXhlM0AlwM144GAYHOsipDpjsLWsyhAmXNzvYlnq0-ceVu3ggbuddHjwzOu2OKPrmabJnCphwPug2ZwESfMpT1UOAJX22Ub53z8Zfio5P9KCGpYlsgRLMeWRvho4mracYoGHCQd9B7EBRrpvHIkePW_KzQRlsHzp8pSmMIzAf_zSjrRh2TwgovkfVgigRZuZ3okgLZTPIvow2C0nBlE78Ccf3l7ZcQM3Qk_Nqv7KzfZqTIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏
ترامپ در پایان سخنرانی‌اش در مجمع عمومی سازمان ملل:
🔴
با همکاری یکدیگر، آینده‌ای برای مردم جهان خواهیم ساخت که از همیشه روشن‌تر، امیدوارکننده‌تر و باشکوه‌تر باشد.
🔴
خداوند ملت‌های جهان و آمریکا را حفظ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/148785" target="_blank">📅 19:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148784">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423b258014.mp4?token=UbJXzznJc0u4kUWe705Xlk-4w0XZuIJ6Z7GD6GOCtGAb556RqoXTA2HPrY1Ix8_8lzojZ_OMC3pY-7uT2KvylKkkornyoB7eDxcsqXzWJG1iuVICsUxUMHM6lb4IrUx5V1_TB_SrN6ANba6vJ0m_mYstGid_x2j6sKlnJzlGKxy6mOlA7a2z1i-Hl57CGKIjp-RidlozLIq59JzXI7CXR9RueG8fwe3yUutcTzWVojEgZ_Os7n3dpppxxtkMGifsemBver5Zcx4n-WYfzevltumgQIEeG0g0NiScbZj-KJoR6nO0cfnBpaQkntUNWUU_mqJV5sLmLzHPhoB0d-6NnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423b258014.mp4?token=UbJXzznJc0u4kUWe705Xlk-4w0XZuIJ6Z7GD6GOCtGAb556RqoXTA2HPrY1Ix8_8lzojZ_OMC3pY-7uT2KvylKkkornyoB7eDxcsqXzWJG1iuVICsUxUMHM6lb4IrUx5V1_TB_SrN6ANba6vJ0m_mYstGid_x2j6sKlnJzlGKxy6mOlA7a2z1i-Hl57CGKIjp-RidlozLIq59JzXI7CXR9RueG8fwe3yUutcTzWVojEgZ_Os7n3dpppxxtkMGifsemBver5Zcx4n-WYfzevltumgQIEeG0g0NiScbZj-KJoR6nO0cfnBpaQkntUNWUU_mqJV5sLmLzHPhoB0d-6NnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۲۵ سال بعد از ۱۱ سپتامبر یکی از فرماندهان میدانی القائده اتو کشیده، سوار بر کادیلاک و با گارد حفاظتی وارد نیویورک شد. زندگی همین قدر می‌تونه عجیب باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/148784" target="_blank">📅 19:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148783">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏
👈
ساعاتی پیش 12 فروند جنگنده f16 آمریکایی به همراه 3 هواپیمای سوخت رسان از آلمان به سمت خاورمیانه حرکت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/148783" target="_blank">📅 18:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148782">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: حکومت کوبا سقوط خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148782" target="_blank">📅 18:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148781">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏
👈
ترامپ:
زنمم تو سالنه، کوشی خانم؟ کجایی؟ اون فوق العادست عالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/148781" target="_blank">📅 18:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148780">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=HisO0OhqTQ-gAlASIslOVoeqJnno_P5yDNNSoVfhVGbEbCMVYJ9JBuWImP4WAI7p1P0fFFkQX_keNWkIyYn7Um9JX7kONEJCorqe3ptqwt0SYhm_sdh7zKEn1K05JNW_c5-0TlskG9cYF3NMxghaQbidkr3BYsXjMZI6NSSV7FqkwGU5F4KlNgMTvyuT0G5YLmPMD3qYaX-iTqyo7eVi2rrIpJVyl8n7st1Xz6294LNtZxE1_Vjim-G6-1RO9YCg8-dy2OjEvPGTBRZsaKujJOrhvxVNK5rC5HITIDxX_GYMhK8JOpGypt7f-Hn1vnNzhbgx3cVzoWdS6UrA2Qy8_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=HisO0OhqTQ-gAlASIslOVoeqJnno_P5yDNNSoVfhVGbEbCMVYJ9JBuWImP4WAI7p1P0fFFkQX_keNWkIyYn7Um9JX7kONEJCorqe3ptqwt0SYhm_sdh7zKEn1K05JNW_c5-0TlskG9cYF3NMxghaQbidkr3BYsXjMZI6NSSV7FqkwGU5F4KlNgMTvyuT0G5YLmPMD3qYaX-iTqyo7eVi2rrIpJVyl8n7st1Xz6294LNtZxE1_Vjim-G6-1RO9YCg8-dy2OjEvPGTBRZsaKujJOrhvxVNK5rC5HITIDxX_GYMhK8JOpGypt7f-Hn1vnNzhbgx3cVzoWdS6UrA2Qy8_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
🔴
دونالد ترامپ درباره ایران گفت: «آمریکا و ایران قطعاً این مسئله را حل خواهند کرد؛ به هر طریقی که باشد، این کار انجام خواهد شد.»
🔴
او افزود: «این اتفاق سریع رخ خواهد داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/148780" target="_blank">📅 18:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148779">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee7ed8073.mp4?token=h9vL7o4BDJ3_b0l5DkaxhGIdxB3hffL1yZSyecQ6rPjgYbEwY82M_8sAMatKZWgx216dbS_nMNNNlULTMDYCF8mZ66Xgky-HHFuoXAodGmVxJEhhX5BHUG70med-8-THne5QCjc7KUIo7CoLKzo3M7jyYEgkGc88flBpCjjsR_oAvwzUKPadheFNVS-7NQcJTrhe6LhNyIFvIS18S2WCtWoK7NqeyNkvtXHgmqR_JZgkzciKEt482w2K0cvDGsERIIkYcOSH1xLtdqS4JQx_6P3B5BZb7kBcP24bFe6vTIFfxMnyrAL1oIL2eYsOl-4ApzUuKAUVMymnfcwq7gDmKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee7ed8073.mp4?token=h9vL7o4BDJ3_b0l5DkaxhGIdxB3hffL1yZSyecQ6rPjgYbEwY82M_8sAMatKZWgx216dbS_nMNNNlULTMDYCF8mZ66Xgky-HHFuoXAodGmVxJEhhX5BHUG70med-8-THne5QCjc7KUIo7CoLKzo3M7jyYEgkGc88flBpCjjsR_oAvwzUKPadheFNVS-7NQcJTrhe6LhNyIFvIS18S2WCtWoK7NqeyNkvtXHgmqR_JZgkzciKEt482w2K0cvDGsERIIkYcOSH1xLtdqS4JQx_6P3B5BZb7kBcP24bFe6vTIFfxMnyrAL1oIL2eYsOl-4ApzUuKAUVMymnfcwq7gDmKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: جنگ اوکراین زودتر از آنچه مردم تصور می‌کنند پایان خواهد یافت
🔴
دونالد ترامپ درباره جنگ اوکراین گفت: «ما همکاری بسیار نزدیکی با رهبران روسیه و اوکراین داریم و این مسئله را حل خواهیم کرد.»
🔴
او افزود: «فکر می‌کنم این اتفاق سریع‌تر از آنچه مردم تصور می‌کنند رخ خواهد داد؛ آن‌ها دیگر از این جنگ خسته شده‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148779" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148778">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ: بزدلان و خائنان دوست دارند بگویند ایالات متحده با کمبود مهمات مواجه است، اما چنین چیزی درست نیست.
🔴
ما بیش از آن مقدار مهماتی داریم که حتی بتوانیم تصور کنیم ممکن است از آن استفاده کنیم و در حال تولید مهمات با سطوحی هستیم که هرگز پیش از این تجربه نکرده‌ایم. ما ذخایر خود را سریع‌تر از هر زمان دیگری افزایش می‌دهیم؛ مهمات و تجهیزات درجه‌یک.
🔴
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. در حال حاضر ۱۸ کارخانه توسط بزرگ‌ترین شرکت‌های صنایع دفاعی جهان در حال ساخت است؛ ۱۸ کارخانه در دست احداث است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/148778" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148777">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: جمهوری اسلامی تروریست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/148777" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148776">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=aZblgDWILJyHybee_eGaCMiW0F0UsplJJr6zx38OUIT0PRWwslD6b-u6GRGUJd-z3GLRiPdGy-Dqcy-XGjZ_t_Y-oqd-FIE2XLuGVeok_CHoYFxKppXlPoRJMI1G7A1pI8X0Usy0NcHzlASXs5ngNUVtO47czG80bhX5zfCRfrYHj2_mQrtY4mNBQYjm_Id7dfJZ90LgZeK9i3Zmb4SwmktEWF-OYkUCKpdWMXPoaVImZWIE6qNBllg8kyXW7EhJ0dLyLNKpMI2WO9a8g6naadN8iVeOysCfM3stAg9MycNn0cpSdjdlJb0lxzOHfwzi-DoMlA7GdOIEoFBjNjOXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=aZblgDWILJyHybee_eGaCMiW0F0UsplJJr6zx38OUIT0PRWwslD6b-u6GRGUJd-z3GLRiPdGy-Dqcy-XGjZ_t_Y-oqd-FIE2XLuGVeok_CHoYFxKppXlPoRJMI1G7A1pI8X0Usy0NcHzlASXs5ngNUVtO47czG80bhX5zfCRfrYHj2_mQrtY4mNBQYjm_Id7dfJZ90LgZeK9i3Zmb4SwmktEWF-OYkUCKpdWMXPoaVImZWIE6qNBllg8kyXW7EhJ0dLyLNKpMI2WO9a8g6naadN8iVeOysCfM3stAg9MycNn0cpSdjdlJb0lxzOHfwzi-DoMlA7GdOIEoFBjNjOXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: انتخابات هیچ تأثیری بر تصمیم من درباره ایران ندارد
🔴
دونالد ترامپ درباره ایران گفت: «برای انتخابات، در ارتباط با ایران، مطلقاً هیچ اهمیتی قائل نشده‌ام و نخواهم شد؛ حتی به ذهنم هم خطور نمی‌کند.»
🔴
او افزود: «تنها چیزی که برای من اهمیت دارد این است که ایران هرگز سلاح هسته‌ای نخواهد داشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/148776" target="_blank">📅 18:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148775">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: رهبر ایران(اسبق) کشتار زن و بچه یهودیان در ۷اکتبر را تبریک گفته بود او تروریست بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/148775" target="_blank">📅 18:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148774">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: من از تمام کشور های جهان میخواهم که به جنگ اقتصادی تمام عیار آمریکا علیه ایران بپیوندند تا زمانی که ایران برنامه هسته ای خود و حمایت از شبه نظامیان را کنار بگذارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/148774" target="_blank">📅 18:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148773">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63e99476e.mp4?token=q8-R3vQVaPdWihNSFVEAUqj8W7L-otVgG2Y331i9I0jI2pz-tf_vu_FvsbTy4yW98cxqIs4yary6Egc3itHvFEteZkJrQXTsdJEPTaAc5WHOAvM_Ou6CB6J0GAvi8NZZ_JNnxlAevLoqfvMRkreIDN50-nmwhPYxaorGELAGJihek3-BIEQYccwXDvtwfWyF75Y8GDn7jFhJRVdtNVsp-df0BCrt2gwy1zpv37NLrrJ5w-UeH--ZccCDeTZFoo4tRnSp9tPpGL-N4yRGLM__GDz5SR0muzPF-8nxvD5FYfTTo7CWUNPnF7-PYlIEYf5A-HLqGkdRSIWlXzddMbM6sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63e99476e.mp4?token=q8-R3vQVaPdWihNSFVEAUqj8W7L-otVgG2Y331i9I0jI2pz-tf_vu_FvsbTy4yW98cxqIs4yary6Egc3itHvFEteZkJrQXTsdJEPTaAc5WHOAvM_Ou6CB6J0GAvi8NZZ_JNnxlAevLoqfvMRkreIDN50-nmwhPYxaorGELAGJihek3-BIEQYccwXDvtwfWyF75Y8GDn7jFhJRVdtNVsp-df0BCrt2gwy1zpv37NLrrJ5w-UeH--ZccCDeTZFoo4tRnSp9tPpGL-N4yRGLM__GDz5SR0muzPF-8nxvD5FYfTTo7CWUNPnF7-PYlIEYf5A-HLqGkdRSIWlXzddMbM6sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران ۷۲هزار شهروند معترض بی گناه خود را به قتل رسانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/148773" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148772">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
🔴
فوری/ترامپ در سازمان ملل:
با تصمیمی بزرگ در مورد ایران روبه‌رو هستم؛ توافق یا نابودی کامل
🔴
آیا به توافقی دست یابیم که به این کشور اجازه دهد به ملتی بسیار بزرگ‌تر تبدیل شود، یا اینکه آن را به‌طور کامل نابود کنم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/148772" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148770">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: جمهوری اسلامی معترضان را میکُشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/148770" target="_blank">📅 18:12 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
