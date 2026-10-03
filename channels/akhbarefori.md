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
<img src="https://cdn4.telesco.pe/file/CTVfq0lPhVwc7XBGgMfy5ttbF_jA3hbT5CTEDLEFwy27SsAl1-QE-5PjVo_wW5O9B9WCBXA4UwfKDpqLjFKzNIK2ZJss7Q2PNYkZAZQZm-foi-VK0kKljP-Qukk38hdT6HU-EWe4WA2V0c3MIqOYRunDx-ULgISg4dPHJ_g3_tAZkai_01H3xY0_amUbpBeIzWH87vzv6SDsVPPnTdYnPARTcVc6Li0muDe6ivMRJ9GSAyZUqX9YXg2I5o6y74-0mgLVVbKpgEHsCku8eaOFMKF4ekhOim-4s7jHTC9VHlKqPM2XnfZxpgTXwRuoogOYJGIgckA6IFx4ztCHJ8-wWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-695102">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
دادستان میبد از تشکیل پرونده قضایی در پی فوت چهار نوزاد در بیمارستان این شهرستان خبر داد
🔹
علت دقیق این حادثه هنوز مشخص نشده و احتمال‌هایی از جمله قصور پزشکی، قطعی برق و مشکلات زیرساختی بیمارستان در دست بررسی قرار دارد./ ایسنا
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/akhbarefori/695102" target="_blank">📅 12:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695101">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
درخواست پول بانک‌ها ناگهان کم شد
🔹
بازار پول هفته گذشته با یک تغییر عجیب رو به رو شد و تقاضای پول بانک‌ها از حدود ۴۲۰ همت به ۲۹۰ همت کاهش یافت.
هر چند بانک مرکزی سیاست‌های انقباضی را در پیش گرفته اما در شرایطی که تورم همچنان بالاست، کاهش نیاز بانک‌ها به پول چندان منطقی به نظر نمی‌رسد.
🔹
برخی تحلیلگران مدعی‌اند که شکل تأمین پول بانک‌ها تغییر کرده و بعید است نیاز آنها به پول واقعاً کم شده‌باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/695101" target="_blank">📅 12:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695100">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
تیراندازی در مقابل دادگستری مهاباد
🔹
دقایقی پیش حادثه تیراندازی در مقابل ساختمان دادگستری شهرستان مهاباد رخ داد؛ حادثه‌ای که در پی بروز مشاجره لفظی میان چند زن، با ورود مردی مسلح به سلاح کمری و شلیک گلوله همراه شد
🔹
در جریان این درگیری لفظی، مردی که یک قبضه…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/695100" target="_blank">📅 12:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695099">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f299fb69.mp4?token=iaLomUV0HAYu7aBS1oJQ8i57UrBgHbk_MolNkRp5ooMtisIBGft5X0Wi2DpdqIDWc7DXnmBVp6Tbvauya4ttatoi4nOiVrSltUcUUJJoS3lBqi-gebXxtf-Qt5wBXvKCUX9nd9J2bge480coM74pgVCFiev5OFsAaCatcHN4F37jgpFYP_ZZntZyVpJThxghliIUIU-N62kXi-RysyAiAQTOkCDgEP-Yi_izjbuJMlVGyoi6hqzQet0F9ZWijYFf8whRRWqFAtAbbhYaKs_cpARxl8oC5ETrKdca6mcKiARqS5EXU5d9OGvnsA9ErxJ9lZd1To3bheBM9VtIHZHZt4B8JXV2wxnt_sScCrUJl12HScaAEpkhq1YezwUPLDkMP0jJLYjrfQtP2ErWKeicHdsHbCdnE6a8ZKz81zSXtR6uBrwdaGppscn251JnRaJ0AL156eWasFzCW8FQmQZ1a_CPDlgwDzM0xChB8NC5P9-dQ7PWFKy7WmKD_E7VkN0qji0uLuIGywrphndXuVxowkOg-DMsJUEsJraLAwSckCqN3bAxxdc4xAPu9xxci4Fl-eS88Bm1nMW2kx514HDWb9SXuwBMcZyOaw9apR_-BoZM8tE6tY2E8RWB9isCwVSxQWP36qQcO5350xea3Q-2P9X50DAvkf-11vkD2hTqaVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f299fb69.mp4?token=iaLomUV0HAYu7aBS1oJQ8i57UrBgHbk_MolNkRp5ooMtisIBGft5X0Wi2DpdqIDWc7DXnmBVp6Tbvauya4ttatoi4nOiVrSltUcUUJJoS3lBqi-gebXxtf-Qt5wBXvKCUX9nd9J2bge480coM74pgVCFiev5OFsAaCatcHN4F37jgpFYP_ZZntZyVpJThxghliIUIU-N62kXi-RysyAiAQTOkCDgEP-Yi_izjbuJMlVGyoi6hqzQet0F9ZWijYFf8whRRWqFAtAbbhYaKs_cpARxl8oC5ETrKdca6mcKiARqS5EXU5d9OGvnsA9ErxJ9lZd1To3bheBM9VtIHZHZt4B8JXV2wxnt_sScCrUJl12HScaAEpkhq1YezwUPLDkMP0jJLYjrfQtP2ErWKeicHdsHbCdnE6a8ZKz81zSXtR6uBrwdaGppscn251JnRaJ0AL156eWasFzCW8FQmQZ1a_CPDlgwDzM0xChB8NC5P9-dQ7PWFKy7WmKD_E7VkN0qji0uLuIGywrphndXuVxowkOg-DMsJUEsJraLAwSckCqN3bAxxdc4xAPu9xxci4Fl-eS88Bm1nMW2kx514HDWb9SXuwBMcZyOaw9apR_-BoZM8tE6tY2E8RWB9isCwVSxQWP36qQcO5350xea3Q-2P9X50DAvkf-11vkD2hTqaVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه اهل کوهنوردی و طبیعت رفتن هستید برای روشن کردن آتش، این ترفند معرکه رو حتما یاد بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/695099" target="_blank">📅 12:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695097">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXUtC121EPkUPDVZGuHUwsN_lhupCYxo0GbWDTBYeQlOEmUMSzS_AGXLIVcLMrhjujeqa_MtZJMXfla5fbTRbow3Rl6xUTHrXFWOPYRoJXjbymxJ5hFOl-vA2MZau60DZDm60KUHVLmFhrJNZgW2n0TdxqthxQks8kcowGpucUf2Z3sZ7Yc0s_IElBc2CuNzXOwqkzyb6uch9-PTnKeHVgMNnOuRPwJpeJaOjNtVoO-F5GMLsZJMRE-dyPGmnsKd6j_ZokgbuCQDtTzoIFC59sfbyIH3kYDwdawEtFGoIamnONCea8Oe4yIiJSOy0V4awq9R1Dw5McaJKpGdcR9-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسیرهای پروازی بین‌المللی برقرار با ایران و شرایط ویزا، پروازها از لحاظ تعداد و مقصد محدودتر شده اند، در این لحظه هنوز پرواز میان ایران و‌ عراق برقرار نیست. پروازهای میان و امارات هم وضعیت نامشخصی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/695097" target="_blank">📅 12:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695096">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b3fc0d84.mp4?token=qUQk-REnk6EUYCnrzGjytOkdFxeCZLqEGOfZX6mWzk5a4VsuLrRho4QjHamDek1aEAt7fyCtSSNC4q88TvueYTKMAQ44wHD0oSif-Ok2VM9ht50O-4nuRM9UprACcbxeaBPWk6yBZkiSkc0NxagX-4upkrRkGvuek40zkGdnhV71OsAPRAs7NDDdNRS5KrTaRMbxusj39_2MBm4dy7lvl4BqRzOenxryzDxh5PsOG4q7c-yVJs2qSQRgUJWn8tduOEsgbenl9PoR6ti84Zsg3cb7cDvanYcfjuSSpkivCNHYPwpxUIjaWLQriFPmBYblBUf9IhYhdmo48G0DWcR_TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b3fc0d84.mp4?token=qUQk-REnk6EUYCnrzGjytOkdFxeCZLqEGOfZX6mWzk5a4VsuLrRho4QjHamDek1aEAt7fyCtSSNC4q88TvueYTKMAQ44wHD0oSif-Ok2VM9ht50O-4nuRM9UprACcbxeaBPWk6yBZkiSkc0NxagX-4upkrRkGvuek40zkGdnhV71OsAPRAs7NDDdNRS5KrTaRMbxusj39_2MBm4dy7lvl4BqRzOenxryzDxh5PsOG4q7c-yVJs2qSQRgUJWn8tduOEsgbenl9PoR6ti84Zsg3cb7cDvanYcfjuSSpkivCNHYPwpxUIjaWLQriFPmBYblBUf9IhYhdmo48G0DWcR_TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان در لبنان: مجاهدان لبنانی پس از حمله اسرائیل به ایران و شهادت رهبر ما وارد جنگ شدند و با چند هزار شهید، نقش بازدارنده‌ای در برابر دشمن ایفا کردند
🔹
برای احترام به این فداکاری‌ها کافی است فقط ایرانی باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/695096" target="_blank">📅 12:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695095">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
درحالی که همواره در سال‌های گذشته جنوب کشور در بین نفرات برتر هر رشته چندین نماینده‌‌ داشت، در کنکور سراسری امسال هیچ فردی از جنوب کشور جزو ده نفر اول هیچ‌کدام از رشته ها نبوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/695095" target="_blank">📅 12:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695094">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccb68a932b.mp4?token=GpZYXdjx2PkU21Xo5MC0BeS2iPVDmw_gS8ID2huvnTmfmdqV8-iijJTRG5JJrbEfy0uLFJdg2M2z42VNA6I3thuywXpQiRUEIBcfoGIpYnq6lkd0A2T82B4UYzsh8vGl9T9WMPzb9sIzF5mcJGRUOcMGf5zrUe9CyNxv_DLgdEp01Waw5wDTGkFA7syuqf6tRIm9TN2-eQxdZ5AOWt0WjmwdMHzh6sPi3lB2LR0h7hR7LwL6i-jxZe8wLeP5WAbqoqqEE0LEoE1UfGTxKuQ8EfKMt-vXVZLZ06OnXL8MXmlosHyIKGYR8lg0JpSD5lfsHLGNjIgUmRobAhcx4S-kGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccb68a932b.mp4?token=GpZYXdjx2PkU21Xo5MC0BeS2iPVDmw_gS8ID2huvnTmfmdqV8-iijJTRG5JJrbEfy0uLFJdg2M2z42VNA6I3thuywXpQiRUEIBcfoGIpYnq6lkd0A2T82B4UYzsh8vGl9T9WMPzb9sIzF5mcJGRUOcMGf5zrUe9CyNxv_DLgdEp01Waw5wDTGkFA7syuqf6tRIm9TN2-eQxdZ5AOWt0WjmwdMHzh6sPi3lB2LR0h7hR7LwL6i-jxZe8wLeP5WAbqoqqEE0LEoE1UfGTxKuQ8EfKMt-vXVZLZ06OnXL8MXmlosHyIKGYR8lg0JpSD5lfsHLGNjIgUmRobAhcx4S-kGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویری تلخ از آب‌رفتن پول!
@titretejarat</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/695094" target="_blank">📅 12:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695091">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تصاویر نفرات برتر کنکور  سراسری سال ۱۴۰۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/695091" target="_blank">📅 12:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695090">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ویدیویی پربازدید از اعتراض به قیمت بنزین در آمریکا در گردهمایی با حضور ونس
🔹
این فرد معترض، هدیه ۵۰۰۰ دلاری ترامپ به رای دهندگان جمهوری‌خواه را هم به سخره گرفت‌.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/695090" target="_blank">📅 12:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695082">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6jVi2rLviktNizAsvdOxLz5LauJ2b3GChf0tFOQvjrJuMjx2cBqBrSIDbt0QFXHMnVYYyoVAiwXvFUVNuV6MgKbfwMTa2cacdpWFe8YNucbIGk1k_w2YwPWc5vZmqigRDauk69VS1_S6J_EK7FTdMR7JBt_Ia5m_-DYaS-HFZdxnZc_HZuGWwjqc4xUg7NIexQbx6xTn_9PyqP9bwoIZRaf5ShjMaVP4B8n-e3zsNkV4fYvfUDLQFqH-ayEqOD5pQ_7FsWBXJoUMNKhfJ5ovfyLRLkQIEOgU2AvqwMkbpiTytTVoGFhfCcZgxajdzFi-oVWHA9OSbbUe0t8wcowaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awi74xrYzQSd_RCONd4oDaJZNu6-j8LfPi9inruns5Sel2gLl_0jc0aq8XyD6J5wXoNgy_96rVN_tx_8tpbrii2chZHMRb_M7Y1tGm-b7oyUsdTE7ITSdV3Gbt04ByEpUD8btxRH5Uh2xfqIuLMUYPRWqRjGi2fx7slqzsa0YuiqZqHkFn4HvBFjsVappPJRxcms1eZt7jVbAyxp6AwIppC_97FRbLIjLkx6653BaJAVBpPpWADJxWCEdbXSTBnBSRYUcMsezS_fMUP04HrtnRMhKkDavZ_zUu7a9zOQErEI2owAFqmLzihgNbYQlHp0IJlBWUB3kPhghSv7QhTyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/of1F30rVmJwokHGFAsBfPocr19NTL71ASGqF-qm_ikr8ay6mo75RsEskazVeoNrlsueBvAQN6oizcWuvJ5XmZp6Ba84Fw3OrTmodLLtCLMDIQQpvfu44pslWWPD27-GHNTv9WjEd_VUvYwGbpa4CmOsdW4k3QwlARh4pXvhekkBsxHpSWMnERcKaBjkzKyTwa8Uglmw9OwmBjNffKPyh5lB7yo8s4SKDxejZFWtjW9fL299Bccain7Oadho1XTwZv4WPDOjFLq78XDEGkKUSJIa_Fs94g3nIpO213fgJcyf5PHq6-K7VTzhmQMWcB5RY2THz2XIV_1EhMQEGrA9drg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Em5Ld-4bO_yVtMWhKtpbcp9RCJC9oq-zMdJ1PSnyziNy2Jn_KFGD-qzFLf_-Q33-sp9OVaM135SRZdULmfgzltKeLlvwi7KmfBkV1R9aVCH5_58YB5_VPlkQO0_abLwYlRmaT1TU16Q5hapZK_V3iFKnECSBP758ztZcYRrb4pHPd4Nv0rs79rfJ8TGMl7EXpBWH9-JaT5H_PtscyvbkHJ_hfqPtg2VR1iqMIdMdYTldrBvyi3J-gyn-1Mf2Q7rbkv-kghD3OnxlwBk4ps9zeptnKK6vjyj8yQ1NUeTTr3UtZ5oU54I1zz6BcKkqlFPP0nappiX8mNxhshIVsmdBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/suo8VvXPes7RA5G6KS8YGRucSEk9DWRuQGcmt-OW_UgdR0Wb9agQXNCbbxTo97u7U6OZ9mS0LI-EXoMHvz8kDqns2p5jdzR4-thOyXJoGD0QNMHXh6RdasJkWfRWMbuUVVKXeRwFE32A33EabHbazSPADSBWHxKi_k2MmHpFAR_E_I9x4kZbgWk2h23x79ojYguqfyc1r16GpAjTd1txPfl-V_X56A666nCUG8bflzJjNeM7nDBXTeW23b42-XLHvGQZ-AEShNOYZBPXnRUmQht_KVpnDiXx3RQox347r5YwVlnq6YsOwa9tKupDRhVpkEga05rgXHxhl9LYEcKRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPjwXyNbSpv9cO6FR6AD3-kDQ3NE1xBvHHUjvcP_vhbUDt9kaT6ZWJT6gwK9DdJlt42B24WU5qGU8H2qqhf-31vG7WZSFivD0XVbgTeHggeBnOMM1NBFrx-EOHCngE-ZGcIdE_zh14_1Sr2asi1qO8-GcPMCt_BesGI0vTr_1_tt4kq5JDMTlo-TvDK165IHL6NfoHgwoj_PUmGSjHPxTUBK16ek589neXHTBvCoEAN4pzDcS8674CvQRcQTzivKljnhD-uveqgHa71ApKLXDZxUjQKBpmS26uVrsa92a9egndyBvTjcBnH7XxsBIYM2qe3lvzKEgdt2jy-N4KWkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heWJViukE-yFT9UCwrMMnzPenfxgeJZCLMSWEcFXWKTqOoS6z5VE-yRc52K2G8IiNs4vj8xpfxqnilS2IfdFqLBe5XpEbjWcY8ad3mGtMVBaM5_5Hzga5c78tKXQb1a3T17WAmtD8KxxRq8ts9uUHE38CvWrQNjj88FclQRVq8FwslCZ7QXbvZZddJwAV2OJW-I0itEaDYXeBOedU9WturMe2XSWmLseZiS2qc9flZPzpEssPHGFe_uyqXJ5Ae9FfvC-qSC7-vfpObtQZfLBdWq_db2OYRcOOjYhJNHGddsdlDDLvoGsRZLxQe1oxmcXbomKVEYinPSGbz0zK9xj5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش آروین حسینی، رتبه دوم کنکور تجربی در کنار دوستانش زمان اعلام نتایج
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/695082" target="_blank">📅 12:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695081">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231efd4cb4.mp4?token=rz4C8aTrGW5VZqpYnBYNtNXRQ6TGjbxqizrWsC2HoTdtBmzNMfdmLd9EFhhqyJod4oDxiGd5Z1FM6PH1UsoqG-Svwny0MeF-zliBFyjzlqsXIfj_03XfWoeJGWd6cYm_-53Cy3IPRlBqu0vpuXUc39mDcjZnv69TnISv0-OaC2HfFa1okc4slu--KCZVwBjL4_07L9SUyDqVopfXnyXpJShjBOLkz5azJFaOLPUuM1BjWSw7-88BbRBxDB_lf9ha0Nvf7iYvVWAmh9mbnAUAAj0_qzFJ54VVe52k7O1PmXHNkpZxSXwmdDPYdIioGvACRL2AmUBlR1kKPE_xPLcDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231efd4cb4.mp4?token=rz4C8aTrGW5VZqpYnBYNtNXRQ6TGjbxqizrWsC2HoTdtBmzNMfdmLd9EFhhqyJod4oDxiGd5Z1FM6PH1UsoqG-Svwny0MeF-zliBFyjzlqsXIfj_03XfWoeJGWd6cYm_-53Cy3IPRlBqu0vpuXUc39mDcjZnv69TnISv0-OaC2HfFa1okc4slu--KCZVwBjL4_07L9SUyDqVopfXnyXpJShjBOLkz5azJFaOLPUuM1BjWSw7-88BbRBxDB_lf9ha0Nvf7iYvVWAmh9mbnAUAAj0_qzFJ54VVe52k7O1PmXHNkpZxSXwmdDPYdIioGvACRL2AmUBlR1kKPE_xPLcDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهرهای رتبه برترهای تجربی همه جزو شهرهایی هستند که در جنگ، تحت بمباران شدید بودند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/695081" target="_blank">📅 12:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695080">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
بابک زنجانی شرایط همکاری در طرح تاکسی‌های دات‌وان تریپ تشریح کرد
🔹
طرح جدید تاکسی اینترنتی «دات‌وان تریپ» با دو مدل همکاری برای رانندگان و مالکان خودرو معرفی شد.
بر اساس این طرح، متقاضیان مشارکت می‌توانند خودرو را با تأمین ۲۰ درصد از هزینه توسط هلدینگ خریداری کنند و پیش‌پرداخت را بین ۲۰ تا ۸۰ درصد انتخاب کنند.
🔹
مبلغ باقی‌مانده به‌صورت اقساط ماهانه پرداخت می‌شود و درآمد هر سفر، پس از کسر کمیسیون، به راننده تعلق می‌گیرد.
🔹
در این ویدئو جزئیات متقاضیان خرید و مشارکت در طرح دات وان تریپ توسط بابک زنجانی کامل بیان شده است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/695080" target="_blank">📅 12:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695079">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/695079" target="_blank">📅 11:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695078">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769e47fdeb.mp4?token=pcebvYpA25CKUQhWPdAvCkaEuJOOSgN6GLdTvzM7t0leL7yD2irhTpD4QjMssI83GHf8J7vWD4RFSM5nJH-Rt7spyZfnzo57IYEbolXnrlRiV5_NqEnYliTLtOnskhD5exj1Sc0rRLfRrqNNpV5wy2d-zn4uklo1qngSXULprPOu7a3Y651QK9zWmzH9rQY1t7cDlqhZsDZj74T0UTP7fbn1VK_gEfUaqss-q95hXDPTVGk1iB1fQ1Y1iXTta7D7iQWExC8r95aG9vA55hD9aro2sxGDQryRA4qPy-7MqeOZoLYOLgqGwanddVubvZVSRvxaKymUZGZhR7PrgMU5fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769e47fdeb.mp4?token=pcebvYpA25CKUQhWPdAvCkaEuJOOSgN6GLdTvzM7t0leL7yD2irhTpD4QjMssI83GHf8J7vWD4RFSM5nJH-Rt7spyZfnzo57IYEbolXnrlRiV5_NqEnYliTLtOnskhD5exj1Sc0rRLfRrqNNpV5wy2d-zn4uklo1qngSXULprPOu7a3Y651QK9zWmzH9rQY1t7cDlqhZsDZj74T0UTP7fbn1VK_gEfUaqss-q95hXDPTVGk1iB1fQ1Y1iXTta7D7iQWExC8r95aG9vA55hD9aro2sxGDQryRA4qPy-7MqeOZoLYOLgqGwanddVubvZVSRvxaKymUZGZhR7PrgMU5fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان در لبنان: مقابل رزمندگان، مجروحان و خانواده‌های شهدای لبنان جز شرمندگی احساس دیگری نداشتم؛ این مجاهدان دارند جهاد می‌کنند/ خانواده‌هایی را دیدیم که چند شهید داده‌اند، خانه‌شان را از دست داده‌اند و در اتاق‌های کوچک زندگی می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/695078" target="_blank">📅 11:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695076">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb9b5282b.mp4?token=GnfmqammsoJB1k5v8ajuVdyfvsAxGdLZuQ1VSsVBucdwuvjww036jtD5FoU16rzwlB9bx0NTmuag41zfZMcjTaMU_-PJOOyvc2o2dmkOusDD9lYQQ86gFXCY1svuD1l2awCf7tZCPeHu1QYKfu5GV0VWq-Y-EFEu6rrY42Q5gTMPe2qblnotBmt8u9921fi9mqeySCZXKQZhxc4uwKpA8HFIY6Z6Xhx10-i_rjWkJN4gg5rtcdWhAL5NZVcjTORD-s-DT2HqwSlmMrtpnZ-iCkA1zloDwFKfK1Jrcg9AIlZSpKm4NZxUWYHm-BFjHYL_gJ-uEekndx-XllNqVTS0MqZiGHFR6h5D5kkMGt_Ihs0BMydw483xJdM4t2ZZXn4-R9SipwCIaiOJ09ZWk9qDZ3NoHSkxtTALNO9ZNyslsdvsko7GIg0wuUB-Tjkv8hr_YCS2zQerkrJHAjVasi_pMhPeZgXvyjBXvRc_NBYWS4ZmxbiOkqRpMmcHsXbhP4Sdu80wlj2spWteYA0gmhHKjTqeYWCHQhtK9OBsmCBPVDrfUt_-_Cb47kIuMa3ERgpWBdsK3DtiLk3gIlJKtNrtKh1b_51_9QpaWrdbAc5lJSlZ0mZfDIFUDBG_OttVKpRNVXsd9FUe6fR2bb5gMTKYFl8ngx5_GmgxzXVMSFzSxSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb9b5282b.mp4?token=GnfmqammsoJB1k5v8ajuVdyfvsAxGdLZuQ1VSsVBucdwuvjww036jtD5FoU16rzwlB9bx0NTmuag41zfZMcjTaMU_-PJOOyvc2o2dmkOusDD9lYQQ86gFXCY1svuD1l2awCf7tZCPeHu1QYKfu5GV0VWq-Y-EFEu6rrY42Q5gTMPe2qblnotBmt8u9921fi9mqeySCZXKQZhxc4uwKpA8HFIY6Z6Xhx10-i_rjWkJN4gg5rtcdWhAL5NZVcjTORD-s-DT2HqwSlmMrtpnZ-iCkA1zloDwFKfK1Jrcg9AIlZSpKm4NZxUWYHm-BFjHYL_gJ-uEekndx-XllNqVTS0MqZiGHFR6h5D5kkMGt_Ihs0BMydw483xJdM4t2ZZXn4-R9SipwCIaiOJ09ZWk9qDZ3NoHSkxtTALNO9ZNyslsdvsko7GIg0wuUB-Tjkv8hr_YCS2zQerkrJHAjVasi_pMhPeZgXvyjBXvRc_NBYWS4ZmxbiOkqRpMmcHsXbhP4Sdu80wlj2spWteYA0gmhHKjTqeYWCHQhtK9OBsmCBPVDrfUt_-_Cb47kIuMa3ERgpWBdsK3DtiLk3gIlJKtNrtKh1b_51_9QpaWrdbAc5lJSlZ0mZfDIFUDBG_OttVKpRNVXsd9FUe6fR2bb5gMTKYFl8ngx5_GmgxzXVMSFzSxSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت روش ساتنا، پایا یا پل را بدانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/695076" target="_blank">📅 11:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695075">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGyA1RbK4Aigb3j9z4O5VFiNxH1X0WPD7x_ryn13Z9Bt30DGpR9mFHsKEVeXS3K3ZzTKO8OP8e1yGI8Pf9YORwm9HdK7Fw0LmZBdr8HchMXwQXx_VpII2UbCYVzrbYMZALcZ3SkXxKOrYSqF6OucUi6yW3K8Xurqmzm84mLoPfGoY_waWnWkXzpm4gwU8P7M7w469PY7o-eNXzwlWjJvcHr_xbygSYAodteM44O5G1kjJ0_oi0kTZbUvqg0lfhv71pTqOuMaGclFawZazGi7LUPQzta_qpAz76HCt7GIVpwzwJ_k6avZeZms7FN6F8qwG0u-nqZS0vBpCGqOhz5H-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیلم جدید از درگیری در هواپیمای فلای دبی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/695075" target="_blank">📅 11:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695074">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W4Dc_SwFKK0MwIYGVqeqT9KXpiDtzp-SU4GJmi4vEj5E2232vei2GueNOSnrTIUL3XdindzrsB1px0v5j5bvPeLjviNXPoVr0J7XeEFD36d9OUtQ7BakpindlE5ZPKj6wIJkfNfSQIPpoJxosF9aiVOWaKUUkfoAKm7mYtZOH8uBWCeRFOtYWKOHGJaJ_kWpgzUEXoSz2c6i1inhr-c39TCYUJibcpHG9E6YosbA4MT6vFJLcgezgLJPVNj-LW3r3l01ZB5YGm9EfCy16b-bJb37r_F8H5nGPjPE5FAOYnfxtXtljQiYqBTTYqQaWAImT-OfNCpjlr9F_oN2Aiw7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیوید کیز مشاور نتانیاهو در هفته گذشته: جمهوری اسلامی ایران در تاریخ ۱۱ مهرماه ساعت ۴:۳۳ دقیقه بامداد سقوط خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/695074" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695073">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تیراندازی در مقابل دادگستری مهاباد
🔹
دقایقی پیش حادثه تیراندازی در مقابل ساختمان دادگستری شهرستان مهاباد رخ داد؛ حادثه‌ای که در پی بروز مشاجره لفظی میان چند زن، با ورود مردی مسلح به سلاح کمری و شلیک گلوله همراه شد
🔹
در جریان این درگیری لفظی، مردی که یک قبضه سلاح کمری در دست داشت، به سمت زنان نزدیک شد و اقدام به تیراندازی کرد. جزئیات دقیق چگونگی وقوع حادثه و ابعاد آن تاکنون مشخص نشده است
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/695073" target="_blank">📅 11:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695072">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403128c4b6.mp4?token=VQdBBszge58ZmGZh2m3y3Ao1eGt9d4la9if43vELoaPZG9YD5Z8RNck0CieeytUBMqIjtX9Z1hnxlEuahQj4TROihFiur5i0nO6GFCOIK6oNA_zx4bal0FZSKDWlL6c1L8jgMgf7GdddYY435CKw2IGHEMRmUIjLum5QlgZ7bC3OH_gyRgY9npEzxvo2pB_bU3p_n91bUOV2MUCgFgncx-QoJXeRxgme9ydjyaVG3H93jH2hVo5FDyiN591vzJPUekBVKaZPL2ZhPZ1-lYdS9xmKaXYby_j5_VvKvpe6j-uhJM2UA5jyocddY_fdH0XMn_BqLL9ehpyS_qqwON1oGgexgPgA6DQPrcnmHHUXFlv-S6Rf1DX3cpbY2_AgtK59IxxYnPPbLPxJRcxPxHWOV71XnauofPUi4AhvpAc1XdO8XMp-Yc6YheIPHmg_YNWEFsZPVesixRx5YnqVcdn1CCLbWsFWpSJuVDyPXMKrTJSBUV5ptjT3Sg_u5cfEQ22rDE24MOuNlNwSNCy0U8Mvbrlz0gpc4Xfm-hAPOQs3RJ0vWtMsf8CrtvNRXbgjjz8D0GmWcI42PIHSPSzJcNxdcaTHFxWurjK5jpQLjnO5dcNJaUhO5o_OI3uNMqjIUf1wgb3IqxJ5aByCJnltfaYeX6u9ZfjpVjA1oWRtEGGM25M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403128c4b6.mp4?token=VQdBBszge58ZmGZh2m3y3Ao1eGt9d4la9if43vELoaPZG9YD5Z8RNck0CieeytUBMqIjtX9Z1hnxlEuahQj4TROihFiur5i0nO6GFCOIK6oNA_zx4bal0FZSKDWlL6c1L8jgMgf7GdddYY435CKw2IGHEMRmUIjLum5QlgZ7bC3OH_gyRgY9npEzxvo2pB_bU3p_n91bUOV2MUCgFgncx-QoJXeRxgme9ydjyaVG3H93jH2hVo5FDyiN591vzJPUekBVKaZPL2ZhPZ1-lYdS9xmKaXYby_j5_VvKvpe6j-uhJM2UA5jyocddY_fdH0XMn_BqLL9ehpyS_qqwON1oGgexgPgA6DQPrcnmHHUXFlv-S6Rf1DX3cpbY2_AgtK59IxxYnPPbLPxJRcxPxHWOV71XnauofPUi4AhvpAc1XdO8XMp-Yc6YheIPHmg_YNWEFsZPVesixRx5YnqVcdn1CCLbWsFWpSJuVDyPXMKrTJSBUV5ptjT3Sg_u5cfEQ22rDE24MOuNlNwSNCy0U8Mvbrlz0gpc4Xfm-hAPOQs3RJ0vWtMsf8CrtvNRXbgjjz8D0GmWcI42PIHSPSzJcNxdcaTHFxWurjK5jpQLjnO5dcNJaUhO5o_OI3uNMqjIUf1wgb3IqxJ5aByCJnltfaYeX6u9ZfjpVjA1oWRtEGGM25M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال‌ شده از مدرسه متفاوت یک دانش‌آموز به مانند کلبه‌های سوئیسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/695072" target="_blank">📅 11:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695071">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: غائبین آزمون‌های سراسری و تربیت معلم می‌توانند در انتخاب رشته براساس سوابق تحصیلی شرکت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/695071" target="_blank">📅 11:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695070">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر TV</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHe0x4aA_E_hi2zO1GO9D24bNcjEtPbXQ_ulJ1mUKkM_JibLk3KP1XjWTw2T7WLn9iOuinqm5TO_vbdPbpV-HsI___gxfkWhZNNwjrPh_tWl7_MWa6M8MAij6kNBH_PkngizWg9vFEprMj7joyy9B7HFazD3FkPSFp-h6P53xiGv02CAoqxNRmtbWCFhynghg9rFQ-nDkHVLWIdY0ORCMndK7Yy-d5VAfmp008gXEnwS7LJswuHseRaxn7cwlChenPkmS6u6FJcMzg7E2Omgpu-9Plt1fk6oce5ntJhCKC22EEthxuWwfUB4nH-AprTLz278sxxWiY3sCYBzYzsEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#اینفو_تیتر
| تورم نقطه به نقطه استان ها
🔹
یک شکاف تلخ اقتصادی؛ درحالی‌که تهرانی‌ها با ۷۴.۶ درصد کمترین تورم شهریورماه را ثبت کردند، ایلام با ۱۱۴.۳ درصد و هرمزگان با ۱۱۳.۸ درصد رکورددار گرانی شدند.
@tv_titr</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/695070" target="_blank">📅 11:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695069">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
قیمت دلار در بازار آزاد به ۲۶۵ هزار تومان رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/695069" target="_blank">📅 11:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695068">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سود سهام عدالت حدود ۲.۵ میلیون تومان
مدیر نظارت بر ناشران سازمان بورس:
🔹
میزان سود حدود دو میلیون تومان است، اما عدد پس از برگزاری کامل مجامع از سوی سپرده‌گذاری مرکزی اعلام می‌شود، ولی به نظر می‌رسد مبلغ سود بین ۲ تا ۲.۵ میلیون تومان باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/695068" target="_blank">📅 11:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695067">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سردار نقدی: اگر آمریکا بار دیگر حمله کند، حمله‌اش به معنای خودکشی خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/695067" target="_blank">📅 11:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695066">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN9VCLhj11LouHTAvXxRwmbtz6Fd3ZySz9talThyz4HWYE5fCPLXUWWufdUpHm18mhYbs80d5-H7CVi48JfnjqFQVI54teHwz3HqSsllgYdALcNIPsl8MmABF8mOXbxqPRHzev6b_S8wy0Pxs4Fl_hvGVhGjrgg5quYy77TRfkyuJEkYOdnsAEOeojkKLJdRjHXrjHQB_zFUliLPtWljT1tN2-i0ZmxsvpcHiVoiA2aRgoOMNJ_dzSNoYLsvxMe1KLwXJ84woiXq6AvjBYXDoQOw3plpGpU0ZOLL-4jsGVnMSkYSXBZA2SPO5cAv95Edq9hIlnejjbBgWOJ9QkhGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهرهای رتبه برترهای تجربی همه جزو شهرهایی هستند که در جنگ، تحت بمباران شدید بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/695066" target="_blank">📅 11:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695064">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ca291056.mp4?token=FsPpUIbr_9p9H1DoxIY1AfW1L_Lr-ATThRbC1-h3njGOiQJClUG5-boMGYHkECuAxqUzC-cmSFCwkyqP3XG5Ydiq6ASvWBVsmuRaZ-fQaFr7kJngPV7jIMYoHrG27kU58bcBjktxJdxxjZD1u0NJeSDUPXTCbOIQgVyxcMkfJKD-uLhRVm_5vCJhQSj6ycrT6qkw_9iZCKUGjtDYZ5CzitGrO_JDu4nFqREbf2mmlzVZ7xxLoJXVptHM0WmNQnHPeDpAb8cid-X3llRVH6T51pGuT-KrNHPa6uQtOe4ca3y2yIMDU0aTGFIQs0_m9BVqZ9Gv1g_ItDtfOcrG8ip7jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ca291056.mp4?token=FsPpUIbr_9p9H1DoxIY1AfW1L_Lr-ATThRbC1-h3njGOiQJClUG5-boMGYHkECuAxqUzC-cmSFCwkyqP3XG5Ydiq6ASvWBVsmuRaZ-fQaFr7kJngPV7jIMYoHrG27kU58bcBjktxJdxxjZD1u0NJeSDUPXTCbOIQgVyxcMkfJKD-uLhRVm_5vCJhQSj6ycrT6qkw_9iZCKUGjtDYZ5CzitGrO_JDu4nFqREbf2mmlzVZ7xxLoJXVptHM0WmNQnHPeDpAb8cid-X3llRVH6T51pGuT-KrNHPa6uQtOe4ca3y2yIMDU0aTGFIQs0_m9BVqZ9Gv1g_ItDtfOcrG8ip7jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واژگونی ترسناک کمپرسی بر اثر ترمز بریدن در کازرون
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/695064" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695063">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
آکسیوس: آمریکا در «ضد حمله» عربستان به یمن شرکت نمی‌کند
🔹
عربستان سعودی به همراه نیروهای مزدور خود در حال آماده‌سازی یک «ضدحمله بزرگ» علیه جنبش انصارالله هستند، اما آمریکا دوباره درخواست ریاض برای مشارکت در حملات علیه یمن را رد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/695063" target="_blank">📅 11:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695062">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e8ca9871.mp4?token=GKHwPXTHTLift_sC3QrkwhwDOCcZYXYMgIGlFr6ApcDZjLr88Tzy4wC1FbpaqwzV-oztudUPhElgGFNDyk8UGxzSXin5TF8Db1QWiVwwV_lxMGmmJft8dsMCyQ3CNXIh5KfCda78THIWMef9vwklP_ePX6R2-A-p1DAdHTfHRxDA8KyAg0RTq-GJakxlTMFpL-_kC6AC87b7JO-oBmwP9El1-lH5h6jQhShoY0y7PsrWhFBrfxW9v5qpwxBXfKtuatUJKgwoEvDUNqeWVwqR5YMYVd9Rb3qJWDePUuEmuI15EVkIdUvFPsac-FbdQBwBmw3oRexuPNvqANHUtRB_7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e8ca9871.mp4?token=GKHwPXTHTLift_sC3QrkwhwDOCcZYXYMgIGlFr6ApcDZjLr88Tzy4wC1FbpaqwzV-oztudUPhElgGFNDyk8UGxzSXin5TF8Db1QWiVwwV_lxMGmmJft8dsMCyQ3CNXIh5KfCda78THIWMef9vwklP_ePX6R2-A-p1DAdHTfHRxDA8KyAg0RTq-GJakxlTMFpL-_kC6AC87b7JO-oBmwP9El1-lH5h6jQhShoY0y7PsrWhFBrfxW9v5qpwxBXfKtuatUJKgwoEvDUNqeWVwqR5YMYVd9Rb3qJWDePUuEmuI15EVkIdUvFPsac-FbdQBwBmw3oRexuPNvqANHUtRB_7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به دلیل حملات نیروهای مسلح یمن، دود از پالایشگاه ریاض، متعلق به شرکت نفتی آرامکو، به هوا برخاسته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/695062" target="_blank">📅 11:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695061">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU8dH6VAJl3owiOiFCO6te2Vj8RGxCRGQiUtmgi179GKFwL8SvditCtKVFL84JNnIRLW1gAoP1mH3XIrmoVkXLZqZ-f9tIAU1YpkkxBMXFuVJMjvKXuJzfZyTDnOXj8QzSF9_bH6OeYfyBVztuGwVLWTQd34J4lObxGFYMnGtWw5Tt9m39GDzTuHFLlI3_YF7zRHQf94v_cYrdQX9l7wIY7pnkFpLTKkqqS5P1wr2lwP_CitL5PSEwhy3HCna7ZbuP3pDp0m1ZtqN5i2nJhbSgzeYer-tqILsGckLM5tjv0ldYQGcDXCGgBsHxDWyj0colJ-Q6xmUBgkNgxCgyrfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
تندیس مشک حضرت عباس (ع)
به یاد حضرت عباس (ع) باش؛ همان علمداری که در سخت‌ترین لحظه‌ها، تکیه‌گاه دل‌های بی‌پناه بود.
این تندیس، یادآور وفاداری و سقاییِ بزرگی‌ست که هر بار نگاهش می‌کنی، دلت را به امیدِ یاری و دستگیری گره می‌زند.
✨
مشخصات محصول:
▫️
ابعاد: ۲۲.۵ × ۸ × ۶.۵ سانتی‌متر
▫️
وزن: ۶۷۰ گرم
▫️
متریال: پلی‌استر
▫️
طرح: مشک حضرت عباس (ع)
▫️
کاربرد: مناسب دکور مذهبی، هدیه معنوی و یادگاری ارزشمند
💰
قیمت: ۲ میلیون و ۳۹۱ هزارتومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/695061" target="_blank">📅 11:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695060">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861734d442.mp4?token=B-ixcBQYYsTmQUbbdYX99yT8bQClz634LE0bFBCUKk7U2wW5WZHZDFVkkngYhgMAfADpqf_JRV0IAebGIZWJKDhQkJmWgBUGQGXLTESrvQf4YsZKDAkPl-iVXiLyT9Pw5gKDCGTUUn886RZfqlo2ZEkrtHCl6xWM-u6UBt98lH3Su2M6a1BUu1MLpaE0uf6F62PthK5PhkwmiYaRhS52FUQxXVvdMe2Dg5pAWSHGXmZjfvpjinSZxhgZAHf4EKKVsBuGFWByXBchqtD7NNM1d3JeXKXPQoeLEd2UWHrOAIeoqiQ-Z-oHBXQ9BcpxQnrVeW-0wNgfaZXhldeKYzfnFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861734d442.mp4?token=B-ixcBQYYsTmQUbbdYX99yT8bQClz634LE0bFBCUKk7U2wW5WZHZDFVkkngYhgMAfADpqf_JRV0IAebGIZWJKDhQkJmWgBUGQGXLTESrvQf4YsZKDAkPl-iVXiLyT9Pw5gKDCGTUUn886RZfqlo2ZEkrtHCl6xWM-u6UBt98lH3Su2M6a1BUu1MLpaE0uf6F62PthK5PhkwmiYaRhS52FUQxXVvdMe2Dg5pAWSHGXmZjfvpjinSZxhgZAHf4EKKVsBuGFWByXBchqtD7NNM1d3JeXKXPQoeLEd2UWHrOAIeoqiQ-Z-oHBXQ9BcpxQnrVeW-0wNgfaZXhldeKYzfnFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواوی، انتقال ویدیو بین گوشی و لپ‌تاپ را با حرکت دست ممکن کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/695060" target="_blank">📅 11:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695059">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی: تمامی کارت‌های سوخت تا پایان سال به کارت بانکی متصل می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/695059" target="_blank">📅 11:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695058">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
انتخاب رشته کنکور سراسری از روز دوشنبه آغاز خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/695058" target="_blank">📅 11:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695057">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLxXMV2b2U1NJVwgXavyWu8l1cmkBi7cTiNS4IwMKcfyxC-9to-Bv4TrWwbeGHyW3t3QJwke5KFCgNSc_87OnMjxS6cpX8VXpNqGFKGV5xnJe85MQkUCsxAXuPpuQW3NrKoUXRAy_jQYKcLhVN3tJ5pRJg2K9fmH3SoWcVoSOF0X-a83Xh1NmdF261Rc4fcPBQM0acaJJARoLgZwiT2vaw_1hQGQcMp03LGEUTBnM8-M6VkcSxHkejpwJpW_jkMqTEO72JN4HQWzugm1r89Gz2ikuPMddjsQpGZkO6SuF_eXajfdKTw-Ujo3kQjxksqkYH4Hl7rwiSTqMgrmfq47gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
فروش ویژه فرش سجاده آریا |
🔥
فرش ۷۰۰ شانه بخرید، به قیمت فرش ۴۴۰ شانه پرداخت کنید.
✅
۲۰ تا ۶۰٪ تخفیف
✅
خرید مستقیم از کارخانه
✅
فروش اقساطی
✅
ضمانت ۱۵ ساله
اگر به دنبال فرش سجاده‌ای با کیفیت واقعی و قیمت اقتصادی هستید، همین الان تماس بگیرید.
📣
درخواست قیمت و کاتالوگ فرش سجاده:
تماس بگیرید یا عدد 1 را ارسال کنید
👇
📞
شماره: 09128044740
📲
آی‌دی:
@farshsajadeharia
https://t.me/aryiacarpet
💫
💫
فرش سجاده آریا
💫
💫</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/695057" target="_blank">📅 11:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695056">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68e89c676.mp4?token=GU1ET_DYI4wXmRhgSkdu0vvCMNisJ24uXOadRuJjTiMiDDFPRjPI2m2szr8mvrjP7IZkMT2yB1vZ1r7hdNgZ7dTU2kITugw5ZtVtl4T1oTn89uOwVmY_rsmoWI6_S6ffB8j4egv1RHuhUtm4NWpj-DZlDR5mWBk66tDYtcXiG9BhnX-xiNkMMUb8PKJWkJsHOuZn6d2YWF0POOPxfzKfuaLuSk2-iPbsfTOH1CBSD7vo1hFDMssQki9rFbLkD3wO9TXi3IJ4OFW1Lc_v19_-o2eXwswsl2TGK-4RTES9-bRxkZmihdGDf-uSzMSqkyrMI1JFmA8AzbEkNc63Pjh4RiSNGv2UsKdcXx4FQsLcheLV5nvrhAUd6nO5dlOZ4iFv3WMXr2OYQoSyDRPAe4h867H1MvSrxmDmyoHEfgn8cOG4mxjyWosC17CI-mawAGBtOfZ57mTyg9IhbSFkPUToG9QrM8AQ1MDbjfZmLqCTvvdC-yOrr3TLq8IY5aYi9XH8FWVmTx-qwgpJt1jRovuYjyvn4dbtOcoNGa1FOly5KrDqvAfLy1G44BkhdQDtF3wk7PNpbLBD0kxOtsEmKVNae_xsBWPf8rcRU0GqGlPg83D_Klwof7b8xiX3ANKUiRzZde-sG1-Rt_JuEi0y_DjHTl3uiWjIt-EUAPruS5TcGB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68e89c676.mp4?token=GU1ET_DYI4wXmRhgSkdu0vvCMNisJ24uXOadRuJjTiMiDDFPRjPI2m2szr8mvrjP7IZkMT2yB1vZ1r7hdNgZ7dTU2kITugw5ZtVtl4T1oTn89uOwVmY_rsmoWI6_S6ffB8j4egv1RHuhUtm4NWpj-DZlDR5mWBk66tDYtcXiG9BhnX-xiNkMMUb8PKJWkJsHOuZn6d2YWF0POOPxfzKfuaLuSk2-iPbsfTOH1CBSD7vo1hFDMssQki9rFbLkD3wO9TXi3IJ4OFW1Lc_v19_-o2eXwswsl2TGK-4RTES9-bRxkZmihdGDf-uSzMSqkyrMI1JFmA8AzbEkNc63Pjh4RiSNGv2UsKdcXx4FQsLcheLV5nvrhAUd6nO5dlOZ4iFv3WMXr2OYQoSyDRPAe4h867H1MvSrxmDmyoHEfgn8cOG4mxjyWosC17CI-mawAGBtOfZ57mTyg9IhbSFkPUToG9QrM8AQ1MDbjfZmLqCTvvdC-yOrr3TLq8IY5aYi9XH8FWVmTx-qwgpJt1jRovuYjyvn4dbtOcoNGa1FOly5KrDqvAfLy1G44BkhdQDtF3wk7PNpbLBD0kxOtsEmKVNae_xsBWPf8rcRU0GqGlPg83D_Klwof7b8xiX3ANKUiRzZde-sG1-Rt_JuEi0y_DjHTl3uiWjIt-EUAPruS5TcGB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداهایی که با آن‌ها بزرگ شدیم؛ دوبلورهای خاطره‌ساز
🎙️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/695056" target="_blank">📅 10:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695054">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6Ak_0a4V96rexMZa9-TlobV3u0ujHP7LRj9wRf0c17iBfZ8DZCkq8KClelLTGzPsWQQAtnnYGsl2_sA97h4jyTBMfJAJ0tgD24G-c7BY6iycnnd9AtrPZbgeTnO5M7S55fT1OVdH0Y1btummftWJE1axE-e_FXrfpPwONugCIQ7lwaw_QXWx2rUYq1R6aXVEwG0avO2hZGWQ7KDZ23sI1REYyspRJuRO7ippTCZP4Rok8cJPL-uprhLtMbksI7LACCu1PY6nEkVoFUvrXEzc74PSC4J5ZiUjEjxKmPYUWfl6hbb1WfLCcseyRCNpAUanTYP5UXEeOFH0KkgZE-KMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sg9fLjr_79pN95LBLen2upUioKv7gaCuViI7lRm00Bqy3lYOxRS5Be8D_gXO8Gw67fwIqKxGm3J11HulQTmrXOufzgJcEMN7pmtdgLIXp9c5eF4cL-PMty36lApMEW3hI-BLk9gA6nJW25NkAHxLw2lyo3QwPGTOvtBc_WrAHtrrhc3t01vLHtb4y4ATWYgwg9WISbWmJsoFuCImT0Swe1hNAEgO9CGaEsde2RM2nfHN8XuS8qi4JanPh0L0x1Mklzws32-Nu7coTsX1k-HPZZieCgKMPzbeDhMQR78KSbQhh7boCEoNMAWVBWcqo23MSzvw6zsq6vHBqbFtq-krrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اسامی نفرات برتر آزمون سراسری سال ۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/695054" target="_blank">📅 10:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695052">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cC7NnaeZJ_3wwJDKIj6ctHEx5IWkqKtSEB2zNXBbl5S2OLudMEdOQbZyleKZA3Xqnydxhz_SuChG7MbklKoUwrr9tu_nDD7i5WKuSlYgeoKaib2cRJsKSEFDOeBC1qo7w22aTExdamSz4t2XF0Hq24kc5flrRfIfvkSz_CQRkOcLbZ1d7KqUd87QjBipqqPnpwgHdwIqYdomyJHOV3GShwUqT7J7pqRpmpWHGxzIIe9vxndE-egAQJVh-DR013Su_8WUBIK2FFDjcnIG003z1d8pQsdgR61zzfONW2BypzArWSlRwy_tdYaW_n0bHBYxJW0ZO6pBDBFr7QLlyuTQlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری پربازدید از وضعیت صندلی‌های سالن سخنرانی ترامپ در آلاباما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/695052" target="_blank">📅 10:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695051">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
نتایج اولیه کنکور فردا اعلام می‌شود
🔹
نتایج اولیه آزمون سراسری سال ۱۴۰۵ فردا از طریق سازمان سنجش آموزش کشور اعلام می‌شود و نتایج نهایی این آزمون نیز اواسط آبان ماه اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/695051" target="_blank">📅 10:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695050">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
نتایج اولیه کنکور فردا اعلام می‌شود
🔹
نتایج اولیه آزمون سراسری سال ۱۴۰۵ فردا از طریق سازمان سنجش آموزش کشور اعلام می‌شود و نتایج نهایی این آزمون نیز اواسط آبان ماه اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/695050" target="_blank">📅 10:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695049">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4dhFkyi0V6BRfAeyszk90GSgtLiumRUCx9AZYGQK4WD9vwqkrhfFkpfQYVsUc37-9VCcgNh9Qf8WiSubgHihALKkVxUP4Vvh0auhd03MsshCwtTSl3AhEZUgJoto_DeidB9uktGLqwwKFmzWvN-kkHgsQeH7qQ5Or1hkANsg6GbXdNMeIu1Kz1EllqeY1jtKvn2wF6ROrNW8jfE5PIm3AXN4DxFGisdFX1NsX4UztmWEUsu-Z7TdzvrqQ_dbJoX9VvW5AxVs-QkNQhPNA2NdeuEtxoWCEg5caXyT5M6UYDGrWA19ivbwG1FsHmY7diYZYKxxj34tYnPC-F4-ooyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از تغییر پوشش گیاهی پارک جنگلی چیتگر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695049" target="_blank">📅 10:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695048">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca05b999e7.mp4?token=QIBMt5SXYjblUmli8bQJR_3lmL1pmPzRj5BcRYgCXokZOZySyd0jZvKm2KdURW8zPDyANOO35XEl0JvManr1bMZUhHUpoUv2IhCCz9LU0uGd_ecOKf-o67kfr2CspDDml8XGydKCThCDuW_YYMuQBJLOGaVVFv6ms-QddDOJ7YWKRiFpinbUVLFmlgD0iKPa3Rt0KKgkv1soQ6BHwNMPV_c-1ODhXhLDbntZFnOi5nIHBiLVuv4ivgVzDyXDADpjQjFlOK--ZfzIw8REmZxsYkG2h656nXK8zsCRLWaCX9zB126U5ZJDm9wICZuOGQ5WROW4dRFErkktRUz9DLRPxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca05b999e7.mp4?token=QIBMt5SXYjblUmli8bQJR_3lmL1pmPzRj5BcRYgCXokZOZySyd0jZvKm2KdURW8zPDyANOO35XEl0JvManr1bMZUhHUpoUv2IhCCz9LU0uGd_ecOKf-o67kfr2CspDDml8XGydKCThCDuW_YYMuQBJLOGaVVFv6ms-QddDOJ7YWKRiFpinbUVLFmlgD0iKPa3Rt0KKgkv1soQ6BHwNMPV_c-1ODhXhLDbntZFnOi5nIHBiLVuv4ivgVzDyXDADpjQjFlOK--ZfzIw8REmZxsYkG2h656nXK8zsCRLWaCX9zB126U5ZJDm9wICZuOGQ5WROW4dRFErkktRUz9DLRPxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریستیانو رونالدو در پی خداحافظی از تیم ملی: یه زمانی، همه مردم پرتغال رو در جریان حقیقت و دلیل واقعی رفتنم از تیم ملی می‌ذارم؛ تیمی که همیشه برایش همه توانم رو گذاشتم و از هیچ چیزی کم نذاشتم. فعلاً فقط می‌خوام برای پرتغال و همه هم‌تیمی‌هام آرزوی موفقیت…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/695048" target="_blank">📅 10:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695046">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
به دلیل حملات نیروهای مسلح یمن، دود از پالایشگاه ریاض، متعلق به شرکت نفتی آرامکو، به هوا برخاسته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/695046" target="_blank">📅 10:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
بیانیه دادستان کل امارات: تحقیقات در مورد حادثه هواپیما در دبی نشان داد که کمک خلبان قصد انجام عملیات تروریستی را داشته است/ الجزیره
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/695045" target="_blank">📅 10:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695044">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b42b3bc2.mp4?token=HdCDrqy_vpbikFAB1dbLaWXMta2pFfr1PGRI4bgvPAlZqOibuJUCWCkElpcmI_EnAKijrInKaQCAvkaolnE5aGgtlL4NhTgfYWKRexI9dl4eP1uZGv7v3-zJ7D6C3DzGrl3GewNiulIBikx7nR0MWNe1wh65zLnDdHfrx55n49ySHFjbiiGa9fKQllOy1HLmiuUjgBPtLURLuY_lM1UeGmtIHzXgx3bu07KvPOwpqOI5z5LshvwLDVDCpas8UgpMw3JzGEwJlkGWt9z-s-DWA7O_Tpi3ObXEi36wJ2UrH0sr5QIkvpfcd81y7kc2WCUHsX5P9stay5vnj85QjLVO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b42b3bc2.mp4?token=HdCDrqy_vpbikFAB1dbLaWXMta2pFfr1PGRI4bgvPAlZqOibuJUCWCkElpcmI_EnAKijrInKaQCAvkaolnE5aGgtlL4NhTgfYWKRexI9dl4eP1uZGv7v3-zJ7D6C3DzGrl3GewNiulIBikx7nR0MWNe1wh65zLnDdHfrx55n49ySHFjbiiGa9fKQllOy1HLmiuUjgBPtLURLuY_lM1UeGmtIHzXgx3bu07KvPOwpqOI5z5LshvwLDVDCpas8UgpMw3JzGEwJlkGWt9z-s-DWA7O_Tpi3ObXEi36wJ2UrH0sr5QIkvpfcd81y7kc2WCUHsX5P9stay5vnj85QjLVO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش نحوه جدید سوخت‌‌گیری با کارت اضطراری در جایگاه بنزین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/695044" target="_blank">📅 10:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695043">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708b6e3f51.mp4?token=fg_s6-2lL_Q3qBHOdGI_MgHcx7SdvmxlzjZTYFH9yEU5FoGNOQttuRr1LxjtmbWOjg973_jrbkYPkKXjed6lK3YzddaGTVl3smItkL2NQca4OHVSgmkGgTbsgoEWEZCcKZh614gVA5jViMsEGxGVBxV0uEciF37PEDLL0gegm5r-qYq1hCu03hZfuKWqmYCp8-31-M2Qmqd25ixOi8FHr0KJQDnydkLgZ01wyF_OouDVAjksvkKHn6RNIr7Afz8N7RmIoYpCnbDucPJFgUL252qwn5nh_QICxFMxdbw343TLscd3Rp_4lb2_KS8EswlDBPfxCskOH2dG7F-e0fF9-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708b6e3f51.mp4?token=fg_s6-2lL_Q3qBHOdGI_MgHcx7SdvmxlzjZTYFH9yEU5FoGNOQttuRr1LxjtmbWOjg973_jrbkYPkKXjed6lK3YzddaGTVl3smItkL2NQca4OHVSgmkGgTbsgoEWEZCcKZh614gVA5jViMsEGxGVBxV0uEciF37PEDLL0gegm5r-qYq1hCu03hZfuKWqmYCp8-31-M2Qmqd25ixOi8FHr0KJQDnydkLgZ01wyF_OouDVAjksvkKHn6RNIr7Afz8N7RmIoYpCnbDucPJFgUL252qwn5nh_QICxFMxdbw343TLscd3Rp_4lb2_KS8EswlDBPfxCskOH2dG7F-e0fF9-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
ترامپ درباره ایران: نمی‌دونیم با کی مذاکره کنیم! کسی در ایران نیست که با او مذاکره کنیم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/695043" target="_blank">📅 10:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
شکلات آلمانی رو خودت، در خونه فقط با چند قلم مواد درست کن
😍
🔹
بیسکوییت پتی بور ۱ بسته
🔹
کره ۱۰۰ گرم
🔹
پودر کاکائو ۲ ق غ
🔹
شکر نصف پیمانه
🔹
تخم مرغ ۱ عدد #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/695042" target="_blank">📅 10:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695040">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEp548JFdw_Ux9okdsHwcePQyGj2HEJMdAw6AuRROwH6eZg6FNdYbXqC9Q86h3LLIduLpB_aPOM4yp2PVUAJTHbXPYDkNQBayf_bu_Z41EY-4sMKt119568_xns1LZMpPzkzAhdGvkSY6KplMGRarclkOizyJQmrFHt9yEphSoBiXbbnvwmrWCyJWumx7F8lRMmlLawBK0nRS83bX5LtDtEAxR83-bSQT58yQ10FtAhHMWrGU9JvfZYTM03baovh58rYaCTmGdZeMNGTxFwBU1KLl8_6mxf7U4n5i67lMvumdhyHFffP7cjQWog0H-hus6gwedxFKmiWKj5Bk3kOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین نقشهٔ نفتکش‌های تنبیه‌ شده توسط ایران در تنگهٔ هرمز
🔹
جدیدترین نقشهٔ مؤسسهٔ واشنگتن که نفتکش‌های هدف‌ قرار گرفته توسط ایران در یک‌ ماه گذشته را نشان می‌دهد، حداقل اصابت به ۲۰ نفتکش در مسیر غیرقانونی تنگهٔ هرمز را ثبت کرده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/695040" target="_blank">📅 09:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695039">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
روزنامه یدیعوت آحارانوت: مسئولان پرونده حادثه فلای دبی تاکنون وجود ارتباط ظاهری بین کمک خلبان این پرواز و ایران را بعید دانسته‌اند
🔹
امارات نیز با ارسال پیام‌هایی خطاب به رژیم صهیونسیتی خشم خود را نسبت به پیش داوری‌ها قبل از تکمیل تحقیقات و مطرح کردن ادعای…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/695039" target="_blank">📅 09:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695037">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1aff289f.mp4?token=dTgskhI9qNq2D2TarDAWzzThb5euY017pXdZs2OplN9bd_Xr7uAHggKhT-DK1R-WBDRANPFHUO5rFgJAnoRFdw_nslbFEZhxhxRYZOO5IF4Ca-z0DGSjOfxVtW9gKsiWnQBbjVH3b_RClhNkCXyh2pcofhcBjtpqhUjm0oKu7mbjhcy36iDRTEmo9WAYh0Pef9lwdzLgPia6g81Hl1UDgN3ke-5fblf3uOA14BsEF190ur-lURJ6dV0XYoz72UergOcFWzncotr6xMAa5BoW8XIQJxWAIVMTNNRAlwTA8jjYO9M96mxf7d7iop6TQKH7ORN2d36EfC9Py_lFeFDFvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1aff289f.mp4?token=dTgskhI9qNq2D2TarDAWzzThb5euY017pXdZs2OplN9bd_Xr7uAHggKhT-DK1R-WBDRANPFHUO5rFgJAnoRFdw_nslbFEZhxhxRYZOO5IF4Ca-z0DGSjOfxVtW9gKsiWnQBbjVH3b_RClhNkCXyh2pcofhcBjtpqhUjm0oKu7mbjhcy36iDRTEmo9WAYh0Pef9lwdzLgPia6g81Hl1UDgN3ke-5fblf3uOA14BsEF190ur-lURJ6dV0XYoz72UergOcFWzncotr6xMAa5BoW8XIQJxWAIVMTNNRAlwTA8jjYO9M96mxf7d7iop6TQKH7ORN2d36EfC9Py_lFeFDFvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم تاریخی از سایت پدافندی سام ۲ ارتش مصر در جنگ رمضان سال ۱۹۷۳ میلادی
🔹
در این جنگ هجده تا بیست و یک روزه پدافند زمین پایه ارتش مصر با مجهز شدن به سامانه‌های ثابت سام ۲، سام ۳ و متحرک سام ۶ توانست در روزهای اولیه این نبرد تلفات سنگینی به نیروی هوایی ارتش اسرائیل وارد کند و تا صد و دو فروند جنگنده اسرائیلی توسط پدافند مصر و سوریه سرنگون شدند و طلائی‌ترین دوره پدافند هوایی زمین پایه را رقم زدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/695037" target="_blank">📅 09:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695036">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyD2vwPV7TzabTUZrfSt-oTXeI9G3CKusxNjXKpn0d912XFhJbZXfdOVBAFVryAh8qhsIopzPioC_vdqZ01NNtINHTpJafV1YLWJud5ELEp_ZsBzNAfs6ICrCrsocF9MPM5Mla96Gs2id1lweAcEQuhwamVkpxC81FPsEqPrlkco3JejR4ab-5sK1WkYTDNc39X_kE9ON0ueh4jnMHD5XVK4JJzzm3zCMH8ds-W_dECONyc-SOFpnL4zqJ9tpO4ye7Y9xxbkWkuOpWUaeUG6d4l04i3X8THnWl_KJvxKwS4kQJNwoHaY50SChfYwWwHQbyuHhOJewxfNUuCVkWspUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت دریاچه ارومیه
🔹
در آخرین برآوردها حجم آب دریاچه ارومیه به دو میلیارد و ۵۲۰ میلیون مترمکعب رسیده که در مقایسه با حدود ۱۵ روز پیش ۱۵۰ میلیون مترمکعب و در مقایسه با اواخر بهار، ۱ میلیارد ۷۸۰ میلیون مترمکعب کاهش یافته است.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/695036" target="_blank">📅 09:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695035">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سخنگوی هیئت نظارت بر انتخابات مجلس: انتخابات شوراها در نیمه اول آبان، در یکی از روزهای ۸ یا ۱۵ آبان برگزار می‌شود؛ در مناطقی که امکان برگزاری نباشد، انتخابات انجام نخواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/695035" target="_blank">📅 09:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695034">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تعلیق عملیات در دو فرودگاه بین‌المللی عربستان
🔹
برخی منابع منطقه‌ای از توقف و تعلیق عملیات هوایی در فرودگاه بین‌المللی ملک خالد در ریاض و فرودگاه ملک فهد در دمام در شرق عربستان خبر می‌دهند. برخی منابع عربی نیز از حملات موشکی یمن به مخازن آرامکو خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/695034" target="_blank">📅 09:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695033">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3qpTeIXP8WnjR4JN6Ew1jmkTm_X1jz9tWxmhgJvE2pyEuKxTCKHo1wn6pWLHpzbiGrsvHIubnnexjYf7nVyCqsQLuienNLQAXY-AeGqsLL4SVb6ugqXV4NZ58k0sI-K0OmQ_xgcyhJ0bmxWF0SVOAEuX29WC54gSxNNayOzxXTBqIByFxPvWD-VsGdntNWmXhmxkHFRsFPNam0sX-LFj_LTymfZos5UbYDubOMmEtIWdlZN2JKdGjrJiZpZVExSc3XnOwlXBB-PPV0HRjMM5D3S54IPAnnBQe52KlmQToTe-Y6cw44ib6WaQFL0IBl-m09L5DOsyx98F-85gir4oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مار افعی شاخ‌دار، شن‌زارهای خوزستان
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/695033" target="_blank">📅 09:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695032">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im642EqXuCu83NC1UrFUyLDCSHVq2fx2ehUfun4oNuV_kjYGRB3vDnPQ0Sq-bitgP-XUoG6_j4u1-BicPUlO9GldHuBs5hXgIttYcjGixsxy4BH0tY5dyaTaOJB2a-P1UcYhZA1obtHpa10zI--bCJJE3bvnNSOLjKGF7ISrCdBv8Sb4Z1Ukufds28oz7XM2SLdsX35Uvaf9yX8e0etz6Z0WfUla_8WlV1mulrLuGHHRvUJkGewoG3V57hGn6DXkcUlAa2VhvRdnOb2QXGLsw91VkZAvbmK1Kz7Di2gTimLl4HRrcnPp0AQ2Q1C9uewHohAK3grYgQlm1_ndzJTDVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕯
یک گوشه دنج، با نور و حال‌وهوای ایرانی...
شمعدان دیواری با طراحی خاص و نور گرم، برای اینکه فضای خونه‌تون رو متفاوت‌تر و دلنشین‌تر کنید.
✨
💛
مناسب برای:
• دکور منزل
• اتاق و محل کار
• هدیه‌ای خاص و متفاوت
💸
قیمت اصلی:
۲,۲۸۸,۵۰۰ تومان
🔥
قیمت ویژه: ۱,۹۹۰,۰۰۰ تومان
🏷
۱۳٪ تخفیف
برای ثبت سفارش:
📩
@gharar_order
🛍
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com
قرار؛ تجلی هنر و ارادت
🤍</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/695032" target="_blank">📅 09:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695031">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2HSmhldztufamoMX-RqC3qvsOUUYJ1uFnbLHGXl6TcMdrEfErwd53BUJR2tEEkyoeRGvMm3t9XDY5hy03K_aLY0jTQPyMzhS4K7j9Lz8hj3BnH1_l62bRlqm-D2XHWugJnv5js0ae4TfPWVNixFHiW5J4oUBiUtMa1oqGkBCvqy0cph3D8FR1Q7gkuvb0LNQxtmDCnXfZC-swLTKMlB2AGcaK0pHgnO69Tg1u5o7ktka0Yijwlfe7fbAqQFpqW6ELXIHN_Ay_mfka_-ga1hU5l2_Yg2mOCLkYHSBYHA4DQMrkSa0EBHNzSINlzpGBvbTZAXKxnZTNUJEqFIUBG_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در امارات بنزین گران شده و مردم برای یک باک ارزان‌تر صف کشیدن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/695031" target="_blank">📅 09:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695030">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه سیزدهم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/695030" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه سیزدهم؛ فرصت وصال
🔹
انسان‌هایی که در سخت‌ترین شرایط، با خودسازی و زیستن در نام‌های خداوند، بر سر ایمان و باور حق، استوار و پایدار می‌مانند، مجاهدین درگاه الهی هستند.
🔹
در شرایط امروز، همگی باید به دور از جبهه‌گیری‌های سیاسی، برای حافظان و مرزداران صادق و گمنام این سرزمین دعا کنند تا ان‌شاءالله در قوت ایمان و رشادت خود ثابت‌قدم بمانند.
🔹
قوت ایمان و یقین افراد مومن، چنان هیبتی در دل دشمنان و خیانتکاران ایجاد می‌کند که دست آن‌ها را برای همیشه از سرزمین‌ها قطع می‌نماید.
🔹
نور مبارک «الواجد» پروردگار، مغناطیس دریافت‌کننده‌ تمام نیت‌ها، اندیشه‌ها، باورها و اعمال است.
🔹
در نور نام «الماجد» پروردگار، انسان بزرگوارانه می‌بخشد و از خطای دیگران چشم‌پوشی می‌کند.
🔹
انسان سالک، در نور نام مبارک «الواجد» از فرصت خوب‌بودن بهره‌مند شده و در نور نام مبارک «الماجد»به بزرگ‌منشی و جوانمردی دست می‌یابد.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/695030" target="_blank">📅 09:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695029">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYPR-fx-9Jmj4W0iYVNjAtqOeBPKOnuCeoZjFWp0ktVU0ZXx2WCAj5R_7mjR-3LQbTPmkxe5uY1zKZJsODR_XYBCZTfKbgTQlhwWxhP9Aq_tvDHjvOmclVqmHYz5OAf85igiwdUZZHFJOF9LinskpZNXG6aR4edKmULJH-Vz_BJXGFhozxz7_ERUCQydUAwNXObw0d319utx3jCOJTpB7-hYGrZ5RX54zE3bocDXpzuSyWxGrgAraSmDkYbMPxmYrKAPOTpGMZiDfcSooxBs2FkR6Ok6HB2z5osyoW51TWnzovDD3PHmWuInMH9XohL3Jgff5YrnUGbl_Yvb_28h-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو ورزشکار ایرانی با رأی دادگاه عالی کره از اتهامات وارده تبرئه شدند و به تهران بازگشتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/695029" target="_blank">📅 08:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695028">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbf960028.mp4?token=GhjlklUm28wJIstHTmKr0XkBRBvzvmmTFwFpFoHVpxjsGJMBhAeJ7hm8zJkkgPf-Mg1oTLDGXBFYHoftMmBJkcR6OXiZ20Tpj3qdpGEbD2tdiab2n9wXWx6jhQHcj6QIicP_wj2lW5BJIw-BhT-b0taOx18bCNZqqL35djd9Laa6VMiXizW8q-8anHLP0ZYhh-g9pFQSP3mDOL6G1Al3IO_R-k6gP5gsuUERlgL14rCOHNmmkdp03A--sUzztybK1sUYr0Yys88Iopvfx7pf8EI1TfzA2f5h6Y0ApN6OMs0ppNM0pXo3lLPdLRU_CPx0_4HVhkVLR279EwoO3A4EKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbf960028.mp4?token=GhjlklUm28wJIstHTmKr0XkBRBvzvmmTFwFpFoHVpxjsGJMBhAeJ7hm8zJkkgPf-Mg1oTLDGXBFYHoftMmBJkcR6OXiZ20Tpj3qdpGEbD2tdiab2n9wXWx6jhQHcj6QIicP_wj2lW5BJIw-BhT-b0taOx18bCNZqqL35djd9Laa6VMiXizW8q-8anHLP0ZYhh-g9pFQSP3mDOL6G1Al3IO_R-k6gP5gsuUERlgL14rCOHNmmkdp03A--sUzztybK1sUYr0Yys88Iopvfx7pf8EI1TfzA2f5h6Y0ApN6OMs0ppNM0pXo3lLPdLRU_CPx0_4HVhkVLR279EwoO3A4EKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت دید چشم سالم و چشم افراد نزدیک‌بین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695028" target="_blank">📅 08:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695027">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZgEjRZS_Mm1UKpdlqTQzP_mgYp-_B23uMu6Z81DQkzXBmsHyRSPbM0Sh9McLYfc7gFEnGmXAJ9KgOg1f-dlyXpyyShofwZdd2hW9xYOTUhKBRvhO82k8jTFlHaTwGl8-quPv5oEf98kWowR4kxpl4pHXWe1oVBIVczkWhc_-skqRB7qz3TFEuFyvqbMlSR27l-KY6RWfZknwfs_-H8groA2ekXfGowuDv4eLR5WU0mXxNYCDgzeg3pzl0a1uzVXkROi_WAM92f8MjvvdCpLtPGXz5l4KuYwKRzyRMmIyC0DeETw2Niuiwxa72DC9MKYTOHiVztdcr8s_w5f8w2bcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیاوش جمشیدی، از اوباش مسلح شهرکرد اعدام شد
🔹
کلاهبرداری، تهدید، سرقت، حمل و نگهداری سلاح جنگی، مشارکت در آدم‌ربایی، قدرت‌نمایی، واردکردن صدمه بدنی عمدی، تهدید با سلاح گرم و شلیک با سلاح کمری مقابل حوزه علمیه شهرکرد، از جمله سوابق متعدد سیاوش جمشیدی بود.
🔹
جمشیدی همچنین در جریان دی پارسال فعال بود و با سلاح جنگی به‌ سمت مأموران پلیس شلیک کرده بود.
#اخبار_چهارمحال_و_بختیاری
در فضای مجازی
👇
@akhbarchaharmahalvabakhtiari</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/695027" target="_blank">📅 08:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695024">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
۷ حرکت که چند برابر پیاده روی کالری سوزی بیشتری دارن! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/695024" target="_blank">📅 08:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c46b365f0.mp4?token=MJ-4FNB2oFFgl8MUpX4On-0_-FEWUWQ09sD-LVNhU0m0Vp0W-8Sx-5A8ShUGE4T_5BerJid79igZ7mUrA6IOWZk-cSFnVNKyYDASRbwpasjgcTBIEMfOx8ZaO0GUJQ4H-O_0hJOfjzb-54SJDJrze_PkHZWxZ5Wz01RKp4Xatg1Xmhsfx_cgZ42h4I1O24tj8YzhpsTMun7RGePgp_5AvGAZf6bEhIdEfMc50h8ACuUWZmvaFYfyMRjvOtkjldBXbZMMAQ4-kO06F-bzLOIiF6Kr0JsXChaMOXymuPWY2REKllUKOjentjb-EnQQ1do6k3Zu37sV0Wczr3uDqLkP-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c46b365f0.mp4?token=MJ-4FNB2oFFgl8MUpX4On-0_-FEWUWQ09sD-LVNhU0m0Vp0W-8Sx-5A8ShUGE4T_5BerJid79igZ7mUrA6IOWZk-cSFnVNKyYDASRbwpasjgcTBIEMfOx8ZaO0GUJQ4H-O_0hJOfjzb-54SJDJrze_PkHZWxZ5Wz01RKp4Xatg1Xmhsfx_cgZ42h4I1O24tj8YzhpsTMun7RGePgp_5AvGAZf6bEhIdEfMc50h8ACuUWZmvaFYfyMRjvOtkjldBXbZMMAQ4-kO06F-bzLOIiF6Kr0JsXChaMOXymuPWY2REKllUKOjentjb-EnQQ1do6k3Zu37sV0Wczr3uDqLkP-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های بالستیک یمن برای دومین روز متوالی، ریاض، را هدف قرار دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/695020" target="_blank">📅 08:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695018">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
آکسیوس به نقل از مقامات آمریکایی: جی‌دی ونس نشستی با حضور مقامات ارشد دولت آمریکا برای بررسی پرونده‌های ایران و یمن برگزار کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/695018" target="_blank">📅 08:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695017">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
گزارش استیضاح وزیر کار به هیئت‌رئیسه مجلس رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/695017" target="_blank">📅 08:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
المیادین: بامداد امروز ۴ نوبت پرواز و گشت‌زنی هوایی متعلق به هواگردهای آمریکایی در حریم هوایی عراق رصد شده است/
تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/695016" target="_blank">📅 08:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695015">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ترامپ جنایتکار:اروپا همین حالا موافقت کرده است که مقدار عظیمی از ذخایر انباشته گازوئیل خود را آزاد کند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/695015" target="_blank">📅 08:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvl_Dd7znRKnxvkpz0qLVURUnylk_SRHpVx19cJf5WLbwestNGdznikNzXSnCNZwgrxPQnT-PHsLwws-KB5dNizWxIMKqlXQTjlz2UIgSdPTZGZRdmwaLvhEGv8qrqB-3mm7OP9xidjcONtgpga0_zlMbG0Mq6_f-bpJcB3vk69g0RpgxgPdrZIw6TeBqlJjosliY6P1f6e8oHv4BfFv9iJpWzAYP1GRqJdhOY_KEeck9jGISYfSkhMVOdzs3pkCaifP8Qan7F0DNg7rWQLEsonRmX1sbx-PYeK5x8_FsmfMWKvgdGftq78gGz3TD5rb0XgLRxbKlioQT7H6U6Je_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به یک نفتکش در نزدیکی دریای عمان
🔹
سازمان تجارت دریایی انگلیس از وقوع یک حادثهٔ امنیتی برای یک نفتکش در ۴ مایلی شرق سواحل عمان خبر داد. گفته می‌شود این نفتکش از سمت چپ بدنه مورد اصابت پرتابهٔ ناشناس قرار گرفته است.
🔹
بر اساس گزارش اولیه، تمام خدمه در سلامت هستند و این حادثه هیچ پیامد زیست‌محیطی نداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/695014" target="_blank">📅 08:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
وزیران دفاع ترکیه، آذربایجان و گرجستان برای بستن یک پیمان نامه دفاعی با نام قفقاز درحال برگزاری جلسات فشرده هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/695013" target="_blank">📅 08:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSpOde0o05zekBN4bYbDu7ZPKxWdw-GXKNmzTnwWYlrVF8r-3ITv8HKdrAmtGxLZ6-AtRV57BHg9mDHilT-pJPOXoUbhYAKpPsLOVTMsekRrMArvL6wWT_vRte-2SeUooFXutLhfraRDBZcXf_-7Mo27-lmoM8S0f9vBc-222WP2SdoifHpDy-XvVt6keUJ_iRId93zFh_TD-ixoQexP-m0QdR0LjuUaDXTdFbOAXi83IJcaC5ip1dHE54Ls3ZSvDOxq0C4H-ter-SGO2XVvRVWmpOVHxvAaD66SktpHXT2QIEVasqhX_s2B84Mz7j9h53JwlHQsQukjzG5M4MiLoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۱ مهر ماه
۲۱ ربیع‌الثانی ‌۱۴۴۸
۳ اکتبر ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/695012" target="_blank">📅 08:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔥
هوا دیگه کم کم داره سرد میشه، هیترتو بخر!
هنوز هوا سرد نشده و قیمت‌ها بالا نرفته؛ الان بهترین زمان خرید هیتر ریموت‌دار
HANDY HEATER
👌
✅
توان ۸۰۰ وات با گرمایش فوری
✅
ریموت و تنظیم دما ۱۵ تا ۳۲ درجه
✅
تایمر، نمایشگر دیجیتال و خاموشی خودکار
🔴
قیمت 1,990,000 تومان
🔥
🔥
تو 4 قسط 560 تومنی میتونی پرداخت کنی
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/35574/180124/
مشاهده حراج آخر فصل
https://l.memarket.me/lp/15/180124</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/695011" target="_blank">📅 00:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695007">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BN7cz-BBsGJxBbcG4lYV1_N1A5tSlh2A0pJN1ZByF2WQYIyEl42zB7Cpy8DaE13k0djVTN4u_LAkgSCG8bRptsMYIwpqQU1oDCMIw1cAGo3fjiT_dtiv4SPQ0WrZapMQQ1sO6PLvbxSinLDLPKci2c4eMnfy9L0-W8n2PwsUBN9tyfEvWRPBytxzoLH4T6hzVp-k07sCa-yku7LCZ1HVQ-LD4A6jX0JGL1chTkY4yooRrBWqpbDuCeYOzU4YpazKVMuI4kbSr04XwkovlN0qUXVywKSwg0kZlQXiuyUDD_MnRdHJkVTVmQsGabz3G5ktQXzUWu72flmlb6a9pScjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJATFHDWYv4Vu6OKifEUTbtItcvCalaZypQ0W425AJmFWknQ__BRkKtvntN5CunPqGU4sT5Slo_vuUoNeUdXZT6c4qzAmFk2iedFWBCiRZ_iEa4_pd-2bDzMOgThlpiO5dNfmf93aEHneSSH29YUf1X73GuZqGXQdvfV3qmigq5oPan6NgBP87mEK2ky8TttXTQD5zV0OhMmR7jU-s_QbcQI_Vk2igNBXJoHbzMl8dMI8PE_SXeAPb7Pi_j7AiEG6LwoC0jgNskK4KA1IREfyMVkIFjop8pFthKZ3unU1nsinuG_dy4juOIq4YkNL9YxBJSw84MFP8hbRfSaDdEoVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SqPfpLdY1ZlAnO5Rts1J7HWy9ymxo39Ur8ytA2wL1ecnrVAym7p3tuVua6QM-sJF9iQVDt6-rcJ-8w-pNPKjUAV8uWcec4ooccBuGQ1XYxo4y8LQIbaerwpYX8JLWeUx8S-74kJblmrytkgQlgX5gjKyDuguFenLnxTf0n9RpB5vGROjFxGDcbp7B1LJvdNt9kGZO9AVDl2U--maqh5G6QpMOTSlV8aJ3XY5AlNH0cNt6AuD4p2ppZLScuTk-CRkTSsH1MLJoLZW-7HhNGM98pA2cHDTOiFkgpa8wNZzY5NtLcJbdbrJuCYn7elnakpb_FF0HkO7lggzWbS-xmWQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQyxCPDskCTqtNDk8rieK0hG3QXF9oNqPn6mi1xatLetlSxE9y-iviXelSqqEqa9lTnL7n5agRjGtxMH1mQCKh5A6o9l3qj9j6LUuOgTc28DWtXorj5z3AzZWDCwYwBYK3ngVmE3ecxvNoQb3E8-iJZDfRkfnCHc80cmK9OKg8jMd2WHu90n1rB7bdvJiL7qqTuvrtSg8ynayT6FEdsqYYfiOa_7BAseEoMycDep92EXuXkSyLh-8KbGvmil3EyJ3Uj15Cmefigfe_0A_KvSM6xSS0vpc3zqcwn4NwSyuM1yhev2Y2Bm67cS6TZJsJOPn7fr1B44n-4iCmFpdo5h8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۴
مدل لقمه خوشمزه و سریع برای مدرسه، محل کار یا یک میان‌وعده متفاوت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/695007" target="_blank">📅 00:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695006">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
واکنش ترامپ جنایتکار به احتمال استیضاح شدنش: من هم می‌توانستم این کار را با بایدن خواب‌آلو انجام دهم!
ترامپ:
🔹
این یک استیضاح ساختگی است. ما می‌توانستیم همین کار را با «جو خواب‌آلود» انجام دهیم.
🔹
من می‌توانستم همین کار را با هیلاری کلینتون انجام دهم. اگر می‌خواستم، این فرصت را داشتم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/695006" target="_blank">📅 00:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694999">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dx3z6AdKp4u06MG5Sv4yRgC1t3kKyDcBUL-E0DhPhsT8aNgAk1Lgr8ZBdZzEBQcutwUpWxB-aLG---4JlBoqsy98qflNj6vQqlV9LUcPQDvSTXjUqpoZULIt46zIowoXvhswvLO9gB6xnpHPdMPBOz1UEzjM-CifVdQhrHYHHocDIbKxUBBG59Km2-Z3jOxVEoU2pBKU7NlxSodXZTIqacSK48uj5Zi-JuUhTouhiiWXY0PZwCyQfY4bh-tZzqFranpNytksNs1tq-DikSUpKo9NCzOuo7dFUAdraPUY9he8r_Rdp9gnU8Wb5TPeL6Of6Lh24oxGhE1W6ThBdWSZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksVHYUvogczuRgc80OQQE9U36fisc4SIECWwHHDLIbLC3FWSKPhgvx2lY4JwAEKoAdCK1K5tYpLo8OIShq6g104in67h1h1P_xmx3OxD9BcnGJ8p1NMPnQRDFZpGsCtrMSCAFIBDNMTpjkFnFzxxPhL9kLxwef3WH0Vb8qjusqjfntfNSo0E4z_RfoIQlEI19V9qo1vRELbwBbU7laFKBLAS0GwUNETC--n8iuOwqsiDJsZushNRRdMzzNovQaExayudTw030Q3_bTKuZ5eEgEWaRM_tutMiBIJTbBe-F1K6q6MpwxuEYxjwM7N4H34D3znwnGuz7-H3cQXNDN8guw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJjBNGrw-BasIWBHB6bSkH9K5wGdG_djFnA-Q5WaIShx1Ol5uL2sGI04aQhIg3yIjlsXXhvXsQcZx0ZkeHHKw6K89H6jS6Z0eXpbz7N7nLYZoaVZKXVhU4lNWjUj9T39p6cNCX-MfBrCPjCsV3FXB2ZD5NGS7_3XcOL2SUWlKzGZCw9WRtwk9k61iGIJjzdw4eLpEk9Hmeq_PgGdOnYdtns8uJOkcrMNd8cl6CQvgWL5b2r9F0rwaMllsRShEIBykViu-llS-eSqf4-NO-LYNMfzprjmJAad35wl6NYMwSe01WPIf059lgjyDjr2vdBK1WJ9xxzVoEDCsfHSqhXAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2n4xo9NDLAxgnttF2hADRferTiq-GOfhGNyytskDGWi3dyiTyHZYi13JAinEtJqwsayPI1SQfAOxJ-ecOI0ZFh_VJKL-W-I-KjpJQt512QH5w3HS_kC_Yvz7KlecNugGID1pY8VHgQ1aHBRpYIAxIsW3pBo_d3tg-Xi0ORkaUE5FWNf1ip7XwJeRonig6NUNRTc8snnWRnFYWRlkg_eMep34enYQIrK8xAfrIIBdhZbyvWjmZl3Xm5s_xhc4AIQvNOflpXSYsd1Mm42nW0TkJI2EHaFtEErLdxAp7g1oS7QkP4wgR-2Y7hahtd_HvPj-FNOGUDZEcf1XE-r08hzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqDot-Y4gw3Z5VcuWe-ATbh-7fhoWRrCpsF4tkkjCK6gWExQfjN9V1fYf_S2oyX3jHnLr8nOuKjX7rFW_I7RSKd_LMJiUPW25dJr_-LZmu0CNcC4ETC7YdDA5nBM7zb_iNqKLJlx-b6yFLt0B20O_h-6MfDtJOmrTaR4GXHmeu9fy7Z58n6NkKlHDW1rL0rAVu2Crw4oYw7SqP3eiNoY0FYIzdLXeZFG756yLugCpBTDP_-JAqqE31B2HE20UpqC8DWNecCdJxHPm9qespdO01VdJyCsTNhOdoTBRE4Ma9L_-z45XWSCfD2i4EBZD5kQ_u3TLw31ivNDul4jxXSfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oy3Fv9DAHGiCFtiPKLa0nSb-6eRpdmkl4C2L-SGT19R_sg1IoXjL_4qlIHPuI4knj5c3dgsxuYLBDUFhROjo9G7obKqvXoPM0wX1qLW3b6I4-3eJCUMdvmtTwzQU1FqbFfbtN--xeToDlCcB2YfSH2i7vEWueI7y8T8PLZmbLrpOkxE8XVH_7iBGQfTTqY3i083gJAD1Joe76GVfgLIghp50ixJ9_lr0U1RoCnE0EcbysZXJUPVbAN8W0SZ1pZJHes_Y8XaUd0f2jWhp8rWADPK4oVj3rx1kzx7Mrbrbvgp5-wjDaxppzh878veTX8E5fXUF0ntApfrlKroW9SsWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPvyNjbYJNRT-OTbnz6uBO127r3oaJn5F7wqSDZjV1IG_GNJiOFipJysnMaQMTfRQVVbEbP3uxd9aGeBmObc1rQu8vd6rBKFnyNy-gZq0o7hNaUy0XUh4DnfiyGdz0ZhImLVp_LLDa_atVbkmEYvb3Ut_ltFmEuj9so0jpd9cpIuYmYndgiKem1JQpcHOx1YG-9fGtLbeaRQIRJJ_8E9D9awE-B9_jDWLGNDpPXX_t1wBJVdQbqTWB7S5dL_7q3nV6sArXtNE3k2D_4G5P8Yzs7g0rk0pVXGAzBH55B_BV8lZmIdyiIvo5YKpmzW1ToTPG5DcQk6mUtsAsy5sJ_wNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر جدید از بقایای موشک کروز تاماهاوک بلاک-۴ که از آوار مدرسه‌ی شجره طیبه‌ی میناب بازیابی شده
🔹
روی برخی قطعات در تصویر مانند عمل‌گر هیدرولیکی بالک کنترلی دم موشک، تاریخ تولید اردیبهشت ۱۳۸۹ نگاشته شده است که با بازه‌ زمانی تولید بلاک-۴ موشک کروز تاماهاوک هم‌خوانی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/694999" target="_blank">📅 00:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694998">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC3Z8NHZsbmvDzDAUTIdrJts-zZG-tD5trIui7rBfEXGDQzbthCcN-lUUy7QrSKZgEAAtQUlGMoZ7MRHZCd4wEHEaNT2PPipxOSMjAf9TmrhCoL830VOU6d1fxHOMNwtcOJ9K7vTUs0i4FNENkWmP2abq5PrTqjhsPEenzx-5crqSbwEP8qsoGHNyT8Wwco4xpwhWDAhXgH1Pfjzi3BxKu-Uv01p9RxLeOyUi9ldah9s2u5a0_8EyjthIkg6cWPyM1poImnFKatO1NFmRX8Q1Jg7kqYmCmuJPFTDgbTn-QbNeis_WaCumMwK4yZjeIGKtjppxh-O2ZDyC1MzfICQLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین خوراکی‌ها برای عضله‌سازی موثر
💪
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/694998" target="_blank">📅 00:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694997">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
حاج سعید حدادیان، لبنان: بیش از هفت ماه است که مردم لبنان آواره‌اند و تقریباً بدون امکانات در یک مدرسه زندگی می‌کنند، اما با صلابت ایستاده‌اند/ با همه این سختی‌ها، حال رهبر معظم انقلاب و مردم ایران را از ما می‌پرسیدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/694997" target="_blank">📅 00:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694996">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IG4a2ONofnal2vrHimVsF__MxZ8m47G6jQ7tqBmnrMjzRhquKYhlwCb940lPty6XrkEHO35tOd8KkqSOsqLgx7UmXqtYsxMv3YvOV71yKDIi84VOwq91xXd4UG8mV1pr3wsirsRCTSgncLb4Z-7izkfvciVrZmdRW3_tQ4H52di-PfN4RLU1jT1YrdHs6J6c8reVmGTnOjECdnCmb7o1-nzpBm1cxl9KLUEdvE4VZDQw1ZpEd8EzSG5HU1aR9AHeVAu1fzXtEXA7RwHe0txw0kT8lkTRxCG2am7--x7wJGufORwl1oNQQjOO692DiIjdenBmH9YKJjV_Ugd65moaxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/694996" target="_blank">📅 00:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694995">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58dabdb74.mp4?token=oCvWHF0ejdSZpby3wMQahZxFpZ67yqzaKcz7WvpyxunuESLvb4lZkoDhhU7FGgPtPjap_wcdBebXtXZQMubE5MYQ-H2Jhz_ts5GcpIER7YVxHzUcL1y67uUPbKH1pDK6sJ0KAzi6b1jGXH80aqek-GV2iG_i7OlET0r236giqaqh3hl_ZyqAbtdSeDNrCSuuLfUIt72j--SukfVP02xf_zvN02WljigmeDPF6B7IuvuuyrK2g5l0EONvuJ_om2jKcb5s01SCQpndkodBlCw7AC8E-xeK8OsQZ2RbPF_V3jZZRovQfQ7csYcb1xZztZyQLErZLvrEg70GJBidLzwrnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58dabdb74.mp4?token=oCvWHF0ejdSZpby3wMQahZxFpZ67yqzaKcz7WvpyxunuESLvb4lZkoDhhU7FGgPtPjap_wcdBebXtXZQMubE5MYQ-H2Jhz_ts5GcpIER7YVxHzUcL1y67uUPbKH1pDK6sJ0KAzi6b1jGXH80aqek-GV2iG_i7OlET0r236giqaqh3hl_ZyqAbtdSeDNrCSuuLfUIt72j--SukfVP02xf_zvN02WljigmeDPF6B7IuvuuyrK2g5l0EONvuJ_om2jKcb5s01SCQpndkodBlCw7AC8E-xeK8OsQZ2RbPF_V3jZZRovQfQ7csYcb1xZztZyQLErZLvrEg70GJBidLzwrnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ دلیل آسیب دیدن افراد در حفظ حریم و حقوقشون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/694995" target="_blank">📅 23:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694994">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: پلیس بریتانیا دو ایرانی را به برنامه‌ریزی برای انجام یک اقدام علیه جامعه یهودیان در منچستر متهم کرد
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/694994" target="_blank">📅 23:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694993">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
وزیر رفاه: معوقات افزایش حقوق فروردین‌ماه بازنشستگان در شهریور ماه پرداخت شد/ معوقات اردیبهشت‌ ماه نیز برای گروهی در مهر و آبان انجام خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/694993" target="_blank">📅 23:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694992">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/361e266983.mp4?token=viXcVfXwIDSdTZ80FAJNH6ugEsSEIw7Z9Ac3aiXyHb-AP5rcptRxjosrG7L-kbcqEKWOXF4uDe5GiHudRIaKDRPACHeUuOBFIPCX53AEu3MG0JBmTlNrm-g335L6T_NQWyTkM1aJUYZz55gmoRb3CNuyp1G21G54VhIZc8lZPSx0TTOQhGFXFGNyaFbcbmW3mExHu6QNF4SQTHQrlUzze1rj0-IFgc5qSQdfPmgwwbXW6QNAqk4S-__-gUjy5EjBQjMJEL0DZW5lSHgGrIvr2di0EthKKfJhIAXjVP2aZaA7bsMkkhl94tMyKS-hF1X8fRo2Qj7M2v1VgPS15SKVWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/361e266983.mp4?token=viXcVfXwIDSdTZ80FAJNH6ugEsSEIw7Z9Ac3aiXyHb-AP5rcptRxjosrG7L-kbcqEKWOXF4uDe5GiHudRIaKDRPACHeUuOBFIPCX53AEu3MG0JBmTlNrm-g335L6T_NQWyTkM1aJUYZz55gmoRb3CNuyp1G21G54VhIZc8lZPSx0TTOQhGFXFGNyaFbcbmW3mExHu6QNF4SQTHQrlUzze1rj0-IFgc5qSQdfPmgwwbXW6QNAqk4S-__-gUjy5EjBQjMJEL0DZW5lSHgGrIvr2di0EthKKfJhIAXjVP2aZaA7bsMkkhl94tMyKS-hF1X8fRo2Qj7M2v1VgPS15SKVWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: شاید درست بعد از انتخابات جنگ با ایران تمام شود/ جنگ با ایران به هر نحوی به زودی پایان خواهد یافت شاید درست پس از انتخابات میان‌دوره‌ای
🔹
ادعای تکراری ترامپ: ایران در شرایط سختی قرار دارد/ به محض پایان جنگ با ایران، قیمت نفت به سطح قبل از جنگ…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/694992" target="_blank">📅 23:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694991">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
حاج سعید حدادیان، لبنان: انگشترهای اهدایی رهبر معظم انقلاب برای خانواده‌های شهدای لبنان مثل «خاتم سلیمان» ارزشمند بود/ وقتی می‌دیدند رهبر جبهه حق این‌گونه به یادشان است، احساس افتخار و عزت بیشتری می‌کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/694991" target="_blank">📅 23:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694990">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6212815d00.mp4?token=Q201ICBCQyN8SbxRoD4XQmmet8dvzC4kJ40Qh4eezps3ytfBEbgrOYOJijqx2YHbqTX7b3rFq4hyrk7qAKHWlNkaZD6VmmTRJD22Zxsf8THGCwD50XvlGSHhOZWY1ZKbAnBZCuruYpXr3sHO8W_7VPw9C46XRiFh4MY3iOWPXk5Wu8WxcgbuhNbQQfDL9I8M79O9zEhAhKHRhhBzoKOLH8Kc2_9Y-ezx1tcVFopLmYnGocCjIJy9JM9YAyBEua8HqaVWvUwK-Gpuxs8E0Y8-6DKaSt0RE-17uwOgZmUV9URywi_r3pSYZzb4WdJoQDuFQgbaDVlWoSH5_FoWE5a75g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6212815d00.mp4?token=Q201ICBCQyN8SbxRoD4XQmmet8dvzC4kJ40Qh4eezps3ytfBEbgrOYOJijqx2YHbqTX7b3rFq4hyrk7qAKHWlNkaZD6VmmTRJD22Zxsf8THGCwD50XvlGSHhOZWY1ZKbAnBZCuruYpXr3sHO8W_7VPw9C46XRiFh4MY3iOWPXk5Wu8WxcgbuhNbQQfDL9I8M79O9zEhAhKHRhhBzoKOLH8Kc2_9Y-ezx1tcVFopLmYnGocCjIJy9JM9YAyBEua8HqaVWvUwK-Gpuxs8E0Y8-6DKaSt0RE-17uwOgZmUV9URywi_r3pSYZzb4WdJoQDuFQgbaDVlWoSH5_FoWE5a75g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند خاصیت طلایی زردچوبه برای بدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/694990" target="_blank">📅 23:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694989">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای ترامپ: شاید درست بعد از انتخابات جنگ با ایران تمام شود
/
جنگ با ایران به هر نحوی به زودی پایان خواهد یافت شاید درست پس از انتخابات میان‌دوره‌ای
🔹
ادعای تکراری ترامپ: ایران در شرایط سختی قرار دارد/ به محض پایان جنگ با ایران، قیمت نفت به سطح قبل از جنگ و احتمالاً حتی کمتر از آن خواهد رسید
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/694989" target="_blank">📅 23:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694983">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RsunKbRPfbJUvgzNumNFkvwo_itEwT--EPzkMBSDQ89JhhMhoC1MSDpqbIjKgwlPjQRwntkoFe0Npog0BSiN3oudE7L1lK2kOpTBNFylJaEi18vn4uCwI2a60xRAiKxgx92XV4zXXeqgjlx8ul8XXxcl3dxjEJS9rDaEqgqevJeFcoGBtQsQJrJzgfxgmXczoP0AXnKGwbsLAizCQH8wQSPGBZaCpIP8wVssxjpHvyYGWqfYlHjA6slkoJeh0_54uHKr1YrOf2DfXZyzsuLnlnBTl18c_rySRt8vgITU2z2FMzURpI_8Co1jIVUmfuRSQ7Dk0OJxGxqgzRdmtDwRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdqXsEA-wG8Nw5PHcEj10n4r2kbJVc40QsO-f4Vs6BWY1LoFOV7CMq8uLdicyS6mwM3T7iSbFTpvmNkp0_bUfOyzHyb3igpgZ7hyDl0_WP0i--sJqe6j4p6ZmVHn-zSAj8StO14pmcvs4qVcop1TCxJg-Ur5VqzpOJX-7pH5rZcqqqdjKe55dozXsAQBVTbyCz9uxfiHEUjiHbxyj98vcf3TXXXghon-ABJxtrOqO_QVVbUuSy9ajrik39q_4Dk1hSbVnz5w85jR8urLwehoALHQLdhRZYdM7NI1kAUf9TYvmbqNODm7QJ3XCrEYBNuaObSy_5JXjGqLWNql4sr4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrIxBcwhMMtZ_YpUUlzdEKNYYqifs9L6uVHL-oGqd9c4FJKTIPfpVK7oDynU5nc-xnuzihDOMcy0-W5qHhsytC-iTNJB5Jb3Zz9Ju9H7r-nHcI66XJMjoEuF7O4uUj8w7o85HC3mOlBm4bfOyfxms6sDbKwhoEj2-0IbnxLoJh4BpaQPfleZGSQQGkuuqZF2it5DMGuciL7norrbAQCCASOsHjxsJ1PzPgQzmss7HHOxdJelnzwnfDxZlp_fMthgrwhxuJwVTo1IbxXwMljgPSn6VSB-VP0EWrFtDrEqvPo49jfPU48RDJaZapv8YdxdqkIg91O1XujnH2p7YD9qwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMxv6JhPA_Kno8Y_vsBMTtD0jW7Nl2kf32YoJBOFwTGisCY1jiucjKFl5B_1yGD4mPmNp3NyhdZJbf-4tWt5TN0U-PfdRmI9Op7KF_7MdSypbWWX7di9Z4-Cuv8yE2b9E8JMme_1vxNZRQfwtJF3fOAOtiiA22IQ28oQPbUYvyF5N6MVH2XJXmiHZGd4CS3ydhzM8Prri1b2P4d4YyKeSWuOXwjwC5okr2gVGN1F_DNZXcorevxzsTiaUw9fG3D2nYpSL298IS6kMJKHgIWIEFjYNEiN6cLJAi4Tr7BXDMRaUCSaxwSoezGuu5jX_oKu4S41FJRzk6qCQ04BEcQdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmsTaZIiL5pajHcIxuhIKI5-yKjaRxy_1begmRKfbP9EocDidE9L1uazMjE83tBWxMtRBlqQOkepP51HCfxUVV3bRBxEmAIDbgG1GWkbnUW9OteJFC1g2eX2-KP1lYxqDDy8PdjPaWiFO1cBkjbOIEJV6W04gGZVwztHy8y1-NbiV7is0UxSGu9rX8zECn_3syt-VqnoWnKwzvv_Qltf9FVmi6GxJLS7iN_L_oKSKIbgxBaY9KBCiWqqi5alJoRaVnAPIZ-H3ZKbhvpX0pPg1956tYuikGaP6FC9xy0UAG4wK3euJ7LBAgy2biAjIblw75XIvxt3_lgBsuj-kPF3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGyvJdrWJwNfKOrqi7byaRjiMTWa7uGSmCyfHUXp_7yxBVg97hiWHde9b9cbH8g1jb3R83TuCMilrijNPtOW5OJtJ3fCyl8EmKLBw-yEWVcPK_E_vZqM--Lje6Z4jfCfuJhPxOZ4-Z2djyHTZ072T3F5MICl5hJrNMZsnsqLxS3_8o0azU0DweKZTX7M2Nf4MdMF8Puiee6vuhPQJZBx21Q0V6aL5dD7pLAT2qxzrszE-uJCXOVCqnXSfhycX7iDebVn_BuLJqFSPS7nKOkIskN8-noaMIvIyKZAwdS6yfxwUQZ0R4zz5lOavJGRh4Vak8NmR7TRF7mOzM0vmIxFJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند مرز جالب در دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/694983" target="_blank">📅 23:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694982">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
حاج سعید حدادیان، لبنان: در دو جنگ اخیر تعداد شهدای حزب‌الله لبنان دو برابر شهدای ایران بوده است/ این خانواده‌ها برای مقاومت قربانی داده‌اند و نباید حمایت از آن‌ها فقط به دیدار و سرزدن محدود شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/694982" target="_blank">📅 23:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694981">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6985af1efd.mp4?token=W-GopAul8gUxTymxsQY-USe5vhVOjXxzwA4v_U4LyRb2r3jlF5jsMDl9ZENYTB3fFV9cH7AzUlXRD9y6PZ8fJON2bB8soCNg2sYOzFQst8nGdhB_H07MRqcT0j_tfJTl2IZiy1arkeeoTdLbkTsCWRf7mbyW9YcFv-bKFn41Ln9-nr8N1gXfNccF4ahTOloHvq-03qsS3JnVuRlbdltSqnoj7HgrhM1wVWQL55kSjGKO52q3U_aJ3cLLDIDxSsWb_kVrZjUXoPV0cxRdDhgcoDv5M0-13Hs4bDVsSuSMmFPM4RNSBN9QDjzStvllWcj1Upi0iD33pwFX7fk6E8FBdjOkwq9KhMZ0yynglStAXGEfQPIzGWNhR3mnMl5CxDsqwGAz37jUJKrp5Jen_NcRhJymA2Y3vi1CXDlwuqViqn8oVVht96IeQARM9ZP24penbAWsmoukWvgHM0n7VIvnTleVkAChHAW0Pe6VxOulK1owV4lph5Eu1IeS5Olb8MBJjnx3B6L11GHkK7hLp2lctUVIg2_wXOmwnT_HaB1Hyudz0l4DXvaro3W2HGNS0fUuwhjmgGYAwRoj0Ao_L4t_LyS6VsQ5yfBvDk_TRtZTQy2HTO1qyscFaSLkouf-dMGxJg2zlccUdr0twrp5PzjrtzELdDV22QGbnV5irOQdn6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6985af1efd.mp4?token=W-GopAul8gUxTymxsQY-USe5vhVOjXxzwA4v_U4LyRb2r3jlF5jsMDl9ZENYTB3fFV9cH7AzUlXRD9y6PZ8fJON2bB8soCNg2sYOzFQst8nGdhB_H07MRqcT0j_tfJTl2IZiy1arkeeoTdLbkTsCWRf7mbyW9YcFv-bKFn41Ln9-nr8N1gXfNccF4ahTOloHvq-03qsS3JnVuRlbdltSqnoj7HgrhM1wVWQL55kSjGKO52q3U_aJ3cLLDIDxSsWb_kVrZjUXoPV0cxRdDhgcoDv5M0-13Hs4bDVsSuSMmFPM4RNSBN9QDjzStvllWcj1Upi0iD33pwFX7fk6E8FBdjOkwq9KhMZ0yynglStAXGEfQPIzGWNhR3mnMl5CxDsqwGAz37jUJKrp5Jen_NcRhJymA2Y3vi1CXDlwuqViqn8oVVht96IeQARM9ZP24penbAWsmoukWvgHM0n7VIvnTleVkAChHAW0Pe6VxOulK1owV4lph5Eu1IeS5Olb8MBJjnx3B6L11GHkK7hLp2lctUVIg2_wXOmwnT_HaB1Hyudz0l4DXvaro3W2HGNS0fUuwhjmgGYAwRoj0Ao_L4t_LyS6VsQ5yfBvDk_TRtZTQy2HTO1qyscFaSLkouf-dMGxJg2zlccUdr0twrp5PzjrtzELdDV22QGbnV5irOQdn6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری پربازدید از ساعت هوشمند در دست رئیس سازمان پدافند غیرعامل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/694981" target="_blank">📅 23:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694980">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ایهود باراک: نتانیاهو دنبال به تعویق انداختن انتخابات است
ایهود باراک، نخست‌وزیر پیشین اسرائیل:
🔹
بنیامین نتانیاهو در حال فراهم کردن زمینه برای ورود به جنگی است که برگزاری انتخابات را به تعویق خواهد انداخت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/694980" target="_blank">📅 23:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694979">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
وزیر امور خارجه پاکستان: نباید هیچ‌گونه هزینه‌ای برای عبور از تنگه هرمز دریافت شود
🔹
به‌زودی نشستی در ریاض برای کمیته دفاعی، سیاسی و راهبردی بر اساس توافق مکه برگزار خواهد شد.
🔹
بیش از ۶ کشور خواهان پیوستن به توافق مکه هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/694979" target="_blank">📅 23:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694978">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ژیلا صادقی، لبنان: زنان لبنانی به ما می‌گفتند «دل‌مان به قدرت شما ایرانی‌ها و ایران قرص است»/ این حرف را از خانواده‌ای شنیدم که هشت شهید داده بود، اما از اقتدار و آرامش مردم ایران می‌گفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/694978" target="_blank">📅 23:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694977">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
وزیر رفاه: از این هفته بازگشایی حساب کارفرماها مثل انسداد حساب‌ها از یک سامانه انجام خواهد شد تا مجبور نشوند به چند بانک برای بازگشایی حساب مراجعه کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/694977" target="_blank">📅 23:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0292f00aa1.mp4?token=V-rerDKL7gcewQnvEyExdxtJ31xXRUmeZvv8r9jFHXcWrHNj2hk86GDTEKfSKWeJGUHkaE2rvqc06UR9WIpSLxyPHCxItO0EI8m3W89dFqpnJEm7KvUlmK4VwyjlC9qoo4lAsr4aghtck-PAum55mbbE_UThHwKnE_0uMneZBbB62LRL_xUqvUGFJuFlPBDM0AftOqCYwZhCfN_Pu8iqtWwi3C1j7Rwef0Wk_w9THhp4rZX4V-xRIpv7olBFxh0_ZzdbptLzTjDw0F7DpqQRSwUOcwqir7DOS5O59g773yXumh9qWXN8nQbyB9-UD8774iDnlw-L_2SecrZa_Zo2Gz9deXERUcxU9JXo0WlT0msAGkAkRwlE1Ni3iibP5tQRJOAZF3753tQ11xvhnip2vo7zEFykAJ8nWUQA7zrhqtxuHtOxwvAf1hOWbfq0IjQ1w__gZiT1D5j-SnPfTPlH5t33yHniECiTW68TampGdCNFji_gurHihn50sHIM_E7HtxOvuPrpa7egv1z0CKSzFJlzYBKxxn-uDPvNw6YEBMmRZJSBYpfd13sv496XvAxCeaOh4CL_uRwhlyUrN34W9HsiX1kHv3ZeXWOlGEPKIzFq_pQCANjksDX9bPy8dd7Cgm6JDSbFsLtahZi4-GWnlhBfoejS-QdG4SkAEDhrWrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0292f00aa1.mp4?token=V-rerDKL7gcewQnvEyExdxtJ31xXRUmeZvv8r9jFHXcWrHNj2hk86GDTEKfSKWeJGUHkaE2rvqc06UR9WIpSLxyPHCxItO0EI8m3W89dFqpnJEm7KvUlmK4VwyjlC9qoo4lAsr4aghtck-PAum55mbbE_UThHwKnE_0uMneZBbB62LRL_xUqvUGFJuFlPBDM0AftOqCYwZhCfN_Pu8iqtWwi3C1j7Rwef0Wk_w9THhp4rZX4V-xRIpv7olBFxh0_ZzdbptLzTjDw0F7DpqQRSwUOcwqir7DOS5O59g773yXumh9qWXN8nQbyB9-UD8774iDnlw-L_2SecrZa_Zo2Gz9deXERUcxU9JXo0WlT0msAGkAkRwlE1Ni3iibP5tQRJOAZF3753tQ11xvhnip2vo7zEFykAJ8nWUQA7zrhqtxuHtOxwvAf1hOWbfq0IjQ1w__gZiT1D5j-SnPfTPlH5t33yHniECiTW68TampGdCNFji_gurHihn50sHIM_E7HtxOvuPrpa7egv1z0CKSzFJlzYBKxxn-uDPvNw6YEBMmRZJSBYpfd13sv496XvAxCeaOh4CL_uRwhlyUrN34W9HsiX1kHv3ZeXWOlGEPKIzFq_pQCANjksDX9bPy8dd7Cgm6JDSbFsLtahZi4-GWnlhBfoejS-QdG4SkAEDhrWrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این سگ هر کاری ازش بخوای، انجام میده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/694976" target="_blank">📅 23:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694975">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پاکستان: نشست توافق عربستان، پاکستان و ترکیه برای بررسی تعامل سیاسی با انصارالله برگزار می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/694975" target="_blank">📅 23:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694974">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان در محضر خانواده‌ کم سن‌ترین شهید سال‌های اخیر در لبنان: پدر این شهید خاطره‌ای از پسر شهیدشان نقل می‌کنند که بعد از حادثه پیجرها، این شهید اصرار داشته یک چشم و کلیه خودش را به رزمندگان مجروح اهدا کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/694974" target="_blank">📅 23:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694973">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
هکرها به سامانه پیشرانه ابرنفتکش آمریکایی نفوذ کردند
بلومبرگ:
🔹
اف‌بی‌آی و گارد ساحلی آمریکا در حال بررسی حمله سایبری به یک ابرنفتکش در نزدیکی سواحل تگزاس هستند. این حمله سایبری که تابستان امسال رخ داده، منجر به دسترسی موقت هکرها به سیستم دیجیتال کشتی شده است.
🔹
هنوز مشخص نیست هکرها چه مدت به این سیستم دسترسی داشته‌اند و با استفاده از آن قادر به کنترل چه بخش‌هایی از کشتی بوده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/694973" target="_blank">📅 23:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694972">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 4- میدان چهارم، فتوت</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/694972" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان چهارم، فتوت
🔹
فتوت به معنای جوانمردی و آزادانه زیستن می‌باشد. در این نوع جوانمردی، آزادی و آزادگی در کردار و رفتار مشهود است.
🌱
در مسیر فتوت شور و شوق و ذوق جوانی می‌بایست جاری باشد.
اقسام فتوت:
🔹
فتوت با حق (به توانایی خود در بندگی کوشیدن): از جستن علم ملول نشوید_از یاد وی نیاسایید_به صحبت با نیکان بپیوندید
🔹
فتوت با خلق (به عیبی که از خود دانی میفکن): آنچه از ایشان نداری ظن مزن_آنچه دانی بپوشانی_بدان مؤمنان را شفیع باشی
🔹
فتوت با خود (تسویل نفس خویش و زینت و آرایش وی نپذیرفتن): بازجستن به عیب خویش مشغول باشید و عیب خود را بد دانید_شکر نعمت ستر بر خود بینی_از ترس نیاسایی
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/694972" target="_blank">📅 23:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694971">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
وزیر رفاه: دهک‌بندی خانوارها به شیوه قبلی نیست و براساس سطح درآمد به سه گروه تقسیم‌بندی می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/694971" target="_blank">📅 22:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694969">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/816b2002b3.mp4?token=T4qDOFdy3OcjknBFk-W6Gx4CNrRRFIkCsLZRaSVhWbfRzKLtcVpFIFZYyjPDCEPT3MygaARpw6xjYBGOmS4Rh-Lx1AlTxz_j1J4Zc-LIaHt6wYl4jc30jLyuE65Xy94sVNdFIwHno_JBccsRRYoot17uOevSpi2IZ4P4bmQiMZjDBEQU7t-ngsINxOt-aCuHuUF_2Tn09SqJZWXfswTikxTI69Rme2kjvjVer92oxdOyHx_KZjuNY7jjvWDV_siHVib6xcTuIc8FabjoV-Y31umPXPPW2pFwsuLU8p7mtJpktArWvoQ5Tlt8xSZSMaZmbijmGlib_2xPLExslI05MwrH883Hcm8NlWP9prkMjzk_QwKXLdSfbHEVX_GhRwJO6kdhZ4iuPUPkT_fhti87Oro_nfipSNt4F6R9vBZ6QCQb6k5p_xwqMqfv17xOdWhcwNC4xs-xELLHNejpKQM3Cgn70q6KAgupZd7xfHOpVNm-p3lT9jYUzZaKf0_AyrUMOmAOpQ5HE0NO28n8udfSSdjDIFIgDLGl-jEWR5wjwmavdkD6FN05sSJD8LdpP3iGXvrwQ1cnYNl0ZpZUoW-pc6MsXEyZ3l0zOfXlpqNZsQwAT1kG1LbxN_8k7s6gQ9Fw5L3KXRxgY8hFaD703aK73EghfAR723WqL5GuGS74rrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/816b2002b3.mp4?token=T4qDOFdy3OcjknBFk-W6Gx4CNrRRFIkCsLZRaSVhWbfRzKLtcVpFIFZYyjPDCEPT3MygaARpw6xjYBGOmS4Rh-Lx1AlTxz_j1J4Zc-LIaHt6wYl4jc30jLyuE65Xy94sVNdFIwHno_JBccsRRYoot17uOevSpi2IZ4P4bmQiMZjDBEQU7t-ngsINxOt-aCuHuUF_2Tn09SqJZWXfswTikxTI69Rme2kjvjVer92oxdOyHx_KZjuNY7jjvWDV_siHVib6xcTuIc8FabjoV-Y31umPXPPW2pFwsuLU8p7mtJpktArWvoQ5Tlt8xSZSMaZmbijmGlib_2xPLExslI05MwrH883Hcm8NlWP9prkMjzk_QwKXLdSfbHEVX_GhRwJO6kdhZ4iuPUPkT_fhti87Oro_nfipSNt4F6R9vBZ6QCQb6k5p_xwqMqfv17xOdWhcwNC4xs-xELLHNejpKQM3Cgn70q6KAgupZd7xfHOpVNm-p3lT9jYUzZaKf0_AyrUMOmAOpQ5HE0NO28n8udfSSdjDIFIgDLGl-jEWR5wjwmavdkD6FN05sSJD8LdpP3iGXvrwQ1cnYNl0ZpZUoW-pc6MsXEyZ3l0zOfXlpqNZsQwAT1kG1LbxN_8k7s6gQ9Fw5L3KXRxgY8hFaD703aK73EghfAR723WqL5GuGS74rrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر تعاون، کار و رفاه اجتماعی: تلاش می‌کنیم افزایش کالابرگ اقشار هدف از ۱۵ مهر آغاز شود
🔹
میزان افزایش اعتبار کالابرگ احتمالا ۵۰ درصد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/694969" target="_blank">📅 22:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694968">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU1bceIBzr93Z2beNyZCQRd8L7tBmOOtiafbGlzwWGShjbAEMZyXrFWWusKQgRp1ujhF4td1mX3beMzR_sOakyPlJI_5nyYL37e-6WDJUsGbbJ5-UwLGeF6jI_aK0t1jo7vmNR01inUPREblGhaORpdIagBcM3FDwgSpY8FEeptiVnpuDT_Ilvuco_hRM6oX15aHerYzpiBiIHJpKyhxflpau7oFt16YLe2rzTDo6lMmXhcEUG0yhqJ0MYGWZmL17E1PkYUSBNjDayrM92QCxZLA9EMV2L-tnfndrwBQ-cUYxUE03l137eauTLuPd5L_ahEKRloqGznG6hk37wBDiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درآمد ارتباطات دیگر با هزینه‌های این صنعت همخوانی ندارد
🔹
در ۱۲ سال گذشته، هزینه‌های زندگی و تجهیزات شبکه چند صد برابر شده اما تعرفه اینترنت در مجموع فقط ۷۲ درصد بالا رفته است. این فاصله یعنی اپراتورها برای توسعه و نگهداری شبکه، هر سال با هزینه بیشتری روبه‌رو شده‌اند، بدون اینکه درآمدشان به همان اندازه رشد کند.
🔹
داوود زارعیان، معاون ارتباطات شرکت مخابرات ایران می‌گوید ادامه این وضعیت انگیزه سرمایه‌گذاری در این صنعت را کم کرده است. به گفته او، فقط تبدیل شبکه مسی به فیبر نوری در مخابرات به حدود ۵ میلیارد دلار سرمایه طی پنج سال نیاز دارد.
🔹
به اعتقاد زارعیان، شبکه برای پاسخ به مصرف روزافزون مردم، به سرمایه‌گذاری مداوم نیاز دارد. اگر منابع لازم تامین نشود، توسعه فیبر نوری و حفظ کیفیت شبکه هم سخت‌تر خواهد شد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/694968" target="_blank">📅 22:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694967">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0098664c.mp4?token=efaYjQb6JPFKcXdfwlEsJ_jgeySe3gui8XtXOshzzWoCgTPKAOA0xIdezP9OhRbXp_ueVl6PpO4ONuzxcLzzQ_0xXuVLQJfjiQ2mhntuwp33AK5SJMFm41WxxH-NqXPLIkGqPCS5zAWBifHCYHiGyj5Sx7zGA6Lhl0qQ9qpycKwN1pJJAeDduchaFn7rWJLO6G5g13yqC_5RbqmsUmJtzzKd_NCjJgve7N9u_Xblkc63XHLu4rhF_Ebl3O_9lsd4NqXbwEV-ddS8FPwQucOzQaFB-gcBMvw1FEMhEF_c3kUiXG8baXkIj5UxXF-4wnz5Q64iPhnTGHvKdjCL2NBaRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0098664c.mp4?token=efaYjQb6JPFKcXdfwlEsJ_jgeySe3gui8XtXOshzzWoCgTPKAOA0xIdezP9OhRbXp_ueVl6PpO4ONuzxcLzzQ_0xXuVLQJfjiQ2mhntuwp33AK5SJMFm41WxxH-NqXPLIkGqPCS5zAWBifHCYHiGyj5Sx7zGA6Lhl0qQ9qpycKwN1pJJAeDduchaFn7rWJLO6G5g13yqC_5RbqmsUmJtzzKd_NCjJgve7N9u_Xblkc63XHLu4rhF_Ebl3O_9lsd4NqXbwEV-ddS8FPwQucOzQaFB-gcBMvw1FEMhEF_c3kUiXG8baXkIj5UxXF-4wnz5Q64iPhnTGHvKdjCL2NBaRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری صداوسیما وقتی اسم حسن روحانی را می‌آورد: منظورم حسن روحانی کاراته باز است، باز نیاید بالاسر ما چرا اسم حسن روحانی رو آوردی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/694967" target="_blank">📅 22:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694966">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15e41163a.mp4?token=QiN_k1Jlr6M-sOQebpQu3UJwYFKfVzaTcE1ras33LNHklCd8ZF-u79pFURCuXpwwsagwQiDOqv93scNQYXpjwDbzaKG5LtVPR5clu_Q09n57LoioEjj_W1wWzecSWCC6FSvZRLqNIT8Ox5XnjPtuLKum3rNBZyDqkryxPrOb-7em4wURmCVi4by4Jo8GlNuEHIaNN4pZB67DrRg_Atbnd5ra0Ar_ljR9IyjLFMvxs7XqKxlbHu9F4wx6YasyR0dLsxyyu0584Ajxqn1DAZvDMUphOtqBa2iz7yXUOSUJfw5o7goV5B5dtPq37bBKofFJ-jrIA3IgbfT0Wa_zKEGSvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15e41163a.mp4?token=QiN_k1Jlr6M-sOQebpQu3UJwYFKfVzaTcE1ras33LNHklCd8ZF-u79pFURCuXpwwsagwQiDOqv93scNQYXpjwDbzaKG5LtVPR5clu_Q09n57LoioEjj_W1wWzecSWCC6FSvZRLqNIT8Ox5XnjPtuLKum3rNBZyDqkryxPrOb-7em4wURmCVi4by4Jo8GlNuEHIaNN4pZB67DrRg_Atbnd5ra0Ar_ljR9IyjLFMvxs7XqKxlbHu9F4wx6YasyR0dLsxyyu0584Ajxqn1DAZvDMUphOtqBa2iz7yXUOSUJfw5o7goV5B5dtPq37bBKofFJ-jrIA3IgbfT0Wa_zKEGSvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات خلبان هواپیمایی زاگرس در خصوص نبود رادار و تاخیر پرواز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/694966" target="_blank">📅 22:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694965">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77717107eb.mp4?token=Kugs0uT2O-9M3WlOqyzkRFPtIzHGHmuJ-hg_IpHQthRARlEyHWn-_LEZVJckYxV_riyQ5LYUOuJJUEKomNrlr4iK3nuQCyxxEgSlnw3AV3rZQ_jXpapkpICNIBgHB-661oZRcKv7QUuG2fFkkL3by68l6Iv4rMWx792dLtbkjVXGTjwojeeU5yEWgJsamCzC0vYpAgvBbiX3WPgD_8vXA-alXGO8fR1rM6AKg1Cc_4GqtxceTyen24UYR8EjDKUruso1ZsMOXlT5iqefzkCxlIH7J_cQq4QzsVdTmUqDDJB_oEXMd6O-V0JegfiKGWVlLYjOZ2k_TmjwT0UGpXpuIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77717107eb.mp4?token=Kugs0uT2O-9M3WlOqyzkRFPtIzHGHmuJ-hg_IpHQthRARlEyHWn-_LEZVJckYxV_riyQ5LYUOuJJUEKomNrlr4iK3nuQCyxxEgSlnw3AV3rZQ_jXpapkpICNIBgHB-661oZRcKv7QUuG2fFkkL3by68l6Iv4rMWx792dLtbkjVXGTjwojeeU5yEWgJsamCzC0vYpAgvBbiX3WPgD_8vXA-alXGO8fR1rM6AKg1Cc_4GqtxceTyen24UYR8EjDKUruso1ZsMOXlT5iqefzkCxlIH7J_cQq4QzsVdTmUqDDJB_oEXMd6O-V0JegfiKGWVlLYjOZ2k_TmjwT0UGpXpuIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای لو رفتن عملیات وعدهٔ صادق ۲ و دستور شهید سلامی برای ادامهٔ عملیات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/694965" target="_blank">📅 22:39 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
