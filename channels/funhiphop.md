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
<img src="https://cdn4.telesco.pe/file/W5sZEDitNsfMOWA-dbD3HFdZgFEvgiE9zFutKQhmVrolyFj7KhAkqH-ca9k-UxXjJjlwy9P1yqMMHJFN6PxdIi_4rs6MQtzHeFCUhvmLLKK_FaOElGbINr9Unp1tiAHyf4KDCNYF556wYJSDeL-kzvC1VixSVQo5cT5Kg94g4GQDCe1NUzg0WrVcZrFNyZV18jwihNNMj6AtlkK7iIyvl1tNrkOMyj48MhmgD0uMkvJMvbTeGa4V_GTXQwdFasSCr8OANzaGe6_5v1pDW-N8qWYb2-abyQTJukiCG2NgVwkIH9ei9MFHlYHsZxIjp5gf7B14R3rMab2Nx5xJJ4eOWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-82729">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpTI2DDwnXJz0Q15k8ugsyzH9Fbjyz_svFXAY7zCU9geWDToTlWhI7z-jUC06MxvdJ0jhSBfPO8h8Z8sqH5NhYRh-5ShJ6FQ0yRjEBaSt2KIJlecOkp5wjoCZjg6m5LU1doN_RuSvehuT1omBBxckeRsvb8y1EFJhoLnCfzd-ux3WjNIa4K9MJKfPJDBjGAY9h3hLrvrhidijDBRXyTxDCNGHv3-3pUvtOz1bAZvROosAT95Yp0R8AzBddQaNgcT7k5ZbMq5V3ICHMrzwsT9rnPYfaxsqMV6T4RIz3M3Yo5GUPQWvArO1zvPgiK42IdY8tlVmjy9rSQAVc1l8ooAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت پولدار شدنه پسر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/funhiphop/82729" target="_blank">📅 18:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82728">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اون قیصر خواننده که اومده بود ایرانو یادتونه، حالا میخواسته برگرده بره نزاشتن، و الان ممنوع الخروجه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/funhiphop/82728" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82727">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تنها طلای این تو کشتی بود که اونم بعدن معلوم شد دوپینگ کرده طلاشو گرفتن ازش</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/82727" target="_blank">📅 17:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82726">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">میگم پویا رحمانی پتو رو پرت کنه تو کون مادرتا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/funhiphop/82726" target="_blank">📅 17:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82725">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iet-yuBP8hINgOIvB3rGCgBwKJ-wQO9foXGlkUjjjgghsa6TyNrquz4pWsKRcM2UjcG3vYgze9qd4hW9BKC022wFvWUoSOy7vV-xasXzmmsBSM6oZW5cgGh65HcxgZlYah9IqSuczt0CvEmhP_K_Hr2aV-6wjHZNNA3Z2j8ZkYYq4JoAYEDaajcgXMBInr8bPVw13g2fGkdvyI93FmHXR5pl4BKdaaIyZNfkaaMt1II1lfPXw4lWc7jI6lg93osCh7blc1lDFhmAcIaD3Mi1QGaZ5gATAuNBkI9H6a1odHMx3T42i0vmz4N5HHnwac7AjMa2wkhxHLwb2rZDYVpB3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگم پویا رحمانی پتو رو پرت کنه تو کون مادرتا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/82725" target="_blank">📅 17:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82724">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw8xMLWzYZXMw0nFCft5MhMXsexvwivCGm63h3qRLalgn11jwkzm4_Z_MXRDMHZr9yUDFCXLZEIxB3W8eeUTfdqey1mb7f99fWERyTTE1QGsK39KgW-eUbzxWHu2ON_VBnyoabdJGWc_j1P2Xb57YvWJTvZvBuYEJzTcS4qE1ikjDypJbgIreR-uKoUzhnFl-d4hQap9Ch5DAXjEKRAE5p3rT5R8-JIRY0IryX03uIuH3tpDbHu08veUGeabyK2x1IRfjIz_3dU2c5LZ8JMvsBlkERNSlpT89GlNzFSkDNhI_tDDXFIE3qPprlTGB8GLSF8GRIwWBUBlCOerHaQJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت امروز گوشی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/funhiphop/82724" target="_blank">📅 16:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82723">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خاکپو لیورپول چقد استیل خوشگلی داره</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/funhiphop/82723" target="_blank">📅 16:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82722">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJ2F3OoRJfRteg8fDd1__u9M9JJ58Kkyw2hRyo8-49ijtzaliGyC8nRcndMKcu_yXGRZ0oAhGCDjvSBIbH8wCJlmykLCEeDwhLDMxGCE344BZebhZ1ZrjtN9N9wyAFT-ecDzbtPcYbmTWSrWEaGR_t6KWD5Gj8Nb6z8qNdWSH4A7dMRMk1QPJOatYY49fZAGlNkAZSSzGGpz7lc7UGqXBIiSR0J8nBvo0-ftYqkavlTmGknMdsWS-woihLkfKSGsTGWkBIMdlfAaUbN2_rZsnjjzKQyeP_U4AJ9tx3Ffdq5xV9ctimzuN2Mvvg7W6_Mu8Sddef5ce3pM1B8yQloiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور سید عباس عراقچی:
یه سری اطلاعات کیری خفن و محرمانه بهمون رسیده که نشون می‌ده قیمت نفت و بنزین خیلی بالاتر از ایناست و آمریکا فقط با خبر و اینجور چیزا داره قیمتشون رو کنترل می‌کنه و اسرائیلی‌های بی‌وجدان هم می‌خوان رئیس جمهور ترامپ رو با این خبرا تو جنگ نگه دارن ولی مردم مظلوم آمریکا دارن این فشار اقتصادی و پیامدهاش رو کامل حس می‌کنن.
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/funhiphop/82722" target="_blank">📅 15:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82721">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj0xz0tiZUWtEqF4jiXLSAguDGuvwuFPsvq7ls9gB7oI4ORpACk4vHitgOHrRgTN9oyEaxSCoRsIfDk630nftcWz8Ncwyen_iBbaeinqlIJz1rmr9R574UqHmylaIMDD8yG2b1Zoo7hJoOf1NY_EFR_C1C7-gdID2i-Ql79Gj7ldDgdhNIdrKBjFH2S27DUxTcSRXjN0LJkDZaaTD973e-pSeYKD3SVQTKA8n_kWGceS1C5pjWkml_AeyZz_wGjwzQH-3oi1YYeWeGYeI3v2e8m3dS9o9wTTZt3pWN3IB88hoTDKUQ-eRw6XyVeZW02zN8vfwMz6RDmtNnMfR7CCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا نوید یک اصلاح طلبا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/82721" target="_blank">📅 14:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کریر تلخون تا اینجا کلا دوتا نقطه عطف داشته: یکی اونجا که فان هیپ هاپ تصمیم گرفت مسخره‌ش کنه. یکی هم الان که خودش تصمیم گرفته از تیمارستان امین‌آباد تهران دوست دختر بدزده.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/82718" target="_blank">📅 13:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82717">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">@FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/82717" target="_blank">📅 13:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82716">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8N0Dg-L3cGBzL0X2ckfitaeWDBZJBnnAyCxgNi9l1qI8eL4AzWPm0fado4NsMBkqDAyC_8zuA_BOkQQ68LPy_BPlNJ0CAs3F08HLJuI2omJnF_rcmzuv0Yw85GepObISM_ts5y6VrYJfu2CSxLb6Xjb9Xf7qB_BuN25x56rMxoPwdVyBoyQXYSG8nAR6k-1kriwZRgKBD1pXDd9S1iJqPzRTiwHL2FCp1V3lF2F2HYTD78YBGfBu_G6ZZUYvUhPZp5Seo95S-WHRVNnIkOG3bsFAZrdGCn_6uoUlDYGuxGKxzixEyeJIgBq70vqNkzxUQtUm-hJzvwupikzLhAY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82716" target="_blank">📅 12:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82715">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsqohrpM9xrOY2PJywX2V6Mz0Y002_RP7dI0ul9_X6rJwGBQtyVog74ZE2xv36KMbnzXcvDRmVeqkkX0PHW7QFjdnFJa9B4GDf9GEZR9FRWpMLOxOrIrRHep7hG_8c-fRSt-CWD0esYdagmvVvwi9XRsTvRzMF3ZeFhMGZ94KIfzD2BZz1qs3feMhoO2P1eGKUm646Ch8Nd2dVLy6HIFmgdn424kuOpZxxnLlMz7JKKXpABsqAwHtsNR1NEinaS5KLNWqrwSYU0tGV5_YZ49D2XHEOOYkD9hnJBKy8nq0D6t5VpCG_xBxCa5neKSiK7X4vNjvbrOnGGRBTzbdnHhQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زن سابق و پسر حصین.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82715" target="_blank">📅 12:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82713">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlvbOLZolfdzyv5h8OZorKtz8anaZROzltfzMDiasSFw0RUA8MZvBGomZM94TBXWVHrICwCGZ319nZHRf8w1-gva4t-TwmME0ho9XJ1WWbLCG57hbtGY1Y2R3fScsXEWp-CvjcKk1OMwdhW2uuIx63om22TuSWDRko043p-1Cm9At7SJEaghh3xJ_1lw3SzuQpT1W_cGAunpXAXp9ygYrOd2h0Dc-PB9oS-vaEi1p8sXuMMr5YjNfDyJwykfSsGzjqOPJ9pf-S1_RwzNHCK-U7OxwxCrGkDIKgoy1vC7ePVrVFSvoWmX3pUeqrzIqwTQ_e1ppeElv4eQardDgflVJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXGltWcZj9YUZU-4o7rqBzw_IvSyKay6ZEvpq2DEIxKAV-QpfH55qO9esY_NNuM15zyLCmrGTcRm0_lbIlgQcRj_A6Iz4YEFmn98JiCkYQT6zxiQ0gBGtNUhQwKu-z2TwaL1lMZJBjrebqPTdq2g8I_lhPhP_nStZmZ0c_miZfgV8aR0WqwjAnOVNDsQQHsKOVAtWgbvglY7A7KSnfEcnL1vZSvBbVvzX7V_Wr3FxnqAGszru8z7RCYIbDyxPffgdGr39FbncTVG6QWJGGDm95FQ8FsZieGS2GDgQtSvXda8EOmw-at51bAKX3pOP2snqsywjMSEdEpLfS2g_YSoEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دولینگو معروف ترین برنامه آموزش زبان که آزمون انگلیسی این اپ اعتبار بالایی هم داره و مورد تایید دانشگاه‌هایی مثل استنفورد و هاروارد هست، اعلام کرد آزمون‌های این برنامه از یکم سپتامبر (۱۰ شهریور) برای تمام ایرانی‌ها متوقف خواهد شد؛ این تحریم شامل ایرانی های…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82713" target="_blank">📅 12:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82711">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVkUG__ZiBlx88KZ_DtzdYVTpfcYCUR90tN8IJgdcFMTFD2hSSXJes_bHoydv49OuKGTWpIDDpRVHpjKYsUsSykatCMbTHYbL3bZPlEgsylrvyFVC7GrPF49FfsPFhlaivhuBHLqp1NLFh9DJfCv0odaXjHkekgiSXZz0AnMFgrcFR-EWb6N-M7JWnLLqzm-Rh-N3kDdGVyxZvC9TUwNXuMNtIi5et0VFisQ4otOy-XePAT94-11CBUc-qRNRSPq7JaVMqtyDIRJOBQ0ALvKFnXYMEnQ0VB5ZzUe1MPv_NJPwqsha_kAMeAwXCYyOY-eXjZs9MX_s8x7ot_b-bFbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه فن اکانت انگلیسی چلسی اومده یه ویدیو از ریدمان های گلرشون سانچز درست کرده و گذاشته تو توییتر
چه آهنگی روش گذاشته باشه خوبه؟ پلی کنید بزارید رو ثانیه ۳۰ میفهمید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82711" target="_blank">📅 11:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82710">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VS3mxaXSCGOPSsou1lBSp-C13hyNpBkfpOV3TgUh66rZNc3olLT9Ql1-N_X1BRMZJv9W1n_d5LnhfyeCartyN8pdF1PXK45nvfMubrqLTnHZ21Dqhvk7gKeKVcvtaCJWqu5oYq2zYWUoZvfkkdvlL0n9JpYasybWkAn7b4datM13TdHyJVw6i381-ska5_j2yExfS-neivKM2sfIGOeLllTKfDDNC_9g1DiHjWBwMRG3hNHIKhl717quTuVQGomIK2HnLOIO6kyK6R-FSJ8M8YZU6orIYBqsFMZu7vgzmDj9jcH26wx_3kSwu1LkPsfLEPAJrknxMasR6bZ9KMemng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ۲۵ درصدی انفجار (ویژه شنبه‌ها)
💣
⏩
هر هفته در روز شنبه، با حداقل ۱۰ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در بازی انفجار، در صورتی که در همان روز حداقل ۱۰ میلیون ریال پیش‌بینی ناموفق داشته باشید، ۲۵ درصد از مجموع مبلغ پیش‌بینی ناموفق خود را تا سقف ۱۰۰ میلیون ریال به عنوان بونوس هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BWC25
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/82710" target="_blank">📅 11:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82709">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه آمریکا قراره بدنساز بشن
پیت هگست وزیر جنگ آمریکا داره به نامزدی تو ریاست جمهوری فکر میکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/82709" target="_blank">📅 10:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82708">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449380bcee.mp4?token=X3a5hoHDBJz3MODhla3cMUE5TlSgtaXQ08CDXMRIGX_hnigJUyucTMK_ZWwjcpPYkvbPP_pbh2PWAno9onx_PSCtffpxuxwmo9zR58su738gyjzMJHCLaeMRn6VkgjjtDx6ZYH6gczhX91vJ0Vci-4iwjAYDYIQz61RvzYHdovworrKC8T8CMyp4ECspEOR0y0N8qhsW70sAtjLWx9Hbspo1OTqFNJj012cJEHjQx43WcEjZ6xZFuZfXxz94UFE_bbnJ9-uoD3Ct5N0cC3tRlV7a-QMd6s2ljdm5tFear12PhyNFre-NnnF937jhTUm8N4mHU-x8p_gy_fwGd67O1Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449380bcee.mp4?token=X3a5hoHDBJz3MODhla3cMUE5TlSgtaXQ08CDXMRIGX_hnigJUyucTMK_ZWwjcpPYkvbPP_pbh2PWAno9onx_PSCtffpxuxwmo9zR58su738gyjzMJHCLaeMRn6VkgjjtDx6ZYH6gczhX91vJ0Vci-4iwjAYDYIQz61RvzYHdovworrKC8T8CMyp4ECspEOR0y0N8qhsW70sAtjLWx9Hbspo1OTqFNJj012cJEHjQx43WcEjZ6xZFuZfXxz94UFE_bbnJ9-uoD3Ct5N0cC3tRlV7a-QMd6s2ljdm5tFear12PhyNFre-NnnF937jhTUm8N4mHU-x8p_gy_fwGd67O1Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجم سیلی که تو نپال اومده رو ببینید خایه کنید  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82708" target="_blank">📅 10:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82707">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fea1138c.mp4?token=GHqYkm3gRtrf67WE_syqJ6oGKlp6JsHzlEbzkGMEadLBBOUO_0fIFyT5HmDnBKpH364opn4pY2aYdWp8uQ_gyAfsGGZeY8s8Ncembf1ZLZVmD31P0ke0qI3s-zJ_XW9Qx0NOqiIjmSx57xtJaOcBOUvxIRx7eB-Vpi0GKjWpSxsoPNS4WUspSoLhrNB6CaE96cY3E2KRAsAnBiPY3nL73sjh6zQcbEbJiGuXzX6FJLMNndZW0ioAz2jg-K24tg7hd4BXvXVR9PJbUfLUyRpunzAEWz8uhBAgta9LKvQ-1AF2r79MPsMLHFx83JPkksJc7sp68KCTpGyRgTPmjlDaLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fea1138c.mp4?token=GHqYkm3gRtrf67WE_syqJ6oGKlp6JsHzlEbzkGMEadLBBOUO_0fIFyT5HmDnBKpH364opn4pY2aYdWp8uQ_gyAfsGGZeY8s8Ncembf1ZLZVmD31P0ke0qI3s-zJ_XW9Qx0NOqiIjmSx57xtJaOcBOUvxIRx7eB-Vpi0GKjWpSxsoPNS4WUspSoLhrNB6CaE96cY3E2KRAsAnBiPY3nL73sjh6zQcbEbJiGuXzX6FJLMNndZW0ioAz2jg-K24tg7hd4BXvXVR9PJbUfLUyRpunzAEWz8uhBAgta9LKvQ-1AF2r79MPsMLHFx83JPkksJc7sp68KCTpGyRgTPmjlDaLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجم سیلی که تو نپال اومده رو ببینید خایه کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82707" target="_blank">📅 10:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82706">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نمیدونم چجوری بهتون ثابت کنم ولی شنبه حتی از جمعه هم تخمی تره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82706" target="_blank">📅 03:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82705">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad6P4u9DLEBxJh1PEANooD8oGfoymf6tTd44nkFIpOL3kLFOCyESjEmouHpXLsw0uXXEy96oMUeJHXyFvOmJUQ1XFbRz7FeWRxJvpZROKTmSo_HxgZqMM_98qYsPoTLWOloNPDaFDfPFCqX-WSm9d9CXH3rkOSrL0FeMGh4DbuE0qABzncxzHbM1s-AOnKzfnGMVpQcHeMUsTT4wTlWH_DQPbUFFfqo6lWYhUYBqOlqHQ3xw2U1CWLKsDAnI_AqvL8w19iy8jDP2CPsroHUPNWpar1HQLIdRwhmPmKeLXUJiCRkAdePQ3CHtIfxD-vp58TkSo8q8F8zqTe9Ard-EcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیلی بازرگان: شاهین نجفی برای پدرم با صوت قران میخوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82705" target="_blank">📅 00:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82703">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ7c0gF-F4tCAt8Amq9uRo0DuBvLJfbGvhzkdj0dVNK00ZNzdTtMfk_xrxS-wpui90qJTOqiOq8_Mdpy_PiiGUZyPiINgJRnkalAAhXsjDUs4GD5Ay3iT3affm09S69PnmK2FTrgQ0p9ABqVnfEaPFAgXvQCjk2iUk-rnXfQ7xmQC9RbE8Hn_GAddW8xeKh9384R_aYtk91MwkkY536NZtB-eqqVcTCMi2v_1VCmUCQianC-9qezqfVV-Bf4KJtr7_SmP-WCYsD6VaBieMjcuf6TdXOdcgWWCyH8MtGwWUugYtemtUU4wAslIKActouk-_cPi5JzdtHqBG8tYEvZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8b3495ce.mp4?token=MiuxxK6_VLK8Ay2hiPFXz8H1a5wP3W4WuLl0DsW3ZQTkOcSpoMrMZVitv10t1pNrnUk_YWYi1uosdbOm9bu4b-GBHfdIX0s2KMu5mrU6L3OBp58Jevxl6OXZAMSGiXBMJ48-H3y6_UuMg_Q4URPgwonLteL3rt8k6QhnKlycVAH55OaMFTnOnlx39QXHwd3nTilZ1vSB95cOMh6hOdZj3EHVAmbD_CAXM09Uy5402kgm4C_J9GgPIWLFqQofsmqJ_d524_MPuP5ui6dm_fhaeLLkRjj2en2l-QIKyl_Hp8E9IgGC8IDeKtJX8zLsCrQzXn1o01OUSpxnu7BuVtRG5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8b3495ce.mp4?token=MiuxxK6_VLK8Ay2hiPFXz8H1a5wP3W4WuLl0DsW3ZQTkOcSpoMrMZVitv10t1pNrnUk_YWYi1uosdbOm9bu4b-GBHfdIX0s2KMu5mrU6L3OBp58Jevxl6OXZAMSGiXBMJ48-H3y6_UuMg_Q4URPgwonLteL3rt8k6QhnKlycVAH55OaMFTnOnlx39QXHwd3nTilZ1vSB95cOMh6hOdZj3EHVAmbD_CAXM09Uy5402kgm4C_J9GgPIWLFqQofsmqJ_d524_MPuP5ui6dm_fhaeLLkRjj2en2l-QIKyl_Hp8E9IgGC8IDeKtJX8zLsCrQzXn1o01OUSpxnu7BuVtRG5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به هر حال کمی روغن میریزیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82703" target="_blank">📅 23:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82700">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a822db941f.mp4?token=YNL1XbHMyzKv6RCL8-7UqsclqtRsDS5NIyDRq862SE5CujTlAEYIV4jDkZDp8CecDL7oNMQINBGB0D6axKRCkBrsaES9r1z6Cj5toGhFOtIdQ3zwfpbQqmfNMLFTYy5Nf4lxmXPnaU0dHCGCApoPnvhVgDq3xqz5WxAQqts6WlxhXv82M4h6q23DL_uIYDc5Ls9zQWgFXRnqDGtBzA4QMZpKZQm387Ag9aDYQSV-Azv_633Vsz0J-yqyXW5ORk8Pr_6n791lkUFK7yMBNQeAtNd4SkPS8N3a9Xu2WqJXJ6Nm1rJrqRmSsUULgsbrpsv7jVTYvwl9g9oKi5_KxZv49g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a822db941f.mp4?token=YNL1XbHMyzKv6RCL8-7UqsclqtRsDS5NIyDRq862SE5CujTlAEYIV4jDkZDp8CecDL7oNMQINBGB0D6axKRCkBrsaES9r1z6Cj5toGhFOtIdQ3zwfpbQqmfNMLFTYy5Nf4lxmXPnaU0dHCGCApoPnvhVgDq3xqz5WxAQqts6WlxhXv82M4h6q23DL_uIYDc5Ls9zQWgFXRnqDGtBzA4QMZpKZQm387Ag9aDYQSV-Azv_633Vsz0J-yqyXW5ORk8Pr_6n791lkUFK7yMBNQeAtNd4SkPS8N3a9Xu2WqJXJ6Nm1rJrqRmSsUULgsbrpsv7jVTYvwl9g9oKi5_KxZv49g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکوندی شیر
مسعود پزشکیان:
نرخ سوم بنزین از ۵ هزار تومان قراره بشه ۱۰ هزار تومان ولی زمانشو هنوز خودمونم نمی‌دونیم سورپرایز باشه بهتره.
(احتمالا بلافاصله بعد از پایان شهریور)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82700" target="_blank">📅 23:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82699">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBuo2LCY2_uPj1qaPDxCH2sdg22wz_solA2YnN5zN3bgyTzIe87Gy8TOQPINvHivto0dC5STUD6whHqWstTtETqqMCNeh0FX0p635SGjFiKyPGqBfaBikTkGyx3bSIJqw0OivppsstpwX67gfF4glWFq4-3Srcgza-lyuDjA0BohuFZUQ6EO2BTMJ7dvoMlB7vVeYLtmFMPz-LpM5RDOah0I94w8fCydJp5dkRwT4U17yzvpWkYKJY9fxQ36X5ixOG8q78egcIffEkxUOc07Fj3fE6x_W4GBX2NVoaMC05IMO1JzAOncXz-zK4v9JqYQd8bBBLgu_wnyhuJdma6wGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای تکمیل بازی Gta 6 بیش از ۸۰ ساعت زمان نیاز دارید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82699" target="_blank">📅 22:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82698">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd-pQNmjixAwFCo3k8sA_v_MuJ4Jwn9lUvSlBWnV4wxL-R-2d_eNwwQgDwyG3UVHG5qxi_x9GFDHVEPd2TPHuXC3UwsYDgsBHouqKCeCqtB6xQPSQIpmfQ-2Ng3ktjUXf_haPuQnStAUW7gckffBT6x1hAbEDc74aJof0xh74BGjGIOQJ4_jcFOIjZJURwJmeUgIMt6sVUV41_joBJO4qT6rbRSVpisLuEq6jiqIR4EtW7pvkoC6XNvZFhdPLGMR7oElelUuIGFcAvxdIlEvnqjqKm6t1C7v9SKro30NhVULOrlspxjdZ9dxhDjoDNSOntXV-b4KGAm6OeWiSXExLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکی گرون نخررر
حجم نامحدود واقعی یک ماهه فقط ۵۹
هزارتومن
تست رایگانم داره؛تست کن راضی بودی بعد خرید کن،خلاص
❤️
@VpnRgbot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82698" target="_blank">📅 22:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82697">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فیت خلسه و هودادکا رندوم ترین چیزی بود که میتونستید امروز بشنوید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82697" target="_blank">📅 21:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82695">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXGBR4cd9uigLcZt8bTvScO-N9BI1b2fguj8WztyUL5f5sCTthvcNVPFBX7aFKN8yp67F94hCjGzLGyJ8q199n8jR1k9wsGWo3mdwL6VYOFv_Y95G-lUBvUERJW1CZKyyXNc2oLAYKDVovY7ZKPxCbpfyGkpKr8NFnSrSO4p-cVLYta-2zloDDydmjv6G1MKMwA9-4_HZK5foMGsonli0faJkOy1wFGbyEluvuSKCfQhjiYbfXWPRJ150J49jxXYodMaJZm4v0AfqVTNMuNlh3E53ss7fpP1EDi_X24OZEVzp4FYihAWEVmDU2DYAf_a_R3sccol6Eu3ZDNgI8XLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSQoK0YYKylJMAR64ZNNzndMEehmISDkixNqf_jGw_H3WMf2aKtPAG1FwbWiyki9OycUdUGv_yj4m4jcrcXN9hc4NitVyzmtrY8cS_XHI8I3bSaLZ1lJ3OYCQBGLpuUSXaQwmUhWjbvmwQbxTUvW6RdY94JG5LeVMPccfPZC9xAyU0vrK7ZG65anRR1SYKqnLD6Q5kHQL0HZSbT0vsIiBX5ZLXUxpXBrhPFPv1Ft9JBQVT-vC4BbjeAN1V_HCnqIl3l7qdchzSI34FRemszeDbAnY6IvsYVTIkXJnN3l6eqxhyOP24kxtxKnQC1iSnhmw7fO1ozxWJvW4tiBRh1IQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ای کسکش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82695" target="_blank">📅 21:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82694">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvwQdXfWE-LvkhDBklU6b60ETVRqmN94D9qlDu4DfJYdfgvwlg5PLaGkgqSH6_gRJPqbUugb-tcIPYRLyW-6-TuahyvMizKJLiI9Mqma7nDRrKBeoKrjwVGWiG6PlKrRCtstNcryBg-WPb-SBhs1SpNxjUq3ik9-7yLAxMO8LSYPgZrmZ5QOI6R_pDZkDT2f049G3Vym6Q0UXBQCmaZijrAB_ogjL91ljLbHgFhdwRf5DTYMn01kSJ8siUet1SjTfg-D8leV_OFXVvh7_toN4-dFUrfunxawJFgroXrrNlB_7UkArHbbZOm3kk5UAxFf8ylkKQlsvjGxCrYc0VrVKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82694" target="_blank">📅 21:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82693">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مجتبی_خامنه‌ای.pdf</div>
  <div class="tg-doc-extra">250.2 KB</div>
