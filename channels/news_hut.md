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
<img src="https://cdn4.telesco.pe/file/bXca-b8SWx0tTpih1-aWrk_ISuEviuD6adU5B5HPnDPgTUo4dYNkWkX11Ad6rPLAfkUU_12Zs6B6-lRcfvS__Q67sMkXfUw2WAa43yvkzwjKTgHjEOHqoqwAjrukIdM1Il8WHLxkeLWuNHSmsW5ecFXlnQnHtacB5lkhp8CTg0-lWCcKxld0PmpWOOwSZ8Gp0A6fWYrObFqvT7gKpcMgMaWWifcYZeF3M37_mpDtiSdJ3GajspuMv5GUIAHBoNjKs5A9xvRz1axTG4FEaqwqNJsBkWYlNd2FGdmAlVu8l53L0yZKxjjSuQqzSTzTkihcI-2n77rETxU8f6flWfuxsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 157K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 23:45:45</div>
<hr>

<div class="tg-post" id="msg-68667">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO0Rj7_WIQUWvQ4Z7DyNnQktYJMiZNQGOsXdUCCkK5jlgL3PrsoWOKkvwCF9-BBFFUxM3EaTgC40CpwuRNTTpbUh9NXdFUmnOUYWtKMPXJj92Px08liq54v6DAhKhAJu7dUSqptiyu3HdgcRRXca2siLqnGxFTd1lApjEiBgsvS14uk-B_6SZm4UAjWNimdWcaFE10Rg1GcPYmMsCKtY9ArJvyz6EXZ7f4R9-ZvbtgcsFO7sI48jpbSEyZiAHYLsQgCFtNLB5NIdpFHribJiboPSPJ7Nh3fTVHHZoz6nI_Widj0RYzstc0JAo5WwZf67wQKP-9ifFfIVB-lLxR0n2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را بابت نقض تفاهم‌نامه (MOU) و اقدامات تروریستی مداومش در تنگه هرمز،پاسخگو کند.
به‌علاوه رئیس‌جمهور، ایران را بابت مرگ اخیر سربازان آمریکایی پاسخگو خواهد کرد و هزینه آن را از این کشور خواهد ستاند.
این ضربات سنگین تا زمانی که رئیس‌جمهور تصمیم دیگری بگیرد ادامه خواهد یافت، اما مذاکرات میان کشورهای ما همچنان در جریان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/news_hut/68667" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68666">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
دو انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/news_hut/68666" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68665">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=TLyoEU_BhbbLfy8I7DLePuMsljgYaP_qXdXSrzd6NeLgni7XuAODWFYDJ2ZYLBmjtr0eunYSMMiRirwkOufsAB1NAwixd_1TyLFRuLgdNhMvlMW1tjn5bdQ3YtdX8-PolLMhBjIKPYq4Cst5Z6kHequiA5Ol2ubsm4ceDCIhUPAld_T4ousqegHTZefsqQh3vTm9xxN9LtHu76DINIX2wA7r7XxWPLH62suUgvoL_y2bwnZu5asNdvQF4tJ2_Ft4hPYnjxN4UUJ77E1_8idyqn31QJQwqNqs5wne-n59qKEhBIZMEoNzzvJ5N9OswILEPG7gBLu5vn0ago7iVEC_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=TLyoEU_BhbbLfy8I7DLePuMsljgYaP_qXdXSrzd6NeLgni7XuAODWFYDJ2ZYLBmjtr0eunYSMMiRirwkOufsAB1NAwixd_1TyLFRuLgdNhMvlMW1tjn5bdQ3YtdX8-PolLMhBjIKPYq4Cst5Z6kHequiA5Ol2ubsm4ceDCIhUPAld_T4ousqegHTZefsqQh3vTm9xxN9LtHu76DINIX2wA7r7XxWPLH62suUgvoL_y2bwnZu5asNdvQF4tJ2_Ft4hPYnjxN4UUJ77E1_8idyqn31QJQwqNqs5wne-n59qKEhBIZMEoNzzvJ5N9OswILEPG7gBLu5vn0ago7iVEC_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یه برنامه اینترنتی، به ایمان صفا (بازیگر) یه جایزه 12-13 سانتی دادن؛
مجریه میگه اینم یه هدیه کوچیک از طرف ما که به ایمان صفا برمی‌خوره و میگه بخدا این کوچیک نیست ، اعتماد به نفس ما رو خراب نکن...
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/68665" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68664">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5swn4zV4jderke27EADSc0hnIWduujhKSJct5Prcs0wnUt0O8Ahg53GRB70oSia_YoMeuczI_adntj5LTZbrFSPDohGX2Rla7Y9HGnaStqJm9froCChLv7-xL3qHO6QeLGwIkq6FYTfN8P5FQkEMq46nrdCR7bOXKW6PFkqlcQHw5DqALAI0t1gneBS1MgcuNB0f_MXKYGh-emTUp-DQNm-iP-gg7WkGT6dffzMZjVOUM-rz_CoekjIYReL5fSnK0VgXF2xRWOddr69CY-RzB6UgNkUdBZ_obrOxvAsZBiWYZwQLorzV1g443xfMcgqmnXj9uil9zPZ4OqSkTZsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
گزارش وقوع حادثه‌ای در فاصله ۱۷ مایل دریایی شرق دبا در امارات
.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/68664" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68663">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
رسانهi24:
آمریکا برای مرحله بعدی کارزار علیه جمهوری اسلامی در حال آماده شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/68663" target="_blank">📅 22:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68662">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=opzBpD3TkHJWYZ4n6jTxrjaHW39mz0fXBVXKQug24ui6IgESyRW1wWwESp42xBbxnqbONTl__zAziYSlPU84frX9Yci8QVvBy1Q3iMW-1YUUD4lJ69oZ6YqHMNlTJJbyA4Blg1t8camqXdJWnnH0NqqP7B1h-dKMcfjgDjfWES9-a7WijJLpgHaduwxKiokMmVTx0CSMHf19r-hPdTxKZqUeEZ9DwI9Wfzyrcmk3YuRaMC1ldGf_r8BKEyx0hfP-8KLDuzElOv6ttGN3bzBMuFMV2cAJEazCTtbGqRuYHh0IlHSDr-x62NzrM5jAr_ZsQPHMK72N7AjQqRzUIjWzvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=opzBpD3TkHJWYZ4n6jTxrjaHW39mz0fXBVXKQug24ui6IgESyRW1wWwESp42xBbxnqbONTl__zAziYSlPU84frX9Yci8QVvBy1Q3iMW-1YUUD4lJ69oZ6YqHMNlTJJbyA4Blg1t8camqXdJWnnH0NqqP7B1h-dKMcfjgDjfWES9-a7WijJLpgHaduwxKiokMmVTx0CSMHf19r-hPdTxKZqUeEZ9DwI9Wfzyrcmk3YuRaMC1ldGf_r8BKEyx0hfP-8KLDuzElOv6ttGN3bzBMuFMV2cAJEazCTtbGqRuYHh0IlHSDr-x62NzrM5jAr_ZsQPHMK72N7AjQqRzUIjWzvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68662" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68661">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONiJVpW-GW-LOYLnyUAdtz7VAJiHf81TnLLQSEBlhFl43xu_2wLdC3GbjvDRW-t0H8fMptNzD9-RGWimhXxGryCkAgCiZJ2nsgy2tVswBznQ4UjlqXXEUKA7q7y33-L4IbjhhA9agrTOnjORw1bY5c3AUkt9uRhmRe_BHAS1J0CumRyl9IydAW2XDZRTN8jAIVOwTmimXMbNjm4j4cSX2McLGNywHlB2fvFq0g9lx4JeYGn09qiJhj74Pwo8BUlRlriZ-QzJbugTa5d1TASRgwQ5O_nrPa8jyw584k3GkMYWaRwiuCZuJECUHAlbz2E_Doh13t6Fw65-SgGESXSu_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68661" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68660">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در تبریز؛احتمالا موشک شلیک کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68660" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68659">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
نایا رسانه عراقی وابسته به حکومت؛یک منبع در سپاه پاسداران انقلاب اسلامی، که نامش فاش نشد، اعلام کرد:
نیروهای زمینی ارتش ایران در نزدیکی مرز با کویت مستقر شده‌اند و به نظر می‌رسد که نیروهای مسلح ایران در ساعات آینده یک عملیات امنیتی زمینی به سمت کویت انجام خواهند داد.
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68659" target="_blank">📅 21:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68658">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVi_QND2zsADdHFfpLB-EA4BCB-7n3-Q5JH78cGjS2iCEmCNARf9xqWF7ewOhEYOdEKQ3wb1iJuHgmQre0-1sMewXvQYD5FXgIRxz_cQAUM51w6oHyblsx0_qDLTPVyD7CKvH8p-jSx6DN_MMcE0INC2Sm3wRJpO4I6RKbAasGkeuezq69cKM80rX-JRbmiXF4tNyc_8p2Nj9ixbWm5MpVohjt1zy9WTvsacc0c8UrAlHNl13K8a0Fc7K9qA-FsVEt23OPl57MIkKHU8P2Yott7QOlGuTbJtPj_NU62HepQD6GwdFw2opLtTc-ztKAGu_xnTaW2TA86t4haJUGjWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، توسط شهردار نیویورک، ممدانی، بازداشت نخواهد شد و «اتهامات» مطرح‌شده از سوی دیوان کیفری بین‌المللی علیه او را در خاک ایالات متحده، «باطل و بی‌اثر» خواند.
«بنیامین نتانیاهو در دوران حضورش در ایالات متحده آمریکا، به هیچ وجه و تحت هیچ شرایطی بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را به قتل رسانده و طی ۴۷ سال گذشته، سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این چرخه بی‌سابقه مرگ و ویرانی کشانده‌اند؛ مسئله‌ای که رؤسای جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68658" target="_blank">📅 20:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68657">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW21tcHFtgeqUb2qG_I03OdDueM_v0d0eDooSC4NG4ztT8gDliz118sYB-5srf0CRw5JOpJCBWkzxg-Yyo7kv3HeLVC180H9W1B9O0Hp1w8cLovLb4tj-YsPp2t0pVgy3X9GvPnPFA1ca1t_ZkwXlXOCIrm0WQ8zH7TXq7MUIU2Ss_Rwh7QqdOA3aXwuDdHFekSjmVL2gfLVZT0Ef-bmm7JA7ct0g1Mhquo9sFT51q-vG5Y7wefY6FBfl4on2fFair5c8XlNHQC8-hSFKcwY33ZFbGrhw3CGVIig5os6tuIjY-bvSAfc3EUsJ4G7dsIkHY1jeoNmYHbg-QknGL8YNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین و چند برابر خواهد پرداخت! این دستور به وزیر دفاع، پیت هگسث، رئیس ستاد مشترک ارتش، دنیل کین، و تمامی فرماندهان نظامی ابلاغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/68657" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68655">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rptRd1jPA8ewvP4zeCtqAfWcPN0f0KUDHa0r8FEJv1wSW6IHCXGXbYKNaRLm3hatqzucz6Fevp4YSeYhRvhHywSvaZ5MXfGV32ZUll9qICN5L9EL5_8OfhO6bBL3E-ciyZiMKc2HXE8QTPRX_6RIICiAhrhZ-rsnPrOtR681BtNtgm_y5cHwpY4dPAPDAgg0knibc6XKyczSr1pHOZ-CFkUdGGs-4sIw1fDEXci3oKm7q_nt4rXpWS-9wMxYY1wrQe8C0-MlOg8sIx9q_js8G196elL-C_mYN7kkRVz06odftHLgaESAsMrpfYbXACYNyg55F5g1zLkCz2kvhI_U9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXBOe9HoUl7S9iD6-2VLrRag1-KebBsstXlZz_FZ_vcY4pZEEai-mN9z3N_CQGwqHmxeMzF3omfbKSUXmcLH3ifYN5rnChDSYCXGX-kOkgSBHbW5NOy3ZK6wiDzBb8xPuSyeFxmkvQRDVpdqElF_D5uyiCH2UcYjUm_fO9IUWZfj4u-GvKjmJyyJnQQWAjVrwvAQNHALqMNf2wzfjgTu-2AVATs4VkNxyxsIiNL2w1g9QvhF6H9EUeJHbtYuLep7CedyNOwamvX1k6OhBHFxN6oB_M6AC0Z9xcMtcO_TzfpXaX4DtmH9LMWCFlHk9GtDxE9N7_yjw7pgQAeQxVQDQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
وزارت دفاع ایالات متحده هویت دو نظامی آمریکایی را که در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق سلطی» در اردن کشته شدند، اعلام کرد.
تایلر جیمز فیهان، ۲۵ ساله، اهل هاوایی
ایزابلا گونزالس، ۱۹ ساله، اهل تگزاس
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68655" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68654">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MssiY5x3raeKrydzdth-mpgHILvkSzX1T5gtqedCFteQcwilwiqpKJC28SrNfgMcKuH7-t31K8kEvr6S_Ni109aLMpP_6J4qomYni6d5JwOTu34HotJfAYqW23EGXGIClMyROL7EjmQ50f4LPdQxC9NEB0IAFsdm1_4VA8HsQu5K5mif9bbe_YoYi-Az9q19-fysnavJWx9mXujv7cYSdb96fWzePavI8Fm3iw9jBDlwJmB2vHm33CcomL5veElEPibx30ynIJ6FWvKmI10NT3CFyPgHZTE9OgiXgjMWFYh-jQy5L7WLL1p8g_RSqvGVmDDWLpx9lBJvyWDbNpps8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68654" target="_blank">📅 20:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68653">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
یک واحد صنعتی در حومه شهر خمین حوالی ساعت19 هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68653" target="_blank">📅 19:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68651">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4-bH0-KXXHTt95nweTCJYnA7avKwHPnoD9bjxK6LOWFmFKLi7vqL1CmiglHZvaMww4N3qlkGABa3vXIl1YK-EFyEUqpPe7R_FycU2dkheE6ZC6x5Z2AGFS6bAibP2WkvmVto047CuqwhwKYY7Rnb0uLFkRbyvxxKasO3YuydnD11w4UOhTS0CXR9A5avuP_sAMj-Fey6HIx-kkrFfBeCoDp8ILuDoLNQ9vsTsRLH7ZkYAl2nnrOp0v4Lxx6UVsiTxymT3Xrggz1FyeoQ0NNcvVnNcvkrlIWVQlDOVF2K-zngiTt2oteHiKU_nE4OpADi_f2aZPMfwsepj1QjsBaTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=aX4aZeI8IKd8xzXN77TNrj-QVQ9V8T_EjwXldF8YPmUm8VJ0o1ZdT2PbElDDjvoCWgn56FPYK7-Hmmxu5xSWXtJgOdvgs6aKbeffrug4gi-AoqpBLdIwc4sCCrAQKGphZN52YcRrQl17fWVq109xBZd-h9DEWwo3zoEN4gblDPckD_ufcEnbjG3zqlgk8ueBuG_bcOheij_v5LX_Uk55LiH0Cw_2j7XrMCtPi31b17cSmORbiBy8_taN0nq7ZhstK1LheyivlGy2xqciQ5RiuHsTR1yCuReUEmCKDXbu6rjAkeP3QV4L2qDc7oVlZLPnUO8RQCmgbLYIMh503HqYtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=aX4aZeI8IKd8xzXN77TNrj-QVQ9V8T_EjwXldF8YPmUm8VJ0o1ZdT2PbElDDjvoCWgn56FPYK7-Hmmxu5xSWXtJgOdvgs6aKbeffrug4gi-AoqpBLdIwc4sCCrAQKGphZN52YcRrQl17fWVq109xBZd-h9DEWwo3zoEN4gblDPckD_ufcEnbjG3zqlgk8ueBuG_bcOheij_v5LX_Uk55LiH0Cw_2j7XrMCtPi31b17cSmORbiBy8_taN0nq7ZhstK1LheyivlGy2xqciQ5RiuHsTR1yCuReUEmCKDXbu6rjAkeP3QV4L2qDc7oVlZLPnUO8RQCmgbLYIMh503HqYtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دقایقی قبل شلیک موشک‌های بالستیک به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68651" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68649">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHfasZ7Fer_cFWwKBY3IRepd_ePE3btlGeScFjWCc8Zqh3SVzRVnrZ2p5lsVl6bqsGf4-maSq_kB4MysXe90nvCuv8rjQeJzdXi9p9_LUWIbn9vCkNK6IEbcUP4hCNTlmwwvZ24c9Jiqu5PVbsptyAPtrWAwGDOVLKcw8Eti2A4T4YBHat8UAYfQkd-SPhl4sYWkrPdXqrCHy0VEs7nUntEqbtOng-ELosgSvTrNiFNQQnFX_Cyz4Abg0BhxeSRITB_nvX1skYJ2xvvWg3FmBLzYFTDKAET6gjxXG-OHBm_LroQdoFsbNOv-m-4BTiZpGAirckX-krrXRfpHV2U-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=MQUtxDM6x1LeTcCyCxeubptYwHNX5-i6AQqlsP7zgvE3S6tIbzIyJOzDDwUrEwEwKTjBZ5DN0mCmBiUia7tSZBJSMkOHgjRi2rJyH7hEML5zqeOIKCEt-O24RqclauCj3hZGYD5P7pabGElY2SJxyQgYB_wamXocB3rEjbhajZg2DxXw3FTcq_cPdjQu52B1_eL0XfbvWdG81fWE0bBC5hj0RHcxlaAPsnPKWX2Zub78N1RfCq_sw46RBm9sdct9ZdhucKmwq8IYs05vJm-_FooeT-5rftyWdcb1ohwT3wgso2_1H8JuXpA1lUDYyP7nCziSDw8aZGV87XrW7RrsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=MQUtxDM6x1LeTcCyCxeubptYwHNX5-i6AQqlsP7zgvE3S6tIbzIyJOzDDwUrEwEwKTjBZ5DN0mCmBiUia7tSZBJSMkOHgjRi2rJyH7hEML5zqeOIKCEt-O24RqclauCj3hZGYD5P7pabGElY2SJxyQgYB_wamXocB3rEjbhajZg2DxXw3FTcq_cPdjQu52B1_eL0XfbvWdG81fWE0bBC5hj0RHcxlaAPsnPKWX2Zub78N1RfCq_sw46RBm9sdct9ZdhucKmwq8IYs05vJm-_FooeT-5rftyWdcb1ohwT3wgso2_1H8JuXpA1lUDYyP7nCziSDw8aZGV87XrW7RrsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی در یک تانکر نفتی در تنگه هرمز، پس از هدف قرار گرفتن آن توسط نیروی دریایی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68649" target="_blank">📅 18:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68646">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJyqZbUu29x2Jn4cuNsmm7ArHN5R1Mmn78WJiNdkGCCuvYn6mWGKTZbuqvmsUi_2gkQb9dxFj15m1FbjemVHWcsBFx35GhBS899B0QZELSb06UKQzFBBd6WUBkwKElQF3yZUVntbOeodyKAxZ2YS5RhBKmLnt2GbByD0jlxHuA2Vd6SFM5Xsor_7LVzGmJwl4rXS-H17nD7KaZ_sygmdJcDLlVksMiEiToOYbE_-Ciy6F7x3T09a2-6Kiait_sYcSgj6QUIyP9mpznqHuAVQZPN0YyYGjS4mokvnF-SbnsLo6DKQH-eyQ66Z_8TBtj5zchA7-QtK99-QWM0C-1OSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkPx2zKWb61ZoCYmPzZDeqkhoUy_ciXF6GuXVDsyofozN6TXv3wgcNAnT2GJMbr84Y76LyzXwhl35Z348pIhHPRCZbInvJSH8mvRllPAPvIzPFTnvbXnyhUgdmtYmE2vfIw8FrTFwcHfzx1keDM6w5lm559E1vCqvFBFWunc-9KLJBzygJlDchybv8qJbDbNS8-35xll07NdPtbCc26afPJAsmMlSDMlmWD41t5KXB0vgzl2qPR5qeglw_fFhZ0dNe-20Lt8jioxAxWnnqx8dUNt4l3x_jhRW7tBo4y6ebFMUeHR9n8zH1LbhoE9ZOQjce-f_E6Ryg1Iuag9QHuuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T89IPaLjuyknBnzQLY6fuTpQIT9Gwm-Ni8_rM0VoI55FnuH2D8KRudCIQwYUk0IcGxCGGOmRxjH9MD3AQu3C-1e9iUl3Rt4dTHjGIBVlm5KbjsHxAgAgVvrq64cPhtXBy581mKp6rKYvsMhXhiOk2Yt1frjdqowLo3YlKy4SlVv4XqIbf9t6QKE51rsrO8WWmYkH-90cHAlNLQpvbP6ndaae_obMMZBJjkurM4PSZYiNid6dlnk09Zwe9TZWagrW2Ds8B0Qrd2nWAsbBRHGqZHg45RGqfPrTIakCWq3s1U4WdvMFJO7FF9qtIO_fitzXYQXiCOYtYlU4-lV6n3heLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
شلیک موشک از شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68646" target="_blank">📅 18:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68645">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68645" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68644">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu-CSegMEF6RU30E6v21_fhPtedUJz1i6Zuu_1soCmUwKvBcrR5leXjD1cl-n_zj3MEVGyf_LWu1tqdTv7PRSwxMotbxJIwN1ZE3RvkwSgWmjvcRQQF2bu_pnmdy5TLzkqqWCEem-sWAyI6RVSn1EMM_2Y4d9VfwjNq8DOoMjzZoPRSnfwXTiy_bvPDwzPhxWpyR7zRmcbY2Wx6cXB2kXBEIY4kLSasWSwrMbui6xg7F1B0SL7ScNx8nw9N2gF55J1d6Bqr7f5Vgpr__AijY9VA0JY8mlZe1sOcy-ygu_LfPBpr01JgREj5loAGZHg-JizU41TvdUNJK7466piV95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/68644" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68643">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
❌
رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا:
یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68643" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68642">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=uhMwWfDOTAVgfUNUm5XdbEmL9v6fLSZdUXYgLKCzT0zQm54dKrN_gEvn118qao03caQz3mGz_AfK20k9B-i5uaXcdfm0p2Wl7PwKvWKNCRcb49d72SZWTqjZPmZzVw6cqAVVP6hvNFyTUh2kILKfXJf_ENqzbxkGtaNHC4HddQRMk9XyjDTvDKCi2UjjRtbLqFCRjDQCQK-5gSnqbPhyXrJ9KoDb0wNd1efTlgpsDQRkBNyZRos7sVVqjUsheuDAIsl-FnE_ASb_rYzS7Xv8Uax7u59n0a4vraqLK4t7GBTRSAyybX4bPctKeTUnQ9MfXNU-D_qlzp1IxfrOdu0Piw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=uhMwWfDOTAVgfUNUm5XdbEmL9v6fLSZdUXYgLKCzT0zQm54dKrN_gEvn118qao03caQz3mGz_AfK20k9B-i5uaXcdfm0p2Wl7PwKvWKNCRcb49d72SZWTqjZPmZzVw6cqAVVP6hvNFyTUh2kILKfXJf_ENqzbxkGtaNHC4HddQRMk9XyjDTvDKCi2UjjRtbLqFCRjDQCQK-5gSnqbPhyXrJ9KoDb0wNd1efTlgpsDQRkBNyZRos7sVVqjUsheuDAIsl-FnE_ASb_rYzS7Xv8Uax7u59n0a4vraqLK4t7GBTRSAyybX4bPctKeTUnQ9MfXNU-D_qlzp1IxfrOdu0Piw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68642" target="_blank">📅 17:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68641">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
فارس:
خبرهای اولیه از مورد اصابت قرار گرفتن یک نقطه از شهر شیراز در جریان  حمله هوایی دشمن حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68641" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68639">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwjV7wciqsavjsuqUvoFkSZb1N9igDCTGJ4CIwIDOsFIuQA4Hu_wp4jYO43bjzjx2WMyDRhwW8A8NH8giCHlBU5B1YitgsLDQNbsiK0v75MZc15zPIMu16nURndeODUe49hIvX43Hu3WihwKRWsWOnZgzrf2Zevd8TbMLJmW8z_MM6rCZHBgQ2NRcCdo5RuyM0PKjsyv5FIuVqPWgzD0wU5_vCfJpBpcz4eMuV8Yg6VIfFEk4S9umqRVbyGhbbrIdWxBgkw0MTWqYQjvTKomDYoZiAOerdu1wvFSIVZxjHFBF_MFHtkUCdG8f0yVgBo80deGGWpVofrwLoz17-zBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CyqCM2ZNJNanebq2ck9EtZsArUQJMEWZeFswWV48RO5tmtmwup2Ykl9nVzUjQLRNkHvnl83dvJn9QNR1MrvTl59xlZdGZx9QTlvT7UK3jVDLYYMI9VJirZOjLi72e4nLXCbW7xiMv2w7dYMuxWYYYTcsmZnp4hfS-htcFmjw7-JjFJIHjWozRpX4zRiHlVnlgJmbUX2D4XPMIJhUmHMowVqfUHbo7GQ4wZtwgbJ_mvomYOV4YZV8misoTTlHNvVzGknf0_XoMqA6_BNAJiKgxMmIZEGnST3_NaKtQAM7WYxkPM11yYmpfla4hX-fVDsPHk3fjpwirvICX3z4hmQp8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68639" target="_blank">📅 17:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68638">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⏸
حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها (1944)‎
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68638" target="_blank">📅 17:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68637">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrsHn0homq-on8pOK2GNaa2l6CQicMwkrK-__hk9MIVGjBgEDekesIecw-5qJ3AhvOnjW7dBfZ98j7dve4-Dcrn_B9XDU6kTeWf_x6HxdZrpcNQQzLgKPuVSpR6-FF0miCXoPwLlNOO8VjRKWCg-v-i7lnbJ3yrsSBQQLN9GSjzvSQl3_RyBXlJIcoHQAPv-Sb6gn_inAOs-b_jFSIz25cdFZ0ckXTmiyKEUEriyOka7b6rRzmbkd1UuSDhgxYiNgzvF3unxhP3ZMpo8aXQ2gKIWjngZDoznqLhBhEtA6aAurqhBImFgmJ-ZaLTmXPQsFXrU_kvAFAyueRY9z5L1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:با تداوم درگیری‌ها در ایران، قیمت بنزین بار دیگر از ۴ دلار در هر گالن فراتر رفت.
با ازسرگیری درگیری‌ها میان ایران و ایالات متحده و اقدام واشنگتن در برقراری مجدد محاصره دریایی که می‌تواند تنش‌ها را به‌شدت تشدید کند، تردد نفت‌کش‌ها در تنگه هرمز بار دیگر مختل شده است.
رانندگان ممکن است دوباره همان شوکِ ناشی از قیمت بالای سوخت را تجربه کنند، چرا که میانگین کشوری قیمت بنزین امروز بار دیگر از مرز ۴ دلار در هر گالن گذشت و به نظر می‌رسد رئیس‌جمهور ترامپ آماده تشدید تنش‌ها با ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68637" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68636">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⏸
🏆
👍
ویدیوی کامل مراسم اختتامیه جام‌جهانی ۲۰۲۶.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68636" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68635">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
حوثی‌های یمن با صدور بیانیه‌ای، از اعمال محاصره دریایی علیه عربستان سعودی خبر دادند.
حوثی ها با صدور بیانیه‌ای رسمی، محاصره کامل دریایی علیه عربستان سعودی را بر اساس معادله «محاصره در برابر محاصره» اعلام کردند و تأکید کردند که این تصمیم از لحظه انتشار بیانیه لازمالاجرا خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68635" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68634">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odrSblDwg2hlylk7KZBnLTQUJCnxkvwL6s6swvO7INhyXJgfzEfjWJy-2C3EQMYPPP7bGvdV6l30BwHeHHDO_1wP12L1rChtK-n7cKdIR9W1TomGFJOz9_7mhj5UhwCjd3CHTzp8zwrGsBQakgrUBOXK3hwmnbUhemLVfsvmfFObkhAF5Bddu1t6vFU1FBQVBNcPgF6UviPhQ4JFDfEPBBtNvhMRiKgGWBDCGeyJstocHAylvV3Zbq9xLvfYXfGSs-WxNHMuMvRGNHmBY8QMSzSbpZAnva7xC-GlWdKPNx3WD5vlAkcj1tjIzKGcnsiobfBnJZBbDgwUK8NVCZJ5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز:
میانجی‌ها به ایران و آمریکا پیشنهادِ یه آتش‌بس 10 روزه واسه احیای توافقی که امضا شده بود، دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68634" target="_blank">📅 15:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68633">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfNCKor4hoOXMiJRfNJ79ZPaJOe3QqP3q87pFXX4Rxb6LjruDTgIxT63XRP6Ln0gkXsNNhkyieVK0bR1IHegQ8KmPKxG099VSltHb2tC3lbWAY3rkcxJGHouxXiWOPLvKJ_RhGBDtbh6yidvAtiytzsMqEvrrHl0Uurdw_TeeVjV_Nmfi8ezN5L3Tpnrq3KbKoYWOCvdJgvieo0GY86UPO_5UjeyE-RSMLAtRyakj_iXCJT5rm11DzaY3AhxiQj-6omGPqReO6KmIZMpeQKYHSkL5HTfWA4Dx1x8O_KS7G2AQXOSchNA9HSKf6bOZ-KKLVLqWIIhT360lohnFpUjaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68633" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68632">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=YqjOxSlB0LgIHUd-_it8BVmN-H-QXXrFR4bbvFHzcbiBzcIRHS5Q5JPv4rYVQZvtqU6JWTuASgjeWV4VqzEDMEytLFu5qEj7YTcSrU-AB3VJ59R9amuVTz7mXp5KSJkDvtmZi2sTqrDEapUPRed7sKl2B7IrGjNx6cROstH9nZwxU-K5Uthke53avYwIhdWEsUGvlsrrsTajbm7N3hqG2VLEIXcYd60vNFTt_wWRqoEy_ps62WMtV7BqiMP3o_v_rloHKXj7162DCMT-piluyeCLdo9dXrODDwKZ9axo1nAG0xvE7f6Z7OiEwTic4guLylmpNqDiObPOkWgzVeKf44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=YqjOxSlB0LgIHUd-_it8BVmN-H-QXXrFR4bbvFHzcbiBzcIRHS5Q5JPv4rYVQZvtqU6JWTuASgjeWV4VqzEDMEytLFu5qEj7YTcSrU-AB3VJ59R9amuVTz7mXp5KSJkDvtmZi2sTqrDEapUPRed7sKl2B7IrGjNx6cROstH9nZwxU-K5Uthke53avYwIhdWEsUGvlsrrsTajbm7N3hqG2VLEIXcYd60vNFTt_wWRqoEy_ps62WMtV7BqiMP3o_v_rloHKXj7162DCMT-piluyeCLdo9dXrODDwKZ9axo1nAG0xvE7f6Z7OiEwTic4guLylmpNqDiObPOkWgzVeKf44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل:قلعه نویی موقع جنگ رفته بود بیرون از کشور تو امارات و ویلای خودش تو آلانیا ترکیه بعد اومده به ما میگه شما تو غار بودید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68632" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68631">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68631" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68630">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4sHB6l0OQlHCHHVPuellDxZSsNBwPh_yZJ0mk_OCGFYmXHVz5LhKF337Ljm5t5MUvQRj1INaXbQrB09g4vXgXBk3LAElU7NhdTAFlGZPOw27kqXc73ZseJA_gIePX9iCoJRLyHdt6RYn7xRFRRGzwO0B5PrlAtN2NMJxKgNSggacaGChpxGAciNa8h7b4mU-G7eRE7vWuByLLXAqonGrtTSI2jr3clxa99YLGCMGfDTNH7VH32qFW403a06bAQzKpgc11T9iOJ2qRhoTHbBJnRZ6Iwt-8bdaCn1-Ks9yoJkLmK4SP-8_JDwXKAhF41bbXpPag3olTqydwiAXPFWwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68630" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68629">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlHJwO7HZpWO04trd743Lu90F1sPeo_2pKTmEhbsaxMnb1TvL3caDirxDEjqkogOxiwm6m_eW91Cz7ChJ8PpiZPsHUsdXmE2pHBCwuDFpdWDo0Wv0crIMRd9cKLWubK_0S_KknRlKSVNyFOusPxrjhyFB8hDAEegJLyIKjQre9id3ikidi_L9fAK4L_kjdFjt0h_7KOiS776uoZe8Bo0j8tQgA9E36M5QjSv22js68oJBvBWmqIN2Za3ZvMnvnSxl6olBf7evsVxR5ucFgyyiicFJK5f5L4jnDk8f6XKusICjfylZ1pbdaPkY17nnOzTcrj17Qv04myrLvVEee0pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عبدالله شهبازی :
شطرنج پیچیده این جنگ داره به آخرای خودش میرسه.
به نظر میاد جمهوری اسلامی توی این بازی مثل یه بازیکن مبتدی عمل کرد و ترامپ هم در حد مگنوس کارلسن ظاهر شد.
ترامپ طوری بازی کرد که انگار حسابی گیر افتاده و به توافق نیاز داره. امتیازهای بزرگی داد و با طعنه و کنایه، رسانه‌ها و فضای مجازی رو هم با خودش همراه کرد.
این نقش رو اون‌قدر حرفه‌ای بازی کرد که جمهوری اسلامی باورش کرد، فرصت‌های طلایی رو از دست داد و دنبال امتیازهای بیشتری رفت. در نهایت هم نتونست یه «استراتژی خروج» انتخاب کنه و مسیرش رو متناسب با شرایط تغییر بده.
حالا نشونه‌هایی از اجرای یه طرح غیرمنتظره دیده می‌شه؛ طرحی که اگه عملی بشه، ارتباط مناطق جنوبی از هرمزگان تا بوشهر و شاید خوزستان با مرکز کشور قطع می‌شه و عملاً حاکمیت جمهوری اسلامی بر جنوب ایران از بین میره. به نظر نمی‌رسه اجرای این طرح نیاز به ورود گسترده نیروی زمینی آمریکا داشته باشه.
⏺
اگه این سناریو موفق بشه، می‌تونه شروع فروپاشی حاکمیت جمهوری اسلامی در سراسر ایران، طی چند ماه آینده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68629" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68628">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=ALVf9RpUZXaBW352d3YTlCLgztaj5aNc6_b31LYORqVlJM1wK0ePQtlfOpEOx_5Xc3CUtgA9mmCLvs-kngsM78s7snwnObvXFoNewykcr4feqxoSPhXts2hv8PVr9-ae_sYpMhrmnc2IBiMZJIAW6eQdjoG1pNTvdFXFRxarwzeeR6fKNKxII0MDgrNWPxO7pFT3OQMI0JtV1wujm-CtGjDM18WhqXrWlQMMaj-xEVo9ifba0aG0zhMQMyvKkL_54RVZrOaAxNvKdWTGd96wL0ehZadc_wvdWI9LK49qeN7ZQLsky-eWfDPoW1XzAUl6dW3sow4JKxAkv1iZyGeD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=ALVf9RpUZXaBW352d3YTlCLgztaj5aNc6_b31LYORqVlJM1wK0ePQtlfOpEOx_5Xc3CUtgA9mmCLvs-kngsM78s7snwnObvXFoNewykcr4feqxoSPhXts2hv8PVr9-ae_sYpMhrmnc2IBiMZJIAW6eQdjoG1pNTvdFXFRxarwzeeR6fKNKxII0MDgrNWPxO7pFT3OQMI0JtV1wujm-CtGjDM18WhqXrWlQMMaj-xEVo9ifba0aG0zhMQMyvKkL_54RVZrOaAxNvKdWTGd96wL0ehZadc_wvdWI9LK49qeN7ZQLsky-eWfDPoW1XzAUl6dW3sow4JKxAkv1iZyGeD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
«اگه اون دسته از آدم‌هایی که واقعاً می‌خوان برای ایران یه کار مثبتی انجام بدن، قدرت رو به دست بگیرن یا مسئولیت مذاکرات رو بر عهده بگیرن، اتفاق خیلی مثبتی خواهد بود.اما امشب هنوز تو اون نقطه نیستیم.
به نظرم دنیا داره به جایی می‌رسه که مشخص شده حداقل یه عده توی ایران می‌خوان تنگه هرمز رو در اختیار بگیرن و ازش به‌عنوان اهرم فشار علیه دنیا استفاده کنن.
دنیا باید تصمیم بگیره که آیا می‌خواد اجازه بده یه آبراه بین‌المللی دست کشوری مثل ایران باشه یا نه. این کار کاملاً غیرقانونیه و اصلاً قابل قبول نیست.
آمریکا هر کاری لازم باشه برای حفاظت از کشتیرانی جهانی انجام میده، اما وقتشه کشورهای دیگه هم سهم خودشون رو ادا کنن؛ چه با تجهیزات نظامی، چه با حمایت مالی، تا این بار فقط روی دوش آمریکا نباشه.
حافظت از کل دنیا برای همیشه، وظیفه آمریکا نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68628" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68627">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=AxeVaHmUbPbmjjhHLpfs8GDVk57GADDJ5XJWNpFuSM50z5Xog978BZqbFO37MXOCHaM5HkREnKfsCtQhARyrPUDKxwvy8PEovVM1GJYWpl-uKwL7zQG65ULNLKGSVkrJKH-3-C4VQMoyFpKLuuf1UsW8iAreEA9pTbDihRg6Q1Mfkh1WXX3wQf_EVHSM5fZ8x5TGoHvJaTj24eCzcrp4CSI68GEKh2JzEPvof2DNYaTlDWGSbEVZebifQ3ArYHQ15Ut1eizECTFEcwxRwP3O3cvkKsuo5KIhOdyUAQPdtAp9Nd4Fn02q18bGi_2KqPYBL2a4KkawvzR7us4io5QQoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=AxeVaHmUbPbmjjhHLpfs8GDVk57GADDJ5XJWNpFuSM50z5Xog978BZqbFO37MXOCHaM5HkREnKfsCtQhARyrPUDKxwvy8PEovVM1GJYWpl-uKwL7zQG65ULNLKGSVkrJKH-3-C4VQMoyFpKLuuf1UsW8iAreEA9pTbDihRg6Q1Mfkh1WXX3wQf_EVHSM5fZ8x5TGoHvJaTj24eCzcrp4CSI68GEKh2JzEPvof2DNYaTlDWGSbEVZebifQ3ArYHQ15Ut1eizECTFEcwxRwP3O3cvkKsuo5KIhOdyUAQPdtAp9Nd4Fn02q18bGi_2KqPYBL2a4KkawvzR7us4io5QQoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
ایران کشوری ثروتمند است. یکی از دلایل وضعیت نابسامان ایران این است که این رژیم هر پولی که به دست می‌آورد — چه از طریق لغو تحریم‌ها و چه از راه فروش نفت — صرف سرمایه‌گذاری در حزب‌الله می‌کند؛ آن‌ها در حماس سرمایه‌گذاری می‌کنند...
آن‌ها باید میلیاردها دلار را صرف سازندگی کشورشان کنند، اما در عوض، این پول را برای حمایت از تروریسم به کار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68627" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68626">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=dv8VUBZgfB5DTafOoH_TBLL4JHi_kMGoaJeBQqBnrR-tUhKhgvSkeqnoDZgLuTIr2OrGHTTlSqgqQJbKVmGpK_WCzas0RDq0wiDRS3heSam_YxqAXcGB-Ld2fgYfCeaxSfAIMNX0z4Cc31uymn5Pf9QFsts0qxULf_tehB5ucF-BLI9fQ1GhgzHh0cjK9JbC1eTwVEf7Ggvdxluc25549J06Czcz8ltlFRjl_3T4xXar2eRNi6_UIGAZtQbcgVY0DqlwDcV__cJeEriM1awr6000VZ9ctKoQaGtCKfwYhXIgCwCnZxKKdQDq7LdjYvkpbnz4wW2Ztdqds3I2N_IXxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=dv8VUBZgfB5DTafOoH_TBLL4JHi_kMGoaJeBQqBnrR-tUhKhgvSkeqnoDZgLuTIr2OrGHTTlSqgqQJbKVmGpK_WCzas0RDq0wiDRS3heSam_YxqAXcGB-Ld2fgYfCeaxSfAIMNX0z4Cc31uymn5Pf9QFsts0qxULf_tehB5ucF-BLI9fQ1GhgzHh0cjK9JbC1eTwVEf7Ggvdxluc25549J06Czcz8ltlFRjl_3T4xXar2eRNi6_UIGAZtQbcgVY0DqlwDcV__cJeEriM1awr6000VZ9ctKoQaGtCKfwYhXIgCwCnZxKKdQDq7LdjYvkpbnz4wW2Ztdqds3I2N_IXxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا احتمال تجزیه ایران وجود داره؟
⏺
مطهرنیا:
امکانش هست ولی احتمالش کمه.
همیشه این امکان واسه کشوری مثل ایران وجود داره ولی تجزیه ایران نه به نفع امریکاست نه اسرائیل.
اونا خودشونم خوب میدونن تجزیه ایران بیشتر به نفع روسیه و چینه.
پس امکانش خیلی کمه بخوان بفکر تجزیه ایران باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68626" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68625">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc5v3_TuFYLRgWXclmQw-BkwGiZTpke5OOYr28fv5GWUMi-wHg8UFr6kADMJIil5NYvkbeqTA3kiVtZXcW2MBK85Dd94eNrR7ZW6VMHPoyF4r06Xg6Sj3ByhVORRJiLCwtTcMnQMKziE9lhSfMQ1Qv8LcbH7t8q20MD2N5LTE5hDktuXZRx_mfdGvgyFJgCCcMIU82lQCN-NZMFTxj7rQn18yHZYPm8iK2S6WzwvpLNQSUDfV6L4MHtprWqMQNJfnIgkwmG-Zs-TMafc8rH2Juxbdf3GV7uNN-suBcpEJENKCTD21aPq8NwF1005SVCNTsk-VOTQKxkUStKpceCBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود قهرمانی تیم اسپانیا در جام جهانی رو به دولت و ملت اسپانیا تبریک گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68625" target="_blank">📅 12:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68624">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=Sr8dgG8y6Sk07hJ_RkqrU3sdyOiYivduR9M6Tw5b8E_uYSBDQNGP325g7Bs-U6Nhk4vh12N73_96H7RPcEHYbFPaqR_5BoP2EFJl3btt_eZrBNpmsQX_4YO1Zp75isb4ONl3Dshhl2CerAZ_DkAynSr_2kqMv5ILbi_tTrg5_pc3CgQkshaSqYvhqfv6QKmar7d1FNAsQo2nGSrbsG-OEqs6ivQIWpzSp6gCKaomV6v8IWw8Hb46R55dwqAG-3al8CmHVS5dvw8n94ZkJFowaXSD5yxL4CKit9xBaWicVfj5hY7e-sgK3MiMkOs1xsZ_R_h7eXhSTy13xXR7K_MbkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=Sr8dgG8y6Sk07hJ_RkqrU3sdyOiYivduR9M6Tw5b8E_uYSBDQNGP325g7Bs-U6Nhk4vh12N73_96H7RPcEHYbFPaqR_5BoP2EFJl3btt_eZrBNpmsQX_4YO1Zp75isb4ONl3Dshhl2CerAZ_DkAynSr_2kqMv5ILbi_tTrg5_pc3CgQkshaSqYvhqfv6QKmar7d1FNAsQo2nGSrbsG-OEqs6ivQIWpzSp6gCKaomV6v8IWw8Hb46R55dwqAG-3al8CmHVS5dvw8n94ZkJFowaXSD5yxL4CKit9xBaWicVfj5hY7e-sgK3MiMkOs1xsZ_R_h7eXhSTy13xXR7K_MbkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام ویدیو ای از حملات آمریکا به ایران منتشر کرد.
تصاویری از برخاستن یک جنگنده F/A-18F سوپر هورنت نیروی دریایی ایالات متحده — مجهز به بمب‌های گلایدکننده AGM-154 JSOW — از ناو هواپیمابر کلاس نیمیتز، و همچنین شلیک موشک‌های کروز BGM-109 تاماهاوک از ناوشکن‌های موشک‌انداز کلاس آرلی برک، در این مجموعه گنجانده شده است.
اهداف ثبت‌شده شامل یک سامانه پرتابگر متحرک (TEL) و یک پرتابگر پهپاد است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68624" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68623">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60340234e2.mp4?token=ojdtYteiV8PNEyIaSk-FVq5pOsFeBsy8JLjtiNvb8WepxOGEDSbKtkuLHaR87BobwSGigp1Sa-G0wfj9K1ul9gjhxR71lD93w9YPYhez6n7hTCwsdseE8GEmXWjBPwX7Usu4nfaHaPWjWhl6fhLKKVi8eYeuAe-WUeDUA12vMNiSipVREM16FNoBHexvPstFYgjWmcDNokZghZ0hMWycli8fr5H-cNss-P9caDgBDK0gCBUZ_2uNkPDtCbQewJO1nDXZAx2_INNWrsAQSHo9UQiE1JsV3IQDMpT0dUft8oSxZYpcw2EyNkkfGqFfUuImX4QNHYgkaDpo47GX1D1W_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60340234e2.mp4?token=ojdtYteiV8PNEyIaSk-FVq5pOsFeBsy8JLjtiNvb8WepxOGEDSbKtkuLHaR87BobwSGigp1Sa-G0wfj9K1ul9gjhxR71lD93w9YPYhez6n7hTCwsdseE8GEmXWjBPwX7Usu4nfaHaPWjWhl6fhLKKVi8eYeuAe-WUeDUA12vMNiSipVREM16FNoBHexvPstFYgjWmcDNokZghZ0hMWycli8fr5H-cNss-P9caDgBDK0gCBUZ_2uNkPDtCbQewJO1nDXZAx2_INNWrsAQSHo9UQiE1JsV3IQDMpT0dUft8oSxZYpcw2EyNkkfGqFfUuImX4QNHYgkaDpo47GX1D1W_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در مورد ایران:
این کار بسیار بزرگتری است که ما انجام می‌دهیم. ما کار کوچکی برای جلوگیری از داشتن یک قابلیت خاص توسط آنها انجام می‌دادیم.
حالا ما فقط به آن پایان می‌دهیم. بنابراین واقعاً همان کار نیست. کاری که ما اکنون انجام می‌دهیم این است که هرگونه شانسی را که آنها بتوانند موشک هسته‌ای داشته باشند، از بین می‌بریم.
اگر به آن نگاه کنید، پس از یک هفته و نیم یا دو هفته [از شروع جنگ]، ما آنها را از [توسعه احتمالی] آن متوقف کردیم. اما من نمی‌خواهم از کلمه احتمالاً استفاده کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68623" target="_blank">📅 11:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68622">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ku4k9WAk_maObrbt1FdamwHt7MUT58LMkYXU0So2n2loHMBK9KAdKLuz9osRC4mmk81kxAj2XIIExKzDxiK8f2j3XUo9ra3yxxF4zrZV5Yo4N-gLA8dOw_QFR25zmhWhTD8_Tba_b9RsjQ35zeVl82S4KAB9Xp2jm8WeukoF33PxLGEKfHyGANDCp1h78sT8uQ0PqPtiopeNPKDVQZKtF4zxBymeGAS4gjUUfQdZCQrpFY1kUmXUqCQe_5_wKRl4YZ3S_xFXOZhhFgzfl1L6KDC8LWwySXnR-_9SQ70nS0sB9l-Q9Z7LvLqDOdmxnMLCL5tNtu8L6qe7jBC3Iv2pvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📢
نیویورک تایمز:با نزدیک‌تر شدن دو طرف به یک جنگ گسترده‌تر، یک نیروی نظامی دیگر آمریکایی جان باخت.
پنتاگون روز یکشنبه اعلام کرد که سومین عضو ارتش آمریکا در جریان یک آخرهفته از حملات متقابل کشته شده است؛ در حالی که جنگ با ایران شدت گرفته و ایالات متحده شروع به اعزام هواپیماهای جنگی بیشتری به منطقه کرده است.
این سرباز در شمال عراق هنگام عملیات برای از بین بردن یک پهپاد تهاجمی ایرانی که سرنگون شده بود، کشته شد. این حادثه در میان زنجیره‌ای از حملات فزاینده رخ داد که تقریباً آتش‌بس حاصل‌شده در ماه گذشته را از بین برده است.
هیچ نشانه‌ای از دیپلماسی یا مذاکره میان دو طرف دیده نمی‌شد و مقام‌های آمریکایی که به شرط ناشناس ماندن صحبت کردند، گفتند که ایالات متحده در حال اعزام هواپیماهای جنگی بیشتر به خاورمیانه است؛ اقدامی که برنامه‌ریزی آن حتی پیش از کشته‌شدن‌های اخیر آغاز شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68622" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68621">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=ej8nDVK6GjsRLVqTa12r-TUfi-tpcTSIwRwgOyXSzgjG65XLDdNoQZC_na2kmc4BqcPD2qCMfHQXZ0EDsebos_03lVOKvuOFio8hYZryrpmzwAg9XfVexnGhFKUPcbGz3ksbfwmFsmHAAO-yhLP9XSyYNSEMyXXAmTirB1YQh0TUl_PcvVd-zZFMkJUIiYrd_zR1UbIeUppPaQocAbBnv4OHuAEfpUnNe_YcGLjz0ORYKV73fcDFCKEjWWiNBB9mfdd8lSq546hhdmSA5ZxgV_5n8lgbLSvAjxSYPA_EsLjqYF2zSr7NCdThT-g4TCTm4RRODqYnL4r3w0VdGyzM5rLcS3IywVSgf3sngjZSnaXihQ6d9-c7Bnl1sM25yBJHVIlv-nytILEzjZq3wZFBBIHPJO7e2mfYaKI7M2KOu198cm3YE33CBpFEOPIfl6iFw2ec1oQ-_Rqbg9g3tk35GEbBQczGPBcRjkxGrVUmIFZ4ro1yb3s_UnQRe2L8Pa78GBJ1JqhBM33gfR-6xuxrA1e9IyUbcf20YekfqgBZT_H-25gtQEvosPG8kh38Kt3M2LGGphSlZfmD9YdsJQRyoBvErOMZhiqUMsh_aeZg3DfcaU6pkeHvURnEpHR3w40jm2xiEm_cClyzoPWE3f4oIo5FhuYizvN_q_dVGw_Zsxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=ej8nDVK6GjsRLVqTa12r-TUfi-tpcTSIwRwgOyXSzgjG65XLDdNoQZC_na2kmc4BqcPD2qCMfHQXZ0EDsebos_03lVOKvuOFio8hYZryrpmzwAg9XfVexnGhFKUPcbGz3ksbfwmFsmHAAO-yhLP9XSyYNSEMyXXAmTirB1YQh0TUl_PcvVd-zZFMkJUIiYrd_zR1UbIeUppPaQocAbBnv4OHuAEfpUnNe_YcGLjz0ORYKV73fcDFCKEjWWiNBB9mfdd8lSq546hhdmSA5ZxgV_5n8lgbLSvAjxSYPA_EsLjqYF2zSr7NCdThT-g4TCTm4RRODqYnL4r3w0VdGyzM5rLcS3IywVSgf3sngjZSnaXihQ6d9-c7Bnl1sM25yBJHVIlv-nytILEzjZq3wZFBBIHPJO7e2mfYaKI7M2KOu198cm3YE33CBpFEOPIfl6iFw2ec1oQ-_Rqbg9g3tk35GEbBQczGPBcRjkxGrVUmIFZ4ro1yb3s_UnQRe2L8Pa78GBJ1JqhBM33gfR-6xuxrA1e9IyUbcf20YekfqgBZT_H-25gtQEvosPG8kh38Kt3M2LGGphSlZfmD9YdsJQRyoBvErOMZhiqUMsh_aeZg3DfcaU6pkeHvURnEpHR3w40jm2xiEm_cClyzoPWE3f4oIo5FhuYizvN_q_dVGw_Zsxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«سرباز روح‌الله رضوی» مجری یکی از برنامه‌های شبکه خبر، اهل کشمیر هندوستانه
🇮🇳
و پدرش به خاطر علاقه‌ای که به روح‌الله خمینی داشته، اسمش رو گذاشته روح‌الله؛
⏺
حالا این ویدیو از این مجری حسابی وایرال شده:
🎙
روح‌الله رضوی:
با سنگ، تیرکمون، کوکتل مولوتوف و هرچی که میتونستیم، رفتیم واسه تعطیل کردن سفارت انگلیس...
🎙
دهباشی، مستند ساز:
به این حرکتتون میگن هرج و مرج طلبی، یه رفتاری انجام میدی که هزینش رو یه ملت باید بپردازه.
تو به عنوان یه مسلمون که به حق‌الناس اعتقاد داری، بنظرت میتونی کاری بکنی که هزینش رو میلیون‌ها نفر دیگه بدن؟
🎙
روح‌الله رضوی :
اسمش رو هرچی میخواید بذارید. وقتی همه‌ی مردم بخوان یه کار بد انجام بدن، شما سکوت میکنی؟ من اینجور مواقع نمی‌کشم کنار...
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68621" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68620">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⏸
ویدیو کامل مصاحبه جواد موگویی با عباس عراقچی درباره حوادث یک‌سال اخیر از مذاکرات تا اعتراضات دی‌ماه و جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68620" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68619">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWI5oun2KYi5o9Ah3p4vJneepKsOCXCxvEEWfjeGNQqPENISBNSmb1nhK6F93QspsnUXvpWIeAVSz1oUCB40pF9q5_nbRmJXZAoqkU-AZ63j7lpv0goBwyGQ69JT9G-RXzJ_oa2x7Ax9WWpXT_aqVZpLgSsvjPDGQAAxQ2BfKKgchmpZVotUwE8UrAR9WJtrL4I3t0aHk31Mei35NAhgpLZNEAbZ-1-khXpyqZRmBOJpIsjOYBU7M6eSkxceXG0QB4bCW5FDlaB_PClvbC3LTR4ooXJbgEKuyBKS5WY9iP0PCtxM3J4LsbcOq94y3pXgwReLYVly7zDtO1f9YciJAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68619" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68618">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-KNyZNtPEq5gJ9AMyaf73E8DtSARgfjFCN6i79cxHdNLhhK7HXQcCVyrxxP4iXHcFtoCxOLxRCLSjYrIxV947f1sPof9VPi3B1jDeACd3rMui7u5MDsA4rN29qgct5Izb6R-IO96Y0ZQ9VKReAxy7v9Ip2keT8YDx9mXnx0tK2wSIQsg-PtlV1P0rjxTKx1GerO6-mj70npGH-7jIX6w3mj9TZoNOA1rRXfgzObxB8y3ISrX6Xs_iI-XApL8PcIff1GwufJcsZ3NXenSevdYc2iRVxHioxed5pkOGzeKuPp-wIkniMexhQx-y0e9gL7dIxiwAfIU66rKK4J3CEUVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در نزدیکی سواحل عمان مورد اصابت قرار گرفت و دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68618" target="_blank">📅 03:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68617">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68617" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68616">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
انفجار در خورموج استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68616" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68615">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=NXU-ZRvJW7-rIS1hfL_tRXu7AWibMDcaQylqJ2VmQzcGj9IFtldtaICPBJfDSf7ijQd0KcqKwsWjqQK16qh0dMeVoIwzPmxQQEvXwNxIfm7JI6Q_PqZpW_gAEjQKJ_CPYk0d3RC_BKwT2gCrNd5-tnWqiKMcAOmHebzWbDVY_2n6_wQQseXAd5I0bcwx2FCbSHND42YUYkUXRduvvN2s1bKUqhve6sYWQGRuedz63kAWH87WjIy1ImoEgZAV9aJGb23k_X3RlCLeEORcR0UXqu_RKWSNMwvynEcnet2RgEg3kaL4ZNB35tqfYc-VM2G0WM5-mk1LZvstc2hkXlDLLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=NXU-ZRvJW7-rIS1hfL_tRXu7AWibMDcaQylqJ2VmQzcGj9IFtldtaICPBJfDSf7ijQd0KcqKwsWjqQK16qh0dMeVoIwzPmxQQEvXwNxIfm7JI6Q_PqZpW_gAEjQKJ_CPYk0d3RC_BKwT2gCrNd5-tnWqiKMcAOmHebzWbDVY_2n6_wQQseXAd5I0bcwx2FCbSHND42YUYkUXRduvvN2s1bKUqhve6sYWQGRuedz63kAWH87WjIy1ImoEgZAV9aJGb23k_X3RlCLeEORcR0UXqu_RKWSNMwvynEcnet2RgEg3kaL4ZNB35tqfYc-VM2G0WM5-mk1LZvstc2hkXlDLLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پایگاه امام علی در چابهار مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68615" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68614">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVg7w0yzKT3e8dlf2qo3KEKlCwwbrjxNXbQ7lyY6Dv2THDinzOXSL_e4gV6heRcewkjtGf6I79QAHWFL34xwKSECToEFR4n3qQ41wdHJHnZHuUMdQnBw1VJZjP6ZoIlTw6YyTMW8pGgeDyJd3aJ84g5DTjhij260ryjgOsXTzE_rysuHgGGH8crXXT5dRhL6D9j0SH16X9mOt0sh-dgvoSImbUrSlwXLqyJhW_6lA247wPDzYluaR9Ue0YuvoKvBhfHYC99aAdXO5-XtrOkR7zUZ-JSJx-zm57ozP6lTmO_ZgPkTtWsny9Mg0PrC9ySP17D6o272z_I2sESFZUzgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68614" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68613">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
منابع حکومتی:
انفجارهای شدیدی در شهر رأس الخیمه، امارات متحده عربی، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68613" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521034efe8.mp4?token=qjerWEPBtecLZcYZYm98TXBoPiBQqVRQrKeWAheVyOeufHgGQtCf1Bd9tN4AQFRjNamz6PraKgVTeirHwj5q1ZNN3SbgcoKjBB6p3YlEIQMvqRmUJYSs9YlC8r-pQAY9zVLZsB4Gbw2vkDO03eZmSkLowr-QzD_KB9cOw2czXo9cf7S8YAiQ7mtXBIMCbfq4dzURuj9-qwDVEH2YBQOkX9Yw-YiXFMIT3BzGlzvwfStR4xNu5isyNIqk4E6r5z0MEK27Ir2kNfTp3knbj3chIw3dQvA9YFjPHYcCd9TKlLhEAlfn2CL-qDEdUHbsVzM-VhSSngPeT0ve_Tksunltkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521034efe8.mp4?token=qjerWEPBtecLZcYZYm98TXBoPiBQqVRQrKeWAheVyOeufHgGQtCf1Bd9tN4AQFRjNamz6PraKgVTeirHwj5q1ZNN3SbgcoKjBB6p3YlEIQMvqRmUJYSs9YlC8r-pQAY9zVLZsB4Gbw2vkDO03eZmSkLowr-QzD_KB9cOw2czXo9cf7S8YAiQ7mtXBIMCbfq4dzURuj9-qwDVEH2YBQOkX9Yw-YiXFMIT3BzGlzvwfStR4xNu5isyNIqk4E6r5z0MEK27Ir2kNfTp3knbj3chIw3dQvA9YFjPHYcCd9TKlLhEAlfn2CL-qDEdUHbsVzM-VhSSngPeT0ve_Tksunltkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت سربندر ، ماهشهر استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68611" target="_blank">📅 03:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f087874ede.mp4?token=L8mkXbHbiby4gDodFvKoXjAfAZmN82Eel9PC3s2ATya2_pSITmgDIqL8CqnIYNwjUvf1eh_2JjXRMu9RyNMDdn_WiXN4E1fqdx-K3N7sRZ9QxCsgqzidxorS3lwgx5BvMMvR5njAXXeIZtCiZ2XI_0hrkJsGKBMPkiNBrxT7ztgSq-2lhkc3sI7apG-9R_YfenoQtxDxHE_SwA4MeQ8h2XEQO52q6E7c4SvU9FphAaEQuM6dqcuWiK1EdVyw4X7eK8Vd_7coJJkJlsxR1vehwrp7FaVljzN1U-qBoralQ2XMp1aA0Tw8jyPczOC_ULejKgHrBJcl8NMRa-XhZJvgwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f087874ede.mp4?token=L8mkXbHbiby4gDodFvKoXjAfAZmN82Eel9PC3s2ATya2_pSITmgDIqL8CqnIYNwjUvf1eh_2JjXRMu9RyNMDdn_WiXN4E1fqdx-K3N7sRZ9QxCsgqzidxorS3lwgx5BvMMvR5njAXXeIZtCiZ2XI_0hrkJsGKBMPkiNBrxT7ztgSq-2lhkc3sI7apG-9R_YfenoQtxDxHE_SwA4MeQ8h2XEQO52q6E7c4SvU9FphAaEQuM6dqcuWiK1EdVyw4X7eK8Vd_7coJJkJlsxR1vehwrp7FaVljzN1U-qBoralQ2XMp1aA0Tw8jyPczOC_ULejKgHrBJcl8NMRa-XhZJvgwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68610" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
تسنیم:
دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی (ره) شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68609" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در بندرامام و ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68608" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68607">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68607" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68606">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله موشکی آمریکا از مبدا کویت
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68606" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
خبرگزاری مهر:
یه پهباد رو زدیم سرنگون کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68605" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68604" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=NbWQ3lvZoQWLvlHTPl5gKkPHtVF_akOjP7-XvzE7RTJDT8o6RFj-Be5hQjFgyXNOa76REZtpQ513ehHgUXeIJ16jdbeVEa0J-oev2juGiaaVYxeKtsYid7dlKCEOmiKwSL5pyKCf5OrVMjvfPWi5e4v7jPI5Cu_-fOduwvh-E1RzlowX1ozzj6vzdumG5rG4trG6-g8fTXOy215dABTo6aImpHA9IVSyfAtk_WRc2vrB8GHldGR1M6tIp2BaB6vUPPpvLlkE2PnGAydsjTDMTAtkZ7b2rLF4e4X1uvQ1BSUtaRhVzEhEWnZvK0znNB2JXpKaoo2IiniSb1UzcU3LtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=NbWQ3lvZoQWLvlHTPl5gKkPHtVF_akOjP7-XvzE7RTJDT8o6RFj-Be5hQjFgyXNOa76REZtpQ513ehHgUXeIJ16jdbeVEa0J-oev2juGiaaVYxeKtsYid7dlKCEOmiKwSL5pyKCf5OrVMjvfPWi5e4v7jPI5Cu_-fOduwvh-E1RzlowX1ozzj6vzdumG5rG4trG6-g8fTXOy215dABTo6aImpHA9IVSyfAtk_WRc2vrB8GHldGR1M6tIp2BaB6vUPPpvLlkE2PnGAydsjTDMTAtkZ7b2rLF4e4X1uvQ1BSUtaRhVzEhEWnZvK0znNB2JXpKaoo2IiniSb1UzcU3LtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا از کویت به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68603" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIOrmXanuQ7Z8jbUbtQYPsLSdc7uaBqp37M_SwJeG50ZnuYjsom9vmh6hiNlLF5YAzroCv9xpOSFJK86V5hTWeSW16Pt61o8J6bhOD0pphYHYUTkuh48I_rY5j2_2Lpn-5WZLPXXXgOElbkpfcZl78OIMfZ1q6yl6qpsjCAV8QY-PzuBSeGcMEIN7VVeM1bsyrVTS3P8CIMdK-cPtYSc-fZi2uAUJoTS5YiONgixaSWtQgR7_VBDU7exNpmJZLc5Z-tLwzzJkYz25BGj4THBmzEAmGv7xQt4hcugkqBrn5r3V1AhlrZjIqB0IDIq9z__iWbxzLks-nfzBEAZ1nQRhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام:
امروز ساعت ۱۹:۰۰ به وقت شرقی، برای نهمین شب پیاپی، موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات با هدف تضعیف مستمر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامیِ در حال عبور از تنگه هرمز به کار گرفته می‌شوند، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68602" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68601" target="_blank">📅 02:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68600">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز شدن دور جدیدی از حملات آمریکا به ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68600" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68599">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
خرم‌آباد چندین انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68599" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
انفجار در بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68598" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68597">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=VJgwfC_XCZbY_T4Vln2oRYpS1f5cpW71wKOPEKOfZFWbbBLZjiSjivrHyMC9aRZDPW7HWgv8EXl3DNJDHNKS9je8uPaQEHfdQHN_nPue96QYfOkrqQXDK2I-70fnIy4soh97pkRoeJ6qL4fs5wLgHAHHB2SMxocVMoKUsC9cHfdHqNA8l2zagK6X6uoru1j0BtfXLZJTt7FBb8nH05BMzL8TPFbe-FqtKgQ9-bY8sJWjscY8Ftfh4thNu4jwHH4c9t5AmebHJLQ6ppN5b4jKG_IQx4OL1Mr_F-TxHApVPaIfhRV7cBNsebJg-n3v25Wkhx7t3IBPMZbxQxRYerRQEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=VJgwfC_XCZbY_T4Vln2oRYpS1f5cpW71wKOPEKOfZFWbbBLZjiSjivrHyMC9aRZDPW7HWgv8EXl3DNJDHNKS9je8uPaQEHfdQHN_nPue96QYfOkrqQXDK2I-70fnIy4soh97pkRoeJ6qL4fs5wLgHAHHB2SMxocVMoKUsC9cHfdHqNA8l2zagK6X6uoru1j0BtfXLZJTt7FBb8nH05BMzL8TPFbe-FqtKgQ9-bY8sJWjscY8Ftfh4thNu4jwHH4c9t5AmebHJLQ6ppN5b4jKG_IQx4OL1Mr_F-TxHApVPaIfhRV7cBNsebJg-n3v25Wkhx7t3IBPMZbxQxRYerRQEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چهار انفجار در سایت موشکی تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68597" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68596">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار در تبریز شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68596" target="_blank">📅 02:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMnm_AN76xuwcbFe61NkLHTll3Vs8W_qUV1uJxzDHxVFi8o2w0TFUN4anP-RGQ8oNipJRaGXXWoeLqP3NIMyrfp1tEXLyJGBj3YHEyoaDwWvQHNQyY3JJRkvkmfBP7kpfQ0PtJ6SFw97fgIVYjpOYCi50uEAUABOyvkDz-r3rKqo1Rq2qR7wMfD7P_W07neaZGHofKefSjCCHEvZybfbKBdI7y5I9p7DQRGVC0uxzwBboIBPwuVZyWs-PrK0DIMqs9JeAZWK_cal393cquwzMOOFxST6Vh39FVTEgGhKe8pxsDlhBbPTO_-eJbCMjqi-s4UJB7n7Ji9VUDtcXHcXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بعد بازی:
از دو تیم ممنونم، بازی زیبایی رو به نمایش گذاشتن و تبریک میگم به تیم اسپانیا.
همچنین ایران سلاح هسته‌ای نخواهد داشت
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68595" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=rHPY3iUFtyJI9iZz1oZmlkZQmc3dSytuSHdneu315pM2Ncs8XKEDJftpie2DEI9JiZC_1b7bYr-vD3Y3CNTeVsAI8HrOWCqP54XFDKkGAJUApVIpKikDMCjFsYu03j3idpikTMtxn_k4Y0VkX_t4YPlx1q8BZ9W3JBauOzhX2lZwu9fdGwtNHj_oN8JNgOS9hTY2LgNSHvSEdEOxe3Dhcg-gzqmkKhNZC0TurGKaMooLK663vwFME0tEbQk-iyxIWffHXIxCiJXv4xhwszbHwk-uVL9GPn9qRV5_wcIMpdsOH847I-NoADX2RCJjMScAVsbVvZ_RS75w456CAaW15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=rHPY3iUFtyJI9iZz1oZmlkZQmc3dSytuSHdneu315pM2Ncs8XKEDJftpie2DEI9JiZC_1b7bYr-vD3Y3CNTeVsAI8HrOWCqP54XFDKkGAJUApVIpKikDMCjFsYu03j3idpikTMtxn_k4Y0VkX_t4YPlx1q8BZ9W3JBauOzhX2lZwu9fdGwtNHj_oN8JNgOS9hTY2LgNSHvSEdEOxe3Dhcg-gzqmkKhNZC0TurGKaMooLK663vwFME0tEbQk-iyxIWffHXIxCiJXv4xhwszbHwk-uVL9GPn9qRV5_wcIMpdsOH847I-NoADX2RCJjMScAVsbVvZ_RS75w456CAaW15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🏆
لحظه اهدا جام قهرمانی به تیم ملی اسپانیا توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68594" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=jEBr4jAcDiFZPNlmBjglHAM0mFCzB7_YyzOqQJvXogwe1_vywjgBhwM9bt5UK3nsH0foQehtUoZN05FbQkTsKjpRiYwgCjRVWuxfEtu-h6KfCzQ18Ro4cWGvomMTEBUBRgyswELyvAjDgnL9C2LYZ3M0_cDhWCRzMwyLbTwjKkwknuzNjjZmwJhml51ug87gpMWYjQpkMrcJJ2o9KB4MfWzRKIMrGHFrUKAzZktfSnYfWhF6vn86tp5g__9JSsl5MwACWK0N98plfYbw5oEtCydIxoD4thbbWwmTFmVX-4JuWFcb0xPcppdd8uEgfXZpduCnCScsOYfCDWF1d3CGLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=jEBr4jAcDiFZPNlmBjglHAM0mFCzB7_YyzOqQJvXogwe1_vywjgBhwM9bt5UK3nsH0foQehtUoZN05FbQkTsKjpRiYwgCjRVWuxfEtu-h6KfCzQ18Ro4cWGvomMTEBUBRgyswELyvAjDgnL9C2LYZ3M0_cDhWCRzMwyLbTwjKkwknuzNjjZmwJhml51ug87gpMWYjQpkMrcJJ2o9KB4MfWzRKIMrGHFrUKAzZktfSnYfWhF6vn86tp5g__9JSsl5MwACWK0N98plfYbw5oEtCydIxoD4thbbWwmTFmVX-4JuWFcb0xPcppdd8uEgfXZpduCnCScsOYfCDWF1d3CGLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لحظاتی از اهدای مدال نقره به تیم ملی آرژانتین توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68593" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68592">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=Wuxz3omxFKDVKLROOQZJDKRnvnCAkosaYzEacoOzau95uzpgj7qGm85Vw3ZA23TVeDYahQc_S1svsVtwBxirgAmrCy1rDsU03yGVBG7vTxDmB7AdOyCMJgTCLVacOjwi8sw6CCrPKUZNVPVkTrNuiHp_vRIy6cVPnmfRTDW4qSoMcs2ZOeDzoHekl3kh9DoEsF_3hEVShxLSdze6VahQ1vNfeoxuaKvn4cSnudYZibo4PPSay5V6QTzf--kDsTjlPQmOvv-vni8E6Dk9NVbRFjzTY52Tlg01UN-25-0_Jqo4pl79tRaRh6qkXdCmJIVzcVpnpgCN4zeYk9rEUNIF3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=Wuxz3omxFKDVKLROOQZJDKRnvnCAkosaYzEacoOzau95uzpgj7qGm85Vw3ZA23TVeDYahQc_S1svsVtwBxirgAmrCy1rDsU03yGVBG7vTxDmB7AdOyCMJgTCLVacOjwi8sw6CCrPKUZNVPVkTrNuiHp_vRIy6cVPnmfRTDW4qSoMcs2ZOeDzoHekl3kh9DoEsF_3hEVShxLSdze6VahQ1vNfeoxuaKvn4cSnudYZibo4PPSay5V6QTzf--kDsTjlPQmOvv-vni8E6Dk9NVbRFjzTY52Tlg01UN-25-0_Jqo4pl79tRaRh6qkXdCmJIVzcVpnpgCN4zeYk9rEUNIF3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دونالد ترامپ به منظور اهدای جام قهرمانی به تیم ملی اسپانیا وارد زمین مسابقه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68592" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68591">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDUQQjsSITdC3r3sR5aVRbTn5vxqjoRc9UXGInyUnB0dlKtNeZPB8Q0J6Ldt0WaKx6QN8Q-kpNaSsEmdfoF7vDJz96CC-LsH2ThgJhDaYKBX_N-YRAubW2wYbyANDtRctQEFWFFRG_APxJLw6i0QtZgnt1vsUFKilqm9Qgd2bswVXBQgD3kX9k8sX-8nM7yMyv_7q9ZiVYwpWnb9jWaaJgmYX815Hd-a7kh7PiT2nI9MWaXAnrEqt8nxpowUFBDi_jU5ZjMYGwqJtCaZWqxpUmAEu0Kh0tlP3krNeKrUx9KQXzL9jSqY60x88iq8csEWmGY-dwfnH_ljDvufy4P7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
عرزشیا به زودی:
ژنرال فرنان تورِس، از جمهوری اسلامی اسپانیا، گلزن در مقابل آرژانتین
😟
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68591" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68590">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vthR-YrbYSEtVr-Z2EkhbkdL8mXRGXzmEH5LmND-ZfhU4YruELWhK_mUHdJiP7EzHsdJlki-UXgqXm59Nf2C9J0rn-8hG9PvCEAtWofwAPkhPvK6TtMEAZBlQGUaGHADmtOR8oaYRP2IYSaDF24YX1s4LVl84UoMx3DP2JY3jyjiqgw6WFXe4YGQsl7kMbIG6NlFLNVGwdyfqbMyJz7DOlgP5IaZoZEl6JtXqYyrISqBTftDNw8JoeQUK8XChyuKm4PXLgNi7NcSvPeWrrAECmGGlkFoAWtPO_QJt97fnZah9tXN0uWyjegK6y9hjmyo61HUXZorNsKneAG5IKRJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ اومد تو زمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68590" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68589">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امشب سنتکام نمی‌زنه یعنی؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68589" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68588">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iao8BzoiCBzqqxjnI8yinudjXX2GcRhNZWGGiqb6iAvdh8bj1M9CW29Iw7CWWoRa2bLFyTQT_xrNtSJveP_iVOzWtEBCmL-KhU1SHSnLxZ7Hc_22tY__XxKtT8xHnf7hx84r3jRQD-BdqyztLi6m5Zz3jxTNtPwJxDbWxwXFCv9_H7uTHTu-1JU5X98kUA_zMRfAhjZ0x5nZfdVKjobtzdvnTECo4-qExvbvHKyG-gH0RTNMCcDcrObgBCpVO4nwJbTZ4rPwNU7SkKeNEBJdo7hMB9X6_PABuY4WxqxCeyyx9QWmzEDdiEw6tq3JaBiGy4FAUmJDuzTUwVPD7qdJfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آقا تموم شد به راننده بگید حرکت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68588" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68587">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWQZPDiGqVfW7LPRt1i9JU6mDHU7l5x1N41w50lF12nptjFKhKtkHRioeWx6euEG41KGNE_v84jAZkcgB6k2mNC9EAvVv8gcZB95GKj_uIl96kiRyD_lIlW9P2LEUg81QfJoWb1BsSxv04YJJtN3jit7OuXqa_9eOQp8G49I2E_TLvKKcz4caZTogYgfQUxwD5CbRWWjddsdklUEr9doIy642zZcrJASByhzEXLeVpQoULk0Nv7bVzDn8Y2rFO0HjACHcSwbI7xITmiAtAv6Fn1cPUf_bYYi2uTC_yPl1XMh9t1DwGevnYEeYFuXY9qudngEL3yxUlM0mFAAp0c1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 هم با همه خنده‌ها و گریه‌ها تموم شد؛
قهرمان: اسپانیا
🇪🇸
نایب قهرمان: آرژانتین
🇦🇷
مقام سومی: انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آقای گل: امباپه
🇫🇷
آقای پاس‌گل: اولیسه
🇫🇷
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68587" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68586">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnksIBVZ4t26tairfJUIHEify2PL8IqYINj43qX--jKlDKsr9fL750M2qBrvlrPvvHEPlLmSB3fjPGujtefFuYQGNfqEJZSXO08VIi8S9l0e95nY1oLIf45uHiuuyoCVJXw28JRY4Pi7WwvhlqDHyT_Q4sQiI01_pnQSg-D2zdDfLAuLM7vhpahvV0ntqR4OJPCh8b85YOQ6ace9SN4xilvIWI-oWXN8INCzekMJhtqpSX4w8IKDus_np1eOrD-Dc60N25JDSlVGIR1EWTCZu09Go_BkxkiWr_f9hGcdJ6VxNotSmEqv0i3NuWl1nyjRmbw-6bcogAk2q2Ljp6p0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
🏆
تماااام؛اسپانیا قهرمان جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68586" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68585">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اسپانیا خیلی بهتر بازی کرد انصافاً
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68585" target="_blank">📅 01:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68584">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به آرژانتین توسط تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68584" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68583">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
گل اول اسپانیا به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68583" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68582">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBUkHue4tSxVTz5SPuCxy6olnYOMQ1dZSWEiW0X2LtmPpJsYDlMdHToDkDp1tDwoXVxK27FP4mYtdlRfhEVIqzNVCstusJffkQCpxnMs_qlLYMjA2vOTvF2rzqA7XN7SkV86z4I48oOVEG668J9od0v7HyrizjZdLaFlY5c6wv7u4uWmfVgNmX-ow3urGdwNq1fN8iV-UVfee8ZbXPnfhaHx2T3GJB19cP2_8HcDRjvwHrJBfmjVNck-bzM1fDld6QUlGiOJdAjdSYFwYH0HgxCwuoMgNnuyKdJVhaI3VsNGHRiHUCQObL_aj7RbDLaCrWE87r-anTi6mHkLD_WD9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پرچم شیروخورشید در ورزشگاه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68582" target="_blank">📅 01:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68581">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بازی که رفت ۱۲۰ دقیقه، نیروهای سنتکام هم دارن فینال رو می‌بینن، حملات امشب، نیم ساعت تاخیر داره
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68581" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68580">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
آرژانتین ده نفره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68580" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68579">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
آژیر خطر در بحرین به صدا در آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68579" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68577">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fe75354.mov?token=tgdqOZsHNEk2fVT819nTFpYoXtqmLbVXwPdG4f5-IAiCSaXGRMRrYPMQKfby2Yy2vUcFZcAOOz2J0ymwQJNHN42hKJ-tMnpzXXHwWP4pUt49sb8hSTuIW5sJNdzRjVH-y6QrJPcAbp3ydJ1sugCsLzlzWILlDOSk14GvyxkmLUQnslfMRIvm38kKek3ZnoSBKjNJOAR9_jgxgF3WCfnBfCWlVNAJaeQLfJS9mBQZe_yj3hwZIMycyELt6lEJ3SKibcJzzUew8R3afQIOE6iEdehTdL-AkjlYW6jwv0uHjzB1iKGPS4IwQHetwc2eX15BDet34164YN8wcu2IKCMCrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fe75354.mov?token=tgdqOZsHNEk2fVT819nTFpYoXtqmLbVXwPdG4f5-IAiCSaXGRMRrYPMQKfby2Yy2vUcFZcAOOz2J0ymwQJNHN42hKJ-tMnpzXXHwWP4pUt49sb8hSTuIW5sJNdzRjVH-y6QrJPcAbp3ydJ1sugCsLzlzWILlDOSk14GvyxkmLUQnslfMRIvm38kKek3ZnoSBKjNJOAR9_jgxgF3WCfnBfCWlVNAJaeQLfJS9mBQZe_yj3hwZIMycyELt6lEJ3SKibcJzzUew8R3afQIOE6iEdehTdL-AkjlYW6jwv0uHjzB1iKGPS4IwQHetwc2eX15BDet34164YN8wcu2IKCMCrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گویا از قم موشک‌ پرتاب کردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68577" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68576">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ComZXDHbM2EVmz96BZjtCEzyOn4cHSJSFYUfBDVdgEP3Ra2WW76seYKtVtId2FfZRo6BhA13KAr9JSi6TIEPj_uBAZgaGj2ZiqxbaiLNiyD5LWh7JKiqWEoyCcahUK0vb8EbgquwFIq-jcWw_F_JkWbGkX1sNWIlYtlxLgLSZH3fk1MpWscFwdLtrQshFkqfBeVi8ZQRvw7K0W1Rlud0Kqp77T0sMtfg5hj4gb0aPXDbD0VsJrP8tR1vy4Py-MLAlJt9NpObCVqcRrT0B-xIFGNBSFGcqz_XAoJM64HBEZYEDbc5UAaIZ0_gIGh5jxWD4RhWrwieGqrzCYMunfi7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بیژن تو فینال
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68576" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68574">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🏆
اجرای کامل شکیرا در بین‌ دو‌ نیمه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68574" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68573">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏆
🔞
🇱🇧
حضور میاخلیفه، پورن استار اهل کشور لبنان در آمریکا برای تماشای فینال  @HutNewsPlus</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68573" target="_blank">📅 00:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68572">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه  @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68572" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68571">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68571" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68570">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=W5VZd_MGB9YLDllQUpNHzKqPi7e18gzkK_hfvY5rBC_D3DuLgV4m9EY53SjWBLyPClhv_S1qjJF7JIFGhhEhxgTD1BZHRhXOI-zJty-RJcw0ChScc1o0Btx5iaSz_VkqPARpLWhN88s1kX38r4vtqoMmlmgsidoqSK9TrOKurX_wefwkLWC8FYhsaNYztgEeiZKjRGbaIFpk5r4B-7iXIdNsYo054ObSGox9Yzgpz9Oj-kz1PDujymNCUBnpTggofV7VGomHYRX3eSiSzytzAH80mEia9W9_mL4fcGbIl4TaqEsk1OgEaUKgm_NTjGmuyxWMVn8KEVwj9-uawYFOGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=W5VZd_MGB9YLDllQUpNHzKqPi7e18gzkK_hfvY5rBC_D3DuLgV4m9EY53SjWBLyPClhv_S1qjJF7JIFGhhEhxgTD1BZHRhXOI-zJty-RJcw0ChScc1o0Btx5iaSz_VkqPARpLWhN88s1kX38r4vtqoMmlmgsidoqSK9TrOKurX_wefwkLWC8FYhsaNYztgEeiZKjRGbaIFpk5r4B-7iXIdNsYo054ObSGox9Yzgpz9Oj-kz1PDujymNCUBnpTggofV7VGomHYRX3eSiSzytzAH80mEia9W9_mL4fcGbIl4TaqEsk1OgEaUKgm_NTjGmuyxWMVn8KEVwj9-uawYFOGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
اجرای عمو بیژن
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68570" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68569">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIttn0OiVWGmlGsg7KdH6CrRhYv58L3Kdzivue--otfcjGeV_tt75OK5p8zDX39QfZqUOJTxw5YcginGLfrFw87Y7P2rYo7dOLZ4KXPxWbe9WuCose_dN26ZUnoHHm7u1zhNEFXQhx6lAeMO7AsEUmdQ70t6ss71IJPzbLxtQN-cd9OQt3iJyZ5XSVqptUU5hIQZGFbhMo7ZasDCrzHW4u4au3C6rnAoOTqCWWdKuMY7DqfbLIkIf8FsACr0SAt1whKVIGX1PERZrBPdCRnw0ieEjqmrZ07pjrqMwttKpyyGEeIs9n2rKHHZN0wUvOORN39enSxruR_ASzVRx8SoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه آرژانتینا دارن کامل لخت می‌شن
🔥
👀
🔥
🔗
مشاهده ویدیوی لو رفته از دختر آرژانتینی
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68569" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68567">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4MRlAj21v-Ab85jekCSZxMSIM4HjI9BeHwMjBXEBWyKaBEAZY_yGE3zViA_X8pRNQqGzM9zEk1AJhygs1ZsMBNM9A3Gkj3z6ZD2-vbAvQbeIFlNHflMz4pRWL_JpRjMGx9FmGeWslFVBeF3zMQqhtDPNTiP2ZCOd9FGOcg8UMyk1OqHvTlKX2gXS2Leukpw514frdm-y_4hKPmiyOT8u2yZRrKmW_L3K04FQz_3v_RSJnVsyLSVxEhLnK5lPnRdXDOZNcpmkvE8Oz6I6YtPXWY0zGS9Si23GwjInrMZVcPt5OEE93tgPjIDoCQ8_NFrF9ja3i712Ww8jLzIPoyz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
روز گذشته، فرماندهی مرکزی ایالات متحده (سنتکام) خبر جان‌باختن دو نظامی آمریکایی و مفقود شدن یک نظامی دیگر در اردن را، در پی حمله ایران در تاریخ ۱۷ ژوئیه، اعلام کرد.
پس از یک عملیات جستجوی دقیق، نیروهای نظامی آمریکا امروز بقایای جسدی را که هویت آن هنوز مشخص نشده است، در محل حادثه پیدا کردند.
فرآیند بررسی برای شناسایی و تأیید هویت این بقایا در جریان است.
در رویدادی جداگانه، یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
نظامی دیگری نیز در این حادثه مجروح شد و همچنان برای درمان جراحتی سطحی تحت مراقبت‌های پزشکی قرار دارد.
سنتکام به احترام خانواده‌های این افراد و تا زمان تکمیل مراحل اطلاع‌رسانی به آن‌ها، از انتشار جزئیات بیشتر، از جمله هویت نظامیان مفقود و جان‌باخته، خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68567" target="_blank">📅 23:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68566">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA9wb-KbtVeGitEcGnmIA6VvxLNMUxg-LtEA3XJXqgVTXiYM-IqKDrXPmu3t1LXnU10lFPQSW_kq3QSZe9uQU_lQY0dQTdWV8BcbTI3nNIK29_ddkGYXVs5h7xJdiBbWqrmkc28CVoVUX3tQz61VneRKYnoYB626Q_Tywlx9y5EkrhctBdbjBeabFjQo1V5uBu_zwaMjJPxHzKz_gPC_VRJQ3_eLRRjupryDhBTKBiaNUyGndhBJpr8K-KmmR32_FW0XICCLwnEE0ZwA8AtlIX2wAxCoUrSURPtUD_YGnx8mAHeFEET9ibj-8lqBZW6-l17Y7OOEImvf9_78tsb0Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک #hjAly‌</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68566" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68565">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=TV1ci_d000oi6a-ZyFLvYRw4xQmcxntWmL8qWp-Ny3-vN749pSlru97ctKxTID0a2PsNMYeh1FXLYqQhYMpz9ptC7EomdAJHZCaOw2i2Z-GrblzrfOawGuUhc-DfJHHb1we01G6hjt9woj5CWuchFgeTaGCoQGmc2udbW-CbNTPvHHfD_xp_W6DqApFeYv7g-iqGb3UHyqrwd6kW0QQYVV7xu9fOThY2CsNHCK4hEs_xiHaPQLmeK0aSRo7uPceAGvWRIuEAkyHIH5sQwdmOgXM6b4vkTS8ptRcCwMW1Zgn_py1AdAcMJ1PZamFO0MaXxjKTmYSwnaMzcsOHK8IVh4z7vwEq37Zn4LF9aSTnalj7oFre4oFEc0P-db7gzwzRxMGwqz_3IyeRaQlCUSFMlYSab8KYyvRm0fQFC20gbJ_cHk-UXej3jPdiGzqxuPKR01kKFvFcrAmDHoE6QhKjHfySP7j4Zcg9co5APLC7NxNF1BFjdSQK7mEXZlLFGVZekk_2G57nmJRWTqJHpMbTXEqsvoqWL58awgXJi6FobWipNDQ_ejKslhEy_vLugwhj0wNMP1PSp3nhl6UwZxAu-6caVnsLGYZUtSqrokQOe_NU99cP7q4uax815VFDhDixQdEIgcACHGND2Oub457o9EkMICOHEmqcph6m5Pqjr34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=TV1ci_d000oi6a-ZyFLvYRw4xQmcxntWmL8qWp-Ny3-vN749pSlru97ctKxTID0a2PsNMYeh1FXLYqQhYMpz9ptC7EomdAJHZCaOw2i2Z-GrblzrfOawGuUhc-DfJHHb1we01G6hjt9woj5CWuchFgeTaGCoQGmc2udbW-CbNTPvHHfD_xp_W6DqApFeYv7g-iqGb3UHyqrwd6kW0QQYVV7xu9fOThY2CsNHCK4hEs_xiHaPQLmeK0aSRo7uPceAGvWRIuEAkyHIH5sQwdmOgXM6b4vkTS8ptRcCwMW1Zgn_py1AdAcMJ1PZamFO0MaXxjKTmYSwnaMzcsOHK8IVh4z7vwEq37Zn4LF9aSTnalj7oFre4oFEc0P-db7gzwzRxMGwqz_3IyeRaQlCUSFMlYSab8KYyvRm0fQFC20gbJ_cHk-UXej3jPdiGzqxuPKR01kKFvFcrAmDHoE6QhKjHfySP7j4Zcg9co5APLC7NxNF1BFjdSQK7mEXZlLFGVZekk_2G57nmJRWTqJHpMbTXEqsvoqWL58awgXJi6FobWipNDQ_ejKslhEy_vLugwhj0wNMP1PSp3nhl6UwZxAu-6caVnsLGYZUtSqrokQOe_NU99cP7q4uax815VFDhDixQdEIgcACHGND2Oub457o9EkMICOHEmqcph6m5Pqjr34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇺🇸
پرزیدنت ترامپ و بانوی اول ایوانکا ترامپ در کنار اینفانتینو در بخش وی آی پی استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68565" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68564">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbRGcp1psZE8aHxc-iBl8vJ0ovxyAeRWkCO9ffZIgG4hOGvc0CkXSJH5bFVVIg0Ef3pgy49YrjFH_RNclLdqetz68DdyLphPkJ7BpnAuwEm2E99_FEZmnz7J7YYTHseKuXbFjhj5E5cyAOeiObuLwfScYFeSqw5J1AYNfGy9ZeXIfXnkKTpsSiSZzU6v4TgXpvVWuCiSHhe9qQYODt-QfE8JlPs385dtdqtrOc6z9gk4DYWy8h790RiUQ3vG3tW39wRUmcJfu0C_hZDRZF4kq-HHR_5-n5E4OeHcc3mBWu7ctGrB1RTzAVBK8BtuJI3hCl9dMGKLdcCZQ57Aguh2jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
گزارشگر صداوسیما : هیچ تصویری از ترامپ کودک‌کش و جنایتکار نشون نمی‌دیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68564" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68563">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68563" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68562">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9k4jT8bp-D3CukaCTlP9Affd6JaXL7kWhgm8_GEUqkUej5wPu82OBtnNaI4DXyUHbcgFHDFlm01W6IrAgKaqE9yaaXMiOq-IICY2rnfXV9asSaxTebzO6RM4GrkT91Cqnw9me0YEsYOrIHSiwvuagy_vQn3iflWMEyRFmf_PlEtBcQteN2HcrYZsy6YxqCpBpR0Bc1X4_W1dsoOwReDZYiSPtsBzpnJY7n_xsiZ8tzB-D7Td6_EdZ23iMleSROzzBaNrpO9jE50nVJDtgdwnm_GJIh7qVxhWuC9eP_nTprcGxrnKZCnBZ9HBbTrAtDj7j556Pvxk6_R-KqYqIPrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون ترامپ پشت شیشه ضدگلوله
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68562" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68561">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP3qj-pPh0-JguqddUkDiqeS58EyT3Getcj1LKIr_uaYI2JE1G5IDYGs_NhkXUsVWjtIsfnsAfL-joSRDqiYd2XcNAJ-sEgWt281rs09gbHfqEyB2ZImmr4bGHro_82X2xnuD8t6Mo6xsQKnQgtVyAhXpJOR3sOeC17j6KZZhFCVsO2VGo_HqZ5UXf7TrubZnnGj1Ajv8aJxH8UrnOOc2bNn46Pq3XwHFuekIakkxlkyXoLN_cIRpgD5CNS5psqpTDjaabShY6DcJovC65kKG0cYSsD_4x2eIXOliMge1R5b3RGfBBwJQKUx8P_lGKIusX8MllH0TvwCeqmXM9suhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام جهانی هم شروع شد
سپی
یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… همرو
بدون سانسور و رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
https://chosefil.com/fa/programs/318
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68561" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68560">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de66012.mp4?token=P17Unzez41elK0Npn2Rmz29P80x0bZ-yZ7Z2NjlMSBGaIDyilweFYGVCz5INxOX89VxROyLDqRcXKHuX-2EdWiWWWz4AMHIsN8kfgh1hPhR4oapKQglazVH-6PCNGyFoOIgGw3PdPNx4NxAOz5ixUcgQmgvdoB9ScWO4c6pHOz_O5fw5RGy2XptTT04RkZr7idtdLU5ddMgTsui2hEVktrbwYAUwRTPtRwcnXKyQQPS9a2I967FIn5UoBmM21mQ7EBceKvg1VwwqYEHCYWkhpYroE7K5I_LRcH5TKOByoPhanShSeFncsmX-2BdJHKwfZSLT1UBnkzXqYiVhcFJ3xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de66012.mp4?token=P17Unzez41elK0Npn2Rmz29P80x0bZ-yZ7Z2NjlMSBGaIDyilweFYGVCz5INxOX89VxROyLDqRcXKHuX-2EdWiWWWz4AMHIsN8kfgh1hPhR4oapKQglazVH-6PCNGyFoOIgGw3PdPNx4NxAOz5ixUcgQmgvdoB9ScWO4c6pHOz_O5fw5RGy2XptTT04RkZr7idtdLU5ddMgTsui2hEVktrbwYAUwRTPtRwcnXKyQQPS9a2I967FIn5UoBmM21mQ7EBceKvg1VwwqYEHCYWkhpYroE7K5I_LRcH5TKOByoPhanShSeFncsmX-2BdJHKwfZSLT1UBnkzXqYiVhcFJ3xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری حکومتی:مشهد در18و19دی پنج ساعت سقوط کرده بود.
عراقچی: اصلا انتظار اعتراضات ۱۸ و ۱۹ دی رو نداشتیم، جمعیت خیلی بیشتر از چیزی بود که فکر میکردیم
.
مجری: ترامپ درست می‌گفت، من رفتم آمارش رو درآوردم، مشهد در عرض چند ساعت سقوط کرده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68560" target="_blank">📅 22:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68559">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=ZcuQ7X4aNM0erPSSXr4OjSoNAUG7jZIaO5kzpQjlWvpN5JumtCd3ROI9POv_sp2M6ywvbOx0oQm2oyEWmAHElFx3vj9jqhKu7fNv5XzzPXWRt3iEiM_wfD-iKI3YVYrib099inpmpTG0RCaL3m-0Zk71PApvOdVD0c9ypg7oYQpHtJNWjqIu_fImkq6xgG4ieWHEwsnE5u00Thwa_X2Xt8Og5d-tnu0yKavV4p8FzLFSrVt7Ns5oR5azYjHhemCwYEtknntnoYeO_SZVN1sEB-cDuDPPlKZBITLHhMqNc8huxoJC1KCGn2W56Vy5rbX9Re3yIq54fMDtGJNZkNAZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=ZcuQ7X4aNM0erPSSXr4OjSoNAUG7jZIaO5kzpQjlWvpN5JumtCd3ROI9POv_sp2M6ywvbOx0oQm2oyEWmAHElFx3vj9jqhKu7fNv5XzzPXWRt3iEiM_wfD-iKI3YVYrib099inpmpTG0RCaL3m-0Zk71PApvOdVD0c9ypg7oYQpHtJNWjqIu_fImkq6xgG4ieWHEwsnE5u00Thwa_X2Xt8Og5d-tnu0yKavV4p8FzLFSrVt7Ns5oR5azYjHhemCwYEtknntnoYeO_SZVN1sEB-cDuDPPlKZBITLHhMqNc8huxoJC1KCGn2W56Vy5rbX9Re3yIq54fMDtGJNZkNAZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پخش تلویزیونی اسرائیل؛مقامات امنیتی اسرائیل و ایالات متحده:
ایالات متحده در حال آماده‌سازی برای تشدید حملات خود به ایران است.
این هفته، خاورمیانه شاهد تعداد بی‌سابقه‌ای از هواپیماهای تانکر سوخت‌رسان خواهد بود، که این تعداد حتی در مقایسه با آمار ثبت‌شده در جنگ اخیر، غیرمعمول است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68559" target="_blank">📅 21:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68558">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
کانال ۱۳ اسرائیل :
دونالد ترامپ، رئیس‌جمهور ایالات متحده، پیامی به کشورهای حاشیه خلیج فارس ارسال کرده است که در آن تأکید شده است: اگر این هفته آتش‌بس برقرار نشود، این کشورها باید خود را برای تشدید تنش‌ها آماده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68558" target="_blank">📅 21:36 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
