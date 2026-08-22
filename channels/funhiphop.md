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
<img src="https://cdn4.telesco.pe/file/arCAShy06VdqPrHH3UjHBF737GlIA4sWqjwjjYawJ1N6D477FoSOyRCCuW05ZYSCjAPLmZ6Kz8FxrmSX_7YKerlJN34CyQ5-AZTz5jNRpK-BbOjjgnyQEx6sU-cLVZIbgxoXD3ywUJez_Vr7nQUIyYsODyJ760JjXXnc_paqcw7FfUsvrO_FUL8tdlsOLICE5a5BZxJVdr53DardWax50nBtWPIeud3fxcuWTFMd3NebKwxYBHFNXlv7TiVE_49HElyZk0H3cbO0qmon0rxB2bwLH6yT9KOiM-pkJPewK3X0juNd2wjE0vZAoBPSDzsS4RhCfwAYhTumDrKHTlMM8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 08:26:47</div>
<hr>

<div class="tg-post" id="msg-82446">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این کصشرایی که عرشیاس و چارتا پاپ خون شبیه‌ به اون میخونن رو میبینم به رپفارسی امیدوار میشم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/funhiphop/82446" target="_blank">📅 01:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82445">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlDUPN4fJYYVNfLbB8b6mBFMZ-Juhko_cgoJz5HHGqY61gVzldgE9TUtB2A-7LlNeyoCRr2ZIHkS52G88Sg_b_pyuJalU8pogFecJRN_Qn1qqeEW3h2aif8wBHcIIx0F8O6e3yW0EL1KMxqPuXWcg4rekXCfVyeOdeEZFhIEku5q2rx1qsNH5mK3MAXLq_BfwT1hQebkoYzSa4onvdm6XgJdTTnwy5VgtCp-XNFVIwyei3QG2d2yOrRId4aZPrjYx7F7LrhuS_cOcLTrwcKDyDkR35Acq8bXsGiK88Avm-hpw-BkD86yn4UQ7VxFQDKqJFTxKLCgNBZ-r45L4AWJDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دوتا بدبخت رو نیمکت آرسنال تلف شدن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/82445" target="_blank">📅 23:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82444">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">از ترند امشب جا نمونیم
صدای انفجار در امیرآباد، تهران
احتمالاً فعالیت پدافند هوایی
مرکز تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/82444" target="_blank">📅 23:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82443">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrVoRiUEYY5w5QGIXS6bQjCtKwMP9Udlv0Aex2XL7lWcjrsKdn4FgeaHUZLixY_3hj2KGhg8MXKTwuG01T52qfi-JD8TkJJaAGDv5IoWUXpQk88A5rX9GQWCe2lS-VActEAi5m4SL7KUMItofaripj-I1fG3bhSbkx0BPQFMQ46j1nTI2FaNxHOUemyYBh58Goo4wBIQJr2i8B2K_X721phNr9PVO1aUpmmRxRWW87XrIFGU6S2DJu2ea1_vHDqPtyijNAg_DtBJY8wTz0wlj7B99BGBHfSOZ2A_-UT4aaZEzPqsMnoGzrkwlu1vzaohXSBzs5quOxLm2IJQ79NZ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زور نزن مشتی جام جهانی تموم شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82443" target="_blank">📅 22:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82442">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8ZCaqDPb6BbqqbtpngXoeNlvZzFWAozt5eOSiGF4LaMDj45pkpM3JJGAYdcT5POiPt_RUyTL0hK8NByG-qdr6NKpBW4-4dCj9nh2RfLuVicXONOIsV1V4EU5oafeieYAypdwKTyn2R29rByCue8u4BsSursMTSwx8qxJtMEnBVukW2JDTdhKvZnF_M-m2wiP2MBJbTJJNu6-ONqOPhtPGuopR-Fo5ph0ivsNYuhFLTc8aH3WggSHg5mi3fkC8vcTWUdVDZMFU-JSh8tQB1gVhnHOoU_Dh6jbqcGNLqhOUDQiGyC9YP2XfIuYb6kFXskcQGNDnv7WJtzuyzLQ_k1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخی، قانون اجازه نمیده کلاغ نگه داری؟
🥺
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82442" target="_blank">📅 22:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82441">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9QM1LrjsYr8zpAk0wqD3NdOV_lIG_3_XS0p8TVHZqy4ZNJm9WFEENM6jeqoqkeIGw1pVkehbW1QhMgykKbXlP3td7Gau6hXvKzWwqUipzsiUserlh1IR4o-mlJvRVglEY59OPdbIA_1MFcrPv808j1j2PvpOMlxLRjLoWG_rxzWjaX1_BkTAPvuJkK9hWW7uvlEXMqIaVaDukY_kzVH6DHRjHikMBgeOBYVcF1K7jEthW2jaX6M4QoJ_Fk39WLW12XtGSjMvDnrNE2IZfIbhEciP03tQQXSbjmNYbCBH-IAZtgTokK6I-DFeT_uihz0i3frCJXiYT2XuoHP__iFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82441" target="_blank">📅 21:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82440">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBgaJt33Y1zFmOOZHKD1JfpkhF97feDDaun8VVnhz6Fr-xwvyyWAQKC5UU_0BJLzsXPqUE4SfuxGCQs0a79FrhjsPV2Y_IQ2UcWP0s8aJPQzBnl5hLTTUxwbfZeQ_QGSyNwsDSmQx1S7XAPL3eD9a1u01kIYkUD4gSxfOoIkkMB_jLy37UGx01Y-kOj5OaeIgiC9DR6wCrLA-hU4E6LH8Gpv_huSNq2rJmjmeZv-61sneyXmOuYc3BJcY7kLCJqisKVc7cDTLNkOkTd6VkfcT8VjYz3JjA3U5C9TziwW6TZ9WCzVgg5i4CW7qTpj8xRI5jiCRMAKEiq2u_1fffsOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی این همه واسه پوری کیر گوزیدی که تهش با مجهول کار کنی، دسخووووش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82440" target="_blank">📅 21:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82439">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مثل اینکه یه تیم خلاق و با تجربه یه چیزی شبیه پورتال و مارکت ساخته که میتونید ازش گیفت nft با پرداخت ریالی بخرین استارز و پرمیوم هم داره
ایدیش
@premium_grams_bot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/82439" target="_blank">📅 20:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82438">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ایده ی فیت پیشرو با سارن رو کی داد اولین نفر پیداش کنید واسم</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82438" target="_blank">📅 20:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82437">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1hjHft7Kzt-JX8wL0JgwRGhAakulQNz1wVv7isvR4-84Ak17fAH678D5_ZSyYCL-P6OOlgUw5fiaMSnnwcWXFt7uzELHMrwKT9D0LVGUwmHY2mmxWF0ei2iKOjJn3y93LOWsAAXWpwssId4AXylW_TX12Bha6NElbqoXHuGDaT7zEsESMB7Y0MtN_aHKQUm3BmbQvFtTFN8zXOwN_FTS1SYxAMl5yx-9PMTvk0J1smlYoyKohOtQFchGpsuqRMH-SEyVgKk9WfehPadY8hapxfBNOXgJR2TWTxzJ-i_5KRClGLxioz8J9DKZdwboAAshc3h-9lZC4uOooDmeiQ7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید این دو تا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82437" target="_blank">📅 20:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82436">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قالیباف:
ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی و رشد اقتصادی نداشته باشیم، دوام نمی‌آوریم
امنیت و اقتصاد لازم و ملزوم یکدیگر هستند؛ اگر امنیت را برقرار کنیم و تداومش را با اقتصاد پیش نبریم پایدار نخواهد بود
ما به عنوان یک رزمنده، بیش از آنهایی که حرف از صلح می‌زنند، قدر صلح را می‌دانیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82436" target="_blank">📅 19:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82434">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iod3yD91zw74ouMFKEow147qeqCVPwOLNyVPoNGEIsEGe-TGTpeKuhEDZksmnKB-p0JKwWnbbd9XTDryGACU9nQB2_bBrOBU3ZwcbgC_0EBP-eCQbfp61dnCHX2nQsr-4t81zapvPtpJtTNgr2owB_V4mFXi8VCcW4th5Xy1pD9oHlrgPgyFxEYPCOevB8hPYVutPqatcbO5vrGEHt9_FMKUS9i7kUS7uHJ3H5hjSf03dbXHL6FlLxfdw0ORppn4hiUO3x29_RScoFLjCDjDVDkEKIBQmBikKbOWCehomYKl_3f7wsBHgoks33Hd-YB14ttynYLaNbxGaikLkZCw8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82434" target="_blank">📅 18:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82433">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یکی راکستار رو هک کرده و داره تهدیدشون میکنه که یه ویدیو میدم بالا تا مرحله آخر بازی اسپویل شه
تا الان هم چندتا ویدیو از بازی بیرون داده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82433" target="_blank">📅 17:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82431">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSsm1LVQXIenjvm1dVlRda0lcGZPe-3oHU2iCKU7d-ldv1jG2_8vW9D0HfxsyIpK-VuKOGe6fOHMkY9FSaPuSkaAJfhBE-GCMwsu-fBNjbJCOtceLCDvH0BxztIkwLAP1k_2jI-vc9YCxzLFR4McYkP4iY7wXtiNjIq8sZGLr7BWEwPuxeA18-tIl8siQG3l3eGTbOOZ28Fl8vkKWuQhJA4j5XO6_LAUUyCM2Aa8Y_tVfSJMxGUo8MQ_m6IrrZPHGHcQqEevM6JxN-TOoc3MO-B1efTWA51EkulR5aJYKvTwBRnw0R634nYaomPgM25ZcuqDcK_aEr-BBa3wCCIaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRJbeQJEo8zIQmBYak0Yqu8zAmg52kLo1afmoJKTHOOnuIkx1LN65K5t5QiD0QN4Z60ejQhvnQ6tulFe0ZxDTT8xyAZFRKdh-59RalcbaTZ80-2dTxwLESd5jy7GfY0t8WYgo5PpqpU0PFhqIw2BjZuIekZdLsgN-PJOXJN4uXt1N6xfnY99bxPkKt4Db2EXmIDAudJg4PbvTuYTn9dCbT7kfX53K-soTMWjrimnHGHnyyF1kmWndCJUD6GzR9iKJkv0-SV1RAF78Izab-5ENiLGpAv907GeAbjOroWjA_PjbUL1P7aUZqMtTTn8NcF5icRtf1hLjTuscP2ZZq-eGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز عقاب نیروهوایی ایران، امیرسرتیپ مصطفی روستایی در گذشت
وی خلبان F-14 و F-4 بود و در جنگ موفق شد ۵ جنگنده بعثی را ساقط کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82431" target="_blank">📅 17:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82430">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCrkofNrT9f3i7z_U6Kxf2VAo8JznlcmFViV1O1xqzFOnJpUuykAkeVJf6CWVxTfpm3o38EZ49whKFrPcZJsY8BDMqqrtr7Hv8OlvdVfm0eugTomBxru20STCEvcWWYNsuqwbCzYPNtA1Rd3W4y8VQRfTfXQgHDhLWPHQx4kpeEI_gyihhHUqlR9b0efnVy4bnAI2xhwMCaXP58oek1-dspiAesHG-5tgbnmgrRbsOfCZovcFPx45wiV6s6TcG63hsVCxeGc8-_wq7rfzbVlT6dkaSOTZ4V7MmTN9aj2wGkxp-KbaLd5Rjh0ag85ZFqo6Il05pp50O6Ss4PtafdyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی ویژه هفته نخست لیگ برتر انگلیس
💯
⚽️
با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته نخست لیگ برتر انگلیس، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r30
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82430" target="_blank">📅 17:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82429">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1djdeXKQ8mA6qV69krXjN7h6OvNbqDtYL0SEa2L6f7p3YJhq0kp-p4cbQVvX1Pa50AtvDtUxK26FAYRAc5n7LGqmrWurFryIo5ypyvu_1zfBmqYRDaezNiXaZ_0sAflxkiAl7mzxJOBXW9mGDPMxjAq0kCT5pSbGfJVHBE8oSM9eJeaPaWZqWvXMvbX5IfAdfwhtuNiQa0Hp9infxCZZReRi8p15DrvBeSZP6O6zXzwUTw2MYhfZYOgakCG6y-_V7iZHeTGHVqYQGu1RI13p1nB2mg5StwkF07nNhU_udMJyPIrZRKhpQmOCX6S1Jap4dWOHQvSnHV1cJ2Tj9xh6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالا مادرید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82429" target="_blank">📅 17:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82428">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82428" target="_blank">📅 17:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82427">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b51c8c227.mp4?token=BwyAZFz0kDeWyGT6oUBct50hnn3xZm-HMpl_52IFW43NQ1CWD89taoUa1c67jNc8e_gHSrCnREiAtFrBOf85U6ubkAHBrrQE-L1uaceOboOzleL9SZfJ87cIvwDD_PQ3Rc4ro3OFt4xVH-Xgo0oSM-PhwZghErWXSAg0HSmpXhGiOC0HTGH_8C_n8n9BuhFxQp8a5DbMtoYP3v-SiAd4l6wIJH7E1rXeaLLWGxJTN4KPGMn8PtmSW3LQw-1n_1B9dhWPyQ2e4UJeg9v4zfmPri_NCWmOtOUNCVL89MS5CLK-MuLRWP-pciJuz-XrcR1Ph5s4cGZ7-i4Mq_IjciD_Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b51c8c227.mp4?token=BwyAZFz0kDeWyGT6oUBct50hnn3xZm-HMpl_52IFW43NQ1CWD89taoUa1c67jNc8e_gHSrCnREiAtFrBOf85U6ubkAHBrrQE-L1uaceOboOzleL9SZfJ87cIvwDD_PQ3Rc4ro3OFt4xVH-Xgo0oSM-PhwZghErWXSAg0HSmpXhGiOC0HTGH_8C_n8n9BuhFxQp8a5DbMtoYP3v-SiAd4l6wIJH7E1rXeaLLWGxJTN4KPGMn8PtmSW3LQw-1n_1B9dhWPyQ2e4UJeg9v4zfmPri_NCWmOtOUNCVL89MS5CLK-MuLRWP-pciJuz-XrcR1Ph5s4cGZ7-i4Mq_IjciD_Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوشبختانه خبر رسید که عبدلله امروز یکم ریده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82427" target="_blank">📅 16:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82426">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
دسخوووووش
باشگاه خبرنگاران جوان: مدیرعامل شرکت نفت ستاره خلیج فارس استفاده از متانول در ترکیب بنزین تولیدی این پالایشگاه رو تأیید کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82426" target="_blank">📅 16:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82425">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJquwgfa3m_I13VOGe22VTRCt2FT-cYFvAQSfenztNIw32Y8Du07uNI83uRc9DW90I4CSxe8UundeBUrZ48kzLu67_xiBLmsx66y8wAOXVxSCPjkrbIIBZb6N6TLAGngxex-DKzUafI349YbjX22LtAOSPPfR2AdYRgTLoc8pmad6D6vEf18_vrQycJl9DlIWxQK1mEIhPMabGsuosbGil11tnaOF-gKxC9M5lp89DEJAxBWwUQCo8UPBQijDJ4KmQr8v6rNDjzJGdD5ylM7Ehic_io_3aNqgyPVz9wwhgMPvn0ljBtUc5x5CxsHfubLp0joefjENqkSg-LRftoUew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کدوم رپر میشه ربطش داد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82425" target="_blank">📅 15:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82424">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پزشکیان : جنگ باید در یه زمانی بلاخره به پایان برسه، بهتره امروز که در قدرت و عزت هستیم و تمام دنیا باور دارن که ما توی این جنگ پیروز شدیم و آمریکا در دنیا منفوره، به جنگ پایان بدیم
پ.ن:
😭
😭
😭
😭
😭
😭
😭
😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82424" target="_blank">📅 15:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82423">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCKl8TbtNZOgu3EeUkKnEbovSsHnGatC9n3GhaGBnK4_FbdRvd4SYZ1laxhefG0FwIdZ_2G_Yq91iIzEMKn6bEeruKmAQH7n38LVyHA5B9uXwvR1EPqWfTRyjuOLFXLeNgnL1fe5THlAOITV2CKg9jrSej73FIVgQ0Wug_9Tsyd1e6lMj84ewMax2BeDaztpzHCEOKvm9gihEeUlSmSMjjByUgnDa7UtKh7to6RX5U40apu8JbUIvQwM3LqGYeKMs2fLrQiPmZh1RXIm5kXD_DaIpYR94Jq3D93oLhNlfJr_fh4h3pGfaf5YlGZVHTmYb1BW4wo2aRhcNUHolC4XOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82423" target="_blank">📅 14:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82422">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کنکورو چطور دادید؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82422" target="_blank">📅 14:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82421">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyIfVmU1Up84LmAJLlXeSzxYt-3zBNGEc54NiwPhG9fgCEgY7l21t7BHqfzxwWtBIIan2YNfZjXYsequRgTJ7nww7XcYMwt2iqTd6Wk9ZDFNq5iDifED024CiF9Fcpofvj5tsKgw9AGe6bBYf3ZzPmEYP18mpydWaQIbM_tsKp_VQ4SjOt3oNdU3TJpLuOpSP9u_9c-peiHu7WEyUspIZIFzhirM4MAMubI8VoNzY-9Auw1O5hzTc1Sk3nWzvE3NH-iTqLKvR28_6Hy5xEsWOqCiE0k6nHdhR3nRe3L1f2wxzEFr3w6fCXT8rYxCDQA6btxeyCxLWXPoXBr4685foA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پیشرو و سارن به نام Mirrors منتشر شد(لیک)
Download
(حمایت)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82421" target="_blank">📅 13:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82420">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwyxlPPAPNERuBeD_KIbnV2LyO-u_9QLSnBPpRi7w-ONq7cXuSY_ELV0beN01AHzYWvyMEkCH7GKDU_ZkxDzAg2ihDVH5rYhAK0zDZWwjJcthEQ2kyoM7dnI4mal1_4whGNXT7S0N069PcsE9dUTVh3MeWZ8K56EqMX_rVTc1zrvEKtcORhZPQJ76gYc5H3PpN6-bNV71hHzUfRiKMg0c8bcM64CYFnczYbuUtHkM567HjJ7ZVqlip-NFd-t5acH2z_MQC5y1zWCRcC5fnHkvLVWBLw5s1pfjzeRJtlfS9HtUC1lPRFl0ba2FhexlklV8Nrr39XczBokNdOPzfYmSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من تست کردم مثل یویو کش اومد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82420" target="_blank">📅 13:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82419">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عربستان اینترنت یکی از استان‌های یمن رو قطع کرده
حالا تسنیم اومده نوشته اقدام ضد انسانی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82419" target="_blank">📅 12:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82418">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=LFD7NUwMjuzuPPY2NU5auaOHIqkLLISn9TUy173XVaY5kr0M95NaT_Ly0O83k-SZ6TNarst3r2TBshfEuxo7sHrL8h4kU-7zMPDMIJj94OC5l1I7un_53xwvyS5kCGpElxiMByOcVbN87ePq72MlIyL_G6Wh1LobyBIaHGZKsqN_3d2tFUzwnezzCOy8ufuX4Ydf8DivBAznUPmijxB-czQigQZCrBsWSiMgK8MRigAjgb9HQoAGg2So7cMavUaQmaUpzqyCX7uShI1HB0NDdGM28M2Xc8FAL-7CoksuDSmjo163kKtrPD7NtOcDcLMPwaxyhfoDO8BXyH3KDHX4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=LFD7NUwMjuzuPPY2NU5auaOHIqkLLISn9TUy173XVaY5kr0M95NaT_Ly0O83k-SZ6TNarst3r2TBshfEuxo7sHrL8h4kU-7zMPDMIJj94OC5l1I7un_53xwvyS5kCGpElxiMByOcVbN87ePq72MlIyL_G6Wh1LobyBIaHGZKsqN_3d2tFUzwnezzCOy8ufuX4Ydf8DivBAznUPmijxB-czQigQZCrBsWSiMgK8MRigAjgb9HQoAGg2So7cMavUaQmaUpzqyCX7uShI1HB0NDdGM28M2Xc8FAL-7CoksuDSmjo163kKtrPD7NtOcDcLMPwaxyhfoDO8BXyH3KDHX4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسره با دوست دخترش قهر کرده، دوست دخترش هم برای اینکه از دلش در بیاره براش بنز خریده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82418" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82417">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فنای پیشرو جان جدتون دست از سر این سامان ویلسون بردارید، از وقتی یادم میاد هی داره تو چنلش میگه فنای پیشرو بیکارن علافن بدبختن هی به من زنگ میزنن مزاحم میشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82417" target="_blank">📅 11:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82416">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f89bbbdd.mp4?token=jxEOmg6-q0REadiE29oL-NpZEZbYen5EdsC_fMlEBJ_gCAk8ZZyOGVCIT6QG3JueTXNTLQduiwIXWGYSdgoe2-dDJMSL5IAv6o8SscUzemD5LMQgxs5a8RhuVX4DKozfwFQ18K_4JkqZXaVCtmkakz0RCHxYaXgstBclOs1iJG49ypRdX63L58azxHdKhj-UvVLWowVN_pc8wznWX8s7y9WwFkVFn8a_TAvWtIn4DFPa7URm5YQv1Wsw_z0e2i2LmnxwYWSx8rR_fMy8c1zBoT1ejTdwzShHLJAWkjMsZbeFCMpb5CCo0BldzDy_opB0WI6veYI0lZuDqKRQLymPHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f89bbbdd.mp4?token=jxEOmg6-q0REadiE29oL-NpZEZbYen5EdsC_fMlEBJ_gCAk8ZZyOGVCIT6QG3JueTXNTLQduiwIXWGYSdgoe2-dDJMSL5IAv6o8SscUzemD5LMQgxs5a8RhuVX4DKozfwFQ18K_4JkqZXaVCtmkakz0RCHxYaXgstBclOs1iJG49ypRdX63L58azxHdKhj-UvVLWowVN_pc8wznWX8s7y9WwFkVFn8a_TAvWtIn4DFPa7URm5YQv1Wsw_z0e2i2LmnxwYWSx8rR_fMy8c1zBoT1ejTdwzShHLJAWkjMsZbeFCMpb5CCo0BldzDy_opB0WI6veYI0lZuDqKRQLymPHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخت و پز
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82416" target="_blank">📅 10:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82415">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfHRjkN-aK5_YrmAazEhBmMoFe6otsh5T_PdZ6cbCaXutrgeqTP3fFlaV0kNI-yW9EE8XHtE-QFr1ozjjnuQQwDQi0kYbrYrIc2FtBZNQlxJWISSBmt35KWXHvO3WnDzzkydxZCPKRN1zbNlpCAy7Nhs72XGvZynFq__IfH3mVz42uMMHBgnthrL3q9xwHOAdEvgj6uTsY7k4JjbSSC6-4iEz_CwreHADdgWs3EU20iF5Ya97Z3BPHsMLkjTtfKb6FfuKiLUPK6Lb5VfUYl3HgeQ1-yTR1yzyHu19VUGe2qkdRdlL-LvvBHOeW8GCIaZcPGXszJcOGvKaZwEXjEpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید آرتا و سمی لو به نام Azizam منتشر شد
🟢
Spotify
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82415" target="_blank">📅 10:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82414">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBveRT_9zEO9YMXe3aZNhYsGExqyXBMhtLTJcXA4x_F-g13vX6kQ0Kx7yXmkXORMRSnWtLZUI462EBcsnX3c0rLwY8sD__OnqGACTZlZILgNFNtyFUVV3IKtSWXjK_69ttqFmuohhMNseFZ6JmgwtoSiMPc_-PS1Yib-toGNAUIBh2FrU277QHaTYireFyrjdqQH827OESmjmPMNjskQezMKyKHiZFgTZIJeXUFMDefp0yNAF9djrbXILJIEFzawa4D3HL-loeo5JegqtmY38v9W2D0M7wLNWJ14fi8bw1RvTND8jTBKD8bDQpyo1A9hRctPsF0PI89SNiTDu7IA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی ویژه هفته نخست لیگ برتر انگلیس
💯
⚽️
با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته نخست لیگ برتر انگلیس، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r30
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82414" target="_blank">📅 10:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82413">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d570e6ef4.mp4?token=McSRIdgsTodJYrZpfnxq0zwb_lVx-q8IH3JerA_-nqmdSOCsRg1CO2hzWscYTdBJ-36OhTJ-wwfncyBMEMPNj98Jlq6zi5cew_be1FsuX7wP2WPoV_UjlzSfDiA1nfRC2ZZdfoHi4jGfzfRPRfzI4Yj9VDL32UVhOr6YoUUkfQltYUQSyjcpKNRyjYoctY551yyJdnpPps173uH5EzQND_oih6XWh-s4tonbH-0RH_Of34O_Mg3cOSUXbcYSjwocMX0MvfR_1RR6G8F7wDIhCFqfSHXaHep735QRSoIEXmOEZr0D3-lQcXGfzHFVLBROJCo2M9s4MFLHkOGY5HdUnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d570e6ef4.mp4?token=McSRIdgsTodJYrZpfnxq0zwb_lVx-q8IH3JerA_-nqmdSOCsRg1CO2hzWscYTdBJ-36OhTJ-wwfncyBMEMPNj98Jlq6zi5cew_be1FsuX7wP2WPoV_UjlzSfDiA1nfRC2ZZdfoHi4jGfzfRPRfzI4Yj9VDL32UVhOr6YoUUkfQltYUQSyjcpKNRyjYoctY551yyJdnpPps173uH5EzQND_oih6XWh-s4tonbH-0RH_Of34O_Mg3cOSUXbcYSjwocMX0MvfR_1RR6G8F7wDIhCFqfSHXaHep735QRSoIEXmOEZr0D3-lQcXGfzHFVLBROJCo2M9s4MFLHkOGY5HdUnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از این لحظه به بعد کیرم تو استقلال، ملوان عشق.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82413" target="_blank">📅 09:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82412">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB7fjGW-I9jf2kljBOjxhc2mb8Yziw3-tIhExHwAbyBAUcymiZ5is5lEsG82c1Kue5xOBsrFSH29Jm04KBEs-Sc_Bo4XsP_acKib6tw_K56QGYxaSM7wCZv4epT6Tbn8SR0FNpUozyhRKlJ3MW9SkpEPYXYHb9RmoaNoQi8Tykzk-gq1k9v4EkLj7cutYBWtPT4OsEjACUNZ0mwC0WYpLD60GdxtLbIWbM2IONwuqYaoX-muxWfnWTG2iBds48-bqABtQmv1Z2v8YItxO5snuZE88TeBSYm2O8rL5CWsH_xW51lSra5IIdj0396ThbjvBSz_0oAljl4uKD85D7vCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارسا یکم بی ادب بود ولی بیس حرفش درست بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82412" target="_blank">📅 09:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82411">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN0dHE3sZCWXpZIKAx0gkQUOYi_h7k8j4wh08WkVzR5dzElrfXshFhBVkvyz7Wv_k1EPjZ3iapk5TslZD2mhQbhf8MNPJE5X6a0Vv94yfBe6Bkeiye_NLUyihx_VRTypvnGwT6XCk3FMeVJ8zYfTUFhRoOr_zoxRnLwRzGk4oK2czqxgw4vGI2M5-PGYg3K1coHi55upGEYpDdFhOCEFRWR_9eBfvcwiTbe-h-w5KKRU0kI5wOQ8r-TGBbeiYgXs-P7OA7KyTSLug_3Y4t2efA380azWaxOO8icwzHB6Mo1wEqvftJK2-zcYRDT7gTWum7E_GhXmUKy4-VzfPZqhfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
💙
با این وضعیت تورم و گرونی دیگه سخت میشه کیت استقلال خرید
ولی این ربات هر هفته کلی کیت استقلال هدیه میده
👇
☑️
@F00TiBot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82411" target="_blank">📅 00:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82410">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvow3e6UR2nJCTZtyYHfwTKa7CZ1yBTRNzFN_jGoERB68gEf4MdvSR2Q9z3E_6PNOUWlUiIczwc5pspOOwpZsEn5AWBeMQutKUQw2mb4A8EvWR33YavfYmsvV9aTx1Q6hw6OD1VprdZ1HadKLxaQjqjy1GSaVEMI8ukEXDUG4f-FoPzwHyKVAW9hlkz_d_jAZ1gm8WrKMT0tB0jEkskgeSnaLDoeOgq3fKucW_H9P6EMy1mEhKqlVbHOhsGDCA6pHQWbLU2HfJE4RNxTHPxyBtiqsrzqfkytTYj8MEw39sF6n0ihnMgIHgiQFkJl9pawDrVv75wLH4JH_MULU82zag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82410" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82409">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb91ca0a56.mp4?token=Nl8oo2IUMHzktkRAEeTlbLwvCcPSmlvd0Q30pzw5sCIAuuA7_STglWqzXyhZjrqSev1OZM2ru1oNIcOyO7WG39ivBIKQDpzDuCY_Whkh9pAIyWq46plvxr9NIiH4oQhLefpJU_D47LG3yFcW7FzbsCKyIk1mRRRIC6zw2i6MCKop-97keILTNe079l4T718NoPSYADpnlkC8t2sEqsTkVFQJeOk5fxTgi97A-Ayzwl1Cegzyy4ViFj9miJ8LaMYDUrKart6W9cBxYTOiQ3UNINQHNf39vVvP3UlBG2_ah9xYJPCWrOZZj1ahxWdpLbA9n5awXEvt-FGH2gNDdRvU_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb91ca0a56.mp4?token=Nl8oo2IUMHzktkRAEeTlbLwvCcPSmlvd0Q30pzw5sCIAuuA7_STglWqzXyhZjrqSev1OZM2ru1oNIcOyO7WG39ivBIKQDpzDuCY_Whkh9pAIyWq46plvxr9NIiH4oQhLefpJU_D47LG3yFcW7FzbsCKyIk1mRRRIC6zw2i6MCKop-97keILTNe079l4T718NoPSYADpnlkC8t2sEqsTkVFQJeOk5fxTgi97A-Ayzwl1Cegzyy4ViFj9miJ8LaMYDUrKart6W9cBxYTOiQ3UNINQHNf39vVvP3UlBG2_ah9xYJPCWrOZZj1ahxWdpLbA9n5awXEvt-FGH2gNDdRvU_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همینو میخواستی بشنوی کصکش؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82409" target="_blank">📅 23:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82408">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW1EwYSHHhx3kp-sgxnjVliOyXDYEond1VSKvfJ7x5MdEctbx2EfdFlf2cqlucYV84JyVdWYQ7-q9HVgklYqhRBTYNzlGoPdnzVAvxWsJQ8NTd3SZ2oxoBdX2p_ZGUDvlVRDk_LQG4AbMHcV6gn5auz-e3-O9z8_IsQ77V5tyWqEdRdIjOwoBXvHw4SKB8x0vDRsurPoUzR6odvKM11IY3eqsN7NzYSk9enP2cj4BPsxqzSJMla_vNdWFenP8ChL5s6QUKVofz9YwuF7SKcN7CWD5Z_7nnEnZp_R6B3kyMwgd-ndF3VN3rkl7mfCVoJzSfz4hhRHQc7fFGqnnyXVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا برای عبدالله دعا کنید  @FuunHipHop | TemSah</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82408" target="_blank">📅 23:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82407">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پسر ایران فوق العادس
غریب آبادی، معاون وزیرخارجه:
آمریکا اسم شکست بعدیش رو «جنگ اقتصادی» گذاشته‌
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82407" target="_blank">📅 22:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82406">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b263aec1c3.mp4?token=kZnzBLrXdQtkuDTx4ESIEgKzKJ8TKd4m_yLnsBXOSewWgYfokY-dLT8ZaEcit4LErxdEC_NeZqtg8ggnHupWqbE4Ov2bkHyaso5nzBogu9QihIhtvlFKfZuzIzCAWdih9Y23MiGvGOkxp1fJbhefyWl3SmJu7QQcQyAVg-ERlvqjysIsPgbMpcAlzZCIGcIMVPFEZ9SpTeD7TpivuiVf9EwxbKsTEMnjLaYgt-bpUgIP_NaFtAm957AIAzmU4WGDHjohqgWTpY7ho-XI9iAiRWI_CeZPMm8DEUl7bJdxKUP-uyF5uUkqePpuHDuC5iNbzGl3HnpcGiHCrg02aTInYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b263aec1c3.mp4?token=kZnzBLrXdQtkuDTx4ESIEgKzKJ8TKd4m_yLnsBXOSewWgYfokY-dLT8ZaEcit4LErxdEC_NeZqtg8ggnHupWqbE4Ov2bkHyaso5nzBogu9QihIhtvlFKfZuzIzCAWdih9Y23MiGvGOkxp1fJbhefyWl3SmJu7QQcQyAVg-ERlvqjysIsPgbMpcAlzZCIGcIMVPFEZ9SpTeD7TpivuiVf9EwxbKsTEMnjLaYgt-bpUgIP_NaFtAm957AIAzmU4WGDHjohqgWTpY7ho-XI9iAiRWI_CeZPMm8DEUl7bJdxKUP-uyF5uUkqePpuHDuC5iNbzGl3HnpcGiHCrg02aTInYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید با خودتون بگید این کسشر چیه ولی این اثر هنری با ۲۰۰ دلار بودجه ساخته شده و تو بازار چین ۴ میلیون دلار فروخته
پ.ن: ممبرا نجاتمون دادن محتوا فرستادن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82406" target="_blank">📅 22:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82405">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">محتوا با تایتل "عاقبت اعتباد" میخواید برید اجرای جدید علی گرامیو ببینید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82405" target="_blank">📅 21:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82404">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آبگوشت</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82404" target="_blank">📅 20:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82403">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آبگوشت</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82403" target="_blank">📅 20:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82402">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezJkA78vibFWcx_59voU7dpdGiIjHkpPdk77KCIkYeiVMwLhEOvIzv5rzamkWHEslRKmgW7RH-Re1WrNNy0TRWXWWPW_gWMoGHxvDZdkLzmblMFgdew6YACWp_VlD-Gf0kbmQtHwFLO6nv3nUujRsX-v_xpN_05Ex_liFY5lF-QgKxDovHTf94vDpbOPIGu5as_b18gfMUxbg6JSrAqwf8oAQOM3mEBlaCAmArXZvb-r6v-DupHx-kxlMZLV6eELxYTpohlRzBwEwDcCRw1kKuqH48gRyWfxOfIMP2CgETyrZ15w-W-URZ_4o7mNr79lxStlPZYZkayNIsfdIkopCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود ببخشید یادم رفت وجود داری
موزیک جدید ویناک به نام باور کن منتشر شد
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82402" target="_blank">📅 20:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82401">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بسنت، وزیر خزانه داری آمریکا:
ما قرار است سخت‌ترین تحریم‌ها را در تاریخ اعمال کنیم، و من به شما می‌گویم، این کارساز خواهد بود.
این روش قبلاً در ونزوئلا زمانی که ما محاصره اقتصادی را اعمال کردیم، موثر بود. در حال حاضر در کوبا نیز در حال کار است، و در ایران نیز موثر خواهد بود، و ما این رژیم را سرنگون خواهیم کرد.
وزارت خارجه ایران:
اعلام تحریم‌های جدید علیه ایران از سوی آمریکا، اقدامی پیشاپیش شکست خورده است که نتیجه‌ای جز تکرار ناکامی‌های گذشته نخواهد داشت.
با در نظر داشتن تجارب ۷ دهه مقاومت همه جانبه، از همه ظرفیت‌ها برای دفع شرارت دشمن بهره می‌گیریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82401" target="_blank">📅 20:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82400">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">زندگی پر از آزمونای بزرگ تر و مهم تر از کنکوره، فداسرتون که خراب کردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82400" target="_blank">📅 18:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82399">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t09si0oyi6ky-X-oeM4pxQUJqEX86KINdT3YVkbGKHAddAKQWRawu9X4qDCbTLDmwbAdFUX48uUUpcAlYRBGC6gH65ZVAE9nYjzxClQWzU7RuCkZCobcI5i1IxfNXxCfJ9BKkx6tVEQRACdbLD0dvXvtDhJCS7lQNzb178L6OWGTDKCIqFsoABRiW23GcOKiLcVx9wdn63cnQEKWAfimWNOWIKafrzlgK-yJfnyfrcGxIEDwlOGcTrabIxuj1EaEJagSqZSvRR969ifW5CUsV6_CI4jADy-Q_qoObu4cKyRc4HyJX3cYnAI-JYvNaYZzHUFiaYTHSLjdowO1YML2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای بابامیخواستیم اقامت و حقوق پایه چند هزار دلاری رو ول کنیم بیایم واس ماهی ۲۰ تومن کار کنیما
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82399" target="_blank">📅 18:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82398">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpfZIPGBtlMb-MQMhqfpu9JonNNaRGsFYnokBzVqX0tNjnqFouHpWDvCc7G6YpXePUMTc2vOVoiYW8K3IVYQIxBnS3tHb00W6fczt9YbXvSrGozXUYHS3Psk0uq9QLW3-uPZFX-wItmwvTzwhh5u-nptutUrWuwa2SdFwrqbx9wkQasHSGHT1gs116H-86_18aL-p2nfbqPB-KSJUanjRKnSgqmhQ2ohvEZsrA5qoFo1rBrINNTkMhXceQOO6yVRLxZTN1DXtf0n4bJwKzBr6iVEV84LBO0vB7W84helIZTW2dYdKwDcSwKcuvF3fcGtuQerjuqj9UU5oeUwNxcHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا شما راحت باشید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82398" target="_blank">📅 17:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82397">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ویلسون چرا مست میکنه فاز رگنار میگیره
😂
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82397" target="_blank">📅 17:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82395">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b61995a79.mp4?token=tNHC-4MGwuaxiPAS-Y3w4HfXztqpeg1dZsLj0C2razC18Nmi_cwCnUy8u2Cbi164w0AA2ZNMpQUAHPb9BOsrBuWd098ZD_wnY9B7BGAdVqTBnOjmwdsIsvtSR6-c4UlCnyvpyXM5N6QEKjYrBv6ICpe6sZ1H9mW_A2fNcGlt4wTzR2gpUCgXgLMiuNMrmedfTTRwiXwfh9oKdc8mKjD-RlrsGHlnAjN75MddhMRzwMxOo8zfUNqzpyCo3VrqfAthTjqx3_eaEU6Gx78TF0WJhi7wkK9w9TvZ8i52s2QNqL8fKFblPeJRVWkFkUlJ-GS-kujxuCWnqRRVB67wMtd3mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b61995a79.mp4?token=tNHC-4MGwuaxiPAS-Y3w4HfXztqpeg1dZsLj0C2razC18Nmi_cwCnUy8u2Cbi164w0AA2ZNMpQUAHPb9BOsrBuWd098ZD_wnY9B7BGAdVqTBnOjmwdsIsvtSR6-c4UlCnyvpyXM5N6QEKjYrBv6ICpe6sZ1H9mW_A2fNcGlt4wTzR2gpUCgXgLMiuNMrmedfTTRwiXwfh9oKdc8mKjD-RlrsGHlnAjN75MddhMRzwMxOo8zfUNqzpyCo3VrqfAthTjqx3_eaEU6Gx78TF0WJhi7wkK9w9TvZ8i52s2QNqL8fKFblPeJRVWkFkUlJ-GS-kujxuCWnqRRVB67wMtd3mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روزیه یه بچه گربه تو اینستا به نام عبدلله یبوست گرفته، تا عبدلله خوب نشه منم نمیرینم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82395" target="_blank">📅 16:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82394">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR5EaZLCWYL6g59M-eo72AYwjiX4NfRlzP_E8xRs01SqyVIelo8hIi8McvMBu6QvPmOXAywZbeXXE1bT0vzyoo1qKy6BKJ4qGzWbpYj11CDFgUBM82Nsg-A-eNry23xABjGB0t7fArUuyL3Oxgjq3AwLqrnCZbgrXxQw18PUHqT-lEOsnU8eD4xD7RcoREFetMXZXUgib23K898BFi4AbvcDTgSjKBYnqfwoIVF-JafNi95aXbXIIvC6cBTU73am7v5pEwc4t_i6ReipHtF-QeTa3D_98O0njHTfLy1z3V5nzmoI0Tv61RXMPtT5MFD1lf4v6Luwe5tO7eogri3FTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس پنج + یک بت‌فوروارد
🔥
⏩
از روز دوشنبه تا یکشنبه در طول هفته، رقابت‌های ورزشی مورد علاقه خود را در بت‌فوروارد پیش‌بینی کنید و به ازای هر پنج پیش‌بینی ورزشی حداقل ۳ میلیون ریالی خود، در هر هفته یک اعتبار پیش‌بینی رایگان ۳ میلیون ریالی هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
btwd.link/51
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r29
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82394" target="_blank">📅 16:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82393">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دلو دیگه نخون لطفا، برگرد همون دوتا۲ ات رو بازی کن(
منم دارم میرم مچ بعدیو فایند کنم
)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82393" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82392">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8zm5t7SG9sAOq3olNgkye6lSj0UR_7XAFQPeOT0_dnM3zSF6sRTDtljj_gNjD8qvUvTPMKM7sxyJKcAs6APwvaWxhhVXLVv08sgQy_-FJ6Fg-4NHVqXGgR_3jZKH4t3cIBsOStqkTpxixSYKil9QQ-2yWVBY1JE5gNVml3qkfBkel6J-hmvzmq7uEuJYcf6t22l-l1TxO3oLFpzLQLKQk-LWrwmMrhBn-eX579137VMG1h_nmx-UGQoRp8YmMWW9Z_6OoILtVg-JQA2nktSqC-Ot7yEw07a9jet7KJbKIh7eM2Bh-Z0988FVBHjmOqnOBQIbSmROYYgrG-GMN4juA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دونالد، ترکوندی دونالد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82392" target="_blank">📅 15:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82391">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چند روزیه یه بچه گربه تو اینستا به نام عبدلله یبوست گرفته، تا عبدلله خوب نشه منم نمیرینم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82391" target="_blank">📅 15:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82390">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر خارجه مصر تاکید کرد که به هیچ کشوری، فارغ از اینکه کدام کشور باشد نمی‌توان اجازه داد مانع دریانوری شود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82390" target="_blank">📅 15:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82389">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بچه های کنکوری بیاید بگید ببینم تو کدوم پادگان قبول میشید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82389" target="_blank">📅 14:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82388">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKzVql8MgEL2w8Av_v_Zpu-fADEXrY0Lqwkgnm8wVGGzJF7Pb_YG0kc86t3Ukcc8EmnktvqMJvPGLoeqZhdz5-_gdH_u4mkhl2-wupN8vOE30WgpvYYaHfJJ7oU770jPBgI91ff6vV7CLOAjqZu-YpP6KK7L6MnBXs3lJm0rorMepM_jW2ztALqiHmSbp3YcKLvjv9Kl8Kjt7k0VdTlvuCSBDlg7Znntqwge9yn8959GipYbynXxF4HkYSU7JNBY1YQeTrZx7G_y7IkS9kbEd6GV9VqN-fpEntTf9CFNQNmHggLX_p2PqK4mIb3rQHsYpQgb50g2vQzXBRGtZB1qSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار رو به جلو اگه جواب میداد دیگه کسی قد کاگانو مسخره نمیکرد اردلان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82388" target="_blank">📅 14:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82387">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b2647e03.mp4?token=evA3ONY1mO0LgX4-tve6hkUsfJ5BySP6sL2qqNskhrZ3GTT904OpIVBL1fPAC6GyLldqsN4wSaM40MJgZmPj6hDzwt9RkSXMUxZBg5YfimWO_JSGNyusLI3tgvLhpgtGFzI3OqHXEgCXK0ejK1rUebKgBjAoNWqgwWxGY9_GKlKUTGUgVWg-EIyyp7cF9g9R_A-3M0_WXDRBs-jNso4gVsmIpx5to1paU31e2Uo5qYqXoDtxMIsE-cXQtFJb-_J59eDq67hDfRqcaYI69S_4yabC1gq_Ont4jdeFNSgQf7raNeNK5cvJVGWLvVdYC4RA72gtUWrvVigYShivsPvDIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b2647e03.mp4?token=evA3ONY1mO0LgX4-tve6hkUsfJ5BySP6sL2qqNskhrZ3GTT904OpIVBL1fPAC6GyLldqsN4wSaM40MJgZmPj6hDzwt9RkSXMUxZBg5YfimWO_JSGNyusLI3tgvLhpgtGFzI3OqHXEgCXK0ejK1rUebKgBjAoNWqgwWxGY9_GKlKUTGUgVWg-EIyyp7cF9g9R_A-3M0_WXDRBs-jNso4gVsmIpx5to1paU31e2Uo5qYqXoDtxMIsE-cXQtFJb-_J59eDq67hDfRqcaYI69S_4yabC1gq_Ont4jdeFNSgQf7raNeNK5cvJVGWLvVdYC4RA72gtUWrvVigYShivsPvDIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازه میفهمم احمدشاه اون زمان چرا این حرفو زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82387" target="_blank">📅 14:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82386">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جواب کنکوراتون کی میاد، کد واسه شارژ ایرانسل لازم دارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82386" target="_blank">📅 14:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82385">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ2GRgG5xPAg0FNaha0N4gM7djMSC_Z8Q_JuN01Mc1cwv5XF8kqz2bPQM3mpvL8T3_Ldot3PP0d5OKoK9eK50zrXdygq_lab1URIZhrEBvT4ukM1AEqq42EO5uOy0gptZObxf18BslBlJr2GQkiCNZfxZkHOQvSNBhpG2zpEvTF93lTPfw6a8kQCo83ZufALDPsoEXco18dvkL7EDrxbvyvAtUhcmDtHvxUuFPLhEYe1AVfKg9SZNjZ3i5gR0d5CmFVpZ67wPGeglWmn84D96hFzOmKH_m0viOl62jC3xZF947Y-oWB-1LTUW8s7yHY_pBfv_sS21hmS4Caz0nIXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی ایرانی هعی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82385" target="_blank">📅 13:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82384">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کره شمالی حدود ۱۰ تا موشک به سمت دریای ژاپن ول داده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82384" target="_blank">📅 13:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82383">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به چین بگید یه کپی از اقتصادمون بگیره، آمریکا میخواد اصلشو پاره کنه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82383" target="_blank">📅 13:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82382">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b86b48a5c.mp4?token=fEcF3jC5ifyHOBzuO4P0z5AUiuzEQZ55HhEhUPMKpqhrsBOVa-t42E5ztPS9umV8omkbNIitXC9YtLfWbnFHpRdgp8lP3u0cjuPhGR8mwphoyPQCgwCT0bTDXt4rsYkdA__kDr7gkDWh3oEyH3RQkGOE3E3Ccl8j4RCrpjn9tVpMXNCgnH_iFT5ba0j_asd9dgRaPRfURXen1Lun2aXA9DM29QPB_yVhIe6amuqLXZ7X9foQoVptb2NjnAHn69Fj-a8xUdM-z4yy4Ob1cg7iKtSi6YdrFcNk_Djq03ZkdSyyIa5gPVlWtzfKX3QCWuCXqT5HU1eQ2SftpE9Ld-5ABA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b86b48a5c.mp4?token=fEcF3jC5ifyHOBzuO4P0z5AUiuzEQZ55HhEhUPMKpqhrsBOVa-t42E5ztPS9umV8omkbNIitXC9YtLfWbnFHpRdgp8lP3u0cjuPhGR8mwphoyPQCgwCT0bTDXt4rsYkdA__kDr7gkDWh3oEyH3RQkGOE3E3Ccl8j4RCrpjn9tVpMXNCgnH_iFT5ba0j_asd9dgRaPRfURXen1Lun2aXA9DM29QPB_yVhIe6amuqLXZ7X9foQoVptb2NjnAHn69Fj-a8xUdM-z4yy4Ob1cg7iKtSi6YdrFcNk_Djq03ZkdSyyIa5gPVlWtzfKX3QCWuCXqT5HU1eQ2SftpE9Ld-5ABA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر زن شایع ازش درخواست آهنگ میکنه، شایع هم تصمیم گرفته این صحنه به شدت فان رو فیلم‌برداری کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82382" target="_blank">📅 13:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82381">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4SC6xWsE1s9fsXMjQyJBPQb4sqXn9MpXHkot-rxyfpaN-gFn5ZfTgy0m5Y0hZHOV38aCg0waCxiJluwJ-ZyjCmp7lyYzPp8L0_Nv4M4OPrPz7_RwNxa2cxs9STeirOOoAb43d0T2cZierAb-qOkIO9FkJlBFCksNUATVprp1g5FrkOG1EYs2QYWFeZKAnyBnoDBNWM6XRfADtVqj4EHOGmIm7gRP4IcF_pg-IBwCwBXZKtuX8N4ywceMnryOjQ8LbghW9LvjitOhJG8xnwZRktGlRJQyUcvr0D9VGWKGYkoQTEUGyEPpXMyqRIfBSCzVJfx6jm0I33zHf304uopCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر پر کار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82381" target="_blank">📅 12:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82380">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عارف، معاون اول پزشکیان: قیمت بنزین تا محدوده ۸۰ هزار تومان افزایش پیدا می‌کند
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82380" target="_blank">📅 12:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82379">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtGmxm9CqHfD5SMxNtWvyWxUc46ZaHUw_WBwZajzNocF9gMDFRsiIENTe4N9JnjRg2uIyAfED5imk17wXkT9FW9U1RDrlwtfmX9OfbKXnYi6fL9A8kCYtP_9gzFmsdHoVAGbj6vPAm6A6AUzOS010qJUMS6GVmAKg7_P6VrXhiYXfU8NheQudhAEad0ijUgIf1O3XNK9nT2EPnWKk-8oeEoEqrsgGfO7_OYDf-gk0UytjpK90KIm-Q6x2RcsdTi-_hP8daVsxjNPW1BUz5QacF_HPzB6IF3uEYSS3nIV9XLLbc6y244qjhy9WAVSf4CCaO0fP9qip0fT9AUcnRvKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری رضا علیپور :
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82379" target="_blank">📅 10:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82378">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45111cea33.mp4?token=RJnDA6H3FwU3l1_28tYXCoFpBtYN6WyKcKb8NOOiOxQlXu-B_GGNSMzzT4dp2t7-OyILHNPypm69NXP4rMETga1glPYD8fdsvr3tGbBfAsgmyEa-C08Xmgk9kANtQP2NiXU7Ku27u7xg-gVcK9vQW2JhoZFQXyNsWtxDmi2beyrMgaSfG7Z80hg5rnerXEVQ8l5m0Hs-gXtww1vpJegEKWcCEaYCClmSxbaq_vFT8NpS_-QQcQnrFPW7a9TrsAu6YcuuMxRhe4fYF7srlPcZRerqW9WbOrJ3SbtHw4m9DrfUNugBfRz0fovHSgaAOdJvxJubncfZN1NCtFq9rFY5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45111cea33.mp4?token=RJnDA6H3FwU3l1_28tYXCoFpBtYN6WyKcKb8NOOiOxQlXu-B_GGNSMzzT4dp2t7-OyILHNPypm69NXP4rMETga1glPYD8fdsvr3tGbBfAsgmyEa-C08Xmgk9kANtQP2NiXU7Ku27u7xg-gVcK9vQW2JhoZFQXyNsWtxDmi2beyrMgaSfG7Z80hg5rnerXEVQ8l5m0Hs-gXtww1vpJegEKWcCEaYCClmSxbaq_vFT8NpS_-QQcQnrFPW7a9TrsAu6YcuuMxRhe4fYF7srlPcZRerqW9WbOrJ3SbtHw4m9DrfUNugBfRz0fovHSgaAOdJvxJubncfZN1NCtFq9rFY5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشته شدم
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82378" target="_blank">📅 10:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82377">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNz1jl8Mk0JeBwnZjruT-7KEI8XrJuyZyiMmrAriqm82b33LsWa1vgxC0vOl8cuMwFgJonILxCP5LTaNiSQ50368qlhze5DMQcSBwaDTldPXTXkZPbm00Yh52Ox5T_KO4Sf_94iuCviz_F_y3FHBT9HMgAf4AOk3_4qDk_wtKIvRGqFNY0ACceGfyb2zJb0-eFWb1K5FmCsPYh-epO1Vjza1D2GxNLTUzSHDXaZKhjbpyVBnjJacQ5oaHEbXRhYw3vlUG_Uedv5EH6KOWWElUtIB6MovPqtZpbSQDMG-oNIQx36pDyAIg6eV5A_XEVW1wP8znzrVh9HulYZm90hhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس پنج + یک بت‌فوروارد
🔥
⏩
از روز دوشنبه تا یکشنبه در طول هفته، رقابت‌های ورزشی مورد علاقه خود را در بت‌فوروارد پیش‌بینی کنید و به ازای هر پنج پیش‌بینی ورزشی حداقل ۳ میلیون ریالی خود، در هر هفته یک اعتبار پیش‌بینی رایگان ۳ میلیون ریالی هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
btwd.link/51
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r29
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82377" target="_blank">📅 10:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82376">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دکی هرسال یه نصیحتی چیزی میکرد برا کنکوریا امسال انگار یادش رفته دکتره
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82376" target="_blank">📅 01:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82375">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSFyK83Re6Nuu5c7tLX7zJQmXd52yKTIkCKZTZMDlP9umKH9W1O9QVjuVhwpSJ7nrRs8N0UgbSOAfiggRetp3pY0rVn3p9JDMOz37X1OyMmONFwIJVMjhaSGJ81f8LMWyfPX4vZXTSn0LKUW6gkeRwbYPLVYVScE1XX7K4GP1pCcQDW3anA2SzVXEeeNBWhB02jHEPg4O_Mr4ttd1xZuz-vbAkjqkoRDvkFVoxrVA64yyXk2s0R6o-eoyRtD7dnxt4Y8fW6vx2iO1UjSCm5oZNgqABiGUd9RreLVL6XFuTX_vF7VSqR2u_3h6MxNxUVpA8UOZhyENe7qK8N8mReoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا قبل از فروختن یه آلبومی که هیچوقت قرار نیست منتشر شه(پول ملتم پس داده نمیشه):
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82375" target="_blank">📅 00:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9019847c.mp4?token=N56rpNO5ie1czPABuQIXc5UbNIM4K0cPmgR9SnJLs9GF5INDQfJ2OYpcu1eqSAAGIZt_-RJ7XtpzCqHNk8RCSTt68khsgo87SngWU3QXdZMLv4Vw_NtDmgnMUxSD4k_O4IWd6HD_cwY0DbBgkhFX5mjsS_X5SbhgSV0Yvbd24SnxbYSTZ6QZ93Wg9ETkUB8NlaSH1J-ElOpwY4u3lmR8eyamrrSeRJKAeM80DqPl4NiedGh-77AWRBsQW9gzB02QtqehjyD0BOOXWxCdQGdeQ8SzlvTfvIBQOS9tYO8-sPpEwtIVcQTSDZc3cCe6BzQg3dWbrQSVcU45dZsu2KrcL2mh1TVhoYvDTPDat_onu8UbIKZSVE1sivf6g9Mdw5YX2GMEPC6U94WDh_-I8WWFAqKAUJcwy-JdBPADHjEf1QNlIboqgoSuS7tjbU7jZcu8gAYNEL5TwLnciBaSVnqx7XZZIsE8Ou5SiVjNeQw6yv6hKdNy15WUscuKJF3ZQiOOnOMnA2EsSSsv9_B5Qe_mW4yAFxEFLtphdFhjkGwSXjLKaR1nqbr9ewC7tQxF6pQApvn_XAx_hlfqNytmKcfJGvO4-lJIBp4ZtZajTEErPx9kj06NjbhtGbGD-q-W5sm1VByrGuarKTxkhFdFMl7SaM8EZDifak5XzfjISJUee4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9019847c.mp4?token=N56rpNO5ie1czPABuQIXc5UbNIM4K0cPmgR9SnJLs9GF5INDQfJ2OYpcu1eqSAAGIZt_-RJ7XtpzCqHNk8RCSTt68khsgo87SngWU3QXdZMLv4Vw_NtDmgnMUxSD4k_O4IWd6HD_cwY0DbBgkhFX5mjsS_X5SbhgSV0Yvbd24SnxbYSTZ6QZ93Wg9ETkUB8NlaSH1J-ElOpwY4u3lmR8eyamrrSeRJKAeM80DqPl4NiedGh-77AWRBsQW9gzB02QtqehjyD0BOOXWxCdQGdeQ8SzlvTfvIBQOS9tYO8-sPpEwtIVcQTSDZc3cCe6BzQg3dWbrQSVcU45dZsu2KrcL2mh1TVhoYvDTPDat_onu8UbIKZSVE1sivf6g9Mdw5YX2GMEPC6U94WDh_-I8WWFAqKAUJcwy-JdBPADHjEf1QNlIboqgoSuS7tjbU7jZcu8gAYNEL5TwLnciBaSVnqx7XZZIsE8Ou5SiVjNeQw6yv6hKdNy15WUscuKJF3ZQiOOnOMnA2EsSSsv9_B5Qe_mW4yAFxEFLtphdFhjkGwSXjLKaR1nqbr9ewC7tQxF6pQApvn_XAx_hlfqNytmKcfJGvO4-lJIBp4ZtZajTEErPx9kj06NjbhtGbGD-q-W5sm1VByrGuarKTxkhFdFMl7SaM8EZDifak5XzfjISJUee4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاش بعد از انحلال گروه تیک تاک منحل میشدی مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82374" target="_blank">📅 00:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رضا پیشرو داره رو یه آموزش جنگیری جدید(موزیک) کار میکنه که معلوم نیست کی میخواد بدتش بیرون  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82373" target="_blank">📅 00:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBO8mSnk4ZTVBfPY9LjMUOXASR4zyWYlp4_ijs4qgvCh22VnFW5IoevmMX1mTh0VaOITDhfynuXtPKCtW7ILYMPgMhqSfPIlFWP1wBmhA-GdCaSnHiXjSVKmqSgIS6wxDF4efEGPQvSF3pRNQcrehZdqxL8O78mhBTJqjgESIITL90iZodLwfFmltWvDBBwwfKTT0Wvvv0CceT12gf2nD4jrO_PvnOk2C0baIGJKkiztIi0QTLu5hhvCiuszpVt-Oc0VIiAp-FKcQlEu_2_WOr4K2k5jztYOU6yAsjWU7itZPaUvDXlj6b_tpaxlTN2VFGADneY9THhVK6oMe2wn9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82372" target="_blank">📅 00:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6215c87b9a.mp4?token=nyI5hlF8K9aW3iFVMsal-86Cv43-hrDnuFornxSajIMu5jZglEsPiQA4ePHpySA4vBusaY15G4TQOPeUoRhJQbSWocRu2822HRHHPajm6xMKz5TPa_4lgh1bYDxpugOywxqBOsWmeoM80YLyklYtcLuEQfJAAMlM1_4qghxI7BZsvp7q_yyVIG0Dxt7xXxTXjVADSGWb09O-d8QL-1iBVDwbauFytS_K6rPvI6jJmEk4QGFuN0bh_vufvhITrcnmgjhLC5i1CevdkQN9vyvhd30etvb4eojHIXJgJDbHfb_2bsB27b3hct7OWBjt-k-IIo24ikGL9s568fTR3mTt2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6215c87b9a.mp4?token=nyI5hlF8K9aW3iFVMsal-86Cv43-hrDnuFornxSajIMu5jZglEsPiQA4ePHpySA4vBusaY15G4TQOPeUoRhJQbSWocRu2822HRHHPajm6xMKz5TPa_4lgh1bYDxpugOywxqBOsWmeoM80YLyklYtcLuEQfJAAMlM1_4qghxI7BZsvp7q_yyVIG0Dxt7xXxTXjVADSGWb09O-d8QL-1iBVDwbauFytS_K6rPvI6jJmEk4QGFuN0bh_vufvhITrcnmgjhLC5i1CevdkQN9vyvhd30etvb4eojHIXJgJDbHfb_2bsB27b3hct7OWBjt-k-IIo24ikGL9s568fTR3mTt2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم تو اینستا تموم تلاششون رو کردن که همه فکر کنن این پسره واسه عربستان سعودیه که آبرومون نره، بعد از این ویدیو فکر میکنن افغانیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82371" target="_blank">📅 23:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82370">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vj9gLEaWFo2JQjM9ICV037uMZ-ZHFuP69oiqmO13UyqhyHRAQgAKFZU1iWzds3QJcAjxV9X2XVeURkZODOjgP5jSzaMbV5t-mlPdUadlKqRVJgoqHhJzyFurPyTWE7afK4OesDgpXaOf9yQ7KRgpGivnxA29JwDRaAFo932JhZdGAJdTxsi2jDN29MqmmavMfEawalRQALnOaeQRBJuar7yVGyxu0MBZ4NLWwP4VEbwqZf-4usp9MKpkoImPPHfZxjwIhKh-oR_IfXegEre2Z94dvVr1o7KBEMiAXTID9NRsPDwVXfZd6WWJoyd6J0foktVtdBaxklyzjVaFtUiPpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82370" target="_blank">📅 22:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82368">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
نه خارکصه خجالت نکش بیا اونم بزن
ترامپ :حمله اتمی به ایران؟ نه ما حمله اتمی انجام نمیدیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82368" target="_blank">📅 21:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82367">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سینا ساعی هم زندس بچه ها</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82367" target="_blank">📅 21:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82366">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304e080993.mp4?token=MWkLKwU3Svld4S26fPBYtzZjPmDbMrlqGW7WqlZrA9Q5X_14MPStX9_4FTXYMZ9lrDEtpcmqzF62zn-1FJ4u51F1YmJlx84HYY_k-EHwlpbvDbXTpJR-PJTHBLNFGo65M7FRP_OIxqiOCkqguNRzQGMsD0F4Gj50RPBLpOeXQFXD0tpdpGA3YJFxbAZvDUkuyQe02OTW0SqgSlzDKCQ1IuBYdTB2ZH3qaUVEa3OclBkNwg91TN--GdwwqRyBRk4IPvuc59CdY0btug4GZt7vAMOCKOsgF-XvhTB71AGrm42ah90fIqpGrJwxzwF24TZamS-grGvXMXb5ZaVzxonBHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304e080993.mp4?token=MWkLKwU3Svld4S26fPBYtzZjPmDbMrlqGW7WqlZrA9Q5X_14MPStX9_4FTXYMZ9lrDEtpcmqzF62zn-1FJ4u51F1YmJlx84HYY_k-EHwlpbvDbXTpJR-PJTHBLNFGo65M7FRP_OIxqiOCkqguNRzQGMsD0F4Gj50RPBLpOeXQFXD0tpdpGA3YJFxbAZvDUkuyQe02OTW0SqgSlzDKCQ1IuBYdTB2ZH3qaUVEa3OclBkNwg91TN--GdwwqRyBRk4IPvuc59CdY0btug4GZt7vAMOCKOsgF-XvhTB71AGrm42ah90fIqpGrJwxzwF24TZamS-grGvXMXb5ZaVzxonBHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران آپدیت جدید داده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82366" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82365">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هیچوقت واکنش بیش از حد ملت به یک سری چیز هارو درک نمیکنم، مثلا وینیسیوس جونیور ریش گذاشته ملت یجور رفتار میکنن انگار فیلم کون دادنش درومده، والا بخدا قیافش بهترم شده دیگه شبیه میمون نیست، چرا نمیکشید بیرون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82365" target="_blank">📅 19:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پوریا آدرویت از وقتی نصیحت داداشو جدی گرفتی رو آوردی به ساخت کلیپ طنز و از رپ کشیدی بیرون همش تو اکسپلوری، همین فرمونو ادامه بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82364" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82363">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNbbFG1ngdbmYQ9y3c0w62k8Endjmk2SiLTWHJ5yjMy4wiUYwwBgCdT39XW1cGI0dJlqF1poIxxb8VYtq9sbBa-76tCpcGRgTUIYMwa7JC9bXDsTkw3NXdoC7ip6MnzOPdXT9spKxwJK1EMinAstHC1u73iD6HyRPY4g52zTwAlQIxC0SuTVG3Rk8F1ea85VQeSD1qvKPvpcagaau3UOopwNnU6uHf77FQEDu99KaHgQr3ZX3xQ_fHZOxiWM6M6p5nmJHI4Jxd2vsb8Blbpx_QY6JF8hLt47lPOrTVxanohTnfFFUzNku5co2sU1mQocQ3zlHUYLRaQTFnqZr0DLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسا خسته شدم از بس عرفان پایدار با هرکی آهنگ داد دنبال ورژن بدون عرفانش گشتم</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82363" target="_blank">📅 18:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82362">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ناموسا خسته شدم از بس عرفان پایدار با هرکی آهنگ داد دنبال ورژن بدون عرفانش گشتم</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82362" target="_blank">📅 18:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82361">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCtdJzU89bA1DSeq7Bfslhd3zX-N5p1Hv1XVM9Z4FmpbR7Z6WUlu5r4zB6h_MAIAfaWythVuu5CUy4brDc2B7IYY0MnQTJ_Nu5Z8BRh8qP1rxnqwbTJXM_bWbk2c_2-8HtAQSc3ZlB3UWtunIRewuGSByoyK-Vnh2YPlCfkMjxIXYKacICKbN9zx7_VcA8WOcSZ7cEncEULXkk03LDgbZhxDfq2SYLVXtZ4VeEtc_-44XNl0R0fBFf2DmW5Ths2Ksoyqfd5xt1hFstfqZvT-MyHz94-LNqr6-7qYjZioKQ_dMkPhEnlPZltDmJ9bb_L6czL3rfN2M36Dz7QOn6jAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات یک سری تحریم های تجاری با ایران وضع کرده و گفته تا اطلاع ثانوی با ایران تجارت نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82361" target="_blank">📅 18:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82360">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قالیباف:
آمریکا به دنبال خروج آبرومندانه از منطقه‌ است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82360" target="_blank">📅 18:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82359">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fb611ffd.mp4?token=WehJZr4LX0lFwQ91JOJU1mC4gR3QzRlypmUU4jlK3H_rWuNeXA_2Uwsbi9Io4OLOfbQ1nr5wgGxpiWc4Dc89ekRI8z0sATutkd09SxCN6Gng41_iOwgC06_6mXXiwNqVSRXghQpodjA9ZWDKnIZBfUtLCpKqrwTGabMsnvYcw--LUMKmCnmhzNHIpVYixkP7EEASx05kuhBMlrtYrJMl8cw2PSXSBfMFLVolgE4_a--pkt96PAa5trx9hOQlY5U6sP3Lm8uzDjpHG6DJV98COXIcuvrRIDSTGI0QhU2adNdiQXmmgPWqu0pDeLpJlTvOTlOraI0ci8claUTpaWHDYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fb611ffd.mp4?token=WehJZr4LX0lFwQ91JOJU1mC4gR3QzRlypmUU4jlK3H_rWuNeXA_2Uwsbi9Io4OLOfbQ1nr5wgGxpiWc4Dc89ekRI8z0sATutkd09SxCN6Gng41_iOwgC06_6mXXiwNqVSRXghQpodjA9ZWDKnIZBfUtLCpKqrwTGabMsnvYcw--LUMKmCnmhzNHIpVYixkP7EEASx05kuhBMlrtYrJMl8cw2PSXSBfMFLVolgE4_a--pkt96PAa5trx9hOQlY5U6sP3Lm8uzDjpHG6DJV98COXIcuvrRIDSTGI0QhU2adNdiQXmmgPWqu0pDeLpJlTvOTlOraI0ci8claUTpaWHDYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانی شدیم رفت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82359" target="_blank">📅 18:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82358">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhfQXJ5mmrd4K0iFL6VDCvf_tQmj35cWsrl1sW8DZr6tq2daXN3WTya1T3HaF8wuE3KHtBvpS4GboEX2ixoKCBGBXxwXR2DyS_zd-YUh_HIZieyiArR8a8ThZuLDcK9uxSPj3DtMeb5Ndhra8pS-WEMSR_1jsdH8-tGVVdnc4Qn1l1ScCnHg4lMuzp_WqgMxwmDF2zhVqiOukFugam1MQlVI08ayDTLaj6BvuR05gkNpfmftis9FVB14wjcB7iP6ZmRuoLefRu5va4BNQBUkj4hxgOoQukP6F41tRy--7nxksFWUOnavVPqGRIG139_7TpvD07MRz9f-9m80MHryRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید - مالاگا
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
㼀 ورزشگاه متروپولیتانو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۷ برد سهم اتلتیکو مادرید و ۱ برد سهم مالاگا بوده و ۲ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
وقتی بدهکار هستید، بازی تعطیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g28
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82358" target="_blank">📅 18:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82357">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پلیس فتا: یه پلتفرم فروش آنلاین طلا با ۲۰۰ هزار کاربر ورشکسته شد و علتش هم خالی فروشی بود!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82357" target="_blank">📅 18:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82356">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">باختایی که دلار داده بود بودش سنگین ولی حالا برگشته با یه کامبک(دلار برگشت تو کانال ۱۹۰ت)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82356" target="_blank">📅 16:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82355">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4162625b6d.mp4?token=DIr_4e2Du4pef1Y_TRgjXB3aq_ktjd3rnkhd4T-JQkElqrACykbwUnJHl0r3eeFTDBVglhLK58vG0TFWUl0FdHtFo_mSnQisdAcingtGslQMTFAS9IS4e9BFtnJ1rAlBkAQ1EbdPXK8vFLaRO_x9MJWciVQXquCWIDjck4N9tHYuGPWmGB_BFj-pJf_u3BjED_m2kKov7icI1UGlnsFwHvYUA5KI9am9xI5_bbGGGIJAzb5lMXVpT-EWoUIauii7H7_16Vo6E1Pm6WhwnqB_r90IV9wW6e8Jz7fzpxOsGW1MMSwclPvMQkTaMsIBTOafT2ST7R29oyzBonv7GzeQEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4162625b6d.mp4?token=DIr_4e2Du4pef1Y_TRgjXB3aq_ktjd3rnkhd4T-JQkElqrACykbwUnJHl0r3eeFTDBVglhLK58vG0TFWUl0FdHtFo_mSnQisdAcingtGslQMTFAS9IS4e9BFtnJ1rAlBkAQ1EbdPXK8vFLaRO_x9MJWciVQXquCWIDjck4N9tHYuGPWmGB_BFj-pJf_u3BjED_m2kKov7icI1UGlnsFwHvYUA5KI9am9xI5_bbGGGIJAzb5lMXVpT-EWoUIauii7H7_16Vo6E1Pm6WhwnqB_r90IV9wW6e8Jz7fzpxOsGW1MMSwclPvMQkTaMsIBTOafT2ST7R29oyzBonv7GzeQEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زید تلخون رو تو یکی از تیمارستان هایی که توش بستری بودم دیدم ولی یادم نمیاد کدومشون بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82355" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82354">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رضا پیشرو داره رو یه آموزش جنگیری جدید(موزیک) کار میکنه که معلوم نیست کی میخواد بدتش بیرون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82354" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hw6lN10EZeOj5HJraks3QKKzH8B2R-qbVBCt2t7FtxG0z88Xbqp8t00d12he-bzWwwXJJlGWlYoGm-VmddG0r549abBM9WX5dVTrOUtcwLkpK_GZekuINPeNP0tkitzbBfZsXaMh0uSnx7Ye-o4QWtwCBHMS4SjlVsBGiEyg-nlewz--fW4a0aLfc3FJicGI5XU3DGMwP6er1g0kZEm0sOkIC9yTLwgeNwvGkju5LM14niWuQWFH1VNmc7bYKPoHaiF-Y66HvFvOoinSc1CJc5P9jbLcCU6cmsoRMtXFmJ3kO3BARd4Z0CykuIjqoRuXbS_yGUVd9slTkruWUr5E7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دلی که دریا باشه کشتی میده
❤️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82353" target="_blank">📅 15:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوستان ویلسون کلی ویس داده ولی از درک منو شما خارجه، اگر معنای فلسفه رو بلدید خودتون برید چنلش گوش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82352" target="_blank">📅 15:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82351">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGwAVd87Py_XCJmSA5Ndrh6HAiCtRk9s8Dt1lAyJPXTDPa6hAxVGmR1_NZKgjNioVTZrA6XoV111ejG8AceKJOrdJq7qNZaAjoO5HLR4PycgRth_xkKk6cJ7aIHSOO8e-YbIqrPA-xTi28PnBlPl1vkRNd2o0Dr6EWaBGQQuAVz0iT1DONiyVmnunhHh3hrTDrmEqU0LCwTGRzhOJ5LM5wKb_qJUWLvsf988SpihA9pkWB8U4on0dAWYvmQ5Z5otbeNWsCFjG42gxcGt7Zftu8hG4IeN_eLI-j4yJm2j783BWlV3FtMDeng3YnJ7r8pE50yZrhWK5g4Ko4DtG9TPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری این زنه که یادم رفت کی بود و حال ندارم برگردم ببینم کی بود ولی به ۱۵۰۰ تصویر مربوطه و داره راجع به مهدیار صحبت میکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82351" target="_blank">📅 15:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82350">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خب کصخل میتونی آلبومشون کنی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82350" target="_blank">📅 15:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82349">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb3975ba9.mp4?token=n7d9cCaG029LgE72uczNFRT98FBcadQQeRXcEOuCfjigMGz077uNEBUskSwH5d56BmrwLghQnvd3WlAKn3FigyHOifoP2fUJZ4CjlmTJeABH6qesOGorJ9dS45vemidTfK_wQw84N7wkAIx7soqSMspFEEXp9qrxsV68v_8LZNYwVkolJvIunwTkWazNxDKqcp0bhICc0kOU4IdY4T_08tLgAnqD2Lxlj_BQOemuQxz1_rpdbpq6AlM_s8eDaAaujez6NcYhaOQLZu3O9fGQIDTjC_t54GLbgbgpMr2OXsiXMBjDzgUs1_c0bXhDE9ZSRum__eGVl85JTnlebbO5KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb3975ba9.mp4?token=n7d9cCaG029LgE72uczNFRT98FBcadQQeRXcEOuCfjigMGz077uNEBUskSwH5d56BmrwLghQnvd3WlAKn3FigyHOifoP2fUJZ4CjlmTJeABH6qesOGorJ9dS45vemidTfK_wQw84N7wkAIx7soqSMspFEEXp9qrxsV68v_8LZNYwVkolJvIunwTkWazNxDKqcp0bhICc0kOU4IdY4T_08tLgAnqD2Lxlj_BQOemuQxz1_rpdbpq6AlM_s8eDaAaujez6NcYhaOQLZu3O9fGQIDTjC_t54GLbgbgpMr2OXsiXMBjDzgUs1_c0bXhDE9ZSRum__eGVl85JTnlebbO5KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانی شدیم رفت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82349" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82348">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1kv8WCUbq2pO2xaFVV7RtyvmtHaab26EAnskvt3hFoGtfXRirlkvWjNatvdACcmEP4TEJAR7aJCLy5I0i9ZP4jLBm4rMufmHzVyDKby4gInOxuzSJueMUYWyiAYQTvC4yQKdKHqJmRh2n3xcCBviuDb_vbOKVQA9I_XFpS2GI7K9CT8lmtHxf1_Vc5pUHXe5EgJWdyXXOLaxcC4wxZ49vEC7RVksAia_TMZSNdzvCE_INyxJpfZ3WhSk6nWXwrdISSbZs_kVseCjbkUa-p0EQNoEACGVkd2JNaXbuPRWgQ_kgx-O9OhLuNPb9BSDqTeUMDMiT9SwxknxMwKyjgG9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82348" target="_blank">📅 14:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82346">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1960c566c.mp4?token=CCYOS5exG9YhaUZh1fTgdvB_-Lqp4TCOtfU93YFbfEepL8rVDpVj73-s4mhBLqz89y0FmeYxW78fWAJrw13t5kySpMZqCh4AuZFM0C24408FOLWug0wqsWjcXqM3Vmq7Ftde3MS5zBAa7LmRDVhkn0F9h7WqXQFSFtFtl2EFeBxV2dtKNtuqbsWao5QR9hfQt1UJHfOgCjADOxFlp16mmTNC6Dcg9DWYb-XIuuXlOtnMVUbTN9G_XwxFLRyzM8lBvyyfO-xqhi42kSWOMJONYmgMcu5l8DGrja32yOsCcFW4QxoBHp-ssRLkS1oUHyoRewft4dqG2EukM75fwXJt6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1960c566c.mp4?token=CCYOS5exG9YhaUZh1fTgdvB_-Lqp4TCOtfU93YFbfEepL8rVDpVj73-s4mhBLqz89y0FmeYxW78fWAJrw13t5kySpMZqCh4AuZFM0C24408FOLWug0wqsWjcXqM3Vmq7Ftde3MS5zBAa7LmRDVhkn0F9h7WqXQFSFtFtl2EFeBxV2dtKNtuqbsWao5QR9hfQt1UJHfOgCjADOxFlp16mmTNC6Dcg9DWYb-XIuuXlOtnMVUbTN9G_XwxFLRyzM8lBvyyfO-xqhi42kSWOMJONYmgMcu5l8DGrja32yOsCcFW4QxoBHp-ssRLkS1oUHyoRewft4dqG2EukM75fwXJt6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرومزاده رو هم گرفتنش.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82346" target="_blank">📅 13:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82345">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH2xEHNTl_IEPEMHFi6vLwkNDzni2xHf8RA47NCCl7_CYCcwHTNt9k_a_dZap8Slx1eMYDBFl_SmPVqTppFbEmPN8vPEucLVWBJCbBIkBzC4FuFSoES4o5kCqq1DkVUAY9mrgaVF-oRvoGdGQolx0TGRPn1GldS5nC6Czhy6WLgXl52Dmup4wuMNFcBAefO8d_vfdJq8hUSN-zmW7eOstJvsI5r1rGaSszeuFqGyVqKuO0I3czCpNOjDx2ezDx3ut5J3YtMUmHop2_nciGS7LY_ybRmF7XQFz3jKwgBqQGqTguGmmHIyWt9UNk8AFOKyMXcnRT-BtlHT5KGZnbC54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نادر دهنتو گاییدم نادر
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82345" target="_blank">📅 11:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82344">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a33e0eff.mp4?token=Q64RvhRgb7X4FIZuhtEaPKE0JINFWZArJnnrfVVImsy5cvB3BHJUoQlrVeiAMyEzU1R1RnLIDRBIQF3JsYaUp0PXk7NuT9wP5ChZLCxOVSYKipUG1pCSRb4I3CGtIU-uz4YBNElFgStxx4QLtA9HOnE8aHzzqYYulFa_-WstXW0fkRMlxpPB_xNFo2GiCFDb9MZ3zMz0Yw-Qd493yhl8IepGVQq96tUK466TjwRTJIBR4F29ezI8M1nUHVjd3evoSzCeW1a0RUAZ6_QsX2mR18PBx7s5JgcEBGMkRNuuzvzEb8W57ML7SyBk9ngwhZMv1W1QjGiLleQkNLFtwjZ5PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a33e0eff.mp4?token=Q64RvhRgb7X4FIZuhtEaPKE0JINFWZArJnnrfVVImsy5cvB3BHJUoQlrVeiAMyEzU1R1RnLIDRBIQF3JsYaUp0PXk7NuT9wP5ChZLCxOVSYKipUG1pCSRb4I3CGtIU-uz4YBNElFgStxx4QLtA9HOnE8aHzzqYYulFa_-WstXW0fkRMlxpPB_xNFo2GiCFDb9MZ3zMz0Yw-Qd493yhl8IepGVQq96tUK466TjwRTJIBR4F29ezI8M1nUHVjd3evoSzCeW1a0RUAZ6_QsX2mR18PBx7s5JgcEBGMkRNuuzvzEb8W57ML7SyBk9ngwhZMv1W1QjGiLleQkNLFtwjZ5PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین دنبال کننده لیگ برتر ایران :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82344" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82343">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA0Sm53xzbikwxC5L1BQJQESdsliI7LYThLmMa9BbgzQ3zODY1O19jyAJAUJMKfE7MXNRd_E4tiSMjhwjvebYPiWKukA_4fHMGqObQn6vSQq6xArzvNYVxc9Lb6FiVgpCWHmbSWKOmjedH8Wp99OOEqBzJ_DVyVAWTIsalHX1GMXC-q7XKjv3_4uexKGAzCLOSRRBV7mHEFznWN8BBMI1QUJnvwXljHX91S8mQE-6Mkjz4n-AafT_iEzHteil6BoKBuIEqlmNgJqY3VRNa513W7Kuo_2bdtZflHqnTReePYisiKmBnkDopOKWU9Ojcs10abKk0DqO1u1tY7-P2QDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید - مالاگا
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه متروپولیتانو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۷ برد سهم اتلتیکو مادرید و ۱ برد سهم مالاگا بوده و ۲ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
وقتی بدهکار هستید، بازی تعطیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r28
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82343" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82342">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400ac60101.mp4?token=A-foCcYWXlMIvc_pEsAPMeFq5aC5cbq8P65DGc-FedydssOpWeYNpTbCknzEjTfgSHm7OQ50CxCDGHBSvd2IVyjFTneW-tD-kJNwdVYFQpfWA0lsIsvo_YoJOuQEzsBKQS5CVLJd85uei4JUUZ5mxjYFW6SyEn_hgngsRJqZdTufuckqJ17FX_3pQsrT7HXICMDDdF2gbVPB5v1--lbpOEYfgcJr8I3cTRyt-RNWuVCtPIqaPPyXuaHSlY-Aus01vskKWwuzYDGPywSnvbRhlqP7m0J-WNLGHJux2xskYdrkjHNt81oGErO8Ge7Exus9JiXvNEcdGQLEaX9i5Omg5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400ac60101.mp4?token=A-foCcYWXlMIvc_pEsAPMeFq5aC5cbq8P65DGc-FedydssOpWeYNpTbCknzEjTfgSHm7OQ50CxCDGHBSvd2IVyjFTneW-tD-kJNwdVYFQpfWA0lsIsvo_YoJOuQEzsBKQS5CVLJd85uei4JUUZ5mxjYFW6SyEn_hgngsRJqZdTufuckqJ17FX_3pQsrT7HXICMDDdF2gbVPB5v1--lbpOEYfgcJr8I3cTRyt-RNWuVCtPIqaPPyXuaHSlY-Aus01vskKWwuzYDGPywSnvbRhlqP7m0J-WNLGHJux2xskYdrkjHNt81oGErO8Ge7Exus9JiXvNEcdGQLEaX9i5Omg5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باورتون میشه یه روز تو همین ایران خودمون
رئیس جمهور تو دوربین زل زد گفت:
دختر بچه ای تو خونه شون انرژی هسته رو کشف کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82342" target="_blank">📅 10:29 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
