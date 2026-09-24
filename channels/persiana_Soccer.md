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
<img src="https://cdn4.telesco.pe/file/FZiO55tkzNDD_2W2N9PRMP4a3ovaw9p9oXugPRwvLkw2HgwNS0VJOr9Tp3P87fRStl7HSn8cYGm4XKwwfs4NvqVriHMJjNWC881AAfyiAgh_nXgRP0Fs0McOLW-P-vi8iVf5zEQ5xmTRwbZT9SCr6yjmYpygGO8K7-EzEIyE_KV0eT22N7xwlgFhn6Pj1UEmCO7_WCt1_QJem9NxKxJ049a0F9me4x6x8V5YmW66BM8sC8zNOttEDhZsBcCVjVtS1mHFSPACJgaeL3vs9BZ6fcq1O7mtBVV48SsGtLOzyvvgSMSh8y6YL75En27R89UHjH2yBMIFxu9JDyKqOnO-kQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 453K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 04:08:43</div>
<hr>

<div class="tg-post" id="msg-30327">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ky8pdZlFdpikM5YYFFJAwV1L1soiCfFc1pcCsB0Nl-Gi9eEvVOfR5ZkLaNo8UX2aIF7k1rdXnHJA14zyCbIZQNSnKMhjtmKJsXwvsmFlXRbxiFVHoBTosqHmI2WT53IJJbVCPrdxR6IyYeN1J227VdmSpJAh7OtBQYw9B5ZD6aiQ3P0hoEaxbSCzNlUFzR8YzL3n63lZ4TE4bWxf1ddrkft7NDLMDz7LCD5TWS256F_qR5qqSQwcVSgWfu0npTshTKob4bnWp1hjsx0LR3u2Sp5lysqaOUiZKqbwJ8BJFJ85CD_z9rDVRpg1kI7USg6J-7DQ9c2KDfBsAt4AjIIRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/30327" target="_blank">📅 01:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30325">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPIjtwh7uEHvnAtencPEl-eoV5nYoKoimUZhD-CCdkyp_EX-VDVjAop1IJFOFshQ2ruE3K-FvQaDfZ2F4BygEhp9BW3hKRZhDuMwDrp_YwAyDyvGS1sTqRaQdWe3DRzyJe6Pa-dq7zVFEb5-p_qJWRFqkkmwnfwBzgfGJGT4dbpiWuOhhjyR3iDWLqX8c3374jfaG47_RRgR6aQZJ921OSBjEvK_dbzX0X7bnlPDdJUU6BCwWops8AAhBR8zOCZ6HBnGiSs0lWyMdwj8OljZF_QlwrTBsBDXFSb4obCV_PlG1xUYMluG2e0ofZ_5G8SbqrZtzqta0PuXf35zktjUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JV35uMZa3OBfdZHfkAhRMuwyNDUPGJmbgCziJUfJznQIbvpxpEwpBI06aRL4JpD_KRR0nnJA_JlueXqgY0RWe26mME5gxlKTXIir9H6uZi0JjSkBClifixUzUBr7ILiBashO75a91fW1X1_IjbmnZftqgvBY9HgMWtI6ielDoheY5GhvHi8bm7eQZ6rVs2SpCdnvsVSRIFMcE5jsgXgl6JG9zEIWkgCB2C-zCPXPDE6xydgTAwlhocw1sHpSZskqRPAoHTWhABLEbtNqDo8kYycOkDMhRJgBZSoZ4Jt03qcdQ1kkCx8oNjrtvxpeb4tQJlZgPSaiVQscqPLeOHucnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آخرین رنکینگ بندی تیم‌ های ملی پیش از شروع مسابقات‌فیفادی؛ اسپانیا بر دنیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/30325" target="_blank">📅 01:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30324">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=TgZZFMLNBdt3Ed5Ptj-GmwXRjSMQ_COhYhndRxoU4wkpEkZDo_08wejYK-5a0vJO17SJSKNcEjXRVUYy_ES1F5BC1AjCrOVKTmsLj0qw2Jfk3KflD7sa2h5uGO8YHD1C2zYQqIHJD5vQdMkRRc5Lrs3lAwYLhm7z3nnDpOU8ba119iiikqR7wyXv3BpvhCSHsMx76smfnu5I1lnfz2HcRTgUuJHxFH2hoz5E_z2zRf11EVpdmM6VEhBZIOojAngS8uNayWsDfTGntkuPBqJn96KAbOJfJYmK6G-YNWtZwwlQuNfVP3dH1n6gKmqy709AR3AG7zh-6ToZGncEkX-spg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=TgZZFMLNBdt3Ed5Ptj-GmwXRjSMQ_COhYhndRxoU4wkpEkZDo_08wejYK-5a0vJO17SJSKNcEjXRVUYy_ES1F5BC1AjCrOVKTmsLj0qw2Jfk3KflD7sa2h5uGO8YHD1C2zYQqIHJD5vQdMkRRc5Lrs3lAwYLhm7z3nnDpOU8ba119iiikqR7wyXv3BpvhCSHsMx76smfnu5I1lnfz2HcRTgUuJHxFH2hoz5E_z2zRf11EVpdmM6VEhBZIOojAngS8uNayWsDfTGntkuPBqJn96KAbOJfJYmK6G-YNWtZwwlQuNfVP3dH1n6gKmqy709AR3AG7zh-6ToZGncEkX-spg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل فردوسی درباره زندگی سخت یان دیومانده ستاره 19 ساله رئال مادرید در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/30324" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30323">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=a2IPuXUHjYFTgs7KLUWiiwo4NbDpqXfH_WXVD_PAKgejupotX_D3uGnpbFP-a_WTzccUashlh15gB5QqW3IBjwvIenqesJlqVJxrzz5-YyIAG1wQLGwCJiRm7bXdS_Ot9Wb38mmajcYajT1unXeKx4wxZbN8yCaF2qHzm2BmjlP5wu9pFsdstQ50ttn0AvFb9gBJBikWYHs5RbZhBx8K8wAp0nNj3eSXiknkPZhkReo9RhNb8_dWDCm1gVeEIfZ7lGHynftgbgtxUgCd8m_ACd4-AszG88f3ZavMrnFV82jXK0WCwTp-arCRdJ_Wb6vrZU_mfmfwN8478iuKz2Vw0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=a2IPuXUHjYFTgs7KLUWiiwo4NbDpqXfH_WXVD_PAKgejupotX_D3uGnpbFP-a_WTzccUashlh15gB5QqW3IBjwvIenqesJlqVJxrzz5-YyIAG1wQLGwCJiRm7bXdS_Ot9Wb38mmajcYajT1unXeKx4wxZbN8yCaF2qHzm2BmjlP5wu9pFsdstQ50ttn0AvFb9gBJBikWYHs5RbZhBx8K8wAp0nNj3eSXiknkPZhkReo9RhNb8_dWDCm1gVeEIfZ7lGHynftgbgtxUgCd8m_ACd4-AszG88f3ZavMrnFV82jXK0WCwTp-arCRdJ_Wb6vrZU_mfmfwN8478iuKz2Vw0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چالش‌عجیب‌وغریب‌امیرحسین‌قیاسی در قسمت دوم برنامه جدیدش با خوردن آبلیمو با غلظت بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/30323" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30322">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdAAW6tMrQyyVtLabx6hReMraiunaHp6eeqZtqQynr7R2BHW_4Ce2j-A971oiRqHw9jfDZkHA7aB4Qv9sCMBxER66_Zm3biaru6QqNi4iKwiFHFX3T6_K5DBcBWyzeQUdjM8wKZz05HF9jHs39TpUumhPRBvK3tg2vd4Qa_1a8Y8K0Mlh_Z32lxO0iwO2SS1PYp50XJ_PB7a9Pbhg4XisFYeZhY613u7a7Dr9UAJ32JwOfznX6FBoiz0FwcL0_5HRaLCWngqHhlmap8KzV5kYaUDScejorkJPN9mC_t_4tKUf3juX38ZQZcyYTtQUI2WZSZFYuy3JF0wCYsdL4JXOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
بازی محبوب و پر سود
CHICKY
CHOICE
در یک‌بت
📣
سرگرمی و هیجان بازی بدون ریسک با کش بک
🤩
🤩
🤩
ویژه بازی  Chicky Choice در یکبت !!!!
✅
سرمایتو بیمه کن !!!!
🍬
از بازی لذت ببر و اگر بازی‌ها طبق پیش‌بینی پیش نرفت، 50٪ مبلغ
بازی‌های ناموفق رو به‌صورت بونوس پس بگیر!
🚀
با یک واریز (حداقل1.000.000 تومان )وارد جشن کش‌بک شو و هر روز  3.000.000 تومان بونوس دریافت کن.
💰
💰
💰
🎊
با کازینوی یک‌ بت‌ برنده‌ی بعدی ‌شما باشید!
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
p1
🔗
https://t.me/+xNPVsLewpb4wMWNi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/30322" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30321">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXbLZHmv2oNoLuDyiW2eqb8b_XRnHzvKvxWmS6QBpvfeN3ZpVC5EpzQYgxUj-Cfy8AKeyoDkE5bBHUo6_eyooyJovQaAa8bOCjrYnf9CuznChgsw7SYV8xqPB8eQbjUPK7e_1vV0J1lhlE6PagBmhx27yTlrhdmCmKjHfKDfEwlqvr-2QTXnQGnGz82RM7T0DdUkpU67dP9-0r3PAKkKNuxxwHoPsKfalbMn55Tmr9RBunv3BMzwmohig4i58p0pdqSwcbw7b24XNhN6rgI0dqWW6Plzv1zJeXSbTZuk1Z0rpkDpFqckHBTqZ3KWKWeYneNHuX2Oa3wPZT-3FUdKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/30321" target="_blank">📅 00:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30319">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY37bJT0LjFJWQEvaCJkMefm0IjdiFDbWpehMKdrtZ36DzP9s160-0vQ8rqXRAAJv132J3cWmYsY74UgtiArcRnG-IXflAKwabRRUc7XnqjOD0KOnjWEzMyCTnZsAIiTfgvlCwTKbJwn_fhoLmojImoq9RbFlcEJer-kink-eOo9qQiSkFcZ7UZ4MuOzb9dMNlMoYz1ZCkk2UQU3hlYaOAvfX8njzf8RC8-F7jPUJXseoKbwcO2m4ZJZWhjQp7Qs4N8qkCk0wutkk6UtPlq7PDlwwQrNLY4Efl6WcXd8XtchmxB6K_5a2Wvb1s_ZOYzdRwYaO6ED7n1llJw8NH96OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/30319" target="_blank">📅 00:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30318">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8eN1SJxjFQzHdy23r21Qf78KrUc2B7vHjATcaSiJ7mHkadZyWHXtvMLW6FAdS03UwcwKgyZ8_ciQYPhpT2etL5jCepPbKZvE_qpna2sZFX4v-PXDAJBKpwempjxVSMFjmJ-aXlR-8kpJfoj2eA5LYCu9W_ykrUOLMQSZaAAfAy4qBGRp6EKhgpiJmvNzwR3LkNn406JKGILgbzLWhgwXj7nNBl2pP30zFXK72kd3TdwtGjaqn4FhZabiGriEAj16U1sJSvBQON30nzaTfR-VdZ5Qft13osX-_bunSklVOFn4trV1KgKCweVi053PaGHAWoqDLe7FdcoYhzyQBKN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌‌‌‌‌‌تنهادیداردیروز؛
شکست‌مفتضحانه تیم امید مقابل کره و حذف درمرحله‌گروهی بازی‌های آسیایی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/30318" target="_blank">📅 00:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30317">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ft_A6mhv6Si2zWJEVkycnCucDrI4girTiK_aseUdHKKAhP0Y-qHH9mPJocdb-J4swtGVTfqwr0168DEyKYOQbEOixeEKi463bV899PljaVUUDMKIojjivJh-DRmInlmqsVb8XIIZ0ZR4KtKTJHsCu9mEUD-NI0l5QLqgms3uDxPFcrc6O3ZQaqzozSTh05_cSMd60467bWGzF0nH6klBL1AtPKbuVy5mX04npuXAAot6vKBYKuOCnPc6YjEKQHU0rRq9UJ_-OiKAf9-u4UmSJ980MnUbWsCrlmtA9QZPPHQYplT9N_Q57OMpEGqf3zrtOFoSaIxsux0VWRyP2Xj7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
گل تماشایی ابوالفضل کوهی در بازی امشب نساجی مقابل استقلال خوزستان روی حرکت انفرادی خود؛ کوهی درآستانه پیوستن به سپاهان قرار داشت اما در نهایت شاگرد مجتبی حسینی در نساجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/30317" target="_blank">📅 00:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30316">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=wAnzQ15Zsu3Gc67BrykscggyzT8TWfMR4NKhhurMr446WcW-yFQJZrHl2REJtDc-bGTDXOrR-Fh8WEAwmdSjugwGbihzWstqgO_QUtQCIhrwgxegKmJqHCjsSAFde6g6MvwE_lbD2XTKn8JzFktYaMJ0PymXJ573slDEC5TscXpHMJ6Wjbuf9NjAAxZ0TTKxG7TTeZ48lj5lOzmHBW8Reyor_9awe_OKIdNHjC7bbpmKoy26a2ZMjPmHmT6chKDKww6nHpM9ofPEDiboYSeb_Y40jCsQ5WXx4U_rv1WoYut3TRKA8f2hAxy3r_F68nEB8S4a1YtqVEmnsaBtre8fZY-W70ZovSOapHMRBY-d9awL9cN9PlCL_QIfazhiy8H7f3Dyy84Rn3koFGSbvoRnGzZZFV23IseL87TcLHLb4NRmRXjL5BhZ2F2qAxa4AnV3Kd3qeInU26WADxETb-Z5PIHWd2mIIQ_NhzjMCKo6xzKZIYoU8SejXU_eW72PBSY2qJ_4JsveQPe97U2LiZ2WX577JodMZ7Rj6CzvZQR6i3KR6vddIw_0_wx_vYECStEUn3VCntqFwuBMTYF7tUCmKobLpIeAyRjEPUzX5Z-0ZK0p9kFEq7izZ42BHdoyi_jI2MtiDaRDZQRAfNVpBRGFwT7TFX267M3hFTiy2P-5fd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=wAnzQ15Zsu3Gc67BrykscggyzT8TWfMR4NKhhurMr446WcW-yFQJZrHl2REJtDc-bGTDXOrR-Fh8WEAwmdSjugwGbihzWstqgO_QUtQCIhrwgxegKmJqHCjsSAFde6g6MvwE_lbD2XTKn8JzFktYaMJ0PymXJ573slDEC5TscXpHMJ6Wjbuf9NjAAxZ0TTKxG7TTeZ48lj5lOzmHBW8Reyor_9awe_OKIdNHjC7bbpmKoy26a2ZMjPmHmT6chKDKww6nHpM9ofPEDiboYSeb_Y40jCsQ5WXx4U_rv1WoYut3TRKA8f2hAxy3r_F68nEB8S4a1YtqVEmnsaBtre8fZY-W70ZovSOapHMRBY-d9awL9cN9PlCL_QIfazhiy8H7f3Dyy84Rn3koFGSbvoRnGzZZFV23IseL87TcLHLb4NRmRXjL5BhZ2F2qAxa4AnV3Kd3qeInU26WADxETb-Z5PIHWd2mIIQ_NhzjMCKo6xzKZIYoU8SejXU_eW72PBSY2qJ_4JsveQPe97U2LiZ2WX577JodMZ7Rj6CzvZQR6i3KR6vddIw_0_wx_vYECStEUn3VCntqFwuBMTYF7tUCmKobLpIeAyRjEPUzX5Z-0ZK0p9kFEq7izZ42BHdoyi_jI2MtiDaRDZQRAfNVpBRGFwT7TFX267M3hFTiy2P-5fd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برای اولین بار در 47 سال اخیر، یک ژیمناستیک‌ کار زن ایرانی درمسابقات‌آسیایی شرکت کرد. هنگامه هادیانی؛ ایشون درمسابقات رتبه خوب 13 ام گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/30316" target="_blank">📅 23:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30315">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LELPJ1MK5OWhwIS3LN1Ibun6O3_FldtFlV4ewicEFw428XdH8o6ysOGsFNgLwBVt6jh9IhhHjgxsjHG5JksBjnt_HmOjoFNkmgLw4pKCt4cJNVT-oq2znR_ETk9xnz4GAdDyUz8UDdGblNBXrRFIEPShItePV7ElaILnFm_KvR8MvuW7UvcB_ykgoDY7RRpRc9MjyBH9qxzgT6dTqgwOfksMeRXeVTYjjdLyApnL6mGM_P2FSgEvHZ_PWtWsN1-k0vcsihjT7v2ptoG8Dtz-YL3WyKCUnvQpIrAjegAP0T6eTzDoTRlTEPtzZ-KzSYChUZu9bEdJv6WgRYnT6NR9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
صحبت‌های کریس‌رونالدو کاپیتان پرتغالی النصر درباره زدن هزار گل زده در کل دوران فوتبالی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/30315" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30314">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtG6zOpBwRM6S3xylaqYAhyC2y8Afm55Ln_-r18g2GUAbaE5z6bcRhC9NDe2aF7CTPMAW4NzmMFkpSB7XDeQuTMqEiipgIlmvGVb7cSYDpEVbIClUoBMUE4nynlUDVrTAHJCli2Trk4A8bQ_yukeu6IQTpymC5C-C6wYvo94cbM8fSRu8LjDgdsW8gYQUa9QaK9QFbSCixSSmjlVkDt8qbvgjwKdIHCGZmQzsp9v6iaKUavhxtEhvf9VDaCk6QaKMZ6uG9DkZJSeZNUdGqy9qNTuCBTRTCqVXC_V28S7vtUUskQ7BlzxE_FsSYHXXhPPsg2-eKg8ML3Y-bG6qjc3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/30314" target="_blank">📅 23:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30312">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOD4Th9yYu5_KP311hfeFXtbvk9-VWge1IhTP99jgMz4aaR9IutLJmiEKGkreEfULm2IR_JK8BpM7FPzn_f8OYAiLLpFU3UTfH4ZSmHv0QNQa9GGalD7FeDXgeKbjVDv9jxUB0v8lffmMywqX7m9POuETH9IOe8liqkaqOHGW6iNpbolpj0aFlDDZHVfpvaemHOarMvPjNvnFQWLolpUW7wfm6PWkpo3dVotzyeC3ik6D-T1VVTxdhp_j5COUubySvzzmsTXpX84fnj1o0yoTziFusR9ciylDviUhgImb2c55c4PA7FUsl9b0cM0vZE8z_FBHzsARfjN5jgDU2oSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال: باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/30312" target="_blank">📅 22:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30311">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI3okQLUpKvBDEXx5ZFq2ws74Vv-T0Vfu2yDFK_i8ES1QhnR28dmArTebQlNVqxb5ZInlof8AUIshCebOSp79OkfhkzXNVtBNYzAgfuf7D8Ja5LHrtbXSWcouot2j8gzDW18ZCuWtcc895MScCJLqqPNMbHCkL52YEcejpatkgRWrAeqfwvv3YVNElO0M-1G2QBW8WSB6hVN7KiucXmm1cwtoQgxjVhXDRXeRDh70PUZRSUgdNH5ph1_914RYlbbyYRzluIPTn0ZQzxLsGHTmXpqN3dyESDAzC5KDG_hi7c_YYBeEYXN5a6DbmGJLfFdRDHxFXJ7hhPj3EavUI9CAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/30311" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30310">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=jv9k-Yvzud9pXEoLCoXhQZd8ywsBEcvwaRunwFC3eo_y7rpNx5e7WQHAuwlHYN53-tfsowm2mOzGGj9PPCSLZW-vuXDRb3hRXrXywcAfcp5hFlBzIe7o58FqYlcDG_fSCLoJLM4tC0hnWbYf6vSc6q9FIkuXrK5plEWZ8vqNQmsMPeCwTFCrv884O5xTsWTJ56XmVbVSmmWeayRFCQWe8yLjrmf4iPGWCD3TWY3sZTCtWNgnmG2fryp0LYbNwKXpZWQ7XwbBdnoty0DFqS9jjGhpG5NqakzsRHDfgcRJNPhd_euzYSoWX8YL9fDuDeNN4Lcg1L3LuuCscRlL4Nz9GjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=jv9k-Yvzud9pXEoLCoXhQZd8ywsBEcvwaRunwFC3eo_y7rpNx5e7WQHAuwlHYN53-tfsowm2mOzGGj9PPCSLZW-vuXDRb3hRXrXywcAfcp5hFlBzIe7o58FqYlcDG_fSCLoJLM4tC0hnWbYf6vSc6q9FIkuXrK5plEWZ8vqNQmsMPeCwTFCrv884O5xTsWTJ56XmVbVSmmWeayRFCQWe8yLjrmf4iPGWCD3TWY3sZTCtWNgnmG2fryp0LYbNwKXpZWQ7XwbBdnoty0DFqS9jjGhpG5NqakzsRHDfgcRJNPhd_euzYSoWX8YL9fDuDeNN4Lcg1L3LuuCscRlL4Nz9GjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های خسرو حیدری کاپیتان‌سابق تیم ملی و باشگاه استقلال درباره حضورش در سریال پژمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/30310" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30309">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔥
هر روز ۱۰ میلیون شرط می‌ندازم که یا میلیاردر شم یا ورشکسته :)))
زندگی عادی شده. می‌خوام بهش یه هیجانی بدم. توی این چالش همراه من باشین قراره روزهای هیجان‌انگیزی رو باهم دیگه طی کنیم.
🃏
اسم این چالش رو گذاشتیم قمارباز دیوانه:
@ghomarbaze_divane</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/30309" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30308">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETe4zAZsiuf8XA50eZ7n2UayqnpYFpOF06ljJ-pdGJunD-dfKJr8fyybwUyrQhSBitKBeRDvnaTP1q9vG3dG6UQKgnn2XxkwmwHZGVq5QCTlTBI5mwM_fYcfZXTrVYfdLdP3vGPC_4Isn96pwjz16PN0Oye-8ecaV6LZZ5PxWpR0XRtnK-Y9XnW7trGOXGWt3590b-Dj2SfdRSrUEYm7ThbNHtIAJqsBzqBTMdhHniayR-a6NxXMKRpezezSoWGMMZPzN-bYvsMVnzIEYKZI7D9hJHMyyWV9eC9cS8_5MCY3239zCFHmscnwqFMCek_7Fy0aI2pATT4YlTPJBadnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرامریک‌اوبامیانگ‌مهاجم37ساله‌لاکرونیا امشب به‌این‌ شکل گل پنجم خود را در فصل جدید لالیگا به ثمر رساند. انگیزه‌وچارچوب شناسی‌اش‌خیلی قویه. این 414 ام گل کل دوران حرفه‌ای اوبامیانگ یود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/30308" target="_blank">📅 21:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=jFIFBXuH7zDE_p-oqMEs1altpIcBojUjRWSwXEGzr1UWTt8QwG--FBXO5Ez53IDWXxKosL0mr1dkyFVV72XxKpVuayQzOGBFnDafGNyoEaZCUBLFsrM7pOTQ0axtSxeKASatJF4z_0GFvc_Z4Cgab_36DCSayuEE96c5Y0QOUCNlnd2iyspMY0QSOs_tJMFKvIN3CQLLYIGgKeNNwcj8a8oDNEYUs4XNhirM0P1zMMwMeQH8SA2V7UvhwfRHSlwf4OB0U1nDjoFDDRR8-DVc-QlnIwXSUwVf0V-TDDmo3wb4KV1b03tOcREdvIGy1FYFeVxOvIKXTUg0hyfVaqj2kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=jFIFBXuH7zDE_p-oqMEs1altpIcBojUjRWSwXEGzr1UWTt8QwG--FBXO5Ez53IDWXxKosL0mr1dkyFVV72XxKpVuayQzOGBFnDafGNyoEaZCUBLFsrM7pOTQ0axtSxeKASatJF4z_0GFvc_Z4Cgab_36DCSayuEE96c5Y0QOUCNlnd2iyspMY0QSOs_tJMFKvIN3CQLLYIGgKeNNwcj8a8oDNEYUs4XNhirM0P1zMMwMeQH8SA2V7UvhwfRHSlwf4OB0U1nDjoFDDRR8-DVc-QlnIwXSUwVf0V-TDDmo3wb4KV1b03tOcREdvIGy1FYFeVxOvIKXTUg0hyfVaqj2kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس رونالدو: ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30307" target="_blank">📅 21:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VALeHTp71FVkFAvwXJWo79M4O5j_M1ItcASYo8CGOyWakdRdc1fDulediJuHTx3r1u8soJ1rTkrS1CeswV1X12ojdYDQlQ6-kdXQpoGkz_uQcpKErKnfHehHWtzt3d1iVWyUtxnHHPTq5s_2gPcuOBX03q6EkpU8vJ1xdaDTQ5Q45to_t-6gjYVEr6907kM5IfujnwR4mZVssYK_0Je3y5kEG9-snegM0yNZKoVi618NroAEaEupqiMcWlER6GF4mNHswSxcDFOm5aQVjSMTPqVFbVqlvizkPwRqjPTLQUvocVkvcKBMOHyGp8N0WAfezc4M1GUf0n8_WusHot8Ptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بهترین شروع مهاجمان بارسا در تاریخ؛ رافینیا با ثبت ۱۴ گل و ۳ پاس‌گل مجموع ۱۷ مشارکت در گل درفصل ۲۰۲۶ یکی‌ازخفن‌ترین شروع‌های تاریخ بارسا روبه نام خود ثبت کرده و مستقیماً پشت سر شاهکار لئو مسی در فصل ۲۰۱۱ با ۱۸ مشارکت ایستاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/30306" target="_blank">📅 21:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EleklL-7a0y4-i2aRdFE41oTTs6RoSm78VjpUv4gEusvh4eOpHiU41ZvHxoT9reoIfExxsoonXhFVBEjYAyoGSRxtIWLXwef7nsmjDEm1eCqj89Hy3ZQX8YKY1d29PaBnucF-M6AhC6KsG3T1IeI-CKJzbgtpi7TSal_qBva0KVS-XfPTuKF4D1EXbL1OwiKN-21YbTvVEmB4KCCwPw_OHVqPq1gdqENO6qqs8cyXbYsMLEbhLiNLlv-GlHzv_bp5SSqHPgyX0wmL7xigzhrlHMA18GmSD2ERz2ZJwvrVY8kfb56xY1KnuGGpJqN1NoRyfMZjE3Oecaje5-hQztMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو:
ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/30305" target="_blank">📅 20:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
موزیک‌ویدیوجدید ابوطالب حسینی با بیت کاگان منتشر شد. خیلی‌خوب‌میخونه لامصب حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/30304" target="_blank">📅 20:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=uzD3gk2Q6FO9IrT8No5vwf0ArX-QiuU6KIpx3iPFAppEWAt23sAugibNak7ofVwU3vrOze-Wehy8TQS6VS4nX36IO-HhAUcF6Rf_03J4G7m73tH3kF82Re-RnDK90K7VkFfp_mxrhVNNx2Naz5JI64xjWlqFjKogKYgWzRBw9iVCo0-3RxZ4aGvHarxbHJcFqJ51S_S6ErZxOdgxQo0UpUVqmN9xXY_EBlZa48vxG7loS6KKqVv8yS9gZ5d8K7dDxgPWP5hlFHkZCSE1yqKST6-NfH-W9lDkiGF0QKM5deT3NtnXd0UvB91gxjUNnW6G74DYLe2SwVaFHFNzjH95AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=uzD3gk2Q6FO9IrT8No5vwf0ArX-QiuU6KIpx3iPFAppEWAt23sAugibNak7ofVwU3vrOze-Wehy8TQS6VS4nX36IO-HhAUcF6Rf_03J4G7m73tH3kF82Re-RnDK90K7VkFfp_mxrhVNNx2Naz5JI64xjWlqFjKogKYgWzRBw9iVCo0-3RxZ4aGvHarxbHJcFqJ51S_S6ErZxOdgxQo0UpUVqmN9xXY_EBlZa48vxG7loS6KKqVv8yS9gZ5d8K7dDxgPWP5hlFHkZCSE1yqKST6-NfH-W9lDkiGF0QKM5deT3NtnXd0UvB91gxjUNnW6G74DYLe2SwVaFHFNzjH95AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30303" target="_blank">📅 20:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30302">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=vFFXEBy6RwwBbQy-bBNCpIY1rRRSDGf1YCXobafrYWTtUTC5qy-hnW1HNyZDKJNeYGfUu1wC4RC7BSz4YlaJOG44XOGbM625NxM5nmf-U-qfN5jaVKZbkQhQDM457RpcOvpLp0LoJ9cUo9qp0siYIPYVhDcXawmafmDAQ3GZgOC-EdWkO0lswjUHr0eDKkaaLKAXSoRfOdgTAI39evAb799yjc6_NihBGzLnM4hYsy3q58eSe5SN5bvX1vVYUjEzXLQ36sVLNoco5mNx1J2z4r5938H1oQgJhDcZM7f7gYYNZ0HTQeeaAVTymchzUbbad-hj1gp7i88T5jNnK1NAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=vFFXEBy6RwwBbQy-bBNCpIY1rRRSDGf1YCXobafrYWTtUTC5qy-hnW1HNyZDKJNeYGfUu1wC4RC7BSz4YlaJOG44XOGbM625NxM5nmf-U-qfN5jaVKZbkQhQDM457RpcOvpLp0LoJ9cUo9qp0siYIPYVhDcXawmafmDAQ3GZgOC-EdWkO0lswjUHr0eDKkaaLKAXSoRfOdgTAI39evAb799yjc6_NihBGzLnM4hYsy3q58eSe5SN5bvX1vVYUjEzXLQ36sVLNoco5mNx1J2z4r5938H1oQgJhDcZM7f7gYYNZ0HTQeeaAVTymchzUbbad-hj1gp7i88T5jNnK1NAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره مهدی مهدوی کیا از قرارداد یک میلیون پوندی اش با تاتنهام که بخاطر سربازی او لغو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30302" target="_blank">📅 20:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30301">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=jvITuig-2B-OcVBKQPeaACGQQBbswBZrewl8Nhqipyl9fBQUuCAIWogO_vu7dfqleLw-UggOewgE1kehjCGFRlYoTM9ozpctUM9EZu8tnGFf5zlrkSw5n-WSO6J-mYu6ciM2DcjbJ0m_bMxbBsis6EA5V-JcX93t-DOPNUKn_uh-3FlnAtH_uZ2yBFMoOGlanw63us7m7cM6tsukj8vUctajl2icHjff_n_z4184NBjDKeztNSrDit98SQ3_XTMuhYv6H5BAyLgH5iX5DBlEWbH9pqDuhsaLyHxIWUVqMdusj_WcGDcdiJ9wE2nMVdAJCvnR-miQ_XJOwkUhvV9SewZagqgV2ovRRRKvj-g0UOd9g7bYAjYAETXtnPgChBH51Mh_VAE1nZhQa5byRUPp3UZZVrRwJV4C0hfCMkg3TBwZSsRaG3fShiVpUI1me46EpxLRlwhy00yZqEuqQQh1gWzsTIavnJfejGbqn206l18g2JwQSITd0U7PkvNPNB4-WukM61loI0zy0w5pgWcgVfm1q4IWGxaBL_IyuSMTnp1E-5IIswc0QZW2raC-TTREtgx1jSxKGSgt84T_u0cL3yl1PbGPYiwsXkooZRYJgi3CQy7q5jQro_L-I3rdUwYBh2o7hS2Lh_Jr_5gTy5jlNagueWtd9LSjNL0NedA-NlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=jvITuig-2B-OcVBKQPeaACGQQBbswBZrewl8Nhqipyl9fBQUuCAIWogO_vu7dfqleLw-UggOewgE1kehjCGFRlYoTM9ozpctUM9EZu8tnGFf5zlrkSw5n-WSO6J-mYu6ciM2DcjbJ0m_bMxbBsis6EA5V-JcX93t-DOPNUKn_uh-3FlnAtH_uZ2yBFMoOGlanw63us7m7cM6tsukj8vUctajl2icHjff_n_z4184NBjDKeztNSrDit98SQ3_XTMuhYv6H5BAyLgH5iX5DBlEWbH9pqDuhsaLyHxIWUVqMdusj_WcGDcdiJ9wE2nMVdAJCvnR-miQ_XJOwkUhvV9SewZagqgV2ovRRRKvj-g0UOd9g7bYAjYAETXtnPgChBH51Mh_VAE1nZhQa5byRUPp3UZZVrRwJV4C0hfCMkg3TBwZSsRaG3fShiVpUI1me46EpxLRlwhy00yZqEuqQQh1gWzsTIavnJfejGbqn206l18g2JwQSITd0U7PkvNPNB4-WukM61loI0zy0w5pgWcgVfm1q4IWGxaBL_IyuSMTnp1E-5IIswc0QZW2raC-TTREtgx1jSxKGSgt84T_u0cL3yl1PbGPYiwsXkooZRYJgi3CQy7q5jQro_L-I3rdUwYBh2o7hS2Lh_Jr_5gTy5jlNagueWtd9LSjNL0NedA-NlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنالیز دیدار هفته‌قبل دوتیم اتلتیکومادرید و رئال مادرید؛ ژوزه مورینیو به‌این‌شکل‌بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/30301" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30300">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErVHx4tnYPzar7d__KKHvdX15DFHMDL9OGwQG8XEryn2XSXnsq2iEd8D82-f19zEzq0DQK1W-jCvJSL2lrcu2V-DCJgsILz33KxPlDdJBN43tnGm91PUSa4POH0vE-tHOMRWCHkwnq6F2XPDkwG6vfsn9jhwJSTtsMRARYTBXC8t71_8_2GXTsxLcaA4HvAGdkm9GFMHeFxifBa2rAKBtQcFr26azme9u6T60_4su_E9lF0jGnK4ILJ0d9moa47k5Oliqm_-v5EvAKkXx81a5Pm5dyfmsJkV5onbYIOkUkZDSGa42MZZodgbDiy1yl0GtN0r6G8O0VpIn_Sw1CfoYdS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErVHx4tnYPzar7d__KKHvdX15DFHMDL9OGwQG8XEryn2XSXnsq2iEd8D82-f19zEzq0DQK1W-jCvJSL2lrcu2V-DCJgsILz33KxPlDdJBN43tnGm91PUSa4POH0vE-tHOMRWCHkwnq6F2XPDkwG6vfsn9jhwJSTtsMRARYTBXC8t71_8_2GXTsxLcaA4HvAGdkm9GFMHeFxifBa2rAKBtQcFr26azme9u6T60_4su_E9lF0jGnK4ILJ0d9moa47k5Oliqm_-v5EvAKkXx81a5Pm5dyfmsJkV5onbYIOkUkZDSGa42MZZodgbDiy1yl0GtN0r6G8O0VpIn_Sw1CfoYdS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 88 روز از این‌ویدیو تاریخی از خوشحالی مجریان شبکه دو روی آنتن زنده صداوسیما گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30300" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30299">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opzTjExt0ATqUr4p3O0DPJkgobr9_j366IdbO0LMa5VU4xhUCd7fZClxonHtbjNysc2OXOiXYW5ARJIoc1YgCsFCmS_KZrI3JscRHMFaZXH-99P4wji1oEK-KqlVF8UufEVQcXxsawuWs5XUTMb5wery0KUCXn9uUlnAyD1pIzZWAX0Wb5H2Lg-0d_hF2CRaq2Ce7amEi3x1-3e9HS3AyW4bSlAiKd3VZ0S61Vu1635zvnZECh_OY-QE4RIrB-uRYn8dEGPzomDnAUirVSeibKnH6zSIWV0HlaZimllTwT-O6ls9_KoXa9836WQoqk_5Xm-OwBob33gYZiOvxmhTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
از تحلیل و آنالیز تا پیشبینی رایگان
از مسابقه و چالش  تا همفکری و گفتگو در مورد رقابت های ورزشی
✔️
💥
هیجان ولذت پیشبینی در کنار بت بازهای باتجربه و تیم حرفه ای پین بت
✔️
🤝
همین حالا در کانال پین بت عضو شو تا در مسیر موفقیت کنار یک تیم آنالیز حرفه ای به سود و موفقیت برسی
✔️
🤩
آنالیز دقیق رقابت های ورزشی
🤩
چالش های نقدی
🤩
ارائه فرم های  رایگان روزانه
✈️
لینک عضویت
⬇️
🌐
https://t.me/+IxmGEx4ep9A0MzQ6
🌐
https://t.me/+IxmGEx4ep9A0MzQ6
🌐
https://t.me/+IxmGEx4ep9A0MzQ6</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/30299" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPufOWyrNYxBjfUgQKhEnyxqrIiNe6JPbDJ8b4Z1CHenU7q2jnmeZmc-TyUlaKLDiUv7xR6b65S44sB4E_Q9MJhYChEJOiL-PyhlTk_IJeaY6yTAD7Ykw8P1t4qIt4-aKLkASzVQuAF_l56HXW1kWASiS47RYr3BuD7luSq3SuuD_HEc2NdygXZlhBPRsImbGbOXH_GlxJ6FuthX_xkFLpDobsFApijsB_JIezdQyTbLePCyC9xTsiF4U_NLclWJLgEBun3PUuR9dlZ5Js57-ISOJpfv2-4x1imYHzaonb6FQT9-ihuXcVehX6BltjziBY1KpT2eXd8Cyeba2pi_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادگل‌های کریس رونالدو و لیونل مسی قبل از جام جهانی 2026 با بعد از این جام تا به این لحظه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/30298" target="_blank">📅 19:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30297">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbQ6mamsydrF48lmLl32XcaQ-x7KS2kQrt4hqDfu5FkcRY0GO_fouNtb44gnD8YePC7BOlW02wCqIUYxZMcwI6U4b_gIGjSzfvp3MLYnVDjv9bzTFNCSIrxah9qbyUypeJnY8cHSSUTInzY6RpQAeeVtS1rrG9m_FpZb89Fft8OvJC9Qff0HeVj80XaKvdVfuXBcZHGilx8wLkIBP8aaR8q08xvnXdUBDMC58ERQRj5jTRA-cIZgvH0y8PKYj7wYcXUVoSDki2w-6MrsuAKw4u64kgUFQ0J3LjnbnrvSGUbNHFqsDdng79XdzWCD581tVrqi_RLRdLej4r51pKC6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30297" target="_blank">📅 19:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30296">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiGDuBkYnJWEnNT7ph4FHBsL6BBIBwDGtGf6dR4UssVYklQ_hJ7UkKr1GsFGGv9mj1aAwkv_M3qMaOmQO71PDfTxo4quI3KoGWiUHHGTuHVEHdrqq2xJq5jwI1F7SK1rloQiW-p4QbCXfVPaCc5Ey5wLxQS15ul4I2P95lM4b59SC_qj9HNerLWE5o1CGek3A3DOLiT9fIPw1ODDmFnl-lEVJ7fdjXH4TAp33IpDNgFkiXbu9K2XcX1nakytbBS3EbJ0nSoMKwL9ayoPl_2yLt2hvyGxJ1ibbQg96pmyKqMXDNGgWeX3aE2paq9ejnuh3aZY8TCXgHpGbrKRYpNvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30296" target="_blank">📅 18:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30295">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBMEH-7NL5NmkF6G30_Yur-A2fMoInsMHfIyfctlJ0WFzn5YwyPqlaZk2G5Qu-WPw1aZecHlQSN_WHuyBohF7APW7ZsDcnY0zhd6QEjvsw6RNZgC6frQhS0TRRELG3ZlFyXI7DJcj8Nq3FyctgiQICAk1yPFTjzjZURYgw12tMm-_ut1Fe6gVNoBzJwzUOUuyZXjweOe09wjF-thXvKkzPudVWUw9Qt3mrROFIcZFQoBFVL1ganCqNaqiuhGbJoOnvwHeM8eTSDshmgFPHC6op3i6E-HAl50hsLWIGJVX7aetlKjVhBd0bk0nMRj3IOIYeXI19rtJnURe4TtttwdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30295" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30294">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=t_lWrczdLQHBy3XjoJ8YcUhc3ahr3kTn1ZudzCUpaCR9AEXvNB4SR18n1slalMHni59pqhYuzqEM___1_SPGL6RPauOP21TCK_0c5zdqtc0l4eOE8qiVT-Cj_VQwxRkVkKXyek_MNPwJ0PEIUqfPMdogLVf_-YFZ7IYTy-XhEOchjXhvZ1d_y9JR9V8og_oEvXNI3AfY1LbDbpRlddG-rIt3rZrGotA4WNmt1JXUd0GKHXZcJcCklxBAQ5kPXnxPP8oeBS0MsHBMyEh_c8cjBvqlHIrbnfSm-_G_pp1-2NofuWNiptl6jL1diRLRlOfnYJNDs476xI_Yg9pKHUrLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=t_lWrczdLQHBy3XjoJ8YcUhc3ahr3kTn1ZudzCUpaCR9AEXvNB4SR18n1slalMHni59pqhYuzqEM___1_SPGL6RPauOP21TCK_0c5zdqtc0l4eOE8qiVT-Cj_VQwxRkVkKXyek_MNPwJ0PEIUqfPMdogLVf_-YFZ7IYTy-XhEOchjXhvZ1d_y9JR9V8og_oEvXNI3AfY1LbDbpRlddG-rIt3rZrGotA4WNmt1JXUd0GKHXZcJcCklxBAQ5kPXnxPP8oeBS0MsHBMyEh_c8cjBvqlHIrbnfSm-_G_pp1-2NofuWNiptl6jL1diRLRlOfnYJNDs476xI_Yg9pKHUrLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛
خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30294" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30293">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=ATmKJKM6C7IUJuuOJ52Gthk4w4139Pk_fct0z0uLVm7P8FN-93CPLJpBfbRMU_KSF3GRYX8oOQQPgIN0h2q34vlpE4dh_1xQSLBvq0tVPTV2BsGZPoYViJiuBeDdvCQ1rYWPOjKTjiIymJFBm0WqRRrk-Hf6v2rtMkvmthK8jcnZX4k6PyzHTd-dxbR4KnBDdqVP-jzQKMHQTckn4GMlAOP1B8T4BAFGte_5pFIyf6GPQuyNzDTqsgT2DsTOGK2Mfgy-YCTIGpTVJNQZ-Ag1zK7etcggywbIINL1TjG80dytq7vw_0tJbENvVXTTk7Ade3hG6zziNLZoD3WDbk3fbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=ATmKJKM6C7IUJuuOJ52Gthk4w4139Pk_fct0z0uLVm7P8FN-93CPLJpBfbRMU_KSF3GRYX8oOQQPgIN0h2q34vlpE4dh_1xQSLBvq0tVPTV2BsGZPoYViJiuBeDdvCQ1rYWPOjKTjiIymJFBm0WqRRrk-Hf6v2rtMkvmthK8jcnZX4k6PyzHTd-dxbR4KnBDdqVP-jzQKMHQTckn4GMlAOP1B8T4BAFGte_5pFIyf6GPQuyNzDTqsgT2DsTOGK2Mfgy-YCTIGpTVJNQZ-Ag1zK7etcggywbIINL1TjG80dytq7vw_0tJbENvVXTTk7Ade3hG6zziNLZoD3WDbk3fbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 3.5 سال از این‌گفتگوی تاریخی علی فتح الله زاده با محمدحسین میثاقی روآنتن زنده گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30293" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30292">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAhmuTQ0YZ0vlQj81311dWCpWbjqBu3cAbMz3j9oc_KjY5fbcEwMLzMu0i8TvJK4SFI2uAS-nQ9fSxeiZjHEha1xDx-5m_qrJ2CsEVp5F8n0OSDv5AT4Hwu74AZB8gP6rRBHjYkHoum65jhoA0tzTsC888toPK79EoTaoJWQAFao-edj2ZplXpI8x5bvFkhjt8aJc-pIK1deMqs09Y3Vp9MAzW12Z_OBTEIrtlxsOI9kgA4vk-ppcQvQrRMqMNG6OhNoi0wt_bw8QAZwVDnFMbVBiq3WIq627LEYVrZTqoK2s1cApp4FDkrT3ui23VYXKagrcH2QdYoMUfh-JgysrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشرف حکیمی، ستاره‌ی پاریس، با رد اتهام تجاوز، مدعی است که این پرونده یک سناریوی ساختگی و ارتباط آنها فقط در حد بوسیدن بوده‌ است. در حالی که شاکی بر ادعای خود پافشاری می‌کند، وکلای حکیمی می‌گویند امتناع او از انجام تست DNA و بررسی گوشی، نشان‌دهنده‌ی دروغین…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30292" target="_blank">📅 16:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30291">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv23Z7rhs3RCxr-dOJ8N-ijV49pI04tFCDaSlXazK6xMs4UyFekJfNfbdsPaN4C3kSAhTx0bkwr3x51_2Rww-XeE-6GpYABZihq45Xy739Qarn7UszLUqQuJVVA1kQ6kZ3mwgsD5ZNQorz33rSDXf0GSMFCH7RKVfwOdkJMh25QwaR0GEQh0_T2wnfGqOuKLg6jC-FKf2O1rP7lWHgz0hKXGGKw0g39_RRQ5QVxOqtRQz17rk5lALDojpC9N6R5aphxYIIlpJZE-kUsa_ihp-3_C5Odt70M-PzKthZXzmUl8KdfKbDqB8jmneDRfQJKe4PZDJ2HH00EBgrKsq1dmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30291" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30290">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUDyXmJ36FEU_MT25i-4u2knrfB4Z6_u_NWWMF_Afw5iZgQaT0XdDyusTKGid2kVNa7HftQUvjaOSzzCkPTNRn8_XvDVXbuhEiIwc2-4f8YmUryyHL4icJz1PdDDSFTDuWk5KTBdXoTj1Xcj1zQR8iMHVIbR4xdcNQCjoRizIVfhvS-TrqNKj7z7lBwBHpPJgA1lB1mklHsaxkUG_YmlVozdpFtO51-GRmE31NkEu7Fm8VQFRXlkFm_B845O0k0ZgVvua_ax1ah_Wgxo3xXzBAFXnCTtry6bTr9wvajXPYXHvvtOGtJgx0MjAskbVIwvX9_UOtvWC6q43YyEcBrLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ظرف24ساعت‌آتی رستم‌آشورماتف، جلال الدین ماشاریپوف و یاسر آسانی 3 بازیکن خارجی استقلال برای حضور در تمرینات آبی‌ها و دیدار حساس مقابل تیم تراکتور در هفته هشتم وارد ایران خواهند شد.
🔴
اوستون‌اورونوف و مارکوباکیچ دوبازیکن خارجی تیم پرسپولیس نیز تا پایان هفته وارد تهران میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30290" target="_blank">📅 16:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30289">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2_l66wN5k9CQOaT6Rix9G-x40nZ3C6o1igDBgQXGWLus28SsllypWOFnXPhALtyfblsvo2I2rGDWpbLo9hcK6709slujCkPEITmWsGfEEHuWeaMJzxreIkwg_zpZAUxMYPhiGSs2THcZQRHkeGoqpAaVyxLn52CmZFbAAPcbYSC4ukSLt96Z6B-MZQKApWh1yakL6HtxB6Dx-W4F5R9pDhEUpPSSOpq2vscrx_bQvP_ejXvgkwRNekvfSqAHBVIY-h2oGa_i2f2cYbdnYvtMUOkTNUOix5O2VAMr9sgjtiXVu7jn9PSdKkpUVBEpQ9h5gzWAMwItCUaRqXcYgc_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تیم پلی استیشن ایران در فینال بازی‌های آسیایی مالزی رو دو بر یک شکست داد و قهرمان شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30289" target="_blank">📅 15:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30288">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmC4UYlR37QuYf3tPuFAYC-L0cLbLgCoSbMJlBxT5zUZEIYy1U-YUcNZr6YrZixaPjsYeRHbL-La9pxwItW97qyCbEotYXi19yl9rkzAjluyr5kcji80xnaziqniCfpe6JR66oyGZykGa3VTalkRXBhAl0YwxlptGGjerMeoxuMA8GVe7tHixFbav6wdGTF40rZ8NuDNYXvoxWHlwEo3pEDnuVlA7SaYWNVGJU0Rf4rpKZeADwlqaK4LRl220FcriVBrYHHfUSGQARtU5GHErvKEffhL8Z-M7zjys9oZfqUGjvHhSLK9anOX9QOMSGT4II_YXEEgiLSj81lUAr3mbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه.تعدادگل‌های‌کریس‌رونالدو با مجموع گل‌ های رافینیا،امباپه و هالند درکل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30288" target="_blank">📅 14:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30287">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_ERqF_zsYr7LAjZng3d4yMUGh4wvNqoEJbWpn63QFDWc4Gt3uRe0PWXC-JXJMqg_EPw77uv4G5ML_uiXQNkkRLGmWUoEqD94uNF1LOWOEYvWpB8SPCI2OkqcdH_pjx0JRFEeKND0a1lc4AopSO7xBHtjQnxea0xGnRV8rz7WPsqyXn1xV80IwW1k5tPTc85AwDM75xx5T538GORcWiJ7xRlsr8kFuhGj_8aDHqRpmdGIj65jht0tzx0oDJi7-rfETkuV-P9c46r1gB34TB0RoFd28XcWfXyeuJh_D9wovjcwaJCnRExK-5VF28elc4-yTy0Y2c2fdl8boqZxmmPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛ لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30287" target="_blank">📅 14:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30286">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7GaLUhaogIXL_lGBaVzWoPNVCq2KprvpCdDXjUaE0cRKujMGFFE7XoeB0oGsbJSPjHZyXPIJJXRmVBvWA3v-RfqwkSu3U0WqevGAFInQOhEodtbUsbT1MJPXCraA-z3FdQEpulefUWuqdUwIm4bmqtqlwaY5GCLMAsaxiq4Dz1vMCffg3MlM3B00cmBZo77mrVXjZlkvYlrM-6AAIdhdO2uDeN20bIAsHJ0UhUk1JCvDznl9WkeoPXMSAj2c15dwOA4RPRNGLDKzbyTF_EYAjgRE2gcB1r_HQflGhFucquUGhpiQ6tdPaHGNJqn_Msu_k3jgjPJz9-TxelTyCR6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30286" target="_blank">📅 14:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30285">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVv945PSqUUNZO5M09_SD5AFoVPXDuSMoO1r8hda6fEWwXXxMRGRpFMOGPWpoLzlPzSUFdHGRcPWW2Vh9yOYXnYzGLs_MrCejKjmjqrHDQ8WFKtWPvY3Y4zUwh-bxCBIZvpsPyPSOhBn2QWA0Zanr_QoYRgf2LI03ijLmoOs7-i4Lx_FjuYBo4qdVeeqko3D-2Ls2k2vZzwL6IMHCPdn4-PMY_wNHmIDrdae670qihZNJ17qkqYx85K-MxogbCzDdHCpfLddYuiE7GakpY1W7XghFswCiwUUOglnFwzB1kx_-n0gqwNvdbZvZedEx1x46rpvmuvWWDCvL9OyXr9LXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇳🇱
تیجانی ریندرز ستاره هلندی تیم القادسیه:
نمیخوام وقتی فوتبالم تموم بشه باز کار کنم به همین خاطر تصمیم گرفتم به عربستان بیایم در کنار کیفیت بالای لیگ این کشور آن‌ ها دستمزد بسیار بالایی رو به من دادند که زندگی خودم و کل خانواده ام رو تا آخر عمر تامین میکنه و نوه‌هام بی دغدغه میتونند بهترین زندگی داشته باشند. یک‌سوم‌رقمی که باشگاه محترم القادسیه به من پرداخت میکنه هیچ باشگاه اروپایی پرداخت نمیکنه. از انتخابم بسیار خوشحال هستم و میخواهم سال‌ها در لیگ حرفه‌ای عربستان باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30285" target="_blank">📅 14:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30284">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1454042688.mp4?token=XlSRuonoHIW1K2SpNjqBWi9Tu7Lpyoebea2PHg3Z76RfkuvgBLV3THlUICi3NLKg798j_tcRv8E9XVp79fHaM9DyWMdbxjfyv-xE5ZQMvqXT5N3vRmRMeR4R84ib73q4wqadCha57eZLDJXETfn8Di_QBd77q22_-X-8WpmIldHJWI2D6hyO5S2nPAyTwVTVZgJPUKdVkJJ7NU7lY_8Se7kEncv1Se3LC5gZBO_jmQTJQsaK1VasaHPgomcfy_UBzuI56FB86GbiRZVUD2gKUJl_9DtzDfP3Ru27-PT1L4ZAAu_4eYN4PPu9zlObgjUHvFXLojhogoob9PzUuH-lfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1454042688.mp4?token=XlSRuonoHIW1K2SpNjqBWi9Tu7Lpyoebea2PHg3Z76RfkuvgBLV3THlUICi3NLKg798j_tcRv8E9XVp79fHaM9DyWMdbxjfyv-xE5ZQMvqXT5N3vRmRMeR4R84ib73q4wqadCha57eZLDJXETfn8Di_QBd77q22_-X-8WpmIldHJWI2D6hyO5S2nPAyTwVTVZgJPUKdVkJJ7NU7lY_8Se7kEncv1Se3LC5gZBO_jmQTJQsaK1VasaHPgomcfy_UBzuI56FB86GbiRZVUD2gKUJl_9DtzDfP3Ru27-PT1L4ZAAu_4eYN4PPu9zlObgjUHvFXLojhogoob9PzUuH-lfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنایه‌گزارشگر به قلعه‌نویی و حسین عبدی بعد از شکست مفتضحانه مقابل کره شمالی در بازی امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30284" target="_blank">📅 13:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30283">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30283" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30282">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=ZO9ikl4UkvbHgx71YS-QjLXs1sd67T-iYNYKIXvxB1yu8M4Mkt4KpuLAjIW6zgP16nW9qQFY1waSWRoua_-c7EehaJC_Q-vgwEag1zRQjEJh4azEuiiytDNm33rTd8trhAVkFWXn387IHCmsifgAxu1Wt-0ptvq5nDrzdMAVnLQbnbw5jqKHPAGU0CkfqTYM7DvLemW13eaPGIZWlKF_9B2q2xMdcD3FSIDY8CLCXhcLsd4arCqV-dDkPsqYV9i-cHDglNXLRZuqdEQZm-ug9LFSCxUlLPQv7v1HWiHFStuL-KRngA430zkIjiA33idpRxWKJxVv7ClpmkDTL4jBQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=ZO9ikl4UkvbHgx71YS-QjLXs1sd67T-iYNYKIXvxB1yu8M4Mkt4KpuLAjIW6zgP16nW9qQFY1waSWRoua_-c7EehaJC_Q-vgwEag1zRQjEJh4azEuiiytDNm33rTd8trhAVkFWXn387IHCmsifgAxu1Wt-0ptvq5nDrzdMAVnLQbnbw5jqKHPAGU0CkfqTYM7DvLemW13eaPGIZWlKF_9B2q2xMdcD3FSIDY8CLCXhcLsd4arCqV-dDkPsqYV9i-cHDglNXLRZuqdEQZm-ug9LFSCxUlLPQv7v1HWiHFStuL-KRngA430zkIjiA33idpRxWKJxVv7ClpmkDTL4jBQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانی بیخیال هوش مصنوعی نیست؛
این چه سمیه که از مریم‌امیرجلالی و حمیدلولایی ساختین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30282" target="_blank">📅 13:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30281">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW2CtsLE1ItLlOUbMxLsJJ4UJ1H3CpH1fJPu_puz5Cpi9hkz1UPu1hyqTtcPQEOUro_0mDfnMuEpRMQFhCEv0cPKout4Ez5utJRb4uhsyQlo3F421Soy0gDIK-SIbQSYnyEosnbYiy-SwXCQW9RD0sYj2uNqZdYV73W50FwOcTbn5qqte1bErB2PIGvcoU4HDlmymL4i2v5O1g8ASDhbmNI9tOenH6e7eOEht-iY8YD92bkiDlonfkeN3RbRWA5tCGauH6AuRtwzHNfPsnnl0nwY7XusYnSUx6ky18yjn6o_Sor4SAp55HbdwX8BmsJlwkXgaJqtxs9Tpk18LLyrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب بوکاجونیورز برای دیدار خدافظی کارلوس توز فوق ستاره آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30281" target="_blank">📅 12:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30280">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdxqiBgH9FFC21EcaNdq2W2mWKuHTomyQNwMPVpL2IYhegtvRjBhaTj1p0VAr_4T2mwc4va6yqyOjzUyQVRuqkHJebNwIxFH7fID_UYJHi-KDVeQgLB4EclROlJvj06zvqSxSchuUQN3XiD5KBflFZ5aUFJfecG9aykx9Qi_7eENjyodUAQp-VIQeHqDf8VTmh6q1S1Sel27R1yzvIugNDfkxyHXlT0-meX4IhSGbSaSBPvXoyiRdazXKp9tjNu9bmAbRh7GjOj0lP83SambiIKcmH6JaFoS6hM1AgOsMc79yihG_6a0KuGM1ah2pPP4skcA2kLg8ta7P9p-qWh0AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناس شبکه CBS ترکیه:
«رافائل لیائو فکر می‌کنه برای‌تعطیلات‌اومده ترکیه. اون به دید حقارت به‌فوتبال ما نگا میکنه انگار ۵ بار توپ طلا رو برده.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30280" target="_blank">📅 12:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30279">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk2abAWzJkKs829YuvdjMvfeV_TbmdtR2mP88UZETptnWk57-MP6F-Gfob4V_uWQ5Exc_PdHwFQA0gLNqyC340umgN5VQqcuKa4iQlhTlLgpL-vU_KQIaMKdXH9VDOprxuw0UZ1KtPy4yu6DDciW6BgfQoveL1WEtxoLNF-m49O8GQ688oofYUDOJGQO4oa745Xs-UZRnndY7ATIY1tZJGLjFhA--wxg_vcj1ObLzzPn7Z4ySNUCDb-qwQhmoYZN-shnK5LSAU73fq_jCr8p2Xh7HWngozLlCeAGbsvbl2lKjoLj4FlnzwmZVfBwSpxScEccgo1CvimivSDAKYhf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30279" target="_blank">📅 11:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30278">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIFSkZoz-WbxOzm20Q61utX0FfcHlal950jkjH7CiM9KMSuLrN2BxBtzbim7Jtpfo2vaPVrDjB_i-y9EqHAyfspGTZZPBvTIhMOj08h6eGybaM4Icrc2oVs-Yeft9-BBhoZ4bBTOH-hqUvo-FzF7BTPSKgbwMsWoonG1ChQORzArZpsvxDU3D0DD9BU_JMVw3n_zRvfcmFd6pFBFS0ejdS6NeYDHj-38HZqk9WMHQMqmo202vXN2oqUYlhiv25BWtT_Oo1KnHCjGPD2aaVrysVKdklX15DGc7Kw4ncIN4glSBtuoY00v-54uSe6ZyJunwS2ERUw-mAlGtSkGv-0Rsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30278" target="_blank">📅 11:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30277">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0JySmYOH4bYHCcSM71h8eSLmb6kcxzC-MHetlU_5_idMrJquuuPRcB1NTtWs6ms0GXj0yXPdgS6Z6en1abSB201z-GrJLAPctY0k7cfwZI8GFvGENpXvtjZICuO1uyqZg_BfHUsrolIQl3IZorYhVbLA6PVPd2-pCcDJbBrlFUuXEaUUXzvAtmHo-brB8sOVpBGMLwNS8BEM1z-FfjJFVmSRsNx0R9KYVcAuFUtdgOD9Fy2eU2WUhLvufLMYYztkWnV9QuTBAKSbU_u5wD8sfOAM8BKIvC36crHo41Mu7W2SNwqZkBRVV0ZGWtQtsYXvP-s9AQW2WVAvgmNCU-54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30277" target="_blank">📅 10:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30275">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBeFeRdsk6n7gNBRhwWWZZGzJTwVKgg3oGrqKpUCOw-hDm2TtOjFs3PTJd7qffb7Kf0fJTAR1pgtEWgiKYgcPHj5adHLVRaho_TbTrJIFSn2zOKdihIiEWCnmLVUOCRSAkDAOZmw1gn2P-REfi0DUiKHa9jdogGsTwK2-i9mwcVFe-ovaaoxOH9vamV_P8pavLcnPiIDT4QrYCyUdjO2ozitFZvI9H9LkTGx0ydFPMtvRQDjje0Wv-hVGL4oqKF2JekKQB3-Fs-Iwacb77F_VYfKQ8BLmurUKDiNEVYLXJ9cwsZ137wACo-Zk6sEU4KZg1kEEJICl86g0mt8w0YHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCFkiE2-5bIgIN9tddfJ--hmG_j3mcYwVHw1o5HxYW-5aJLJMhCWBSpjHITW978zlBSKNH9KJhGzjMZDPX7ka8SDbrPkI46uGjNglrzmXkLvTMqIAr05qy91C2SMFjp3suJ7l9S7VBA8aoKP5gnRvwtm2dNm38Oy7BQQEY9tEb1x3NXcHpDsbf0LsJlBq5sceKZHwjz3FYlGsv2F_kYNbQ79l9O0z3C_kPQOaZnD81_hNJTY7JKR3kUhUR3AB8Y3CLUKMZL8MloDz0cu6vx30K7h_Kij0y4RC_4w0U4c-FjguXfIjxRoQX5x0li0uX7BpJMZA0w0n10jl1WbBAEUZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30275" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30274">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWUCg5QmaHkvsoTVoa7-_c8Qeo10w1auaQSq9rrgv1QVufYpJCKlVIZsFg9KVsqf4hNBKXycPHgb9Edgs02v7DZEft50Dc6ymyiEk1p55cs4tpZ0KEtBEsYmAhnemU3jGh8qVdxb4BL96DAKj9AGXakYORe1ZHZhOk-fWt72s7-NhpMfs0iiRV50peJo6cCbt0gvbh175zGNyglmQToUtLwo0-LgA1bzobJeJ3eb-sHDiBoyNH2FRzbwK9bbs4ZXl0ApRgNr1jTVCDV73V1xlrEFTYynGYzV-CI00DxCR0p59F_VzFGi51cLEG9IQ8v8T0q6Ux7W1pGF_FI2FuwJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30274" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30273">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzRxZMiKof_30so32IkMQ39vyfxbtqfyr8DCJJvsgk6f01LJGBz3uWuFlI0j98wDj_vjt7IHl5pgQ_h4VGbMIt_LR6Q23GAPYdkF2TbO09oEbLV-WurxN2CopJukBL7FssyTnTDKNGYDz_66A7smE1Zb4fgvHMcCGDJggkfqe5r405urva1UUdV2Gai3eAeEO8D3CzkaOdgoHsW7ikEtwCNw9p8AEwLI4Q0j0PImcoE4hox7iAMA9JL4JyB_hlHfK__MWA2o-8jqL8Cx5ttIMKHHpnmUV0ZTTkML_xAJYROYetpKh8nD-MIB18pYvlx1lRgSe1_vMGJ10cz9BbDqLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤬
گردونه شانس یک فلک
👑
هم برنده باش هم لذت گردونه رو تجربه کن
🤩
واریز کن
🤩
ازپشتیبانی کد رو بگیر
🤩
گردونه رو بچرخون
🤩
بدون پوچ همیشه برنده باش
🌟
جوایز بی نظیر سایت بزرگ یکبت
👇
⭐️
آیفون 17
⭐️
ایرپاد پرو
⭐️
پلی استیشن 5
⭐️
300
💵
جایزه نقدی
⭐️
و هزاران جوایز ارزنده
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r1
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30273" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30272">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3EHlt82Y026fgD_0-K2IyR86chZetenfQM7Aghl11XQ9NRWRTGer1ncqXVT77UrcMYZgol0m7QDRHaL9F1WPuCBXcqyGb3Up1rWNlBXWTjDm2SYTtfHOwywlVR5MVn08cgtT7BHgQjPEw0qmM3oios22WnFoMovFkFxKkrElzflnkNzRHHQL5VPEHfB6o6zYXnQ9iW7j2MuP_GPj-WHSPmdS4R0cqOpaQgy4ChsZQTmWqJqIfdpkrmkVNMaQAn8j4g9D6tUHnQRRUWTtrm96NmND9qzNH-8UBvWB_Sn-vgNc7vCUuca8mKtg_8l-30IEAHW27FrZ7ks5Uy76bbFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مثلث خط حمله بوکاجونیورز در بازی دوستانه خداحافظی کارلوس توز آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30272" target="_blank">📅 10:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30271">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=VLkNNAIZ7aCh-SO_i3GFAVih-ppCaokwxARz4hJcbQUIcsfwFxpD7mhR3AlVxxlqrZz0rKtcfoUQTQhDurFTkJNCPUJSvDnQqq2852G1GluIyn0aybRzRD6BUytv91R92EfhcnS30SqV-SHUyWk3uGx0IpWef8L7vbGf7uH3Gfw8PAdE2EaD5u1eMieYRr8iyuuTuW4ZpOeL4qREbDmQxlGYhmQBVPdFY-YIf4jyHaNHX6jDgbspwo3BLu3nJc_8zr6vZwgwynrbSWdY9wjcc1Aqt8kKaVLhb_uDjoZP7HiCtwntlMlfHBxFpxf6oKYNvyee8LfkhVWFwxzaH_sWvh0Md1VtMvZ_EJ9_Ws50KX9wYMZio-uJDHi5WH7Al2bIihvDz2gDiuy6wuojgpQn-PWDpUxdZER4FVHzpNcytawpAmIABIp1nYDRTLpUgI2qbXWxt_AoLElx5rxJWYm8CtsFkYEZtbN8HcEfuiWcC9Pmm0p5_HyYl7PM5emGBSbjxiSyURDR2TiLzpX9rXFDwluFMtPbfqMmrpzW48_ZEWcE6yQYCdfE6fP3mptFfkZkYYNIp4lKoiFhkKZizCAXaFy8LYhh__OXz2qP6xE20djD7GvtExNPB2M0za7m_Ax5i-rqK4C21DwBkAClQ9DzkDayb84c8Db730_-E6qPxg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=VLkNNAIZ7aCh-SO_i3GFAVih-ppCaokwxARz4hJcbQUIcsfwFxpD7mhR3AlVxxlqrZz0rKtcfoUQTQhDurFTkJNCPUJSvDnQqq2852G1GluIyn0aybRzRD6BUytv91R92EfhcnS30SqV-SHUyWk3uGx0IpWef8L7vbGf7uH3Gfw8PAdE2EaD5u1eMieYRr8iyuuTuW4ZpOeL4qREbDmQxlGYhmQBVPdFY-YIf4jyHaNHX6jDgbspwo3BLu3nJc_8zr6vZwgwynrbSWdY9wjcc1Aqt8kKaVLhb_uDjoZP7HiCtwntlMlfHBxFpxf6oKYNvyee8LfkhVWFwxzaH_sWvh0Md1VtMvZ_EJ9_Ws50KX9wYMZio-uJDHi5WH7Al2bIihvDz2gDiuy6wuojgpQn-PWDpUxdZER4FVHzpNcytawpAmIABIp1nYDRTLpUgI2qbXWxt_AoLElx5rxJWYm8CtsFkYEZtbN8HcEfuiWcC9Pmm0p5_HyYl7PM5emGBSbjxiSyURDR2TiLzpX9rXFDwluFMtPbfqMmrpzW48_ZEWcE6yQYCdfE6fP3mptFfkZkYYNIp4lKoiFhkKZizCAXaFy8LYhh__OXz2qP6xE20djD7GvtExNPB2M0za7m_Ax5i-rqK4C21DwBkAClQ9DzkDayb84c8Db730_-E6qPxg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛ مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30271" target="_blank">📅 10:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30270">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=lcx-mRngoM__T8Ox2igmc_bMW2wHwfpP8bNG5he8cxRLI8Q5hrYnIE6KjJAMghRfTpxnRr7us6bDq_ya3F7mIFpr3H4L_CNnpdQD-RmBsjQ0qxsI8ldor8yWUv321mOYcUiCw50UeLWpLs-5LaKESIuESAKpL0qR_dhgCgKCN0Bh-tnFmGg2g3cWo_VMflfTZJl_n8_Q7TEAdTHYPbSNdFZpmq5S1-2OYLCmucTOeLItz2l1CA9BwxCBhVzoyeYgyP52DtCMYUfbNgAD7ctFn0OVFkC-1nX_cKgBraZYI8G7vaI0hSMofZnb6jX3LGJ_O1wG09--uRz917UjMFgrZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=lcx-mRngoM__T8Ox2igmc_bMW2wHwfpP8bNG5he8cxRLI8Q5hrYnIE6KjJAMghRfTpxnRr7us6bDq_ya3F7mIFpr3H4L_CNnpdQD-RmBsjQ0qxsI8ldor8yWUv321mOYcUiCw50UeLWpLs-5LaKESIuESAKpL0qR_dhgCgKCN0Bh-tnFmGg2g3cWo_VMflfTZJl_n8_Q7TEAdTHYPbSNdFZpmq5S1-2OYLCmucTOeLItz2l1CA9BwxCBhVzoyeYgyP52DtCMYUfbNgAD7ctFn0OVFkC-1nX_cKgBraZYI8G7vaI0hSMofZnb6jX3LGJ_O1wG09--uRz917UjMFgrZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛
مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30270" target="_blank">📅 09:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30269">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=JAyVsmgQoRUG6JH5eW-ynWcab00Pk43QPYxMHDyogSopayU7aphzJziPZU4X5MQ2inzcLop_c-h38OPTzyp8LFcsHoWnThxkDp6Zpp5c8i62WoK0Mr2XK_m7rmYBjXxgfEMJMlMddgZ8C-ckC1WyyJCdnz2Jsf3xgMrLW8fRd-ffO7gxQXDIFBLADdXYVU9Xt5bOSJ0sDeroItUyyP714v4Krr8Gynv_ggqKDSXbwYpSYY5eroTdpdzJgCsjmBSVNJ-Ydv110hquz4sSdY_p1xbziG45qj4DUVgffyBTZz60G6_Wz1xaWVak8aCYOgydxMhN9UW-wHN4vV6839ZEzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=JAyVsmgQoRUG6JH5eW-ynWcab00Pk43QPYxMHDyogSopayU7aphzJziPZU4X5MQ2inzcLop_c-h38OPTzyp8LFcsHoWnThxkDp6Zpp5c8i62WoK0Mr2XK_m7rmYBjXxgfEMJMlMddgZ8C-ckC1WyyJCdnz2Jsf3xgMrLW8fRd-ffO7gxQXDIFBLADdXYVU9Xt5bOSJ0sDeroItUyyP714v4Krr8Gynv_ggqKDSXbwYpSYY5eroTdpdzJgCsjmBSVNJ-Ydv110hquz4sSdY_p1xbziG45qj4DUVgffyBTZz60G6_Wz1xaWVak8aCYOgydxMhN9UW-wHN4vV6839ZEzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌‌های ابوطالب حسینی در قسمت اول برنامه جدیدش که هر هفته سه شنبه ها قراره پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30269" target="_blank">📅 01:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30267">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pqi93xOccv0m2-tcF74FfP9-m1AYu7dmTwvZJutD_4jSI5UaYeu4jZ8avcaRjEICaLagJg75QUwV4cusf9Wb4R8l3RdkMNPII3ZE3oAMd4EwtlT2CTdRAymZuYKg31q40GUypBrNqsBQzUZfO3-QEAhz0Uz0SSGgmEAbSWi74HlBqtNVwdv9YGRxBrupbpLwi1d29kOzZskA7t55BZ5PQNPdd68YLTm9BYiUle-aLDtxAC_OT_sx2Kob4kHGwYIBjiEP6vUo4MkQv1-Dc0L4BLcZemwXYl8zget1vKI0iK2BEJp1Lo63K-UMtyJzJpVNviDcr82UWXCLaHDAbuzLyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ بازی تیم‌های امید ایران و کره‌شمالی برای صعود به ‌عنوان صدرنشین در ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30267" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30266">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=SLp5QuJ52Rn-KE8k5cyMmYXJyzmU2gEEABFwd2ODmryKP58do-Z9D9fmwjIaEAxs-WprkRIEEMcE1jXS2Nfo4vP4CRcKba-9c8UCBhC53VUipCnGvH_qU-6zdEqPcAfMsli2yQiGa-hTPd-MPxbdpGPbkVXkvxuRXbgJQ22F4DRlTmvv0S7-HmbIZxpg87rnxFtLvXMAZrYzf8PY_Or_mb3ql0uQrXi3AnIucJZZZUflauGlkdBopCA4v8uAq0I1K7KrSIx1hNHa_tasRHSqwo7zZM1TSI3JBl1OEo8h2ElHLD4qUUkRV98NyO66GBOAZZLsMwuGaLzhEhd2NpfrPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=SLp5QuJ52Rn-KE8k5cyMmYXJyzmU2gEEABFwd2ODmryKP58do-Z9D9fmwjIaEAxs-WprkRIEEMcE1jXS2Nfo4vP4CRcKba-9c8UCBhC53VUipCnGvH_qU-6zdEqPcAfMsli2yQiGa-hTPd-MPxbdpGPbkVXkvxuRXbgJQ22F4DRlTmvv0S7-HmbIZxpg87rnxFtLvXMAZrYzf8PY_Or_mb3ql0uQrXi3AnIucJZZZUflauGlkdBopCA4v8uAq0I1K7KrSIx1hNHa_tasRHSqwo7zZM1TSI3JBl1OEo8h2ElHLD4qUUkRV98NyO66GBOAZZLsMwuGaLzhEhd2NpfrPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
توصیف‌های عباس قانع گزارشگر مسابقات فوتبال از لیونل مسی فوق ستاره آرژانتینی تاریخ مستطیل سبز که تنها یک بازی باقی موندهه که از دنیای مسابقات ملی برای همیشه خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30266" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30264">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eISWRU58N8nIv5JBiJTlH6AJgaQerMuLjdHDyxdcKpd_dirBn7l7x78FSz4ITpT5zVebtIM8ShlSRK1_R6tOsM2N93X4CTBcTAf_yivv2tEfC3nYl07GXRddcRJI8AJjkFrsdxNf_RxzGOfwn_Cs_9DNAz-dmNqIJoEEhOlMHpWHQTrKV5BjppDDzEaIZ0A86OnWTTri6V7D2vvjEwNUzsjzOxBSyIw4Gx1GTi13AxiU1fQiLEQVcJNYIMfcjwZXBfK98d1hJRW6qOQtpaJfJNOWbtG8cl2KqKSTY3-uTRoIyontKv4-i2EORkJEqxuAMakXMVYbHw_UnhSbbz8ofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30264" target="_blank">📅 00:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30263">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=crwTqLsrXQwlSpCfVdgnCDLNwZ7dTS8iOipjxSNVdL8QyJq-S720dQVG4Te7sVcSNo6uNN15VD1mgOKm8VIiEBweA-NBwGkr2PDYDjPx4B5S-gsZax9fchSC3TjoD_Vy9GEGhxSAdKEWn8HkzIuMvPRccgxWlSl3Q3vCKQPMt6rHLjo5bFzdfgl6uYycX6tAocn1Ap4i9kKd2Sp3iBkKBji9yXcw4nu38II14vlW9stt2Q4Y_HG6ZNdcv6K6wUY-4uBgl-UgbsCL2Jyzf-mhqXWpA9Y9fBsHRAsvdolAWD9D3VrXjjKO4oRXEI5Q9XCSpqRUt65ZAQXaGQOGr2hlGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=crwTqLsrXQwlSpCfVdgnCDLNwZ7dTS8iOipjxSNVdL8QyJq-S720dQVG4Te7sVcSNo6uNN15VD1mgOKm8VIiEBweA-NBwGkr2PDYDjPx4B5S-gsZax9fchSC3TjoD_Vy9GEGhxSAdKEWn8HkzIuMvPRccgxWlSl3Q3vCKQPMt6rHLjo5bFzdfgl6uYycX6tAocn1Ap4i9kKd2Sp3iBkKBji9yXcw4nu38II14vlW9stt2Q4Y_HG6ZNdcv6K6wUY-4uBgl-UgbsCL2Jyzf-mhqXWpA9Y9fBsHRAsvdolAWD9D3VrXjjKO4oRXEI5Q9XCSpqRUt65ZAQXaGQOGr2hlGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بالاخره‌تابستون‌لعنتی با گرما مزخرفش و قطعی برق پیاپی اش تموم شد و وارد فصل دلنشین پاییز شدیم. باشد که روزگار هم روزی به کام ما بچرخد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30263" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30262">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeArt9pYK9gK8aml4KNH2W2E5T8LURxwIKwBWWilEMVfsXNXimGnW1Btsvm6Sga6Xfw7_C1WH5c_LL_PEMs6iUhMJquROBnXbW1qN2evHp-obheU1dRcCobsBvPMS5s97ODip1lsBLi48M7SAZAoz0KGnRqwnSP3cU6ANzmAusWbEx03G87ZSPeVNNfYdHkWpJ2emhkKMfEm9bz3qvDOMb68yYRlZhTCEkU8zdb9kV6iumg3X0pnvOG48Xr1eRYWtqQOgmC8A0cOU7rD1TvaupFoThfGL1YFznfuUVoapC7yizYowrI3rWGV3JCXrGSmMW29OimYywiqdRstMqjnkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
شب گذشته تیم زیر 17 سال النصر در لیگ برتر عربستان با نتیجه 2 بر 1 از سد الاهلی گذشت. هر گل النصر رو پسر کریس رونالدو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30262" target="_blank">📅 00:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30261">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqWkg1jo6CwkxTI_Vl9INB9x9YNXBfuErjFPYI9kDxuTWTrqhbqb5pJMc_kdhyg1k-163cxs01PD4YZxBzLjaWbkFc-q__hZ7c4qZ_B54EMW49WB6OpCIZO8eCOAt8YH-JHVA7Zyry9v6NeEH8tWy3D601eueZszNzrfeYSzO-MtD8ES4-0898zsc3EE7wW4Yj09NmERCAyhdVTvbNJVXUdHyeolwswjcXCihc0tqA5bC5OvrwiEJg_35hSqq5U1Dh95yT73rKjSw6cZNCi_X2uSzuS0DYeb5oU8_aEkyii4usjeZCtzg8j7t6p0bcVMcDLCJPSW1GgdEI5VRrkiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام کمیته داوران لالیگا؛ لی کانگ این ستاره کره‌ای اتلتیکو روی این صحنه خطا روی فده والورده کاپیتان تیم رئال‌مادرید بایستی اخراج میشد که داور جرات‌این‌کار رو در ورزشگاه متروپولیتانو نداشت. به احتمال فراوان مسابقه این بازی محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30261" target="_blank">📅 23:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30260">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqWWuee4pQVZG79EZjVd7ox7Z8q0M2knSp6KHl5kXtjnimeu8se5bBoR9KM2oy09PsjfDJImCu67HZuqbccbz3Eq_goMhqDzGp3y2NzCHWLdPXNdLAeDwkf7FkiWFGkSlbX9iZ8ZNl3mImROOpZ4OinpO8LuRo4FluUDW-SE0sPD_Ncr6JZ60vk2L8dse4zk1vFI7VofrHFJ40EgRuSisHRRh6fUc54drFbUZK3v6UhYidzp5v5vu7OiFkhVQQDM2Xb0sIKgngUgTFOQSgHSGX6wYqPYnhXL5PFpW82IofUZ_HT8_fTf_zBbH-8OyBVKmAIKNCSdsH2BiF2jUuM-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30260" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30259">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
چالش فوتبال دستی بین تیوی بیفوما ستاره تیم پرسپولیس با زهرا خواجوی گلر بانوان پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30259" target="_blank">📅 23:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30258">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R69BV5fdyhwWI20U-uFORHsaz1tX3VTKjbkbp1p7P5cwnHDOrjtxnx-ZMC_ga4TAtt3NzvMr6sgJu2v0lAbckx_vuOOBSSLawimxq2reczlAbcby-sV7X8dO1aAEkmu2LdR6sSn5TTbqyFAj7LdCxOrFXA50ngSLcHdykbOTDpFAez58erHt5eUW0LWtv7SSwDnJJpVhW_7xcP-bfcpV-Ao-9jSoYl0rQDm_7Vd_00fCHsCM1s5Me8s1Whk0qo0quWwEOhp2DBm2L-PiwPL2nnM1AQ4pzcLSX2v3B00X0IHqRv-96ThNJr6IuHSXDx_sj9rl6_XyXEu_LTJuEqVQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
در جذاب ترین دیدار دوستانه امروز؛ تیم منچستریونایتدِ مدل کریک مقابل شاگردان روبن آموریم در آث میلان با نتیجه چهار بر شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30258" target="_blank">📅 22:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30257">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puLHRZEicRKNqiIPAd5YJEr_OjRFl1XmFf06oRdZ95maedL_pYPiWilxFB5o9rFLQmT6oFYnDDhDy8tdwvZ_V__qJCvw6rF1_cna5bmhiQdca9Yo0vJvvwEsU0hffVPSeMjN8QPwkHRcYLu671dXB2PWFpkfFfbOAnoR2DDTFa95_kFob3AvjmVH2AvQ-nixMBfnTT2zjkAiHBsRXbhl2OrS-SytKjoPeTpaLPE-SdCV-aqsG0LjefsKQF4Hg2VZFc_Rzf4QLSB-4oplSRBbzj5ktOtGwsBGX3wm6cpCIlNr3vBTOzsirG2E7xdU9xqtcBa-jarAaXv4Rw2LAMZB1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30257" target="_blank">📅 22:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30256">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=eJ6RNHC1mRnUpNN4nF2ASaskxXahFkVKSDEiV85eKN3mGiZU1BjnMradtnM56sNvS6_i8FhJDrAMsRhlmw7poe6g0hZcsc6X0xKmnJ7c4PfgmAa5yA_VLaXjuIDtj3Elfdk_XkyHzEjnj4NcYahJPQQ0C5-b5yqWmZrQvMD3WFv0q44ivnipomqliN0FEjn8XhfLY9Lb6KWSsAN950Oq3VsDJLn8yUaAIi4caPQxiONhF1xNfNycjblVbm6s-JQG4dgc6hjq_m5xN0zlmZ9vcXJSeBrAD0OVNib3WOoNR57n4fIWmu7YOj5g6gNNJXl3T2bqa0WLLXwK4UAY4OOQgDMQg0ME4yfJ38_IFqepVL6EDrdP6xjhJqtVVHFiAiBChYLwt2ayinYKgHjEhLw7bgGqDVIJH_V7LISUBdUz31SCA5UZJNehq22v7jBKxbDbeTbU89Zp-2nZ7Rq-FzH1uzCz1HrzUkEmfXPM53OaMa3YLYu2uCkDs_vAuyfMdllxdd3paZpCJFdKXg1ylT_7xj-1Il363iTmbkPjRiRhpZbBNhXz2tb0X3jXzTU5qtcn4ReZJsOs6-QgCEHysSRzhLOKqE4cfu2vfMh2a2VFpZrg5ihEV2KB36fqKXYAZ2kXw3mBCF22ncpyZ_2-anVRgflhrc8859kdulgIklQGWIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=eJ6RNHC1mRnUpNN4nF2ASaskxXahFkVKSDEiV85eKN3mGiZU1BjnMradtnM56sNvS6_i8FhJDrAMsRhlmw7poe6g0hZcsc6X0xKmnJ7c4PfgmAa5yA_VLaXjuIDtj3Elfdk_XkyHzEjnj4NcYahJPQQ0C5-b5yqWmZrQvMD3WFv0q44ivnipomqliN0FEjn8XhfLY9Lb6KWSsAN950Oq3VsDJLn8yUaAIi4caPQxiONhF1xNfNycjblVbm6s-JQG4dgc6hjq_m5xN0zlmZ9vcXJSeBrAD0OVNib3WOoNR57n4fIWmu7YOj5g6gNNJXl3T2bqa0WLLXwK4UAY4OOQgDMQg0ME4yfJ38_IFqepVL6EDrdP6xjhJqtVVHFiAiBChYLwt2ayinYKgHjEhLw7bgGqDVIJH_V7LISUBdUz31SCA5UZJNehq22v7jBKxbDbeTbU89Zp-2nZ7Rq-FzH1uzCz1HrzUkEmfXPM53OaMa3YLYu2uCkDs_vAuyfMdllxdd3paZpCJFdKXg1ylT_7xj-1Il363iTmbkPjRiRhpZbBNhXz2tb0X3jXzTU5qtcn4ReZJsOs6-QgCEHysSRzhLOKqE4cfu2vfMh2a2VFpZrg5ihEV2KB36fqKXYAZ2kXw3mBCF22ncpyZ_2-anVRgflhrc8859kdulgIklQGWIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2011 در چنین روزی؛
وین رونی فوق‌ستاره‌انگلیسی تیم‌ منچستریونایتد این سوپر گل دیدنی و به‌ یاد موندنی رو وارد دروازه سیتی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30256" target="_blank">📅 22:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30255">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0pbtj-aLTMAletqhir_AdxSZoURceUwx2XLhB5vctpPnB3qBVdV08-AINnsHvgnz7n3Gj33aKG3dbL6wHWXnTmjJoQenutonb9C1Ko1bG2Xw7Jf_f6I8Kkj8fvbaD1qu7BBVTTZWItu9owH0uehyG_u5nE9cNmR3URqEzagOgAFpl2aMgYdUnlRdIERhk2bHVNQ_vdanHdUcZOyLp-7YpseHPvMtD1HFBDpd-4OrQE_v0UiJQuAmLCEMVW1jtfWOOa6gpeisUzjS8A7utBWBdjqfpO7PKZvEuyFohcv0Ds3un2BjSbc5YD5WHlaYk8YLq-HVGfqeApn8VGimblZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30255" target="_blank">📅 21:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30254">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVkQjKp2-wgOOmFnihP5ldPqDDe3fv9Snw9l_ZDW3rpqWrWcjxFPNUsTVGhW4eLkwEC6tyP6QRfARV_bmhxUY-CeD1VZ6reeDbSckBvvaeqr0_cgVxyKFV1TeG31oHY9e56A92yKBv024oziiuTYMmBzkcjrXjbik4aj9zW-HxBL1lOrvTFh8TLJ422LkvoAcuG4CumdimxI5qL0NrME4wqusbWUAIq8PL41BT2GKlv_4jrEFi9YuYBOsx3bPbJTeYWl_PCRDOth_T4T0ZNRwlDVaIdrjbWQmSVjOSJjOUlnvZlk8poLj_vSChhrssS1K_tO33xAcwMl2akvHa4isA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛
لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30254" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30253">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkjQlfqjzmCtThYojhLKm4pQP3KxA22kOYFTvSNC5ASkvqWmfWdB6tDd-6iv5DxZTNLJV05Bp4fq1hVbk5MQdtuWZnQ8LkP4eyliZH2Z00MlRqNfuYZEeWdu7qKSeH1oqozIo0KkB3kxcXEk_6DCqzClusTDnx9YgcYgh1qW2Irp9WBIBCXHnQc1FbUUmv-pzZBwEISNotM3EBiqRLLx3y7ed75NoToVq1fWrmNX_6ozacSxn3MWbN75YL5vP80bmSm-6h7XgMET1SqjVS0j87bUXpx9s5f4leP9LUd-pBvsHCDpJ0gSLlLA-YCXmjGKxrGYS2fdFu-Xb1vlNhxJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30253" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30252">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTJqFga6CVxsNe8y-B0B8s_g_i-ue3m82W3dCfpYt3Sxg67RmYb_e0Dhutw-7sEBa0J9-9uFTjUo3j3AmHoh1R-wvdpY4YR1-WrCshFZ7gi53-CWYBYwujzJ1X9SjA_p24mRAnKHVzmxIjeHaTg4pJ6LuoCo_0mdfnbDwjJ1bSTAjGyYFmW9mfoh5slIzFi5KEWcBG-usOtjiNOzKcHEzWMmxT0ZYaeXcBFB4Yx3rQFgetsLjVIQCSirNrHtRsblxwMGgsZ7Y36djNCK2zF0MLC1Vxh6rhSRnkAnNDCc7ZEDObljb43lyAnRBeefpyqr2snTwn7DCiCQJ_rvnDrycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ خدمت سربازی فرهان جعفری 28 آذرماه به پایان میرسه و با شروع نقل و انتقالات نیم فصل از ملوان انزلی جدا خواهد شد و راهی یکی از دو باشگاه پرسپولیس یا استقلال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30252" target="_blank">📅 20:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30251">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=r6X6KWxn-6wApK9TQNMhKMrrgGkSlaOkw5WwZ9hsrCWgDLGctdlplz3aQYU1_k0qoIXlc0wocLNDnX30ZdUvaQ_2xhWbm-917OzAe5h4Ed8n9asIWTHYlfcbP_4hB0lSUuYCY4fYNnibTl6mSghZ_Ami9hTyeXRJhM4IJdRcReDKiRpPQ7hL7nwKlwYpFqmqz7fgC6HO9z68H_666Kflw8IL1XXyMf7zlkss9ERsYYVBX77J9ef1sMJjHIrOx850iX4tVz2auatfuyxACQocIl3Y6Ia2tZ-1iSeEV7gbD3ZCykWWxWbOg4ka6fN8ScMk5BcfCG18g0W-zrP29V4y6bg6Nga0jgAVkmIa80SSgu4s_303R36oliOsGs8HTyS_F1iRSdmEMSAJUQ0VLlweljdjeJjARGSycXj2iPsGkHjFIN_Jq_LkVHCtn5kHW9tb98xvQX5DXPCEVWU0JaxSDcU_16VXOfZomp1hAjKwRjF9JXt14OKnaoXG2BRv-dFIPB9nc3jABOH8_VN2yN6Bqm-M6id7GwhUPVbVbrB9_GMyLbaemiNtsxVicU7vi21Abulp-ZY6-I8_P-etIIxwMj73miBXmyU2ChWGAGpeDwEL61TbfgGvs1PEbJ7QN3R6GU809XFGYpyLeDtAEXAnM6RlZbgOTe1NK_vlUThrXZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=r6X6KWxn-6wApK9TQNMhKMrrgGkSlaOkw5WwZ9hsrCWgDLGctdlplz3aQYU1_k0qoIXlc0wocLNDnX30ZdUvaQ_2xhWbm-917OzAe5h4Ed8n9asIWTHYlfcbP_4hB0lSUuYCY4fYNnibTl6mSghZ_Ami9hTyeXRJhM4IJdRcReDKiRpPQ7hL7nwKlwYpFqmqz7fgC6HO9z68H_666Kflw8IL1XXyMf7zlkss9ERsYYVBX77J9ef1sMJjHIrOx850iX4tVz2auatfuyxACQocIl3Y6Ia2tZ-1iSeEV7gbD3ZCykWWxWbOg4ka6fN8ScMk5BcfCG18g0W-zrP29V4y6bg6Nga0jgAVkmIa80SSgu4s_303R36oliOsGs8HTyS_F1iRSdmEMSAJUQ0VLlweljdjeJjARGSycXj2iPsGkHjFIN_Jq_LkVHCtn5kHW9tb98xvQX5DXPCEVWU0JaxSDcU_16VXOfZomp1hAjKwRjF9JXt14OKnaoXG2BRv-dFIPB9nc3jABOH8_VN2yN6Bqm-M6id7GwhUPVbVbrB9_GMyLbaemiNtsxVicU7vi21Abulp-ZY6-I8_P-etIIxwMj73miBXmyU2ChWGAGpeDwEL61TbfgGvs1PEbJ7QN3R6GU809XFGYpyLeDtAEXAnM6RlZbgOTe1NK_vlUThrXZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
هایلایتی‌از عملکردخاطره‌انگیز و فوق العاده لیونل مسی درتقابل‌خود با منچستریونایتد و کریس رونالدو در فصل 2007/08 لیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30251" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30250">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=Tsn4XfdeBWnikZDiNjO51HU-J_Ee4CzCgIFJj_ZO6e9XDJt8XAllhamrtfOvBJO9WJsnlC7drwMHcGCzdgLuBdB8hC2-c7agO2khVxp-RwVH64cfd9jimns_TxgHNZGn3QR_mgxjjqNROs_cXvQDY3U-8mlg01a4RHPnc4LasCGyUYrNIQ5LkY16GWHTuk4zXDuBgpqTzQuRtFopgNm_5hPwEAJby9zXQVkI6aFg7vLCfIcxBvT13RDu1sg3vy5bJ9_E35es4UHH1Lxp2ihmlb_nbHrdmcsH0_FjSCpHhNHDxyDrNJ908mYQIKSNJjxEUD4RbHqFJgnaPcGB6cjlHYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=Tsn4XfdeBWnikZDiNjO51HU-J_Ee4CzCgIFJj_ZO6e9XDJt8XAllhamrtfOvBJO9WJsnlC7drwMHcGCzdgLuBdB8hC2-c7agO2khVxp-RwVH64cfd9jimns_TxgHNZGn3QR_mgxjjqNROs_cXvQDY3U-8mlg01a4RHPnc4LasCGyUYrNIQ5LkY16GWHTuk4zXDuBgpqTzQuRtFopgNm_5hPwEAJby9zXQVkI6aFg7vLCfIcxBvT13RDu1sg3vy5bJ9_E35es4UHH1Lxp2ihmlb_nbHrdmcsH0_FjSCpHhNHDxyDrNJ908mYQIKSNJjxEUD4RbHqFJgnaPcGB6cjlHYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از اولین‌مصاحبه‌کریس‌رونالدو 18 ساله با زبان انگلیسی بعد از پیوستن به منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30250" target="_blank">📅 19:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30249">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWfdhgSDoBGzw7qTzbOHvlWrCdtVz0flfWswokhT7c5sM7qfwIBXd7qp-RCfiHTah-y4ByDmbJsCAarwk_xt_oi54ab_n_qyrbFCmWHNY1A1FkAFY2T4OV8eRZyNY9pG_gWS_ensI4mCnwafBJi6Bdb0uI7PWeEMgIXUn_DyL1hyliQ9jIAVXkAi11BpZpIUwLN9bzmdmLL7yLp-vKViEztarpTeuMDc8oT8MMD8YOkfybkzNcMVSGa4_0B3cNlwrYLEL76lEMMZe1dKngzKBihW4TCwwtc5egolMj9Zz7Mu_Mwtvrp1b-QMdMVDx-LhbLYG4hB9ivqlCjPxU-ghYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شیخ دیاباته آقای گل سابق لیگ برتر:
استقلال باشگاهیه که حتی آدم مرده رو به بهترین فوتبالیست تبدیل میکنه. حقیقتا من‌قبل اینکه به باشگاه استقلال بروم هیچ تیمی بدلیل مصدومیتایی که داشتم باهام قرارداد نمیبستند اما اومدم استقلال پیشرفت کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30249" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30248">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=d2zsZvTw2NMD19ecnB4LAkXRMPYUojMpZSA1O9ZuJ6ZEEmO7k1P2iuxAnxPclHVJTp7SWCyILMhic8DBBjOBCpHNm30uDnESdRmtHWEJ9r686ASUUidqTedMR6HvilzEKI91NI8q1DO0Qz_6fIl_EU_eYwCxYKCfi3lxu-FPcGPh8nLqKb92XQ89qpz46TpIwShyI8OuyVQqOLDVi0-SC412IePLsQUPBz-Gtsrbp4e1VlxjjtEmkZkIhD1e_sVFR0ZF-rWsnxDnuDJmZhBRDTO2bWwnDysO3MVfqCUvpQyJVBFUa19aNgvEQmNiIpJplCXm_AxPXrTFJsQXdT7lQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=d2zsZvTw2NMD19ecnB4LAkXRMPYUojMpZSA1O9ZuJ6ZEEmO7k1P2iuxAnxPclHVJTp7SWCyILMhic8DBBjOBCpHNm30uDnESdRmtHWEJ9r686ASUUidqTedMR6HvilzEKI91NI8q1DO0Qz_6fIl_EU_eYwCxYKCfi3lxu-FPcGPh8nLqKb92XQ89qpz46TpIwShyI8OuyVQqOLDVi0-SC412IePLsQUPBz-Gtsrbp4e1VlxjjtEmkZkIhD1e_sVFR0ZF-rWsnxDnuDJmZhBRDTO2bWwnDysO3MVfqCUvpQyJVBFUa19aNgvEQmNiIpJplCXm_AxPXrTFJsQXdT7lQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30248" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30247">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVqHhJWJH1EuiqufJ1IlYGaCuKQJ6g_uKcqLpe5pM5Gdw-fagBQE2VnFDdATgkTh20iX0qNDvaekz9e3Q2AqQyqLxnuWYcB-n1THu74IrhtrCggiplZI6Gpl1cTFtN0oo40KXHBJ4KHGLkOm1F57LOhhB4Qn7rd7_63eONEVSPvf1a17Hkmx-Kcee1TNZsRn52HztJyGV_502uzKNyJ8GPRW1Vv68QqMQb8fG7lKRep0-y2TuD-QbJkeDHL3khQ1J0P72hH5G80IpUhKrhuSrWMB6Rrhz27OskUVZXRYQ_ag4y0LFMnZIAU715duBC_8YtaUxqwH6555mSx1_2t1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30247" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30244">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sn_T9FyUyCRWMhQT7QSkU7FUw5ALKrLdbLPG9QaGepaX1ifHtS5CW0I3b-QUYC74IlK1ZI_9ikFfXI0QNP-2YMqkK_KBAtgt_FMNRhBAs-79FYgLI1XSX05LzZdotrmkXa-dTy9vPt91w9ILmCnWJ-e5jCsGdwvjybhGdzbJt_yfTfNwBN58dw8WDjY-swpa83qlzT2RtsRg9GH9OCmfJTzSwNESLq8tXCQ58niZ9xoJCuKPgktDKwcZG5JeeSw5lxUUsVQhrNhvNHP47K0P8pQ1Oo2QtR4vyGvRpdpoZlHia0myv5XRMv3WoLVvsC6ezYStMfOWD87P3w6BaiudIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCjFyjNf1XZ5_GxevCZRMzC5Mt0MRLr68GCN2grHHc91d8u7Vw4-EffxgQUONuILSLteD3TtPL-9B1GuCX6phVLrrGigpMHByydchAlJSVuknWLIUPiF12Souoa2u9LXDfWbWMYHKKHBU8BDdK4LcqZ-vYEBfXUapUSb2RUdOinMpzPnNiRuqBVctpjEDt1yRzbpbh1G02066_w9PXC7bqrsXE5P6-uLmeKHQryjKNsYNFWMz4DBUn3s9GVEW7xLBsnEhErEKCaZOlz75Z-SGUlQBYThVPQumMcsgYIrt0IL4_9mEXMQ7Oqg_jQyKDRxI_F7rhg6S-7YuKjR-nv0rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
برسی عملکرد خیره کننده خط دفاعی استقلال و خط حمله پرسپولیس در این فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30244" target="_blank">📅 18:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30243">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hToP-RZJK5UIyeKYAP5tKiF1G4Drv0-d1WfJsjWnpaN8xEqeYthwuOzs2zBKAMNLng2dNk8_D3ZXolfYd_CGda2_46zb737-ZcBUfjV0l2rSyMxSDomj_T-NfNgXG2bnxsdJKyooi-KBbYzQA75kCxhZwzbDE1uHUuUll4_p-kafEm4bGCI2qIc9e7Id0J_t2HLGMQZzrkF8reNXd9cmVN9T77cU5yDBz-6B7l35qKQ25lmw7WBM9XVOxJopKh99XeCYDBxuR6j-jDRyfT1ZI4S-0n2LhPcpbX8R_hb6QjBskb4Ls5Cng1xmn78wnNVBakx531kGGWq1faIwGwnMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30243" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNZabfvx9aZkxLKf9aaFNSbZhfTBibhy63chbOfAZxCwCZrSpqJRDt9KWZL55k9VDOdJl8e3c1YRkjdfLAx7r7L6WrDtlqi6zb-AQh09M3h9pu5wFzo6ESYXO24j9migeg3QORSmKT7EnHjeS6KpA7wujYFAMiPOyLK6-KiUNoLTGKcRByCjFk4QSoRVZ6mDzUPvAfyUJQSgepFwpA2Rie7PgeIloBsgpRxFKLM5nI0Fwa7eqYrXn0RRG51peUUp-fWDGbTLUcRvu9BjF1lkYoya2-o8eCQtVYsGSdJpTE_rJa9v7OqUl7i-ARDWub6W6DUaTiKUhju2Ja4EuyaNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه ستاره فرانسوی رئال مادرید رسما داره از تمام تکنیک‌های نامزدهای ریاست جمهوری مملکتمون استفاده می‌کنه برای کسب توپ طلا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30242" target="_blank">📅 17:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30241">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrme0Zefn6aA0KLJXsJymGeKrvGHNKZ5i4QI-0RZpK7HUsAYgI89yez8wkOvPfR-jJpvWhFr3GCmWgFxp8a6KaZZCrMR9PCF9WijO7uBCwslJFHzhOHBJygXI5ocK1tdVm0wrc-RbWIRySRA5WzGMcKsDhuPQwuhUy8yvO38xJFZKpxPWivzXBl6XSzNTkWfuKmyuyxfLSt-ko08DSRwHHnqEcdmpr_5w3n-WNIJLlKgPVEvIB1yfVTSoFMkO93PHiwG0ZPDNbTEO7oyvb2PxUo6_zY3Q2u0sfp_W0Uj2F2GBsY3NrdZlY_9PgVUOoYshfCgAeUllbpR-ooNrdt3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30241" target="_blank">📅 17:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30240">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAVQEKwSJKydqFmFOVA63L00W3szb9R12GmXADEVRqoz8oo0Cp6i3lXF44qh85fkvhiMlDa31yZPmyGQH-j5lcrNrVrQmw6sGR6B1-3F4QOJOpG4LLWEeNglk22WQL0UdkdIxYu2zylCCQTVsnq67oFoRDPYcskI0QleJXteSGt4QQ4ndgJQdrZcE-TETbY65AvlrEG_JS7urmb4r1LoOAQdDz5qTSo1JD5yyabUVg6K55Pdjd5CJK1U-_whRdqQzXaszkf1l0X5kW7JcBmwIE8rni_HfQjCDN-5Ld0fBp4awfODYfeaBwpHRmnOMOzJhZZzt_JRqJ6srq06WH4X3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌حضور دریک باشگاه در پنج لیگ معتبر اروپایی: رایان گیگز ستاره سابق منچستر در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30240" target="_blank">📅 17:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30239">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=o_i_HXk1HzXneq5oIhztpsdEKLbWqzX4pBabOFqR4wD7km5hPx2GSIj-SxrpnbTHPwO5E3eCR27Zp35xj3vIDf_VCZc4-8k3SWfcB7FpB5x9iskVgBaX26ioLOR1iockznXgWaVUDzOOqVbLl3zBxSAU3nCLQMNqYyrl7nh7fopzLyr8y24kIsHVatq5tEq6fytZx77jo7KnU7Anga-X6FDVhXkg2CEBuEuj007boL-em9dl4kwwfELiWa867XY8T5nYdrR0PRArqh5yh0anfz52PFy84coidQ6jRz6pqoF7DtYsqokwMZXl8in88KMdtJDfKY517ZgFeD6dK0ce4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=o_i_HXk1HzXneq5oIhztpsdEKLbWqzX4pBabOFqR4wD7km5hPx2GSIj-SxrpnbTHPwO5E3eCR27Zp35xj3vIDf_VCZc4-8k3SWfcB7FpB5x9iskVgBaX26ioLOR1iockznXgWaVUDzOOqVbLl3zBxSAU3nCLQMNqYyrl7nh7fopzLyr8y24kIsHVatq5tEq6fytZx77jo7KnU7Anga-X6FDVhXkg2CEBuEuj007boL-em9dl4kwwfELiWa867XY8T5nYdrR0PRArqh5yh0anfz52PFy84coidQ6jRz6pqoF7DtYsqokwMZXl8in88KMdtJDfKY517ZgFeD6dK0ce4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30239" target="_blank">📅 16:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30238">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl1SLmdBFkKce7SUTIq9OWY4vHdYiix-VPAB_yrYz2537xUXayizy6hyKWFE3HhOXY3kusZMrEAEn-fdqCGTyUU6e8lIRZspTv_9kKrXctkAChkV-GNZM_usFWK5KY6ZoYTUPmKhBoFSQP4N1p3nALbooZmxdAFr17jhN1JsnzYYLwZdMs0kFPd65NRKCe7YfvRmTDx7UgsnuerRS3STUyW1aosyjmwzTseu4fZmKDG4RSV4N8sTx77CdQZdkmIlAE3h1h8q-TgajJUlDQQTexReq4YOE-APt_jcDLJDPW4-A8GdIOroeo8th6SxeflPj5uh4_RPqgKkD_6bVVmHcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌مارکا: جانشین‌ خوزه‌مورینیو سرمربی فعلی باشگاه رئال‌‌مادرید درآینده یکی‌از دو نفر میکل آرتتا و سسک‌فابرگاس دواسطوره اسپانیا خواهدبود. این فصل خوزه مورینیو برای رئالی ها جام نیاره در پایان فصل قراردادش با کهکشانی‌ها فسخ میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30238" target="_blank">📅 16:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30237">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=tzFVZmOysZFWjHFlscMcUlufSwcPyAjmJRJS8TNBq7NyFut2n_dJWij46jUmp_P80q8_kFvbMm9UNF0yEg3uyPF44rG1v-e088_JjzabWz3ncw6nY72A_S6bhvYAK6eOP4wXEeeISGahre8jbXSChFstv7rFg6I9i70uETY-qXCs7qqfXSZdVzkyL51j7B3av4mCMmwN7ZDxczx8me5MrKZvLRKkSKVfseXpJmTw5Oql--nvQmn6rlDjdITQsoU2mCUx58oBzUmE0gt9sh_dtxqmUKVXquaTmyOU4ziptRBk4OVyYNPXE9v_2JGkdEkmRuVoWRjDr9xeyTZuZUkBWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=tzFVZmOysZFWjHFlscMcUlufSwcPyAjmJRJS8TNBq7NyFut2n_dJWij46jUmp_P80q8_kFvbMm9UNF0yEg3uyPF44rG1v-e088_JjzabWz3ncw6nY72A_S6bhvYAK6eOP4wXEeeISGahre8jbXSChFstv7rFg6I9i70uETY-qXCs7qqfXSZdVzkyL51j7B3av4mCMmwN7ZDxczx8me5MrKZvLRKkSKVfseXpJmTw5Oql--nvQmn6rlDjdITQsoU2mCUx58oBzUmE0gt9sh_dtxqmUKVXquaTmyOU4ziptRBk4OVyYNPXE9v_2JGkdEkmRuVoWRjDr9xeyTZuZUkBWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعریف و تجمید عجیب و غریب علی رضا علیزاده از نوید عاشوری بازیکن تیم گل گهر: اگه زن نمیگرفتم میاوردمش پیش خودم باهم زندگی میکردیم. عادل میگه چرا تموم مهمون های ما اینجوریهه.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30237" target="_blank">📅 15:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30236">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXYo9mEhbDqARuOFrPUAnXycIvDbL11WpomrKN_ZKs831UelPGly4DVofwGaa1dJXRaaHaiWvicKrjD3kbC9j1S8MzeliecYDiLoeHux7wwamLj5qcQhUn-W7VLTE6ijwBGN4bI56g5rEcl89XUXyQ0iYtaGxNwuDQ0HfjFvVvsxSOsFoATyTtMqcFh0LOPKhI8CnM-_EEiXW4dRDQdfzAXEwluZ1-6XdISo9TvIlOlJKkhOKf8IbjiM_jnF7MNuPLbvWbq7Zx9ZWJANxr7qFd00TQ8pRWahcVHl7ZMnqWD99eaqcxKph_sr6CU2BmUqP_cqEEt8p2DwTdrW_-oZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
درشب‌پیروزی پرگل و چهار بر صفر ترابزون اسپور مقابل گالاتاسرای؛ محمد صلاح ستاره مصری ترابزون با ثبت 3 گل و 1 پاس گل یه تنه سه امتیاز ارزشمند این دیدار رو برای تیمش به ارمغان آورد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30236" target="_blank">📅 15:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30235">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx4De-wbGDvVXGo0Q4xdF59fcgf0d6rT1VnoytyFTyeKwSgc26-Fd6eh90BuQVXp3WNP9fDibwTMVx4DhoTujUKkA112afXAxk_WimpH2MJZl-cwNPDDkwzQevBv8h2rlQxWcT_YFbW6DSZrLciaMf0itr_amrH-IDWWkpYApKrWlo91epkcj2k-gnT0Iqiz_iM3yZMWa4jSqk506LK3UmN299PbttvKNBBV8rAT0cMgXsMq2qfdwFSH8HcowucUA95joZuaoXcsEeKJBENs_AfOHFgmkgKy7ipENIkpGSTgglnJ6566-gK6OCxGyB1BXD9kplr2I-Iwbc7hASDVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30235" target="_blank">📅 14:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30234">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=JOJ5Y9h7PHvN1dEPboWdWUrZe3rZXloy6Nk2hHD9vUrkAQe2aHsZaeMrlYG_Rt4-bcblav54JMuERxJY0mPqdLsg5sqsLAYbHpxtC7Khz55bfkrt8ya0kBCSHvrqX9s08vruOuXylojZJxFAVtMnLDt2G0wukwZOYiH7sZ7Qew1IVQqwRX99wOGlUAJq7EzuHp14y5_E56t0R4G46-KpHrbdam6XpFqrCtPsDjoRoUvB0fVVX5hU5kyVy0-91Melk_RFUAWIG3g-KLqRXKvn3gK99fDqMCbwOGbD4LQ_RuspCyg7zTbFamLOGRd1_7HhaY7g3wRAgFrhiGNI6TtY8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=JOJ5Y9h7PHvN1dEPboWdWUrZe3rZXloy6Nk2hHD9vUrkAQe2aHsZaeMrlYG_Rt4-bcblav54JMuERxJY0mPqdLsg5sqsLAYbHpxtC7Khz55bfkrt8ya0kBCSHvrqX9s08vruOuXylojZJxFAVtMnLDt2G0wukwZOYiH7sZ7Qew1IVQqwRX99wOGlUAJq7EzuHp14y5_E56t0R4G46-KpHrbdam6XpFqrCtPsDjoRoUvB0fVVX5hU5kyVy0-91Melk_RFUAWIG3g-KLqRXKvn3gK99fDqMCbwOGbD4LQ_RuspCyg7zTbFamLOGRd1_7HhaY7g3wRAgFrhiGNI6TtY8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30234" target="_blank">📅 14:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30233">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6VNj_XZVK4CNR2d1_98WqmnqLM2Oa-xODd5ts029ACI4pz7QlVOdXvfnoCr-flCUHtjvgqtnPy2pSuAlPPkvnWNPdg5G6rG8T-pjXd0b1ZoQPDyAhJwPC8P5FN_iXqUykHadYHwCc7iSkVlLP7aGqBMrsl7oJrZMOsLQF9O9iZcOoPBfWDV_2LSXGKA0tRF4oVopK6w6vAP176lNghIh34uJ8Wexnu8m0A9eOZW-NTyHeD0xcZmgEs1bMzfKIAR1wffB4283eADeLvpe7g5xF8S9JI_E8X4sXVxTZ2io76Zlx7VCtdbc-H-Yk4ZKPsM-5vF13ZxtTN-R-8OI5DYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👤
#فکت
؛ آخرین بازیکنی‌که تونست تو یه فصل باپیراهن‌باشگاه‌یوونتوس 20 گل یا بیشتر بزنه کریس رونالدو بود اون این‌کار روتوی‌همه فصل‌هایی که برای یووه بازی کرد انجام داد. از وقتی هم که رفته هییچ بازیکنی دراینمدت نتونسته‌ازمرز 20 گل‌هم رد بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30233" target="_blank">📅 13:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30232">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=fWKyGg23qWAu6Xtrq0fmx9cs7SGW8hTXtMyob8FolqOXaIcybTwwxjzhCjpwfD2YLjt8YaM-rwNGMOTUaom2myp8AKB0kizaIEltPtAgxMBOL-icnyJGHlXAOREd8w6R4q3HqiTdfmP2Qfkc-5lVaBNnX-LmRdht_JeYGtMyyDvpI5vGLtRrf8H7JIf_lI6mteUOh5sSvwYpNGtHNHgXMVgiGXc6oWkJJbzJq0MG50QU3QwKbteuhuWFddfzAHM0NfcMkxEzcA_D84dQ4qOUeJkD6ztJ1jyz31OWO1avb9GIr8BY6NjoNx8-XPCo4SEczhjf7sH_YgkNpI9Uz8r_ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=fWKyGg23qWAu6Xtrq0fmx9cs7SGW8hTXtMyob8FolqOXaIcybTwwxjzhCjpwfD2YLjt8YaM-rwNGMOTUaom2myp8AKB0kizaIEltPtAgxMBOL-icnyJGHlXAOREd8w6R4q3HqiTdfmP2Qfkc-5lVaBNnX-LmRdht_JeYGtMyyDvpI5vGLtRrf8H7JIf_lI6mteUOh5sSvwYpNGtHNHgXMVgiGXc6oWkJJbzJq0MG50QU3QwKbteuhuWFddfzAHM0NfcMkxEzcA_D84dQ4qOUeJkD6ztJ1jyz31OWO1avb9GIr8BY6NjoNx8-XPCo4SEczhjf7sH_YgkNpI9Uz8r_ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30232" target="_blank">📅 13:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30231">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AP0M9ow8bdIgc4hASGagRBPKJ0sh3cwg0zwmroOJwTvB0mjK2utLLLHhXrj6OMuZRSIjhE_fBXruZAnn0r3BypdeSHPCVFoDgA0A37zMu3TdayAm8bYQFwnd4p4822KLeFtlBRRa9my8Y57y96L6iY1PzMj9rvSTrqDWDdeNCMv9QlJ3lSKcJ31JCDGgSlagVF_Bp0C_A8KVamaR28drBwk9MOe8IXXkxsajknnhtKv-wq3WrWe5ikYgg1JUcPdU8iqKbkdKH-CAY_N2_hqQugvoUkOwUmxdPZKfIcumpRRn8IIHIyOxzt3h4BLXKO16cvG1pc3sSnRXu_n3dHCZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منصور عظیمی معاون ورزشی باشگاه تراکتور که ارتباط خوبی باستاره‌های‌ایرانی و خارجی داره بعد از اختلاف بامالک‌تراکتور از این باشگاه جداشد. در طول سه سال‌اخیر عظیمی‌مسئول‌مذاکره با بازیکنان بود و مذاکرات حرفه‌ای او باعث شد که تراکتور ستاره های زیادی در طی این چند فصل جذب کنه. هر باشگاهی عظیمی رواستخدام‌کنه از همین حالا نقل و انتقالات نیم فصل اول رقابت‌های لیگ برتر رو برده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30231" target="_blank">📅 12:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30230">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOu8BCpNNPXe8YYJ_cHp-EJf_sOnpgu16kmmm2c6An73LfK6fQWQLNNA7l9HusUek4S8Ha6TxJP55q-80X8nfVD4dosKABtLrQzi_eyfRm5lD1yhaAIIXhdyzYItT6wPVrNZzTQqFniEcbn3B_1CeF1ifB5AD1FSs7yKp4muPDoNjZlcLZYMVVAB4PwBnpMqnFAnUCt1_IjISZZWJ_q1lc1kdeGk8U42lAvOaPTleSEKrw3qYJmZPcZRsVGdVqHbz_2JYaF9XmK-JVot9jIfYJ5HlPV3ldogQbAQ7mHuj_9o-qx5TqEGpPUMSmMLFv_HTIlwELT0dssFJ-IMT53V0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30230" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30228">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: توپ‌طلافوتبال به بهترین بازیکن دنیا داده میشه نه‌اینکه‌بدن به بازیکنی که فقط 80 گل‌ زده چون که برای‌گلزنی جایزه آقای گلی رو میدن. اینا خیلی‌ متفاوته! بهترین بازیکن جهان کسی هستش که وقتی به عنوان گزارشگر یا تماشاگر بازی رو بخاطرش میبینی لذت‌میبری…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30228" target="_blank">📅 11:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30227">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV0SeQau-_79FOKSM3MD7QMeQb04dkySRSSAZj8vCA_tO5GAsxaJFjUUbL63G9qiU1dxwInsle30GvS8G1wPJS3ZjjrmaxCUcq9lWRmE_Knlh3W2nOsiCvUx-Eg9b5gTUH0S5YHZBudOy428ZZ5Jq4pzUzBUHEFmd2VOqB0TmeUjQBS_lsDUVHDJR1eah7j-kbg6ujHWc8-eXOng2P_Zz9lw6Mh45o35lUFaa0OdWrYnciCO7-rgqv0g5EJ_BtJl_R0faCC2rQ9HUhQTyPZtFH9Ly-WcW7t8Gu-8ErnNpra9WD3mmf5nj807Ua-RAuD_kYcVulhoz5XxAyh6QtUOpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
مسی درتعقیب‌رکوردی تاریخی؛ لیونل مسی حالا تعدادگل‌هایش‌از روی‌ضربات ایستگاهی را به ۷۵ گل رسانده و تنها ۳ گل با مارسلینیو کاریوکا، برترین گلزن تاریخ فوتبال از روی ضربه آزاد، فاصله دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30227" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30226">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇫🇷
ویدیویی از اولین تمرین تیم ملی فرانسه بعد از جام جهانی 2026 تحت هدایت زین الدیت زیدان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30226" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30225">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=tRO_n-jdTTD87fYkqaj5Njqj_-stUCXb80wl00CcHSX7JVCVCMjo10tkZZFraDJPtkgdbWcQJinHNhPnzVJtvIgkcHhJ3y340BWj_o1lGxYOTrPs1ledF49tFyv0QL0cAGygAxNyUCq5lgYXftq7UgO7v0WZ8_0UJbfzpUAg_RE0JcdVKr0TsnVR9TDnEhfdTa8xYDGCEOW-1osDwokAEMBvPn03OnP5P0PM4kDfnpikx28VnFa92IV2i5F9Va8TNkGRi13FKIUmnztKFqSOlWzrt2VeXNJaM_aJJp8qnzeqqH2GtcOeBVuV5R6SSXmP5BF3HPREz9vr7b5YFtF2tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=tRO_n-jdTTD87fYkqaj5Njqj_-stUCXb80wl00CcHSX7JVCVCMjo10tkZZFraDJPtkgdbWcQJinHNhPnzVJtvIgkcHhJ3y340BWj_o1lGxYOTrPs1ledF49tFyv0QL0cAGygAxNyUCq5lgYXftq7UgO7v0WZ8_0UJbfzpUAg_RE0JcdVKr0TsnVR9TDnEhfdTa8xYDGCEOW-1osDwokAEMBvPn03OnP5P0PM4kDfnpikx28VnFa92IV2i5F9Va8TNkGRi13FKIUmnztKFqSOlWzrt2VeXNJaM_aJJp8qnzeqqH2GtcOeBVuV5R6SSXmP5BF3HPREz9vr7b5YFtF2tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده:
من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30225" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30223">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619db5893c.mp4?token=QJf7ivx1OOJXQ8w3DiPICTBkDDr5HC0u6albvqKIcO5qI7jhuBYD4GdnapxdZzeue2izbIcJWVmTsOZopjpvfTcNQBBRL2IOhQTlnMJr59WfflnsZ7VCJCdk8jq0Ik9bXsa1Ik2Z7IuWPEmoClO0TywhqECiX39h3NH_WIQ6GveLva_IqKfUFKeTlmcP2jpAHfuk9bANbr53pV2y54i3QALsfguYBMSD1ooW-BijhPdMgOfSSXM9fgA03tPPhhaNX890XaSZEScKZy7hyS2mA2DU99OdxHJQk5HRsLACCXm-_wIvFcnG7cTg_PBcJtn13Wyn9DAIw4q-wALwKwkhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619db5893c.mp4?token=QJf7ivx1OOJXQ8w3DiPICTBkDDr5HC0u6albvqKIcO5qI7jhuBYD4GdnapxdZzeue2izbIcJWVmTsOZopjpvfTcNQBBRL2IOhQTlnMJr59WfflnsZ7VCJCdk8jq0Ik9bXsa1Ik2Z7IuWPEmoClO0TywhqECiX39h3NH_WIQ6GveLva_IqKfUFKeTlmcP2jpAHfuk9bANbr53pV2y54i3QALsfguYBMSD1ooW-BijhPdMgOfSSXM9fgA03tPPhhaNX890XaSZEScKZy7hyS2mA2DU99OdxHJQk5HRsLACCXm-_wIvFcnG7cTg_PBcJtn13Wyn9DAIw4q-wALwKwkhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد ضیا مجری‌سابق‌صداوسیما که بعدِ اتفاقات 1401 از این سازمان اومد بیرون درباره خداداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30223" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30222">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=hmAl6ETk3aTXmWfRxS8qGsInI73nCv1mY4ovF-pa-tD4Msb7-uOx8JzafsED8DS6YjDDQVmpiGtLNmAb3T88lPbZobx30LweziKp4QKFPg0SIn5z789E6v00-_o2XlmYaAv8KWFjZpM7PXDox7mT0_ZuRC60pKoan6afu8bKRnTZN47B8dRk8b0xNIpTKy7X35FvtylvQfHWL4rLNS083AFPODD6TnVoRSgmxwVUE7lw1V-2xA6dVVvICdrO1lY-0d1WgoGZ0zsiTACtf77TMbxH5jK6mrjefpoNDIwjeFwIVQjJ9V-Kp6PRv_FmvOu_42tLgobfZhevAgKSjPwAKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=hmAl6ETk3aTXmWfRxS8qGsInI73nCv1mY4ovF-pa-tD4Msb7-uOx8JzafsED8DS6YjDDQVmpiGtLNmAb3T88lPbZobx30LweziKp4QKFPg0SIn5z789E6v00-_o2XlmYaAv8KWFjZpM7PXDox7mT0_ZuRC60pKoan6afu8bKRnTZN47B8dRk8b0xNIpTKy7X35FvtylvQfHWL4rLNS083AFPODD6TnVoRSgmxwVUE7lw1V-2xA6dVVvICdrO1lY-0d1WgoGZ0zsiTACtf77TMbxH5jK6mrjefpoNDIwjeFwIVQjJ9V-Kp6PRv_FmvOu_42tLgobfZhevAgKSjPwAKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس‌سنگین‌ابوطالب به خدادادعزیزی در قسمت اول برنامه جدیدش: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30222" target="_blank">📅 10:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30221">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8hFv94x1Gp0vr3jARENUE5CaysLBUnIB38IWp6MutgHpXifCT0o75yZswYLm3F25ODhhE-HR7smf5IjG49uh8-yFVsLOPd5xsarorpr3IIX8hOo_Ol_jlhRSoUL9UJFYaIoSoqdJIfFigAogBaA9eWyHS8aJm_N9BDsyWMO6Lv2Y2UuZqtUb6AzcUNQIVlStjnDpIYwsf-53oguCCSNkk8Q4wRLAs7DBQ1mDHdsZ9ke3gui8uB3fdpyiYL9JEAI3QHYhCpRXGuAjlRSsLs8KM3Fp7z2vauuW1b2AUtsH9o0o6j-fShAIvnWkK17BujpnXSgBU3QJuoi-wdWhKeqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از علیرضا بیرانوند در روزهای آینده در سالن تتو کارها. این‌بشر شده کل بدنش رو تتو میکنه مثل بدن امیر تتلو تا بالاخره معافیت رو بگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30221" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30220">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTFip044aFFO4x79G5op9MY23Tt4Jm9g4d4ywIBXF99cGt-qkawYpDR3fDPc5MbXJXqog7LnPl5q0OOiIUh4Rc_Q6gD-j7-6HjzrLJFr9gAUlSGsgF5Pp7dEyf4sx8RqQeZN0258VcJTnX3pn-N2wzS73cTup4dF6JdYk0diEzKNQUqsj5uMGu-koSnuTqycQkiQrHSxjKO2v483pCeMKU9p4hKWJjG6gyFtFdpPwuSByFG432k34Uk-rpEVTL2Ds0IHZZyRrZY3x3a6Xu4ktpT8CxFQXf65HE-tdqHzphKaFpw64UHww3A9G6EbGYKBATlan4zj5sPQUNoF7H_85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری مدیربرنامه‌های یاسر آسانی در تایید خبر ظهرامروزپرشیانا: همیشه به‌آبی وفادار خواهیم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30220" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30219">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=JPDOyB7CZJzePJjSaKD2_ujjXn-IQXB-9eNJ6nmOjpgrvCGnJddwnb9jwhChHMaZ0pySa3fLwN_wulzUhSXynYr1Si8UChO3a8uBLRFMKaq93YkMpetWgG_wSQTcgZHm6XIKggVh-rGCdSHXSFKWccaq8gxF6UhxXuZunG9H_TU01sdqy_empnJLxpUFr-c6BSnB3QhD-_RrWHsNSOhAGHUCvmlRkgkT1vsCwVJLQbPb1x6T_bF4Cb1BerVYE_zdbHAm6ne7wqkP01sJoKtMdX1OxpcvEeNaEzotPizhwe5m5zn5vPgWXEM49VoMyyILXRo_C94nqzlUdfIhOe_Zyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=JPDOyB7CZJzePJjSaKD2_ujjXn-IQXB-9eNJ6nmOjpgrvCGnJddwnb9jwhChHMaZ0pySa3fLwN_wulzUhSXynYr1Si8UChO3a8uBLRFMKaq93YkMpetWgG_wSQTcgZHm6XIKggVh-rGCdSHXSFKWccaq8gxF6UhxXuZunG9H_TU01sdqy_empnJLxpUFr-c6BSnB3QhD-_RrWHsNSOhAGHUCvmlRkgkT1vsCwVJLQbPb1x6T_bF4Cb1BerVYE_zdbHAm6ne7wqkP01sJoKtMdX1OxpcvEeNaEzotPizhwe5m5zn5vPgWXEM49VoMyyILXRo_C94nqzlUdfIhOe_Zyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی‌هوش‌مصنوعی‌از قهرمان فصل گذشته لیگ برتر؛ رقابت بین دو تیم تراکتور
🆚
استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/30219" target="_blank">📅 01:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30218">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnqkYpvXebAV6BxePm-KC6ryJSThBB6NCSmpGl4JrAiL2PJTfQjOxYtMyXt-cz3qM67I1QxWtJ6GHblJnFE4QE8bKsG-Xr8pa7UCyIzGxcPyHcVCyY_s9b7rrAeQAJ_MWbprEJB72PY3_qTTlLreltskryS9schJHakMEUxZ9JW4qOdsFcLQg-Lqa8DcyT4nGZ_qS7rIzjpqikDTXuDusk13HkubQpO4ItaIOoD-SdPE9PbtTi1OLcrWQ_bUMIBsjXP0WcQALYqw_JULZMyaOK_9F5lfLBVDo3iJffQfqDFaASHMP70fr8_sjFm_uqY21IilcjuDXQnU4e8BzZOrNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/30218" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
