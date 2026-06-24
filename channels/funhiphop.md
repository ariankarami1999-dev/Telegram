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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 09:59:19</div>
<hr>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">و تمام
انگلیس موفق شد غنای آماده کارلوس کیروش رو متوقف کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/funhiphop/78638" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">توخل از سبک بازی کیروش کلش کیری شده</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/funhiphop/78636" target="_blank">📅 01:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بزرگ‌ترین اشتباه تاریخ فدراسیون فوتبال ایران قطع همکاری با کیروش بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78634" target="_blank">📅 00:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETPN8DH6cVgyeEZZYM-iYaydmj-kPef5AczDTSEeDvOgfigKR-pQX9ecoTcgsmj4XgGp4T3AXYkswAd0z0UjH9dP70mTa4ihxZPfSH74J9OEkMhLYRH9Lme4a0GJl-pu51wuj4kXUt7REd4AvEXp4bynQJkG2ZWbRqIDUswSarvywIXxrCwemHOlk3Cp5I4Z2PGfr7upL2DCX19CAMzMQX0FH5nFaKKXZYutJof-i5njXYFJwwvbB2B_uIMOf0ziwo10KIlDx2ix4dhakge8SZ10BsJqKnapWdUi_9HqxR3qBmUs19poBsejSjAPxb-mGGP384PooQsR6zlkxQsPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد ۳۹ سالگی بزرگ‌ترین، بهترین و با ابهت ترین بازیکن تاریخ فوتبال هست
مردی که با وجود خودش به فوتبال شخصیت و اعتبار داد
تولد لیونل آندرس مسی بر‌تمامی فوتبال دوستان عزیز مبارک باد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78633" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کیروش عجب تیم سفتی ساخته دمش گرم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78632" target="_blank">📅 23:54 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78631" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">واقعا افتخاری که تیم ملی نروژ به اصالت و تاریخشون میکنن رو میبینم حسودیم میشه بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78630" target="_blank">📅 22:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این سری کیروش کمتر از ۶ تا گل از انگلیس میخوره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78629" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شانس اصلی رو پرسپولیس آورد که کاناوارو به اورونوف بازی نداد وگرنه درجا تمام تیم های بزرگ دنیا مشتریش میشدن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78628" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بازی تموم شد مبارک رونالدو فنا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78627" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پرتغال امروز با پرتغال مقابل کنگو 180 درجه فرق داره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78626" target="_blank">📅 22:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خوسانوف از کنعانی و شجاع  هم کیری تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78625" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faixXVY6Fso_pJh9dL9Pa9im2aJNVayV04L2ocAKLPSKA6Wd-ZHZzyEIJ3n-j0RNFp4sKSXswC663jPE4E78N8oSC880xRGuSYDZG1Gkj_onuvxnzsMvIABVfDT7WDkwJXByBpPBVSH37NEHIQ6gQnjInikJvUXB0cSEdodJADBJ8_fD5JXksk1GadsDeukb7rIpuFxoAERb3fcjCLgtJU9fdSfBy_NexToj9LDx8cehVELB_IRNsOe93yyNTbZJ3xyAorMHLTAQj6v0le93OYkTBXUJe5kwY4Nrm8ymU6l7iUU1F8zPYhUJiuMkB_9Liw9dOcfAoDu-tv2SscpvQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مسعود دکترای افتخاری دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78615" target="_blank">📅 21:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3t81DvEGuH_iU4Oogc-Y4WGhcMYmR9OniRq11Q00xfUuCe34yTigjw3cBwgA4NFL-C0XE0hc7_Xu08J8F4RPKrewNmzAl92aHAFy6b9dQqRoMfGyycq2Y4YTc6344iD5mfRaUAmDjfeEwY1AyZJv4Z5nskJFiNhsaEAoIK7LxQG_qBlGEgBiF293za8rgEAOaSMfI-kZ3LmiD3axHJxCzBvLCABtE-7QHuWXkSkyhNTv8dnRPG9bOTSK1aNMlq7Tmf6y5sTcZLF0n5IhXLQ5KVAC9cKUxNWE2WuSKEsMO-U1HuzENMU5zQmjCa6wP4lygdNIpP5PsRa3klAt7mZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو بعد گلش سایز کیر ترامپ رو نشون داد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78596" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امشب تعداد گل های کریس تو جام جهانی دو رقمی میشه؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78595" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCbapY9jeNyXAglDhQTvmySWq80AAmEwVnfE14wEDUGVgYU_6dbfN2Xwb7Wqo2h_4iEd77FgbQTtyztrXI8CwPGa_ow8WxKYAaLXfVsqiSD02bbIB_7A6mJ7i5JqfsJjVIDiTuxCoqlM_pbO_qhcPlMS0aUCKVnZECGQKpkBEIlNAagKkwSp48Ek1S0g7Q1tLmL6XjJxByY2_C21mOEUxVDAwk1M4INj6e7ZYhRPelkUIK7CXSAB4nlud7WZTmwBelKq5vWWN4daB9lZoremLyxElr-up6bUUt9oHGSoAJUB0d6Q6WWYEeZhFs3WxTgVoH2wnExf7b9eykg12ENhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نوسو بغل کرد
😂</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78589" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78588" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره  بماند به یادگار  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78587" target="_blank">📅 19:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسپویل:
رونالدو امشب با پنالتی گل میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78586" target="_blank">📅 19:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78585" target="_blank">📅 19:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWCvjSmxTDfewbAj7eKgoDI0cbdyV_NIagsRquDRfefSyaYaaFRV5Hd-31JclTuIkuWK_5_a3k6Edz2379oYdj06cgTllxlsfI297nLfJa8GKh0HCA7LHlNyVhdIMxV3ibVV-Z1OrB2oYR0-dqVYi0PHMCEtuNNAEzrEJfPZ6WH2LpP0JrEe-clzuVQ_Ip0vIOWaOKz-lGs9o5IoDZJQzSG9hIBREo3mWaWZCtnIMl2ZujS_VytdkfzrxRWqyJffV8EpBAO1i0CmKBnI5yZckeVLghQ0p2aH4UDzHurk-1rn_LTjJN46KgerXCvQBCml9yvhM41tPf4LF0AVK-KN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jj7e9whDb2uBAhqXHMu6SKXS0XdpmrGMTFb57dgHf_QJ3_sxVh8JQgbm3rg2dbFImtEJW5oVZP4wG1ehJpOLBo4j7oFZggudlCDexu6GVei0vA1s8nL84Be31o38ybUyCWYxg-X01kPxHpLoh-YtRzYxwSIKVMI0W2u9gk782V3A6SQgD864FfK-kI9961P-C5xbH_uz1srgJ1j51NXY37sd6xLwjYjBQ_Je5YAM_T31hQmFmXmBDSYxyfV2tYvu4_PyDqLzoGfmaaTn2OhEr83328lmkJhiilDf9KumqSBV6Ri21kV3VFOXKTCF5wzCfbDU9NDZxoZs2jXEeF279g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب پرتغال و ازبکستان برای بازی امشب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78583" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=R5cL6tuarIvFIj1NIbvuFZ7KFBe-ImFoZLuG9_oc-IJGRUUEtGEfu4g91ZeSgM2iHiDrqMD8AoJZQuHpvEWY9lba4U1pjBq2u01-1kGOOGYZAEPEL2aDadt0NGrz7ZnAZ5CNUEjZ9rvccLqJPdZnn_jH1F6318NaLIhoIV15uk-j4f07W8mab6ffniVOIX_iA3EMZzxi7b10VcyW1KkdQ-uq73WJh1tf8iX6p8IUoojceVowVhhByBp_JUvJGLpKIEGgPjGoBA2dZ5lLRqtE8eS3loOA721ubrRFNyywyEm4vBPo5cQsms_M-8Hq6aWivJsbbYXLE1NbnJLJ5AvuvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=R5cL6tuarIvFIj1NIbvuFZ7KFBe-ImFoZLuG9_oc-IJGRUUEtGEfu4g91ZeSgM2iHiDrqMD8AoJZQuHpvEWY9lba4U1pjBq2u01-1kGOOGYZAEPEL2aDadt0NGrz7ZnAZ5CNUEjZ9rvccLqJPdZnn_jH1F6318NaLIhoIV15uk-j4f07W8mab6ffniVOIX_iA3EMZzxi7b10VcyW1KkdQ-uq73WJh1tf8iX6p8IUoojceVowVhhByBp_JUvJGLpKIEGgPjGoBA2dZ5lLRqtE8eS3loOA721ubrRFNyywyEm4vBPo5cQsms_M-8Hq6aWivJsbbYXLE1NbnJLJ5AvuvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سریالی که دکی قبل نوشتن ترک نگاه کرده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78582" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78579">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfWLxMODjacku8Ui20lw3t2ShejgCo6-pmU2UhMPjVwe1qttIOd9O9iKUysU9_B8sHTvs-oyRAvpGpUlHn4mikuUHo9mKp8DFxoKgMVMNBlfQfyzjFhz_q1YdlBOGmi22sXZ8NbPRgg-WmMj0gLFDgP_2cwdQfNGobFmgYWb3pJ6lokKAmO9XrwmgjFCwg00xhFhRmHUKlfsX3wo9zHTTbZuJ_ZpnUkXVh3e9RzKjiWRBfCe-nzFomFIxmtWxKXJ-l3nB3-o8MnJDWhNA90qoAv5SLJctdS54noxuovE05NWqMrZ6CpL5OR4yB66kSGTsKeFMXIRo_B8ITlXpKfARw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78579" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR2kUV8PdPwo-sK61EJhn2uxtK7A6CDylq_tXpnbgHSn3lTvDvoLKWwh8AQsH1wtzZVJ0WQARlOdHxbkoB9S3CjkLfb9t6G2dUSldXf83YgREl2SKLMGKxFuu_3A44jfNPprf46p1eMkmUjpgYPh5AdD_jihZK13t1iEmP7TBX-Npqg3NzmNq1pHSMjYj07tLpkFOQwuDXqHSaLmkiuQsDAc4ZOLBXsCYA0mAMOwhYFKK5MTsfhjxXvyEVUmxsFbKgXXzFn0lMPdfnAEBId63BRI1JFuzZ_0-zNviJcn4qo2ZtgA3TTMJkMAjXz5N22okD_nmDzNaMMOL41mbDZtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیت دانیال اصلی و مهراد جم بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78578" target="_blank">📅 18:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqNpRVzBF8teugXdg6ei1iT--tbXoZs5BbWUFE7WiptRq8Fx2gYp3ecBkXAoXtSf_524AOdNsHRaMA5x5Qj2PZwTc0I7f-_24QwFxGFYxd8Moj81NiWNQQoVByz32AmRIuZjXLBtiTJWgoWFdIzvzCaWyR7XIehtho6Axy5aPT_rAro6SA8s-kGgCj_FHOudD5UmSE3FtCK4XvbLlXgZytPg7Tz-UDfZcBoohZMP5IpR7jHz5hPC3OQcpa_fxMorNzaAvYXjUO4ZMcN2TmcmPWFSWZ6-Sw9wCw3fYF7At8U7Rz62yKzaxjRiYX1fZSmtVecb1u0SyZjGcLkbrOYcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که سپاه قراره با غلات بکنه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78577" target="_blank">📅 17:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حرومزاده این همه ناله کردی که آه ۴ ماهه زنمو ندیدم تروخدا زنمو بهم بدید دارم می‌میرم که در نهایت ببینیش این کصشعرا رو راجع بهش بگی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78576" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فک کنم پدر زن دکی پوریه، وگرنه هیچ توجیه دیگه ای نداره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78575" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78574">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78574" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ PlaylistShip ]</strong></div>
<div class="tg-text">فقط اون بدبختایی که فک کردن لاوه فور زدن برا زیداشون</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78573" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78572">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خجالت نکش داداش از سکستون فیلم بگیر بعنوان موزیک ویدیو اپلود کن یوتوب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78572" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دکی: صدبار تو اون خونه کردمت، جای بد نرو جون جدت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78571" target="_blank">📅 17:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دکی: مثل بابات عاقلی مثل مامانت کص
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78570" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78569">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اونجا که میگه چسبوندمت به دیوار با صدف بود یا مامانش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78569" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza𓆃</strong></div>
<div class="tg-text">دکی وسط سکس نمیتونه چیزی بگه چون پای صدف دهنشه</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78568" target="_blank">📅 17:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فکر این که دکی وسط سکس به صدف میگه مادرتو گاییدم داره مغزمو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78567" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8qVhFVNrp07JfXpNG4V3hFY_bnRKtDYpJa9g9kN9Opmvkqq0MO7DZAoe6BOX68no69TYdCu28uzHyZ_AWJRG3VHN2m7lYIAFCb-DXC8nTf5mkFCykvPRVfv36Rtwf_VFrqRWt-1Yt6gDwB3qbBKcBqKcVboldAp9EfGcomG9lvqELabAjUgo7Rv9Euy1XiOfTGXMIs9CnvFlnd7xE3DWr-mMb5nJcsq38Nk9HedXobHanFqF_YtEdHCbDwzfVmFSWQgq-aKBlELAEmHIVCkP3M2rOwfsVGoRjzBqTA5USLQDC42ZJQG5EHCKoJBhWXKoiz94_zkDYXltPXovOx5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbB4gukqBz3hf75XI730WPdgEWQP9tlOZgzmou6Yp0o_hBwkTsr4AAolzUh4hjPmzbxrf2vSLdv96jgfI6MuYAFfA9RDtmUQ3d8txwc-PcJ7GWXScn_SMCH8uT_Q0-0UvsJCSEhIIitmnW0mxNJzCax0pEFHC_3Tw0xggIqxlX_zonKRQy7UmIfwr2zaciEEg-DXua-R08URG8-4dWUmEWNogZ3OBA72HRg26msINSunXQ55WNS28h_I9ZYLRUHXuuUurDubGil2RfXT7o2BNc9r20a67O9xw-9NK0O5-ZwQGozyarAEpyHiWSVKPjFfFN7HH1L2MLzp-1HtIv1bUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78565" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbtsvCJmqC127XV-1gpKhtpT5oP9Z3nAOlh_7jZDo9mcqWfjxSNBXQskhCQHZ5UgVXZNqjodGTBAbAdqflK4VKb2wZcPiQbL-iK1oWhS6j8hh4FxkTLyBsgfxZFTQmYz3FOzQat2dOUYHzGgh7y8NvbjeE7qCOvwKRJccka8H4yvtV0q_egfDKjQYlelc6ZpwefKIDeIJQR3pmgzArSer8Sd0bCMJNxDqTOq8PG376Ghg9xzRwO8m3ciXVIYX_X88TWpRfv2jFwgBBa6RYsm9NDF1CHhjnVeYZQIuLOk8FxFfCCkKR3_9BlitDgs_CTY9rkTIHay1lI1lwk-Pc8koA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.
Youtube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78564" target="_blank">📅 17:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78563">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کونی رو ترک عاشقانه این چه اسمیه گذاشتی</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78563" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دکی کونی موقع ماشین شستن من چه وقت ترک دادنه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78562" target="_blank">📅 17:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78561">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تنها چیزی که اَ بابام میخوام عشقه فقط
من برا بابام قیمه میبرم من من عرضشو دارم
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78561" target="_blank">📅 16:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQjLi2yrMyhOv0MIRhPnbEF5Eb-E_oz8f23TDGZR4NV3uBADTNs4AOgxbXR0Ygmo9vFEB1w0WO50VXR1tIwPchqaa7slvVp7Ma89akfxUii68mc33WGV17J_OoG7sx_5iksvrvgtQwBG7h_x2ThBrCOn9HyZMWsMAGNc2D1uvJ76QzIepGHl_kvE8W7YyCa8dZ3nYmlQav0rHJFVly0_iHF87sWYZvdPOCzh0rfJWqdtBmV6xG4aYfeKWmEp4PODaFHXho8FSRRI618lK64rXSOoP0TlMRcIHA-fivuzagV5BJnmVA-Py0zLdhn2XQ9OkkcKZRuug3jU7aWM4D_a2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو رسانه‌های آمریکا به جز فاکس‌نیوز کلا یدونه نیویورک پست برا ترامپ مونده بود که اونم کیرشو کرد دهن ترامپ و توافقش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78560" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLeJizSxsxMi99J45ZGX4mJ7mmqUUswFm8LEjIx9dXCr2qutxOnmCeO8V3o4T8AEKxc4QSc7Zs6DhaoAsGe5oyuImk_xrkrX1Cjk8HgKentlBF7InPkBV5wOf7W08zAgoIXLHXVbt_L2Y5UBrifN4vRWw4UxY4uBeyorpITnFkMy4cu3pDrpM5Xgw5Mtru9LuUVrZcv2w-4DQan6giew8OWdz9mIT-rvHj8ULNazQnvTJn_CfkVA8sXLB3JvHi2W82b7ULCuD0iNIg2exAw0Z4RuGBF6-5tIZn8TNhpFFxhVmBGgB_WURCApQ4GQNrlWwMyJgTvFxLOnQG22Xvw3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا با دست مسعود روی شهبازو کاری ندارم
چتر چی میگه اونجا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78559" target="_blank">📅 15:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78558">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پزشکندر و عراقچی رسیدن اسلام آباد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78558" target="_blank">📅 15:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">علی گرامی بخدا خصومت شخصی باهات ندارم به عنوان یه شخص بی طرف دارم میگم، یه آدم رندومو تو خیابون نگه دارم بگم بیا رو این بیت رپ بخون از تو بهتر میخونه، روی این مسئله شرط میبندم، پس لطفا فاز نقش اصلی سریالو تو یکی نگیر بزار یه نفر این کارو کنه که بهش میاد
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78557" target="_blank">📅 15:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مسی و رونالدو جان جدتون زودتر خدافظی کنید فناتون مغز مارو گاییدن
هر سری یکیشون گل میزنه فناش مثل زامبیا تا یه ماه میوفتن تو گپو چنلا سوراخمون میکنن که ابر ستاره تاریخ فوتبال گل زد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78556" target="_blank">📅 15:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJgVA0gxluxbj1l6-6DoUX7Exz9pWrbHMzz6QZKI-fKOGnyOzEyc4uFtfbGBS7GjAJlCydSp-FXteHjHZM13e70ek_Gs4hGFOkZLfriKD8TDhX8VBb7g6AvwhmsvLksdv7VXcdJ9hB6QPcIeo_zzIavyE30WkKboWowXhL_EV3lyr55X3WCQ1G-_R-8SFt3MBsuFnPbKqIefr2GSC0vGmlpK9P_u4gXN87KpBhNg9If7tQx5HmPmIcReXFW67xsDBXHtB_EhGfEd2Nl-2vQCHvtFhWM5j9f0oSXsGUM3T8t7T4DJL149tljSKLyDgwuvJvM82LIYDTq3LyIKRBU6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78555" target="_blank">📅 14:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">من ک میدونم بانک هارو بگا دادن تا حواسارو از عروسی دختر شمخانی پرت کنن ولی نمیتونم ثابت کنم:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78554" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مثل اینکه اکثر بانک های کشور بگا رفتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78553" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آلوارز گفته از سبک بازی اتلتیکو خوشم نمیاد، اتلتیکو چی گفته باشه خوبه؟ گفته خب بیا برو آرسنال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78552" target="_blank">📅 12:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمید سحری عزیزم تو ویدیو هاش به کصشر ترین تیمای جام هم اشاره کرده ولی به ایران نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78551" target="_blank">📅 12:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMuKNfeQvK5cS5DlcMFPoquG3GXUe23uEN6VFZPLd3QoQr22ZI9iBnB6VTsfZJ6nF73gDsuHxP3KU6aoIDx_nZ0PJbC4F4xfHLjcri8PHu1gAOZPEVFM5xsFCvwk7g8hvpW4UAzG5ePvHQ9LqcvNu41YBliKApsKCs4BfIBhiozrpwwgcpO7-HryOY0Uz-Zv8XKH8w31ts1ebfstRHFNkREjGqNOCEUMuTjdYj_XVpM3ymBa8lSHKMhb3jvJgzS7Ah5A78jJpOtDOq47kLwNW5IqRhIDimmHMbZINQcQNyOlrK3ocbqoQrRKHKPssNonAw20-A2DtC_9p7mjOwUc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78550" target="_blank">📅 12:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ehc5uFF85238ZCGL9wL03FeAX7gqzt-_wOIRyxi0HZ_Lxdjv5KxAX1H_rBf0HWv_S5pJ0u_0XXu3e4S-8AeRBcM7WUx5wAw_GKT8TbeMY8hSyalvCoeaCCTKNi-xVCo7Z3R7sXngZ6ifedDHKZ2XMt0pfmyDgYGvwWFWFQTntVjFz91Zu4LAkOBJZIxmleakOg7wwbkriPeXAGiZFHAhNGE2X_MMBgia5mmAhqpubxGA6JCez4WUAfFtD2O2tdvI6G4j6-qpDi_HgIU7Z6JEcEKZHDoE5Wt9GW6ENFpctC4rd7Hl6eNt4lwBobP8QIEtS4Yg2dojznG_oFNrcvbsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان از ارث محروم میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78549" target="_blank">📅 11:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Oum15ZAGEN3LZ_UjyByzj7xyoxZurEsVA6-xf4YH7rB1IryYiFSAsjt_xLZcOGPIpVlhnTksPUI77AsvZcWFZJFrT1OJ66Rd3_-kjyJSGYX3IgOcK4wq4ZTJ1P5wK5ZPlTiBU3BWnXx_lhBPgPWDTLgkzcSqbE-rlylzO4YiecuKp1yDawgfJzixQ2ktKxpkp2_KFrasWrDuC1dkRZ4lHD8qAzLUMIeE3VHvoQ5z7-xi4TFV8MVw8VJWDpSvOW4mbVArHx1Qybj4N77E8sm-9GiwVssQEciXv0VH8acAlcjiVZbUMByB2vDL-DNkAG-NzUbntKd8KszTRkEwNDVgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ هالند: راستش بازی با فرانسه زیاد برام مهم نیست چی میشه؛ احتمالاً اونا ما رو میبرن و حتی احتمالاً قهرمان تورنمنت میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78548" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78547" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwV1e1sNXU2Cys2gZDx883SIHY8bKbHGKyxYk6AGJRgORtrKGAUz2JIZyV42BZS_nOTa-G9Bs71AviZJ29SKCo818FUP6V11O0XiZ9XmNpBd3U1TvpBr4cA1xGr2567bxkvjihQj7NZKqIC3azrzlIsD41TSjCLTGH6iF_y75HJaxMlWS84IDAOZkcacYd3zoLQ3Y9QKycFF3J9TJtzG7bQjNj645WOOmRGlQn6QHzQ3TqMdFfZb5HtU5ITbbthaQhDZ0xm6AyrNtGPWDC85nkcfjmE8D80Nj8tarXG4x_54tEU__FtuOb8mDMdJe1SkYz36qvaLym9G4aSmoGQCfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78546" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbOA0GW7abZ3AZv_nYHwOZ8Edmbux-hfV6NokvFdagrlyr073Ndg5hlonI1K2hJbSgm6lc_lZf2pnUk9EUPHXUqrtO8mcR4lK7GaqmZHlP_05UMTWfTGpqFACUdIgTVfiiABP11WInANMtcdp50adM867T5zGo9tGBlNeRBKXx7kRqPmQ09KHOyFu7Wq52bilgGhIIijQnZPkRcaRqVssP5812ytLcEDQ5tQM5VlmPTHUZEYgYJCJA_wPlQe-uIFVpNfpCqxUboSuAFeIaN4Tp5nmzC4pHSS0xJNFsqCQ25xHhq4_jhspsVgayi7M81voqnJ-Aufcrupp6619a8l2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این الان تو حالت طبیعی به وانتونز و ویناک گفت فید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78545" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78544" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78543">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inPOiHaP-1RtSnI7eMBwAlkqDrGBnVnyAuOlDTwB0XYjwOM9xiT2vWGbt-QFQZsXjo9ZfrUys0xHWLfo5ioIfgKeu6ZycqBo5CE_eXzp7b5a35Y3nUbYFMzYC5pEqHjscKSAY4uLZpJ2RIWoOqIOnHkc48NrkTCovm7QlMbxMhRpgLTTUL20gTezfji2ftNEQh7fTJXHrz4mHDcPkHUAh23f4gEdJtPVGlb-7ZekwQsUca0yGPJAXUogvAX1YhmoMKZvio3uxwlT_mfzqbVnM5k0cuwhjS-9xgonOF9ul2hovZAazeBkWC602aWgrFtwnW8_0hxo8KjXx24nmXHi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون مسی رو ول کنید کصکشا مثلا بزرگتونه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78543" target="_blank">📅 10:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sX_w8-sr17R0RhJadcpguYSQt6Ydf7xurm9cvCSRivhzHfLjugscmHSnIeeEP_RDCa0cVjxCy0TmtJ_ZhzPgIt_Or7-CkI2KYOhXlUyZLZoFqwtMxOUYb4ala1qf82cu9Knv_jCGLpNKCF8z41001WHoimL7e8ahq-ioY5jrLzEFyfKjgaoYhEky_TUwbwpSyLtmqZDcvq5nALj5QgTlVi4MnsBz4Ln2xhPTbPCR2R_TtbY3udiqMvQkITkYOrV2N0VUZJE2mW9nya3MCETn35M_l3xD6nGxQ6SdSpQ3gbyuoSXEkJDNg1pdiJxc1V0tD6JinZ4U1GdMqi0igcCmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی رئال اولیسه رو بگیره کون بارسا تا چندسال پارس
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78542" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بعد اون همه کارزار گذاشتن و اعتراضات دانش‌آموزان پایه یازدهم و دوازدهم، آموزش پرورش امروز گفت حتی یک روز هم امتحانات نهایی رو عقب نمیندازیم و سر تایمش شروع می‌شه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78541" target="_blank">📅 10:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من تو کل زندگیم دو بار واقعا از ایرانی بودنم شرمگین شدم؛ یه بار بعد چک کردن کامنتای یوتیوب استاد فراستی یه بار هم بعد از آنالیز میزان ثبات روانی و نمودار ترسناک سقوط IQ ایرانی‌های عزیز ساکن لس‌آنجلس   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78540" target="_blank">📅 10:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef49ae44df.mp4?token=lvpQVUdNtD1ZCTvSzZaTnOhkA2r5qgn4iDJ4yMV_L_OFGBLxEUHXjjZTRU6lC0IKxJnM7gDORyOi-k1EJDo_ZqCjkor3PC0Pz9h4Arf9QrfkmTqj5xWOpjUAWJklXNE8lQg7v9JneQXFzkViVwdjx3CbFFeDMZByuDJzO-sDOGW6YQsBsW27uWpkDeVZ0ORAwuBnYkW50bzFaiLP3u6soiaGNdvv3IYNHghst6Tvc2C3LbRG7YlczJFXAAJPRglrMik9Ddpuc0dwX1sLWmYJj612DbOf_Tg2_P2zsV2rCix-5ASP7Bf8evsWhbfH2cgi-jQroHi2OIDeo0M3f9znBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef49ae44df.mp4?token=lvpQVUdNtD1ZCTvSzZaTnOhkA2r5qgn4iDJ4yMV_L_OFGBLxEUHXjjZTRU6lC0IKxJnM7gDORyOi-k1EJDo_ZqCjkor3PC0Pz9h4Arf9QrfkmTqj5xWOpjUAWJklXNE8lQg7v9JneQXFzkViVwdjx3CbFFeDMZByuDJzO-sDOGW6YQsBsW27uWpkDeVZ0ORAwuBnYkW50bzFaiLP3u6soiaGNdvv3IYNHghst6Tvc2C3LbRG7YlczJFXAAJPRglrMik9Ddpuc0dwX1sLWmYJj612DbOf_Tg2_P2zsV2rCix-5ASP7Bf8evsWhbfH2cgi-jQroHi2OIDeo0M3f9znBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تو کل زندگیم دو بار واقعا از ایرانی بودنم شرمگین شدم؛
یه بار بعد چک کردن کامنتای یوتیوب استاد فراستی
یه بار هم بعد از آنالیز میزان ثبات روانی و نمودار ترسناک سقوط IQ ایرانی‌های عزیز ساکن لس‌آنجلس
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78539" target="_blank">📅 09:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78538" target="_blank">📅 01:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=W2hztfFqgaGRU97mSrtxq-TQcT8A6edpeWmGjx-zgexthChVzj-BleC_NIkqig1xSfJNhfO6MaaE1h9m8JSn-4BJTBTU0rLaDSbFVSZXIPuUtEs6hoK843yAKC71YS3G_tVFj8rar6TWUk7cUi1r9F2H9WX5cZ1LWtCvRNjQfxfEivwjXaVeEwGsAH8Irq8edityZlG971k0HG0R6_tTBpzXfWzYo-05VaiIMCu0gX_hBKF_riG2J9nlMWrD-eonlaJZZLdiZ7QEi02UJ-X0HgC9GltOc7ql1Avypy9AF0qXwQdfSuo0POZ1iUJavRzM1NKEzsEmV9MLxy_2Vq8pXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=W2hztfFqgaGRU97mSrtxq-TQcT8A6edpeWmGjx-zgexthChVzj-BleC_NIkqig1xSfJNhfO6MaaE1h9m8JSn-4BJTBTU0rLaDSbFVSZXIPuUtEs6hoK843yAKC71YS3G_tVFj8rar6TWUk7cUi1r9F2H9WX5cZ1LWtCvRNjQfxfEivwjXaVeEwGsAH8Irq8edityZlG971k0HG0R6_tTBpzXfWzYo-05VaiIMCu0gX_hBKF_riG2J9nlMWrD-eonlaJZZLdiZ7QEi02UJ-X0HgC9GltOc7ql1Avypy9AF0qXwQdfSuo0POZ1iUJavRzM1NKEzsEmV9MLxy_2Vq8pXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78537" target="_blank">📅 01:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHBvaVfjaCkH8zlHV_bfzirUEuSjI1Mu-hwN-72Xq-x-h4FmOj01Va8XdE771xjuk1uIyBwfovkzOUcEp52WB5d6b3EfqvIO6fj6oGHo9zBGbPYVbLUARBdvcML8INst3iAbzvQtPCCVb9FVZjXXMrFJA4K9e_nx3JyMWvkuQpl7GwlYhezhrwZ0Gn5L3V-dRXUXVVaf9c_M3IidZU2XqfIW6jX_bEpL2SyUHfDxBs3qafoFb3fZdwO2UNelmNArQ4SHrREPzN9doIc3UBsE5N0kPXEesuwuveyZ5l0gjuVsG_Rah2qnUjqdfBLaB71Ol6e906hmzQ4Q9ZmMHawS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان هشدار تخلیه برای تماشاگران ورزشگاه رو صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78536" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78535" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78534" target="_blank">📅 01:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آمریکا تمام تحریم های نفتی ایرانو به مدت ۶۰ روز برداشت و ایران تو این مدت میتونه به قیمت بازار آزاد نفت بفروشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78533" target="_blank">📅 01:05 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78529" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6oMaHV32yqkZa-JsKDZtxQvLfiDP00VDeiL3uCMd_dlzEqBL5pI4SiUu0C8QF8vzSPkfpD-KHu1b_ZDhqZ8cUt2M5U7ytXnCNiVPvlpfrUJqj3yL3AyNFjwre7gCTd0f0l9mSlUQSLSYoEVzzAJhC-0kkvliGYOvf0p6i11KxPhSfEV2n9CZh7VvHeRfYDUD97w7OSxDKENC5dy-gnqyByxsG02GggPt8MuWuw49qzniay8DiqRDcgT3soc7DDwO6SmVvYqSn8rjS4a8KY6BJ15dC3ljWuyX5dIPZEyfrX8ow9imedsLbBiW8L6sQ6oOfRxbBfgaCPcRO8pt8eOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی جدی مجلس چهارماهه که کامل بسته‌ست تا کسی نباشه که جلوی باقرشاه و پزشکیان رو بگیره.
یه سری از نماینده‌ها هم علنی دارن صحبت از کودتا می‌کنن و برا یکشنبه آینده فراخوان دادن که برن جلو در مجلس، اگه باز شد که برن تو و اگر هم نشد همون تو خیابون جلسه برگزار کنن درمورد روند مذاکرات و جنگ و اینا تصمیم گیری کنن.
یه سری حرفای ضد و نقیض هم درمورد تصمیم نماینده ها برای استیضاح فوری عراقچی و حتی پزشکیان و باقرشاه وجود داره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78528" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/427abb0164.mp4?token=cOPinh92d4qwoZ9QLUh6_d7DBUdYpJt0DABOxVpkiEoKku4xJsYdIlilrWY0EbNe2Qx3loP3wTUUAQnwk2KkRKlfsoGNvuP-bL6Dux6N3gJ4WQmCjnjuYo5MqU_wck5aDiQAbFr8Q1oRd0Tsgf_EtjgNFUSUZJx9eG8OFx6mDDpyMVFaNUBR8BjS1KhYlkUxTluxy_sH8fCyKGrfUb07-0NqBFNNoMSvgoX0On-tc_An2m6FaJ5Lca9_uGnL8Qer8iy7Iq0qqlxlvDTn8-MQTCU3wwul6HLW8w0HCGmYYRRAgabUg9P5vjgP7SS4E9rhqTBbTM1WWKpi-Pw-GgmzNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427abb0164.mp4?token=cOPinh92d4qwoZ9QLUh6_d7DBUdYpJt0DABOxVpkiEoKku4xJsYdIlilrWY0EbNe2Qx3loP3wTUUAQnwk2KkRKlfsoGNvuP-bL6Dux6N3gJ4WQmCjnjuYo5MqU_wck5aDiQAbFr8Q1oRd0Tsgf_EtjgNFUSUZJx9eG8OFx6mDDpyMVFaNUBR8BjS1KhYlkUxTluxy_sH8fCyKGrfUb07-0NqBFNNoMSvgoX0On-tc_An2m6FaJ5Lca9_uGnL8Qer8iy7Iq0qqlxlvDTn8-MQTCU3wwul6HLW8w0HCGmYYRRAgabUg9P5vjgP7SS4E9rhqTBbTM1WWKpi-Pw-GgmzNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78524" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78522" target="_blank">📅 23:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پسرا رو برد فرانسه میبندن مردا رو برد مساوی عراق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78521" target="_blank">📅 23:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlpjLP3wv8nBdnEMdql0Nv-0CZkSqNn1LXMNbvBi3-fvZVQQmsiWD2rKeyplgb4kmqIZ2ZqQWK1lgrM6FsNIomr3hueWEAy1fbtjfw--xxdrTD-NDfp1AhHn-eJ7BRlWdBFBnCBDUbB9_gXWzUM8ybfktc36xNmiGtH2VzA0FJhW6Gcqo2opcUQsI9HVarQNHXuXmbB8UF3tU5VG6zAt866zPS0eelCBQeb_tlr25Hg8oMyxM8ktsQ9nWs9m-9zEz9NJPVSVcvG90yVxYXO1ZlTZJ5GvWkOgxWbQTsG5zryX1ZAhuRiDdsTet1QTCxoYAKiaxAes6Cs8DaoWVOmKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب رسمی فرانسه واس بازی امشب
اگه ببرن میرن مرحله بعدی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78520" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تا الان صعود این تیما به مرحله بعدی قطعی شده:
آلمان، امریکا، ژنرال، مکزیک، النصر، آرژانتین.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78519" target="_blank">📅 23:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ia5DqfUwdoOsqpHDAHSxqNVfhH6DyTYeUXXe2Yd5XtheJD50UCNZDuiiDe-euia16GEFFY5MITZUwy8FOjpmpnru4iq30s0-IxQaobvHra4I0UQV4mEfr_NpJTBS7YcoM1GSNtwHU-8ROP96SNqDGT1L0Ur_V2aG35wuaPdZyhw8gfmWPn6IjiUDoN8ZcYTo03A9-w-ykQ4kLWynnSVmCf3tLHha40A_n3TR9ZQEVrMWtXKyHVyK4lsy4RVUGxNrOcMuSVdTvJzlPyRTZJp3EpZxhW361Mp2mkNtnb9zIoNoySakDSCNJnoKS0dfaEivmK5cvgSKrtpJTWvx_QEg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BE6TzFRWD3NtYZzk7iPT-G156MFnyU5TsiA0OOUFLhR2-6b8fviGJxcHDTGsygvs9139oYuWhMwz2KDe8RaT_LMFG3UoiRuqj-Uvw-rq60FG7Y_OfRjOF1Yj43zabg9Ch0OIKgRFZeb-t_8Pwi-3Bdv0y_YE-lFTLvqDS-iUYQibGU06KzJ0mqGT7u6D25aOjGieJvbXtluNxOh00c0QJ3cTXIhUAfYmxA1sUW6UmG5WoRpQ2kfFpUZgnMxaT88bvOjr0NxLz8Euae6K8P7RIk-cw42_iIywQRTmja_W5WjVEW9uBm945Ln89vFkKzCpfVxUYX8Yb0RhVGAWRaE8_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78514" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78508" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV6Qa-Dg5ps6vswvIlJKk2N7eiR_Ehk-ZdZWBh81toWTSTuomprHzmiDU4OGvojEBhASk5Hu9qwApD_N6P-cjq3gj0VqHVSzjme_lQKTSrWGqAYRlsz_iMSJguD-WGBbYVPR2TmgkNeKa2zus3pe-EDVHsOyKC7vxa0qViHaa7gpOc9fBfCpAL_7LhKBTAqNQFykQog-gNsICqfcNuPr0QRpN4CY8x1ByIJyyEhEZZqgWk8DfyJ6MyZretdiJZfUX5IjMIJrBQis8eSh9CQYPA8e9s4IGeybvq5MlIwV-kZo6cCTm0XAY2KgNOV5CLN9sYgnH3oJ2ey0LI6oDBRT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78507" target="_blank">📅 21:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78506">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYzc7v4T4IhYgJKBzq5s9uYEHzgzFLF198Y1gMxdvh9tXIAOKyYjboTsUbPA7_alxoTt0GTbxigsrSAvjyBrpaqALN6Rl1J6IGjySPXiRVorNRAF9gurHEu1C0NMLzMjf1AWBW9bSTYLsTEWs63mul87ge9AJ2xGmV_CzWuyPzuWollmPJxCWTfZxjjqsn7_l5kdlm2psMn7_gm3j02SVrrb-j4tq8raoBVopuQpSefn4cKcyNEf3zC3L2P9R9i1mzXQfI4TPxr_hXBdTunu5h_yNvFr65_DZ6GVbxOyXbLOo8OmfgaAcQBNo_H-TyLuTAd65gXYTxuaqx90L_WX6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78496" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q-tCcTHzaj_uft2K3y5y4d-UOJBg8zEIzUWjZfS8K_R3oMZccFeWMetcQxoIlynQ4YsO1Ii-FnR6mIMOBXLHlQqkVRP4EL1iUXEjy41FmFdXSfeBXS-nY1hWseai72R_y4kJIJG1O-d9enMerVkkVo_HBHa2dOSGTNDZrm-9MotyHW3tOwN_XOBwPeyiV-9hnBykf6AEN1Yq0JguVLFEU4psElMhrdConQ9ioYRXCQ5d5TVeGbMad79rMgQDFrG-xPKMqi0XyTG7T6gOmJ9sPaOyVr1s4wratT5UR6TMLA1RPIXVdaEvTj1C0wSeyzYPQz6PhgvXgcJmmlVJP1GiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پیام رو نخونید!
نماینده رباط کریم رسما درخواست فیلترینگ میم الاسکی را به کمیته مربوطه ارسال کرد!
میم الاسکی با سابقه 4 سال بزرگترین چنل میم بودن بهترین پست های کل تلگرامو جارو میکنه و با ذکر منبع میزنه چنلش و باعث شده مجلس از دستش فشاری شه!
جهت حمایت ازش جوین شید:
@meme_ol_ski</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78493" target="_blank">📅 20:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چیزی به بازی پروردگار فوتبال جهان، حضرت لیونل مسی نمونده
به امید درخشش برترین بازیکن تاریخ
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78492" target="_blank">📅 20:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=vbXa1VPHjgIrQ98aEeYKrD5UZqTL7-B8u3K0fyzlGT-yvz3uz67lCAHpW-4gh5KCF_i95SMCAAWMYoHv-8U2NaDAeF_b4X4o4A_gxhT1yR41k15JXnqpE4BTNy5lyYts8i6XsxfEEDnSIZKup91E8MsiMnIOKXuo1ZF3SkzDR_xgCQ0fIgyYS1ZCiWokRkLP8JA5zFKyHSMQMa5M0E6BW4U3v93qkRUg4g8c5g5tJGfrjz0loiyE0My1ishCA8vHpdeZg9pMig6lBi9PUZFWbmo5RYqEj3Hn0utSENsYwTBZyqwtr3hFE4Y9ROAqw6wShFHugHqQeKXspomlyjIFjwjDVPme8472oj1iyzI-8BmIoervRnMYi9ibi059bGrS684x1gfSTCGqNKVBGJPrLwwJrPC_NIrH-sl3beHX_1ORheVJeyvAkDRSTuUFdUNz7WmThdMcuiydjvn9sLxpaq3GMargabRWQ5ad8QVevclxNR7iRovEMmQ3JBgsAEPI2w6giei8mq1tooDL2AplYcJvxhsL7-TFNRWeiEMwbg-wdsVWdi5KYV63U6Ru4Kil5qlnrlQJbTfcr8E8POj2zbjGySy3GQJ1lD144bREHotuob5QPwZfRx0z3O6mlurnILBQcnO1-qPmulVJV4_31gJ64Bxzwl20AvoYKypwrtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=vbXa1VPHjgIrQ98aEeYKrD5UZqTL7-B8u3K0fyzlGT-yvz3uz67lCAHpW-4gh5KCF_i95SMCAAWMYoHv-8U2NaDAeF_b4X4o4A_gxhT1yR41k15JXnqpE4BTNy5lyYts8i6XsxfEEDnSIZKup91E8MsiMnIOKXuo1ZF3SkzDR_xgCQ0fIgyYS1ZCiWokRkLP8JA5zFKyHSMQMa5M0E6BW4U3v93qkRUg4g8c5g5tJGfrjz0loiyE0My1ishCA8vHpdeZg9pMig6lBi9PUZFWbmo5RYqEj3Hn0utSENsYwTBZyqwtr3hFE4Y9ROAqw6wShFHugHqQeKXspomlyjIFjwjDVPme8472oj1iyzI-8BmIoervRnMYi9ibi059bGrS684x1gfSTCGqNKVBGJPrLwwJrPC_NIrH-sl3beHX_1ORheVJeyvAkDRSTuUFdUNz7WmThdMcuiydjvn9sLxpaq3GMargabRWQ5ad8QVevclxNR7iRovEMmQ3JBgsAEPI2w6giei8mq1tooDL2AplYcJvxhsL7-TFNRWeiEMwbg-wdsVWdi5KYV63U6Ru4Kil5qlnrlQJbTfcr8E8POj2zbjGySy3GQJ1lD144bREHotuob5QPwZfRx0z3O6mlurnILBQcnO1-qPmulVJV4_31gJ64Bxzwl20AvoYKypwrtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exIZqMVe128FrYPsAvE64_zmhri7wJnt4RTqItuvV9P8nQCGaPJvsxZSH2mg-VzEvmQpBKw6yAOAEIsRAXQ5_53Fsek43DUHPIifPuosIUEPjSGwSd8-3iP0QVKK-cHPgGqlo93v6DJFUVLp3cuL31CHQFsJbTTcSUPWi9TGELEv-OrjIQi0cNCgkqSnN1MMsJLk6APpoOViu49ARtggMKxKDbazL3RgfAO-wX65C49gDcpJHhcmQStpZSsCpOPjYWQ6_rSmS7sKHuldpSGKki29A6foK-uGFxui9Tp8GYDMAcK0avaBhRJZ-kOsaWMSIxeeRP6C7idnlQh2zHkLTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78486" target="_blank">📅 18:46 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
