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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 05:15:07</div>
<hr>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxT9xHgroECRLmhokrrkXcMFsLzz9zmWASbaXhAh5SEaud5WIZgO0dOnvMbc9zgcdkAskbzaWCYmAA50fNVqKNlvKCfkJ1vqQ129Zmplbvq-x7mFevlRRX1BxPy4EFtqK5ytjXIz_E283YJt90xewnwk1Lp-5b76l42JlMy2rAK975DjLPvA7XgInihub6eHWkpJjGHTGaTuF6CFmP7mqlobGaQJtR21VTOsPdogl5ooKSdkJwzrhYf8Hs71fCAl7fVQWclVPl-gAPyJqYMdNdgQV_ySOaOpUUK0EVH5tEybFC6WJlBcEwSF1XTapYlrCNRcOdYwu5LK8DYPBM1WGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwjNRMZrqccY4ATQNLOWknmKFnoT8R3-TWmx5t6dk5hPwbQ4QOk6YJkEq4AqrlHkwzhiqLHrR27GccWdju8SIRJ5jyB87IR1vkAk2xVSfUL6zuWtKNAPTkj2r7opn4kCifkY8LjOMma7IIVGOisXuAiHDjHbArUJrsYcjqGd2y6QVWVeERlGpHkzGhvpfDFUXAeNjH0CRtUHYKWiGurOcEL9es0bYX0XCcl-mm1-IqXng2rC5g9qTDBfsxzU25epAiQhVPC8od7yUdA6Gh9rqea-XAktBCPOKdP0fwXkFZ6_8_G5Fkb_oeQ17kOs0uAI_R8pQjP3vB2GKT9OQNgZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=DowtIvwaJ4vmBCC96I9f2qTQZmmIDQ8dasbMJvUlkDjTFrxWXWMFih2LhFsLk6dHLhjD3SOPEVd7s4FFvEWZnvXU4EOldhMaRgsGidOcJiHgD8de91VFZXQ9swopzB8Fn3RXvDso__qpAGv26nmDF8IvRuEOJtOZgpAYqt1VnzpFntWm5E5XLx46CWf7uvbroBT-zAgx3eVRut1UagqpSe54SqEsVtSdq1BzY6CUC9XFdZIY162m8BO2-UbrlUBF8TVSSl_3Rg5vt_sYf3isb4Q6a4nXenVJpNFvJoYQtI_h6WXBKHwCY1q4sf9L7H7K8zwLxxLlSI-RGv02zSITLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=DowtIvwaJ4vmBCC96I9f2qTQZmmIDQ8dasbMJvUlkDjTFrxWXWMFih2LhFsLk6dHLhjD3SOPEVd7s4FFvEWZnvXU4EOldhMaRgsGidOcJiHgD8de91VFZXQ9swopzB8Fn3RXvDso__qpAGv26nmDF8IvRuEOJtOZgpAYqt1VnzpFntWm5E5XLx46CWf7uvbroBT-zAgx3eVRut1UagqpSe54SqEsVtSdq1BzY6CUC9XFdZIY162m8BO2-UbrlUBF8TVSSl_3Rg5vt_sYf3isb4Q6a4nXenVJpNFvJoYQtI_h6WXBKHwCY1q4sf9L7H7K8zwLxxLlSI-RGv02zSITLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvC89mjNjHBWL6b0vy9acYOsPkSnLXJMexvf_rjkvsEkEXoP85dA_i8iklFuviiEghQSJU2lvl9Gs4QRkETBq_LC5wWY8h51Tq54CHyHJvtk-XXRTFckrtvAqLqE94N-xPSElXluhTwkxWiu1fkaTUYp9Xe8X8LMWt7SO39BJEaVuaXyvrL5IjOt7_JvfhtHrVklgN6sUjqrLNWWjG75kA5mPxi0bOg77-47LfXsRLcwS2e5FLR9GE7fsMr53zEbB0SjmDwYkP4WjA6I6WM1eh4Bz_n7TT-hQkLjbrTfm4p_uZig9-HStjcPx-Nv1GWCkswQormET-kwwwku8GsYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66651">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">طارمی گل زد #hjAly‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66651" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66648">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">طارمی گل زد
#hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66648" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66647">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چقد خوشگل بازی می‌کنه بلژیک
#hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66647" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66646">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WA79S3C3Nzw4WQlSxmncMLarR8LqwdpkbyPGVLIat3GM4ERM_JbvhqPV3rlz2KsS8Te1uXx2jjr3fd34BvZ73QHmDaXJG1E5HEN2KycfXMxAqhsw0TKZi2R3ByUQG_ldUBB0GfLTv9WbaQ13u8tgOI4ciQkN2OaHek0wr_JxlucgXUJvpZ4Y3u6s1GcVF7ZFVE8jcthP_bazq49OVlH4Jf15fR3AA8GPqzup_Ta3M5Jw1_QYUFCPSLIOUEtiDTI9IawzgjJttjaJKg46f8qSESniM4UNII85-ercm-eW20ZfpkjQD9o4fCjtF09KXmOCQlQagWobuxJRDA40DW6Rkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از نکات فنی قلعه نویی به تیم
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66646" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66645">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66645" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66644">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
سال‌ها به ما می‌گفتند: «شما نمی‌توانید به خاک ایران حمله کنید.»
بله، شما می‌توانید عملیات موساد انجام دهید. ما تعداد زیادی از آنها را انجام دادیم. من به بسیاری از آنها مجوز دادم.
اما شما نمی‌توانید ارتش خود را به ایران بفرستید. ما این را تغییر دادیم.
ما خلبانان شجاع خود را بر فراز آسمان ایران فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66644" target="_blank">📅 22:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66643">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در نشست بین‌المللی سیاستگذاری در اورشلیم اعلام کرد:
در ایالات متحده می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد، و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد انجام می‌دهم. خب، هیچ‌کدام درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66643" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66642">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66642" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66641">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66641" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66639">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTxHzvoBKiazieauEgVe34zFtPwFfx9nGyC-S4aYywRdgzeVO7dQPnHtSCVbCcQO6vqMiJrOGzgtvs0x5NbT8NEof1bsQdtv6czeZXR_fiJXHonRlQ3P0FnHu2qQsf090iymJQ1oGuJK5o1XwUYrMyEaRR__wEaE80HAjeZuLunR_MsJUqy2pEuNKVi9zHNRe2jXfOvti-QrJxdqoiM6GhZs9d_h95t1CQvjuOkm3yBH32cpKsJkC3bQvgEz26nD3eHTTaKzTztIZEcmQfSe1JhwA-V6yIQ32ZnwrG6oVY2WH6WL958ZuyWYXwQldaVswQzJ6_oCQ_kSb1QXzlGBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAqrlBkZFz20jIy6xgc7RLL2xxTUx3LjegpXPTdCpDcgJkv4z8VGE29NJRyBUU4tfeJOxv35QAgWGRRC-D8zo8BAzQAfKGXzwTHnaZ4qaxCDVF3dxrp0J1t5Z6ZwOwl_AinJdXq8uW0cyXs60SA5KLKGRNPKBN-Pu46o7R2M8uyjfD8o4Ewmifvgalc4vSGjX92Z2MDq4QUIDR0Axi39dJ6s1SvfMlY44i0KAy-l1_kPgMEA5hmfIK8qNDzH8Om-a5C1ayrl2t31XW_RYpxPvO7zS5ETL2p3xHX0V7ypn5PhNc9np9huJfAy-f4i9hDsZzvlWVuOpMmGyKV6gYjSfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن  سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو بدون سانسور رایگان میزاره گفتم اینجا هم معرفی کنم…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66639" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66638">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4SAhcla65ZwQkAhG0Nixz0NNgaRraD7XCKQECgMxtMlwPL7U-FngmXP0FJt8A4VXyHvGqe8aVxF4XUZd0frXmS_NU0ge9RWkMrGGY2nST90ehtyDVON9H8sB2dhAa3cVJYe6JJH4JIqs44W_qEaYzViA0RFCl_P8RUWs5br35dhmBPlTv2ZKHXfYNxkrVjX8f28IFaV23JvDJl6Ai1ny-Enp2Fy69tgCBP4fX38bmoxug6R_RvXxafkKrYrdp4enjU_WgP7ExQZuyaaQS0YL8y43Q2Tik522psj-3pNhWi1yYXQ2EyTTLYVm3c9vsmKoHK7AajD1nUDg9RmirSbzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66638" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66637">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLOuVFdN_3qhS_uMvTbvajYu8EWjPACF-w8wYOcYZwJ1c6Wqo07e4wU4YBzTXqWp49iqfsh3ZQyymhh-Oa17p3oS1YsqcExA_ppXIg_g7NNWFvf_eP44UQi1CcneDMOScWlerE2pGOKwXkQpZ-F0Z3lmpTPKaxYgp-OsoXJJIl4GeriEjTVfZ4vN19CG9pFhzjeI8Ei0yMlwUyIsPMMwQ6SGCsRBvKcLDuVENnqHEd1qgMNZXjvTADu0BIbmn32qNzTi4nW_MVD-ewTDC-AQQWj-BcNqDrfqV6SH7d2C-2gjv_gU9Xq-mW-w4mL_grWcsw9st_dFokSn65sEIsDs7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
یک دیپلمات حاضر در مذاکرات در سوئیس ادعا می‌کند که هیئت ایرانی آنجا را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66637" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66636">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqeVdocc98gkMjs9mOQ8Ko1lSfEiIOLK3omaBv9biAriorh9XJh4xEf_dAS1AZehX8_JutyVFjkx0-nVaLe0R3XOtUI-HQVN_297V13vy2HyS8wyln1H6v1TBTGDQogME7Yo9sflkFWXfbHqc-GO0luS7ity57t9AXNlr7LI_qACsOs36FZmJnnYp8oOMrSTHeMKwqaQmVP7-NthHP68eOO3EgQRmtL7wYy1U1xnJmlBZuxlQaFMfeHjYhte7QqX79fBKvNFg4IdAbd6-6a-GYn-eWmYZ0ApYSjiOEJ8Gs5s8Xl__UoEK9H52nD4T5YhTACLQniLGJ2aoTOYCiqN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
نتانیاهو و صهیونیست‌ها در آستانه نابودی توافق و اقتصاد جهانی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66636" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66632">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZim1s9cPFQfE4vyVg2xqnJbsMdfVgpg5sxyXED9sTIODagMCSrouBbHYLWBcgy8tAWGOZNpQHEuj8Yxd4tjg9UBoRNILJPDSbit4HJH2jHxcNmcio1OJg9FmP_HG_lt0qX1j7ohvP8l0J9Zp3VTFwgEWyvORWAkMppwFWvpEga2KmeVsIJdZoYiGkvFYAHK0tgJI2wih1ixkrF48kAXYJNi6xv4iDFMNlo_KY0gwVFI_8D3Lc2fVg6ejD0OSXjRYeDyGUjX6O3kVo4vkO8JzFNnzBDcN6F3i0hp7FkanN6PvGgLqbtb3hQIj_n7JH3n85h1ZbqskJO__zIJu-KOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzZ3exCfLqf3TfXWSaXM2D6wexjWxzU0-X2ulDwYjfiwywx5bY7Yn5DbIZ9yguR4-6buMyLRZU_NVPxW4fLHExMLNe_GIP9dXVxCmxah1qxYMA3MkmDU6Zok_W34s9IMnb2b7OewlqSf01uSqBPyL4j1CZTk5dPf2crsTsSLeWKj31-CGXQeFIFPLADcnt0pNRyfb29fk8550dPXKwGO28xEd5jYihNKpq4VOxFZcgJpGXbeLcx_0uCl2P5bdYB521dMY21KxLyreR6AhXOp8FpEuPA8ZGNQn72Wv8wWd8mN8P8NetwZNGyPGg-6r96XrFZK4Xh28-b3Abybz2a3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAn0oQeFrM-BbriUKHF1m_eO3FSuXXfQ6hKUZmXZMf08vYbxGZCeK23oPZ6t6OkN93sRL8bXl4XbRiFooi67CjhParJQBdF3R19JLjXZvgKj4BACyC8s37UujkQtyIK4k4fVAPdVjevNFhB9Ht4mkKj1gZ_k0YLo8dpiY1rvC3H0Ykth-ey6ysR5RulZo6Ak-pA3tWUJEgxFSC9DSkZlP-O6PN5sNp1iDcuWjlgs5zIGJF_c-rhxdtZiIiQ3iLz-RvRZ2Ys0aeAxDL9Wg7zNqGAPybos0nzdYAcDF6w1AYr559s8TBrso6xUI9HvTI48Usgsd3XZp64ZwKUtVhcjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afzWGhKz8TbyJRQa25jqwLv3RdPruRGvrXD9tqmtD6xqkq4vB8XKPDgePE8lasxhrqOG8vj5Ic7-vGBUNRgNekES8i-MEsBU7fNtemshOFYpcYITVFGwWm0AfUh0dIzlcHpX2_WgvkNzknVV7RmIIlX8Clhp_gotK9Az2LSCxiZJKKz8eDG9EtUoecrSFwlgZW0UYME4KK-Ywly0ZxwiQyDLKDe_YZyQGOey4ru8YiHC4C0TwtrAdn476XhJzyjM13YOdlO2VNWw5JlAPRgcTykTp-SvB0YDHFo-6TVoMCYtEny508ytz2X_nxgj30iV5J9A544NVYvcE4dvt3-XOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
گروه تروریستی حزب‌الله که در زیر روستایی در بالای تپه‌ای در جنوب لبنان، تنها چند کیلومتر دورتر از مرز اسرائیل، مدفون شده است، یک «پایگاه هوایی» زیرزمینی برای پهپادها ساخته است که از آن هواپیماهای بدون سرنشین ساخت ایران را به سمت اسرائیل پرتاب می‌کند.
مقامات نظامی اسرائیل در جریان یک بازدید رسانه‌ای سازمان‌یافته از این مکان در هفته گذشته به تایمز اسرائیل گفتند که این تأسیسات زیرزمینی که با درهای فولادی عظیم ضد انفجار محافظت می‌شود، در دهه گذشته با کمک مستقیم ایران، از جمله برنامه‌ریزی و تأمین مالی، ساخته شده است.
به گفته نیروهای دفاعی اسرائیل، این تونل چند صد متر در دل کوه امتداد دارد و به عمق ۲۹ متر (۹۵ فوت) در زیر مجدل زون - از جمله زیر یک مسجد - می‌رسد.
به گفته ارتش، در داخل تونل، که به اندازه کافی پهن بوده که یک وسیله نقلیه استاندارد بتواند از آن عبور کند، حزب‌الله پهپادهای ساخت ایران را با استفاده از قطعات قاچاق شده به لبنان مونتاژ کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66632" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66631">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66631" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66630">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QednTlioUa3MqEKwKMw2_6ZhJ0pfzjazyOMJvs4Wls73JlfSGzy2pxEowPdqNq6GVpcsaLJ7rHvMW79I3E_rcBGowv2-a8P4vv5dloOzMw9YAS5X4TInUXvG7O_MXxwRaeSlJn2rsdG_x_mw6s1jZBZ99w-XM0HxV5qF0lPjbKi3WNLN2Neff51inJDOpNvd9AzcTrbbdaboamnuRw1Mxv7xll292V5mmSg-EROF16OhbI8HT8qyq8nSVXx79AVjNDcbZr1M6gdjVYndfSBScDXo0atkDWaEys2lZNka98Ev5Q9j9w80lVHTCil8M9LJ865bvtgOt1gfyCtlzPpCng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66630" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
یکی از اعضای هیات جمهوری اسلامی به صداوسیما: «اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66629" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66628">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
قالیباف:  خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم. بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند،…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66628" target="_blank">📅 20:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66627">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYc9nSun1vg1D3IxxSRbMcQPjVPkt4kAR-jqz4fYQHxIiZiqSG1aQilCAm7qq54CADClvOSR--QGQDXSdzOtkoLJspHRnKGhEgA11C_a7SH_iCsNPpOb7E0jzyi1R22iRq97fFLOWUQvnUY-8HsKzsoD7ZCw37XR9TRk7B6d9zyKy1jptx6s7XjAVVeqAmmOGm62tL2-KTNrTWC_Wt7jCqb__sWCyH3pJlN1KmuieiUETE8A9pVU2Kpd9_eSYKnNfmH-VfZ7NLCDGSlDVFpq6iK1SsqGeHCLyI3QmdpYCLXuo1oD_xQ7JbfojkLMvFqY6d1ZUEi29796ZMfkaSOqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66627" target="_blank">📅 20:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66626">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛خبرگزاری فارس:
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66626" target="_blank">📅 20:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66625">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66625" target="_blank">📅 19:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66624">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=azn75r3uaSl2hC6JHZr0mm_VKlWHtU5U7BNoSHJKg7kUGvynCwhlEim5ezjxO--hNhQlIEbw3rLANBOkTvAs7xR1vfRgetXvZt6pxlOfE3tOUJTNXYw9TyHvvhN0PkiZlCjVpBj1Ir1iDg_U_TBrOb9vuaP_MIJfY7fqh3iEH7M77G-A9mORmgfT_L-NDIkViHOROHoGSngiDUCyJVuNCvfjC1uMS-UdAXG59f4vJHfWG_nUttjlgxiiQDGn7dHI3_C6rch4smd6s5BbHzRkfp4B1f0JVkz0LWY2o7EE8wksRAConTBuUB05uDMxpstQ-w-bC4b7pbS26yXNqocGZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=azn75r3uaSl2hC6JHZr0mm_VKlWHtU5U7BNoSHJKg7kUGvynCwhlEim5ezjxO--hNhQlIEbw3rLANBOkTvAs7xR1vfRgetXvZt6pxlOfE3tOUJTNXYw9TyHvvhN0PkiZlCjVpBj1Ir1iDg_U_TBrOb9vuaP_MIJfY7fqh3iEH7M77G-A9mORmgfT_L-NDIkViHOROHoGSngiDUCyJVuNCvfjC1uMS-UdAXG59f4vJHfWG_nUttjlgxiiQDGn7dHI3_C6rch4smd6s5BbHzRkfp4B1f0JVkz0LWY2o7EE8wksRAConTBuUB05uDMxpstQ-w-bC4b7pbS26yXNqocGZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام ؛به ایرانی‌ها می‌گویم اگر صدای من را می‌شنوید:
وقتی شما از حزب‌الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66624" target="_blank">📅 19:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66623">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSWIdyt4SY2HcP_Sg6rXv3UEtiZ3Gb3TNXhSZXywwT4vyfRTEsIN7iNzRHUfUZZQHD1ztExRTL3km1iu_f8xbUQ-xpFzEjjwZ9tTqGoKhX489CVAKWE5iD2im-m9y9mJTLFMrGe6JkJ--PzCZW_QKJpn75Wt8zE2AHuvyi8LVnlDOOvOwU1mlmMB_UtLg0FdNZ7ku2mr2RqG4Nu3ffY5RjK_P8tdNc5vfl4UZwvfkLFkz72WxaZRz8zwqeWgZ_xe_zDkbYr1rzr3pogroX5r6LvxDULeMfepI8iI2QS4YHvTBPbkhWrj4QV999BZDhus3CQ3R24meuLzfYdti89sgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی اسرائیل مواضع گروه حزب‌الله را در اردوگاه البریج لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66623" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66622">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
رویترز به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد نخستین دور گفت‌وگوها با آمریکا در سوئیس به پایان رسیده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66622" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66621">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🇱🇧
حزب‌الله:
بار دیگر رویکرد مذاکره مستقیم با دشمن صهیونیستی و جلسات آن و آنچه از آن ناشی میشود را رد میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66621" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66620">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK5cyeWGiIEyH-LgNgm97vXisi8rVISI18k4Q-S5etX2DUVTkZhxyi1TCQXM6NiwgXV7LlyYPuzJSHdPDv6_1CxyHZCcKztY8mqeiCcc9Nmwmro37j03Qq99Deasj2Yi1VN6ejR5equ4Rzb-5c0RIdlaF2xxmRtjKpgcTwvWp5tZ3SBCOKf4K_ilHPlbG8KK7J1KS15d9_aiESCpx3DhNYn-W4YlibJmJCdRRtAVUDgzrVwColqzw4vYdN4Vt6XOxgzu6MXamECy1f_zJdj_iRrbB979bn2dDET1hONU5nZtC1cvuvnJityaAQCLXVl0GhonuRkN3I3H-0gN2PArlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بند اول تفاهم‌نامه اسلام‌آباد:
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66620" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66619">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
اسرائیل هیوم؛اسرائیل سه شرط اصلی خود را برای پذیرش مفاد یادداشت تفاهم مربوط به لبنان اعلام کرد:
خروج کامل گروه تروریستی حزب‌الله از شمال رود لیتانی
نابودی کامل زیرساخت‌های این گروه در جنوب لیتانی
اعطای آزادی کامل عملیات زمینی و هوایی به اسرائیل برای مقابله و حذف هرگونه تهدید امنیتی آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66619" target="_blank">📅 17:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66618">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
رئیس ستاد ارتش اسرائیل:
آتش‌بس در لبنان شکننده است و نیروهای ما باید سطح بالایی از آمادگی را برای از سرگیری عملیات رزمی حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66618" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66617">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355294b30f.mp4?token=FOjDuqmYhszQ7H56uoS-oTWhbT8tMBpbnTDq0jII4A11vhNpHJgNlAHBZbnDH0RIpSgdwb62t-Ajo4F2refrbhEhN28gvNoa8B0SoNzDtFfMadah_3S155EzCt64hvtTdVffTcikZuAxsDQLhXWVsHNUp3k83u7OoqLe_pFdg42rxm4bFIuJgeVDwGt7prW0pxt3oZAuqm_4Tktqu0TSywLIYIXUyPprKcJT5tcECjG92HdCYkFJLFhXTCHuQm3qRj94n4JYO_xMQQjB8B6Ru4C9LS8stpZY-6GbNBEsAkRzlPCDRB3dGaOc-YpaurFVn5y9aCmN2-fEwJjJZvC7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355294b30f.mp4?token=FOjDuqmYhszQ7H56uoS-oTWhbT8tMBpbnTDq0jII4A11vhNpHJgNlAHBZbnDH0RIpSgdwb62t-Ajo4F2refrbhEhN28gvNoa8B0SoNzDtFfMadah_3S155EzCt64hvtTdVffTcikZuAxsDQLhXWVsHNUp3k83u7OoqLe_pFdg42rxm4bFIuJgeVDwGt7prW0pxt3oZAuqm_4Tktqu0TSywLIYIXUyPprKcJT5tcECjG92HdCYkFJLFhXTCHuQm3qRj94n4JYO_xMQQjB8B6Ru4C9LS8stpZY-6GbNBEsAkRzlPCDRB3dGaOc-YpaurFVn5y9aCmN2-fEwJjJZvC7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منابع داخلی:
هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66617" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66616">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd4iysk00rCA48Sd6txXyLOHic0m1OXdnGNgJTydPTd6vCVMzkRZIyOpQPm3rUtUVnNkAIGPS2FsHT5BBM7yrFLAZ-xFfcsIOxyUJbYwtT1RfX8OAoJJQRUv2fZZ3f_Ph0Eu-gjdY9DHN9BojeELorTWyA42g28iwC1cvhGsSLQthU4PS-QnCkEGWom7eQcbOg0Z-8xe-IzKyRE_pJf6pP2elPsDgxjQpxTPC29kOIiCnrB3-8gXAOjFLrhk0-5OnaktWLHCPRAgktzC4J_-MBIW3jZJo-xHJqU8K7YW1d37CA8rr79Va8TUR4sU77rsETlcCXQu1ppCGkbsC6LJJq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd4iysk00rCA48Sd6txXyLOHic0m1OXdnGNgJTydPTd6vCVMzkRZIyOpQPm3rUtUVnNkAIGPS2FsHT5BBM7yrFLAZ-xFfcsIOxyUJbYwtT1RfX8OAoJJQRUv2fZZ3f_Ph0Eu-gjdY9DHN9BojeELorTWyA42g28iwC1cvhGsSLQthU4PS-QnCkEGWom7eQcbOg0Z-8xe-IzKyRE_pJf6pP2elPsDgxjQpxTPC29kOIiCnrB3-8gXAOjFLrhk0-5OnaktWLHCPRAgktzC4J_-MBIW3jZJo-xHJqU8K7YW1d37CA8rr79Va8TUR4sU77rsETlcCXQu1ppCGkbsC6LJJq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66616" target="_blank">📅 17:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66615">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwipsXxZSz9wF-7dzX3lGY5LShWkhFNDj3uBQzRA8xVP4EdZ0av5ymiWWNxESHTUQbIMVMLJkOwFIPeLEmHtXlBDvOY_-y9s2_qGfyqyiX7wr8cgqo0zTKwSUawoK0XqK2TDZDmi_5M3HFkIpCidN15CtzWZbzyvu2kxLa67LI5IAMQ4ErvhFZv9E53ObatZ0ulFEPqZ2XlRR4obdoiSSNd46cElGWVju6juWN4Drq7udUqhfKWYKQDPyIZihdudIUx_142Err0FCqSc7MsbOxVGt-nJcPpEBe4fKcVu90dF_5PxKIvtM4TJAlBtdoo_dC6La0BPXs-BT05XewuuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66615" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66614">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=Nlg38XvBHwkNq5DMgxD1glhiZ2COszHvkNk500Fgeg6CM1-tSLW3ZQjBr-nnky9wYYReEArES53ihrb8EcpwqTl_LfMoo1X0YMKRifPGFP9iLpa28cXSO3bvMZpUsxgYJyu6KaoN73eurCXxTNfekzmrEpVu9oWBjjSpUkl7bQrvi5T7-NG79i8l8-c-oc8oYBLDG6V0QBd7X3qyaC9jxEkxr6ogz4lN1iMGySgMVvp9GwFUCyElLWYItijZUylW7DtgkPXf3M34ITdEGdXJzv31dWssjtc8JX_TmQQ_D2Qg1LKPTysCXqV9pDsGoW9Ti9B4kXAcgdOV5s-aEXUaLrhI1FYsJuHKxQrDcHKsCrmKnMgcA56Ee965c-HYljie74tkltcoiMrgPru8eji9BXUJfKUwqvDPbgomQAsTVNDltDaHdNOrp5Qjt48J8eoLCKKWkPKFvrWOA7IfbLezqD5N1k8u_I5OiprgY77KVvy9NtR7hBNXPJ38nPhc8mnlUYS6qQ-SSlgfbUjw3TPbMaS5e2tL7sePpz1TWE3M-d1Qjbd8ceEnVgldEc1hv1UjFpHRmn0zgqMMAOuGdcNm92wPuJuutZY-bdjWgihatgK7H5O5tarj8ir7MkquBkxJejm8rgGkgIEllQt9pifj047sQXFow8rYsM3fqHxix-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=Nlg38XvBHwkNq5DMgxD1glhiZ2COszHvkNk500Fgeg6CM1-tSLW3ZQjBr-nnky9wYYReEArES53ihrb8EcpwqTl_LfMoo1X0YMKRifPGFP9iLpa28cXSO3bvMZpUsxgYJyu6KaoN73eurCXxTNfekzmrEpVu9oWBjjSpUkl7bQrvi5T7-NG79i8l8-c-oc8oYBLDG6V0QBd7X3qyaC9jxEkxr6ogz4lN1iMGySgMVvp9GwFUCyElLWYItijZUylW7DtgkPXf3M34ITdEGdXJzv31dWssjtc8JX_TmQQ_D2Qg1LKPTysCXqV9pDsGoW9Ti9B4kXAcgdOV5s-aEXUaLrhI1FYsJuHKxQrDcHKsCrmKnMgcA56Ee965c-HYljie74tkltcoiMrgPru8eji9BXUJfKUwqvDPbgomQAsTVNDltDaHdNOrp5Qjt48J8eoLCKKWkPKFvrWOA7IfbLezqD5N1k8u_I5OiprgY77KVvy9NtR7hBNXPJ38nPhc8mnlUYS6qQ-SSlgfbUjw3TPbMaS5e2tL7sePpz1TWE3M-d1Qjbd8ceEnVgldEc1hv1UjFpHRmn0zgqMMAOuGdcNm92wPuJuutZY-bdjWgihatgK7H5O5tarj8ir7MkquBkxJejm8rgGkgIEllQt9pifj047sQXFow8rYsM3fqHxix-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت
:
بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66614" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66613">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در مورد توافق ایران:
من یک گزینه 60 روزه دارم. بعد از آن گزینه می‌توانم هر کاری که می‌خواهم انجام دهم.دیروز در نتیجه این تفاهم‌نامه با ایرانی‌ها، 19 میلیون بشکه نفت خام از خلیج فارس خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66613" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66612">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=RxTl3wXgTP8qh18X6cpsT9sEpHt_Il_jyOHO2uJ02kTeOVsrMpARk3zIVNNQlJ4-RRs2lL0lkj4hy_EWFHMtYer3htBQffjvKboDnjM3E-G-cu-MzaeLzkotgMNDACd0BeqR8dnmBYsXd-0T2oeLkyFIpGHw_6HOEXkiFeoQZ-Ra_iFFZ_KtNL-CUWNr_Arn2SkkVMvlzaJ2MPoyrIuNKug_xjm_uiFAJoxlPIUSox27whCCkFzG40cDJ3x3sd6PxylLpsCkv3su1vdopA8iAMoLgHUMeJ_KiCHS4ZrP_l_SRBHWtD5te4RV7o_2o4Xt3-oZrixpuOEiX5ozKVl_OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=RxTl3wXgTP8qh18X6cpsT9sEpHt_Il_jyOHO2uJ02kTeOVsrMpARk3zIVNNQlJ4-RRs2lL0lkj4hy_EWFHMtYer3htBQffjvKboDnjM3E-G-cu-MzaeLzkotgMNDACd0BeqR8dnmBYsXd-0T2oeLkyFIpGHw_6HOEXkiFeoQZ-Ra_iFFZ_KtNL-CUWNr_Arn2SkkVMvlzaJ2MPoyrIuNKug_xjm_uiFAJoxlPIUSox27whCCkFzG40cDJ3x3sd6PxylLpsCkv3su1vdopA8iAMoLgHUMeJ_KiCHS4ZrP_l_SRBHWtD5te4RV7o_2o4Xt3-oZrixpuOEiX5ozKVl_OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی‌دی‌ونس:
باز شدن تنگه هرمز، پایان دادن به برنامه هسته‌ای ایران - این کارها قبلاً انجام شده‌اند.
سوال این است که اکنون چقدر می‌توانیم با هم به موفقیت برسیم.
آیا می‌توانیم روابط در خاورمیانه را به طور دائم تغییر دهیم، یا به انجام کارها به روش قدیمی برگردیم، که ترجیح ما نیست، اما مطمئناً چیزی است که می‌تواند اتفاق بیفتد
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66612" target="_blank">📅 16:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66611">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
‏پرزیدنت ترامپ در گفت‌وگو با فاکس‌نیوز:
ایالات متحده می‌تواند به «فرشته نگهبان» تنگه هرمز تبدیل شود و ۲۰ درصد از نفت آن را سهم خود کند. «اگر لازم باشد، کنترل تنگه را در دست می‌گیریم. آن‌ها را به‌شدت در هم می‌کوبیم. اگر به توافق نرسند، از کشتی‌ها عوارض عبور خواهیم گرفت»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66611" target="_blank">📅 16:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66610">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=pxe-mMNU3OwZz3F5OlqWf034ADXjuImseVilyGaluVWQYpNlW9T733QA_a47bnIFSunLTT6YiuGlS7kGkFIIiYMMbH2PMaxzoTvCqbTzfEqTsXXxiFArB8s2GNGuYV1fOWpmx9XDGDP-wRSbjOchMcRGAGO46Gxv-0ILEqN2pa_12AcPrYFpcmhRtlT75TyBWl6GEOUzmFR0sg1rzYVQNGxJTsdhmHk5RhXHI11EfpSZJEOGcUZvwAbmdeNLkGLZ7SwoB-zwonX4SjiGJuRcIHRWBrgFbRokDrfrYHQ1vp22cPTswNdDe2B530OBe-iiqeGD3_OUefBuODux43OmIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=pxe-mMNU3OwZz3F5OlqWf034ADXjuImseVilyGaluVWQYpNlW9T733QA_a47bnIFSunLTT6YiuGlS7kGkFIIiYMMbH2PMaxzoTvCqbTzfEqTsXXxiFArB8s2GNGuYV1fOWpmx9XDGDP-wRSbjOchMcRGAGO46Gxv-0ILEqN2pa_12AcPrYFpcmhRtlT75TyBWl6GEOUzmFR0sg1rzYVQNGxJTsdhmHk5RhXHI11EfpSZJEOGcUZvwAbmdeNLkGLZ7SwoB-zwonX4SjiGJuRcIHRWBrgFbRokDrfrYHQ1vp22cPTswNdDe2B530OBe-iiqeGD3_OUefBuODux43OmIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره عاصم منیر :
من احتمالاً در سه ماه گذشته بیش از هر کس دیگری با فیلد مارشال منیر صحبت کرده‌ام.
بدون سیاستمداری او ما اینجا نبودیم.
او یک رهبر نظامی است، اما فکر می‌کنم خود را به عنوان یک دیپلمات عالی نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66610" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66609">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=sV7IxxmqogbN7nUX1R2tAbeD5LAPjqdcg90gWy1NPGS0vh4XETihfMDcFpulqkcM5LAd4vb1QelYGM17EgQ9ETYQ7ZAihlFVWDTpVPA_NRIOCsPj8gFZYlTAQmYuaF85ptdxJNXL5ayST0bDphdBZ3SgVtQ8shlANwy56SoGIF7FeRE1sgqzbBBkisjjaiqIe7efJMORHcfsnOUkHOILmIrYMI3LspbIlDJP6Ss9Catjjy51RX_XgSFu4AXQH3TAyDWq9pQSfwv-Gufjfw6dLKM15_fQlFTUrKINSESHYnMSO5CRFl6bKh1zla6NOrJ4ylQemc5ZsZejgi3BCZFAWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=sV7IxxmqogbN7nUX1R2tAbeD5LAPjqdcg90gWy1NPGS0vh4XETihfMDcFpulqkcM5LAd4vb1QelYGM17EgQ9ETYQ7ZAihlFVWDTpVPA_NRIOCsPj8gFZYlTAQmYuaF85ptdxJNXL5ayST0bDphdBZ3SgVtQ8shlANwy56SoGIF7FeRE1sgqzbBBkisjjaiqIe7efJMORHcfsnOUkHOILmIrYMI3LspbIlDJP6Ss9Catjjy51RX_XgSFu4AXQH3TAyDWq9pQSfwv-Gufjfw6dLKM15_fQlFTUrKINSESHYnMSO5CRFl6bKh1zla6NOrJ4ylQemc5ZsZejgi3BCZFAWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: متحد شما اسرائیل چیزی شبیه نسل‌کشی در لبنان دارد. مسئله اصلی توقف این است.
جی دی ونس: خانم، من فکر می‌کنم ترامپ و ایالات متحده برای توقف درگیری در لبنان بیش از هر دولتی در هر کجای دنیا تلاش کرده‌اند.
صلح هرگز آسان نیست. صلح همیشه به کمی کار نیاز دارد. همیشه به کمی بده بستان نیاز دارد.
اما ترامپ نه تنها به صلح بین ایالات متحده و ایران متعهد است، بلکه به صلح منطقه‌ای نیز متعهد است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66609" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66608">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66608" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66607">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldhHRenpqVMg03Ru5lK0HkB-uv5qrIh06lexlQWR49j_nr7oJHLyFEUiwAIyaxhRLMiOpT4ZsIoi7OYOjGSMBOqHihKqXZ7Qrwr-mvcbrEI8YHq9hIkr46xb6hSIG7jhV40KKETibYod5BVaGKiqcYQQmSmE05XgOWUxZQr_f8GtC-GY2X4KfebtJZadID6oJfz7SmqpD3h0Cl8y6xxovZg2AZn06U0rs44Yaf9V_oeYthgyHcAlnHPffmwMISiSXrQW3132RK_oOtXdvXbHpFOaUj_HHXoIgmIrDPZqN8pWVQ4ZYxiNJ2UP0lGaFG0mZdhSGdBhOeOHtGWeoOOKMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66607" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66605">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvcUXCI_a4FJi4l77RY82gjv6rqz_JF4DMmXdFH_rs2n4XRJCoBlin339at7MXcl3t1T_LNaTVStPN-sKGVOY7t692968L87vayQGW3qR0klna8kFgTzwTts8xDVO86991ctdQVtOfxn2F5HDj5we-sGOaSMpWXVar_qfSzoCICk2FOetuVfCrbu9Z0bJBArQVjgq9ZKPAvWtWDOMFEWcbZYhV03eCQsddrGfG3vSmpegMcIPhDzrcdR7zB-Wl2k1n74cNlt5bRAs_DPyyr9RcF6xoAVMXhcR8oj8YjoL1a9nFtuA0CSWiRl2Ln9aED471nTgTI2Oa0-eQ6upra1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=CJW1Jtj4272gFDxG06wT-2N4OK1gPlh3Mg2fvY4uOJJcyyudxAaxvBFT1xy6uq2ZBJyKZbijKnCOFy7W32YcG58Cgvr20lr4p_AeeI9glljEgqbEhu2Z2_9U8Cz5_ydBU5CmbEZLfZ3nQILcMn1GJfjrfKIBglMy_9Me9pdS6Rwo4OmrtLWE0HrdCAq9RQBkh-pGJct0qqedrRbKL9h7Ej2kxkGjLvAhJWObHmH1Fz_FuX-FGEm9MHAZhoYGamUOgwxZMX8dIDULO_2fprZHxMU-bOapseaotQkFysq-KkZr1-FRtehT23P-e9uahzJy0oEsOMhpFtMM1oLhBxnJkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=CJW1Jtj4272gFDxG06wT-2N4OK1gPlh3Mg2fvY4uOJJcyyudxAaxvBFT1xy6uq2ZBJyKZbijKnCOFy7W32YcG58Cgvr20lr4p_AeeI9glljEgqbEhu2Z2_9U8Cz5_ydBU5CmbEZLfZ3nQILcMn1GJfjrfKIBglMy_9Me9pdS6Rwo4OmrtLWE0HrdCAq9RQBkh-pGJct0qqedrRbKL9h7Ej2kxkGjLvAhJWObHmH1Fz_FuX-FGEm9MHAZhoYGamUOgwxZMX8dIDULO_2fprZHxMU-bOapseaotQkFysq-KkZr1-FRtehT23P-e9uahzJy0oEsOMhpFtMM1oLhBxnJkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کریمه در طول شب پس از حمله پهپادهای اوکراینی به بندر و سایر زیرساخت‌های حیاتی
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66605" target="_blank">📅 16:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66604">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=i-orfuOY8sm1q1ECVh7TMcly8uyT8ZzkOY6L8DM1C-7R6IDO6Vg3YWZhtKLFyPRHlMHlbckaW5A7XDDceMPuY_lMnwtIGpcV1EF9m0NXM-gQhwYYrNLI-aOa_sgb0_FlDxtNcgqpe3bVUaKrv9DbQgyMJ14fJMPFPtebgb3KbZiZeXWrxhsof8WEBehOYDUPlbvMsf4K5OnlgBUtmrd9xiKb1GaunGFy83S0UKe1S4WihoMbZx_a1ZbRYDH0X-5gPUFe_QRfME9TMI75wY5FoHRHN37B9bQBaCwIOzPBNpkzRhM4_cI3-rd8pbI4uE35xFFzIG-bQMgdSZoiqLMRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=i-orfuOY8sm1q1ECVh7TMcly8uyT8ZzkOY6L8DM1C-7R6IDO6Vg3YWZhtKLFyPRHlMHlbckaW5A7XDDceMPuY_lMnwtIGpcV1EF9m0NXM-gQhwYYrNLI-aOa_sgb0_FlDxtNcgqpe3bVUaKrv9DbQgyMJ14fJMPFPtebgb3KbZiZeXWrxhsof8WEBehOYDUPlbvMsf4K5OnlgBUtmrd9xiKb1GaunGFy83S0UKe1S4WihoMbZx_a1ZbRYDH0X-5gPUFe_QRfME9TMI75wY5FoHRHN37B9bQBaCwIOzPBNpkzRhM4_cI3-rd8pbI4uE35xFFzIG-bQMgdSZoiqLMRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیستی که صداوسیما از موافقان موضوع مذاکره با آمریکا منتشر کرده و گفتن که این نفرات به مجتبی خامنه‌ای خیانت کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66604" target="_blank">📅 15:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66603">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
کشور قطر از آغاز مذاکرات میان جمهوری اسلامی و ایالات متحده در سوئیس خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66603" target="_blank">📅 14:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66602">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
خبرنگار صداوسیمای جمهوری اسلامی:
یک دور تبادل پیام با میانجیگری پاکستان میان جمهوری اسلامی و آمریکا انجام شده و هیات جمهوری اسلامی نیز با هیات قطری دیدار کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66602" target="_blank">📅 14:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66601">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF630zUV0yFqxuk8KhoNmpKTSb7j8oojSBeZd6tO1gxS82WV1j6P2fFsANbEPFAO91BLcK8pfw4NQwnTbEtziUeOffMAK2wTB9Fm1EfJlSCWsnV1ijdNQXtvuQmI6oUQ0QnJjxbS1ppNh7DJY9uGKwgJ8gcO3EiOb8Pgb8V6DwsRJPw0JtmWJ5WDAuz2PMZNMh633SCcKv2U-Hi6jmpcWQ0XrY44syVhT-99cTZefMM7pBulGtAfhnUauuA7Ih9qvQ8XJ1eIiKncRUDoaWlKdXwke2XPNDADXBkKsI1Wthjidt72cedqUsmCNVGyjd2PTFTON9s_uVytrjhi0UP69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است. بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66601" target="_blank">📅 14:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66600">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66600" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66599">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🇮🇷
پرزیدنت پزشکیان:
«از حق غنی‌سازی خود دست نمیکشیم»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66599" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66598">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=u7MxcQMU4zRNyiZw-VSwknpDGOwT2ueQZThi9L_x2Dp96Jo3Hnwl9hKuLZLSdLTR8GXf55fLqn_TgAnaxm5ow2jF6UqQbNojyudxwCuHPiMDQQGAq796v40ZA4bu3Ns0WSUU1PdwcidSt2T-XILtU-pmDbc3pHBDDjdBunLkRLuyvbojXztFeZU06sjWVnID5kc4IsX9NX1SEEXhszCwR41ttdLBDxFHaJPXTQJ4mPlbHCZtuxfa3ei3UhbRS4TWpfS5k-xyS6RUUs_oMPb-febLToxsQa52ly6agRYAqnya94HUX9TinzKiIVTWMCHJcRc-q0l9o7275HGTkYd2Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=u7MxcQMU4zRNyiZw-VSwknpDGOwT2ueQZThi9L_x2Dp96Jo3Hnwl9hKuLZLSdLTR8GXf55fLqn_TgAnaxm5ow2jF6UqQbNojyudxwCuHPiMDQQGAq796v40ZA4bu3Ns0WSUU1PdwcidSt2T-XILtU-pmDbc3pHBDDjdBunLkRLuyvbojXztFeZU06sjWVnID5kc4IsX9NX1SEEXhszCwR41ttdLBDxFHaJPXTQJ4mPlbHCZtuxfa3ei3UhbRS4TWpfS5k-xyS6RUUs_oMPb-febLToxsQa52ly6agRYAqnya94HUX9TinzKiIVTWMCHJcRc-q0l9o7275HGTkYd2Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار هیئت آمریکایی و پاکستانی
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66598" target="_blank">📅 13:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66597">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=IkHMyqBD7Vd931fqnqKlH5DfNUVDGE9_78JHB667m2WyUxE8qtK7MBWrFis-e2PKYGAyCxP2i8952tKzIryj55pM-WMmUyOGBj350x4Qz8JKx4gd7PzM50NaWIbKvVLvo9tfJo_wDm6XR7589V56u-MfnN4h63j00aQ0fCGdZJtcUVnlDlFNXbZ5CzZdifC71hdjWD8m4CTrfogpd1LZHTBreZO1maMCKv5bgP6p8FSvLbWfPtr50CXTPCbRVTDo7yJCOGlp8GlEuyhwUO5aJOXmlMpuG03nOdykNHmdleocXUwIoH2QeUN8BvtFfgHATzFQwLBCPKkC1VHEi3lpgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=IkHMyqBD7Vd931fqnqKlH5DfNUVDGE9_78JHB667m2WyUxE8qtK7MBWrFis-e2PKYGAyCxP2i8952tKzIryj55pM-WMmUyOGBj350x4Qz8JKx4gd7PzM50NaWIbKvVLvo9tfJo_wDm6XR7589V56u-MfnN4h63j00aQ0fCGdZJtcUVnlDlFNXbZ5CzZdifC71hdjWD8m4CTrfogpd1LZHTBreZO1maMCKv5bgP6p8FSvLbWfPtr50CXTPCbRVTDo7yJCOGlp8GlEuyhwUO5aJOXmlMpuG03nOdykNHmdleocXUwIoH2QeUN8BvtFfgHATzFQwLBCPKkC1VHEi3lpgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم مذاکره کننده جمهوری اسلامی در محل مذاکرات:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66597" target="_blank">📅 13:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66596">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=PsR2K9Um-exja7b6KihfCQXc0bdgsT6njdkdnDFmj1GkmE2FSXCQpDla52GCE5zYHtlWmAhFU7Cr7fcC5k8TFWA0ctfbFp2m3Et2yZ3jhdB18McbOk7jVvl2sji168ZeKkZCEDBqGRYDHgYiNX4ujwWvwsnkfplhfdq37U2uqxBjlPwqP5E0hKglyLeLJfC6g_Qb06TR7vgfND-Mu6svGVADJUtDUL7_iTHMydBU6JpnMqmVyYCxhRHYbxpTyMre1a48MblmnnRTr-VqotOJTgIvI_FmzH7Mzpv-Pum__ENiVn1s5wtVy96u9gnhmety7WQ7TuvJfm4SX8vBDRO3Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=PsR2K9Um-exja7b6KihfCQXc0bdgsT6njdkdnDFmj1GkmE2FSXCQpDla52GCE5zYHtlWmAhFU7Cr7fcC5k8TFWA0ctfbFp2m3Et2yZ3jhdB18McbOk7jVvl2sji168ZeKkZCEDBqGRYDHgYiNX4ujwWvwsnkfplhfdq37U2uqxBjlPwqP5E0hKglyLeLJfC6g_Qb06TR7vgfND-Mu6svGVADJUtDUL7_iTHMydBU6JpnMqmVyYCxhRHYbxpTyMre1a48MblmnnRTr-VqotOJTgIvI_FmzH7Mzpv-Pum__ENiVn1s5wtVy96u9gnhmety7WQ7TuvJfm4SX8vBDRO3Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند چینی وارداتی
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66596" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66595">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsEjn0Jjtkoeda2sh-m4BM3TB2Lvm5dm04FoEUeTIPnytZXiTcd1HYbkC0xeUqBkea7B45DxLavdPwHg9-n8iGcq89DcxQzU1KCoEm_3Lvt8tb_S-AhcSaKVwGaenLqQ1lgpdGdL2xPtUuWHDzwwpT7Jofqi5BQ3C9kCpToYNny30LBEyJPB599aSV0Y3s5NvWA11v9uPRr2I7nHH6JLreg3gvuQrHqy53_DJuf1dfuE7bf9VclY28HgZwqyuIB7d2OkwKCJCyV_innspCSGhJwLdM0itoH5vj0NTUu3Q8xXF_PWKo5sIUogFvfi2Z30I70GHjp6OOVG_hKDVjZueQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
آمریکا قرار بود با راهبرد «صلح از طریق قدرت» ایران را وادار به تسلیم کند؛ حالا که شکست خوردند، از سر استیصال اصرار به مذاکره دارند. اما دشمن نشان داده که عهدشکن است. باید مراقب بود؛ هرگونه خوش‌بینی مورد سوءاستفاده دشمن قرار می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66595" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66593">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmePG4-SU37GyzNB4ynizikcMlGEezO592iRAv5vIH20_46aY2i2HdKfiDzSix6k-aibJWWPfw23b_n2hF1hgwAEW6wB2P6lK-ddg6MfbbQnknIYJ0E7H4izMy0UfKtXM59WIEuLp0HPOSIUAj0yXFkAUMRQvLNiZZivwDZPbJdajPvpYD8muuQDUbR-dhy9BfvMLnSp6onqrHqoMY7bS7YCaHEvIohshvaabExgOwMrfklrkHKgvt9_89G5mfVjzoxbazE9fY1H9mGhvi8bbxSA8njBlmh10HBc8eFheyxOomu_t25y7odiiBfCa9uRM5wf_DdqnYxqgyhKPOhnsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=GAe2lVjOZWNN6noZ79YuE_2zQqAifTbvnrxvonXHi8s35fK-DrUxnE64qPmzAAvDGTyagEdS2hkpgTBnX28-TDjOb9JLoe9bBuq1p7PdHbGXSbRmvejYx6160RVQ_SkiWTSz3PNZUuh8cc0hL5Vldu8sDdcZh-_xHiArdjRqJdX9bV8rU6vkrYDEgtulIGen0sK7Qg2HwAdJDyxau-XfzizBKIePfgxhQVGvSs3mAVoW-qHfaRkdvMYc4zPYDPKuar1286HAm_l08NQda6mlkK3DMk2Js1cDsGVhI3lGzv5AqVsKeQOFth2AFOXNx8ggd9qWNedAv1lBL3JHowJsew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=GAe2lVjOZWNN6noZ79YuE_2zQqAifTbvnrxvonXHi8s35fK-DrUxnE64qPmzAAvDGTyagEdS2hkpgTBnX28-TDjOb9JLoe9bBuq1p7PdHbGXSbRmvejYx6160RVQ_SkiWTSz3PNZUuh8cc0hL5Vldu8sDdcZh-_xHiArdjRqJdX9bV8rU6vkrYDEgtulIGen0sK7Qg2HwAdJDyxau-XfzizBKIePfgxhQVGvSs3mAVoW-qHfaRkdvMYc4zPYDPKuar1286HAm_l08NQda6mlkK3DMk2Js1cDsGVhI3lGzv5AqVsKeQOFth2AFOXNx8ggd9qWNedAv1lBL3JHowJsew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رشته کوه علی طاهر، دژ استراتژیک حزب الله در جنوب لبنان:
طبق نشریات این سازمان، در زیر آن، تأسیسات «عماد ۴» - شبکه ای از تونل ها، انبارهای موشک و مقر جبهه جنوبی حزب الله - قرار دارد.
یک افسر ارشد ارتش اسرائیل فاش کرد که عملیات روز جمعه، افشای یک شبکه زیرزمینی حزب‌الله بود. ارتش اسراییل این تونل را محاصره کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66593" target="_blank">📅 11:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2s-ahD3_V4qyZLZdRUBa7aVTEeKYLAE30txD-l2HKpQf2LcG2UtfAhKsr9WWICfcYxzt9RdqXjVfAWCFqvOaO3s_5LQpFSbvrS1Mvh0Rg6CrZlkL2vUWK9cl9PeLcmwTm_wC1bozmXqfWbrv2PvvxIDRZX8cWRfSFqqLLRIX8IV0rvL1nguvfKW42aA8vOIGGHyYPaK1KzLSD7S_P_C3xcoWz5q0zne73aiVFRXY0A-9CsrE7ct9VumV1X_eBDM-NwhBuYVnfkmo7insgS5s5y7vqzECx7Za0XsWuTuHiNRmV2sL49vJvcIkVy3N6Swg3l2iLpEmmSE-B2Mej7KWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پس از وقفه‌ای بیش از یک ماه، صادرات نفت خام از جزیره خارک از سر گرفته شده است.
تصاویر ماهواره‌ای دو نفتکش بزرگ را در پایانه صادراتی نشان می‌دهد که نشان می‌دهد محموله‌های نفت خام ایران بار دیگر در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66592" target="_blank">📅 11:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=Ng12E1HXZCSzdED-T-CT6TbTDQxEZ8zWljXLd6xWZkJNPl-_GUk9YYiZJfQ0qumnqwXIpocMf58dkvuAxzSe3n1ZI2uuRTd3yQXcD7aP4W1URNVsRsN-lOAFbPjIqs_YqLkModRBiAILrKF8e2hKxAF4VszPOck4AK9OVFesY0ThSYd5yZowcJSFJhEQdr2BsjWonyQb8dtPrcsjf3jdULxGjSoP3ujALEPhKFOspndsWCwG_Ls0MP5ngD9_oK9NrZlJQKwTntebIcNN9xvgSB99kNpcZxmKBAtoWPwpdZm6CCkHg4WGR61Q6mY6LDhAu9If4Bm_XPccVLCCKMjB_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=Ng12E1HXZCSzdED-T-CT6TbTDQxEZ8zWljXLd6xWZkJNPl-_GUk9YYiZJfQ0qumnqwXIpocMf58dkvuAxzSe3n1ZI2uuRTd3yQXcD7aP4W1URNVsRsN-lOAFbPjIqs_YqLkModRBiAILrKF8e2hKxAF4VszPOck4AK9OVFesY0ThSYd5yZowcJSFJhEQdr2BsjWonyQb8dtPrcsjf3jdULxGjSoP3ujALEPhKFOspndsWCwG_Ls0MP5ngD9_oK9NrZlJQKwTntebIcNN9xvgSB99kNpcZxmKBAtoWPwpdZm6CCkHg4WGR61Q6mY6LDhAu9If4Bm_XPccVLCCKMjB_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از جام جهانی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66591" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1YrGQrBpTbWPDjii53FqkU2IvrnLfqwk9mRCc9CMVmzgsJjbPlJw6nrp0Lu81QlURFGRIcWF1cU71G2wq04gmIew_fFcijsoSCpkQGKcP7x1TzSLZYsdNppCShJiJNK2YGRI6nGpCNUxU5yMyMMabbuwBGn6J4ztnjXnfF-A8N1kqcPt04sBacExMgMTyhtggqsIU6PfO1nAaX-gtVtA4MxdhqnenHO_43h4ppoScu--lrHStA4D4s4dc1B1MtBVeGAQ0nztrbPXZU1NZ1OZDH09hi43BQlxfmTmKodglEhIc37JPIywDyahs6Cr5YDLwEqG6_l6XYzpMhXtrGWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاونت راهبردی پزشکیان :
تجمع کنندگان بهداشت روانی جامعه را برهم زدند  تجمعات باید بعد از تشییع رهبر جمع شود.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66590" target="_blank">📅 10:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
منابع پاکستانی:
عاصم منیر فرمانده ارتش پاکستان وارد سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66589" target="_blank">📅 09:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=UD1QjhW8s-findZr5b0S87u5gchdZsFSfry1JGtu8LOiREFQ-SLOPGtR_FNz5ABOmQaaSZv9057hLU3IYSHkPZJS4ms7D2Ut-0sQqWVjsEO1GsX7Xc9h87Ez7u-S8c4m6tWaEyKO_yvJcj2MzkxfpU1kulOYXp6LL_oRCQaA-A8pruWxW7Adfza3m0HTo7TCsoZZvOIia5n91U0-Tf3pEfqBh3JXAMyBwo5lorIuAce5n7W4eEUIhVGuiq9pWh69xkflkQxz5wvNV15d-z5nJG8UXNkAzgdRBsI-ObSiqjeShOSaafgti9xD8OpqQe33I26_KlJY4hezOiD07Li7fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=UD1QjhW8s-findZr5b0S87u5gchdZsFSfry1JGtu8LOiREFQ-SLOPGtR_FNz5ABOmQaaSZv9057hLU3IYSHkPZJS4ms7D2Ut-0sQqWVjsEO1GsX7Xc9h87Ez7u-S8c4m6tWaEyKO_yvJcj2MzkxfpU1kulOYXp6LL_oRCQaA-A8pruWxW7Adfza3m0HTo7TCsoZZvOIia5n91U0-Tf3pEfqBh3JXAMyBwo5lorIuAce5n7W4eEUIhVGuiq9pWh69xkflkQxz5wvNV15d-z5nJG8UXNkAzgdRBsI-ObSiqjeShOSaafgti9xD8OpqQe33I26_KlJY4hezOiD07Li7fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صدا و سیما:
علاوه بر تنگه باید فرودگاه مهرآباد رو هم ببندیم تا مسئولین برا مذاکره نرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66588" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=IhiYT8jIVI2bJlv-HRbsNnrE7uT-Nz2aalPfEWMpgfee7KFWfdWw9C19HrDrf4WjOxIF_pACt4DZqSpZgoL202GKkpIZLYRVq6F-ZZeGMiIBuNGL14R8NCxZcxh_qEXWKkNNh01VQX6YFqgGSQhNIQa1gZyAX5VcFl8xHS7osis9kXX5_iOiD3O_ADpsnlnSR7YRE65RvN5lPYcTa7X2LBR3ZoQIQeJxAoUJw8I1CJeMmDCh95LQ_MKkePhbcpZ4FAzet92SzxjOJtfBe4KSXSzaH6nrHGB5qORbAM8iYOqc9wwglBBuK3WI6Yo25B_F1QLBQ0EYc4dyqQOzop_F-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=IhiYT8jIVI2bJlv-HRbsNnrE7uT-Nz2aalPfEWMpgfee7KFWfdWw9C19HrDrf4WjOxIF_pACt4DZqSpZgoL202GKkpIZLYRVq6F-ZZeGMiIBuNGL14R8NCxZcxh_qEXWKkNNh01VQX6YFqgGSQhNIQa1gZyAX5VcFl8xHS7osis9kXX5_iOiD3O_ADpsnlnSR7YRE65RvN5lPYcTa7X2LBR3ZoQIQeJxAoUJw8I1CJeMmDCh95LQ_MKkePhbcpZ4FAzet92SzxjOJtfBe4KSXSzaH6nrHGB5qORbAM8iYOqc9wwglBBuK3WI6Yo25B_F1QLBQ0EYc4dyqQOzop_F-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خودزنی مداح وسط هیئت:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66587" target="_blank">📅 09:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66586">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66586" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66585">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f5qQ2ttkK6AHUCnzZwJyhdnqGHPeeQWlnb-Le_o3rWZEHwGR_WrwF6PVuEYDrcp3eMRrThGVsJMMKdaa0ZzT-qx1jSszeU2vDr0ZQNvfeNjw86BOCVneIUzUiEPi5nN09dnPQ2atmsdZGrapZ0gFsmgsYFkpNd9rVnCfvpKOlBnWkGumMghdUMYANeSrfmftHKOt10LkrxjZJHJKWypyRh8DW6MvVr3e56SHOIRdr_rKJONnCjtarGA51xq76R4L5b74OiHzRqnvl0xQLL20uiFP8rzlyehpp_37EB7UB2-3YV-sDB8JxKxIek4Jb8C3HhprRsRN4i_mcVgaAkEARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66585" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66584">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcMIaCmE1YkBdTMYebR9bRraV50kM7QCZMEYWvsVPC6x9QfgJ--pIvPdlosdWA1YwBx_esbE0qSjQG25Z7LGOPol6nnZY4rgm7BrYOxRqF4fR009ThnQnpZkUjBNUnbumM-eCNYYtBMFJNkTrOgiDszqnd4Wf9MVr_MiAEEOXmh1RK7e7wbzdQYqLv83Vs6fE_1hGpNbKSGq_eCP4QHJLnMg-LHSHvO0OM2-xK-86H6DXDEzNUa1vamdPz6t3pyfCJTPuMKod5YIDiHyEtVkY6T7PMz1Aj1qwwyfrVoZNsPtPZphG_BAu1Nq9ptwzHDBIrDApzATvNTF5bMp1_R6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف بعداز ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66584" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66583">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=YCwa3Nz6iPSjONzWbx1XtJ5hrIsWqyzDljmzPfyogOA5T9hdCxy0xnw4TkGHxUMlI6ZyK_hqMuOH7UAWUlofpRXyu_Jw8TnFgAaLkSu3s7PpZC7eyNWo1fIMP4aSt9InEJKcjXOdgWsFdsKnL979oz4Wf3HatHiqDUccMJoX1xpG7_swa7_Myy-J3Lb01UXAs1Gux1BI26f3UjfmNCr6pX8VviGb-LJaQjczwo3WMgiMNSsAwDz2yPWOXBSVIDTBiMXPgye9-lTDU0bt7FueAW4Xxe7wHPnW-enzdqUDwCyR_SSogec8D2i8TAIInYOR9kGzHbH_ha-Y1e3jCNn6DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=YCwa3Nz6iPSjONzWbx1XtJ5hrIsWqyzDljmzPfyogOA5T9hdCxy0xnw4TkGHxUMlI6ZyK_hqMuOH7UAWUlofpRXyu_Jw8TnFgAaLkSu3s7PpZC7eyNWo1fIMP4aSt9InEJKcjXOdgWsFdsKnL979oz4Wf3HatHiqDUccMJoX1xpG7_swa7_Myy-J3Lb01UXAs1Gux1BI26f3UjfmNCr6pX8VviGb-LJaQjczwo3WMgiMNSsAwDz2yPWOXBSVIDTBiMXPgye9-lTDU0bt7FueAW4Xxe7wHPnW-enzdqUDwCyR_SSogec8D2i8TAIInYOR9kGzHbH_ha-Y1e3jCNn6DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی‌ونس معاون رئیس جمهور آمریکا برای شرکت در مذاکرات با ایران عازم سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66583" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwRpen1taepU3eRIegry_YgU0LFBV9pKSKrMIG6p8-Jl5e6O4-CuHGllsbE2aePmxLC03YWOmbe14jQTg3bocIrlp6FR4GtzPJ8ChYKRB-Zhvj3N0vxY-TQYVQLH2C-rtK3AKshajvFhl8TrIGf4AnNchFxy27lCMnuvZVkXAZwMW4nS2unc-hjJ7SrEfPwnnE5RqQf8jrxcP-69oCYmHXn6TZmsmptu5u10uKfW3s7Sm4yY4hVOSBiGvDaT9uK7qJXNtrW80EZPNr8cK4ApsIB3OiaUgSfq--zVC3Lv_Dbz5Y3A0z63pGrp0tByfgLCXIekxQlGOSt-Wa5r4WeT-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مرندی عضو تیم مذاکره‌کننده خطاب به ترامپ که گفته بود هیچ هزینه ای در تنگه هرمز نیست نوشته:
«هزینه ای وجود خواهد داشت این قطعی است»
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66582" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66581">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666063795.mp4?token=lBfXwGKflDGe6z9EkofdXVrtWmelURUrEnRn3OhWKekG88ZFPZ46LPPE3GoHDy5N0CxPcR27CEVdTadUOGrkiXkNIMAiD7gdR9rVXbIWJ3RemQfP6gI2tVLbCrc7HItdoXfOY35rh-5iQSUQP3bHAEn2WX4xLmfAKR2iQzjdg5Oqhhs3XRVPlZveYAnw2RGUxREydMzjmR760uRP5BJ9prWNcL5DhXY2Axq3x5h-8srRf1l4PTnuGK71nZ3Nd453ZWkww1GKGdV_N3o2vOiuGebV8L4Fd0eoGxpX9FOKSN2rPQGn2qOn98klNhHrHCEPBK11vSA6hOXZ1mazf5g_rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666063795.mp4?token=lBfXwGKflDGe6z9EkofdXVrtWmelURUrEnRn3OhWKekG88ZFPZ46LPPE3GoHDy5N0CxPcR27CEVdTadUOGrkiXkNIMAiD7gdR9rVXbIWJ3RemQfP6gI2tVLbCrc7HItdoXfOY35rh-5iQSUQP3bHAEn2WX4xLmfAKR2iQzjdg5Oqhhs3XRVPlZveYAnw2RGUxREydMzjmR760uRP5BJ9prWNcL5DhXY2Axq3x5h-8srRf1l4PTnuGK71nZ3Nd453ZWkww1GKGdV_N3o2vOiuGebV8L4Fd0eoGxpX9FOKSN2rPQGn2qOn98klNhHrHCEPBK11vSA6hOXZ1mazf5g_rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری که در شبکه‌های اجتماعی منتشر شده، برگه‌ای تبلیغاتی را نشان می‌دهد که گفته می‌شود به سپاه تروریستی پاسداران تعلق دارد و در آن برای اعزام نیروی داوطلب به لبنان و همکاری با گروه تروریستی حزب‌الله، حقوق ماهانه هزار دلاری وعده داده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66581" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66580">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=P3MZ8aokh05Yk86ZL7sQ4KiHSDVhoBANBGFSQDbBKCJ-u3NyoykWe_Bh9x5vIXJe7P1U-wtiQ8iY0woP7OpljOc8upw7pz8FVWLxYx7sWZ0OezejPFnqVjgZ3N_k7HIJwuDGG2I8Gfd_pqtyvG1pCIStgjsrMYoODVmoiyf329glRFVA_-5KRg3-BLFHaFHn91R8WHaEI8OCGWRctIZVUajPxZCHLBu_oCRzCpSL5ZTAcXVPWo3PyzvjNgXNY5mHNuZOXkwo-DfvkN-_cXArr7m0WKr_TTk0zWHqdyTg5jD0tk0F7wyZqmSisp2ousDUTkInUJr-sVP-Il4cPJdufQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=P3MZ8aokh05Yk86ZL7sQ4KiHSDVhoBANBGFSQDbBKCJ-u3NyoykWe_Bh9x5vIXJe7P1U-wtiQ8iY0woP7OpljOc8upw7pz8FVWLxYx7sWZ0OezejPFnqVjgZ3N_k7HIJwuDGG2I8Gfd_pqtyvG1pCIStgjsrMYoODVmoiyf329glRFVA_-5KRg3-BLFHaFHn91R8WHaEI8OCGWRctIZVUajPxZCHLBu_oCRzCpSL5ZTAcXVPWo3PyzvjNgXNY5mHNuZOXkwo-DfvkN-_cXArr7m0WKr_TTk0zWHqdyTg5jD0tk0F7wyZqmSisp2ousDUTkInUJr-sVP-Il4cPJdufQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=f3bbp4-JlEJSUkdbZ8tXwjiDIxQ9fXq9TkGQYssSYHtnm_Ix6haYwZO5WKUpMok-9l0qwxK8oHLDwXvtbPn8_42tD1Vac03QdHsWfFKK4e1wATS4o6zZhQLkZT1VCY6B-mF2GTHFWD9jR16iasLw0-469v2lyKE4PyT_GQZYhevxKZoaeORi5lEYciKi66aA0hwHPwHUJy0201B4zhQDQ26NStnbBSRi-gi8PnOMHBT57sJ1l4frO3N3_7CaY-iJft8h1GdGfdo6z7ajusvyFTV5LvfKTsn7hVJnLDdjznQjm61Oxwv6dmlbuuImLOZFZxrqxa8ub6_fg58OnUoRWC7QIl1rkWooMNkwU85zEGAysMXkntXLu-EPjBSzzocS3i5_HRbC2RsudLcy0WxmjCmUIovJ7FTfQ7OuHZvwCNJDFG7mWrDT4y1uXHu8pr4RyfVtmvcyM4EKLLboPxt61AVUM3w9huUaG6hBpNQWs_-NyIsZeIDEGLtzRKI_N5LI9IWGe0ZVZr9d91W5-DiqJjHXRZ5ho61xxydpU-58aHXNXuIZ5FIqzU_GkxA6d33MNkxOmuXvuOXVUptcX2L-KlRUCcyIfRMLs7N2NWZy7t-eGL13Way7SDsyf2-5X7eGSxYxztZA9jrxemE6Z8JwAlAqOLifxXY73GN0ysKRvdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=f3bbp4-JlEJSUkdbZ8tXwjiDIxQ9fXq9TkGQYssSYHtnm_Ix6haYwZO5WKUpMok-9l0qwxK8oHLDwXvtbPn8_42tD1Vac03QdHsWfFKK4e1wATS4o6zZhQLkZT1VCY6B-mF2GTHFWD9jR16iasLw0-469v2lyKE4PyT_GQZYhevxKZoaeORi5lEYciKi66aA0hwHPwHUJy0201B4zhQDQ26NStnbBSRi-gi8PnOMHBT57sJ1l4frO3N3_7CaY-iJft8h1GdGfdo6z7ajusvyFTV5LvfKTsn7hVJnLDdjznQjm61Oxwv6dmlbuuImLOZFZxrqxa8ub6_fg58OnUoRWC7QIl1rkWooMNkwU85zEGAysMXkntXLu-EPjBSzzocS3i5_HRbC2RsudLcy0WxmjCmUIovJ7FTfQ7OuHZvwCNJDFG7mWrDT4y1uXHu8pr4RyfVtmvcyM4EKLLboPxt61AVUM3w9huUaG6hBpNQWs_-NyIsZeIDEGLtzRKI_N5LI9IWGe0ZVZr9d91W5-DiqJjHXRZ5ho61xxydpU-58aHXNXuIZ5FIqzU_GkxA6d33MNkxOmuXvuOXVUptcX2L-KlRUCcyIfRMLs7N2NWZy7t-eGL13Way7SDsyf2-5X7eGSxYxztZA9jrxemE6Z8JwAlAqOLifxXY73GN0ysKRvdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره با ترامپ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66578" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66577">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=QqVu-AoB-hYdo0JMYKLtVLSFwWPhw-Ns-v4icVpxcsiATNkAP2l4fRZBtpA5ErTWsYWfijslrjp0oZKfJNXVnN7kO5C-E4Lfz12zNji-JrTctH2znd_SSkRKaEObewQp54ke6E_5-Qr7UrkjYzEfWgxR34um8buiBP2JSadMKVaoKKIDzet6-VUh4TVo-_wlLwzZRMzcJNvW50ybmE4IX15MC-qrLfkV_u-b0tBLxulIx-dPumEWm2ZlOl02_Kea5BKAQEHYHNMU-m1rXzk1QPJJzBpLbw91BWcNSrohSYRjVC3cS5amOvJhiAZ7hNEkqOiD-yXL9UcMs6VfUw9crA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=QqVu-AoB-hYdo0JMYKLtVLSFwWPhw-Ns-v4icVpxcsiATNkAP2l4fRZBtpA5ErTWsYWfijslrjp0oZKfJNXVnN7kO5C-E4Lfz12zNji-JrTctH2znd_SSkRKaEObewQp54ke6E_5-Qr7UrkjYzEfWgxR34um8buiBP2JSadMKVaoKKIDzet6-VUh4TVo-_wlLwzZRMzcJNvW50ybmE4IX15MC-qrLfkV_u-b0tBLxulIx-dPumEWm2ZlOl02_Kea5BKAQEHYHNMU-m1rXzk1QPJJzBpLbw91BWcNSrohSYRjVC3cS5amOvJhiAZ7hNEkqOiD-yXL9UcMs6VfUw9crA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرار موفق یک کامیون روسی از پهباد اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66577" target="_blank">📅 21:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66576">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
منابع پاکستانی به الجزیره:
نخست وزیر و فرمانده ارتش ریاست هیئت پاکستانی را بر عهده خواهند داشت و برای تسهیل مذاکرات تلاش خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66576" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66574">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I88UdNibwHoHUPidFEfNA04HyS6fK6jGg6ZY3IUu84A3xpoe_Q4VmBxdQEYCzzUIZwCCAP5nnGbplRx0YFDBs0hBYSWHa8NcBn3Ux1Lp56rQEIacX0AaYSeUIyxq1BO8EKBFO-_r3wq2wy6WymArZ2ubP19a_MspdbemBNGm7Z9jgwLPUlbGksH7eBOshca0cKkYT1PtwymcPyIEsBlUc4XzI4TZZpWDCKO1GIPVk6EY-NBtyqqJpWXlFkTgaBWeBHEwU3MMjnch3gozFOexJwULl3OnLqaIfGrz9Dm8pwNMUyZKkz0I-FjypSar9QIyP5aPovyPpJs9orLZlm9PjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8349099df3.mp4?token=QsL68gswvQ_beVd2TUFFm56BEygUATeKp6hw6C9XYFUjZE0uoB9nKBRtgswcvWrtLfSW85mQTkdPaowUGyAtIGpQdNve1Sw25AByCo4RfiYhHa182-fjdCCJ2ekZC-22Pb2uvgN80HlsH_qDTdTV4LnT49KtqeR4WSyNqtjDNJsNh_n_rJEym-Rh9PwON9jVPimbwdpRZ_bl87OmstgjXTI6Smfy7catRkQGIvpDqGWHOTusyoKEtvfDrkvQz5CE7kK9hnk7DgFGsYY6ia1ESRt8CI3mt08hnZ7HvQEjfpKwmCluot6gmB3UTClMgZ5Fpn7EgILr3kqWAhjOs9NnXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8349099df3.mp4?token=QsL68gswvQ_beVd2TUFFm56BEygUATeKp6hw6C9XYFUjZE0uoB9nKBRtgswcvWrtLfSW85mQTkdPaowUGyAtIGpQdNve1Sw25AByCo4RfiYhHa182-fjdCCJ2ekZC-22Pb2uvgN80HlsH_qDTdTV4LnT49KtqeR4WSyNqtjDNJsNh_n_rJEym-Rh9PwON9jVPimbwdpRZ_bl87OmstgjXTI6Smfy7catRkQGIvpDqGWHOTusyoKEtvfDrkvQz5CE7kK9hnk7DgFGsYY6ia1ESRt8CI3mt08hnZ7HvQEjfpKwmCluot6gmB3UTClMgZ5Fpn7EgILr3kqWAhjOs9NnXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
امروز در شبکه خبر در مورد چرایی مخالفت رهبری با تفاهم یادداشت ایران و آمریکا مشغول بیان دیدگاه رهبری بودم که به صورت ناقص رها شد. بخش مهم آن بررسی متن یادداشت تفاهم بود که علت مخالفت رهبری را بیشتر آشکار می کرده است. انشاالله خداوند ما را در پیروی از رهبری عزیز ثابت قدم نگهدارد.
«ویدیو هم از لحظه ای هست که آنتن از نبویان گرفته شد»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66574" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
‏به رغم اعلان اخیر سپاه پاسداران ایران مبنی بر بستن مجدد تنگه هرمز، فرماندهی مرکزی نیروهای آمریکا «سنتکام» اعلام کرد تردد کشتی های تجاری در تنگه هرمز امروز افزایش یافته و ۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت به سلامت از این مسیر عبور کردند.
مرکز اطلاعات دریایی مشترک (JMIC) نیز با صدور بیانیه ای بر تأمین امنیت کامل این آبراه بین المللی تاکید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66571" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66570">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzoQWx7a0kk1MT-eDNO732lo0UhqGUwoolbrmkggwGXOBfrpkzZz49wv4dWe1Eir4eOCGDs6unGQVnqHu-cRPXsueEuCNiOvnTn6RjqlA_6vbNuAYToXssRxMhXF9XAjsBdHbkNxoOhOCzsBDvYpJFe31OgRoRBDCKeVdOhfRsUMu6BA3YLQcplRrAEp7pXw2i6pUFsXrGJW9zaydPHNaYTooGntEDhjzbck36jK-Hbnt_tOaNWBAb11WmSNt5ow9ZEx9wq8IKArlG1mPgdETwTxuQjYH-LzeMph9irBM8lrlhqkGZy4g3MO-U6XW-oPSnOtmbVLBCPgjN9qLDmz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
جی‌دی‌ونس برای شرکت در مذاکرات فردا با ایران به سوئیس سفر خواهد کرد.
قالیباف رئیس مجلس نیز در این مذاکرات حضور دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66570" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66568">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCO5PclkQNrg9rOaBFw7vBhIE6t3Ibgr8_a7-MwsrOIIbrn7Ps1sEIE6hwVSfMHRpPZA5Km--3UKKGJ7NHpUTrsnAH6ZvgwbGlO1h5hxaVDUGO2fpP-AP5XbPzuMyso20ss1UCiQXqhAd0Xp_s6A3chWkJxUx6pKfX5PQS2Req40r41d2tclSwWG-rcIsxAnkX1NMZzFbtd26ny_p5NyBQo5R_sNzbz4-J6I3XI16Ht6-wtAdrrv-cu2D51VVxZmcv7HXksahCJ8yED8zwz88q082EZainkjzBW9vobjhEPPE4NtCuiaCtsNkwNIOuifoME8zP20HSI3WSzHaPSqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=k7cMZLzPa7tQ4dpL9D5IZ7KtLRiTradxLHza1Glbq85tXPcFcZ-lWm1QwxUL49ndiw6KnRvAHsncgldeNmxlYV5pED2HYCB8DpihlXyFZREef9Xudxsb2Xj0P0wHjakxWSyOW6hpeouQcIPfJalsoqvAqjBFNDKLOSaVJ7TvceaSfBnDDP9b2KgGB6qsd_kW-zhaf61E99rsbphCVLkA6f8nnMpygYoEEdMtVRXAUizEg3peFRvUTG7Zu7AMlTia43F6dcny4_zxotnAVDnTfLiZMp9N-t7OeE2A8Le84prqT2sgePdrNe11-WZQPnNu2RtRmPXC3Ha9DcsteoASCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=k7cMZLzPa7tQ4dpL9D5IZ7KtLRiTradxLHza1Glbq85tXPcFcZ-lWm1QwxUL49ndiw6KnRvAHsncgldeNmxlYV5pED2HYCB8DpihlXyFZREef9Xudxsb2Xj0P0wHjakxWSyOW6hpeouQcIPfJalsoqvAqjBFNDKLOSaVJ7TvceaSfBnDDP9b2KgGB6qsd_kW-zhaf61E99rsbphCVLkA6f8nnMpygYoEEdMtVRXAUizEg3peFRvUTG7Zu7AMlTia43F6dcny4_zxotnAVDnTfLiZMp9N-t7OeE2A8Le84prqT2sgePdrNe11-WZQPnNu2RtRmPXC3Ha9DcsteoASCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏پهپادهای دوربرد اوکراینی پالایشگاه نفت تیومن (آنتی‌پینسکی) روسیه در غرب سیبری را در فاصله بیش از 2000 کیلومتری از مرز هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66568" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66567">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhh2NxMWip8LxCLiAJd8r8BykkbsTdKEAMjVzc4NJQgv1lPJzJ-F6twuQZ2Jp1T_hg07R-zfsKN9DYrNZcwSSvcCDwq4L_3RnbaS1x5pwr4YT6mXeOP1NQNMN91Tqcm9usbMaaSkh2btjJQ1gnTYMBBWzxjczsL9Ok_UgwQYI-bxJG-T0xukURD2MQu3wvkq_60FSncEuuL9a8PHJTsXbfO_Iz7INSQSv-NvQXyh8iddYNNei4NtV9cLIUSATSENhm3s7pNTtP6P66TO3jwSCrVpojnV-TQhHjSOBCxcBZ6gi8Q6Be_rutvOBNZh2uAkwSS1aynOWC7C3lSi2ZSqVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛الجزیره به نقل از کانال ۱۲اسرائیل:
نتانیاهو و کاتز به ارتش اسرائیل دستور دادند بدون عقب‌نشینی از مناطق تحت کنترل خود در جنوب لبنان، آتش‌بس برقرار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66567" target="_blank">📅 18:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66566">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdFcb07OZqQFaJA50YnvumEr7CyLXuwazz6L5fz0cgTy-3T8s45SPCcLd95TP_CKASnVLTYLKVBkYbY6EbNmO8DcD-XQFigNzcTi8ZbVB6qW4evHcQruLwr74O-naakCBPJS5mE2Zb6Otf97jIuupjJmkM19b7dK6z80Km8epWw6juyVb-oa62ClJc4isfuOmMNaDJcd-awGL1TklKF6mdnssCR4fmIZqJMQaRumcuEIdqsZPBkmzuMKi0i1cRHuO77sjzfrBvu9SRzMDTM7L4VNaynYmLRPFWEDdQFJ33rP0yt0MIlARz7Zn9XXi-B5bfPRZ7I3I-9xLnvc2j9JEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی عضو تیم مذاکره کننده:
جبهه‌های نظامی و دیپلماتیک دست در دست هم کار می‌کنند. تفاهم‌نامه باید سریع و به طور کامل اجرا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66566" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66565">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMFDt2NMvrg8WCCAxDX0_a-Q4KrI7pjLxd3GjUohCCo9QQkMYUuNSbZoOfuQfaiLxz91FinEDGLKQ2DV-dvd23hdFkCMzP5gnECaSslxEuHiHNU4LEGYuRcItbU4jxGTaMfSxJagp95dKsEwplnik-CcFTq5AT_641nrvi3ivbnm2n2DeaW347lPXp1T__ycIQ19ehLjL6e6ClCyLVhbf8MXP52nsPAKR5qQQ1P9nNgTYE_cKaQv5GoTrLdLQkWTECYQcTcFN-9marewasuN6fdFprvea9HdpWxHQU14qKsz5Zr3-mszqk-_aNuiZgjhXwMEZSupsamTVaqWmjJodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ دوباره به جورجیا ملونی، نخست‌وزیر ایتالیا، حمله کرده و گفته:
نخست‌وزیر ایتالیا، جورجیا ملونی، در جریان نشست G7 در فرانسه بارها و بارها درخواست عکس با من داشت.
او در ایتالیا وضعیت خوبی ندارد و میزان محبوبیتش پایین است، احتمالا به این دلیل که در موضوع جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران، از ایالات متحده آمریکا  کشوری که واقعاً ایتالیا را دوست دارد و از آن محافظت می‌کند حمایت نکرد (البته ناتو هم همین کار را کرد!)...
حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، او می‌خواهد دوباره دوست شود تا محبوبیتش بالا برود. نه، متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66565" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66564">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه پاکستان اعلام کرد که مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66564" target="_blank">📅 17:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66563">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66563" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66562">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
اسماعیل بقایی:
هیأت مذاکره‌کننده ایران تا ساعاتی دیگر عازم سوئیس می‌شود؛ این سفر در راستای پیگیری اجرای تعهدات طرف مقابل انجام می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66562" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66561">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
❌
قرارگاه مرکزی خاتم‌الانبیا:
در واکنش به آنچه «نقض تفاهم‌نامه پایان جنگ از سوی آمریکا» و «نقض مداوم آتش‌بس از سوی اسرائیل در جنوب لبنان»  تنگه هرمز به روی تردد شناورها بسته خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66560" target="_blank">📅 17:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66559">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد بسته شدن تنگه هرمز نخستین گام در پاسخ به «عهدشکنی دشمن» است و در صورت ادامه درگیری‌ها، اقدامات بیشتری در دستور کار قرار خواهد گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66559" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66558">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛قرارگاه خاتم‌الانبیا: تنگه هرمز بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66558" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66557">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e32956668.mp4?token=sBYGeCeOywl4ZYF4klO-PI5rl49a3q01UfPqZJPorLAqz41j-_tHPBI0-USWiJEIZCVIEBDFaSu0qlsIcONH-maWSQr33oj-tR6ItkNl4b1QRjpHN3JD96FivaBJnmIDdy0WLmoHmnU5tUd7h8CE67d1ou0KlroqOAeChP3gRXVXwXcJ3iPDzy7rcAZVOI6f1Ew9Dt07wA244dQE22y9OYKWyyhRt62nUUgUPu7MTjGSw3yXfglgna_VnXm4R_gVnTgjKYNO08xUCas53sxMzLDgabMykYTgZKexJw3EvK2qmM5pwBDr6mLJLuO8BMfYQ_5d_gt7EutfgE5QiAFbVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e32956668.mp4?token=sBYGeCeOywl4ZYF4klO-PI5rl49a3q01UfPqZJPorLAqz41j-_tHPBI0-USWiJEIZCVIEBDFaSu0qlsIcONH-maWSQr33oj-tR6ItkNl4b1QRjpHN3JD96FivaBJnmIDdy0WLmoHmnU5tUd7h8CE67d1ou0KlroqOAeChP3gRXVXwXcJ3iPDzy7rcAZVOI6f1Ew9Dt07wA244dQE22y9OYKWyyhRt62nUUgUPu7MTjGSw3yXfglgna_VnXm4R_gVnTgjKYNO08xUCas53sxMzLDgabMykYTgZKexJw3EvK2qmM5pwBDr6mLJLuO8BMfYQ_5d_gt7EutfgE5QiAFbVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چه قیافه‌هاییه که ساختین
😢
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66557" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66556">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">باورم نمیشه ۵۰ سالشه
😐
🔥</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66556" target="_blank">📅 16:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66555">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=bNOrryh56UbHJI4jc0WRkN1FoKlCVezVjIVSioHAE2kIBaBZVsJiavzRgQH0zrRYtuYFgNdplKKnOjAnOy_dWlnbQ-KAywcD9Pjc-a5wXscH2JaAtZo2UcXDHfJ9wEA5UMDV1fCpoP9o0aNMXPR_94kAVKh6NKckLhqvJ3wnC0j4RFLpyPb8L21HZPeIQRJId_487vOZiYKm0WiXWx-aIr23xGiNpU19NAxO8nJM-SG4diiQFmUD2MrrsnqBH76__CVZKN4sUgxNy6rD98T5p-HHXhE5hZjWeAkBQZ_f76XM7eTriRktHlaTri6N9lguRXSPIYaH3w5E-RWxNgSqTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=bNOrryh56UbHJI4jc0WRkN1FoKlCVezVjIVSioHAE2kIBaBZVsJiavzRgQH0zrRYtuYFgNdplKKnOjAnOy_dWlnbQ-KAywcD9Pjc-a5wXscH2JaAtZo2UcXDHfJ9wEA5UMDV1fCpoP9o0aNMXPR_94kAVKh6NKckLhqvJ3wnC0j4RFLpyPb8L21HZPeIQRJId_487vOZiYKm0WiXWx-aIr23xGiNpU19NAxO8nJM-SG4diiQFmUD2MrrsnqBH76__CVZKN4sUgxNy6rD98T5p-HHXhE5hZjWeAkBQZ_f76XM7eTriRktHlaTri6N9lguRXSPIYaH3w5E-RWxNgSqTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
رهبری سه بار در موضوع هسته‌ای به تیم مذاکره کننده تذکر دادن و گفتن «در موضوع هسته‌ای یا باید به پیروزی برسیم یا اینکه برای همیشه از دستور کار مذاکرات خارج شود »
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66555" target="_blank">📅 16:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66554">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=ER6kWH6zDKC5I0UfxyuSbl2DV9UsYhGXOgyZ_9LOSSC7djTsECQgv0i0lfUFQUoLyO97x1z-QA-UHzik-JlNqyXpXUIvftPcOvnUEAlGCQ3ETiFE88cl78oApo25CydHXmFjJRgcSiMtdAeh8nMVQ7DCYbWPu7fopxitzs6zy75d9Ss9kELViqnV1dYOxvuqAFtn6iuHFvQdlU6swUw1pX3kwarD5AAOJjyFXqlvVOFDmxbnva4GAfIDAIJxbVg7EVn5tePGqdDOJ97fh69y_kryOZbG6nFprOUtyHdFsovRF_Xs1s-3PtosqxpNAEkXUQmL6d-GfdHSUI13jt6NfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=ER6kWH6zDKC5I0UfxyuSbl2DV9UsYhGXOgyZ_9LOSSC7djTsECQgv0i0lfUFQUoLyO97x1z-QA-UHzik-JlNqyXpXUIvftPcOvnUEAlGCQ3ETiFE88cl78oApo25CydHXmFjJRgcSiMtdAeh8nMVQ7DCYbWPu7fopxitzs6zy75d9Ss9kELViqnV1dYOxvuqAFtn6iuHFvQdlU6swUw1pX3kwarD5AAOJjyFXqlvVOFDmxbnva4GAfIDAIJxbVg7EVn5tePGqdDOJ97fh69y_kryOZbG6nFprOUtyHdFsovRF_Xs1s-3PtosqxpNAEkXUQmL6d-GfdHSUI13jt6NfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
فاکس نیوز:
بنا به گزارش‌ها، استیو ویتکاف و جرد کوشنر، فرستادگان کاخ سفید، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس خواهند بود، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66554" target="_blank">📅 15:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66553">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=iD75waRJ_qNi-x2NO23O64D6pvIdqFePtZrOrHE_l501WSBLgO5-wiXDQ8nLWucQSZRRYbkw-uH21cbmSHCuSRXhNsNKXMXfkKMc2-bGY-EtW69K6LL5V_BpQZLQdMDiOY1cYTK8bdNzHSJgoelItdbkafk2f7n1VK5GwHa7JbAV7JAOKvS9vJ0t65p6Ao4UmH-iL6jUo4bDGuwUr03rWZjjA2bF-Z5_HrHLEWe4htnjq7cxFd5rN70H01eCFaSswn4dTd0IHrbQAz3C793GWgEPCQ0iNBgLPvrvMWRNkEDWukjA0LXIEO6YRwu79KLuq3bTtfwxGJ9M8vLuxYEreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=iD75waRJ_qNi-x2NO23O64D6pvIdqFePtZrOrHE_l501WSBLgO5-wiXDQ8nLWucQSZRRYbkw-uH21cbmSHCuSRXhNsNKXMXfkKMc2-bGY-EtW69K6LL5V_BpQZLQdMDiOY1cYTK8bdNzHSJgoelItdbkafk2f7n1VK5GwHa7JbAV7JAOKvS9vJ0t65p6Ao4UmH-iL6jUo4bDGuwUr03rWZjjA2bF-Z5_HrHLEWe4htnjq7cxFd5rN70H01eCFaSswn4dTd0IHrbQAz3C793GWgEPCQ0iNBgLPvrvMWRNkEDWukjA0LXIEO6YRwu79KLuq3bTtfwxGJ9M8vLuxYEreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله هوایی اسراییل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66553" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66552">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmkcwN8we6V6qAxLMUiNsHRa1HGGVDI8C89dNF3__0odkeE9QkIRCWOAKZ1Ox9ccdDYRS3EgUHPTKEam3rv12ofxNtn5JcV1ojr3ymg33Z9VF50kYKueWcBBjuRQ8sXClrb1SJ7pHmQ5kl9pKlEUVadmEcMbekpuRceMMAm0pCB8lHnKcCYVWeDSPlg74LQMuiEGzh0AI3G9hNXNFeFxPtRRTpUkDbqTHDPDi9GXC2V48ivwIJBy1zgnNJNC51JeMHVmPmjZOGrvhUZvprOiga_WRxQojrITfyCaZukvQFmgpbnnRxWqqj2L-QtlMeFXqvImNowDhG0DqEQPH32o9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:
نقض مکرر آتش‌بس: حزب‌الله بیش از ۵۰ موشک به سمت سربازان ارتش اسرائیل که در جنوب لبنان فعالیت می‌کردند، شلیک کرد.
به منظور رفع تهدیدها و در پاسخ به نقض آشکار آتش‌بس توسط حزب‌الله، ارتش اسرائیل در طول شب ده‌ها پایگاه زیرساخت‌های تروریستی حزب‌الله و تروریست‌ها را در جنوب لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66552" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRubqlhMKR_xy0UIhp8_m2z3xtvGZdVHVK2_P9LY5-y1tkGu_y7Geoc-wNzYYKszRCCDXTLGZr2D2kuL-FwRidU0VSN0tV2-UXDi9LxPTeneE-95S5UEyWsT-L3W1TpWy9SNChoWW43y6sc0vnR6V6g5hlMxGRQUGie1UGBWN0pWZ3w4vbckVrrE8xaqOxh61Oikhb5EwVQ5-R7ofOD-4ijIOKAC8EzPTomwfmPt-vkf_LC0ITKdtPeN6UXLiNQuNXGgoxoe7aEfAtMGUbfZPveI-aYmHT-xf7jLinu9AQM1kBv7WXhQXA0zQVw-TDA3yso_ecenQI0xyCRvA11mwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چپ‌های رادیکال احمق و دموکرات‌ها بالاخره فهمیدند که ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد. اوباما فقط به آنها میلیاردها دلار نقدی می‌داد و هرگز از ارتش خسته‌مان در آن زمان برای انجام کاری که باید برای مهار بزرگ‌ترین حامی تروریسم در جهان — ایران — انجام می‌شد، استفاده نکرد.
آنها هیچ احترامی برای آن قائل نبودند. آنها او را، مانند جو خواب‌آلود بایدن، رهبر ضعیف و ناکارآمد می‌دانستند — و در این مورد ۱۰۰٪ حق داشتند.
ایران به مدت ۴۷ سال بدون مجازات باقی مانده بود تا اینکه من آمدم. و سپس همه چیز تغییر کرد. آمریکا بازگشت!!! رئیس‌جمهور دونالد جی ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66549" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
