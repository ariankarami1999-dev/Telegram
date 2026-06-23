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
<img src="https://cdn4.telesco.pe/file/fZnbjiToV5ruyywVWxuEEifhIqMzYxKQ-Brh1J-UFdNg5l_aX25_ON8NG8Cpm3X8rl74khPXG_8jtuPbMHI9M08EPXJvMmZNscd6j2cMQfpcH7zfFKrLjeDG0idWkqvvOrCGqxe_x1WtVxnlIf4942A-QiG30OoVLAV8AHGC0_Kfb_BBni4PQ5aAYctNVJzptynPjHbVePTsM2rKIPOBjrCSVKqJc29x-LcBzgVsqmwOyIqZIvZf4xn_TL2Db2g1i_dxQEz3-O-puvWj3qXjl5IR9WZblGt9CeTF7TmRe0GqHYWTxaOrCe9z0H3PsrvnhkFh9hThLuatKbGULUdexw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 175K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 03:19:16</div>
<hr>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">و تمام
انگلیس موفق شد غنای آماده کارلوس کیروش رو متوقف کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/funhiphop/78638" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">توخل از سبک بازی کیروش کلش کیری شده</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/78636" target="_blank">📅 01:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بزرگ‌ترین اشتباه تاریخ فدراسیون فوتبال ایران قطع همکاری با کیروش بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/funhiphop/78634" target="_blank">📅 00:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETPN8DH6cVgyeEZZYM-iYaydmj-kPef5AczDTSEeDvOgfigKR-pQX9ecoTcgsmj4XgGp4T3AXYkswAd0z0UjH9dP70mTa4ihxZPfSH74J9OEkMhLYRH9Lme4a0GJl-pu51wuj4kXUt7REd4AvEXp4bynQJkG2ZWbRqIDUswSarvywIXxrCwemHOlk3Cp5I4Z2PGfr7upL2DCX19CAMzMQX0FH5nFaKKXZYutJof-i5njXYFJwwvbB2B_uIMOf0ziwo10KIlDx2ix4dhakge8SZ10BsJqKnapWdUi_9HqxR3qBmUs19poBsejSjAPxb-mGGP384PooQsR6zlkxQsPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد ۳۹ سالگی بزرگ‌ترین، بهترین و با ابهت ترین بازیکن تاریخ فوتبال هست
مردی که با وجود خودش به فوتبال شخصیت و اعتبار داد
تولد لیونل آندرس مسی بر‌تمامی فوتبال دوستان عزیز مبارک باد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78633" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کیروش عجب تیم سفتی ساخته دمش گرم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/78632" target="_blank">📅 23:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=iXU-VUFxc6ClcPdHVzP2oTS2BTDIY0h4k-1XoyUVvOVypc3mrKDTXvwZY1eu_liHWdmZn-TSCAb_1UjNkvUtLiLTHHChg-5vV9by1EnFLtq_jfjaePM9W6sgBpdiHsagf-e9KJ0d-4nu3iYALd3GqSufaohC0IWnqXml8Fy7zlDijHaJHjNEuMOl8vNdO0VvLEXuTajf2MEMWlhUxtX9Gu5I9sW2BEssJl49a2teY4cdQW3j26KF_IaNgK3NP8XALXIHukjllgkyDmcbUWZIedxzuI0zy01etKdvoBtq0vsZYIKrwxUYnE339TsPocNBfoZ1daGLyBDkxfpwshl2_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=iXU-VUFxc6ClcPdHVzP2oTS2BTDIY0h4k-1XoyUVvOVypc3mrKDTXvwZY1eu_liHWdmZn-TSCAb_1UjNkvUtLiLTHHChg-5vV9by1EnFLtq_jfjaePM9W6sgBpdiHsagf-e9KJ0d-4nu3iYALd3GqSufaohC0IWnqXml8Fy7zlDijHaJHjNEuMOl8vNdO0VvLEXuTajf2MEMWlhUxtX9Gu5I9sW2BEssJl49a2teY4cdQW3j26KF_IaNgK3NP8XALXIHukjllgkyDmcbUWZIedxzuI0zy01etKdvoBtq0vsZYIKrwxUYnE339TsPocNBfoZ1daGLyBDkxfpwshl2_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهره هوشی:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78631" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">واقعا افتخاری که تیم ملی نروژ به اصالت و تاریخشون میکنن رو میبینم حسودیم میشه بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78630" target="_blank">📅 22:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این سری کیروش کمتر از ۶ تا گل از انگلیس میخوره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78629" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شانس اصلی رو پرسپولیس آورد که کاناوارو به اورونوف بازی نداد وگرنه درجا تمام تیم های بزرگ دنیا مشتریش میشدن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78628" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بازی تموم شد مبارک رونالدو فنا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78627" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پرتغال امروز با پرتغال مقابل کنگو 180 درجه فرق داره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78626" target="_blank">📅 22:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خوسانوف از کنعانی و شجاع  هم کیری تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78625" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faixXVY6Fso_pJh9dL9Pa9im2aJNVayV04L2ocAKLPSKA6Wd-ZHZzyEIJ3n-j0RNFp4sKSXswC663jPE4E78N8oSC880xRGuSYDZG1Gkj_onuvxnzsMvIABVfDT7WDkwJXByBpPBVSH37NEHIQ6gQnjInikJvUXB0cSEdodJADBJ8_fD5JXksk1GadsDeukb7rIpuFxoAERb3fcjCLgtJU9fdSfBy_NexToj9LDx8cehVELB_IRNsOe93yyNTbZJ3xyAorMHLTAQj6v0le93OYkTBXUJe5kwY4Nrm8ymU6l7iUU1F8zPYhUJiuMkB_9Liw9dOcfAoDu-tv2SscpvQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مسعود دکترای افتخاری دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78615" target="_blank">📅 21:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3t81DvEGuH_iU4Oogc-Y4WGhcMYmR9OniRq11Q00xfUuCe34yTigjw3cBwgA4NFL-C0XE0hc7_Xu08J8F4RPKrewNmzAl92aHAFy6b9dQqRoMfGyycq2Y4YTc6344iD5mfRaUAmDjfeEwY1AyZJv4Z5nskJFiNhsaEAoIK7LxQG_qBlGEgBiF293za8rgEAOaSMfI-kZ3LmiD3axHJxCzBvLCABtE-7QHuWXkSkyhNTv8dnRPG9bOTSK1aNMlq7Tmf6y5sTcZLF0n5IhXLQ5KVAC9cKUxNWE2WuSKEsMO-U1HuzENMU5zQmjCa6wP4lygdNIpP5PsRa3klAt7mZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو بعد گلش سایز کیر ترامپ رو نشون داد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78596" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امشب تعداد گل های کریس تو جام جهانی دو رقمی میشه؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78595" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCbapY9jeNyXAglDhQTvmySWq80AAmEwVnfE14wEDUGVgYU_6dbfN2Xwb7Wqo2h_4iEd77FgbQTtyztrXI8CwPGa_ow8WxKYAaLXfVsqiSD02bbIB_7A6mJ7i5JqfsJjVIDiTuxCoqlM_pbO_qhcPlMS0aUCKVnZECGQKpkBEIlNAagKkwSp48Ek1S0g7Q1tLmL6XjJxByY2_C21mOEUxVDAwk1M4INj6e7ZYhRPelkUIK7CXSAB4nlud7WZTmwBelKq5vWWN4daB9lZoremLyxElr-up6bUUt9oHGSoAJUB0d6Q6WWYEeZhFs3WxTgVoH2wnExf7b9eykg12ENhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نوسو بغل کرد
😂</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78589" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78588" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره  بماند به یادگار  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78587" target="_blank">📅 19:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسپویل:
رونالدو امشب با پنالتی گل میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78586" target="_blank">📅 19:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78585" target="_blank">📅 19:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiLUCgzVbNmwGObEvRa1fDRLD5ZC-jCw3PoZoIRujytrUS4mog0WNvaunIaBpcA7KcbhV2Gwt1KFCaYi2QumvBSadaLCiX_8K_FHAozG6Df-x9jSW7jjYFumb2CYBAYvL9IyEz1pxsNJBXauc4v_Zg0DWlxu6AvsbbKJAV160HW0hqr0MaH_1DZ8Zj1ojLJOUCM3AUIWGtJbWHR2EAPSldmek2VrQ5l2RAu7GeIXkv7ERAck7HphmnnJ9ojbVgFv8EG55Av6kjL78Ujk-rRklSQYNWwKFAoL056Ghwz2KNtdYHU324f_ikjo4FH-fwgeDvw5PsojIu6N7tIAbgJOAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jj7e9whDb2uBAhqXHMu6SKXS0XdpmrGMTFb57dgHf_QJ3_sxVh8JQgbm3rg2dbFImtEJW5oVZP4wG1ehJpOLBo4j7oFZggudlCDexu6GVei0vA1s8nL84Be31o38ybUyCWYxg-X01kPxHpLoh-YtRzYxwSIKVMI0W2u9gk782V3A6SQgD864FfK-kI9961P-C5xbH_uz1srgJ1j51NXY37sd6xLwjYjBQ_Je5YAM_T31hQmFmXmBDSYxyfV2tYvu4_PyDqLzoGfmaaTn2OhEr83328lmkJhiilDf9KumqSBV6Ri21kV3VFOXKTCF5wzCfbDU9NDZxoZs2jXEeF279g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب پرتغال و ازبکستان برای بازی امشب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78583" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=EORmPVkymle8KlkCK8H3cYKpQ0lXg4QVVFqmyKule1AIfX3wFRdwvz3x5__hUhlf9Y863mPnfXCDhwBtuz-WikXznB-aN0xEGz0ESY2fxJ75tQKLnG8GgmXXB-TJUf3zzj6385mUbvAb4u3PB0pef85M5B76Ijj-Wx1UnJQ4K9Yh3nXXUEj46uXaOdvXqc0_kS_0TxM8gjcMfE87iquHpJoA0HkzeSIAYjOI4vaUjlo9gS7O3M1ffBWslW1ZA6qfHZln5lntXlVjxsf8jCozhqyeH222hr0n9ar87MrrIGyxM-LQnS5hyXWQqdMIWSnbNrGT-R7Jj_nSiptbfHYvTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=EORmPVkymle8KlkCK8H3cYKpQ0lXg4QVVFqmyKule1AIfX3wFRdwvz3x5__hUhlf9Y863mPnfXCDhwBtuz-WikXznB-aN0xEGz0ESY2fxJ75tQKLnG8GgmXXB-TJUf3zzj6385mUbvAb4u3PB0pef85M5B76Ijj-Wx1UnJQ4K9Yh3nXXUEj46uXaOdvXqc0_kS_0TxM8gjcMfE87iquHpJoA0HkzeSIAYjOI4vaUjlo9gS7O3M1ffBWslW1ZA6qfHZln5lntXlVjxsf8jCozhqyeH222hr0n9ar87MrrIGyxM-LQnS5hyXWQqdMIWSnbNrGT-R7Jj_nSiptbfHYvTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سریالی که دکی قبل نوشتن ترک نگاه کرده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78582" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78579">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo-uU4ZvU1PNTcTNzbMfqGZ8lUN2vnQrnlfzIU6H02z1U2xOPMHGbC66YBiIbH8GdlE6KhQ1Zi2qw46DGQispCGC76L6a81bQnc_BdiGH_UEIA1vsLDUY-Ll3sl2UxstskeP2U4aHrJyQYlBG0nnx4pEUJnhi2zF9N6sWiyz03tXsO9kcnKklZ-TVFtJYSdohi4tHkLsx3sLmcRl7nam5ONEI1yMZvgLOEAf71IOaALigae12XCD8EkxwcX_SFfpHSzqXY7qSrW8Sgra3mFE5MX16lRL0xvHR_oXj0EhxElOposqwXTeDW82VaYa_Ghudv8W90D_0XKwKU1LbwICUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
برای اولین بار در ایران
🇮🇷
تا
0️⃣
0️⃣
1️⃣
🔣
سود اضافه روی شرط‌های ترکیبی
🤩
ده تا بازی میکس کن، سودت رو
2️⃣
برابر کن
⏩
فقط کافیه بازی‌های موردنظرت رو توی یک میکس قرار بدی. هرچی تعداد انتخاب‌هات بیشتر باشه، درصد بیشتری به سود بردت
اضافه میشه
🛍
🆗
تا
0️⃣
3️⃣
🔣
سود بیشتر با 3
انتخاب
🆗
تا
0️⃣
5️⃣
🔣
سود بیشتر با 9 انتخاب
🆗
تا
0️⃣
0️⃣
1️⃣
🔣
سود بیشتر با 10 انتخاب
همون برد، پول بیشتر!
میکس حرفه‌ای بچین و از ACCA Boost
نهایت استفاده رو ببر
💵
💵
📺
تلویزیون لایو برای پوشش بازی ها
🅰
g2
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
🎰
همین الان وارد شو و اولین شرط ترکیبی‌ت رو بساز
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78579" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR2kUV8PdPwo-sK61EJhn2uxtK7A6CDylq_tXpnbgHSn3lTvDvoLKWwh8AQsH1wtzZVJ0WQARlOdHxbkoB9S3CjkLfb9t6G2dUSldXf83YgREl2SKLMGKxFuu_3A44jfNPprf46p1eMkmUjpgYPh5AdD_jihZK13t1iEmP7TBX-Npqg3NzmNq1pHSMjYj07tLpkFOQwuDXqHSaLmkiuQsDAc4ZOLBXsCYA0mAMOwhYFKK5MTsfhjxXvyEVUmxsFbKgXXzFn0lMPdfnAEBId63BRI1JFuzZ_0-zNviJcn4qo2ZtgA3TTMJkMAjXz5N22okD_nmDzNaMMOL41mbDZtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیت دانیال اصلی و مهراد جم بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78578" target="_blank">📅 18:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFOg0iKY1yl1WQznvKc7ILDMcA7q7DgZmXMRVKJv9MS7-RxXeZrJMX4gJ5W_Ay--0Xtj-FF9FOQH0PfYeDSCG-CHSSh7ZJ8vI4U5MZwkwZBkEnb19lRVdTVQO0GelgoyIpcYglU2R4ZI4nyUZzmv6-Bn0E_s96utSWkSvQYpVObFSwsE9MnRbNOkjawjSUjKqCbzHAta4VfsZ_q44x7QFR3_v8WgabWu4EFttOC7v2v4_yQmMMnBSCBtWqzP_54koIya4UNhFCwSZFtrtjIWKiHGBFsclJaIOslfNkZ2Ys1Pm_jmj5Vupzk8Ri25YG_kWVDR0ofn_LTklUnIezAGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که سپاه قراره با غلات بکنه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78577" target="_blank">📅 17:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حرومزاده این همه ناله کردی که آه ۴ ماهه زنمو ندیدم تروخدا زنمو بهم بدید دارم می‌میرم که در نهایت ببینیش این کصشعرا رو راجع بهش بگی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78576" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فک کنم پدر زن دکی پوریه، وگرنه هیچ توجیه دیگه ای نداره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78575" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78574">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78574" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ PlaylistShip ]</strong></div>
<div class="tg-text">فقط اون بدبختایی که فک کردن لاوه فور زدن برا زیداشون</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78573" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78572">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خجالت نکش داداش از سکستون فیلم بگیر بعنوان موزیک ویدیو اپلود کن یوتوب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78572" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دکی: صدبار تو اون خونه کردمت، جای بد نرو جون جدت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78571" target="_blank">📅 17:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دکی: مثل بابات عاقلی مثل مامانت کص
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78570" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78569">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اونجا که میگه چسبوندمت به دیوار با صدف بود یا مامانش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78569" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza𓆃</strong></div>
<div class="tg-text">دکی وسط سکس نمیتونه چیزی بگه چون پای صدف دهنشه</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78568" target="_blank">📅 17:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فکر این که دکی وسط سکس به صدف میگه مادرتو گاییدم داره مغزمو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78567" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8qVhFVNrp07JfXpNG4V3hFY_bnRKtDYpJa9g9kN9Opmvkqq0MO7DZAoe6BOX68no69TYdCu28uzHyZ_AWJRG3VHN2m7lYIAFCb-DXC8nTf5mkFCykvPRVfv36Rtwf_VFrqRWt-1Yt6gDwB3qbBKcBqKcVboldAp9EfGcomG9lvqELabAjUgo7Rv9Euy1XiOfTGXMIs9CnvFlnd7xE3DWr-mMb5nJcsq38Nk9HedXobHanFqF_YtEdHCbDwzfVmFSWQgq-aKBlELAEmHIVCkP3M2rOwfsVGoRjzBqTA5USLQDC42ZJQG5EHCKoJBhWXKoiz94_zkDYXltPXovOx5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbB4gukqBz3hf75XI730WPdgEWQP9tlOZgzmou6Yp0o_hBwkTsr4AAolzUh4hjPmzbxrf2vSLdv96jgfI6MuYAFfA9RDtmUQ3d8txwc-PcJ7GWXScn_SMCH8uT_Q0-0UvsJCSEhIIitmnW0mxNJzCax0pEFHC_3Tw0xggIqxlX_zonKRQy7UmIfwr2zaciEEg-DXua-R08URG8-4dWUmEWNogZ3OBA72HRg26msINSunXQ55WNS28h_I9ZYLRUHXuuUurDubGil2RfXT7o2BNc9r20a67O9xw-9NK0O5-ZwQGozyarAEpyHiWSVKPjFfFN7HH1L2MLzp-1HtIv1bUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78565" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFykGRxKXFGRIlm_Ikw7VP9QA5Ua7kDScipIzkanlk1mLdn_lFPC1Bj7-uNqfKwP07wD-0AxCky6TOyIGaNxuUvncxpfTMqaec3coL22Ir1MpQ8q0yIXcnM9poi_iryeR51mEwq_OCWjXMmuAT8CE3z2TXJF4m6tLemqkcHw3dQu_vfRsqyztOh2wCkmiC8iI9LFRu3O03AxHk1M79Ke547EG04apenDd_-3gXQBMZmO-di3o-er7RnDJxej-h4WKjudUgani1IUefutiCUdW7Ahuo3WvTS0_4Ox-uGZjRLJCv8GeE7IIQidGe77iRBmDVseGkBouxlgm_8bCYFopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.
Youtube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78564" target="_blank">📅 17:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78563">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کونی رو ترک عاشقانه این چه اسمیه گذاشتی</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78563" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دکی کونی موقع ماشین شستن من چه وقت ترک دادنه</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78562" target="_blank">📅 17:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78561">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تنها چیزی که اَ بابام میخوام عشقه فقط
من برا بابام قیمه میبرم من من عرضشو دارم
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78561" target="_blank">📅 16:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0d6UV9vuWj6vQaSZnKSOv-8zAkb19xnDMBMAs5djA2JhADNISmvCPc2PMKR2tp4L1l9NN98WdT0a5GniRQKdQ6JasrRs-XhkS_ds_QcAthIiItdCTrfrNl0LAGvjU9D_dlK5e_CDKZwy5aiKTojIB8uRQ6KfbSUwA5GWxTOmEi2hgknpX8l7ZBsWRIFUWTlP893Z_odXjFks2LeUdLjBhInF3fq2o4rcEu3_EbW8W34wQKAOLqKTjjh0owTXR741zMAmoRZdcEjw_wvg9OxRyBlM3Yfs--J12a77Zz1Quf_tofMq_sT_6u3Voo6QL3qCl22uoZoV1ZqsH6-oZJPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو رسانه‌های آمریکا به جز فاکس‌نیوز کلا یدونه نیویورک پست برا ترامپ مونده بود که اونم کیرشو کرد دهن ترامپ و توافقش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78560" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwkhhOdMTzJG5-MyHafYX_CJ_QTxFyk4ETjejv4GKUTPP-U4wCjQG5EJ8npZlWr0MvFZ6pQMs9TtFfGxGAgjSMhNlLba5NPjF_C8zvxSwQrddiTNFzMhTlNVyB83UJorZKuura0dliS_gTZEv56Ao6cztwkESXkyaT27yS_8fttSmlLXP_9UsPLxauDIA5niDGX3r35JkcL6ld2jGn4W6lhLdFPj4KH6CVWcROsf4udu9qUcA7r0bAo5fikoMNLhOKUJjgeah2yZz3rl3wPAicKX130zrwj7qv93yITQe2Nx0Uoi53FHc8sbtasqR6TUcdk8ATqZICie3o3Z2I7gLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا با دست مسعود روی شهبازو کاری ندارم
چتر چی میگه اونجا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78559" target="_blank">📅 15:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78558">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پزشکندر و عراقچی رسیدن اسلام آباد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78558" target="_blank">📅 15:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">علی گرامی بخدا خصومت شخصی باهات ندارم به عنوان یه شخص بی طرف دارم میگم، یه آدم رندومو تو خیابون نگه دارم بگم بیا رو این بیت رپ بخون از تو بهتر میخونه، روی این مسئله شرط میبندم، پس لطفا فاز نقش اصلی سریالو تو یکی نگیر بزار یه نفر این کارو کنه که بهش میاد
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78557" target="_blank">📅 15:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مسی و رونالدو جان جدتون زودتر خدافظی کنید فناتون مغز مارو گاییدن
هر سری یکیشون گل میزنه فناش مثل زامبیا تا یه ماه میوفتن تو گپو چنلا سوراخمون میکنن که ابر ستاره تاریخ فوتبال گل زد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78556" target="_blank">📅 15:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJgVA0gxluxbj1l6-6DoUX7Exz9pWrbHMzz6QZKI-fKOGnyOzEyc4uFtfbGBS7GjAJlCydSp-FXteHjHZM13e70ek_Gs4hGFOkZLfriKD8TDhX8VBb7g6AvwhmsvLksdv7VXcdJ9hB6QPcIeo_zzIavyE30WkKboWowXhL_EV3lyr55X3WCQ1G-_R-8SFt3MBsuFnPbKqIefr2GSC0vGmlpK9P_u4gXN87KpBhNg9If7tQx5HmPmIcReXFW67xsDBXHtB_EhGfEd2Nl-2vQCHvtFhWM5j9f0oSXsGUM3T8t7T4DJL149tljSKLyDgwuvJvM82LIYDTq3LyIKRBU6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78555" target="_blank">📅 14:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">من ک میدونم بانک هارو بگا دادن تا حواسارو از عروسی دختر شمخانی پرت کنن ولی نمیتونم ثابت کنم:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78554" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مثل اینکه اکثر بانک های کشور بگا رفتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78553" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آلوارز گفته از سبک بازی اتلتیکو خوشم نمیاد، اتلتیکو چی گفته باشه خوبه؟ گفته خب بیا برو آرسنال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78552" target="_blank">📅 12:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمید سحری عزیزم تو ویدیو هاش به کصشر ترین تیمای جام هم اشاره کرده ولی به ایران نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78551" target="_blank">📅 12:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwHVrYSD8GracGbA8z7D3pF82alWFBgE6KvgiH-LiCcdWX-8iSwiebg1utuDPHpX_oWUrUi3aIWNc6sbGvvhkIB9WHZuiA3MFnC1AsJW2I9gieJB5Vk7RRaGRdoat_n5tEcFLh9AxT1nlEAAXk8EiWY3Duvqc11bGGNWDAV6N_FMH1VO73ixvZW7k1vG6iX7MJ1pkd1CL1kfebWIQgkGM8nGapf7xiIZQ4jE_h3JAZYBh5ZzcN_YgvsXQOwCRNBHjUYr9V_4gDTFK2z2LnFaiNIP1Fdfh6aXq8MXuTRn6gwJONTZcS-PD00thi0HkJQG-s12dqWkbgEtQJrGwgsauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78550" target="_blank">📅 12:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ehc5uFF85238ZCGL9wL03FeAX7gqzt-_wOIRyxi0HZ_Lxdjv5KxAX1H_rBf0HWv_S5pJ0u_0XXu3e4S-8AeRBcM7WUx5wAw_GKT8TbeMY8hSyalvCoeaCCTKNi-xVCo7Z3R7sXngZ6ifedDHKZ2XMt0pfmyDgYGvwWFWFQTntVjFz91Zu4LAkOBJZIxmleakOg7wwbkriPeXAGiZFHAhNGE2X_MMBgia5mmAhqpubxGA6JCez4WUAfFtD2O2tdvI6G4j6-qpDi_HgIU7Z6JEcEKZHDoE5Wt9GW6ENFpctC4rd7Hl6eNt4lwBobP8QIEtS4Yg2dojznG_oFNrcvbsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان از ارث محروم میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78549" target="_blank">📅 11:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lex7ZBCaItm0y_nmeuud8bAwLKyxuxmkVGrJDU_wDPUFsdJtFPZJ3B9J7R7g1ldLYhhOWS9diW9n_Tvn8fS0t_jtShxsT41fY4gUpWpnbZDAjGh_3JB5SLX3HrKFQ9OgdhzedR9WgpPphRpL01FtaabYSm_qsoUL2O4va-bTAJ7o4TaKregcDkLtJ4sIuZzcI9805KvxHQzqHgswFsk1PKacA8QdBsNWCeoz0pdqSp0jQ3AIP3C8WXr08sd7Y6C0zkESecQpRnh8QKxqC67jv-2nPFx4--N75zsHqOlFtdQbyrQd4yuJPy4teMfFU5-DUzGVntArK1-r46_Ycaq-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ هالند: راستش بازی با فرانسه زیاد برام مهم نیست چی میشه؛ احتمالاً اونا ما رو میبرن و حتی احتمالاً قهرمان تورنمنت میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78548" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78547">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78547" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RElM0u1HljsZ3cYTfSULvIVjOx38muPVUH4BNVqXnG4TrDaU3FiTOs5HPKBtbEYDkIELOA7GbaonbLTwjZxc95uBn7mrs1hR8gVZyWTIDWs8MPoaXU7W6LTawXTQLuuoYZ2PQu4rrjNRKK5-wsq8zWDQb9vsOaNb71RpHaEfilLjseAeZWB8acrJ-RDjg1rFVfNMqzpQpoiZruVXPbrDEAVI7_Z60bguwGkQmO_A3QJtZr7ZLGJ0Ws8rK2G-sU4WJ3Z_Gc7So1a4WHo0vQlBL11nQGBGe0fm2bUYzg5YKnUwvQL9zHuZ6izM2c2qa3IFlGavA-5Bo78RBsL8BaGnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
R2
🅰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78546" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVb6RfD2scBHJKgEqyAetuLLm7v3myPUe2WOs_S6QPeI82FKV8uLUImASQJ81e7IhLoBRPmdue_Tf3bG3j50Gnd8jThN251l5GiLmSxziX2tloFlNR44uREgjpeHtu45tyi1RY7cfZoa3gkQKMwqyBuClF6xB9SJwKPu-7jPVdyA3PycR-vkkkopQaA85Fb5ScqXGN3lz16KUdH_CvScI5PfWY0GpVKNlN_JtkevaVdEjokmmGieh6LWXIgp8tkU9c9pvmLpTFOZB83-1VGsWOnL1oVeJo8KGX8goESliXWoZiPqB2WqFGIJa6G39ROMJi5iKp8UMAopqS7qT6Fw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این الان تو حالت طبیعی به وانتونز و ویناک گفت فید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78545" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78544" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78543">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkLJXWf-qFGSSaVTs6x1DPCJ-u6YHI-oiRxvlkJE-ClchFBqIAGJyNyCv5CMgE0O3O4Mr7GqThnfEKEjgAN7G-xeJJGtweA0hfyB_lJKFJGxTSq5wKuZZqlWn4HzcY50CpX-gRmskBDYKtSO3aY3JX7spxN9vdh40cLi1Og1hDaXzC53nLV43A8ny3K7PccDquC9hr_dKsLVX_XJz-T-7C16622V_AjpCkfjIHaGEm4Q0hoV-39EuLNaKypdku-OhErdv43-5Ieiw4I2EDysorB4vTIxvlRKfX7OyMeHZ-CYPHImB6Sik1voMc4_W52fyawESINxLlNHK3E6VANlAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون مسی رو ول کنید کصکشا مثلا بزرگتونه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78543" target="_blank">📅 10:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8HMeDnIsxWl34unBUhO3Mx0BP9IXV1gYn78lBUkporioGf4mCvfkagRyBxL7pERdmwTj9P3BYz15iJm3DXUo2v3ZEADxOEkckmuVLqvIROlo_vJnXhGMtRY5UnrFBpOH4FesDe9gobRmyZdZ-n8y4ae3Rd913pxs8NZv1dT5byoM51M7aEbMlmguI_iZapJ24fT3Od36hPOUKmfcE35eLb0iNY0AzoPIZjRXKy4V_Ff3D8SVkaRzPlDZf-E0tSRCaHnqE04Cj3-Iz4rnTUiAzgdkwDBJpT5P6WeBmFCchzn0d8z60w0jJmttf1nFP4bmS1KKEMpq8DnleWv_sFGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی رئال اولیسه رو بگیره کون بارسا تا چندسال پارس
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78542" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بعد اون همه کارزار گذاشتن و اعتراضات دانش‌آموزان پایه یازدهم و دوازدهم، آموزش پرورش امروز گفت حتی یک روز هم امتحانات نهایی رو عقب نمیندازیم و سر تایمش شروع می‌شه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78541" target="_blank">📅 10:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من تو کل زندگیم دو بار واقعا از ایرانی بودنم شرمگین شدم؛ یه بار بعد چک کردن کامنتای یوتیوب استاد فراستی یه بار هم بعد از آنالیز میزان ثبات روانی و نمودار ترسناک سقوط IQ ایرانی‌های عزیز ساکن لس‌آنجلس   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78540" target="_blank">📅 10:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef49ae44df.mp4?token=uLPENjBkdVqvqYj0iIQdlOz52tBdwLBxIGfua92OjqSj9-48iBkl0XVyF4Z08EU8lDl1sxkrJGQnd7ALg104oYx5LBIrw1BHVtd4LwxtXo3sY9trZy6WaP5JUZBsmwKbXrYmQZs9s4U6GQO_dFmTsamUuvm6-cwYORsWXC7mdfHvPR8eQKCKkLjnxyaY05-z6Ob8ezaO_cYHzOXL_esh52VJc0JE_uawi9-lVpSPLPqnqBwVKCNsOLZYhUPJbY017Ji80sckgXcG6NLtKV-aIBDGt32QCspCNJToWP_QpAjXlSxGuPIOsXLZLMGqgnVxl5aXvI3G6ObYLNwUUEV54Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef49ae44df.mp4?token=uLPENjBkdVqvqYj0iIQdlOz52tBdwLBxIGfua92OjqSj9-48iBkl0XVyF4Z08EU8lDl1sxkrJGQnd7ALg104oYx5LBIrw1BHVtd4LwxtXo3sY9trZy6WaP5JUZBsmwKbXrYmQZs9s4U6GQO_dFmTsamUuvm6-cwYORsWXC7mdfHvPR8eQKCKkLjnxyaY05-z6Ob8ezaO_cYHzOXL_esh52VJc0JE_uawi9-lVpSPLPqnqBwVKCNsOLZYhUPJbY017Ji80sckgXcG6NLtKV-aIBDGt32QCspCNJToWP_QpAjXlSxGuPIOsXLZLMGqgnVxl5aXvI3G6ObYLNwUUEV54Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تو کل زندگیم دو بار واقعا از ایرانی بودنم شرمگین شدم؛
یه بار بعد چک کردن کامنتای یوتیوب استاد فراستی
یه بار هم بعد از آنالیز میزان ثبات روانی و نمودار ترسناک سقوط IQ ایرانی‌های عزیز ساکن لس‌آنجلس
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78539" target="_blank">📅 09:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78538" target="_blank">📅 01:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=t0GcCdhufM7MIpSFSmnoP06fNbwxGa3Drdtnl7O7ZYCKuxuwgWzPW4iWPWNyr1eJCeMjLSZaUhNyLuGt0XIXBXaKkX0JVzXIoCC2wRGtOIOnscX3bFbpNpmBIMw1TEoPHTcHVyhyIGRIoOAvvfacYYm-pyVv9cGrF7WG7ultf1Xhf5wJsPzuoV0i2W7q522Gzqd2qrQT2HYScwsFS6oC1CLndHun8Hx5tDqk_zbxP3bvLkcQylVwrP0xXlmYS7sG5W_lpr3GEPKSTPv_7a-u1jMT3k0AkspSFlLMz0fHgT1m3Lo3UBfiTjTHS7THXaiOLfMA35QQ4B8RWKoYc6RmDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=t0GcCdhufM7MIpSFSmnoP06fNbwxGa3Drdtnl7O7ZYCKuxuwgWzPW4iWPWNyr1eJCeMjLSZaUhNyLuGt0XIXBXaKkX0JVzXIoCC2wRGtOIOnscX3bFbpNpmBIMw1TEoPHTcHVyhyIGRIoOAvvfacYYm-pyVv9cGrF7WG7ultf1Xhf5wJsPzuoV0i2W7q522Gzqd2qrQT2HYScwsFS6oC1CLndHun8Hx5tDqk_zbxP3bvLkcQylVwrP0xXlmYS7sG5W_lpr3GEPKSTPv_7a-u1jMT3k0AkspSFlLMz0fHgT1m3Lo3UBfiTjTHS7THXaiOLfMA35QQ4B8RWKoYc6RmDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78537" target="_blank">📅 01:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWc1L7yg3EZjxnzmHpsqZs25ZUNh2g-1jhEeZvMShxpHYOSwww3kylPbeqIU__hw2nDRb2dw0CjhIn0dhfELL3wH27ItEs2bt26VYBKh6iCjQdaj5pdfwoebXV6R_UMFzRkrcx24kbWyWy0ddjNBJiiDQ3Sqi47ka8pgw6MnWFqsCIP4UScbUoG3M_NCIwvtlsbBEYvyc4j5mnvgwgpiy_za9_qMFQPAVFDhqgKhmJ2q82UffPQVCitdmDm2IsfFKyTOLauZgUHi1wbVRe6mEFkvAZPJxOXmSJbilsYvOPDK7_M6i3Xm9AqvtEZmwzXYmqWI8P1WiuU6bPzT7nq-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان هشدار تخلیه برای تماشاگران ورزشگاه رو صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78536" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78535" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78534" target="_blank">📅 01:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آمریکا تمام تحریم های نفتی ایرانو به مدت ۶۰ روز برداشت و ایران تو این مدت میتونه به قیمت بازار آزاد نفت بفروشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78533" target="_blank">📅 01:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امباپه احتمال زیاد موقع پایان کریرش بهترین بازیکن تاریخ جام های جهانی باشه جلوتر از پله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78532" target="_blank">📅 00:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کصکشا اینارو من ۴ سال پیش دیدم، چیز جدید ارائه بدید</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78531" target="_blank">📅 00:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">امباپه چی زد خارکصده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78529" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwofZ_rHYYLuCZPvJQJ-oTG0D_BezYkYo3cBUlOC-ecZcx6pgMsUHvBUwK_1BvqcWrCfMbLed_Dw5Xa9X3agQk-X-d7s6TzZc3jVhy2M6gMc6QDlKeOQmYP18hldjahe3X3dTpsppLJ-TsEZZDMQ_m3RKqzSepJGM9TOLZs9SPBv2yE_GC1FCPeovsZXEemTdxoSTzHcMCC04evCC5-dLWWT0zljU4pNHmnidFR0MwYSJIIWbZGHECsB3it84N00eZScsVgO-_hbtE0YF9zL9X8DZ_7cLJXcDZsD5dA7_Xaaol1A7k8sCVfwIWMOz7TOJwIEIb7rHSwgMFgx1Ccn4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی جدی مجلس چهارماهه که کامل بسته‌ست تا کسی نباشه که جلوی باقرشاه و پزشکیان رو بگیره.
یه سری از نماینده‌ها هم علنی دارن صحبت از کودتا می‌کنن و برا یکشنبه آینده فراخوان دادن که برن جلو در مجلس، اگه باز شد که برن تو و اگر هم نشد همون تو خیابون جلسه برگزار کنن درمورد روند مذاکرات و جنگ و اینا تصمیم گیری کنن.
یه سری حرفای ضد و نقیض هم درمورد تصمیم نماینده ها برای استیضاح فوری عراقچی و حتی پزشکیان و باقرشاه وجود داره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78528" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دالگخیز:
پسفردا به ناتو اتک دادن کیرمم نیس چون زمانی که ما به ایران حمله کردیم کیرشونم نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78527" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427abb0164.mp4?token=bthEk3TKbA9cYJNJ1XikhjgIVmYQdJq_Pcm3qxm1T5bnewuXS6-pAODDNU5J79jZ46sRfmY2gul-bFmTyWP2tW4a9NVyUqUPJywonWtoQhlOwNbUVCeKzcjqnnYS__I4-uHN8pCto2hztAvOb1OIKLtDjIuNK7a9Awu0Xt_48EcpmRST1bjb4GhgXQO5mduEh15oGNGS-DtysVgPuyc8kAAX0GKnaNvv7GZal85bCpdYnFdJgmMsqg9yrpD_kS9iOhV_VvjUNMw2DwiUi5LVXlfggmZCWAweXU1Idfcrw1Dv9JFS60zCwAxSS3AgT8coqb_brbTRezRKL-uQYNjT7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427abb0164.mp4?token=bthEk3TKbA9cYJNJ1XikhjgIVmYQdJq_Pcm3qxm1T5bnewuXS6-pAODDNU5J79jZ46sRfmY2gul-bFmTyWP2tW4a9NVyUqUPJywonWtoQhlOwNbUVCeKzcjqnnYS__I4-uHN8pCto2hztAvOb1OIKLtDjIuNK7a9Awu0Xt_48EcpmRST1bjb4GhgXQO5mduEh15oGNGS-DtysVgPuyc8kAAX0GKnaNvv7GZal85bCpdYnFdJgmMsqg9yrpD_kS9iOhV_VvjUNMw2DwiUi5LVXlfggmZCWAweXU1Idfcrw1Dv9JFS60zCwAxSS3AgT8coqb_brbTRezRKL-uQYNjT7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویناکیا چیه دیگه کیرم دهنت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78526" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگه این جمهوری اسلامیه از آمریکا مواد غذایی میگیره میده دست بابک زنجانی که صادر کنه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78525" target="_blank">📅 23:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ: دارایی‌های آزاد شده نزد ایران برای خرید مواد غذایی از کشاورزان ما استفاده خواهد شد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78524" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قالیباف: توافق برای آزادسازی ۱۲ میلیارد دلار نهایی شده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78523" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قالیباف: توافق برای آزادسازی ۱۲ میلیارد دلار نهایی شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78522" target="_blank">📅 23:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پسرا رو برد فرانسه میبندن مردا رو برد مساوی عراق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78521" target="_blank">📅 23:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAbtl4_YbVKJq1oSVQ6l3XMz6zwBr03-TGUXcW_K3P7_4F1f6fQRh0EeTjzTRjy2-qAoxBb8y81BWViCsV48M9Un8hBqV7q-4-GIogH-BUSpmcJFlYUEWjPHpGVlsa2toUXbOPvYxh-JlpJo5GZ5hYF-4msGS3twXtuZvCybuPjNAyH1JvqgklbSaiaYjGIKtZaaqWsE9IWEw9dVIfyAAR3tECeeIqaIISddhb5tJq5NzOobCacTrkdFoo9v0jmg1bmk6v2Osefhlj1eAxUFocPeUvoewYU-uQ-yryTxscFSOowxhax5ux-IGCVWpV3JFk7dut9tH7mZISMhE24LPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب رسمی فرانسه واس بازی امشب
اگه ببرن میرن مرحله بعدی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78520" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تا الان صعود این تیما به مرحله بعدی قطعی شده:
آلمان، امریکا، ژنرال، مکزیک، النصر، آرژانتین.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78519" target="_blank">📅 23:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0lPt4XE_TKok8g24DVvu4t-yFmWpyLWah2O3sGkHhxjHYB6VCqHFsdQVeXmU7wiU_IkQuaHnn-Qz9gNeS79eu4GQCMcnlbKtalNmSgzZa4rfq592cswSMIp5G3iz1NoPUqzQ3FtLQB1v54iruyAzhJGK6z9-0I4sACmI_nnP4l9OxEr0Iz6wvNDMuODxJG4wkQVZW6PZEFFoACfXrgIMw9cf5ALOoWMAATDoUR8jdXug_DlEWk1GmX_O432IyAk-osH7nUkAIfSW3RBURQXBIJb3yifURi8ipXLbFvvljybaVfXsDvsx06iG6CpL8MPXlfjjw8D1GwjrNnBxxSwtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wx2RzqnNKHXJNliK5sTRgQmD1uF0Hht0YyHAyI52_l1AXOqYZJiJlefMnFkSJprVpxFw4dYpRXX0gbSqTk4gHRoo9oB3vXyY8D_YLSl2Wbn8u5IJz91pK-xR3Iut7UhOst3H5AKLlwRpxs2kUzQ6Vp0LXZxbvYP0fTllU4iF59VgqTGqbXgB1gnnHNQj23xCDUMjFos3jVtdFSFGbVvXHCs1T6bldhBE6cjRN-NVqyOA1iVpkH-TUm1f4KaNRmoJm1tKnnIkCkHPDkRizcegvY0-TVID0-Gs5fWBcChNELcvkgg2iaXv34SdBiNzHJ_vCLp2IhJVju_ViEFVbi9Nxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78517" target="_blank">📅 23:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خداوندا سپاسگزارم در دوره ای زندگی میکنیم که سعادت دیدن بازی اسطوره بی چون و چرای ورزش جهان را داریم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78514" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رونالدو فقط و فقط ۹ تا گل فاصله داره تا آقای گل جام های جهانی بشه</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78509" target="_blank">📅 21:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">متاسفانه نیمه اول تموم شد و قراره به مدت ۱۵ دقیقه از تماشای بازی خداوند اصلی فوتبال محروم بشیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78508" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOVnwta2S2PhKD2qekcL6aQVd1FnQvqzIosWJ44gqtFNGIz-LU8hWj4uoFi_GMCx04RKsjLjN5pepoDGodyIQ9bEiXZ711KLlqO35IObj6bcgU4ki6B3yCDATUCKGnmkKdnEQnsP0t4Z4Bem4u8g99sg4CCtBULxmk9X5-OcyoDplR4jbJZEHXLtYvHerTkc479NDMNs6w9yoBHqpEoLLlQ7PHNXw-FHsWWdPb7cdUL1SbFmLiwg1vj-DjSJj1NHcDPQRTYoG6f8RQ10AUb_sGG1frNwgykrMTGFRndhrMFoYquU4NYFyQO9Zwcgw7a-C8BtKPpmjHaK9PszF5PKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78507" target="_blank">📅 21:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78506">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bO1atWWeJsTDNqspdLXKrdz7l7HWbfKZw6ySmTB0XdNy0uGKNn5AQ5vGBO8VNj5rnEH1Hd1IqEIyBRpmlmp935gdtupuvuSYBF5c9Fu6s41i5ny-QPStxuzn5x2x-g608XXIHFC0k-Cv29klJKZ9gcdLTSYy0YuPCjEq7E777QR3W73ygM7UyHhmXr8VJnmj-HIecMPY334cEzqfWYwjQuxNzRgmPgwsm4b9rfHS1fFBJR6vB_g0w6nteu5I851jD0WTzTS10GuZcaSt2RRpvw8Qm7mTdebzzbpVKRoA1Cua8pLD_8f3xVzsjKAx4VpaGCk9SodAixP3qkUnfdPrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78506" target="_blank">📅 21:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رکورد کلوزه شکسته شد
سر تعظیم فرود میاوریم به احترام لیونل آندرس مسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78505" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78500">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رونالدو اینو میرید رسانه ها عزیزاشو میگاییدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78500" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پشمام
چی گرفت بیرانوند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78498" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وقتشه پرتغال یه ستاره بزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78497" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نویسنده کتاب تاریخ فوتبال اوانس داد و پنالتی رو زد بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78496" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jjxH3ElZzkqLjDqAKLU5YizR7SvzMET4wSjZkAK9o7JxuvIb68Gj-32sueXXtAu8-VVbKsg4mb_wNkHvdZ9WLKQn3kck0t_MJH99UeOjQSDNAKw46hLyLo4CTgbYygTDO8QVGmCTKcTNGG7SLbJatb1uAPyvaPDgIpnpqwyFEWfqmPgxfhjAZsaf2mxT0AgHvHnlLNHFYAfHz3jRJnFs9hkXF4CuHXlUm7xuOXHY5xAtRjYogWmxle34YydDJyOCUy_6HYNT-4IKiOClNgJLmksLmuXf0ZF_ra901ydI3lB50OJ_lMa7eAZ-4vOcHgc8lkIavDqdKJ9desng0Ey8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پیام رو نخونید!
نماینده رباط کریم رسما درخواست فیلترینگ میم الاسکی را به کمیته مربوطه ارسال کرد!
میم الاسکی با سابقه 4 سال بزرگترین چنل میم بودن بهترین پست های کل تلگرامو جارو میکنه و با ذکر منبع میزنه چنلش و باعث شده مجلس از دستش فشاری شه!
جهت حمایت ازش جوین شید:
@meme_ol_ski</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78493" target="_blank">📅 20:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چیزی به بازی پروردگار فوتبال جهان، حضرت لیونل مسی نمونده
به امید درخشش برترین بازیکن تاریخ
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78492" target="_blank">📅 20:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=kKgF9wGf-8bOLGZnPl_gMiEi_pY1zZKm3hg2SeQvbQZ58GpqecDfXAK56xabnUdGg_loMVyXNo1auP2dhqfPNz-2HTOQPC1WKG0AiuPm7SFT9uY-nON-rf8PZK9I9AdllZ7h-O33BR3UuBan7iCiDYgg_64vT-IERub8CFnGsMUGiSCiXbcOP9f8QjLIZg2b905KOJKG5VD-HA1xrRlP5NMUo82w8W845aUQP8G9VjMQfhr5dhv-eCKu33lxCQRlDp_6d2mrAcgNNsWBiMPJxvEIzcPmxt-M5w4y3Tq9pJpLl68Oj22SlNtdEdIKOTx20-blSr7Puiws_m2Ej8neIng4ZUNPU0j5tv5wQPqH4aD8gNGEtuWuRC-rWQweS4HRlML2f8f5ZpwRItiNn5WJ-OcTDnrPmR0qgicHoRbl67LUKO-MFClq8YsA-7oEDfDA19bbdqflat8h0fKiQ--qFWEC29qmV-P1Nzp-gSP84j66ehTCel2uzJSgJjMgvo6j2G74bTXZLQ-hvMBpBWL5zVZlwcBB1l7rixcRyYCZe-xsjbJtVJZa8Oor7DtecGCl72O2oTJ71fH4rJwKisYv-lpn72XraOs3lZr3FPTiV1RH3uMYZgqo6sI77xJCEzUL6JmM6EymnPc8VuxyoSSj9tpPqsU3kqeQI7_ZyyqDdes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=kKgF9wGf-8bOLGZnPl_gMiEi_pY1zZKm3hg2SeQvbQZ58GpqecDfXAK56xabnUdGg_loMVyXNo1auP2dhqfPNz-2HTOQPC1WKG0AiuPm7SFT9uY-nON-rf8PZK9I9AdllZ7h-O33BR3UuBan7iCiDYgg_64vT-IERub8CFnGsMUGiSCiXbcOP9f8QjLIZg2b905KOJKG5VD-HA1xrRlP5NMUo82w8W845aUQP8G9VjMQfhr5dhv-eCKu33lxCQRlDp_6d2mrAcgNNsWBiMPJxvEIzcPmxt-M5w4y3Tq9pJpLl68Oj22SlNtdEdIKOTx20-blSr7Puiws_m2Ej8neIng4ZUNPU0j5tv5wQPqH4aD8gNGEtuWuRC-rWQweS4HRlML2f8f5ZpwRItiNn5WJ-OcTDnrPmR0qgicHoRbl67LUKO-MFClq8YsA-7oEDfDA19bbdqflat8h0fKiQ--qFWEC29qmV-P1Nzp-gSP84j66ehTCel2uzJSgJjMgvo6j2G74bTXZLQ-hvMBpBWL5zVZlwcBB1l7rixcRyYCZe-xsjbJtVJZa8Oor7DtecGCl72O2oTJ71fH4rJwKisYv-lpn72XraOs3lZr3FPTiV1RH3uMYZgqo6sI77xJCEzUL6JmM6EymnPc8VuxyoSSj9tpPqsU3kqeQI7_ZyyqDdes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس علوم غریبه و جادوگری در شبکه ۱۴ اسرائیل:
دلیل اینکه یهو رفتارای ترامپ ۱۸۰ تغییر کرده اینه که ایرانیا با استفاده از یه سلاح الکترومغناطیسی با فرکانس پایین که توسط ایران و روسیه و کره شمالی ساخته شده، مغز ترامپ رو دستکاری کردن و این افکار مذاکره و امتیاز زیاد دادن و اینا رو تو ذهنش کاشتن؛
از منم خواسته شده که مغز نداشته‌ی ترامپ رو به حالت عادی برگردونم، منم دارم تمام تلاشم رو می‌کنم خواهیم دید چه خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78491" target="_blank">📅 20:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ایموند داداش این چه کاری بود کردی</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78490" target="_blank">📅 20:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjJ1lItcT0CQMc7oWCp_uUclUZAyDMaCpuNjhrqqg6iEHk13-ZwBdUaYdokTNRUQNtXaxqlPMNvty_Cx0Yo6Dxu3bg3ZNIX_c9ZS9Vg23QiBT-eLedJxzN02dYJ4T9cK_F0U6fcdidVpDw1_EXZQqB7dNgg7t-sVXo8MruREllN0PMjrxITfcWW09hzlELF8f_MDH1Uq0OFVTbGOJgGJAZKREzlPOP7OccJbDPW35aYg_DozNgd9bawZAmX1VCbsK1xZ8KMy_lZWslLCFqCjeM3bb63oXCRz1D22J3Y0CPHi_WNC7Us5KTAmuhn_AEIVDf3uTZWTNBzsqvSxv5RF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد سوارز جوان شد
بازیکن جدید لینک شده به بارسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78489" target="_blank">📅 18:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فدایی به هرکسی دیس داد طرف بعدش چرا زنشو طلاق داد, اون از هیچکس اینم از حصین.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78488" target="_blank">📅 18:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فدایی به هرکسی دیس داد طرف بعدش چرا زنشو طلاق داد, اون از هیچکس اینم از حصین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78487" target="_blank">📅 18:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حصین زنشو طلاق داد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78486" target="_blank">📅 18:46 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
