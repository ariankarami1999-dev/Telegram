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
<img src="https://cdn4.telesco.pe/file/iZsXwPdPZ052qUWAgpQndPbZKpmRboQsNroInN6az79fTNcIErNv3xGA-NW-N5ILa52Cv3B6I8hlnQDQIWJkX_6-3-yipmukXmguPF_4BjDLQPqwhE-L2t-bFo_i1r0vu4ZfAeYNfkbM2BHxiQrDLeGxLovVEndaNI_4XbpN2iMP87p-VOEF59p47tcWvZZf1peejuzab0rIbM9gEw4vAOc2NfgdcyhrYXUd8SmaTwDIBQCUR0ZGmoiWwg8W1AiLnhqDNR2iSD8wGQfkiVZ6rdIfGUC1Lbtef8_EcHUIyowv8DrqF9_UswhrIC-Ogw_Tt6aDIvF9x6-2b5VUGFy53Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-694012">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxc1mim7R-DvJr7A2Td8lgESO0TTddcbXNOyziMnh3ZEh0LmBPpn3ZM6lOnIWF4Fy_KzxuNnNC1X0hDXewRa3mYBeVwJ4YEqoxS_0JcrZuH8H4f1wnNt2h_rAh_07pWMfW2xr3Rv2GzqUM3amaBxLWT0hb-dJaAhJ02rtuNtS0x2FGfojICgpuUSTrXoIHOFa374wv0f9dHZcQqCDrljvnxf_C5HV5tCkD2pr8XQFEWOjHCtga8zPqc9yI_H3zfgVDqrOakGMpxZUUf7mlY95BrjPZ0oxVu-I_ZsJgoW5NZxcQKm1gtqWm-gcfLgjtfVdieHp9xOw6cLO4LS7Ged_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش آمریکا شروع به بازگرداندن هواپیماهای سوخت‌رسان و قرار دادن آنها در فرودگاه‌های بن گوریون و رامون کرده‌است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/694012" target="_blank">📅 18:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694011">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0MLR0TB7vrNs4iItArCpHFmnM8J5Gfx7YnPpCKhSxnqOeyE50vWnuwSd-6azZchc8NVwaSPcWGUWFpRpSFluJoXU-sy-6v4yll0fUZEU0gdF0BK1hkC78jCexU7GHYLTbbzm3Ca8Og8lRzNfmbbI0JuyFgJS02lh2wRnD21zMWZTOhzaGDXTL1Y4UbfvyegL17LvbYOk_LnJgeCEyg2N2LVRsUGm65MzNCvJ6LJtVcS6Dm_3r3i6w5eygYgeT3oRJAEcXftEkPH7rBBOW_h9QrvfRRncBuAdak3Eqa1FPG65r9TFeovSVOrp-N0ckCRnm8rmTleK1hdD4ORmGE69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل شخصیت از طریق گروه خونی
🧬
🩸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/694011" target="_blank">📅 18:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694010">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnUVIfRK7AXd9AzcW8IBlZbBevJg9czYMKP1qurekbJzjdYmUyVg3BzH1yIi7VE259wC6eHnhjQJNeSbvryzRrxY434oM7ocMN-t4MyTzGooWFTrN3jZLVHdoz_Bc8X5Hlbt7Uyd8gu3SSJwgCJq1ZJc3PwlZIB-XLq-S-RvgUJeADig0ur_RJRZiPZVVc-XVEStvxqjRYEZRtA97G9fAG5IsknkaJp4E7480sFv9d8eYqEeK6PoFt1HQmx2vyPx1lEOxA4Cd5G1VHC3VkBBFMuQ14Q_g2xI0jpF4pKhTQvG7d7zkUZX5lDlk5eLkjdtUnxm7PsSi1zPzNbRfr9VGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درآمد ریالی اپراتورها با هزینه دلاری شبکه همخوانی ندارد
🔹
علی ذاکر، رئیس هیئت‌مدیره انجمن کارفرمایی شرکت‌های سروکو، می‌گوید درآمد ریالی اپراتورها با هزینه‌های دلاری توسعه و نگهداری شبکه همخوانی ندارد و افزایش‌های مقطعی تعرفه هم نتوانسته این فاصله را جبران کند.
🔹
تورم، نوسان نرخ ارز و هزینه‌های ناشی از قطعی برق، فشار بیشتری به اپراتورها وارد کرده و توان آنها برای نوسازی تجهیزات و توسعه شبکه را کاهش داده است. نتیجه این وضعیت هم در افت کیفیت خدمات و قطعی‌های مکرر به کاربران منتقل می‌شود.
🔹
اصلاح تعرفه‌ها به معنای گران‌کردن خدمات نیست و این کار، برای حفظ توان سرمایه‌گذاری و بقای شبکه ضروری است.
🔹
در کنار اصلاح تعرفه‌ها، تنظیم‌گری بهتر، اشتراک‌گذاری زیرساخت‌ها و جلوگیری از سرمایه‌گذاری‌های موازی هم مهم است./خبرآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/694010" target="_blank">📅 18:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694009">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
اکسیوس درباره ایران و امریکا مدعی شد: شکاف‌هازیاد هستند. فکر می‌کنم رسیدن به یک توافق نهایی برای میانجی‌ها به یک معجزه نیاز دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/694009" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694007">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/492bab73b4.mp4?token=aGZaasGZ5t7SWSuLmwosqtKwaR5bUC3vtQhNLASV0kb4fH6M1brUWVTG5NVqcyXp2ldBiTQH0iZT_MVzGZnWud4guSj2tKtwBliR8L4qlkwNFUKIAEuBDL9NLSd4xSEpbEn2PeG7StgPNQZ8l9Bg94glXBa-rKr2u43D79WgNpeU6eOpwVRZe6UcSyZrI9xjsVdsYnMdOnAGYFQRmOwxhdC6Kk8oA08tYRA0Mk14dJsBrLoTF4D8XkCCRW8J7g0e6Q5WwkUwQGasZbh8Su_ipt27E5-gKiuHGu2QMb61Pm_R8_wBhF8trOoEghY-TENQScBP47d4J5lkZOflyAurEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/492bab73b4.mp4?token=aGZaasGZ5t7SWSuLmwosqtKwaR5bUC3vtQhNLASV0kb4fH6M1brUWVTG5NVqcyXp2ldBiTQH0iZT_MVzGZnWud4guSj2tKtwBliR8L4qlkwNFUKIAEuBDL9NLSd4xSEpbEn2PeG7StgPNQZ8l9Bg94glXBa-rKr2u43D79WgNpeU6eOpwVRZe6UcSyZrI9xjsVdsYnMdOnAGYFQRmOwxhdC6Kk8oA08tYRA0Mk14dJsBrLoTF4D8XkCCRW8J7g0e6Q5WwkUwQGasZbh8Su_ipt27E5-gKiuHGu2QMb61Pm_R8_wBhF8trOoEghY-TENQScBP47d4J5lkZOflyAurEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ تروریست: جنگ علیه ایران یکی از مهم‌ترین کارهایی است که انجام دادیم
ترامپ:
🔹
در سال‌های آینده، کسانی‌که تاریخ کشور ما را خواهند نوشت  خواهند گفت که جنگ علیه ایران یکی از مهم‌ترین کارهایی است که ما انجام دادیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/akhbarefori/694007" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694006">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6b96753e.mp4?token=UsDT3HbsdU1QGPTYkbbS6lrtX0LQOoj2AArNssA6whZNvqzxOYlvd-4dT4BMYCnBkviYyBgO7PX-KY4TXpsb1wJnuLlkUmMJl-gSB-A5TppRVid3x_5Y4JbMIGkhZO9J6Ei7Nw9ESzIe0dqgbUHbNxwVqusns5fjGtznhq-V1xsvDfvG9UwVCZuDlKhnvO0w0HTOqCuCLFpuz-YJiT0O9iRonFYDilKFjhvN_Xu5R97h6ZL5r-EGM72kpe-o-PsvfABOnXATFa9hezkgJeWL-DD_mPxpjp81HdghTsEEFIv444nbp1f4VGiN5t7HSx9m-eyOU76_5-l-ENhLujZurw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6b96753e.mp4?token=UsDT3HbsdU1QGPTYkbbS6lrtX0LQOoj2AArNssA6whZNvqzxOYlvd-4dT4BMYCnBkviYyBgO7PX-KY4TXpsb1wJnuLlkUmMJl-gSB-A5TppRVid3x_5Y4JbMIGkhZO9J6Ei7Nw9ESzIe0dqgbUHbNxwVqusns5fjGtznhq-V1xsvDfvG9UwVCZuDlKhnvO0w0HTOqCuCLFpuz-YJiT0O9iRonFYDilKFjhvN_Xu5R97h6ZL5r-EGM72kpe-o-PsvfABOnXATFa9hezkgJeWL-DD_mPxpjp81HdghTsEEFIv444nbp1f4VGiN5t7HSx9m-eyOU76_5-l-ENhLujZurw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکرم خانم، خواهشا حنا روی سر او نگذار؛ خواهش عجیب سردار آزمون از همسر بیرانوند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/694006" target="_blank">📅 18:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694005">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/694005" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694004">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ویدئویی از لحظه انفجار در حلب/ هنوز علت انفجار مشخص نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/694004" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694003">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سخنگوی ارتش: اگر بفهمیم حملۀ دشمن نزدیک است، حتماً عملیات پیش‌دستانه انجام می‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/694003" target="_blank">📅 18:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694002">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: روز پشیمانی کشورهای همسایه بزودی فرا می‌رسد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/694002" target="_blank">📅 18:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694001">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeyHNXgKnVdE3o0Y1H8LUi3uNhp_NX8uT1Y-sHdNuwUYZ0LfqsgEaZO_x759YN4twns8u8wE_Ml9ER1at_kFUzjApWH-HIYEbjLvcBitUyIy1zXnJOkrqUXpw560y4lp5npQZMlaO4uwXL7NqS49lM9r3U3KnPjreSKQNMik5LXJPh8hMbTN09M5OHptsUKutZlh_GqC-7lz3r2QQyooNpcrUsuXxe3bW8V96rXRBJIW71ueNCExXpW2Rsm5a9umoHHIktaeDmQRYUF4OZ5EwMzXj6MOF7c3piT2J5BMhLOKpi3Y7P3NhXO_GjnXr5jAtbZcjvLWtKUwEC1nSsKUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در این پست با چند جفت کلمه‌ پرکاربرد آشنا می‌شی که خیلی‌ها فکر می‌کنند هم‌معنی‌اند و اشتباه به جای هم استفاده می‌کنن! #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/694001" target="_blank">📅 18:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694000">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fff281272.mp4?token=l02R6K-h7Ra_Rf-nO3WENuelR6UsBYOrEdCxZDjfS8x99r0X5Jh0vV3jk5RBAmcLUWNqM7DnoIibedJtzcXl5EfzHdBzV5jUq-tVILKURoBk4PG-0v-Mcm-iR8VgodDmCOHdraS1_RDWZThp3Z4xpJhvJu3xTh6jSAXa83AxqtVLMWYg3_8jtEFefA7fyX8PZ5DEIFfOGpXp3Wh9vKStDQG70kGhJywYPu4ILINymh54Zq7i2U7bFJs_3mJxmRvKjufR9mRS2ZGqxJGVjUbxkI_hzC6b7L7fYROMVVl4QrDPdceSOwtQDw9d8IIUp2rdrC4l_WwkfB_OUJFfaF_Icw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fff281272.mp4?token=l02R6K-h7Ra_Rf-nO3WENuelR6UsBYOrEdCxZDjfS8x99r0X5Jh0vV3jk5RBAmcLUWNqM7DnoIibedJtzcXl5EfzHdBzV5jUq-tVILKURoBk4PG-0v-Mcm-iR8VgodDmCOHdraS1_RDWZThp3Z4xpJhvJu3xTh6jSAXa83AxqtVLMWYg3_8jtEFefA7fyX8PZ5DEIFfOGpXp3Wh9vKStDQG70kGhJywYPu4ILINymh54Zq7i2U7bFJs_3mJxmRvKjufR9mRS2ZGqxJGVjUbxkI_hzC6b7L7fYROMVVl4QrDPdceSOwtQDw9d8IIUp2rdrC4l_WwkfB_OUJFfaF_Icw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه در کمتر از  یک دقیقه به خواب برویم ؟!
😴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/694000" target="_blank">📅 18:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693999">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvJKrIRvfywTyjOe1waWAJpqVUpXYiPjFu5u-pXbm4JoBkrCD3wTe7bhiddEF7kthEw0ux3_s2gSxoo20UdIEVxa9qAFmYCiGIZ2GemZdstCRqN-TDM3Yw0rRIGDzdCQPp-RmEBEWOq9FYnF9cTs3hh-OUkWFbvIkRpbcA5GsW-zL5jzFKeF4m4_lxZuvIB1nukNez_05-wMwDPUKvT6edR0_XtI-j6O-gF5uKg_AgmgmNiJFDzFoAUalTFkgWFfCFe926ySK56IHcCHjYHa7PtfyuCfN3hQyeEJEng2WbniNDAeleWPVnKvCNLMvlNDJAfqbcSyxhGH1p9OEnnWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بر اساس گزارش عملکرد سامانه «فواد ۱۲۸»
بانک کشاورزی رتبه نخست سرعت پاسخگویی در شبکه بانکی کشور را کسب کرد
🔻
بر اساس گزارش عملکرد سامانه فوریت‌های اداری (فواد ۱۲۸) در شهریورماه که از سوی علاءالدین رفیع‌زاده، معاون رئیس‌جمهور و رئیس سازمان اداری و استخدامی کشور منتشر شد، بانک کشاورزی با ثبت رکورد ۲۸ ثانیه در رسیدگی به درخواست‌ها، سریع‌ترین عملکرد پاسخگویی را در میان تمامی بانک‌های کشور کسب کرد.
🔻
میانگین زمان رسیدگی و پاسخگویی به درخواست‌های مردمی در کل شبکه بانکی کشور طی شهریورماه «۲ دقیقه و ۳۷ ثانیه» و میانگین کل دستگاه‌های اجرایی «۲ دقیقه و ۴۶ ثانیه» بوده است. مقایسه این ارقام نشان می‌دهد سرعت پاسخگویی و رسیدگی به مطالبات شهروندان در بانک کشاورزی بیش از ۵ برابر سریع‌تر از میانگین نظام بانکی و دستگاه‌های اجرایی کشور بوده است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/693999" target="_blank">📅 18:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693998">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYJYBCCYFk6VYwSB56SHv7MsKFjCm2cEDjHhAxWTwfjoO-KYX_eGKqbTeguRgZ5oS-HY99Gij0srBStjBDNf3WUT7WKix9q_6NGjoK2ENs6eD7u3iv8KqwqFE5RGHcO6CoGbBkjTM4ovpuZjbuoT_VoCVmxfoxdn2sk-TSPFAdU3kKdl87c14k2C0OsyQHyZIUEKP5XILROpGX_eVzkvLuIXyQWOlIp7k6hMD1_dYMIYJLCCtOJXaMGNzxAXtovTfnlD44J-bMBec_Sy4Wr9EHJfjusN6HfgKLsNsXubzQ6sU28yPBYgkjHHu-FJNn5GYfABn60mr8bpeLxA5FtoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمدبیگی: هیچ مدیری حق ندارد در مسیر تولید و اشتغال مانع‌تراشی کند
🔹
دکتر فاطمه محمدبیگی، نماینده مردم قزوین در مجلس شورای اسلامی، با تأکید بر حمایت جدی از سرمایه‌گذاری و تولید گفت: مدیران دستگاه‌های اجرایی باید حامی تولیدکنندگان باشند و اجازه ندهند بروکراسی، تعلل و ناهماهنگی اداری، اجرای طرح‌های تولیدی و اشتغال‌آفرین را کند کند.
🔹
وی با اشاره به احداث کارخانه دانش‌بنیان ۷۵ هزار تنی آب اکسیژنه در قزوین افزود: این پروژه با بیش از ۶۰ میلیون دلار سرمایه‌گذاری بخش خصوصی و حدود ۵۰ درصد پیشرفت در حال اجراست و پس از بهره‌برداری، بزرگ‌ترین ظرفیت تولید آب اکسیژنه کشور در قزوین شکل خواهد گرفت.
🔹
این طرح ظرفیت ایجاد بیش از ۲ هزار فرصت شغلی را دارد و می‌تواند در کاهش واردات و توسعه صادرات نقش مؤثری داشته باشد.
🔹
محمدبیگی تأکید کرد: وظیفه مدیران، حل مسئله و برداشتن موانع تولید است و مجلس نیز با استفاده از ظرفیت‌های قانونی و نظارتی، عملکرد دستگاه‌ها در حمایت از سرمایه‌گذاری و اشتغال را پیگیری خواهد کرد./نمایندگان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/693998" target="_blank">📅 17:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693997">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
نقدعلی، نماینده مجلس: بانوان فعلاً نباید از موتور استفاده کنند، زیرا هنوز قانون آن مصوب نشده
نقدعلی:
🔹
اینکه بخواهند با «راه بیانداز و جا بیانداز» کار را جلو ببرند، نمی‌شود. گواهینامه موتورسیکلت برای بانوان، یک موضوع دست چندم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/693997" target="_blank">📅 17:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693994">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
امیر حیات مقدم، نماینده مجلس: در بحث توافق، وقتی رهبری، شعام و حاکمیت تصمیم می‌گیرند، سایر اشخاص باید از آن تبعیت کنند، نه آنکه با طرح اظهارات بی دلیل، مردم را به جان هم بیندازند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/693994" target="_blank">📅 17:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693993">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
روس‌اتم در حال بررسی چندین سایت جدید برای ساخت نیروگاه‌های هسته‌ای با ظرفیت بالا و پایین در ایران است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/693993" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693992">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c80d548650.mp4?token=YznCsExgUDbW5dkFWgMZxelWDM0SOp9YFU4BfD575L65yPWxjPQsiUbu5Pqi-wAIpy9gJuDfpM_0Dh3rHhlTbOHSfb7WObjboQQoEWnvDsHl-9LtEJUjvfyaUsWh4JPC3o97ZLuFUekSElEBRWsynLg6zXIP-acUYTeOlRbkMoPwsOa3CdkvRsaYwJdkUGvJ3o0MBdLIK4QZcNQI1XGOZX-pBUX4JxRkJLvAIFWQtcFhemYKJ5520uAB1OyGK1ihvDrNLdnmsTp571SbRJzfZwsIT5oWgLM__186YWuSPwLjS9GgGSm8P6fhN7NdBGpn5_bYbfC0R8c1qowxqIj2Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c80d548650.mp4?token=YznCsExgUDbW5dkFWgMZxelWDM0SOp9YFU4BfD575L65yPWxjPQsiUbu5Pqi-wAIpy9gJuDfpM_0Dh3rHhlTbOHSfb7WObjboQQoEWnvDsHl-9LtEJUjvfyaUsWh4JPC3o97ZLuFUekSElEBRWsynLg6zXIP-acUYTeOlRbkMoPwsOa3CdkvRsaYwJdkUGvJ3o0MBdLIK4QZcNQI1XGOZX-pBUX4JxRkJLvAIFWQtcFhemYKJ5520uAB1OyGK1ihvDrNLdnmsTp571SbRJzfZwsIT5oWgLM__186YWuSPwLjS9GgGSm8P6fhN7NdBGpn5_bYbfC0R8c1qowxqIj2Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنسرو‌های عجیبی که وجود دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/693992" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693991">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
هیات مقررات زدایی وزارت اقتصاد:
موجودی طلای وال‌گلد، مورد تایید سامانه ناظر و قانون‌گذار است.
🔹
به گفته مجتبی قاسمی، دبیر هیات مقررات زدایی و توسعه فضای کسب‌وکار وزارت اقتصاد،
وال‌گلد یکی از دو پلتفرمی است که به سامانه ناظر بانک مرکزی متصل شده است.
🔹
سامانه ناظر برای جلوگیری از خالی‌فروشی و اطمینان از وجود واقعی طلای فروخته‌شده طراحی شده است.
🔹
بر اساس توضیحات قاسمی، هنگام خرید کاربر، سامانه بررسی می‌کند که به همان میزان طلا در خزانه وجود داشته باشد. پس از خرید نیز معادل طلای خریداری‌شده برای کاربر فریز شده و از موجودی قابل فروش پلتفرم کسر می‌شود.
🔹
در نتیجه، یکی از مهم‌ترین نگرانی‌ها درباره خرید آنلاین طلا، یعنی وجود پشتوانه واقعی برای طلای فروخته‌شده، قابل بررسی و راستی‌آزمایی می‌شود.
🔹
به گفته وزارت اقتصاد ورود وال‌گلد و طلاسی به سامانه ناظر، پیش از الزام عمومی اتصال پلتفرم‌ها، گامی در جهت افزایش شفافیت و اعتماد در خرید آنلاین طلاست.
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/693991" target="_blank">📅 17:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693990">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سامانه رسمی فروش خودروهای دست دوم راه اندازی شد
🔹
سامانه رسمی فروش خودروهای دست دوم با هدف ایجاد شفافیت بیشتر در بازار خودرو، به‌صورت آنلاین آغاز به کار کرد. در این سامانه، خودروها پیش از عرضه، به‌صورت تخصصی کارشناسی شده و در قالب مزایده و با قیمت‌گذاری منطقی در اختیار خریداران قرار می‌گیرند.
🔹
یکی از مهم‌ترین مزیت‌های این سامانه، کاهش نقش واسطه‌ها و دلالان در معاملات خودروهای دست دوم است؛ موضوعی که می‌تواند مسیر خرید خودرو را برای مشتریان کوتاه‌تر، شفاف‌تر و مطمئن‌تر کند.
🔹
برای ورود به این سامانه و مشاهده قیمت خودروهای کارکرده از طریق لینک زیر وارد شوید:
https://mashinaaa.com
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/693990" target="_blank">📅 17:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693988">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSUOB5B7RdALWskoXLY2OW9ZAcLPk4Di_B9pEqkG7vu3w6Ju3D-poDZj0wL9Ap_d4trOLkrqMZWiXE9ugSld9yFmNRJo5pquHST_iarI913vgH-ZxEipnT22mhVyozv4Le9vF1p0BP9cdnYLuWNjlqKyXUQZmQITsHO0JQZavoDNdjAFh02oDMzwcRNWbiqp_jk6GO5sVu88Uhzo4mQY5eijMeXc9FM87Wl1BYc7yQAq6uTNUVpmc-HfTQQJwU9vcJfwBUpgVdMawiulosNzbTCUt3j7DXWvayvEgsrH_RleKGcTeafmQjvT70FrOJXRh6XPga3eMOZ4P66Q6Fb_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین علائم هر بیماری که نمیدونستید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/693988" target="_blank">📅 17:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693987">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
امکان افزایش 50 درصدی صادرات گل از ایران
غلامحسین سلطان‌محمدی، رئیس اتحادیه گل و گیاه در
#گفتگو
با خبرفوری:
🔹
ایران در تولید گل و گیاه رتبه ۱۷ جهان است اما در صادرات رتبه ۱۰۷ دنیا را دارد، یعنی ظرفیت تولید کشور بالا است اما زیرساخت‌های صادراتی باید تقویت شود.
🔹
در صورت رفع موانع صادراتی و زنجیره حمل‌ونقل صادرات گل و گیاه ایران می‌تواند حداقل ۵۰ درصد افزایش پیدا کند.
🔹
ارزش واردات لوازم مرتبط با گل و گیاه حدود ۵۰۰ برابر صادرات گل است و هدف باید تغییر این نسبت از واردات‌محوری به سمت افزایش صادرات باشد.
@TV_Fori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/693987" target="_blank">📅 17:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693986">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c1d4fe451.mp4?token=dQ7_zo5N-6zndpxlXH5yXYaMAWaHbEVZ5iaZgTTfyaFkKGNI0T6f8YlmdxP_ocNeYcZ3OWblHc5r19XXhdVzw7CTt7sfLwwUMVUVl8jC4sWPgUdgwTCSBnO_MjJgXmXKzEngo3mlB66w8PfWXaOYs9dREOwXohipj82ZCseSUgFroDmxq25PGhan3qtQeLiMU7HSAUVb93YDJam0Y1OvztlEHWN2bCD9_OleOrxh66nqHDnzxICU61HLIFA0846Zgq8mXyTa3zwpkIk7bC9I8TnCMiPzSXHLuPStloc5DDjqJE0RdoA6cjXw_uxzGt_ASTaj3BHC6FigtHKzEv_AslkvrYhTAhbeHWr5WBWtuu31JzRokBJ1lBEsDYn2wob06ZFA4jH7Dl9Kyl8bVU08MM3pyMTdh4GhBXmsiACAfCRftxbMrjauKH9QOYH-BaJypGDgUDirTvnPQGgMWDzhltx9mbEh0p5mAHI8yUFKjZ63NcRwNnDCaqI3CU9A1Mm8o13bO1iT9Y0_ixWRSAhgY-ECdarbBx-jGKO8pRZZq8RP53zrjoMvGAhZ1nJGIKs23hgo74STe4GD5MmSPzQMF7hGkps10VpO-lUUwCyvc3WTIQ458aEV5zMhN2Z5YaaQwAo1oTWaFqtwI9M0J9n6bpCfrfVTQ3rt_nDUvSAyxdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c1d4fe451.mp4?token=dQ7_zo5N-6zndpxlXH5yXYaMAWaHbEVZ5iaZgTTfyaFkKGNI0T6f8YlmdxP_ocNeYcZ3OWblHc5r19XXhdVzw7CTt7sfLwwUMVUVl8jC4sWPgUdgwTCSBnO_MjJgXmXKzEngo3mlB66w8PfWXaOYs9dREOwXohipj82ZCseSUgFroDmxq25PGhan3qtQeLiMU7HSAUVb93YDJam0Y1OvztlEHWN2bCD9_OleOrxh66nqHDnzxICU61HLIFA0846Zgq8mXyTa3zwpkIk7bC9I8TnCMiPzSXHLuPStloc5DDjqJE0RdoA6cjXw_uxzGt_ASTaj3BHC6FigtHKzEv_AslkvrYhTAhbeHWr5WBWtuu31JzRokBJ1lBEsDYn2wob06ZFA4jH7Dl9Kyl8bVU08MM3pyMTdh4GhBXmsiACAfCRftxbMrjauKH9QOYH-BaJypGDgUDirTvnPQGgMWDzhltx9mbEh0p5mAHI8yUFKjZ63NcRwNnDCaqI3CU9A1Mm8o13bO1iT9Y0_ixWRSAhgY-ECdarbBx-jGKO8pRZZq8RP53zrjoMvGAhZ1nJGIKs23hgo74STe4GD5MmSPzQMF7hGkps10VpO-lUUwCyvc3WTIQ458aEV5zMhN2Z5YaaQwAo1oTWaFqtwI9M0J9n6bpCfrfVTQ3rt_nDUvSAyxdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو جنایتکار: دشمنان می خواهند قبل از انتخابات اسرائیل به ما حمله کنند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/693986" target="_blank">📅 17:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693985">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سخنگوی سپاه: هیچ شناور آمریکایی در خلیج فارس باقی نمانده و شناورهای آمریکا دست‌کم ۵۰۰ کیلومتر از دهانه تنگه هرمز فاصله گرفته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/693985" target="_blank">📅 17:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693984">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b29cf3393.mp4?token=o1OoOh6kg35LoIPSZ4lcpuAiYKueODQ2EzOx4toGQdG6cTE6MFOBwRXE-bPWVHFqRQhgyudAHEByNfJPCmmh4olH6n902xq85dGVpPvhtmILsSF9iIHeZ2d4PtFUq2QJp5MnaDhTpQ_lEEKGm7XGhjEWUxIGb06a8rEmX7crITuOij2YOSEN3U8KzW5ra7V1oYGanCbwe19jjDPQImuWmeBFUklj2CV8v13u-I6d6v3d6WmgiKkPfyEtiyge58voQkgXrSmTPic-CLGFNi5W62hsvWzGnkuaer70-9TRcS9zLmKlwY66eNsN6BeiBS6XW9GrWWLxyWXK9FvcuJ6jCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b29cf3393.mp4?token=o1OoOh6kg35LoIPSZ4lcpuAiYKueODQ2EzOx4toGQdG6cTE6MFOBwRXE-bPWVHFqRQhgyudAHEByNfJPCmmh4olH6n902xq85dGVpPvhtmILsSF9iIHeZ2d4PtFUq2QJp5MnaDhTpQ_lEEKGm7XGhjEWUxIGb06a8rEmX7crITuOij2YOSEN3U8KzW5ra7V1oYGanCbwe19jjDPQImuWmeBFUklj2CV8v13u-I6d6v3d6WmgiKkPfyEtiyge58voQkgXrSmTPic-CLGFNi5W62hsvWzGnkuaer70-9TRcS9zLmKlwY66eNsN6BeiBS6XW9GrWWLxyWXK9FvcuJ6jCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از درگیری فیزیکی مسافرین در یکی از هواپیماهای کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/693984" target="_blank">📅 17:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693983">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVvHAlTXUFxdS_bE-VKY-HPj3EW5M2ydE8vRgiikRtn4kbXGhAfC4KHAHOX_axtrW-NvGXVbRjus26hhivyKIzMjuKzQvBXQJOr0lx_S4h2m4HPPWqqmxcpPyar8JfNKe2qwBgLOFaf7iOR58Zu6DM43vQEM--cFHXZlMqQdwRheUMroJ3qyMRxpBaJuWZhINKUFIDpsguhmfE56fjrMrqh-Rd2pCko-8Cfh2i4-iLoJKVON8Jl1MuSwJboJnzQnEmmiLQOFfjSHcHqq8iVvosXH74jUEhlnAGKyyJTfXYWxqFkhRrAw3zUdnqOjM7zrx1DCmrcAal1HEZZPFdQ0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتبار ۲۰۰ میلیارد تومانی برای خرید آثار هنری در دست طراحی است
🔹
سیدصادق پژمان، مدیرعامل مؤسسه کمک به توسعه فرهنگ و هنر، از طراحی ابزارهای جدید برای تأمین مالی و توسعه بازار هنر خبر داد و گفت: برای رونق اقتصاد هنر باید هم‌زمان عرضه و تقاضا تقویت شود و زیرساخت‌های لازم برای شکل‌گیری بازارهای جدید فراهم شود.
🔹
به گفته پژمان، توسعه نظام اصالت‌سنجی و شناسنامه آثار، ارزش‌گذاری، بیمه و امکان توثیق آثار هنری از جمله برنامه‌های این مؤسسه است. همچنین استفاده از ظرفیت بورس کالا برای عرضه و معامله آثار هنری در حال پیگیری است.
🔹
مدیرعامل مؤسسه کمک به توسعه فرهنگ و هنر همچنین از طراحی مدل خرید اعتباری آثار با مشارکت شبکه بانکی خبر داد و گفت: در مرحله نخست حدود ۵۰ میلیارد تومان اعتبار برای این طرح در نظر گرفته شده که امکان افزایش آن تا ۲۰۰ میلیارد تومان و بیشتر وجود دارد. هدف این طرح، تبدیل تقاضای بالقوه به تقاضای بالفعل در بازار هنر عنوان شده است.
https://www.tfarhang.ir/_تسهیلات_خرید_آثار_هنری_تاسقف۴۰۰میلیون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/693983" target="_blank">📅 17:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693982">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecbe0f8dec.mp4?token=T1oeHYRayOYubd7SkgxcbQ2jcH7qAneE_fVG8b8zn4FXTYTnzvR77lpEjDWpKseGMDzBLiUe8StXTlgoTmeJe8hh8md0R5TMNsV1O-Z5Ti_MReC44vopygGNkmAFHwf7AbIi--1HT_Pk1PDb-1OdMKoQVhXOJZESodpdGMwd1J9Z8i9dGa_ITOP3-yaeZ3UysAFnILWrYvkjxXFFeWCeOYnwXWxzzZBO_fz71LdaTKbYnMs5qx7ig6ruOzAMQZ885YgUtpBu_7yXZI4_ekC6GI7kZzLMraDIVpc4UOQyt3azJbLyIHXuaupHI2wYmsLdifo9XaMVErItFVon4qAFgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecbe0f8dec.mp4?token=T1oeHYRayOYubd7SkgxcbQ2jcH7qAneE_fVG8b8zn4FXTYTnzvR77lpEjDWpKseGMDzBLiUe8StXTlgoTmeJe8hh8md0R5TMNsV1O-Z5Ti_MReC44vopygGNkmAFHwf7AbIi--1HT_Pk1PDb-1OdMKoQVhXOJZESodpdGMwd1J9Z8i9dGa_ITOP3-yaeZ3UysAFnILWrYvkjxXFFeWCeOYnwXWxzzZBO_fz71LdaTKbYnMs5qx7ig6ruOzAMQZ885YgUtpBu_7yXZI4_ekC6GI7kZzLMraDIVpc4UOQyt3azJbLyIHXuaupHI2wYmsLdifo9XaMVErItFVon4qAFgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه به شهروندان درباره استفاده از طلا و زیورآلات در معابر عمومی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/693982" target="_blank">📅 17:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693981">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حدود ۸۵ درصد خانواده‌های دارای ۳ فرزند و بیشتر، هنوز زمین نگرفته‌اند
رضا سعیدی، رئیس مرکز جوانی جمعیت در
#گفتگو
با خبرفوری:
🔹
در طرح واگذاری زمین یا واحد مسکونی به خانواده‌های دارای سه فرزند و بیشتر، خانواده‌های واجد شرایط در شهرهای زیر ۵۰۰ هزار نفر جمعیت و مناطق روستایی، می‌توانند تا ۲۰۰ مترمربع زمین دریافت کنند.
🔹
تعداد ثبت‌نام‌کنندگان این طرح به بیش از ۵۷۰ هزار نفر رسیده است و تاکنون بیش از ۸۴ هزار قطعه زمین و واحد مسکونی واگذار شده و بیش از ۲۷۷ هزار خانواده واجد شرایط شناخته شده‌اند.
@TV_Fori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/693981" target="_blank">📅 17:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693980">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ایتالیا اعلام کرد که نیروهایش به‌طور کامل عراق را ترک کرده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/693980" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693979">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2240e6fff2.mp4?token=vQjO1yHCiFIlAdtOVzLKnuNFYamijMhvW8qy1doknq-I2lAsjBMbC3qFDRv0HnKIk2aMI4dJolCH_FAqT7MpkLJXuaMWkpaA-J9HZ-n4fQTLLMOF88AnCSMXEDvIGWyCdUSEillVKqj7-VLPXQfbbXKhlJp8NtTua4Ozu1S8F92cQ6bJfpJo5H10Gk0YKJBQBgX0sI2mceXfDsvw0vcpQ46Nt5go0pYgE4ENpnD_rTHTh_HAztCsu5-gn6xDGgvh5lDZhzJpxFD-0wkMGK1_gWr2KTfbt1YZJbke5msUSmQPugu8iTh9U7lXaAWQHDSl3jbAcdYTyvKEfQWW2r4tLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2240e6fff2.mp4?token=vQjO1yHCiFIlAdtOVzLKnuNFYamijMhvW8qy1doknq-I2lAsjBMbC3qFDRv0HnKIk2aMI4dJolCH_FAqT7MpkLJXuaMWkpaA-J9HZ-n4fQTLLMOF88AnCSMXEDvIGWyCdUSEillVKqj7-VLPXQfbbXKhlJp8NtTua4Ozu1S8F92cQ6bJfpJo5H10Gk0YKJBQBgX0sI2mceXfDsvw0vcpQ46Nt5go0pYgE4ENpnD_rTHTh_HAztCsu5-gn6xDGgvh5lDZhzJpxFD-0wkMGK1_gWr2KTfbt1YZJbke5msUSmQPugu8iTh9U7lXaAWQHDSl3jbAcdYTyvKEfQWW2r4tLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معجون گرم برای روزهای سرد و سرماخوردگی
🌿
🍵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/693979" target="_blank">📅 16:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693978">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
آمریکا مجوز محدود پروازهای عراق به ایران را صادر کرد
🔹
وزارت خزانه‌داری آمریکا مجوز پروازهای شرکت هواپیمایی عراق از نجف به ایران و بالعکس را برای انتقال مسافران ایرانی با هدف زیارت مذهبی صادر کرد‌.
🔹
بر اساس متن منتشرشده، مجوز تا ۲۸ اکتبر ۲۰۲۶ معتبر است…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/693978" target="_blank">📅 16:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693977">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای‌ ونس: امکان دستیابی به توافق با ایران وجود دارد، اما این امر مستلزم تعهد این کشور به رفتار خوب و عمل به وعده‌هایش است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/693977" target="_blank">📅 16:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693975">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای نتانیاهو جنایتکار: دشمنان می خواهند قبل از انتخابات اسرائیل به ما حمله کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/693975" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693974">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a46b6b6a9.mp4?token=ioqEXdspWZN_uV22Ha33PRhQxWmO53MV6nQ0SrNC6TxNCkLUauq2tLdEKRrAc9pWbo-SWJFMGbkrvg_5Go2mCtODPSEBno0Q8ybyNauu3LZ4w1ROM7ol5H-81Qzox6DwRCgJlDFiS2ba-YkHuApOzu-IFXxbfq59fQ4vQ-aqUPZKL40MHAl-j3milBF5qw1ZVZ64vX6oD-d3u_FbmmkijI-M-Mb11wtsKbEWi4hXQvV9g7mSgpTN99w7T05zU4_Lpmq_w6-aLgG-oNbjvKSy7u35-8fjSJ6e109GDdJuRU3mYouU8-WuRxYs6PIDD2g2tjG4yKTo8xP4uD3iYvqNzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a46b6b6a9.mp4?token=ioqEXdspWZN_uV22Ha33PRhQxWmO53MV6nQ0SrNC6TxNCkLUauq2tLdEKRrAc9pWbo-SWJFMGbkrvg_5Go2mCtODPSEBno0Q8ybyNauu3LZ4w1ROM7ol5H-81Qzox6DwRCgJlDFiS2ba-YkHuApOzu-IFXxbfq59fQ4vQ-aqUPZKL40MHAl-j3milBF5qw1ZVZ64vX6oD-d3u_FbmmkijI-M-Mb11wtsKbEWi4hXQvV9g7mSgpTN99w7T05zU4_Lpmq_w6-aLgG-oNbjvKSy7u35-8fjSJ6e109GDdJuRU3mYouU8-WuRxYs6PIDD2g2tjG4yKTo8xP4uD3iYvqNzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوه‌های رنگی معروف به آلاداغلار در اطراف زنجان
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/693974" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693972">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای‌ ونس: امکان دستیابی به توافق با ایران وجود دارد، اما این امر مستلزم تعهد این کشور به رفتار خوب و عمل به وعده‌هایش است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/693972" target="_blank">📅 16:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693971">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
محسنی اژه‌ای: شرایط قوای نظامی کشور از وضعیت هر ۲ جنگ قبلی بهتر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/693971" target="_blank">📅 16:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693970">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3IWvmaYORq_kAERP4trlEyadE4z-AoczVRRE_htEFbISpx00pXYAEgnee5QAWC4JyKk-L1D8_bAhkcGH33nGnEZpU_wjStVS_WtHWWZwYKEx4LRU-e3lfHw7nCMakewk5LjWJyd_Z51NqH7YdGgmwXiEw5PFt7-TQ-fX9svM-Tku_Gs8am0nImN2EuOkZIobPNBnMzZCgZoQUizzvK-QoHV6OwnzBMVqlYoOfSkAZGfoudOzU70cnz8yoGOo0CaT98TWTEmrCKaPVd3bBa_XSpnIeTACW6YKeVFRhWlT1Exi70pzKOKnAdVwq9-qBJDAAS9CNbFsP3PRitYFfdeIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رمزگشایی از بوی دهان!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/693970" target="_blank">📅 16:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693969">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b12f3c51.mp4?token=Z6edNNtiuDRcT4t89_vT97GUfw6kA6TknDDVwEXIPyFhWTad-tBSPJP4BHvFDXldxVka0dcraA9qg0b--KTb3W4ByrAXFkwcqKfu2P9VHAiGhRwI3vP_j8xJJ55qSRbaQvfIOlgFl7vxoDG_q4vaRIs0fq9ZLJ7HCMRX0qYm87tBvaK4zApPo_gStSIsjx7ZarkGdmKqTHRug4g9QB902KBsyPu-nralbbH0wCy8cW13z9p5-fh29WeQOXh3Y8Wc7irAjwA1-Cs3p60GQlf_BBRojipmSypYVTB9cmV9o0OxoS0PukqNmBSAjaeCz79CYZ8NXZ9IctfzQfOdB4FdrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b12f3c51.mp4?token=Z6edNNtiuDRcT4t89_vT97GUfw6kA6TknDDVwEXIPyFhWTad-tBSPJP4BHvFDXldxVka0dcraA9qg0b--KTb3W4ByrAXFkwcqKfu2P9VHAiGhRwI3vP_j8xJJ55qSRbaQvfIOlgFl7vxoDG_q4vaRIs0fq9ZLJ7HCMRX0qYm87tBvaK4zApPo_gStSIsjx7ZarkGdmKqTHRug4g9QB902KBsyPu-nralbbH0wCy8cW13z9p5-fh29WeQOXh3Y8Wc7irAjwA1-Cs3p60GQlf_BBRojipmSypYVTB9cmV9o0OxoS0PukqNmBSAjaeCz79CYZ8NXZ9IctfzQfOdB4FdrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا فرزندم از حقش دفاع نمی‌کند؟/ در خانه شیر و در مدرسه موش!
فاطمه باقری، روانشناس:
🔹
برچسب‌زدن به کودکی که در مدرسه منزوی است، حس خودکم‌بینی را در او تقویت می‌کند؛ ترس از تمسخر و قضاوت هم‌سالان، علت اصلی خجالتی شدن اوست.
🔹
به جای سرزنش، امنیت روانی کودک را در محیط آموزشی بسازید و رفتارهای اجتماعی و ارتباطی خود را به عنوان الگوی اول فرزند بازنگری کنید./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/693969" target="_blank">📅 16:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693968">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
روس‌اتم در حال بررسی چندین سایت جدید برای ساخت نیروگاه‌های هسته‌ای با ظرفیت بالا و پایین در ایران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/693968" target="_blank">📅 16:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693967">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQxK20kEUe8vn8RnyI37KG_Ov9-ymFPy-9eFyu-c4fuoN5l9qtDIGKsl4FtVFJAC-knQOpy5DaK3t37ErbSfzKLcVpiAImHhcyxKcU9DKDTB1yFrAk3saIKjxR8FCRRpQa_AuMpucGMTuZkqOLfzf7CNbxtKVu1fcfD8l0T9_wxPeY8WxKxZStj7pTrFYvRqOmdfZSUveflJ5tN59IGgVu657EKBoNcVD_R5isGZNVwWd7Qu3hIpPrYNFs4RNeN257WcW2EAevRqY9iZF-wpSsB_fOFLUwN5Qao0jEgGsBtjD7FgNVVTosF8umr9F9yt7FnKysGMTo_kK0Ak3cBZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد حمله پیش‌دستانه ایران به آمریکا | پنجره گفت‌وگو چقدر باز می‌ماند؟
🔹
علیرغم ادعای دونالد ترامپ مبنی بر رد شروط ایران، تحرکات دیپلماتیک و فعالیت میانجی‌ها برای ایجاد چارچوبی مشترک جهت ازسرگیری مذاکرات شدت یافته است؛ هرچند پرونده هسته‌ای همچنان گره اصلی هرگونه توافق میان تهران و واشنگتن به شمار می‌رود.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3248721</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/693967" target="_blank">📅 16:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693966">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92727ef7c8.mp4?token=QPh_uTigl5snLJnacgYSsENbLd5FevEtHBptuXDAm8LaExcIQt8E8u0bZlx6c6GMXdTwrM8K33_AR1xOBe4FK-6-6b0qVHIdmujoaFglky21YZgIrgSuUvFyvMXAl7NG3x31Bn9Zy1MAxU28aOXr-PvQbpmvgqY1P5jrze6Nt3Vx534GdJzjiPMTExFBovDJbZf0dH2q2l-DxFuGbyr4uuamQJgC9IUqbrSskITOczJxEkdq1HDZ8GVDC5MdGfmt9XnKWCeTZQgPIiOdcc3RHvTlrDh9NP9qgmRf9zRI92-tSjQMg046XZStKYk5Nxkue8SdB1R6d_qGTMEzOxSq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92727ef7c8.mp4?token=QPh_uTigl5snLJnacgYSsENbLd5FevEtHBptuXDAm8LaExcIQt8E8u0bZlx6c6GMXdTwrM8K33_AR1xOBe4FK-6-6b0qVHIdmujoaFglky21YZgIrgSuUvFyvMXAl7NG3x31Bn9Zy1MAxU28aOXr-PvQbpmvgqY1P5jrze6Nt3Vx534GdJzjiPMTExFBovDJbZf0dH2q2l-DxFuGbyr4uuamQJgC9IUqbrSskITOczJxEkdq1HDZ8GVDC5MdGfmt9XnKWCeTZQgPIiOdcc3RHvTlrDh9NP9qgmRf9zRI92-tSjQMg046XZStKYk5Nxkue8SdB1R6d_qGTMEzOxSq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ۲۰ میلیون درمیاری این‌جوری خرج کن تا هم کم نیاری، هم هر ماه طلا بخری #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/693966" target="_blank">📅 16:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693965">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp_k4r1xc9uR78RXPcZKAQO5cexXTUW0Yl9AuRWF4D7joYouf1GgITUeLg6YCybMZg2OHWiL22Qjbv-sGsu3FQ11cMkP8NTsgfq-UAsfxQ-W-YCBkSo4gytwW0H6jFbtXhAZhiW9PstGHHyLpPGGJQNNCX8JUzWvl2BIINHmTnVtxHMIurEPHfBmoK4w_oUeS3EPNHnwi4pnw3HHaENIhYuMTdZ7xa1DitngYTvsugTNukDTyjePBAMdSr7ixCnqshtUk2M2_ZiJtvkmsF14b_ydjPri_5qmA_pX3H84bcEs2jPh1HHqIZBn38c6IbCP0yXB176tgmg0JFcdsg41sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای هدف قرار گرفتن یک ابرنفتکش کویتی در فاصله حدود ۳۱.۵ کیلومتری شرق خصب عمان را تأیید کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/693965" target="_blank">📅 15:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693964">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e48dd8d710.mp4?token=r4fP-FnihWbhkfdQEd4Q7qlmV1zHVKlmxPjQUxcO0AyDVSigd-W5xVZfbIX2K1FY9mHlR1SWl8aA81q8SRBEAE_3DuKp3ASWZeDDv2Jax_9p5zpzyZLkXBKxRp5vslr-TIsT7Nm9UdSUcnXxr7mVqB9O9r6mH0hIkobXYezsIv2hCCpDMxRhuogDPydb4STe5kDZV6M2iFPHDu8pHg1QaNTbOiHGseHTOYe-jXitCSZ8DRyCN5QjEBjvUB8TMx57QH9h_hZgTK5dBN56E37tkcE2nvukbDLTv0rdS7SdBWSBLnDuRfgLhIJMWiDz-NwwEUnRmowv3AEyu3OYQhwebrVSCuz60_wHhsFjYpYaziw0SRyR5JH3jcSwgb95u3cgw70Y3USk66KjTj0SSTUWhIDRjfqMWsM0HcwetxrjQQvD4jj-e50Y1U1iF9Z06BL7Cssbsg9pelXb8xQLgrMe2tlmztSiLwX2wT_8GHYUtv7Gcjed24fbgpYZrOjsMl6dHYnyNy9yuwUPKhbBg8P40CzB39TTfH5b2QasHCxSTg-NZJD98Rl09TRETvlZn_HhQysNcYkvkV8gq02dWx5b5c2c2RgtNjPibMFYy4PtxvMG_OlaijLsF-8Q8F20islGwLV5vOp7qCxftXlXY-pqCnpIDMUiMyxvvJOW5bV4o3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e48dd8d710.mp4?token=r4fP-FnihWbhkfdQEd4Q7qlmV1zHVKlmxPjQUxcO0AyDVSigd-W5xVZfbIX2K1FY9mHlR1SWl8aA81q8SRBEAE_3DuKp3ASWZeDDv2Jax_9p5zpzyZLkXBKxRp5vslr-TIsT7Nm9UdSUcnXxr7mVqB9O9r6mH0hIkobXYezsIv2hCCpDMxRhuogDPydb4STe5kDZV6M2iFPHDu8pHg1QaNTbOiHGseHTOYe-jXitCSZ8DRyCN5QjEBjvUB8TMx57QH9h_hZgTK5dBN56E37tkcE2nvukbDLTv0rdS7SdBWSBLnDuRfgLhIJMWiDz-NwwEUnRmowv3AEyu3OYQhwebrVSCuz60_wHhsFjYpYaziw0SRyR5JH3jcSwgb95u3cgw70Y3USk66KjTj0SSTUWhIDRjfqMWsM0HcwetxrjQQvD4jj-e50Y1U1iF9Z06BL7Cssbsg9pelXb8xQLgrMe2tlmztSiLwX2wT_8GHYUtv7Gcjed24fbgpYZrOjsMl6dHYnyNy9yuwUPKhbBg8P40CzB39TTfH5b2QasHCxSTg-NZJD98Rl09TRETvlZn_HhQysNcYkvkV8gq02dWx5b5c2c2RgtNjPibMFYy4PtxvMG_OlaijLsF-8Q8F20islGwLV5vOp7qCxftXlXY-pqCnpIDMUiMyxvvJOW5bV4o3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سختی های زندگی ساقی زینتی،بازیگر قدیمی سینما و تلویزیون...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693964" target="_blank">📅 15:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693963">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHBO3yFVQq-i76fqG-cw8hsHpXF2b7tyrU8zBHadIPJG6n5Xk2cummqlizE_M_SKGFK4M-KjYIcAVfT7SQyF0xjwvB8M8oaX3ZwFQhSzc_UJbKNoGqt6A-twTFjW6PMi7QJavxJ5FuQ54C-BZrn6SYGB7qE0po3NEkyTQpZ8iHRQJ5nj_0dtLgM1SmVG_1xuhv7H9XoaS1IoViWXc_7PcYMz-eQxmqw0idLtMyEb4pIijmyH9nRPBD11jdrXesjlLUD-2_qzwBWYnhzbZ_1hZZAdJbY2GoorpGM0tPsCXyXIOZUa1g_fQsPBo0VHtCnnPer-DyOpGDhXbdcIcLuGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح حمایتی شهرداری برای خانواده‌های تهرانی شروع شد
🔹
شهرداری تهران طرح «تورم صفر» را برای خانواده‌های تهرانی آغاز کرد؛ طرحی که در قالب آن قرار است قیمت ۱۲ قلم از کالاهای اساسی به مدت ۶ ماه در میادین میوه و تره‌بار و فروشگاه‌های شهروند در سطح شهر تهران ثابت بماند.
🔹
شهروندان تهرانی برای خرید غیرحضوری، کافی است از طریق شماره‌گیری کد #۱۸۰۰*۱۳۷* وارد سامانه شهرزاد شوند و مراحل خرید را دنبال کنند.
🔹
نسخه تحت وب سامانه شهرزاد، از طریق آدرس
https://zaya.io/k4opp
(بدون فیلترشکن) در دسترس است و متقاضیان استفاده از اپلیکیشن موبایلی این سامانه، باید با مراجعه به سامانه شهرزاد یا فروشگاه‌های آنلاین ارائه‌دهنده اپ شهرزاد، نسبت به دانلود برنامه موبایلی و نصب آن برروی تلفن همراه، اقدام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693963" target="_blank">📅 15:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693962">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4df221988c.mp4?token=TgQDv_VOz9CyxaBWBMQpJIRonPfLdIDRA-XaedzG4NpQbx2J_9zzuEkWtM42ImZCehP0_Qvr1DRzHzV227PV26RfT348YYRuY1FMYDDzW3u45B8fzFjdYSmkLn_UsGMIDGrKUumDgbGV3vKecX-CDr2uuhTUTXjMtUeKr0Vq0IvOw_Wng36aaf365WyJw4x72J1hrqwuI07crYHbU064v7A8p5nzYaGgo1OpvSMFX8L9lflYzl8sCRSfaUdiDwFVffbBrAFT2M1We7RY6hpxiNyvBuX6KsBocEKXFeGtBQ_LNXnfSvpO-WxQby_bugxYOvKufIKQMXsyT18gJROabA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4df221988c.mp4?token=TgQDv_VOz9CyxaBWBMQpJIRonPfLdIDRA-XaedzG4NpQbx2J_9zzuEkWtM42ImZCehP0_Qvr1DRzHzV227PV26RfT348YYRuY1FMYDDzW3u45B8fzFjdYSmkLn_UsGMIDGrKUumDgbGV3vKecX-CDr2uuhTUTXjMtUeKr0Vq0IvOw_Wng36aaf365WyJw4x72J1hrqwuI07crYHbU064v7A8p5nzYaGgo1OpvSMFX8L9lflYzl8sCRSfaUdiDwFVffbBrAFT2M1We7RY6hpxiNyvBuX6KsBocEKXFeGtBQ_LNXnfSvpO-WxQby_bugxYOvKufIKQMXsyT18gJROabA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کسانی که از سال گذشته در صف وام ازدواج و فرزند آوری بودند، امسال وام خود را دریافت می‌کنند/ نزدیک به یک میلیون نفر در صف هستند
مرضیه وحید دستجردی، دبیر ستاد ملی جمعیت در
#گفتگو
با خبرفوری:
🔹
ما از کمیسیون اقتصادی مجلس خواهش کردیم که کاری کنیم که صف وام ازدواجی ها به صفر برسد و بعد سقف تسهیلات را افزایش دادند
🔹
اگر در بودجه امسال که برای سال ۱۴۰۶ مطرح میشود ، اگر بتوانند این بودجه را ۷۵ درصد افزایش دهند، صف پشت نوبتی ها صفر میشود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/693962" target="_blank">📅 15:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693961">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq8giK4BbTmZ7bOQDARgDbJ7Y7PMUqG2CptWjJEKPnfHRpTR8xsoA-AIr2l-LrRwBYFb9ZQ1nr_9ouUqexottXc-12vtBFT_oxy4FORdMT9uLfecBXjCKKQitp7Ddpd2X2PAX_OQv7fxr_faj-2FWss2MxHAMIje3FJxe41gnRyVCZlRTILPKxRVTtW_83WURMilpwji7qgc-hIFbm0qA04TNnZySxBQ5Xgv4izDBas4c6iJtDzCPAuAOwCKmS3-4dqHvAVrTzz-qL9SmHUTUv9cCc_s6W02o2mYzmKUbTvQlrgBSEBApL1_vr_hcl5v_38Zet9DaApJT2Y7hdbuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمید رسایی: نه شرمنده‌ام و نه عذرخواهی می‌کنم؛ بلکه در برابر این ملت باعظمت، سربلندم؛ کسانی باید شرمنده باشند که کودتا می‌کنند!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/693961" target="_blank">📅 15:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693960">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
رویترز: نیروهای آمریکایی پس از بیش از ۲۰ سال، تا فردا از عراق خارج می‌شوند
🔹
در جریان این اشغال گری ۲۰ ساله ۴۵۰۰ آمریکایی کشته شدند در حالی که بیش از ۲۰ هزار آمریکایی نیز مجروح شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/693960" target="_blank">📅 15:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693959">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
قطر: در حال انتقال پیام میان ایران و آمریکا هستیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/693959" target="_blank">📅 15:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693957">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
چرا بدن‌مون دندون عقلی رو می‌سازه که اغلب باید بکشیم؟ #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/693957" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693956">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l17FoGNYRp55e-4ehknaFww6r9oAJU2MMHPkAiiZKDCo-YGnNxR--5U9Dllutm47YCERWPuEGblZIgB2TxpRXuHs2qzyUv5dG0GX7lgM_qw1wGY9w8rxFHOwKHyHHJSiyRiak2IcaKi0SnlBbFUJ5_1WityBoNAo5KGOXIvANAVCjqn_nssyRGxmcwCOVNhUHiRJwSkd_Uxm3cKlPSuk55NyVqOsm8KjS7nxA2Lne2BTMOR2007CEmmATEH38zIFjbbGxj1Xg0eB95ViUQ8IH-CSL3n86tWVXJR0qgvGn6z6zGPt6-n6vimk9RZOB1f6p9n7JqyjHPWf56a2sLXzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواص درمانی عناب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/693956" target="_blank">📅 14:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693955">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDRBx-tYaLBJkdiIcvVRQsbHYbDpmnP2m36pJkkhekJGjrB4ogNGPE5okxsbNQmgGd5hMwEE8C-SpSsZWhOVPx717MNk-PrgzFgxm5FpX3sGLGvB1RLjL4XhbJv0VcIQnopOeaID-3Xy8Yth9ohSap0hjSx5usLt064kAfMG0tN3UoFdQW0zr6qJPBepoBZiKkQxIwRwMpIh1mGXM3LcpR9MpLKchzro2RCtVQKu5DRrLHizjFjL-gCHyh6VVab2CM9odr1lYtvaKiVyjVzUHcvQXv92K4EdgJhbdzr1lvJPXrhb4Q4quuZLoRmyubGA3y0awbyczoHjO2f15gmJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه چیزی موجب شده است که رهبری تا این اندازه به جانفدا توجه و امید داشته باشند؟
🔹
پویش ها بسته به شرایط جامعه و قابلیت‌هایشان یا موفق می‌شوند و یا دیده نمی‌شوند. جانفدا ناگهان به نحوی «ترکید» که در ادبیات عمومی مردم وارد شد. مردم با عنوان کردن اینکه:«من در جانفدا ثبت‌نام کردم.» برای خودشان نوعی هویت تعریف می کردند.
🔹
در اصل جانفدا روی امواج قوی ملی‌گرایی ایرانیان سوار شد و آنچنان موفق بود که با وجود بمباران افکار عمومی و شرایط اقتصادی، بزرگ ترین پویش عمومی ایران شد و طبق تمام افکارسنجی های موجود جانفدا در نسبت با تمام کمپین‌های ایران بیشترین میزان فراگیری را در لایه‌های مختلف جامعه ایرانی داشته است.
🔹
همزمان با رهبری آقا سید مجتبی خامنه‌ای نیروی سومی قوی متولد شد که علی‌الاصول پشت امر ولایت می‌ایستادند و همین موضوع موجب شد که رهبری روی این قابلیت تکیه کنند و در بیشتر پیام‌هایی که ایشان منتشر می‌شود، کلمه جانفدا درحال تکرار شدن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/693955" target="_blank">📅 14:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693954">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7074068b0.mp4?token=uVgTnmQchLLYJf35uDatca0Ow3BfyyN9R-Y8CcvEr-fJH8My_sFtiiqE94cDXgO9ruPQussef6cN7gJ7PyNJChpRlUSi72ApbuIfxOoWx9Xr2bpuEJYVGltGzhDsd36ABV185LaQ1h5BvDqH6LPYtvc6D4pew8TXuc6sPzCj0GUMkVaSEWtb-K3_a5HPgXgPhomoXTqB1BGTEsXogEWXJopqtEPS-LSBy53kD7uDq6p0coTZKLXTsL8b_6j1QvwtuFyw4Mlz203viXLyGkumJ6FwIUfmzGt58YB3CX8wh00x8ImoyZH_OxVqBEubCocKPOAffuJN8zqyDl18XNnsbjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7074068b0.mp4?token=uVgTnmQchLLYJf35uDatca0Ow3BfyyN9R-Y8CcvEr-fJH8My_sFtiiqE94cDXgO9ruPQussef6cN7gJ7PyNJChpRlUSi72ApbuIfxOoWx9Xr2bpuEJYVGltGzhDsd36ABV185LaQ1h5BvDqH6LPYtvc6D4pew8TXuc6sPzCj0GUMkVaSEWtb-K3_a5HPgXgPhomoXTqB1BGTEsXogEWXJopqtEPS-LSBy53kD7uDq6p0coTZKLXTsL8b_6j1QvwtuFyw4Mlz203viXLyGkumJ6FwIUfmzGt58YB3CX8wh00x8ImoyZH_OxVqBEubCocKPOAffuJN8zqyDl18XNnsbjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاح پنهان چین در نبرد هوش مصنوعی؛ فلزاتی که غول‌های فناوری آمریکا را زمین‌گیر می‌کند!
محمد رسولی؛ کارشناس مسائل بین الملل:
🔹
با وجود پیشتازی آمریکا در غول‌های فناوری مثل OpenAI، چین اهرم فشاری حیاتی در اختیار دارد: انحصار و کنترل بازار «فلزات کمیاب» که ماده اولیه ساخت چیپ‌های هوش مصنوعی است.
🔹
تسلط پکن بر منابع داخلی و معادن آفریقا و استفاده از ابزار تعرفه در جنگ تجاری، توانسته روند توسعه هوش مصنوعی در ایالات متحده را با اختلال جدی مواجه کند./  تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/693954" target="_blank">📅 14:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693953">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
عراقچی در پایان سفر به نیویورک: تعداد بسیار زیادی از ملاقات‌های این سفر به درخواست طرف مقابل صورت گرفت/ قرار است پاسخ نهایی طرف آمریکایی توسط میانجی قطری به ما منتقل شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/693953" target="_blank">📅 14:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693952">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93e4903d2.mp4?token=LD-KlzHLHlqYGayWFGf26VKHjWPa6Vc4C-RxtcUNw03EJl9g9tyvxcTK35Hn3GihhqgzdseNf8VDJissciv-aP6xvG4VzhnX1XCmfkKnsoE67wR0oflglUyWP_I9qwShqc9qfVdRbff_zZ2pN3-O5gUEPzRgvVD395o8RqrhFerZN6gVwIQif6ttJrNJ1Lj62xpTXl3hNjzk4LhBhnpJnadNCDSEMmNa-BEN4QWrVWhG7f-A1jGrvPX766yy44eTfBXC2Xrq9Y4SRuIvWdQ1nCvYZoECSS0CZ33_L0nuRbmIBDdJOZY2wQkGmdawg0ALmh1lWIf1gr6AiCCc18oRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93e4903d2.mp4?token=LD-KlzHLHlqYGayWFGf26VKHjWPa6Vc4C-RxtcUNw03EJl9g9tyvxcTK35Hn3GihhqgzdseNf8VDJissciv-aP6xvG4VzhnX1XCmfkKnsoE67wR0oflglUyWP_I9qwShqc9qfVdRbff_zZ2pN3-O5gUEPzRgvVD395o8RqrhFerZN6gVwIQif6ttJrNJ1Lj62xpTXl3hNjzk4LhBhnpJnadNCDSEMmNa-BEN4QWrVWhG7f-A1jGrvPX766yy44eTfBXC2Xrq9Y4SRuIvWdQ1nCvYZoECSS0CZ33_L0nuRbmIBDdJOZY2wQkGmdawg0ALmh1lWIf1gr6AiCCc18oRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکنیک تنفسی ۴-۴-۴-۴؛ «تنفس مربعی»
🫁
🔹
در این روش، ۴ ثانیه دم، ۴ ثانیه حبس نفس، ۴ ثانیه بازدم و ۴ ثانیه مکث انجام می‌شود؛ گفته می‌شود این تکنیک می‌تواند به آرام‌سازی ذهن و بهبود تمرکز کمک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/693952" target="_blank">📅 14:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693951">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تخلف محرز برخی دستگاه‌های دولتی در قانون جوانی جمعیت
مرضیه وحید دستجردی، دبیر ستاد ملی جمعیت در
#گفتگو
با خبرفوری:
🔹
یکی از شکایات ما از سازمان امور اداری و استخدامی است که باید ساختار و چارت تشکیلاتی ستاد ملی جمعیت توسط این سازمان تصویب شود تا ساختار پیدا کنیم، اما متاسفانه ما ساختار نداریم.
🔹
این موضوع خوب نیست که به صورت عمومی مطرح می کنم ، این را به عرض آقای رییس جمهور رساندیم و به سازمان بازرسی کشور اطلاع دادیم. در واقع، ما شاکی خصوصی از سازمان اداری استخدامی هستیم.
🔹
دستگاه هایی کوتاهی کردند؛ مانند وزارت کشاورزی که باید یا مهدکودک تاسیس می کرد یا با بخش خصوصی قرارداد می‌بست. مواردی از این قبیل را به سازمان بازرسی کل کشور و دیوان محاسبات منتقل کردیم.
🔹
بر اساس تعداد شکایات ما و تعداد بازرسی های سازمان بازرسی کل کشور حدود ۳۰ مورد کارشان به دستگاه قضا ارجاع رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/693951" target="_blank">📅 14:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693949">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
عراق: پرواز نجف به ایران برای یک ماه برقرار می‌شود
🔹
تنها شرکت هواپیمایی العراقیه، مجاز به انجام پرواز میان دو کشور است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/693949" target="_blank">📅 14:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693948">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIJUu7LH_W64yVJnCWrmkRgIHF-wA4QBkuyLlxbrlihFQh7BiZS7xXi8-xLjkmvWsqdK0qFJCMFxScstY25Tyk2-VUWts-dVqt5SLyi0Lk_FRVeF_W46G-JgO9DMJSpb0YxVd4nAIA8A1Trc6z4Agp8zAriHDoYIwhFGWMLsX5mr188aZElrIWjYhkKk-Sbr4vyr6dOYxl5jTgJRQUotN0bLNc0jy63lw_d8A7Y8guhXA8SkvPWjE6a9JhWvnZPYEhjD44UntlbFmvgUfSVVk1xWjGOaygqNpllJyJoOPRdi4JRCRVEXAhyQoOS3a9vvaJ2MR9gNEWbxIXEu2mY_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گذر تتر بیت‌پین از ۲۵۴ هزارتومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/693948" target="_blank">📅 14:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecff2467e0.mp4?token=oUZOsnpAimohP7JvSwwqjSBgPjWhQYGgvlkcZZHjFzSZOsljg_XvSRWf8ZjjFCg2aU9uUpAqDmdqkOGGKALkzYwMpIeZRyA5wKtqsmVK9142sy_7u6aIf3a1by4vHPrSTVQ0XUzcTRbSn6_fIJktKz5iyi0apxzY5yI2GVIouE-zGGBTEuIpzsMBzBhktQsOjE9aa9xwSMbd7HNTf4inGAsSy3dL0_-1kx0-UCeqRFp6z4K53HnKZ7mqSj2Mnp97AIRTrhlJ6QRbAmrfMeMCJaua42ZgO3n7fHxXefLzerjEW6HO8_5fbSI9RTl9N-romVLeVUsbIa5YiMudSV3oaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecff2467e0.mp4?token=oUZOsnpAimohP7JvSwwqjSBgPjWhQYGgvlkcZZHjFzSZOsljg_XvSRWf8ZjjFCg2aU9uUpAqDmdqkOGGKALkzYwMpIeZRyA5wKtqsmVK9142sy_7u6aIf3a1by4vHPrSTVQ0XUzcTRbSn6_fIJktKz5iyi0apxzY5yI2GVIouE-zGGBTEuIpzsMBzBhktQsOjE9aa9xwSMbd7HNTf4inGAsSy3dL0_-1kx0-UCeqRFp6z4K53HnKZ7mqSj2Mnp97AIRTrhlJ6QRbAmrfMeMCJaua42ZgO3n7fHxXefLzerjEW6HO8_5fbSI9RTl9N-romVLeVUsbIa5YiMudSV3oaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکرم خانم، خواهشا حنا روی سر او نگذار؛ خواهش عجیب سردار آزمون از همسر بیرانوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/693946" target="_blank">📅 14:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693945">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
در معاملات امروز بورس انرژی هر لیتر بنزین ویژه (سوپر) با نرخ ۱۱۱ هزار تومان کشف قیمت شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/693945" target="_blank">📅 14:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693943">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvrkT1XZl70HGEy72lsEuq1578Z36T4A-y3q6FovTTQ2BAk4S-EM86AFGX-f42MXVR2odKrOJMrNg5rbW_TTjSgEJcBliisS6abii40AmYPGFxo60KNo4Fn2RpkZRskp6HoMpOD4bYFlWcXYaP_x00E0NHwuTdaZdNC74WF0dLy5lTEXnORJWDJB2xLJWuTUisBk7vXawkl2VO46pmZ-CIh4PUhigORE9HgSb_X3sVZAY797UjlB5dBZ2QJ73tb2cl1x3DOcOanSEzkpxVyzXztxSmISsVxyumA38eGS-CUAuoleyrhXSrn1pV-HYvZksAA_igN_VipAOghoEx7VkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از دلار ۲۵۰ هزار تومانی؛ سرمایه‌هایی که آب رفت | افزایش ریسک و نااطمینانی سیاسی؛ موج جدید گرانی ارز تا کجا ادامه دارد؟
🔹
بررسی رسانه‌های اقتصادی ایران در امروز سه‌شنبه ۷ مهر ۱۴۰۵ نشان می‌دهد دلار آزاد در آستانه ورود به کانال ۲۵۰ هزار تومان قرار گرفته و هم‌زمان طلای ۱۸ عیار نیز به محدوده ۲۴.۴ میلیون تومان رسیده است.
نظر شما چیست؟ اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3248755</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/693943" target="_blank">📅 14:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693942">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139f185597.mp4?token=WC8fucaV8b3ecMys68ujBp629ziXeycUC1ZqbA_PwIviqHTOkW0AWp5ywBgDfkz47fZ7QnJLYgq4sBhpGxQsO-4tSqYPvnWASoN9l8SiiqZqYN73NQPtb_iQYrgRvTS6JVcQikX1L_cWTEPVkTP9gKJzasT_jRp-qrL0RQVqTONe2EQHrm8AsPTpSvFJGZ8PPm9Kl6uDC68b2e3pYtTxUogMAXQJvwzHdtwsJhAW67UBmKvIDlEh-_1sGvsmCPg8I-86vk5hPKLKHvZ2dQxI8mgBH6o_rjRy48gHJxCceM9e3gKf88OCI-zPAcv5nkNuj7tB_VokT2SYcCyKkeLyCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139f185597.mp4?token=WC8fucaV8b3ecMys68ujBp629ziXeycUC1ZqbA_PwIviqHTOkW0AWp5ywBgDfkz47fZ7QnJLYgq4sBhpGxQsO-4tSqYPvnWASoN9l8SiiqZqYN73NQPtb_iQYrgRvTS6JVcQikX1L_cWTEPVkTP9gKJzasT_jRp-qrL0RQVqTONe2EQHrm8AsPTpSvFJGZ8PPm9Kl6uDC68b2e3pYtTxUogMAXQJvwzHdtwsJhAW67UBmKvIDlEh-_1sGvsmCPg8I-86vk5hPKLKHvZ2dQxI8mgBH6o_rjRy48gHJxCceM9e3gKf88OCI-zPAcv5nkNuj7tB_VokT2SYcCyKkeLyCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فصل ژله‌فیش‌ها در سواحل قشم
🔹
با آغاز پاییز و تغییر دمای آب، حضور ژله‌فیش‌ها در سواحل قشم افزایش می‌یابد؛ شاخک‌های آنها نیز هنگام تماس می‌توانند با آزاد کردن سم باعث گزیدگی شوند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/693942" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693941">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrlSqhRloP_7OeqFcXHKABWPxxt8DZPzl7AehfHY1Sn-vjvHSdKnOJXk1KFa9jtAt0X8Zniob23upHUmcBbmxZN8mdlN7bPniApgbxsqF4ZbV2SzIxOuwTh2Ggz9e74brI28oCjec3DeaYITO0EB5y0qbDZYIpcwKCHujBmo_tUhFWuFBvU3YAa-LhZTqEBKnS0nYGBrr--f4M79hYZ__CCmE3FkuxZm-LKRmSVzV_rtlRfzKzACNV8LzNYbxyNkqvLP9-BtDWqNoS-7wnsCQ4Tq_O1OFsnC31ETT5KLxiI-_4D25XEUeQmR6K2_dfExdXIdM2jZSl2Rxt4qs7oLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بعضی مدل‌های لپ‌تاپ اپل در بازار به حدود یک میلیارد و ۲۰۰ میلیون تومان رسید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/693941" target="_blank">📅 13:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aM5BWcVxiKGq1nzI-vJYrLKgZxNo54lXxMSsPr80yXvGE6f68temcvC6nAevMrc2gbEffOvY_jjfS-ZdqVSiutWVue3TZNlcQB5hdZY4LcDdKAOMJTh7ef8S6TrXsFbgUEU_wn7ZtmoAMp7QSPVtBPE5OFK2zK4Q9evq3UbqW3prmAI0GdZyu-A4Kmgn7zkjbFmVuj5kY3NXGV_yU0PiOl8UfeWwG9bAoYynMrcu3et1FLH3frZ-tk--jrTTNWFUn6rc-Bw3uR3uQCIc1yDnK08lDKP_Qo_YYkl0ETfogUSCaZo08ZfDE9AgAYOjaB2xpne9k-_mso08hx4RJE9fOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
یه وام جدید منتظرته!
💰
✨
💼
مالی پلاس | خدمات تخصصی امتیاز وام
🔹
تأمین و واگذاری امتیاز وام
#رسالت
و
#مهر
🔹
مشاوره و راهنمایی تخصصی رایگان
🔹
همراهی و پیگیری تا مرحله دریافت وام
🔹
انجام امور با سرعت، دقت و انصاف
📌
مالی پلاس؛ همراه مطمئن شما در مسیر دریافت تسهیلات
🔗
عضویت در کانال مالی پلاس:
🌐
https://t.me/MaliPlus1</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/693939" target="_blank">📅 13:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axSXeslgxreXzZKYsa78xbY46RjjapJSGSkccdogwWHlurG6yCiJFze4ylSNIj9sGVGYTzTUJkQIOkR3YXNyzKbq-3h4pCzoBSNq22M2e-pI_BagxnF7aN55DIlSY_K0PAN5FgKrBDy8Xi-jGQ0SyU9AVhKFews24r9mrWsjUXFjcjg5tDNATIa_BeFgcJF6Bxy9syGkJvZnqEMm3lWQxq0ONCl5qLDQUXtWfU79BfxJuHZKVG2HZ4rCuaoYx9rINLjGjAxsHorySJ33XeJhkjiqvF6pnp0EH_t3I6G2Axfow3i9Gk2O5xfcgfIOX6CgrqJGWdhp946FpGtOjSIRMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رأی مثبت مجلس به عملکرد وزارت راه و شهرسازی در حوزه مسکن
🔹
مجلس امروز پای عملکرد وزارت راه و شهرسازی در حوزه مسکن نشست؛ آمارها، اقدامات و روند پیشرفت پروژه‌ها ارائه شد و در نهایت نمایندگان با ۱۳۸ رأی موافق از پاسخ‌های فرزانه صادق قانع شدند.
🔹
این رأی، پس از بررسی عملکرد وزارت راه و شهرسازی در یکی از مهم‌ترین و پرچالش‌ترین حوزه‌های معیشتی مردم صادر شد؛ حوزه‌ای که طی دو سال گذشته، تکمیل پروژه‌های باقی‌مانده، پیشبرد مسکن حمایتی و تبدیل تعهدات انباشته به واحدهای قابل تحویل، در اولویت قرار گرفته است.
🔹
نتیجه روشن بود؛ رأی مثبت مجلس به عملکرد وزارت راه و شهرسازی در حوزه مسکن.
🔹
۱۳۸ رأی موافق؛ پاسخی روشن به حاشیه‌ها، با زبان عملکرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/693938" target="_blank">📅 13:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb7a95c1.mp4?token=vNpcVbi0LtgwQx2hROY9GgvZI0ptc99wklCq6tWFmUOJSLGjV8ELHXPTJsDh_elKXaEIkEZlVWtx61kY_PdpRWtJReR-sTQau187W1edVJgi7PduWlyMSkY_Yug5CGpq_KSjgEGO20zNIND602NaWcBV33qiGxm_AHm3x7qwtnNqrBuffey7mXzmsETPOr_7FyGQwCGnZAsBbb1oPyK26Eo9PMTlsBjQ3SX-o0VhWuuMz0BkbrNiZtKYTi5z9WibO5cnZ5JQRx-ZgFNOgghrSSU06rCH8xZ7rt8rvi6VZHfQtUjD3OSi3VQl_WTd8n1n4mfG9EFt5Vpi01K9BQnISL153Ie52fHMsTKJr-k2e_S_nqaZ1cQfnW788pJYuD5qC-apmwKH8Kmr5bw7YMcSqi1nFUqX9ugBzYZURyOMlsZtUIacUPbEI1f6N87e95Yzv4TIINBBDQCnGgr7Fs8KKI5j0lwywh6hsdbk8USminc6NDQE01hO5efanvJ4YwYwmQGQNYoMfXK9QOEl2Q2nJKk-NIfzLKaCfeqxe-thNRceFu6Oz0TcPRalZj8fiw1NkRWHDTey5zltkQ0PLRYMd9Nrx1-WJ-SmW3oCu9aCmoC4M5n4nP4_06YBYk8YWZR0MyGG2fQ90viWOo-0C4nxOyGSR1yQRFyu2CiYffNBunA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb7a95c1.mp4?token=vNpcVbi0LtgwQx2hROY9GgvZI0ptc99wklCq6tWFmUOJSLGjV8ELHXPTJsDh_elKXaEIkEZlVWtx61kY_PdpRWtJReR-sTQau187W1edVJgi7PduWlyMSkY_Yug5CGpq_KSjgEGO20zNIND602NaWcBV33qiGxm_AHm3x7qwtnNqrBuffey7mXzmsETPOr_7FyGQwCGnZAsBbb1oPyK26Eo9PMTlsBjQ3SX-o0VhWuuMz0BkbrNiZtKYTi5z9WibO5cnZ5JQRx-ZgFNOgghrSSU06rCH8xZ7rt8rvi6VZHfQtUjD3OSi3VQl_WTd8n1n4mfG9EFt5Vpi01K9BQnISL153Ie52fHMsTKJr-k2e_S_nqaZ1cQfnW788pJYuD5qC-apmwKH8Kmr5bw7YMcSqi1nFUqX9ugBzYZURyOMlsZtUIacUPbEI1f6N87e95Yzv4TIINBBDQCnGgr7Fs8KKI5j0lwywh6hsdbk8USminc6NDQE01hO5efanvJ4YwYwmQGQNYoMfXK9QOEl2Q2nJKk-NIfzLKaCfeqxe-thNRceFu6Oz0TcPRalZj8fiw1NkRWHDTey5zltkQ0PLRYMd9Nrx1-WJ-SmW3oCu9aCmoC4M5n4nP4_06YBYk8YWZR0MyGG2fQ90viWOo-0C4nxOyGSR1yQRFyu2CiYffNBunA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات پیک روسی؛ از پله‌ها بالا رفت!
🤖
🇷🇺
🔹
ربات پیک شرکت روسی «اسبر» با استفاده از پاهای مفصلی و چرخ‌های مخصوص، از پله‌ها بالا رفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/693937" target="_blank">📅 13:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
یک فروند بوئینگ ۷۳۷ کاسپین هنگام آماده‌شدن برای پرواز از استانبول به تهران، با حکم قضایی در ترکیه از پرواز بازماند و مسافران پیاده شدند
🔹
بر اساس این گزارش، یک شرکت خدمات هوانوردی ترکیه‌ای مدعی حدود ۳ میلیون یورو طلب از کاسپین است و پس از مراجعه به دادگاه، حکم اجرای قضایی علیه هواپیما دریافت کرده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/693936" target="_blank">📅 13:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
نامهٔ سپاه به مردم آمریکا
سپاه پاسداران در نامه‌ای به مردم آمریکا:
🔹
حساب خودتان را از اشغالگران فلسطین که خواه-ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید! ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.
🔹
در این نامه آمده: «دولت یاغی، کودک‌کش، شهوتران و بی‌خرد را کنار بگذارید، امور خود را به‌جای اراذل به اندیشمندان بسپارید و به آنها یادآوری کنید که دنیا عوض شده است.
🔹
مردم جهان بیدار شده‌اند و دورهٔ غارت ثروت ملت‌ها با زور سرنیزه به پایان رسیده؛ این قرن، قرن غلبهٔ اراده ملت‌هاست. ادامهٔ این مسیر ضدانسانی، سرنوشت دردناکی را برای آمریکا رقم خواهد زد؛ چرا که روز مظلوم علیه ظالم، از روز ظالم علیه مظلوم بسیار سخت‌تر خواهد بود.
🔹
۷ ماه پیش، ارتش متجاوز آمریکا با نقض قوانین بین‌المللی و در جنایتی جنگی، با حمله به دبستان میناب و کشتار ۱۶۸ کودک دانش‌آموز و همزمان حمله به دفتر کار امام سیدعلی خامنه‌ای، رهبر انقلاب اسلامی و به‌شهادت‌رساندن معظم‌له و خانوادهٔ ایشان، از جمله نوهٔ ۱۴ ماههٔ ایشان، جنگی را علیه ایران آغاز کرد که طی آن تاکنون بیش از ۳۶۰۰ نفر، عمدتاً غیرنظامی، از جمله ۴۰۰ کودک به شهادت رسیده‌اند و ۸ دانشگاه، ۳ بیمارستان و ۸ مدرسه بمباران شده است.
🔹
اگر در صداقت ما تردید کردید، می‌توانید با یک سفر کوتاه به هر جای ایران که دوست دارید، حتی تنگهٔ هرمز، بیایید و صحت اظهارات ما را شخصاً بیازمایید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/693935" target="_blank">📅 13:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=KAxgK-b464Lye4t7dtvQmaQK6YvMNyt7-81b40qnEIS8neoAKeFex7qjfFVaX6aZMcpCWKvdgoQcKURhLhE9yrJzdzhoGXmIjU7pqCjhmvL229ad9fxG0duCJNlHiTh1gU_5jRJVqP6UkbhSc2VbcDx2Bq3Af26QW5WiHVJYbx7O9200JlTLZN6bqWiXzZ-HhvOwaNGiRPpJZQBvf8hBQNk28lPDDonHmKEdd9t89Xo8hpnHo44myFobfRHVGKLs2dgeaHqDDDTJBl2SFDjiPsQPa__FsXMZiWov4hNtRrxFrksahdCKDg0AqcHD1Ofqm9yrTRLnGdyEBJFCkN1onUZU8u3CCdNDSHdYbFcBny4-fKvCkqpmQNvqp8TXannSRo0RnBWWJVEAnqwIgk_e59IcW2mpc9ziPmWaxLoJkmu8RleR2SES57g8LczIMeSDs6RodyUqNVNPrWg2ITj0nD7_ygUbGVSCX499d1g-_UX8UoylpwoD5E9mHPhVUSURIYvEmgWNdr18DG0NYxw3mZ-isLhoWvwFLufgGif72kaASACbEkNES_L6JaJGT1Hkbi4IhwLPwQd3iEpfaN35JF-Acdv5skk26GwguhJeL4OsIrgizn8mXRnUIPT5vhbvHzi1pRtKtOJw7I9fDtw6wedjB-j_CDfE92xQ0t31Pz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=KAxgK-b464Lye4t7dtvQmaQK6YvMNyt7-81b40qnEIS8neoAKeFex7qjfFVaX6aZMcpCWKvdgoQcKURhLhE9yrJzdzhoGXmIjU7pqCjhmvL229ad9fxG0duCJNlHiTh1gU_5jRJVqP6UkbhSc2VbcDx2Bq3Af26QW5WiHVJYbx7O9200JlTLZN6bqWiXzZ-HhvOwaNGiRPpJZQBvf8hBQNk28lPDDonHmKEdd9t89Xo8hpnHo44myFobfRHVGKLs2dgeaHqDDDTJBl2SFDjiPsQPa__FsXMZiWov4hNtRrxFrksahdCKDg0AqcHD1Ofqm9yrTRLnGdyEBJFCkN1onUZU8u3CCdNDSHdYbFcBny4-fKvCkqpmQNvqp8TXannSRo0RnBWWJVEAnqwIgk_e59IcW2mpc9ziPmWaxLoJkmu8RleR2SES57g8LczIMeSDs6RodyUqNVNPrWg2ITj0nD7_ygUbGVSCX499d1g-_UX8UoylpwoD5E9mHPhVUSURIYvEmgWNdr18DG0NYxw3mZ-isLhoWvwFLufgGif72kaASACbEkNES_L6JaJGT1Hkbi4IhwLPwQd3iEpfaN35JF-Acdv5skk26GwguhJeL4OsIrgizn8mXRnUIPT5vhbvHzi1pRtKtOJw7I9fDtw6wedjB-j_CDfE92xQ0t31Pz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی ارتش: اگر هر بانوی ایرانی یک سرباز آمریکایی اسیر بگیرد  ۱۰ میلیارد تومان جایزه می‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/693934" target="_blank">📅 13:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693932">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAvq-cWpuyzMSW_STB0o6b8tQ0OBpjb5aKk2m7_XITilh4yOPY1SxTcPOtvZAgcYXALPy56Qh8X3UGSzhICKUyxrYHu9TH6j8CP4To5FBB-p2n0JhIYVpOf-ORtdovBVCqQDVR9DUduIjlVlDtsPeIPJS07lI-N9dDl2ESwNLoCrhXdZgcmeC0Z3ngrJRsipPqgsHObjkQAChbIIEnE8PWE591-folhzXEWG7Xqpv009eibx0ToNtWteCWOX4Wm3aNZ-zLCi6W25XSgH6FMfreEdFRHYha0utDx3uZ9oZPpdZzSi9kKPHRsVheaoVnRkDeiTt-RwEfP1pxkDaGAcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👜
هیچ چیزی از چرم‌دوزی بلد نیستی؟ از صفر شروع کن!
دوره جامع چرم‌دوزی با پشتوانه ۱۲ سال تجربه؛ از یادگیری مهارت تا راه‌اندازی کسب‌وکار و فروش.
🎯
✅
۱۴ جلسه آموزش مهارت + کسب‌وکار + فروش
✅
مدرک فنی‌وحرفه‌ای و قابل ترجمه
✅
۶ ماه پشتیبانی
🎁
پک ابزار + ورکشاپ هوش مصنوعی + مشاوره رایگان
📅
شروع: ۱۱ مهر |
⏰
۱۶ تا ۱۸:۳۰
👇
برای رزرو ، همین الان روی لینک ثبت‌نام کلیک کن.
https://maharatjo.com/charmdoozi/
شماره تماس
📱
09016169412</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/693932" target="_blank">📅 13:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693931">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b604a918.mp4?token=U5wMDMFUonMLIvVj8krYJzzqZ6oA3LTfQGAsM_f1bfn3hQDovLlrFoTsROnHxW-IfLzKiPHpSlIbDFXIXJzseDQ-PUIRqTxyZNPdx1r8BPXLomNOTS_LS0qmJpRIDNipN1djGk7PEd8-825oSdjc6Mz4qe1YrStmZ0j9XMSWnh01Pi6X1paFA5pqXTXuPMz9y7UzPWwmX8Uw0Oho6kPYEiiWTl-IlmVNINBVqzka6q8n8SbV0F3FiAvHtMeKiYR0UHUyFa3cCowwl5vL2e8Wvg2c2YfeTEHWLY75NwpU_YlgnXgR9YDpRFj1CMryOTw9lonw1NGrS_aMwt46drFdNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b604a918.mp4?token=U5wMDMFUonMLIvVj8krYJzzqZ6oA3LTfQGAsM_f1bfn3hQDovLlrFoTsROnHxW-IfLzKiPHpSlIbDFXIXJzseDQ-PUIRqTxyZNPdx1r8BPXLomNOTS_LS0qmJpRIDNipN1djGk7PEd8-825oSdjc6Mz4qe1YrStmZ0j9XMSWnh01Pi6X1paFA5pqXTXuPMz9y7UzPWwmX8Uw0Oho6kPYEiiWTl-IlmVNINBVqzka6q8n8SbV0F3FiAvHtMeKiYR0UHUyFa3cCowwl5vL2e8Wvg2c2YfeTEHWLY75NwpU_YlgnXgR9YDpRFj1CMryOTw9lonw1NGrS_aMwt46drFdNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پژوهشگر روابط بین‌الملل در شبکه سه: بهترین زمان برای تشدید تنش، ۳۶ روز مانده به انتخابات آمریکاست/ اختلافات داخلی آمریکا فرصتی برای پیشبرد منافع ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/693931" target="_blank">📅 13:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693930">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
آخرین وضعیت پیگیری وضعیت سه خلبان سوخو  سخنگوی ارتش:
🔹
همان‌طور که قبلاً هم اعلام کردیم، ما به طور جدی خواهان روشن شدن وضعیت این خلبانان عزیزمان هستیم.
🔹
اقدامات حقوقی از طریق وزارت امور خارجه و ستاد ارتش با طرف‌های قطری و طرف‌های بین‌المللی انجام شده و این…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/693930" target="_blank">📅 13:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693929">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05b1544704.mp4?token=qa0qg6mW2IzVTBq2S29arKIzshM6lcksYoxO-z9HuVcIdWuoSYTYfgbVxcYXtxWmFdk41nwIWlvKACGNjBTSMIIp2iiNk_7x2173XXl4SYJi3LwcU4UgLgeJ1ddX7zdW9wsN3pWoj15LH2wihiXDEJuQcosdnTCfoDY7vyywE8lypPOMX-LjwMmY1I4GGx6g6aDKKdSKhDYePpGsH27QQZTkZUZdpVghu3pcEwOBuOdD29nJvVI5g3cxQvPYhOAS98spAoJfBjsinGNOp0abEy9Xh-sDp1fjwspYvbV_J-sWL8B3n_uBJ6c_x0gt-FtXf6QkP7gKlLPYZBkN0WDc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05b1544704.mp4?token=qa0qg6mW2IzVTBq2S29arKIzshM6lcksYoxO-z9HuVcIdWuoSYTYfgbVxcYXtxWmFdk41nwIWlvKACGNjBTSMIIp2iiNk_7x2173XXl4SYJi3LwcU4UgLgeJ1ddX7zdW9wsN3pWoj15LH2wihiXDEJuQcosdnTCfoDY7vyywE8lypPOMX-LjwMmY1I4GGx6g6aDKKdSKhDYePpGsH27QQZTkZUZdpVghu3pcEwOBuOdD29nJvVI5g3cxQvPYhOAS98spAoJfBjsinGNOp0abEy9Xh-sDp1fjwspYvbV_J-sWL8B3n_uBJ6c_x0gt-FtXf6QkP7gKlLPYZBkN0WDc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حکم پرونده «کنسرت کاروانسرا» صادر شد؛ شلاق، ممنوع‌الخروجی و محرومیت هنری
🔹
پرستو احمدی و هشت نفر از عوامل «کنسرت کاروانسرا» به اتهام «جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای خلاف اخلاق در فضای مجازی» به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/693929" target="_blank">📅 13:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693928">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgHEfO009-LZOZOtiS1Ah1pDuUHHxfw2WyZLxQZz3HQu6mWys4Qh8J1f0DrQnLhjTBr9aAe3U1M13Fj55i9yxKC5jHbyBdwH3J2_hiCn7MbVLJISQgGLHKauhvc4I4c-RjlBV5GAQx2WQJWjTwbgoRGeRPiXFI7Lj8fHHzCrYNjKLnvAEIQHLdfN-Aamyl5vvdtg_5G5i7nl-mCkjJkIiBEUlBm8dUo-bWCgqgoZH5rxsGnVZ7pjt8ZFpsrATEIAvFJMhEUDFuOlVGxrlEGlUc5b_eKtsKSSa5vRe_7RqRh978qxcfmF5R9Uc_GMgZz3c7grh8U3Ptg66-BBBUUMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده سفر مرموز نتانیاهو به امارات/ نقشه بی بی برای ایران چیست؟
🔹
سفر به امارات در حالی انجام شده که نتانیاهو تنها دو روز پیش از آن، از نشست‌های مجمع عمومی سازمان ملل در نیویورک بازگشته بود. همراهی رومان گوفمن، رئیس موساد، و شموئیل بنعزرا، مشاور امنیت ملی اسرائیل، در این سفر نشان‌دهنده اهمیت بالای امنیتی و اطلاعاتی آن است.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3248737</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/693928" target="_blank">📅 13:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693927">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
نایب‌رئیس مجلس: مجلس طرح سه فوریتی خروج از NPT را بررسی می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/693927" target="_blank">📅 13:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693926">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae10109bb.mp4?token=ku_zoEXce_KdtJSxzNkGb8iM-tFoCDKoID3Imh8IwTkiN6i46_UP0lJbaFT32IISYUZ4S4rmbwMubSOpTgpz9OZ2cLhbxib8eIjL9EDl7Uy6hDGP7u5ZUTrvUCB4P3bOrNvqu_FpCTCRq8Nz_JQ5aosqOgNhOlAg0fz5srOaPs31iuLeUA9aPdmaF4G75fKp_GzzOMOb9-iqmynA9Jb0STle62JTJBHwYzOvMTbNOMoxn-Pm9HLgOY0HC583BVJhYLYNFCnNDXfZzVbtfoIH-2w6ju1DTZ3sC4Vrb06rKxU22XHkkS_2PoxpHqjndyUztUfXcpolwpIj7M0c99nVnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae10109bb.mp4?token=ku_zoEXce_KdtJSxzNkGb8iM-tFoCDKoID3Imh8IwTkiN6i46_UP0lJbaFT32IISYUZ4S4rmbwMubSOpTgpz9OZ2cLhbxib8eIjL9EDl7Uy6hDGP7u5ZUTrvUCB4P3bOrNvqu_FpCTCRq8Nz_JQ5aosqOgNhOlAg0fz5srOaPs31iuLeUA9aPdmaF4G75fKp_GzzOMOb9-iqmynA9Jb0STle62JTJBHwYzOvMTbNOMoxn-Pm9HLgOY0HC583BVJhYLYNFCnNDXfZzVbtfoIH-2w6ju1DTZ3sC4Vrb06rKxU22XHkkS_2PoxpHqjndyUztUfXcpolwpIj7M0c99nVnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از کجا بفهمیم کبد چرب داریم یا نه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/693926" target="_blank">📅 13:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693925">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
طلاسی داوطلبانه وارد سامانه ناظر شد/ گامی بلند برای جلوگیری از خالی فروشی
مجید قاسمی، دبیر هیات مقررات زدایی و توسعه فضای کسب و کار وزارت اقتصاد در
#گفتگو
با خبرفوری:
🔹
یکی از اصطلاحاتی که در اکوسیستم خرید و فروش طلای آنلاین رایج شده خالی فروشی است.
🔹
به عنوان کاربر وارد یک پلتفرم خرید و فروش آنلاین طلا یا نقره می‌شوید و مثلا طلا می‌خرید؛ اگر طلای خریداری شده در هیچ جایی موجود نباشد اصطلاحا خالی فروشی رخ داده است.
🔹
باید به اندازه میزان طلایی که می‌خرید در خزانه‌ها که اکنون تعدادشان نسبت به قبل بیشتر شده، موجود باشد.
🔹
طبق آیین‌نامه هیئت وزیران، سامانه ناظر طراحی شده و تمامی سکوهای آنلاین باید به سامانه ناظر که توسط بانک مرکزی تهیه شده وصل بشوند‌.
🔹
در حال حاضر دو پلتفرم طلای آنلاین به نام طلاسی و وال‌گلد به صورت داوطلبانه به عنوان پایلوت به سامانه ناظر متصل شده‌اند و برای سایر پلتفرم‌ها نیز، اتصال به سامانه الزام قانونی دارد.
🔹
با خرید کاربر از یک پلتفرم، میزان طلایی که پلتفرم قصد فروش آن را به کاربر دارد، راستی‌آزمایی می‌شود تا مشخص شود به همان اندازه طلا در خزانه وجود دارد یا نه.
🔹
پس از خرید، به همان میزان از طلای موجود در خزانه برای کاربر فریز و از موجودی قابل‌فروش پلتفرم کم می‌شود؛ کاربر نیز می‌تواند بعداً طلای خریداری‌شده را از پلتفرم تحویل بگیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/693925" target="_blank">📅 13:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693924">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBxnkZaxpZqOHnyVgZ6RgqQvK55DWG4y07A9sIdfvGCN3IrOzFURYc7e_3LFBpfiDByqPtFsfBA2ReRf19neoQQVETxbthnYLHqRs69JsIq1CAiJjoYZL_AKCpwKjxndw8E2Ln6a8HyPnKAmm8zRE5sPbIozVD73TP06lOVpJb7GEVNGe6Ck11rb579-DDQpCw3UUvAaZlPyByOAS5Aq5nkIc84mUbaFvxsihlAmCr3vgYYRsu_Tq1pX8wfRtMyJJslccbxui6_k3Ix3b-QrW9ptSR0MkhcC8rGJg2G4fIF58S4ocOhJG-HDMYoT5qmULiQshBlboxJ3-063LTHjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمایه؛ چالش اصلی راه‌اندازی کسب‌وکار خانگی
🔸
در این نظرسنجی بیش از ۲۸ هزار نفر شرکت کردند که سهم روبیکا ۶۰ درصد، بله حدود ۲۴ درصد و تلگرام ۱۶ درصد بوده است.
🔸
۴۷ درصد شرکت‌کنندگان کمبود سرمایه و حدود ۱۸ درصد هم نداشتن ایده را از مهم‌ترین موانع برای داشتن یک کسب‌وکار خانگی دانسته‌اند.
🔸
کارشناسان نیز کمبود سرمایه و دسترسی محدود به بازار و مهارت‌های کسب‌وکار را از مهم‌ترین موانع راه‌اندازی و توسعه کسب‌وکارهای خانگی می‌دانند.
@amarfact</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/693924" target="_blank">📅 13:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693923">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
قیمت تتر از ۲۵۰ هزار تومان عبور کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/693923" target="_blank">📅 12:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693922">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5e6ece44.mp4?token=SVKwRWjVcbBMfkaHYzSPPbZRPc-jBgcgJxs_f_CBAihlEnOQjThBDgNyODZlowoDFbeO7ztxiFTegKT8F30USAvKSCJ9bjiex_u4ivJ4e_1AKJcbugueXA0nBG1YpUHEHRoSPEfsMymD_ajmxQu8ScGRaO_HDuJmKLznZLYVgGPg83FoeaCz9wVAeYn9z06IiO0nOV14NRF93l2eT4UPtaw6WQM7PhcZWzO2AdYUguON1YaiXIs-UAZDVj2dlF2EGt_M7_keJdCrypoIgIwibBA6sKSuTYdWzTLi7yXcJ1ZeU6RcclW93Yu_SHruNyuKVukNOJARxuHFmzgr3BWZQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5e6ece44.mp4?token=SVKwRWjVcbBMfkaHYzSPPbZRPc-jBgcgJxs_f_CBAihlEnOQjThBDgNyODZlowoDFbeO7ztxiFTegKT8F30USAvKSCJ9bjiex_u4ivJ4e_1AKJcbugueXA0nBG1YpUHEHRoSPEfsMymD_ajmxQu8ScGRaO_HDuJmKLznZLYVgGPg83FoeaCz9wVAeYn9z06IiO0nOV14NRF93l2eT4UPtaw6WQM7PhcZWzO2AdYUguON1YaiXIs-UAZDVj2dlF2EGt_M7_keJdCrypoIgIwibBA6sKSuTYdWzTLi7yXcJ1ZeU6RcclW93Yu_SHruNyuKVukNOJARxuHFmzgr3BWZQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای عادل فردوسی پور: فدراسیون از استقلال پول گرفته و الان پول نداره پس بده و میخواد استقلال رو بجای پول قهرمان لیگ اعلام کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/693922" target="_blank">📅 12:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693921">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWrS_PXHQ6RmB8Il8ojXeR5YfR_bmJcN_KGI_EsrA0XAlz2Qvs6ONfUHtALTlt2XltmZnRcp2xSe9cqa-nbXmKu3nly3Mm4Qu6g2JevqISPITlBTPYlkQumyBqgfJrYUYLUMYAxaaxxyQceP2M13_ylVaO9J2C2ia81MyA7565BEHEyxhWDmXHGEDVhtS_YOYjSBi48YTCdOpNIQKa2Y4tpyQ6c6Yx9xmtpJR4CRpAWl8lZcjC25wUeQ1B7vfjNha0HowF8L_MA2_uzZydjPTKQOMZ292AN3pf07Fo8WeTvkEkbFhE8PhqILEGz09ygpHNkIt9zgNXCHQYgFs2vH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمید رسایی: نه شرمنده‌ام و نه عذرخواهی می‌کنم؛ بلکه در برابر این ملت باعظمت، سربلندم؛ کسانی باید شرمنده باشند که کودتا می‌کنند!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/693921" target="_blank">📅 12:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693920">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e104eddef.mp4?token=Wk1Y18kPZnpfnb6D7XkH1j-S788d6Wdn7mIzBej2JMSN7R9OV-GJ7Lo68ElKepyup8YYdY9OcMNoDammqib4EFA3EnOVdzbDJo1I39L1AJMomtJ-Cs-BSNszWFRh_ftbu0O5Ic0JIrLxSCpbahTiaRf5i1mMd43-cvijotJYWd5QYqMcTWJyQKhAB0U5PtGfUFamTY7uQyH0f7Pr0lK-Fr4tyICE5a-vvFLH_Y-4AlN-1-k4caHXsBdOOwClzWv7oMXhm6cO1xodPTtSjMdzk9Ymk_I4cNmiQV9iTj8-5T6Gz2CCTwQLTthvTjhMVJq4PcdGKw2FTHgpiVoh4zx8bwq5mVQbFzoJUtUPA-UbrquBUYc0KHFbfCqtjuSz0GylpAXsR7pB0-dsxBicf_3c5vdrBmxxsUm1FbFYs7DFk96G8DWPJ01pHCYrSloXyqbNsUBZ63V6HODR4pPdMu6BC0a9F_1ksUID0Rbjahw4ZiauaUWLL_vT5Z6PzOtGAbUcrBpUpx7APWG54EjsTFQp8eyEmWBYwvF_z3oh1Z7rYXSLe092RLVvMLZsoH_xtdfbYhDXf8A8cEoHWFHdO-baZpU2B8ItL0bMor7dDdTzgMgYXPQlek_Wnu8BU1w0vsL3A78CcR-IE1fwsHoHS-6DUCd2oEGYLcZGZbFVFD6Jv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e104eddef.mp4?token=Wk1Y18kPZnpfnb6D7XkH1j-S788d6Wdn7mIzBej2JMSN7R9OV-GJ7Lo68ElKepyup8YYdY9OcMNoDammqib4EFA3EnOVdzbDJo1I39L1AJMomtJ-Cs-BSNszWFRh_ftbu0O5Ic0JIrLxSCpbahTiaRf5i1mMd43-cvijotJYWd5QYqMcTWJyQKhAB0U5PtGfUFamTY7uQyH0f7Pr0lK-Fr4tyICE5a-vvFLH_Y-4AlN-1-k4caHXsBdOOwClzWv7oMXhm6cO1xodPTtSjMdzk9Ymk_I4cNmiQV9iTj8-5T6Gz2CCTwQLTthvTjhMVJq4PcdGKw2FTHgpiVoh4zx8bwq5mVQbFzoJUtUPA-UbrquBUYc0KHFbfCqtjuSz0GylpAXsR7pB0-dsxBicf_3c5vdrBmxxsUm1FbFYs7DFk96G8DWPJ01pHCYrSloXyqbNsUBZ63V6HODR4pPdMu6BC0a9F_1ksUID0Rbjahw4ZiauaUWLL_vT5Z6PzOtGAbUcrBpUpx7APWG54EjsTFQp8eyEmWBYwvF_z3oh1Z7rYXSLe092RLVvMLZsoH_xtdfbYhDXf8A8cEoHWFHdO-baZpU2B8ItL0bMor7dDdTzgMgYXPQlek_Wnu8BU1w0vsL3A78CcR-IE1fwsHoHS-6DUCd2oEGYLcZGZbFVFD6Jv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای فروش گوشت سگ در تهران و اعدام عاملین فروش گوشت سگ از زبان رییس سابق دادگستری تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/693920" target="_blank">📅 12:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693919">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHRF6ta9zTCD1nuXsGW0OCmijOVyGWqYmO6NVCUmu_D4S_aCtmM6vI_KKPwkBPne9eGpUDnx72lcTmLqz_RF51xZXdXame8aV46N6FpGH_SBF8IeMSRgTgtzMJl1TfH_Wx59WeZB3Z2-VZrY3XNfCI2MydMmlHn7bYPiuOYrVMY5_2A1_6Yzs5tTnjL0buyACdSk4MwR_5m4I8vSZ6JDF6pxYZhuVYT6yGwQg8YyEmw_dsz-jnVcfBoadOcNq2eXCh_QmdA4FiGKHfl2CzlCBklgCc3IhpGyiab7Q7Xa_NFCPZcVRul0u-PgvhJTokU4RLV5Ot4rIE0xZOKPV63zQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش مرکز پژوهش‌های مجلس نشان می‌دهد هزینه سبد ۱۱ قلم کالای مشمول از دی ۱۴۰۴ تا مرداد ۱۴۰۵ حدود ۶۷ درصد زیاد شده است
🔹
با وجود این افزایش هزینه‌ها، رقم کالابرگ ثابت مانده و در صورت تعدیل باید به ۱.۸۶۰.۰۰۰ تومان می‌رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/693919" target="_blank">📅 12:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693916">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRWQunrpyY0ZvSE6qMuZAuiniwRyU4nwZKK3JH5zdCk2yIBpo_MpyxUGyZf4OkgPHKyAW8ZVMfUGATJ5If_-3plRKZ45D2IselnjXRi5TlfCGfdEAunXGOD-zd9SXGRmC5Nnh5dAj3wrHak7E6Bw_jVnJaJny5mQUprV_uj5kEvum4ZZN6MHH71Gx95MSWKy8WdeXF1NEIYtwhf9EmiWoSbH0wy1ILmaqYd5trB4scvr_iikUSq2snVQYeL_QoytygBjy8PFoXuSf3CwwkU9plfO5bxjkpaxh-0hqrBkpu5Ik5bCnKyjon-0ZD-leuSTshaQExDo_4-WqzepQWrPdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت امروز طلا و سکه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/693916" target="_blank">📅 12:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693915">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
مهدی نصیری: با پول‌های بلوکه شده ایران، افرادی را در داخل ایران مسلح کنید تا در صورتی که نیروهای آمریکایی و اسرائیلی در ایران پیاده شدند، این افراد آموزش‌دیده هم در کنار آن‌ها وارد عمل شوند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/693915" target="_blank">📅 12:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693914">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe05986f0.mp4?token=v54wp3PBEP19k_qVG8VhzDq59DHatCT23AOui-1Mnu5OHUIJs1iVhZVZIdainEesz3hK6UloG_Q1KZFISxZmqRufLrPBd9u2tNdGE_xUPHifDCGolRFmDSS2ge9n_IqnXN_GVOs2CudsdHp5KmlOLJaxfEJqLg2XQGogA37zWNBdvWUfubsVNb5IfQWWtiEQ0lTeqrTuOxEvZmcSWDK-0hw0Cl1CTRU-BIrqCCRf1T34GqyOYZELGs8ZiEDuyj5KOCpJyRQTgokuEhxB6mAIws5jNy8Gh-AeS2QOnZyQWF98owbWz_2KBlelmwaG7SDvm-4uGOhApq_qhSjKjSHXzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe05986f0.mp4?token=v54wp3PBEP19k_qVG8VhzDq59DHatCT23AOui-1Mnu5OHUIJs1iVhZVZIdainEesz3hK6UloG_Q1KZFISxZmqRufLrPBd9u2tNdGE_xUPHifDCGolRFmDSS2ge9n_IqnXN_GVOs2CudsdHp5KmlOLJaxfEJqLg2XQGogA37zWNBdvWUfubsVNb5IfQWWtiEQ0lTeqrTuOxEvZmcSWDK-0hw0Cl1CTRU-BIrqCCRf1T34GqyOYZELGs8ZiEDuyj5KOCpJyRQTgokuEhxB6mAIws5jNy8Gh-AeS2QOnZyQWF98owbWz_2KBlelmwaG7SDvm-4uGOhApq_qhSjKjSHXzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات‌ها؛ فقط ۷ سال از روزهای دست‌وپاچلفتی گذشته است
🤖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/693914" target="_blank">📅 12:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693913">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvNnI4hM2CNVwXs4eDYJK-gISabvm2OY8KL7DFL9xEdqHSxWTl4aDNo-oB7ocAQfjfobf9ac62CJyp5IaehmXha373zc-XaO0Xutg9eq6LZ7y5WmdROFeP3KPu7Erj0H6gcJevJnuQZNM2OAhYLUEB-2j0dQ2zJIuzsOCgHDg5TtMMzfw9tnrjmNEr-3w19siPhxTDxzNnvQFXXgho3uF7FNC4OG3eDo1aRzbhpMnznoUHjhYhOU9sPAMYQzr70pShKeT725tZspVx6grW06IsXn7i76f2uC6G_QZWqfkEDn2t8dxn8URwJ5Y_CH7Cz_nlzmwnXP1giai3Q4E6AItw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
«مهسا بهشتی» ورزشکار مورد حمایت بانک اقتصادنوین، در «ناگویا» تاریخ‌ساز شد
🔹
«مهسا بهشتی» ورزشکار مورد حمایت بانک اقتصادنوین و نماینده وزنه‌برداری ایران در بازی‌های آسیایی، صاحب مدال برنز شد.
🔻
اطلاعات بیشتر:
▫️
https://enbank.ir/s/mfaba86
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/693913" target="_blank">📅 12:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693912">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f7e668b9.mp4?token=rzHmHjt2IleazQ6JiPJ8Le6asO3AlKKavnf-KqHMJDOlBiRhpJ-Kc9itrpsHVefoJHMSaEI7pvMIsCLIhDjA0e00VzVrraz8f5npoZMgLn_07YjG0uHO1hXhkuoy0vt5ahAUQd_NAXTnq_5UQbM8ZxDOdzfKabvw1E0TWSkfeOkce_V6yLY35yxvuoj4gneB3N5VKURe27LqjVNmYMzW5gTy02IizH6ZhhOuQhUanC-BepHDa9JA_i1pcWXegVO8J-D0MNGuGLDgwvhoEUYe7N8rBtAuhpwn0sS42D7eMi8ij60OGcM8cMLe-n9pEy1i4nbMAG8G4ev5G3WCEY7BR5Ks9V-YvENeldVUL9FNl_3Ie-Rn1vcN3KtgFy4JxhH5WUcB766TPAJeIMVKN0IwnnpAoe-t4EueC01-amFzoAMN0mvr0z9LPc3Rt0lCDuu3v7XSiN86mELVm5s4fpvAbFhvUeObvinevCjrAOh0ry8auVeWQG1mDsFXG7gKZRTn8dTXQLuzGSIkTGeozfvfzBu16FqYMzEj6lnKyHQw2li4GZcXVK-MwsP5g5XePHw8LRqCL__avFub0hvZkEK-1pj_sljDa-3cEwQtHfdFKKnawHm3bDwgiq7EjQhRGFc6KaE27MoWpbpEOjJanpa0PbouLaGRy9hgwgThJeLHs_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f7e668b9.mp4?token=rzHmHjt2IleazQ6JiPJ8Le6asO3AlKKavnf-KqHMJDOlBiRhpJ-Kc9itrpsHVefoJHMSaEI7pvMIsCLIhDjA0e00VzVrraz8f5npoZMgLn_07YjG0uHO1hXhkuoy0vt5ahAUQd_NAXTnq_5UQbM8ZxDOdzfKabvw1E0TWSkfeOkce_V6yLY35yxvuoj4gneB3N5VKURe27LqjVNmYMzW5gTy02IizH6ZhhOuQhUanC-BepHDa9JA_i1pcWXegVO8J-D0MNGuGLDgwvhoEUYe7N8rBtAuhpwn0sS42D7eMi8ij60OGcM8cMLe-n9pEy1i4nbMAG8G4ev5G3WCEY7BR5Ks9V-YvENeldVUL9FNl_3Ie-Rn1vcN3KtgFy4JxhH5WUcB766TPAJeIMVKN0IwnnpAoe-t4EueC01-amFzoAMN0mvr0z9LPc3Rt0lCDuu3v7XSiN86mELVm5s4fpvAbFhvUeObvinevCjrAOh0ry8auVeWQG1mDsFXG7gKZRTn8dTXQLuzGSIkTGeozfvfzBu16FqYMzEj6lnKyHQw2li4GZcXVK-MwsP5g5XePHw8LRqCL__avFub0hvZkEK-1pj_sljDa-3cEwQtHfdFKKnawHm3bDwgiq7EjQhRGFc6KaE27MoWpbpEOjJanpa0PbouLaGRy9hgwgThJeLHs_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده از موتورسواری روی پل عابر پیاده در مشهد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/693912" target="_blank">📅 12:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693910">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250aabb1fd.mp4?token=m__1G4Zwq9ZWwacMdeOcy-j45r92xUzo2itEeOFcZYo-xv0aRjXHh77Yq-1GTio1TMDTSKxiyiuBasOsV5xxznqH-SUVxrAfWDOhjZH6BkBh4g3hXztFIB_mKxLc4QRYgG6ylY6_2mbd6kre7EaR-dkwVTkKFc9hZXfDYoomht9382JuXnBAPHgZIrCMqN0brRH-uis3HgNHoerjAA5zDGEzJWazZzl-4LD0DRtpsfbcREQodMDICEL8EsDTKx8RhaMbmpsDvC_XRuiurYHf9HZU42m74DiDJR_MrceMyu_0Yt5ulU2dQ_Z1sL79ecYoHJqey3bsZGox9pWOyqdnTGy_I6vcvpben-LtC2kCbJJNnDLd8of9Cgl9-GgixO7MTSC6XjiFu47W94BEOaAfvLruLU_mvgqJfFz6FPicJqaRejN60xQNb4JfeQsBCixrrZEdfq1j5uK4BTfTgUfgJEivLkmgZSiss7BQOEMbeJm_jaxDpArtaUnNnvlzPki7pT8KDoqeGMaRelXq4iyhX4hKCmFws7URcEqYU3aJ3X5lgzKp94IeLF_WptP6Sh5aPpuvDm-IdCzCdC4Dmw_syx7FqeFuePm-WHoaE-LdO2Oqe9KPEEbPusrnT0Ao4jWLu2JCj2AmAiAaOvfvu-g8xpmO9Xh7kwGdcegH_6uc0vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250aabb1fd.mp4?token=m__1G4Zwq9ZWwacMdeOcy-j45r92xUzo2itEeOFcZYo-xv0aRjXHh77Yq-1GTio1TMDTSKxiyiuBasOsV5xxznqH-SUVxrAfWDOhjZH6BkBh4g3hXztFIB_mKxLc4QRYgG6ylY6_2mbd6kre7EaR-dkwVTkKFc9hZXfDYoomht9382JuXnBAPHgZIrCMqN0brRH-uis3HgNHoerjAA5zDGEzJWazZzl-4LD0DRtpsfbcREQodMDICEL8EsDTKx8RhaMbmpsDvC_XRuiurYHf9HZU42m74DiDJR_MrceMyu_0Yt5ulU2dQ_Z1sL79ecYoHJqey3bsZGox9pWOyqdnTGy_I6vcvpben-LtC2kCbJJNnDLd8of9Cgl9-GgixO7MTSC6XjiFu47W94BEOaAfvLruLU_mvgqJfFz6FPicJqaRejN60xQNb4JfeQsBCixrrZEdfq1j5uK4BTfTgUfgJEivLkmgZSiss7BQOEMbeJm_jaxDpArtaUnNnvlzPki7pT8KDoqeGMaRelXq4iyhX4hKCmFws7URcEqYU3aJ3X5lgzKp94IeLF_WptP6Sh5aPpuvDm-IdCzCdC4Dmw_syx7FqeFuePm-WHoaE-LdO2Oqe9KPEEbPusrnT0Ao4jWLu2JCj2AmAiAaOvfvu-g8xpmO9Xh7kwGdcegH_6uc0vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر یک رابطه سالم با شریک عاطفی‌ات می‌خوای، این ۳ قانون رو حتما در مشاجره‌هاتون رعایت کن! #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/693910" target="_blank">📅 12:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693908">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
سخنگوی دولت: فعلا برنامه‌ای برای افزایش حقوق کارکنان دولت نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/693908" target="_blank">📅 11:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693903">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRexU8hBTXZ8QebGU3lLDhrnXEs3hvdcL58ddphGeZS4jBjK7li-fnvuehSBblUFWlrDdxK27wjOvEGl-rATYZ6b4Tsn0ZghruVssM6W7AFbcxKGkugzYYQ-W9t8CNWwA0X35jBNXertllHFmTAPILeBTj7EN3Z5m9zlZlR9OZ9afN6p02jW2CKR9ZBCdRo_uoZZgWA8wNRullQh1ScLZHnH-x9q9F7kJeLPQfH-LeMECXQvJfz4J_o7nKQWLtZ2j9q5kvfUWj5gWBu77-4lWQhUUugvcA4YJYB9_ZQCo5qMkWLQQ0JTTXOKERoVgN7-8IkJr2RXeXor9CPVjFqXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز با انتشار تصویر دیوارنگاره میدان انقلاب: در ایران زندگی روزمره جریان دارد و ایران با صدای بلند دشمنی‌اش را با آمریکا به تصویر میکشد!
🔹
رویترز با انتشار تصویر دیوارنگاره جدید میدان انقلاب به یک بیلبورد عظیم ضدآمریکایی اشاره کرده است. گزارش رویتر تاکید میکند که در این تصویر با عبارت فارسیِ «لشکر شیطان در خلیج فارس غرق خواهد شد»، در بحبوحه افزایش تنش‌ها میان ایران و ایالات متحده، در میدان انقلاب رونمایی شد؛ در حالی که زندگی روزمره در تهران همچنان جریان دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/693903" target="_blank">📅 11:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693901">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e36f7b9ceb.mp4?token=MpGpneZyrZAsrlZ3sB94F5NR6MEgthQ1su7IAHhEdagRNJ2As1HFFO0-KmA9Eo95GL-kl-hfDaGJckM6t5XIDthEk4OrHMeKhXHDidbnr8wRUri56NHHOgKnXLk3nvagxUQe0y-3tW29_fUp_TTwSQzHPGkrUYIrs_dbobl3cqw0q6ZzaX7FPOcKsXY7kCklxoW_wPHpBMwfK1C4aaCyQj1AX8G3vAFd1SnLG_-bZV_3EnJXo_AXon9LJAiGKpzeGhcuQXsyuUFENRmiW8gVXB1LYVVn79R01plhagqdiXVzYQR4EkqPRNp-4F09a_tNoTUs7OqKN8UNNjgVHnvBoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e36f7b9ceb.mp4?token=MpGpneZyrZAsrlZ3sB94F5NR6MEgthQ1su7IAHhEdagRNJ2As1HFFO0-KmA9Eo95GL-kl-hfDaGJckM6t5XIDthEk4OrHMeKhXHDidbnr8wRUri56NHHOgKnXLk3nvagxUQe0y-3tW29_fUp_TTwSQzHPGkrUYIrs_dbobl3cqw0q6ZzaX7FPOcKsXY7kCklxoW_wPHpBMwfK1C4aaCyQj1AX8G3vAFd1SnLG_-bZV_3EnJXo_AXon9LJAiGKpzeGhcuQXsyuUFENRmiW8gVXB1LYVVn79R01plhagqdiXVzYQR4EkqPRNp-4F09a_tNoTUs7OqKN8UNNjgVHnvBoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود مشاهده شده در مناطقی از تهران مربوط به آتش سوزی در ساختمان در حال ساخت در محله نیلوفر تهران است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/693901" target="_blank">📅 11:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693900">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFnYOnZ3ZDixK-a9v9DxmUZ1-AERkUjqNamoluSMAIGj9QlqU_LKz0TEMrfzwiK91kK5xDVjy8YTUlHZNY8kEOiWSoz4o1DGlW9xXawxOZaK-GcdpUzb5u-7OScizevFvK_Fn-v8EL3ORdFzd9Vg5vmMS_f-s6cjLvHXo0F6YbgXCifKiN7ioS4yV5Zzd4rU8rYrFNPirV0_6J4f7HuQ-QSdj5X0L5kMK6aStOozfOGITAxYB4joMqpC3QMJsatBle_x6GfpKn-PaprN8SlKTe3gLd030-X-fTvGuoH1ML_zTWP7EpkEjyd0iUKLDGu27Tdkp1wuJlG0Yoc7hrF-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام کشورها بیشترین استفاده را از ابزارهای هوش مصنوعی دارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/693900" target="_blank">📅 11:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693898">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سخنگوی سپاه: ادعای تلاش ایران برای ساخت سلاح هسته‌ای «دروغ قرن» است
سردار محبی:
🔹
آمریکا سال‌هاست مدعی است ایران در آستانه دستیابی به سلاح هسته‌ای است، در حالی که برجام نیز با هدف جلوگیری از دستیابی ایران به چنین سلاحی شکل گرفته بود.
🔹
دشمن خود می‌داند ایران به دنبال سلاح هسته‌ای نیست و مسئله اصلی هسته‌ای نیست بلکه «نابودی کشور پهناور ایران» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/693898" target="_blank">📅 10:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693897">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZJUHZ9Jmxq5d7QWwLw4YIC-gINlDtMpPPEeS5U5v37otX6hRENa7PVhSG8nxiSeCi1IQkKPr3pUfoIWjW7-bU-AyEeGUt6yt2Kvh001Orbfx5mlg0ENoXzMssjyIhW4B6rAulGaOrtKuiOb3zw3jiUFnP4kyLmhDp1YFbnh7IaB0Jd2Mpb8e_hoNWsTsV_5BblYqaRZmQfBBLI2pUjbSBchGHrS7xbUe6Nz3wJMf7aiYWieBA2ZNOMLHbXnmw9b_FMx3iBZMihNXTlxrHAT0UhUyPAIUJ7rpl4RLuE6TUanRDPu3bnU7_r-M0jpEt4ePBm5TML3Kgku2C602omHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مفت‌خورین عقب افتاده؛ چه چیزی باعث شد آمریکا از جانفدا تقلید کند؟
🔹
فراگیری جانفدا و عمومی شدن موضوع جنگ به نحوی موثر بوده که حالا آمریکایی ها درحال تقلید از این پویش هستند. اندیشکده های آمریکایی قدرت نمایی جانفدا را به عنوان عنصر تاب‌آوری ملی ایران و علت اصلی پیروزی ایران در نبردهای پیش رو می‌دانند.
🔹
خود وزیر جنایتکار آمریکا پای کار پویش «مرا بفرست» آمده و آمریکایی ها را ترغیب می‌کند تا توانمندی بدنی خود را برای حضور در جنگ با ایران بالا ببرند.
🔹
ایده درخشان جانفدا موجب حیرت رئیس جمهور روسیه هم شده بود و حالا عملیاتی شدن جانفدایان ایران در گروه های مردمی موجب ترس بیشتر جنایتکاران آمریکا شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/693897" target="_blank">📅 10:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9404ae77d3.mp4?token=NQMuCOrkAediu75ZMn6sqxe_Y_DrRPKwxfloBZDX3k_IqgVUSbz7HwMBnoKpoqdJqLct7hx46tyftOqaHnYJaQDKRbzcioqQztEmuxHe9P4vSm0SBfV0fKqXp8iCuAPw9xO6BIZzkDsk1CxI1THN7i6SKNAnRA3n-uHYMoPSic8uCxHrlZq00q0DGClvAJcXIl-SSsp-Cvr5ZqsVuW8phCfVbkLAu0QbXio7SjvgEZ8oIImQF03zeNmmAcYB3zA3wFazRFeDzGNJlSSPmdpnneDHmIUftVXEcGV91OKVChapnNjYVcHqgrteEH0qt-yDtJn76SbpfB3FOi3aw2kn8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9404ae77d3.mp4?token=NQMuCOrkAediu75ZMn6sqxe_Y_DrRPKwxfloBZDX3k_IqgVUSbz7HwMBnoKpoqdJqLct7hx46tyftOqaHnYJaQDKRbzcioqQztEmuxHe9P4vSm0SBfV0fKqXp8iCuAPw9xO6BIZzkDsk1CxI1THN7i6SKNAnRA3n-uHYMoPSic8uCxHrlZq00q0DGClvAJcXIl-SSsp-Cvr5ZqsVuW8phCfVbkLAu0QbXio7SjvgEZ8oIImQF03zeNmmAcYB3zA3wFazRFeDzGNJlSSPmdpnneDHmIUftVXEcGV91OKVChapnNjYVcHqgrteEH0qt-yDtJn76SbpfB3FOi3aw2kn8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه: افراد تحت پوشش کمیته امداد، بهزیستی و افرادی که استحقاق دریافت کالابرگ با مبلغ بیشتر را داشته باشند، بدون اقدام خاصی کالابرگشان افزایش می‌یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/693895" target="_blank">📅 10:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693894">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
آغاز رسمی هفته فرهنگی ایران در روسیه با اجرای ارکستر ملی ایران
🔹
شامگاه گذشته هفته فرهنگی ایران در فدراسیون روسیه با اجرای ارکستر ملی ایران به رهبری همایون رحیمیان به‌صورت رسمی آغاز شد.
🔹
در این مراسم، وزیر فرهنگ روسیه با اشاره به برگزاری هفته فرهنگی ایران،…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/693894" target="_blank">📅 10:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693893">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv36829b5zTFVFi79ZyPI-P9wwkWXaYxxrpjfTkcHi86dEAE96JdUc2D7h9UE7f7sV_8zz39AaP7pDpB0QaGUI2uoPRr07vTBUBkt6ru9bmBgDyHEDRsA2BTyz_kIncA7zfrCI6ZBFSJsW-3aDdUMhYSOwFkhpPJLV-L9Qx2TkpBhpEBiZUsbV-YtPRG-E6YaAeASVqWiMLYSChIK6NEphpKSwI5QUgCpEv-QmhbyXJgCtKcd5rSD9peTxbmfC-Oo7CwTXE4KslsXk5VYy51SdOJysOr0gsgsU-gdLO_96V1DqcQ0w9H8N6XQbOjerZVrc37G0rYXdsul8PXSje_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترور فرمانده تیپ شمال غزه در گردان‌های قسام
🔹
نخست‌وزیر و وزیر جنگ رژیم صهیونیستی در بیانیه‌ای مشترک مدعی ترور فرمانده تیپ شمال غزه در گردان‌های قسام شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/693893" target="_blank">📅 10:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693892">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f3c62e804.mp4?token=aLzy6RDTluXuP1U3HLpjTao-0qzIQeZFP6lQxt5TGT_TxqkiwOgRvmVEs1NkkHlNXkT9Rv_hAw-B1W5MzAGTi-OA8yJD3KrDeYef81s5SRhfRIJqLgA8e1rxj1mGMfprOZMkEiL1Bz55WWD2aaiAjQbj2bIwpUFB0YHuIR7YW7rpU5skvemmm9oS5eHOE6Gc5f95fADs7WgfuwTp_uFOZjjFROzDAgZcQV3Sv5n2wuDslZLzFG6pod-6lvqbhBxk5gPpkTWuLXpnlonhYcbMO0abYdy1UdqsKeMnI1jvW9s4e2vTvWFbtBY6dndupGZQaGdiSdva8Gi26A47bqeE8HLtatfdckC2wKJdmJef3qsxETsHVhewUhFjT9COAcNzV6nacJDqcGl1RcMq0cUJQsmSM33qCCQGrYW_dnGlRkPTthAIWU1XMGh97HbQN34AbEB1c_dG5vpjsaWlpbOHZ3YHcE52ewLL3p5TWGuvsC3x_eafHrvvm31q-IChAj-hxvLPLD74chyo9exl9SVFP-NhePZdpsHEb57KBRTWlxU95a84dKL0TdpRbpeLihN7Ks-P1knuhkqYIIO0jV1TMh5hpOdKStqmYOvOvqvH0sCXpriIUixMG_blVlaOAWW7Mn_ybuUPUxiPIwQQ9akkP-TfMg3Vdx8u6IkHH08ZTwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f3c62e804.mp4?token=aLzy6RDTluXuP1U3HLpjTao-0qzIQeZFP6lQxt5TGT_TxqkiwOgRvmVEs1NkkHlNXkT9Rv_hAw-B1W5MzAGTi-OA8yJD3KrDeYef81s5SRhfRIJqLgA8e1rxj1mGMfprOZMkEiL1Bz55WWD2aaiAjQbj2bIwpUFB0YHuIR7YW7rpU5skvemmm9oS5eHOE6Gc5f95fADs7WgfuwTp_uFOZjjFROzDAgZcQV3Sv5n2wuDslZLzFG6pod-6lvqbhBxk5gPpkTWuLXpnlonhYcbMO0abYdy1UdqsKeMnI1jvW9s4e2vTvWFbtBY6dndupGZQaGdiSdva8Gi26A47bqeE8HLtatfdckC2wKJdmJef3qsxETsHVhewUhFjT9COAcNzV6nacJDqcGl1RcMq0cUJQsmSM33qCCQGrYW_dnGlRkPTthAIWU1XMGh97HbQN34AbEB1c_dG5vpjsaWlpbOHZ3YHcE52ewLL3p5TWGuvsC3x_eafHrvvm31q-IChAj-hxvLPLD74chyo9exl9SVFP-NhePZdpsHEb57KBRTWlxU95a84dKL0TdpRbpeLihN7Ks-P1knuhkqYIIO0jV1TMh5hpOdKStqmYOvOvqvH0sCXpriIUixMG_blVlaOAWW7Mn_ybuUPUxiPIwQQ9akkP-TfMg3Vdx8u6IkHH08ZTwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز رسمی هفته فرهنگی ایران در روسیه با اجرای ارکستر ملی ایران
🔹
شامگاه گذشته هفته فرهنگی ایران در فدراسیون روسیه با اجرای ارکستر ملی ایران به رهبری همایون رحیمیان به‌صورت رسمی آغاز شد.
🔹
در این مراسم، وزیر فرهنگ روسیه با اشاره به برگزاری هفته فرهنگی ایران، گفت: «وظیفه مشترک ماست تا از این بستر حاصلخیز همکاری‌های مشترک فرهنگی برای استواری روابط دو ملت استفاده کنیم.» او همچنین تأکید کرد که این رویداد می‌تواند به تقویت روابط میان دو ملت کمک کند.
🔹
در این برنامه، ارکستر ملی ایران در بیانیه خود یاد امام شهید امت، شهدای دنا و ۱۶۸ شهید دانش‌آموز میناب را گرامی داشت.
🔹
گروه ۱۶۸ نفره هنرمندان ایرانی با عنوان «میناب ۱۶۸» در چهار شهر مسکو، سن‌پترزبورگ، قازان و آستراخان حضور یافته و به معرفی وجوه گوناگون پیشینه تمدنی و فرهنگی ایران می‌پردازد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/693892" target="_blank">📅 10:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693891">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ادعای تتر: از ابتدای ۲۰۲۶ حدود ۵۵۰ میلیون دلار USDT در کیف‌پول‌های مرتبط با ایران و شبکه‌های تحریمی را مسدود کرده است
🔹
به گفته این شرکت، این اقدام با اطلاعات وزارت خزانه‌داری آمریکا و برای مقابله با دور زدن تحریم‌ها انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/693891" target="_blank">📅 10:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693890">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9abd452db3.mp4?token=oxbfNF6a8Mkk09FscazCD7KXbX52wNEndAVM15wHcS6J3GsiKOHp33SN51sthAt33vgfRYAu3mP8WPpNnR4h2IsnV0EEYBW3eoxuyqP-eHagNfwJprd9MXKDgSkmRyQXL5587CN5SZuT-XG-8IFKyO50xWg_cnJtI06P76ZoSRsU-Chs6THM9AGtvWE5uK_kSkUAW2L0egTJErow1ztW0Ac6eCzhVwLkCQwVke3WOcZt1dk5iVSNXBWA95x92vb0h4_DNFI5rMznNsK0PI23CISLgXWwtuXEhWVQ9_SIbkfbHLw27BK5qyTG8y6kfrL0mKY6vjWy93dBDjaL8sV43F5jVQOFo78PcBP1QZqi8FR8f-7hQq94GFAExz5imkdojt_aioeeIkYs7K6qOpkv0NOhxTKx8zI_ZPgwxjOHIzfYXsaJb0A4ssjO_JnCJXyc027K-JfoUEB8fr7vW5mYA4765G6MBdlWZUEvzrVusuWcP5g9q6p41Ik9HeCYObnJB3lZeHMpOZwGerjk3RfT6mHP1WZefHHInVQAt-UsWuhF_HI3ejmOpNKOQYlf_S-zoZNkv6hpx3RZMdMlZhQZZzE3WY8AlGV2H8ur2c4awLO_PccpHiyCnZnEGBGGIeFBDJrWpNzHtG-KoAVIYlTabokmTW_7RNhOB6MwQrnlK2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9abd452db3.mp4?token=oxbfNF6a8Mkk09FscazCD7KXbX52wNEndAVM15wHcS6J3GsiKOHp33SN51sthAt33vgfRYAu3mP8WPpNnR4h2IsnV0EEYBW3eoxuyqP-eHagNfwJprd9MXKDgSkmRyQXL5587CN5SZuT-XG-8IFKyO50xWg_cnJtI06P76ZoSRsU-Chs6THM9AGtvWE5uK_kSkUAW2L0egTJErow1ztW0Ac6eCzhVwLkCQwVke3WOcZt1dk5iVSNXBWA95x92vb0h4_DNFI5rMznNsK0PI23CISLgXWwtuXEhWVQ9_SIbkfbHLw27BK5qyTG8y6kfrL0mKY6vjWy93dBDjaL8sV43F5jVQOFo78PcBP1QZqi8FR8f-7hQq94GFAExz5imkdojt_aioeeIkYs7K6qOpkv0NOhxTKx8zI_ZPgwxjOHIzfYXsaJb0A4ssjO_JnCJXyc027K-JfoUEB8fr7vW5mYA4765G6MBdlWZUEvzrVusuWcP5g9q6p41Ik9HeCYObnJB3lZeHMpOZwGerjk3RfT6mHP1WZefHHInVQAt-UsWuhF_HI3ejmOpNKOQYlf_S-zoZNkv6hpx3RZMdMlZhQZZzE3WY8AlGV2H8ur2c4awLO_PccpHiyCnZnEGBGGIeFBDJrWpNzHtG-KoAVIYlTabokmTW_7RNhOB6MwQrnlK2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو پربازدید از دزدی خانوادگی در یکی از خیابان‌های اصفهان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/693890" target="_blank">📅 10:19 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
