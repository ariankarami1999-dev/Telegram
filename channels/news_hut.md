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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 03:39:11</div>
<hr>

<div class="tg-post" id="msg-66460">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/news_hut/66460" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66459">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQyHMgKs7t0zIr58Ye0dJhONHaMPQJgbNJhpJQX-zPiPooZxGyR63EVKlNk7Td9pmumd_sXWY-KQZCc2gjg9_YD2g1och1f-EUNsXpsci7EjpfOx4UNTXRxZ79ZAFM4SXjEVXL46b2KesAlnsnQvUssuB6uaJMtbKeokEBREQ1N1aMJxFkUQ5uXNf2cdsaoc0cZFZ1-2_7OJJ3UzrgTxTt1lNsn-a2QCV3ma9EzDHVraAUVTOjOFLej7SDndfxf0EGXSX-BcHfqpcjR-FaevaUw8Y0W529aGL8mBpDVQXCLmHpLMcKeCYqPfQwYjuQwfoPOcBCvXLD26NwduRwFsAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/news_hut/66459" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66458">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
‏به گزارش المیادین، هیات مذاکره‌کننده جمهوری اسلامی در پی تداوم حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس را تعلیق کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/66458" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66457">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=I-27YFr5Dz-bFc-M1diPoqJ4r9Mm8xUM7F0OuhWFKLhuMmrQpZBuSYc_h3mzdB1E5KhCWgRAOXDZy4iATWgdc7IF__f8b3iiABi5GixZHIgYmN-DUBjxU2xPICzULlsgs-753J6KugoeyzbGFxCzL6zaV4zrQ4mYyqQxkTFZYkWNMF3GTakaOmAUUhDjlZPV9AX1xfUHYIqZ_9gbqY5xptawt3YyZ18gxAEC_7z-TPDAXnCpeVNL7doV7-X9ct0D5SH3jERuiSiGGZwU8ExaDTliJfsvo7yWPGVmT3a9MR9dxoPVroidQL8SOWLZ56Tl-MQa6-cOyEYvrxWnpw_mBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=I-27YFr5Dz-bFc-M1diPoqJ4r9Mm8xUM7F0OuhWFKLhuMmrQpZBuSYc_h3mzdB1E5KhCWgRAOXDZy4iATWgdc7IF__f8b3iiABi5GixZHIgYmN-DUBjxU2xPICzULlsgs-753J6KugoeyzbGFxCzL6zaV4zrQ4mYyqQxkTFZYkWNMF3GTakaOmAUUhDjlZPV9AX1xfUHYIqZ_9gbqY5xptawt3YyZ18gxAEC_7z-TPDAXnCpeVNL7doV7-X9ct0D5SH3jERuiSiGGZwU8ExaDTliJfsvo7yWPGVmT3a9MR9dxoPVroidQL8SOWLZ56Tl-MQa6-cOyEYvrxWnpw_mBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آیا در جامعه اسرائیل افرادی هستند که بخواهند ایران را به لیبی تبدیل کنند، یعنی یک دولت شکست‌خورده با ۹۰ میلیون جمعیت؟ احتمالا بله.
اما نمی‌دانم که بی‌بی (نتانیاهو) چنین چیزی بخواهد.
من شخصا هیچ‌وقت چنین گفت‌وگویی با او نداشته‌ام. گفت‌وگوی جالبی هم می‌تواند باشد.
اما همین را الان می‌گویم: آیا تبدیل شدن ایران به یک «لیبی ایرانی» برای ایالات متحده آمریکا خوب است؟ قطعا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/66457" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66456">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=mZaG-04wNdO_m41zokPHQnqO3qY-fyYdzMHJhGEVQCS9J2ir7Dp4yGNt_AhxvX2rKdnyYJ7PZ-EKqYI2rxeka4IbYlmSxo8NbgPdutGz0B3uXkiwicj2dOTaQfGLP0ey6qS0yC1slRcRBiEJcfv11Qdi47z1pqi1AJ8s2yszM30irmwtGxAu-6_eIMIMKtXd8bixM08ruwpZUMbR8Jo1XFXbtGmbL8ZjA7RnKbrYbYiG7VCR4SyuePY21yndpAZLhWM-njNzmywKCDObuioiJMYUqEJr6LL-AaP1H-VuqSnkZ_b8g4JlERk5nlG_CZRm_TpfwnnLNMINDxk7HzCNUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=mZaG-04wNdO_m41zokPHQnqO3qY-fyYdzMHJhGEVQCS9J2ir7Dp4yGNt_AhxvX2rKdnyYJ7PZ-EKqYI2rxeka4IbYlmSxo8NbgPdutGz0B3uXkiwicj2dOTaQfGLP0ey6qS0yC1slRcRBiEJcfv11Qdi47z1pqi1AJ8s2yszM30irmwtGxAu-6_eIMIMKtXd8bixM08ruwpZUMbR8Jo1XFXbtGmbL8ZjA7RnKbrYbYiG7VCR4SyuePY21yndpAZLhWM-njNzmywKCDObuioiJMYUqEJr6LL-AaP1H-VuqSnkZ_b8g4JlERk5nlG_CZRm_TpfwnnLNMINDxk7HzCNUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس این انتقام ما چیشد؟
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/66456" target="_blank">📅 23:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66455">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66455" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66453">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
یسرائیل کاتز به کانال ۱۴:
ارتش اسرائیل دستورهایی دریافت کرده است تا در صورت لزوم، برای عملیات دیگری در ایران آماده شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66453" target="_blank">📅 22:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66452">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTVlotVuiXNnxDVvblT8Z3lNDwxnuRR8YoKA1pVLu-80osZ58mkvU8KOnXECqg_lEPTdgLqM8Hho38fyIXRYL5FubKwALcAK__IAKW3ovztCyTkeNBqEFSkxhmNJsFLHCpLX0VxlZyr7SSmTKz079_nq1VYfwIxLN37Q4i5O9KHncIbr3dvIglo0hI9PjZOUge4m48BogmZXEuVIleGoLBQBy5kJsa7Vwooqze713Sl8nssycvZuOIGsjLid7fBW7IOe6oRxvdT6pPlkpuVeCIOPx9GcwKiSkZK8zXsVLOdVrTozYb6KpM4P0lGqkqUptSXrLeMnTY5y4XrQ26abjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در تروث سوشال:
ایالات متحده به صلح متعهد است و ما همه را در منطقه خاورمیانه تشویق می‌کنیم که به تعهد خود برای پیشبرد مذاکرات ما به زیبایی پایبند باشند. بازارها از آنچه که با کاهش قیمت نفت و افزایش سهام اتفاق می‌افتد، لذت می‌برند. ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم. از توجه شما به این موضوع متشکریم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66452" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66451">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66451" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66450">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66450" target="_blank">📅 21:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66449">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این پیام یعنی پایان پزشکیان و جریان اصلاح‌طلب در ایران، و آغاز حکومت نظامیان به سردستگی قالیباف #hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66449" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66448">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66448" target="_blank">📅 21:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66447">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuWa03tufeLY4c9mcM414FJCFRa0P-Kgn3BTe9xlOEYx_bt30NA_24JZOB3KbXw6UbMU4ekof065U39rhwUDvQwwiddNiz8uxL4h72rrCKt3yyqtDqE7AqhlxgQWHPfsav4qVzGEztnWhKI5UsNDaRG1963xABLdWEZVPZjgS6O8FlEpyLYwg6i-Uroc1VkXjpobFTZxZJkSMYHxfmFF8Ca9n9geQHuibSv_CBnGKTgh6bsyVW34KE7ZIGZaLvrHKyxHfheUZtKOVA_Ol6thNqxnQWcoRcXfh83Y1Augh6FrA3ksEq-H4lEiP2RfH7Y21DLKt7w5MS8LaEhulPBXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66447" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66446">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsAbBQ4B0aVXX27SRjTVZ2IacBEkz_DEFJcV5Q5MwMAN2BF7wBCJodnesaqCeuLcK8XlcBk5vS3NTahQPbLVO_cc90LJJaE0xmYo9hvWuVuHenS2qk61GNSuamGJP2RiM1gGeIwHGLNl8hI5R_1uKKDlnUYSOut8YIRF_UQSj1nhh_LzxLTsULpQQrRb3RbNf2VHGLOa4h9EuVks2iGTRWcAV1ljlyrwsC7XOz3W0U8jTZYyCU6zs_W0lvMsQBqI9BVwnT9GlDifCQA8bQD-CKSE5blbQlYiZ4yso3Y91zrcP7_i7fkNO5NSr5ezxv-IW9ecTRPJ4M8r-aGLCBTeEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: آمریکا هیچ پولی به ایران نمی‌دهد. اخبار پرداخت 300 میلیارد دلار به ایران فیک است. تمام آنچه برای آمریکا وجود دارد، موفقیت، کاهش قیمت نفت و پیروزی است. وضعیت بازار سهام را بررسی کنید. پروپاگاندای دموکرات‌ها در کار است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66446" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66445">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏
🚨
🚨
🚨
⭕️
سنتکام اعلام کرد، نیروهای آمریکایی محاصره اعمال‌شده بر تمامی ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کرده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66445" target="_blank">📅 20:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66444">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66444" target="_blank">📅 20:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66443">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66443" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66442">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66442" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66441">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66441" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66440">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66440" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66439">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyih2pb5HXOREaTD8ppws1iqwzHPdZ1XKjxWI8hvlyhDgSiEk2Qutb56UKEQ3ppO3A62-7uYin4ckuN6TyyBrBs9XN7DWi_ZOngT50OJbnq1fgr435P4A4k9AJAFVBZHZLvZuRPNgWsWSR28bYrtldTCuZizhzuSfl3YQnoJ_Yhfxf0k3J-eO-J2fMXVmZoYlIx98KtlHF14p96pecsJnyloKQRwV9pHts0skrxOzXvX_jr1atMC8qj-pDl12GjARvu4ekIgHCjLiLHeviQ8oTNJAeJg_EbIc3kMtiukWNsNZO9G2erh7Y-xtcporgM2zWgSOXWf0J80Sz9c49Hjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
فایننشال تایمز :
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌های بلوکه‌شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66439" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66438">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9W5BJcyiMm7ew4-HP7Qjb2AiRKZrQrhBlQSV9UglTYXh9mQFp9URRUYiODNdOwTM1uqmFFLmKDf9uqFxoWZUYO1IM5lBhjbUKEFwazu96t2-ZeAh9jrGA9TJdOdwEyaAAd-W-9I_m31RLHxDS7HFldDRknjtemfSkPSBQj9i8P6QesjXd0Y2-W_jPDrQu0Pn-MYJAr0aHzdQbsc2k8LA1a2ZsNuVTh_7XDCwgAHGZKpy4dpP8TNIGGD6Pw1S3Lq8a8eaZjnlYnSGl9H4A18Q7AEcasCoaJLVSk686lbbu7_FudQGuwn5VSWi1_SJnFCgme-1QG5F_KVQe2u4GkiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ونس: کجا می روی دونالد! «امام مجتبی» منتظر توست!
دونالد: از روی امام شرم دارم ونس! شرم! توان دیدن جراحات ایشان را ندارم!
ونس: تو هر کار توانستی کردی! تصمیم امام اصلح است بر ما!
دونالد:‌ چه کنم! چه کنم ونس! با این جماعت هزار رنگ٬ که دروغ را چون «رج قالی» میبافند! امام مان تنهای تنهاست! شرم بر من ونس! شرم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66438" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66437">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=len8KxEa1rTpNfGFsZ40jtly8iMHEoEaNpha31FJmNqzsMWOl9u5xWjgV_jiUvAgPYiPUaxD82md4mDmIpR13R0YwzXjwh7_JwfmDbxHazMMAcXSv2LufdQuLbcAUVJKUKRltrvPzKgGVJ6ptl0Sx_ObaGP6r6N2LELR7V668pxdoIlNfdLCPKP3Ih276CPQ-jbJCSmwrgvu4XBppnbBB8XxOqXn-dQd0TDH0hPJEAaHxIQcR3GxzMeFAMJSe26g_C5CQ4kYEX3_2QYXRm2KpA7cU8OKJuZc3bI-deUZXCI0YkHi5sLN0XYBgG4B4ZvLUuM77ItXHVkgCWubXr66Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=len8KxEa1rTpNfGFsZ40jtly8iMHEoEaNpha31FJmNqzsMWOl9u5xWjgV_jiUvAgPYiPUaxD82md4mDmIpR13R0YwzXjwh7_JwfmDbxHazMMAcXSv2LufdQuLbcAUVJKUKRltrvPzKgGVJ6ptl0Sx_ObaGP6r6N2LELR7V668pxdoIlNfdLCPKP3Ih276CPQ-jbJCSmwrgvu4XBppnbBB8XxOqXn-dQd0TDH0hPJEAaHxIQcR3GxzMeFAMJSe26g_C5CQ4kYEX3_2QYXRm2KpA7cU8OKJuZc3bI-deUZXCI0YkHi5sLN0XYBgG4B4ZvLUuM77ItXHVkgCWubXr66Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار:یه مرد دانا سال 2020گفت ایران هیچ جنگی رو نبرده اما در هیچ مذاکره ای هم شکست نخورده
ترامپ:کی اینو گفته؟
خبرنگار:دونالد ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66437" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66436">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfZSaK00HcDi6Sw8qCbfQF5zcVJbSFRLGBqW0xjrL3H3k1CZ03_6TMl3JZKApTnWuf2OTSMNYALgp9tfvKT1bIaVcRhhYPJkozVXErUDPzEbDDeS9TohZx6hQ73GkCf7m5akv-B2TyWpYpRvW1ww65XyBk2s8qUL04MBUXWbM_Ah4DpcAEv_ztLu6RkmmL3nYJ5nPoX9DG_xTPxy2rgiGREAxl8IHaIf-XcriDXwZaNlIKHRFTgl67C2n_tCllPiiTuA2fVoYX_c0jzVDpFQ-qj-FUzM61AEGivjoPfnNwJ6PD1c9TcVbSoBgVeyIUUJJyh8NpRrIp4Agv0b-xnQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
الجزیره به نقل از تلویزیون پاکستان:
سفر برنامه ریزی شده شهباز شریف به سوییس بدون ذکر دلیل لغو شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66436" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66435">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm9yJ7fUtfNwORohSXGOJ3DfRx-c2HcVLTC70Ug0OHYYEX2jTICat6l-htr53daWgcsSqyJQ5v7bWM8Q9J_dEdJDPhpi3Zl39bxz1T4B7IotWMzBGT-3fBTp8AgZtUICg3dF31UO3C2OUldNyLy5jrIBU5vxSWFZN6qtlTMhFgDUSI-sBeUpTSubUZk9jh53TRKyQGOfvVlERg4yGP__w-saUNwRodwYlW19eaUKymgJSFgU2ByszyRfa_bLbOva62orXQ875MuDMXSP4tE9ZgMv-qJ-M4zsyzD6DGH94YNgdDyQjiGRw57p8FzWnIigFfy0lvV8raUWy3xLanaTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
نفت جریان دارد، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (قابلیت خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. «خواهش می‌کنم!» رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66435" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66432">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SR3nY-SZBogUrnp0qmhudTfxbU3MTWu6-1yPgAGZCIaGZGuCbz70aW0yWnMf2f45klVB3CWRIEhaTWINB_V-rUL_VhMP6ZU5M8YU_pvq_kJRLzxsGDSQ6Mnp84A7lNbKAnp9S6p6MZGe-k0T_wLsZ-8HJx3lyc_UORe1LF8QRb0d88cIt3B1G8oMPHBD9Jqz_2J2A1SAFlWmkA-sjeNSmClpezeYnQbvjvmYKf1CPsY3egldWGPu1-D2eqVEKzb8HRheNFt4-ZS--Y-Uexz7bXDQ9ty9uh5n1mm0uIVqMjcX4JxKcnhsH1-wznoRHMnyv4Kmg9q1qx8Mb9Fiv5apqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mpy5lw7UdiS3Ytv_erCydNIMwxbcc9wKVqnZnuWbyn6jtgkEKKrvETP0yz60MEa5NvkOabJNJ2Br61lvEqYg92ISUtN6xPFsRAACTgCKt0f9HwycnDC5Lmtb9BH92SqcY85iI0VogYsNFrRuZ85GcbRnQkfxU6-jRaCJOak8JezdeyUyAS8wPWjd_kOz2x0fXk_wIAjzqjK4GXCYK20AtaIZ_HCUifw33c4cVQ3TVEeI7xJOVnyVLPegVYeUtYPU0teT5qswB9Sr15O1fS06N3CZ6eMy1obOdAeZjg7KwumCntJaWgaL-kZ15dZlW04XlD7KbikMKZ8c7krxDxx-UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=RRp68CQ70HbVkpp0dPerrSosTv_qth2E4fzeiXOD-NvtE37X3XmTuK1N8oTspKV_JQAsr7vq9Er0F_CtFNjYaYHYRjob-PX1YLS3HxzSymo1pnUn1XdyM39APd1-u1xf7zEJLYHL1326SqwJcaaXvkKkR9mwAnsvszW4kSMkoyWrx-Pt30p27kAaEyCXu2jxnqrmNPWTHiWwtG-3mV9YWxXP20Y1U87KoxCEHvtWGCDX9_YAzPit5ABiZ_9qclwXFVHurjvMLGjISJlQ_o-Z1mrDJ89Z7xzXjFLvmM3wdVNmgNcI-92GP4GO64-jhcbEZivk_himYBdgVRWEYMSH3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=RRp68CQ70HbVkpp0dPerrSosTv_qth2E4fzeiXOD-NvtE37X3XmTuK1N8oTspKV_JQAsr7vq9Er0F_CtFNjYaYHYRjob-PX1YLS3HxzSymo1pnUn1XdyM39APd1-u1xf7zEJLYHL1326SqwJcaaXvkKkR9mwAnsvszW4kSMkoyWrx-Pt30p27kAaEyCXu2jxnqrmNPWTHiWwtG-3mV9YWxXP20Y1U87KoxCEHvtWGCDX9_YAzPit5ABiZ_9qclwXFVHurjvMLGjISJlQ_o-Z1mrDJ89Z7xzXjFLvmM3wdVNmgNcI-92GP4GO64-jhcbEZivk_himYBdgVRWEYMSH3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پختو پز اوکراین در مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66432" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66431">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=bkEmyNiBKHxLvGB2qtKJlukZm6Qd7JYvR_w_wQ6ZuMt_8cGwGk5BofnUfKsdoLBPClc0RqJvi_kA2gEq899Nk5-uKovnfpM3B0f8kW4lv6h0joefMvWo3uB029XxuxJYL1EuOq3yK63bF7T6ShxFStVx_TH9NbzQ6OQcJDb9gD-6dgA3VurB-XPxdNr0dTl0e0q5ZdY26hLOr0nOCRfz4H4GoTZ_TKlji77y3w0OgT0HdMWJ9FLKg8Q9tYrBElDXW18PgVGbFB05MLYxSG3_tV7hCzJqVH7z-iUPmccbcI8lTtL1IQPl-0436wiAbduVHFVn9FCgDJZbT9gu9AeDdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=bkEmyNiBKHxLvGB2qtKJlukZm6Qd7JYvR_w_wQ6ZuMt_8cGwGk5BofnUfKsdoLBPClc0RqJvi_kA2gEq899Nk5-uKovnfpM3B0f8kW4lv6h0joefMvWo3uB029XxuxJYL1EuOq3yK63bF7T6ShxFStVx_TH9NbzQ6OQcJDb9gD-6dgA3VurB-XPxdNr0dTl0e0q5ZdY26hLOr0nOCRfz4H4GoTZ_TKlji77y3w0OgT0HdMWJ9FLKg8Q9tYrBElDXW18PgVGbFB05MLYxSG3_tV7hCzJqVH7z-iUPmccbcI8lTtL1IQPl-0436wiAbduVHFVn9FCgDJZbT9gu9AeDdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد کشتی ها در تنگه هرمز پس از امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66431" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66430">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5FvI0wzOJhuQKGSUnCqAFq5vFpx3jaQl-26yJhnXWjMwE8V4MgJ2w6oM_YeJHOUOWvXbOSVGHcVXgfQVkgteUls4f7n1FMC_2UeIMPwN2m2fkTaqyBm8KhJnX3SaBgVgYG3qeJWELWjLGwlmt8B-3inyczSeQdEUbQ7wL8PzHKE6oHYdE4x7-pyoS6kyGI13kuErZhIyY1ZecY0rmAvBKa9rWYQgs3zsU8SjIqjRMjaaqheYJMxFMsMtAH-WeBdE4E9aYQrw4-RF9Ft5fgwKXItu0ymfnfSNRt35vi2vcwTgqjrzQIYerxMG842rRybN4pyHVcWJRVyVg-KbtXTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارتش اسرائیل؛منطقه امنیتی فوری در جنوب لبنان:
نقشه منطقه‌ای که نیروهای دفاعی اسرائیل در جنوب لبنان در آن فعالیت می‌کنند
بر اساس نیازهای عملیاتی، نیروهای دفاعی اسرائیل در منطقه امنیتی واقع در حدود 10 کیلومتری داخل خاک لبنان مستقر شده‌اند.
نیروهای ارتش اسرائیل در منطقه عملیاتی جنوب لبنان مستقر شده‌اند و به تلاش برای از بین بردن تهدیدها و بهبود دفاع از جمعیت شمالی ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66430" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66429">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcaCCrc-u4Rz88NcZQmRMf4Ow4EIoalSoGXKJH89hl07KaGnPb4DBHcp5vYZrJWQR73XUKFKjw-2Ix_7f233e0Ukr3RxTfoZZxgSzIvsvagkdCCSfeqSdj9YapHBU6vNBVEpurxYHVyJILVZgp6QJ8gd0zI7eFmwWqVobrJVuNi9hwASshidaqPngqtPJKlRjk48yNc_g7YCWr69VNdpQsHZYg1i6ufdhpd4uKvnnDcKLNBAbICRdbdBBIbrJYfezAC5-yZRGKalsCwxKg5bBTV9KZ8HkYt-QOgY0_1xuGeX39Gmljjf0CG4SnqHXQZCEtMwT9AOTT3o1rCwaf3mXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان؛این یک سند تاریخی و پیامی از ایران مقتدر است:
صلح در سایه احترام متقابل تحقق خواهد یافت.
جمهوری اسلامی ایران به صلح جهانی با حفظ عزت و استقلال، پیشرفت و همکاری منطقه‌ای همواره متعهد و پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66429" target="_blank">📅 16:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66428">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66428" target="_blank">📅 15:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66425">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=fYmd-M-wIeY-0FA6UGvsdaRJbbXE3VmyeGyKVAsSUFOLZtPCrE7aAcDN12u1r4EW8-ZZsn2YGL1BVG6VvVi1NNeh32vtbGNhT1lhSCjCrEN9ag9ra00XgtuNFnG0GCbk7Kvh0evjBMvCycbquBXg712pJfrIhD0mVjsIijsi-tOGPzQSrEgH5itHTyR3oW1UEUbV5FEqDBPwOin95ssw7mCSlZ4kxywaKkth9AoSnIqBIVDiTMvmTTlIvk-eF70kpUxvydHe0qw-eHliHGl4k-tA6T8vH4R6xLDQBZZ_w2P0JJT3WeMyDPcV6ilVFZ_CcV5v5tjdibdfAayRO5covA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=fYmd-M-wIeY-0FA6UGvsdaRJbbXE3VmyeGyKVAsSUFOLZtPCrE7aAcDN12u1r4EW8-ZZsn2YGL1BVG6VvVi1NNeh32vtbGNhT1lhSCjCrEN9ag9ra00XgtuNFnG0GCbk7Kvh0evjBMvCycbquBXg712pJfrIhD0mVjsIijsi-tOGPzQSrEgH5itHTyR3oW1UEUbV5FEqDBPwOin95ssw7mCSlZ4kxywaKkth9AoSnIqBIVDiTMvmTTlIvk-eF70kpUxvydHe0qw-eHliHGl4k-tA6T8vH4R6xLDQBZZ_w2P0JJT3WeMyDPcV6ilVFZ_CcV5v5tjdibdfAayRO5covA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین اوکراین به مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66425" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66424">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=IsUJZFpLvIS3rm9NU3DflJovm0cdxRcKzU8i_bL4Ho7cZeT8xJCmF5x4uQY3qqz1qDttOOnFaauAjbaDE5pZ7Pws3q-ZIWng9qQeI36IS9GoToYaGrDo83U3rPZ4WHAPSaHHlHxhV9kns65AtyVZSpdkvkPm-z3SRVse2f607QKlnONSkY3OD53p-praFotmIhAOr__Hv2rakftuQnO5dU3UQuTwAfLq8_3RXUXG-ljklUbGKpg8jVgEjzTpIBYdovrnRa_vD3G1dp19dBtYkZrGw4oT8cnT7i_EKpXIcr75-Emm-hhxLNpsI2DKqZOhjrVkUekBIjizso1XvwlBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=IsUJZFpLvIS3rm9NU3DflJovm0cdxRcKzU8i_bL4Ho7cZeT8xJCmF5x4uQY3qqz1qDttOOnFaauAjbaDE5pZ7Pws3q-ZIWng9qQeI36IS9GoToYaGrDo83U3rPZ4WHAPSaHHlHxhV9kns65AtyVZSpdkvkPm-z3SRVse2f607QKlnONSkY3OD53p-praFotmIhAOr__Hv2rakftuQnO5dU3UQuTwAfLq8_3RXUXG-ljklUbGKpg8jVgEjzTpIBYdovrnRa_vD3G1dp19dBtYkZrGw4oT8cnT7i_EKpXIcr75-Emm-hhxLNpsI2DKqZOhjrVkUekBIjizso1XvwlBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏جی دی ونس در مورد مسلح کردن معترضان ایرانی:
در واقع تا حدودی دشوار است. می‌دانید، نمی‌توانید همین‌طوری از آسمان سلاح پرتاب کنید. واقعاً زیرساخت لازم برای رساندن سلاح به قلب مردم ایران وجود ندارد.
یکی از چیزهایی که رئیس جمهور خیلی نگرانش بود، همه این معترضان بی‌گناهی بودند که توسط افرادی که چند ماه پیش مسئول بودند، قتل عام می‌شدند.
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم متفاوت رفتار می‌کنند؟ مطمئناً امیدواریم که اینطور باشد.
و اگر اینطور نباشد، می‌توانیم وقتی رفتار واقعی آنها را ببینیم، بفهمیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66424" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66423">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPCbnso7tBMy1g3d3VMaUckQgyA7RZlfu4t0vUwxsCO5enagG-Pzeo70Z6qpp6GbaA7K6lyTOcf0FwVBsLIwe0LyHgCqIpu4CEwzhWu_SOBAuWI9KtvjudHPaxMn5Lk7w2pP1SUs-8IQlOGav_O3Vew5s1i9yWLFbg1EY2T5lxEEHVs3RjecJLWIjG_IXkhKo7zdFXgGbsDqXoCcbrh4U3D6f0TIDIjASwkRRQUARIlCFCTtwagidd_FxQEhXREg6hUcpdDDh6KdlaD4wSy54_9kRaxfIJ-6Uwfvaa5-1MM8pFE_fA4XG8lX84n7l9YB4JgzO9vZ1PLznpfHIL2Jdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حملات اسرائیل به جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66423" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66422">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66422" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66421">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66421" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66420">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVDvpjNz2u9D8NBbFOCH0YxTWckFsPjCuLaLKUKaukAr0cndJa0OWDRnTwZGbmu03uASiSQbVpRQCy5pRvJ-MCzCNluPCkuoV2rmtHDbu06iPsl_d0Hq_tUGWCq6OKbqJDvkb21WRr1yDEy3Tk8ve-TY09TS2byOKRU_uaTvd3f7btvAb1m3vX8ZJ2wEDr8PBCGVhToOULxEcTThAdnm6KMTOHgIlzpy44J_7u9PY0LjSyeOKprAzIYDw8_JF9hKhVKxTL91AiiY7cDSMEkKAXBLhH_EakbhtUpyPQ1UWDnPT9Axc8RGydO0qdUl9eW0P_GIeprFnsbDpNEJnO1DLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66420" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66419">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66419" target="_blank">📅 13:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66418">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66418" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66417">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قطار پیشرفت آموزش و پرورش کشور خدایا شکرت   @sammfoott</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66417" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66416">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9c8bYm4Bokjr5hc30sytoYwVvQmHP9tJpUXPN3tudtPhDh0w3hOd02_wGsAbrlVvd0IJFgq7Iz3C7mh9pY_CZD77_1qnhdAcLNtVA5k-HYEYvUOCjePaYf-kzxZMCFhqYhgJd7e7YylZIOSunJr1NJ79y46QDZIRsf_MjWGk2-EFWDe-4fkieKMmypDEZ9Nu-w7Z0BekcwL1Mk05vkthw3ImFrfXlWOdTUaejh13Wgo8WYxOCiHUB9qm5xjeSw0D7PXyN6HiJNW9S6lhvQ82Hk2D4zCtJpgUNwp7N0VJGK8ANk0jopy3UnAD6taJHEpNUc3EF4UojzaDznvRDqzMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«این احمق‌هایی که فکر می‌کنند من با ایران به اندازه کافی قاطع نبودم، در حالی که بازار سهام به تازگی به سطح بی‌سابقه‌ای رسیده و قیمت نفت در حال «سقوط» است، یا حسودند، یا آدم‌های بدی هستند، یا احمق. بیایید دوباره آمریکا را بزرگ کنیم!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66416" target="_blank">📅 12:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66415">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66415" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66414">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66414" target="_blank">📅 11:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66413">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=d1cRqqCYVGAMWGPubXRYTyDUTyzyP86H8esEdY9UALLB2pIgtjSN0qt6aBwJtaWy6VCUY_r-p-fhwaIXMcoXGbE9OYdbx7AhBeVPg9oDZYf5yGhOSeO8usVmjCD1J8LjscxiwnfNnk1XULDzPDcA12UWZL78BwNjHidyAje0Bxy66ZQIsTennG2nNX80CGSsQziAptpKXGUJi37mo66FWgaC3TfNUcs3wyaUe9HmivPqpD2BAxhv1fm4hHO2wiQUwMn5iol8eO0k1sMWnGzo3xMoALlIycEMg5H50CXpkgcac48VM3dNJQ1QJZzeKN6uf91rqJEpmmMNBCzub0gs5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=d1cRqqCYVGAMWGPubXRYTyDUTyzyP86H8esEdY9UALLB2pIgtjSN0qt6aBwJtaWy6VCUY_r-p-fhwaIXMcoXGbE9OYdbx7AhBeVPg9oDZYf5yGhOSeO8usVmjCD1J8LjscxiwnfNnk1XULDzPDcA12UWZL78BwNjHidyAje0Bxy66ZQIsTennG2nNX80CGSsQziAptpKXGUJi37mo66FWgaC3TfNUcs3wyaUe9HmivPqpD2BAxhv1fm4hHO2wiQUwMn5iol8eO0k1sMWnGzo3xMoALlIycEMg5H50CXpkgcac48VM3dNJQ1QJZzeKN6uf91rqJEpmmMNBCzub0gs5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
برشی از سخنان تند شب‌گذشته قالیباف خطاب به ارزشی‌ها و تندروهای کسمغز
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66413" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66412">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66412" target="_blank">📅 10:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66411">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=K8fepzKEbmotfOA4IjUkDS-9VJATEU5OzPWd5vhAPVV4d94b0slJFoviCW7kGmoJDwvbvsoZP_ut1NvK6IHBH-PQPcqh8dVjVPyUCJyzw9XwKLLsDkXkquDjBrILbNQ1kpfMCEFnJLyZe6-erXS4f_zELJ2LzmdX8m42jn_VNTZWcMdqJPJmWosFoYmfzarrUMGYGV1Cj6sIVFbX27AES43d3yiI23EaVUx9Vgdic9TxP3k3cIJ93-H8KDpbsgvQoPXrYaMlgfWcj_kjx8-ZHs8qPJbvZ1OVsgitGIt8CQiKuuG5inr5FtgYRVNREr0BZ1t9WIcZbJFMzgnyBq8IUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=K8fepzKEbmotfOA4IjUkDS-9VJATEU5OzPWd5vhAPVV4d94b0slJFoviCW7kGmoJDwvbvsoZP_ut1NvK6IHBH-PQPcqh8dVjVPyUCJyzw9XwKLLsDkXkquDjBrILbNQ1kpfMCEFnJLyZe6-erXS4f_zELJ2LzmdX8m42jn_VNTZWcMdqJPJmWosFoYmfzarrUMGYGV1Cj6sIVFbX27AES43d3yiI23EaVUx9Vgdic9TxP3k3cIJ93-H8KDpbsgvQoPXrYaMlgfWcj_kjx8-ZHs8qPJbvZ1OVsgitGIt8CQiKuuG5inr5FtgYRVNREr0BZ1t9WIcZbJFMzgnyBq8IUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب دو سال قبل شاهین نجفی درباره قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66411" target="_blank">📅 10:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66410">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66410" target="_blank">📅 09:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66409">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66409" target="_blank">📅 09:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66405">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VI2Yaq_BKLHQX_aeNMuKgsI_vUbvBGPtfpffoiOyKp1InQCI95vCJnb_JMtr8wdXBPJ0ce4_P-BTAD7Zx6kFGchlV0RlUH2CKjD-H7dSNpsqWVgXmDK3dx85LmyT9eKqLrRkB1TDbpmMfVAX7Owmw2Ps97wLWyrGGMy4ZD242ksX7Kc_TLAsmYHsw2OgOb_FtW5VWIwjuJL6_3PP-vZcc8a_MnNaOylvWcg2eHxWNip8qQNv6NXWoz4cBXEvgqyAdTE5jt0j_GkL751RwBq0H2skgohYEuSZ9f0bF9jmxFAvf4Etbpm2KgHEFCarboBMfaLvFILHBUfjQ01mhZRYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qot2_it-zJShEm21bIk7VKcmLNuw5pIM8Tz-ozUprzm1LCCBvqUl36AFqwzPqsrzao1HWr30LmoT5TgxLg5vCfQh044O5X1zQQmsG3IMWR0rM-6FRSyJJ45z1njcyhGAmK6j38Bmbg2l1PFQ5XN4z7ILrEH_tIo-hoystIiDxybzD5oN0ogSIfIAQUglSEgJXjKwW_6azBlWH0TBgDsJnYd2krzgifKUtsdEzX7pXQeGm6o-yqzu8dpD2Mu2B0OTRxpcBiA-Viu2CDqgtwziIMHT2tJLsRieJYGygY6Wp-ebCUt9j6wdlfAjRKdLhsNDuW3T5NT-MnSLEpeepoZd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDGYoL03BM5dT2gySG7vwxwgwblGY1f2MbnmCuoy5Esr4ruPJgteAO2roeo-n1dsNymljvray9RxeWoxpkjpwW4wxdS1yd1IWbTUk_GT0pYGhaUtj0XJa-xn7SNIkI8AJlvJv2kDAmET-SFxlmjnMtqJhKaql7sWrV3tWMizV38lI4LodM-w4kZtn4gdje2oJ6ZzwSauUefb1sVpNe4QcgneyYOYhOgRQBfD-gI0gah7E3nNgQZRVc7Isrh-rt8oocAMufbzlAtyx-m48t2zHW9vLBZT58Y4D_cAeZSXIhajQYC25WYoCRejSAVQpQpeJ9WRHcoocVWN_rh2kl-ZIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد  @News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/66405" target="_blank">📅 04:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66403">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrWn8zDtdE8qQ0NfpgE1P69GHyu_mcXSunXJD8IpBM_nFSISN2oe7hisLi6bfOEBNZCRggk60VHId_6UHsKyzvpTtWXQXTqR6N31SVD8MdWaSlr8zDZyWwjD3rO4sWriCuJEc6o_VJnA3sL1mMnrAO1EvoCfPf8aMl5lPtn1EFixZ0mNZJNV1p_zi9z434TlqfjEpUiiaLDb4_83LxiM8UP5PlOaodOroAx-uGk8fwdKtmj-DzkvDPdAzOfgRTMval1Bq8PcWMah2afy5su7wceFmIdT9v_gWQV3orT7qf938yAmDKFasO5AruN4cW0g-5yqtC0_qylR_t5drR6X8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=Dc3k8oKpdIqbioFi0Ft6A9l4BuQXMfBRLBfCcTgt-DYFgS4pip9ujPKNPMtnwvmcExHVJhRQuR2K_JB0C7h69nkNfmOXbnkVgXfqPEWYASSTLkRPu41OqkHrEojyLOwNA0W971zwgjDiF-7Qjxrvg-SCJiJDSpIXITFRgrL5wIkczfzu9ZNt5MfwPpVc_mKC1PyEhZv1CKt7ZD0fSPUfSzZNdw61H2sGUqEwOa1805XZvnz9BtpvOLH6GDwhasKJ05XiqvhlGrUQXcqyAgFhm30E74mdwSFdlADc6TUumx53Dd2N0y0Rp5X_Xd4OdBnaRYeCLgiTGfwwYdZnI-KmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=Dc3k8oKpdIqbioFi0Ft6A9l4BuQXMfBRLBfCcTgt-DYFgS4pip9ujPKNPMtnwvmcExHVJhRQuR2K_JB0C7h69nkNfmOXbnkVgXfqPEWYASSTLkRPu41OqkHrEojyLOwNA0W971zwgjDiF-7Qjxrvg-SCJiJDSpIXITFRgrL5wIkczfzu9ZNt5MfwPpVc_mKC1PyEhZv1CKt7ZD0fSPUfSzZNdw61H2sGUqEwOa1805XZvnz9BtpvOLH6GDwhasKJ05XiqvhlGrUQXcqyAgFhm30E74mdwSFdlADc6TUumx53Dd2N0y0Rp5X_Xd4OdBnaRYeCLgiTGfwwYdZnI-KmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری
؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66403" target="_blank">📅 04:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66402">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66402" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66401">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Si3LNuOBRFwUeckxEF7SkenM97sRCjydkyTCz7_gD5Kha1BHoJ0rAPoJBxxXXmJLqFyIVQkXzyYd9VW1f0RB46PvuTFORInM1kBK0x5Mubg1lCncTLkAwKi8ejE2gnTJcn_Bvn4o4ZF0Z_Gi0fMZ2RtqmVeHOHcZQwtcGtyHRJVOE71CIvBwudEjkoTsMyfQyDZWg-bTPKy805pdxmMTRvGpm6z305oYkvxCteq4Wu6-6xemovZLncHGoevGUjYVSNGMG3AyDsKXWuDDxf0GVkg4Owg4RyJcFQ14-CtKpORQT_-LWFgwLBJpvFRiDPG-euLZyOp5TVQo5HPZFATXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66401" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66400">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66400" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66399">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66399" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66398">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛بقایی سخنگوی وزارت خارجه:
تفاهم‌نامه به‌صورت الکترونیکی بین پزشکیان و ترامپ امضا شده. جمعه هم خبری از مراسم رسمی نیست و فقط هیئت‌های ایران و آمریکا به سرپرستی قالیباف و جی‌دی ونس تو سوئیس دور اول مذاکرات فنی 60 روزه برای اجرای تفاهم‌نامه رو شروع می‌کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66398" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66397">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
سخنگوی وزارت خارجه جمهوری اسلامی: متن توافق با آمریکا نهایی شده و به امضا رسیده
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66397" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66396">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=DJNeaT_CwO4-GqCXeIpOl0g1RbV5RLZO-lwQ7Xc85EmsZK1E30RxagwrEX4u9Hlwi2EcQqeSdz_drpglq60h5zq6Es3oTad0gLSJKeoRpZgV_2moI2ICz5XfVg91VOyZ1fjN7o_97_IM60Rcs1j01cWEtsQTXj872Xe3VcPJ9ao91WU5r1Xg2tmtcLr7Up7mf5v12KSlTgsUz1eI3VDOe0mOHXTbuD67l5niEfJY_9QxysHT2p_D6xResiXFyPY_Gvtn2GKQpHCeeKxHND3ettTEAs8NLSSuAmRYsXbNTx9vh4-X2gePqrBnbz7s8_iqIeJnTmLu-5zvfVZyJYllww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=DJNeaT_CwO4-GqCXeIpOl0g1RbV5RLZO-lwQ7Xc85EmsZK1E30RxagwrEX4u9Hlwi2EcQqeSdz_drpglq60h5zq6Es3oTad0gLSJKeoRpZgV_2moI2ICz5XfVg91VOyZ1fjN7o_97_IM60Rcs1j01cWEtsQTXj872Xe3VcPJ9ao91WU5r1Xg2tmtcLr7Up7mf5v12KSlTgsUz1eI3VDOe0mOHXTbuD67l5niEfJY_9QxysHT2p_D6xResiXFyPY_Gvtn2GKQpHCeeKxHND3ettTEAs8NLSSuAmRYsXbNTx9vh4-X2gePqrBnbz7s8_iqIeJnTmLu-5zvfVZyJYllww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
به محض اینکه آتش‌بس برقرار شد، دیدید که دشمن در خلیج فارس اقداماتی انجام داد و ما بلافاصله پاسخ دادیم.
آخرین نمونه آن حادثه مربوط به بالگرد آمریکایی‌ها بود.
علاوه بر این، دو ناو جنگی دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند - موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن برخاسته بودند، هدف قرار می‌گرفت. همه این اتفاقات در حالی رخ داد که ما همزمان مشغول مذاکره بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/66396" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66395">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66395" target="_blank">📅 23:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66394">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=P2b-DoO_K3mqouffRj1fQBzoo63e6ftdq7L16MdWxbv2qK5lmSTVrzNJ0J4Eb4TwJi9WkG96bTyhnCYgSzPUusDm-gn-Sb6Yt02j6jP4IyOCefXefpDZXS2rQroo518nSstHchO8cUnYYQnbUwvQGDXM1BBJ5yb4nfT5PQM9ipr0fbZEMs1pCehLqQ6r7DViyD8Noqf80ZxTa7ELbLBhjIZlodZVV4dd6DEdRIY1SRUZj3P9Yr7An8sepD_244LFcJ8FcnxxJ1mNN8Jjjkdu3b8aUZyIXGnFC4XTOAhLLq901xYTX7eZYEO7CGeGGKEx63iGlAmsmiwcRnwFnOmJpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=P2b-DoO_K3mqouffRj1fQBzoo63e6ftdq7L16MdWxbv2qK5lmSTVrzNJ0J4Eb4TwJi9WkG96bTyhnCYgSzPUusDm-gn-Sb6Yt02j6jP4IyOCefXefpDZXS2rQroo518nSstHchO8cUnYYQnbUwvQGDXM1BBJ5yb4nfT5PQM9ipr0fbZEMs1pCehLqQ6r7DViyD8Noqf80ZxTa7ELbLBhjIZlodZVV4dd6DEdRIY1SRUZj3P9Yr7An8sepD_244LFcJ8FcnxxJ1mNN8Jjjkdu3b8aUZyIXGnFC4XTOAhLLq901xYTX7eZYEO7CGeGGKEx63iGlAmsmiwcRnwFnOmJpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66394" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66393">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=gEm9VqeApATJZYX0u2pAIzdg4iEi-wRhAuqoEVOUBVn-v5XCmcwLZ7BIUo51Hu-j9E9Cu-DLtUBJTSfd7C8H4oh4mGsRtjzvPfoDy0ZoEXGzzXtqRYnBEwXrqBen43gQ2ZBbtqSWrCNhO3n6u6ZbXyjOcV33SHmZ-mSP4xxGy2pgRBYXqDz5NUgfJyfqRiqGrwLidn6KgoXK7vtbJOHyt4b51rY0BY2kBwd-leNU0DMiFsd3JKYziSx5jEXZ3aum7EraDdeYX-C5es3nmBrmhVPlgK09_0lu0yjs-EntQR77eyycSb8AIiHx4sHKtYtAlRQBGhTYHy4fG0n8bqiwmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=gEm9VqeApATJZYX0u2pAIzdg4iEi-wRhAuqoEVOUBVn-v5XCmcwLZ7BIUo51Hu-j9E9Cu-DLtUBJTSfd7C8H4oh4mGsRtjzvPfoDy0ZoEXGzzXtqRYnBEwXrqBen43gQ2ZBbtqSWrCNhO3n6u6ZbXyjOcV33SHmZ-mSP4xxGy2pgRBYXqDz5NUgfJyfqRiqGrwLidn6KgoXK7vtbJOHyt4b51rY0BY2kBwd-leNU0DMiFsd3JKYziSx5jEXZ3aum7EraDdeYX-C5es3nmBrmhVPlgK09_0lu0yjs-EntQR77eyycSb8AIiHx4sHKtYtAlRQBGhTYHy4fG0n8bqiwmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
بدبینی و بی‌اعتمادی من به ایالات متحده از هر کس دیگری بیشتر است.
حتی اگر توافق نهایی حاصل شود و توسط قطعنامه شورای امنیت سازمان ملل متحد تأیید شود، باز هم قابل اعتماد نیست. تضمین ما قدرت ایران است
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66393" target="_blank">📅 23:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66392">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb769475.mp4?token=oEdnXFCSX6d-0ls0R_8jdt-FzFVkoIuO44Yb-Rvx12fxso2qKhIqRyRXp6JUZ8LwRDX3P0YCgmny0CNXpgFP7RjKiqxYhS8GC5jIiHJLwkI1JWhK2qX7upkaqMUbhmspbKQgujszPY8y8mRcZuTuNtJFdAb7vQPop9msApVQlb-vaATTeraKjDQRfe7mYUhe4ijgWOkiMyKvCcKbZhT-BR3cKgbP9vduP79vvg80Cy2H9ZRDhpOXtCozzvRWlR2G1Dn-jsBG5k7HwIQeQR_w840huEv4U8vxxe-M5JkIfP_q0NSv-sUiToc5ffH-3Jx1J_8PWAUdnOlJKlrr2inS-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb769475.mp4?token=oEdnXFCSX6d-0ls0R_8jdt-FzFVkoIuO44Yb-Rvx12fxso2qKhIqRyRXp6JUZ8LwRDX3P0YCgmny0CNXpgFP7RjKiqxYhS8GC5jIiHJLwkI1JWhK2qX7upkaqMUbhmspbKQgujszPY8y8mRcZuTuNtJFdAb7vQPop9msApVQlb-vaATTeraKjDQRfe7mYUhe4ijgWOkiMyKvCcKbZhT-BR3cKgbP9vduP79vvg80Cy2H9ZRDhpOXtCozzvRWlR2G1Dn-jsBG5k7HwIQeQR_w840huEv4U8vxxe-M5JkIfP_q0NSv-sUiToc5ffH-3Jx1J_8PWAUdnOlJKlrr2inS-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
ما بر ایالات متحده و رژیم صهیونیستی، که قدرت‌های نظامی پیشرو در جهان هستند، پیروز شدیم و اجازه ندادیم که آنها به هیچ یک از 9 هدفی که اعلام کرده بودند، دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66392" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66391">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66391" target="_blank">📅 23:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66390">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C50NIXLh-JRj58O5mbCiHWASvYpyiWxQeMNmhKDhrvANGbkmQuMIRr_edETs8FLOh4OCCWHbnHDG-8Z-TSZ1rMsZs9zQ1CfNeB2TNfh_TS845MLS69JQFUBALsKQgQiLC542IMc7LzKkJbHDG-S34mY2m3USDljZJ2ScjOBNtBUkxihBdcDqON_J2w5pKxyfqwLIO13AWDKWHfvMc9CrSPPwmdFDACCcar_IGI5cee_-SBUzdnQJl1quppfpKAbtxrEM0sNxD7GYek2t2QTWUDLrDM-eI4gPbvGZOyzLAI0PynYu2sOWNQpQnPem2yMlPMrmaywp2ccgQLlEwn-P8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شبکه خبر:
مصاحبه اختصاصی رئیس مجلس درباره تفاهم‌نامه پایان جنگ تا دقایقی دیگر
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66390" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66389">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66389" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66388">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-2FPYcn7T9w_AvDdYz3sdA_URn99_UIgjFqMqntvXNidsuuyzxiuoVuIvfR7_UOSj6Blfl3WspbNE814tZhxTe_zV1Db0GnbjjbCfmyf_2mC7OgmkGFO6TEkYiFZ2XOaXz8uWimJtYjej6TH8Vo98uBuIkzHC4GsVp89freXVHGRR2wW37uy0Ng27cUgC0gScwCq8nnkkej16zXuMLuu-9kdEWoyhUy-Bn-9rKHoFFsJyag-iu0oKMfaD7BkjZr5C8uzpTQfCKmYfoMKzfyBjqZ-w__BEDomeMgbXxlb6WffKx5Bg-jCeO5BfbQBCA_hKRbrKGsITyzDO8XdJOlIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیندزی گراهام: من همین الان یک بحث بسیار طولانی و سازنده با ویتکاف  در مورد ایران داشتم.
بعد از این بحث، به نظر من امضای تفاهم‌نامه برای ایالات متحده مفید خواهد بود، تا جایی که تنگه هرمز شروع به باز شدن کند و خصومت‌ها با ایران متوقف شود.اینکه آیا ایالات متحده می‌تواند در مورد برنامه هسته‌ای و سایر مسائل به یک توافق قابل قبول و قابل تأیید با ایران برسد یا خیر، هنوز مشخص نیست، اما من جنبه منفی کمی برای تلاش کردن می‌بینم
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66388" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66387">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66387" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66386">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=ZWH3rVqXhOXuKQucH5MrivPDI5WTRVrt-4QebnnZFLt-C78SZAVd_Dq0gPfv5LuDen2WY3bKiVM8UBtVg9R-P_tDClYKjL6qPEbEhtE_oHHHrSYxGpBtIc6--Wy1OZ45rFDo-vj949QR0SWmtua12Yb4cHTmD_DYbDZiF-AMlNwMf3fI-Qj0PesD_sU_08wL7MxbCYBHYhMF0Q_tqa74ebomLElAza7gbLnmDA5AQAMhrCdQgxmGi7Seg6-nescBYVygM8bfmbdES0Z9kK4PZ7BsKOWF33yEQ9a1tRo5HL_I1MkrGBuFjiA8vEfO9UI5thZhacrxiEl-Sx-jqY0naA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=ZWH3rVqXhOXuKQucH5MrivPDI5WTRVrt-4QebnnZFLt-C78SZAVd_Dq0gPfv5LuDen2WY3bKiVM8UBtVg9R-P_tDClYKjL6qPEbEhtE_oHHHrSYxGpBtIc6--Wy1OZ45rFDo-vj949QR0SWmtua12Yb4cHTmD_DYbDZiF-AMlNwMf3fI-Qj0PesD_sU_08wL7MxbCYBHYhMF0Q_tqa74ebomLElAza7gbLnmDA5AQAMhrCdQgxmGi7Seg6-nescBYVygM8bfmbdES0Z9kK4PZ7BsKOWF33yEQ9a1tRo5HL_I1MkrGBuFjiA8vEfO9UI5thZhacrxiEl-Sx-jqY0naA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
وقتشه که سنگر رو از بچه های لانچر تحویل بگیریم و یه زندگی خوب برای مردم بسازیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66386" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66385">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=sKu0w8q8nAltIdFoX4ZLZ5RWuZfOppFuiNaTbXDrV1yuy0VsqGk_mWkxAQCsqdhg5qo1ATu_mmHITcJX1TLkMbFFVgO4aLhWRb0GPxsw24lSPu2d3evEFIxn7Q3w3tmQJo3olMeeYJ-qVKHnbYLB8S7WVkvLvG1ODv2SOO6l1bFAo71fujy-Crva9dVrfyqonCCobjNQ4SF4m7gH4OWImJ9bkP-Njf5UnfbkLo4DY_vcSwbOtddbnhFCJovkXKhV2hE8bnVOv-gZeTT9E1wA2hUiE6raTS_SqKf_ezyf3PafMSAyeoVLXQ6cjfmoeV-l4SiJAOXfUqAUY71ouM5ODg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=sKu0w8q8nAltIdFoX4ZLZ5RWuZfOppFuiNaTbXDrV1yuy0VsqGk_mWkxAQCsqdhg5qo1ATu_mmHITcJX1TLkMbFFVgO4aLhWRb0GPxsw24lSPu2d3evEFIxn7Q3w3tmQJo3olMeeYJ-qVKHnbYLB8S7WVkvLvG1ODv2SOO6l1bFAo71fujy-Crva9dVrfyqonCCobjNQ4SF4m7gH4OWImJ9bkP-Njf5UnfbkLo4DY_vcSwbOtddbnhFCJovkXKhV2hE8bnVOv-gZeTT9E1wA2hUiE6raTS_SqKf_ezyf3PafMSAyeoVLXQ6cjfmoeV-l4SiJAOXfUqAUY71ouM5ODg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد پرونده اپستین:
ما نمی‌توانیم فقط به این دلیل که فکر می‌کنیم چیزی اشتباه است، مردم را تحت پیگرد قانونی قرار دهیم.
شما فقط می‌توانید مردم را در صورتی تحت پیگرد قانونی قرار دهید که مدارکی برای اثبات تخلف آنها داشته باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66385" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66383">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه جمهوری اسلامی:
در یادداشت تفاهم ۳بار ذکر شده باید جنگ در همه جبهه ها از جمله لبنان پایان یابد.
همچنین بر حاکمیت لبنان تاکید شد و حضور ارتش اسرائیل با آن در تضاد است.ادامه اشغال اسرائیل از جنوب لبنان نقض تفاهم‌نامه است و اقدامات لازم را اتخاذ خواهیم کرد.
یکی از بندها تایید میکند که آغاز مذاکره و ادامه آن مشروط به اجرای تعهدات است ازجمله توقف جنگ که شامل لبنان هم میشود.جنگ بایددر همه جبهه ها از جمله لبنان متوقف شود تا مرحله مذاکره آغاز گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66383" target="_blank">📅 21:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66382">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=oI_OJC3XZzeIgugdBa6dNV3gtBXwsLVUEz8C-2sNsuzGpWfY99iGukXwxZ4Tt_q9upmRfqd4baaK1aHOgN_4KO2ZZnciumgppQLnaP_S4M_Q6XrIuqTz3dUNgDnWT8i_HVljXZ2QzeIrEo2E2OJPilx-BKJ3s-GSoYnaRXvWFL53rep6HRZ5DZCsWt7Q2oI5BcDIXcTCdyDF0dy4kiVvXxnSPsFC3H5yVR-SHFXHF47g-4w4TXifO3OkFhT0-KSSfGGX_y2MxLJ2Sm9ICd5_irkqw8YVpDbbH9ikb-OuFcgOewenVdoQU_Y6A34gSjc2tf-Y6x91CwLHdVLOtZ6KPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=oI_OJC3XZzeIgugdBa6dNV3gtBXwsLVUEz8C-2sNsuzGpWfY99iGukXwxZ4Tt_q9upmRfqd4baaK1aHOgN_4KO2ZZnciumgppQLnaP_S4M_Q6XrIuqTz3dUNgDnWT8i_HVljXZ2QzeIrEo2E2OJPilx-BKJ3s-GSoYnaRXvWFL53rep6HRZ5DZCsWt7Q2oI5BcDIXcTCdyDF0dy4kiVvXxnSPsFC3H5yVR-SHFXHF47g-4w4TXifO3OkFhT0-KSSfGGX_y2MxLJ2Sm9ICd5_irkqw8YVpDbbH9ikb-OuFcgOewenVdoQU_Y6A34gSjc2tf-Y6x91CwLHdVLOtZ6KPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره محمد بن زاید:
محمد در امارات متحده عربی یک جنگجوی باورنکردنی است.
هفته پیش بمب می‌ریخت، گفتم «کی داره این همه بمب می‌ندازه؟» امارات بود. او یک جنگجوی خوب است
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66382" target="_blank">📅 21:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66381">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VH4oGPmLxXJ7aT93chGaNKk8kZ4BOtNVL1qPW9jFgFrnwaBKyElBq4fFeO6GBPbmOwokCMjuD1SB1FDkwuXtZ8VIIxooPNbk9i6-rbw8vFTVkttNcGDqi0aaaIekYY5ss9g9q7BZ9ptc5HMiixa-I8R8_xcKBFHG6Ul8KjUOA0BXdROtC-nsCK70QyjhhCng3pp2Q9A55EtjeYHgz0QyqwP1h4MkJ3leCaXVdCOQ-CIeyv5SnAmvkAaYKNUtK7tP75oE0kxkB3pNqxZI9O7eDfEDiNzOCfIIVr8RH43RK0HKck9IA4WFaliWbdKNx2XZtQxe7cWB-shjeiA3r6E72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛الجزیره به نقل از وزارت امور خارجه ایران:
ما در حال حاضر در حال بررسی ایده امضای یادداشت تفاهم از راه دور توسط روسای جمهور ایران و ایالات متحده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66381" target="_blank">📅 21:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66380">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66380" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66379">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
#مهم؛ پس از روی کار آمدن مجتبی خامنه‌ای به‌جای علی خامنه‌ای، #سعید‌_جلیلی نماینده‌ی سابق علی خامنه‌‌ای در شورای عالی امنیت ملی عزل شده و #علی_باقری‌کنی( برادر مصباح‌الهدی، داماد علی خامنه‌ای ) جایگزین وی شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66379" target="_blank">📅 21:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66378">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=PHZpySjKR6grS47-e-DDGNzWXQ9LDNB2u6mzvMGtQqRMOyRzEBhmReRQazMMqQqO_Lm4k0w4JKNn_PnYYmh_xQSdpGKn7vcj6MUXsXZBjGs6Zh16L401jQIeYNCFjvAVJd2IX7qiCUrtVayeThkrLgUjiahTSU62dtW2vSufBthf3NVfkXH0s4A2LhabhgGKpG7rcHpRIjj39aGnxrMSMrrwqwI3ipev1TN0pLtEReJgURhXMvOD0bb9t74lE23aMgZcbzX-ohim4J_MeXnStMy6bxY8MeApJf8a92217TC7gVJ3yNZlVJK3qCugR6HLgWukUSj5W67DSPdWmeINEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=PHZpySjKR6grS47-e-DDGNzWXQ9LDNB2u6mzvMGtQqRMOyRzEBhmReRQazMMqQqO_Lm4k0w4JKNn_PnYYmh_xQSdpGKn7vcj6MUXsXZBjGs6Zh16L401jQIeYNCFjvAVJd2IX7qiCUrtVayeThkrLgUjiahTSU62dtW2vSufBthf3NVfkXH0s4A2LhabhgGKpG7rcHpRIjj39aGnxrMSMrrwqwI3ipev1TN0pLtEReJgURhXMvOD0bb9t74lE23aMgZcbzX-ohim4J_MeXnStMy6bxY8MeApJf8a92217TC7gVJ3yNZlVJK3qCugR6HLgWukUSj5W67DSPdWmeINEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
مردم از من می‌خواهند پل‌ها را بمباران کنم.
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن ایران.
اما ما آن پل را بمباران کردیم، دیدید که
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66378" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66377">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=PjkUQA5uYiJPYVewXL9blmW9Laj2l_VtcUeiq6EqA_-HP3n3tv04CEvD21JRNM5UFTBGJi9SDVgX1BqUsYVGpsm8qH1mI7Mv3nx_HRtmO04ctgRl2b3WpyEvv0lp-k7Mnp2G739_IP1WaEKvqJ7aNvZXHqQzAspq1hqxIpYE1VEtSWXtxliWz936FJaNJsuntE6bTH8yME3FZx-XkhL3gYCOywMJscr9RqpGGMl0gfftg-z3h2NctqfbjDBHUH_X0D9vUq3vEOVPcMwLA_8u60z1aeORXTOvtrlQZw7f25j4FurAkoiqWNCn5hL5H33U5X-epbYGhDRLjH-DKJdw8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=PjkUQA5uYiJPYVewXL9blmW9Laj2l_VtcUeiq6EqA_-HP3n3tv04CEvD21JRNM5UFTBGJi9SDVgX1BqUsYVGpsm8qH1mI7Mv3nx_HRtmO04ctgRl2b3WpyEvv0lp-k7Mnp2G739_IP1WaEKvqJ7aNvZXHqQzAspq1hqxIpYE1VEtSWXtxliWz936FJaNJsuntE6bTH8yME3FZx-XkhL3gYCOywMJscr9RqpGGMl0gfftg-z3h2NctqfbjDBHUH_X0D9vUq3vEOVPcMwLA_8u60z1aeORXTOvtrlQZw7f25j4FurAkoiqWNCn5hL5H33U5X-epbYGhDRLjH-DKJdw8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
گسترش توافق‌نامه‌های ابراهیم چیز دیگری است که امیدواریم به آن دست یابیم.
و من فکر می‌کنم اگر عربستان سعودی پیشگام شود، لطف بزرگی به خودش می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66377" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66376">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66376" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66375">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=kMEyWS2E8F_xUcC6sBXC49q_03xMhOc6CebsJwiKDRg81ikrtU3EswOVtVZkxEbJku8qIhS3YuRuUmy_eca25bmiDK0JMSQdIuxOMJj6nJT6hfAjYN_uHJl_U5rvJrY0AA56JRi46G-8n-Nz-RmKKpVnOlPccJuWmrg6OCVh5pN9lBLsLTOHBd2wLirMPlq0_4wt9-caZnTwLECHmBqdC5o_eqtTAIENM9p6dAbTHhpEcW2nbF38nEdJY5hOmHuxrlnBZrG6aXKEKcfB23scXP4dWKzwAYfkEagiUMA4nIiJOK_3Wla7stJ0lwglAcW1wjANgBU_8YFETYHsnShdggMEuU8mbN5m7FfSerNnC-3BakODPmcYqEX8Rmlib8Cli4F4lETwepZ0f10iKB6gV1VuE8erLpjqxnYn4heezMVP4x-MQ1tpfcH5ae801-YGG6Wptv6kE4df1OBI8CuxeBRVJtJVwWcUDdj2ccvW7VpZ5ZRcgiPAPZny0ukw31vDG2BhXH8KViXQEvQ-pmaTIKIzfFTEN9bFulEZx3MhkuQpiSS5oQpX6deKyVY4UtHPdGC2HQR51I0fs6zMvaZSAB5IzGlzlKNqYoJFa6GuwTda0_4DT0w2dP34dXOSV3KXrAKqVi2k1ah_asP3GyUzJY25actVIVWTP9DZjC8tXMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=kMEyWS2E8F_xUcC6sBXC49q_03xMhOc6CebsJwiKDRg81ikrtU3EswOVtVZkxEbJku8qIhS3YuRuUmy_eca25bmiDK0JMSQdIuxOMJj6nJT6hfAjYN_uHJl_U5rvJrY0AA56JRi46G-8n-Nz-RmKKpVnOlPccJuWmrg6OCVh5pN9lBLsLTOHBd2wLirMPlq0_4wt9-caZnTwLECHmBqdC5o_eqtTAIENM9p6dAbTHhpEcW2nbF38nEdJY5hOmHuxrlnBZrG6aXKEKcfB23scXP4dWKzwAYfkEagiUMA4nIiJOK_3Wla7stJ0lwglAcW1wjANgBU_8YFETYHsnShdggMEuU8mbN5m7FfSerNnC-3BakODPmcYqEX8Rmlib8Cli4F4lETwepZ0f10iKB6gV1VuE8erLpjqxnYn4heezMVP4x-MQ1tpfcH5ae801-YGG6Wptv6kE4df1OBI8CuxeBRVJtJVwWcUDdj2ccvW7VpZ5ZRcgiPAPZny0ukw31vDG2BhXH8KViXQEvQ-pmaTIKIzfFTEN9bFulEZx3MhkuQpiSS5oQpX6deKyVY4UtHPdGC2HQR51I0fs6zMvaZSAB5IzGlzlKNqYoJFa6GuwTda0_4DT0w2dP34dXOSV3KXrAKqVi2k1ah_asP3GyUzJY25actVIVWTP9DZjC8tXMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66375" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66374">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66374" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66373">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66373" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66372">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66372" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66371">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmaaGd6ggrH45FIa96P6z07jByxzyrP9e0m1E370qOdKBbNIxIAFKHKEbGzTzRlfmv3PSFkILiqHpNzAZgJbNh7cYU33kkLSUcUA_vY5oYhqDf6GrCZsxpV17plbSkaCm_oTdLGUeTfaIN3AkzlUc0xnWeifW9-CJzKyGAhv2p3irdRYm6Ls39e55cMqR9xZyaOfT7qTz6QOJ1-5vzDo08ZL0sP9Xkgg9NOkVCzs8JKL0TczcHvswnEsiqQgwQKsbEeyahF0XLLkUXchBTMeNoe68PaemT3j6GjXq2vp_lXlKPld77eTwEp8HfU9x7JWLQ3ZjSmToebbDwyBdjAF8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66371" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66369">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgb4dSvKmcNIK2Rze4kSwu-uXrf7viZtBiLXE3rxlmY0bgBN8eVCNs0AauCpGOGqyftKlPJJGvlS0aiocxzOl3L9gzKO1v7mTGygvMyyIiJzVXwj6CSFRf8mrQpv3v6Jt6WPyoOtw5Y3sE9iH-28DEWJ6oKZwnrgfoPHNUIxAZEhw0oHy6unlhmAYjjPHuMgI_rEEVIccQ0qxd6pf87sQLQ1EsUPj-1WB5wsGkOUM_bDxlddJ1BIiRVB2yCpne8XS1mR3DvhwKTt0_2C1_o43aiUEcEhlPequkQlG3ZHZDyfcxUSowY4fvhHt9nna8nkWCv5_E-xQe0qYeQ1PC8Vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توییت قالیباف:
تعهد ایران به همکاری برد-برد که بر پایه مشارکت استراتژیک جامع با چین بنا شده، قاطع است.
در جلسه‌ام با اتاق بازرگانی ایران تأکید کردم: ما مصمم هستیم که اجماع استراتژیک خود را تحت GDI به نتایج عملی تبدیل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66369" target="_blank">📅 19:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66368">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53224e4497.mp4?token=ufn9ZhEdYKG1wxLKFVB0NHWtE1aVqyul7PYShQQcbDIj1S5-wLxhLLSkoll--rQ60TOkzvDvCL3ooOXcLDKqvYRcCYiA0ROrGFORPLHafUSfDnji_4-8BS9xrpOi7BckKAuxheWDZeWllhw-VRy1UgpnBFH2J6OvV0VB8ohmss9imrDnuu7ft9sSN7lQM6-ZlMPgHTtjL1pvu5wYGAyp1GOodWaPYlfh6EkcRuscnREXKvYRsnb-qEfoL4cxtHAWu4I20tBLWnqMimiMzQhlp5AnUed5Gp0zWnt6LfLd2GKLCln4O1CfCHvBeuKzWuKymZDJWmyA8cdhUBsUnYC5sVL2fcwUfrbehd4UaHyQYbd8QIK9VCKV8I4wSTccSJnpOgAKPUAVsi1YB0NPWzFw_anNzPQM1Y-yCmcyRAD7xWYjwBl6f1XIP63Gc51OLdzTJkidr_qieNw5U8TutlJtmx8GvUqVOs3rQj3RuTFbmEyMryTE3soq7u22mLR-2j8nKqW_-38y2zy2XpSF4GMSbHM4_1mCq-cZHshTHR7f8c4wUlVrSN_su7G5LHd1dQYcNgnrw8TQ_d7L74nvk6ds6iE-Iqi_EujW7-KDgNp8HH-yCKC1sNl01ZZmZtIIPpPXowXf3UdNhMghMOvt8AzBqATAjbXx0LMVmmyl8UTfG9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53224e4497.mp4?token=ufn9ZhEdYKG1wxLKFVB0NHWtE1aVqyul7PYShQQcbDIj1S5-wLxhLLSkoll--rQ60TOkzvDvCL3ooOXcLDKqvYRcCYiA0ROrGFORPLHafUSfDnji_4-8BS9xrpOi7BckKAuxheWDZeWllhw-VRy1UgpnBFH2J6OvV0VB8ohmss9imrDnuu7ft9sSN7lQM6-ZlMPgHTtjL1pvu5wYGAyp1GOodWaPYlfh6EkcRuscnREXKvYRsnb-qEfoL4cxtHAWu4I20tBLWnqMimiMzQhlp5AnUed5Gp0zWnt6LfLd2GKLCln4O1CfCHvBeuKzWuKymZDJWmyA8cdhUBsUnYC5sVL2fcwUfrbehd4UaHyQYbd8QIK9VCKV8I4wSTccSJnpOgAKPUAVsi1YB0NPWzFw_anNzPQM1Y-yCmcyRAD7xWYjwBl6f1XIP63Gc51OLdzTJkidr_qieNw5U8TutlJtmx8GvUqVOs3rQj3RuTFbmEyMryTE3soq7u22mLR-2j8nKqW_-38y2zy2XpSF4GMSbHM4_1mCq-cZHshTHR7f8c4wUlVrSN_su7G5LHd1dQYcNgnrw8TQ_d7L74nvk6ds6iE-Iqi_EujW7-KDgNp8HH-yCKC1sNl01ZZmZtIIPpPXowXf3UdNhMghMOvt8AzBqATAjbXx0LMVmmyl8UTfG9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
معامله‌ها شگفت‌انگیزند. من تمام عمرم معامله کرده‌ام. وارد معامله‌هایی شده‌ام که صد درصد قطعی بودند، اما اتفاق نیفتادند. وارد معامله‌هایی شده‌ام که هیچ شانسی برای انجام‌شان نبود، اما انجام شدند و به آسانی انجام شدند.
پس هرگز نمی‌توانی درباره معامله‌ها مطمئن باشی. اما خیلی زود متوجه خواهی شد. فکر می‌کنم انجام خواهد شد.
آنها می‌خواهند امضا کنند  می‌خواهند به زندگی عادی بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66368" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66367">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=YlDClpUC2W2TxxIzkJVAIs0Nqt99Nz58aWb9guxyjuOeR89EcXcpiZ3YsZhxi5IpCvdR8hNzOhVF-JR1-NDXlZZ5lRjMDWfQmFZ_yga6pY4zyTEn65wKo4DAU4mQih6A_GJ7qSYnX2g6GT0XskOLyZaizeJAfsOFrJQIVQwhsahWOrYyz2Am5ACm6tqrtHHqMK2emRAw9cjiROV1yDEG7FP_Y4iloVtYMMBw6K5NLvM7cbbd4snS13pWGQ634dIxuMnkkfF5cbvvFesOCGA5R9_XpNOLJiyquTdGqt3I3jOdle8n2eAdLFlsm1RC3ubjHMlUisO3geU58RXNrc3zIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=YlDClpUC2W2TxxIzkJVAIs0Nqt99Nz58aWb9guxyjuOeR89EcXcpiZ3YsZhxi5IpCvdR8hNzOhVF-JR1-NDXlZZ5lRjMDWfQmFZ_yga6pY4zyTEn65wKo4DAU4mQih6A_GJ7qSYnX2g6GT0XskOLyZaizeJAfsOFrJQIVQwhsahWOrYyz2Am5ACm6tqrtHHqMK2emRAw9cjiROV1yDEG7FP_Y4iloVtYMMBw6K5NLvM7cbbd4snS13pWGQ634dIxuMnkkfF5cbvvFesOCGA5R9_XpNOLJiyquTdGqt3I3jOdle8n2eAdLFlsm1RC3ubjHMlUisO3geU58RXNrc3zIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار: آیا می‌خواهید اروپایی‌ها مین‌روب‌ها را به هرمز بفرستند؟
ترامپ: ما به آن نیاز نداریم، اما اگر بخواهند بفرستند، خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66367" target="_blank">📅 18:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06239668e.mp4?token=uctMIs82sHRVqQIrUwK3hxUpt202z0GZBMWrQKjX_CrSkY1AAI50XLKbcukw_N56A5PLK6R6Y73GnskurbwnvehRddkG6CaCKOV0TA-AMZeYYIC1srDp8uYjUmiJzBdHOMuwqnHmsSjkcAPiB3dSSqnAFTsvkdqEZr1Ej-4pxdCNWOTu8FMLezw1akbwm84g254RNoFPSiGrVO6eMxs8QF4f-6_w31mkGu9hlqPp7dJWDB-cbYzK6Jo7h2AtglXIhkEYZHF31y8bEnJ0dHbAFrqU3c-gSxhSjXJsn0sEh0bME-DPBj7rr91Xrf5IKevu986amOoqYDBQO9m3P6wtPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06239668e.mp4?token=uctMIs82sHRVqQIrUwK3hxUpt202z0GZBMWrQKjX_CrSkY1AAI50XLKbcukw_N56A5PLK6R6Y73GnskurbwnvehRddkG6CaCKOV0TA-AMZeYYIC1srDp8uYjUmiJzBdHOMuwqnHmsSjkcAPiB3dSSqnAFTsvkdqEZr1Ej-4pxdCNWOTu8FMLezw1akbwm84g254RNoFPSiGrVO6eMxs8QF4f-6_w31mkGu9hlqPp7dJWDB-cbYzK6Jo7h2AtglXIhkEYZHF31y8bEnJ0dHbAFrqU3c-gSxhSjXJsn0sEh0bME-DPBj7rr91Xrf5IKevu986amOoqYDBQO9m3P6wtPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا می‌خواهید اسرائیل عملیات نظامی خود را متوقف کند؟
ترامپ: من می‌خواهم اسرائیل بتواند از خود دفاع کند، اما همچنین می‌خواهم از تصمیم درست استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66366" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OB7hPiUD8KtN18FF4BRClRpLryFsJ2Mpa-HZ375en1P3WAZ4NB5DNSY3xhTeYYX838pHFIKlXxsNNGCzOk4EF3jztwwIUGdJPaIsLZLyM2ODnivDwu4UCp1e9juwE3FYfr92JesnJ5yPYMCyTr8eLvk0mH501wGLN6bHce9b9ONhpPKD0jGxx1jAb3S8WmqeOxhstJmRyaBGO0WMeszxJZmqODRFE2UbokJQ2vti_23XF_t0MJk2w9XXTu7ntmQvFUJU3bMfGkDMvbsfSJdS0ZdhrEBonV6c-D81PDfl86GlFGPPGRzVcUjxj75B4xC9K6C89VuSeN28dtBZ4hBX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت سوئیس:
بیش از ۲۰۰۰ سرباز امنیت محل امضای توافق ایران و آمریکا را تأمین خواهند کرد و منطقه پرواز ممنوع برای تضمین امنیت اعمال خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66365" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWxfD1hiU6-2m9FnluXx_af2wQ6v3389-SDMTNjEHnhvjyjvuvb-LDKBHHMwiOUU7jpqInYkxUIHb1MWsWVmDMDADl--psRsMLa-nLjXLIDa-JPURlwEfCNmGFh6-jUUlNBfxfqLiJTa0y_bLhwUvsQ8CR3EcTZBKSxKeDjExJuk_aT3mkiXwfspk-_fK7Sj_ht_zY9a4QD6Kqa19mIYGL4j996_bPui7le9_6U0Zqz_hvQIiZiYqHEEFauY5MGQ4HUs3TELJSP2a4qNCET75kJTrM-xZouQtF5mv66ob_X5QM4uNTrM9BHyBtAzfyuZNhvVsFCjNJ1FAeEETYL-iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66364" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66363">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ft2rPE6SR_Lnkz2-XSnn1wkmYeXVvgy7Z2zud4jnC8BE8mPwUZcbLE5rv9BlBZ_ptrFhtVD4sDY0d40KmoXOAuT-9soclIGCekxtLCob3TEnjyp7QTus54A8WCJI-u-PjNGuVo9B8iiCsSBhsPqBRZ_GiA94DOPXP7Ky_KY7-oPMOkgUdapMHnUK61yo4i3WJBfKL71L5ftZsf9BlGxBhg3j9NB6ro5PXHMLROukJy5eem5krbW-PidEAcDz3chMRFsE3u6VS8kjNr5VG3ZYz7yFbhdBYWY4iquyQaFWR9787BpRLbGijHaL_lg1RHUPYcB38WYpb7Nt7RYspJOdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ در تروث سوشال:
۴۵ دقیقه دیگر از فرانسه یک کنفرانس مطبوعاتی خواهم داشت. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه برمی‌گردم! این سفر موفقیت بزرگی بود، اما چیزی که بیشتر مردم می‌خواستند در مورد آن صحبت کنند این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد! اعداد و ارقام بزرگی در همه دسته‌بندی‌ها برای اقتصاد ایالات متحده با تعداد افراد شاغل بیشتر از هر زمان دیگری در گذشته. بیش از ۱۹.۱ تریلیون دلار در ایالات متحده سرمایه‌گذاری شده است، کارخانه‌ها و هر چیز دیگری در حال وقوع است، اما مهمتر از همه، اعداد و ارقام اخیر بازار سهام به دلیل توافق بسیار بالا هستند و به همین ترتیب، قیمت نفت در حال سقوط است!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66363" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66362">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66362" target="_blank">📅 17:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66361">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66361" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66359">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66359" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66357">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoN0fBhuY7IL1OkI3-mAD7XvPtJ3e8xZhUQd8fjcMMGAnDltXkyguAhyz34WoPYYCQPqXaohn6pB3iZtHsL6yQpfc21DSpYVI_E_qa8uxqOudD4PFt2rZ-xh7H9-AADlRplQpZbEoNkqcbe5ZB1Vv_hgvwjEEbNPKjj9b5vGSevaERJ9SsXfS5H8bem3v0yiIohS_HzMJPSbeA4vm3YcBl9169AIycQc_BRSNJYZWB_zJTD96zDy7WgmbQtFXHvZk1MLtBJiWIhB4VWMcfV1R1-wtOTGiA3A5wm7cXXM3pKbg7SwxmGzrXb3sRXmsB1zevUsnjUmnxlePd1W4JXX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145629d21c.mp4?token=iheC4-glJGNbo8YExoMC_nXBkR9Bt58Jw06dAoWy2-Pz4OiugyN7Aa3jodKtprScix6rTSQ56LnCwPyJkYC2nPPlqNRNoH5LplwZ-P19Nn0Ye8TFIyyO3-sPP_ckNmJnXytlcelhXnxfIbRgaAHqXKRNlXu90Goks8_q1fETc5KIZMVaTUIbWQxrmDZwewy9qk1teQc1DRsI8HJjqmNwB8rXBuwzLmjWzsRhHddPvVxnv2CHp_ZswdYu5xRVnoqe8Ahe4CCFIw_tZNtNxKmaSuZ1hO9WgQpMGRbBP8bWUtG7KPp5qEPbV_HOLssCVNGPO19eHMdLgsmcEGc5zEAuzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145629d21c.mp4?token=iheC4-glJGNbo8YExoMC_nXBkR9Bt58Jw06dAoWy2-Pz4OiugyN7Aa3jodKtprScix6rTSQ56LnCwPyJkYC2nPPlqNRNoH5LplwZ-P19Nn0Ye8TFIyyO3-sPP_ckNmJnXytlcelhXnxfIbRgaAHqXKRNlXu90Goks8_q1fETc5KIZMVaTUIbWQxrmDZwewy9qk1teQc1DRsI8HJjqmNwB8rXBuwzLmjWzsRhHddPvVxnv2CHp_ZswdYu5xRVnoqe8Ahe4CCFIw_tZNtNxKmaSuZ1hO9WgQpMGRbBP8bWUtG7KPp5qEPbV_HOLssCVNGPO19eHMdLgsmcEGc5zEAuzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جنگنده‌های اسرائیلی مناطقی در نزدیکی کفر تبنیت در جنوب لبنان را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66357" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66356">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=lhUXqb7Lxd36XD45mN52mFY0GjVhAzBhcqKjwHRUH5Q63VSzW5Lhc-tRU-sAQWzIWRn5tMC6KuOC3R6W4j_saPgHBvXFv_A0yzUaCuKndmJupDUkf3wI7QokH0FehHHO6gnScX-bY3Ue19ZvH7VWQeRS3ouUQT4VpHfkANa95Ux4P_Vtb6VbjfB4nBnIoaf_oM2cWfbE2T8BhZpyEwB0xwTKKk0BBp2v0uRNINGtvaiq8KM_B3VmeOLGXV8m463NqpU1CTodxvqkq-bpRrYYgom7uDlLjKHEztCBoojpmDW4V78e66qvipTQImr9VmfwKIvU9Q33jh79Nup7P8X4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=lhUXqb7Lxd36XD45mN52mFY0GjVhAzBhcqKjwHRUH5Q63VSzW5Lhc-tRU-sAQWzIWRn5tMC6KuOC3R6W4j_saPgHBvXFv_A0yzUaCuKndmJupDUkf3wI7QokH0FehHHO6gnScX-bY3Ue19ZvH7VWQeRS3ouUQT4VpHfkANa95Ux4P_Vtb6VbjfB4nBnIoaf_oM2cWfbE2T8BhZpyEwB0xwTKKk0BBp2v0uRNINGtvaiq8KM_B3VmeOLGXV8m463NqpU1CTodxvqkq-bpRrYYgom7uDlLjKHEztCBoojpmDW4V78e66qvipTQImr9VmfwKIvU9Q33jh79Nup7P8X4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
فراموش نکنید، هیچ‌کس تا این حد در مورد ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری دیگر از افراد انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66356" target="_blank">📅 15:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66355">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66355" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66354">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=l5qkOOCRzu7CPRHy0yY-pwT8p1JqNEMabOojDR36IryjMPXBAIf4XycD-Vi1yXlZabkgTIcTvB7XdDnJjF1wdyQR_5H8bmtIXoBJfAy-DgKi0V06XNowUWHaelPv6DUpt7AODUpvWjaViA5y7dbVOzXe3EHRl2CqFHvhd9UheQWk4o_1z5UGrCOPVpFFimNLJTFh6mgq1zMV4xGN7YHlo9naMPLUXGiuVQNkymfBWJ93nslPzvmyrZD0bG9tjocpbfZC9iRaxV4KtETNF7iNve6EY6PQBfrD1oA9HsLK2aSwfU4IYQN3gdfxjqQJVfFd6nysfyWHDV2Bv1EPfWOuSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=l5qkOOCRzu7CPRHy0yY-pwT8p1JqNEMabOojDR36IryjMPXBAIf4XycD-Vi1yXlZabkgTIcTvB7XdDnJjF1wdyQR_5H8bmtIXoBJfAy-DgKi0V06XNowUWHaelPv6DUpt7AODUpvWjaViA5y7dbVOzXe3EHRl2CqFHvhd9UheQWk4o_1z5UGrCOPVpFFimNLJTFh6mgq1zMV4xGN7YHlo9naMPLUXGiuVQNkymfBWJ93nslPzvmyrZD0bG9tjocpbfZC9iRaxV4KtETNF7iNve6EY6PQBfrD1oA9HsLK2aSwfU4IYQN3gdfxjqQJVfFd6nysfyWHDV2Bv1EPfWOuSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: «می‌دانید ایرانی‌ها چه کار کردند؟ آن‌ها به اوباما خندیدند و به او گفتند احمقِ مادرجنده.»
پرزیدنت ترامپ با اشاره به نحوه برخورد رژیم جمهوری اسلامی با دولت باراک اوباما، گفت که مقامات این رژیم به اوباما خندیدند و او را «احمقِ مادرجنده» خطاب کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66354" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66353">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=QCEMlPLjVKYytcCWwM5JyQl_psWIGGvXShm5JNe_P4Dv5ghMfmnL0CozD8sZYUHlRg9UcDaZJkA96y5fQrMKPVy-lXRkIzPoflkWwQ-Yr8Jr3Et-K9TXNDIetC7ZiD78sK_zPdpuL3tHssxSuOPGKzsm3PTYAv3bCs-1Q6Br89U0V4WaoZK-8KyWjKEffszkWTwqL-jWp25czUuj9SSBb2nbLDXMwCrICyGhnG-7HhlRCrmRKb1XwaMK17IiIYTz6lOywLiRlUY6eWqmjDj8jtjUB4wjIU6s96q6YQbNOdMBj2KEg9RBabVaodyR079uQ1ukyD6-FFHomZ144Bi13w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=QCEMlPLjVKYytcCWwM5JyQl_psWIGGvXShm5JNe_P4Dv5ghMfmnL0CozD8sZYUHlRg9UcDaZJkA96y5fQrMKPVy-lXRkIzPoflkWwQ-Yr8Jr3Et-K9TXNDIetC7ZiD78sK_zPdpuL3tHssxSuOPGKzsm3PTYAv3bCs-1Q6Br89U0V4WaoZK-8KyWjKEffszkWTwqL-jWp25czUuj9SSBb2nbLDXMwCrICyGhnG-7HhlRCrmRKb1XwaMK17IiIYTz6lOywLiRlUY6eWqmjDj8jtjUB4wjIU6s96q6YQbNOdMBj2KEg9RBabVaodyR079uQ1ukyD6-FFHomZ144Bi13w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما مردی به نام سلیمانی را از بین بردیم. فکر می‌کنید اگر او زنده بود، این اتفاق می‌افتاد؟او یک نابغه شیطانی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66353" target="_blank">📅 14:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66352">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=D1NS_WPALQU62rWb7srgUlJGdrrwFyr9xpf-8THygp6RLS_DoztdJ7YCxT_DUB21aGC0kt-36H0UsMHMWWyu9hx7udGhWL6NeuvHHvkUlcIYT8rs_v8GRDGfLmMHSKJzD3g2LxEma_DcA4E5aJSABQtzHt20b3iPF8hZ1tmKA5SidK68Ofu-VNpQzgop3NJBwbPxhwPmUxTQt3yAukDR2RA-ikB4c7UBUpXj6iD2xRxZDN1763J3CW_Yt--z3tdM6kwS_nTzFJByMnQo5jzldD4ZAGi8dLRME8_j9hXa0vKyU0jx2c_x3loIG7X1YG6lmzesiociJj4HOKtNoDrb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=D1NS_WPALQU62rWb7srgUlJGdrrwFyr9xpf-8THygp6RLS_DoztdJ7YCxT_DUB21aGC0kt-36H0UsMHMWWyu9hx7udGhWL6NeuvHHvkUlcIYT8rs_v8GRDGfLmMHSKJzD3g2LxEma_DcA4E5aJSABQtzHt20b3iPF8hZ1tmKA5SidK68Ofu-VNpQzgop3NJBwbPxhwPmUxTQt3yAukDR2RA-ikB4c7UBUpXj6iD2xRxZDN1763J3CW_Yt--z3tdM6kwS_nTzFJByMnQo5jzldD4ZAGi8dLRME8_j9hXa0vKyU0jx2c_x3loIG7X1YG6lmzesiociJj4HOKtNoDrb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:متن نهایی نیست؛ این یک یادداشت تفاهم است.
اگر من آن را دوست نداشته باشم، ما به پرتاب بمب روی سرشان برمی‌گردیم.اگر آنها رفتار مناسبی نداشته باشند، ما دوباره به پرتاب بمب برمی‌گردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66351" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66350">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=ns31TWd-e6Rl8GLRvnFETnB5LKqETNvkpDI-slBsEy9rvthxb089Is9JKr4wFj9P0M9aTdZgEwT5Ujqanj6D1jEjHQ0IqKwByJRwjSY6ACFPtKlVyF9Rqp65w2kUGO2oZVXBMvVSX-4lYNCW3whl9g1k_jzcq1-CoeLFwGMoh0593_Wv3bcw211lTkD8wqDvF4B1q-YH9xxjOe4YLhZt07-4dSeAcQxOGjMRnE7UHKUrId8-IfaMqfxjUR1F5-ZaXlFOlp8qk3LleRXMjuh5SPi4l8gtVUrSJnDhzEkIscCxYqWU8HYBINdAM7EeW2tBstiQeRTkU5mY_tG1PwvEiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=ns31TWd-e6Rl8GLRvnFETnB5LKqETNvkpDI-slBsEy9rvthxb089Is9JKr4wFj9P0M9aTdZgEwT5Ujqanj6D1jEjHQ0IqKwByJRwjSY6ACFPtKlVyF9Rqp65w2kUGO2oZVXBMvVSX-4lYNCW3whl9g1k_jzcq1-CoeLFwGMoh0593_Wv3bcw211lTkD8wqDvF4B1q-YH9xxjOe4YLhZt07-4dSeAcQxOGjMRnE7UHKUrId8-IfaMqfxjUR1F5-ZaXlFOlp8qk3LleRXMjuh5SPi4l8gtVUrSJnDhzEkIscCxYqWU8HYBINdAM7EeW2tBstiQeRTkU5mY_tG1PwvEiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:
هیچ‌کس نمی‌داند این چیست، اما توافق بسیار قوی‌ای است.
به نظر می‌رسد اکثر مردم بسیار خوشحال هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66350" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66349">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=oxbaA7uYtyub8u_W0ObSz8v7fcUCGOZzi-oJf_HOJXxrKA5X2AQTZMcaTb6gFEXYYLNllFa6Bp3l0sdvna1PkoHRRsW0zjrN7oqsFj1xmzndX-Uf8o07YD96VCXLDze7M5pT-Tu_WbVT_6zTV-b8UiVRrhF4Ms95AIE6_hQ-FFHl_SmnT8DMMNf_mQhsbHZIfvEazi-1IrkH5AR82V5Cpv48D-B5sEKwUhcU9MR4Pwh3NKFTtFqyKquq4cILwrPhd1tA4eTMQqT46yj3XwLl7930sffwzFzQyk3Pvjv4Lc7ljFNwpaey7CepC1bcJaAqVQCAAMlttbPrOSOkk4Cf3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=oxbaA7uYtyub8u_W0ObSz8v7fcUCGOZzi-oJf_HOJXxrKA5X2AQTZMcaTb6gFEXYYLNllFa6Bp3l0sdvna1PkoHRRsW0zjrN7oqsFj1xmzndX-Uf8o07YD96VCXLDze7M5pT-Tu_WbVT_6zTV-b8UiVRrhF4Ms95AIE6_hQ-FFHl_SmnT8DMMNf_mQhsbHZIfvEazi-1IrkH5AR82V5Cpv48D-B5sEKwUhcU9MR4Pwh3NKFTtFqyKquq4cILwrPhd1tA4eTMQqT46yj3XwLl7930sffwzFzQyk3Pvjv4Lc7ljFNwpaey7CepC1bcJaAqVQCAAMlttbPrOSOkk4Cf3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یسرائیل کاتز: هر کسی علیه اسرائیل اقدام کند، بهای سنگینی خواهد پرداخت
🔴
وزیر جنگ اسرائیل هشدار داد: «هر کسی که علیه دولت اسرائیل انگشت و دست بلند کند، چه در غزه، چه در لبنان، چه در سوریه و یا هر نقطه دیگری، می‌داند که باید بهای آن را بپردازد. اول از همه، آنها زمین خود را از دست می‌دهند و خانه‌های خود را از دست می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66349" target="_blank">📅 14:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66348">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
