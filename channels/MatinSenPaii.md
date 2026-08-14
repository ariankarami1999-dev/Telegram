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
<img src="https://cdn1.telesco.pe/file/B7OufTAJOzZrQUbONepr9u_0ZC-ShZy0_rYgDBk6e9LsAPQ08xvEwALBc6HGYOTjuT6cSYVs7x9JaECebvQsj1jZY9fTJL7nPQBomb9jnWsrLrocRjjRsA9II6ZjJDIySlqWRJkGyfYClnTsYPjdLa3bAfSRHRDLlIjo8dG40DE9S1yciQ_JkgDMb8aHo_vizU4GOhW8oH2SvEeBD79RneI65l4Hy8ULD9n8r_RSDkO6d7DHdHSKQH8ms90plCaNsZb8tqeRut4qnnPtjI7rqWc-O4bULeOKxKaklPoqbk0i2QA0ME07ZbzBj6cpKy-8wu5ThIbDDfU01o71nNZmuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 13:02:44</div>
<hr>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">جالبه که من دقیقا سر Kimi3 هم همین مشکل رو داشتم توی کلاد کد.
الان توی OpenCode + DeepSeek V4 pro این مشکل رو دارم
سر دیپ سیک فلش هم داشتمش اینو توی کلاد کد</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/MatinSenPaii/4928" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uYUEspiy4Y7W51wyDlOX84IFH6ziE5RYjakEf4IeqWLJW3QFOz7uqujEizO6DFv1G6F4LoUAhy7jQBmP9pFJQUre2H18g6-RnxgB8gFXw570gSrpMJRa5q0aRUmvpxqGBPm6NRRNarvKTWt8Fa_yuHDIUp7UnCNmS_NrVYVdKXHlIQX5WI9njPiy3W1pXU5uVHvxbcDA6d7sLpUDRo5urhD37D2x0Tb5qn9Xssx4dBo5lg_kf0slAd-3LM5hssGpFlfxTh_I_XIi9QQNJFS_4MY2z61cZWl4pTaJ6H3vsTC_-Ihfh9xhH71QG6bGsOXaSBA4mCDdKD2-i3fxCjj4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا عوض کردن VPN فقط باعث میشه که از اول شروع کنه به Think و من اشتباه می‌کردم</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/MatinSenPaii/4927" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/MatinSenPaii/4924" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c15mQx3uxxVYkg9RA3g-tgQfvGU6Nuc_57VQjrLqW5ehxkUM_wRDvpTnfcIHN-umSHnHzjwy_5yh6DaHIIqT9CKYTbSMKjLkRGBE00QEGcR9KW9Hh1Xz4OQRijNsQk0hAF9U09vFyBHaHqAHQDlYJ7iTBXTIZKHRxGPfU398m6Tgyrj-ALua5udgrfJRia2b93dcJ1HUdLwYB-GcMJxT_i8ChhitIKznkdfx-cSIUNs2xQIyzILvYDrZnAWC7feDZrGxwt0HvhlHbh9KaDwmSwLPZOLKyFGtB3zHs6th-muaaiUT03T9JcdSvLY6-sDTOqvp3p5rtpqYE-WJ5Fz1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو
تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/MatinSenPaii/4923" target="_blank">📅 10:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vPohOmeyrp4MdIohWphBFlneyjAMNxNXNO0SGhxcbSZAHsfoOHtPNFxrB2XFQztBtnIHyzJUwbtnH7aYqURcMQQONxcsO7CKskFrEeH2XGdjVE_nmpYQJRmnWMZmpeeLXRn7_3EXLF_FvpLXY2wkTLDexLg1YQEWzt-o5jelNfIs_8ApLIxiU1VKS2xewATKjm2o_345oRVDDnnecvRhChSYIM_I99H4H5_SSwEntyAfRz8OIqr_Yv5kOE1CZKYMgDR5KSAMF9WDNsfte4JMby8gyEqw8HHtlIC0yl_bFj5K4zyEk7nGIwo8Od6mQ-RdkMeRRjB28T2toRvKMqfwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از پلن فری هرمس که گرفتم</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/4922" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lOXOUGCbKP7vxmrrxIjVjLzM3l5yIvKwUI6A1tHjNahumbPmvtCd3-1GSI-8tXF1BAzVIVbsEJqqvmxqRiU8DXOB9a-md8DiALK8KPbcLTlLYp84kX619FRRFZ8-D0YePigjTZuB5xgrLSpI9LWFZEARDsNehtrjL3QhL83AWNU4Lcmy55zMOJU0m2WHtz9lSkdwmNKsr2B4O3gzqtkL2Kik_cBK5Hn5ngBUjYV1UtBpc3FZNSTHf2QGfSV01gMzCG5sAYSOTTI_HdmbGFlIblmCA2NWZ6piYorc4yUsjQjUl3jSjAXCHgavtloBumACdzAityssU1H4gKADU38IMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/4921" target="_blank">📅 20:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگر روی 9Router+Antigravity به ارور 403 می‌خورید، یه بار اکانت رو حذف و دوباره اد کنید درست میشه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/4920" target="_blank">📅 20:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4919" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fpAeZizEN6KthjNCE1LRoslaU9e1OMX8llm-U-AzNq76fkimSQOun8drSRoNWq3I2OjD4fkzSgjeRje-c5vfJ3JlYlFdvJpE0k0TKdgT2mWHozp04HP3xpDl14tdYEXTXHv2XNGS7ghY2k0Mtekvv_m0m1p81cM5ZxuByBYWmwsT4EohUulgStpzzf0ZI1U0P07NAO0Nb1J6LWcG_JQUhS2Me8A1QkDyyL8DEplwB9uq1icTG0pwH-KYc5pOIN3GfXtKi9fj0mCAfOrktOakp3YzIUtKf590zlNsjRYvQBhs44x4Ft0id4LwPTeVzsyhBRyjKjT06ynEKZPBe5kTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4918" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BAg0BzqNoWoGkAAZ-8RV5Vd0LrftcyAhy4z0PN9Z3pGA1J8AO72XiY4Sz5mtSFMv8c7nzw5Ou_Dl9TN-9qbC5N-Fzzx_DFUTkERFK2lAjF12aQN2S5jvIqP7O-nnwaBbVmf8BrXkEuW6FCM6ixnLR83FOcmWJbD8vTGhnJHjv8Zk5GSceQA9_X2XpmJKgUD4E8OLHt8UJMI5n3eNkWRNazSUwXR85rS_a5KfJMkzNyK8Cf0JRgRmBGHRHNoEAPayAF3egXR-y5Re8JgwKYgtVc5xF41keSSlJ0MqepifTyM3HJZoc9TlqXWm2VMfxbvzvP296IKjR94XreIEFI3CcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gfrlDzoqPvlP64_KTX8Tr8xFk4_c1AGVKSUjx1qPUNUF-TptGitYGfvjavvcun3yuuoIUxQqN5gU8_sjvZl_b_CeKvd8YjLKlBynqR_Be2Ho75Q2CohEZWHYcr_sNuZqpEpuhQ3kNE-PqCftBg7Jy_vlJeJwz8HKkchH0wbWzeow4tWagQqCfxwA7CwQalnBLdij6NOia2IkNcLUoP-luryL2rObVHUEMjR_qU5X2kQHX_tYcCK1EwF8MYqgxNA7oasaZ2sHAw4gwc5hp9mfixx8kYBLMLuCcHlmNjr3u_V5o1k4-Cs5A3aIlJdXfryN2wH5p1buXy5voVJtAOfiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MPGHUwOpejzudQ4qTIKtZiq53xALvnguBUeHvZdOonVLw0ny_jiv_5WoSpShk4HbdBV2cl4-u5l_agQ69J8rrAZBkedp7nJF_j1z1sP-U4VjB4RKK0wxkv_W0ev3oYJSz1vRdVATJ9vnH7sfFSQQpOBDRaEXrHSJaKV6dGZbfPTP_4ZuPA1KUgTPvZ6NkTXqmEuneRInVqNVCiUPuMlnPYKDtN6PYaajCntyN7rCRlm7jJXtHV3lZNwfAm5RiW2oiJEoNCkvPyJ76s7jE8R9TfodnlS2GAGszggAyYRjorMNtBqjxze3GT61VHs3jBiF2bYpygyKa_qLPA9OIEfAlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی
خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید:
https://app.mpay.cards?startapp=ref_PzwXZ8
(لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید)
1- بعد از اینکه وارد وبسایت شدید، Next بزنید تا با تصویر  اول رو به رو بشید
2- روی Apply بزنید
3- با ایمیلتون لاگین کنید. دقت کنید که تمام هویت کارت‌های اعتباری شما روی این ایمیل هستش
4- بعد از اینکه وارد شدید، با کریپتو 5 دلار پرداخت می‌کنید و کارت برای شما فعال میشه. از USDC و تتر و... هم پشتیبانی می‌کنه. برای آموزش پرداختش با نوبیتکس و...، می‌تونید یوتوب رو بگردید. من خودم با Trust Wallet زدم USDC و مشکلی نبود.
5- تبریک می‌گم، شما Visa card دارید به اسم خودتون!
مزایا:
- می‌تونید توی تمام سایت‌هایی که نیاز به کارت دارن و رایگان، اعتبار خوبی میدن، ثبت نام کنید(من توی Nous Research پلن free رو فعال کردم)
- می‌تونید برای OpenCode و سرویس‌های بین‌المللی، با شارژ کردنش پرداخت داشته باشید(کلاد رو هنوز امتحان نکردم)
- و تمام چیزهایی که سالها از ما گرفته شده و ازش محروم بودیم.
- ایرانیکارت و سایت‌های مشابه، با مبلغ‌های فضایی و میلیونی فعال می‌کنن همین رو. و به نظرم 5 دلار، منصفانه‌ست
معایب:
- برای واریز به حساب، باید اول 25 دلار شارژ کنید اکانت رو و بعدش می‌تونید به کارت منتقل کنید. تنها محدودیتی که بهش خوردم همین بود
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/4915" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ogmT5PsfmZPGWVwm9lJxIJvWLx82_k_j1uFEKck2Z4N-5iPjyfN9yorlt95PE0qaggpdgTtL-rBwhhOegZmur6mQWd4fJYrNv-y5bf5EG4JuJmSuc62dL0-DJ9GCqMudgDr4BGBu-2nhs7ew00OvESeUQ0-eBhw-NYNH-llTxIfzptdYfoYSFRVeLxxzivjr8GeqWaOsoI-2391IuAsprnfCmJaWtDtRVJVRjRzxVwk0xnRCXCP7cKGUqH2FKZc75ricX9jU3gbapNMSJdWlj_LWf5ANGARkUBUKg8livJkAqxaouXiABBT9H-I2vQCg8sDcWb98kSanQ6yeGS0_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.  از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/4914" target="_blank">📅 19:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">همینطور روش رفع تحریم آنتی گرویتی هم چون یه کار کرک ماننده، باید همینجا آموزش بدم و اصلا نمیشه یوتوب گذاشت:) چنل سر دو دقیقه استرایک میگیره</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/4913" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.
از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم به صورت متنی</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/MatinSenPaii/4912" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این دسته‌بندی جدید کاناله، با ادیتور جدید عزیزمون محمد.
پلی‌لیستِ "قصه‌های مدرن"
قراره چیزای باحالی با همدیگه بخونیم و یاد بگیریم
🤝</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/4911" target="_blank">📅 18:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SMPsTCDTHbMC1CrZUNTSXgNqd9luOxb9KB3ZqfgCYa4JesIHc4dIAiOTtfBegdJ9-lzqIdcyUQOSb-u2sMNIvOIe2dyXCQOkzj3XT1Avr6Rv4n00ZZrYk_bk6uFqEGy3OL31llLJMFtRzxFZkHphBMqwYjYQV6d2aLSQ9fSOvhlYrEbNZpkGgW5sV4MAiDTuWLsCyW9NE7QMjLf0EHLVOtdx001pNcHjwSYnOpYOSmxHcM1MVO8-jnPhN_ZVhYzxTpjJKCA7aLbyuJ_EV_Ouw-h9KdqtUoVdtPXlxTdXdNCbF5ns0L7nNJO18nTY1BQa__qYXTFFoIHEVq79unKdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
قصه بارکد، خطوط سیاه و سفیدی که دنیا رو عوض کردن
هر بار که کانفیگ V2ray اسکن می‌کنید یا یه چیزی می‌خرید، دارید یکی از هوشمندانه‌ترین اختراعات قرن بیستم رو استفاده می‌کنید. اما داستان اختراع بارکد اصلاً شبیه چیزی نیست که فکرش رو می‌کنید؛ نه آزمایشگاهی، نه تیم مهندسی‌ای، فقط یه دانشجوی بی‌قرار و چندتا خط روی شن‌های ساحل!
توی این ویدئو با هم می‌ریم سراغ:
➖
اینکه بارکد اولش دایره‌ای بود
😂
و اینکه چرا تا دهه ۷۰ روی زمین موند؟
➖
لحظه‌ی اسکن شدن اولین بارکد دنیا روی یه بسته آدامس
➖
بارکد دقیقاً چطور اطلاعات رو مخفی می‌کنه
➖
چرا و چطور QR کد به‌عنوان نسخه‌ی پیشرفته‌تر بارکد متولد شد
📹
تماشا در یوتوب:
https://youtu.be/PAHA55mHLWs</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/4910" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">و اینکه مدل رایگان Hy3 خیلی از Nemotron3 ultra قوی‌تره. از اون استفاده کنید</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/4909" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l8_v34ozP9ZePTDyvWXoqvr5vck2LJRuikkCkbqykq-TRCTfCHOhoSlz3uMUy__O9DC6xM8uDGVBpxwLoTSf5fDhXO0TRG4VRMB3kga1-QTpBGg2rBc2iZ5lUd-7kT4yQKm2k55q8n7m4UkJV1Ufg3aSY3qiDgI2PQ-HvweQk7SKdv4xffoZIEX4E4UTPD4gMQNAggyD6crWxEE1BxEynUe3mSz_yXIUUsZxNtK2h-2Z4EDDnkJcVxEyhrhvtq8VXjWNbGrO4a-K6AGe2YNJIiJB8dZ-NgeT6hQW-FCOSKA0N1yIqmEIEIq8eX3i8cj0DrS4-loZf12pGH9jQ5gqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا به آیپی‌های کلودفلر حساس شده کانفیگ‌های کلودفلر رو با آیپی‌های دیگه chain proxy کنید باید درست بشه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4908" target="_blank">📅 14:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده و فقط روی خود OpenCode در دسترسه واسه‌ی خودم احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4907" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده
و فقط روی خود OpenCode در دسترسه واسه‌ی خودم
احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4906" target="_blank">📅 23:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حالا که شماره مجازی و کارت گرفتیم، هرچی سایت api رایگان میده باید شماره چینی تایید کنی و پیامک بیاد برات
😑</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4905" target="_blank">📅 22:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Li3EdOCHMgCELbhGS-oWvQkvEJ69cl0oy2zcT6zeL8KJOLTmab5j4jkHG6FZcE3qtDY3GlTAVrwfRoDY6yGBxVM4q0UI7vYczH_V1Oy2KWbNq5xYrS4HI3JtgTFSiCY33H0LhO0A8degRneNASJzJmRArO-Ie042Q6Bv9axHgXBz-TIeXkFJVlOu2CWfZnZlu6dQE2B5ZfOCAbkrw5yn3sATdYnGBXyN0lk7oyfUocif3nNx-Uj1jo7uW1rkxGae6sCBsrQ1Sa1pDnKuwLT27OvxHS-hNrmp_bB69rLW9JPyBJ1G3o9nqc0vOsbJCHZJ-C1PFD6DB32sC1jJPG1qtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dpy2BwSHmndX82QpVyVIm8J4Ni_-pncnJv-3_stxPMLZKChxDddO-9p0uLBniECPelFC7a_EXxlpe3gKy-rts6FOSPG_BN0LQlEEogiu5f2NDx9zPpzMPtq1x_CDWRbpkc6wysRp4EPZ1WQeeSHMKdG4vdvghafYbi2waICef2oYJJK8KRB4PFUWEXpViLhwkrLFkPRveVT50-ONaytNI0g1wG0NdH5k6rHzfHlINYyIf5x27mVTb0N9jpwRYDdepAMfy6wcPZWWEqJKYMkcjLB2nVtSEwSbL1B0NnCg9JEjXoC39Wm7jejFMqni3G9koQd_er7hL_-Ql_qYAtCbcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLF6UO-gUas6WrcHRZJ9q6uAHaYJA_1-NgwHkaMeSQQXT-NZgtdUM_8n3cGz9MTxXY23YsY7xTa0GlXhF89J8oLDp8VVNv0VhrvwTPky48tD3o7jHvekyPPVIkA8fR9-QI3Eoe0JvKPbMIayE5RvxdxTkkg4riz2lx0xSLt9ENX_fN7BEUrx5KB97R5UhuLzUiUb2hJWTKFCGhwGwVyqSLVC0aEmdTbdFPBFlk7Et3AeoLPjkirxoaJw2lVknRQMQzCjBefxj3Lx1bh5uhSRqSwKf2VMwKCZozZ-uCAqOV6Vae9yojz-mkeCRd5r6DpTWbVWzl7Sc50eB5eeB8_gzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q2Sappey_SY-CoQr4wDhEuvwWaewo70d-8WIhYseAXlO1fe7wv_pUhMPSUmgENGNjCQyRthNaZrkyrVeowVNlaUAz18zT3FHEgfStEGwtP-NuKuvcSsXtivDJV45G9spXwlpoIW5itbzeex9VSPbShX7draMIZwK_9-Lh_k0tdCCpH-9dhKQECdF47lkwSC3pdXYTLp7Sy3iCacmSrqOnG8WsB_1B8-4wl2Y3Ny3J_XJV8HQC4KIyvYb8hIAvK4Zxr0CALFLvRl2N74FJBQc69hU2-0d_h6l4vkuC6fH6WUq8iUf3hV2uPBP-j5DqK4ILbpCOX-vBOHQQ9wNQ3B9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cdz-fJLtZwxtVVnlaCODtZLyJbx9hhpn7S1ctF485Mx6rdiSCDKqfnZ7VvYdbgHOkaJnM-9CrE2uzxOoV22FeQtmEUJbXRhdewasmApgjYYN5RLJ5pRk70btsxgDrPnH7w74NERgM36I578HwgNPvUsU3Wy_a3wp5uqAya8n3str5MkE6CXcSE0OeaR73DygnV3o3Zow2a-Xc56MG_PSMYUW_AfeWYD7TJGAIe8UJ_5QEkeDtLK2BVjjUIJaRelzbBO1R-RbbBjBbPJeHS3dWhte_oyieXrTqrNEPN1Ql5f0Z7EaMRPRwkiIGJIVZSaBhyyWaD2Ooo91-R-fAF4RhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KUxNMrcf2fA0blgl1GufdbLSX7NykaMdfbU87mU472pkWtivervzxRaOoPva26Q5zqwDKh4iJHDvPPEGo5JwKrOgQJlLpRbS5m6sPHHfUwIRdsciIgQxSJ5FqpArAhkxaDNMljUyR-5ZfARtm6eU_mQyDF0tuOMfTVj9VqNzFjL7art0dbuWtF1vjtqbDEveTLWLeElKFxapUD9X6uVCaCXDDZmH9U0jp9CLr_7y-x555DaLJzLUglIDdsku1wLrId8MCtQR1lDcgz_lNkxftY_B4SPtM88nYFiajF2Uj_TwY3wJ5-_kCzdmgWMudpqAdY4Dp4dcBaBD5J4zZD-mKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4883" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=gsrk4pcJkyBGKYDx_wPJK9SHlbWVg6e6oqtvpo-fVhMPA-k1gezKMim61syLzS4kLyXqijCODDuJ2Wi3PeoZoA7IiFz0jBq5EXEF3x-2orlK6HlSf9KNCyukzP9voUXRyHpfFIRxZOrq4V5gmqGgHdaGO8pD2GwcmDRokXhPPDYiDAlWHwQmlZ7wkQJ1UyiIyEzBdU-7n8bv9_l4ImOdsUjfRYPqDo3P3Sq6_TFaHgfJKQuX7WxFmNLJe-g4WNtAaJDtoTS9cWTFsFKJTley3KZD9lsgkAlh5x1dcpH81YjHs2fXF8UFLwU5y1VIkMMeLk5AYhKvAvRIX1uXVx85aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=gsrk4pcJkyBGKYDx_wPJK9SHlbWVg6e6oqtvpo-fVhMPA-k1gezKMim61syLzS4kLyXqijCODDuJ2Wi3PeoZoA7IiFz0jBq5EXEF3x-2orlK6HlSf9KNCyukzP9voUXRyHpfFIRxZOrq4V5gmqGgHdaGO8pD2GwcmDRokXhPPDYiDAlWHwQmlZ7wkQJ1UyiIyEzBdU-7n8bv9_l4ImOdsUjfRYPqDo3P3Sq6_TFaHgfJKQuX7WxFmNLJe-g4WNtAaJDtoTS9cWTFsFKJTley3KZD9lsgkAlh5x1dcpH81YjHs2fXF8UFLwU5y1VIkMMeLk5AYhKvAvRIX1uXVx85aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/4882" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست قابلیت های هر پیام رسانی رو داره:  - چت های شخصی و ایجاد گروه ها - تنظیمات پیشرفته پنل کاربری - پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ  نصبش ساده ست و با یک کامند انجام…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4881" target="_blank">📅 13:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZethRise</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4u05SG5uGOb8vweVolj3MiIpbTZJ0zTvZR4FWl3LEYIZPVAS56EuwWXyksCQKZekf6XnDAwoGoS60U3rO0scLVRV85DF0N14VgAVJg-3FW2AfCAPcJaw6mJSh3UtjkgjveB5QZdw6yY_ngYyclSMA-vV-f_G-5vMsT9dQzFU7gKoIofUQlOVqieTvd-InWde24tztTsYKm9R8YOZLDGm5ynfMwDIH9u4SykebRhBNJOVhmmgnUugG8kInAKgD0aDh-F-rzf2CzaQD1KrHjKtnhqVbaodzccOW0jbQOY3U-GehgPqiTDfspuvQBnjhgzAWsx2uiHmEoNyYYrrv4FvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست
قابلیت های هر پیام رسانی رو داره:
- چت های شخصی و ایجاد گروه ها
- تنظیمات پیشرفته پنل کاربری
- پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ
نصبش ساده ست و با یک کامند انجام میشه:
curl -sL https://git.diastom.xyz/ZethRise/FelFelChat/-/raw/master/install.sh | bash
و سپس با کامند
felfel
در ترمینال سرور میتونید اون رو مدیریت کنید!
درحال حاضر فلفل چت ممکنه مشکلاتی در UI داشته باشه و همچنین در backend چون نسخه اولشه (v1.0) پس اگر به مشکلی برخوردید توی ریپازیتوری issue باز کنید!
👩‍💻
Git Self-Hosted Repo
📱
X Profile
🚀
Developed By
Zeth</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4880" target="_blank">📅 13:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
امروز اومدیم با یک
#آموزش
کوتاه از کلاینت/اپلیکیشن incy
🔥
داخل ویدیو به چه چیز هایی اشاره شده؟
. ایمپورت کردن کانفیگ ها
. وصل شدن اتوماتیک
. تغییر dns داخل اپلیکیشن
. تنظیمات مربوط به تست پینگ(مشکل پینگ فیک کانفیگ ها رو رفع میکنه)
. وصل شدن به پروکسی لوکال(باگ کانکتینگ تلگرام رفع میشه با این روش)
🔛
خلاصه:در قسمت dns از quad9 مقدار گفته شده استفاده کنید،تایم اوت کانفیگ رو بالای ۶ ثانیه بزارید در صورت باگ تلگرام از قسمت پروکسی استفاده کنید.
دانلود اپلیکیشن اندروید
دانلود اپلیکیشن ios
دانلود اپلیکیشن ویندوز
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r9vX8BJjFKcYPV3Q5zVIZ1NXoXG7xgElR0DTCmm4OM-g0OT2iaqrSSqVrKdDN2Y-ElAs1E77D7b4AQTja7YcymNUyUjaXnUC_-Z5NFlLi6DUHcO3kgrQDnRSixRT-4D15Vu9PtLxnP4yd5LYYqlOjexbBnLdYApvV6mHqx36tGU1RV1raSj_QcCBdWat6xiEjmWp9EoGggU5Kvp600WPZp2F4W4fYE9FyI6ZCvSOtr4xXwO3_YpqJS4sUT3t24sUtWD8veYVUJIwM19UEdG1lqLKOmc-XHBvw8nIgmDOttrorOMhIsLUJCAEfSC2WVXPqU7H4SM_cYSHyeWDLqdhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز دوم و هوشمند برای ایجنت‌های هوش مصنوعی؛ پروژه‌ی متن‌باز Synapse
🧠
حتماً دیدید هوش مصنوعی‌ها بعد از یه مدت حرفاتون رو فراموش می‌کنن یا اطلاعات قدیمی و جدید رو با هم قاطی می‌کنن. پروژه متن‌باز سیناپس، مثل یه سیستم‌عامل حافظه‌ی طولانی‌مدت عمل می‌کنه که روی دیتابیس محلی SQLite سیستم خودتون بالا میاد. این ابزار فکت‌های مکالمات شما رو استخراج می‌کنه و فکت‌های متغیر (مثل شغل یا محل زندگی) رو به شناسه‌های مشخص وصل می‌کنه تا با تغییر اون‌ها، مقادیر جدید بدون قاطی کردن جایگزین قبلی‌ها بشن. سیناپس اطلاعات قدیمی رو کمرنگ می‌کنه، تداخل‌ها رو رفع می‌کنه و به صورت خودکار مانع ذخیره پسوردها و توکن‌ها می‌شه
👍
این پروژه به صورت سرور MCP ارائه شده؛ یعنی می‌تونید اون رو مستقیم به ابزارهایی مثل Claude Code، ادیتور Zed یا Cursor وصل کنید تا یه حافظه واقعی و تحت کنترل خودتون داشته باشید. سیستم بازیابی حافظه‌ی ساینپس ترکیبی از سرچ معنایی، متنی و فاکتورهای زمانیه که همراه با هر حافظه، یه شاخص میزان اعتماد (Trust Qualifier) هم به ایجنت می‌ده تا بدونه اون فکت چقدر معتبره.
که به نظرم یکی از مهمترین قابلیت‌هاش هست.
با سیناپس، ایجنت هوش مصنوعی شما به مرور زمان با بازخوردهاتون هوشمندتر می‌شه و تمام داده‌ها هم کاملاً آفلاین دست خودتون باقی می‌مونه
✌️
🔗
لینک ریپوزیتوری پروژه:
https://github.com/Danialsamadi/synapse
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8wgwOd_nyeVCpDdqhX5gTHv_CitJqDOUxwRbz4tUSJGq2iTwqZTVNBI9phpYAfF5PdqFundLB-oxTlJaLDYNa9c5cziQ7fSRM6xXVqVL1dLQRj3COGR4HvDJlm0sKR5K8ig3t_ERMRma2jfCGnThzy3xOQ6R4ReOdPm6o5fiotyXmsyKKJr1rUzpGy3rPOKegUSE0omEB93qR3pcDwLmcQVm5lC9WSqKdOMVfE8q7GpZb4Iq_g8UknE0N7HuXtXHLuXuo91aHpYQGgpQisgWLGJzBIckANXWvmkRKQWUocxMWCKZtSI1DqsCs9b79RhoxVHQn-17mLP0gQrSFTPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J2AMGwFDP0YNdaQ209MB2rdVuGvm-3vUEny6y_SDO64-DPol8CHh1UIjR7OkX4ZHa5p-zeRTGDbUZQlYApDiyu50aSAM-5Yz9QVL8RJMXvunDenlgh-i2umA8QwlKWheyBHqbs6mAmrzeteeBCXfgQhjXhNXhrBVLnw1TLKPEXvZAyFDAsHY8a5g1BYHSvSNxGENTHQNif2V7h30MioQefdjhi_8z2Xg-m-2CBRuTZ1Uy02DEaWgBpkmy4JWVy2k8EBwH9338Z2DHDtzO2ySeyaJ8_aSCB3uvuemsUMzclbpTCGrPcGeayN-d-HGFoeLWSQbwATWyC12YHocLrm8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bnJy0HxWGBFxuTKBtzfTUSlk418BvDIlh30u7rIS3DC199NVwn4wDUf9WAs9d4Wfi5gA2CJmqi5oBKCZ34OS51mSVQSxbnjUZmEebu2aQmquqsYGC3oB-BSfiiuFQu8X54odXvqcY25xWJ3avG1sL5gPQ9SIi9hZlYbdQoktWHs2MPCjaxCIHZxZgPC1RoSlGE93uQpne8qAZFazA9G_D6PbSh6UnjbuipeAuuQzW44v37ilNahsT_bfpLqnu2xsNWv_ur32eT9LFISAYDUPlMikQlHimfOz3IkDEhT3qYPAGngkgI5g0NaJcmfuOoAGX7_VeJDbfIRXjAmDO1cmYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دسترسی رایگان 14 روزه به تمام مدل های zed code
ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده!
​مراحل دریافت: وارد سایت بشید تیک Free trial پلن پرو رو بزنید
zed.dev/pricing
با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
✍️
CypherDeveloper</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a7QBQsa-tMhTL7jqRVRL6nun6p_owizm2rF1DtO5Qp3NVbnDNFihJinfDHPSqXT2FxbbN5GJfVQpda_CnuHJSfvaW8XuMLSEA0gIwBqzCS1Tp1DZ759ckfNVYEXyyFGNI1t8Sf0CDE5Wo0jqp_jnLhQgiccXbvD-phtEM3-x-pacMYbctte-s2zs7jfRnzBVagWocbPNb75M-NUlmpdizSDIpvBrA2z28TD36RvkJQqQ9QPDA3PJKjx3wfkT7TcpJ84gy4sQRVwoBi8FVJAtIdicPVin3osxo3Mu5xCltmQdHwx94nOFpFKuq6lQsHYQf_U8qAhDMv2g3DeXfONsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=fDyp0VYXRBAvMSkfybOT5pqtqG0Yjg5MZwE6-Og7WnCOtpwJiA8Nvgoxu-_OX1m2rk9vi_5TpUYqfqMmDAfuMaKFtVEsQID0OULKJZzswWdKCHAOSJUi77fAHGcq_dIlZFIAtFLO9ENlNwJrid4x1DJVjlJmgC-QgHQkjmXwpp6TwzTUN3QLBx-IsAezT7EFyF1L5_0_OsZPmE0kIf8HMeCHonsuJ9emIFsY7I3Gy2DJfPdeZpHSFUeePZqh1urWTOp6lxTv3rPPSIcL-yvzBP2mJaHBBAVIF55MTpdjFMMzpnH9BXjKZ7Z4LG8ucyJFNmuHyrsYmKcv__LBVmrqjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=fDyp0VYXRBAvMSkfybOT5pqtqG0Yjg5MZwE6-Og7WnCOtpwJiA8Nvgoxu-_OX1m2rk9vi_5TpUYqfqMmDAfuMaKFtVEsQID0OULKJZzswWdKCHAOSJUi77fAHGcq_dIlZFIAtFLO9ENlNwJrid4x1DJVjlJmgC-QgHQkjmXwpp6TwzTUN3QLBx-IsAezT7EFyF1L5_0_OsZPmE0kIf8HMeCHonsuJ9emIFsY7I3Gy2DJfPdeZpHSFUeePZqh1urWTOp6lxTv3rPPSIcL-yvzBP2mJaHBBAVIF55MTpdjFMMzpnH9BXjKZ7Z4LG8ucyJFNmuHyrsYmKcv__LBVmrqjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=djUg1GvtQPNLqmaTPk_8A-cPMd6AKjvmdmPN2usSxqvO-wu4NGo59iu1AkUCG7nXa5dpzPaBV6gG2gAiVubhb0tjbAZgK-UUytysI8W6qrby5LdU7Pn1WKoJGjhD98ojb1Avay47kXJ9pXzC0IDG0uBv4L3kcKoIO1tsbST0yVHqhrf1f4SfjIjkUjrORZx_P3oL4kZ87I437lsEm-WchgBFPUWBMV6Q59OliWyuCzGHxPQrjMLbIBvGwfP5VZm-wL3Biyv6uz1O4VmbRXPbz9UkrljPhbFPlfeKi17kg0YNZfc7tmtyHfHmgG2-nAbfANJfd9wZK4Y2YmL7BFjDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=djUg1GvtQPNLqmaTPk_8A-cPMd6AKjvmdmPN2usSxqvO-wu4NGo59iu1AkUCG7nXa5dpzPaBV6gG2gAiVubhb0tjbAZgK-UUytysI8W6qrby5LdU7Pn1WKoJGjhD98ojb1Avay47kXJ9pXzC0IDG0uBv4L3kcKoIO1tsbST0yVHqhrf1f4SfjIjkUjrORZx_P3oL4kZ87I437lsEm-WchgBFPUWBMV6Q59OliWyuCzGHxPQrjMLbIBvGwfP5VZm-wL3Biyv6uz1O4VmbRXPbz9UkrljPhbFPlfeKi17kg0YNZfc7tmtyHfHmgG2-nAbfANJfd9wZK4Y2YmL7BFjDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JJL0f6P2kC7TSgDsEmMqMO9OaQWiunE7hAS8TXtI7bv6w8pn8yEndBX_0ebcIqtYwiFYIYdceUw9TXZqUXMCoA3NoI7rzLHZl7W6SBz5VBhjb5O6QGjlUyfw8OrChaijvBr9bTBqBQtrxtv9u33S6YWlAukrDlR2WTtgxZtubFqCVpBV3NhawIJE0htDxby1_Zn5hfJLg7zIIOa_AVBYJCyblo4gLjozAHkr9dZ68p7Jg3itLA1B8qKia4E7_Qa-UUJeGZ4CKoPRHvlvxVV_VjAZFnwce5e2FfjzZvCCa51m-W7btQU-Mv5q9_5iLQUI5dULo-kfi7-XWGsoefpfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aljNu93Xs8yUnh_BsfxXG76lR3BSaEDv4EJvUzwG7X9JG8DFXqOxzsf0ugxNS3-fP_VJPfPx1cDFTFzTy9C2cc-3tr2wEWGW_EiZbjd0MEJb6NTdzwYoiQXfzflaN8uuuxS8FfUHTzhfzV-MNL9beq9arSCftLU5aX-FijMZm40_sGP6AzY45hDNUZ0s2ngrR5wCuqB_J1hPiY1iwQMPXway-H2s2gH4uRIMWF5c0O5NKX2O0JIUhgN7zzPsBro6lnCUL6CEuQXluiFyW5VlfEXz8oR2Mt9wpspJXh_AviVT5WMlEYIBpC5HR1O6u0Ex6WKBdo_1P6RcAHXn67EtJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fwxY8tKXNpRR3DhGiHmdnzMzq0EU3CxZaq3MaWhICT6tQaho9lXcsxYbmw88lzB58yq5DkUi08cTDWqWjTVnNPrxwD8FMbM-ro_nSmLE0iIgHVN0Qc2WA8dScfSGtaI1OcRmWnITnI28nl8IB9XUb4dFdMlZUAPDoNC_sjG9kesxnHvvbbkN5qD9jYIIlTEb9X3Puo_RyW6HWr1w8o-sJgJeDo4l8Qie524HJc4ZS3gGQUL6ASaYu_ppEbcB6LjxmE_HI6sx3ZWpCB4V_2wOuiM_TsRXBxdIutdv4fzHY9Or6tqcdAJ0TV42lWANn1gaNV-t--wcG4bk3yz81Qechw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q15dWA08JfE-WTOdPXrkfk1lnClW4hwT35yl7sEqsHP473qeawPbv35tsMTFQV3ooBrDb6g4s89AKWk8bXRGaJWhFp-yuxV3NOCUN7oU-Btl1x4LGg8FmUim0suF2EdX1wpy39x5n7cFLJOHMh4EWkGqASezEdcut-5wHGFqNTyH6hZsozfeXbowZyZ7p1C6EW5z9Nsv5yfBIzjI8eKyMEcQe11oacPYEcKSkAvzpbj889GbNuo8dE019XHT1AqjfKzVIfqZxt2wwwyEfHM4QMPNMIL7H3ci2dEyekmNDRks2bwb3PXnEHizcsxpnlkGt2kC96VnYYXffVGWAwC08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ Hermes، ایجنتِ دوست‌داشتنی ما، نسخه v0.20.0 منتشر شد!
📊
این نسخه که بهش "The Herald Release" می‌گن، کلی قابلیت باحال مثل ارتباط صوتی زنده، سرچ با منبع معتبر، وب‌هووک، اتصال ایجنت به ایجنت و بهبودهای شدید پرفورمنسی داره
🩰
تغییرات و ویژگی‌های اصلی این آپدیت:
1- گفتگوی صوتی زنده (Talk to Hermes): پشتیبانی از استریم صوتی زنده با قابلیت قطع کردن حرف ایجنت (Interruption) و کلیدواژه‌ای که باهاش بیدار میشه (Wake-phrase).
🎙
2- منابع و استنادات دقیق (Cited sources): توی کارهای پژوهشی تمام ادعاها رو با منابع واقعی و مستندات و سیستم راستی‌آزمایی (Fact-check) لینک می‌کنه.
📚
3- وب‌هووک‌های خروجی (Outbound webhooks): فرستادن اطلاعات و رویدادهای چرخه‌ی حیات ایجنت به HTTP Endpoint‌های خودتون به صورت امضا شده و امن.
🔗
4- ارتباط ایجنت به ایجنت (Agent to agent): پشتیبانی از پلاگین R2A v1.0 برای شناسایی و واگذاری کارها بین ایجنت‌های مختلف.
🤖
5- سرعت به‌شدت بالاتر (Faster everywhere): سرعت لود اولین توکن (First-token) تا ۸۰٪ کاهش پیدا کرده و پرفورمنس اپ دسکتاپ به ۶۰ فریم رسیده.
⚡️
6- پلتفرم دسکتاپ: قابلیت پیش‌نمایش زنده آرتیفکت‌ها، کیت توسعه پلاگین (Plugin SDK) به همراه تسک‌بورد Kanban و پنجره دسترسی سریع به دسکتاپ اضافه شدن.
💻
7- تاییدهای هوشمند (Smart approvals): پیشنهاد تایید دستورات ترمینال بر اساس تاریخچه استفاده و قطع‌کننده هوشمند برای لوپ‌های ریجکت شدن متوالی.
🛡
8- قدرت‌نمایی در CLI: اضافه شدن ابزارهای اسکن پروژه، مهاجرت ساده و اجرای مستقیم کدهای شل.
🛠
9- هدایت بهتر ایجنت وسط اجرای کار: قابلیت اصلاح مسیر و دادن دستور به ایجنت وسط کار بدون اینکه پیشرفت قبلیش خراب بشه. نسخه‌ی قدرتمندتر Steer که داشتیمش
🧭
10- ابزارهای خودترمیم: توانایی خواندن خروجی‌های نصفه‌کاره ترمینال، تشخیص خودکار خطاها و بالا رفتن محدودیت تعداد تلاش‌ها.
🧹
11- اتصالات جدید: هماهنگی کامل با پلتفرم‌ها و مدل‌های خفن جدید مثل Buzz, GPT-5.6, Claude Opus 5, Gemini 3.1 Pro, Grok-4.5 و  Vercel AI Gateway و رفع باگ‌هایی که داشتن
12- قابلیت‌های جانبی: پسورد Vault داخلی، فشرده‌سازی خودکار سشن‌ها، لوکال عربی، فایروال و مقاوم‌سازی امنیتی روی ویندوز اضافه شدن
🌐
این دستور رو توی ترمینال بزنید، آپدیت میشه:
hermes update
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jewECt9rXPA5dM3e9z1u6ijJ_n72Uh7VscHhxZSoRFA3y8EWymiGcye6MJqhKsbjXZ08bm1o08_Tl5x26wWAY7HvTrVEzpZMNEW0Q0jJSmfBytRGVN4nxIgLGM6HSij4oqfLE47H6PTwDpO2yf70BD3cRzQELnRg6H-6ZlRAWgQSDRJUidfPfiRC-JDNKcLlfpscOOfQVq0aHVRQUHLISy1TCm37DsfrFA6TSvD3FyZcXwQ4PuKLq7iLxyzFNr2KNYTBTKb9WVS3dkUFeSma37yBybsdsZnlu0ZTRJCjU4Z-xkGOOw05XybSsz_waqYRWzNztsSTa-Xxj134Bvazlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YOy-dC8qDsB6_ko-6cPRrKzlQksYSBjGG96IFqcWCoiG4n0TWPuc7MsRrcyx4Wq-dqH7swAUVAxUgxz-pVZnIxlLvT2x2UQk1UMIletKMdXDzqgNv0QhnZ6I45CHbFkatmv5zCgTL4SAQLal6qQBnj9UN9m0zk6OG6el5GuxtXi7wxhFite1sxifpYm0vz6mfaa2NUqFELF7c__BjMxriAsPyMqXwc5mOORvGVF5lki3bV-0GoeArbi6V-92G41_7hw_DaypSlYlz5pbZoOcGmmBCPLzr-5AHMALiIrWHR4vWNw647Xo_qBEud9iUgUALvuC62QDDwxKHVJvf4Hqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Iv9nqaWfqG2MdsNj0oJX7ry4enNbMc5s_8o84PPGrEsZh_w3t8GPDtuBk6KuOxKpWgJA3xCtVfYrckEXFj_KM9Q3Cvbr6uTy_aPoFAdqNi-AugBbXPyKQLG-7KwdRNm1bk_dU4HMHadkV0UiNYGL5v6_cD_Us7LbuJ4lD8g2Rl5spOFoxtUVZoVecSwG8BcUthrSR5sJikUDwL-zIZhHgcXnyGCO76uRC2-30Adz17e-y_wH_3MDrsVy0_cU7P2Nz6NoHPbwMkTR9IwYYlTFbVnjVjTOchVHSetIiuBFXm34JvFGL6eQLOVY4JUgu7QMt3sARg8eqLyStD8QcnUkbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KE9izoglOH631b0b4sS3Cm8hhu8Eloo6Nr1XcERS7Ix7l6NBnd-6K6kvL8ik-Aqy2WWizKIQDLSutTo2dEEgkGrIBdfg5-SCXcUlXv2AXAy7JfYudGYcumhtN43RLJ-62WaJ7HuBug56LRE-_XlMEyRVSWQBxpvc8NQnYb_CykNP0z87DT6KlsfKaBXaQsDZTVN6_toz_K5f5AGF9BMxV_MotXWFRbJRixgCh4jQ8pEDle8-0aGClZg2eEqFNy2r_PNTssKy5JQH_zw93883xig64ezA8ae_50NVElbseI0gOKsHfB7JotJ5_SggEJjvU-680_AslwqjXVwMqorCpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mC03Jf0hWvEp6diCU8qelC-vS4JM5_ODni8IwCshNJtRqzk0h0OPvEB2qbbe2GhsQ9wY2ub5c-ex3doffOup0YD0ujhNRCJXyWJpfy9kGbf1fnuQfuzR4HLP8uae4CoVkpdVOijCyUrOqVbv706XWNsimdsivnHSnn7uKhQJH05I6vuhmngvFndC8e9U3bX_Tj0Old7fmYcYQF8wIdgFHJY_mBDouflgAQvqZXOpe5Nde0YtXscBg7xCzJ-l5IwNTEzBkR6BJp2ML-twE2_iZLvfNdq8R6czYBP4bD2TLflqOvyxilJ5-lI-VbQlQvoZODLvX3vqfURKVeDXsyj1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SQOAOqI1OAvXcWA6l5WLimvYde0-Qa159AwSuuKIeeZfMnBxg8UL3fDY_z1wqSCOwEz5x9NTMoAtlyXfx6aLB9Uo7mclsAe5Zsg_0IIsafP4UyZ4tpCsWw_qV4l-5xg04lxQK-5pRhlFXvLtCmbqeCCM_4LbWKuOhlWdx05BMxEmiCOfh_AvgYK1vkWWCeUAgYAISRyX2UosVe_vJXIzH8w5ype14sdngbcL5FhXOhrTdGZflQYJ4mKrtp89stNPvwyLuqHzlM8rUFN4P7Qb2c1ME-tIa7JQqruonrwpfNY3PYYAjazI9uGA6A3nZOEczYWoUaMTSR5MiYzG6BjWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNaCibDqUSMJUfPeEN6L250xKYxrckFZ-C5Z5Ei1jQ5_5qADNH1YGycWfexFqGa54pym2ZoiQ8YZA0LV9RRkqPxkcsULF4IsCVY1LA2X0SZ_8NRmwaELKTXlUEEwcb8QP7ho3Fe9s2SYCZl1fD1CISX4KIG3dB_CsVw8Eb-pRZ2bmcQ3MMHa97DCZ3y_Kj-7dFGPLmuBRrewz0be-VUwBp3Q_hofZobafxO3uBa5S0c9qorsF0dKJhp2MUuAQpM7PnoQe7VAwLciqI_DZIHvu1a6rw_HG26H3NtKkjpYD-H2bXC8H1E5lzdMSF_GBdlhH6Ba3zJZRS8XQFpNnJFVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eLb02D1fuwMFt45_SMJVapYSSvs8iBi4OoPtwaj0TUCgpTjSvYpRzIyxf_J8NkeQ6nRp3u0KnE3sQ-mznURa_vjyzmJDZoPpdQkOTinSvG7Y53H0pE0ff1rCH8ExAvn5_7M2Fazu15Sr53nujjfd6YDtaT1sUvDnHYq_fVKFShRegGq01UTfLHTFuwh9ZkUHu2xc5FE-KSSRf385gp9Km5pdOwOjOP-50k15z_8BErNvof5GiHJkfixEqVoIcsOV1i03I1TN2l8xEC8Tl6PXfdcjyiU_t9iGDgyr8Z0pFTBVguAYiwK2LPJ17Ow6V8nsMYZP2bA7aKR2gtuopU63YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p3wvv7EOb2TVyroXP-MXeJQ8WjVPLiRs_OZatu_mE1bLZqboh7SiE4GdW3crF2QGryszmMS1W-qQUmatCNcKkECUoLaKIwNbmfPWb0sUvJ7LtJJWYdDgXh69ZKdRlObWutAKn3jS6LKcry8V05rUSQzCNcJsgyraBb0lpOlROhcg1sJJPGX7hsbNxRiZy9UhysjpJgnqW_U3typ4ryqCzm1uhSblxUacOJNVtkUXUbYG__9GE9CSZk4iAJle98e3TSqN_csz9buJGbY5QPK-cAP9PBDdjF2g3ZiYUR8MsNRpR1HCAQcmi70qaVlVthAfUFOmozLb4ElkbFmAtL4-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k-fq_pvQnSRmOsypwZiQfND1q4HWS2ri7wKeqmAF645AuExr0hs8arhk7KTskRvCu1kg_iwv9rxDoFqq9una2oEXV1xtsZ3HhNy8I3I2Zs91S9Fvnq0gdcBlXykaBlHeLfEBg7f346O4EI8PRtqBa7lKBc5_OBC08yYzlBfBjVbcfFZTBZEvDHTo679l9z01uwrTnJjwuAJURPFN4uNWJnv1XH2iXvT8i0AOtAL8ewBK9BceHO-eaUW6vdw62koIaxcEy40-dwx2Bzarmki3Dd8fpIBby1-hDpxn9ppKpGaUwA7Wg_sb7esNdz58MP2MN3evAsbJeNFKlGfYIU_Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tQoKuvVrUYPUnL2evMMMHnHhpjwiKX0g_RwWQ8fLx0_7yhZM2WjRLvf7ZapxXQ-thBObcg5Zr7kP00FR133dnNt94aLal8t0eCKf2PTG_OhREGQtzPdHLJRxPc2gH-gaUYEbAalcNQuvm51SgYrYAzyG6qsRs7Ud8QI-AJRilFwGozlkAEoYY_9g0QjA6USq6wNc1kAqaswUD8anPtsoNCnVcxWntsPesrOg9Ge8lx5a74rKyxDZp0V8IraFV3-T4ikl9HPLq8Ah8MK6_xFnEouJFEVZHzNRXi8Q1vLBS_l--BXAu5p-EVp97UW0N29EA_CQ9SN5Sfato_0GCDXEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/doBJBhY2UhwJPbjklyhZPpQSRQd5seJa7054qpauRlLsewc6_hxU6RRg29FaaPnZlhogB6cnYn8j5wg5qIj8VDbEj2SASETIhTsVIN15YOL0Yk_A2UXvTfvnw07qkMOCOhxRVk4CkpIH4UA1jTIOuttOYzVE-0oW8yNsp-5TlswDH3qzMB-0JBDPtzBTMlXVQPzf7inqIDok7z4jX9F0E2IGDeqC1BA4DeCMsMrKTKsopE53zYvv9MN35Bw7jZiWq-3AH4dINXAv_9tA5wtzLGz-J1sFTxQNTZBuoZEXGcWiT6rQlUr63dKlBp7l37iUo6ZoFK6uxApdIUTGi8-BsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uKVCp65WyfO8LrDzvT61fL5Vh07M1V5mmRT5oi8gECiZ0Q9rqU_Rn_GbnflELyAWYqWZo2p5DHmYuEJFH36z8ORpg_Gai5Mii-p5_KJXYanviHYdqxAa0j5a4XPtY9tXlUkL_lD0OEcj-e__uD30bbnytzGtAoEqhmmxUe6J0OwxLe1w-H6PI8BXZpcu_rVNbfKomf3rY7-oRDiStG7hOBWjWttTUt-wyokAilasnwL19R8JQlUzNctnfmDYQbvo7KZeH6toukypOJQq2imKVQirKB7ouTAHoxlShoDoQmmw9XWfRJA2lPW1ftxCPj-MwU4V4jnArjuFnvW8ul_fgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FMiQkAVF6sYe0DFPX3zEvWnAa0zGZqN1ngNCTrOguVo1YKSHZpq_GTMU3MDWgn4ZgU0prOVbhom_7vAdkoDUkkeaLUwArsz64CNaArpq4XeMzNFd4W_Jkskm5SmPHSsfzgOxyswHwWfzWRaz-2btjf8rYPR8sHmyKaVi_lzMPW4SSYsCA8U9yyAjyWxYkxG-SC4xf8304e9xxjXU9lsHV_t7dN9PDSLX7dx-FRMyHleFdX_3eMCvOl7o-GLo30lFG-uTyJ0fS-4WiVnGXsSgSIWla50he9A0v7kVfZfI9QQUbDC9QS72W_6IlY7G2EUaj-x8YUYtL5p9n3-njGy_aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k_KktjmGN3CxuxytiRl_Ls11gFixHG4HlBWXr5-MmvKsXdl85YsDLnWpaDa7G18Fzbhg2lqqKZSBINVIXcRkWJ5Gl0ZP8TLRS-kzX8-vTgRPrQ7PRa7kbB-nNMTu5yN7ecyHTfPm2e0FlyfARdqJkLIDeFXSd4kEevBc3uoWUDr7XxII42gv3QXv0ddWM5sf6cbeh0cpJ1iit3Oxd0Bph13tpnc6YWBHdDWyRZK8xQggME6U7X7jDIVC87PBq7ci0mCsrahA6ezg0Z4ZpIqeWd8SlYf-9mSuAQDUuzc5ZVCANVtuLtFyjxNlkl1o0YKWB0oYQmWsWfwqJbl9nP4UjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPavel Durov(Pavel Durov)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg5uKtdKLU_Gv-slR1-_a-phxIBaqhztD2AM8uNbxOaMox5BTZEcxy536iQVloiTYqOeR_P9zbcf7MpyDGmdTpgNSNCa2e5U4SEbUMzsrFqIPE8qRcY1UC9TfBOdsfh1UtGOAQyXPHROcwQfrxHhG7JByTGd4R2fwy4F2Ng2x-0_zcxccSs2JnYFGM8OAU6Kbat2_kbaxlV7IqbAQpcy9Rw6_J1faOW1MufUXHirdQIb59ArpFHn1s2NHbHuwS_l2m6FejQGYthUcm-G1edHGK3cGRborGgy8qrUKpSKePNhLdatDpyo-bQ3pyS6BuMNvMQnR2OkSNZoA6iPfNfo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
The 2026 International Olympiad in
Artificial Intelligence
starts today.
As a token of support for those who will reinvent our civilization, we'll issue
🏆
240
exclusive
Intelligence Cups
to the winners.
💵
We guarantee minimum buyback prices ($
1,000
per
Gold Cup
, etc.), but the cups' limited supply may make them worth much more on the secondary market.
Good luck, AI coders!
🍀</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pluwx93eEt1PZqy4iidGXRNPwC_p8PgSZSkGc-F2AOVxQ-1IZw5hNDXk-oRQ8SIfQJmGBzRC9RN7TmYJ0La2nC8N5a4RgxjAXMI-ozZGtAS1cqkDCPL23jcCAYTn3Mm2HWWe4BgAVPn3g-Yg2gnJ9d0dmJyf7jvxTvosl6Lf7g9JcpER5R1G7-XjG_xZ2QTaR8eQbUjCNbiaEjk8ikKbK6cuaIT44mo2rJzOIwhoOjphVnDgGyMqIqyV60aIddJBFnMhc1CB1I4qArp8Rgl03POHCIafsqFXxKHlLl4clAkCNFMHUElzkthFDBL-XwZ7Vd9SAnRqb7qgRdl4gtH3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی گوشی VPN دارید، دیگر لازم نیست برای لپ‌تاپ هم VPN جداگانه تهیه یا تنظیم کنید.
ریپو
Relay
یک ابزاریه که با اسکن یک QR Code، اینترنت گوشی به همراه VPN فعال روی آن را به‌سرعت روی ویندوز به اشتراک می‌گذارد.
اگر زیاد بین گوشی و لپ‌تاپ جابه‌جا می‌شوید یا نمی‌خواهید روی ویندوز VPN جداگانه تنظیم کنید، این پروژه می‌تواند گزینه‌ی کاربردی‌ باشد.
https://github.com/Mahdi-mortazavi/relay
⁠
@RepoFA</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hRKlVMuI52xYb50vcJGSzwC9OD64Va_aVg3yGMUnlpsLPrrQmilbLoAHqhkq-mtsq2kw2cdDaapaDsoc5gYU7t3SMV8U1vg98K3wFgDiM78dlUmByl34e5yAj8BOmUCYUt_-adI6s4FXA0SzO4_mmDLFUURunTPizivILGLmJHFZnP3W_BZqMfk3DX_END6N917ZEZwkQX267N842CJ1qtOZCbsRUD51P1vztzdtzVLKmIBeO8T2q1V-3N_3qvFCH979uqY3q3zdvXid9j4hxbBcfosayvsy4Em5ygICZ1lG1R32hHEGbNSghoYM_0fM3N8WJ7MA85jRwkvlfuzvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=mAHrfRxs2qW1dyUlIwEqBOd2D4oVBk85GyU6FB_HxJ_3rOd5hQCx9XwY6o72gCRQffFBgmQpfrIixNmIefpVfM0sDCDEs8OkDMmiMCDtOhJ55cCDB2UTRfZzATTWkwO4dMsgAqNvtgTKjxwcGEeSjlDHzm2FVS2nSC0vqaorhXf1HTw9D6vnCPi9DJbpEKfUU1aGKmUtbJv4mNwiZxFMdG6VqUa_mJCJZWVUutshWbgl7Z201I-bP7MWil2a6W2qKzGOGZw08G7pkZ0hJEmlDChse2yA24NumVrx5b7NfpzLjoXkSK_3F1GFARzE4rFTr_S1BBp3hvIou5jdLdkwwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=mAHrfRxs2qW1dyUlIwEqBOd2D4oVBk85GyU6FB_HxJ_3rOd5hQCx9XwY6o72gCRQffFBgmQpfrIixNmIefpVfM0sDCDEs8OkDMmiMCDtOhJ55cCDB2UTRfZzATTWkwO4dMsgAqNvtgTKjxwcGEeSjlDHzm2FVS2nSC0vqaorhXf1HTw9D6vnCPi9DJbpEKfUU1aGKmUtbJv4mNwiZxFMdG6VqUa_mJCJZWVUutshWbgl7Z201I-bP7MWil2a6W2qKzGOGZw08G7pkZ0hJEmlDChse2yA24NumVrx5b7NfpzLjoXkSK_3F1GFARzE4rFTr_S1BBp3hvIou5jdLdkwwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش
سا
خت کانفیگ Amnezia VPN(وارپ)
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
💡
نکته:روی تمام اپراتور ها متصله هست.
لینک ابزار(ساخت کانفیگ):
👇
https://darknessshade.github.io/Amnezia-VPN-Config/
دانلود اپلیکیشن ios
دانلود اپلیکیشن اندروید
@xsfilterrnet
👑
@ConfigWireguard
✅</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EZJ_4WFAeZpvWrRRHkSsoKU4plJcviJdvrVr-M98Hvnn3PSMiaN1t_ymQasxxMIMwU9WYwQ5JG1kfpq-z1D3uW3BDlS44-jl6PWQSmGfhI3mMeixb8enxzSvRHg-WdzdTewx-qQtMFLZBljqYfT99Gysa8jbbhWc0Nh8M9uFIwsqzNGf_piH3siAWe2dyqfc2X_1KuEcseOeD8eqo9YcmggUg9dQgSeJs9yHJvYvkhK4SMnjaHcjXlAyGvNTmTvE3mGg9aIrIZvdfEcbTeMP2PDJ9UP_JHB6TtHpx8KGBSqIruqxXN8_YcyZMIlq-bqOOWuD_xVOVX5aju-324Z8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hs4zWPWVl1ksKN9kj48IMvQeBf0bWjMVF2GoBei2l2ZgoMKNYi_ML97g1JbQAwCAbjhp3mwPjOiXaCPcd4iSM8n3fvjpT2IfBOIvxB6FWP0OMtl2RBtjU10EcMDezi_UPfDiW1Uq5xQVRA_WgiI69nZ84vydkuXhii0EB_aAmX5Ry6PSOxjqgP8wZbQaBl2ztLM6wCyKcrsH8O3ufidrZ7RusxeO5s9Py4WRaSZ14MzwuE4-Iirp5oOkksfb9RqSLVRzx_3KPWUCtHe2SUow6916ZTwN6y0TPWcfZnSwGEGQqPp9OfaHZ9YOcUI88X-zuncSJtQqI953RdgAf3RiuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)
بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.
مهم‌ترین تغییرات:
🖥
یک GUI کامل دسکتاپ برای Windows، Linux و macOS
📱
اندروید از نو بازطراحی شده؛ Kotlin + Jetpack Compose + Material 3، پشتیبانی از اندروید 7 به بالا، APK جدا برای ARM64/ARM32/Universal
⚡️
دیگه لازم نیست منتظر پایان اسکن بمونید — هر وقت IP سبز کافی پیدا شد، متوقفش کنید و فقط از همون‌ها تست سرعت بگیرید!
📋
امکان کپی نتایج (همه IPهای سبز، ۲۰ تای برتر یا یک endpoint خاص) حتی وقتی اسکن هنوز در حال اجراست
🔎
اسکن همسایه (Neighbor Scan) دیگه اختیاریه و به‌صورت پیش‌فرض خاموشه
🌐
تشخیص ISP و ASN چندمرحله‌ای با چند منبع (Cloudflare، IPWhois، IPinfo، Team Cymru + دیتابیس داخلی رنج‌های ایران)
🛡
اعتبارسنجی واقعی کانفیگ‌ها با هسته Xray؛ پشتیبانی از VLESS، Trojan و VMess
📦
خروجی مستقیم به IP:Port خام، Share URL، Base64 Subscription، Sing-box JSON و Clash YAML
🧠
موتور اسکن بهتر: الگوریتم weighted-random برای رنج‌های Cloudflare، جلوگیری از IP تکراری، پشتیبانی چندپورتی، خواندن ورودی از IP/CSV/CIDR
جزئیات کامل و دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
