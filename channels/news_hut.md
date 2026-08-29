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
<img src="https://cdn4.telesco.pe/file/W3ciE8AV0pkbirl9eXVsxWBWZUYrlKYbzvSXY8BN7gA6vvKXo1_7qz0Iptan7W2rIWA4Ml5MlP1OclZJlbEc2k5Twkg9me-6N-id8Uds314pf7Ga3SPxhul9-YYvbZ9Yuf5o33lGwlcs__rnTJo5JVNSm3E8RRR4hucBdKo1_LwRhJGIUzx3w3TuDjsoXG__p62I7qzdDw7Pq-wgHenCvfUjmZHUZKAuX8iYYuDsjfDJxB2h6ErpPzUZ9sqpVPVPoxouNqdPZXvZjPTSUPCwM7T49xlLao4KwWb6d_RJMUVS9NWWS_KJi1lI05dOrHExTRSYMZ7guKfqWLUCDkc4Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 116K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 14:44:54</div>
<hr>

<div class="tg-post" id="msg-70753">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=LrqgDbIBzJqPSy1xLbftRhLIs4obl5mBj30IENv11-8TsFelhozrLplYnZ2pcDgWSTAMPJAgayMoO0I39vkdP55pfbs3xuZY2ZudnQsrLBKrbjWFXCM6h3L61I0fjWmFQ7LVKq-KDSkCVlT8YpJw1lCcgaF4rcm-1FGsIuuHnSNzOHTp_AUY2ltXwoZKDcDzpH8zqq1_t2tvqT9mtpSyFaJ11n3MNzZmugbOwap-v70HD-fA4cnLzsoS3ZGLO1qFv1xCj4109YRT2q9QnscdG3n-3ELOVoxyIl2ni_G0IRBJrnITTfTeRShyiuJZywadJxguoOqs_swqc8BBFf-8PV4uDFYayLLsZWoU9lbzTicqh7bbIJgD_cXZdcw8V3FQxGo0RRRoGQumlrmtMEi7p-5SKK5sY-gHSD-ZXhzZqct6sc2YG4eUCvWMixPw-YgJSmPfNEdtRv1lS3SenmEYUG-NrVRtvrFnL4lvP-DZvqixBSpK9zS6WkiYEoq-rxXdvafzpKvfb5llN_tA4GQoIrTh3QYHnTKHbtc6eQC54woB_R8nEqPOlRy5MpUrj6gYNqhomIS_wZyqD3TTd844K-n9LJW-kcKOg4Yv2NJXl1lU0pQzIEvbGFSXR5-IhUHPW4lgYtL7DvZMK6-alOQSwgqYPNL31yFDJXxGbYIeMAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=LrqgDbIBzJqPSy1xLbftRhLIs4obl5mBj30IENv11-8TsFelhozrLplYnZ2pcDgWSTAMPJAgayMoO0I39vkdP55pfbs3xuZY2ZudnQsrLBKrbjWFXCM6h3L61I0fjWmFQ7LVKq-KDSkCVlT8YpJw1lCcgaF4rcm-1FGsIuuHnSNzOHTp_AUY2ltXwoZKDcDzpH8zqq1_t2tvqT9mtpSyFaJ11n3MNzZmugbOwap-v70HD-fA4cnLzsoS3ZGLO1qFv1xCj4109YRT2q9QnscdG3n-3ELOVoxyIl2ni_G0IRBJrnITTfTeRShyiuJZywadJxguoOqs_swqc8BBFf-8PV4uDFYayLLsZWoU9lbzTicqh7bbIJgD_cXZdcw8V3FQxGo0RRRoGQumlrmtMEi7p-5SKK5sY-gHSD-ZXhzZqct6sc2YG4eUCvWMixPw-YgJSmPfNEdtRv1lS3SenmEYUG-NrVRtvrFnL4lvP-DZvqixBSpK9zS6WkiYEoq-rxXdvafzpKvfb5llN_tA4GQoIrTh3QYHnTKHbtc6eQC54woB_R8nEqPOlRy5MpUrj6gYNqhomIS_wZyqD3TTd844K-n9LJW-kcKOg4Yv2NJXl1lU0pQzIEvbGFSXR5-IhUHPW4lgYtL7DvZMK6-alOQSwgqYPNL31yFDJXxGbYIeMAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از شیرجه زدن تو استخر یه پیرزن دزفولی 85 ساله در بانمک ترین شکل ممکن
@News_Hut</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/news_hut/70753" target="_blank">📅 14:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70752">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDl7C-LJkbnvGt-r4FiAWmycU3aoOxHuoQjHHUCpl24hFvNCAeB_Y0oF1d24fzEnm5G98U2_2oCGArbfqqJJ0MO-UvQ453_C9aUtb6fQFy_P_9pqzc-T7kFNg5cPPLUHImmr9g9Gbbc_Py39Mm3eG5SbrnZdC6ZeGrif9UK0riueeVqU9vRTtnyEnj1CGJW3zn8S0JYuOC1jFpM_Tvoyfcxlpa9T08TNm00-J4La3x-OEZUOH4W5cuZk2tXiYVEyxYDJRGC43AhQlerRkNp8JmXM6K1kMSx2-q8U5ok6RTXz182Cw61Sptwjc85BORPwGSlIiODq6TSn8b1TXUXjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بنر یک عرزشی در تجمعات شبانه:
آمدیم امام زمان را بیاوریم
مجتبی خامنه ای رهبرمان را هم به غیبت بردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/news_hut/70752" target="_blank">📅 13:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=azm1_wid_fXnrvrVQA_1jDVquKbmQkSvtPMZrHX95P-vGrbGkibK0wxSDMmQatTvh0eBpeBRXfz2wsSGDvEY3VUl8ckakLxSVVqvzNuXiJXLZdfXsulrIUHx1GgfOMuJbaTJL5B1timA_j0UbpcYwvQd4uzStYhSf_ybO0ew10yESbI0ettRKJtrrINzY7zb0_9AtbKOPjpRlUFBIox8WiW4Uc3Kw3YcEGZq82V1IFH8dKtYQgAYSJ8TI96-1Zl7ruxZ6Wib8AS1WVH9p9CZFrNW4B3ydzOpWMpE0aQrdaZiWzcbVNr8XvRZuBJyuwFlJwrvDhgd6sMqOYQnj-jFmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=azm1_wid_fXnrvrVQA_1jDVquKbmQkSvtPMZrHX95P-vGrbGkibK0wxSDMmQatTvh0eBpeBRXfz2wsSGDvEY3VUl8ckakLxSVVqvzNuXiJXLZdfXsulrIUHx1GgfOMuJbaTJL5B1timA_j0UbpcYwvQd4uzStYhSf_ybO0ew10yESbI0ettRKJtrrINzY7zb0_9AtbKOPjpRlUFBIox8WiW4Uc3Kw3YcEGZq82V1IFH8dKtYQgAYSJ8TI96-1Zl7ruxZ6Wib8AS1WVH9p9CZFrNW4B3ydzOpWMpE0aQrdaZiWzcbVNr8XvRZuBJyuwFlJwrvDhgd6sMqOYQnj-jFmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مجتبی خامنه‌ای:‌
به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛ مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه.
🇮🇷
پزشکیان بعد اینکه مجتبی خامنه‌ای گفت "دولت نباید ضعف‌ها رو علنی کنه" :
واقعیت اینه که ما پول نداریم، درآمدمون کمتر و مشکلات‌مون بیشتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/news_hut/70751" target="_blank">📅 13:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70750">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXhG_4bmQI130SoVlqIokrNj0sSmDpQG6yOxQ3C44PMpsB9jVpXW92bUe7wLlun3bh061nIq2bAq5HO8snf1836ZpGJmjIL8uBYd4vo1ctZeeKBPwwRbnBI5s-vjNoy4KfpAdHK022prQEJUWVDSWaYOqIjZuaqiJ-XJ-PaiVcdttC0HzE6SJLHA0WF8oqK0w6JK5ojgXWdqyRLKPjObugR9M0BoEeCkBNYZS09NpRrdUIBX0d35k5VSQkD1FyiePbEX4ssZ-ZPt0w2aaKGD8S_NIDb7eeOy32ZWbSUyYDiGBMPKwte6ymMcSx5jpTVbfJwOPE6hSeGdhsZvVJQ-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
گلدمن ساکس:
صادرات نفت خلیج فارس به سطح ۱۵ تا ۱۶ میلیون بشکه در روز بازگشته است که حدود دو‌سومِ میزانِ پیش از جنگ محسوب می‌شود.
نفتکش‌ها به‌طور فزاینده‌ای با خاموش کردن سیستم‌های ردیابی («رفتن به حالت نامرئی») و استفاده از روش انتقال نفت از کشتی به کشتی، سعی در دور زدن اختلالات دارند؛ اقدامی که به کاهش قیمت نفت از بیش از ۱۲۰ دلار در ماه آوریل به حدود ۸۹ دلار کمک کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/70750" target="_blank">📅 12:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=hsNYY2iVP0J6eJCuQtDi8Qsq6J9dqT_fvQtzLeYbfMkKCcGCSB4m0odltWm2UA-JviYqecNgm_soZVtyyOuCrCxRJUAS7GDwPPknW9oKNaotstyKh295rO38Wfn_crQk4OXYmwjbCklFD7EwYTgGBovzY1G-t-77lcSeT7rivndhaCKGMFfTuFa7L3EMPdg1Wqmo1M1TU1cSf-hv6EkQspHa99anRRe6BAfPGP8dbntYAzIcRi9-NNok0xrYsXw6h4CEZEtE50v3asV03ossvUGNRgL-zk8OqDIjlpLEmFiSINsABXOK15wwNUj-tCc6GB9Co8hb6bNCNi7JeHYW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=hsNYY2iVP0J6eJCuQtDi8Qsq6J9dqT_fvQtzLeYbfMkKCcGCSB4m0odltWm2UA-JviYqecNgm_soZVtyyOuCrCxRJUAS7GDwPPknW9oKNaotstyKh295rO38Wfn_crQk4OXYmwjbCklFD7EwYTgGBovzY1G-t-77lcSeT7rivndhaCKGMFfTuFa7L3EMPdg1Wqmo1M1TU1cSf-hv6EkQspHa99anRRe6BAfPGP8dbntYAzIcRi9-NNok0xrYsXw6h4CEZEtE50v3asV03ossvUGNRgL-zk8OqDIjlpLEmFiSINsABXOK15wwNUj-tCc6GB9Co8hb6bNCNi7JeHYW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روزی هست که اکسپلور تحت سیطره این بانوی بلوند ایرانیه؛
و خیلی‌ها از ایشون با عنوان "قرمه سبزی جاافتاده" یاد کردن...
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/70748" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70747">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70747" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/news_hut/70747" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70746">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9FbQzYNwPvLp6hdzYk0kBbR5zYtNlNsyTI8j0wyGB2KDmZzUdOhibqb519xnwcjNc2yLDyDNvPGL6vgQHuvetkR2CNz9zqxwLvHy8KIDcWiRaNBJKtsEf8MZOcUJkbc-CX1o7HghQHEh7tcL6f8bRXjJNeLPUXp_n-x2L8jvhQxE552lKw_EiXH_cMVXqTM_wloS7RdJtcCjkhcjFzw4XLb-gO6ipFfiejzHuaEXAzxZepbBbmvbAz4hGJ0mPZAvlkSVNc5nbc4_d-nHSjwTOKBS2EPCchajnsY3Iws7sLTLltvX2NGIGGzIr0NGjprSHXSnISI5Y8nTpoOKGa2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
پرسپولیس
🆚
ملوان
را در سایت بین المللی
TrexBet
پیش‌بینی کنید.
🦖
دوشنبه ساعت ۱۹:۱۵
🦖
استادیوم شهر قدس
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر:
ملوان: ۱ برد، ۲ تساوی، ۲ شکست در ۵ بازی
پرسپولیس: ۲ برد، ۳ شکست در ۵ بازی
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/70746" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70745">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=buWAoLNT6-I6M_N8o7ZC7HcNJ37mg4xo5doPzudUac0-01fuaBPiBn6e7xfXNAluQAph3oEFbZFJSQtIjsaQ89C4ox9cqN6paXMNgeLM5TvkqnMsMOMx4T1Td5mJeesdKcZ-A3YXNQPNa4ZFylmc91bSlv8YAuPa_MserTIGJXxcLDT-RKNn7TDrWm-kST2CSFu9cXwytQntK2QGLVtdshvRUSTRxnyaiLIootphcPNftE9jpLT5Y87Kpou3fzXSiBCk62Bj6x6Wo7Eeiff8DhNXLvS1agMGS75D_Hqfi7pUgwBggcTzoaF4euUKRJRiRaqi9KaxQ2zGpmDVspqu5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=buWAoLNT6-I6M_N8o7ZC7HcNJ37mg4xo5doPzudUac0-01fuaBPiBn6e7xfXNAluQAph3oEFbZFJSQtIjsaQ89C4ox9cqN6paXMNgeLM5TvkqnMsMOMx4T1Td5mJeesdKcZ-A3YXNQPNa4ZFylmc91bSlv8YAuPa_MserTIGJXxcLDT-RKNn7TDrWm-kST2CSFu9cXwytQntK2QGLVtdshvRUSTRxnyaiLIootphcPNftE9jpLT5Y87Kpou3fzXSiBCk62Bj6x6Wo7Eeiff8DhNXLvS1agMGS75D_Hqfi7pUgwBggcTzoaF4euUKRJRiRaqi9KaxQ2zGpmDVspqu5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شعرخوانی محسن نامجو درباره علی خامنه‌ای و جمهوری اسلامی، شهریور ۱۴۰۱:
یک روز مار صدسرتان می‌رود به گا
آئین خوک‌پرورتان می‌رود به گا
سیدعلی اصغرتان می‌رود به گا
سیخ و سنگ سرورتان می‌رود به گا
@News_Hut</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/news_hut/70745" target="_blank">📅 12:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALuhG7RHUsoUUxnkdVMNU-5rmfn99FYMAn2AXFYWfJKWnvEcmSVE-c6HcJP4BUdQp4nibvdjB0HLKj9cIBm9dFuMC13ajzoF5i3GUJhREAbOCEVMjSFh-59D7Et_DcNSmAMJX5zAnLn-ymEHkRADJbjYZDjPfJv1mU5GQ_KdrX3aGlyu-onMloRIewr2Kjcs8QMrb9wZ7uw6PzpZcSUvb16YhL1lISO63NLCTf3bz9wZch_YuIbRw33mWAAgjF-lq1zDMCk0ca0MD6meAvMr7cCy6gYlQL_z4iiAIPOSqvtP4AsaFAtkSZQ5_8r9S4wHhLa293TZC5fLBEnjVSfs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:
به گفته مقامات آمریکایی، ایالات متحده مقادیر زیادی موشک و سامانه دفاع هوایی را برای جنگ با ایران به خاورمیانه منتقل کرده و برخی از ذخایر خود در اروپا و آسیا را در سطح بسیار پایینی نگه داشته است.
به گفته مقامات آمریکایی، پاتریوت، ATACMS و سایر سلاح‌های دقیق به شدت تخلیه شده‌اند، در حالی که رهگیرهای THAAD و سیستم‌های ضد پهپاد نیز به منطقه منتقل شده‌اند. تکمیل موجودی انبارها می‌تواند سال‌ها طول بکشد.
این کمبودها، فرماندهان آمریکایی را مجبور به تنظیم برنامه‌های احتمالی کرده و نگرانی‌هایی را در مورد توانایی واشنگتن برای پاسخ همزمان به حمله احتمالی چین به تایوان یا تهدید روسیه علیه ناتو ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/70744" target="_blank">📅 11:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=Ao_n1vzSQktOH9mwLMUBG06XkpqGlaCQuWCvdbgD_XoMLfBMFmOERpVvEI14nJkoWIgI59mUrfCuPKMFclH2syiYZFPiUzmWy5b7EqE_3hUjcdDXGv_ByALvxrzQ6OSATYvV-hd7yoDTzjJMUydIY3rFI-Ntl6GaOquqJL1ggKwqnXLbEjn7Wp98s7-9mz7VAr7QVqpDSNCIN2i26azyzIGhOMvyAzc2GDMRt0VtrS_AECtyc7KQ5K_nTXV6xckYHnrYzT6-jNDYLxs4KgITnrBKdqQjGK6enW9Leiz2ZnkRKniVWUf66g8iSytqnFVqe8pk069LaHuXzLduPp9Lgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=Ao_n1vzSQktOH9mwLMUBG06XkpqGlaCQuWCvdbgD_XoMLfBMFmOERpVvEI14nJkoWIgI59mUrfCuPKMFclH2syiYZFPiUzmWy5b7EqE_3hUjcdDXGv_ByALvxrzQ6OSATYvV-hd7yoDTzjJMUydIY3rFI-Ntl6GaOquqJL1ggKwqnXLbEjn7Wp98s7-9mz7VAr7QVqpDSNCIN2i26azyzIGhOMvyAzc2GDMRt0VtrS_AECtyc7KQ5K_nTXV6xckYHnrYzT6-jNDYLxs4KgITnrBKdqQjGK6enW9Leiz2ZnkRKniVWUf66g8iSytqnFVqe8pk069LaHuXzLduPp9Lgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک دختر ۱۶ساله رفته تست بارداری گرفته و تستش مثبت شده:
فقط لرزش پاهاشو ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/70743" target="_blank">📅 11:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70742">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=N3OTNUmcfTYoooauDFOiMVpuMvzIP3YMIe4mpVX4T18Ls9mBQZJifyIzocbvGF4J2tZcaK_M1dCanMc344ZS7R4bdBTgYG7QNirF_mp_mEW_vWMO2XwgZHf3EKzYl-aYdoUglY16zF6eCAMrrMhfcyz03YAapJ1XP6OU7EZvLLXySkB7jhemQFMo6lW_5UPxrznk9ynUkgiduXAkJrmZ_qbNkoDrVIcLI-I0_j8bb14zWxOB3I6DDt0-FFQ_zCBw_FpHGpcUhk8FtK_tbjSq77JWLnte8faapb05WLICG-i1A6a8jlbj0D1gAxsb0gauns02blOmFd_sgJQkOZMCVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=N3OTNUmcfTYoooauDFOiMVpuMvzIP3YMIe4mpVX4T18Ls9mBQZJifyIzocbvGF4J2tZcaK_M1dCanMc344ZS7R4bdBTgYG7QNirF_mp_mEW_vWMO2XwgZHf3EKzYl-aYdoUglY16zF6eCAMrrMhfcyz03YAapJ1XP6OU7EZvLLXySkB7jhemQFMo6lW_5UPxrznk9ynUkgiduXAkJrmZ_qbNkoDrVIcLI-I0_j8bb14zWxOB3I6DDt0-FFQ_zCBw_FpHGpcUhk8FtK_tbjSq77JWLnte8faapb05WLICG-i1A6a8jlbj0D1gAxsb0gauns02blOmFd_sgJQkOZMCVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آیسان اسلامی درباره شاهزاده رضا پهلوی:
طرف میاد میگه این که نمیتونه تو ایران نبوده د آخه خارکصه برای مسافرت که نرفته پدرشو کشتید
میخاید برگرده ایران بکنن زندان مثل تتلو عکس بزنیم آزادش کنید؟
سیاست مدار نباید مهربون باشه که انقد حرف بهش بگن
خارکصه ها خامنه‌ای رو دیدید؟؟ کسی خایه نمیکرد بهش پخ بگه بعد میاین انتقاد میکنید؟
خامنه ای خار روحانی خاتمی احمدی نژاد رفسنجانی (پدرنظام رو گایید)
خب دیدین که با رای دادن نمیتونین جلو اینا باشین چرا پس ۵۰ هزار کشته دادیم ما
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/70742" target="_blank">📅 10:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70741">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=owA4J1FMm_W60Xjinkt2nYEAX8ORVUtv0ZNYZY6TCH7ECasKm_TVT_ZNA74bqELdakCvWq4cGzx-JFpVeREPHCQiHdRVWgyD8aJjV__0ziQW4_yMgl551kzapXEH774VNnwc1T3GwmlcFGTJfNUQt60fWPAVyH6WHP7uX4yv05VfxXRMYTTRGro1OYip_tejU2A86ftoKAMDlTWhdmMJ7zKStzx-tPa3kC-L4-iP9iAicSBg_Ij1yFV6jxNbz7Z0wVpK2HaebyP_jqXQOZb9ycEbgK78LcVk49CZTkyCd7_DWYRfHcy8gjraoYBQDToCCHA3mcTn8ZExyp6SPiVJm2bgobIP3HNeAqgIgCoDokpaDS9RNHi4pEEmWm5XAKd48M3FzxdbbbwxB0N9275_3eMe-gI36NZ75GWidr4P5G3epnDLbrrF8LRC4CET-3SmKKOik7HpmwGkINQJmngWMUCikZg3yrQc82vLLpWc3B2nWxTIcN6pnxA9Af0cl6i3xmPMlHvsOb5WBHWF9w8CoRAWbl8OkJnwBPw1m7rIc9MNr2IoofceCtLIlCqbiyiH46wKTViIVCCx165FoSWy6GxilZXCvdj1zqd1VOjTsbkgS_tr-yMrN2_TeQVhDcbW3UlZs5Y2O20lGayi3zOYqmw6iNlV91m_Gxqi9-30XDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=owA4J1FMm_W60Xjinkt2nYEAX8ORVUtv0ZNYZY6TCH7ECasKm_TVT_ZNA74bqELdakCvWq4cGzx-JFpVeREPHCQiHdRVWgyD8aJjV__0ziQW4_yMgl551kzapXEH774VNnwc1T3GwmlcFGTJfNUQt60fWPAVyH6WHP7uX4yv05VfxXRMYTTRGro1OYip_tejU2A86ftoKAMDlTWhdmMJ7zKStzx-tPa3kC-L4-iP9iAicSBg_Ij1yFV6jxNbz7Z0wVpK2HaebyP_jqXQOZb9ycEbgK78LcVk49CZTkyCd7_DWYRfHcy8gjraoYBQDToCCHA3mcTn8ZExyp6SPiVJm2bgobIP3HNeAqgIgCoDokpaDS9RNHi4pEEmWm5XAKd48M3FzxdbbbwxB0N9275_3eMe-gI36NZ75GWidr4P5G3epnDLbrrF8LRC4CET-3SmKKOik7HpmwGkINQJmngWMUCikZg3yrQc82vLLpWc3B2nWxTIcN6pnxA9Af0cl6i3xmPMlHvsOb5WBHWF9w8CoRAWbl8OkJnwBPw1m7rIc9MNr2IoofceCtLIlCqbiyiH46wKTViIVCCx165FoSWy6GxilZXCvdj1zqd1VOjTsbkgS_tr-yMrN2_TeQVhDcbW3UlZs5Y2O20lGayi3zOYqmw6iNlV91m_Gxqi9-30XDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📱
این ویدیو تو اینستاگرام فارسی از شدت طبیعی بودنش شمارو وارد طبیعت میکنه و یادتون میره که این فقط یه کلیپ:
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/70741" target="_blank">📅 10:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70740">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=R7jlCDusNnw3g6UGRz5SoVsHDcV3YsR6t6vCGraMtvuF7S3JuYtOQAOwOoFfvecOfi0CbKyv_R6ZdyqzjJyEeQYHwTaeQow8DLL_Ee7HsMfZx972exDf3MH1gQAnwAKX4i8lUKkptLr7kDWwaa0Bbu7mMmViH-iE8uraBEXwNNzVIl9ekaILUuzpE7vYTEJQll5q0gggeQOlf0Y0OCQ1t-KR4NQScJoe0WdzjaZmotr74xM4wlF3Vn0v2qOL9zTzPYlagPj8kjJUHDpGT6fEjLg7nN1H71Un58mDZoUhOSEOgYpSbF2COpuIw0fatG2TzpnoSz7-KjsMI9tBl5XZ7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=R7jlCDusNnw3g6UGRz5SoVsHDcV3YsR6t6vCGraMtvuF7S3JuYtOQAOwOoFfvecOfi0CbKyv_R6ZdyqzjJyEeQYHwTaeQow8DLL_Ee7HsMfZx972exDf3MH1gQAnwAKX4i8lUKkptLr7kDWwaa0Bbu7mMmViH-iE8uraBEXwNNzVIl9ekaILUuzpE7vYTEJQll5q0gggeQOlf0Y0OCQ1t-KR4NQScJoe0WdzjaZmotr74xM4wlF3Vn0v2qOL9zTzPYlagPj8kjJUHDpGT6fEjLg7nN1H71Un58mDZoUhOSEOgYpSbF2COpuIw0fatG2TzpnoSz7-KjsMI9tBl5XZ7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال‌ شده از گلایه‌های مالی یه ستوان سومِ نیروی انتظامی:
تا صبح میرم گشت‌زنی و حقوق خالص من 21 تومنه!
با این حقوق حتی غذای خانواده هم نمی‌تونم تا آخرماه تأمین کنم.
به هرکی هم می‌گیم جواب میده که دست ما نیست.
من نه ضد نظامم نه هیچی، آقا به فکر باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/70740" target="_blank">📅 09:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70739">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8l84jHhem2V1LgwWIUWmgrPZZbV4megoqusE5tfb4Zi8IGms9VaYYyAs3TDvxuedGM8gB2veqOs-dtOP_caUwvBaopZ8W_IP4H6NjlbMbOEaQMz-7V4WkGUuOdb6bayjsKJy2cPihHFFW49aUHmqeo-vyrF_Boytstz81qlbq2c5KxwqGQOenPEtJ3zUtW9xqDbqfvcd5fCaCz4rlwoZMR0EJZa7k8vObyoMMKklvT5a0vH4sb5CajdeoVmvKNl3Hn0jF5m4WfkDQ62gKpy_w8q6AteQm0VDAvWIOSG7GBEPvpqDz1yqBl3VshgMYhgUjGtZue7bbD5mQQ200OFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
باراک راوید:
بیش از ۲۰۰ شیء شبیه به مین از مسیر اصلی این تنگه پاکسازی شده است.
مقامات آمریکایی می‌گویند تنها ۱۱ مورد از آن‌ها مین واقعی بودند و تعداد اندکی نیز به شکل اصولی کار گذاشته شده بودند.
تنگه هرمز باز است و آمریکا در «نبرد هرمز»دست بالاتر را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/70739" target="_blank">📅 09:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70738">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70738" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70737">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL6bikRQU5sagSvJ7gkzTMIaEcpmeK6Jg7TIfCG9ThA5lhO3o8KCDz-P2UMVEFUUegA13FBDk7ZvcbtG24H09krURJaZU8Szid_HqlWPxRVaM9nmfgZLderR-3sKv8I9fOnbzkNWaQ3FSJxSMyxKb1-HOFK_1DCRbSefM2hM8FRMYvPSeBt3xK0IeAkqBMHObl0X47wqq6ZAqDpQ6a08kl-Inm3KEz7_tCyfVm7b0tpVtMwE1BSdaj9YakcRBwBCjMl7ayxFf5FRIKmprGgrL1S6SdsipL5mjdb5MHyMx0p1yfENCIazMdySG1CYUgyCGOBDsT4tgllgi5VccieRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70737" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70736">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
ادعای العربیه:
شبه‌نظامیان عراقی قصد دارند در ساعات آینده به عربستان سعودی حمله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70736" target="_blank">📅 01:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70735">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRMTPorfJBPYx1kvegtNYB8U6QILwbcO8tsd50exh-jTI5YxcR-5W-YlCdLvtIVwQBYEAvLQv1WdIUiIZGwC3tRviyfO6s8lEHnAmWZcbHUEfNhuxHxE4FcF893ldhTzAUYHFIibJ-KydqZN-66erkpCFUPoSfPF_qSMM3feihFCotMB4JirlS1X-z4H-R8plhh3xW-JuEBk3u9GHd_2LblYxNLVnLLvP7A8SYiRn_oSMOum32Bm6EWpbuXvAcQOyy6z6u26pDDLqudidTLT1_SUiSLPzN0pbxMSfd_Dm6QGc48IBlBETysaa_DURcJaWH0nXaWjVTRlqc0duAX6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مجری:
غیر از قرآن و نهج‌البلاغه، کتاب دیگری هم مطالعه می‌کنید؟
🇮🇷
پزشکیان
تا دلتان بخواهد. فکر می‌کنید همه حرف‌هایی که می‌زنم، فقط از همین منابع است؟
🎙
مجری:
آخرین کتابی که مطالعه کردید، چه بود؟
🇮🇷
پزشکیان:
آخرین کتابی که خواندم «فراجامعه» نویسنده آمریکایی بود.مگر می‌شود کتاب نخواند؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70735" target="_blank">📅 01:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70734">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=PDindH9ekVsmIwCk810ORmkp3R7zIKKLuR_YziCC4PBnE3j3KBOeQtR0dp_z0Oo7xbFNp8AC5j3kny4V1aq_DczSGMDKDPUYVdTuw_8uE6f_ovvTqTVqe2glj4hw3NQUNt_zRV0wZxUVKekENpZj_IneddNzW7hda157gKmdZpszl48BQLvvmoiOsD-KznYrfwsrgAMSoyOLaqRsGVocb4mGdgbzL0K7pZHV-CpGUCSz27-n2M-4eHruaLS2uGkUfIoPOVfs05cIsQfCEKNGjSixSOhu4c7oaZhyZXwYxNKHNTw0iam4C1W2ET8hsdkziAQxEeieJNiSySmoyA0Weg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=PDindH9ekVsmIwCk810ORmkp3R7zIKKLuR_YziCC4PBnE3j3KBOeQtR0dp_z0Oo7xbFNp8AC5j3kny4V1aq_DczSGMDKDPUYVdTuw_8uE6f_ovvTqTVqe2glj4hw3NQUNt_zRV0wZxUVKekENpZj_IneddNzW7hda157gKmdZpszl48BQLvvmoiOsD-KznYrfwsrgAMSoyOLaqRsGVocb4mGdgbzL0K7pZHV-CpGUCSz27-n2M-4eHruaLS2uGkUfIoPOVfs05cIsQfCEKNGjSixSOhu4c7oaZhyZXwYxNKHNTw0iam4C1W2ET8hsdkziAQxEeieJNiSySmoyA0Weg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مسعود پزشکیان:
«زمانی که حتی پیش از وقوع هرگونه درگیری، با کسری بودجه ۱۵۰۰ هزار میلیارد ریالی مواجه بودیم... آیا این صرفاً ناشی از سوءمدیریت است؟ آیا این بدان معناست که مردم تورم را احساس نمی‌کنند؟»
«بدیهی است که ما در زمینه معیشت مردم مشکلاتی داریم. روشن است که... باید تا کنون میزان طرح کالابرگ الکترونیک را افزایش می‌دادیم. ما در برابر مردم شرمنده‌ایم.»
🇮🇷
پزشکیان:
«در این شرایط جنگ‌گونه و در این وضعیت اقتصادی
بگذارید بگویند
:
"من می‌توانم با همین شرایط و محدودیت‌ها مشکل را حل کنم"؛ آنگاه من دستشان را می‌بوسم.»
«نه اینکه به من بگویند "پول و منابع در اختیارم بگذار تا مشکل را حل کنم"
خب، اگر من پول داشتم که خودم حل میکردم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70734" target="_blank">📅 00:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70733">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MYbNatPLoAw2Iv4xQJmPmUDBqJEAy_cPfGKUBzJmjzUotckwRb5MsivU9TUbVp2d0KVR_0PBin9Zk2EeQtWjfOvmHJZF7JjA-WTxxWIXqnAtnZn7JkN0cwr8mxnyadXeNXAfi6qkZD5ihgD8cPDNJHqUjttrB9SXNiIACiFFcm_9zKPxNTxo253g1-HCM1Ue9qQBu5F_Lqk5FSZ16jq2qi5BRMg_ABP6WVjydBqByj1Nlq6Nk6y3vcZ1yLpgDFuzMBW5iIXw0SDO0Jm9c7b-TkWYBgyW-XQcFDD8O1dtmpPd-35cSBw5NnBl9vDp4MkLSZbW8wrryENfKJHySutrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇫
برای اولین بار تور افغانستان گردی برای مردم ایران موجود شد.
قیمت تور ۷ روزه‌، ناقابل ۵۰ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70733" target="_blank">📅 00:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=cXlkLvVlvWteOiEP-U_morUSEseQWifDYw_W9u9HXBU2Id59_aExhxU2XJk8l9GRHFvvriJk0Kg4aa44avCdA31kiO3R8-LSwaGRfkuAc96k9HSADjZ8eGmca89tR7pkyYIBWHMWlvDCqAeI3bjXeXugH7gLydMeINBkJw62x7QbimJy-J8y8pCG2FaXvOABmpSQsXvhB9MzsJJysxXdkkp8RUNggmuFtRpljmEelN9r2aZ6sF54WU1YHNoowxz9T4pKHDZHYLtrWKgN_ncaFQ4kCG_LgQijWzHNRSpq9DryTeY4DBZdxiHjuRzSDLsVKf8DmNMhKSw6bcYJ5yS8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=cXlkLvVlvWteOiEP-U_morUSEseQWifDYw_W9u9HXBU2Id59_aExhxU2XJk8l9GRHFvvriJk0Kg4aa44avCdA31kiO3R8-LSwaGRfkuAc96k9HSADjZ8eGmca89tR7pkyYIBWHMWlvDCqAeI3bjXeXugH7gLydMeINBkJw62x7QbimJy-J8y8pCG2FaXvOABmpSQsXvhB9MzsJJysxXdkkp8RUNggmuFtRpljmEelN9r2aZ6sF54WU1YHNoowxz9T4pKHDZHYLtrWKgN_ncaFQ4kCG_LgQijWzHNRSpq9DryTeY4DBZdxiHjuRzSDLsVKf8DmNMhKSw6bcYJ5yS8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
بنزین لیتری ۱۰ هزار تومان !
پزشکیان: فقط نرخ سوم قیمت بنزین پس از هماهنگی با همه نهادها و ارگان‌ها از ۵ هزار تومان به ۱۰ هزار تومان خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70732" target="_blank">📅 23:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70730">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=qqPZ8iKGt8rs8Yt6k9uz5taoGrj0KfPO532t5ARrsDo57K8RR_EGa6yw7b3kqgL1dwFzMUYR-zTBwsAtYtG0Zd_i2gZ4SwMgSFzNHh1UAZkg-duQ76L6Rfs2VfE9b8LrV7HR9bnXC97B3a9qJerj-nX74PsL7YnkgPMMjH4tvXvs8nmOwI65TqlMKWyN4bGLv5NT4zEgFGcr3OcFlhVnRZyiRzN34HN6g5pKl_YlvGCNyvCpwgjpOtSL8hGTpGIpvFRsbbAll6Z3jhzadflPzJZR9XRSlxt_yFOyTGpA_IvnaJhCDWcPpL6BraAHfGqZKSNh9zvNDCUNyOD4nEUKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=qqPZ8iKGt8rs8Yt6k9uz5taoGrj0KfPO532t5ARrsDo57K8RR_EGa6yw7b3kqgL1dwFzMUYR-zTBwsAtYtG0Zd_i2gZ4SwMgSFzNHh1UAZkg-duQ76L6Rfs2VfE9b8LrV7HR9bnXC97B3a9qJerj-nX74PsL7YnkgPMMjH4tvXvs8nmOwI65TqlMKWyN4bGLv5NT4zEgFGcr3OcFlhVnRZyiRzN34HN6g5pKl_YlvGCNyvCpwgjpOtSL8hGTpGIpvFRsbbAll6Z3jhzadflPzJZR9XRSlxt_yFOyTGpA_IvnaJhCDWcPpL6BraAHfGqZKSNh9zvNDCUNyOD4nEUKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای انتحاری اوکراینی از نوع «شاهد» به پایگاه هوایی «انگلس-۲» در روسیه حمله کردند؛ پایگاهی که میزبان بمب‌افکن‌های راهبردی نیروی هوافضای روسیه (VKS) است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70730" target="_blank">📅 23:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70729">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=ZDg1Y3w4U-bWbofZnhMbI4y9hZ3Azy3brQZclrJtBvdcMoPpbzsk01M4pV22xhHDoGMpFxVU4M9hVq78c39bD-qsnK51pUMJsXF8G6jA_zrQdKsVjqu-VZJeVhdzzzVgWhzj7ug1BolbPOOZxfGOukmWr3TbI1-ULjasSt-PEbl3ii5FfTlmmKbVvw9dBrBrkGUtCHxTBGQ_k_ua3MCGeZJdnM_b4k5PJvR8R_uFMqhEeCSCYjJHMtnsMyduq0gQVh_os9zN3MzjEgRenmevcjtyHAxQ9FlI3dvFQmyoQRZ5JPDnl5aD9JOL9BtQGt51OPD6A1337lN3muhxvND7sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=ZDg1Y3w4U-bWbofZnhMbI4y9hZ3Azy3brQZclrJtBvdcMoPpbzsk01M4pV22xhHDoGMpFxVU4M9hVq78c39bD-qsnK51pUMJsXF8G6jA_zrQdKsVjqu-VZJeVhdzzzVgWhzj7ug1BolbPOOZxfGOukmWr3TbI1-ULjasSt-PEbl3ii5FfTlmmKbVvw9dBrBrkGUtCHxTBGQ_k_ua3MCGeZJdnM_b4k5PJvR8R_uFMqhEeCSCYjJHMtnsMyduq0gQVh_os9zN3MzjEgRenmevcjtyHAxQ9FlI3dvFQmyoQRZ5JPDnl5aD9JOL9BtQGt51OPD6A1337lN3muhxvND7sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبتای یه مداح؛
روزی بود یه میلیون حسابم داشتم رفتم ده میلیون چیز میز خریدم تازه پونصد هم حسابم موند
خاک تو سر مسئولی که چوب میندازه لای چرخ اداره این مملکت
اصلا دلار بشه یه میلیارد رزق ما دست خداس نه دلار
دلار ۲۰۰ تومنی هزار تومنی ۱۰۰ تومنی همش یه عدده مهم نیست
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70729" target="_blank">📅 22:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70728">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇮🇷
چندین موشک ضد کشتی از سیریک به طرف تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70728" target="_blank">📅 22:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70727">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=DhtMJtRt_NOO9LH2bQfHeyxC_gm5phl4b7Zf6RP2Jkq78zfcNiqALeHM-SfJVLYQVhQzlS_hE6fTe8Z0BZSBZN2C547QpbNIeD0W-dtjRTrODcwrGM88VyZkdIL3ZNBELDXV2V1aZXmMYfueH_75KJ9iq2isaOKRllPYgtTmuZj9LBpcZATaQN-hmsxW7uBemZu3rcZ6YUclAh-bdj8PB6W9UNFlDmZIi2i2ILfR2iSjMmWfK5hH74-h9FTggENj-QDGnjyfBfke19BpXSGP5W0euAzXTpyKzNE4BKWom-YPq4nLXyxeHoYiJyPUTndNpn3viHoOeEcwXXgob6upNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=DhtMJtRt_NOO9LH2bQfHeyxC_gm5phl4b7Zf6RP2Jkq78zfcNiqALeHM-SfJVLYQVhQzlS_hE6fTe8Z0BZSBZN2C547QpbNIeD0W-dtjRTrODcwrGM88VyZkdIL3ZNBELDXV2V1aZXmMYfueH_75KJ9iq2isaOKRllPYgtTmuZj9LBpcZATaQN-hmsxW7uBemZu3rcZ6YUclAh-bdj8PB6W9UNFlDmZIi2i2ILfR2iSjMmWfK5hH74-h9FTggENj-QDGnjyfBfke19BpXSGP5W0euAzXTpyKzNE4BKWom-YPq4nLXyxeHoYiJyPUTndNpn3viHoOeEcwXXgob6upNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجید شریفی:
جایگاه کره‌شمالی با جایگاه ایران اصلاً قابل مقایسه نیست
اگر ایران سمت سلاح اتمی برود، همین چین هم شما را تحریم خواهد کرد
مطمئن باشید به اندازه‌ای که روس ها مخالف اتمی شدن ایران هستند، آمریکایی ها مخالف نیستند؛ این را مطمئن باشید
بازی مناسبات قدرت است، بحث دوستی و اینجور چیزها نیست
به محض اینکه اعلام کنید سلاح هسته‌ای داشته باشیم، مطمئن باشید با تمام قوا حمله خواهند کرد، هیچ حد و مرز اخلاقی را رعایت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70727" target="_blank">📅 21:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70726">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209278afcc.mp4?token=Vu7yMg-1ROVrkAXJZa8iXf4AYDHS9D7TILbpYW5QpcQovg3nqfP5NDMIPCkKWEfek76Ui2lcL0n37_iRSh0MkSIIy4HcWPR4_QmLNLoeUyFVLr_O1i_PFfCNeCjVIq5RntUvlmd2HH7xGJ6XgI0TXYzUHwZFmJHHQMTXEWq5DKwHiwgLxP-aFHUXzHnVhZ39kXBmKPBf72rnRrf1UgyYA97JDypjbZmGtBhEURlZvm10YxcaZpoZMqL2Dubopqiwe5Jc_YAcaz2UNQIrAhNMZefRMy7eGlRaDHJlgvid4GHZ3KESi4kURHiP0K5KWmchtsSEk7uRuY55ZSg1xfF2ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209278afcc.mp4?token=Vu7yMg-1ROVrkAXJZa8iXf4AYDHS9D7TILbpYW5QpcQovg3nqfP5NDMIPCkKWEfek76Ui2lcL0n37_iRSh0MkSIIy4HcWPR4_QmLNLoeUyFVLr_O1i_PFfCNeCjVIq5RntUvlmd2HH7xGJ6XgI0TXYzUHwZFmJHHQMTXEWq5DKwHiwgLxP-aFHUXzHnVhZ39kXBmKPBf72rnRrf1UgyYA97JDypjbZmGtBhEURlZvm10YxcaZpoZMqL2Dubopqiwe5Jc_YAcaz2UNQIrAhNMZefRMy7eGlRaDHJlgvid4GHZ3KESi4kURHiP0K5KWmchtsSEk7uRuY55ZSg1xfF2ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
بعد از حذف شدن سوریه از کشورهای حامیِ تروریسم؛
احمد الشرع، رئیس‌جمهور سوریه، به یکی از فروشگاه‌های دمشق رفت و اولین تراکنش پرداخت با ویزاکارت(کارت بین‌المللی )رو انجام‌ داد...
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70726" target="_blank">📅 21:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70725">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=LunrzEWYzRy_dBi7wv6GV9NBHC4nW8JA06uQSTVsGhe3xO4VstlHaCcA1vuZYBwp8v2bG86CfLlu7mwDdQSC6F_P7FCDPsJ6euRM4wUMEQiGDAxMxnJwh3Z3CMejdUrudQRpxt5IHXawuZElMf73WGBMldlWdT8ulSMo56n7UnXf0vkJdNQhWNxQnFEdd4VP8vJizKdADc69EoHG7DWnIUsL6juSvhqayx46SttxzgrDuKGtLipcWqLWS0HV6-BvdDzfXcOsFWXdhj3xLqZmcj3RYI4OG7OIz3bVg8RRozNMpn9MupX0Qvjf_4V7hL4xiGpc4aon1W1DthI_5I_4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=LunrzEWYzRy_dBi7wv6GV9NBHC4nW8JA06uQSTVsGhe3xO4VstlHaCcA1vuZYBwp8v2bG86CfLlu7mwDdQSC6F_P7FCDPsJ6euRM4wUMEQiGDAxMxnJwh3Z3CMejdUrudQRpxt5IHXawuZElMf73WGBMldlWdT8ulSMo56n7UnXf0vkJdNQhWNxQnFEdd4VP8vJizKdADc69EoHG7DWnIUsL6juSvhqayx46SttxzgrDuKGtLipcWqLWS0HV6-BvdDzfXcOsFWXdhj3xLqZmcj3RYI4OG7OIz3bVg8RRozNMpn9MupX0Qvjf_4V7hL4xiGpc4aon1W1DthI_5I_4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇵
ویدیویی دیگر از آنچه در نپال رخ داد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70725" target="_blank">📅 20:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70724">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pxip_QGJyyBiE7YwT-6XISecUnItXKNnhvs83pcq1lymo5Zq0MxSAwif-nKRfgrTGTZsWpsr_dFmLslHtjaKOb97e7IGeDBJTRG3849eNyu6RABMi2zwKw3UTlKJkd1PfmtXXg_d-NiCqjmxzdnypuxj9mEJEjdYkn7xgjgj8AjM05ZpCe_J_YHsbNeIaUAhQijiR51PFDcE2LoCRRqZeiuB0IGtkByGfr6yAygwVzMUv2nhssWWT9I4KYrPxRY-uF-qxQoanEW5_kBhoDtGVS_xLKzQPk4Bo9M0VxBT0BUy0H8Ru2FKvsprJLUUDJGqOZSBZD1QWpvKxtWiuNbY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داد که تمامی شریان‌های حیاتی اقتصادی باقی‌مانده برای تهران را قطع کند و سرانجام به تهدید ناشی از رژیم ایران پایان دهد.
ما همچنین هشدار دادیم که حامیان و تسهیل‌کنندگان فعالیت‌های ایران نمی‌توانند همچنان از دسترسی به دلار آمریکا و نظام مالی جهانی بهره‌مند باشند.
بانک «مصر» (Banque Misr) در امارات تصمیم گرفت این واقعیت را به بهایی گزاف و از طریق تجربه‌ای دشوار دریابد؛ و امروز، ما نخستین گام را برای پاسخگو کردن این بانک در قبال حمایت‌های مستمر و فاحش آن از رژیم ایران برمی‌داریم.
امروز، در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)، شبکه اجرای جرایم مالی وزارت خزانه‌داری آمریکا (FinCEN) مقرراتی را پیشنهاد کرد که دسترسی «بانک مصر» (شعبه امارات) به خدمات بانکداری کارگزاری با مؤسسات مالی ایالات متحده را لغو می‌کند.
علاوه بر این، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری، «رضا محمد تأیدی» — مدیر شعبه دبی بانک ملی — و همچنین یک شرکت پوششی مستقر در هنگ‌کنگ را که در پولشویی وجوه برای یک صرافی ایرانیِ تحت تحریم نقش داشته است، تحریم کرد.
🔴
«عملیات طرد اقتصادی» در حال قطع آخرین شریان‌های حیاتی مالی است که رژیم ایران را سرپا نگه داشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70724" target="_blank">📅 19:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70723">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4qw7bb4BfkOuGmtJ43nhVJkXnukuJiPaqlsvFksCc5iXfZtwuhcDmwZK8fdmCDMjEZDfG2YzoZdMQ4dowOJuCOu1zivLb8ar3sLFrYROHVKN8bh496Wjxiw8jqj-9tX3rJPItksAoVxwhc33xwOmt_v289FssDtWtw0ywOreUb8E3qxO71WT81qCJeKS7WrOrSBPWJMbOQCMbQojYfR43bRJidkMYDahFQBuUoLb9OpJzMF59lyLjIYLT2N-vQvjFwQpjis-wm2QWaO0ARGZVZWYftWadmtAeru9sQR1Lg2x24uKks80nfAIOH_US-DCZ-skEIX4tJgC4bHgcx7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ: دیگر خبری از آن آدمِ مهربان نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70723" target="_blank">📅 19:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70722">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=A0E6zcSjMfiDUpVhZtXD9s2BYxqNWl-c2wqPW1Zu8F_RVlQ10nkHenG-ioQ87jNG1t0yCNTxCtnWgh7HUNVnCI5j2vBq1oOuiPXMTeXwxWRahK2hq1GhqC3SKmt5kKAY19HZpPI1M1dJ_1lai7lHQsPL0nl-vo-N9vqEWcS0pTf_x9qpd9v5ITdNEWlXpT1VUl3ndlQWPlybSfnQD95fi6QeuzsrqYIjNGhbHxnv6C-kEcj280AyFOMLs_0QGlqcT1Fjm7gqMbc8KImmvN-dolflhCQcWYdy-uvpY7YmCfWfFJ68XKbse9PVty2xEjt7iLKti8SPs6_ScmaKxu6AIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=A0E6zcSjMfiDUpVhZtXD9s2BYxqNWl-c2wqPW1Zu8F_RVlQ10nkHenG-ioQ87jNG1t0yCNTxCtnWgh7HUNVnCI5j2vBq1oOuiPXMTeXwxWRahK2hq1GhqC3SKmt5kKAY19HZpPI1M1dJ_1lai7lHQsPL0nl-vo-N9vqEWcS0pTf_x9qpd9v5ITdNEWlXpT1VUl3ndlQWPlybSfnQD95fi6QeuzsrqYIjNGhbHxnv6C-kEcj280AyFOMLs_0QGlqcT1Fjm7gqMbc8KImmvN-dolflhCQcWYdy-uvpY7YmCfWfFJ68XKbse9PVty2xEjt7iLKti8SPs6_ScmaKxu6AIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دوربین مخفی ضبط میکنن از رفتار جامعه با دخترها و پسرها؛
وقتی دختره بنزین میخاد صدنفر برا کمک بهش می ایستن
ولی وقتی پسره درخواست بنزین میکنه حتی یه نفرم حاضر به کمک نمیشه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70722" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70721">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70721" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70720">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnegxZ1H_JDBSpzE_jJdwEAMVv06ftMlaNljfu3susokIDw3rG2KRFax8TwrKHBUqGfMChIeyM45C5CkniiMzIpoGJwceliRi8qmy4UYzSeL3pKrgxOhUXPN9uBhGYKLyfeI7Y9DaVAZZoLplyKA-8fdzSzKHxKBEyT3005rmMuT2l9Tc3xoQMnXs_IlovtzUHzNr69jGCUOpqOZtQGP2adsMpZiqJc2jSpyJiTwOzUdA4XOFzsYLjsBFSHiOxmNIKHxI_bve4VGzny27pdMIRLJd7jVvYzZ_U-EItdQqPc5dyIU9vIsyD3SGD5CFeTmtW0OZN5GbQllWCWQtI9qmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
منچسترسیتی
🆚
کریستال پالاس
ویارئال
🆚
آلاوز
ونیز
🆚
میلان
اشتوتگارت
🆚
بایرن‌مونیخ
پاریسن‌ژرمن
🆚
لیل
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70720" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70718">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=FFksDvsk9FQuVwi2NCtSToFwPcabo1TuVIv9m0nsiqZiYZSK7BKo8Kq-yENTUlivG8yagHvCIYNV1DnFMHC56QHHWF2URgv-PvVMmjps8UdlrbR1VndmwB4t4YUUtC-0RT0Ebrde6cMvpMMawFkO01TzLnLiKxgGT3yCoBXci2gE0bzyEL2yhHS7qtVNCO6ysaVjGTWq9-PpwNkXjfFUjcC-YJ5BbSkPJdG3B0z5shLSeFCqNzykqH5wWj4Hx_7qsBAn_2q1J91-N1Em7Y1kOexIwxRnnVckE6gQFUO_o11Gk3EBkb_jGsMZD9V3fY1A6600S_HwEKzVBkhhqQyTuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=FFksDvsk9FQuVwi2NCtSToFwPcabo1TuVIv9m0nsiqZiYZSK7BKo8Kq-yENTUlivG8yagHvCIYNV1DnFMHC56QHHWF2URgv-PvVMmjps8UdlrbR1VndmwB4t4YUUtC-0RT0Ebrde6cMvpMMawFkO01TzLnLiKxgGT3yCoBXci2gE0bzyEL2yhHS7qtVNCO6ysaVjGTWq9-PpwNkXjfFUjcC-YJ5BbSkPJdG3B0z5shLSeFCqNzykqH5wWj4Hx_7qsBAn_2q1J91-N1Em7Y1kOexIwxRnnVckE6gQFUO_o11Gk3EBkb_jGsMZD9V3fY1A6600S_HwEKzVBkhhqQyTuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری خطاب به آخوند:
یه چیزی بگم باورتون میشه؟وقت تموم شد.
🙁
واکنش آخوند:
خوووبه؛اگه اینجوریه که من دیگه اصلا نمیام اینجا.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70718" target="_blank">📅 18:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70717">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55129dd199.mp4?token=pfnI5cDAe3q3GPDPvGIVESJey84sex7LpJTHSjlxAbOFOsmxo9tQz5Uh01gQ9XpEhCcgtdRz0E6L41Q3qIR8ngfX5X2J6UQBJTEDPsDyJEvjiaES35GbiSXKVx5rSgPycDWAITz9kd9IOmoc-pNw8FmpWyBnsTLT0YNAHXzwSpaDJbQKd_WTrbxV4gfsIebK5fxOdVZxPopa6aw8w7WuCLwQd_QhIQqtEjENwIpsPsngubW7E11hhuiQbq_DCUiuo327vmNBz1eoZIZoZCldzd7U9LZZ__YpAnc7M1VJjPQyhJk-f2eetDkcrqPWbvuzlp7yGsRWwgNMU_pAWlp0ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55129dd199.mp4?token=pfnI5cDAe3q3GPDPvGIVESJey84sex7LpJTHSjlxAbOFOsmxo9tQz5Uh01gQ9XpEhCcgtdRz0E6L41Q3qIR8ngfX5X2J6UQBJTEDPsDyJEvjiaES35GbiSXKVx5rSgPycDWAITz9kd9IOmoc-pNw8FmpWyBnsTLT0YNAHXzwSpaDJbQKd_WTrbxV4gfsIebK5fxOdVZxPopa6aw8w7WuCLwQd_QhIQqtEjENwIpsPsngubW7E11hhuiQbq_DCUiuo327vmNBz1eoZIZoZCldzd7U9LZZ__YpAnc7M1VJjPQyhJk-f2eetDkcrqPWbvuzlp7yGsRWwgNMU_pAWlp0ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چرا یهودیان بهترین بی‌سیم‌ها و شرکت های اینتل و راکال رو دارن؟
⏺
مهدی طائب؛ کارشناس مذهبی: چون حضرت موسی یادشون داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70717" target="_blank">📅 18:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70716">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/508daa856a.mp4?token=g16Sp71EWYgVOPky13zKBylBhN4bpHQ2W_8wMzZyF1H-Us5ubp7dEg2jMorXvC6s-yNQdZTErV4w-Nnz3lOraYQy10lX_h7tX-J1HGO-5Z2yFIotVFfw5lFnT7LAYSpig3PwQ5ZJWyEAHoYZ9ltVd4ErE70VfJponfm8_oziA5MmgiEA8TQu3UW4Hgqy8TbWIdB5LBTIMWQX-qDz8oYgThonzKidY6LXcWR1MqX60cFMq43BoGrgmqMH4ENH3aEOUfV0X_G5GxXCI-oz0dwaT-UPrsmJgk5DrSyEWOCaezrusl4OQeZuf_9LgxGvywJoAp3W1MGowjtOGdzHT0n-fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/508daa856a.mp4?token=g16Sp71EWYgVOPky13zKBylBhN4bpHQ2W_8wMzZyF1H-Us5ubp7dEg2jMorXvC6s-yNQdZTErV4w-Nnz3lOraYQy10lX_h7tX-J1HGO-5Z2yFIotVFfw5lFnT7LAYSpig3PwQ5ZJWyEAHoYZ9ltVd4ErE70VfJponfm8_oziA5MmgiEA8TQu3UW4Hgqy8TbWIdB5LBTIMWQX-qDz8oYgThonzKidY6LXcWR1MqX60cFMq43BoGrgmqMH4ENH3aEOUfV0X_G5GxXCI-oz0dwaT-UPrsmJgk5DrSyEWOCaezrusl4OQeZuf_9LgxGvywJoAp3W1MGowjtOGdzHT0n-fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشماتون بریزه؛ یه پسری داشت توی خیابون قدم میزد که یه پیرزن رندوم برگشت بهش گفت: تا حالا کون کردی؟ دوس دارم منو از کون دار بزنی، حشرم بدجوری زده بالا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70716" target="_blank">📅 17:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70715">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=IetUKvSxhICU4qrZc5DoSXQI3DF3fQoqiy3_hBUGjrNnoN0zq-4eqnkJLPXbwZ5AbzSKaFWn5zZi767FzsfsXoTL6_EY92yUiRMpaHkUMLC7KpxVF2fN4gA2yuFWlIpl0SOuZo3YieHvhTu9fEb4ODRAHZjfzA4PxX3cHqHMe-Ribl48B_Ev97b15l1btYuGKkm33rlUzEgCuE1lphgIRxnXBtABGhtKXUNBcPKWijANaWgD4F-UfXl-P0FT2L2t6XOG16nV0E6YPiNBJqAK6zia3OHE7AoO5T9oCQL1xVw-sYAQ3gVJiWyCKQW0VvX3ilP9OcdwDZFejsm993TIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=IetUKvSxhICU4qrZc5DoSXQI3DF3fQoqiy3_hBUGjrNnoN0zq-4eqnkJLPXbwZ5AbzSKaFWn5zZi767FzsfsXoTL6_EY92yUiRMpaHkUMLC7KpxVF2fN4gA2yuFWlIpl0SOuZo3YieHvhTu9fEb4ODRAHZjfzA4PxX3cHqHMe-Ribl48B_Ev97b15l1btYuGKkm33rlUzEgCuE1lphgIRxnXBtABGhtKXUNBcPKWijANaWgD4F-UfXl-P0FT2L2t6XOG16nV0E6YPiNBJqAK6zia3OHE7AoO5T9oCQL1xVw-sYAQ3gVJiWyCKQW0VvX3ilP9OcdwDZFejsm993TIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو وایرال شده از پسری که ماکت آیفون رو میگیره دستش و زیر ۵ دقیقه ازش میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70715" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70714">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=NKSnPLojMLwcameanZdBf2kCJuc0ZVFEtWkccUFFnBYFc8ZsMMRvP_6PviItSu8Fi47uahUOHplTegKaQw_LnBT7B8kEhnVaVxxGSMPkYlrRdHP_hlA4lTlccI1oKJAFDXLAdeK9EaySfxc1aViUeBhY6nTOv76g4Z56LFrBOVMMt2bFexOmJ069kJEWHHGmhpI5evyRQE02V6naog4LjDJU3cKsOgrRzCGlqHqr2XoTvdC2X4BBFJh0NDV9DO1jWytkqzBK3P5hGK-VMzABj2eD91dEyjo9ZuOsSLanp7JYcNrrVSZP94CuFlgekOUPN1d3k77aaTOnOVCtl5-f0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=NKSnPLojMLwcameanZdBf2kCJuc0ZVFEtWkccUFFnBYFc8ZsMMRvP_6PviItSu8Fi47uahUOHplTegKaQw_LnBT7B8kEhnVaVxxGSMPkYlrRdHP_hlA4lTlccI1oKJAFDXLAdeK9EaySfxc1aViUeBhY6nTOv76g4Z56LFrBOVMMt2bFexOmJ069kJEWHHGmhpI5evyRQE02V6naog4LjDJU3cKsOgrRzCGlqHqr2XoTvdC2X4BBFJh0NDV9DO1jWytkqzBK3P5hGK-VMzABj2eD91dEyjo9ZuOsSLanp7JYcNrrVSZP94CuFlgekOUPN1d3k77aaTOnOVCtl5-f0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر با زنش دعواش شده و رفته جدا خوابیده، و اما آخر شب برگشت تو اتاق پیش زنش و این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70714" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70713">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1E7ZhDcc3tixenpmtAKY6iAX_sxxj0uxnbQ0CUvoLeuHqzWDO2YfmaR273c826admjLwxnvPWoz6xeItu4A6CK3_AWQNUTNgdME5Ei-z7FJQXVeZsRDDNycVCiy3BWJAmCXVqALumsDLWnVyRltqOXI52fN5et5cGeEgbrA526iktaQG5rB2NPMZmDT8PoB0FZt6knReGCud53XElneDoPJ7qmi-smhqZ55U7GWk3jgeWFlg51w4PUSjGZVvfBI2oQmmMX9GLqOpno5K_bJV9k5h6gdG9NygUycBlv65fYGCYvXmvPoR6aUnDBKwWV-yMpO0lDJVMFbq76j9wOwdJd0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1E7ZhDcc3tixenpmtAKY6iAX_sxxj0uxnbQ0CUvoLeuHqzWDO2YfmaR273c826admjLwxnvPWoz6xeItu4A6CK3_AWQNUTNgdME5Ei-z7FJQXVeZsRDDNycVCiy3BWJAmCXVqALumsDLWnVyRltqOXI52fN5et5cGeEgbrA526iktaQG5rB2NPMZmDT8PoB0FZt6knReGCud53XElneDoPJ7qmi-smhqZ55U7GWk3jgeWFlg51w4PUSjGZVvfBI2oQmmMX9GLqOpno5K_bJV9k5h6gdG9NygUycBlv65fYGCYvXmvPoR6aUnDBKwWV-yMpO0lDJVMFbq76j9wOwdJd0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سخنان ویرال شده از یک آخوند اردبیلی که درحال وایرال شدنه؛
تو دنیایی که جوان نمیتونه ازدواج بکنه ولی میگن عیبی نداره تلاش می‌کنیم درست بشه
تا متخصص های شما وضعیت رو کنترل کنن جوان مملکت از گرونی استرس اضطراب سکته میکنه میمیره
جوان ۲۵ ساله شب میخوابه صبح بیدار نمیشه این خیلی حرفه
میگن بچه بیارین آخه بابا پوشاک شده ۷۰۰ هزار تومن شیر خشک شده ۳۰۰ هزار تومن لعنت به قبرتون بباره از کجا بیاره آخه بیچاره
میگن آخوند میره میخره بابا بیا منم عمامه رو گذاشتم زمین
اینا همش شده شعار به ولله نیازی به مذاکره و کشور های دیگه هم نداریم مسئولین ما بی عرضه ان
ایران‌خودرو شده مافیا برا خودش چرا جلوشو نمیتونین بگیرین؟؟ ولی واس یه تار مو میکشین واس یه قسط عقب افتاده میندازین زندان
جلو اینایی که زیر سایه نظام گردن کلفت کردن رو بگیرید ننگ بر شما و حیف این ملت که دست شماس
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70713" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70712">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=t3F0Pv1hfNZMDRH_zhAHWx_CWt6n5YT7dhPtdA_59B281DuO4f27vH8Tx0h7ORrnj4S21f-B_807zbf--b76p6pVcgUSsmyf31HEoth5VciO4O9VF970vOvgzX2XicGFNwhn_MW6JLqupzbXP9CqXmy2K4Am3_rdMO3KVtr4hjORORWXjkClVB8BWPf4TQhH5TZmv6zRh2a-jbTfeekLqlVYMHKCCEbnC_cAv5I1KkJ0UsDhkKMVrC2VgkLCHzWm8yibDscyTJHDKEBLMA2WzHx4LcAd7Q9WkbFko7nDgzUtOQ8yOI26cPpJAFsNWwPyeiaAn3Ik1hCnoE6WXUe58A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=t3F0Pv1hfNZMDRH_zhAHWx_CWt6n5YT7dhPtdA_59B281DuO4f27vH8Tx0h7ORrnj4S21f-B_807zbf--b76p6pVcgUSsmyf31HEoth5VciO4O9VF970vOvgzX2XicGFNwhn_MW6JLqupzbXP9CqXmy2K4Am3_rdMO3KVtr4hjORORWXjkClVB8BWPf4TQhH5TZmv6zRh2a-jbTfeekLqlVYMHKCCEbnC_cAv5I1KkJ0UsDhkKMVrC2VgkLCHzWm8yibDscyTJHDKEBLMA2WzHx4LcAd7Q9WkbFko7nDgzUtOQ8yOI26cPpJAFsNWwPyeiaAn3Ik1hCnoE6WXUe58A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سخنگوی دولت:‌ مردم منتظر بهتر شدن وضع اقتصاد در سال آینده نباشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70712" target="_blank">📅 15:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70711">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⏺
🇺🇸
پروفسور جان مرشایمر استاد علوم سیاسی دانشگاه شیکاگو درباره اینکه چگونه تحریم‌های آمریکا می‌تواند منجر به اقدام تلافی‌جویانه ایران شود:
در سال ۱۹۴۱، ما یک محاصره نفتی شدید علیه ژاپن اعمال کردیم و دارایی‌های این کشور را مسدود ساختیم. ژاپنی‌ها در وضعیتی بسیار وخیم و درمانده قرار گرفته بودند.
آن‌ها تصور می‌کردند که ما با آن محاصره اقتصادی، بقایشان را تهدید می‌کنیم؛ و در نهایت، دست به حمله علیه ما در «پرل هاربر» زدند.
به گمان من، شما نخواهید توانست ایرانی‌ها را به زانو درآورید.
اما اگر بقای آن‌ها را تهدید کنید، آن‌ها دست روی دست نمی‌گذارند تا صرفاً محو یا تسلیم شوند؛ بلکه واکنش متقابل و سختی نشان خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70711" target="_blank">📅 15:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70710">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
📚
#فوری
؛نتایج امتحانات نهایی تیر و مردادماه پایه های یازدهم و دوازدهم در سامانه بینا منتشر شد.
🔴
آموزش دریافت کارنامه :
۱. ابتدا از طریق پنل سنجش وارد بخش ثبت نام در آزمون شوید
۲. ورود به سایت آموزش و پرورش
۳. مشاهده سابقه تحصیلی و ثبت نام ایجاد و ترمیم سوابق تحصیلی
۴. ثبت نام ایجاد و ترمیم سوابق تحصیلی
۵. بعد از ورود به این بخش از سایت وارد لینک سایت بینا شوید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70710" target="_blank">📅 14:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70709">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=B9STpXMiBiAfdUQLQTDKrcqETECbJP95DfEuqWbCxyXofxh3GUH826dPWY3LqL5PKdhxCCGN59J06HNHdzs8CGYgbZWOI6GbKo0LK8l8v7i1Qjvd-gCk4Pce2o1yBWuBWMMaTEAeYQp3KNX3sFkfOJpIhBv2ICGoiGQjUlmyWsvGM7ozSw7_zCvlCY55TGZI6dcpwbsoSPfAPTiEuJv049tG-F_X1j__oAbcevXsZ__XKju6jT-zfL5ltJyB4xTStUbK9c_8CBgVT9FLnsKwk9qZwKiz6QAQR4GIC6kaWZqcirWRb1Bwn-svLV0GGcvjSZbiWYQ_dVtPY3yE7i-CUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=B9STpXMiBiAfdUQLQTDKrcqETECbJP95DfEuqWbCxyXofxh3GUH826dPWY3LqL5PKdhxCCGN59J06HNHdzs8CGYgbZWOI6GbKo0LK8l8v7i1Qjvd-gCk4Pce2o1yBWuBWMMaTEAeYQp3KNX3sFkfOJpIhBv2ICGoiGQjUlmyWsvGM7ozSw7_zCvlCY55TGZI6dcpwbsoSPfAPTiEuJv049tG-F_X1j__oAbcevXsZ__XKju6jT-zfL5ltJyB4xTStUbK9c_8CBgVT9FLnsKwk9qZwKiz6QAQR4GIC6kaWZqcirWRb1Bwn-svLV0GGcvjSZbiWYQ_dVtPY3yE7i-CUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ویدیویی که بین طرفداران حکومت در حال وایرال شدنه و دارن میگن به زودی این صحنه از صداوسیما پخش می‌شه؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70709" target="_blank">📅 14:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70708">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇹🇷
شرکت‌ترکیه‌ای«روکت‌سان» (ROKETSAN) با موفقیت موشک کروز جدید خود، «چاکیر» (ÇAKIR)، را از یک پرتابگر زمینی آزمایش کرد.
این موشک با بهره‌گیری از جستجوگر فروسرخ تصویریِ نسل جدید، اهداف زمینی و دریایی را با دقت کامل (اصابت مستقیم) هدف قرار داد.
این آزمایش‌ها همچنین قابلیت افزایش برد موشک را به واسطه سیستم سوخت جدید، تأیید کردند.
موشک چاکیر که پیش‌تر از سکوهای پهپادی پرتاب شده بود، اکنون توانایی شلیک از خودروهای زمینی را نیز به اثبات رسانده و قابلیت یکپارچه‌سازی با پلتفرم‌های گوناگون را نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70708" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70707">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70707" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70707" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70706">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBukELYzx2IdUjnnqwG7qg9Zc9zXz0MbpmOG-v0w6M9rdSLH8FTXeftMPl_AyM51b5G4Qsgv4p0ROsFknAMR7ckOxlkrmerdFLMLNQnR29JTKsVHIcU07EjOzeM73ZiQAAw4aPjV1TkWlmrTadCuYM0cUnrgW1cE42WnZrMdH5flmgGH4pTMD8jEH8FTLyp-lHb_sc29H3WzWWw1djDv74GnrPP0oBTfCFiZ6Poo0dgq7vOrOU6EniEaiHcooeuCF9WFDyWbHdSiik76bBsNCoBJeHsumL29vta7Q6SjCTP4Osymjt1I4nevsZ0oW0QX2wvwhoBU62-1ZySJBJ7VVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد جذاب فوتبال ایران را در
TrexBet
پیش بینی کنید!
🦖
استقلال
Vs
فولاد
🦖
جمعه | ساعت ۲۱:۰۰
🦖
ورزشگاه شهدای فولاد خوزستان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70706" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70705">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=D64-dFVhVcSo9qyhxO3_d36Ij4sl-nSRZ2oTUIIlksgH253QuHn5FWSKe1h-YDM1_vBZonOqinGfbUspfQka9--8EJX5tzQBu1rYtbkvuzb5PkxDORF_Ywqmeu1oZwteBzFFJhmiZefsPSbwlH4Qihj0COcOZpTe7WQL0Ecm-Kc1eacFpPu1575Hot8T0r0aqZoCLIklGToIiBh_GvmTtfK__iCIsXgTE_bcdLxuIHi9KPcHTOuL8L7i-7Cujq2hIWBVuzBZG7-XUcx8KIQDkyeEK2GNslrgGTAJEz2KhlR2vu7K0NXEl4nHZz6e9hqFEGQulDnYzxyLVDt2UDboSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=D64-dFVhVcSo9qyhxO3_d36Ij4sl-nSRZ2oTUIIlksgH253QuHn5FWSKe1h-YDM1_vBZonOqinGfbUspfQka9--8EJX5tzQBu1rYtbkvuzb5PkxDORF_Ywqmeu1oZwteBzFFJhmiZefsPSbwlH4Qihj0COcOZpTe7WQL0Ecm-Kc1eacFpPu1575Hot8T0r0aqZoCLIklGToIiBh_GvmTtfK__iCIsXgTE_bcdLxuIHi9KPcHTOuL8L7i-7Cujq2hIWBVuzBZG7-XUcx8KIQDkyeEK2GNslrgGTAJEz2KhlR2vu7K0NXEl4nHZz6e9hqFEGQulDnYzxyLVDt2UDboSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیزر سریال مرد هزار چهره هم اومد و مسعود شصتچی یه جایی عضو تیم مذاکره کننده هم هست:
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70705" target="_blank">📅 13:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70703">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihDTqkgWBCgs8NAOGJoebG_rQDh1n4KP7tR3O9sAyEabV8pgLB2MvHMXmXdgpcbbb3yS_SXP2gkd9zUL-3o-HnN3-g6hk6LGZ-GsDdmiDN6y8OOCYcz7514PHe1fQxXdfvdtJC-LE-zDtd7PYAQppBnPu4gOjPtaf2rPNcF3hrm7Z5eP08ZWGmYCkW56UK47kgTAfKfyiXcK_SfNpOTjt772spqQ605FZDloj3yoPd-OePTm0AYD9mwk7hIWrBCW_RAEhwqkwqmwBGb5XUwyKCEaAWqvtRNewVRcvEhv05Dwfokt6flJ9qTp5f9bRNngeh8YPo0DrlOX4YP_AOw8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APNO8DkGLHkYgx1Vx6ZUwLkKKhqBHfS1nYhjM12wmnP5IzikOzLPnNn-cwc-cIUJs4ChTL6W8ThvT1BxKeJw5lyatTN9DYwLuesz4AfLQz5a4uYK4tOBVpVXKy4Q26ijf-bszKfQ3V0m-cs8in_y6TmLwhltjBfUIa-rIGZ7G6ovSvzVDDV0uPa9NyKfHpUGrlV7DHN3n3hCT4SJC50qUJlWbrqXFQ0ZyJipVmWSz2HlR0EOgOeI_wYth44iqC5p1_q2_2J3oa6dX8MS0lDch4OqvvM69EUfm_uwDLLSsqbgilqb38GPo_c11DQbM4ZxtndO3aRRQ7mtbBR2AyibhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بیانیه وزارت امور خارجه جمهوری اسلامی در رابطه با تحریم ها:
تمام کشورها موظف هستند از اجرای تحریم‌های یک‌جانبه آمریکا خودداری کنند، و تحریم‌های اقتصادی آمریکا علیه ایران غیرقانونی و کاملاً غیرموجه است.
استفاده از دلار توسط ایالات متحده به عنوان ابزاری برای ایجاد ترس و فشار بر سایر کشورها به منظور وادار کردن آن‌ها به پیروی از سیاست‌هایشان در قبال ایران، نقض حاکمیت ملی کشورها و حق آن‌ها در تعیین سرنوشت خود است.
همچنین، تحریم‌های آمریکا به عنوان نقضی آشکار از منشور سازمان ملل متحد و اصول عدم مداخله در امور داخلی کشورها و همکاری بین آن‌ها تلقی می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70703" target="_blank">📅 13:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70700">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n8mpn_ngn5oIDq5mwRLM6MnIDyKsT2i7Ah1jPHNPaJEhEtK2kqPl8gWykJB_TKtAqMRZHLa2VFxswAlG2NrWjZQo3YwAxTqBUhcR-tQVoWrlbz6cBeH1ZufOkWAeptgPZnHmC_IDC8qOjVgCnd09Rqy4k2wCwj7b1MXhSABqXFSKW9wTCJu7On4eQ_Y-_Q2anHijd5C7GPP9HfPqKHrYfJ3S1oKjK47br5XxBwiRnXHKWTonkrsSazHl8-5nXyq-rTlptwDN1fQbdyP4FpJhPoFi1TVRHkz2naQBFVUpdSCBHskg3pCA1HwNF_60PmM1YvdahID6xPA8TDDDvBBmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DSWVMfJf8FDEOChwEyHCeYj0JB-hXeD4akGsMJG43b1lKRuX3gyfvnHFja22Nd29wIU9QvZRVZvhU9Ecw2Marn6BTKUZGWsXC9s1_NOYyo_4zAGD1G0deYJcDDREIf0L5DvOZEvcKTDCrF5wg_FLoS8zXVYwBEqxdest2L7vRlzybLJbaFwWf2gfIAWiYbPU9noWW-UbfDo0AanT5FeIVU3CC2dAz-n-VT2WX4Bjw5JloGBT6QK8kdR_dpfVrqmNn1Dh1FcZ8SQDTV-PwojUlxKrjq6rvJolBzNoocUxkAvJ5KYfZxroVzbu42TqIIvCpYfua8Cpj5FucaKzs6W_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rlLU7O24PnSyWbNVLwD6pCgezTIKQun4GvkzqmV3ZL1i466hBj-ZJ8BCsXSagHTwd_-lHjkP_drIDqd11rSRc8X8G-zXFVBkpjZJeWtt69pjjfYR98Rzqhi8YCTOsZQgjQX6aH9IiEHPb2vyBSp0GEVSu_OfD4YU_ZUbHcARb2gHFNhagcAOZc2L-CrsW69z9en0osQeLvBzKjP8_VbeqMV-SnIkgx-HE3_PM4YUnlKpUkgkxiFqmzhlpW3HuSF2LPshhT6OS7G7dtNoDFxWg2R9uOl1zRYqljYCVLdMRUKcEL5_7gUJmatCg9M4SOMV9i-xuE8LRGU79UTN1ROmuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نسخه پرمیوم ایران این شکلیه؛
عکسی که چند تا جوون از دورهمی‌شون توی تهران منتشر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70700" target="_blank">📅 13:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70699">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqdJbBWbDrMGZ7RfviriVqxjGNhwyHNZehFhTxIco7GvjsTn1SdFU-Hy8WrLtRGu9JC0n2Z79D7VfVR5sK-01mG5hOcJYiy2SsF2XdqXR5Mxm2mxof3LGjEsdklznxBVlLc4Ch-pC2q-I9xcPMRKnWoJgXs8UV5TShFnKPjPN6S7XOGCNTmgYlVBsINTVKkyGVC7yquN-d9Qh5szVLscr5L0sNZw2tJaeEAmFOF5t5eDnDajck3eKR9KUKyboVHAW2v9l_JCkYAxNqlVItygmKqq7F_5Wz7QMBD8-EBXZlEdjbM39zgz6xxPmjCF_JC_aFk_JBnCJwgq2oPXveMhBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کافه بابک زنجانی که هفته گذشته افتتاح شده بود؛ به علت بی حجابی پلمپ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70699" target="_blank">📅 12:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70698">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1291af3432.mp4?token=HJQWCwyGQRyHJaP7C9X4vuCZnVWyl4y_OkIgXOKQ7qBV_M6wUb6SjrZnTGjLoPHS10YDnuaJW1l_JINgCOtSEZUI5axPDFtAL02cE2IOnBz1eulJuQURsQ6O74w_or_JjGfE60vgg85op9yGjT2NLwpoRPa2of7nc8KNcrouoHF7rwmOMiCbh3yNB1RKdF1EPqjv-0FbD1PRRYuTGmpre0XKSNh9i5uW_6a3EpFvq-AXeeSvizxQ10lGyb8BP4xGe7qg2DAJi0skzxqHgw0-aw0cvT6uarFBydF7U8jJby86DxIDckpGhmLbFYsXMbk1BkZXdJUQhh8K5wo5e9NR9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1291af3432.mp4?token=HJQWCwyGQRyHJaP7C9X4vuCZnVWyl4y_OkIgXOKQ7qBV_M6wUb6SjrZnTGjLoPHS10YDnuaJW1l_JINgCOtSEZUI5axPDFtAL02cE2IOnBz1eulJuQURsQ6O74w_or_JjGfE60vgg85op9yGjT2NLwpoRPa2of7nc8KNcrouoHF7rwmOMiCbh3yNB1RKdF1EPqjv-0FbD1PRRYuTGmpre0XKSNh9i5uW_6a3EpFvq-AXeeSvizxQ10lGyb8BP4xGe7qg2DAJi0skzxqHgw0-aw0cvT6uarFBydF7U8jJby86DxIDckpGhmLbFYsXMbk1BkZXdJUQhh8K5wo5e9NR9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
🖥
من دریاسالار برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده هستم و گزارشی عملیاتی درباره مأموریت‌هایمان در خاورمیانه ارائه می‌دهم.
۵۰ هزار نیروی ما در سراسر منطقه، ضمن حفظ جریان تردد تجاری در تنگه هرمز، با موفقیت در حال اجرای محاصره دریایی علیه ایران هستند. ما با بهره‌گیری از غواصان نیروی دریایی، نیروهای ویژه (SEALs) و توان هوایی مشترک، به دستاورد مهمی نائل شده‌ایم: پاکسازی کامل مسیرهای کشتیرانی بین‌المللی از مین‌های دریایی که پیش‌تر توسط سپاه پاسداران انقلاب اسلامی ایران کار گذاشته شده بودند.
طرح‌های بین‌المللی تفکیک تردد (TSS) — که حکم شبکه بزرگراهی حیاتی برای کشتی‌ها در اقیانوس را دارند — اکنون کاملاً عاری از مین‌های دریایی ایران و برای عبور و مرور کاملاً باز هستند. طی چند ماه گذشته، ما به عبور ایمن نزدیک به ۱۵۰۰ کشتی تجاری حامل حدود ۷۵۰ میلیون بشکه نفت خام از این تنگه کمک کرده‌ایم. در همین حال، به دلیل اجرای قاطعانه محاصره دریایی که از اواسط ماه ژوئیه از سر گرفته شد، ایران حتی یک بشکه نفت هم از سواحل خود صادر نکرده است. هیچ کشتی غیرمجازی وارد بنادر ایران نشده یا از آن‌ها خارج نشده است و ما تنها به دلایل بشردوستانه اجازه عبور داده‌ایم.
نیروهای ما با به‌کارگیری بیش از ۲۰ ناو جنگی و صدها فروند هواپیما، با موفقیت مسیر ۷۵ کشتی را که قصد دور زدن محاصره داشتند تغییر داده و سه کشتی متخلف را از کار انداخته‌اند. در جریان بازدید اخیرم از منطقه، شخصاً شاهد فداکاری، حرفه‌ای‌گری و آمادگی فوق‌العاده ملوانان، تفنگداران دریایی، سربازان و نیروهای هوایی‌مان بودم. آن‌ها همچنان با تمرکز کامل، توان رزمی بالا و عزمی راسخ به وظایف خود ادامه می‌دهند و من به موفقیت تاریخی آن‌ها بسیار افتخار می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70698" target="_blank">📅 11:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70697">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=TQiiLRxhdFC4rbHWYIu7mRax2NPn0kJbB7J6BAl6Myo-BUUofNjlzxT4OvL77VmVESY-rT_HQhwoOOzMVJXEumY7XK3f0p3e6aBAUypagJAFgVGJWjWR1opCJn5RHlROi1k3RGAbyVU_7JSugr9qi3ye6kXNIqPo78BH3GS97vW3Cw_Mf1UFGvCwwgw6euUZFDhd2OaIz4QMgSUxLdpRD4jDUC92KyPlnc6wCOzDFhywOOO-IvvVTl_8lMkgv-Z6408qEbD7ZJClEoY4FaCT2h359fxQnVDBJdY3PZTyKL5dy06bQIa5oXuWzWANk6nODIkYogVPjYbmzgzsVZjLuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=TQiiLRxhdFC4rbHWYIu7mRax2NPn0kJbB7J6BAl6Myo-BUUofNjlzxT4OvL77VmVESY-rT_HQhwoOOzMVJXEumY7XK3f0p3e6aBAUypagJAFgVGJWjWR1opCJn5RHlROi1k3RGAbyVU_7JSugr9qi3ye6kXNIqPo78BH3GS97vW3Cw_Mf1UFGvCwwgw6euUZFDhd2OaIz4QMgSUxLdpRD4jDUC92KyPlnc6wCOzDFhywOOO-IvvVTl_8lMkgv-Z6408qEbD7ZJClEoY4FaCT2h359fxQnVDBJdY3PZTyKL5dy06bQIa5oXuWzWANk6nODIkYogVPjYbmzgzsVZjLuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی کنم!
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70697" target="_blank">📅 11:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70695">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMetmc87nbCc5ysb58-Sh7DoPZdmMPg2Dlh2eCWVqcrfCj7dMYFYtTPQbDPVKXbt6jacFSTcdT42V0myWlTcDnaEC6oQbYmR0a0AwaPEEIIOsyRU5Z_E8ywohE1BIjZMyWzbLbzy_6NVi0qFYNmSueH3C4Z0hqQSlO18IO5elKyfHxmxrqiugJbXy5fDq8Lbiioao8zPUwc7oN1C0xmERu_dPJuJ6mBPFKCe_BFYgioGxtWSRUyD24o-XxtviL9wCxzyPyvmfPWf7C52FsZuIq5JYu04FeourKPm5hVZ3vmLvPuanrVQm97oGdW1qByNB9FwjQCgEWz4efK_BoHWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029290388.mp4?token=UZvMBgpbPdBefNjFDTk_V5f5a4duQDgsMdqozKBxuJuz0HOa8y_ZA--h7xihxoWvwrvkLKrAtyDpXNKi-O5HPbip-JArDagAQPqD9N1jCgiI7GoVkyA1SDQN5JwCtYIEhqf9_XxP-khjej13_t8fhaB-wfE9aC0ocLwJWVeBgGhIzrjBTPNit64KGbzUIrSWiNahYJb7vhns-UJcdfitHwbKA2EzoYIjFdhat2GeWQCWRpkcYw2v8rsm0x3t5t07XjyBoKO2iQxxCxSIPq5hyPuyll4aviwZLeveJVTVpl4CQqvD04YKw8wpuM2Eb9SBbRsymgzwhytx-xT0XKxIlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029290388.mp4?token=UZvMBgpbPdBefNjFDTk_V5f5a4duQDgsMdqozKBxuJuz0HOa8y_ZA--h7xihxoWvwrvkLKrAtyDpXNKi-O5HPbip-JArDagAQPqD9N1jCgiI7GoVkyA1SDQN5JwCtYIEhqf9_XxP-khjej13_t8fhaB-wfE9aC0ocLwJWVeBgGhIzrjBTPNit64KGbzUIrSWiNahYJb7vhns-UJcdfitHwbKA2EzoYIjFdhat2GeWQCWRpkcYw2v8rsm0x3t5t07XjyBoKO2iQxxCxSIPq5hyPuyll4aviwZLeveJVTVpl4CQqvD04YKw8wpuM2Eb9SBbRsymgzwhytx-xT0XKxIlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📚
آرش عمید دبیر هندسه و گسسته کنکور، وقتی یکی از دانش آموزان بهش گفت ما پول دادیم، اما نصف کلاس یا داری حرف بی‌ربط میزنی یا کلا صدا قطعه، به این شکل توهین آمیز جوابشو داد!
🗣️
بعد این قضیه آرش عمید اومد و از شخصی که بهش توهین کرده بود عذرخواهی کرد؛
ماه‌های گذشته با اتفاقات سختی روبرو بودم، پدرمو از دست دادم و شرایط روحی خوبی ندارم.
اما بازم این کار منو توجیه نمی کنه، بخاطر حرفام که باعث رنج اون دانش آموز شده معذرت می‌خوام.
در ادامه هم گفته که هزینه که این شخص برای شرکت در کلاس داده رو بهش برگردونن
.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70695" target="_blank">📅 11:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70694">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">💢
‼️
تریلر کاملGT6 که راکستار رسما منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70694" target="_blank">📅 10:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70693">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی:
ادعای ترور پسر ترامپ؟؟ توهمات نتانیاهو هستش و اگر ما چیزی بخوایم بکنیم کسی نمیتونه جلوشو بگیره
ضاحیه و بیروت خط قرمز ماست کسی نمیتونه به اونا صدمه بزنه
باز شدن تنگه هرمز منوط به اجرایی شدن شروط ایران توسط آمریکاست
محاصره ادامه پیدا بکنه بشدت اهداف اقتصادی آمریکا رو میزنیم
آتش بس در لبنان و غزه جز شروط اصلی تفاهم با آمریکا هستش
نتانیاهو رو خواهیم کشت
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70693" target="_blank">📅 10:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70692">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51590b7113.mp4?token=FYzB7AhfNev-F4nidvgHmyPOcuegG-ykossUAJlbe2khy1ssmn_ohBVAQhTEw3MQypkrY93fo6EF8XhljxYETkt2649ddSxL0ZKBCzTRCnOx9l_Q9CR1JYUQXGj3SZFbQ1LYr8g5nDgEp957i8tigQZtDNGqY0LGG89Kkc4-8UuIM3p-WftgCEsyqyRqCwHEVYTpfTQTgLIUV5PaCMZKjXIsYZS6ldWVx_C85n8iWp5_K-HSrGe-51S_AC4T56kJHPEVdmnOoIxYpe68aDfkpHpJmsz6MEwSGKFlltBAwS_65UO96Wjo9FYbXUOIEopZIKioqIrmMlu1WSFHBCodIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51590b7113.mp4?token=FYzB7AhfNev-F4nidvgHmyPOcuegG-ykossUAJlbe2khy1ssmn_ohBVAQhTEw3MQypkrY93fo6EF8XhljxYETkt2649ddSxL0ZKBCzTRCnOx9l_Q9CR1JYUQXGj3SZFbQ1LYr8g5nDgEp957i8tigQZtDNGqY0LGG89Kkc4-8UuIM3p-WftgCEsyqyRqCwHEVYTpfTQTgLIUV5PaCMZKjXIsYZS6ldWVx_C85n8iWp5_K-HSrGe-51S_AC4T56kJHPEVdmnOoIxYpe68aDfkpHpJmsz6MEwSGKFlltBAwS_65UO96Wjo9FYbXUOIEopZIKioqIrmMlu1WSFHBCodIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از وضعیت اسکله شهید رجایی بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70692" target="_blank">📅 09:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70691">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iknk_7E5bLbHJQbwJoWVQTeIMVI98cDTvzNJOipaiVvk5EvL_go5cTfAMg_599sqDcobpUY-jeho8jprJ4MX8Yb6tFcnFuN8-UFb51PJRAGQ3qUBCsQEE9U7pWjaOfYFwWp5sBzJ2bGGhLMBcRkpeoazxScQVAyim5wiq5z9qasGoWCzGlMKBFUG7vw_VPNJb_t7kKiZ0YJJm5I5nQRxlptQ6HCauu68UgJKCLDmAb6g-cCYwKOb-di9MGkFfEPXV4tPB24QYqGzu21EsFo8OP8tfSognRg66rmUsP-ejmEizDnWYP3RLbJ71goXo2sUNANZY54K0v0nX6IBvabFkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
وال استریت ژورنال:
ترامپ بازگشت به توافق اولیه ماه ژوئن میان آمریکا و ایران را رد می‌کند و در عوض بر این باور است که تشدید فشارهای اقتصادی، تهران را به دادن امتیاز واداشت خواهد کرد.
ایران تأکید دارد که هرگونه بازگشایی تنگه هرمز باید بر اساس چارچوب ماه ژوئن — شامل رفع تحریم‌ها و محدود کردن فشارهای آمریکا — صورت گیرد.
پاکستان، عمان و قطر برای میانجیگری تلاش کرده‌اند، اما این گفتگوها پیشرفت چندانی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70691" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70690">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbhbykSrM3JMlsRcJ5BSkpalvBXkz8Fa2LMnUY_-Gzhq5CnSl8DkXDRf0tHYii2bkpIinawxMrh0AaYPMAlzIARXrUCjxS-Exym0aGeYN6dW6CBz-NBdPOfBIU3_4TmcCEmXRRgaCaQTUBJJNe-x7a0084jCY97hIzAAjxIRoiXGJRlh2OyU5Or60kOg0T84u2IzryX4Q1Jr6AWrOL8rI8CNsrPedS8AuqD4y4XMa3sjb6M9Bx48oSw3v68wwae_qx_MygTd7hXhH4rXzQd4bRXhn3BlftvgqtWg1Q_qrHX2TX4_QWSyrRYX8lFPuP9Lt9BICgXl1K6lZNMiJ5xx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایران کشوری رو به فروپاشی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70690" target="_blank">📅 02:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70689">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qydw3ZJngelftcpbPQcp7wVzWFa5hF4UIIQCxyPbut-Wki4UL6NZ-ShEnDRVuA5HWIpIfDVP4yXqLuigGmoLKC3Ohb-77VqCZSWUJhxQYsIOds6QCC70OL_LWMGWVbl8PI75-jT-KbVU4P5JECUiTOz2AcLB82WtdSZzQcKn3pD8voyV8ZXSq6B0INfBrl2rk5IRAzxm0ZwyHL1Kunm8NWjc--OZQMjuWpmrtCSbGWV7-r1ZT1kME6SxKICVhin0I1ve25Ss_kxCvoFw-hxrT--po5VoGd1fU8d5HHFIjO8fkwomhD0LcwSsBw2wGUWDnV876-ufhXBzLWege5a6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت! می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.  @News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70689" target="_blank">📅 02:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70688">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSAhbVOpAdOXeE8db6mNv4rAJjRcWFKg9yJj-aFByQfx698WcSMfmYkpucVmpFYmG9aU2VHk0f-5p107dYhSebKynqmVXxucJU_mLyqTWXYLGbolYf0KuzkX1ahBhO2e08M9o_ksTjADARF_CmD-VbWrmDaTBhODphb_MZOE1xAm9JecYxtiaUD85jUXfEcKeMnQWSnsOOMKD3PwEpy1CLhULzagAfATusL98Ms9RBP4rQKKiJ0V5cOQdR1n6f5NpdwGqrDO0j98dKz-wQFHwOse0cgkMD05NX2OaLFr-QS4QG76MJg_dgf9_PhguwlbUHFNswcjVhvxP2BX_euyKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
ترامپ رده‌بندی رؤسای جمهور رو منتشر کرد و خودش رو به‌تنهایی در رده «بزرگ‌ترین» قرار داد.
🗣️
جیمی کارتر و اوباما و بایدن در پایین‌ترین ردیف«بازنده‌ها»قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70688" target="_blank">📅 01:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70687">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭕️
تریلری که راکستار به صورت رسمی از GTA 6 منتشر کرد
💢
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70687" target="_blank">📅 00:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70686">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_7tcpWYPFSDKpUciX_lvhd0T8vArIa85RutaNNhvWK-Ja6c1ToW0xkmv9fPT5iV-ygQFnJ06jMZolfPn58lvdd6TGoW7YZrMmn7y5X5pw0AX47bfU3lCQHrCQbNVp5z0QvcmFhv4VCOd8pTJvnwnrplYuSUZ__6JrsUzDBJsSSP_EjuAc6eJ6rX_0OgyA7Bja9K7QIjcX3_L-2Ec5mTfrgzxVqIpv_PYsY0Eiup3ZTXRNvDWkkkhqog9xbVsjQxXiI5CVfpyE-re3WpWzLcrzU0Zds9tMfKxISlBFqbNBGsGoFcOex0GujiEdl3GAoQz2wGzASuyXYnwemQZyMUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
درحالی که دلار به تازگی از مرز 200 هزار تومن هم عبور کرده؛
دیروز پزشکیان به مناسبت گرامیداشت روز کارمند، از تیم اقتصادیِ خودش به خاطر عملکردشون تقدیر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70686" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70685">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=MSgwZaw-U279Rz2XYAgj8gDFwTtTyuNaNgDmEQ8kHijJguLPY6e1HN_8pFY_ePFXseHR1sqWxHF-dTag8FX4zBHCCkycfsEDjjMu9Zc33R4wbyz4HRzq9AFrbiiy3c860nPMO_e_i8NTNuQJtmYY0T6wQjtFGhoPX6PLZx7EIn8DrELFZzND18Fnyr4t34rJBv3pSGPyvZRzsk-n6YUqVr-FN-SAstCUqwptz3L31EmKiSSs8oGIIVCEA_W7JUeSQXyOvlBsXozFD_nCDYrgjfBtPAI2W2m90nLjDtkgb-9fPqj-4_kAxCBmF6LZvHwflMT2f1zU8tDNVp4nr3FdDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=MSgwZaw-U279Rz2XYAgj8gDFwTtTyuNaNgDmEQ8kHijJguLPY6e1HN_8pFY_ePFXseHR1sqWxHF-dTag8FX4zBHCCkycfsEDjjMu9Zc33R4wbyz4HRzq9AFrbiiy3c860nPMO_e_i8NTNuQJtmYY0T6wQjtFGhoPX6PLZx7EIn8DrELFZzND18Fnyr4t34rJBv3pSGPyvZRzsk-n6YUqVr-FN-SAstCUqwptz3L31EmKiSSs8oGIIVCEA_W7JUeSQXyOvlBsXozFD_nCDYrgjfBtPAI2W2m90nLjDtkgb-9fPqj-4_kAxCBmF6LZvHwflMT2f1zU8tDNVp4nr3FdDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بخشی از یک موشک ضدکشتی جمهوری اسلامی در نزدیکی سواحل ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70685" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70684">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=R1uOLBArAYkOqgQOmyIpOvakFaPPt-Niom76m6ss0QYErd4Wy_ij69I6UVKqth-dAqsBhuS5_kzPAktqTulfZzWcRnqF_u9JClrl2dw3NWNWJ0GaHyfEbmZJPOKV5I-gCq1GUAVJKKDdcfIZjq4SADPTlrNPieIIWe67LkOUPYFUHyDcGSjrtyBaLS7TV6N4s_lBH09qRPakhjfMSyzdzG5j9XqH-3KYYsVtHQn_o2SKP0IoH-mpmvz8Tj19B-oxkF6loYZs3zMhvElgY9BlwLuqGJU7Z3Lb3H5ZvKyV_da9tZmU7plSXwuREWy4z9sh1J-pNbemujGTcB27tTt8Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=R1uOLBArAYkOqgQOmyIpOvakFaPPt-Niom76m6ss0QYErd4Wy_ij69I6UVKqth-dAqsBhuS5_kzPAktqTulfZzWcRnqF_u9JClrl2dw3NWNWJ0GaHyfEbmZJPOKV5I-gCq1GUAVJKKDdcfIZjq4SADPTlrNPieIIWe67LkOUPYFUHyDcGSjrtyBaLS7TV6N4s_lBH09qRPakhjfMSyzdzG5j9XqH-3KYYsVtHQn_o2SKP0IoH-mpmvz8Tj19B-oxkF6loYZs3zMhvElgY9BlwLuqGJU7Z3Lb3H5ZvKyV_da9tZmU7plSXwuREWy4z9sh1J-pNbemujGTcB27tTt8Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت در آستانه آخرین روز کاری‌اش به عنوان سخنگوی مطبوعاتی کاخ سفید، سخن می‌گوید؛
«احساسی آمیخته از تلخی و شیرینی دارم. تلخ است چون شغلی را ترک می‌کنم که بسیار دوستش دارم؛ کار کردن برای این رئیس‌جمهور، یعنی رئیس‌جمهور ترامپ، افتخار و موهبتی بزرگ در زندگی‌ام بوده است. هرگز کسی مانند او نخواهد آمد.»
لیویت پس از ۲۰ ماه فعالیت در این سمت، کناره‌گیری می‌کند. دلیل این تصمیم، تمایل او به گذراندن وقت بیشتر با خانواده و دختر نوزادش است، هرچند او همچنان به عنوان مشاور ارشدِ خارج از دولت به همکاری با این مجموعه ادامه خواهد داد.
«آن‌ها در مقطع حساسی از زندگی‌شان هستند و بیش از پیش به حضور مادرشان در خانه نیاز دارند؛ بنابراین مشتاقم که وقت بیشتری را با آن‌ها بگذرانم و در عین حال، همچنان به عنوان مشاور ارشدِ خارج از دولت در خدمت رئیس‌جمهور باشم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70684" target="_blank">📅 23:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70683">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c174815597.mp4?token=MhlPtFn3m1pQu2FUeglLIZTZe8QUbc7-zH6woa39NTzsB5MDLvBwFaV2t9s8tVisSlfDr61owyaV8pNex2IlT5sTFAeFj0VhLOjjt54ZzhbD1DSPr6mwbHLBQDIcYfr-x0pIrERQaAUyp7ueqO8c0HNiMOGHYJaYmbN6a1NuTn3XQUK8Q46D3cxtxauvYmQPZwcudFyfiPdtT26UT1n89DEbjgNUvSLpUIunouj6HPZArsl3ShJP7ueoUfsJ7ObAlE8CTZR-oCYKD6sqbU2C4fHPNbemWtK7eqcTvD-CH2FJyhSsO1rTkCW6UI5g86OZyxBOMLJlwNG5qYMqU08vPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c174815597.mp4?token=MhlPtFn3m1pQu2FUeglLIZTZe8QUbc7-zH6woa39NTzsB5MDLvBwFaV2t9s8tVisSlfDr61owyaV8pNex2IlT5sTFAeFj0VhLOjjt54ZzhbD1DSPr6mwbHLBQDIcYfr-x0pIrERQaAUyp7ueqO8c0HNiMOGHYJaYmbN6a1NuTn3XQUK8Q46D3cxtxauvYmQPZwcudFyfiPdtT26UT1n89DEbjgNUvSLpUIunouj6HPZArsl3ShJP7ueoUfsJ7ObAlE8CTZR-oCYKD6sqbU2C4fHPNbemWtK7eqcTvD-CH2FJyhSsO1rTkCW6UI5g86OZyxBOMLJlwNG5qYMqU08vPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای این فرد که در حال وایرال شدنه:
الان که رهبر رو زدن، مسئولیت این کار زدن رو گردن نمی‌گیریم، جرأت نداریم رهبر بعدی‌مون رو نشون بدیم. به هزار تا داستان دیگه داریم. ته جنگ‌مون معلوم نیست. نمیدونیم خونه هامون میمونه، خانواده هامون میمونه، ناموس هامون در خطر هست یا نیست.
بعد بگیم که آقا ما دست‌مون رو تنگه و هرمز گذاشتیم. خب حرکت بعدیت چیه؟ بعدش میخوای چی کار بکنی؟ خب من... شما پنجاه سال این کشور دست‌تون بوده، نمی‌تونید یه تورم ساده رو کنترل کنید. ادعای حکومت امام زمان رو دارید که میخواید دنیا رو برای ما بسازید. خب خیلی خب.
بحث ساده فرهنگی‌تون، آمار طلاق‌تون، آمار احتکار‌تون، آمار دزدی‌هاتون. یکی یکی آمار، یکی یکی دارم میگم. میدونم تمام کل و هزینه سرمایه این کشور رو برداشتید. همین آقایان استفاده کردند به هر قیمتی هم باشه.
من یه حرف رو میزنم. همین آقایان سپاه رفتن میلیاردها دلار هزینه کردند، عجیب و غریب و زندگی من و شما و بچه هامون و نسل های آینده رو به فنا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70683" target="_blank">📅 22:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70682">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=AtDPsDgX5AsArXWJkaW8v2Hs-ihkDU2GqHn5-ZZ88VGr-VXwj8Sl0JYGThl-sa9AItiKy3HC94TBLjqQbtJmJkzNAYztmOClOSmK1rkNLlBF4GJw6m8tUWtHi4axp9ZTh0rgPqaZOp3qgViQHzU4TpeJMFED5YIfJYeG12LvzgpQMHLSMNkrGWwLpdD5tQBAtT3tcIry7V-lTr5p9pPtGYVN-J54hqVRNBgEDBZDisfkW4d42QJmMcIvShTqeirbeXA4sfP_vCLDMSHmcxOVFosgy8tWvbkNSz6HLV5QDHaeH1JcvtVGwPqH3PeSLtmtdYlz4EjDPNu95SQLQ7J5kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=AtDPsDgX5AsArXWJkaW8v2Hs-ihkDU2GqHn5-ZZ88VGr-VXwj8Sl0JYGThl-sa9AItiKy3HC94TBLjqQbtJmJkzNAYztmOClOSmK1rkNLlBF4GJw6m8tUWtHi4axp9ZTh0rgPqaZOp3qgViQHzU4TpeJMFED5YIfJYeG12LvzgpQMHLSMNkrGWwLpdD5tQBAtT3tcIry7V-lTr5p9pPtGYVN-J54hqVRNBgEDBZDisfkW4d42QJmMcIvShTqeirbeXA4sfP_vCLDMSHmcxOVFosgy8tWvbkNSz6HLV5QDHaeH1JcvtVGwPqH3PeSLtmtdYlz4EjDPNu95SQLQ7J5kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سر دادن شعار «مرگ بر آمریکا و مرگ بر اسرائیل» در نشست علنی مجلس
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70682" target="_blank">📅 21:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70681">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=U96k6kgbXFhmeJggSY-BsFmfjODiRZHSUyAFli_XaUTJ9r1QvJtlGuqQS6DptEipGG55J86nTHBj244xY6LgX3DjkXIfQW7K1Zz9eEiggsDnfF33KEf7vIXax5E6wJHKJKnAcqySKUOIJ1ie9v-RwVON-dkQLeAop0HbPti6CWvHxrIwdkO8GT4VjOw7kUIT7yOtZcihGpnN-DPcEe2LmDMQVZYSVxhUIbNPzLdM6YVfwEA8SCx4N8ZB6o2aQKmUg3YTmb_uIAHwTAvKLNV5BRM-GRtkCDe4LOsRh97YoyzlQMdFtT66fJWAxmNwDnjMEK__OeDiF-7Tl5LMMuxJfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=U96k6kgbXFhmeJggSY-BsFmfjODiRZHSUyAFli_XaUTJ9r1QvJtlGuqQS6DptEipGG55J86nTHBj244xY6LgX3DjkXIfQW7K1Zz9eEiggsDnfF33KEf7vIXax5E6wJHKJKnAcqySKUOIJ1ie9v-RwVON-dkQLeAop0HbPti6CWvHxrIwdkO8GT4VjOw7kUIT7yOtZcihGpnN-DPcEe2LmDMQVZYSVxhUIbNPzLdM6YVfwEA8SCx4N8ZB6o2aQKmUg3YTmb_uIAHwTAvKLNV5BRM-GRtkCDe4LOsRh97YoyzlQMdFtT66fJWAxmNwDnjMEK__OeDiF-7Tl5LMMuxJfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ما یک خلیج داریم. یک دریاچه هم داریم. حالا چیزی که نیاز داریم، یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا آرام را تغییر دهیم
😠
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70681" target="_blank">📅 21:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70680">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d624c250.mp4?token=HSWXsmUPNHkuC04Ig11fCfOWrwjQRUyp1Kr6OYUHX9uU6Mz8-7iZkTj0Y5fKsfVSYjAWZgBxp8EdLBG_BeSON7laMzKJJwbScf3gmhpsWQooowiMy7PEVAClu1N2LTr3CJLQ1yKQIbs_-4luz3-eSwt6z5PjTPU3iNk9z7cAz1UhL_bFYtV-FqAcc29gGwFJL1pZtG3dn4q_WTv8om5kkobbCEVsAA3svF866nU1Qrwa1mKKNEPYdEVWdbuQIoURBNJBJ22lR3Eq_L7IkesmFx9er__T1eHViXspKzGjNNZ_Eg1B0IdLlTA20_x3U06q5K5PRGNDa8yD8A1TKArYOKPtT4Dhh9SZji16yClLckrEyo_VWzvQwOGBciuDhzg7vzePZqLGYj7i-NNNkK6zZc1_Jc29_5QoGbqP9mCx5KvAjTtGko6VwJzvx2GFLJbAB84varqyZeH4FfCZXwiAzVQRWNkMtXvTezoueMm2rh6Y_dc8go55HWntLs-cntskI-HlmcBligvM3QHmf6k-9Sq12alRRUqHbyDvH7WaTfgrxZNQN3WByiLxAVbRJFBxpCdk9FRiLFpnH_Rw_e1EG2_P3wqqg6LNsJNPC1DRigKsbBXHkfWFKdjjF-UZ9PL1SEsQHwziOeDZ3Tr5Naq9qMtXBDWLjpyOsNE5WHlxve8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d624c250.mp4?token=HSWXsmUPNHkuC04Ig11fCfOWrwjQRUyp1Kr6OYUHX9uU6Mz8-7iZkTj0Y5fKsfVSYjAWZgBxp8EdLBG_BeSON7laMzKJJwbScf3gmhpsWQooowiMy7PEVAClu1N2LTr3CJLQ1yKQIbs_-4luz3-eSwt6z5PjTPU3iNk9z7cAz1UhL_bFYtV-FqAcc29gGwFJL1pZtG3dn4q_WTv8om5kkobbCEVsAA3svF866nU1Qrwa1mKKNEPYdEVWdbuQIoURBNJBJ22lR3Eq_L7IkesmFx9er__T1eHViXspKzGjNNZ_Eg1B0IdLlTA20_x3U06q5K5PRGNDa8yD8A1TKArYOKPtT4Dhh9SZji16yClLckrEyo_VWzvQwOGBciuDhzg7vzePZqLGYj7i-NNNkK6zZc1_Jc29_5QoGbqP9mCx5KvAjTtGko6VwJzvx2GFLJbAB84varqyZeH4FfCZXwiAzVQRWNkMtXvTezoueMm2rh6Y_dc8go55HWntLs-cntskI-HlmcBligvM3QHmf6k-9Sq12alRRUqHbyDvH7WaTfgrxZNQN3WByiLxAVbRJFBxpCdk9FRiLFpnH_Rw_e1EG2_P3wqqg6LNsJNPC1DRigKsbBXHkfWFKdjjF-UZ9PL1SEsQHwziOeDZ3Tr5Naq9qMtXBDWLjpyOsNE5WHlxve8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
🇨🇦
ترامپ فرمان اجرایی «تغییر» نام دریاچه انتاریو به دریاچه آمریکا را امضا می‌کند.
🎙
خبرنگار:
با تغییر نام دریاچه انتاریو، چه پیامی برای کانادا می‌فرستید؟
🇺🇸
ترامپ:
هیچ پیامی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70680" target="_blank">📅 21:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70679">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=tV29hNJOxs92B1ARVvs4-F0nIwLyIKrLHCDG0ElzYqSvSUrhskupo7Dyd1sFOinBfRuw9GYsksHqYFLTWe2nTDeGqpX4Z_i6rSYDjrixeYmS6mns6t4blSIL0_1zEtwbHKltG-me-27wmIgocceL8kA0u_Ov1cQxcgkjhLx06n9XKvkAyZpeBkHUggpfPqiVlPh6ihF_HjM-5d02ccEqsZ-hmjvPgMK-z8pg3xeOQzSBa2SiBCrmi9nEmdb7aQiRfaDRAQkfoFuMOTk9uhqTd7AUq3MhLG2E8cv6IkcxeM0l7JtDylDKDPAQ4m_UcfNI_YHqPfbQBEA2fWigQ7-pxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=tV29hNJOxs92B1ARVvs4-F0nIwLyIKrLHCDG0ElzYqSvSUrhskupo7Dyd1sFOinBfRuw9GYsksHqYFLTWe2nTDeGqpX4Z_i6rSYDjrixeYmS6mns6t4blSIL0_1zEtwbHKltG-me-27wmIgocceL8kA0u_Ov1cQxcgkjhLx06n9XKvkAyZpeBkHUggpfPqiVlPh6ihF_HjM-5d02ccEqsZ-hmjvPgMK-z8pg3xeOQzSBa2SiBCrmi9nEmdb7aQiRfaDRAQkfoFuMOTk9uhqTd7AUq3MhLG2E8cv6IkcxeM0l7JtDylDKDPAQ4m_UcfNI_YHqPfbQBEA2fWigQ7-pxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
چرا بانک‌های چینی را که با ایران مراوده دارند، تحریم نمی‌کنید؟
🇺🇸
ترامپ:
چه کسی گفته که این کار را نمی‌کنم؟ شما نمی‌دانید که آیا مشغول انجام آن هستم یا نه. لازم نیست همه چیز را اعلام کنم.
🎙
خبرنگار:
با کدام‌یک از رهبران درباره قطع روابط با ایران صحبت کرده‌اید؟
🇺🇸
ترامپ:
صحبت خاصی در کار نیست. ما نمی‌خواهیم با آن‌ها صحبت کنیم. تنگه باز است.
اقداماتی که در قبال ایران انجام میدهیم به معنای منتفی شدن گزینه نظامی نیست.
گزینه نظامی همچنان روی میز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70679" target="_blank">📅 21:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70678">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_8brylnzWPpUqCL2jyIMm7Hp4Uqkhs1_pHkRzmksJU6rquOeNsOye7ZJkhwZssHOMlPuB7W4RLbyUUpIXX2U84v4Mjp8q-SL4VJfdD5O-Uo826mjH_wcswU6XxzmA1SNEK4I4p6ZXmDeUs7L4zWyr4ZXA0ewMT-cj5gdoKklRZsyjPBye4UrxdZM6j5NIEQ-NLJT9M0165sw_dK-Azi87mSAts6CKT0TjDVaA1UscDgDqup4IRYQEfRJSfhZxlJB1RKWvoF9U8YREsZOU_UbrGwX5hhbTUCwQBTmRNRTHwWhDVow79KQCIIMSIcusRdzNCIUy2jfm529A87hF5ytA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
🇵🇰
کویت و پاکستان یک توافقنامه مشترک دفاعی و همکاری نظامی را در اسلام‌آباد امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70678" target="_blank">📅 20:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70677">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukj1hxRY8ROXplsKjyAM9P3mMmEuYnp7gIY_uuULi_IC4o0UMIbW8CGdBK89y8anRBjsfFg8ZissuOw0ZC4Gzz0iJn56F2pl3zdMs_0MTwc0IQr6xtPIXzP8CAGjV5z5mDWvuzVuapufrwW3tXZ9fmOqUVaKYN1o5zUIasVCyfW8a-aGKjR950Dn81NZMl9ycVaTcc35lpVb3u6aIyAaAX6DRWtPQKOv-RcdESoGawCAswop7NabR4mpArGtaaqIYBsRzYBe_0BTFxadSOONtEj7EcxPcDilqid3gtiUGxDIt23_pCeSEwwJ7mR8b--5EuqtqQNS5C1utcGdJSsc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
قالیبافِ در جواب بسنت:
این امپراتوریِ رو به زوال، به‌جای سرازیر کردن میلیاردها دلار به سوی اسرائیل — آن عامل نیابتیِ تروریستش — و صرفِ هزینه برای ۷۵۰ پایگاه نظامی، می‌توانست آن پول را خرجِ مردمِ خودش کند؛ اما نه، چنین کاری برای این رژیم بیش از حد منطقی به نظر می‌رسد.
اسکاتی، رفیق، اعتبار تو در خطر است. کاری بکن.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70677" target="_blank">📅 20:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70676">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=HNtWo6rBIGtuxVa7T-YhKT1P7gTo5SD3NbsHaOfJOxJYHjB7Erae9_rbvUwvluLwjDTlerTVZYOpQEvant3NRnGqNnM9250b6Hl5TnQbntjZcTRuIGxnEVVlZuAvaZVWFuw2odkRjF7-Xp9aydIsY_TMYnhNilIqrzXDMS8887rMd38IXfG1Qh8hk5vWUwqvU1QTHRg357urf_aNjvKbEP-TF1kFcgrTDnwRW0b0OyrJDenO4m0SimOXpW4yC3ltjKmIqEnv6-DdpF9nvVNIcXrwUNfBhug9qHun8YP0umS7IE5L2_EARhdr7M9rIqFkwKGP1yyt-4wRNhE2J6hTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=HNtWo6rBIGtuxVa7T-YhKT1P7gTo5SD3NbsHaOfJOxJYHjB7Erae9_rbvUwvluLwjDTlerTVZYOpQEvant3NRnGqNnM9250b6Hl5TnQbntjZcTRuIGxnEVVlZuAvaZVWFuw2odkRjF7-Xp9aydIsY_TMYnhNilIqrzXDMS8887rMd38IXfG1Qh8hk5vWUwqvU1QTHRg357urf_aNjvKbEP-TF1kFcgrTDnwRW0b0OyrJDenO4m0SimOXpW4yC3ltjKmIqEnv6-DdpF9nvVNIcXrwUNfBhug9qHun8YP0umS7IE5L2_EARhdr7M9rIqFkwKGP1yyt-4wRNhE2J6hTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف عجیب پمپ بنزین در کرج دیشب
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70676" target="_blank">📅 20:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70675">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU7_gFTgS_HsTmSUrwhSbn6FD7bleRJfrdMkswJmSKo_bynZKOSq5e-6a4K60MvMaFgQmkIeYkC4rZplskZqldLhBERERsJeX22bMZwsKwMtj97O931UBrbV5Rmn8KANReguddtWXm9bEZriB2OOoUtlMffWysywToUrtOryPvcYC03J0J5rZtfGa33k2i4ZsFo5e-DqbzCTc2y0fIbJlRwlxlbBtVFuivyroAbwC5ZLr7Dz-ggJraobjzNpf84GHDOY2fVzX11K-8caRd3E1pvlp2gysF0jZvbRoURStByqlYKpQOJ0RZ8gXtXDu3Ojw4ieq-NfPv6jukvN_PxEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
هم‌زمان با تداوم اجرای محاصره علیه ایران توسط ایالات متحده، هواپیماهای جنگ الکترونیک E/A-18G نیروی دریایی آمریکا بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند.
تا تاریخ ۲۷ اوت، نیروهای «سنتکام» (فرماندهی مرکزی ایالات متحده) برای اطمینان از رعایت مقررات، مسیر ۷۵ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای بازرسی وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70675" target="_blank">📅 19:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70674">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0833865a38.mp4?token=tT_RpcMMbNYXDK5Ev3dITLuqkhoVVZUgJ7Blu4JsxMoeiiFaesy_rCNG7Sz6z_aA_w-0SKvyw2TyqW9VpiWbwj4odsXaqk3l7wkAMd98p73-mUwBUL-pSy-CRP2r5Xxz34kZYQSlT1XV42UgyC0c6-886mAIEd0NKL1n_RRXoXrJVoandDeyzBPJ5sXan7ayZ6FUxh1j9xrgAhYfSc2Zbx5owTOhgO1H3DUJePWTeJmfMZDsp8A1Q1rgStV0EGNnNYGM6pZSZzjUv8GyJ_S6o2zeT-w8xCY1ZZZCmrjy_j6gzwbgA1qbE1YcbQ_byDN12WKrv6p6qca3Op-RNus_eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0833865a38.mp4?token=tT_RpcMMbNYXDK5Ev3dITLuqkhoVVZUgJ7Blu4JsxMoeiiFaesy_rCNG7Sz6z_aA_w-0SKvyw2TyqW9VpiWbwj4odsXaqk3l7wkAMd98p73-mUwBUL-pSy-CRP2r5Xxz34kZYQSlT1XV42UgyC0c6-886mAIEd0NKL1n_RRXoXrJVoandDeyzBPJ5sXan7ayZ6FUxh1j9xrgAhYfSc2Zbx5owTOhgO1H3DUJePWTeJmfMZDsp8A1Q1rgStV0EGNnNYGM6pZSZzjUv8GyJ_S6o2zeT-w8xCY1ZZZCmrjy_j6gzwbgA1qbE1YcbQ_byDN12WKrv6p6qca3Op-RNus_eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس نیوز:
🇶🇦
نخست‌وزیر قطر در حالی وارد تهران می‌شود که تلاش‌ها برای کاهش تنش‌ها در این مناقشه، با هشداری صریح از سوی رئیس‌جمهور ترامپ روبرو شده است:
ایالات متحده تا هر زمان که لازم باشد، به مبارزه ادامه خواهد داد.
تنش‌ها در تنگه هرمز همچنان بالاست؛ جایی که ایران اعلام کرده این آبراه حیاتی تا زمانی که واشنگتن خواسته‌هایش را نپذیرد، بسته خواهد ماند.
در همین حال، ایالات متحده با اعمال تحریم‌های بیشتر، فشار اقتصادی را تشدید می‌کند.
در داخل ایران، فشارها رو به افزایش است. صف‌های طولانی بنزین، تورم فزاینده و تضعیف ارزش پول ملی، مشکلات اقتصادی را تشدید کرده و نگرانی‌هایی را درباره احتمال شعله‌ور شدن دوباره اعتراضات برانگیخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70674" target="_blank">📅 19:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70673">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=fRfyokMIS_L71js9YC6MthEVuZJ-M_Kdil2PlYFJFT7euo03zaM5IwQiSG1gH7s_J-au_KNkymEUobJM4xMECvuGWwPywlUmZw0w742H88pEalMzIh8hjsz13M9iMTJUCDbZvAbng46tQwPUY3QMsLsZpwHUUWSOfwDD7bA3SM10hw0HW5UJ4sjTPxx9Nnt3QEZ-TCbk_TXHW6vwWyFIbdncaLR9it1Rd1BYmUnxVHRUPCT2dR80_TyolRD0e5rqdfC1LEJnQx5uZDxQXM0e7JEauOFUBDsJxdVGP6UjsNMdglKbVhkemYHarue1eBq5mVO5T9CxtYNKzl6D826fbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=fRfyokMIS_L71js9YC6MthEVuZJ-M_Kdil2PlYFJFT7euo03zaM5IwQiSG1gH7s_J-au_KNkymEUobJM4xMECvuGWwPywlUmZw0w742H88pEalMzIh8hjsz13M9iMTJUCDbZvAbng46tQwPUY3QMsLsZpwHUUWSOfwDD7bA3SM10hw0HW5UJ4sjTPxx9Nnt3QEZ-TCbk_TXHW6vwWyFIbdncaLR9it1Rd1BYmUnxVHRUPCT2dR80_TyolRD0e5rqdfC1LEJnQx5uZDxQXM0e7JEauOFUBDsJxdVGP6UjsNMdglKbVhkemYHarue1eBq5mVO5T9CxtYNKzl6D826fbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
فیلم از منطقه صنعتی بین کفر رمان و نبطیه الفوقا در جنوب لبنان پس از یک بمباران هوایی اسرائیلی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70673" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70672">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvzbxpiIkpXdmriv--Fi3gV8Afj1jbVgDw7wFo9G1DqMVr9uI_K7lYwwgJTFzKJroMsyUrqTm5uMKVlVVrc3qUNDWFYt22qtkwrNADXM6Jze5fF1gxKEsF0RlvzZIXQcfmS3cry9xxmn2geOYoqm2j5WX4VPxKO-ati0oEwCho5FTVvSR9VdkWmJi8Y-5VOahhdM2lXmNCftpYAsqAgw9f_D2APaX1PyipWtoXvQjwgYOvzBo3GgFSQMGu8fSn_XSQl6FP3R3VrHRb0X5NKjTop-wR1lPDWZwbK8IM8ngZp-y505kB4zhmuO7_5BALt6JW_0z4nXpcetpV4igx5rlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
〰️
بِسِنت وزیر خزانه‌داری آمریکا:
در حالی که مردم ایران برای تأمین نیازهای اولیه خود با دشواری دست‌به‌گریبان‌اند، رژیم فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.
این رژیم باید به‌جای سرازیر کردن میلیاردها دلار به سوی نیروهای نیابتی تروریست خود، آن پول را صرف مردم خویش کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70672" target="_blank">📅 18:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70671">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=NJ0zEeIZC_W9fdLH5eDxU4Yx9chK4iRNOy7tuMGcFuweg4Ymk8JW9cIoUjhdh3qiJOGj2rPQBknokMQJPXQepDUCXarytDzRdRp1b-zEtLWm8846Z7nmuGrb5iwP8KGUBwMuNwxAVHw90zRPt7eRTSK5Dibe6mZhubTbFMtsJg-o4SubWwGr8PszMi2vgys3jfYB_-noLFlHmpvl4saG9iLhweUvknejT_6_xmTI1JLaGnR_ldyZ8Sw2FXr5qRjz2QaLilNd-K85zEpfo2pTUhtM7gD0c8EHyunos_rjtkSabSWnL8H1Zcdb1eo4eBEmpWYfKnbpdtzrT2q5_VHjOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=NJ0zEeIZC_W9fdLH5eDxU4Yx9chK4iRNOy7tuMGcFuweg4Ymk8JW9cIoUjhdh3qiJOGj2rPQBknokMQJPXQepDUCXarytDzRdRp1b-zEtLWm8846Z7nmuGrb5iwP8KGUBwMuNwxAVHw90zRPt7eRTSK5Dibe6mZhubTbFMtsJg-o4SubWwGr8PszMi2vgys3jfYB_-noLFlHmpvl4saG9iLhweUvknejT_6_xmTI1JLaGnR_ldyZ8Sw2FXr5qRjz2QaLilNd-K85zEpfo2pTUhtM7gD0c8EHyunos_rjtkSabSWnL8H1Zcdb1eo4eBEmpWYfKnbpdtzrT2q5_VHjOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
کارولین لیویت سخنگوی کاخ سفید:
در حال حاضر هیچ‌گونه مذاکره‌ای با ایران در جریان نیست.
این وضعیت تا زمانی ادامه خواهد یافت که ترامپ احساس کند آن‌ها ممکن است به شیوه‌ای معنادار پای میز مذاکره بیایند.
ما هنوز چنین چیزی را مشاهده نکرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70671" target="_blank">📅 17:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70670">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=agp6vkp2qXNVFbYnQd_dbqdle6HzHIMz4ftrvhdmC_PLM8pjJARnwzwDG3IBcDdy5RFk-BAzck7wloV8F6R3A48ObnbC1xxklr0kKEEHo28YWp6Qck1KoFvzZ6bO-fKktux4Z5l4QawVcfdqAgA7zRYPIDgU6injjIRxEL8Z-Gl-oGKVvMdqZgboR5K62v3KYCwSDeE8Sm2zsBy1AVMGwuiUyhTRwyYUPkD0iWj6V1yLdFjGswsSf6kEDKcEEb6KOEmNH07xkuQY90cUja8pyStWy17Zon7Br_-uvZen7h8eWmQEkkkggGQjd1O5EZ_vpjZi3CAnu4hfMpFdYqX4Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=agp6vkp2qXNVFbYnQd_dbqdle6HzHIMz4ftrvhdmC_PLM8pjJARnwzwDG3IBcDdy5RFk-BAzck7wloV8F6R3A48ObnbC1xxklr0kKEEHo28YWp6Qck1KoFvzZ6bO-fKktux4Z5l4QawVcfdqAgA7zRYPIDgU6injjIRxEL8Z-Gl-oGKVvMdqZgboR5K62v3KYCwSDeE8Sm2zsBy1AVMGwuiUyhTRwyYUPkD0iWj6V1yLdFjGswsSf6kEDKcEEb6KOEmNH07xkuQY90cUja8pyStWy17Zon7Br_-uvZen7h8eWmQEkkkggGQjd1O5EZ_vpjZi3CAnu4hfMpFdYqX4Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت!
می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70670" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70669">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CewCeJMLFNzGy6a81pGUExvTs8gAYCLmses0q7BExNfEPw8ZzZnQfZZDJ4idfHSqEYKYrRVXC7-5q-TU011gsyqGC5HDL61TajZJmdgcK03ASvqAGbSWYfeuc0UG5eDO3zGrOxy7tIbbXs8lTv1E6N-vLRXlo-tDnggq403YEPYvU_YkRERNWtyZaPXVfUtVajQFcGTWsU0gz1v5t5RB90lEClCzaq4nRYMU38vm6w7NwmrBZD883n0d5nr7tiGHAQLuGQLEcKgEjgMeIgEjZbQKyaWqgYzmEua5iews4IAtDVit37MCyjkBPlmA-lrgyvpyQ03S-oThPUtDKydJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70669" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70668">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=iXjLt6QqB6L1-U7HFSaJX85isbvkGDpP29I7obieTNx4MV23uXK_NW8RXMcmLhRtxiiwUYNhgGms9cw1LfgzfYs4SYpdqe10qANWIEqYrwKgQzEgtfMKA4jYW5bq7mhCtnI_yMDHnCVBSfasnlribOTWRaAqEmhDLGzp2ScuoFyeZ-e7lH79rxW89YEa99e2AnqA4XPaoKoOr7jSk6_dkzF2OVji8fYFnhyhAjMO6IbjqSbpmS9LjlexNaHD5YqdOlcmsxH9bPQRZ-RiMO0_wYStXnDwaE47tuXL1EcsC0bI1amg6DJzOvq8pWWROgLvCWF6sOU4Vc2VIg9UwoQcvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=iXjLt6QqB6L1-U7HFSaJX85isbvkGDpP29I7obieTNx4MV23uXK_NW8RXMcmLhRtxiiwUYNhgGms9cw1LfgzfYs4SYpdqe10qANWIEqYrwKgQzEgtfMKA4jYW5bq7mhCtnI_yMDHnCVBSfasnlribOTWRaAqEmhDLGzp2ScuoFyeZ-e7lH79rxW89YEa99e2AnqA4XPaoKoOr7jSk6_dkzF2OVji8fYFnhyhAjMO6IbjqSbpmS9LjlexNaHD5YqdOlcmsxH9bPQRZ-RiMO0_wYStXnDwaE47tuXL1EcsC0bI1amg6DJzOvq8pWWROgLvCWF6sOU4Vc2VIg9UwoQcvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بازرسی امنیتی در مراسمی که تحت کنترل حوثی‌ها در یمن برگزار می‌شود.
آن‌ها به دنبال کمربندهای انتحاری و مواد منفجره هستند.
همراه داشتن سلاح‌های شخصی مانند تفنگ‌های تهاجمی و خنجر برای مردان یمنی امری عادی‌ست
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70668" target="_blank">📅 17:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70667">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe281d624.mp4?token=pdU9kEXOZz6mh0Lfm8PORrZB6EOvrW9mzrtFxKA_6qNDjH7oBoE6o_ZPLHhIUeOJkWeBiwf-vTXF1d806htZy5Jfpc8H78I8QN8nimbAzsdIFIgqmcmmqdWQA5JtGa7a9gTVaUKb4B_vAKLhPdFm6vWQVw1esDqnF1OEKsNnahkQrOH2NhKkKcwQAChtyg-OSCb8fPe-rqXKc76tfFEJr3y3zqAGcK_D59_e6opRFlBE3SjfeqYPC7boxOQq1z7xPhurR6tZlvKgBya-xVepw3QYJo2VPc7Ea1rfKh80DX08CW2UCu992MpJv6qjAnG30n5GlSayKT5fgr_GKWng1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe281d624.mp4?token=pdU9kEXOZz6mh0Lfm8PORrZB6EOvrW9mzrtFxKA_6qNDjH7oBoE6o_ZPLHhIUeOJkWeBiwf-vTXF1d806htZy5Jfpc8H78I8QN8nimbAzsdIFIgqmcmmqdWQA5JtGa7a9gTVaUKb4B_vAKLhPdFm6vWQVw1esDqnF1OEKsNnahkQrOH2NhKkKcwQAChtyg-OSCb8fPe-rqXKc76tfFEJr3y3zqAGcK_D59_e6opRFlBE3SjfeqYPC7boxOQq1z7xPhurR6tZlvKgBya-xVepw3QYJo2VPc7Ea1rfKh80DX08CW2UCu992MpJv6qjAnG30n5GlSayKT5fgr_GKWng1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خنده‌‌های علی مدنی‌زاده، وزیر اقتصاد در واکنش به فشار گرانی‌ها بر مردم
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70667" target="_blank">📅 16:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70666">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=TnVjnjbCqVyFPuwq2OPhjY4vOTM9F_Yq90t9L21ic_f3b6LQH9r1cRmAuXv73I_OJ_NAuQ6jVWeAPYfEUSC_juSQkB0o3PSk3i0yIqE3lcpjJ62TXE3-L0uHBZxBQiSTtEhNcIErc-g0hmnAHG47iSGkK2zJRZJTHqXlaXaxmzDhDlNz3uOOMvBhECPs5m8AEmdC4-gZtdiVUq0Os2nfXX2omkD40lJw9hYDE_v88GHEZTmMtwkvntT2TnY2tWEhEA9HVkKX82-N3r4ljZtbBEp18sQzhGsNiFCryNIIoaYZ4G6JidWK4WuqkVRKc6q26B7mYV9TDWEdC8oqCtOwvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=TnVjnjbCqVyFPuwq2OPhjY4vOTM9F_Yq90t9L21ic_f3b6LQH9r1cRmAuXv73I_OJ_NAuQ6jVWeAPYfEUSC_juSQkB0o3PSk3i0yIqE3lcpjJ62TXE3-L0uHBZxBQiSTtEhNcIErc-g0hmnAHG47iSGkK2zJRZJTHqXlaXaxmzDhDlNz3uOOMvBhECPs5m8AEmdC4-gZtdiVUq0Os2nfXX2omkD40lJw9hYDE_v88GHEZTmMtwkvntT2TnY2tWEhEA9HVkKX82-N3r4ljZtbBEp18sQzhGsNiFCryNIIoaYZ4G6JidWK4WuqkVRKc6q26B7mYV9TDWEdC8oqCtOwvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یک طرفدار حکومت :
قیمت دلار همینطوری میره بالا و ارزش پول ما همینطوری میاد پایین
ولی این میتونه به نفع ما باشه چون برای اون خارجی محصولات ما میتونه ارزون تر حساب بشه و بیشتر تحریک بشه تا کالای ایرانی خرید کنه
این یعنی فروش بیشتر بیکاری کمتر و چه بسا درنهایت مهار تورم و توسعه اقتصادی!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70666" target="_blank">📅 16:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70665">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq2j9vO2Y-OGxDRC01fwwKW9NJJeQix9i9uWTo03PqoFWFrcem2Sxp4VYRMUwx006faMyZ8ZJJUYbcNGs4F4oZhCmBC7aboa7g-BvrDA9Dsd7sAxajUP8HIqj3Tr3pN-zgOhPUUI2zRgmBDRPIKxQPi32q0XFkB0me_kH_wRlfl_MYn4_bGIxFutBDzSEuFsyDdnwBGTpbnyhrvdtA2f2RtxIJPiKu5tINao4kJRg5fvrqeqAYajlJL3XQudrzfzuWOYFHGYfEfjDsmnWyN_K67MJ3I9VIPZillKQtuKvjuYyQ2YlghK97-r9Z3i-O4iJmfOkUVSZNT-I-C8PSYGEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
📰
سی‌ان‌ان:ناو هواپیمابر USS Theodore Roosevelt همراه با حدود ۵۰۰۰ نفر قرار است در هفته‌های آینده به خاورمیانه اعزام شود.
این استقرار حداقل ۷ ماه پیش‌بینی شده است.
جان پریمن، Master Chief Petty Officer نیروی دریایی آمریکا، گفته خدمه می‌دانند مأموریت بیشتر از هفت ماه خواهد بود و فرماندهی به آنها گفته برای ۸ ماه برنامه‌ریزی کنند.
این اعزام را در ارتباط با فشار عملیاتی ناشی از استقرار طولانی USS Abraham Lincoln قرار داده؛
لینکلن بیش از ۲۵۰ روز در دریا بوده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70665" target="_blank">📅 15:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70664">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=Tu4pDuHX6VoQ07tnxjdoUAhboM8URahJJoF8mwkiXQgnUPjHpzI-bWbMRNxowrHvUt9knqnkbnAZbEX5GHKIIuS5g7tK6U4tnsfXPlEVAN6ngIn_0W1_sEGbKd4MPFJw0w4_1u4pvu0Qx94o0KAC9HU6Fjhc5l1VjyWECeD_pXvD7ROEb3mX_2VdjIxk8ta69PIb7MHfeGr0kB1V7_xlx6rV61IOK5eTbev-IV8_oGKKqjhK6lc3fGJyn-bRX2AZJKkWdPk1Nt0OqupFwWvuOGasqp6lN0JjAWlfhHj7UubOqeVIytpc_76BD0_LN6Sy5jgknsm0pCHYDC4X-V4Vrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=Tu4pDuHX6VoQ07tnxjdoUAhboM8URahJJoF8mwkiXQgnUPjHpzI-bWbMRNxowrHvUt9knqnkbnAZbEX5GHKIIuS5g7tK6U4tnsfXPlEVAN6ngIn_0W1_sEGbKd4MPFJw0w4_1u4pvu0Qx94o0KAC9HU6Fjhc5l1VjyWECeD_pXvD7ROEb3mX_2VdjIxk8ta69PIb7MHfeGr0kB1V7_xlx6rV61IOK5eTbev-IV8_oGKKqjhK6lc3fGJyn-bRX2AZJKkWdPk1Nt0OqupFwWvuOGasqp6lN0JjAWlfhHj7UubOqeVIytpc_76BD0_LN6Sy5jgknsm0pCHYDC4X-V4Vrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیزدهمین فرزند مادر ۳۳ ساله بدنیا اومد
؛
از مرده میپرسن چرا این همه بچه حالا جوابش:
اساسا بچه ها رو دوس دارم من ، هزینه هاش؟؟ هزینه هاش با خدا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70664" target="_blank">📅 15:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70663">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=GQVtrxB8PJDEosqxKXdX3dUdn7yAlecpzszwSzUMShd012C5WglSOeCs8MTWabzbJC6S7QVUrkRbvepWtBx4JR0oD-Cl04xgSl8entFtxCcvTiURtqKTkdPmsHejrXByn4O_kT7TBLR_U9w0qBOis_jTyeU6WCwGpRx23akMrdBMy59VNUULPfq_-jqObk7nHniZpHLV2aVQA3_5zhe-xUy2rIPbPIWxUeHrJRJW_8OBpb8pSm5s247xoxIaD59QvPkkhBV5l1XcWuhZnd-haDhGLpOwl21efVDfsI1GRFSLTEUeYNHzO1CG6x-S71CxFguhNk5aayYiqnE_DWuAHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=GQVtrxB8PJDEosqxKXdX3dUdn7yAlecpzszwSzUMShd012C5WglSOeCs8MTWabzbJC6S7QVUrkRbvepWtBx4JR0oD-Cl04xgSl8entFtxCcvTiURtqKTkdPmsHejrXByn4O_kT7TBLR_U9w0qBOis_jTyeU6WCwGpRx23akMrdBMy59VNUULPfq_-jqObk7nHniZpHLV2aVQA3_5zhe-xUy2rIPbPIWxUeHrJRJW_8OBpb8pSm5s247xoxIaD59QvPkkhBV5l1XcWuhZnd-haDhGLpOwl21efVDfsI1GRFSLTEUeYNHzO1CG6x-S71CxFguhNk5aayYiqnE_DWuAHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش یه دختره اومد از خودش ویدیو تولد بگیره تنهایی که یهو یه 207 اومد کنارش و سه تا پسر اومدن وسط رقصیدن و تولدش براش جشن گرفتن
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70663" target="_blank">📅 14:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70659">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCFmrqtdIFk35NmUWoDG0Yi5QL_DRLGgdRYi9gyMXjJfk9o3qqcDakAneRBKoQOmfKW8wbpW0tPnxDn_g6E-InyAfPtJNHY4RZ-R18AUkOrz3OCNy7fxNEcGVEzEpmodrAm8ioXVyPiSEbh6zrp4HEKvjjOIbZ01esnwFkE0QDfcdKabgTV8ZaMfAJzC_poZCQTG7dhbcQCVVfCf80DmQEKpJbHA608619JxtFrVt6sZQJOS49n5ysmpUOo4ZdyLwuWqKJuFxyuixek2VlzIYe9aa2eMqQgG3C1o1tDFyHs2lEIus1nunpKBMDwWk7ya-7Z_7aCqVOltNFVSAGpouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oDfTYi2pLmlp7i1VgWRBpAOA0Ja7kECdNLhYcRpjKCfqiAAn5zSDvN5nEZU2UzvcN-JbKPRQ9dg9mhIq0y8EapS7aHGQDeqC40z5r9AiHPML1w9nssi-Y2RC6JlAuRaPTzltCJJ1z6cyQkxZvnySjHZkJIWFYlEZgzIpLj6pGDnQwjjV8obCdozgq3CIuNHbbicsXNp-v7H4aG-4piyS7d6yl7H-fAl6Wrs0blgFyFCR7gczmQtqyYkpOcH_k04PuKIGuXpU3_UjYvzSyoJ8UWfR58QBqULtCqsrsqVk73AVXWuhXhjefNwbi0QsRVVpJFSEzUp_J9-70ioNU5Ub-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=Wae3xff44HKDN0tlEz39xnydz7f4FaTdUfru42hTbTR9DQgTy6p5xN8gHTel3VYjq-UXni-fpgRWZFdEeC0WEcqL95jnH92Xg15wJFa_UXdp1SemON-KkAO6Opx__f5o0YZmsp9NcLzGzSsN8XZ-E2VhTB0OmBORoLKmnSJDVSDUueCduwm8hJl6_LqNsLCiJYYU3V_npL4jbvJwqsD0DIxAlbuXlHMSAhDHqNgpGs94lQ_ca6DlplNrsd1UeEV6oRj2tDow0lvI5T-w1IqgWrSCJRnB3ddy-etwO0HmZsLHTdp4kQcFDTapvwUl-QrOuEDk0mFkpjTw_bKFAe1jMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=Wae3xff44HKDN0tlEz39xnydz7f4FaTdUfru42hTbTR9DQgTy6p5xN8gHTel3VYjq-UXni-fpgRWZFdEeC0WEcqL95jnH92Xg15wJFa_UXdp1SemON-KkAO6Opx__f5o0YZmsp9NcLzGzSsN8XZ-E2VhTB0OmBORoLKmnSJDVSDUueCduwm8hJl6_LqNsLCiJYYU3V_npL4jbvJwqsD0DIxAlbuXlHMSAhDHqNgpGs94lQ_ca6DlplNrsd1UeEV6oRj2tDow0lvI5T-w1IqgWrSCJRnB3ddy-etwO0HmZsLHTdp4kQcFDTapvwUl-QrOuEDk0mFkpjTw_bKFAe1jMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ایرج مصداقی از نزدیکان شاهزاده رضا پهلوی در یک مصاحبه درباره علی کریمی صحبت کرد؛
صفحه اینستاگرام کریمی در اختیار شخصی به نام امید دانا است.
بعد از انتشار این صحبت‌ها، کریمی در چند استوری به‌شدت واکنش نشان داد، از مصداقی خواست ادعایش را ثابت کند و شاهزاده رضا پهلوی رو مخاطب قرار داد و برای اظهارنظر درباره این موضوع ۲۴ ساعت مهلت تعیین کرد.
⏺
مجدد مصداقی در ویدئویی جداگانه به واکنش‌های کریمی پاسخ داد و اونو مخاطب قرار داد؛
علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره
حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی مثلا؟! داریوش که میبینی که بلایی سرش اومده تو انگشت کوچیکه اونم نیستی.
بهش گفتن جهان پهلوان باورش شده. اخه مردک کسی که دوتا لگد به توپ زده پهلوونه؟! همین مونده بود تو برای ما شاخ بشی. فکر میکنه چون فوتبالش خوب بوده سیاستم میفهمه. ما اصلا تو رو حساب نمیکنیم ابله.
اینا رو ارزش دادنی فکر میکنن خیلی بالا هستن آقای کریمی با تو یا بی تو فرقی نمیکنه زیاد حرف بزنی صداتو میبرن
⏺
علی کریمی هم در ادامه اومده گفته؛
از اين لحظه به بعد؛
از هيچ شخص يا حزب سياسى حمايت نميكنم.
در حد توانم به مبارزه‌ام عليه رژيم اشغالگر شيعه ادامه خواهم داد.
این تصمیم من به منزله سنگ اندازی در راه مبارزه دیگر افراد با رژیم اشغالگر آخوندی نیست.
به اميد آزادى ايران و مردم نازنينش
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70659" target="_blank">📅 13:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70658">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBO4pqY7MrslwATT-AKQtv0Qw0-96JcyMD57YtyGkDTn-9fXTzN_5HhLrUlqmyOxToZylFzHM_rimUXL4_mJVwC_OTFr7dZqXcMzdHLgfIWd3IlgdS_mdl2SZs4qY5lT5DicKKt-7tbpFwk6XPCXL2f51qFMjnQ9uN017T__r5ZvpNY8Ns7bA_Zz3W66vinnPo2h-_9U58jSnYS0Tjq9tCWfEeAy5gy-22URkGaR9CK0fPmZdnLTuznRsDRO-5Jqt1bt8IXPQGRn_5hsanUBTX5-oeooD5khzLZpI3VZ7p1LZone8tji4fJb0yW8bDsvDvCecO54K9MoYPqjmvgMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
📰
وال استریت ژورنال:جان رتکلیف، رئیس سیا، این هفته در سفری غیرمنتظره به مسکو رفت تا به روسیه هشدار دهد که به کشورهای عضو ناتو حمله نکند.
این سفر در پی ارزیابی‌های اطلاعاتی جدید آمریکا انجام شد؛ ارزیابی‌هایی که حاکی از آن است که پوتین ممکن است در سال‌های پیش‌رو، با انجام حمله‌ای محدود به یکی از کشورهای متحد، عزم و اراده ناتو را محک بزند.
مقامات آمریکایی نگران سناریوهای مختلفی هستند؛ از حملات سایبری گرفته تا تهاجم زمینی در مقیاس کوچک که به احتمال زیاد یکی از کشورهای حوزه بالتیک را هدف قرار خواهد داد.
آن‌ها همچنین نگران آن هستند که کاهش ذخایر تسلیحاتی غرب — که ناشی از سال‌ها حمایت از اوکراین و درگیری‌های اخیر مرتبط با ایران است — بتواند بر محاسبات مسکو تأثیر بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70658" target="_blank">📅 13:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70657">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=H5LrW1n09Z6zjyqjc7pmNd_6Z0kgdTNY6sZrA9RTGtYQH3nKsXEE6KwTTqHJ_nYT_F4w65TduJA0vKT-2tasS-0w4xk5S09tqNsJLXJy1MJzuCo7-luutdCxQCH84bwrJTepnkHyf3G5B3H99NbkI2TVhnfllCBAQBoyXcMICOLlISFIb0xsV3gXVJ4p3wwW60RBKDiB701fCV09R6tePDodY-YMVgEcnLT3suu5D61iSpI3bLSOVReZ9h_mcTMvcOuBaoHYeGnY979u75f_irIWDCynI7l8CQdtpXkyXKRJdmrJDp3PXREmnI4hi1now0psVqOJGL0O7QlXVXKiHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=H5LrW1n09Z6zjyqjc7pmNd_6Z0kgdTNY6sZrA9RTGtYQH3nKsXEE6KwTTqHJ_nYT_F4w65TduJA0vKT-2tasS-0w4xk5S09tqNsJLXJy1MJzuCo7-luutdCxQCH84bwrJTepnkHyf3G5B3H99NbkI2TVhnfllCBAQBoyXcMICOLlISFIb0xsV3gXVJ4p3wwW60RBKDiB701fCV09R6tePDodY-YMVgEcnLT3suu5D61iSpI3bLSOVReZ9h_mcTMvcOuBaoHYeGnY979u75f_irIWDCynI7l8CQdtpXkyXKRJdmrJDp3PXREmnI4hi1now0psVqOJGL0O7QlXVXKiHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از خونواده‌ها میپرسن چقدر خرج کنکور کردین برای بچه‌تون؟ رقما به شدت عجیب غریبه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70657" target="_blank">📅 12:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70656">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGJLVZU56wItGdEH84FNfdQu0N-ZNCPEJy2D6I1xK5_h99McGpDYstaA9FY6IfmoHJatuz4HdPBABWk_SK8-gfrZPQ-l2fhE6zoFK19MgP15CSJtSQMmog_9peSJoson5DkCK1b2yeiGirx-vdE76LLgR575KdXxjH2mGku9MZMWzTSwUYZckg4TEriPRMYSoSBA7hZZSO4PIeiRMq8YNmUt2aTcow2faW2Zxm9yodwlYd5Rb5mqJAOCU4ZvoUDWvBg94Y85aoy26NXL_yAWLS8UMxnjjei9tvJA6368ZPyqMMDOyosrjhwKR6vnV_iiNh1RoyelMFia9CWo3Nrlgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی دریافت کردیم مبنی بر اینکه یک نفتکش در تنگه هرمز هدف اصابت یک پرتابه قرار گرفته و در پی آن دچار آتش‌سوزی شده است.
آتش‌سوزی در نفتکش در تنگه هرمز مهار شده و تمامی اعضای خدمه در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70656" target="_blank">📅 11:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70655">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=k5ijrMWTTZH8NZ2JUTHVu9nnggfPtJ1hM8rDKavnp9VG9giS41-5TkeA8azhB2SYsco430n1Qzwr4MWEHY1PO89LqABxwY_XohfuZLsR35cQFkLDeh8ePIYb4TjozvOpGIiA6qOaCnF9Lb-1NhwDLJ8cj5ylqxAlZAH786mLZgJGVoF1yGJkPRb_Sj1xStDOsEL4P6eTK2GlWmCP1Yls-qu0vSvToviK7XIx_eRPrcf-d7EqEFwYEYCTiKqyEv8aWcIPSC3NDj577Dl5D7f4MJxonblk_ugZpYRQj5BJyBSDHQutJ3qD1e8dG5zxZzKwdv6lE-4DnrW39r1zJMRiQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=k5ijrMWTTZH8NZ2JUTHVu9nnggfPtJ1hM8rDKavnp9VG9giS41-5TkeA8azhB2SYsco430n1Qzwr4MWEHY1PO89LqABxwY_XohfuZLsR35cQFkLDeh8ePIYb4TjozvOpGIiA6qOaCnF9Lb-1NhwDLJ8cj5ylqxAlZAH786mLZgJGVoF1yGJkPRb_Sj1xStDOsEL4P6eTK2GlWmCP1Yls-qu0vSvToviK7XIx_eRPrcf-d7EqEFwYEYCTiKqyEv8aWcIPSC3NDj577Dl5D7f4MJxonblk_ugZpYRQj5BJyBSDHQutJ3qD1e8dG5zxZzKwdv6lE-4DnrW39r1zJMRiQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇴🇲
🇺🇸
کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، درباره دلیل و نتیجه نهایی مذاکرات عمانی-ایرانی:
ما گفت‌وگوها را با عمانی‌ها آغاز کردیم تا بتوانیم به آن‌ها بگوییم که حداقل در روحیه همسایگی، این اقدام برای باز کردن مسیر جنوبی می‌تواند یک‌بار دیگر تنش‌ها را ایجاد کند، فرآیند اجرای توافقنامه‌های اسلام‌آباد را مختل کند و حتی منجر به شعله‌ور شدن درگیری‌های نظامی در منطقه شود.
​
انتظار ما این بود که با کمک دوستان عمانی‌مان، شاید بتوانیم این مسیر را ببندیم. با این حال، فشار آمریکایی آنقدر شدید بود که متأسفانه این مسیر جنوبی بسته نشد.
​
سپس آنچه رخ داد را دیدیم: جمهوری اسلامی ایران تصمیم به بستن تنگه هرمز گرفت و در ادامه، شاهد درگیری‌های نظامی بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70655" target="_blank">📅 11:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70654">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=kGPzE-3lhbL8QIVAEMxo8Uujt8Jrj10ZDvk4PrIdmGA7X7TcAIoydC0Ka54B40BzFboStj2R1a-DdPvrhOMe5LCCVHG8F6czHEkpRARrnCjL1Y5TF-5lGr_sUjIdoqtYu8kiqt0tecdP152z7am62Hv1uCcOv9zwW76BZIOFN8FQVkOYXt2dHxs0kP-k6msz8GXeZhTu0fg0dag80eBV-5-cZwZKX75_nT9LOJwhVeoIcTqMlWRmf0sI2Jr4WSOFXcRkfXMit5Y8IxdjpOK9DI6YdFFicq86b9YaQJyidYSuBEin3wmV2HnMafbQhCKWIYVxpTZstEny84Rt-r5WCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=kGPzE-3lhbL8QIVAEMxo8Uujt8Jrj10ZDvk4PrIdmGA7X7TcAIoydC0Ka54B40BzFboStj2R1a-DdPvrhOMe5LCCVHG8F6czHEkpRARrnCjL1Y5TF-5lGr_sUjIdoqtYu8kiqt0tecdP152z7am62Hv1uCcOv9zwW76BZIOFN8FQVkOYXt2dHxs0kP-k6msz8GXeZhTu0fg0dag80eBV-5-cZwZKX75_nT9LOJwhVeoIcTqMlWRmf0sI2Jr4WSOFXcRkfXMit5Y8IxdjpOK9DI6YdFFicq86b9YaQJyidYSuBEin3wmV2HnMafbQhCKWIYVxpTZstEny84Rt-r5WCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعارهای عجیب حامیان حکومت در تجمعات شبانه:
دلار شده 200 تومن همتی
یه کاری کن میگن تو بیغیرتی
حیف که نمیشه بکنیم به تو بی احترامی
ریاست محترم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70654" target="_blank">📅 11:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70653">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45450621ea.mp4?token=q5NF51Ev2NShYlDkmfztJ7x7rRSdOE0rx5sIkQ4vvocfIkqEFg4pjr4mNHhs1-1g9kBrIWRS4MxEEtk1N7l7OQ-jelN5OGJn0dXF8RPz4l8GBvf_sg_lbUJR1uJSEPrGL8qXdSKrjRmFKaT4yU7vSP-GKD5opVD3oLshwdcTzqoqn7cgEbgPIBNDnJkm8D-nT_cfjeDYHUsrraPAUNOQS5QplhYsuxLhOT89YBBpMc11bkiJHzy4e0Q2qETb2kuMYyjS_nY0P6F-klxJEgPO35LloaBUHNDUuRJFY6YBiJ6oVt3vl25gCnCWfkw-P6v7rAh2tUP3J63pdaAl5Eg9FjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45450621ea.mp4?token=q5NF51Ev2NShYlDkmfztJ7x7rRSdOE0rx5sIkQ4vvocfIkqEFg4pjr4mNHhs1-1g9kBrIWRS4MxEEtk1N7l7OQ-jelN5OGJn0dXF8RPz4l8GBvf_sg_lbUJR1uJSEPrGL8qXdSKrjRmFKaT4yU7vSP-GKD5opVD3oLshwdcTzqoqn7cgEbgPIBNDnJkm8D-nT_cfjeDYHUsrraPAUNOQS5QplhYsuxLhOT89YBBpMc11bkiJHzy4e0Q2qETb2kuMYyjS_nY0P6F-klxJEgPO35LloaBUHNDUuRJFY6YBiJ6oVt3vl25gCnCWfkw-P6v7rAh2tUP3J63pdaAl5Eg9FjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
سخنان جالب امیرعباس هویدا و آمار ارائه شده توسط وی درباره وضعیت ایران در آن زمان .
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70653" target="_blank">📅 10:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70652">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
اعترافات اندرو تیت (بوگاتیت چه رنگیه) و داداشش تریسان تیت :
اون زندگی فوق‌لاکچری که از ما تو فضای مجازی می‌دیدید، قرار نبوده واقعیت کامل زندگی‌مون باشه؛
ما داشتیم یه نقش بازی می‌کردیم، مدل کارمون اینه که هرچی محتوامون عجیب‌تر و اغراق‌آمیزتر باشه، بازدید و لایک بیشتری می‌گیره و در نهایت پول بیشتری درمیاریم.
اون بوگاتی‌ها و استون‌مارتین‌های چند میلیون دلاری که تو ویدیوها می‌دیدید اجاره‌ای بودن و اون سوپرقایق تفریحی 50 میلیون دلاری هم مال ما نبود؛ برای تبلیغش پول گرفته بودیم.
حتی خیلی از حرف‌هایی که درباره ثروت عجیب‌وغریب یا داشتن چندین پاسپورت می‌زدیم، بخشی از همون شو و شخصیت اینترنتی‌مون بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70652" target="_blank">📅 10:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70651">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=sbNgOMuIJ0BmmR26EzmhOai8JSxmrP5xxFLnb1Xp4-_xl_AHagLgRJlF248j1Ru_AfpmSWrHg36HucZ7ZwtnzSyaz5gSERgnoK4lYJR0jhiPU2dClro271lYJwzHwgfyCBDW_dls20C_qQz28_KRDE-mAs4JPzQK1IaUhvlMpQedf-5rpHC_wyVJQ6dwBpJF9FSvuXTCppE0ef1-VeROQro5MrGI2C1Qwjl6n5zNZryW7p-5ywcevnM00Y2d7S2QiV7zFyZ1awWiGDH97_oeFenTI8N3oVZvTbEwlSIqby1o6pPnpuf7M-bd4D1kcIVv0mAn7fEAw7AEO94BU-4xFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=sbNgOMuIJ0BmmR26EzmhOai8JSxmrP5xxFLnb1Xp4-_xl_AHagLgRJlF248j1Ru_AfpmSWrHg36HucZ7ZwtnzSyaz5gSERgnoK4lYJR0jhiPU2dClro271lYJwzHwgfyCBDW_dls20C_qQz28_KRDE-mAs4JPzQK1IaUhvlMpQedf-5rpHC_wyVJQ6dwBpJF9FSvuXTCppE0ef1-VeROQro5MrGI2C1Qwjl6n5zNZryW7p-5ywcevnM00Y2d7S2QiV7zFyZ1awWiGDH97_oeFenTI8N3oVZvTbEwlSIqby1o6pPnpuf7M-bd4D1kcIVv0mAn7fEAw7AEO94BU-4xFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکنا گزارش داده یک فرد که بلاگر اینستاگرام هم بوده، عاشق ماشین‌های مدل بالا بوده و توی دیوار دنبال آگهی ماشین‌های گرون می‌گشته.
با صاحب ماشین قرار می‌ذاشته، می‌گفته یه دور تستش کنم و بعد با ماشین می‌رفته!
نکته عجیب ماجرا اینه که بعدش زنگ می‌زده و می‌گفته من دزد نیستم؛ چند روز با ماشینت دور دور می‌کنم و بعد سالم پسش میارم!
ظاهراً هدفش فقط لذت بردن از ماشین‌های مدل بالا بوده و بعد از چند روز هم ماشین رو سالم برمی‌گردونده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70651" target="_blank">📅 09:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70650">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=uSa2VTHFELsf_6O7L80lCiIATX-odxyP3ICIfeuks-K56siuYlO-uE4OLIwUNyulK37i4BXpgJnIRXmWrcPFIdL0pHSjfm2Ik0oyyBRNJ66pYh53A6DID9qRWYkcdxMLuAWXCeyDEtsBxODdpL3V2Lsq6UQeLyVrYN7IDp7IZUvtjFEGdfK5-3qyPwqJcgHVpurule4g49xf5wEXg8F51Y1G6l9eTThAGMTMt2RAHoZxn0oYJ4hbBlx1WGmzTmT3Gu9r6-Ly8pkpWSka1l9p_Vu6TJ_mSPlhcnaxj0CL6aMVz1lR0Jy8kw62e61zePQGAK7LADEEwzKR3cPBpy7JIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=uSa2VTHFELsf_6O7L80lCiIATX-odxyP3ICIfeuks-K56siuYlO-uE4OLIwUNyulK37i4BXpgJnIRXmWrcPFIdL0pHSjfm2Ik0oyyBRNJ66pYh53A6DID9qRWYkcdxMLuAWXCeyDEtsBxODdpL3V2Lsq6UQeLyVrYN7IDp7IZUvtjFEGdfK5-3qyPwqJcgHVpurule4g49xf5wEXg8F51Y1G6l9eTThAGMTMt2RAHoZxn0oYJ4hbBlx1WGmzTmT3Gu9r6-Ly8pkpWSka1l9p_Vu6TJ_mSPlhcnaxj0CL6aMVz1lR0Jy8kw62e61zePQGAK7LADEEwzKR3cPBpy7JIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
یکی از زیباترین سخنرانی‌های محمدرضا شاه:
هیچوقت به زندگی فعلی خود قانع نباشیم و دنبال بهتر کردنش باشیم.
برای بهتر کردن شرایط زندگی، اولین شرط خونه و سقف بالاسر هست و بعدش قدرت خرید مردم.
محیطی که در آن زندگی میکنید باید شاد باشه، غذایی که میخورید لذیذ باشه و لباسی که می‌پوشید تمیز و لطیف باشه‌.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70650" target="_blank">📅 09:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70649">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70649" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70648">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=fk79cZd8TzovwyI-xw-qWFbSctB0Lv3r1ThKU_mBWNfYZLyxJMhNbUe1UeyOGn-EMeDUHGwjKZKuNRYNivM1neIskC1a-Y2-TyJo-PweaBgmvErtr0cN_Abv6f4xX-rfUFPARbKTXfAhbTxSdwh8FUvSfGfaWC9wNzcLH8ueZPnXwDGgNOxiggqeAYmw7SN0qXGevuwq2WsEX_ovWX4QeCgO4JMY9aC_FKeXmtWkW4DFxAMjyQm9LWqY224EzZxqe0RtTM_R4ABv-h49fd6tITIPmRjB_TNxUB-snzdKKQLI3upcdz2Z40N-EUBDELwUBv3YZz8Eq9zH87HucQNoHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=fk79cZd8TzovwyI-xw-qWFbSctB0Lv3r1ThKU_mBWNfYZLyxJMhNbUe1UeyOGn-EMeDUHGwjKZKuNRYNivM1neIskC1a-Y2-TyJo-PweaBgmvErtr0cN_Abv6f4xX-rfUFPARbKTXfAhbTxSdwh8FUvSfGfaWC9wNzcLH8ueZPnXwDGgNOxiggqeAYmw7SN0qXGevuwq2WsEX_ovWX4QeCgO4JMY9aC_FKeXmtWkW4DFxAMjyQm9LWqY224EzZxqe0RtTM_R4ABv-h49fd6tITIPmRjB_TNxUB-snzdKKQLI3upcdz2Z40N-EUBDELwUBv3YZz8Eq9zH87HucQNoHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a4
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70648" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff574e553.mp4?token=AyCzA3KpYIKohwdq9mdFbDedeCLPomNo2wGuAYI0hfeVJ9Sl-IbMseMQj8KpwBKS-BdkyPovVinZd--0_6mYvXQY94taYtmYIEaqOxBZ1qkVEK-Owcih9tFYTmH3lw_pYA_WnS3Lqrm8XEzbVgaNoW7-LMilBJu4QG6onCSBtkP8XIsRGtkCdie3790eJuT4kiddcC-FTNKOMcVqGsyAmfIxZhkwFR_JRkkT51O6Jsj7CqnDzdEoSFUcUAywVVZagUrasXRzpDCPEai_r8sfoN9JRcvt57H2_llXOCB-7l1FRnn2eYn99NzblUUk3GI_7T0wxWFns4y_p9h0bq3mLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff574e553.mp4?token=AyCzA3KpYIKohwdq9mdFbDedeCLPomNo2wGuAYI0hfeVJ9Sl-IbMseMQj8KpwBKS-BdkyPovVinZd--0_6mYvXQY94taYtmYIEaqOxBZ1qkVEK-Owcih9tFYTmH3lw_pYA_WnS3Lqrm8XEzbVgaNoW7-LMilBJu4QG6onCSBtkP8XIsRGtkCdie3790eJuT4kiddcC-FTNKOMcVqGsyAmfIxZhkwFR_JRkkT51O6Jsj7CqnDzdEoSFUcUAywVVZagUrasXRzpDCPEai_r8sfoN9JRcvt57H2_llXOCB-7l1FRnn2eYn99NzblUUk3GI_7T0wxWFns4y_p9h0bq3mLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهروندان اسپانیایی ساکن منطقه "سئوتا" به ساحل "ترامپولین" حمله کردند تا مهاجران را بیرون کنند و اقامتگاه‌های موقت آن‌ها را تخریب کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70645" target="_blank">📅 01:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcuYGFSCkD9_DbnRjPKfkUwidzwdafzng18rDxa3jvvIwbKnM4CYWUZqE7r_BMm-YY-1T3YcHnHA_Sqln5kCdb197HlmFIS8JoJiC4fqChY3tHRJscCw-N720k99WCQlDA47MsHx2ILDU_hX0YuAPzolr42_6XA-l1QXoxzE01O-9a4KQw-QB8UIX0w975ITCe0o9QDsDa7riNKp_wyED0dhOuyd9PPVTi51X8oUprnuOWPdtZurdCZGuFGMzemTYpIZlnoIqjx0mnZjRu_VrLdXjpgX2p3UWWdxs66-dagQMP24OIqxZkCii1j2eZOJSKVCRt_9JDi0IKroVk0igA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا ناو «یو‌اس‌اس آبراهام لینکلن» را برای نمایش قدرت به منطقه اعزام کرد.
پس از ماه‌ها جنگ — و بیش از ۲۰۰ روز بدون حتی یک بار پهلو گرفتن در بندر — این ناو اکنون برای استراحت و تجدید قوای خدمه، راهی تایلند است.
مأموریت: نمایش قدرت.
مأموریت فعلی: نمایش تعطیلات.
«خسته‌ام، رئیس.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70644" target="_blank">📅 01:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3143921715.mp4?token=prXK97uCOB4EqR7ZQiD96JvHtycTrSkkFsLsOtbxeYFbiniHm8riviL5F0NeFvO2RUfqQLRL3eIFFUYLtsePFKYL6XmutqxdN0fN9QY6E3N7RzUOtuTppTqOHPNb_3JYB34gTphjHR7ldrTWDLqYOIy6PzQvFUzj-qf5XUktK_Tku_mCezafmhUpGm9Jt0eyaJOYYBcc-tf4HSIlhNCeTolyz3-2C3e_LP02nV5VvbTKzTBxYuiJ935LyEsgYbyMBU6BkKGpivI5lI_ZsTZf711f2vQgkRXTBS9r_cRaoez7SADgNrbiBRipWg6kREzU-CUs2Y1kpWRdI-fxboon1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3143921715.mp4?token=prXK97uCOB4EqR7ZQiD96JvHtycTrSkkFsLsOtbxeYFbiniHm8riviL5F0NeFvO2RUfqQLRL3eIFFUYLtsePFKYL6XmutqxdN0fN9QY6E3N7RzUOtuTppTqOHPNb_3JYB34gTphjHR7ldrTWDLqYOIy6PzQvFUzj-qf5XUktK_Tku_mCezafmhUpGm9Jt0eyaJOYYBcc-tf4HSIlhNCeTolyz3-2C3e_LP02nV5VvbTKzTBxYuiJ935LyEsgYbyMBU6BkKGpivI5lI_ZsTZf711f2vQgkRXTBS9r_cRaoez7SADgNrbiBRipWg6kREzU-CUs2Y1kpWRdI-fxboon1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شکار شکارچی
اپراتور پهپادی روسیه توسط یک پهپاد FPV اوکراینی کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70643" target="_blank">📅 00:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70640">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpsE5O3Djhrg9ml6zwRTmDOfhxzHQG3rsk7GzpDVU5j3koHXu27XGWiT_PrheT2CnYHsQ2lmxlVMrM5AQ9-MIQyCE8Ox-atyNRJKaSdByTKRoPNzIJyu8YFxKaQuJ9gKJse4gchVraQCFW9EHaNUgfXvOJh19e4eKszlTJd4H5J8LZumy52Fi9Z0PBeDPO7LE2Jz7NzL6zqQno_nRGmiou1eJtTmwdT5kgO8CPsYUZ0RhX8HGSjr5Nv8Kls7IMAUejRnRE9UjJDKqISRt9o554ZeNJd9IDgXABJqi7uoTHoGkcDXl_UbrdHpvmMxw73Cb_GUBptM9IM88WekSOHgSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=XLGfKJ0UDm2ItpAdIYdee3w75hg-UXQRWWkO83BQZxchcUxmAnteB0EO-t9sXTETmIElLREA5Io3-gKlc1DPZ6RF2AH0ONuACTBoa-YET1Ej82Pzwo1nAwKTicaXzU94XNsKBLeGKxtZW8Rc-AsQ-TvMJGruOCSd1jVHrVNZX5J9gUxDVzMbP4zBqYfNo_DMtoxi0FUIs7oLViPvdyABOBalw0MipJGkRvdL3If6-Nvd7c7N4ObzKp3zo-BFPIwYscaa-s5DnhaTHGqf4g0mfbh1gfI6HTCR_5bVO-vgN60u-Rdyc_GBqkoE1DHhJWhGm9xM3uZkrPl7sANS40Mcxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=XLGfKJ0UDm2ItpAdIYdee3w75hg-UXQRWWkO83BQZxchcUxmAnteB0EO-t9sXTETmIElLREA5Io3-gKlc1DPZ6RF2AH0ONuACTBoa-YET1Ej82Pzwo1nAwKTicaXzU94XNsKBLeGKxtZW8Rc-AsQ-TvMJGruOCSd1jVHrVNZX5J9gUxDVzMbP4zBqYfNo_DMtoxi0FUIs7oLViPvdyABOBalw0MipJGkRvdL3If6-Nvd7c7N4ObzKp3zo-BFPIwYscaa-s5DnhaTHGqf4g0mfbh1gfI6HTCR_5bVO-vgN60u-Rdyc_GBqkoE1DHhJWhGm9xM3uZkrPl7sANS40Mcxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇳🇵
ویدیو هایی از سیل آخرالزمانی و وحشتناک امروز نپال که باعث شد صدها نفر کشته و ناپدید بشن!
ویدیوها عمق فاجعه رو به خوبی نشون میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70640" target="_blank">📅 23:55 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
