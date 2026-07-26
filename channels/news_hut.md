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
<img src="https://cdn4.telesco.pe/file/PYvkd-GTfp9RNpmKWmsuepLgvDaLAPwRDvz7YXofKsG_C-LMOf7PppC9eW_AR1JjDu1K_zN3hSYYsV9ZmGs0Yvd9t9vJtqDQ2kyyeehLKb3SxEHnC2DC1ZTBOhWV31OlZ2_VOJObeSwD7RND4WcFRmHN-6gImuHzvbII2IVMA4DCYaneKJmq-OCEsQ8rB9lZ77kIVRFKR3aBTMjCWrpe6RkuDQ9_D03xAY7anW1INRYqyVoWhQt-8sjCmR_XioTG0M8xRlyi6QyQhaxWppCN4PquuF7D9L3iiRnocQRSCwcc72X2cDpSFRp02KffArMwGsL_Si4hIyiD1LZatzbH-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 148K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 14:43:39</div>
<hr>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=NbvSKvRjnN_HwY-a8jtZWyDeSfKANY9kv1huz5KGbphcfVLwFPxE_3BT2cwqowx7Eb0D4vgY9Xk_ArsMpQ4TbFMKvqviI5VaeaGOC0LNd80fi2Gl8AP_0cy_HpPuC5I-drxN1XKYHIBjbNAMBLxhLavwa22snLqaC_GnBZFRpVoMcxsKFP4kl9yKvJ-y-Ye98Nb0o3zA0iZtzkgm6LvKkSHZdoN0ats_RO4IYcgjtXq40UwTNWhLlttsl9ZCgohtUWnZkSNN_JoFmNnTy2wM3vhp1e2BT5Gq4q8w-IxvOku8Jl_rnj_0qdRn0R_2_gJWn06rUMOcZXUmMehfzJrjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=NbvSKvRjnN_HwY-a8jtZWyDeSfKANY9kv1huz5KGbphcfVLwFPxE_3BT2cwqowx7Eb0D4vgY9Xk_ArsMpQ4TbFMKvqviI5VaeaGOC0LNd80fi2Gl8AP_0cy_HpPuC5I-drxN1XKYHIBjbNAMBLxhLavwa22snLqaC_GnBZFRpVoMcxsKFP4kl9yKvJ-y-Ye98Nb0o3zA0iZtzkgm6LvKkSHZdoN0ats_RO4IYcgjtXq40UwTNWhLlttsl9ZCgohtUWnZkSNN_JoFmNnTy2wM3vhp1e2BT5Gq4q8w-IxvOku8Jl_rnj_0qdRn0R_2_gJWn06rUMOcZXUmMehfzJrjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LHRd6ziU10MYZnjCkxjDvNuFiNRsOj-aOyCzAUrNjbvjUMQhaZZ84WLOxJHPEo7Uzx57X4NuPAyMhpycLadJLe16etp81qA49RuoCtMFXsZ2EQ0sjb_hAOyC3aOPpJprHuUPYIyw0XA8bnc-ZmEz4UdExTHcejfp_5wl-oU9F8yHBTS7Cv9_a78m8Xdn0tgzEOqI8iXLm2QUkJQFX-iPPakMEa3osK6eLUGzyo_sio5s7VuRzfPu9vQLHY-VMmclYr9Bgd-nH-OgVOTLkwZ_0conZDDkAC2ukaakWa7labGcCnqIiMiCwbSF1h4eTsQA9E_f8jTV-XFTZMsPicRGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VhM_LCqynRbZ266g7KnyCRJf15p8chELdYMfkhw7O-NrCFhIvTZnrZXaOmB8yCxUT-651pPxhDlBomOxB6vDR3MZZ3g-NciJK1f5yd40ZEuzige_0lmBbWmC7d1jFGbEG8x6_Xq5zT7yPmdhHXJ4mcS9H0x7cjnACicR-64aIgyxfg6LQ9g3QQtKszryCl5vO2-p5rh_Xf2EDXVJRd8ljP4P822trlz6lzQM6a-GPlf-3rU4DWTWgBIsnCeyXbYlWnoNNGTnOtN7WyV8vqMiZZA5fC6gOH4ZAxn4xm8FLGanscRTWdEVpvkdol6OxdmcQeFlL0QJhxBjYmbD8yXJvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuT63B1GKxsVNAKqRniCAOCIUaGABCPKioWq0veF0wpQxRwTHMm6yPBV0vdUTlHocifarYQ8ElQsUtVhu63bzxKlG-Z_7mfp5OgN5AaJ54_h4u7Cupl9rgFSjPAZxU6QtIbvb2mfwj_K6_9x7ZHcilwXNxuYBtTpvJk7gFPr5ACnYCP2drwcV-bDDfAIPEH7pdzpi5a_2GHx0NRlHcYJtVTJJ6gm7QejECQ6My_r1932nS6XVRD1g47NZH-n-SodnHdVZVy92kFiUtnGbm-BHW8VsX5aGGx3GdLnkB5aIoNtq4e4NRlpwcY32lGxZ3XcbMW7bLH0j9J8wN2RinIZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt8n_TpB0cFjFBi2s1PaMRRl7PeUTtpqBFH-tTkq0ukwrlfIKpSJxcmGN8y-huDKaIl8z1c6C81fUyKW8TVDbL0wRwS2GvXHXXPojazRy2RjXhMUYgpwUuZqg0OlzsAHF4YLDAR-I5IbhwIP8rZfNty-kmGKl9aYX_vlFNLMEilg7YouudwY9vBCPnHHdGClvdeWc61AjJwwY5IO-y2QAsL0mDL5-1NDDcijEN4vxhcQgmeEGeWt89siWnFBvwgMRCHWPUfWRmUEdat0O24bLGL2pfRSIYHWhWlw3PwNKr7T6BvBRu3F3BcwDVOBYnZ3wVV85UeV0FIWuubvnIQmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_grE6OHQBPvQvezozuJenYYGsYRXjuQknrzZPEc9mW5gvXTELXK_aSk-YtmRDlCjPIsst2tPyrdAJbInR1JWlIB3UvcdiKT8wUGxsA09eBBV-XHRhZyehHMmjUDfYlqQEQJKG_KsdC9Qb8ufsn4KCdU2EuVTn_KdEq8pmmSoUqv8U4ujFPyKYku8IKjEii_lBaFJvgfJ0p9aAWSJUjY0vi9Z2rcvjaNYOYTGmpRh09VE2543mmK4fnwnoiesIjP4TR5rjWdQuc6mALXba7Kgcq2d8wV0HjNT_vdDNCy_J5bWpw_VqKYtZzHBWfi5foN-eOGT8fP3E2Dvj7DsUcJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1C3-VgQcfcryqgOkebK_uQ365IIOulvJo-pLPGzmcngvq6gxp1Ex58Hfgta2j1xmSjLUHa_-E09v8344vGZhO2k5rDxbCwPLHG7lJ7aQqNZXYElPU-Lk0YA9GcJYyq8xMmN39iGmoEnE_tsIO1flK473XF3cPR-jqEERP3r7f2RaPP1-JejBJXklxqXGIa5eWLkMzzhJo9J9AE3xkElaN__iOA4Viec5x0uGRWfqGTP-JE8awT5hpXZ7pBrRUmpZdETrcqSmTZGuaJn13x6uWxiA-F_5SoeVuAp3SMnBSHp0lxNf4_LbSi39qte2zIazTLnqamE5MYVlB9VbEnb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUc1DqU0SAG3Uh48ed3v2uA0KRGQPwuHqVSNTxRri1oMwOgi8CNC6Ys20fKWryVrVCt1JGDJc2eXDvxQB3CiOIn5_qmiArDnVI0o3uN3db95SDRnjv0V_J3aO9B18yltNBgTNsz6syH56RvvFsmmWZiSJtZNTFAj5QhNdDPpZ9AN86vurG6ELLncSPKVcs8iy_sMabdUuSgjzeDQqvj79Pd5WO0hkhKkDu3w02m65vozczk0xQs4vay7TtG85eK3iI43-Gfx1fkzGmR1z1jWuy9ATegvdJPqZXEpzTl-xFu0TTVVk0gO4IyLsfmG1xvCBfHjRSuwsdzjJtOOwz3pOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT066vbXZVvUEEXkVWveOlNR1CjcIztnenLL73Jx_5aqK9L1rwJNA1QcvH6n-l5hugcFT1gwlAwM1I3pb_6RxXJaKr1IVErss292kWz2MBzw74qPDH3k2M7srEgKixJxCsiKQGbVkp65zkJQJUChV6Ri62ULHgC3oRoFJxPro0v2XCGp8ljK0hSCVRk04HUVmM_xiVPLaELvWEO7AD1wO5MQ6K50ER3wEuuUL6I9DzygDTR8AK6ZPhgQ0vQN__E51A7jn8pqF6BC11cZGpAeRhSBDKUbgAtq0hmtLHUEr9bM9TKGo449D0cQuXa0oYuWa8xxHoMQWLP2nB7eCi055Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=fV0cqwTaJGmTCtq7WR-KbgLmXp9cGNPn-TLr7L_PXnekZvkMT4T4tsrFPFxNhFBrOzS7MdrKJiE9sYnXMCf-M9rI_XY5zTS9lz6ofB0GfB9AxRldAp1Y1_NvkcTfB4Ytye8y8rlw3NKdTs1xe5M91oatpCLIW8pb_XoZUKDkRDHmJ_Gu3Q1-DbuQ2xK_K8vY59JkCb5iEiVAXpEE9uaZnzSRycuDqxZwMEbCEvRAMXsha3t7YmVgCHtRHKDjefLEIKCohjxEAKCzhArLvVwQeZq5PmlRENHRpBL-Uc3q7G0dCVB0BqxqazTdqwEVyFyA6h1QblotuwrzQ3_dyRbVww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=fV0cqwTaJGmTCtq7WR-KbgLmXp9cGNPn-TLr7L_PXnekZvkMT4T4tsrFPFxNhFBrOzS7MdrKJiE9sYnXMCf-M9rI_XY5zTS9lz6ofB0GfB9AxRldAp1Y1_NvkcTfB4Ytye8y8rlw3NKdTs1xe5M91oatpCLIW8pb_XoZUKDkRDHmJ_Gu3Q1-DbuQ2xK_K8vY59JkCb5iEiVAXpEE9uaZnzSRycuDqxZwMEbCEvRAMXsha3t7YmVgCHtRHKDjefLEIKCohjxEAKCzhArLvVwQeZq5PmlRENHRpBL-Uc3q7G0dCVB0BqxqazTdqwEVyFyA6h1QblotuwrzQ3_dyRbVww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxxS86Te4H1EutF0Ly8bwwYyp-gHoOPdqka1mKR9IAfq0gVvtFtqW6J_0Kp-4zMyLlhRvZRs1mZcvBYm-l1-rgSKq5UGs0FhZ30MDxSq_tYG9H1c7AIWSZkjiMltjhdZy8hbgt3m1bAmll1QOC_lhQ9dEZ04UdeX00IUM10sxUQX-CwioiIcTrNXSUsflvDcHPwcS0pVtgH-UaH7cx2xgxJFk_7EowM00WSpNi5d7fygb-D5YguuYtKTYcFA0pYqCXNwA915GM-ue0o80mb6zDh-LGMFOOGKdIVbgLzXk-Mi5h0pZwFsAs-Jweui1kEaZoVc9f_XXdrBnHXMr-KJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=aIetjiKWkgaC8-jnSBmbD-Tq_rdUPveNXTafUpyJQ2foNQbD1wtgeMbx-p8n_W881ZfSMTSiUe_gMUlvTaPGnTltUQuUx4VCcz_6aLscxjLjgo9pf8QB2f8pFgHNgy6u3nQIoCUI_sBmPEBhGKdjz75yX_bqdZlhVzWgHJ4izCU3_moP8yVGZ0wlh64yyG56KGD9jBjt9jvoHWFX5FvM4Tbw0pWsyaQVPCm_i2JkGU2JAObisqmiq94jc2prRoSKrdj-AYM4niQ6v160jXbYxEHY7eQt27JMGpBta_GETS9XstgxJdbFKQvHdEyBIqu5Rv3U6lJkFQCHUyDe7NL3Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=aIetjiKWkgaC8-jnSBmbD-Tq_rdUPveNXTafUpyJQ2foNQbD1wtgeMbx-p8n_W881ZfSMTSiUe_gMUlvTaPGnTltUQuUx4VCcz_6aLscxjLjgo9pf8QB2f8pFgHNgy6u3nQIoCUI_sBmPEBhGKdjz75yX_bqdZlhVzWgHJ4izCU3_moP8yVGZ0wlh64yyG56KGD9jBjt9jvoHWFX5FvM4Tbw0pWsyaQVPCm_i2JkGU2JAObisqmiq94jc2prRoSKrdj-AYM4niQ6v160jXbYxEHY7eQt27JMGpBta_GETS9XstgxJdbFKQvHdEyBIqu5Rv3U6lJkFQCHUyDe7NL3Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=v2l5VT1Fw6GT2lWcIrklddhwOfiXGNKMbAuTVHx9ONqRKT44vcq-EUZb9c5pGfJXUgQiWZNL4rdo7oc-qllh304PysufcLRZh8BLCes50Fgvei7l7Rvpn0hPqsK4SfVIOe6R-FHFl8p1REs_DCa74qD-2wiwH2FTP9WnrPADFJ3VJLO3yoB7U0SwaJHa9xYCOda8TXHqx-lOrXRTAWY24_3yFSa3dticHKWAtDLOWntQuoPle85bVU8E0j4skLGcOYKz6faWoulqu-SxwvZt5RtETiJYOzD9rwo6tGMRkXJw0CyTVDlq1SdhhPRCnwO2TFjCQUykfQ3OWdPt2U4i0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=v2l5VT1Fw6GT2lWcIrklddhwOfiXGNKMbAuTVHx9ONqRKT44vcq-EUZb9c5pGfJXUgQiWZNL4rdo7oc-qllh304PysufcLRZh8BLCes50Fgvei7l7Rvpn0hPqsK4SfVIOe6R-FHFl8p1REs_DCa74qD-2wiwH2FTP9WnrPADFJ3VJLO3yoB7U0SwaJHa9xYCOda8TXHqx-lOrXRTAWY24_3yFSa3dticHKWAtDLOWntQuoPle85bVU8E0j4skLGcOYKz6faWoulqu-SxwvZt5RtETiJYOzD9rwo6tGMRkXJw0CyTVDlq1SdhhPRCnwO2TFjCQUykfQ3OWdPt2U4i0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkbHWKJa-luOZglAZWVJXrK70lZ5bhyoYeWBsM3j00kDqKKsqUSeT5nEDA2YgrvFEnx5pLTnvPEKsEYqWT41Dq92NOmUreeQ0Lq7OyErnTxMrdGdAeJNj2g860ZaDKgd_Gr2wVa59iGoGJP6_pUDUcYGcZdd2UbzKbz37re1MLKZwctgWnbOPRQ_1mbfrjOLfkj2DmyMhry5NeTSXC4-ZRa-6rSoVVX8jAPkdy_JmQG3KLtS47sbtLviic_GFjOtH0yMvn6TpItm0LMCS_nFZKqvtiNCK_i8RVlFZ5UFnKE-FMRLn1n__GFUh5DjiT9hvKYWPf4vXWyZYuqqPdXDRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=OZzYL2nT4F0qU3pUg9gZCFx44Bp6WfTTdtClriN8zHMvGiPkDogyAcSVs9PkowKWbelKVerzJCgqfbIzmS4G7OW11SnJj_Lr-qQ1PAV-_peEPA-Fewnf08Rsjfi0Zz6BGeA4ztGvi5u5yJ172uPy3f0GD43iPlcRACs17VeuZgV0Mvx0_xikdLPft4gfweUv9rf76Pk1XSWRNwRE-Tpx5Ffwz9ckYU030rLy9VE8GnOZgC15DNbMryu7Z14ynZd21bsgt1wFroHVXVZw8qilDHmHUtLk3i3JzsoVhVkw7Iu2T9-8lfY4hv3zknGN5CnNZufipYg-B-yg_vV0czrNFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=OZzYL2nT4F0qU3pUg9gZCFx44Bp6WfTTdtClriN8zHMvGiPkDogyAcSVs9PkowKWbelKVerzJCgqfbIzmS4G7OW11SnJj_Lr-qQ1PAV-_peEPA-Fewnf08Rsjfi0Zz6BGeA4ztGvi5u5yJ172uPy3f0GD43iPlcRACs17VeuZgV0Mvx0_xikdLPft4gfweUv9rf76Pk1XSWRNwRE-Tpx5Ffwz9ckYU030rLy9VE8GnOZgC15DNbMryu7Z14ynZd21bsgt1wFroHVXVZw8qilDHmHUtLk3i3JzsoVhVkw7Iu2T9-8lfY4hv3zknGN5CnNZufipYg-B-yg_vV0czrNFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=gcjejWI7EIOF0HcZ2Xav2FV97Xx7ZsBMW063zKkOYm1cAwbkBx98BNiHOjD7ItyU1U-bEDDDN130C73ND5xEBWHEOikYBkq9sUAsyV4UMHHnD8R0oqhV9lAzRwWwfOQKC33U8Xbx4EMB-0VFp4HRzjgWDOFrmDFHYgg_X2LkMGtF2mtY8zD2wxLqPeRkogbK_MpeQeMNOTDmgqx3_1PLFTwIN_oSF8B4PE6huBXi5VsjTpmf1dEBeh6lSPK7Cz1B6EYLppmocGJm7rIs3MHK_vvWrp-x_7wB6xDZyXLO8ZDt06rqyFXPMtbiaJjrc1yIMmOqBF8QjiAjv-DeoSa3ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=gcjejWI7EIOF0HcZ2Xav2FV97Xx7ZsBMW063zKkOYm1cAwbkBx98BNiHOjD7ItyU1U-bEDDDN130C73ND5xEBWHEOikYBkq9sUAsyV4UMHHnD8R0oqhV9lAzRwWwfOQKC33U8Xbx4EMB-0VFp4HRzjgWDOFrmDFHYgg_X2LkMGtF2mtY8zD2wxLqPeRkogbK_MpeQeMNOTDmgqx3_1PLFTwIN_oSF8B4PE6huBXi5VsjTpmf1dEBeh6lSPK7Cz1B6EYLppmocGJm7rIs3MHK_vvWrp-x_7wB6xDZyXLO8ZDt06rqyFXPMtbiaJjrc1yIMmOqBF8QjiAjv-DeoSa3ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=pzUXOgo7wDNeTmTA9wQZQninYHAhwX6WE-AyibMayIxCIXnt8NHSLsz8D_VNoi5NM5j6WLepAY40BprhuqYJY4o2Hw0rsrNBB5d2uHmWtlzg-Iy4UA_bFVo9PVTmWVs1Cle3uqhxiQaygAOKJSi5H056_da33f3c4kkjoRAnixeRdmco1uuCwLaaWZN7tJOakkj267Jcfg2cwy_w144O3AwlqW_n9epi3XHXNBoWxHYoH_zgWViV-5SRby732dgadXNjG80tHp1DqvyqMwCihtM5kAuFI1UtMmW3HEivSP8loKE0E8S1CiP39t3NLjc6a9t8SoETDrQ50aAD6bGrIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=pzUXOgo7wDNeTmTA9wQZQninYHAhwX6WE-AyibMayIxCIXnt8NHSLsz8D_VNoi5NM5j6WLepAY40BprhuqYJY4o2Hw0rsrNBB5d2uHmWtlzg-Iy4UA_bFVo9PVTmWVs1Cle3uqhxiQaygAOKJSi5H056_da33f3c4kkjoRAnixeRdmco1uuCwLaaWZN7tJOakkj267Jcfg2cwy_w144O3AwlqW_n9epi3XHXNBoWxHYoH_zgWViV-5SRby732dgadXNjG80tHp1DqvyqMwCihtM5kAuFI1UtMmW3HEivSP8loKE0E8S1CiP39t3NLjc6a9t8SoETDrQ50aAD6bGrIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=gbkVirzRYwHa71Gf5VXyXLv-H32PWdXBSwM94_ZecxL5OgnWV1DcYh49THbdRe3aGtT8bSmaRychkTqKJ7V1rwX7-ZFE9AbZMlFlU79mQfXd4yplTIxqe1Dok78GPxFj3blgDISpWaSxNfRssgcr42U4YvwwaDMgaj8RXiyjvO1fhgyn25d4A-9nCQosnQg3_aQ7fLkGKesaJGaWz6ODJPzyFfDgCGaAtLZuK7YDVsCYsR__NYflGke1lufmg9Pj2IrROqL2VqMbYKzlc8S-TIOdBMvojDb6yvTXnRaKFCtvpfpz1Ulhs_3t3gdLz44nNfeOQzAY_LJ0_V_NrydlWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=gbkVirzRYwHa71Gf5VXyXLv-H32PWdXBSwM94_ZecxL5OgnWV1DcYh49THbdRe3aGtT8bSmaRychkTqKJ7V1rwX7-ZFE9AbZMlFlU79mQfXd4yplTIxqe1Dok78GPxFj3blgDISpWaSxNfRssgcr42U4YvwwaDMgaj8RXiyjvO1fhgyn25d4A-9nCQosnQg3_aQ7fLkGKesaJGaWz6ODJPzyFfDgCGaAtLZuK7YDVsCYsR__NYflGke1lufmg9Pj2IrROqL2VqMbYKzlc8S-TIOdBMvojDb6yvTXnRaKFCtvpfpz1Ulhs_3t3gdLz44nNfeOQzAY_LJ0_V_NrydlWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtgS6H_D2zTMeVTg8EOpJCwSI3JuHrDjHvlezm5CJinT-0eMZlkTZTLDEjS5Kbhb20gb7RxnvyFtIIsWHM9Kvw_H4hv3MWgxpQg67H5c7eiyeKuyxnehAkU5AdDgmqpLOT9esaGaMtWqhkp7k6n6LwNcLVmCCpmO-HFH1JK346QbxKkR9DiJ4-lOuReaQqKTfM-A32DU4BB16WmKQ7YQZDqwb2vnJoPxzsksvlbyyaAAaInzRuFgST4UbALz6dBF5aYRzP9weoH2BrdshHIHbz-N2d10yWYOVaKO4Oeu6Mm676eLYqWnfC9BMxtxE_Tll3LUHUZzC93fSb8zPMmgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=kwTOvqoYvTBKp2CasuCpuN8VLa_PPGOA01_I8z-9qsh3wOZCcxv5ojruLon2AVHaMdmVzerSKu0TCsBUq-x75-N-pfG7jyrOhvkpoL4rB37IdM0JuKx4e5zZcb8pytvamgjn7BacNF992Aw6EyY_yE7JcgHy5TEQ_WgGasK0nZ2QLYlHZYC3g7IqVjUQirBtjgLA3-rBV-kIyvPHi2sHpmKWnL1GzxrAzrUdqx7uwURMG_RvMUOU2ph1OLXKgIGg7H3jVevmQpcKh2wTv0wv3pkHi95bXE2iptcxigA4-L9eVyxQ61IAWjraKHUaqkM7zpK5fa9FQZUa9mx7HPz0Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=kwTOvqoYvTBKp2CasuCpuN8VLa_PPGOA01_I8z-9qsh3wOZCcxv5ojruLon2AVHaMdmVzerSKu0TCsBUq-x75-N-pfG7jyrOhvkpoL4rB37IdM0JuKx4e5zZcb8pytvamgjn7BacNF992Aw6EyY_yE7JcgHy5TEQ_WgGasK0nZ2QLYlHZYC3g7IqVjUQirBtjgLA3-rBV-kIyvPHi2sHpmKWnL1GzxrAzrUdqx7uwURMG_RvMUOU2ph1OLXKgIGg7H3jVevmQpcKh2wTv0wv3pkHi95bXE2iptcxigA4-L9eVyxQ61IAWjraKHUaqkM7zpK5fa9FQZUa9mx7HPz0Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2szNFt3yZS6q4XuWZ86UFvhpj_P02dbBDYdoPRe8n_fEz1Z-K-z43q8X_LUZhGMlktIhULOowuh9FgJzds2i_kh-iuXroemL1Q7fFBlNI4Bth6RTBcN2AfgKIQQXsg2T6f45bk_xXfM5bllhq7ahHeVCyrxfVj3ZFgWZk3fH8oI98lS2NtJ35gBSd3MegpPkDmnHu4oZsD9hjReFyT3sWdXCUbQ6LMpSOuFZHOkvz-IVOVxpvkeqebUN5xl-vvBfKUHTe72ip9S7e8gQWYUnWg0mSltO2ftqX8W1i1HJDON4hA3Gdp7VFXur6oE2HKK5It23EvUQyHfZlnpgt4gCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=AxJdVeV0VDtI_mtFSzjn4UdHRtqLfHd9YM-7gizjWT-2UIa_O4EEWB09YVLm535ZOiYyzMxHFftA0DINy1WIUSRngpM-9W94SQhLmAxPy-7go8U4zwW6okP6j33XvSvGWUcXGP9LH-87aaJMBAzER2_eTH_E1NLfzig3UEhQzafl6kWj4ws5a-EX460BOIj0w6mYcWgaFFppdqQmzasqsnnZErhXMgOhNlkvA0jLNbCQBm-q8U05b1eYuLd1ZrjQvmGXfGINhXby1KLR8RtVY44_mv7tBvjLwy6dmCVE5xGPWW6ntlINehpchjTGzRci5KKBII43nsEKmFs_jj8eUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=AxJdVeV0VDtI_mtFSzjn4UdHRtqLfHd9YM-7gizjWT-2UIa_O4EEWB09YVLm535ZOiYyzMxHFftA0DINy1WIUSRngpM-9W94SQhLmAxPy-7go8U4zwW6okP6j33XvSvGWUcXGP9LH-87aaJMBAzER2_eTH_E1NLfzig3UEhQzafl6kWj4ws5a-EX460BOIj0w6mYcWgaFFppdqQmzasqsnnZErhXMgOhNlkvA0jLNbCQBm-q8U05b1eYuLd1ZrjQvmGXfGINhXby1KLR8RtVY44_mv7tBvjLwy6dmCVE5xGPWW6ntlINehpchjTGzRci5KKBII43nsEKmFs_jj8eUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=HGfh1jrtv2i1mybO3EFDHt44rai5KbsIjxdGVaGiVF54L5_W-W2bzFkaAaNf0UjqPOXzBvM7Pir3Qere9SkaUkJhvh-3sCvCC-6r_1f_61B4KacmbNYXzNZkqr3uSa7JbVnBTV2zyu1iS6Fg2ULrzQFj9KkVa447z7VAoRZAz14i90qMIyLgmKHbfrSsm5gsZKOJHDGVI9momHBPoCDjY4imMyUCrRrHGU6LYvK7N5YsvzKj5JwLyAULCIL2nSRLHpsGed0QjCxXZvDHQ7c-xavv_POA8Wba9uQeUzpkHSFQPCqAqZZejucLWPS0RCnHtyKyXo_pK-LDOjqcIoKjbDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=HGfh1jrtv2i1mybO3EFDHt44rai5KbsIjxdGVaGiVF54L5_W-W2bzFkaAaNf0UjqPOXzBvM7Pir3Qere9SkaUkJhvh-3sCvCC-6r_1f_61B4KacmbNYXzNZkqr3uSa7JbVnBTV2zyu1iS6Fg2ULrzQFj9KkVa447z7VAoRZAz14i90qMIyLgmKHbfrSsm5gsZKOJHDGVI9momHBPoCDjY4imMyUCrRrHGU6LYvK7N5YsvzKj5JwLyAULCIL2nSRLHpsGed0QjCxXZvDHQ7c-xavv_POA8Wba9uQeUzpkHSFQPCqAqZZejucLWPS0RCnHtyKyXo_pK-LDOjqcIoKjbDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=bLvIgmQ4p-hfy3PrpqgLbnn_HJBKNkP1MQLMSpucb1P_48ezLOpX0l_XcwpxoxTbC6dr4JOan0xBcpr-Aaa9MeAkYEk8T2ED9yzpc4HpNjQYsKpd9ivvPGiW0zoW83-DgcFrNNKaLh8HlbmPa01z_iklZlx-ItgaxIxAtpNmW4GYxTM9Xu3Uei7vZMeEWcyjDav5VMO8HsNa6rPECQj2dnLueK2yA5IR6Rr_snEupPjGUNMgAU5N5zLMB077ZrnT5QGvYkU3rQUoc1AGzKaAwpSgwmLEHxhzz3hDdsdgq-RljF8bGeI4Whsy39gHJczBv3BITucB1OLDw_qI1prysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=bLvIgmQ4p-hfy3PrpqgLbnn_HJBKNkP1MQLMSpucb1P_48ezLOpX0l_XcwpxoxTbC6dr4JOan0xBcpr-Aaa9MeAkYEk8T2ED9yzpc4HpNjQYsKpd9ivvPGiW0zoW83-DgcFrNNKaLh8HlbmPa01z_iklZlx-ItgaxIxAtpNmW4GYxTM9Xu3Uei7vZMeEWcyjDav5VMO8HsNa6rPECQj2dnLueK2yA5IR6Rr_snEupPjGUNMgAU5N5zLMB077ZrnT5QGvYkU3rQUoc1AGzKaAwpSgwmLEHxhzz3hDdsdgq-RljF8bGeI4Whsy39gHJczBv3BITucB1OLDw_qI1prysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=V8SRidtcp9cwSdU35h1zUO7qQ7MApPchwcAzY02vY71dUJyi9bfnAdFmzpEuZ70KEcHWi3POhXeaHTEb2adhHFa1uvDi3WJkYO3rj5xPFIopv1j20LM41pXQ62pyAXO-I2D1wZO41nM9z0l_UX3ebFz_LpPIsaOJFblAARfUD73PVBy7hEmk3SDHS6GeQ5jPZyJyGGaO-rBNRy02CIJiqXI_L83uTwwXKFTHdMWffdQd-vqUm-Lm-eZsOKmLHVA83-n-RJ9v1GxdWxvF_FCOqD9F082D05kmTJVLp1Fc5yZKenbh0MbMtJ8fbSbbumQYHCFcuRqL43TKNmiOy1fBRmeX7dB67Lvs9UK2_8mJ3QKe8KLCCsS1KB9ztMrxYdOvdfk74_Yz-WbV3mgna2wN0qNQlgfbo1Yp0PLAhBdBbEL9xUZDsamKTn571m9umRyvkUTSOQOTC7_0wLxEEQbmQucRWQR_CiLbdUxMZy8iAuJfWRX32qvLjs6mL-472lk69QPGx3p551RfC14eXsP4I_uf8QbdCHACdnst0HV2nKJI1aZEEyRftXL2RiW8kHmBcDgnaSzTGke6TuusVl57WDRlAVyexNrZdUGGYeVC6Ggjl_tz9JS2-i5GUx2ByN0sVZcKcUxLr3VW3yZIeSOANwLDtAifdwzMfZ6x7Y9b91c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=V8SRidtcp9cwSdU35h1zUO7qQ7MApPchwcAzY02vY71dUJyi9bfnAdFmzpEuZ70KEcHWi3POhXeaHTEb2adhHFa1uvDi3WJkYO3rj5xPFIopv1j20LM41pXQ62pyAXO-I2D1wZO41nM9z0l_UX3ebFz_LpPIsaOJFblAARfUD73PVBy7hEmk3SDHS6GeQ5jPZyJyGGaO-rBNRy02CIJiqXI_L83uTwwXKFTHdMWffdQd-vqUm-Lm-eZsOKmLHVA83-n-RJ9v1GxdWxvF_FCOqD9F082D05kmTJVLp1Fc5yZKenbh0MbMtJ8fbSbbumQYHCFcuRqL43TKNmiOy1fBRmeX7dB67Lvs9UK2_8mJ3QKe8KLCCsS1KB9ztMrxYdOvdfk74_Yz-WbV3mgna2wN0qNQlgfbo1Yp0PLAhBdBbEL9xUZDsamKTn571m9umRyvkUTSOQOTC7_0wLxEEQbmQucRWQR_CiLbdUxMZy8iAuJfWRX32qvLjs6mL-472lk69QPGx3p551RfC14eXsP4I_uf8QbdCHACdnst0HV2nKJI1aZEEyRftXL2RiW8kHmBcDgnaSzTGke6TuusVl57WDRlAVyexNrZdUGGYeVC6Ggjl_tz9JS2-i5GUx2ByN0sVZcKcUxLr3VW3yZIeSOANwLDtAifdwzMfZ6x7Y9b91c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_r6oTqFm4xPBTHlITJEkrKn8Pri1RVkK8HIvA1NJgwEvcV0mNL12lvYm2nIOHXRvxZwden06TDw3jrhMLMxb934apjSdtOAJpBnrPdinu76i0yFBribZ_yIiPhhDuVzO4oJPnJId3rTM2tK75EzuTvrq78AU3s6edxocKl-njILVpS8q9dl1ODfqW5xGFaqx_eQ308uC2yKf2aIc6EV5YdyWumZjQmCUi2hAVdWdhcvOdgbtBDpWDGx2xYVQWIi5IaWzdRxu_bpSmgN68yWhMNxAaGgF1M2QSbUNyEbeCwWKKylArDoIHX1YIkAbCKmn5EDeyLxy0Emy8LwdkAIjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=CqlVNOYUPkKVVWDihIA-FfUUsAAW-zbjd4tVzh73IQ61N8HHrgbPoIbHH5EkMcaOWz8z2qG8QWu5rS_122EEY3b6uliXvI083fk1tWSy3UydW8nTqDZF_JQTpUHQnKwRt6b8JI2GgjFFhTe8o_Xjiojgn5v6DR4BiEnBhiEov-3B5ciGW_ob65pVlGxgRxyVfhyNV01A7lG83FDHV5Ttg2z_VxKzMiih7QAdSrk99ABHf72XTH8yOQRdiPP3nsoKV2anJJRuTck_O2kufIPMnyinBRsCdxj3O6-ZJj-L44QDvxWfQb7dEEFmKScWL--XreklPvVW_AVaYNhW1Pegxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=CqlVNOYUPkKVVWDihIA-FfUUsAAW-zbjd4tVzh73IQ61N8HHrgbPoIbHH5EkMcaOWz8z2qG8QWu5rS_122EEY3b6uliXvI083fk1tWSy3UydW8nTqDZF_JQTpUHQnKwRt6b8JI2GgjFFhTe8o_Xjiojgn5v6DR4BiEnBhiEov-3B5ciGW_ob65pVlGxgRxyVfhyNV01A7lG83FDHV5Ttg2z_VxKzMiih7QAdSrk99ABHf72XTH8yOQRdiPP3nsoKV2anJJRuTck_O2kufIPMnyinBRsCdxj3O6-ZJj-L44QDvxWfQb7dEEFmKScWL--XreklPvVW_AVaYNhW1Pegxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ-5dGzxzQhAfjSLdtkN-r9HK1_d04srbcjYNudenlV7F7PUOqNAm4-Mq9nG_ZeM4xKyTAomiTfH3Fhe7JBooXGlSk12GFJWcrelCw7hXpnTwoutAlJmm2gHsrFKURgOP4PZjc7eIkDy91CsqHH_ZYpNVQdXk-qlsnpvI34iikg8yd4MoeplITEjHRj3e8SA8-5ddcFMl14dh2ENg9QvytYbOGt9zlz4sqkLxhjcc717_ur1vYqfyignAMey7T7Wz6ryaqjUe3jgV1Kd4R0NJEidckCm677XS2pd1Stj0t3DQDKQyEIB3ejzEKxm7YeIfkG8JeLpXiJm_JDCWOxdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTPc7b53QgxDKYTaYjSoRSVoNNfJSbNPHxmZsXq0AL3-kfQvwSaE5zWLPWMKLG-FK13M5PdD_BI3ehTvUqo12F_v3Mq-Swhxb2CydkT6r_FN_LPKZUUVb6YJwJLijXnCDaOTeEelIS2SlyJJJSmhK-NyzK2DDVTF6JffX4GaAelMx_U8RDN1mw3aPTAjW_i_k5YocttKXAJ1JL4-wIONjsE6TblH3uNow4lIa6kbG0MG87b1x-tI9VbpTdO5c91Cgo73p-BjVOwsDPHTzfRdwuwSHaDwbqBp0FWQS57Rc_9fERxdgmlR-Uc4kS2BJ6poY0nTSzoRs8ZwaRtF5hxYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2SPKCwx8bq8kf5qjf3luZX-4QC1ZEA3Yht0ZMpPcqY8rHsVh6ERsusd--t3dSee17GQqhQn1IZuOTGmVCn69PUCIxltEAdML9_6x26hA-oPF4rv-kSiJnIIZEdU54n26iKNFX1jRHrS0Vx4glRGJvNWdPKZCVspZ0CSiX5GCrU27fXWSoH_vS4wqCZUgq8hjs3krXAFFbcrVUbd9Z9JJrBwl4478yKDNRMZ5-wNVBgRCmMQ51yBo1adU-FyjzM0L85N3ZEczkVXXhzSQ7vDzVFYGXcT0M3gHI5jDT99MFZ9a0HKRTzZuzMmmNoRKYzi1JBhBXSE_TRekhPHPMU4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5CZv-ZR1dZJXCsD7bQFKGoXQcadOkAwhWg7vSw--kfRFZCU4QBT4u7XSb0diR097dkQ8gW_ZqErUYkOn5cGrUbJrcRRH0LGkdC3R8Zom8tHIlkXlf9gz7HCrBR1jiPt66iRImE8WJjiLCkxs4_hTz-F3r_3gNIfrs6uRzCQP-VKZjrMp7p-swmkLWciCJs_ZBU8gHDneJkmhA02YxjAfxjADd8DK6_dOV9gG3t2L65e8PJrTDmRPdEcozdSaENAjaqQzv9w9WaoeE8k4Y5Jk-ScVTd_-DDBmbOIYTzmiRZ0zjOIvOdWN0ZvOGD2ESzrfIXe7csoAFPbT87c2z9sPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vG_Hd5tTsEU5vXgJQrKCjsiQXQ6bMyRiuF8FjNlgRScRr-noBuhTOFgbdmT_Or3iNkJvvHzQt5fbNUIAnIL8blikopRZmgUzvRz1t_1u_gQYXrxOgeC93CXuRcB1RYDbuyeGKqqJ1Es1N3gsGrRtuUgEMJ5khif-KDR1TkfjGL9xBSrhMvufzeoqzADPAqdu7WGlLeAavPPf_1vE9thVdN3WrnBDHHGWkmEUTiQSjC1EnHpfjzWMDwsgM__JEK5In9NowZ-BwS73z-zVKdUM6c7T9TmUnAYZZse76B3ZOHNOwFDGjVv-7GRDFjFCcd9Cx1dHEDmIsrB089x_AgBTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIavqW_v8G28_Ug67EMqzW4BHTOz-ZDtUpugUZPlSIW53NwndcBnhe8s1qyp2RKlC-pjteUXoN0m7kUH6Iw1h77Ikd6R0dlTaYgWm0psOeHYsWHjF4mc-qlG54l6J-R50gnUQ4SDp2RNi--od8jxikMloPA6rw9wTLUklutHzS_As4h9SsZfiR9_lwSyeV4Bu_a4-tQznHqY03Xv0nLIcDYxahd1rRvmPe064I5_HyqkdUpEla6WnJoP-oVsXdz-jMEvnz1pD_hMPVUuOJw7uvscPHsHCZ6maYYcMKfMjg6LrFqkv2z5_68SLCsufLxlGOqj4BO-useHh1GMJg9tew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=fxGAOPKnnwbB8k8VRSHZfSFBz1wQ7MxlYAjQLmFl0co9zvS0S19IeR3Snl92NldClLd1L2X0eZpo6yuOAXVNTwKdpBXo5bPUTSp-KpEN4fpG-UJqIscGkcZugobLiy2WpHDVlnV0FtBY7kPxWezhU-NySKmRmE7cVEuZ6FyvpXohcoQYItIole3va3icVYQFNLiNfbUfccSRuut8jE9HTbMd5gQw8FPldyK7xUtMWhXEXdKmqthq6hQ7tsLGSCOVxPnL9RkLog02mo9MLbzSy-3dRSkUyl2FZuBHtPJfjcq_ghbYeLhRW0bwy2rdH1UaQ5ZuyISRkP37co4laWePSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=fxGAOPKnnwbB8k8VRSHZfSFBz1wQ7MxlYAjQLmFl0co9zvS0S19IeR3Snl92NldClLd1L2X0eZpo6yuOAXVNTwKdpBXo5bPUTSp-KpEN4fpG-UJqIscGkcZugobLiy2WpHDVlnV0FtBY7kPxWezhU-NySKmRmE7cVEuZ6FyvpXohcoQYItIole3va3icVYQFNLiNfbUfccSRuut8jE9HTbMd5gQw8FPldyK7xUtMWhXEXdKmqthq6hQ7tsLGSCOVxPnL9RkLog02mo9MLbzSy-3dRSkUyl2FZuBHtPJfjcq_ghbYeLhRW0bwy2rdH1UaQ5ZuyISRkP37co4laWePSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=ExuVAwnnxVp0zd1oDYi_W6RUQTF4IsZ5aGbLMjviCzUocDWwWZILhVFMhqAThyNl3wV6_EgohGcmN_yzF0wNAqGW_c2WO88ICcdO9IQQbPIFqAc8DkBJISfTaU_3v1K8o-JAgFQxoXqw06RuOj5PjFljJlR3d5TnTiSAFcDx0wmxXapcQknZAHQzAa-aIm-AFGieSf75z37qJLv3s8e5qHcSRKnVbt85_rTaTeOlvPhkdko9suyAGNNfHBS_OZFPJDEaDX9dqH338nXGejdSK6kInhI2900QEe6cmh4qkJN5ZrzKr4WFmRslZ1Yl8-iifyFllfU1p19w30Cm3_P0fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=ExuVAwnnxVp0zd1oDYi_W6RUQTF4IsZ5aGbLMjviCzUocDWwWZILhVFMhqAThyNl3wV6_EgohGcmN_yzF0wNAqGW_c2WO88ICcdO9IQQbPIFqAc8DkBJISfTaU_3v1K8o-JAgFQxoXqw06RuOj5PjFljJlR3d5TnTiSAFcDx0wmxXapcQknZAHQzAa-aIm-AFGieSf75z37qJLv3s8e5qHcSRKnVbt85_rTaTeOlvPhkdko9suyAGNNfHBS_OZFPJDEaDX9dqH338nXGejdSK6kInhI2900QEe6cmh4qkJN5ZrzKr4WFmRslZ1Yl8-iifyFllfU1p19w30Cm3_P0fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=GOTAwdvRFdNkrcvmnXVnVRo-wWPE4b8UMiuFIMmKorqFeGTLu0G44gWAkiZOBmWm0gVQ1YsHBCuDLS1NSZ9x3-V0_4owHiZU1SaqwCicwwZyzI7XwGjgP5qf27C0zLIxsvDsOxEYQWSEC6HlsQeys5hBhOOZEdvddIowxq3HJdgprIm09dEI26eCNequVZhn956KJ-qg1SKMteu_v1Oa3qKYVjhJqnrkWwrNRDt4Xotqf4omjHZsLtLtE9M54hmNuRygF3LuVIJ9AXGfdauKiM-fo39cD309imFO5kblJiJeiXs61e-dSb3mAOLCnyjx4AKY3E_dbghUrogi2xr3Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=GOTAwdvRFdNkrcvmnXVnVRo-wWPE4b8UMiuFIMmKorqFeGTLu0G44gWAkiZOBmWm0gVQ1YsHBCuDLS1NSZ9x3-V0_4owHiZU1SaqwCicwwZyzI7XwGjgP5qf27C0zLIxsvDsOxEYQWSEC6HlsQeys5hBhOOZEdvddIowxq3HJdgprIm09dEI26eCNequVZhn956KJ-qg1SKMteu_v1Oa3qKYVjhJqnrkWwrNRDt4Xotqf4omjHZsLtLtE9M54hmNuRygF3LuVIJ9AXGfdauKiM-fo39cD309imFO5kblJiJeiXs61e-dSb3mAOLCnyjx4AKY3E_dbghUrogi2xr3Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=t1XEsojTyYD439XMoFsBfPH_LlbxhF5-VxNSt814E8DygNIOPdbY8kwZDKcd_W4mBQFpVGai9P8IblKOC3JraplAKkJoFCAz0tT4wFdSIHZcN3HhEGCIYtfv-mFhMhkpfYk3dxB_5WSj8cxad-b2nYimNnOUUtiLLJa8vZ4Q1qJWLQ3gOtATUZI9BO7txNQFJdrGykMKRWTzpjNaCcqlNx2GV8UlG9VlfwevV3T_efvacbOGbTyL-QQZz_YVsjXEhN3z-ePlHtlP2zMWQhZkbCY8VFJwTGoCilMANx5Ja_c8ER4FrUrHZD4hV5LzXow5pAWVTjNrOX3YGrl7ecuIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=t1XEsojTyYD439XMoFsBfPH_LlbxhF5-VxNSt814E8DygNIOPdbY8kwZDKcd_W4mBQFpVGai9P8IblKOC3JraplAKkJoFCAz0tT4wFdSIHZcN3HhEGCIYtfv-mFhMhkpfYk3dxB_5WSj8cxad-b2nYimNnOUUtiLLJa8vZ4Q1qJWLQ3gOtATUZI9BO7txNQFJdrGykMKRWTzpjNaCcqlNx2GV8UlG9VlfwevV3T_efvacbOGbTyL-QQZz_YVsjXEhN3z-ePlHtlP2zMWQhZkbCY8VFJwTGoCilMANx5Ja_c8ER4FrUrHZD4hV5LzXow5pAWVTjNrOX3YGrl7ecuIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=Laf2JeLjNEcm7lGf_5OnnRKtjD3P90f2ROo0IqoXiEIhXgqXUubgQhHlDCGu9KQlR9CtEAIIgtY6UFLqAalRBrh7GvibMpV0vWE9xFrl34RoyzUCuOC4_Qu9akaDUjEZxddlVbOoVeizcf9ZbKBZPG7t2gnOZkty0DEc7CeZ_8xEAhXkvrlDBHQp2YOWrW76V6C4yqYLQStacXX1xBLIibuAxvVtjoE8EXyE_9uB23heVigVVWQwwRE_0D367o0Ews0-tcBjNavRG8Ucpr5wf5HsgHls7JiBnXy9TqeacNVKfhXtsmhFSoO-a1Uow9hMvsM_LJDf4IbLbihIp7X1BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=Laf2JeLjNEcm7lGf_5OnnRKtjD3P90f2ROo0IqoXiEIhXgqXUubgQhHlDCGu9KQlR9CtEAIIgtY6UFLqAalRBrh7GvibMpV0vWE9xFrl34RoyzUCuOC4_Qu9akaDUjEZxddlVbOoVeizcf9ZbKBZPG7t2gnOZkty0DEc7CeZ_8xEAhXkvrlDBHQp2YOWrW76V6C4yqYLQStacXX1xBLIibuAxvVtjoE8EXyE_9uB23heVigVVWQwwRE_0D367o0Ews0-tcBjNavRG8Ucpr5wf5HsgHls7JiBnXy9TqeacNVKfhXtsmhFSoO-a1Uow9hMvsM_LJDf4IbLbihIp7X1BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=IkNMi29BYiGv0RfCyCwAsLP81zepeEgCiO9PFkl2TEKSe69OkYLT3rmNtCU4RhIK9rMR_elJgyxPTB3W2oCnOKeYP7ZyWV9bs3B4_gARvKFxDHcizrGPE_vS15d9cjBsxVXbNWafrU7SWjJiZLq8I6SQqFWmbASn9kxME18_HIAdZkwyzIWqv_l5-EbykV35re-y8jjKIZfzR9E57csUPhYBfNCHthGctjSbmIOuCD0o0njSse0VHMTQFh2FvjRaE3u5hpNTONcA9Qbtj8haaep4IFp6UebXrdLZGZTZKQ2dQZrFgjDiYdHbASsSGJ07takgxzs6kxR3OchcL-teAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=IkNMi29BYiGv0RfCyCwAsLP81zepeEgCiO9PFkl2TEKSe69OkYLT3rmNtCU4RhIK9rMR_elJgyxPTB3W2oCnOKeYP7ZyWV9bs3B4_gARvKFxDHcizrGPE_vS15d9cjBsxVXbNWafrU7SWjJiZLq8I6SQqFWmbASn9kxME18_HIAdZkwyzIWqv_l5-EbykV35re-y8jjKIZfzR9E57csUPhYBfNCHthGctjSbmIOuCD0o0njSse0VHMTQFh2FvjRaE3u5hpNTONcA9Qbtj8haaep4IFp6UebXrdLZGZTZKQ2dQZrFgjDiYdHbASsSGJ07takgxzs6kxR3OchcL-teAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DySS2o3wuCXVP6JyEXR9YiaYtxI6MoKL2tw-mpQ52-VVUQPB7ImmgNrmMOdHDpIb4Gmsckj0S3dc7Sntp0IUiLXTMvdjk85gfwS_rlSw8b9DDc35-NcIAfN_tKDJB_BWXmwy5p-qg81kuu0sNJlGzQDDxDx4h0ct-0F7IhuS160iDI6ZN4U-j6ZUegqFo9wShay2QFIKnZy0xgpgUZ4u0NivOC45hjHV6DJI3TQI1kRqHNCGeOliKDifboxSggyl4SUkdKKGaaA9rzVSZZfhGGzIf57HnQyTNujBte-ZO9wOUeGy1F3QTuxuyeU6w-Wu80fI7RKX-TlBS7ciAzKMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbGfW0xH6P1Fz1H0yzI58DSaw0i4CNw8zRrVT7Y-kJxZOVZthnVNSS_NkreBm68irfeidxqaja40GzN6bMTk1FxaRJlD1nPBJPz6Gg_WDoQH8jsN5hClqdPR77vp9N0MtZ9-eXLZCBEHrHwbep6mlHFe_p3krJ4_Cg6UzSF3mKlsnqKj2V92tO0iWqEaHj83vdwltx5jKp5xe2Kbu2iPCjMh9dtBxNYkC0v_fZmPKk_a5eTHBeNH1UQA7WS0NdD7O4id65kjV1x0MVMpfX0Yl48Z2n-gZEBfJVCMaw5RGJ9MNPxhv94hjyq_7eHiCfLcOZV-fMDzRTsRSc0Y978fXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNnpspKX2nfGnRmp4bCShjlQb0m85sqhXwuUP5T-SmtPOrAbWHrA35NHTxbOg8dNAGeaYDz0YlE_W8VOMnK9I4o_SwpfgU3JxmqVNt_hfATSlnCtbjWofgwg11VhJMTk-6X_tHq_hgOvS6Et_hetfe4hwgeVBeyGSiEdsjCIrEje_ev0RkrMJ_QH6qTSxujpO8sBSjVXYTgSAVAsTJANxEz_wLS6kNsFQeYvGqgvqdqjWp4ejOe6DWwg1LO8LNxti01WMD4yPoKWuzIcJecUSnjNEpOKr2JhkZMAnMT7CR6xjsT082OQ1Mv3CNl-NFEYmhiXNUH0RUjXSd7bHxXGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=MjpGYafs2IdoM8yMtjxKlnC7bxA8-kn2tohG9arry8IPA3o-25qJCgFISwZpTC2PMZsfCyYVkOLMjyhgbSMw-_bYvfauwJegYhpeLaYGJH1jHowLU4qmMGJZTTeLYuMu8RLPDVDTjqHrTdhE5VWQquElZRxhzupunyzh72I5F_X2-6rWrhxjjdX0WqlNSmfxr4Os_rpUXssUN3gB2Cr6NrTHeBfaiApFaknQ5aCMYAzG_2IBN-vs7S9FtlPfnU_kuPZGCZWkNG1a48y9OR6Wg1B9-D2Wj83VEU_c-Iz5dthd0GIEkXslFg7q3Eq9OHnPz72BqyFyPxb-RoxHm31BSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=MjpGYafs2IdoM8yMtjxKlnC7bxA8-kn2tohG9arry8IPA3o-25qJCgFISwZpTC2PMZsfCyYVkOLMjyhgbSMw-_bYvfauwJegYhpeLaYGJH1jHowLU4qmMGJZTTeLYuMu8RLPDVDTjqHrTdhE5VWQquElZRxhzupunyzh72I5F_X2-6rWrhxjjdX0WqlNSmfxr4Os_rpUXssUN3gB2Cr6NrTHeBfaiApFaknQ5aCMYAzG_2IBN-vs7S9FtlPfnU_kuPZGCZWkNG1a48y9OR6Wg1B9-D2Wj83VEU_c-Iz5dthd0GIEkXslFg7q3Eq9OHnPz72BqyFyPxb-RoxHm31BSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ipellfv4RF2irIu-JZLHdjqASV49CuMlx0r4EgbkVPcWfdeC4WRwX9HfW19fjqVdRSIt-XILmumWdkaLslht3CLS9m60-_S7lQ-hWKGLfpNp-RU1GWNw5etWnzJTPjTjPmovG9iSNf9fCmzZgC3MIXFE5xWU5e0vhgl-CIlQpYCgoJofhBqZFmWg-Iw6Y_LwzNWwGVfpbs-ozBBNmcHijYTsOsbAjiluGktnaTDtrCoMme0ITyD1l0fgCB7Rqi_2ljsUFlyrWQqMZQk_Rw9NAYfGsEJvk9sBI4cEwcWoGOBD5BwCSJVR3nr0JsRVgB4Gi8QS6S1N0-FXicVVivOB1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbPfEIIDoywum14XpBuHDDErLwlW-gW_UnTLkXvwmbPGDzo_TpI5jozZ-I21GR_QVFLsj0xrVFo_3GsGtni8EzAo6k6Fn85UieaHQprm418vqp70mEaJAbG5t63MaPmijPIu8eIZSQcVcshWw4PT8ZE0wFOWQ1SfRF5nYRD32bU2fiwHpEr_8oUhPf4dTl45n_MVPa3RIUpRAxGtmdE8uRyXaS5Lwu-tLRgTB7jWNAy3Ih-8Yt5HS2x-zgHtlok2wMoXfiY1W2CSfv6YluTLaLYDxl4gqyyITGpBaNfXW4K4Dja3hfIkvDf6tool9Hc0YOsPdc4xunPTuTgtmoxsig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=mwaWZQpI3g_zR5fUNtc0UGbtGqEe_GUCAwm86qESeUiUqolTvqPqztU_gUa41UEvAYIjN19mEnih81mhfzVqumeBSjBzXnVY_bC2EcjG4qNqscAAcHq1D-WbhOwEaDNzIKNtZkdQYqRtnvx57xRj6JE-zgAaAkg5BMJBH4prvccrP8X6jIKfcpgzykEnuf0tCsDGt3Oyg_-pfsNlUqI57WzQtHoZqmilx2hOTjwiMvL0d1k9D8sgXhUMUjr0--X6CgRveTiwNnDtiaC3Cdmmrt5_SCuq4EIRWe63Ulx0PnhYNkYJSS_eEtuHQ6TCsTgc63mwu_EyE4zB4lyVFZq3Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=mwaWZQpI3g_zR5fUNtc0UGbtGqEe_GUCAwm86qESeUiUqolTvqPqztU_gUa41UEvAYIjN19mEnih81mhfzVqumeBSjBzXnVY_bC2EcjG4qNqscAAcHq1D-WbhOwEaDNzIKNtZkdQYqRtnvx57xRj6JE-zgAaAkg5BMJBH4prvccrP8X6jIKfcpgzykEnuf0tCsDGt3Oyg_-pfsNlUqI57WzQtHoZqmilx2hOTjwiMvL0d1k9D8sgXhUMUjr0--X6CgRveTiwNnDtiaC3Cdmmrt5_SCuq4EIRWe63Ulx0PnhYNkYJSS_eEtuHQ6TCsTgc63mwu_EyE4zB4lyVFZq3Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFYt1W-FkGXO6CqxYQtsCrjO281fz8G-fkid1JQ5t7OALLXdaCpRaBYWiwk6Zh4wA1Imvv3VB_j5D2DWIiTxnmaqPK68jji1epYl6Aoj-jREBsj7lksOfd9fMfD7CRsVglw5C66HwANmLvFho_DEIgWfYkRcor4N7kZbhptDhTIS_uxM4oIPEzy4kzIKd1nBjLexA5Sj_DaIow6zfU4IWqIcPcSCsWkgyfI82pRUmckWqkZxu4WJDxFbRgAzpQVehv77lkGhk6O3HFulcC_lWdmKQz9l2TTbag5qdgAw5kG1ZqPJwaut7oabq3nrjwZUCqK5RwO1GrZazs0kzrYjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGb7WTj_1oK3MCQNzBb03hKuWc9zGyNorHeGTQcIoUuklCV9rGOfdTUm5qe9PLkgc5LoQs9UaQwf5AlU9yCB6I3fGAAkxi-dE3jj3LpWEPQZOVQ_fgsHkX6QufezcEWl7TkMNZ525qj1I3M6GJ294X_woFaNPxUAYcG9d9i8N1k4Mxoizw3We7_2Vi8qn8PLTLTo9Y6lotT6FB8DN1PWzCdDdx6PrgOGbUa3Be2iDdrgc_ZbPt6kx_XF93l2Lfeuj0Q9P5unFiReK0iCxlOv7QNyEdQ409YFA_lJglcLQc5FI94572dt3c4_3c_JDwyv-f61lcbONEBJuGp5o-OvHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkeSnYFsD86AodAQZSXAaPdfnQlSBeT97eHwQMOvEgOtO1q80_irekuTvRnbansmGncVECJB2xPfPsaQ9jVz0nQ7SOrXcmu2UVgmzbgpHBzgtD0HcyunUOhJ_d_SLSS20MUVYy788HaE4tSLFQAVdrAMIc-hW5TNAtffWfYJo8Ibqd0cdd-m4_FkfQtc6Q2CKGpePeUgode9YvZO9-_uiy5I8WyOHGGrnjmBg5Oz8_iI0QdsBuSg1_amJlxzXuJKkb6lC-Z7IVIH56g652dg0SsspnEYqcTqDGXL2vPhdC8kbDJIYGVsFd8MMqZf2Igsd6LWerQqSKGPoWovddo__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9FMS-SCsWF0LnwFpL0rGY9WU5VvWxmIxsCar4wu1ccXS_l91_iLW-Ap9L1Lpo6iFAsShDjXWiLRUe1yi6UuNUPBaECYGUxP8_I4aQzpdKByg5Cp8iwApJOR8tEQztpAxwky_72UhUG-yLCfssI_bV0gdDeqlFHGkM1-6FZG2qQ_A9BlEyqv5c3bmXLH_XXXTPyFXCVFsysu9hX24uKebFnI4oF2mcctmhcwmIa7pU9152VRW7rL4M9gyZitMWb0mtb0xaTRdKU8aDBvBLUb8niOtp_DSwqP6SlRTPZ8lSLzhjIan5s7St_-aueNutfS1DtB6YDdfvt_UKxzmprEPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=sgQrPZ8gSSCiLP1P800wCEE96dVPBTNYOYEqD9AwX0_zCg7u9R9_soergj5eOZ2LF_njzz9JEARx5vnXfjfOzWc544iktc3qgnNM6LORikbDMPzYqZgHFBrXtGL5pW8OvsPn9l95dCS1Q69N5z71F9wf5va80oHaew_ZqcC5uSS680hkn7FO9h1QIf82L01lkp4F1WXU7VcVdf86IctQIDDtbZNBQUfFveKOFFPsYV-UXBCD8jpaHnUrgvWwL8G1v3-HlPCGy8ASnw9GZ1s2sD6pSZkNIFVsFkcb-T18sHdj_lBGOzt4yxLkKhW4r2LU3HWdyZXuob41C-BkFqJNDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=sgQrPZ8gSSCiLP1P800wCEE96dVPBTNYOYEqD9AwX0_zCg7u9R9_soergj5eOZ2LF_njzz9JEARx5vnXfjfOzWc544iktc3qgnNM6LORikbDMPzYqZgHFBrXtGL5pW8OvsPn9l95dCS1Q69N5z71F9wf5va80oHaew_ZqcC5uSS680hkn7FO9h1QIf82L01lkp4F1WXU7VcVdf86IctQIDDtbZNBQUfFveKOFFPsYV-UXBCD8jpaHnUrgvWwL8G1v3-HlPCGy8ASnw9GZ1s2sD6pSZkNIFVsFkcb-T18sHdj_lBGOzt4yxLkKhW4r2LU3HWdyZXuob41C-BkFqJNDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=pnmzJTGp50fvf8XBzj9mg-aL3BGTJRsw-apsV9dE4fyrSKtF9lXHiO7GkXq5bdvPZJ2EQfXnWmVqbtTT348RAN_Fpzaxt1crchsqhdMwjKYC6vI4-uV0xYtBsAime_JDbcJz-Fqf37q0TQpetQs13fIF2GgTfCBHdFn1dbFQYJids7hy6x-N2vgOTEf7PnmTDvT97vPT7uDpTZAH0aS2saocpGKzP5tmZiig4msiit1ZHrzNRaDUck76i_aUa0cWp3h2O55h5otsChokF4Fk-GcMhRzj3ljZVzgosBXzRbkxM7HZ62ONgsqukK26OjPy6eGrB4OpX0YLYg054oMiqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=pnmzJTGp50fvf8XBzj9mg-aL3BGTJRsw-apsV9dE4fyrSKtF9lXHiO7GkXq5bdvPZJ2EQfXnWmVqbtTT348RAN_Fpzaxt1crchsqhdMwjKYC6vI4-uV0xYtBsAime_JDbcJz-Fqf37q0TQpetQs13fIF2GgTfCBHdFn1dbFQYJids7hy6x-N2vgOTEf7PnmTDvT97vPT7uDpTZAH0aS2saocpGKzP5tmZiig4msiit1ZHrzNRaDUck76i_aUa0cWp3h2O55h5otsChokF4Fk-GcMhRzj3ljZVzgosBXzRbkxM7HZ62ONgsqukK26OjPy6eGrB4OpX0YLYg054oMiqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvUlupcnCCM9M_cctbxeyeJS_aTu_pthXwo7Ne6NjrVl81WF4_F4DPjHDVEes6oKA-REAr3_ckSJAvj00uPA5B0LIPUJyvxWhBG66dpEIm4TIn94krG1_7r4YaKPzyQQUMwe3Kr7h5ax8AJwrj2H2CtqbNr85b5orw4R_s4j_RFVP7BzzEKAR02siQf_NyHlVwGcb-EjT0-lHvwyTUWESEtQc04cdwop2SE3KfNLylJGqcISB-lEDM2GyCpdtzqPbIO2ouj7LR42H_AQPtZ-KiT45ldj2EOwt2kSrFekVoUBDpIhvpUhB6Ei0pSbpMIdUSewZe86A9AacsEL_yAdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=J5ZMLFmFP0_U-DzT9x11x6wZVVm0UhWgDGg_q3feqnlRVBL1v9El6-25b6B00or9V9CiJgN9WsTFYyypd52P-_vVGnXmOWvFQDIoWbjlhL6MwzqFN2oSJ3FMwC0JzU1xHxnMoWFIhRnWXg_xLIukpAh6Qmi9QKuAeFlkUvztIvaShxiQ6M60ojwfXkXLszzBt9wZi3iS0eb2En8vF9iiUq2WD-fVY9qm431107bNq8uxpt_d-CKCsiX3lUCagrLpRt3XHVchWdTo00p4nut92jxpImTuD0pieWvASWLFPmPL9ujUsF4qyu-hTeJP9Wb7ViF4NkItH8ydEhicxoclFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=J5ZMLFmFP0_U-DzT9x11x6wZVVm0UhWgDGg_q3feqnlRVBL1v9El6-25b6B00or9V9CiJgN9WsTFYyypd52P-_vVGnXmOWvFQDIoWbjlhL6MwzqFN2oSJ3FMwC0JzU1xHxnMoWFIhRnWXg_xLIukpAh6Qmi9QKuAeFlkUvztIvaShxiQ6M60ojwfXkXLszzBt9wZi3iS0eb2En8vF9iiUq2WD-fVY9qm431107bNq8uxpt_d-CKCsiX3lUCagrLpRt3XHVchWdTo00p4nut92jxpImTuD0pieWvASWLFPmPL9ujUsF4qyu-hTeJP9Wb7ViF4NkItH8ydEhicxoclFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=Xir3ZTt3jprm8VQIDXtvOjflvRYJ8BLPLGVLMOlHfv6eDml5h6f3RgbB0shhXvPP9RjVV0nbYqr8bDs6PTEiuj9NsMsHRx6s8p7Tmf6srUKUV1UHkmoNJcivSkOIdjE8L-Z4Ix0Arx8Y8OjV8Ic9Gh61YtSGdVLz3fxB8Tz3ztJoh6ZIpFmLCNYagpkYlwbVCI-BuC7M9LxiRv2LUc4H_tJJHKUBEQ1PKMQMhnCkOvbMpajWUjBQwqg5KrzAJIqB_hDpZxUy57ZAoL-MwE1v3_j_hLwUeF_GDhu31zgAOo6LXu6A6O73DHiaz-CwaMVNrwzfRzw2M8RzkWNheNtfMEBj6Ch6bd4QzKQzLUQe4f5tOg5770IpNLR7ZdqdFndswV35vd7He-u9lopGFk48DdEMg6d_KtUDCCbRMM1Y-w4ezG5DtVh1CA5bwe6qB-Y0jEXudPo3Htu9mHJr4ZGVP3YaEm_KNEOId7jhEVScv1E3px0ye55B4Ydpv-bPz9ukMnU530k8OcLmx4sHFFKckUN617cmfvpVud6GKFQH6US-4dMaHLYrMQeAFgcn5T4O-dCpOCglXrN_saW-vItx71z78SArhOrrTT28lZHp0NMT73S5vFqeqSa2sXJxO39r3t2YioESPjl1vyf9t96lGniByatSkBgtfqDVRlFrkF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=Xir3ZTt3jprm8VQIDXtvOjflvRYJ8BLPLGVLMOlHfv6eDml5h6f3RgbB0shhXvPP9RjVV0nbYqr8bDs6PTEiuj9NsMsHRx6s8p7Tmf6srUKUV1UHkmoNJcivSkOIdjE8L-Z4Ix0Arx8Y8OjV8Ic9Gh61YtSGdVLz3fxB8Tz3ztJoh6ZIpFmLCNYagpkYlwbVCI-BuC7M9LxiRv2LUc4H_tJJHKUBEQ1PKMQMhnCkOvbMpajWUjBQwqg5KrzAJIqB_hDpZxUy57ZAoL-MwE1v3_j_hLwUeF_GDhu31zgAOo6LXu6A6O73DHiaz-CwaMVNrwzfRzw2M8RzkWNheNtfMEBj6Ch6bd4QzKQzLUQe4f5tOg5770IpNLR7ZdqdFndswV35vd7He-u9lopGFk48DdEMg6d_KtUDCCbRMM1Y-w4ezG5DtVh1CA5bwe6qB-Y0jEXudPo3Htu9mHJr4ZGVP3YaEm_KNEOId7jhEVScv1E3px0ye55B4Ydpv-bPz9ukMnU530k8OcLmx4sHFFKckUN617cmfvpVud6GKFQH6US-4dMaHLYrMQeAFgcn5T4O-dCpOCglXrN_saW-vItx71z78SArhOrrTT28lZHp0NMT73S5vFqeqSa2sXJxO39r3t2YioESPjl1vyf9t96lGniByatSkBgtfqDVRlFrkF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Urnsx6fxnUb6q8PISREYo9vH_Ep1dpcGQ9pOGkrsn5hYky-uuQ-y5zedpFdlW5IqRFqUpepJgTsEPGUEWgycmli5Q9V7h-Y0sQDtC23Z2Qp0SMR57-_yWvaZf8PnMeno7BCW7xMy_0sSqy5SFd75S-RLatwMN67MFC_yolaollKc9aEOCxIW-aYMDqJ7m88doOXpsdHWhvsDroEdh0GlpCxGI19_JcrrIYujYGuinxhTJaeU5kOBAPfXX3_RGDQGpQjfgBDc4So189zAr2tdzh3__tLmacoKYC73omc2OfveQhgR6xQXDjeQ9jvHsRYrBdHlPeJsBp0n_VuGO2uBkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCQyKyGDF8TlwtuHb2GDkbEcVgncqr80vbnUUCQjDJI0iUPAQHNVf-GGKm7A0Pwi5IbT1iNMqz_LFfSd4092qbSR4R_E9QX2CSFV9VtaNXTDL_XLtii-eQn7F8MHQzJPpEXe5KZE_UNE_WFAivlKMCX0YFlK72LdxOko5DRp2jTONyXDCTPnopgJ3wA9dZsjYocQEpEUWkuTUPsicHzLKrucKmV8od1_zLSIr03mTMpiU3BhGS4QJM5D84BHHUy7M9qZedwZGh7d_ybSdFCl8y5Hf_vhT5e-wo2pnr3X_d6DBnnH3lJkAGaXz8uUuxoLm6hhZlL7UKE9Lz4tEiankA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2cvz5dDMXMBBuQQB8BS3TqsbI1T7H5IZ_tSP6VF8vid718-V3OHs5MO8KGuj4LOQeWt-s7iGsi5LOTwOlwivFm-CUKB4-OLcQvwh1wNz-5OALcpKhxtEOfLcNy7rvPAWPXRhQevTbJbb8yRrJar3Lu5SbWdd0de-z_hcP5Gk2cKOWtli_72F5PElUyr2ZhRZLZ8fW3yYQDgazNkB5jnlcyAwG6Ss5VZ-Gfn6H-1XrJu4W0k1Lj2OS9bWrgDAuUsuM_TfkEoijTiAFki6rWZqNlt_aa5TpSDmp0a0uIfugDF0xNr3jXmkjLfD-99cJpwQOFwuMK_fVbziqs5WOEIeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYdTL8RIUEKuiVcXV98pZtqUTFOpwmtAIolj2-P7PNtFaDGHKYlj5Q4bxxED8LPBFTDvlJ_TzbpjNzgUKsBGOMNaX1KSdAf4TfrxcqrJgJyEUcs40M_sfQgZsFQRZZDIO6-D8qzaRWge5AHQu62M7LlY3DGhwHDDj8mf4uJqfVWqsKUP28wLmhhvN-rldf1uROcmjf__lYplBKED0xm7C0yrMJoeAPE6TW6sqGQEhVAz1TeuwgGf89yQM5fkb8pYzvWS15X5Cy8FTcSnZZ1SCkV_Gc5appmAWqotNHfVZQGvD1jOTodZ8jrpW6rBz194qMIY-zpEZDROuP02gjUQIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=YHjpCO23aeNseI_luJQmhU1_WOmpPGMQDqNwrEmGTy8DtMdyP88gFbijj7RDzUgil6GKHn2GdGH-f_-wXBAV7Mav_WM5sOPGqiwNIOKiNmGzdL4Putym_jjieKSQ2HSC1dJwcmweg--8KUvG8mB6SoI8oUQcKFQp8PIrtG09oLlUR_nm_f_OwF6w1eGouIfV1xqgttyfnW2fqb5DjrFw31LOYC9f-ITpqjheAYUxXp-SM85KyEt5WqH5Bo8gnh0SdOZ_CuFf-pfuYtDul0x7wYOYVI-qvq5K8y_aB_FqVPSh-WsLhhSin9_xlIihWLBmrsFOnml06i5mc8z1oekwJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=YHjpCO23aeNseI_luJQmhU1_WOmpPGMQDqNwrEmGTy8DtMdyP88gFbijj7RDzUgil6GKHn2GdGH-f_-wXBAV7Mav_WM5sOPGqiwNIOKiNmGzdL4Putym_jjieKSQ2HSC1dJwcmweg--8KUvG8mB6SoI8oUQcKFQp8PIrtG09oLlUR_nm_f_OwF6w1eGouIfV1xqgttyfnW2fqb5DjrFw31LOYC9f-ITpqjheAYUxXp-SM85KyEt5WqH5Bo8gnh0SdOZ_CuFf-pfuYtDul0x7wYOYVI-qvq5K8y_aB_FqVPSh-WsLhhSin9_xlIihWLBmrsFOnml06i5mc8z1oekwJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyqiudctbDMcONDd3gT0RgULRujVn_M8fxx-b0Q43TG2lmuF40hbe5ifqIHJUh7R2vJs0P-q5LQNaa_bGzcN94kM0tgdr4R1iHfZb4S0k6R9R2fRQywIf7FPDdwXowveLK1q65UXmt2uLefkFI14x6K10h9KtjVaYD68OFSNPMBWayxSCSfdaMv1w3p3lL1jw1lE2MnGt3wVZdNFJjhtVfkxVKcVVHn-QJzHoQBfbwJxhROg-pddQZwjgIumxLS5pnc1EFp0x1NiPzyhW5aPZl-wUVzWBTAXA-EtPnPTW7tTrNxGQtTr3bWYg-3EcKaoO78neVBPY-uwhLIPpi1Tww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0srVUqBY9dzyUX2dcOGSoR87YlQFBoCREKrIaVMPOz408tGPxFks10C9ciImpO2E_YatQB9_U7A8U_vdqWj2E2ufkFU3wpiBZpVbTYGFlmWVi3oBIid3djTIdWHFAybVwljnxYw11xwPEpPVXLjRy95rfM5-OidsI8FHGVIa8jBNDbcpqxbETvLEdeYMAKmjVmOiz8GBuz5sZ7ghXUcIEZOvT1_mZ30NMOgPcEuQT0EqOc8BnIj3NRZBM582wBRICWXZrjAz2jhvl09fFNVL-BQRoPrCE9wsChVLSMY-kQ2WN_ywBPHwt0WOrnaz55ECK-FKsW1nDP0324lOh6_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=uEi3YxC6pArnaIjBXKVbHn5MmuHO6QQu9_pbBil0hK6A4VXND9ON01nUbTNRK0_SaGAHFSxqLZjgJboXntKjJfqVO0CRhyAkZJOR2YcNSgMNDlyfqRXvavTTJwd1lzmmAeHUnx4iFUWHMD1YaE6xssPjaj_MBZkD3o-I17sSvS6yE5iiOlQPraBqMW2AK3S1Sha9e1zA4H70v6oc6fraQheIYQ_ZlxRbNd1HX91FI5BG5zYnJeI7x-zCP3two8UjNQskKm7EjjPFTiPoAiDODVGcMMMw01HBt0cJTH17XyWEcnRlOkcYrW-AKd3v1ttHmEhWds4UjKXAZ7EEFyUHRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=uEi3YxC6pArnaIjBXKVbHn5MmuHO6QQu9_pbBil0hK6A4VXND9ON01nUbTNRK0_SaGAHFSxqLZjgJboXntKjJfqVO0CRhyAkZJOR2YcNSgMNDlyfqRXvavTTJwd1lzmmAeHUnx4iFUWHMD1YaE6xssPjaj_MBZkD3o-I17sSvS6yE5iiOlQPraBqMW2AK3S1Sha9e1zA4H70v6oc6fraQheIYQ_ZlxRbNd1HX91FI5BG5zYnJeI7x-zCP3two8UjNQskKm7EjjPFTiPoAiDODVGcMMMw01HBt0cJTH17XyWEcnRlOkcYrW-AKd3v1ttHmEhWds4UjKXAZ7EEFyUHRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=SmpfkFW5RjiDwZC_wAXvcZANUTaj7l9OR2OrD-54oNqLVqEJbju9-T3VrA3gVXzE_x74rygO7Rb-waoVUa2TUcge1F9D2lOvF4Zki0K3n_eFclPnH8ZjZpIq0lDcUdGnzxamhfZoehzImzVvUMGsNd6EEoPrdHYQcS26gIDbQyPpr9xZr_wJaKJN4ftERRsjaV5qVFmRcimDw90RwWbJxUrNCQxVSaaaZVdJ4tUagowOJMDBXBfC0JJPzK6exocdl289NplyE8qcDhvzKg7PSSknp6Azm4y0KXMbFojL1fiDxWne4V_4w6NhYLyOxBVPByJ05NpxkFLkcdIpMEwfmg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=SmpfkFW5RjiDwZC_wAXvcZANUTaj7l9OR2OrD-54oNqLVqEJbju9-T3VrA3gVXzE_x74rygO7Rb-waoVUa2TUcge1F9D2lOvF4Zki0K3n_eFclPnH8ZjZpIq0lDcUdGnzxamhfZoehzImzVvUMGsNd6EEoPrdHYQcS26gIDbQyPpr9xZr_wJaKJN4ftERRsjaV5qVFmRcimDw90RwWbJxUrNCQxVSaaaZVdJ4tUagowOJMDBXBfC0JJPzK6exocdl289NplyE8qcDhvzKg7PSSknp6Azm4y0KXMbFojL1fiDxWne4V_4w6NhYLyOxBVPByJ05NpxkFLkcdIpMEwfmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=uEdeiyMd-0dym0-iuDv8wcm9cD0hnliWkhLLFZi-Nmz3JY7CRVR0W8K5Otn5WuiQHAEPADhwK6VtF5_cymnkA5Gm-NzMjr-YrS7N_nt0FBJpWkrWKEeGOqHZ4dMEFMaJXbEIBntAYjSJR3H_Qpgcyh671FOGZsKUvZVGQpuPUzRfYJ7Scd4YUl9Nz555El9XxBr5LaZkfSInBvAigHoEdo57K5gJ6kiLwvuzjyrcQP3bVq5UZcIIMjjGLlu-GARaIuR-GdURNNTM3dRXX8EiLBEa26GX16Kmtu5rIW2tU8gzQK9OIch9zY6OpTxs84SfzD8ydguXtpXXeCa7FVi6A4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=uEdeiyMd-0dym0-iuDv8wcm9cD0hnliWkhLLFZi-Nmz3JY7CRVR0W8K5Otn5WuiQHAEPADhwK6VtF5_cymnkA5Gm-NzMjr-YrS7N_nt0FBJpWkrWKEeGOqHZ4dMEFMaJXbEIBntAYjSJR3H_Qpgcyh671FOGZsKUvZVGQpuPUzRfYJ7Scd4YUl9Nz555El9XxBr5LaZkfSInBvAigHoEdo57K5gJ6kiLwvuzjyrcQP3bVq5UZcIIMjjGLlu-GARaIuR-GdURNNTM3dRXX8EiLBEa26GX16Kmtu5rIW2tU8gzQK9OIch9zY6OpTxs84SfzD8ydguXtpXXeCa7FVi6A4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=f9n5Kok-6dU_4Ltxi33tHwzSpZSFlfKid_PlSYEt5Sf1Yv-okKj3WKbl3v2nfNYZ83NCatQALqae6N1MVXkQpEfKACXECgeVltT94boWELFqgCcKnlHJ6CcEYzCh1RnqgkXx1XoV91LsJ_Ikj80kTDhmvttdJtarsoy-3ZmXDkWFRodfFvjzkrKIEZIC0yc9LgHihBGUvsFesvbZDB015UVkgW4p3E8Mco4EILf4VkQXPhIbUhos7Ll9bEO7RB3f8kcRWDTkH2Aatcr_MD1PehR7KANa37jYj3z9bMJ7OzJckRbvAHWUonP2vxZtygZlwMUJPCBcl4INDzZiVnLUKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=f9n5Kok-6dU_4Ltxi33tHwzSpZSFlfKid_PlSYEt5Sf1Yv-okKj3WKbl3v2nfNYZ83NCatQALqae6N1MVXkQpEfKACXECgeVltT94boWELFqgCcKnlHJ6CcEYzCh1RnqgkXx1XoV91LsJ_Ikj80kTDhmvttdJtarsoy-3ZmXDkWFRodfFvjzkrKIEZIC0yc9LgHihBGUvsFesvbZDB015UVkgW4p3E8Mco4EILf4VkQXPhIbUhos7Ll9bEO7RB3f8kcRWDTkH2Aatcr_MD1PehR7KANa37jYj3z9bMJ7OzJckRbvAHWUonP2vxZtygZlwMUJPCBcl4INDzZiVnLUKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=FHtm3MMdf-qXi0CrmSWGOsCTwDscBLUsqH2zjp1wV54Fj8ZPwk_kqihUAtq9hYjoXd07a1NMHAot_Nl20zutoaP0gDydBZn_0Lh27jdhlE_CxKaRfpwwXHmSlyzbsqpD5Ko4VTYrP_0LlyfxcEbWotK5C6b885K03T6K_nfIVTPvp4le4T2FTZPfqIlnIsJN54PGlDwD9vBLxTszW0r7VH8ESFfqqOwnW5gWozmhVHR2ZjqcWvgQ3q59Yu-QnWw-Q1RuT5CeYGwq2wmS1_Qwil005zdAGMEUmdvPCyAFQqGeEQwIGtfed0b265_rfZinbtkN1wyZ48hLIeeGOileaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=FHtm3MMdf-qXi0CrmSWGOsCTwDscBLUsqH2zjp1wV54Fj8ZPwk_kqihUAtq9hYjoXd07a1NMHAot_Nl20zutoaP0gDydBZn_0Lh27jdhlE_CxKaRfpwwXHmSlyzbsqpD5Ko4VTYrP_0LlyfxcEbWotK5C6b885K03T6K_nfIVTPvp4le4T2FTZPfqIlnIsJN54PGlDwD9vBLxTszW0r7VH8ESFfqqOwnW5gWozmhVHR2ZjqcWvgQ3q59Yu-QnWw-Q1RuT5CeYGwq2wmS1_Qwil005zdAGMEUmdvPCyAFQqGeEQwIGtfed0b265_rfZinbtkN1wyZ48hLIeeGOileaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=bpiW6ifO-E3BQnhpzHjUnXh3FlaR7gV6i6mQm_8jpmvmtLuoZOP3xq0FtIzbd2zGi89fti6Gv4oeCQuHQSo5EVQnTTtFIM6Hm8D91v9o2pDnYAgZLU38grtGXWLf2WMIDIx7WPLjNU8R-hnPm4Y_1iEWAqsPH1CzPDPWZTc9yfYbznXBiO6d_dmp-342LUEZUt3Aq8lzySlQMgEjpBXCXn7ZEYRhitJwgy96fGWYu46D5fhN9YQSkrQELhUef4tvx4d9N1JhZpf_sAWY5thnoEqB6VNQ8b30FB0YJ4s4gzZDwr0fDKfqdTtl73SOuaJwCC3_yjbNmeM6nRPi1j3_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=bpiW6ifO-E3BQnhpzHjUnXh3FlaR7gV6i6mQm_8jpmvmtLuoZOP3xq0FtIzbd2zGi89fti6Gv4oeCQuHQSo5EVQnTTtFIM6Hm8D91v9o2pDnYAgZLU38grtGXWLf2WMIDIx7WPLjNU8R-hnPm4Y_1iEWAqsPH1CzPDPWZTc9yfYbznXBiO6d_dmp-342LUEZUt3Aq8lzySlQMgEjpBXCXn7ZEYRhitJwgy96fGWYu46D5fhN9YQSkrQELhUef4tvx4d9N1JhZpf_sAWY5thnoEqB6VNQ8b30FB0YJ4s4gzZDwr0fDKfqdTtl73SOuaJwCC3_yjbNmeM6nRPi1j3_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vh9h2a-68tEacH4Fu4Rrsg6rpIhR6YKzVct7wZU36ES4ZBkFdpnhT4bBFSzn8QXEBxNi3leWOIoJQrfRMfOHpM1XwetcO4vtye0E3tN7Yq-XeiNmycImeE9zCG6PxQvvAX-uXYZfzHA6vwfoTKSAlJcRpkPteCVOhlhtalPwvsiH-kY4e-PM5CSBRb-5Zj9x5uGfpHeMQE3AEVzIXpTqnrCvFujUPq0GuI4T_3QvvDTTdo5qnTr_CGrPHf5vAYUC-haFGg21K4a7Dy8WjD-mMFxl8WZPUxaeyEdVtjvd-iBpaJs2-ufJovM-n9CSM9vOClhILgoCymQRBWLHsvAZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaMvstE8EYLcZftFvU7aznPlplRI6X1ytntfz1PGv1khbIDsrBviVCEoKTc4milonPC-RCvqfZXau9WTwp4VjkfFg6886B5F3yGby2Ym7ue3U2GBzsGYwl1GY9ZDmhdplEnIrS1xJn5eKrG8pZAoCqj_c1__NFr7SNtQJFLyji8hnG87wbH9ZfrS662lOuInJDxb3Kp9LsVVk2P8XvPCoxQ9UOcmJpYU8LP81S0ZcSfFQ180zd5wy6T1gd56Ef1WUcjoLcZsa7ekMFgriFkZJVk6mwkkpsvQc2eNgYPo-yPN7YmvvyNLNqZ6R936l4WFXzmlxwnk5PS4R8A3ilZmLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZtxmMeez2n8oNVMiw35oLi4SVfRlj4Yv-elEszudenXl6tg7WhPRO3UafqCTb_q4x9Mg_Ra4JDo_NyRY6UPgLQ80YB14Pv2NbNGhUHYaauLQDfTRwDKV-Vr1rQsOzVEb2kZIUmfE2qCkjy62qoBMs0-bwYMSJK0iudTRQg7RDeolhrRXzSSUqo5QlgUBCGP2pSaDvUh7OLb9UGdiwUWAxKBWlpO1LB455asrE4n4_0nJ7F5-piTB2rUIgfabwZxztv96ZdZmjpTI553Am__LIjrmGDiNMuWV25yC1efJrEiE-4nlvNVjsquZFmBwKf051wfLuHhwqhEsOBHoAeo4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=mVK-KGVft5k40ZChPl0pYf5rqLr2o_6nBx1hPXP5rus29kN1AztJmuDuX8w5sk9NNQn0e2596cTc3upyPD43YM-PKqqr7p4ENjtzynTUov8wUzeF2L66j4QMtn-AopyjirB2FR7kSrnHt50ErfNGiHcbBJtohenBnZeD6hq2Y5Iv11TITigPeIv0AcAmuqC1M-C0JgKSHPYEl78cT-oppvpsavYobvGCEaSbfJDVKIWFgk_4_TfvpcT2cQsGlDkr8OF7oq25M3Ow_l_pRWDH95KieQld_DZl26dmnX5VOa-CsTqZMZ6-VKoRIrf_sOpoAkc1x2g7xbQ-_rmF7-ABRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=mVK-KGVft5k40ZChPl0pYf5rqLr2o_6nBx1hPXP5rus29kN1AztJmuDuX8w5sk9NNQn0e2596cTc3upyPD43YM-PKqqr7p4ENjtzynTUov8wUzeF2L66j4QMtn-AopyjirB2FR7kSrnHt50ErfNGiHcbBJtohenBnZeD6hq2Y5Iv11TITigPeIv0AcAmuqC1M-C0JgKSHPYEl78cT-oppvpsavYobvGCEaSbfJDVKIWFgk_4_TfvpcT2cQsGlDkr8OF7oq25M3Ow_l_pRWDH95KieQld_DZl26dmnX5VOa-CsTqZMZ6-VKoRIrf_sOpoAkc1x2g7xbQ-_rmF7-ABRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=eEUC4siUDJWy3mBqBYKp1NUJAWRzmV43gMNSi82C8XaRl5rUCz-OOFmyK9Cs3ACdqOwLbyFL5yhBG_eynHke25x4_EgPl59fcT4Ef4rdYsg1oBwi9-F0i0Vx4NoXBDpNb5qVsSE_XICeOGHFz_BVEYtGeg1r6CvJICXoWCYkBKZAlrrr7MXC_eKDJzorPZ-Gq5dtBbHeY-1aQtc3LXGrYRxJlKnwGWs9ffu3VWEtc6OlwQDQhoczKW1B217SqQ0QOGbvHj5XlvTCSMP6jsKXu7NSZJ0EZtD2FqokyYwoJWNxoZ9I3tcr5iDDZ_a9BAIwWCawmy3OoJjAmi-3_MkrKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=eEUC4siUDJWy3mBqBYKp1NUJAWRzmV43gMNSi82C8XaRl5rUCz-OOFmyK9Cs3ACdqOwLbyFL5yhBG_eynHke25x4_EgPl59fcT4Ef4rdYsg1oBwi9-F0i0Vx4NoXBDpNb5qVsSE_XICeOGHFz_BVEYtGeg1r6CvJICXoWCYkBKZAlrrr7MXC_eKDJzorPZ-Gq5dtBbHeY-1aQtc3LXGrYRxJlKnwGWs9ffu3VWEtc6OlwQDQhoczKW1B217SqQ0QOGbvHj5XlvTCSMP6jsKXu7NSZJ0EZtD2FqokyYwoJWNxoZ9I3tcr5iDDZ_a9BAIwWCawmy3OoJjAmi-3_MkrKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=jb2wRf_EFU2DVHonstnF7QRVO3-trpaZQTG6oltsvIcdUtgkkqPwRxFv3TjcjfgMIAP8ZElxHn2ptNLrvH0U6K0zMDXRKz5cATC_n3TFLv0QyS86srzrtQ-8ADsoP9qnszkpNnHNFbuiom1GBWQ2AVD_EPYfiER38sohW-PuzuaEWnUZdwUuwTgv2C2QHqqhJicvvwrHxN6sV_l4lKjB5BkGhtIqe0aDz8QH04LXtg8fmvNcBkxMWqDZTymWEe8odDryjoDc6p4ilKXSx5njzwJbLW7v9rJby5TyY9GUv9SigSs0N7KGkrfZzDCwYD-8g04S4XzWaYI_-SZya5N04g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=jb2wRf_EFU2DVHonstnF7QRVO3-trpaZQTG6oltsvIcdUtgkkqPwRxFv3TjcjfgMIAP8ZElxHn2ptNLrvH0U6K0zMDXRKz5cATC_n3TFLv0QyS86srzrtQ-8ADsoP9qnszkpNnHNFbuiom1GBWQ2AVD_EPYfiER38sohW-PuzuaEWnUZdwUuwTgv2C2QHqqhJicvvwrHxN6sV_l4lKjB5BkGhtIqe0aDz8QH04LXtg8fmvNcBkxMWqDZTymWEe8odDryjoDc6p4ilKXSx5njzwJbLW7v9rJby5TyY9GUv9SigSs0N7KGkrfZzDCwYD-8g04S4XzWaYI_-SZya5N04g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQABhu2KqLU5jSJ7Jfn7S7QDzIddf5pzEKFHJdkSbK6evJxBvoicHZPCYCjW0el-5JLJNbICo_Cn0063Kcnl1xLNywgOhfYbjhg2kNwy3eHF8uDffl-9hfnsl7-lOULa9NAtTyTGlprZaXkh92pvnB9LsEFi0i7zptWIGAAdtLkwUDRM_LGIo1WEZEOOQGZqIHyZFQwP2GwIhSfSceXcwmf3_oxxxZPVrrQSNcBsO90b1hdqX_sRVikP8GExZhOcwb_5mG5lRegdN58wW5bxdgKTfA-mdfknDYXoD536jXkgziQfifxtPtn0tDO93waRZcyn1GyW8NknDA0fO26KTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=fcAruhxAqqlHum8NqCSFrs8fgUHuuB_PZF_mA2Hzv7QKz-M2N6K4y22w0Gjq0xnICymeWJeUbnByyK3VIpkerdCHKf7bsf1O23Yg3dyOFqIxDY6tD2jJbVPaAlzWwKwrjhz3IwyppDeaapH147ewC95kRzbceBvuYU5o9nqsvV764TrFUtVCfzdd12zK3omWLb8v4iapQOUiKkH-xeBVl9g0GED8FSe_nVD6ECvveDLVG2WRrWSrGHFUndel4SmpwvuntSBQUmFu9YOoMyJsv4BB1vOSZ3jal-cOwc1h7QFJS0Bi05Je4cW9ywJUnUHcIVPk5FndNUQwlbKB_RiuCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=fcAruhxAqqlHum8NqCSFrs8fgUHuuB_PZF_mA2Hzv7QKz-M2N6K4y22w0Gjq0xnICymeWJeUbnByyK3VIpkerdCHKf7bsf1O23Yg3dyOFqIxDY6tD2jJbVPaAlzWwKwrjhz3IwyppDeaapH147ewC95kRzbceBvuYU5o9nqsvV764TrFUtVCfzdd12zK3omWLb8v4iapQOUiKkH-xeBVl9g0GED8FSe_nVD6ECvveDLVG2WRrWSrGHFUndel4SmpwvuntSBQUmFu9YOoMyJsv4BB1vOSZ3jal-cOwc1h7QFJS0Bi05Je4cW9ywJUnUHcIVPk5FndNUQwlbKB_RiuCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=WXtqKRaxwK9Q1YJ2e62uXUlWZmEz2OmX97h55ylRd2JIQlgGfWr58Fq7LWLU5jJQFeBCtGUTuKSKxuDCmrGItdkScMGHoHAxcrsYSt2O-eu1MjOERuUnATiBTv4D-mzKWedtsvRVEmL-1P0iqMV3uDntcySbS44FB-YSaddh1KwqMIYd0nl7rLyNG1-H_lj9GwfKrW5OK4qsH_GRXyqCY8SMtVI5RipcCD0MPRAFzR-6JIBwlydaImXGXMEKA0uaxZRnY9L875xILtHZ0KQNzun2J230ZzglRw4cwxjt-j_Hv1VT9qWzOTI2CFRAwdb9mN6XTsMxDvAaL66uS3fz-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=WXtqKRaxwK9Q1YJ2e62uXUlWZmEz2OmX97h55ylRd2JIQlgGfWr58Fq7LWLU5jJQFeBCtGUTuKSKxuDCmrGItdkScMGHoHAxcrsYSt2O-eu1MjOERuUnATiBTv4D-mzKWedtsvRVEmL-1P0iqMV3uDntcySbS44FB-YSaddh1KwqMIYd0nl7rLyNG1-H_lj9GwfKrW5OK4qsH_GRXyqCY8SMtVI5RipcCD0MPRAFzR-6JIBwlydaImXGXMEKA0uaxZRnY9L875xILtHZ0KQNzun2J230ZzglRw4cwxjt-j_Hv1VT9qWzOTI2CFRAwdb9mN6XTsMxDvAaL66uS3fz-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDY_-O2mpy2tTLw7QHnZU_P9akM_YU6CDT5YeKpfNaRjoig2dLKsb2DzNJXNUgHHnl8vkuXr7LPhBUWQgRN9f8DpX9wdJ93Y43LM5Kid1ONu_Kz7dOV3RQ8XNH4tT8b_HhUUxYxhO7aHzhQE7U5UwhRkVnaafmMrMwCmxC54vUPK_lKupED1_6CkNYy2TT8eOWOdIBgee002MNkEIg4msPWi9JL1v64Us1_wYhJCkolDnkdITRl29OhOYGVM981DIdwA9V_5D7Irlg5LCKfBGG5TL8-ciNlAsKLlUJGF0U92bV_8SFDta5fW-AAJ5ZpwhGDdAKIN3OnUIgAXWWFVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=WCSOS31ORytA6s9iu7WKyLJcShWcFhbG6HydQTLtbFyDfYDvqv8B8b4m8sYdvoh08330YZl8t7duQJEjmBoXvuVTOqLss4FvVdVq5fsDnwF1uOzRHC2kuH1IT7P-VV7xpRwjYZuQmpLHjahtqbeRjYT7ZP9ktS2OrywI005sAgXxbzKAMWvlJQrp5vqAt3Dg2IIlA22Myuwk9bxG2zAXUQqJtBos8ND5Gs20hdql5lPTmORQNACfoadbZW4cfqq44P3vhE_JHTFJB-h3hPq13SzKvI7FmhSZ6dqV7meV2iyBxFSKHx_nJpKDHvRAJZcEHYRcDI7g9XKLxijFiTcUyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=WCSOS31ORytA6s9iu7WKyLJcShWcFhbG6HydQTLtbFyDfYDvqv8B8b4m8sYdvoh08330YZl8t7duQJEjmBoXvuVTOqLss4FvVdVq5fsDnwF1uOzRHC2kuH1IT7P-VV7xpRwjYZuQmpLHjahtqbeRjYT7ZP9ktS2OrywI005sAgXxbzKAMWvlJQrp5vqAt3Dg2IIlA22Myuwk9bxG2zAXUQqJtBos8ND5Gs20hdql5lPTmORQNACfoadbZW4cfqq44P3vhE_JHTFJB-h3hPq13SzKvI7FmhSZ6dqV7meV2iyBxFSKHx_nJpKDHvRAJZcEHYRcDI7g9XKLxijFiTcUyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=Av9ynde3kg0B79Z193uUwckyKejcWMyI6y7lfN8m-2DM0vlFZIb8lMs4BXG-AqPBeWEfuESzplCfkKN93vqeWfixdIvne0-IY0l4HTTQ2NxmOV6WQ5kj9qK0eGElBauKX2SxHrxjgUQKRwZ__uoXg2Y3yq_AS7twbaqqvGQZi0EFwCpt5Z2Ul3O8fxshfXQ2vkiCWoVHgT2K4rjj8o7iqStm5Zq7wD027nPMphG7MMeeXB-jphpy7TRNZVwouC6FSVBUUaF_feTI7C-IodN_YHrKT8VAOOFYrksE8ppLI_BARukr6Vs_ZE1awMqVosAiOP_j6lzTnEMMz-wFElA73g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=Av9ynde3kg0B79Z193uUwckyKejcWMyI6y7lfN8m-2DM0vlFZIb8lMs4BXG-AqPBeWEfuESzplCfkKN93vqeWfixdIvne0-IY0l4HTTQ2NxmOV6WQ5kj9qK0eGElBauKX2SxHrxjgUQKRwZ__uoXg2Y3yq_AS7twbaqqvGQZi0EFwCpt5Z2Ul3O8fxshfXQ2vkiCWoVHgT2K4rjj8o7iqStm5Zq7wD027nPMphG7MMeeXB-jphpy7TRNZVwouC6FSVBUUaF_feTI7C-IodN_YHrKT8VAOOFYrksE8ppLI_BARukr6Vs_ZE1awMqVosAiOP_j6lzTnEMMz-wFElA73g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
