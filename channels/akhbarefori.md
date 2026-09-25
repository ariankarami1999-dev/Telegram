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
<img src="https://cdn4.telesco.pe/file/eoeNUCF0Uvh3RCp8aQpxbBrAIPMFCLpXN8oZ1WYxw916wnxdxdNUc573-oOesFzKZ4hoQiYb34mm7mYypWOL8e4kap6xSkkqYSIz-GPk3mZ6BlEEd5gd0uERoycWGVe1K5Pai4YkTT38LWR490jXOuorxj0UxVC5-iB6hfFjnYJLPcmwzngT-AMCObtmDYY4gtggwIOWZNwlWHlG8rwH_csz8ZzLAWCVctzkBbEYnf5f2yB-XTyBFQVilG7QilJ15GkqaaZk8Q4b2PxxvEsqHJyQGxWxJLNP72dEOfyhjWtohOD-HAEJqFj-YVMVrVSBgJnCz9iZmyIqi50u90dR5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 00:06:01</div>
<hr>

<div class="tg-post" id="msg-693011">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ec3c93e1.mp4?token=C0aeoM6SlOpqelSNIek_ofppIdZsAZEolWadg4q_-MOD_6ghK3spFRfXOIplVY_7172qxn_BrDnMTXEpvTzoZeAhbVe8l5PUeSCEeWqmSnp2r9CXpl_Ufj_hbKXWdp54KovOZ-4lhGyCOkfCGmNJyZABAWR8MdunvCuhH2gMNXctkcSQF4OU-mK_Xd9vHmtdpWlBjQq_obNs6mkyHmTGvno6sqIySYmlRn54KPKdfqklaxnheqzpbTpLLU-dT32OD_szpJin5eiKnToPDb1HIixr2Sshkw2WCd6VHUyw4EEc9pWAnnl_hj2QYx-f-A2c4e_NVPUZVlccJiQ4GJhnOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ec3c93e1.mp4?token=C0aeoM6SlOpqelSNIek_ofppIdZsAZEolWadg4q_-MOD_6ghK3spFRfXOIplVY_7172qxn_BrDnMTXEpvTzoZeAhbVe8l5PUeSCEeWqmSnp2r9CXpl_Ufj_hbKXWdp54KovOZ-4lhGyCOkfCGmNJyZABAWR8MdunvCuhH2gMNXctkcSQF4OU-mK_Xd9vHmtdpWlBjQq_obNs6mkyHmTGvno6sqIySYmlRn54KPKdfqklaxnheqzpbTpLLU-dT32OD_szpJin5eiKnToPDb1HIixr2Sshkw2WCd6VHUyw4EEc9pWAnnl_hj2QYx-f-A2c4e_NVPUZVlccJiQ4GJhnOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این قابلیت رایگان ChatGPT، هر دوره‌ای را با هوش مصنوعی یاد بگیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/693011" target="_blank">📅 00:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693010">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toYfMR1Hj5g_KoTMT1dKhKxwGGZlnCz_jg4sAZ0Dwh_V-tNWqDD9pYBqz2OU33hTMpKHDTWA5xZCdOliB1WD616_GgZiZfL5SGySOwvU1SNW8dowKL6_h0gOC5ZOz-IFY6hFJXz3C6FwzP1w9vE0dEirEkwfPcFjVunNHUDCciiqWazappxct38l2YOBykQqtxM8pGyjPBxVV4BVupk5MycH2HQzdGlUFf-eCiflINqXhyhV6CQNi_IDJaJvjXvUZJfonkIykW1WBJvK0QnzaiPw0xK6ObJH3bOSuUZkLUz9CIXBLysp8ILKW0gR8ryb3y93ib5zZq5LBoWXMo7pzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/693010" target="_blank">📅 00:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693009">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
عراقچی: در نتیجه اقدامات آمریکا و رژیم صهیونیستی، بیش از ۵۰۰۰ نفر در ایران شهید شدند
🔹
اقدامات آمریکا و رژیم صهیونیستی علیه ایران، نقض آشکار حقوق بین‌الملل است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/693009" target="_blank">📅 23:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693008">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
عراقچی: در نتیجه اقدامات آمریکا و رژیم صهیونیستی، بیش از ۵۰۰۰ نفر در ایران شهید شدند
🔹
اقدامات آمریکا و رژیم صهیونیستی علیه ایران، نقض آشکار حقوق بین‌الملل است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/693008" target="_blank">📅 23:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693007">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki2W5CuV8KOhdXN0O9_hW9auspSZz0V_A4S_H8nlu2m-2yOrWWdvcg131vFh8nwMOMypOMOHKLFVKR40nXhHr-aBrNm2iJaOSTToq214F2PWfjM9ACh_vgQy77UVCZQYoVuhD87cAzzqqOijDQ55fDCWJsk87FLhfUQhGO44auKkMjqPUp2g9nSwI831vcOQesSM2SBDqD4r9IKXnZybj9_RmwTA8GrthUN0uGlrCfJ7fI6Dm-x05CMhqH1lABAB2Gie_M6viuo5gWVoOkTzTvFJ9xdnpZlq-6XQaLPY_rzDycWuAk4tsYBP5AH6WE-pV56PHt3_aOOZv5vLyxyixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
سی بی اس نیوز نیز با پزشکیان مصاحبه کرد که جزئیات این مصاحبه بزودی منتشر خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/693007" target="_blank">📅 23:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693006">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c113eb8d81.mp4?token=C11hqzqHwawrD-OnJ9ddZJ2odPtUAA0VUuMBOGzJ9Y0MzVXCLOQ8UlaVcXxvdmAc_POl8QHh4yxZ5gLI5nGWi4oRBIhUlCMGCkVAXDBr9IF5ecS_rzDcn74ot0FMMs8K9vHKtuCt4CJ7aGy9hTyNlUDKXz8E6LuUjTm3QJmKPd6RG8BvlXb3CYjtKJ0o8IH9yLuSKtDxyxP_6z34qXV7diBTUmx6z2B9N2G5cVYPsHFfST52AbPZpiR2PLF87IQagBzVbKj4nwOaqyLFWvFlJS9FAiqbY9JDoo8Paw7PhiESOCqfyxORGo5UHasc1585p2TLpcTB6RP9_BTxcwcaNGDbEVC80wa5pEvpH_j77jev0s3V4WcvP78uHpipu_xsT5sIoLWYxL8H-HsEtX6VsulIa3z9Pd__bhydtBT-WynHigCYRt5JkWkyBi5TOaCvJbk_xOENb3eSqdcNtCjG0GzWdEJcA7INpq9QWvS0sMsQ2_eNtouQmG3z6FFhYaG7g1wczM9AREzLWL89tKOuxpEcz6HrMnjrblutCeSARklvrmHcq2PPU6t-UzETzKhqf1F4KHZCcyiPPtk53VDFs1MAqEIypSzFgL42uIEavapGAKcLM3DHHyqvmhCHZsPQVS2Zcobz5ID8Ld07Of7pZSlyQZFNKc0y0a3C3k1BFQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c113eb8d81.mp4?token=C11hqzqHwawrD-OnJ9ddZJ2odPtUAA0VUuMBOGzJ9Y0MzVXCLOQ8UlaVcXxvdmAc_POl8QHh4yxZ5gLI5nGWi4oRBIhUlCMGCkVAXDBr9IF5ecS_rzDcn74ot0FMMs8K9vHKtuCt4CJ7aGy9hTyNlUDKXz8E6LuUjTm3QJmKPd6RG8BvlXb3CYjtKJ0o8IH9yLuSKtDxyxP_6z34qXV7diBTUmx6z2B9N2G5cVYPsHFfST52AbPZpiR2PLF87IQagBzVbKj4nwOaqyLFWvFlJS9FAiqbY9JDoo8Paw7PhiESOCqfyxORGo5UHasc1585p2TLpcTB6RP9_BTxcwcaNGDbEVC80wa5pEvpH_j77jev0s3V4WcvP78uHpipu_xsT5sIoLWYxL8H-HsEtX6VsulIa3z9Pd__bhydtBT-WynHigCYRt5JkWkyBi5TOaCvJbk_xOENb3eSqdcNtCjG0GzWdEJcA7INpq9QWvS0sMsQ2_eNtouQmG3z6FFhYaG7g1wczM9AREzLWL89tKOuxpEcz6HrMnjrblutCeSARklvrmHcq2PPU6t-UzETzKhqf1F4KHZCcyiPPtk53VDFs1MAqEIypSzFgL42uIEavapGAKcLM3DHHyqvmhCHZsPQVS2Zcobz5ID8Ld07Of7pZSlyQZFNKc0y0a3C3k1BFQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ مدل سس سالاد متفاوت برای روزهایی که از سالاد تکراری خسته شدی
مواد لازم برای سس سالاد اول:
🥜
۱۰ عدد بادام زمینی
🫒
روغن زیتون ۲ قاشق
🍋
آب لیموی تازه یک عدد
🌱
شوید تازه
🍅
رب انار یا سس انار ۲ قاشق
🍇
سرکه بالزامیک ۲ قاشق
🧂
کنجد یه قاشق
🧂
🌶️
ادویه نمک و فلفل
🔹
مواد لازم برای سس سالاد دوم:
🧄
۳ حبه سیر تازه
🍾
سویا سس ۲ قاشق
🍇
سرکه بالزامیک۴-۵ قاشق
🍯
عسل یک قاشق
🧂
کنجد یک قاشق
🧂
نمک
🌶️
فلفل پاپریکا ۲ قاشق
🔹
مواد لازم برای سس سالاد سوم:
☘️
جعفری تازه
🌱
ریحون تازه
🧄
۲ حبه سیر تازه
🫒
۷-۸ عدد زیتون
🫒
دو قاشق روغن زیتون
🥛
۳ قاشق ماست پرو
🍋
آب لیموی تازه یک عدد
🍇
سرکه بالزامیک یک الی دو قاشق
🧂
🌶️
ادویه نمک و فلفل
﻿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/693006" target="_blank">📅 23:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693005">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔹
از داغ‌ترین خبرهای امروز غافل نمانید
🔹
🔹
ماجرای اشیای نورانی در ایران ادامه دارد | آیا پای سلاح‌های لیزری آمریکا در میان است؟
👇
khabarfoori.com/fa/tiny/news-3247768
🔹
آمریکا و ایران به اتاق مذاکره بازگشتند؟ | خبرهای ضدونقیض درباره میانجی‌گری‌ها در نیویورک
👇
khabarfoori.com/fa/tiny/news-3247729
🔹
جنگ هوایی ایران و متحدان آمریکا / ایران به فرودگاه‌های کشورهای منطقه حمله می‌کند؟
👇
khabarfoori.com/fa/tiny/news-3247842
🔹
بن‌سلمان خواستار ادامه محاصره دریایی ایران شد | چرا کشورهای خلیج فارس از ترامپ می‌خواهند فشار بر ایران را حفظ کند؟
👇
khabarfoori.com/fa/tiny/news-3247829
🔹
گوشی ارزان شد، اما نه برای همه | بازار موبایل در دوراهی قیمت | پاییز متفاوت برای گوشی
👇
khabarfoori.com/fa/tiny/news-3247770
🔹
صفحه ویژه اخبار جنجالی خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/693005" target="_blank">📅 23:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693004">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
دیدار پزشکیان و دبیرکل سازمان ملل در نیویورک
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/693004" target="_blank">📅 23:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693003">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سخنگوی سپاه: تا تحقق هفت شرط ایران، تنبیه آمریکا ادامه دارد
سخنگوی سپاه:
🔹
موشک‌های ما قادر به نابودی پدافندهای چندلایه آمریکا هستند. آمریکا با وجود بزرگترین نیروی دریایی جهان نتوانست حتی چند ساعت تنگه هرمز را باز نگه دارد و کنترل آن در دست نیروهای دریایی سپاه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/693003" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693002">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f901180784.mp4?token=EU-avO-nhXDP3AgElZafwflPPqh5mvqrMQCONXc47UU-8oivC7XBIuwABHYKRcQbZME8T-fEp3N7nUH30unpQk79FxRI0FZLqVwCNK1PJRolYaHzuChyiQDKhCcWkhxhnU1Qdz50_0mRTnXW1W_B93KzllRBR-ifWcYFa_xB4QDVUUh1K0EkQIqjVTOA3O-9mSwfq9ndT-TED9cSDI-blZgksjwxMey3xj6AED2H-8fLlrSdtZ1t7DZ5QJOEBHo0oBjuTIYMwWeWSt_SZHi3shq2GpS8QhCZuxV7hRDNkbQRKssdGVkPxKRbkINAQ7_gDxQxCKRSsLX_-3t_KIBjGKnBM91jjMarLl6Rggwj-4hI4PkOjqX5r-TStPgYNnY9d_LKwuwaQiGHbf_4P1gfXxocjNXgOmJPSSr5cDzlbELAWoT-u_RHEThOXbWKNmJUVYPL_wwJxj_-0YWxQcHJvlD_qQNyG99eWKdGRh8qSxR3-Fanelg4KoG0zrb_bIPRka3rk_KPGREwIQT2B_tfoUbz-t9c8XacSZtyqDfGmj1P4suWYE8LYVDY_d8c1pCvJvfZ3_8khuiFgB3fhEGA1QRV9gYM9-JkBjAV5W64ab2liVTU1w4iSjRyaLrswdzEMg0GoBPV3VyYClby6Bm_otAaqNc2zqqC2RJJNTj2SmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f901180784.mp4?token=EU-avO-nhXDP3AgElZafwflPPqh5mvqrMQCONXc47UU-8oivC7XBIuwABHYKRcQbZME8T-fEp3N7nUH30unpQk79FxRI0FZLqVwCNK1PJRolYaHzuChyiQDKhCcWkhxhnU1Qdz50_0mRTnXW1W_B93KzllRBR-ifWcYFa_xB4QDVUUh1K0EkQIqjVTOA3O-9mSwfq9ndT-TED9cSDI-blZgksjwxMey3xj6AED2H-8fLlrSdtZ1t7DZ5QJOEBHo0oBjuTIYMwWeWSt_SZHi3shq2GpS8QhCZuxV7hRDNkbQRKssdGVkPxKRbkINAQ7_gDxQxCKRSsLX_-3t_KIBjGKnBM91jjMarLl6Rggwj-4hI4PkOjqX5r-TStPgYNnY9d_LKwuwaQiGHbf_4P1gfXxocjNXgOmJPSSr5cDzlbELAWoT-u_RHEThOXbWKNmJUVYPL_wwJxj_-0YWxQcHJvlD_qQNyG99eWKdGRh8qSxR3-Fanelg4KoG0zrb_bIPRka3rk_KPGREwIQT2B_tfoUbz-t9c8XacSZtyqDfGmj1P4suWYE8LYVDY_d8c1pCvJvfZ3_8khuiFgB3fhEGA1QRV9gYM9-JkBjAV5W64ab2liVTU1w4iSjRyaLrswdzEMg0GoBPV3VyYClby6Bm_otAaqNc2zqqC2RJJNTj2SmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه انبار مک‌دونالد را در اطراف کی‌یف، پایتخت اوکراین بمباران کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/693002" target="_blank">📅 23:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693001">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
وزیر خارجه عراق: با آمریکا درباره مسئله تحریم‌ها گفت‌وگو خواهیم کرد تا امکان ارائه خدمات به پروازهای ایران فراهم شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/693001" target="_blank">📅 23:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692998">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCrUBLWEYnCzT6TqlTVZ6SHOKbqnetYN8-MnVh-IOv1B2zKv-5DHCfmLDVopzGHDHGhXEs9dL3ByYjiedI-OLZ7vW3NG4WhVKXoxtVOTxNVBxmnM3Ugk3_puopDFADU-2ZDgdcTtbiYbsRJNS-o4FHpQrr-kM6AS4gBUboDgRyepu3X6i_EhaNawWdcsTGruWWip-I2iDLkkfd98mHF8v-f70lBneiT72HNRnmOGfrrcKLz7_FkSooxMbH1dg9hXv0DI3On2wijxBwChrG5ZTBQVlP-YXDuk5JoVVteox64TvU5ywFIZQZ5vNbTWBio569LezMoVwtP6Aitolz7iqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQ2YzfMek06Hs3VarbphES6jI2FejWCbc__-EZQMbbSQFn2GATEvyILffe6nj6-Prs4JH-RjsgPDLYR41RhLWwxwp0T4mwqmq1D3D47JMHfRCe_h33fhTLxQujJQSn-cO62jnvDPlDQ74yoG4unExv1VaEG846rePN-ZITAlqjW-Pk8ngUQ4pWkIyvKDbPQvSMe6J3raGqqaQf7WOlCfwTPIfsVF3GcLoeOUzKmN40pE1xqrwpwQot7f2HuHW8NnXLkxlmLo_q8pORBqGHcSAu1aXZ-CLsfiJcpYewXUWPFdBOIvBJmK1s2blxM_d9HvdMCuOFsmwX_G7LHdUAgH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vF3r8JOiEGm54tyNx0xcIKE57FWahLE27wAUCUmX7dazHfi_sJaZvh7L2nk44MoB3_HqMQjp7kXsR5n0UrPwHXAkWIIHfKZZCgscKYjcx3QR6JSKyuabVxwz24r93XpaAZffy_uFbofF1G85Jlm075fxMQGFuiiqeVoLkyjC8-jz_R_Vh_klhffOiz6emhp97WVakcElBCRcpzPXH1X6q-IFkYbASUZ3IKVxE7M65t3xi4zEMXbNNSoSW8B-FIOiyIygrOdQXgGocyNn5urvjV5mDOPwJWB7uXTyalmoTlMRN98MsitA8NXVFxaPTngyAvMx0J_uc6Izc7BImfOCOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قالی قهری؛ فرشی که ناتمام ماند
🔹
«قالی قهری» اصطلاحی برای فرشی است که به هر دلیلی ناتمام مانده است. با شنیدن این مفهوم، این پرسش مطرح می‌شود که در هر محله از تهران چند «ساختمان قهری» وجود دارد؛ ساختمانی که سال‌ها و گاه دهه‌هاست ناتمام مانده و مانند زخمی باز در منظر محل باقی مانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/692998" target="_blank">📅 23:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692997">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه پنجم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/692997" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌‌ گذر از دجال
جلسه‌ پنجم: تفسیر زیارت وارث
🔹
امام حسین(ع) وارث فضایل و کمالات پیامبران و نیکان عالم هستند و هر سالکی می‌تواند با خواندن زیارت وارث با معرفت و حضور قلبی، از این میراث معنوی بهره‌مند شود.
🔹
صفات و معارف الهی با انتقال به دیگران کم نمی‌شوند، بلکه میراث معنوی می‌تواند در افراد مختلف گسترش پیدا کرده و حتی بیشتر جلوه کند.
🔹
زیارت وارث برای شناخت گنجینه‌های اهل‌بیت(ع) است که خواندن آن با توجه قلبی می‌تواند زمینه دریافت ایمان، عقل، معرفت و اخلاق الهی را فراهم کند.
🔹
زمان تحقق ظهور صاحب‌الزمان، با میزان ایمان، دعا، آمادگی و عمل مؤمنان ارتباط دارد.
🔹
فرصت توبه محدود بوده و همیشگی نیست، لذا انسان‌ها باید پیش از بسته‌شدن فرصت بازگشت، از خداوند طلب آمرزش کنند.
🔹
انسان باید از غرور، منفعت‌طلبی، وابستگی به مردم و ترس‌های بی‌اساس دور شود و با توکل به خدا، توبه، صداقت، ارتباط قلبی با اهل‌بیت و تلاش برای پاکی درون، خود را برای یاری حق و ظهور حضرت مهدی(عج) آماده کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/692997" target="_blank">📅 23:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692996">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مدیر تعزیرات کهگیلویه‌وبویراحمد: محموله ۸ میلیون نخ سیگار و ۲۵۰۰ لیتر تنباکوی قاچاق در یاسوج توقیف شد. متهم به پرداخت ۱۰۹ میلیارد تومان محکوم شد.
#اخبارفوری_کهگیلویه‌وبویراحمد
در فضای مجازی
@akhbar_Kohgiluyevaboyerahmad</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/692996" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692995">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5b79d80fa.mp4?token=MypB6vmfZspXx6RY3x59yNC27q85h1yhZjAqXXcsr2hKrJHAe5baQCkTXj56JrdVq3UdpkJPFZJ0A9zfIh0o71iJnn_ri43t8uraypl1AXSPO4H1yCZn6w2IOUcHX0tz5MlfJWtiC25Eqcg2UCHojtlBFjqRGcaTUl6jtnvvVoQrsnBB4Zdekq6N2sQvpgejNrFPewbpRwPSIOI_kz5ywh6JP2MkdH8UOkwIKShA81JgI85RpvglmfkqgaYDZWUZColtbZjhl-STko_rJCzy5x3TyaLKCRrJSlDzDzmYAeODG7KcdzTC5WOASy2YzhUqNJ4sQ7WJZ9b7fZffu9idUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5b79d80fa.mp4?token=MypB6vmfZspXx6RY3x59yNC27q85h1yhZjAqXXcsr2hKrJHAe5baQCkTXj56JrdVq3UdpkJPFZJ0A9zfIh0o71iJnn_ri43t8uraypl1AXSPO4H1yCZn6w2IOUcHX0tz5MlfJWtiC25Eqcg2UCHojtlBFjqRGcaTUl6jtnvvVoQrsnBB4Zdekq6N2sQvpgejNrFPewbpRwPSIOI_kz5ywh6JP2MkdH8UOkwIKShA81JgI85RpvglmfkqgaYDZWUZColtbZjhl-STko_rJCzy5x3TyaLKCRrJSlDzDzmYAeODG7KcdzTC5WOASy2YzhUqNJ4sQ7WJZ9b7fZffu9idUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجوری سایز پاتو اندازه بگیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/692995" target="_blank">📅 22:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692994">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0yB4du_VZ9SYdtcrouq2Vxnu0oFYWLJFJJVLRQPFw4lZAMkxgPK5hXFnu0kZykIXq_BiFqETBU4BTUroEVNP4d1WDvVzpiTK_d47Hwif5jn2hICCjTsbngTl4QE5VLv_WvF0Y2XklmijM-quUMaNPBDnMasNJPTwutF-Had2X5Iu0pWCER_-xxLfnRLjH9VMbSFvWf199NLVVYAIhZoI7C0iZSss0RLOAz_RtHcfQDk7p5sRj-fledAjwD6rwaNDrQLedW3Cj9hQT4REiMysG6v8uHXaEJhu-yLUx0QveN6agnZeCbsfh88gxJVreyi2ROkWUWzWGK1RUqMIgwXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت مشاور فرمانده معظّم کل قوا خطاب به نخست وزیر عراق: مشروعیت از واشنگتن نمی آید، از خاک نجف و خون شهدا می آید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/692994" target="_blank">📅 22:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692993">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRGix58JnfYaTXNVlxAqU3yx2RY37tYWfVEDjXppwO41Yr7FQPacLHPj2WN9IkqI1XcVqeVvchQWGKwo4CCuIPI4hjbKqPKa-_cQNlkWqskLi_YAfNQHPsCzcu4zj34XIS-JSEFOt6ruv3KKb1RENheboHvyq87KoCQekRsErhpMRrwXFnMOsQ8IuqhgFK7GAU_a6nqUeQTKrmfoNyTKaZfWeAHHwlKm_5f3vWFfdAhmjOi0bEP5V36lmfFNogbrdl8d0NQd0XjdonRZ44xjtQr5w2wlDgCvdId0q8GVcF32uCP5Yb8IwCI-L5iY-No-_0epxWXhIn4sG0EPEXnGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیرکل ناتو اعتراف می‌کند پنج هزار عملیات هوایی از خاک اروپا علیه ایران هدایت شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/692993" target="_blank">📅 22:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692992">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8nU3IhGXtjM0RWNST4N5Wy5AQxMidcEQzAQCeGLi73EiWlbqEUkGpvQYF-5PNaX7KfxEFUlrYh3bMGwOMB1tpwl__AkJOhyJx7_cX0PSvOaVJDlzZ0wGLvJ_JQDW5Jv7GUcuxi7JnGJfCs-3CQ1_D62CmjAcrUcx_x0AZrSfv5kV29ygVs29rdzmGqgAjJ3liR4XdfQ2QcsRCwQqVvg1WiU0_hPof0GwHe8FtXtYskpadzXckpsBA2dB39WJgb07HLLVHQbmEM_DK8p6Vd_gB7tXEO3mmIwRGqvoUtDicMhplC_iD1byhYRtOXBYk5kK2jaSqmNzoZKvOYSyQb4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ هوایی ایران و متحدان آمریکا
ایران به فرودگاه‌های کشورهای منطقه حمله می‌کند؟
🔹
ایران در گذشته نشان داده که به تهدیدهای خود عمل می‌کند. در طول جنگ ۲۰۲۶، پس از حملات آمریکا و اسرائیل، ایران موشک و پهپاد به سمت قطر، عربستان، امارات، کویت، بحرین، عمان و اردن شلیک کرد که این امر منجر به بسته شدن کامل یا جزئی آسمان این کشورها شد. ایران همچنین توانایی خود را در هدف قرار دادن پایگاه‌های نظامی آمریکا در منطقه به نمایش گذاشته است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3247842</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/692992" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692991">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxpBc9GRsELynpAOUJFQSIGh-1OKzBY3YXfncVACMciMOowUdYKFl6y0BMwhXziLrXNk-UrAwpITk6iJGwOQFuphp_oZzoG91VhqwiPi5ZuaFIzXFgBydYZnP9OGOYahtRlx_8lGTwkvMHfhE_MRTKbku-BbMv24hztHPTcj44_epLOpsWhRXR1dNVfgkFocVo-oqkb-BAldkNDZE2N9JKv4o85M-lk59dhD-EP6slufdfZJ5-SXJjEh47c0JiGWJRC8V7o5MgoaaLbyV29IT5WE5yBXOIOCavMjC_tp9a__q9OHhKM-6M9bObdicHC6mVS0zjyqWlwkMXuR0T0Bcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ایران بر بازگشت به تفاهم‌نامه اسلام‌آباد تأکید دارد
پزشکیان:
🔹
اشتراک‌نظر تهران و پکن در ضرورت احترام به حاکمیت کشورها، کاهش تنش و صیانت از صلح و ثبات منطقه‌ای، مبنایی مهم برای همکاری‌های سازنده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692991" target="_blank">📅 22:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692990">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLSWIFda9P2eFppvrCTRnjzykyVDBxBnKRWL4NxZiGRXT3xz8VIW-UNfxZil2CFq_O_Z1lpVJJOm-FcU2NmF61zQyVzILc2lUg5M8iOlxaoh2MvbVLXQu2kMTW7mr8YpnW5ruBX2v6DxXySP55ng4-EZmMm4_i_w4qcIa03fhgsouCYqlENpXFz-KPIaM0Xn6FpRf8wRm8FNCkNPUieArpKZQzftMb11NaIBaPpdz-XDtB4u5neKuJbZFu99i6j-NSdG6Drf7OaWTpnXMLhbdM9tnt0TOoqZl7dX55ynIzukK5FGEfWOr7NIgJxr_5oXIToCRxJgXy9WUgnuI2plWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ نشانه‌ای که متخصصان مغز و اعصاب می‌گویند نباید نادیده بگیرید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692990" target="_blank">📅 22:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692989">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN-vbfxQOt5BpgoiNXJalzkABlPoAf5yXfVOq2-CoBBGTt7S3WW5DCNLl5eORoH60AJbqdv_4Su8FpQrae5xNQ0lkMIzD3CVDDlijNSiq-ZjUZVLLlALL6sL8mSz9qnMv3noYfSgMws7HHuKYtT-GbuAZMWiz1vPKYLAeEpIYuQ2MiXI97_T8zXNdbBQoiJK5SJizY5Ps4FN4Ovn8my7SSOGBhR2Ecoe1U_tJcUopDpPzBl6iSm4Aj_cgHAgr7S5iEIKYzD8n7T5XSga-JMKFaeRNGdWQb8ygG1_YrAX8Lprlt2zQKaJOlcKorClcVrvKx-hFknKcdhlHKsMK_XLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منبع آگاه: ادعای آکسیوس،فاکس نیوز و الجزیره دربارهٔ مذاکرات ایران و آمریکا کذب است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/692989" target="_blank">📅 22:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692988">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRVlW3jQBd35YeaJzcJpKT19SnHE0hrcON5q8kXIG7BoZ1uO79B5t6Z4COpo7IPPBeJdUSJEZF2fEyRkJrNekFlcR4YQUp5RYiY1xHhk_GW_jzqjtZxctDzGTgpSR3Hod0gYR2_K_jiJW5xoGBfpdZahs1rciSTlQ6DcBvXJKm6DWEu_Ulp3twVYH2dQvI5_js3j6OyhAXADLPdhz7AI4K23-IvQ-z2pzrOOtNhibezSaNZ5KF1oqINU2F4mKXUSMqLLwvfuakKab6CAEAovKSUX5WcpsvzfvwDhmaEmbx6o-vPCQBiNxkuRmPjOdpM_8ImcpeBpSM-URzUFpdqDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درگیری قریب الوقوع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/692988" target="_blank">📅 22:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692987">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
کلمبیا به طور رسمی روابط دیپلماتیک خود را با ایران قطع کرد
🔹
کلمبیا در این بیانیه ایران را به آنچه «ارتباط با گروه‌های تروریستی بین‌المللی» خوانده شده متهم کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/692987" target="_blank">📅 22:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692986">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQUJwMyZoHS-01412aTw73VffOm73cgH4flBtpdvYt9uALI18fztZp9m6MsgJagNco2zwoFEA9qOzlWtB36IMBO3m-jmlYETg1Ya7ICb1IL8u0mmc29Yp-cWYA92L3jNgf6UJFJaWm_M6Sk0mTOsVKb8eR2e9jFzFYiCExh8Pra2LdQ1UH0ynLqt7n1WnFj2S5WfkerSWiuh9D4z6uN7YtdpUj4tv9K1BHuuz5Psoav8scpF-g8Sp62frw0Vej5JpR3eHIbcy484gn2PNsTjTwupTdyV25945q23yj2KM_NMY3f2OdRXpj5MgVxDD6bKebVnHx6Yi5I0-4_Dd9HIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمبود ویتامین D؛ علائمی که نباید نادیده گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/692986" target="_blank">📅 22:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692985">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
صحنه‌ای متفاوت از آغوش گرفتن در یک تئاتر که در فضای مجازی وایرال شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/692985" target="_blank">📅 22:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692984">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
دبیرکل النجباء عراق: اگر پروازهای ایران از سر گرفته نشود، از مردم عراق، موکب‌ها و زائران می‌خواهیم برای اعتصاب در فرودگاه‌های عراق تا زمان لغو این تصمیم آماده شوند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/692984" target="_blank">📅 22:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692983">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
الجزیره مدعی شد: مهم‌ترین مطالبات ایران در مذاکرات کنونی: رفع تحریم‌ها، لغو محدودیت‌های صادرات نفت و دسترسی به منابع مالی بلوکه‌شده
🔹
دو طرف همچنین درباره ترتیبات تنگه هرمز گفت‌وگو می‌کنند؛ از جمله امکان بازگشت به نوعی مدیریت مشترک تنگه توسط ایران و عمان…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/692983" target="_blank">📅 21:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692982">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeDVZZiF4v8Guvs2t0hHTxeH-0IQ-o-CnlYfgwfBbDsxK8Svct_WPUm4-d2OQrXVzf1hOw9EPkaIGFSS8nPluhpag-V_Cz5BOVpn3JSWo6h2uIyf1T2uozObfAm1iCRo4xCdvyV8F_cT3FS5o4tVD06ZimnvF3KGMM3G33YqVsw5k6BBN2aMstPZr-kTDTttR51lPkPzlmkkDqPCt7Mq-vGWRwVgbP24JCBOnwRpdCsdYRVZdSXfmt2TwO1PMkYdeWpAX08xHXwATH2ZFDZPlnDp2PcgGRN9gR5A-xjjxVe906ogCVlAMT4rV1LERlNx1tAKuJDp8PVnNQ4AiBxL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متن یادداشت پزشکیان در دفتر یادبود سازمان ملل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/692982" target="_blank">📅 21:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692981">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28bae1d8c9.mp4?token=u1z5ixKJwHWP5fh20kZu9ckCc3zgLUdKrT65GYBcB9mrm2LpI7Ui9mRdZhCgXZX_1-XTDjQATDbiSvXDwkAJMnB0aV7wlrbyh5wzVHLVr2o9-FFRt6otq294yS2PfMxq_VSuK-tEakJjCGSsTcHw83rMlPKqUKmZVnI9WBYEODcVNR7IkwRwTKVvaWFQz6ko9v6dzJDId4mb-uQLQy0MFO7h6B4jK0GpJ0RPFuNwOBTpgSbK4SJ7J-btpbAYJKev_ziwaPeC43Bci2JZe_sK3VEDT3aogk00y21o55LJJna5gEeF5_r_oZRf0nxtCXKBD2jLqW4PE9E0gha1pkYh-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28bae1d8c9.mp4?token=u1z5ixKJwHWP5fh20kZu9ckCc3zgLUdKrT65GYBcB9mrm2LpI7Ui9mRdZhCgXZX_1-XTDjQATDbiSvXDwkAJMnB0aV7wlrbyh5wzVHLVr2o9-FFRt6otq294yS2PfMxq_VSuK-tEakJjCGSsTcHw83rMlPKqUKmZVnI9WBYEODcVNR7IkwRwTKVvaWFQz6ko9v6dzJDId4mb-uQLQy0MFO7h6B4jK0GpJ0RPFuNwOBTpgSbK4SJ7J-btpbAYJKev_ziwaPeC43Bci2JZe_sK3VEDT3aogk00y21o55LJJna5gEeF5_r_oZRf0nxtCXKBD2jLqW4PE9E0gha1pkYh-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت غلوآمیز شهباز شریف از نقش ترامپ در نجات صدها میلیون انسان از جنگ هسته‌ای!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/692981" target="_blank">📅 21:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692980">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59448866a1.mp4?token=LL7FC_eBbJuACGnFv0qPQEz4hUzSasY_LLlFblT3eBg7R5CMyuvhVjz4-MFkWaeztZSqqUbL24IP5NIQvK5-LscSeyiSQCox045AESAt9EMJGkoXxoE8uTqR12cfWQymvx8hfty4eHgXHXmox-Bogoitv4NCv06CnMab9TpPlUw5eJVnpbPOLqwdd7d2kqt6NiShHtNKPPG6sGFzieR3eEFQa0seLVc_bgweTjtdgZW6HWgJQ-aFXpVs980rPAT7LghsFM1geA3CPEpl8yMtR2q2zcfwqvs61yQb1FasJsWTlLqkj-wDMj1uqtZB9j3rtZZz8Lmqfo7lzT30LUALiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59448866a1.mp4?token=LL7FC_eBbJuACGnFv0qPQEz4hUzSasY_LLlFblT3eBg7R5CMyuvhVjz4-MFkWaeztZSqqUbL24IP5NIQvK5-LscSeyiSQCox045AESAt9EMJGkoXxoE8uTqR12cfWQymvx8hfty4eHgXHXmox-Bogoitv4NCv06CnMab9TpPlUw5eJVnpbPOLqwdd7d2kqt6NiShHtNKPPG6sGFzieR3eEFQa0seLVc_bgweTjtdgZW6HWgJQ-aFXpVs980rPAT7LghsFM1geA3CPEpl8yMtR2q2zcfwqvs61yQb1FasJsWTlLqkj-wDMj1uqtZB9j3rtZZz8Lmqfo7lzT30LUALiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از تجمع عده‌ای مقابل منزل حسن روحانی و درخواست محاکمه او!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/692980" target="_blank">📅 21:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692979">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اختلال در چند مسیر ارتباطی اینترنت ایران ثبت شد
🔹
داده‌های پایش شبکه در روز جمعه سوم مهر ۱۴۰۵ از اختلال و افت کیفیت در چند مسیر ارتباطی اینترنت ایران خبر می‌دهد؛ هم‌زمان، اختلال اینترنت در استان‌های مازندران و مرکزی نیز در سامانه پایش مستقل آی‌اودی‌ای ثبت…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/692979" target="_blank">📅 21:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692978">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پشت پرده تعلیق پروازهای ایران به نجف   یک منبع عراقی:
🔹
نخست‌وزیر عراق دستور تعلیق پروازهای ایرانی را به وزارت حمل‌ونقل این کشور داده تا این تصمیم به فرودگاه نجف ابلاغ شود؛ با این حال، تصمیم‌گیری درباره پروازهای فرودگاهی در اختیار سازمان هواپیمایی و وزارت…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/692978" target="_blank">📅 21:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692977">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619837f067.mp4?token=dp5gdnligE9WDet4NCwAoSEA2XbPmCFM4p5EPiTh-FZto77bq2W9i3w6Fo4I6VDCBpbJuhe5eNP96M75vFK7xxuL19jujM-r9xcEV3gGznPZC7i4lZi2Mgn7uXv4M-RxSqShYx2-d8C1JZ9LBA-0xoEb8ywK3ymSRcZf7iyCKvtcs0Vfa_VggAHSrOjL6tDI6U0IjhWDzCy7gk0XZsRfi4zt3Rn_RsVhzXTj8d3m0ISzx6HCM7UPV_gDDKTErUX6c4f0Qu7b1iqHK3rEAoaB2QAllwrHsoD2STbonSaEqkfDe0pACXzOXVuLPse1H20dJNuSNkw4ZKwY6uCXYep6ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619837f067.mp4?token=dp5gdnligE9WDet4NCwAoSEA2XbPmCFM4p5EPiTh-FZto77bq2W9i3w6Fo4I6VDCBpbJuhe5eNP96M75vFK7xxuL19jujM-r9xcEV3gGznPZC7i4lZi2Mgn7uXv4M-RxSqShYx2-d8C1JZ9LBA-0xoEb8ywK3ymSRcZf7iyCKvtcs0Vfa_VggAHSrOjL6tDI6U0IjhWDzCy7gk0XZsRfi4zt3Rn_RsVhzXTj8d3m0ISzx6HCM7UPV_gDDKTErUX6c4f0Qu7b1iqHK3rEAoaB2QAllwrHsoD2STbonSaEqkfDe0pACXzOXVuLPse1H20dJNuSNkw4ZKwY6uCXYep6ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژاپنی‌ها قاشقی الکتریکی ساخته‌اند که بدون نمک، طعم شوری به غذا می‌دهد!/ دیجیاتو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/692977" target="_blank">📅 21:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692976">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749678b1ba.mp4?token=cJZ6xjfeWfX7zxRwnPiuFpDg9kPdEVJyd5O_6Rjd4FmsPEY-86sjhayUoCRtdgnw_p5GGopqEPQMzJp7puy9p1t9aGwAOqy53WnHa187Jx-GuBQEVbURbqWWETRCKoepvRHprxxdeJFyHbFUwV4NZ6-Cu8MnLJ74VcK9t0skVBJofXA7RY8VdbifgGfq6t8ou9ewA9OMqmGqV9EMI-G_WNQqKHjZJK6zykrcJs0Dw4YzzyXVWRLUcnNUvXnCmHiv-ZMM5lLCTmUA9BzMSEJXSMjtV0TRqL3c4Udx4jBHnnkVflW1FLRvjT0AXkOLnsLCDLaMkc-rNnoke53kFORcGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749678b1ba.mp4?token=cJZ6xjfeWfX7zxRwnPiuFpDg9kPdEVJyd5O_6Rjd4FmsPEY-86sjhayUoCRtdgnw_p5GGopqEPQMzJp7puy9p1t9aGwAOqy53WnHa187Jx-GuBQEVbURbqWWETRCKoepvRHprxxdeJFyHbFUwV4NZ6-Cu8MnLJ74VcK9t0skVBJofXA7RY8VdbifgGfq6t8ou9ewA9OMqmGqV9EMI-G_WNQqKHjZJK6zykrcJs0Dw4YzzyXVWRLUcnNUvXnCmHiv-ZMM5lLCTmUA9BzMSEJXSMjtV0TRqL3c4Udx4jBHnnkVflW1FLRvjT0AXkOLnsLCDLaMkc-rNnoke53kFORcGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست‌وزیر پاکستان، شهباز شریف: تنگه هرمز و باب‌المندب شریان حیاتی اقتصاد جهان‌اند؛ باید باز بمانند و حامل رونق و پیشرفت باشند، نه میدان جنگ
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/692976" target="_blank">📅 21:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692975">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای سنتکام: تاکنون مسیر ۱۲۲ کشتی تجاری به سمت ایران را تغییر دادیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/692975" target="_blank">📅 21:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692974">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVNREOT9fD0UVVk6CjHY3UGksH3MkEM1F8cFFHkkf0noDv51xVipgBLnby3aX3ZHlM5a8hH8qWkGDZTnI1bI4GTPcRaCSap9AJ7b_v3Ny6hKgy1mU5eu-PIacqOU91MD8ZNMrtinnvjfSytTerxbeGebork-EUqwLZ-oV-9xJir9fVHcrUw6T0gLTb92QTGe53n4D5nXMIb5dYUMjptQF8VQuwOe9IjA44Uv7L3gl3MI_PB_pbNjVqftpQ1bGgvLQNjRPk5dR7PaFhBXsWbjPj5XHDpAl7EzVOJ4aaiH35vFrXhGkyXebGTXB8QC3syrV-KNwIiR6WD76H7AflNHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک کارگشایی نگهداری طلای میلی را منکر می‌شود؟/ میلی اسناد تحویل طلا را منتشر کرد
🔹
در پی انتشار مطالبی درباره محل نگهداری طلای کاربران میلی و این پرسش که چرا امکان تسویه دارایی برخی کاربران فراهم نشده است، امیرحسین صدقی، مدیر ارتباطات پلتفرم میلی، با انتشار توضیحاتی اعلام کرد که طلای کاربران به خزانه بانک کارگشایی تحویل شده است.
🔹
روابط عمومی میلی همچنین با اشاره به نگرانی کاربران درباره وضعیت دارایی‌هایشان اعلام کرده است که این پلتفرم خود را مسئول پیگیری تعیین تکلیف دارایی کاربران می‌داند و موضوع را از مسیرهای حقوقی و اجرایی دنبال خواهد کرد.
🔹
بر اساس توضیحات منتشرشده، میلی معتقد است میان اسناد تحویل طلا به خزانه بانک کارگشایی و پاسخ دریافت‌شده از این بانک، ابهامی وجود دارد که باید برای کاربران روشن شود.
🔹
رسیدهای تحویل و نگهداری طلای کاربران میلی در بانک کارگشایی نیز برای بررسی عمومی منتشر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/692974" target="_blank">📅 21:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692973">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sP7b3-flL51M9JYTGAQaH5pJr3rFPENFfm9bmJhfPIEX2azhU0VkyJ4E72lmfqwBVHz1wsq7D2GmyDuniH6-5IZeIswHxP8NGORcMhpx7wR7syM0O3mxN_4ljS4LDrg7MpHAAfNWH8D0-huToxwD0wUR2puFm4BlgG6GvU6NzhlRgt3ZXqL8liEOHigCGutXCKThfz2098bj6oYASTnn5l5Giaq90x0tfLkDXCmivRV-my5YShWJB1vi-JkcEZNChDoWyO9_hsUz1V4msGil9hTH16kHXBDfCAETQS-Va0-n3VK8dTSiqBEem4DPbNEif9kuT4VGsYeWE7fsd7TGvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار پزشکیان و دبیرکل سازمان ملل در نیویورک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/692973" target="_blank">📅 21:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692972">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
جزئیات جدید از مذاکرات ایران و آمریکا به روایت مشاور محسن رضایی: آمریکا فعلا طرح ایران را نپذیرفته/ پیشرفت ملموسی در مذاکرات حاصل نشده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/692972" target="_blank">📅 21:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692971">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baf527f29.mp4?token=CS18gEmgVBTTIJCVhCI7iCIvpni7URKKtkqJ9olSr_9JRkzwRNWlADxyUt9bAtL8LDlBa8OOYHaUEX5irWQsrO0Dwvd5RTwH1wEJ7mpAHaUMNbpHJQEGGbO5DHlHyqoL9q_d8VIUTb-mGL7l1w9yXP2Y8gmzakEpsqCioH-1pacicxuUo6cBXVtNiTJ9NBliAOcIAOiT4XDpWisFUuZsVFK9oA361KH6FpY4Ky755SyQLc15k-dMfMmVH6tRtR1eI5HKvpYAYD6gSqGE_9pBAd7Ijg3DiLkJX8AiT0FEZIK41-GULRDJ1NRlgt9Xs4AzvrWbWLUfmH4lPRCh3srrVah8-dldhNhng8qdOVuHiZ7d5odlSJhFx3625vV3PzQcOHj5ywmY0zNIaOaohI9Mdf4bhrN09-zntVNJL-C3tEWn6L1VNGYSDylYaVtm6h0RZfguhmVt949svnRFPa2qNgnsu4HlwTj0Kism0ff4NxkK765XCGF7V6EXoaXKaJiWW-CbA5R_gYsd_XDDfHKayVZ9YKN7vHkHR4p6DCvyC-L1D5mKAdYogmaQXfDtUI2jWRjcNPfF-jXKmKfNqi2CK1GNvTCAWEQIFJsL_RGqJE1nHJ2VRk5rmjnhH8PhXkR5mdc2ktE9RK49Ks3szMzWOBNquAmf-nyvo5K1JYnyftE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baf527f29.mp4?token=CS18gEmgVBTTIJCVhCI7iCIvpni7URKKtkqJ9olSr_9JRkzwRNWlADxyUt9bAtL8LDlBa8OOYHaUEX5irWQsrO0Dwvd5RTwH1wEJ7mpAHaUMNbpHJQEGGbO5DHlHyqoL9q_d8VIUTb-mGL7l1w9yXP2Y8gmzakEpsqCioH-1pacicxuUo6cBXVtNiTJ9NBliAOcIAOiT4XDpWisFUuZsVFK9oA361KH6FpY4Ky755SyQLc15k-dMfMmVH6tRtR1eI5HKvpYAYD6gSqGE_9pBAd7Ijg3DiLkJX8AiT0FEZIK41-GULRDJ1NRlgt9Xs4AzvrWbWLUfmH4lPRCh3srrVah8-dldhNhng8qdOVuHiZ7d5odlSJhFx3625vV3PzQcOHj5ywmY0zNIaOaohI9Mdf4bhrN09-zntVNJL-C3tEWn6L1VNGYSDylYaVtm6h0RZfguhmVt949svnRFPa2qNgnsu4HlwTj0Kism0ff4NxkK765XCGF7V6EXoaXKaJiWW-CbA5R_gYsd_XDDfHKayVZ9YKN7vHkHR4p6DCvyC-L1D5mKAdYogmaQXfDtUI2jWRjcNPfF-jXKmKfNqi2CK1GNvTCAWEQIFJsL_RGqJE1nHJ2VRk5rmjnhH8PhXkR5mdc2ktE9RK49Ks3szMzWOBNquAmf-nyvo5K1JYnyftE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیشه‌های شفاف و مقاوم ساختمان‌ها چگونه ساخته می‌شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/692971" target="_blank">📅 21:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692970">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBt0CZp-TrbmWxDyu2oQTuQCr9v6tTjprlW-B8bL_RMdh_5i93x2etFuRwYsEgBSCBpnjbhYhBjgACu7ASQtXaW1NuFIqORTIAcoi4VrS-njIo6cjK96GICMGdxP3YoHi0aG_qhkCsz_-KN0__Ak5VMwywpMmrpf_Og2tH34UaJZjvIKB_9SHYU33G3Oi86NQg_DgrBJMnv7QADjqZvdsk8f8Z_KoskuIXcjdDSowy3iLnnsl57kg3pjCnjV8FzbEu76NOSaFDpAg1qljL9RTCsn_sNSWiGN_UopddsjCzEa3TzT5cvvOGHcEoeZfYx8BFiKquVoOuJhcBRiG53PZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره مدعی شد: مهم‌ترین مطالبات ایران در مذاکرات کنونی: رفع تحریم‌ها، لغو محدودیت‌های صادرات نفت و دسترسی به منابع مالی بلوکه‌شده
🔹
دو طرف همچنین درباره ترتیبات تنگه هرمز گفت‌وگو می‌کنند؛ از جمله امکان بازگشت به نوعی مدیریت مشترک تنگه توسط ایران و عمان…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/692970" target="_blank">📅 20:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692969">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b2a67d87.mp4?token=cMHmJ-Dfgl2791mEDqelNLYFH-45k0s9MD0GfzT3i7YoWFOW_6eg4K2RWBcnhDgplQyk_hBYJvnZvzULwSRy7ctTOzefCJkftZEGFUTPv--Wh452oche3wJW7RLPxdTXPySU4_D8d0iwgN2vHP88Vz0bbj4fhKMuf088QCCmT9h3S2JgeWpp9pgLRzUI_7seju4wW7NFcn77m1xqeyZKSpNHeGRXPUtqhbI88x5Atyo9Kk-VZaBjzvp3bQmtqd6ZjRPqdbTgiplSvWWo5k3cly3Ag5nAEdH5hqjiCUfhx12PgJVHiHr9iUb_LH0J1ITmZaX55GiGOTvb1sg7ymuId4q4HJzxekGAoyRzg9uQK5FrTFXM8RoUMadNzNNNEU4bimi0oUfp8OEI83VLhJPS3HlyYoiE4V6-2QB4ZDwQtstZsco8If9B9sp8K7-L4_lqZxh8KwaLSOIwAEzCTGmIU3-RG_KXHkLZsrURLQ9Lf2qE9Vrr1-4mJdZ47mrsdD8AkSYIfIYqx93wAmP1NWdnjrPyoMyWUAQeIwsngtDP11qv04TIuowBNnyVEOuvZpP2VZ0YABZjVBX_bMOhxlOmDc0ziXGihM_HmCIV01LIDMx2Kg5FO2gIyHVX1FFsPiZWwV9WkqX3HR5bue-DuHDqKv2-IHOcK6_IeaGgh4B8ERA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b2a67d87.mp4?token=cMHmJ-Dfgl2791mEDqelNLYFH-45k0s9MD0GfzT3i7YoWFOW_6eg4K2RWBcnhDgplQyk_hBYJvnZvzULwSRy7ctTOzefCJkftZEGFUTPv--Wh452oche3wJW7RLPxdTXPySU4_D8d0iwgN2vHP88Vz0bbj4fhKMuf088QCCmT9h3S2JgeWpp9pgLRzUI_7seju4wW7NFcn77m1xqeyZKSpNHeGRXPUtqhbI88x5Atyo9Kk-VZaBjzvp3bQmtqd6ZjRPqdbTgiplSvWWo5k3cly3Ag5nAEdH5hqjiCUfhx12PgJVHiHr9iUb_LH0J1ITmZaX55GiGOTvb1sg7ymuId4q4HJzxekGAoyRzg9uQK5FrTFXM8RoUMadNzNNNEU4bimi0oUfp8OEI83VLhJPS3HlyYoiE4V6-2QB4ZDwQtstZsco8If9B9sp8K7-L4_lqZxh8KwaLSOIwAEzCTGmIU3-RG_KXHkLZsrURLQ9Lf2qE9Vrr1-4mJdZ47mrsdD8AkSYIfIYqx93wAmP1NWdnjrPyoMyWUAQeIwsngtDP11qv04TIuowBNnyVEOuvZpP2VZ0YABZjVBX_bMOhxlOmDc0ziXGihM_HmCIV01LIDMx2Kg5FO2gIyHVX1FFsPiZWwV9WkqX3HR5bue-DuHDqKv2-IHOcK6_IeaGgh4B8ERA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردمی‌ترین شرکت پول‌ساز دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/692969" target="_blank">📅 20:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692968">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3ozC39XhtLzhKpLZ_0D_OsEVp5QsaTtTk_G84rrUVlcX8u75G05GQNPN3vP1hqdIe0sHYwWFH-g4w9KnGYKZYWtfOqwDPGN-1qGrT08Vk0iK3rqakf-tN-3pMAXOmoPJOwfZgiAIkWmo8tvIT7dK9Ym_PRteSUrlsGhPprmKZ1uw9z24zDZExkGOYSqbUOPl82qH0FWYKQznfrkGPtxGmgQZl3R6HyCOx1rs-45Z5gNTa6vg5RBm2ysGTW80D-9VKDduE2gz5oPS4ltvGKH46DgBFaI0vEfAScelRU8IbjDCEDgSebzkz423QJT4XkaXroK5pgIFHBdrUaFzmmvwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فروش کیف‌های اضطراری در آلمان از ترس حمله روسیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/692968" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692967">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17c8f0887.mp4?token=AS8D7hmfLnz71v1aePm4-ZMqTfZHn9XuopQrQgCoIScRplp-y_GslRzrYc4-CQGS20fBw61-VtEKEXbkLruO_2OQ2wZaIOgaeAG87nmzTXGvH1lVgNRop-lC3-nHPwcNEmC26J9AL3RCsP1Ys86pwfIWIUn2lmGnwoqTx3uyep92auRbO7c2Y9f6Fn0XQGQoESDAm7JvLDszjecvRFNipn-_iMkQmzcXIYi9rqhWKWWYdMOS5cweY18lkKEedx2otxnjkRqmhMQt-a0seP24cogu04Lt9i1vJEbNXh559F44BI9EYau8yr6HPOJUoB3SELvcdRgD2hxIc6SSHPgLL2LCvAPD9ssqzdC5Z5KCEMHiCJ6SJ_ZIgB8VdBDKjomgpjQK8Wu_kAW3m9nS_kCB3B9qaxz2gs3W6yYE5zVxhvGFOPCSnpbaY267_jJqVeAPMrdQpYIOqeEx5nGWxaGYlV8KthH9i49PPwkV_qvJ_3vdMR_DdFxq6duf8UCM68bjCfbFCxivJOURDFrq6UdVpkZTob4XU_cMXS0XfMID0gt7u_iPM0U5HBC7t9QvFU5p5iSJbM4bpNcQiGhE9dgkVnqYDrXRjH7GttTqG7IAv5AptFkKvWyLwz1t523P7uUTgS1YvNvEdJTRPOOxFPVbVrvyIv6EmAC10ECjdkxDe_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17c8f0887.mp4?token=AS8D7hmfLnz71v1aePm4-ZMqTfZHn9XuopQrQgCoIScRplp-y_GslRzrYc4-CQGS20fBw61-VtEKEXbkLruO_2OQ2wZaIOgaeAG87nmzTXGvH1lVgNRop-lC3-nHPwcNEmC26J9AL3RCsP1Ys86pwfIWIUn2lmGnwoqTx3uyep92auRbO7c2Y9f6Fn0XQGQoESDAm7JvLDszjecvRFNipn-_iMkQmzcXIYi9rqhWKWWYdMOS5cweY18lkKEedx2otxnjkRqmhMQt-a0seP24cogu04Lt9i1vJEbNXh559F44BI9EYau8yr6HPOJUoB3SELvcdRgD2hxIc6SSHPgLL2LCvAPD9ssqzdC5Z5KCEMHiCJ6SJ_ZIgB8VdBDKjomgpjQK8Wu_kAW3m9nS_kCB3B9qaxz2gs3W6yYE5zVxhvGFOPCSnpbaY267_jJqVeAPMrdQpYIOqeEx5nGWxaGYlV8KthH9i49PPwkV_qvJ_3vdMR_DdFxq6duf8UCM68bjCfbFCxivJOURDFrq6UdVpkZTob4XU_cMXS0XfMID0gt7u_iPM0U5HBC7t9QvFU5p5iSJbM4bpNcQiGhE9dgkVnqYDrXRjH7GttTqG7IAv5AptFkKvWyLwz1t523P7uUTgS1YvNvEdJTRPOOxFPVbVrvyIv6EmAC10ECjdkxDe_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ایران قربانی اقدامات غیرقانونی و تجاوزکارانه آمریکا و رژیم صهیونیستی شده است / هیچ‌یک از اهداف شوم متجاوزان محقق نشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/692967" target="_blank">📅 20:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692966">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
مقام ارشد ایرانی به رویترز: ایران در ازای بازگشایی تنگه هرمز هیچ امتیاز هسته‌ای نمی‌دهد
🔹
تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته باقی خواهد ماند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/692966" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692965">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
اردوغان، رئیس جمهور ترکیه: توافق دفاعی مکه ائتلافی علیه ایران و اسرائیل یا طرف ثالث نیست و هدف آن تقویت امنیت و ثبات منطقه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/692965" target="_blank">📅 20:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692964">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
بهترین روش یادگیری، روش حاجی‌بازاریه!
🔹
بهترین شیوه یادگیری، مدل عملیه؛ یعنی از آدم‌های موفق الگو بگیری، دقیقاً مثل کاری که حاجی‌بازاری‌ها می‌کنن. دور هم می‌شینن و از کارهایی که کردن می‌گن و این‌جوری توی اکوسیستم خودشون شروع می‌کنن به یاد گرفتن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/692964" target="_blank">📅 20:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692963">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4470da11.mp4?token=lJOmx_KDq8PAcv_uhyPNK1dhz4VWWDF2YIOGsMdREG8GVO8lkXgrKNv-BPQ9eQo5KDaGnP_yNEO4aSSErKQVVGXN3wJ8pToEJp0UGh88gA_xYipFbGwsfS33YRM8J63De_5f7Yx2X-GAhnyqMhoW1UXyFQVbcLYWRhSKKFuJEBNeUTmamGeP18yWIRXLpVofui57M4R-jqbk9Gx-abRwL6M9niIkocLJ-HTCkUnVpjSLoZGNhvxgRNm1WkM5mfdw93d8xH3VsUcGvpqyQmi7vgE19NcbGrYcQdqBNDDFSh1Hru-K2HrzYfqKzK0G2bKawSbCJoCV4KViqenBgfPBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4470da11.mp4?token=lJOmx_KDq8PAcv_uhyPNK1dhz4VWWDF2YIOGsMdREG8GVO8lkXgrKNv-BPQ9eQo5KDaGnP_yNEO4aSSErKQVVGXN3wJ8pToEJp0UGh88gA_xYipFbGwsfS33YRM8J63De_5f7Yx2X-GAhnyqMhoW1UXyFQVbcLYWRhSKKFuJEBNeUTmamGeP18yWIRXLpVofui57M4R-jqbk9Gx-abRwL6M9niIkocLJ-HTCkUnVpjSLoZGNhvxgRNm1WkM5mfdw93d8xH3VsUcGvpqyQmi7vgE19NcbGrYcQdqBNDDFSh1Hru-K2HrzYfqKzK0G2bKawSbCJoCV4KViqenBgfPBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مِتا مرز تماس تصویری را شکست: طرف مقابل، سه‌بعدی و زنده وسط خانه‌ات ظاهر می‌شود!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/692963" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692962">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff824d345c.mp4?token=IH9bNYahMmMgTuHrw45Rruoi1nckajjHd3z-byASZ4j3RM_-4VhV7jhKPnrlz3-GS4aFNIitC1nrFcRvTbzB-5hNxa5_JnRHdzmnxRDXMyNO6RLp1WxUmruoNthy-YQsFPqe8kLA5VAUiQa7u1DJp-YXd3b2bXJu-MplKTd-NbhedjEcJbAcA1OXhFYwXHYo_ah-IhebeWNWVDmxhVihbd7YlXjVzl75w8wa40jMtnxUPszwufUvDyzuq70puQOJ6lv5fWcicmIY9aL6eVxqHc6q5vCGKli7NripbpxzCwmf6C7PaXWMU2OoCjXUQEWb-stIoV7CyMhHtYJTSyFhuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff824d345c.mp4?token=IH9bNYahMmMgTuHrw45Rruoi1nckajjHd3z-byASZ4j3RM_-4VhV7jhKPnrlz3-GS4aFNIitC1nrFcRvTbzB-5hNxa5_JnRHdzmnxRDXMyNO6RLp1WxUmruoNthy-YQsFPqe8kLA5VAUiQa7u1DJp-YXd3b2bXJu-MplKTd-NbhedjEcJbAcA1OXhFYwXHYo_ah-IhebeWNWVDmxhVihbd7YlXjVzl75w8wa40jMtnxUPszwufUvDyzuq70puQOJ6lv5fWcicmIY9aL6eVxqHc6q5vCGKli7NripbpxzCwmf6C7PaXWMU2OoCjXUQEWb-stIoV7CyMhHtYJTSyFhuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرخ زندگی
🔹
از ایده تا اجرا؛ تجربه‌های واقعی فعالان و صاحبان کسب‌وکارهای خانگی .
🔸
داستان گام‌های اولیه و رمز موفقیت کسب‌وکارتان را با دیگران به اشتراک بگذارید. صدای خود را در یک پیام صوتی ۳۰ ثانیه‌ای همراه با عکس‌هایی از کار یا خدماتتان برای ما بفرستید تا با مخاطبان به اشتراک بگذاریم.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/692962" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692960">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
الجزیره: پس از دیدار ویتکاف و کوشنر، کارشناسان فنی به مذاکرات نیویورک پیوستند
🔹
آمریکا ابتدا به هیئت ایرانی روادید نداده بود، اما روادیدها به‌سرعت صادر شد و هیئت ایرانی به مذاکرات ملحق شد
🔹
طرح ایران برای بازگشایی تنگه هرمز طی هفت روز، در صورت لغو محاصره…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/692960" target="_blank">📅 20:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692959">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
الجزیره مدعی شد: مذاکرات ایران و آمریکا در نیویورک از تماس‌های اولیه دیپلماتیک فراتر رفته و وارد مرحله‌ای جزئی‌تر و فنی‌تر شده است؛ منابعی در تهران فضای مذاکرات را به‌طور فزاینده‌ای مثبت توصیف کرده‌اند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/692959" target="_blank">📅 20:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692958">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای اکسیوس رسانه حامی رژیم‌صهیونیستی: آمریکا به ایران اطلاع داده که ایران تنگهٔ هرمز را کنترل نمی‌کند، بنابراین نمی‌تواند در مورد آن شرط و شروطی اعمال کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/692958" target="_blank">📅 20:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692957">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh_rqjn2NsUCDWBjbgXoYY2DZqsdhdjLy476zqK8dFjw080hXB6PtBKNKPOl4KreGwe-sSc5xmyLBg8PglPNQ-KqgowA6Rel5D_QI9-0EwcRGBQYsar6nSC5Ew8FV8JTykE_3QsPOFYJ_A8g6lzrA-5NQ9meZ5Z2M_oZwtoYZYzqkvZtUskB4uCgUnOkyfOv48WPGGh62JASN2XHVTGxN7l1Dh5vKKBK_Rk9qBrb356tqy1RuX0EUQQjifUL8KyKX2UG0r6YaALwjNwM6uJIM3TAJOj8AI-kW0koqYOZAdaBl4DrO2EDvIeKKJMkUtGTg4qQWEnmuj78XZd97XsqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط نفت برنت به ۱۰۳ دلار با خبر مذاکرات فنی ایران و آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/692957" target="_blank">📅 20:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692956">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
فایننشال‌تایمز: انسداد هرمز تجارت خلیج فارس را بحرانی کرد؛ هزینه حمل تا ۸ برابر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/692956" target="_blank">📅 20:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692955">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXLmr6q0x8tkp_T7IyPhrIGcQE1BfQiyHICLBbOJ-Qa53mIT2aAya53FLmxL0BhAEB0WJjQn4_YUwnSiBUTSO2F2JlMjIa1C4MUwXAK9GBGiTDT2n1NRg5ZVVVnhim3QPyJ2hcrRGB0fPWDVaj8URu_nr_4jdeXjZiNFAMlTUs6aHklam2_VFcSbZG_AixOr1ISUEHwMOHnpreNHOk-X1J7nyoljIYt1hCTuK_0VJMn6EfNQGUTKisMzAwkKyA5DEJkLyFV3JvnwU0n272KYxPn6ZpZNlm5ppFFKa_z_DO7HBQA3l0R0lzD4gZDOpo41bqiaRPzrVe7OAr9Nl5bLlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتفع‌ترین قله در هر قاره
🔹
بر اساس داده‌های دانشنامه بریتانیکا، قله اورست (آسیا) با ارتفاع ۸ هزار و ۸۵۰ متر از سطح دریا، بلندترین قله جهان است.
🔹
پس از آن، قله آکونکاگوا در آمریکای جنوبی با حدود ۷ هزار متر و قله دنالی/مک‌کینلی در آمریکای شمالی با ۶ هزار و ۱۹۰ متر  در رتبه‌های بعدی قرار دارند.
🔹
البته اگر ارتفاع کوه‌ها به‌جای سطح دریا از «پایه تا قله» محاسبه شود، دنالی (مک‌کینلی) بلندترین کوه جهان خواهد بود.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/692955" target="_blank">📅 20:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692954">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">18-2 Ane Manaee (1404-02-03)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/692954" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هجدهم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
خلقت انسان با همه ابتلائات، بخشی از رحمت رحمانیه خدا و پلی‌ست برای رسیدن به رحمت رحیمیه الهی [00:00]
🔹
در عالم حق، مسخره‌کنندگان در تسخیر حقیقتی درمی‌آیند که روزی آن را به استهزاء می‌گرفتند [05:18]
🔹
عرضه فریبنده دنیا، تجلی رحمانیت الهی و محکی ست برای برون داد حقایق باطنی انسان و نیل به رحمت رحیمیه [09:44]
🔹
رحمت رحمانیه نه الزاما نشانه حقانیت ما، که گاهی بخشی از سنجش الهی و محک ایمان ماست! [12:59]
🔹
"امتحان در میدان جهاد"، "فریبندگی باطل"، "رفتار منافقانه برخی خواص" و "ابهامها و وارونگی‌ها در عصر فتنه"، مصادیقی‌ست از رحمت رحمانیه برای محک ایمان در انسان [19:55]
🔹
آیه ۳۱ سوره محمد صلی‌الله‌علیه‌و‌آله، بازخوانی درونی از امتحان الهیست، چلاندن بنده برای اثبات صداقت او در مسیر حق! [26:52]
🔹
حالات روحی امام حسین علیه‌السلام در کربلا، مصداق استخراج خبر از دل بندهِ‌ایست که به «نفس مطمئنه» رسیده [34:24]
🔹
تحلیلی از رابطه ایمان، انفاق و جایگزینی اقوام و ملل در آیات آخر سوره مبارکه محمد(ص) [42:45]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/692954" target="_blank">📅 20:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692951">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
مشاور و مدیرکل حوزه معاون اجرایی رئیس‌جمهور: قائم‌پناه، معاون اجرایی رئیس‌جمهور، به‌عنوان نماینده حاکمیت و طبق ابلاغ مراجع رسمی و ذی‌صلاح در مراسم روز ملی عربستان سعودی در تهران حضور یافته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/692951" target="_blank">📅 20:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692950">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLLG-fDf2YuJtmb-cAQEikYScqGbQkc4WSubZt8K13KopUhTgq9UyF7O-Rxmw4d1aJFbPIVFieSsjhJyEn3lmvE04H3zFr8lV0CrVww0F5_PG5tIPYlQqZohSHmE89Bo73cz1Rnj9ZRGxiABQCzugjergaXMb-uPMoU9kP8Ye8jw-3HZg8UfEtrSJa0iaup2josc0IoDPoR1CjWHyput-Sj79g_a_wYo3kROd6RTZ-nKdGxCDcxaqj3Rptsr-2lLGmSxEt70SdSRKp87fJO-WolQKpf7C2-bHnChwQF12cvuYN_uKvfvrW7aHCL5uJTJysPbjgK_BSEstktkU5M8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از عقب‌نشینی ناوهای آمریکایی به سمت اعماق دریای عرب از ترس هدف قرار گرفتن توسط ایران حکایت دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/692950" target="_blank">📅 19:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692949">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای اکسیوس رسانه حامی رژیم‌صهیونیستی: آمریکا به ایران اطلاع داده که ایران تنگهٔ هرمز را کنترل نمی‌کند، بنابراین نمی‌تواند در مورد آن شرط و شروطی اعمال کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/692949" target="_blank">📅 19:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692948">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e493231e18.mp4?token=RXVXMQtPWvshEg7uHt7k1cHIFPQfKVKOgUYKQ6IUOfmQELcE3MeW6eTwnbY4-QLEymOtdc6VHDDRCV8E4KMM7gqZQfgExADQ52UPFdvLuGO2wQ7VvYslAXoNpHEoadxhRA5iMXQfRTAu7nzO3OFDZPbxpmYQE5yNw0p3ceXC4Q__aUWpiuHHXCulb4e5c2Ip1Jd1XCyAHFF5-69FQq38OhUhqAeTnIc8ijL_stHjK5tK4qVCN2FB6ips47mXTZ0t9JXupgFA3TpHYX6H9niTcbwLAM6sX0TMtogz6TMjBkvUzsNuRypd2nJZTf3tuwpE_ftXclibJ80hNA8Wh7vSYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e493231e18.mp4?token=RXVXMQtPWvshEg7uHt7k1cHIFPQfKVKOgUYKQ6IUOfmQELcE3MeW6eTwnbY4-QLEymOtdc6VHDDRCV8E4KMM7gqZQfgExADQ52UPFdvLuGO2wQ7VvYslAXoNpHEoadxhRA5iMXQfRTAu7nzO3OFDZPbxpmYQE5yNw0p3ceXC4Q__aUWpiuHHXCulb4e5c2Ip1Jd1XCyAHFF5-69FQq38OhUhqAeTnIc8ijL_stHjK5tK4qVCN2FB6ips47mXTZ0t9JXupgFA3TpHYX6H9niTcbwLAM6sX0TMtogz6TMjBkvUzsNuRypd2nJZTf3tuwpE_ftXclibJ80hNA8Wh7vSYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: با رئیس جمهور چین درباره ایران گفتگو کردم
🔹
قصد دارم برای شرکت در اجلاس اپک در ماه نوامبر به چین سفر کنم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/692948" target="_blank">📅 19:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692947">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ترامپ: با رئیس جمهور چین درباره ایران گفتگو کردم
🔹
قصد دارم برای شرکت در اجلاس اپک در ماه نوامبر به چین سفر کنم.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/692947" target="_blank">📅 19:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692946">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cdb1e902.mp4?token=qYlHY4PPdUoqJ6_QjTjfKFpXnWD7D_KVJ3W08TuiFsqXjTwbKk6aI4MrCldfWZvPmzOb2B6tU1-q8RP5tZrMELt3xN_rcF9NIi1b1FpPcEyRtML2EBgSq4LD9Zs35Ey97NjQqe756hbyOCpJrabhQgdYE4lG7H3Ilcxduq5qgIs50cMctTGFglAqMABTYFP7Z0QpH5jl_xIlOOlc-F3cTqfSaZ-_8ZioSOjbVuzjOYQXFrkV975TyO1Jp3A9Ah0kMzqTluTPOixbF4CTbkwC-JTj4A_Ei4gwez3bIQtRhaSKgR5hItY8apz8yBp0ulOSy1ryYDAKRoyziAuzj6Ad3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cdb1e902.mp4?token=qYlHY4PPdUoqJ6_QjTjfKFpXnWD7D_KVJ3W08TuiFsqXjTwbKk6aI4MrCldfWZvPmzOb2B6tU1-q8RP5tZrMELt3xN_rcF9NIi1b1FpPcEyRtML2EBgSq4LD9Zs35Ey97NjQqe756hbyOCpJrabhQgdYE4lG7H3Ilcxduq5qgIs50cMctTGFglAqMABTYFP7Z0QpH5jl_xIlOOlc-F3cTqfSaZ-_8ZioSOjbVuzjOYQXFrkV975TyO1Jp3A9Ah0kMzqTluTPOixbF4CTbkwC-JTj4A_Ei4gwez3bIQtRhaSKgR5hItY8apz8yBp0ulOSy1ryYDAKRoyziAuzj6Ad3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عروسی عجیب با تم مرد عنکبوتی
🔹
تصاویری از یک مراسم عروسی در ایران منتشر شده که داماد با لباس مرد عنکبوتی در ارتفاع حدود ۱۲۰ متری ظاهر شده و عروس نیز با گریم این شخصیت در مراسم حضور داشته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/692946" target="_blank">📅 19:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692944">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
دیدار علی الزیدی،نخست‌وزیر عراق و ترامپ
🔹
دولت عراق پس‌از این دیدار اقدام به افزایش محدودیت‌های هوایی علیه ایران کرد!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/692944" target="_blank">📅 19:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692943">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9939e8cd05.mp4?token=CS6g5_z7i-QqvSr2a452Rnt6E-YtHURJaSRJPlI0Pw4CDRNeTIzh1R4Hn5MlONJy4GZcxkVBcycyhP-k7gVSnpfVdAuB0ipXHlGzr3v8S8VMUsNpqej0z9QHkuKYNDr1WbAzFGHVmnePpOERDYovu5eex-0pyuakQg2LcKtkd3gQL0KxIeNvThqA3i_PqR2TCGiPSA-aNvEbNVdRlS1b3si6MSRRCqqViY6lWMIvOcLjX2-fDlyEUP4KZWElzuslBFhow6AAbvjH6TRlF9gWAavGZO8L43DSQAbTp82hjJKP78Zjhk6C4vUH1qtTQ-zwlIWBo9CHUaS18xuzTDyha0HmuGjkovWzSMP250ivQbNGq5CPugpFwzzsFOvXP-dZKM5vI2z7CKvDgWEvqcdd79Ja6wVxme8nAGSgyhz-nCTIRY0ZDPzHrnsBeZq4d4vahDr9ckDHkAKh3MTVk4mOI_LN3vTE0q2jkGAJNb4V9vDfZ3JgcSy4Kjy3YnPHEGT5IJiyJRpwLlGj_r16ArPtqIyiyb9REXdC6zQy2Pmzah8PXYKMXcpnNw6s5UgNfXrCmFGjtB31pa_lQ9mBwrO8S5gK9miCdDwboQ0XMsqdUVggTIzuqHA3rP-lwSHGyO3--Eeq6yp4oBk1qfg-Q_otq9iLyJ6xoAKbCeZq6d2_CB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9939e8cd05.mp4?token=CS6g5_z7i-QqvSr2a452Rnt6E-YtHURJaSRJPlI0Pw4CDRNeTIzh1R4Hn5MlONJy4GZcxkVBcycyhP-k7gVSnpfVdAuB0ipXHlGzr3v8S8VMUsNpqej0z9QHkuKYNDr1WbAzFGHVmnePpOERDYovu5eex-0pyuakQg2LcKtkd3gQL0KxIeNvThqA3i_PqR2TCGiPSA-aNvEbNVdRlS1b3si6MSRRCqqViY6lWMIvOcLjX2-fDlyEUP4KZWElzuslBFhow6AAbvjH6TRlF9gWAavGZO8L43DSQAbTp82hjJKP78Zjhk6C4vUH1qtTQ-zwlIWBo9CHUaS18xuzTDyha0HmuGjkovWzSMP250ivQbNGq5CPugpFwzzsFOvXP-dZKM5vI2z7CKvDgWEvqcdd79Ja6wVxme8nAGSgyhz-nCTIRY0ZDPzHrnsBeZq4d4vahDr9ckDHkAKh3MTVk4mOI_LN3vTE0q2jkGAJNb4V9vDfZ3JgcSy4Kjy3YnPHEGT5IJiyJRpwLlGj_r16ArPtqIyiyb9REXdC6zQy2Pmzah8PXYKMXcpnNw6s5UgNfXrCmFGjtB31pa_lQ9mBwrO8S5gK9miCdDwboQ0XMsqdUVggTIzuqHA3rP-lwSHGyO3--Eeq6yp4oBk1qfg-Q_otq9iLyJ6xoAKbCeZq6d2_CB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید از «آکبند کردن» آیفون‌های دست‌دوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/692943" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692942">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای عجیب مدیر دفتر خاتمی، محمدعلی ابطحی: در سال ۸۸ در زندان گفتند اعتراف کن که خاتمی به اسرائیل سفر کرده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/692942" target="_blank">📅 19:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692941">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
نیشن: حمله به مدرسه میناب مخالفت با جنگ را افزایش داد
🔹
پس از جنگ با ایران و به‌ویژه حمله به مدرسه‌ای در میناب، تماس نیروهای آمریکایی با سازمان‌های حامی حقوق نظامیان و درخواست برای خروج زودهنگام از خدمت افزایش یافته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/692941" target="_blank">📅 19:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692940">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پزشکیان: حاضر بودیم اورانیوم ۶۰ درصد را رقیق کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/692940" target="_blank">📅 19:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692938">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b0fbb38e3.mp4?token=QXPAFXn0DXvcFGmdqPEfvZLMQWcHSapQnG0gfmRNJFNFXyNpk80m7o_F-7MSYIiAMH2Q9x3_thJAR-X-GKTMkBH7ESealyXfzJ66xTymYKP3av_mm49Az0qFSYJmIKcrdDOOXrEWD-Z_E_0k4uBlwWJ8IhCHWRRvKbJQtGDKWxnJA4EPhP2kFct39LRPklb4QcOrfusRJDkkfiWUbkX-WpAQFUv0VVNpbO8crZGj-VV59qwwYYgcxt4QpAevLaXvARcE3pfNl8HqNZgW7jWNcf8uXEgfyWB_386_DnGT5S6kPXdFEMoSpkwzDEyEbmyoGcUcmNsps-lM5LrAvdwnyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b0fbb38e3.mp4?token=QXPAFXn0DXvcFGmdqPEfvZLMQWcHSapQnG0gfmRNJFNFXyNpk80m7o_F-7MSYIiAMH2Q9x3_thJAR-X-GKTMkBH7ESealyXfzJ66xTymYKP3av_mm49Az0qFSYJmIKcrdDOOXrEWD-Z_E_0k4uBlwWJ8IhCHWRRvKbJQtGDKWxnJA4EPhP2kFct39LRPklb4QcOrfusRJDkkfiWUbkX-WpAQFUv0VVNpbO8crZGj-VV59qwwYYgcxt4QpAevLaXvARcE3pfNl8HqNZgW7jWNcf8uXEgfyWB_386_DnGT5S6kPXdFEMoSpkwzDEyEbmyoGcUcmNsps-lM5LrAvdwnyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادی که هم پرواز می‌کند و هم شنا!
🔹
دانشمندان چینی پهپاد TJ-FlyingFish را ساخته‌اند که می‌تواند در هوا پرواز کرده و تا عمق حدود ۳ متر زیر آب حرکت کند.
🔹
این پهپاد ۱.۶ کیلوگرمی می‌تواند حدود ۴۰ دقیقه زیر آب بماند و برای جست‌وجو و نجات و تحقیقات دریایی کاربرد داشته باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/692938" target="_blank">📅 18:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692937">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhwzV1b0ktLNAWiI51zi8-gjL_9H1cx6_in7-P1s1BXddp2-L1UM_TmVYRiwY3dnbYa_Mkzw3jf8tR82-VaCLDGeEw-DBzkLbLoJFlrBQHs-6rzFHhAZfSCLq7SFho9Pwbs1w2mFfT64Bup_VTK9VzsgFLeLUt-RUaPQ9sPjptuEuAwG2ktCXUf7hoECTg4-ad0ceJ2XSINpZGr9ZXI6WMzn9ZlZxygTjd9LSzkhLk6xW7JM21kuJvYUqOLKY8lhpOHAcqenkJS-RjTR8rSvbZT-MFuu7L1H7IEXKJ8Y-E_44GwmYrv7PrGoOBkqQhDBFtebh3i2rXcOWFVdrUyQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بحران پلتفرم‌های طلا در تحویل طلا یا پول آن؛ جایگزین مطمئن چیست؟
جمعی از خریداران طلا در پلتفرم‌های آنلاین، با چالش جدی در تحویل فیزیکی و حتی تسویه ریالی مواجه شده‌اند.
ریشه این بحران روشن است: نبود نهاد ناظر، خالی‌فروشی، شفاف نبودن و سازوکار نقدشوندگی.
🔹
اما جایگزین مطمئن چیست؟
🔹
صندوق‌های ETF طلا که ۱۰ سال در بورس فعال هستند و طلای آن‌ها در خزانه‌های رسمی نگهداری می‌شود که حتی یک مورد شکایت نیز تا امروز نداشتند.
به عنوان نمونه، طبق آخرین گزارش سامانه کدال،
صندوق طلای «رز ترنج» بیش از ۴۱۱ کیلوگرم شمش و ۸۲۰۰ قطعه سکه در خزانه‌های رسمی دارد.
در حالی که پلتفرم‌ها در تسویه مبلغ ۱۰۰ میلیون هم ناتوان‌اند،
صندوق طلای «رز ترنج» در شهریور ۱۴ همت گردش معاملات داشته که بیانگر عمق بازار و نقدشوندگی آن است.
اعتبار این صندوق به اندازه‌ای است که امکان دریافت گواهی تمکن مالی و وثیقه‌گذاری برای دریافت وام در شبکه بانکی کشور را دارد.
📌
آموزش خرید صندوق طلا را اینجا ببینید
.</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/692937" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692935">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fcdf5128.mp4?token=gTIoPZekdH-2z_TeEI4cvdWTJ6g2UkgnAHE_foyNdLWnPpY57ye4RjYRwFsKKRBVKIHp-zIdIvAijxykeJP4BgvsKes2qNSzsRFbeTvhhXPeRthqRbeR80Zaa1HJfieJNyUtXGeBQbF1W5-ypcVP4dJz3KNdAYrTGiC1Lo_JQAm2_VKofrzf60f1rjmVbVrzzVYrGOhGHs9Wlgmi4Cj8lPt69a5dPHiZZ8pCF1qgxqLfmkkn_dkcrmQZvOK2MXoPW_TXkvZzBtO_v3KX74G1HCCuv1UkD7xyy7fZfkVIX9XBr-VQZVM1SGki9IZUNjz32nahVR4HWuTqwVcg27YzYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fcdf5128.mp4?token=gTIoPZekdH-2z_TeEI4cvdWTJ6g2UkgnAHE_foyNdLWnPpY57ye4RjYRwFsKKRBVKIHp-zIdIvAijxykeJP4BgvsKes2qNSzsRFbeTvhhXPeRthqRbeR80Zaa1HJfieJNyUtXGeBQbF1W5-ypcVP4dJz3KNdAYrTGiC1Lo_JQAm2_VKofrzf60f1rjmVbVrzzVYrGOhGHs9Wlgmi4Cj8lPt69a5dPHiZZ8pCF1qgxqLfmkkn_dkcrmQZvOK2MXoPW_TXkvZzBtO_v3KX74G1HCCuv1UkD7xyy7fZfkVIX9XBr-VQZVM1SGki9IZUNjz32nahVR4HWuTqwVcg27YzYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیرکل ناتو اعتراف می‌کند پنج هزار عملیات هوایی از خاک اروپا علیه ایران هدایت شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/692935" target="_blank">📅 18:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692931">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsjKNvLY18U7Dy5NwOhekFoKmScNHWBhGns1GOjVl4mAmwu7XHxMvQp8dG3yRMQ6GBkxJFWTppxdxbJPuzovNbYp_Gtys4Zu-4-xzicLdnrzVI6umHHLDEOjAZRtyIeatYHeuK8C7ZZquLcdu2YYddTlLPVoduawVTGJ1163XSWULUKBpsRbJ0E5jCP7cqzxapeZSpEjDlDxL4RvdiA4Ksd2ByhwGK4aOv53Ap_DbkyA2wYH_JNRZJ78Kd2xSTtshHF5u9KXpQmw2qseezhCUU9bqUK0LC7VEWohzQtaT9JozoENfaHSmwiU4_nz2odq6isroesqLnzKurOSrkneIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOGsiV7fWMlYxBZbQ6pl5rYIVZg1yzk-cMZfw7pl7BohaMOnaQVJ6HCjR4bHDq4N7wBIGtu3BgfNpdxNO1zsT2IldczcJ9XRuPt-V5sqMlJS2SyWkzPZBm1fIVv4K0sJptmxWlLXNjWWE_ALXIvDb0Gmu4ot1aKcEiPcUwxoE8Ai9Prbotkxf6TI88nFhLjgFYWnhEPfsqgj15HWSJ1z8jQLTfceiTNFeFVpJjNho2Q4Y-sRX4Oh6rq-qzNYXEYbB5zITYpS21dFSCKuhqPQU4piBrwuaYLDV9o_9WOwgvLnvq56nG83eNfUfgnbMpr254baVMUNFVpmfIqEG5z5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Md5V3JOejWnLedQhhV_L4888ejBDvqbmzcV8Yw-dUshjDEbo_sscwNb1e98O0WwuQftNhUsLWs4dp-8AZ_K0UJiQAc7rQY-eiyilMgcev7YBvro-lmic5XOHl3MhQQy4HeSW24PsFJLjgEtniOygE8_WJc8PAJLRvyntfXn6ux1ZpkzjODcZzYh4sVe9TiA_bpnzFlL22K8raKPn4gIKGITlVJerhr1GRrEI58U5xdTkyDis1MXBKklzr8KdD-asdZ9en8hx7HiJDD-hTdyktj5KcrDl1VYp1-p0KN_fijxMDhthKGsr9JkiJTsdKXLOjSU3qzJb5_qvt8ZytTsDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYft2wCLRdib6R14RqQXt43NwvAvM0H3GTY82gHDOEVGzvYl6X9hfxmnWaXWcWTp7UNWmuKTD8mkhugtp58O_G_2iLO6SJTZkANzrv8HGqWlUxRqAPAmkyx6phSVHZVueEzxEgeygU49EXOSTbvUpv6UH4Bc3HELAL9tUewpgdXtubBlskrHmwh3zxUYkXYVSM8yNOkhf4Bfvb3_8bLNtQa4tve1tWabHIDILA1eQpxJ3ntXhYkszXloIH3-ln8XwmIv-S3w2aLTr-zp0OqWMyMbTJnNct8paE5rj6pbTjCGJ2tN_fX0zUoePZEj1cBecQ4zfs9iG0ViIuu-o08KSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند دمنوش مناسب عصرهای پاییزی
☕️
🔹
با سرد شدن هوا، این دمنوش‌ها می‌توانند گزینه‌ای گرم و دل‌چسب برای عصرهای پاییزی باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/692931" target="_blank">📅 18:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692930">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان درباره پشتیبانی اطلاعاتی چین از ایران  سی‌ان‌ان به نقل از ارزیابی‌های اطلاعاتی آمریکا:
🔹
تصاویر ماهواره‌ای و پشتیبانی اطلاعاتی چین به نیروهای ایرانی در رصد کشتی‌ها در تنگه هرمز و انجام حملات دقیق‌تر علیه پایگاه‌های آمریکا در منطقه کمک کرده…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/692930" target="_blank">📅 17:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692928">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KsftNR8ZhHrgG5AjVyXC7U4NDEg3MZjUISpERbOsosuMe5JuhM9tWu6_NCAqGlQAHzmDcbDAoGcxbCZTOA0OVM3rHDUbIqSi9tKOmzNLta5vc4MELC_2qmeQexEvsL9NdnoDyVR0ZKailXRWvfVwZc1GVlE0JwYGGRxGS0Pdo-_8-dBWJglig0BzxXmO_3_DS6wrrUH3__CFFyL0XElAxY87h5DGfcXmk8-UW80Bxc5hXo4nhvfVSGP-prJrYPK8u_rn96VXwce_jwNgYkWkrkB7BJSDBSkhNP-ZYRsBYChenk0n7L-ry3Hs8PPuGXKqzsGAl71lPP0YkiA3FscG5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6vEkFwHFuPZq7CQyd2W9FJ68OkVdWszP6ch7c_MTYVNRgJvB9Rud9MYoAnrEAsjAr_czh6nRCcZScbPbsW0IRJ8x0KpPVoJT98HdgXQT_Piv9FqS0dXq40H-yIBfWqTGt7zewKBE0qjp9R9Czm4klzWrK6f9wlHWMbm-5zFMhLgp6bFv0wc1MzMhFviD8Cv3zNkW188hcJCxDIDMDVKInnlDgXtf-YOOAvT7BeT7qqEiwHNTi2Wka5_VxdBtHwT2BID1b4rMfcX7CIltA2GlQTT8Pfd80VQ8nLfS-BNgzhGIuyjHma3g-HQHulnftWmMWtINjyTW-sHv9enc5tEbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بزرگ‌ترین تولیدکنندگان متانول در جهان
🔹
بر اساس آمارهای ICIS و MI، چین با تولید ۱۱۵ میلیون تن متانول در سال، با فاصله‌ای چشمگیر بزرگ‌ترین تولیدکننده این محصول در جهان است.
🔹
ایران با تولید ۱۶ میلیون تن در جایگاه دوم جهان قرار دارد و کشورهایی نظیر آمریکا ۱۰ میلیون  و عربستان ۹.۱۵ میلیون تن در رتبه‌های بعدی جای گرفته‌اند.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/692928" target="_blank">📅 17:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692927">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzGxYGtmzV92qTk7GaSkCfTIXnlOFJYb3J92TF36Xcd1Dnyp-JAjjmNC66L1JpI_neEUzzakmhH5RZfGkgEp1E3PkYa0PXLcnOo9xR4EisDOjfqg0udAL2G6SAWL4HPovfdDDoZ74nraHsua7NNh9QF9Fu1AJ22Wqipga622Iggn7wjVAciBr01fTQL9u_QNaskGIU40pIC12qUnSCYLXA1_tcX0xo_-eEuCH_Mu3HRBDIFyKDMWP7R0LMYFvOIcR_7q6_p-Jzx3a9tJJ5l0JqnY72kSghmUJiAwBQ943945h480rzP98yi1vTbGI0L63eaHv4H1GzInSWYjFOqP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قبانجی: عراق نباید تحریم‌های پروازهای ایرانی را اجرا کند
🔹
امام جمعه نجف تأکید کرد اجرای تحریم‌های آمریکا علیه هوانوردی ایران از سوی عراق صحیح نیست و از دولت این کشور خواست در این زمینه تجدیدنظر کند. / خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/692927" target="_blank">📅 17:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692926">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
عروسی عجیب با تم مرد عنکبوتی
🔹
تصاویری از یک مراسم عروسی در ایران منتشر شده که داماد با لباس مرد عنکبوتی در ارتفاع حدود ۱۲۰ متری ظاهر شده و عروس نیز با گریم این شخصیت در مراسم حضور داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/692926" target="_blank">📅 17:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692925">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjbJIqqaUN8nM97MCNnHSjb0dTNa4WntB7_wE3_av29wWQVeYjXhS-DQfz0l3mEiz5gUgGz335zkq7zwtpp51cICvDDSr4CWs4XtVGMMxY-yt2BvnRVJ8OcWm7ecVS-tT4_c7Bsqt3dy6lkql8pURpt6jrquEyRdhGRXaKp5k5mzvERlXPEzkKtY5kwEoQfzB4C3sYdZCB3_c5Tbuq0G879KgcdStBCWJ_FJjpoCY3UIhe7S-ljsc-Q_urxA-gPYPLg8l9J1PUxSX5WbvC1U4ghxpNs1tTpE00eBkmDhfk6EZlsxKnzlunENvZXDSJjGVKTUbGFLwvqpdAlZNdKkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: همه باید به‌جای «هوش مصنوعی» بگویند «هوش برتر»
🔹
از این به بعد، در همه اسناد آمریکا و امیدوارم در اسناد سراسر جهان، به‌جای واژه «هوش مصنوعی» (AI) از واژه بسیار دقیق‌تر «هوش برتر» (SI) استفاده خواهد شد. ببینیم این اصطلاح جا می‌افتد یا نه؛ خیلی بهتر…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/692925" target="_blank">📅 17:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692924">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
تصاویری از تسلط نیروهای مسلح یمن بر برج کنترل تردد کشتی‌ها در تنگه باب‌المندب در شهر مخا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/692924" target="_blank">📅 17:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i89Np1mwqpO3lWQVVjuWzu0lSpCXya1LjuP-DK61x4PuCi7PTH8K2ZHlOLAIx-wAIdZ8GdYsgSnzgJOpzy64xygGkMkL6KjRWjUbCGhJS4RrbsPNVkzX5FIV_fiQrmbv-AF3W5UThrOFuSxZIivoSDEkwhboyVhzHKA6zH-6CntXoFleRVEIQ4hf3cATtveio-IKkWE4cfGgrude-B7xEgF41T9hLZEvS9vpxsu59b7hPd671ns9_G89CK6w1UFfRD1SC10iqJ7rN7r5LLwx_CIv5SOlaOzHizc9V_lZi8eEj3iBNxTFtlmIdkNceJ-QH8eRApjUTR3vdFS1nn67EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدئویی از مراسم نود و ششمین سالگرد روز ملی عربستان سعودی در تهران
🔹
کیک سالگرد به حکم رسیدن آل‌سعود با همراهی معاون اجرایی رئیس جمهور بریده شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/692922" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
توقف فروش بلیت پروازهای عراق تا اطلاع ثانوی
سازمان هواپیمایی کشور:
🔹
در پی توقف پروازهای نجف، فروش بلیت این مسیر برای امروز و روزهای آینده متوقف شده و وجه بلیت‌های لغوشده باید بدون کسر جریمه به مسافران بازگردانده شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/692921" target="_blank">📅 16:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692920">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJTboKG_PGLbwTm2E7ST2NZvx0gI5cgodU_UlcKLseJidI_PS2OsKbWA3f5CeWN6YFOiPGAtI6Tbi9-xwAN2S1sEtkv0uFdC-QAOZqS6_ZdFc_o-Y8do6ZY9mdUQUlWpcrwHilm_v7efIUz_pLuDQokkcBpN2_yuO_pucvRnr5pVkGvIO0cS2WwMo7GWxvRYt22LGg8SB2sfmiKif2Lg5vfMk9wuHndG26PV6Wuy5taCZAaIC5e-DUVQFDHgS8cXto-uGg8ilKjbdPRmerKfDI9crh9-2u5p6lNFD_lnep2NG7qomOJvK_4gezy1Ads-V3L4apf2ZbCv5qvol69D7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چیکار کنیم که موخوره نگیریم!؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/692920" target="_blank">📅 16:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmkfXKoXgvMeaYGVp5W0ufKYePE5j3Pwdrzu5Y_fTgXNHe7pFIrdsrZnb0MW2SNK_jrp5Uz0wi3ZicA2xCTVe1qHrAqJgu19AuM8GTavKN0LmeAjK7BYIn0gAXU6yIZm_6lsNQYd0KZCVQVv_Btxd1i8WlBrByWJxaKiFgjVTvif-5XKLJ2f6R6yhKwpHkh_Ry-8a5bA1DncMGpOCvCU2S97yv78u7ZZe0hdaFo6582_8NwjQWjlWCAneV9BqwIN79IGLxeCk1PMx3aoZgbVhjQ6nGuSLAfAixakIStdA2x4TjoSiHihSSl5mo8QfTZ5pXw8tIBgb6dgD-fj3CyH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlEN8MynlloJ63oPwnoJYMSj3XLUv_hoM2qeUECWcmp5V99i1J2EioCxBFPITX967f0cwFsLlFGADsgs4kYWQkkRnhE7mzcaEktKax_SdUFrO9CimDp5VQn3QNdV2IhWiWiX2Wq6cnYcVic0yFZGdR2QzpTcsgW9_kraNs-JkPXQPh87BTrObCgwr_EmRvvWM-ppF13rFJ31a_RV4Ws2H_JEh8cqJgLCn-kuuIWj-UlXVN1nn99sJW-ka5__zeJIYKEN5GceK1nllzlCr2xj_Pesf0oa2D53No_gB0uAPJmzhxt1MCkMdWK4O8yjDUdXdrfJlHg7qcd0zmof_k_dIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4ZDECIRbRbgzfA3cdqlfhrlboTefmFLYmnC-6UFWseV0W3ZNOgHYt3q7rWUoOztYlHrxuYKap1VZYIMS4raVhiOLM3sjaYlm1CbP7ltXrYXKYxPPx6oTDCDtbo-k4aAAJT4louEBTHQMln3xVTZ8kzVoYoYGFNORNZ5bp3pDeKhnHQ4X5aKoGMlWGWn38-US0wQLmoNh9XY_chaUz5XyIWJdlLpdPJXck2SaXKvfok9C1VTBhbGGmg4awuK_lIYShMUbhtfAlB5vZGQn5JifwtxD8DXzRRk65h8zKDlBqt8lfQ3aQs_FENJ17koKpyNe4GVkD0cMs0h5wSqmsXg7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
میناب منطقه توریستی گردشگری نیست
🔹
عرفان کوچاری عکاس خبری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/692917" target="_blank">📅 16:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692916">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c889ef1f42.mp4?token=McbTw1P8vB7cJVEBe0WT6j05sVGj4GrJL26iwAHywi8VlyRwxZn2zW5T4uLXfh9JWglkcLVf7-u3yFUL_MDmiF0VRlhdo3U4paf-F0i1vWK-UT6qUXhXbnTMznprcc7f3HlP8YAu9QfcFThmJlekdrdkwxjORdkxi3FH6nibpwH-UXUYLVOvTAzqPGNBoyHVuq5vjoRzFrHAIpLcYgxhP8r2fETHcBR1w6t7eUNwIfw3LFhyIydQeJqxAYUFUte3qL9bdF4lFfcJtfzs4bQ2mEN6wyX-rrMcIQVi-eR_8Q_oDx5gm2vOMKmJxKHwaHGf9bJSPSTd3jI7qdOHPF6c9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c889ef1f42.mp4?token=McbTw1P8vB7cJVEBe0WT6j05sVGj4GrJL26iwAHywi8VlyRwxZn2zW5T4uLXfh9JWglkcLVf7-u3yFUL_MDmiF0VRlhdo3U4paf-F0i1vWK-UT6qUXhXbnTMznprcc7f3HlP8YAu9QfcFThmJlekdrdkwxjORdkxi3FH6nibpwH-UXUYLVOvTAzqPGNBoyHVuq5vjoRzFrHAIpLcYgxhP8r2fETHcBR1w6t7eUNwIfw3LFhyIydQeJqxAYUFUte3qL9bdF4lFfcJtfzs4bQ2mEN6wyX-rrMcIQVi-eR_8Q_oDx5gm2vOMKmJxKHwaHGf9bJSPSTd3jI7qdOHPF6c9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان در گفت‌وگو با فاکس‌نیوز: اگر دولت کنونی آمریکا بخواهد در چارچوب قوانین بین‌المللی به توافقی دست پیدا کند، خوب است
🔹
اگر نه، چه پیش از انتخابات و چه پس از انتخابات، چه تفاوتی برای ما دارد؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/692916" target="_blank">📅 16:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692915">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9537af776b.mp4?token=b3yov51-hy3JibTCXAgWM1nT-mIiBBiNB-G10uWrKPDURkP-4X5ghhdQfiFRyCFCPAdbV6PrxghGZzzIJK6-Yf4YT0Z1FNv6y77IXpkOzaWdpl3NJh38psw0EItuwSIf4ypdbqzboWQP8oZbH91U2kn-XHh_qqOxYlFj3ZIidNYKBWlv9rDZhL_3BOFGL5ILgjbbLvabXNbuxNdmyU3ml7Ql-vbP7Ur-VzMfxbIpJwz1rBLnejd8wJNeftCgFFOYH3ErCklSPVGgHFIRFBQgrCvjKRhdGe8I6wObLAgfZNJsxnB_zIs6QR1e7RMQNr0OvvfTRB0KveCrAdq12bEopg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9537af776b.mp4?token=b3yov51-hy3JibTCXAgWM1nT-mIiBBiNB-G10uWrKPDURkP-4X5ghhdQfiFRyCFCPAdbV6PrxghGZzzIJK6-Yf4YT0Z1FNv6y77IXpkOzaWdpl3NJh38psw0EItuwSIf4ypdbqzboWQP8oZbH91U2kn-XHh_qqOxYlFj3ZIidNYKBWlv9rDZhL_3BOFGL5ILgjbbLvabXNbuxNdmyU3ml7Ql-vbP7Ur-VzMfxbIpJwz1rBLnejd8wJNeftCgFFOYH3ErCklSPVGgHFIRFBQgrCvjKRhdGe8I6wObLAgfZNJsxnB_zIs6QR1e7RMQNr0OvvfTRB0KveCrAdq12bEopg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر پزشکیان: ما هرگز جنگ را آغاز نکرده‌ایم، اما اگر آن‌ها بخواهند به جنگیدن علیه ما ادامه دهند، ما به شدت پاسخ خواهیم داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/692915" target="_blank">📅 16:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692914">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22f1a729c.mp4?token=IP77DOZpmf0_ly3Mg2kEdntBxg1iOWo9ep8w3KkXohJjDag6WGgVcyT3p532X7zMX1IwmWAvBaGax7mEYO0HUCLCHh0kSMrT6T1bbsbpKF5rslnm1Uo1bRsVruZU9uZTVDqdobhyxOXBV9dQrdPkwGJWLJdFWlyLvsf4tXYGuhs4uLwMJdH7jUOD8NH_bAbikpDRJoRhhN2Ln1EMxBrLhHfROCx8z7RXtGJ2iu7Hd1Uyyvar52GciQLsoIr_SC3GEX0cz5I8bQdyNnZSzjWD_1uIaZK6iwTWxnORVKYLMWpOF3fcPfK0anZ5_oGy58pZ4xnSLc2_029opgPAANEg1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22f1a729c.mp4?token=IP77DOZpmf0_ly3Mg2kEdntBxg1iOWo9ep8w3KkXohJjDag6WGgVcyT3p532X7zMX1IwmWAvBaGax7mEYO0HUCLCHh0kSMrT6T1bbsbpKF5rslnm1Uo1bRsVruZU9uZTVDqdobhyxOXBV9dQrdPkwGJWLJdFWlyLvsf4tXYGuhs4uLwMJdH7jUOD8NH_bAbikpDRJoRhhN2Ln1EMxBrLhHfROCx8z7RXtGJ2iu7Hd1Uyyvar52GciQLsoIr_SC3GEX0cz5I8bQdyNnZSzjWD_1uIaZK6iwTWxnORVKYLMWpOF3fcPfK0anZ5_oGy58pZ4xnSLc2_029opgPAANEg1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون، مجری مشهور امریکایی: اسرائیل ۳ هدف در جنگ دارد
🔹
این اهداف شامل حذف ایران، تضعیف کشورهای خلیج فارس و خروج پایگاه‌های آمریکا از منطقه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/692914" target="_blank">📅 16:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692913">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7QK954JaZSf-dXnAMaN9SisJtObtHZHE9DNozXbIITA22AxWz1XJs6NGhjh_3PDq_5qKta-Mvpr8GdpBflo2DNXSlf39tk9wByylviHxyXFD5VNHtyAq_EdcNXoODgBJAkMeMKHJlEg9vODozV7Wa2o504DqfU4uo5-7lz7c3yY_x7Q5wW5H8BnBWjY8es7PCMqs64Fpmpf3gO0bgwYBZ5ZZEgixI5xqgeBVWWrKojfqqzzdSJbGMO9z_e7guc_uzBcC8ACMKCXFpTsa7dOdvq0uK1y7Xq5FrBE5FZj4LOWQAdv4NZwl1L3Z20woPqUpd2VQzWYfyboZ4oOIRRyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلمبیا به طور رسمی روابط دیپلماتیک خود را با ایران قطع کرد
🔹
کلمبیا در این بیانیه ایران را به آنچه «ارتباط با گروه‌های تروریستی بین‌المللی» خوانده شده متهم کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/692913" target="_blank">📅 16:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692911">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-MkgbW86BGYkbxseC5362QUBFKLZ-rZp5PdtSwL9vFXbqjXqAKFTuqXnu52zUqc53o8sLQZkkaRAzoOPS_Qp9yds2szqmom5JCcVXtgSmlDEeh_tSNEEDnvRJyyZ4JZRP_kGgxg-qIHLJP39mO1dsJaaXZrzMV3bYZAI4ZkwAE0lnWhoz2CwzZNhpFdasOY_h-Ob8FhWIGe8mRVQDMaQCyhp-sYq1XghDdcrpNVWblCE2BPoYu_prXLOzwrWmmWrDZppcOVBWUaVXTsez6pkpgiW4a_t7qi5O3MNQ1qPe8aNj3xjvg9ZhWjYA9oY5J58AdZyt518iUIMEFrdRwXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خروج نماینده دولت تروریست آمریکا حین صحبت‌های پزشکیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/692911" target="_blank">📅 16:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692910">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85bcc69018.mp4?token=sMK_8F4n2E4KN0ZrNTIg1uO2n6MHLN2i5MuCZqIYE2pnnQe-jYwaxx4p25rviFC77FjwIf9TAJXDlrYb7b4dwkQQyJvUyUq69G0eRGNvvNrRT6WSXxvxycvahLN51reknxodW-g0zFcZsoRm8PqWXDenQz9KqlYOzD1kZ4wT9kCSS2Id1ahhlummBjquw-RZPbYmpF3h5uuDQit4DdqHI_fPgpwMVuUsF87JYynmfg3bZ4PEBHA0Q0gHVcnKuBLF5gG_g0nfss03QEsWWKz9QzANJC-SFgzKGckk6I5-TGHen4aueHSGh9mZHyZC62QxUtYkHvXEdK_SDG1DTDRtYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85bcc69018.mp4?token=sMK_8F4n2E4KN0ZrNTIg1uO2n6MHLN2i5MuCZqIYE2pnnQe-jYwaxx4p25rviFC77FjwIf9TAJXDlrYb7b4dwkQQyJvUyUq69G0eRGNvvNrRT6WSXxvxycvahLN51reknxodW-g0zFcZsoRm8PqWXDenQz9KqlYOzD1kZ4wT9kCSS2Id1ahhlummBjquw-RZPbYmpF3h5uuDQit4DdqHI_fPgpwMVuUsF87JYynmfg3bZ4PEBHA0Q0gHVcnKuBLF5gG_g0nfss03QEsWWKz9QzANJC-SFgzKGckk6I5-TGHen4aueHSGh9mZHyZC62QxUtYkHvXEdK_SDG1DTDRtYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از نزدیک‌ترین محل به مقتل رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/692910" target="_blank">📅 16:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692909">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVSox7gv9sRpN13-4qzY2zCb_wO1E6wS_LUU74CzLuUShN2OhWx-P1ntUPIvUHfr6uyW8ZbggOmhGyWF50Z8QzieXpINPyG1mbTcGCYD2ccfoHVG34b1k-41YtHnixtdCuwwdrcV1Givt6nVbFWNqsXafTannCkvQ3gwvoc-b9oiQCfHOmYAPkkjTV4fg_-wbMjJFQJS_IOJ57NEkbc-YMJjlGZUTLt4uuJ_VIfeRVZSJiPqNsrWWc9A7lniSHM9aMD__E7wdW6OAxutCninl8fwalyRbTxrvNmmKqb9oGoW_EYzj3j0SDLoYr4R8bMvc0AT1WXcFplYipqLscKLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از خونریزی داخل مغزی؛ فشار خون بالا از شایع‌ترین علل بروز خونریزی مغزی به شمار می‌رود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/692909" target="_blank">📅 16:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692908">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj3GRJk0Kzl18Cyc1KEOYZdsn7C7bCgrwvKU_PntFITCLhl_hyKTMYKAY4vUzKztwvpLO2-XA6nG2kwqB_xlLc-lmdULWk3LQul-__kmLl4qwTzccF-WkzbJd1ncInf-2W6u0hWy8F_tvhnd3IM8CpJ4_Q3zAiKFdzrWbHDnyYHWDU73GEFF4_ZlMhgaJuhLbO5s4jP7h-PMe2sWq-l8uFwA89IMN7sWIJBHOPGSMezrhrT1Db6lLL3EjCabKaP96V5gcxJufKEctfnSEumI5qx4Lov4TqpIctIGWndlw3PTneKzfa487ZtneF8tVSvd1NS-Z3Ruqcx5JwOFtzX9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷۷ هیئت زمانی که نتانیاهو سخنرانی‌اش را آغاز کرد، سالن را ترک کردند  کشورهای عربی — ۱۸ کشور  سوریه فلسطین اردن لبنان عراق عربستان سعودی قطر کویت عمان یمن مصر سودان تونس الجزایر لیبی موریتانی سومالی کومور  آسیا — ۱۴ کشور  ترکیه ایران پاکستان افغانستان بنگلادش…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/692908" target="_blank">📅 16:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692907">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
نفت در بازار نقدی به ۱۲۵ دلار رسید
🔹
قیمت نفت برنت در معاملات امروز بیش از ۱۰۶ دلار بود، اما قیمت برنت نقدی (Dated Brent) به ۱۲۵ دلار رسید؛ فاصله‌ای حدود ۲۰ دلاری که نشان‌دهنده کمبود عرضه در بازار و اختلال در عبور نفت از تنگه هرمز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/692907" target="_blank">📅 15:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692906">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8afb82f10.mp4?token=jp1LCY3LFYYXqoKAQ0G-nReGIqJKcMIpyl6CRVsrPq-IINHnKZUGv9qQCiLrfsB6HQ_hMjr5cz3dXYuPKEMUFoyWo41x-qvPOAbBFIQggJ3hxI2OUS5aBi329vMGhXjLylqDmNQIM8MqILxzs60VX7he4go1iVGLTLcfc6klogMI_2fbE1Xr7u_Ps81rxnVvn8kg_UUkuHtfOnVgONIlTpNgABerbzrCtS4SbWDoTLYkCyIfkGwwIKvUTpM2x04ojUd8UhMmbzq6A8BbCZBLPIhz9Zwyo-eNe8cHQZ0InmpSxQaukEncLv76wzG0V5TqmxAxTPJ_zX2k-qV0TzrzLLs1oHAflQYRCovN-YTRWga0NLLl33PofA9I05LgTLWSePwxmK_75kM8d_gRVtIlExIiv1ckYvP3iaMbN47UaCMvaOmsuwDaHaU8n-7jPBYYFM7m64jAWyI8J5i6oL4yk7-ETbo1JM4q2_2WPTSDlfbishxVBZCPHL3p8d6L8o087DEYntkOW1xkDTi2fNIx6ZEQqkQt_OcXTc_jtKNqNRfW_9L8DYKmlA84_lAEiDc6zu8sZEsUH25NV9NeV4WdwHMjq8PprbTGI_KrCLELJ1swfpl4TzjtPsZGCfbSUE7gmvCslzF8Gx9bAJ1OJAeVv8eEpwDd8eJ6mcXppDtjkQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8afb82f10.mp4?token=jp1LCY3LFYYXqoKAQ0G-nReGIqJKcMIpyl6CRVsrPq-IINHnKZUGv9qQCiLrfsB6HQ_hMjr5cz3dXYuPKEMUFoyWo41x-qvPOAbBFIQggJ3hxI2OUS5aBi329vMGhXjLylqDmNQIM8MqILxzs60VX7he4go1iVGLTLcfc6klogMI_2fbE1Xr7u_Ps81rxnVvn8kg_UUkuHtfOnVgONIlTpNgABerbzrCtS4SbWDoTLYkCyIfkGwwIKvUTpM2x04ojUd8UhMmbzq6A8BbCZBLPIhz9Zwyo-eNe8cHQZ0InmpSxQaukEncLv76wzG0V5TqmxAxTPJ_zX2k-qV0TzrzLLs1oHAflQYRCovN-YTRWga0NLLl33PofA9I05LgTLWSePwxmK_75kM8d_gRVtIlExIiv1ckYvP3iaMbN47UaCMvaOmsuwDaHaU8n-7jPBYYFM7m64jAWyI8J5i6oL4yk7-ETbo1JM4q2_2WPTSDlfbishxVBZCPHL3p8d6L8o087DEYntkOW1xkDTi2fNIx6ZEQqkQt_OcXTc_jtKNqNRfW_9L8DYKmlA84_lAEiDc6zu8sZEsUH25NV9NeV4WdwHMjq8PprbTGI_KrCLELJ1swfpl4TzjtPsZGCfbSUE7gmvCslzF8Gx9bAJ1OJAeVv8eEpwDd8eJ6mcXppDtjkQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از مقوی‌ترین ترکیب‌هایی که تو زمستون هم میتونید بخورید
🥛
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/692906" target="_blank">📅 15:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692905">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7324ff78ff.mp4?token=jCZ4BljoqaDceGi08OTt9pFht5lHlz6Q-HKsgGGhKXVYhz-k-_GGUrVQ0wXX4qzsTfX4UPyAEFI-81e7wt9wIh1adU6-0bZvK1gJr-7X8ebXW1fhDupIX0fFWCpzZDXYPkKOM9YNfPGjiPq5hozuNLxmzsKYJgT-nn9N7tC0kfbL_Wl0Clk35sRf22xQ5DpzOTrkZVLdbQMKXQfeM-Giv_BBFCEby8WQ1DLUHYH4YNonHZrVy2GE0pnwyNJSjxAa25SsyzTM2efJKezMeQsTwT0YJKUeVcT-l5sgsEEB49HwYXzj8cKu8vb22M84F1E1YanJHjIk978hV9fmglQofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7324ff78ff.mp4?token=jCZ4BljoqaDceGi08OTt9pFht5lHlz6Q-HKsgGGhKXVYhz-k-_GGUrVQ0wXX4qzsTfX4UPyAEFI-81e7wt9wIh1adU6-0bZvK1gJr-7X8ebXW1fhDupIX0fFWCpzZDXYPkKOM9YNfPGjiPq5hozuNLxmzsKYJgT-nn9N7tC0kfbL_Wl0Clk35sRf22xQ5DpzOTrkZVLdbQMKXQfeM-Giv_BBFCEby8WQ1DLUHYH4YNonHZrVy2GE0pnwyNJSjxAa25SsyzTM2efJKezMeQsTwT0YJKUeVcT-l5sgsEEB49HwYXzj8cKu8vb22M84F1E1YanJHjIk978hV9fmglQofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
با اخلاقی‌ترین ارتش جهان آشنا شوید!
‎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/692905" target="_blank">📅 15:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692904">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
اختلال در چند مسیر ارتباطی اینترنت ایران ثبت شد
🔹
داده‌های پایش شبکه در روز جمعه سوم مهر ۱۴۰۵ از اختلال و افت کیفیت در چند مسیر ارتباطی اینترنت ایران خبر می‌دهد؛ هم‌زمان، اختلال اینترنت در استان‌های مازندران و مرکزی نیز در سامانه پایش مستقل آی‌اودی‌ای ثبت و تأیید شده است./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/692904" target="_blank">📅 15:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692903">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLUW74Azzsin9vYDdkiD4N2A59cVuYZrFR4QV-5hv2GXnSjQ8zayq9JQjRbgDSqVofxFJBV40C-O5YvUlYS7PIvDt0lz_iuQQN7IHznnOU9pTEr9w0pkrKlP4q7wUixEg9Vb_AjZYpLpbBnRO8oF2wsf9-dokRPD7L8v3p-ZHNmpc8XBZWcpKnks6GH_m2ttvBPx9GAHUY5So2rilwam0LSBuoGv5WoweVck1IlDXnojeVgCilyDoUWTWEcDnHjopoei3z6w1NA4BNpDDoyZTgtNvK8Gckcyx7ch77QLgY4uzX4JmLwF_aUSdwbEUQGE-4LcgObCfC3_GCdoK-p9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف کتیبه ۳۴۰۰ ساله مرتبط با پیمان قادش در ترکیه
🔹
باستان‌شناسان در هاتوشا، پایتخت باستانی هیتی‌ها، قطعه‌ای از لوح رسی و خط میخی مربوط به «پیمان قادش» را کشف کردند؛ معاهده‌ای که از قدیمی‌ترین پیمان‌های صلح مکتوب شناخته‌شده جهان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/692903" target="_blank">📅 15:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692902">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
نصرتی معاون عمران وزیر و رییس سازمان شهرداری ها و دهیاری های کشور از تشکیل دبیرخانه‌ای برای هم‌افزایی سازمان‌های همیاری شهرداری‌ها و سازمان‌های میادین میوه‌وتره‌بار و مشاغل کشور خبر داد و گفت: هدف از این همکاری، استفاده از ظرفیت‌های موجود برای عرضه بخشی از کالاهای اساسی، میوه‌وتره‌بار و مواد پروتئینی با قیمت ارزان تر، کیفیت بهتر و سرعت بیشتر به شهروندان است
🔹
در کشور ۱۶۲۸ میدان میوه و تره‌بار، ارزاق و پروتئینی فعالیت می‌کنند و در برخی میادین میوه و تره بار در شهرهای کشور، کالاها تا ۴۰ درصد پایین‌تر از قیمت بازار عرضه می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/692902" target="_blank">📅 15:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692901">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سمینار آبِ ناب مزدافر مؤمنی قسمت سوم</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/akhbarefori/692901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
آبِ ناب
؛
قسمت سوم
سخنران: مزدافر مومنی
🔹
02:40 آبی که درمان تمام بیماری‌هاست را بشناسید
🔹
18:00 افراد خاص و سران بزرگ کشورها از چه نوع آبی استفاده می‌کنند؟
🔹
26:40 آب حافظه دارد و اطلاعات را منتقل می‌کند
🔹
32:50 تأثیر ذهنیت انسان بر روی آب
🔹
37:00 شعور آب را تغییر دهیم و به بهترین شکل استفاده کنیم
🔹
قسمت دوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/692901" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692900">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2S1o8VmO1b0tZiBZIeirtlVTG-oWB3JLNiRn83UDUxWaRkjcvHbb07zlqNpzXp4EtGv4AnsCBkPrEeLvkpgoMrG5cSXArzkzgwEYJTtC1qkVGKJBco0NpPEtx5BXMGnWWSctuh7kpEbN6gtc8SAgCClWTNRdG-c7HXz79LX5IVLgsxIX8lYKYSTGBZeyNxEOKnYEcN97d6cNdZzM-mjt6TygdEIs8405w5snDxbWEPqjD3fG8BUbyh2L-wIGkRn3gLDgCJgC6WusrtxJCb5feLJqPiDi29eRObn5UfGycw1vH7eZ1LsejWKzdhjcRAT9_GIFxel2rkuloOdpa-Ldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | جشن فرشتگان
🔹
همراهان گرامی خبرفوری، شما می‌توانید با ضبط یک ویدیوی کوتاه از دانش‌آموزان خود با لباس فرم مدرسه، در این پویش شرکت کنید .
🔸
از کودکان خود بخواهید این جمله را بیان کنند: «کودکان شهید میناب؛ ما راهتان را ادامه می‌دهیم.»
🔸
ویدئو های خود را به آیدی زیر ارسال کنید
👇
#جشن_فرشتگان
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/692900" target="_blank">📅 15:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692899">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz3hRO-lj11KjrCatx_SPxOgx0ZWct7OneZ7paSjKbOC4AngLJi3-J3r1IXMQCAVvpR7fuJ0iTQXy1JGaUAxS5_xEb9r1cbdlnKcC4dab6MeUbPXjqqKKl9jbTn9lp2W2xwp74IPGX5EwT6XvG-Jw-tiIYThM2Z_hXSJBZGd5axzI23nYyXUa05xgAdmT_gHYoDYqPSNcoTdtk0jJ2fFiTlHSev9P9EEmJQPRGbbbZNbryGv8b4i7pTU7LXMzJE53IRrvX6dmhT4wNlrCIX15H_DNKy5xnW995CpsZorukZjp8M7AhlQqrU76eSwiGEiS_VdFz8opFrixl3rM5rxZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فکت‌هایی درباره تخم مرغ
🥚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/692899" target="_blank">📅 15:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692897">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
خاتمی، امام جمعه تهران: کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/692897" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692896">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ9asUvKCb8SkeyCIX1wxzIZ0KDiRspuU15GkIwIFFEd_Ia_pAVMqwBrxzQHz-FhC47VH0nSO58JBZsw2NX94URrYt2_bEwI09SvWcIb83LVmvw5iCNi22BzpXZWwp_H49II-aAw_mVfMYK7_WAi_G8h-3Hebbj8B8rW__H9hEmtoppUl1D6eZ_7sk2xvXXZqkuLkc2iec80Yll_cG6NlNnpYIlwGRdWuM2pxyFe2AQybsVOXzk4SQ8Bify7eRQkYMh_ciGlHgwbBR_jI3bwvaPwp1C7W-WgvBTA-hnXga6lJ5fHSryCdsiX8BQSaUxgHvOOOA8tAYqlhhR7DJvniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قبانجی: عراق نباید تحریم‌های پروازهای ایرانی را اجرا کند
🔹
امام جمعه نجف تأکید کرد اجرای تحریم‌های آمریکا علیه هوانوردی ایران از سوی عراق صحیح نیست و از دولت این کشور خواست در این زمینه تجدیدنظر کند. / خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/692896" target="_blank">📅 15:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692895">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1aTPufjNGNqMq1yHHOk3NwispYtOo6CeO0zFSJ37fbll-ZCRynDgJGrZIADL53AiATOvp7_7lcNKZxu_EDn3wfq5zZhZ6HneDdBzzRR7v9KejuNMCNo_qCwWYxcGvu4RtJq1ufao4DqT1i0DlZnS81OOHI7ekr4C7pUwefWLil6dM6jp0vicRMax3JDYHl7bIMAvOlUI_ss54CBmEUcSWdeD4rineN7rdl4UdzMne5yIIDfFO57oaFFf8ni2xk4LsRF5oL2HS4RfBYbvrUDuvxU_sDvPfRS-49rBvLF2xHkfp4i6sm3PP0pHxgHnl9A7rkiOi1Uwu0E3GmMp-Eo6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حضور وزیر راه و شهرسازی، پل‌های آسیب‌دیده هرمزگان به مدار تردد بازگشت
🔹
پل شهید مویدی (گریوه) به نمایندگی از هشت پل آسیب‌دیده در جنگ تحمیلی سوم، با حضور وزیر راه و شهرسازی به بهره‌برداری رسید.
🔹
بازسازی پل شهید مویدی، دو پل در محور کهورستان، پل نیمه‌کار، پل سه‌راهی منبع آب، دو پل محور بندرعباس - رودان و مسیر رفت پل رودخانه شور در مسیر بندرعباس ـ حاجی‌آباد به اتمام رسیده و زیر بار ترافیک رفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/692895" target="_blank">📅 15:12 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
