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
<img src="https://cdn4.telesco.pe/file/LOmm47VkYr54Fv5EbfcjMyo2gps5sTghdTO5RHR9kdUOAneDgNFQpNfxfPAnX3Jdv3saBMTONFKAI46jOE42pzHAYaNkpe6MxqnJRsedTyz8wvdOcRH6vxigx9yJLBvHJB-Ix1zDo8bV196_dO3-Cok7WAeP8CJEmS6CCKEJ0UBGNjZGs2Waih6pLRmcQFfssaRWSvQ3-AGXSs1_nCxwZ-25W45zh92qnt28G9rSa66bN3i4RpjeOZmKiCu97Va1kska-3nCUvrt06yeMWHdyC1amusXvHNZp2WwQO8K_ztxYDMR3sTPTG7lt8UVXD4s8c--A02mvp4Q1IaLRIMKZg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.94M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 03:28:01</div>
<hr>

<div class="tg-post" id="msg-654081">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
خبرهای داغ امروز و امشب را به انتخاب مخاطبان وبسایت خبرفوری مرور کنید
♦️
🔹
آتش‌بس نقض شد؛ آمریکا حمله به ایران را پذیرفت
👇
khabarfoori.com/fa/tiny/news-3217914
🔹
اینترنت بین‌الملل فردا باز می شود
👇
khabarfoori.com/fa/tiny/news-3217890
🔹
رهبری برای مداوا تا ساعت ۲ بامداد دهم اسفند مهمان ما بودند
👇
khabarfoori.com/fa/tiny/news-3217778
🔹
کانال ۱۲ اسرائیل: تصمیم برای حمله بزرگ علیه حزب‌الله لبنان گرفته‌ شده
👇
khabarfoori.com/fa/tiny/news-3217652
🔹
سلاح مرموز آمریکا و عربستان علیه ایران/ جنگ پهپادی تهران - ریاض آغاز می شود؟
👇
khabarfoori.com/fa/tiny/news-3217866
🔻
ویدئوهای منتخب را در آپارات خبرفوری ببینید
🔻
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/akhbarefori/654081" target="_blank">📅 03:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654080">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhNdqIuzsDODllyLUMyK7iH8AnqH8fdkBFds6nVjyi2pgvqXuehb3tPhlfaXvKA_PFhfONcgXilzu1wB_3Vf8OjwdkMGw58oUcdt7zq3apMRWC_Ti0mNnzg094svD8Y8w0QkLq8keQaZ5rFjlkXrKMKL5qh_zWDKbVOTJNoiVSWSmS9FySu7Bq-_KcQTAJeoESPtvnGZUsaivAzdtEcbjpvfLV4n-a4GoU2-YyiB20WHR6Ai0l4Vu_Dv2g71tFNXBwJejvM0MLRcEpn03D_naqAFzVX4uT3_Qp2wCtMQRydNF5newhREupLA8JfLcQq22pRDDWYRwzVzLC2p53gT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان سنتکام به نقض آتش‌بس با ایران
🔹
سخنگوی فرماندهی مرکزی ارتش آمریکا بامداد سه‌شنبه به نقض آتش‌بس با ایران از طریق حمله به اهدافی در جنوب کشور اعتراف کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/akhbarefori/654080" target="_blank">📅 02:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654079">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP2zPv6468CxI0wkCmgb9mTyM_RPOTIUQrVCYnWBctZG_EnOJSUsZyufYRkvEe3zJmzDeoYpmswTAmS0vC6gidRN6oGyLsOs1nJCkQNwKbtpmbElVlY20oZ0nP6VNCeEXsRuH18fdDEN_Qhitl5Jioi32B8UayzgDv6auiNNa0LZc0KWKRJjkN32g7bVBYXuMS4Aa7rKAYqtGrpQY5D7OBooDU4tmSnEE_ncNP6zckJodWiaO3TS0hf3y6lvSKh7k1uho0iic7hNNFNzv4ICpjCDWkZ-QdC9W4S-LJxY9tslO4RBKQHthxdUFWRW4OhsOvejHySU6u_x1F4EMQ9FAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بار دیگر زیاده‌خواهی درباره اورانیوم غنی‌شده را تکرار کرد
🔹
رئیس‌جمهور آمریکا بامداد سه‌شنبه مدعی شد ایران یا باید اورانیوم غنی‌شده خود را تحویل دهد یا آن را با حضور ناظران، نابود کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/654079" target="_blank">📅 01:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654078">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5aZwzsbituUBO9s-nATkr6JCH3ZuvR2a6AomqlqPTcrrSaCR29ov2UWCOFuWB9JP9OmS7ALCMrNo8SocTQa33pZGQVWtx4YYGA8c_K7rVzjlSNvgk9MunBp3wuE1AE69v_u-Y7fwlOF1ipyy0wjmebRwfOyTXjySAhiR9a0sI01TAJReXgNh8RrcVJTj2MIV5cLouMDYQYM4Q86UGDTexYl_Q48uY8gNxYwPl7EUItjOZCQ4Nrz0Ue-bL4S0M91NdAztIIvZPMyfyTQw2OjkhW3O8igavni-n_O1dZDURVBKT_2cB3meX7wERfGVHzMe_tBhK9TIghB4cUlS57Otg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبر: منبع صدای انفجار در بندرعباس هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/654078" target="_blank">📅 01:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654077">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
دو قایق نیروی دریایی سپاه پاسداران در خلیج فارس توسط جنگنده‌های آمریکایی هدف قرار گرفتند و چهار سرباز شهید شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/654077" target="_blank">📅 01:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654076">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
مهر: اوضاع بندرعباس کاملاً تحت کنترل است
🔹
منشا صدای انفجار از منتهی الیه شرق بندرعباس بوده است.
🔹
همزمان برخی از شهروندان از شنیده شدن صدای فعالیت پدافند در این شهر خبر داده اند.
🔹
اوضاع شهر، کاملاً تحت کنترل است و جای هیچگونه نگرانی برای مردم شریف بندرعباس نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/654076" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654075">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
تابناک
🔹
باند پروازی فرودگاه بندرعباس مورد اصابت موشک قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/654075" target="_blank">📅 00:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654074">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
دقایقی پیش مردم در بندرعباس صدای چند انفجار شنیدند
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست.
🔹
همزمان در خلیج فارس حوالی سیریک و جاسک نیز صداهای مشابه شنیده شده است.
🔹
سحرگاه امروز یک فروند پهپاد متخاصم در محدوده خلیج فارس توسط نیروهای مسلح ایران منهدم شد.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/654074" target="_blank">📅 23:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654073">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcVG8nSoWGHSyLPsMzJVrPbqonZwNtK8Ufo_81gJl9b6qSrroOlIETzIiqY7Z9_-ihzK5TvLZDZoDwdrQcIFjRbclrob8GiImYGlkykCk5a6saKDlvLbimbmxyUJosbBniSo5ceZUIpcjMe38f6BEDw2ogbw3zp7c3jhJuiWLFf_JZl6dwgAoQQU2B1xsEcBDUx9gzfLC5klfKXCeulIzLzb2Cg1Y72qcjXlDcprcvkGe1OtZGgWRuF079ZEcmVfE_DIWtNE5IzrOCu4l7X-Sky5YsQjo0VZwUwSTc5IyXBQFABBUxTv-ZcbrZDRVF1bx5dPcgOnA1pIeyCw9kLUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وظایف مسئولان و دستگاه‌های اجرایی و مدیریتی در جنگ
🔹
مروری بر وظایف مهم کارگزاران نظام در شرایط فعلی کشور براساس پیام‌های رهبر انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/654073" target="_blank">📅 23:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654072">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38a79f3e.mp4?token=A_KSvofc0bBYPFoQ3UP_5I53AekrChTJJikx5xd5ndtlvwGjH6Azot6A4DJzoDL6FsHkNNRfEf32ou-5_Qr8HIBzgXnz613mGK-EZIE9VfdUK2jYJLKBuPmGkdO6SeEw3-bIdQ40C5x1Yxxx788BRSCj0OFaB6bFH55FD1bkyRUhAk9SnhqAW9UiXqfLN2L_B5u-J_X9LPy7ujiqXwrr4yEaHG6-qoYgc2qfJDVRN4Q1RdGzBz0ZbGkN9bKrNMhIPUw6OVgjjkbUv4pJlMU43sCqFmlJ70CBd-ilYhL0teh2QSBRvDtF0aQLuzeT519YH12RraQ1eV0vHGTm0agbGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38a79f3e.mp4?token=A_KSvofc0bBYPFoQ3UP_5I53AekrChTJJikx5xd5ndtlvwGjH6Azot6A4DJzoDL6FsHkNNRfEf32ou-5_Qr8HIBzgXnz613mGK-EZIE9VfdUK2jYJLKBuPmGkdO6SeEw3-bIdQ40C5x1Yxxx788BRSCj0OFaB6bFH55FD1bkyRUhAk9SnhqAW9UiXqfLN2L_B5u-J_X9LPy7ujiqXwrr4yEaHG6-qoYgc2qfJDVRN4Q1RdGzBz0ZbGkN9bKrNMhIPUw6OVgjjkbUv4pJlMU43sCqFmlJ70CBd-ilYhL0teh2QSBRvDtF0aQLuzeT519YH12RraQ1eV0vHGTm0agbGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا ایران به سمت ساخت سلاح اتمی می‌رود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/654072" target="_blank">📅 23:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654071">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e1d60f76.mp4?token=Ug5YWekOD6gTaAZ-W8LtdDC7E8emsQvgGTi3j41cqjh71DQt2x2OOqDrCyDp_lN5jYupk2OjGwJ-oKS8tuPjFud1ov3v2vnorm7WyQhgbH_DMyNHVAD-60dPk_ZCd3MWcgXT_pDKco_uGO-72v--LrGJieGrP4DHVFLeCK39o1R1iYzPnhn96miu2As4ZrTmHp-wyBjcvfXKcAyOxXZ-wdFeq2s15c4xjqgNpHHHrjaFmB_wrX2d3okNV-s1C64AYwZ4cMOf8_9LAZ9FcL7UrM24T5tqiqCLaG6o77tt98OIPhHI36HPHJN9BXG1GL1wlt3tkUfnWVNk1xwRXOMjlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e1d60f76.mp4?token=Ug5YWekOD6gTaAZ-W8LtdDC7E8emsQvgGTi3j41cqjh71DQt2x2OOqDrCyDp_lN5jYupk2OjGwJ-oKS8tuPjFud1ov3v2vnorm7WyQhgbH_DMyNHVAD-60dPk_ZCd3MWcgXT_pDKco_uGO-72v--LrGJieGrP4DHVFLeCK39o1R1iYzPnhn96miu2As4ZrTmHp-wyBjcvfXKcAyOxXZ-wdFeq2s15c4xjqgNpHHHrjaFmB_wrX2d3okNV-s1C64AYwZ4cMOf8_9LAZ9FcL7UrM24T5tqiqCLaG6o77tt98OIPhHI36HPHJN9BXG1GL1wlt3tkUfnWVNk1xwRXOMjlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: اگر توافقی با آمریکا شود به معنای پایان چالش‌های ما با آمریکا نیست
🔹
در شرایط موجود بعید می‌دانم که آمریکایی‌ها وارد توافقی شوند که خواسته‌های جمهوری اسلامی را بپذیرند و این موضوع خیلی دور است و اگر بپذیرند باید عمل کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/654071" target="_blank">📅 23:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654070">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceac5dbe5f.mp4?token=ebZjYs8DOQ9J-Pnkn-FSjt0hreLaatvQmDqfeqFqSXJKSIMbHFbQR4K5njKXOi6E_fbBVATjxW_im93Um5k79HMBg3HoHh9cc65AqV_e5r199ffO39lqc7SmedvI4kdte4xPVtWWcoSAuL2NdNIP4tomqUyiz5BQCGvh9Ao-Cmu_xxVGEDQ-fGKgL2j-xfdzdX5hL7EyXLEnPpUnT3ConlXO3gkPlat3kTxVBXc6woENgLudMW_jBvPQ7aOJZpjARHriT7sRDiGpj-DrIQ3qoYaD-AJwWScKiUspV694wUq0rMFQ93C6ij-QJJAszYytKzN0ljFPQRrr756hT4KgZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceac5dbe5f.mp4?token=ebZjYs8DOQ9J-Pnkn-FSjt0hreLaatvQmDqfeqFqSXJKSIMbHFbQR4K5njKXOi6E_fbBVATjxW_im93Um5k79HMBg3HoHh9cc65AqV_e5r199ffO39lqc7SmedvI4kdte4xPVtWWcoSAuL2NdNIP4tomqUyiz5BQCGvh9Ao-Cmu_xxVGEDQ-fGKgL2j-xfdzdX5hL7EyXLEnPpUnT3ConlXO3gkPlat3kTxVBXc6woENgLudMW_jBvPQ7aOJZpjARHriT7sRDiGpj-DrIQ3qoYaD-AJwWScKiUspV694wUq0rMFQ93C6ij-QJJAszYytKzN0ljFPQRrr756hT4KgZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: پهپادهای دشمن همچنان در مرزهای ایران در حال گشت زنی هستند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/654070" target="_blank">📅 23:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654069">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
۲ تلاش اسرائیل برای ترور شیخ نعیم قاسم ناکام ماند
🔹
شبکه الحدث گزارش داد تل‌آویو دست‌کم دو بار به تازگی تلاش کرده شیخ نعیم قاسم، رهبر حزب‌الله لبنان را هدف قرار دهد اما موفق نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/654069" target="_blank">📅 23:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c740ca854.mp4?token=IzYze0teOdYi5mVF0IbE7z3KWujTe-qdZjE5KEZz7qJEErzD4Ry8-BAdgDqOtBSbmfbKYMP75Zi_gxKQwW44VA2IjvO6PgHNXtC1ZjrqxBKdOcpVGeGniTdJLK4A92d_6ZugvmPIqo7_tHK_xYqpAba4Z3r4cw2HB84kL18f_jyPlxrwon1fADoupFGFUm6G7iW0UTj-sXbyhO5eO4D8or4UOUhp5SjidJUBjiS__haNCC8_CP0ylpqd6kp5HNpVnDBEeDOlrSnLu9bT-hak5S4u8MFmYy_bXBm44DU-v9LfJYTKZ2r57InWbYEOcgqc57nZ7tY4CSq_TU3SH62i-rRmXwNQYJMWVM3RZVj1MCfywVhPZ-ZQXjUoQhO_PfmCQpMuJO-tNVRNNJbrppqn4TzyZkLi6dDL-HjxHm9xnuSFzQRVXpl6wiKySfF3RsrtgytwUWSfzZyR7GV38lqZ50kF1H88xCatGe5TeuENccqocJhR32AIy8Tza5Mj5RwVzc3Vo7TOhOOuthfGsMx0QS3ifO0U_w7bGpvEneKP7vvJ_oe1qPC4IyE3pVD2y5svt8VEBItIymHvDE1npkPM6hKV9sS7ND7hn0peU3xqc-Kkx7Vf4bpSdZp14Z08NGMb5e53fNSofBOFM5y1TB4YbVkKcccJHlS5o8774-TCiRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c740ca854.mp4?token=IzYze0teOdYi5mVF0IbE7z3KWujTe-qdZjE5KEZz7qJEErzD4Ry8-BAdgDqOtBSbmfbKYMP75Zi_gxKQwW44VA2IjvO6PgHNXtC1ZjrqxBKdOcpVGeGniTdJLK4A92d_6ZugvmPIqo7_tHK_xYqpAba4Z3r4cw2HB84kL18f_jyPlxrwon1fADoupFGFUm6G7iW0UTj-sXbyhO5eO4D8or4UOUhp5SjidJUBjiS__haNCC8_CP0ylpqd6kp5HNpVnDBEeDOlrSnLu9bT-hak5S4u8MFmYy_bXBm44DU-v9LfJYTKZ2r57InWbYEOcgqc57nZ7tY4CSq_TU3SH62i-rRmXwNQYJMWVM3RZVj1MCfywVhPZ-ZQXjUoQhO_PfmCQpMuJO-tNVRNNJbrppqn4TzyZkLi6dDL-HjxHm9xnuSFzQRVXpl6wiKySfF3RsrtgytwUWSfzZyR7GV38lqZ50kF1H88xCatGe5TeuENccqocJhR32AIy8Tza5Mj5RwVzc3Vo7TOhOOuthfGsMx0QS3ifO0U_w7bGpvEneKP7vvJ_oe1qPC4IyE3pVD2y5svt8VEBItIymHvDE1npkPM6hKV9sS7ND7hn0peU3xqc-Kkx7Vf4bpSdZp14Z08NGMb5e53fNSofBOFM5y1TB4YbVkKcccJHlS5o8774-TCiRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: تا اقدامات پنج گانه اعتمادساز آمریکا انجام نشود، مذاکره معنا ندارد
🔹
اتمام جنگ در تمام جبهه‌ها و تضمین عدم تکرار آن باید از طرف آمریکا اثبات شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/654068" target="_blank">📅 23:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjAVNPuNIJJIUsW9fpTnQ62_wHVjFAMb70jukTxOwUPDah9fCSXO-C1Uf_-WFtrU4UuG-t52vY3Q2sL44sXDUb_iOTJmduuMTty5lYUQ4XG_Jj3PL4u1UfPlc624jOILlPZWxJsAH4w8ntH_z8VU-sbUQUIzoObF-rUA6i6BTZa3pa82LgPlZnu9pEEuAKFnh06FfFQWJQQg1KGC40fhVbbqQEEq3BOELabBP8zO9WhThc95--Nxt65pTi2oq5I5mGABJtOd-43JhnAlwkX2Im9R6ilhJ2DGms5b08cv4l2vWjYlPugNh9WrJhF8ggKi3f5FjFKI8ZATP-6GcZ1jUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌وگوی وزرای امور خارجه روسیه و آمریکا درباره ایران
🔹
وزارت خارجه روسیه روز دوشنبه خبر داد که سرگئی لاوروف و مارکو روبیو در تماسی تلفنی درباره «ابتکارات دیپلماتیک برای غلبه بر بحران در تنگه هرمز» تبادل نظر کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/654067" target="_blank">📅 23:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
رئیس سابق سیا: آمریکا بعد از جنگ اخیر تمایلی به استفاده از پایگاه‌هایش در منطقه ندارد
🔹
دیوید پترائوس، رئیس اسبق سیا و فرمانده اسبق سنتکام در مصاحبه‌ای گفته که ایالات متحده آمریکا بعد از جنگ اخیر علیه ایران تمایل چندانی برای استفاده از پایگاه‌هایش در منطقه ندارد.
🔹
پترائوس گفت: «ما از دسترسی به بسیاری از پایگاه‌هایی که معمولاً در اختیار داشتیم، منع شدیم. البته حقیقت این است که خود ما هم حالا که دیده‌ایم ایرانی‌ها چه توانمندی‌هایی برای هدف قرار دادن این پایگاه‌ها دارند، دیگر تمایل چندانی به استفاده از آن‌ها نداریم. این تهدیدها بسیار فراتر از زمانی است که من فرمانده سنتکام (ستاد فرماندهی مرکزی آمریکا) بودم؛ یعنی بین سال‌های ۲۰۰۸ تا ۲۰۱۰.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/akhbarefori/654066" target="_blank">📅 23:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654065">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4bf824f0.mp4?token=D-kWHWkncTNDRnydjrk1uMu2vj6qdmJSp5Gt7AFYg-MWSyktH6W5bMAVYgWVl9RqixK_uHKpy5mIjbLs6f2USaZc4ZDFYEO4-ecI3S8yLlAhSd9qNAoPhfLEyssyVD0B0XhOpTwPQaWPrRIoI_s3hvZKk5pD0nk5WDDxWPKwycBEv_amjY5l2Gx6JyXvhIsA7h9gIPoFTu-ipoDbN34lPYWnqGohs5bhvaKXOczvZsw_YjPTX2c0Nu8Lf1UVdG-oPmlcZnZ1KK7xZ-UDMlqHpRR1sh9F4beDy10Cmu48l2isYXv_rw3UkCuxT6zudKDMxddgbzi3IHYNeNTNqwlBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4bf824f0.mp4?token=D-kWHWkncTNDRnydjrk1uMu2vj6qdmJSp5Gt7AFYg-MWSyktH6W5bMAVYgWVl9RqixK_uHKpy5mIjbLs6f2USaZc4ZDFYEO4-ecI3S8yLlAhSd9qNAoPhfLEyssyVD0B0XhOpTwPQaWPrRIoI_s3hvZKk5pD0nk5WDDxWPKwycBEv_amjY5l2Gx6JyXvhIsA7h9gIPoFTu-ipoDbN34lPYWnqGohs5bhvaKXOczvZsw_YjPTX2c0Nu8Lf1UVdG-oPmlcZnZ1KK7xZ-UDMlqHpRR1sh9F4beDy10Cmu48l2isYXv_rw3UkCuxT6zudKDMxddgbzi3IHYNeNTNqwlBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکایی‌ها هنوز درباره آزادسازی منابع بلوکه شده ایران هیچ اقدامی انجام نداده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/akhbarefori/654065" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654064">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
فوری
🔹
۵ پیش شرطی که ابتدا آمریکا باید انجام دهد
🔹
رئیس کمیسیون امنیت ملی خبر داد:
🔹
۱. خاتمه جنگ در همه جبهه‌ها؛ مخصوصا در لبنان؛
🔹
۲. محاصره دریایی آمریکا علیه ایران باید برچیده شود؛
🔹
۳. پذیرش حاکمیت ایران بر تنگه هرمز؛ اگر محاصره ایران برچیده شود، تردد کشتی‌های غیر نظامی برقرار خواهد شد؛
🔹
۴. تعلیق تحریم های ایران طی ۳۰ روز؛ از جمله تحریم نفت
🔹
۵. آزادسازی منابع بلوکه شده ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/654064" target="_blank">📅 22:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654063">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcea-dBwP0MCXTqeu6sF9XTOFjpxu-X8Z8o83pqXWPl7rsv2g-BFCsXAQ-1Cpq03TjU9TRJDfcW-B8381MCdHl_CaMMT3tKxT1M4IHzr-cFTKJIbk_ZbNXz0BfXu8_rypnuels96PmqCRb3Olqa8AqYqkZ1NRqp0zOc7SmSX-LqOXM-z7N2EBI8i3ONHyF5A7J8YhnP2FCEBWbzS7857Ys_wzw9L3saNmJJRIGGR6_DYsDycKg_zfRfZ25g-R9LRoGV5OR3QASfywzDVyqqNtjjSXklQjF2NUdc6BAtehRYSatqC5POT7TSeBfJC4K99lrMh6GCzswZ8wl4Z--arUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سلاح مرموز آمریکا و عربستان علیه ایران/ جنگ پهپادی تهران - ریاض آغاز می شود؟
🔹
اخیرا یک شرکت تسلیحاتی آمریکایی و یک شرکت سعودی شروع به احداث کارخانه ‌ای نزدیک ریاض برای تولید پهپادهای رزمی الگوبرداری‌شده از پهپاد شاهد ۱۳۶ ایران کرده اند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3217866</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/akhbarefori/654063" target="_blank">📅 22:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654062">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjyxlVQNYkHVXDYfviSS3aNS1auiIrgAaD5zr-FQKKKxOzobR3wA1lX0gV-rU9hhcsZPJrYRskKKil9t-GXPJ6YaqP_0R1_nFjgiOk57zHbv26KkYC3R-375qslzwxGVdK8yArU0dirNJvFZukv_KaHZ0FgZbde7pv_RfPYU7t-L8yXQfCS7v1_xuKQ25tDnB4jvUmeYEaTKI_vDbb7Qk9IFieVlIlCaooXFMJOAKKanXJN9jBT0vR9epELEjKMw7qyUHYMBrY_UrwH1TghkC3jFOg2Sa4wJK-MUThO7jJKtxHOtyKguFdVyWiv5fbh15mB74SvWT1alaj2jOXU6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطر فوری
🔹
قالیباف، پس از تمدید ریاست خود بر مجلس، در سفری فوری و از پیش اعلام نشده به همراه با عراقچی وزیر خارجه و همتی رئیس کل بانک مرکزی، راهی قطر شد. مقصد این سفر گمانه‌زنی‌های گسترده اما تأیید نشده‌ای را برانگیخته است. برخی رسانه‌ها محور گفتگوها را آزادسازی دارایی‌های بلوکه‌شده ایران می‌دانند. در مقابل، گروهی دیگر موضوعات راهبردی‌تری چون برنامه هسته‌ای و امنیت تنگه هرمز را هدف اصلی این سفر اعلام کرده‌اند. تا لحظه مخابره این خبر، هیچ منبع رسمی جزئیات را تأیید نکرده است.
🔹
هفتصدوپنجاه‌ونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/akhbarefori/654062" target="_blank">📅 22:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa05d72b98.mp4?token=o1P-ayWz0Dyc3GRkfN5NLnq7j4WC_eU-wUkW6YDuuK8a5Oy0Xnf-e0GTC9rxEDuS8E-pzL63rT9r7igYK90hDPtbHU9AjnFj6YAFmEDWHhEqb7cE4NVZMtJ0zK9KJpdmWcerq7lXqau-CD7O7FK2jKkpgtPMXD7WflJna4ges4UibZ0NvNH_KkK2_D_ZOrOiZl_5frGPPHGmWoDFhVQeMWaskV0JGfl07zH_rzYAzvfhldRzRpQusK9Mo2olLEydhQE1cQqHgV4imiBQ3JPvTfC0c1hj-4k2afqNuCZR88RGwYQqTNSz7y5HWlwDdLoNBuOs0nIMc8_xajSrTYSlyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa05d72b98.mp4?token=o1P-ayWz0Dyc3GRkfN5NLnq7j4WC_eU-wUkW6YDuuK8a5Oy0Xnf-e0GTC9rxEDuS8E-pzL63rT9r7igYK90hDPtbHU9AjnFj6YAFmEDWHhEqb7cE4NVZMtJ0zK9KJpdmWcerq7lXqau-CD7O7FK2jKkpgtPMXD7WflJna4ges4UibZ0NvNH_KkK2_D_ZOrOiZl_5frGPPHGmWoDFhVQeMWaskV0JGfl07zH_rzYAzvfhldRzRpQusK9Mo2olLEydhQE1cQqHgV4imiBQ3JPvTfC0c1hj-4k2afqNuCZR88RGwYQqTNSz7y5HWlwDdLoNBuOs0nIMc8_xajSrTYSlyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکا هفته دوم جنگ از طریق عاصم منیر اولین پیشنهادش را ارائه داد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/654061" target="_blank">📅 22:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654060">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmRWMfvPq0qhw1v0V88J_9nMEbhk26IQ-eb84JOAq3aDEfWJv61ZzOUwiNB1OYyAroBwfBIGDHvtGc6u_z-sbdZmGled1CCcOcgyZAs1MO5Y-IPRqjZ0r6nv9INU9woIzliAPdILxMxiDnqHeTawSBQM6oPjnYX08c392A-cQUKN4FcfaoDr1FpQxSLIN_FxphcECBjMn23iPfyMnTSSNmBnZGrHGhRCE7HawgNgeITX8vLdEJYzjaL7qYcN-bLSrmPVLo0WfnJZLQdzPnoU25DViHJH3TQT2Nym5Zla41u_O5rAr2OYKR--IOveLYJ5Oz5iaARPB034MVlcZCPmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همنوایی شورای همکاری با اسرائیل علیه حزب الله
🔹
شورای همکاری خلیج فارس امروز دوشنبه ادعاهایی علیه نعیم قاسم، دبیرکل «حزب‌الله» مطرح کرد و از اظهارات وی علیه حکام بحرین به شدت ابراز خشم کرد.
🔹
جاسم البدیوی دبیرکل این شورا،‌ اظهارات نعیم قاسم را «غیر مسئولانه» دانست و مدعی شد دبیرکل حزب‌الله در امور داخلی بحرین مداخله کرده است.
🔹
وی ضمن دفاع از سیاست سرکوبگرانه دولت بحرین در قبال مخالفان سیاست‌های آن، مدعی شد که این افراد علیه وطن خود مرتکب جرم شدند و برای ایران جاسوسی می‌کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/akhbarefori/654060" target="_blank">📅 22:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654059">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/654059" target="_blank">📅 22:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654058">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۲۰ فرودگاه به چرخه فعالیت برگشتند
اخوان، سخنگوی سازمان هواپیمایی کشوری، در
#گفتگو
با خبرفوری:
🔹
در حال حاضر، کارشناسان سازمان هواپیمایی کشوری، در حال ارزیابی شرایط و رفع محدودیت‌های موجود هستند تا زمینه بازگشایی فرودگاه‌ها با حداکثر ضریب ایمنی و امنیت فراهم شود.
🔹
تاکنون ۲۰ فرودگاه فعالیت خود را از سر گرفته‌اند.
🔹
روند بازگشایی سایر فرودگاه‌ها نیز به‌تدریج و پس از احراز کامل شرایط ایمنی، امنیتی و عملیاتی انجام خواهد شد.
🔹
همچنین فرودگاه تبریز به زودی بازگشایی می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/akhbarefori/654058" target="_blank">📅 22:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654057">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJSQULCyBprYoSZk3unkItlvkJ952Cw4R7GZ8IWR-IeAWvZN6jVDJmA8_2QHYJCgnC4z8UwFCs3mWyZOFbD60qxLtqaovirhx9LKwmucpPVpu_X7nOzjy0tdBinavkUe4BPSg6gpisBvGqsbekToyEGQo2E1CJBavXooKVrnKOSebcBTEgvc53X166uG52SyfCPtALe2D2UPv0sUZFVY-4Gl_IUzeBF4eGp40XPwXgKy7FC6BAZbvkMlHOYX56ohxbui1iUg5JWyjcSftqXBSuWzcIHyRe16g-ZwSGdlP62EkI2LBNushejWPW5uINvL0y-PSBDte1KQ3BKNQr2M3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس امور اطلاع رسانی دولت، ابلاغ رئیس جمهور برای اتصال اینترنت بین‌الملل را تایید کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/akhbarefori/654057" target="_blank">📅 22:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654056">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1913aef4a8.mp4?token=GJSgDYkLiAmFueAwGTCLStggKD2y58-awe4Yp5XuYVR4Wg_XQcNWVNam9vZxM2DENesIA87tH5lQUSnnzG8iZIoMiXnB-JZRPQfocajJjsg-eaL9a9Xgrg72JjmNszSpKEZzB0fFDU1x5hZkl_eS4SovIW5RaXbtO5fytBmt-8RAhy_qYlvyDDExJ31xy-6s4Sp1GKh3cyl-upC9V18eQ_O_tFNfTsdwXp2RZsK7phToRI0VHN4oQb49oV2-MhLPAGKzzfUptVWX1mYmrFEI5tsKAyFTwKY5FgwFG0Y0XHFMxCTXldA4YDNoBtA0Gj1LANKIWNUbLquK04YHzBtS8WyieWuk38UulcxIjnQ1_x3kZ6sPH3vjzyMODfN2TG_QjDA0ueRUiwT4krfBfGE1togWRLo5LgKf_V6gVQbCWQC_LypU9-A4RWaAcfBzzhB5gq8y0QeTOe3kSntx6sLY6QWfd0Y4s9uZQMC6sPqXSJar13mov_Q52JlI6ZMETCCP0924JLv4FCpmoimhVvjZrdVZxpwFJXhX7zditq_9Nw2V6fMzSmaoGD85lsZxzZJdUfnNQ_bnuxk0aPhyJXzjTB9NQpIflSoFX4gr9nhfc8HnM1aJNsVDLRenU5i9GDG9Iov67iT0xn7IZevwAo7IoP1lb_lUty-SbD9cJ4vOuhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1913aef4a8.mp4?token=GJSgDYkLiAmFueAwGTCLStggKD2y58-awe4Yp5XuYVR4Wg_XQcNWVNam9vZxM2DENesIA87tH5lQUSnnzG8iZIoMiXnB-JZRPQfocajJjsg-eaL9a9Xgrg72JjmNszSpKEZzB0fFDU1x5hZkl_eS4SovIW5RaXbtO5fytBmt-8RAhy_qYlvyDDExJ31xy-6s4Sp1GKh3cyl-upC9V18eQ_O_tFNfTsdwXp2RZsK7phToRI0VHN4oQb49oV2-MhLPAGKzzfUptVWX1mYmrFEI5tsKAyFTwKY5FgwFG0Y0XHFMxCTXldA4YDNoBtA0Gj1LANKIWNUbLquK04YHzBtS8WyieWuk38UulcxIjnQ1_x3kZ6sPH3vjzyMODfN2TG_QjDA0ueRUiwT4krfBfGE1togWRLo5LgKf_V6gVQbCWQC_LypU9-A4RWaAcfBzzhB5gq8y0QeTOe3kSntx6sLY6QWfd0Y4s9uZQMC6sPqXSJar13mov_Q52JlI6ZMETCCP0924JLv4FCpmoimhVvjZrdVZxpwFJXhX7zditq_9Nw2V6fMzSmaoGD85lsZxzZJdUfnNQ_bnuxk0aPhyJXzjTB9NQpIflSoFX4gr9nhfc8HnM1aJNsVDLRenU5i9GDG9Iov67iT0xn7IZevwAo7IoP1lb_lUty-SbD9cJ4vOuhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی «تنگه هرمز» اقتصاد جهان را به «وضعیت قرمز» می‌کشاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/654056" target="_blank">📅 22:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4HC5ZosdQrH_r2ENa3aN5j7f4cL1NNZ0SaamMTGMCik671OarpmniA5Bd8nT9UHQac62jMcv797tWUUIvKs8igz89uiSeOyGKebBckQc3zf1uAphrmQ5N4Ol3nM0I-cPFVwq_G3AGurL0L75uu0iaPj4gpF7F0yykwvwVnJkzb-NYpMpp9fdlKWN-vYmcCTUvuu_NrAbaDobLk654xsyNGrvshniGWgjyQ1gI3NRHBV8JQ15DL1SiJBo5Y7oVUhi4tDI366SHTJ3UbDcAkAz4wjq1-40CDI0LFpe7t6yd3XD6PrJqR12LETWqaGHZXyZjpqJTBXnJ9HxTTjV9vcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معادلات جدید حزب‌الله؛ آیا باید منتظر تغییر در غرب آسیا باشیم؟
🔹
جنبش حزب‌الله اخیرا دامنه عملیات‌های خود را گسترش داده و با پهپادهای انتحاری، تلفات بسیاری از صهیونیست‌ها می‌گیرد؛‌ همین مسئله باعث وحشت مسئولان اسرائیلی شده است.
🔹
«تحولات لبنان و مواضع ملی‌گرایانه و توأم با شجاعت مقاومت به رهبری حزب‌الله، بارزترین خلاصه‌ی مسیر ساخت خاورمیانه جدید، بازگرداندن کرامت به امت‌های عربی و اسلامی، و شکست پروژه استعماری آمریکایی-اسرائیلی است.»
🔹
«عبدالباری عطوان» تحلیلگر برجسته جهان عرب با اشاره به سخنرانی‌های اخیر نعیم قاسم دبیرکل حزب‌الله و نبیه بری رئیس پارلمان لبنان، نوشت،‌ این سخنرانی‌ها نشانگر یک تغییر مهم است که منطقه و امت اسلامی را از حالت تحقیر، ذلت و شکست کنونی خارج خواهد کرد و به تنها گزینه مؤثر، یعنی گزینه مقاومت در تمام اشکال و صور آن، و در رأس آن‌ مبارزه مسلحانه بازمی‌گرداند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/654055" target="_blank">📅 22:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
وبملت اثرگذارترین نماد در صعود شاخص بورس
🔹
بانک ملت با جابه جایی حجم بالایی از سهام به عنوان پرحجم ترین نماد بازار و ثبت خالص ورود ۳،۹۵۰ میلیارد ریال پول حقیقی، علاوه بر قرار گرفتن در صدر نمادهای پر معامله، با اثرگذاری مثبت ۵،۱۰۶ واحدی، بیشترین نقش را در صعود شاخص کل ایفا کرده است.
🔹
با توجه به رویکرد مثبت بازار از تحولات سیاسی، در نخستین روز بازگشایی بازار سرمایه پس از رفع محدودیت های معاملاتی دوران جنگ تحمیلی رمضان، نماد بانک ملت (وبملت) در پی برگزاری مجمع عمومی فوق العاده و تصویب افزایش سرمایه، بدون محدودیت نوسان قیمت به تالار شیشه ای بازگشت.
🔹
بر اساس این گزارش، بانک ملت با اجرایی کردن افزایش سرمایه ۴۲ درصدی از محل سود انباشته، سرمایه ثبت شده خود را از ۲۳۸ همت به ۳۳۸ همت افزایش داده است.
🔹
بر این اساس، در جریان معاملات چند روز گذشته بازار سرمایه، نماد "وبملت" با قیمت ۹۱۰ ریال به ازای هر سهم بازگشایی شد که حاکی از ۴.۷ درصدی نسبت به قیمت تئوریک بوده است، این روند صعودی با استقبال گسترده معامله گران تا پایان بازار تداوم یافت و قیمت پایانی سهم با ثبت رشد ۵.۲ درصدی نسبت به قیمت تئوریک، در سطح ۹۱۴ ریال تثبیت شد و تا قیمت ۱،۰۲۰ ریال ادامه داشته است.
🔹
اعتماد سهامداران به سهام بانک ملت به عنوان یکی از ارزنده ترین سهام بازار با سودآوری بالا و بالاترین تراز عملیاتی در بین بانک های فعال در بازار سرمایه، از جمله دلایل صف های سنگین برای خرید سهام این بانک بورسی عنوان شده است.</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/akhbarefori/654054" target="_blank">📅 22:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 57</div>
</div>
<a href="https://t.me/akhbarefori/654053" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌وهفتم
رائفی‌پور:
🔹
0:10:40 نماد برکت در یهودیت
🔹
0:20:30 بلاغت و فصاحت بسیار زیاد در کلام حضرت علی(ع)
🔹
0:33:00 هارون باعث سجده کردن و ایمان آوردن ساحرین شد
🔹
0:40:40 خطای تغییر صلوات توسط اهل سنت
🔹
0:48:40 چرا هارون حضرت موسی را برادر خطاب نمی کرد
🔹
0:57:00 خواب شنیدنی فاطمه بنت اسد و تعبیر آن
🔹
1:03:45 منظور از الم نشرح... چه کسی است
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/akhbarefori/654053" target="_blank">📅 22:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5093129d.mp4?token=hCBik05zJHPZlgcdaY9J8sm3mje-fsKWhrMufeqM38BGZW7WTZG69kS7qJe9V8tMOskhS_AEWriN1K8x2Xpj0XCMvRhUBoCHBzjYw6_CUJczc4cWaXSvy1PG8ldSrwQrZYVVzQV7KM4vM3nzCrUw1sVwqpfbWOs9ojJ5pmW5o1M09_Eslp0uCX2ntYbuKzkcBr9rVmT_KT1_y2dVctW-4gnUwj1G2XNW6wDHe1KQh8s16oBBmApWNJCW0eD9O49Gr-OH-NwxCvml-cfQoyXkfHHgLyN9VmPTPYsnD3AGIABsmcEOXv8RxelPwpRVZIDy92YT9yz1oQU2UK5vAhu7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5093129d.mp4?token=hCBik05zJHPZlgcdaY9J8sm3mje-fsKWhrMufeqM38BGZW7WTZG69kS7qJe9V8tMOskhS_AEWriN1K8x2Xpj0XCMvRhUBoCHBzjYw6_CUJczc4cWaXSvy1PG8ldSrwQrZYVVzQV7KM4vM3nzCrUw1sVwqpfbWOs9ojJ5pmW5o1M09_Eslp0uCX2ntYbuKzkcBr9rVmT_KT1_y2dVctW-4gnUwj1G2XNW6wDHe1KQh8s16oBBmApWNJCW0eD9O49Gr-OH-NwxCvml-cfQoyXkfHHgLyN9VmPTPYsnD3AGIABsmcEOXv8RxelPwpRVZIDy92YT9yz1oQU2UK5vAhu7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در جنگ گذشته مقاماتی که در پناهگاه زیرزمینی بودند با وجود حملات سنگین آسیبی ندیدند
🔹
حتی برای ترور برخی مقامات ۲۸ بمب سنگرشکن به مکان مورد نظر زدند اما اتفاق خاصی نیفتاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/akhbarefori/654052" target="_blank">📅 22:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WO1cTwignQyaqfDUsg77CeWShUKcoGXWyiRB8UK12xmLxSUVaqPSCMf6A66fOe2G09Eo_erFaCqvhnls-GkzV2dvKAcCUTDk5AI3X0-S8wwKXeFicVWCMQprp1dQRDOG_D1FeNUWrsWCvcoAUEwiuv_mlEXmMPt77fJnxisnT8RMeZkRabBArtrO8MqfCjj8vDkQtvxgWLqGiBESR4eyjWsj0kdz8ZzQuw7noEjPYk9rlYw3A-2rw1j2K-6rBIRz0RBePs4PevfeWWb8JzQBoGx21cUdQTxlTufG_e_86AtynJQRzrL_Yjp1RTRq5_MdkgI7UlkvQY-b0tHy7V_Pxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1S-WaMhwa9pYWoNZkoUpV0r5UA-4sF48Imc4YImKszX8j_QIYlrL56WeDUy8MTrIki_kdQKGAlkacpEdv1xwt4hCZ69U66Su3Y6RB7Kv3rVydA0g60NhgMSnebvMoS9grbgNqfmHiIMJzr1NA89aC5OB2ZXJV7e8Vemz5M_kopXQ-lnxf54Of1j2I5QOOfZ9owrJkOHyghTTQ-_-OwHsybrF_fVKlW2kSxRejey48hnuMvsl8MmVcRBkKKsXgexe3rz1LWxeMbb1nkIEhwbziD7wSulMisGxGx_mRWYexbmUlB4YdoztvajOP9IIPzOoyC8D_38aP1y5BBVF6Z-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUS9WV2BZAtluD2A8p8uHfjhy6uwT1ezcD3XH9F8qFcgoGW548kCdfQMxe1VY_71g0zC9Z7OlFH_MqNP24uT-7AvNaAyNfYp8pOzRy74Kr2OXNQY-772TlJbCZ-Ubx1xeyk4kg67vX9f1W_2TRSm5QbozIPB9I3WQrqLhWoi1e_lf1vD33FS9-xfhIJQnV4CAxjYHiaeKqCx3QU9n3M69g7d2sEkdgLMNwfMk3IYgSg40rXVDPvWXkJ019mjKpuD6lLeGLn-7l3B68LjnKmZ125I9pYNJ1VfrzATOlDRrsZSXJgt8ZFGJuh1Ty5SdFBEpF1vkBaKm1ZmpqVy9aHLag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GvnDP-VLS9VgzhF2YAdB132TKJN4CPk70Efd5BnTfh-ugjo4vah4uR4O7GiXRBYhrLsNAJA8HTOBYcV_62DvV-CahrrArG7Nv0vlDtu7g65YaX-qKcs42bME3dFwVewgx_mEmnuoXMjZ2zPEX1yyrifYvRgqwyEfBJnoM2bPofmunOsc2vlDFPvpOSmx_ssyqPB7e4Bfv3ZIiUg_ErZxy38IF5VSmp8qPxmFZFjeuOrdZPySmNKN6II0OdU5TcfLxfQ5HhHa50Rf2vX3_0-7J4WrVa0JJtCJpwcmOoGDmr7DosI4RVFTkfssUDtNnD2nWpM3jZjyKt2m6eMre0Y3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcKaGzTZpSUwLXyuApt12K6OGuaimKvLImLqNlfLcrMkSAuWckraRM0lef8IkrMX53JDMAJUjQxL_MZ9vrOWaW1XEtgTzkQwvYZH5C-YjrdnJ1ju8ZrTQNGQKHG65HJDn8LDVGD0_qi_cBy9P2Cwrx_KhT69-c3AhCCeEB2htGt5_gbf25rrtKnmB3B9tpJBKjYL04czn5WgmJLpgpibdOLgmFptycMJS0jvSuZqc-ZXgz2RVmu46ILRJqPlwhUHNfCJU6NwBfwDrezAGVdnv2G9AT6QJqH7t-epIm-gdiSUgFZljjC4goJ_NBqE8h33oAKEBxKMyzfbpjqrxJa-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaRcr-uDZvUqOaQvvtR6gDpntJc3RXd-btHf_9hkpJy0-wzGPw5ZPwP1UoEoD_5jIBJa0Wzqh2VL6E5hLZGP9mvOygCPKONANcM0N2wXdERemEDuDfsBWWOwuGrDJqTg46Z500bZj2ajUc24GdSkwAFwGwfCrIIX8i8RNq8q9NWZ0x-78RKnkCldlKp2nzo9w0uQ_4Su0WC3SFR6sJ2EUIauYN8F5_FCnOUvL2FzaWZ_-yLrcuNWoK5--YNem4jL51ptf8AhERFexU-N3UoLs4rH2IazpKs7xcaSrzknFuG7nF0NVRk2SWiE_v6xkVBrt2n1kBAnm22-GvYNoDamBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8dq68G_3BxPhP8x76oDZHvqk-Jstv9ta9VqrlG7BOLt1r4pHW80PuK7haKYi4ahWjn5yohGbo-jgIkad6I8PHT94pl3w14aSqrqvC9lC0h5UK1M0ulbrjNS0MKqvUEviC3mYhiTiAFT0Mc_IRxGd5zLuARlz1KrO3tJbvH_81fAkC0dKxHtVgvVWvPwgrt5BASJco3wdl1JQbrZFp0W0SLy0e0nskimRMvoGLycTM3jmSxKs8bm1hbI9kSyo7csCkOZP9yXdQPwKq4e4Z8Gbwu3254Rbqsa_hEBx3cXNyBnkJLEM7SxX52qjIDLUyHHjRSNeYEwB8j5v3BrNjSu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-6-AykO_JJ8JdW1RJnJ1_VLXDJRm373dbSvt4mR6Ya3nu75eFCzRikpCan3ZPchig54T9NHHuN5uQMoJOvkzSiBfMtLN5TUX5mm_x6c3CvDbnjmP6Y_UGIY7H_BAbbncoy23yWhmxhrlXxlewGIyyV-qnln8A7_LLWqcZ1rTC24SWc9Qni_Hib65vg1c_9zb-O-a3WyUzGDEcJVDgAzfPC7AjUX5lWErXzSe00c9H3BHFRvmT2kxLR0USkUZrlc4Wq1T_Y4gb0zlZPsKk30YmKsTzqe7VEDKpBdqv-JhkoCVMtdkjzuTFHdSFE9uZBSuwrSTR5edv8U7g33M7Q22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LW7ApeF6TBgayyNLPJNA85VqVT6z0U8TQN0UkgiKPvWLyiHAmYKcOoYxBBS4QeMtmuU4MYzjxFDD_0sQHEQPZdVdUXMCthDktLb31rMFvyw8lLSXTgAl_sYQM_y9c7qZ8BV64amY14u7Ln5mELjTAi5K-cb85tDyckG6mhp2GazNSo3CfeAUKa2r-sV6-AlkTXYApHJQpDxDXBiNdBSj9PCbcYP8vdpHIVwyMCzsNUgBSnwcmySsap-ZUCVOfSxXoEivyWF2ycmHzbMQ_kjvthkVkm1iV_npbqXVvhsPTtw0pVHyT19aydwUxccoyeCAU6RNq7FP_EqPLR-pwwFCtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت همدلیِ واقعی
💫
✨
#همدلی
اینجا یک شعار نیست… یک جریان واقعی است.
#هیات_قرار
با همراهی شما مردم عزیز، ۳ رأس گوسفند را قربانی کرده و گوشت آن را  در راستای حمایت از خانواده‌های ایرانی میان خانواده‌های حائز صلاحیت توزیع می‌کند.
این جریان، با شما زنده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/654043" target="_blank">📅 21:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654042">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
گستاخی روزنامه صهیونیست: هیچ تکه کاغذی نمی‌تواند اسرائیل را از حمله به ایران در صورت عبور از خطوط قرمز باز دارد
روزنامه صهیونیستی جورزالم‌پست:
🔹
آنچه ممکن است بیشترین شانس را برای بازدارندگی ایران داشته باشد، احتمالاً هیچ تکه کاغذی (توافقی) نیست. حقیقت تغییرناپذیر این است که اسرائیل آمادگی و تمایل خود را برای حمله سه باره نشان داده است.
🔹
اسرائیل اکنون به وضوح به ایران و منطقه پیام داده که برای جلوگیری از بازسازی تهدید موشکی، حتی به قیمت حملات مکرر در مقیاس بزرگ به خاک ایران، هر کاری انجام خواهد داد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/akhbarefori/654042" target="_blank">📅 21:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654041">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79a8fcba2f.mp4?token=B64rptrlPd4hE8azgT4m8LOqsnKOUeOlj9bU2irAKtWqbwjB21NKIKiR1MSYWvlgVQfzZfLnPA2bFDplYbMQFN3BFFD4o7xMyy1GARBog36m-ILhUThboFtNGK0qLIEf_-rKlKx0YyS3pdHlft30MhvC1_SgWD3ar-C62UVYpeYtibMvohZv1JkGHSB1QXnnEWDNI6AVd2rKy89Bkg4UCATZ1NK2bnNWLWOvUDjVWs7l59jc1TIK2nRcTvbHhBbMe4er93sUKJf1rBHM7BHbLVMlMAFhuis0xfUSGYhl8aJuxDlPfo2_r1-FzSk9OokENG5MxySXuqiw0som7qWwLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79a8fcba2f.mp4?token=B64rptrlPd4hE8azgT4m8LOqsnKOUeOlj9bU2irAKtWqbwjB21NKIKiR1MSYWvlgVQfzZfLnPA2bFDplYbMQFN3BFFD4o7xMyy1GARBog36m-ILhUThboFtNGK0qLIEf_-rKlKx0YyS3pdHlft30MhvC1_SgWD3ar-C62UVYpeYtibMvohZv1JkGHSB1QXnnEWDNI6AVd2rKy89Bkg4UCATZ1NK2bnNWLWOvUDjVWs7l59jc1TIK2nRcTvbHhBbMe4er93sUKJf1rBHM7BHbLVMlMAFhuis0xfUSGYhl8aJuxDlPfo2_r1-FzSk9OokENG5MxySXuqiw0som7qWwLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ایران تصمیم به پاسخ به تجاوز آمریکایی‌ها بگیرد و جنگ را فرامطقه‌ای کند کدام نقاط زیر ضرب نیروهای مسلح ایران و مقاومت خواهد رفت؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/akhbarefori/654041" target="_blank">📅 21:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654040">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چراغ سبز مجلس برای حضور سردار آزمون در جام جهانی
عباس صوفی، نایب رییس فراکسیون ورزش مجلس در
#گفتگو
با خبرفوری:
🔹
دعوت سردار آزمون باید نظر کادر فنی باشد و در حوزه فنی نمی‌توانیم نظر دهیم و قطعا نظر قلعه‌نویی موثر است.
🔹
سرمایه‌های ملی را باید حفظ کنیم و ممکن است فردی زمانی اشتباهی کرده باشد و بخواهد الان جبران کند. پست خیلی خوبی سردار آزمون گذاشته بود و ابراز اعتقاد به ایران کرده بود و انشالله بتوانیم با نگاه اغماضی، سرمایه‌های کشور را دور هم جمع کنیم.
🔹
آزمون در صورتی که واقعا ابراز ندامت کند و به لحاظ فنی، مورد تایید کادر فنی باشد، می‌تواند به تیم ملی برگردد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/akhbarefori/654040" target="_blank">📅 21:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654039">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21453ebbc9.mp4?token=EAeZZEA18xiZeWUPgyooxLakr_J3hYCJOP2BjFmbAxKzO_BhFxHoZ-VUPoNbHf1Cruivtk0V7N2CO_lxk859eDC1mHfUsAnISs6ShOkK68-b36y39JuWM_pgZFweIkjisoqEvnyObJtgrXBVmjHVSHJB7uGJc0mzV5G_a9wBPyR4vSHGQaHp5RrQYyopvReUFkUyq1x-Llljz1kMzprDvyX6CtAJeX14BDBjnWLeKTnNKma7Evgtz-XDDuaIazmay8hmfdjioJBRzsWAOChik0n44IXoLLJB_goxgbnAxCmiRV9l53SOsnlxpD27y4KL5GtuU5reM8gst8Sg3pKrUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21453ebbc9.mp4?token=EAeZZEA18xiZeWUPgyooxLakr_J3hYCJOP2BjFmbAxKzO_BhFxHoZ-VUPoNbHf1Cruivtk0V7N2CO_lxk859eDC1mHfUsAnISs6ShOkK68-b36y39JuWM_pgZFweIkjisoqEvnyObJtgrXBVmjHVSHJB7uGJc0mzV5G_a9wBPyR4vSHGQaHp5RrQYyopvReUFkUyq1x-Llljz1kMzprDvyX6CtAJeX14BDBjnWLeKTnNKma7Evgtz-XDDuaIazmay8hmfdjioJBRzsWAOChik0n44IXoLLJB_goxgbnAxCmiRV9l53SOsnlxpD27y4KL5GtuU5reM8gst8Sg3pKrUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: اگر ارز را در زمینه کالاهای اساسی اصلاح نمی‌کردیم، مطمئن باشید که الان با قحطی مواجه می‌شدیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/654039" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654038">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مدیر روابط‌عمومی وزارت ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/654038" target="_blank">📅 21:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654036">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96a26c75c6.mp4?token=kJv7TKEuhYGw3_6KJyD4hNuJIrRT02fONa4g4M6vUNzAGD1tVduSyBhbmcJEPOYKkIppeXu8H5vxLwRFPG_bnWYDjt6DKZu8tKO5uR-kRQzR-KHuQkVXKC5E_yrLyZOIUfAcH-U5vS731ibLM3KbSjr2h57JZ0xJQROHjR_SDL5rk2igujwseyqDJz7GDYipANpQ-90PEezfJ1TqDrXWoDCaHUyjNxKxFvIJeRAfOdT058nKLUfERHSnS2TjF_Psn31ooaLDOGneXmrwXWe91c7-MZuQ8lI4CjHSGhMJ5e-9S2gtdYq-ZUMYZT8obMSoUM-08e6bpw3q2trDxAmuDrWXq2IF7bx9H6dLypn0Q9ZYEp5xFGzi-GnzA5bAXIeoXtLfMPmlcedLDOW7AHo0nJfS8CCM5WYdleU0AF5Z-JgzzNKdZVP76y95VHQozoVbG7TnK8I5-VoDhRl30RR5dq9G8tZ9d7IVEB6aJkfrj0GSMJyfT9zO7ImYgCVBXcwDtcoIDcb0acWO8GaEffTl85Dbmhxz1TZCSHoO0lubhk9hO3m73HMFmYEQeIuL9CXW-N7DuRv8g18O3fP-hrEUpvf5pYTXDYKD6LltJmGcpmpmcVDiIojI2P1_UI-4qj9DYd_ctDyAZoXDsXCZzevd23y45Lw_8HKu8g8q7U5d-Q4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96a26c75c6.mp4?token=kJv7TKEuhYGw3_6KJyD4hNuJIrRT02fONa4g4M6vUNzAGD1tVduSyBhbmcJEPOYKkIppeXu8H5vxLwRFPG_bnWYDjt6DKZu8tKO5uR-kRQzR-KHuQkVXKC5E_yrLyZOIUfAcH-U5vS731ibLM3KbSjr2h57JZ0xJQROHjR_SDL5rk2igujwseyqDJz7GDYipANpQ-90PEezfJ1TqDrXWoDCaHUyjNxKxFvIJeRAfOdT058nKLUfERHSnS2TjF_Psn31ooaLDOGneXmrwXWe91c7-MZuQ8lI4CjHSGhMJ5e-9S2gtdYq-ZUMYZT8obMSoUM-08e6bpw3q2trDxAmuDrWXq2IF7bx9H6dLypn0Q9ZYEp5xFGzi-GnzA5bAXIeoXtLfMPmlcedLDOW7AHo0nJfS8CCM5WYdleU0AF5Z-JgzzNKdZVP76y95VHQozoVbG7TnK8I5-VoDhRl30RR5dq9G8tZ9d7IVEB6aJkfrj0GSMJyfT9zO7ImYgCVBXcwDtcoIDcb0acWO8GaEffTl85Dbmhxz1TZCSHoO0lubhk9hO3m73HMFmYEQeIuL9CXW-N7DuRv8g18O3fP-hrEUpvf5pYTXDYKD6LltJmGcpmpmcVDiIojI2P1_UI-4qj9DYd_ctDyAZoXDsXCZzevd23y45Lw_8HKu8g8q7U5d-Q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش ترامپ برای کوچک‌نمایی آمار تلفات آمریکا در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا مدعی شد که در دو جنگ اخیر (علیه ایران و ونزوئلا) ایالات متحده آمریکا مجموعا ۱۳ نظامی از دست داده است.
🔹
این در حالی است که پایگاه اینترسپت چندی پیش در گزارشی افشا کرد که پنتاگون آمار تلفات و خسارت‌های آمریکا را پنهان کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/akhbarefori/654036" target="_blank">📅 21:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654035">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a81erOeAi7uU3it88g6SXjJHof4NhbAeKe3-2M7a_H7FrSaEag8SMw6nHzrzVKapc0CmEQVbrJ98fNGPqNgDK7lUHSdwhv9TuQNxraCmMZkIjJelRF6okw7R5oRLkq_Yx_Jel9N6HH3by2iJulZqegLcjHM1F2Bg_aP1cIIQW6R9V3yX2kRZ09WRHMA9jBSa3aJCscD8OUW_IJXftY-dxOPTx61AApzPL93YbYKNl6cg8pypvkgg7sfUXuxIXaft_irFtFonjRVse_lGlWVzrHXj3-aQyljcj-Zk68UYdTx_xSB6PuFGyxvh7DdG2HE_SHpHuuS5iIVzN-ncNoFiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا استفاده از کتاب‌های فیزیکی در مسیر حذف است؟
🔹
در این نظرسنجی بیش از ۲۴ هزار نفر شرکت کردند که سهم بله ۳۷٪، سهم روبیکا حدود ۶۱٪ و تلگرام ۲٪ بوده است.
🔹
در کل به دلیل افزایش قیمت کتاب، حدود ۸۵٪ خرید کتاب فیزیکی را کمتر کرده‌اند.
🔹
همچنین حدود ۵۰٪ به جای خرید فیزیکی کتاب از راه‌های دیگری به خواندن کتاب مشغول شده‌اند.
🔹
سهم افرادی که افزایش قیمت باعث شده به طور کلی میزان مطالعه‌شان کاهش پیدا کند حدود ۳۴٪ است.
@amarfact</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/654035" target="_blank">📅 21:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654034">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اسرائیل به دنبال گسترش عملیات نظامی در لبنان
🔹
شبکه ۱۴ اسرائیل اعلام کرد که نتانیاهو و کاتز( وزیر جنگ رژیم صهیونیستی) درباره گسترش چشمگیر عملیات در لبنان و تایید حملات علیه ساختمان‌ها و منازل مسکونی گفت‌وگو کردند.
🔹
این رسانه عبری تصریح کرد که اسرائیل در خصوص گسترش عملیات نظامی در لبنان با آمریکا در حال رایزنی است.
🔹
طرح صهیونیست‌ها برای گسترش عملیات نظامی پس از آن انجام می‌شود که حزب‌الله به خصوص با کوادکوپترهای انفجاری خود تلفات و خسارات سنگینی به ارتش رژیم وارد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/654034" target="_blank">📅 21:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654033">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDhddHwaM33l387OFYAtEDn11KzzqjuE4l5Alh_JhW5pX2CQARbn6OjjIpAiFjpy-aD8_eJqRZouPqH9Fuct0u4ORa03qIsjWuBPKb-IQGzYJ4Q0sTU1DWxJp70hzckj36rZJITpnGHWikB7wJmZn6CMmS_vp0krh0228fp_L9eUBY3U8MArUwuo_Pz-e3I9ElBah9C339jB3YxmDe62MYYoeHtNFpBkMGJRrrXgjoOsZR9px9H7_N9_VniMRUsdc8LySFpj2PyCeqOYiBc6qlmOpYlCxDcVtDnVFiG9l4KP2pCfDOjNBMGdrvRUqTteQ_r4orNRuU0hIOx_xq1Lgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکن در دهه اخیر سالی ۴۲ درصد گران‌تر شد
🔹
قیمت هر متر مربع خانه که در سال ۱۳۹۵ در تهران حدود ۴ میلیون و ۴۰۰ هزار تومان بود، حالا در اردیبهشت ۱۴۰۵ به میانگین ۱۸۰ میلیون تومان رسیده است.
🔹
نرخ رشد اسمی متوسط سالانه از سال ۱۳۹۶ تا ۱۴۰۴ معادل ۴۲ درصد بوده است؛ یعنی هر سال، قیمت خانه به طور میانگین نزدیک به نصف بیشتر گران‌تر شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/akhbarefori/654033" target="_blank">📅 21:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654032">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گفت و گوى مژده لواسانى با خانواده‌هاى «مردان ناو دنا» در بندرعباس
همسر شهيد ناو دنا: اولين فرزندمان سه ماه ديگر به دنيا مى آيد / اسمش را پدرش در ناو دنا انتخاب كرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/akhbarefori/654032" target="_blank">📅 21:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654031">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
یک منبع در وزارت ارتباطات: مصوبه بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴، دقایقی پیش از سوی رئیس‌جمهور به وزارت ارتباطات ابلاغ شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/akhbarefori/654031" target="_blank">📅 20:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654030">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2FxhmxrDF-Wv9zrPt8F_kEB2oZjPFUvzMlWeujECnsZVpk6jff0LUx8fRzp16ijHemRP5jrEF8jmz4k3ZpIAem4WIOT6TBa6_RhMhG5lxKb1nCFuOC9dNK4smMgCbEgHwX2wtwhtHYh7JKMI0eutVYJCU2ADu4stdYzbAd8dDcDI8AK8jHc63X8553PP60_r3accGoox2SZLJscgN5T-wvikWZHTcGXSXszR1iRPEbC7w_JJZOLxg7Lcc0i5wJPgcpekFfArLb02YJGj-2vMAw-eZdhFbrTUUSnYG8wFbGBCprLyzP1ZqKyRW6NOF_l914_DaH_tOeZpbG-UsEmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه اصناف از اینترنت پایدار در روزهای بحران
🔹
قطع اینترنت بین‌الملل، ارتباط بسیاری از اتحادیه‌های صنفی با اعضایشان را مختل کرد؛ ارتباطی که پیش از این عمدتاً از طریق پیام‌رسان‌ها و کانال‌های تلگرامی انجام می‌شد. در این شرایط، اینترنت پرو به ابزاری برای حفظ ارتباط پایدار میان اتحادیه‌ها، اصناف و اعضا تبدیل شد.
🔹
اینترنت پایدار، علاوه بر تسهیل ارسال اطلاعیه‌ها و دستورالعمل‌ها، امکان برگزاری جلسات آنلاین، آموزش‌های تخصصی و دریافت سریع بازخورد اعضا را فراهم کرد. فعالان صنفی می‌گویند تجربه هفته‌های اخیر نشان داده دسترسی به اینترنت باکیفیت، دیگر فقط یک نیاز فنی نیست؛ بلکه بخش
ی از زیرساخت ارتباطی و عملیاتی اتحادیه‌ها و کسب‌وکارها محسوب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/akhbarefori/654030" target="_blank">📅 20:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654029">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b41a3263.mp4?token=Jtq8EFhVN_YDj31xBnZFZy3bTcDDQk1M0H6Q0OfvnmPfDlLIBMfV_bcwiLKjHPJ0CKRw9P9O_H_8KWQiDNvsWntuzERNBwGznCOgBzY0BDxbG67iQbCJyWm1flIz_FncBPiMrg6hQztfpzNaIj60hQv9l7FIB_Ti7o8UhALLG_vM8sfxcVvMfipTZVkox7AeLoC65GFJx5mUdPnTo0K8g2d2jh3mDoAPX8Q8oVZmsh9o39n_F7Dyz_WaIsy-nKoCfGCH9GXZJDRXqbk7XFNQ_dn6exaQPIwX1I5DcDmMDUMJMBqU3V7YGqASujvkYWnOMyHOFUYMzZZmuXORAYaXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b41a3263.mp4?token=Jtq8EFhVN_YDj31xBnZFZy3bTcDDQk1M0H6Q0OfvnmPfDlLIBMfV_bcwiLKjHPJ0CKRw9P9O_H_8KWQiDNvsWntuzERNBwGznCOgBzY0BDxbG67iQbCJyWm1flIz_FncBPiMrg6hQztfpzNaIj60hQv9l7FIB_Ti7o8UhALLG_vM8sfxcVvMfipTZVkox7AeLoC65GFJx5mUdPnTo0K8g2d2jh3mDoAPX8Q8oVZmsh9o39n_F7Dyz_WaIsy-nKoCfGCH9GXZJDRXqbk7XFNQ_dn6exaQPIwX1I5DcDmMDUMJMBqU3V7YGqASujvkYWnOMyHOFUYMzZZmuXORAYaXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباس اکبری تروریست: مسلح به کلت بودم و شلیک کردم
🔹
او که در کودتای دی‌ماه ۱۴۰۴ با به ناامنی کشیدن خیابان‌ها به سمت اماکن نظامی و انتظامی اسلحه کشید و تیراندازی کرد صبح امروز به جرم محاربه و اقدام علیه امنیت ملی اعدام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/akhbarefori/654029" target="_blank">📅 20:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654028">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
لانه عنکبوت اقتصاد ایران
🔹
یک سوم واردات ایران در گرو یک بندر جنوبی در امارات است. ۵۳ درصد صادرات ایران به امارات، سوخت خام. ۱۶ درصد واردات از امارات، ماشین‌آلات صنعتی. این یعنی خط تولید ما دست آنهاست.
🔹
تغییر مسیر یا ماندن در نقطه خطر؟ ویدیو را ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/654028" target="_blank">📅 20:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654027">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c723e189ec.mp4?token=j0HqQ_75-iclDTY_IV_ulqXhjpF9yCFOE2HIWBkfe9s4lskP3I67AN8a90ff7T4hEeoVYJ-NtcoTVi2hH0B9M5XT4s1T7ZwPmKkXunvNPb-d3x-92Zxp4znH2RsEAHzYCsNxCzoB084P0J2R99iaS8Ulvd9Tjbefqt_5nQKOuDM1HTUek_3udmMa3rMHiyTwbmHzt4ipiTWvjtI92etv1U2YLWCZRRYf0Hru-l9vJCHfWC8e-RfkUiRKjm5cjFClE4gsN2v2Pkmoq38nouTWo0haW_03RgCX7sEzNHxYmJ-282SPUYsdSTETWU2TicLZqK8_bHTytEI9w5HS0AnJ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c723e189ec.mp4?token=j0HqQ_75-iclDTY_IV_ulqXhjpF9yCFOE2HIWBkfe9s4lskP3I67AN8a90ff7T4hEeoVYJ-NtcoTVi2hH0B9M5XT4s1T7ZwPmKkXunvNPb-d3x-92Zxp4znH2RsEAHzYCsNxCzoB084P0J2R99iaS8Ulvd9Tjbefqt_5nQKOuDM1HTUek_3udmMa3rMHiyTwbmHzt4ipiTWvjtI92etv1U2YLWCZRRYf0Hru-l9vJCHfWC8e-RfkUiRKjm5cjFClE4gsN2v2Pkmoq38nouTWo0haW_03RgCX7sEzNHxYmJ-282SPUYsdSTETWU2TicLZqK8_bHTytEI9w5HS0AnJ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان مرشایمر: حمله به ایران بزرگ‌ترین اشتباه تاریخ سیاست خارجی آمریکا است
🔹
نظریه‌پرداز برجسته روابط بین‌الملل و استاد دانشگاه شیکاگو: تصمیم به حمله به ایران در ۲۸ فوریه، بسیار فراتر از جنگ ۲۰۰۳ عراق، به عنوان بزرگ‌ترین خطای تاریخ سیاست خارجی ایالات متحده ثبت خواهد شد.
🔹
این اقدام جنگ‌طلبانه، فاجعه‌بارترین اشتباه استراتژیک واشنگتن در عرصه جهانی است.
🔹
پیامدهای ویرانگر این تصمیم، آسیب‌های جبران‌ناپذیری به نفوذ و جایگاه بین‌المللی آمریکا وارد خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/654027" target="_blank">📅 20:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654025">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
زخمی شدن ۶ نظامی صهیونیست در حملات امروز حزب‌الله
🔹
رسانه‌های صهیونیستی از زخمی شدن دست‌کم ۶ نظامی ارتش رژیم صهیونیستی با جراحت‌های خطرناک در اثر اصابت پهپاد حزب‌الله خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/654025" target="_blank">📅 20:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654024">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHcwnqrOd6-yhrPpoh76A-7UFir7LF56YRFSVA60Gok2g79_fznvvsaICWMAR_sV8zctdKxMt_0Kf8zesrUybWEva9Trqi8y86dre-VfPKFJd0miSqnfuFI1NFrGYaaXhHLuF5-yuPLmmTjTw0Qdmj-ntR8OWrpNWosS9kK4m0ZFWSmnbomy13B0CPjnI2AFa4IhtK1EWcf7z-GhtNPbCxxERrjQQrE6OLIW2BHL9kunVN0N6MdDjwYCc8g7B9udHPKn2N3Jv9VcLAkj6DVsIIeCpaSI798sboOEirevdEWkg3lrlBunBsz-aGxuYZKgFAqRuCK0Ha8fRGRrHWYWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیغام عاصم منیر به چین؛ توافق ایران و آمریکا نزدیک است
خبرگزاری آناتولی:
🔹
همزمان با تشدید تلاش‌های میانجیگرانه اسلام‌آباد بین تهران و واشنگتن، فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، روز دوشنبه به وانگ یی، وزیر امور خارجه چین، گفت که توافق آمریکا و ایران «در شرف دستیابی است».
🔹
منیر، وانگ را در جریان آخرین تحولات در نقش پاکستان در مذاکرات با هدف کاهش تنش‌ها بین ایران و آمریکا قرار داد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/654024" target="_blank">📅 20:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
کابوس شبانه جدید برای صهیونیست‌ها
🔹
با تجهیز FPVهای حزب‌الله به دوربین‌های حرارتی، در حمله صورت گرفته، یک سرباز صهیونیست با موفقیت هدف قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/akhbarefori/654023" target="_blank">📅 20:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOMxEBTvBDHJRSlmzQkckBZIKumTq1I23nTa62zpd-W4ya_boOB4mwFsOGlEcqHGQTZisUkhLi91lIvo301gBKobw7FfoSLnx340sBEcNpInvEM-jV7PkfSA9cbG_G-_NHxGORgTs7BM3OpeOMbWTfHTjYaGVVP4z4wUlVmW7mffemY50TrAW7QQmXdGhF-f8cvW7RkissnSYz3F0P-WjY453BXOpBbWcTpLHOZgm5dcV2-EwI01QQbMWKCFH6G6Um2P95P95ldQVWKJ72NfpPRcq39gvjQbqd7qmRVe_crUKMyhbs36ij3JMcemQXhreChwUc6hICZXf93ueuuVFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجله آتلانتیک: جنگ ترامپ لنگ‌لنگان به شکستی ناخوشایند نزدیک می‌شود
🔹
جنگ ترامپ با ایران به خاطر فقدان یک راهبرد مشخص و هماهنگ، در حال فروپاشی و حرکت به سوی شکستی خفت‌بار است.
🔹
کار به جایی رسیده که حتی نزدیک‌ترین متحدان و حامیان سیاسی ترامپ نیز از پیامدهای اقتصادی و نظامی آن ابراز وحشت کرده‌اند.
🔹
این وضعیت منعکس‌کننده سردرگمی مطلق کاخ سفید میان ادامه یک جنگ فرسایشی پرهزینه یا تن دادن به توافق‌های تحقیرآمیز است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/654022" target="_blank">📅 20:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654020">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPcXCkTeraHs8_oc8s20hbbBeb4CdoqmVUaxQv0VInwrIyA0KjImPYyxV4wIPIqW_j8Iy-L_1LvRYE_5bC9y8aq14_bP9fJ31SVHXCMne1tWxnOch_618R7OINt2DknyCYAIT4aDtW3uUX_T8oOlfgAjT7ST90RWIWmXCAVH1DPHZo2DT5lHTDZco7PfpTSBwsX6qsLp-aasGjK8OMZ8Xcl7yl1fUpDsxAv-FizXaEiKRZTdqu-MJBb8HKtFPcchtPxuTwXVLXgpqjQ8itgl9YsBwItN9xvr44G8Hy0rkAXznBTFSiCtGPg-cSegNCvfLpdw3kLgRPcgVCaiGDc02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیر تاریخی شاخص کل بورس در دولت‌های مختلف
🔹
بورس تهران امروز هم در یک روند رو به رشد قرار گرفت، به گونه‌ای که همه شاخص‌های بورس امروز سبز و افزایشی شدند.
🔹
شاخص کل بورس با معیار وزنی ارزشی با افزایش ۸۳ هزار و ۳۵۲ واحد به رقم ۳ میلیون و ۹۹۳ هزار و ۱۴۲ واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/akhbarefori/654020" target="_blank">📅 19:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654019">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3LBbsxRa2Jy_uoe4Wch8nO8DEZ0kwgukXR1zvobji4lgdnityxXsyg9nSIf2h30-Mkof5L_tUsFXCsD_w5klcBWD2ghdKxq2LjcnGk7tP-QKH2lMuZt3Z8QhWXT5NfNFbLVfK8JekXZ3CLOlKVhW29m9KvYQlCeQndonItuHeRBY1DNcmVslBPrgSSgurnvE_tLD_Fbv-_ceeON5wK8p8SxUu9qZa_h2GVxmYI94X6Tanz6e5wtSWpI1KvIJX8G7rlHhQi-7EM6CDHxh9ej2auhwHptd9XuyxgNTKewUh53j0Ek2uiQyOr5t97lA53CzUsdATs_bEI3fKLH_oASVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران یک‌پنجم ناوگان پهپادهای ریپر آمریکا را نابود کرد
🔹
ارتش آمریکا از زمان آغاز درگیری با ایران ۳۰ فروند پهپاد MQ-۹ Reaper را از دست داده است که نزدیک به یک‌پنجم کل ناوگان پیش از جنگ واشینگتن را شامل می‌شود و ارزش آن نزدیک به ۱ میلیارد دلار برآورد شده است.
🔹
به گفته ژنرال دیوید تیبور (معاون رئیس ستاد برنامه‌ریزی پنتاگون) ناوگان ریپرهای آمریکا که دیگر تولید نمی‌شوند، اکنون به حدود ۱۳۵ فروند کاهش یافته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/akhbarefori/654019" target="_blank">📅 19:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654017">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6vasdUCBvdaPGCr6pXdEinNbXFm8jj373r3qMuJ-Q2KKE3DFZHAKpFGxCvtHAaj6vzOMCT5KFr0bvNCJm2iyjoqEW4GJWLn2qqUkamjyKsK54GoPru8u4urbZgA8MA1_qwZefIWxciaDLN0RM8sQjo13WyaMeHXZayG0lWNcebfDyBGtrFMwWxVxT-u4e6uOLuzIJwWXW5NdaLUaBhC2duk-FxFFJXDkliysjMoKBVb4yO5z9JWvaAxWUA-8bybtEFXVTNLgvUsEBTH5fTkLn6HMW_7QI0oo0v7XuAmQmeOyiYLmZ3obCNHXNSVHcTlcZv25jWhlUBgozXHnAKaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بار دیگر به ایران حمله می‌کند؟ / ۵۴درصد شرکت‌کنندگان در یک نظرسنجی پیش‌بینی کرده‌اند: بله!
شما هم کامنت بگذارید و درباره شانس جنگ یا توافق نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3217351</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/654017" target="_blank">📅 19:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654016">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUJwvQ_QUnLHbYYK2FcVFkZRTEI4CbFHiJdXmG4tnuFzznvaX0WEsYOhlnD5dodvI_8ICq5b8G3-D0qTJcmkLCoZBy-l-DAURrIluBeUguIUhj8dkMFuJb3gw_qyS1o1aVAppKW3vPNfqyunjvpnsoiJa03OAqhpMyXyvukxdwCGwZuMi_6s-k51ZJzUW5oVvDyEW9ZAMJiUtQligEH6JT_5EY7OPX1H8mAduh3gMR1-SNHK3zCiPb4TD7D7OBjLzhwppdXzkkvxlO-hS0X8kMP-dcZMIle-i_7eMzq1Xeg_sCWNZbPq1KtnMj0cr7gqK4OI1rtu0qqUMMBrhsGODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین پیام دبیر شورای عالی امنیت ملی به مردم عزیزِ ایران؛ عقب نشینی در‌ کار نخواهد بود
▪️
"عقب نشینی در‌ کار نخواهد بود"
▪️
این را میدان نظامی، میدان دیپلماسی و مردم مبعوث شده حاضر در خیابان با مقاومت جانانه خود نشان دادند و دشمن را زمین گیر کردند.
▪️
حالا بیش از هر زمان دیگر کشور نیاز به وحدت و انسجام دارد تا آمریکایی‌ها و صهیونیست‌ها در این زمینه هم مأیوس شوند.
▪️
میدان وحدت و انسجام هم یک میدان دیگر در مبارزه است. تلاش همگانی برای جلوگیری از هر سخن و اقدام وحدت‌شکن، ایرانِ عزیز را به پیروزی نهایی خواهد رساند؛ ان‌شاءالله.
▫️
محمدباقر ذوالقدر | دبیرشورای عالی امنیت ملی | ۴ خردادماه ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/654016" target="_blank">📅 18:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654015">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
غریب آبادی: واشنگتن باید توضیح دهد چگونه دادگاه را با موشک جایگزین کرده است
🔹
معاون وزیر امور خارجه: در ماه‌های اخیر، ارتش آمریکا در کارائیب و شرق اقیانوس آرام، ده‌ها قایقِ مظنون به قاچاق مواد مخدر را هدف حملات مرگبار قرار داده؛ عملیاتی که نزدیک به ۲۰۰ کشته برجا گذاشته، بی‌آنکه بازداشت یا دادرسی عادلانه ای در کار باشد یا افکار عمومی از ادله و هویت قربانیان آگاه شود.
🔹
اکنون، یک بررسی محدود درون‌سازمانی در پنتاگون ناگزیر شده به روند این حملات بپردازد؛ اما پرسش اصلی فراتر از پروتکل‌های هدف‌گیری است: آیا یک دولت می‌تواند در خارج از میدان جنگ، «ظن» را به حکم مرگ تبدیل کند؟
🔹
مبارزه با قاچاق مواد مخدر مسیر حقوقی دارد: تحقیق، بازداشت، ارائه ادله، و برگزاری دادگاه و دادرسی عادلانه. شلیک به انسان‌ها در دریا، بدون محاکمه و بدون شفافیت، چیزی جز قتل فراقضایی نیست؛ همان نقطه‌ای که نقاب حقوق بشر از چهره مدعیان آن کنار می‌رود.
🔹
واشنگتن که سال‌ها برای دیگران نسخه حقوق بشر نوشته، باید توضیح دهد چگونه دادگاه را با موشک، و قانون را با مرگِ بدون محاکمه جایگزین کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/654015" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654014">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d47069e70.mp4?token=QK6hh3yAktQhbz2Th11idiKN57v_zVg2xfwVqH3QHm1ZYeVUdk2V3ORGEP4XlessFYYK1IB4Nd7vKH9vCNflZn611peSWjLe3ftJVxdA5Ar2xN_Wf-y6COEnfGyvh0m1klF1JltqZurB4GSqz6B4wFx3RtiMG1yZkv1zIHWxfGg08h8BTy_t1jYlVqR1k6qGcEfW2ezvd9UGozaCtTv-Y6stuwPppGD3j0aFaYY7VPBXQhDZAjmE3M2EPOS59Y6ix6gr_ddcGmBd6-vdR3IaKg2gMBnmSGTSwrQAutlyUAgm4QvtbivKhiChMlePmaDNt7QUIMoUpHlFLwcDjZAXyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d47069e70.mp4?token=QK6hh3yAktQhbz2Th11idiKN57v_zVg2xfwVqH3QHm1ZYeVUdk2V3ORGEP4XlessFYYK1IB4Nd7vKH9vCNflZn611peSWjLe3ftJVxdA5Ar2xN_Wf-y6COEnfGyvh0m1klF1JltqZurB4GSqz6B4wFx3RtiMG1yZkv1zIHWxfGg08h8BTy_t1jYlVqR1k6qGcEfW2ezvd9UGozaCtTv-Y6stuwPppGD3j0aFaYY7VPBXQhDZAjmE3M2EPOS59Y6ix6gr_ddcGmBd6-vdR3IaKg2gMBnmSGTSwrQAutlyUAgm4QvtbivKhiChMlePmaDNt7QUIMoUpHlFLwcDjZAXyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرایط دریافت بیمه بیکاری تسهیل شد
🔹
وزیر تعاون، کار ورفاه اجتماعی: شرط بارگذاری کارت پایان خدمت و مدرک دانشگاهی برای دریافت بیمه بیکاری حذف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/akhbarefori/654014" target="_blank">📅 18:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654013">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyFCg0yTBaQ4i1AVet9sIGrUDNtbBXJBiSsdHd0p-pdUlgqXwb9Z03ZactpiB3SHUKDQ8VljCjnlMadgp51i2H9FESnbJfALD66xUfoNxqZCKa0EjLFKRYIVBRBCjGkSsyzA12_OooOvCo6ScUMO3GLSSy391uYt7i7z29zC5g75fNsbJBsQ-vBOgkqMDQevgAe_1lUJA7MiXSHZKN-GNR3YOIPnJsdRAciFtJHYhPjMO8ZKZYUT3K3z_rb5f1o0IQkjvcTHkV-I-K4-BksX_Dop9Svk5Fwa9bfnHGwpBGDLqZptkXBxc9jGRVw3_MYKc-_xvUkB5KyV7I8oM7pDNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت‌های جدید لبنیات اعلام شد
🔹
دبیر انجمن صنایع لبنی از افزایش قیمت ۴ قلم پرمصرف لبنی خبر داد:
🔹
شیر نایلونی: ۸۴ هزار تومان
🔹
شیر بطری: ۹۸ هزار تومان
🔹
پنیر یواف ۴۰۰ گرمی: ۲۰۳ هزار تومان
🔹
ماست دبه‌ای ۲ کیلویی: ۲۲۸ هزار و ۷۰۰ تومان
🔹
هفتهٔ گذشته نیز قیمت شیر خام با افزایش ۲۹ درصدی به کیلویی ۶۰.۵۰۰ تومان رسید.
🔹
گفته‌شده انجمن صنایع لبنی و سازمان حمایت برای افزایش قیمت‌ها به‌صورت لفظی توافق کرده‌اند و هنوز ابلاغ رسمی صورت نگرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/654013" target="_blank">📅 18:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654012">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b1019673.mp4?token=AQxggCCmY4uwhHM3NmiOKKbfvmGayDgYNNtJn5cUn-kbjH2KeTR7yDIMBIp128MuN7qtgWcnL08jbNdsn3PkBL7rzSPXQkyZ2VjFHoh0W3erShFJHKxXLC19f5fzPJcVnemckqQ8om6sPcUYx2blATSGxecTpWlhCmswFfAMWkryheHzHdhmm3VWb4yXaftneCcqEbrL4PZF9VfqfcxOR3EK79X9vkK0GqpQ5DUsdAx82KnIMi5SDvRw66VDMrPPhkEDeuGm_FV337bNwW3YN8mF7Yqf4-GyO3Bp7FoMSjB_jXpujcmXxe2mhwRHWJogt3OIbQNh5CVXgNfeMjuj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b1019673.mp4?token=AQxggCCmY4uwhHM3NmiOKKbfvmGayDgYNNtJn5cUn-kbjH2KeTR7yDIMBIp128MuN7qtgWcnL08jbNdsn3PkBL7rzSPXQkyZ2VjFHoh0W3erShFJHKxXLC19f5fzPJcVnemckqQ8om6sPcUYx2blATSGxecTpWlhCmswFfAMWkryheHzHdhmm3VWb4yXaftneCcqEbrL4PZF9VfqfcxOR3EK79X9vkK0GqpQ5DUsdAx82KnIMi5SDvRw66VDMrPPhkEDeuGm_FV337bNwW3YN8mF7Yqf4-GyO3Bp7FoMSjB_jXpujcmXxe2mhwRHWJogt3OIbQNh5CVXgNfeMjuj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نفت: باید عرضه بنزین کشور را بطور خاص مدیریت کنیم و در تلاشیم تا تاسیسات آسیب‌دیده به سرعن به مدار تولید بازگردد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/654012" target="_blank">📅 17:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654011">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ffe5cedf4.mp4?token=khY4pDpmgXXiPXp2gY6gXhyZ5LPoasWHVxY4WCTkFnJ8XEiqNN7KICtVtLOOejbId4IT3TJq5rltQ4dPeRpI6izVPLFUOKxQ8oEx0MGBZX35gefMleEX-lpyWdB7N2m-s0_f-AAMJ58dzoagm5nNphax2Y7CDgVayH4RPc8M-OAT61vsPchP5DALLTxtoEEEiObM2h0_FYEnX3xGTmTolXy0KosU8xZiex7efRQMc1tvYnNuX__lchMPdI3YhGFb4I8CULG6ZYJdx39jM1q2a6wCmaAY4zoFQIMYZlDocbWZqZMrMUdoJRe1hABwt_-NXnRAINjXcFzOT-A9TzqpKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ffe5cedf4.mp4?token=khY4pDpmgXXiPXp2gY6gXhyZ5LPoasWHVxY4WCTkFnJ8XEiqNN7KICtVtLOOejbId4IT3TJq5rltQ4dPeRpI6izVPLFUOKxQ8oEx0MGBZX35gefMleEX-lpyWdB7N2m-s0_f-AAMJ58dzoagm5nNphax2Y7CDgVayH4RPc8M-OAT61vsPchP5DALLTxtoEEEiObM2h0_FYEnX3xGTmTolXy0KosU8xZiex7efRQMc1tvYnNuX__lchMPdI3YhGFb4I8CULG6ZYJdx39jM1q2a6wCmaAY4zoFQIMYZlDocbWZqZMrMUdoJRe1hABwt_-NXnRAINjXcFzOT-A9TzqpKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوتی‌های عجیب خبرنگار ایران اینترنشنال در پخش زنده سوژه کاربران فضای مجازی شد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/654011" target="_blank">📅 17:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654010">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxmoFg-B4prM9N0h_F7W9F_76qvCaAnNVDGL-9f8o3DqRBhYQT6PnOl9yKBTpSqc15KhDz-jX0Acx80HoFzoZYEa5I52JajMgtpPNhqXag22Jn687mbGWG9hm_8sk4ey5XGHRgHzA0E2L5LdDBEmbYeA8AHWctU_QOB7YvNxuwpUdtpCpS9SMHQt6UrpFYzXjHWJ4BuvjZiaB8iocJG27g6nhubgFHtaQ6UtPZJhvu7O7KHShZuRypOi7JJ44CPKfwq2tpKEudrCdtcrdPg0QW4sdsFtg6LjuBWRpWoeEjo6ZvQ43WhXWmDyOFL-mnRXW2hMtMjCMiRaeNq5nw2CNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
اعمال شب و روز عرفه را در این پست ببینید
▫️
با نشر این پست در ثواب اعمال آن شریک شوید.
#روز_عرفه
#شب_عرفه
محتوای مذهبی را در این کانال دنبال کنید
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/654010" target="_blank">📅 16:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654009">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51460aa976.mp4?token=ReTRbqxw1YGbTOPS40zH9siuseaTljV39qPqrqDO5WLCY4kIXU3pdq2nD_t28P6ngDTCYb_QqRNBAAbpD_rkEowPrWiGiIt7247sCilUqxQ7-bIqx1Wb4SUyH_4_DL5LjKtlfvGuO0EzZo1IanXin42nveOoVbehAF5Uj4OHTuceaEh4zcxr9343Y7paZLkxR1ZvL9yvEbp-bL3Clm19T3IYppQA6cpmTmxRTmIC2oLjCcv4lACzigXnPIdZ9PJiXgd9LW4mKLTk27UTkJn1LShRBqneKiAvckaepieyrIx_3ZN2bY7YbdXqzXXPrh_AKRmq-K69foU2khTBqWRRzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51460aa976.mp4?token=ReTRbqxw1YGbTOPS40zH9siuseaTljV39qPqrqDO5WLCY4kIXU3pdq2nD_t28P6ngDTCYb_QqRNBAAbpD_rkEowPrWiGiIt7247sCilUqxQ7-bIqx1Wb4SUyH_4_DL5LjKtlfvGuO0EzZo1IanXin42nveOoVbehAF5Uj4OHTuceaEh4zcxr9343Y7paZLkxR1ZvL9yvEbp-bL3Clm19T3IYppQA6cpmTmxRTmIC2oLjCcv4lACzigXnPIdZ9PJiXgd9LW4mKLTk27UTkJn1LShRBqneKiAvckaepieyrIx_3ZN2bY7YbdXqzXXPrh_AKRmq-K69foU2khTBqWRRzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احمدی، نویسنده کتاب و راوی دفاع مقدس: عملیات آزادسازی خرمشهر در دنیا بی‌سابقه‌است، ما ۵ هزار و ۴۰۰ کیلومتر از خاک‌مان را آزاد کردیم
🔹
ما در یک روز ۱۹ هزار افسر عراقی دستگیر کردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/akhbarefori/654009" target="_blank">📅 16:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654008">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21bb2b8bf.mp4?token=HzZ1gYhe_5xOgg9bJSM9sCeW0fUXrbzcAXrM97V--ZTmlRDDNqeXHfII4kKbJIteTxupKQgks4017lKFp_W5gBROXwc5tY8p-IOr3k88_ug58k5CfCK7NpCu6z3pEbLfK2SEKzIYwzz0zCSGpFNmeNrA8jVg3UaS2lYOlZS6tthGwJsSR_Akv53IxQbcAvXbAXG8izO6unsLv1Cdm4boEaT7Owq2cQZPpTdwGJoJNPTP_cfy-09uZYlAIaraLbAy5SF5_EdCb-hfAoKfM8DZKls-36tRz_zAN_uCf9MR0A4YGmlCrYZ2eSWtwE9yoOpp9oeJZX5z1QeQz88zNj4-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21bb2b8bf.mp4?token=HzZ1gYhe_5xOgg9bJSM9sCeW0fUXrbzcAXrM97V--ZTmlRDDNqeXHfII4kKbJIteTxupKQgks4017lKFp_W5gBROXwc5tY8p-IOr3k88_ug58k5CfCK7NpCu6z3pEbLfK2SEKzIYwzz0zCSGpFNmeNrA8jVg3UaS2lYOlZS6tthGwJsSR_Akv53IxQbcAvXbAXG8izO6unsLv1Cdm4boEaT7Owq2cQZPpTdwGJoJNPTP_cfy-09uZYlAIaraLbAy5SF5_EdCb-hfAoKfM8DZKls-36tRz_zAN_uCf9MR0A4YGmlCrYZ2eSWtwE9yoOpp9oeJZX5z1QeQz88zNj4-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیماهای باری نظامی آمریکایی در راه غرب آسیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/654008" target="_blank">📅 16:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654007">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjN1lKP8QlUmH1oNMwnLuYl7h3d3wVy1Zy2y-uHN9a_N2BQMbnMyLFhpcQeQCWzGWPVbzxIi9Mjs-dRezdlpQ-YslB8r8-C3AYz-yKFsPW5h0IwZAxrOJ0PtjEuxvJqQ1PgLEvqcOQb-fVt8V-FqG053XDrWKD8SfOiAZied0Tn4_TWo61O_r7lVRTeJGBTB6s-MeQHsgW55YpGenPTJk9-G7tfWEyNf-Wov6YblErroz8VqlGki_fp4-dV0UWoTPZWFdEEfoTG0c06iCYkcyGnEZbusHdAF21sKhkqsXCmKYAhRpQPmQj0qQYoXDGmDEWnpAyVAbj9CB3dmGNMpeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست فرمانده ارتش اسرائیل برای حمله به بیروت
🔹
رئیس ستاد ارتش رژیم صهیونیستی در جلسه کابینه امنیتی خواستار تصویب حمله به بیروت در واکنش به عملیات‌های پهپادی حزب‌الله شد.
🔹
روزنامه «جروزالم‌پست» گزارش داد که «إیال زمیر» از اینکه رژیم صهیونیستی به دلیل محدودیت‌های آمریکا، استقلال عمل کامل در لبنان را ندارد، شاکی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/654007" target="_blank">📅 16:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654006">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3863ddea63.mp4?token=AAXwncYbNSWMEdYSNdU222Vjvk_LsdH24JzcWm4pQX-COb7Jpfzn5hBqKR83nqfCUbKZ11r545SvdHNw49WzqyHGtdGRBhaAa00ZEsiqhtpGSFtyNX3HUMCyy890S824RrJCWL9eN1WeZd0_NSDG2O0OyjyzUbiPgwLWfEVU80T1GcCrAYto9PwL1mJmYSJjPEpfC5sSI7CRcQZd_QfQSaLFnR8cUequAyDeAq02IXcBipRnBSdQrtERAqQNaqYAQg7jhn-yhIk3-9sQHTX_8PP4zLkmE8Dt5CYY5T1uTgeXnnHDI03F_M_xX19DO7_2Sb1OLkKpCnws3xpCg0y4Cb0N132xKHCqg82Bllzi1dzKuIacHUiZ-iztnd8hGC2d7r5SMy_CDL2k-3Gg269sFD4dyAYsko19lkku0Nhoxfz8iaIxG1S4fdEm7b2Um6JQ3Mn9CSEdpnLYS2eFlzqbeYwdnyVtDqe4RXFzL42BkU7Y4cqVXKtwZRYFpizMqwiuossWSruMIg_tFGWfsfSQI2FvbufYQKHiPGVgfsmVJ0BJyz-25ZIUq_M9W_QBdTmhI8qInK2uDiumvT4qeR971DQjWK9R5a5oa1RkJ00uceP-A6wOLMAnxw4N7bwma34Cy_uxSTCVGqGxiSXE3VxYpdqdKVzojKxKesPhNaCdEXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3863ddea63.mp4?token=AAXwncYbNSWMEdYSNdU222Vjvk_LsdH24JzcWm4pQX-COb7Jpfzn5hBqKR83nqfCUbKZ11r545SvdHNw49WzqyHGtdGRBhaAa00ZEsiqhtpGSFtyNX3HUMCyy890S824RrJCWL9eN1WeZd0_NSDG2O0OyjyzUbiPgwLWfEVU80T1GcCrAYto9PwL1mJmYSJjPEpfC5sSI7CRcQZd_QfQSaLFnR8cUequAyDeAq02IXcBipRnBSdQrtERAqQNaqYAQg7jhn-yhIk3-9sQHTX_8PP4zLkmE8Dt5CYY5T1uTgeXnnHDI03F_M_xX19DO7_2Sb1OLkKpCnws3xpCg0y4Cb0N132xKHCqg82Bllzi1dzKuIacHUiZ-iztnd8hGC2d7r5SMy_CDL2k-3Gg269sFD4dyAYsko19lkku0Nhoxfz8iaIxG1S4fdEm7b2Um6JQ3Mn9CSEdpnLYS2eFlzqbeYwdnyVtDqe4RXFzL42BkU7Y4cqVXKtwZRYFpizMqwiuossWSruMIg_tFGWfsfSQI2FvbufYQKHiPGVgfsmVJ0BJyz-25ZIUq_M9W_QBdTmhI8qInK2uDiumvT4qeR971DQjWK9R5a5oa1RkJ00uceP-A6wOLMAnxw4N7bwma34Cy_uxSTCVGqGxiSXE3VxYpdqdKVzojKxKesPhNaCdEXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ علیه ایران، تجاوزی علنی و جنایت علیه یک کشور مستقل بود
🔹
استاد حقوق عمومی دانشگاه فرانسه: این توافق، صرفاً به تقویت حکومت ایران منجر خواهد شد؛ این یک شکست راهبردی مسلم است. جنگ علیه ایران تجاوزی علنی و جنایت علیه یک کشور مستقل بود و بر پایه سناریویی هالیوودی بنا شد.
🔹
آنچه ترامپ به عنوان دستاورد ارائه می‌دهد، بازگشایی تنگه هرمز تحت کنترل ایران است! ترامپ درکی از جنگ نامتقارن نداشت، جنگی که در آن لزوما ارتش قدرتمندتر پیروز نمی‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/akhbarefori/654006" target="_blank">📅 16:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654005">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSI7Arnq4JSKoU9pjCy5M3-eVOeUgbxkkd-X3GDBem8BuWEKox5ZouNy6Zlab1abfiANYZBJL5R18RcKs7FCL7gTzXTZYpO0LDkxTbyOQOEaOjfHAN85eMVUtmFY9r-O-R1EnJPaSTRA3nxzN89WDjIFKSTMXZl87vgufzEzhZACcYk6_pnQqLNhesGUaAWy41xp7SAIlWUjxmRWl8DxKcksCrQUZqBk7Pt8QSNUS05S4Upz8Sb3wXr2fMTY60BEtKD5D5wuRtGHywPx5IMZBFmKllACcKdAvyfjXjfa-IK5M7L1HxVu3GVybQO36kLMQ4cgnXVRwwkDf_96NSBcUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون اول رئیس‌جمهور: نمی‌شود شعار کمک به مردم سر دهیم ولی در عمل به مردم اعتماد نکرده و اینترنت را بر روی مردم ببندیم
🔹
در کجای دنیا اگر یک کامیون در یک اتوبان تخلف کند، اتوبان را مسدود می کنند؟ ما کاری که با اینترنت می‌کنیم مثل این است که به جای برخورد با راننده متخلف، کل مسیر یک اتوبان را بر روی همه خودروها ببندیم.
🔹
برخی مخالفت‌ها با بستن اینترنت ریشه‌ در سلایق شخصی و منافع شرکتی دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/akhbarefori/654005" target="_blank">📅 16:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654004">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHd90h_eVPOX-lVuMIHoc80I3M-xEJR756m8R4nyvcsFNEpCf5wnoSHUIn4SR1ox5RrjVQOeHvjxSlgQhJjpITn8YcKr3-MEkYBx5tenwfZ4b-aQIJvYHzanP6zy7dFDTtwG-LutMSyx5VtS-swm4VDIFt856Y4nqM0qusNJsweVT3-Zdzj-EgOfVOmr6MjswajFJpRBMkbOr8PUMNWegA4EVwQjR-a9nBf4I1DAw7aDf2uNS8HcMZOJJbquZBdyh8PXwuVM0B2iTFXG4fPI952PiITqb2D8NH9PYoQsRmaFBBgVJej_KvQ1sZdT6WRBmeKowT9iWF2Eemd9-PaPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عربستان هم «شاهد» ایرانی را کپی می‌کند
🔹
دو شرکت استارت‌آپی مستقر در آمریکا و عربستان قصد دارند با ایجاد کارخانه‌ای در نزدیکی ریاض، تولید پهپادهای جنگی با الهام از پهپادهای «شاهد» ایران را آغاز کنند.
🔹
این هواپیماهای بدون سرنشین با نام «اسکای واسپ» قابلیت اصابت به اهداف تا فاصله ۱۵۰۰ کیلومتری را خواهند داشت.
🔹
بنیانگذار این طرح، لوسین زایگلر، در مورد اهمیت این طرح گفته که «اسکای واسپ برنامه‌ای است که می‌تواند شرایط را متوازن کند و توان بازدارندگی عربستان سعودی را تقویت کند.» او از ارائه آمار دقیق در مورد تعداد پهپادهای تولیدی خودداری کرده، اما تأکید کرده که این تعداد متناسب با نیاز عربستان برای حفظ بازدارندگی این کشور در مقابل حملات تعیین خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/akhbarefori/654004" target="_blank">📅 15:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654003">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyvusYEb_iOKQW6AKrmszByb-GPgX0Ara2oQxQiT-6nnp70upZKhc8iN91Sjg7O7qEJHrhzk49stRgUr5_8chyoQgZMcictU_uZj92CvnMxJsfYGrbo4pcklwCy4wxMeFiCrb_wM7QGG60RcXi1ktegXIsV53_4vkT3ggAWNQNI04-snUNdzfrrTlXQDSMG6CQpxZPtFbntdAF1M_baZvv8RnUOsKHQgozJR856zWVWF_QT1lLtk12sdS_EME3w7izS8pQiJ2nIEKS-fRBja8P7DncIsWftAMe39O0Cgl5Nw_qyuE54USzZIJwm2BCSu1bjwxIU_s5iQWScyt9oEXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‌  قیمت مرغ درحال کاهش است
🔹
براساس گزارش میدانی، امروز قیمت مرغ در مناطق مختلف تهران از کیلویی ۳۹۰ هزار تا ۴۴۰ هزار تومان فروخته می‌شود.
🔹
پیش از این، قیمت مرغ در بازار به دلیل کاهش جوجه ریزی به ۴۸۰ هزار تومان رسیده بود.
🔹
یک مرغ‌فروش منطقهٔ بریانک تهران گفت: قیمت‌ها در چند روز گذشته هر روز حدود ۱۰ هزار تومان پایین آمده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/akhbarefori/654003" target="_blank">📅 15:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654002">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
معجزه‌ای که امدادگران هلال‌احمر در یکی از ساختمان‌های مسکونی مورد حمله رژیم صهیونیستی و آمریکا دیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/akhbarefori/654002" target="_blank">📅 15:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654001">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
رویترز: قالیباف و عراقچی وارد دوحه شدند
🔹
محمد باقر قالیباف رئیس مجلس شورای اسلامی و سید عباس عراقچی وزیر امور خارجه ایران برای دیدار با نخست وزیر قطر و گفت‌وگو در مورد امکان دستیابی به توافق بین ایران و آمریکا وارد دوحه شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/akhbarefori/654001" target="_blank">📅 15:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای خبرگزاری رویترز:
🔹
مذاکرات در دوحه عمدتاً بر تنگه هرمز و اورانیوم غنی‌شده با غنای بالا متمرکز است.
🔹
رئیس کل بانک مرکزی ایران بخشی از هیئت اعزامی به دوحه برای گفتگو در مورد احتمال آزادسازی دارایی‌های مسدود شده به عنوان بخشی از توافق نهایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/654000" target="_blank">📅 15:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653999">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaPCEt0f7t1nkQqQvFmUzQlkP8vG062kVEmUGwrX997yfPBN6uBXtQeU1vcPaPx6_9_9ngepoNODJYozCKTQW5HUXmNxEtUjfjzIyuv8LvXSbXv87GBRXQXGU5vawA2WImpDUk_F8ggVtzzyTtKtkUM8D8CqkpBMKkQt46fWGwcxnznmeNSUosnowqzw-2AoOMERMdvvdy3tzKx5fX9bJTfp_yNNWRxrLvsC1N2Txo_CICQ7pbDneuo_ZGKtw9zgLj-0eoc6HjX35xlduams2N_iMCGH9XpPXYbj1gI5aOxyrqCr93ieIR-_kpjPeyknOqAjMANjS1j6Tdv33rgukQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حنظله اطلاعات ۶۹ افسر اسرائیلی که به کاروان صمود حمله کردند را افشا کرد
🔹
گروه هکری حنظله: نام‌ها و مشخصات کامل ۶۹ افسر نیروی دریایی اسرائیل که اخیراً به کاروان جهانی «صمود» حمله کردند، افشا شده و برای هر یک از این افراد مبلغ ۱۰۰ هزار دلار جایزه تعیین شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653999" target="_blank">📅 15:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/218662fffa.mp4?token=Lf0ljrH9elFm0EjY22RmKaVxvQPu7e6CXp88-gvCRcgcTJZa4zrlpRFAQXtf1pDN1Eue-I0L4tDvu_8hJyi5FliW3OfZNPXO9QQ49JHwfzlTDOC6twZrD4MtYlIqqkHTvzAlPlNMPfBprB63soDYPNzPLYVGJCr0dk0t044Vp41DPEDBdR1-j8v2D--0noEcZrLnFmACHcFShyUFkYPgC9Ip5zEaCrOxlpb--fw98e8hRJn7YL_xBB883QMCI36gF7VYIZxrOsMTF82rgI9K29elwbrXHg5SseAUbfovBY7vKp96jiiA9Qxra4IqQAWAnLr6CxRQdSdsNo7CzpIYPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/218662fffa.mp4?token=Lf0ljrH9elFm0EjY22RmKaVxvQPu7e6CXp88-gvCRcgcTJZa4zrlpRFAQXtf1pDN1Eue-I0L4tDvu_8hJyi5FliW3OfZNPXO9QQ49JHwfzlTDOC6twZrD4MtYlIqqkHTvzAlPlNMPfBprB63soDYPNzPLYVGJCr0dk0t044Vp41DPEDBdR1-j8v2D--0noEcZrLnFmACHcFShyUFkYPgC9Ip5zEaCrOxlpb--fw98e8hRJn7YL_xBB883QMCI36gF7VYIZxrOsMTF82rgI9K29elwbrXHg5SseAUbfovBY7vKp96jiiA9Qxra4IqQAWAnLr6CxRQdSdsNo7CzpIYPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرندی: قرار شد قطری‌ها پول‌های بلوکه‌شدۀ ایران را پرداخت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653998" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjArKdMXVEiGXlXFWL5UmE1nSGLK7i0yqoO3i7NNRqmfuN_-Ozff31qkYoUyn_DghQszWN27pwvRPMfJXFMT6jdDUWwZwUdrPNlTyxrhMCTJbd5NwmEG7nokWEy6Us17g2tdqIGt30D0u7e8sWAs3HItM0quWh4zLIVL8KS9qEzMtnEKyyozPrexbvdTD6gOC0nUOBFZwzSkghDGwWGfp-Q9bn-71vk-sr0aCGgbp5YSk5vNnENaj08_Ut164sezlJ7GiMounRITMFudvUKwikNOJrLN_95dGbD7GPlk668fDrNBDVCW7fsLQGQolNy4XMnEPerZT56wu0aabObcTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تداوم ششمین سال خشکسالی پیاپی در ایران؛ بارش‌ها در ۱۲ استان نرمال نیست
🔹
معاون شرکت مدیریت منابع آب ایران: اگر چه در سال جاری متوسط بارندگی به ۲۲۹ میلی‌متر رسید‌ و ۶۳ درصد نسبت به سال گذشته افزایش داشت‌، اما نباید دچار خطای شناختی شویم.
🔹
همچنان در ششمین سال خشکسالی پیاپی قرار داریم و ۱۲ استان کشور که ۴۰ میلیون نفر از جمعیت ایران را در خود جای داده‌اند، همچنان در وضعیت بارش زیر نرمال هستند.
🔹
نامتوازن بودن بارش‌ها و زمان نامناسب ریزش‌های جوی مدیریت منابع آب را با چالش جدی مواجه کرده است. ‌
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653997" target="_blank">📅 14:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969b451344.mov?token=Mkzt717L1APeJUJ15CQNO4T_kgi7B4Wb_uAsCzmkQzU0Bg1gb_1snUmtfUA9D1PuopXlOfEUH3Q52XbCdKutKF53B6cWiZAZwhp99jgrNa_t0uQFC2y5OQ9lXOz7JZH9oK5ksRFPp7P--qU4oAjGGn7Fl4iMv1aa-YI-_s21mWhJjLqlcYOIefYVU2S_mmcYxiXjqKPU52IotME1fjJh3hy2f1nri9FWYq-OdoOXxGMHI05P5JSKoPyQTzJH4hxC9bIz6RpPCxgJZxKIiSl6cOfMP7-Kn_j6hj-gBuBKWseELYgtflWklRjvDuLOj7YUlVMOfyBTS8RaKtUq4i4f1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969b451344.mov?token=Mkzt717L1APeJUJ15CQNO4T_kgi7B4Wb_uAsCzmkQzU0Bg1gb_1snUmtfUA9D1PuopXlOfEUH3Q52XbCdKutKF53B6cWiZAZwhp99jgrNa_t0uQFC2y5OQ9lXOz7JZH9oK5ksRFPp7P--qU4oAjGGn7Fl4iMv1aa-YI-_s21mWhJjLqlcYOIefYVU2S_mmcYxiXjqKPU52IotME1fjJh3hy2f1nri9FWYq-OdoOXxGMHI05P5JSKoPyQTzJH4hxC9bIz6RpPCxgJZxKIiSl6cOfMP7-Kn_j6hj-gBuBKWseELYgtflWklRjvDuLOj7YUlVMOfyBTS8RaKtUq4i4f1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز متناسب‌سازی حقوق بازنشستگان روستایی از تابستان امسال
🔹
مدیرعامل صندوق بیمه اجتماعی کشاورزان، روستاییان و عشایر: در صورت تأمین اعتبار از سوی سازمان برنامه و بودجه، مجموع مستمری مستمری‌بگیران این صندوق در سال ۱۴۰۵ حدود ۵۵ درصد افزایش می‌یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/akhbarefori/653996" target="_blank">📅 14:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653995">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ-y7CD3JIriiQtDidW05YYor7w3vqCc3odC2Mg54o6BOBt0je2t_Fox2j3lP7-MGVEsS99Tgn7rfjV1Pegj0vD_t5PcpVmZ0Gqn-TgMHrodvhDd9aSULR55nFulHZB8yYetNUHKeUrKlL9kLO1uuAH4uCTDqjy5oZnKDBso6EBf-ZdoPuwgxUGUY26VSSrp0ZVwCVDzBjDrbunsFmUBOCyn0wg35l8AoL11D-7mp62L7-ZhIAGnva9z_Zpq7C4Q6hJW8J3OuTlY46-uR0WDr1FabwyknuQwYZSR5yw1t54uLGlkew-MGzq-xClkoS7Hc4gl1ZRwrJkZ_BgcN50OCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بن‌‌گویر: اسرائیل باید به جنگ تمام‌عیار در لبنان بازگردد
🔹
وزیر امنیت داخلی اسرائیل «ایتامار بن گویر» با حمله تند به نخست‌وزیر اسرائیل «بنیامین نتانیاهو» خواستار بازگشت اسرائیل به جنگ تمام‌عیار در لبنان شد.
🔹
بن گویر گفت: ما نباید واقعیت پهپادهای انتحاری را عادی‌سازی کنیم.
🔹
زمان آن فرا رسیده است که نخست‌وزیر بر میز رئیس‌جمهور آمریکا بکوبد و به او اطلاع دهد که ما در حال بازگشت به جنگ در لبنان هستیم.
🔹
ما باید برق را در لبنان قطع کنیم، زهرانی را تصرف کنیم و به جنگ با شدت بالا بازگردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/akhbarefori/653995" target="_blank">📅 14:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653994">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b5b3e85d2.mp4?token=OpRwFIY59FT8AZkL-dsyaR6XUuMr5MI031DGn8ZzvChUpG3dVseKkQ5UvCX8Ei-m6uVsL0MlCgwBbyrYEwgKIHeKjiikmFAPr5L3E52S4Ovgb9cXV3IYGPPFRKT5KE78o9b5hnRMpjCjCjw-qBiPCqRwlgpOYT6bsT8H1xIUwjc2Zo48rnU1fs00FvW5STr9dxRyabQnczOVyRWE8XJMvtNsVFQMDSOi4oCy5AaCaVS--pO1H522XK4ju00R6cFyTqLEWqwlCs3dQj9UBzMUpIvXfvHa19HEJuB_skwgGBApp1KDSGgijRCMAKodJCTtMfa1OxC4BUJ6hdwT60krSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b5b3e85d2.mp4?token=OpRwFIY59FT8AZkL-dsyaR6XUuMr5MI031DGn8ZzvChUpG3dVseKkQ5UvCX8Ei-m6uVsL0MlCgwBbyrYEwgKIHeKjiikmFAPr5L3E52S4Ovgb9cXV3IYGPPFRKT5KE78o9b5hnRMpjCjCjw-qBiPCqRwlgpOYT6bsT8H1xIUwjc2Zo48rnU1fs00FvW5STr9dxRyabQnczOVyRWE8XJMvtNsVFQMDSOi4oCy5AaCaVS--pO1H522XK4ju00R6cFyTqLEWqwlCs3dQj9UBzMUpIvXfvHa19HEJuB_skwgGBApp1KDSGgijRCMAKodJCTtMfa1OxC4BUJ6hdwT60krSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع بی‌سابقه در قلب اروپا: ۳ هزار حامی محور مقاومت سیاست‌های آمریکا و اسرائیل را محکوم کردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/akhbarefori/653994" target="_blank">📅 14:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653993">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY_3v9xBiT4GaWQSO_FW1BS1wAyQVSbMieJqsIHlIvDFdsf7W_Sr9m45MGqylDP922-bN_MXJWLjWSOpxa6T5D6bcNOjHzEOMVlH0V909P5KtcMP6OR_zBOOF4W06WeEwVOApQKef-l_nBGR5aZwOaf0yj05PuC5C6lrMY2R7IvrVwM8gOoMYA4nsHNiaFv6UEORFQN2QXgHJkTnBj4Hy2RarXwEgvOvPzLqXzeOvAWrmeO19n_n561-ARBVcm3vbsZENPF0liJsIcF9X_sfyoAPR_GGQkI_oMthv38gJGbUnj47OXBLJAtGh31QqAxAQp1JodZPVtQh9-pxv-0tHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاکید سران چین و پاکستان بر لزوم برقراری صلح در غرب آسیا
🔹
رئیس جمهور چین و نخست‌وزیر پاکستان در جریان دیدار در پکن، بر لزوم تلاش میانجی‌ها برای پایان درگیری ایران و آمریکا تاکید کردند.
🔹
«شی جینپینگ» در دیدار با «شهباز شریف» گفت: «ما برای نقش پاکستان در میانجی‌گری صلح در خاورمیانه ارزش قائل هستیم».
🔹
شبکه «المیادین» گزارش داد: «هر دو طرف باید ارتباط و هماهنگی نزدیک خود را حفظ کنند و با یکجانبه‌گرایی مخالفت نمایند».
🔹
نخست وزیر پاکستان نیز در این دیدار، از حمایت‌های چین از تلاش‌های میانجی‌گرانه اسلام‌آباد در مذاکرات آمریکا و ایران ابراز قدردانی کرد.
🔹
شریف در این‌باره اظهار داشت: «پیشنهاد چهار ماده‌ای رئیس جمهور چین درمورد خاورمیانه، چارچوب راهنما برای دستیابی به صلح محسوب می‌شود».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/akhbarefori/653993" target="_blank">📅 14:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653992">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McIS7Q5LCNQjEyFIcsNzhctM5bfOpnBqR2NGycy1lPcwZY4-r9_eqEPy5X0QvYsnHdPcIfSGJRUVFrKmdM5mzuc51EsHQCbI7a8Z67c2z9IY7pdT2LYsglQgUY4FImllAyi1zRAWpvJE5dDRR5cxX_aajfwCbRthvl2Es2RvJTeCdli_swCAf4BCEvT8xv0e0pTS-yGkZOOB_iG5nhnS8-Pej-VP3k-ovte67-eDJwbEpzznPM_h5YZBXF2WVjVTEGcqbLgqP1UhIJkmrvo_ypBOfIUVQpipT8nbs2C4FERzxp8Eix6n1cR4a5l85Md1vxw_bBOZa23jv54nswDDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع پاکستانی: توافق موقت آمریکا و ایران، قریب‌الوقوع است
🔹
منابع پاکستانی گفتند که آمریکا و ایران می‌توانند طی همین هفته، «یک پیمان موقت برای پایان دادن به جنگ امضا کنند.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/653992" target="_blank">📅 13:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653991">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2dQVHy3ENAlR-KFpi7zyIVqOPU0omMrSoGSRPB14pfCxP9WiZwBKgwXQ-4X64DZzKhHKkGNa_XtHy0_ube8JhAAqMQ6lRDWTtfOhEtIwzMCln0ImNOyKSuCDF_wsuwl7kppF7CN6tra-fps2HR92eRgs5HwLCmsGPfaP-52ttE88d_uZd8VDlfEb2n_WRQQnKo6caF70IG_P3yQaf527pShoyWQ9e_I2SQSoPzAech5NUkExY25WLwKfeawIWbNNpqyysZRACvBhSfJ_d1ZXHckTpamhlr5Pu7pnRi09DM8GRNG3p32Fhyzc2LUYAq6gDRIi3Hnuz-65JgqSx7hHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفتکش عراقی با شکستن محاصره دریایی آمریکا عازم چین شد
🔹
یک نفتکش غول پیکر عراقی ضمن عبور هماهنگ شده از تنگه هرمز و شکستن محاصره دریایی آمریکا عازم چین شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/akhbarefori/653991" target="_blank">📅 13:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653990">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bubiBdjoYbQAwePIqV6JmxWvOxJzI0VAC12DvN9JhENo6ZFwcVsz5pKX3WE79Z4ZO9mqWd1fOKg3QTvwFj3_fpY2yvw5rdDIRIBx61QKlY6HosEY3ghC4s8dONpPD-4Wr3OYRhk-aDfvi5sSrpwd3Y8Shw16J8kJNWstQZGWCTc9STn8YZH6qie10com7PzJuvvOWhEUTg0Wdc7jiaWNkj0LpDr1pp9tGxO_7OzNBn8iPjVV11QWTj-OIuWG91whrus06GrVRgqZUecXVTBb-4TQf1BupHl4a8X0xcs561j6C5z8Blpfed1NkTwZ_jpkZ3NKAHcd_MJzMyazAmLARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهدید مقامات اسرائیلی به جنایت جنگی در برابر پهپادهای حزب‌الله
🔹
در حالی که ارتش اسرائیل برای مقابله با ریزپرنده‌های انتحاری حزب‌الله ناتوان مانده، مقامات این رژیم گزینه جنایت جنگی را پیش کشیده‌اند.
🔹
بزالل اسموتریچ، وزیر دارایی رژیم صهیونیستی امروز در نشست کابینه که با موضع بررسی معضل پهپادهای انتخاری حزب‌الله تشکیل شده بود، پیشنهاد داد که «به ازای هر پهپاد انفجاری، ده ساختمان در بیروت باید ویران شود».
🔹
او همچنین گفته است که «این هفته بودجه‌ای حدود دو میلیارد شِکِل (حدود ۷۰۰ میلیون دلار) برای راه‌حل‌های تکنولوژیکی برای تهدید پهپادها تصویب کرده‌ام. از جمله موارد دیگر، این پول به نهادهای غیرنظامی اجازه می‌دهد تا راه‌حل‌ها و ایده‌های نوآورانه‌ای ارائه دهند.»
🔹
ایال زمیر رئیس ستاد ارتش اشغالگر نیز در این نشست پیشنهاد داده است که در پاسخ به حملات ریزپرنده‌های حزب‌الله، بیروت بمباران شود.
🔹
اما ایتامار بن گویر، وزیر معلوم‌الحال امنیت داخلی اسرائیل نیز در این نشست، پیشنهاد بمباران زیرساخت‌های برق لبنان را مطرح کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653990" target="_blank">📅 13:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653988">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
رادیو ارتش اسرائیل: از زمان آخرین «آتش‌بس» در لبنان، ۱۱ افسر و نظامی «اسرائیلی» کشته شده‌اند که ۷ نفر از آنها بر اثر اصابت پهپادهای انفجاری بوده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/akhbarefori/653988" target="_blank">📅 13:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653986">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c8fb333c.mp4?token=DihA0wlslizxapGpSJ_GuCOSJQNStXFCqtJAyFMhrNPL2PItqigN_mtS2IW56w8apGMsg8vllehH90q8OBTpSUoC09knviRg0LvlRaNG0daYLAYoPS427krI6SDn1K8IqjCU0UU1xiZV7ryAyUUejzjAsY13c5D-ALzDGoxkC3oyaeQUFWaKr_pAvH66jmAloJ0yEROcdxhprVCyTgaON0cQmn86R_9v-vTMheEbVtzQcjos0EXCSfJEDJuqeKLkpAniyl2WPPaOtzElYc-64i-8BiADOMNn6dcas5rT4Qv1lPzTJLmbY5M7uWYJLx96oeDioq2M-sEumbrYy2geMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c8fb333c.mp4?token=DihA0wlslizxapGpSJ_GuCOSJQNStXFCqtJAyFMhrNPL2PItqigN_mtS2IW56w8apGMsg8vllehH90q8OBTpSUoC09knviRg0LvlRaNG0daYLAYoPS427krI6SDn1K8IqjCU0UU1xiZV7ryAyUUejzjAsY13c5D-ALzDGoxkC3oyaeQUFWaKr_pAvH66jmAloJ0yEROcdxhprVCyTgaON0cQmn86R_9v-vTMheEbVtzQcjos0EXCSfJEDJuqeKLkpAniyl2WPPaOtzElYc-64i-8BiADOMNn6dcas5rT4Qv1lPzTJLmbY5M7uWYJLx96oeDioq2M-sEumbrYy2geMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون امور زنان رئیس‌جمهور: اگر خانم سرپرست خانواده هستید و ضامنِ وام ندارید، دولت شما را ضمانت می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/akhbarefori/653986" target="_blank">📅 13:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653985">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVX3KvYGwy9436ltCsgRWFzVD3hkQU2GO11iGhciSDriuf2TOAUs-36uA3QJiT_mj9K1zEFbwlod3MrOlncSjf6yOhIWDifpI2f-EzUvMJ76sBJbOWTJcWvs7UHE0-CawiTElCLnI-Vuxcnckgs85o1Y_0yOMFUuUnTtlX4XTd-J2A6YfrMsBx8nqVxnuDQbdy2EH3RgjzIUfwoaFJTxb7LFz-J0C32DelnXWFEwyTaUMwuPnAirgAP1k_Vdqlg-rM5s73-65RFe4Kb7_WTQTM-vgXfTVq5jI069jL3aQfnriit3uQfXcPwowGpndZYcx7Ea9FbswXQTJADL_VMFzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهار شرط اتحادیه اروپا برای آغاز مأموریت تنگه هرمز
🔹
روزنامه ایتالیایی «ریپابلیکا» امروز گزارش داد که طرح اتحادیه اروپا برای مأموریت دریایی جهت بازگشایی تنگه هرمز آماده است ولی فقط در صورت تأمین چهار شرط، آن را اجرایی می‌کنند.
🔹
این روزنامه نوشت که با فرض برقراری آتش‌بس دائمی بین ایران و آمریکا، شروط مذکور برای اجرای مأموریت دریایی اتحادیه اروپا بدین شرح است:
🔹
«اول. پایتخت‌های اروپایی در آینده باید درمورد رضایت رسمی آمریکا از حضور نیروهای اتحادیه اروپا در تنگه هرمز با یکدیگر دیدار کنند.
🔹
دوم. رضایت ایران برای حضور یک ناوگان خارجی در سواحل خود. کانال‌های ارتباطی بین کشورهای اروپایی و تهران هم‌اکنون برقرار شده است.
🔹
سوم. حمایت سیاسی از این ماموریت دریایی توسط سازمان ملل متحد.
🔹
چهارم. اخذ مجوزهای لازم در پارلمان‌های کشورهای مشارکت‌کننده، مشخصاً در ایتالیا و آلمان».
🔹
این در حالی است که جمهوری اسلامی ایران صراحتاً هشدار داده هیچ کشتی نظامی خارجی اجازه عبور از تنگه هرمز را ندارد و در صورت هرگونه تلاشی در این زمینه، شناورهای مذکور هدف قرار خواهند گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653985" target="_blank">📅 12:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653984">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qur8LRpv8HDquRF5Nex4z1aWkiTSA7sAVRCEURCcaUV0RuYUqnZ_rAKCq7CKfk6UbYlulVlwm57eaxzOX4uYGUtAKVPQIyZzPt1DGY-9EhOTE51sRDis4xHdAG4ygwMWP5-xjBDYp6HH46M6PYtETQvgt-pzRqDVZRF3hfCoAZIlKbFnMZcBteguAa8VMk10bVhyZa_HoUJEDrbsPMBU9TKPTzrvitYpz3TGv0Gh2F7EJqrqmsp_N2KylfsTBEGhcLjyxkfC-9uvqZTEPlFYrwxik1UvFkinbMRZrF0JmdTrEzwPyIgejWCpNaGov6GXLfKUYU_3DtXhkewmBizlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رژیم صهیونیستی، سناتورهای جنگ‌طلب آمریکا و گروه های تجزیه طلب و تروریستی دنبال تخریب توافقند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/653984" target="_blank">📅 12:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653983">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
تصویب مصوبات جدید در خصوص وضعیت اینترنت
🔹
در چهارمین جلسه ستاد ویژه ساماندهی فضای مجازی، مصوبات مهمی در خصوص وضعیت اینترنت کشور مصوب شد که پس از تایید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات و فناوری اطلاعات ابلاغ می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/akhbarefori/653983" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653982">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP8pt2eDOnG9WeLaOwv3kwlE0MHkPh7Fm-JCC4-9Yi-SBOFo7BUuUBzAAwgEjAqxgmEsqDLLVLtJiiDQBLMfVqGTTJPk71AH_MEUcl5hRFOgQlobcRwJ04dXDhnIhBXJO202RxfmXLaRoTbTai5bXBz8oOVXFg3axYNZFkn_pfTcHM4PyRvSz8ASJKTTnfN5nVKVJoclJylLKlC1cg5VidhIxZYEK7nhS_RCwEokovlwynwv1XdfrEgGIBAyoEBS-OtzciKDG6a-HDHGhAKGeWXIoZ2iSwUFTtPiIYv2m1JB6x1uTQ7V1AiUHQ2tjtb-5Ka8lTY9nXGLzrFT0PnM9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خنثی‌سازی بمب سنگر شکن ۱۰۰۰ پوندی در چگنی
🔹
سپاه لرستان: بمب سنگر شکن ۱۰۰۰ پوندی از سری mk در ستاد فرماندهی انتظامی شهرستان چگنی توسط متخصصان و مجاهدان گمنام یگان کشف و خنثی‌سازی سپاه استان لرستان صبح چهارم خردادماه خنثی‌سازی شد.
🔹
به سبب عمل‌نکردن این بمب در مجاورت یک بیمارستان و یک مرکز درمانی، فعالیت این مراکز در روزهای گذاشته با اختلال مواجه شده بود که با این اقدام ارزشمند رزمندگان یگان کشف و خنثی‌سازی سپاه حضرت ابوالفضل علیه‌السلام، فعالیت این مراکز به حالت عادی خود بازخواهم گشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/akhbarefori/653982" target="_blank">📅 12:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653981">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249b96e72b.mp4?token=RIxmt7D6Su7_l8DhGv7qKdwJjS1LOOk5fgJtjpIPMChcq2s49pVyrNWFNBfWfBkYaCxI_rDNPQRnNCK84SFvSlpHrKvUy-MOeXYW9uaW1UyASzlxp1emLejtdIGaBxmt6xIWbeGOpJbnjHBfCcITvveUWbcdqHlQz_t5eHrBJQ29uoGZxkfysI2WNhB2DjVUzYbrLKLyWfPCcEnG4kMFP1HklqUcwgsoiTNwIGbJCiCVNiXY1XRpE46qPaAnsRS0kFJ5jZInHLXJ2KWCLgVtVETyp-yZSAFaU_qTbvyRJNDi-I-P2xzuVNmA14uaG01Lwiu_ul7qOp1uMIQvSXpHkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249b96e72b.mp4?token=RIxmt7D6Su7_l8DhGv7qKdwJjS1LOOk5fgJtjpIPMChcq2s49pVyrNWFNBfWfBkYaCxI_rDNPQRnNCK84SFvSlpHrKvUy-MOeXYW9uaW1UyASzlxp1emLejtdIGaBxmt6xIWbeGOpJbnjHBfCcITvveUWbcdqHlQz_t5eHrBJQ29uoGZxkfysI2WNhB2DjVUzYbrLKLyWfPCcEnG4kMFP1HklqUcwgsoiTNwIGbJCiCVNiXY1XRpE46qPaAnsRS0kFJ5jZInHLXJ2KWCLgVtVETyp-yZSAFaU_qTbvyRJNDi-I-P2xzuVNmA14uaG01Lwiu_ul7qOp1uMIQvSXpHkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت اعضای ناوگان صمود از ۴ روز جهنمی در اسرائیل
🔹
پس از اینکه دهها نفر از سرنشینان ناوگان صمود از کشورهای آلمان، ایتالیا و فرانسه از شکنجه و آزار جنسی خود توسط نظامیان اسرائیلی پرده برداشتند، اکنون سرنشینان استرالیایی این ناوگان نیز روایت‌های مشابهی بیان کرده‌اند.
🔹
برگزارکنندگان «ناوگان جهانی صمود» اعلام کردند برخی از بازداشت‌شدگان پس از آزادی به دلیل شدت آسیب‌ها و جراحات به بیمارستان منتقل شده‌اند.
🔹
«جولیت لامونت» فعال استرالیایی و مستندساز، در گفت‌وگو گفت: «این فقط آغاز چهار روز جهنم مطلق بود. من به چشمان بی‌رحم‌ترین انسان‌های دنیا نگاه کردم و هیچ چیزی در چشمانشان ندیدم. باید جلوی این افراد گرفته شود.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/akhbarefori/653981" target="_blank">📅 12:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653980">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRvD7QREXksB7hXYOsCAqG4odU1PpCQ0GCBVm30uv7S-94DSPqVPdC0ZlFKF5bhuofdQJqtYI9LUu8WpTZyMUg99rlOqXlMKc7x5aVMJXisJ0OL4cfs252P6BLBjMW4ZzeisFobNnxO2b2SrDiBth-DFL0qj-VSiaIBC5y8GWvEzw6E9zkyXWIqGLMvpPd_2Gpjd0fQ33Qctv4oPM6LTiR7eZ-NAjc1Z16qOQZZ5OioY76cyMmnU_WDCAg9AYN3Ww-kZZP2l25AU8EpVyOJL5B0H8T5qr9hiTZwc0xfXlIVnpJPXYx6nc_X9i_zgttdzDo9b30lfl1S_zTFWcO9A9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: ایران زیر بار زور نمی‌روند/ اگر توافق می‌خواهند مذاکره کنند، اگر بنزین ۶ دلاری می‌خواهند بایستند و بلوف بزنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/akhbarefori/653980" target="_blank">📅 12:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653979">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تشکیل جلسه ستاد ویژه ساماندهی و راهبری فضای مجازی کشور
🔹
چهارمین جلسه ستاد ویژه ساماندهی فضای مجازی به ریاست معاون اول رئیس‌جمهور و با حضور اعضای ستاد برگزار شد.
🔹
در این جلسه مصوبات مهمی در خصوص وضعیت اینترنت کشور تصویب شد که پس از تایید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات و فناوری اطلاعات ابلاغ می‌شود.
🔹
اخبار تکمیلی به‌زودی اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/akhbarefori/653979" target="_blank">📅 12:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653978">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4jluRSQfrP7MMHV8W_mjJ7GvUILp90soyqbRrgT5V1f7R-Z_CVg8gx2I5YPGDE1FBlD7-mqE80AsYR_DOhq8rfN-glE9T7XUbUg1mKSk5N7OgZncAD0NHoZbMfmuyNi26Em6nHQSq3FR_3CQU-qMXG-IrWj8fLc4sjn9J1nKtdY1SkEOIy6iSUb4-veaMqFlPW3UeglHeaslkaEZOJn6L1C5g0iRlKQWMF-eU3O_qhTEzEeEpeKsu4uzVfL-iI1WLRYAYX7icIYyFD1ErICeUBV7Heum0LC9oAmlQIUx7l9yj6F1xd1v2W5TVkm62QiEGOlA8XcdOSLMdTp8SGe6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقابله با رانت و قاچاق مطالبۀ رئیس‌جمهور از اتاق بازرگانی
🔹
پزشکیان در نشست با اعضای اتاق بازرگانی، مسائل و موانع موجود در حوزه‌های ارزی، انرژی، تولید و تجارت را مورد ارزیابی قرار داد و دستورات فوری و لازم را برای تسهیل فعالیت‌های اقتصادی و رفع مشکلات موجود به دستگاه‌های ذی‌ربط ابلاغ کرد.
🔹
رئیس‌جمهور: دولت خود را موظف به پشتیبانی از تولیدکنندگان، صادرکنندگان و کارآفرینان می‌داند و در مقابل، انتظار دارد تمامی فرآیندها با شفافیت کامل انجام شود و زمینه‌های رانت، فساد و سوءاستفاده از بین برود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/akhbarefori/653978" target="_blank">📅 12:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653977">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
رئیس پارک فناوری اطلاعات و ارتباطات: دسترسی به اینترنت بین‌الملل تا هفته آینده محتمل است
🔹
مصطفی مافی، رئیس پارک فناوری اطلاعات و ارتباطات: اگرچه با هماهنگی نهادهای امنیتی بسیاری از شرکت‌های فناوری با دریافت ip ویژه حمایت شدند، اما به نظر می‌رسد محدودیت های دسترسی و اتصال به اینترنت بین‌المللی تا هفته آینده رفع شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/akhbarefori/653977" target="_blank">📅 12:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653976">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86d693271.mp4?token=gk2thl5j6us3aV0jVXpCafQBYuJISDHV6eD8wO8DKTrxIElR0jOKmOpeiqWgaHm6geDGr5YcVew88DaEdbNqY2E8PGCYwn1ZGs9BVuBiGtK_9zbQN-8EXe0LZ3OHqvW_45pe6Kqy9UieWoQKao3SmTogCByS5QBO1j6V4X2XtdJqPl682GbGIATiZnbZq1BtMTnMACO6gaueGlB0achetJq6Yc51nuA5zA9DDmhPLsLLdpTJ_fyk_WAyPnh-Z-7CCULTd8OWJHTUllu4ON9D21LIeQquXWUEfsbAkVaSqbiqDeJmwlY5KHO0eUOMzO7FWNW0-miV_ZPVe7SpKJfExA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86d693271.mp4?token=gk2thl5j6us3aV0jVXpCafQBYuJISDHV6eD8wO8DKTrxIElR0jOKmOpeiqWgaHm6geDGr5YcVew88DaEdbNqY2E8PGCYwn1ZGs9BVuBiGtK_9zbQN-8EXe0LZ3OHqvW_45pe6Kqy9UieWoQKao3SmTogCByS5QBO1j6V4X2XtdJqPl682GbGIATiZnbZq1BtMTnMACO6gaueGlB0achetJq6Yc51nuA5zA9DDmhPLsLLdpTJ_fyk_WAyPnh-Z-7CCULTd8OWJHTUllu4ON9D21LIeQquXWUEfsbAkVaSqbiqDeJmwlY5KHO0eUOMzO7FWNW0-miV_ZPVe7SpKJfExA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین شعارهای ضدصهیونیستی در برلین؛ ۳ هزار معترض به حمایت از ایران، لبنان و فلسطین برخاستند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/akhbarefori/653976" target="_blank">📅 12:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653975">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f516eaef.mp4?token=oS0jNhyb2J42OcqAYhfQ9JY4HpFA9hgocxKj1mLVBggargNsLan62LTVXYqtOzdVaW0ZVLLY-zR_MchD2ZLedO3YKCDsPkh9CgiEFyxmK3V9K-8w1TjETm8cHF44A5A5TqaDyqRTxSW-03Uk7pCiklGA2UdLXc9GMYgKVvJLH-Wp7Z_ux90pJje_lpEhSLDjDL1qim5PA0OAUGCuHm0wHWQRN1cYFwyF81ksFDhhnTaklRKJXhZuAZisw7YZgdAxktHy2T2tmyPLT0hoZE5hvoy3QSM7KKmLwyaOOYsPqHWA9tpAbNpEQPRfdtOK6I_OHx_AhL_oc8cJgKQe3hIHZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f516eaef.mp4?token=oS0jNhyb2J42OcqAYhfQ9JY4HpFA9hgocxKj1mLVBggargNsLan62LTVXYqtOzdVaW0ZVLLY-zR_MchD2ZLedO3YKCDsPkh9CgiEFyxmK3V9K-8w1TjETm8cHF44A5A5TqaDyqRTxSW-03Uk7pCiklGA2UdLXc9GMYgKVvJLH-Wp7Z_ux90pJje_lpEhSLDjDL1qim5PA0OAUGCuHm0wHWQRN1cYFwyF81ksFDhhnTaklRKJXhZuAZisw7YZgdAxktHy2T2tmyPLT0hoZE5hvoy3QSM7KKmLwyaOOYsPqHWA9tpAbNpEQPRfdtOK6I_OHx_AhL_oc8cJgKQe3hIHZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: حتما بخشی از پول‌های ما خرج موشک و پهپاد می‌شود/ اگر چنین نمی‌کردیم دشمنان ما می‌توانستند به مطامع‌شان برسند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/akhbarefori/653975" target="_blank">📅 12:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653974">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiKZhnD1CeHeTmXdd4bcD0TbgTHcFXAiURQ1-yfUUvsXxqHEpcPYrUvwK4lEIRY9sl8Ji_nph1vqEdqyOWMaYXcG85Bbbe2Mte_Whhs8b-ToURDHnu9uhJ2IOJ-4j4PWw9otgKihOSJ7SN1bsbUvnlxx6n1P1vaijVBNv7QnoLs1THbV7Ec4W0nC3rGq2voud5u3pCDJKoEid_4scXxfdTxHp-juryRRy7UaXVPs16KDbssvAQmRpKuZLOVOm8j_b1jjrKkCPVHh44b7mYgsRUF0Kf_9tO3k7gFrMbIGnnuwfBF8Bv728djLIh2Fr2AgjLTh_z1glX39jPhNVPO9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک مرکزی: برای کنترل رشد نقدینگی سپرده قانونی بانک‌ها یک و نیم واحد درصد افزایش می‌یابد
🔹
همزمان، بانک مرکزی حمایت هدفمند از تولید و تامین مالی بخش‌های اولویت‌دار اقتصاد را دنبال می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/akhbarefori/653974" target="_blank">📅 11:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653973">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
فرمانده قرارگاه خاتم: سامانه‌های جدید پدافندی به کار می‌گیریم
🔹
دشمن بار‌ها مدعی شد که بخش نظامی ما را در حوزه‌های دریایی، هوایی و موشکی نابود کرده‌است؛ ولی همواره ما در صحنهٔ جنگ نشان دادیم که همهٔ ظرفیت‌های ما باقی مانده است. ما تا آخر با دشمنان مبارزه و شکست را بر آن‌ها تحمیل خواهیم کرد.
🔹
روند ارتقاء تجهیزات ما به لحاظ تطبیق با شرایط روز، مرتباً درحال پیشرفت بوده و این موضوع در میدان مشهود است.
🔹
پدافند هوایی ایران در جنگ تحمیلی سوم به‌مراتب بهتر از گذشته عمل کرد؛ ان‌شاءالله سامانه‌های جدیدی را به‌کار خواهیم گرفت تا بیش از پیش با حملات هوایی دشمن مقابله کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/653973" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653972">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhkfXLMPNNKd4sdnSYT931M5gB-UScmsq1cjeQ-Coks5NyupDP4yLqzaLEO6fg1lBSfNa6C4rT6Xw_bU9EeFroV5YrHmhMmtm_PpPMEJMU5bWArGMYpC16aen6pz-1mMaA3MZVT4fMh0w2-ZPq8zBt4P9AyL6P_L1a6oApXkgjlvmfXT1QkwSjfcxhGPK-ZzaDY8EtFSV6Xh69bPJfqLAExDr7J8atcPXFfedMPVg6ALqbZtEQHkU5ecoDfAT0YRNGiesG0FfEOjt0lvYin5km_SVjxXkNdaX-l2dhXIM4HZLXTpapHVNksWN7Ma7YtGe_sWCrD2BHh1Z-bKgYjBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا دبه کرد؟ روبیو: اسرائیل حق دفاع دارد
🔹
در حالی که به گفته مقامات ایرانی، آتش‌بس در تمامی جبهه‌های جنگ به ویژه لبنان در تفاهم‌نامه بین ایران و آمریکا مطرح شده است، وزیر خارجه آمریکا در جدیدترین اظهارات خود گفت که اسرائیل حق دارد از هرگونه حمله توسط حزب‌الله جلوگیری کند.
🔹
مارکو روبیو در پاسخ به این سؤال که آیا اسرائیل طبق توافق، به لبنان حمله نخواهد کرد، گفت: «اسرائیل همیشه حق دارد از خود دفاع کند. هر کشوری (رژیم) در جهان این حق را دارد.»
🔹
وی ادامه داد که «اگر حزب‌الله قصد داشته باشد به سمت آنها موشک پرتاب کند، اسرائیل کاملاً حق دارد که به آن حمله پاسخ دهد یا از وقوع آن جلوگیری کند.» به نظر می‌رسد که روبیو با این اظهارات، این موقعیت را برای اسرائیلی‌ها فراهم کرد تا به بهانه حمله پیشگیرانه، حتی در صورت امضای توافق آمریکا و ایران، همچنان حملات خود به حزب‌الله و مردم لبنان را ادامه دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/akhbarefori/653972" target="_blank">📅 11:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653971">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a012e51993.mp4?token=rjsdEf4q0SmpX1UQbdVVfnxB-9lRNvvhzDGbk445_T8gUmW6fYLqvxc7LWpu_kh0yfHtrEzxj5NkniihEG0UqNWMfPh8THQvB7DP6i_1Rr_u-RYbKY412HLjwj6L9KL1qh13oGf5qtMz7KwoMUlEPul0NzJd-0FGDpE4nPdznzRczygvP6EZZVfQ1PBGQoaeiQhKle0RjtgoSRbSgYPQkA6G3ekD5qjRNtOxAj2JsYEFXMfI8jO5A8tXk4QdDY3RmeX04WrVDMVuN-m5aeaRSwlrAkNES64Xpoy9gU_HJz8PZ0kqGKXrMHlkN3oEGCRKwzijKIfJvTvd8UzkAWldOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a012e51993.mp4?token=rjsdEf4q0SmpX1UQbdVVfnxB-9lRNvvhzDGbk445_T8gUmW6fYLqvxc7LWpu_kh0yfHtrEzxj5NkniihEG0UqNWMfPh8THQvB7DP6i_1Rr_u-RYbKY412HLjwj6L9KL1qh13oGf5qtMz7KwoMUlEPul0NzJd-0FGDpE4nPdznzRczygvP6EZZVfQ1PBGQoaeiQhKle0RjtgoSRbSgYPQkA6G3ekD5qjRNtOxAj2JsYEFXMfI8jO5A8tXk4QdDY3RmeX04WrVDMVuN-m5aeaRSwlrAkNES64Xpoy9gU_HJz8PZ0kqGKXrMHlkN3oEGCRKwzijKIfJvTvd8UzkAWldOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: قطعا بخشی از پول‌هایمان را خرج موشک و پهپاد می کنیم که اگر این کار را نمی کردیم، دشمنان می توانستند به اهداف شان برسند/ پل ها و نیروگاه های ایرانی خار چشم آمریکایی شده است
🔹
سخنگوی وزارت خارجه در پاسخ سنگ های میناب از شنیدن سخنان وقاحت آمیز مقامات آمریکایی، کهیر می زند.
🔹
بعد از ۷۳ سال اقدامات علیه توسعه ایران، باز دم از دلسوزی برای مردم ایران می زنند.
🔹
آمریکایی‌ها در ۴۰ روز تجاوز نظامی به ایران، فقط زنان و مردان و کودکان ایرانی را هدف قرار ندادند، بلکه به تاسیسات زیربنایی ایران حمله کردند.
🔹
آیا صنعت فولاد و داروسازی ایران با پولی غیر از پول مردم ایران ساخته شده بود؟
🔹
لفاظی‌های آمریکایی ها، برای فرار از جنایات چند ماه اخیرشان هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/653971" target="_blank">📅 11:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653970">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIqdQr7tVa6DP1RmhOfdnp6MMDniQC18B7sVC34i3_e7eMgLYmc5H5osgdVIo6btAxgXFrqCTAbBK-h7qoAfmI0BPSAJAl78kiYXHQ0UNfRjvX9ZJKARZQMHBsWxkABjRMnJGEMOAa3QcR0U6w4oK3TG1dLDdhtjOPSG02dD0CHcZCjZat9u8lvSvCUiN0BlTa8w7IUli9ChtOnfcdWRxQKOIUQrl9u_tWuIPDEg5aZ9vVITyqgGiZ3jzdQJInk5mgLneCsGaIk50raI1KJL23eKYho4BuwThEGWMx5SDiOttqov1vXvwuZOWMG8AQCY6hlVvvzo-z-xouEOX9ZCiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده قرارگاه خاتم: سامانه‌های جدید پدافندی به کار می‌گیریم
🔹
فرمانده قرارگاه مرکزی خاتم‌الانبیا در واکنش به ادعاهای آمریکا درباره توان نیروهای مسلح ایران، گفت: روند ارتقاء تجهیزات ما به لحاظ تطبیق با شرایط روز، مرتباً در حال پیشرفت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/653970" target="_blank">📅 11:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653969">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: بسیاری از کشورها در تماس‌های دوجانبه با ما، به شدت از وضعیتی که ناشی از اقدام آمریکا و رژیم صهیونیستی است، ابراز نارضایتی می‌کنند و از اینکه یک ساز و کار مطمئن و پیش‌بینی‌پذیر برای مدیریت تردد در دریانوردی تنگه هرمز ایجاد شود، استقبال می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/akhbarefori/653969" target="_blank">📅 11:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653968">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
موضوع توقف جنگ در همه‌ی جبهه‌ها در پیش‌نویس اولیه توافق احتمالی لحاظ شده
🔹
سخنگوی وزارت امور خارجه در پاسخ به پرسشی درباره لحاظ شدن موضوع توقف جنگ در همه جبهه‌ها از جمله لبنان در پیش نویس توافق اولیه با آمریکا، آن را تایید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/akhbarefori/653968" target="_blank">📅 10:59 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
