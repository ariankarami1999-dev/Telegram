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
<img src="https://cdn4.telesco.pe/file/v8PzzxOhu63Ov8gWZOYVU5XEFB8I1Z4hdBsEm4_1oC0ucECtjQETqvyHUnSn_yVwAa34DdiKiE5xLQDaQVkD0w_biQgmBK4-BGx0zxBSOTfYOCN8v2-J-LyuJkdzLEmZ1ZNWBsIIpDlRZTbJitdfg-U4-n_XcFUq4EzlKYb1SAfDf-D8QJNFyCGABOtPDItlJ0r9MQNnaeNAQqrdFA-1Ok7e0ygyyPOEXfceZPvzYVSy7n-VdrhWts68XkcF_vOiweg5IWyhhzQzV6WV5Ise40vNrOTYsbwKan6TX5RYHX0AYx-y4mvnU4TMjmVTM6IboyhP_Ieer1YDDk53r-_QXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 23:42:23</div>
<hr>

<div class="tg-post" id="msg-66455">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=W-q82WBLp6Pj7Zs85aubnjIHbflDwaiYoLvUfwi9l_Sm2lYCJoMCGdA7ykMV1-zFCYXkpjTu6dOrTyolMnSrw8eM1VSFwKuYbGDlqN3f8w0M10eoPD6klefgkHefxsAU273b0lU--NXNm9pOLgDq2axFIJhd2p-WAWa8D0YFpxXSNTdXXsLhnVG48lZvMtXLId7QFP9_JarfTh3v1lPyXZKJYaWg2QcTf3inFY18tw0ArwuIfUTIdOmeQqLhmq6ZLf8NTd97eQZNDkPpz5QQzN7BfilFsqRog5U1TVpBpXGPvU6AojEw08cJk136mYmWQ3mwKyRjIAtZv4CYbcJgpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=W-q82WBLp6Pj7Zs85aubnjIHbflDwaiYoLvUfwi9l_Sm2lYCJoMCGdA7ykMV1-zFCYXkpjTu6dOrTyolMnSrw8eM1VSFwKuYbGDlqN3f8w0M10eoPD6klefgkHefxsAU273b0lU--NXNm9pOLgDq2axFIJhd2p-WAWa8D0YFpxXSNTdXXsLhnVG48lZvMtXLId7QFP9_JarfTh3v1lPyXZKJYaWg2QcTf3inFY18tw0ArwuIfUTIdOmeQqLhmq6ZLf8NTd97eQZNDkPpz5QQzN7BfilFsqRog5U1TVpBpXGPvU6AojEw08cJk136mYmWQ3mwKyRjIAtZv4CYbcJgpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آنچه من به برخی از منتقدان این توافق که شنیده‌ام می‌گویم این است که آن‌ها می‌گویند: “خب، ایران این همه منفعت به دست خواهد آورد.”
من دوباره همان چیزی را که قبلاً گفته‌ام تکرار می‌کنم و احتمالاً مجبور خواهم بود چندین بار دیگر هم تکرارش کنم: ایران دقیقاً چه منفعتی به دست می‌آورد که قبلاً نداشت؟ پاسخ این است: هیچ چیز.
آن‌ها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتارشان را تغییر دهند. اگر رفتارشان را تغییر دهند، آن چیزی است که باید از آن استقبال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/news_hut/66455" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66453">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
یسرائیل کاتز به کانال ۱۴:
ارتش اسرائیل دستورهایی دریافت کرده است تا در صورت لزوم، برای عملیات دیگری در ایران آماده شود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/66453" target="_blank">📅 22:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66452">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTVlotVuiXNnxDVvblT8Z3lNDwxnuRR8YoKA1pVLu-80osZ58mkvU8KOnXECqg_lEPTdgLqM8Hho38fyIXRYL5FubKwALcAK__IAKW3ovztCyTkeNBqEFSkxhmNJsFLHCpLX0VxlZyr7SSmTKz079_nq1VYfwIxLN37Q4i5O9KHncIbr3dvIglo0hI9PjZOUge4m48BogmZXEuVIleGoLBQBy5kJsa7Vwooqze713Sl8nssycvZuOIGsjLid7fBW7IOe6oRxvdT6pPlkpuVeCIOPx9GcwKiSkZK8zXsVLOdVrTozYb6KpM4P0lGqkqUptSXrLeMnTY5y4XrQ26abjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در تروث سوشال:
ایالات متحده به صلح متعهد است و ما همه را در منطقه خاورمیانه تشویق می‌کنیم که به تعهد خود برای پیشبرد مذاکرات ما به زیبایی پایبند باشند. بازارها از آنچه که با کاهش قیمت نفت و افزایش سهام اتفاق می‌افتد، لذت می‌برند. ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم. از توجه شما به این موضوع متشکریم!
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66452" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66451">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66451" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66450">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/66450" target="_blank">📅 21:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66449">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این پیام یعنی پایان پزشکیان و جریان اصلاح‌طلب در ایران، و آغاز حکومت نظامیان به سردستگی قالیباف #hjAly‌</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/66449" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66448">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/66448" target="_blank">📅 21:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66447">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuWa03tufeLY4c9mcM414FJCFRa0P-Kgn3BTe9xlOEYx_bt30NA_24JZOB3KbXw6UbMU4ekof065U39rhwUDvQwwiddNiz8uxL4h72rrCKt3yyqtDqE7AqhlxgQWHPfsav4qVzGEztnWhKI5UsNDaRG1963xABLdWEZVPZjgS6O8FlEpyLYwg6i-Uroc1VkXjpobFTZxZJkSMYHxfmFF8Ca9n9geQHuibSv_CBnGKTgh6bsyVW34KE7ZIGZaLvrHKyxHfheUZtKOVA_Ol6thNqxnQWcoRcXfh83Y1Augh6FrA3ksEq-H4lEiP2RfH7Y21DLKt7w5MS8LaEhulPBXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66447" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66446">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsAbBQ4B0aVXX27SRjTVZ2IacBEkz_DEFJcV5Q5MwMAN2BF7wBCJodnesaqCeuLcK8XlcBk5vS3NTahQPbLVO_cc90LJJaE0xmYo9hvWuVuHenS2qk61GNSuamGJP2RiM1gGeIwHGLNl8hI5R_1uKKDlnUYSOut8YIRF_UQSj1nhh_LzxLTsULpQQrRb3RbNf2VHGLOa4h9EuVks2iGTRWcAV1ljlyrwsC7XOz3W0U8jTZYyCU6zs_W0lvMsQBqI9BVwnT9GlDifCQA8bQD-CKSE5blbQlYiZ4yso3Y91zrcP7_i7fkNO5NSr5ezxv-IW9ecTRPJ4M8r-aGLCBTeEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: آمریکا هیچ پولی به ایران نمی‌دهد. اخبار پرداخت 300 میلیارد دلار به ایران فیک است. تمام آنچه برای آمریکا وجود دارد، موفقیت، کاهش قیمت نفت و پیروزی است. وضعیت بازار سهام را بررسی کنید. پروپاگاندای دموکرات‌ها در کار است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66446" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66445">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏
🚨
🚨
🚨
⭕️
سنتکام اعلام کرد، نیروهای آمریکایی محاصره اعمال‌شده بر تمامی ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کرده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66445" target="_blank">📅 20:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66444">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=vgUZfrqujawumOMQSSwYWr75Oi3HkTm0l4Aia4-XV2siYUH4CCDt9itwI8t76eZPuauVg6_DWAm2cpZvsJC0RDGBATaUmfzSkj_95sIlqcwpFWjPTDzv_c9gO1eJDFkVtpmG1KSr-z9nsARmA4Jvw7q6Oj3lQQb-6uvHcU24umxsS6afIIx0qLOm9xxPQMp0OD5mBlfb-KcFbzH_EMTXQflnPlD4Hu4sNVUK1C4Ti96rX8ZNnP6xPZLt3R-6uVXYP4j9cOwNKaqm9RCxwo-Ie1XEGoBjrb3jDlCvbHtum_1bpdaI7Eb-6EtUiQ33C7RR8E68Bzx-DkiwnTe813PIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=vgUZfrqujawumOMQSSwYWr75Oi3HkTm0l4Aia4-XV2siYUH4CCDt9itwI8t76eZPuauVg6_DWAm2cpZvsJC0RDGBATaUmfzSkj_95sIlqcwpFWjPTDzv_c9gO1eJDFkVtpmG1KSr-z9nsARmA4Jvw7q6Oj3lQQb-6uvHcU24umxsS6afIIx0qLOm9xxPQMp0OD5mBlfb-KcFbzH_EMTXQflnPlD4Hu4sNVUK1C4Ti96rX8ZNnP6xPZLt3R-6uVXYP4j9cOwNKaqm9RCxwo-Ie1XEGoBjrb3jDlCvbHtum_1bpdaI7Eb-6EtUiQ33C7RR8E68Bzx-DkiwnTe813PIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس در مورد اسرائیل:
در طول سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط آمریکایی‌ها ساخته شده و با پول مالیات آمریکایی‌ها هزینه شده‌اند.
مشکل اسرائیل دونالد جی ترامپ نیست و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلش رئیس جمهور ایالات متحده است، باید از خواب بیدار شود و واقعیت وضعیتی را که کشور در آن قرار دارد، ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66444" target="_blank">📅 20:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66443">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=Z4H8rXu68M8gbTyIOru6_q1y3gwzDJ7RFtfitbNo9Rzaqp4g-1USJp0UOm7DsAJxTQ9TnSFCMTZdLzG6mHRm_K9Ulac2t1ZrYlGFfqTEPte9F4b_ugdjXCHA396IQkhZv_HZ0Y_9HgfcnEsA4_xRic7wjxPw4hCLiBiPFjpPtByOyryKEhHYkEpGwug-nKNZIt5nJVRbgKt8U86Oyp013XdcIi_94XUrDkdfSgXLlW9ZKwEpq7ot5HGk6nLW9cAMPofLQSKZPMQurXxQT8iRN4aAxoMs5AO9Z45xde0k82Nu1YbzMv1adKaNp0ECpcsr8GJ0zCWuZLjV1EZbA3A8ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=Z4H8rXu68M8gbTyIOru6_q1y3gwzDJ7RFtfitbNo9Rzaqp4g-1USJp0UOm7DsAJxTQ9TnSFCMTZdLzG6mHRm_K9Ulac2t1ZrYlGFfqTEPte9F4b_ugdjXCHA396IQkhZv_HZ0Y_9HgfcnEsA4_xRic7wjxPw4hCLiBiPFjpPtByOyryKEhHYkEpGwug-nKNZIt5nJVRbgKt8U86Oyp013XdcIi_94XUrDkdfSgXLlW9ZKwEpq7ot5HGk6nLW9cAMPofLQSKZPMQurXxQT8iRN4aAxoMs5AO9Z45xde0k82Nu1YbzMv1adKaNp0ECpcsr8GJ0zCWuZLjV1EZbA3A8ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏جی دی ونس درباره ایران:
آنچه واقعاً اینجا اتفاق افتاد این بود که ما روز یکشنبه تفاهم‌نامه را امضا کردیم. این توافق‌نامه مفاد توافق‌نامه را تثبیت کرد.
چیزی که ایرانی‌ها پیش ما آمدند و گفتند این بود: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً متوجه این موضوع نشدم - می‌خواستم متن را فوراً منتشر کنیم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «مطمئناً، باشه، تا جمعه صبر می‌کنیم.»
و سپس آنچه در روزهای دوشنبه و سه‌شنبه، در حالی که رئیس جمهور در اجلاس گروه 7 بود، اتفاق افتاد این بود که شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را به انجام این کار تشویق می‌کردند.
ما قطعاً به آنها می‌گفتیم: «ما تمایل شما را برای منتشر نشدن متن تا جمعه درک می‌کنیم، اما می‌دانید، ما در یک سیستم دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق‌نامه را ببینند. ما مطمئناً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها به این نتیجه رسیدند که رئیس جمهورشان آن را امضا کند، رئیس جمهور ما آن را امضا کند، و مهمتر از آن، شعار را تکرار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/66443" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66442">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/66442" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66441">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHXak9rYBtajJSasGcvJ5iB0gaykyin-dUn1tno48YB4e26agYecv_BDoGVKOXbEzOk64aMGUOqEDYEW9KC53GCl71rxNEvwf3eNyC5TBn764aX1NfFA83KB9IaG_OplYFwioxSGhe8w3gIzCLEU8PP7XPdv_ddPi24Ndisc8WBwGaCJtnaR4GVoZ5zOwj4v8Qyl5v69EJVI_d0eDa4bJK7hlSkDvDmJNfpaMW40WWk9_M0l17wGiyBaE4TWRw212bqVogiYCIyzUqonbWSdcAD0wrYOVnwRFUAXeidcKL4DZ4Mg7Rvpe8lqRwNHgFL_db2ecgg3mBWHbXWziTJKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/66441" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66440">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=CFOBUXRcGTlLvgucGwlfIk1Uu1s32iXgbdPan4LNrhtg2xNY4fd-pNR9PLnZZHC6cR9kWA_bYXdFOoP2_cm9NHUoAT4gdFug3pKil28hs3qTd9RVSmGGQ2JUz9yqeFg3Ou0HXKROBwUjAkxiqKjlarLsMR_vfAvQB4wDsWYm7UXsDZfVrCOIW4UF1vJs858jxl2Ewocu1dXVN8Fk1HUWsXEthgI8Ek2oTi7DR8L69RdoPkdLMYLbJ2RzKMvhV3wlOgbiRP1megkTeGohX1vqkrGTtMN26b80BtlJZwQoaianysJNGjsbvprJ3HwGGGt9_5EO78jb0G9Ca4-bPc9nZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=CFOBUXRcGTlLvgucGwlfIk1Uu1s32iXgbdPan4LNrhtg2xNY4fd-pNR9PLnZZHC6cR9kWA_bYXdFOoP2_cm9NHUoAT4gdFug3pKil28hs3qTd9RVSmGGQ2JUz9yqeFg3Ou0HXKROBwUjAkxiqKjlarLsMR_vfAvQB4wDsWYm7UXsDZfVrCOIW4UF1vJs858jxl2Ewocu1dXVN8Fk1HUWsXEthgI8Ek2oTi7DR8L69RdoPkdLMYLbJ2RzKMvhV3wlOgbiRP1megkTeGohX1vqkrGTtMN26b80BtlJZwQoaianysJNGjsbvprJ3HwGGGt9_5EO78jb0G9Ca4-bPc9nZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آن‌ها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به سهم خود به تعهدمان پایبند هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/66440" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66439">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyih2pb5HXOREaTD8ppws1iqwzHPdZ1XKjxWI8hvlyhDgSiEk2Qutb56UKEQ3ppO3A62-7uYin4ckuN6TyyBrBs9XN7DWi_ZOngT50OJbnq1fgr435P4A4k9AJAFVBZHZLvZuRPNgWsWSR28bYrtldTCuZizhzuSfl3YQnoJ_Yhfxf0k3J-eO-J2fMXVmZoYlIx98KtlHF14p96pecsJnyloKQRwV9pHts0skrxOzXvX_jr1atMC8qj-pDl12GjARvu4ekIgHCjLiLHeviQ8oTNJAeJg_EbIc3kMtiukWNsNZO9G2erh7Y-xtcporgM2zWgSOXWf0J80Sz9c49Hjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
فایننشال تایمز :
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌های بلوکه‌شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66439" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66438">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9W5BJcyiMm7ew4-HP7Qjb2AiRKZrQrhBlQSV9UglTYXh9mQFp9URRUYiODNdOwTM1uqmFFLmKDf9uqFxoWZUYO1IM5lBhjbUKEFwazu96t2-ZeAh9jrGA9TJdOdwEyaAAd-W-9I_m31RLHxDS7HFldDRknjtemfSkPSBQj9i8P6QesjXd0Y2-W_jPDrQu0Pn-MYJAr0aHzdQbsc2k8LA1a2ZsNuVTh_7XDCwgAHGZKpy4dpP8TNIGGD6Pw1S3Lq8a8eaZjnlYnSGl9H4A18Q7AEcasCoaJLVSk686lbbu7_FudQGuwn5VSWi1_SJnFCgme-1QG5F_KVQe2u4GkiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ونس: کجا می روی دونالد! «امام مجتبی» منتظر توست!
دونالد: از روی امام شرم دارم ونس! شرم! توان دیدن جراحات ایشان را ندارم!
ونس: تو هر کار توانستی کردی! تصمیم امام اصلح است بر ما!
دونالد:‌ چه کنم! چه کنم ونس! با این جماعت هزار رنگ٬ که دروغ را چون «رج قالی» میبافند! امام مان تنهای تنهاست! شرم بر من ونس! شرم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66438" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66437">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=CFnnx4seYcbmN1gBcdQmuWEkzhxHbaal6TEBpi0kX4SmCA4bPIdyecCwMhDMXtlfaHLlbzbxvlxxPDTmyXgDpNc2eHsEjimP-arhqa0kjXJewhG5OIIucrnd1HYqhILaD5tyuSJu1ZTGrKNYBjKCDsZNmWeDddgMJqqwv0X9I9A4AvmsrFuI4kJkrVRCS8sCxg5Ex_ngzYuc1UO3ZQFnpJAb1SAwu5ZX9kcLVfnB7ioGhH5KCFowLHwWfuh3gIjS-2TdJ2aF75OBikKVsCsRhdFoKwDoSvKAs86xekQQpJ6PSPLKBBqfuiWYl1BNeWyfsrKktVUYStqIhZGZSUDOkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=CFnnx4seYcbmN1gBcdQmuWEkzhxHbaal6TEBpi0kX4SmCA4bPIdyecCwMhDMXtlfaHLlbzbxvlxxPDTmyXgDpNc2eHsEjimP-arhqa0kjXJewhG5OIIucrnd1HYqhILaD5tyuSJu1ZTGrKNYBjKCDsZNmWeDddgMJqqwv0X9I9A4AvmsrFuI4kJkrVRCS8sCxg5Ex_ngzYuc1UO3ZQFnpJAb1SAwu5ZX9kcLVfnB7ioGhH5KCFowLHwWfuh3gIjS-2TdJ2aF75OBikKVsCsRhdFoKwDoSvKAs86xekQQpJ6PSPLKBBqfuiWYl1BNeWyfsrKktVUYStqIhZGZSUDOkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار:یه مرد دانا سال 2020گفت ایران هیچ جنگی رو نبرده اما در هیچ مذاکره ای هم شکست نخورده
ترامپ:کی اینو گفته؟
خبرنگار:دونالد ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66437" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66436">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfZSaK00HcDi6Sw8qCbfQF5zcVJbSFRLGBqW0xjrL3H3k1CZ03_6TMl3JZKApTnWuf2OTSMNYALgp9tfvKT1bIaVcRhhYPJkozVXErUDPzEbDDeS9TohZx6hQ73GkCf7m5akv-B2TyWpYpRvW1ww65XyBk2s8qUL04MBUXWbM_Ah4DpcAEv_ztLu6RkmmL3nYJ5nPoX9DG_xTPxy2rgiGREAxl8IHaIf-XcriDXwZaNlIKHRFTgl67C2n_tCllPiiTuA2fVoYX_c0jzVDpFQ-qj-FUzM61AEGivjoPfnNwJ6PD1c9TcVbSoBgVeyIUUJJyh8NpRrIp4Agv0b-xnQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
الجزیره به نقل از تلویزیون پاکستان:
سفر برنامه ریزی شده شهباز شریف به سوییس بدون ذکر دلیل لغو شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66436" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66435">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEsdyeg1XnOYNtdV7ofQ82cY-tGJm-NaqwK3zOuzZkymiNc9lK8CCvxRkc46lBGd-0nv2X0aMQekQSmP87WIJc4FR452qMGPj-9xdZvJ7OMK4yZj7gVqKDo6Pa0NAKvt3ulDR5wGAL3QeOWUwd_uuOGR9bfqw1tkyNd5F1TpJsN72pALSkHddSPjTiNx8JQyJQaZDo09T1L5viFza0QP-MFcIwIaBWFxapvFik4IwKNleCKtRd8aVyU83TkhxmCtZMPf302578afDux7EQc5IGje-TX-Reeh1yCFpcRVJdOiqHZ6M0PpDgiweNRbNgjW6NUOOucW6tYCqKhMtEdIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
نفت جریان دارد، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (قابلیت خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. «خواهش می‌کنم!» رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66435" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66432">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGmNRpuCsFSi7AGSfZTytcknBCI-BJbe5Zr1v62AE0CQM1g-vHcZPApcHsxWNidbfOTU6OgmSdFUFGEhZ6NImoM9T695iO8i_tQkmWwQ8vhpmlgkYt48fRM2W3r16Wb5lFQxWkHeSzXjV6vPs0hqpP1ssrtTPnF1T_-48ynnUqcFGZq-TovohedG-Jso44L6bI7sTWU-JCyLU7XaYK_BkuiqSCHyvhO6kxYeUiXVr7UFvCS6fs91ykVwLnVmYIsQWFrt-Z43f76GqpWX4zoSdoFal-y-ynrPnLb21RrSFR8UrSIGYq2jDg4QIGqR1sxyT3GwC3g8cOzv4yHMjwknRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mpy5lw7UdiS3Ytv_erCydNIMwxbcc9wKVqnZnuWbyn6jtgkEKKrvETP0yz60MEa5NvkOabJNJ2Br61lvEqYg92ISUtN6xPFsRAACTgCKt0f9HwycnDC5Lmtb9BH92SqcY85iI0VogYsNFrRuZ85GcbRnQkfxU6-jRaCJOak8JezdeyUyAS8wPWjd_kOz2x0fXk_wIAjzqjK4GXCYK20AtaIZ_HCUifw33c4cVQ3TVEeI7xJOVnyVLPegVYeUtYPU0teT5qswB9Sr15O1fS06N3CZ6eMy1obOdAeZjg7KwumCntJaWgaL-kZ15dZlW04XlD7KbikMKZ8c7krxDxx-UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=NVBbkKC4xTo6btyNpJPS0PTCLP5M0F-D-JLHLrRYQ0embx9sh0y2qZCDeBKjSsP8q7bMi_CNgzygoQywXxA3L_adczDdrIL3vHRQx_9KxxMK8NffdRwCt83Tjq8I6VkDlNgbyXg_Pex2cvi7iHlAspKzlSVTZlznRyiZYx0vx1HTCI-mhYLg-w8B69K1sOmSdIwYZRd6CqB2Z8xptFD-K5UfsYdl_HO8ejp8LdQplEgY8YaN4VUZDsdZlTRVCcpR_raBSqD1JeMcG3UAa2CGv3DOauTeJfKK6plfuyhOlVYFQdBa6dXmvL8dwaDXCMSoN1u38GobHUJdFn6jRkFFXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=NVBbkKC4xTo6btyNpJPS0PTCLP5M0F-D-JLHLrRYQ0embx9sh0y2qZCDeBKjSsP8q7bMi_CNgzygoQywXxA3L_adczDdrIL3vHRQx_9KxxMK8NffdRwCt83Tjq8I6VkDlNgbyXg_Pex2cvi7iHlAspKzlSVTZlznRyiZYx0vx1HTCI-mhYLg-w8B69K1sOmSdIwYZRd6CqB2Z8xptFD-K5UfsYdl_HO8ejp8LdQplEgY8YaN4VUZDsdZlTRVCcpR_raBSqD1JeMcG3UAa2CGv3DOauTeJfKK6plfuyhOlVYFQdBa6dXmvL8dwaDXCMSoN1u38GobHUJdFn6jRkFFXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پختو پز اوکراین در مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66432" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66431">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=oNMju5buMQMTMSKbgm6sL3W6wh9YFxsORI4OdWCh-kevc1cyWC4ahfelc2fA0bU1ySyS7QSMVEd9LYNVhmY4GT-uHyv6gSNmR7WVTZwirPGj_NchoPKUAQ-T3Aj6mY3eQ71DqbRY5Y6sIcQ8_CArWyUlwpbd030CuQULRj6GrTO9eEHK0sNvx1mu2VoE1xTz8JNXXIUql5J9-tiPJVZt5d2Vn0JE6T34NDinIiMQgYXkVr9cdif9XFPY6Re7ixtnqamDSg-TMWTS0-96UNap8Dnhvk9xmGmyViqypFfWe_wWGdLE8r1ei2PwEdnn9HOwg5_85ZBFfLGVhDNf_kIvPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=oNMju5buMQMTMSKbgm6sL3W6wh9YFxsORI4OdWCh-kevc1cyWC4ahfelc2fA0bU1ySyS7QSMVEd9LYNVhmY4GT-uHyv6gSNmR7WVTZwirPGj_NchoPKUAQ-T3Aj6mY3eQ71DqbRY5Y6sIcQ8_CArWyUlwpbd030CuQULRj6GrTO9eEHK0sNvx1mu2VoE1xTz8JNXXIUql5J9-tiPJVZt5d2Vn0JE6T34NDinIiMQgYXkVr9cdif9XFPY6Re7ixtnqamDSg-TMWTS0-96UNap8Dnhvk9xmGmyViqypFfWe_wWGdLE8r1ei2PwEdnn9HOwg5_85ZBFfLGVhDNf_kIvPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد کشتی ها در تنگه هرمز پس از امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66431" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66430">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5FvI0wzOJhuQKGSUnCqAFq5vFpx3jaQl-26yJhnXWjMwE8V4MgJ2w6oM_YeJHOUOWvXbOSVGHcVXgfQVkgteUls4f7n1FMC_2UeIMPwN2m2fkTaqyBm8KhJnX3SaBgVgYG3qeJWELWjLGwlmt8B-3inyczSeQdEUbQ7wL8PzHKE6oHYdE4x7-pyoS6kyGI13kuErZhIyY1ZecY0rmAvBKa9rWYQgs3zsU8SjIqjRMjaaqheYJMxFMsMtAH-WeBdE4E9aYQrw4-RF9Ft5fgwKXItu0ymfnfSNRt35vi2vcwTgqjrzQIYerxMG842rRybN4pyHVcWJRVyVg-KbtXTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارتش اسرائیل؛منطقه امنیتی فوری در جنوب لبنان:
نقشه منطقه‌ای که نیروهای دفاعی اسرائیل در جنوب لبنان در آن فعالیت می‌کنند
بر اساس نیازهای عملیاتی، نیروهای دفاعی اسرائیل در منطقه امنیتی واقع در حدود 10 کیلومتری داخل خاک لبنان مستقر شده‌اند.
نیروهای ارتش اسرائیل در منطقه عملیاتی جنوب لبنان مستقر شده‌اند و به تلاش برای از بین بردن تهدیدها و بهبود دفاع از جمعیت شمالی ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66430" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66429">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFVqkl8z05T499PPFoUxn66E7q3j1V1iVJ4X5s0ScXiOuTNZVzf7N6HnaKpDYM8FoFkzX6tY2GZQ0ulCy5uVj8UiCljVlVUbCpoPuppzmR9eZlLpBaPhhup9mzO8JfYPLAubUiZm4wnta8u4kColZ4JaQvhp2oiQP9zN--vNa6GBSYdl3gLUfXybjrypZXVNfbV39duUjmaEcO8LAyNQuESeLEw-MEvYe0i3lEnibzsR3NWaFy4S32LBBFznO1GUITw3dRWq3D68irare2FpjeEFfYoMs9lkadACemC_lzmKzehJPmh57V1jgGWc8LFz8w3yOwcKdDeUEoRfg72apg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان؛این یک سند تاریخی و پیامی از ایران مقتدر است:
صلح در سایه احترام متقابل تحقق خواهد یافت.
جمهوری اسلامی ایران به صلح جهانی با حفظ عزت و استقلال، پیشرفت و همکاری منطقه‌ای همواره متعهد و پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66429" target="_blank">📅 16:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66428">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622db6728d.mp4?token=BX57iP5zl4mm5_zYwYS5NG2u7wGz1cJvIJIZazwqhqOKLve3a3DBkP4aF00ddZtGajTzTtmWvCBNRi0-1wxGgs7KF0B_ET_Z7vfc5dMNfw0rxEsUyA5osoQ2dFa-EBamAfX3fSXSRrCGXPYlGWnhZRSY7VZOwl6ztxnUVS5fTEKp11f-w4M5wqZEY0pkJDATRC1ef62k2AK-WnSRlXgmEdD3rYocdL5UH_GtRW4FOBGbdb2W02JwqNEAKj2tsDvqgoN4rOqSmPdHD2V1MC_WI4N7YYJXBNwvHf1q65-G4gtIUv9XJtXUbVEvKX5kJhTxp4W3CYxsxh0M6gpT0o6xeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622db6728d.mp4?token=BX57iP5zl4mm5_zYwYS5NG2u7wGz1cJvIJIZazwqhqOKLve3a3DBkP4aF00ddZtGajTzTtmWvCBNRi0-1wxGgs7KF0B_ET_Z7vfc5dMNfw0rxEsUyA5osoQ2dFa-EBamAfX3fSXSRrCGXPYlGWnhZRSY7VZOwl6ztxnUVS5fTEKp11f-w4M5wqZEY0pkJDATRC1ef62k2AK-WnSRlXgmEdD3rYocdL5UH_GtRW4FOBGbdb2W02JwqNEAKj2tsDvqgoN4rOqSmPdHD2V1MC_WI4N7YYJXBNwvHf1q65-G4gtIUv9XJtXUbVEvKX5kJhTxp4W3CYxsxh0M6gpT0o6xeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعد سه ماه هرشب توی خیابون موندن و پرچم تکون دادن ، بهت میگن اقلیتی تندرو و خون رهبرتم پایمال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66428" target="_blank">📅 15:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=RUrMovVSVcBedZI15fUEXwxatThPfWA8EVrRJNCf6Vjnw6qzdRGZOd5vDe8rvyYotoVEmfnwglK11O0Hq975JnoBiu3PPlCDF3Y-saHDrfWvbhJmOh8oM6lsICDSlntbiWfASyCe85z8XUUBQuOc6YJdIdc4jsn62vWnSj4372QYB9spxE4f2PHhy06LzZUStZTIheYC6MtK63TZswMIh9UjN3zPY3laga_brmguNSKFrZv4hIFxAfFfYx9qA3m6X0cSj-yLaE6Roz6-o7L71N-3bxFi140ekSCN-dPIiz2XCN0b2AouIqZATEuzMnafWQSE0tPJsXjV73TXdMgU3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=RUrMovVSVcBedZI15fUEXwxatThPfWA8EVrRJNCf6Vjnw6qzdRGZOd5vDe8rvyYotoVEmfnwglK11O0Hq975JnoBiu3PPlCDF3Y-saHDrfWvbhJmOh8oM6lsICDSlntbiWfASyCe85z8XUUBQuOc6YJdIdc4jsn62vWnSj4372QYB9spxE4f2PHhy06LzZUStZTIheYC6MtK63TZswMIh9UjN3zPY3laga_brmguNSKFrZv4hIFxAfFfYx9qA3m6X0cSj-yLaE6Roz6-o7L71N-3bxFi140ekSCN-dPIiz2XCN0b2AouIqZATEuzMnafWQSE0tPJsXjV73TXdMgU3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین اوکراین به مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66425" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=LZRhqapoBpO0lj18NT0U6MfYkrqKrjYU2jb02p-TovriJKj68yCUEOnY254EwN_YL70hODO9L7TNRTub_bgup7u4gM4h6VHAm1MQq-p-nBmTEwualheiXJxfjSEkFwOpkg6q9jBqt_Ak_ZBnNuLrYKoDdQZdh1kYHXcnnwBfxOvg5Q76jmP4eaudlPx7rra7RHYX8GdOgiqN9YriwhCiXXWhDVa7zCAG_e1XU-nOpra_eFEIUYW_DtJp284EkEMu9Pc6Rb2UkS0U3b5m0bE24VmN8D_Mx2NZiGbNx_p0zGc_d9rHuUDGVWFDMde4p7sG7Du-mCprzS7UezUZXfAc6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=LZRhqapoBpO0lj18NT0U6MfYkrqKrjYU2jb02p-TovriJKj68yCUEOnY254EwN_YL70hODO9L7TNRTub_bgup7u4gM4h6VHAm1MQq-p-nBmTEwualheiXJxfjSEkFwOpkg6q9jBqt_Ak_ZBnNuLrYKoDdQZdh1kYHXcnnwBfxOvg5Q76jmP4eaudlPx7rra7RHYX8GdOgiqN9YriwhCiXXWhDVa7zCAG_e1XU-nOpra_eFEIUYW_DtJp284EkEMu9Pc6Rb2UkS0U3b5m0bE24VmN8D_Mx2NZiGbNx_p0zGc_d9rHuUDGVWFDMde4p7sG7Du-mCprzS7UezUZXfAc6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏جی دی ونس در مورد مسلح کردن معترضان ایرانی:
در واقع تا حدودی دشوار است. می‌دانید، نمی‌توانید همین‌طوری از آسمان سلاح پرتاب کنید. واقعاً زیرساخت لازم برای رساندن سلاح به قلب مردم ایران وجود ندارد.
یکی از چیزهایی که رئیس جمهور خیلی نگرانش بود، همه این معترضان بی‌گناهی بودند که توسط افرادی که چند ماه پیش مسئول بودند، قتل عام می‌شدند.
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم متفاوت رفتار می‌کنند؟ مطمئناً امیدواریم که اینطور باشد.
و اگر اینطور نباشد، می‌توانیم وقتی رفتار واقعی آنها را ببینیم، بفهمیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66424" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66423">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPCbnso7tBMy1g3d3VMaUckQgyA7RZlfu4t0vUwxsCO5enagG-Pzeo70Z6qpp6GbaA7K6lyTOcf0FwVBsLIwe0LyHgCqIpu4CEwzhWu_SOBAuWI9KtvjudHPaxMn5Lk7w2pP1SUs-8IQlOGav_O3Vew5s1i9yWLFbg1EY2T5lxEEHVs3RjecJLWIjG_IXkhKo7zdFXgGbsDqXoCcbrh4U3D6f0TIDIjASwkRRQUARIlCFCTtwagidd_FxQEhXREg6hUcpdDDh6KdlaD4wSy54_9kRaxfIJ-6Uwfvaa5-1MM8pFE_fA4XG8lX84n7l9YB4JgzO9vZ1PLznpfHIL2Jdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حملات اسرائیل به جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66423" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66422">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66422" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66422" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66421">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrXcU7EROSpR4qcWdNjyT-DqSvwjxv6XMXYQ8xUn2JaCO8YA_UtjLUkc3ZzirqTGGLEW898zsLOlWVpHjWRF-VBD-uvYY-rSTf2I4xtyAq3whZeDgD9v3DO7gl69o3b-eB3BfncGt7li4MbcPtE_QbfQQXWe1c0HP-aXkqE6Y8-Ntt0I3lwncPLC_JpNd05b7E-ohXS6klPw8bEjWdfxeFWTkcmkNp6jtmLtObXoAulRUZiRRQLAb72BzHMIEYzkf3qEcefTUBIIZrokQlqMQmrJ2PwR2DqIPABeru25YJ-cK_o4IJDHIIpREEEWlF-Z80tqUM0krVIFjatkeCwG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66421" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66420">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m40yol_8M8m96IRGvysFeJdDRcQp7GAxoi3D1HTKZpJlSxqvhdYy_jkzwvDxKIXINGEXjLJbmjQaDnL15NHctMO3zDbmLAcKet5tKmZAX54IYM0qvxbTVkYks9Zj8lYJ2tfkSYCdVufvK3G7vjkpNPF5Sx59tgiG1bZJNy8C6rwPeCTdt2DU4hXLpAEXH1gqDe40NHNmXwL_vylJ09AkdN7-k7PqX_b4K9Hz8D5QBfPT1-1Lq_hqsEJWEFOvscGpEP9AZwQB613nAzDtUs9IQ117HRI1hGZDSK0sG7ZCEkTet3C_a1EB8fhastO-vKNXy1dDXWV6-3Se9HDtrQlG5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66420" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66419">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=t3bCFZ_lAESiCacAMAXxggjGZ6bXGe3AJ_u0OO6EfBCIf9is7Sg_qxAjTTBPv4bdf__X6WUYHOYmXeTQIWKh5pN9mTGkJFRd7j0enhGf66ZUZmnne2z8TyuXtGxWbo_YcM3cNcoEdETMCGJ5HzpZEyPJtDUiTU6xQH6l0_ZYkm4p5VZQRXWdECvMbj9zWjQG-ePZa92GRhjDMvYlF9Yx2zm588YqcHSeU4ovMoBhDkyErUK3EMOr4_COR-xkt2lqF53_mgCLjbySEkmfF6zGY5EY6PfYu2zyI16SOKfoUuu_E4s1-Jp5OzuUFxtParaU-rF7DRqrCwvC5Pv24kJXig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=t3bCFZ_lAESiCacAMAXxggjGZ6bXGe3AJ_u0OO6EfBCIf9is7Sg_qxAjTTBPv4bdf__X6WUYHOYmXeTQIWKh5pN9mTGkJFRd7j0enhGf66ZUZmnne2z8TyuXtGxWbo_YcM3cNcoEdETMCGJ5HzpZEyPJtDUiTU6xQH6l0_ZYkm4p5VZQRXWdECvMbj9zWjQG-ePZa92GRhjDMvYlF9Yx2zm588YqcHSeU4ovMoBhDkyErUK3EMOr4_COR-xkt2lqF53_mgCLjbySEkmfF6zGY5EY6PfYu2zyI16SOKfoUuu_E4s1-Jp5OzuUFxtParaU-rF7DRqrCwvC5Pv24kJXig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه امضای تفاهم‌نامه توسط شهباز شریف نخست وزیر پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66419" target="_blank">📅 13:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66418">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=nL8X6aF8jiWoXpIkM1dQQ-HtrpE2l5X38QQKEY6aYI_a3dGvRomtlqGYViCKMF1gVCrOnlVZrubALmpDcpMXq1-OU05DHwfYH0QmTi6WP_zo5qWA0Iozig6XSloHVKbodukgMRKWRtxu6i__NSAhwzHT0juG5AXp5Rb3CcGw2nbeV6akRWcAI7YrQ8zyIjWAFRLP_PLfHv-XxdEHdiidYto-KDPo9GWwIC20sfNXOUSkknScTkppXiQBxLLKqNDWiP3ex6tkKhg1EBjv6Odyz4YgX_7QCiv_oOxCT3mNTxUJNlBTozXFX1TNaiRR0F4_eZZfOCH6LKC_ndSZcODHYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=nL8X6aF8jiWoXpIkM1dQQ-HtrpE2l5X38QQKEY6aYI_a3dGvRomtlqGYViCKMF1gVCrOnlVZrubALmpDcpMXq1-OU05DHwfYH0QmTi6WP_zo5qWA0Iozig6XSloHVKbodukgMRKWRtxu6i__NSAhwzHT0juG5AXp5Rb3CcGw2nbeV6akRWcAI7YrQ8zyIjWAFRLP_PLfHv-XxdEHdiidYto-KDPo9GWwIC20sfNXOUSkknScTkppXiQBxLLKqNDWiP3ex6tkKhg1EBjv6Odyz4YgX_7QCiv_oOxCT3mNTxUJNlBTozXFX1TNaiRR0F4_eZZfOCH6LKC_ndSZcODHYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیرزن کسخل مکرون دیروز موقع عکس یادگاری سران گروه 7 نزدیک بود زمین بخوره و شانس آورد ترامپ بغل دستش بود گرفتش
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66418" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66417">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قطار پیشرفت آموزش و پرورش کشور خدایا شکرت   @sammfoott</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66417" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66416">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxx9LwOGvtf_DVh7Biknj7AEP6JEo-nYH5XKt_k1y0RpeKUjiYjyjd9BYmozJcEk__f5Mf2fAeS4lX7jjeYIphcnBmM-clOAQZzanirKFrqq4PJN4NxSEkr0wvS6xvVibBLonrrLrr-KHWVL-1D_QbuCBGtwcpX9OaIGX_CJ7kFmqZK-f8-NGVd81KZSrBNw_DAOSKQunPpq4VR31gGGuE1OEjbIc9JSLJ-8TNQ6KEb8wtKD0J-4sIZGDaGUmO2V0iSmBxiS-EA30VTXPV3LPwbuFtUoYuHCTqONYrwbcXAurndJQgkbgmYHzvDW9rtAmz-4KGV0qGuNnJggJ6DfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«این احمق‌هایی که فکر می‌کنند من با ایران به اندازه کافی قاطع نبودم، در حالی که بازار سهام به تازگی به سطح بی‌سابقه‌ای رسیده و قیمت نفت در حال «سقوط» است، یا حسودند، یا آدم‌های بدی هستند، یا احمق. بیایید دوباره آمریکا را بزرگ کنیم!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66416" target="_blank">📅 12:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66415">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=abUMji8xkTVZp6HpGovpNhTyJi8i-d50X_w9x5D220vDmmVRT98zTF6yfa_M2V8D8epoPJXUqSHfP9tOLt-Em71_91UvDKwHePREDSAEla0T5ZW-RGPz7flvQExlXmMcb0OZFhKpVoIw0_4tN1pNMkj5tyXRD-2iSk5bI65ePOyH7d-rKdzigZYG989mDO6E0pLk3jL7n0IwrMF2oUJGOvDH9-yMigEaWhxkv7_3IBYQUpecho9MENj2bL9QWrv3CRXLfJMl03Q7gYTSGdYfEfXmJ0PpTdOrU3oh7qn2EL1SED70bHA9BJBGLzaMwb6c8T20TmpO4CbQiXJu7Kxi-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=abUMji8xkTVZp6HpGovpNhTyJi8i-d50X_w9x5D220vDmmVRT98zTF6yfa_M2V8D8epoPJXUqSHfP9tOLt-Em71_91UvDKwHePREDSAEla0T5ZW-RGPz7flvQExlXmMcb0OZFhKpVoIw0_4tN1pNMkj5tyXRD-2iSk5bI65ePOyH7d-rKdzigZYG989mDO6E0pLk3jL7n0IwrMF2oUJGOvDH9-yMigEaWhxkv7_3IBYQUpecho9MENj2bL9QWrv3CRXLfJMl03Q7gYTSGdYfEfXmJ0PpTdOrU3oh7qn2EL1SED70bHA9BJBGLzaMwb6c8T20TmpO4CbQiXJu7Kxi-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجاش که یه موز و دوتا پرتقال بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66415" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66414">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=WL4o1TUQgMm1Vxvb008Pl_Ym7ixHEnXCXtxBII54PJAPRcFpGlp_1i2vH3lW4xZePkrIa5HDqRQlDCdiQdRgYYeHvm_8TkWF7IGltvo3D31p2a56aWkBrVbU5a4F0zSTS3AGarKFznqfV3JzQqVX95FHWtkzjdgVEfpfyF9m_YQEM_7cgeUwMnz2n7rh8vP8DGGakCuZgzaY5LXWNywVzeYnjHZGEud_JhrCoyVAuXwr5RNiyh3WoQ0IpZ5qRLS_YzkokNmuU3Gjy8ZZQ7RXKDZ1_IVSk-paGaBsfxDc4XNAd1ATWl6A5WKD5VUzgB-0vi1LuGGu0zB4XqFbOum7cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=WL4o1TUQgMm1Vxvb008Pl_Ym7ixHEnXCXtxBII54PJAPRcFpGlp_1i2vH3lW4xZePkrIa5HDqRQlDCdiQdRgYYeHvm_8TkWF7IGltvo3D31p2a56aWkBrVbU5a4F0zSTS3AGarKFznqfV3JzQqVX95FHWtkzjdgVEfpfyF9m_YQEM_7cgeUwMnz2n7rh8vP8DGGakCuZgzaY5LXWNywVzeYnjHZGEud_JhrCoyVAuXwr5RNiyh3WoQ0IpZ5qRLS_YzkokNmuU3Gjy8ZZQ7RXKDZ1_IVSk-paGaBsfxDc4XNAd1ATWl6A5WKD5VUzgB-0vi1LuGGu0zB4XqFbOum7cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
با همچین عزیزانی تو ممکلت هموطنیم :(
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66414" target="_blank">📅 11:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66413">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=u6OudX7uN6qBWnkpfjcViYPoUjYndw9lwzlrojAuka-1w2zi6kKCs4WV_AwOLS5VRJteS-l-Sh4XEA73NLaxwV9HLW_KBdnkT1o5n7gNxji8oysbnx9pR0Yg_ZrmA_ZaKmcUwwpldwaK3VSS0nZWvKr4Xhjm_wh06zqcrSMkY1gSyrVWIVFrk9fvh1rq49Keha2MpOipD_mCxgJNJfBoKvh_tuI6gT4va3T8_EJknmRdd53xUAI0DgimwwbdtZ1PIMoaXRMIODs0Gxik5UQPywfPXNBxjNzd6r6MkFuSLFHFCvhwUH7mhkal3mnKXSI-oS9ISaTZKzxozzQrNmAg7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=u6OudX7uN6qBWnkpfjcViYPoUjYndw9lwzlrojAuka-1w2zi6kKCs4WV_AwOLS5VRJteS-l-Sh4XEA73NLaxwV9HLW_KBdnkT1o5n7gNxji8oysbnx9pR0Yg_ZrmA_ZaKmcUwwpldwaK3VSS0nZWvKr4Xhjm_wh06zqcrSMkY1gSyrVWIVFrk9fvh1rq49Keha2MpOipD_mCxgJNJfBoKvh_tuI6gT4va3T8_EJknmRdd53xUAI0DgimwwbdtZ1PIMoaXRMIODs0Gxik5UQPywfPXNBxjNzd6r6MkFuSLFHFCvhwUH7mhkal3mnKXSI-oS9ISaTZKzxozzQrNmAg7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
برشی از سخنان تند شب‌گذشته قالیباف خطاب به ارزشی‌ها و تندروهای کسمغز
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66413" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66412">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=YUkE49vrMuWdad2QSsEcQ7t4ceQOQfFcSRlCfJ00Y_CV9Ycf5peV78Q1p_-i6RYASTBMzGR8291sFDRkBABDWkL8KK_RTapoYGTsYBNjLplLFg83mtg3Me1_8WhGdjctvNmhzjUsf6cKQZqNBzG8rLWsKrcZgfkTmVEjW7Gy1C1JvgZWLfYqehgmwng7bUM2GBJ8OVgyzAFQro_KvKAkFgbNOanIZ2xBAiWEwXYdRrxqRBR_eXi2-ojkId9VctAoJW1gkkuBgv8qjEJuBFKTJ7SVL2npWWGHScEd3UEVEVkwv8CN-xNqkTfu9Tv-mbTyOFMDqUdHpQ9o0eyqe9MTIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=YUkE49vrMuWdad2QSsEcQ7t4ceQOQfFcSRlCfJ00Y_CV9Ycf5peV78Q1p_-i6RYASTBMzGR8291sFDRkBABDWkL8KK_RTapoYGTsYBNjLplLFg83mtg3Me1_8WhGdjctvNmhzjUsf6cKQZqNBzG8rLWsKrcZgfkTmVEjW7Gy1C1JvgZWLfYqehgmwng7bUM2GBJ8OVgyzAFQro_KvKAkFgbNOanIZ2xBAiWEwXYdRrxqRBR_eXi2-ojkId9VctAoJW1gkkuBgv8qjEJuBFKTJ7SVL2npWWGHScEd3UEVEVkwv8CN-xNqkTfu9Tv-mbTyOFMDqUdHpQ9o0eyqe9MTIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66412" target="_blank">📅 10:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66411">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=UMlx1if8hnNKjwBBbal7y7LOFfbB13JvlHCO7eMc8jajb-pqI06fAbhNraqgf0HkX-b5yaYBO63LfyG5NN0Pc7mbhSnVxFOWV8--hJpk_iUnkaRZunAILDp4VCpNR9a2ipHhkXb5NBvH6ZEWRLRSfmIWndV6ApdgnLJ1CLPuklUyoBLX7RV3sC61SElXGP_eTKZ5LN5Qz3i7LhHO0-giAjnZ6mE4eDm_tvC3oSOcvkU1SbE2DeHVtypvUHyktjLGHPVx0cnMxCe-fFv928_czrAzVyTJJ1Z1hjqsReJ5ya_EpfWyV7_0n8xKf_KlfAuI34SllWHirV_s6fpWsXc-wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=UMlx1if8hnNKjwBBbal7y7LOFfbB13JvlHCO7eMc8jajb-pqI06fAbhNraqgf0HkX-b5yaYBO63LfyG5NN0Pc7mbhSnVxFOWV8--hJpk_iUnkaRZunAILDp4VCpNR9a2ipHhkXb5NBvH6ZEWRLRSfmIWndV6ApdgnLJ1CLPuklUyoBLX7RV3sC61SElXGP_eTKZ5LN5Qz3i7LhHO0-giAjnZ6mE4eDm_tvC3oSOcvkU1SbE2DeHVtypvUHyktjLGHPVx0cnMxCe-fFv928_czrAzVyTJJ1Z1hjqsReJ5ya_EpfWyV7_0n8xKf_KlfAuI34SllWHirV_s6fpWsXc-wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب دو سال قبل شاهین نجفی درباره قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66411" target="_blank">📅 10:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66410">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=gtThSQhoL53jc3bJM1Eyhgl5aFvEnxLQX5fWe-4V3Dsu7sy20QWyd_x45h5A1t7m5CBIWYr_jRY884ZgS5tWP7WA9HRQUTYR-cJFS2OpWNgLk5Ch-dZyd-eL7BDaT8XTSFUT4puxMzlY6c_WCDfh_ppt2iQK_wNe3ZiY0Hbx0xtZ6TWqoziVNUoUa9lGXyZJ9lTYTY0Cmdw0Bo0r1ttlcocPpX53fmOaP8fYLy5tN-MtOV50o9grT5FaqOJmjNhRHqXyvMoX9NiVp484cPdzmzMwtrt7f3398hZWjc7PlIZGWUwtf813qeKOR4kHQumLDpCrP5XMTANiUeXEpQUthw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=gtThSQhoL53jc3bJM1Eyhgl5aFvEnxLQX5fWe-4V3Dsu7sy20QWyd_x45h5A1t7m5CBIWYr_jRY884ZgS5tWP7WA9HRQUTYR-cJFS2OpWNgLk5Ch-dZyd-eL7BDaT8XTSFUT4puxMzlY6c_WCDfh_ppt2iQK_wNe3ZiY0Hbx0xtZ6TWqoziVNUoUa9lGXyZJ9lTYTY0Cmdw0Bo0r1ttlcocPpX53fmOaP8fYLy5tN-MtOV50o9grT5FaqOJmjNhRHqXyvMoX9NiVp484cPdzmzMwtrt7f3398hZWjc7PlIZGWUwtf813qeKOR4kHQumLDpCrP5XMTANiUeXEpQUthw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
10ثانیه تراپی روح و روان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66410" target="_blank">📅 09:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66409">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=Kjk_fjDTDlgYXETSpBw5pE1J7hHXw9wWls5sFwrIV0TaWP04tkkKHiDnzVFU8kF1KxrixzxgwXdjexjlnAjN8j2Rb4UxqR7arkm4oOhFlYzigU2YhGcnOZUg9LdhgfGo7yZJUmjJJTzWbrMtA-tvhrp8PFAJIr2irNjr2SDjQKP5c9E-Ef5DmzbuBh1FogFSTr4VLxnZVRT7RKm3d_b1z2wjJ2nuzuBs4J5RNLbVZbQ_TwcUs_JkuA8kpD1eBI2VNiqla_OKiJw2kwTQ3zQQ8zB0tHg55mkXRmfZOVJTcq5Np7Q9uLo2DLeaPZuLeymOPbJ6GEwoA3LdwUURxVfmmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=Kjk_fjDTDlgYXETSpBw5pE1J7hHXw9wWls5sFwrIV0TaWP04tkkKHiDnzVFU8kF1KxrixzxgwXdjexjlnAjN8j2Rb4UxqR7arkm4oOhFlYzigU2YhGcnOZUg9LdhgfGo7yZJUmjJJTzWbrMtA-tvhrp8PFAJIr2irNjr2SDjQKP5c9E-Ef5DmzbuBh1FogFSTr4VLxnZVRT7RKm3d_b1z2wjJ2nuzuBs4J5RNLbVZbQ_TwcUs_JkuA8kpD1eBI2VNiqla_OKiJw2kwTQ3zQQ8zB0tHg55mkXRmfZOVJTcq5Np7Q9uLo2DLeaPZuLeymOPbJ6GEwoA3LdwUURxVfmmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چه مدت نیروهای نظامی آمریکا را در خلیج فارس نگه می‌دارید؟
ترامپ: هنوز به آن فکر نکرده‌ایم. احتمالاً برای مدتی، جای خوبی برای ماندن است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66409" target="_blank">📅 09:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66405">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VI2Yaq_BKLHQX_aeNMuKgsI_vUbvBGPtfpffoiOyKp1InQCI95vCJnb_JMtr8wdXBPJ0ce4_P-BTAD7Zx6kFGchlV0RlUH2CKjD-H7dSNpsqWVgXmDK3dx85LmyT9eKqLrRkB1TDbpmMfVAX7Owmw2Ps97wLWyrGGMy4ZD242ksX7Kc_TLAsmYHsw2OgOb_FtW5VWIwjuJL6_3PP-vZcc8a_MnNaOylvWcg2eHxWNip8qQNv6NXWoz4cBXEvgqyAdTE5jt0j_GkL751RwBq0H2skgohYEuSZ9f0bF9jmxFAvf4Etbpm2KgHEFCarboBMfaLvFILHBUfjQ01mhZRYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gOJEwnVN03Kc2l9bgdjRAy0TCoo-sNpqMO6uL-sAe3ed8sX0G3b5eHZWm_cZPY3gdUDDP6oFsolmDcZGx0-p8KD026bOD66Dt43j0FxGE-Z79t8ZLnoBmjFz2kLtr3Z4VhI-hb2YtkuEpJ4RV74lYSjSQIWrjFzlluHPCDHzigcNn5a9_Q85oIjQPo7NlHtaC45w9nUIfJI1RSpzI18L8HzIRFKf1hZ2r2mnm-g2xbf0WqsZuOTzs7OUQRm_p5zQqJWXINLCToDuo9ZkonBxb_NExuyvgU9mb9zlOR6lwcqOiN6XLjsURceTvOJdh2GP1DRTuAPWlRs-I1w2T8cfpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rv-B6odaf6X1h4SGpWEnlexRD4n62kBr528XgX1i4NtKhM-rVl1ZLATTzIfvvCv_apVHWCixYpJ29KqOFC6JMn3bDcRhJI2L_mu6C3XGtdgPFbIHoX9uNAs1utvY72JCLJ8N317ojbmG4u6cQ6HQB0DkigAIlXdb0LXfLNpLo8NzGubq2JHxDdUIK9LytDzWFkXmdSWM4eogczhnvuYLEOEtCkuOX-fi-YV4QViHSXhLNY9e2HWNeenXcWcPX0kYhCNkN-gWLvyApYevA-UU16b_aQj5t55eEfi2lMOWHgGJvO5PAKZbrjqZNLOVG-vM710QIX-JE9vBBrg1Nht2Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد  @News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/66405" target="_blank">📅 04:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66403">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrWn8zDtdE8qQ0NfpgE1P69GHyu_mcXSunXJD8IpBM_nFSISN2oe7hisLi6bfOEBNZCRggk60VHId_6UHsKyzvpTtWXQXTqR6N31SVD8MdWaSlr8zDZyWwjD3rO4sWriCuJEc6o_VJnA3sL1mMnrAO1EvoCfPf8aMl5lPtn1EFixZ0mNZJNV1p_zi9z434TlqfjEpUiiaLDb4_83LxiM8UP5PlOaodOroAx-uGk8fwdKtmj-DzkvDPdAzOfgRTMval1Bq8PcWMah2afy5su7wceFmIdT9v_gWQV3orT7qf938yAmDKFasO5AruN4cW0g-5yqtC0_qylR_t5drR6X8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=uTUupm4j1oWd08iMwZlYFBvLj7cu8JQfoP3hxy8ck4Xv1cf16lMFpR4Ro8tLw-2kR2_ncywaOZbfavrj0MMA2nA6k9jI_3_5VLFlnFmWNhNaml6F31_ZbM2UoDcM5Zylv86273BzTHfjEAO_PwxVLFB-S_NtNsWhCA38CHtA-y4qGDOb3tNg-CaS6L2cikfWLJVxztrAPaqUxJgM2kJ52C9_W0Ea7WAsWN_x2-xv6AYz-Ch6uSGB0Q2tsOhK4T8I-0d6e9Ymry_GN9CsZJSFLfjP70faYQ9KZyR3G741TL1BXNuPYZNeFYK8VqKfoVrkXnQabUUa0vS4cnuhGqLWRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=uTUupm4j1oWd08iMwZlYFBvLj7cu8JQfoP3hxy8ck4Xv1cf16lMFpR4Ro8tLw-2kR2_ncywaOZbfavrj0MMA2nA6k9jI_3_5VLFlnFmWNhNaml6F31_ZbM2UoDcM5Zylv86273BzTHfjEAO_PwxVLFB-S_NtNsWhCA38CHtA-y4qGDOb3tNg-CaS6L2cikfWLJVxztrAPaqUxJgM2kJ52C9_W0Ea7WAsWN_x2-xv6AYz-Ch6uSGB0Q2tsOhK4T8I-0d6e9Ymry_GN9CsZJSFLfjP70faYQ9KZyR3G741TL1BXNuPYZNeFYK8VqKfoVrkXnQabUUa0vS4cnuhGqLWRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری
؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66403" target="_blank">📅 04:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66402">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66402" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66401">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NVfxrJNwF_057B7sBeVYhmein7txDy2B2MQ4cGoFYscJP74NwIjdpWaQk46W9NaID6QG80bYTEsGfhxYYRnOrFsQUKP__ochWhx8nCkn-mry6chYCtY0hpPTifPQVXiVqdEsNVeo38vjahCjbhNw8J3i_HFLtVyVlyIfS4IgnCek37DHLLLTgrnj50CwXPzzAQapEkH-pBt_H3EU19bAoDq8lFXSXIlMBt9QHzDsrFNLLxOHfxs-VT0ATny24YhdWUcnBMCc0FAqTsKHnSAHKCoWG1IOy5jw2tZg_Cwi5T0F97LJe3ZZVuqu9f19sOYDUsL6B9DUK8a0ozvC40Nf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66401" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66400">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KrSBescnTXYHjHi-l0MWdlVKTntlWtjJxISpZqI915MVSawpkyRBZhWHY4U1h8KNDP8thAQ3IDtGFwZOA8OBP8jw-750-w5VfbEAhh96SHaMQ6UFTS6TnoAcPA_XICODYQtNYSIv8Fx-PQxDPZMMPaB7acr_dmS3wxUXdO8HGgtobDOIkAw4Ks29cmFD1qbzD8TYW_M9jWl6Q4hdUNygGrlyUw23xfBlcfrn89wmLFUxUvjq9l8ovG2GlpmOgZmB9PASjui8S9k4BvLWeDx0r5QGl8Ze4mIXcwEjtwLobXXTyFqb0cy4ozu41qMIHjyLQm8Hf7SUkDRWPLEzS8nnyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66400" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66399">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
متن تفاهمنامه جمهوری اسلامی و آمریکا:
🔴
1⃣
توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
🔴
2⃣
هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
🔴
3⃣
توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
🔴
4⃣
ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
🔴
5⃣
ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
🔴
6⃣
ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
🔴
7⃣
ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
🔴
8⃣
تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
🔴
9⃣
ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
🔴
🔟
تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
🔴
1⃣
1⃣
صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
🔴
2⃣
1⃣
دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
🔴
3⃣
1⃣
یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
🔴
4⃣
1⃣
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66399" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66398">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛بقایی سخنگوی وزارت خارجه:
تفاهم‌نامه به‌صورت الکترونیکی بین پزشکیان و ترامپ امضا شده. جمعه هم خبری از مراسم رسمی نیست و فقط هیئت‌های ایران و آمریکا به سرپرستی قالیباف و جی‌دی ونس تو سوئیس دور اول مذاکرات فنی 60 روزه برای اجرای تفاهم‌نامه رو شروع می‌کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66398" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66397">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
سخنگوی وزارت خارجه جمهوری اسلامی: متن توافق با آمریکا نهایی شده و به امضا رسیده
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66397" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66396">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=Lm5syJgPhgTm5R3QKMJBwYnzhNw9GgZgqrH25jnazc60ZnzZ-6RRuCiCGTMcqaOf3VN6Ba__Cb7H300wRSh35tU0mysO6f80qcD3ayX5r6OTtsaZZx1X5q7oW8r5la3sxlkGAwwYt9963fNU3YCDwP5k_a_ED2iBr_D9oPSN8eUrMQaZDsG_h92e0mgbjxf0zq17abnPl0h7-5fTk0sqjgHNfjWsB-II0851dI3UDb7z75yL2R_S7GP5ShatYN08TNqd9dMzHIkxqFh1txsaAaXPkNHlXAfcz2_9q3n6jm5iDunbvqf-nID5tbEJcAbpA3vD9Vuzfj_GGVToNQtWrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=Lm5syJgPhgTm5R3QKMJBwYnzhNw9GgZgqrH25jnazc60ZnzZ-6RRuCiCGTMcqaOf3VN6Ba__Cb7H300wRSh35tU0mysO6f80qcD3ayX5r6OTtsaZZx1X5q7oW8r5la3sxlkGAwwYt9963fNU3YCDwP5k_a_ED2iBr_D9oPSN8eUrMQaZDsG_h92e0mgbjxf0zq17abnPl0h7-5fTk0sqjgHNfjWsB-II0851dI3UDb7z75yL2R_S7GP5ShatYN08TNqd9dMzHIkxqFh1txsaAaXPkNHlXAfcz2_9q3n6jm5iDunbvqf-nID5tbEJcAbpA3vD9Vuzfj_GGVToNQtWrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
به محض اینکه آتش‌بس برقرار شد، دیدید که دشمن در خلیج فارس اقداماتی انجام داد و ما بلافاصله پاسخ دادیم.
آخرین نمونه آن حادثه مربوط به بالگرد آمریکایی‌ها بود.
علاوه بر این، دو ناو جنگی دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند - موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن برخاسته بودند، هدف قرار می‌گرفت. همه این اتفاقات در حالی رخ داد که ما همزمان مشغول مذاکره بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66396" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66395">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=T7iuLvGm-9bM204GNIz6t-g_MY9JggbOX5RfJ_ePpy4LzNQWyVNrmEd4LxaFTYwlEBAWh9FLdqnuTZChkBl58nijV_8kFWd1-xOohSsGNyl-rCNrW8XChbRN3_jOG4mmu5o0HEPRRUBsek1yrljITvFln40VycXllw5pQc5b8hnQ1AgzZpGppVo-etSsjVTEBAuFZXcGcxOtKQr6yPeDA4SIS0HWGOyPPxKGc_9Z87hStSrSUboIWuADIuTbrvumBpzYHvLEjNoMLpBFV5aJeRBnyfC57V0OQ0slR3AMXkojmWRG2y_UeWn5EsWLzapf87UuV2WG6AbV58rpLjpXSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=T7iuLvGm-9bM204GNIz6t-g_MY9JggbOX5RfJ_ePpy4LzNQWyVNrmEd4LxaFTYwlEBAWh9FLdqnuTZChkBl58nijV_8kFWd1-xOohSsGNyl-rCNrW8XChbRN3_jOG4mmu5o0HEPRRUBsek1yrljITvFln40VycXllw5pQc5b8hnQ1AgzZpGppVo-etSsjVTEBAuFZXcGcxOtKQr6yPeDA4SIS0HWGOyPPxKGc_9Z87hStSrSUboIWuADIuTbrvumBpzYHvLEjNoMLpBFV5aJeRBnyfC57V0OQ0slR3AMXkojmWRG2y_UeWn5EsWLzapf87UuV2WG6AbV58rpLjpXSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏قالیباف:
نه تنها خودم برای حضور در تیم مذاکره‌کننده داوطلب نشدم، بلکه واقعاً از پذیرفتن آن هم اکراه داشتم. پیش از قبول مسئولیت مذاکرات، هر کاری از دستم برمی‌آمد انجام دادم تا این مسئولیت به من واگذار نشود.
یکی از دلایلی که نمی‌خواستم این مسئولیت را بپذیرم این بود که دونالد ترامپ طراح، فرمانده و ناظر ترور قاسم سلیمانی بود.
سردار سلیمانی برای کل جهان اسلام عزیز بود، اما برای من به‌طور شخصی معنای متفاوتی داشت. آیا فکر می‌کنید برای من آسان است که با چنین فردی بنشینم و متنی را نهایی کنم؟
با این حال، وقتی دیدم هیچ‌یک از مسئولان فرد دیگری را پیشنهاد نمی‌دهند و پیشنهادهای خودم هم پذیرفته نمی‌شود، مجبور شدم وظیفه‌ای را که به من محول شده بود انجام دهم.
ما قرار نیست فقط کاری را انجام دهیم که دوست داریم؛ بلکه باید کاری را انجام دهیم که وظیفه‌مان ایجاب می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66395" target="_blank">📅 23:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66394">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=Akt7GcG2txvCxLxE7eq9A1uhHJjCSVfSmDT5fgRcpDEkplvVxt6Xb5J5IKtmRCPgN3aNkwy19gQfBOHJxGqn4EdeQVCA_iLbkEf0Pf8jI-DOe7B5FASaCpZUKoVY162zUMaO4hEoSpEPTVdUmGWVvSpw-afCl-g7yknSdFInqE_UOj13Jo1-JPJc2qhsVBMEMmn_-gQs_-3oXwLMqulu3JpywME8gL9YWOX7cUYHmiFkyAmPerWI4auHX9aTC5qX3lE7s4_gscdolLpSAsEo68gMe9WKYdtCZHADUketVRi04ekWhhz43DPMY0M3PLsrkZFTzdnlTIrpK8rFc3198w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=Akt7GcG2txvCxLxE7eq9A1uhHJjCSVfSmDT5fgRcpDEkplvVxt6Xb5J5IKtmRCPgN3aNkwy19gQfBOHJxGqn4EdeQVCA_iLbkEf0Pf8jI-DOe7B5FASaCpZUKoVY162zUMaO4hEoSpEPTVdUmGWVvSpw-afCl-g7yknSdFInqE_UOj13Jo1-JPJc2qhsVBMEMmn_-gQs_-3oXwLMqulu3JpywME8gL9YWOX7cUYHmiFkyAmPerWI4auHX9aTC5qX3lE7s4_gscdolLpSAsEo68gMe9WKYdtCZHADUketVRi04ekWhhz43DPMY0M3PLsrkZFTzdnlTIrpK8rFc3198w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
لبنان بخشی از جبهه مقاومت است. طبق توافق، ایران از جبهه مقاومت حمایت می‌کند، در حالی که ایالات متحده حامی و متحد رژیم اسرائیل است.
بنابراین، طبیعی است که وقتی آتش‌بس برقرار می‌شود، باید در همه جبهه‌ها، به ویژه در لبنان، رعایت شود.
باید از مردم عزیز لبنان، به ویژه شیعیان و حزب‌الله، که در طول تجاوز آمریکا و اسرائیل به ایران ایستادگی کردند و نزدیک به ۴۰۰۰ شهید تقدیم کردند، تشکر کنم.
در حالی که ما در شرایط آتش‌بس بودیم، آنها به جنگ ادامه دادند و همچنان تلفات دادند.
وقتی رژیم اسرائیل ضاحیه را هدف قرار داد، ما ایالات متحده را تهدید کردیم و اولتیماتوم دادیم که خواسته‌های ما باید پذیرفته شود؛ در غیر این صورت، ما پاسخ خواهیم داد.
ترامپ مجبور شد در شبکه‌های اجتماعی پست بگذارد و به نتانیاهو بگوید که حملات باید متوقف شود و دیگر نمی‌توان ضاحیه را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66394" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66393">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=GJs3N1Ry-Bd5TgsRi3cypqtbpZks8YMT8-_Ac_BH26-1KwRdkBaZ1HAyCgehvnQ7GEBCVpqfZr9fqpGmpfsFHIgia4EEKk-10rXc48ZSrM7vE1xoVVRKzmYZFwG7INButs-b8eWLXkZFEDKhd1zAbTKc9Xgwfc9Kf_tUOMT2CJa-ldYp3kqAOqgjRHXRm_uGK0CPuuiSJdbfiZyPemKzIVe2t6TitF3R2bBJcLLXDDHEJWVFSwAQKnd8W9S0a4v08ZZ5iKvpK9tNmu99EQ73tFq6LxqontEHFTNPqDna2bUZJCFI5FWfVWCtkgBNtYNGu59egU1hxSCCcMq1jaP2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=GJs3N1Ry-Bd5TgsRi3cypqtbpZks8YMT8-_Ac_BH26-1KwRdkBaZ1HAyCgehvnQ7GEBCVpqfZr9fqpGmpfsFHIgia4EEKk-10rXc48ZSrM7vE1xoVVRKzmYZFwG7INButs-b8eWLXkZFEDKhd1zAbTKc9Xgwfc9Kf_tUOMT2CJa-ldYp3kqAOqgjRHXRm_uGK0CPuuiSJdbfiZyPemKzIVe2t6TitF3R2bBJcLLXDDHEJWVFSwAQKnd8W9S0a4v08ZZ5iKvpK9tNmu99EQ73tFq6LxqontEHFTNPqDna2bUZJCFI5FWfVWCtkgBNtYNGu59egU1hxSCCcMq1jaP2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
بدبینی و بی‌اعتمادی من به ایالات متحده از هر کس دیگری بیشتر است.
حتی اگر توافق نهایی حاصل شود و توسط قطعنامه شورای امنیت سازمان ملل متحد تأیید شود، باز هم قابل اعتماد نیست. تضمین ما قدرت ایران است
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66393" target="_blank">📅 23:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66392">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb769475.mp4?token=naW-ca6A6pO54FYesxFDgvdz2Yy3KiuMVE8AQvljTuc2Jf2Gr_rl1t2-TVEZ9Zs2M67282_ZwHlAUmtPhkutv5AlD5Eks_seKkohMCf5XgqKZR3fSyVFSrZAY-8Hb27NmUTlUPWE1DSNZ_8zV2SKct9FQ7LcQgiV8PYLpKbYU-x3zjlsT5lbQ6OlajLjTbCX-4DBm9RtfHiFF7x-8eBdRHzpeU2B8D4Lw8tT7E5CMrLCwpeJf9AQ-eDgmim1EODfzhkcDQF-LaKYKKgBWT_iDVbBuv3U0u4Nx0NbFRZV3EXBeNCArvq30AlAq47B1MQNzBzeXqCvZPxENEpA8pfcDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb769475.mp4?token=naW-ca6A6pO54FYesxFDgvdz2Yy3KiuMVE8AQvljTuc2Jf2Gr_rl1t2-TVEZ9Zs2M67282_ZwHlAUmtPhkutv5AlD5Eks_seKkohMCf5XgqKZR3fSyVFSrZAY-8Hb27NmUTlUPWE1DSNZ_8zV2SKct9FQ7LcQgiV8PYLpKbYU-x3zjlsT5lbQ6OlajLjTbCX-4DBm9RtfHiFF7x-8eBdRHzpeU2B8D4Lw8tT7E5CMrLCwpeJf9AQ-eDgmim1EODfzhkcDQF-LaKYKKgBWT_iDVbBuv3U0u4Nx0NbFRZV3EXBeNCArvq30AlAq47B1MQNzBzeXqCvZPxENEpA8pfcDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
ما بر ایالات متحده و رژیم صهیونیستی، که قدرت‌های نظامی پیشرو در جهان هستند، پیروز شدیم و اجازه ندادیم که آنها به هیچ یک از 9 هدفی که اعلام کرده بودند، دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66392" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66391">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=UZxKA8Qx1nkUdNXY_dkVSOprchd2LfeKG8cFRu96FF8DbZDnAwfF1DxjgL1rMPjgyR3Hg5ZsCvfBkqL1vnDWFX3uZ71GUnomZusuFTMa4FIKL80vfD6ZPvxzlGySjDbPhKS5825W14Tk4HpXOSSaXTqNdSqVJM_j6yMLEWPzbIXuqfke5NuVumTDXTR31TMYfCVKjBu_ZrOQPLErkjO80xDXqJK9L8XrAjEpZp-SpzkamjzwDKrfden5meSJjRsME96Mi1zex0R5-dsgtM0beqmTzImMJ7J_Qg25RTckvKz8ASBJOhizcNsXL1XK_vOy3x_zbH-vUCO9jg40SRfpOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=UZxKA8Qx1nkUdNXY_dkVSOprchd2LfeKG8cFRu96FF8DbZDnAwfF1DxjgL1rMPjgyR3Hg5ZsCvfBkqL1vnDWFX3uZ71GUnomZusuFTMa4FIKL80vfD6ZPvxzlGySjDbPhKS5825W14Tk4HpXOSSaXTqNdSqVJM_j6yMLEWPzbIXuqfke5NuVumTDXTR31TMYfCVKjBu_ZrOQPLErkjO80xDXqJK9L8XrAjEpZp-SpzkamjzwDKrfden5meSJjRsME96Mi1zex0R5-dsgtM0beqmTzImMJ7J_Qg25RTckvKz8ASBJOhizcNsXL1XK_vOy3x_zbH-vUCO9jg40SRfpOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
تفاوت بین مذاکرات فعلی و دورهای قبلی این است که امروز دانش و دستاوردهای پیروزی در میدان نبرد به عنوان پشتوانه دیپلماسی عمل می‌کند.
در مذاکراتی که به عنوان نوعی مبارزه انجام می‌شود، نه تسلیم وجود دارد و نه شعارهای توخالی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66391" target="_blank">📅 23:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66390">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C50NIXLh-JRj58O5mbCiHWASvYpyiWxQeMNmhKDhrvANGbkmQuMIRr_edETs8FLOh4OCCWHbnHDG-8Z-TSZ1rMsZs9zQ1CfNeB2TNfh_TS845MLS69JQFUBALsKQgQiLC542IMc7LzKkJbHDG-S34mY2m3USDljZJ2ScjOBNtBUkxihBdcDqON_J2w5pKxyfqwLIO13AWDKWHfvMc9CrSPPwmdFDACCcar_IGI5cee_-SBUzdnQJl1quppfpKAbtxrEM0sNxD7GYek2t2QTWUDLrDM-eI4gPbvGZOyzLAI0PynYu2sOWNQpQnPem2yMlPMrmaywp2ccgQLlEwn-P8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شبکه خبر:
مصاحبه اختصاصی رئیس مجلس درباره تفاهم‌نامه پایان جنگ تا دقایقی دیگر
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66390" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66389">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=VOU7N_mPLefmZ8425UI6IH3w89FcUXHEsXYpRvh_u-3IsPUOLsww-jZiqqgfJSqR6DCjdZC53k7ITkv6wN7vOCMlw7TyzYLrc61kQsCh3moDupyGUCy41vzvu_w3J57yGEzUzY2A2JSnPXp-KAVr3wBwwIl7njMMfNVvE3E2TXZ0yYfaHTgjVn-uJYh1wP0wZ3vHOnBgjj39WVftArRteN_flE_51zxhGjhcyGWJ_RSPtuJjL4KQVVmYdKjk6Cp64_-j75yKvX7QJZFUqJE9Y_6Z7-cuw6WEB0_hpnnvXaXBj_x5i4BdLhHtqmHBnWXPCTdC1q-UpQeFIaXVpqhGqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=VOU7N_mPLefmZ8425UI6IH3w89FcUXHEsXYpRvh_u-3IsPUOLsww-jZiqqgfJSqR6DCjdZC53k7ITkv6wN7vOCMlw7TyzYLrc61kQsCh3moDupyGUCy41vzvu_w3J57yGEzUzY2A2JSnPXp-KAVr3wBwwIl7njMMfNVvE3E2TXZ0yYfaHTgjVn-uJYh1wP0wZ3vHOnBgjj39WVftArRteN_flE_51zxhGjhcyGWJ_RSPtuJjL4KQVVmYdKjk6Cp64_-j75yKvX7QJZFUqJE9Y_6Z7-cuw6WEB0_hpnnvXaXBj_x5i4BdLhHtqmHBnWXPCTdC1q-UpQeFIaXVpqhGqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی گسترده انباری در سن-سن-دنی، پاریس
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66389" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66388">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-2FPYcn7T9w_AvDdYz3sdA_URn99_UIgjFqMqntvXNidsuuyzxiuoVuIvfR7_UOSj6Blfl3WspbNE814tZhxTe_zV1Db0GnbjjbCfmyf_2mC7OgmkGFO6TEkYiFZ2XOaXz8uWimJtYjej6TH8Vo98uBuIkzHC4GsVp89freXVHGRR2wW37uy0Ng27cUgC0gScwCq8nnkkej16zXuMLuu-9kdEWoyhUy-Bn-9rKHoFFsJyag-iu0oKMfaD7BkjZr5C8uzpTQfCKmYfoMKzfyBjqZ-w__BEDomeMgbXxlb6WffKx5Bg-jCeO5BfbQBCA_hKRbrKGsITyzDO8XdJOlIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیندزی گراهام: من همین الان یک بحث بسیار طولانی و سازنده با ویتکاف  در مورد ایران داشتم.
بعد از این بحث، به نظر من امضای تفاهم‌نامه برای ایالات متحده مفید خواهد بود، تا جایی که تنگه هرمز شروع به باز شدن کند و خصومت‌ها با ایران متوقف شود.اینکه آیا ایالات متحده می‌تواند در مورد برنامه هسته‌ای و سایر مسائل به یک توافق قابل قبول و قابل تأیید با ایران برسد یا خیر، هنوز مشخص نیست، اما من جنبه منفی کمی برای تلاش کردن می‌بینم
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66388" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66387">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=KuUAcjqRJRTQ6AUdI9l4wBN1DA-UsnVAkTQ9bdxl_4A3Njyk9ZVOh6cd1PWvy52rQssFM9bWZ2c__BJDEX36AsaiDVjfKa7P4QpdHpcW8Dq43W-pV_N42xJ2xnv28khbM-AAyMSUQ4G_LNA9_cXatMPa-Lpbijzo3qlyhl5mg5shQS_tDFiA3EfSBwLdnH5CGhwrzVRlLvLltmEN3-Bsl9Tke2q68hkQmlcIaYvJCec__T-hxIpjMguF9fTw9rKWbUI6ZT3EL4ZQjiRRaQbCeZm8FW1_Rk4uiAUBJzUsYAljAk-i16Htw3x8P6_lNCDWzs4ov5CI14hKck4lRl0SFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=KuUAcjqRJRTQ6AUdI9l4wBN1DA-UsnVAkTQ9bdxl_4A3Njyk9ZVOh6cd1PWvy52rQssFM9bWZ2c__BJDEX36AsaiDVjfKa7P4QpdHpcW8Dq43W-pV_N42xJ2xnv28khbM-AAyMSUQ4G_LNA9_cXatMPa-Lpbijzo3qlyhl5mg5shQS_tDFiA3EfSBwLdnH5CGhwrzVRlLvLltmEN3-Bsl9Tke2q68hkQmlcIaYvJCec__T-hxIpjMguF9fTw9rKWbUI6ZT3EL4ZQjiRRaQbCeZm8FW1_Rk4uiAUBJzUsYAljAk-i16Htw3x8P6_lNCDWzs4ov5CI14hKck4lRl0SFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف؛ آن روزی که من پا در میدان دیپلماسی گذاشتم گفتم:
من اینجا آمده‌ام که هم آبرو بدهم، هم خونِ دل بخورم و هم خون بدهم؛ اما اگر کسی فکر کند که از مسیر امام شهید، مسیر انقلاب و عقلانیت ذره‌ای فاصله می‌گیرم، هرگز!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66387" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66386">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=ibH6MCcJjUXnYG1N_ZnAWADuYIeVTeQk7IgSLs_VcTYo3XPhplwbg5-KVPD7Tm3OomejIu9IE_CdO3mq-ErW5AEP5Q8v9Uh1cZ_d9p3Ra5MhfZG6m0DdRSoEpTxr4lD8PoT5i6JNyecO07cvvuSEo2wgwSoyk8NxlhlFt9N5f1R9ItnN1RSolMCrKK7AjaD5aoRp54PWk8wcTk8qZMef68SYS6tNIlgUVvo1UdHX7UMOLy8k12rqVZllEwTgSjJR4n_8hbptMW5g4zcCxhF_aR-l5LZHi8tuHYAICZaHnr_ErlQgjujUqQV-hH2ziIfanEbq8_Ve4r_PO7SgVReN0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=ibH6MCcJjUXnYG1N_ZnAWADuYIeVTeQk7IgSLs_VcTYo3XPhplwbg5-KVPD7Tm3OomejIu9IE_CdO3mq-ErW5AEP5Q8v9Uh1cZ_d9p3Ra5MhfZG6m0DdRSoEpTxr4lD8PoT5i6JNyecO07cvvuSEo2wgwSoyk8NxlhlFt9N5f1R9ItnN1RSolMCrKK7AjaD5aoRp54PWk8wcTk8qZMef68SYS6tNIlgUVvo1UdHX7UMOLy8k12rqVZllEwTgSjJR4n_8hbptMW5g4zcCxhF_aR-l5LZHi8tuHYAICZaHnr_ErlQgjujUqQV-hH2ziIfanEbq8_Ve4r_PO7SgVReN0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
وقتشه که سنگر رو از بچه های لانچر تحویل بگیریم و یه زندگی خوب برای مردم بسازیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66386" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66385">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=fwV4v5ayRgLSu3T0s0yjbUmQ_T4wPoCHxYWhA4akBdaCp3CUeYxiUyOV7ucBSFYx0UTyFcnT9htx-NBya37KjzpkmivFmfl0dutbsCmEmu_hMRaYfL6fuecFF11e2be05bzxmKd_8aS-J41qCX7gJSAy-Z3aWsr2OeONU7ODzbAcmSLMAAW3LMx5Pa3R0j4vdNFHgrQL9R0FFhLjSg-zRuotuNbEIX3QmdYMRNE9uw4dGICw4AA-TJdc-E2ns9IAnFS91CwXxQ5GDp-_YjBeZIK90JPDNzHKmjsFKvf5HikcIPOA7k4sX2utPNz7P260clVumG4ACTV1bFYUjENLFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=fwV4v5ayRgLSu3T0s0yjbUmQ_T4wPoCHxYWhA4akBdaCp3CUeYxiUyOV7ucBSFYx0UTyFcnT9htx-NBya37KjzpkmivFmfl0dutbsCmEmu_hMRaYfL6fuecFF11e2be05bzxmKd_8aS-J41qCX7gJSAy-Z3aWsr2OeONU7ODzbAcmSLMAAW3LMx5Pa3R0j4vdNFHgrQL9R0FFhLjSg-zRuotuNbEIX3QmdYMRNE9uw4dGICw4AA-TJdc-E2ns9IAnFS91CwXxQ5GDp-_YjBeZIK90JPDNzHKmjsFKvf5HikcIPOA7k4sX2utPNz7P260clVumG4ACTV1bFYUjENLFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد پرونده اپستین:
ما نمی‌توانیم فقط به این دلیل که فکر می‌کنیم چیزی اشتباه است، مردم را تحت پیگرد قانونی قرار دهیم.
شما فقط می‌توانید مردم را در صورتی تحت پیگرد قانونی قرار دهید که مدارکی برای اثبات تخلف آنها داشته باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66385" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66383">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه جمهوری اسلامی:
در یادداشت تفاهم ۳بار ذکر شده باید جنگ در همه جبهه ها از جمله لبنان پایان یابد.
همچنین بر حاکمیت لبنان تاکید شد و حضور ارتش اسرائیل با آن در تضاد است.ادامه اشغال اسرائیل از جنوب لبنان نقض تفاهم‌نامه است و اقدامات لازم را اتخاذ خواهیم کرد.
یکی از بندها تایید میکند که آغاز مذاکره و ادامه آن مشروط به اجرای تعهدات است ازجمله توقف جنگ که شامل لبنان هم میشود.جنگ بایددر همه جبهه ها از جمله لبنان متوقف شود تا مرحله مذاکره آغاز گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66383" target="_blank">📅 21:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66382">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=fzLU7pN9KzGh4ZEPXWScjF703m6c_KOlB2-pfgmj0Cl6zMJA29ToAXoLyPRDz0H97CM-HZ6BPxCtZ2LVA2Zy-LsQWxXghrO5uVnoWMYJUukfP7Vcqji0ZZFWuCgy951SV9EFNFUqvsxPV1-1c8vgw-E2BdT3ZKDQvgFIFA1HTXq6INwgiW10D91TLJTEn45nlr_f79RT0uE4nIi-qOlojeRvZsXcsMkYgFMAKOFzqILPkRE-qfGJinjWB0DBS7mrukwYXSdN9Q1EhZpuy_6xHQ4c57o_8ErG9N7GtRI4-d3ORkuxhHOcFDNYi8U9W-3fXGnK68SyTF5PcMLjLNsFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=fzLU7pN9KzGh4ZEPXWScjF703m6c_KOlB2-pfgmj0Cl6zMJA29ToAXoLyPRDz0H97CM-HZ6BPxCtZ2LVA2Zy-LsQWxXghrO5uVnoWMYJUukfP7Vcqji0ZZFWuCgy951SV9EFNFUqvsxPV1-1c8vgw-E2BdT3ZKDQvgFIFA1HTXq6INwgiW10D91TLJTEn45nlr_f79RT0uE4nIi-qOlojeRvZsXcsMkYgFMAKOFzqILPkRE-qfGJinjWB0DBS7mrukwYXSdN9Q1EhZpuy_6xHQ4c57o_8ErG9N7GtRI4-d3ORkuxhHOcFDNYi8U9W-3fXGnK68SyTF5PcMLjLNsFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره محمد بن زاید:
محمد در امارات متحده عربی یک جنگجوی باورنکردنی است.
هفته پیش بمب می‌ریخت، گفتم «کی داره این همه بمب می‌ندازه؟» امارات بود. او یک جنگجوی خوب است
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66382" target="_blank">📅 21:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66381">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwEgAcDpGyUJMkbiQVg1BfzXmTsqJAf72AeHjMnNe0WKFtIklABqaghh5KQsmnchYFehvw0UFfGA2j506buzqK-V7Qeev1OlFGgbiO3cXKfDevBQC4KK-l5jiu3VYJJyrybCqo23l9yDhoeFYHrjtuPM0yuMs_Mfixe_oMMugdm8_HhxgsZFbkUrVocXvH3GVje_ggWgzQEw_BxoOwq8N78g5rRsUu8odljOeUkHugsGbIDMMLL4wqQOT9jTa7bSYshEnXhB591nBKZN5W1kmzIkqB9Qz33YOq28TITAX50lwo5-XGhYZm11vL3lVO7WqqStSyh11j7sd11F9wSoZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛الجزیره به نقل از وزارت امور خارجه ایران:
ما در حال حاضر در حال بررسی ایده امضای یادداشت تفاهم از راه دور توسط روسای جمهور ایران و ایالات متحده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66381" target="_blank">📅 21:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66380">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729c69207c.mp4?token=mTvZ3B_BRhTW-Xt7bomoE0QoPeDvbegBZCrpF8aIXI5FKNkTnzgaYrLSPP_4gVcTljtURfHeiGiAhKxVb6ui9K9onET8usFXJPW4RfgkzRuCUgroMWx2WhZ_YwzTD7vJbhpXaXLM1XdwGJIAyzG175OcUJEG8vaMkFWrhE2FINRo4KohqAI20xpXxW420HmpdNEYaU3QQZzVXrzPBu94O-YruApxN_qhQrtrX4Rbn0CdJfJbT4ti6w83MsP5x17XlZ7MYVnE3ZisEk2Y9eOtxFAX-79PjFagSBQdZA3ARLymp4voANd0BEy6Ea90jFDlpMZEFhx9QyKcZOD-xOSLrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729c69207c.mp4?token=mTvZ3B_BRhTW-Xt7bomoE0QoPeDvbegBZCrpF8aIXI5FKNkTnzgaYrLSPP_4gVcTljtURfHeiGiAhKxVb6ui9K9onET8usFXJPW4RfgkzRuCUgroMWx2WhZ_YwzTD7vJbhpXaXLM1XdwGJIAyzG175OcUJEG8vaMkFWrhE2FINRo4KohqAI20xpXxW420HmpdNEYaU3QQZzVXrzPBu94O-YruApxN_qhQrtrX4Rbn0CdJfJbT4ti6w83MsP5x17XlZ7MYVnE3ZisEk2Y9eOtxFAX-79PjFagSBQdZA3ARLymp4voANd0BEy6Ea90jFDlpMZEFhx9QyKcZOD-xOSLrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر آنها به توافق‌نامه پایبند نباشند، یا برخی موارد حتی در توافق‌نامه ذکر نشده باشد - این یک یادداشت تفاهم است، اما ما بدون نوشتن آن، از برخی موارد درک داریم - و، اگر آنها به آن پایبند نباشند، احتمالاً به بمباران آنها تا زمانی که به آن پایبند باشند، برمی‌گردیم.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کارهایی می‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66380" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66379">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
#مهم؛ پس از روی کار آمدن مجتبی خامنه‌ای به‌جای علی خامنه‌ای، #سعید‌_جلیلی نماینده‌ی سابق علی خامنه‌‌ای در شورای عالی امنیت ملی عزل شده و #علی_باقری‌کنی( برادر مصباح‌الهدی، داماد علی خامنه‌ای ) جایگزین وی شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66379" target="_blank">📅 21:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66378">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=GdSfUbZ7Nwht9FMNb3GMyGYrVdYFRLlNPx4piVlKQf2rJf9rNVY42WgxrGAlxgqTUpesLyZAPZfxJHFEtwRVISkc3dsNMDJm4GuJI5kkbTiTDTgOT5aqeHiJPLNAz-U-PT4mOh_e8kXTb4CR81V9UFNgShLJOlhGMG7UB7TOpMwBiRsU7Bw5O2Bvi4rCFbsxaCp76hefoqDmWXy82bQfoQbqlOszWLp8t8BrBZ5PFzuNzPbnRqAnXKjT9t4VexIRs2JKgS3v6NObxaIUsViQD0ClWDBVMsJFQVLyUim1_mUSte553hp05-nC0Lr3yukiTCN08Zk_zcPdBdsP2ryZ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=GdSfUbZ7Nwht9FMNb3GMyGYrVdYFRLlNPx4piVlKQf2rJf9rNVY42WgxrGAlxgqTUpesLyZAPZfxJHFEtwRVISkc3dsNMDJm4GuJI5kkbTiTDTgOT5aqeHiJPLNAz-U-PT4mOh_e8kXTb4CR81V9UFNgShLJOlhGMG7UB7TOpMwBiRsU7Bw5O2Bvi4rCFbsxaCp76hefoqDmWXy82bQfoQbqlOszWLp8t8BrBZ5PFzuNzPbnRqAnXKjT9t4VexIRs2JKgS3v6NObxaIUsViQD0ClWDBVMsJFQVLyUim1_mUSte553hp05-nC0Lr3yukiTCN08Zk_zcPdBdsP2ryZ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
مردم از من می‌خواهند پل‌ها را بمباران کنم.
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن ایران.
اما ما آن پل را بمباران کردیم، دیدید که
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66378" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66377">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=v5pn5oJMWJ6lIE380G_NW7YwksBOiP_UolFM2tRqGO0fmEwahos0m1Yk2UY79efAN7xFMqDkVCE6RcCU_sEFI9es_KQGqGQMBi1PblXHfTbhh2qOSBh7A6dkVKp8ve2XKM5R5hOursrX8mlWTGSSUI7_Q626HoKEDKqEWvjDYoOw8DuAdihkyfIiBKfU7X92-WnhcwpMej_aPBWb_LLsq5y25atoeNFD644EQJfYNz-17EuyMrkE7bQtiNklDrW5kARAcfcWyQLVFO1W1J8c3Te6-xsy1k3BPm6TAAQ7to0D9GvKY-ilEKmmLmvDMoFXDDghS-Cx-lDR0UhEk4WcLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=v5pn5oJMWJ6lIE380G_NW7YwksBOiP_UolFM2tRqGO0fmEwahos0m1Yk2UY79efAN7xFMqDkVCE6RcCU_sEFI9es_KQGqGQMBi1PblXHfTbhh2qOSBh7A6dkVKp8ve2XKM5R5hOursrX8mlWTGSSUI7_Q626HoKEDKqEWvjDYoOw8DuAdihkyfIiBKfU7X92-WnhcwpMej_aPBWb_LLsq5y25atoeNFD644EQJfYNz-17EuyMrkE7bQtiNklDrW5kARAcfcWyQLVFO1W1J8c3Te6-xsy1k3BPm6TAAQ7to0D9GvKY-ilEKmmLmvDMoFXDDghS-Cx-lDR0UhEk4WcLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
گسترش توافق‌نامه‌های ابراهیم چیز دیگری است که امیدواریم به آن دست یابیم.
و من فکر می‌کنم اگر عربستان سعودی پیشگام شود، لطف بزرگی به خودش می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66377" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66376">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=gTBt5OJZUS7_UFxbamqgE5vc6moAqhmGQ7hO5QAEyQLp1MopfMvJbI9oHqBOo0KNN9uhqC_7o85xR_xg1SJGdhVJ2OK2dfM6wlTW-r7cDdjwpHk7IZU1swl0IqTnDfx4sL_ZZviuEFrADcEqkCubrN5akRr0YJStszFhW_w0NsviX8hLIzRFbNHjHyN2NH7BXIEgsceXzyiOwXAaMiXHzsNLwvr3huAbgyxlTLTtFWLznK-fSXRm42taV_aIwTIdv3-eVAP56emINOc-Y2iT-KAdDpGxP8mgVg9BzMSdxZsgNRKCRas6raEN3aZrMz7BVKsxPNzdis4xF_5W5TsM3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=gTBt5OJZUS7_UFxbamqgE5vc6moAqhmGQ7hO5QAEyQLp1MopfMvJbI9oHqBOo0KNN9uhqC_7o85xR_xg1SJGdhVJ2OK2dfM6wlTW-r7cDdjwpHk7IZU1swl0IqTnDfx4sL_ZZviuEFrADcEqkCubrN5akRr0YJStszFhW_w0NsviX8hLIzRFbNHjHyN2NH7BXIEgsceXzyiOwXAaMiXHzsNLwvr3huAbgyxlTLTtFWLznK-fSXRm42taV_aIwTIdv3-eVAP56emINOc-Y2iT-KAdDpGxP8mgVg9BzMSdxZsgNRKCRas6raEN3aZrMz7BVKsxPNzdis4xF_5W5TsM3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد اورانیوم:
هیچ‌کس نمی‌تواند به آن دست یابد، بنابراین مهم نیست که ما این کار را به سرعت انجام دهیم، اما می‌توانیم آن را نسبتاً سریع انجام دهیم. هیچ‌کس نمی‌تواند این کار را انجام دهد. و اگر آنها این کار را انجام دهند، ما با موشک‌های پاتریوت به آنها ضربه خواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66376" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66375">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=a9u8wolfB1_edeoNNtFMg-2mjWlLh9dKgO--Sma2qvQMUCbn0Z0FvUN7Jk5knu4MaKOWwSIIKFb2uhqTbPHxYTX2JAYGciUiqprWbfXYWnBA9P00EFysqD_trFKfiDzNyymQ-i4UGg4SQnod542EzDoEIg1s9WR0reQ9rrwVkEpvUikpXOOGPQrrzqrF1QKwqTG-SbDBOeW6KfUwkhbia2EwIog2J9Drrl7mxsLrJAflLWi_z3NfvhQQKcXcXdP0wkdbJnU06wBsulWUREi4VBcvID_06Dh8FUBijPNdjCEs0zczGtFPg9xOkvNIcmlFj4jmZ9auwyrjN7XK0k74YmrLnS9FBSgs48lm4BildI5r8MJIWbqiAERZ241k1YdpJwdbYJDUIH0OfznrrpNqebK-GiU50V1eUYle7KFmvkbb5mOblRmWFYaZbl6Lb9iL6PWIoxF2VxgJ7Q_2ce7WtvJnxFonhHpnoV5IRejy8UBstrWBLx0FYDKbHuwrv0VSfZmi_ln3MsVa_uC0laB2fUTgwqzhEbfxLsjTSLJsvSM6461afRUgcdxXGrA-DqpNVHRDtJJ0r-1Q8E1nsVW6opITLeC7nJh6sQVXgbELse8W7CjpR5B9UmTvgiZmhQOwd99BZ8G_zK4-S6yKBKltloda8SsptcTpKcB04TxyqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=a9u8wolfB1_edeoNNtFMg-2mjWlLh9dKgO--Sma2qvQMUCbn0Z0FvUN7Jk5knu4MaKOWwSIIKFb2uhqTbPHxYTX2JAYGciUiqprWbfXYWnBA9P00EFysqD_trFKfiDzNyymQ-i4UGg4SQnod542EzDoEIg1s9WR0reQ9rrwVkEpvUikpXOOGPQrrzqrF1QKwqTG-SbDBOeW6KfUwkhbia2EwIog2J9Drrl7mxsLrJAflLWi_z3NfvhQQKcXcXdP0wkdbJnU06wBsulWUREi4VBcvID_06Dh8FUBijPNdjCEs0zczGtFPg9xOkvNIcmlFj4jmZ9auwyrjN7XK0k74YmrLnS9FBSgs48lm4BildI5r8MJIWbqiAERZ241k1YdpJwdbYJDUIH0OfznrrpNqebK-GiU50V1eUYle7KFmvkbb5mOblRmWFYaZbl6Lb9iL6PWIoxF2VxgJ7Q_2ce7WtvJnxFonhHpnoV5IRejy8UBstrWBLx0FYDKbHuwrv0VSfZmi_ln3MsVa_uC0laB2fUTgwqzhEbfxLsjTSLJsvSM6461afRUgcdxXGrA-DqpNVHRDtJJ0r-1Q8E1nsVW6opITLeC7nJh6sQVXgbELse8W7CjpR5B9UmTvgiZmhQOwd99BZ8G_zK4-S6yKBKltloda8SsptcTpKcB04TxyqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💥
پرزیدنت ترامپ:
هیچ‌کس سخت‌گیرتر از من نبود. هیچ‌کس سلیمانی را نشانه نرفت.
می‌دانید، وقتی من سلیمانی را هدف قرار دادم، مردم فکر می‌کردند این بزرگترین اتفاقی است که در خاورمیانه در ۵۰ سال گذشته رخ داده است. این بزرگترین رویداد بود.
او رئیس ایران بود و مورد احترام، اما او یک نابغه دیوانه بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66375" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66374">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=kNTVR51C9jpVEgZCU91-6F_cBvhbPVdiQPSNkAJRagoY8xx9HNpCDF9gUu2cNCRnOgzn18AwqOCOJGU-gOs7eGj7lTnw1nPGJVPCiSvcKsNibkunAQPOhWfBVoXBACUoz43X__uoBQ0WFLKoxrpcU_DUugvpISh3DA4hBxpU04qj0UmLyD_kh9TpPdqhHAC6GaQpwp7BEUWj1DkWKj7fxpoYiGv5fBsR4x-KCNJLQWu9wHKtXIN6ZvOebgumTLk6l9WWVGVL0RlLBB9pA3Jeow3Ln9OL8DRQ683almPX7yIeGu_X_fyugxC7sql53eGB0IkNdhu2SUFAWT2Ne2QX0GM5WD0cmRZCxDZhoBn8KZKaRJXDfU9njePGxFyXJ9ovyMgiMSbe-KiCWIeb6gvkcLuqsf3ncK38ir2jfGmbzrpxFF068IJzRZv8j-M5cXvpycIT8sLUQ50Qm6JjNOBoxeSTRskWlf-HSOAC_9XiyZQfjydBN-SxSSwshPUhsfMuUnHQgdv060pmQ0FeLS2wIjA4d_lzLjdmIP__BmtdMS1H8URxMURQahiMFN0s5pS6uCgg-37ReIylD5w5fGU7UdSNPXCRvNHRG1YusVMeUPv52ex7g9GVzMvIBna0X5T1xnFfcSFxsoPofsXuy-VBrh707LPTeN2DIEbaBQlQUwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=kNTVR51C9jpVEgZCU91-6F_cBvhbPVdiQPSNkAJRagoY8xx9HNpCDF9gUu2cNCRnOgzn18AwqOCOJGU-gOs7eGj7lTnw1nPGJVPCiSvcKsNibkunAQPOhWfBVoXBACUoz43X__uoBQ0WFLKoxrpcU_DUugvpISh3DA4hBxpU04qj0UmLyD_kh9TpPdqhHAC6GaQpwp7BEUWj1DkWKj7fxpoYiGv5fBsR4x-KCNJLQWu9wHKtXIN6ZvOebgumTLk6l9WWVGVL0RlLBB9pA3Jeow3Ln9OL8DRQ683almPX7yIeGu_X_fyugxC7sql53eGB0IkNdhu2SUFAWT2Ne2QX0GM5WD0cmRZCxDZhoBn8KZKaRJXDfU9njePGxFyXJ9ovyMgiMSbe-KiCWIeb6gvkcLuqsf3ncK38ir2jfGmbzrpxFF068IJzRZv8j-M5cXvpycIT8sLUQ50Qm6JjNOBoxeSTRskWlf-HSOAC_9XiyZQfjydBN-SxSSwshPUhsfMuUnHQgdv060pmQ0FeLS2wIjA4d_lzLjdmIP__BmtdMS1H8URxMURQahiMFN0s5pS6uCgg-37ReIylD5w5fGU7UdSNPXCRvNHRG1YusVMeUPv52ex7g9GVzMvIBna0X5T1xnFfcSFxsoPofsXuy-VBrh707LPTeN2DIEbaBQlQUwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ :
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آن‌ها بسیار کمتر تندرو شده‌اند. فکر می‌کنم آن‌ها خوب هستند و واقعاً کشورشان را دوست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66374" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66373">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRZUbT_RoeQDfZzOrMu-Vu4zrhKstGyoN4im9rkVDw8j3iPCvKBYei2_tIoF8FmqxXc_Jef3djfzqg2O-DbNQzOshcc7eSRrzMKsbEVGaJTOUPRwhtAjoqQXfn005a2V6ktTLWy48GlFWcG25wJhVTQhP3q1mP9kTdLo_rvpY_xmoMEyPc4M3WqJ7ZWooyo7gYWc8WOvDuCCbx8TRr-Ac06b37KACGAwAJtzuKsTDWL5oZzK0gIB8mj-8dRi9wCbGgyaJtZe4d7BTaxaryA6SoX1OBVvcTU9_yGWj42GdI_S9MT_ezOxWZrv72f50EiHrV0vrfJXXbg5ePY8FbGKQxBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRZUbT_RoeQDfZzOrMu-Vu4zrhKstGyoN4im9rkVDw8j3iPCvKBYei2_tIoF8FmqxXc_Jef3djfzqg2O-DbNQzOshcc7eSRrzMKsbEVGaJTOUPRwhtAjoqQXfn005a2V6ktTLWy48GlFWcG25wJhVTQhP3q1mP9kTdLo_rvpY_xmoMEyPc4M3WqJ7ZWooyo7gYWc8WOvDuCCbx8TRr-Ac06b37KACGAwAJtzuKsTDWL5oZzK0gIB8mj-8dRi9wCbGgyaJtZe4d7BTaxaryA6SoX1OBVvcTU9_yGWj42GdI_S9MT_ezOxWZrv72f50EiHrV0vrfJXXbg5ePY8FbGKQxBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پرزیدنت ترامپ:
روز یکشنبه، ما به توافقی با ایران دست یافتیم که به همه چیزهایی که در نظر داشتیم دست پیدا می کند - همه چیز و خیلی بیشتر. جلوگیری از دستیابی ایران به سلاح هسته ای همه چیز در مورد همین بود. این حدود 99 درصد بود. آنها نمی توانند آن را توسعه دهند یا بخرند. آنها هرگز نمی توانند سلاح هسته ای داشته باشند
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66373" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66372">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/66372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66372" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66371">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBw3vKNLZnRGMUnVqm-OR5-ZO1cai1_Q6R9GgdR6f_eMhyXxvZQ5MurED6cplmyQchcvNdY8unU0SnYTp4NQ2rDHQEHiBn_Mfkmuw_cDB1d77r_I84edelJOnnbQbDHPz2kXQQ91XHktMhDbM7hWSTVHEOPptQWykYN-fTI0NZjI_kyyDVDm1DeaD9vS2ns8RF1Xk0D3d7BLtmh723_ow-xvB5wVTDw8QtlD5NZZOSrbUv5FH6TVbMsWjHWmoUY_eUCMruQdAK02Yh3Hs3SbrCvvPISvvDJpNlFfPJaDsnqsapLcVvXY7EssYungFE7ooonmIm0gR9iSO3GzIxOogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66371" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ifbs7iejCCp6Ex5hA05PPqJ9wQhipbTgimA1TizZMFRQi78B9NX9SFFOLrsCVFKKFZ6qN2RReUFx0ingV4QRvXHglCMGf19apmS2AkCVL3zItTZAG7SPOH4y_6esBo1zVo2v283RoNMGKcDjFEjt6Mt7JSihnKNulAvtA6gL4-kc0bAI-G6iWt7K22ozl-IOqY5NSKfve9vfn-iv7_eDVEV40Yitez0dVF-EWSV5kdGRPhBcA2_Wudoju8bmhuHpZDsC8KzLsFw60zSA3TcNXp1OQBnddtRVdvE1BZSfq0tYSX7hrGbCgkmaCIcsWEfKOsftNcbg23v3JpXD16mwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توییت قالیباف:
تعهد ایران به همکاری برد-برد که بر پایه مشارکت استراتژیک جامع با چین بنا شده، قاطع است.
در جلسه‌ام با اتاق بازرگانی ایران تأکید کردم: ما مصمم هستیم که اجماع استراتژیک خود را تحت GDI به نتایج عملی تبدیل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66369" target="_blank">📅 19:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53224e4497.mp4?token=S6ZR7WqssFE3T9V3YIkoucDqDQymsJCnbhrd4qlZBo8BQbgmLFwEyNjkGebGiN4pKlnnZkLgzq6fRrZ2GeSHqqAwyjcxVQqp3uWmT8Yz0QCgEMBQOLZ0n9S4fA5fY9KguWfB4Pq5S24nwF46W8ZStyZ3e_r5N2x7Fz57Vn6TCFTKje_hG2d-RS1JFL4jOI6YQYwGRvnpb5WLxaQiHGtpSEkp7JPopK3IFykQyfcgYEmgyqABfG1MyBq3LpLuu56GSBaqQjPzikKBsSZwFSOT-dbgJ_iROTNo7j2v9WmePejlSC4XSPx1Q5d9W-hIuqBAJdtgDjkRV1H0p0m1rijfNALt-jEXyhE32BqhOjHDOlEFQR_n3kdFMYj-Esz4uALSEGau9mc2QmAzS2exZ0YqKweFmAzNkVF25O9R1qRcdEFZ-qqtPLGcaHfC7Bwvta1iIMzfzjR2SehBRCPMiKRpq3Og_0Qh4gEhubJpFchWocoGYawnelt4UW7pUEnvLdINTkon1QXn_03WYiNND79JNiny2aD4fFY7wjSe6ttJMNK_T7hl7KSIdHB1bAd1ApXzM_pd-tJViFggVKgYu8FDmQQCp92Lj2bJwfqi99eyYTXr_ZeJji3Y1Eihni_eAk5LXSCTyi8A9tL6u1xgTpEgAFsv82o1ClRh6RuhS7arDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53224e4497.mp4?token=S6ZR7WqssFE3T9V3YIkoucDqDQymsJCnbhrd4qlZBo8BQbgmLFwEyNjkGebGiN4pKlnnZkLgzq6fRrZ2GeSHqqAwyjcxVQqp3uWmT8Yz0QCgEMBQOLZ0n9S4fA5fY9KguWfB4Pq5S24nwF46W8ZStyZ3e_r5N2x7Fz57Vn6TCFTKje_hG2d-RS1JFL4jOI6YQYwGRvnpb5WLxaQiHGtpSEkp7JPopK3IFykQyfcgYEmgyqABfG1MyBq3LpLuu56GSBaqQjPzikKBsSZwFSOT-dbgJ_iROTNo7j2v9WmePejlSC4XSPx1Q5d9W-hIuqBAJdtgDjkRV1H0p0m1rijfNALt-jEXyhE32BqhOjHDOlEFQR_n3kdFMYj-Esz4uALSEGau9mc2QmAzS2exZ0YqKweFmAzNkVF25O9R1qRcdEFZ-qqtPLGcaHfC7Bwvta1iIMzfzjR2SehBRCPMiKRpq3Og_0Qh4gEhubJpFchWocoGYawnelt4UW7pUEnvLdINTkon1QXn_03WYiNND79JNiny2aD4fFY7wjSe6ttJMNK_T7hl7KSIdHB1bAd1ApXzM_pd-tJViFggVKgYu8FDmQQCp92Lj2bJwfqi99eyYTXr_ZeJji3Y1Eihni_eAk5LXSCTyi8A9tL6u1xgTpEgAFsv82o1ClRh6RuhS7arDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
معامله‌ها شگفت‌انگیزند. من تمام عمرم معامله کرده‌ام. وارد معامله‌هایی شده‌ام که صد درصد قطعی بودند، اما اتفاق نیفتادند. وارد معامله‌هایی شده‌ام که هیچ شانسی برای انجام‌شان نبود، اما انجام شدند و به آسانی انجام شدند.
پس هرگز نمی‌توانی درباره معامله‌ها مطمئن باشی. اما خیلی زود متوجه خواهی شد. فکر می‌کنم انجام خواهد شد.
آنها می‌خواهند امضا کنند  می‌خواهند به زندگی عادی بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66368" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=uTnviUTMRA8SVmlF0wI0lcO66dtjr6VvT_NIhfkpAJjVwHzvTtlnp-nk6gwUAheCNNQNOyyxKo_0p2Av7sAnvLmViolO8L2lCSXfKwDGIZurh01XcDxZ9BkIHw0rKCkrW8TtOZHtvE_G5AVQm8uZy2WYBiQu0mTUxcyWn3zsPMiFNdGbLSBGLbd2edxqYAZ6ro_IZdLZaA20LcuYGbGYJplqzl_wth1xptxJt22e-cmi493pTAlDio8d8-KEiABdCAhAzdPg5xcb3b1YeJMFhSXRadqPJKfIEyYqf15uqxrUXY7VRU7__mjbPLvPqyEa0w7j_V0o5haS1_z5AVhDUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=uTnviUTMRA8SVmlF0wI0lcO66dtjr6VvT_NIhfkpAJjVwHzvTtlnp-nk6gwUAheCNNQNOyyxKo_0p2Av7sAnvLmViolO8L2lCSXfKwDGIZurh01XcDxZ9BkIHw0rKCkrW8TtOZHtvE_G5AVQm8uZy2WYBiQu0mTUxcyWn3zsPMiFNdGbLSBGLbd2edxqYAZ6ro_IZdLZaA20LcuYGbGYJplqzl_wth1xptxJt22e-cmi493pTAlDio8d8-KEiABdCAhAzdPg5xcb3b1YeJMFhSXRadqPJKfIEyYqf15uqxrUXY7VRU7__mjbPLvPqyEa0w7j_V0o5haS1_z5AVhDUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار: آیا می‌خواهید اروپایی‌ها مین‌روب‌ها را به هرمز بفرستند؟
ترامپ: ما به آن نیاز نداریم، اما اگر بخواهند بفرستند، خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66367" target="_blank">📅 18:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06239668e.mp4?token=Y_LQyed1poBcsf4UGZW7RZabZBq4lnQMmjjwtY-htB_45VdO-848A-T7UUhS8TU37wo5gPdJS0bD3ur0wP4nqgHrelBLtY5J2mPHI26dnVwlZMCLwYjsi9Uem_ki4W4etZ9AZW_8yql_vJ_W2tYpr9gmfVJpwp6DBUaAxc05yC8touAz_GSfqVqK4ydm2vP9xRYIL8IA9z3jng78xl-GjOFjAY7quCOj9JA_ktI6yT6Vc0CkfL9dfQmkY3eWpA4T9TeAoTzngRN3jCtEihbDdsW2LdXfW5x7u3HluOON3VkRV2vyCGA-iSQQ8J_IW1Z_467GdPFpNTQSNNakH_PdXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06239668e.mp4?token=Y_LQyed1poBcsf4UGZW7RZabZBq4lnQMmjjwtY-htB_45VdO-848A-T7UUhS8TU37wo5gPdJS0bD3ur0wP4nqgHrelBLtY5J2mPHI26dnVwlZMCLwYjsi9Uem_ki4W4etZ9AZW_8yql_vJ_W2tYpr9gmfVJpwp6DBUaAxc05yC8touAz_GSfqVqK4ydm2vP9xRYIL8IA9z3jng78xl-GjOFjAY7quCOj9JA_ktI6yT6Vc0CkfL9dfQmkY3eWpA4T9TeAoTzngRN3jCtEihbDdsW2LdXfW5x7u3HluOON3VkRV2vyCGA-iSQQ8J_IW1Z_467GdPFpNTQSNNakH_PdXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا می‌خواهید اسرائیل عملیات نظامی خود را متوقف کند؟
ترامپ: من می‌خواهم اسرائیل بتواند از خود دفاع کند، اما همچنین می‌خواهم از تصمیم درست استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66366" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT2vaxRbGdor-oeJ2EWfBtI65K6V5YA-wdga3q_ZSDRvutARbuRVG4wPaQ6QMPerIgczI_EvB1gkXrQiOLHkvaObJhZvAZz6hNVbNSyj54kL8SQ__lGBeInM39HJ-XzXGHp8sB6_yaORdeUAxdX5o6bFlwHDh2w0vo0DgLuPgrQZ6COwcYDQZjIhWZ2CAcLPOUa0WsQ_bejhgpC7a6xugA7Y1fjUm9qys-yoqLL-hlDJkOlpU_z-6S0kUA731OPbx_VOS5ZyrWxI4FNMxlvRXcvki2RNSPF6TbhMWx8SGY8m1I-VsU1nttz5NK2eI_szqh1e0xB54xz8jOTHO8kJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت سوئیس:
بیش از ۲۰۰۰ سرباز امنیت محل امضای توافق ایران و آمریکا را تأمین خواهند کرد و منطقه پرواز ممنوع برای تضمین امنیت اعمال خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66365" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66364">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvtARVRjNn5ldEAxDeW5u8SozhpMTJ3C5qNdGRDFtT7g2U44f7GkhJCHhgsIcGwwHXtSOdIWPVml2jZHJKaw7cONPZrhxqRUM5A80DJIkG74Owptnp7NrjIUfeq8K5-6os0kSVVmYdV2meCZCHs0m1-b6H2zUHvSXi1iC6rbhbAaEWUuBbNIuc4zhFxSJos5ZTxlhs1RVDlwYdr3ERjOTnTJXOaUhD_neIqajODgnLO5NxFOQbws43PTySLpcZFc-5uRdHkEGYBSeERNIFiDJTh7T1aI_enqHvDQa3bONev9bshUgn649qO7vFbv5S_PZQwjUUCuh9UO59gZ8xsOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزی ۹۰ میلیون سود از جام جهانی
⚽️
برای پولدار شدن تو ایران چنل زیر فالو کنید
⭐
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک برمیدارم
❌
❌
❌
سریع بپیوندید
🖱
سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگادشون
💀
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66364" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66363">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt8P7PoT9PjTgROv3sYZ1jqRqXXhtwlygGNyGmMAIAeF76GxECs7rnmePdvmaS2jJrKuHDircV6jstMVyWQ7Fkj4AjXv0aBj_2ozSi4rzC0L41VkN-RIplX7rX9anIiagudWb394IPF2_oQeBLA9NZ28GAtBf-9b6LCR71IdLbxdNRuygPdZFRz4gkaJRTzQ6QkGe64myMdPSbJbmJVQCZhDdE5qrrchopzg2gWqdOJyFHk0mHBEL28jF2VGdHh3s5qmkEYA5d42C_DBE5F94fqi9VMjLEDmwoJcY4nj1oINOU0_tCZptfOh4bGNGnPl5b1kdG9atnHdiQxNb0fDzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ در تروث سوشال:
۴۵ دقیقه دیگر از فرانسه یک کنفرانس مطبوعاتی خواهم داشت. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه برمی‌گردم! این سفر موفقیت بزرگی بود، اما چیزی که بیشتر مردم می‌خواستند در مورد آن صحبت کنند این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد! اعداد و ارقام بزرگی در همه دسته‌بندی‌ها برای اقتصاد ایالات متحده با تعداد افراد شاغل بیشتر از هر زمان دیگری در گذشته. بیش از ۱۹.۱ تریلیون دلار در ایالات متحده سرمایه‌گذاری شده است، کارخانه‌ها و هر چیز دیگری در حال وقوع است، اما مهمتر از همه، اعداد و ارقام اخیر بازار سهام به دلیل توافق بسیار بالا هستند و به همین ترتیب، قیمت نفت در حال سقوط است!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66363" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66362">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a882497b26.mp4?token=kzT6HSGvYLMYEOjQ7EFfbcpXtaOVIeR6tF9u45b5LoAUuVLDxn3kGF4p090ecuav2epUzT2uDwJX6EHNl4v1mimnwbhRFU4HSQj6_5_OCIQt4XTXyh2O3JhpD4pjsHwCfiRI1uVxBN78x85q_XWjTOIYX3FzbtjQbGXsckHKRTPgNLBHJZFSIiPaCduUS4_0eGA8h3r4k2S4g5KalK0PGfdu447XNWnnKcHlXqPtEdH7a4-zD8Jc4m_ymUh8T_pNXmA7OUs16urlqr_0ApbWfrbJHorKKQVF8u2hhX5vfimGdCP-0ehh4wfhu-bmhnUGN0LfuhCLrIr_4oucfFOn6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a882497b26.mp4?token=kzT6HSGvYLMYEOjQ7EFfbcpXtaOVIeR6tF9u45b5LoAUuVLDxn3kGF4p090ecuav2epUzT2uDwJX6EHNl4v1mimnwbhRFU4HSQj6_5_OCIQt4XTXyh2O3JhpD4pjsHwCfiRI1uVxBN78x85q_XWjTOIYX3FzbtjQbGXsckHKRTPgNLBHJZFSIiPaCduUS4_0eGA8h3r4k2S4g5KalK0PGfdu447XNWnnKcHlXqPtEdH7a4-zD8Jc4m_ymUh8T_pNXmA7OUs16urlqr_0ApbWfrbJHorKKQVF8u2hhX5vfimGdCP-0ehh4wfhu-bmhnUGN0LfuhCLrIr_4oucfFOn6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نه از دوست شانس آوردیم نه از دوژمن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66362" target="_blank">📅 17:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66361">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=rvHfI-O-jD6j7nfv7_8gkDOutB3224uFc2b3XTxVhv9y_KqnaT8iuZ3fO8Sch-ZUvBhndemhuYPJNxjtG47rghVtAGQEREcLCwVQiDzzEgHZJWs2qxrTYw44OY0_0aTSlMvqFhJ9MMNp8jsZKUGXyfxH1NQtweiKSvEZcatPSnAXSCQwd7tEl5T6r-YHaz7VgqDV0GsOuc_8Zrap1AcTZJmAaRFSe5WyL15FHgIqPoimUkkIYdA5nj76oAHaS1BRvH5m24fuUz9AoGrM46lv_wkgeIR_ANNoPU1bOKeeuZBnir3Rf432tjVRzCLhsLpWKeBEjWltLq-4scnGfW9LUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=rvHfI-O-jD6j7nfv7_8gkDOutB3224uFc2b3XTxVhv9y_KqnaT8iuZ3fO8Sch-ZUvBhndemhuYPJNxjtG47rghVtAGQEREcLCwVQiDzzEgHZJWs2qxrTYw44OY0_0aTSlMvqFhJ9MMNp8jsZKUGXyfxH1NQtweiKSvEZcatPSnAXSCQwd7tEl5T6r-YHaz7VgqDV0GsOuc_8Zrap1AcTZJmAaRFSe5WyL15FHgIqPoimUkkIYdA5nj76oAHaS1BRvH5m24fuUz9AoGrM46lv_wkgeIR_ANNoPU1bOKeeuZBnir3Rf432tjVRzCLhsLpWKeBEjWltLq-4scnGfW9LUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی: «صرف‌نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود»
شاهزاده با رد مشروعیت هرگونه توافقی که بقای رژیم تروریستی جمهوری اسلامی را تضمین کند، تأکید کردند: «صرف نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود... بقایای این رژیم هرگز در نظر مردم ایران قابل قبول یا مشروع نخواهند بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66361" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66359">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=O7mAibxnspVPg0hmW-L01t7mQ0vzl7-oQdl7mYn_J4werQTVO71bm5wM7uBdYUvouzDikw4-nAa1seDaNRFC98CoCyROeGcaed9pvaqVTMeA5uupMg2fh7q0CQNNEtA6RGCHxevOvljLfLmFLGTPmFEZeG_fBOpztXSKIMvDK1K_YPqFFO31VFyoyVxA6ZNHbfWaKFR1csHmzeHQSi21AhO4ZdaubIR9qth6wLAfIjkfKSVFxSLnBlGBNQbE8piM_Gi6eaopVY9LADOj5RUCEvgo1qDXtwSizLLCO-CtVwkI_jRwQgFadDOHgaj6jsTy0jot0OiYQ-iDOnBw0LEKSUA_-pYemFgydSJtex5PFJ9ZopX04_Tb8p7k_9kWQk53vjDwIKlYFXH97c2r8KRXAo1EZRZ71BBmcCPC6E0qpBlcS-ic42NkchFskrO3S4JKWo_l_YaJ54dp0-Z0IToDDM1sA6AWRYNdUarf6BYgHF_hU7HPsXC2SuUdqAuQebFAA_y-WkOzAKd8B4DaXSc-LoQK_9AxwRpsYunbNrGeKY-wikiwkvgHMNm1xvVt3B3Aq0vnTYoGhGU6iFlpCa4dpLF_f-fTVglZCOlIW-DEHPym2dG8kZmIa82M8-sqv9GySw4sM8D_60T1SK-hgA3kBxc9P9xX-LUPcqKhSZwDbYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=O7mAibxnspVPg0hmW-L01t7mQ0vzl7-oQdl7mYn_J4werQTVO71bm5wM7uBdYUvouzDikw4-nAa1seDaNRFC98CoCyROeGcaed9pvaqVTMeA5uupMg2fh7q0CQNNEtA6RGCHxevOvljLfLmFLGTPmFEZeG_fBOpztXSKIMvDK1K_YPqFFO31VFyoyVxA6ZNHbfWaKFR1csHmzeHQSi21AhO4ZdaubIR9qth6wLAfIjkfKSVFxSLnBlGBNQbE8piM_Gi6eaopVY9LADOj5RUCEvgo1qDXtwSizLLCO-CtVwkI_jRwQgFadDOHgaj6jsTy0jot0OiYQ-iDOnBw0LEKSUA_-pYemFgydSJtex5PFJ9ZopX04_Tb8p7k_9kWQk53vjDwIKlYFXH97c2r8KRXAo1EZRZ71BBmcCPC6E0qpBlcS-ic42NkchFskrO3S4JKWo_l_YaJ54dp0-Z0IToDDM1sA6AWRYNdUarf6BYgHF_hU7HPsXC2SuUdqAuQebFAA_y-WkOzAKd8B4DaXSc-LoQK_9AxwRpsYunbNrGeKY-wikiwkvgHMNm1xvVt3B3Aq0vnTYoGhGU6iFlpCa4dpLF_f-fTVglZCOlIW-DEHPym2dG8kZmIa82M8-sqv9GySw4sM8D_60T1SK-hgA3kBxc9P9xX-LUPcqKhSZwDbYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از ایونت های شبانه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66359" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66357">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwlTelhEDKgVus_cpjurREHkQA300kGxqAt8WwGjBJp_nhsafjZ2-V5RAC4OV4onRG2Zp41jX8AOUo0y6dsipdHftNmRMXcfccOsxKXMMp4uIaG03OcaIeXS-zxkI7B4JitDR8qAgJ-EypOSDV3RDBeD5DCEoXNqAKIEfd6AvH_RQjrCIb1NSg1atF6G32yZ5e2VCRENWW31Mq0DuNepEcytg-j6BXQpOTOAKFkGrK9kAcZL6I0aLxA5FKBPaebRGvZMEtS6TcKLmDjnG7mRSTLrtCbSDnroRWyJTrrrbC4I9EdDLNFWeUKTMbb2wfQzfcT__DR8K3R9lAGAQ4A9pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145629d21c.mp4?token=jkd8LI05ONojyzBy_qOFZ1s8KEUgS7AP9yPDKW9q-x6ZRmjlLmwD25WsUs5qrBV7vCUwZCKIB3o3TP8yeX8_Eyj3x_O9ykw8nfccx6iAZBJljGb-nVlF69ueIQC9dX0qUfv4TGWTYf2yxrSfdBYAVpbaMgDLRKeiix-zsMmpjgtA-RMhYXLmuOGl-Ceiibf7PDtSibfKr9mQGZU8TdBoe2X2Tf0RaOlrwaqRL9l7yHWiV7GsmmJhVlwO_IvuDsKHwkGWZW2Hj6vfb5kYB04XEcAh9CX8_IYh8SIinXmXpU-5Pr2pQSg9hCqmiShb07AIqTcKVOeJMKQAp9TE9NAp0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145629d21c.mp4?token=jkd8LI05ONojyzBy_qOFZ1s8KEUgS7AP9yPDKW9q-x6ZRmjlLmwD25WsUs5qrBV7vCUwZCKIB3o3TP8yeX8_Eyj3x_O9ykw8nfccx6iAZBJljGb-nVlF69ueIQC9dX0qUfv4TGWTYf2yxrSfdBYAVpbaMgDLRKeiix-zsMmpjgtA-RMhYXLmuOGl-Ceiibf7PDtSibfKr9mQGZU8TdBoe2X2Tf0RaOlrwaqRL9l7yHWiV7GsmmJhVlwO_IvuDsKHwkGWZW2Hj6vfb5kYB04XEcAh9CX8_IYh8SIinXmXpU-5Pr2pQSg9hCqmiShb07AIqTcKVOeJMKQAp9TE9NAp0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جنگنده‌های اسرائیلی مناطقی در نزدیکی کفر تبنیت در جنوب لبنان را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66357" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66356">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=hN4OTLQO_VIJAs-ftnAdlYrs80FgoFAXZXzgSBjbcSq6jgLodFOPdc3MDbwzHd_SPlZyM_WCP7bCHWn88ylsbYb60PZVRAo1xJvalu35XFwgB_hEuUHx_KjR1J7pNBQ_kEittqk1Bal1OvVIIjAQtWp0sk7saAq8ei_y9M3lLf7kmTcbtncx1Aw5yoB_W2X8QktHU25ViZiZvAuA6W1tVfUdNRp2KaWuGspOCHZow6dV_ioR9qGQW-DsT_Ozh5gkrdUXUbshlyB2Qg0gdhhNjqUOeSwnF4c3b3O2qtVc7nu73Q7zCSSls6P6esjKGqvWtQauQmotKBsMxt0bfD6dSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=hN4OTLQO_VIJAs-ftnAdlYrs80FgoFAXZXzgSBjbcSq6jgLodFOPdc3MDbwzHd_SPlZyM_WCP7bCHWn88ylsbYb60PZVRAo1xJvalu35XFwgB_hEuUHx_KjR1J7pNBQ_kEittqk1Bal1OvVIIjAQtWp0sk7saAq8ei_y9M3lLf7kmTcbtncx1Aw5yoB_W2X8QktHU25ViZiZvAuA6W1tVfUdNRp2KaWuGspOCHZow6dV_ioR9qGQW-DsT_Ozh5gkrdUXUbshlyB2Qg0gdhhNjqUOeSwnF4c3b3O2qtVc7nu73Q7zCSSls6P6esjKGqvWtQauQmotKBsMxt0bfD6dSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
فراموش نکنید، هیچ‌کس تا این حد در مورد ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری دیگر از افراد انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66356" target="_blank">📅 15:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66355">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=FPmQdK5BwzqmGyGyo3X-J5EX7MgJ099odVGSdo2BAe8I-1ZniNV5S_EXxyBi9Ug9hlU0D56kT4EcKvYXiIRSNoTZyIv1bJgWGheirXiQIZ-TsDtx26IF-bIjh_9uKdVe-Wh6atD2Xrln_QBxqv0_Hf5mRARuMvBZ9xd4FPpfKS7xcgkbHbuMLn13yGSP4XIzV5MdvR33Q2I37VvIT7s4JN-m820d9qlXlpR7cdQUWFFsphP3oqs_dwFyMCUfn7sf9p8lUWtINoKDaKCgezwYvGi8jYyzFAvOje9wd-Q5_jjOWFlSH1USRdx7_V3LNLArgWNF8bOCzIWlGdbBzLs3KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=FPmQdK5BwzqmGyGyo3X-J5EX7MgJ099odVGSdo2BAe8I-1ZniNV5S_EXxyBi9Ug9hlU0D56kT4EcKvYXiIRSNoTZyIv1bJgWGheirXiQIZ-TsDtx26IF-bIjh_9uKdVe-Wh6atD2Xrln_QBxqv0_Hf5mRARuMvBZ9xd4FPpfKS7xcgkbHbuMLn13yGSP4XIzV5MdvR33Q2I37VvIT7s4JN-m820d9qlXlpR7cdQUWFFsphP3oqs_dwFyMCUfn7sf9p8lUWtINoKDaKCgezwYvGi8jYyzFAvOje9wd-Q5_jjOWFlSH1USRdx7_V3LNLArgWNF8bOCzIWlGdbBzLs3KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: نیروی دریایی آمریکا هر شب بین ۱۵ تا ۲۵ کشتی را متوقف می‌کرد
دلیل پایین ماندن قیمت نفت این است که ما هر شب کشتی‌هایی را که شما حتی از آن‌ها خبر نداشتید، خارج میکردیم. دو روز پیش، سه روز پیش و حتی یک ماه پیش، ما ۲۲ کشتی را خارج کردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی داشتیم و هیچ‌کس از این موضوع خبر نداشت. نیروی دریایی ما کار بزرگی انجام داد و به همین دلیل قیمت نفت به ۳۰۰ دلار در هر بشکه نرسید. قیمت‌ها به ۱۲۵ تا ۱۵۰ دلار رسید و اکنون حدود ۷۲ تا ۷۳ دلار است و حتی شنیده‌ام از این هم پایین‌تر آمده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66355" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66354">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=cYwwfUBYic-eGJtb1FkkMyoXLbtvIZfJHrsFYi1zBiePFMr4_lzyHDXHYSLXNWLM649hHoMrHx0WMGumkiCABlMVt1_HPwwehkNTqYyNrOLA-0RyCQ4PATXwrQ-yF3cxvWiWsOIEhooOSS5BXFj50eCcmMfFjiEg1W83bYcUjavqRngSeQ2YAXO3O3P8ik_Mt9U-s0m9ghQ95BuJwwiEa1l1Vjg1yEOuHoJeo3k71RPCQenzziJoUZ-4iO2gm-NjzyikB4tFqKJ_RUj2kOPXsC955kBulz2-GTBVUIrOWN2a0WQK8J8jwz0TALnbYWk0i1Mi9Gi4DSW7VVItSr0nzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=cYwwfUBYic-eGJtb1FkkMyoXLbtvIZfJHrsFYi1zBiePFMr4_lzyHDXHYSLXNWLM649hHoMrHx0WMGumkiCABlMVt1_HPwwehkNTqYyNrOLA-0RyCQ4PATXwrQ-yF3cxvWiWsOIEhooOSS5BXFj50eCcmMfFjiEg1W83bYcUjavqRngSeQ2YAXO3O3P8ik_Mt9U-s0m9ghQ95BuJwwiEa1l1Vjg1yEOuHoJeo3k71RPCQenzziJoUZ-4iO2gm-NjzyikB4tFqKJ_RUj2kOPXsC955kBulz2-GTBVUIrOWN2a0WQK8J8jwz0TALnbYWk0i1Mi9Gi4DSW7VVItSr0nzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: «می‌دانید ایرانی‌ها چه کار کردند؟ آن‌ها به اوباما خندیدند و به او گفتند احمقِ مادرجنده.»
پرزیدنت ترامپ با اشاره به نحوه برخورد رژیم جمهوری اسلامی با دولت باراک اوباما، گفت که مقامات این رژیم به اوباما خندیدند و او را «احمقِ مادرجنده» خطاب کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66354" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=LWcmWsK3j658FEh-IrOPpozuhF2fULosatmd6SqTTksL3BDJpYPDofDzJYeLG7CHW0MWJjjMWNXBSBb2UQNjmOE_YzZfREWBj4oRxeJm0NObZedGLZiDNfeoXZZSoIrdAp6gKHULStV9UB9hblfnoTdCoYqJnXivl7GpsDyIjcfa4tsZjmYhCBvQtb2oEteVG-fmyc5D1xQ0rNStmLitv4fO766dCfJP4FJU8-QYhpv78-R4LcaBDX6f0CBrnIl8M_P9Gv6JivpxyHk62T6_CP38LYIceDWOKkPgWuVCx1RorVxNlneU9oTCQr6k0EAKownxOpA5nztHoYrPfbYJFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=LWcmWsK3j658FEh-IrOPpozuhF2fULosatmd6SqTTksL3BDJpYPDofDzJYeLG7CHW0MWJjjMWNXBSBb2UQNjmOE_YzZfREWBj4oRxeJm0NObZedGLZiDNfeoXZZSoIrdAp6gKHULStV9UB9hblfnoTdCoYqJnXivl7GpsDyIjcfa4tsZjmYhCBvQtb2oEteVG-fmyc5D1xQ0rNStmLitv4fO766dCfJP4FJU8-QYhpv78-R4LcaBDX6f0CBrnIl8M_P9Gv6JivpxyHk62T6_CP38LYIceDWOKkPgWuVCx1RorVxNlneU9oTCQr6k0EAKownxOpA5nztHoYrPfbYJFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما مردی به نام سلیمانی را از بین بردیم. فکر می‌کنید اگر او زنده بود، این اتفاق می‌افتاد؟او یک نابغه شیطانی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66353" target="_blank">📅 14:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=v8-obsCy2F3Ax_XEKTPbmzT-bBehrQ0wPDkFwbF1ZCw3APGbO4jzeQu1jWuBI1oatcrqA1tBjhjujEWK593Sh40SfsZcSzboQV4yHJ53b4H_9ARUJOukTIX1NB6J7WMcFYglrjQpWyYnFm3dm3KyWCJ9ucYiR_zArF5MG5SaoG-XdvMC9DdupgczId0hyGCIj4CH4l8NrapbsQ4VEOQmNLWiYFeiwG4UiRjmphsIURSWP3dnk64aQ0mvU7FvfC1tzPnLxDI2R2mEtErpb3CSs_QzR5Hoq9es3gbHsT9dVQNPbjwZkFeOhLswCltH9hexc6MxeJEw5Qe4Aw8DGgG7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=v8-obsCy2F3Ax_XEKTPbmzT-bBehrQ0wPDkFwbF1ZCw3APGbO4jzeQu1jWuBI1oatcrqA1tBjhjujEWK593Sh40SfsZcSzboQV4yHJ53b4H_9ARUJOukTIX1NB6J7WMcFYglrjQpWyYnFm3dm3KyWCJ9ucYiR_zArF5MG5SaoG-XdvMC9DdupgczId0hyGCIj4CH4l8NrapbsQ4VEOQmNLWiYFeiwG4UiRjmphsIURSWP3dnk64aQ0mvU7FvfC1tzPnLxDI2R2mEtErpb3CSs_QzR5Hoq9es3gbHsT9dVQNPbjwZkFeOhLswCltH9hexc6MxeJEw5Qe4Aw8DGgG7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: بازار از توافق با رژیم جمهوری اسلامی خوشحال است
«چه کسی واقعاً خوشحال است؟ بازار... بازار در حال نوسان است و قیمت نفت سقوط کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66352" target="_blank">📅 14:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66351">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=AS-ePiuLONqoSqh8awGXjpe7MYxjgJA5aP5yLL7O9Otuyota-s_BrgVeBsIdtgQmCJ_8nPKmhqEnl28F45VEB6AWbIMh698ZOLG6Z9klLHX6RObUM9SUvywlxTyC6lKMemU-_PQpxzJhjQQiNoVAE9BFnXlj9ShZlwsyDVVOCGflypePiEqyashPTYILSP6h1DVIV7sCYARUld6iAAaMNLFhOU5Q50ht3-_aPxwqrPgmD0xvzxOTjqKzHGdqurFZWaNTrD3lgl6gocRwuusfkKgXOaFh21CTDQ9GCBv1Uwye7udGNpUJKwQ5WxpK2vUzCYEe9bj7bQKqo8pmo40hdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=AS-ePiuLONqoSqh8awGXjpe7MYxjgJA5aP5yLL7O9Otuyota-s_BrgVeBsIdtgQmCJ_8nPKmhqEnl28F45VEB6AWbIMh698ZOLG6Z9klLHX6RObUM9SUvywlxTyC6lKMemU-_PQpxzJhjQQiNoVAE9BFnXlj9ShZlwsyDVVOCGflypePiEqyashPTYILSP6h1DVIV7sCYARUld6iAAaMNLFhOU5Q50ht3-_aPxwqrPgmD0xvzxOTjqKzHGdqurFZWaNTrD3lgl6gocRwuusfkKgXOaFh21CTDQ9GCBv1Uwye7udGNpUJKwQ5WxpK2vUzCYEe9bj7bQKqo8pmo40hdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:متن نهایی نیست؛ این یک یادداشت تفاهم است.
اگر من آن را دوست نداشته باشم، ما به پرتاب بمب روی سرشان برمی‌گردیم.اگر آنها رفتار مناسبی نداشته باشند، ما دوباره به پرتاب بمب برمی‌گردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66351" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66350">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=FP5Q2gGAkwmmCJ87ziU3rozsgEf6ev97DHXdgB3Tvh0unCbQwLSaOjUqU8F5QUmjuQ2GSMUD8CvxaFvqYNUaqPcxy1ygOCddyJRMGGdZe_LkElC7V2GZJfDj0N-GzEg9VG9jf3PVxmAzA3EWIpXxFFaISiOXK_jh-G8UX--brr0QBW-4C5h2brlRwNsabDXM8V8IctqOOfm0CEHxkq5egzFWLmtAkDIJA5IQX8kmSb9oKvcCfktunOjQh39JxaGgxKr-iPGxtF1f-frlJ0WGua9NrxGQ6AJKW0uyFYyeMU4wqw_iYAHQCNIrQKg1AiJCwkzlnPBWhTP4fbm3w7DNpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=FP5Q2gGAkwmmCJ87ziU3rozsgEf6ev97DHXdgB3Tvh0unCbQwLSaOjUqU8F5QUmjuQ2GSMUD8CvxaFvqYNUaqPcxy1ygOCddyJRMGGdZe_LkElC7V2GZJfDj0N-GzEg9VG9jf3PVxmAzA3EWIpXxFFaISiOXK_jh-G8UX--brr0QBW-4C5h2brlRwNsabDXM8V8IctqOOfm0CEHxkq5egzFWLmtAkDIJA5IQX8kmSb9oKvcCfktunOjQh39JxaGgxKr-iPGxtF1f-frlJ0WGua9NrxGQ6AJKW0uyFYyeMU4wqw_iYAHQCNIrQKg1AiJCwkzlnPBWhTP4fbm3w7DNpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:
هیچ‌کس نمی‌داند این چیست، اما توافق بسیار قوی‌ای است.
به نظر می‌رسد اکثر مردم بسیار خوشحال هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66350" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66349">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=pRFEJtaIGALtF6Wz9khqxU9yJf3RQtmgn_uG4__iFIKm4gdzXkDk2G_WRAPucqGckYsPlDjHFpBiFzRnyMHMy8-imXP2HCRjrxLTHk8_ybkW8s2Hy_3_es8c7JIS46px1ltPr2kO6QJuI_JKOlikNfTptDb1F5Y6QZDRgd93TuKWCEjcBtnHtgnShur6TXCtc_Ju6FPsQaGJjoy-HUAcLw3JscYdsdoFqNz718EHfXFtCbD-1_okDiy5UW7c1nBkhgCPF72kVk6ppte36d0Y-KrtO4QKiSncsXHEWz7sXY9r7BKDkn4qM8VWSTxe9i2wTxmCnta601oM8tRnI1bwTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=pRFEJtaIGALtF6Wz9khqxU9yJf3RQtmgn_uG4__iFIKm4gdzXkDk2G_WRAPucqGckYsPlDjHFpBiFzRnyMHMy8-imXP2HCRjrxLTHk8_ybkW8s2Hy_3_es8c7JIS46px1ltPr2kO6QJuI_JKOlikNfTptDb1F5Y6QZDRgd93TuKWCEjcBtnHtgnShur6TXCtc_Ju6FPsQaGJjoy-HUAcLw3JscYdsdoFqNz718EHfXFtCbD-1_okDiy5UW7c1nBkhgCPF72kVk6ppte36d0Y-KrtO4QKiSncsXHEWz7sXY9r7BKDkn4qM8VWSTxe9i2wTxmCnta601oM8tRnI1bwTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یسرائیل کاتز: هر کسی علیه اسرائیل اقدام کند، بهای سنگینی خواهد پرداخت
🔴
وزیر جنگ اسرائیل هشدار داد: «هر کسی که علیه دولت اسرائیل انگشت و دست بلند کند، چه در غزه، چه در لبنان، چه در سوریه و یا هر نقطه دیگری، می‌داند که باید بهای آن را بپردازد. اول از همه، آنها زمین خود را از دست می‌دهند و خانه‌های خود را از دست می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66349" target="_blank">📅 14:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66348">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831548d977.mp4?token=vNDvFR9J8R_JZo7onXh8IDri8FrlOyYkFySxlpNb84BAxq4wYv4rN8CwoI3d0sW78vqNzbW_XatMMmhyz2wYKlmAzmc2M-whjHHIO1EwoXpArxtw6FPddclb1xSd9cKHyKwTluI9mW1lvKKrkVERWKmhUcz1ZJy6CjHG5YOS2tICzA6ATTqvda9bvBPvhl7JimAJR2l_AeL8dTJWN8DMMJopXjm0FFDbmheEt5gBqs_-yRyM6fUyOIhaLr_juvanQvO41LsWPUfew9P_Y4BrzIUj1Zmccd1bqKoO7jnMWiQDk345_tFkIr5rmnlRhNlNILcqkxQ8ewnLQGQpY8qyGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831548d977.mp4?token=vNDvFR9J8R_JZo7onXh8IDri8FrlOyYkFySxlpNb84BAxq4wYv4rN8CwoI3d0sW78vqNzbW_XatMMmhyz2wYKlmAzmc2M-whjHHIO1EwoXpArxtw6FPddclb1xSd9cKHyKwTluI9mW1lvKKrkVERWKmhUcz1ZJy6CjHG5YOS2tICzA6ATTqvda9bvBPvhl7JimAJR2l_AeL8dTJWN8DMMJopXjm0FFDbmheEt5gBqs_-yRyM6fUyOIhaLr_juvanQvO41LsWPUfew9P_Y4BrzIUj1Zmccd1bqKoO7jnMWiQDk345_tFkIr5rmnlRhNlNILcqkxQ8ewnLQGQpY8qyGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس و دیسبک بازی مسعود با خودش
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66348" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66347">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=U89RpMSOSGGdLKg2RKBfiEdDe764Yoxbo9G7D3Py2MF5TQZMOQofgUrCisOUPP0prUnqlXQt0wVt39VCvMcn3shKXlqlBiXGNWYLyozXK8KJFrW8pUltK9CmioquuX-BupnvA1uvIvcG0ePBu08XScRJ_Rz2sQFaZM9BZCrXtbXGgb3MvnFbMWe5RoIcFC0aSklPEZm3bODgigC0hCa8Hzk-4X3Ioik6f4M1R4PMThMQwuNOpto6GXr3NmpER-qOxm-5GH_auFgM3B7Da0QKjLvzCauXRP7Neul9bNDlBDDSJMMSch9h0fLMEZZ9iJe5Itg1lAiAE65g9i69Syq5RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=U89RpMSOSGGdLKg2RKBfiEdDe764Yoxbo9G7D3Py2MF5TQZMOQofgUrCisOUPP0prUnqlXQt0wVt39VCvMcn3shKXlqlBiXGNWYLyozXK8KJFrW8pUltK9CmioquuX-BupnvA1uvIvcG0ePBu08XScRJ_Rz2sQFaZM9BZCrXtbXGgb3MvnFbMWe5RoIcFC0aSklPEZm3bODgigC0hCa8Hzk-4X3Ioik6f4M1R4PMThMQwuNOpto6GXr3NmpER-qOxm-5GH_auFgM3B7Da0QKjLvzCauXRP7Neul9bNDlBDDSJMMSch9h0fLMEZZ9iJe5Itg1lAiAE65g9i69Syq5RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاوره اخذ مدارک دانشگاه آزاد
واحدهای معتبر تهران
کارشناسی، کارشناسی ارشد، دکترا
با استعلام
💥
(
بدون پیش پرداخت
)
💥
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@irantahsilat_iau
Instagram :
👇
👇
👇
👇
Https://instagram.com/uni.irantahsilat
جهت ارتباط با ادمین
👇
:
@madrakuni</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66347" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66346">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1725e10790.mp4?token=h4EPold-2gzmHn6yyaqOQqlYR33oAVM9b6-5Y-awTNaSkbFIt2kkCs-NSrXb_ujhSfWxvP0cDZ8ceu2IYcmEvjXboBV7zxtpL0CNV8z54EH-6tMJ0QxXphnBCy-pSOdvfOuebc5KPxl-1x820_kGjeFfFFg_2s_NHPi6TCfrDwzOWd9MsD7KkmAdWSWI4jgkqip6VXwRf9rTk-oUDDTOx3R7POf_vzbrs6VD4dEuCl7Waslsm5JLPgZ26nX18j2LS7GlkOhg15j61_IFZPfOuCIg5EPNa06Y-RJWw9UciPYX4RMw5CtVk4GP1iOtMm-aeXM39ALGOg7OzZIb_p1wJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1725e10790.mp4?token=h4EPold-2gzmHn6yyaqOQqlYR33oAVM9b6-5Y-awTNaSkbFIt2kkCs-NSrXb_ujhSfWxvP0cDZ8ceu2IYcmEvjXboBV7zxtpL0CNV8z54EH-6tMJ0QxXphnBCy-pSOdvfOuebc5KPxl-1x820_kGjeFfFFg_2s_NHPi6TCfrDwzOWd9MsD7KkmAdWSWI4jgkqip6VXwRf9rTk-oUDDTOx3R7POf_vzbrs6VD4dEuCl7Waslsm5JLPgZ26nX18j2LS7GlkOhg15j61_IFZPfOuCIg5EPNa06Y-RJWw9UciPYX4RMw5CtVk4GP1iOtMm-aeXM39ALGOg7OzZIb_p1wJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
بالگرد کاموف ۵۲ روسیه برای رهگیری پهپاد انتحاری اوکراین بر فراز مسکو به پرواز درآمد:
در جریان موج حملات پهپادی صبح امروز اوکراین به سمت مسکو، یک بالگرد تهاجمی کاموف ۵۲ روسیه تلاش کرد یک پهپاد انتحاری اوکراینی را در آسمان رهگیری و منهدم کند. این تصاویر بار دیگر نشان می‌دهد که جنگ پهپادها تا قلب پایتخت روسیه کشیده شده و مسکو بیش از گذشته برای مقابله با تهدیدهای هوایی به ابزارهای غیرمتعارف و واحدهای هوانیروز متکی شده است. حملات پهپادی اوکراین در ماه‌های اخیر به زیرساخت‌ها و مناطق اطراف مسکو شدت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66346" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66345">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCMjvj3iIvjqQzrkNrw4B1E6c2DBlh7BC5d2r6ecMh90xfPNselNUjkug7pIhLjNngzGP98gRCEaWIfZQUywH891w3LREtbc7M9CQJqDKMcNbhzU3JmrJFXe88YB5_SLcnNk56RZIrMn_Dj-tbogA3Q5u6clJgvH3OToQ3izUEEEVk7yFkUO36bhVyhcrHHzepHNRXC80O8A-ZMFm0DA8xQfNaRwkYaNApzbLAMn_3wVbVGyVvJEngKq4qrERbd90Isdujwk9nG88SID3Vnd333lsI_H5iSLzpdUJHL8tTzbyQVmqjV3TO27oMHK2bKABviN96iaF1JIa_db5_dikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مارکو روبیو بعد از شنیدن خبر توافق
😔
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66345" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66344">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66344" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66344" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66343">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkUCORPaccG3g5H2kfaYYwPVOF23YfmjBuGkzKV-v0wGn6_iegnqRHgbgiFVTRu2S-tOKX0N_h5Pv7zTA7VDCU1yyC_3EB7aRt_aa0UO5PdB-MhUDAi-AjEZ_u9wAqxUBrYZtm2Ad4xIxVfT4r8aq5Hngibmlg19gOKw9hCzpH5P9qr_wtuRItt-b6HdgIeRw8aGqA8De5v7tomuH7rs9A8jixQ7l_W5l465AAR881n_a3pXhmbU5oIS4N7ajBr9RMWE3YdZ4TWCsiUeunBPI_L229nN9VloTdetPLJccjsQUC2c6Hq_vqlq_pH7RQR_UnqOGegh6VRhl1FaXvrrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66343" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
