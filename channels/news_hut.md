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
<img src="https://cdn4.telesco.pe/file/v86Oc6utbMeeY0UQf6ZixNb1XZ5qEeJoSvUnyi_2q889zebKEI5GeWFesJ5Tn0PNL1Zu8wMPsqOsCbj4Q5zHcPRE9JN7igugiS6-GgPzE9-dqnIKbXU-7wUHoGol2WjLWabd0uys01_5AyyhV_4MVNjv4xoBYWLujSJooPlb3z2uvHrJlLeSIoR_IeidmoBTYgNFTeaedtQLnptNy5Qya12DCn6U06EJ8fivA5g9WZC3YArLl0IX7O6bbsIyu9x59X5OyciGB4CmgiVgcvvAbjZ0pVlqxMzBEP4HbU8FfJ3VppybWlrNjAUIQbQ4jYXxCLiqyefi1Ffcsh1Xe5KbRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 15:07:03</div>
<hr>

<div class="tg-post" id="msg-71359">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkMRUfCZ0NjpH3ZHmpJcesmPf4lzqkGaGmB_kUMuzYBXT8NvmmPccQJl91Rj2JzAca89OoCvWhTcRtfLL6TyIVDrhjGZUZtvBDOiS1HdXc3lKPWBDuBJFIX-fEg7uFGhe4x2s8-OJ9Tn94aXyxgI3txEpwtVJ6I0hTCAO0YMmTPWlkKE34CUEuDGyPr7aM2gK4e9lHx-5S9sOaYqkTrTWR434YwSULc2mMBHGfGnH9kX5qoMLHOKGVGbLJnlcLzrPPMt_P3RCAoktrId7amkiTFKBXBxb5L_xCqQG0Kjjk9tEMS5nAckcdYySoZzsAFunOZVf8UlEaOo5uHUmKjbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
🇺🇸
#فوری
؛سخنگوی سپاه پاسداران شروط جدیدی را برای پایان دادن به جنگ مطرح کرد؛
🔴
اگر دشمن خواهان پایان این وضعیت است؛
۱_ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد
۲_ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند
۳_محاصرهٔ یمن پایان یابد
۴_۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۵_از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@News_Hut</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/news_hut/71359" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71358">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=sj7q-8T-H8ImwmqpYqZAlD32Q2ALTSFdrKFHOM8WUJZjzHKEQdXFS8Ok53ySHWn8X4OaC7FSGqtjlhshvgB0lpd5oCRQrUFbqUbOuBVnzD4VD2X4uWahxw-Jj_UazU6mlTsdq-G4F-6sqaJrT-q_3V4M6fWsjH8l61Pj5yXvJo-YyvdLZNvR8EktzMG5sW-M5eFQHzQS2Tj7fR_jTbz7OguNm-omXByAbthpAUGGOwdrVfkNRSU5IMAVtEaV97h61a2vIYtFHC-ItMFKIMVcyPFUkZUA0xWt1TxrKoFQxrIuHIn3L4gfx5JL4-fQwuWdTW8KfdANlmeKh44PZJ2YNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=sj7q-8T-H8ImwmqpYqZAlD32Q2ALTSFdrKFHOM8WUJZjzHKEQdXFS8Ok53ySHWn8X4OaC7FSGqtjlhshvgB0lpd5oCRQrUFbqUbOuBVnzD4VD2X4uWahxw-Jj_UazU6mlTsdq-G4F-6sqaJrT-q_3V4M6fWsjH8l61Pj5yXvJo-YyvdLZNvR8EktzMG5sW-M5eFQHzQS2Tj7fR_jTbz7OguNm-omXByAbthpAUGGOwdrVfkNRSU5IMAVtEaV97h61a2vIYtFHC-ItMFKIMVcyPFUkZUA0xWt1TxrKoFQxrIuHIn3L4gfx5JL4-fQwuWdTW8KfdANlmeKh44PZJ2YNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
یک فایل صوتی که اختصاصی به ایران اینترنشنال رسیده است، نشان می‌دهد یک هواپیمای نظامی آمریکا در مکالمات رادیویی به نفتکش جمهوری اسلامی هشدار داده به‌دلیل «رعایت نکردن محاصره نظامی» در بنادر و سواحل ایران، موتورخانه آن را هدف می‌گیرد و خدمه باید در ۱۰ دقیقه موتورخانه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/news_hut/71358" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71357">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcr65FOwbCxhzQVRrAcmP_0IOd8HTk5KfWwe7ohcHFZDiBib5ehqzNlhSqZCgc25jgex4iFVuIvgZlLonv_nNSqrSElD38AwCESofdqZE0n_pwTmPZJrWS3so3Y0Gv9e01BpQrdHwrSpv_lhCSEsZCvwjHet9KDHWbMwtt828YyJcMlA7hb3G6KUkUEfVcYng9UmY-YPuP4T6G8IY_B2yQk4tS0IimHESO6iRknIFzmIWtZrBu2xO6bhxIvOsDCuUGmP8xv9oBhTLv2lqHgM5u26MLPhjUPBPHy-DP2EZSD4QcSfJg78wdZ0LIMqL4TVtHEvd9j9nExWsUUlAKyUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع حادثه‌ای در ۲۸ مایل دریایی جنوب شرقی «الفاو» در عراق دریافت کرد.
فرمانده یک نفتکش گزارش داد که این شناور مورد اصابت پرتابه‌ای با منشأ نامعلوم قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/news_hut/71357" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71356">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSdfg8Qu9dSXOwWqX3AVZfo3crxjIvhn8afjoW_l7uHJuBn4daj1c82xef_d7D8YVjew5v5qnAAfMliK4Rqez9LD--slCQKajxMtruSbffem_sIPIdQv8VsDdJNw-uywpR2vStjuoXPZHugmNLEYv60MtwKsUmzNQooi1PenjrPXiNoVZ6pcvonQ71b2cJDiKFDvJaB3EoPaTqxosshXUtbBp1CnQ1LOKeAs1ddB_HjZbDd8BpH4WgBSgxglmMatDkqZuTChs70BU9Bb_X8LLRFPKuBZTCLrYyTDwJwQ0FbhjXqLJMzhxlOSeOMTr2G8pZ7YSQCqtFCz2WDqjv3oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
🫵
دقایقی پیش دلار و تتر به شکل عجیبی تا 241,000 تومن بالا رفت و دوباره برگشت و الان 234,000 تومن هستش...
@News_Hut</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/news_hut/71356" target="_blank">📅 13:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71355">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7Lh59d7Su-5iqq_Feit-_dCQvSkzY7IT02pGP10ww20yzjefM6qb68RP3yHh9B4cISbb7rGNpBJnWU7j2s2c4jkPD_bIMyOeIdbWCtit9xjVOgU8yoTNnMCcbNMYUrQI1fSHXIClPm8WD5MxFW-lT-0ilRfSuy6xW4l_M_DWVkltxeeOwGYiwe5vmmGZelJdGfi-VhDWzp6i9HjFwK1LxWwZCGqYyA1aVEYL_Gywl8Vj3BOi-S2RUcTHRg0uSaF34_xk4b4p2Ae1ylr62izOMtGE-z0AU28_3PYOV9V3gHQoJVMakclsub-S0Bn0nD7UYH4s4nwVE-eqB2xU4s6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که به دو ناوشکن نیروی دریایی ایالات متحده در خاورمیانه حمله کرده‌اند. این ادعا کاملاً نادرست است.
✔️
واقعیت: هیچ‌یک از شناورهای جنگی نیروی دریایی ایالات متحده مورد اصابت قرار نگرفته‌اند؛ تمام تلاش‌های سپاه برای انجام حمله با شکست مواجه شده است.
در همین حال، نیروهای آمریکایی تنها در هفته گذشته موفق به انهدام ۱۰ نفتکش ایرانی شده‌اند. این شناورها بخشی از یک شبکه پنهانِ چند میلیارد دلاری بودند که بودجه سپاه را تأمین می‌کند و ایران قادر به محافظت از آن‌ها نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/news_hut/71355" target="_blank">📅 13:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71354">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=X2SAkz7F-lUPBnmgNFqMc_vXLW-lfoBN-N2JUtmrG-We3zXX77ru80SSZkRK5zyDQt5DsByjxlos0vspRDilgjnvXRn8El_vrzlviQF_zNXm2o83KXElNbvDHsSv54-tMPpmwUsLolpLFBIYmT2ZiGvJ17cidY7b6SDgZURua6wztIbUxqRIdh5R8ZoMEo26FVRAektYcarnyyNaND2Hh4m4EhMkLxVFw1O1hlQw__H36rEBlkVv9VzoFe5N1BdLvRH8XdsLKHcg0mRZvR70CyigeA5zDps1gqijjxhcQO-AL-HnfL894Xl1NBjFxFXw_9D-ioZzLWUGmT4HWND4vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=X2SAkz7F-lUPBnmgNFqMc_vXLW-lfoBN-N2JUtmrG-We3zXX77ru80SSZkRK5zyDQt5DsByjxlos0vspRDilgjnvXRn8El_vrzlviQF_zNXm2o83KXElNbvDHsSv54-tMPpmwUsLolpLFBIYmT2ZiGvJ17cidY7b6SDgZURua6wztIbUxqRIdh5R8ZoMEo26FVRAektYcarnyyNaND2Hh4m4EhMkLxVFw1O1hlQw__H36rEBlkVv9VzoFe5N1BdLvRH8XdsLKHcg0mRZvR70CyigeA5zDps1gqijjxhcQO-AL-HnfL894Xl1NBjFxFXw_9D-ioZzLWUGmT4HWND4vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
پرسنل نظامی جمهوری اسلامی:
رفتم یه شونه تخم‌مرغ رو گرفتم با یک کیلو میوه شده یه میلیون تومن. حالا نمی‌دونم بیست‌وشش و خورده‌ای هم دریافتیمه.
مثلاً بیست هفت هشت تومن سر ماه به ماه میدن به ما. مردم چکار کنن؟ خب دیگه یارو میاد بیرون حق داره اعتراض کنه دیگه. به جز این که اصلاً راهی نیست. بعد هزاری انگ هم می‌چسبونن که آقا یارو تروریسته، فلانه، بسانه.
مرد حسابی مردم گرسنه‌اند. خودتو زدی به اون راه. من با این لباس دیگه قشنگ با این لباس نیروی انتظامی ناراضیم. وای به حال مردم. یعنی قشنگ میری بیرون خشم و نفرتو تو چهره مردم می‌بینی.
می‌خوان جرت بدن منتها نمیتونن. یعنی همین الان میری بیرون اصن یه جوری‌ان نگاه نفرت‌انگیزشون نسبت به این لباس قشنگ معلومه.
حالا یه عده خودشونو به خواب خیال زدن. بابا دیگه خجالت بکشین. بی‌شرفی یه حدی داره. مثلاً انقدر. شما دیگه رسیدین به اون سقف. یه کم خجالت بکشین. یعنی اصلاً من نیروی ناراضی‌ام. وای به حال مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/71354" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71353">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jciHwHbu0mjZ1DU61jWT25o0fPAdkqbbXtUJyMcaAzNEGvss-fpWpCGOztBfWhDAoqQQ1e4KpDvEhl2Xrg6tkt8LWvYa8UW-lxjteDs25OZxyphMeD2NldqKHFcwqjtejSHchZ8NcBnOtoMpnQgdoHylvHXicEQa_VTZWY3wVDhlGPEQ8-vRtKeDEEmxk8TWLzLvM8FD8VlaUmZCTncq3FypIiUsXgSfqBAo-LicBxI17DHwMu_EttpKx4nv-X75xFvYVwbIW7mrlmwSNANfNcsk72kztiiNiDDoudnhC-_tWu99HlYfU6mM-pYWdGhP1u06o3PcPvqUxwoy9oIXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی از یک طرف ثالث درباره وقوع حادثه‌ای در فاصله ۲۴ مایل دریایی شمال غربی بندر راشد در امارات متحده عربی دریافت کرده است.
فرمانده یک نفتکش گزارش داده است که شناوری را در وضعیت مایل (کج‌شدگی) در حالت لنگر‌اندازی مشاهده کرده است؛ وضعیتی که احتمالاً نشان‌دهنده ورود آب به داخل شناور در پی اصابت پرتابه‌ای ناشناس است.
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/71353" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71352">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71352" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/news_hut/71352" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71351">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QonBR4P7GQXmXbedtdRwnFl11-KTBpv0k0fxaOYta_FdzQFtU0G0G47ljNC-wWps5Ng0EdGPZf4cEMB0HXATG89hCEWphyxhmPtL9SZqv4MVcJ6WDrReRp4I7VqRYpi3J-4G7bvepeR1Jdgp7zs-9I9Ksoi9v5XK3rx3epGCJyGT_6PyPd93Lq_s7IZ231rIW74haUbSUIHFrJm_9fYxltsLbIyx1kowfiZ2LGRfBM4VEnHMAjz0WL1Zi19pNndPYRKIA5GE3Vs4500GYHsSvX6jlGW8iDqrLorG01MEcoOTcrhz4iFxATwr_AieXFpL2C8RGX_eXcJwekQwwGVvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
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
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/news_hut/71351" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71350">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5Ady4c7H3JQbgOZ_Kk_WptbtRepiRj2bOnixZSoyPtdcOJZXDpbzEVNAYA-Y9StHrTGfrGpL2z3ScWrB1Rdh0YRMZ1f7clKtfueSgJeSDgifvPNoAe4s39Muc8YyYkiIt6JDPqJGAdrpHJNOpuKkiAXAHkdRdP5tWb6zPmxEhkp6E5YcSrA5LI5zvhoR3mzcMA4uJxEFVIg96w3q8iPahlgbNqv3lt6r4gyHSP1IO2dC0w9kEi-z2HUUxOrvmA-_mhjgrtPo1izASTo_otX-647PVnDGiC74c52Sraz7YIiPeqpep6uFKhN1AJSzgROK8WavIWHl6BU6mL2F09HwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📈
قیمت نفت خام برنت برای نخستین بار از ماه ژوئیه، به بالای ۱۰۰ دلار در هر بشکه جهش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/71350" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71348">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkjZALUia6ZUowUskeP6uhHjD1bRqg5sPwwMKkVS1UcjXLEU9CWPV_TrKt2dDLyaa2Y-R99-wqC1Vm1qU26rLfpYKfmHLmS0uLfVsJ71bczNrYnxzdBGPUdf1NmygPudj_HVUfz4X8Zn1KDzovtO4m03z38X_BNFdGFVYbY-mDIyzRYp7dzmkFwf9Mx-aw21qQqdfyHZNXfjypBjs8QbqeZwLc1AA2souHtQlSl-DFuLPLN7lz2AZ6D75DbgcGV1JYQeefWryM30QfbIHecCjq6CbhJ5gqkZzKOAYgqfM-LrvYgDYmNBvL7DRG2lyXXgRMWOtXp_NQ5LTR_4zwIsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=BqakshGfk6PwR24r41352a5UeMj_2Fe3udGo_Tc1UlNluer4G8BHWQqY9HgiYOh50WwDZHHPyDy1bK6sGNct5zdOgK5b6KDhh9aJM8Ln942jZaIYAS8JPv_rkpeA6m9XtULfRX59USMzO_ywXol8BxVEDzZx5dWkm_0ol99AS9gvsDZLf_VAIqKLVJn9rOu63rHXe5NtJv3fUyrrrG8YAxPQdcab1BEgMVVGHhiRpW06GdDXwdjLbiyu5loZ8h0vLtYPiszmA9J_vKBjWDsXLLOfYfITSQmE4YnPFSQ08NfWsanEEGGs2PZiChx_wyEwRP5djdb2iFzvhKYvBa2CrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=BqakshGfk6PwR24r41352a5UeMj_2Fe3udGo_Tc1UlNluer4G8BHWQqY9HgiYOh50WwDZHHPyDy1bK6sGNct5zdOgK5b6KDhh9aJM8Ln942jZaIYAS8JPv_rkpeA6m9XtULfRX59USMzO_ywXol8BxVEDzZx5dWkm_0ol99AS9gvsDZLf_VAIqKLVJn9rOu63rHXe5NtJv3fUyrrrG8YAxPQdcab1BEgMVVGHhiRpW06GdDXwdjLbiyu5loZ8h0vLtYPiszmA9J_vKBjWDsXLLOfYfITSQmE4YnPFSQ08NfWsanEEGGs2PZiChx_wyEwRP5djdb2iFzvhKYvBa2CrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دختر یکی از پشم ریزون ترین خودکشی هارو داشته:
دو روز پیش "پایال دِوی" داشت اولین فتوشاتشو برای یک مجله تو حرفه‌ی مدلینگش انجام میداد که یهو وسط عکس برداری تصمیم میگیره بی دلیل خودش رو تو رودخونه پرت کنه.
ویدیوش خیلی عجیبه و بعضیا میگن امکان نداره این خودکشی بوده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/71348" target="_blank">📅 12:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71347">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032667483d.mp4?token=lbs7VbOW4vvuhFa-aNprfcITrtTUlATZ6DKFSpy_LnWbCRVywTPvt7ogU73dLsWfjV8n3UZDCpZVx83Id44aB-m9YUcxdT4Vwf0ZWBdnPxaz1Ni1GvBZFtd8ZYou7HUg76goy85b6Khz1iT0m9KaSNZrcKvqHsKJIovSDuggLxafKZ1Kwmoa1GoxxxCj3joMRZNeAxl2z-F9S6ZHLfpDEv88K97G15sEK3OSAV32kNk_PyQSQ6I-yGXJHdUqh8NAAzWSopqyiXDLmFK2IH4yiqb2gNv4D1gyq0WW7o7KIqyBFysol8o2o39dgVowBI8fk60GSZEqN3it1yvfUVECLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032667483d.mp4?token=lbs7VbOW4vvuhFa-aNprfcITrtTUlATZ6DKFSpy_LnWbCRVywTPvt7ogU73dLsWfjV8n3UZDCpZVx83Id44aB-m9YUcxdT4Vwf0ZWBdnPxaz1Ni1GvBZFtd8ZYou7HUg76goy85b6Khz1iT0m9KaSNZrcKvqHsKJIovSDuggLxafKZ1Kwmoa1GoxxxCj3joMRZNeAxl2z-F9S6ZHLfpDEv88K97G15sEK3OSAV32kNk_PyQSQ6I-yGXJHdUqh8NAAzWSopqyiXDLmFK2IH4yiqb2gNv4D1gyq0WW7o7KIqyBFysol8o2o39dgVowBI8fk60GSZEqN3it1yvfUVECLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا طبق فتوای جدید حضور نداشتن تو اجتماعات شبانه، غضب الهی رو در پی خواهد داشت و تو زندگیتون ذلت و خواری میاره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71347" target="_blank">📅 11:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71346">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-ETe9uWeO25ltn2U0Gv9iGS9GEGb7gg6YzX0PTo_ZC7AlI8e22nbiyL4APt_vyt1zQ6eLFIIB8FJ1PH-J46QQ_WVdss7sNJSIacRAJaFUwqXe4PScrWB989lcwDmEeUC5Yj62D5kjIqG90SY88eNFawz_MrCKC-jJRr_V3EHeSoPkEvem0Vzf3v4RUrEfIJ_Wt3MaNopX-eJMIOT8PMWRMUoPzaVz7SKQLgSFehp9FtvrNLj6pKx9-eH6Ngq_WJ-WfknX9bd7pp0QKCGCpd7DeXmft2VT-0Fr98r4YeUL9UgpAU1iFMU6QegmEQUD0BvcEpoZ3dqgT99qOTlMEVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
دوازده کشور با صدور بیانیه‌ای مشترک، ممنوعیت‌های ملی تجارت کالا از شهرک‌های غیرقانونی اسرائیل را اعلام کردند؛
🇫🇷
فرانسه
🇬🇧
بریتانیا
🇨🇦
کانادا
🇩🇰
دانمارک
🇪🇸
اسپانیا
🇫🇮
فنلاند
🇮🇪
ایرلند
🇮🇸
ایسلند
🇳🇴
نروژ
🇵🇱
لهستان
🇵🇹
پرتغال
🇸🇪
سوئد
مکرون، نخست وزیر بریتانیا برنهام، و نخست وزیر کانادا، کارنی، توافق کردند که وضعیت با خشونت «بی‌سابقه» شهرک‌نشینان و گسترش شهرک‌سازی رو به وخامت است و به طور خاص پروژه E1 را «غیرقابل قبول» خواندند.
آنها از اقداماتی که قبلاً توسط ایرلند، اسپانیا، هلند، نروژ و بلژیک انجام شده است، تقدیر می‌کنند.
این بیانیه از اسرائیل می‌خواهد که فوراً گسترش شهرک‌سازی را متوقف کند، شهرک‌نشینان خشونت‌طلب را پاسخگو قرار دهد و اتهامات علیه نیروهای اسرائیلی را بررسی کند.
آنها «قاطعانه با هرگونه اقدامی که منجر به الحاق سرزمین‌های فلسطینی یا آوارگی اجباری شود، مخالفند.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71346" target="_blank">📅 11:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71345">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf294068.mp4?token=Q5ioMJBhHuLuxjcO9zYqRjhkE4Hc05Anajp7AvLdVvZgKrxu3ulHhFX5GB0A_MuaZrHGaVeIYYcOfEYtyAPsBBKt9rqDA66w2fjUXexOmLoB37NBb1qgSg-A4672Bmxfd36S8Laua83H1MvPTSfMt9pSdzje-wJIqbgiIzGLN1zzOU82OYyCIzJgtUErF3eOcCp54j93fHXkdMJvi1RLjmKrhQaaslo1O8xRw_vkmvThnAXDDAmKg2A9bJ-Jjdm73cIDQUfPry5pEsshgKTzXewwMWyJVCJyZrmaxjhedR8HkNROHddiab45wEiZqjJC7ks_cTS5_r2AlDHv7_Ti9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf294068.mp4?token=Q5ioMJBhHuLuxjcO9zYqRjhkE4Hc05Anajp7AvLdVvZgKrxu3ulHhFX5GB0A_MuaZrHGaVeIYYcOfEYtyAPsBBKt9rqDA66w2fjUXexOmLoB37NBb1qgSg-A4672Bmxfd36S8Laua83H1MvPTSfMt9pSdzje-wJIqbgiIzGLN1zzOU82OYyCIzJgtUErF3eOcCp54j93fHXkdMJvi1RLjmKrhQaaslo1O8xRw_vkmvThnAXDDAmKg2A9bJ-Jjdm73cIDQUfPry5pEsshgKTzXewwMWyJVCJyZrmaxjhedR8HkNROHddiab45wEiZqjJC7ks_cTS5_r2AlDHv7_Ti9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
سنتکام:
کشتی «ریسکو» (M/T Riesco) در تاریخ ۸ سپتامبر در خلیج عمان غرق شد؛ این کشتی پس از تلاش سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی ایالات متحده، توسط نیروهای سنتکام (CENTCOM) منهدم شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71345" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71344">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=NZ3slh4goNvydExL3JFAB7U3DiX63UpHA9I1umIS-utSOTj_-Bipo0o4RCKVWb1HGKBsN3k2uwwZf00hNO76nRtCI5ps1F5NcAJfMQdcveAi6-rQsMT5ABNa6l-I8gkkAqiETiZNkjvgcjhgoA0WDsJO48zUm24wCGZY1xIKg6-l52JZ8zgumySRuXqFElDMT9knZPXCflXjOqCXzVl8yoZIGzCLFZwV7IocpjtVGVdpxnhLjAkV1KJvk9bhucYHEZuyR3CIKfWD2UGMv8hJIBoX9YJRkJYayqzzRI67rO148V52CDVZF8kPTo9MlG72OvwJqYhVongO1Th4IhIKfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=NZ3slh4goNvydExL3JFAB7U3DiX63UpHA9I1umIS-utSOTj_-Bipo0o4RCKVWb1HGKBsN3k2uwwZf00hNO76nRtCI5ps1F5NcAJfMQdcveAi6-rQsMT5ABNa6l-I8gkkAqiETiZNkjvgcjhgoA0WDsJO48zUm24wCGZY1xIKg6-l52JZ8zgumySRuXqFElDMT9knZPXCflXjOqCXzVl8yoZIGzCLFZwV7IocpjtVGVdpxnhLjAkV1KJvk9bhucYHEZuyR3CIKfWD2UGMv8hJIBoX9YJRkJYayqzzRI67rO148V52CDVZF8kPTo9MlG72OvwJqYhVongO1Th4IhIKfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
مهران رجبی:
اونی که نمیاد تجمعات باید بهش بگی فازت چیه که نمیای ؟
این وظیفه ملی و دینی ماست و باید بیایم کف خیابون
ضرر نداره بیایم و شما کاری میکنید که کفار ناراحت میشه پس بیاید
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71344" target="_blank">📅 10:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71343">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=FhLZ-Za7PJhsQxfq0Bd9-yfxRMjOkO41vDtyKyq-Ekky_2CqCinKzR9CfQEEbA6k-MGxEz0l6utDswOKuk0jwBSV8RM-G-4AK_KnPcHcUt2DteYnXRL_kqvWpeimrHj8K1h4KUUrTqpCK06mOCpCy6wPMwuOtSRw46z1ixoGWDSBt3CqResrB9ZJIZrW1KKQhFb7ujCwlp6iAhwmw0cXZBXDbG60kbUvETgSZrsda87lv6wfjx0XpYhbNppwTKQ5grhKW2y-FRCV0bnFsToTksY1oSV5JoxBq0DE5Pol4eexL4mAGwx8LsILaUbX88d87zNtWRK1p9bzU7HZRnwfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=FhLZ-Za7PJhsQxfq0Bd9-yfxRMjOkO41vDtyKyq-Ekky_2CqCinKzR9CfQEEbA6k-MGxEz0l6utDswOKuk0jwBSV8RM-G-4AK_KnPcHcUt2DteYnXRL_kqvWpeimrHj8K1h4KUUrTqpCK06mOCpCy6wPMwuOtSRw46z1ixoGWDSBt3CqResrB9ZJIZrW1KKQhFb7ujCwlp6iAhwmw0cXZBXDbG60kbUvETgSZrsda87lv6wfjx0XpYhbNppwTKQ5grhKW2y-FRCV0bnFsToTksY1oSV5JoxBq0DE5Pol4eexL4mAGwx8LsILaUbX88d87zNtWRK1p9bzU7HZRnwfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از طویله مجلس
😳
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71343" target="_blank">📅 09:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71338">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gv1YBgJMLhclOyuDsz55CcaK8wf1-eYffpnFeT2zMmaKyNd3hKzTO45qQGe6TgAxJi9H8gNsN2_7NHtSQNxSIZRmMYwAZ0wRqwx8DQql0_9GwSUyUVgwUENAYNyhP0O9KgoX8RASqecnWpIwf_sL1IoIb8rbZftpmmez2TVc_RFaEcXjhsjKy2bsSVe3ZfJLNcAZjsvut--KWBhbyL2tcsn2OBn4pwJ3Np0oLxxF6yBmgdGbfTCzGcLZ4veAdi3dMf1c9eKLRmDbtn1FvCRWM9bZFMoGEK9_ZwgIJn_VsGAe4QGZ2hF4jd9gn-ukLPb-XG4jhtLpv2AGbGZAl_WSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAwdnF1jCz_irJnnd5sqEp6xLYHISEoSV7p-WBoKZEYju4PBpZ2f959_byegN9YHe0Orq6BkUMU_Y5BFGZHrJ0T11aEXtw9vESgVuBTuyuK2BkM_8dPEiohu7zolGo_msbFZD76_BIFvtRPQtTQ_po6Nbhe3JfXI1_4PvOnAfFfTF6C_E7HM-BgdYBbqQAtv9u3U6Gqx2J970UE0acdDOLtVcW6a0LKEMPRKK4Pe0qttlmvZBJWlRXOW6rKigeZatyCVG-BCf5WZEfSqsh4MqRpQfhSsYofF4Ho83007Ac_e_ULpVWZzN4j1FtREkQYl5y7FY1O2YopICqnYGUmS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fh-M2SGW_r9Nm7pvyYGc-pXxeU9IYw2U5HlWqSEZeYSbWvJfJVVqpaQNzL4bgOnk9UETXrTjQzUqbLH2sd4dLgkq0W60aNRlx0jFn9LkPvv7waVdvK5lE3lIw27PG95ZaKNR2ldtH59oHMnKxTX9Jm4Bz1kehewkEDIVKiTTqKKTqlJ1ZdYl_2NaShv-TBGaABz0rHcLQPTs057869yEikH-jUyAIEpeh4zffUTBEBXbeN2lE9dEPY83oAt1AgLAQnOKMd4JK_GMQOnuBJCNHu09JZQROxNQeMBDSzcT2PN31zV2e2N1RqkBn97qakRmyGSuqHPZB1dOKLp-fwct7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUy470p1p-UNKk1d4YDy5Cu8gRwcLSwJagMpliJANavHFcpDNDh6QKxZHvIjzecz26WZ_rYMiaH0YD8BWJUSmh_bdCx8ju259CwceivxfDVPv5Admb1RddO8KxyrlHoC-N8EnUzoJWjHtAA35tDt1hXeRWm0BPog-XpwrzVpPEkV0TcgYBCMVMjQ1AQAIFn1WMrkOMWvoLq5PeIl_weU9fPJIc0OPpw-CE1_YD0Pf39lJ8YgouMEJfALPxxUZrAzigCendBu1V0bk8DQkcFqQF4miSYJeqDHA7QT_9041LCbnWWX31mIEbEsYneIv1My7-ErXDnsRIql1gPeFOFU0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzvCsm2kq9jBWh3Mh0TGPrnPmrrISRYpszN2I3pl1-yUdgI6Hegjr23zX2Cqvfm6guGQaBuYqdoTlS9G3GUYNNKOxzcLjIdtL6AVj8O1ndDVr8DU5fSgH2kHuqsvRIXzOTexLcTnc8UqjbLrBeTOc7XMQhQDMzy9Mv_zYYWhGFg1B6MW7V0eeYF1vHuvUjVzKmlEP6bofVahXteUX4aZxGr0O2ARvVSqB8gq8gFh4gEAiSYjf-YpBqhpouLMFNx9XE6vOaEzK8ROxOdDY_VngmrxdywwNkHNW1GRtSiVnYmoKY9K23s6FOaVjImx6_KGyyTTkMr3q6I4jPcAYgEelg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه پاسداران تصاویری از زیردریایی‌ بدون سرنشین آمریکایی که به عنوان غنیمت گرفته منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71338" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71337">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71337" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71336">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy50Hoa68qEdZP_QneeoJXMdNCyr0Sa-hp01vyxxySdO8eK4c9D020V8sdxeZFyyC2g7im4oybiafMfXaISuxDTKYZMXx0URGnrvV3bYWime4Wf1Jr-d7UFYdPfPO0Dm5h4hs_APcLnG1R-cQPh9b4iK9kdOi31kc-KAPIGncKp2RT9_4hWCWFQM86CNmAWl57yanVYLhstt5hFtDnmGTU-FTx4oUjDnntRS-99nNHpDHQUgtt0TyND14jX6bcfMgsMNAQ0zfBRFn-f3s6mLfk1UxLQvaKwId15iuwYHvuZ2itlJAX5Ue9sjGgV1sXJGYVGcFnFEWdDbohIa0Y4JtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71336" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71335">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
〰️
#فوری
؛سنتکام:
نیروهای سنتکام در تاریخ ۸ سپتامبر پنج شناور حمل نفت خام ایران را منهدم کردند؛ این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی طی دو روز گذشته، دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد.
کشتی جنگی آمریکا با موفقیت از حملات تلاش‌شدۀ ایران گریخت و به گشت‌زنی در آب‌های منطقه ادامه داد.
هیچ‌یک از پرسنل آمریکایی آسیب ندیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71335" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71332">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
📰
خبرنگار العربیه:
چندین موشک ایرانی در جنوب سوریه رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71332" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71331">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=qNNcWRQRHn7V3RHwZtuHm6dWcwvWuL-gjL9XMmn3vQlvWkw09yhszzuhP87n38dGPKOyFvRyFUL1Pg5UxNpevCvOMgS1hr5c0mDg6l1GmU-ISVhzQwVUdTjKOxrU3n-Ipntx-UN__I3fFsy42dq3nFAiK2oHFQd9mp94fDxCyokZA02ncNbGVar7HOTexds8EMnxpX8kJv2T63RUkDCDeQo6vnMYGXTvVTV0CleFOLOb6H9d-mt7a0GtPoKh_Qkf_dmHGXdqOLb0MBIq6SVNNKrlyJ-Nsg07Y4u_1Uwvhnh7mUleNBI3Y9xCFc2__zcUBLkSH-ZqbrphxtHa0hcL_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=qNNcWRQRHn7V3RHwZtuHm6dWcwvWuL-gjL9XMmn3vQlvWkw09yhszzuhP87n38dGPKOyFvRyFUL1Pg5UxNpevCvOMgS1hr5c0mDg6l1GmU-ISVhzQwVUdTjKOxrU3n-Ipntx-UN__I3fFsy42dq3nFAiK2oHFQd9mp94fDxCyokZA02ncNbGVar7HOTexds8EMnxpX8kJv2T63RUkDCDeQo6vnMYGXTvVTV0CleFOLOb6H9d-mt7a0GtPoKh_Qkf_dmHGXdqOLb0MBIq6SVNNKrlyJ-Nsg07Y4u_1Uwvhnh7mUleNBI3Y9xCFc2__zcUBLkSH-ZqbrphxtHa0hcL_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمون اردن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71331" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71330">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=rt2KFLTHWEGNb_aBOgCm6swzoieX_6nEOUsSq_tIx_PiKidMeQmhPUS47C8l6xdkLhhVLaKL9wxKuxBR12z7QZRAr3QAl2qKqZagLRsc7BFCT4ozz_s58FSw6x9Ls1aZTJUDQjMhBAijOE-e3GyngyiEGbOCRZDTOxhJgq-Z9qnxM8t5kTG2htugIsH2gdFMJYyKOUKJJkAd0HApaMKfoyIPj6YLr8_tKWTbOGKsnCrAHLPj0roOC_qNtmuOC1U2672cZNj4S1q_0uQh8d8Ny3_79m78RIS8aQ7WG9ti-dhisCjBrpMPmTPGMgJS-LZuH-brQybc2v-w06Ps9qgcIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=rt2KFLTHWEGNb_aBOgCm6swzoieX_6nEOUsSq_tIx_PiKidMeQmhPUS47C8l6xdkLhhVLaKL9wxKuxBR12z7QZRAr3QAl2qKqZagLRsc7BFCT4ozz_s58FSw6x9Ls1aZTJUDQjMhBAijOE-e3GyngyiEGbOCRZDTOxhJgq-Z9qnxM8t5kTG2htugIsH2gdFMJYyKOUKJJkAd0HApaMKfoyIPj6YLr8_tKWTbOGKsnCrAHLPj0roOC_qNtmuOC1U2672cZNj4S1q_0uQh8d8Ny3_79m78RIS8aQ7WG9ti-dhisCjBrpMPmTPGMgJS-LZuH-brQybc2v-w06Ps9qgcIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
مهمات خوشه ای سپاه در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71330" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71329">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇮🇷
نایا به نقل ازمنبع ایرانی:
سپاه پاسداران انقلاب اسلامی، دقایقی پیش، موشک‌های خیبرشکن را مورد استفاده قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71329" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71328">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=NOPo2E40b42cEkQu7sv_7lkN2-oC2-fqP9IYobUVcnlhS1zE1AIib6fcWhncYPC5DvBcKoiyon1tM8eMFYOp1FMfixSzUS2xp4Aj9aWQQJqslQ-uNY29t4rtUmFZfKzrmt-pyuL7PnsJOX6Ur9AVRSrPLtIyL_HwR0E_eAI3ylg3CGYTY3sJ5-djskBnuvDMJYDPGVv41PYzYpMCQvw4kq-1CVt3ihRPYhFiH6dOb3YO-NTNl724p1EHgvMkWU6aOsWm1eJy0QnhSLdtaCXArSJlNszi0JiJvyHZMjPhUls9zyxd4PuOd-75UpiE2_g5ocHe9fR6Jsbv1l4eiHNzeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=NOPo2E40b42cEkQu7sv_7lkN2-oC2-fqP9IYobUVcnlhS1zE1AIib6fcWhncYPC5DvBcKoiyon1tM8eMFYOp1FMfixSzUS2xp4Aj9aWQQJqslQ-uNY29t4rtUmFZfKzrmt-pyuL7PnsJOX6Ur9AVRSrPLtIyL_HwR0E_eAI3ylg3CGYTY3sJ5-djskBnuvDMJYDPGVv41PYzYpMCQvw4kq-1CVt3ihRPYhFiH6dOb3YO-NTNl724p1EHgvMkWU6aOsWm1eJy0QnhSLdtaCXArSJlNszi0JiJvyHZMjPhUls9zyxd4PuOd-75UpiE2_g5ocHe9fR6Jsbv1l4eiHNzeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گویا سپاه توی حملات امشبش از موشک خوشه ای استفاده کرده
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71328" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71327">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f211389571.mp4?token=FVi3lfRP2oyQD8b0IZ0qQBhsojI2sTvOyFEcBL1eAeW-6564-P950kfTOZOUqWwddJmn5lAhldCU1gvPGcSciayX61hG2YNCduA2v9wAzFxM7qP5FSX1JgEu91jQmJrxv2oydM8PdDr1xB1iL0iUvIKSHj4mg7YYNRl2IXu_Uzet11mXHKRo-gn_pBUe2zerDd9IY1EV2hqfhrIwyz8kpvx00yCDIJJ0tTxh2L3OooB_jkZDN5S0AdW0EPgDUTnisusy9-x2jxv83gLDaQExUCttYXP_aiVjAdXLqU0bFSuABFRpEE7HGMyDZt0PbWMxbqC914-TIGHF-ahYOcNTXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f211389571.mp4?token=FVi3lfRP2oyQD8b0IZ0qQBhsojI2sTvOyFEcBL1eAeW-6564-P950kfTOZOUqWwddJmn5lAhldCU1gvPGcSciayX61hG2YNCduA2v9wAzFxM7qP5FSX1JgEu91jQmJrxv2oydM8PdDr1xB1iL0iUvIKSHj4mg7YYNRl2IXu_Uzet11mXHKRo-gn_pBUe2zerDd9IY1EV2hqfhrIwyz8kpvx00yCDIJJ0tTxh2L3OooB_jkZDN5S0AdW0EPgDUTnisusy9-x2jxv83gLDaQExUCttYXP_aiVjAdXLqU0bFSuABFRpEE7HGMyDZt0PbWMxbqC914-TIGHF-ahYOcNTXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت شدید پدافند در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71327" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71326">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
از اکثر نقاط کشور به سمت پایگاه های آمریکا موشک شلیک کردن
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71326" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71325">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=g-UI6zzYOFK_ZM-Pbie_9AkJF3G4BbOxm-9Kff2XhKuJin1pVk8bSm0YfGWMvdyG6F8y_oPZNUR5cJviy1LmuwnusJbbLuEKmT87HCvG6kZzQcqdvQFlYh2QCvNi1gvujbgWE-fbqAj3nFdMVbtiyT6L2tGfmfngy8vuSU9M8CyegPW15cHBHNT_WYU4TH9C29FTrARvbKdFzdw_43GK-hyQncIJ9j9gu0w2_PMiBDZqjn8xYCoVAD17F6N7rJ5OmGbBP00bhXrAZFAnAMNZIZgKsUuqvivPLsmSpcADF-7NDL2pu9nCMJ17KeTNH0wA6Ym28RyWcCZCrS-cubrW5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=g-UI6zzYOFK_ZM-Pbie_9AkJF3G4BbOxm-9Kff2XhKuJin1pVk8bSm0YfGWMvdyG6F8y_oPZNUR5cJviy1LmuwnusJbbLuEKmT87HCvG6kZzQcqdvQFlYh2QCvNi1gvujbgWE-fbqAj3nFdMVbtiyT6L2tGfmfngy8vuSU9M8CyegPW15cHBHNT_WYU4TH9C29FTrARvbKdFzdw_43GK-hyQncIJ9j9gu0w2_PMiBDZqjn8xYCoVAD17F6N7rJ5OmGbBP00bhXrAZFAnAMNZIZgKsUuqvivPLsmSpcADF-7NDL2pu9nCMJ17KeTNH0wA6Ym28RyWcCZCrS-cubrW5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موشک ها در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71325" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71324">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ارسالی از اصفهان:
از نجف آباد دوتا موشک از اصفهان ۴ تا
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71324" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71323">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=ICRuvu2qkKT162ZrPAUcwxMHLyHDkumJRMZ9VkIJ_1kyAySa622O-NTjLAsqPwwUw7TmeBNR5VsNALqIr7MlCSqkVk9JzLF9ff-1y3fZjWRm5gOGhbb7XzlSt-HttVesFZ_AcVP9Uokl2Na6PhkwmcPVShE1FCAII7RrZkf_f-aDhsyJXYrTGpg6b4S_mGBTfcefG_DRYrhzFrWtqX8Bp5q_H77NhDN1fnOji5ZUBAnIdfvigV5WNg7Gu1SZXw6sbnEdZgDqfUqdMM_sxZ0vv_pxMO6cC_vuZCf2s_8-LyeeeAqdh_JG9ua9BGt_4qqPFy9mTMLXEj32dIp2eW4fkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=ICRuvu2qkKT162ZrPAUcwxMHLyHDkumJRMZ9VkIJ_1kyAySa622O-NTjLAsqPwwUw7TmeBNR5VsNALqIr7MlCSqkVk9JzLF9ff-1y3fZjWRm5gOGhbb7XzlSt-HttVesFZ_AcVP9Uokl2Na6PhkwmcPVShE1FCAII7RrZkf_f-aDhsyJXYrTGpg6b4S_mGBTfcefG_DRYrhzFrWtqX8Bp5q_H77NhDN1fnOji5ZUBAnIdfvigV5WNg7Gu1SZXw6sbnEdZgDqfUqdMM_sxZ0vv_pxMO6cC_vuZCf2s_8-LyeeeAqdh_JG9ua9BGt_4qqPFy9mTMLXEj32dIp2eW4fkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71323" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71322">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
گزارش ارسالی:
از زنجانم موشک زدن همین ۱۰ دقیقه پیش
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71322" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71321">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQSvfYlKp1tc04iok6QeyjJnWzKuBt4OQL5ipuImXABSuJTk_c-H7xlWCbdOhb5gkXDT4MrDEoasaKhyF0vp-S8KJQi58YgDYqDIQtBR3wUkoOvu2tSIR3UJuVFa8Pn_aVfW7ZLFvm8qEhR3ouMqjza_8gxfqSiL9XSGNiUkpcvTHU3bN2akO2xtaMnFZDQ69jEqKDS6EtHOKU_eX3n_tRvq_rYp7NbKGWr3RvrB4PFHPZVgeTTYbUjvI79nRg7I7B6fZOgrXVDyMJnmBog3ga6QDko9bGGZgnhJ5Csg8OHy7k7z--R7a3ZRdtIO1n9_nPTSg_BFDSv31r-wAuYDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارسالی از نجف‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71321" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71320">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc98612785.mp4?token=h2IthuViUvJOItp_eNedaSCLRvh9aMnXF4kSU4ScAjp3wxtZfSQFvydpQ1TRRpm1qmN9sdu8HzGSdLGtHTHjh0BS-Aztr5qMk-EVntMZhpTgJR5guRSu-ni-I4jcFwuGFCwOrliqcb91Z12ZYcWQvq-Nk60tZgxY1dJDqWi_vqRAJOaYyNxvchXWO3wuhmWYMQWU2qYEfo6g3dyYv22PjIOEEhunlNZie9B6hVp4KUpI28ZRSyKTfht0TPYapMxndWzBE9Rz-cdKSFDjpF_Bu4eRb8XMdBLWsJNupoBJL_-obntH2lv2oSXrRpB4azmAOgbI1Bc9TjZVG6eQqVGMXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc98612785.mp4?token=h2IthuViUvJOItp_eNedaSCLRvh9aMnXF4kSU4ScAjp3wxtZfSQFvydpQ1TRRpm1qmN9sdu8HzGSdLGtHTHjh0BS-Aztr5qMk-EVntMZhpTgJR5guRSu-ni-I4jcFwuGFCwOrliqcb91Z12ZYcWQvq-Nk60tZgxY1dJDqWi_vqRAJOaYyNxvchXWO3wuhmWYMQWU2qYEfo6g3dyYv22PjIOEEhunlNZie9B6hVp4KUpI28ZRSyKTfht0TPYapMxndWzBE9Rz-cdKSFDjpF_Bu4eRb8XMdBLWsJNupoBJL_-obntH2lv2oSXrRpB4azmAOgbI1Bc9TjZVG6eQqVGMXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارسالی از اصفهان:
حداقل چهار/پنج موشک دیده میشه توی آسمون
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71320" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71319">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c50434db49.mp4?token=ZpD36_IOnrWGJ30PvbKlgsE_4wahepFFvGQII7onTLDa3H8JmGdhDHOb9NEyr9ldmE9Ry7ppJvBbPzEUZgYR2m9qZZTAL2TwQIK6muYbgXN3CJmi0ePUUH4KuOBm1dMcJ0POQJivsxe-EbJt1hjCHC-Ldp8N2b568_cNqDvX8izT8aGv5nPfu1DrKYNNONk3MglUxlSLtMhXkIDsH1-_NnLb26m6AbT04vcVRT_YLq8ucRdP2r9O4aZnhziyuE-CxkMZDy8D2h08YhFWIKjOyUUFAaCRIQ_4gyha-Hm16L2ijzRf7X5RzYLtHBV5cVKGRm5xjfNZQZdoVv0Ge8pgGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c50434db49.mp4?token=ZpD36_IOnrWGJ30PvbKlgsE_4wahepFFvGQII7onTLDa3H8JmGdhDHOb9NEyr9ldmE9Ry7ppJvBbPzEUZgYR2m9qZZTAL2TwQIK6muYbgXN3CJmi0ePUUH4KuOBm1dMcJ0POQJivsxe-EbJt1hjCHC-Ldp8N2b568_cNqDvX8izT8aGv5nPfu1DrKYNNONk3MglUxlSLtMhXkIDsH1-_NnLb26m6AbT04vcVRT_YLq8ucRdP2r9O4aZnhziyuE-CxkMZDy8D2h08YhFWIKjOyUUFAaCRIQ_4gyha-Hm16L2ijzRf7X5RzYLtHBV5cVKGRm5xjfNZQZdoVv0Ge8pgGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ارسالی:
همین الان از دماوند موشک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71319" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71318">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
ارسالی از تبریز:
همین الان از تبریز موشک زدن
سایت موشکی امند
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71318" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71317">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
چندین گزارش از خرم‌آباد اومد که صدای انفجار شنیدن./احتمالا پرتاب موشک
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71317" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71316">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ارسالی از بروجرد:
سلام بروجرد هم فرستاد
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71316" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71315">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
گزارش ارسالی از اصفهان:
هفت تیر مبارکه اصفهان موشک بلند شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71315" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71314">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJS8TkO1z1Us7nUf1N5v0MEVRph5DWKlKG_wo9vRCqcJ6BoOhMbTDLM7LrLAAgjT78-vaR53Lf8MwS_zjAgD0Ok4_ykuexDtPuFFvlYkXl-X7mt7_BxRiD5JdoDUOt3OlIOwv3RurFUHnNFIb8sehIyBN0BFXklI7Tzz-zgVUAmWACMB1g6c0pnXN9biJpPn3YZi7mVfb-r98MWBzv5N-5kVgkVExK5YIq3VyX68mkEeIkK-ERDpnlLuhGvcNQbeNUnvZndkbYRGKFtmBGZVy4w-vI9Sqn-4sjIjIa-6lshVL8CwJFahYLMNcJWPMC9-ORj6FNrbpFdEeCjD2NO3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71314" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71313">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارش ارسالی از یزد:
از یزدم موشک زدن همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71313" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71312">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
گزارش از اصفهان:
اصفهان الان زدن موشک نمیدونم شهر رضا بود یا نجف اباد
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71312" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71311">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
گزارش ممبرا:
۱۵ خرداد اصفهان شلیک ۲ تا موشک همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71311" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71310">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛صداوسیما:
دقایقی قبل نیروهای آمریکایی به یک فروند شناور تجاری در آب‌های ساحلی شهرستان جاسک حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71310" target="_blank">📅 00:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71309">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LREZcyBSe-2M9z8nVA6dtFV3LmDi_6jc_HbQBWCUsd6iv5ru-OR1tP-VtGHfmWIXJ83DFSHsGarUK0L5zfIjVaDRKb69365Au0BwlvUdUWr4Vk9FcYZshByNw-8QRgfOqQ6JiU0EjyC3LDAiAphkMUZUNluaRPVO56hiYjkWwehbS-jz_dFrSz3gu37rVhOHXB-1qsmanPHkAUcS7qsR3mr5OieST6qAT75sNAgoORPDW1_1vGfLLh5hH1nG6fqotrKXidBaKCwn5XB7Ka4XsVVfgN1pSNPoUtwKSWnnIUOrf6h2dtUb95HrY0-fpVwVArFHdv--wVxBz7S84ImTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:ایران ظرف سه روز، دومین موج حملات موشکی را علیه کشتی‌های نیروی دریایی آمریکا انجام داد، اما هیچ‌یک از شناورهای آمریکایی هدف قرار نگرفتند.
این حملات موجب نگرانی واشنگتن شده است، زیرا به نظر می‌رسد ایران از موشک‌های پیشرفته‌تری استفاده می‌کند که قادر به هدف قرار دادن کشتی‌های در حال حرکت هستند.
مقامات آمریکایی همچنین در حال بررسی این موضوع هستند که آیا چین یا روسیه ممکن است در شناسایی موقعیت ناوهای جنگی آمریکا به ایران کمک کنند یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71309" target="_blank">📅 00:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71308">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tT9G5EODA4jPGbzme6hIdYpseARtT6_-sn93ciaUliDF7jFIwZ_AJxDXTSVshb-dQ4Xpep-Ujzh8elT-4qQI3qzPi6Gj5ynVhtXXPwU_-H7yOmnN6M7CBFY1LWkyywtQ-0Bys-053YVcrlqv1FJlcmYRhncWo_Snq5HFtmEEQHrsT_O0DDNStgw21mRbUsci5S9iRxq5v1SatgnPi74eOn3p261AdiuAV3vLhaY8FOYVWHrTs3o1CsNVsP3y60kfQKqWUViQQKGpBlQ_qTKaBbRvTpoLUFjAJvVKwgaj2GlWbDEaTdRbyy5V62kc_VtrrLI2kC8Y9MUGz3OCV7G4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
به تمامی خدمه نفت‌کش‌ها در بنادر و لنگرگاه‌های کویت و بحرین هشدار می‌دهیم که فوراً شناورهای خود را ترک کنند، زیرا این شناورها هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71308" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71307">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geq3I5_4Nyre5KSG9BjJZVoAyN4hAuJkw3O3XQe8aRIoPNQvM4Aufv6F52Xlvm9kCBQAgESnP3LVOYzgO3L6S5z9BoACX7BEqSqZ2lRY4gCEb9Hud1FBvUNNmNI0BwL6guAdK2LS6GEkebzDrjahcv0tYsdUwv5MHGKupiMGrcLyCt_9GVoekrpfgcFfD4MZ0K3QpMYCbxmJ2jDl__FDLnOKU80OPH5WvoPI146i0i0jDcE_bE5IsH0HZixyr4vSenZMoWjg-Ay8DKA6_3ZG8Fhp-VTjSJ30beRLs1RzIxQHsB5i3-ljHYNxS5ACbl4OfSbo5h1hlbO5XuG6Fa81tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
مصطفی نجف زاده:
آمریکا با هدف قرار دادن نفتکش‌ها در سواحل ایران و مشخصا خارک، علاوه بر اینکه می‌خواهد بازدارندگی معتبر در برابر رویکرد تهاجمی اخیر ایران در حمله به ناوگان دریایی آمریکا ایجاد کند، ممکن است گام تازه‌ای در راهبرد محاصره نیز باشد که براساس آن، قصد دارد حلقه فشار را از مسیرهای انتقال نفت به مبدأ حرکت نفتکش‌ها منتقل کند و صادرات انرژی ایران را از نقطه آغاز با اختلال جدی مواجه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71307" target="_blank">📅 23:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71306">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
📰
فاکس نیوز:
امشب
برای سربازان امریکا دعا کنید
نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز
ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی حرف‌ها* می‌زند
امشب برای نیروهای آمریکایی در منطقه دعا کنید
و برای خانواده‌هایشان که بدون شک نگران پسران، دختران، شوهران و همسرانشان خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71306" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71305">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=uqnLRsyvYg2C4pHzH0Rq_EvdmHQlsnQC7dqIuUvnh6DrNgdmkYzWESPiNc9aY0s4PcXUCGePGlb6awzOD90VINIZFs000Gi9AEPLpHY8ECyF9rs1eQvndHN9brIalGTQVtJhwX73IohKZydARUJhhJLD5W-Nl2I4gJmRT1VP-eKswHS5v1yiOsaCTmc14J9OfF35FM-BNBX8G08AiT5XkiS0gJV9IVJBxq75VsFZ9def0lvHB3aRp-L-4IlOopvKAzGiCsAHgulvd0tbhnqZQpLwNmxjpJAiggw1qzT26JN5jBT3ERw-jRfewEwZT0P1oKRPVdNpnj-nRtyJ7X_2VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=uqnLRsyvYg2C4pHzH0Rq_EvdmHQlsnQC7dqIuUvnh6DrNgdmkYzWESPiNc9aY0s4PcXUCGePGlb6awzOD90VINIZFs000Gi9AEPLpHY8ECyF9rs1eQvndHN9brIalGTQVtJhwX73IohKZydARUJhhJLD5W-Nl2I4gJmRT1VP-eKswHS5v1yiOsaCTmc14J9OfF35FM-BNBX8G08AiT5XkiS0gJV9IVJBxq75VsFZ9def0lvHB3aRp-L-4IlOopvKAzGiCsAHgulvd0tbhnqZQpLwNmxjpJAiggw1qzT26JN5jBT3ERw-jRfewEwZT0P1oKRPVdNpnj-nRtyJ7X_2VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این فیلم‌ لحظه‌ای را نشان می‌دهند که هواپیمای باربری آمازون در روز یکشنبه در فرودگاه بین‌المللی میامی از باند فرود خارج شد و متاسفانه ۵ نفر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71305" target="_blank">📅 23:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71304">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=EVk7RTDYYlXBk1KASoV8onMX7-1_ZTVMTkYVzGsMMCaZWtKfjuB8hj6qIzjqdxOggHPS4FW1fjG2zJyUVTcHqlrhyOIR9FG4clOsRohHWOn5zuRHPvAYF_MJC8AOntT6f5jEG8PQbHm0NNT0KwhYxYEnk7Hvown87GG-OSCy_cDXmdhVkEpWeMstqqiSbERcUukBfwGdfCNzmigbh-DtiViN4_ah0afHXnF93r4wV8q4Uwbkm0soaVUmiDycerbwYxy21tSdMTig6KftFiQk2JTQFNI1VnBrax2dqlE-UgpSFH8dsIVBjj6vo-L_8CHWxR71NcahQ8oJSYfNN_x-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=EVk7RTDYYlXBk1KASoV8onMX7-1_ZTVMTkYVzGsMMCaZWtKfjuB8hj6qIzjqdxOggHPS4FW1fjG2zJyUVTcHqlrhyOIR9FG4clOsRohHWOn5zuRHPvAYF_MJC8AOntT6f5jEG8PQbHm0NNT0KwhYxYEnk7Hvown87GG-OSCy_cDXmdhVkEpWeMstqqiSbERcUukBfwGdfCNzmigbh-DtiViN4_ah0afHXnF93r4wV8q4Uwbkm0soaVUmiDycerbwYxy21tSdMTig6KftFiQk2JTQFNI1VnBrax2dqlE-UgpSFH8dsIVBjj6vo-L_8CHWxR71NcahQ8oJSYfNN_x-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آیت‌الله بی‌بی‌سی از لندن فرمودن بنزین(۱۰ هزار تومنی) در ایران تقریبا مجانیه. این دقیقا عین جمله‌ایه که آیت الله بی‌بی‌سی برای مردم ایران پخش کرد!
تا حالا شده بی‌بی‌سی فارسی حقوق کارگران در ایران رو هم به دلار حساب کنه و نتیجه بگیره مجانی کار می کنن؟!
یا تورم رو حساب کنه و مقایسش  کنه با حقوق کارگر؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71304" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71303">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=ulbme5hQNAv13C0Wp0wwxEPGNHBYI66SUXcib42eoT5ITgas0WkHvY4cKLItLiLH2-DHwPu4OB8g_oUMYYdYJjRU6ak1IeB3Wm3zfkzCMhpHdFdEfYjR4D0eqfIkZXR0pXS3IFDNZaZbzAXpNFRWI9LOjTY5NWbO8IvOSyKgQSfdixYx1LX6qU8mWc3Ekes_QiEEcwocznhLY7B0lPYGZe1ruGNPur0HJdUOtBsZcDG6UA3zEU6I_TUK3h260SYWHsANhZeUmWO_eITR2hjgJ_txiuhHnaXMdeY2pZVPHtb3PJGC9fu5OkcHUQ4TiwYGWo90Xcqn0gPNMqGqC2eO3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=ulbme5hQNAv13C0Wp0wwxEPGNHBYI66SUXcib42eoT5ITgas0WkHvY4cKLItLiLH2-DHwPu4OB8g_oUMYYdYJjRU6ak1IeB3Wm3zfkzCMhpHdFdEfYjR4D0eqfIkZXR0pXS3IFDNZaZbzAXpNFRWI9LOjTY5NWbO8IvOSyKgQSfdixYx1LX6qU8mWc3Ekes_QiEEcwocznhLY7B0lPYGZe1ruGNPur0HJdUOtBsZcDG6UA3zEU6I_TUK3h260SYWHsANhZeUmWO_eITR2hjgJ_txiuhHnaXMdeY2pZVPHtb3PJGC9fu5OkcHUQ4TiwYGWo90Xcqn0gPNMqGqC2eO3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این روزا تور مدیتیشن و استراحت مد شده و طرفدارای زیادی داره
:
اونایی که مشکل روحی روانی دارن میرن درخت بغل میکنن و گریه میکنن
یا با حشرات توی جنگل و حیواناش اینا حرف میزنن حرف میزنن حالشون خوب میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71303" target="_blank">📅 22:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71302">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=sRSN7H9oLiVWHUewir7iqqkNvcJqwaqz0xW_sndKlqQqPgpGTg_kwTd1pXUR4xeLqXuinBhlCONEKXOeLcOTmost_Ji7GhCLDIILKGKsfn4kAlzI_e_2Nj5SInIJBkyHX4X94q1UzUd-MnYkG9NlsXFxmHixs3R-u4ju7RoWIXdRvcoE8AB_d_kBr9b2R_-p-vQiRF_zD8tBOvsdQ72GNcW3wQlaJcwlG6uihZpOBhuJ5_UoTbubYBweMUlELjeWa1O1LjfbPJGyxeWtD8twELEM1m765X1SfmghKjE2XasBsur1OYKlpsH2plLvOZWxkf1GmH_Lz224VQoz8c2prA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=sRSN7H9oLiVWHUewir7iqqkNvcJqwaqz0xW_sndKlqQqPgpGTg_kwTd1pXUR4xeLqXuinBhlCONEKXOeLcOTmost_Ji7GhCLDIILKGKsfn4kAlzI_e_2Nj5SInIJBkyHX4X94q1UzUd-MnYkG9NlsXFxmHixs3R-u4ju7RoWIXdRvcoE8AB_d_kBr9b2R_-p-vQiRF_zD8tBOvsdQ72GNcW3wQlaJcwlG6uihZpOBhuJ5_UoTbubYBweMUlELjeWa1O1LjfbPJGyxeWtD8twELEM1m765X1SfmghKjE2XasBsur1OYKlpsH2plLvOZWxkf1GmH_Lz224VQoz8c2prA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
زمانی که بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود.
گاهی مارهای سمی زیادی در حیاط پیدا می‌شد.
وقتی سر مار را قطع می‌کردید، مار می‌مرد، اما خودش نمی‌دانست که مرده است؛ بنابراین باید مراقب می‌بودید، چون سرِ جداشده هنوز می‌توانست شما را نیش بزند و دُم مار هم ممکن بود تا زمان غروب خورشید تکان بخورد.
اما وقتی خورشید غروب می‌کرد و هوا خنک می‌شد، تکان خوردن دُم هم متوقف می‌شد.
🔴
حالا مار ایرانی — یعنی همان رهبری — هم هنوز نمی‌داند که مرده است، اما در واقع مرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71302" target="_blank">📅 21:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71301">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=ZFzvSvKXPZZtLj0YOnB_1qxOTQNbQfH2gVNQybojGBoNMaprQQrCt39vUbXiP9Y_S2I83Dtsy56h1GBsm1RB1QyFrWUemW_WmNtUbKm_5QKy2zYY5ysMYfd-3J2WVTHmN4NnxV-q8-VCfCjjm8FHjSfEVbrNcRB1Zv2MlhH7akCrLHXlF8249373KLJVcDFUte-eCb-iMGK2LDC5fYBfoPO_lwdWElbrUnHpE_3aPRqCWt4aEN7w2ZLYCYl68GdN-74O5qpw_DH8hY_FwfTwbmZ9hwgd_SKN-AJNaSBZx51aFB8El19yRntrNvYS0Kx3tDSJUkLM_Iogx6gYt_-8bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=ZFzvSvKXPZZtLj0YOnB_1qxOTQNbQfH2gVNQybojGBoNMaprQQrCt39vUbXiP9Y_S2I83Dtsy56h1GBsm1RB1QyFrWUemW_WmNtUbKm_5QKy2zYY5ysMYfd-3J2WVTHmN4NnxV-q8-VCfCjjm8FHjSfEVbrNcRB1Zv2MlhH7akCrLHXlF8249373KLJVcDFUte-eCb-iMGK2LDC5fYBfoPO_lwdWElbrUnHpE_3aPRqCWt4aEN7w2ZLYCYl68GdN-74O5qpw_DH8hY_FwfTwbmZ9hwgd_SKN-AJNaSBZx51aFB8El19yRntrNvYS0Kx3tDSJUkLM_Iogx6gYt_-8bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقتدار به روایت تصویر؛
🇮🇷
مقام جمهوری اسلامی:پمپ های قدیمی جا برای بنزین ده هزار تومانی نداشتند؛
یک صفر دستی اضافه کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71301" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71300">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">از دیشب تا همین الاناست که مسلمونا افتادن به جون هم، شیعه های یمن، سنی های عربستان رو دارن با موشک و پهپاد می‌زنن، یعنی کشوری که خانه خدا اونجاست
عقل
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71300" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71299">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWASOShF_BOzv_EoiACOCPvpd3j3uO2mmiOrdaVun_IEmj-XH7fiJitC_Ol7jbuJkXN7FQrKRRglvN_TmMfUW4zvjxBMQzKGVIXM69kTbJVrx7KZsmogV8gnNG4uIw4gvZGuP8CAaKAdEE-7_FVX9DvlFgS9LBLn0CK4XJwDl_PrPpjSeKtJuoD84NQCdjtSdVGlHWeYSry7MZZY4ygXwlRiZKO6zjSwVxAzLlSoEvc6SyMs76nAmIfE9aSmW8FE5tG6-usMzezRUSjj6FpqRF4AKSrwzfa1QJrq_2JFD7GS_A7Ayt251dw-J-vglzzlIlsey143SPV05mSXaMqjzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
وزارت خزانه‌داری ایالات متحده تحریم‌های گسترده‌ای را علیه بخش هوانوردی تجاری باقی‌مانده ایران تحت عنوان «عملیات اقتصادی مطرود» اعمال کرده است که ۳۶ نهاد را به دلیل حمایت از خطوط هوایی ایران، دور زدن تحریم‌ها و شبکه‌های تهیه هواپیما هدف قرار می‌دهد.
دفتر کنترل دارایی‌های خارجی (OFAC) ۲۷ شرکت هواپیمایی فعال ایرانی، از جمله ایران ایر تور، هواپیمایی آسمان ایران، هواپیمایی کیش، هواپیمایی قشم ایر و هواپیمایی زاگرس را تحریم کرد.
وزارت خزانه‌داری همچنین چندین مجوز هوانوردی، از جمله مقرراتی که پروازهای خاصی را مجاز می‌دانست و به شرکت‌های هواپیمایی غیرآمریکایی اجازه پرواز هواپیماهای آمریکایی یا تحت کنترل آمریکا را به ایران می‌داد، به حالت تعلیق درآورد.
این تحریم‌ها همچنین شرکت‌ها و افرادی را در امارات متحده عربی، ترکیه، بریتانیا، مالزی و قزاقستان که متهم به حمایت از ماهان ایر هستند، هدف قرار می‌دهد. وزارت خزانه‌داری اعلام کرد که برخی از آنها انتقال حداقل سه هواپیمای بوئینگ ۷۷۷ به ماهان ایر را از طریق امارات متحده عربی و عمان در تابستان ۲۰۲۶ تسهیل کردند، در حالی که برخی دیگر محموله‌هایی از جمله قطعات پهپاد، تجهیزات صنعتی و قطعات هواپیماهای ساخت آمریکا را جابجا می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71299" target="_blank">📅 20:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71295">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KHcgO1HWNT1pb2j19oUEIdp6lP1hR8LLexIAOGz0VQRI3GvyqKX5iGMxMjL1hm4klPPNHmQWQneIAEvpPMAOSNmrXvhEYNwjVG9hmpQGeYUwwGVv_-grExSHz-IVdl5lb05awll4d3i37zmshYFwCsF1hJd1tCqGtwVpTX44wp4FD02St5N-ZaIxN6oNSiO5p-fhw7u4L8In_4IF_bP9FqCIUJ7vKiATagtl7MEPuJiUctbEnjUP520f70RBC8psxNWtz4Rq4GtF_p2W-9KjjjAdPjVfC-mz7oY6SLRObGQFLf9SFTG_OhlMOBHAA7oKui9-NW9DSqKcs0LynB-1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d307bda604.mp4?token=gAJdZiYVfTt7KgzrGOPT_H1DM1Mg2afw25iHLe9c624OJzN2bPZMYby7JZ1drChSnUICofsEw1sLqwNb4Snhr5LSAUTFSsGp_JZdHERGmWvUyFE-6UpMY_k41RcQg8pUw-Cgy0-ST5jJvo9zFsngwOxy9GYItwpnI3806pLztixQcIy29CmeZ82gouYMX7qrkYBN1a_Od9FMPzZdeGTfzuF5PTqsuP0zPFHlfg1nWy4DGARkJsjp_JQAuF9OWxeWuyGun0-2ypMvl0twsMYih63mcKfRFuG8OO1sYoefmQgl2FdgVUY6K7YJADwZHlyCwm8NXNa6BW2Y-9CN1evc-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d307bda604.mp4?token=gAJdZiYVfTt7KgzrGOPT_H1DM1Mg2afw25iHLe9c624OJzN2bPZMYby7JZ1drChSnUICofsEw1sLqwNb4Snhr5LSAUTFSsGp_JZdHERGmWvUyFE-6UpMY_k41RcQg8pUw-Cgy0-ST5jJvo9zFsngwOxy9GYItwpnI3806pLztixQcIy29CmeZ82gouYMX7qrkYBN1a_Od9FMPzZdeGTfzuF5PTqsuP0zPFHlfg1nWy4DGARkJsjp_JQAuF9OWxeWuyGun0-2ypMvl0twsMYih63mcKfRFuG8OO1sYoefmQgl2FdgVUY6K7YJADwZHlyCwm8NXNa6BW2Y-9CN1evc-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌂
امروز صبح رسما شمال کشور رو سیل برد!
به حدی بارون شدید بود، که حتی آب توی خونه‌ها نفوذ کرده و تبدیل به استخر شدن.
ماشینا وسط خیابون تبدیل به قایق شدن و برق اکثر مناطق قطع شده.
باد و طوفان شدید باعث شد کلی درخت و... شکسته بشن و بیفتن روی ماشین، خونه و مغازه مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71295" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71294">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reh6FWWY3K0_aeT5VgemXTLtv_NJydXB7UPVi5UMMYHKifdO0jnRxKn33GPq5-JGVh2bI8isF0QNpq0quuHMOdwZGlov4B0mZwk6VCxvQsxEOYA0sqt7Fn7eEClHrRUhcUzCx-JIwYLGQgQwQnq_yLRAWGhSD3qdHE_idq9RRNNbaHdZ4amFx2xE1ehWox3cBYJNTWDJE6FagvTqpmSfm2lTUAA8E6QNZb-8dH8dLcAakrjEwmXIhQVPYsHo-34wxUHY0Eor_GXVsVXwmEVjPfrB7U22ws79CtKtF58R7mSI14qymB0yDVB7AEhAaLhC5Dr_OJQbQTz0dMpsjVVqNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران انقلاب اسلامی:
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی‌های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز طی یک اقدام پیچیده اشراف اطلاعاتی و عملیاتی در سحرگاه امروز به دام انداختند.
این زیر سطحی هوشمند از جدیدترین تکنولوژی در حوزه زیر سطحی در دنیا برخور دار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش تروریست آمریکا تحویل شده است.
گفتنی است این زیر سطحی اکنون به غنیمت گرفته شده و طی ساعات دیگر تصاویری از آن منتشر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71294" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71293">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⏺
🤩
تسنیم:
تا دقایقی دیگر خبری مهم از شکار رزمندگان نیروی دریایی سپاه در تنگه هرمز منتشر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71293" target="_blank">📅 18:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71292">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=MxBssK0Flh7iR2spWwKiu4WafHuUy-hzeM6SYj_TFy3WPZpcWjrTUnmutbBcsYkTmJmK8hIBwI7Nv3N3chz9YQ5kQY8djENsC2bqUAZaHq45CF-U2wLtSfCImiL7_UX-Fr2sUPdtbqEpedOrYxq5niY9nuRyO5xATwov2vkvVxaYHy7NYytRZ1Z_zNYcZsbHH-UFPg6iMy3CbtqxmL6s6WpXN4Ulik_jo_O5TeiRINtpOBLph1NbINkZk9gxagYXdKUOe0cuaCIRPn417Jj3S_vaCQ8QgIc70qx-EEZcFWzssjYS6jROYL1Pkn-CJkDWGmZEE1ir7EQxcifSgkZ2Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=MxBssK0Flh7iR2spWwKiu4WafHuUy-hzeM6SYj_TFy3WPZpcWjrTUnmutbBcsYkTmJmK8hIBwI7Nv3N3chz9YQ5kQY8djENsC2bqUAZaHq45CF-U2wLtSfCImiL7_UX-Fr2sUPdtbqEpedOrYxq5niY9nuRyO5xATwov2vkvVxaYHy7NYytRZ1Z_zNYcZsbHH-UFPg6iMy3CbtqxmL6s6WpXN4Ulik_jo_O5TeiRINtpOBLph1NbINkZk9gxagYXdKUOe0cuaCIRPn417Jj3S_vaCQ8QgIc70qx-EEZcFWzssjYS6jROYL1Pkn-CJkDWGmZEE1ir7EQxcifSgkZ2Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
⚠️
🇺🇸
افسر نیروی هوایی ایالات متحده که در ماه آوریل پس از سرنگونی هواپیمایش بر فراز ایران، دو روز زنده ماند، برای نخستین بار در برنامه «۶۰ دقیقه» (60 Minutes) — که قرار است روز یکشنبه پخش شود — به بیان ماجرا می‌پردازد.
این افسرِ مسئولِ سامانه‌های تسلیحاتی که نام عملیاتی‌اش «دود ۴۴ براوو» (Dude 44 Bravo) بود، یکی از دو سرنشین جنگنده «اف-۱۵ ای» (F-15E) به شمار می‌رفت.
در حالی که خلبان ظرف چند ساعت نجات یافت، «براوو» به مدت دو روز در مناطق کوهستانی ایران، در حالی که مجروح و تنها بود، از دست نیروهای ایرانی پنهان ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71292" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71291">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71291" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71291" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71290">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWyiXkKlllLNCm4jDcJjnHY2IZUjs4nikHgjSSKM-akMXth2Dxmdafjx3cvGgd3PI-rLKZm5uhZgtFDEice6lXDOx8rhZsEeJmmS8VVxitrJAt8XIvWMbgePAIeyDOIq1Gggk4s89tNPdo3HAJU-_rzOQk4IiC983yeDDtiWx4cBPibzvPGB6-nsKQX-bEk9FWWcvFjqEI99p6GsKKaC1faIM8KdXntypp7kEkZUx96KwOO3joNEKAfMaT-OowBH-K9PI0PO-Jh_0FLkXvpksUs1_6A5iS9VuSX1PJiqHKN03L4c5gOY6EFr2ZRL8-ZlKqtmLoGGJvIj7HX3BwF4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
منچسترسیتی
🆚
پورتو
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
منچسترسیتی: ۴ بازی، ۳ برد و ۱ تساوی، ۹ گل زده
⚽️
پورتو: ۴ بازی، ۳ شکست و ۱ تساوی، ۳ گل زده
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71290" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71289">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
دقایقی قبل صدای سه انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71289" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71288">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=dA_lvzi1gozrMsxIHKKH68BC_YBcLqwv3yG3wh528fI7PF2u1JnNw3H9x9WFxapqMOIZu18trVdgT39GBpHnSK7vkjzaqbxo1KB_i1x9UAS68VBT4z-zVqP3RgyHSaWoR0t8YmDdc_UQ0jNdJr1aZ8V1eS3hZat0M9k4CkSY1oYl5sUBtfiFuSiu_uJ-KbOHEzcW7-rQlfjud2RO2KAEI6hPK-uqKmc9C4QguIE1NDkK2fVZIwMPt0MHM-PMQM34-REojSmU86WGk-D9OJOjLZX6hRS3llHwuDKWsu6Oz150PZwtTnHmGyM_4IC7pVb5tUxLiqtkmmIVhs5NeGU0_RyxJkBK_3WEYLiMz_4Is1ff0augcZuptl8K5o7XylqTLW4vFI2Q2h1dUu8uGhZEMgOxSV8wlyhMY1HnTKBm3KcECLtLcbb5REbM9fjDi5gEvrVBJCgEwCSSQPSbAfXkJRtzagZ3dR2MsHs8wiJyCoP8YPH3yyzixAKHvNuGaQ8QiWevc8OewAYuVz3P4cJ4Ide9LSEQgTS5bCxDaQzxvAGXAKx8i5uAuIUsHaHuCW-kEldjTcYNUmBzudngD4fYnipVFDMgu42QUFje8xiiqr6dAAihR5ga5iiRorddWB2VJeLzNySkmEHsqraRjnb8lvIWXGoxiJXKNO3xF2BvZd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=dA_lvzi1gozrMsxIHKKH68BC_YBcLqwv3yG3wh528fI7PF2u1JnNw3H9x9WFxapqMOIZu18trVdgT39GBpHnSK7vkjzaqbxo1KB_i1x9UAS68VBT4z-zVqP3RgyHSaWoR0t8YmDdc_UQ0jNdJr1aZ8V1eS3hZat0M9k4CkSY1oYl5sUBtfiFuSiu_uJ-KbOHEzcW7-rQlfjud2RO2KAEI6hPK-uqKmc9C4QguIE1NDkK2fVZIwMPt0MHM-PMQM34-REojSmU86WGk-D9OJOjLZX6hRS3llHwuDKWsu6Oz150PZwtTnHmGyM_4IC7pVb5tUxLiqtkmmIVhs5NeGU0_RyxJkBK_3WEYLiMz_4Is1ff0augcZuptl8K5o7XylqTLW4vFI2Q2h1dUu8uGhZEMgOxSV8wlyhMY1HnTKBm3KcECLtLcbb5REbM9fjDi5gEvrVBJCgEwCSSQPSbAfXkJRtzagZ3dR2MsHs8wiJyCoP8YPH3yyzixAKHvNuGaQ8QiWevc8OewAYuVz3P4cJ4Ide9LSEQgTS5bCxDaQzxvAGXAKx8i5uAuIUsHaHuCW-kEldjTcYNUmBzudngD4fYnipVFDMgu42QUFje8xiiqr6dAAihR5ga5iiRorddWB2VJeLzNySkmEHsqraRjnb8lvIWXGoxiJXKNO3xF2BvZd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇬🇧
⭕️
#فوری
؛اد میلیبند، وزیر امور خارجه بریتانیا:
ایران هرگز نباید به سلاح هسته‌ای دست یابد؛
از این رو، ما نیز در این هفته همگام با متحدانمان اقدام به ارجاع پرونده ایران به شورای امنیت سازمان ملل متحد به دلیل نقض تعهدات هسته‌ای‌اش می‌کنیم.
همچنین امروز می‌توانم اعلام کنم که ما در هماهنگی با اتحادیه اروپا و ایالات متحده، تحریم‌های اقتصادی عمده‌ای را علیه ایران مجدداً اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71288" target="_blank">📅 17:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71283">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645274372a.mp4?token=hiicmzvO9jYomQudcE5I2VNX_dBx7HmtLTiOb90QfMDMzG5H8xJ7JCb2Z5A14jJFPLYl1YiJCEEyqUr1dCYM5JfKsyj6PMZ9Tow44-pT6VPF7DLPdIO6iilQivcVZ4z-UgBgxxZ4R2BpiCUzq3X48tgZlH_7t3b-Ai7K7V9j0uFu7A8q4fYaeyD2PIm9M8eprs6qmL5eWTtQtziMT20ME_PW5Mo8qaQz4q5gcwYh9mA4pgu0L-cQAsReO8JUH5dcKHzlkMprbIUhS8MVZNHUQzRZrS0f6HAu6EIdFLTRy8aIHDmzSDa-URp1qj8HHz_-Lhpu0Wq78khgg_7U51lOIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645274372a.mp4?token=hiicmzvO9jYomQudcE5I2VNX_dBx7HmtLTiOb90QfMDMzG5H8xJ7JCb2Z5A14jJFPLYl1YiJCEEyqUr1dCYM5JfKsyj6PMZ9Tow44-pT6VPF7DLPdIO6iilQivcVZ4z-UgBgxxZ4R2BpiCUzq3X48tgZlH_7t3b-Ai7K7V9j0uFu7A8q4fYaeyD2PIm9M8eprs6qmL5eWTtQtziMT20ME_PW5Mo8qaQz4q5gcwYh9mA4pgu0L-cQAsReO8JUH5dcKHzlkMprbIUhS8MVZNHUQzRZrS0f6HAu6EIdFLTRy8aIHDmzSDa-URp1qj8HHz_-Lhpu0Wq78khgg_7U51lOIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
نیروهای «شورای رهبری ریاست‌جمهوری» (PLC) تحت حمایت عربستان سعودی به همراه جنگجویان قبایلی، شهر «الیتمه» در استان الجوف را از کنترل حوثی‌ها (انصارالله) بازپس گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71283" target="_blank">📅 16:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71282">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⏺
فارس:
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق ارتش جمهوری اسلامی ایران شناسایی شد و هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71282" target="_blank">📅 16:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71281">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de453ade.mp4?token=PX_B0EYePfIcPM3G7YSJUN-vHJV41_tgxkhvn8AX-pTx6RX2EBrQ5EkurhSAm73yw_px6aL1Iusi96IW8_qQIW0F50H0V9yguK8cuwncmRcEjgyx_MKKh0CX2oDscRx9RERZBGmYqA_MOUTl1P7yPid-wR4Te9mpHt54S3eDvjMR9feC6Ooynqcg9b8StprvMlOwLzkkZJxCqi90_KpYjHZ-8vV1Xxie-pGYL03UOWBEvSjxRMCPv721-aK4ur1uGDSUNZ1pAo1prMZA6yaSBjKkLb4fkPk9V31BrL6HMOhKrAHNMQpyjWBGDa06f7Zio79KcfmQkWaSojyNt1MQ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de453ade.mp4?token=PX_B0EYePfIcPM3G7YSJUN-vHJV41_tgxkhvn8AX-pTx6RX2EBrQ5EkurhSAm73yw_px6aL1Iusi96IW8_qQIW0F50H0V9yguK8cuwncmRcEjgyx_MKKh0CX2oDscRx9RERZBGmYqA_MOUTl1P7yPid-wR4Te9mpHt54S3eDvjMR9feC6Ooynqcg9b8StprvMlOwLzkkZJxCqi90_KpYjHZ-8vV1Xxie-pGYL03UOWBEvSjxRMCPv721-aK4ur1uGDSUNZ1pAo1prMZA6yaSBjKkLb4fkPk9V31BrL6HMOhKrAHNMQpyjWBGDa06f7Zio79KcfmQkWaSojyNt1MQ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جنازه و تابوت ترامپ و نتانیاهو زیر پای طرفداران حکومت برای بار هزارم له شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71281" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71280">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=jhewj2JKHA1WNjNSEfLsrnclnTxxL3C7OOO6gj-hNJWLKA_-5d7rB-02V2YJJLZ38jZTdgwYMFvfzl53We-ZaYwvkBJA4EWT6-MUPxL8Af1DW9GPQhwEaj-XGuD2tnuhdWiwze2Yy3RAsyVRdsm2H6qTFwF6RL18sWIHVPqSIDxg-gsoE13O98AZDg3Ipe3f4BLSA7_6PipkdZOVe6M9CgK1kBZTs8dsxHSn-_0e14l4yC7VRtaPH9hNiclGtte_tD4olWv3CMRn62aDSyPMSS-qazwsK6t1sKRHnEe3MvAk40VUhl_A1rCed4VUr9ELKBxeYu57XjQkhpTPvc8K21ciYeh5FQfFvf2o215YYUI28HRoJVBvFuCdVy1KhWckN0Psnyxmf2AT651VE8SlqOzrhBSyVY0WxnfW9G949-vyKDUPqVxl9uZkMvQDv3Shml-5xFz2SNuXNR8FxU1ZfPG5g2zX8Kzb-VwmFLXst-JemeX3yYCfyhSgM2n7fOX6994DQO8aVvE0qwT1XsEo5UkiiV2q2M6X7ioDNaujKh_G44oqYQEXYEkFhKyI7ag5LTYvQbTRixHR9YjlZC1SlPfL558BcgLOpPdBqkHieGNrdoj8r-XmFt5RUq0fvdqDP7KJoj45CpD5mBnam_R7FIIuNkChAaMTft9v5CEegHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=jhewj2JKHA1WNjNSEfLsrnclnTxxL3C7OOO6gj-hNJWLKA_-5d7rB-02V2YJJLZ38jZTdgwYMFvfzl53We-ZaYwvkBJA4EWT6-MUPxL8Af1DW9GPQhwEaj-XGuD2tnuhdWiwze2Yy3RAsyVRdsm2H6qTFwF6RL18sWIHVPqSIDxg-gsoE13O98AZDg3Ipe3f4BLSA7_6PipkdZOVe6M9CgK1kBZTs8dsxHSn-_0e14l4yC7VRtaPH9hNiclGtte_tD4olWv3CMRn62aDSyPMSS-qazwsK6t1sKRHnEe3MvAk40VUhl_A1rCed4VUr9ELKBxeYu57XjQkhpTPvc8K21ciYeh5FQfFvf2o215YYUI28HRoJVBvFuCdVy1KhWckN0Psnyxmf2AT651VE8SlqOzrhBSyVY0WxnfW9G949-vyKDUPqVxl9uZkMvQDv3Shml-5xFz2SNuXNR8FxU1ZfPG5g2zX8Kzb-VwmFLXst-JemeX3yYCfyhSgM2n7fOX6994DQO8aVvE0qwT1XsEo5UkiiV2q2M6X7ioDNaujKh_G44oqYQEXYEkFhKyI7ag5LTYvQbTRixHR9YjlZC1SlPfL558BcgLOpPdBqkHieGNrdoj8r-XmFt5RUq0fvdqDP7KJoj45CpD5mBnam_R7FIIuNkChAaMTft9v5CEegHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چنتا دختر با کیسه زباله خودشونو شبیه لاکپشت های نینجا میکنن میرن تو خیابون...
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71280" target="_blank">📅 16:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71279">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=BuQwXeiHaC4RYWx8CbRVhY-piw1OIO3aMc5TE4KVm6trOXK-FkrTKQ_lwQdh4tNciKadBAflWOw7uM3eDI1twy4L6xnwShXysoYpKmSLMdJl8YQiwBWPyeLDQTK13BtRJ4LZ2h-Fw6G5BxQTufHZT8lukUWfkVQCjz-llf4lWWRqgWxS7-0qq5-FyxaMXdA8ei62o67FIAU1zPF8PYW88aXLLjdJ4fFqlK2xpiLrVp9PY-v8BkC5PxSToUx0U8C4aBYkBnMPyWKoKQlg0Q0uWUVQBGh4W3_krdfriDbCaWfcR4gQ9D3J5M4Ft4wbo1CVyk0opzxfbCScUDkrrm8SiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=BuQwXeiHaC4RYWx8CbRVhY-piw1OIO3aMc5TE4KVm6trOXK-FkrTKQ_lwQdh4tNciKadBAflWOw7uM3eDI1twy4L6xnwShXysoYpKmSLMdJl8YQiwBWPyeLDQTK13BtRJ4LZ2h-Fw6G5BxQTufHZT8lukUWfkVQCjz-llf4lWWRqgWxS7-0qq5-FyxaMXdA8ei62o67FIAU1zPF8PYW88aXLLjdJ4fFqlK2xpiLrVp9PY-v8BkC5PxSToUx0U8C4aBYkBnMPyWKoKQlg0Q0uWUVQBGh4W3_krdfriDbCaWfcR4gQ9D3J5M4Ft4wbo1CVyk0opzxfbCScUDkrrm8SiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
آتش‌سوزی در تاسیسات آرامکو عربستان سعودی در پی حملات حوثی های یمن
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71279" target="_blank">📅 15:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71278">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=mMVJS-6TvwR4zA_HXDWUwdlWgtMvheCZ7bv8E1j3KRPi4jsy4hcVAoJDnS2nsY7XTc1WuDSyYZcUcImosu_KuF-Evh8EurhO2r88QcnDq9nyrMnitEO1hKd62Fqisi_WYdB3K70aiL2jXvE5euS_4rETudN6KxvCpNiz9wvmZD_vwNhdnNkhyjcZ_XIfsw_12P-84PVmSPtyCpxKyLGs-ReV3Mld4eestF3Xj7G4xGjKOoTtlMvj3Fur73QaF1gbT_P4fjVigU-Xqw4B8CDfxir3APvMNbfg7fLhP03dyAlywDT3Q3S4gM_VNMnLPNHNJuqGz-A0hD_RbqVLnD3zIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=mMVJS-6TvwR4zA_HXDWUwdlWgtMvheCZ7bv8E1j3KRPi4jsy4hcVAoJDnS2nsY7XTc1WuDSyYZcUcImosu_KuF-Evh8EurhO2r88QcnDq9nyrMnitEO1hKd62Fqisi_WYdB3K70aiL2jXvE5euS_4rETudN6KxvCpNiz9wvmZD_vwNhdnNkhyjcZ_XIfsw_12P-84PVmSPtyCpxKyLGs-ReV3Mld4eestF3Xj7G4xGjKOoTtlMvj3Fur73QaF1gbT_P4fjVigU-Xqw4B8CDfxir3APvMNbfg7fLhP03dyAlywDT3Q3S4gM_VNMnLPNHNJuqGz-A0hD_RbqVLnD3zIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
در سمنان برای دومین شب پیاپی میان مردم و دانشجویان عراقی وابسته به حشدالشعبی درگیری شد.
این درگیری روبه‌روی خوابگاه عراقی‌ها در باغ‌فردوس اتفاق افتاد.
ماجرا مربوط به متلک‌پرانی و مزاحمت آنها برای زنان و دختران است که بارها اتفاق افتاده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71278" target="_blank">📅 15:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71277">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHauySPc4NuRGtzIJCxHX4IT0tP_1nv-UF5iR7ogvHKtKaQkxdSBAWfuh0Ev3PsTEn8Ly6Z0Hob2f0eP0yxEuObd_xaJfiPWQOseppID1Fi3uGL3Fg_R11QJ34sqayUb4O16LIy5BfiH3pJ2h_fIS1CUEc2UmDy4vm_9xR85CDGur2t876pP9-dNGSMKkGQkhoaNkWLleRoP24xXjXmg_vPyJivTEYFP5yXy4Q01IvA__e0oRIh9PQ-L7DKGkBMTJv2jucxLMSb1yW1mnzrFXVLPvRsDbw0-MjqR4BiOCcajGiaJbGFIi5z9tClEWD0oEbUSJreImqYc-6n7PLvo4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
امروز ۱۷ شهریور، تولد مجتبی خامنه‌ایه و ۵۷ ساله شد.
اگه زنده ای شمع هارو فوت کن
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71277" target="_blank">📅 14:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71276">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=XYs30pkZ1c1wHN7yx4bsnn--xwsGBI_KJUg3_JDSPdyin3KmAroL1cYEfi2drAgL6yRY_JWEi_XBJ2ELzPUFR0rXMOAaNOFGvT3Ji1zolLTKrpkn-BgfSuy0t59lTZPUg4I-3fZeOUjC-oJ1PUf6f4onVnWIJjTBt9ChmB3AyQAyluCyLoqJBkWWbJi-maBVU-tKcBjEnz65JGzpYAJTBuPoXiC9wU87ieXNdj7eddDM89BvZcekvefZcQkYYzry4VwSWLtrDWptuWde5Aw4de7-ie_ItS4eRafNDbnOlpnrnBNtDdqemSl-Qm-sQQIfAd6I2I6uh3vs5efxnJ8LCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=XYs30pkZ1c1wHN7yx4bsnn--xwsGBI_KJUg3_JDSPdyin3KmAroL1cYEfi2drAgL6yRY_JWEi_XBJ2ELzPUFR0rXMOAaNOFGvT3Ji1zolLTKrpkn-BgfSuy0t59lTZPUg4I-3fZeOUjC-oJ1PUf6f4onVnWIJjTBt9ChmB3AyQAyluCyLoqJBkWWbJi-maBVU-tKcBjEnz65JGzpYAJTBuPoXiC9wU87ieXNdj7eddDM89BvZcekvefZcQkYYzry4VwSWLtrDWptuWde5Aw4de7-ie_ItS4eRafNDbnOlpnrnBNtDdqemSl-Qm-sQQIfAd6I2I6uh3vs5efxnJ8LCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
شب گذشته در سمنان، به افزایش قیمت بنزین اعتراض شد.
این اعتراض در پی تصمیم جمهوری اسلامی برای دو برابر کردن قیمت بنزین خارج از سهمیه یارانه‌ای از روز سه‌شنبه صورت گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71276" target="_blank">📅 13:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71275">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F95YuGq3GAVQbRQgYuq6nGeC-B4J43653tnCLbH455ROdrjKz7hsw0OahYgP8If6uXLM-iYu5egU0WipN7rsWvtSHPXzA_h2-t2y9P8gBh8gYTv9iVqMCYm6Bz-zobHwR2XbGcMhOwJvdnV3mUgMR93mnfGeKJRpX7N2EAm25L5vi8C7-sGo9juvgQNKEuUGewxGBG6ViOPF5bgIUivLxEw33tElRdXbBcZFYrZAN5Oq0TxHnXL_X3NbTzdK_nqOnCB8O-tzbEfKrm1ITdLURyCzzGDcaFVXOOWljwtnRgE32d8LG6WMe8Kknwf90uwiuxyzbPolSh6n4isKfOho8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
جمهوری اسلامی ایران همواره با جنگ مخالف بوده و حفظ منافع مردم و امنیت منطقه را در پرهیز از آتش افروزی دانسته است.
اما چنانکه تا امروز در برابر تجاوز، دلیرانه به دفاع برخاسته است این مقاومت را تا پشیمانی کامل متجاوزان با قوت ادامه خواهد داد و پاسدار حقوق ملت بزرگ ایران خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71275" target="_blank">📅 13:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71272">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EKJarUUfxyJkXEPFUkCPfK81JPqFjZRET7y_Pvvv_afSfdOg40bjkHIN8GzjUKJiUVXVct8XVap3NIb9noqm2FFWihFhNE6MSRT-fobh4Qtyh2HnXiJzpcVA8z7QoBX7h7MsbWzLrAu_W_LcVJ1Y_b_5ioNtarJLUe48AKqEUaJXvsJNoi49DLYNn0corZzSjbPmivS3uz5IfqiG-4mnaALNNM_9xTZEfDDqlCbJoBvGcFewJbWzKjYBqliqqiCpEvoZVf1e2-2QcC9HP_9IKIPmEBmtWsc-it3NKfCPtvGm4ZToVLSZikeaVu8dRGkjQ_yFz1WhPHDGwrSX_swXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8833895957.mp4?token=GqNsubCvJC4pDqdQy5p1Pla9wU7bMHQvbFvMq2UFwe9BDAuBRVfdt_cBP5q_hseGTjizH6MW-Y2t4fkzbJVYh-P45wQKwy7XlZloznWK0yQCE7cJSg-NwDkalX92aFP8Kd_TuG715U3wAyNlLlu7pITtb7n0XdcKt-8TA0HDrtcX4IOwTHtGkY2qLlKVpMRPlgGsxIPM-PesnXv8QnwVjwP4ipDDUAMKQtN1LQ30JJjCmeQm4xolus6mVjrC2nMeAKpubMJEd7FsioNKRanHUo4xSep7MMoNFqVSmIkvF9apoChcYmlva8RHlRRvAzOGTbTEfEw2CZIMnkEWwXbFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8833895957.mp4?token=GqNsubCvJC4pDqdQy5p1Pla9wU7bMHQvbFvMq2UFwe9BDAuBRVfdt_cBP5q_hseGTjizH6MW-Y2t4fkzbJVYh-P45wQKwy7XlZloznWK0yQCE7cJSg-NwDkalX92aFP8Kd_TuG715U3wAyNlLlu7pITtb7n0XdcKt-8TA0HDrtcX4IOwTHtGkY2qLlKVpMRPlgGsxIPM-PesnXv8QnwVjwP4ipDDUAMKQtN1LQ30JJjCmeQm4xolus6mVjrC2nMeAKpubMJEd7FsioNKRanHUo4xSep7MMoNFqVSmIkvF9apoChcYmlva8RHlRRvAzOGTbTEfEw2CZIMnkEWwXbFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌧
بارش شدید باران دیشب در رشت که منجر به وقوع سیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71272" target="_blank">📅 12:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71270">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaU2kdpf6CzcpW0o-ZVfduSwsS5M2KLgLoA9Kr9FRDzcHam2PhSNXNDOAeLAdzkL_2eVokLTI3IJePkLi9Y0vT4RxTAXLYrbg_vm3cn5W0o9KqONC6wx9sngzARiflmWGKSEhnQS82FILezNTOgDmNGYyXg8uKZatI0datSx0hRUrNm5pY8ulkFsynWgNviVej5gEoxx4QaxKfOJut6CdnjiStp9_NSWir8nu1kP-W3DaqSASZWPpywL7GV4PikkpcAdWtwCMa954bxbISnxreZVWju9nfPsUZIc0vgNR5ssRV4cuw-T7UFu5pswNj8ddwSfFfm4RvHsLczOt0at4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=Yn_-uN3MeI7YmggrheMQ_zS6ERIJdlwR_vxR1SYYcHN3zmNf7P_DUWT6bOgSzev53_-pnqyAEPGo2aPXCH3I4ZQ-QZSI2F1_vN5LxEgVm5xrIr-5Joj5whRO6wmG_yNQ3adgU4CSxd8hbGY3o2n08aJLZq1px9UxSSrqV8WphhIlkfqMqdlm4wDbAn6Qlgwga7jWc8L85kanwWTOuGyo7D8tbxCUrcgQ5Xbaej5hJYOhLEgyrzXhFZTNW_GQgATKoc5CvDCIDmaXZU7sG0TFzmkfTZ0f7Lw7S2veRh6YVCeZ5Z_-VwN5SXnvpzD69UYC6C_Xh9LqpeIXxaqq1BUmEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=Yn_-uN3MeI7YmggrheMQ_zS6ERIJdlwR_vxR1SYYcHN3zmNf7P_DUWT6bOgSzev53_-pnqyAEPGo2aPXCH3I4ZQ-QZSI2F1_vN5LxEgVm5xrIr-5Joj5whRO6wmG_yNQ3adgU4CSxd8hbGY3o2n08aJLZq1px9UxSSrqV8WphhIlkfqMqdlm4wDbAn6Qlgwga7jWc8L85kanwWTOuGyo7D8tbxCUrcgQ5Xbaej5hJYOhLEgyrzXhFZTNW_GQgATKoc5CvDCIDmaXZU7sG0TFzmkfTZ0f7Lw7S2veRh6YVCeZ5Z_-VwN5SXnvpzD69UYC6C_Xh9LqpeIXxaqq1BUmEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپاد اوکراینی به یک ساختمان مسکونی در پرم، روسیه، تقریباً در ۱۶۰۰ کیلومتری قلمرو تحت کنترل اوکراین برخورد کرد و یک نفر را کشت و چهار نفر را زخمی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71270" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71269">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71269" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71268">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZ-m1tuDRm4rwcp7FUHahRp62ByrnKKTHdxVm2X2sheIGEDXNXjiOSjm_BpYlk-IxkeX3kkFsAxKdkXVnnAiXAkzUWD8zyLRqP4bLRbLJ5OEpEkUVF9wQ7rO0wjmf3Hg9DlWj4M-LE0oylSVpGS6KMhAVvM4PD_3f008TBcmOEWv-Jw62vMFzbSwYrT1UD7SniqFlxIt5CnTg7RAznZHyKNicjUk7763Uhp8MPQR3Rxmd4mGaVdq9CpUGpathsrPjgi3ZOrNuTAbnRb6tW31X9nUIyEfJ1Jpm3_SxT7AGA_9lVtKW76cVXxZW_ww-h5aQogTCxZg_AEWgo2S-8bJcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
رئال مادرید
🆚
اینتر
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
رئال مادرید: ۵ بازی ۵ برد و ۱۱ گل زده
⚽️
اینتر: ۵ بازی ۵ شکست و ۲ گل زده
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71268" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71267">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=NRYrbvAPBs1ryGXga_ZUuou43-JSWkUDIX-eHWra2QeD79swZF_TzwStIONBACPkmaW6BU8VOE0_jMB_xKRO2d3AcefRfx-vv7TOEjMdeW_ni0Gy1qyK1diZVKm0PTM9uCQ__8hx4smhtiEU0nF12cz1KMAmiHeZMcYK2sNGMfohq0hBCzaYgG7W2AppeIPBUaWNntBCLMeyiwJ9J70c_ivRHtVxbXSjsb0xFARI4WN_Fv-mHs-_CxCLIbLoVp5a5FahN4hnzC7jCHh4VdqzxU-OJmHeGVjIs0nx-i9th8XAuHdQ35iAfoeOxXB-6ku9zwLhtn5c5tu5QqUve5WF3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=NRYrbvAPBs1ryGXga_ZUuou43-JSWkUDIX-eHWra2QeD79swZF_TzwStIONBACPkmaW6BU8VOE0_jMB_xKRO2d3AcefRfx-vv7TOEjMdeW_ni0Gy1qyK1diZVKm0PTM9uCQ__8hx4smhtiEU0nF12cz1KMAmiHeZMcYK2sNGMfohq0hBCzaYgG7W2AppeIPBUaWNntBCLMeyiwJ9J70c_ivRHtVxbXSjsb0xFARI4WN_Fv-mHs-_CxCLIbLoVp5a5FahN4hnzC7jCHh4VdqzxU-OJmHeGVjIs0nx-i9th8XAuHdQ35iAfoeOxXB-6ku9zwLhtn5c5tu5QqUve5WF3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
حساب کاخ سفید در پلتفرم ایکس:
در روشن‌ترین روز و تاریک‌ترین شب، هیچ شرارتی از نگاه من در امان نخواهد ماند.
آن‌هایی که قدرت شر را می‌پرستند
از توان من برحذر باشند..نور فانوس سبز!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71267" target="_blank">📅 12:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71265">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=AwTqL6kxh6KOWWFjoM1sF24scyZe2Fl3tlbfYfDPVgzecVikPX1_oinMG2kN-7n-C9TxtLIZhzpUoT5aP5s4dJ5z75zn_zmcNEjT26lRPd-Lx_gJxNYAl7vrFkF84XFEhpiZQYOtjIuf1oxIJHe5Fqg1sAvDreGKp2XTGcySUtobigrfUEDRKGH_qarEUTNQ0rd6m24TaIIy_G22mg9LjxNdVRhJyLO8PZr14ew5-JgENuK_V_jUHm7nRt4AET94SfrIovEiJCEZOOLOMOHHK3CbLtu5OOShsDB0SvQiKdqDpFh8N6IhdKFtqvW3w3ZTJ9bRNazLC985CNZlmy22mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=AwTqL6kxh6KOWWFjoM1sF24scyZe2Fl3tlbfYfDPVgzecVikPX1_oinMG2kN-7n-C9TxtLIZhzpUoT5aP5s4dJ5z75zn_zmcNEjT26lRPd-Lx_gJxNYAl7vrFkF84XFEhpiZQYOtjIuf1oxIJHe5Fqg1sAvDreGKp2XTGcySUtobigrfUEDRKGH_qarEUTNQ0rd6m24TaIIy_G22mg9LjxNdVRhJyLO8PZr14ew5-JgENuK_V_jUHm7nRt4AET94SfrIovEiJCEZOOLOMOHHK3CbLtu5OOShsDB0SvQiKdqDpFh8N6IhdKFtqvW3w3ZTJ9bRNazLC985CNZlmy22mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یکی‌ از مراسم های تولد در بالاشهر تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71265" target="_blank">📅 11:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71264">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=Xi-aEKoRvuCMZubN3fB0VMjhL41igq1rRruPR5TcoLnHFLndZTsu7rIeL4dR8qoX4rBneymq96jyuJWtIo5uE4SfuMOj28a_3QgNw8gy8oaLmhgb10OCEMApmyBUBw8wSCu2KOFwYXQQVH7DGI1PqW_pt2VZZ-UwPQv9-zbP17W7W15vlpYQuotpc7mlHoJy8RkjEfqfUJqkSqpVYGrIsgDg1Z35vh_Qw7p9TX4BmkQ6P_3SGqgD7_f3aHRm73Iz7qC4hR2kznmpvqbCVxaou07Fq2JV2qDVLG59bQ2NVyVsxzuJh3XaKcxHtA7I2o6GrrW6KSym_nDmfXp2gmAMFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=Xi-aEKoRvuCMZubN3fB0VMjhL41igq1rRruPR5TcoLnHFLndZTsu7rIeL4dR8qoX4rBneymq96jyuJWtIo5uE4SfuMOj28a_3QgNw8gy8oaLmhgb10OCEMApmyBUBw8wSCu2KOFwYXQQVH7DGI1PqW_pt2VZZ-UwPQv9-zbP17W7W15vlpYQuotpc7mlHoJy8RkjEfqfUJqkSqpVYGrIsgDg1Z35vh_Qw7p9TX4BmkQ6P_3SGqgD7_f3aHRm73Iz7qC4hR2kznmpvqbCVxaou07Fq2JV2qDVLG59bQ2NVyVsxzuJh3XaKcxHtA7I2o6GrrW6KSym_nDmfXp2gmAMFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یک پهپاد اوکراینی در طول شب، بمب‌افکن تاکتیکی سو-۲۴ روسیه را در پایگاه هوایی ساکی در کریمه با موفقیت هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71264" target="_blank">📅 11:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71263">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=GnUQIRHXHvP9iCu0EXmmrQYuH6ZsbWhtDQDKZomcsuPkn70RnJALtEu6TOn9YBjqxndCy5hqCtXTP8h0EHS97DgJEE42T25QwFhUJddf3HGmx9uqJXGJTkW10_fmy4uhIDK3h5Ce5KhIRkTz9PlvJJaI9WBbmBhz9zJNf0EMvozzBOOIsbcQ9rx8uCMVWIisK5PMr7uDy7ufiwmVq5WwjOas-7JK2gmFrW-0jfbLz3ZQFYdPdLFHMNiBZimOKpTc6wKAPIRlP5cRdL9Rh17eehAiCxTNY045DCcfWaGHaZo2Ks_8xy7XhrN0H9_lnxRYYLECYSTUF7vGG3hA1BiEzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=GnUQIRHXHvP9iCu0EXmmrQYuH6ZsbWhtDQDKZomcsuPkn70RnJALtEu6TOn9YBjqxndCy5hqCtXTP8h0EHS97DgJEE42T25QwFhUJddf3HGmx9uqJXGJTkW10_fmy4uhIDK3h5Ce5KhIRkTz9PlvJJaI9WBbmBhz9zJNf0EMvozzBOOIsbcQ9rx8uCMVWIisK5PMr7uDy7ufiwmVq5WwjOas-7JK2gmFrW-0jfbLz3ZQFYdPdLFHMNiBZimOKpTc6wKAPIRlP5cRdL9Rh17eehAiCxTNY045DCcfWaGHaZo2Ks_8xy7XhrN0H9_lnxRYYLECYSTUF7vGG3hA1BiEzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تهران، بیت رهبری، ۹اسفند ساعت ۹:۴۰دقیقه صبح
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71263" target="_blank">📅 10:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71262">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=dSZx4YH1kj8A66w3u0oI41h37g6DBK_x7PAUmu4y_lAnjfPXlzYWpvc-1iPtuZ-xHLfizShuwTiNjnvMV6KQHczfZdwlHvCoDkYYMrJR-L8fclFirwEmsZuhS0xKE48_nfVHnaA2WZ74pSekWpTPMbUxJOXtjNd2zZpCZtdfUsu6IPZoNXopxCeUf-yEjlFB5bu-3IgXkAhK83TykaplDQdqG5mk-lL-xw9nBDBqJEU9lUjEYeF8Z0E147mrIErIi8RgQaoNfd5TSY5I60C597uo4ewzcI6Fl7NYtyapS84lDqUAYJ8YuCLrM1RXL9SgU1jv-salMydy4E4kkayaYyS9M8Eb_VQXmpImJCCAYsGBaD2nQ5lfA3xLdoNxZfoitdwHV5kyKIUCNlqgoZ-Q7rUnU-HD7iV6z_O57xeYPeNdVmjzlAPlFxutyCSwepMDmtjmqzcsIKz9tuoAzayHgYnPX6VYHKt8lztPd74FdvAc83Y_VUNlgFI1HMF6dFZ9cE0G2-YU1puUl-R2CyMaNG_aO8i8tS2889o08FdyqjBSsXmE3Clqn_ZamUw8nMoZAjyBbhFsMU-UUdS3EHBFqbX9L2es5C55-oFOvHoU3rPotJHJudW_QtJdngKy9cOkdOxyRPfQqLBtpO2aBsFXJB5RO8N56ykQouOEhSnqfAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=dSZx4YH1kj8A66w3u0oI41h37g6DBK_x7PAUmu4y_lAnjfPXlzYWpvc-1iPtuZ-xHLfizShuwTiNjnvMV6KQHczfZdwlHvCoDkYYMrJR-L8fclFirwEmsZuhS0xKE48_nfVHnaA2WZ74pSekWpTPMbUxJOXtjNd2zZpCZtdfUsu6IPZoNXopxCeUf-yEjlFB5bu-3IgXkAhK83TykaplDQdqG5mk-lL-xw9nBDBqJEU9lUjEYeF8Z0E147mrIErIi8RgQaoNfd5TSY5I60C597uo4ewzcI6Fl7NYtyapS84lDqUAYJ8YuCLrM1RXL9SgU1jv-salMydy4E4kkayaYyS9M8Eb_VQXmpImJCCAYsGBaD2nQ5lfA3xLdoNxZfoitdwHV5kyKIUCNlqgoZ-Q7rUnU-HD7iV6z_O57xeYPeNdVmjzlAPlFxutyCSwepMDmtjmqzcsIKz9tuoAzayHgYnPX6VYHKt8lztPd74FdvAc83Y_VUNlgFI1HMF6dFZ9cE0G2-YU1puUl-R2CyMaNG_aO8i8tS2889o08FdyqjBSsXmE3Clqn_ZamUw8nMoZAjyBbhFsMU-UUdS3EHBFqbX9L2es5C55-oFOvHoU3rPotJHJudW_QtJdngKy9cOkdOxyRPfQqLBtpO2aBsFXJB5RO8N56ykQouOEhSnqfAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🔞
وایرال شده از رقص و شادی سربازان ناو آبراهام لینکلن توی کلوب شبانه توی پاتایا تایلند
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71262" target="_blank">📅 10:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71261">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b860e39243.mp4?token=o40SkEDM2npOhFf0bXypGTfUGSE8Fs0DnsGAEW9477lPZT15mP0wU0kOZmoUFc66eMq3XqVm8ndBtb4LdnjM4JvvUo66fHIZzGbxxouAS8swVPgpb6a1EkX4Gfdouany4RdqaL_kYJcn8q5HJtG0fOve-2VQZ4Iaf4KfR69nth8zmxpOSIV3Cu7bQqh2zT0rNKwi5gCUNlvkK2kpx9NehMwK-k6A1ZuKMmNKrCtP-0OJk3PKK7ik4H6MF5RNugGwnynbhUFDQxyTwW8AWMSjL1_rV10PwMM-KZoxmDBEBTij2VDjVzGH8DdvS550yjvcIUOMowTy9kl8M90P4zGwBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b860e39243.mp4?token=o40SkEDM2npOhFf0bXypGTfUGSE8Fs0DnsGAEW9477lPZT15mP0wU0kOZmoUFc66eMq3XqVm8ndBtb4LdnjM4JvvUo66fHIZzGbxxouAS8swVPgpb6a1EkX4Gfdouany4RdqaL_kYJcn8q5HJtG0fOve-2VQZ4Iaf4KfR69nth8zmxpOSIV3Cu7bQqh2zT0rNKwi5gCUNlvkK2kpx9NehMwK-k6A1ZuKMmNKrCtP-0OJk3PKK7ik4H6MF5RNugGwnynbhUFDQxyTwW8AWMSjL1_rV10PwMM-KZoxmDBEBTij2VDjVzGH8DdvS550yjvcIUOMowTy9kl8M90P4zGwBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم ترسناک منتشر شده از یه بیمارستان روان‌پزشکی و رفتار یه بیمار ساعت ۳ صبح بخاطر مصرف مواد مخدر شیشه، گل و...
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71261" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71260">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=GD5DdQM1UH7XNbkw_yIIgyiGRSov9cWVw1O8xXZCrcqpvC2G85MZlG5JRRzZ3ojzd88TVFZw3KvBHJAzgMKH5G1JBRHEw5qcRUKaavY7quNa9DtE0q7fL9YJBGRYhzJxeo8xpKv1aknHBMLdGFHVulwOfadxFVlzv3m6WdqILaIbzQQ0Xv6KynCyXROvida50-gh8CbfJr0DHdXvh3l-z5od7bN9uhMF8RvB0pb1FnSAogaHJDiIMISm3ojmkIeSnsJi_bwiE30JrU3IhasEpVZ7_S5Bpb7f-TEzlqLuf68C2I4hKY2R2figampTf-aaibbUWYJFxpF7bWcQIoSFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=GD5DdQM1UH7XNbkw_yIIgyiGRSov9cWVw1O8xXZCrcqpvC2G85MZlG5JRRzZ3ojzd88TVFZw3KvBHJAzgMKH5G1JBRHEw5qcRUKaavY7quNa9DtE0q7fL9YJBGRYhzJxeo8xpKv1aknHBMLdGFHVulwOfadxFVlzv3m6WdqILaIbzQQ0Xv6KynCyXROvida50-gh8CbfJr0DHdXvh3l-z5od7bN9uhMF8RvB0pb1FnSAogaHJDiIMISm3ojmkIeSnsJi_bwiE30JrU3IhasEpVZ7_S5Bpb7f-TEzlqLuf68C2I4hKY2R2figampTf-aaibbUWYJFxpF7bWcQIoSFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
⭕️
گزارش‌هایی از تماس‌های ناشناس با ساکنان جنوب ایران؛
درخواست برای خودداری از حمایت از سپاه در درگیری‌های احتمالی آینده
بر اساس گزارش‌های منتشرشده، اخیرا تماس‌هایی از مبدأ نامشخص با شماری از ساکنان بومی جنوب ایران برقرار شده و از آنان خواسته شده در صورت وقوع درگیری‌های آینده از سپاه پاسداران حمایت نکنند.
گفته می‌شود این تماس‌ها با کد کشوری سوریه برقرار شده‌اند، اما هویت و وابستگی تماس‌گیرندگان تاکنون مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71260" target="_blank">📅 09:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71259">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71259" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71259" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71258">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGNUj8wJymjgj-XK1VvrDkcA6iwyoVZBoL4EUhPq-ZYv4A1tBl6Aq7fPb_uMxpPmojr0-T6eGLG1_tD6HP5eNKrRHzXCsPu9i8CGJi_7UdNzQI15JAZMIQlAhTfuRCIVynDeaZm83H2Akgem8IrsHK2DsEO9_oo4G4QWTYMLsn3zmQVqx5dudq-n3MEDFqrjHyY5VwnlXq7nAxpzHzv15F93oL22xfUhnGSB8R8dKS5GyblpmA4uOLwjIQR7xaEAUXUg0akJbxXAsjwUsbgsTTls2lkzYI9P832pTeXpY92tCNhPRbpLsteucYUmx3sg0xGpp85Xt2yYYaB6xXs-dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71258" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71257">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⭕️
⭕️
از دقایقی قبل نرخ سوم بنزین به 10هزار تومان افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71257" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71256">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a780504.mp4?token=rqdnJRnnqyLRIiMOHBXZA431b_jBfvgHuJ3uFljIeYpXgAecROGZ6vFSVn9NkMPpFo9dTlqOjvjnzRrz8LXCnu-MYcIlvooguvnb2-6TfMLZi8t87Dsclc4jUQyhmvw9kW4FAZ0VEIKYoDs6ElOkoOwVw4PHfOKjcQ3FslbnwODwuy3lvW_83Ajh6aFDsq9Dzi1ckHxJPINis_uk2jJcRqtyIby5noosTKKgvJ5udHmwh3b_vZhrw6XzUBV7Cibdw5h3HJ5DhjiA6ttT46kF19wiiKdwvTnMtSiDQsfHGR07PFuHi4O2_i8Q8niNpu81K0MjznFxbjQ7s7WEd0idXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a780504.mp4?token=rqdnJRnnqyLRIiMOHBXZA431b_jBfvgHuJ3uFljIeYpXgAecROGZ6vFSVn9NkMPpFo9dTlqOjvjnzRrz8LXCnu-MYcIlvooguvnb2-6TfMLZi8t87Dsclc4jUQyhmvw9kW4FAZ0VEIKYoDs6ElOkoOwVw4PHfOKjcQ3FslbnwODwuy3lvW_83Ajh6aFDsq9Dzi1ckHxJPINis_uk2jJcRqtyIby5noosTKKgvJ5udHmwh3b_vZhrw6XzUBV7Cibdw5h3HJ5DhjiA6ttT46kF19wiiKdwvTnMtSiDQsfHGR07PFuHi4O2_i8Q8niNpu81K0MjznFxbjQ7s7WEd0idXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
عادی‌سازی سقوط تپه علی‌الطاهر توسط طرفداران قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/71256" target="_blank">📅 23:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71255">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=Ozh8k5bhB5I7uILE2VboWK5HeUaeOdSKvCqLFvoOVbPh5tl_CyIdWfYEUNkCrrGaySBbU-zzrCS5ULVGXe3MP2auzonONNcxM8lhfLw1As9XV3mV9-w9RNb2PzQJnHQZpm7g1fuIgkoFy1OrEecFKy7Y53YpwdEwgULRqDFoOZ5cSHOfnOF9LJARn2I1yjD-aDSbu4FX-7j-pJqs3Z50Ofa2vUnDT6w2a7-kxz2Q90bmKEq5r742Ow0O0_FW_dV6rtMfbrZGUSHHutgWl5El-rTDL8ivcNyazs5GA1gSDn0n3qZ_HVwww9RIvmlMPvqS0babI9DdXmvcaCtdOTmh9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=Ozh8k5bhB5I7uILE2VboWK5HeUaeOdSKvCqLFvoOVbPh5tl_CyIdWfYEUNkCrrGaySBbU-zzrCS5ULVGXe3MP2auzonONNcxM8lhfLw1As9XV3mV9-w9RNb2PzQJnHQZpm7g1fuIgkoFy1OrEecFKy7Y53YpwdEwgULRqDFoOZ5cSHOfnOF9LJARn2I1yjD-aDSbu4FX-7j-pJqs3Z50Ofa2vUnDT6w2a7-kxz2Q90bmKEq5r742Ow0O0_FW_dV6rtMfbrZGUSHHutgWl5El-rTDL8ivcNyazs5GA1gSDn0n3qZ_HVwww9RIvmlMPvqS0babI9DdXmvcaCtdOTmh9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یادی کنیم از اوستاااااد خانعلی‌زاده که در دوره جنگ 12 روزه معتقد بود جنگنده های اسرائیلی هرگز وارد آسمان تهران نمیشن چون باید چندصد کیلومتر داخل ایران بیان و برن و این کار ممکن نیست  و اینا همه شایعات مجازی هست!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/71255" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71254">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/71254" target="_blank">📅 22:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
⭕️
دقایقی پیش صدای چندین انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/71253" target="_blank">📅 21:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead429175.mp4?token=pOaZllZaa3yfrfCCT6ZAIbVWRHjJwWymZsyXICLeLfPb69gZGTEaLpwm3CCM30G8I2StKjJ7s-043DCGwOhe1orYZyxIiX4gJ_NoAPmBBOygpjZd6oRsxkMolHLNS5KANP9oqVY-AArUXcfNkFr0rLbwPvh7R6dyAlgH-T1BHOeFCmI0mm_ehqhr9PNXZBeSbVe_eBg1IRM4JIoho3Q3MhdjACDND0Xmg1uSE-mlFGdu7gw22T73znn_KTbTlaLObeLpfv1zM9j_EWajj6BP_KLAiiAFh3O8AsxA8TBMmRwuNc4DUUlzTw2CKNFIidnbCnwCoMrjdUKzgFF6g0DP0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead429175.mp4?token=pOaZllZaa3yfrfCCT6ZAIbVWRHjJwWymZsyXICLeLfPb69gZGTEaLpwm3CCM30G8I2StKjJ7s-043DCGwOhe1orYZyxIiX4gJ_NoAPmBBOygpjZd6oRsxkMolHLNS5KANP9oqVY-AArUXcfNkFr0rLbwPvh7R6dyAlgH-T1BHOeFCmI0mm_ehqhr9PNXZBeSbVe_eBg1IRM4JIoho3Q3MhdjACDND0Xmg1uSE-mlFGdu7gw22T73znn_KTbTlaLObeLpfv1zM9j_EWajj6BP_KLAiiAFh3O8AsxA8TBMmRwuNc4DUUlzTw2CKNFIidnbCnwCoMrjdUKzgFF6g0DP0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
دیشب خبرنگار لبنانی داشت توی نبطیه گزارش تهیه میکرد که همون لحظه به شکل پشم‌ریزونی اسرائیل حمله کرد به اونجا و همچی قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/71252" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=ZJDCLi8X5LTsnJh8edEhc0E9nm8Y_0_FFYn6eHcArHwhU5qaDBHC8p86H0dg0u31AvrdkHGhgroFcVXTx3Fbq9cnsU0-ahklUzIxNZhcM_Q4qaVy_BVK77swMTXPFfM562fnkium23Z7z8uXcpDbJ_hEuV9nJswfJf6bKRh4AEBbofU05cOxV4ULlLGqGyZeKLuCY_QQNwj12UaTdh76mQLzQe-qvoviSgecg5VXibCvBFCcEqym70Bq0Wy29QXCfpEjm-5QqYIJMoJiIclMYI13qBplSLEklq8MqHjL5tf0KlGv0hJThWNjkCfvsVAldtz0cj9srLRCDFhbzHY97jYvV3ak8E3lWzIG8PID71JHAsq5BPv3NMwWNwx7s3YYrvXHP6d8SgTlOLWMVQc1H62Jr1agie9YPa7eS0UZdeBnA8OeT3bE-xtUjMk_b1dDirt7kLjff_vua-daQOWdubU1rhXYR2X87CZPRmJSrGefRygo6uKqDO4kwJpyU_V-S_fCDOnRlgP3OmAkPm3sJjX8BKYV7NuR6OOIR5xGyr2MbbzUBUwIl44SvWSaBHVCjoevjhNFlXiz4ePXi5FurS_zbBtHB8JPuKAm2gSE4ZI29lHXzqGJXnVmkS1XcVWdhUqiFN23MdE-CJTP8jdwKVxG2A_Cf0oDJABLYfBxlZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=ZJDCLi8X5LTsnJh8edEhc0E9nm8Y_0_FFYn6eHcArHwhU5qaDBHC8p86H0dg0u31AvrdkHGhgroFcVXTx3Fbq9cnsU0-ahklUzIxNZhcM_Q4qaVy_BVK77swMTXPFfM562fnkium23Z7z8uXcpDbJ_hEuV9nJswfJf6bKRh4AEBbofU05cOxV4ULlLGqGyZeKLuCY_QQNwj12UaTdh76mQLzQe-qvoviSgecg5VXibCvBFCcEqym70Bq0Wy29QXCfpEjm-5QqYIJMoJiIclMYI13qBplSLEklq8MqHjL5tf0KlGv0hJThWNjkCfvsVAldtz0cj9srLRCDFhbzHY97jYvV3ak8E3lWzIG8PID71JHAsq5BPv3NMwWNwx7s3YYrvXHP6d8SgTlOLWMVQc1H62Jr1agie9YPa7eS0UZdeBnA8OeT3bE-xtUjMk_b1dDirt7kLjff_vua-daQOWdubU1rhXYR2X87CZPRmJSrGefRygo6uKqDO4kwJpyU_V-S_fCDOnRlgP3OmAkPm3sJjX8BKYV7NuR6OOIR5xGyr2MbbzUBUwIl44SvWSaBHVCjoevjhNFlXiz4ePXi5FurS_zbBtHB8JPuKAm2gSE4ZI29lHXzqGJXnVmkS1XcVWdhUqiFN23MdE-CJTP8jdwKVxG2A_Cf0oDJABLYfBxlZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمودی بعد مصرف یک بَست:
موشک رستاخیز ایران می‌تواند در لحظه اصابت ۸۰ کیلومتر مربع را نابود کند
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71251" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71250">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU9HWQX-Ffiy2Y2MYs809S9kj8Xt7RpWfbInnAz2VYGO7kJjWF0GSipz_OAZSQ65ZdxEmMHXueG_jO-G4Gxa-9-TG0u5NTiKzFBibaX9YIyUuriCN84sST4-S1bqi4biDtREAvpQBSMwEsd3JlBXOeNjMzjqmjw0Izd2vHinpDbDLkuHWAtuttzksYqv3hLv9CGXqueswPaRJL-yiEdrroFUH5CBKAEmOuNNjtqVncjsjol6YFC_YCi7q-BEYcEtgNY9UrdGl22PZC3HYrUe9tCiMiQpoUWK8uurPrgCydpqNOWPXoH68YWlglYC4HpwK4SPEvOFl8dIRy3O-tTlnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
🇺🇸
ترامپ بازنشر کرد:
سیاستمداران ارشد ایران خواستار پایان دادن به جنگ هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71250" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71249">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=WTVeUk_N8Pav71XkALh6Dfh_nhfsF0pl3m5nZVAfPS4bGkFxiT8rGvrLuL2ONzUApn8cF1p3JCejk2yRtq5_1D5hExoHcYYvVD8TDaXb_FOB89AGx2dA9bJ1HaqJA3_3PQ47Zb4chs59vk_fqf8tkNQFqs1tXsIg01f2PGcUkT5OjiPCTb3DwLeipxIKf5ZuiZwPghCNoH_dO1VMJmDR0B1KhYNCUFpAelbpMJFPZoDS62DBB_73-JOvoLUqSFeZ0Yhpf7unvv3Wx0dNpL2yqwny-J-KUpXMWoP3MDRpl1Egoyi_J6_yCPiPUtxbqtJvADZ7GxiTmmp-htEKWcXUKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=WTVeUk_N8Pav71XkALh6Dfh_nhfsF0pl3m5nZVAfPS4bGkFxiT8rGvrLuL2ONzUApn8cF1p3JCejk2yRtq5_1D5hExoHcYYvVD8TDaXb_FOB89AGx2dA9bJ1HaqJA3_3PQ47Zb4chs59vk_fqf8tkNQFqs1tXsIg01f2PGcUkT5OjiPCTb3DwLeipxIKf5ZuiZwPghCNoH_dO1VMJmDR0B1KhYNCUFpAelbpMJFPZoDS62DBB_73-JOvoLUqSFeZ0Yhpf7unvv3Wx0dNpL2yqwny-J-KUpXMWoP3MDRpl1Egoyi_J6_yCPiPUtxbqtJvADZ7GxiTmmp-htEKWcXUKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
به تازگی یه چیزی مُد شده به اسم «جوجه پارتی» ، تو این پارتی، پسرا رفیقای دوس دخترشون رو به همراه رفیق سینگلشون به این پارتی میارن، تا برای همدیگه جوجه بکشن و از سینگلی در بیان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71249" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71248">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZ3N3OOOmyu0_qijkXsLRW20lp7RIfMVhZ3K1J7ZKH9xV89ibatPNoA95nDIUHMqhpFcJrq9vVbfff7euZg93yEMJ0IgIw5yYstpxEkbJt6Z14SkS3z9SbutDcYPnMpXHfNfYky5_2ulPFbh83dX7WHO3iWSjAVEQRYTYCWm8UYjVRV8niERX9ruJAfkuzGcyI19yIo2vU6JJtIb8n_qW-3uQoXknBMriMQ9MEwFnQ0gOxsSGKsm0jzns6qRjvBCII5M4b9SoT-WBWe1WGh9PogdJCz1q4mtz5d8B0or8tdaCpBnRygtPU4BVmk_bucb4f7tCH2bTH2W5KQrYAyhGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71248" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71247">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71247" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71247" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71246">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpHfbMjZ502j-NWWHdJxcsldDbf60Up3VqaAo5Iv_LwLnUrb18m-obbGb8dC2YtpXiaU8ftvHEAaUfqVMRAhk0jgrGq77mp_BMzDGo9c9iOkc9ouJ5tdl778JXXTnDQ39gDVkVBU7MbIBSV3IFfyGxCzQpcrk9Un3wM0LyvyU8E5AVkGjPCy1J-AHxn3eTrxH5IKZscUfpKJWTPIQ4qN5FYTsf_5Ml90LFpL-mIAev3Kxzw6_79XCP3Aqh58cqIphQbTXk4M4zpnn_f-hxBWuDd9ZoWDbPe2cjh6tf0D2QdAem15PoFUPelT6exu6WXn-fBd1Mo1w9G-yXq_q3jGsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71246" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71245">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">▶️
🇱🇧
🇱🇧
این ویدیو رونمایی شهر موشکی عماد است که مو به مو طبق شهرهای موشکی و پهپادی سپاه پاسداران ساخته شده؛
دو سال پیش حزب‌الله لبنان از این شهر موشکی زیر کوه‌های علی الطاهر رونمایی کرد.
جمهوری اسلامی بیشتر از خود حزب‌الله لبنان خرکیف شده بود؛
از برنامه ثریا تا اخبار سراسری صداوسیما تماماً افتتاح شهر موشکی عماد با ۴۸ کیلومتر تونل بود که مدعی بودند ساختش چندین سال طول کشیده و اکنون تسخیرناپذیر و نفوذناپذیرترین دژ عالم است.
این شهر پس از سه ماه محاصره توسط ارتش اسرائیل سه شب پیش در سکوت خبری تمام رسانه‌های جمهوری اسلامی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71245" target="_blank">📅 19:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71244">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=CS2_oafNwTfYxilOT2PRZNaDocvnU1QnQPCPV6uOpCpQuWXGPoUHhhLBbelB9imZI-17KHCBxfOOfXERRWa0TvS7_Ptjb7a14_FX3FDoWr4cs6la0cIvIXRfPo6xUadlCiLW6tcW9VIa1tte7OFjugtrrRIHQnGrat2ImCr6zWy9SZcI8Bv0bRJbgejMWg1gnN1LQ-5Di1U7qIK6Kn3TOAhfoPALRbxRIkR3VZKmAMUTcPsfJwmnXCbY_DFf_RaDcm3Sb8QHsHVFvcIrSxSbvQSLTEvzd3PovO6bVTPmNYW8JaRYN93yYzlcuRNOEaIkrDKBPs0AIOL5VHUlyifWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=CS2_oafNwTfYxilOT2PRZNaDocvnU1QnQPCPV6uOpCpQuWXGPoUHhhLBbelB9imZI-17KHCBxfOOfXERRWa0TvS7_Ptjb7a14_FX3FDoWr4cs6la0cIvIXRfPo6xUadlCiLW6tcW9VIa1tte7OFjugtrrRIHQnGrat2ImCr6zWy9SZcI8Bv0bRJbgejMWg1gnN1LQ-5Di1U7qIK6Kn3TOAhfoPALRbxRIkR3VZKmAMUTcPsfJwmnXCbY_DFf_RaDcm3Sb8QHsHVFvcIrSxSbvQSLTEvzd3PovO6bVTPmNYW8JaRYN93yYzlcuRNOEaIkrDKBPs0AIOL5VHUlyifWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از لحظه فاجعه انفجار تانکر حمل سوخت در سنندج که باعث مرگ 11 نفر شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71244" target="_blank">📅 18:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71243">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=arxu8CaEnlLpzuZt9QDzNyqJWZ5lLzINb3172LUNCTQ9_FMQ9yjuTvlMmuTmMQNAF6EK3nqUL8_Sy3Qk1ITf7BljT-TXEA17FcOBqP_GvbP_nx2XeTcyRkBe7A-WQt_7e6thwJEJyBs8vw1zYdNfWBsijnn_FkuFU_vp68DiOraTkybNDmUayS7cZtNUbwpHaLeqm3MbcHJeilJlqRMLwK0gici5IaiXyfbm4Xp1LU3D7-OzqGwB5HkVA9zsvhxFGrV8fQaBPiF9y1gKK08mfSv9Iqe9KBnFcBySYEJKXZVjq3LGGT8q7WZnmcJW7643_CxPIoiOF9u-u1u5RBuCWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=arxu8CaEnlLpzuZt9QDzNyqJWZ5lLzINb3172LUNCTQ9_FMQ9yjuTvlMmuTmMQNAF6EK3nqUL8_Sy3Qk1ITf7BljT-TXEA17FcOBqP_GvbP_nx2XeTcyRkBe7A-WQt_7e6thwJEJyBs8vw1zYdNfWBsijnn_FkuFU_vp68DiOraTkybNDmUayS7cZtNUbwpHaLeqm3MbcHJeilJlqRMLwK0gici5IaiXyfbm4Xp1LU3D7-OzqGwB5HkVA9zsvhxFGrV8fQaBPiF9y1gKK08mfSv9Iqe9KBnFcBySYEJKXZVjq3LGGT8q7WZnmcJW7643_CxPIoiOF9u-u1u5RBuCWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
طبق قانون، استیکر و گیف خنده داری که از رفیقت میسازی جرمه...
و میتونه ازتون شکایت کنه و تا 1 سال حبس و 5 تا 33 میلیون جریمه نقدی داره.
اینکه شوخی بوده هم هیچ تاثیری تو مجازاتش نداره
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71243" target="_blank">📅 17:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71242">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06303045.mp4?token=rBqvAoAjVHaQQ_ShINAJa6oiOOIzouluTvKfhQX0cchgUugfFrjujsARacObqODJpxC_32ombbznI4OnhQtnC1VvY_OrbfBB6DXTtcjj4ZyqIWKpM27yh6zUgJiXusIJDUlEsQEy7hdRqFKrmbNwVoacGTZm-KK7M_R20XrOAtFn9M-dX_UC121qnmGCz46KQsc8JlVm3UOrhpoOEitRbKwAYd8bOlxlYGfSEEJ3wdWymmFNvqp3lnmDCqspHNw4zB1DmVmzwgvSTEILbTP966t4spZV4xZMDZUTKwa0E0tTZfZZX2ndDwu1hgcOg5vavv8VnTeXwySfFFdQAiDoVpHmr5Hr89_9cMuqaBTY9-mqDEDmioD_9UXJEfPEpCzpV0chYsFrQsgQnE8XMIabaXefbiJEI8G6VjGqMVv8nE-bLAjeg3c6DKYM5TsvGWePEhB5Ccb_cyhacm_isxTwxUXDem67syGHS7dAQQkn9tQyYhB6Sk3ryL0R26vtTfUb8nSX6xFvm4zV6UNXPOyPnZDNjk3vk2CUrQnYgvR1Y--IyDV8Y8DqmL8MoeH5Bd3JNHTZVCS-KQ7EYXWL68bN26E-e8FA3kh4tXaopwAjy1HbXLp6TnxOHIcES6z9dvQRw2mmn-i0U3JzE--t7PNluSLh8-l0a0u6uWnOxXO54VU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06303045.mp4?token=rBqvAoAjVHaQQ_ShINAJa6oiOOIzouluTvKfhQX0cchgUugfFrjujsARacObqODJpxC_32ombbznI4OnhQtnC1VvY_OrbfBB6DXTtcjj4ZyqIWKpM27yh6zUgJiXusIJDUlEsQEy7hdRqFKrmbNwVoacGTZm-KK7M_R20XrOAtFn9M-dX_UC121qnmGCz46KQsc8JlVm3UOrhpoOEitRbKwAYd8bOlxlYGfSEEJ3wdWymmFNvqp3lnmDCqspHNw4zB1DmVmzwgvSTEILbTP966t4spZV4xZMDZUTKwa0E0tTZfZZX2ndDwu1hgcOg5vavv8VnTeXwySfFFdQAiDoVpHmr5Hr89_9cMuqaBTY9-mqDEDmioD_9UXJEfPEpCzpV0chYsFrQsgQnE8XMIabaXefbiJEI8G6VjGqMVv8nE-bLAjeg3c6DKYM5TsvGWePEhB5Ccb_cyhacm_isxTwxUXDem67syGHS7dAQQkn9tQyYhB6Sk3ryL0R26vtTfUb8nSX6xFvm4zV6UNXPOyPnZDNjk3vk2CUrQnYgvR1Y--IyDV8Y8DqmL8MoeH5Bd3JNHTZVCS-KQ7EYXWL68bN26E-e8FA3kh4tXaopwAjy1HbXLp6TnxOHIcES6z9dvQRw2mmn-i0U3JzE--t7PNluSLh8-l0a0u6uWnOxXO54VU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
🇰🇵
روسیه و کره شمالی یک پل جدید را در امتداد رودخانه تومن افتتاح کردند. این پل دو کشور را به هم متصل می‌کند و با گسترش همکاری‌های نظامی و اقتصادی این دو کشور، اهمیت این اتصال نیز افزایش یافته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71242" target="_blank">📅 17:05 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
