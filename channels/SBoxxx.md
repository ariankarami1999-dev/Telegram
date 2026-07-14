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
<img src="https://cdn4.telesco.pe/file/vtADaINdUsgJ6_UqxQh3PqFseAoSOQL24-lz_BF8IWWFNgPi5DpS7-tfzEqH97k0lWwxjGSaQe-YKemQbLfIEzP1KFoZmZ8RXtJkwXa54Y5Py1pPUC13Uf2_1DPcEES0wW60YSYR28B6uflKOE5ME_gvCgLhpO6WMD72HHIaA_-14NRCFKwlx7om3TM2eETn6mVm8qAA0sxinjeKN_X7b-tBPZt4WF7Y1nJR_B8DvLfGduSWwiBmoKnWaRLKAJ5Igp_iKy11R1WIQB6hkXyfE9M1FX37v-mhLt9JnYp61_tXNiMPaJarJbfKxeJWh9eCLFnz0mfvOpHwp1iD9QGaEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 22:34:32</div>
<hr>

<div class="tg-post" id="msg-18748">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2Q_P7HLwcZY2dDVlUJVS8ynHsV7MSmNeET-Oq3O_MoZb3XaQK2sIy5HGS-4eNz_j-gnO5SQkjCQEMwGY0m7F6fg5uUpqQQ2566JOsVB06bSZCeoU4mcaxaAk1L3bIO04_iU7eLpdIshLO_uqGWGkXW1-FFsqZF71MzUHhQ_950zJ0E1doWzGelQlJMuwYbIPlxnAFsMW9zUHLL7STyM_i1fdLevioiZoHFeAT2kur6anr0xMEbonWxeIVpjw229s-SZc2nPeZhhC_RoydAAndxfud5RcoapRq3J2lIGuuWOzlP8Vl6epmwZQ9RGOVbrEBtOnQzv9rGFFDCJf1xdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید مرندی:
برای چند هفته دولت ترامپ در حال تدارک حملات هوایی گسترده و تهاجم زمینی به ایران با حمایت چندین کشور عربی است و  ایران بی‌سروصدا خود را برای یک رویارویی بزرگ آماده کرده است.
در صورت آغاز چنین عملیاتی، آن حکومت های عرب خلیج فارس دوام نخواهند آورد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/SBoxxx/18748" target="_blank">📅 22:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">موشک ایرانی پر از منور بر فراز بحرین!  این منورها پدافند موشکی را فریب می‌دهند تا با شلیک های پیاپی، ذخایر موشکی شان دچار فرسایش بشود.</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SBoxxx/18747" target="_blank">📅 21:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18746">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یک مقام آمریکایی تأیید کرد که نیروهای آمریکایی در حال حاضر در ایران حملات هوایی انجام می‌دهند.
شبکه ABC|</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/18746" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18745">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پایگاه شیخ عیسی و ناوگان پنجم آمریکا در بحرین در معرض حملات موشکی شدید قرار گرفته‌اند
خبرگزاری فارس</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/18745" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18744">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ به نتانیاهو دستور داد نیروهای خود را از سوریه و لبنان خارج کند - آکسیوس</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/18744" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18743">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52c0b59bc.mp4?token=Qc-DHlL3YOTNPkKh2dUnv4O3_RUGQMOdyaB4uRlwMjEUMrIXTvq-TfNk-4gk2eVgaocHtlzS5a5HbLigtJvvqlyvIiwWw3rzGcL9sZdHPw2QumnhBXn3mv3uQr-b9yLcf0Vmut0OJ322XyDThu5YvnpXT8JCSRNNL-VVCFNJKVDfioNMx2ahI61-yt7mi_SUJC6Y7Lk4Rii_9KHjENUeA_Os3hYdRlltVY5DZO2vU4aDW2jkp4I6GDWAbBt8MMCpMyu--g0y9RLMohHOul9Ul_X7VUxAyxwRZ_7tBQi0sBKsCC5wXVzpceIf7exz-7Rgw9mGEGlQACC64ioOrjsoBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52c0b59bc.mp4?token=Qc-DHlL3YOTNPkKh2dUnv4O3_RUGQMOdyaB4uRlwMjEUMrIXTvq-TfNk-4gk2eVgaocHtlzS5a5HbLigtJvvqlyvIiwWw3rzGcL9sZdHPw2QumnhBXn3mv3uQr-b9yLcf0Vmut0OJ322XyDThu5YvnpXT8JCSRNNL-VVCFNJKVDfioNMx2ahI61-yt7mi_SUJC6Y7Lk4Rii_9KHjENUeA_Os3hYdRlltVY5DZO2vU4aDW2jkp4I6GDWAbBt8MMCpMyu--g0y9RLMohHOul9Ul_X7VUxAyxwRZ_7tBQi0sBKsCC5wXVzpceIf7exz-7Rgw9mGEGlQACC64ioOrjsoBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موشک ایرانی پر از منور بر فراز بحرین!
این منورها پدافند موشکی را فریب می‌دهند تا با شلیک های پیاپی، ذخایر موشکی شان دچار فرسایش بشود.</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/18743" target="_blank">📅 21:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599f22b724.mp4?token=KbZ_gFpmzi-2gC1dDFgUnKURqdGD4zvZp2O-UM9p_-8b8SkV8LyMjHqR51Fxh7--LUZcr7iZT9y-IMrIROnbuZbbN2wlS9h63knJzkHlUhJrPKg4U9t8nT-IE69w2Hopd1iT6M_VmIxfvThty3IVhdTSdY6GSeT73NIPHuRf6k05rjYgZUnsfVL4zJxXa9GlGuOTUfCgIr-ZAdYskW_qszqOv5Z51RmJD_M9nXDu33vkQr1VcNdm-cpTrHSuE_F6miYWSK1YR_3aZ-8zByB6TB0cRuRipv8PT7oK293-awILMDpAbFfIhJT1qQj0Kre7ZT_TMh1hBvtH4Ett0ZSoIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599f22b724.mp4?token=KbZ_gFpmzi-2gC1dDFgUnKURqdGD4zvZp2O-UM9p_-8b8SkV8LyMjHqR51Fxh7--LUZcr7iZT9y-IMrIROnbuZbbN2wlS9h63knJzkHlUhJrPKg4U9t8nT-IE69w2Hopd1iT6M_VmIxfvThty3IVhdTSdY6GSeT73NIPHuRf6k05rjYgZUnsfVL4zJxXa9GlGuOTUfCgIr-ZAdYskW_qszqOv5Z51RmJD_M9nXDu33vkQr1VcNdm-cpTrHSuE_F6miYWSK1YR_3aZ-8zByB6TB0cRuRipv8PT7oK293-awILMDpAbFfIhJT1qQj0Kre7ZT_TMh1hBvtH4Ett0ZSoIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دیگر چه کوفتی است در شیراز ؟!</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/18742" target="_blank">📅 20:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18741">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">به نظر می‌رسد حشدالشعبی هم …</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/18741" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18740">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:
به نظر من، و این ممکن است برایتان عجیب باشد، اما خاورمیانه در حال متحد شدن است.
ما در حال از بین بردن زورگوی خاورمیانه هستیم.
ایران، زورگوی خاورمیانه بود. آنها به عراق زور می‌گفتند. آنها به هر کشوری زور می‌گفتند. در سراسر خاورمیانه، ترس وجود داشت.
دیگر هیچ ترسی وجود ندارد.</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/18740" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18739">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مهر نیوز با استناد به منابع خبری گزارش می‌دهد که رژیم اسرائیل حملات خود به جنوب لبنان را ادامه داده و آتش‌بس را نقض کرده است</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SBoxxx/18739" target="_blank">📅 19:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18738">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/18738" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18737">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:  او جوان و خوش‌تیپ است.  من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/18737" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18736">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8fda31b18.mp4?token=pEuRsQP-iNPZfjz8KyOoq-7mdOWFHJNGOGNuY1k0c8VkWKHAuoeBFk_-fav6fsdoFe8Mog6ajUEkB3TSpAc-aqomnsLrVM3NDCj9fX5CJl6q1VbwSkPU1V0WvlM5EVQkyEJc-yLOBP82aUaBBhNxRWD7JU-23-fMMPP6I4YEfUrQRS6T55ywmSy37LbIF3y56WUt9tB83QNa3ksC64q2BAHnxcrZ6-EeeoKQjLNDuYAlI3vsrivm1rZm6ok8fBDtGZXemDeJUBNBY6LGemA61hqQL9MobC6kPzSV_sdWLhAPh1xQTEQYT2bIgzTVKXMkJ01QUhkA2dGzpO3zqsZDMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8fda31b18.mp4?token=pEuRsQP-iNPZfjz8KyOoq-7mdOWFHJNGOGNuY1k0c8VkWKHAuoeBFk_-fav6fsdoFe8Mog6ajUEkB3TSpAc-aqomnsLrVM3NDCj9fX5CJl6q1VbwSkPU1V0WvlM5EVQkyEJc-yLOBP82aUaBBhNxRWD7JU-23-fMMPP6I4YEfUrQRS6T55ywmSy37LbIF3y56WUt9tB83QNa3ksC64q2BAHnxcrZ6-EeeoKQjLNDuYAlI3vsrivm1rZm6ok8fBDtGZXemDeJUBNBY6LGemA61hqQL9MobC6kPzSV_sdWLhAPh1xQTEQYT2bIgzTVKXMkJ01QUhkA2dGzpO3zqsZDMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:
او جوان و خوش‌تیپ است.
من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/18736" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18735">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارهای شدید در جنوب ایران و شمال کویت!</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/18735" target="_blank">📅 19:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18734">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">به گزارش‌ها، حداقل چهار موشک بالستیک ایرانی شب گذشته پایگاه هوایی پادشاه فیصل در اردن را هدف قرار دادند.
گزارشهای تصویری نشان می‌دهند که سامانه‌های پدافند هوایی نتوانستند این موشک‌ها را رهگیری کنند.</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/18734" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18733">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارهای شدید در جنوب ایران و شمال کویت!</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SBoxxx/18733" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18732">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ:  نفت مانند گذشته بی‌سابقه‌ای در جریان است. تنگه هرمز به روی همه کشتی‌ها به جز ایران باز است - به دلیل رهبری دروغگو، خشن و بدخواه آنها که آنها را در مسیر نابودی کامل قرار می‌دهد.  ما محاصره کامل خواهیم داشت، اما فقط کشتی‌هایی که به بنادر ایران می‌آیند…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/18732" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18731">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqLBRNlJPvjHkorpLs0KQ1zYq_mAFZ3CjfeLV6U5XutTf7QURzIg7JdiGnKAhGxSND5IPmDERlZCUcIylWxOkS8eOlwnZSu-dYhNdirnusala8KmWgZ97oqhS7ggH8i7WElKHSr8mf9l-bo96I092GPAuI3VLTCOkM6kPBYGp5ON8p6vJiqODEVi6VF-nj-Ce31k5uGfZby_QrBfh0fyTk1w-yWKtF1xhw7nkI86bZCIG_WxmMveKFnczCS6lelvX_f2xpExL7mp6QUMgi9gTiAjd9041ma8AMvV2PNIWd5PgVtKpNrfrelusuMr8G56-Vd4i5dfbfx4UFbVqzQy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:  امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!  «ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!)…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/18731" target="_blank">📅 19:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18730">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هدف قرار گرفتن یک تانکر نفتی که پرچم لیبریا را به اهتزاز درآورده و متعلق به امارات است.  3 نفر از خدمه کشتی در میان مفقودین هستند</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/18730" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18729">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هدف قرار گرفتن یک تانکر نفتی که پرچم لیبریا را به اهتزاز درآورده و متعلق به امارات است.
3 نفر از خدمه کشتی در میان مفقودین هستند</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/18729" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18728">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ:
نفت مانند گذشته بی‌سابقه‌ای در جریان است. تنگه هرمز به روی همه کشتی‌ها به جز ایران باز است - به دلیل رهبری دروغگو، خشن و بدخواه آنها که آنها را در مسیر نابودی کامل قرار می‌دهد.
ما محاصره کامل خواهیم داشت، اما فقط کشتی‌هایی که به بنادر ایران می‌آیند و برمی‌گردند، یا هر چیزی را که مربوط به محموله‌های ایرانی است، حمل می‌کنند.
من تصمیم گرفته‌ام هزینه بازپرداخت ۲۰ درصدی ایالات متحده را با معاملات تجاری و سرمایه‌گذاری که کشورهای مختلف خلیج فارس در ایالات متحده انجام خواهند داد، جایگزین کنم. این سرمایه‌گذاری‌ها عظیم خواهند بود.
روزهایی که ایران صدها هزار نفر را می‌کشت، به پایان رسیده است و از همه مهمتر، ایران هرگز سلاح هسته‌ای نخواهد داشت!</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/18728" target="_blank">📅 18:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18727">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آیا چین آماده دوره پسا-پوتین در روسیه می شود؟!  به نوشته وال استریت ژورنال، چین به آرامی روابطی را در داخل روسیه ایجاد می‌کند که فراتر از پوتین است و با مقامات و نخبگانی ارتباط برقرار می‌کند که پس از رفتن او، آینده این کشور را شکل خواهند داد.  روسیه هم متوجه…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/18727" target="_blank">📅 15:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18726">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIi5HGLziJenhxdgIlAvpyv6T0GxysexjaUDxm4KiTwtAhwZGYYwa204plbad1qo7wRa3qkvoSC8SPgrOeLIdulyCLcM6V6VlAlMR13mpJ1pnvjsQeQuDOMsVzL3iTWCLEFxlJMzIQMCawn63xTKeGjqfhyPq4ok04hIiu8fLtwBg5pOcouA1FgOGxDNYzu9IMVaktYxMDIDrFa7XK-UbXhDDDRp4p83ZrFYlQYaVFT47TklMgOlpapz5LC1jI2Pe7Py3VecKyV48EpGI0OhKRAafD8yiUGOJS8p7ODzxd_SpA3eYoNSevSRW2f164mJIWfVOqWosYM7PzPnCMVddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا چین آماده دوره پسا-پوتین در روسیه می شود؟!
به نوشته وال استریت ژورنال، چین به آرامی روابطی را در داخل روسیه ایجاد می‌کند که فراتر از پوتین است و با مقامات و نخبگانی ارتباط برقرار می‌کند که پس از رفتن او، آینده این کشور را شکل خواهند داد.
روسیه هم متوجه تلاش‌های جاسوسی فزاینده چین در میان مقامات دولتی رده میانی شده است، اما مسکو تمایلی به مطرح کردن این موضوع با پکن ندارد، زیرا از آسیب رساندن به این رابطه می‌ترسد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18726" target="_blank">📅 15:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18725">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شهادت ۳ نفر در شهرستان حاجی‌آباد بندرعباس
🔹
بر اساس پیگیری‌های خبرنگار تسنیم از استانداری هرمزگان، حمله به مناطق غیرنظامی در غرب بندرعباس و شهرستان حاجی‌آباد تأیید شد.
🔹
در روستای سیدجوذر به یک ساختمان محیط زیست حمله شده که ۳ نفر به شهادت رسیدند.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/18725" target="_blank">📅 14:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18724">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYYtEAzWesZaEzI_M4hHXkkCZFs3_ljt0a7-W7W_E3pYi7bwljfZ60H3F1UuJdnoD-YxYw6DjSA4X7VmRfIqJUr6gt9nRIb4-gwh-Bsh7HkQsnTq308PUzFvOhCATcWoy6rKpYdPUgyvLdk1RIrlt8Siqh1bS7tPy0IXmllto5QTBanc_akLFGtZHUeVb-t8Xp-IcJg-f9d3meXXqtuxwMzgPhnGsvwcACXg_VVrNuCiA9_SRhMrRvNsWGKf-GH3f-vrAmx6Fe_VmtFhM5WGL1F9qbBdJA_CpHEhcfH58ANO427krryCPsFLLMYHOatb85JnvSkIHrJKQEyCyb84CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی که دیشب به ترامپ توصیه کرده بود برود نگهبان قبر لیندسی گراهام بشود، همان دیشب از هیات رییسه کمیسیون امنیت ملی مجلس کنار گذاشته شد!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18724" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18723">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پاکستان از عربستان وام گرفته تا بدهی اش به امارات را بدهد!  مستراح گدایان!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18723" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18722">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بر اساس گزارش‌های رسانه‌های دولتی ایران، حملات هوایی آمریکا به چهار نقطه در شهر بوشهر، ایران، انجام شد.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/18722" target="_blank">📅 14:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18721">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ضربه قایقهای انتحاری آمریکا به تاسیسات صنایع دریایی مواردی را آشکار کرد. ارتفاع قایق نهایت 2.5-3m باشد که رادارها سطحی توام با کلاتر دریایی کمی دیرتر قایق را میگیرند اما  باز هم چندین کیلومتر فرصت دارند (رادارهای پر ارتفاع؟).از آن سو ج.ا مدیریت شبکه محور روی عبور قایقهای خودی ندارد، میتواند با آنها اشتباه بگیرد.
نظارت آمریکاییها با پهپاد از آسمان، گشتیهای سپاه را هم تحت رصد دارد که با یک عملیات شبکه محور از میان چند جزیره ایرانی به خوبی عبور کرده و خود را به سادگی به بطن صنایع دریایی رسانده است. در موقعیت شبهای بحرانی احتمالا گشتی ها سپاه و نظارت انسانی ساحلی هم کاهش می‌یابد، زیرا ریسک عملیاتی بالایی با توجه به تسلط هوایی آمریکاییها وجود دارد. در کل شکست عملیاتی جدی بود و رخنه‌های بزرگی را آشکار کرد.
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18721" target="_blank">📅 13:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18720">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">توییت سازمان اطلاعات سپاه!  به تاریخ ها دقت کنید؛ مشخصاً راهبرد سپاه این است که این تاریخ های حساس برای آمریکایی ها خالی از جنگ نباشد.  از همین تقویمی که در پست ریپلای شده قرار دادم استفاده شده است.  11 ژوئن = تاریخ آغاز جام جهانی 3 نوامبر = انتخابات مجالس…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18720" target="_blank">📅 13:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18719">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18719" target="_blank">📅 13:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18718">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjUGGIr_-5LixfaLieUiJUAxqpJh3EE6uM8i-d2oJ3mlIhZxjit06mdYatA8WezHSNM2lzIzWHzDLKUJIQZKxH5RlMXxLbvOf7u_6F47HxNbR1Jr4SjZzvv1hWZxCTscWdq7swZ6QrtjBObZ5E6HhAm-O-qU7sdThhUb57s0xt42g7Vy7jd-ooNfG2-ooBd3frL91cick5FxurAbU_dCWtY51apBaBbwkrusTUZDPz466e5mMeIDIl9DZ-I7tUkIEeA6tA_LwkZGx2PB7onGZb-osb2cqEVUsb0PLrXEt3jG9-Lj2RDjabQhLt4n-ze-1PjoLHOvqgZNBAEce6XhXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی قرار دارد.
با توجه به انتشار خبر کلیدی تورم، اساساً این ساعات برای معامله مناسب نیست.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18718" target="_blank">📅 12:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18717">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 7
سه شنبه 14 جولای 2026</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18717" target="_blank">📅 12:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18716">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی:   اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18716" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18715">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک نفر دایرکت داده خدا لعنتشان کند؛ دیشب ‌پیک اول را زده بودم برق رفت همه جا تاریک شد فکر کردم کور شده ام!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18715" target="_blank">📅 10:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18714">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزارت دفاع امارات:   در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18714" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18713">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزارت دفاع امارات:   در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18713" target="_blank">📅 02:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18712">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزارت دفاع امارات:
در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18712" target="_blank">📅 02:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18711">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارشگر: شما ماه‌هاست که ایران را بمباران می‌کنید. آیا این وضعیت عادی جدید است؟
ترامپ: ما ۱۹ سال در ویتنام بودیم در حالی که فقط ۴ ماه است که ما اینجا هستیم.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18711" target="_blank">📅 02:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18710">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ادعای وزارت دفاع امارات:
دو نفتکش اماراتی در مسیر جنوبی تنگه هرمز با دو فروند موشک کروز ایرانی هدف قرار گرفتند</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18710" target="_blank">📅 02:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18709">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قطعی برق در دمای 40 درجه به نظرم خیلی زیبنده ابرقدرت 4 دنیا نیست ولی خب.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/18709" target="_blank">📅 01:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18708">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">راه قدس از بحرین می گذرد!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18708" target="_blank">📅 01:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18707">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجار در بحرین!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18707" target="_blank">📅 01:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18706">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تلویزیون ایران: دو انفجار در جزیره کیش، در جنوب کشور، رخ داد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18706" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18705">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ:  محمد Something آنجا وجود دارد که نیاز به بیل دارد.  بیل‌ها به شما کمک نمی‌کنند. بزرگترین ماشین‌آلات دنیا هم به شما کمک نمی‌کنند.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18705" target="_blank">📅 00:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18704">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ادعای ترامپ:
عملیات نظامی علیه ایران ممکن است بین دو هفته تا سه هفته ادامه داشته باشد
کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18704" target="_blank">📅 00:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18703">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز جمعه ۱۰ ژوئیه به طور رسمی کنگره را از ازسرگیری عملیات نظامی علیه ایران مطلع کرد و تعهدات خود را طبق قانون اختیارات جنگی انجام داد.
این اطلاع‌رسانی پس از ازسرگیری حملات آمریکا به اهداف نظامی ایران و بازگشت محاصره دریایی این کشور صورت می‌گیرد که در واکنش به حملات مداوم ایران به کشتیرانی تجاری در تنگه هرمز و علیه منافع و شرکای منطقه‌ای آمریکا انجام شده است.
طبق قانون اختیارات جنگی ۱۹۷۳، رئیس‌جمهور موظف است ظرف ۴۸ ساعت از ورود نیروهای مسلح آمریکا به درگیری یا شرایط قریب‌الوقوع، کنگره را مطلع کند.
این اطلاع‌رسانی به خودی خود مجوز اقدام نظامی نیست، اما الزامات گزارش‌دهی این قانون را برآورده می‌کند و کنگره نقش نظارتی خود را حفظ می‌کند</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18703" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18702">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ درباره ایران:
حفظ تفاهم نامه نوعی آزمون بود.
آن‌ها به این آزمون احترام نگذاشتند.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18702" target="_blank">📅 00:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18701">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آسمان کلیر، پرواز چند جنگنده خودی در اطراف تهران!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18701" target="_blank">📅 23:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18700">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNy27VdkhBXi7bYkB6HcfZKol3-AxmcavORHiiNyKWj5CRPKtzpIoR80Y3_qNdSsedjh-GjmLnADMUz89U13e1n0zdXy_FF83JGVdCVIXJY_6SXC7D0cdyIhzPuctIUQynmveo7vgDVXh1tHqHpWs7myxBS-eiBw3uhYby5wOV_CIuAjcDP4rxYCy28GNf_W6Bf0qcUcrBeHtukYNXor-g1kNJbiRvIFI2EQ1onM4_b4-YjLt2TGN9LSH0PSfRNzeJpmB0n9Gxsb4ECK7GEuS4-hx8IoG8-EHKQBMhCJ6TYrAIMMlt979sCOM150Mjbym5Kx6NmQ4BmNtKg5KkuQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمان کلیر، پرواز چند جنگنده خودی در اطراف تهران!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18700" target="_blank">📅 23:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18699">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یحیی سریع سخنگوی نیروهای مسلح یمن:
در پاسخ به تجاوز جنایتکارانه سعودی، نیروهای مسلح یمن با تعدادی موشک بالستیک و پهپاد، عملیات نظامی را با هدف قرار دادن فرودگاه بین‌المللی ابها انجام دادند
به همه شرکت‌های هواپیمایی در مورد پرواز از طریق حریم هوایی عربستان سعودی هشدار می‌دهیم و از آنها می‌خواهیم تا زمان لغو محاصره فرودگاه بین‌المللی صنعا، هشدارهای ما را جدی بگیرند.
ما از جمهوری اسلامی ایران به خاطر کمک‌هایش به جمهوری یمن در لغو محاصره ناعادلانه فرودگاه بین‌المللی صنعا و تسهیل پروازهای بشردوستانه به و از فرودگاه، صمیمانه تشکر می‌کنیم
.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18699" target="_blank">📅 23:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18698">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18698" target="_blank">📅 23:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18697">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش‌های ایران از موج انفجارها در چندین مکان در جنوب
منابع ایرانی از وقوع سری انفجارها در چندین مکان در بخش جنوبی کشور گزارش می‌دهند.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18697" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18696">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ارتش آمریکا اعلام کرد که از ساعت ۲۰:۰۰ به وقت گرینویچ فردا، محاصره دریایی تمام بنادر ایران را آغاز خواهد کرد
.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18696" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18695">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نیویورک تایمز: ترامپ رسماً کنگره را از سرگیری جنگ علیه ایران مطلع کرد</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18695" target="_blank">📅 21:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18694">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عقل ندارند. خب الان کله زرد می‌گوید من ۲۰ درصد میگیرم ده درصدش یعنی ۲ درصدش را میدهم به شما!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18694" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18693">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عباس آقا عراقچی:  رئیس‌جمهور ایالات متحده کاملاً حق دارد. هر کس که عبور امن و ایمن کشتی‌های تجاری از تنگه هرمز را تضمین کند، باید برای این خدمت عوارض دریافت کند.  ایران همیشه نگهبان تنگه بوده و تا ابد نیز باقی خواهد ماند.  ۲۰٪ البته خیلی زیاد است. ما منصف…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18693" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18692">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:   تنگه هرمز باز است و باقی خواهد ماند، چه با ایران و چه بدون آن.   ما محاصره ایران را که به این دلیل نامگذاری شده است که فقط کشتی‌ها یا مشتریان ایران را از ورود یا خروج باز می‌دارد، دوباره اعمال می‌کنیم.   تمام کشورهای دیگر می‌توانند از تنگه به صورت…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18692" target="_blank">📅 21:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18691">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18691" target="_blank">📅 21:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18690">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLF4FzFVe24eMf1wwTXfAxJgJdC6ZkuZNy832_IXheo_GZ-KagmLZiJi8Fpz8aLa9vvGdANnC0-lQvRMrJQIh5cbboFl1Ktf8J4L0f3tpGCtt4lUnN6Fo8UHUSnDmcNb0ORmxYH61X23G3b7bCxJszDAG2Drl28ljdm0_MD8jR8lVVyE9S-p0V3s93blC4IDgzNkntpOWkaUy8OoWgu1dUOV-937lm3HbWZrRS27pEempEYU_7b0_9K6gozOZAlr_4sHQbcsF6K_1Byd_huU0B1e-1o5kBJViSfUsC57UjXvvOh7b-hREutW5xxXkuNfDu-oQj2jZemt9Zf6MULg5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18690" target="_blank">📅 21:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18689">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزارت حمل و نقل یمن: حملات دشمن سعودی و هدف قرار دادن فرودگاه صنعا، تلاشی عمدی برای محروم کردن هزاران بیمار و مسافر از ابتدایی‌ترین حقوق تضمین شده‌شان است.
🔹️
ما از سازمان ملل متحد، جامعه بین‌المللی و سازمان‌های بشردوستانه بین‌المللی می‌خواهیم که مسئولیت خود…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18689" target="_blank">📅 20:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18688">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حوثی ها با موشک بالستیک پاسخ سعودی ها را داده اند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18688" target="_blank">📅 20:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18687">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">— گزارش‌هایی از انفجارها در استان عسیر عربستان سعودی منتشر شده است که فرودگاه بین‌المللی ابها در آن قرار دارد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18687" target="_blank">📅 20:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18686">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">— گزارش‌هایی از انفجارها در استان عسیر عربستان سعودی منتشر شده است که فرودگاه بین‌المللی ابها در آن قرار دارد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18686" target="_blank">📅 20:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18685">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18685" target="_blank">📅 20:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18684">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256741d101.mp4?token=U26kziutKLO_khqpYtWWPeEBxVDP5oHpyLhW7ucrLvri30zjJXuIAM3F-iI_3THLMW4VgnIe22z1y0LAU8XA2czcYS9hnu_CuoH7a4zeAnMnJ67kiCAlC2N_GCyBUfSU3VSmrHg5hS1S5DiKmBGLosWCD7CqJBh_NTrq-Bmbq2CDHoltLtq7l1w9zuDu0pyxcmFFeB0auZzAZqIXbtoh4yo5Wnc539e_s00WecOIWcWkRVlMk8IALkEYcDFaXUJwXjr9dbXl2v2EGW38WjNBbuFAVMuXbdNLnA8lRiNmk2FI9kW07lOlMws5MSvmktW27jCfm8GU78LrQCQk_ch0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256741d101.mp4?token=U26kziutKLO_khqpYtWWPeEBxVDP5oHpyLhW7ucrLvri30zjJXuIAM3F-iI_3THLMW4VgnIe22z1y0LAU8XA2czcYS9hnu_CuoH7a4zeAnMnJ67kiCAlC2N_GCyBUfSU3VSmrHg5hS1S5DiKmBGLosWCD7CqJBh_NTrq-Bmbq2CDHoltLtq7l1w9zuDu0pyxcmFFeB0auZzAZqIXbtoh4yo5Wnc539e_s00WecOIWcWkRVlMk8IALkEYcDFaXUJwXjr9dbXl2v2EGW38WjNBbuFAVMuXbdNLnA8lRiNmk2FI9kW07lOlMws5MSvmktW27jCfm8GU78LrQCQk_ch0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی آمریکا:   برای اولین بار، یک پایگاه دریایی ایرانی در بندرعباس را با استفاده از قایق‌های بدون سرنشین انتحاری مورد بمباران قرار دادیم.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18684" target="_blank">📅 18:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18683">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فرماندهی مرکزی آمریکا:   برای اولین بار، یک پایگاه دریایی ایرانی در بندرعباس را با استفاده از قایق‌های بدون سرنشین انتحاری مورد بمباران قرار دادیم.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18683" target="_blank">📅 18:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18682">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فرماندهی مرکزی آمریکا:
برای اولین بار، یک پایگاه دریایی ایرانی در بندرعباس را با استفاده از قایق‌های بدون سرنشین انتحاری مورد بمباران قرار دادیم.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18682" target="_blank">📅 18:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18681">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مارکو روبیو:
دیوان کیفری بین‌الملل در پی آن است که به داوری پاسخگو و بدون پاسخگویی از قانون جهانی جدید تبدیل شود — که توانایی تعقیب و دستگیری شهروندان ما را به دلخواه دارد و حاکمیت آمریکا را به صورت وجودی تهدید می‌کند.
ما به دیوان کیفری بین‌الملل معنای کامل عزم آمریکا را آموزش خواهیم داد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18681" target="_blank">📅 18:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18680">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ در مورد ایران:   خمینی رفته است. پسر او ۹۰٪ رفته است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18680" target="_blank">📅 18:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18679">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ:   تنگه هرمز باز است و باقی خواهد ماند، چه با ایران و چه بدون آن.   ما محاصره ایران را که به این دلیل نامگذاری شده است که فقط کشتی‌ها یا مشتریان ایران را از ورود یا خروج باز می‌دارد، دوباره اعمال می‌کنیم.   تمام کشورهای دیگر می‌توانند از تنگه به صورت…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18679" target="_blank">📅 18:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18678">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پوتین: پاسخ روسیه به حملات دشمن متقابل و چندین برابر قدرتمندتر خواهد بود.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18678" target="_blank">📅 18:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18677">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دبی برنامه‌ریزی برای ساخت بندر جدید برای دور زدن تنگه هرمز دارد</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18677" target="_blank">📅 17:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18676">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ:
تنگه هرمز باز است و باقی خواهد ماند، چه با ایران و چه بدون آن.
ما محاصره ایران را که به این دلیل نامگذاری شده است که فقط کشتی‌ها یا مشتریان ایران را از ورود یا خروج باز می‌دارد، دوباره اعمال می‌کنیم.
تمام کشورهای دیگر می‌توانند از تنگه به صورت عادلانه و آزاد استفاده کنند.
ایالات متحده آمریکا از این به بعد به عنوان «نگهبان تنگه هرمز» شناخته خواهد شد، اما به همین دلیل و به عنوان مسئله‌ای از عدالت، به میزان ۲۰ درصد از تمام محموله‌های حمل‌ونقلی، برای هرگونه هزینه‌ای که برای انجام وظیفه تأمین امنیت و ایمنی در این بخش بسیار ناپایدار جهان لازم باشد، جبران خسارت خواهد شد.
فرآیند و تشکیل این ساختار بلافاصله آغاز می‌شود.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18676" target="_blank">📅 17:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18675">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ستاد مرکزی خاتم‌الانبیای ایران:
ما تحت هیچ شرایطی اجازه نخواهیم داد که ایالات متحده در مدیریت تنگه هرمز دخالت کند؛ نه اکنون و نه هرگز.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18675" target="_blank">📅 16:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18674">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ در مورد ایران:
خمینی رفته است. پسر او ۹۰٪ رفته است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18674" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18673">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ:
ما دیشب ضربه خیلی سختی به آن‌ها زدیم. هر بار که آن‌ها یک پهپاد می‌فرستند، ما ضربه خیلی سختی به آن‌ها می‌زنیم. اما ما یک توافق داشتیم؛ چیزی که هیچ‌کس نمی‌داند این است که ما یک توافق داشتیم، کار تمام شده بود، و بعد آن‌ها توافق را شکستند. آن‌ها همیشه توافق را می‌شکنند. ما تا به حال ۱۰ بار با این افراد توافق داشته‌ایم. بنابراین ما فقط قرار است ضربه خیلی سختی به آن‌ها بزنیم. و ما این تنگه را حفظ خواهیم کرد و احتمالاً آن را اداره می‌کنیم، ما تبدیل به "نگهبان تنگه" می‌شویم؛ شاید اسمش را بگذاریم "فرشته نگهبان تنگه". و ما باید هزینه‌ای که برای این کار می‌کنیم را پس بگیریم. وقتی این کار را انجام دهیم، پولمان را پس خواهیم گرفت چون کشورهای دیگری که طرف ما هستند بسیار ثروتمندند. و از ما انتظار نمی‌رود که این کار را مجانی انجام دهیم، برخلاف کاری که سال‌ها انجام دادیم. می‌دانید، ما برای ۵۰ سال یا بیشتر از این تنگه محافظت کردیم و هیچ‌وقت پولی بابت آن دریافت نکردیم. آن‌ها همه پول‌ها را به دست آوردند و ایالات متحده فقط... می‌دانید، هیچ... شگفت‌انگیز است. ما هیچ‌وقت سودی نبردیم. ما مجانی از آن محافظت کردیم. اما حالا که می‌خواهیم از آن محافظت کنیم، قرار است بابت محافظت از آن پول بگیریم، پول زیادی هم بگیریم. ما فقط می‌خواهیم هزینه‌ای که برای انجام تمام این کارها و به خطر انداختن نیروهایمان صرف می‌کنیم، جبران شود. اما ما در واقع مردم را در خطر قرار نمی‌دهیم، ما واقعاً داریم نجاتشان می‌دهیم.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18673" target="_blank">📅 16:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18672">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ :
ما قصد داریم‌ حملات جدی تری علیه ایران انجام دهیم</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18672" target="_blank">📅 16:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18671">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ:  ۵.۲٪ از روسای جمهور کشته می‌شوند و  به ۸.۵٪ با گلوله شلیک می شود.  رئیس جمهور بودن خطرناک است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18671" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18670">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این بنده خدا واقعا باورش شده ما برنامه ترورش را داریم!  یک نفر به او بگوید ما از سال 1367 هنوز سلمان رشدی را نتوانسته ایم کامل بکشیم.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18670" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18669">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ درباره تنگه هرمز:
ما تنگه هزمز را حفظ خواهیم کرد. احتمالاً آن را اداره خواهیم کرد.
ما نگهبان تنگه خواهیم شد و وقتی این کار را انجام دهیم، برای آن جبران خسارت خواهیم شد.
ما به مدت ۵۰ سال از تنگه محافظت کردیم و هرگز بابت آن پولی دریافت نکردیم. ما بیهوده از آن محافظت کردیم، اما اکنون پول درخواهیم آورد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18669" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18668">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">در‌ این صوتی وضعیت خر تو خر یمن را توضیح داده بودم .</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18668" target="_blank">📅 15:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18667">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزارت حمل و نقل یمن: حملات دشمن سعودی و هدف قرار دادن فرودگاه صنعا، تلاشی عمدی برای محروم کردن هزاران بیمار و مسافر از ابتدایی‌ترین حقوق تضمین شده‌شان است.
🔹️
ما از سازمان ملل متحد، جامعه بین‌المللی و سازمان‌های بشردوستانه بین‌المللی می‌خواهیم که مسئولیت خود…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18667" target="_blank">📅 15:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18666">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18666" target="_blank">📅 15:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18665">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزارت حمل و نقل یمن: حملات دشمن سعودی و هدف قرار دادن فرودگاه صنعا، تلاشی عمدی برای محروم کردن هزاران بیمار و مسافر از ابتدایی‌ترین حقوق تضمین شده‌شان است.
🔹️
ما از سازمان ملل متحد، جامعه بین‌المللی و سازمان‌های بشردوستانه بین‌المللی می‌خواهیم که مسئولیت خود…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18665" target="_blank">📅 15:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18664">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به نظر می رسد زمان حمله نیروهای مورد حمایت سعودی یا امارات به حوثی ها نزدیک است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18664" target="_blank">📅 14:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18663">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :    تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18663" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18662">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :
تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18662" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18661">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18661" target="_blank">📅 13:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18660">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.   زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.  اکثر این پناهگاه‌ها…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18660" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18659">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.   زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.  اکثر این پناهگاه‌ها…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18659" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18658">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRLXI7aCS7qt3sYjRuT8HHqyc50KVJD7ahEZYWBqG9-w4MvG_5-I_J0vTS8SmCYOcFCrkt3iQ6Qs7s8WVBk3Hw4bDLJReZ31jaCJwzgRaL3SE_IXZqN85VvHsFLdrUOmt4hiK5tBEqHvpFrVgcLRBQSScADhCDu5_0uMjS8pQqn2UgcvGQyHzNhORhrWkzhjGft_kma4Qc9G8P_r20KiTCzwMeABa2yKrjwAo5SFY4QVsAkxDnxY8PycGhSwv4mPJMgKrPV9_nJCEbYyY6oYD26hdQ1jdW_B87rEbQ1bxKLvb0Ul0XCz6wtaFpqgeiJozPX_SHdrAb92a6_7SlnLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.
زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.
اکثر این پناهگاه‌ها برای اهداف روزمره مانند سالن‌های ورزشی، زمین‌های بازی، استخرهای شنا و حتی فضاهای تمرین برای گروه‌های موسیقی راک مورد استفاده قرار می‌گیرند، اما می‌توانند به سرعت به پناهگاه‌های اضطراری تبدیل شوند.
منبع: The Times</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18658" target="_blank">📅 12:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18656">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732e84f6ce.mp4?token=N4Jq6sGtpm5K1VGZAYZnKiEZSlQ3HNKfcyIDPtuv7RU1ErZxrkFjsRhU_1cqGyCLsvOzGWyTG_KnBc1m1FwXnbprcRqOPF__oW_UAeQ9EKLQ423q1-hsNl5bLqpYaCQFBwlPMZitVVJer1MRLNDSMsfpOZXajtrZ919fVnitT5TVJ-piCWBWEVKSK0pchXUxhkobmBtkHh4UJDl7QjfX4SeZqWVDG9cpH73iyqJJnEiJ4U0aQoAWzNrDqzo-HvVbr-GhDpwTwkyg-w_n0bjqiwQ-N-fIetRXJX6Ls-ehStUaiCG1j4Dr0Jg152xb-OfDJuFaoRLnr4p4xhMVuQv1-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732e84f6ce.mp4?token=N4Jq6sGtpm5K1VGZAYZnKiEZSlQ3HNKfcyIDPtuv7RU1ErZxrkFjsRhU_1cqGyCLsvOzGWyTG_KnBc1m1FwXnbprcRqOPF__oW_UAeQ9EKLQ423q1-hsNl5bLqpYaCQFBwlPMZitVVJer1MRLNDSMsfpOZXajtrZ919fVnitT5TVJ-piCWBWEVKSK0pchXUxhkobmBtkHh4UJDl7QjfX4SeZqWVDG9cpH73iyqJJnEiJ4U0aQoAWzNrDqzo-HvVbr-GhDpwTwkyg-w_n0bjqiwQ-N-fIetRXJX6Ls-ehStUaiCG1j4Dr0Jg152xb-OfDJuFaoRLnr4p4xhMVuQv1-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قاسمیان: شما نباید بگید آآآمریکاااا بی دوووووو ، باید بگید آمریکا بی دو. یعنی باید با تحقیر بگی
✍🏻
exxon
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/18656" target="_blank">📅 12:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18655">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18655" target="_blank">📅 12:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18654">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18654" target="_blank">📅 12:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18653">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5052358e.mp4?token=OqAvKQ1Q6I16DiBJKka4IaE8EkpMEOaJU9EkI8sSQt3qzCnVeFhJHFoCJ0ky6y2LzBt5_42bODU4rPl596sNTAcZpVU6sXuGq0O1TK7YcmIVh1fPC0al5ZHVEcrT9qlBOeGRMMUlKkEQUQDSrs1ZukKfiU3O1LzOMBrZiJL9Nx7hwhLfkfwDsKMlVAiQG1xTSCuvO_ljqO603Zx1GIXjT5-sWhPl7ic9MbI5hEblvKa2G-jr8YjNOvJaOnjWGlzyK72qEEHDq39VB-S13nuKJqlSURwyzHfm3g6l_Cbwb840qbbdqrl1KbBY7YiSlsLi8BlPHHZZSJoZgavCX4fEjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5052358e.mp4?token=OqAvKQ1Q6I16DiBJKka4IaE8EkpMEOaJU9EkI8sSQt3qzCnVeFhJHFoCJ0ky6y2LzBt5_42bODU4rPl596sNTAcZpVU6sXuGq0O1TK7YcmIVh1fPC0al5ZHVEcrT9qlBOeGRMMUlKkEQUQDSrs1ZukKfiU3O1LzOMBrZiJL9Nx7hwhLfkfwDsKMlVAiQG1xTSCuvO_ljqO603Zx1GIXjT5-sWhPl7ic9MbI5hEblvKa2G-jr8YjNOvJaOnjWGlzyK72qEEHDq39VB-S13nuKJqlSURwyzHfm3g6l_Cbwb840qbbdqrl1KbBY7YiSlsLi8BlPHHZZSJoZgavCX4fEjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18653" target="_blank">📅 12:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18652">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔹
حسین شریعتمداری، مدیرمسوول و نماینده ولی‌فقیه در روزنامه کیهان، در یادداشتی، بابت مرگ لیندسی گراهام، به عزراییل، گلایه کرده که چرا:   «پیشدستی کردید و قبل از ما حسابش را رسیدید... از خدا اجازه می‌گرفتید و کمی صبر می‌کردید تا این عنصر پلید را با دست خود راهی…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18652" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18651">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQEkpzKtTE8SPk5W6VgCpll9d4pV_Vp6B8U0wed5bFj9ISlfQFznkxQb1ke6jrrY0G2mij87M275svCkTifYJ912Oy3gZRd5fdQILFoEXoKeCWEzwPKTsyErpM_fCJfnMOHs_hj0vmEafSefYuMgkeN1IQHxKG6_F5acdlBG1X1zczt19zY9cf2wHuBsIESOtNmihmt7Y-mY9-2CZtsHfSyPVXfjQvTr7ATp1q_HzCNlMUUJBrGxlyjMschJ2bWNJlzuUHafcxKJbP4pJL7rCxHl6m9LXPcoSPI67mStLPeSdiFgrit1ZHG9Wswnce--xcFQ8IjiE60oicYS33Hh4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حسین شریعتمداری، مدیرمسوول و نماینده ولی‌فقیه در روزنامه کیهان، در یادداشتی، بابت مرگ لیندسی گراهام، به عزراییل، گلایه کرده که چرا:
«پیشدستی کردید و قبل از ما حسابش را رسیدید... از خدا اجازه می‌گرفتید و کمی صبر می‌کردید تا این عنصر پلید را با دست خود راهی جهنم کنیم.»</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18651" target="_blank">📅 12:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18650">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkG90YMJLjjhywQeKpnA-O0vVNyUOumwXduNloYiOUO8KGOOYBCFglTOTS1dmy7IYz06BQHPJvG1kl3jvWfp-F3ky-UnNgj63jikUpvzNLV8YDZRIDTsOhAR-EEVlMruSzAlZDyDRSGagr66s65zIgwuciRVOynD2PhC5aa409j5quatN703S8aIymtAq0EfY8u3zSl_oPQNsHPZcmh8PBzq58CkfrVzAK1xAZQHzZHEeUVe2kjBc80TH-GeBRkTChAGF_MEkjpWLlzllQ2nQg2xB7fGIMmMGjLdG60GGo_2Obunn9gBx13eFqQ5gMAwutEKcMtLNQaZiNyWJV3zXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در این لحظه کاهش اساسی یافته و کاهش تنش ها را پیش بینی می کند.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18650" target="_blank">📅 11:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18649">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سومین پرواز از سوی دولت روسیه از مسکو به سمت ایران به پرواز در حال انجام است.  هواپیماهای توپولوف ۱۳۴ معمولاً برای انتقال افراد مهم و مقامات رده‌بالا استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18649" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18648">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران در مورد فوت لیندسی گراهام:
عزرائیل عدالت را جاری می‌کند.
برای چنین فردی که میراث زندگی‌اش سرشار از کینه و حمایت از تجاوز بود، چیزی جز یک سابقه تاریک در ذهن مردم باقی نخواهد ماند.
مرگ این سناتور پرخاشگر و با دهان گزنده، قطعاً قلب هیچ فرد آزاده‌ای را آزرده نخواهد کرد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18648" target="_blank">📅 11:33 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
