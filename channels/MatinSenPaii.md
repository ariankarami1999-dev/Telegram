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
<img src="https://cdn1.telesco.pe/file/huHc2qn_DiZxymcBZFFofOwUaXJWkrkssmXCWt-O1uEiceDEeoNgEXuFBu_qd4eUYWF0meipk_KSKar1X9lEWD9D9DPUhPmGLIK2TrQiR79i0yWhiqO4dgdhrcqfVtOQ5ttLUMdwmMNwkgvN-UdjICm4FcYy8x-zwMEaGbJhzxQJKsdjbCb_iipsPS_zTjFV1b0obK0J7ljpOijE1PSAkMkrW43adCtbxEfACQHbV3mvYS62tfR7AzsHpRImeGitvUv18T8HIkkIPdeBVUi8Wsix9oOvcuL__DfYjhiCTmq_jMcLNLHVlMdfNfeVZIISTN83d52Xilby9lMGtnxKyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 00:06:01</div>
<hr>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت
توی 18 دقیقه
هیچ ابزار خاصی هم نصب نبود جز ffmpeg
و اینم پرامپتش:
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
که یه کم بالاتر داده بودم.
روشی هم که ساختتش اینه:
۱. هر فریم فقط تابعی از زمانه
کل ویدیو یک فایل HTML به اسم showreel.html هست که یک تابع renderFrame(t) داره. این تابع زمان رو به ثانیه می‌گیره و همون لحظه رو می‌کشه. هیچ حالتی بین فریم‌ها ذخیره نمیشه و حتی موقعیت ذرات هم مستقیم با فرمول از t حساب میشه. به خاطر همین میشه هر فریمی رو با هر ترتیبی دقیق رندر کرد. تیکهٔ «Rewind» هم ساده بود: فقط renderFrame رو با زمان‌های قبلی صدا زدم.
۲. حرکت‌ها از چند اصل کلاسیک انیمیشن میان
- Easing: فرمول‌هایی مثل outExpo برای ورود تند، outBack برای کمی رد شدن از مقصد و outElastic برای حالت فنری.
- Squash & stretch: نقطه موقع افتادن کشیده میشه و وقتی به زمین می‌خوره پهن میشه.
- Anticipation: قبل از جمع شدن شکل، اول یک لحظه بزرگ‌تر میشه (inBack).
- Stagger: حروف و ذرات هرکدوم با کمی تأخیر نسبت به قبلی حرکت می‌کنن.
- Motion blur ارزون: به جای نقطه، برای هر ذره یک خط از موقعیتش در t - 0.02 تا t کشیدم.
۳. تکنیک هر صحنه
- ذرات: کلمهٔ «FLOW» رو روی یک canvas مخفی نوشتم، پیکسل‌هاش رو نمونه‌برداری کردم و هر پیکسل مقصد یک ذره شد.
- سه‌بعدی: بدون هیچ کتابخونه‌ای. چرخش و projection پرسپکتیو رو خودم با فرمول ریاضی نوشتم.
- مایع: با metaball ساخته شده و داخل یک WebGL shader اجرا میشه. هر حباب یک میدان r²/d² داره و جایی که مجموع میدان‌ها از ۱ بیشتر بشه، سطح مایعه. نورپردازی براقش از روی گرادیان همین میدان حساب میشه.
- جلوه‌های نهایی: یک shader دیگه chromatic aberration، grain فیلم، vignette و فلش رو روی تصویر اضافه می‌کنه. شدتشون به ضرب‌آهنگ‌ها وصله.
۴. صدا هم کامل با ریاضی ساخته شده (audio.mjs)
هیچ فایل صوتی آماده‌ای استفاده نشد:
- Kick: یک موج سینوسی که فرکانسش سریع پایین میاد.
- Clap و hi-hat: نویز سفید که فیلتر شده.
- Reverb: با چند delay که بازخورد دارن ساخته شده.
- Sidechain: صدای بیس موقع هر kick کم میشه تا ضربه‌ها گم نشن.
- زمان‌بندی صدا با تصویر یکیه (۱۲۰ BPM، هر بیت نیم ثانیه)، برای همین همه‌چیز روی ضرب می‌شینه.
۵. رندر نهایی (render.mjs)
اسکریپت Chrome رو بدون پنجره (headless) باز می‌کنه و برای ۹۰۰ فریم (۱۵ ثانیه × ۶۰ فریم) renderFrame رو صدا می‌زنه. هر فریم به صورت PNG مستقیم به ffmpeg فرستاده میشه و ffmpeg اون‌ها رو با صدا به MP4 تبدیل می‌کنه.
۶. کنترل کیفیت
وسط کار فریم‌هایی از هر صحنه رو رندر کردم و کنار هم گذاشتم تا ببینم. صحنهٔ سه‌بعدی زیادی کشیده و شلوغ شده بود، برای همین طول ردّ حرکت و زمان‌بندی تبدیل شکل‌ها رو کم کردم تا واضح بشن.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UogdDOYR_XzMnsXIN0hLkzMuy5E3QYN7GK61B5-T6Lki43nMN9Iy9IG37CftXcmOtKTeWfFVKqupNh1ftg0ccgldKyxqvtoG4ifKdrTn5_saybUv5D9Gse1Vd3_x5RvJ29pzpDXtIulQgHDSj17wEWmn75ewuOmBETYLCco7IgY41rm5Pn7VTmfA44p74oLZWSH9pyAJ5tfjLuYC7z94zhcnXcoSNflKMu6RmutMMTriCYWdLQop4giOxqowwUqSego9halMETMN12sDsm8geykdw0BIriQ5775aTK0-XMIP14nSG_Rqt5WvJvsh4QjVXrlif5wXa9vbomQg7be-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEIlnCC3M9c58dOO_4QQKGuf4LEU-1-jZyqMyI3uoluLuPoOKnhUORcA59l0xF_5eToKWZPjoUS97v4lGJCbanZBDPG8JAo4Nj4t9FfJtMOfrk3n2RI7ubCoKQRZEH0wRQFv14t_ef3CCQXIZL6HNM4ZBqYZSbY34XG8paQlYsA8_1sHanmszJzJTNnJqYzpsJfMCBnnyEHdWJ3rNikdMOsg4EOBrGq6qdAdifnlvI6ALV2idj1jMyfx2JCf4KUxJBvfYIfekj6wWtVdI_mKVM3k37uv25Eg42UhyCTp0PwsngmMm8W6H-C3oy-ortYQkta0zHZlc_IbQUHHc2pSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bkronMePW37Xy-n35RXI8-jhLVGeUlTDKAId7CsfofX8qLSSd6IOGgvrQr0ucyjhv_c_kwPoy5OZNzziU6L1v6FElGTUU8GogYHNRYCZiDWaQCt4pG_gGEvY_9ao_GXrNSqgj-vHOl4FnGhALuD4rNlkChjGbPvkmUarYpNvjq1kU9JBrlPwM6hKkWdwnbFS_zp7q89Y3q0gtI8AOBqBG3grbBYSBcYPHzolwMVZ-sQVBNZHgaVdjWkPZy-Ysw03WZxapbgEpWoNh7XyU20alvmB45OiF9kNLtBv6YkKuhdTZXMFv_RZjcfNIT8Qjz1CkNgLXxlmjMjdgY1179Ba4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq6g9ggwZDZ-cx9WJAyI6inEVDfIVGHz2uQH5PlTEXxDPHvCMimqGy69sZf4CtEoZlu6EaMh92Rrx-WZ1htO5v4M4f9oEEo0AB2sda2tnMVpVi7XvmcFzGopb1LXi7qWdCy4g1GXelau__at5_zsv3g0ojenvZIzDCh2uKZxucLyHCqykqfAe5UmZ6_2OLIeYRS92cKo2oMax5ocxxoOsejFiuQWqbYgkTrzdf2DZNORNWfqFKWFgZNApHmVaKdKl8b4iS-7VSnWrSclNS0t_ZtQsfaMDI0qsRLbcJsIdSxg7AhHSNg8RqkjAyQRdEpUm7sVhQkFTVlXDF-agM_Kuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NTsbvwaqzoOiB04gmHyqNm8wPi_Ctt6OSH7MvWxL4zcNwhEdAuPVJTUIxnLIJLjSmbiU0jy6OST-iMgrVcIHHyj15ulYOoiUs0ZHxECUoT2SsseVNtlRdrQcH-NEie8Rgl3Hc3artGoVo56P7CasCE8jhPeIhy1f_yQq_v-12N8T9PA_ycFw6TG8VsRAn10h_AruvtrKgc1Ic2uDZUwbI8KZajSVGjEs7IDO_5BM4AjzExNUEbodsBLpGDw3cc-2RHcxme1bU5BzIv8XJs5iYbwVMy8MiHaeqfBXLFc7yOvdhPZiHxICVX7fQ7n5jwjN9xS4g1R6hoLUdQCATPfdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=oLKczy52Qx7DZESeQW4gSoVOw_Ozf3yjVmfWg-yhN9-P4kfSNKSrJB1NPFRQ7wz_x2sFoemu-nYJjc_FizaYDIAgJlzOLtiraBXr9v1jlj_fwwVej1E6aJljvnWH0JXuGDc5lNgPTwtNfPym4gvEfNpo17B4vKIV47bcjAur1UkvkphbzD5TdHtiRzQmfFYb_Iu7msEEKV1FBgpa__-Uen7J9bPcJabgVGTMSBbZY6bKl6odmEmaolK4rDs0M04SWuJBl6Kt-DTw6wHNwVD60x2mOYTGtRY6UrUC1lQbsDad7lrKaRWT7js4tO4R1qBYlOHQ4GOaTpmZTI-qUORvuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=oLKczy52Qx7DZESeQW4gSoVOw_Ozf3yjVmfWg-yhN9-P4kfSNKSrJB1NPFRQ7wz_x2sFoemu-nYJjc_FizaYDIAgJlzOLtiraBXr9v1jlj_fwwVej1E6aJljvnWH0JXuGDc5lNgPTwtNfPym4gvEfNpo17B4vKIV47bcjAur1UkvkphbzD5TdHtiRzQmfFYb_Iu7msEEKV1FBgpa__-Uen7J9bPcJabgVGTMSBbZY6bKl6odmEmaolK4rDs0M04SWuJBl6Kt-DTw6wHNwVD60x2mOYTGtRY6UrUC1lQbsDad7lrKaRWT7js4tO4R1qBYlOHQ4GOaTpmZTI-qUORvuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، Jev از زمان عرضه داره روی GitHub منفجر می‌شه و همهههه راجبش حرف می‌زنن؛ و اینا چیزای باحالیه که مردم تا حالا باهاش ساختن و شما هم می‌تونید بسازید:
- پروژهjev-trader — ربات معاملاتی واقعی که سفارش‌های limit زنده روی هر بلاک ۳۰۰ میلی‌ثانده‌ای Monad می‌ذاره و فقط Jev تصمیم می‌گیره. ۱,۹۱۱ استار
github.com/jarrodwatts/jev-trader
- پروژه jev-ultrafast — ایجنت مرورگر که هر کلیک رو خودش انتخاب می‌کنه و فقط وقتی واقعا باید تایپ کنه، مدل متنی صدا می‌زنه. ۱۶,۷۵۸ استار
github.com/browser-use/jev-ultrafast
- پروژه jev-doom-agent — Chocolate Doom واقعی کامپایل‌شده به WebAssembly؛ دو موتور روی یک نقشه، Jev هر فریم تصمیم تاکتیکی کلان می‌گیره.
github.com/lukaske/jev-doom-agent
- پروژه jev-t-rex-runner — همون دایناسور کرومه که هممون هزار بار بازیش کردیم، حالا کامل توسط Jev بازی می‌شه: بپره، خم شه، یا ادامه بده.
github.com/joshlarsen/jev-t-rex-runner
- پروژه‌ی typesafe-chess —خود Jev در برابر یه موتور جست‌وجوی واقعی، دو بازی با رنگ‌های جابه‌جا. موتور جست‌وجو هر دو رو برد، ولی حدود نیمی از حرکت‌ها نظر اولیه‌ی Jev رو وتو کرد.
github.com/TholeG/typesafe-chess
- پروژه jev-drone — یه کوادکوپتر شبیه‌سازی‌شده فقط با دوربین مسیر مانع پنج ایستگاهی رو رد می‌کنه و Jev نیم‌ثانیه‌ای یک‌بار وضعیت رو قضاوت می‌کنه.
github.com/RomanSlack/jev-drone
- پروژه tax-doc-classifier — فرم‌های مالیاتی IRS واقعی رو با دقت ۱۰۰٪ روی ۲۶۱ فرم دسته‌بندی می‌کنه، با هزینه‌ی تقریباً ۰.۰۰۱ دلار هر صفحه.
github.com/kyotofin/tax-doc-classifier
- پروژه killmyidea — ایده‌ی استارتاپی‌ت رو توصیف کن، Jev از هر زاویه‌اش امتیاز می‌ده و بعد kill، fix یا ship برمی‌گردونه.
github.com/monteduro/killmyidea
- پروژه jev-curate — ردیف‌های Parquet و JSONL رو با قضاوت‌های typed با سرعت ۱,۵۰۰+ ردیف در ثانیه پردازش می‌کنه و فقط چیزایی که از حد رد بشن نگه می‌داره.
github.com/AkashPriyadarshii/jev-curate
- پروژه pg-jev — افزونه‌ی PostgreSQL که بهت اجازه می‌ده به Tableهای خودتون سؤال انگلیسی ساده بپرسید و جواب واقعی بگیرید.
github.com/realZachi/pg-jev
✍️
imryven
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K_Vmlr_215TOiKco-nNQDhZ9Fybb71pZ82dWwVK1I9QcZTLMPLFaG23DJPK2_2LtgV7FB9hwhOFuf7nRUie_K0mLUA9tgaPTZn3kHMwOP003JSlBDplTWGMytP4oB4piyB5H5tlXs5-d_SjwloxturwhggTfo8m9uQZVkto9YMUHs8Bd_slpH5m6KAV8xH7kOy8_muprQsM49W8ZZacdLkxwr00VEob4hYuzr9TQiSN-4i98EWriG2W2sLQEeVAj8XuXW-Co2jD8WrZvWK-IyUE_nW_oInF8fdAmUFm1Q2ne3r05wfT1w3jf4tK7LAWZxLbL3jZgl_5DpmN1CrXMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هکرها چطوری ChatGPT و Gemini رو کردن دستیار کلاهبرداری
🥸
یه تحقیق تازه از Vigilance Security نشون می‌ده یه کمپین گنده (اسمش رو گذاشتن Dark Sourcery) داره جواب‌های ChatGPT، Gemini و Google AI Overview رو مسموم می‌کنه.
قضیه اینه که: کلی پست و PDF و صفحه‌ی پشتیبانی فیک می‌سازن که با تکنیک GEO بهینه شدن، که هوش مصنوعی شماره و ایمیل تقلبی رو جای «اطلاعات رسمی» بهت تحویل بده.
تا حالا دست‌کم ۳۷۴ شرکت قربانی شدن؛ از Fortune 100 گرفته تا Delta و Lufthansa و Bank of America.
چطوری این کار رو می‌کنن؟
1- شماره‌ی فیک رو با فاصله و نقطه و ایموجی می‌نویسن که فیلتر اسپم نگیره، ولی مدل راحت درش میاره
2- شماره‌ی تقلبی رو قاطی شماره‌های واقعی می‌کنن که معتبر به‌نظر برسه
3- محتوا رو فوری می‌نویسن (جابه‌جایی پرواز، قفل شدن حساب) که هول کنی و سریع زنگ بزنی
4- پست‌ها رو می‌ریزن توی LeetCode، اینستاگرام و حتی PDFهای سایت‌های دولتی و دانشگاهی
پاک کردنشون هم فایده نداره؛ کمپین اتوماتیکه و روزی هزاران پست جدید می‌زنه.
بدترین قسمتش؟ Google گفته این خارج از scope‌شونه(
😂
😂
😂
😂
) و OpenAI هم گزارش رو بسته، به این بهونه که reproducible نیست. چون عملاً به سیستم خودشون حمله‌ای نشده؛ فقط خروجی AI دستکاری شده.
۹۱٪ آدم‌ها جواب AI رو چک نمی‌کنن. شما جزوشون نباشید؛ شماره‌ی پشتیبانی رو فقط از سایت رسمی خود شرکت‌ها بردارید
چون به زودی شاهد همچین افتضاحی توی ایران هم خواهیم بود متأسفانه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v1G_r3zV3nAfcB_E-kLc0yapFQxJ4DGqlyAGHYyVanUKxvI6roi3iPuxNKkJhJbvlpnZn_WW2L13QlzychvNy5kQf42mdQK8DRFoLZzukl9SU5A5SunGr7mmOngdQHRFHgke8NtAuE-DNlIfYmBsXPEBp2GLSvgVAMdUNAFuG5Np68wQosYeL8NgZheZkL2xXPTEddxKBfM7t3TxLL42of9kBcOuOaNofK6DMNhRay27gYlo7S7wS5X3gFht94ih1Byow65bgTbotf6Yi2a35N3JtKX5rO71L7fjCSzL_Vof3oouUXGbsYE4nO777YiFDRDrHJbMqWXunYAwVy5ZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AeQsMAZpzdtJrTH0NWiUdxAOUnk-hgJQO0rhvDBF3ykHNciJibKsv3XewL8cycJ7eF1v80AQvfykNHpSbil7g2ra17jI7e0sYY-eXb_9Oo79J8FyC2jvX-HpzT2vgW-guKLfHBD-1ecEQuVUpKdNwDfAa-nMX-R9WxAcwvBkzsJgGCoQZ8buCCMme4ahNedIBa-nvUyDq888vmstRtMTYWtVzP9bxWcQZarn1rassul5wFAtCj6ve8elIVpgCjF_WFgYyAfmEgiGS2MqLbENL1jXegm0G2BcwW0LxT_MD6W4_oY82qkOUEAiwd0qSRMzfKyX_4nQfVDXR7V7BQ65xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EWY2CyEiv9WFPiaB5y0JwPt1Luzk0otAqKMjXPfgKZncukSqIJ5uZa-9rr2dcwHkAh8hsWFFo74UBRAA_gsb7IuX_cJBiPWfFLNe4nx8FGhrrI4PBfA-1789zqf2JXwme7A5zwBrxS4GR4r4IOl49zO8CRP6vy3FzWTaa9EkjzHyoV_SiXIicOIQiGR1J9cbGWNms43j7FWkbGPFhCE4G5Su3qTRPT_5_D6e_gHwVFmtV64N4gpg6N6oCeC9MKn0B54EjBlxJ24xxWpo25TE_vhqrBq9TW_p7ru0IG-3awQlzS3tIxO36o-kshvs15hp1lk2CHqaeAcUns92zdVcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=tumOq5z0a2H-KyCC2gDvUVQh0wOLexWr3GSETV8MKuWGB4t5Ixex0p7boipggKqmSgde5AP5CBuYFQC8VSE2D4R_f78TRrfZLhfXflua9pMGdfddHgvl6_Gf-5OHmzGYAIuOtvzcOXs7guSVATSkKiwMv_Usr8sx6g2lVHALypzrDcrL0cTYflSfa809Za0Zcnnsbw7HQqJ6zizKJYnfXxGj9SgCzFKLv4UmAwKeWfHiPfbjxVjCatMVTB96FJHSIOF8Ho_ank76mtnLV0g7GSCxwjHikAPl0b0K0MPUZnIzlFsf1MT50sLOSZiLkVuaT4MWVoZYS6NyJwykvyElew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=tumOq5z0a2H-KyCC2gDvUVQh0wOLexWr3GSETV8MKuWGB4t5Ixex0p7boipggKqmSgde5AP5CBuYFQC8VSE2D4R_f78TRrfZLhfXflua9pMGdfddHgvl6_Gf-5OHmzGYAIuOtvzcOXs7guSVATSkKiwMv_Usr8sx6g2lVHALypzrDcrL0cTYflSfa809Za0Zcnnsbw7HQqJ6zizKJYnfXxGj9SgCzFKLv4UmAwKeWfHiPfbjxVjCatMVTB96FJHSIOF8Ho_ank76mtnLV0g7GSCxwjHikAPl0b0K0MPUZnIzlFsf1MT50sLOSZiLkVuaT4MWVoZYS6NyJwykvyElew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsvQ-wCJdiqQPyJB0VFsyy2ULN5Y6IuhcbloxERy9SWRhpCiA4xEzJ201lAyJzEJOfEQamBvVbC7yJlGfhvMDMtX2AwAPbq0ScJJ80sZuIcyuS7AUtmY6fNtZyerEm2QxT_zXDGRPDPUY0n-3IM16PKMI_6bNaoneUfF4e4CI5XWmQ930e-52WxQOEvMBhdbfSplmcIRALT8IluJ0NPHZkbNHTKvS4OyqyOKtiMmvDahT-E_mZq4LVCb5hGQEOc2YJkNZTs4ZtHwWuedIY_sohULRL1IoNpzY21hFY5mVMobYNjXh9g9p_HjMREtE4U4iZ4DzL8A8DZ-fYXQ_8CX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=UeQDUDIu67LLTsuKz0TMtZbuoNl00rj-4N7Ex7FZo0peYMhKGbl1oR53fyq78fgdrpkYGmmhTG56XPK-oaHpgLR83paiEryDa0vF7Bl2-Dy5kzidoTTp42Cud3rVz9rttoMZO8DMgnhH_eL0Yn9HrOlsl5DaDzBAgd3EK0N6BUXlFUrKrdV3gi04pBKyKCSrTQmRSnMlhOWLz76b4wemfTHHFelldPY9aEcI1-4ld038d7XQ17I80lWaRgXU1Blh9ACryePi7oXTZlazLHA9iJvhRnUtwD_Cwru3VIaSvCe2ZYiWTE3SMwmKbrwkxt4K8J31IINBKa69z2-RZcGNUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=UeQDUDIu67LLTsuKz0TMtZbuoNl00rj-4N7Ex7FZo0peYMhKGbl1oR53fyq78fgdrpkYGmmhTG56XPK-oaHpgLR83paiEryDa0vF7Bl2-Dy5kzidoTTp42Cud3rVz9rttoMZO8DMgnhH_eL0Yn9HrOlsl5DaDzBAgd3EK0N6BUXlFUrKrdV3gi04pBKyKCSrTQmRSnMlhOWLz76b4wemfTHHFelldPY9aEcI1-4ld038d7XQ17I80lWaRgXU1Blh9ACryePi7oXTZlazLHA9iJvhRnUtwD_Cwru3VIaSvCe2ZYiWTE3SMwmKbrwkxt4K8J31IINBKa69z2-RZcGNUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WgIzZGoZoJroatxBdbVaODGX1oQ1qkK9b6O4OgeD6uYqU1lSxlKHu-paLP8Y8cvkHUNhZeeLmqzD714EDCPnzD5z9ChUUcVQc9mI1U8infIG_BL6bLQcLg6kHvl2AEnogmaSdqPYV-MljsdZ59KXKYqN9en_UC4RVVISFJLTglNYXCto0GRbJuJgnPbKVvHli26unSc5OYEkXqsBSSmzaQunFUcTgq-gtqyLIab5evcxubR4LpP6xslxfbekULiuj7jXL6fEq8_A5HH6R8D1O4mhHkAKTXcUm7vMaoblutnBaz8TZGRgwa2ItfbZauHcPqTUOEm5-CIfiLlHRcIERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O5qvGhKM-UE6SeZynYujgDH7vD5WO9w93j-NDM9v5eZkyJ6IWl3JkKhCXNM1BHRRQ-XYMZqf9pv4HivrkSCdRxWtH8-r7vBhhVCS0SzrYBviEEkPu6XM9Ci2kFxc9PmF_KtpCN45K0P21WXE_17PAA-an9g_PtNmqXnnL7Ug5XCjk-7Caq0QL7ZbSRaw-f_nTl6nEzkmbioMt_jv-bM0yOvdFjwTBWQLTsP5E95tIIGgC5VFmEAqVkxJYRULGlGfpE1LzIiudanHT_h9X8H2rVy2VgKPQ_Bq6ozN0Czk7gQdNFMxMJmalMbvfQsYxGs0PyymeUhxA2L8yxyAe-nc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mq5LGU5api2TS7joEWQZP8kpOUwW-Xijmw6LWwgaZs5-tojcy5dognbym783OgOQ7k6U14_TE7i7AK5Ig2vkJMP_LKNd0mHBVFQULwYnJWJBnftkNcpgtbKXe3hf0CdamfkbBphgunCetD-yD7bEv5sGzoS5KHjDveLBwgu4G6ptSrXhNL4R1PAtgtbV6vIQs7bkqXsL_fVkLIX0VX0Mt7rJ5c4bAG_JLJYX1CCdHXymrhqklEq0Aq8VO2O2UyrwTDc6MnPfQzTZQpM0MuKF9W6yFGvvxfvZJCOfuTDmI9wLiNjFTambJ28xC1ZGrvMWgHCrrG27v0oxuFG6OQNtCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U9DDWIAIkt10GRf2e-G9X8nI6I9UjEyb4PBQk-VAQNNeDe_ImSmUQztjMfAEK8pFOTckHNE6LLG2IK1Z44OA5SAU-lFh43N1LcAhrVMDooVksObeCDMLaZhxAnSryTigby4mjGZMqmuyRfB8ya_jw0_FmrIAOqvZJmVVcAhs66xOKfXPD9FUFbs8mTa9itIMXY8SuaE279z8Oj4uKX390mkLxlNF8LGlZTFTapcqA8YG8T6Tzrj-d4ZJyg9yBzNV7_PdlpkUnnE-6oSH8uMLFYIJqSaezHBDJhlGYtajIcZqxelTC5fvhaoPBNcnRN76xu5cLSiBosDTS96OodYuzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fEshxfYqFyveDQRSzXEaMcklPRH-c4tXKF4Hyppx2LTvnhGwQgNJSXhcb9UCdPQ6VZcjJnQddSynFmBMG3zwuQZTOUIfKb-bIdBWVM0Nc1w-31Yma27-eIekE_JcemrTGO9dyxfUgUqvDo-G93yYck702PmidTUKEW4mBwvPPX-g2FfAGFdsn6HRFgR1XgkYe17mnOey4D4_TCIlocCKoYjGWHceqBoctRSvrZ0UBVDLVqt7GK1sOWQ6ZaQRwLm1LL3eNOUE9GO75SE5tZtWmGDZ1vhD0i4fNgpitozGM9ZCodEnFb-VfmUNgf10TZS93kuemc7iUwGFGFhpS1rr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fV_XwvAxvHM-5GjZ7c1EiCeFx-GXqiNVfztOXWtZ5Yk_MtkVu8s36Ks1nIeewmMNVO7y6xzF-ueKWbO1B97t0UnS2NhGD9v4qGHjptEAlulZrp1eeI2wUVaARzc1NUJz4LV9XmHus0FZtvH08hmvAT8qrJ-HW5zz6i3VqrlQ96KDBA68cKgrqi3yn_bl33DJJNB26pxteUlFxUreo32ytCO-M90xninT5u8qFbzPXdcewtASKNVjC1Yu1sEqmK5bbXA8NQv9Jb7nQdEOkvZpeDeCr2tjF6TRxrpwO751mB2qCfSefhNP-KFvJVv42tjm9iiJXwU1kmLzTImWiKNYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TxxFa3IYvHo7aWFj3YCDF6TIL_w1t3L5AMmL4jni6Vt7Y8U9_nDX8wCrO0SxDnzjEFVGQSQU85eLHOquQrSZv8xpvDQU5eCTm8Ng8nkW54SWK362qFLD0-K3HPxXN4MHhpGOJ-T52Lwv1KSaKzmO0L5FE41SdGh_5MBRdwr3SN5nAqulKWoH0q1ijGqko_P6OgfA-nEyYtD2OH5gqkDSYH63ugaRbwJSz5Peprd6fupsjWXFxO3zVWuaWt5ZXQ3aPWm9P2ryGamkK41Mdffceg2jIXIjv4NkXOBwKIvUpSD2F9-54zik_YQZzVcgQg-eXf72uMc4RU0kG9XTypv-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vo1yG3uZeqwbTOf8DLWmyjVgsHif7a5Rl-R4l0yrKLVGhi9c_Yc-Km-XNCkl-w_cFpjD3ElwYKnK8_LLzFfhoxoTBUB88capHUn3icdFpD2kGlXvt4VVln3KNb631x3pmS6SJbYC9aSAc1jUa_mGp-5MAAJmyq4jQu1xPcZ5v1OAS-v-ESxcpSWuaFvaca3eds1dho5m4PkFDxSU4QdOPqlEMYtPTxH3IjTwrP5m9gq86qL_HZEiGd8UN5_h6cVOdJyt20MvuutbSMpgokTk4eTFntyedYmE8mqWEg-KsnCV8GEiCxKzfG34ndL8qxHhFSnUh_qemPxuZqKGbhKw0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev  توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev از برادر کوچیکم دعوت کردم بیاد کمی راجب…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sYsj8sqfLlyfpFEQFa4xR08Jp5ENI6tyKt5121z-AKqY1vIiMkLQkovCahlVGWKvHrByYswJWM0pdAqylNAbiOypCCF0tIixaORflmwyYp9o6w-fCNRPJDwcad54_LvHSOu21AC7gxWcLEyBXq5_-ESs4qPgTMxIULCNt8nunqLYkRkB_daHFGYw75M0xt9QtbTKovg9pQwp9ap2K1zonR0IPFLgf1uKFEtq0tyRSawgJbHpspxDZWetBHNL8pQcBVKdn0OU9v0bYVCEt6KwIBxClKHHAAPT6YUPxYK2MXF6H2MCGhn5t3GDSJT11bN8mc9jU9dv8Z_fOoOdrbEQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dmFD-sAmtivy2XklK8hFZYaKGwebpivAvFnd_XVJTAYydzRDjOc3HDFh4Hr3xl6hYtL5F8TJVSeFyiCAdm5To_2vSnMNkgebOq15Wpuy733blix07xUHM7x3qfW9h3hMuuqUdh_qMB4KZ09t8pVwLc3WLmgpXz3d04Wki7GKdvwfCq6mvlm2-Y69PKoGmz40SwiTOnFAkUFt97AlWNrd-HjHzf-xd-w2aAWxUhK9kRcmCuniDtLnJaTQ8lxL7AzvdN33MEt517yMsydieYyrTgHgj9lenxOBIdvQwLKAm3DExLwVlUj-QjE0QkC3QJYNiS9TlkOtclpNmdCjEyw4OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uks10JHmY7xoAisTw8euP8WyG6LdngqCYejpMLlhRJVSkXV-8qtoC83Jp7VSrifptSWZxtOPWt5_F5XuNKhrpuz1XyGwxdFOw2clhspw-uKY-zVRwC2bxMiMuz29IA4JkhA6JmWdqlpDW5DyMyfM9exLs81jxfoIpeX1NVEiJzvnXy4Dkv_DXWYbcJ3fntMrY0hhU6JXSmiraxtPANImxey3QxjQNEoERNyoHSaX6Xrc3LN5qO_vnyrZEj6--2cDx8lPhXuf7bjgIbzHNjOvu4mWhTIDBAfMKJV34mPHGZ3FZ9CSWgjYTmc6oq4xVLHeNtfJqlnNtn2YAIMXmFp9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CLC8mYTM675S3yrX3H4jGqtwqhZWNJWwnBPUBp9O6RMbmmWgD6p9yoeAm37RilftGodmcsjXD8wrqMjBTEVUayPTJKU8nLEq6CG4alNV3arXQ5jmzrfZYeo7Z3zQfZ5nW6d873WxvSu_pVv223iJT1YARKYj6nexwavA0QXJaEIIcjTanR9JU6YIts6X9AknhHvfX_WRh-uxoV8xV3-oj3ayZAdESX1EFK_RdM3AAohuuD8VQWXEDzaV_dWLYjgNBVtAaBeJkSQP62iawMIMuu1ABXq4wG1AWccoi90oV-gai18FlR5VXJj-ZXQC6lpuYYzGYjQn058U545Wuij_FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nXwMlwPxnDuUhDzHIBhaFGa3_kro7dSLfRfV_hZAwzIc4j1KBUKdtjroCqDrmiotBp5Xru026PY7-C7Wb7lZtrOW5Qejr5WjD0I6J-y7ciSY-aO0GHBGJzc1Bad_4JTL1_7_h3O1KZFDV2HkVUGM4PLw3daQdAAbv-OS9oq4iKwRltzWYwlBWPWAm3tGyEUcE5quONSro45v-D5B72u26noRq1uyHmCxVHv8yHR5JVIOHBOZpWJZncdWkzITM_rQ3fBFEArsj85RaZ_wkcOOzCpsAyPp5sKMPCPmxETy6idlEtpF27ktYpAHf854HoE4lMqvA_1V8rA-bsOkbVSDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی 9Router ارور
HTTP 403: [403]: {"type":"error","error":{"type":"FreeTierError","message":"Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"}}
می‌گیرید از اوپن کد، علتش آپدیت نبودن 9Routerتون هست.
برای آپدیت کسایی که با npm نصب کردن، از دستور
npm i -g 9router@latest --prefer-online
استفاده کنن، و کسایی هم که با داکر نصب کردن از
docker pull decolua/9router:latest
docker rm -f 9router
docker run -d \\
--name 9router \\
-p 20128:20128 \\
-v "$HOME/.9router:/app/data" \\
-e DATA_DIR=/app/data \\
-e JWT_SECRET="change-this-to-a-long-random-secret" \\
-e INITIAL_PASSWORD="your-strong-dashboard-password" \\
decolua/9router:latest
استفاده کنن(با پسوورد و JWT دلخواه برای JWT_SECRET و INITIAL_PASSWORD)</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mFSoIgxDYC2p12X76Xm6rFp4Vlir5VmE9gLWVMSkvKBVyBrPlKrtAGzvjjZ218JdjL1hc8xq0Gdc0rjQZKccVIQHLJvflgiizSZ74HvCE77PMbXyksZm6S-hgUDuw75YJNfKiNKQNQUyeiktEyc8xh1LbNC1DgqJ6FHxre51qoQPX25mqaoj05c2p8VIKPH2c1o9NWm6KCpoGms-PB3ygohxbk1Sb3ip4p3X-rvLzvB0jJ3mALal_20BNkAHd4gHGoVDLouFbWMc923l4XtKzlJryRr_mcILWQmIRihEfJaf4J6CkXm7g-2618o7PWKuuQE_4vT7EOJ0yIgSfPEo9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GnqBuGA8GXU-k074xSe4zfficbyblZ_NgfO7Akn0wuszMNKgf1FgAhvtX7XQGbTk_2Ksa97Y2JDxd2ylpHb72wC3IR_j46fhV1q6jAyEWcA6B0uW0QvnkDTOORlYjrLK93DxKWLQP_dL_Y94kRJkcRM8zT7TDEte8RKdPKzHBIzLlmfKPUDvNu7QHPcKJdpmL3MR5ZSCYl1y0AhetiM-ruWhMLagVSLH7nvwJZR-j8NatYneLdV8pTTXNW8PIEWl2WdrPD5icRqGsf54D9mlvZXF6X3dGDWfgLiHu5PiY5zVgrS8OuYRRYrcGSEHVLIKMIbyDZbgIs_IK5h_76f3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev
توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev
از برادر کوچیکم دعوت کردم بیاد کمی راجب خود ماینکرفت توضیح بده و کاری که ادعا شده ai تونسته انجام بده.
همینطور در مورد Jev صحبت می‌کنیم و اینکه اصلا چه نیازی به این معماری حس میشه در کنار LLM ها؟
و می‌ذاریم ai ای که کدشو نوشتیم، ماینکرفت بازی کنه برای خودش ببینم چه اتفاقی میفته
😂
لینک سایت Typesafeai برای گرفتن 5 دلار اعتبار رایگان:
https://console.typesafe.ai
لینک سایت هوشیار24 برای تخفیف 90 درصدی API از GPT 6 Astra:
https://houshyar24.ir/?ref=B2N4W9SS
پروژه رو هم توی ویدئوهای بعدی که تکمیل‌تر کردیم می‌ذارم گیتهاب واستون
🥰
📹
تماشا در یوتوب:
https://youtu.be/l-o_fQM_9AI</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مدل
Grok 4.7؛ آپدیتی که بیشتر ناامیدکننده بود تا پیشرفت
ببینید Grok 4.5 نسبت به قیمتش واقعاً مدل فوق‌العاده‌ای بود؛ سریع بود، کارکردن باهاش حس خوبی داشت، قابل‌اعتماد بود و به‌عنوان مدل پیش‌فرض عملکرد خوبی ارائه می‌داد.
مدل Grok 4.6 از نظر من یه قدم اشتباه، البته قابل‌درک، برداشت. کندتر و گرون‌تر شد و برای انجام هر تسک، توکن خیلی بیشتری مصرف می‌کرد؛ درحالی‌که فقط یه برتری جزئی از نظر هوش داشت.
البته دلیلش رو می‌شه فهمید؛ بالاخره تیم سازنده باید خودش رو توی بنچمارک‌ها بالا بکشه.
اما بخشیدن Grok 4.7 خیلی سخت‌تره.
1-
مصرف توکن برخلاف وعده‌ها بیشتر شده:
گفته بودن مدل جدید توکن‌بهینه‌تره، اما توی استفاده‌ی واقعی بین ۳۰ تا ۸۰ درصد بدتر عمل می‌کنه.
2-
بنچمارک‌های ضعیف‌تر:
توی چندین بنچمارک، امتیازش از Grok 4.6 پایین‌تره.
3-
سرعت و تجربه‌ی کاربری بدتر:
کندتر شده و کارکردن باهاش دیگه مثل نسخه‌های قبلی لذت‌بخش نیست.
4-
هزینه‌ی واقعی خیلی بیشتره:
هزینه‌ی استفاده‌ی واقعی از Grok 4.7 بیشتر از دو برابر Grok 4.6 درمیاد و حتی از هزینه‌ی Astra هم بالاتر می‌ره.
با توجه به این‌همه تبلیغاتی که برای این مدل شده بود، باید بگم واقعاً ناامیدکننده منتشر شد.
البته بنچمارک‌ها همه‌چیز رو نشون نمی‌دن و Grok 4.7 توی بعضی کارهای مهندسی واقعی همچنان تجربه‌ی خوبی ارائه می‌ده؛ ولی درمجموع حس می‌کنم هنوز خیلی به مدل‌های سال ۲۰۲۵ شبیهه.
مشکل اصلی، قابلیت‌های Frontendـه:
عملکردش توی کارهای Frontend به‌شکل غیرقابل‌قبولی بده. قابلیت‌های 3D تقریباً وجود ندارن و مدل دائماً توی حلقه‌های تصادفی شبیه Gemini گیر می‌کنه.
حرف آخر:
این انتشار واقعاً ناامیدکننده بود. امیدوارم تیم SpaceXAI این موضوع رو بپذیره و توی نسخه‌ی بعدی بتونه دوباره ما رو غافل‌گیر کنه.
✍️
theo</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PxbhDQT5qVqCAV2k7KjyZfVmH4CHUsRwzof0b20emlzBrbtI3e5uEk2E7YBaKKHm4l_1Dq6Rvn5efPS9VbE-_R1cKs5IZDzvdk2A0cnUkdp-XYh3wwNwZWzHAvZnmM15r-naJbbgrLJjGdKNICzUi6WGLsmSvmeyeKxrKTCVFgB83uUQwaBj9MbilcCkC36HgSTKjKGZUffT7vvT6x7HKyR5WBcOy_zZWy11xzm5-MqrcsVTjKZ3WhY2Q1PLW0Zve29XHeyZffEDvkR3d_yP10wPFIyt0I07OBCVmK3LHktipkv5mZ-GioiXXWySG_xPST1lN0NbNxxddDwsYxTIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t0BSDdI8LmjiOu0RhinPJ1Cxjs9ba0_uZ0VWUkCwSC7TyjQePf0c3UCzwzZliN5r1LOQO_q0LSZGR94BY3QKfkgpEmhimQ8Dd-pBYLTBachCJaxuYVELXdO0i1U2EUp6HZVKfwiPDzgMzTLpERchkJvIBG8aW9ncow5a7e64ddYnSzx_U6qbkH62nj66UqZ0LPE7zv4cz9Ny3U2M8FKoyfox3LyCqn2sAgObpnQFOoXIlS8xcaRtYiZJCQqqZ_jBGc6JVEX_ufvXxz_R73NBECr__L_Aoj13TTZ_tIo5XqRSJYoxEbUiR8iZ0GFd6iu1peB99v5ngJz4LajWwgqJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bB84VnWic8_PyZmvz2WsZxuat_ci4KdcuEep2Fpg1zHaEMrbeNcWzgTx3nr3-s4C1Z2Lo6IN-toggjtRBgaSAdGQsdI63l6s0vVXwo_amzwTw-FREoCNByrNwX5ezl9bBqPHX-z_em5pXMhyULnr7MHgLngWgVUx3r7YNJrgosPBI-LKo_tgH5WP7cA8WvO4HBRyE6rm9p76ZvNauSm5OkkHI5N5-tRTCZbBE6Uaav_rgUTkKnfUxW6hzAjtHJkd3cKcZ6E32FhNd848TWo0gUgujob5jGoq2PumiTzQbm5ELueqKfAw05Fs4ClNEyIokUAw7Gu5I7LCQQrEhDRtJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mzAhl_GC3flCK_J7bR9ap-zkEVEOFKri0NfYWnbiRw4CNFhVM8SU9IvRG-p8JWrgaXrs-FMMyW-W8Lro0aQ2_3Cll3hXmwCzWP1dfExctmep3nCYvCxzqXslC5QJ8gFx06gywDPXbzHnZoD887ao_pUKV-EtspjPG1sJ7KLba9_Pfy7rxnRgFq21gPy1kmOYGVODXGSwSQCsiuQQ0YloysAzzdBfuCXfbW3ujS6kGTxL0kXBYr9EAW_LmFqaBhXIH8_05hL_UY1zOXjmN12cnRXN_57QM2M6nzO6yfXJSD9oaHsZIX1L8c_2GrofJhJ1Bfx5hkYyd3OyOI8FM_I07A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PwiI2yu81dcFXYB-VwTXCF-BRkQfhFOAQuvPqtgbKCKcTYiMqkdU7sJCL-n6lhmtQpGkEozYRBm1fhUl92bFM7GiROTKCN190XSC1ljejkqxbhF2RLe7pzvwSxthP2DC8G_zV5KpFdDfuIVzdzL51g8yvIyrIoZDNXk4JDnD_W0NA7fzHlc3mQN7QvpYllGYQiCbkswCPYtyR1LIGW-Db-6_HkN1YB7r44jouvtG2XAPuJAKhOEXtflORaePR6yqUMaGXa_qKSvIKxSgbXiA3B9DhswgPfA8Rp7QUXQarrxsgByZs3pr0m22O2kQ4JpKk3anRt3AGz9aXn9X4bqlpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bKtT_gZD9-WZwFjBbJMEQbOsHpfzfEDwB8XIUZsHM2Be3staeATYmE4Z58T33rFP8NxH40Sg-D6KTWywqyeCJ2IOgdzL7rMDpJQTQGxXk8OhF5MHg_ZbNFSrw3QDCPYLf8ZszAjppkWTW0WBlZ6NWrQcCKpxovk0EBS199aZA8fRWRlsHZjfiFpKtF28JL21Tg2wFHzMSP2wEZ3RpaC0Ewy78sVhuvJBLNoFM5bPNvLwJG29WKnzDFCeMw4g23V2NTTec7YfJ69SF6was3_79zv7sdeokpJKYFzEFv0XzLfyrLjru9DL751tl8lnvZSRNX2OiV4gtkoE0qw_QZY5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IZsw50f0AxI0CrgH9nROqJ_7V-5oWQcxgbPsm-TSSB6eMEUhcs7A0QuPBWrIE06Xewb3zeExFS6OH62MF3QIF_H5EsAYcqOUvuLXI1p0n6q9Cqod6Gpgh9r3ZpFGTVT3HGgHTNtmAzv7w9oVMlT0gseV9dk-UcD-3e1iVyEBjZWGCJ8dYT0YG_t71qmL5Wt0aY2r0MmcZ35lThsXAbVuWzAbPMsKB9fkTIT8AQ8vHiP4ewbqhJjVdhghaJhuYgrD192aRdkr40HEa3lffS5r1G-OHwYK-l3wYvJUzYEWYeCzMJwq2Wj4KI3MMr_owJpyyE6_JGKLnwNheNStlrMa5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O7Dp2Wy5j9PL522bNvmyRBKmw2iLeiCFVw5SJL3TiQOpLAGwM1L9gM21vJ3_8XKrbPQ9RH7zQki5SGwHtYb-lTmxcAUQtvGlRHxp9iwtYM70INrQeRsJeaB_MhV9dBltN_83czOHKZFs9KNEEr5RCajwwSDsDnuyVX0N9u762GMmybIJNE7gBFyy4Lg8lGcecVxIPtpOY1uUODTzD1xSAZydKRsmzHCRusvLVD26tgTS-qWwvAB41Eans857F4ZnpcxDlpzh3KfmAaEboKz4BQFqwtD7AzG_ArX9S7KejexKV5mCR5Q7uBR7mVp2043xa2B6u6WZ4B8n-DtFp8pRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZDIh9wWeRXGPJpczVCwQCD7LotY_dLX7wx1bF9Iv6zsLCGVChar308w2YsahBZvEeoZ_k6OjcjxpaYor0KBYA4UoRMnsVowPgnFlFIzBJV6yejC7chtg5e-GF5pQUcDMBBsMe6SSdTnzi9aOi4Xr2cEIXU0NwyAZx3kDOhuu3m7P-WyS-fZui4DaeLjczr3IPWROvqEOElfsnX8lAuFTBrlJtLBRaHaourdeeTds4G1UJoKSmPh5soJI1lLMSRCd14cgFaWV__OK9bjrXALJuT7NF3bB8Met1I72aofZ6YJ-rU8rkI4GsOZ-6jvagoHR92gLcJfXd-S8us_A6qiODg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gmzQ36erMg8sn3ql7JYNLy03zJw5oO_U4FjYFHAeXvIQQXHlt-5Cp7P9XR3fZ0xvwdHXWHwDNgpmT0x344bTtN2NqUVnqKUgqQLEuLAIGlQTA4pVzUBdx7J9VytDD1n2v7eVf2j4kzL2spPh2F3qq8wmD5iSCs8M0Qk-bJz0ghLkE-t6A1vI52qsNfGCsxnkx_uXIuMerMRH4NQb99XI2QE4ETTsKrF6uaJfsFE3MviJ5xvQLyXiXsy_EniiGsyivRb4CjyBdgmZrXSHzmHaWul20j9U_SaNKuAbMHZ67ymkT7r6shhp7r_S4hcquSOu1NMaFwuJU36hgTP9ULnQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه
هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن
به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم
، سعی کردیم با
یزدان عزیز
با استدلال و تجربه‌ی خودمون به این سؤال جواب بدیم. چیزهایی که بررسی می‌کنیم:
— چرا بیشتر بحث‌های این حوزه توی شبکه‌های اجتماعی «حکم» بدون دلیله
— فرق AI با یه ابزار ساده مثل ماشین‌حساب چیه
— تفاوت نوآوری (Novelty) و خلاقیت (Creativity) و اینکه AI کدومش رو داره
— جایگزینی شغلی و تحلیل آینده
— چیزهایی که هنوز دست آدمه و AI نمی‌تونه جاش رو بگیره
— بحث کاهش نیمه‌عمر مهارت‌های تخصصی
— ۵ تا کار عملی که باعث می‌شه بازار کار هنوز بهتون نیاز داشته باشه
📹
تماشا در یوتوب:
https://youtu.be/x8V0w3I9g10</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGN0gsitdNIW_U-FhIG_gg35gbcPeqzMeCpTXRCIyNplll99FO2HNOHorIZCxn9HWAulOBGoAR8-CGI3-ROkfKZ77JQr0SZn1F7LUmq51TgNUuf2WRTvpgMH2-GnVGhU0mlQRFYmVKIfSw_N-KK7LzMmdnlALiniMjk5CW5Ay-NpSjAiFBuHy9GVtaP75Wy2op7pHW9grxbUse020m4fwIcEAwnPhrLvBdsT6KeCjyrne191V11uCZOBnz6ZXxLm3asMruK0fdCg9Fao7bpGwYJQ9KSnYyD-_eNGpU8E2tnTLCEgNbQ137OhcH4X2e4BdLuklB_OrWUy3p8UT1oYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=ZuVllsOrMcEis96kciG_IMwA078VZDauAE31M5Kd0NKfR-rnsYZzvbuUu9DYTuvjqMflLv3enofTqeF7woOzKyk6lnjVlBj6jXETsnnkfQfNTGj4C-a8yb-8XZGDf_0-GykwuuSbvYlDSf20491MOlbm2X08XGZycTUNHM1XFQtTLPj2jroJ1FZLSCArWq6_yj073zpOdE0e8PMoOpIW5nViXbX8uM-mcVuAg-jBrQDbNiOPlqoSXvGaoCNNHu7DJmhhWPrTNMsEo3mjSqX_lK2f_wL_RvNzq4GavB05RsZPKXvyqDqeRpDmoA4rFYUMPmhkVUX_42QpnObjYOKVoYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=ZuVllsOrMcEis96kciG_IMwA078VZDauAE31M5Kd0NKfR-rnsYZzvbuUu9DYTuvjqMflLv3enofTqeF7woOzKyk6lnjVlBj6jXETsnnkfQfNTGj4C-a8yb-8XZGDf_0-GykwuuSbvYlDSf20491MOlbm2X08XGZycTUNHM1XFQtTLPj2jroJ1FZLSCArWq6_yj073zpOdE0e8PMoOpIW5nViXbX8uM-mcVuAg-jBrQDbNiOPlqoSXvGaoCNNHu7DJmhhWPrTNMsEo3mjSqX_lK2f_wL_RvNzq4GavB05RsZPKXvyqDqeRpDmoA4rFYUMPmhkVUX_42QpnObjYOKVoYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=pPyEHxPW8rGt_A7-FalFZoCB2_3-_Cx8wCm6pcv7Btc6fbrwKPcIdCizTUPIPx7cRUwQiXYfyCWTPDrk2BBa9c66z7Ge9iWusLVz5L42Ataqj_egj5kexafWCnbnJB1Q9gIfjeFGj3rINrR9yKc3TwkXYGWleyfPFOF_8jjJPV9QSQCR7blTiPsrOSAZgwBu-6nuDY5dk8avjCwuSiq0T7LR2nXIUS5txfB6MieSXHpZgMu91KL-yPTZFShX4fGJHiKZwtrJ3M7-cZm7t1P8jdsvm6c0jrrTexu_K2BJ0T11hLCi33jQ9Bbtq3nMitPYEOWoUvj1nokU5ve1H5kS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=pPyEHxPW8rGt_A7-FalFZoCB2_3-_Cx8wCm6pcv7Btc6fbrwKPcIdCizTUPIPx7cRUwQiXYfyCWTPDrk2BBa9c66z7Ge9iWusLVz5L42Ataqj_egj5kexafWCnbnJB1Q9gIfjeFGj3rINrR9yKc3TwkXYGWleyfPFOF_8jjJPV9QSQCR7blTiPsrOSAZgwBu-6nuDY5dk8avjCwuSiq0T7LR2nXIUS5txfB6MieSXHpZgMu91KL-yPTZFShX4fGJHiKZwtrJ3M7-cZm7t1P8jdsvm6c0jrrTexu_K2BJ0T11hLCi33jQ9Bbtq3nMitPYEOWoUvj1nokU5ve1H5kS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lgxpqSYbxfaOHtGjEclJ0xtP0KvkGHNoWLGpPxngXwVjxFxzmup_bAg-2sFduMR1VtVp91yaM0Rjgy0TSgdHj0xjr2UmR8VBjLHS1GmapZaddRsPVX1rjYusSuh8I0zipe23RiafUHHYzAWLv7uqGRPhHPw9HD5AZtDKFUkgU1d2VG1ZUkUi49-ARBSf26jh__SeenHzMDfBEVln2mENtCouSu5cElb6Aos9BB3Y-zDiBCz2eMOL1PUbGsAxyy0aMHQjor3ftQRxjlOsvfpVjM6J0YA7MHcYT_-l_pqYoHI6XpeZZSvxRbXy4gssjZ7wgAA3T3WFPc9SX55bQdIL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l92u__DSG3yzHwbKW6WX0ncrd1pE9Y47i7s_Q0Htjc6CMd0CaNS2q_cKngLjS3hE6Dh3pen344obRTaHJDjATZtdP7yteDqX8Tr0jlRTZbRuVm8eQL02bdH0AvqJVTRVh60adcMNnRGHa6EiKWetxmMff-Tmxe358xjcBfRl-kO1gap2Ay-w-9JsKp_ywYwm8boVu6E69bfef9yalSGsB8QSMugeRaxLkkDto5vH5QZw5OLVjSFWMuzips009f4rdR6pehPAY9gtxXO6usPIStYjAnHRzkQgNH9k4rlNKloiT2ZMrvwmkIoION6N_Chp4U3Wqv9HuAtM2Ie65Pityg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=W-StXlXKEfyTkch-pUlJAmj-gT9QggZlTG1M1x8fMceN0fOUp4Qg12ZjU5XxkFH2e7GImW_B6o_dQvr1ppwZJT5QLNSTKebdxjdTVuW8EjFEioT5T5LFSvZcDlhrMrFZC15oW2f2DGdjXsszLD4d2O7nZbR1_PmHaER8Is_ptIjLRWnW5T3YlN0h1FZXGNTi5d0Hkyr4W6vP5G_mHA-He7RCb938rBQ7hhX1yNly25c1eZao5nz98LUoL4Nuh7B5IcHANUc530NArZZHAOHVXQqYr3LQHk71wGX7e5A1o0xiTdMrTo3UTvEbC61OHWm1PiUkNyh7Eus5G3dLB7Ty4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=W-StXlXKEfyTkch-pUlJAmj-gT9QggZlTG1M1x8fMceN0fOUp4Qg12ZjU5XxkFH2e7GImW_B6o_dQvr1ppwZJT5QLNSTKebdxjdTVuW8EjFEioT5T5LFSvZcDlhrMrFZC15oW2f2DGdjXsszLD4d2O7nZbR1_PmHaER8Is_ptIjLRWnW5T3YlN0h1FZXGNTi5d0Hkyr4W6vP5G_mHA-He7RCb938rBQ7hhX1yNly25c1eZao5nz98LUoL4Nuh7B5IcHANUc530NArZZHAOHVXQqYr3LQHk71wGX7e5A1o0xiTdMrTo3UTvEbC61OHWm1PiUkNyh7Eus5G3dLB7Ty4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=rZgocDzDhJ-lHYB5hIwk2JYxLZtUGe70JxAmWx8YsxVCPbcrSSpkEK2wvAzfi22tK5etsziGr1DNTC5rgVhVc7___hjvr-0h-GAwQnUsMpwQwEr1YXr3DdXHXSfULp0BwrEs4oOmqnMDDbbwArjLcgW2umOd89Nn7vVRG61MhEJqck9v4yiRl0WqjTsMrd6Gbo4VE4sE3XbLVV9M83935D3tgFdRZBLd8kel7uFSOQwv4m5BrOpN1k9x4E0auccrT6gs3XCfeQ-gI3DTCGXQi_uTG1wnEqvRDUS-33bSll6Ig56QATKMie-i3BM9i-vRe6c8_XTfAdC6VzOkgvOm2VEpncJcUFDZDkNH-WqMqgrSdHt1YXAO9d8dBEI1ijNNOOmINQ6mZqKkEbQBPHpbFGgNwLANrhU2GByWK724VsmP7KQYNMw1VShvajKN0X2gqALyJS8J0eSt-Oo8WaLyNM-m6X0ddNsSpwuRM7DEWT-3vFME7u0YoTzehiRfJkq_Te4kQJMGqZ1W7XhGyBD9LtLtKNQxVqaeicW4YmtUKX-KVuy2yvFT51DE9m83mL2gwyLdiA4gqwu40bzHd_11aD83s17v0b8UU_EXnDDnj7wvNvtU9dQtWr8GuN_WyaudpPVO8Df91IAw2dv9pzcp5ULZKn2MnXXyoMddBuU5_Co" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=rZgocDzDhJ-lHYB5hIwk2JYxLZtUGe70JxAmWx8YsxVCPbcrSSpkEK2wvAzfi22tK5etsziGr1DNTC5rgVhVc7___hjvr-0h-GAwQnUsMpwQwEr1YXr3DdXHXSfULp0BwrEs4oOmqnMDDbbwArjLcgW2umOd89Nn7vVRG61MhEJqck9v4yiRl0WqjTsMrd6Gbo4VE4sE3XbLVV9M83935D3tgFdRZBLd8kel7uFSOQwv4m5BrOpN1k9x4E0auccrT6gs3XCfeQ-gI3DTCGXQi_uTG1wnEqvRDUS-33bSll6Ig56QATKMie-i3BM9i-vRe6c8_XTfAdC6VzOkgvOm2VEpncJcUFDZDkNH-WqMqgrSdHt1YXAO9d8dBEI1ijNNOOmINQ6mZqKkEbQBPHpbFGgNwLANrhU2GByWK724VsmP7KQYNMw1VShvajKN0X2gqALyJS8J0eSt-Oo8WaLyNM-m6X0ddNsSpwuRM7DEWT-3vFME7u0YoTzehiRfJkq_Te4kQJMGqZ1W7XhGyBD9LtLtKNQxVqaeicW4YmtUKX-KVuy2yvFT51DE9m83mL2gwyLdiA4gqwu40bzHd_11aD83s17v0b8UU_EXnDDnj7wvNvtU9dQtWr8GuN_WyaudpPVO8Df91IAw2dv9pzcp5ULZKn2MnXXyoMddBuU5_Co" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/riSf8C-mbl4Xvq3vscyYF50pPBpCOkumMK3FVbG-7DnRs3jFi9hdKifKRcFtG4lRbndE9AEExwKuGvl--Cd1jU-gHgRafc7sOQk-XZvae8YqF1xZ6exQPM9duDqh541A6byXkJtaAKQfW0fVjqffCgtWAhMYFrT2FFvgRzDAk01rOJOvfCvwog3YR8emRQsvJTpX984mNSHTZBeve5yMxBCnqKRMyeV_A7xV8mssEaDT1uhNOpd3LKCeDzy_ug_3htPnD959hTym8r3wCFaXKUHCOsW6aGffFjWloyUZvzPVqwu1cV-SgBRM0ADDdza42s6hxW1f-uz_t_W-5hCheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nHXf-ktJMJ_EYiGwyD1Z_9_ODXab-c9Gu2WkoMmj7p3dmtWhm-domIUj1BF9q0S-oVITVXLffm5lG2ketRaljK3wj1zGdD3HKC1DtzNTnXsF164doHirx-IYRRpjTo5c2dzyCYbuz22ieFMae4oZ-8DOhO1FGgWUbogR_xXcZmXiyDEAZcia3gOH-v9HzUt42Ctv99YP0q0L_C2_0kGdkfixahATj_0DH3jW9_Uqp9VVOPhd02JBDYil_19icbLkWZmiSXt17MVgYELKnxLq5N_i5BmCs_1PJgLZKzx616hA1Rx64ilC6kxMxkaimZ0gDSgSvgbMNA9REh6IkBmHrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ibLG37cIhaKs2mzb8uwBXqeiDh1hKWx7T1kB4lrgWfzB20vlggSNBe_vjX-KXR1MVAGDBNfOH1TIb6Dc8BPU9gm63tEcv1zL1Sf0co8JTxE-ru4C3foxgmz5pzlOD7k3coJj4W-4LcmXaP9SSxL-RfOzxHHuuIJSkGg7LMEEtxwR4EfrhnyI7ATLWnMf0SACC8x-Xs1DN-efVqu55h7jjHQE1yU8eGOysIZT22go2NQK8BMdinqdq_ER4HqpfbAIRahDOMOm41X-EsVZWxOcFKzt2YB2rkr1jwECBHOVey4WlPOjd-7EFDO3m6JoyWhiQZJKoFsuvAI6zSBKiLoauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hoh586N-GbxHG7mPfJU91sYp6dvRSwewwK0myYJ8uzTP8y7l8z4A8ZzJdvT1vr8sdMHMmGM3ZzYogG3aWbMZO5x8y_cW8teIeGjZ2PcC0MlQ1MBBX7wxvQqFQfOe8I1Li3QzATNoeJrjsM1sQ7MWAmD6_9bflt3DReUc_h60UhvMcgbwQiOx_ByzaOM8k3HoHPAdT5n5yWWyddsMeCoHm0cmKPS0B1FAZyqX8S89ZvDqd-BHxV8jAdco_4yGWKkLm0BWilkc-R0dWIlGyWY1ox__HmyC3r2-UqO7Gepjff1kxLDsxpK5oPzndvE0U7zCiNx_pZl_AzdA9JS_13CTZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ulVyKtCxYh7WZtWiFlKALvJHtwsJ0pyb5UJMJA3n_Jz7WAUyowhRQLB2x-5dnjdRnH_xSQSeu7voo14Z1dwuK2_-8MNUkIzInktaE3plyXLo1nVnOpzzk0cN3M4m--LU71_DMcv1JOHZQtzQzwxqFz4Q7dmDzS0xEF3zZG_aaNZl1RkDnQr6sx9plTdmQS_A3TCLz0vDGbX8mtcqnYyfG_E9y_aGOuPeH2kHFnWhFGUB39c3k0oEfBKLiU_y3LLyfxniOk5fA48_e2b4rZIQwTZimLdCG7sPvlmgaDM4uhfZiUEa6CgUQjdzy51G7T8zVuiPTqGCRZXi_gf3ETRJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pAzVhIu0frcBR6elUEeA5OhspDQSxk5iqPkYTqQrSK5nFk01VyLTk9w8Otprk8_WUBMwOHn3gNDqavGsvVQ--QKeOvUXmcKP7ouZViNpkZV3vKSHEvE76cMhgDwj_jxkoGV8gR8QmGlDqfg0fLZzEbtcr70myyNMQTYkqzyVvP3q11kIuUgF8uk9NZqpd3uFw3HmuHa_3YXntL4b6hxrSVMr8kaLUte56erZwgzbMjmYhz4QWmqZlE7eIiy8qV5RXwwQD0VFGS6dCTM1qdGeWTyH4qu8S9lr3bRgWZGgvZ_0X_B3Yaw7HVxPI47SrKR-drSbvLUfJX8nuw4TWf5dJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WaPrTgTQJ9Mx5mhxm9PeM_Rt8yGFJMhIjXMAh7FgTWQQBvAnxGsl5TwSN9zIRzSVj1glrViFkP6Y4TOcYce-Qb0PWk9SRInJHAAyiKn56CWPHgMkHOPED2FwQ4Y9oAq6khylR9w3ZIqwEXrNJjp_XRAoUWmAHhLhDkjfsrIADHtfjhikK-Tq3mfLcUOWdAHkkN0m1ZVk6n5e95pjH-0saWszK3ihGUey0HUD4W5SRhsKbHxVLcDMwowA2XWiLRinlkRw7x-EGhCeiDM8ScAniJLVTrqANsPDlsUupX5pnqG6LG5R1WGct6W6f_MhEOwrOKzyxdDi1Ykt6aXQXINFSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BDMdCccB7YIRQbP_JPjPOfZ22tfqhulWTZ1wsWd_eqeS1dd3_oCaYseQ8q4XsSxFyCbJwHz2KHir4WlDM_bDJwySnqCr4F2Idd3Fk8h7-5NzJ0v_4hzNf7ubdmq-ewtxSNQ8kKOEZTrIZNfJy5tgc5Vz97s5V3-ZKAfK5eooNVn-rXmEfN0UbuSeTKnI-krj9lUdyYDXft50mOToas4fnuMhadsnD0GflhTCJjydfOJ5nJpvUHUJTHQPH8JEyrS3Y9jD5wF4_Q6T9X5ooEDILyBFY1-fXwsa-NcxOw18W3kVFZ9fnAjClYVshCG2lWStyGWHacmCYc2ES--zWVl7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RmVFJQk0IjRTTR6lWq1am5ZOeKsbPt4nnFuyetKwW6kwlwau9s8pVNznsJBAl9yuI20TM0yW_nlIdlCUJED8uz65OHOEGluJ1hPvWDqiOiZupb97idkZvkavZ1ywFa64KHZpxRAj0d1RoGlvDuc5PDSnPQnsU5sB1tnnt2ewP6_rpou5HK7O1C0T4ARUURoYhT1GGKAek86oxjUlCrbXEEm49evqT1tF7z11Jo3xvyoXx5RtygTtUgamts2Bi_1Q9v5hyyOJyVtk8Hns5yqONsXH2-kgr6DBCveOPE3W0sBi3dWHhjQubHYVK5_k7rPBcgcdbjovxYlwwm5XP5Wg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLHTY-klC-lcVb631_8vsLBqitVwVfCTrb9vaZBIBoPgWt7OFdzO8QZHxZB1uWm2DlULNx10ux65DTucSWyZPAHXnrr7i4N-xHeho55AaLHL4UMJxR8MNSXxGwrxwvDm3-CoeH7dyCsZqfaD_FjIIlcR64apoCx83diPlBU7B2oQg8M8uRWbJp88D1yae6G62xy7Osri53C6FvOTmGd3KrT3tOVScy_N23ml_TjYGGS9Ky0CyiGthC70XRNQfFX56_zlmBHxbe3D2fBbLTfLqWLo4PivfaGotrCLZ0WvGzBMko-zSe-Xpa3_blL8aDJqvcmGjj2nf8j6NcfxMfphZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPNLPkunIoFxEj5GRhpwjqMemDXQyNRmZn9FMPa6uH-AbXlUpkG5KIvuFT34TVL00SQ8olm0SMBjyQq6d0QnBF7hkUF6MOIGc3scoQrFzdPIpjjQSdeDn8-JB7_HwI3guWbK0yLkb7xF_Jmwb64DiFm8bttLK4wi9aTQhXlWad6k24U-m7QxWKyqTT6fZZEFDyWGBVvYQGX9RiJ4z2CqoCdI92JiXSYfgUhvlhRnHvU9-5YPf4GNdsaNnWrBQaO3IW67zcHvKsPj-jvUdfdvN8FKmblOVfJvUZVkwxWhwqKlnZW8MpYK0CwXj5L07tJ2jxVfrmbpaMgIWJKzQpm_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPe9Vj-hWN00TSLGdNOQAa3D4HiBQ1xyxAX1eBHGp3vf6pTZ1X_pSs8rcYHcaRC5HCo0dGnx7tP7VUJpVaiy29cNSqi2gtis7yR2LfIe4-vpDn_Mst9ZWEnrnkcStANIR8k3haaYycBDN23y9X42VkP3_-mRD47n_HJeeXJI9wCdB1MSUj4ONTl7hyp6vHO0W4GtP_OeiQLRkgIFrfFDdJDaJzMZpryMYiscD6ljV-0GfFRr-FnGmYCkFuGPG47p0ZC5RmqySfXsQDFyMgNjtE-QCzGjWH3y73tz0u_56zRgLTPqM4wfzaAxEZbMk05BkEXgwEC58uKCAv7Bk3TFsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bdcrU3fg3aET6AthIlMWv8m8lXsu63NmbgFWtX-rFM5p8KdYENTN8JfbK3VLFq7xInTkk30DCMvQOEal6_WmXYj2l8ICt4tqUz-7isAwU7lPJIrh2Iprs5klQCuhmYgxp6o2eCTOFjilfLi9Jb-nH2UjmrNMP8ewBca64ZRFCJ0sdGDG7Wa3qVKcWoQw8FcwWTF6gJQccZhqfHbtphUEwxgkV64ZssOwCqkKa4QiGYKS6RVcbcRGWv7VgwBPTSIlfECtV2N6LhyeVrvsEn5UG_qvDPsFrP-tAnPxzv6nYPyeO_JrGWAARzNnhHkoI0-TjAHiAPfz42otEwkklYdplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BtKuRdoEA_mBI_tS7sjqTF_05AdC0X3WWvujW0bHuGFcdSUdHy6lE3OLB8WGJ4zqDRc9e4ixMi57_aK1mGVJ2LXjGPFT-tNeGEIjvErashr1iDHhsmQGLw0ULYSoXGXI36vWRgj2fArYxZ7rulfGoRXl3yNoYzKP0qc1NcxICUMeqPY7WtSBTjrEsX_pM_UHKWEWBdMIAUA5nHdxptLLzODAh1rpNGwFlVu1Wuqe91quZaLH8QkCE4kvbpNAh-oEb6P62mB3OqLJ8vIdiRO6996ZE53JDHM5nerz11hZBEy9drOuTOBB2353vJS5T8MfZHDF_-8hwUpcTfWmC00E3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/USgg99PcOjGGPzIEw5S8g8pQH5-MDA1-2Rgt4YJF7sRrN0s02Z9QzvbuFWQUduhcXiOyxjPfeFhMEp5LI0n8L2_emPENvZFcOBl6de7IABLI98RnsNuEdOiucgXrrdN4HE09rniFTAWKlzJQfrxZ0MMu7sHS713JwVueYapwOavr43Vvymy2Dl-dQL0epik_FMqFgRxL96pjvaDu9tdLxSystgyI3-IRKFZ5QJrJoLp9cadrWCWipjAaXXebZSLLmptWfrCQaNYnhMy59LlXGgj5PiTpQ36eu0J58xx_oDKx5NLWv0dRpVl4Gkd35mSl0qPBKp_He-lbZAAszL5HWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
