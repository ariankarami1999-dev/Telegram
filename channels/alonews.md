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
<img src="https://cdn4.telesco.pe/file/Vtct5wxYmIQrzi7qus3NG2rIQnYQ-ge9PcgR1DTO9Q98lShMqILHygY7232Jo7oYwOEr3pab3uWTVwvFt83WSxNUvSIBNcJSnuYIwJQUuuYafXQkIGOXqjX2m1MbqF6UN5knUU1SIH32h9FoTJWD6cMa8cAx2l_DZxxRFb7Ye_2ZaAfacDKPCzTrm0w74Q6Eo7JtbzDvkztrAVYb5t96hjfFc1v-roHzPXx5gAUIdM468jBMgGDfL9a8mlFOymx5zJ29jj_2aSzZxiNtNgB7W7rUkXl1ZLV_Yv1vEbOHldEVdJ0KejZy1fzhnwVeiNQyWDqAUC-IFWwXFWvprPCS5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 20:56:09</div>
<hr>

<div class="tg-post" id="msg-141535">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
قانون‌گذاران دموکرات از پیت هگست، وزیر دفاع آمریکا، خواسته‌اند درباره کاهش گسترده نیرو و امکانات دفتر آزمایش تسلیحات پنتاگون توضیح دهد.
🔴
آنها همچنین خواستار بازگرداندن چند دهه ارزیابی غیرمحرمانه تسلیحات شده‌اند که از وب‌سایت عمومی حذف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/141535" target="_blank">📅 20:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141534">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزارت دفاع ترکیه: بر اساس «توافق مکه»، رزمایش‌های نظامی مشترکی را با عربستان و پاکستان برگزار خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/141534" target="_blank">📅 20:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141533">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThGlhu2uQK6Y7AAVvDIc0-tCmsm_GfYPPKIaLtt0FZO89y2YKVZwT0LBf2kpQtUf6kCJ1n_VBd_poOYdEakmXGYDfieOijy2FFRrq4igjvOxbibcXPatKeysdE7ZjXqG4rpE0-64ykH5f7z8odV0fBe2lGfx5k_-AgzM0GtEfNRit5rmk5Uh7-SM1MxLKyW0i2QLRgXr6byqcVTQb9TKZ05Abyi1R9C-qxbnP8tF_5O4EK0QAIJoebED0JgrHz9ikA1fy-GQ2j1Mwe-WtYhFHejvS4m-6jPHt_Y0QX5rRaGqezqWMIqLbuvlwQJWYyEFUph7PbBMkkuBU1_uLCrUMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عبدالرحمن منصور، شهردار منصوب طالبان برای شهر فیض آباد، پایتخت استان بدخشان، توسط جبهه مقاومت ملی ضد طالبان (NRF) در یک کمین بمب‌گذاری شده (IED) ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/141533" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
مارک کارنی، نخست‌وزیر کانادا، تأکید کرده است که حاضر به پذیرش یک توافق تجاری نامطلوب با آمریکا نیست.
🔴
هم‌زمان، مذاکره‌کنندگان کانادایی در واشنگتن در تلاش‌اند به توافقی برای کاهش تعرفه‌های آمریکا دست یابند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/141532" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141531">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZYQ5fAFvbzqmC1fd3f5QW8XpC-9nxVZDCY0_EYU9JEboeH17i-Guwg8o4U3OQSS2_Vpuvk_V5ooUArj3gQcWNA-RrwCYpALu99nsAAv2lmJCH64lD0cQmhTHje5xQJc3pxI5yINb1IQIRQxr4wBUtXKbuPahoEdiBgbhTi9aVybghfu8g1_0bpAEcNbHBMbZhGvCcq2fJA8bDWiVm3c6fKIVUmj6zqCAcBQa3U5EqP7gIG61KrCjJV2cKaSw7uDPFerGhWrIxhp_dtxyOcCFs40fPKOiqwMmo2GFu9WHwGQJdcUs7vepbS001ogsmJuzNqiAuKGF3v5w4Y5zJ7EBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
افزایش قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/141531" target="_blank">📅 19:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141530">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
برخی منابع عربی: تهران دمشق را به هدف‌گیری ۱۰۰ نقطه، ازجمله کاخ ریاست‌جمهوری سوریه، درصورت مداخله در لبنان، تهدید کرده‌است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/141530" target="_blank">📅 19:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141529">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نشریه WaPo  : آمریکا ۴۵ پهپاد ریپر از دست داده
🔴
آمریکا در جنگ با ایران حداقل ۴۵ فروند MQ-9 Reaper از دست داده؛ حدود ۲۵٪ کل ناوگان
🔴
ارزش این تلفات بیش از ۱.۳ میلیارد دلار برآورد شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/141529" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141528">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
برخی منابع عربی: تهران دمشق را به هدف‌گیری ۱۰۰ نقطه، ازجمله کاخ ریاست‌جمهوری سوریه، درصورت مداخله در لبنان، تهدید کرده‌است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/141528" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141527">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnS3isT2n9BRJfqNMt_azyGxgAbb44qXOeTKW5bd432iaATZK9-KZK41wK6EsjK2dlLTXBiCNElB0utUZA0vf_5KrYtzZRdj5ZIdG9aVaISHip3fgGuptyuklLxgMGjEZ9x4wgysY6A4-tW8Usq2WMx222E_PgIF6KoujU_ttov48gZH1hxDw5hsJBTp8hzW4ak4YrdQ0JbmDv1QcLUCAEx4GW_m3wFB33_OnBhFFaK1CJPClvw41mycPmD-XR2F3F0Cb8Er3idIeS5V-5oitnWQcmHfJMRPU9CtCw4qnNoawLkbRCEv6KftrRDquIHGCsPEu_RyNNFQcxJ7REECAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر بهداشت و سلامت آمریکا، رابرت اف کندی: تا جایی که ممکنه فست فود نمی خورم، مگر اینکه دونالد ترامپ مجبورم کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/141527" target="_blank">📅 19:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141526">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
دبیر سابق شورای عالی فضای مجازی ، فیروزآبادی: یکی از نهادها فشار آورد کلمه «هایده» و «لوزام آرایش زنانه» را از موتور جستجو حذف کنیم؛
🔴
چون ابتذال و تبرج را در جامعه ترویج می‌کند؛
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/141526" target="_blank">📅 19:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141525">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ناو هواپیمابر جرج اچ دبلیو بوش ظرف سه روز به خاورمیانه میرسه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/141525" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141524">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: ما قادریم تحریم‌های ایران را تا زمانی که لازم باشد ادامه دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/141524" target="_blank">📅 19:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141523">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFHIidye8VNQPmZdyt9s2HM-whqHAQSsHEXdU3pQfF2JWTrJjkhm796UbcOzcMxf2__c6rS5p7EOSzcawDgkPSlwFMxHxyFi6k3FayEU3inZ_89D2BDCLDp4U0dQLaK0-eUX-VV8d9SSjdpM1oRKDRkUwv3meQvY76I6k2giita7ja5xJAyqLjvEW4BnkLgViZunCaBMU6PmKf9YwxQ8qQv7jt_wb3j22s3XaIXP9-pTnrUsGDIpps6Zg2e3phsKiAvmDnBNiqYuiSw-UTqh_ZxVISXa-eXnyD-BC9nwuobd_RhrFEAikmMSwhbnfeUtkpRXgJHpX4BF4Aq3HhL74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل رئیس پلیس غزه را هم ترور کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141523" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141522">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
تحلیل بنزین و تاثیرش روی تورم  شنیدید از قدیم میگن فلانی «هم چوب رو خورد هم پیاز رو»؟ الان داستان اقتصاد ما و قضیه بنزین، دقیقاً همینه!  بیاید خیلی ساده و خودمونی اقتصاد رو بررسی کنیم ببینیم ته این بازی چی میشه.   قضیه از این قراره که کفگیر دولت بدجوری به…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141522" target="_blank">📅 18:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141521">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
به گزارش رویترز، شرکت هسته‌ای «نوکلرالکتریکا» رومانی روند خاموش کردن تنها راکتور هسته‌ای فعال این کشور را آغاز کرده است.
🔴
با توقف این راکتور، تولید برق هسته‌ای فعال رومانی به‌طور موقت متوقف خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141521" target="_blank">📅 18:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141520">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نیروهای مسلح یمن: ما ۳ قایق حوثی‌ها را که حامل مواد منفجره بودند در دریای سرخ منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141520" target="_blank">📅 18:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141519">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نیویورک تایمز: غول‌های نفتی خلیج فارس میلیارد‌ها دلار صرف ساخت مسیر‌های جایگزین تنگه هرمز می‌کنند
🔴
این پروژه‌ها میلیارد‌ها دلار هزینه و سال‌ها زمان برای تکمیل نیاز دارند، اما شرکت‌ها و دولت‌ها آن‌ها را ضروری می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/141519" target="_blank">📅 18:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141518">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
فیروزآبادی، دبیر سابق شورای عالی فضای مجازی:  گروهی در ایران می‌خواهند اینترنت ایران را بالکانیزه کنند، این افراد طرفدار توسعه انسدادی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/141518" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141517">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8563204fb3.mp4?token=WgY4NM7obaq94AQHmLS1bNOvD0LetrBHI5YCsBxgRc_BIJEc6dXSrkAJq-Jwq7AKFydw_dGj6TaIIa8yMPxR53_NlgVSAabBQa4YP3bZCUo8C3Tj2ejWW-zDhPxF9Y0VEoyMNOAvJN2CdqE-Q6_lhSVGRsH0ysg5FnY4vqXWth-VEaBADzld8QliZpd_C-0zS1t3e6tHrJzNCqY9vb1h03Kp0TwzeYZT0Lfyqo6ytc8gfNJMeT8zXFllSnlCE7nykYD8AtlW7_5ZRUYNXqvsfXmUG0TNxbXLXsVv1mVxNhtSms7kG9ERJO8eP1GiDpaxYvujfWLfBqlQzBUCHQXt0h7U1r64t5x9Ohg8xTApD85IwRI7P3AHz0vO08zZnbnHR_DlNQ4UnCYmZJuaB1YhhKidc8KqB94xFeYRS4yKPIIcGBJDMsYXTV7VT91lJHuWL2NkiTPiNRvbDi6Pt5Ds2ZcLHd9AsayOlT-H2j-AM5zrOmmrNLPnFeyT7GnA0_T4Xp44e2fhOqdHdM3sZMuNZhKKufHV7d8Ar0hyRLsQ5eWvXX-OgIfkU9iIei_Ca5xqI0tJRmQrkCFfbyVjelnxGI3GQ4eqw-YzaIGLPqNJiCmdlZXZvrL8vYwDnbZQSI92byW65CkcOkQPPbNJ3FjS1D1h6IMweUblA0t4-o7Bi6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8563204fb3.mp4?token=WgY4NM7obaq94AQHmLS1bNOvD0LetrBHI5YCsBxgRc_BIJEc6dXSrkAJq-Jwq7AKFydw_dGj6TaIIa8yMPxR53_NlgVSAabBQa4YP3bZCUo8C3Tj2ejWW-zDhPxF9Y0VEoyMNOAvJN2CdqE-Q6_lhSVGRsH0ysg5FnY4vqXWth-VEaBADzld8QliZpd_C-0zS1t3e6tHrJzNCqY9vb1h03Kp0TwzeYZT0Lfyqo6ytc8gfNJMeT8zXFllSnlCE7nykYD8AtlW7_5ZRUYNXqvsfXmUG0TNxbXLXsVv1mVxNhtSms7kG9ERJO8eP1GiDpaxYvujfWLfBqlQzBUCHQXt0h7U1r64t5x9Ohg8xTApD85IwRI7P3AHz0vO08zZnbnHR_DlNQ4UnCYmZJuaB1YhhKidc8KqB94xFeYRS4yKPIIcGBJDMsYXTV7VT91lJHuWL2NkiTPiNRvbDi6Pt5Ds2ZcLHd9AsayOlT-H2j-AM5zrOmmrNLPnFeyT7GnA0_T4Xp44e2fhOqdHdM3sZMuNZhKKufHV7d8Ar0hyRLsQ5eWvXX-OgIfkU9iIei_Ca5xqI0tJRmQrkCFfbyVjelnxGI3GQ4eqw-YzaIGLPqNJiCmdlZXZvrL8vYwDnbZQSI92byW65CkcOkQPPbNJ3FjS1D1h6IMweUblA0t4-o7Bi6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ ایالات متحده آمریکا:
ما کارهای بدی به آدم‌های بد می‌کنیم.
برای مدت زیادی، آدم‌های بد کارهای بدی به آدم‌های خوب در داخل ایالات متحده آمریکا و در سراسر آمریکای مرکزی و جنوبی کردند.
ما قصد داریم به آمریکایی‌های بزرگ و شرکای بزرگ قدرت دهیم تا کارهای واقعاً خوبی انجام دهند و در اعمال خشونت علیه کارتل‌های مواد مخدر و سازمان‌های تروریستی تعیین‌شده بسیار توانمند باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/141517" target="_blank">📅 18:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141516">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5Be-xGy-VsjeUS-71FSAvdKIWu1Obij_FEGwK6owlR6n8T-zKyp_FhqrOuqGj_q3ULwC9tjDEbM8VIuWYw-JqfUueZVKxstJ82WwBPJc_R_47ioZtiz27TlpS19YD1qi0EHmpHMIoVlF211uD9ZYPr0eihkHxYT25e52rcOHUslgWf8THKAl9OQKUk78HLzWmB5fKsqkYX8piTGu9KptbnHt2MsywQN2bAPSP1nFJb0Ag_qvoNZgO12mQZXwx6KuQ5pD0JQAbgdn-mheUrAuPFIX-cYQE9fqBuGTbF23R8igAVGxx68E64_gXBAprmTIpiRwJ2z0Fze-Yro3HqiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الحدث: سفر اسماعیل قاآنی، فرمانده سپاه قدس در بغداد با هدف منصرف کردن گروه های حشدالشعبی از تحویل سلاح خود به عراق، به پایان رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/141516" target="_blank">📅 18:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141515">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd4d419c2.mp4?token=dOFMTNj7XPn4ZfMuw5aKRVi6xvAQ8_LoQ20OvdXMu3exIOBnbxhBil8uvLcdGC8GG9ldKnRZ82M2dJ-_8XfPdgwRkqhszFD75NvAbViNe7Jl15RvPgK1SLkoa6DIYrQxlgEwaJZxsnCOWRNdKVLmnrfJrwAIIUS6UzZfnL9IxrkkJoK8VwdtsD1jNQOOeB3_jnvDQ9jAH3Gluz_jlaQKqfxLXY37TT17oQXfBOpUJULsAFHH2p78iThLkPECR7KXNeFWxRZxq4ehqDr_Ut3QWfJhUz8d374fd80BY-YifVHegbK-akgkI_GMh2HMYfcatGyDDu2HfFhGkGNF5HTDOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd4d419c2.mp4?token=dOFMTNj7XPn4ZfMuw5aKRVi6xvAQ8_LoQ20OvdXMu3exIOBnbxhBil8uvLcdGC8GG9ldKnRZ82M2dJ-_8XfPdgwRkqhszFD75NvAbViNe7Jl15RvPgK1SLkoa6DIYrQxlgEwaJZxsnCOWRNdKVLmnrfJrwAIIUS6UzZfnL9IxrkkJoK8VwdtsD1jNQOOeB3_jnvDQ9jAH3Gluz_jlaQKqfxLXY37TT17oQXfBOpUJULsAFHH2p78iThLkPECR7KXNeFWxRZxq4ehqDr_Ut3QWfJhUz8d374fd80BY-YifVHegbK-akgkI_GMh2HMYfcatGyDDu2HfFhGkGNF5HTDOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه پَر کالباس 80هزار تومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/141515" target="_blank">📅 17:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141514">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075e2967ac.mp4?token=KIcXMhIZOO1Ei7HURywI-1cotGzIrU1CDu0D8oOOe_Z6q-BCBghAW4OdsEMbIfo8wpfADRJbLzbNqqqsiQTAYyvvOIq9TiKVLyL_tjN_4s3xnc18ssxOtpZD3LMT2HNSA8iNgADPz5bkJsV6zNEJghuVKxExhHPM3Bx8-4QBMlIHzxdm03-Xn5hSP4_CzE7SXFmL31xFyp8R8MklguNIBB173sIzLzhzUFdZQkvoUdLa63Rd1PAyiH4gk5oNKwsISMPyGoB2FEQiy6_pBngfq4NfCSzFM7O_Xi2ae8tCPIr9w53hnBAs6ATy276Xdl_h66M2lTdIpPZZUKQcskFRgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075e2967ac.mp4?token=KIcXMhIZOO1Ei7HURywI-1cotGzIrU1CDu0D8oOOe_Z6q-BCBghAW4OdsEMbIfo8wpfADRJbLzbNqqqsiQTAYyvvOIq9TiKVLyL_tjN_4s3xnc18ssxOtpZD3LMT2HNSA8iNgADPz5bkJsV6zNEJghuVKxExhHPM3Bx8-4QBMlIHzxdm03-Xn5hSP4_CzE7SXFmL31xFyp8R8MklguNIBB173sIzLzhzUFdZQkvoUdLa63Rd1PAyiH4gk5oNKwsISMPyGoB2FEQiy6_pBngfq4NfCSzFM7O_Xi2ae8tCPIr9w53hnBAs6ATy276Xdl_h66M2lTdIpPZZUKQcskFRgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه زنه بلند شده میگه من رهبر سوم جمهوری اسلامی هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/141514" target="_blank">📅 17:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141513">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neY3ejk5dmK03Kla9t0ymn_3albBNSSYAblB10sjH0pRHu4BJ8-PggWZEVnR0yOX4foE5vSml1nFUhyz9ifpeEML5hP523oYtfuFlSa55rdOMDvrsILrVhBp8HN6WSo2BFLG1hAr1vnnSQEXckQbe0O4xI7dU0ldrReYqH_F7NotHK8ecYPtswip0yOaZCk40TMUav733lmQsfQzGbsQdngZ-_E-Ial-Ece8R5gqIOhtSFRSPm1nL_nIYV9XFuMVgM-RslvGHsPBezooXlSIT7D41DoFRZNeMmXWYChMDMwOvGlEdTlSnVfM9R_UPbW4nTaPdRuH2dtQzqRfP_I9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مخبر:
راهبرد قطعی رهبری مبنی بر تهاجمی شدن جنگ در صورت تحقق نیافتن شرایط ایران، بدون شک معادلات قدرت را در جهان دگرگون می‌کند با اثبات ناتوانی آمریکا از محافظت متحدانش در خلیج فارس، پایدارترین‌ راهِ نظم جدید در منطقه، اجرای سازِکار‌ اقتصادی-امنیتی هرمز، مستقل از تضمین نظامی واشنگتن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/141513" target="_blank">📅 17:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141512">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
روسیه یه شرکت لجستیکی اوکراینی رو تو شهر پاولوگراد هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141512" target="_blank">📅 17:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141509">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a179373787.mp4?token=Lxqj9M7UYyKZUkU_DRyEvXAbwEZz8d2tk-98_pVC_OKvlrfnJoUcGaWToZ07vxrgQTBcP430U7FWRLFQmEe9UzF_-Sq6eqIX8z_tZiY54ZWNOwT4AXURGkKArR2e8vHxZO2B9tNVpBtGG58KuyDg4YrgT7XQqSlX9ryr2NoX8ExdYQ8DOM_SeVioH3U7Ilxmdge3LkCrJ96TbxG5dT5qKaSHIylzgSrCE8n36pVXK1zqo0PsibOwDc1E_oRj3N5ACebVwN4zxDGFDpsv5OSshUPl1fECiJjzpZlasmBqIINh9FJG85viHi3ZMgYUrejYbrsONzvCJFlB_L9we0dTGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a179373787.mp4?token=Lxqj9M7UYyKZUkU_DRyEvXAbwEZz8d2tk-98_pVC_OKvlrfnJoUcGaWToZ07vxrgQTBcP430U7FWRLFQmEe9UzF_-Sq6eqIX8z_tZiY54ZWNOwT4AXURGkKArR2e8vHxZO2B9tNVpBtGG58KuyDg4YrgT7XQqSlX9ryr2NoX8ExdYQ8DOM_SeVioH3U7Ilxmdge3LkCrJ96TbxG5dT5qKaSHIylzgSrCE8n36pVXK1zqo0PsibOwDc1E_oRj3N5ACebVwN4zxDGFDpsv5OSshUPl1fECiJjzpZlasmBqIINh9FJG85viHi3ZMgYUrejYbrsONzvCJFlB_L9we0dTGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز، اعتراضات خشونت‌آمیزی در پایتخت سومالی، موگادیشو، رخ داد. این اعتراضات پس از تلاش دولت برای اخراج اجباری غیرنظامیان از خانه‌هایشان در منطقه وابری آغاز شد.
🔴
پلیس سومالی به معترضانی که در برابر اخراج مقاومت می‌کردند، حمله کرد که در نتیجه، یک زن مجروح شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141509" target="_blank">📅 17:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141508">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh1_wMTx1MUA77geAALj4MpcYaofKruEEhobjUYhlCT3E3appbpwxAVE-lEQwhObzwl45ePRhdd1uszmEoNBjPIGjejHJgEtQt3w0ZM3F0dfJeN4acy83_D1FRIapqi2xXSa7YFu_btm_IZUk7D2VJ9A8N77ljjebKGnV_y3XIzr8jTFpWUwKN0DUDkuaVUVMgNsQTCucyZQJGboN_UbNp4qr6axSwPwX4tcoLnigLM1Albar82TChXAnEdaFnIuCSiZz1EZ7livE_HgrFFK5O2CzGl_j7AZavvKfuAbEMJey-CKZLxjd2qw43Q8dObLmC4JsTGEyu2Bp2mR8m2otQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد ارتش اسرائیل دقایقی پیش به یک خودرو در شهر غزه حمله کرد.
🔴
بر اساس گزارش‌های اولیه، حداقل یک نفر کشته و چندین نفر دیگر زخمی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141508" target="_blank">📅 16:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141507">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
حشیش و گل به عنوان پرمصرف ترین ماده مخدر در ایران اعلام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141507" target="_blank">📅 16:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141506">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN0J1We5eA3BHY-qtFZFbYrvMxqGV5xlNRGOuQlsgANqy6r6j7BrpnGd59RgyRlNYivlf8K-HKMuRAlT1DbhGMdT2SC9jEH08WoSKQV5JutqteZ-JuRSj-nWC5r05wbkERYIA-AwlD2qvKNcrbhhAIk-572OaLgfYWNph2zWR4Y4E7f3LWJuE9To31WjASMidAMAWO50JHLlImby4JpvXzIuOeEI14VynUZPJmQgzUMLqP8fUq2ksOqgGZLYdLOhEIMTayqvqbvqaaLdWAa5fI3bGnU02HQeKVFPqAEp86ooJD8Fd50pRxGxP612vWiUJUiqFohwld2VQwzTr0F7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏ ️
نامه عروس معصومه ابتکار به مردم آمریکا: عاشق آمریکا هستم نگذارید مرا اخراج کنند!
🔴
فرزندانم فارسی بلد نیستند، و مادرشوهرم در اشغال سفارت آمریکا فقط مترجم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/141506" target="_blank">📅 16:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141504">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHr7nGhwk5S29JmaTv498xJg41pLYYenOuAl9NbzsjOTl7ob_EvxFqUuazxKJInbMb3GqXc4wFb6och43OzzTxtw9b_muntD0WJ-q0gmlUdt8cNyaAdOVgopA3QyTj2QgRDYHWuSQVY9oNYVgJjqwWbkhhjUjP_Bwx6k-z2NqaUQkgIn8UyfXLphfRhkQOAcgb0tDI7PnlDjaSa_ffMmD1riCCNyH8SGUyw9wHLJeT3fLeQhLO9cwTeNlBlFuklgOVSQajWt3v5IwKCuoPtXAifrrHSNWcvaBQajdXUZ0_VLYmHVcwVKffoGqGUZEOrLPTywawDdPn1ASIc7xxah4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSLXWzzW6CanWl9--WvhhIJDC9PTP_sEdMlghDEz3L-kHoNkSp6FfHG0pals5Auw1DTMWiav90r7XiPrPu6UFQXOuDX-Kh5_rXO3dNJbqikgrD-rDKW8yK7T4CTRQrLiyAO-XeIxCn2uk7VzbGJJfWWsrLDr2Hir5wKpSiNgSEpLz-vbM6pqpHF9gjv4t20MdW02sQvA9A-d9Ad_jsMwWXUXfTBw64ySt8FrJUdfMis2o0cnnjYLvyicKIqlT8x0j2w7aYMTubfV3Z_md4uiD_5x0PiAOlTwbp8aGQBEZzvpLwlSOdxq1jJiLK_XkwPZ2lk5-YRoN08RA_jvp3PZLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از عملیات تخریب نیروهای ارتش اسرائیل در شهر بنت جبیل، در داخل منطقه امنیتی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141504" target="_blank">📅 16:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141503">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏
👈
الجزیره:  ایران هدف خود را طولانی کردن جنگ قرار داده تا درد را برای ترامپ حادتر کند
‏
🔴
واشنگتن هیچ ابزاری در چنته ندارد تا تهران را وادار به انجام خواسته‌های خود کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141503" target="_blank">📅 16:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141502">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: خانه ها را در جنوب لبنان خراب می کنیم و با تمام قوا به شهرک سازی در کرانه باختری ادامه می دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141502" target="_blank">📅 16:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141501">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edd86b4e6.mp4?token=bsX0UklrQ2cWyPBYYRIgWJUaabtSWK_NwFnpnzzZSJJ5dW_QE767KpwqDn-Ez0hn0Y0qpfR6ByLaPzvjXKVMbjEAe4h_0rxIGNy8Z8jOAaLL5seRt6ebByKUtYfXOYdhmWP4ob290ScPvAaVx84q8pro9i4NxkldNQc0eNW8mHzvjP-Gg5DoW1wvh1fUcw4M4hsxdaJJIpsO20sD6wXxkxNrEPLmUObyc7Gu99a_FYf0JC_KGSweD1zcRQK6vcIZ0k32uBQmvO52bYEbeiChDfQsrbQZnM2USIj6bySJVa626_XWKo7dg6eUPU3g02gwJMtUKRZAm0IfWMRzzD40iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edd86b4e6.mp4?token=bsX0UklrQ2cWyPBYYRIgWJUaabtSWK_NwFnpnzzZSJJ5dW_QE767KpwqDn-Ez0hn0Y0qpfR6ByLaPzvjXKVMbjEAe4h_0rxIGNy8Z8jOAaLL5seRt6ebByKUtYfXOYdhmWP4ob290ScPvAaVx84q8pro9i4NxkldNQc0eNW8mHzvjP-Gg5DoW1wvh1fUcw4M4hsxdaJJIpsO20sD6wXxkxNrEPLmUObyc7Gu99a_FYf0JC_KGSweD1zcRQK6vcIZ0k32uBQmvO52bYEbeiChDfQsrbQZnM2USIj6bySJVa626_XWKo7dg6eUPU3g02gwJMtUKRZAm0IfWMRzzD40iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: هیچ کشتی بدون مجوز و نظارت ایران امکان تردد امن را از تنگه هرمز ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/141501" target="_blank">📅 15:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141500">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
خبرنگار العربیه: ارتش اسرائیل از آغاز یک عملیات نظامی سه‌روزه در شهرک قصره در کرانه باختری خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141500" target="_blank">📅 15:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141499">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dska8IY-oFyT0I-pO8G_smBzu8P45E_s1s_9ysDNPUN3h9dVlxRTTN1x2CTb5bJS-nwzptmoIRik5pgyWle14wUDNTMGOt_jcACtYRDZ2EFdEoh-9lyOBtisgJMd_IG8EJMg29yaDgDBVCp8TaF0SDsrJqG_zo8f5PuYpGIEIkj3TeYHcZ5mSgwUxwuAKC-sfA649Y9Y5dS9iYESTk4w0wLAyO_O9nERB0gN5ZoNGruN5YGtMm893LPZt68gEcWHxuLLrPS1XXCVuw_ZlKW4PkP7HBKOxz82_RI_UMDV_Nw4Yq57bWCs1qx5D-Y5n0bPxjPFaaCRjWnqN2obKjYS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر آمریکایی "جورج واشنگتن" به همراه گروه جنگی خود، در حال حرکت به سمت ایران است، این در حالی است که مهلت آتش‌بس بین آمریکا و ایران رو به پایان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/141499" target="_blank">📅 15:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141498">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T14NxQ7FNO03Al0zyP7jL_mF2aFF_fxFQeq63iaRUPu3zLkzfPeBwrzuDr11L6QqdJlWYebL4dvpb_FQQ-MLJBKSlISCkro-vdDCKCpVk5oCUZHKeih1TgDEFap2riFOhF0XuRSplUoPxR4eSW_a9r1AXZ1xQFWIwMtgfHXy4iyc6E_W1-yhiCvlPj8aVCGX3PyQUXyz8YqEV5dwrEmaO372sLOEU1_rFl7IUr9S-68ZeJEIAz2eT3sgFi3KRDUkui1AUFDcN76CjOoqq1nqYes6bnPIyuEeXo-Ex4bxWqva5jtwWGhi3qzVZGbVNIPbbFM0GgogrZUiQvdlsYQ8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۷ کشته و زخمی از نیروهای "درع الوطن" که به عربستان سعودی وفادار هستند، در پی حمله‌ای توسط نیروهای یمنی با استفاده از پهپادها به یک اردوگاه در منطقه "العبر" در استان حضرموت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141498" target="_blank">📅 15:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141497">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm14OJQhw4pnWwlqA4QsmAd83NnIVZLBPJZaolsH1EdzCdAPzvjnmH_4b6JMNaPB3FLMbEnRkbKd2432qXJID0UQnpcjmStpxyu0wqqrsVrKeNdC2-W91pvLlSY6cw8V2WiW9prVLdXbYYCF56Gbp2sIXo1vUErcxptet6GLlKAVP1dOlxkqSe_2AwVDZfk9hNgYbmCe-3ewHJ-MycOPm3RL4L55uKldedXpYQQYhd4YdOV-c05B624RH0U3TolnAMr1EPhgff-XDXjQyOE7dS0VAFx-EccZ-4fqfR2ZBZ2OHpFpHv5C7gCIMy9vL4ZSoKIqdT_-WXbL0eo26YMHUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش یمن با استفاده از پهپادها، مواضع نیروهای وابسته به عربستان سعودی را در صحرای العبر مورد حمله قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141497" target="_blank">📅 15:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141494">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVfEFclfK5e-2f3DsDcBDg6Mdk4kkKt9cM2MlG5JvjVhWygr008-x7ijfxuuzl0zzoTmME9_tctYzqiFKPgQ6hetDyFE6rH_3mt1HsT4sS9LfGp4RdznErR3lUX-BdDQ3EM1eirbOX0qi9RLVvY-P-DnE5k1P3GegAW2vR_uZiVTasyqfAIQWdPue7qOKTW_arf6VeeaaNzPz5h5ZrzJTAEavyr8CQXrgqJ9tspc3eLpTjlocOT_YWAjHt6NAMKyWkQsJPrYpmTOdoppjBUK44oROGM_j7hCcsvMJzvHB51rtAdA93-S1q9CAaVn7CxCOK4_QvpNVXOBMsnmpDoKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NotEXejBSb9vVlwHT5W6jL3Gt3X0GzGsvBrHRCzwbWw-kp7pMHwfbnyNVqPnvYnLbJLNugrxjY-fO-dcGh2Zgv-9OLovrGYh2ZNuBxPQffhFYB_JQZZcKw4F1UAqeKbTbJhK_tx20mPM6CBRY64IxY5ilQa4sIvZ9HbTBlrg75vqgEfMSeuWdeEO-OwYu3E99otxbIOXE9pvlD2xnPbXiqpRF4s25A7Eb2oRHkw5BosgLHJq1KOwdu4Y4mj2x36Ya9CGo2j6n17HAPT_2msOQJPFbgh1lQAppHyNxMdawNvOnRXiqijXA_S8-A7l56GbGQ--dSv7IFRneHPDmo9nXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGi3KHn2TIufZD-xUOq3JlEKw3gymhu1NtqK12_EMGBpaAA2Pt6dhGnx2OCoDLPq8v0jXdHqMG5AUjFAgRHSUzTrgN-lEPoOGDbArfkl8ApaSe4QRy3ZB5DjTHKSPTcaSq-ryiZmerv7N9VRm7dIEMDG9z2b5n8vLKLZ2htOqW2UScA5yoH1X-gW0c5Y8_z_ILoVCA7uUpDaeCdWyJTsIRMrGaRUHARqNLCbguV31Q4kc1h5iSRFGwhq2-DMNU1SsHhGD3YLQof1vXqNRCreXN53_C-GxCgtBhIrk7mfDuWN_8GfTHsCNgxVDcXxQ9mF2TQ2sjqg3QD9MWej8lZAHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل : هزاران تن تجهیزات نظامی، و وسایل نقلیه جنگی از آمریکا به اسرائیل رسیدند. این خرید و حمل و نقل توسط وزارت دفاع و ارتش اسرائیل انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141494" target="_blank">📅 15:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141493">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
پلیس هلند از کشته شدن یک نفر و مجروح شدن چندین تن در پی وقوع انفجار در بندر روتردام خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141493" target="_blank">📅 15:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141492">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/244de8d332.mp4?token=LYoV_BibPsTvJpd-pwjOh9f1XUlln4eayXcRP80wVcf1PFCr-s55uBvn3mDfaUneYZED0lI3NkOwYFIy22l0SWPN1DyTSL31o3raJixjihYR4A_7AqYRzqRQ-k1KRKK0v5JhvY5TNTP_gCparOvU9RR1f7nkBJGXLPogNgxVhk0UOZ5Id6SCb4Itz5p-NaRNUyExr42oBthyX9FYtIpPGkUxUGf4vLb9z-BCBjdsoNgLj3dZlUIIrXAK9eaPGlnXTkeiWcYmfE3T4QfMxd8VP1Nk2nPAtrWztofkiA_ulvdfHQLBAjgHTnwEbJ5pKTl5ZDNobPWeddrqwIW3-AeApSAosgmGBg2B4dy3P0_9RdlUvBAJ_mRuCQ1Y-AjOKylx97giRi7smE8lF-1Bv98zkYsnG0_I9jDtQ1EwBjvDseMKNvvSPkF_-fFmM8vhoAuugJqY23fltnQbxw86SvZDfNSkIXgB1FUPNUTEC5Jy7p03XAFcBl1-n_Ixj4pEcn-XtSrQ-jXwTQnN8r7f6uRKtDH7Ho8Dta8TGyTJm78iuKZwIp9tTNUm4-pPTzFeNM6ovf37Nt5G3Kegfp90WtxFAYh2vWPpVO7Lpg2jWuBgVCThFv2ZticdCDY3QWuma4HBIRwRdszeF8iCA4mG3gfukU0SYCUutf-6WodLRXGpXMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/244de8d332.mp4?token=LYoV_BibPsTvJpd-pwjOh9f1XUlln4eayXcRP80wVcf1PFCr-s55uBvn3mDfaUneYZED0lI3NkOwYFIy22l0SWPN1DyTSL31o3raJixjihYR4A_7AqYRzqRQ-k1KRKK0v5JhvY5TNTP_gCparOvU9RR1f7nkBJGXLPogNgxVhk0UOZ5Id6SCb4Itz5p-NaRNUyExr42oBthyX9FYtIpPGkUxUGf4vLb9z-BCBjdsoNgLj3dZlUIIrXAK9eaPGlnXTkeiWcYmfE3T4QfMxd8VP1Nk2nPAtrWztofkiA_ulvdfHQLBAjgHTnwEbJ5pKTl5ZDNobPWeddrqwIW3-AeApSAosgmGBg2B4dy3P0_9RdlUvBAJ_mRuCQ1Y-AjOKylx97giRi7smE8lF-1Bv98zkYsnG0_I9jDtQ1EwBjvDseMKNvvSPkF_-fFmM8vhoAuugJqY23fltnQbxw86SvZDfNSkIXgB1FUPNUTEC5Jy7p03XAFcBl1-n_Ixj4pEcn-XtSrQ-jXwTQnN8r7f6uRKtDH7Ho8Dta8TGyTJm78iuKZwIp9tTNUm4-pPTzFeNM6ovf37Nt5G3Kegfp90WtxFAYh2vWPpVO7Lpg2jWuBgVCThFv2ZticdCDY3QWuma4HBIRwRdszeF8iCA4mG3gfukU0SYCUutf-6WodLRXGpXMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حاکم دبی در لندن مشاهده شد
🔴
محمد بن راشد آل مکتوم، حاکم دبی و نخست‌وزیر امارات، در منطقه چلسی لندن دیده شده است
🔴
تصاویر منتشرشده او را در حال قدم زدن در خیابان‌های این منطقه نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141492" target="_blank">📅 15:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141491">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
پاکستان: مهلت ۶۰ روزه مذاکرات ایران و آمریکا قابل تمدید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141491" target="_blank">📅 15:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141490">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
اوکراین: ما مجتمع گازپروم در باشقیرستان روسیه، بزرگترین مجتمع پتروشیمی را هدف قرار دادیم
🔴
ستاد کل ارتش اوکراین: مجتمع صنعتی گازپروم توسط پهپادها در فاصله ۱۳۰۰ کیلومتری داخل خاک روسیه هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141490" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141489">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است
🔴
کنعانی مدیرکل حفاظت محیط زیست مازندران: تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141489" target="_blank">📅 14:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141488">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نتانیاهو: شاید بتوانید بریتانیا را «جمهوری اسلامی بریتانیا» نامید
🔴
یک نفر گفت که اولین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141488" target="_blank">📅 14:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141487">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ناو آبی‌خاکی از رده خارج‌شده USS Peleliu (LHA-5) با وزنی نزدیک به ۴۰ هزار تن در جریان رزمایش RIMPAC 2026 و در آب‌های هاوایی، در یک تمرین نظامی به‌عنوان هدف مورد اصابت تسلیحات مختلف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141487" target="_blank">📅 14:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141486">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزارت دفاع ترکیه اعلام کرد که بر اساس توافق مکه، رزمایش‌های نظامی مشترکی را با عربستان و پاکستان برگزار خواهد کرد.
🔴
این وزارتخانه همچنین تاکید کرد که توافق با عربستان و پاکستان بر تولید مشترک صنایع دفاعی متمرکز خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141486" target="_blank">📅 14:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141485">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نتانیاهو: شاید بتوانید بریتانیا را «جمهوری اسلامی بریتانیا» نامید
🔴
یک نفر گفت که اولین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141485" target="_blank">📅 14:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141484">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ادعای یاهونیوز: امارات میلیاردها دلار از دارایی‌های بلوکه‌شده ایران را آزاد کرد
🔴
پایگاه یاهونیوز با استناد به برخی منابع رسانه‌ای مدعی شده که امارات متحده عربی میلیاردها دلار از دارایی‌های بلوکه‌شده ایران، از جمله محموله‌های طلا را آزاد کرده است.
🔴
یاهونیوز نوشته روز پنجشنبه بعد از انتشار گزارش‌هایی درباره اینکه امارات متحده عربی دارایی‌های بلوکه‌شده ایران در بانک‌های اماراتی را آزاد کرده است، قیمت نفت کاهش یافت.
🔴
بر اساس گزارش رسانه «هرمز لتر» (The Hormuz Letter) و سایر منابع در شبکه اجتماعی ایکس از جمله دارایی‌های آزادشده ۱.۵ تن طلا بوده است.
🔴
برخی منابع، این اقدام را سومین جابه‌جایی از این دست توصیف کرده‌اند. ادعاهای قبلی در گزارش ماه ژوئن خبرگزاری رویترز حاکی از آن بود که امارات با آزادسازی ۱۰ تا ۲۰ میلیارد دلار موافقت کرده و بیش از ۳ میلیارد دلار آن در میان جنگ آمریکا و ایران تحویل داده شده است.
🔴
با این حال، وزارت امور خارجه امارات در آن زمان این گزارش‌ها را تکذیب و اعلام کرد: «هیچ‌گونه دارایی بلوکه‌شده ایرانی از طریق امارات آزاد، منتقل یا تسهیل نشده است.»
🔴
مقامات آمریکایی نیز ادعاهای مربوط به توافق‌های جانبی یا آزادسازی وجوه ایران را رد کردند.
🔴
گزارش‌های اخیر نیز تا تاریخ ۱۳ اوت هنوز توسط ایران، امارات یا آمریکا تایید نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141484" target="_blank">📅 14:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141482">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYWxWfDOSyj3c7wqkMQKN2bBoij0JU8yzYe3E48lih4csNJPInz25HDYvfCNeIfIn8N5sQ4lsHP9gWFJKTxq5mtajEwNpjZd_as-oWoc2A47zj2Hbdxusk1ADpBQRlqzHSoBa0z_4XBETeXfWq5206wPQ-_WrbCJVUH6tnXbPIb78KJbZm_Wtq4-1-ZY2uNHPI2zGHCN2xbPLf5qNCjKz7mE57ThqRlWYIrU909a_9bYgOLwqz5KyEihx4FMfWz4OYCcOqZlqt9voAtbo-Hghr77kebzBPUab6WqqWoTF5viwnIJJgrYYTClhDibDnwFHEG8wrmzz8XBa1evcpgV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=KXKKPIiv88iCgf7Zmcyp6N1OyAyrmxkgYjxe444b4q1VuGmwEVK7ye00rn_2uwzScNCbJoxI1kdVRN74OZCrZsYwuZGM8XZHBhsaYLP6yX8uispcT9vkZm_mfYcpJyZ6lmPEJiEo3EFS_qOQrtpFx8xINvs1VkL04lvJ7EsOj-3h5D8qPBCB0SfZCW1xjISxW8qpLiGXumiiVhAdckAh4Z0FkT-N-JqTCZeo0NpxezSq28lCK3J9P4HnNWAS7BqvjAs6WYxQwmdpU49gqwtp6NGeLD4DH_lWiB6Qf1bht8ti42GK-jQH6IVhOqcHDmvnNqnZ0oJAGzstUjPKx4YzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=KXKKPIiv88iCgf7Zmcyp6N1OyAyrmxkgYjxe444b4q1VuGmwEVK7ye00rn_2uwzScNCbJoxI1kdVRN74OZCrZsYwuZGM8XZHBhsaYLP6yX8uispcT9vkZm_mfYcpJyZ6lmPEJiEo3EFS_qOQrtpFx8xINvs1VkL04lvJ7EsOj-3h5D8qPBCB0SfZCW1xjISxW8qpLiGXumiiVhAdckAh4Z0FkT-N-JqTCZeo0NpxezSq28lCK3J9P4HnNWAS7BqvjAs6WYxQwmdpU49gqwtp6NGeLD4DH_lWiB6Qf1bht8ti42GK-jQH6IVhOqcHDmvnNqnZ0oJAGzstUjPKx4YzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل درحال حمله به زون، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141482" target="_blank">📅 14:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141481">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
عضو کمیسیون انرژی مجلس: هزینه تولید و واردات بنزین به ۵۰ هزار تومان رسیده و من صحبت هایی از هزینه بنزین ۷۰ هزار تومانی هم شنیده‌ام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141481" target="_blank">📅 14:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141480">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است
🔴
کنعانی مدیرکل حفاظت محیط زیست مازندران: تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141480" target="_blank">📅 14:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141479">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرگزاری اینترفکس اعلام کرد یک مقام نظامی روس در انفجاری در کریمه کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141479" target="_blank">📅 14:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141478">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
قیمت آتی نفت برنت با ۴۲ سنت یا ۰.۴۷ درصد کاهش، به ۸۸ دلار و ۵۶ سنت در هر بشکه رسید و بخشی از رشد حاصل شده در ۶ روز معامله گذشته را از دست داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141478" target="_blank">📅 14:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141477">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
الجزیره: بحران تنگه هرمز، بازارهای آلومینیوم را با تنش بیشتری مواجه کرده، قیمت‌ها به بالاترین سطح در ۷ هفته اخیر رسیده و ذخایر جهانی به سطوح تاریخی کاهش یافته
🔴
این وضعیت ناشی از نگرانی‌ها از اختلال در تأمین‌ آلومینیوم و پیامدهای آن بر صنایع خودرو، هوانوردی و ساخت‌ و ساز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141477" target="_blank">📅 14:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141476">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba390ce5a.mp4?token=kG1XQrCIeIuy_uJvfF0ATitkp-i0iiMfqQ60_m2yNGCXnhe2QMZ0Oq0_6LQA1B8d6H7cU0kZDE2I1TBvBPLd2_XVWQz3xW357cxwFWMymHHM6T3zREzpvJLupFdY5cua5R_RAqp9NjLLeVhzOa0WsRUDcPNRzPRRUOk4gZZbGwNG3uWFIG07ngFQzIq9UxHCHhbe3eE8XmUrtVayVXXxbNF9hxlwT7fkbLwt2fAroZrNbIT7Sm-LoDC1NxoIedGJ3uWc-LvdRp2Sy-bEBRsbj-JZ60k7vJmqIetUkio2zWsHYs94HS2skQsiSyICiGCF4J854plSEt-jxHyXu8HW95_1K_DWtDsQmabPCpbpZuqFlzW33fcff00vIJyyBBrUvKYlGfw5T1-tDPkt5ZUdcgGFNu7DSkGrV96_KjzBx7znBQ8QDN9BrY9fFWsr5yME26J8Ev27irvhiV-A7TpIydFzJNEovU1TqkS21CV-DpHG19Qp8RYI_Gfaeagk5_3lPFRw5qf9nIuVdKs93cFauHfUTKb4Eo0iDSrjnIfXiUiMU8tRw3Jp5qP-I2SW0Hxq3zq3y47gw47BtPUM4NXiCEcYvqliQ4dvRtHWchscHB84eoEQ6mdpY2auKOKYm0n3YTkqP835xX9ErbIKG8WcEjO8YZrl9QBFKl91UbV6kNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba390ce5a.mp4?token=kG1XQrCIeIuy_uJvfF0ATitkp-i0iiMfqQ60_m2yNGCXnhe2QMZ0Oq0_6LQA1B8d6H7cU0kZDE2I1TBvBPLd2_XVWQz3xW357cxwFWMymHHM6T3zREzpvJLupFdY5cua5R_RAqp9NjLLeVhzOa0WsRUDcPNRzPRRUOk4gZZbGwNG3uWFIG07ngFQzIq9UxHCHhbe3eE8XmUrtVayVXXxbNF9hxlwT7fkbLwt2fAroZrNbIT7Sm-LoDC1NxoIedGJ3uWc-LvdRp2Sy-bEBRsbj-JZ60k7vJmqIetUkio2zWsHYs94HS2skQsiSyICiGCF4J854plSEt-jxHyXu8HW95_1K_DWtDsQmabPCpbpZuqFlzW33fcff00vIJyyBBrUvKYlGfw5T1-tDPkt5ZUdcgGFNu7DSkGrV96_KjzBx7znBQ8QDN9BrY9fFWsr5yME26J8Ev27irvhiV-A7TpIydFzJNEovU1TqkS21CV-DpHG19Qp8RYI_Gfaeagk5_3lPFRw5qf9nIuVdKs93cFauHfUTKb4Eo0iDSrjnIfXiUiMU8tRw3Jp5qP-I2SW0Hxq3zq3y47gw47BtPUM4NXiCEcYvqliQ4dvRtHWchscHB84eoEQ6mdpY2auKOKYm0n3YTkqP835xX9ErbIKG8WcEjO8YZrl9QBFKl91UbV6kNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسعود نیلی: امسال رکورد تاریخی رکود تورمی را در ایران تجربه خواهیم کرد!
🔴
با خروج آمریکا از برجام ۱۰.۵ میلیون نفر به زیر خط فقر مردم اضافه شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141476" target="_blank">📅 14:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141475">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
هواشناسی: گرما تا یکشنبه در بیشتر مناطق کشور ماندگار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141475" target="_blank">📅 13:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f465758dd.mp4?token=c0u5f6Qgh1CnrXeVcoeTXeXq7BvIApflCiWFtIJFnq1E2dszj-WTgJ0pjPS5HoXqUcQ7coqiaSjqWFNeapibAt3lMu4Fammk8-3JvuynxaMLMPCva1hcQwprwxVtjj9QBtXrjOKkOJE-YVoWhIIbqzRWBOPqW-DHWnub_A3NNtO8j5XIZtfJ2AyJCaBsoaV0F5jtKL9cHPcz_-1c0bqw90udyZf5Lu4aLbpLzH3Hoia1ZIhNzVoMeJ_xjIwBtWBOpG8Q2SJPhPEc85ssbvp_TBueDrV1BoTXWx7YFaQpnPgi5kr2DRcRR7nOojeE4ugn_CMUm-oqQERiR9O0mDedoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f465758dd.mp4?token=c0u5f6Qgh1CnrXeVcoeTXeXq7BvIApflCiWFtIJFnq1E2dszj-WTgJ0pjPS5HoXqUcQ7coqiaSjqWFNeapibAt3lMu4Fammk8-3JvuynxaMLMPCva1hcQwprwxVtjj9QBtXrjOKkOJE-YVoWhIIbqzRWBOPqW-DHWnub_A3NNtO8j5XIZtfJ2AyJCaBsoaV0F5jtKL9cHPcz_-1c0bqw90udyZf5Lu4aLbpLzH3Hoia1ZIhNzVoMeJ_xjIwBtWBOpG8Q2SJPhPEc85ssbvp_TBueDrV1BoTXWx7YFaQpnPgi5kr2DRcRR7nOojeE4ugn_CMUm-oqQERiR9O0mDedoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه قایق ایرانی رفته تو تنگه هرمز برای ماهگیری که یهو هلیکوپتر آمریکایی میوفته دنبالشون، واکنششون خداست
بنده خداها اصلا جرئت نمیکنن نگاش کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/141473" target="_blank">📅 13:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141472">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2g9nxwRdUojksoytjCzbGSjfrfENtd-Sx5mb42zUs2Nt4Rdn-PI0sofj1wGcvegmVbxPvQg_uzw5CTj9HlcE-rXdLuMaA7PiTrj8mCBYEbsbrx2glXkdNSeqL9oGcLSrOxgz9HnVzLNR7TxbKuf2Ilvtp13EaQ3HDRz9ESOsadcIiDgtyzGHc-2iCPEr-RAfEtZnRJcaRAXUcPcjq_nnDXSr0_sDj9v3OFKD6PEEdxxUwda0mtuo5dUnQkOLM3lSnD5xUO_Hg1ELl4gRKwHy89owViTi_4141EDs3LO1beqtZVOLMf2707XsWEAw6Db34k0Swk6HHQQ6ipKrZyZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز یک هواپیمای باری ایرانی از فرودگاه تیانجین چین به تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141472" target="_blank">📅 13:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141471">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgCc-fA0ngyqTHB6wQU_dcSqx1LHIUcxt1NxlMhVM6OcpOzk7EGWWi8RmzC836ZbF8L8af7gpkscbCzDB4T3M6m_mP4Ktr-I7laUDVOdYR2a5enbFG_N9fggs7UYRCdVRUzuQLGacMEt5Fgd71DvuNBWgJ03MYjCjm19CAN2M_P-1ZO_NeDW3tqy6GMTp1anlNMH-YwCApjwzc5viRB5tmw3u15U4hCMWknUYGg1Wjr6JKhVo3aVU25Oh1iNjSZgImu36taZYxVeZRhTTXHuatUg3CZYW70ViC2iFnRhkYuC5y2W8DUGuNRA1NBYuAs4NLuZzC40M67T_M6EVTUiEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
مردم ایران با میانگین درآمد ماهیانه ۸۵ دلار در در بین کشورهایی که پایین ترین دستمزد ماهیانه رو میگیرن رتبه ی سوم رو بدست آوردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141471" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141470">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزارت دفاع ترکیه:
توافقنامه مکه با هدف ایجاد روابط پایدار بین ترکیه، عربستان سعودی و پاکستان امضا شد. ما به دنبال انجام رزمایش‌های نظامی مشترک با متحدان خود تحت این توافق‌نامه هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141470" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141468">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbmIOEPSKBtrDPYgyHsAzBMZM3Fe0pi2dIvfy0CHpSN4rcZDq6gOk0TZj1HrkZrRVjcG4GDRiS9wSoVWv_9436czPJYpd32rkATvYPQpejpGdlqQWWyx0DaOMyx7Bmt3w1yfHwtbg2VZ3wP5-A9wlJJholaAX1d8xdhnwjfl2LZHcnilVcXTquMEJZu3OvVZMlq0MufzLQirJ18x2Axz2FizUQxc0yJIuyHuGPBCAjJ6mawkvqD17T_AAHuV-vUxCb14nv5YBJlxbbXyJv6bvIaTODovFzey8KTVJ5bSJyPh1TZ8K0YUd1N4iCbdQgqG3SHPrSRiCxjRyO32omgjqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=Aw-11VuX-YXOFVa_anbIOOPrqLvDftpeoNQQCDV7tVQ5cURnGJVLJkGXztF79rMEoeb8UiJSW_NqBWHn9Oj5Vf9QpygG07KVazDem9dvD9wtHD2vlWFHocns9DIQIKNjHGtg1Vm2Tpjmwi9NQZqJ02ALpJa8dO2rRsF2tSY1EFlTn-Bw5W-EOiCSlgwCy3nHHTka04E4VKU6DjeHbkJrPwDBBDGQ9ZN9MUc5XrHMdLKh5gMw3GxqlN0EF0LPQq5xdfcOT-HhB80Sue3E4WgnkaDrvh2Z0LaugrPlvMuc7XNbdb5qqNm-ez_lxqTvDkuuvbc-9jO1su3jogt19k-Z9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=Aw-11VuX-YXOFVa_anbIOOPrqLvDftpeoNQQCDV7tVQ5cURnGJVLJkGXztF79rMEoeb8UiJSW_NqBWHn9Oj5Vf9QpygG07KVazDem9dvD9wtHD2vlWFHocns9DIQIKNjHGtg1Vm2Tpjmwi9NQZqJ02ALpJa8dO2rRsF2tSY1EFlTn-Bw5W-EOiCSlgwCy3nHHTka04E4VKU6DjeHbkJrPwDBBDGQ9ZN9MUc5XrHMdLKh5gMw3GxqlN0EF0LPQq5xdfcOT-HhB80Sue3E4WgnkaDrvh2Z0LaugrPlvMuc7XNbdb5qqNm-ez_lxqTvDkuuvbc-9jO1su3jogt19k-Z9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل درحال حمله به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141468" target="_blank">📅 13:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141467">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏
👈
انجمن تهویه مطبوع: مردم بخاطر گرانی و نداشتن پول کولر رفتن سمت خرید پنکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141467" target="_blank">📅 12:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141466">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نشریه فارن افرز نوشت: «آمریکا ذخایر تسلیحاتی خود را در منطقه از دست می‌دهد. ورود به جنگ برای واشنگتن آسان است، اما هزینه‌های پنهان اقتصادی و کاهش توان مهار چین و روسیه، روند افول آمریکا را تسریع کرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141466" target="_blank">📅 12:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141465">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgHaR5tXw-p8hq0k2T100VNNn6PzxrWhPO0BQjKHjuxJa8NtEOlhaPxZGD8f3T9KxyR53w75JcmaIvipCRaST1hAtHKeFa9ewOiKOOV9F7YW2Tb-RZnpkIQLk1k75o5UAIh9gnCL2VEDvafI9DKT_eJEmg0zy5O3LwQQrokIuR-8dRqAJxVTvuMiI5_6xgGEwThQZ9WSsarG9ksc-yrW5yjukDhe7DyXWcB8UqdgqU9JULY0Iohp3idtQ-KHL9g0p1VADTH5gm5s93BpcJ3_0NBLbv7xWVqhvHSR3-dKRdPYAlohhwAVFwYREkneqRg60epQwueHAYeD2KSE7MQ-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
عضو کمیسیون انرژی مجلس:  طرح گران سازی بنزین از اول شهریور طرح مشترک سازمان برنامه و وزارت نفت است ربطی به سازمان بهینه‌سازی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141465" target="_blank">📅 12:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141463">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985e98ad84.mp4?token=q-wy0AYRuwLDegre8oAd9ZDv-5QkRKIjQiO1Wn71gE_qyf0YuS2HdKkWBsgQ7q_vP7iWE5pYYqfRkXdlQ4j6ne4TQvO5usFQs1vKgKYizlwKQc7w_aoGar7QkkGODCzHI-y95V0xrOJ9c0Gzuze_HCgO6z5i3dx3f7Tl3jopNnGf9JI4YD2EjCj6NXhcmndL7t2YXepIEmZ_fUSwo1n4mqNAN_3YTxVoDYn6UKx3zptM38tvW9NtSlbrIu89EgVYqvSLy1DoPEB33cmonJv0dFRm91fADsj3fc37Ot2T6HIHUn_tA1XKADsqEKF80h7Rk0n7-8Qe10e2w58OphkLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985e98ad84.mp4?token=q-wy0AYRuwLDegre8oAd9ZDv-5QkRKIjQiO1Wn71gE_qyf0YuS2HdKkWBsgQ7q_vP7iWE5pYYqfRkXdlQ4j6ne4TQvO5usFQs1vKgKYizlwKQc7w_aoGar7QkkGODCzHI-y95V0xrOJ9c0Gzuze_HCgO6z5i3dx3f7Tl3jopNnGf9JI4YD2EjCj6NXhcmndL7t2YXepIEmZ_fUSwo1n4mqNAN_3YTxVoDYn6UKx3zptM38tvW9NtSlbrIu89EgVYqvSLy1DoPEB33cmonJv0dFRm91fADsj3fc37Ot2T6HIHUn_tA1XKADsqEKF80h7Rk0n7-8Qe10e2w58OphkLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری متفاوت از خورشیدگرفتگی از داخل یک جنگنده و یک ایرباس!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141463" target="_blank">📅 12:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141462">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت خارجه: لفاظی‌های نتانیاهو درباره تعلق همیشگی بلندی‌های جولان سوریه به اسرائیل و نفی فلسطین را به شدت محکوم می‌کنیم
🔴
او در جایگاهی نیست که راجع به تشکیل دولت مستقل فلسطینی اظهار نظر کند
🔴
موضوع فلسطین همچنان مهمترین مساله انسانی و اخلاقی دنیای معاصر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141462" target="_blank">📅 12:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57340e99a3.mp4?token=btWrf1sBp-Lxz6BqGfP0E3Db6bQbrkoBhK3eo76eOvEsRUay7kTaJ6ONFII7NaUvXw96OoYhZCQP9J_pNpfkH8kAjnTkkyyOVTjJStFvRtwpUhX18R4dTSIj7kwVRt3MGQ6Au_7od37vJiXPq2dU83L3jysoJ1Tt9EKjbAYpheaGfsTvg9t119F41V3LM03Fr5knieqpt1ZN5k_jzT6SwH3kXCiIHZm625bRbzI6NbBu9tT7kXRwnwH6As_Qp5puqplIVfQDdHO4uX1TNPHQPlsX8-u4vSOAqRC3qhBCGwbZ-BlZpDOI7I--v1I6mZKuFg0ZnDZCKunXbyl6zeUn9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57340e99a3.mp4?token=btWrf1sBp-Lxz6BqGfP0E3Db6bQbrkoBhK3eo76eOvEsRUay7kTaJ6ONFII7NaUvXw96OoYhZCQP9J_pNpfkH8kAjnTkkyyOVTjJStFvRtwpUhX18R4dTSIj7kwVRt3MGQ6Au_7od37vJiXPq2dU83L3jysoJ1Tt9EKjbAYpheaGfsTvg9t119F41V3LM03Fr5knieqpt1ZN5k_jzT6SwH3kXCiIHZm625bRbzI6NbBu9tT7kXRwnwH6As_Qp5puqplIVfQDdHO4uX1TNPHQPlsX8-u4vSOAqRC3qhBCGwbZ-BlZpDOI7I--v1I6mZKuFg0ZnDZCKunXbyl6zeUn9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک عضو کمیسیون امنیت ملی در پارلمان ایران تأکید کرد:تنگه هرمز تنها در صورتی باز خواهد شد که ایالات متحده به شرایط تعیین‌شده پایبند باشد. مذاکرات بین ایران و عمان به هیچ وجه به معنای باز شدن تنگه هرمز نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/141461" target="_blank">📅 12:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141460">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYinOH5mcLAv1IA6sORccD8ZnwtCVPcvpRraQ4w3mS9mYaWlPWlAAhFrPGxWGBukyRsm7f9zpkxLR6CpuUtws5VD27APfikKr_ibssyuk5uajx_YRE7yNq-rCWL6DtrbZLu1g5pZe2TMgkOvjTKEQCf2FudAcXyQwTVoydbLgDwQqA4R18aJqn6tMSnJZ-wxGfgme4l7-qCPa2Xr3HZX1rFSAY_RmqlDAxgrQf4YQPSqDHC8ftnqHxMygvKGmHkSnxyVyEcW9nXxbETZn75T7lHRdfqXuI5fbf6lDMlEhgOAxTrrygFHSoXf1ffmv2RajQ76duu0GTnEWLUhZp6pZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای باری متعلق به ایران، در حال خروج از فرودگاه تیان‌جین در چین به سمت پایتخت ایران، تهران، مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141460" target="_blank">📅 12:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141459">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa62e58cf.mp4?token=ZJ-asZu1ZjmkJQxmCWNvLpyZA1VOWpGPbam-AyE2NhjxZn2PuzuDLV_pofgfpKuJ6dkO5s_TMCal_0dHPHEIiVLScMMIE1pRCV2wm5bgsFUdZlVPe9GYJEAxU7I12QEg86XC0dm5s_57kj9yxNO3UsNGbm4qBFB_0m2zEvNTyIV6J1pdljuiJ6L3VOEiapYg6BiP_jz3NttohB-un3OPgv1B7zcJo2DQt7ijWbk8Zp7OPE7tiZwHHAsBBW9kW8mi0kVfxC0ScMa5L3ct3HdpZVtuduSiLlOwwPlqK3zsE2FYd72-xINUlKNPIqTX_kQRug8sFsAhsW06ldRfaZNprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa62e58cf.mp4?token=ZJ-asZu1ZjmkJQxmCWNvLpyZA1VOWpGPbam-AyE2NhjxZn2PuzuDLV_pofgfpKuJ6dkO5s_TMCal_0dHPHEIiVLScMMIE1pRCV2wm5bgsFUdZlVPe9GYJEAxU7I12QEg86XC0dm5s_57kj9yxNO3UsNGbm4qBFB_0m2zEvNTyIV6J1pdljuiJ6L3VOEiapYg6BiP_jz3NttohB-un3OPgv1B7zcJo2DQt7ijWbk8Zp7OPE7tiZwHHAsBBW9kW8mi0kVfxC0ScMa5L3ct3HdpZVtuduSiLlOwwPlqK3zsE2FYd72-xINUlKNPIqTX_kQRug8sFsAhsW06ldRfaZNprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
ویدئویی پربازدید از پرش اسکیت‌باز اسپانیایی از میانه تصویر خورشگید گرفتگی
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141459" target="_blank">📅 12:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141458">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
بر اساس اعلام معاون وزیر نیرو پیش‌بینی می‌شود محدودیت‌های تأمین برق ظرف سه تا چهار هفته آینده و حتی زودتر برطرف شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141458" target="_blank">📅 12:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141457">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfCNkGn_cItT3FxuJWphhde6ZSxPO0dWQnJsmzOMRABcNAIzeZK6E6V4Rh7MYDBR8wY2UMCuk_YvLi43KgDhCIGn2xShI9Q_eCVRfX-7s5Oh5v2lLMMtSucQo7K3oPQz5a0eMSVlKQOyIRoAeoj_HhN2BtHELS2Z6ouidyZrNtSK1yZ8Rg4GrYajMBkbkqSumoRLBWwF0RxSmyGr9H7MhoEYMab-RIzO-pqWRW2wnQKIoT46x35mwS8s3PhbLYfoo_tBh-XOLJaxQo1Wuii-y7YXUKRyPK3l7dVPN8swEi136kz99Uc-Jzvr8DC-XQeSq8VU5cseyGb-Ix50n_6DAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
مردم من کنارتونم نمیزارم بنزین گرون بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141457" target="_blank">📅 12:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
مقامات آمریکایی اعلام کردند ارتش این کشور در مسیر خروج کامل نیروهایش از عراق تا ۳۰ سپتامبر قرار دارد؛ اقدامی که به حضور نظامی آمریکا در این کشور از زمان حمله سال ۲۰۰۳ پایان می‌دهد.
🔴
مقام‌های عراقی می‌گویند روند خروج نیروها و تجهیزات از اربیل نیز حدود سه هفته پیش آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141456" target="_blank">📅 12:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141455">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
الجزیره: تمدید دوره ۶۰ روزه آتش‌بس میان ایران و آمریکا دیگر کارایی ندارد
🔴
تمدید دوره ۶۰ روزه آتش‌بس میان ایران و آمریکا دیگر کارایی ندارد، زیرا ما با چندین موضوع فراتر از پرونده هسته‌ای روبه‌رو هستیم.
🔴
مذاکرات ممکن است طولانی شود، به ویژه اینکه در ماه‌های گذشته سخت‌گیری از سوی ترامپ و ایرانیان افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/141455" target="_blank">📅 12:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141454">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8cb1de271.mp4?token=aNOpyjBz4W-HY2IM-Xd6WlMb3xisz7PZQJRkeX-Tv4bIdBzXnQrlMGxJEwzuho1bGGYbOdWp3dtkAwFvWNPFXND137dxqZDw8JUqT49iQ_FCw74uDz9xng8U_eTv1b19NfJeya8bHh-xYOUtEjmig2Mleoao4oc1W3rBbf1Q0FTBr9LDwthtMk3iRR9kyVlOcXFdeTb_sbFRlN54IeCwKJBOQg_MZjNthFLKbOasz_aVYN0KnbBv_Odhcj2cgQCbwsiOVT-o1nNy5hVthVLQxdEZW5vMpmAUwy6h1qDqFr1yVTr70kK0sSUXa5r-KlrwLfyUwvDMOEoGAmO9OTlMhov4Pmf2XX1Od1hZkTI2BTOgPFZXUdHOour14nsTBg7104Gn4eiAR9PNZZqHoOn26SyM7WgNKWbumbz97PRiC9y7QKtEBga-nje3iKqFdDun1aNWinOpRuPQuTEFiOf9i9Qx3Eb4RdGorw1Gf7TdbV5Ye-RqmhS_O8zAZEVCO9DA3vB0yAPhEcSrmU9w0cyE74lzjVSDaX6pMx6bT8l-mAGU72kkN0xK45HSZxOl-3fMS0VTUqz_QTybIgPt5hEM4BcPf3izZ5_xaeedmm5zxaSROI_TR4llLlp1VP9CwbfJ-XwAdTmvjTvgCoKbUgWNReFCPAZu8eku9gdCalrHFzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8cb1de271.mp4?token=aNOpyjBz4W-HY2IM-Xd6WlMb3xisz7PZQJRkeX-Tv4bIdBzXnQrlMGxJEwzuho1bGGYbOdWp3dtkAwFvWNPFXND137dxqZDw8JUqT49iQ_FCw74uDz9xng8U_eTv1b19NfJeya8bHh-xYOUtEjmig2Mleoao4oc1W3rBbf1Q0FTBr9LDwthtMk3iRR9kyVlOcXFdeTb_sbFRlN54IeCwKJBOQg_MZjNthFLKbOasz_aVYN0KnbBv_Odhcj2cgQCbwsiOVT-o1nNy5hVthVLQxdEZW5vMpmAUwy6h1qDqFr1yVTr70kK0sSUXa5r-KlrwLfyUwvDMOEoGAmO9OTlMhov4Pmf2XX1Od1hZkTI2BTOgPFZXUdHOour14nsTBg7104Gn4eiAR9PNZZqHoOn26SyM7WgNKWbumbz97PRiC9y7QKtEBga-nje3iKqFdDun1aNWinOpRuPQuTEFiOf9i9Qx3Eb4RdGorw1Gf7TdbV5Ye-RqmhS_O8zAZEVCO9DA3vB0yAPhEcSrmU9w0cyE74lzjVSDaX6pMx6bT8l-mAGU72kkN0xK45HSZxOl-3fMS0VTUqz_QTybIgPt5hEM4BcPf3izZ5_xaeedmm5zxaSROI_TR4llLlp1VP9CwbfJ-XwAdTmvjTvgCoKbUgWNReFCPAZu8eku9gdCalrHFzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر جدید از آلودگی نفتی سواحل قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/141454" target="_blank">📅 12:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141453">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی مشهد:  حریق در اتاق برق یک مجتمع تجاری-اقامتی در خیابان شیرازی مشهد با سرعت و هماهنگی مناسب تیم‌های اطفا و نجات مهار شد و حدود ۲۰۰ نفر از ساکنان و مراجعان این مجتمع به‌سلامت به بیرون منتقل شدند.
🔴
این حادثه هیچ گونه مصدومیت در پی نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141453" target="_blank">📅 11:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141452">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtIzsr1IIDfgRdb6SYbyXzyeDWtFVhouv4nYl3nEsiloh0M66Io5s1hBi818pw2Zc5k_i4pXtztlUQR90tnAP7Izknrbuuc5V3dcSRZyXRFahgfBuPY_3iFDM_ElxH3xafWzbi9D_2T5RO7U9dLLbueYxvz4wdXYp99_GEpPQynh89w83m3spohgvL752SIyQXeEZiFsTmuUifVnXieCjJAYJ9IH8qi9LkKO0CG0tBfFDTMpXL3Nte88q212FfjTqI7IKEoNM8XrV0-PoLbuko-vwnLiDU3X0FBByOnrGu8UQZUg6jP-5mOLGkrxonGHdHV5y2WyS2juA7ykeYJnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: آمریکا در قبال تنگه هرمز، مرتکب اشتباه محاسباتی بزرگی شده است
‏
🔴
آمریکا مدت‌هاست که به دلیل ضعف اطلاعاتی، دچار اشتباهات محاسباتی مکرر می‌شود. جنگ علیه ایران نمونه‌ای روشن از آن است. اکنون نیز در قبال تنگهٔ هرمز، مرتکب اشتباه محاسباتی حتی بزرگ‌تری شده است.
‏
🔴
بدتر از اخبار جعلی، اطلاعات جعلی است. مراقب باشید.
‏
🔴
الله بزرگ است، بزرگ‌تر از هر قدرتی بر روی زمین. ما بر الله توکل داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/141452" target="_blank">📅 11:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141451">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msl9Sw0pn0OlFd00K2cfE3r6VADkZXl1reCR2tFLU1Yhb0cDuWYxa16U3zCE4bYhhs9Rrml65QyT7eqACWTozJdHpP8MHzIzstohrpMi8HxCt6iPirmkRwNb89epe03UZ9K23K6n504B2D6gX5ce4NUtJBHOubovGer5fkPdOMuoaz7QFGbXuXjelWZ6OOgQ-Hdjv1UpsBy2zdb8AkwS4OYCzergXtmL6W3zE64m_jhwAU95crOr0HLQddkiostZe1qOsQtPF42aqPIrzjNx-9f8xwq_w4IUF9ucyqmyXDvqPLPaa0IUFgNg695vjrvKBpUbxIXSWpLEHVyK8LTnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یورونیوز: نفت متعلق به کشتی تحریم‌شده «کارولین بژنگی» که به روسیه وابسته است، به سواحل عمان رسیده است. این کشتی که نزدیک به یک میلیون بشکه نفت حمل می‌کرد، در ماه ژوئن در نزدیکی جزیره قبیلیه منفجر شد و روی صخره نشست. مقامات گزارش داده‌اند که آلودگی در راس مدراکه رخ داده و جزیره مسیره را تهدید می‌کند؛ نشت نفت بیش از ۶۰۰ کیلومتر مربع را در بر گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141451" target="_blank">📅 11:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141450">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d7922013.mp4?token=ejV33beWrLqCRP8HMGyxuYP_HemxcJgRtSOUG33TDfPW_hQuGZHUZ5Cd_cuN2g3gNr_g6gaZmHLmKfHbbUdIMjxdPMkYcT84XRDeGgDOFbKx7oJ6LJ44ZdbcC2b5lFOCOSX23MNyYN8ygZXH0Cbn-bV5Q8ZTF1_xVq5LxS2x62gUmNdYaxWQz3o6jPMcpWyKMNgx8T7PKobWB9SWQ4IUFv_7ZXCEip5eZ0sJgIPyTAUYynGXprUzfV8Djp7T2XyRsDWue3r9oDJf3JvWcYZyckqJXoRHS4d12rgM5-EBx5S9yDEVUiDJ_H_kH026SzCjJTQBjFR7Rr1ZmP7d5yXScw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d7922013.mp4?token=ejV33beWrLqCRP8HMGyxuYP_HemxcJgRtSOUG33TDfPW_hQuGZHUZ5Cd_cuN2g3gNr_g6gaZmHLmKfHbbUdIMjxdPMkYcT84XRDeGgDOFbKx7oJ6LJ44ZdbcC2b5lFOCOSX23MNyYN8ygZXH0Cbn-bV5Q8ZTF1_xVq5LxS2x62gUmNdYaxWQz3o6jPMcpWyKMNgx8T7PKobWB9SWQ4IUFv_7ZXCEip5eZ0sJgIPyTAUYynGXprUzfV8Djp7T2XyRsDWue3r9oDJf3JvWcYZyckqJXoRHS4d12rgM5-EBx5S9yDEVUiDJ_H_kH026SzCjJTQBjFR7Rr1ZmP7d5yXScw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه کافه مذهبی با آپشن‌های فوق العاده توی تهران راه اندازی شده:
اینجا آمریکانو نداریم، فلسطینو داریم
نوشیدنی‌های خارجی مثل کوکاکولا حرامه.
موقع اذان، توی محوطه کافه میتونین نماز جماعت بخونین.
پرسنل قبل از پخت و سرو غذا و نوشیدنی، حتما باید وضو داشته باشن.
کافه، نزدیک مزار شهداست و میتونین دیتِ خودتون رو اونجا ادامه بدین.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141450" target="_blank">📅 11:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141449">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141449" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141448">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای زمین حین خورشید گرفتگی اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141448" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141447">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ny0p6QLTEmZDIbxJMEIpuNnaGxtk2bOPXoZuhlq20qMiPLZKRi6BOVOJEpKa-6xFDoNW4RQZkmhWie-H_O6CVvbGAGrqJAbc9l1Z8SZeWOvMX43BUrJ9zqlIUrg9ShN9ptPeQphNmBCuRmScdfMnEIe63kNUJyyrREGQCwDlrKC1xygbixFRJZDXhyHFrXuAaGwCcgdbcSWKD-PDoFNBayZCcNq3l_PLW0heHi0QwdCD1eSRvpkT-VLntAhsChAKRJ_EjQh61IdRHB3ynXPJa1gM3qLJ1IA0de8eug71QAVioi6klF5A2Fa9jjT0nW23ENSZwsTOwZohUEO9rKFKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلمبیا رسماً به ائتلاف مقابله با کارتل‌های مواد مخدر قاره آمریکا پیوست.
🔴
این تصمیم پس از دیدار پیت هگست، وزیر جنگ آمریکا، با وزیر دفاع کلمبیا در پاناماسیتی گرفته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141447" target="_blank">📅 11:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141446">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2711d095b9.mp4?token=nJHxoo6GJWoIxkcMvyIYxvtAdel-EVbfKJYWFFdeDG3tyKPTMs4PLOwc3BBMeC6Gzo8irvFhrY5um6rXleXb-YtYUPmIFfxiuwEscHsSsGAYnTFNpQjFxbPjzlRSwyDgoVLTqJjEsBBAzXckfFvNMvRY0b5QlYwviMF58kYFSlNsunrlll5k4zSuC07yyT7P03uwMgYim-AF4_jVFreadfBbY22zRjWrXVWU64raIVQCeJ3Fwlap348cZt3W9ClHFDgPh2KH-7yeWY-p5-USfEvbru-Tz9U3uccD6WwlAbzwhZ_hQIEu0P310PSo7yex5gdGugGVmzKdVmH44g8sSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2711d095b9.mp4?token=nJHxoo6GJWoIxkcMvyIYxvtAdel-EVbfKJYWFFdeDG3tyKPTMs4PLOwc3BBMeC6Gzo8irvFhrY5um6rXleXb-YtYUPmIFfxiuwEscHsSsGAYnTFNpQjFxbPjzlRSwyDgoVLTqJjEsBBAzXckfFvNMvRY0b5QlYwviMF58kYFSlNsunrlll5k4zSuC07yyT7P03uwMgYim-AF4_jVFreadfBbY22zRjWrXVWU64raIVQCeJ3Fwlap348cZt3W9ClHFDgPh2KH-7yeWY-p5-USfEvbru-Tz9U3uccD6WwlAbzwhZ_hQIEu0P310PSo7yex5gdGugGVmzKdVmH44g8sSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
👈
عضو هیئت رئیسه مجلس : ما حریف مافیا خودرو نیستیم استیضاح وزیر هم چاره‌ساز نیست
🔴
محمد رشیدی عضو هیات رئیسه مجلس در گفت‌وگو با رسانه تصویری «آن»: با وجود سال‌ها قانون‌گذاری برای ساماندهی بازار و آزادسازی واردات خودرو، موانع و تعرفه‌های سنگین همچنان مردم را مجبور به خرید خودروهای داخلی بی‌کیفیت و گران کرده است.
🔴
ما حدود هفت سال برای اصلاح این وضعیت تلاش کردیم، اما صراحتاً اعلام می‌کنیم که حریف مافیای خودرو نشدیم؛ حتی استیضاح وزیر صمت هم در گذشته نتیجه‌ای در این زمینه نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141446" target="_blank">📅 11:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141445">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DznwD4N0n56nZy4kqa3NzGuBxhJEvnhDpOw7LA5pgm3fisCojAu57MDPYAxL9_1gxXNjUVI-1EaGJZifIBOLlESCtKSVyrhxOzEoY8T9xBBVlaGV2qau1QbvbyWQaabgN_ZVzGqsL6evWqVsdyNoHZH1m-I7rUPqidzfyuoTLQaTDihKQemf04c8FDr5mE0paSVdOUukqeqjnwu8c-HcBtM8pdWoz-_nnpPWzWxhuw10V4z9IbjLg1CvDqGux9-8OBAtVoSSFhs53BA4yE1qwUbZXry-PP7lqEuovl7slsmMARRNYQVxRgwwRjNGfzticksI9ybvvsVKGNPtmYes_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتورهای دموکرات خواستار تحقیق درباره وضعیت ناو هواپیمابر آبراهام لینکلن شدند.
🔴
پس از گزارش‌هایی مبنی بر وخامت اوضاع تا حدی که چند ملوان اقدام به پریدن به دریا کرده‌اند، سناتور ریچارد بلومنتال نامه‌ای به پیت هگست نوشت و نگرانی خود را ابراز کرد. سناتور روبن گایگو نیز خواستار بازدید رسمی هیئت دوحزبی سنا از این ناو شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141445" target="_blank">📅 11:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141444">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فرشاد مومنی، اقتصاددان: ابرتورم در ایران رخ داده و وارد مرحله فلاکت شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141444" target="_blank">📅 11:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141443">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff225435fc.mp4?token=VnSxKCAvmDKJzPiZjEDL5VPUbNb7IahKQuK2QwsC1WoDiSk4Ahl-F0-U3WpaaZnWwFD2ihoaLzycwGp1_ce5lfhk90cdUisYj3r8r_7wJI3aSOIf3FH2u1hQHs7UndpyKjI949CBuqe1tJsv5_PhrUoHVlf05Zurtc15X5MSYQFBCJ73DBis4KgLqCLALw1E8HbGeMrvjrQPFC0a1L41uk8VHSK75JdZyS5lToZjjor9TrLEG3XMLLx936MJzJs-ZIy99NQo7Bix8H-A3BgXg2ur4pzqdGBFg6FD5udFA_8iUcbRa4IaK-Fpv6f-QimKRHv67EFOGxaGd5nuaLecGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff225435fc.mp4?token=VnSxKCAvmDKJzPiZjEDL5VPUbNb7IahKQuK2QwsC1WoDiSk4Ahl-F0-U3WpaaZnWwFD2ihoaLzycwGp1_ce5lfhk90cdUisYj3r8r_7wJI3aSOIf3FH2u1hQHs7UndpyKjI949CBuqe1tJsv5_PhrUoHVlf05Zurtc15X5MSYQFBCJ73DBis4KgLqCLALw1E8HbGeMrvjrQPFC0a1L41uk8VHSK75JdZyS5lToZjjor9TrLEG3XMLLx936MJzJs-ZIy99NQo7Bix8H-A3BgXg2ur4pzqdGBFg6FD5udFA_8iUcbRa4IaK-Fpv6f-QimKRHv67EFOGxaGd5nuaLecGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
لحظه‌ی خورشید گرفتگی کامل در تاراگونا، اسپانیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141443" target="_blank">📅 11:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141438">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwIwUOu_ZWuiFyOKW_fnmOArvwHzuvA0T7yu8_FaskH1gaiv7IOfFogLH9aI26NoZf62mYOiajyXePDhDnS9v4qUbT50oMdVhcq7QY2Qz8mPnLOOPcOX-FKoZ5PY9ilo11_xioEdYZEit8PN2PHT83Fl4G0_hZ1xVLKcGcToI8LtABazDxIqvMXuX_QrS7AktfQXs8nw3NLL9JDuxgYsE_I1j7WKeuUPIBh-D7k4qtydhsuew360PVBFnQDPHH3uRCsYgTVgRGQ0lLIHgiqqiSAIkvy1krP5KoIa6J2PGgb8_WJGn0-1SngmWIT93LWFQMidOoPesKa2sQd2w4XkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0vaaRA7aHQ04SPHSmZA3sBsCAoAbmSptmQW_k-atvmzlkPuWrLIOmutTzJeAMWGN1a4ZEj0JNWluwR_6I73T6mDM5NLtQTU0-UvMVwSRx9yTgh2R8DHuzqlMkUdTDH6o7iKTEJ10CSiqlxHBuyAVlL_AqoML7qmAK8n4uV1oRdnA77x5XHZSumx8ah6zLwulQPU9_9VkkOYrjktvGCCABS9wHPuj9DyBbeFYILetG_j121uP2wu9VASIgCbriiXvU46yE0CrfeZPwDuPaaLbRNS49Md0oLKAXR0fOkl1abBeU32qBl3skMlOqUq_qzLAIYYEu4Ma_umACY3QZReDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAMmxw4kVivwQ1Y0Omb1oZIOk3H6-fSLtgeDX7vMLDpN6x6owPo076xhg6AQ3X9qdCHNEhZ4JWQ9lQuwQX6Rvx0Sy2-1kUinMn8tx-8jCT8EQZzY52xYAlYEsuIlwHz_dzPQDBl3fZM8oULKB93CiizUd0Ph1xgkWduGePX1czoerCTUxqwAM77CcxngNa-OwJsOFhMCaiNEhya8toR8QOsQTB1TcE9H7kJ3LnndZZZxx04OXdKY7STW_l-AJSppDFZTL47ciDP1p8E9zGYBBoOmw92Y57c9_Gtr2UMyxenKybc2oxbzZhUadNEI2lk5ar4PR-R4EEnT9kugag6EJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XbiLZAzqbAcflJLyIdYMuVv9F8rTRLI6Q0o2HYwvDWGG7cmMfOjb2VUrg10OEPi__HawrsCDP5kLgqNlelaRpvj1HDMtq1hd025FDW_T0iv8uiPO7OjYmxWiXNptPFtl51ttJb_AJk9WuHzip4ZalZ93E4730KrUkThyBb76CUE6Uj3sxIk2RsJZ9pqcsa-S6rOr_pZ3KWG5edGLDYE3GwNIiSx3dzXDPjMo-40RSJ2MkZspGU5Vx8qPH3pCMoxsJJgFuINux5jTMvQ4iitwLM5OT3iQKotqjBwvrjKWen6nvl9-zHI2u8UzMttfvoTUZmsh-qgfc46nU7TGH4g7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KScl5IgNBX0nTpP22FjbT1INOQKPonqEia49aiI_8E2tvrlrPXlNCcdbE_Uw2Oz0By34xJ6V7JlT3925Z8hFrFshHKIhLOAUU3pqIe40U5yaeL-f1lPk5-VH2gydl393cfV7XRlVbET5V28ypbweF-jfBVGiR5BX3ZXQLNGN5TOvbHRN3GPZygIzTmFNgC2TOsTx2AytyhptLFJoXbgl8_wCMN25uTreJWd_lbohJNivpPts9qfSw_m7-xTqULKFejPSgJgJ7cMiUo0HeYADbo_pxJBMYtZT4rrGGsnU3ZqSaYS3o_lvl_42US_kddSuEOROSLObjqRYPvOze5IrRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از خسارت به تأسیسات ذخیره و بارگیری غلات در نووروسیسک پس از حملات شب گذشته اوکراین حکایت دارد.
🔴
همچنین، یک نفتکش در تأسیسات انتقال و بارگیری نفت نیز هدف حمله قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141438" target="_blank">📅 10:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141437">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏
👈
هواشناسی: گرما تا یکشنبه در بیشتر مناطق کشور ماندگار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141437" target="_blank">📅 10:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141436">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7nMd1gvXARKkrcbXxZYrOmGlt34KzIuqyrdVjB9_YW2gRC3_d8r_IjFix1gxaYZp5HDrjuTD9JxaGUL7EbW2DblID70ztXPJ3tZJjBRl_mdGB_HihTYYJmB74eyM9v323R_lQl46c1p4-Y-MfMo25-QYtq_C0aeSFwSwy-33rvRI1iiHHGYdBtczxfaQ47Ekh6UrX5YyUmuJRlopQwRj4yhrLnFMGcaX-7bqSmILoNzcccPiUdCdxqIB1mjsI4oqI24WAfYDxvSA0vDlBlwyXUhhvVNODkm3Lk2pxxtOPKyGSAP8-xSYfKR60vns4eAuvQlSiRCtN7_5aa1tKkmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست: همه گزینه‌ها درباره کوبا، از جمله اقدام نظامی، روی میز است
🔴
پیت هگست، وزیر دفاع آمریکا، با اشاره به قدرت نظامی این کشور گفت: «هیچ‌کس دوستی بهتر از آمریکا و دشمنی بدتر از آمریکا نخواهد داشت. بهتر است با ما درگیر نشوید، اما وقتی مشکلی پیش می‌آید، ما نخستین کسانی هستیم که وارد عمل می‌شویم.»
🔴
هگست همچنین درباره تحولات ونزوئلا مدعی شد: «قرار بود سامانه‌های پدافند هوایی روسیه از کاراکاس دفاع کنند، اما کار نکردند. محافظان کوبایی نیز قرار بود از مادورو دفاع کنند، اما نتوانستند.»
🔴
او افزود: «اکنون شاهد اخراج کوبایی‌ها و روس‌ها از ونزوئلا هستیم.»
🔴
وزیر دفاع آمریکا در ادامه درباره کوبا هشدار داد: «همه گزینه‌ها، از جمله اقدام نظامی، درباره کوبا روی میز است. آن‌ها قطعاً حریف ما نیستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141436" target="_blank">📅 10:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141435">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزارت دفاع روسیه: سامانه‌های پدافند هوایی ما شب گذشته 362 پهپاد اوکراینی را در مناطق مختلف کشور سرنگون کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141435" target="_blank">📅 10:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141434">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
‏فرماندار جاسک : احتمال شنیدن صدای انفجار کنترل شده مهمات  در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141434" target="_blank">📅 10:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141433">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
به گزارش برخی منابع عبری: امارات ۱.۵ تن طلا که از اموال بلوکه شده ایران بوده رو اورده تحویل داده تهران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141433" target="_blank">📅 10:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141432">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
شرکت امنیت دریایی امبری: عملیات نجات یک نفتکش آسیب دیده در سواحل عمان
🔴
شرکت امنیت دریایی امبری اعلام کرد: ما در عملیات نجات یک نفتکش آسیب دیده در سواحل عمان مشارکت داریم و کشتی‌های نجات در مسیر رسیدن به محل حادثه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141432" target="_blank">📅 10:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141431">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نقص امنیتی در پل ارتباطی میان XRP Ledger و بلاکچین Coreum باعث شد مهاجم با ثبت تراکنش‌های بدون پشتوانه به‌عنوان سپرده معتبر، حدود ۲۰۰ هزار توکن XRP از ذخایر پروژه خارج کند.
🔴
تیم توسعه‌دهنده اعلام کرده کد آسیب‌پذیر شناسایی و اصلاح شده است. این سرقت طی ۹۷ دقیقه انجام شده و موضوع نیز به مرکز رسیدگی به جرایم اینترنتی FBI گزارش شده است.
🔴
یک خطای نرم‌افزاری کوچک، برای مهاجم به در خروجی یک خزانه دیجیتال تبدیل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141431" target="_blank">📅 10:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141430">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImYNTHCuNDZacVPrO3tOh3iQIAYGGTAl-Gzc4H2j4xliacj7lKgOPZIjmCHeMZ7WOqqcQenwEH6PjeJWrtvZ5j9k5y2F1fTT_d9jyeIfFMiJg09I9lZbJOXEjPcGjJM2T14RynxMCYlh1u8AwENNmxVxnR-8K4ZAjEAXncoR4HpfQc9fdjYd6qfADYt8vBXGK_Jt7EWF4KDcW9ohyH5Ebv2VhaXmR5UFqmKx7s-bhEXic-0J2DQQtlqdBtKJUhLPYJZjDOC8vaHqlxrRhstZPzOI8pOICUH4ZT0RSnN-03eu57NxifMgLJnQ8w5V18I68mIuhZjLLA92BGfxIyqyRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
تصویر روز ناسا؛ خورشیدگرفتگی کامل در اسپانیا
‏
🔴
۱۲ آگوست ۲۰۲۶
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141430" target="_blank">📅 10:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141429">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17fcfa2fa.mp4?token=Z7zqaMde4lIgjsU1bHXYkNUXm7XQlQ8gkIMnMtXs521tBFv_jK4TvEYR_4t9PNXykw5wxuWIrbwqbtZ3sR9J3v2aAr1qbH-1MHB-2RzlpCS5eBtGv3h9ev6b868civJY49svbnwooX-h3jPgQR8-pccb-8mr7Bvi6vt9TA3pIpXGqW_2R4wc9MFdTxHfhutr5naMrUNBvj3dEn7BsA8n3R1jWN-ePTBZaa6op1I5v3iuscHtStNS8YRpgyVPEIXZ9qqy_L7yMGRmUFEwurHAqb4w2FY526mgl408HZHIwm4Mkn7gKANNh2sou_9uQNPfXgKvKVsTqLPMycyH36O8hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17fcfa2fa.mp4?token=Z7zqaMde4lIgjsU1bHXYkNUXm7XQlQ8gkIMnMtXs521tBFv_jK4TvEYR_4t9PNXykw5wxuWIrbwqbtZ3sR9J3v2aAr1qbH-1MHB-2RzlpCS5eBtGv3h9ev6b868civJY49svbnwooX-h3jPgQR8-pccb-8mr7Bvi6vt9TA3pIpXGqW_2R4wc9MFdTxHfhutr5naMrUNBvj3dEn7BsA8n3R1jWN-ePTBZaa6op1I5v3iuscHtStNS8YRpgyVPEIXZ9qqy_L7yMGRmUFEwurHAqb4w2FY526mgl408HZHIwm4Mkn7gKANNh2sou_9uQNPfXgKvKVsTqLPMycyH36O8hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمان و عربستان سعودی اخیراً «کریدور سبز امن» را راه‌اندازی کردند که این دو کشور را از طریق الربع الخالی به هم متصل می‌کند.
🔴
این مسیر شامل حدود ۵۶۴ کیلومتر بزرگراه در سمت عربستان است که با هزینه‌ای حدود ۵۳۳ میلیون دلار ساخته شده و برای کاهش هزینه‌های حمل‌ونقل، تسریع ترانزیت کالا و ارائه یک جایگزین زمینی که گلوگاه‌های دریایی کلیدی را دور بزند، طراحی شده است.
🔴
پروژه بیش از ۳.۳ میلیون ساعت کاری برای تکمیل نیاز داشت و حدود ۷۵۰ دستگاه سنگین که به‌طور خاص برای شرایط سخت الربع الخالی انتخاب شده بودند، در آن مشارکت داشتند.
🔴
ساخت این پروژه نیازمند حذف حدود ۱۵۰ میلیون متر مکعب شن، پهن کردن ۱۲ میلیون متر مکعب مصالح محافظت‌کننده از شن و استفاده از حدود یک میلیون متر مکعب آسفالت بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141429" target="_blank">📅 09:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141428">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
واشنگتن پست: تحلیلگران سیا «اعتماد کمی» به اطلاعات اسرائیل در مورد توطئه ادعایی ایران برای ترور ترامپ در ترکیه داشتند، اطلاعاتی که سرویس مخفی را بر آن داشت تا یک عملیات امنیتی فوق‌العاده برای پنهان کردن خروج رئیس جمهور از کشور انجام دهد.
🔴
یک مقام آمریکایی گفت که گزارش‌های مربوط به تهدید جان ترامپ «از اسرائیل سرچشمه گرفته است، نه ایالات متحده، و اعتبار کمی دارند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141428" target="_blank">📅 09:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141426">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb171b134.mp4?token=TeIutK9BmQ1WbtFBe4lNI8vjkIO83fIQk_tRe04Ymqe6cnHX_BOtvx7lFztadzwLeHVhKB_9ojgVdAgenlDvzuntBIjX4u3k9IaZDDcj7KtsV7QS-qJR3Sg2JWPTwLVp97G7XCXKtoLJ4DoFDLSls_w8XwEojzZU90wzELT6IX6DjlZ_tcV1bm7XokR8_6Hdu97vdIqf9vTDkJ8UDuvAUu5HTKb8Ic8K6ywCEMmdGgp09vFZw6FcKCoQorQ1vJKH5xP7s8e5RpUBXnEjyK2yItzb9xobhV1Vf6OuT9jVf4ICbQ_PynAOLVJ_WJfD4wjdSiIdt7LkL_Kr-g95RdAZSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb171b134.mp4?token=TeIutK9BmQ1WbtFBe4lNI8vjkIO83fIQk_tRe04Ymqe6cnHX_BOtvx7lFztadzwLeHVhKB_9ojgVdAgenlDvzuntBIjX4u3k9IaZDDcj7KtsV7QS-qJR3Sg2JWPTwLVp97G7XCXKtoLJ4DoFDLSls_w8XwEojzZU90wzELT6IX6DjlZ_tcV1bm7XokR8_6Hdu97vdIqf9vTDkJ8UDuvAUu5HTKb8Ic8K6ywCEMmdGgp09vFZw6FcKCoQorQ1vJKH5xP7s8e5RpUBXnEjyK2yItzb9xobhV1Vf6OuT9jVf4ICbQ_PynAOLVJ_WJfD4wjdSiIdt7LkL_Kr-g95RdAZSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه ایران، اسماعیل بقایی، گفت که حفاظت‌های زیست‌محیطی باید بخش جدایی‌ناپذیر هر چارچوب آینده‌ای باشند که تنگه هرمز را اداره می‌کند، با استناد به آلودگی‌های نفتی اخیر در سواحل جزیره قشم.
🔴
بقایی گفت که شواهد اولیه نشان می‌دهد که یک کشتی باری خارجی منبع این نشت بوده است و آلودگی در سه مکان ساحلی و در بخش‌هایی از آب‌های اطراف شناسایی شده است.
🔴
او گفت که دهه‌ها آلودگی و فعالیت‌های نظامی باعث خسارات زیست‌محیطی به ارزش تریلیون‌ها دلار به مناطق ساحلی ایران شده است و استدلال کرد که تمام طرف‌هایی که از حمل‌ونقل دریایی از طریق تنگه هرمز سود می‌برند، مسئولیت قانونی و اخلاقی دارند تا به تعمیر و جبران خسارات وارد شده کمک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/141426" target="_blank">📅 09:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141425">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThTMmdLWQ_zmATngKBrJnC6YIxznJpL4h59App4_ey1aAy-jkbmRAwQk2fi2S-RiIAw9jasatSphgjG8pEIOKS47U4Q2FiPJk52VHxSyXy0Os3ic9r9VaaMeCK5YWkN-d4YTlJWLNoWkX_CfJVcYv5eKSoi8yG49OZy3Gf1MUZublru9-KNnSutjZ1RK2sJj27bqqYccLDuuRtDByD9rQAL9LexaKnsNITmTA9wUCT-A2bfMzvmzkD0qC-t4eyWeJZ1cBDvrSQ9umrfKrp2iRBUlBXa69TksTZRAJVGU2A17FRtByYU9UuvMjIItIT9hZPw2qlhDjpPBqta4r-uGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مرد ۹۹ ساله ایتالیایی نامه‌های عاشقانه قدیمی را در یک کشو پیدا کرد که نشان می‌داد همسرش در دهه ۱۹۴۰ رابطه‌ای خارج از ازدواج داشته است.
🔴
او درخواست طلاق داد و به این ترتیب پس از ۷۷ سال زندگی مشترک، به عنوان پیرترین زوج تاریخ به طور قانونی از هم جدا شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141425" target="_blank">📅 09:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141424">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA2f-24nT_ssg8G-XqOyOi29QjiERuUq5bQVZEZO2xJOFk19RALOZxnWn6fzctCNNv9UTa3jRbPvQwWmA3jZm36lXFhj-JUW7OsLnwdCrd-_TnbKowHRrfCSXalfl7BtCJZKjzsMOyaSVsYIyn1ZOH372HZrJEFLu6wvA8o93X9wrlVsXP7rIEuQIiF2YSBd02_RH6dEUMeoXd5MbiaKdKJSl1-ox_7N15i5W9PWIO_Q-smBJtICFH2f8EaFuViInaNuYBzUGxffxlw1lFSIJBPJj8UjLqHQjLGpwd1B8OYfvNhhtPXgwoWFLPCr0nUFGgst394SiP4GLvsOAI10uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت حمل و نقل مصر:کشتی "تهامه" (TIHAMA) که مورد هدف قرار گرفت، در سواحل یمن قرار داشت. این کشتی قبلاً هرگز وارد بنادر مصر نشده بود و در مسیر سفر به مصر قرار نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141424" target="_blank">📅 09:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141423">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsBuFSw4rY39-NYTbQe05aLMvC3zKsnyxpPsb4_nGmjERnRx8TEZemGf0hpWB4NkHX2jbxh0tUdeguOtWAI3-53Ayyv6l99neNrpAtPOYQrI5Xsf1vwSieTEmwzQk8J0ywsxYX7l2JNq2HoH_-hQguEHFdDWuqXVJoO3aZ4llPmSITxfrth3TVq5sSxdWZ4cPldPnrFukRQEOIOjdHCbypLbxvfN_L4kxC0kuNZTO9AgqukI5chXZYMdkmj2xY33uOhE-2gqWCQQqJhlPDSBYrbVUwCeoxjtTNzOWUUiROD9gPEs9SjQ7dQ5WtXKBg2e7KCPYdFTyfnaiOWn5pCkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلتمن مدیرعامل OpenAi:احتمالا تا 6 ماه آینده، Chat gpt بتونه صفحه نمایش موبایل شمارو ببینه و بخونه!
🔴
به این صورته که کارایی که در طول روز با موبایل انجام میدین رو میتونه تحلیل کنه، مثلا وسط چت با پارتنر یا رفیقتون، کمک میکنه چی جواب بدین.
🔴
یا اینکه سر کلاس آنلاین، جواب معلم رو چی بدین؟ حتی می‌تونه تماساتونم ضبط کنه و وسط مکالمه کمک‌تون کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/141423" target="_blank">📅 09:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141422">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1mn-67bwFOyWRSX8mlvL5tEMNTlBiVc9RYGAstmgV3JDHShwSpjzkbcYZMhW2YEBM63xy2EWcEGKupcv_DGgjjn5Yt_jLRdiakhv8vBEKEDivxUHi8uWRizOLDM5L-i8yWQZiHNB1-4x-R6QfEFd_OVpZELrZnY6BSQcI5NzcDoT8nyxGYqsTLzktn35XJ5YKkXW8XJ5ejMU2DsXZyT1HlmU-H-TfGn0gE7pdiPpCWi1h1Cv46z3vfdD6Fr0yKfikvpcJ8iblk0OxyfWS2L8jBBIQbWvXO2Hz_lkaVaUTgahlOhcbS9LJlDu66ydBenl0NQNPOEz17wYZBuMtRVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلتفرم ایکس حساب یحیی سریع، سخنگوی حوثی‌ها، را مسدود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/141422" target="_blank">📅 09:24 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
