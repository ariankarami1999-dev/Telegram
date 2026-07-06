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
<img src="https://cdn4.telesco.pe/file/Mc9KBt3uUFjBj7OblSlHJSBVtcsquzDO8NIehmIP4XNSfYSW74sB4OQQ9vFFm7d39C1oaeixtLiUBpH7mxBNk704wbzbZNje2ajnO_xekYLdCA2G2qwcb2pgw8gQ9NNkeD1tQwE-9CZLnHzu18qeogCzc8C9TyFbMrbxsBBR83RtrJtDxDCxZwtgPkTVJR-PUB05B3Yh26FlwqVMMMqfOuzESJ_cfmJVqQDJbxZ4gtYbpkOjPCI-Zpz2PJvigT9mXPLO8VtJm_Dv6xy2oWP7e36OJ_Mg1UN5WFE0PX0TosUYLqRQLeiHJ_d5H1MM_RAVpsysoM1wvh0g7phFiegx7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 203K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 03:28:57</div>
<hr>

<div class="tg-post" id="msg-67363">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/news_hut/67363" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kb60kppNtGUbRxgL1M0jKjiAdO22VNs5mlwzt8WUtf3pAZLVoOWy7G92d64OKOg-cFL_RtjQBV0QRP9uQjSGH3wTuzzoU9XABDOc1RIBp18kU9p1tBAV37TVgnIgG5n3oSC2z5E1cw_ugP1PR4d_qf7Movvx2vmNXWkv9INkZA15yb51ObV6w8UZAiVRTBr-viY5ymilp9dIS135sTTP8kI7FAe3c1KvTgp5C0TbdIvp7-oeIdmIA_ugtl7mUujIF7R1NZsIPYNS76Zz1qvmfldQcBnlZXppwJxKySyOAQEBmkXKNbX70etdE6y5KtdSVWLAPxOpWq8rq8mQqkQn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=WxFit6KpQSLJQaiTdnpj3tWxZOIHlpc29-8ALtwJNHayqytyztfrcU9sW2W99q98AEUX-oaL4yWd3l6Rb65e59tQKMd8NmxwAJ_faW-QX3mZskNWmE_DgmQcL1_JNLNsscmBq9i5m5-a1is2Q_ursuKm-yO9bRz0m56MzOLFRRv5oDPMxSHvIijQ1nab5rIBtXedWVZynvpNj3OChxXatr6rphRMbR-xOa-UBIvCzPek_lsN8ZlMWD9RfOpxpXLKl8JoxvqAZByFd3S-hogPaKe7_puy4ujn00xwD7dV0KPvzdZmHzOCBJrpdosogE3cCZaEn8SdHLv4Grvtetz2Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=WxFit6KpQSLJQaiTdnpj3tWxZOIHlpc29-8ALtwJNHayqytyztfrcU9sW2W99q98AEUX-oaL4yWd3l6Rb65e59tQKMd8NmxwAJ_faW-QX3mZskNWmE_DgmQcL1_JNLNsscmBq9i5m5-a1is2Q_ursuKm-yO9bRz0m56MzOLFRRv5oDPMxSHvIijQ1nab5rIBtXedWVZynvpNj3OChxXatr6rphRMbR-xOa-UBIvCzPek_lsN8ZlMWD9RfOpxpXLKl8JoxvqAZByFd3S-hogPaKe7_puy4ujn00xwD7dV0KPvzdZmHzOCBJrpdosogE3cCZaEn8SdHLv4Grvtetz2Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ارتش دفاعی اسرائیل:
پس از فعالیت در نزدیکی نیروها: ارتش اسرائیل یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را در منطقه العقیده هدف حمله قرار داد
امروز (یکشنبه)، نیروهای تیپ کماندو یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را که با موتورسیکلت در منطقه العقیده، در نزدیکی منطقه امنیتی محل فعالیت نیروهای ارتش اسرائیل، در حال فعالیت بود شناسایی کردند.
فعالیت این تروریست‌ها تهدیدی برای نیروهای ما محسوب می‌شد.
پس از شناسایی، ارتش اسرائیل در یک حمله دقیق، این تروریست‌ها را با هدف رفع تهدید هدف قرار داد.
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود ادامه خواهد داد و به سازمان تروریستی حزب‌الله اجازه نخواهد داد به شهروندان اسرائیل و نیروهای ارتش اسرائیل آسیب برساند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaPT6RWhqkjXN-jyalnLJmnY73C10zKmf_aUKn0nCBhGp_M8m0GyscTMAzmfOe2ER8cw7QU5yrriXAN2Oi13jnnllXjTkrGkwf2ceUXWHCYTEtlwQ_OzoMERXimQA_5nx8xyUFQd1dakNrpE8pnibOgMtpsYfYynwmLoV4rdZ-Wdeq06MZD5qDlFkFnt4RPV-LOXVUaSh35a478xG1PnE1hGEEIUx48VVbt68LTUNOdar4QtnlCBuN6e2SoXm3uhCPMrUYB-83wG4HC7FnuI1FAeOGwA_o2c3eKsyfiWa0nTayBnSooBChqjkX0BRPnGYOecb2EyNz1RYb5DDbhCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=jWJ6SorMn5Zr-SwtbwPjVbeY6MCOlB95OLobrHAb-5YH4ZW8z5ekY3k5vPzJEBt37wbmcPoPgmTG2c-CzE24705AeS75jyInVyrEmCa_w1uHxuqZ3oqE6WS3x_3_ok0yqTCbcsHLBVMKHZ6GB5QVtQrTtzRWPuhh6q82VBmDpl2rQWSYRzEqStcj646jAFjHGGVJ7H2VbIIkhKNEJN8a0VTnsRZI-3uccJuuMR2Qg6y4_kuukABofHwzk1A1diOJiCUi9N3m5vQbJZVw3soUPa1FEaHDMSgkcj4wo0jGmBiFS_iaBYLQu-XPCJnDrYBU9g3N_KEz24PyQKLQdBq2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=jWJ6SorMn5Zr-SwtbwPjVbeY6MCOlB95OLobrHAb-5YH4ZW8z5ekY3k5vPzJEBt37wbmcPoPgmTG2c-CzE24705AeS75jyInVyrEmCa_w1uHxuqZ3oqE6WS3x_3_ok0yqTCbcsHLBVMKHZ6GB5QVtQrTtzRWPuhh6q82VBmDpl2rQWSYRzEqStcj646jAFjHGGVJ7H2VbIIkhKNEJN8a0VTnsRZI-3uccJuuMR2Qg6y4_kuukABofHwzk1A1diOJiCUi9N3m5vQbJZVw3soUPa1FEaHDMSgkcj4wo0jGmBiFS_iaBYLQu-XPCJnDrYBU9g3N_KEz24PyQKLQdBq2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=AlsN1BKTid6YKlGhg_i7FbS9ltXuECCvw9grH_o5rIKpR92RfRG_n3MjCBZxQeuf3ivOJcUe93e_wXcp4dFPrEPtesE6582qMmBh1imaD7eNyqIL1fXWAzUETVJJvIDGNu6JBMRaXP0hpmkwGgT30u-hH-GfsVfYy2VSkCWQp1PdPKaIZl3FfxIPpgfH8Xxu0zrQSsP3u3x7Zpo_wOc5X-UT1l_FyXq55otUMEAgrg653hvoMrcZD6L8KuGS_Gig-SBWvGsRJjo_5epeQW-VvoQQHmPGBJXuwYW2326Z1gww8ROt5NLOjfkXMVMtvbASx4KgC3ZhG9l8p3mQ5bdUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=AlsN1BKTid6YKlGhg_i7FbS9ltXuECCvw9grH_o5rIKpR92RfRG_n3MjCBZxQeuf3ivOJcUe93e_wXcp4dFPrEPtesE6582qMmBh1imaD7eNyqIL1fXWAzUETVJJvIDGNu6JBMRaXP0hpmkwGgT30u-hH-GfsVfYy2VSkCWQp1PdPKaIZl3FfxIPpgfH8Xxu0zrQSsP3u3x7Zpo_wOc5X-UT1l_FyXq55otUMEAgrg653hvoMrcZD6L8KuGS_Gig-SBWvGsRJjo_5epeQW-VvoQQHmPGBJXuwYW2326Z1gww8ROt5NLOjfkXMVMtvbASx4KgC3ZhG9l8p3mQ5bdUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhJBO20txXNK-eJMxl80OtCM6OkOkmy1I5mIrlYyCNMLXudaDRCgz6kruFnNLrWuypjbI8HOSlwOMeQ3333R86WLA9sXAnxmxG0h5ZHymNV6iiP59HkHPv8b7S09CWB1qKZ6P8ysTOhezXL4PAml1QXgr639F4Rjiq71cJYkmCSakrtSSbRs8N_Dlem9S0_4UrRY5tZdxhOHxt1QJOpe--UBEraHOCLW4y93CUL-g2GxgCoQ6AjUoYood3H0qBbIJBcwdTyEKZRrWqTjiDUm52ou83HnGk6shSZkygK2p34opp8IgVVyiK6yXvtuhNchO0bU6XUDC_pwbZVU_z9q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=Js9yI2rJH0o_b3MXy2BsbAIiVtZHlr9fbRCoZpItnBG_l8d4xwKDO4dZ6jrs3cU5vWiZBYeheIr9zzyNcxNVg7oHDP13fGwifHJOh1ysLxAIMzFYd8hG8Cg1TPaEIvh3yL1ofpH7WDGFtnPoBXMnXqMZqcePW5Mt1BpScR6j-Y_LMrbG9PBhHy0za5ni_BPe2hsCZqriBEzLIrx6yIyYKBwhwA3wonrEb0g0OE4OSGeW7KZzNwHwPrQ66W-Z6wfgIwWVKhqhqAeEzU4QPu9PEKmFMwxql2J_rgeFjs3Zyd0Z0ImzP0EkVTHd8Mbel_jIxsVHeGgpGvffdioXWAtO5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=Js9yI2rJH0o_b3MXy2BsbAIiVtZHlr9fbRCoZpItnBG_l8d4xwKDO4dZ6jrs3cU5vWiZBYeheIr9zzyNcxNVg7oHDP13fGwifHJOh1ysLxAIMzFYd8hG8Cg1TPaEIvh3yL1ofpH7WDGFtnPoBXMnXqMZqcePW5Mt1BpScR6j-Y_LMrbG9PBhHy0za5ni_BPe2hsCZqriBEzLIrx6yIyYKBwhwA3wonrEb0g0OE4OSGeW7KZzNwHwPrQ66W-Z6wfgIwWVKhqhqAeEzU4QPu9PEKmFMwxql2J_rgeFjs3Zyd0Z0ImzP0EkVTHd8Mbel_jIxsVHeGgpGvffdioXWAtO5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkU0dNc-yWf0fHB26KWF1oDP8sJMsSKcnmZ0BTxutwW_Ou9g-auz1-J0oa-eHrP23ndQ6J6fxZEAqc-a7nRQjloWknmQEw9Ls4VeObLOmDpA_TJCWtXjSyegZ8cqTG_IcE73ifnaovtFj-QgVD-lV-_ZWxqBQmCf__g2RX8tdxkBPIqz4Yq-OdivF8QEym6R3HFRXHCcqgkH-y7SqKwPQkyYq8j-crRAYGUEgPO4nC2xmO0W4oN4_nPs7I8jc_GHZRTHQDoyQOmd4_pf7BQnIn25oSN3Waf1wuVGy-xfoYTkrKW0PX_za1xKQaVu58qAc0jktLjf4sExkrK8_K3HwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=tuArcdsdB7t7gTc-O2AD9A9lzfZjwvlqZr_zwHmsb1xLw71nBwdn4gNHQnNayHXfORlk8C9eKzAEJ8bcuGOhlEiKDoRaHltAJLYqFvfe1JMZRkJg9jhmgOUeBAkZfuSB_ejNQ9b7ZQtBAOWfzvcwTtpTmO0XGIrSJeKIHZtMlrFhjgi1JuuSbvjQ_Wei95AswwXvlkng63qZCgzqsqoOsIOlzS_FlYPRjBJD4JLZRQf9nTzsMzP9qSovJkKJW9XVV8U68kEyBBHlBHRSpz_cwthyYvGb2NwvNTR55uPMl9W86UwZgO-JI6dChdYJzds4bh8DiG0WEVS2XCZdZgWZJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=tuArcdsdB7t7gTc-O2AD9A9lzfZjwvlqZr_zwHmsb1xLw71nBwdn4gNHQnNayHXfORlk8C9eKzAEJ8bcuGOhlEiKDoRaHltAJLYqFvfe1JMZRkJg9jhmgOUeBAkZfuSB_ejNQ9b7ZQtBAOWfzvcwTtpTmO0XGIrSJeKIHZtMlrFhjgi1JuuSbvjQ_Wei95AswwXvlkng63qZCgzqsqoOsIOlzS_FlYPRjBJD4JLZRQf9nTzsMzP9qSovJkKJW9XVV8U68kEyBBHlBHRSpz_cwthyYvGb2NwvNTR55uPMl9W86UwZgO-JI6dChdYJzds4bh8DiG0WEVS2XCZdZgWZJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obf9JaJGHQ4m9bN2JAeDjK1Eo9P_86JBQn7MlAcYpcRYtdoBwNovuKRIX4dk3GYI72fIlglaMxSaqYIgNo0AjzT2Qnkzcm9Hc6AOzfFefITtKTpN6pOMQ9aXep4b5_Y8QvLV6ADQJG5ZylgKaYfnixn8y5BZJiB13TwXBCxCDIsLot2SqPerV24118IlHnpWFkHqzQzjbtZ3Lq6EfSe_ACUoUpP665FiLDI4yRUCwBYJqIZ_RPDQ2Z68NZw_WxNxdPiySYwSpEThgX7siPR4W4sS8IkF0Y_LvPYvIAjEtxCsO9coXl6oxy0pgDETcIU92oODTj9cq0UaTAIZmkrgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Ooh3yFt3X3f_7PcEZTRxbzNHfUILqxAJsAYpDG3QabT37qhKupFb8tYCqF5qMP9IcLtsayHbOfHDzZ9OYM92vVDSTXClv8-VpGBD2-RSdN3FoJ8j4i-UDrygmRD_qRHbYO7PSerNftSbsL0U3nz6oKz4VedfHahcEOCgZHuSsjbC7qGVyg86kFGwuiEklaVlu5t5ihr-PC3HppXqjNr-GVjVNeA5Thu6t1gmbYqrFTcdKgJAcx7awopHVOtzldgwb6iwi80a9Xt4ytE2ElbIA37k3MThIKsKWjGGE6BD25YJzMINpZ942CIrqtXB3vWQVJFM6h6nHxDTpFYT8eGOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Ooh3yFt3X3f_7PcEZTRxbzNHfUILqxAJsAYpDG3QabT37qhKupFb8tYCqF5qMP9IcLtsayHbOfHDzZ9OYM92vVDSTXClv8-VpGBD2-RSdN3FoJ8j4i-UDrygmRD_qRHbYO7PSerNftSbsL0U3nz6oKz4VedfHahcEOCgZHuSsjbC7qGVyg86kFGwuiEklaVlu5t5ihr-PC3HppXqjNr-GVjVNeA5Thu6t1gmbYqrFTcdKgJAcx7awopHVOtzldgwb6iwi80a9Xt4ytE2ElbIA37k3MThIKsKWjGGE6BD25YJzMINpZ942CIrqtXB3vWQVJFM6h6nHxDTpFYT8eGOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=e9QNADRIU7DvGH08h80HsGcb85GAmeoEz9Z7feq08wY6qyvgCKQCOV0j3I0PaiXfQJ4pcMGed0cXicLo0mmG_-Vo3MAgvhBS_FPaOGx0wsnovHINPTcoq20ZB1-Rnpr3BaLZNEsqQ197aZGVkTgDzo9VYs9W_R4-XqYxGzVDCtIbWKQA4kN2pq4Q2IXPaJivXaSIElUW-iYupXWc6uj41GEK3Koli20jz-6pLH3AEa4oc0ceDyDg3FmLrXpGqywDjcvhus6lQIc5uvkqGLYRGU97WzW-W72o_Ho931cVyxQuSOHXdLfrYyux0b2SqPME_e_skR4OMj6I9kimLBCuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=e9QNADRIU7DvGH08h80HsGcb85GAmeoEz9Z7feq08wY6qyvgCKQCOV0j3I0PaiXfQJ4pcMGed0cXicLo0mmG_-Vo3MAgvhBS_FPaOGx0wsnovHINPTcoq20ZB1-Rnpr3BaLZNEsqQ197aZGVkTgDzo9VYs9W_R4-XqYxGzVDCtIbWKQA4kN2pq4Q2IXPaJivXaSIElUW-iYupXWc6uj41GEK3Koli20jz-6pLH3AEa4oc0ceDyDg3FmLrXpGqywDjcvhus6lQIc5uvkqGLYRGU97WzW-W72o_Ho931cVyxQuSOHXdLfrYyux0b2SqPME_e_skR4OMj6I9kimLBCuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ET0K2pTvdh2_72WDOvTMmVIQGr4NKss1hbEDBygUEnd7fwWOcbY16NE3-B-uLbvnp5UMno9nDK7zbckoaZSVRaAj3kb5KXAbwcqh3enbf26VhBqw1VUHjKoebq5sf0QT37Gp5O23e1fWcVBrY6aR74SHwPtoqx0xVCfay94FGNClqRjgor0lRACom3N-y44mDn0y8CqBNk_MZqD4ptRgUfSVXhyEUtx06q3BtlyWS-OnjHzizG-zHqdr5DgImhQ8AyxjkIVTRZJV10j1zv32-Z8ZQWzZB5oWeoDdiXYZ5l8ypMsu2zVUZkAJHv1LnI6rI6AJT7-xKe8IC7XLl2wu1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5djCapQrqonqHvkxK29FL85i-gIXhM_oate_qaOnlakFBsyYkE4Pr011yKxUdxGV3wKv7YUlue-3AN_Jq_tPdr9Mh1IWf810dCl8fmOSYBJxuFCtuxBt7_yvoO3dF_hK-Rhj5komyD-MrpXeFBRi4qkT5pW2pD_nDTDIBC6CNd3CntziyOZDBQ9mazCQ2rYefdWL2xlrX-KU-1jBVOZicvqlfus_dkGeKqVNfBhAulA7ejOqM3A8_kGTuM3btglAGKu97QfNDDN6BS0E_ch0pWHJVAMedBkEPGGOI-FJU1zHDw9bAXbfxLfDqZ5okanLb5eTxNpPX0Jj5atrkAPmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=T_rJ3vF-o89IUehsLlyxRQzuMsyASEeG_kTW6g1La28N8B141AI4lSLQ-xtL4EjpQSzxcukHu-MuXe4qkLFdF-p3-dJ_MhMJlHRLo_Pzz494M-r52vzJ0Dps7rrwZK21A51HpV5nAKTsUhg5KVONyHVMXjiwjNJxyxUmyvt5PZk93G7b1yU69Hrf5Ss-QYl5bdcSuIxHpu0J93ixEjwNBupbZPwPw6Yh7gdlYC4hTWvhY3iNnq7Fu5wmPW4Hx9Hxb0WZy6xSDwsieI_c4MW0jAr5K38D58vdygj5X44WqYH8E9Pb_VKNmYm3zHIKiz5eQ5SypKvRFfuf5zqlAue_fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=T_rJ3vF-o89IUehsLlyxRQzuMsyASEeG_kTW6g1La28N8B141AI4lSLQ-xtL4EjpQSzxcukHu-MuXe4qkLFdF-p3-dJ_MhMJlHRLo_Pzz494M-r52vzJ0Dps7rrwZK21A51HpV5nAKTsUhg5KVONyHVMXjiwjNJxyxUmyvt5PZk93G7b1yU69Hrf5Ss-QYl5bdcSuIxHpu0J93ixEjwNBupbZPwPw6Yh7gdlYC4hTWvhY3iNnq7Fu5wmPW4Hx9Hxb0WZy6xSDwsieI_c4MW0jAr5K38D58vdygj5X44WqYH8E9Pb_VKNmYm3zHIKiz5eQ5SypKvRFfuf5zqlAue_fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=ZvZzqP_qndQYQZ6p6zftKV7rRx-0FdVSvVygTCFkuGZcc38Z0i9LM6mdJiRjbbw5t3oVFtuwDZMscXSXJCpCKF1XVFgrnc4JMctWg5poQZ-pGTYv0GikZ8a0LXWJ8MRsaWtYMt3dQ_evG1y-wzCA33s9f1cTrUkAuQYtG9P05GaDa6J_h1416RKFrZw-K2f6twMEtspRf3b2N2RIcryHoekcMg2bl_WuXlI9MdnICDGC0mJm_9tu_0Vp-kXQKZ69BxUIIef2IznhwiUHjZzVacpwi_1KX6dy7G1bvsvypENAyQHhMyfvtCoWli_o28mdmwO4CHsxzg5HX2ljlVJoyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=ZvZzqP_qndQYQZ6p6zftKV7rRx-0FdVSvVygTCFkuGZcc38Z0i9LM6mdJiRjbbw5t3oVFtuwDZMscXSXJCpCKF1XVFgrnc4JMctWg5poQZ-pGTYv0GikZ8a0LXWJ8MRsaWtYMt3dQ_evG1y-wzCA33s9f1cTrUkAuQYtG9P05GaDa6J_h1416RKFrZw-K2f6twMEtspRf3b2N2RIcryHoekcMg2bl_WuXlI9MdnICDGC0mJm_9tu_0Vp-kXQKZ69BxUIIef2IznhwiUHjZzVacpwi_1KX6dy7G1bvsvypENAyQHhMyfvtCoWli_o28mdmwO4CHsxzg5HX2ljlVJoyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما در وضعیت دائمی جنگ نیستیم.
من خودم، به همراه رئیس‌جمهور ترامپ، چهار توافق صلح را به پیش بردیم.
تنها مسیحیان لبنان نیستند که از ما درخواست حفاظت می‌کنند.
دروزی‌ها هستند، مسلمانان هستند، مسلمانان سنی هستند و حتی تعدادی از مسلمانان شیعه نیز همین‌طور.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=ftuHmp5nW1_Bt2d4Dap_15e0sS0SlUM6cUuCry3STtbOvFCcFVLg8sB7K5LCy21XPi2jox4BpkbrSGaYIHOxqylUVn9CAgisELy9TDTeuZ-ejcooj8xbM0aFT6EwN_xzgFzgtgTNGMi1g7qlTJsirHqZgSCw3bdWF9byWVg8o0lLkNuuHCmYbcilBx1vO5QmyXr6ycp8Q5ZsugRaiShUdS7eY8bEuPqWk1XwaDi3yHc-9apcxlQmY7oq4FaBFnm5DVqkvqIce75w2-5BpLw5erj8ulwaiklXoI6kR_qORAWflm-O26WNhbQuDUT0OOTm4pz4RWjj54j0NXBhks4Rdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=ftuHmp5nW1_Bt2d4Dap_15e0sS0SlUM6cUuCry3STtbOvFCcFVLg8sB7K5LCy21XPi2jox4BpkbrSGaYIHOxqylUVn9CAgisELy9TDTeuZ-ejcooj8xbM0aFT6EwN_xzgFzgtgTNGMi1g7qlTJsirHqZgSCw3bdWF9byWVg8o0lLkNuuHCmYbcilBx1vO5QmyXr6ycp8Q5ZsugRaiShUdS7eY8bEuPqWk1XwaDi3yHc-9apcxlQmY7oq4FaBFnm5DVqkvqIce75w2-5BpLw5erj8ulwaiklXoI6kR_qORAWflm-O26WNhbQuDUT0OOTm4pz4RWjj54j0NXBhks4Rdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=pDs6a4dY4DEyir4Io_mPH2c_yGuHZfAC7xcNym4HOs9ToJwTI-kV8z-o6ApCj-eOtcUmHqHzOeGtXfAdfCE97AheIEa9j8mAhecAo6AcQiEgpRwCPyUmUj7BftrPf4-YCxasM_g0iweZVYe_BYiE-IYjhHp_q_WWq9xwniNfX0lfi5CsiVxsT3ukM69etjUXDCybO1564KhGR6xaNeGlzLQNKsDdhpfYSjR1LdTZXk4mODe2o3HNiy86LY1k6-JS6fFrDmh7b81v1_0KR2wUqeylOjzLfkJQdlgDS2dGmGl5_eCvjNKNUtZUB5Wj_Hdst5FmVHULgOH4zNxWzRjPFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=pDs6a4dY4DEyir4Io_mPH2c_yGuHZfAC7xcNym4HOs9ToJwTI-kV8z-o6ApCj-eOtcUmHqHzOeGtXfAdfCE97AheIEa9j8mAhecAo6AcQiEgpRwCPyUmUj7BftrPf4-YCxasM_g0iweZVYe_BYiE-IYjhHp_q_WWq9xwniNfX0lfi5CsiVxsT3ukM69etjUXDCybO1564KhGR6xaNeGlzLQNKsDdhpfYSjR1LdTZXk4mODe2o3HNiy86LY1k6-JS6fFrDmh7b81v1_0KR2wUqeylOjzLfkJQdlgDS2dGmGl5_eCvjNKNUtZUB5Wj_Hdst5FmVHULgOH4zNxWzRjPFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=vAfiQEeIBlH_OnUDVy7DMjeA83Dg8ipxo07cuHp7Ja2e0_DFv0cIMiNBTdTDeFHAjqq8VFgbmW68CNl1KXuQiXUj7b49SJUSmUTzpCgwBK-KSYAKx2GHKGLM-vsmiguFDz3TJt213br9eCwriwcwgUFMthBzyHJQDe95qEsIOFNhpXF7K8zTSkmmUcReWxA2vxx5N5lPx_s66JZqNzv6pLACWH1DLlJR4Iz3R0fCsrnNtw9-N6Sv-mpcPdeKYMriyKm7oev3ThGnoOJAoMAIToobUznCyhsQ_iDtWOFx7kXf0keK7FFYWdZHHY1be3tNE_G5Ixxz57JhSn69ePfZiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=vAfiQEeIBlH_OnUDVy7DMjeA83Dg8ipxo07cuHp7Ja2e0_DFv0cIMiNBTdTDeFHAjqq8VFgbmW68CNl1KXuQiXUj7b49SJUSmUTzpCgwBK-KSYAKx2GHKGLM-vsmiguFDz3TJt213br9eCwriwcwgUFMthBzyHJQDe95qEsIOFNhpXF7K8zTSkmmUcReWxA2vxx5N5lPx_s66JZqNzv6pLACWH1DLlJR4Iz3R0fCsrnNtw9-N6Sv-mpcPdeKYMriyKm7oev3ThGnoOJAoMAIToobUznCyhsQ_iDtWOFx7kXf0keK7FFYWdZHHY1be3tNE_G5Ixxz57JhSn69ePfZiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWfMuvNit0HsvO3Pxtlz12OvOMhduVo_V-I0vSVKlcTTMKxcjE04ifcggWR8TPpbnHnUCb2o3vtoPMQAuO90ppvBd-N78OKINmhGriabBW6YWkrJ3MSaY5qyVV4eMBohz_aj5lupTZd4CeNyvkOPKVyqC1f09R19eUIwEq1Rg1mm0ZHxBTKeu536PtvKgsI9fxt1N_GDvt6Hm7iOzt97rl0hDfrgiLrHOjK95KZ29GzP-vQNzgJgvaWih2WYAOSlrcIQyxD2t2SPykyJhFQp5mlXxLtyMQAY7MLDMIb1FfsZjj5wE7jCwemf05xlpfKjR0AHU6YbU0Z_3FEXDoitmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=XdIzk5SV8_HLdXs_eXSFNvnkYzFclTUcr3ZzKJ9GtkmJplea-yP8nFsSKbrh3b7Ds8wy1qPS-FRyE7HFte9JcIcBRpMU9B3cx-AsFCu8kPKoIVxZZ55I6dm4ARud0gqneYarMXn20fyFjmuZzthd8k69eU0mjkzJ3m0ZFSjKZ-iKk-bOtBpX1uGKfrbykTbgQ_cfrJaFqKuZEanS2Uv9xbFUUKYYAMJd76EU1eNvJmQGL1B7tV-vBGuW6XJXp4TWAoQgEr6vxvEilaNmk4BL4GVuViMJRG2GsIpiTwgChuyllCiYXa8OevJPvOU6AjXBDj5SFtZlBaWHG_zuYLJHCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=XdIzk5SV8_HLdXs_eXSFNvnkYzFclTUcr3ZzKJ9GtkmJplea-yP8nFsSKbrh3b7Ds8wy1qPS-FRyE7HFte9JcIcBRpMU9B3cx-AsFCu8kPKoIVxZZ55I6dm4ARud0gqneYarMXn20fyFjmuZzthd8k69eU0mjkzJ3m0ZFSjKZ-iKk-bOtBpX1uGKfrbykTbgQ_cfrJaFqKuZEanS2Uv9xbFUUKYYAMJd76EU1eNvJmQGL1B7tV-vBGuW6XJXp4TWAoQgEr6vxvEilaNmk4BL4GVuViMJRG2GsIpiTwgChuyllCiYXa8OevJPvOU6AjXBDj5SFtZlBaWHG_zuYLJHCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm-J8mdXqDkBr_GYo_c2Dx4iJTRUUb5_JNg3BRFsh5-XoE5FFhzQ78pZ5OFEwayM-fx0qbqo0VSWFp0hQpEFhkrbx-KfjAeHdNjLAvqqt6_U-5qXAEh5FvYOSLJlh9NyncoUscHZZvN-5wBx_-8oW3LDWAspJMQQjc8I9xXgKdbh68vJa36n-k_RMVg99DBYyn9Q_QBDK4gA5Vq4XBqJ5T6A8LK989zJtdl8ZxkCtqIveLdquG--URu5HD3BpesH6_SM4P6x3XkfdH1WEyb0nKSDgj4IcpodW9RYWK93lLuj-t2iHa6BZpQhAWkweoq5LD7C5tvZqRXP-TFCo_Rnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=RZt5QIytLvpuG6rnPW9RDU69EnrDsQqVNlZH1j5iWYElfWhCzJ3JNzNwKBD5D5jvPLViL0Mw5BSI5dopAL3zifFnguIy2uuQZlHZ-iYHKz2jQSSilgxTcZe9MpT_l4-WbWT1z6FzNX-bXWdhXe66IOYiY1r9zUAn9GEncAFDu5p6LjTCfQHUwNVfHokTwhBkLdGx_I7Yt2SSM66QWtpebHfYOINi2jNB7zmnAAJ0ocVtuQho2Y7HPx6hIlw4AbRj2VIFBBGjqDA7ABtOxYjZDj1i8OPiTlEQ1Xu1FpQWQAdJkhO3kq1kaejiuVChqaJ-rTsx8LkHhl-CZ3QYliPBfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=RZt5QIytLvpuG6rnPW9RDU69EnrDsQqVNlZH1j5iWYElfWhCzJ3JNzNwKBD5D5jvPLViL0Mw5BSI5dopAL3zifFnguIy2uuQZlHZ-iYHKz2jQSSilgxTcZe9MpT_l4-WbWT1z6FzNX-bXWdhXe66IOYiY1r9zUAn9GEncAFDu5p6LjTCfQHUwNVfHokTwhBkLdGx_I7Yt2SSM66QWtpebHfYOINi2jNB7zmnAAJ0ocVtuQho2Y7HPx6hIlw4AbRj2VIFBBGjqDA7ABtOxYjZDj1i8OPiTlEQ1Xu1FpQWQAdJkhO3kq1kaejiuVChqaJ-rTsx8LkHhl-CZ3QYliPBfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imlaBmP8K5B94CcNALz1qLnopgVMnNhhP7CefwNXd94_raM1gkJcnzf6LgvOF748VqwOlXi5y8Jw763_f6lYIdzviBzrZvm5554MuY7HgC87d_x9hi-BMyq_k7SMaqrPdZ-dTLs_mAEnl1sqdc50tn2OBfvsfJCtEwRW_nlKrugNpLlaWjpoLpOZZvqpE8VFx77zgXx5FN2IJSJRJw_RfwyCgJ170w-gF8mTYLA3FF02GWvwNunJuTQ9-nB9IgrnUw5jg4QnmMJJA8mepfg-SAZD2dcKIXcQPFfrMULSdAsSMZYhf7yMoVl1xpSdKwKyFkM0cANdEIyQbPinoVq24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9uzHggrWGm_JNxIag7AlIbRbibq3aXDeM6qxRDetqEh-sWWBrs3BoHJ1dfNqm6m17hT2dcnJhioBhFynkb8HIlv16Go4lPwzzW_eL1k7K8A8tghqkm9Ubw3ZzcLfVOBzsKTKp9my_zC7h0xp-QH_1TG2Sn9d89yehlCiVL7D0fTg2jCmjU0TJm9fbrsFdtckdDh2KlMt7Xph-VmSNG6v6gEsS3r2Da-MyVlDnbqSlWM5TGxUrSxl88tG1rvL6qmiE3Os_I8JsyVOqOfkcd4bp_te9neJb4pKIIPJEraFBKefm2KcMmUmn9yj0g0_NGuEbzBy0XDFQPvKA3FAUvDgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkIvGibpMQ9l_aeINA5PYRkMJZW_lz4if56v4uaWP_7xPx5-YNDH2C0Sz0FnrXGOdvPdlk-BoCxI-RTbAt71QanvkauSSDcfHaVe1-HyeHAHdT0_hPdmr2QHxI0OoZe3JKS14Fceg2xPhR7W_nKdB-gL1pSHTr7gaBd20irATSeowlZjRbUOJlJcY5fHcQTuv3Z52iob1Ml3FMd9Fl9Vf290sO_zy0TvKOUv6Vrbjv9iEaDQUUKM3gHje9qf9Rb_1r89SLZwBw-EZ7QM1ILLxCvoVP6Cep7-0DO7yG8FoRrtNNpkbgyK8ZQ6BO_e9APXfx7oIuapVHM0R3eVraVM3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpyD0fhNR9THP8QLFqucwWM0NGSlEMnPBR92AunmOB49eNiBULBs33dlkLGMXBDW6xkEOhoX2o5Go5iGKPeaKyYLOCtqLoNxfFr9vodETQ4QBOU7FaAkRAw9fGcrhDlEZhy3m4GRzBzQcaVOOQkS8TKVyDu0sACdD3M-uNCE7UccqMWN6OVES0qr8wdBDCMqgeef7PxZLwE4bBNXk-tcbC6dtvDo0TpFL_DVEfti5XdX94qcFiz2zzPONOkbRfJkvlZlSLnzm67fEeu1iqPbCMxUt6VL2sLXbQh5OkU9HZQZmIqGujO-RVZWm5t_IVO7vyHqBoz_sUrzU5-7YMBr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=pLX7jKgBKXMn9DDZ7YfQwVcJFaBvDlAGyyqfCt8jAWi_7qffu2r9XG1epGhuQXCKNiOR-HD1LKYc2MtOwT8uW9lEhS0bRgRLsFN-X8B3PMvwQqfQSr6fK-xtL6je-TMhwanIWUu2TTWK8j37LpnTruhIZE4urJ46sWMkLevgYUNxlhJNz5wEyV1oExeAZVZUaQlT3ssIQbM-i1WeaVLfPVmHjmCMNgAiNUgm3fWJBL1cl5S5Eg3moWM-oDJB2G6dEf43n-uB-NndhP-j0xT5zLBcacfWOA49Npx9hoLPqIi-Kruut1aVtoiBssE7cAhmXKXQcAcXbZt3JOYYrowJ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=pLX7jKgBKXMn9DDZ7YfQwVcJFaBvDlAGyyqfCt8jAWi_7qffu2r9XG1epGhuQXCKNiOR-HD1LKYc2MtOwT8uW9lEhS0bRgRLsFN-X8B3PMvwQqfQSr6fK-xtL6je-TMhwanIWUu2TTWK8j37LpnTruhIZE4urJ46sWMkLevgYUNxlhJNz5wEyV1oExeAZVZUaQlT3ssIQbM-i1WeaVLfPVmHjmCMNgAiNUgm3fWJBL1cl5S5Eg3moWM-oDJB2G6dEf43n-uB-NndhP-j0xT5zLBcacfWOA49Npx9hoLPqIi-Kruut1aVtoiBssE7cAhmXKXQcAcXbZt3JOYYrowJ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=rfcz84OVHs4SoZYKu8flPj6t0Q9tPJgn87Zyw_wH7xohP_IlK197XECIZtZ_5pqxSZ_FinwkWGV-RsOev_PlA_CMxm1OuIfrvnKsbwhpD6NGDt5Nxx7cFn5GqkWufksL9sJ4LU8_dcb1nnMrf0TB9uQXdxNoTREpo3_ECc7vT_BUAC6j6saacrdyNlW3Zw2NykVEB7dqCX3LTKS_v8cTYyhtppM5ufJDYqz8MK2bg2kRiHRrrwa8vhr8DZUbSuadoPLGnkcyoWz4-_691XYkq0TqMwCIzYAPpkKVmOKuTkIm_r37-D-4t7BJlPVcUq2khZ0jHA3-noFqRm2aYAmjag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=rfcz84OVHs4SoZYKu8flPj6t0Q9tPJgn87Zyw_wH7xohP_IlK197XECIZtZ_5pqxSZ_FinwkWGV-RsOev_PlA_CMxm1OuIfrvnKsbwhpD6NGDt5Nxx7cFn5GqkWufksL9sJ4LU8_dcb1nnMrf0TB9uQXdxNoTREpo3_ECc7vT_BUAC6j6saacrdyNlW3Zw2NykVEB7dqCX3LTKS_v8cTYyhtppM5ufJDYqz8MK2bg2kRiHRrrwa8vhr8DZUbSuadoPLGnkcyoWz4-_691XYkq0TqMwCIzYAPpkKVmOKuTkIm_r37-D-4t7BJlPVcUq2khZ0jHA3-noFqRm2aYAmjag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac4BNJdKFqVIJe_cfPKqTKvb_EVAOEg66WXMcbywQo9D5t05-Mmx_p2g-ODN1agpc9qk3-E7xBq7rMkF9dFerR13KLGullf06zN2_iJD35ANN7mQQvMbxK8iXpu2eG952_SipvwMhUIyWfr_6AWX0TvMfxieCU6qz8TXf_FFa24tIuzt7atsz87ois5SZ9RCQNaLJFOorJPD58A6w9RD5aBMWosRENSXpT3B-jrPFtwA7tusnklUEG2EEUl9byazNkeIxfyv8_jxx_FcW7kRnzoSiML_T4XA3v-MUQVRCBAqa0VkZHUaWqJwy7Et5anU43ECpU2ykIjWKCb4j7ngTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAtBmPHEL2En4jK8XxbXjPpM8acf0MJQElHwLTYHMRa4jUd8qaTO3HZfpqjm5sajxmU576A9P7HwG6OBF3Whu1sgdcjG9tavRRIi_U1HdtpZlnA2zlqjIn1GwTnrcScscPrPOcWWAGJNFj1abO2kaHPjLU97Ot4TcwmZRk08NjxpPwTb2AW7U4OcNHJ1HW0C-KS68PdR5IxwwoUtbLqtdtTadN1WAo-g3hRK4s8Cabca3xRoz05x8RGx3ygDYcvJ2d_f1QuuayIeN0O25OOddkYUs0Addhc0N7iA1WU-JuZdFceOsN5UfmWE5jKGIXyWpab0kkZbLSqCgPAo3lcc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=DYIqyqHhYZap7942VtiP6l2HbyiikGtR31htvccuFu-657VbPRsS8kVNMOy6th0U8t8IAhdatxogsawAHOU6uCvbUbCUEZ8LI7Zb8S20FIc-ND9wTKrbitMIw2I-RlVR0aOtGFvLWkOI4JamcyOJ7K0xV5FMSTcXsdobCiIt0qZ7BoWllXfffaUwWJgQ_hv7CAwOoXEZNk-iou9cz6pKtjeKpGh8kZwKn-MJztIzxxCEnsOv2xDK7-_q90e330G9fsZyxExpWeEveVFeMYXSIZ550o3sqxgkS8xDb_8FMWPOM1I6TknGaxFSy-GGMBuuNKRoe0OrA3fbnBn2LgNE-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=DYIqyqHhYZap7942VtiP6l2HbyiikGtR31htvccuFu-657VbPRsS8kVNMOy6th0U8t8IAhdatxogsawAHOU6uCvbUbCUEZ8LI7Zb8S20FIc-ND9wTKrbitMIw2I-RlVR0aOtGFvLWkOI4JamcyOJ7K0xV5FMSTcXsdobCiIt0qZ7BoWllXfffaUwWJgQ_hv7CAwOoXEZNk-iou9cz6pKtjeKpGh8kZwKn-MJztIzxxCEnsOv2xDK7-_q90e330G9fsZyxExpWeEveVFeMYXSIZ550o3sqxgkS8xDb_8FMWPOM1I6TknGaxFSy-GGMBuuNKRoe0OrA3fbnBn2LgNE-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=IAjjxQltLmZQdZB7vfXOqxnAOUDgQV7SSl2DoHHJ8u29DhgC5ctYQ4uUinZd9Mm5x2Bn13nbXNZhIYWW_tPEtokrDBJWMGk0F1V_NTGOojdVs3clWnDxpxIROpGshGyC41kIVcC_F-yzv3DuQuitNbU2Ni_fqankzyHsiQ3nudHmno5oE2HaOTsnBFRWy1oxW-MS1EnFNZMQLcbJ854vpF2LIYsG8Xl3u3G8rtSs_vr39BG-XUfVHWJVCyWQBuHqDcQ-uObMxc_tdVOSWxBQ3CtEdPzmrzJZWJMlR-tWStJR1yS-Czj-d01S30dZKX7c2H2TaKJViT6-Zt9_5h-rPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=IAjjxQltLmZQdZB7vfXOqxnAOUDgQV7SSl2DoHHJ8u29DhgC5ctYQ4uUinZd9Mm5x2Bn13nbXNZhIYWW_tPEtokrDBJWMGk0F1V_NTGOojdVs3clWnDxpxIROpGshGyC41kIVcC_F-yzv3DuQuitNbU2Ni_fqankzyHsiQ3nudHmno5oE2HaOTsnBFRWy1oxW-MS1EnFNZMQLcbJ854vpF2LIYsG8Xl3u3G8rtSs_vr39BG-XUfVHWJVCyWQBuHqDcQ-uObMxc_tdVOSWxBQ3CtEdPzmrzJZWJMlR-tWStJR1yS-Czj-d01S30dZKX7c2H2TaKJViT6-Zt9_5h-rPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=d0UUpixMErAOpkH-7wuGGE293BdTFAujUDpphlOFQaNVHKJaHOUdI3WFDAtL9jZ6u1jckJqmyFhwlgI4-93ARySPTaxklvWC-vjpxW6t0MHhjbNwye0Ffy4FI5o24eKFf-dLyO3LKxnlcuCuxnxz7xtXLrdjbtQwJonQ668_l0se991-jYhqKEAC-4Xm8-jUoF5I-wUaVefsHO3LrO6F2Zw0_SK3PwPDvb_I3sQvP427JsdgkhmIejUPL56PvPTyU6PEvXV9UokDnT3IMUXu41KKX_4GUnDWASIG9TC9Hk9SZ96ANLsCvO6pXU9vdojr0RoP7Od0ycVAdzvfN_U2PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=d0UUpixMErAOpkH-7wuGGE293BdTFAujUDpphlOFQaNVHKJaHOUdI3WFDAtL9jZ6u1jckJqmyFhwlgI4-93ARySPTaxklvWC-vjpxW6t0MHhjbNwye0Ffy4FI5o24eKFf-dLyO3LKxnlcuCuxnxz7xtXLrdjbtQwJonQ668_l0se991-jYhqKEAC-4Xm8-jUoF5I-wUaVefsHO3LrO6F2Zw0_SK3PwPDvb_I3sQvP427JsdgkhmIejUPL56PvPTyU6PEvXV9UokDnT3IMUXu41KKX_4GUnDWASIG9TC9Hk9SZ96ANLsCvO6pXU9vdojr0RoP7Od0ycVAdzvfN_U2PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=tLdq3xl20wdXjuL5F6D0fttWLOHfS8leamGmFxlLBSlvzcZfifgkSnY6GpUtftMQAWJUlw1MeNJgQde4xoZxkDOM94Af20NSpSs-__TQKBNjb6D7BBysjrirH3j_gxeadt75QirgYo-yDq-uDGPnmjJ1c2AJrdTbEJXp0LTTartbWUH1osTRHEzT9ouDfvPnvxPggeqVn2_OEkR-BewuU3iCtOLY8QrAgvakHufsCaxxe-EToVwrGn4izp0aUs4D0tB9xyn11-YRRhTFdDQTDqa3beVHYNF1EjSKqWQuQist7xSklXZ5trxpPyqH8m9u1IlTWgLLMylooSs9XbriPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=tLdq3xl20wdXjuL5F6D0fttWLOHfS8leamGmFxlLBSlvzcZfifgkSnY6GpUtftMQAWJUlw1MeNJgQde4xoZxkDOM94Af20NSpSs-__TQKBNjb6D7BBysjrirH3j_gxeadt75QirgYo-yDq-uDGPnmjJ1c2AJrdTbEJXp0LTTartbWUH1osTRHEzT9ouDfvPnvxPggeqVn2_OEkR-BewuU3iCtOLY8QrAgvakHufsCaxxe-EToVwrGn4izp0aUs4D0tB9xyn11-YRRhTFdDQTDqa3beVHYNF1EjSKqWQuQist7xSklXZ5trxpPyqH8m9u1IlTWgLLMylooSs9XbriPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=m8O-NDsOwsKwcD8zPGnpcz8rweLbHbItEAgExEDjvjTO5oysPQvzi1LcUrULb6c2fYxFXle9hbi10xD8Le044s-iEBE_IrQ3RBDVpYabDUNHA0hZqHnSn0XWTsimj4zYgVHdXIoVAIs3FQ7uTyfpCP_auwQDBnQ73l9y97ZwHRRnPyocMg0jDndJmdIPWbzRqASOWI_gjY3Y79oxypDJZYwCfkOd1iTCBbksrkI1itTHTTr924bTkEFI0pmxbcipTLGxpje3fTYzb_07F921i1l6CL1MDxWIG0hkKkVbVouQHc4oS8kqjfMYfVNXtxYqA4UehCMWhX26SzG_wttgkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=m8O-NDsOwsKwcD8zPGnpcz8rweLbHbItEAgExEDjvjTO5oysPQvzi1LcUrULb6c2fYxFXle9hbi10xD8Le044s-iEBE_IrQ3RBDVpYabDUNHA0hZqHnSn0XWTsimj4zYgVHdXIoVAIs3FQ7uTyfpCP_auwQDBnQ73l9y97ZwHRRnPyocMg0jDndJmdIPWbzRqASOWI_gjY3Y79oxypDJZYwCfkOd1iTCBbksrkI1itTHTTr924bTkEFI0pmxbcipTLGxpje3fTYzb_07F921i1l6CL1MDxWIG0hkKkVbVouQHc4oS8kqjfMYfVNXtxYqA4UehCMWhX26SzG_wttgkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=eAk_oOkwSaNZNVUKPND9lq05B3CNrriSjkHdnSIonRV_vlff1z1i8ZvKxC10zep0_jfypbA5RQo5vopHj5jUzeKjASxSCoeNBy3sKDhdIhq9enhSQa0Jgo4BWAILFCeTlWucjPrh6hJ_6e-Xi7v2FbzP8Ox2cOq68v2A6NyLBjB0rXao4qWMIcoOWcXrOOmkIazd9qD1Toe9ILLvOmml4P2tjDqwr14rx6JpX5RqV2QaR_htEY1tGSl0tfh9dUYaLy36PZ9RzV4nvfs4_53Lt5p6tIcCaol_W8L-WdNNRG1RLqNZn-15ACo039tN1n0LhEBA1rcqtb8WffvOh1jDsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=eAk_oOkwSaNZNVUKPND9lq05B3CNrriSjkHdnSIonRV_vlff1z1i8ZvKxC10zep0_jfypbA5RQo5vopHj5jUzeKjASxSCoeNBy3sKDhdIhq9enhSQa0Jgo4BWAILFCeTlWucjPrh6hJ_6e-Xi7v2FbzP8Ox2cOq68v2A6NyLBjB0rXao4qWMIcoOWcXrOOmkIazd9qD1Toe9ILLvOmml4P2tjDqwr14rx6JpX5RqV2QaR_htEY1tGSl0tfh9dUYaLy36PZ9RzV4nvfs4_53Lt5p6tIcCaol_W8L-WdNNRG1RLqNZn-15ACo039tN1n0LhEBA1rcqtb8WffvOh1jDsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im1KH1U_oOIM52nVJ_FGvYjWqbqzZZ1JhT8u4HvAlXSp6FXPY7Ypw2vVsHmlRh8K87tTe8jJLQxfcbsdez542_9rTVICL6k7pGCqrKa8nOq00UkmiuieB7n53-D1T8rdXZ7l9Gc_1_xYEyxGwedBBNUE3OpsD6JCCtn76QnjD5CVYvR5OyLIeyo8hyaiDwkTdasYJU6yqvgKooSbHsEdNGi8rHF2nr5UzK05pXU9PEf5ht4nPQ_qYpjmMqfWvWW65g-H3MK8hk_eDsGEKylQQaY1zRlB7szxZNnVpXX2JYdM65D764PkKDuIDNV_KlxwuVAWLRT5gT0U9oD3vTwffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Do8Mb1d3NQMFPqjfW-WCTBCS1EEiRNsBVwhEgycrjHZBNoekR-fsnDlVdvvPuAIbNfk4TSAyy9GlQe-J_U9pPkqMXbUQnKfPDSAz_OHINwzCK-VXUhe77E_rUZbm6epseoCEW8KwUn9wn5wzqMDPJvw6s4XWf1_PE-K2x_HBejeNGCSEE4_M5zQRPzMdNedDiYRzlqO0I4Cmjdletss7np7ModMSlHEjDo7bAVOeptQbA0oCDIlnQON6hMq5hFSkFEdqgolC1r0cjTd0TbcnIqAr7MIj6-czPHvFu-3cWHXMdeQOzvQvIKuR-BC1BQiG-5g1vA-ufRtuOUD2UA2uBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9JA5Jg7FA9d_xyS0lTdjw1U_eOGnA23IglRoKmEEypviW_vQtb3KGvvKn6gSpAP4Ul37TwWJ45v57Q3KkRZoH8rGmQIUAfXz2KWcjEXN6-hRY91etlVKFwfMFUqWxbVbMzh58EBT9WT2cKIoWsmhIS-Rhgi_DeTvkiH65We4fDkpQ2EK_xQppP6ywvxx3rCVk4VJ1gBXnKDexcvEtGfEkK1PSeSyp4dzjzUS2KdTrODoSFMUASUyOdwimCUDKCmQDxLGG4aBdVIJ0AOrE_stvqsaifCMwxiaodmYr8vk-7wncCJgBifQltASmwXdeF3bR2HB1LVlbR9kLJpMHiE0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=Ywc9ezL6eJJfQmw2eUusz5uQ3TUiUQubEdIGLwBQxjjm5jRVk8KhLPxXh9Eiq7mel_AQjrkSicrN5wFYcizeu1hFvIV8qwM8EYJXWzpEIGJaANrGlT7T_x5QXLEj43aSmEd9D66DGFyX5ivJeF_0UjXmsbBE-Tmy-XTaKhvhKV6t5XMawaxyeS5qxSYKXsBRrrdajJTCfYBHzd_0FAuIhh_LEvSZWX99BRcJD7xisHELv3-fuL2Yi-_7-LboYwxNTOgP5pJqTfp4KzwcU0b3BMUtEmcCMocKb8W5sQ3Q0onlNV3BV51k6yi-wmFQS-wdw1NndJddoD1EvwtfeqdQyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=Ywc9ezL6eJJfQmw2eUusz5uQ3TUiUQubEdIGLwBQxjjm5jRVk8KhLPxXh9Eiq7mel_AQjrkSicrN5wFYcizeu1hFvIV8qwM8EYJXWzpEIGJaANrGlT7T_x5QXLEj43aSmEd9D66DGFyX5ivJeF_0UjXmsbBE-Tmy-XTaKhvhKV6t5XMawaxyeS5qxSYKXsBRrrdajJTCfYBHzd_0FAuIhh_LEvSZWX99BRcJD7xisHELv3-fuL2Yi-_7-LboYwxNTOgP5pJqTfp4KzwcU0b3BMUtEmcCMocKb8W5sQ3Q0onlNV3BV51k6yi-wmFQS-wdw1NndJddoD1EvwtfeqdQyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBmHBZEDtk6vawUGHKOj5OK_4y26ViC98_XWZFOCOdZ9oRU-FJaxrXByNzazfuW2DePuPgKYqzqsoEsTmcvXqVj5Gy95VLBvqZ4cAg83VqpqEK7jh1ti9OebcgwGzh8HrPFyR3KaOHb_xtJF6cEGdCiiMWUQK8RLE1oN8q3eyPhirzl-B54OXQJ_ZtB3m28BWucv_XFRQdtdvuv7MVTmyeLtnXvrbuj1c6FTiEusRmqwN73aLZveVTFUCqW-2CpbP95zrGnGkWvrvJwxs49KLbjWeXfjE-G9hY53FwYdkZxzTjFwpICvQed0tQTWtSyEGfVRI09OtBzEi9tGimbw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=uFdzSZUHbYZSfbwaLhw_uhK0-1M0g00EBE4OWs0Cb2aO9WcOsUU6phLnAeFPNUvEUGy0QIVqeylslVKWifCoAPvsMXAUCEDSxCrfAdLX73qMGYChZB3a70Mdj_kVqbKrQGEyUjzNNYmwUS2WTG6JjRxrrhf6cIgAGYvLXQEWVnsURLCKl68GzRkNmCo8hZ1cWN7iCTkhjgt4l9zchD-K4QsLzUQS65TW1gvTL_5HhHEqtrSnYKGs9cLbg2CyYBY_YJukck5p0ZOAi-zYf_XT89PpGl10_zyGGt1VApHRCFaAQK6Op_0KRXdqS7VEKrhNuUdAMYiei4QQvHxCyMyCSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=uFdzSZUHbYZSfbwaLhw_uhK0-1M0g00EBE4OWs0Cb2aO9WcOsUU6phLnAeFPNUvEUGy0QIVqeylslVKWifCoAPvsMXAUCEDSxCrfAdLX73qMGYChZB3a70Mdj_kVqbKrQGEyUjzNNYmwUS2WTG6JjRxrrhf6cIgAGYvLXQEWVnsURLCKl68GzRkNmCo8hZ1cWN7iCTkhjgt4l9zchD-K4QsLzUQS65TW1gvTL_5HhHEqtrSnYKGs9cLbg2CyYBY_YJukck5p0ZOAi-zYf_XT89PpGl10_zyGGt1VApHRCFaAQK6Op_0KRXdqS7VEKrhNuUdAMYiei4QQvHxCyMyCSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y_0weV63qFWZ_ojdtzCXnJ27M4IYJ8l3Fp_YeTzsGB4FeC7TiNklUFMkYKTBP-MvJ7EMWsul7hL9jgeqV3Lh0M-a-qExV3Ks2W90QWvFID3Jl17O0lLH7IScLUYRMeQhns5KVTsZvidADVYoJI94bor7hN_Y7hYUGjYmATXYTiUiCtwQULv2KxSN_KyxUUuKWuNwiHGfh64lF2ehArkxnPsKoOgOf7To0P87IScXZg5HfFQfCMVysHXC06pfTLPL4SqwmeNL-JOKC98O0Cw5ksiZsPHnGaXTqtiDLUEMZfewSJauHNibwLrOzINgcksLi_kMHdym_uBTmytoSVNocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=oY1jtFj1eFBkYfIQNHy7siUEaPb_JFEOVKfFtnS5GT6MXRgHLcJhHkUX6UoNN4p1qrpbiK_v6dbnRaQCFzHqY31bgeE_kBi5tHOGfFJnNSmFGvZY4CJ54fPF07wd7HAWXMpJuOO9J9xaA5dsw54QcVpgD6LXLxKSI4gHTgl1rzjkKF6bdyCYcDe8_NshuqYl9fx23eAwM7UxbDSJLjpR9J7hxpFb84KbRZ8hNFkCTuY51ct2EAaatqwu8kbCKeEd7BIfg1Nc0x26IEI-b-B-CyRv_qZ0prlWeVXzU4FIdmqfAWhpPrjCoPSBIhY6YO3tf2Ai7J9QhWEwj3vZWKhZBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=oY1jtFj1eFBkYfIQNHy7siUEaPb_JFEOVKfFtnS5GT6MXRgHLcJhHkUX6UoNN4p1qrpbiK_v6dbnRaQCFzHqY31bgeE_kBi5tHOGfFJnNSmFGvZY4CJ54fPF07wd7HAWXMpJuOO9J9xaA5dsw54QcVpgD6LXLxKSI4gHTgl1rzjkKF6bdyCYcDe8_NshuqYl9fx23eAwM7UxbDSJLjpR9J7hxpFb84KbRZ8hNFkCTuY51ct2EAaatqwu8kbCKeEd7BIfg1Nc0x26IEI-b-B-CyRv_qZ0prlWeVXzU4FIdmqfAWhpPrjCoPSBIhY6YO3tf2Ai7J9QhWEwj3vZWKhZBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVRQcDJXRaCeWDtVvxlDM1nxGA5ICfhYQLwILbCvjHKYll7z1vpQcQRZ47zCPFKf2GY9jGNjCLqShekfowJPudES8Us6y0AAZuQ0Le92NheYqyu9hxyAVeCwTzQRHYBHWi7e_7MRpAxtQDodfGLogoOGcoghOtBPdNaQIQWjv92TUmum2SiHleJMS9TtaN2o6057qcbMayotpnt5U3GZC6aXhbE5NCwIrFAVOabj_pYUiYE4S0-m1fYpgkVrq8o1hPYBC3hOkxScWEUpPbWAQhx1jDTtRpH-1FqOK40NYxMy7M3wcaTehxoikOjqK52D03VE3bat4ouXA6VB1ECUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=JjV5N-qHPiFxWe_BQZAysQA-MgPwtemSkqs3EG-vK8gjL8AxX4YbHvGwxq-xpsmo38-2_4BilWiFAHWjGo6uWiz37K-2f763TafjjON8zngaemwfGIZgtSox-Kfu_ai0AZxjB2c-fERcwz5mbG-lliOK6H-GihQorgktQXbCKinhbhdyFHxWRcGNo7yCJNIcqYSMr18hp_AvuJokLfR_uyJWEpoSaYlVByJaK3OL5E8NI8o5ljhl2WuvCqnOv8qbw_lHJiZpsfuQKNQ5TA9D_UZm39Cz1agjwtkAijbMQUPkN7rfsWM70odLGtEirQjY6Kp_bGU9pAVGqZNwQoAZIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=JjV5N-qHPiFxWe_BQZAysQA-MgPwtemSkqs3EG-vK8gjL8AxX4YbHvGwxq-xpsmo38-2_4BilWiFAHWjGo6uWiz37K-2f763TafjjON8zngaemwfGIZgtSox-Kfu_ai0AZxjB2c-fERcwz5mbG-lliOK6H-GihQorgktQXbCKinhbhdyFHxWRcGNo7yCJNIcqYSMr18hp_AvuJokLfR_uyJWEpoSaYlVByJaK3OL5E8NI8o5ljhl2WuvCqnOv8qbw_lHJiZpsfuQKNQ5TA9D_UZm39Cz1agjwtkAijbMQUPkN7rfsWM70odLGtEirQjY6Kp_bGU9pAVGqZNwQoAZIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=kilY-5eiCUXCKOCnXLui7_3fEYeS4azFpfRQRcAXX7914e5wptgYLPnFlP7LN9iRJR1wbm1MsLuuPkJRo6TnsQSKwflZzVlo44k67xoGyTrPyNb1Mq4LZ2Wajxq5TFk7WTStkY3t3h8jhrG00W5VCzkDP8awvsm8Ok6d0A8cWPsUPjxmzF7RDqyGtYGX8v7FzqDQaQywFbDhrQpLkjqD6SyH3u1vNW36XIM2rFSo2kn_YgNE7dC7nuWhyQRgJpqSWm8Pa2a3Rxf22uwEyvOi3Momu4xGFsJ9fRq2pqPqUJe9ghaNooFBo2pegHLRHpeqbyPHQepRpR8xgi9ba5HUxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=kilY-5eiCUXCKOCnXLui7_3fEYeS4azFpfRQRcAXX7914e5wptgYLPnFlP7LN9iRJR1wbm1MsLuuPkJRo6TnsQSKwflZzVlo44k67xoGyTrPyNb1Mq4LZ2Wajxq5TFk7WTStkY3t3h8jhrG00W5VCzkDP8awvsm8Ok6d0A8cWPsUPjxmzF7RDqyGtYGX8v7FzqDQaQywFbDhrQpLkjqD6SyH3u1vNW36XIM2rFSo2kn_YgNE7dC7nuWhyQRgJpqSWm8Pa2a3Rxf22uwEyvOi3Momu4xGFsJ9fRq2pqPqUJe9ghaNooFBo2pegHLRHpeqbyPHQepRpR8xgi9ba5HUxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vJN2wZ_Qm9HS5LxompLPEJ5-UGMh2KgGHwCvihhT7bNYcye4zWD3r3ckDpWOUyp8CQHM1iIaV_bAihuoZuj0f3COIx2KY5PZvtkNsOUhFM16EhqhP-Hg4TCj5tcoVssQpMa9JO4Tbd9as9JZK1EWKQ4jsO3P7Id-uz0vHysaOgXJOGsqKTJdSi4W2Om7yIq1QWx0UXz86iL2fj1iIHbMvZ2lT0ddxFEHMv4MEeeaTn2PGyRADkdsVqozvDxcs1oNaBdT-vJEh4uQ3koZsSJjaZhni8KXMnCUnx4yC5AOMG5nJHq_qleSV_tKO_KSmykyDg8jUgjH825qiBl_2Xx67A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UxmsshQ6yQpWtugMrbdiP1QPKkuBYbghoWKtACk58JwMSo2tQjPPttnPamL8a-b1tJFGhT463X26s5KQcoofomTRuSEH8CWCZSCtzP2THl-bqvd-bxPwIv77l-Uh1dN_zjDVWSpp0VeKHH7IQVsThA9hk3UG-k8boSttv5mq1VOyEsU9gj_qdCquiPyjIpWitr8aXJCeSSj5teJ1NnEXbg_gKE2VK1gCVwgJeOuY-zzyYEYb090q2fn-La2VwxwTQ8rXbVihprC3IIU0GUYHLDYcyogRXG2nCfP8vparZRbH2XBL9zs5CdngyK_yuUyjzUYX4RprIdTPa1DNoiB_4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcD3JLrsGTN3JvxWPXGTtpw5ruj1w2UrxMKMAXpF6I4laa05e7xRFQIIjl3wBP4FSQLunuEoYAEW2VXMIFeQY3aqaXUT9BEzoktBED4IWkaYg1ocI6FzynPOq1auO1YMhPohDQlOE8bQ5bjsRuV5MgjfHbjjW0OkIBn5uAEyUzOPB1NEduDwOAoQU25C9Mfmi4JDknUMo6Ikr7AQXhFTODy1MoTq_SrMsDIB4qYIMweEFcJIr-ND_MSc72YSDBLWh-Qe2u0ByaosD5-lpXh6kJhftgpcZpQUxh0C6byAAM3pxfi-9s7gDXnAE9p5op13VVN9MiY6LT8E5eOXEd7hYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=D-P2DLqYcT2rxRTTVFxl-PTtLIAG0djBDqguKqyqoB8PrtmmgTX6pOIGEYAyd2_dbC808FzSdCkm7qEDacprxnpyi0C4n2xGoavSWmmbtrZSPrvgUG0iq5Nq0o9Cl-uzY84jOlFGeUdl7N7LkUwYJlX5yUwna4XZrCxUKh80-Xt18I3bTeYSOpZhrto4Guhcg6Dx7iVVH2B8IPn_7_69tZFO0G2DI9WnGN5Sizc9QNxdwiJ8LkiKSDeoj5QrU7t_gydqxUVIm0vrPsbM3lfmdArDpuqwq3iooOcJzcN3VRPBF_9nyuZeifSfzdu-UPtKCW0deWoCEGM1OdKh5lWK8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=D-P2DLqYcT2rxRTTVFxl-PTtLIAG0djBDqguKqyqoB8PrtmmgTX6pOIGEYAyd2_dbC808FzSdCkm7qEDacprxnpyi0C4n2xGoavSWmmbtrZSPrvgUG0iq5Nq0o9Cl-uzY84jOlFGeUdl7N7LkUwYJlX5yUwna4XZrCxUKh80-Xt18I3bTeYSOpZhrto4Guhcg6Dx7iVVH2B8IPn_7_69tZFO0G2DI9WnGN5Sizc9QNxdwiJ8LkiKSDeoj5QrU7t_gydqxUVIm0vrPsbM3lfmdArDpuqwq3iooOcJzcN3VRPBF_9nyuZeifSfzdu-UPtKCW0deWoCEGM1OdKh5lWK8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=hV1JXDreguDlPn5dCdtBixJjiFmo6jN1_5YTeYBdEh9tpPd-5CJo1uT2X-Ox0QHVB_15sdqxfuqE76DtaTheEB_AaYiLTaWnnrsHiC_5b3Uf00k3Gbg4tymRMoCmk5AIbRXsmIN3txAdbzEHJMYNKMV55PmaQZVf2n4F2xOTrzC3Yb6R_y0C4oTcZBeEzhxq2Big7zSsOChqyVIT1--agIniZKU1U8_O2m1g92rC6ay9MlC3UXJN3tmDkmhO4oYhrghBknSUyqoct5wZa6v09h_yJlb06k6THeszFzlX9pa1oSWiLxgR24XM14s-l8srMP8NqUO_zofQ2WbuAlTD4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=hV1JXDreguDlPn5dCdtBixJjiFmo6jN1_5YTeYBdEh9tpPd-5CJo1uT2X-Ox0QHVB_15sdqxfuqE76DtaTheEB_AaYiLTaWnnrsHiC_5b3Uf00k3Gbg4tymRMoCmk5AIbRXsmIN3txAdbzEHJMYNKMV55PmaQZVf2n4F2xOTrzC3Yb6R_y0C4oTcZBeEzhxq2Big7zSsOChqyVIT1--agIniZKU1U8_O2m1g92rC6ay9MlC3UXJN3tmDkmhO4oYhrghBknSUyqoct5wZa6v09h_yJlb06k6THeszFzlX9pa1oSWiLxgR24XM14s-l8srMP8NqUO_zofQ2WbuAlTD4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQY7zSPGcmBJTSvimpOeXqOBMjF4MFOLJpf-fuilNf4rEQyuS7bN2Y2A5CTcUd4-XcgpaQ7mJILfLz9cLn-ZRcg7N_-KUqrxwrDrkDat-zEv67J2IwyQ6NL1t1L7VRF0WVTTNDKWVycEvNeA5FdAZaKTziuJwk5ORoqI-U_8eN-amrIhmgf1bimD33xxPdxB6B4zf0D8pLdJIRkyHii8qK2azTACZQEorjQktCFOG6eO0uyzaHIOLq9xdvVyUak8eEgaQOC62AeLy1he0j4mrBkXYZVHjDl8n4ztrgSxDAm072RrCbmom_kJMxXhaBR31X-lY2Oi2sXHyWJWVwi20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0n2cPUgnpl6krHJab28BG4831XTxlZLOqWOysSA64-rUNed4eMfkIbTQpMzQgn1gKiRii3A7h1JXOuPPq1qtp3m68nL4d2RiGZaYVYj1jFc__auOi33kWpxxeCHfNhL3wuy0xTGNAMAtG2ZN5vWPrkGbkVmDotLtzcgJfMmXxaq6Wq_zpX9UxZGrrzzUJ5XKkjRpN6L8ykcgpk29RHCu8DIlX6kULHuIX0rX7F6lWzHZwWLY3n7rc2c7zFW--j6qNqidS1EYxWk2PVvsPaRj0dbSFfykcs7WUQdg46MvI6G-sW_b9pTgeMwxLsvb1RdaS59dFBA6tYouvMgFd1qug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkE6WAmlDSVpTxZ3sviCPP1whdOZUPvXp8ezrvaUjUzfyZKNK9yPaTNwXNX6Qi89Fox8ObWszlYl5q0k-C_jkVz10P-bvynIlql8b7ZRl7OS1FXhVq4Qv8xp-fLQuvjWrfhYILn6g9dRbECMcq9X4lpXV2KGYkS7IPiQsZJJ3S90cfIBIlbLusfVEaQSVkLOg18Y5CnsSbmL3rA98rr8Ma3wtwRpm2LvPYC2emgYvx1ddi5wiu2_Hw2mKic_JV9XAur3gl20jRVv3W_A6ytiuNP8-xCWd7MbuTwH1UImgaUGyQWF3AHAACIqkAq9jJ6aP1mn0cDlh8hOE7_VfLSV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=lSB0aaGPJ6egEbyx_YMuXqhXL8ex2osusIjyylwN-GCXCu3t6S4yMe8zv4scrcpaoIpVHR1ARdD0oifBUuOySxpcSZ8f2_0KEe4b6QmatF_QqAK-dM41Ft_QUxK-HpHYULj1KpiH5Tjsnf1gcGIkzE2L1m0UuzfkTJl_txQYnwqxLHhrA7iKuxPWV8ZAoJtvhndnMsJ_JRFgdhgSzs4XR0dGBFSD-eT6q4Y72xz5CmOtpJXBk45GyPQFQ8yhrg2XS72o_Tlub6adte9c3PDz1yabCf-cPLhr9WAUwtUwzXbCPx6Wsl3O9d5ocXm3gJdlF2cNeTk_CiVDrc_rJOo1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=lSB0aaGPJ6egEbyx_YMuXqhXL8ex2osusIjyylwN-GCXCu3t6S4yMe8zv4scrcpaoIpVHR1ARdD0oifBUuOySxpcSZ8f2_0KEe4b6QmatF_QqAK-dM41Ft_QUxK-HpHYULj1KpiH5Tjsnf1gcGIkzE2L1m0UuzfkTJl_txQYnwqxLHhrA7iKuxPWV8ZAoJtvhndnMsJ_JRFgdhgSzs4XR0dGBFSD-eT6q4Y72xz5CmOtpJXBk45GyPQFQ8yhrg2XS72o_Tlub6adte9c3PDz1yabCf-cPLhr9WAUwtUwzXbCPx6Wsl3O9d5ocXm3gJdlF2cNeTk_CiVDrc_rJOo1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=tYil66U35qzWAuoIRrebnkcyXPf2vAiQVjL9virbWWCFF0T697QblqGcbvcegDtS9DRLsFKzWsHI_7c2aDjo0ZKC5QiVlXPMlD9F3WKjOJX6zgLF-9O9PxElZ26COxK0sqyQZSQkPDkFsR0SgjdStXJRaBHLEF_-PxotFoTBpIETjTvHU2J8_lEaU2XFgnDhPuZJKpQPi5wUqAQZkwqrncCyQ2gCecFghFPfMHD5yS1eThSqx2ZBboUX---WmTXrNxQ1jEWNaNOw1EFA8IEa4odnlo8DpWQMOvdoXVXAlyIVzetF2hE0nVEjz2z0G1tAlHsEocTlKipNEXEQpaqvfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=tYil66U35qzWAuoIRrebnkcyXPf2vAiQVjL9virbWWCFF0T697QblqGcbvcegDtS9DRLsFKzWsHI_7c2aDjo0ZKC5QiVlXPMlD9F3WKjOJX6zgLF-9O9PxElZ26COxK0sqyQZSQkPDkFsR0SgjdStXJRaBHLEF_-PxotFoTBpIETjTvHU2J8_lEaU2XFgnDhPuZJKpQPi5wUqAQZkwqrncCyQ2gCecFghFPfMHD5yS1eThSqx2ZBboUX---WmTXrNxQ1jEWNaNOw1EFA8IEa4odnlo8DpWQMOvdoXVXAlyIVzetF2hE0nVEjz2z0G1tAlHsEocTlKipNEXEQpaqvfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=MBm4BrN8lHQUnKMnRrVVmqlCnaoUZsngJYhIH-5y-RY-tPZGkHglij5IB7nQPkrVyTb8iqjLUku8FkIfYgXodk05hzQUHZvFa2jzg4vvJy_pLmDfb6aPDcCdh1je-DhqcQRfvecxGIv7jYYCxvAEANv_e_Bbgthi-IT9N61NyUIECAqZvIXUTZrTtbjQ6dOt9k3WMNvmp70XdtWBq-yc04mJYpaIxvS7xWHbq67AAmzVZjIup_dM-P2NmipnC5JhzQwBgJT2OP_l2UNNLhOuO1k0sZv_gSCH1NawYoDy1ei1OohWVWoMQmca8EKjMQf9b1b153OmowOFkIGxtagDDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=MBm4BrN8lHQUnKMnRrVVmqlCnaoUZsngJYhIH-5y-RY-tPZGkHglij5IB7nQPkrVyTb8iqjLUku8FkIfYgXodk05hzQUHZvFa2jzg4vvJy_pLmDfb6aPDcCdh1je-DhqcQRfvecxGIv7jYYCxvAEANv_e_Bbgthi-IT9N61NyUIECAqZvIXUTZrTtbjQ6dOt9k3WMNvmp70XdtWBq-yc04mJYpaIxvS7xWHbq67AAmzVZjIup_dM-P2NmipnC5JhzQwBgJT2OP_l2UNNLhOuO1k0sZv_gSCH1NawYoDy1ei1OohWVWoMQmca8EKjMQf9b1b153OmowOFkIGxtagDDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8-eJrTt5qDY5B88u88ba6fReapYDmTneXRsZXT84TPK6gbj0NroLiaKfh4xERN-TtlRpJwE1c5FdkZnYB41xiJ7rFuw8SAyyRoSb9vS8XbnGggsA6P_pTEtJypnfG912bv8paU0KU4QNmLKVxAnlwfguQYuvqE_pp9S7tofqW5x6n5FgtjF73AD5awyYhI9o1nBLzX10ESCAQb3m5wwoW5LeYz09_Dh6mCaOIaZz3ptymPQPA9iXOMSsLTokfjERDHzN5UBhr9QiuhpVeFxHn_MkoDeXXLlPrUwUwqyDuspnaBI25vEesMmD_bo1aGcUvESHZ0GB4TUiCTJoirZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=VsBBljY79oKMCxOJyLSWrO9eZSWGQ-tA05VfQ_EEhWGSnId9cZsEQksc2FDqM6zkonBX1de3RBDXMl0fEk8RD1r212v-mFT-WfOdc-5eqcrJ8ATxDjjcS0R6mPWHhg0PTsqYe3fLJMjyorXO1yq0PTDhK__ANGQiquCGHqjOFdnv6cPaLIgYq9a9IERdhdbCe9Agf383rQ8ASIsg9k5cs79_-m5xJMlboObqM6SSHJVbcwhyhJUU80nUGeChbJSQpoI0lRlBUo262-F7_SAIXTLvQAYbgjgiIPqRQvGuQLbaJ9oqvRgbsacmGTDywMkGYxGMvJSmzyhCq9t0_UHERw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=VsBBljY79oKMCxOJyLSWrO9eZSWGQ-tA05VfQ_EEhWGSnId9cZsEQksc2FDqM6zkonBX1de3RBDXMl0fEk8RD1r212v-mFT-WfOdc-5eqcrJ8ATxDjjcS0R6mPWHhg0PTsqYe3fLJMjyorXO1yq0PTDhK__ANGQiquCGHqjOFdnv6cPaLIgYq9a9IERdhdbCe9Agf383rQ8ASIsg9k5cs79_-m5xJMlboObqM6SSHJVbcwhyhJUU80nUGeChbJSQpoI0lRlBUo262-F7_SAIXTLvQAYbgjgiIPqRQvGuQLbaJ9oqvRgbsacmGTDywMkGYxGMvJSmzyhCq9t0_UHERw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=eZawFqC3xaUnEsQTrS1zJLv5REqXiy1gKSZbKyFpAJwKzvf3Vr_-z8BQMyowEpf2nYXBhNSEc5HEurYkztaUIWmKRtcE-tmmLbiybz4WCb3pVphux7BOFt-WCahj5Fjl-Zub7RGQgQRBcI7_IfZc4mdusp1EnWuwbVmV-IGsnB7FqbHuwjSckFoKPNH-wzLnKs_hCTWN3uTY_OsgpVqko-rDz3ZsxZDOLHghQy3QwGmG1dfEN9b6BnYwWEdTuBwcIeO0UKLJcBzep0BrztZG8jE53G7Sh66xtqOxbn2Ro98sJeAtsSYE1Jzw0BPMcAs6KY_grihX6i60Eb1e4W_sgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=eZawFqC3xaUnEsQTrS1zJLv5REqXiy1gKSZbKyFpAJwKzvf3Vr_-z8BQMyowEpf2nYXBhNSEc5HEurYkztaUIWmKRtcE-tmmLbiybz4WCb3pVphux7BOFt-WCahj5Fjl-Zub7RGQgQRBcI7_IfZc4mdusp1EnWuwbVmV-IGsnB7FqbHuwjSckFoKPNH-wzLnKs_hCTWN3uTY_OsgpVqko-rDz3ZsxZDOLHghQy3QwGmG1dfEN9b6BnYwWEdTuBwcIeO0UKLJcBzep0BrztZG8jE53G7Sh66xtqOxbn2Ro98sJeAtsSYE1Jzw0BPMcAs6KY_grihX6i60Eb1e4W_sgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=r5sp_ek0HBiMbeDlStlR6d98t_TbS80wNM36SgSKpOqfNLoUYXlzwYIhDy9g7kTa2r-YHgwzavKBxF2b7a-g5bmrNATGE-zFFbqX7SHyBk0vhjWvgojkDSySs6zfMVr_8HB4m3aHGIoSeVarRWe4OANqAN6X7y7KqAdhV0v3onroXABqrTdZzDQnTvh75zw60aOf9P_3ZANlK5A-iSTXsWMExAmyvdEdWNxWjPUN0pwZM8XOtymMjtQuyG0C9LBPm6gZlk_UilNMWv2CtYUTKJzra8bJUvxtWj8YLoGBR4wQNQacU4pYBgkq-vJeO9Wb1YoiQc0WY-0HYJXCMjGezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=r5sp_ek0HBiMbeDlStlR6d98t_TbS80wNM36SgSKpOqfNLoUYXlzwYIhDy9g7kTa2r-YHgwzavKBxF2b7a-g5bmrNATGE-zFFbqX7SHyBk0vhjWvgojkDSySs6zfMVr_8HB4m3aHGIoSeVarRWe4OANqAN6X7y7KqAdhV0v3onroXABqrTdZzDQnTvh75zw60aOf9P_3ZANlK5A-iSTXsWMExAmyvdEdWNxWjPUN0pwZM8XOtymMjtQuyG0C9LBPm6gZlk_UilNMWv2CtYUTKJzra8bJUvxtWj8YLoGBR4wQNQacU4pYBgkq-vJeO9Wb1YoiQc0WY-0HYJXCMjGezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_yZquZ5lfarh4ZS-vEl5G09gdiN36Mm1dSx-v5iRn9FY2SUW7KlB5o30GqC_r0q4iHWtidya96ItD3ei2XNcoxWAoG0LJHrkXe8cCK279wUYmrlo-RwfGlVvrFOzlQnUP7puD8DTgZyzjfwyZBIUuy24xe4cPXkF28VelPq0ZChcoDFm96_tuSrt4w1ov01ExzalAcV7ep07hIFaOkzIw42mAFVvdg9fvp6zTUCO-2gBj8siBwnx8ylUWLcYrfou_NoqgiC3j696Oihx1CR8SE2W8FJiKiWpzvyK5mAUcsAwBf-qplS_1wf_5lAxM9GE7C7LAzyi3ZphD47fovY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfvkvv-nZFlkHUPUKcrodyLjM_vlvFLtPOYG3dsNcUx5ku3228BpkvanMTIjuihsltpEmHizT-yhjJaye-VKi5Fm3FA4J-dDc71pRZKa_LNtlEEwJirAZZlVoJfepLEARDSA7L6fJggO0oM_UPHjhFrWPUDLIgOSj97AqCJ-wjjkBR9XTGaBk2eVWo0VjWm0kgb2ceFR73uibCMkmAp-n2xcyC-qpLucah0K25YFzYqx82rTXS6EDRZxmzeKoYUoCGa0dkUCqOg7PKHu9i7brIonRgJGnnboo-KhJqh47wj0bklWuSnb-TLkIxYlV5MlXq4m2Tme_0S51evaG6InNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fgw5WFmiLyT8yY6gZoddvB3gYP2ifoKjUxqJ-Ck0GTKeR8p4sWxKIuD1_lYQ0vdlxDf0mg969wi2weZ94vemtFwOoP_dQtRry63UBQDMetip2VvSzDqOdiHIDPBbuRGLSiR1BVt4ZbJKrmPLfLgWOefaIBWvhohuOvR39QJfEP5kzIhjYyeOcEaFSIbSx7QnTIGBETA6P5XLF53NA7FeXyPCLTAzUyq9D1yFd3qkgHijjqNfyI4XUF04k4kkSY7FZL_crI_CmbXuLPT4TfrK3BTmzx0frPnuP3hZoQqlPBismtDsOpy5hyk3i6Qc7E2AWhZm7FL-gVHHnQkpNVpc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTT267JEMEZDNvveZG-kiCueehW_WtXl-HyGvAg0hLhCm3HkxcFuH5mOSc8d6BZkWEn2NgljW3TKTCCYrQzD3R9rWtfafAvmLlUblh7qGQREOzK-hGNKEqxJlFdHN_oUJwBNLlgpGSy9hWs6JSDt59XINSAHksNuzcBdoaZ_0ZamyPGzhOQRfeMDfFMtGazJ0Rl8krOaIE_VlpGO1STnBdKo40TLpt_NoTSzoYi17svgUXmJ6Bh5vKGcuqPm0FYtoIAEfgCIiNhfFXR5y7gnkTkfN7iw-XbGfkAhIr8xiOYSvqbFJ-CxWu1EXjYs-Ju9OiRW8OYfM17snsB2uazveg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=uZb3kbqoOsKbIppNetnDyrPxwelKSJjtW5gN_toKUy2BDBlPpRIi-vTlo3kvhmROXcFtS_QmCoxNHylrJPTl2uSB1Px1SfxN-vMQaQz0XVfghnq2YMN609d3DLXtmnW-M6i0wF03TXibJShkURtYJnydlm-9wK7uJSHLflRgs3AMCqxt_77Fi5Xs6GNllXOAiJFg0kst9dR1_zDJlO7Gi2Fezs0q5DzyfcRAKAdb43izunAUne9RV8dc2slJ-LXi0lzKsRka1u1uiE8jWObpB-FbOGjYwR0qN3fvQKRcA-fVKcTrevxk9XFX1x-JZprUE5UyaZ1rx55SkchxltLg1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=uZb3kbqoOsKbIppNetnDyrPxwelKSJjtW5gN_toKUy2BDBlPpRIi-vTlo3kvhmROXcFtS_QmCoxNHylrJPTl2uSB1Px1SfxN-vMQaQz0XVfghnq2YMN609d3DLXtmnW-M6i0wF03TXibJShkURtYJnydlm-9wK7uJSHLflRgs3AMCqxt_77Fi5Xs6GNllXOAiJFg0kst9dR1_zDJlO7Gi2Fezs0q5DzyfcRAKAdb43izunAUne9RV8dc2slJ-LXi0lzKsRka1u1uiE8jWObpB-FbOGjYwR0qN3fvQKRcA-fVKcTrevxk9XFX1x-JZprUE5UyaZ1rx55SkchxltLg1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mg7lh6rAk3g52Zr61jsKAfMBeHfE_32E2wuBoGEHwzmK0dkos-HZvc91eXVfzC_EIKWGYuiY_ovevIL4DscDRDUmDhavLzk6CAeasB5rObt-hRoOZG1xFtFzWZSSjVsMULaFZAvr2we2n6rdbU4tQK3WPvKla2I9tX5sIAULR3t-k_Jf-RSFRDix_ov9tSFos1m4Rgv1WxhNPsN4xHHJTBv5k_VCEcGaY5c1px36z0Ck5C7oHPIQy4CUY0KYLH29yDtmrNRbC4Te5cH72nux3DckI304uqrIbYlDKErPesTx_0UKa-3QsHByYhNe12cQan3cPt2gZUe6Pg7k0FRXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaTN4Mug3pLHj5AUJ9NElzBmpdMken59CQmFthWJ1yynRhKoUCAM5H0a2Bnw9BvOuOkeOLgxQWqRAAht1Th95ZGEWDOnJRSH5Xi2nd1MmS5Fo9H1PQRE8_76Q5BqTcFPHG82KTyYbnppgyrL3mnjmTx3NHsqUvj0nxRHgS2mOY6yUNC5NL7OL42lHvJtvJj3gPR29tK-njGx1qjO783X_dUNsPi6l1oji2vJIJSz0h0MP-smWCWsFHIpHVD3W85f1IBHtaNbuDwtH8ulVo6eixPQq1vRs3kkVUF75W1c0c6K5OYUgVGa3ErjVGwa1XIfDMAQh1Q8pG9bX9wi5soJlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVUbuxth4lhmKYOkBIJKfDiK_6InSjviEW7HPLTC9mqgyurhJZxpbLSLpbuXaV3vzcO3Hhvv8ksmmc05SVVzaedpABOzmuqjXxQxyZKoE395EraIPs8WykVS937Zc05NRvYKJpz-ys-374v1Hei-KYSeJxFfnO-87ziFbprSQpWmVx1_XVRRvnTm0xjQyb-KWyjFOCcbsoHxcl4Bp4wEIkkeC9SC09d63BDn8u-Br4Do6cFTac05A6ubx2zow-bFK4nQadQ9h_aHYoEEctTUi-WSPajQyO5UpGQJGViHu1AeU-Fr4zYpLz0L5OovWN82fDBU0Eakf3OnFKatblwa1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=NdbutJlesxK0SNhecyugTBvI8_HyQtYzj5EecX3CqPJYT7g9wHcdtIyBahYg45wTTMiKtSlIBYa8OisHR96opCHMHH-3NlG9sxbevANervBP9PJp0WJotXIBPKCigZOlFk6MNf3KKVFxLgiE6Ditm449h9yAOo4Gqsvt9VxQ9y9doQF_8dl7n_C9uJJiX6bjEia0AHYIXlME0i6PEbZULZvw4-wfcRnh_qeHKwPqgznS8L5-aSFIlTaZ3iuMNiJRsIwR_ccCoHF6Qgd7ImCcb9r1wU1vyK5P8vuH-EC4zbK7EOwX4gK0_q2_r1GCmSexvyFaLxSaC37hVJ_NWSWqIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=NdbutJlesxK0SNhecyugTBvI8_HyQtYzj5EecX3CqPJYT7g9wHcdtIyBahYg45wTTMiKtSlIBYa8OisHR96opCHMHH-3NlG9sxbevANervBP9PJp0WJotXIBPKCigZOlFk6MNf3KKVFxLgiE6Ditm449h9yAOo4Gqsvt9VxQ9y9doQF_8dl7n_C9uJJiX6bjEia0AHYIXlME0i6PEbZULZvw4-wfcRnh_qeHKwPqgznS8L5-aSFIlTaZ3iuMNiJRsIwR_ccCoHF6Qgd7ImCcb9r1wU1vyK5P8vuH-EC4zbK7EOwX4gK0_q2_r1GCmSexvyFaLxSaC37hVJ_NWSWqIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLp1YSYZO5-QhbMAdCzFePZ8NZ1BrEAgDUAJZuoG1-0Px25slOlVM7Au6wRRED9U6Di9TrVsKQSH_LTMSOzRGSTf4sRBHs6klu3gzQm_wyC9OP3mL66Pam4XeyhRFLvibRs7hMOtY610SKqXrprmiG5qKwnGydLrCp9s0rs2CZRurfka06L88PEJxbiEJ4eh6fSDxj6WMToQIIvjlGfy5rclkM9lmrASGRFhCkM69OD8J356xZrPGnen7MMJQXHQ0XtrA_LwXGqavdEY3B2fsBsKUw1lZ6a9h6xPLw7RLY8gSSdTCO5XcIWrBqmwT23ZKkq-W0YegFwXeIa7z3I3KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=oprkgpefVrqB_ubPl8BojwHfYOlmD5tgBu_cH3qm1sNYkc3IPFR3AJh26XP4S8YX4R-YZXmp4S8lRpDmbl18Eone69id4ZQdiAwIAG6Eb0kIJPME8NavOLqvAx69NLJJk9KEwOr4ZJXt3VOTVyIIqblvrpoRu74mDhSga0Nvr1xShEp6o8AufdN6q3uXHOrCQD7KasDXEXIksRHT0Kt_tz4mV23bbYwDLYxeyLjnVioWK2xBj4K55RubgjS5z5bn9bP7Yg9ozs1hVGRNRV7yNthIzRHUk0JXDh7UO3poGFY_Ac2mUW80VL4CjCS1RI3xoeK_9iyugEGhrEjm0Fq2nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=oprkgpefVrqB_ubPl8BojwHfYOlmD5tgBu_cH3qm1sNYkc3IPFR3AJh26XP4S8YX4R-YZXmp4S8lRpDmbl18Eone69id4ZQdiAwIAG6Eb0kIJPME8NavOLqvAx69NLJJk9KEwOr4ZJXt3VOTVyIIqblvrpoRu74mDhSga0Nvr1xShEp6o8AufdN6q3uXHOrCQD7KasDXEXIksRHT0Kt_tz4mV23bbYwDLYxeyLjnVioWK2xBj4K55RubgjS5z5bn9bP7Yg9ozs1hVGRNRV7yNthIzRHUk0JXDh7UO3poGFY_Ac2mUW80VL4CjCS1RI3xoeK_9iyugEGhrEjm0Fq2nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=lJSmYj3CKB5Rj2pLFqVI1yhl69JWrHYY3Q8Ia9Nm2qbOxjourM5ix8I3-Rzb9mzBnVUbxV1K5g9fhROWKVh0R2MH4Mf0uzHUu0lBXrJKZoudBGButCz2i0haNnUWcX-cOl_GH5XIt2S8PIer96eb64J-RoOKcynzvkeOsTbu3I7ZVqigk_BY99_SQimNy4MYku76owB5OayMF2Oi1hJqEDBCfFqyC-YgfFOgvwtaizKxHgT-Z_1fu1Lvo09d0Um7OGxrWUbRjd4o9fM_XJjaV-qKDMSPmo6nxmgxmg6B-Hyl_evuOVyblM2AV6nVrCnaYROIDVyu_Ly2kMhR_-XSUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=lJSmYj3CKB5Rj2pLFqVI1yhl69JWrHYY3Q8Ia9Nm2qbOxjourM5ix8I3-Rzb9mzBnVUbxV1K5g9fhROWKVh0R2MH4Mf0uzHUu0lBXrJKZoudBGButCz2i0haNnUWcX-cOl_GH5XIt2S8PIer96eb64J-RoOKcynzvkeOsTbu3I7ZVqigk_BY99_SQimNy4MYku76owB5OayMF2Oi1hJqEDBCfFqyC-YgfFOgvwtaizKxHgT-Z_1fu1Lvo09d0Um7OGxrWUbRjd4o9fM_XJjaV-qKDMSPmo6nxmgxmg6B-Hyl_evuOVyblM2AV6nVrCnaYROIDVyu_Ly2kMhR_-XSUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=cLRp3QbmNX2Jy9kdFhJgs6X_CeXiRX0BHd5Km8NZ3sRrOL2AaOulO2Op8EuD_g72OF2moNDfm1V66vwTmND5M1mq2niRmj5eOuQh2kh_bHT6MCKiUIL9MofExFArtVpRIEC3F90G6yyJxtGJGKIl2IZ_W1dlEtYGy-HvjE7_pzqGg_limCaFwlA_yMrHdHu3hHQYFtRnWlSpdU5AkvIbTO87IxiceMXiTRtKUKq6aekWiMLXuswwVyU8-Av4CDhG1-PyZVbmr2P9odebu3BcSmaYYi1Q-o6b50swMIBEi4eV7GbLd-ihdAQzOggTZZ9HoTetcwxyJzXbEzD78qLBdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=cLRp3QbmNX2Jy9kdFhJgs6X_CeXiRX0BHd5Km8NZ3sRrOL2AaOulO2Op8EuD_g72OF2moNDfm1V66vwTmND5M1mq2niRmj5eOuQh2kh_bHT6MCKiUIL9MofExFArtVpRIEC3F90G6yyJxtGJGKIl2IZ_W1dlEtYGy-HvjE7_pzqGg_limCaFwlA_yMrHdHu3hHQYFtRnWlSpdU5AkvIbTO87IxiceMXiTRtKUKq6aekWiMLXuswwVyU8-Av4CDhG1-PyZVbmr2P9odebu3BcSmaYYi1Q-o6b50swMIBEi4eV7GbLd-ihdAQzOggTZZ9HoTetcwxyJzXbEzD78qLBdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=JjfGoLRzx0upyOZeT_Fgg0-pyCS5fYCgDjk3AnLl9TKuqBDdKg19LAqm0DfDvJyi_ZYNrwM6pc2DaMuBxpnxPJhRpWwbnj5ubcZInn6DHTNLH2fVvzeUdGAGyMaBvdVyP-jnsXEvkvoip1i-Gp3NqDFa9SgAQTysMv5ahTCBVqv6GSH_HjG7QuOKGoUIAuWd_mHVmIyMOqq5sLyJmSSR5JTpy_NcvWU7KUmx1q2aQn1dzaFgsDAuXj3SnqeWC_Rl8kH6NmdGfC3G-7RoHv9DR34PQ8deiAg3yj2M-gmJ0Ta0vfiIgRD1jMzXIjDOViBA8RW5bfM4w1nryBV66SQ25g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=JjfGoLRzx0upyOZeT_Fgg0-pyCS5fYCgDjk3AnLl9TKuqBDdKg19LAqm0DfDvJyi_ZYNrwM6pc2DaMuBxpnxPJhRpWwbnj5ubcZInn6DHTNLH2fVvzeUdGAGyMaBvdVyP-jnsXEvkvoip1i-Gp3NqDFa9SgAQTysMv5ahTCBVqv6GSH_HjG7QuOKGoUIAuWd_mHVmIyMOqq5sLyJmSSR5JTpy_NcvWU7KUmx1q2aQn1dzaFgsDAuXj3SnqeWC_Rl8kH6NmdGfC3G-7RoHv9DR34PQ8deiAg3yj2M-gmJ0Ta0vfiIgRD1jMzXIjDOViBA8RW5bfM4w1nryBV66SQ25g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=IPS5e7_fVCOjPsuhz5jrHzSjlEC-_BGer1GCt7ZvjGmkBF_ufdEEkhbhZxpW_DRCdZtwXmCuZuvYpbucIGwfq6kjfZYiFoU0zk2Ww_DNT-H2-KQeLMccje70s8CdPscxNQgZhDoXhy1_aebw0GC03X3RJomooAiFTphYJYPoV8NiPJkrj13clP7lEd9wAKORHTUAc5Q_1rXZ2Mwnw23xM9zB0AOyyTNd2vNetmet-0qMGRdv5icjTqOMC2TkUMQbe1Tx8738lPM7edKYbEUY0PE1RN_e6dSsvhDQJDsYpFgHSM3So_Hq6NzN2NHqL-tdwa0DD6LarCUTUfAsEcpu2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=IPS5e7_fVCOjPsuhz5jrHzSjlEC-_BGer1GCt7ZvjGmkBF_ufdEEkhbhZxpW_DRCdZtwXmCuZuvYpbucIGwfq6kjfZYiFoU0zk2Ww_DNT-H2-KQeLMccje70s8CdPscxNQgZhDoXhy1_aebw0GC03X3RJomooAiFTphYJYPoV8NiPJkrj13clP7lEd9wAKORHTUAc5Q_1rXZ2Mwnw23xM9zB0AOyyTNd2vNetmet-0qMGRdv5icjTqOMC2TkUMQbe1Tx8738lPM7edKYbEUY0PE1RN_e6dSsvhDQJDsYpFgHSM3So_Hq6NzN2NHqL-tdwa0DD6LarCUTUfAsEcpu2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=bOBoMEyJEZjIinJSQsTRFWXqHxbn6rD5qwN1RKj6oQR70aXHukdngoizOncM0vZhJk9fDi8ZjRnb4oqUSiuoGgXC_RFmv2D2bQedaXkgkiqrpZB2qKYz-5oe2Xs9n9Pubyaq6GKVsXM2VPjas7D-G_R2nHXnNGjs7-VOT9BPGO9L8dOU86NoaKQsajHnB5VOKYMB9_iZH6Dzl2ugQtNrIUlca3cFSddY20jVjw6yeaiiwQDl73tS6fqtDtSdqyYdXVFhdJ_in_GihgZ0fTVPxHUOWXSTfk2ynUGfmUz3pUxeVO6-SzgpopFSza0q7GsO1qMonMe-IWNfkLjJxGPG7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=bOBoMEyJEZjIinJSQsTRFWXqHxbn6rD5qwN1RKj6oQR70aXHukdngoizOncM0vZhJk9fDi8ZjRnb4oqUSiuoGgXC_RFmv2D2bQedaXkgkiqrpZB2qKYz-5oe2Xs9n9Pubyaq6GKVsXM2VPjas7D-G_R2nHXnNGjs7-VOT9BPGO9L8dOU86NoaKQsajHnB5VOKYMB9_iZH6Dzl2ugQtNrIUlca3cFSddY20jVjw6yeaiiwQDl73tS6fqtDtSdqyYdXVFhdJ_in_GihgZ0fTVPxHUOWXSTfk2ynUGfmUz3pUxeVO6-SzgpopFSza0q7GsO1qMonMe-IWNfkLjJxGPG7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=jNrYnf1rBLxvnbLA2r7nHTJ9CM2ZRWoeQB6cTQCNDYEwkLJtDUWiHI0dQynG9yvugL4OOt2CG_A4UWTkf7slhYTWMv4rhKtKgNE_oDU2He6C8GhlgOk7sM3hBOY1txsTgtODeROsScJDC0uUrogPPjHr_PH2kn8NzU3549DYfiMbEbU0Vl8VvzkfAL2UyRAUozU7Ewk6o_WFNoDvjoqLrzAJIGab36va0BvlgRUPrYukppM24EyIsYykMfelYxar4T-sZCvZDepFJZ5rjUQtOVuJa4q3FZiPrPW7KP-CUcab7U-kCxD7-1d-AGTN7afcKrtmVKQvc4YrcTJvk6ZnNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=jNrYnf1rBLxvnbLA2r7nHTJ9CM2ZRWoeQB6cTQCNDYEwkLJtDUWiHI0dQynG9yvugL4OOt2CG_A4UWTkf7slhYTWMv4rhKtKgNE_oDU2He6C8GhlgOk7sM3hBOY1txsTgtODeROsScJDC0uUrogPPjHr_PH2kn8NzU3549DYfiMbEbU0Vl8VvzkfAL2UyRAUozU7Ewk6o_WFNoDvjoqLrzAJIGab36va0BvlgRUPrYukppM24EyIsYykMfelYxar4T-sZCvZDepFJZ5rjUQtOVuJa4q3FZiPrPW7KP-CUcab7U-kCxD7-1d-AGTN7afcKrtmVKQvc4YrcTJvk6ZnNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/oeJYfWeItllMeijaOGyZRohQZK3WGsRS9l2nLOqCjRixk_BLQwRc9abs5-waV3KuOTLEqwWz790XX-9OzLIB7GrWIO4uavLZbQk1H1HAfDBrWbSehJwl-wlu8mOjiQQSQYSQg58GPM_Eeve2XAyGR5820JiDmthHgQjfFqzyM18Cy2vUQdGQNmMb9wlZkD4MJX4vsX8kC5n-5Jgsea_fMlGT7uBbChbjy27rA9QVf798g47I2GZsnwM0cvdpnqMI-OyuxFVGsaTw2t0Eli9CRixOto1AKMUD9RO6DTOjJevuLmO1tsvu_oYnTsAqckC0QdG4d4AYsC0BaG8FHXzzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R2boETEcBObzZklMuUBgnXiCaI3sh-kztvbzID3zAuGeS--i4xl_VVLLSgmKAp14VP7VUWAKUCW_oRqzRcCKVerOGXrOn9ka_GGdzCU2BawPe6O8PvJ3jwSukP_fOMlnOXJue6hzgWuredU8xi7jL2EpNkvVWDF6neD7Av4iRwFkBoPpwTWS5NKnT6FfX8fgfmSie4MsKHJbERZOOIpGGFUfkBC5RP8GOWxILZEJHtwhUPeeTmO3-wsBnbd3hCDkYm_MtOFVVpCVpL-74KaW_aCqCDfaDXEYgLePdO1KYTigGgB7hBbPqV1F0uHmrV_EG1RygBT-wvdZUWJWHr9jnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=LwIV438WGcu3PfstiykbnNvaWymeWG59Tql02KfPY-MI6v25Ul5c5FaD1YcygbJ8BimSg0j39IQ5gWCfFgL1Rt7WZ1gWK3pRrePX98IuSN5xz-3obhTh8IWYby1RUb1QMx9OEEjgxGoXfSfcWzoZ63RXoFSXANu18hj7dNqX3w8HnEAvvMdopJ8jPVh3L846FnWt8X9WHlfViI-StxLksBz7FrK0r3NyR51c4C12i_-s5wNcLvo2nssUmLXAcid7qa-YiQkWk5l9tWfeoPg4z4L0N9GFgXthAOWRsozFrSbyYXO46DjBD5kpHrB3m1ue-LFijmUBSOmjrZoA7Qq6HCetdyDA_ruIzxWePe05uxuKStRqV2QWHXQr91XEmqBePdinh_fvOogPE0MR8NSvaZJXd4zy-zcgNEAMijEnHpLpStMAgdK8Zv4oZOkdZJ5LihmNA5I5stmb03OUxRp8-9BEYTO5fA_ZUnYruu9FXXniRZj93HhN-9whe2miG073UdUI_1F7aQmsWnqc34Q-HmxCy4aSCzk-MVxKRPeOn02jyOgk-o6x21h2WEM2ipOgeAnDAT-BlNgHHP6SUMQebJMyTkdDc-0tVDzn6Se8YY5mL7t-Qtx4herrkPBIiuzi4kszRLeTog5m8BwAq-ajsfaOLX-Gz4EerFcptbuCIQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=LwIV438WGcu3PfstiykbnNvaWymeWG59Tql02KfPY-MI6v25Ul5c5FaD1YcygbJ8BimSg0j39IQ5gWCfFgL1Rt7WZ1gWK3pRrePX98IuSN5xz-3obhTh8IWYby1RUb1QMx9OEEjgxGoXfSfcWzoZ63RXoFSXANu18hj7dNqX3w8HnEAvvMdopJ8jPVh3L846FnWt8X9WHlfViI-StxLksBz7FrK0r3NyR51c4C12i_-s5wNcLvo2nssUmLXAcid7qa-YiQkWk5l9tWfeoPg4z4L0N9GFgXthAOWRsozFrSbyYXO46DjBD5kpHrB3m1ue-LFijmUBSOmjrZoA7Qq6HCetdyDA_ruIzxWePe05uxuKStRqV2QWHXQr91XEmqBePdinh_fvOogPE0MR8NSvaZJXd4zy-zcgNEAMijEnHpLpStMAgdK8Zv4oZOkdZJ5LihmNA5I5stmb03OUxRp8-9BEYTO5fA_ZUnYruu9FXXniRZj93HhN-9whe2miG073UdUI_1F7aQmsWnqc34Q-HmxCy4aSCzk-MVxKRPeOn02jyOgk-o6x21h2WEM2ipOgeAnDAT-BlNgHHP6SUMQebJMyTkdDc-0tVDzn6Se8YY5mL7t-Qtx4herrkPBIiuzi4kszRLeTog5m8BwAq-ajsfaOLX-Gz4EerFcptbuCIQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=Fgm5jQeLjkxJfDaEoQVLnDvFdJJ9aGHmU-x31KPX7at-a3KMW_mWmy0lVoUkuFDB4O6YeO-UfPGrD56n59ZE2TlcIZM5y1Z83lmN-jMRDTKsdVESfz5BiwAx-j3zSo5wDhU1Bw0WPhUmfIybsIZ3pYNIWNWThCgeaZPaIy-yZfzNtm6LtiK_Ko45pChGpfbIH_pp2TeovY6oPSJ2fs5ou-Vi6Tjv0jQYXRnuMqSuvihLosXXq3ArA32qT7gf6qL5_w4Fz9v7JGBnB6s0EHhlsWoOmJMgtejdiFWekXg4cKQLnM3yojgQKxwhpvLdstmZENGFYMoEvDv2WmiqZEwFAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=Fgm5jQeLjkxJfDaEoQVLnDvFdJJ9aGHmU-x31KPX7at-a3KMW_mWmy0lVoUkuFDB4O6YeO-UfPGrD56n59ZE2TlcIZM5y1Z83lmN-jMRDTKsdVESfz5BiwAx-j3zSo5wDhU1Bw0WPhUmfIybsIZ3pYNIWNWThCgeaZPaIy-yZfzNtm6LtiK_Ko45pChGpfbIH_pp2TeovY6oPSJ2fs5ou-Vi6Tjv0jQYXRnuMqSuvihLosXXq3ArA32qT7gf6qL5_w4Fz9v7JGBnB6s0EHhlsWoOmJMgtejdiFWekXg4cKQLnM3yojgQKxwhpvLdstmZENGFYMoEvDv2WmiqZEwFAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=l7AEPmuaicZfWkgVS0oyxUgVLVKCAEXbRm2ln6M737b-nt3RCyEfRig5XvLERy1CleQlOUvspVsROJ9JmpH0wFKy5O35kRh7SBcmsKTxbdekk5hJKQ37AeTsJXsxsDrHmPMnL5GlZBbQC4RKYk6vIHQ7rSfiQFcP8VPbZLpKQvItssre9u1jGneyuTZBMXf9_TA4ukk50xrf5g_smEcdcQRcAf8nuikVJ79CWyMADkuzghfIi2_1dMYd_WWk0eJqRFMbWAC4JgQ4oRncQ-L1Lqx_jaWzCKUzBv_wEpdG3ZdONVamMZ3nO8BSEID3KDWU_DlyCeMF1kmfxE20S0HLZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=l7AEPmuaicZfWkgVS0oyxUgVLVKCAEXbRm2ln6M737b-nt3RCyEfRig5XvLERy1CleQlOUvspVsROJ9JmpH0wFKy5O35kRh7SBcmsKTxbdekk5hJKQ37AeTsJXsxsDrHmPMnL5GlZBbQC4RKYk6vIHQ7rSfiQFcP8VPbZLpKQvItssre9u1jGneyuTZBMXf9_TA4ukk50xrf5g_smEcdcQRcAf8nuikVJ79CWyMADkuzghfIi2_1dMYd_WWk0eJqRFMbWAC4JgQ4oRncQ-L1Lqx_jaWzCKUzBv_wEpdG3ZdONVamMZ3nO8BSEID3KDWU_DlyCeMF1kmfxE20S0HLZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=TF8RcsqgTPGuMq4vBXP_6fxhRGtLBbSo48QyI5CCc1Vyt0cJUV6OYh-SDQsMDhsEifqQdOMR9jeU24RRfQ9DDr1kUcYXVf--pPhjd3uR--OFCtZgOf6SLXBwjTfh_CD52ku9ZWM_7g4-Acl01MfQTSm-xBNG3Mrtw7i82RFNJwCTJjumiN7rQSyOGnPKsH4eBSSphsZFJ5jR_TNgxKcLNkifEe4vWT3CeEMkvYS4C5OWZi76C_702cCDiflag0z-cSS0BcCRFr3H7h5jmR3mDidmLAdcP8yXEi91dPDlZ45PeBUY-JOayMgfWsrdv5a9Q5KXmQjzNGC2jm4vIN-URQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=TF8RcsqgTPGuMq4vBXP_6fxhRGtLBbSo48QyI5CCc1Vyt0cJUV6OYh-SDQsMDhsEifqQdOMR9jeU24RRfQ9DDr1kUcYXVf--pPhjd3uR--OFCtZgOf6SLXBwjTfh_CD52ku9ZWM_7g4-Acl01MfQTSm-xBNG3Mrtw7i82RFNJwCTJjumiN7rQSyOGnPKsH4eBSSphsZFJ5jR_TNgxKcLNkifEe4vWT3CeEMkvYS4C5OWZi76C_702cCDiflag0z-cSS0BcCRFr3H7h5jmR3mDidmLAdcP8yXEi91dPDlZ45PeBUY-JOayMgfWsrdv5a9Q5KXmQjzNGC2jm4vIN-URQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=crBXhAreX0_-fSx67HKIEFwpr4YFVAxFi00Uy5ALWOZvtJBcoqGt4NLg1TsFNJXHY44-Fjlwzft7C3Kji0URL3Me7yWQOolSK8q8h3ovhAH0hcgJNwQCafNrvd6oUMHILdeeASOQikeTe9qzAbJW9epuhPEV8zU5BmLkAS3KcytYJdXiPs1MiqCK8NYoboKgXTBKNK1YZM0G2n-WT2bR5lxVTe-p7rNX48F1ZlmFAWt9PC3LUS6x3DFm8oqftTMaaD1qdRElTUl9Ac3he-zPykrOE5oDr3MtIZSx-TIuG3X0IndBlR6_YJlZUAJKYrujryRRfT-csk1NV8EXTCieXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=crBXhAreX0_-fSx67HKIEFwpr4YFVAxFi00Uy5ALWOZvtJBcoqGt4NLg1TsFNJXHY44-Fjlwzft7C3Kji0URL3Me7yWQOolSK8q8h3ovhAH0hcgJNwQCafNrvd6oUMHILdeeASOQikeTe9qzAbJW9epuhPEV8zU5BmLkAS3KcytYJdXiPs1MiqCK8NYoboKgXTBKNK1YZM0G2n-WT2bR5lxVTe-p7rNX48F1ZlmFAWt9PC3LUS6x3DFm8oqftTMaaD1qdRElTUl9Ac3he-zPykrOE5oDr3MtIZSx-TIuG3X0IndBlR6_YJlZUAJKYrujryRRfT-csk1NV8EXTCieXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ70mX7g9TtaBFn_CLichAa01cm2CTT378Qt29G4RoqPGIt4KCrXIQbR5fr39oR54N0h6xPJdfe50Ztn-iGFCvn-44tnCwBq-ulc_bvVRJcubMrtmJ-GqZj6k8SAeENrqgO-I9gJ7r7PJg5wPn-hQew6SvmP5YbfZafGQXPrW0JTPI4G26nlA7PXFFZX9xtd9Frudqhp6vBn2VcBd7TDoKGlNRUzO_anisgalyQKhtvsL8fER3rvj7XA6eu28ICa-Cwl__oG1l1ZTSyToHvE5vuw8mFhtw83mCYnZbyvRpb_I9DDQvVOkAzpyPAWwcGs3jndrZD7tzH96HWIU6GFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
