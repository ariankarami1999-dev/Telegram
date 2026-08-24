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
<img src="https://cdn4.telesco.pe/file/oOacAhha7vINREydCT6bMq_lg_glAXWVujcodFfab_407WhmUqUZQSoiYqndGFXWLE_2ZrzuhMuhk2uWa7OdXRKof1Dt1-ZJQIVInZPRtPEiDCXqd40OzrqD2_cjOZs4dRHDqj3dwFM7YxnEjeDRf73U0iK3kVrHHeafNLFgERBvJupZyLNTnYNERGLlvA0eCBPV7o5RAU4QbMvpAhKEzcUwEIu94QbM2Sc0yrlQguKfmAlrXiV4myxuOg7upAeoX8L4hio8GZn0lylq7zkT5FdvuQc37407o7K8_iG0NwuJ5iSzL4OaYP8z8AAxfwVIWAIkwbgbvsWh8kOmjnPbxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 118K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 03:13:02</div>
<hr>

<div class="tg-post" id="msg-70547">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/news_hut/70547" target="_blank">📅 02:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70546">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAkJaXwEMNKff3J6OoEyk4PQjGdJuTI0nZZNxHAcjtG_BW-67CViCm6_N7bodvzf-qcaRUPFWyMbjXD6qXvah9Wz-4HumO2LqO6W4mYtXnYWcG5SCRNXtyAucHzxnYOflu9B376NWpKJrbUjXni3hO1spncV29J9LGK5qpLpaiPXcaWX7L1TFk-NiKewvCOX1xGVBblv4Oywt9dy9ZNlouLy-2JQgMxN6ItaeSwva8bT_cINcFFOMwt4E45SJZ-V39v1Wwp0tMAaGVeylKzh8SIozBh2nHjW6WRdwIgmuYqiv3Y7tyhkdOR5L3PRSoOAeUbpiVcv-KW4fvcwF0KCxBg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAkJaXwEMNKff3J6OoEyk4PQjGdJuTI0nZZNxHAcjtG_BW-67CViCm6_N7bodvzf-qcaRUPFWyMbjXD6qXvah9Wz-4HumO2LqO6W4mYtXnYWcG5SCRNXtyAucHzxnYOflu9B376NWpKJrbUjXni3hO1spncV29J9LGK5qpLpaiPXcaWX7L1TFk-NiKewvCOX1xGVBblv4Oywt9dy9ZNlouLy-2JQgMxN6ItaeSwva8bT_cINcFFOMwt4E45SJZ-V39v1Wwp0tMAaGVeylKzh8SIozBh2nHjW6WRdwIgmuYqiv3Y7tyhkdOR5L3PRSoOAeUbpiVcv-KW4fvcwF0KCxBg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
⭐
کانال اطلاع رسانی سایت:a2
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/news_hut/70546" target="_blank">📅 02:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rsfGYcdPwrc6qah3QD-RuO5pTHFIttzSolZYe50IUSJ1CvlBuEWmts-PEwsxl4tL9LeJXrfuX_lWK-DbDkgB-mqAQoBf4dGV2xSTlGGfo8Aa3I9PhZhdsvXLKPO14btBfKfv9V-9tnZAWfkti969IY93pXZCOjSTSd6S-no2T2FfsDvCdLzmm3I4TEkAIDm99aD_E5UbIesj_N83tHos6CqeGFsiRTadU7MWyvTG9fR-TsvfKgPUcrYH0IFloSsfAXMT1J5fDTwkbUGqoAQVg2lN6TAo2ElpGveUCcwHrjGvtpsspy9TxMXrCnaCQAeAKH9RA021DIyB_rC6YqKbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5fWVYfMRjoNqqBRNbC__hG3jM6Lyw4B9fFBkwc_kieUqWovncxZppgkuMfRH4MDHNw3Ac_xYmKIr_DNOCtrkFIj26sOaNmZ7zkkldE57LAkbrdwVmS2WchJhsp3TZDT7OJ1H7BTMFmPnSH3i7KdrZsenDMO8iCowwgAMfrEksGs1KS_0Im_3yw1qLVNE8I-3whgqbdtcwH3irFQ5_VoaalBSfLIGKoHWuKGRXva_G76p-gPfQioLMESjFJBuo9uIa8Yk0JIyNA7sRYJmlJ1Q3hqMZPkWvGaA8vK-28ODGXl5czCIxm1QzkA5baeS92KCyzU9JG0zdK8HnMlgPkN5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
#فوری
؛وزارت امور خارجه ایالات متحده:ده میلیون دلار برای کسی که اطلاعاتی درباره رهبران سپاه پاسداران انقلاب اسلامی ایران ارائه می دهد
احمد وحیدی/ فرمانده سپاه پاسداران
علی عبدالله/ فرمانده نیروهای مسلح (خاتم‌الانبیاء)
سعید آقاجانی/ فرمانده واحد پهپادها در ستاد هوافضای سپاه پاسداران
حامد لشگریان/ فرمانده واحد سایبری در سپاه پاسداران
مجید خادمی/ فرمانده اطلاعات سپاه پاسداران
⭕️
خبر واقعاً دوباره در ۲۴ اوت ۲۰۲۶ در حساب (Rewards for Justice)منتشر شده است اما تصویر قدیمی است و بروز نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/news_hut/70544" target="_blank">📅 02:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70541">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=RkGRlQitW4uZbZGzWCAGMQlLJhSRSbZG3BKefCM3G0nc7y3mtHxP-ffgY3uaUq1g4jMTKveQNsPd10S4Hg2m4PfkR0_TXbis6H-jFV6AxS3ZAe44nXX9Ip46Fu93PllONj5-LlQVsr-4wIjsQJ8hjYM3OJr06-tjCjl6bt0nosIZyrXZbAqeApCIzdX7qS8oVjfLu0JyLqLym4UNpYgFegYY9TEeQLib8cXm9eRgZpxpzifyhDbLCEnFAMuAcc03IpRwWufTH-RzmqT49dhB0nl6hSBqgfn2o2-UacoMvDzjfw3OMnAqkEF6zzdqEO4QkIFMkAH7OjgL_hOaqo1yLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=RkGRlQitW4uZbZGzWCAGMQlLJhSRSbZG3BKefCM3G0nc7y3mtHxP-ffgY3uaUq1g4jMTKveQNsPd10S4Hg2m4PfkR0_TXbis6H-jFV6AxS3ZAe44nXX9Ip46Fu93PllONj5-LlQVsr-4wIjsQJ8hjYM3OJr06-tjCjl6bt0nosIZyrXZbAqeApCIzdX7qS8oVjfLu0JyLqLym4UNpYgFegYY9TEeQLib8cXm9eRgZpxpzifyhDbLCEnFAMuAcc03IpRwWufTH-RzmqT49dhB0nl6hSBqgfn2o2-UacoMvDzjfw3OMnAqkEF6zzdqEO4QkIFMkAH7OjgL_hOaqo1yLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم تکون دادن ترامپ در رویداد «Freedom 250 Grand Prix» در واشنگتن دی‌سی، برای آغاز مسابقه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/news_hut/70541" target="_blank">📅 02:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70540">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kik2-bqtZcARdXH1IQCDX1VBkRl4qCnj9pnFkA27qh1wAKYANuUjcenBwviB2pCmMJBy1zKB4FVGPQOVAy071z1kx5QfVqkRYdxxZmTRroGBM2hENyOCzsZM7wKS9uUyrrFFuFwqtQejtSrul_37AjsvnWa1ctESk4NLJ0bU3kKIUOuRplY8daxliVZhgJ1LcxgVsAgXYb7e8PiLNxKiLW148j_A6Eeh_Fqtf5Yr3LaiVcNU1r1K0oY4ifVdLIHy9Z-i-fgXGVjtTQcAnQ8_VoA1CqGiSHpBQs8bThMQkjammOxay3Ixyn0wtz23Ym_CRUrBWezPkounuKoyjD61kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا:
ما گزارشی درباره وقوع یک حادثه در فاصله ۹ مایل دریایی شمال‌شرق منطقه الشیشه در عمان دریافت کرده‌ایم.
یک نفتکش مورد اصابت پرتابه ای ناشناس قرار گرفته، بخش موتور آسیب دیده و کشتی از کار افتاده.
خدمه سالم هستند و تاکنون میزان تاثیرات زیست محیطی این اتفاق مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/news_hut/70540" target="_blank">📅 02:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70538">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6611759db.mp4?token=kAuDvBqAi85HudRTKUsv1kpZ16VlC1fHFkAY3HTAWbQKete1SD3FS1cZJKmRBUTZU4ruEcZst4lH3hvqbY9-INxtdkX78dlQiDq4F9BccvWtlJkPEUMZtvO6H4uHJGjCrX8MvtQCD6N2y-7HdWASQnhKbk-ohJuiWH66UWbYyAVKIEDi_xts_iIak0vJ5k_fHSkVF6gOgXKVCOnKLavqjyZuBR9kJ9Y5errAdigEjWTsjmTFWO0ZdeHjHM9NgQGzmrS2EKu8PC01YOnjep9kNnJputUu2G4_Ik9039k1zc5A2Kf6keL7zgVvuAE2dXmp5PVXjS8ybEDxUuT-l3CIaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6611759db.mp4?token=kAuDvBqAi85HudRTKUsv1kpZ16VlC1fHFkAY3HTAWbQKete1SD3FS1cZJKmRBUTZU4ruEcZst4lH3hvqbY9-INxtdkX78dlQiDq4F9BccvWtlJkPEUMZtvO6H4uHJGjCrX8MvtQCD6N2y-7HdWASQnhKbk-ohJuiWH66UWbYyAVKIEDi_xts_iIak0vJ5k_fHSkVF6gOgXKVCOnKLavqjyZuBR9kJ9Y5errAdigEjWTsjmTFWO0ZdeHjHM9NgQGzmrS2EKu8PC01YOnjep9kNnJputUu2G4_Ik9039k1zc5A2Kf6keL7zgVvuAE2dXmp5PVXjS8ybEDxUuT-l3CIaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
برخی از کاربران فضای مجازی مدعی شدن امروز برای اولین‌ بار جایگاه های بنزین تهران با کمبود بنزین مواجه شدن:
@News_Hut</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/news_hut/70538" target="_blank">📅 00:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70534">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK23w5zRf1tlNLx2C1ErXZl-5ua4eIO5M6l_nGhoBpZVbNOaPgIEUZ7o__RXpEwjgRQVcn6yfZXBk1P-wz6AW1_8llgknnKn7hvfe9BShDrDCbhsdWoWbnxi7VVG4pewT4cUhXU4nBLbcy0GFPDPDiOgpIWbsXR42CYgMLMSzj_g2vDoHABISma1J43L5f5DkSJCZT-troRFeoLq8lQYAevCA3vodLMXq6g-iv66aP40g2cHvO9hYz1150I2TEqACt7Q8nvMNHHUOYur5sXSu4fpSToobshiGl7p2rFtozBFaqxVxsWy_gWDAL-d5gOcvY1pbmy3D-mOTN-wgPaRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a3f2ccf.mp4?token=o5vIqMA5ugdGHFVik30OIbLhAvGU5iRud1dhlUrjNMGz5cE2SIFaKMHqRfPmknhAbLVW1dRM5xd77_6ULf5yDzg7Z7nUyDwHPXg4PgZbowWYYdn4db-EsvsjILyzE7X31OTf7_4zK4ihCubZwONp33n5y0LGxZyUyOibkJI4WUZ3ibDKvZqwRf0UpYEw-AY2tmEGiRd5qqcw7WinXyScp9EQ4aEEmEIsXEGG_oMuRDJ_L3XwNM6LbQFHantUaJABMuRozmTyMOAOLAxW-YChaB_ShjNB-M6Q_L3kczhAVleS8avW85Th7CCaFnBYvkPcVZhTL3xJP9orvDRpWrXnsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a3f2ccf.mp4?token=o5vIqMA5ugdGHFVik30OIbLhAvGU5iRud1dhlUrjNMGz5cE2SIFaKMHqRfPmknhAbLVW1dRM5xd77_6ULf5yDzg7Z7nUyDwHPXg4PgZbowWYYdn4db-EsvsjILyzE7X31OTf7_4zK4ihCubZwONp33n5y0LGxZyUyOibkJI4WUZ3ibDKvZqwRf0UpYEw-AY2tmEGiRd5qqcw7WinXyScp9EQ4aEEmEIsXEGG_oMuRDJ_L3XwNM6LbQFHantUaJABMuRozmTyMOAOLAxW-YChaB_ShjNB-M6Q_L3kczhAVleS8avW85Th7CCaFnBYvkPcVZhTL3xJP9orvDRpWrXnsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خرسی که وایرال شده بود مهمون سفره کوهنوردا میشه
متاسفانه رئیس محیط زیست مشکین‌شهر از شکار شدن این خرس خبر داد
💔
شکارچی هم همراه ۴ لاشه از حیوانات کوهی دیگه دستیگر شده
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/70534" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70533">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaOswemOIouSiW3BfjvPQpm6MOIXAsMeAuf-PRWjeg8rylu6ABAi6MHAO-G9RjUOPCKqSlO9hVQ9B36Q1_-FBSj0VtZOIK551mI4agvmr17XdeQoTRXn7PWgPYU9TQxDTzLy77_ZMKJpEfVwz_Fc1aAmdt0FRYbre09HKxDdSAkrMtbtvbGewg1r1skqh5D2ObvFUXy-qpMClXzkOAmBq2kW8hctIMW51yj0on17zGjc9l1yBPOE_KJtZp1R7pjY4xK49gOnn9R6JVw2BYFTQeHPqvpxR9ylYpH2i37xRWyqEy2vUKMZDatosT-SJ5QG0bVLjGZQYb68TJcPHb1pCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
به دونالد ترامپ، رئیس‌جمهور آمریکا، و اسکات بسنت، وزیر خزانه‌داری آمریکا، بابت تحریم‌های جدید علیه جمهوری اسلامی تبریک میگم.
شما کاملاً حق دارید از این دیکتاتوری سرکوبگر و کسانی که به ادامه اقدامات تهاجمی اون کمک می‌کنن، هزینه سنگینی بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/70533" target="_blank">📅 23:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70532">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=QdD0e1gt8ao8wkzkmll9Rg5ZRqOJt6CFDtStoq9RxRXh8IcC8XZbPiTF16m5Mv8VdO7QV-V8eYe3hDmmTRqgfACT8M9G_bYdPeWRv_8qIq8TU55sBybSQNRvROBnGlJYpYjjn8DGpf5cPJ0yv8MKmEW5M909nTiNhzmb0DAtYRQITen4ypfHzD2hYlzuQuG801dQHg5bWt0MK_khOC6oDVFrh3dzeTg6C10UFJuzYZQk0gFVHShvOU7Mw03XtE7j5iXWM4EyEVo38Sf3N5PqC1medJ1zXVkYomEhxt_R6_1T6iOQxdQNRqmjjXM3KHiuCw5Gs2Q2RAKbbKUJYo9okA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=QdD0e1gt8ao8wkzkmll9Rg5ZRqOJt6CFDtStoq9RxRXh8IcC8XZbPiTF16m5Mv8VdO7QV-V8eYe3hDmmTRqgfACT8M9G_bYdPeWRv_8qIq8TU55sBybSQNRvROBnGlJYpYjjn8DGpf5cPJ0yv8MKmEW5M909nTiNhzmb0DAtYRQITen4ypfHzD2hYlzuQuG801dQHg5bWt0MK_khOC6oDVFrh3dzeTg6C10UFJuzYZQk0gFVHShvOU7Mw03XtE7j5iXWM4EyEVo38Sf3N5PqC1medJ1zXVkYomEhxt_R6_1T6iOQxdQNRqmjjXM3KHiuCw5Gs2Q2RAKbbKUJYo9okA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اوستاد خوش‌چشم :
جنگ بعدی تو آبان و آذر با بمب باران شدید آمریکا شروع می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70532" target="_blank">📅 22:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70531">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">با این کیر شق شده‌ای که من از اسکات بسنت و ترامپ می‌بینم، مطمئنم خیلی زود دلمون برا دلار 200 هزار تومنی هم تنگ می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70531" target="_blank">📅 22:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70530">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=ntyA5bVAC4l0Kg25c9FUj-12-INHN6OQaKDKKZjDdnAzYr2zh-WoTvIBcYxiGweOOZDg9g5gBi8mQc70PNbQd2xKo3z9Eb_B6Nkms0KgBlEZw59vfmjvHqfIhndGZt2qNmtYAk0lABnKu8O5oQkwCYJ9c6NrmkPLU5Z5la1Gtrm5eFcAfXXU7VVQpt09lv7xv-8FKhcCFLi58NPsRIAm2ntOMCtRDFMY3JeUi303uISETOS1jqtAZVmafZZovpgO-9rqSaTKyTuoFAZTDLjBxDPgjA7iAcONtr0WFbFrDFMBF9HGtgDGLlkSG6NsrmLUz-j3Ai1DcZvCZSG8qaDffg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=ntyA5bVAC4l0Kg25c9FUj-12-INHN6OQaKDKKZjDdnAzYr2zh-WoTvIBcYxiGweOOZDg9g5gBi8mQc70PNbQd2xKo3z9Eb_B6Nkms0KgBlEZw59vfmjvHqfIhndGZt2qNmtYAk0lABnKu8O5oQkwCYJ9c6NrmkPLU5Z5la1Gtrm5eFcAfXXU7VVQpt09lv7xv-8FKhcCFLi58NPsRIAm2ntOMCtRDFMY3JeUi303uISETOS1jqtAZVmafZZovpgO-9rqSaTKyTuoFAZTDLjBxDPgjA7iAcONtr0WFbFrDFMBF9HGtgDGLlkSG6NsrmLUz-j3Ai1DcZvCZSG8qaDffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیوی وایرال شده از یه پیرمردِ حامی حکومت که به طرز سنگین و عجیبی داره پرچم تکون میده:
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70530" target="_blank">📅 21:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70529">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9839729319.mp4?token=Nsab7gMcNhOylfme6s_wG-UtL5esaOu0ysaeZpWHCC8ilA-gsGezpkYK9-VpqghzMfxvS78SvPfBfBV-Y9QWJyYhKkwEavnw8DKqoWje2jEzAMJfXMCVcqrnqBxPqlkFAkc0oyPs5984apFAEotceBvknAqfZ-9yAsNxGs5zL_zOqiIbokveB0GSHP0DwwoeHtszmBpuic9dasA9TMxdBSog0BAPH9ntNDl3sLdJjUCO5pBps4CYeiBdOEwaH2Yl0mC10ZPRvTQ0Zn760kwYlmFU_aI0hRE572xmCyjUWc9XA2gMxC5vb4O5Ek0-HXtrhjld99Fm6YazcUQURu3I7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9839729319.mp4?token=Nsab7gMcNhOylfme6s_wG-UtL5esaOu0ysaeZpWHCC8ilA-gsGezpkYK9-VpqghzMfxvS78SvPfBfBV-Y9QWJyYhKkwEavnw8DKqoWje2jEzAMJfXMCVcqrnqBxPqlkFAkc0oyPs5984apFAEotceBvknAqfZ-9yAsNxGs5zL_zOqiIbokveB0GSHP0DwwoeHtszmBpuic9dasA9TMxdBSog0BAPH9ntNDl3sLdJjUCO5pBps4CYeiBdOEwaH2Yl0mC10ZPRvTQ0Zn760kwYlmFU_aI0hRE572xmCyjUWc9XA2gMxC5vb4O5Ek0-HXtrhjld99Fm6YazcUQURu3I7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
«بِسِنت» درباره ایران:
کشورهای حوزه خلیج فارس در طول سال‌ها از سیاست مماشات با ایران چه چیزی به دست آورده‌اند؟
زمانی که ما ایران را بمباران می‌کردیم، ایران کشورهای حوزه خلیج فارس را بمباران می‌کرد.
سیاست مماشات در قبال این رژیم کارساز نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70529" target="_blank">📅 21:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70528">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fd4a88095.mp4?token=Q2zMBvZ_UmUj3TxSG4-pIWQVkpurXOi7Fk5E7opFCrQCIqfv5O9B_XOSXeqpxxmvlAmhGwQYFhsJHKQC100CvpGdCGg-TeiRQfcAaeZc2MDXm8NMGCu72N0Q1A8QeB6FqfZ5tSEejU1QkrQrjClqPQbs1AmagcFn3QPV0OZsuqJPw3FolfTlG9S9BmotuKMnExxdEWcAFt7nudRjsGhzPzWUR8SumNmTgG5nsDqc-5UqYxqFv1MURVkY2cP-KeigaYRsYSyowaVKmKAd8Q-PhgsQ33vhZVkNr2G5CNzIbLPjv0qsfyCU6MJgjwqOba1EDznyDvbjzjPuSbmdam5bhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fd4a88095.mp4?token=Q2zMBvZ_UmUj3TxSG4-pIWQVkpurXOi7Fk5E7opFCrQCIqfv5O9B_XOSXeqpxxmvlAmhGwQYFhsJHKQC100CvpGdCGg-TeiRQfcAaeZc2MDXm8NMGCu72N0Q1A8QeB6FqfZ5tSEejU1QkrQrjClqPQbs1AmagcFn3QPV0OZsuqJPw3FolfTlG9S9BmotuKMnExxdEWcAFt7nudRjsGhzPzWUR8SumNmTgG5nsDqc-5UqYxqFv1MURVkY2cP-KeigaYRsYSyowaVKmKAd8Q-PhgsQ33vhZVkNr2G5CNzIbLPjv0qsfyCU6MJgjwqOba1EDznyDvbjzjPuSbmdam5bhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
بِسِنت درباره ایران:
کسانی که در کنار ایالات متحده می‌ایستند، از مزایای شراکت ما بهره‌مند خواهند شد.
تمام شعبه‌های بانک ملی(ایران) باید تعطیل شوند.
🎙
خبرنگار:
گفتید ترامپ با رهبران جهان تماس می‌گیرد. او با چه کسانی تماس می‌گیرد؟
🇺🇸
بِسِنت:
ما نامی از افراد نخواهیم برد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70528" target="_blank">📅 21:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70527">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d89159ae.mp4?token=BTx5t1p2UNPI-Xw6PfPd1EQpt4b2bClGU89hDoU4lmnLqcTsN9pCEJNSXHyY00_miAL4drkWicNvrJ_1NnPHR1-H8hfCLT6EU1s8SXbeWpFKZOmUX_kyUNx-j4yCmBQUSVLozYQHcGACVwMHCS64JybxMDe3OEr0g4AA4rMiDAbmUhUKdaUtG8mBdCeTctRCwy9crRT2QE8UCcmg6Jbj5sHB4FX0CweyEP-veZDnf_M7MRe-K0yJ64MmiVpfrWWmf97ob8YOHAek2dfSo_sTtM7cI48v7LYPbSanyvL24cfbiwp58lMYotPQq4anUcSQ8ZDN73zysdn5vE3MSOC_Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d89159ae.mp4?token=BTx5t1p2UNPI-Xw6PfPd1EQpt4b2bClGU89hDoU4lmnLqcTsN9pCEJNSXHyY00_miAL4drkWicNvrJ_1NnPHR1-H8hfCLT6EU1s8SXbeWpFKZOmUX_kyUNx-j4yCmBQUSVLozYQHcGACVwMHCS64JybxMDe3OEr0g4AA4rMiDAbmUhUKdaUtG8mBdCeTctRCwy9crRT2QE8UCcmg6Jbj5sHB4FX0CweyEP-veZDnf_M7MRe-K0yJ64MmiVpfrWWmf97ob8YOHAek2dfSo_sTtM7cI48v7LYPbSanyvL24cfbiwp58lMYotPQq4anUcSQ8ZDN73zysdn5vE3MSOC_Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اظهارات «بِسِنت» درباره چین و ایران:
امروز می‌خواهیم به صراحت اعلام کنیم که هیچ‌کس از دسترس تحریم‌های ایالات متحده مصون نیست.
اگر آن‌ها تراکنش‌هایی را تسهیل کنند و بخشی از آن چرخه‌ای باشند که نفت ایران را به پول و ابزار سرکوب تبدیل می‌کند، هدف تحریم‌ها قرار خواهند گرفت.
⭕️
اکنون زمان آن فرا رسیده است که رهبران جهان میان آمریکا و ایران تصمیم بگیرند.
انتظار دارم تا پایان همین هفته شاهد اعلام خبر مهمی مبنی بر اعمال تحریم علیه یک مؤسسه مالی باشید.
🎙
خبرنگار:
شما این وضعیت را یک «روز دی» (D-Day) اقتصادی توصیف می‌کنید، اما «روز دی» صرفاً تهدید به تهاجم نبود و ایالات متحده هم برای آلمان ضرب‌الاجل تعیین نکرد. چرا تحریم‌ها همین امروز اعمال نمی‌شوند؟
🇺🇸
بِسِنت:
چرا باید بخواهم نظام مالی جهانی را منفجر کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70527" target="_blank">📅 21:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70526">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155ae6e1ec.mp4?token=Dcg85yQB-zfx45ZAlqfNAZphXYnRFSVTEFWwpQ9snkqjfAsn320eiHEfftPwE9LinGvSrClUS1incRthjgjPjuKPY8qLwZaJsWHu9umQIZSl4eR3oYGB3sCMVWl6GsAfr5NDosDR0z4kiBS1paeG86b3A8wkMWWPhaDs7euepwHBrArvA72ahiQhAS0UFHEUR4fN-0yF7q37kDmt8TtKuy3ZrxHxEy1AhfqWvSOwsErhGij65ptwUi0jhthnILEbuRd7mIHGPZfeUNBtXagGXboS2yxNSvtcI6dm_isc0grYQ5FIHcnzRLYwsDPOc1f8t5Utn5ItwZ_AoNXwSBUdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155ae6e1ec.mp4?token=Dcg85yQB-zfx45ZAlqfNAZphXYnRFSVTEFWwpQ9snkqjfAsn320eiHEfftPwE9LinGvSrClUS1incRthjgjPjuKPY8qLwZaJsWHu9umQIZSl4eR3oYGB3sCMVWl6GsAfr5NDosDR0z4kiBS1paeG86b3A8wkMWWPhaDs7euepwHBrArvA72ahiQhAS0UFHEUR4fN-0yF7q37kDmt8TtKuy3ZrxHxEy1AhfqWvSOwsErhGij65ptwUi0jhthnILEbuRd7mIHGPZfeUNBtXagGXboS2yxNSvtcI6dm_isc0grYQ5FIHcnzRLYwsDPOc1f8t5Utn5ItwZ_AoNXwSBUdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
«بِسِنت» درباره ایران:
⭕️
خطاب به سربازان عادی حامی این رژیم:
در شرایطی که پرداخت حقوق‌هایتان بیش از پیش متوقف شده یا به بهانه تأخیر به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشور را به سوی پیروزی می‌برند یا نابودی؛ و به یاد داشته باشید که دیوار برلین زمانی فرو ریخت که سربازان عادی تصمیم گرفتند به سوی مردم خود شلیک نکنند.
⭕️
و خطاب به کسانی که راه را برای تهران هموار کردند:
بهای آزمودن عزم و اراده واشنگتن را دست‌کم نگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70526" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70525">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91fbf3e30.mp4?token=LIgxmoFjKn55xa3YHMCu3BH2vnQsH1EKh8dMzQfCCuDDDckr6O0mzDm07Y5n2XK-lXyTvDBQK68cLRk8Nj260i112fQDK50YvoyWIHgm8rJ1CeHnOAqXWr1vspAu7q6Boq6pPACrskWdBl64SbVl-iBa9HPAtcSwymYSyTRZgWK7sN9tbpXZSnNuVke6TJRt6uV0v1xEdTi1a4x6emK-ryARPKaZnQoIYxscAzouOJ8yaLMIpQYCJis6qkrErvvYFzQHOwyuUIoGFvBwAxQwf0Bzh9Ezzwx38MG12dqCi3N0Bnvm2wltDHFhwVvbMxRKp4HkNlPuk8qMHNhIxzaljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91fbf3e30.mp4?token=LIgxmoFjKn55xa3YHMCu3BH2vnQsH1EKh8dMzQfCCuDDDckr6O0mzDm07Y5n2XK-lXyTvDBQK68cLRk8Nj260i112fQDK50YvoyWIHgm8rJ1CeHnOAqXWr1vspAu7q6Boq6pPACrskWdBl64SbVl-iBa9HPAtcSwymYSyTRZgWK7sN9tbpXZSnNuVke6TJRt6uV0v1xEdTi1a4x6emK-ryARPKaZnQoIYxscAzouOJ8yaLMIpQYCJis6qkrErvvYFzQHOwyuUIoGFvBwAxQwf0Bzh9Ezzwx38MG12dqCi3N0Bnvm2wltDHFhwVvbMxRKp4HkNlPuk8qMHNhIxzaljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اظهارات بسنت درباره ایران:
از امروز، حلقه محاصره را تنگ‌تر خواهیم کرد و تمامی منابع درآمدی احتمالی را که بودجه سپاه پاسداران و رژیم ایران را تأمین می‌کنند، مسدود خواهیم ساخت.
ما رویکردی را با هدف جلوگیری از هرگونه نشت (دور زدن تحریم‌ها) به اجرا می‌گذاریم.
ترامپ با رهبران جهان تماس می‌گیرد و مشخصاً از آن‌ها می‌خواهد که تعاملات خود را با رژیم ایران متوقف کنند.
هر نهادی که به نمایندگی از ایران پولشویی را تسهیل کند، از سیستم دلار آمریکا حذف خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70525" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70524">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75070defdc.mp4?token=diznu9Sk_T9YE5_L4Izb3yPWIFq07_6mTSgXj-hNxUAs8lvdaNJL49l4sDKlE1PFzuMxBNNOKMd5pYGb7A391eSRLBTCXVTV1Z6CDkDR3XHmcuN-GSKF6GpU8YR5ouq7qakWDbmzdEFu6bkVFM7Qyntz8RqLZsHRGoh866PMAPiDPf_mwqrMIPHJa4VC0D_wc5z5TVIxQ8VMs2jtCAmOcINc1i-bdmNNg4JeK3sO24KJsc9GbRxsOFp3nQwSS8WPwm_m6QSSTuw3W_hxfnPOZf8tjQdLwR1RtF00YqrD3hJDv5detUbM7h126a41RQfQzKrPTtSEGOdQ9H6UCSGIaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75070defdc.mp4?token=diznu9Sk_T9YE5_L4Izb3yPWIFq07_6mTSgXj-hNxUAs8lvdaNJL49l4sDKlE1PFzuMxBNNOKMd5pYGb7A391eSRLBTCXVTV1Z6CDkDR3XHmcuN-GSKF6GpU8YR5ouq7qakWDbmzdEFu6bkVFM7Qyntz8RqLZsHRGoh866PMAPiDPf_mwqrMIPHJa4VC0D_wc5z5TVIxQ8VMs2jtCAmOcINc1i-bdmNNg4JeK3sO24KJsc9GbRxsOFp3nQwSS8WPwm_m6QSSTuw3W_hxfnPOZf8tjQdLwR1RtF00YqrD3hJDv5detUbM7h126a41RQfQzKrPTtSEGOdQ9H6UCSGIaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
اسکات بِسِنت:
ما در حال آغاز یورش اقتصادی علیه پیوندهای مالی ایران در سراسر جهان هستیم.
هدف ما قطع تمامی شریان‌های حیاتی اقتصادی است که این رژیم ستمگر را سرپا نگه داشته‌اند؛ تا زمانی که تهران کاملاً تنها بماند.
🔴
در دوران ترامپ، آمریکا دیگر صرفاً تهدید ایران را مدیریت نمی‌کند.
ما در حال پایان دادن به آن هستیم.
ایران دو مسیر پیش رو دارد: انزوای کامل جهانی یا مسیری به سوی بازگشت به وضعیت عادی.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70524" target="_blank">📅 20:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70523">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b43c7e4e6.mp4?token=T_x9SDWCCgtadPUfu9KZVKRcEROfj3_8g3zUwkS0u0o8v4cwVQ2cyFKSvTZEhJVVyhWdXW0D9f8tBsm9nYpOWDDSbRhOar5THRCjtJdp3c84_4g9CIIGgk6_yR7BEI3BEjqOkB8MsfKdEl0unsAhQCF1CIbV93iqxm8_a9YOQNUwBmHFHD3poU24IBjKAaYyeu27GC_XEmcm8p2mF8k2-2fm8lemBV0AGgdGN4HBHYWYLuERbE4mGwd1i0dj2QWsT57wzHniRCf0K0XNhBndgmySw9yjWVGY45J2pESSrWDsvrKBJ7nigUuJb2xvF5x5DqcGmXhcpCH2y-kyVHy_lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b43c7e4e6.mp4?token=T_x9SDWCCgtadPUfu9KZVKRcEROfj3_8g3zUwkS0u0o8v4cwVQ2cyFKSvTZEhJVVyhWdXW0D9f8tBsm9nYpOWDDSbRhOar5THRCjtJdp3c84_4g9CIIGgk6_yR7BEI3BEjqOkB8MsfKdEl0unsAhQCF1CIbV93iqxm8_a9YOQNUwBmHFHD3poU24IBjKAaYyeu27GC_XEmcm8p2mF8k2-2fm8lemBV0AGgdGN4HBHYWYLuERbE4mGwd1i0dj2QWsT57wzHniRCf0K0XNhBndgmySw9yjWVGY45J2pESSrWDsvrKBJ7nigUuJb2xvF5x5DqcGmXhcpCH2y-kyVHy_lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
اسکات بِسِنت وزیر خزانه‌داری آمریکا:
امروز، وزارت خزانه‌داری ایالات متحده «عملیات طرد اقتصادی» را آغاز کرد؛ کارزاری بی‌سابقه علیه جمهوری اسلامی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70523" target="_blank">📅 20:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70522">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akKsdCuyTo--wZ8RbT9O0QXGUTVCLoY6usIC2cT25sm5gpVY5lo0GeQ7YGCnSIc8_D8lJFHOl__YuSP0T1SSXKdJvrRS8uU188K7AHRgGMK8-5Hg_iTV-EnxxQL627_yHOjdw4EIvZn-mtBa0tu9wJb7qKAMfQm2jSdxlAuOkxv2B786LyhP0X4DYKM9aYzeLxc2iCef--kZHd_kAXwDz_56nqe0fH1lwZWfzbu8sgtWfioayO5Y54fNxMWWFGPbgbOA69MnwqrPVXqgzWZ7foaJE-pyd8_t0U9BMgm-mEOWnKrO4JRO_vQ9uUtFQLtl1ITcwVvanLpd5Nc63eVWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو:
ایران تلاش کرد یکی از پسرانم را ترور کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/70522" target="_blank">📅 20:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70521">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsRUcVYZg7Gf_5CXriG-7YbmQmF7Plq0D6Fl6AE-li9NuXqcoBLujDPTS9g-ogtUZT5Bxyt2xyLO_SPGD6u_EUV-0CU88Eshix1p77muzrpLLWLAwugXW_4mnLB7M9YO06ASzeZXL102XkKwQLJuwTWRgDnxeDRyVB4y3pUAl5zNoQBuDsg2vsymDX0G5qF07TCWYebjOJzgDiZ0XyP4W6h5BxHjOKWydJNT6Cj4-z1Vn9_5TiOgbw5Ip_f0M4HF1aFww39kAWJUGVoW3S3H87aDvumXyOfk0FwcsUXwq66DJUfW9nSHpQM52FHjrAbw7GW7ty1aWKcuKYRhYZo8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دموکرات‌های چپ‌گرای افراطی با انتشار نظرسنجی‌های ساختگی، دیوانه‌وار عمل می‌کنند. آن‌ها این نظرسنجی‌ها را در سطحی بی‌سابقه منتشر می‌سازند. این اقدامات «عملیات تضعیف روحیه» نامیده می‌شوند؛ تلاشی برای دلسرد کردن جمهوری‌خواهان تا پای صندوق‌های رأی نروند.
اما واقعیت نظرسنجی‌ها عالی است و روحیه مردم کشورمان در بالاترین سطح خود قرار دارد.
⏺
ما در حال پیروزی بر همگان هستیم، از جمله ایران؛ کشوری که در گرداب مرگبار اقتصادی و نظامی گرفتار شده است.
از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70521" target="_blank">📅 19:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70520">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGPOS_fRfEOjsJHy7agSxM8Y91HrthF_8DetgU-7ZhunD6oME8-_gZlS0xYqL4wLIUuBhJ1UvjVbjbiH3bymw-VDKFnbR61ws-mD_-Sp6Wfux_Ky8JQKsGxLVOuHktesmXd1py0sJdKDm40uWCvlSc4qXCTJtUguUSpJfIlq094Bd4QoxqkmDqzjuXK6zicJlbQM2ezHiXoqhND4vQVR7KUtzzZJzjiIAQrY_dNta7tE9VRIdzfDtqe51cUtRFJfEP2RkL2l4ahT0FS5_HVa7dbmzpRsYre8gf4CJKGt9qbPCVZ0j7pRyZQpKjPw3gskTmiaHAvAjasM7dDVx9HGAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
قالیباف در دیدار با عاصم منیر:
تعهدات طرفین در یادداشت تفاهم روشن است و این آمریکا بود که با بدعهدی مانع برقراری ثبات در منطقه شد و دلیل دیگری برای بی اعتمادی به این کشور ایجاد کرد
رئیس هیات مذاکره کننده ایرانی، ضمن رد تاثیر پذیری جمهوری اسلامی از فشارها، تاکید کرد: ما پیگیر اجرای شروط یادداشت تفاهم هستیم و این امریکاست که باید به تعهدات اش بر اساس تفاهم نامه پایبند باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70520" target="_blank">📅 19:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70519">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235f69fa4b.mp4?token=VaYkHP1cM0zJHRcHVU6Ebpl2SMjOlDQc7LYZ74Its6PVnvaGfA3dxtVnsUxkcWEx2vBNnze12J735mjwyaO4ilS0SC8mPI_53NA8P3kTIIudcSF5Z9HewNJPsIig-84S-IQROlk7IvY-rSuIvVAJJnNS_lYmUCoBWnqRGf0Ujd26ZnGgiqBr4UgFv3A9abxwPxanq7K5BKmiTE726HxryfvSkIvxdj39gbD9hmlwjSzzHvW1Qh4zYN_E1TmVsl2nVuEfxo_94WLrpLXNYG7VPermLHVa5hLK3BDNhoNFGQRUp6Y83mFnOnkavT9K721rvazLyni8Egf3wEwDtUjoIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235f69fa4b.mp4?token=VaYkHP1cM0zJHRcHVU6Ebpl2SMjOlDQc7LYZ74Its6PVnvaGfA3dxtVnsUxkcWEx2vBNnze12J735mjwyaO4ilS0SC8mPI_53NA8P3kTIIudcSF5Z9HewNJPsIig-84S-IQROlk7IvY-rSuIvVAJJnNS_lYmUCoBWnqRGf0Ujd26ZnGgiqBr4UgFv3A9abxwPxanq7K5BKmiTE726HxryfvSkIvxdj39gbD9hmlwjSzzHvW1Qh4zYN_E1TmVsl2nVuEfxo_94WLrpLXNYG7VPermLHVa5hLK3BDNhoNFGQRUp6Y83mFnOnkavT9K721rvazLyni8Egf3wEwDtUjoIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🟥
فاکس‌نیوز:
در حالی که ارزش پول ملی ایران به پایین‌ترین حد تاریخی خود رسیده و تورم همچنان رو به افزایش است، کاخ سفید آماده می‌شود تا آنچه اسکات بسنت، وزیر خزانه‌داری، «سخت‌ترین تحریم‌های تاریخ علیه ایران» می‌نامد را رونمایی کند.
ایران تهدید کرده است که علیه کشورهای حامی تحریم‌های آمریکا دست به اقدام تلافی‌جویانه خواهد زد؛ این در حالی است که فرمانده ارتش پاکستان برای تلاش در جهت احیای گفتگوها و میانجی‌گری برای دستیابی به توافق صلح، عازم تهران است.
همچنین انتظار می‌رود وزیر امور خارجه عمان برای انجام گفتگوهایی با هدف کاهش تنش‌ها پیرامون تنگه هرمز، به ایران سفر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70519" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70518">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بزرگترین کانال پیشبینی فوتبال در ایران
🔥
g2
فرم های ما رو از دست ندید...
⚽
@Tabanii_Mafia
@Tabanii_Mafia
⚽
@Tabanii_Mafia
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70518" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd3cM6LZl4dePOEFSvGMXgTiFWg9NjxpGVHN6QHHtw6I_0AgiNGldOufkSjYRH5WgrjClNDmjDkZnXoPk4tVzlWIo58-8UZSH6330HECT2Tj5Au3iePGaDycPAdGDUxK-hWm45iQ_-sgakcrA7sGQ67SYqCg5ZRSa5Wyf1JjwBvQVOOBenh-gTt5oQo9y7g53AFw3E2a5CdkmvzLZaN7bMUwWG4oH_T8jFUoejWnnXaqHOmks4TNTxiha5vPOW-SwFxepL-TIfw5v0362nrKQS6j2UB9CeKsq0oJZD1Iyle8yg6cvbd5ZP_v7dgMLLfIpHst_mTJn1mgNqgowdYe9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
❤️
✅
✈️
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/70517" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384afb6ff9.mp4?token=ffwCuopcahP72KiCwO7izQlwMO3fmRfXxsDQV-fIunewyARDHllTckRjJa7kWH8AFrqyDa3FiOPfGTV-ZJiWi6YQ_HcBoSUgIgaM5NL-dBcAjKggukHoWqb8bbQ-SnlwpPMWOGp6H5v6Jl_nUCvdzMoboRNFNGd7mSea1RQnyBBfAd7UTu0MkBsqexvjObQzaYln-fQXDI9FxxcJi9NQeELAGnh0K-hQNIE7SMITR-CktExq6zCef3oAUAuVlhjwttAr69hG4uJd0ZTbfo2XEB6NLNEA5buN58_CBxVKkFn8ctMOcF9vq9DHmdP1w87yss25S9Utgy_MoFJgJeogqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384afb6ff9.mp4?token=ffwCuopcahP72KiCwO7izQlwMO3fmRfXxsDQV-fIunewyARDHllTckRjJa7kWH8AFrqyDa3FiOPfGTV-ZJiWi6YQ_HcBoSUgIgaM5NL-dBcAjKggukHoWqb8bbQ-SnlwpPMWOGp6H5v6Jl_nUCvdzMoboRNFNGd7mSea1RQnyBBfAd7UTu0MkBsqexvjObQzaYln-fQXDI9FxxcJi9NQeELAGnh0K-hQNIE7SMITR-CktExq6zCef3oAUAuVlhjwttAr69hG4uJd0ZTbfo2XEB6NLNEA5buN58_CBxVKkFn8ctMOcF9vq9DHmdP1w87yss25S9Utgy_MoFJgJeogqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن حاجی‌میرزایی، رییس دفتر مسعود پزشکیان رییس دولت جمهوری اسلامی، از قطعی بودن کاهش سهمیه‌های بنزین خبر داد و گفت: «افرادی که بیش از سهمیه تعیین‌شده بنزین بخواهند، باید آن را با قیمت بالاتری خریداری کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70516" target="_blank">📅 18:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70515">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a8609222.mp4?token=HCwll2-nd_v0eSdxScq97RTFcJYjZ4iJOYfbAidiMMuqpJ6OvQKR_zxAUisggYzclRfQ6EkcGFI7PMOKKRbMxM2Y04NDyBKcS7-YTcJjLDz6VTgswqFW4cwe4jWoItwvl-cF-MQERBbIlZyn5jgOFhxsk1NcM9PpEd2FPI-l0u2C6fG5lAod0NJzYvNK4fh4m6_h8zWtJzbCXGQ-aeOA3_UkTs3FQMJ3REm7xYF3ZqokpbfRjoxd4bwNvZGCBx1T58uqktdpPtg3egeytdFeKeTq5rEB7XOSVKRjph9JeYVMjdAqFuYLcuoGe5e3kKr7G5vMFYQ2wHQiWOVTGuqYyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a8609222.mp4?token=HCwll2-nd_v0eSdxScq97RTFcJYjZ4iJOYfbAidiMMuqpJ6OvQKR_zxAUisggYzclRfQ6EkcGFI7PMOKKRbMxM2Y04NDyBKcS7-YTcJjLDz6VTgswqFW4cwe4jWoItwvl-cF-MQERBbIlZyn5jgOFhxsk1NcM9PpEd2FPI-l0u2C6fG5lAod0NJzYvNK4fh4m6_h8zWtJzbCXGQ-aeOA3_UkTs3FQMJ3REm7xYF3ZqokpbfRjoxd4bwNvZGCBx1T58uqktdpPtg3egeytdFeKeTq5rEB7XOSVKRjph9JeYVMjdAqFuYLcuoGe5e3kKr7G5vMFYQ2wHQiWOVTGuqYyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو ماهیگیر جنوبی موتور قایق‌شون خراب شده بود و چندین روز بود که وسط دریا گیر کرده بودن و دیگه جونای آخرشون بود
که ماهیگیرای عمانی دیروز دیدنشون و جونشون رو نجات دادن
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70515" target="_blank">📅 18:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=uj746qcWZKUb5rPHck2RAnVnt_666cJDffklCRXJE8ojABBBSLgRyRxux5kcvib8X0QoaBcU44Zg2ciDyFmLqm4oc6-wDLH0UTJ8pnuTB2rrA-EJZUvsHdoIqJXDEGlTZ6-uibpFuQKB2TPYrOjt3Ba9rSWcEpYMY5EaXKg2FAdmCV_Pu5QB1DxUGJU2iDnb52v4395v8hOqwULbrhc2cLQzXL6x7dtVIDjPRxEl9VkgHT_0z5-cBBRiblpke5SDjrjbE_ln4P8u7AVHqmwJQ4aouvRqvOiYK9jUBYVvnFjcjDzK1HnGKBGUWL8wbq0qoAiIRaY41f64XctRNZB9gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=uj746qcWZKUb5rPHck2RAnVnt_666cJDffklCRXJE8ojABBBSLgRyRxux5kcvib8X0QoaBcU44Zg2ciDyFmLqm4oc6-wDLH0UTJ8pnuTB2rrA-EJZUvsHdoIqJXDEGlTZ6-uibpFuQKB2TPYrOjt3Ba9rSWcEpYMY5EaXKg2FAdmCV_Pu5QB1DxUGJU2iDnb52v4395v8hOqwULbrhc2cLQzXL6x7dtVIDjPRxEl9VkgHT_0z5-cBBRiblpke5SDjrjbE_ln4P8u7AVHqmwJQ4aouvRqvOiYK9jUBYVvnFjcjDzK1HnGKBGUWL8wbq0qoAiIRaY41f64XctRNZB9gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به تازگی توی بالاشهر تهران، یه رستوران ساختن مخصوص شوگر مامیا.
خانمای میانسال جا افتاده و پولدار اینجا جمع میشن و پسرای جوون و خوشتیپ هم میرن اینجا، تا برا خودشون شوگرمامی پیدا کنن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70514" target="_blank">📅 17:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OdbB0-xsx3jJVSGv5v6zsl6spW3Ym86J6FzvSoPyP3PjWJYDJo7vBFE519Mpuw87RY1K-f6Tj-83N9k3ADers9ImCgmNVqPV9d6i4yxCEpv4yzTTZd8DTH1polWiEWQIDqchtgNWueBfPkyenaNFMiCZg_F5ez9vZh6kf-jsyxOQo83t6x5eBRVCqLqsH6Mt67iBnfzqtlg0FgigeeB80iMT7jShnuvBf8gVaoFuZajzACpsLzbgrr3yQISLjhy763Fym10ep-NX9wxLCQULBvi5KCAe-rKuXr3iDJsN9-OpjLarS38pNlcnRyT43QGvuIu-1IkwCn3BKekdfO2bbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قطع برق کمیسیون انرژی مجلس،هنگام بررسی علل خاموشی‌های اخیر.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70513" target="_blank">📅 17:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7GU8nshGaxGMUln0ImGGpMABUUj84BnbKBT2t12gFr3MlJtMHhb3WCjeTAG4SkxrO709txiH64hjZwBbPOwAE-eiKszFQjzrnz57qmsKbMXAlHzgDJ3pnPrP1nXqcE16-sehJHg5oe2wpyo54vAEg8nzBYc4dFQjFqSOXQcu70WUSzLA8RbkLqKhB5e5AMErSPWC1C_TbsUKZA56aGhqTFhd6U4fhPPtVgRyuYMv9Uib4ZRF6IJyZ563-6i5DLshD05U0Z5cOPHq--mjkl0k_SZ_h50I0vvdOSHYarYQAGghzmI245ncMbBq9F0tVOLzE9NF6VdYy6xOViFS_H2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ
:
ایران به طور کامل در حال فروپاشی است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70512" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98f13e516e.mp4?token=jOkB14tUhcDOdge0yZ9xl2qKQD6bwEXetED2CimHhWWacukN2oDXwGBnwSgWKld0UOONRuUhvpMric03HnRAAGXoRS23bIGhx8E5HNYvPat2tdLjnfLGUeMR-meoXXXZWi8mWiaSsUi2hsVROsQOaZIpTdkXZJUHDesPHghqlC1ZDb2bAjQXX4U2qJ11C1PfvbLFf70HTOb00CkPHkYsGB4pzKurfS4eFNwYhSzD-prNtfbq9SRseFSVXNK96t9dHJdFJSuY4bIv2FFTWif4cJXFcao4x6cVzWQRGh7jM11ZR-MZO_Cmc6iXNZFOL8GstN1AGGOOeFvpg8ZJ3UmcPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98f13e516e.mp4?token=jOkB14tUhcDOdge0yZ9xl2qKQD6bwEXetED2CimHhWWacukN2oDXwGBnwSgWKld0UOONRuUhvpMric03HnRAAGXoRS23bIGhx8E5HNYvPat2tdLjnfLGUeMR-meoXXXZWi8mWiaSsUi2hsVROsQOaZIpTdkXZJUHDesPHghqlC1ZDb2bAjQXX4U2qJ11C1PfvbLFf70HTOb00CkPHkYsGB4pzKurfS4eFNwYhSzD-prNtfbq9SRseFSVXNK96t9dHJdFJSuY4bIv2FFTWif4cJXFcao4x6cVzWQRGh7jM11ZR-MZO_Cmc6iXNZFOL8GstN1AGGOOeFvpg8ZJ3UmcPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه واحد 131 متری تو ولنجکِ تهران :
131 میلیارد تومن
🇫🇷
یه خونه ویلایی استخردار 1080 متری تو فرانسه :
130 میلیارد تومن
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70511" target="_blank">📅 16:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70510">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/685fbb8085.mp4?token=B8Sh5uu39U7KSL7WkucKRF2o7wuEvioXPZvsvhv22oY089YY1cQMGFpV9Ug5CuWsosYTBSg561HnGcGOsniOvQhE0fIF13C2DH40PqAv2dulaQsih_r8JALyCpFEXjGLp7dYl6h5TP-6DQNgcTh17yzPDb8RfKPxx6Fy08BgE5vyRRnZiB1BZdiue5kiT-HDZqk_M3C4_7UT19qKH3xZEUpyukxESu6BPCVlu8oPRcRl5UM33gLzF-cXAjIvoA2RDblTThC4VUkhLuElKFIdO8dRjYsAPVBdc-53kYnqRUSurv1cI4vXJOTFYbfmcMmCPn8JOEsUcpfpp0BgfhMrUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/685fbb8085.mp4?token=B8Sh5uu39U7KSL7WkucKRF2o7wuEvioXPZvsvhv22oY089YY1cQMGFpV9Ug5CuWsosYTBSg561HnGcGOsniOvQhE0fIF13C2DH40PqAv2dulaQsih_r8JALyCpFEXjGLp7dYl6h5TP-6DQNgcTh17yzPDb8RfKPxx6Fy08BgE5vyRRnZiB1BZdiue5kiT-HDZqk_M3C4_7UT19qKH3xZEUpyukxESu6BPCVlu8oPRcRl5UM33gLzF-cXAjIvoA2RDblTThC4VUkhLuElKFIdO8dRjYsAPVBdc-53kYnqRUSurv1cI4vXJOTFYbfmcMmCPn8JOEsUcpfpp0BgfhMrUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
ما از قدیم شطرنج باز بوده‌ایم، در سال‌های اخیر پوکر باز هم شده‌ایم.
الان هم مدتی‌ است که ترکیبی بازی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70510" target="_blank">📅 15:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YauQOdCp_miDMQEJJyV9B9Gcf7_mHvBqtYF-EolaEN9UL6Yug59ozKXlQVCnPsFS8HwtE7RuHQAeNmIC9YbzNPFZmJKpB-yTjx_XPEOBZyX-UkaxU--c9oromU4mMRYOdFyuo9sCIeYUu7B9YfgEnv-IGPXLbxcTtg3oPS3roLzA7VVpQIu5Nb6cVHIMY5z4nmM5vHWWBtur_zbFvGH41CS9u4JS7NVOhSsc3WyXgAjl_SiNzUq56qCsxrwJW6J6gsN8Z0IniURf1gifuqYdZ-RMjIGfvNtHW0SgZ6a_zyd2mLQJUfSSRCuS8wAu6fWSX2U4s1wm2VKkq4rbsiPk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇷
ترامپ در تروث؛از قول رئیس مجلس ایران: «گرسنه‌ایم، نمی‌توانیم دوام بیاوریم»  @News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70509" target="_blank">📅 14:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70507">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ4Bja5KlDMIdb7ajcG_Qf6E1zvs0GwCbbq-5N3RwY7HbOdNmkDyRkWGxCCNF2S6TmC4TF4MSzgisrT_IO_f1Gt7uwzP7bYorGwTF42JDoQXveq8mP4AR1hbSKy-G3wXVUwwiyg7zirkgXk6VH40se4hQ872k5320t6GKVmSnMi1A7Bey0ZAcD_kYY3UInE9x9CcdOaGHkkLRPsCKTofJrYH6WIFqzGa37Oz5m5A8wn-Ovycgl_DIOIeokBMdtY4d99flrQbPTJFEW1NWC5DFxF2olrxOBlS5LX1QK8-HJqJsVQHRmqc_PPRjj30HxD1eGC-JiqwW3bYi-wD5pwQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7684c0f69a.mp4?token=h96clbO7rRiN5BodhqicgLk-Bnh1ciE7SVDGxhbbpOOfQED9iAPj9EpCA_VOBEkay1wwnNkk3NcvgRLM0gZ6JLWYqxUG3CJCn77PQ8HXx7GLbddeI3YRm1m1a2Au1_t1s3TR1beFDjODusw9Pl273cRHMD98_HtmlM9KVD05NvoijK6kcLLnVLci8oPcCuOif3OmaK4FwL3CAY8vPxkQEjW4QQHX2812IOL9nzqSgUdXWZFUnzy8gG6XCYDfhLZnaM5YVVs3caPqCeIYmAT6Vk5EUXhMgixRRX6gVYWdkVxszvdNK01wk6M4jwUBVTIP9P0zE5jUmT_DWf88qOST4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7684c0f69a.mp4?token=h96clbO7rRiN5BodhqicgLk-Bnh1ciE7SVDGxhbbpOOfQED9iAPj9EpCA_VOBEkay1wwnNkk3NcvgRLM0gZ6JLWYqxUG3CJCn77PQ8HXx7GLbddeI3YRm1m1a2Au1_t1s3TR1beFDjODusw9Pl273cRHMD98_HtmlM9KVD05NvoijK6kcLLnVLci8oPcCuOif3OmaK4FwL3CAY8vPxkQEjW4QQHX2812IOL9nzqSgUdXWZFUnzy8gG6XCYDfhLZnaM5YVVs3caPqCeIYmAT6Vk5EUXhMgixRRX6gVYWdkVxszvdNK01wk6M4jwUBVTIP9P0zE5jUmT_DWf88qOST4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💲
❤️
ثابت نگه داشتن قیمت دلار درطول ۲۶ سال حکمرانی شاهنشاه فقید ایران
💵
قیمت‌دلار
زمانیکه تحویل گرفتند: ۷۰ ریال
امروز بیش از ۲/۰۰۰/۰۰۰ ریال
یعنی ۲۸/۵۷۱ برابر!)
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70507" target="_blank">📅 14:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70506">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3317e927b3.mp4?token=inIryZjyR57KgQHTwDuU1PE2c43Jurp2c0-WAG3AnPT5fSSP5_2DJetjqW5e5ddHMqBf_XEyMIl-tlo-56FQ31FFM5lCCP07BG5SNSUYJKIFggXiVrDXfKds2el1n9m00S3XptPnXgFsLWL1W-fWQN1Vo-_waFvQ0T8282StkTWlWE0PqcbttYbGu8Rjscpr_Gh172Zkb3CHp4zLVRwQ1hmPmwPMtn3SufNjsJfD5dBIRPf9_hHsX3U17QkfigOnJk7NHdK0fnzUs9I7xm4WiG37td7puWXQp8mf6bUmJyOIUnzh-Lsc9ss8i3-HIK9PCJz_4hZXxyCSg5WP-mp7SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3317e927b3.mp4?token=inIryZjyR57KgQHTwDuU1PE2c43Jurp2c0-WAG3AnPT5fSSP5_2DJetjqW5e5ddHMqBf_XEyMIl-tlo-56FQ31FFM5lCCP07BG5SNSUYJKIFggXiVrDXfKds2el1n9m00S3XptPnXgFsLWL1W-fWQN1Vo-_waFvQ0T8282StkTWlWE0PqcbttYbGu8Rjscpr_Gh172Zkb3CHp4zLVRwQ1hmPmwPMtn3SufNjsJfD5dBIRPf9_hHsX3U17QkfigOnJk7NHdK0fnzUs9I7xm4WiG37td7puWXQp8mf6bUmJyOIUnzh-Lsc9ss8i3-HIK9PCJz_4hZXxyCSg5WP-mp7SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدحسین عادلی، رئیس اسبق بانک مرکزی و دیپلمات سابق:
بر فرض که در آمریکا، صف بنزین تشکیل شود، چی گیر شما می‌آید؟
اگر فکر می‌کنید در آمریکا صف بنزین تشکیل می‌شود، باید بگویم که نمی‌شود
چه خواسته‌ای داریم غیر از موارد موجود در یادداشت تفاهم؟ کاخ سفید را حسینیه کنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70506" target="_blank">📅 13:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70505">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4e1f5587.mp4?token=Gn7Pt6VeYRD_RtFABQ4hgf2VnEyeoyXy2M05bFKaqOUdCyckU0IDOWF8yvKXf2SyXZgASt6pnj2B57xWR2kb3shn6wFrhHQSztRGDIXlUtqh12fog--YLadHWGuGDl-KhpuhiONwisFJdJgzBC83UCht1MMRVlfGBaU4WE-TmoVmURJMFVcIpsjK_0MCPxtPFUjRwiEjwAmKAW8505uD_JLs3onMzEYRRu7iY5Kxn8BvjJhOKz1A9PXsseDfzlMhbmi_V5wQhWbiR2Wb-NrkY3ZwmXaIoIIiU2B7METVeMdqXt76kQrxWSQkIZ_D16HUXI9Nt24RO5qv_EnzVtonDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4e1f5587.mp4?token=Gn7Pt6VeYRD_RtFABQ4hgf2VnEyeoyXy2M05bFKaqOUdCyckU0IDOWF8yvKXf2SyXZgASt6pnj2B57xWR2kb3shn6wFrhHQSztRGDIXlUtqh12fog--YLadHWGuGDl-KhpuhiONwisFJdJgzBC83UCht1MMRVlfGBaU4WE-TmoVmURJMFVcIpsjK_0MCPxtPFUjRwiEjwAmKAW8505uD_JLs3onMzEYRRu7iY5Kxn8BvjJhOKz1A9PXsseDfzlMhbmi_V5wQhWbiR2Wb-NrkY3ZwmXaIoIIiU2B7METVeMdqXt76kQrxWSQkIZ_D16HUXI9Nt24RO5qv_EnzVtonDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو از کنترل خارق‌العاده با سر و گیتار زدن تو ارتفاع دو جوان ایرانی، حسابی تو فضای مجازیِ وطنی و خارجی وایرال‌ شده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70505" target="_blank">📅 13:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70504">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⏺
🇮🇷
🇵🇰
تسنیم:
عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشور وارد تهران شد.
عاصم منیر پیش از سفر به تهران با ترامپ رئیس جمهور آمریکا گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70504" target="_blank">📅 12:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70503">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d7db3b25.mp4?token=FGnlA_jY875_nOqYtDmA2gB3x2M92mSLjIovwNbj5PcRT8ztiGaE5U36PUdXGlGSK9ZfjPWN9gCjHUXzuqEMUN-R2t0lrS7xyXLSqun6XlpzR3JB798_Gv0U6D991qFECLqUs2T958xax7mRLZvhOIh0B1sidqC3o5X9T1qj7KxQag8shw_k2y5g3ZLIoxK-v3nWSFksg6h-45MGa0Md72maZ0kxa5kFC7UuSN9vLGbG8T4rHcceS9qkvPVENJtVFM6venUBWQK0pmXnd-Eg1wThPkWBqxruUJNEpgzB6Kbf1XxfyeqOOTk_7AqSMu8lSPRl_PKtATlcSO8ef-oHUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d7db3b25.mp4?token=FGnlA_jY875_nOqYtDmA2gB3x2M92mSLjIovwNbj5PcRT8ztiGaE5U36PUdXGlGSK9ZfjPWN9gCjHUXzuqEMUN-R2t0lrS7xyXLSqun6XlpzR3JB798_Gv0U6D991qFECLqUs2T958xax7mRLZvhOIh0B1sidqC3o5X9T1qj7KxQag8shw_k2y5g3ZLIoxK-v3nWSFksg6h-45MGa0Md72maZ0kxa5kFC7UuSN9vLGbG8T4rHcceS9qkvPVENJtVFM6venUBWQK0pmXnd-Eg1wThPkWBqxruUJNEpgzB6Kbf1XxfyeqOOTk_7AqSMu8lSPRl_PKtATlcSO8ef-oHUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی نزدیک از ظاهر موشک تاد و پاتریوت؛
موشک THAAD: طول ۶.۲ متر | قطر ۴۰ سانتی‌متر | وزن ۶۶۲ کیلوگرم | سرعت بیش از ۸.۲۴ ماخ | ارتفاع درگیری: ۱۵۰ کیلومتر| ارتفاع درگیری داخل و خارج جو | پیشران سوخت جامد | روش انهدام Hit-to-Kill | هدف: موشک‌های بالستیک.
موشک Patriot PAC-3 MSE: طول حدود ۵.۲ متر | قطر حدود ۲۵ سانتی‌متر | وزن حدود ۳۱۲ کیلوگرم | سرعت: ۵ ماخ | ارتفاع درگیری ۴۰ کیلومتر | پیشران سوخت جامد دوپالسه | روش انهدام Hit-to-Kill | هدف: موشک‌های بالستیک، کروز و هواگردها.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70503" target="_blank">📅 11:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70502">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7ee8a017.mp4?token=RjCA3v9xzo-fmjHNZIGGF2dNMXqD4pr55rJA9iKNLXmZQ819hyHt7nwy1fW9nyTGcJmojkoi5DKi_lC2e8LpPqq92KyoTZyvpV5LFs86autWx3W49husMf0MXyrBP09vOpQFzazs7sIZKLL0tDogNa2ihMIgN7eYVukuvZ2yOVAvxUm6lb7JCCmIrY_7D1X5wxA4G6LYl1SPrFBVp-3NPwFzWGn6tcaK4KBidb4mYA1NK0pqpe36TRFNGpjP_2ArChnL3cL3wKNO61RHIViF2kem5DIymp4E0NTZcdIBYltv0y3gyLkuRfE1wVKQ2tA5PSkwVqNYGbE8dzMTSA3KUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7ee8a017.mp4?token=RjCA3v9xzo-fmjHNZIGGF2dNMXqD4pr55rJA9iKNLXmZQ819hyHt7nwy1fW9nyTGcJmojkoi5DKi_lC2e8LpPqq92KyoTZyvpV5LFs86autWx3W49husMf0MXyrBP09vOpQFzazs7sIZKLL0tDogNa2ihMIgN7eYVukuvZ2yOVAvxUm6lb7JCCmIrY_7D1X5wxA4G6LYl1SPrFBVp-3NPwFzWGn6tcaK4KBidb4mYA1NK0pqpe36TRFNGpjP_2ArChnL3cL3wKNO61RHIViF2kem5DIymp4E0NTZcdIBYltv0y3gyLkuRfE1wVKQ2tA5PSkwVqNYGbE8dzMTSA3KUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محیایی، معاون هماهنگی امور عمرانی استانداری گلستان:
تو استان‌های خراسان شمالی، مازندران و گلستان توی فصل سرما، قطعا بین 60 تا 90 روز قطعی گاز داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70502" target="_blank">📅 11:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70501">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70501" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70501" target="_blank">📅 11:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70500">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4cZoJeULczr-We9Tg-yyau_sM0Iiv6PuUCFMykSXOFJJj9BMMnopEz598lnkeH05qino0c4NoEbPk-lM0LJsrXOgL6SV9LctzsE3SupcZR8MRyGcUZSx9B-e1SRpYPCjsOH8-JE65KsTJ7JP8lswqe1r1rkU8uP3L6oIYaFiBfbGn-_OonjKmSwovzy8Nmjd0v4tXiMKxfrVXMQGJYkSv7pIQ1OPMQ5hJR96n_WpkEdfjDZYugYoJLK3zS5-aUv5c_gXPF5eCHR64XHcRagZ31N7YiUU7TT4gKNY0rfpQGyxYoiNt7Ufcb1U-I7slVsvK7lRLBFk7ZaXMebe-Ug_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r2
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70500" target="_blank">📅 11:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70499">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqsLJ37PtDC-GBjyxdTjOxK02dOEWbtpV-ZxjkDRuL5qYMOYWMWFFhoXsBaOG-LEg-Apwc4hlXHGkXVjhH7Tss8eDcdQRQHCKNmN_nH8x-0NFA53x5nDp6LX-gd7ITlPzdkPpiDT8Ju1U4v70Nryf-ciS0bbXFBP9mEU_0ttUgTMVxLLa9rwo3N9XZKPrKralx1pRmIv5K18n4q5yor18D7hDeOSKX0h9qbicGOHmVdFrWv2PDWI_kMtltNxUvvLfLft5AbvOqLZIwVSUYdk6N1X07KnYSZxi0dNgLaETuktg2EMm-WGCvTan1B6JZsxqN-IBLAwVrCYbGzzN2ndcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇷
ترامپ در تروث؛از قول رئیس مجلس ایران: «گرسنه‌ایم، نمی‌توانیم دوام بیاوریم»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70499" target="_blank">📅 11:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70496">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hd13LcrSGfZPOqKf2q1ZN-6DHDEuCBej0f8T-iSo8wQEh05JIsDyXcQUk8G7C9IWkywWKeaRps18IamyMmArTwedsq0jARoTASaxOJAtawGbqnEIgu7QEWqE2b8AwdG2wZJR1dDqi2WowRlX00u-eEdCZacjVenaD2Pjs5p63kaRjw6RBou-3umriBlwQKafbnn6f4oXteVjoXxjGg6-bfKgDwf1wnrSFSk2BAWnTzzqiUDydYtljJOYSTl_nMotwHp3o1wYOQCoQ-THigxZFZ_Yd3ekDWkfMHNRt-uoFM5YdOQSSmrEAhcE6xWShoeu3-Joeh-K7ESw_zPUQ2W7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JnHgbZRB58KFZlKLqRfq6FjKmpmA9VKBRsB0Zd1DoUdznwl6AEhRMB04Qhy2ucoVm4pcfCgH5IEptmybtu7XBxaEoMkFxTqo3MfUXFrir1Bga60HoJy_cr61utRgK9kEhjIEg1L7ucMQ-sPSbB0xCPgy94oO76QYv4aFfnH9o8FlyRwurc8f01kJ6Aqb5chud7yc2rplZ5ZmUL18Er68Xfet2XRBJ0cup78EX10cMdOuGh_yHOdR8kKjWdvNMJll66PJJeFfZWrYcj9o3nuxgqa64F06I2XNsTQZiPILO_rRQsgc99A54TYTpImXkCrSSN5PlyJbP4xwrfX-5MwIzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73af71539f.mp4?token=TE2FwA6Y2RI5-g_GFX48N1mWcWo9gbXE1TJwgMfNDi8x87_q6WGszdVU1NUpBiQrKVMEUqrRVdXHfmyr2WACANBnTZxKaYIy0x-ad_ergwZOU_svJ9hv1qu_wU9IpHnoOH6l3ZaewdCQd5T0Ru2SZFeTnbt6ELpLZQ3x6QsCppkHL7857lz92V6rg7---UwQ_nN6qgcOWM2ykXJsKx-pj505OgGVMrh6vXjW4X4wUDX4KAUd3UmG4spUtH5fCoG2zn9vYENRl7sR8TOCZwOsMpEcDHD1LM_KwsOJYgozADzvWO-P0ukHNVOgexv2Rk5tczlskNQiZCJD55zxc1H78w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73af71539f.mp4?token=TE2FwA6Y2RI5-g_GFX48N1mWcWo9gbXE1TJwgMfNDi8x87_q6WGszdVU1NUpBiQrKVMEUqrRVdXHfmyr2WACANBnTZxKaYIy0x-ad_ergwZOU_svJ9hv1qu_wU9IpHnoOH6l3ZaewdCQd5T0Ru2SZFeTnbt6ELpLZQ3x6QsCppkHL7857lz92V6rg7---UwQ_nN6qgcOWM2ykXJsKx-pj505OgGVMrh6vXjW4X4wUDX4KAUd3UmG4spUtH5fCoG2zn9vYENRl7sR8TOCZwOsMpEcDHD1LM_KwsOJYgozADzvWO-P0ukHNVOgexv2Rk5tczlskNQiZCJD55zxc1H78w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوالات کنکور زبان امسال رو بردن گذاشتن جلوی یه آمریکاییِ باسواد؛
طرف پشماش ریخته که اگه اینا به زبون ماست، چرا من نشنیدمشون تاحالا؟
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70496" target="_blank">📅 11:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70495">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⏺
📰
ایران اینترنشنال:
قیمت دلار در حالی از ۲۰۰ هزار تومان گذشت که پزشکیان گفت کشور در وضعیت جنگی تمام‌عیار قرار گرفته. همزمان، محسن رضایی به نمایندگی از مجتبی خامنه‌ای کشورهای منطقه را تهدید کرد در صورت همراهی با آمریکا در جنگ اقتصادی علیه تهران، هدف حمله قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70495" target="_blank">📅 10:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70494">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c05438d58.mp4?token=cWHSyFac67h3QOcMb_48f2BGwCbMQZlqbXCo-_F7gpi0rtwVwqv4cLNecUCtacApfl6q0KKGWtHdXXbfjIrwSfnqr2fYGq94O6Bmhq4C750aAQtMbVvymuQrvZWuxa0P9kgfpuhGG7HqTRs6B4pAWRD_-h2KgpNq_TiMAX3m5VkxZMr9IbcLYS1lfPZPTD8irikXlVfUQWr2Y6S_BgNx4Sx_SbWjWdHbAB_TjZw1zli8Zb6egJuozVOZCjYcrdLVKw0TJwM0PvqA-3YRA4HWKjP5tyuqxrTSngtBKFwGnme4U47g2w2lqf0fxoLMKBeOIhjO6-PxjZ-Qwhg6NwpCuUEhMbraN3ec9IlhIW8i_4Ufb20Bcvl46Qv-hBbZmSGbz4LMZu2uNZ-vNgMjCda7_D0MC5LI_FpipVU_y1Cb6M7hNA2b3jPo2SeY-2El1LjArf0gFiOTruMi0iOYH18R-UdX_dPTSVNyhXRnCDWTQuUDhgRwwXqb-E_uKNucVo31q90Kf8LVg8zSti1WLgSxQGcHXAM5NMv4QwEPUQgvPMZanMYCZjUAdtc2g6e98d9Z648evliC9afnyWHIEpkDjNwq4lJDb_1X_1e8doPjHP_Reqg9JPizMyo-LjxI5euoSTF3-y_DfWDDHJxH-ERL6_8ymg1kbx1_E37B4qPng_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c05438d58.mp4?token=cWHSyFac67h3QOcMb_48f2BGwCbMQZlqbXCo-_F7gpi0rtwVwqv4cLNecUCtacApfl6q0KKGWtHdXXbfjIrwSfnqr2fYGq94O6Bmhq4C750aAQtMbVvymuQrvZWuxa0P9kgfpuhGG7HqTRs6B4pAWRD_-h2KgpNq_TiMAX3m5VkxZMr9IbcLYS1lfPZPTD8irikXlVfUQWr2Y6S_BgNx4Sx_SbWjWdHbAB_TjZw1zli8Zb6egJuozVOZCjYcrdLVKw0TJwM0PvqA-3YRA4HWKjP5tyuqxrTSngtBKFwGnme4U47g2w2lqf0fxoLMKBeOIhjO6-PxjZ-Qwhg6NwpCuUEhMbraN3ec9IlhIW8i_4Ufb20Bcvl46Qv-hBbZmSGbz4LMZu2uNZ-vNgMjCda7_D0MC5LI_FpipVU_y1Cb6M7hNA2b3jPo2SeY-2El1LjArf0gFiOTruMi0iOYH18R-UdX_dPTSVNyhXRnCDWTQuUDhgRwwXqb-E_uKNucVo31q90Kf8LVg8zSti1WLgSxQGcHXAM5NMv4QwEPUQgvPMZanMYCZjUAdtc2g6e98d9Z648evliC9afnyWHIEpkDjNwq4lJDb_1X_1e8doPjHP_Reqg9JPizMyo-LjxI5euoSTF3-y_DfWDDHJxH-ERL6_8ymg1kbx1_E37B4qPng_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدئوی وایرال شده از دعوایی که  تو گیلان رخ داده؛
یه مرده به بهونه‌ی دفاع از زنش، دو خانم دیگه رو کتک میزنه
!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70494" target="_blank">📅 10:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70492">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536dc396b0.mp4?token=vE1icGXAoGLR9Aa9Ksx3Hi4acZvZDMz70_1SQUffz6PJcLHkQ9hWrzFkzs8WnUQaOn4OLDHsWu8xZXNgbhPM7-g2UC39cnew8amgRv2d4o5wkbYEjUS_ZBepjWfm0WIwKmRZPWh1MQbH4wFGx0FXHd-5OlU0QwNiTqZljNiZHr2H3IDdMr8OsFEZF1dfuwI5KabUEOFK8gv4Q2Bq3vzfl2vfB8MsaTfj9T_j80h_JXYhfIEbnTtm8bZ2W-NKHdn48LLsYaRRywn1WqUvCmtmUEQ7s29XMJfcNRSo1iEXthzbQAt6ofOVqKs3Y0ZbPz9lw9ke7D6iWFHK_32iLrW2DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536dc396b0.mp4?token=vE1icGXAoGLR9Aa9Ksx3Hi4acZvZDMz70_1SQUffz6PJcLHkQ9hWrzFkzs8WnUQaOn4OLDHsWu8xZXNgbhPM7-g2UC39cnew8amgRv2d4o5wkbYEjUS_ZBepjWfm0WIwKmRZPWh1MQbH4wFGx0FXHd-5OlU0QwNiTqZljNiZHr2H3IDdMr8OsFEZF1dfuwI5KabUEOFK8gv4Q2Bq3vzfl2vfB8MsaTfj9T_j80h_JXYhfIEbnTtm8bZ2W-NKHdn48LLsYaRRywn1WqUvCmtmUEQ7s29XMJfcNRSo1iEXthzbQAt6ofOVqKs3Y0ZbPz9lw9ke7D6iWFHK_32iLrW2DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
هلیکوپترهای CH-47 شینوک، UH-60 بلک هاوک و AH-64 آپاچی ارتش آمریکا، در کنار AH-1Z وایپر تفنگداران دریایی آمریکا، در یک نمایش هوایی ویژه مسابقات Freedom 250 Grand Prix در واشنگتن دی‌سی به پرواز درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70492" target="_blank">📅 09:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70491">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6f5402ef.mp4?token=toQuB00GGJ4eaAubCDJawNsByQqky-W4nhZelOFrFL0UwmjMtEZQ1YIl2kpLmtYTjmyHIWoyKl9bNoVyOLpcQ_jT0DOsYEQgC5uVNu2A7zfAhWdvUL8y0JFnQDrjB6A6G0wTng1WHCmESW7RIZ4fUGZ1XleDa4HZmk1UJ3Milx_LKJ-UtNBCKC0GV7uzXlMH-WNN-7cRpFhWIqGbgXshsWksbKZpEtnBgJeJnYBb0KNeSi9DJcVNy7mVIyK-0hTFPKqI1j3fLB9l7bsxZEcxU0N9O5O5JNz3yid5HjKObu2ROZiWHG0QL7gW2Q27Yf58PjE8LAmAUG8kwwwquTMwIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6f5402ef.mp4?token=toQuB00GGJ4eaAubCDJawNsByQqky-W4nhZelOFrFL0UwmjMtEZQ1YIl2kpLmtYTjmyHIWoyKl9bNoVyOLpcQ_jT0DOsYEQgC5uVNu2A7zfAhWdvUL8y0JFnQDrjB6A6G0wTng1WHCmESW7RIZ4fUGZ1XleDa4HZmk1UJ3Milx_LKJ-UtNBCKC0GV7uzXlMH-WNN-7cRpFhWIqGbgXshsWksbKZpEtnBgJeJnYBb0KNeSi9DJcVNy7mVIyK-0hTFPKqI1j3fLB9l7bsxZEcxU0N9O5O5JNz3yid5HjKObu2ROZiWHG0QL7gW2Q27Yf58PjE8LAmAUG8kwwwquTMwIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
متکی، نماینده مجلس:
۹۰ روز آینده روز‌های بسیار مهمی هستن، ترامپ ایران رو مشغول تفاهم اسلام آباد کرد تا انتخابات میان دوره رو پیروز بشه و بعدش قراره تازه بیاد سراغ ما.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70491" target="_blank">📅 09:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70490">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70490" target="_blank">📅 02:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70489">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6kykairQVd_e2Zla4TiK-AB1T6nH1pH4KsCpdfARJa7K8BbYkzc-v7UG12fE8yWcUvjFVvBYw3Nq3M5IYPfdW5zrPyTEJLpEWzb9UluVkzNSX4RN0nEnCCv8Y7TeDEL2rVen2hnHE3Zs-O9WZig1kEY-Mlj0iH1zGZnrzrlME8EdRHOywyha8h82ks2oVWMTXiEeQhNKBadxaiKWgIzaP7aXJ_noIO1zdwyXLzYv6jqepFCdc5xHjhVO7RIwQ1hhJo2NX5q_1RQsaCVS79ekrORSS_wTmE2ZK0WNC1iT14v3EpdRywodI-GZ5E4r557yu5UOrmDyaGtpe8A9Ollqfm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6kykairQVd_e2Zla4TiK-AB1T6nH1pH4KsCpdfARJa7K8BbYkzc-v7UG12fE8yWcUvjFVvBYw3Nq3M5IYPfdW5zrPyTEJLpEWzb9UluVkzNSX4RN0nEnCCv8Y7TeDEL2rVen2hnHE3Zs-O9WZig1kEY-Mlj0iH1zGZnrzrlME8EdRHOywyha8h82ks2oVWMTXiEeQhNKBadxaiKWgIzaP7aXJ_noIO1zdwyXLzYv6jqepFCdc5xHjhVO7RIwQ1hhJo2NX5q_1RQsaCVS79ekrORSS_wTmE2ZK0WNC1iT14v3EpdRywodI-GZ5E4r557yu5UOrmDyaGtpe8A9Ollqfm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
a1
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70489" target="_blank">📅 02:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70488">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛وزیر خزانه‌داری آمریکا، اسکات بسنت:
«ایالات متحده در حال آغاز بزرگ‌ترین تهاجم مالی‌ای است که تاکنون علیه یک دشمن به کار گرفته شده است.»
او هشدار داده کشورهایی که به تجارت با ایران ادامه دهند، به «منفوران در عرصه جهانی» تبدیل خواهند شد.
🔴
به نظر می‌رسد فردا روز مهمی خواهد بود…
بسنت آغاز فشار اقتصادی جدید علیه ایران را به «D-Day اقتصادی» تشبیه کرده است.
هدف آمریکا، به گفته او، قطع شریان‌های مالی و تجاری ایران و منزوی کردن اقتصاد کشور است.
او به کشورهایی که با ایران تجارت می‌کنند، نفت ایران را می‌خرند یا در انتقال پول آن نقش دارند، هشدار به اعمال فشار و تحریم داده است.
بسنت معتقد است فشار اقتصادی می‌تواند حکومت ایران را وادار به تغییر رفتار کند.
او همچنین هشدار داده اگر ایران به نیروهای آمریکایی یا کشورهای خلیج فارس حمله کند، پاسخ آمریکا سریع و قاطع خواهد بود.
هدف این تهاجم اقتصادی وادار کردن رژیم به فروپاشی یا تسلیم در برابر فشار است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70488" target="_blank">📅 02:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70485">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f407bb9f5.mp4?token=urDQLQGVGKlJ9T4Gt9F2s1n0Xo4QC7kIc-VagNKA23Z46pLZFCQT1NhYTp9-oiY9o1tTvZ3nQ9O8HQtx01f_Vfmtoj3tsyhZWHpq_Pc_51hjuYfxuEDE4z55qdk9iZ3U1bvV3ZHvNbT47PgdpCF4GBqz71xqg-zo_TzYlngpuXx05Gfk6bO-zFzm0ROCXO47xONciaTrwielMD-LQrYRRjACgcdy7EDhoy3mDq_GCQ4cLq8kNBGy-LvT90Rpzkw4ED9Fd2o5JCiYGa4yiMUHfbB0ka1CoWvatuy44MKJPR81PzhlbpP-PD7OlG72UMLdJd74OOw4u97hUfBvFdY3AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f407bb9f5.mp4?token=urDQLQGVGKlJ9T4Gt9F2s1n0Xo4QC7kIc-VagNKA23Z46pLZFCQT1NhYTp9-oiY9o1tTvZ3nQ9O8HQtx01f_Vfmtoj3tsyhZWHpq_Pc_51hjuYfxuEDE4z55qdk9iZ3U1bvV3ZHvNbT47PgdpCF4GBqz71xqg-zo_TzYlngpuXx05Gfk6bO-zFzm0ROCXO47xONciaTrwielMD-LQrYRRjACgcdy7EDhoy3mDq_GCQ4cLq8kNBGy-LvT90Rpzkw4ED9Fd2o5JCiYGa4yiMUHfbB0ka1CoWvatuy44MKJPR81PzhlbpP-PD7OlG72UMLdJd74OOw4u97hUfBvFdY3AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
راغفر :
رئیس جمهور مطرح کرد
گران کردیم که مردم نتوانند بخرند و اینگونه مانع قحطی می‌شویم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70485" target="_blank">📅 00:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dzypo_AEBjzp00V6_B2LfioIKdJkHW5-Xdt3OMHIYu8W_ITYGsooKNRZ2FXRBmdDKipgWNPXzSVP7TPXbvndFPKznKdObc0BWbTPGyj0lliHSIa3MVcNi-FbtrTkGaI7pwc368eu06qEGmunIUgZFav8EyDsBI8ELNh86VgX9CO820nkepEmueNu0DlO4GqE-cHoWSkCYpdz9mPK2O9M4mMou7F5eyGMwocgxf5465dKTn7Sz--CTu-viP4Ct2p780PMIrDFjMcMWOid3fc7pm-gS-S2Xi2btxjncRQneJAptkMISZnEaBRCAquVxK6LPN7cgDX7p-_gd_6RgT_pGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0qSSGnwhIldDUobYIcCOc1UhVvsHpXakb8oZn51DcZKmi5MO1XuY1m4ZdJcZbKi51d5bC60iT0v9u75Relp-if4F9twVwm2C8Tgi1yem5KgEWd_HKB0IdNYzcLLlS4UtDX1rBIoiRbLdh5bXo0H6ytqIkFWJuEizij50QvOkQM1flmytiQgfk_p2dmcPfVJEZ5Krwbk6nuTl1PhMcxfQeHF9VagZwYMVwxFjrnax1E1Yf8IN12YJTzNBvOxnQ07T4VKu6OjF-xDPibcG5gVNxtranZ8EFDgIxAHD2eoHcc-VX4DWW2ZwFQZZliSM3N8oYOPuCC-IQ6AdgCIZ_To_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی امروز صبح منطقه آرخانگلسک در روسیه را مورد حمله قرار دادند. این منطقه در فاصله ۱۸۰۰ تا ۱۹۰۰ کیلومتری مرز اوکراین واقع شده است و این اولین باری است که پهپادها به این منطقه دسترسی پیدا می‌کنند.
بر اساس گزارش‌های اولیه، پایگاه فضایی پلستسک هدف این حمله قرار گرفته است. پلستسک یکی از مهم‌ترین پایگاه‌های فضایی نظامی روسیه است که از پرتاب ماهواره‌های نظامی، آزمایش موشک‌های بالستیک بین قاره‌ای و سایر عملیات‌های فضایی استراتژیک پشتیبانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70482" target="_blank">📅 23:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d033a4797c.mp4?token=ajFbR5v6Lr8yOSDb8SHZnl8gH6kEfzM8qeRHIxsGU4VivveKN-jQjy8MlVhVXYdpZEfuWVQMZmmEUmVpU_1v5hVCWP1gUipzqFz5m1v9HDk1pTk4IO98LrwWZ7RgtEfnrXiJahId27iluEOLhUn_SqLBwI7fLuqVJ70tXMngjf-FHAw4ZouXj2Nrf7dPvy66HJFEeWlBE7wu3ssLY9RGH1sOULlzu1uJGln_VmJ5hhDcUqU8NZoPZVAUHSFHxFaVUmauwZ_f-l0n4VF1XhrksQVuy11_rSWHDsKg-JyKMtPN3l-Ej6dpqNJganh7Fx8wb7EqCvC6hOUay7l2uKwjTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d033a4797c.mp4?token=ajFbR5v6Lr8yOSDb8SHZnl8gH6kEfzM8qeRHIxsGU4VivveKN-jQjy8MlVhVXYdpZEfuWVQMZmmEUmVpU_1v5hVCWP1gUipzqFz5m1v9HDk1pTk4IO98LrwWZ7RgtEfnrXiJahId27iluEOLhUn_SqLBwI7fLuqVJ70tXMngjf-FHAw4ZouXj2Nrf7dPvy66HJFEeWlBE7wu3ssLY9RGH1sOULlzu1uJGln_VmJ5hhDcUqU8NZoPZVAUHSFHxFaVUmauwZ_f-l0n4VF1XhrksQVuy11_rSWHDsKg-JyKMtPN3l-Ej6dpqNJganh7Fx8wb7EqCvC6hOUay7l2uKwjTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رئیس دفتر پزشکیان:
قرار است جانفداها به سراغ ۵ میلیون مشترک پرمصرف برق بروند و بگویند صرفه‌جویی کنن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70481" target="_blank">📅 23:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZoRWPl6YyhNjxmzoC01EUxcJhE69N3cZTH0NmjfT2D4ABFZbSPJi1PdmGRmq84n8taEGkp593MbOLRAjO4Wzi2qS_vqkb741gy0laENTbh0iczcTkfnQoko3raW6F780FHTNXajMI7KSUB8cGBI3fQuse3qk7voTBCbpduw84l1GOInAiC-bYzA5hklDb0fyoU8GQCAYXOPGFKhT_BjIMX2m_N2Y3xHTwdECeL_VoDP8fgc3pbaOMnyOCC45y9z5izuN6JbLpymXC1SjQjOlT_aYGxfEMJvvuGTXsotCKcchz1apKvbULzP2inuF_7ZypPuQ3d2tTWT6Tvv9AaiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی:
اگر جنگ اقتصادی ادامه یابد، حتی یک قطره نفت صادر نخواهد شد؛ نه از طریق تنگه هرمز و نه از هیچ نقطه دیگری در خلیج فارس.
ایران مشارکت یا حمایت هر کشوری از جنگ اقتصادی آمریکا علیه ملت ایران را به منزله اقدام جنگی تلقی خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70480" target="_blank">📅 23:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wB177cSs3hdawusfwQphPN8TXcK1H4kkj_gZ6NWyrHXXEtT0PXXi9eOG9h1MAWn9K4_6X4j1HGGLvWXGVjyVUPUHTVg97oImgHyNcL6z9hPUfzPHSByuzKRK-KlLc5jO8WWa-BwgSbf23A6H9OFf4huOiKqHqt8m2mQHBHDdmIOw20iR42fn6vqTTUPRTcBciDPsd-QhzNCJRE93rFu4Y2xtkotH-h9qYX5UueoJjYw_7JQs6YRgG7G8o3WFTSJ1BUztWBIPDbCQWLPLpXyz7rtzP5ZGVGxGfuETWsOlZWrqDn-vS_mWHcRWtQ871GjG2NX7PNYhKappU3hrhE-n0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گسترش فرصت‌های سرمایه‌گذاری در وال‌گلد؛ نقره به میدان آمد!
💎
تنوع، کلید موفقیت در بازارهای مالی است. پلتفرم «وال‌گلد» در گام جدید خود این امکان را فراهم کرده است تا کاربران بتوانند در کنار طلا، روی «نقره» هم سرمایه‌گذاری کنند.
🔸
روند یک سال اخیر نشان می‌دهد نقره بازدهی‌های چشمگیری در بازار سرمایه داشته است.
🔸
با این امکان جدید، سرمایه‌گذاران می‌توانند با ترکیب طلا و نقره، یک سبد مطمئن‌تر، کلاسیک و پربازده بسازند.
ورود به بازار جذاب نقره
ورود به بازار جذاب نقره</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70479" target="_blank">📅 23:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vj26pEQ5lLMd96NdQRbc1BxghQOuZMybVioAHaEhoeEZbJX5SzbDua5RjgGE-E1j_rJj56sxZ2-_FSk34WFczZtfT3OUoVMcFMhfZyNM4W-YXyrAzvrc4QPggPxJ8QuWBF00CcAnkfk4wdOMahEiRtNKDinOAPQgWsBdTAs0DCWeXNy7UhqAbJipt1KVDZWdMCod0wL2m_WJFCJ5gUZ2yBSPPaJYtQkww2bUQRxi-FMTDGcOFT63Ht7b63BHOgtrLdJoAUZkvLpyrwgmfYSIbdw7cF3u38k3p_ZIq03BtI2MbjQWGH3YjYFTBTI8mOI2SillhQWxvj_Q_4K4KLQdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تا ۲۰۰ میلیون وام بگیر فوری!
🔥
‼️
با اسنپ‌پی می‌تونی بدون نیاز به ضامن و فقط با یه برگ چک صیادی تا ۲۰۰ میلیون تومن وام بگیری و تو اقساط بلند مدت تا ۲۴ ماه پرداخت کنی
😎
تا ۶ شهریور ۲۰٪ هم تخفیف اشتراک داری
🤩
پس همین حالا از لینک زیر وامت رو بگیر:
👇🏻
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70478" target="_blank">📅 23:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇷
توقیف و مصادره در انتظار شناورهای متخلف در تنگهٔ هرمز؛
🔴
نهاد مدیریت آبراه خلیج فارس اعلام کرد شناورهایی که از ترتیبات اعلام‌شدهٔ ایران برای تردد از تنگهٔ هرمز تخلف کنند، در ترددهای بعدی با محدودیت‌هایی از جمله جریمه، توقیف یا مصادره مواجه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70477" target="_blank">📅 22:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XeMtH-HzMv_uQ37pX3UVQO5KeHkfXE5sx6FM3eQrrnNpJpF-FUq1poP-MfkfdWIGs139qI3ZszNwgXXh_eZqLOp2LkFTnhz1iY83l1ZnP1VQnitI8Td34uWwB_Pc2XAXGbhD35EnSUG5SK_gAjZefkoXDqafG9QssFQZ4kJ0rfbjlW8Fp5-jslw25DM9-uT84bj6MtnClf13HsKatoDc0cjKkRIQGUAXZ1hsM3zXEzF1-DMg-v1xNAYOEf5r2DdU2Bd8cticTIvaQxsMfVYzA5hWbnjLSkUqJrMNZxqHfgS_PAXHW6VYzVUQQACheYCDqaEmU6zw0R14mxEiXUwA9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجری عراقی با انتشار این تصویر نوشت به این جنجال پایان دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70476" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d44391ebe9.mp4?token=dwRCTUgDc9SkXyk1XVTJW3Rbm8f_doPzpLYXFT5mlG9ZgNrDWiLhKHEvHaryR9mRLUY4MtgyWpSkXJOFFcxQquwPw1i7QvOk9ll9zZ6Wj952Zzf9EVe1STLpbT-O71rtYzQQbQT4ZP18NO19XEHkh5zE469u_wT_H-FqQyKTnInwljAec1hdIVk7i2zXxGgyPkMtGEnVu5xkj9MtglbQ-w88PLsJr88Opof3B7tSO2pQgVV2xvUhkDWhLYG_v6ot8y57vUn_iiLgKqf13TVu7MJ-OU4xvy7ei2t75Am0U75pTort-ulIWCk_S3j5s_kBjcZIJ1RbgC-BN7mMbIdpog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d44391ebe9.mp4?token=dwRCTUgDc9SkXyk1XVTJW3Rbm8f_doPzpLYXFT5mlG9ZgNrDWiLhKHEvHaryR9mRLUY4MtgyWpSkXJOFFcxQquwPw1i7QvOk9ll9zZ6Wj952Zzf9EVe1STLpbT-O71rtYzQQbQT4ZP18NO19XEHkh5zE469u_wT_H-FqQyKTnInwljAec1hdIVk7i2zXxGgyPkMtGEnVu5xkj9MtglbQ-w88PLsJr88Opof3B7tSO2pQgVV2xvUhkDWhLYG_v6ot8y57vUn_iiLgKqf13TVu7MJ-OU4xvy7ei2t75Am0U75pTort-ulIWCk_S3j5s_kBjcZIJ1RbgC-BN7mMbIdpog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سعادت آباد تهران دو تا گروه تیم‌کشی کرده بودن برای دعوا و این شکلی با بیل، چوب، سنگ و هر چی دم دستشون بود، افتاده به جون همدیگه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70475" target="_blank">📅 21:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70473">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30c15be54e.mp4?token=JkiUNSRFwenIHl7c4GZ2y1Vr4dKquVjZjyHHZ-MZKTWic5CMDcmOP0kULKbfEO5Y0XKv-pkJVfvW51rvW293e21-H8ZJs7MIkGpVjaZmlFa4MrzoYV40BFnNQIaCBvucJKh3MLKF-iG1wnwWVxsCy5EAmPSLYYrWqr_NeHa-D32CUmIO9-gsIWqBXk-um_2mtwSABTkkiN7C2idlyLVCreCM9xPxtqzl1yXH_UHNN4EAylLGDIA0RF1zXzHzrgJBW78xui-a-2T8e-SeFdAO8O2I3Rr110IFyEQyjC8ZP1KrHXR-01IrlvN-qiDpiRfXSNDMir3nWSqfR-YHPiQYwjTRmcGN0XcvBbaSLsI20k-v-ridPtKX7GvdDAYqND_EHQ7PwSakBeEStgJNq2MyjygynTwM0vUVln9mTQHtpnSR7f_eVhLktLCE0HODV0UPeOW1qibxWPVerQHgF1Ld77fdqe5TTqUHYombFWrHgfbE8-ZXmxNHFtf2HyJXkUuzRdCeH5owl0sQoa_-ywAZuAAMV3chjhDHLf1NkKN0myAgEIhQw0yyDIQ3qwXhO1mZ9YyG8KCcFLCajqFhEkJ8jo1wweCBu1RsIiH7zbJAX0oZKxyHZE2Y5IBqEanXDCFiqX3cOMAwwz2QY-oo-2X1zAximJC4TKSbvKeFVbTehr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30c15be54e.mp4?token=JkiUNSRFwenIHl7c4GZ2y1Vr4dKquVjZjyHHZ-MZKTWic5CMDcmOP0kULKbfEO5Y0XKv-pkJVfvW51rvW293e21-H8ZJs7MIkGpVjaZmlFa4MrzoYV40BFnNQIaCBvucJKh3MLKF-iG1wnwWVxsCy5EAmPSLYYrWqr_NeHa-D32CUmIO9-gsIWqBXk-um_2mtwSABTkkiN7C2idlyLVCreCM9xPxtqzl1yXH_UHNN4EAylLGDIA0RF1zXzHzrgJBW78xui-a-2T8e-SeFdAO8O2I3Rr110IFyEQyjC8ZP1KrHXR-01IrlvN-qiDpiRfXSNDMir3nWSqfR-YHPiQYwjTRmcGN0XcvBbaSLsI20k-v-ridPtKX7GvdDAYqND_EHQ7PwSakBeEStgJNq2MyjygynTwM0vUVln9mTQHtpnSR7f_eVhLktLCE0HODV0UPeOW1qibxWPVerQHgF1Ld77fdqe5TTqUHYombFWrHgfbE8-ZXmxNHFtf2HyJXkUuzRdCeH5owl0sQoa_-ywAZuAAMV3chjhDHLf1NkKN0myAgEIhQw0yyDIQ3qwXhO1mZ9YyG8KCcFLCajqFhEkJ8jo1wweCBu1RsIiH7zbJAX0oZKxyHZE2Y5IBqEanXDCFiqX3cOMAwwz2QY-oo-2X1zAximJC4TKSbvKeFVbTehr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🇺🇸
هواپیماهای B-1 Lancer، B-2 Spirit و B-52 Stratofortress و چهار فروند جنگنده F-35 نیروی هوایی ایالات متحده، پیش از آغاز مسابقات «گرند پری Freedom 250» در واشنگتن دی‌سی، بر فراز محل مسابقه پرواز کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70473" target="_blank">📅 21:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70472">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63aefba4cc.mp4?token=D66peAK1uWPLljfHd3VZ5Da-3XcmgQ7tHC0mE8v6Kx0ZsOOxaMyZ75f2zal5CXzELA2vTM1eDQnOtxNsuFTc3cB8PBMprRQNHRvplRim2p4uiA0aon-ccjFJYN2H2bSUc1_YZ2Wxx8wfZtdP0TeFXCvryKkBV5TGu5oh58Lqj09W3SsOL3HPCo-OlWudoL1H0tu6SX6ch9xD9PbSuQVUmDirrGiNftX7qY1s7BQ1SOJv4Kr9BnYF_KtkFWpSucJNrmvHJAIG4vvy3CR0Cs686rsS6zgoIvxeMUkMQLkhgFwoOVsGzgT1bb-GeOhmwEJ5ju5NpVf8S5hS42fm4pLkRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63aefba4cc.mp4?token=D66peAK1uWPLljfHd3VZ5Da-3XcmgQ7tHC0mE8v6Kx0ZsOOxaMyZ75f2zal5CXzELA2vTM1eDQnOtxNsuFTc3cB8PBMprRQNHRvplRim2p4uiA0aon-ccjFJYN2H2bSUc1_YZ2Wxx8wfZtdP0TeFXCvryKkBV5TGu5oh58Lqj09W3SsOL3HPCo-OlWudoL1H0tu6SX6ch9xD9PbSuQVUmDirrGiNftX7qY1s7BQ1SOJv4Kr9BnYF_KtkFWpSucJNrmvHJAIG4vvy3CR0Cs686rsS6zgoIvxeMUkMQLkhgFwoOVsGzgT1bb-GeOhmwEJ5ju5NpVf8S5hS42fm4pLkRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وزیر نفت: ۷.۵ تریلیون گاز در جنوب فارس کشف شد.
بیش‌از هفت‌ونیم TCF یا به عبارت بهتر ۷۵۰۰ میلیارد فوت مکعب گاز کشف شده که با احتساب ضریب بازیافت حدود بیش از ۷۲ درصد امکان حدوداً ۵۷۰۰ میلیارد فوت مکعب استحصال گاز وجود دارد.
این میزان گاز معادل این هست که یک فاز پارس‌جنوبی به‌مدت ۱۵ سال بتواند تامین این حجم عظیم گاز را بکند.
این گاز خوشبختانه از یک ویژگی خاصی برخوردار هست و آن اینکه اصطلاحاً شیرین است؛ این شیرین بودن گاز باعث می‌شود که هم هزینه‌های عملیات توسعه‌ای کاهش پیدا بکند و هم هزینه‌های عملیات بهره‌برداری.
در کنار این حجم گاز، حجم عظیمی میعانات گازی را ما داریم که مجموعاً ده‌ها میلیارد دلار به‌علاوه ارزش ذاتی آن گاز برای کشور ثروت جدید به بار آورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70472" target="_blank">📅 20:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70471">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyy4QBt9CwsLtAns2p63AjLqfLpyKO1iEEsxYAfg9PuM5tlnZfTBxtdZuK-Hgp4oRAsbGmR_2GJ1KMwpqQZZt2u4ShQiOHGVXyBOGRydeUFwB-gVEnSUfD52h9XWlywhVZ2YSwEfhXR2uC4kX-40Ty4Vpf84GRH2BJ6q20eZngGgH3R5vgJUXgV_nqMTun3cRikSjRlTJ8cAB0sk5iEN1acleVeZsDbkmmUHdFTa8c9b0sFW4V7U7UmzCKmQQyoYh8zjy6CQLRbq-CI54FLF8ZKC2givhMhX2CYOKE45NFoA3cPB4hgs9Rs4B6XNM2qmQfF9v2Du00mijrVpUU6cqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف در مورد سیاست های آمریکا:
واردات گوشت منجمد برای مهار قیمت گوشت؛ خب، شاید این راهکار جواب بدهد.
اما برنامه برای اوراق قرضه چیست؟ واردات بازدهی‌های منجمد؟ خریداران مسکنِ منجمد؟ یا حقوق و دستمزدهای منجمد؟
سیاست خارجیِ منجمد، اقتصادی منجمد به بار می‌آورد.
تنها چیزی که همچنان در حرکت است؟ بومرنگِ ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70471" target="_blank">📅 19:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70470">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd998e89b.mp4?token=cuLrsGNN6ReaVimXVup-DL6BzAsIvqYzrqmf1AtxBO8c5Bodn8lgpyEVO3vOR07X5JlWAywWIiMnDMSpXt0K237JDANj1KdS_BIP_wh2fKbMMDmqDpjWWAHl--jqZs8ZxWjauVLb1N7MLnwap3wKwt5_ccoNO5mmJ-DBanjcwO2QjxzON5NpGtkZa5km3RQXgJHMdckC1RZ8b10AOzKFo6APO_6Mzr7O4kDt9oLyoe7MZSucHOVLVrIoP1dusR8HTOR_wRCcDFJCTpsLxDCqr8nnYFt_NdaaLEO3fL3PctSXZ5X79g9vaMAUqF_2otAhSX7Jhrb7bwEd_8VmlbbjYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd998e89b.mp4?token=cuLrsGNN6ReaVimXVup-DL6BzAsIvqYzrqmf1AtxBO8c5Bodn8lgpyEVO3vOR07X5JlWAywWIiMnDMSpXt0K237JDANj1KdS_BIP_wh2fKbMMDmqDpjWWAHl--jqZs8ZxWjauVLb1N7MLnwap3wKwt5_ccoNO5mmJ-DBanjcwO2QjxzON5NpGtkZa5km3RQXgJHMdckC1RZ8b10AOzKFo6APO_6Mzr7O4kDt9oLyoe7MZSucHOVLVrIoP1dusR8HTOR_wRCcDFJCTpsLxDCqr8nnYFt_NdaaLEO3fL3PctSXZ5X79g9vaMAUqF_2otAhSX7Jhrb7bwEd_8VmlbbjYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
❌
🇮🇱
نتانیاهو و ترامپ در میدان انقلاب تهران اعدام شدند
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70470" target="_blank">📅 19:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70469">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70469" target="_blank">📅 19:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70468">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSu3czMNzNpuuuTk4ngJE0xK-DMG4dgExdpFK-8oAK-gWAkf8SADzC1V_D0k13LLPKbN_QQ1HcZQ1ZYTL-LxFbxs4KS7lt-Xdt76Yw4HQNaNIdKzIKfx6SsIEHvvpj7-KrSU8dNFnlJO3WZBGwFI5Sz8LFH5X9gUNJyJ6oHq0C1NYCtKJPuZ4h9TIy8Et3BGshyRNb-C5hPLgXxs4QLMUNJeN1sDe4cOavKvYkZE2AVAvrCoUAbRqXBtYGuTjrXW-BI7hfWaO9XqL-ezlJPMJvGllOSRdzYcAMp4p9S_NRdGUADzRgzOuJFydHq564HYPu3vaSSBsacwW1WaqxhHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70468" target="_blank">📅 19:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70467">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f7dd3a967.mp4?token=GaaMK-PCvKfaeq35AKKcAKBjln6nNGXeburislPXfBjjBsEc2h90fq-OdoC3plwq_4NkiVKJEdpxkHX6DBDsUf6cMkWOH_d41XTpw-MEa5zCvfTx-yd0P9ICMBCKXxinbeLd8qCgC8gkrbArCI--uHDgIMIRsv1vzwIsKVxPLZKau7r_BQLhMxKKJPexOGcK9RMT3nC_STkhzh_qI-V4q8b2i6JTh09uOX12kisp9Yo7DTkKszDeyq-1jQT_NhCCYJhfoODfBsjfIScQp6OKjkOQKlqqeP7PdoYq7M-mX_daOYmqrkyGT6wa6CLo9jfhXKiMBWJn-XuJusF8Edvkcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f7dd3a967.mp4?token=GaaMK-PCvKfaeq35AKKcAKBjln6nNGXeburislPXfBjjBsEc2h90fq-OdoC3plwq_4NkiVKJEdpxkHX6DBDsUf6cMkWOH_d41XTpw-MEa5zCvfTx-yd0P9ICMBCKXxinbeLd8qCgC8gkrbArCI--uHDgIMIRsv1vzwIsKVxPLZKau7r_BQLhMxKKJPexOGcK9RMT3nC_STkhzh_qI-V4q8b2i6JTh09uOX12kisp9Yo7DTkKszDeyq-1jQT_NhCCYJhfoODfBsjfIScQp6OKjkOQKlqqeP7PdoYq7M-mX_daOYmqrkyGT6wa6CLo9jfhXKiMBWJn-XuJusF8Edvkcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی مشهد طرفداران حکومت که علیه قالیباف شعار می‌دادن و خواهان انتقام خامنه‌ای بودن برخورد شد و متفرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70467" target="_blank">📅 19:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70466">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c51d98cde4.mp4?token=r1_DZl0FEFuc5_kWdxP9chu4nJMo-OdNFp9wcZZVLNNjJb1fhMHHCZYJPEu3YzegMmcZQ79bOm9SwyAieUlZEcaRfRWBOY5iyXWVMxpaGxuSfD2EQMHjkIze_ZujEtduuwxpes6mo0xr4uX_WRR5wKi_ykP8HKmwRSlWPh5T4XZBd5RrWCmmavMnwvE9E7vXqsOzLcl2ceZ8-Yr7TmW-IFNfU01RQ2n8AWn7Qz4r2Z0C9tX3Moo6JqmMPPCtUtoVcQL5OhrH92oGjJcXmCOkBi6Sl1bYrhcUtSVkCGdz3VUViCfpqIEc_8FKWT8e0m8Ty8tI1KLmlGrrgabylKZkvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c51d98cde4.mp4?token=r1_DZl0FEFuc5_kWdxP9chu4nJMo-OdNFp9wcZZVLNNjJb1fhMHHCZYJPEu3YzegMmcZQ79bOm9SwyAieUlZEcaRfRWBOY5iyXWVMxpaGxuSfD2EQMHjkIze_ZujEtduuwxpes6mo0xr4uX_WRR5wKi_ykP8HKmwRSlWPh5T4XZBd5RrWCmmavMnwvE9E7vXqsOzLcl2ceZ8-Yr7TmW-IFNfU01RQ2n8AWn7Qz4r2Z0C9tX3Moo6JqmMPPCtUtoVcQL5OhrH92oGjJcXmCOkBi6Sl1bYrhcUtSVkCGdz3VUViCfpqIEc_8FKWT8e0m8Ty8tI1KLmlGrrgabylKZkvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
علی خامنه‌ای، بهمن ۱۳۸۹:
زمان شاه حکومت وراثتی بود. مردم هیچ نقشی نداشتند..
🇮🇷
صداوسیما ۱۸ اسفند ۱۴۰۴:
مجتبی خامنه‌ای فرزند علی خامنه‌ای بعنوان رهبر سوم ج.ا انتخاب شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70466" target="_blank">📅 18:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70465">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e23c4e23a.mp4?token=Sfm-99baO6d7nzeizPBm4UkRw6qvJGGOVbW7PXjPHKLAlTJQaxQ2vV-WFbzDquU_wzSCqWp5dxNeT5dKjXMspgLlXT_UqpHY-JBE2WdfY5OrAX1sMOnNrKIjK557hBeBdxadsH3PSSjRNf9f29jCF9XFfODWD9xr3qFKSeWWGXsMg9A5fj7PcSaUpkVg2V5zOtDl7ifW2Hjdwu_V4VHv3YZDn0-5RFEPzHa8RMcv9pBvHZrsDePXEoWZ_LNGv_uMr-idQxbq-dHqu6wKgiU4pHkFY-WzxULgzqbKD3BCMFP0U47Za_tTru310NsjcngZE2v8R3aR_ooCM7NW8v5rTKzmDe4MHMecnScsyMZu9sQRc0e909X6-GwIzcOJCxrGkOBzCMF9Lkd6pFI-RXr2nT4VKD97ufTJGjea_5yPDDsOLhnhcpq26BmIKYzwct7wU4LKmC7aLOciqFZIclrO0cwA_ekiq72q1Zb6r0LeELHZVEiwHP2Bwr4-B1iK_w_1eqGmE7ekOczpoPVnG4bt1OhGqiugE7pnBCoJ2jYHoFpeF3cDKUy6jWAC7dehImrHt8yk7w-RQC7oIWTUIcEt_EVCNUl3l7yqksMIBg3WfqgivIQwLZG8OFzR3EAb3ToXsAuJzGZ_8TbfAMmmelReB-8jx6wzYYQjPP0QUfm8zu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e23c4e23a.mp4?token=Sfm-99baO6d7nzeizPBm4UkRw6qvJGGOVbW7PXjPHKLAlTJQaxQ2vV-WFbzDquU_wzSCqWp5dxNeT5dKjXMspgLlXT_UqpHY-JBE2WdfY5OrAX1sMOnNrKIjK557hBeBdxadsH3PSSjRNf9f29jCF9XFfODWD9xr3qFKSeWWGXsMg9A5fj7PcSaUpkVg2V5zOtDl7ifW2Hjdwu_V4VHv3YZDn0-5RFEPzHa8RMcv9pBvHZrsDePXEoWZ_LNGv_uMr-idQxbq-dHqu6wKgiU4pHkFY-WzxULgzqbKD3BCMFP0U47Za_tTru310NsjcngZE2v8R3aR_ooCM7NW8v5rTKzmDe4MHMecnScsyMZu9sQRc0e909X6-GwIzcOJCxrGkOBzCMF9Lkd6pFI-RXr2nT4VKD97ufTJGjea_5yPDDsOLhnhcpq26BmIKYzwct7wU4LKmC7aLOciqFZIclrO0cwA_ekiq72q1Zb6r0LeELHZVEiwHP2Bwr4-B1iK_w_1eqGmE7ekOczpoPVnG4bt1OhGqiugE7pnBCoJ2jYHoFpeF3cDKUy6jWAC7dehImrHt8yk7w-RQC7oIWTUIcEt_EVCNUl3l7yqksMIBg3WfqgivIQwLZG8OFzR3EAb3ToXsAuJzGZ_8TbfAMmmelReB-8jx6wzYYQjPP0QUfm8zu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قرار آخرشب خوانندگان پروین ملکوتی و حمید قنبری محصول سال ۱۳۴۹:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70465" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70464">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76845d14b.mp4?token=iti37OFLPebJDFJccLptYzKPg1CcG9TzM_35e7iv9NbJQvAIbg-IaUEwxMyq1eONe2pAVklpN8O4Hf31ILrFQDk1DYPtF39GL30M-SpM54QAUbfz-wfQxGAQlyO2f7okanBgyIQHNIEL-tz9y0uil91fGDAQUj1PfhE6zLktMnDdXUQ8eRC1YtZdqZcLHqJDqUd4pvjkKoTP-2LGCxVn6QUfLfKkqSpqlxYJu7BKkmLjTXfIBlg9qyZS0dwvqUjFuk7bz0ImzpA6IMeNcrJqW72fpjJ5PCelGEQom0RflCUZ9A5MAAaMu1aK87WfjWGlKZl7k0X7k-fwBVnkUF3fdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76845d14b.mp4?token=iti37OFLPebJDFJccLptYzKPg1CcG9TzM_35e7iv9NbJQvAIbg-IaUEwxMyq1eONe2pAVklpN8O4Hf31ILrFQDk1DYPtF39GL30M-SpM54QAUbfz-wfQxGAQlyO2f7okanBgyIQHNIEL-tz9y0uil91fGDAQUj1PfhE6zLktMnDdXUQ8eRC1YtZdqZcLHqJDqUd4pvjkKoTP-2LGCxVn6QUfLfKkqSpqlxYJu7BKkmLjTXfIBlg9qyZS0dwvqUjFuk7bz0ImzpA6IMeNcrJqW72fpjJ5PCelGEQom0RflCUZ9A5MAAaMu1aK87WfjWGlKZl7k0X7k-fwBVnkUF3fdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس این ویدیو رو با عنوان «تغییر مهمی که در پدافند ایران رخ داد» منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70464" target="_blank">📅 17:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70463">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a699022499.mp4?token=GWMcXYgCPp0FwewBwyPTzmH2dreTwyoglsgonxe5sGIcw87cNH9lFyK6o16Y92o8mXD4NboM7MaddK-VbZHRHHnHIkZydhRVtMpIawKdZIkRr13nfjiEpTqEPTkgjRp3ouX4RRRXEpArC8TIfFKrQjO4ZQTwQwcg0la41aVBGDLisKedPkLsaGwhK_iR4ZPKcpDJsWpCd08TEAp3Bqopm7MmCo7KGsOu9amOmy4Aikp79KXxGFIOLRYbq6jAbme3S69q5oMvyuE6kVZtqvkmkfWP69x9mVwz9UmFHTIJjb8eEngQB5VBTM747zqAqSc6UMc-kHz3R-RrFltAj_JE3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a699022499.mp4?token=GWMcXYgCPp0FwewBwyPTzmH2dreTwyoglsgonxe5sGIcw87cNH9lFyK6o16Y92o8mXD4NboM7MaddK-VbZHRHHnHIkZydhRVtMpIawKdZIkRr13nfjiEpTqEPTkgjRp3ouX4RRRXEpArC8TIfFKrQjO4ZQTwQwcg0la41aVBGDLisKedPkLsaGwhK_iR4ZPKcpDJsWpCd08TEAp3Bqopm7MmCo7KGsOu9amOmy4Aikp79KXxGFIOLRYbq6jAbme3S69q5oMvyuE6kVZtqvkmkfWP69x9mVwz9UmFHTIJjb8eEngQB5VBTM747zqAqSc6UMc-kHz3R-RrFltAj_JE3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی برزیل یه مرد همجنسگرا رو مجبورش کردن برای اولین بار یه زن رو در آغوش بگیره! اونم از شدت ناراحتی بیهوش شد و از حال رفت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70463" target="_blank">📅 16:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70462">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
این زن و ‌شوهر بعد ۶۰ سال زندگی مشترک اینجوری باهم رفتن برای خانومش کارای زیبایی انجام بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70462" target="_blank">📅 16:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70461">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd43a5dfd.mp4?token=N76uTcJUanSp6c8MQSo3lyULbGaWfLKTzO3wcgz9a1w6nXRWY01KEmuN4rXUg46iddJaKwEWUOAh66euo7WCC-e5jZlLjViaLYuU2ZKfgoQw1CKDBnZLmzRj8Y5GD5KDOGJK6rofJOa1xrKKhcl3fTyl8kMSNdb-FgsBzK0QuO7dlyC_e0QhfeWSRDaM1Rmk4scb0zYfkDCwPwbTNlX6UVM8TIkcoRWrNHrcdj2piBQAQUEx4T2oY0mN-7JyTlzyybf-GJU7KFobTzBYrQmMztebRRv4TDaPNUM3wuybnlc-NIx8dTSpsEatZbew9fkWDVNEM4d5zd9G3m5kPsGuSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd43a5dfd.mp4?token=N76uTcJUanSp6c8MQSo3lyULbGaWfLKTzO3wcgz9a1w6nXRWY01KEmuN4rXUg46iddJaKwEWUOAh66euo7WCC-e5jZlLjViaLYuU2ZKfgoQw1CKDBnZLmzRj8Y5GD5KDOGJK6rofJOa1xrKKhcl3fTyl8kMSNdb-FgsBzK0QuO7dlyC_e0QhfeWSRDaM1Rmk4scb0zYfkDCwPwbTNlX6UVM8TIkcoRWrNHrcdj2piBQAQUEx4T2oY0mN-7JyTlzyybf-GJU7KFobTzBYrQmMztebRRv4TDaPNUM3wuybnlc-NIx8dTSpsEatZbew9fkWDVNEM4d5zd9G3m5kPsGuSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت گمرک شهید رجایی بندرعباس، ۲۹ مرداد ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70461" target="_blank">📅 15:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70460">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">1
💵
= 200.000
💸
🔼
یک دلار آمریکا=دویست هزارتومان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70460" target="_blank">📅 15:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70459">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
🇮🇷
سعید آجورلو، عضو تیم رسانه ای هیات مذاکره کننده و از نزدیکان قالیباف:
آمریکا از مسیر جنوب تنگه هرمز تا روزی ۹ میلیون بشکه نفت عبور می‌دهد
مسیر جنوب تنگه هرمز همین الان دارد کار می کند
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70459" target="_blank">📅 15:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70458">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155fedd97c.mp4?token=AxVnUxILA_rG95mBTAOk6Rp1LtGzf2B2RuWRuYzBzkce9t9r5QKP865J1wjme06mQSS2TahlcZueufAjpnGPVlxeJNVrYiKA1oKuFAe9MpI5qjmqPYRfpF2OU3oYAZsWEx40VGk6pAch7TGu-SDFJD9as-mi9tNqM9PKs5nOgXb9xm3C2xodGRsYiDfnoj7b6PXL4kGqyjLprPJsPY4oc58gGlkKpj-UQpY8LbFGY4X9SpNUFvo9McGZcO4OwdBFECEx3bkMbA28MsmsyVT94SkxoVfFbolyTTfLxuitE1yRCTJCeGwLJZ4lWg0fRlels4yQSZVIgDR3Tua_ApIzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155fedd97c.mp4?token=AxVnUxILA_rG95mBTAOk6Rp1LtGzf2B2RuWRuYzBzkce9t9r5QKP865J1wjme06mQSS2TahlcZueufAjpnGPVlxeJNVrYiKA1oKuFAe9MpI5qjmqPYRfpF2OU3oYAZsWEx40VGk6pAch7TGu-SDFJD9as-mi9tNqM9PKs5nOgXb9xm3C2xodGRsYiDfnoj7b6PXL4kGqyjLprPJsPY4oc58gGlkKpj-UQpY8LbFGY4X9SpNUFvo9McGZcO4OwdBFECEx3bkMbA28MsmsyVT94SkxoVfFbolyTTfLxuitE1yRCTJCeGwLJZ4lWg0fRlels4yQSZVIgDR3Tua_ApIzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شبکه سه صداوسیمای جمهوری اسلامی به طور آشکار بارون ترامپ، پسر رئیس جمهور آمریکا را تهدید به ترور کرد
؛
در این ویدئو، اطلاعاتی درباره رفت‌وآمد بارون ترامپ و محل‌هایی که می‌توان او را هدف قرار داد، نمایش داده می‌شود.
سازندگان ویدئو مدعی‌اند این اطلاعات از طریق زنی به دست آمده که با عبور از تدابیر حفاظتی، دیداری خصوصی با پسر ترامپ داشته است.
وب‌سایت حکومتی تبیان نیز این ویدئو را با عنوان صریح و تهدیدآمیز «بارون ترامپ را کجا و چطور بکشیم؟» بازنشر کرده است.
خبرگزاری تسنیم، نزدیک به سپاه پاسداران، در ماه ژوئیه نیز ویدئویی مشابه درباره ملانیا ترامپ منتشر کرده بود که در پایان آن بارون ترامپ تهدید می‌شد.
سرویس مخفی آمریکا در آن زمان اعلام کرد از محتوای منتشرشده آگاه است و هر مطلبی را که تهدیدی علیه افراد تحت حفاظت تلقی شود، بررسی می‌کند. سرویس مخفی آمریکا تاکنون واکنش جداگانه‌ای به ویدئوی تازه نشان نداده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70458" target="_blank">📅 14:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70457">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/625bbb5ced.mp4?token=hLvplBWEw9J1enRtH4XWNxqchPHoCWB2jsbO-88OBxL2579n5CqBvcFC1Aa3URONA5vO3zv5YREiUZuXbF0R0Ir4SASRcApqcY_VV-BRH1Ry5N0s4GroY3J1S9vA8lr4stGR5eGEy0qaYLKN9SthHqSpTmEdecp_EnJHU3lovYw8mwWjdG36_vgNmMbgv3FSdCGU-_tOlXKHEg4Bw7w3BAsshGSCQMJ_V_UjEGvglWz1ziw1hPKHhmzTb4pDFPL0av__45y9miHB-AIhvmwOiLd3Z0rGqV3zDCN0kyexM3i29xzBMf172jFYMmm919vhLy-rRdbcpGt6dFlgjA7ANw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/625bbb5ced.mp4?token=hLvplBWEw9J1enRtH4XWNxqchPHoCWB2jsbO-88OBxL2579n5CqBvcFC1Aa3URONA5vO3zv5YREiUZuXbF0R0Ir4SASRcApqcY_VV-BRH1Ry5N0s4GroY3J1S9vA8lr4stGR5eGEy0qaYLKN9SthHqSpTmEdecp_EnJHU3lovYw8mwWjdG36_vgNmMbgv3FSdCGU-_tOlXKHEg4Bw7w3BAsshGSCQMJ_V_UjEGvglWz1ziw1hPKHhmzTb4pDFPL0av__45y9miHB-AIhvmwOiLd3Z0rGqV3zDCN0kyexM3i29xzBMf172jFYMmm919vhLy-rRdbcpGt6dFlgjA7ANw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هیبت الهلبوسی مادرجنده، رئیس پارلمان عراق:  ما به قالیباف گفتیم اسم خلیج ، خلیج عربیه ، اونم گفت شما برای خودتون یه اسم دارید و ماهم یه اسم من بهش گفتم پدرانمون بهمون خلیج عربی رو آموختن ، اونم گفت هرکی یه اسم صداش میکنه! آخرشم به دیدار رئیس جمهور که رفت…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70457" target="_blank">📅 14:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70456">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2228bf806.mp4?token=bRiOuozZMz7nl26Ixd8GYuCUIOp9yuQpr4nRQ0yq6AS1JthZ3ow4IlZpzTmjIZ0DlXMlLke8xXxv37spupUewl6RjNOWYQ6o3RxUnW2Onfe1zUGKXMD3nnME0mJ7zdffmgPJarGp53akWQ6WOAzTLDPMbQJXNjvqao5GkcVFRkCpvH7HIsoYPl33K9t3FDqKApDCRgdCdWaWMH1xUTPbmVVuDuzv636oCqOvpsbGDz6DFCV0ZgQNbs7Tr7llg8Djim7zlqgdE3V9OCWYKNchm-iCX7Vsr06Hx_fBjM-wQkOmoGX8-THqnWX7InU7XNDLGgI-wfe70P-uLbxeKrtNkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2228bf806.mp4?token=bRiOuozZMz7nl26Ixd8GYuCUIOp9yuQpr4nRQ0yq6AS1JthZ3ow4IlZpzTmjIZ0DlXMlLke8xXxv37spupUewl6RjNOWYQ6o3RxUnW2Onfe1zUGKXMD3nnME0mJ7zdffmgPJarGp53akWQ6WOAzTLDPMbQJXNjvqao5GkcVFRkCpvH7HIsoYPl33K9t3FDqKApDCRgdCdWaWMH1xUTPbmVVuDuzv636oCqOvpsbGDz6DFCV0ZgQNbs7Tr7llg8Djim7zlqgdE3V9OCWYKNchm-iCX7Vsr06Hx_fBjM-wQkOmoGX8-THqnWX7InU7XNDLGgI-wfe70P-uLbxeKrtNkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هیبت الهلبوسی مادرجنده، رئیس پارلمان عراق:
ما به قالیباف گفتیم اسم خلیج ، خلیج عربیه ، اونم گفت شما برای خودتون یه اسم دارید و ماهم یه اسم
من بهش گفتم پدرانمون بهمون خلیج عربی رو آموختن ، اونم گفت هرکی یه اسم صداش میکنه!
آخرشم به دیدار رئیس جمهور که رفت ، رئیس جمهور بهش گفت که بهتره اسمشو بزاریم خلیج اسلامی که کسی ناراحت نشه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70456" target="_blank">📅 14:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70455">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💵
دلار: 1,980,000
🔼
هرگرم طلای ۱۸ عیار: 21,907,000 تومان
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70455" target="_blank">📅 13:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70454">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd4541c3f.mp4?token=GqRGD4VK6mvDf89UO-DsYPXMUkD7B_giWrrHzG9GeY83z8WqPlRq1opLADrt0ugS1zSr6V2x2Zb7MCGvbNBcK9GZXX9KRhkgwuhjXFJ6KJidY_xqWNghy4JIV4nd51wad8LRMlxiak8lX-_elXdgV4MuKwlV36-T9cs2m_HbI1chIdyEl1OjCR6FdZUAMNi2JFjoTxnq_aJ1ROfFuDgHk_TNmpC_wkapz6i9Up-mBWSloAuxriYYsMIiYgIuMv2jZHpYMwt6GmpYkmGFc0O2FJtTBk4QHn-_bfNJO3FegZ-Ij8auUF2b-pT4Amy8nKVlOhL-U7lXAHzVf0Q3_AI1yhD8ToRbcspZ_tNydg1vPtvZIxFQ6EYgNjswaXbKaQ7RtNKpELu7AIwFp5-F4WYrEsUPoShWAiDuUDnSnv2-ypUNr4Hp_K_SRIKuZQJAr_WpRIrtjGzdfdJKHc8qNb5BShE2IKneRWiGtCHJBtJWGGoWa7DFc1FjovtuM9nw9lmAUGI0awuaq2Jadq2bZvao0GMLlQPgf6PAy0oTeaBGxH8otpI-TwtEFLuftb8P6CE0h4xYPR0W6R6P1boIQ3FB0QV_wD9rv4jIm-5BoNvy8BaUtZ5tIgcIGuRBt6ecP6Xj6j6nsXxckNKLlFX36yswOU248od9G_gI0Okt_llbGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd4541c3f.mp4?token=GqRGD4VK6mvDf89UO-DsYPXMUkD7B_giWrrHzG9GeY83z8WqPlRq1opLADrt0ugS1zSr6V2x2Zb7MCGvbNBcK9GZXX9KRhkgwuhjXFJ6KJidY_xqWNghy4JIV4nd51wad8LRMlxiak8lX-_elXdgV4MuKwlV36-T9cs2m_HbI1chIdyEl1OjCR6FdZUAMNi2JFjoTxnq_aJ1ROfFuDgHk_TNmpC_wkapz6i9Up-mBWSloAuxriYYsMIiYgIuMv2jZHpYMwt6GmpYkmGFc0O2FJtTBk4QHn-_bfNJO3FegZ-Ij8auUF2b-pT4Amy8nKVlOhL-U7lXAHzVf0Q3_AI1yhD8ToRbcspZ_tNydg1vPtvZIxFQ6EYgNjswaXbKaQ7RtNKpELu7AIwFp5-F4WYrEsUPoShWAiDuUDnSnv2-ypUNr4Hp_K_SRIKuZQJAr_WpRIrtjGzdfdJKHc8qNb5BShE2IKneRWiGtCHJBtJWGGoWa7DFc1FjovtuM9nw9lmAUGI0awuaq2Jadq2bZvao0GMLlQPgf6PAy0oTeaBGxH8otpI-TwtEFLuftb8P6CE0h4xYPR0W6R6P1boIQ3FB0QV_wD9rv4jIm-5BoNvy8BaUtZ5tIgcIGuRBt6ecP6Xj6j6nsXxckNKLlFX36yswOU248od9G_gI0Okt_llbGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طرف رفته ماشین "شاهین" صفر کیلومتر خریده، بعد بهش گفتن با مانیتور؟ اونم گفته آره؛
حالا که ماشینو تحویل گرفته دیده مانیتورش روشن نمیشه، دست انداخته پشتش بازش کرده دیده توش مقوا گذاشتن..
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70454" target="_blank">📅 12:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzcFjMD4a9DwhREuV3nWJ6JsD0er-K3WjI068n7ef4t8XWh0SjP7TsSk8AWkUjIo4Zo-oDwJaaZys2k4sbItxaNdGMyXc1DiJlEtx0Y_SHn_0_p1Zt0kfYR1-kp2MWPXyKQt8fhTw__2fLmRPn8VNMzKa4bKaKj5uLKi_T14WkSN5N9UREJaBJbjL6PSfdBLrahFSMfWmlQodp5C8EyZ0ix9JzGbFppUmsw5YpJmxvdHPVwVECW91wfPZjF11p9SDJU8baTN90iocReizShxuqvHWByio0lMUhWALCdJFMsYMTaZdmZapRvKAx9izlwfwbbVbFjr_lrzBwii2y_HWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد کنکور و امتحانات نهایی قیمت چادر های تک نفره حدود ۵۰۰ هزار افزایش یافته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70453" target="_blank">📅 12:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70452">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70452" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70452" target="_blank">📅 12:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70451">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn3GTAdsOmO2OqYGn0mwAb85xKUBfVEb2UIfaxhLgDLL3ciiAeZdqeiMxSFsioqp_64pAeQm0r9-t3lA6itp4JZJt309LVSZRcKAiUxy6Dwwp_YbTUQ_iZ4aJrziOS46GBVaOiQl-QLbRZ9NfhRTZtA7m8xfXMK4s-yDSAuLwAcFlsRT5SvmMTUBPCFgxgM_2WKJnpmorhnzbrJ-nvXRNJqzbNAvOb6G2YXXvGABibjobvtox9qoFqyJarHwdy311BV67Ma7QSy1L3rx-_RljMjKFhpyv4032HG-53o7Zb2aJmsJmTBTeI8HX2fF6in-itBe6oRHhZSzWri012HLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r1
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70451" target="_blank">📅 12:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70450">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25b2c22e49.mp4?token=G6VzJ2QQwJvj61x5VMnN2srh6kI2mdy6H2net9rvdb7HiKXJU6XzhXdl4ewFjDAMUJex9K0MgYPPzQmy_Mkmln55FFYUUWcuYS425V3vsZR9Zlu6ut6wb8IHM1NSbN0HoqiVaMmYKmki3vek5gCLwsTBYi5WxNdT7EYW9wAPjTmoGFcHI7r_xmpo01YieXn-8xuAsaGT2_sHIGP6SZQas1cHKquAJSU-QVVXeF2sj8iv14F0-O-WNP-vdTfSmXeSyntI-IbSJ6v6bWlia9TqRPHXR_ryCADbukoNpxrBOsLa6C_ohfdUdnl7vR6DZe0AK_D-IXfpqLsju2Z14jnWmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25b2c22e49.mp4?token=G6VzJ2QQwJvj61x5VMnN2srh6kI2mdy6H2net9rvdb7HiKXJU6XzhXdl4ewFjDAMUJex9K0MgYPPzQmy_Mkmln55FFYUUWcuYS425V3vsZR9Zlu6ut6wb8IHM1NSbN0HoqiVaMmYKmki3vek5gCLwsTBYi5WxNdT7EYW9wAPjTmoGFcHI7r_xmpo01YieXn-8xuAsaGT2_sHIGP6SZQas1cHKquAJSU-QVVXeF2sj8iv14F0-O-WNP-vdTfSmXeSyntI-IbSJ6v6bWlia9TqRPHXR_ryCADbukoNpxrBOsLa6C_ohfdUdnl7vR6DZe0AK_D-IXfpqLsju2Z14jnWmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
یه دختر ایرانی رفته یکی از روستاهای روسیه فیلم گرفته و نتیجه‌اش قراره شوکه‌تون کنه!
فرض کن یه دختر ۱۰/۱۰ داره لاستیک تراکتور عوض میکنه یا سیب زمینی جمع می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70450" target="_blank">📅 12:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70449">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0832bfae35.mp4?token=InTFTUFYjG_kz9sSVf0XVb8KEV0miuBmtzpSWq24_o0zVLngQEQ_15rElcEX3ndMkoAw6ubGAeiV5D8WI5992_y2rGF82_Yn16puYzwUPj_lnGEKS8uY_xYQWnUpiLIwHNIP1Xr-eJmjBql5N_3CG5zyzHJiWEf4xG72vRHOKu9f6czJ0S-O0hEmkmbhs3HwvknAGUFvbsCpib4o0d0nTa2EUA_C8knFUFLU58E9TfM41OPeYFpiYau4mDtUdMedQSuNBlsqlXnlujv3N2xBQLc9gj99qw9C7cucDLlQAA6B66UEcesmPGhBtDIsuP-5oPU8k2K23fAGbYROqcsjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0832bfae35.mp4?token=InTFTUFYjG_kz9sSVf0XVb8KEV0miuBmtzpSWq24_o0zVLngQEQ_15rElcEX3ndMkoAw6ubGAeiV5D8WI5992_y2rGF82_Yn16puYzwUPj_lnGEKS8uY_xYQWnUpiLIwHNIP1Xr-eJmjBql5N_3CG5zyzHJiWEf4xG72vRHOKu9f6czJ0S-O0hEmkmbhs3HwvknAGUFvbsCpib4o0d0nTa2EUA_C8knFUFLU58E9TfM41OPeYFpiYau4mDtUdMedQSuNBlsqlXnlujv3N2xBQLc9gj99qw9C7cucDLlQAA6B66UEcesmPGhBtDIsuP-5oPU8k2K23fAGbYROqcsjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی ساحل میانکاله مازندران، حامیان حکومت با چادر دست به اعتراضات زدن و اعلام کردن مردم رسما دارن لخت میشن، ما دیگه تحمل نداریم، یا دولت برخورد میکنه یا خودمون دست به کار میشیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70449" target="_blank">📅 11:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70448">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⏺
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:عاصم منیر فردا به تهران سفر می‌کند
این سفر در راستای تقویت همکاری‌های دوجانبه ایران-پاکستان و ادامه کمک‌های پاکستان برای کمک به تقویت صلح و امنیت در منطقه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70448" target="_blank">📅 10:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70445">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8129d80281.mp4?token=pvoBzlz9_DrPj4SZZdi8y2H-op6YPsGEG_t4BYZ-4IPDwZ89AkYFNQisg3xMopMeU1aFtyjNg2wVEvvhzBkkaOxGjGPCKvh0TIpX4Vb_XAN2fMpaFtio314Q1IlidrxVfY3Vq9jMDqWzFBKzFNezo-ctPm4EYbIDZ1VQODwgRWYitIu6T0qWG9UXxQYictqshkJ8Q92khkLNpdpxWcgIXkqKitdmKjWahdE77zFPoX5FOjxaApuq7QL-Hir7epn2v6Cvk46QbAqSt9W2V88w7xHnWG0hpwkHTj4hmaV9T-zN7fIG-BoAXhURE1ah_fb8w1RpmyfHFLfVqnH04n430Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8129d80281.mp4?token=pvoBzlz9_DrPj4SZZdi8y2H-op6YPsGEG_t4BYZ-4IPDwZ89AkYFNQisg3xMopMeU1aFtyjNg2wVEvvhzBkkaOxGjGPCKvh0TIpX4Vb_XAN2fMpaFtio314Q1IlidrxVfY3Vq9jMDqWzFBKzFNezo-ctPm4EYbIDZ1VQODwgRWYitIu6T0qWG9UXxQYictqshkJ8Q92khkLNpdpxWcgIXkqKitdmKjWahdE77zFPoX5FOjxaApuq7QL-Hir7epn2v6Cvk46QbAqSt9W2V88w7xHnWG0hpwkHTj4hmaV9T-zN7fIG-BoAXhURE1ah_fb8w1RpmyfHFLfVqnH04n430Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درحالی که تمام شعبه‌های ساعدی‌نیا پلمپ شدن، کافه قنادی "بابک زنجانی" تو شهرک غرب تهران دیروز افتتاح شد و قراره پاتوق جدید بچه پولدارهای تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70445" target="_blank">📅 10:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70444">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc8a06759a.mp4?token=pC-yh87Wmk_8nX5zKHGDZhrBu9ySwK4KFHeK4gsg_gHN-Z6SuiPB2rdWHPo7dqhaYHxbbWJinc9N3CluI4aQOsWAyTQefVXYiBCxznhWIeqTPz9uSZ0_dkjsJX3G32K_syUxtwuYpAMgXhJ-CPanIYTfQJ2luzDtz1PJzS60FVpNC0Izp0ggGfn0liwZDuCzzBCT8VX3QXuZk2PcXXb0nyN_PlwrW2vq1t3F6CtENADSSPRUzGipEf2qm_mtv-nRZIrAqiVGjuRkiZQd376eFSNPHq1FROTbv-kBq_RqmiLgsVo9fi4wdQbVsTVVYZd6RWTbMb0HEptVpTOGG-NCEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc8a06759a.mp4?token=pC-yh87Wmk_8nX5zKHGDZhrBu9ySwK4KFHeK4gsg_gHN-Z6SuiPB2rdWHPo7dqhaYHxbbWJinc9N3CluI4aQOsWAyTQefVXYiBCxznhWIeqTPz9uSZ0_dkjsJX3G32K_syUxtwuYpAMgXhJ-CPanIYTfQJ2luzDtz1PJzS60FVpNC0Izp0ggGfn0liwZDuCzzBCT8VX3QXuZk2PcXXb0nyN_PlwrW2vq1t3F6CtENADSSPRUzGipEf2qm_mtv-nRZIrAqiVGjuRkiZQd376eFSNPHq1FROTbv-kBq_RqmiLgsVo9fi4wdQbVsTVVYZd6RWTbMb0HEptVpTOGG-NCEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یادی کنیم از سخنرانی طوفانی «معمر قذافی» ؛ میشه گفت این سخنرانی یکی از دلایل آغاز پروژه سرنگونی قذافی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70444" target="_blank">📅 10:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70443">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bteU6E-dAaDdLsRA9rX4uuCVfSdLMCZCl0qzNP4Lz4BXIPy1PH1flRQk62JwkQqmij-unR3QP6KSObo43prz9oziddpfm_UAHoToc6cBjqlrwkol8OC2MOszchCMXORLp9fgCNK6m0Whows-FKZerZrabaiOGk5CFkjWYPKteO5mRo4KFCFd7Bzj4fyu5rvo3HXIKH5iTmqV_9tQi2neoI1x2rGsWMt3EXFYMGhJCKKi8WVOtXJ2Rt4uyIYdbVGsX-sD0SyV65UooQl5bixZHiiLvQEVxVaZ_IKAyxZDSyGD2PCFxean6PMTJIkAderb-hVkWgnPB0F-HjxPDu8cBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کنکوری که گذشت:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70443" target="_blank">📅 09:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70442">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b2128551.mp4?token=BDoaYsy1j6CTpKG1V2SYMbHDoTemEfiIBozPUUbCdyr_O0HC7nOleBSIiusr4N1sbTDf17DpcrL1b2izhfqIuHY_Vr68-0X6NuZVMQA_e5-JfkmjqjAM3PbkjjeZ3u5I7AAeYHe3zYSD5bRJ_w_vnMP_OAJb8MUgKeUH-WX-6zgWJlogJ_GHCizEXCPFNOG3H1hADAwzOdgNg3DK52IT-HCjz90HlAjBMIoufLnvtrbEJ02j86WLmWvtm2hj24AkCRV40EDdoUPK0OWnSlqjSGbW7TF-pED6hSUsGO04B0eGCjJGeq3g4pLjwDHPo3pl3hLLVRGXkYJ4l5thUKhr5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b2128551.mp4?token=BDoaYsy1j6CTpKG1V2SYMbHDoTemEfiIBozPUUbCdyr_O0HC7nOleBSIiusr4N1sbTDf17DpcrL1b2izhfqIuHY_Vr68-0X6NuZVMQA_e5-JfkmjqjAM3PbkjjeZ3u5I7AAeYHe3zYSD5bRJ_w_vnMP_OAJb8MUgKeUH-WX-6zgWJlogJ_GHCizEXCPFNOG3H1hADAwzOdgNg3DK52IT-HCjz90HlAjBMIoufLnvtrbEJ02j86WLmWvtm2hj24AkCRV40EDdoUPK0OWnSlqjSGbW7TF-pED6hSUsGO04B0eGCjJGeq3g4pLjwDHPo3pl3hLLVRGXkYJ4l5thUKhr5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
مراد ویسی، تحلیل‌گر ارشد ایران‌اینترنشنال:
🔴
جمهوری اسلامی با سه‌راهی مرگباری روبه‌روست:
تسلیم شروط آمریکا شود
وارد جنگ شود
بدون توافق و جنگ، با فروپاشی شتابان اقتصادی مواجه شود.
🔴
این وضعیت اختلافات در راس نظام را تشدید کرده؛
احمد وحیدی، محسن رضایی و حسین طائب خواهان ادامه تقابل‌اند...
پزشکیان و قالیباف با اشاره به محاصره بنادر، قطع صادرات نفت و کمبود بنزین، توافق با آمریکا را ضروری می‌دانند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70442" target="_blank">📅 09:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70441">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">💎
میدونستین تو دربی بت
✅
با شارژ بالاتر از ۱۰۰ دلار ۱۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70441" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70440">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70440" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر D
erby Bet
✅
✅
✅
✅
واریز و برداشت ارزی و ریالی
‼️
✅
بونوس 120% اولین واریز
‼️
✅
بونوس برای 4 واریز اول
‼️
🎁
بونوس ورزشی هر شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🎁
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
@DerbyBetOfficial</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70440" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70439">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9RTDsaFCul9h1zHM5X-zofd9prvS7cA1N9bKDQi1Oz-I76sQaW9mBoVFZOT-LHbrBJZmwhE3IhWrXS5rnzAbFgf2p5N51RIwmXUX5W-WArwD8Fe2LXkuntvQeKxLdVCsLlvLBnH9GnkCnkoE8p2DsOWC-CZn1DdFEOtOPI13BR7bTn1ZZeb3GzorVa8MPv9sqyt-5L96g7xRzHxcCVa_posuU8eQMdZaDYJtyd2XedqSdJrb0UZ5M1LFAE8-cNPe4GIByKkzrm_bYGr3LnFVBggfE9wwvNQr4OR9yrmml9wTV-W9VuuNtl9-KA1kms7PANfnhfGBfDUHvDuUVjHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ با انتشار این پست ادعای مارک تیسن مبنی بر اینکه بیش از ۱۰۰۰ کشتی با اسکورت از تنگه هرمز عبور داده شدند را تقویت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70439" target="_blank">📅 01:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70438">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6VsSDxp-GOfS-Ei25D7D3if6v_ns9zUzcrj00aJSDxlUAg8c8MDMFv9iXONak7AmolK2ND8l4vxUCXjzbrP68wfL1sICisU7GZRvqvJwrnIRhbjdeQNaa-RazK4-JwWCmIJAktoQDX6U2d_b4T3cpJDiCmNn89ed-N5cWyeJ70XEOtUXYGSwOVW-NJiwLnWi5TcMx8qhRTuThhvtGTm_XkFdpExmuh9hMiADckxmVVLdr2sdW4n99PxnmJN8exXMC3l-2TQKJ_rVnoUlX3upwJyvNXA7u5uGcwL8Ex5_cuvX0qE0k3WbqxTCcBGwP5yxoY8r8e9X-wdjnGf8FmRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
املاکی مجدد این تصویرو با عنوان تنگه هرمز قلمرو جدید ایالات متحده منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70438" target="_blank">📅 00:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70437">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39665a7cce.mp4?token=cDcTSvHnQrtXYxeMbXdtejK8zyXDojSfZzf9vnun9mfDDzhJq1ZB5UetWnSk0E7THewKsDh6Rb18p38ju34bxkjY8VNohJayVtzS4jfqysW3lXOSI2kqtxR085Re86-hPK4K4b5Yo-bo4vgk-GFkApoOjS1C-tSyzRQ35gSVpljd3YiW918-mklzC9vsw42vKtnupVhnduJhrIQERky2jSAmhs8Fx-wBkzgSjmHwWKFbSuxUQKyHYX78HT6P09tnbhYlGNLVQQFVQd2xmD70_6MOGqCklxa16OVp6F3nJDoD1bciqnFwypN0zuTldyEotrpus0_1NJrhFk5nn0VPDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39665a7cce.mp4?token=cDcTSvHnQrtXYxeMbXdtejK8zyXDojSfZzf9vnun9mfDDzhJq1ZB5UetWnSk0E7THewKsDh6Rb18p38ju34bxkjY8VNohJayVtzS4jfqysW3lXOSI2kqtxR085Re86-hPK4K4b5Yo-bo4vgk-GFkApoOjS1C-tSyzRQ35gSVpljd3YiW918-mklzC9vsw42vKtnupVhnduJhrIQERky2jSAmhs8Fx-wBkzgSjmHwWKFbSuxUQKyHYX78HT6P09tnbhYlGNLVQQFVQd2xmD70_6MOGqCklxa16OVp6F3nJDoD1bciqnFwypN0zuTldyEotrpus0_1NJrhFk5nn0VPDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
توصیه‌ام به مردم اینه که کم کم از تو همون خونه و محلات، شروع به تولید چیزهایی کنن که نیاز دارن
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70437" target="_blank">📅 00:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70436">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927919a024.mp4?token=KzdGBn_VWLdsa2VC_HWuntdGmIHolwrF4BWewDSJCeRHiupVGRs04ETMmzNLLekpfWjhcSUuC9JEJ6mLXfzOihbKTWKpAciz6G59SS2XRsDZ6fqBSWvVbCEjsG_04TmPLSsW_I1IJk5p0QJMFG-bovOeE9fLMiAmeLl3q8EHhpwq2wx-dM2a1w5-Cu7i1SzkDiNfgVJgeFVu19RPLd926_cv8PWBJPmQY2Aj6zU062Kj32AosCLp9r5sSJ97Est58tWWsNyCgdTMvjV4C2ro6mf4w60rpgxOw966GN_jjVt97ZZGT-JzY7vkGp0sENZ40dfI4cWnz3PFnQziWpn4Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927919a024.mp4?token=KzdGBn_VWLdsa2VC_HWuntdGmIHolwrF4BWewDSJCeRHiupVGRs04ETMmzNLLekpfWjhcSUuC9JEJ6mLXfzOihbKTWKpAciz6G59SS2XRsDZ6fqBSWvVbCEjsG_04TmPLSsW_I1IJk5p0QJMFG-bovOeE9fLMiAmeLl3q8EHhpwq2wx-dM2a1w5-Cu7i1SzkDiNfgVJgeFVu19RPLd926_cv8PWBJPmQY2Aj6zU062Kj32AosCLp9r5sSJ97Est58tWWsNyCgdTMvjV4C2ro6mf4w60rpgxOw966GN_jjVt97ZZGT-JzY7vkGp0sENZ40dfI4cWnz3PFnQziWpn4Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن رضایی، دبیر شورای عالی امنیت ملی:
🇺🇸
🇮🇱
نتانیاهو به ترامپ گفته ایران رو 6 ماه محاصره کن، تسلیم میشن!
ترامپ بهش گفته اشتباه میکنیا، نتانیاهو هم گفته آقا تو 2-3 ماه تست کن، می‌گیره.
آمریکا به طور کامل از حمله نظامی ناامید شده و محاصره اقتصادی راه انداخته.
هدفشون هم اینه که یه عده معترض رو بریزن وسط خیابون تا اونا به F35های آمریکا کمک کنن.
محاصره و تحریم‌ اقتصادی آمریکا ادامه پیدا کنه، شرکت‌های آمریکایی منطقه رو می‌زنیم!
تا الان هیچ کاری با شرکت‌های آمریکایی نداشتیم و فقط پایگاه زدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70436" target="_blank">📅 23:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70435">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=iEeBhq28P7eACwZ2wKpxbzFJi9-x21ale9FvqGIegKo9zOpm8FcpROWBLFweggsVQf47tJCdKANuntEvPQb-_gZPZgZCYTlAAQuHkKVf1b3xVXf_7dZutn8nxLWStrDgbhbSnsTIgbc3cMFch2I3C273M1DViBYiWQSKwQnctZWrc3WsYS64gyiJZ6-1uuQl8BwQzIN0ShniWtSiYlP_Qd0-5u_sweiU0hO4GcV8bXazH6LSM7krKIavu2XJ5uXcnKP8zLKq0h52_ZmKsur8hM0L9yISBFNLiZTCth1_7Vr8itsfKSFeuxtbPlp7Pdfm1b2Y2-CTIv5VwUUIWfpGeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=iEeBhq28P7eACwZ2wKpxbzFJi9-x21ale9FvqGIegKo9zOpm8FcpROWBLFweggsVQf47tJCdKANuntEvPQb-_gZPZgZCYTlAAQuHkKVf1b3xVXf_7dZutn8nxLWStrDgbhbSnsTIgbc3cMFch2I3C273M1DViBYiWQSKwQnctZWrc3WsYS64gyiJZ6-1uuQl8BwQzIN0ShniWtSiYlP_Qd0-5u_sweiU0hO4GcV8bXazH6LSM7krKIavu2XJ5uXcnKP8zLKq0h52_ZmKsur8hM0L9yISBFNLiZTCth1_7Vr8itsfKSFeuxtbPlp7Pdfm1b2Y2-CTIv5VwUUIWfpGeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
فیلد مارشال محسن رضایی:
در رفتار دیپلماسی ایران قطعا اصلاحاتی انجام میشه و تکامل ها پشت سر هم صورت میگیره
تصور جهانیان از آمریکا به کشوری خوار و ذلیل تغییر کرده و ایران قدرتمند تر شده
ملت ۵ هزار ساله ایران با دولت ۲۵۰ ساله آمریکا داره رقابت میکنه
تصمیم رهبر انقلاب برای آمدن فرماندهان جدید نشونه جنگ متفاوت و غیرقابل پیش بینی از سوی ما هس
حتما شیوه جنگ رو تغییر خواهیم داد
دشمن روی تفرقه و اختلاف حساب باز کرده ولی وحدت ما کمتر از لانچر ها نیست
حماقت ترامپ باعث شده کل جهان خواستار دستیابی به سلاح هسته‌ای بشه
در جنگ جدید اقتصادی نیز به حساب اونا خواهیم رسید
ترامپ خالی بند است چندماهی هست اصلا حرفاشو گوش نمیدیم
وحدت بدون اطاعت از رهبر انقلاب ممکن نیست
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70435" target="_blank">📅 23:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MMgf8_fa6XMaTws_K9jSogJ_jeFcnaO5dfbqmfy-0Pq4b_H5lGLGBmwLnh-XDrs1fRpXitgTEjc_4pkW4xuvktJWpzAkwXuR56aRl_XIpY0zlbowCY5q5jiqNU_kl5phscgxLVZxDFSBCMKhXKk1Y9CaT-Vd_Udh9loeTRsdyfzdTypaCZVzs4kVm9XdJNj7Y7gsHEOqdokzoj7Clc2mZHMX0ad9ChmGwFrFPIbWldTFSu2TnlB4ZVOSWxlgpvANO4W8sQMh4DXZbkp2CYrpmytYRCK5XIgup3slbVrBclUhmOW-i3IiiWI4NKeH9GXYwTqD2wSPLB10wsQGSu-Xyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ACvjWlp6PuraHMPiw9tiHD_DKz4waUTzGaJKbbMT0MOvvYjG6eAkw-DKrkMX4M6VG1jj-4B02bpdVi0ktqlYX2OTEYuCgyq9p3THzR5v3WrczA-gTnLnI-hclv-FwTlzSbjaFdnVoPLuBC-RSGV-U4NtMqOafGqXn5KzHKKRlpWteVtMVIqzZ9ouUlh0qUrPbTO3B0FHSeamxYgYTF7DV_xdBQpQbf69iGRMmKrab2nVRyGIuyLPjuLdtbI8WYVJCwdTWcQC7-BWPgwEpmHa6wriBxf1BLNsYWKSlU5vF8GOBs8IeQXVLO6XkMfSxE1diV21_DorkMG8LC8SwClu1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kMLYa8Q2uvPjYsjtJmC07ryikAkd0DM82Ov8olCTHlNPyLUNZV9D0hX8YYshQEuklrykxdX1PCTNGkqt10U1L0uZv1oGaOK6irPtLgE7lV3WQbTVjZ0NVn9XIfTHa2hFqHCJuD200NuP9jujajlJO9zcZhe8FfP0kRAr3omm5cyqpmWS0YFhvwnK9KeFRcIhi8HacvtVsKVsSqGcCH0S3LPJL4he8eIbfrNzJniBMC87RD7Z3hugmrCTLRzlRccGjrhHkybt28oeKO9kJxfV5nvnrD746_0Gb_t8DnePv0x3rLAYlRmhrYeDX5HdJFX0yL_VJxwRWYZH1yWERXIjhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
جفت کنین؛ یه دختر به اسم نگین، سه بار به دوس پسرش خیانت کرده و پسره بخشیدتش.
اما بخاطر اینکه پسره با خاله و دختر خاله‌اش رفته بیرون تهدیدش کرده رو صورتت اسید می‌ریزم!
چند ساعت بعد دختره پیام داده که حتی اگه صورتت با اسید نابود بشه، بازم مال منی!
من پنج بار تریسام زدم اما تو وظیفته منو دوست داشته باشی!
فرداش رفیق دختره پیام داده که نگین مسته و با یه پسر به اسم امیر سکس کرده، اما خدا شاهده قلبش پیش توعه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70432" target="_blank">📅 23:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
گروهی موسیقی در جنوب ایران همراه با جمعیت، آهنگی سنتی به سبک بندری می‌خوانند و با افتخار نام رضا شاه را فریاد می‌زنند
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70431" target="_blank">📅 22:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg0DEbxCnu7Hn0KXRG4yKsuQ0K4bSsv0X4uNvkUNgRP0tTZERnYTh5KhOPqbgZoE7v2BXgOIOc21X6IW0Rr-0SFndJ89yukA2JBOswCObCxLE2z3yAW2Zq8g24UR2CAE-IBtJsip37wCqb7C5ORtV9qAfbZWfcFtlFP3rCidk-tVzwJv1KeNXT6h7m85mV8b4b8WyNVJhp0SA1bm3oj589rbZ_WiWha70zYTCG101y7t4VgMcvGRYIDpyoA3Zqi2MFOf3XsqzxQqVL8DwxGAhK8Dxc6DGHFPsqe_a4Jckc8Wxnl0rZf5UUxGH4cj-MoonO2bbCI7cR5FuEdvFNYSOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اینترنت یکی از استان‌های یمن رو قطع کرده
حالا خبرگزاری تسنیم اومده نوشته اقدام ضد انسانی :))))
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70430" target="_blank">📅 22:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b6fb2242.mp4?token=K2d_7A7ev0eSirZFm--iv00trEmak4R8ueTcB5vKP96H5bGDZGIf5gJt_yfMxUTZzbVbtpOPWKUN81zoZQfhZj9EkNYu8MsxgSBjpHhKIM-Raw_gYOW-hIAS7gVuP6kEdYUIpPbC6PPtdg5WrE2WiunCsyuzT2ivJatJ_xA7rOg3JI389IBKAjJdWxg0DOCLaHIvCPGBO0tOOQ5HuPu-FdNoGHQFXb801WeIvs-01rHqR2d8wSg0XVD-cqg5wFjDooNSMLtKqSZfHtaASnNqpZQ36qbzMJ8Q1HL_880mdeq8FQB46nPO9SKx82KCCfwY7Qvt9EGDcVb1Wbc97QmL7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b6fb2242.mp4?token=K2d_7A7ev0eSirZFm--iv00trEmak4R8ueTcB5vKP96H5bGDZGIf5gJt_yfMxUTZzbVbtpOPWKUN81zoZQfhZj9EkNYu8MsxgSBjpHhKIM-Raw_gYOW-hIAS7gVuP6kEdYUIpPbC6PPtdg5WrE2WiunCsyuzT2ivJatJ_xA7rOg3JI389IBKAjJdWxg0DOCLaHIvCPGBO0tOOQ5HuPu-FdNoGHQFXb801WeIvs-01rHqR2d8wSg0XVD-cqg5wFjDooNSMLtKqSZfHtaASnNqpZQ36qbzMJ8Q1HL_880mdeq8FQB46nPO9SKx82KCCfwY7Qvt9EGDcVb1Wbc97QmL7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه عده از مخالفای بی‌حجابی تو محمودآبادِ مازندران رفتن فرمانداری و علیه آدمای بی‌حجاب شکایت کردن؛
حالا فرمانده نیروی انتظامی محمودآباد هم با این سیس و خنده‌های ریز اومده بهشون قول داده که با بی‌حجابی تو محمودآباد برخورد می‌کنن تا یکم آرومشون کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70429" target="_blank">📅 21:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70428">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48faea4858.mp4?token=osXpuzvDVoCAW1Fo1kw9PxSZoqwBRzSB6hZgXAkHoiDdomC2Hd-VM1swmb8DkA2PRnEtdac375iLWd_yB6XXgmuweDqsDYhJeRg34COY9mx_sK_jciNSMegXdpFPlzkafYTED2Gcal_Siaa2_zTaNo-KoRlZZHdGe3PbHKd4a0E-SwEB_ylIBG_MmptaGa4kjOFOanQInIex0gtGAAVOZMl3RFtDw_sOJzHRvUVyxaD6bKISzhJ8hOI39gluwUmtPpFmO_eTQ4IuOqA8wpsRbd0w0gFvY2ejr9tM-GUKEg8zeJWRBfkqlcvaOlRoD5x95n5Zr191Ycl2TRZrL2MuXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48faea4858.mp4?token=osXpuzvDVoCAW1Fo1kw9PxSZoqwBRzSB6hZgXAkHoiDdomC2Hd-VM1swmb8DkA2PRnEtdac375iLWd_yB6XXgmuweDqsDYhJeRg34COY9mx_sK_jciNSMegXdpFPlzkafYTED2Gcal_Siaa2_zTaNo-KoRlZZHdGe3PbHKd4a0E-SwEB_ylIBG_MmptaGa4kjOFOanQInIex0gtGAAVOZMl3RFtDw_sOJzHRvUVyxaD6bKISzhJ8hOI39gluwUmtPpFmO_eTQ4IuOqA8wpsRbd0w0gFvY2ejr9tM-GUKEg8zeJWRBfkqlcvaOlRoD5x95n5Zr191Ycl2TRZrL2MuXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید ماساژ هپی اندینگ به گوشتون خورده باشه، حالا چی هست؟
بعد از اینکه ماساژ صورت گرفت، آخر کار نواحی جنسی مشتری رو لمس میکنن و ماساژ میدن، تا ارضا بشه.
حالا با یکی از خانمایی که ماساژ هپی اندینگ انجام میده مصاحبه کردن!
میگه هفته‌ای ۵ نفرو ماساژ میدم و از هر نفر ۵ میلیون میگیرم!
یعنی با روزی ۱ ساعت کار در هفته به غیر از پنجشنبه و جمعه، ایشون ماهی ۱۰۰ میلیون درآمد داره!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70428" target="_blank">📅 20:32 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
