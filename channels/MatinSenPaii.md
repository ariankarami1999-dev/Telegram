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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 20:53:33</div>
<hr>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UogdDOYR_XzMnsXIN0hLkzMuy5E3QYN7GK61B5-T6Lki43nMN9Iy9IG37CftXcmOtKTeWfFVKqupNh1ftg0ccgldKyxqvtoG4ifKdrTn5_saybUv5D9Gse1Vd3_x5RvJ29pzpDXtIulQgHDSj17wEWmn75ewuOmBETYLCco7IgY41rm5Pn7VTmfA44p74oLZWSH9pyAJ5tfjLuYC7z94zhcnXcoSNflKMu6RmutMMTriCYWdLQop4giOxqowwUqSego9halMETMN12sDsm8geykdw0BIriQ5775aTK0-XMIP14nSG_Rqt5WvJvsh4QjVXrlif5wXa9vbomQg7be-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEIlnCC3M9c58dOO_4QQKGuf4LEU-1-jZyqMyI3uoluLuPoOKnhUORcA59l0xF_5eToKWZPjoUS97v4lGJCbanZBDPG8JAo4Nj4t9FfJtMOfrk3n2RI7ubCoKQRZEH0wRQFv14t_ef3CCQXIZL6HNM4ZBqYZSbY34XG8paQlYsA8_1sHanmszJzJTNnJqYzpsJfMCBnnyEHdWJ3rNikdMOsg4EOBrGq6qdAdifnlvI6ALV2idj1jMyfx2JCf4KUxJBvfYIfekj6wWtVdI_mKVM3k37uv25Eg42UhyCTp0PwsngmMm8W6H-C3oy-ortYQkta0zHZlc_IbQUHHc2pSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bkronMePW37Xy-n35RXI8-jhLVGeUlTDKAId7CsfofX8qLSSd6IOGgvrQr0ucyjhv_c_kwPoy5OZNzziU6L1v6FElGTUU8GogYHNRYCZiDWaQCt4pG_gGEvY_9ao_GXrNSqgj-vHOl4FnGhALuD4rNlkChjGbPvkmUarYpNvjq1kU9JBrlPwM6hKkWdwnbFS_zp7q89Y3q0gtI8AOBqBG3grbBYSBcYPHzolwMVZ-sQVBNZHgaVdjWkPZy-Ysw03WZxapbgEpWoNh7XyU20alvmB45OiF9kNLtBv6YkKuhdTZXMFv_RZjcfNIT8Qjz1CkNgLXxlmjMjdgY1179Ba4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq6g9ggwZDZ-cx9WJAyI6inEVDfIVGHz2uQH5PlTEXxDPHvCMimqGy69sZf4CtEoZlu6EaMh92Rrx-WZ1htO5v4M4f9oEEo0AB2sda2tnMVpVi7XvmcFzGopb1LXi7qWdCy4g1GXelau__at5_zsv3g0ojenvZIzDCh2uKZxucLyHCqykqfAe5UmZ6_2OLIeYRS92cKo2oMax5ocxxoOsejFiuQWqbYgkTrzdf2DZNORNWfqFKWFgZNApHmVaKdKl8b4iS-7VSnWrSclNS0t_ZtQsfaMDI0qsRLbcJsIdSxg7AhHSNg8RqkjAyQRdEpUm7sVhQkFTVlXDF-agM_Kuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NTsbvwaqzoOiB04gmHyqNm8wPi_Ctt6OSH7MvWxL4zcNwhEdAuPVJTUIxnLIJLjSmbiU0jy6OST-iMgrVcIHHyj15ulYOoiUs0ZHxECUoT2SsseVNtlRdrQcH-NEie8Rgl3Hc3artGoVo56P7CasCE8jhPeIhy1f_yQq_v-12N8T9PA_ycFw6TG8VsRAn10h_AruvtrKgc1Ic2uDZUwbI8KZajSVGjEs7IDO_5BM4AjzExNUEbodsBLpGDw3cc-2RHcxme1bU5BzIv8XJs5iYbwVMy8MiHaeqfBXLFc7yOvdhPZiHxICVX7fQ7n5jwjN9xS4g1R6hoLUdQCATPfdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K_Vmlr_215TOiKco-nNQDhZ9Fybb71pZ82dWwVK1I9QcZTLMPLFaG23DJPK2_2LtgV7FB9hwhOFuf7nRUie_K0mLUA9tgaPTZn3kHMwOP003JSlBDplTWGMytP4oB4piyB5H5tlXs5-d_SjwloxturwhggTfo8m9uQZVkto9YMUHs8Bd_slpH5m6KAV8xH7kOy8_muprQsM49W8ZZacdLkxwr00VEob4hYuzr9TQiSN-4i98EWriG2W2sLQEeVAj8XuXW-Co2jD8WrZvWK-IyUE_nW_oInF8fdAmUFm1Q2ne3r05wfT1w3jf4tK7LAWZxLbL3jZgl_5DpmN1CrXMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v1G_r3zV3nAfcB_E-kLc0yapFQxJ4DGqlyAGHYyVanUKxvI6roi3iPuxNKkJhJbvlpnZn_WW2L13QlzychvNy5kQf42mdQK8DRFoLZzukl9SU5A5SunGr7mmOngdQHRFHgke8NtAuE-DNlIfYmBsXPEBp2GLSvgVAMdUNAFuG5Np68wQosYeL8NgZheZkL2xXPTEddxKBfM7t3TxLL42of9kBcOuOaNofK6DMNhRay27gYlo7S7wS5X3gFht94ih1Byow65bgTbotf6Yi2a35N3JtKX5rO71L7fjCSzL_Vof3oouUXGbsYE4nO777YiFDRDrHJbMqWXunYAwVy5ZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AeQsMAZpzdtJrTH0NWiUdxAOUnk-hgJQO0rhvDBF3ykHNciJibKsv3XewL8cycJ7eF1v80AQvfykNHpSbil7g2ra17jI7e0sYY-eXb_9Oo79J8FyC2jvX-HpzT2vgW-guKLfHBD-1ecEQuVUpKdNwDfAa-nMX-R9WxAcwvBkzsJgGCoQZ8buCCMme4ahNedIBa-nvUyDq888vmstRtMTYWtVzP9bxWcQZarn1rassul5wFAtCj6ve8elIVpgCjF_WFgYyAfmEgiGS2MqLbENL1jXegm0G2BcwW0LxT_MD6W4_oY82qkOUEAiwd0qSRMzfKyX_4nQfVDXR7V7BQ65xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mlJCb_bklgIFbWd04RDhtX07h53W8Ynqq8re0szSzeQ7RtZB3zzcP2T5HIR6wsmf84rHL9ZizzeNToHS5LETtzSc63k_jA4fbroRO6aE6vXr2zOblZL_fDvUL9E-Endygm6Pp3vZ7MHaDPhUXn_Kaoi4-JY7JLMcbpjiUqhkRWr2Sskogzc1PL4L5aFQdMPspRIfR4iEFuBxezGO7S4yRp_G-snASnkpVwtBwlEDKDnfe9Cevxw8ZGROoPi4crIQo4_azsepqKLeSW2zu7zOkU9pBR8CR4TkbqU48ITY9m_225dQW0wTifKhWsGMyW-Uu0iXjhBGGavy3muNVajquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=Tm_eRu3-AnhpTpP4UjWMZiQ1Vs66cX0rKPROvDHQzlsU1MZ-jGlyocnd9mCB_GplWXNU9AS57Zm3l1tf7p7V8b5ObJt8e2o72G_CiFnyvE5c6z233CICxff0cpT2yPb6_NgpxfbBJYp_nA38QqEjSljeLo29ibwXP15PFV8ju_RdUsWmOF950dy2WGLOSJ-mxu7fP6rGDtGXTvNHAQbmCsLYkKZB7mG9nK2zuDTM0x1fkRo_ZSfyA-dSjeH7ZWeU3b-zF9yB6so7A1RJFtZKhoIxDL99fApQ4tfKSk4kJ7QQcqMsYMIcsyIT3y8TzLckk-AK8_VJvicHfvJo5U0B_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=Tm_eRu3-AnhpTpP4UjWMZiQ1Vs66cX0rKPROvDHQzlsU1MZ-jGlyocnd9mCB_GplWXNU9AS57Zm3l1tf7p7V8b5ObJt8e2o72G_CiFnyvE5c6z233CICxff0cpT2yPb6_NgpxfbBJYp_nA38QqEjSljeLo29ibwXP15PFV8ju_RdUsWmOF950dy2WGLOSJ-mxu7fP6rGDtGXTvNHAQbmCsLYkKZB7mG9nK2zuDTM0x1fkRo_ZSfyA-dSjeH7ZWeU3b-zF9yB6so7A1RJFtZKhoIxDL99fApQ4tfKSk4kJ7QQcqMsYMIcsyIT3y8TzLckk-AK8_VJvicHfvJo5U0B_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsvQ-wCJdiqQPyJB0VFsyy2ULN5Y6IuhcbloxERy9SWRhpCiA4xEzJ201lAyJzEJOfEQamBvVbC7yJlGfhvMDMtX2AwAPbq0ScJJ80sZuIcyuS7AUtmY6fNtZyerEm2QxT_zXDGRPDPUY0n-3IM16PKMI_6bNaoneUfF4e4CI5XWmQ930e-52WxQOEvMBhdbfSplmcIRALT8IluJ0NPHZkbNHTKvS4OyqyOKtiMmvDahT-E_mZq4LVCb5hGQEOc2YJkNZTs4ZtHwWuedIY_sohULRL1IoNpzY21hFY5mVMobYNjXh9g9p_HjMREtE4U4iZ4DzL8A8DZ-fYXQ_8CX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=UeQDUDIu67LLTsuKz0TMtZbuoNl00rj-4N7Ex7FZo0peYMhKGbl1oR53fyq78fgdrpkYGmmhTG56XPK-oaHpgLR83paiEryDa0vF7Bl2-Dy5kzidoTTp42Cud3rVz9rttoMZO8DMgnhH_eL0Yn9HrOlsl5DaDzBAgd3EK0N6BUXlFUrKrdV3gi04pBKyKCSrTQmRSnMlhOWLz76b4wemfTHHFelldPY9aEcI1-4ld038d7XQ17I80lWaRgXU1Blh9ACryePi7oXTZlazLHA9iJvhRnUtwD_Cwru3VIaSvCe2ZYiWTE3SMwmKbrwkxt4K8J31IINBKa69z2-RZcGNUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=UeQDUDIu67LLTsuKz0TMtZbuoNl00rj-4N7Ex7FZo0peYMhKGbl1oR53fyq78fgdrpkYGmmhTG56XPK-oaHpgLR83paiEryDa0vF7Bl2-Dy5kzidoTTp42Cud3rVz9rttoMZO8DMgnhH_eL0Yn9HrOlsl5DaDzBAgd3EK0N6BUXlFUrKrdV3gi04pBKyKCSrTQmRSnMlhOWLz76b4wemfTHHFelldPY9aEcI1-4ld038d7XQ17I80lWaRgXU1Blh9ACryePi7oXTZlazLHA9iJvhRnUtwD_Cwru3VIaSvCe2ZYiWTE3SMwmKbrwkxt4K8J31IINBKa69z2-RZcGNUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WgIzZGoZoJroatxBdbVaODGX1oQ1qkK9b6O4OgeD6uYqU1lSxlKHu-paLP8Y8cvkHUNhZeeLmqzD714EDCPnzD5z9ChUUcVQc9mI1U8infIG_BL6bLQcLg6kHvl2AEnogmaSdqPYV-MljsdZ59KXKYqN9en_UC4RVVISFJLTglNYXCto0GRbJuJgnPbKVvHli26unSc5OYEkXqsBSSmzaQunFUcTgq-gtqyLIab5evcxubR4LpP6xslxfbekULiuj7jXL6fEq8_A5HH6R8D1O4mhHkAKTXcUm7vMaoblutnBaz8TZGRgwa2ItfbZauHcPqTUOEm5-CIfiLlHRcIERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sYsj8sqfLlyfpFEQFa4xR08Jp5ENI6tyKt5121z-AKqY1vIiMkLQkovCahlVGWKvHrByYswJWM0pdAqylNAbiOypCCF0tIixaORflmwyYp9o6w-fCNRPJDwcad54_LvHSOu21AC7gxWcLEyBXq5_-ESs4qPgTMxIULCNt8nunqLYkRkB_daHFGYw75M0xt9QtbTKovg9pQwp9ap2K1zonR0IPFLgf1uKFEtq0tyRSawgJbHpspxDZWetBHNL8pQcBVKdn0OU9v0bYVCEt6KwIBxClKHHAAPT6YUPxYK2MXF6H2MCGhn5t3GDSJT11bN8mc9jU9dv8Z_fOoOdrbEQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twmWd89L9Wbh7VRGwKZNWLp1BZlqA_pgH2OkgyXrICHm0kbF8dPe8lH8P__ysussav0FObkQkDd40bWtHcVYYBG6Mx4xuOW2u8oXOAYCxjDMBDGtFOV8xtVSSvm3mNnqn-hYfb1OFfkOdHfjazwHlHxFXuXtR1NKx7iu35wl2uJMHa_sSgzuC7MhVUy0DUR6DhOU9UhcAlEnjd53aGxtoboulzVlVg99_7OOW-3rBWozz4blyBAo2zHPL6-1DtUroRyGOFAMuznG94xBy6bg8arz4Bd-XUzJj2f6wZK3aqHwigbvD_rS6MCJok5iAgYNBw1UhhFWGJBF_sZq_0eW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p2wp_-nW0urWFTfe6IkrFfFzkTP07X6eYZSuMKYAwtOzMwfDfh_I5VydeRuGoIz8E9GEyVfEOvTOAoM7fY3hMl-kzXomwL_t-ND9VS7Ry1XWcdlCJQzl2xb6OQsPqt_JYQ84XS-1y1MBcgn6UvZKonKjaa3k0zWEGumy1ao9Qh_3rjCx-S7XJxM3AGLOVkBneF2xefwqS_LW3mVNj5ZJbV2zOTjZfa9U8Mxn1vCBBSAGip3OqDQgr_qERdHJWmEpkY0UZMI5bKKbz-yIWXMtLap4XmIwbMKZ6yNgVIef0pySCydqFzZ3KcDxTYLWu9sG8B-myVnd94QMPIakqlv4Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CLC8mYTM675S3yrX3H4jGqtwqhZWNJWwnBPUBp9O6RMbmmWgD6p9yoeAm37RilftGodmcsjXD8wrqMjBTEVUayPTJKU8nLEq6CG4alNV3arXQ5jmzrfZYeo7Z3zQfZ5nW6d873WxvSu_pVv223iJT1YARKYj6nexwavA0QXJaEIIcjTanR9JU6YIts6X9AknhHvfX_WRh-uxoV8xV3-oj3ayZAdESX1EFK_RdM3AAohuuD8VQWXEDzaV_dWLYjgNBVtAaBeJkSQP62iawMIMuu1ABXq4wG1AWccoi90oV-gai18FlR5VXJj-ZXQC6lpuYYzGYjQn058U545Wuij_FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mFSoIgxDYC2p12X76Xm6rFp4Vlir5VmE9gLWVMSkvKBVyBrPlKrtAGzvjjZ218JdjL1hc8xq0Gdc0rjQZKccVIQHLJvflgiizSZ74HvCE77PMbXyksZm6S-hgUDuw75YJNfKiNKQNQUyeiktEyc8xh1LbNC1DgqJ6FHxre51qoQPX25mqaoj05c2p8VIKPH2c1o9NWm6KCpoGms-PB3ygohxbk1Sb3ip4p3X-rvLzvB0jJ3mALal_20BNkAHd4gHGoVDLouFbWMc923l4XtKzlJryRr_mcILWQmIRihEfJaf4J6CkXm7g-2618o7PWKuuQE_4vT7EOJ0yIgSfPEo9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BiUXRt7soZFlvI1yFp3XJSJIQedmNdFB9CA8iuRvbelJdD8G7hsqI3zu4jgZs6jQdDCdgRaMdB2Xud0k-FVX4LycdB_GtoGDLuPJX6c-ZiySimsyijTgEk2C4D7E4x_y6bCjWMVOtq3lgJ3dvq2xYlhDBHmzFoxHo86JU8Lg1IdSkYbzcToM4vzfR4IBeBGdeWPse9ay3SrDQrVDjd1chYI37ujRUDdyMKC0RcFozQChUy8CDN7p83hi1Y8gd016QHb1eCK1eyP_5x1NATylM5_Chhvdp4sY_xICny8Muc2-hkH8cjwdtOFz2QNCPZPFQvr0wLUWV22OoG6H97KgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t-W2UxVMXr60Bb9gc1a2WG67ej3QCpyXHz5QfOTugDWoVZwC8verlqvQm-_e-Tk2gXHvxpWgcpmG6RJdB3mhczri4M3HMljDdtHMSciekuiE82uQ9ksDAKQvmz4a3pbYSSsw7Fmi_zf1b1MkOo_a7vybqwYQi2lPdWokbpHe_x6Ir1usprgtQeW9ibMKSuCV2KJ-dpSPHj4YvBlSIhVtWDa3tJNwHu_NkpzrLTSzzY20l43w139znl1k7YysxTCSVnTMTHdXxMmbU_jjTnJvf9I6SuuON0CNkDmJuPht11LD7UcNLvxCe3ZRucN01N2UMW3xEPwzgansZnkCriS5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aOwP4i-w20DG2xXN5ryXkjb74pfBlAHX50k-dJLw_W-NsE6ebT1SskZ8lt53svHFUnwQBiLF2zWxbJG_zxopbdEFxcVIwoinYOpvBO05rXTTDqTEgiM3ZQipOTcoWaDczMnoyM_LBZO3Y1fjU8ew_j5CSfxUf19nOVDzIFrY3qg0EXwON6P41BN2z0esHATUuzq09P4QZB3C8vv8V9H55_4rhFdrUdxga2phtPy2q81uC7RWA62ZTi6XxSuz9Z0BKue9KoqQlM0Cj3zdA643tySmGHsQDKhn3rLSngdaJ9q2bcvpG03YND3Sl9GVEED1Muw3aXAfMwMCgWTQeEccIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G8VjlXQHapGnoJfqfgkOjc518olXfAzOHcGipo9I_Xdms_zHcDCGNkTzCsWvAPvHBNX8paXDiDAyqRtSZEyVgUpn7GmHdgoiydgsAvhdvYrz48CgZq0I1yJWGLyYpenUm_vOH7g-lZulZWqDVUD1BTMgD90T-M7_XG48bwKdDtGI6yeD6zHChoDNNeB-pusKDReAGSAkEahciqRmE3Win25aBghAge4ubCyroQVBvo7KxYjIBWbxC9ZOlip3Ocilj8qHy6tFoaQSgdYewDhr4Zd_b23NTKm9G6x5GyBJsFU08pSZr4wnSwp_RyA-AScrU2G6qvdS2y4U-dd_uG0YZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PwiI2yu81dcFXYB-VwTXCF-BRkQfhFOAQuvPqtgbKCKcTYiMqkdU7sJCL-n6lhmtQpGkEozYRBm1fhUl92bFM7GiROTKCN190XSC1ljejkqxbhF2RLe7pzvwSxthP2DC8G_zV5KpFdDfuIVzdzL51g8yvIyrIoZDNXk4JDnD_W0NA7fzHlc3mQN7QvpYllGYQiCbkswCPYtyR1LIGW-Db-6_HkN1YB7r44jouvtG2XAPuJAKhOEXtflORaePR6yqUMaGXa_qKSvIKxSgbXiA3B9DhswgPfA8Rp7QUXQarrxsgByZs3pr0m22O2kQ4JpKk3anRt3AGz9aXn9X4bqlpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bKtT_gZD9-WZwFjBbJMEQbOsHpfzfEDwB8XIUZsHM2Be3staeATYmE4Z58T33rFP8NxH40Sg-D6KTWywqyeCJ2IOgdzL7rMDpJQTQGxXk8OhF5MHg_ZbNFSrw3QDCPYLf8ZszAjppkWTW0WBlZ6NWrQcCKpxovk0EBS199aZA8fRWRlsHZjfiFpKtF28JL21Tg2wFHzMSP2wEZ3RpaC0Ewy78sVhuvJBLNoFM5bPNvLwJG29WKnzDFCeMw4g23V2NTTec7YfJ69SF6was3_79zv7sdeokpJKYFzEFv0XzLfyrLjru9DL751tl8lnvZSRNX2OiV4gtkoE0qw_QZY5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ebnbqRLXz0UoxISDMWElt7u-RQLcBAA2lZNdXkiauhSso-nKs2MtqGsasBMTWWHnOdwYpxh2JcXOjzGzd-JhaRKyTVq62z_xUxaSPY-25SkhnJijGoomgS6_YG5Ea56OOkcmWm0xMQ0hC5odSukWwl3-FE7aCk7vl8QPwyvKIeeKi1ynpPHOZiR-6yLsS4RGGiQB9AuTkSHpTdRtMhpF_kffaK4eVf7XWudkUSvbreqTko0_T4cTN84_c7dAMwU0NFq9NnFucYMPQm3inOp1PeTdQbJHPFjnC0MF-clVXE3ylN-B9V6Rj7d-mvu8SVk-gSJwGfSqMCrq7FMHlQDgzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f3TDdN5I66l3hQVKNTU4uE7I8mE-NdRd_CMJZnS9um18I9O6gdXyBwKGya-AG0CMFZAmATs4ZzS6kNBCiNCzFsYYdTGwhD5p6vQCSnAm1Qn6tZjSPNqJLnaQTonhnmDFecqZHPYEsOcwAIe1J5CbwmeGc2dE6MtnGHjV7yv-UVTJdbXEv_yUWCaLVuAy7GT3j52QxbCwIHUFCBN-Ko3LT1ymDh4jaVc5G2pe-xyxH_XPsaxRYJL6gffSreA8bdbPpk-VrpuX5mfzIU5iFNY40o5AZhMBvgp9cgV-8VYaiT8gO8Dx-fpY-Y-eH-3hAgtTcmsJ3LOAFd_7lHyFA825DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AUomk40Rr8bFXN-SzbEpPXLB_EATta6mmqhBVDa-3qf_uaHDtSNIRPI4mgYufy__l2GO-ad2_gJiA5-QHBG3Kuj5uZ7YyH_QDRbIY9iKnkJb0wEr4yNxlLAI8W1LDm891nQOuzAwbZcaZItKi6TS-G-X37xvzz4TALIdxGXlHTuSzXfaqFG1Qe-xsrnE-NDNbkx5TOeh_GKjLWwDWUuzi0q99bSZuqUat06XXZ9BtIxg8qXYGmpWr42rYjIs70lrU8l9EjRpmj_0_ukCuVUvX1Gd6aMKQPut4ROWLW3lLr-4Mm4JIH09CBC33N2bLwdco6sGE5X7Kh-r4wGx0-31IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g3nimxXpHrmLNCNBxkOTTtFVtQiiuPh0Ls87VQsCW0k204l1s_cIPuP2sfDt8itK_MTEAinHz-3uJkdc91GPWVj-h_6eQY6bRCWjrbPrdKves1j-wzBXLgXyR4-cTcWgh6ZJi3cTpkzqxFxhRXfVp8L3lM_TCwqNPjwsCreqfuMEHqqlIRKygRDWJN35h2nL62EJuA1oN42dRX9oFA-M6XXfoGG8TZWlXK5pYv8jBZv9VhdhSvdpYSRHSjFBhRycLuuBGRwTY35Dd_HsQTJA-rrrvgzHXikl65mUgxqR1uvkOWA7xnoHYjP8jA7q-hI-TTkLsWRYQ2W6qvM4ZoC4NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1WThxQoSxdRiSXpVLxu6Kzk7t-RO8CA4a0y0vqdqrRqjiVpDHWJelsQBxEQoviZissrGTSk2Fv2V9aXvFzpHSqOPDYE928XNBainC9KDYl5iDMH_IYaj1hUem0ywqK-ijzEL8A6auoGwuEUkLytfbEbVKu3L2Q6_iCg9lKmulxG5_I-lyEvH91nx0S37RcW2gbj-rz8hCbVADY2waHHedWqdhOnc4k9ms0Z21u-ftipQG5fmJbFSrh59YlGXs0qxpObycob7Rj4iwLH3f56SU5AbB2b4tue_TZ8hRKf1Faxj0fJP-8jp0fZooI5jPAVS3k8dmehKbU1NDW_otr21A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=lqnwBnqhmWLJ70KuI80hxk5St2P0lZRTQH4FJaMB0wgWibhmZZC1kGT0e1bEkfM65k_Q7PGJydKW4IQyXX-lAwcPmu3Qrth0NUHm-y5YKq45JO4Pk5687QJy0xSBtlM6ERMOG7Mfs3kbJ76IQEDR6Fn3f2p7rCEdKeY9cyj9h3d3FPh3JpNSWtgAr8Y5mm_utQq1EtpwWXpGaLcHSpp7velUSnksry-IKaCRdcTADOOJ9SPlka_PilTD1tTB6lyW225HnZmlyRaK3UsQs_ERLcwt2_-I7s9n97ZU5U0d5u4O1QCzFVvTfHf42zVcNsv6KZ4nU-wDjVdeWrMYM7xtI4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=lqnwBnqhmWLJ70KuI80hxk5St2P0lZRTQH4FJaMB0wgWibhmZZC1kGT0e1bEkfM65k_Q7PGJydKW4IQyXX-lAwcPmu3Qrth0NUHm-y5YKq45JO4Pk5687QJy0xSBtlM6ERMOG7Mfs3kbJ76IQEDR6Fn3f2p7rCEdKeY9cyj9h3d3FPh3JpNSWtgAr8Y5mm_utQq1EtpwWXpGaLcHSpp7velUSnksry-IKaCRdcTADOOJ9SPlka_PilTD1tTB6lyW225HnZmlyRaK3UsQs_ERLcwt2_-I7s9n97ZU5U0d5u4O1QCzFVvTfHf42zVcNsv6KZ4nU-wDjVdeWrMYM7xtI4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=BapnKkWhlva2TLAQAZns3_OuOJILkHTvSuScSQidljX2Lce63BoJsCBdS0iNMAAFBUyckZeDKi843qPJjcIagWG08G_S_jtz7FJTezQaRRbbLSwxn5zmjgvif_orY4nWt1sJ9kPjiSAs8V24XHCtuWRi-ZE1fLOye8jyPNz8trmpA_rENtFCBF6ajcvn8ZoNlh0TCexFXubwKW1YNovp6W_SWNR53PUqo6l0mvZ6QyqwOt8Iqs7Wa5kIb280ePDNQzf6sQj6bYwJ07qmtYYm7WQN2p8b07BxZzmh4rrrK-gkOvW9bd4hJptDVTzF4VPXN_LtxPX6UQogAFTlLpCj1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=BapnKkWhlva2TLAQAZns3_OuOJILkHTvSuScSQidljX2Lce63BoJsCBdS0iNMAAFBUyckZeDKi843qPJjcIagWG08G_S_jtz7FJTezQaRRbbLSwxn5zmjgvif_orY4nWt1sJ9kPjiSAs8V24XHCtuWRi-ZE1fLOye8jyPNz8trmpA_rENtFCBF6ajcvn8ZoNlh0TCexFXubwKW1YNovp6W_SWNR53PUqo6l0mvZ6QyqwOt8Iqs7Wa5kIb280ePDNQzf6sQj6bYwJ07qmtYYm7WQN2p8b07BxZzmh4rrrK-gkOvW9bd4hJptDVTzF4VPXN_LtxPX6UQogAFTlLpCj1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lOZQP23PscVFlcjv1hXy9IPl3n0cDyALgL7Px0Y1GwiDI5DxfXY_IJSZArd4vD_EMHaFLfe90X3VVx4bSPRI230CqqmaKffNY9wrwzW6dGVKJtIaQzMclkiEPKUS9aIeaIYXprCnjSo4f0Dz_uUVFzlCP2UKGdyb8BqNWaQd6Q3IcPwmCaoVSz5ONSOc5ElzI5641FImSz-onrvyq9qz3NZkOiJfVZSe2ILnrUIAtkNBLkxsBZ98L55mtsAwWgtsOfj9C1_eEAgYffwGPSf4rQLLHBHnijLsysByUUCpIAnofvONQ74CSWBKtaRJOFuTCfpcNIJULoC2ZrzndiIuag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eZ-jhEwgBJFug9kRALYD40Mt25Syglm2GsBLcOkhMc-n-RRXAQrYFPd5sj0hDghaBuQ87N2hbGxCUjcg49Rdz-9fMy7JmBJZczfTlVTV4ny3dI8adlSCeI35LY_cNjBTTU2814kZJaCbv6NblTVrjJ-cSo1M-jOCSSYPu5cQVz-Dbjzz3rNtZ872yavZYUbo25olO-401s0yRxgsyoLsqurwNw2uCbOfgnZs21qCicj2eN6ujyH-YApEjxC-xNAeHsaxQSvEZtkj9H2JKJOdyDPTQB2UNysFLytDmgdFUe4CE6cik2UTOZwlOASBG3h06D7oT2-giVVccfswNtsJzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=RbtsGzF5wYLhBq8q34HJ-8C11_NxuTduTncgdIcZo2DjD_XW8XdyvK90PH04Et2NUhMnyGDIGnNy8m-SEAZvTY8TNn-AynjeNvJyhac7dNJgmJj92wrPKt71GnZVJKOtGRcDWZ_hn1lf0p_zUZ8NExy6_eOwXGkyCmU3a96gIZ4J0Z6TRh-JXICbDu_d2AV4pVguNt2vmfObok37NtTtMuFfrGcR3qps3u5pvVVd2VhAQlFNTQ0qkuaygWhjmVI_GwFRsdYv1ywGhl2sa11AGtgJPjctv7UeXhZspZpO1KjtIzUd09bKWIRHmhgp9U7DBo1sxqyTWRY3a_D6BfP-NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=RbtsGzF5wYLhBq8q34HJ-8C11_NxuTduTncgdIcZo2DjD_XW8XdyvK90PH04Et2NUhMnyGDIGnNy8m-SEAZvTY8TNn-AynjeNvJyhac7dNJgmJj92wrPKt71GnZVJKOtGRcDWZ_hn1lf0p_zUZ8NExy6_eOwXGkyCmU3a96gIZ4J0Z6TRh-JXICbDu_d2AV4pVguNt2vmfObok37NtTtMuFfrGcR3qps3u5pvVVd2VhAQlFNTQ0qkuaygWhjmVI_GwFRsdYv1ywGhl2sa11AGtgJPjctv7UeXhZspZpO1KjtIzUd09bKWIRHmhgp9U7DBo1sxqyTWRY3a_D6BfP-NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=FFkgXGljIevuinZOXItZGOr84lmNuxIvAaKYtNe-nxTsqpxTMRKGjKNIEq30lTN04ElfVgPgab9hpM-JWtHAeM2eoVrSU7j7BdmGEQbewZZbrxBQEnCWUPOtAMoTiEe9v8CHwQUmYDjOyY6ic-O4iNjOTqEXGE6bGcTBVZFT8WHptYuk7blCJ0nX94p8VFZMWIRx19dNWRg1vt-W_NA_FqnTD8l9BMOCFvV2kcRKwRXM805Lwa1keDj2Idke7uNScxT3lXPz3sRrX05OWRix8QvgV1A5zLoxrIm8bHg_QOkdTgjr9sXCSbv0t6zya4lrXCpAmubDZbmeymE1NApW1wLpYGvbY0BVK4rR_UtVN4BV-c1PQskvvWvVD9bsHIufpxbrOezaeacG8c3RunEWa4OZK6MYP0sthSJPOln7o-murjdp6Z5loRwY0L-Yq05CAp1LVyB97R9O4u-nHwBDam-afTUQz0-GB9RowK3kwy-PEC1oICsDF37Nv9BX1k-oyeCA5rDdwNib-PzSqbD3ZOdSjPi9zQebToOP25GqpZzZhTrwxJG5pl3DeqL-2ZAp3uiHggFOd7wpxCjp9ljLmz1AwJ84OHy9H1FATs9161xcx3lRiEAlVbDP2lZDnL8VOZ2ySUux4gUd7YfsQcdwCgzESu7BoKL4v2qtQPQvfV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=FFkgXGljIevuinZOXItZGOr84lmNuxIvAaKYtNe-nxTsqpxTMRKGjKNIEq30lTN04ElfVgPgab9hpM-JWtHAeM2eoVrSU7j7BdmGEQbewZZbrxBQEnCWUPOtAMoTiEe9v8CHwQUmYDjOyY6ic-O4iNjOTqEXGE6bGcTBVZFT8WHptYuk7blCJ0nX94p8VFZMWIRx19dNWRg1vt-W_NA_FqnTD8l9BMOCFvV2kcRKwRXM805Lwa1keDj2Idke7uNScxT3lXPz3sRrX05OWRix8QvgV1A5zLoxrIm8bHg_QOkdTgjr9sXCSbv0t6zya4lrXCpAmubDZbmeymE1NApW1wLpYGvbY0BVK4rR_UtVN4BV-c1PQskvvWvVD9bsHIufpxbrOezaeacG8c3RunEWa4OZK6MYP0sthSJPOln7o-murjdp6Z5loRwY0L-Yq05CAp1LVyB97R9O4u-nHwBDam-afTUQz0-GB9RowK3kwy-PEC1oICsDF37Nv9BX1k-oyeCA5rDdwNib-PzSqbD3ZOdSjPi9zQebToOP25GqpZzZhTrwxJG5pl3DeqL-2ZAp3uiHggFOd7wpxCjp9ljLmz1AwJ84OHy9H1FATs9161xcx3lRiEAlVbDP2lZDnL8VOZ2ySUux4gUd7YfsQcdwCgzESu7BoKL4v2qtQPQvfV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e-nWvCVeMetJAihJ4hV1bpFQNF7mxfQGAZ_tAWSmuRfalEZ4W9yYZxcsoWyH-SMU7pLJk8qmpoBCFLzLxEV1tZTvFoLVtm45mT3TKNDftMI5Md8X00Ipfj2KtlSYmPgMAJQMK4Y6AefSg_RC97puVi2F2zYWfh200GOklummz3ZE8w1-cW4bEFq4MpKKpaLQfgAkoqLRgWuI_a7cd2waokIL7x6yR32EkFnbluQkZzKS9qJBTAairM5HUeeAvongrpZFJ82rDIrpUvhknklemrL_xRLFJ031R4ZV9Kn-lqZJkFryG8wWPo0L6oTxvqc9q_izKI6k0oYtRdX62hnkag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TdZ6bcG0qJLskry368T2LJAe3d8zL88tZsisxUx69ohr-3f80aL7U-H4IrzQja7RoVdpsFjoCx0JlF0lfph3c98PHxntEoiwVYPN72PlwVj1AJpxjrS74sUkSK4RZBZBVHCZwgj5zlBa2-kjtFywntRBRpxvPPoPql-vCCeQmPl5wZdQ8ojXS2Qoy_PCp2W2ZnKbnQuI1SDus988OBBBm_-qU99IYVF9BUHmxuPNjDaUerc6HEAqha_tC8LbTlN3evUwBbSq4yz1JZ4Tv-f_hQpLO0vmG_-ytXyNN3wIZ2tc-9DBR1Wqcj49-Duhmnw1ltv-1-Md4AKvgzGVcnZ1qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KnHU-EBoPLBk2j39HwTBVybWleZc7VR5njNHbMRnQ3YEN415MW8LCzDtWmJP0WoQWg_7XpEn2B1YOdiJrZPXjV-jiJqnUT-735S1jk-ElFmvziAQFktyd6FXtrin0DRc_tYoaslcdLnlABfnVlFCErxIXZV2rK1XSAVzPUsQTvGC5SilPcFyuVWAOwuDHtEN9sG6Aci7YchVLrnEGM9OOfyDmjYUwfHGgWP6P1iQD9zpmLkwlZmMgvGF-cobwSdFlDZJVStkCgtgdc0BUgAsobZ7VqM9oemQjKWZefBp1jbRBlQH7e_8flURsvgBCxGAxFSpYXD8M0ywnMCsmu-Cog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LxZZXwFFWKshW41HdbTMyiFvj_psWYJpVTNV6barN63pbcle6-Gvat5z1ifl_5mzTWNc1D8zPwkwTieACY_v0XIApZhyRD0Uos6hKzXpDfpKHAJL22MEtLT7RPj9Slj80tRMcRe4e10ffoU4qKYYEcY4mZ3FQJRfVThlhDpXwvM3ZCV81DCz-0IVYeom0GLrkerU1bKSAIazLvaSWA_m_iZ-2E8SdvsbDMYC2AYDgoN5kWOC67Zsw9T2GYYXalj5yr108AXE0kpnpIR2V8Cz_LtbrRoYFvbdb73mHF3Ww1fERWf6bQuuMvAWvhgWK51rrF9ZLJivA4MnGWacNpGs-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/snJAs33tRTTVzKX75YzMyY2Ri087Nbk8xYpHlRdQXFcEsH8Epc4S5RHRzPdIeCYZm4M2-oKkafrG1b7_TqmpCnpsP3EP3A9vNbZWpv_iJrvvkRR0vUt2x8oN370BzY-yt6ZLcOVgYGnO-Q4ajCbotonwNKn-gcNJRu9x0HpKbpgPjK21nFYQP0NCze6W2RegPHN8NkuBDr9AJcHEd5lCLmvsyMhOJccBVGKGylpzs_FRn-O7fV4Sf_3aXKg49zK6dGqq7xF0sQqJLV51nmmqGcF-tALbgnnlPpGaBBJ3AXUjBulWQOrasj2sKTvgrGSYgc5VODb2w1dbRjmj4aRt-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/azw2aAAV933fLZ34YLegdYYL3acPGkYm2EOrU9ZmOjyqHLUxQNEV19ERa3ljAz3MvXxCHbdCqCA2M9zwCCjyiLe9RMK_MUbuTNPzhnBeHsvHj12VETeHGDVf5g0xT05_yHbkfqrsnIawZj0oj1oS1ASDohOAysbP8p4KgRBqKrjwzWBsqeKTYtTRqHmnAL0dkvqBYHry-PCyPwVCRp_kyvaXpTkyOMwrMeil0FISEhd5BxybWz-iGv8D6aOFoWExeavYP6dvzyBVDChSn8vJfzogB3XOgHsWVlrHFtsIWnYKgUzNW2cVQz6UeSJ63-2sOMk4oYn2owAKldyG6gcrdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RzixQvs05I3EMbc8KK4cBd7agSyrt7rGuCNNz3wWgwTM8w-0EnX8UMqJsct0wXWnleY2eO-jLf5837F9EfoGrCSXHhb_G_Vfuwfj24W4PwcMet-dyHYsKIimoKkADDucUCYjZfInrabg_5PNLXs8_Y90ZqHaWCDWWiR844hE8iiZX_NVrSX-2hPxIMXP6HCc83dvqjbmeMKgViVed0r5yOC5QDS4_NBv14fBZwMEfWAFyDSktw7h4JvtrqAqs1W7XV1gyd1bM8sdEainEDcg6AHSkz0gPBbRY-Z9IK-j4NiDi4B9O0xTOeGnhzldxRg1hxkJbs2teVM75B3e592p9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KHdFAJvJy_39Sp7Z950ICHf6XVisjQJ33KMUsIgz9ZCbXZNhjnxJSGPNK62X2sIzc7i0f5r9-e4N9Dv63epE1_zLq32mk5l5U8gf8NlI-w21CrxPgCHIsP5HPxmRjkTVNL4LYYNF3X9JRbHqeGdOaD4dJp0ehmJrNzGLHlUxagncjyiJ9-gHNgdBI6pYvLgS0oKCpP-KM8pIzTXyyTyZhsgprBx3eOpujurOWJp9CZ4ZgWCH8xyMt0b7LmFscVqtvWzLhu0P3F7m1a4vPqwEC8I7X5ph7x2b7ouGKY__7U3tItQemCH3QXQq7aRl2R7XRfy7EcaYBHKuea59LgqdFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uQqLnEJoKsnLWH-6Mf89UU-_FP_Xb9MdreSrR4CTf5lrjLOqqMdrKH1kQxwPyySQDeS-Wk9UU0HUrZPdUQhhKYXJeao82tVhaBkk74GH0yhtQVlh9ceE6mr8pmUXcPtbWFKPNg8srWByCH4T0PKmDi1KREGkXNiFEkNpfbMxzKTBIJRz-1gBtk1RkWgOUEGq51iMcoOHZw5MroSZDSmGOj5K5NNSOehfrYSHM5B1w_0S94nrzOhJi6HIOQjfbLnNzLHXGSwRjOXYtDQ_MrNSaQfhrD2oNaodf_-Ez6fjqC9rE_oWSCG_89CfvGSf_QPfz5I9GVYKVKBOjo6AjlAYrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_bcrNYREhw-IBf-SeFudPYapIClk-YWIJAgx3kGe6V72zIwLKNpviAYs5rt4ry6I653Uz1R_JOsQGkYIKTPFsatqPWngzY3ui5cdcjsnA0iYbUvrBat9zxsLYFHvngd5gQugnrIR_wKz1tUdbjDsWvsoob0J-R1bhw-YT0dxuccZEt9smm2cMJa4-ZKDxxkMg_j09NNeD8o2AttDZs6fuGBdynbQ0KUznXOslMmuO6eNckDfmTyFmkFcoaBnMn-l74dygnF9RpvU8I2KWxdGp8We8vCrtEdfXH5EIURgGCB2PrDRoqKxitRQwftqQca4l9mi6QzWpYNwHZMERicDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcP1F7gaR0mh4D-s27U4A5MRLJA51w-7cUt5NOKW5QCI1PLRPV5bnw_wNSDKxULOd2Kv1df9ZQ27m6R84PKaR5S-jmAPVdCTH68ZRhY_-1DvbcyAFc4F_d5J_j8KRmyYg4DAe2Bf91CVB7VrlWFGoeajkaCkGaXO4ukHEcfHlzt35g1vqaHNczf2Wrvu2_X7LxNyYo50P12NYZcoIojlGIze5qlL2jXPd_THdl5u9az6mIZ1jyqwX57Rtqpm_vrQs3E-sBmXOLSDFkoZSpBZk7lpbx6-YrRpeZdRCUZOsvjr50AXSejqjSXnVxVLOWJRcwQ4u0nkw2khLRxLs2c8-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQLaRVY-DkwpyZhM_JBRgUVliTSakTu6iElNPu4HckSHjjpwoQRRvEU62S_czzbuQ2qTRqQ1TVz8X9NgRUsGoceqnbXWPWQbRsZJ996OCuypIbJujzmm-i3N_phKsod9Zwrp3w1XGLDJ8zcWryLsNMIuXW2NBQvyjd2VsqC51AvhnrVxy7bXFutB7e_6lp59fkBd8Q_xS8IB3E4zwYuFk46anL_E2_sURWwks3ea2KPYkEa8k9O3_KX04FDMEJPNrHht5AZrLoB_isoJ88-MgHf5059nviDaKNUIBrTR7XH4vec8SdiyKvkw_OTB1QnyvZ2KfwVaAjHQs_0mT6im0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QxcHH6_CA3Dx0qZw83WTOD2LeHWXXw7gzO0WuRvFACvhhkWI06SmYGxVjIl-3SMwesnjS23LjsM-F1Pb8AnftinPXiFSojsPNGDHPBAvkaBE1rrPpoIegairH8_y-gelo3WhfkPP59NAyBp8UcvL4ksnnCa0suWjrgkbCs9pJHceLqqmr6pbSkXDUYOuQLCF22SMBwykl1cUlOe5_r9vBoz9RT1BbO4EW18bWtMqC7s5usrLt1SabNFK8uEiZ-lW4kgt1gA4yZBHzCCGc5q8GI49f63WtrCI8oNze5hLvSgivFiAWaIwd89otel51jWHnUj8jLbyif2ifA1zYypBWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pco-eyOF9j1Nhcy-4l6UUU4zeY2I4NuT8VSQXrxnpjn3ohf1mvcS2epxu7eGZoDxrbtlM3XOiLsTYTig_daepdPmemTEm5uT9CbpYW3u16LYxGHzsGPYt1bI2TxmXiq3oOKnqSIcAROsTMm2A4y66nVEFfPfgSczHTF17JuIVFYQnhpRIrek9dyz7CfuEhzgy-Uqgiu0JhZ5bzSYUYG0vFD5oFPM0bSITflzy6cWT8f7jzxVSJIMR1xTcVbpcZuZxfjQ-BWw3y8932HdJQgmjHKDgOJins5jrkBJvBt-izfxdQYVY5Jx6PzamAKdEquecZOWg4K4-FVYLoYbaRNOWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kIqK3uX-pyvD0zsJBGJ7V0PdT35aLpo6ioymYsUBhihldUZdnEwgJUCjTnRiRCqqVd-QGhPPisaPUf81VJUg70iCgx3h9LWSFZUoVyJLykYsSA-nnMUCJ3vZVoRiakR9RZAOZq6nhGNDGXiD9Lr3H3iVlZk19vV09u4xbLcYYqrOkAfoBYEIPACZN5EceWlrlKGWXP6i9wH6OW-3e1UNUumlK-UrNiWR68UQ8AHmfm4xW81vgSU5Vhvi6RpSDMVQDLmzXZAzk9JZ0gsZFvmwNuwtRoFFO2WoPJopyHm8jucl_HfQ7WmKL0-aVDfEfjHAXLJQhYhYF9LvNRxneKWj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttUoGSWuTbOLqoVUYU-3YnKxKXiyKYNs1UGxhtg7-zp8yuMQKSNOm-UQeOg5bfJvEco2p5_R2_XMsNCn0V8AcmfMGAa8BmtBXoGjv6mIP_1p1kQl_5PD_vHmI56JFghjfH35zL-cWwS7VfZtDTjZhINon6uCSTTIrFgvBanjZPSjn4gDUxKlyVHwWf1ktFN1iSoQD5kmZGm70UuQVdo22LyIDU0lb1caPxkvpheqChX4LSar8rtRIKpqjiieXQR7J_hAdvdYZJCTPEghRCs1xRfBqKdYrqHUNE9BYZT7bXyJMerOyWueymSWfD613I8ChkNK73-o2sVFsBVOrwwaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
