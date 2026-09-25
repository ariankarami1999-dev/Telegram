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
<img src="https://cdn1.telesco.pe/file/k0dHcBPMtvASzaU7B7UQ6C2XdtY6hK9eBWyZc6j5kcKrDZMb3wMPgldK4hBVtGIMum30yLyb_96fp5jMSC4IRbgY0QIZuyQa8WR8VQARQOWjQ2XgofQsFCaYfooHpUr0fs-_yG7IJOSZ-MOEeUNUTp19TbBdO1F1d8HvNrAnKZ7XstZNKle3_mZSkLJH8GcrOVmBdgYxv-KsFJdkoZbTvV37cJXUwTHpeyezakQ1L3KUu2mBzqMcKiWZBFiWz4yaPxuJ0pY8b1GgozUpn-1_ZOJl34pGHPFEwuJH2OnUh1l6FdOQhSIV0x6hxIClGyzQLsoMrFqDv7cK_3onDB_SUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 15:32:00</div>
<hr>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEIlnCC3M9c58dOO_4QQKGuf4LEU-1-jZyqMyI3uoluLuPoOKnhUORcA59l0xF_5eToKWZPjoUS97v4lGJCbanZBDPG8JAo4Nj4t9FfJtMOfrk3n2RI7ubCoKQRZEH0wRQFv14t_ef3CCQXIZL6HNM4ZBqYZSbY34XG8paQlYsA8_1sHanmszJzJTNnJqYzpsJfMCBnnyEHdWJ3rNikdMOsg4EOBrGq6qdAdifnlvI6ALV2idj1jMyfx2JCf4KUxJBvfYIfekj6wWtVdI_mKVM3k37uv25Eg42UhyCTp0PwsngmMm8W6H-C3oy-ortYQkta0zHZlc_IbQUHHc2pSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در
کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bkronMePW37Xy-n35RXI8-jhLVGeUlTDKAId7CsfofX8qLSSd6IOGgvrQr0ucyjhv_c_kwPoy5OZNzziU6L1v6FElGTUU8GogYHNRYCZiDWaQCt4pG_gGEvY_9ao_GXrNSqgj-vHOl4FnGhALuD4rNlkChjGbPvkmUarYpNvjq1kU9JBrlPwM6hKkWdwnbFS_zp7q89Y3q0gtI8AOBqBG3grbBYSBcYPHzolwMVZ-sQVBNZHgaVdjWkPZy-Ysw03WZxapbgEpWoNh7XyU20alvmB45OiF9kNLtBv6YkKuhdTZXMFv_RZjcfNIT8Qjz1CkNgLXxlmjMjdgY1179Ba4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq6g9ggwZDZ-cx9WJAyI6inEVDfIVGHz2uQH5PlTEXxDPHvCMimqGy69sZf4CtEoZlu6EaMh92Rrx-WZ1htO5v4M4f9oEEo0AB2sda2tnMVpVi7XvmcFzGopb1LXi7qWdCy4g1GXelau__at5_zsv3g0ojenvZIzDCh2uKZxucLyHCqykqfAe5UmZ6_2OLIeYRS92cKo2oMax5ocxxoOsejFiuQWqbYgkTrzdf2DZNORNWfqFKWFgZNApHmVaKdKl8b4iS-7VSnWrSclNS0t_ZtQsfaMDI0qsRLbcJsIdSxg7AhHSNg8RqkjAyQRdEpUm7sVhQkFTVlXDF-agM_Kuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NTsbvwaqzoOiB04gmHyqNm8wPi_Ctt6OSH7MvWxL4zcNwhEdAuPVJTUIxnLIJLjSmbiU0jy6OST-iMgrVcIHHyj15ulYOoiUs0ZHxECUoT2SsseVNtlRdrQcH-NEie8Rgl3Hc3artGoVo56P7CasCE8jhPeIhy1f_yQq_v-12N8T9PA_ycFw6TG8VsRAn10h_AruvtrKgc1Ic2uDZUwbI8KZajSVGjEs7IDO_5BM4AjzExNUEbodsBLpGDw3cc-2RHcxme1bU5BzIv8XJs5iYbwVMy8MiHaeqfBXLFc7yOvdhPZiHxICVX7fQ7n5jwjN9xS4g1R6hoLUdQCATPfdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=Vwmtlb3ZPlJLw0s3XrHePpnWVXjqq1tFsmY79aWbW_04ABIuFFOo_3q2XENgownUpc0C3LcrQSyaWWbzkYH6oC0gSuyqMyYXfeJKvuEgEOo7alNxSWSYm0iFryMY-Pruy2ZA59wHA2qp1R5YNbGPMIM7-oUgIncj1lCACe8lrTOFaNGOR2f52Ob6aynCc1Vcil8ji6bSLnvfflJvtdPBngg0zns15mBtEt6MmT-CKUOosvwZbcQ8uVoZmLWwFDAtQB5DEKtucCz-lid7p4kODnk9HXqcYfGrxWj4RmrTt9rkeseavwpHMznuHv7wyJF1IZk6KuWrT8fgJHsaJkd_wA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=Vwmtlb3ZPlJLw0s3XrHePpnWVXjqq1tFsmY79aWbW_04ABIuFFOo_3q2XENgownUpc0C3LcrQSyaWWbzkYH6oC0gSuyqMyYXfeJKvuEgEOo7alNxSWSYm0iFryMY-Pruy2ZA59wHA2qp1R5YNbGPMIM7-oUgIncj1lCACe8lrTOFaNGOR2f52Ob6aynCc1Vcil8ji6bSLnvfflJvtdPBngg0zns15mBtEt6MmT-CKUOosvwZbcQ8uVoZmLWwFDAtQB5DEKtucCz-lid7p4kODnk9HXqcYfGrxWj4RmrTt9rkeseavwpHMznuHv7wyJF1IZk6KuWrT8fgJHsaJkd_wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tqx4IfpW4yxSRKOEXZteiuShoF6r6CKduXUEE8GnrPS7us-hvX-JvCOMvcDgXDSXJ6s_vRRtAjVd2vKpltyZjLrNCoYV5zf0G0WRtQBcg43wQWpFf-bSpnIqacP-8iuoHyPbLyIOPai4c_bNoE4H9WiTBs76zcWkjaMomMYP3h0HZCa355_Y9HPnh4x3r7i8hSSAuEHh0MQwiVmxKw9bhBfzhU6BajC3SEHp5xRDVAgzHJXSO22-i1uNxcj4x4SQZrp6FEI29qZPzBiTGNTGWZkcHHsH4Z6G-03Pw57znoOXMIAGIZXutD-wrO_1YAjYSpfiyIS6hRDnnNlOGQc-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QEEArHFTaTYOU7ZWNG3xAZv5Rz7PpMNZZxIioeAdQmyOeSFmwwtIpv8HBeOIU8A8zWT3eEtpPd8t-DKBJbH0xxaYir417b0wU5C7MpEfoQrixMNcwBSJdtzl1EtveFaU4dXA9r0yahsXiu4C_dq8qefwzGPMa2Ofwc8QAnkZVAehogC2tz37UzieTvJ_GKkJE7x1qgcR4cHoLxd6hfuQp2x3xyd-WLGfnuTYoVzWPrwA6_h5xjmpnRwS0ONqTnXeJGxJNDmCY60xJzSdejq4Plv4DVIJvd1lXiOa6059LM_J3AOEQF6aHkja5cTamb8YXJgx_sjh5zop8ypDiC84uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AeQsMAZpzdtJrTH0NWiUdxAOUnk-hgJQO0rhvDBF3ykHNciJibKsv3XewL8cycJ7eF1v80AQvfykNHpSbil7g2ra17jI7e0sYY-eXb_9Oo79J8FyC2jvX-HpzT2vgW-guKLfHBD-1ecEQuVUpKdNwDfAa-nMX-R9WxAcwvBkzsJgGCoQZ8buCCMme4ahNedIBa-nvUyDq888vmstRtMTYWtVzP9bxWcQZarn1rassul5wFAtCj6ve8elIVpgCjF_WFgYyAfmEgiGS2MqLbENL1jXegm0G2BcwW0LxT_MD6W4_oY82qkOUEAiwd0qSRMzfKyX_4nQfVDXR7V7BQ65xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mlJCb_bklgIFbWd04RDhtX07h53W8Ynqq8re0szSzeQ7RtZB3zzcP2T5HIR6wsmf84rHL9ZizzeNToHS5LETtzSc63k_jA4fbroRO6aE6vXr2zOblZL_fDvUL9E-Endygm6Pp3vZ7MHaDPhUXn_Kaoi4-JY7JLMcbpjiUqhkRWr2Sskogzc1PL4L5aFQdMPspRIfR4iEFuBxezGO7S4yRp_G-snASnkpVwtBwlEDKDnfe9Cevxw8ZGROoPi4crIQo4_azsepqKLeSW2zu7zOkU9pBR8CR4TkbqU48ITY9m_225dQW0wTifKhWsGMyW-Uu0iXjhBGGavy3muNVajquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=Tm_eRu3-AnhpTpP4UjWMZiQ1Vs66cX0rKPROvDHQzlsU1MZ-jGlyocnd9mCB_GplWXNU9AS57Zm3l1tf7p7V8b5ObJt8e2o72G_CiFnyvE5c6z233CICxff0cpT2yPb6_NgpxfbBJYp_nA38QqEjSljeLo29ibwXP15PFV8ju_RdUsWmOF950dy2WGLOSJ-mxu7fP6rGDtGXTvNHAQbmCsLYkKZB7mG9nK2zuDTM0x1fkRo_ZSfyA-dSjeH7ZWeU3b-zF9yB6so7A1RJFtZKhoIxDL99fApQ4tfKSk4kJ7QQcqMsYMIcsyIT3y8TzLckk-AK8_VJvicHfvJo5U0B_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=Tm_eRu3-AnhpTpP4UjWMZiQ1Vs66cX0rKPROvDHQzlsU1MZ-jGlyocnd9mCB_GplWXNU9AS57Zm3l1tf7p7V8b5ObJt8e2o72G_CiFnyvE5c6z233CICxff0cpT2yPb6_NgpxfbBJYp_nA38QqEjSljeLo29ibwXP15PFV8ju_RdUsWmOF950dy2WGLOSJ-mxu7fP6rGDtGXTvNHAQbmCsLYkKZB7mG9nK2zuDTM0x1fkRo_ZSfyA-dSjeH7ZWeU3b-zF9yB6so7A1RJFtZKhoIxDL99fApQ4tfKSk4kJ7QQcqMsYMIcsyIT3y8TzLckk-AK8_VJvicHfvJo5U0B_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGpnRA1aNHt3h6CuNEzpaKKSzwJIQFAxh-kuq7yigAVX0i5leo_RqoK6iH2Perz9KfhWZy35cLdmEMWqGJntkeUf_u5UrRvFyx6yqtn32_CWVY9uSC3ebq5dae8exx4zMHXOSOG8J7-v-mKW0PiPnhRT-hKKx0BnuvQEGMCaLhpBwEv-nmrFlB6oPotD4YI_R3J92e0t7wn3BECj1HK_cVICQFUCAHBASKUD4t2d8J114jkaj68HUu9lzIzz8u4R8Af0h2AegRNW9dBzcrcOK9yDMtKvAF7FFdBAl003X_zB8q6AZ_z9mttGLoh01aHhbu23_kBz8q0fPv4aMPbYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=UeQDUDIu67LLTsuKz0TMtZbuoNl00rj-4N7Ex7FZo0peYMhKGbl1oR53fyq78fgdrpkYGmmhTG56XPK-oaHpgLR83paiEryDa0vF7Bl2-Dy5kzidoTTp42Cud3rVz9rttoMZO8DMgnhH_eL0Yn9HrOlsl5DaDzBAgd3EK0N6BUXlFUrKrdV3gi04pBKyKCSrTQmRSnMlhOWLz76b4wemfTHHFelldPY9aEcI1-4ld038d7XQ17I80lWaRgXU1Blh9ACryePi7oXTZlazLHA9iJvhRnUtwD_Cwru3VIaSvCe2ZYiWTE3SMwmKbrwkxt4K8J31IINBKa69z2-RZcGNUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=UeQDUDIu67LLTsuKz0TMtZbuoNl00rj-4N7Ex7FZo0peYMhKGbl1oR53fyq78fgdrpkYGmmhTG56XPK-oaHpgLR83paiEryDa0vF7Bl2-Dy5kzidoTTp42Cud3rVz9rttoMZO8DMgnhH_eL0Yn9HrOlsl5DaDzBAgd3EK0N6BUXlFUrKrdV3gi04pBKyKCSrTQmRSnMlhOWLz76b4wemfTHHFelldPY9aEcI1-4ld038d7XQ17I80lWaRgXU1Blh9ACryePi7oXTZlazLHA9iJvhRnUtwD_Cwru3VIaSvCe2ZYiWTE3SMwmKbrwkxt4K8J31IINBKa69z2-RZcGNUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WgIzZGoZoJroatxBdbVaODGX1oQ1qkK9b6O4OgeD6uYqU1lSxlKHu-paLP8Y8cvkHUNhZeeLmqzD714EDCPnzD5z9ChUUcVQc9mI1U8infIG_BL6bLQcLg6kHvl2AEnogmaSdqPYV-MljsdZ59KXKYqN9en_UC4RVVISFJLTglNYXCto0GRbJuJgnPbKVvHli26unSc5OYEkXqsBSSmzaQunFUcTgq-gtqyLIab5evcxubR4LpP6xslxfbekULiuj7jXL6fEq8_A5HH6R8D1O4mhHkAKTXcUm7vMaoblutnBaz8TZGRgwa2ItfbZauHcPqTUOEm5-CIfiLlHRcIERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sYsj8sqfLlyfpFEQFa4xR08Jp5ENI6tyKt5121z-AKqY1vIiMkLQkovCahlVGWKvHrByYswJWM0pdAqylNAbiOypCCF0tIixaORflmwyYp9o6w-fCNRPJDwcad54_LvHSOu21AC7gxWcLEyBXq5_-ESs4qPgTMxIULCNt8nunqLYkRkB_daHFGYw75M0xt9QtbTKovg9pQwp9ap2K1zonR0IPFLgf1uKFEtq0tyRSawgJbHpspxDZWetBHNL8pQcBVKdn0OU9v0bYVCEt6KwIBxClKHHAAPT6YUPxYK2MXF6H2MCGhn5t3GDSJT11bN8mc9jU9dv8Z_fOoOdrbEQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twmWd89L9Wbh7VRGwKZNWLp1BZlqA_pgH2OkgyXrICHm0kbF8dPe8lH8P__ysussav0FObkQkDd40bWtHcVYYBG6Mx4xuOW2u8oXOAYCxjDMBDGtFOV8xtVSSvm3mNnqn-hYfb1OFfkOdHfjazwHlHxFXuXtR1NKx7iu35wl2uJMHa_sSgzuC7MhVUy0DUR6DhOU9UhcAlEnjd53aGxtoboulzVlVg99_7OOW-3rBWozz4blyBAo2zHPL6-1DtUroRyGOFAMuznG94xBy6bg8arz4Bd-XUzJj2f6wZK3aqHwigbvD_rS6MCJok5iAgYNBw1UhhFWGJBF_sZq_0eW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p2wp_-nW0urWFTfe6IkrFfFzkTP07X6eYZSuMKYAwtOzMwfDfh_I5VydeRuGoIz8E9GEyVfEOvTOAoM7fY3hMl-kzXomwL_t-ND9VS7Ry1XWcdlCJQzl2xb6OQsPqt_JYQ84XS-1y1MBcgn6UvZKonKjaa3k0zWEGumy1ao9Qh_3rjCx-S7XJxM3AGLOVkBneF2xefwqS_LW3mVNj5ZJbV2zOTjZfa9U8Mxn1vCBBSAGip3OqDQgr_qERdHJWmEpkY0UZMI5bKKbz-yIWXMtLap4XmIwbMKZ6yNgVIef0pySCydqFzZ3KcDxTYLWu9sG8B-myVnd94QMPIakqlv4Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CLC8mYTM675S3yrX3H4jGqtwqhZWNJWwnBPUBp9O6RMbmmWgD6p9yoeAm37RilftGodmcsjXD8wrqMjBTEVUayPTJKU8nLEq6CG4alNV3arXQ5jmzrfZYeo7Z3zQfZ5nW6d873WxvSu_pVv223iJT1YARKYj6nexwavA0QXJaEIIcjTanR9JU6YIts6X9AknhHvfX_WRh-uxoV8xV3-oj3ayZAdESX1EFK_RdM3AAohuuD8VQWXEDzaV_dWLYjgNBVtAaBeJkSQP62iawMIMuu1ABXq4wG1AWccoi90oV-gai18FlR5VXJj-ZXQC6lpuYYzGYjQn058U545Wuij_FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mFSoIgxDYC2p12X76Xm6rFp4Vlir5VmE9gLWVMSkvKBVyBrPlKrtAGzvjjZ218JdjL1hc8xq0Gdc0rjQZKccVIQHLJvflgiizSZ74HvCE77PMbXyksZm6S-hgUDuw75YJNfKiNKQNQUyeiktEyc8xh1LbNC1DgqJ6FHxre51qoQPX25mqaoj05c2p8VIKPH2c1o9NWm6KCpoGms-PB3ygohxbk1Sb3ip4p3X-rvLzvB0jJ3mALal_20BNkAHd4gHGoVDLouFbWMc923l4XtKzlJryRr_mcILWQmIRihEfJaf4J6CkXm7g-2618o7PWKuuQE_4vT7EOJ0yIgSfPEo9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BiUXRt7soZFlvI1yFp3XJSJIQedmNdFB9CA8iuRvbelJdD8G7hsqI3zu4jgZs6jQdDCdgRaMdB2Xud0k-FVX4LycdB_GtoGDLuPJX6c-ZiySimsyijTgEk2C4D7E4x_y6bCjWMVOtq3lgJ3dvq2xYlhDBHmzFoxHo86JU8Lg1IdSkYbzcToM4vzfR4IBeBGdeWPse9ay3SrDQrVDjd1chYI37ujRUDdyMKC0RcFozQChUy8CDN7p83hi1Y8gd016QHb1eCK1eyP_5x1NATylM5_Chhvdp4sY_xICny8Muc2-hkH8cjwdtOFz2QNCPZPFQvr0wLUWV22OoG6H97KgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t-W2UxVMXr60Bb9gc1a2WG67ej3QCpyXHz5QfOTugDWoVZwC8verlqvQm-_e-Tk2gXHvxpWgcpmG6RJdB3mhczri4M3HMljDdtHMSciekuiE82uQ9ksDAKQvmz4a3pbYSSsw7Fmi_zf1b1MkOo_a7vybqwYQi2lPdWokbpHe_x6Ir1usprgtQeW9ibMKSuCV2KJ-dpSPHj4YvBlSIhVtWDa3tJNwHu_NkpzrLTSzzY20l43w139znl1k7YysxTCSVnTMTHdXxMmbU_jjTnJvf9I6SuuON0CNkDmJuPht11LD7UcNLvxCe3ZRucN01N2UMW3xEPwzgansZnkCriS5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aOwP4i-w20DG2xXN5ryXkjb74pfBlAHX50k-dJLw_W-NsE6ebT1SskZ8lt53svHFUnwQBiLF2zWxbJG_zxopbdEFxcVIwoinYOpvBO05rXTTDqTEgiM3ZQipOTcoWaDczMnoyM_LBZO3Y1fjU8ew_j5CSfxUf19nOVDzIFrY3qg0EXwON6P41BN2z0esHATUuzq09P4QZB3C8vv8V9H55_4rhFdrUdxga2phtPy2q81uC7RWA62ZTi6XxSuz9Z0BKue9KoqQlM0Cj3zdA643tySmGHsQDKhn3rLSngdaJ9q2bcvpG03YND3Sl9GVEED1Muw3aXAfMwMCgWTQeEccIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G8VjlXQHapGnoJfqfgkOjc518olXfAzOHcGipo9I_Xdms_zHcDCGNkTzCsWvAPvHBNX8paXDiDAyqRtSZEyVgUpn7GmHdgoiydgsAvhdvYrz48CgZq0I1yJWGLyYpenUm_vOH7g-lZulZWqDVUD1BTMgD90T-M7_XG48bwKdDtGI6yeD6zHChoDNNeB-pusKDReAGSAkEahciqRmE3Win25aBghAge4ubCyroQVBvo7KxYjIBWbxC9ZOlip3Ocilj8qHy6tFoaQSgdYewDhr4Zd_b23NTKm9G6x5GyBJsFU08pSZr4wnSwp_RyA-AScrU2G6qvdS2y4U-dd_uG0YZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PwiI2yu81dcFXYB-VwTXCF-BRkQfhFOAQuvPqtgbKCKcTYiMqkdU7sJCL-n6lhmtQpGkEozYRBm1fhUl92bFM7GiROTKCN190XSC1ljejkqxbhF2RLe7pzvwSxthP2DC8G_zV5KpFdDfuIVzdzL51g8yvIyrIoZDNXk4JDnD_W0NA7fzHlc3mQN7QvpYllGYQiCbkswCPYtyR1LIGW-Db-6_HkN1YB7r44jouvtG2XAPuJAKhOEXtflORaePR6yqUMaGXa_qKSvIKxSgbXiA3B9DhswgPfA8Rp7QUXQarrxsgByZs3pr0m22O2kQ4JpKk3anRt3AGz9aXn9X4bqlpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bKtT_gZD9-WZwFjBbJMEQbOsHpfzfEDwB8XIUZsHM2Be3staeATYmE4Z58T33rFP8NxH40Sg-D6KTWywqyeCJ2IOgdzL7rMDpJQTQGxXk8OhF5MHg_ZbNFSrw3QDCPYLf8ZszAjppkWTW0WBlZ6NWrQcCKpxovk0EBS199aZA8fRWRlsHZjfiFpKtF28JL21Tg2wFHzMSP2wEZ3RpaC0Ewy78sVhuvJBLNoFM5bPNvLwJG29WKnzDFCeMw4g23V2NTTec7YfJ69SF6was3_79zv7sdeokpJKYFzEFv0XzLfyrLjru9DL751tl8lnvZSRNX2OiV4gtkoE0qw_QZY5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ebnbqRLXz0UoxISDMWElt7u-RQLcBAA2lZNdXkiauhSso-nKs2MtqGsasBMTWWHnOdwYpxh2JcXOjzGzd-JhaRKyTVq62z_xUxaSPY-25SkhnJijGoomgS6_YG5Ea56OOkcmWm0xMQ0hC5odSukWwl3-FE7aCk7vl8QPwyvKIeeKi1ynpPHOZiR-6yLsS4RGGiQB9AuTkSHpTdRtMhpF_kffaK4eVf7XWudkUSvbreqTko0_T4cTN84_c7dAMwU0NFq9NnFucYMPQm3inOp1PeTdQbJHPFjnC0MF-clVXE3ylN-B9V6Rj7d-mvu8SVk-gSJwGfSqMCrq7FMHlQDgzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f3TDdN5I66l3hQVKNTU4uE7I8mE-NdRd_CMJZnS9um18I9O6gdXyBwKGya-AG0CMFZAmATs4ZzS6kNBCiNCzFsYYdTGwhD5p6vQCSnAm1Qn6tZjSPNqJLnaQTonhnmDFecqZHPYEsOcwAIe1J5CbwmeGc2dE6MtnGHjV7yv-UVTJdbXEv_yUWCaLVuAy7GT3j52QxbCwIHUFCBN-Ko3LT1ymDh4jaVc5G2pe-xyxH_XPsaxRYJL6gffSreA8bdbPpk-VrpuX5mfzIU5iFNY40o5AZhMBvgp9cgV-8VYaiT8gO8Dx-fpY-Y-eH-3hAgtTcmsJ3LOAFd_7lHyFA825DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ueiRNT_OGfCaaNS9oApbDU9Y3EqFJGwOu2kFBmRe-EnmUo8Uj5MrQJyh72wTshq5FsnT495z7Su8k9y2F1FjzS16uByW0aA_K6AmPd4f29clSQsHWfkuMr5rEW1DhRPPLW73rJDwsdDr9eyvDGG4Uy7P8Pck1hBU5pncQIFxGdONdhYscxRd1ed633MEC8HR-1MZaSY4yhpqCH18eWxwHikspFrvuWUQYyl2yIv8OOvp1FKdbykluDS0UABVUufIJaS8M1kM5Fec3z_3QpvqjRutcGdNi5run8_8sZAARVyfEylRZsXEe6y8dcM2ZHce3mzfTXQCnEOdOdprE4fugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AoRW-sDVPdXuBLjinU9IYC3WgijFqtifBHJMay9LTU9HxNh4tfB5eUCTXJ8kkgdR7yOl3J_VmyZffYxy42XI7b9LAxEQmC_fxt2327JdzAgCKQJhtVWRijTGjhxjaPcMLUgEurmxTRoqr3ecqYSe8fE971-xLGRu0lvUdNZZ7JgU4G4AX0x2odJEwhopssb9mpYavqhM0ijR8WxBIf10gxOXRjMNvJtc50BNrvmFmPg6Jj1MMTjNsGha9ujKOwtQq6N2sgc3RI72VhcmEYq_vSntgB_tyqX2GrtWBPCCPQREqtGJuoALDGMyz-ryIcaOZK3j65LfI9e8GK_QOSkqeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwSZNMA1uNF_wqpTwz0fle6LXWyotA9MzLteFb4d9nlPSUzGwjHgbZQqusRtTJrnG6PL8em85n9FjsZeOtasEwYEQEO_em11EUDRsnKAFunLvxPaEfE2nv-t4ksDnH5nu9tvknVDSCZ9xJBsWTj05KyBrmCQKq0NoIdYnJqSIhHulk4bXPtQm-eNR7X34u9b-DGNnIicRXCKfLzQ29xvfwrElHg-nmV-1Frz8ZCFVUWFgbitXLTJNKAJxMrqcazw53DCczQmLorTCsWjMn2zdvFSQRGkfdxO__u6bGQXzbQuldWhwPyQd0qt2R4ki7JhnQ3hOxo_jVrGMh61G4gXsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=ZF7cvdLPV3avgvgsle3M682Ptn2hChpzjnHphRkLC4bBfIhrbYAIWfjL1gWnvke_8CHlQHKVLypuhBTYd-l38DpfrH6Sv8ODQ2XKoIVZV__uOPUIM1BHy0sqd-LQz5fNn5NkWo57Qs4Hhn_U0K0I_ytAzmceojywc588cZhUSQt0Q3KcQiMsXjkZtVK4YgECBFRih0xtYw9dmFRHQRXVCiVt2SVrIvnUsWzhJpSc9UZyZ44FgSTuEvriv91CD1shEa3q2Xgg77Rv4BQlmHhZDKqUFDLtLyKCdNp8lrWlBfq8wZdGNa08fEnwnAINHbphQV8aR9o6VlOO6H5qntPBGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=ZF7cvdLPV3avgvgsle3M682Ptn2hChpzjnHphRkLC4bBfIhrbYAIWfjL1gWnvke_8CHlQHKVLypuhBTYd-l38DpfrH6Sv8ODQ2XKoIVZV__uOPUIM1BHy0sqd-LQz5fNn5NkWo57Qs4Hhn_U0K0I_ytAzmceojywc588cZhUSQt0Q3KcQiMsXjkZtVK4YgECBFRih0xtYw9dmFRHQRXVCiVt2SVrIvnUsWzhJpSc9UZyZ44FgSTuEvriv91CD1shEa3q2Xgg77Rv4BQlmHhZDKqUFDLtLyKCdNp8lrWlBfq8wZdGNa08fEnwnAINHbphQV8aR9o6VlOO6H5qntPBGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=rUPdRCnLwvWYU5e3y6ukJWr3QwdEmf25bPkMNBk5WXNhTHIVj5d4jGVRX2WyNXp1pCCIbSJzMvtXEE9E0IanJUSO1OXG1NGq8x7qudAIyYKgkzbw3esb9KazA6Q-VKKKhnRshmeuwFkCSxPmAqYghm3rtgrePiejMosIsHxCRHbKBiACL9E-0EavBGZu63ALoTzDOQyWFXxcOehc3ZuN6mgT1_-TSZpzQ0CEj6rROcDnoWzQ8_Nyzr7zypkWXGVQFri8ser-yuBENvZ2TYDWt4k3x_QoIiDZU8D0LGQeLeoDVDpDlYrG8mOBciBde0mFsmq8j3kOSAiMKEp2dlwyEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=rUPdRCnLwvWYU5e3y6ukJWr3QwdEmf25bPkMNBk5WXNhTHIVj5d4jGVRX2WyNXp1pCCIbSJzMvtXEE9E0IanJUSO1OXG1NGq8x7qudAIyYKgkzbw3esb9KazA6Q-VKKKhnRshmeuwFkCSxPmAqYghm3rtgrePiejMosIsHxCRHbKBiACL9E-0EavBGZu63ALoTzDOQyWFXxcOehc3ZuN6mgT1_-TSZpzQ0CEj6rROcDnoWzQ8_Nyzr7zypkWXGVQFri8ser-yuBENvZ2TYDWt4k3x_QoIiDZU8D0LGQeLeoDVDpDlYrG8mOBciBde0mFsmq8j3kOSAiMKEp2dlwyEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UXKDTTxIt1RUrQ8Wj1NsquddYUrR4ZiNKGRAJFewZiY3vLVcmZVizqkmz33iI-38nd4qg6nwnIiHCRsM9Id1A9KfAuNVx6EFmgdRvqGJJYuqxEDUmuNdUv66CODjIpZKkRjWhIjmEOsFOFBdYg2hSPVPMjBK2sFo0qsVMTBFJyX72CK97Ek9L40v1Y2M0sgI-CPNbJrMBJ1MEj5g340-KL7NEzJ9vcLDhT18Zp_jJoEdtF0DXBQp3kc-1sJi0m9ISSZvan9oEuVyYJTZ76_w-G53ZOFcKWBE94jKcEwqdSfM_y3jl01CqkaaVmXbRhJWkRFG13rmpx331qxmqt4upg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eZ-jhEwgBJFug9kRALYD40Mt25Syglm2GsBLcOkhMc-n-RRXAQrYFPd5sj0hDghaBuQ87N2hbGxCUjcg49Rdz-9fMy7JmBJZczfTlVTV4ny3dI8adlSCeI35LY_cNjBTTU2814kZJaCbv6NblTVrjJ-cSo1M-jOCSSYPu5cQVz-Dbjzz3rNtZ872yavZYUbo25olO-401s0yRxgsyoLsqurwNw2uCbOfgnZs21qCicj2eN6ujyH-YApEjxC-xNAeHsaxQSvEZtkj9H2JKJOdyDPTQB2UNysFLytDmgdFUe4CE6cik2UTOZwlOASBG3h06D7oT2-giVVccfswNtsJzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=GY6qShYI8YjE7iojxOC5SYao0kXK5ynGm5lhzyqIoz3RTWWacUIl4Hadh7RIbqAzz9guhIt6pWzPuEZdjpO2ii93-LAS5GsNLHk2FAZLowAIuEdxOcSkCdEvuUMctJRiTA1SIyKbe22y56IhXwIGI3mk9FySJ3dcRFjOAHWcg-YsM0K9YLkc7202YMPbGrcGLe99QRmMAxPzS4vvZxAOwTu4nttkr1nWkOTIotlQwXoQZHHJANTFHYCD35y2QpDTE9OLrlfDP_VLwNBvdnFbaSVoA_3l3WWEJDI48y-9pqFYcBEYewCZLMee6lzeVsvPIDunWK210QhZiCRvij8cvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=GY6qShYI8YjE7iojxOC5SYao0kXK5ynGm5lhzyqIoz3RTWWacUIl4Hadh7RIbqAzz9guhIt6pWzPuEZdjpO2ii93-LAS5GsNLHk2FAZLowAIuEdxOcSkCdEvuUMctJRiTA1SIyKbe22y56IhXwIGI3mk9FySJ3dcRFjOAHWcg-YsM0K9YLkc7202YMPbGrcGLe99QRmMAxPzS4vvZxAOwTu4nttkr1nWkOTIotlQwXoQZHHJANTFHYCD35y2QpDTE9OLrlfDP_VLwNBvdnFbaSVoA_3l3WWEJDI48y-9pqFYcBEYewCZLMee6lzeVsvPIDunWK210QhZiCRvij8cvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektHl7c6DUpIFTyLna6blGOY7BVQLv1n14CgIKgGWk83GvXV7Wy17kvVkZ8Qc_f8JikiUbbnwi76ibdiPL3S24DtrER8s1gLZBa1d8hQqE6ChiNwX7Crpb4hqR6iLzgFYzLGXoxvwk4a0aUmmUHBBmQckN1WKsLFVNZmUGBaA0F62ofAYs1YS7o4-stteWQdhWkcrg4IrA8c2Ex7gT4PD5jyr-dKuH1fBlSW1TOd81veOuTnVBT42iN2zCQ1S3KdK39Ph6e3v7noASUc19jSgyGB4PxGTDKnjR1DfwMbZd94v5SoT5jYBS_AU5OMgDIZu85Fkf_2kIkq95oGbyP0LnxgU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektHl7c6DUpIFTyLna6blGOY7BVQLv1n14CgIKgGWk83GvXV7Wy17kvVkZ8Qc_f8JikiUbbnwi76ibdiPL3S24DtrER8s1gLZBa1d8hQqE6ChiNwX7Crpb4hqR6iLzgFYzLGXoxvwk4a0aUmmUHBBmQckN1WKsLFVNZmUGBaA0F62ofAYs1YS7o4-stteWQdhWkcrg4IrA8c2Ex7gT4PD5jyr-dKuH1fBlSW1TOd81veOuTnVBT42iN2zCQ1S3KdK39Ph6e3v7noASUc19jSgyGB4PxGTDKnjR1DfwMbZd94v5SoT5jYBS_AU5OMgDIZu85Fkf_2kIkq95oGbyP0LnxgU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vGORt6vhSpkcCVOt96a9bKHvw0Q_R0bxkM-LsSNJjKukpjR90A8MtYIM5FQ42DiUwzfXvAZ1Xx6EIwDqKdv-P0ZLmTFsftnnIE8oxBdFF2SPjmkkDEl45zLrRa9L7zjbLn_BKeN1Xs5AeCnraX3d6EXndZZ-Voml8jfgTJT6mxuAm6ztzG_6KulrFPvpif9rikhNTTCLrmwc_S2j3xvcLna-aid2K2wT5EVlm73lDYPFLaEQm8oGt9-vqs3CsKHZ9nazZ-QM1NlZFU-CKs08K-je_go0bLM7U48RyZid2YPy7PMsI2m6jckvgVx06wW_sbLUTFyO8rC7j0gR-LGS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bEZIDrv9mxUnV2-KtOOygT3pWJokS8Cw9yU7woSIW5FNQuqRe7awBVo63zNMiuzhTJw88naRKucSj4xTRHUaTwzwNTdFx3vtNWsTBfN6cw46oIBmeeeV1AxmYfs16MTuA1CBg9HXEBaVqME5rznheNYaYooyWR94FmOb8cC6kCEnJSK_9YPdewaley1Rf8k3yCrpana-ho30P18l2hHjXmlmi3DjPg9fcomc3wIpgqBliGuJH0RO-dFZxPWfgiq0n5BDQIp1QFPhq_t-1ODAHVhsereE50k3pRiR7JlM2o0RgkMWkE-ByF4kvkV_8F5FLbm200jY9_jSkz9c3vWXLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QuZ7kfaML73GQcJ6RlrdLfZFTdgsW4lPsPrKYV2-PQLD5EalMzwLUXipvIQ13Wixn-jMGyMYM_YrtxYb1vY79grboXF-aAV75ni6r_6Phg-5DGoUbXNyFdGA-OlOS4_xWLJ8kxQNz9JtuyX9v1FdPeDSM_jkTLg0w1g8y-KnIUKx1NpOd4YAOI42zIE8N5M1DWDA3Pl_Ky1y3ifSUwp7uogVttbBRfVTrU5jdy-bFDS7SLKmkpODkO8_0vPD51X0TGsdsYJ6HJLkP3xBvmOOjJeJjJ9i_I0SIu2Hpaa1ClNFhTtCGILSWNufDVZlbbm8om0XlFie7mY2y8p5aaZP2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/szlJpn8J3KllyIlUtRI2L6fxdixWejfaP4BsYzYtdAIbWEfqNtdc-28PYFzaUgbSSHCUZzYCqAfYcQLwbPlsAo5EzPFWYOIRjySQxuqlbWfT-OL5qKe5OiNyyIxM6wbVVdZtqjUZSkA3j1mD4pWP25X0m_zMo0AYzmsgkFR6av04qtMFez6ZFvuL4RMBeZ7Kw4hebQdjXtppdq0dhmEEL4H9Rx15tAYS8mTfifZqwD3V9ERno0KRq0dk9Y30ABSJr5TTHW3qcNKSvedyZaL1269cZExZI-nLB0esyhFA9NWXM0qTi3tsM_0gpYnDLvln7A71ZENek3jJwhWyo39rPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/snJAs33tRTTVzKX75YzMyY2Ri087Nbk8xYpHlRdQXFcEsH8Epc4S5RHRzPdIeCYZm4M2-oKkafrG1b7_TqmpCnpsP3EP3A9vNbZWpv_iJrvvkRR0vUt2x8oN370BzY-yt6ZLcOVgYGnO-Q4ajCbotonwNKn-gcNJRu9x0HpKbpgPjK21nFYQP0NCze6W2RegPHN8NkuBDr9AJcHEd5lCLmvsyMhOJccBVGKGylpzs_FRn-O7fV4Sf_3aXKg49zK6dGqq7xF0sQqJLV51nmmqGcF-tALbgnnlPpGaBBJ3AXUjBulWQOrasj2sKTvgrGSYgc5VODb2w1dbRjmj4aRt-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZpsEBE83aHYwfOlLdzPTUBUrLuSEc2kb-fR3TRF2oKDt2m7TKEE1T369i9ji-NFGnC1vw8NvcE-ytsF02VYgSzdUGuiD60CLtq5SK_Mjpo7sZdgFQhU43QHEfph-JWvZrPmTrAx_gbcSh7p4OYgUcQxtEDEIOORdk-de3Syn0yH5qpE6Uyrpta8ecnj57-5zyKxAysgKZ646LSGrfoOvl5bTzMVA5JhyiGPxvf0xqHCKuX7_rAKbdXmgIdbJOkhy4MnZij_MQa7vIz-wmajtHLKelOJDUQeH5bIgiCBO-_vtS43s9-isUTdEs29Z8rXJI_Q3dnpktLVmaagQX9rbNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gPC2JaPyHAkO-VwPbtFBDOh02Bxgk9SFyG1QJxzBXhck6jz7UKCoO_yDom5BTHXIBGdL3dDtBQNj8LrvlDh80dToJlFJaOEcunFuJ7UDyKNQGDrvhtRwVeKc4JX451vE4Jhr4eeQPCwEph0yczYqWCO71eqaEyiVenlS7EFrPnHEkibPMGYRLwwp7dO3U42gYCF4C4d7JaQf430RJ2bGKZvAGE_rYTp877yDNc40yjdFeB57jwoSKUROrXPOo0jziPkF6xnLslJ4BIRShGVlbW8L-9x8m1uRcG8Rs1n4J05KWLPlfwROxb2A3NSvGxuwDhGt0f3NE85Vn_1dsgwGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ML3Jz2cRb6aMWD3gYX43MjEWuqIDnsAMprXwYjfl305fs2fIm2d1KqbdAEowAPRd6sRj6FY3_0_GsIjT2a8oFz3MM28msI1ylemA84ZhgDnImX8o3R6WmB1OzgSHM-PPUk7WjWeGsQV4btMYcoNA6DqaDB82g_kZAzPtwkq8BMBtD93cAkdiLuV6eu53MFYUzL_DwByaun9RaVXPz0JFFk2rfOxgmmWs7sJ2PXDVz7SY45Zpye2O618juW3U5FdC6zu2ezDoqOHDzlSKDVL_0mwGLqHRg8nm2ujrTLq8S1WTea6rsQ7vqZPAaq6zWtYh4kLn7YXiIHxSQCKenIJBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hNf-hiOymqe7BJGq6q1m-vIMh_ORiLP265jYKYVo0R4xNJqni8z9TZ6kBBt8-hTMzTZ4YLOhlAvpEQBQyjhuw5QT1m0TPvj36xyMR9lJBfbPv9Vg4HMP-eiurtCKs_qu9GAhxvSNDnBVjZ-qb2vPZ6RpOxHgkh04zuHZl1Dr9gsUh3ARU86gB82MBCRpX94uo3pgAfJWDa503A57IFL-mupzDiQSn04hJDS6lD3l6B5RuBX9uQWY0pj5YGOdvOmiAzv8Zwl9GBMjls-UPLEZH-3PppWiVjTx09p67KqRMSEU2nr-WDh31JLBX5MCs7nNyTPc69iQdgfB3rT7ZxhZZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZR7jhGA3mj1pcT4wDihPG4E50ceJbKcy05LXntpH04w7e7DubKDIBYALJ_5YJRs9u3r0XnozdaqnzqVvqLwG1_2lkEKIyztJuvnXRx7F17_PG2RdgKLon1rB5sglnIEA5pVaF80AFdAgbcEtaCXxcMOs3vd5SfUibdQViH7J8SOrFhO4_dU2VZC2EzdKl_CVvyIrmwXqOoOtLzmqHo6JuA3feZki7QojAkrYLsdYp0pyWwbJLm9Xp6xZ-kt9dCbXaiQcvsaI71NzzUmMOQh4kHbcxokZoB5jJuPFEvK1Y0VMQkJKQLbzJlrS8v9BrRbc-Of0tCi-C5-OztxuFD9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtFBkE-z7tt9iHd9CjRjMcu8Ue_Q1gd7fb1mK5fCI5TwiV-viE9ylR6SWPvJAOfubw0LLc1BxSAe6LV6_xER6qoX1W8hSysMsFXme4tV-Jc-KRqYw_vPOsJqjPtp5iho9ziKzmbnHhUr2yjO7WOMJEiT767jF-xyLkwKvNQm4lfG11M9EHuUTxb8aS2ijBwf9WKSQm-yub_7RuWSV7jVUYbRZF75pAiiAsE40nrF-ATfB3y44nLy48IdaW9mWAqwLcfVzR1wM0HpUMKGtUKr-rIuFK0HWECHYziwsuGfdmDp7jsvNTQrJouSS80xfYUkKju8r0NIvNx26v54UDlu0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py3llimZTDhNu_5vnsNaCG3rW60G2wTpu1WDwp-L7e_nyZZO731FLouuM9CqG4DjljmGqJJPK9DBn4UhdXs1JPlrDB2Aiw0yiTSqpjiO7FvPR4Z-DCDTLzeNKjdov9RZxYQGb0qOIOhUjdgztV3zf18UjmWMduKP9hdYIT3gGT-rU2guk0VUxkxTK561qOYJigGTAoQ8VO87S0S-9Pazv8EUlwz1kEvk05uAGLcmhGg9gfBkLvQQ45LqzgwNmGxUO5vRkPiwbTJLWKu38vRtu30E2sIsQRfObVTwFeNY1pgkrK74b8043TyqqH25j28GMzXWrWAxyqwtxMj6_VUt1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KR3I9JRBGu9jpXeo7J7phhgPCDJxxtosy008XQMo3nPpqGeNNyCS_yTCOCr06IVd4zJbrU0OEI3BCjGULSIYXTvv4BrcguMZql-D8TSVyi0riynJfuIWisDV0I4L4ygC0jpj-0dY3VU4UDHxqVi4M5oS9QKm2BgSBuKCOu15nFkybGE0TEip1-lzVUBBMbdYBgc02bA4HXp-N95MQIQnY3YRwDbF40vLlNUwYtXOxTCzrfYqJap0wGmSNFc9aZgy7dS8HqauOfx8nO0ssWZFVlsm7MIty2ml8kkDalbkGdbVCczps3xXRRcU-vS7IrkCOf3vz16PQ1tWjLRCQYVzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/puXrpANcPS23iVzPRQFN2hReg8TcV5Sa98cqzk0pIe2-kWrZQUMNwLC3zkh9e0M4JOPIqhiuSQhCaDeklb8Qe6--onQ963hpJ95umYj8HJ-naIkzwG7k2QIK2yMp0aN2ClIfQxMSDlLd6j76ErJOnlHka5VJyLK5VyxxlJWC1tr8ysSf8n6FAUdrZK4b3y94mgeGHjD4r_sT4EB2HSNHPCw2kNzBcro1NH9REEvJBJb0qdLFjUkzPBkzcdgykB4N6TDEatU_bVGAY_bYO7Y142VULeLrx7pWqWxTvjFV3yUf2DP_C_fzQllUXcfw9crccMFCqVeV_WM328hXvvOh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZAIs5YmeahJusDESGitlaGKeSLSxPppRSNPHCifI5gxznHCNS81xDKX2C49KXV8mOXPy-i47LWoPkI20U8qDE6Lc9B0IY_C6SqVk1MYBjZ_5ckVv2yWmydlnfaS7vgQW8L_id28Eqo4w2E7rKS7p1mBiDQGpw7bmzWckaO8dz3BtNFNjVdRgmtU0wtyssLkD5AzAvvOT2-SEWk33N9uaYMrIZqTCqFTfU1PdhUbd1odQa_X4-GFYmX_H2VWORkWagSHKWsmD_f2LNs5W_pqejjKPjFJIkcW5AXq9r2CGrEpU9ARcktq0KlgiYNWfqgWCvwjbsgi5fgWbn-tb6ewJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5kpH23NGIm7uuiAZ9nN5fB_90LEbSdeDDClAswoFv3NNC1o2iJokGZoQIrzyfULZ78dW0uWuathrev7sVA8byVKjz5eIxJcUxxNnXtsoRyIFJRd4IZO4GZqVMMylYbXdKuB_bSto90YKiCgjxwaVLgNom7ilxroZm0DQ4vy955TNCQX_QrGyxU86uOhYbrlBFRjs4c_rjzQhDP-dnn-IcH8g791HRIvfdyvSHymIQyu4BTJbyNt2J8R7RXeWcJkNT5uDZ0BmfCzwQhFALC-gAB66xa7d_MpLU3lQQrjwnD3GcuEJUKh-KZk37t9Bdp9C42c86Vb4f5DRdBBn8Dj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wh6Bl4PD2rBSpml7t80fnqndMURqQJgVVmbbB048vH20d7xiodIfXEHHfveaYbXJLQzpjM8FITyBBKVV0ynksLD2W0uVMbJnpkZg6D6rA4tHyLP-5mOWg6ZLjJ0VnFVPIjeNwkkQG3ssGJ8b6xCZJYH_ghkHeqDxmLY4ikMEIRpvkwU09yc2nW3YSe_JiB7EMpxCbZ8VNXiv34PTIh4xpda3xR8S4zk9AOHn_O9YgL81TmeOxWQ8jpkEwYBW5R4cDjLb72g_OFi2gKq3f6I4kxwxJyxUDCeZgfPd3V8WklJodqbmWWR6-yBCgQeRnq16g3qdnC8qr3KI8vMVGrHYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=HmVflrdRQZfmQwE2c3QIg5_o2hZEk_Pge9JQ8pslaL4XVGmDQfbeaWm8I8fumFUsnlfSgCQ1emWej68DbybdCyHASqWOE9ue6l5CKZRjarwUs6YWEJIo6nZODi8bmMBsPNIWvbauxOxb4kttcnhw3I0tw9cT_DK4FdG-uTLWqcnkMxurA8CYe2qoanWRsPPYp73HYimb6Pat3tR3urIw7C205-tCUdXa6HZjj0per2VV2cb4A0nuZaeUnNHHLYbHiNJflHRj9LP9qMfdnyvYg6udYn2Y4g4BlAITKgUuQcdvswRSOzX6eQkW41NZkmD5ljtIf2M6KydG9WGk84UIJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=HmVflrdRQZfmQwE2c3QIg5_o2hZEk_Pge9JQ8pslaL4XVGmDQfbeaWm8I8fumFUsnlfSgCQ1emWej68DbybdCyHASqWOE9ue6l5CKZRjarwUs6YWEJIo6nZODi8bmMBsPNIWvbauxOxb4kttcnhw3I0tw9cT_DK4FdG-uTLWqcnkMxurA8CYe2qoanWRsPPYp73HYimb6Pat3tR3urIw7C205-tCUdXa6HZjj0per2VV2cb4A0nuZaeUnNHHLYbHiNJflHRj9LP9qMfdnyvYg6udYn2Y4g4BlAITKgUuQcdvswRSOzX6eQkW41NZkmD5ljtIf2M6KydG9WGk84UIJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kKz9AmdtQAK2u5dSXMhnw40gGsCaJuP5IXZbdh7EtAZFUu1tEaaJs_vN9MMkl0Msddd8HVQZxdR5Yvj0AI32sexh8SAyolZth9LrFWIU0_KZ-RVy_GsEL209r-4iQp96mF6EhQK0DaGFv00OunJ0KQ-aeiNBR02vaJDJmPx4AEuabZQlIE1XyArnQNaqJ4b4Uy2Lf2o1-E2NA1yJFVQe7urmQ2xv_7KMqvMsqYy_1qdWaHWogBFJ7mINjow_05jYRIDGXveNZLMhCgsYLfsHr8dRWbscbnKhtY8-wb5HONhsC8knI7GD2ERNOpHhPDy3A_reR3oLJpFNi1_EA2tYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
