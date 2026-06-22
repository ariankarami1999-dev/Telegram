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
<img src="https://cdn4.telesco.pe/file/QUWrsBeVcezt6XZnOhlTFVmucaUn_uuqX9SOtZjfU0d2nV4T63JPkL6rIBdEZhcPoo1sgEOEcumFFtCxW_8FnHJ592LHjvefFUog-1ealBabOiyovNxaNCrlUZmek6_LWiAE5LKLfWEUq-tPSwpZiANcXbC2gTX7l6WerGDtrjwYWn0nRU2E02wp5deYHfLqJQorwORxiQDic5Sm1syQLuz_LX_RY1yI_-CqLTG4SXGaWYYIUME0xQxaBCUqp3maLeddz63AurkRTfcYXa4lLkJb-kYs1UjHWbk139AGEoeMGGRyNkqxOvE4SX5RKWrL_6KmWVyiBk9-oBijSxN1WA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 220K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 10:42:50</div>
<hr>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372418cb00.mp4?token=v89IeH0mYtWD2A8PxmBLTbN-UrF0iONGkyjo_02mwpqSTvXBjgP5XjaQ7PO0JWtq7cZHb67hzHVrjEfVBI_AyEsZwLRca0P6SVWFDQ-IK8PsNsvkf9OhSFViLVrSQWqwq-SMMId-17W9L-qvPehKxDa0A7eLmQYx5nKAypB5t-HTWENuKvmD8xrt1t8aZuljaF06NveQKDXOsIz_e-iJ5v8ECZF_LXkG84ySW4FA4za-E-ZNx97Bi12ShNbFvmSBQhijgjbxhbnMOz17WWqat6y-MFI1JBMzQXv7kSH7eUYPTPsn61XlUFWfVA6vu9a8ShnUomVQo8UYgwPWQh164g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372418cb00.mp4?token=v89IeH0mYtWD2A8PxmBLTbN-UrF0iONGkyjo_02mwpqSTvXBjgP5XjaQ7PO0JWtq7cZHb67hzHVrjEfVBI_AyEsZwLRca0P6SVWFDQ-IK8PsNsvkf9OhSFViLVrSQWqwq-SMMId-17W9L-qvPehKxDa0A7eLmQYx5nKAypB5t-HTWENuKvmD8xrt1t8aZuljaF06NveQKDXOsIz_e-iJ5v8ECZF_LXkG84ySW4FA4za-E-ZNx97Bi12ShNbFvmSBQhijgjbxhbnMOz17WWqat6y-MFI1JBMzQXv7kSH7eUYPTPsn61XlUFWfVA6vu9a8ShnUomVQo8UYgwPWQh164g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسماعیل بقایی:
با حضور میانجیگران، سازوکاری برای تضمین و نظارت بر تداوم آتش‌بس در لبنان و در تمام جبهه‌ها پیش‌بینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c83xDXYIA21kdReHwriwlAfCE0PNMwVUBqWVZbAEUBKG16ZiTfw06w6ns2Vt9-DNak1Ac6OM5Fz_OaUywSFfwnw8tNoTybBx4hhbRHF1RWNkKeLQUeT4jyify5kwJtlkVU5AmGRIXDxMKLkGYD_daWLS_6Vli1w2OKzVhnYfaVLhneM_qRWIrWZFFkD0kemsXoj0GSmCL1yKXNzNnIaLcQdldhiduqI3qG0b31AvZEXZaUoP-3rFHCU9t0VQvF8FZysTXx7XoSe_lhVuTL_DuuFNLvBY6nRKVibuDCkyhCBV8c3PlGWdkZ3xi_UUXbRPcbzURoprkdW1Go9l8qgPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmbIsIUX1ruFrB2f3vnuPGVtDFthWDmBybEC9RUuAQH5nlPbOF-nm-7KMuvZ8L3V_jSG7Xecx0n71dEvMGIzoF3dLZj4i6wZlRmvntLioaVKzP2dabO2v-WiGoQfmCIhKXr2OJIyXm0B1Gg9zSq7W69bCymY5QUxHIN9aSyAfVGHf-1ZBSh8aKXUbiEiWNKF5vj_1fvLE_Q2Adoj7YXUT5K0jDY8YANOXUQHR1no_op-fyaQ_3ypVcCNOGE_LFEItfJUljMqOGz57W2XX5UBGp9VViidX3z4uZx7eUaZYDE-q2hWBvgf9ouzuqsfNZbcK2qjLYpXLste4P9hkzQFLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bXZ2pfFSYBiWOzWhAXpPV52DwZF4CcrQx7CG5ue-A8g4vTZmt-tn1eYld15UL4is91LVrXDG1-B6IkbUmJjma2HB77ufC5IpXGQE-siTBkqSbPCVahI4s9wGCgHjVYX1625zUtxvEVJiUIpkPn06EZjSJBgZqfbjI9CJ652VDQyd8l3m0GKFk1wMmXUdUJN3D_DI03IoSrj7o5tSCMExw2eXT9r0s08dFs-lTWDFWQolZ9kr55NrLkEwxvw1prQjDs2Exw9Eha1gmyK2VINGJ12t5P3XDpBZnqaaKl_pR-aGgEJit0bo5y8C5q8P0hOd0VL6lchJ1Us6DzWHrmPzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxT9xHgroECRLmhokrrkXcMFsLzz9zmWASbaXhAh5SEaud5WIZgO0dOnvMbc9zgcdkAskbzaWCYmAA50fNVqKNlvKCfkJ1vqQ129Zmplbvq-x7mFevlRRX1BxPy4EFtqK5ytjXIz_E283YJt90xewnwk1Lp-5b76l42JlMy2rAK975DjLPvA7XgInihub6eHWkpJjGHTGaTuF6CFmP7mqlobGaQJtR21VTOsPdogl5ooKSdkJwzrhYf8Hs71fCAl7fVQWclVPl-gAPyJqYMdNdgQV_ySOaOpUUK0EVH5tEybFC6WJlBcEwSF1XTapYlrCNRcOdYwu5LK8DYPBM1WGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwjNRMZrqccY4ATQNLOWknmKFnoT8R3-TWmx5t6dk5hPwbQ4QOk6YJkEq4AqrlHkwzhiqLHrR27GccWdju8SIRJ5jyB87IR1vkAk2xVSfUL6zuWtKNAPTkj2r7opn4kCifkY8LjOMma7IIVGOisXuAiHDjHbArUJrsYcjqGd2y6QVWVeERlGpHkzGhvpfDFUXAeNjH0CRtUHYKWiGurOcEL9es0bYX0XCcl-mm1-IqXng2rC5g9qTDBfsxzU25epAiQhVPC8od7yUdA6Gh9rqea-XAktBCPOKdP0fwXkFZ6_8_G5Fkb_oeQ17kOs0uAI_R8pQjP3vB2GKT9OQNgZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=DowtIvwaJ4vmBCC96I9f2qTQZmmIDQ8dasbMJvUlkDjTFrxWXWMFih2LhFsLk6dHLhjD3SOPEVd7s4FFvEWZnvXU4EOldhMaRgsGidOcJiHgD8de91VFZXQ9swopzB8Fn3RXvDso__qpAGv26nmDF8IvRuEOJtOZgpAYqt1VnzpFntWm5E5XLx46CWf7uvbroBT-zAgx3eVRut1UagqpSe54SqEsVtSdq1BzY6CUC9XFdZIY162m8BO2-UbrlUBF8TVSSl_3Rg5vt_sYf3isb4Q6a4nXenVJpNFvJoYQtI_h6WXBKHwCY1q4sf9L7H7K8zwLxxLlSI-RGv02zSITLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=DowtIvwaJ4vmBCC96I9f2qTQZmmIDQ8dasbMJvUlkDjTFrxWXWMFih2LhFsLk6dHLhjD3SOPEVd7s4FFvEWZnvXU4EOldhMaRgsGidOcJiHgD8de91VFZXQ9swopzB8Fn3RXvDso__qpAGv26nmDF8IvRuEOJtOZgpAYqt1VnzpFntWm5E5XLx46CWf7uvbroBT-zAgx3eVRut1UagqpSe54SqEsVtSdq1BzY6CUC9XFdZIY162m8BO2-UbrlUBF8TVSSl_3Rg5vt_sYf3isb4Q6a4nXenVJpNFvJoYQtI_h6WXBKHwCY1q4sf9L7H7K8zwLxxLlSI-RGv02zSITLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvC89mjNjHBWL6b0vy9acYOsPkSnLXJMexvf_rjkvsEkEXoP85dA_i8iklFuviiEghQSJU2lvl9Gs4QRkETBq_LC5wWY8h51Tq54CHyHJvtk-XXRTFckrtvAqLqE94N-xPSElXluhTwkxWiu1fkaTUYp9Xe8X8LMWt7SO39BJEaVuaXyvrL5IjOt7_JvfhtHrVklgN6sUjqrLNWWjG75kA5mPxi0bOg77-47LfXsRLcwS2e5FLR9GE7fsMr53zEbB0SjmDwYkP4WjA6I6WM1eh4Bz_n7TT-hQkLjbrTfm4p_uZig9-HStjcPx-Nv1GWCkswQormET-kwwwku8GsYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66651">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">طارمی گل زد #hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66651" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66648">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">طارمی گل زد
#hjAly‌</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66648" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66647">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چقد خوشگل بازی می‌کنه بلژیک
#hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66647" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66646">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WA79S3C3Nzw4WQlSxmncMLarR8LqwdpkbyPGVLIat3GM4ERM_JbvhqPV3rlz2KsS8Te1uXx2jjr3fd34BvZ73QHmDaXJG1E5HEN2KycfXMxAqhsw0TKZi2R3ByUQG_ldUBB0GfLTv9WbaQ13u8tgOI4ciQkN2OaHek0wr_JxlucgXUJvpZ4Y3u6s1GcVF7ZFVE8jcthP_bazq49OVlH4Jf15fR3AA8GPqzup_Ta3M5Jw1_QYUFCPSLIOUEtiDTI9IawzgjJttjaJKg46f8qSESniM4UNII85-ercm-eW20ZfpkjQD9o4fCjtF09KXmOCQlQagWobuxJRDA40DW6Rkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از نکات فنی قلعه نویی به تیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66646" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66645">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=MaiWUiH_SI70sjb-K8g0d-UJCsyqoiLFDd5_SojLzqPRnW3XuTZhGzmCWRC1495MWy_2H_3xAI8z0Yh8UfnzpTQ4wVof5UZeGDNobp1o8bPzhTWKVGLejbtzkqvaIvYfm4SXvwumFElHCC0jyLJr1NAUDuQBMq7h9Ss9MDUJXakjgdMRCvvPKI0ELk9EToUmoqUVEOPBkzlHRHaM5T3jjhUeUazm1eNg2G2khQGn64mXhabzH2LEg0fJghMEwXenaBg3fi2H4qaCTDsn2KS_PBy3JRbfX_fpse0KmuVdrJgeMtYMlcuyC5MjPadcxnmHcWh2AHTzJYeA5IUquSP06w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=MaiWUiH_SI70sjb-K8g0d-UJCsyqoiLFDd5_SojLzqPRnW3XuTZhGzmCWRC1495MWy_2H_3xAI8z0Yh8UfnzpTQ4wVof5UZeGDNobp1o8bPzhTWKVGLejbtzkqvaIvYfm4SXvwumFElHCC0jyLJr1NAUDuQBMq7h9Ss9MDUJXakjgdMRCvvPKI0ELk9EToUmoqUVEOPBkzlHRHaM5T3jjhUeUazm1eNg2G2khQGn64mXhabzH2LEg0fJghMEwXenaBg3fi2H4qaCTDsn2KS_PBy3JRbfX_fpse0KmuVdrJgeMtYMlcuyC5MjPadcxnmHcWh2AHTzJYeA5IUquSP06w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
ایرانیان حاضر در استادیوم لس‌آنجلس
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66645" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66644">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
سال‌ها به ما می‌گفتند: «شما نمی‌توانید به خاک ایران حمله کنید.»
بله، شما می‌توانید عملیات موساد انجام دهید. ما تعداد زیادی از آنها را انجام دادیم. من به بسیاری از آنها مجوز دادم.
اما شما نمی‌توانید ارتش خود را به ایران بفرستید. ما این را تغییر دادیم.
ما خلبانان شجاع خود را بر فراز آسمان ایران فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66644" target="_blank">📅 22:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66643">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در نشست بین‌المللی سیاستگذاری در اورشلیم اعلام کرد:
در ایالات متحده می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد، و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد انجام می‌دهم. خب، هیچ‌کدام درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66643" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66642">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=VQVQ7p-lPUZwAEGGaMYkvmLi8Hw65c57aPEmn2DjDjfBwo9sUkKdkCaJrYaodESJrDDz3CgW0KVB604xfnLpCBMjHZrL29cFo1uXIiMTmzvh10yHySs4Srct49_sI7CPFTDBM-CGARkYgAcZgiE4nbxUiPQa4QlvL9icp7nVgd90BFaxQfd3ykB73Hp-YdpzG6svflMFUqVFehPU50usTGe03nClIR1IqOHbOPthHHAwc-l7mfkQiTTuZWA-RM0puzZWNWgWBkAN5XEVOudoXparrwxwHhoR1eVUUH8ygOHWeAchm6PuuAFpKJjzubxeHZsLXQrYhuLxhd7VZl2xOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=VQVQ7p-lPUZwAEGGaMYkvmLi8Hw65c57aPEmn2DjDjfBwo9sUkKdkCaJrYaodESJrDDz3CgW0KVB604xfnLpCBMjHZrL29cFo1uXIiMTmzvh10yHySs4Srct49_sI7CPFTDBM-CGARkYgAcZgiE4nbxUiPQa4QlvL9icp7nVgd90BFaxQfd3ykB73Hp-YdpzG6svflMFUqVFehPU50usTGe03nClIR1IqOHbOPthHHAwc-l7mfkQiTTuZWA-RM0puzZWNWgWBkAN5XEVOudoXparrwxwHhoR1eVUUH8ygOHWeAchm6PuuAFpKJjzubxeHZsLXQrYhuLxhd7VZl2xOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون ایران،جدید در مقابل قدیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66642" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66641">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hk-2VV0yp9dyjqwhqbnYqIpg7ek8nMTc7qAItbbzKAe9cWA_zXL8T72ypiPHJ_j-OoLNpoOvK4DGcA_yYIGYpEWKxzdyl0unaN1_xkjVmfod2r9JEyeVIBsDCg8xEE0vxRq_cQ-HOwB_S318yNm3rnv68uJHG-xyTBu_kFD-zWidttZ-d6TVmyjbNtw_d8glAhpBjnIvbYMnAbgogAmpH_R_zdR94CNdf113T5YKFLJcaPD1oXLnFkhVnkyE6DLRSVzk_5vgIOxA4xf1ykqduxpD_o3k8Ez14qBoA3fI4ZkkfIt1mNraQQpFaNg3GaXl_Af1Q1wPAa4wsXNtWx01lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
با صرافی ارز دیجیتال اوربیت از جام جهانی ۲۰۲۶ جایزه بگیر!
⚽️
🔥
سوپرکاپ ۲۰۲۶ با جایزه 4,000,000 دلاری شروع شد!
‼️
بدون واریز یک دلار، رایگان ثبت‌ نام کن:
✅
وارد بخش Super Cup شو
✅
ثبت‌ نام رو بزن
✅
کارت تیم‌ های جام جهانی رو جمع کن
✅
الماس (Gem) رایگان بگیر
✅
توی مارکت پیش‌بینی شرکت کن
✅
جایزه بگیر
🏆
جوایز جذاب برنده شو:
⌚️
رولکس
🏎
پورشه 911
💵
هزاران دلار USDT
🔥
ویژه فوتبالی‌ ها:
با هر گل تیم ملی ایران 2500 جم رایگان دریافت کنید
💥
نکته مهم:
این جوایز با قرعه‌ کشی نیست و هرکس به نسبت پیش‌بینی‌ درستش از جوایز سهم می‌گیره!
توضیحات کامل کمپین سوپرکاپ
همین حالا ثبت‌ نام کن و یکی از برنده‌ های بزرگ جام جهانی ۲۰۲۶ باشی!
🌟
https://www.ourbit.com/register?inviteCode=OurbitIR</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66641" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66639">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ax-QUg7OGVpwH7PpObDtSJ3XbyAJuYwVexNmdGUmcDtriEkKf-3UEP75_iLfg6yEWg_ufFwdVll2b5YOgrJIoMi4Nenjkyf8d7riHfg1qspc8DAKQThqPGYe_2d6YekmOatJJY5zRmD2vJjQ_x25W8k3Z2A1Qg9KYdIgfO8HPZe71dFAzCnibnsYnoYMHCLly4QOSxyGnKXKKCO9aE99rKmeRO_YsCboKa7eZoBdS7d_BJ03z4-ddg2voVFYHRJDDg2diPg12Kz0Ehw9jI6lQC9LZOlcVlxM9bkvMkX_oChcW28A7Q27bT6RU_RSlp_gsXodAko0AgBJ6KNcKo4DUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAqrlBkZFz20jIy6xgc7RLL2xxTUx3LjegpXPTdCpDcgJkv4z8VGE29NJRyBUU4tfeJOxv35QAgWGRRC-D8zo8BAzQAfKGXzwTHnaZ4qaxCDVF3dxrp0J1t5Z6ZwOwl_AinJdXq8uW0cyXs60SA5KLKGRNPKBN-Pu46o7R2M8uyjfD8o4Ewmifvgalc4vSGjX92Z2MDq4QUIDR0Axi39dJ6s1SvfMlY44i0KAy-l1_kPgMEA5hmfIK8qNDzH8Om-a5C1ayrl2t31XW_RYpxPvO7zS5ETL2p3xHX0V7ypn5PhNc9np9huJfAy-f4i9hDsZzvlWVuOpMmGyKV6gYjSfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن  سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو بدون سانسور رایگان میزاره گفتم اینجا هم معرفی کنم…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66639" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66638">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSVCI83VVBV-QYmeBgfDLAW9t9OnqKF3uE0dI9B0jFDXFeW2fzOmvWKqtGtunUVdXNx2dmelOghoOCYQrFBVj6BtWEvUQiqmNodoZnHUl9pTJJHuj4BExcCKiW3KJR8MknCjgvB6QOV1JpKBQq756rHNfJX1spgxJGbl55oqkw2L3iAi2EJYgbhGwP_LVLLzuszQOqnv4U72oMNND4CNvgpHRx6lHDPHTec1Qyajuazkf0w21OttlVfqnwqXM2JD8jfH-AuMTZEfNaDxWz0td5i6PaajZk3mRPcztTy-OyAIdxjwpCrhARolqMcmoSUzAt3H2nl-tz8UkUc6prJ_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن
سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو
بدون سانسور رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
chosefil.com/fa/programs?utm_source=telegram
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66638" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66637">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT-ASgFfBaM3rYL7hkCXckLb9Q7f-ROzeGwbYu5VP1FNdAHrXiyevl3DiyVUWfrgIC92hrAWqTxgB_mRI9b0JMlt5SyUg2O2R-igqt49GpXqRiD06t1_jLJjyVT_nX6PpNB7yJ3w_C6cQ4KbE7Au9INqirmiCdi7Z6xxW5VAOt8-IyPHZsSSZrD0N6Wi_0J_--6pehlknXt44kt0rX02JyO6K-e_n2gEcwdyHTbm4vyl8KuFLBefaXb40Vm_pC5ZZRJNuAiF6VSowTxVhPrr9NwBW5dJ1FdTTkks-FoCZ9SzCm-HUzB4KCHNLwXYr8caiH6zz2yAbq46Y-HkNrh-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
یک دیپلمات حاضر در مذاکرات در سوئیس ادعا می‌کند که هیئت ایرانی آنجا را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66637" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66636">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqeVdocc98gkMjs9mOQ8Ko1lSfEiIOLK3omaBv9biAriorh9XJh4xEf_dAS1AZehX8_JutyVFjkx0-nVaLe0R3XOtUI-HQVN_297V13vy2HyS8wyln1H6v1TBTGDQogME7Yo9sflkFWXfbHqc-GO0luS7ity57t9AXNlr7LI_qACsOs36FZmJnnYp8oOMrSTHeMKwqaQmVP7-NthHP68eOO3EgQRmtL7wYy1U1xnJmlBZuxlQaFMfeHjYhte7QqX79fBKvNFg4IdAbd6-6a-GYn-eWmYZ0ApYSjiOEJ8Gs5s8Xl__UoEK9H52nD4T5YhTACLQniLGJ2aoTOYCiqN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
نتانیاهو و صهیونیست‌ها در آستانه نابودی توافق و اقتصاد جهانی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66636" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66632">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZim1s9cPFQfE4vyVg2xqnJbsMdfVgpg5sxyXED9sTIODagMCSrouBbHYLWBcgy8tAWGOZNpQHEuj8Yxd4tjg9UBoRNILJPDSbit4HJH2jHxcNmcio1OJg9FmP_HG_lt0qX1j7ohvP8l0J9Zp3VTFwgEWyvORWAkMppwFWvpEga2KmeVsIJdZoYiGkvFYAHK0tgJI2wih1ixkrF48kAXYJNi6xv4iDFMNlo_KY0gwVFI_8D3Lc2fVg6ejD0OSXjRYeDyGUjX6O3kVo4vkO8JzFNnzBDcN6F3i0hp7FkanN6PvGgLqbtb3hQIj_n7JH3n85h1ZbqskJO__zIJu-KOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzZ3exCfLqf3TfXWSaXM2D6wexjWxzU0-X2ulDwYjfiwywx5bY7Yn5DbIZ9yguR4-6buMyLRZU_NVPxW4fLHExMLNe_GIP9dXVxCmxah1qxYMA3MkmDU6Zok_W34s9IMnb2b7OewlqSf01uSqBPyL4j1CZTk5dPf2crsTsSLeWKj31-CGXQeFIFPLADcnt0pNRyfb29fk8550dPXKwGO28xEd5jYihNKpq4VOxFZcgJpGXbeLcx_0uCl2P5bdYB521dMY21KxLyreR6AhXOp8FpEuPA8ZGNQn72Wv8wWd8mN8P8NetwZNGyPGg-6r96XrFZK4Xh28-b3Abybz2a3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAn0oQeFrM-BbriUKHF1m_eO3FSuXXfQ6hKUZmXZMf08vYbxGZCeK23oPZ6t6OkN93sRL8bXl4XbRiFooi67CjhParJQBdF3R19JLjXZvgKj4BACyC8s37UujkQtyIK4k4fVAPdVjevNFhB9Ht4mkKj1gZ_k0YLo8dpiY1rvC3H0Ykth-ey6ysR5RulZo6Ak-pA3tWUJEgxFSC9DSkZlP-O6PN5sNp1iDcuWjlgs5zIGJF_c-rhxdtZiIiQ3iLz-RvRZ2Ys0aeAxDL9Wg7zNqGAPybos0nzdYAcDF6w1AYr559s8TBrso6xUI9HvTI48Usgsd3XZp64ZwKUtVhcjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vAqmHJOHK2yxii53Z6SQeajDrreWb4I7-hXgCW2L12kjLKGa3YJV6H8HCZ8PZ8PH3Wumloywzu-v0UjAefygXLkPNXv0EnSM1MQQCsNf7J3OG_mEdZZNhMC1U8q6UB_UAG8GCUVrcyms-K57V7q-WZlg6ttXhJWNgFAqEhmsTYQv22TYnahwtGqoasXCv7s_t61TY0C2lAFSBWyx3luXTwtXYxWgrr8g3xaRBMkMighoNqT6I11BYSguhMJ3vhFjMEeU26_4ED8Z-jR_ycWKYyBPTUtYnnxsD4yBCenpf8rABT4CikXR2pu-Po2CtJQPRzLToaqnimt8RGOiAPZtpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
گروه تروریستی حزب‌الله که در زیر روستایی در بالای تپه‌ای در جنوب لبنان، تنها چند کیلومتر دورتر از مرز اسرائیل، مدفون شده است، یک «پایگاه هوایی» زیرزمینی برای پهپادها ساخته است که از آن هواپیماهای بدون سرنشین ساخت ایران را به سمت اسرائیل پرتاب می‌کند.
مقامات نظامی اسرائیل در جریان یک بازدید رسانه‌ای سازمان‌یافته از این مکان در هفته گذشته به تایمز اسرائیل گفتند که این تأسیسات زیرزمینی که با درهای فولادی عظیم ضد انفجار محافظت می‌شود، در دهه گذشته با کمک مستقیم ایران، از جمله برنامه‌ریزی و تأمین مالی، ساخته شده است.
به گفته نیروهای دفاعی اسرائیل، این تونل چند صد متر در دل کوه امتداد دارد و به عمق ۲۹ متر (۹۵ فوت) در زیر مجدل زون - از جمله زیر یک مسجد - می‌رسد.
به گفته ارتش، در داخل تونل، که به اندازه کافی پهن بوده که یک وسیله نقلیه استاندارد بتواند از آن عبور کند، حزب‌الله پهپادهای ساخت ایران را با استفاده از قطعات قاچاق شده به لبنان مونتاژ کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66632" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66631">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66631" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66630">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urzK5RIcLAaUcITL_riTnTPtQuyi5ym02vZTElNkV4gTxImD4GpVJHRHXF2xitDG7hAxaZWcd7V6HZehuFVJMRKLgD1afvgddRbaMManUwwqqUVFxKQ2VPv-xFEYQhaBwZ5Is8mltAwhanYhL0ijpn-stizZ18HHFJ2a7hYU49pQNMb9ccjgfZUyt411ib1XGpMrLCEibJkTEMvUG9xGJ17SwSfgohOTQneWADQTOHVQuq1HOobTT9jB-3GIpqv2wp6WuutV9YmuEWxIfzJ_HTnpzYUYjbcopQlu_mVrR_xW_K347c_unjSpoAqvs80I7cGF2RlWO0lwhe_eNkjKiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66630" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66629">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
یکی از اعضای هیات جمهوری اسلامی به صداوسیما: «اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66629" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66628">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
قالیباف:  خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم. بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند،…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66628" target="_blank">📅 20:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66627">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFjqRt-5tuKiwN4jdjjvaCs4RwDa5jCyCdIWngKuGmegb8Se002Bzf6LOh56hBbpDWHDeDI6h30NgAwmH-bVdxZO9tUth-OES_s-E2E1Knh3v-xOVLUcb-cfPTVVhznhAUg2Flu6itVEGvGrtYQHO6af0ZiWzrGdc3sawe1dG2QLy2wrVV35eOTOgN5E2ZCOMfoZg4UYmAfm48X8905EXMLRewAqRNlgcRCcATQ4iryi6asyvLypAto1FR_KHvDsXR81bTOn_7UyRuDSXbU32e-AUwhXkC_guR3OicyQhuapLxB288UpcXBPbHBFL59vO6UOrA_ADQ6VlmDk6XcScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66627" target="_blank">📅 20:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66626">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛خبرگزاری فارس:
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66626" target="_blank">📅 20:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66625">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75671dee37.mp4?token=MkmsVmfzJGMLKwAppySTQz_v_pHjlCGI7g4RdzIZQ0r2aaEqL0_4dnli3uq91GkX1biyIHSW7m2vGdmlfT3hlm2TdZBhZzaEmn35eCsWOhGGV0nblDXUM8J7KorPRChSUuYktw5T5TWlULeu-qodCgZmiKUhIttAoyZtnMfciD6IdCH-9evYblQx1nGS8WdW-tN7rQeCxKTLBrFXl2ublYEy07SZVyUeO2a7wA0t6cnxaaQJxHuZHUq8MIJNgyG-gUzJyRPk7SrcHrLGX9yoS6IqHg4rff5Wn5CTx1eSX5IQE7_gLBwrwsVXG1vo90XNIosCt0G_E6OrgiQez9FWSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75671dee37.mp4?token=MkmsVmfzJGMLKwAppySTQz_v_pHjlCGI7g4RdzIZQ0r2aaEqL0_4dnli3uq91GkX1biyIHSW7m2vGdmlfT3hlm2TdZBhZzaEmn35eCsWOhGGV0nblDXUM8J7KorPRChSUuYktw5T5TWlULeu-qodCgZmiKUhIttAoyZtnMfciD6IdCH-9evYblQx1nGS8WdW-tN7rQeCxKTLBrFXl2ublYEy07SZVyUeO2a7wA0t6cnxaaQJxHuZHUq8MIJNgyG-gUzJyRPk7SrcHrLGX9yoS6IqHg4rff5Wn5CTx1eSX5IQE7_gLBwrwsVXG1vo90XNIosCt0G_E6OrgiQez9FWSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام:
من روز جمعه چهار ساعت و نیم با رئیس‌جمهور ترامپ گذراندم. این چیزی است که فکر می‌کنم در ادامه اتفاق خواهد افتاد. اگر این توافق شکست بخورد، رئیس‌جمهور ترامپ با زور کنترل تنگه هرمز را در دست خواهد گرفت.
ایالات متحده کنترل تنگه هرمز را به دست خواهد گرفت. ما برای همه کسانی که از آن عبور می‌کنند هزینه‌ای دریافت خواهیم کرد تا هزینه عملیات را تأمین کنیم.
و ما در سال تقویمی ۲۰۲۶ توافق‌های ابراهیم را گسترش خواهیم داد. ما عربستان سعودی را وارد توافق‌های ابراهیم خواهیم کرد.
و اگر ایران کنترل ایالات متحده بر تنگه هرمز را به چالش بکشد، ما آن‌ها را نابود خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66625" target="_blank">📅 19:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66624">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=LdfqZi8urn7H2Ks_NUc09iDQugJLHONthzJKJ9xk6kHGRKZJAVc8my4beEdKCWv9TZUCEfyDNmjW55aPvwsohkhycBNASZYKfYwUjQRjYRDJgiWVHqJ2Nr4gcFe_QGXG9rrghEZloJUBJuqOhawRqQCpi-zsWDLBa5cBhdNuY4MOzCVndnMm8SHWU884NWXST4KOQjmOPI_vJyHeHWTQPZUeD63W5S9pmerA8QP0-HdEcvMrcgu4MOOWTDRLVhQ4nN3G9GFtvfAyyXLNCmDOphvAleJ9dTXQEbggqyLlr3cCyqSSSDLmWMwInFTSWqafta2P28M9yjONNM6FyP-txw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=LdfqZi8urn7H2Ks_NUc09iDQugJLHONthzJKJ9xk6kHGRKZJAVc8my4beEdKCWv9TZUCEfyDNmjW55aPvwsohkhycBNASZYKfYwUjQRjYRDJgiWVHqJ2Nr4gcFe_QGXG9rrghEZloJUBJuqOhawRqQCpi-zsWDLBa5cBhdNuY4MOzCVndnMm8SHWU884NWXST4KOQjmOPI_vJyHeHWTQPZUeD63W5S9pmerA8QP0-HdEcvMrcgu4MOOWTDRLVhQ4nN3G9GFtvfAyyXLNCmDOphvAleJ9dTXQEbggqyLlr3cCyqSSSDLmWMwInFTSWqafta2P28M9yjONNM6FyP-txw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام ؛به ایرانی‌ها می‌گویم اگر صدای من را می‌شنوید:
وقتی شما از حزب‌الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66624" target="_blank">📅 19:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66623">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF5cNUd-HWoTrDdg_-CIyK7GloAWiX6peZWTheSJbUuNBVKp4xtbuSUAILj_9Zmv_oiyzftv7s4iI2e_SXDjtcdy9-xdzzFWp4XTzfQ8Lx2lbf-xnXSjk-oj2lE8TzHPCxu7RNCC6Emsxl2Tsmbin6ptyP-IQy7QWBqg3-lS31mLmoWwI1HuuNJynt_6ikC9L7PPryD0bNY_8pNeP7TGsY652lTCf10bn3hfbejubhAIwopXECPtZoS2Wmaq0FPkDzbCzR35AHrknE1SKwL7S9YvA_YGqUQk20-p0ZOENQ_T-txawFYRWHZKopw8zQUDFq-ivOgbUHjwQZ8wGMynsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی اسرائیل مواضع گروه حزب‌الله را در اردوگاه البریج لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66623" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66622">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
رویترز به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد نخستین دور گفت‌وگوها با آمریکا در سوئیس به پایان رسیده است
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66622" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66621">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇱🇧
حزب‌الله:
بار دیگر رویکرد مذاکره مستقیم با دشمن صهیونیستی و جلسات آن و آنچه از آن ناشی میشود را رد میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66621" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66620">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgSL41qaKHghF2ltT5dhISVRgav9Zt8Hm8LVeQmCAJozAP6XbY9DPYPLFrTiq3s4PYH1GYRVd0KqR9GM1BLrQ2hUw_DhVKNttEZTPETqFkccpSK6SBWBFZnf8zOT-8E4D0K1tyk9dHWHjNrJ7WYed1YePyaZnBXnaRVCyHzBGwLPLyPoUl74lOL0Ju4pg50nyqYhQa_w0y1dl4_TzyPIidGkbUnfLZw3aRwYUpcJigeFNiIXAN01fm0skOK_Bt68qf0om92uJ5atC-37TrNfA4hYU6arqAtbgP_UQ_FU356qgGbdn0VCUeF6ph_cuggd8Swor6nDXr4ZAV8J0KTRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بند اول تفاهم‌نامه اسلام‌آباد:
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66620" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66619">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
اسرائیل هیوم؛اسرائیل سه شرط اصلی خود را برای پذیرش مفاد یادداشت تفاهم مربوط به لبنان اعلام کرد:
خروج کامل گروه تروریستی حزب‌الله از شمال رود لیتانی
نابودی کامل زیرساخت‌های این گروه در جنوب لیتانی
اعطای آزادی کامل عملیات زمینی و هوایی به اسرائیل برای مقابله و حذف هرگونه تهدید امنیتی آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66619" target="_blank">📅 17:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66618">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
رئیس ستاد ارتش اسرائیل:
آتش‌بس در لبنان شکننده است و نیروهای ما باید سطح بالایی از آمادگی را برای از سرگیری عملیات رزمی حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66618" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66617">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355294b30f.mp4?token=tJAEbOHvBb0nTz75U5m2aB8vgT9ZvDBVh0AQiihO1O-u9IWyIA0o3Z4-CH_T9D0JOtfkPHvLoSbNHH8D4unSdZWbFVMIGSmyeftAsyMDDaych3Pc1CUUme-OJUA1a2e8-xF2cwpliQUTZXhYlty1eWKw_ejce_EMKWayd9R_L0APxupIrwaG0O3oLJofh239o_sOm2cdtO2jevP8zhHa3vWPrj5NBkIty-nrvZEO5V6VxrQyUuSeEsWTj-IJnHhwVEm0GlRIXb_FQVWH06gZ7Rhsrnyt9zQozUYQEIxe5AW2Snn6dc8aobuT5ac1kRsy1tyMxSoRkNNTwjx-koPuQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355294b30f.mp4?token=tJAEbOHvBb0nTz75U5m2aB8vgT9ZvDBVh0AQiihO1O-u9IWyIA0o3Z4-CH_T9D0JOtfkPHvLoSbNHH8D4unSdZWbFVMIGSmyeftAsyMDDaych3Pc1CUUme-OJUA1a2e8-xF2cwpliQUTZXhYlty1eWKw_ejce_EMKWayd9R_L0APxupIrwaG0O3oLJofh239o_sOm2cdtO2jevP8zhHa3vWPrj5NBkIty-nrvZEO5V6VxrQyUuSeEsWTj-IJnHhwVEm0GlRIXb_FQVWH06gZ7Rhsrnyt9zQozUYQEIxe5AW2Snn6dc8aobuT5ac1kRsy1tyMxSoRkNNTwjx-koPuQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منابع داخلی:
هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66617" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66616">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18DjkdyA9hWGcApghostcCWyllt7NZIz9EWM31NLYQqJA43HyO3PjHbumBON-rX5nk4-rDCqGwvEGCACZ2heSdUtQ53C0uJlbx826H-oGaI8uyLQtBPBahlLgQac8o2O8-Z4R7j34MRo6H49u9amkltM23TQ4z2V5PtHOiq09_uC4KBKmxYAFEO1O3lwZPMHzceWqZQ_QyRMZ0NWqe0JifjLG6APmFc8zbqlbYL-7e8cK3tCgzX_ZRhaaFmiB464OaI9_Q32QUxzmY32bR-4oAZsRtK_wjnMWnSpQK-owRY6EoHS-yxnm-7C7tNdT6fVVVdbAPAcV5ZNx0Jpi5T1Ev8ZhX6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18DjkdyA9hWGcApghostcCWyllt7NZIz9EWM31NLYQqJA43HyO3PjHbumBON-rX5nk4-rDCqGwvEGCACZ2heSdUtQ53C0uJlbx826H-oGaI8uyLQtBPBahlLgQac8o2O8-Z4R7j34MRo6H49u9amkltM23TQ4z2V5PtHOiq09_uC4KBKmxYAFEO1O3lwZPMHzceWqZQ_QyRMZ0NWqe0JifjLG6APmFc8zbqlbYL-7e8cK3tCgzX_ZRhaaFmiB464OaI9_Q32QUxzmY32bR-4oAZsRtK_wjnMWnSpQK-owRY6EoHS-yxnm-7C7tNdT6fVVVdbAPAcV5ZNx0Jpi5T1Ev8ZhX6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66616" target="_blank">📅 17:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaOFJaJfh37cebZhpqSXt-xY6nxdtv84EpoY43BZ2iBRnSMmIovMZGRXvwT2qiYo5Cyseoxva4DGI47kAwT_u5RQr-ASkEAlLPrDWsKBxZ5YcNCHz3bpPcIVCPH9DG5Sx-nATlN52Qr-0EOdhuhDLJo37VKSr6BOj6gua8L0yITNISUNGuhRUd2tu-XV5ZwermHrZPG_3HGMfk_kdWLgRCaBB4n_mB3yexZjfoTQ6tlDfpoLepasfY_jSkjwF8wV4HOKeq15ZJ0HrhLnAKKxOY2SuEapIK0zP2r8H2p7WoPANipwFJMXM8gSnHKrWRNcq17gvOLjeyeiiUNJBrPXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66615" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=LAEetlFaO3ARjZ0CEFvjV1UH2WYiYJJxJv6ObqDlN17TXSpyvfcbVIVmqZBOjsHPuwiWpHXp5jSGAoDlskJRhviIJ5TEuX2NKuHZgCpAVVhDNnL7QQJANm_B5T7tUMrHKF7kRW3KqFL4f79QHzXBkq5kHucWWvLVM9WEpnhMeFZJ2Ys9dnTZKXuDQeHlMeV_Ut7R9Trk7ylH7Q-H72jtUPOcrYcCm37OuGJWKbQTn5Ve8d6RjQXgdoX9FWehcWzr5h9ZSL4gjViXLptEYhsVRYPKM0OP0qk3WMYUoZm38GFDdP94Ze8Mr2NG5pyNZRr_ZhVb4I8NaW-p7LBueRSO7Udq0Q_HTf_Am0WnwI1HIjCTt9SZ4pKNVMHw7Z3BgmrFGt2CDh9WDo32aJ5h5Ca6tAHmBHcdS8nBqGOMkca9umCftjPxBbUpnoXcwGDDqZN2-pfABY771bbdLaayAUx8XDTEidacB92EDAe8n_HKkRJtTb7U5ibEoQeutPKwx68uFyOIvi8re1-beI2X-0-K6fdEd2iyGGr5bMMGqGSQpWWrut1PjNUyxvviSy9Uh_qYqUavWKK6ABqSsMCKeX1jQauWvD78ew_ZK_Zft-5iCbcZaCnanasdhy8rIiTy26xw31_DkeF07QNhA2bFEv3x-KMs9X8gJCteluuAjZgeYos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=LAEetlFaO3ARjZ0CEFvjV1UH2WYiYJJxJv6ObqDlN17TXSpyvfcbVIVmqZBOjsHPuwiWpHXp5jSGAoDlskJRhviIJ5TEuX2NKuHZgCpAVVhDNnL7QQJANm_B5T7tUMrHKF7kRW3KqFL4f79QHzXBkq5kHucWWvLVM9WEpnhMeFZJ2Ys9dnTZKXuDQeHlMeV_Ut7R9Trk7ylH7Q-H72jtUPOcrYcCm37OuGJWKbQTn5Ve8d6RjQXgdoX9FWehcWzr5h9ZSL4gjViXLptEYhsVRYPKM0OP0qk3WMYUoZm38GFDdP94Ze8Mr2NG5pyNZRr_ZhVb4I8NaW-p7LBueRSO7Udq0Q_HTf_Am0WnwI1HIjCTt9SZ4pKNVMHw7Z3BgmrFGt2CDh9WDo32aJ5h5Ca6tAHmBHcdS8nBqGOMkca9umCftjPxBbUpnoXcwGDDqZN2-pfABY771bbdLaayAUx8XDTEidacB92EDAe8n_HKkRJtTb7U5ibEoQeutPKwx68uFyOIvi8re1-beI2X-0-K6fdEd2iyGGr5bMMGqGSQpWWrut1PjNUyxvviSy9Uh_qYqUavWKK6ABqSsMCKeX1jQauWvD78ew_ZK_Zft-5iCbcZaCnanasdhy8rIiTy26xw31_DkeF07QNhA2bFEv3x-KMs9X8gJCteluuAjZgeYos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت
:
بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66614" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66613">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در مورد توافق ایران:
من یک گزینه 60 روزه دارم. بعد از آن گزینه می‌توانم هر کاری که می‌خواهم انجام دهم.دیروز در نتیجه این تفاهم‌نامه با ایرانی‌ها، 19 میلیون بشکه نفت خام از خلیج فارس خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66613" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=J1P8sjHvguvPMZTd25RVPCafFAAHas7NigYNGK--PUC2y2kZVI1pb4OM4SuM_pmYbBY4o4rARHKnkbfSaNkV-i_-0j57i21Lv_MiwQFurqigd93eOH37yb6f2lPJrNo72qO0mjNQNxW15P9y6Z4EByzJJax1BaUjLyCw-UjuMTX16tFTQzKQ4PfuQwlBDDgjCv8Az38pvQoVTChz7UeUQzZBaHgK3PUyp3zo8UTH5F-hx4vnnxvs3jHNzaml_KB5j5rMVgCrQwCVWKCB1z_0cCHtjBbkbHaZjeYZpjoQfJnZNjaBH_nYav9ZjyPtRulWYqsDjTnD6WYXQ6Ua3pKjOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=J1P8sjHvguvPMZTd25RVPCafFAAHas7NigYNGK--PUC2y2kZVI1pb4OM4SuM_pmYbBY4o4rARHKnkbfSaNkV-i_-0j57i21Lv_MiwQFurqigd93eOH37yb6f2lPJrNo72qO0mjNQNxW15P9y6Z4EByzJJax1BaUjLyCw-UjuMTX16tFTQzKQ4PfuQwlBDDgjCv8Az38pvQoVTChz7UeUQzZBaHgK3PUyp3zo8UTH5F-hx4vnnxvs3jHNzaml_KB5j5rMVgCrQwCVWKCB1z_0cCHtjBbkbHaZjeYZpjoQfJnZNjaBH_nYav9ZjyPtRulWYqsDjTnD6WYXQ6Ua3pKjOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی‌دی‌ونس:
باز شدن تنگه هرمز، پایان دادن به برنامه هسته‌ای ایران - این کارها قبلاً انجام شده‌اند.
سوال این است که اکنون چقدر می‌توانیم با هم به موفقیت برسیم.
آیا می‌توانیم روابط در خاورمیانه را به طور دائم تغییر دهیم، یا به انجام کارها به روش قدیمی برگردیم، که ترجیح ما نیست، اما مطمئناً چیزی است که می‌تواند اتفاق بیفتد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66612" target="_blank">📅 16:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
‏پرزیدنت ترامپ در گفت‌وگو با فاکس‌نیوز:
ایالات متحده می‌تواند به «فرشته نگهبان» تنگه هرمز تبدیل شود و ۲۰ درصد از نفت آن را سهم خود کند. «اگر لازم باشد، کنترل تنگه را در دست می‌گیریم. آن‌ها را به‌شدت در هم می‌کوبیم. اگر به توافق نرسند، از کشتی‌ها عوارض عبور خواهیم گرفت»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66611" target="_blank">📅 16:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=sC_ciLa-YF6EMki0twSy4u15LFou0BJtHG5c2VEJzhpxxKh3myt_KFAqWmZ0hzRsgDQrfnKesS8Ivjd0EvF0BZ-ry6NFThUye7yVU5DidtFqVpfGjKAL_XJWXmnJ_0PvEN1EXdQoSvS-hb41wJtqfzJSY9gzE2lAE-huq_TFYVhvm4kC4mNem77jWZBOM5rCyk4IO0HgiPUxaSm4bUSj-MEep0BpwGj1pEDX497RnkDFAoMYOB7DRHIVlbfAKmjaMhNs9O5SVxlrSvy4JT1E7CRbJixTNz-kra5tA4i2ss7N9FPULlpU8a13VUn6YWogU-yjJyOeI70QlCk2kUPULw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=sC_ciLa-YF6EMki0twSy4u15LFou0BJtHG5c2VEJzhpxxKh3myt_KFAqWmZ0hzRsgDQrfnKesS8Ivjd0EvF0BZ-ry6NFThUye7yVU5DidtFqVpfGjKAL_XJWXmnJ_0PvEN1EXdQoSvS-hb41wJtqfzJSY9gzE2lAE-huq_TFYVhvm4kC4mNem77jWZBOM5rCyk4IO0HgiPUxaSm4bUSj-MEep0BpwGj1pEDX497RnkDFAoMYOB7DRHIVlbfAKmjaMhNs9O5SVxlrSvy4JT1E7CRbJixTNz-kra5tA4i2ss7N9FPULlpU8a13VUn6YWogU-yjJyOeI70QlCk2kUPULw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره عاصم منیر :
من احتمالاً در سه ماه گذشته بیش از هر کس دیگری با فیلد مارشال منیر صحبت کرده‌ام.
بدون سیاستمداری او ما اینجا نبودیم.
او یک رهبر نظامی است، اما فکر می‌کنم خود را به عنوان یک دیپلمات عالی نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66610" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=n83mGPNDntKXYhDATWzkvMSk-s77ZkkkH6Kbapt_0PmodQWn-2rfLW5znapaMGMRxSgISvhGhRVcm4ammJc8FfU8zgWQ3rNsosQSkFrqZtzs6a1bKnggIaILqwTzuu77vPHeBrN4ZL9uDDtzcHGXyrBH4eqwF7oAMfxlpbZeQ51T3aDBJIk-hYAlbkhiRZ7V0ARd5upmf-ofGM7LVP4qAH5Q7YCOc4o0w1hbztv1gq0_UrnFmZC87hNin6xiAho1JU751BjEgMRxE9q9_MYm3xMsqrqh50-kWoMZNTz-pDn38J-e3pgeObY1Ef1fAVezwtvX0Dnqb3yfjhiZ3jbUFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=n83mGPNDntKXYhDATWzkvMSk-s77ZkkkH6Kbapt_0PmodQWn-2rfLW5znapaMGMRxSgISvhGhRVcm4ammJc8FfU8zgWQ3rNsosQSkFrqZtzs6a1bKnggIaILqwTzuu77vPHeBrN4ZL9uDDtzcHGXyrBH4eqwF7oAMfxlpbZeQ51T3aDBJIk-hYAlbkhiRZ7V0ARd5upmf-ofGM7LVP4qAH5Q7YCOc4o0w1hbztv1gq0_UrnFmZC87hNin6xiAho1JU751BjEgMRxE9q9_MYm3xMsqrqh50-kWoMZNTz-pDn38J-e3pgeObY1Ef1fAVezwtvX0Dnqb3yfjhiZ3jbUFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: متحد شما اسرائیل چیزی شبیه نسل‌کشی در لبنان دارد. مسئله اصلی توقف این است.
جی دی ونس: خانم، من فکر می‌کنم ترامپ و ایالات متحده برای توقف درگیری در لبنان بیش از هر دولتی در هر کجای دنیا تلاش کرده‌اند.
صلح هرگز آسان نیست. صلح همیشه به کمی کار نیاز دارد. همیشه به کمی بده بستان نیاز دارد.
اما ترامپ نه تنها به صلح بین ایالات متحده و ایران متعهد است، بلکه به صلح منطقه‌ای نیز متعهد است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66609" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66608" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66608" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66607">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFSzzoa_Sxqh3Yk7fmS0IrcZzT8dDrr4rdev7vaAhKU-IHP6yZey7Ne3NTg-UsTOV4c7EO2iZyeNmGPwevERTCi68h54itoOvGYMUpN4KrC9ivE2cMoyIbO8aM09NxcI1rU7jN4wKTD6gQXjfR0f2F6-GSkv-8GME1ulInRAgGuVy4dFyeWwWJ6v7EdAcPPikPqNhKpk_AFbQyTfzrLPCan2JE1W8mNeFjCuZGfPJ7aIwiy3T5UjbOMy1dDjwVAWQu-Qei70btpHKPfhMrWHgCd7O_3f1SU4idP_wVumWKOKYWwXYt6fsu82Rfg3eDD7v1yJRASVK3GnLw61B9hHfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66607" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66605">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuX2aH_FHxs1K6Cgd7v-dgnMniqi3t94onKcByo4xgcw3ixwga0c5sziFHOhki92dXGXisBmde1qJi8-kTUmqNuPJbfQ1iA8ijOrJwSNynnkdQZdrXKQxAWkogUJ5R_Lyl5rsymiLFyvKP0srrNQbdugr1-KKju8EfSk-wnbGK8npfQ6HDesUBK5Vwncs6jW_mqI9SU3rL0kQJnBOPNqSz7YnGUBVSZ8hRlH3wHfAFvQmfgKe0I8WG4OFdC_IvNm8m_F4Ld4DvS-jeF6gEh7jh1yDNZdZYeoTv5p-q7U7kWeIfj0MOI9zw7gaoJLQByxQMo-qnEL_FDO5ri-hLsiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=hodJ1WFSvYXm7H5GeW7Xf9sdOSBEl295KN8WDwVIv3X01N6yRGMrh4hkFfxXm4iEHbCwA6OPwT2htXtQ3NjSrPpDHWubkjrS_ifnr9on7Sd8QUy68mw4ARHemK9C70pFYD6tzP-6yep2VBk7obY8vE9MYvpdZHN6YHxq6Tg1ZD462K63lxAE4tSIC_vpZl_2jyN6A4xI0pxeEazJ1Sm57eAFcLImdy8p1apYYudGUzLx8k3bzxR38CBUS3xcCrMoeAQpcca7BJHsV7omRF1C4gCgGQG1v97qbUkJwuBwBZ27ol8lJmE0QDZNgGeJICx63cqs0GvwDdI3HyO6Nj2QEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=hodJ1WFSvYXm7H5GeW7Xf9sdOSBEl295KN8WDwVIv3X01N6yRGMrh4hkFfxXm4iEHbCwA6OPwT2htXtQ3NjSrPpDHWubkjrS_ifnr9on7Sd8QUy68mw4ARHemK9C70pFYD6tzP-6yep2VBk7obY8vE9MYvpdZHN6YHxq6Tg1ZD462K63lxAE4tSIC_vpZl_2jyN6A4xI0pxeEazJ1Sm57eAFcLImdy8p1apYYudGUzLx8k3bzxR38CBUS3xcCrMoeAQpcca7BJHsV7omRF1C4gCgGQG1v97qbUkJwuBwBZ27ol8lJmE0QDZNgGeJICx63cqs0GvwDdI3HyO6Nj2QEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کریمه در طول شب پس از حمله پهپادهای اوکراینی به بندر و سایر زیرساخت‌های حیاتی
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66605" target="_blank">📅 16:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66604">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=kMUH5npL-0U5NrL9aDvrazl7OdZo2yFt8HPk-60y-6BULu0dpc6lhIfonKWjRvwnLy2H2kAGHLYn5QBbLeD0SkszXUfIHMyimoMRRjZvzLuVkrNu3a8nUdsXZV7Uc2_ciwKLwlyoSuslOh8l9IssYwirg2z1alMhc037Ma6t72SRKNmrsQvSa4gmrBSJWFGJq67_z4wGnLEatGWPdwkfSp0cCaQrjObjtedok-s-vVo-V1vg83hu-8MhLykcLf6nUWTl3lCd3BsTJExKUI2p-KwAOZnFbJfIfXI0YZusl6R_FQYX8W7MA_g_52zRaV548uu97QOqFuHYHWeeyzaEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=kMUH5npL-0U5NrL9aDvrazl7OdZo2yFt8HPk-60y-6BULu0dpc6lhIfonKWjRvwnLy2H2kAGHLYn5QBbLeD0SkszXUfIHMyimoMRRjZvzLuVkrNu3a8nUdsXZV7Uc2_ciwKLwlyoSuslOh8l9IssYwirg2z1alMhc037Ma6t72SRKNmrsQvSa4gmrBSJWFGJq67_z4wGnLEatGWPdwkfSp0cCaQrjObjtedok-s-vVo-V1vg83hu-8MhLykcLf6nUWTl3lCd3BsTJExKUI2p-KwAOZnFbJfIfXI0YZusl6R_FQYX8W7MA_g_52zRaV548uu97QOqFuHYHWeeyzaEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیستی که صداوسیما از موافقان موضوع مذاکره با آمریکا منتشر کرده و گفتن که این نفرات به مجتبی خامنه‌ای خیانت کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66604" target="_blank">📅 15:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66603">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
کشور قطر از آغاز مذاکرات میان جمهوری اسلامی و ایالات متحده در سوئیس خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66603" target="_blank">📅 14:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66602">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
خبرنگار صداوسیمای جمهوری اسلامی:
یک دور تبادل پیام با میانجیگری پاکستان میان جمهوری اسلامی و آمریکا انجام شده و هیات جمهوری اسلامی نیز با هیات قطری دیدار کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66602" target="_blank">📅 14:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66601">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3bwet3o3ExNlc1zGf7jWcu4vw2QdFNV3-ouqB4r2NazrX00PKuF5IiTUy60Ek-PvHuqOszNNpTWijtzY-alJyc6YqLbV3C0PGSsThfcCCpoPvDZJTD9YVDfYa-oGuLBNlWS9ClVNdZ2sy8cTOBdMTo--8uj6xZfeYM4B31i3NEHEOkfl_3t8UDkordlQ6kV4HQtayJqcgqXqyCCsQYFDgJxaI_qymvg0VFu77wH_pGKnVj-z4VFPIh2r-hCeIp5AjUQICDjbOdetvEaaQZiIdUwsZJXsjSrWlfLVpTtHj44nipqMmw4Re_B2NsFL-CI_u39foF1ohoDh9Ks6dP2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است. بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66601" target="_blank">📅 14:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66600">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:هیچ محدودیتی برای سربازان ارتش اسرائیل که برای رفع تهدیدها در لبنان فعالیت می‌کنند، وجود نداشته و در حال حاضر نیز وجود ندارد.»
پس از حمله به نیروهای ما، ارتش اسرائیل با قدرت زیادی پاسخ داد و تعداد زیادی از تروریست‌های حزب‌الله را از بین برد و به زیرساخت‌های تروریستی متعددی حمله کرد.
حفاظت از جان سربازان و شهروندان ما بالاترین و مطلق‌ترین اولویت ماست.
تمام دستاوردهای ارتش اسرائیل در عملیات لبنان حفظ می‌شود و نیروهای ما در منطقه امنیتی در امتداد خط زرد در لبنان مستقر شده و از آنجا علیه تروریست‌ها و زیرساخت‌های تروریستی عملیات انجام می‌دهند.
آتش‌بس اعلام شده دیروز، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که از جوامع شمال اسرائیل محافظت می‌کند، باقی می‌گذارد.
همانطور که من و بنیامین نتانیاهو، نخست‌وزیر، روشن کرده‌ایم: اسرائیل از منطقه امنیتی لبنان عقب‌نشینی نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66600" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66599">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🇮🇷
پرزیدنت پزشکیان:
«از حق غنی‌سازی خود دست نمیکشیم»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66599" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66598">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=kX6cQpqX1Wr02oh0AcQ-Yajru7WKFbaYxNsyytCInUpN6PY-Rls4c7J8Xje2MIfItHjeBC_FcCIxD1ibZRFn7A4u9Io8tw8Icip5n8vxI7Jv5gUI0aGmJ0WAZTLB3clNqcAE77zq7NCGmCisqW7nVwBZM6-M8NYUzF5Wlwa4rU4a1RT1XShyouP9IW9vlaKK8KEbCgoUtQ7f4QsGDQbNWELfEBAwsvCHl4R2hOFA7F28KZIjkcr0eI9IEBYa6piMnOGiVje7PF14F_Pb0CYbfi4AMCcPnbwe4SnsVpWnkgA6YHAix1JsrTGtJyruorubIeJXdJ_7pK4Hgw5Xb5ugpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=kX6cQpqX1Wr02oh0AcQ-Yajru7WKFbaYxNsyytCInUpN6PY-Rls4c7J8Xje2MIfItHjeBC_FcCIxD1ibZRFn7A4u9Io8tw8Icip5n8vxI7Jv5gUI0aGmJ0WAZTLB3clNqcAE77zq7NCGmCisqW7nVwBZM6-M8NYUzF5Wlwa4rU4a1RT1XShyouP9IW9vlaKK8KEbCgoUtQ7f4QsGDQbNWELfEBAwsvCHl4R2hOFA7F28KZIjkcr0eI9IEBYa6piMnOGiVje7PF14F_Pb0CYbfi4AMCcPnbwe4SnsVpWnkgA6YHAix1JsrTGtJyruorubIeJXdJ_7pK4Hgw5Xb5ugpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار هیئت آمریکایی و پاکستانی
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66598" target="_blank">📅 13:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66597">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=pbqFxunJsIrJANJLDF6g6trFVNFjWcEVwwRhD2LZ19BP4wIbS0mHwKoMODHghO2tESvuUspomwMUTJGG6piR4lo8q7iEtFwv0twPztjEw_X-gkm65ORvCnPp8PhncZiy4AkvoXaY81IINWgWQJFEdosenElD0eXEkf4VQ9KKxCuwjKL1Puooh6gyB4O503PUXEKaBI0Tvha1YV5OoPOyI9K0L8Z8Hkrq7MhO84FXmH0poieN_zbFaZXYf1tgoO8Hy87zor6NvgRl_r3GX8ywprc9sHfJ4GM1WtIL7JFPSM_CA1m9NVmJyZ3GQ-twvVUrTAm7CN-HQLpYzrRm1WejHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=pbqFxunJsIrJANJLDF6g6trFVNFjWcEVwwRhD2LZ19BP4wIbS0mHwKoMODHghO2tESvuUspomwMUTJGG6piR4lo8q7iEtFwv0twPztjEw_X-gkm65ORvCnPp8PhncZiy4AkvoXaY81IINWgWQJFEdosenElD0eXEkf4VQ9KKxCuwjKL1Puooh6gyB4O503PUXEKaBI0Tvha1YV5OoPOyI9K0L8Z8Hkrq7MhO84FXmH0poieN_zbFaZXYf1tgoO8Hy87zor6NvgRl_r3GX8ywprc9sHfJ4GM1WtIL7JFPSM_CA1m9NVmJyZ3GQ-twvVUrTAm7CN-HQLpYzrRm1WejHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم مذاکره کننده جمهوری اسلامی در محل مذاکرات:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66597" target="_blank">📅 13:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66596">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=XUnX75WMd13I0F89Lof5fHDEKFYrE8NvG91Buny_O0OWdSiZW8zBzXC0Kv0wuOoMytW9oud1125nqGOQpq2jVHU-sGOB_ZW3a0E6CZ1rHPp3Ybrfo19SdFNmKR3hafndDOk9adsM_fVCkQVWy4bQ4Sr-cvzphJPaMTelc2HYIneXc16qNbJKcuhGOykAiVyMnTsdLsdZfYpZ6T8jQZmf5YiZqA0Rl9pe-u4ZH0aXZZeRoXzpN3jnGXq3IPD-q4gAd5Ym9eF3JoqKdc5c1ctvsHPjtrMBjML56KUnUKwRHZ-qyb0in1dXdDH3Cwlf4e-gP4aOZphOQnfiJovpg2SJxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=XUnX75WMd13I0F89Lof5fHDEKFYrE8NvG91Buny_O0OWdSiZW8zBzXC0Kv0wuOoMytW9oud1125nqGOQpq2jVHU-sGOB_ZW3a0E6CZ1rHPp3Ybrfo19SdFNmKR3hafndDOk9adsM_fVCkQVWy4bQ4Sr-cvzphJPaMTelc2HYIneXc16qNbJKcuhGOykAiVyMnTsdLsdZfYpZ6T8jQZmf5YiZqA0Rl9pe-u4ZH0aXZZeRoXzpN3jnGXq3IPD-q4gAd5Ym9eF3JoqKdc5c1ctvsHPjtrMBjML56KUnUKwRHZ-qyb0in1dXdDH3Cwlf4e-gP4aOZphOQnfiJovpg2SJxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند چینی وارداتی
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66596" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66595">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue3GgIBC6MQNIun_ANASYsMngY-plGeV4RfIZHGLbm17bVsTQ51GvU_RMXNtODqUe1ODZLpoqxUEq4y83C4ed0FsUhkTI0UqVBQKXNv01oVCfxyUEWdtk7m1B5EX46wDCQDvVrvQwYsNRNoo5Oj78X_WXTiu6vAO0lA71um91oBTHJJTKGePSsh8YWjHgjFdLYgL3nMqs9L-ibm1UiSaCImyyZAT9mDoQD0jcb5ZQj1LW-AJqRQQQFpDgdROmbnYDGBELS_7fy-guok812I4_9sTNNNE0qo-k22K4i53rcgOAzPi7MnHa9aAeMaTzarbqgd7IIGkHLxIgxXBJVbYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
آمریکا قرار بود با راهبرد «صلح از طریق قدرت» ایران را وادار به تسلیم کند؛ حالا که شکست خوردند، از سر استیصال اصرار به مذاکره دارند. اما دشمن نشان داده که عهدشکن است. باید مراقب بود؛ هرگونه خوش‌بینی مورد سوءاستفاده دشمن قرار می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66595" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66593">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9jk-NT_kA2F5eEuColcCrhAX8vUbbsKfeQW-2i1pu7uLiJbJS-udkngIcAZjbmgAUqj3fSUCvmsnKGmRf5cleafwsbhXfMDS9cO0eqsqTH2R_J32yverqCWqVpkfiSM--sbhmyMZ9y7dbBKtWBf9qjmK9kfO4RrMcgr94GdNkCuLwEUa6r295B-4z5_iaGNofbsL1gXoSGw6ESqljAtRyz4D0Vk7jTjciV62moAzDq4xzM02hYZeO7x9GDjjqT2A0kZM1Mwtg5YuWEifkdGsIjJCVMh57p4O4tvjoBPFMk-DNvMhKQbf6cWX-EJQ1FDr5ZimpitK9OQG6iBIZHeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=JrYYZ5Oi54IhA3HprmqS5R46xVZ05YC9Jtw-Re3hldylAzQnlV8y74Sg5PQK1zsKMNOJgorZ-lhuX-1lTnQKYBwU_JlBynIbgSIqJoUe-eW0exN6NMZCnVv_qSI276M2Mu2XbxuMmYk5OLG55LMCcRBO9XcdDziZ2MC5utsbIWuUTpmjDC8rV3I0x2ulxeccxlpwWscIjcT9ZsLyva7KMWiErvBHKifzCFxDiwU-WrigWxIcLf0Ne4PK5h3Pj1mJt5w_a4AwCObN4cmTnk8c9Zjg-Z2uVH8c8gl-JxC0n9AL5zvRjU-eITIUWVxVvPGb8QKhCPpL3OtNDpURX1ECcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=JrYYZ5Oi54IhA3HprmqS5R46xVZ05YC9Jtw-Re3hldylAzQnlV8y74Sg5PQK1zsKMNOJgorZ-lhuX-1lTnQKYBwU_JlBynIbgSIqJoUe-eW0exN6NMZCnVv_qSI276M2Mu2XbxuMmYk5OLG55LMCcRBO9XcdDziZ2MC5utsbIWuUTpmjDC8rV3I0x2ulxeccxlpwWscIjcT9ZsLyva7KMWiErvBHKifzCFxDiwU-WrigWxIcLf0Ne4PK5h3Pj1mJt5w_a4AwCObN4cmTnk8c9Zjg-Z2uVH8c8gl-JxC0n9AL5zvRjU-eITIUWVxVvPGb8QKhCPpL3OtNDpURX1ECcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رشته کوه علی طاهر، دژ استراتژیک حزب الله در جنوب لبنان:
طبق نشریات این سازمان، در زیر آن، تأسیسات «عماد ۴» - شبکه ای از تونل ها، انبارهای موشک و مقر جبهه جنوبی حزب الله - قرار دارد.
یک افسر ارشد ارتش اسرائیل فاش کرد که عملیات روز جمعه، افشای یک شبکه زیرزمینی حزب‌الله بود. ارتش اسراییل این تونل را محاصره کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66593" target="_blank">📅 11:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66592">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSi3nrCCoPHeer0tJBR5lgSrPIYVRTJrD-6iUT8DsjkRuvZIuXOS1gydbMG0By3pxZukN6zAaxexhhibO0t9pWyk9x-W-KajxiogKpxDR7om6-N0cXTUo-uON4W9mc8IW9bUx6sRQnqbxI6tQryzZfqzMpHSMDroMh_9-wW7s0DKsLeXKIRN3Zns5yPb4nh2ThBxKr9UeqNg8Plev8W-tOF6S39lnXiWqsbW3NhV4RyTGBz_GSijfuCLrzr1GmUpbFPCb_WBSzfD2MjY_t7WMztRUabOqInkgPkIJE1rTBorDsa5WS9VudmuIA7qLfVagPgoGAYVkcVegmaxyp9Q9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پس از وقفه‌ای بیش از یک ماه، صادرات نفت خام از جزیره خارک از سر گرفته شده است.
تصاویر ماهواره‌ای دو نفتکش بزرگ را در پایانه صادراتی نشان می‌دهد که نشان می‌دهد محموله‌های نفت خام ایران بار دیگر در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66592" target="_blank">📅 11:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66591">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=TEvdGnwmealNmb2PVus7RPftFDkxrjc1hU4QX-YzNgC4OJ0CVsHrcP2iZTwAmBDfj2aV3_ccf0sYSUGjv37u_m2l_wwd-zzlShIcW4Bq7zs59ImU-YdOf8RWTMwB54QGwl0KutP0yIuYggNg9To6VUlWRPpxE9ZtErvyN8e7Q-kRlhwy2FrOxpgA77oGq4PDaWFzTgMPq_JXcydJIEvzw59TnHZd15D_kjA7bZ7KCJLF_sJCUX5SxUt32xEXc6QKbvWzV-G2n2aZZJ2xGOv-gz39orOUQdxYXNKsrsbX7ZNWFXr8Us3p69ddYoF2dVvzBI-fyoeGh_HTeIl8pM7aVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=TEvdGnwmealNmb2PVus7RPftFDkxrjc1hU4QX-YzNgC4OJ0CVsHrcP2iZTwAmBDfj2aV3_ccf0sYSUGjv37u_m2l_wwd-zzlShIcW4Bq7zs59ImU-YdOf8RWTMwB54QGwl0KutP0yIuYggNg9To6VUlWRPpxE9ZtErvyN8e7Q-kRlhwy2FrOxpgA77oGq4PDaWFzTgMPq_JXcydJIEvzw59TnHZd15D_kjA7bZ7KCJLF_sJCUX5SxUt32xEXc6QKbvWzV-G2n2aZZJ2xGOv-gz39orOUQdxYXNKsrsbX7ZNWFXr8Us3p69ddYoF2dVvzBI-fyoeGh_HTeIl8pM7aVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از جام جهانی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66591" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66590">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeXq410e-zkuQVimHentuz5WkdKZq2zITTMi9VOVg3ffT7fjxUrSEV0rMF-ttzEVFLZRoiwzzZfw_aTywnok5g40hnTbov0VZIdSZr3LSoWhRIKFdOZL3FQM_eAvl8rPt1MwQAMVwGId4qahUDZJ8Xus_OTmB73L0Q_nEPbj3rhAPCnFZVnMD4_rhWFcXfs668bAkc8_sBJEVkHWLfeb7Hpwydzn5h_7ft0xiTry0c4xSeYgxsxBhppn3eWIlMr6xQE7gpTVFSzpT2na5_EBwho_zTREXTFn1lkEb4XCsjNO4t98c0ezmB1Eymj-Vjc24mdHNfTvyJhqTzfSGNytcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاونت راهبردی پزشکیان :
تجمع کنندگان بهداشت روانی جامعه را برهم زدند  تجمعات باید بعد از تشییع رهبر جمع شود.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66590" target="_blank">📅 10:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66589">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
منابع پاکستانی:
عاصم منیر فرمانده ارتش پاکستان وارد سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66589" target="_blank">📅 09:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66588">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=IhZeL1EGe9KPbKteTR_i-7mqa8pFSHofdFArfl8VOMCmD4_dqP5_ovd2Qg3Izlx_GvMPVxiHauFaGo_8qmy1DWLpD99p4orqCNDaGW-pPEBotD17GpLGxS6tp-j6aLOhpRTTQXrC9dK_WYRdGF74FFvT6a4C4Y9w4T8GHuFHlTlWLC--G6P46tXwpmOhFFSkeUcDA2HjBeXsT2e6tNmV4V-58txmYNyIt3Y-0S9mlfqUH2yg9QRaNiL-brVrVC5ajDlxHI5lwvcbgSOAQC9zpAssVazNc5TPCPSCmq-xq_QRCZnjZxRYxs4DAhlr4SrA3EveAbf3b1F1r7EaoLzF-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=IhZeL1EGe9KPbKteTR_i-7mqa8pFSHofdFArfl8VOMCmD4_dqP5_ovd2Qg3Izlx_GvMPVxiHauFaGo_8qmy1DWLpD99p4orqCNDaGW-pPEBotD17GpLGxS6tp-j6aLOhpRTTQXrC9dK_WYRdGF74FFvT6a4C4Y9w4T8GHuFHlTlWLC--G6P46tXwpmOhFFSkeUcDA2HjBeXsT2e6tNmV4V-58txmYNyIt3Y-0S9mlfqUH2yg9QRaNiL-brVrVC5ajDlxHI5lwvcbgSOAQC9zpAssVazNc5TPCPSCmq-xq_QRCZnjZxRYxs4DAhlr4SrA3EveAbf3b1F1r7EaoLzF-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صدا و سیما:
علاوه بر تنگه باید فرودگاه مهرآباد رو هم ببندیم تا مسئولین برا مذاکره نرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66588" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66587">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=qbfWriu_TN4hVnLYQQWK7xqsqrHIkbrw0LEmCfA-ifYOtlaCNMG5cr4XqFpJ0LKh5OGlyBQdHdfT8DxvD8le2qaNXUMQgJuadixWFR8kERdHYrIH60Ky4SnzN_MLW-nzz7abTRf9rO7M27mVqnBwm_4YRZ25npRO310V6PC4AxNMhtlZI99qza7JzTHD7okbHucfjMDSdvtnF1raVahBNQMV8iwcyHx4cQgzjW-6Knpn8kxKk_KCA6ed3hIFUMPjymFSnG3yrMzXjvrci33WYiM5qiRuRx8wttejX0ao6FgHN2IesBglBsfz0MZEoZRd_qPX6qxCb7IyhRfqD1R00A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=qbfWriu_TN4hVnLYQQWK7xqsqrHIkbrw0LEmCfA-ifYOtlaCNMG5cr4XqFpJ0LKh5OGlyBQdHdfT8DxvD8le2qaNXUMQgJuadixWFR8kERdHYrIH60Ky4SnzN_MLW-nzz7abTRf9rO7M27mVqnBwm_4YRZ25npRO310V6PC4AxNMhtlZI99qza7JzTHD7okbHucfjMDSdvtnF1raVahBNQMV8iwcyHx4cQgzjW-6Knpn8kxKk_KCA6ed3hIFUMPjymFSnG3yrMzXjvrci33WYiM5qiRuRx8wttejX0ao6FgHN2IesBglBsfz0MZEoZRd_qPX6qxCb7IyhRfqD1R00A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خودزنی مداح وسط هیئت:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66587" target="_blank">📅 09:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66586">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66586" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66585">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O7CCUwRcBkjbyjoroDARTG-Q5k8k3Fu8LP98daWqkar4TrU5f8EYNc3BMPx3vWHAZY2LuqeHtyg6VGVTjJNwX7wEPKfemjvCUqYcsy0RoGYFoUSQbPmk_a_Wq5uLtLg_3qypZDW9Nl3KVdqyuB0ARKOWA1JRDwrsfwd_4df8lgrkDt_2ItGWwfWBVDYGMZE6kRzFI9m5kBgY97NKq9g82WsZrhJSUWZ0uiJ7SlaUV8rdkVjy4Ro1eKp6Y5AGXz1lgbIs8NVi0muLIwQcktPQXRkv8L6PC_Pg8eDOWDq7Q1e_UQh438HuU7biUzaUyhnKGwmWzchChFiroxVeXJMrbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66585" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66584">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKNWjNgqeGZL2fo9Zc-_ZZKqrzM8Cg0eDlk4z-yV5HtbzVT2UrtCtVZZqnolA1schQs3Jj2X4xtDzkXLuc0mcGGHZYjOgVebwwj3NZB-PEq2kXnmbmdEIN8eDA1OkczHyGI3tYM7MysmJWBz32VWdj6fL8NH9LbS6QQ_CgtQZwa1wrzJ97tCer4xyvyOvJtu3bW7954oFnO_CYgRQs9RslYc_IoxSuXctj2rZzUVdEbRc6oJJ2gySIqavJBbTvy7quUYBUKZKS9wK7fgZBqiWhcgVWMlrTRqcfKCHk3zXmsOBl1tKKoujete2Zpy07UlqxdSUvQqCg5jMoexh3_hwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف بعداز ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66584" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66583">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=QOv0moa5CrRmbD3A8x6slHfRg--lZao70FNglRjz_nCXYfzJlwgqL0cyoHYsYdqUu6g6Ek3GjfHFSZYturFY-m3dJVJiq2OK3PNqo1DA1Irz6P4s6lNGQWIXqEwBuHEs7XUY8p1UzFTz5TqCMHwm8tkTCXaDOEnkUZ7qUuHxQTOCL_AwJx9jHNdeqAm73ic6JlbBQP5f2wFmVP0ccl7IAzePw6gBMtbyP37WQRaM8FP4U_AmSBAqt9mU0Weix6zmsKAJrPBEoxVZ4iFGCVsvbBtZfhMbbq24isSy_hRtMt4jHN7bZhuWBDT-UtQSY-D4EZbC3gZk9LAsoqIwcuoJmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=QOv0moa5CrRmbD3A8x6slHfRg--lZao70FNglRjz_nCXYfzJlwgqL0cyoHYsYdqUu6g6Ek3GjfHFSZYturFY-m3dJVJiq2OK3PNqo1DA1Irz6P4s6lNGQWIXqEwBuHEs7XUY8p1UzFTz5TqCMHwm8tkTCXaDOEnkUZ7qUuHxQTOCL_AwJx9jHNdeqAm73ic6JlbBQP5f2wFmVP0ccl7IAzePw6gBMtbyP37WQRaM8FP4U_AmSBAqt9mU0Weix6zmsKAJrPBEoxVZ4iFGCVsvbBtZfhMbbq24isSy_hRtMt4jHN7bZhuWBDT-UtQSY-D4EZbC3gZk9LAsoqIwcuoJmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی‌ونس معاون رئیس جمهور آمریکا برای شرکت در مذاکرات با ایران عازم سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66583" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66582">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoJ_fghWqVxcibD7Vat_roRmbqzBrY30oQUo2W0sMer3stUJXChEuP8kapVorLInBP0C51bzNM4fNv3UKIDzHrlrElyMNd3G3b-HCM2GsRkjVEel-iGM2mkwSS_J-5mue40zG6UAXeBi0Ertu-nZWk0o5-TABhMAs-TZRqhPj2iwfmcLGQzT5FUjPnV1RPnMseFgI5zsUPSFxKaB2Q18719MyQfmu6YlCtwi-fbbN4nhZ4AtsR0G-H9HuaLAwcm4pPdJmK548uvnaIzGN1YkKLVC2TrxSvyTOlZ0tkL5x_r__a--cUPuj56uvGcYK58XeRCUkdEvm1DrU3e56vMStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مرندی عضو تیم مذاکره‌کننده خطاب به ترامپ که گفته بود هیچ هزینه ای در تنگه هرمز نیست نوشته:
«هزینه ای وجود خواهد داشت این قطعی است»
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66582" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66581">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666063795.mp4?token=FOS13qTNnB4cp06rAzLvq9Kybc7G2oaHIn3s17tGEhcur394GC6uYMrAdl-QU1WSCv4_SiyVwZeTK4r0rSopZOQkDhkemMkH79jhfrt6U_IhXWl8v1yqkSfokmF1BVQiWad7qyxwh1uzljhKn7sfHj10O1oEZQ0Kn8N_JyI3ZCbUsJ5ewALIvsdw0iQBJdCuk1zEL4RNwqIgm0sNX6AJk-gDDOlQNu_RvWHFXvQLq_Ok_gFvcRg00zrRo0Ik-NIY-jX3oFRmBupT3IV2C4DJ-QD5FGM8LdVz491yQ1yK8aP9-w1YwzxlvdJpDz0DZd71WKG2u1PKOcvLxjjTOHSm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666063795.mp4?token=FOS13qTNnB4cp06rAzLvq9Kybc7G2oaHIn3s17tGEhcur394GC6uYMrAdl-QU1WSCv4_SiyVwZeTK4r0rSopZOQkDhkemMkH79jhfrt6U_IhXWl8v1yqkSfokmF1BVQiWad7qyxwh1uzljhKn7sfHj10O1oEZQ0Kn8N_JyI3ZCbUsJ5ewALIvsdw0iQBJdCuk1zEL4RNwqIgm0sNX6AJk-gDDOlQNu_RvWHFXvQLq_Ok_gFvcRg00zrRo0Ik-NIY-jX3oFRmBupT3IV2C4DJ-QD5FGM8LdVz491yQ1yK8aP9-w1YwzxlvdJpDz0DZd71WKG2u1PKOcvLxjjTOHSm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری که در شبکه‌های اجتماعی منتشر شده، برگه‌ای تبلیغاتی را نشان می‌دهد که گفته می‌شود به سپاه تروریستی پاسداران تعلق دارد و در آن برای اعزام نیروی داوطلب به لبنان و همکاری با گروه تروریستی حزب‌الله، حقوق ماهانه هزار دلاری وعده داده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66581" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌های گذشته، حال و آینده، اعمال شود. از توجه شما به این موضوع متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66580" target="_blank">📅 23:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66579">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=mhEInTh3x_CZrzDbHi7MmnRKgBLzbOE4Npn9dT6KJvW1vFUGNRBkuGMf3oAyyomnN7zRQb2xcwtNEz4nlOy-SUPj-ybKGRsXr4v5b8d2tt4V4spr5IxfJW5B8bbu9XyQ5RVjFl4QaGdtNCyC7HkmoCqT3C2ydJ2NXibQImGUUkhR6uVinl16qFiSlDiY7woLOB_eDeEYD77-YMZmCehAcbAJXCBE-hMkVrBZ8CI4UeQ5Wliv0xdNzomjDKSOxGtZ0FXS1PFE0F8oTee78uW1PSHIkJidLKotLXeqJZfy6K2TQqa_vMH2M4bIKZnwmxvJC03CKzTdkRbyWL9Oibsfcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=mhEInTh3x_CZrzDbHi7MmnRKgBLzbOE4Npn9dT6KJvW1vFUGNRBkuGMf3oAyyomnN7zRQb2xcwtNEz4nlOy-SUPj-ybKGRsXr4v5b8d2tt4V4spr5IxfJW5B8bbu9XyQ5RVjFl4QaGdtNCyC7HkmoCqT3C2ydJ2NXibQImGUUkhR6uVinl16qFiSlDiY7woLOB_eDeEYD77-YMZmCehAcbAJXCBE-hMkVrBZ8CI4UeQ5Wliv0xdNzomjDKSOxGtZ0FXS1PFE0F8oTee78uW1PSHIkJidLKotLXeqJZfy6K2TQqa_vMH2M4bIKZnwmxvJC03CKzTdkRbyWL9Oibsfcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
جدید: مقامات آمریکایی ادعاهای سپاه پاسداران ایران مبنی بر بستن تنگه هرمز به دلیل تنش‌های جاری بین اسرائیل و لبنان را رد می‌کنند.
یک مقام ارشد به فاکس نیوز می‌گوید که ایران نمی‌تواند تنگه هرمز را ببندد زیرا "آنها آن را کنترل نمی‌کنند" و به حجم بالای کشتی‌هایی که اکنون از این آبراه حیاتی عبور می‌کنند اشاره می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66579" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66578">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSoy5RgNqAKBbXDIvI8RIaQQSmaQdJmPbvcp68j-QxZlimOUNjTUXqx6z74Pc1x-ZLy8UmNTxDWI-EWoBeRQVXXQCpGI-9uKc6EODWpEnS6Mmq2R1DvX-HU9CqDiIAIuso-bif9jau439e6H_siZc0UXUoVzpuJ2Bz0lnzcHAoRDF2n70FHz3fa9ylV0fHZHPKEYYgL4wGVeZR9qG8volxMgvgKZgPbgO2ZuP5KdJy5EELQALwwkAirg4ye3w6fidex8viVY7pekyFImiT0P6Bcha1bnOMYdFpRtjBGq01qBczScSX-T8FMGGSXvLzaO9WnsrITJ8-u7aOUVch-ScjAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSoy5RgNqAKBbXDIvI8RIaQQSmaQdJmPbvcp68j-QxZlimOUNjTUXqx6z74Pc1x-ZLy8UmNTxDWI-EWoBeRQVXXQCpGI-9uKc6EODWpEnS6Mmq2R1DvX-HU9CqDiIAIuso-bif9jau439e6H_siZc0UXUoVzpuJ2Bz0lnzcHAoRDF2n70FHz3fa9ylV0fHZHPKEYYgL4wGVeZR9qG8volxMgvgKZgPbgO2ZuP5KdJy5EELQALwwkAirg4ye3w6fidex8viVY7pekyFImiT0P6Bcha1bnOMYdFpRtjBGq01qBczScSX-T8FMGGSXvLzaO9WnsrITJ8-u7aOUVch-ScjAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره با ترامپ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66578" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66577">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=kAGR6E416PGBAsQE3nADgHbw-6cK49jjt2MYcGHEWZ5sBn9CtskRWpxt7yQnJSy5-BIoX0XYHWZorQfAxr6WEVTLY7ry1HBagN2kIqBWSdDm71PD-AgO-fY8v1_WwN8xVgus94HkQh8xz6FVv3jsl6b5UPQpfis71YjO938boaUsTSTDKaJDRXEC00iQEbwwFgCx2hmYvJ7jb8rcGhZnEDggUnmqTDPmdXfN2ddzyPUQBF2EfztQN9lxHdsZj41rAiPr5COqv2BFvieGxYqBUGBIbDjGJn1Ye_29h6T1P4Sn3vB57U1mLZs04ZLxoH5AEeB5yqkVyCSVEPU8VorTXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=kAGR6E416PGBAsQE3nADgHbw-6cK49jjt2MYcGHEWZ5sBn9CtskRWpxt7yQnJSy5-BIoX0XYHWZorQfAxr6WEVTLY7ry1HBagN2kIqBWSdDm71PD-AgO-fY8v1_WwN8xVgus94HkQh8xz6FVv3jsl6b5UPQpfis71YjO938boaUsTSTDKaJDRXEC00iQEbwwFgCx2hmYvJ7jb8rcGhZnEDggUnmqTDPmdXfN2ddzyPUQBF2EfztQN9lxHdsZj41rAiPr5COqv2BFvieGxYqBUGBIbDjGJn1Ye_29h6T1P4Sn3vB57U1mLZs04ZLxoH5AEeB5yqkVyCSVEPU8VorTXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرار موفق یک کامیون روسی از پهباد اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66577" target="_blank">📅 21:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66576">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
منابع پاکستانی به الجزیره:
نخست وزیر و فرمانده ارتش ریاست هیئت پاکستانی را بر عهده خواهند داشت و برای تسهیل مذاکرات تلاش خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66576" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66574">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRLfEsJf3BuvgdQQjPvp9oVxt-k8pooeqPa_P02HSVWxkWl22yvBMx3XhfwWlNl_XDW9zwYl_aCnIKx59Vw17BweCU66c_SuCDyoN2S8VhdTKKlLcLJbfVSnG8AxQpmWPaCXdky4cytGu1isQkynii_xPDIgqW6X3kTopow5gw8Su88CdtFUaRvm6CKgN0bwa2CiXDotl97ZhjMLAnpKvZ-AmRuIzi3NggAj8KEvtY3RREl710VXk_5rXXgFUDIcvYx4qMq99gO2rToM_GwTw4y7ZgQaNLL5mYz7RO4xfueb3x9e2a-vIrd4pkjAdLycSJMZWZpVW7yfsv2Z7NAdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8349099df3.mp4?token=W9jgTH3grr7mixDqWcIVwJtggPFtWVqLPpPL5P93uag0XRdelmtTJjx2rlN_Q5_IJulCiLycVmEEOCVisOeupgB_G3qyVhYmVPEFygUEybHpQW4YGo-K4NS-75vBfulmaW6RIX1d_BBFCQQaIhCciOxViWr6nARSi6TX1N5uCR90NB0UgbAyVPWg4pbzPDYDZ49mBC4WvBPJrNoFc0g_0EL16cdxcDUpzFOe3rH_m-LT8Y2sqIecc0lZjs8_0_Rb5PRyYmfH0DooTMRYV2o_XVPy7IULXHUAurB33Qp5IFtjTB8wCgZTu8IB5DiAFVbev2awQkxJR7JG7mmxJLs2sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8349099df3.mp4?token=W9jgTH3grr7mixDqWcIVwJtggPFtWVqLPpPL5P93uag0XRdelmtTJjx2rlN_Q5_IJulCiLycVmEEOCVisOeupgB_G3qyVhYmVPEFygUEybHpQW4YGo-K4NS-75vBfulmaW6RIX1d_BBFCQQaIhCciOxViWr6nARSi6TX1N5uCR90NB0UgbAyVPWg4pbzPDYDZ49mBC4WvBPJrNoFc0g_0EL16cdxcDUpzFOe3rH_m-LT8Y2sqIecc0lZjs8_0_Rb5PRyYmfH0DooTMRYV2o_XVPy7IULXHUAurB33Qp5IFtjTB8wCgZTu8IB5DiAFVbev2awQkxJR7JG7mmxJLs2sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
امروز در شبکه خبر در مورد چرایی مخالفت رهبری با تفاهم یادداشت ایران و آمریکا مشغول بیان دیدگاه رهبری بودم که به صورت ناقص رها شد. بخش مهم آن بررسی متن یادداشت تفاهم بود که علت مخالفت رهبری را بیشتر آشکار می کرده است. انشاالله خداوند ما را در پیروی از رهبری عزیز ثابت قدم نگهدارد.
«ویدیو هم از لحظه ای هست که آنتن از نبویان گرفته شد»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66574" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66571">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
‏به رغم اعلان اخیر سپاه پاسداران ایران مبنی بر بستن مجدد تنگه هرمز، فرماندهی مرکزی نیروهای آمریکا «سنتکام» اعلام کرد تردد کشتی های تجاری در تنگه هرمز امروز افزایش یافته و ۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت به سلامت از این مسیر عبور کردند.
مرکز اطلاعات دریایی مشترک (JMIC) نیز با صدور بیانیه ای بر تأمین امنیت کامل این آبراه بین المللی تاکید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66571" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66570">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPknTmA73n5tB9kaCtLd6xJR41Jvzmg3CQyhHaxMcL8a2phQs7bqrmow82FmYvfVnFhvDpEr8L50BNteMNCMMYugTCkt8pXsv88ifx_Kjw1xYQMpVjtUBi2mElCMoTS1KznWvGYB_w6ff4tBwRWUxHWHl1f_EfnznRX5RSAZgfseKMw-sBTIBD3YsKkvAtnLgGVpLCGvWy_sYDIOPPx60EcuOCexp-0hrBa839VNaZypR4LfOc6Y6o4_i4JakKKX9AC1P31paFhK1e5NY2aCT0FL4udjVozcMOYZezKjm-Vmh9r8lcKM42OaoqBk4Ml3cQRXc718ZKnSu-abcWCkCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
جی‌دی‌ونس برای شرکت در مذاکرات فردا با ایران به سوئیس سفر خواهد کرد.
قالیباف رئیس مجلس نیز در این مذاکرات حضور دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66570" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66568">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcc-lAGK9Ql1-iV1p-Mt5bayZT5lWl1DqZXqjBwx8SrxloDgWKTGUgYz6vCdjLP2Lcan4l-koVef7BzjVihT16jXX1deo7BCorgZMq3JthtQviUgt8UOG_Bj5_RXSltkopUeraN25QoVREqigN13SnMIT0or762V9rXVvyZJj-KmwRbAkHrAojJTEUYkk7K352M2SPGhGe3k2cvrlYlCFoorTuZq5hn_lTF1kp90Bajt7meKqgHU5bYOd04MGEp1b8_oRVZTcHMgdoHjcO2Mt8CdbCSKh9zdfY-wdQQo8cg_s56WYmZydbelafB6DlQIcazTu_iD-r7wrx6pKmV13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=odjlJmOIuvF116Tdo-eP6Jg4x6RqaTRkdKHFYdosZgnPAFhVr4desHFntp2vbU2Im83Uczd3-pIp-X0YfkPeKNRt2aP5RTUd3ZArl6YtT9x4D37Bn5q8Nhzr29IqtD7Zd2lXPihCO2_ehT3q1teWpzv9SouE4Jb_pf2VMnRh_122gLgB1nwrjXLUp8Er_CPTi8DnMROjUQvirw60uDndhzCcZxX85OpwPvSgpQw7VseWV7Ti494A3mYAWvhDLmmnBL9yePmUJpwcBQjVdYI-evcWbT2OF8Mm98v2Lbe-tdQoF1pz0QxZKiWiUChs2LQtwqnZebriIdw8UPNgAhRL7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=odjlJmOIuvF116Tdo-eP6Jg4x6RqaTRkdKHFYdosZgnPAFhVr4desHFntp2vbU2Im83Uczd3-pIp-X0YfkPeKNRt2aP5RTUd3ZArl6YtT9x4D37Bn5q8Nhzr29IqtD7Zd2lXPihCO2_ehT3q1teWpzv9SouE4Jb_pf2VMnRh_122gLgB1nwrjXLUp8Er_CPTi8DnMROjUQvirw60uDndhzCcZxX85OpwPvSgpQw7VseWV7Ti494A3mYAWvhDLmmnBL9yePmUJpwcBQjVdYI-evcWbT2OF8Mm98v2Lbe-tdQoF1pz0QxZKiWiUChs2LQtwqnZebriIdw8UPNgAhRL7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏پهپادهای دوربرد اوکراینی پالایشگاه نفت تیومن (آنتی‌پینسکی) روسیه در غرب سیبری را در فاصله بیش از 2000 کیلومتری از مرز هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66568" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66567">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpAykgHtl1H8ZbKH1GcvaJxJCXdNHCNfeRFQakoshG90MiqHX0-9Teujmjb8e2lMkYqf0trGq5XEILnAke5XwLaqq2GIPTpYSNo7XhrWa22_DPZeVy1hwQ07DXvBbh3ZYBUDFVivOM9N11x4nB2Md2svxiHVFPOQV963R0CG8nX_0GqT7kUmjL05qd-uX1I3bipmifk4Dm98hGYx6vx3z8aYr5Ll8fOqaYK7M2iwJ-qgNr0DXm22HaCqaB-d7iFs4kpXH0XOPZ58cSFnI-fq8Izt3XbKpTGjGZzyGAweQhgowgZpfyCagzYNAlO5fGH9m-PPftyOelw7EeR9mVXWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛الجزیره به نقل از کانال ۱۲اسرائیل:
نتانیاهو و کاتز به ارتش اسرائیل دستور دادند بدون عقب‌نشینی از مناطق تحت کنترل خود در جنوب لبنان، آتش‌بس برقرار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66567" target="_blank">📅 18:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66566">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqaXnt1m7gwFhKIRQDbXLQzwaWrTqf-SQnTWPEO_aFG4fag5Wzxc6MDvnd6Fe3q8XG1FEhNh5nQCEaMveudNLKGobmyYgUYBJZSXXDF8f28Qn7fDZfEF-jdHm1QPGbEX07XwvXgo5pcBFyaQFCWO6DykSUf6nO2AW8b4rO3Q7r6zVEGPYWJ4xHf7Kh853vP9ngN9PEvx1fFFse9yzxf-RndvO9Wvr5Zy4uarWFc50zHCrJzNkBwQMeZRjr2ofqLG34bH2ZJ5F9WT1KP1PD5R5b8ILXvHES-3-f5FjIlAbTBUczyNM-cIGUV6MLiKeJ1VXux7qdBNY9R15Duog3OVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی عضو تیم مذاکره کننده:
جبهه‌های نظامی و دیپلماتیک دست در دست هم کار می‌کنند. تفاهم‌نامه باید سریع و به طور کامل اجرا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66566" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66565">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvzTlpeVVnYTX4t753jqgudNuDL7mpqXDrgoI5kXpVtACcv5mUr1fyJDB1tFxLBgMfm07Y-Xb5OVuQ0cnzN-MSBBgpg8WsT-AH1ms9-2dtX-869TEIkNEx9l029fHuNy0PlniF14S1RN2FQVxOu-9xO_ZuKsb9LOu1yZUTq2wMFR1GulkMfaiSlpKWW8lQMjVsNhy0K9BlLpLZ4XvYZ_ZNqGZ7nGfjYTNs8Xd3byEC7ESkbJsNsvhIxbYBcWr-GLVP8RX1-7YoiAOMsRi4AT2KvK47qi6HQUIAucEysd2TEHRvkIlJ5A9s85yoiaX8Yl5uXlClWOkG09QNe2R-gjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ دوباره به جورجیا ملونی، نخست‌وزیر ایتالیا، حمله کرده و گفته:
نخست‌وزیر ایتالیا، جورجیا ملونی، در جریان نشست G7 در فرانسه بارها و بارها درخواست عکس با من داشت.
او در ایتالیا وضعیت خوبی ندارد و میزان محبوبیتش پایین است، احتمالا به این دلیل که در موضوع جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران، از ایالات متحده آمریکا  کشوری که واقعاً ایتالیا را دوست دارد و از آن محافظت می‌کند حمایت نکرد (البته ناتو هم همین کار را کرد!)...
حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، او می‌خواهد دوباره دوست شود تا محبوبیتش بالا برود. نه، متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66565" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66564">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه پاکستان اعلام کرد که مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66564" target="_blank">📅 17:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66563">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66563" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66562">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
اسماعیل بقایی:
هیأت مذاکره‌کننده ایران تا ساعاتی دیگر عازم سوئیس می‌شود؛ این سفر در راستای پیگیری اجرای تعهدات طرف مقابل انجام می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66562" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66561">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
بقایی سخنگوی وزارت خارجه:
ما به تعهدات خود پایبند بودیم ولی طرف مقابل به تعهدات خود در موضوع آتش‌بس در لبنان عمل نکرده است
-طرف مقابل موظف بوده اسرائیل را وادار به آتش‌بس کند اما این اقدام را انجام نداده است
-اگر طرف مقابل از ایفای تعهد خود سرباز بزند، ایران نیز مقابله به مثل خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66561" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66560">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
❌
قرارگاه مرکزی خاتم‌الانبیا:
در واکنش به آنچه «نقض تفاهم‌نامه پایان جنگ از سوی آمریکا» و «نقض مداوم آتش‌بس از سوی اسرائیل در جنوب لبنان»  تنگه هرمز به روی تردد شناورها بسته خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66560" target="_blank">📅 17:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66559">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد بسته شدن تنگه هرمز نخستین گام در پاسخ به «عهدشکنی دشمن» است و در صورت ادامه درگیری‌ها، اقدامات بیشتری در دستور کار قرار خواهد گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66559" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛قرارگاه خاتم‌الانبیا: تنگه هرمز بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66558" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e32956668.mp4?token=u5sxvnhOI-VIJqdfleI4yPsyg4tWdQL0GcmtW2ACeWmmb7VaHvhHeC_fG71LRNVxpqCUvgRYHF4Yd64on-JtPrMslZRxSlVFosn-Ecd-IIUXNBRfarEjVleGaXfcDdJAu_YMJS7KlpSn1epMChHO9mzaSubIw2ZbLv79N9MCxDKSQ6cIlfCW-m8ZbU17TdvmN564QuRxAGlg21_5-sNA2or9CgUHXsKtaUX9np2Fz3TdgYkCN1QB19oly8VMFr7rIBycGVTCF3dCSliU8vtPd77tNQrhUTN6Ow1d0HKuIqgDyq1JzpSmcD-rvNLj60z1Paixgeat0cV4du32Ac9SNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e32956668.mp4?token=u5sxvnhOI-VIJqdfleI4yPsyg4tWdQL0GcmtW2ACeWmmb7VaHvhHeC_fG71LRNVxpqCUvgRYHF4Yd64on-JtPrMslZRxSlVFosn-Ecd-IIUXNBRfarEjVleGaXfcDdJAu_YMJS7KlpSn1epMChHO9mzaSubIw2ZbLv79N9MCxDKSQ6cIlfCW-m8ZbU17TdvmN564QuRxAGlg21_5-sNA2or9CgUHXsKtaUX9np2Fz3TdgYkCN1QB19oly8VMFr7rIBycGVTCF3dCSliU8vtPd77tNQrhUTN6Ow1d0HKuIqgDyq1JzpSmcD-rvNLj60z1Paixgeat0cV4du32Ac9SNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چه قیافه‌هاییه که ساختین
😢
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66557" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66556">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">باورم نمیشه ۵۰ سالشه
😐
🔥</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66556" target="_blank">📅 16:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66555">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=Cga59tgWX1HGfAUTxcYPX9OVCAjscWT9LYRBYyEmeFuk4wgSW3Hc7jP1L58zGgVW8RucyEBNXRSiLSMhuEw4yoZcmC3m6Xp1Zh-ccGXcqf4qQ_ZUax9k-xt_syz6MJyNYd30VvWKuVwsOZa28O_jl7zTNeF_aDcmarDBcBT3GCk3l3pk1jkscHt_sbb5CUkJgw0GRSZ37mpn-ct44QWXlyo8lydeuu5bIt1ebDwM8pa5jhAONem26y-beBx3ZbNlY95pLasI54JJw7MPbcoxALBJvrERnlbOmhr_x4J9IQUtK8Napk2e9t5CNkEFc7HqKJJ5mndG__1Xs9VV2oTlLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=Cga59tgWX1HGfAUTxcYPX9OVCAjscWT9LYRBYyEmeFuk4wgSW3Hc7jP1L58zGgVW8RucyEBNXRSiLSMhuEw4yoZcmC3m6Xp1Zh-ccGXcqf4qQ_ZUax9k-xt_syz6MJyNYd30VvWKuVwsOZa28O_jl7zTNeF_aDcmarDBcBT3GCk3l3pk1jkscHt_sbb5CUkJgw0GRSZ37mpn-ct44QWXlyo8lydeuu5bIt1ebDwM8pa5jhAONem26y-beBx3ZbNlY95pLasI54JJw7MPbcoxALBJvrERnlbOmhr_x4J9IQUtK8Napk2e9t5CNkEFc7HqKJJ5mndG__1Xs9VV2oTlLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
رهبری سه بار در موضوع هسته‌ای به تیم مذاکره کننده تذکر دادن و گفتن «در موضوع هسته‌ای یا باید به پیروزی برسیم یا اینکه برای همیشه از دستور کار مذاکرات خارج شود »
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66555" target="_blank">📅 16:10 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