</div>
<a href="https://t.me/funhiphop/82693" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای: به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛ مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه. دولت باید قدرت و مقاومت ایران رو به مردم نشون بده، چون اگه…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82693" target="_blank">📅 21:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82692">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مجتبی خامنه‌ای:
به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛
مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه.
دولت باید قدرت و مقاومت ایران رو به مردم نشون بده، چون اگه خودمون بیایم ضعف‌هامون رو علنی و پررنگ کنیم، عملاً داریم به دشمن کمک می‌کنیم.
مشکلات و ضعف‌ها هم باید با تصمیم و عمل درست برطرف بشن، نه اینکه مدام درباره‌شون حرف بزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82692" target="_blank">📅 20:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82691">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a618ede86e.mp4?token=gEzm752gQtfuDr6328RAAO_9ZhXnm2b5cEcGvNzieHeg0qCCTfB0DICd0kD53uznWXMawBZMlDT3gWpTHi0xqiI5AkvP95HcW1UY_1e6mK1ERHsoO0Mgt5iBdsYLTTTLiaUBIBPZeY1e3CdS4TQYTIRgr0FYi1JatpZ7wDTJhmdoH2GjH-9bD74v38Ngtf0gMhroEStTUQl-770f5oixkzRbW2vjGqkxWsz_3hWTXv9nlGSOK3DoHA8FfD6KpbN_zQ31IWCL8VJODdx08CjPjN6f6BKYl37rcNgcOwkquTHmOn7NJsvwz95mPV30v4JOaEqOcPeB1n-b4s1ElFUtXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a618ede86e.mp4?token=gEzm752gQtfuDr6328RAAO_9ZhXnm2b5cEcGvNzieHeg0qCCTfB0DICd0kD53uznWXMawBZMlDT3gWpTHi0xqiI5AkvP95HcW1UY_1e6mK1ERHsoO0Mgt5iBdsYLTTTLiaUBIBPZeY1e3CdS4TQYTIRgr0FYi1JatpZ7wDTJhmdoH2GjH-9bD74v38Ngtf0gMhroEStTUQl-770f5oixkzRbW2vjGqkxWsz_3hWTXv9nlGSOK3DoHA8FfD6KpbN_zQ31IWCL8VJODdx08CjPjN6f6BKYl37rcNgcOwkquTHmOn7NJsvwz95mPV30v4JOaEqOcPeB1n-b4s1ElFUtXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر کلمه‌ای که اینجا تایپ کنم فقط از شاهکار بودن این محتوا کم می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82691" target="_blank">📅 20:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82688">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNm753tpZQcNP6YPLBtvsso6Jvg_lapd2EhxP-xhl7-iejJTS-sOnkZfuFXq6mN_T4OZ-CcSXw2gO3EFhjmI87QdpsYbuiLzlXmFTHJmE8gCsDiPoxLxigsZVA4vJBvkW_Zgbkls3s_iyPEKWcUJZfS_7heOBYDfXiIveDxhoPGOsS5_eRHzYOymMjOt5NV3tcHjwoLyyPA81lmfDvXcGk8UqO5BdDViV7RRruRal9APIpKEWM71QTL1QPG8bLdaSgXuV1LtObe4KkwH5ZxrCRSLryS4q7S1hotFc45WuLH7oq0FVilDadWnaQECVtU7mJMEP2HsZteWTTDcNm_3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولینگو معروف ترین برنامه آموزش زبان که آزمون انگلیسی این اپ اعتبار بالایی هم داره و مورد تایید دانشگاه‌هایی مثل استنفورد و هاروارد هست، اعلام کرد آزمون‌های این برنامه از یکم سپتامبر (۱۰ شهریور) برای تمام ایرانی‌ها متوقف خواهد شد؛ این تحریم شامل ایرانی های خارج از کشور هم میشه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82688" target="_blank">📅 19:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82687">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn_isuIUUTHzIOWIki8RnV96lSU8Fnd7TytR7kc3JEafiri68u98kI_yHYaWugDXhMvYfwLH0KUg4iy9VeeK-F7UaGW7GyCuB6CIt6yfBYmUceXcXs6jDOFfXBAX9TdPDt4BqSm94h6rCqoDAtMU2hx4K3XId1kTm35QPxM_JPq5-ofqRRhZj7dUFagXIX_J8e29glMtrC9eRWf6UGeeuQ5Gwp4RbmxTfVzR9Jeoesy0Y8bBH7Ym05PehCEZXO9Iy3VN7BaqicaUK5V9JQNBhRrBZZQFmioW3kfsmiOlKV6ZIyoR4bMGyAEiuayk6K8ocvnMGuM-byc0WJgDVBfy8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا راهی میابم یا راهی میسازم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82687" target="_blank">📅 18:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82686">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐍𝐢𝐦𝐚</strong></div>
<div class="tg-text">حیف بازیو نمیتونم بخرم وگرنه  تمام کاراکتر ها رو میگاییدم زن و مرد فرقی نداشت کل شهر رو می‌کردم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82686" target="_blank">📅 17:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82685">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecRcSRd6OYfnHYM3eHhqDu9tKY_7_dSz4qQG3UiXkAcSCRxMZLx7LCzhI6CQNo0ssYcvZRNSFaoF6EFuot6MSiH7q7Oa1E5M9Fe9b13hKp5b9ULehAYZbZe9jWtLg_uJwxRLjKrBhvrYLL77c8I4-Lz2TuXKv2INclDlcA_O7EA3OjNBJD5_ab-X7j4WfaegKasPDB1nRUMXodUDYlPrEkxwnJubGsZoJEDCwB3xGlZxRxwuXjTFL9UQPeLtV0s7O8BN0FV-RI7LX7BCsSj0RGfZL11faBJmsa6cFHKHYsa5ywaUsMeUtk_GFI-D5u841Cy5Z02hHcOkEWHyCe2QSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیم ساعت کسشر خالص بود</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82685" target="_blank">📅 16:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82684">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پوتک آلبوم داد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82684" target="_blank">📅 16:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82683">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پوتک آلبوم داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82683" target="_blank">📅 16:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82682">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نتیجه نهایی اومد برید و کارنامه طلاییتون رو این زیر بفرستید ببینیم چه کردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82682" target="_blank">📅 14:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82681">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03afa533d5.mp4?token=rV8LdHaw9FlUUp0q2TJ3nDXBCSgGYbtfEjD9GxX1cbmTtDv-1Fy38Rv0qAjANggO02cNPG-noAQR21mZ95T2bskn55AtQV04pNjnnmChEXW3sHAiHWR0U8ImggDN3XQdOThoD_9RW026DNA5U__vQohgVhsi4qiFAyUXcEtFqha54CxtUxfvmsNDX74PJrSV-r0OXOXvCxPa6tuatM7JRXJu3YokFa8ri31Z8Tjgf_PUbZ9x6uizmlNRswY3N6LQ2jLzpRvin2DcOYGeKuJhHgKEs0OVLMPOK48LgBvMDcgeZBtkXyueOjp0h2npU0tZND55NucFtKbXfX2mpdwD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03afa533d5.mp4?token=rV8LdHaw9FlUUp0q2TJ3nDXBCSgGYbtfEjD9GxX1cbmTtDv-1Fy38Rv0qAjANggO02cNPG-noAQR21mZ95T2bskn55AtQV04pNjnnmChEXW3sHAiHWR0U8ImggDN3XQdOThoD_9RW026DNA5U__vQohgVhsi4qiFAyUXcEtFqha54CxtUxfvmsNDX74PJrSV-r0OXOXvCxPa6tuatM7JRXJu3YokFa8ri31Z8Tjgf_PUbZ9x6uizmlNRswY3N6LQ2jLzpRvin2DcOYGeKuJhHgKEs0OVLMPOK48LgBvMDcgeZBtkXyueOjp0h2npU0tZND55NucFtKbXfX2mpdwD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرش عمید، معلم هندسه و گسسته‌ موسسه ی مدرسه آلفا وقتی یکی از دانش آموزاش گفت ما برای کلاست هزینه کردیم به جای صحبتای بی ربط، بیشتر روی آموزشت تمرکز کن هر گونه توهین و بی احترامی که دوست داشت به دانش آموزاش کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82681" target="_blank">📅 13:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82679">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv1vlDnQmZzfBUreyhJUckHeTMk_SGB5i5dLVRSyW8c7VjNUy0VQz-y3LVrhWIHV6adO_ccfy2LIfkSCIwDs9yhtnln1IdxbzZT1nm8mFILrPa-X4nBXxutxgWanIVCPUFgzbiW6i-yzbeArL_E-cBGd-uEX9TQkzfFzwtnrIhn8zhngZ8t7mthgTuNRLXFVp_MZtC6yAM70i6O41_5F3_d2aXFQnj_Jwbh-S4IuZw26dyhCQNBs_UxE2vTVkHrmn-5pliMB7BVTafu7Y7sf9fa6tXQVhH4D4gAMQFT4E5ZVlzmskWYVJbfSEK71GaaNkPUzQC0Z12x-3lr99WuV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون دکتر عراقچی جوکاش قابل‌تحمل‌تر به نظر می‌رسن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82679" target="_blank">📅 13:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82678">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDi-BLiF2jbTjdmHieVAbgJFijvgm1W77qsxnuOYJ9hyuk9IK7TzXABZvMqo1ji2naz3jH1hgKSL-DjoA7F5mL5UXDSblLR1cCP7OGh9Vu_jRHCAUVlA-kwKqydgeQMPaRu1rqBtiWSQ5Bw978Dx-EE3sUipROxnj1G1g0gDvlBfSNwpd0NICpL7y8jz78Wf5g-4CxyD4Bpv9gTpRKWZzIDOtfabwPkGUjtmPC2y8SCYFsl945HgR1MRBZ7VHK5sY22I2N7394dkSGypqf9xFsXju8CsspweO_SK1CdpoVtKewMEPg8UY9IQiaqZvchTszZg62qhNPRo6VgjXF5GJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم از همین الان پس‌انداز و لحظه شماری می‌کنم برا کنسرت استاد نامجو تو برج میلاد. واقعا حیف این همه نبوغ و استعداد که این همه سال از وطن دور مونده بود. ممنون آقای پزشکیان
💘
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82678" target="_blank">📅 12:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82677">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcfb73b16.mp4?token=OXgZOUwxv8rSrryW3ouiYYLw2bdaiNuD6B9mn8GRxrd75VWP94aanJPkGEd6LjY3C0R2mW9ZGI6pvmcBe84GZph0j4sOeE6wDBBk5MT-rc8TMEP5LkhCWIy0eOhmiGXofEOXFU5ZbGXHpzISFfvAksfdcPZfChlJdDU5Ayctrhgf34Wqx1k5LphBKJX3laNTUE_OVSyTjKNHhSgdp_kUlXfbTUBLNE8iXfyeLoCnCqCsyT9MsaOGkVNQNtwRrKhNh1Xyny1mrUhXKZYtsE_32L7sN_dCVWu1B8L87iBV1Fr0B3QYjAbmgNBZFtGyIqzC4IzXfCO8fNjkHaWuPV-0Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcfb73b16.mp4?token=OXgZOUwxv8rSrryW3ouiYYLw2bdaiNuD6B9mn8GRxrd75VWP94aanJPkGEd6LjY3C0R2mW9ZGI6pvmcBe84GZph0j4sOeE6wDBBk5MT-rc8TMEP5LkhCWIy0eOhmiGXofEOXFU5ZbGXHpzISFfvAksfdcPZfChlJdDU5Ayctrhgf34Wqx1k5LphBKJX3laNTUE_OVSyTjKNHhSgdp_kUlXfbTUBLNE8iXfyeLoCnCqCsyT9MsaOGkVNQNtwRrKhNh1Xyny1mrUhXKZYtsE_32L7sN_dCVWu1B8L87iBV1Fr0B3QYjAbmgNBZFtGyIqzC4IzXfCO8fNjkHaWuPV-0Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82677" target="_blank">📅 12:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trYZd8WQ9GXybF_mAAFOqgT7CW6GNC40NF0pb6hpcL8khFgh7RrpisXn6b00kHS6wZ4N_8K2A6U2ymWVJKmriD-MxaS-wIAQq83IZfae6L3rTawIGQpdnm7Mu97b31LiLWq0qfzSjF-jKQK3bXRzoeFK3OEEtMyH9XJfPuXG2OkTJVu9URjwx1nN5gCTgt5EI8g6us7j5IsGrT5haCSTIIf73sCu71YVCqJdr9U5NjV7whJJ_0NeSfHJihHAj02XT7hgBSBWfcPwTxmXN7P02FLAAFMpFe2beyp-rH7gHSM9hDAWZjXoNH_3lbQp0ztjED9LUnWkfx_vOvJFhBN5hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qokovE5udJXmiKUFD3h8LELLekW2aBIs2aeLzfy82FPKtFMO6IbxDVQMb4kTDwnQpgpIvxJuJL7vbCe8UVz6oNJiVWtSALfvWkGMNwB5Oo1wfb8KZAsaF-ra_2JNQt_GFMV-hkSx91z6ZetUqLTN2zjryVOqll6AUMbi6NkOxjNt-zGsbVsuDxi2tlrAgAqeAOup-VdEMlE9Q1hXBwXB8xPQk4KkahHMiRYXQJ-lMz--GDmlyzkfXccpv9dYwp7ktN0c6CaGUhrsXso2PJu37GykvP5Tx6MQQ1Ei8YlfH1X_V6GUDy8g6eWmdcNv5Re4hToqhvOyGEpH0bqAUenjtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارسلان دیگرد (یه رپر زیرزمینی که احتمالا نمیشناسیدش)، چند وقت پیش تو یزد یه اجرای خصوصی و محدود می‌ذاره و تو اون اجرا یه ترکی رو اجرا می‌کنه که یه لاین سیاسی خیلی تند داشته؛ برای همینم براش پرونده تشکیل میشه و به جرم تولید و انتشار و اجرای موسیقی غیرمجاز، ۳۷ ضربه شلاق می‌خوره و ۸۰ میلیون تومان هم جریمه‌ی نقدی میشه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82675" target="_blank">📅 01:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGN_nZq2XZKPjgs8VDsUg5iuNTE9u1OrqqXSJDTcdMoPWM_hj65Gfrr6RQFJ9tAriYnHcmKvvwnh_F8MMY1UjeIl90G3am_mUJ3rfRxg46ClJY4LVIhCLctye8sN7CzR_Elm9Xb_638nFBSvb-EwWfU5jA5ApPKsphbCKWO_sHItwS8XF_f_Y7HjA7PuC7AO6Kj2jAqnJUSxQYpgv43f7HrJv_NSVCTSUTu-vkgxQO-lZc1wgqEQ8w7bsjuz8uqHsgxi-hNFiHZjKKR4P9PAiRWDCy3FSpfJhH4hIWel1cDtfqhMp4Kb4aA5HXJYUIj54OAvqSNMo9HWyhZrdFct1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نا امیدی ممنوع
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82674" target="_blank">📅 00:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82672">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پدری شاهکار ترین هافبک تاریخه</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82672" target="_blank">📅 00:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82671">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">از تهدید کردن فک و فامیل ترامپ با زبون فارسی تو صداو‌سیما منظور خاصی دارید عزیزان؟ زبونم لال دیگه اینجوریم نیستید که مثلا انتظار داشته باشید پسر ترامپ میان برنامه‌های ضلال احکام شبکه قرآن رو با دقت نگاه کنه و بترسه مگه نه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82671" target="_blank">📅 00:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82670">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نیم ساعت کسشر خالص بود</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82670" target="_blank">📅 23:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82669">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده. اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82669" target="_blank">📅 22:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82668">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده. اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82668" target="_blank">📅 22:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82667">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده.
اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82667" target="_blank">📅 22:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82666">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اینکه هنوز ترامپ نیومده بگه برای آه کودکان مظلوم ایران و گریه‌های سحرگاه عاصم منیر همه‌ی تحریما رو لغو می‌کنم و بهشون ۵۸۴۳۲۳۹ روز فرصت مذاکره می‌دم کم‌کم داره نگرانم می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82666" target="_blank">📅 22:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82665">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ بعد از تغییر رسمی اسم خلیج مکزیک به خلیج آمریکا و دریاچه مرزی کانادا به دریاچه آمریکا: ببینید، ما الان یه خلیج و دریاچه به اسم آمریکا داریم، شاید وقتش رسیده که سراغ اقیانوس اطلس یا آرام بریم، اقیانوس آمریکا تنها چیزیه که کم داریم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82665" target="_blank">📅 21:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82664">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=QBX5yDzMnHXjdbJBxkQmLxD-dvPGRX9I4qloakOhUI9V1Ahd92HrQyWj6yYKVeWC-hqu1dVpSKVtolQ5GQEUGvujmu730W9u_f5CQ1gUCIMTZPA0TOSIaPjTIyVVbs0Gh3kgV88uZBBZ38euzTzEMVEoTJ6iEEzxiZY9Iiy3h_N7MF80dHHIiFs-PnrqXE8S2OjzA-9oqxV-eywU2n2jWMMZbYMK9S4BjFQyB-ukqPLA0HeTYDeasvuHJWAxuDexewChgOxN7REapdK6qAXb4FHvHtkkB8_PoaswZoZIrG9K3pt6spkIrIdqJGR3CvHAmqHQ88DC_Hm_asakrpUFtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=QBX5yDzMnHXjdbJBxkQmLxD-dvPGRX9I4qloakOhUI9V1Ahd92HrQyWj6yYKVeWC-hqu1dVpSKVtolQ5GQEUGvujmu730W9u_f5CQ1gUCIMTZPA0TOSIaPjTIyVVbs0Gh3kgV88uZBBZ38euzTzEMVEoTJ6iEEzxiZY9Iiy3h_N7MF80dHHIiFs-PnrqXE8S2OjzA-9oqxV-eywU2n2jWMMZbYMK9S4BjFQyB-ukqPLA0HeTYDeasvuHJWAxuDexewChgOxN7REapdK6qAXb4FHvHtkkB8_PoaswZoZIrG9K3pt6spkIrIdqJGR3CvHAmqHQ88DC_Hm_asakrpUFtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از تغییر رسمی اسم خلیج مکزیک به خلیج آمریکا و دریاچه مرزی کانادا به دریاچه آمریکا:
ببینید، ما الان یه خلیج و دریاچه به اسم آمریکا داریم، شاید وقتش رسیده که سراغ اقیانوس اطلس یا آرام بریم، اقیانوس آمریکا تنها چیزیه که کم داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82664" target="_blank">📅 21:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82663">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXnWWbwFKg8zCgXFVjJp-VUb18-XCZqhZWg8l-lFwQvhZ22MvXyp0ckIytFt0-d-IoUErLZ7nTw6ZXnPHoKPT08hy3FmxiWUlt110sMcZYwv5HnW_ATM-B-WtdQ1BfO700iHyMx5GQBcxCk6QNeVLD7CPBLKjO4f2tgoe8cWyYXulgbH2Y-hL7K4nEfE3rY9_4yb2nvLrl5VLboOzmGM30g7pQhdmMpWujTv_7fmWkD9D5AVPopRGwxGd0gSJ2WS19CRQ0rBOtTaSAbOSiswGijPv2GxoKaydxFehsbB2QvPToLsXanhO1prPJ-25vvR8N9agLU1zOUbg9zoRZq4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کافه‌ی اسطوره‌ی نون حلال و ایلان ماسک نابغه‌ی ایرانی به خاطر حجاب پلمپ شد.
💔
این بچه تازه با کلی زحمت و امید و آرزو بالاخره تونسته بود یه ذره پول جمع کنه تا به آرزوش نزدیک بشه.
اینه جای تشکر و حمایتتون از یه کارآفرین مستقل؟
لعنت به قوانین سختگیرانه‌تون.
😔
آقای پزشکیان و مسئولین با غیرت لطفا هرچه سریعتر رسیدگی کنید.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82663" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82662">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9SQ1ORCbcgypcMgFLey738MLRGxwJzF0EVSvrqkOCe16BWXZvzAwYRPFWn46U8MAFDFrvF-b2F1jcHHTfkpiL2_qlfAjYOw3aB9QU9QqR-vioKaynpIDK-HtW_Prv4etjVx4Qdqj6hZgZIatPhZKqAQiQ0HpnAeDfIR63Azk_cepNPtalWxfZCcIL4Wkv_2R9wHq-vHsZGTWWk5-qVesgNXEHP5g4N5UPADBmByhFke4Hw04tyIQKoypSIQu1kULBfbfZAvUbc9wzNhF6n1hP50acxDhyKHdEh0HGTYJ-2ng2uJU8Sn8oxFx3ror_mINXfo3rSiDVz2ta01JyUu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه این دوستمون اون اسرائیل رو اون وسط نمی‌نوشت، خیلی جالب می‌شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82662" target="_blank">📅 21:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82661">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShirazVPN | شیراز وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLGFWAPn9xIfiFyRysPFEWsfVxBAJqlkiKXDOYTayL4-DbPfGSQ48pRaRqTb8BUJoqdroAAQlDz-bNxOk8ZMrlhNHtsf1w22BNJaG5IinDi4Jcfw5AxjdhTdFB3_R6ISaZTtCbmvNEPzoH1RonAr0kKgR0npq4qhMPrSyHaTUiiaHePKNdl-3RfBhEctGk3K_ouD43Mz9fDpJxcboHpV0819_qeQ9lms99e8Hvy1bCnUw0-dDJ1I5444JjsI19IYat1s8OYot7PSm0MD_SIxVWFa3uvxMe2eZyaFNB-zEh4GVzhGh1TE8j_AZaT1XCfqtpOS8lD6CxNoFsA5HcAQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پلن نامحدود فقط 180 هزار تومان | خرید از
🤖
@ShirazVPNN_bot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82661" target="_blank">📅 20:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82660">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4gkhr29RpyyXGie7LKX72Z8c0SH5KfrtmBicyqXYLiv6TRrNItdj5qzVhX-0KaeEz_MX8al4tHGiVWeuoTUfzQwefO5IXjMGanNznYKsgd_oKR76GN9VkVqj16vhblJZMrnxvzD19gxQA7KUfroq6ENtowcki4-eyUqfR4Sw99cYaC3E9F0qhYm31GhQ2k0jrYYsI-WLEznjT-D887eSr-DjujpgZfFTUCA0AVg_-I5xwfNL4vjeyVfIuEHctBzULdoKN_VSvNnDcPRxFYNPu-Z82J0XUW8zTsCYOZPZz4zi0HSIQIzCVElHNuJaYJg-iwQ7duemBlxkqTfpOi7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسا خورد به سیتی و پاریس</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82660" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82659">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بارسا خورد به سیتی و پاریس</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82659" target="_blank">📅 20:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82658">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyNnf6SaZGpjoFHcHAY7UUj9uskgftAtebnpskfTT_-If7aqKH1hahhZPozNocOLFZlGp19OfgkYjDXket3mEmSU78YORvwDW6dgiTMysB6DkfcYaSgcEd9c2BW8bZpeDO2DEQ-M905Z_JxWcV0ySOLkSx5ceXdx-v-DADRk2UE83Qx7XayeHmZo7R5GgkitD94ALUdUz8b3kDVCnMrBLmoS6zQiIbnA73MnZO7kRbxFiseFs7XjAkB4PF8idsp6p38_FRHHJF-IOuJTSAUNmhF2R4Wc8NeA0qgWBVtNlDtuRL7soHlgPbeT2G5f-8DgjNWyUjcIHgHFmQzVTXaNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرعه رئال تو سی ال چقد سخته</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82658" target="_blank">📅 20:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82657">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بارسا بخوره بایرن بریم برا انتقام</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/82657" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82656">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plTRX-Q3XJnJG3dtAeiQZA9dyJjXuiHVAr4GbofQqufVIfYjY6SpEEwYtWKPpgbdqVjLamY5Tnyw0IlKPqoDp4oCDoAgnweAATS1JgHIDeZiwrBX_cITZDDY7mVw_aUGVKiQWDp9PS51QG9dEbWAK52F6WsQI-fUlZAPIq6Ja5uEvqcnC5rXLkNEyDc0N2yHJ7O833RxS3uRq4Ajfry17SqSEiGABto4wX4TlqiFJKAxkOEDbJL6GxC3DFztiHmLvS3_o67Sqja0Gx5x8sWpjt7Y7rewy7kY8g3dRPPGIKMSIBWuOToA0a6I3KMqG9L7JxksyeU5Ivsck-4whzCpHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82656" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82655">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17918269ee.mp4?token=EM5JwG7uoMmTVKrnwL1JuIfWTEwId9lus3u7OGRxTAFgvp7oX4lqb9rf1oQNotW2wL3xOd1RQAWd9Vq0Cd8tbiE08QN60Besh9O7148efiH2hCXWKFnom-bPK-rZVFo3alswqoC8AToJVBSjniBZ86dcocOF3fyfB4QUrgO0uRCrq-Zqvk20p9SFMdpd-kqxwoThUl3MMb_Iltz1NIo-DB1NrhszR8wUeqNv3YeWsZnpkjDpXf9samcRQPQGlsyIODExPFpgCBdIGA1IJHCvlGgdxKcVQqlJ5WlTw4B075zOb8SZ4Gxu82hI6PB2A_nuWkkM81bwoursRs01u-ALVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17918269ee.mp4?token=EM5JwG7uoMmTVKrnwL1JuIfWTEwId9lus3u7OGRxTAFgvp7oX4lqb9rf1oQNotW2wL3xOd1RQAWd9Vq0Cd8tbiE08QN60Besh9O7148efiH2hCXWKFnom-bPK-rZVFo3alswqoC8AToJVBSjniBZ86dcocOF3fyfB4QUrgO0uRCrq-Zqvk20p9SFMdpd-kqxwoThUl3MMb_Iltz1NIo-DB1NrhszR8wUeqNv3YeWsZnpkjDpXf9samcRQPQGlsyIODExPFpgCBdIGA1IJHCvlGgdxKcVQqlJ5WlTw4B075zOb8SZ4Gxu82hI6PB2A_nuWkkM81bwoursRs01u-ALVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داش علی تو لیگ عراقم داره شاهکار خلق میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82655" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82651">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWHxFW6rKs0eYhk9Di_SmKnHrLI4ju28XfS4SYMtKiFYgBBOJgePuKvgpZWAyXtcy0H-EevxXs15EXy3AHrfLnC-kPsn9e-uAurJ8LnEbD1yhTuQnmV4nB2Mrl7T5nOJaAVq3oJQRcHwvgPzjRbJpN38Tcdl4UM16FR6BCiKS0AZcQyCpmtpxaJ9_abArzQBZeqn0ngPLgvW7meB7FLEvj4hk-_y2JCKuIF-I67r0D6KVWBGH7S5XgQbO8T8THrMF0Hjdvu8KQt1IeNE-7fG3mdM_UCAYtKmkXmGJv4GC1C-QfCdBqqN0HtNemJcWKq3jlWwZ5f5PCB1N5-srIhNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این خیلی جوکه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82651" target="_blank">📅 19:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82650">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">listen to demo</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82650" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82649">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jpxx-1A4K2fAF_Ta_GD5P2ufzmQ1Je7Y0VgqXryAdXxO5npt2SAufKWianK6X2mi2obOs8x_3lJiwtbIsRWoHSRT6cl03FbV6QdMDu9OlegU0BcCQi9QXXL9ni0QY1u62ftJL9XV_9I-N_02wMx1Yjyh0zMB3282PqxxxBG7IDbasyE_kEIWRXOV5Yc2lYcgV-O2-RZEb-RnA-9su0qO8LTfvRQgQQyuL15yfidKkKnjQycMXGDOaqaxOsUVaFd4ibspZb2mq9inpwtM5dcQ1gOXuYrOorlcL-CzZghKkUiINFGF9dYA6ED3dCDNIwwmBqqJebcMMzWvsP5OHMX1zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید زبر به نام ثاگ لایف با همکاری سعید دهقان و سیامند منتشر شد.
SoundCloud
🔸
Download
حمایت
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82649" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82648">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6cb16ab0b.mp4?token=SGOzA_R79ozxqTMsS4WdqgYtkYpDEzMtNxzlMZBVycOf_TkLG7idFQ9ZbIju5rHO-OyqhuWUBW3xDemfVpuWTLXm4T09s_Df0icQq0eDAA3MjVc1eFxTf-MNw5B7PiGvNHWgoXhxjr-mVSGBPwt3ha1JRvosLoYLerTJswkzsetgyNUfTMHhN9B94h3DwE3_zmom4bijax120LPUFlLoP4XxPddBek_DNDRJkKs9_bs3rGEw9SN3MWr0O9tWznBXa3iDHlyfiU6Sy5RXW_fIlWsnnHCDJyNbvIrD9jCuVmJhW7-l5OPzi6oAQk5acFjM46OHvE_2vjrrGXJFMfHcIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6cb16ab0b.mp4?token=SGOzA_R79ozxqTMsS4WdqgYtkYpDEzMtNxzlMZBVycOf_TkLG7idFQ9ZbIju5rHO-OyqhuWUBW3xDemfVpuWTLXm4T09s_Df0icQq0eDAA3MjVc1eFxTf-MNw5B7PiGvNHWgoXhxjr-mVSGBPwt3ha1JRvosLoYLerTJswkzsetgyNUfTMHhN9B94h3DwE3_zmom4bijax120LPUFlLoP4XxPddBek_DNDRJkKs9_bs3rGEw9SN3MWr0O9tWznBXa3iDHlyfiU6Sy5RXW_fIlWsnnHCDJyNbvIrD9jCuVmJhW7-l5OPzi6oAQk5acFjM46OHvE_2vjrrGXJFMfHcIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82648" target="_blank">📅 17:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82647">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82647" target="_blank">📅 16:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82646">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82646" target="_blank">📅 16:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82645">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b53927e2.mp4?token=tY9vBQWowAxo0LDTfwVq55XufBX5R5L8fMkrp2EpNeizp-vTaIOkLBkqcckr98I7GcqQ2OIg3dWFjLTFlTT2_o3R65epaFHjMNpoqN5XpM8tCsACOO1x_rSEAy2vo0L4kw3Z-zDOQhjlpxDKwJfjCn8j0WffvUIMALxj8C483C2EUFnwNp8USLoo8OeK4GPN_TkNwiRqbse8thjXEqImTB28GAekH4v4kGaIi_6Ar66nYnHsn4H3eqQj9XF8KcM6ZDUNEW5cNs8-rmOkeBhW55i53zok2WRWTHiiETit6f0NBx4FNVco_EHKQ2aRm45HnxA8MrXiWD9ZDS04zFd8QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b53927e2.mp4?token=tY9vBQWowAxo0LDTfwVq55XufBX5R5L8fMkrp2EpNeizp-vTaIOkLBkqcckr98I7GcqQ2OIg3dWFjLTFlTT2_o3R65epaFHjMNpoqN5XpM8tCsACOO1x_rSEAy2vo0L4kw3Z-zDOQhjlpxDKwJfjCn8j0WffvUIMALxj8C483C2EUFnwNp8USLoo8OeK4GPN_TkNwiRqbse8thjXEqImTB28GAekH4v4kGaIi_6Ar66nYnHsn4H3eqQj9XF8KcM6ZDUNEW5cNs8-rmOkeBhW55i53zok2WRWTHiiETit6f0NBx4FNVco_EHKQ2aRm45HnxA8MrXiWD9ZDS04zFd8QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو برگشت ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82645" target="_blank">📅 16:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82644">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82644" target="_blank">📅 15:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82642">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gj1cS5RbqTt8a6MA2_uHrVbdPLRCSAxw06-l9W28U5zLJ6YbUrdnALZpG-E4e_KxXNgPnjsTCOq1ds2OZbIFJKWaofnvPWdEde-1CbNDinQTAuy7s8bUNeoq0pQSQm4V4Vrc7jKJLnP0WDI0wLcSb_SheKjQhO5zws0XX_JrUdr41bekP0Tkt4ZXsEbeGKa0nre21uKQzHetyQd62cYWq0sxLZCkueDN7Cq2YzW1wZ5qVymzhsko_xYrsyCkl3r0xQ7V7VxdpIkOIIdtu8xQIQdOGmsCJuoGMr0K5kdpyuoVRfhI37TUb9dRieZ_H0OL2DBiVIZddR_N8nkblwUAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqCauLAHLv2G2kOoff4OMtOM4W_qZQ4VCdO1sCVa8KWjv_fSIK65rj71RsS7Rz_RV_Jzv2kf66uDZ3OpA9XSClblInZUWWX9ntTlDy2g4XXI0beP6y-gSb7uyAH5VM6r3kkl_PPU5MNmd4WxPJWmQ0up7ZEUXqSfWCSGt5yrFjIFodQ6QRyEbFG-7IIPgLJtFDrhx54LEusK27Tta9OThRMiMWnvf5b17PBo3j1-t0NzWj9cmh8Ia4M21yjrgu7kB-7uvmbB6PRUK8yLlvnfqcXSJOE0157eSJhq-TuhMe14rRaIf0KndIeVjYoQTin_ZcgX-ZCe6Z0qZ82W5JV1bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82642" target="_blank">📅 15:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82641">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d8214fc7.mp4?token=pU-c-20iBEGlfB1VBNdbfT5uLGQ64IAJz3AISVeHKTt2BWZYyvg9_i_EV5-heiNyXrYd2-jGdwBMWBTzpWsK7We8ejyW8mbbWP3g3UuvcrUI2M0ZmFT9x_kJpLeiTpvZyV91JncehlgdpMvajBeJzmL4QV_aSHNLWqedX5ruJmY7JnvXWg4edH6V_slvaMAfCzWzRjwr1Ao8GnDt6ALocWSAmzS-FE2bkeHa0X3LAHrtqmJGJiIdjVkzesRi2Ij4ZYIY9XXjpbvapFjOWup8EwUlyilyGO1KEaPS-00IOJWAmEKiERLWDgxjDN2ZBCcQdCFmnAAQM7AATGbSs2Y0gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d8214fc7.mp4?token=pU-c-20iBEGlfB1VBNdbfT5uLGQ64IAJz3AISVeHKTt2BWZYyvg9_i_EV5-heiNyXrYd2-jGdwBMWBTzpWsK7We8ejyW8mbbWP3g3UuvcrUI2M0ZmFT9x_kJpLeiTpvZyV91JncehlgdpMvajBeJzmL4QV_aSHNLWqedX5ruJmY7JnvXWg4edH6V_slvaMAfCzWzRjwr1Ao8GnDt6ALocWSAmzS-FE2bkeHa0X3LAHrtqmJGJiIdjVkzesRi2Ij4ZYIY9XXjpbvapFjOWup8EwUlyilyGO1KEaPS-00IOJWAmEKiERLWDgxjDN2ZBCcQdCFmnAAQM7AATGbSs2Y0gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82641" target="_blank">📅 13:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82640">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1O3oIFi1eDyMcK0Hm20OOYyILh9o0Dw1U6g2WiOzfAHxPSxAb4An6rSntMyea9CwhWQ4oR4xTDoKAk5Dnva57wAoUoncs7enNYSLE1uyv4voDanYXGdB8TleOOCM-CQ32rujm3s4Z1_hpD7UelqqCOt3uwmEHm3dGeEw39QKC_KLpB3VNyI3zGSRzDCojpgo8npdJYh6Sw-a9COUrxQ5s6Cxvo3zxBDdrOD7_u9APIRSPu_zA6eR70mDXtcl_OpRnAbEQ8MRxT3ahV-81d1h2pR3rgymCtYEemUQxqvrhyg3DUf_MiHMQpDLz8WDioA0lBNnxG2igGMmEuAEdHX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی این که چیزی نیست، پوری سه ساله قراره پک فیزیکی فیل رو بفرسته برا خریدارا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82640" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82639">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbgjNzfC3Z4LnBFwMo8qcSNoLzzXaAAG7hVAfu1cWa-Ch8CAWYfxoUc8Xm0MU0LhR7qo94N61NlvUlTHALS0VGjwbDp2AjO4oGM3iiHhi6dfPl8P7gjQ-TFh9cQZrslg_7mTFhjPMJGTPgfKyExsElvEPZGXsA0TgWP2JAuHiZWtLRaUE4AmUtYFx0vrFZiJF8SoYrA6YkGb8RO23mXeJt3cj_0SJ7vbg60Knd1NUJKWcJbqH8Jdt0eedDoCmvwhUSiBD6z_OtvsHvr0qNqpbCkGp13KZukwlkyUU22Hl5eAREGmomPoZSGv62JyYxdnmCumQ0lwbDkElRnt-gnfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا میدونستید راب استارک تورک بوده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82639" target="_blank">📅 13:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82638">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سبک جنگ اوکراین خداست، اینطوریه که ما که چیزی برا از دست دادن نداریم همچیمونو زدن هرچی دم دسته تو روسیه رو میزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82638" target="_blank">📅 13:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82637">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آلبوم جدید ویناک به نام "Concert Type" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82637" target="_blank">📅 13:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82636">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOqVs8zzOxB5KjVxZ8XE5SmX0r2knQFSxMTb6xaBSGACANpj58Xg-VfjVQklCmrvKIriMFPKf82RlR4k8XnawtOBbHCFGd7doaW2oMLpTuUzmNcbC9_9jdtoLDHvNIaeTCEl4Yrt3o3A6Guu5YD1P0zG-onOCEEmFO-2g73TU6an5rwfmVTn4VSPoWkpyissrSFC38hYpOZKH-2WiEUcBoTM_ySPyZStFU8k7qAbM7GlXSUTC3N2I2B1BWXOraCVFIzpP6_pzIDcxcJecYs4l8vjBKUEAf9w_3nCrfSPXrY27nIkdcR52ReVLBo-fJMyngYnoMwNYRE0_N_oK76pLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ویناک به نام "Concert Type" ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82636" target="_blank">📅 13:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82635">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خدا برا ماهایی که تتلو ۹۸ رو ندیدیم محمود ویناک رو فرستاد
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82635" target="_blank">📅 13:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82634">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d048ddd9f1.mp4?token=f_Pq7b4UBrkmq2jKVSkUq43Tezww4FBVKRkmmf1pDrBmgWtijYMAE3qDFwaxFH7YPS9TSQm_K0qmmaocg6_ojEmUQmkpU5QZugcEjT-k0cBgAwfoCgH385jtFcW-Bon02d4MAWghxQiSV6DxdjddOcZHBdKIk4JcWHd9zeaDEwzKf84uilCO-v93Y15feCgv9uUrwlxSSCTZTNPkF4Gwdpfvlf2CqOpSDLXHstTKkKs-xOMEHfF-ejKtpxqbeofFO2pxFRv55CMsviLqQixDYRH2MWLoWFdxRIqkKZbL-RHbzLtduc1SlFBxnkR91YwYoOX06OTmHHMM8SMHVvRt_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d048ddd9f1.mp4?token=f_Pq7b4UBrkmq2jKVSkUq43Tezww4FBVKRkmmf1pDrBmgWtijYMAE3qDFwaxFH7YPS9TSQm_K0qmmaocg6_ojEmUQmkpU5QZugcEjT-k0cBgAwfoCgH385jtFcW-Bon02d4MAWghxQiSV6DxdjddOcZHBdKIk4JcWHd9zeaDEwzKf84uilCO-v93Y15feCgv9uUrwlxSSCTZTNPkF4Gwdpfvlf2CqOpSDLXHstTKkKs-xOMEHfF-ejKtpxqbeofFO2pxFRv55CMsviLqQixDYRH2MWLoWFdxRIqkKZbL-RHbzLtduc1SlFBxnkR91YwYoOX06OTmHHMM8SMHVvRt_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82634" target="_blank">📅 13:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82633">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عجب چیزیه پشمام</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82633" target="_blank">📅 12:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82632">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ویناک دیروز اومد گفت این پنجشنبه ترک نداریم
شاید فک کنید خب ترک نمیده بالاخره یه هفته، سخت در اشتباهید چون آلبوم داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82632" target="_blank">📅 12:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82631">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ماشینا شمام تو تک استارت روشن نمیشه و بخاطر بنزین بگا رفته؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82631" target="_blank">📅 12:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82630">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اگه پولتون زیادی کرده بیایید چنل بتم باهم بگاش بدیم:  https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82630" target="_blank">📅 12:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82629">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اگه پولتون زیادی کرده بیایید چنل بتم باهم بگاش بدیم:
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82629" target="_blank">📅 12:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82628">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبر خوب هفته علی گرامی و سجاد شاهی آشتی کردن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82628" target="_blank">📅 12:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82627">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ff60b305.mp4?token=LG2oEuGQO7v1rS69wX5jeOc3fXKxFOwIA7h8irwnA0dOdqaz-wWwQFkJeRrm_i6DiZDImGZo7v6x_tYe2pcuhPMFf7ymUTMRDNiQHBSPJD9MqL5wv_D4sTZnZB9dj6R6q2B2OqpvBeDtmWa01ahMpa3ZDKgJZ8-rRLTtcv3mVQHZN-2LbjhTUPLvRxfvvxWKTk4WHeoLCtC5TGeBfCLigwFTN1jGOJtqE2fmF1jsTJ5CibIsGGPBjvjdpDX1K7dz775TLZ9-4jukKjPisLaua-8EEKmiwwjMOBhYgMKQt2Uv1pZuFSEU68yY2ZpTBf4zJugus7Uai5ezBtKscQH7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ff60b305.mp4?token=LG2oEuGQO7v1rS69wX5jeOc3fXKxFOwIA7h8irwnA0dOdqaz-wWwQFkJeRrm_i6DiZDImGZo7v6x_tYe2pcuhPMFf7ymUTMRDNiQHBSPJD9MqL5wv_D4sTZnZB9dj6R6q2B2OqpvBeDtmWa01ahMpa3ZDKgJZ8-rRLTtcv3mVQHZN-2LbjhTUPLvRxfvvxWKTk4WHeoLCtC5TGeBfCLigwFTN1jGOJtqE2fmF1jsTJ5CibIsGGPBjvjdpDX1K7dz775TLZ9-4jukKjPisLaua-8EEKmiwwjMOBhYgMKQt2Uv1pZuFSEU68yY2ZpTBf4zJugus7Uai5ezBtKscQH7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوب هفته
علی گرامی و سجاد شاهی آشتی کردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82627" target="_blank">📅 12:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82623">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZ5qvwXo8hojzmWy7U2Ky02y8b0j5C6tj_SqKlxWoEUpTCY9paPxMxqZUeRl3zzIEHeZ3iCmWGDMHhOYYVT2l6eTywoXlKkv-exMJaxwi1cqszypn_tL2zf0Fuq9Qb_Fpe7K9Ln-cw5X9YQJtU1pRVMqHF0rjTcJoQoDsjQAtVwBNt6gKjZCW62NWy_5rWrbzpscwkvrzbIAm7Sv9R6FT4yTqSkzK28sznGoYPuWpKUHE3ATG9yKX9hS0lTKIX7hxhGGajfIwlH7yQNsa3tsPNcwMvmBQiFGyQCr1lPG2_VZUYVki7lvJRhILy5Gpy0M_k2L3FCGQF_oZip1PB2mgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIpkqRhtRU1svOo8JTGLwtHMydCw52hguevxHaRhJdj8qpV8qNZeeBdh7JR6Cj-_pUsB5qI8_zYpANTSv7INnxv4NqwKqruOv02yEQCfBP1lyZ3gwn8ZboaarsRmNEC6kzsaAfB00_ZMXJDcrRv7InvSbypObyVRrC03Th5Y5mpiR6ff6kfH_JcRhkvMGVSoBMW6CxEC7YJPsu79jqRsQ8h5K7n4UBI650znQ_m3uMOf0jVczKn9OXYj3cRaN-MBOIwp1q-DYEXOUTBRH8fWRWLX0uGChM_-Jqh9MnMKM4cRN0gkVGwpJVxa4zyuf1HtAsPjvmAqh9Y9Uh-d4CYCbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oH-48ZNKfUxRpgeR1KWPMeSoGtxtxIGWJZfOAaCDpeP___Ya33XtTqdwHZAWZ32iPO8VCRP2uXSv6ny_uRxKPTOnklVf2mKdfgfZO3BB-GToFOcrEz-I1Ys2fkR42xDGwdbHMuQ3uPPLhsDEoPDsb7ksl2xfEnCimpaiCNxbkCmSyps005MIYcLIIM9C-q5jZmESbvyV2I3ufOFX6LqZZAyiBzqJT-Q7dQoJjeppMPXBDCbZA9bIAqmbEGCy5Ykok4OiVRcQH68jTiE42PCMDBrZ96-Xhrh_PTLOrBi7YHy3li1om2owd_aZ4H_UciI0H13YU7GO2aUaS4DvB8bNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2nzPz_vJ5NrFuVrHLuFwNKb_DgHDD-HqwwNu4yFXmT-4dvUNNjS5fqpaSymZLrKTKCDLOyMAbC6YHe7l_CRUmCqgegl9WX2hvLS1MbUzOfxX0Niu0Nel8j-4oT6I-Ib23VxTnxxT36Cmnilk_skyw7np0XDAWW66H3Ti_soSPU5UeGPmy96IpRyLAvwJRBeY-NGnwRAcWvXffJg0OTlsbRITTxpcylHRrrabUEZTn6ejroHdsuZuF8Bebc5k4WW9mu3UZCftsabbFxhqkcD97eKWv-fbDrup7aAXwmEbPtVqFzlzUqiVgd9YjKIIXNc528o1zZsyRmAgSJnjSRTFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماجرای ناپدید شدن دختران نوجوان در تهران و کرج
در هفته های اخیر تعداد زیادی از دختر های ۱۲ تا ۱۸ ساله در مناطق مختلف تهران و کرج در حال ناپدید شدن هستن!!
همچنان از هیچ کدوم هیچ سرنخی وجود نداره و طبق گفته منابع خبری احتمالا بهم دیگه مربوط هستن و ممکنه حتی یک نفر پشت همه این ها باشه!!
زهرا متقی ۱۲ ساله چهار باغ البرز
ندیمه اکبری ۱۵ ساله پرند تهران
هلیا عین الهی ۱۴ ساله پرند تهران
زینب سون قوریی۱۷ ساله پرند تهران
آنیتا شفیعی ۱۵ ساله اسلام شهر تهران
پرنیان ۱۸ ساله فردیس کرج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82623" target="_blank">📅 11:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82621">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzzLNNkgtH8wtlU0XpmavkTEIDDE_e7taphTjfRdGry6Z9YW-rOjKJN_Ut8LF3ilCAA2doKWqS7aj9JHy4CZKADWl_JMuc6APskrptdtfAS_R1NSLZ6Ai27-OEgjmW70l3v_e2k9tAsZApRB4UrS-nb9McgLXkz2uOF1zy2Oq-5RC2uKJexflpKr9JVs8JUv4waoNJxBwyUgwl_N397m8QaHQyeHl32QpvAKbHVYGHtGs5NTHVr1co0YvCIPWk0gbQBwpJHfDU-eru6TaAPeJBTFVtPgE0weYsuSxCURoIY5u8Q5AWpGxVZl_U9Vlz8oIv1nO0PTdOLTRf-62VMw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام صبح زیباتون بخیر. 8
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82621" target="_blank">📅 10:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82620">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82620" target="_blank">📅 01:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82619">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امروز 4 شهریور زادروز کوروش کبیر بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82619" target="_blank">📅 00:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82617">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">رئال جذاب مورینیو</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/funhiphop/82617" target="_blank">📅 00:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82616">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY3GTT6X4Ha6jqSoj27ibcBH_p0-nwLAK7mLhfYkHakpL-ioHp75qWKgBbsneufh6raKbFI-f38qgMYbaggiWd9zh-vKQAy8XfKs3YD9cLztlr_aou_FXKypUFHZ43CeJ8ir4cfBwFcYlx_-DwwduUXbkZYnH-J-RVU0MFtT11SbROgppTRJn2tocUMC0k_GyX19Z7KQJJl7kUZuJRmX7Qf566HGF0Eo73jLnL4UVbg-yutENJv-h6whXzyLoKoGKDztKx57IpIKxqljOgqr6ezrD_eAmrYAemxRqki2lPdHli36PwVFfmMZX58HvlPu38Cx5NOxLtq5ebTu6g_VvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه خدا لعنتت کنه با این جوک بامزه و سکسیت، حضرت آقا شاهده که ترکوندی شیر.
فقط دفعه آخرت باشه لطفا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82616" target="_blank">📅 23:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82615">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO6en1CWCxIUvuI5PPZlwncZYZAxPo-NAF1Y3E4OPwtdmlBcOpK1wuGwTWitX9izKoxc0gnnsJP3Zk0T3rdS8m3Y86KSZIq93RHilGjEmlaWeZ97oKc5770J2Oeq31_N98Mw2SIckNCGLzG83Q4f35M-UyqJBV6AKeXUoeIW0GFxqeVuSXLRAvKd0vBNjE2IA9IhDnC-MsNwHATikKo1DKn6-ueNxmYLGAKqyiAeAJWNIxHpNPfJ7FwW_z9o2aEI53fzxIbUtHmeERU7QSR27UO_NSY--Al3BP1q9vBBM4jtt70oRvMov70V43S6vPrwv1KS_ivymjqWckeTeNp4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناراحتی دیامونده از بازی نکردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82615" target="_blank">📅 23:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82614">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رئال جذاب مورینیو</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82614" target="_blank">📅 23:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82612">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cisT85lYso3lVjSIqZDGkF8JCqPuVxSMBsNMGzUqWNgSeXsDEf2jkjgrbLQDnQzjbSEJIPbplpv9EFu0QH6b4kREs-4_xRWKkDcKL_FYEEoj1HoZ9vWmqu_WPNKPPO1GweoJ2DbWK7eXiO7qKAELmj4gyWmNy1juq1ggEzuR4eGuqfaKJfpjBWeG8lREtuILVed3dlPHRvmSwPkXtGgHVey2q-gCsa7ERpE-kxg7xPLDchu6zU5PPAGa3kdkjTWnYghLyrU-_3I5EsX8nBFM0SwORbYksDnQ030BRX8KpfLD4GfUcLDWvXxqZXL1US-63_K-KKIWzgps_43Kc5Vtfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه فان هیپ هاپی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82612" target="_blank">📅 23:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82611">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuNrEeXg81UgxADuz5VPmaGM-hRMGwqvKNzMmfccTka_8KLxiVDH_ytaKY6s2HSj5F3kwC36sb_f0MtOaneYZlHYUm_IzuAPT6Z0Mylx0Udn-F7HYYf8z6InfZdlPat5_AV5gDEblDIrz_KUXm1DBeDjgk39KPGTemZ2WA-RVcepz3Yhxe_0hR0KODQFQKEOEruiC21I2NqP0eMGLfO2PuQn6bh2wepZ8j_gqma_bb3bHIf8i7H825yDw5lkbw9M4TzKHVvG70ynvhS95AprPxGF8lNBXKA5NCokNWgMW5S3g-pieS-eN0aoNaGZsPx-_P3ZhaAT-fw9DtNT9OsXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الهلال از وقتی یادمه داره سالی سه تا نوک میخره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82611" target="_blank">📅 22:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82610">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y82PMFBcv7WXxO9GJpmReuR1jNrlbbr-4xMsXboTg6AT6sgkc6wNIKT1xI1uh6OUQXYX0abRLdC8Tfec4BbXeq90q2ZrFgHey68tO1tfhDOq769Z-EqVUU3xK0lFe2ytOXZD31I_mQ--zQISuhwrKj97e4eH9ZWOhTPj1KpB-J6--DITXsoIs3d5XO-Kas8A2gVcS8qbuJL7RjVnvmydb2dO-zpQ13nYNND-U-Rd38Qau171vtzt1ITsK7Si5XGYVg-oY15cVxSzMD8bRVGxsWWjipki-JNlY2JbsWQrOarhanTQgitX5YnFDymaqEPL8dX34uMeKNmPVk_KWSFNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82610" target="_blank">📅 21:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82609">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_lsX1CCb_mKkOI3KEgUOM88e63CuxKkzdaMv3PJzXla9b_yoa-nzrZjVQyWEYkx_SxndDkWYFXTwhZs1OIac6_sng_KQppSAmBbM-m9HYyUFA5fGl1HvwgpKr2fBsZ0AD7V4WGnh7jPlfIwpCR3AdqtulwUuA-XPQ5QhyGGb0pfQIpGqwCA_2VE9Dd4JgnocjqjwOTM0dFIjtLEq2HoIIwu9kMdlVqN5wE9T-G8SrEkQCDYw3oNGIypkfgTgtGTYNZWsHihg8IHXQbYV1bKNd8i1BCSYaMwZAZwGqXWUZ08nLsQwqcRsuIZLAGJcjNoSlkWx4KdlAVUEtAvXnhMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس یاس چی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82609" target="_blank">📅 19:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82608">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a262ee6c0f.mp4?token=HKS1geZi1d9NCTNRIsDdifyxGnfFw__lwBiHerB7P9UoDRSiEj2Qv4FY1-I-2nEVm2H7e6UKSuyxVmVQ2RQR22cRoqkz6uNWTrSLRsinMQHWBc0kNegXVVvm-1UfBbiTOlLrcRkGpx3Vh2dST3f-ZwjODm-CsEqko02YSwt2LVnRng7QRElmxx1s9ZAfOiEuV2ljjAxDczHpEC_Vk_lNJ9sjmXXjo5F0NTs12A3Ye7eMClq8XZAvRWAosCnCXomeQ_-u8yG-l6Vi0yTPTAV29x0Kc92N8j5jnqdGIgvmJoUY7f69l5hjgsTewaxFV3vj6MGBQTLs3E-zvjHN8o3jPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a262ee6c0f.mp4?token=HKS1geZi1d9NCTNRIsDdifyxGnfFw__lwBiHerB7P9UoDRSiEj2Qv4FY1-I-2nEVm2H7e6UKSuyxVmVQ2RQR22cRoqkz6uNWTrSLRsinMQHWBc0kNegXVVvm-1UfBbiTOlLrcRkGpx3Vh2dST3f-ZwjODm-CsEqko02YSwt2LVnRng7QRElmxx1s9ZAfOiEuV2ljjAxDczHpEC_Vk_lNJ9sjmXXjo5F0NTs12A3Ye7eMClq8XZAvRWAosCnCXomeQ_-u8yG-l6Vi0yTPTAV29x0Kc92N8j5jnqdGIgvmJoUY7f69l5hjgsTewaxFV3vj6MGBQTLs3E-zvjHN8o3jPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوش، نیما تکیدو آزاد شد
❤️
💘
💔
🥵
😱
💋
🔥
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82608" target="_blank">📅 19:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82603">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vl4QMM9oJ3rLlwGd437NhbbF2OQensblZY9cSgCPf9WLdIPWfm2Y8uGEnj67oSfN7J5QXNqqihFDTYNt4z4XA3vzmS8j8ZAdKOLoX8fhBB-NCeCN0XzOrzQYu8H2rhRlMpkTV1-AAq0ef_n2JCj4EZyTrrzkltAaFRnGaOt-Jy_VxnsTb-vzVOg_Yn-VLZsML5fMChZUEhSya3huor_umWgMT9IJ8sAHwciO_C8vE0I9fJI209Oe6K9ZdUceQE3ln4--yZDPPihcHTBbuRYyEHggJbvrMcLsBLQjy8TyzvZJzOM5EF_FVENw3St9m3DjJViFK8KZsz5Z4Wuur-nB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CIYYBv8H_MibvMbUOG0VHOJ5_kVfLv9BsWEQ7CpyI5YiT3WiigaS-pga1e5COH9td4k2TNTp9pPtV_fQNoiBQBE2pw2bPJrtE1OIp6E9rJZq5GtMMz4LKqIpVifrWEXheZtER8B4SH5RI2Udoz9b4rrvBtjjgNrRp0SC-wHDeuUzRgKZD7B02FLeqFNgS0WC60Oe7TNhEQU3ttAU1c7m_Zhg46ML3Q-xsg1CCHcw-3m_uuRUhZEnXm2cCwYC0v8pY15q1UXJEBUPedMTOutlDyj4AsRBG5sNQEvd56as-hOC4G2M6-ZAb9nAzcPerfy4Ic2eRMHgjHDrevUuVkta4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jES86EFvaTo1zxj8BhFDg2UTWFek42Z1mSAxjjRRTp7SX3W0spLSwsHUAsLfic5ARKi22ivOrtGdN1W_j5LQr_3IqX2mdEnHfC4wLUSgRtkcNhdWNLWkjVDTESgv7TJptkl4muALoXIV9SZFe5kYvwrs-UGqh2DrjKTxNaqxqM03Wztok9WqA-C_ppH3GUWdfk3V4tokHpMCrq-A5UJitYb32vaXFBsIbn_G5P6y9tlrrPnziZjweD2HNYoa0SEIaFmmpg9lRFISAcT-zZ3EFY0mfVY9hX5xspIkZXxnQQ6of7O-FoYQSc_J9dleR7o7lSFlGigExqiv9WYi-ZlsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7OfGjswYzhAVcrT1W9_CtGJORgGwysStI-O2MAqWigDffIpFqKhcgstjCioygvpgczm7cZk8qn9KzKX_B9dfmFMdCSwkrlCVN9Irl3MJ_DhX884gfCdqyhpHfKprKFSJH_H64zcpRO6Q4XzYRsWO9CZC4ET_ndVRraZu4bnaTRrV7cqOOEW1zc9JMV8bOk9bbve1QvRFU7SD-rgmcjHnXPhN-FDpVQtPfIRloCeOjAELu_tnd1FT0HoO1MjajiB8UqYwqdSTsmx7KxPiPuexEzvrcx372xG3-f72UArJt219R87C2tCGj1KqZjWfPtKflq9xyHTKg15LVkQvEf72w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d5151d06.mp4?token=G1i3TTvJ-aSf7ueT6om78oI1QVQXXic_xjWiKGbgnxcTwL12EbrcE_TapgBqurKds37M8t5SdR2fUkiaIeGE_BfrZmwOg_W7EhgATHGZGgLh7qm7daucv15_nfJSNQ2McrQfAzmX8vtf2QzzoVhJK4lgx4CVtzMcIRbISBrwfyCM98ip93U7YHqZoWsj5hHsr6k8IeKc1rutu6cWXwwksDramfe_ECriefTestaX0duBmMLlZpV2iS-bQJnqGT93TSPA_UjqgFvG3F4dxwYqyvFYZwC8jHSTSmi9hnu1c_aO3y0JAr7R4svWZUgGVWNprI8h_HT8F1BrzcvN8sVL3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d5151d06.mp4?token=G1i3TTvJ-aSf7ueT6om78oI1QVQXXic_xjWiKGbgnxcTwL12EbrcE_TapgBqurKds37M8t5SdR2fUkiaIeGE_BfrZmwOg_W7EhgATHGZGgLh7qm7daucv15_nfJSNQ2McrQfAzmX8vtf2QzzoVhJK4lgx4CVtzMcIRbISBrwfyCM98ip93U7YHqZoWsj5hHsr6k8IeKc1rutu6cWXwwksDramfe_ECriefTestaX0duBmMLlZpV2iS-bQJnqGT93TSPA_UjqgFvG3F4dxwYqyvFYZwC8jHSTSmi9hnu1c_aO3y0JAr7R4svWZUgGVWNprI8h_HT8F1BrzcvN8sVL3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوش
،
نیما تکیدو آزاد شد
❤️
💘
💔
🥵
😱
💋
🔥
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82603" target="_blank">📅 19:28 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
