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
<img src="https://cdn4.telesco.pe/file/LFjUXjGtxS8fkyn-rrH9VkjAP-S19_DuHEw8tHEDJbh7p4yC3jfK-27DGJGhyCqBi-j7NRcGuDwzsC7C6Lc8F27AmEnSVmVY58xr8h0-ntG9ySfbOVzQBs8K2yiCAvmBrelOxE5NIV8_Wx7ImrHaSabhHe_XmrArfJbhR6LlBtgiwoJC92RoXMxwkkdts_LVGtZrthUaqH2C2YthOV6InPCnmKrGqFsaEG09asYI0lfaWzfJ3kgmuEM1E2-iE3X-YniK66P7hBH0_4BYFNZ52LwhQP8BJOHdbsPvVcX7DN4Sb9XHvrTevALv9rh9A5m-YYX_4S8-oXj66du_sjeDjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 202K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 03:18:50</div>
<hr>

<div class="tg-post" id="msg-80932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">چرا قبل مهاجرت کسی نگفت که خارجی ها چیزی به نام تعارف ندارن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/funhiphop/80932" target="_blank">📅 02:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تا اینجارو هم نبستن هرچی گیف از ژنرال ساخته شده بفرستید
ما تو این جام 3 تا زدیم و 3 تا خوردیم و من تو کل گل‌ها آروم بودم؛ حالا سرمربی آرژانتین همین کار رو می‌کنه و واسش کلی کلیپ می‌سازن، پس چرا واسه من نمی‌سازید.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/funhiphop/80931" target="_blank">📅 02:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جنوب
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/80929" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">برنامه عادل فوتبال ۳۶۰ بخاطر انتقاد از تنها دو تیم شکست نخورده جام تیم ملی ایران بسته شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/funhiphop/80928" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شیراز و اصفهانو زدن
انفجار در شیراز خیلی شدید بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/funhiphop/80927" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خبرنگار فاکس: احتمال اینکه آمریکا دوباره وارد یه جنگ تمام‌عیار تو خاورمیانه بشه داره بیشتر می‌شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/funhiphop/80926" target="_blank">📅 00:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یادش بخیر پزشکیان میگفت پایتختو تغییر بدیم و ببریمش تو جنوب به یه استانی که نزدیک به دریا باشه
خواستم بگم سلام دکتر مسعود پزشکیان، برو دست اونی که باعث شد از این تصمیمت منصرف شی رو ببوس وگرنه الان بگا رفتن تمام امورات اداری مملکتم مینداختن گردن این تصمیم تو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80925" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80924">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امشب خیلی بد داره میزنه</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80924" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آمریکا بدبخت فکر کرده مثل همیشه با آدمیزاد طرفه
سخنگوی ارتش: اگه آمریکا بخشی‌از خاک ما رو تصرف کنه، ما خاک خودمونو موشک باران میکنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80923" target="_blank">📅 00:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سنتکام: همون همیشگی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80922" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80921">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قاطی "همون همیشگی" امشب
یه همون همیشگی دیگه هم هست
و اون "اطرافِ نیروگاه هسته ای بوشهره" که دوباره زدنش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80921" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یه سری منابع نسبتا معتبر عربی خبری کار کردن مربوط به اینکه ایران میخواد یا خودش یا به پشتیبانی یکی از گروه های نیابتیش به کویت حمله زمینی بکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/80920" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آلبوم راکستار از گوچی فلیم و اشکان کاگان ریلیز شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/80919" target="_blank">📅 23:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سنتکام: همون همیشگی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80918" target="_blank">📅 23:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80917">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBWM6j3D8NrvQbC5rWJ7C8VFqAqltm8lKiWRNUMkM4n3q0ozw9M62T0jwcMsuuuGjuK1YQapa6xYXrc7ZYupOgGg9oGDwmFYgmfN-Ngotwu6nZfNUU0qgTuXuHacHIfPZoMQnl5aE9zCksyHoQSbGa9biuSVpXkpMcJxzCZz5f3CHSYBoDKCJfBLwlDxl7PPjN5ZFrVCMXaiR2wkgrLb9R8O29d_GXRid404quRyzVMvFwS2NvFXuT2ztRplfRpvEa_x8JZhUBpsBi3QP7GOez-pnyHPNMHfwvU7dr1mvY_zVjgtB4Cy4zCYBznqvwH5OipIdCyWEaRUKEqA0cRpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور آرات حسینی تو جام جهانی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80917" target="_blank">📅 23:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSd8JGnj5lZQ4HHfK5eUN13ejgKk1tO37YTq9HB3yzdjCTHo__-HErCm4HMKZkSiD_NAmrDgw2YpC23pF5FkYIKENMr6T8ZbryY0bry0UBEtZHJQhsqcKydVMoC_9_bu8OFviU9Gl1WD4B8xmfme2bPwepmUJ6kUHINv2rrro4VrTbNVqi6_yoiOLDoyDYFPW7vYHKlmrEJXqmsymhsc8QBhs9X9sP7KYf0XCE89ykslpJgQIe3XJexamuy2c4KRIOy5eORRtmdPNX59ssdAfEDZ5TQSY7kPyi7SsZhEnxE0Ai2LN6vLDm5YUzRJuukoXy64rjZYLJPBb8ThvHryiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
با نایت موویز بدون نیاز به تهیه اشتراک، فیلم و سریال مورد علاقتو تماشا یا دانلود کن!
🎥
توی ربات نایت موویز هم میتونی جستجو کنی، هم تماشا و هم دانلود، تازه مینی‌اپ هم داره که اگه به فضای سایتی علاقه داری میتونی از اون هم استفاده کنی همشم رایگانه :)
🍿
@NightMoviezBot
🍿
@NightMoviezBot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80916" target="_blank">📅 23:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Onv4DWzpEqz5UIYbh3wWqZcN4AYpfoVPHUCmwgO60Qgn8h6fMAdXshlSCYb2kwYFJ4SBv4nFyx-GO0gs-PdxKxfa_uk6kXo0j9dAoZW2-PBqVA_Ye1ylRq9_eeWvgfu8u23LsjrzxEYjUB9yD_J28OMoYWc6RuDD9k4K8KR9_LPaG7KumWC4zBamxnZM1_QMpEx_idICTo33NkgbvBVJr0zdqta9xUkNneWu4_a_fM7wqfPFDr-H_64PIwm4MMHlRTUb0P5PqIh5ZwpoVTBMT9D0eQY_QvGwchhret7iQGcQKOMkIKUJSxp6XGu9v1LvSq8SEiaT01s0tUE0xuAUEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنری که یامال گرفته دستش
شب هفتم سال :
پارادس
🆚️
گاوی
(این به یک رویداد خاص اشاره داره که در اسپانیا برگزار میشه و شامل مبارزات بوکس نمایشیه)
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80915" target="_blank">📅 22:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNslTQdxNFS28vn5o009F7LQeHuRP5caURrJi4N_BtSwgdfibpFnCeydmbazYyt4HALy8PHmxR50v05W8PgTq66pGLPgO1U3Z24RkBl_biV1ySAJUSuaZ52gUm0JKf75stjsCv68NNx6FSJye9AWTlBZ57IpR_wApxVvUcrADw9gw-nPc9BwUpX8kdKq6HKCnMjsjgCtHINx7mBLNETuLvVdPT3SN_rsO15Y7O75pZ_B7GgWNc2Szvc2jfzOjWQfslc3ppg8baMpMXBZUzCdpp87CYxHm4PHqyAQq9Jd5ZBvRpU8jGII8CJaWttVjV-v8_L3cOVuctB7inTdOv74sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید پروردگار و برترین اسطوره تاریخ فوتبال:
شکست دردناک بود و زخم‌ها دیر خوب می‌شوند، اما با تمام وجودمان نتیجه را عوض کردیم. حمایت هموطنان و تلاش تیم باعث شد دوباره جزو بهترین‌های جهان باشیم. امروز قدر کارمان را بدانیم؛ این تیم دو بار پشت‌سرهم به فینال جام جهانی رسید. از ته دل از تک‌تک تبریک‌ها و پیام‌ها متشکرم. توانستیم مثل یک کشور متحد باشیم و افتخار آرژانتینی بودن را با هم تقسیم کنیم. همین‌طور به اسپانیا بابت قهرمانی در تورنمنت تبریک می‌گویم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80914" target="_blank">📅 21:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جام جهانی 2030 با 64 تیم برگزار خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80913" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یچی میگم به اروم ترین حالت ممکن بخندید
یک مقام  در سپاه‌ پاسداران:
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80912" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80910" target="_blank">📅 20:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80909">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbbd065f52.mp4?token=kYIaqNJC_k0SfcOxWZyrZAjCjm41dNKiLijV2bZauGZ2oblypf0CyWXXpVuoIjhkCXhF9efpZmp9AAQUi4Ga-596fXRgQw3jEDGRaQEePcBF7rKX9LWu_cmBpoNE1chGS8jjXq4leRauA_-VO59aMlmVNW2g2SjbbN1P-jsUJdVDI_WrEFPXvIHNPInFh-hXORYUf-y9cfPRziloB_Bs3rtobukcgU5LrmW7ofO0DddU9626zkIABAn4eX3chg7l5K_JOC9eHAqz0tMIpTJOY6mgYG29_7BkvPdDFS2jKiyiYFOei1fd8j0oS9_ZdnfoBwtgnbD-qUtZ3QZwDZW13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbbd065f52.mp4?token=kYIaqNJC_k0SfcOxWZyrZAjCjm41dNKiLijV2bZauGZ2oblypf0CyWXXpVuoIjhkCXhF9efpZmp9AAQUi4Ga-596fXRgQw3jEDGRaQEePcBF7rKX9LWu_cmBpoNE1chGS8jjXq4leRauA_-VO59aMlmVNW2g2SjbbN1P-jsUJdVDI_WrEFPXvIHNPInFh-hXORYUf-y9cfPRziloB_Bs3rtobukcgU5LrmW7ofO0DddU9626zkIABAn4eX3chg7l5K_JOC9eHAqz0tMIpTJOY6mgYG29_7BkvPdDFS2jKiyiYFOei1fd8j0oS9_ZdnfoBwtgnbD-qUtZ3QZwDZW13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیوت خر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80909" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بچه ها جی جی آهنگ داد
دیدم سولو موزیک میده باباشم نمیفهمه خواستم دلش نشکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80908" target="_blank">📅 20:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80907">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پائولو مالدینی و گواردیولا در بارسلون باهمدیگه دیدار داشتند
فدراسیون فوتبال ایتالیا میخواد تمام تلاشش رو بکنه تا پپ گواردیولا سرمربی تیم ملی ایتالیا شه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80907" target="_blank">📅 19:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80906">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxCovgB0rynwMV7z_XukpFqg8lmtmsYlNVz00SNsRMi8XN4awMXVvMzvfPtSHRQRgq0DO5z9HULl9nC6uJv1XRjl6OlPXbEu1uipAHKMNm2O7jHLbIK6H4lUfoN0qN8p0IKuMo3j98Vd0_91vBgQPAEXXiPWwH6AZPDlggX9Yb5l_oncTwEuLw-QhHrJZ8xkGKYVt40tTlQrv04AsP8RqQENYjozTysrEJT0_1hRM_syuHf_-nQuVt6BOsKRUbdnDgq5T9pBLshAFG59kML8cxjtEIJdYLWoUJSH282KKKbJG7Vkpu13SPY3Y_DGdAmVCbCQ1H8-DoYPmBY-wtWLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب راموس تو زمین بود یکی از بین راموس و پارادس زنده بیرون نمیرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80906" target="_blank">📅 19:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80905">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m59FwFxWCTRokOosRxLdFcpnxLnC0nBeOg4CwXqVXqniC0RWWp-78QtsI09u8vcr3RYIpQN5FwpoN0R9TC94lJ33GrmkLp96NmFdnEEjokQ2LRy3942vs_SGRCOixZFQ-0uCsD3ml_S_5fSSD08gveHs-sM9PzDSXIJipyMWFqNgErrror0fRgnb5IqpBOSgJQAcOI55inlrgBGzNh8d3HVOKwesRkKG986F5m7tiFJMR_JV46YS_PPPxLAaN3k5ydjCpvR0sw3nANrsnQmU18jWxygcJvUNYxlqGQEk13ndcUaRlnphiKD7JVduZyYP3tT-VC0dzEv3nYa9jMmUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب اسلام هم به خطر افتاد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80905" target="_blank">📅 18:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80902">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حقیقتا انتخاب بهترین از تیمی مثل اسپانیا که روی تاکتیک مشخصی بازی میکنه و هر بازیکن وظیفه خودشو داره اشتباه ترین کار ممکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80902" target="_blank">📅 18:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80901">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftu-ZTPxDNVWIh93tbK-yb_oEjugBEXAoK9aqlFxfgWVTu6Qini-scAQ6rGfPBFtJ8TAwcGFUibtnwuXZrw4mBa9CqZRkpXHGXJ4E0smm-w8S-zh-FKNNh3hUVG829te44-TIgZOTsxgg35HAa1M0oQ5Klea1SVNNe4-ZGDSjyowb7V66xkcRmc3fAOtIZHD9Hv1ePwod3COUVs6SBcqvZOUfQQZAOZv77nw9cRy75mktdqPncTcezcwhUn1ZA07IjyAZziiVz3S-vvZU3c6YFgx7kL8iSlpsp3PwyEHHUsLUUwFrtBJjKeXPuPQa5IsY-nwVHj2kcAkIb1lHOaGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید عمو بیژن در کنار یکی از طرفداراش  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80901" target="_blank">📅 17:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80900">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4kQxkrCfk1F0cz-x5O1Z1hfHKJP49GzsBg_YR6dd_eS4SuK8dIGFEINQD6yxyKSbiOeZo1n6Pka6-7zKRmfUA4p-kqPg60AI5oyw6fH66_TNCPpX2UPUWw7k9HvK_LHjJ249CFJwynRM1_abhiNus3fJKDx1lbEaMbyDXua6Kr6GmwQoHVnjuLwUpUAUi7m-wPVmXdo8G1chvL6d_MaQ_e8-BKS3SXKVXbY26rbKLvWs1Fx5yUlXBzAdIxQcHKbmnBumtL71zhLDV9GpbPpX2kVftNP8Duql0Or7w8pQjsh5OKfhjKflujxLvxwoZVHZaTbls0ETRBQBuAKAr3d_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا: یکی از قربانیان حمله موشکی ایران به پایگاه در اردن، ایزابلا گونزالس ۱۹ ساله، اهل تگزاس بود
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80900" target="_blank">📅 17:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80899">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtGSUSK_Bzb2j-H8Bs6X3bCjUypGaxaLDilZMjJc6KA-9IGXHLseNl53RDD__cOrUnvpPBG_zE-QQANm3mW9tOXBTo779GZf_krnHvvnLe7h400euj5vGgR0kRHT1d1VhsX4jVr2031cHB9MHPg0mCN3CAyP54nAbZPGtk3EG8a3qjCkAsv-7i6SDOGapmg65FZpHO1jrAQ4tJiEeeEe3n7BhVDHqYR6W3C9bbvQ_gnzqY9bvxShzRkOAfBGk8nQ1AD91dc_MkMDQv3rv12OvtXfyuR6FQTVTpjOtYVrgP2xETK782yUjBY2lTbfZQfsIYpgmUDkRbOSgo0EkGJLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اسپورتینگ لیسبون
🇪🇺
-
🇫🇷
استراسبورگ
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۲:۴۵
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپورتینگ در ۸ بازی اخیر خود شکست نخورده است.
✅
استراسبورگ در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اسپورتینگ ۳.۱ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما بماند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r29
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80899" target="_blank">📅 17:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80898">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgQeSH8MqUuSQPfYDsTJvCOX-ZMSK5bBc0wNYt1m--AVibkkMBtkZ83z-Hh3eNeYV7TL8UcKHto8CpsLmsYOTMVYEjAJJpeFAhOVzHcbRbBUxHOsq9341WSt-BrkNjCSKJePG6MQRb_Q21VeBukdzEIPd3Q0hIWlnZ7ac4rNQ4LA06xJJQWvTZrw7YB6u3fm3CTuwPYKCgB6YNXg9jhoVKCyYcY45YQuqriHfojRBTwjm5bNh0hLqV5CM0Zq-Lg0YNNV6-Qb9qUkBTHN16TzNrkqgPvK5IgYkJl1NFplbNqVDhocCWox-milUOizaJ1TqU24T0SQj2mNaf5STDJlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام دلو هم زنده اس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80898" target="_blank">📅 17:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80897">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhW7ft9zSUIYUq3MHtQwqm3UYOQNgYw0ENhZ-cRW1-vjI9gBcBx4Eh1h1lpBscs3NLT50huAKGDkDGNuM75tAtlksx5Sfp2aZkZnVcJ5xFERgSoL2pKg1Kf41GuHn5xnqPow-sumnebL867TAVo04MaDtmbdzGysD9YU1aAVXJHpmMd92FQ093Slqf-9eYLjljVHF5hnHSmhxcn52bnjVh8fa62V0igHcGp7YobSMF0ZNsbKGcqn2jJbUnqt7v8mfEZLu_lWk73zjA_eSxJlgARFRmsauo7z4cXN9rOyX5cFpXM1HNONvr7OT3A-sEJZqszq2vHaeuXx1Cq1z1h47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک های مسی برای رهبر شهید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80897" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80896">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0RN_rz7pu4QuWu3p1_K7Li2lxJ9eYwlrH5OqGtQa3UX9afuNFq1K4eQslypcLlm64C41Z9dNQZGBPgSeGONKG8kaWZNOH7gtn_nGMUyU35nqXCO1WHrflRPy-UY1dE6v0sFk0C0KT-j23lQtDVDiWI3kocVOMMqBUWeP-vO28xnsGHcI0-vncg_0DWPIkHY_tIkFQ0WHostUqUFFXwElIAVXIoCrEjJvb9FsyxJ7vNClzljfFJDsdpcn8m2q2wcI3s4eER1uTED7GtHtUH-XtbW8nQ4xt5XJGOTarOHdi2yGeAKE47WVCwaWjVSa4RxKEotyzyMnPqsQVXH0chw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه :
نقشه دانش آموزان برای تعویق شکست خورد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80896" target="_blank">📅 16:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arTgiMrd3ig3jXzTMltebUl7aWLy-Z5xuIwrZd48qrEoOjUl4eZVlojlAemzh0UXnXqXj4oHKXoA8JO4aX3g0LSdeH17KLn9vzNBZyjXV7R5wMlks6C6GDAmsr2vvM8WOIZrY9ttVJDOLn1Jkxoph7cp4aAic3rdiW2Emcsm-jB1B0wI2JQnm1nUMeFTdJPZPEU8rYIjKQBeJJaVbbxSm8CoGciv1S9FO5lWe3TCA13kkfGKnWzFVEopVyyfRni1qCEci9K_qCHwPaO__AgK88QDAs6UyfOCyVmNARIvDeCx2MwIxC0B_fKBZ0mKt78OwKz_SY1ObvL8L-6AVaW2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpeIoukAenjbhO3EqXywgMmp65ktJGA8kSoZmqLWFNUZJ68CrO-D_G4FDPu488-NECN9jPSCdxt1bxenH0Spzq9J-GqQEnMb81r5wY0w2uYjrKTv1OyKIXVL0rth6mfW_a-hasD8jdQdhw9VzEmNJNXZuaY7Fspu73axWg8gcdSsOFNLAi-TGidMJdpTdsKm5_sFzFN7NrlVnPjm7qtEGq1UbFaK0FTPcfnpgHsNdbdniPc78knBEYU7yLGtdr8XmQU6b19BG6XbqPkxgqblss3zLHHSXfKBQLhnjZTVv3BRvc7gfeN_Pbk2jrta2sixevaEKoxmZYOhECLNnuvJFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دکی و صدف در حال عشق و حال با پولای ویناک.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80894" target="_blank">📅 16:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80893">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHU32VYQGK79HIhGwUahiQMypSm-JT-FYaM2C67e2vSY2hOh_IvSeT3_aX9KpYm4_2MqpCKFzdaHOSaKKNN0qJThzOv8PdIi3XlEproqQJ4FjNLtivJpIgF-ztcM8nuwyvQlTFmI4zS9Asy5Mokdja84wQNHLCzBXak_RE14bTnWkVsCXeH0wJ4iXEP0pIfYf74HVEGNptPU8TDb00qF4SqMTsIoehZVPcKrAOMmD2274N0cXZYWVFBf5eiSZPjm8Hbgh_MQIrBDzoVa5CGp1OwYrA9ZigMthZ8URfpHcIDCP6IuGF7qbjG6YafBiWNg84FBiUn0gWd-wWK52QBpDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی دیگر برای جبهه مقاومت، حوثی های یمن محاصره دریایی علیه خاندان کثیف و نجس آل سعود رو شروع کردند، به امید آزادی هر چه سریعتر عربستان از دامان خاندان کثیف آل سعود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80893" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یکی رو گوشی این رپرا کیبورد فارسی نصب کنه تا گوشیو نکردم تو کونشون نچسبارو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80892" target="_blank">📅 15:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80891">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پیروزی دیگر برای جبهه مقاومت، حوثی های یمن محاصره دریایی علیه خاندان کثیف و نجس آل سعود رو شروع کردند، به امید آزادی هر چه سریعتر عربستان از دامان خاندان کثیف آل سعود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80891" target="_blank">📅 15:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80890">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_d5UrS3G2_qj27QD_T_37haVNuI3A3lyhhIq7mkF13mda9vfVEwmb4nKDHpLQ8Jptf3jeWpEzZrO2EZfI9_DXVrm14cvUs5T_t8srBvFvAawNhfeZopHar97UIJGyUgXSt8fHlP_t1-Lm8T5DdXaldsO7Mbm75zKHdLsA2KWy0c7p2AtWA1tHWrpQ7_5Fv9dcBqY-qVB0UJgUD034n92F3aD5EkoxM80s327P-SldnnWFX_kMa6qN8IWO1eYxekvao7_gn3yQGMKc-cnhV6IjBpvRRmE7Vw8-xWIHYW1CD4gD5KVC4-SqM35OIJNgh1EFPKUNx0BVus64upxSaThg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسیجی جان بر کف فران تورس، گل پیروزی جبهه مقاومت را به تیم کفر و استکبار زد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80890" target="_blank">📅 15:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80889">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaH-chSWxTIj80vfbscZ0XZyJjqjeaQ-0enb4Qv2_-6fXDxh_r3wX1USlzMruyvhUI-rQyXRFJPNP-Bw4JFIBmShGvj6bqSXyFcmKIEqN7fw0MVrPC-96nHJhNMcBvT0b8jz8y97TbvJEwESgS_Slof8OZcM74C4-iTg2jU5C09c_4a6TlrAVBkYb09TdWYM_9_pqURZ_WgtzMK_kTfxaBQc3yBon-eNB7f--t7yMiYEI8f-uIe69LcTyypnzgnO7zXyWZ8KN8XpXYYM1BpVLVwnic4qrXgIu5nq2TU2vrM0jJPBNZWQ1_MkKndPwiveBv4_rCLbK263VxMpWq0OUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسیجی جان بر کف فران تورس، گل پیروزی جبهه مقاومت را به تیم کفر و استکبار زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80889" target="_blank">📅 15:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80888">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rplo6zwwTf7HHiCvnPpIvjhJusV4kNZt9V6mVbWOWztd54oz-V29HTnnwO1YGY_BcTCtnFmYanRVR-CAc0mJvLgp9UjIVniwakt8A-n-xg-PnVtGbx0khEeDVvB0-qhzYjhi_CntHgM_7Y86XZEM431PriCWrOnjM2-fNDICHxcQ027jaOIE6F0LMRWjqA3jl4D84B4wyZVWifU8PzI4Fh_6XKwMR_YdQApSEVQMANvJR04OVHpAWTzqhey03i2nACXrKOT6lnERz9Bxfq6npaPdFdzAYS1A_I1y8CkukrJTXy9umYb_LJRsXVIc0mnd-AkIQ01ZgXqLuWhlfOyLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین همینجا بازیو باخت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80888" target="_blank">📅 15:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80887">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد پس</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80887" target="_blank">📅 14:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80885">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اصلا وایب خوبی نداشت امسال</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80885" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80884">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آقا من هنوز سیر نشدم، از اول برگذار کنید جام جهانی رو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80884" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80883">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N53EgiBQraGuh4dOAgIJnoqKkOKTX20F98evSAVb3mQTGHI5bnG2PIz6QShMr8SvKJ_2w79bgs-dF-PcurmytCcq1TeCKUYH2OLPFA26deGu7-pYtubERSUUdQ-L3QVLZ5tqgj5qUsvhnlcS6PlZqio2E5tSt35_bNMV8f6dmyMLJ4hyPkxZX7jbooDPb8BghIWKziQiKhV5nVDEnhGbOSr0AVxECB7IwUFeiAW25l-3tvwk9sKjFw0K1LG12cv72Jt5PtE5UyjSD-5bO-wbz2ehEsi2WQ1yG4mv9UTM9yfXD0TfkyWPCvEzP-Z87HvpYNpCH9zwMJU82Bx57geL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فواید رابطه با اسب.
#بخوانیم_و_بدانیم
#اطلاعات_عمومی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80883" target="_blank">📅 14:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عه ۲۰۰ کا شدیم</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80880" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ei7F8GGOKrYtaqoVU0vtGN1-opwzZnKcVCsoREZGr89OFIQy3DhEW_K5tGHSJMltPmTUpmufOBuKrAKLLqJOGFsYYOvU5gYCPwrL9IcagLwB1ZlKlhRq4uDMT3xxNOl2JkjFB08LwGveHmZDnokvUFeV5fsrBFao0WoRdOBoJnX9VcqHwru_jTPm-vmFgo00Uk9gqZc5QWAUA2MeFOOdPZIg7nwQqO3fhmmgXhIg6mJmnucLSHnSDeA2obABoUcsWKKytI-Cxu7Ijj7ClY4aj8VOloP__WMCUyndicD1UdxRSgXWhtkydUS1jffklo76dFE8s46qFVy6zmaWQ9JSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش یامال باحال ترین اتفاق این جام جهانی بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80879" target="_blank">📅 13:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80878">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسرائیل هیوم: نتانیاهو امروز بعد از ظهر جلسه‌ای اضطراری با هیئت وزیران امنیتی خود درباره ایران برگزار خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80878" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80876">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NUGXGCZyRHRqmGa2zZ-g2CsOiR3vB6DFrRevaUwGnMMV3u5gkc6IFc4i1LMBUR-U6usDqN9597-J-V9TnVHEGB30FqRQNNlPrmgnEZKFxNWDH-kYcLWFFqTWnmP2v813ZJ4PTvSzzEaDsYmRfgT4crWcHOd3I7AdogOfxAtERuZ6Z1VaSXkquoMabsYeUCOjASY45GGJrGwpl5ngOZSi2ZZIMlt_4D68U9PsP3eXaI6R1SrXQI2AoLdEgTztbtCUhorBBPz3xEqu-Elb-lrwM-l4m_n45bTCiXAKwNcQA5AWEORkDyJIuHKBUXASL3L8uaYgfzg8R2aZTBwcLxCssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i09wwmrH9q0-csQctoyL7pbAjqCLnonXdeXhjQByMFYnW7VztKSiKHiUMp9bEZwI6yWltUtcLsd-s4g4felaehd_AOrn5t_yA0n7s2V4Q3-MZ9rKXWHKwdi7G9mUVhKuv0quZmb2MdkmNtTbPJvkJwghO8cvMGBXT-XKW5vvCmth3BQVKwE2617lG97_yKVMczcogKox7bDWtIqZLTUVA8QErRS6fUfn4P0yvA4fNko_K-VoJnltl696qLsYmS8w4K4LBinp64OpvoC013WPoP963rusrgC1s3rRCfEO1HnG754zgoYg1-p9VrYap1HLJaUqrkZCUJj2S0VUyRillQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آقا اجازه؟ امروز میخواستید امتحان بگیرید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80876" target="_blank">📅 13:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80875">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdYYt20FeaAmnUbcAFOBmuIbOCCS3-_pHGjV7kMNEV8BZQkE0S7dNYdS4ZcXfNI38IX2gZZE4uGX2VM-3Ll77xNq4vqymhViFpbu7jqoLX7S4oivhMBYi3Q3lLu-TVxIbGaeaPCqU6Xe6k3tJ_atj2wXMv8ZtJrwGDlz8Zc1oNbys95MP0Rdjz2Z38Zo9EwwfojMIHXarChwDhnmQ8SuUwWTIXDHTeSQBtuzRJzWogAElxgjzuygs-KtQkM9pohAB7nr5oQFnjyohnydyYJOhCetJcimqp3hws3NP1cxpGYIlcOXPL3cB05tOIOso0qGJ0UVn6JAus-vibpyeDmfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا اجازه؟ این دستشو گذاشت جلو دهنش به ما فحش داد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80875" target="_blank">📅 13:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDiLc3f_H-p8LpoJcSED9b8aWuougDcq60J80ng9C28kz6_0XDPgHgEHNSU7Zx3FOR8GnzAGgSqy3URGI5ZNf5Q_HIIBMqhROqNTRFRztZcII0-oke6E93Cd6WDdk9iEW3oPze6lonPjbhBYJYpkSzV7B4xS7pxyPEgLLmre9ea1t556WOyYY4pWwF8RgdeTFjpSr5L3UcwqfpiNOuy63KpXpAD_YUuIwX253TjytR20vIYFj26_Fr4-qccZJpo0h0OJ0X0DVcnT_VACLQ_G4wZ4Rs5aqWyygJ41Gy0c7y01PdzuSiYVWb3ndOeGAD4Xr6AkTwiuB4SYG-tb9Xeajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چشم های یامال احساس تنفر به ترامپ کودک کش را فریاد میزنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80874" target="_blank">📅 12:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Woi43lGZPTicqbBI8_f2LaHitBT7kH3-TEHMLE7PMoE70ZT7-cJrI-edsSO4UyUdRbOULPuFy3EdYgg4Me3zdaf1xMf0iEWRgYKulXNuKJfSPcM5CBrGqeH4Uvbqmua66n8Kk9LEqvDJZi2y3xh_xlNTji4FQAqWhMr7g0byxU9EfqxFd9RkGpqFVB6tu2cZqOSJ46Qe-H6Q0J6n_zW8W1SIgdiJe-076WrrDPEGYZ8DrHh4j4oDpx5nIX7TkHG8-E29Mjv2tBJYGbo-qNHKmfkHfCcY7N7SCDyporktI6XMN4brC6i0LItKN2f5LXA-g_YhmrqH7JtnNyaCdrYLdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک پزشکیان به اسپانیا بابت قهرمانی و افتخار آفرینی برای جبهه مقاومت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80873" target="_blank">📅 12:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">صدا هایی که شرق تهران میشنوید مربوط به خنثی سازی بمبه خوشحال نشید، امتحاناتون کنسل نمیشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80872" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf4UaRwIispU2vzrLXgcpztWM9N6BoyZSnYbhlApqsdVUB1YZSPFND4niNG283QpKBKwa2w-u5kMdZjQenlGPZ-2OidADVKsf9stmG9juW43-OrCT4DioSLmNWyppKxkUnBgIFSWFIbifG1GNzTBzwz8bs8DGKksPPwldw0gx-CI-HDEp7uk0HbVKDmge08L9eIZGgQ3so8IciZRE8jSaaDw62AnHQOonSjAPJxKme-xaPK67b_8O-itM5vya8qz4dcBAHRKGPk8KRRpDsF-cvnYI0YQwN2vrCGGNsIxRUfJP9eYcy38_g-Gem5uj__FOdH_1_3Rqn_zFP-Rdmj3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید عمو بیژن در کنار یکی از طرفداراش
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80871" target="_blank">📅 11:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80870">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az5GLdDfS8H4277cdbv5ILUf66fKudWK0COx2NgoIREad51fjr44TErvLKoFzBUz4cgEBtMKYCBW06UKLdVz5OOOYPz3inYeeN454JzEACEu2ubR8P4HuCf7dzBXb5nBg5pk2X1He--hXWLoazzXOV-DUNPkH9FzKtn56Rdm-Nf6tqjcQWxrwtXg8o3kMuTWrd1aanMlZekJYc_3Mer766SW_yzQL7-tmjK073pDfeyT6VUj-2dLgFAWMX431aqN1iKaR2947s2L3avcCfXUl-z2dw0x9mIHCXw7suoJyE4oQ2cBpO6JiYCbPFIV-Dq4LSYLlkX_wlfeDbirZQT92w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی این توپ طلا حق مسی یا امباپه بود کصکشا
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80870" target="_blank">📅 11:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80869">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsDWN9NHmiJG2879Lc-pVHWiORjQwLZ21dHaeC3nfMDlxu1qbyDtSh1WjwQxLXOt5PYmj8adkVyOvL-Qcld7prDm3JSopsO17cWbGltqhFUnQHWAc6VBMi7bzJmEhWZOQTtkFOTBwUEmHxLJz94JYHl1o6SA-mXmajlTkFRhaIKB1LMjUD4L9Z-8CS0cuTbv3exl_J4YvpmGcR_jP12POc0Ae1BOiXPJD775NOM_NlyI_sPn3jRsk2xidejxX7xZK0jcs9pykjwQYIjgLhatvdkBMywxI442u5l58fWF2FLPf-nWIOzUTpaXODr8twqrSvtEHxMj0CalDttzhu4rNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اسپورتینگ لیسبون
🇪🇺
-
🇫🇷
استراسبورگ
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۲:۴۵
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپورتینگ در ۸ بازی اخیر خود شکست نخورده است.
✅
استراسبورگ در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اسپورتینگ ۳.۱ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما بماند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r29
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80869" target="_blank">📅 11:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80868">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffy3GrnbDlxqFa33DTwEZ7lyip67Njxjo2xhdPWL1GyW9k8UBJBS-lI8KIXC2ayoStaB9triTom_dnK1qI2VXw88E7vP08AqEtkoHjc__EJ5qjM6WNAVIM4TlNIBch1qufUOA6fWTAWO4MXBE-acaAsnCmVVUjge9L6UX30WZsltnTXpspTMnm07vDg2yP7sfVeZVu0hpMj1azv8MmLQiUMWWw2wfZu4rPoLtP-mRG9lryrS4VUBQzgJmcReVnqwzbKKBNOHRdsE05AhIE6lbyYvoVBkC--XT0KznWH0vtr7WsfMcFrViw5lfglnrJsHyI0nvGH4ewH2ePN79TIX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#خلیج_فارس
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80868" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80867">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVePdMRxYz7X2w_uJi7DtBKOxSYHaCVw31WtzPKhgvzPq1HxH1fId9RhBCRkUxooR91zD83N9w8xN1RqGJ792b7f5Z8YKBxL5ltGFXrzwsbz9ChtIoQq5IhfQMh71zd9fMKCtCRRdUvE02ueAn-7EoDlr_JAiGUaKWSKrY84NvzdLRgH-KhoTSHXGwTlIhLZ4ngeMQIQZdGb8fmf9PIB4yik19L0P_DOIZV_R0E2jvPLETCbvPTFaCXrtLov9dVcocJ7uRoZcx_mwnd6q80rSgUHFOgfNJ_hIV8nUE6DBNrzJlJ3zxQCK6V6VVvNBMNlvrMN-Au7_Mbk6fstfERvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس شوهرعمم بعد از ریدن به عکس های خونوادگی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80867" target="_blank">📅 10:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80866">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfMzcPMmyMvMIEPw2snZAISDXG35t1qaQa9NoMqMm4A4ko5bipTwoik5KV5HfEA2TY9LpM9D-5P7CwZfpNUL1iph4iCNOyl0oJ2OGGBwEm7pDCYgZxwpUbrVuQ7FcG5son74KADZZZU8D9yq8RjBBFYBl8hIcySc3oQov85hqvAu6dOHeS8UDgaeqlJwbF74P9pwmq1XrlOuyrbT7u4jvokNEanf3MELl3_AMHFIF8BzbkF3ptAmwxg3IcI_KjpocqL9PBKHjX2eEcMTUzbC2DGKyEzTfT9ly5otDxv06oclWxCWJ8I12rJxtDD47sapW7CQF5RaLJtT4N0bAd28nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۷ و ۱۸ دقیقه صبح تو کرمانشاه یه زلزله ۵.۷ ریشتری اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80866" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80865">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGU49Pihl_8Fd4atyQ-vkKpoQ4vZnXxaPoJRa4YWm6JSrMc3vLfNCQrjn4AqOlvdgq-UJiQAAFwk1jsPy_rlvm4vE3BUWIRbQnTCpcBabDQXXmOwrP50D6177UNv3rUW4KsuRHVhSbs7b747j44nJg6wpDGxu3u_wkNS1mL3u9-KKttbj5LICVyN0Z39zIuL4gOEo9CK2u_txCNIv622r1wMfqu-juR-WcNnTeib_NjgmNr5oESZj0GyFaVzckzl5wTjZjyuDId3tl1yij7Tb8WNfpH5KeVFTEMuI6e_RApFA481aCsH_i9vyvQAGy8sugRxxa4v7NBTSLquiPsxww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکی Dior از استایل ایرانیای دهه شصت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80865" target="_blank">📅 09:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgUyM8aG9TlT52-TcEzSF0PXCs2gZmTOwlGUedXdQQZtRecADticTwwpNRGZtqBxpkTxh4Trw-7MmOyZ6Wr31K9-Ec4_wCz0au063e250IIRP44In1j2AZyEqliCPZi2msGTW5x6C7P7dZkwzw_yAD1Jmi4zdDLNlEyeCxQPEDNRy0-cWNh-RamlLxgBF_4nCMbneu84if3zoAFVl3hT1HFhb4s_cd7L82UcjC12pptLgIwdtXOqh8VA6j5osgeegthq6hVqW8L0nIHVgh7vfYIK9swpY6MIIwV4uVX_MtwsITrPaDydOshuXD7hbKaH_h3CSfakZbKcgwLsnF2I1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام بار این سفر جذاب و فراموش نشدنی روی دوش تو بود
خسته نباشی مرد
🩵
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80861" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حالا که جام تموم شد، رونالدو جان تو کارتو کرده بودی، اون "i'm back" گفتنت برا چی بود آخه مرد مومن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80859" target="_blank">📅 02:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ آخر نزاشت تیم ملی اسپانیا یه عکس ملی بگیره تو همه عکسا هست کصکش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80858" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80857">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KiWR-Rb6qobj9MHNdLHdOiZ1ixb9sOXNVYLD0iCCW5cboRPd5wRcS53QWtQFX6SZR9AMC_c9Q_EmXlzfH5K89rqWE4X8c12qKIHMItqSzJiq1PeGoQYGoQvTjXlU4kSyzaWjB70IZpU8s1Cc0F6vT52wze_QSrRAkptRs-zo6fJvqwGRcYD8fFtI41GRH_CkW5873isRd4wHsDaBfX8DODDGKtK5pm_4JGDolyu7RPEWE27Sz87TSBg8235vEpCR4T6dz3BtGPiInNO1D6YGwHXlgyzhwnecS54TS4zzMbJteTR5T873EmIVeh3HJ52vfqciTCItpvQodHiBHuNTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر خوشگل و کون بچه بودنت به ایران 2 هفته دیگه مهلت میدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80857" target="_blank">📅 02:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80856">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">علی دایی اومد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80856" target="_blank">📅 02:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80855">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خب دیگه جام جهانی تموم شد ترامپ زنجنده حرکت کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80855" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80854">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بارسا بلد نیست سی ال بزنه چطوری جام جهانیو برد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80854" target="_blank">📅 02:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80853">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپو یکی‌ بکشه کنار
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80853" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80852">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn-LOZo503cMoRy5KXFe5TvmjCLUu_z5AbYShOr2vytUtVLyBksKodZu3ij452G-GJiYxynrvkLMeDTRTRmlU1lkO1PN_NM4KCDmHwyLQQiLXt8ey0emfA603cw5U4zAlsYzenwqS9K8jI2qJtDQLwVPWRLl_bIISOso3Wt2jjwejy0C66H8nFZ6U3t8ll28ujxQu7q9hdRDWYVgvnfUwWSqlPe9cZP1lhSU6IpUB_wITsPsFbuC1hIAfgGyodH-VeHG8_E2BGkZGzNsdvyX18iX2-lsmPmzKPFEf6euj3YuqbVcxrk7yfeUEUD7ffEh3dv9AEwhQUVLTNfJ2SDXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80852" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80851">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رودری هم به عنوان بهترین بازیکن جام انتخاب شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80851" target="_blank">📅 02:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اونای سیمون هم بهترین گلر جام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80850" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کوبارسی به عنوان بهترین بازیکن جوان تورنمت انتخاب شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80849" target="_blank">📅 02:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80848">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQBZMmZk8EKAeuZ-9zKvqxWcy4y0GnpQ2kkJx4Rrayggr_naVPCgUlqIMJdCwvojvhGey2hMZt6maAlXyCKLXsHQnwFOBFSINR6Juhn_E1lNpAlxdtifjHRhyO1OTlw5T5l2nl9UdUFqquMawyFbbTHcWvG45Zr9ibilOBpiP2Lsa7HbUqv7a05On3L35TjOOUBZOTrDOL6Yrq2FdK7lL4sxBlCE_5ZMnYE3aYqR79NRQJPZIm6u8VXxwD3cVgcc7fSaFWtJOV3Q36o9ruW6DnHfgWalZL6rUNDWg5B6CK72OmoaCIR2AXEBFgJsW82rxdUVSxG794Nn7Edp9R7Kfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخاری دیگر برای جبهه مقاومت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80848" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80847">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeQCOEGX2aXBfPPK-LnoHcCPdYgAMdR-cSg95WS1TOZhJHqBLJ5mFORrSFOolJAlkgvm8PbOn_Sz8wi4u3cNF6B1jXiICGbKdLOwgzx559KZ4i74d2JPVPLMLdLDA8kctkkiCwdrD1aBSxTq9KJ4jCoLbEPSZE7FFYeGd75vFFcaFpLrsjejolb2fzO18b7Bl34MWZU1QVRwSGaN8b8xlrXbr-RYpJDM_l4P2j2wNP71JaLFamx0r5SxkMqL8j8uoMnInjSwfwetpi_YHPSZvu9AAV_WJb0QUykTPLLhUlhNoS6SkjM1ly0UmLWdFcgTkhVIbZa0_-WFY5gvKF2qPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80847" target="_blank">📅 01:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80846">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه این پیام بماند به یادگار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80846" target="_blank">📅 01:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80843">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMdlIm-qFXD2jSdkDNF-whcBIOAwgNqzWJhEVL6AMSWGzcNEPv6jDCr1flPAIvJgO0uX9-5a_sSy_A7YAoSPRBhB4rUXSlBi1Q_5sYjI9GG1xLY6tKxsaP07evKI7o1Scv9qBiB2JhImaUS24IEd8H4jPrM2zZfeN1rKDsPmOEeVX9t5SKEXBbo_syrbgnz2CefZSsKO4lIkJjuHED5FvQtsXfW_o947Xxg-xc634BPVJmyFgqwOL9JhV8twroMuAQRqMBw0zCjUViXylDR9s8c8O0XU6JnbpHjzbCJShRhhdKmeZVoM6P_pzioLw_wXP0F5N6xVBpuJzfaMibTjFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MeB1FCOIwF9nHqZKZxUDL03AVgqkM6wZ7MJpDGdgZ7C1JjEnvIQp61jZJtqP9Jv2QV3P04sBz3HVg12tn3oMpWVCU6ptIKCQPfAgu7DF5w3ZRCtpcSbN7dmFxf6MshRyWXWozDLbYaPQuREj4yL6URM-uG0NBTP8u5OfQaZOC-U6nVjzqbrZfVEuHvyMg54KVzdjqdrKlzpR-W6hcTZkoEu9xmAF-idUYGeQ5hYr4mPoGRmxhH0k5L5XZp9t6E8l7bb9opW_DfWTrA87c-K1JnMclIbHHj4j_JUxXKyFmxDBqdONBRG19-KUlvttATtUIzeKkqD3oX4-ywUheQ2LkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پارادس چیکار گاوی بنده خدا داشت
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80843" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80842">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خب بارسا فنا حالا وقتشه خیلی سوسکی پرچم آرژانتینو بردارید بجاش اسپانیا بزارید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80842" target="_blank">📅 01:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80841">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسپانیا آورده میگه ببر، صد بار گفتم فقط مصر و کیپ ورد و سوییس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80841" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80840">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh8on9kJMbWDAYFKuPjQ9j3xLbVE7693rQI2uh6q1IQekyhra93ysNMfzQG-jQo0rl1wRC7Nmg6Zw0Mv2pKPvzGUZ08mkWWBSBuUHEMMpzN6Fuv-49gQelUACsjaGxmbAPqHrBP6vrPJprrmYfdh7GrjTlFEbGV4AB0b_sNn7EUonjlCT9gA_JIYMrsP8hcF8RK9MJQlxDB8pi0AEdS-UcnTe8BxZCZwET64lywk68hjBZqVGMQwMl2UDCEuB5nZYtzuskQMzWeOXW-xQOMKWfN4zJFiei5MJaiHn_AY7boJWtWqqs2zABrOp_W7ZMTB-ZWC_O4A4Mb7WsL3sIzmBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا اجازه؟
این دستشو گذاشت جلو دهنش به ما فحش داد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80840" target="_blank">📅 01:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80839">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دریک جان کیرم تو ناموست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80839" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80838">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">لامین یه جام جهانی
مسی یه جام جهانی
رونالدو : I'm back
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80838" target="_blank">📅 01:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80836">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFrITbHO7BAXq7asaObdLKI04NO9Uz4w6e2R6zs3VJWLantBKdHf1N6z8CYdBh4n4ymmePZ2QKoeogQP8HuZdlGl3KxoXfOmIYOwH11DNYtlC76jb3bGob3Rdk8DYZ-yIqpAEXsdPzhkA-z0-Cfr52IaGNXv5pK36LIExXMLzFgzsQepw5vMuxaLSjIyHiq1YqWCEMZT2nofkdsyjyhXvYGRwY8cmyQaLkIy22WSLwr5jD1DW6g2wS0-86VxO5Lgs8pbAUFRt7sq-jMdymXQFHBrYrU3oOVDYVvBkdYuX-zkOLGDUmZBvIqLa_9tj8SmAuzNwRxga-f8pYxvtIZyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غروب یک سلطنت همراه شد با طلوع یک سلطنت دیگه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80836" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80835">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37b90c753.mp4?token=i_CCUF-g2dJkGgWfVjtie3HR_-Ymy1Y51lXN-a8YSRerJSBFhNsteYJmrsoGhYqsJgBZj_nNIVabgk_MKNgPVE3PPcJlH5aSyPOAbxGZ6PwkRXXFV6heCBd1AqWIwzRsrdgYV-55ObZvooEnrlqSCLcA6FAudSkL0PVqLDYOLGUt7nzauVF2K44Fz90oV3YnPH53lhJiQ29j5estbOkZi9NfCc7IqZhXQeKu6hKIthSbbURqCz3__TXbeQSBGO3IhVaKW2aY-kB31WNgyck-kk1wLguy1l9fEWRI1qdcj8QIX_YV_882ZHB5AOBOPKuJ5is9-X1ag3NxMgUUxv0oVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37b90c753.mp4?token=i_CCUF-g2dJkGgWfVjtie3HR_-Ymy1Y51lXN-a8YSRerJSBFhNsteYJmrsoGhYqsJgBZj_nNIVabgk_MKNgPVE3PPcJlH5aSyPOAbxGZ6PwkRXXFV6heCBd1AqWIwzRsrdgYV-55ObZvooEnrlqSCLcA6FAudSkL0PVqLDYOLGUt7nzauVF2K44Fz90oV3YnPH53lhJiQ29j5estbOkZi9NfCc7IqZhXQeKu6hKIthSbbURqCz3__TXbeQSBGO3IhVaKW2aY-kB31WNgyck-kk1wLguy1l9fEWRI1qdcj8QIX_YV_882ZHB5AOBOPKuJ5is9-X1ag3NxMgUUxv0oVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80835" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80834">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGLiMllT8sXw2nDbi_4SRfNiV14f77iE6N-4AHd4esQ2mLtdz806U4pLOJQ99MR296DPMcq4CO4Mg6QgvnRkMkCeNH5Cwz8_hErQJSgJPUmTA2Y9KX0N2HnOjTltEGSKN7X9ln71W8V-AtpJQVvJlcZcsb-u4TEEWTC3Y1B5U12MLBGwCeN6ozcaWQ3lnXCtIhJQBmAFVvVj8Zm_-WXUJWt6WaqKaN8_UP1nsRIj8AV1VoaBxeY0W_U0NkvuUeSE6qIFcsgaQt61qjvkCbKKqvfz6YCtfmlKxZfEchiiowgqy4QZ9_yQ_o_z1G1gkEGLr3CjUSnlQmlw9hc7X7faZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی فنا شما بدتر از ایناشو گذروندید اشکال نداره این چیزا
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80834" target="_blank">📅 01:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80833">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWNo8TN-_USyC37b8sl23KC6lHpFnf1F8DqObqhGxiWr8jYmQ6LHUo47HdvQvuwMo8K89lQnsEBzihotb1FehBRSw7mHiECknpV1MryaO22gCZmge_XvSaZhneoMe_rQmeKHlX4mcGvqdTkV5cTpVmgXgdVqXCD-Wp9MD-J55eFDZH8-ETZjoCUfadF3D9_6JMWmKMtXKiNkMS2pDCQHHB-uB3ehW2sBxhnaikYwvt5qrxxNnr7iTes_9cJ2d_RoqvgwRTddIaRcnNAZLAnuP7Hy9-Ee0CTnXsokwEeUdJ14T-L3sU_RcGafnDJvLvhTEu4D7SK1bNSOZdL2B-fjhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عکس دیگه</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80833" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80832">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اون وسط یکی زد ناموس گاوی رو گایید</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80832" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80831">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ریدم گاویو کشت پارادس</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80831" target="_blank">📅 01:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80830">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRh3vvMKLBggvjlLOaITqDVuGlRcfL1YCa8e6ZLw_R4z3dq22-XqW-YxxqX7FG0wcIkEdWZulwx-k6uKQfuZaAc9otdIG1zxZxOAdnz2Op2-VdDsxmKzJBTovr4iXiEsCg72XvSD9kLkdj0MXt3KUUbG-w1EUedYiO9M6fURQ2wMQNXgv9PQehW2vEo9hREox6OySvSolmAAtWMTIP1yMEk4asa2o6T9m6tAjbmPaYi2Z4Y4aR8AQgf_n3C1ACgIY7JZHXyIEa8XnZjqoZIht4EG8iS57g2z-TcgUxMbMhQNu1FHPPoDFWZphbzbJYLULLqRfkxCbpE7lCBIW4LxsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80830" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80829">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">داداش یامال هم از باخت مسی ناراحته</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80829" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80828">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مسی چرا اینطوریه، وقتی میبرد گریه میکرد، الان باخته داره میخنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80828" target="_blank">📅 01:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80827">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسپانیا قهرمان شه پرتغال میره جدول شانس مجدد که انقد خوشحالن رونالدو فنا؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80827" target="_blank">📅 01:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80825">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80825" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80824">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80824" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80819">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907a6900e9.mp4?token=JKZm33wFwZytROIo9JH5W_lDck_E_QwjO9_PuQ-jUI8-zcnWEgqv_g69M7VgbUCNgp8fe9D5tIZXE-vXGvWA4QnZcdk9HqzmR2muG6T71bM8TUqXQVcOM_Yzi2mCMrfIieTc2svTQc3LblcHIZBRAtuUG-RVdYhugMup5ynaFknBQkjz2koW6mTsYI0tCzDgMsNvPMek0fzeDgZaJwpXbwW3OoKNsQ138c2RT5PaMQWZauxSGbOFro07E8CxKdI066NJ4YSuauQfRAIfaFQgRwYCwAYbVhXOojyBKmH5HXUBH3AG9EgqcUuCdgzgfebGGQk6IzMaRsYTzDkPPpQn4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907a6900e9.mp4?token=JKZm33wFwZytROIo9JH5W_lDck_E_QwjO9_PuQ-jUI8-zcnWEgqv_g69M7VgbUCNgp8fe9D5tIZXE-vXGvWA4QnZcdk9HqzmR2muG6T71bM8TUqXQVcOM_Yzi2mCMrfIieTc2svTQc3LblcHIZBRAtuUG-RVdYhugMup5ynaFknBQkjz2koW6mTsYI0tCzDgMsNvPMek0fzeDgZaJwpXbwW3OoKNsQ138c2RT5PaMQWZauxSGbOFro07E8CxKdI066NJ4YSuauQfRAIfaFQgRwYCwAYbVhXOojyBKmH5HXUBH3AG9EgqcUuCdgzgfebGGQk6IzMaRsYTzDkPPpQn4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80819" target="_blank">📅 01:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80815">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الان رونالدو فنا با مسی فنا رفیق میشن بر علیه یامال فنا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80815" target="_blank">📅 01:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80813">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لاپورتا تمدیدش کن</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80813" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80811">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80811" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80810">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بابا یسال گذشته از شروع بازی، چرا تموم نمیشه</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80810" target="_blank">📅 01:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80802">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hx2312fjPo6G9zw5EfulcsfozzzEY_vixAmjUC8nuAS7_-uyHPV9BsBZ3am0ERQjqw71D6sJcqCKdyJqBIXOrg7MrcsltOUpgrgmyhYWIr_Mtohulg60hzzQC024tKTIsi--qo7mR6NuzadSROH8D1mIXVgWTOknB0wyp-MHokmAiNQsLQfkMoRAdQZof43j2SV6gTiVVYhp7D4QwTiMY8iotn-znYsVyhDD7uhXNeKhViseKK91wYSdeZz1eKuuIuOfv1cOMhertmC9G_rUfwDcWpGEjdUVzAiM6_XQ1aoI4JAP9whRWbEv8Mmtz_DH6h2FL6HcAMA7zinIhQKtqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا حضرت سیمئونه و امام مورینیو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80802" target="_blank">📅 00:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80801">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این تاکتیک آرژانتین بود ک بازی بره وقت های اضافه
حالا باید ببینیم چه نقشه ای داشتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80801" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80800">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHWsPz510HTTa5pYEaETyIgBURQLoLz75UX1iWaXmLo_PPCn-Y5NHHonOr1pPRiGvDnbucb4F2uriVCz8XZFlCNJuq4B91UB7BvhB-5KDqG_RnCPqjQgjHDxFwA3iSQVnC2DHAdFJl0v8mhuWojITUeoTd5HPPUWpyOBf6vW4grwonf9MLj8ekqQul0KpnPzPpm9pdpUPmjko1cRPfJMhYv0ST1Hm-fy_X9AVtuhPKLZy6npiklN95JWamY0dQNjC9Mii3giv761qAHShbEvIUNeWV4HSxuW4VLrvxu_HJw6uXlxMuhAwDca7nIR8XedcnP3E7YLi_xUfDU1EVweCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش یه خطا ساده بود، نباید کارت میداد واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80800" target="_blank">📅 00:44 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
