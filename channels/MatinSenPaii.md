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
<img src="https://cdn1.telesco.pe/file/sCEp0nEzHmQ3vAqStqieHgam7b0BVpx84rh3DJ7w9zqWatj9stQCUNvgwzzSBrFGd6GE5Bo01ba1iaXJuIaHFW-0FzCNZZQXVEWL1IYbhIYth2mdGo6Z2KygUrEcNiPj1J2-TJ5Cc1IOzYyiM88Af9LpuSt1oTh9pCoCagKijcM-WFvNLOY-FYsdxR61XKJSkyVs1Z8mgfMYAERF4Yjg6Op1vQHxkQ1NdOyVi3uGLXMuFG-7oWEg8hf1BqYT0NfIMpJZ1j788RTJmgZVeH57ECX2dXIdEM22JrsI9WmCm3qE1adKu2w77cOqXQbV5aLv5t9b6O7Kr3AREE-Z3cUCJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 161K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-3938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KJQOStGowo9wX0ZArYdJgqnux0r2caX3ATC7PX7isAw-inmgMBm59gtbRHSDV_ZndTGsHnObo3b9q1zUtThb5d6WV1bL8t8A_uNyNjrAwnecqsnJuv4src2Z05hNqbufIOLsjzagIumEQltnUoQ-VxfgGUXLtpivZns1a2FPyGJxF46I96kwkG9But9Fh_qaEcq-nkhl-COe305aqedbZ8q2AbtCZHjMDIv7Ov-hS4Q5Noa8n-IlxqpHSIsqdmcZgwZJi7iREgE27Y-Wcbr8iixnKyZVNL6q2FrEdgOAV0-Ro43gfHQV-6LXBNnCQBsHrRKjCHoIH10IAPv8f3tt1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
بدون دانش برنامه‌نویسی و کاملا رایگان، اپلیکیشن اندروید بساز! (فعلا اپلیکیشن ساده
😁
)
⚡️
لینک‌های استفاده شده توی ویدئو:
1- خود AiStudio گوگل:
https://aistudio.google.com
2- پرامپت ساز ریک:
https://chatgpt.com/g/g-6a319e2a22648191836468df375a3763-prmpt-sz-ndrwyd
⭐️
توی این ویدئو:
1- بهتون نشون میدم که چطوری می‌تونید از یه پرامپت ساده، یه اپلیکیشن ساده با تم دلخواه تحویل بگیرید
📲
2- توی مرورگر، Emulator اندروید بالا میاریم و با اپلیکیشنمون کار می‌کنیم
🏆
3- و در نهایت، اپلیکیشن رو مستقیم روی گوشیمون نصب می‌کنیم!
📱
🤎
اسپانسر ویدئو:
خانه EB، خیریه حمایت از کودکان مبتلا به ای‌بی و بیماران پروانه‌ای:
https://ebhome.ngo
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3934">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ed6B9vhHxf7nCzNP2IWKUG3zwyo5JSM_Nn_PeIMPcHSkXC6lIAaffqe1CeNJkJG5G0iCKRtQatAp9I5aoP8W_mDFB7xN7DByL3QcvedVfa2ZlWoqIFaJdzlKzcfiMP_h2RSadOoyWlgRQu1MAmyl4wV9rotVrP1J8LnqXQJsKqQO7WAtC4fv4Tq89m4tyNz46GPCJgWwj5EFHJ38oXqmJ21SwKyqNzegBUUWfKSyICrz3N4_4s1P0E7KWYOc5l-Xtm-JfBxff0puqbOSsRq-BnY-yGWOOUJyW0Ej_RnisL4G4NWqwGbOBrEs_jzPpgej0bYDsIbX56fKoI2HE4yZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PbBmc16Jw3am9nvgz5BWCupOexGbuRXloRnc3HVBMaH1c7die2jUVPiPRFeUqax9Fss0e-HRlo5RQ7gb-p8_IrjuO2Daa-WLs6P6exK__AP1RkJgiSD3t5VDEdSWbp3IoNNQDrua-IApK-Vehjd3xcW7vnLxpDzBVmHNUbJduu4IeAw1jrI127wN6On8nu-0V-yj_-0oxEB9of8hDwPCQnYUD7g9Du89-bauQ61E5IjLsKqgZpRzdt6joAAEZIV5xGkMrnxe2b9QPKaLSnqpnOku2_axxFp0dISFe8OXq3FhqeZcoiu5IYeAzzhqc_5klqM7-CJTPohENS4nyN1J9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d3vgb5kvkqNTjIlgGCDg1sYe4b-ul7oN-L5ugCA6H9wQ0XKpaNCyrYd8PT8gNcs1CFvIcZY4puAUrbzllsU3Z68CWkKp5Mn2L1RjdjWG4jduegk9WQ8oHXtKTywPpf7GWvhnU9J67XtvwfJ9aWZmEiUvkDE0O5atZG2d81A1MRviugIs0yJ001jF3cPb5xlFwu6o0IZWPqDdo2gDdkERNkIm1Vtn9DisHJYAWLI-LTLw1lfRLhQRROolWxoVbMnh4hlrMdE3qGcEC63TqvSDCA-ddnIuSjGXSJn3f7BJezWxujnCmCs0aGqbvb2pYDjdrF3oBdXdthX2DzP8seeq5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه اپلیکیشن مسخره‌ی اندروید با AI گوگل نوشتم مجانی، توی بیست دقیقه
ویدئوش رو ضبط کردم که به شما هم یاد بدم. اصلا چیز خفنی نیست اما خب بامزست</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/3932" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ورژن 0.0.3 خیلی بهتر شده رفقا. حدودا بعد از 20 الی 30 ثانیه وصل میشه روی همه‌ی اپراتورها و سرعتش هم عالیه
منتها می‌تونید از خود Wizard استفاده کنید و بسازید برای خودتون</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/3926" target="_blank">📅 18:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3922">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I4r4NcuaVXKU4Y6qVVgfw4LNVfRSYC_pcpdrTwmZs_7N5Xm5YiGippaK01xf4mA09YbH4rTTsNFelpqqG1EGi2h36re6UwS3MMeX4m2NzS4SVwKpoTRCDeVPyT9RILn6EUE7JI7w0LVL1VbR8zQpkZJowgLDv4QV3cI5vT1J8ZYwXPcjUC89oBwetTzk7GtihJh49-STiaBosYBlCqYKyBebB88hnyWzNIk1JJuwWa0kunc1_YCfQ94VZf9x4yyXboMEBMOn4WAhKrS6pe_vg3Co-dRag5u3O3ZDW5HZDbwTkAaDefd3x8BaLd29P8iONLlFI9dGboPzcpenYA21Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iKCFp6eYX78R0S-Y5MGSWlbpcJTPZLInNTFkh1iTq2RiaV_fxxd6z33Eoul3ruHZ4gS2dK1EGEpR9orqL9iKbKidE3YeqcrWCzDIMT-MbhIWExiR1IHLmxrn0ml3eQ4Lg8lmoCPLydUr3OM_A5s7GMQ9C90FX2qk7YJ2OhKd6e0a9fKGVCDN-fAXSIHC_FRa8lnMb0afeZNxpf2bLhtH3xttdAo19n_R0ijPen5EjPAdmCDzdbwoqQUb8cXUx_vQvuoD3xVfINP7-ZXAzC43sOQ7s6bmPZduSc0rNRVY3ESfDhHHlpre7W2zyzkJ64xIATv0hyKbGztAcLwcmlgrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kFOb4pWxllivaG9JFY6lOdn6Tz27p6gpyryCZA1oU-ziPMOs2aZ0D8WnwMvzf2rQ8FjnVL7oKutkjRddzHcORnL62DcUBBIhD37dgwA8hLnbKrpXfGWxI2ROU5Jma6J54rxiuAnF-UjqFi5Pp0jBSxZjHusLyZgkN6py5dnLpnkm17HakcQnz9BzfNFbpkVT3Ts_Vy3QOGiVRzkzx4r523vqkbDSFY9IohXKaunn7eEQA_joQc7b5QYWOrZN0H8uprFVFkKXwjt0R5M-HLmt61culAzNiTXA2WeeVm9l16fb9O6avSdEdR0iBR5GtA6FJSuZ0tiiUCVeZc6J4TlQ1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره قابلیت ضبط صفحه نمایش به همراه دوربین سلفی، به اندروید 17 اضافه شد و دیگه نیازی نیست این کارو با نرم‌افزارهای مجزا یا تیک‌تاک و... انجام بدیم. کلی قابلیت باحال هم برای گوشی‌های تاشو اضافه شده؛ از جمله foldable gaming(که توی تصویر دوم می‌بینید) و ارتقای مولتی تسکینگ
اطلاعات کامل تغییرات:
https://blog.google/products-and-platforms/platforms/android/android-17-features/</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bAjeru_sANolfiDcqTBJe_kT4RlnLmgjBlI0lsXms8dnxIM3XeSUSfkHktyeEDZh3D9MXLFyJMYmov5YeT3s3Xzst6wzg3Hc5NO-Pym2Ip4rgkWWHxCe49yZXOYuu3-7fwRdozgThqIn1m-zgOcoc95ZFs1X-Z_o6prsipBn8HcxL1TGg9TvXK-HoaHpLgqTMHpmxjLxx4L1VLt8OikgYeB4boLVf0O915iWZvrwXimj8HXChwg33MT86HMveB67jgtLvlN5WbXhcucmwKy-VS5batuDjnlnsUdaE2hxFhBRruPg1Km47YDfy9InAPpgrp1JD_olSLnn7YUTVxDmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CYE-TcCro_wUb1HrwB3OJB2i6TPuxyv178cuqh1OPFJHacYzzxVOv5ax_ZfRN7ndf4Y6WliTBKTGpz3iXT3F8DQebe1AecoZkc3DH967I79vfXr86nQYSX_yfyRELol5pLt2lYcvSWDnBDFr6_-ONCdcwt9W8UvbfeNYGO4sSYS-EtSA6WdH4ArTOi7ejO4DvaXStvLagyAz_Kc09VfCT6P4n-jCu8mo_U5k9-nOmA8_hdKuI7T8LSuyScNh1g3lFUt64K_m-MLrF3hQW1aRCQMKVDulMGniUR3N1mMn4L5uVe01N7a6MnDp1xSZXI7S1Th5W22EzEM0bQ3t2ey2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/okgyV7bb4g9qvn9e8gulklG0pwGI9wvH0sc10QhJp1IuJvT2vwUGiASDh9mzWSXDIGT13YL1hSAWsP174d0MgqvSO0OO0oO1uOJIRtWPn6M9rZewGXmJrr29dBkSxWtyMBKTvkkLudwHyN3X0gTOpeTZ3UKrK68t3m48vHUl9VQ1inQLMYbpewaF9zbHnSGrvdsjEcGM57VISl6v534GhXazJjnUr41SjhxAIHDgZPUv7Q-KbRfRKoRq9O2_GaS4JqXAVJpjgBnRGXnAaZnLr5ywnnu-mlzu8qPUq3nfujL25jXJMB5aLQMatVG4gmKDnzxcmuMEzjpmcxG1EiKlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qO8xOyKOmSQwS8QArS_PO0g-PzEi7gAb1d6PY6dgy5Vi9V5Pd34UBWbp8gT85dUdHiSv8lNVu4Sa3Kx6LMReL0yrmAPXWCB2r6fzigqdHyUCdNBOI--TbcajB527Lowbc17pkVg8obJTAS3__0-1A3KnOuv2MHx2TFUPgnXiFaY4jOiF-dvR9l8-eqQDckrvTF3CKdfgRsYPU-g5v-mf5QC08n2yCciaLvsKn5hKN0EDp-CUYm6sSV-Dwun5U0fHv8MyzIOfnqmVi-BH-TqgIBOl3g6BkAIrOn367GXUg9UxosecYldWORsXC_EadppRhVEBVCYkm9Kvseq85qDbMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3910">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3910" target="_blank">📅 00:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا من داخل این پست میخوام توضیح بدم این بکاپ ها و این ip به چه درد میخوره؟
ببینید قبلا یعنی تا چند روز پیش شما تو ایرانسل اسکن میزدید واسه ip اینا ۱۰۰ تا میداد برای مثال ولی الان هر  چی میزنید ۵ تا به زور بهتون میده و ip اصلی که
188.114.97.6
میشد که ملت روش وصل بودن رو بستن
❗️
یعنی ip ها کلا رفت تو دیوار کاملا خاکستری شد
اینجا (patterniha) بهش اشاره کرد:
https://t.me/patt_channel_x/68
بعد حالا همه ip ها واسه همه جواب نمیده باید ببرید پشت gpt با یه سری ip محدود برای sni spoof استفاده کنید.
جدا از اون میتونید تست کنید این لیست ip ها رو که واسه شما وایت باشن و مستقیم بتونید داخل پنل های bpb و نهان و... استفاده کنید
🫰
ip:
103.160.204.34
185.193.30.94
45.8.211.57
199.181.197.1
159.112.235.52
170.114.45.239
104.17.21.111
104.24.200.94
188.114.97.6
آموزش ساخت پنل bpb
آموزش sni spoof
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K6sNOtRIXrJnvijaY8vB2ziKg6iBWF0aCgn254QrwplqCX_5-ptin1-qNpljwQAdZboyNnNDO5Z6VpIXoDsFvfFGeHATtHZEtoshUS9dRBVkQByYt2Cuu-eDrOWFJNQZNAuqDFc9aXA7qvGr6FLgtMr3StqyprCzkIFFAsK8ANpJl0diluWGJkxWcK--wFN3tMx__TsFoV-kRehX5fXq2SbS3jfFmFS23IjjI22OIjKzC8P-lj7WQEsy-EyLLFtMncfvw21h5VR7kAQTyQgoM_Cd4hc3yM4aI_g830Ee8zPCcO70dmp-3E-R8UYNZ-4EbxIh-TuhX2J3itT4QO4fAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3905">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی نهان:
https://github.com/itsyebekhe/nahan
لینک اسکنر:
https://github.com/MatinSenPai/SenPaiScanner
لینک ربات ProxyIP یـ‌بـ‌خـ:
t.me/nahanproxyipbot
لینک ویدئوی اندروید:
https://youtu.be/2otJfXgNWCM
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل نهان
2- اتصال به ربات تلگرام و api کلودفلر
3- ساخت کاربر و مدیریتشون
4- رفع مشکل وارد نشدن ساب در  V2rayNG و ارور 1031 و 1101
5- اسکن آیپی تمیز با اسکنر SenPaiScanner
6- پیدا کردن و تنظیم ProxyIP بر اساس کشور یا بر اساس سرعت اتصال(توی ویدئو نشون دادم چقدر سرعتم بالا رفت برای دانلود)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از
YeBeKHe
عزیز
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(نسخه باکیفیت‌تر)
💰
دونیت</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3903">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی نسخه اولیه WhiteDNS BPB
نسخه اولیه اپلیکیشن WhiteDNS BPB منتشر شد.
این برنامه برای کسانی ساخته شده که می‌خواهند پنل BPB خودشان را راحت‌تر روی Cloudflare راه‌اندازی و مدیریت کنند، بدون اینکه لازم باشد همه مراحل را دستی و پیچیده انجام بدهند.
با این اپ می‌توانید:
✅
به حساب Cloudflare خود وصل شوید
✅
پنل BPB جدید بسازید
✅
پنل‌های ساخته‌شده را داخل خود اپ ببینید و مدیریت کنید
✅
پنل BPB را با مرورگر داخلی اپ باز کنید
✅
لینک‌های سابسکریپشن مختلف پنل را ببینید
✅
سابسکریپشن‌ها را کپی یا مستقیم وارد بخش VPN کنید
✅
کانفیگ‌ها را تست کنید
✅
از داخل اپ به VPN وصل شوید
✅
لاگ‌ها و وضعیت اتصال را بررسی کنید
در این نسخه تلاش شده همه چیز ساده و مرحله‌به‌مرحله باشد؛ از اتصال Cloudflare گرفته تا ساخت پنل، گرفتن سابسکریپشن و اتصال VPN.
اپلیکیشن هنوز در نسخه اولیه است، پس ممکن است در بعضی دستگاه‌ها یا شرایط خاص نیاز به بهبود داشته باشد. اگر مشکلی دیدید یا پیشنهادی داشتید، خوشحال می‌شویم گزارش کنید تا نسخه‌های بعدی بهتر و کامل‌تر شوند.
WhiteDNS BPB v1.0.0
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3897">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hHM8SCxTmEMEz4PH_g4_wPjubLRlOPMoHin5n39jF8hRlmP6B1SQE3LCerZEo1f9O88hzs0oddY34eaZgx_2hq-izqs0fZH6Fi2L8i38UMOulb8uHz1-_A81GXymrE3PL4fXbaoJNDng4Y2qLXnahVPI5O7yPVvf87FpBlo0UUFz5xtFTpo7mIRWoUKn4ZBIFUwckm5L0Pu2UloqM9k2Q4L624zrIiq2YYig0BeDE5tR9G5ugZJeArZgJLxtxcpG45dQRtxilx5CzfYMOa0haAW1c8RQ9BFXfW6IkJhsvwRWIVSajyGirGqhEfOApKeSt0dOLXqXRgwvQBCoMIf26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BfX16DFImBDC7O203ZyFXu5Xy9m2FwsfGFTyft34tSRTGpMLG3KWX6qh534FamMFkgstM1g8aRf5VzWravmnlKv-047T2UixHuYlaMWFwfP27NU4ieALWcA7s0g1t_oFbkn-DdAI8FGf062C5IJLAirTr9_96WVexn7RLVauGqR_xO0OBJ5iHPDn3Jq6Os1oMJZMu8ZWjD0FNmhzG5YVG7BPCQJ5HghL_FfY4CUVv6z5FTsy3J7yN4NTpaOGCvx7NigVvAqczIzKR_lBiXPatRS6fKvpq2QYs8duQx35s4gXYaQl5RdpEnsKBouQhqd20I43id6m9f-PBJKrTWuE5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DaOIacawo6c3WSde6CKd9HuitsNAV9WJKLjbeZaTvR6ddSTr0XdmLLSJKolG12BL59G1ridTH8aumr2uHc1gViiAYPGvnOf-rXSw0LJCXQ6KIRAhBUbyGlYDfKhdQzxLL9uLofyeMf0x0NkOuIGWDVFramaSsYybvmcYOtlqZ_tgT5vWgiht12glqGQYWTkOBO6vM84NPBnAAbOJK1BuAGjHAJWb_uwlElYrreqNfFNz_pBEuDNq15s5uIeBBiHaO8X6WuCAMC89dNhO2Lm2iAh3eW_9rHdIaYOExyC39O1HlFyY4GtNyJCXLri-SkaMg0XgE-lM8qaJhd_ye1jKDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد میگن چرا کامنت‌ها رو جواب نمیدی
چون 90 درصدشون جواب توی ویدئو هست، اما ویدئو رو کامل ندیدن
✉️
مثلا اینا کامنت‌های ویدئو BPB هست</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OdfI6nmMuMaH1Pox2xFP40UxUlW0Ag54uuZ3V9RIdUf8jD751HyVAtCuYzPo0pgtHn-7hydKaj5bs-opjUdtVxZacZK4sui5m43VEUHFE8MOWTTLeyzKCwYN2bSwx9P1HeaFfUsrgGu2-na5GnrL78eGYpxQ1AdJ-nBCC0o2B3jn9JeYlfhfCHBjASR9Lk6sDPqDd77uhwWabh_Msuy8KqaNwr1GSqrus3_Hv1d0acSm2bOi5or0iwPq8DVMEPFp0iL0kThjqzwDF2B_6rRgnL8nUEQo4tzg34PayakHPvRVUzuTG1rntkddivdqE9KiiHTTZh8zwjTazsaPKgyyRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I_FnlApSw92M4dqpdA5uNqqwupqWuI7e44F13FjI-kiYQ0kmVWGb90FKiN0QFPiFMZ1_KvAm47B0rgGs90IQ3a-0plfg-ooEaHEk9WElwGgOMav_pNTgCYNaLcszvu1i0m6UNiZ2IBf1A_KkC_ErdrJSI1-ehjulASao3OrFw2sfIsVnNI-O4emeDq2lpJPG-bfAWTECMBH5HI0NpkLg5gIPnH3RBBzdFVE8_P1WrKyE15US7pMg_exDHJbh7ZUzJjRpCGki4zWE6ErfDuWfy2-LHJYjJbCNQsZjOvsQVf4NWT4VoPbTghE2x216qMwMaD5pyTwYzFc4fPV6M7u_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HKpz6zBpljZvB74oD8xPhD-8nkJ0vqFrR0RZyKIKk_QPfWhO6PZIJwx417FMxSCiKb6x-b50GNs__sVRqXCOjhJA1edMV5Nm9i8gbiu552pnW6vjstAAHhVNmyEvYdZQlImrELWT6IIQDtVqsmPpcuHXUKjLC--SBlM0O5VoK3hWj842TvcWaIB1EAbPJBhUjNf9Z5yq37uB3emO1DxT_0Egmqoyp8N6TCuGf5pJsdbVZH3xP825U78FbqTIOCgWRNm_Q1TH4hwg0MTDfyO8cnvZnnq4IzXmioK1pZC1KZEJ2O6_l2RT9mtt4ApFxLsDb6DSrbBM2Bw5amOzV7Zocg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyWvk5IxTjW7lhY9d4eNB8yMQ5DEiZ93jAoFW_V1NBPDuX8N-UypWSG5BKiUwJqmHc_clEZs9_HNwjiEotrpxgbtRD0Dn0yTC6BGMEJnJfwb_YVrjrWade1QlF06uHP90gmTjlJkrDvMpNNF4ybctpUsPAIvme_oToFYiFsKKpQEEbVQqd7s56HegDQaS7nrW2P4qhR5xOro0E7Z3mh5_4m83jsIPEjapPOIgVTKUdVbrMICFncCCoy4trks9nYXwcJnLYBeAmBImC4fC50itMtX21P-0-rantn-XA5Nkr7dfOBRCNdKOG-s5D3YMqe0bwByTlamJsKZNQLnPwzAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IRT43n-p59n65FFYQRh8Yr7QRS1BXNAugTcvt_3LcFOtXrxruViL_0scJ5HhGGj9tMfV6INmGpoY1d51l3yUKfzaWaq8T5XZzMXusUhtblsDM7Lz757Uv8Ha6-eoXxrjSKnoLmsR82uChCwJG_Jeoj4jL0viO1XnWnDJChb93B9NS9HDjORtKX2xKwtqvHb--77x9retmxbhJH3t7IL9XsXhhNsQ5mDOQqwkEHbEcFvg9gKdvKIFW8jO_0ZIC4tN-M68C2AwxOmzzxVfiEXKZ04srNUD9EzAoXA29jYzIiPJn9PDqGC6s6f9QnOIGWx1W1pb5-MrBgTzJZ42X0XjBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LkinNmIkLJJS-svFzsUMiN464YX0GWLCwyB3hd6BNDqoj9p8O8Zj8oV-jTKpnGjaDIqJz6YqgLZDPjwZ-jKtkSO6NuIePj4gVgy0-JiKjgNlxFanAqQnkktJz_ogHv1i17TH7PYXL0SyLvMup-91CvqDVHNsg_XovO7nEY0MeF-JOYu_HCVqCMyxg1SEKwLkcH_3g5g0cIbr0WuYwLlfWiDB-wjpLsHlmG4w5L4oCIE7PUIvScIjZin0v2F9RsmqZzsOBIAW5-EQYclj6nn6RXJtNgvdnxnFzs-tTxOQolREd5QtKOCwQtvSZSyxBWYqyNpx0FAlGt9-hDLWJsa4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FoQGgoErdN0Le9pNKDsMYmgEWBu5QagCt_5Ba5o1nL-5uz6zoF0IqaJTNRqgrZ3qT64QiWpxRUWkAi4Qbft6JxrIySfXGvA4SKENa-FTTMbkjHHoVxLxhPfuOrunKQgVK-WqhcIA0aGl7SA9l0Eo67f2QoZrYwVJDRB2mawZdY5q4oalRtC7naUKVX80QXVPCTiEOagULEecy5BsVldDGJRA6vEmo0M1p_iS6D2LAZ6uvhW6oDaigftufkJhnjymmyVikxegolKRatEBQlcsG5zs8puI-v9WrLmDkc_I7uTTe0C7dopS6XzT74kUuryiNpFeuF11VcSYRAIFY7emRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R5MPkypAkocTYgQXvLZN03qXG54hL7J1w7gc4aPaRaIMn4LGpv26YeCtOR_dKlnutFD6BhJ46j9dQh18tEzQaIG3zIfv73bnjwk-whcZjjlBgeDVEkZ3SajM40jvQmYnJlQdsKmBSRDagECoykcbkGTedPFK77JNbdn8BuZaaYZ76jcvnTwRlsFhEsiMpFeRNawAbKv6QhMKgyswJVsG27vUSMrbtMZ2Afwf9wciTOhjjDowPKIEov39JX7sRYk9eo-_opLeFkgc-nGwqINO0VittFK726wGBGUEX8_vsxJdWe-q_n-qa7PRxcz5zR486WqNQjPtbdd1twmJy5Ft4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZX_m1dS7BlNxHjlHecxl3mMJZtcEoVzdUwdKAm_RAjn8-q5_G0Q3QGMIxcfKZB-laI-tL3MbgJk3hWa8ie3A3Y3oKdmW03VTzD8mBx62e15STHjes9DrQSXWB_HEBVWXDqznkjm5GmhEG0WVGDE89u2x2jUDkEz_tz96QeK9aSB18E_zd40OEDi8L5hlWbJyVLSWzpBD14sox708H3hULpHRKMqI6J4PcOBm9g3XkDLUGn54E-gkol0XbegguDuO6LKtHq3GS1z4NpqRsUEJB1VRru-YFd-sv9gRRaQgK2eII76iSkeJ8eiDChGQwv86bluSJUBgJvfchJi1bC9XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پروژه‌ی جالب دیدم به اسم SurfSense، که بهش می‌گن جایگزین اوپن سورس NotebookLM
📞
اگه از NotebookLM میاید، باید بگم که SurfSense همون کارو می‌کنه؛ صرفا با کنترل کامل دست خودتون. خلاصه بخوام بگم، یه agent تحقیقاتی اوپن‌سورس و با تمرکز روی حریم خصوصیه که شبیه به کار NotebookLM رو انجام میده.
👍
مزایا نسبت به NotebookLM:
• اتصال به ۲۵+ منبع: گوگل درایو، Notion، Slack، YouTube، GitHub و افزونه‌ی مرورگر برای ذخیره‌ی هر صفحه‌ای (حتی پشت لاگین)
• آزادی انتخاب مدل: ۱۰۰+ مدل از طریق LiteLLM، یا اجرای کاملاً لوکال با Ollama و vLLM
• بدون محدودیت داده: هیچ سقفی روی تعداد منبع و نوت‌بوک نیست، و دیتا روی سرور(یا سیستم) خودت می‌مونه
• جستجوی بهتر: RAG دومرحله‌ای در برابر سرچ تک‌مرحله‌ای NotebookLM
• قابلیت‌های تیمی جالب: به شما رول‌های Owner/Admin/Editor/Viewer میده + چت و کامنت و...
• تولید پادکستا بدون محدودیته
😭
معایب:
• نصبش هلو برو توی گلو نیست واقعا. رو اعصابه — باید با dependency، API key و فایل‌های Env کلنجار برید
• هنوز کاملاً production-ready نیست و در حال توسعه‌ی فعاله
• باید خودت میزبانی و نگهداری کنی؛ طبیعتا که راحتی NotebookLM رو نداره
#️⃣
جمع‌بندی:
صادقانه بگم، NotebookLM همچنان ساده‌تر و آماده‌تره ولی کاملاً بسته‌ست. SurfSense سخت‌تر راه میفته ولی دیتا و انتخاب مدل کاملاً دست خودته. اگه با self-hosting و سرور هم بخواید پیش برید، به درد بخورترینه.
🔗
ریپوی اصلی:
github.com/MODSetter/SurfSense
آدرس خود وبسایتش برای دانلود مستقیم نرم‌افزار:
https://www.surfsense.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MXmTdwNz34vRiESxkBipDvgDyWKUGKAOJ6RZBd_Hy2cgDBYSTDxql1LOF7A9xOElwhQHRFzAGCKguJLhyXabIWwNy0w3PMhAmWfPv1L_yxnHyx58KAMHp-DVbOx5E0hm07LYBk6eBsbbAxW5jxnH0CNFBuSL6tdK6KQ6E6Nl_83wmTi_-kVlbOOx320_vn737kmZcRG0fthP2ldNvGSNtoWfFnDsjwXCL74EwlgHgTiEjK2J9DdsD0bzrLjWnMHN5qsSbZYPrtNhmqlBvltxrr2Y9jpIYJlLdcqkkQNQuvYNfhHvY35i22_m38k0-qKJIiI5QLlvivKcaCGMmXJJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZRc6vGGOAIMD6mtEZ5i2E88QTOm_Whn_3MAFsdwk4LLwsbp12qfaJ5dB53kf39BV-4WD8apFr56KlTRoBlsSJlrQGtU89uM_ADpJfyrPKCSCgkZbUnuDhwtk8dQp-1xOz6jWh4M6gXKBlOuAktbBs4NIWhO3DAhOZ-MpYH4AKZ3FZzjZOKFlDFCqXuHHk59U2yB7kLJhXKtij0cOyMK7XJ5Gw2NcsAb76b3Po_-IWd3eAlhBiPh80wcTDvNEMGbrKxsCRMC_TQJIoF_Vnchw1ybRgDUxRMBUeSERxoPDFdjyc9ygGfj2n_2Ctu5_DAxW4eZ9ZywBhw8WrCNW_Monw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3876">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید اپ WhiteDNS VPN آماده شده.
در این نسخه
• سرعت اتصال بهتر شده
• مشکل داغ شدن گوشی رفع شده
• اپ همانقدر ساده مانده و فقط شما باید دکمه اتصال رو بزنید
متاسفانه باید نسخه قدیم رو پاک کنید و این ورژن رو از اول نصب کنید. این مشکل از ورژن بعدی نخواهد بود.
ممنون
🔥
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/3876" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3875">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iml-9DIrVzKgZC7w3XhSfG1TQIUEWITgUdekhnmf-U8JIfUc0SEXU6hSSxusAEubkJPcw382zeOPlnNmcfgX3rD8t7KQXx3GhJhjOhs5l2qSgR8cMMQfHnOqUFkBi_YOAkJGYnAIVvvCuEnJtcdm0nIZII4Fw_e6irPDde_Y1yUxxRdNAAZXUAWgYFOCc_cmbRrXrzATp2475LH_-cwj_e2J0GTEjYu2cmM2l60FZl1VOTPNudtGSVnBQqY5RTie64yisxW9mWr16q1SnL24fDo5fq8thRCmcjOhNDk5ad9CKoes7z8dRul8a_BXZoHxhzpw5iQhcns0gg4TDAS_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو نمی‌کردم یه روزی قالب وردپرس رو هم بگن بیاید اقساطی بخرید</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QOXax6wTkGoNPSbOORQ1jERYMBroE-Tho9Q1hw_vrY2fZcBjuj6XloIjLMLD9uKa5B8HZzv5Ee8cJHj56qrYSJjo3P4B3mEh7hbYgDOZrWCAp-mbm99VHeoknntaaXM8vV16bmKbeXmYfUEAzuVnHpbP_TL8x1u4JT-PsQZCLKtbg0iNpzaoC3Z-C-OGpv9E0Npdz9IZHW05lalatQw8ROzby5GanBfP1CWHiMDA0NIL4yVend5wtSGkFAlSlxYuhlpGSQZ1Zf_Cejsu0Xg81dCZLLSwZ_vEXVJClzW9utx-a3kS5qCtBvG82Zjy-s1TwYhCvl8QHkDCg3cb5yuhwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hAoIXYa8D1KATRUQXb2mWOoSI2kYQBSFmCRGDUt8c4nXqh2difAIFvZne_GSRKeWFFFyziXwT_WHT7XYjxsbXjkcwdl2lIUtUZU219c_FlQiARjX_Ob26986dTeQq7Ym9OpON6SfpHymzXGQC1nwc7uDFnhhz2xuJv0-uY0Nueuaz8wGPkv9_zcCLaR_NzhR-bOYporoXcUFvGnMox1xU_5AJl_QXgtsga-AzUpF-YYdiimySLYLtcF3pTp_i9Ul45Gt_1soDLFDqy3tRc5yTAK5fGtPS7bZwP2W29TK3Ufddosn6ldzHAbT8wNM2KRYujusz1fEWHPc699mjGtF2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qbLdBvFrtabvh2MZHhFSJizgkNYlGPbEkSKX0kJQ-1NADzGaHIrN4hoTHfSiUqJlohV_-kEsnH0rUqUxlqZspxKHQzMiif2bVCdQG2zRe4y6j0GivCwSf1MoYg_gdS6m_ygvugwpQ7V_Zm_qeYGLK64kVtPhuNcq47wftR4R6FEALowTox-mmdSejhJnLl7aXHXwKDN-qBLhDdgwgD-ZVLiCiQMhBFxzwr4Eu6gDcIgWpMNQ_v7clU2AVrpNEdg2tHNFbXDUVZNgoYUefBRkN9zJgR26pYkuJFGkGed5CoGiYq9NT66h7tZdAQpjyfuQ9HJh5KUeHqcm33C-YyUfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/3871" target="_blank">📅 10:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3870">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3869">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3869" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3868">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3868" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3867">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
بدافزارهایی که با ترساندن هوش مصنوعی پنهان می‌مانند!
تصور کنید یک سارق بعد از دزدی، یادداشتی آنقدر وحشتناک جلوی در خانه بگذارد که مامور پلیس بعد از خواندنش، با خود بگوید «بیخیال…» و اصلاً بازرسی را ادامه ندهد! پژوهشگران متوجه شده‌اند در موج تازه‌ای از حملات نرم‌افزاری، هکرها از ترفندی مشابه برای فریب دادن هوش مصنوعی استفاده می‌کنند؛ آن‌ها بدافزارهایی می‌سازند که بخشی از متن‌شان طوری نوشته شده که هوش مصنوعی از بررسی هرچه بیشتر صرف نظر می‌کند!
ابزارهای هوش مصنوعی کنونی، ترمزهایی از پیش تعریف‌شده دارند. برای مثال اگر از آن‌ها راجع به نحوه‌ی ساخت «بدافزار»، «تسلیحات شیمیایی» یا «تسلیحات اتمی» سوال کنید، فوراً ترمزشان کشیده می‌شود و از پاسخ دادن طفره می‌روند. حالا هکرها متوجه شده‌اند که با افزودن این نوع از متون ممنوعه به بدافزارها یا نرم‌افزارهای معتبری که آلوده شده‌اند، می‌توان فرایند بررسی امنیتی کدها از سوی هوش مصنوعی را هم مختل کرد.
به زبان ساده، مهاجم سعی دارد کاری کند که ابزار امنیتی وقتی به بدافزار می‌رسد، به‌جای بررسی دقیق کدها با خود بگوید: «من اصلاً اجازه ندارم این را تحلیل کنم» و از آن رد شود.
﻿
این نوع حمله نشانه‌ای است از ورود به مرحله تازه‌ای در امنیت سایبری؛ مهاجمان دیگر فقط انسان‌ها را فریب نمی‌دهند، بلکه رفتار هوش مصنوعی هم هدف قرار می‌گیرد و ترفندها در گذر زمان فقط پیچیده‌تر و خلاقانه‌تر خواهند شد.
✍️
NooshDaroo</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7D7ug0MAjoaLA8e0YmlXOeWNRx5ZdYGXIXqYRc1yS-uFOvJxGomwLE74Kc12ImmfitHxB0QO1DxLg3-pCNfCRySD6419Hy7dvRk96NPNrsPXqSPH1ET9TseXnffoJ2fntCBFhmnjMtBsII2LzwfojiB_IaA1Sm6XuoN8w_anxDcN1QjPiE7X9RCGGj2VWkbRhUGqoA7hLgB6hS97q941q7Ce8vxlwMYz0xyG0qnii6AwydBpBQ7s5p16nJkSm6iay6rhTRQHui256S3blh-TA0unaI2eFrq1XWNoTjO-XjlxtMg40Bnj3zgIH6E7hkcXTjhSAd40VILjNUBlOJkfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید دفید قراره قابلیت چت با رمزنگاری e2e داشته باشه؛
باهاش میشه ارتباط امن با خارج و داخل ایران داشت.
کل این قابلیت با ریزالور ها کار‌ میکنه تا توی فیلترینگ و قطعی شدید هم وصل بمونه.
طبق تست های من یک‌ سرور متوسط با ۸ گیگ رم و ۴ کور سی‌پی‌یو میتونه تا ۵ هزار کاربر انلاین رو هندل کنه!
اینجوری کار میکنه که هر کاربر یک اکانت رندم واسش ساخته میشه که توی سرور های مختلف ادرس اکانتش ثابت هست؛
ادرس اکانت شامل ۲۰ حرف انگلیسیه که هرکی این رو داشه باشه میتونه بهتون پیام بده.
(سیستم اکانتینگش تقریبا شکل شبکه اتریوم هست، یعنی‌یک seed دارید که با اون یک اکانت ساخته میشه)
کلاینت هر ۱۵ ثانیه به سرور هایی که بهش وصل هست درخواست میده و پیام های جدید رو میگیره و تقریبا برای ارسال یک پیام چند کلمه ای باید حدود ۴‌ کوئری دی ان اس کوچیک‌به سرور بفرسته!
واسه اینکه به سرور ها فشار نیاد محدودیت های سختگیرانه گذاشتم، ولی همه این محدودیت ها توی سرور قابل تنظیم هست و اگر سرور شخصی راه بندازید میتونید محدودیت هارو کمتر کنید.
https://x.com/i/status/2065531715041239193</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OqiCdb983JNZdT8Fu4qh2pWG5ryO4lEITAL6-_SvpCTyuf2SA9LHTq96h8lMXf0xY1a0szWVLW49xav4m8jVFHTClcyDO7YM6-KSZmt5y8bSabcUWZVD7QTOZ6pzWCExMnl3G41cvgOP5PDqzDwAbQ9KnrAuqM3HUebxMD7Ic81WzWx4SdjKVQpf7zW6QuzKCcflXeiSXFjLK4KZ-pBYEa84Ch0Ab0iCkQjtibXw-lTeUIU96x3oReXBZM7vNEoYZqfnuw9Nmj5usUl8YvmPa7UQhAFztApXuToCFcPRE4HPJW86pGaSbJaH854CIop6U-0PGH2rGcu8vjkwF65w4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UbrezOGkppHCMRVZpNtlVEqJrVolIHY5bCl1Lt2QMxvan0KLTeiZwsgkfzT3OETjKg3YmjlvATuAas4CBQkmaAzV6NyuyZub83f1L39qSSC1KjMI1VDah6BRNKNS7CzKisVklbuplY6oZJWfTG5Ph5gTv8zXIl5q7Db52kNC1mgNB3i74DTpF8pbHBS02cwpT2VT_3HWYk7sh1M27NdI7oCJBMas0w3vqhjtyXTdeqbVHFfRn85Xt4PBw-sPHaiZA8FmAK7xvk_82MSd44jnU_6QhayBmaHIj8YmrUcIH6NAzGjNPoCMxPokuUu-f9aqg4SgMgCRcD1wSwSWtYE3iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KqPegN7AjWMe1WNyIr38abx9j8__pDEAAX5VQjnWSBV23vYmhsJaJZObJQRGtrziOsJXOtmp9QJxesFTieQZCUtH-ThfM1rxa4-EzQJdV10_KqGqjx6A-ttpiKQH0wBcfnBz-MtDSBgoqTDDv_RBo2Z6XmywlOwDn6C75v6LXlDUxxxPfZ0CmXGxez97Yoh2P3GhuknTQvAXX1cdefLPqHc6zHVLq9aTn6UggqMWk9rAM3PpXyJaArvzbHP1IIdRBNXimqjHDgm9TTO3BgcdhfitHaSXqE-1Mdxef60BI64-CSJBkx3nJI3fE9Yyks3pLh8haxhT2fe5iQz6_jRjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A3RCiR0F9ZbcsWvICS763haZfAblh6pZrokYEw4n4ufjm5E2vsE-TC2LAxiDJP2h8uVEuk5Z5Fyf7MtLAWz3YYz6PcQFIZi7KvYbA5VAbQw6noY4HfWXEXpqXJ3HOelJ3yvy5GZAsz3U8P7U-ZYUHVFS9efVnc3pmhdlyjPIwlQsXJeLEL-iTlFfsTCv3Q8OSkrvRpZjTCMzE1pXjhO4xaTmW1HFDOVBAp_dxfoMMEiD8n56eizIMhvSF1iiSDkswvMKtx-XDIrAb8eKJRgZiPmQFl-s0008sZ8FpKT7XkoWv893uYYedx84_mqjcU2tu2ht8p0N3gIJWkeiMDLIaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن 0.7.1 از SenPaiScanner منتشر شد
✉️
😏
پروتکل‌های جدید
: پشتیبانی از
Shadowsocks
و
VMess
اضافه شد — هر دو از فاز ۱ اسکن تا فاز ۲ xray کاملا کار می‌کنن.
🧮
خروجی چندفرمتی
: با زدن
e
بعد از فاز ۲ می‌تونید نتایج رو به سه فرمت صادر کنید:
1- لیست Subscription
2- Sing-Box JSON
3- Clash YAML
🔥
تنظیمات سرعت
: فیلتر حداقل سرعت، تست سرعت آپلود، آدرس سرعت‌سنج دلخواه، و سایز sample قابل تنظیم.
🤖
ذخیره تنظیمات
: تنظیمات اسکن ذخیره می‌شن و گزینه «retry last scan» هم اضافه شد.
📚
پشتیبانی از CIDR
: حالا می‌تونید توی
ips.txt
، مستقیم رنج‌های
/13
و... بنویسید.
📱
اولین نسخه پیش‌نمایش
اپ اندروید
با Kotlin و Jetpack Compose اضافه شد. معماری MVVM، تم‌بندی کامل، و ساخت خودکار APK از طریق CI/CD(هرچند CI/CD باید روش کار بشه هنوز).
لینک دانلود آخرین نسخه:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.7.1</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هم پشتیبانی از Trojan و Vmess و Shadowsocks اضافه شده
هم تشخیص ISP
هم تست آپلود و شخصی‌سازی تست دانلود
هم WebSocket(که بهتره On بذارید)
هم هسته رو به کلی بازنویسی کردم
و این به کوشش دوستان عزیز برنامه‌نویس دیگه هم بودش که اسمشون توی Release note میاد و contributer پروژه هستن. من شاید 20 درصد از این 10 هزار خط کد که اضافه شد توی این ورژن رو نوشته بودم</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3853" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3851">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s6Qhh31dne4P7OCpTu-xh09P9rk6eR9Z7uBRBoHGl7mglFumFjwU-limIGFEDZoJBgmgw0IKAsZLLa_1yKC_bt7ZFgIlNWb3YfKFQSLmqDtewAFsSvTd26hF8eHOxp_eHw32mbHVTnXo2PQhNHFxZGnB5gme_BaXfBuhHFpio_8LvNe8psePlNZofrt0ZNqLw_RBrsPD-zk4SDXKPvRDeXF8naqnNnlDhIHsQVdwQxcBqyvSSh8BoQs0jbTKAEsGRm9oVB1eZhPHx-ZGiaGD5J1TbjuXwmRBukVJdkxw3iMjGBtIW2isKxFCZl9hQuNOdttSNoheegJN2qFvMeKCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cdFEju1zgisPD0z-4e9Ha8Pe80Jbn8F1wVTTMFDvAvUoJ48a8ulkOPLfMm-aWl85YB3a74ij2qh9t0qCExShiRUMLdC0gH8xGxhj__N6SCy8001PXSiYKux9ho8Q3q__7lK64mh4xCdRGcNH-un59QLpTq380k755sgskuL8OUDjM7DYf_kbTqoLiIeMqHFfODc6hmZBQaHfc20N7KBz3FHoqaBTVsiQX7f9FnqGuZCjtLCyNJBG79YISEn4lHsaSqlVwRmcVf9FgSDBIidHKPcrmk-CsvXzDoLAFfmKNpa418swSGIUf3fGJ8_si-oD79bWN-kyubjRlZUL7G-Idg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E6kXvNJEK9xygXVjYQ5VQvKo5i6PiO-LWd1Jna9sNzx1eNjtBrRTx3BF_Rc45m_WsUH4RCBY_RtGVz-eoVKrCmMGvvw6hWr0n_MYFRJDIUlmyabTbOgH_-N6mZAxXSy-OmG37z_62VmhN0ZUGcwUTIbxwB37kB93nawxL3HZOVoB3eObPrfVNGhxE0nPCde_chU9OMyY0SQs1gcaHUu5cMMNL8gBkdb4uokHUqwb2Bp8uVwL79CYLc4Ex8ziNZa0ew0vaAx2RBuV4vZrIwHEkU9GtWhP7Wh5D3Eom2BQvbB-UAKl43U_OWeGgfJt1SrK8msTpKPg7YCLPxTCmte-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3850" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3849" target="_blank">📅 11:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3848">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mPf5QI651jm05qvmk_c9ftRspsiW4EgueoYTqj4QcLb1U-EeUnmiOx-KWfz-ijQTDTSYi5ozd1rJar5Rm31KmbDGt4ZNWQNddHeFhxF8oDrSE5TOkpuzXiOA2SvllEzZIEMwLUOzLYx0uNsx7nH2T1iYD7P9i38iALF95Jv7opXbvcGQbx_J9WsX5T3y2SN1c9VKhXZMyoMhlKgyF3A47PX-QcVIdGeRaqR06zVyDVl1oXvc9BWdRvtMdiaP2BmeEJ6pS8W6WOQVXywMCBeEguC3f-KdtZJIyllsPHZrR2ZPzWjwVoRM9g_Lef6jhM6TMc_R0ZrP-YaroTz66bqvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان خوب، لطف کرد و هسته‌ی اندروید و تمام چیزی که برای ورژن اندروید نیاز داریم اد کرده، صرفا منتظرم که خود اسکنر عملکردش به بهترین سطح برسه، اون موقع نسخه‌ی اندروید هم بیلد میگیرم</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/3848" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نکته‌ی خنده‌دار اینجاست که دولت آمریکا دستور داده دسترسی به این مدل‌ها برای هر فرد غیرآمریکایی (foreign national) — حتی داخل آمریکا و حتی کارکنان غیرآمریکایی آنتروپیک — مسدود بشه!!  آنتروپیک اعلام کرده که چک کردن ملیت کاربران به صورت عملی ممکن نیست، بنابراین…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/3847" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/3846" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/3845" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3838">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">32 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خب، دوستای من هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3838" target="_blank">📅 11:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3837">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خب، دوستای من
هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W6kp-6G34N9LNYHCx44DFRPyTR5YBRAndBFANbbIO2ZDUb7I9SHShvpR4UopN-iuQDGKpVq3oXnsH5kUEv7-QATsYtGdSrX-fYfWfeoFz7PWrLUn0aP9jzf3rE7mlVtxwAizUg9LGLSTiU2T6PmCSPWUr4q1I6L3x30w5d5mdv3N9eZpVbO4b9Wvt5bmbAEVRKa28_f1mH2xlegqYeMjKS7vCd0sXlPxo2rn67fC7ueaotLNKlkTc_kQelSCU1wjK2u1OimnjUfjMwSkQck1SDK3bPkjLtOqfuX5thlN2XkRdKMH-vDE1dFD-rQFdocYnuWJHQb8ireTf6HOFtbBxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SmeP4bfoJ4jwQY5EjvEUr2Q50KcXDKfx4bspzknEFG1HA-Qgbo2lz8z5lH78uDLVmEVBhMFER_EiLsTG9sSXnE8cEcEtE9Kbl0HpQVilvFXvk6eUudEhurj4QL08vWwJEsz_ta81QZ5gEzarEyVVtYYE4l4tF9Yj0MBPZuQ5wlbEcaZVf5yoQNwHxDGH2IIG8bPcW_ACq6A6zUEZZ47-Kx2BwLajJuoWagPHoT5ljxIQ9ijs-495Jr6eWRBNKXuAylN0GgbxTKQ7U5XvDdjtip3clyRoykwvnHBYlXgIQ-BI-LiEk2tPenoxftblO-FqaJ5dseB_HOv6rg0WQDtRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/3835" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3834" target="_blank">📅 09:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3833">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nWoEYSZHTVD6Vl6LnsMSxmoRIXPR0Vk_5qEASe2mnbziMJ1hsm3oZuevO6Biv2_Y3Zi_57v4rBO4cMRQP_fjyv_oFom48WQIMSHmViC1oIdzGebOO6bBEF9jPQkd1TxAcaz4sjGMfYfLrb-EzFrokczOZpruTxIKeE9te-kZ3u-QzrzNWeHAoukIOfjsptmvi3b0Gt3mikMlBK6NLtx_52cnziW-E6AAv5YuABuspBuo7hIi-JQ5xRoJhSYuDn3lheLDNHr23CT9d0jkNqFC5gWeyQWYrHe2I9tOzGArItsdaNe6k-846ggHF5CoGdpwwfkIWj6wFHBSZo9gq6ovHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3833" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LIhpXWhybTnyQkmt5c0BGKo1pHYNzVjotFRT4hYxeKdMEDgMg7MiuFW7TGhuYT2t6_WTE91AFIgQKpTIzHEA-Zn8wRKvFzEIY1bzqxct7PmBBRJEobhJx6aQlgXXafHS2J0aEjfBiu03VTNUz5bRc-eJjyOjMWDwVZTJdsoTbBeLhuTjNBoSHENhlwe0hOJZseqyprX2yzZrYl3MfFoIHcYAD7r_z6T8ajY1NDOvw-_yNTr7IHvpq6UmPX4CrlZ-9bKyc3lg_GhGCZKy8j2iRhaIMWpn6dvN8fS_5VIgYoYrIHgTA_AwgTWT-pd71JALbLcpc6wtbGPyKEuI9HhMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3830">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">من شرایط ضبط نداشتم دوستان. یه مشکلی هم برای لپ تاپم پیش اومده که باید بدم تعمیر و ممکنه کلا مادربوردش بسوزه اگه روشن کنم ترجیح میدم ریسک نکنم چون دیگه پول ندارم بخرم
😂
تعمیر شد، آموزش‌هایی که قول داده بودم رو ضبط می‌کنم</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3830" target="_blank">📅 01:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3829">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWireguard Configᵛᵖⁿ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=Qzs7wr05eQrPSsC0lRMat77_c6zQA2TL2fngsRFXq6GdIDdvKA-AERyDExS3XhjWAg8Dpj_hnn0e9_hb6B5yVseBh9Fe9dd35Rusil5oqhLT5pyKN-yuXJ6y8-Flq-q9B_b5Fa5dbl00eZkH0_ql1GXv59ia8CHbQKjJBPEiWtd4j9lQIdFNNi82NSfvYVC_XtxIcGNGgkxatkAhcRutEVmolkmAhult5Hg5QVYrtvR0S-gYMPqWRLRcJUvDW8jmzuzuZ_mfJrFo00q2X8c_8IZ2VyXtmlVpydXARSiSGyNwhwROVnTxtyc5MT38kezMcz9f_f76Xr3EWe5blk_dLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=Qzs7wr05eQrPSsC0lRMat77_c6zQA2TL2fngsRFXq6GdIDdvKA-AERyDExS3XhjWAg8Dpj_hnn0e9_hb6B5yVseBh9Fe9dd35Rusil5oqhLT5pyKN-yuXJ6y8-Flq-q9B_b5Fa5dbl00eZkH0_ql1GXv59ia8CHbQKjJBPEiWtd4j9lQIdFNNi82NSfvYVC_XtxIcGNGgkxatkAhcRutEVmolkmAhult5Hg5QVYrtvR0S-gYMPqWRLRcJUvDW8jmzuzuZ_mfJrFo00q2X8c_8IZ2VyXtmlVpydXARSiSGyNwhwROVnTxtyc5MT38kezMcz9f_f76Xr3EWe5blk_dLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سا
خت کانفیگ Amnezia VPN
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
🟡
فعلا روی ایرانسل
💯
جوابه(همراه اول ،مخابرات،سامانعلی)
📍
ای پی جدید هم اضافه می‌کنم
https://darknessshade.github.io/Amnezia-VPN-Config/
@ConfigWireguard</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3829" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3828">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کلا فکر کنم ساعت از ۱۲ میگذره دکمه‌ی بمبارونشون روی سیریک گیر می‌کنه</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3828" target="_blank">📅 00:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3827">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RoDNykL7zs7DoKEIY1pDSbyXJ6DiBSvUAJkInr6M8D8b7lyzwQXLn3LwHm7QrKAPmqbKvVcIeXcS5qtueXU06EBhnC5JolymF0uqzpRwNwi65uT8y8JtVkFxj-6V2mxpQUJDlLTLXFfNE4RphJ2cqF0_CfZpzqKLpTFM-QzAmNga1xuP3GbNhoJ1ZY9RPfxbCMAxoT4Ov_gJKNpFGmZpLFDA0nq9p_3f1eJA-ajNmmqCk9Gt6Bw-ljQVpgFkV5sRXcRWKp8zJNEDskJicJvXUMP53kqfrAOnDcdpBupn3S2vJzDJunJGvR5cAqlc-ktLLcixYFmhofx6WMEYv-unWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3827" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اگر مشکل باز نشدن توییتر با پنل BPB دارید، همونطور که توی
ویدئوی تنظیماتش
یاد دادم، NAT64 یا ProxyIP ست کنید. اگر باز هم نشد، صرفا کانفیگتون رو عوض کنید با چندتا کانفیگ تست کنید، درست میشه.
proxy chain هم صد درصد درستش می‌کنه.</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3825" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rilTXpn_ez2ODOsl1qzPvxo-4nQChxCdxYYCZlbsCle7DqgJtZiDxzkB0ASK-L4Rg9My7l_XvqKRTW6WLLnzKLop0RJ44XMj52U_GQ0P9mpKZs6HHOFlH6EHdAwvucCkJ3Stjk0kLd7oLA2TnuPgwsYa_9EXkBfFQBDcAjyojJn20Hvxaj43wp86f_357lRMFb90o227wZwDWO5Nqghqday8fTHPkEBs3NC2Z8vXB0O5GdGzThD9EAnmu8tVnb1WLE-e69RMnuLhi66rzkUxJDpVRDBjAibmabgrjC83UeFXNEh5znXQb7v5RzcmPlA5uj4vebIorMFK33AhgPzieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد
توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش
فورک OpenCode
هست!).
خلاصه‌ی ماجرا: تیم MiMo شیائومی به‌تازگی، دو روز پیش (۱۰ ژوئن ۲۰۲۶) نسخه‌ی
v0.1.0
از یه
AI coding agent اوپن‌سورس
با لایسنس MIT منتشر کرده که توی ترمینال کار می‌کنه و برای پروژه‌های پیچیده و
long-horizon
(بیش از ۲۰۰ مرحله) ساخته شده. این ابزار فقط کد نمی‌نویسه؛ می‌تونه دستور اجرا کنه، با Git کار کنه و در طول جلسات مختلف، درک عمیقی از پروژه‌ت رو حفظ کنه.
از اون‌جا که نسخه v0.1.0 هست، طبیعتاً یه پروژه‌ی اولیه و اکتشافیه — ولی معماری‌ش جدی و قابل‌بررسیه.
ویژگی‌های جذابش:
۱. حافظه ماندگار (Persistent Memory):
برخلاف ابزارهای فعلی که فقط به context window مدل تکیه می‌کنن، اینجا یه subagent جداگانه (به اسم checkpoint-writer) توی پس‌زمینه کار می‌کنه و تصمیم‌ها و پیشرفت رو لحظه‌به‌لحظه ثبت می‌کنه. حافظه روی
SQLite FTS5
(جست‌وجوی full-text) ذخیره می‌شه و توی فایل‌هایی مثل
MEMORY.md
،
checkpoint.md
و
tasks/<id>/progress.md
نگه‌داری می‌شه. وقتی context پر می‌شه، خودش از روی آخرین checkpoint بازسازیش می‌کنه؛ یعنی دیگه نیازی نیست پروژه رو از اول یاد بگیره.
۲. ویژگی Dream و Distill (خودتکاملی):
دستور
/dream
به راحتی جلسات اخیر رو اسکن می‌کنه، دانش مهم رو به حافظه پروژه منتقل می‌کنه و موارد قدیمی رو حذف می‌کنه. دستور
/distill
هم کارهای تکراری رو پیدا می‌کنه و تبدیلشون می‌کنه به skill یا command قابل‌استفاده مجدد. هر چی بیشتر کار کنی، بهتر «پروژه‌ی شما رو می‌شناسه».
۳. قابلیت Max Mode (آزمایشی):
چند راه‌حل موازی تولید می‌کنه (best-of-N) و با یه مدل داور بهترین رو انتخاب می‌کنه. که با
experimental.maxMode
توی فایل کانفیگ می‌تونید فعالش کنید.
۴. قابلیت Goal Mode:
با دستور
/goal
یه شرط توقف تعیین می‌کنی؛ وقتی agent می‌خواد متوقف بشه، یه
مدل داور مستقل
چک می‌کنه که واقعاً شرط برآورده شده یا نه — در نتیجه جلوی توقف زودهنگام و خوش‌بینانه رو می‌گیره.
۵. ویژگی Compose Mode:
با زدن کلید Tab فعال می‌شه و یه workflow ساختاریافته برای توسعه مبتنی بر spec ارائه می‌ده — با skillهای داخلی برای planning، اجرا، code review، TDD، دیباگ و merge. کل چرخه از spec تا کد نهایی.
۶. ورودی صوتی، Git و Multimodal:
ورودی صوتی real-time با
/voice
(بر پایه MiMo ASR و TenVAD، مخصوص کاربران لاگین‌شده)؛ مستقیم با Git پروژه‌ت کار می‌کنه و multimodal هم هست.
۷. سازگار با Claude Code:
authentication، skillها، MCP serverها و دستورهای قبلی رو توی یه مرحله import می‌کنه از پروژه‌ای که داشتید با Claude می‌زدید.
۸. انعطاف‌پذیری مدل:
MiMo Auto به‌صورت
رایگان(1 میلیون توکن اگز اشتباه نکنم) برای مدت محدود
و بدون کانفیگ در دسترسه، ولی خودش هم از هر API سازگار با OpenAI و prov/erهایی مثل Anthropic، DeepSeek، Kimi و GLM هم پشتیبانی می‌کنه — یعنی vendor lock-in نداریم.
نتیجه؟
طبق ادعای شیائومی، توی بنچمارک‌های SWE-Bench Pro و Terminal Bench 2 (به‌ترتیب ۶۲٪ و ۷۳٪)، با همون مدل پایه حدوداً
۵ درصد
از Claude Code جلوتره(که هنوز بعید میدونم. به چینی‌ها اعتماد ندارم). اما می‌گن تفاوت واقعی‌ش جایی خودش رو نشون می‌ده که کار طولانی و چندمرحله‌ای باشه — نه «له کردن»، ولی برتری معناداری توی long-horizon.
نحوه استفاده (خیلی ساده):
۱. نصب یک‌خطی (Mac/Linux):
curl -fsSL https://mimo.xiaomi.com/install | bash
(بهترین تجربه با iTerm یا ترمینال VSCode)
ویندوز:
npm install -g @mimo-ai/cli
۲. اولین اجرا:
خودش راهنمایی می‌کنه — MiMo Auto (رایگان) رو انتخاب می‌کنیم، با حساب شیائومی لاگین می‌کنیم، از Claude Code Import می‌کنیم تنظیمات و... رو، یا خودمون می‌سازیم.
۳.
می‌ریم تو پروژه و کار رو بهش می‌سپریم (با زدن Tab بین agentهای build / plan / compose سوییچ می‌کنیم).
لینک‌ها:
- گیت‌هاب:
github.com/XiaomiMiMo/MiMo-Code
- سایت:
mimo.xiaomi.com/en/mimocode
- بلاگ فنی (درباره long-horizon):
mimo.xiaomi.com/en/blog/mimo-code-long-horizon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3824" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3819">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UZoaac8q0hHu364DKTj-FsSEqavGCp3u_7wqcUT3jsw_jdIJd-VF6r-aoSMla-UL8QBM4aadKeDMUwv8HfBrSilCWCNp3ok1ushUQfLzmVQXQ0B_O9Et_oRjeYoJOAET9vvmVV4VG8at_zKS8pOA1-dafMhX9XMjUglxaNNGVhH20tdqCbRxTkq-Xxw3utwc1eDt8ilxlUf3HpvUC3dLN2XZkSq5rprY7SVGy8bAIQeoHHUgHIt6eJVc1nPgpRh66xMUe4XiskgDcc-lA7pna0GQVpr0u7h9laAqWND9k2666uRW70zbJnHcVWAcydgLASlA3KdV1ZMCypXNGbCkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از ChatGPT بپرسید که
یه عدد بین ۱ تا ۱۰۰ انتخاب کن
بهتون به احتمال زیاد میگه 73! علتش رو هم از خودش پرسیدم:
وقتی کسی می‌گوید «یه عدد بین ۱ تا ۱۰۰ انتخاب کن»، من واقعاً عدد تصادفی تولید نمی‌کنم؛ بیشتر یک عدد دلخواه را انتخاب می‌کنم. بعضی عددها مثل ۷۳، ۳۷، ۴۲ یا ۶۹ به خاطر الگوهای آماری و داده‌های آموزشی بیشتر از بقیه به ذهن مدل می‌آیند.
جالب اینجاست که در آزمایش‌ها، وقتی از انسان‌ها می‌خواهند یک عدد «تصادفی» بین ۱ تا ۱۰۰ بگویند، عدد ۳۷ بیش از حد انتظار انتخاب می‌شود. مغز آدم‌ها از اعداد خیلی گرد (مثل ۵۰) فرار می‌کند و به سمت اعدادی می‌رود که «تصادفی‌تر به نظر می‌رسند». من هم تا حدی همین سوگیری را دارم.
پس اگر چند نفر قبلاً همین سؤال را پرسیده باشند، کاملاً ممکن است من دوباره ۷۳ را گفته باشم
امروز توی توییتر اینو دیده بودم و واسم جالب بود علتش</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/3819" target="_blank">📅 15:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3818">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mT5T6sX8_-Hfn_O38N-hcg7PNVM2BF2Ap_Vdb4JdVvmhmd-jIB73xPZx5n9BEmoVX4U8-es5iAH61skx4P3BqFS8ovI0ljEunjVlZGzneCsUDHPODr6mVrUfPB9yCvLpS_M0Zupo0ff-9BK1T-aRkKiL09m-R5dbAfPEpZVqHsl0DAG8EP82T4YxQ4mXbroqVr6xlb3n9UxNIxheemKBjlemWQ7NcfujohDP3-NrMMWSdyDrSmZdW0uT8hg9kNwhpKmHOuuz_xJ3sRwMrGQ7RYZSBXRXl7b00ssjyIRFp3LAAZmsyxd5yzn50f2S0d_C_yH_ElRvDdQQLjbfgBfGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار باحال آنلاین پیدا کردم: یه عکس می‌دی بهش، بهت گرادینت میده با کلی تنظیمات.
برای وقتایی که دنبال یه بک‌گراند یا پلت رنگی هماهنگ با یه تصویری، عالیه.
تو مرورگر کار می‌کنه و رایگانه
👇
photogradient.com
‎
✍️
Reza</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/3818" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3817">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
ابزاری که امروز معرفی میکنم...
داخل این سایت میتونید تمام ip های مربوط و بنا بر نت خودتون چه برای ورکر و کلودفلر یا شیر و خورشید اسکن کنید
❗️
ویژگی ها:
💡
اسکن راحت و سریع و دقیق
رابطه کاربری خوب برا همه سیستم ها
داشتن ip بیشتر cdn ها
لینک سایت:
✅
https://cdn-scanner-pro.vercel.app/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/3817" target="_blank">📅 12:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3816">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2658a29175.mp4?token=Jw66ZCe7VMyR0F4VGgUVY7QpNAM_xf0K1DKLBKvDLiPPqop-0Q6IlTUJMSDUDMsXanyK5AXfl-P48ympjvrHewx2PyEBJSVfFB5khM208OFDMDnBZQH8wyC0GppoWdWJlU-QaihNETTo0JLF2s9MvVOEKc5DWrmXL5BoXGdE2zIwZm7ilHBCiZGV2Ua5KaK4OjKGp6_BnMjPWrmmFssPSjhmB-DTaA6tJilwKBd5TbUHV-UJ5_PfqHOcU-fSva2Sztl25-UjrrU8PhG1Xwj6UltOu0LrZCWIeqcG_2KFls5KTUldiFj5iEhSwmPCE_kMOpe51HsINRdFtMtn9AiJEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2658a29175.mp4?token=Jw66ZCe7VMyR0F4VGgUVY7QpNAM_xf0K1DKLBKvDLiPPqop-0Q6IlTUJMSDUDMsXanyK5AXfl-P48ympjvrHewx2PyEBJSVfFB5khM208OFDMDnBZQH8wyC0GppoWdWJlU-QaihNETTo0JLF2s9MvVOEKc5DWrmXL5BoXGdE2zIwZm7ilHBCiZGV2Ua5KaK4OjKGp6_BnMjPWrmmFssPSjhmB-DTaA6tJilwKBd5TbUHV-UJ5_PfqHOcU-fSva2Sztl25-UjrrU8PhG1Xwj6UltOu0LrZCWIeqcG_2KFls5KTUldiFj5iEhSwmPCE_kMOpe51HsINRdFtMtn9AiJEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیگما یه اکستنشن کروم منتشر کرده(فعلا برای کاربرای پلن پرو) که با رفتن توی اکثر وبسایت‌ها، می‌تونید با یه کلیک، تمام اون صفحه‌ی وبسایت رو به شکل فایل قابل ادیت فیگما دریافت کنید.
برام جالبه که سر بحث کپی‌رایت و اینا کسی بهش چیزی نگفته هنوز
😁
اما خب گویا هنوز با چنگ و دندون قصد دارن نگه دارن اکوسیستم فیگما رو بعد از اون سقوط سنگین سر Claude Design
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/3816" target="_blank">📅 11:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3815">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!  همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.  بعد…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3815" target="_blank">📅 10:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3814">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uHpAa39K4tno4X5YWodIGLl5X_hmrlps8PjSQx3nifG1UHMKOwSDCBj32m2np-BweZINRDnBfwtRUek61kZIQSZGWhYTWdTEauEFX4nnW19cgK9gTv2k4tzRggCu8ZyH0lTECHfOP_54vMci5azgCaJNhQpunUgDVn1aEBCySJJz-rgUhj5iCjwi-rXKV1x_0nZS293Y6AHAp8dBVlbotnTJJfkoPmZfIOllxSEuIpQydLU4BF3zVyjOtfiy7QtXCxwhjKhrLN3HI-hEOzj9Jv6W0pu3yQehIyQfn5tc8T5IDrfhGHAH2zrZ0e7JzRK3WDslrNSdLmSRSW208sRPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!
همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.
بعد از چند دور summarize کردن، نهایتا بخشی از دیتای مهم از بین میره و تسک به صورت کامل انجام نمیشه! پس اومدیم یک سری تکنیک پیاده کردیم مثل تقسیم کار بین sub-agentها تا از پر شدن سریع کانتکس اصلی جلوگیری کنیم.
بعد این ایده مطرح شد که بیایم هدف نهایی (PRD) رو تعریف کنیم و اون رو به تعداد زیادی sub-task تقسیم کنیم، بعد مدل رو در یک loop بندازیم که با هر بار اجرا، یک context و یک prompt جدید داشته باشه و بعد از هر iteration چک کنیم که تسک به صورت کامل انجام شده، و در غیر اینصورت چرخه رو دوباره تکرار کنیم!
در واقع به جای اینکه برای اتمام تسک به مدل اعتماد کنیم، ما در یک لایه بالاتر این رو validate میکنیم و اجینتِ تنبل رو harness می‌کنیم :))
✍️
Amir</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/MatinSenPaii/3814" target="_blank">📅 09:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3813">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j9KAPRz-BQ1VJiEhqnXYwx7xvZkmt4lVnkfOrNz0nbDwvWI8WQlAp3BsAFOVwa_Xq_trAfgX3DH3C0P3rf60KhpH_dOKrohoUWP3lsnaJxYDbeLwXpsT-vja9DlECPHaaov37pTSXJ1k0yyyPkWjfHOklGkcIwEerNlnmvne-_dBaJokGsJtpTnM6kYUW7JBPavPKrspdiApYWPwL505CX-t-6lPhSJuKJlkjS60zeLcsETLgHN1mQnAa2IJo7QIkSgegT53LnpZCw3yyXr68xH3dYBVB0IbWKUzdzUfYD69hl6Y20fvUfVU0quNER4afrdUDhcYEOpj2OI07lrX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله شما می‌تونید دامنه و سرور خارج رو از سایت‌های ایرانی هم بخرید، اما چندتا نکته وجود داره:
۱- احراز هویت سایت‌های ایرانی کلا جالب نیست و خب این ریسک رو باید در نظر داشته باشید
۲- توی شرایط قطعی، فروش دامنه و سرور همه‌ی این سایت‌ها میره روی هوا
۳- شاید عجیب باشه شما اگر از سایت‌هایی مثل netlen و با کریپتو خرید کنی دامین+سرور رو، شاید ۸۰۰ هزار تومن(با کارمزد و همه‌چیش) پات بیفته. اما همین دوتا رو از سایت ایرانی بخری زیر 1 تومن نیست</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3813" target="_blank">📅 07:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3811">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نکات استفاده</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3811" target="_blank">📅 01:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3809">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rqwlAJkVFKNmg0CahQhr2qFhupTxqQyrCKZhOECKIqjdj4sDzIYO3UuLhcUIGX3kDoK0jFt6MdI-BXnNflujJNBVrI6fj8WE7HkTWusRges4nv21ZQ1A22lPoQyJFcd50CnMkEbt_fmbuscjisC7TjkUAbRD2pWRlSSdr9SHjaiJz_HkbrQA10vWlgAPBiIcng9g-LtdGmmA20YB3xK5EbGdY5lctPccGuNz8sHGbyd_v9Wp4JAQVPyQ_wZR_OSGUWu7ZBIJD24zyxufiUnTf8kqv3fr8C0xcUqqCSekqTV_edHSLmOanlZIY264VdN5OYhzucSGjaynpbGsJkzs2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran  * دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)  ///  * حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)  * کافی است لینک subscription را وارد…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/3809" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3808">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/3808" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3807">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mFG_rzs_4oru8ODj_YhJTnUHifsFsxdSFjh7r5RCqE2QUknBsyKT3bvH1yEY4kL05HkgRVPolmu1KqSGE64CFuJEQBS2mOFd6G8Rb1vXYhH_OtVJKqoi5sTeUli64OfRWreE3IDsUtMJNGSgHThDaABAG6z9M2txVZFWwXBFYM3-IXPqJAHRGu5P3dJjXgetZmMcVQfNn9oP1BGSqIz0E9wacsWf83MYS6VisbZrPGNElytvUsY7LC48QpHk-8DUHYBdZ6FFSKS8l3XUiG_Ijd5Ihc1uXdxewxkXqwP6VDHTUJICYFhSNw5315kh1ncXScLaFyFgNcQOlKcV2OqucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از http://Netlen.com.tr بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰ باز هم خود دانید</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3807" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3806">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">درود به همه رفقا
🍷
اگر از پنل bpb و... استفاده میکنید میخواید ip ثابت باشه ولی جز لوکیشن آلمان
🇩🇪
میتونید از ابزار زیر استفاده کنید برای ip های مختلف برای مثال:
میتونید از ip چین استفاده کنید برای دور زدن تبلیغات یا از ip آمریکا برای بیشتر هوش مصنوعی ها خلاصه این ابزار مشابه واسه خود bpb برای ثابت کردن ip هست ولی با لوکیشن بیشتر
❗️
لینک پروژه:
✅
https://smart-ip-scanner.10-354.workers.dev/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3806" target="_blank">📅 22:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3805">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید  محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان»…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3805" target="_blank">📅 22:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3804">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IJ2CmFbS44RMoI0AZxgXbd386PmlQk8stmOSp6w0p34JuMDnEfMvXXUhslIbgphd_zLDKQ8gHih5nEj2NYNglRcC-V40BXm8BzwY3K9-K3SCJgqla8YXx4-xZjWcbugxIy7xtQe0Ewhmv_a2eYsqvhcB8srq9kQzH9894rHUKE6UCJ72GlZP6RNObt4oBZvzFdh6_GB8TS7HUZ7AijuT2s333EuKWJQXUAODb_lLeUq5nXj3Cvj-J_SrqKSImzyNLjfrH5Cs-4dKbCCDKMXJ9SUgyE3o9t9LaB5M7iOBL3kmkKIvkh2BYZh6t7wJK2cqSSslRUsFCpi0qkgcYvMlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید
محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان» (X-VPN) است که برای نصب بدافزاری به نام STX RAT روی سیستم قربانیان استفاده شده است. این بدافزار می‌تواند رمزهای ذخیره‌شده، نشست‌های فعال و اطلاعات سیستم را سرقت کند و به مهاجم امکان اجرای دستور از راه دور بدهد.
در این حمله سرویس ایکس وی‌پی‌ان هک نشده و کانال‌های رسمی دانلود این برنامه سالم هستند. خطر اصلی متوجه کاربرانی است که نسخه آلوده را از منابع غیررسمی (در این مورد، یک مخزن ناشناس در سرویس Bitbucket) دانلود کرده‌اند. در پاسخ به این تهدید، ایکس وی‌پی‌ان به‌سرعت آپدیت نسخه ۷۷.۵.۳ ویندوز را با کنترل‌های سخت‌گیرانه‌تر منتشر کرد.
➕
نوشدارو پلاس: این هشدار مشخصاً به نسخه ویندوز X-VPN مربوط است، آن هم زمانی که کاربر نسخه جعلی و دست‌کاری‌شده را از منابع غیررسمی دانلود کرده باشد. طبق اعلام X-VPN، نسخه‌های رسمی دریافت‌شده از وب‌سایت X-VPN یا Microsoft Store تحت تأثیر این سناریو نیستند.
▪️
روش زیرکانه هکرها برای اجرای حمله
این کمپین ابتدا با نسخه‌های جعلی برنامه‌هایی مانند «بایننس» (Binance)، «بای‌بیت» (Bybit)، متاتریدر ۵ (MetaTrader 5) و کیف پول اکسودوس (Exodus)، معامله‌گران را هدف قرار داد. آن‌ها حتی به سراغ پلتفرم بازی استیم نیز رفتند و در نهایت تمرکز خود را روی کاربرانی گذاشتند که از ابزار تغییر آی‌پی ایکس وی‌پی‌ان برای حفظ حریم خصوصی بهره می‌برند.
💡
نکته: بد نیست بدانید شرکت Kaspersky (کسپرسکی) پیش‌تر متوجه شده بود که همین بدافزار با نفوذ به سایت CPUID، بیش از ۱۵۰ قربانی را در صنایع و کشورهای مختلف آلوده کرده بود.
بر اساس یافته‌های شرکت سایدرز، مهاجمان در فایل نصبی اپ‌های معتبر یک فایل مخرب به نام CRYPTBASE.dll جاسازی می‌کنند؛ تکنیکی که به آن «بارگذاری جانبی» (DLL Sideloading) می‌گویند.
به دلیل ساختار سیستم‌عامل ویندوز، فرایند نصب برنامه در ظاهر کاملاً عادی پیش می‌رود، اما فایل پنهان‌شده، بدافزار را مستقیماً به حافظه دستگاه تزریق می‌کند تا آنتی‌ویروس‌ها متوجه ردپای آن نشوند. پس از فعال‌سازی، بدافزار می‌تواند ارتباطات خود را در قالب ترافیک عادی و قفل‌گذاری‌شده وب پنهان سازد.
▪️
چطور قربانی برنامه‌های جعلی نشویم؟
دفاع در برابر این نوع حملات بسیار ساده است و نیازی به دانش فنی ندارد:
• دانلود از منابع رسمی: برنامه‌ها را فقط از وب‌سایت اصلی شرکت یا فروشگاه‌های رسمی دانلود کنید. این هشدار برای ما کاربران ایرانی که اغلب ناچار به دانلود از منابع واسطه هستیم، اهمیتی دوچندان دارد.
• تایپ مستقیم آدرس: برای جلوگیری از ورود به سایت‌های مشابه و جعلی، آدرس را مستقیم تایپ کنید و روی تبلیغات کلیک نکنید.
• استفاده از نرم‌افزارهای امنیتی: داشتن یک آنتی‌ویروس قدرتمند و به‌روز در کنار رعایت اصول دانلود امن، لایه محافظتی محکمی ایجاد می‌کند.
اگر گمان می‌کنید نسخه جعلی را نصب کرده‌اید، فرض را بر لو رفتن اطلاعاتتان بگذارید. فوراً رمزهای عبور خود را از یک دستگاه امن تغییر دهید، از حساب‌ها خارج شده و احراز هویت دومرحله‌ای را فعال کنید.
✍️
یونس مرادی(نوشدارو)</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/MatinSenPaii/3804" target="_blank">📅 21:49 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
