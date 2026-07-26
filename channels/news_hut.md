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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 16:05:54</div>
<hr>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g75wtzPZw2SblXu6oXv5BZ6InUgOfJGiJNDS6VdHetuZLJ77wDSsl7o_Q20Kk2v4W4U6ri0uz2DrjIBinIkSc3s3Ik-Vd9TqKtwMcYNL3Epxj6dhCKz2Ugmjot4AA_9G9360td4-p1TFkLN27Bj0JLgmTxb-gzuahMSos42sSYWuL7NeFwp7CxexRid0KLmW0QrSxXka4tfSMmxkregjXJssT1N2CwPw-gWjm6dlUHqfG8DA4vrtEpOETP5upkUbokYxGH4f88BjeK2Mb8ekMwYkaz_mhl68CfeJChCOtIeytOtriJAaR-ZuY76eRTu2aNIzk3FoOnkWr7X1Vxg3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH-NTtkv-Up4LkjTEf8KPckOUWDbxnriyLA65RRPt518bla9DVh14li0S9MDzsQER3PcDHiPudoI6M4KoZM2dVGSesa3Z8ETS24l_waza2LiJR2m9jBeENORsPlnQAbCSk2jvygpAbbH8cG0R5m9NYdJ8m4G2jOr6I3Jna1M-s2eGNhXr4Ewz2sl8k3-CWn3gR792ZZk6IjakKo4j_uNu3t4Si0IPQyIDxw1_IsnCoCGrNgbO3Z1BqftXM48FenACPR7_p5QcwBnNno2FCtHncE98frk6EkT2mdOKgV4u-V0Xf_YC7V20_Cr4s7f0GzrpSYQWkn_obU2JpqxbS8PZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt8n_TpB0cFjFBi2s1PaMRRl7PeUTtpqBFH-tTkq0ukwrlfIKpSJxcmGN8y-huDKaIl8z1c6C81fUyKW8TVDbL0wRwS2GvXHXXPojazRy2RjXhMUYgpwUuZqg0OlzsAHF4YLDAR-I5IbhwIP8rZfNty-kmGKl9aYX_vlFNLMEilg7YouudwY9vBCPnHHdGClvdeWc61AjJwwY5IO-y2QAsL0mDL5-1NDDcijEN4vxhcQgmeEGeWt89siWnFBvwgMRCHWPUfWRmUEdat0O24bLGL2pfRSIYHWhWlw3PwNKr7T6BvBRu3F3BcwDVOBYnZ3wVV85UeV0FIWuubvnIQmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_grE6OHQBPvQvezozuJenYYGsYRXjuQknrzZPEc9mW5gvXTELXK_aSk-YtmRDlCjPIsst2tPyrdAJbInR1JWlIB3UvcdiKT8wUGxsA09eBBV-XHRhZyehHMmjUDfYlqQEQJKG_KsdC9Qb8ufsn4KCdU2EuVTn_KdEq8pmmSoUqv8U4ujFPyKYku8IKjEii_lBaFJvgfJ0p9aAWSJUjY0vi9Z2rcvjaNYOYTGmpRh09VE2543mmK4fnwnoiesIjP4TR5rjWdQuc6mALXba7Kgcq2d8wV0HjNT_vdDNCy_J5bWpw_VqKYtZzHBWfi5foN-eOGT8fP3E2Dvj7DsUcJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1C3-VgQcfcryqgOkebK_uQ365IIOulvJo-pLPGzmcngvq6gxp1Ex58Hfgta2j1xmSjLUHa_-E09v8344vGZhO2k5rDxbCwPLHG7lJ7aQqNZXYElPU-Lk0YA9GcJYyq8xMmN39iGmoEnE_tsIO1flK473XF3cPR-jqEERP3r7f2RaPP1-JejBJXklxqXGIa5eWLkMzzhJo9J9AE3xkElaN__iOA4Viec5x0uGRWfqGTP-JE8awT5hpXZ7pBrRUmpZdETrcqSmTZGuaJn13x6uWxiA-F_5SoeVuAp3SMnBSHp0lxNf4_LbSi39qte2zIazTLnqamE5MYVlB9VbEnb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUc1DqU0SAG3Uh48ed3v2uA0KRGQPwuHqVSNTxRri1oMwOgi8CNC6Ys20fKWryVrVCt1JGDJc2eXDvxQB3CiOIn5_qmiArDnVI0o3uN3db95SDRnjv0V_J3aO9B18yltNBgTNsz6syH56RvvFsmmWZiSJtZNTFAj5QhNdDPpZ9AN86vurG6ELLncSPKVcs8iy_sMabdUuSgjzeDQqvj79Pd5WO0hkhKkDu3w02m65vozczk0xQs4vay7TtG85eK3iI43-Gfx1fkzGmR1z1jWuy9ATegvdJPqZXEpzTl-xFu0TTVVk0gO4IyLsfmG1xvCBfHjRSuwsdzjJtOOwz3pOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxxS86Te4H1EutF0Ly8bwwYyp-gHoOPdqka1mKR9IAfq0gVvtFtqW6J_0Kp-4zMyLlhRvZRs1mZcvBYm-l1-rgSKq5UGs0FhZ30MDxSq_tYG9H1c7AIWSZkjiMltjhdZy8hbgt3m1bAmll1QOC_lhQ9dEZ04UdeX00IUM10sxUQX-CwioiIcTrNXSUsflvDcHPwcS0pVtgH-UaH7cx2xgxJFk_7EowM00WSpNi5d7fygb-D5YguuYtKTYcFA0pYqCXNwA915GM-ue0o80mb6zDh-LGMFOOGKdIVbgLzXk-Mi5h0pZwFsAs-Jweui1kEaZoVc9f_XXdrBnHXMr-KJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=G0lKmwy9XzAI-T5OIMTi7ygUV3qG3s3aazyTGjJRQADMsYxjGKQEFyTEeKHXVM2MaHez6JiJke46v37OCqckBrDyEDVkWCGA__vu0yK4oNs9dGVvUiow4MiJfmdj602SC5EOMW56hM-xN2gep8f713vcjNg1aqlcrIsjJL_fKMqBR-IXcV2nydi-dMPild-EkeTvor8EFQto63wXcV7DAfCCKLta0VAeEeClEfzdpccthmyzU7QSCtwESXIHRxQEaXQ77ass3M87OCv3Dp0djy_fio52H7eI4ipdaeyb1exPUUOCZU53dgR_hNs9YlKslRnE8e1fYQVNMEZ3uqPujw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=G0lKmwy9XzAI-T5OIMTi7ygUV3qG3s3aazyTGjJRQADMsYxjGKQEFyTEeKHXVM2MaHez6JiJke46v37OCqckBrDyEDVkWCGA__vu0yK4oNs9dGVvUiow4MiJfmdj602SC5EOMW56hM-xN2gep8f713vcjNg1aqlcrIsjJL_fKMqBR-IXcV2nydi-dMPild-EkeTvor8EFQto63wXcV7DAfCCKLta0VAeEeClEfzdpccthmyzU7QSCtwESXIHRxQEaXQ77ass3M87OCv3Dp0djy_fio52H7eI4ipdaeyb1exPUUOCZU53dgR_hNs9YlKslRnE8e1fYQVNMEZ3uqPujw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkbHWKJa-luOZglAZWVJXrK70lZ5bhyoYeWBsM3j00kDqKKsqUSeT5nEDA2YgrvFEnx5pLTnvPEKsEYqWT41Dq92NOmUreeQ0Lq7OyErnTxMrdGdAeJNj2g860ZaDKgd_Gr2wVa59iGoGJP6_pUDUcYGcZdd2UbzKbz37re1MLKZwctgWnbOPRQ_1mbfrjOLfkj2DmyMhry5NeTSXC4-ZRa-6rSoVVX8jAPkdy_JmQG3KLtS47sbtLviic_GFjOtH0yMvn6TpItm0LMCS_nFZKqvtiNCK_i8RVlFZ5UFnKE-FMRLn1n__GFUh5DjiT9hvKYWPf4vXWyZYuqqPdXDRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=gzs2r2xyx9OW9cnawNjqt5p-5MCzpqbWZ_tOAGkYzRT5xzuODNYw1UB6325-DU8D4CyZhdg8U0G-Y1BNKcRva_It1_liRL4JU-k2Yl-mosHp94tAVQQtpAMxtuhB1_NfGle5jqEqCahCWB9eDFuWAWtP4ktT2tauvNwiVLvG7CNgjRXJSMiEV61nGgT9PjXIqc-bz7bjauEsapmCLihArOiJkHn4t-FY6clBKpVcWK2m6Md_SgocMuamZeYbipWnsw8kpWvamW6527hDXmmz7YhGU3nS6cFh2XjLxX3M_U4n8aQrvmcU9YafwwaU4jjkMBCLGha7_53trR0RSWra9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=gzs2r2xyx9OW9cnawNjqt5p-5MCzpqbWZ_tOAGkYzRT5xzuODNYw1UB6325-DU8D4CyZhdg8U0G-Y1BNKcRva_It1_liRL4JU-k2Yl-mosHp94tAVQQtpAMxtuhB1_NfGle5jqEqCahCWB9eDFuWAWtP4ktT2tauvNwiVLvG7CNgjRXJSMiEV61nGgT9PjXIqc-bz7bjauEsapmCLihArOiJkHn4t-FY6clBKpVcWK2m6Md_SgocMuamZeYbipWnsw8kpWvamW6527hDXmmz7YhGU3nS6cFh2XjLxX3M_U4n8aQrvmcU9YafwwaU4jjkMBCLGha7_53trR0RSWra9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtgS6H_D2zTMeVTg8EOpJCwSI3JuHrDjHvlezm5CJinT-0eMZlkTZTLDEjS5Kbhb20gb7RxnvyFtIIsWHM9Kvw_H4hv3MWgxpQg67H5c7eiyeKuyxnehAkU5AdDgmqpLOT9esaGaMtWqhkp7k6n6LwNcLVmCCpmO-HFH1JK346QbxKkR9DiJ4-lOuReaQqKTfM-A32DU4BB16WmKQ7YQZDqwb2vnJoPxzsksvlbyyaAAaInzRuFgST4UbALz6dBF5aYRzP9weoH2BrdshHIHbz-N2d10yWYOVaKO4Oeu6Mm676eLYqWnfC9BMxtxE_Tll3LUHUZzC93fSb8zPMmgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2szNFt3yZS6q4XuWZ86UFvhpj_P02dbBDYdoPRe8n_fEz1Z-K-z43q8X_LUZhGMlktIhULOowuh9FgJzds2i_kh-iuXroemL1Q7fFBlNI4Bth6RTBcN2AfgKIQQXsg2T6f45bk_xXfM5bllhq7ahHeVCyrxfVj3ZFgWZk3fH8oI98lS2NtJ35gBSd3MegpPkDmnHu4oZsD9hjReFyT3sWdXCUbQ6LMpSOuFZHOkvz-IVOVxpvkeqebUN5xl-vvBfKUHTe72ip9S7e8gQWYUnWg0mSltO2ftqX8W1i1HJDON4hA3Gdp7VFXur6oE2HKK5It23EvUQyHfZlnpgt4gCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=EyBoNA2YAX0Tf2laeUu2ZMvG8l0fTmvVmCvgkqVcspRgzOQrygPc3MHI4XFv_86Y7yIP4U9fm9qKCmln_MGyjnnZdTxfmsMAL2aw4JBG50Hkhu_rdRyPxm4DX2Uz5z5sp6O3UdzsE8Ca1SvUEpc96TEtkG-QI4-0yje6G2M_dYuFJv33XXKkCi_6h4ZfPCGUCHL356CrLRLg0oDUx1ou2vz8JW3_qbmOsg3GAzCHuUmKuxcdmOvStbo2dEP4Q3nA6PMSPWbgTWjd4lxFRdmSqoTMSYMuZDwhvU0CDPsoCp7WfV5QSD4j6W3CRYTEs2w90EXQDwWaAvPhWERJHKS30IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=EyBoNA2YAX0Tf2laeUu2ZMvG8l0fTmvVmCvgkqVcspRgzOQrygPc3MHI4XFv_86Y7yIP4U9fm9qKCmln_MGyjnnZdTxfmsMAL2aw4JBG50Hkhu_rdRyPxm4DX2Uz5z5sp6O3UdzsE8Ca1SvUEpc96TEtkG-QI4-0yje6G2M_dYuFJv33XXKkCi_6h4ZfPCGUCHL356CrLRLg0oDUx1ou2vz8JW3_qbmOsg3GAzCHuUmKuxcdmOvStbo2dEP4Q3nA6PMSPWbgTWjd4lxFRdmSqoTMSYMuZDwhvU0CDPsoCp7WfV5QSD4j6W3CRYTEs2w90EXQDwWaAvPhWERJHKS30IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=OOUrVPRZnaFFx8zwv0bmETXNAb2UMmacXFk22dyUW3GW0RjzgnrPtbHQmARw4oU-5SNFHsSHrDHvFcqvYdwISho0xqqAy0rM9z4Os9wTCDJRhn08CruF4OP1SpKvzItCqx4xPYMfFoHzI1NoghNt2hCoyv_hdZIITv2GrDEXSMzEPJlolcRXG1RqpXw9cPF8dyf6PP2L63noHdhpWjtDROPYes09EhBiRGZR4utRMPsojJY1pZ01myECwc4xo3Lheh0MV2kGpwXUIvj8GC90cp3h2tL5ya276_mCV1tpAG_ACmMJbKX5K6rmlufHIRWb2ithnLNhBV5XhTdfquO07Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=OOUrVPRZnaFFx8zwv0bmETXNAb2UMmacXFk22dyUW3GW0RjzgnrPtbHQmARw4oU-5SNFHsSHrDHvFcqvYdwISho0xqqAy0rM9z4Os9wTCDJRhn08CruF4OP1SpKvzItCqx4xPYMfFoHzI1NoghNt2hCoyv_hdZIITv2GrDEXSMzEPJlolcRXG1RqpXw9cPF8dyf6PP2L63noHdhpWjtDROPYes09EhBiRGZR4utRMPsojJY1pZ01myECwc4xo3Lheh0MV2kGpwXUIvj8GC90cp3h2tL5ya276_mCV1tpAG_ACmMJbKX5K6rmlufHIRWb2ithnLNhBV5XhTdfquO07Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=UD4T9TyvS50fTKwQxOAK-bXTD8WJ8tkAQCWpeugAjfu0fjaz5RcTG8Ifrub-m_1kyDPV9WoT_7B9itgHHUaw2bcLNwTyuKNhexvwloqqLMitGbWd6FJ_rUluXOQ8-J3WGim2YDP708lkMYhVTtCWN1osht7xOX7EGTz9VjMTRWv6S_rZN7up4UiuxOQvXj0QGvsNj_SQLLQdfE1HVi5cutbvqMiLEC_yRTwH8zhCvHzsMedc0MXJkoyhGsz53h-GrdyzWo0EOr-G8PK2mb310N9L5Vm-TH-9xSR6MlSk62I_N-CqAjwEUtlCgCoNt6u5kMPCLP1z7q5BveLzjU5CHWlNdukh441L2bBBMjmen4GHHp77c3Hsi9MdsBQjgSMnR2pMclRSNoLYH9tUIkneuMSsqIL4IBZS4IbWjuVFNjjlAp8tahF-PvJimIBiENFP5QvCoQmGdHhWnQl4b-lcQFyXOg5tsl3l_brMiAUInNTQ5U9N4y3-UqJ0QeXJejIj2KzFbN4ufOr90Yc3XlYWj_gBbQsm0TZMtMf1qYFQ6x-SKo9joHppiTtHiChZO9L5mV1vOaps0-MNKOOQHE-XOCJMpeTEwMG3i7sCFmFZ8YtGI0NrN8cwH9qZEIgorAFzpR-8FiNWwgBhXRVW-OD5-HEGdDA86uzOgSOKWZzU2l8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=UD4T9TyvS50fTKwQxOAK-bXTD8WJ8tkAQCWpeugAjfu0fjaz5RcTG8Ifrub-m_1kyDPV9WoT_7B9itgHHUaw2bcLNwTyuKNhexvwloqqLMitGbWd6FJ_rUluXOQ8-J3WGim2YDP708lkMYhVTtCWN1osht7xOX7EGTz9VjMTRWv6S_rZN7up4UiuxOQvXj0QGvsNj_SQLLQdfE1HVi5cutbvqMiLEC_yRTwH8zhCvHzsMedc0MXJkoyhGsz53h-GrdyzWo0EOr-G8PK2mb310N9L5Vm-TH-9xSR6MlSk62I_N-CqAjwEUtlCgCoNt6u5kMPCLP1z7q5BveLzjU5CHWlNdukh441L2bBBMjmen4GHHp77c3Hsi9MdsBQjgSMnR2pMclRSNoLYH9tUIkneuMSsqIL4IBZS4IbWjuVFNjjlAp8tahF-PvJimIBiENFP5QvCoQmGdHhWnQl4b-lcQFyXOg5tsl3l_brMiAUInNTQ5U9N4y3-UqJ0QeXJejIj2KzFbN4ufOr90Yc3XlYWj_gBbQsm0TZMtMf1qYFQ6x-SKo9joHppiTtHiChZO9L5mV1vOaps0-MNKOOQHE-XOCJMpeTEwMG3i7sCFmFZ8YtGI0NrN8cwH9qZEIgorAFzpR-8FiNWwgBhXRVW-OD5-HEGdDA86uzOgSOKWZzU2l8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTgxXT0Y3RwN33uwIRAIGm1L0QK0HpOYCxqHTeULa_ycBe6PijbBh3fPjqd861IWX3UbyR9DUpkVosax9D0CzNt0-Ss9kL3pH0gsFKXMyL1FyoN1vPJr70v4-x_U1DERRYZsNsCkAeAQ_tV7O5LtXuBOdljg7QNfpQpTdVfKJIT719a_cdv3UVsA0Gr9RU05O3pJ-bHJIGs74HjD5TPrDFez-wWE4ZEPcCf7dRA9ldy0uU26efi9bS2H4eMEQqlGkdX992tN21tmTExEW96OaEDI4TIopdC3tmyMlkgMEl2etAUu4QKLOo_r85kNB3usLKtNCZRUKsmTSZ67OOm-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=JzYbs34NsArW4FfFIaKYdeuBxhOMi7uujilUw61lLKugkqIq63AMavNcuF3JFZG-RYeVshDvbPkg4DByQyuRyDA9lHLr6vl8l9f2E8feezl4u7x3XyiA8B6xn2xRqTNj6WVKqtvdMfzPIyVSNLDee8kPCLsUvLc-52xaqn8882ZibCBEM6wZVCv2ujvMHrMCTRxmvB1Y-znvYDZG69pzi9cUXfYjizYXb6S4f7gIi1F9pMXV5p7RsMgVS5D09C09mbaYfZ5q1-k_AY6l3r_xMHehi3UnwdRoI7aBqtmyQtC-WR090fo69HkSh91FGeTrElQJm91MUMCQzP-S7sj0cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=JzYbs34NsArW4FfFIaKYdeuBxhOMi7uujilUw61lLKugkqIq63AMavNcuF3JFZG-RYeVshDvbPkg4DByQyuRyDA9lHLr6vl8l9f2E8feezl4u7x3XyiA8B6xn2xRqTNj6WVKqtvdMfzPIyVSNLDee8kPCLsUvLc-52xaqn8882ZibCBEM6wZVCv2ujvMHrMCTRxmvB1Y-znvYDZG69pzi9cUXfYjizYXb6S4f7gIi1F9pMXV5p7RsMgVS5D09C09mbaYfZ5q1-k_AY6l3r_xMHehi3UnwdRoI7aBqtmyQtC-WR090fo69HkSh91FGeTrElQJm91MUMCQzP-S7sj0cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ-5dGzxzQhAfjSLdtkN-r9HK1_d04srbcjYNudenlV7F7PUOqNAm4-Mq9nG_ZeM4xKyTAomiTfH3Fhe7JBooXGlSk12GFJWcrelCw7hXpnTwoutAlJmm2gHsrFKURgOP4PZjc7eIkDy91CsqHH_ZYpNVQdXk-qlsnpvI34iikg8yd4MoeplITEjHRj3e8SA8-5ddcFMl14dh2ENg9QvytYbOGt9zlz4sqkLxhjcc717_ur1vYqfyignAMey7T7Wz6ryaqjUe3jgV1Kd4R0NJEidckCm677XS2pd1Stj0t3DQDKQyEIB3ejzEKxm7YeIfkG8JeLpXiJm_JDCWOxdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTomJxacE0z3PupXg0FO1TBiQeU0q0EeKDR1uFQ64jk5cc8KGbuOoRazeh_USckYOV0c0n2LYNw36ujqKrDNtaveSf8XXI6CSXj7p8TmfpoXj6m88cfkzSf9lkV2U77PIlLrspOFrWheUuX9SsEaRFb8CiGLrLcYG1ONOPzxwqiXKhm_S3EGMRqoJOlCHHldd6junfPJ1RckE4UGvlIDMfzzsIKNB_QcN632h8Htswfnm20QqxwNjxTmTHXlu4IRoB51DtyQ6C5oqcBXKJr8hmywEnP2TFvR-xxgg2xVNfYLiDeeWUlDERIxWp7C834dbPf0h9kJBkXR5B9zOyWuxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYorHnYrWLoDF12ukGdwpm8pKhD3CoaqrLFDzreEARL0alMmTrdzLjqDN3gc0CWW_GudN4Lgf8LCRqw0YyNG7wUK1ebfycmjv1POGbONgFScQAdy24zAVshnoEWOhPE52XoKsyfP03tf4mEW4n3rTxchbymb1dTkuAgXTbChYq5tdO--jgsgorP5uJbwEQxf41emHhpYkI03H4-D2xNw7l3fddwnEzhWJgeroP8x9L9X2ok1hfvz7WX5iZKbEyx5VtMHHJSXkADthnO7q84ESFp0QwdRPHcQmUaNVJpM4fs12K4cyBuOqjW7RF0nZjAXu7Nek4RfNIFtqoGl8GiYlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcBKdvel3p3DRE3M4lfJhTTA65NGTIsSUoGLKJtRCPHiAABscl2m5XNKrz8R6WfEf9-FSVT7O5lHsP_XIURDxhWoGCiu8RXa-g-HFm7YbmLMW1O6FLCFOk6pFroO1rirxnag0Nrh2qRF793869P8EFp-WFpCmxf8GYaIOkzX3Pb-JAZR07pWWDtdTJnYUGmbBPzegKiPXnHov5w6j7u8axoV2c2z_9hWPy6-bh4oszuZ387HH7SPfu0sOARRAgcpiQfBrwjWG7IfT6MTpZsCMXDmbmVeREoB4l_7IvGpAqoQHVl3fLYmwEkw63LIhKnBxtH675K_YHS39KEQCha61w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vG_Hd5tTsEU5vXgJQrKCjsiQXQ6bMyRiuF8FjNlgRScRr-noBuhTOFgbdmT_Or3iNkJvvHzQt5fbNUIAnIL8blikopRZmgUzvRz1t_1u_gQYXrxOgeC93CXuRcB1RYDbuyeGKqqJ1Es1N3gsGrRtuUgEMJ5khif-KDR1TkfjGL9xBSrhMvufzeoqzADPAqdu7WGlLeAavPPf_1vE9thVdN3WrnBDHHGWkmEUTiQSjC1EnHpfjzWMDwsgM__JEK5In9NowZ-BwS73z-zVKdUM6c7T9TmUnAYZZse76B3ZOHNOwFDGjVv-7GRDFjFCcd9Cx1dHEDmIsrB089x_AgBTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrHV264wY_u_L7H4COdybM45hA2sg3XRjAsQ2wHCSyEF7UcoxjGZoYB2mWYoAaBuWvvMkUNFtXb5O3iWhPb8-zlQBkY8xpxaNGl_Ku944oSEX7WplfQ0CiLpAzq0x3E3rXo0fobdLIshNEfPhWES-5eXDRPlerOMJUwuGEYBn_ageQZ6ETRE43ctSe2NKlzyfYzTyx6-tRgJsbmE27LpHMRF56tUlpS2Mmcd6BmjWMwFPVyLhlAJp4dmrArBaUHE69somHkk9fGNzkPEQSZNA9gnSdINhs-vA2YEm2gdwSS7HG6qrlRLtKPHyILlqnJBMipwCbdcU7kWhIK4_ALslQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=Fm_oEbN6YEBW6U24_t1-ZJJI6bpGngFiB-w4BTpcF8n--rrWGJGA_t2tabSjh2BBRHM5JZvbjWaS2m25LxdOxGhupMidc3F9VIi-_729t30D8X9H5fpSpkhrDT0ofSGKremrUyqrNcSrAjFPP8_jDvPmf9nu2F2x5CpOviTfBWNPyN5e79HmHLhRH1TKLp_g4j_7s1NholC4vxqHbVEQLq1wRtU4seIh17iHi5LpKtwVAeiq6_b9wG91NSskf1KmphZWCuFw1ctZAEss05tc5AMZYZAD1jKYC_DlpEja-N-dN5q-YiQ9RSSrvHc6pEYsFXPov7OAlVj6yW5XrL3BKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=Fm_oEbN6YEBW6U24_t1-ZJJI6bpGngFiB-w4BTpcF8n--rrWGJGA_t2tabSjh2BBRHM5JZvbjWaS2m25LxdOxGhupMidc3F9VIi-_729t30D8X9H5fpSpkhrDT0ofSGKremrUyqrNcSrAjFPP8_jDvPmf9nu2F2x5CpOviTfBWNPyN5e79HmHLhRH1TKLp_g4j_7s1NholC4vxqHbVEQLq1wRtU4seIh17iHi5LpKtwVAeiq6_b9wG91NSskf1KmphZWCuFw1ctZAEss05tc5AMZYZAD1jKYC_DlpEja-N-dN5q-YiQ9RSSrvHc6pEYsFXPov7OAlVj6yW5XrL3BKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=aT3_prOwc8VEqLYjWUcSk-iQc_elNrhEzZn-2vhg6WlEkTNY3XEbRzRfg5DcUEP6QNMoa4R8Il_DqZEM9gS1U1DveBDUfyS9DKwdmTMlFyCFU69BoSOJUBF_fqB0Bjqpr-JKJVaXLqo4FuyWQFJCtq1ROPXnQVIaRCB7lg6fhxr8CR2GsM_NnFWKIMQapRNXMDiR3aNZL4r7OiHBMX_Kr7Vcf6IUHxH6EhwI8lfygPVB1f63dUZZRQLhXo-sM-7IlHS2DPZLkRjrSJoFvYs4k7H1gcJq-w4xx3VDp6TQZPqk50TnLXX4lEs-qljOb0Ukl1ZBmWsIbOptTqXcD2w8hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=aT3_prOwc8VEqLYjWUcSk-iQc_elNrhEzZn-2vhg6WlEkTNY3XEbRzRfg5DcUEP6QNMoa4R8Il_DqZEM9gS1U1DveBDUfyS9DKwdmTMlFyCFU69BoSOJUBF_fqB0Bjqpr-JKJVaXLqo4FuyWQFJCtq1ROPXnQVIaRCB7lg6fhxr8CR2GsM_NnFWKIMQapRNXMDiR3aNZL4r7OiHBMX_Kr7Vcf6IUHxH6EhwI8lfygPVB1f63dUZZRQLhXo-sM-7IlHS2DPZLkRjrSJoFvYs4k7H1gcJq-w4xx3VDp6TQZPqk50TnLXX4lEs-qljOb0Ukl1ZBmWsIbOptTqXcD2w8hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=gP3-Olpd9JQHaxerj_yqgnrLcTXs0JhJ0RCIRlj4D7P0ZfogXWOvm6E2A_McigauMhiFhrW8QN7HfNC4IBn30FOHyVoDE3geXll79kTEXx1fAA5FgW14wjllQIvIJLUpgie5ldx7Gc7kFLbj3OSBKnjl6izfpA6u886VUpzbCqQFdQE5OUhVVwETvWdYXypHIqlp8wrBprJ53FpbkI46JTs5mP_QRqGVRm7UXrhmhUqpbZusKXKKkzQunj6EnbSKu2qXvoEAWah-txqnTRAwkBVSSiVK3JQjEZidfdytLW9O8AvRglnESEYGJvJh4HULgj5jlaQUDDN70nwMG_WTPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=gP3-Olpd9JQHaxerj_yqgnrLcTXs0JhJ0RCIRlj4D7P0ZfogXWOvm6E2A_McigauMhiFhrW8QN7HfNC4IBn30FOHyVoDE3geXll79kTEXx1fAA5FgW14wjllQIvIJLUpgie5ldx7Gc7kFLbj3OSBKnjl6izfpA6u886VUpzbCqQFdQE5OUhVVwETvWdYXypHIqlp8wrBprJ53FpbkI46JTs5mP_QRqGVRm7UXrhmhUqpbZusKXKKkzQunj6EnbSKu2qXvoEAWah-txqnTRAwkBVSSiVK3JQjEZidfdytLW9O8AvRglnESEYGJvJh4HULgj5jlaQUDDN70nwMG_WTPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=j74Pg3TJXrlRTHPWlyGaXVMAfZBfzJhuLe9N-esjWhHpoMDMBFWkaZQg1PxLqZQ1CCHuelbqm_El7zFJMC_anzOkK5UPnyYxXkX64aK5Ukeji6dY3y9eO9WKgCSY8Uj_EVvswHv-4XgLLuy2bpQ-GPyeXmmDkGpHcDxyFqSaI0nW7x7fAjdekOfGHC38pi9mQOdA8S89H3-oPP5bZC84OTUNwivOzc6Z5aLwGgjsTKzow34ltHjTjRrr28WjRlbrP0Q-8TmVKBrCrOQK93HIKoePC350ViqZa_Bm85o5JbkCAJ83BWVNEHvg5tOMKv9BtgaOOxyDOcjQFNz8rfU6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=j74Pg3TJXrlRTHPWlyGaXVMAfZBfzJhuLe9N-esjWhHpoMDMBFWkaZQg1PxLqZQ1CCHuelbqm_El7zFJMC_anzOkK5UPnyYxXkX64aK5Ukeji6dY3y9eO9WKgCSY8Uj_EVvswHv-4XgLLuy2bpQ-GPyeXmmDkGpHcDxyFqSaI0nW7x7fAjdekOfGHC38pi9mQOdA8S89H3-oPP5bZC84OTUNwivOzc6Z5aLwGgjsTKzow34ltHjTjRrr28WjRlbrP0Q-8TmVKBrCrOQK93HIKoePC350ViqZa_Bm85o5JbkCAJ83BWVNEHvg5tOMKv9BtgaOOxyDOcjQFNz8rfU6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=ve66zyeieIfacw6uyoIxTClaSbVstOIKP_cylVz98eWuOX5_SVtGALOXgFlWpZszc1JO9i3QClMCmt4NhEWwXTdaQ-Iz-8b2twN0_6GdIdE03AU4XZ7QhmHForRzgtW62ARLHlOANUv9VkgGFiOQZoHtOf6N-DM9we2Er0wHoatxNkksh02nWlt3dz35FtM535xr_TtDaCEX5SPX-G_2VG1vfIixNTg-W1k4404sohq8xE6UUa06zOKTDQ46fawn2CrYu-rINGBG1YOoj2C7TkuPma1NGxlunHKyG4xJqVDodQySBge5zZ_bU27Uv81BR9ys5s1ggL9_c9YWU5Wl8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=ve66zyeieIfacw6uyoIxTClaSbVstOIKP_cylVz98eWuOX5_SVtGALOXgFlWpZszc1JO9i3QClMCmt4NhEWwXTdaQ-Iz-8b2twN0_6GdIdE03AU4XZ7QhmHForRzgtW62ARLHlOANUv9VkgGFiOQZoHtOf6N-DM9we2Er0wHoatxNkksh02nWlt3dz35FtM535xr_TtDaCEX5SPX-G_2VG1vfIixNTg-W1k4404sohq8xE6UUa06zOKTDQ46fawn2CrYu-rINGBG1YOoj2C7TkuPma1NGxlunHKyG4xJqVDodQySBge5zZ_bU27Uv81BR9ys5s1ggL9_c9YWU5Wl8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=eUu-ACKym5L8AGGlY_Vcd0PB0S2zPwltVP2EusJdbaUdj9xZP--1ofCPwU3jMROO-mXT1MUNstfUMWy_GJ3q5ylO9vHuJYKaFYQamY6II01l8Y4RMnnGN5ptPzcbciTJPWnwOUCoJA0TqyiJK6x9CLyvMMjpOdT6vwmVN7iy741_MnKeEqf7xbBX27JIdPmc3XizyuNPcY949i9Jv8-mKE7sDxkSQtJrKubXJ3aHXb98RUBF1u04qutWTYpYSAjKtd6hEAxKlaH9_LFrjHVrGeWti-iek-s1giwiBETnU-HSv-9jJ-Zb1WyymnvqHOeleRzbvjKmLnXwuPLfsnC5Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=eUu-ACKym5L8AGGlY_Vcd0PB0S2zPwltVP2EusJdbaUdj9xZP--1ofCPwU3jMROO-mXT1MUNstfUMWy_GJ3q5ylO9vHuJYKaFYQamY6II01l8Y4RMnnGN5ptPzcbciTJPWnwOUCoJA0TqyiJK6x9CLyvMMjpOdT6vwmVN7iy741_MnKeEqf7xbBX27JIdPmc3XizyuNPcY949i9Jv8-mKE7sDxkSQtJrKubXJ3aHXb98RUBF1u04qutWTYpYSAjKtd6hEAxKlaH9_LFrjHVrGeWti-iek-s1giwiBETnU-HSv-9jJ-Zb1WyymnvqHOeleRzbvjKmLnXwuPLfsnC5Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfZS-an4akhajGpgWmahB9zESHPwEV5_MM9MPuOCOF61O8e52yFdBhXjPduZoWlGH-q6bBAkGema-JmYxI3Kk-SFxay_Hc8Q0PhBA5ASTf59MjJ1R5Fy72n3gIIQxh633hYhT1VFBtlLoDqH21GRbzLTQTD8kns8SlPxKBRoDzAK136ovtwv9EWjugUUetMYfDK38-a-7lSyuznshZastgTPDRdKwD9kztYTQROxXxrBpSwsfNAMh76Ehbrr6SrKNr5HgPfPo-XyKx6IQZ-fkuIxd-ZG6kU6zeHqE7W5MyWqPBJ9gbr9HndnZ37N-VHS5GwWkgAGbwzNKhjlyNIsJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4Q4CaxOn6Bu-aIGNST12ufImhSpTuClbZGYYxh8IRk-mPFs1CebuaQz98ClFSrBQvNJWQP9J6ljxp3Nd5iZ5emwm0uA-QV9mZKebiDR9ay2gp18bowFZFsuGic76ixnrenFDr8hLwhFljx08CU893sKcHGo3QgeZtGAqYmpLqc29W6vMsxN0z_ZSqzYzMMaIO-a-CCslW23gPPyy0l_xF3HZDxl9QxNiw_-LMSXVB0Uj-T41STRtyCbxoibQSCpQlDIOi9QklJKhhWqDXNY8Z8QvLSdcLRr7AtktF3J4LVcAFyTimtaByT3g07YLmz4Udmcojwnk8DkZeAgyEOttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZRgtfd4iAiAzAmqHT_1D8KXQxPRaQAk--qJrvi7T7muGUO4nJDJfufU1_lPRhV-6WAKsuYczXhGbAzS_H-iEeEs-8UoFGJn4tWBS4aruNc_RH97GxQApjMEMCxTW_ipNRK8opuD1TPTabVKHXbkvDkwg03WIJe0ppY5dHlvCCPcQvJ9ZQVkTSqWaHMym681hyW_gxZD3tjFVjNHuY0-P0qaMmJC-S3-rDU4tpobI07vUkcH9sEKzJWeYDoIuvr7AlPPRyTwA3g7BvwIH2Y6k_DDYfa7SpbPR94R7kyFtcManEmmkh5MvM8X0D1WDlItRbUie1uWRhcktvDUzncFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=AQdrDME0PAM7U3VSnnGMvC45HB86V_J5KbCqus2fRW-IKcgSRFaFyG6czYD_EcI-HPQa7WoWOutB0O9J6P_DISxF0N6K50JvQiVd4GXPq0TkrEkr64LrVIIKrqOTQJOpVHj9nlDBk_bv4U_-LdOeOxibviPI7hu-eVmZPN26Vk9Ckksy3L-zI_ETGwNdzh0JThxm-aljKNNSPEPuziXm_KFUA7wvCnhqw36yNz6XAsaigm2RHf4pAtFysdQ0X32AT1PA13dgzNGcF-sh-pH5o1vbTb3ka26MHfG6TQkpFeQEIcAjYwMJ6KcRxY6KagmhzlwDl50ZQ841S6_Qc9iPIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=AQdrDME0PAM7U3VSnnGMvC45HB86V_J5KbCqus2fRW-IKcgSRFaFyG6czYD_EcI-HPQa7WoWOutB0O9J6P_DISxF0N6K50JvQiVd4GXPq0TkrEkr64LrVIIKrqOTQJOpVHj9nlDBk_bv4U_-LdOeOxibviPI7hu-eVmZPN26Vk9Ckksy3L-zI_ETGwNdzh0JThxm-aljKNNSPEPuziXm_KFUA7wvCnhqw36yNz6XAsaigm2RHf4pAtFysdQ0X32AT1PA13dgzNGcF-sh-pH5o1vbTb3ka26MHfG6TQkpFeQEIcAjYwMJ6KcRxY6KagmhzlwDl50ZQ841S6_Qc9iPIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwWVgBrjdjqurfq1R-worJAwz3EhQkQQHM8AUaJ_TRvSCdXIvEKrMeYA1n4zusw3r5SBBuSxcLnUtBETmaMd2amu9NX7sFCx3lr1sjibgtACtaElvHsi-M9ld8MC7SSllyuUKWxBa2TqgPZMekd3jx1k8qbemazcCt6TXEKGpAVb8D0doCf4oX5bED8Z9-EjO0QO23Tq9fAuFBDiy55G_n-uHgSikZ5HcCwKaDGm5_vJ9NwPuj27I_U3GR2XgtD1CqInIb6rwvHGCuhrl1-TfyEXmlXdWGYm-c1BM4Gbvchxk_o4hBf8XAi3CYrBZtWJ8rBwzaDBm6wT5gt_Wr-ZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96fp4gJSWkwRD8ngc-mnWb-XUKJYdLTHeCSBon1cPZW-VD-zSiT_hJYg1hvyppkDwmmOKGAFYLRtzMNiXh5dgrK37wFsVenA0UKTMxy4q3hAzvP4RKJQPNTDwtyb-eTUwOELMqT39GvW650HWjlwDUmSK16Rn8WCt9x_zV90i84QCDZOxUbm4ogMbcB7bAp4jd_Vj-uW7aYpJW4VdjZhaEr-sq6E1sSyw7yl8byLZdTDNp_RjdhZYdKPQi5dw_ro4bReU1yLUGz6d6mk0S4_yTCNkowI09ajvMaDbsdERPiV0x3VHSNAIPKioEGR13cAzKlcNcrsi6JGZZD1i1Png.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=G7giyEmF-56vy4BLHEc4-fcfOjqfTiA_4em9ESsIi9DUBr9pWCo2O7LpAr4KbRMdlAKGRWysTYyqchAyQJ3q8VuMZz3RJm5K8mt9YKvL11bmUmIBR8pMtBaHTtNDcIhCjkGkNPFNMHhC9LJ0Iwvf5YlIwXNTw3IgwNOfEtxR4QyJVuZX4iDrsKnK_866RvN89bkGnu7m5pDBsFPd-0x9HBtsugK_mifbcLfdpslkjtDpRGJSh1IaQ_Tu_jzSBWYSqrcdWSaHzjB2nBwiGRKIEh3QMhqBraoMfbgxyTfZFlPM86nGi1wIhOnKrY_eDNmkUpt3xJmhx19rJKrF3K3plA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=G7giyEmF-56vy4BLHEc4-fcfOjqfTiA_4em9ESsIi9DUBr9pWCo2O7LpAr4KbRMdlAKGRWysTYyqchAyQJ3q8VuMZz3RJm5K8mt9YKvL11bmUmIBR8pMtBaHTtNDcIhCjkGkNPFNMHhC9LJ0Iwvf5YlIwXNTw3IgwNOfEtxR4QyJVuZX4iDrsKnK_866RvN89bkGnu7m5pDBsFPd-0x9HBtsugK_mifbcLfdpslkjtDpRGJSh1IaQ_Tu_jzSBWYSqrcdWSaHzjB2nBwiGRKIEh3QMhqBraoMfbgxyTfZFlPM86nGi1wIhOnKrY_eDNmkUpt3xJmhx19rJKrF3K3plA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVWOD3zBaT2ty6PsVJNXi-FWPg39Z0iE2Wx1G7OAjiHu2M262i30-CcKQYLLlmyJFejD8hRP39_HNIAi8d3XfPzrSqJaWxRpMx_peLsZ6tMxcypkcL5C8bFLMYwWfXP-UupA8wSpsS3N6ZLPiSCreidZFF5m28Qhn2bZpwcr73Q4EzLzHu-skKn9eWj1olFUMnFrM-_mfHfq8J_0eKB5DLyEOm5wKuGbqWIZeOhclhynYeLzU6AKw3D2XmARKVSLV6CdoKyUmiyVS01mXOOXnW7Mzm7SIGU--RRLqjGW95ydQrwFX4lPcNDgkNPd1sC_ojH-gaE34vi-34Nb6fA3tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7K_CbQiH9qbPFZgcc9e9pgL8EZoh2lKm-gCROvtMp2Mq9GJy-K42lc2tJtNmmT_ZO7YpE2Rum0qXLMsSLTLmJAYB8ezOe9jSOGvH90w2rLVoXksY0uO-p-e54Ki7bQo5JNT0Z6kZ6YtqMieDoPiqkpaFBT11YJfpFWsySpBpypMV8xbrzMhCc4ANkRrGUkXMLZOddGlz6ZLKB0yVKRo0tDwhqdGULQ1WIwvFoXdb1HpvxmnmNydwQqrcnwSALH0z-br_2Ubt-COpHQ4Ojyzp5T4OH4OD3okSfezG543F9ZXUCAkDm27hw8BUiL2-31XcYGnWlygRrNRSyQk5UepQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSQfwzBYjD22cyEFyaBWtsNPv2W23JzMxh2tHZmKRczGVK9bOrE1anZwjYZ_lYJwqoMNc35GvrTQe1GxUrRGxmcqXXZo209RPjHhdJxXLpvUhjnV1aALw1QKiFVkq6qvYGfS3SOrxfozt7qeDfpcIPDgLqmmo_LvMHwWmFcd9mTvuz4IOnPvXvjRxcNCkTiDZm4FrxVpCDjg66caeujvfPEjkYb9cE0a1qk5-21Yj2BYYSz-cVovuKRaFwIgdYZNFarcqrmHvR0h_ty8Zs3SzesI59qb62NxWwpAVhBTUu_3aMdvKvgCFu4O6pyYkP0MplbPgD4rcCFnTRTMGlHDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFGrmLL7EvVzgV89rLQ7WhNbgxdHU8jTnjAGLIyC2M6GY8pQ4tfDiwi2xzwEa3YtozVWoSOVZeai9sd-sRt6lwWJQt1bA4czpgo3ImbrX2wcxs8ovsDWZ_ft0u3NFBJcoUIK6szohtJ6A2RUxBhEG_pcnKTWLyxUh-mMDRsuz6D_beRTCXC61qmyWDo53CM50k5H1UM2D3O5sXaSXtrBdjz0rTjlbIm6-1ixzK9Ae-e4CmraMIInyYn0Cdi9pURIV1cv369_K3x6DNV9j0eI-GD81TeM_u14TNsHmmyXuY0FuhNK9R8pkbzYvFWz_wNdVIe8gMSsCeUE-BeXnO9i3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=UWO2vWkfeEAMcKKnA5_nobCaUH8ITO8O0ive66Vl0ZVI84pXrGfptX0u1oUUNVr0RotV0yXWYMsz4emGypE5d6Wfk-7jGBkKw3Wh6k8X9Ew2eTkfVyw9_MUQWvOzLnzapGThk2mgXdJo9wBkFg5u57H_SRJ2ZnLamgO2jBw2Fzi4WN36or8PiyQZqh97un0gVstw-7TXWf2JqjQ8FEBbxuohKYvpNyLsIkyRvw77eQzHo-AC_iY33mF5oSg6I5cPioMaN8tBzrndYrSq0Sr0ukXWqzHQz8l6GAbw06oIqOSdv1kpaqwcw-bwr2T24mj31l1NuBD8Hyz2YUsUDOirWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=UWO2vWkfeEAMcKKnA5_nobCaUH8ITO8O0ive66Vl0ZVI84pXrGfptX0u1oUUNVr0RotV0yXWYMsz4emGypE5d6Wfk-7jGBkKw3Wh6k8X9Ew2eTkfVyw9_MUQWvOzLnzapGThk2mgXdJo9wBkFg5u57H_SRJ2ZnLamgO2jBw2Fzi4WN36or8PiyQZqh97un0gVstw-7TXWf2JqjQ8FEBbxuohKYvpNyLsIkyRvw77eQzHo-AC_iY33mF5oSg6I5cPioMaN8tBzrndYrSq0Sr0ukXWqzHQz8l6GAbw06oIqOSdv1kpaqwcw-bwr2T24mj31l1NuBD8Hyz2YUsUDOirWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=sPAYSdg5-QOMIM1oEvNCJUvZ_yLq0A12TeeUDhtrwY07XhNOtDwpJzzg8ngRAeNPHhPMjCCoJsz1zeawoptxRQyCfvye1zZUySbv5LQgmpoTPU5Z-ygL86fDlAZlCaE6MSMDwccdw6CPY6ODbkicas0KOoOPU-SIS0ptNEPpiyFxyO1W4_zrMKEMMGav_noZJ8Dpt53_AOHUnv5RTxKFg8_WvPYYqSuiyIREhxWjAy2oJ_sPKO1wbDRBkJA0Diyl8GazEwfju5o5v_gTuXNmd_LZTwlyYbONnKdV98Msbw69VNal5fja1W-7qmDHh45hCD1-TqpMBkEdHXJ8ZZhBmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=sPAYSdg5-QOMIM1oEvNCJUvZ_yLq0A12TeeUDhtrwY07XhNOtDwpJzzg8ngRAeNPHhPMjCCoJsz1zeawoptxRQyCfvye1zZUySbv5LQgmpoTPU5Z-ygL86fDlAZlCaE6MSMDwccdw6CPY6ODbkicas0KOoOPU-SIS0ptNEPpiyFxyO1W4_zrMKEMMGav_noZJ8Dpt53_AOHUnv5RTxKFg8_WvPYYqSuiyIREhxWjAy2oJ_sPKO1wbDRBkJA0Diyl8GazEwfju5o5v_gTuXNmd_LZTwlyYbONnKdV98Msbw69VNal5fja1W-7qmDHh45hCD1-TqpMBkEdHXJ8ZZhBmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEM1KsP3CDoMlQnq6qMZvvthckxrk-McVMrfiwIgkd53QDNj4ketDtDgLwKVLMqy7_ZzUoAmi_OwXkeDT7MRoZ1RQYuL3t5rjcyRYw7r_FhXPX5JjgFnziSCQ81giiPLNBXUhVhq57FHw9j54ZhEuy3wtLq3pqfooUnEK6ERCid2SoLwz2iLxLhaSzZypktWzn0fT64E6e0PkdW_kZ2ZSBg_tOPN3wU2u_3m9tkAkxu6AHl8KRL67kvBY0JjZSxeosig-zxw42PPF43wIpp6H03fs8D0uA29kqIVsrQoG8zPIDQ4rs7vTY-_MYFrTP-nwhV_xEhjTKM-dchmi_9dzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=q8vQ-zt0b9gxPquIwkn8nQCdHzoQu82zfEbYjtPy0EYW05chFM_4Qt4ZlHK2dds7lj769ruA_IWf9kemg2x8B6Hqttgu3RiyxzYZq804gN3P1ioFVJE07XIQMdhAL0fE3Z6xbrzQ4Z2SoGoQJ9iJO0ecJec5pFP-VtxEM4Rv5CWqTICsYvFrTq8HbPhuGUy56IufGC8XXkx46iULSstI2HXYeqA-AxPN01rxzg-_ivHXMkYwCE45o8XXTsYwk6nCi-XQkKC2kFz2Mf4d4djIXDKMeWKLPVs0vCYlfHSb5LYKOcyTBjrBsuMHhRjmeLi1QP47PlinN_duRucoCApQrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=q8vQ-zt0b9gxPquIwkn8nQCdHzoQu82zfEbYjtPy0EYW05chFM_4Qt4ZlHK2dds7lj769ruA_IWf9kemg2x8B6Hqttgu3RiyxzYZq804gN3P1ioFVJE07XIQMdhAL0fE3Z6xbrzQ4Z2SoGoQJ9iJO0ecJec5pFP-VtxEM4Rv5CWqTICsYvFrTq8HbPhuGUy56IufGC8XXkx46iULSstI2HXYeqA-AxPN01rxzg-_ivHXMkYwCE45o8XXTsYwk6nCi-XQkKC2kFz2Mf4d4djIXDKMeWKLPVs0vCYlfHSb5LYKOcyTBjrBsuMHhRjmeLi1QP47PlinN_duRucoCApQrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=qR_VJfITWcAYSiG-XhLsXOCE6Nm8YWgqaEy8OBg8WmWs36q4lSUtDsWfJjPy4qR-meeC7jsnc3jMGgoNUqlSAMG9LW5y-eVebvzmhMEXFVvSasYTh3hLMdXqVcxrwx8dMJcbtkG-QsQhhVONfTcVKDMyMCfNWAv9-JpYe0pFZuvmoiWsiGi_fsJBbvgcvCD2s1S67myceT-b1Lrq7yi6sGdG4eaYivh3oZLyB-rCC70_Ko5Dm22LKfPQW3Ao4_jt5OSr7SBLTpxx4whc9SmuBTcLzH54FtvC-p7HP8Q5TeyicKtxbhyrKF5TXoct9hrH8JVUM7H0ZwzSNLz4M3SEgjSfLChMosCqRGVRD15S5cteVSHg4bGci5VoQ3bPfuDs80o1v1yOpsjribRmHbFuaj2mL11DFsa0jRGMQzxh1ASv2RSZo6cQzLNN4aTHtso_4fsFFiRKXK0AywYfzUPBeAelARREmFHVz9wjb5plrBJ_2_QLzhndDnlpS5rDzMxhPnjVT96fVQ_GAVnZtwPSUw96_p4U_yc40f-X2Mu4FsA7rcHAg6QDBzj31BlxsTvHSeSNkjin9KrDlBmzzegnZ_flxOd-W9N0dc5YkWh-mAcPBSfBZC_PcN8v_uBv08hyeqJcnjOUe7jiJBoskOxzWE9NkebqzS9SXdaYhsugNUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=qR_VJfITWcAYSiG-XhLsXOCE6Nm8YWgqaEy8OBg8WmWs36q4lSUtDsWfJjPy4qR-meeC7jsnc3jMGgoNUqlSAMG9LW5y-eVebvzmhMEXFVvSasYTh3hLMdXqVcxrwx8dMJcbtkG-QsQhhVONfTcVKDMyMCfNWAv9-JpYe0pFZuvmoiWsiGi_fsJBbvgcvCD2s1S67myceT-b1Lrq7yi6sGdG4eaYivh3oZLyB-rCC70_Ko5Dm22LKfPQW3Ao4_jt5OSr7SBLTpxx4whc9SmuBTcLzH54FtvC-p7HP8Q5TeyicKtxbhyrKF5TXoct9hrH8JVUM7H0ZwzSNLz4M3SEgjSfLChMosCqRGVRD15S5cteVSHg4bGci5VoQ3bPfuDs80o1v1yOpsjribRmHbFuaj2mL11DFsa0jRGMQzxh1ASv2RSZo6cQzLNN4aTHtso_4fsFFiRKXK0AywYfzUPBeAelARREmFHVz9wjb5plrBJ_2_QLzhndDnlpS5rDzMxhPnjVT96fVQ_GAVnZtwPSUw96_p4U_yc40f-X2Mu4FsA7rcHAg6QDBzj31BlxsTvHSeSNkjin9KrDlBmzzegnZ_flxOd-W9N0dc5YkWh-mAcPBSfBZC_PcN8v_uBv08hyeqJcnjOUe7jiJBoskOxzWE9NkebqzS9SXdaYhsugNUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke8K2sehTbieBwakncT5YVuMpkSgOzDJnY3oaklTxApDcPhj4N8uEVhZ4Ipv9mzfqCioD9ceJBStOvOvQ3IUN5qUNgSywyMwKL6hPhXGgWM1eG7clReaYDlw1lWjeC52yF7gcg_qwLmSE9OjR-3WUMcLTP0IhcBIFuH5LuWuOhdcD9JDbCA4a3gpYuTmQ9mBCGNiBKGAPJjA40_RYwtIPzVlgKRtE4PrwkywDAqmBDjMjQQFP2QBAYzFOHdwKoNGl5O6LG-rAzJ1J5qxlKSEQPMIpzew6X_C3o5TlaUmSdAjmIvQkFMMXq1B-qz2wEmWumYwUgK0uiEisxia42hWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHK1K4K1NNyopihAkojgL1u1ME4vEpPDufADzv4BreJHb5v9NtVbBaXqWhIApBP_kuPpiqcCgGD6c8OScpbTj459z6d1boSTFEB4vd3uMoL0LEbZI0OeipRJv4_oiA_vFrScOHASMzvjl9JJVyntfLeT-WkiAXhvFc6EPf8qxmkv5CdQPhOPVmalYRIxjeKL7Vd-8ibYNUMDQWHftEenYmhXzIk2sSxzOQbAIw0XNdcn7oIGrcmTU0h61wHu1jJYvMH_vfkxqBwYUP2FTDmQD7HRokBPfEIbGXQ5faghT2SfL6JCPCT-4ViTeuB50mDFH0V6jHPmJKWkfuitU4brMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gOOHujbLXhN-Y-H80kQ-qtEcKVxoWWScQYxk8ufpPyGOXViNIZ1rn6gfjs6QG3MqHkIe2twMGXS1VnvnJydSrGwHd2AIUFdz8Kbg1cO0LRVMD5ExjXuYY9fJREXC7u8NbrfChYeLRc72Dif2xfF0AoQDW_WBvWaokwu-f_6TmeGyV1buVBJK7PQweZOEsLj6DvUKMNnH7hloINynx0qM1bU7a9x4d8KSwYenjI9n52MoZobgb2I0VkxZXDkj3CH-sLxukJIupm5wl7djTgKuOMbZ-FTl_PrhK46719iBE60lzBuz2mZLmtSYOFQ70Ze3-4hMWynZ709MOeUWHiqUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_7xGEoynhI424DKmt-TEdFUWCX7NDyv4Q6tfyZ6-tLTOo8WMlJzx3Ay2v1ZWjRuH_iyO-fZD7cCNT0OGTNgfYWRaYuVDlSO5yV7pCkOSM18C3lQ_w5THt46KcNDLhGacF8vWPktGSZOV2c8WFbIC8D9aTcmDRdiZXgtcetrgrXHNWr9zGYgOi8cVZtlRVrUAJossON9hPqWRBYjIR23fF-3J76yNkwbFSgWtK18xDrBYp59pfpxi4TSnOIXEFhvqc3n62eScu37z8VCrx9R1g9hzcwaPl0R3zX_0TMzWUJkrmE05AEGvwyYuWec-pWcyfqeYIBadiC5AkpKgrNr4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=Nt3R7MWsHiwixLBBs4T2tgNS68yWH616liFl1yxlnp-tuHIFvU6OnrQ2YMME3ah-98QFU1uzqolsA8O1DPz4lRIVPE3APQLHu5sh0647KCaUuDRUP97S9DXK-XCyLotjVdGRUcWZ_uDzjKGUAjYfTyHKGnmSwMIsmpl9jgjxgwe729_fMFVehwq5rM0rxyzEYIWvDcTxbhjW2AB1tHOTyrySiM07deVTyzP8XMxz6Z5SEpg09KCbA0GKlkpMODsH8KLukOogDHLwYDzDoNyuESqloYQQMpjciOYo2YaRA-JnpT-JUkx0X6Ii7ZxVnEoAfppppc9_76yDj0NYt-IqRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=Nt3R7MWsHiwixLBBs4T2tgNS68yWH616liFl1yxlnp-tuHIFvU6OnrQ2YMME3ah-98QFU1uzqolsA8O1DPz4lRIVPE3APQLHu5sh0647KCaUuDRUP97S9DXK-XCyLotjVdGRUcWZ_uDzjKGUAjYfTyHKGnmSwMIsmpl9jgjxgwe729_fMFVehwq5rM0rxyzEYIWvDcTxbhjW2AB1tHOTyrySiM07deVTyzP8XMxz6Z5SEpg09KCbA0GKlkpMODsH8KLukOogDHLwYDzDoNyuESqloYQQMpjciOYo2YaRA-JnpT-JUkx0X6Ii7ZxVnEoAfppppc9_76yDj0NYt-IqRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNl9UXG_YpGVlTxfUgR8XN2ggTl6N7obcsiwLgkQdymf8e7rSwWGw9J2OeHzqWRvQ_bh3hjr_KOswhAZVbUoXwH-5JkLmgFc9M-AgwAKot6M4oBJzsAZkTKwGb_1KXFmZDU_8i6xNbgCHPgztIe-WLyswaH_84FdfV1c_ilhSRMt6Cz0_-Y6veV01O8pXLRcW8bjV0rVDwi8BmjQv-8d15XoAkezGp8sCcmf3P9jpc1BypXbhPzRE5w0D3Szr2xn_vGLWmNx-siLNgAP5TRvpsA6JVvl-ZzloxI-BwnC7oDvmKttTOb5bbWYF9MukHhPCPJGxd8C4LBHC_KNAqS6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxcGOhfQ_NYtllSz7FQLW4OntAsgvO47fEUTrNv2DryOzP4uvBPDBnr4OO67-u0vzDwPOjEzmkMrWgIgvjNFLJY3lhSgXnBzNYG1oVu6BcGhZ8ZubVx49f5ksShf1TQtWqDZvYuz80I3p_uQ3TFoPbHcQYoHnekVHhcG-v52S7AVtjHfP9m7A4wpyg4kptiGsS3nE6Pf5XKuFsY1XI7HlXjlVtnavP4z6DZBBMTld_dxE6qDkWu1hy8KeunjiUBq_JScAeW0IoIzvq2PwEwewrQM7dxXVBFieqDyotDbgtAHTZxbRnUtERTRxUuY9YtM3Ya86lIqp5vQvo2N4GsJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=OmFvFbOJpVViNs82qpyST8X-JaubsP_Z3EwI6aO4pWdxM8Vl4KBLRJqYT-pRssrFBiQoF1lwyQ6ObHZmP0VeINOMUqNFADya3mdDRAsjqnD62kVXuodO7NgfBjkX0jzx8QV3o_dxjkAy8PTuBwPQF7OJ8EXmfGBMtD1KChYf4-OOvSZYwVOOLhhZmSP49lzvUwHqNVXPReS1vu4qIJkTudghwdnQ3xsRQB2jtgGdIFE11JvhWddBo8iOoldWLLXXbg9ZoV2ZgZVCzB-frgRTvbAe1-l1Jexw-npLmzms7FA3cTkUXvMzQpdRSSvtjVEbuq3GXMsxgqJvZH0bU-IgeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=OmFvFbOJpVViNs82qpyST8X-JaubsP_Z3EwI6aO4pWdxM8Vl4KBLRJqYT-pRssrFBiQoF1lwyQ6ObHZmP0VeINOMUqNFADya3mdDRAsjqnD62kVXuodO7NgfBjkX0jzx8QV3o_dxjkAy8PTuBwPQF7OJ8EXmfGBMtD1KChYf4-OOvSZYwVOOLhhZmSP49lzvUwHqNVXPReS1vu4qIJkTudghwdnQ3xsRQB2jtgGdIFE11JvhWddBo8iOoldWLLXXbg9ZoV2ZgZVCzB-frgRTvbAe1-l1Jexw-npLmzms7FA3cTkUXvMzQpdRSSvtjVEbuq3GXMsxgqJvZH0bU-IgeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=TvNeSAtilQR3WJlG3MURRbaw0-qhg88Etu6ggmZMiSeOnOw4jOat8wJxIS4bDzB_2_OUFZWS7P8asGG1cvFKuYATHUXSDbAJfIPP8pw77J2R3n7uW3QmC-stsioMjI56Qsjt45yzXVCowdpaw2GjCdfmvpU2DiuORqoUMWnUGKGPpq5J1T5olz7MsEM5oLkNg7oeSV0peqLn56GEVknCoriXW0J-svhthkwjM1Lk-NrAaziudJjZwvZY9umxYEwBfZ4PtyRzAYkVG_Kt7P6Q-ei_-MelngyocmP8qX21a2NPNV7bdcfDtctdzT7daO5vww24KsBn0pci5osxD1I9vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=TvNeSAtilQR3WJlG3MURRbaw0-qhg88Etu6ggmZMiSeOnOw4jOat8wJxIS4bDzB_2_OUFZWS7P8asGG1cvFKuYATHUXSDbAJfIPP8pw77J2R3n7uW3QmC-stsioMjI56Qsjt45yzXVCowdpaw2GjCdfmvpU2DiuORqoUMWnUGKGPpq5J1T5olz7MsEM5oLkNg7oeSV0peqLn56GEVknCoriXW0J-svhthkwjM1Lk-NrAaziudJjZwvZY9umxYEwBfZ4PtyRzAYkVG_Kt7P6Q-ei_-MelngyocmP8qX21a2NPNV7bdcfDtctdzT7daO5vww24KsBn0pci5osxD1I9vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=WxssiePEdgvMzakweW92KE2htTDwLIv_Y0Fxz5n_nAuWwAyYgz_4zNEQoV5eH1Wi8HJMyA9-ATWcFHHXSDPRVkFfxSofC2_6zyG4cv5_j_x9XgGJbLNxAETaf-WWTn32MBF2aQeiiE2tgzf-QoQzavx0Gad_GVfeqBvJQjSfhzVtLjLRWtNm8f1cQezXjLrM1ZljTEyHadR3TJyNGGWHme5af0TahO3wv7CRZnl_LIfJQjpQQIrJ_2hYjeNtv6d1WvwcX1Cj-lQCVGY3ecaHbzV3oRifnU0dl6giaSXVk5mvD3cLwyyslcdcDn1jNBLHhmig6M_jNYMhiIOFcIMXNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=WxssiePEdgvMzakweW92KE2htTDwLIv_Y0Fxz5n_nAuWwAyYgz_4zNEQoV5eH1Wi8HJMyA9-ATWcFHHXSDPRVkFfxSofC2_6zyG4cv5_j_x9XgGJbLNxAETaf-WWTn32MBF2aQeiiE2tgzf-QoQzavx0Gad_GVfeqBvJQjSfhzVtLjLRWtNm8f1cQezXjLrM1ZljTEyHadR3TJyNGGWHme5af0TahO3wv7CRZnl_LIfJQjpQQIrJ_2hYjeNtv6d1WvwcX1Cj-lQCVGY3ecaHbzV3oRifnU0dl6giaSXVk5mvD3cLwyyslcdcDn1jNBLHhmig6M_jNYMhiIOFcIMXNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=psgOt_gIXqoZ5m7lDczcebZD6NWVmaoiKwKfke5hE8I6wjQUrdNDZ8g43CkdN4bWD05f7fWWRfTu559p6S579noN_9E6hrbLaCbUTrMXME7deA_oWGuERGloZvddZQt99A9Voujk50We_ADPag99AhssIUnKXFw56Zw4KHiBQhFf4XWbz1W9v2FYg22z8z8gZU5uMKSQeglO9lDMUqRfm8CS81v4C_abYX5LJ1mzOZFBc9pMz37o6Q4MN0hAF4lcGenjL3qvM1MY03lCRst55RqvXf5CmFeajrqJ0CINzV7M9RtfknEfM4hNmuf898qxjBqC8y8uyRZq6zQz01p8TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=psgOt_gIXqoZ5m7lDczcebZD6NWVmaoiKwKfke5hE8I6wjQUrdNDZ8g43CkdN4bWD05f7fWWRfTu559p6S579noN_9E6hrbLaCbUTrMXME7deA_oWGuERGloZvddZQt99A9Voujk50We_ADPag99AhssIUnKXFw56Zw4KHiBQhFf4XWbz1W9v2FYg22z8z8gZU5uMKSQeglO9lDMUqRfm8CS81v4C_abYX5LJ1mzOZFBc9pMz37o6Q4MN0hAF4lcGenjL3qvM1MY03lCRst55RqvXf5CmFeajrqJ0CINzV7M9RtfknEfM4hNmuf898qxjBqC8y8uyRZq6zQz01p8TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=fdAPSRzDDCB4o7Zmchz_DSXayR_WcuIWV9cCGz3cCqV9FPLoGm6yJ9NSOoVbnda0HCcGaO87eHMUABUO2p0XN3WlcjlEgQ6VcUtJFURUeJGuovAqP3jy4xGa7p5Mcen5BHyHAbtrkDiuhU5gNf0U55OAqgkBz2cyWee_m0UAU8bWahWN4O6hiCtADqaR-9RHIJqFq5-sql_39wpGjzSZ_gYiBMxMhr297AIdLQbd_xal0BEsjJeXMXxMl3Kf6xffdI8iKjBSC7HMLhzmHEjfyAzmq57eIdrJjCFw3u9vB92Doq2eh0F0rbBdjHyH_7rR1UKE53Mguk7XwUbW0B5y0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=fdAPSRzDDCB4o7Zmchz_DSXayR_WcuIWV9cCGz3cCqV9FPLoGm6yJ9NSOoVbnda0HCcGaO87eHMUABUO2p0XN3WlcjlEgQ6VcUtJFURUeJGuovAqP3jy4xGa7p5Mcen5BHyHAbtrkDiuhU5gNf0U55OAqgkBz2cyWee_m0UAU8bWahWN4O6hiCtADqaR-9RHIJqFq5-sql_39wpGjzSZ_gYiBMxMhr297AIdLQbd_xal0BEsjJeXMXxMl3Kf6xffdI8iKjBSC7HMLhzmHEjfyAzmq57eIdrJjCFw3u9vB92Doq2eh0F0rbBdjHyH_7rR1UKE53Mguk7XwUbW0B5y0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=iUh9noHyWybgMH85kO982mLxuZxLVMNNoxAZr2XUVpIe4Qu21eT9j1B06PKgWoYJgACGNf6-kDMFREBH_c1owe7ihahqgl_cqL0WhO3VO1X6axAGMOcpt_NEh_YWBKqGD4WaVHpXGwH_TlC3Yw46LT9FzkFutUi_018eedwxVhdBl4yh3eTAWMqv4fUVdKVE9Rh4lNZ87uh_RKnv-LLlfEZYtPLs4eutVA-Il1qMvm9HepEwGuuZjV20oNhLnl6x6LpFCcVnXK65-kqMGu0KbSMIuDU5uQ9KQcI-5DNsvD02kXGSvUxUYemmaDmI0VOKwuMo83rQRQD-ApZ08sJcWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=iUh9noHyWybgMH85kO982mLxuZxLVMNNoxAZr2XUVpIe4Qu21eT9j1B06PKgWoYJgACGNf6-kDMFREBH_c1owe7ihahqgl_cqL0WhO3VO1X6axAGMOcpt_NEh_YWBKqGD4WaVHpXGwH_TlC3Yw46LT9FzkFutUi_018eedwxVhdBl4yh3eTAWMqv4fUVdKVE9Rh4lNZ87uh_RKnv-LLlfEZYtPLs4eutVA-Il1qMvm9HepEwGuuZjV20oNhLnl6x6LpFCcVnXK65-kqMGu0KbSMIuDU5uQ9KQcI-5DNsvD02kXGSvUxUYemmaDmI0VOKwuMo83rQRQD-ApZ08sJcWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5-6lLyVi2V7MqtqzX4XFTmfLnJWDe8JugfYqR5dTK9zeIMqyBFE9KWZpq9KV18yEADks93CVUg9c2Kc5FYnUgT1Rbf3kQ7W8UEfIrYEuBNU68yQotXApgSjuNnBYEw4pv-F-KunBKAdU9r4J_-Ob3zsQA83hqUpJBx6yWjQnOE_y4FZ_0NF55o8IwT-xQTYxc4aF_vDFX4LG4WXemW6N7zJEYNq0BfEdCaICwazkd373ZdPLvoSxXjycSeHoD5wI9kQSTObc-oGSCDY9tyoY0AcdeJiwzZvFJKBGe84dM9z0QbQQ7Sr4qQVfDEngPDCBpEXj4w50TCZVqM98JIOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwyhX9S0v938kRqzCO02rcxVWmsalclVfDaz4NKuGqFTWdhwgPmf5rK9zvVgTKBVTnoOhOlUmyxcEC3iPj_FvR2n3muLG87AzdCvvRAzMal6OwPFagoGz1lDfwxsakbsGnIUwJnE5pJHz4hrokAehUjZgHw0-odl2Z-hBjIyner6xbiGmUWcx5MQDIJYrf9dKiASptoTbkBYozEyv2z4YRd3koTWJ6utQldtMzGtmqLVTJVV2vlhJ1hfNE7Gk8BJ4oeOPWDGQxJNDeUoAp6yllZ201duxkSfLNEGoPMrHkPMAN8Kjl-jlinuV96Mp3txS6ME0b9U26WTYqkAtAaS2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8h7NgZvBOk5NNNlLo_YQFDsz_KSLkFtezlE7vaUOpWPVHI4RmGbGtHtVwewokVdU4XCwzMluJpKoh_9pkVYNxXf5FkigV1awBKdcM7eGbJ9mQX7sDU61fkFUJI9kDN6t3BB47WQYps3gU0M82i0FaJyAD5FGvNyUmk69AGGJzcG-ldW0ibK4zL-wJVC6T7_aiumdwX2osHsSqvS4hu14X-B93VKvKKSjorQmmm7pwKIJvIs8WMJDf8F16hKcrlVnvWt6HcZRKDbqAVRfWNB6gEUyf7GyA3tvLf5buKdMHUHM3AFyk9o4t3_yplCitdBZwvg218z4BKmLmuYi2wuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=FjfI6_L7mNQESPQxXNbS910EW1hmZKgPqh1t9bi0JmX9IqoHNiAJfMT-xxGT_NgfNpBatrByiRDWU6bgRNX_3MW1xHtfuXiyYQmqSzrddkErlazvVymfvGlSFjWrEVdGpCkrIInuRFpJ1NIjlYVhrcb1-QgWyRXHMxcup5WdhqRrtVfJUt_8dSrw_cb8NJRCzzEYr-UcjOsUih-eEyuHeYMyYIght21wXvLVawAt2Ffajat_yt9g2cXRT-8NK4deZQ122t8KW6RfsGzwNlGBH-_KBYXBU5-lBRUV501P6E_mIWl7Y0KVDa1gNF3rXLE9Qtp1EJGttgcWHfQb3c1dgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=FjfI6_L7mNQESPQxXNbS910EW1hmZKgPqh1t9bi0JmX9IqoHNiAJfMT-xxGT_NgfNpBatrByiRDWU6bgRNX_3MW1xHtfuXiyYQmqSzrddkErlazvVymfvGlSFjWrEVdGpCkrIInuRFpJ1NIjlYVhrcb1-QgWyRXHMxcup5WdhqRrtVfJUt_8dSrw_cb8NJRCzzEYr-UcjOsUih-eEyuHeYMyYIght21wXvLVawAt2Ffajat_yt9g2cXRT-8NK4deZQ122t8KW6RfsGzwNlGBH-_KBYXBU5-lBRUV501P6E_mIWl7Y0KVDa1gNF3rXLE9Qtp1EJGttgcWHfQb3c1dgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=XsJW7AWFyptqz0PSHJUEONIXWUAcXy9WiBeAT0-nC6oTuRS6KjZ3f-h11J9q0nNxg_kjxJQoBy5557kj0yXf41yCSORJhz76aZ41Ue9ZrTwrtoYB0aHTtAIESAr6u80s6jv9kwvsdu8qaYayUm4L4PQxp9NbhkG37_cszdncOvt0opsrJeXolA9ARTGVrfbPcE_fa4Gn1Or9i7DVfwhDrS6INA4UuewjLlyP6DmZj2D3Zt8wdQkIzgEmy_dh66ITU1DEMKS7RvaMfvlBJ1VCABBrTjdAcfiED4H1rd8LFLtF-MoXJAD_bSDrMN4mmIan2R7Hf8KyTq8M5oy1-c3H3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=XsJW7AWFyptqz0PSHJUEONIXWUAcXy9WiBeAT0-nC6oTuRS6KjZ3f-h11J9q0nNxg_kjxJQoBy5557kj0yXf41yCSORJhz76aZ41Ue9ZrTwrtoYB0aHTtAIESAr6u80s6jv9kwvsdu8qaYayUm4L4PQxp9NbhkG37_cszdncOvt0opsrJeXolA9ARTGVrfbPcE_fa4Gn1Or9i7DVfwhDrS6INA4UuewjLlyP6DmZj2D3Zt8wdQkIzgEmy_dh66ITU1DEMKS7RvaMfvlBJ1VCABBrTjdAcfiED4H1rd8LFLtF-MoXJAD_bSDrMN4mmIan2R7Hf8KyTq8M5oy1-c3H3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=VRD1U3ffHTbB-GgCXIKlB4GUdurXTcQwQo_9YjEkhH4tiCaAu7s3g5mFO1DDXw07ipxJ0TV3uzIBPNZSvgWiiblKp8nY5NjtLu9o_h0zZ1AD2pNoQDKpNvu3hB5Fa83jrkt6JH7Wfs8RYdQW_aoynQ4wbz9u07DEkJqNjLg4nyupAUsxwnGMvUZSfggpm44ZqpwiNUGQWBcTIsowaDSK30Hqm07T4vUvZtxScIEVz8mUJQKQ7TR0mHSKHAnn52VT5-cKpxuffQEB2dXPNPBIl-kPPU3sRWaqLDX9gsque5_9YlH8U2tS1MKdV3LGw_9uqm5qZv1Rv-ERpDz0qhJG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=VRD1U3ffHTbB-GgCXIKlB4GUdurXTcQwQo_9YjEkhH4tiCaAu7s3g5mFO1DDXw07ipxJ0TV3uzIBPNZSvgWiiblKp8nY5NjtLu9o_h0zZ1AD2pNoQDKpNvu3hB5Fa83jrkt6JH7Wfs8RYdQW_aoynQ4wbz9u07DEkJqNjLg4nyupAUsxwnGMvUZSfggpm44ZqpwiNUGQWBcTIsowaDSK30Hqm07T4vUvZtxScIEVz8mUJQKQ7TR0mHSKHAnn52VT5-cKpxuffQEB2dXPNPBIl-kPPU3sRWaqLDX9gsque5_9YlH8U2tS1MKdV3LGw_9uqm5qZv1Rv-ERpDz0qhJG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhq_R8CEm_KbM-qKuyBzDe_TyVmnbDgTN_3tIoICnLHi5frEEKtAzL736S8v-JYjxMnbA5gb1qE1Nc-xnvTg7b1ctkeG__236jDvGZE9rpSxbVrYTVatHWsN-LzjGng9PCyFZxoI6aGRoMkcDmkaCS4h56rZ0xWxIrfb6OUvMrDQM61F-wC73zmf3T_xsTpPakJx2lMSnI9bWrfq5TU2Mzpm2vNMhCXytj_m9-dtU680LyWk_3enNl2IcqCoy8dgfFAZcP1QqwgGiNZ5-EWSa5d1PKK1b9IC5uyX_hXLrO_StZXI2c7dy9wYU_-Kj9bv1P_ThyJIxPcQdH9pIO7wsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Es_w4Pg9SjnWUjjxyLmFPdIVBC4Mhx_UUz4Kh3yYiXsqQj1wSx-7xvm_6NNOMyqBdxAOoSNDXtx5raiSf6PycYnQu2kUx5RBkcRN2ptP9v4Ga9dip9t8aMaXxd6-tH5kpvIKUVI3dw0cfdek7WtXZZ99b3zM6uKk86enGymnBqXx27sk057-QNVHgRqeCmUKHF41JrN_Kn9uIqwKvt3cmJebNA2QX3koh_z-DA_2OqgNRn6lC59xz8XJ31ODeTNqbzYea_JMuPA8pA_OcJXm_USyvy9iC2rYC8mzRVy5gqnX8Jg4t54SyIu4xOtv94lVhbe13VcfMQUSelLGK82BrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Es_w4Pg9SjnWUjjxyLmFPdIVBC4Mhx_UUz4Kh3yYiXsqQj1wSx-7xvm_6NNOMyqBdxAOoSNDXtx5raiSf6PycYnQu2kUx5RBkcRN2ptP9v4Ga9dip9t8aMaXxd6-tH5kpvIKUVI3dw0cfdek7WtXZZ99b3zM6uKk86enGymnBqXx27sk057-QNVHgRqeCmUKHF41JrN_Kn9uIqwKvt3cmJebNA2QX3koh_z-DA_2OqgNRn6lC59xz8XJ31ODeTNqbzYea_JMuPA8pA_OcJXm_USyvy9iC2rYC8mzRVy5gqnX8Jg4t54SyIu4xOtv94lVhbe13VcfMQUSelLGK82BrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=AaDGgx5L1oHGculzU7khVt6kUKjAnrdhf3yHY9dAu_sEx2MC-LsUwPpu4VEIR9xDUWYODOkrLqkThXgvsJMAdtp5Qq8BVrcMe1K-OangnWjJhAP-OjG3wPlJOHEgZkOLihG_4L1NLq4EjHo-brVLBBcic8F0VF44NoiWkwMsIeKulmxZIBeXXgFkCrkOUaAU6XKKQL7Z5zl06tIbQ9wBXLWGIojDttN8DSg4fCmmZnqlin7tHxklJqLFBGvbJmCfeo45qw_N6PhCevRVQTgiDxfhJgoN4wG5-USz6ernexXnATCRkWq3Ftq4kBAziLf76mcfTgNaHaXkxaZCLs2aSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=AaDGgx5L1oHGculzU7khVt6kUKjAnrdhf3yHY9dAu_sEx2MC-LsUwPpu4VEIR9xDUWYODOkrLqkThXgvsJMAdtp5Qq8BVrcMe1K-OangnWjJhAP-OjG3wPlJOHEgZkOLihG_4L1NLq4EjHo-brVLBBcic8F0VF44NoiWkwMsIeKulmxZIBeXXgFkCrkOUaAU6XKKQL7Z5zl06tIbQ9wBXLWGIojDttN8DSg4fCmmZnqlin7tHxklJqLFBGvbJmCfeo45qw_N6PhCevRVQTgiDxfhJgoN4wG5-USz6ernexXnATCRkWq3Ftq4kBAziLf76mcfTgNaHaXkxaZCLs2aSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyyNP6_UukZ2zmrCdnmMbfcNCWdb2z0qDY6w1TQHcV38dvfIStMycZbrJpD76pkFmRZzBc7fX7e3y5YGYfwppb78OUVCGRbx2-SMG9FTDe8ok92SKavzjnzeS0MquxL5IorqOjRcI6RFx6d56eB7F0TwI15y8zg3LumROXHMkoMdiU3bOKD09DTp99BB7u1m9FL4kynpOqGbq5hWIqHlOKvh3wZMgT99HNUjoa6Xhvv1Vgh4OjnjlvM0xKNX8ktP7kYirvXqZETqhiUHlaFlQuXCMW8JP9otvBtZASf8t1ctHJRc7nM3tx0Rx0-XNQi65cvCmNPgBr35fMbhlqHEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
