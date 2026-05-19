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
<img src="https://cdn4.telesco.pe/file/k1ZK-KXDRipi8sWQmzXa8XxorNQYEaCNYx8dsH2qpFg4F0iQebO0xPzW35ZqghGNzA2iN5mZxej1U49W4ZiehDwvavC_CVVPLPrbLwNXf9uMprZL2ePFWffAd7rM2CQUaYOVKq3PQcACTO8gnWrI382lJBsc-cYMXmiqE3Et_DU0yai5o4_5I4WATwBRf9_cueXKpeyb6Sz9kGegYmHGcKvVkGYn48Ea21vpVzPBUCfG2E8jyvo1FhfW64owmJq6BfBICNLbZFLZPs8MVVo3SC3w1jFZ-NPSV15niQQDfOte1CeJNY8FphE5dVN4VsNRZGljquIeOKXAGU_7GSz2Yw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 154K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 01:23:00</div>
<hr>

<div class="tg-post" id="msg-75397">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAmTVdQGphnnaGdScDhbBqvQ_VikEwAfqTxP0qhMwCnb_SLZIl9a70_48sgU8oxPqxFllpsEwTz14lA7IXbnTxZxgVGyP6UdOWqKIzXEqQBCcEwnJ4AvxrkKKD-kFy4Dl2NNlmXMDgNm2lzH-pbUrDl25XFGpBOZaPINbUtVGTk3P2hFCVaoClI4hRBdsXHSYDU2xL-A-XtLOKoR6fzYlqEtak0zEvP_elGAUSDGG95F9omhefdPq9fm2xsvHKIYtb_drsmOitmZcWW4kvkh937WDJ1JHk590yLO7tLUs1_I-4-ETtAOnCeQTiwIXuFu2Quq-sFbmiZ2lHL-QhB_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز:
فیفا قصد دارد بار دیگر ورود پرچم شیر و خورشید و پوشاک مرتبط با آن را به استادیوم‌های جام جهانی در مسابقات ۲۰۲۶ ممنوع کند.
این پرچم همچنین در جام جهانی قطر ۲۰۲۲ محدود شده بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 685 · <a href="https://t.me/funhiphop/75397" target="_blank">📅 01:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlIan87fFvD_DvNgqzLON99XC1T5Hxi34ZDlFshGxWtZBZMvcC2ubXong-4aCSg9zPTLdtuZQrrdebE0eG-y6-10OAPCjy0NJglLTzPJvSf262Vg3jtwwqm-TnrryDMu2CRdNHXTozsh2z0M2cjcog6qfYjP3clAwGuNC20UALRjj5oXxwv1l49AacWChU4q8onttsoWDi_Mlh_Slo7ZjqNeLO5oFduQPZGMqyaJwFdRz3HDhEMur9sVeQuHdUyhYUejoGX0WDJgZm3UgB4n9V-yOn9ID3N_LIB3PJAWOeS-HOdMQyMJSUbhiz5rqwRuPeKUYAsquSNX1NAK7B_sxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور عراقچی:
ماه‌ها پس از آغاز جنگ علیه ایران، کنگره آمریکا به نابودی ده‌ها فروند هواپیما به ارزش میلیاردها دلار اذعان کرد.
اکنون به‌طور رسمی تأیید شده است که نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه F-35 را سرنگون کردند. (به اجدادم قسم اون f15-E بود)
با درس‌هایی که آموخته‌ایم و دانشی که به‌دست آورده‌ایم، مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های بسیار بیشتری همراه خواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/funhiphop/75396" target="_blank">📅 00:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp33TtOg-kO8d8JoaDS-LToGZ8b5UsbHamSdKiX3-4ITeKjuum1nExq7rqLj99UcLx5Ibolz3_4uSi8IBKmSjrRX1THo6SqqYwluFcHxoSxNgoRT3aoQ45lRcHDI4gCRagcNXkDWQ6qH-cyZzqoWkb7Rs-Mwx3W6ZJsJ-oLt375HSyuYbGLiszL6nUJwk2MrEoDaVBTIt2XGe0qi2lziyOpC73yf3LqCPTtX9kllit-MjMuJPNQyWukBnIJhLeYJpUIW1sntq5WVDC-E6tFqYd8C0J9tgxSIdbsYQ8xsNgxkrHHQrjSVZw4RsVIC1PeVQGmmKejzH0rfxbP2KPZvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت قهرمانی آرسنال در لیگ برتر، یادی کنیم از جاویدنام عارف جعفرزاده
❤️
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/funhiphop/75395" target="_blank">📅 00:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آرسنال پس از ۲۲ سال قهرمان لیگ برتر انگلستان شد
🏆
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/funhiphop/75394" target="_blank">📅 23:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دیگه به هادی چوپان نمیشه لقب آرسنال داد باید به همون مادرجنده کفایت کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/funhiphop/75393" target="_blank">📅 23:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75392">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">توضیحات کامل فرمانده سنتکام به کنگره آمریکا درمورد مدرسه‌ای میناب: کاملا روشن است که ایالات متحده به طور عمدی غیرنظامیان را هدف قرار نمی‌دهد. مردم ایران دشمن ما نیستند. سپاه پاسداران انقلاب اسلامی در این مورد دشمن است. تحقیقات در جریان است. این یک تحقیق پیچیده…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/funhiphop/75392" target="_blank">📅 23:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حکم پژمان جمشیدی صادر شد و به ۹۹ ضربه شلاق تعزیری محکوم شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/funhiphop/75391" target="_blank">📅 23:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d909bc992.mp4?token=cG-9-gV2MdTZSNvdohwC5aAYwoQ-Icnp1iN55RCw8jwlVCgwfKWeV3Va5RgrfSkQ8D9GLt1iuYbO5YyyIhOIdH_YGa0LszPWPi--KpwstrQvH4e7Ad2T5xXwNgUjCjZRZys7ptagP9prDtysWvOdhSLQvrAbaVe8tJ1HQh0L41E4jvXSf-QxGua-y-KT_FWBdce-URp2USVKaLy9r8O5XmlBchWgHZXWCcL3jdFsXLqv8tIQMybB5O1VrfIMzuOhvAIYWp0SWtBXHP7WKQKbv9zJq704ALyEKdkXgTp3fYCyggg3BhNk7W0-6042-rFcE_cM0VmQueEOC83fXmytfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d909bc992.mp4?token=cG-9-gV2MdTZSNvdohwC5aAYwoQ-Icnp1iN55RCw8jwlVCgwfKWeV3Va5RgrfSkQ8D9GLt1iuYbO5YyyIhOIdH_YGa0LszPWPi--KpwstrQvH4e7Ad2T5xXwNgUjCjZRZys7ptagP9prDtysWvOdhSLQvrAbaVe8tJ1HQh0L41E4jvXSf-QxGua-y-KT_FWBdce-URp2USVKaLy9r8O5XmlBchWgHZXWCcL3jdFsXLqv8tIQMybB5O1VrfIMzuOhvAIYWp0SWtBXHP7WKQKbv9zJq704ALyEKdkXgTp3fYCyggg3BhNk7W0-6042-rFcE_cM0VmQueEOC83fXmytfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده سنتکام به کنگره:  مدرسه میناب در سایت فعال موشکی قرار داشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/funhiphop/75390" target="_blank">📅 23:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فرمانده سنتکام به کنگره:  مدرسه میناب در سایت فعال موشکی قرار داشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/funhiphop/75389" target="_blank">📅 23:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🛍
تخفیف ویژه تا پایان امشب
🛍
دوباره تخفیفمون رو تمدید کردیم
😍
هر گیگ فقط 149 هزار تومن
‼️
✅
پینگ عالی و پایدار
✅
بدون ضریب و محدودیت کاربر
✅
لینک ساب برای مدیریت حجم
✅
پشتیبانی ۲۴ ساعته روی همه سرورها   200 گیگ شارژ شد
⭐️
تا تموم نشده به ادمین پیام بده…</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/funhiphop/75388" target="_blank">📅 23:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🛍
تخفیف ویژه تا پایان امشب
🛍
دوباره تخفیفمون رو تمدید کردیم
😍
هر گیگ فقط 149 هزار تومن
‼️
✅
پینگ عالی و پایدار
✅
بدون ضریب و محدودیت کاربر
✅
لینک ساب برای مدیریت حجم
✅
پشتیبانی ۲۴ ساعته روی همه سرورها
200 گیگ شارژ شد
⭐️
تا تموم نشده به ادمین پیام بده
🔗
کانال مشتریان
🔗
خرید</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/funhiphop/75387" target="_blank">📅 23:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">من سیتی گل خورد
قهرمانی آرسنال از همیشه نزدیک تره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/funhiphop/75385" target="_blank">📅 22:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75382">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceda97bf16.mp4?token=fmPaLy5E9AF4IzpaY8Zmd5NRw5bcKZgPAEsVck8wl6ZQpYl0zNqnadSDRJ7nENR5dXVYSpSRm3jhQqBLda1rdo_MVM9eqXjrnnUg-ZE3LwX0QwuoI5JLPUMDKAWjTF-ivXCNfYCx2Saa9kX6CjmkFbtrCJX4FgtcxQdEY4YwKmPzw5FHK6yKlYd4DOR3AXObe-6ts-7Jfxe8YgI4CY-SGfYjQ1ObJasb8TG69PS2OKs2MJH2gozTHgywJF5X5vzgP_n-fJ0fFbwvAY87VOjm4GL3MKW7NFCj8rOF8Hf0Chx2TZTwjJtu0KdKrEGvBHtRD8t3PupPjFvC3Zxfh1uEGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceda97bf16.mp4?token=fmPaLy5E9AF4IzpaY8Zmd5NRw5bcKZgPAEsVck8wl6ZQpYl0zNqnadSDRJ7nENR5dXVYSpSRm3jhQqBLda1rdo_MVM9eqXjrnnUg-ZE3LwX0QwuoI5JLPUMDKAWjTF-ivXCNfYCx2Saa9kX6CjmkFbtrCJX4FgtcxQdEY4YwKmPzw5FHK6yKlYd4DOR3AXObe-6ts-7Jfxe8YgI4CY-SGfYjQ1ObJasb8TG69PS2OKs2MJH2gozTHgywJF5X5vzgP_n-fJ0fFbwvAY87VOjm4GL3MKW7NFCj8rOF8Hf0Chx2TZTwjJtu0KdKrEGvBHtRD8t3PupPjFvC3Zxfh1uEGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جِی‌دی ونس :
ایران کشوری بسیار پیچیده است. کشوری است که من تظاهر نمی‌کنم آن را بفهمم...
این یک تمدن بزرگ و پرافتخار است.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/funhiphop/75382" target="_blank">📅 22:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75381">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9aacc343d.mp4?token=hCH86vyERau5k__advfp-rrFXUsfnrykJCJhptBzGY148UppKKp75_PqyXXPJnGc8jQv6FPzysyJeJeXDgy775fC-V19ogwA2_6qRIkTDJDvKu0Y45-xq9Opn6P8Z0zcZkqDNb5BYIxv0CjeqACE1W92FAGcIsxxeHl1uFgz3Yjz4_uBxQ6Z9saVT7aYGKuAmfUKhUWLIjxNEbx1tsjjF2wQJ4jDfYW9h_7sL3aAUFSEyVXGht9E9spw1OjUK1mAgnlwOIgyC505a54KjSUJjeowb2rRb9NtC2NifmeqB33YUyCxXqMK-VyyI-PJxC8If2tkJ2U8JOaqYGjVfpmVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9aacc343d.mp4?token=hCH86vyERau5k__advfp-rrFXUsfnrykJCJhptBzGY148UppKKp75_PqyXXPJnGc8jQv6FPzysyJeJeXDgy775fC-V19ogwA2_6qRIkTDJDvKu0Y45-xq9Opn6P8Z0zcZkqDNb5BYIxv0CjeqACE1W92FAGcIsxxeHl1uFgz3Yjz4_uBxQ6Z9saVT7aYGKuAmfUKhUWLIjxNEbx1tsjjF2wQJ4jDfYW9h_7sL3aAUFSEyVXGht9E9spw1OjUK1mAgnlwOIgyC505a54KjSUJjeowb2rRb9NtC2NifmeqB33YUyCxXqMK-VyyI-PJxC8If2tkJ2U8JOaqYGjVfpmVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان قصار استاد جی‌دی ونس درمورد ایران:
تا هنگامی که ندانید، هرگز نمی‌دانید.
تنها کار خوبی که ما می‌توانیم برای ایران انجام دهیم، مذاکره با حسن نیت است...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/funhiphop/75381" target="_blank">📅 22:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75380">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امشب به احتمال خیلی زیاد آرسنال قهرمان لیگ برتر میشه
پیشاپیش به طرفداران این تیم تبریک میگم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/75380" target="_blank">📅 21:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75379">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مقام امنیتی ایالات متحده به کان نیوز:  تدارکات مشترک ایالات متحده و اسرائیل برای از سرگیری عملیات نظامی علیه ایران تکمیل شده است، انتظار میر‌ود ترامپ به زودی تصمیم بگیرد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/funhiphop/75379" target="_blank">📅 21:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssxKiA21NvbCOtEGhpM2eTEz3U-_g3-kAha11AYBnUB4cgEH_BOXH0oveee5DmhxxsCKiUBwc2WB13F76lEc7NImOVLvTREiPegROvoUkLulkMsp6p1qedDZ5B2Bx9E1nSZKU7nN7yl0wFgPumB8BZOQte-bS0Ax0RNxfOv1cRwu7Vh1dDoByvAD-jCMKgwAAmdLTCnznjICmtyt02JJ2Gg4tT_jl0b9Akyru8cJiaQAlbz3bL3ndM16_X59c2e_zY1HNlr2vXzVbgeUA9X2Sbqw_Jij3bvA8SvclAXZFdO1sK9w8FoEm_08jsby7JgZ97qDhS-Xp10x3bXAzsygGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گیگی ۲۰۰ پول وی پی ان میدم که برم اینستا از هر سه تا ریلز دوتاش صدای آنچلوتی باشه که میگه نیمار جونیور؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/funhiphop/75377" target="_blank">📅 21:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!   دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
( فقط 300 گیگابایت موجوده! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/funhiphop/75376" target="_blank">📅 21:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مقام امنیتی ایالات متحده به کان نیوز:
تدارکات مشترک ایالات متحده و اسرائیل برای از سرگیری عملیات نظامی علیه ایران تکمیل شده است، انتظار میر‌ود ترامپ به زودی تصمیم بگیرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/funhiphop/75375" target="_blank">📅 21:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbEWOGJgvKt229a1lZKWbJ3ZYCTB9tEjmZPJ_KDiLJ7zuxL4wV4x5jrj4tqPHpS-IT53CKkgKF5IMFPF8s7PTGPyhWeZYMJQ4oX2424WCLhiJrI_lZFaj3DQfEWkC7-V8KpjMhCqy68zhumepUur5uKh7oB4L3wi1szJS67qB-G1z7Z3sYDpfRsowl96rKfSPtptzaS5nWTMxAxN-d5M3qgSSUFBKkLzCfqxhlVJjrf6QItEllSscCBw5TG8o_tcQiXPQFV_169PQcSFMICsG5RWSXocSsw9CbPnoE9gl4OLo3orohg6O01dC8b8ZSbzVZLrB1YSSx7VlL1jobMSVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و استاد جنگ هوایی و دریایی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/funhiphop/75374" target="_blank">📅 21:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">زن رشید مظاهری با این استوری اعلام کرد رشید مظاهری بازداشت شده و جونش در خطره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/funhiphop/75373" target="_blank">📅 20:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7tA0uz04Je9bSX6oqMFf60Vh4E5RHZ5kFAEjr_j9WV6y_1akP8OxdkB65Q8IweIQeC96P68kKFauOS01NRFlmbI2-ExygK3Ji2k6_HP7622w3i3n6rYhaSSvCSWrao9fHzy-xbQjoL5cSrKiOGmR2farizrRfuLVPpePeqO3BYZMzpES7qCXOjqwJCfKQONWVtwtRLmfM08lCZkQewfaFvTE7UziMZjejquBWUaNo94H7uqfLZzPLS-UjXGCd0fdhVWDytsZ1U1POJxwdROT3aF9H_jWCXuYLsDzI2Z55fglJmhR4pdwlaZKpJ92ynzDU5VdznLufN_QO2Oa8GQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏علیرضا نجاتی با قید وثیقه آزاد شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/funhiphop/75371" target="_blank">📅 20:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75370">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانال ۱۲ اسرائیل: درحال حاضر اقداماتی برای اطمینان از اجرای یک حمله گسترده درصورت لزوم، در حال انجام است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/funhiphop/75370" target="_blank">📅 20:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فیفا: هر پرچمی جز پرچم زسمی کشورها وارد ورزشگاه بشه باهاش برخورد میکنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/funhiphop/75369" target="_blank">📅 20:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7FlxeKLCaOWlsAWCF6ZqQ4xKN92TJX-Bi__T0483hyfc2OCjeN5j2nIWTzi6koOk2X-NhFrX2f6b-XNhO3wRSbqvSwKCDNb1a0nGMzgLvNoWvZJzcCbRkAawQeL5j_Zu-L--tNVgj_WVVYu3Y6dWkiq3zoCZi7-PpPIhMlVM4bXaiIJan7NFh3grpPQWep45kHwlvbHehB1BrQjMDYoC61x7Q1z4Yn0H4cbHN5lJosrJb5GKRplKs1WImkhu3ISAiABszw5K-G5ggdyjfAFKJyHfxJIoNYi99pI_dE8HYvD_eG9tle32MUIOtHH4YEhdl8ix47drekgKP4puE5i9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرتون همچین غولی براش مهمه تو فینال با اسپرز بازی کنه یا تاندر کون جفتشون میزاره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/funhiphop/75368" target="_blank">📅 19:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
(
فقط 300 گیگابایت موجوده!
)
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/funhiphop/75367" target="_blank">📅 19:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این حرفای منو جدی نگیرید همشون “ترولن” و  تیکه انداختن به حرفای کلیشه ای بعضی افراده اگه به دلتون گرفتید دیگه نگیرید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/funhiphop/75366" target="_blank">📅 19:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75365">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
تنگه هرمز متعلق به ایران نیست. این آب‌های بین‌المللی است — این کار برای آنها نیست.
آنها درس خود را گرفته‌اند.
اگر امروز بروم، ۲۵ سال طول می‌کشد تا بازسازی کنند. اما ما نمی‌رویم، ما این کار را درست انجام خواهیم داد...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/funhiphop/75365" target="_blank">📅 18:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75364">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ درباره ایران:
فکر می‌کنم خیلی مهم است که اورانیوم غنی شده را به دست آوریم.
شاید تاثیر روانی‌اش بر آنها بیشتر از هر چیز دیگری مهم باشد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/75364" target="_blank">📅 18:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75363">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ رد داده:
کشورهای خلیج در حال مذاکره با ایران هستند و
اسرائیل
هم همینطور.
دیروز تماسی دریافت کردم و به من گفتند، «آقا، می‌توانید صبر کنید؟ ما خیلی به یک توافق نزدیکیم.»
و  من به ایران مهلتی دو یا سه روزه می‌دهم، شاید تا جمعه یا شنبه. یک بازه زمانی محدود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/funhiphop/75363" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75362">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ درمورد ایران:
ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم.
هنوز مطمئن نیستم ولی خیلی زود خواهیم فهمید.
من یک ساعت با آغاز حمله به ایران فاصله داشتم و اگر منصرف نمی‌شدم آن اکنون اتفاق می‌افتاد.
به هرحال قایق‌ها و کشتی‌ها بارگیری شده‌اند و ما آماده شروع هستیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/75362" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75361">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1vYstRPffhQqwrl7ldlmqAGnrqwzCf8mC7muEvHCeaatlLmY8iWBjjM57IYRoatg9cmEqShhM6X0ix5m-OHckqPtBsdrvwK1gThWncrEXxRjt1MvC_ZOpcM4X4FlpjdrZ8BPUWQeTnc9X5dWpj_uh1hqihyTe5AbU-7Gn5Px1H91jCusu9eJg7-3-0VOemn_vWoe8JZPMPvZigRsC3oNBsBl5VLbiq1mZQ7p0uC0E3LL8633vyShW_1k8lDdxwsPM16nD12ssA25BYhUgFwTJqohS7_zgxAzkzi8LS8G2w_43FxlMn1dhRRNDo5jZajcSdGnaUG_neB01vZ67YJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون دکتر عراقچی:
ایالات متحده می‌گوید حمله به ایران را «موقتا» متوقف کرده تا فرصت مذاکره فراهم شود؛
اما در عین حال از آمادگی خود برای انجام حمله‌ای گسترده در هر لحظه سخن می‌گوید.
این یعنی تهدید را فرصتی برای صلح می‌دانند!
ایران یکپارچه متحد است و با قاطعیت آماده مقابله با هر تجاوز نظامی است.
برای ما، تسلیم شدن هیچ معنایی ندارد؛ یا پیروز می‌شویم یا شهید می‌شویم.
و همانطور که شهید رجب بیگی گفت: ما ملتی بزرگ هستیم، بیایید نام خود را در تاریخ ثبت کنیم؛ از میان همه رنگ‌ها، قرمز را انتخاب کردیم، و از میان همه انواع مرگ، شهادت را برگزیدیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/funhiphop/75361" target="_blank">📅 18:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75360">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">همیشه یادتون باشه که بازارهای مالی بسیار باهوش هستند و زودتر از هرکس دیگه ای (حتی خود ترامپ) اتفاقات آینده رو انعکاس میدن
دیروز بعد از صحبت ترامپ، تغییرات بازارهای مالی نه تنها نشان از سازش و مذاکره نمیده، بلکه بیشتر احتمال وقوع حمله رو تقویت میکنه
پ.ن: بورس آمریکا دوشنبه هفته آینده تعطیله و این هفته بهترین فرصت برای ترامپه که هم حمله رو انجام بده هم بازارهای مالی رو کنترل کنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/funhiphop/75360" target="_blank">📅 17:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75357">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پشمام معین میخواد واسه دعوت شدن نیمار به تیم ملی برزیل تو جام جهانی آهنگ بخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/funhiphop/75357" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75356">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX5UryCO4jA60bHNyeofMJ7btiv4RjIF4tAaeU1nk46BzfjRy3mr5Y2HOZAXhKeaavM9DhHYrGcEmQCp7P9-x9aavcT8nMlEbECRbSLPKx8__XetoAVyrB19gESv3B1dofnMRpJIIa5CotrEoBRqBF4fVQ09q64yd7fNJoGQDALF_k1Fqqaq91CM5-EsO4jWfARGi0V2A9OkzNclLUzuwwS65CtaaHI5Re6L4-Sxa2xea685vtyR4CBq3gbT__stZIiibsBjkrdUM42JB86fplxRIb5wgqzrn8SFj2kWp5eJUOlt12DKHXRZL5-wO0tdfpwaip0t09C3I8TaLyoJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی ناموسا تاکتیک های ناشناختتو برای خودت نگه دار به اینا آموزش نده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/funhiphop/75356" target="_blank">📅 16:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75355">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d9062d93.mp4?token=Lz8i3sFJ_hCYrLxEHibwLUt2EkP0iUuw_D9t_H6WMDMHDzGHmLTxIRncqohFrMZVv8dKVdDL9wF9EZi8Kkd3_6OX6HmU-mNR_Mxj1KUtqW_gPGLZSCFbIGl5Wmj-ABlNX9xwBdZ_t4rojuPq7eKYpQC144mlKPfPOE1gve0E8rxkrWbUjUzuymhjHgkVCMZgfpLB9LByV3ojq-hvSrqGbYe6Ou0wZdeztt1oLV0N1iUkl0jqfiD66HeeVQPcv-EPGKBLvV40XhFgqlBLwZD3ES8FLismDv2dPGRyxxz2KMywd-WeooNckFI6A4lPpEDr02AGrnEuKukYNHtOAVFbsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d9062d93.mp4?token=Lz8i3sFJ_hCYrLxEHibwLUt2EkP0iUuw_D9t_H6WMDMHDzGHmLTxIRncqohFrMZVv8dKVdDL9wF9EZi8Kkd3_6OX6HmU-mNR_Mxj1KUtqW_gPGLZSCFbIGl5Wmj-ABlNX9xwBdZ_t4rojuPq7eKYpQC144mlKPfPOE1gve0E8rxkrWbUjUzuymhjHgkVCMZgfpLB9LByV3ojq-hvSrqGbYe6Ou0wZdeztt1oLV0N1iUkl0jqfiD66HeeVQPcv-EPGKBLvV40XhFgqlBLwZD3ES8FLismDv2dPGRyxxz2KMywd-WeooNckFI6A4lPpEDr02AGrnEuKukYNHtOAVFbsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راستی امروز سالگرد کشته شدن ابراهیم رئیسیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/funhiphop/75355" target="_blank">📅 16:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75354">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📶
بهترین ارائه دهنده فیلترشکن
🤝
آیپی static (ثابت) ، مناسب ترید و وبگردی (اینستاگرام - یوتیوب و....)
🔥
| بالاترین سرعت ممکن روی تمامی اپراتور ها
✅
تعرفه سرویس ها زمان دار :
🥑
1 گیگ | 4  روزه ⇐ 290 تومان
😼
3 گیگ | 9 روزه ⇐ 850 تومان
🛍
5 گیگ | 14 روزه…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/75354" target="_blank">📅 16:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75353">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSeniorVpn</strong></div>
<div class="tg-text">📶
بهترین ارائه دهنده فیلترشکن
🤝
آیپی static (ثابت) ، مناسب ترید و وبگردی (اینستاگرام - یوتیوب و....)
🔥
| بالاترین سرعت ممکن روی تمامی اپراتور ها
✅
تعرفه سرویس ها زمان دار :
🥑
1 گیگ | 4  روزه ⇐ 290 تومان
😼
3 گیگ | 9 روزه ⇐ 850 تومان
🛍
5 گیگ | 14 روزه ⇐ 1,250 تومان
☄️
10 گیگ |  20 روزه ⇐ 2,300 تومان
🥶
20 گیگ | 24 روزه ⇐ 3,880 تومان
🚀
50 گیگ | 30 روزه ⇐ 8,770 تومان
💢
💢
تعرفه سرویس‌های بدون محدودیت :
💆‍♂️
1 گیگ ¡ کاربر نامحدود  ⇐348 تومان
💆‍♂️
3 گیگ ¡ کاربر نامحدود  ⇐ 1,000 تومان
💆‍♂️
5 گیگ به بالا ¡ کاربر نامحدود ⇐گیگی 290
💆‍♂️
10 گیگ به بالا ¡ کاربر نامحدود ⇐گیگی 250
✔️
جهت استعلام قیمت حجم بالای 100 گیگ و اوت باند ویژه فروش همکاری (1TB) به پشتیبانی پیام بدید
🙄
خرید از طریق پشتیبانی :
✅
@VpnSenior_admin
💵
پرداخت به صورت ارزی شامل تخفیف می‌شود
___
꧷
📣
@vpnsenior</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/funhiphop/75353" target="_blank">📅 16:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75352">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKRuWBgLweR2Yyd3YMOkjnr4PBuBkVaClpVfQ109RqDNpdsbS5BnkW0_kvGELxWmUl9llSYRXU14RDcI1JZXQ_UoAujGEVgmdVt7GKOieB_NGHOVOMni4PsHFhZrq4dIpns62nLt2gR3RhgV5xcNkpkZ1VKzDxbgpWl17ebKxxxT3xtdUldIBCDaSXk8I5mKhHeJE-1QPCXd6t96W4EdeaABHcPbND8fUSYgtbVgJuIBLQLGbUiXQA-uMr5w4BEVXyYI5zrDCS8pNXruGXqXzlk85g5afaAXhftS8V4sQgmeeNOhff6nx_l3cRkNUs9si4rmOjSSej8y0TFDlhUbcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید سردار آزمون و آرزوی موفقیت برای تیم ملی جمهوری اسلامی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/funhiphop/75352" target="_blank">📅 15:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75351">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ گفت که پس از درخواست رهبران کشورهای حوزه خلیج فارس برای زمان بیشتر جهت مذاکرات، حمله برنامه‌ریزی‌شده آمریکا به ایران را متوقف کرده است.
این در حالیست که چندین مقام خلیج فارس به منابع ما گفته‌اند که از هیچ طرح حمله‌ای از سمت آمریکا مطلع نبوده‌اند که بخواهند مخالفتی کنند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/funhiphop/75351" target="_blank">📅 15:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75350">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گیگی ۲۰۰ پول وی پی ان میدم که برم اینستا از هر سه تا ریلز دوتاش صدای آنچلوتی باشه که میگه نیمار جونیور؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/funhiphop/75350" target="_blank">📅 15:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75349">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سازمان عفو بین‌الملل:
تعداد اعدام‌ها تو جهان تو سال 2025 به بالاترین سطح ثبت‌شده تو 44 سال گذشته رسیده و اعدام‌های انجام شده به‌دست جمهوری اسلامی، اصلی‌ترین عامل این افزایش بوده است.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/75349" target="_blank">📅 15:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75348">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ینی اگه قطریا دیروز کونی بازی درنمیاوردن الان داشتن میزدن؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/funhiphop/75348" target="_blank">📅 14:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75347">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرگزاری مهر: شنیده شدن انفجارهای مهیب در قشم. ماهیت این انفجارها هنوز مشخص نیست.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/funhiphop/75347" target="_blank">📅 14:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75346">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری مهر:  فعالیت پدافند قشم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/funhiphop/75346" target="_blank">📅 14:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75345">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سعی کنید تا حد امکان از نوبیتکس استفاده نکنید فعلا، آمریکا بدجور سیخ کرده روش هر لحظه ممکنه همچیشو فریز کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/funhiphop/75345" target="_blank">📅 14:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75344">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اهواز امروز  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/funhiphop/75344" target="_blank">📅 13:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75342">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c99MVQUhtvgYooQRrEhIf2KWXYG6KdGdFjFImsNZ5gdpDwVMmNo14RiHtJBwT9kML9wTTVPLYjnJEfInxtTM9KQOEGHHk7TSVXukXcr-hirAZxorIFBpvMBzT1Cao0AxQHWH4A11hAWZArQgkpSFZmqk3Jk-ZHu9pWaSBLdnkGXS7S-E8tmrcTeGJl9wv6vbgVa-3Viyxq8JsDaTECn7y92FAsjoERk1bl71IfLZ_rDJH6Dz7PBpR_HxS7GI_EczAoAM0drqj6Nmqvt4FxqvOIVJFKsLUayBEjVIIYaX5I_lTOb2GmZyslyUihQL-GrL3cMrz1paDLSQdnT4UVbnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهواز امروز
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/75342" target="_blank">📅 13:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75341">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90d827a7ab.mp4?token=MZRLdgrvmHmpGgPIQg1rusB88IdyB3OoVQecbe8105BGj42IdXgemrIwwL5zBNoix8a6waGGEdmDdFPoyDHVgJBU-PV7UyATPHHivuJwf-sRDnJBcOXSiB6m1_dJwiqygJsRUv_UHAfgdWIiTVKfPdWlo-JWArBwFomstG9Ik7flVaeZ-PAOz26GjXN-2mhO_qrp6ProGolDtQM1M7XT3qgjGnBM39wft2ywrqXnsXinlkCSCCx8V8TIiiq84TEoUQKU-850XxK4Quosj_BVQ-Ux9iehY6uM-q6OcDU_ZFpjnfjC004mNa8e0u1SKSF_EFvieWHqFKBQmV88A7taXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90d827a7ab.mp4?token=MZRLdgrvmHmpGgPIQg1rusB88IdyB3OoVQecbe8105BGj42IdXgemrIwwL5zBNoix8a6waGGEdmDdFPoyDHVgJBU-PV7UyATPHHivuJwf-sRDnJBcOXSiB6m1_dJwiqygJsRUv_UHAfgdWIiTVKfPdWlo-JWArBwFomstG9Ik7flVaeZ-PAOz26GjXN-2mhO_qrp6ProGolDtQM1M7XT3qgjGnBM39wft2ywrqXnsXinlkCSCCx8V8TIiiq84TEoUQKU-850XxK4Quosj_BVQ-Ux9iehY6uM-q6OcDU_ZFpjnfjC004mNa8e0u1SKSF_EFvieWHqFKBQmV88A7taXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بصورت خیلی عجیبی امروز به لبنان اتک نزدن  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/75341" target="_blank">📅 13:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75340">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بصورت خیلی عجیبی امروز به لبنان اتک نزدن
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/funhiphop/75340" target="_blank">📅 13:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75339">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">He said she was Persian   میشه  پسره گفت ایرانیه یادگرفتم ممنون
❤️</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/funhiphop/75339" target="_blank">📅 13:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75338">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Diddy:
He said she was Persian and started speakin' Farsi
پسره گفت ایرانیه و شروع کرد به فارسی حرف زدن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/75338" target="_blank">📅 13:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75337">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مدیرعامل جهاددانشگاهی
:
به دانشجوهایی که ازدواج کنند ۳۰ میلیون وام تعلق می‌گیرد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/funhiphop/75337" target="_blank">📅 13:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75336">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تسنیم:
رسانه‌های اسرائیلی اعلام کردند یک هواپیمای مقامات دولتی اسرائیل لحظاتی پیش به سمت امارات پرواز کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/funhiphop/75336" target="_blank">📅 12:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75335">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6TawOfPEbWKHpqe--oLyeZQXAvc4HhjiA8KaABkeSIrVLvaoZrDGMN_dc3KuJ12-RUiUl-uFyTRZdy5rwinQRnz3EO0Y_4LyLW51GwwNTCvAC7u6543wp-z91LtftRFE4NsJuooa35up-ZL3gV3InpSauaoyC_Jt06AaPCaFgzDTNjC5LRxoM5ZXzt1FxRX8l3381gcBiCWV4llie6aGOb5Ey3FPOgaO_402xd_bqIXdtDazaRKrsckKF3xof0q7SDCG1xSuvn74LPWoRPqhaoPG2AZ4IjOgGh5vY1ixLczc3kBjyLSpJ9uf4V6CvtD-RtjhowuaPO5VkzLXWjByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادر فکر میکند شخصیت اصلی داستان است
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/75335" target="_blank">📅 11:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75334">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یعنی ترامپ ریسک حمله قبل جام جهانی رو میکنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/funhiphop/75334" target="_blank">📅 11:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75330">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVPBw4sQwdZAhY6992IffUy2PK5Z_XQYdILhhsh50wKHqlohPajd3ZgGR8hznQ5XQO7sVpItHjB_AxoV0XUClSr6iug5B3VhkL8PKM7cEx4hlrezkbBQVBeCpKhHhVoEtGPJDJi702QeBkGFITzZrSpuutU1fhNBYAfymjDxtryMU6ZqWfGsg4WFyM_R4ob3KHdzYVEIDYPojbXz6LqDrdTNPRI-exH0mUZTwHYZ7ZDqqPcDBOBaQhuma5lo82NpOG1QxOavQ-iZMx45ktQGcwQOnD7X-_l04D-MShl0-6V9IL1E1GY4rm61d6rkaDVpRtBzSnMoxy_OqPxvLfEkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mxKY79YHVN35FpbQ9YmIM_loxQM6MWqHO2K-vUp3p9ibclGD3tRJ3pQQJuFacsemPwFU7YC4LrWGLG_D759krd67JB4pXJQwQZ3Vh12JqTPvtmqflBzRGeo2Z0pKxBcWr0Frw889IKySPAhRWgq5eKk7uSN5sa766oE090lkHNDKHZ6WPGnHIJRdDe7vZCDq8Bcg-bLdGOakxEafaFuYcMiq4_KO7J0YKTB0Op37W5EwZbFW19S1lgaJDfalRp3OM-CjaWhOK5o544itSJ9gCOfvYm7kBcOie5jWi-TAyZaf1h3RzCMR6wicAgeswDzfYGtN_6NRV_1CvmjNQetdYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Erl6-EZHI96DgjIhyWRIKFybBkv5AOZoKgc7M3M5EfyEfllG3610dDMhEaQCKyZ-3JoeHPy1vlndTpUHmCBK15ZlSnyzBSXqDZrJ1OdxWqb10FcgSs5iDZPsYRJRM_WYeoPb3UmuXEM5KySo9r-JQiRWXPvimpaVffSNVhLbaif3hLXiQlQIrQxW2cFtyk2jLZKIimxYXh0t7p3yCOP8A-IKEgJkJ1e8PMWQSiGMZUx-pqNTiBzoHgQORuC7lNirTyUh6AjboPvIenkU9dZo2KZLmc42fP_RFeZGZX5cj29dSsvCqcLPf8NvfkojcM-lGWIZ1DnBMgc43WqAcReiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2QYAfytN7ulqjTRUNbSbzNAR9HjzglILABZPEYyFY6l543_K7DHvsUrLtwGoPaWC1geZeuStttcwAYvDGJ7i1aDOLeipfNPwDDU0tWFqY9Lvi-3VzePyNpDTxdxP0AvWNURpGC5qbkO4nKgOz84CuQHYd5XkG4jrieYeV5mDDO5Jz6hWimCQfvcPoNqkWZmybBV0hHyy3dhJyDUz_8hCFPz3EYoPZ72Zp1MnIBEbTye3NebekBv01gIRCqRfVYqXK9SpWnnEOsmdrwgfNCt97l_0dRcVWIsaG1NCv0sRj9arsSEGATseHykYqcYGWQHgGDWcvb_zzZfb4NRV6Rtjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راک‌استار رسما اعلام کرد جی‌تی‌ای ۶، ۲۸ آبان امسال منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/funhiphop/75330" target="_blank">📅 11:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75329">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فرمین لوپز جام جهانی رو از دست داد بخاطر مصدومیت</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/funhiphop/75329" target="_blank">📅 11:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75328">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بورس ایران بلاخره باز شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/funhiphop/75328" target="_blank">📅 10:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75327">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIF4O-gBi48yS3gC47XXpSlxdPTWK0JLt_jSdAp_lM_qm8XZAMOeWe925tKvXUZ5nmTp1adiDHhN37sPfhLX-TfVDIlZrMvx8ohisw7KjmLYdfeNzGNFwNVvwzaHsLbeRhNqQtS3p6kBc4EfNY0j9rkW-TOpyCa_LZOT1Nxpz0UFLseFxch_j1__cWFAlRCbT3c-VXA7Xqx4dQBAOwplDiVNYha5zVSOPogB1ySyymN1lqHIyGoXvRO5PAw_IqiBKO3-yubVQvHu5LKREJrDg-n-rzIwJDzjEoouYuL8cgqVEodPzWTZt8mJmDnlIgc6uRZhQe3EmU3rnm-jy8r0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ایران بلاخره باز شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/funhiphop/75327" target="_blank">📅 10:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75326">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔮
اینترنت آزاد با «ملوان زبل»
📦
تخفیف 24 ساعته
📦
50,000 تومان تخفیف روی اولین خرید مثلا 1 گیگ میشه 140,000 تومان
😐
🔥
پلن ویژه:
✨
1G = 190,000 تومان
✨
2G = 380,000 تومان
✨
3G = 540,000 تومان
✨
5G = 850,000 تومان
✨
10G = 1,600,000 تومان
☄️
تمام سرویس ها با ساب تقدیمتون…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/funhiphop/75326" target="_blank">📅 10:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdMRSNoikq-ZAR-enq3FZJz6aZndC58oOqnRfWYcp1zLISYxS6cM1AYaXgIcd6pxFZBazKe6P8YfbegwhL8mI3hF_3AbPQK0ULlSBkPWE64O92ukr1GIYSiEpCWTQ5zUQ_gjeS1xGK-fucz0piABzZaNeNLK993RJX8QCuYp5PV9ATEh5cTTxaojzKk7tpgUIS4rw3TT1oF3OOLbJIgWygFVWCsuAAKr7UQTPYU__-yG7KbOqtF-6oRpzGiWAA-FzNSglzcSq-Q2lbJwegNU8Otg8bRE-wgvS36AkXHXm1tK4vser9ZvIGeJ56C6AuIfuywtbP-lis5YRmN9p_y5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔮
اینترنت آزاد با «ملوان زبل»
📦
تخفیف 24 ساعته
📦
50,000 تومان تخفیف روی اولین خرید مثلا 1 گیگ میشه 140,000 تومان
😐
🔥
پلن ویژه:
✨
1G = 190,000 تومان
✨
2G = 380,000 تومان
✨
3G = 540,000 تومان
✨
5G = 850,000 تومان
✨
10G = 1,600,000 تومان
☄️
تمام سرویس ها با ساب تقدیمتون میشه
☄️
⭐️
‌تا 100G هم موجوده
⭐️
کاربر و زمان نامحدود است
🌕
✅
تحویل سریع
✅
پشتیبانی
✅
مناسب آیفون و اندروید
✍️
برای خرید پیام بده
🚀
«ملوان زبل»؛
@MalavanZ_SUPPORT
چنل
🦠
@MalavanVpn</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75324" target="_blank">📅 09:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس:
ما در حال کار بر روی چارچوب قانونی هستیم که توسط مجلس شورای اسلامی برای مدیریت تنگه هرمز تصویب خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/funhiphop/75323" target="_blank">📅 08:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75322">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a0f52793.mp4?token=kdsEbxMzDVCkppYg4G2BEj5htMfZdFH4xBd_S7wobwDN4WUor73MgV048iRTSWhITMTdHoC1KvuCo3fZPQty-no3GPUGMTEcYXNS4ew3GnC41yvbN7prI6t3DeZDY3Q89HS_SG-waIK_3i00t3pcHKcX30Dzmq_dD5gItbC-A4Q5b7joFnZRlyBKwHbp8l5fAWpsuHjw7jIm1l-HRi0DApIXVGQCt1XyB7rygwELsXHe6GiR8BTm2BOK8ctCm5K-e_51jIZliOqTKT7_sEmug3J5pSWMI9K8LMp-4rSSukGJ9vq9cbMLmtWTxHEI6RUL5smqzI_Mt5U2mdP2TQIcJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a0f52793.mp4?token=kdsEbxMzDVCkppYg4G2BEj5htMfZdFH4xBd_S7wobwDN4WUor73MgV048iRTSWhITMTdHoC1KvuCo3fZPQty-no3GPUGMTEcYXNS4ew3GnC41yvbN7prI6t3DeZDY3Q89HS_SG-waIK_3i00t3pcHKcX30Dzmq_dD5gItbC-A4Q5b7joFnZRlyBKwHbp8l5fAWpsuHjw7jIm1l-HRi0DApIXVGQCt1XyB7rygwELsXHe6GiR8BTm2BOK8ctCm5K-e_51jIZliOqTKT7_sEmug3J5pSWMI9K8LMp-4rSSukGJ9vq9cbMLmtWTxHEI6RUL5smqzI_Mt5U2mdP2TQIcJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی از من خواسته اند تا حمله نظامی برنامه ریزی شده خود به جمهوری اسلامی ایران را که برای فردا برنامه ریزی شده بود، متوقف کنم.…</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/funhiphop/75322" target="_blank">📅 03:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ:
ما حمله‌مان به ایران را ۲ تا ۳ روز به تعویق انداختیم چون عربستان سعودی، قطر و امارات فکر می‌کنند که به توافق بسیار نزدیکی رسیده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/funhiphop/75321" target="_blank">📅 01:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75317">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7hS9LeqD0-s4_QBKRuo3WCLl-dqi6u3lqjveH30LVeMTiWK_EJ0AufXW3c0mjfS8p2T94FDrQ_hCD5cc64VKI1Krp-ZLpIZ0E3Fk7l7C-CwemGxTpryWHTJ-y3hdsZOcgGfetma_bpl6dGINGJydb8xAl3UQfs02k388v2r3OYHzL2QUrvvWstWds1C8XweGgXhACIahm9U99zc1QeqT86XJ68CjfXEPUIzut3bsT6LMDuZAkxbonmuyP-9jGqli8YPzRrgBgQN3bLfLkWl9vN14c_wRHdDM7ed_vZplAXfZT2ScYwc4z9pXVPveDt4lzKc0UuSJgc0A_DBM1KSig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/75317" target="_blank">📅 00:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75316">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کارلو آنچلوتی تو یه حرکت انتحاری ژائو پدرو رو از لیست برزیل برا جام جهانی خط زد.  پ‌ن: نیمار دعوت شده  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/75316" target="_blank">📅 00:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75315">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XC14ZOCUDL3jWeUgnd3QeUbaDfYvX0DTasxxrsJsJaiSrwOobMrRaMzPU5z1mA2PC_rbm6QNPYVCGHTpF-RHY_KKrVxGgGXlxEtbCHwuQikxg2Uc9hIFew0xrS6u6l5HpeZHAgKjfgMtfubOFYYF9so5YYnL2CK1ULHadL1McGO3SXg-2no29nu8IjFG7GOZtFshwUZl7z57e7zhckHW0mz1lB9rYFkbaCMgZGPgO7Q1hDA7QyCWqlc6_lXc4K7SrVSFebFibs5whyEfkO4TMgZVk2SFEEM63kagu7JIvbcs7fdCq47dr5EVJvYiWVwmxzrwlfmnJKhrLf5Wd2v_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارلو آنچلوتی تو یه حرکت انتحاری ژائو پدرو رو از لیست برزیل برا جام جهانی خط زد.
پ‌ن: نیمار دعوت شده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/funhiphop/75315" target="_blank">📅 00:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75314">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کل تلگرام دارن با کانفیگا رایگان سونیک وصل میشن شماهم وصل شید:
@SonicVPNRBot</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/funhiphop/75314" target="_blank">📅 00:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75313">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پدافند هوایی اصفهان درحال فعالیت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/75313" target="_blank">📅 00:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75312">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppa6bp4TPP6pq_Ft-NtTHmY0zvvQTgF_7aiXUhW2X8KPZ8GyDxNujlM2mMDJ5QKxj0MrTb1XkJ08xUEHU40_Hqo3VojErwrONVK44GHJTmECk4bBnRWh7YqEznARr0D_Sp7yt4ke6YGBAw5JR9KolxZSudJyBlRGNr6APUaKTPIM34bNdyS82mn36CpDUMkPWPmRAzRrXmaN177RIYk2jxsA_McLsUy1ziAOIFOjdyv2m2v2L4qOAVL9OTdslMT2-DcHBVOAGAVeN6DUrfMqB6RdSPiv9CKw99bHD3hwcTi99HHwaRq_ewS1x3_dwbx-80AVHpRdQBttLH9oZkbReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
فیلد مارشال رضایی
برای حمله نظامی ضرب‌الاجل تعیین می‌کند و سپس خودش آن را لغو می‌کند!
با این امید واهی که ملت و مسئولان ایرانی را تسلیم کند!
مشت آهنین نیروهای مسلح قدرتمند و ملت بزرگ ایران آنها را مجبور به
عقب‌نشینی و تسلیم
خواهد کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/funhiphop/75312" target="_blank">📅 23:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75311">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فوری: پپ گواردیولا در آخر فصل منچسترسیتی رو ترک میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/75311" target="_blank">📅 23:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75310">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">با رفتن پپ از لیگ انگلیس، دوران پادشاهی آرسنال با رهبری آرتتا رسما شروع میشه و تا سالها هیچکس نمیتونه جلوی این تیم رو بگیره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/funhiphop/75310" target="_blank">📅 23:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75309">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فوری:
پپ گواردیولا در آخر فصل منچسترسیتی رو ترک میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/funhiphop/75309" target="_blank">📅 23:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75308">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">باز حداقل الان ۱۰۰٪ سهام کمپانی های خودرو سازی داخلی دست خودمونه
نه که ۲۰ درصد بنز دست ما باشه نصفیش دست اجنبی‌ها
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/funhiphop/75308" target="_blank">📅 23:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75307">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQCJQcs1l57CYuuxowy0C0vsEIrqHO__iRzpzDV5u4UvxigCxkCtYW3OPO569lIM-mCcTv3Q8Kxc-6An62dUweb7hu1d0MBciGJm0PY2dgw41chXESLviWF1m7qFhOgAETo_2T5EKuUmW-VvYL9B9M8sH5HGhmpEXBcOVP9MLIwYGlff6x7EskeMBc2wbM58oxq_kPAOWzhIq8n3FnqwZxVL0EUgCVsk3VOAwMUF9f6KzUDqEOqXcLDObeETv9UDn-OCZzPqZJqQQ24njUC5EGfTJBUStIPPpS28cxY9T32oryvg4RV7A4P1yzTKxfvrgWczzf27o3YW7-3mILfPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی از من خواسته اند تا حمله نظامی برنامه ریزی شده خود به جمهوری اسلامی ایران را که برای فردا برنامه ریزی شده بود، متوقف کنم.…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/75307" target="_blank">📅 23:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75306">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNDWZi292RNNhj4c6BTOWxQk_2HRstVpFdOjzUhjMiBou29Aj8iu1mRPhIShk2sEFMoPwBSamNiyOO1DtABkUkS7xg00vUFCrXZIpADcpYcTU9ApC-UHp_rTxdNIWKoyy97V7_PYSwAKCo7lJo869mVmxxDC1S7Rf3mkbjL5S6xr9mqfels2KjCT3LRQgvR2a9FonDeHEL3uomcgYOrcpzMVAe6VBN0OC578uXeO1HBwepOEJd1-z0HUV18Vgtdg8stJtz5VmlDrVfI6ZmktBSqPMX_q5QuLnv54Lvr1UoyYglTgdpSs4LupkaP2xsT4dwmUcqXGDLqehSRvmldpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی از من خواسته اند تا حمله نظامی برنامه ریزی شده خود به جمهوری اسلامی ایران را که برای فردا برنامه ریزی شده بود، متوقف کنم. به امید توافقی که خواهد شد که برای ایالات متحده آمریکا و همچنین تمامی کشورهای خاورمیانه و فراتر از آن بسیار قابل قبول خواهد بود.
مهمتر از همه، این توافق شامل عدم وجود سلاح هسته ای برای ایران خواهد بود! با توجه به احترامی که به رهبران فوق الذکر دارم، به وزیر جنگ، پیت هگزث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین و ارتش ایالات متحده دستور داده ام که فردا حمله برنامه ریزی شده به ایران را انجام نخواهیم داد، بلکه به آنها دستور داده ام که  در صورت به توافق نرسیدن آماده باشند تا با یک حمله قابل قبول و در مقیاس بزرگ و کامل علیه ایران آماده باشند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/75306" target="_blank">📅 22:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75305">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرگزاری مهر:
فعالیت پدافند قشم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/funhiphop/75305" target="_blank">📅 22:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75303">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الان یادم اومد ک تتلو راجب ممه های گلشیفته آهنگ خونده بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/funhiphop/75303" target="_blank">📅 22:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75302">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FN-s02UyHLgx0AWDWFLveD2P-G7gwrW6EjSCb7Erf5XFN4qsxLpsUgH_QeFO4edvpVjYO1czuW8Xm44gW4JiuVLEYWGnDcYH_r7jeb-g5Je3TLFIRtMrLsFXlb-KcZWjqkg-H8vfAItz1i-FvxoCvd73JuYCIq51Eu2JUsKmhIJxXlfRM9hPu1QMjXAceIK20WYdPTCLXqOvN4vVgbwtsvQKLfjJZdRU8OQ5j-grnoGy4Lfwrj7PQpKsSuYJBPMx4duJtpswc8EOC8fDlxIPTR1H5fGWd5YMb7klcDnfJG1cfAtMiDtyUF60v-Vsi2vxtFS6UCMzBB6uo_cRC91WAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/75302" target="_blank">📅 21:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75301">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✈️
واشنگتن پست
اسرائیل برای آغاز دوباره عملیات علیه ایران آمادگی کامل دارد و اکنون منتظر تایید و چراغ سبز نهایی از سوی آمریکا است.
😶
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/funhiphop/75301" target="_blank">📅 20:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75299">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: از آنها کاملا ناامید نشده‌ام و می‌توانم به شما بگویم که آنها بیش از هر زمان دیگری می‌خواهند معامله‌ای انجام دهند، چون می‌دانند که به زودی چه اتفاقی خواهد افتاد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/funhiphop/75299" target="_blank">📅 20:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75298">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وقتی نیویورک پست درباره اظهارات قبلی ترامپ که می‌گفت ممکن است یک توقف ۲۰ ساله در غنی‌سازی اورانیوم ایران را بپذیرد، از ترامپ سوال کرد، ترامپ گفت:  الان به هیچ چیزی تمایل ندارم. در حالی که از ارائه جزئیات بیشتر خودداری کرد. ترامپ در ادامه: واقعاً نمی‌توانم…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/funhiphop/75298" target="_blank">📅 20:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75297">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ به نیویورک پست:  من پیشنهاد ایران را قبول نمی‌کنم. ایران باید بداند که در این مذاکرات من حاضر به دادن امتیاز به ایران نیستم. ایران خواهد دانست که «به زودی چه اتفاقی خواهد افتاد» پس از دیدار من با تیم امنیت ملی.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/funhiphop/75297" target="_blank">📅 20:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75296">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ به نیویورک پست:
من پیشنهاد ایران را قبول نمی‌کنم.
ایران باید بداند که در این مذاکرات من حاضر به دادن امتیاز به ایران نیستم.
ایران خواهد دانست که «به زودی چه اتفاقی خواهد افتاد» پس از دیدار من با تیم امنیت ملی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/funhiphop/75296" target="_blank">📅 20:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75295">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الان وقتشه مکرون از گلشیفته به شیما کاتوزیان مووآن کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/75295" target="_blank">📅 20:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75294">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ به العربیه:  ما کار بزرگی انجام میدیم و نصرمن‌الله و فتح الغریب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/75294" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75293">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYJAccWV5xGCyFzVrR32AeqIEfEqOGaAQXUiDDZfwWqRcU_rgrwKqOnmRdm_CXb1uSABVn3bPscyRK986gk-TyEoMmanAZQ64NZH_eV_JPmdjrf193C1VVaXjGqBxQYkWwa1LgfslLRCFDT9mtzERuHONeLRHA1OSHdo5PVigCwuoFwHDn9lXzcPMKZQk68c12fHfKeRezCkFDGysmD_lMZnGNvQ6oRFyAYcmkJ5AWNmh3zpzTNlil_sbRUw2YLCO4ACBl1AUNCZVEiDdHu1rNpL1e_mYke0iutb3jiSbik2EgfDGbOztPo01_vZoiJ-az5z-9khyD2zh7HAOTDvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا ارزش خرید داره، هر بازی بیشتر از پنج گل میبینی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/funhiphop/75293" target="_blank">📅 19:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آکسیوس: یک مقام ارشد آمریکایی گفت پیشنهاد اخیر ایران برای توافق ناکافی است و هشدار داد در صورت عدم پیشرفت در مذاکرات، احتمال از سرگیری اقدامات نظامی وجود دارد. انتظار می‌رود ترامپ روز سه‌شنبه با مقامات ارشد امنیت ملی دیدار کند تا گزینه‌های نظامی ممکن را بررسی…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/75290" target="_blank">📅 18:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75289">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✈️
آکسیوس
👾
کاخ سفید پیشنهاد به‌روزشده ایران را بسیار کمتر از آنچه برای توافق لازم است می‌داند.
🔜
یک مقام ارشد آمریکایی آن را تنها شامل بهبودهای نمادین توصیف کرد، با زبان قوی‌تر درباره تعهد ایران به دنبال نکردن سلاح‌های هسته‌ای اما بدون تعهدات دقیق درباره…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/funhiphop/75289" target="_blank">📅 18:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75288">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✈️
آ
کسیوس
👾
کاخ سفید پیشنهاد به‌روزشده ایران را بسیار کمتر از آنچه برای توافق لازم است می‌داند.
🔜
یک مقام ارشد آمریکایی آن را تنها شامل بهبودهای نمادین توصیف کرد، با زبان قوی‌تر درباره تعهد ایران به دنبال نکردن سلاح‌های هسته‌ای اما بدون تعهدات دقیق درباره تعلیق غنی‌سازی اورانیوم یا انتقال ذخیره موجود اورانیوم بسیار غنی‌شده خود.
🔜
این مقام هشدار داد که اگر ایران از موضع خود کوتاه نیاید، آمریکا مجبور خواهد بود مذاکرات را «
از طریق بمب‌ها
» ادامه دهد و افزود: «
ما امروز در موقعیت بسیار جدی هستیم. فشار بر آنهاست که به شیوه درست پاسخگو باشند.
»
🔜
هیچ تسهیلات تحریمی بدون اقدام متقابل از سوی ایران اعطا نخواهد شد، این مقام افزود و گزارش‌های رسانه‌های دولتی ایران مبنی بر موافقت آمریکا با لغو تحریم‌های نفتی را رد کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/75288" target="_blank">📅 18:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75287">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بمب پشت بمب: آمریکایی‌ها باید دریابند که ایران به هیچ وجه با اینکه پایان جنگ در گرو تعهدات هسته‌ای باشد، موافقت نخواهد کرد. ایران درباره ضرورت پرداخت غرامت توسط آمریکاییها به دلیل تجاوز نظامی به ایران، بسیار جدی است.  اما آمریکایی‌ها با وجود سخن از چیزی به…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/funhiphop/75287" target="_blank">📅 18:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75286">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌شان از بین رفته و در ته دریا است، و نیروی هوایی‌شان دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود.
دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند.
آنها کاملاً دیوانه شده‌اند!!!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/funhiphop/75286" target="_blank">📅 18:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75282">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کان نیوز:
نتانیاهو امروز جلسه امنیتی محدودی با مقامات ارشد دفاعی و چند وزیر درباره ایران برگزار خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/funhiphop/75282" target="_blank">📅 18:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75280">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بمب جدید تسنیم: اختلافات اصلی ایران و آمریکا همچنان حل نشده باقی مانده است؛ منابع می‌گویند آمریکا هنوز خواسته‌های غیرواقعی دارد. یک منبع نزدیک به مذاکرات به تسنیم گفت ایران در پایان دادن به درگیری، بازگرداندن کامل دارایی‌های مسدود شده ایرانی و درخواست غرامت…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/75280" target="_blank">📅 18:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75279">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">العربیه: ایران در این پیشنهاد جدید خود خواستار آتش‌بس چندمرحله‌ای و بلندمدت است و همزمان بر بازگشایی تدریجی و ایمن تنگه هرمز تأکید دارد.  در این طرح همچنین از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/funhiphop/75279" target="_blank">📅 17:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75277">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">العربیه: ایران در این پیشنهاد جدید خود خواستار آتش‌بس چندمرحله‌ای و بلندمدت است و همزمان بر بازگشایی تدریجی و ایمن تنگه هرمز تأکید دارد.  در این طرح همچنین از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/funhiphop/75277" target="_blank">📅 17:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75276">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز:  آمریکا در مذاکرات نشان داده است که در برخی موارد انعطاف‌پذیری دارد، از جمله در محدودیت‌های مربوط به برنامه هسته‌ای ایران. با این حال، آمریکا تنها موافقت کرده است که ۲۵٪ از دارایی‌های مسدود شده ایران را در یک بازه زمانی مشخص…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/75276" target="_blank">📅 17:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75275">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDon Quixotet</strong></div>
<div class="tg-text">رویترز فیکه بخدا</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/funhiphop/75275" target="_blank">📅 17:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75274">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک منبع آمریکایی به الجزیره:  صبر رئیس‌جمهور ترامپ به دلیل عدم پیشرفت در رابطه با ایران در حال تمام شدن است. رئیس‌جمهور ترامپ تمایل دارد اقدام نظامی انجام دهد مگر اینکه ظرف چند روز چیزی از ایران دریافت کند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/75274" target="_blank">📅 17:37 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
