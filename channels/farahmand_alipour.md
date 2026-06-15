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
<img src="https://cdn4.telesco.pe/file/ZrXuPUqlNrc0vh43nv6XWRLjb3nlEoLniLr96zNXgYPtBnJ3gyEWIxVrk1WGopuJLjDaEv2_l2JxUCqQqHUU4z3ukiUC2_xA2x3lO_6xPWRwuS72GJRqTQqL06vgJuXggT5i92JxraNI7LIZcoNWtrVpIV7OsiWJh-38rbDYXOHSuH-Ajmjol2N7KsKDoEniOxTyyxKXYaooz6SWWgaqmfHuVuoHp93voWwzgLglpNWz3bWXu-jYlPBVjaNfyL8TfxCopDqG2QaHZk__Sa81ee5RzxXZaPqs4Tb81UcAEPQFL_CC9_gN_e3BH0FS10LG3Q00_UucsWg08j0YKDNhOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCeY_I6ZeHmowhf6WSFQldHus8QaITXuVMBt7wfR7KyhMcmpiKL-TitEfrUgO_IX-BJPAOXc8wvaXh45EKEb4bj-hFM3PGn4YvMAGB6j2EF4UKe9Tq2GfjwKD-5QlfQ-xgaRfOx_u9cF7172-TESNyt_q-k8sFXiVYDxsVmlchmb3EcJNA_nDWgz5iYf83Iffd0xN_sG55o-rwC6SvZQCqCvAaZ96Bx45sIZmrafFC-0XVk7fq2kADWqk88buDahgu2qsrBzvjeZflgMEljUwotb-KjehHgw0cH9WTCsg0Xbh0otsftgWo7_9c557dvjF1DgTerIrvqZICjWVLVzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzOsHTYpo_JOqRS_pLj7DSlT-gcBF7nS2c61U5AH0GK4N4AmG99UFkk4ESWwTADBVDB5XfYDCQ4L70jw9w_gFGwosxzQK_9l6Ya5UoccO09OPZOvw3acR9Ben0MDTgJrDxMT-Wb9tZ0TyvJRWFCrYJH-dESYua3D5s8ZWT8fjJifoREVe2prTnz0JhJekHSoaRSb4p_IDVCHUmLmS6r-_I2zCn_d6s9XHhykbs8fpfu5dfZfvOlym5_382Dhl1yX5ZHdCdUrE550XMKobp-0LttMabgsHIYSiuPV8xPgn_TKR7LeW1MqC2DVAs1XIilxzMovRoqUuPyzZK7EHwHImQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4F_6F5Aa2Zvx1bf6wMEbKIfsbubOSZ46j1fmUr0dASQPfltrhG8UR--PfE2Hd-HF4DFo0uw4QQmJ7SzY5-XB2-u1frziVWW9IUu2TSdTlHTcpcCD1gbuQT1PfzEbqShX3lDD3SKHKHQ0qdTseRxA6tQkuVh6vvcMUDejLamnqcaXmn1Z8AJZDdUZ6yfSZtD9ZKzhjEgoip6liCjhmt0UbJ0-x2jWXjZUyNVnM1QcsKiHvI3f5XPeg0z5RxPq9omv0fQubvDBgT147u9NzDgrGxw-9YZNvrWWJMZW7zaHPO5UgGzwQkyKnH1YZJwxPMLgaHVcU41GTNITZW1aqKG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-W6O6I1KeX6NbbXk9akso76C05rdaw9_jsnyzfse0ZjYLOSikD46nUKu5zA7YiXFtLUaQ_duoXXIDrmOcY2uGmMsgIMuYngjUzP_ptm3C_hxNua2SNeFchdyWEgf_ghs-O4xGfhT6fQCRZxddI0OVyU2f_AvSTQRe1gJUoPHJyNEE7O_O0MNssF3LMHHceKh2FPE2zTq2TjTtvoVymAY7VFUrSeGKA0PuOErEIs6YVMsPQZbN0LMymHNfs1QuckvsnosuBLbaLIpFP-XRKWCpocMTOCnWLys_t2EvvNVQm9gZc40leEiyh-lGFMy0P6ua9N5paF2_jWYs_a5pUleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd8n2E54zJ8YhoaiObz1oEyyyKdT4EljHv5C-oa4YphBW4e2PYCt-fTfOzgimFWexppyieUUXbU2PR0Vcym-WEXEXw62WlMzAsURgvkxWbzViMTGBevPVKqgoMcyRStRQaRXs_G3xXC6epTo8byI6NG0KDMzU81LhfNrcXdBuFemT5xUZvqXcqq-P2Z5nBbWlC_wXjU09FXDqBhftj3v-hafODV9wt9g8Qq_fP1DwB3_PhzEXEsmOfeIrsPaYjfWD6dDVtVULey8wk4gfYcA2HGNIibG9DOyQhw21SCvX9CeGLFJ_SIvEV-Rxa0ZPkAh1ATUxYeOeZ4S-g4-KO_MGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=sqxOdFoSRfU1xFWOj9H2KGu56nSOTGj4NJJhhrGDUTFsfv68ApkuWMnx6VAev5vFF3VBEejt-Lh8Lty0Pl0qaOGegfscxRnVOFmBiyzu52o_DtQ0bfbM0RKtHvRyoQPmOLwUE8lSYCO3rGXgtq4s6Txxmd1GBk0Q8mN0EzUC4OGUVKByu8skUuiaH-v440cXNeuWcH-pw6AZSyPiZ2zFUivOrIMJ3PoK9VK-By_ZtlkvcJ1b9ml7rudSmoSzo_vNL1Hq5-RyEgAFkQYrbb90PGmF_mfjW4qTgAKEs_M0ORNPkzusmBqIHZr02g59BrwS2ON4RQLkqZcTjR-5ZcXpxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=sqxOdFoSRfU1xFWOj9H2KGu56nSOTGj4NJJhhrGDUTFsfv68ApkuWMnx6VAev5vFF3VBEejt-Lh8Lty0Pl0qaOGegfscxRnVOFmBiyzu52o_DtQ0bfbM0RKtHvRyoQPmOLwUE8lSYCO3rGXgtq4s6Txxmd1GBk0Q8mN0EzUC4OGUVKByu8skUuiaH-v440cXNeuWcH-pw6AZSyPiZ2zFUivOrIMJ3PoK9VK-By_ZtlkvcJ1b9ml7rudSmoSzo_vNL1Hq5-RyEgAFkQYrbb90PGmF_mfjW4qTgAKEs_M0ORNPkzusmBqIHZr02g59BrwS2ON4RQLkqZcTjR-5ZcXpxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-thAneT0i8IHfFu9t72fBzz4_Gcp3Lj7pfjP774Kf-5Y_GzT_DhK_Wotra5h4YfY6uejTQZQkb1tmo85wphu_oz-R4rbDRACJDgWHl0swkVvebHQcsl9vzt6NFsyzV7Xi9gR8pfMw_tuvHmyrmEtutIoZfYkxiYfHWfCmjTiDrQoeFZT7f7iWPdmN200ctEfmOtc2bKLxggSJ6uSlUcyhEL7g4mmYVKJDAVFZzfyOd-Yi9lz0QS5GbJxnw3-uJY2qOT2f9ioNhWATHwYhhAQq15PgBDm6KaAJsrdo96ToNBrAfQwyipWxVPfqgRk5ZdsBmXPbG_0ptHd_37y2YeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4mVibPBw0eTr1gRTGNQb3XRCfny3Oz-uh82TwTsV3xvMGClyO5fmI6shvbZpKO3XEey5XidRloasQiHdbrALRSFQZAnisgoaRceVWlI4CTKNGoB00Ghe5CNX0baKLelkuhdT_iQQYC6R1cKSkDT-QdKb7xG2HyJeYdTcbpNYQfJF62EvT2qREMpgg72uID-BgYQXRuufpMUEYKXaIsoR98w56qi5eDOPV31uMsOMUmdiiJb3ba9oX6hVb9z63MOK-DUDfFC5X88bAtLXs62907JLlWfcpIy_lhoy1aIlLLZEMtLoo-fdn5qg5ppozUDL6y7ocXanJeMU1m4OJcOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-BzrRHeVQ2UMm9WuY2JtXe5_pV9kg1-2rfhdVquGkw9j4gBVXeCkCYZX9ziQVOvFIRyqp8V1y-tWNRHg1ZT3Qi4YSYoGJg9u_mfGwmYRfXI8GPV46QIGw8lIB6L0TVCJ5w2H7L3rSzMGrExDF_-AcQ3xu_A4nWAQvLNnT_XWD46MObcGK0sMN92FPYG41BH19LRgq4YK7iFXK1hFIQst-2BPIqEap-5D50stkDm2Uu8sIsONpqrr3W5D0TeMYCmBz-im5D8ZfEcn0oY_RxM17mfofIocWayViApPRhL2dO9OPVKKn_ZeXKtZkpT4ulXU4d7I8BhGiAA1sBFivemXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcTQKFWjSocS4SiURLk0QU8VKDJbJ3ZvZtIoL1Zdd7eIdtMnINUgw_suDMlRPq4xhGD6J0PnZxqPoF66wOX4C7WEz7hxwOOClopXQsFYYRzQ0iSzd5ABJrz437HPxBx0YWK0hyDfctCvoXwczBiCZzg44nk6rzxYvTAjNM2AsjA1-Gu_tKcPl-ZJbe9q7JOx3vxoA0dF-I65tgvlGG5qEwDNrXnq6GzmjAM46MEgTuG-sFna2fqwyqIHoaSs1ui2EUXCQTR0oDJ54xGuHn6N3KV6NA2eOQm9L9KpxbkaOOEH4_SwYp1Oq8c-x-6GbqfdkzYgSTAkeGhAnpkk7K8MYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M03B7noW6qpfJyjjTW-RS8nZ6WmvQ946LYKNhoR89xFn8Pioz_m_X40n1XPxopGpcFsgNQX175DEJGJ4j2KU0SeyZ5h7xF_bx8uFFXuOX8jj1ZxQkWABP-WtxtoHjpyJNGAQkekDxOnGPAH1Dc4nsWeQNjC7piquw7uP4VkEoNkJj_vdCVhb5jME70-wLWtILzqnDgZvFCqL8j1DaVojrX-LtGBO8_AJ5E04m28SdEptNzefVeiUfOPIakWAed0UayHGisY8nw44lJvykCkczegOQWAp3xKgNwwqEVajXHvLYzDQcYdimzSqiKalqFAgY8VkfN1i5b3fRIsnDuIILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOn4FVtZPOksup3-ez1BI-nJRPNbncnyMtzk_w2mxk2zdrfkjyvjCYVakTgR3emLPgN94hYGWl0OR5dM7sJ46NkZAX5kOaamDdM9R5PQY_JBtqabf-degEFgvTp3kg2LRSgTSwkXJPTe_j1yqmGYhsEe86vER959rrWNbTHY8tGvl2Fu6MrhbNilanJOY5-gkPKs9gKE8q4wyHVwu6zpp6XDj-M24_iZ0NMCp0tCZjCm-bgvrGTx5ibw5XBlbuWLz98gCFip2GNMX056rBbnst2HqkPadUl8O3Tzwz-D7U3B8zMXQ-o7KhWI3f0vmWKV6NvSk3Of-Kn0CMfr2vCY9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMNMVmk5kk9580hCIUT_or_h0VtIQFJr_H49C2h0nZxUAYhiGraBg9eADo67OEtSclphit2yRxIRU41bQLssY3MxUrfsgg_s8CoDxRw_nBDBQNrQq_LJo_w1ZnOTadeH7DjlkQQLsrXgz-2UymRQ4DEuZf1Xq9RjWMwfS4AR2EaLsUY7iSJHzaWbkL5Oqbbxh-U6S2FMIebSKsMYef8S8lBePHLjPeU1ijhJryZvDtYGsbRChtndunFCOdO46pNYNjx03fUPnOlybq84nH93YJaezeaRjLuzWka9sxTYXjjml3Xx2iPn1HcUgPQVaKsP0xkCQGKTagpN4Kvp8u3TiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCih9Wib4QqmE-nmlaYMaTAww_1_BKpyJYTVv2ZOMd-hrWF-Vp44dbm9FbzDE9N4HtLIm5Ub1jnCNU4X5D1fHdGmw05wH6Dr2vU3CObOS4VpKgmktmRRGIpaV1PlGOgUTuovF6m78HtxKYgvobyT-yj91baQgxlHG6Ipd6qnnqWyqyM30J82m1cc1RLEPag1GodvEYB6jsqQF21Y8lUllGZz7SLtKkzRt-pTpAXbv90MDW_tzZIUSG4TiIkY6j118Li1QiqjEj4v-2pSQpsjmiOuB_MZG4JxeKK35Uk09rehQc54HMbegpsgIqf6zDnajP2DQ1gq6toc7KwLss85OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=pQo1-GOe1snUtoy_Aq_ljtI_nchtHDugG2naDUkl9RVBQ3hQ-b3d8IqDzX1CJ6xXm6qVnrU1XGc_MCW9hxMeDxTAnv2kbmSUlECoAB9glr8q1KUM3wR0W_7EM-2_FcwPLLojfz31R4aO8tMWb2GgNrA7xfCagrifwNc3cfM-gqdFD9_59kly605190pXeTQUQkDmz9Kn3aNo39nipA7L8ycYoLnIB_q35rF80pO7xsR8nsuaTK_2v_froEr4eln-_fNnR-NOAE1n1TJNbZ9bJZTm5Wmud35-RNmuvjQTh1w8EUQ7EqMncZQBjkkmmm8Aaia3xXYRSGW2a7bD5jFoRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=pQo1-GOe1snUtoy_Aq_ljtI_nchtHDugG2naDUkl9RVBQ3hQ-b3d8IqDzX1CJ6xXm6qVnrU1XGc_MCW9hxMeDxTAnv2kbmSUlECoAB9glr8q1KUM3wR0W_7EM-2_FcwPLLojfz31R4aO8tMWb2GgNrA7xfCagrifwNc3cfM-gqdFD9_59kly605190pXeTQUQkDmz9Kn3aNo39nipA7L8ycYoLnIB_q35rF80pO7xsR8nsuaTK_2v_froEr4eln-_fNnR-NOAE1n1TJNbZ9bJZTm5Wmud35-RNmuvjQTh1w8EUQ7EqMncZQBjkkmmm8Aaia3xXYRSGW2a7bD5jFoRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=AnsR6HuzF1jS4T3-glMe3v2mQyngRhuX0SU1Ruk0NZiKFQi2F6ECvj7Golr75nZxWgwtLVsNguc75fEbnSqdzwaxhaJW9Boasg1YWVs2tQSJJiM1cd-h2fq40KQMTconyxaxRWcGHpTtkes_EJjvLm9RbjhyOQsBdlqyQv5WStxeLUzxldMn7_5l1_SSMaan_Q11k3PRLK_aFKF20HxdmtrqxnWbXn2DFhQrwKyGRadiarhwXXzXz9WdEZ-1GjHYcW6SoeEyAIKT458BwNTtCv20H7kUexsgj7esduwtNA9Z7cdT_Fcmxj0s3QnKNrbwwriEjYLL4fnP3LMLaUQaug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=AnsR6HuzF1jS4T3-glMe3v2mQyngRhuX0SU1Ruk0NZiKFQi2F6ECvj7Golr75nZxWgwtLVsNguc75fEbnSqdzwaxhaJW9Boasg1YWVs2tQSJJiM1cd-h2fq40KQMTconyxaxRWcGHpTtkes_EJjvLm9RbjhyOQsBdlqyQv5WStxeLUzxldMn7_5l1_SSMaan_Q11k3PRLK_aFKF20HxdmtrqxnWbXn2DFhQrwKyGRadiarhwXXzXz9WdEZ-1GjHYcW6SoeEyAIKT458BwNTtCv20H7kUexsgj7esduwtNA9Z7cdT_Fcmxj0s3QnKNrbwwriEjYLL4fnP3LMLaUQaug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=qGPMAzPLrDmWumgOxC_7J7tHhkBPdHSJA4GahzV1IJQUcOkZI-gWd11Mp6EHl8Ujoyu4pvKJCuP8TiLplvd25sZRIPC6srplh-bJWdW8Y_VUVQqt6HIDUkRpvSwipFZkI17TjIrZwcRuFDrtSsaZKYkx0F-D1vaUps84q5gWF1Q8TkPI0Zh45GX_tcayR0QbPlMasaOvmeaZv8CzFuBF21gWuKtH5buqqufQ3wsRcIAwTZv2MGeGWNB94Y_DtbRfYgvzPpm9baKXCX2kwJVnOQVxEwAlTK9BnyXe12TQORw0FMKoXFbXVYn014hLzeg3dSAjEhqHcYrhDJJd_2mzXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=qGPMAzPLrDmWumgOxC_7J7tHhkBPdHSJA4GahzV1IJQUcOkZI-gWd11Mp6EHl8Ujoyu4pvKJCuP8TiLplvd25sZRIPC6srplh-bJWdW8Y_VUVQqt6HIDUkRpvSwipFZkI17TjIrZwcRuFDrtSsaZKYkx0F-D1vaUps84q5gWF1Q8TkPI0Zh45GX_tcayR0QbPlMasaOvmeaZv8CzFuBF21gWuKtH5buqqufQ3wsRcIAwTZv2MGeGWNB94Y_DtbRfYgvzPpm9baKXCX2kwJVnOQVxEwAlTK9BnyXe12TQORw0FMKoXFbXVYn014hLzeg3dSAjEhqHcYrhDJJd_2mzXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=DphcUubGnEBY4wPVOpBWSjfVkdh313Xb5pedC7URcbSj_MJ0GpeeS5HyGnFLP-Ce9wTl6wi1353tMMFEcj11ZVNrQOynQrF65GNdZ1qPeH9ub62aepIx4s1HwhtptF9uavexUqK1mB0YdZxWuZMnGaRpltvnQYCcC7L9OtAEo0dDDDbfO0Tal5l6CkAa-OgIhFY00sVUTJEn-IXh2xs0uTttr01zN80vDvT1tPdGtta00uRSTPAedR2y49F81Kd0Fj4cO4MjPmvYwqYtFIzFi6Q_MWtZfYkrVuP6KSC_UMYcwkcrjWWuYAra5hUo3XtKeBlah1IuVzHB3amwrw7fYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=DphcUubGnEBY4wPVOpBWSjfVkdh313Xb5pedC7URcbSj_MJ0GpeeS5HyGnFLP-Ce9wTl6wi1353tMMFEcj11ZVNrQOynQrF65GNdZ1qPeH9ub62aepIx4s1HwhtptF9uavexUqK1mB0YdZxWuZMnGaRpltvnQYCcC7L9OtAEo0dDDDbfO0Tal5l6CkAa-OgIhFY00sVUTJEn-IXh2xs0uTttr01zN80vDvT1tPdGtta00uRSTPAedR2y49F81Kd0Fj4cO4MjPmvYwqYtFIzFi6Q_MWtZfYkrVuP6KSC_UMYcwkcrjWWuYAra5hUo3XtKeBlah1IuVzHB3amwrw7fYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=auxTgBkz5DUAru4Wj5EPm1LZu2hEnBcwDfuOQKDTUra1UQt1bnff7FitukzIMi7a8j5xrIveEMdr23QvQUO-R0i9mCei1goDL-pGC9Dp5CBOgB4FMaYFLZPUNJcp9GKJogezd24_KUE3ORXWYCjWGAEsAakOPxbQeqh69HBQFohpjNYvKuHHEGFsrcYsMyQMO7y9v56Pp0uFzpZoM-EbdJlm_yBw4AyvSDaqcfXqS4O_UH21ixlvfOsx1JaC6Ts4ZOX1WJ1ePp6lS3nDMNuylyxV874s2TnHxAcukbID5Wsus0uRD61TaSteSRlj2jeVBOsSvcWlqkEhecIGv_3x-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=auxTgBkz5DUAru4Wj5EPm1LZu2hEnBcwDfuOQKDTUra1UQt1bnff7FitukzIMi7a8j5xrIveEMdr23QvQUO-R0i9mCei1goDL-pGC9Dp5CBOgB4FMaYFLZPUNJcp9GKJogezd24_KUE3ORXWYCjWGAEsAakOPxbQeqh69HBQFohpjNYvKuHHEGFsrcYsMyQMO7y9v56Pp0uFzpZoM-EbdJlm_yBw4AyvSDaqcfXqS4O_UH21ixlvfOsx1JaC6Ts4ZOX1WJ1ePp6lS3nDMNuylyxV874s2TnHxAcukbID5Wsus0uRD61TaSteSRlj2jeVBOsSvcWlqkEhecIGv_3x-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=VF-DRoUmulZZ4zvU1bV0yVT2nn_EMmyAVrdbso5b772t_MjkyhBmewq6t1fAHoUSOIjClwxAt50FcHdb3syUve7MjaqusLE03Dfx9JslVHOKlROOcBk-39jAiDContHMBndIuGAM3G5FvOnuUDJZkqQEPxl4a3cbR2lD-eR3Ep09Ajvx4KjSL4jdfUQZO9ofREzXnbhNSIwrbxRxxzmsPqEYVc8sFTh94UC1N-4Pf49SNxg_O-jSpwBMO-_fKCEY3WbSOdc-CpeoX81F6CIS2X4klq5AmH-CPNr5E2Ark5-PritHZ9X48dv3cbZEh9DuK6OWtrOl4DrqWj19AyseyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=VF-DRoUmulZZ4zvU1bV0yVT2nn_EMmyAVrdbso5b772t_MjkyhBmewq6t1fAHoUSOIjClwxAt50FcHdb3syUve7MjaqusLE03Dfx9JslVHOKlROOcBk-39jAiDContHMBndIuGAM3G5FvOnuUDJZkqQEPxl4a3cbR2lD-eR3Ep09Ajvx4KjSL4jdfUQZO9ofREzXnbhNSIwrbxRxxzmsPqEYVc8sFTh94UC1N-4Pf49SNxg_O-jSpwBMO-_fKCEY3WbSOdc-CpeoX81F6CIS2X4klq5AmH-CPNr5E2Ark5-PritHZ9X48dv3cbZEh9DuK6OWtrOl4DrqWj19AyseyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO95GzKbpW4ybZQwVTvXpxf24D7q79Dg_sb45AmYV4WmG6Wd5yh6YQxGfueZWYzzkvMVJ29UwU40wYTKhKlKX2McUWFiV9NcJOPxX0m8QZYgGvgJwHEKuJ_TolmxhTq5E4AeQqdOCBF-QUPEQVORQ6zqga9k2HFDDVgUI_0zf-5if7cRxFFODT19ISzFS07F7Tm9pTRaavD31XqcQiHzr-z8RG9VqRgVZu-krpuiqqKvT-6ARUXswTqGvwao47dVQdtwrmxn3b4W1-YSZ4uVDfa6-D_2_vFuTRwOQ-GzmnuyZcQ4QBNm6SbRhE0OhqU0ZH3kNO0UWmL1gjYMFM6DmIB4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO95GzKbpW4ybZQwVTvXpxf24D7q79Dg_sb45AmYV4WmG6Wd5yh6YQxGfueZWYzzkvMVJ29UwU40wYTKhKlKX2McUWFiV9NcJOPxX0m8QZYgGvgJwHEKuJ_TolmxhTq5E4AeQqdOCBF-QUPEQVORQ6zqga9k2HFDDVgUI_0zf-5if7cRxFFODT19ISzFS07F7Tm9pTRaavD31XqcQiHzr-z8RG9VqRgVZu-krpuiqqKvT-6ARUXswTqGvwao47dVQdtwrmxn3b4W1-YSZ4uVDfa6-D_2_vFuTRwOQ-GzmnuyZcQ4QBNm6SbRhE0OhqU0ZH3kNO0UWmL1gjYMFM6DmIB4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac3A1uoAD_zigZx97pc0sgpKwVEG4gMg5W_FaqFOj3QOCC_kZMSQvw7wWMv6ZuNHkCCt5nrUEUWCQlLU59zFXp_48evDyUolRR3yvegcxN9jqOS4GSe8vzrFxY-xqfH4eigqpGTNcDzvuQPtPV1JRBMPhQOG7xDKam17TbrlZekj6IGzfM7ydUc58G6TUTQRcDu1LUvMMxPcMA_7xJ-MPOvGYfrefjo3mgbFpHCVF3Hsyf9a826Hf6TLYhd6fMFX5NI4xTSnpjcWQ2-rmmHB3GQGPzYQy4LYhvTcC_HuMJhz4jduuj4Iv-rdmlqJx_PrER03DRhVSptKNzqt7i3AkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=lJVZD1yr_UdFw3aMRp1rDXc3r6NtK0UZ-yFJnJLLiA7HO2bgDTLJTphmvEiyPSyON7SY5NPqwhvbZvjCSJ9kpeg1Y6TKv-NIj3TrESwIE2QZHSHdHaNqliTCXW847F2XzOuWBdPWlA6WecN3ojlzcW_Xkjgvi5r_3k88Ks3OsUxFzAwMf3SAsX_tDa-IVWnURv7Mbdcj85AmPy0tncp1TtRRQBE2EDDLsSB9kEPkZs9ztLx8Tv9ZjphNDiS40eir7A3SzD1SiqqX76Mf2L8ady044N5NTDN9mulr8bWs8M8JS-4UZYSt2wCW0sqk-hAw7XmAzX6PIYkSdxDBEh8gyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=lJVZD1yr_UdFw3aMRp1rDXc3r6NtK0UZ-yFJnJLLiA7HO2bgDTLJTphmvEiyPSyON7SY5NPqwhvbZvjCSJ9kpeg1Y6TKv-NIj3TrESwIE2QZHSHdHaNqliTCXW847F2XzOuWBdPWlA6WecN3ojlzcW_Xkjgvi5r_3k88Ks3OsUxFzAwMf3SAsX_tDa-IVWnURv7Mbdcj85AmPy0tncp1TtRRQBE2EDDLsSB9kEPkZs9ztLx8Tv9ZjphNDiS40eir7A3SzD1SiqqX76Mf2L8ady044N5NTDN9mulr8bWs8M8JS-4UZYSt2wCW0sqk-hAw7XmAzX6PIYkSdxDBEh8gyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_ikGIWgs1MiQO0_w4RgSC8kPonO-UIpOmmajXB2vKjD2cgJAAbg8uQTOy80ajWHe43BQGF5cD1jI6LtlHIIT5TVD3Cy38aZIbtYA7k66IgV-438FLujiJsfHf3lPpjBpBkG1maxvqPb-exKDSlJ457rkBl5IDW4Ncq6XZPAIHyb3veSrRI67FtSnmJnVkmaRyDzgHD_lbZU-enzXci8ruVSc-U3IErWmM07zvbF5TbcZ0td0gV5rcyoAVdNA_BqLFF3tD8vV-cQdij8cS-GfJS8D5uU5bdKAzmP2uJjY7ocU8EOJkHqQ0LYhv8Dp9WNrU0Kpdjjk77pJ-kZ97uWWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btPsMZNR4V2KKAzj8VaKef-6BqQYoiTn08lPb_YJrUqabuzPmZQIZIpfQdwrZzQsEa-IwLnMC8ohomn-XdBJEPlm0ObIJcPZXfDpdnh4pwDMQcu7N5gNOyIfUDudQ0BfG9g2G8zOQK_luw4U7QKtVfz0yl5lhw1_iVsW1gCMymB5FkXCBfYNVG8cwlf7Yf5agCw-E65_AD1vaOKD2GZF2MnGwwc_FpkSJ74yf6qLpRRF-w_oVjg_BwzU4c3Znd5N1y3pnyYBWcSwUG-WdDOGdr1BpBiKcnVP2De_ziCwScL9IQ1nOYuyVeGA7lyvfK02N87HRL2OflzSTUOCT8mJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aez2q1ym0aq_J3c7qUy14hLIT2GnJz-W5aMNfr5pUEOQcmQDjcHn1We6VPZjqyQkmaxEo_l2umDoAo-1ezHgIS4Mim-ydNJxxd4b43CY1ko8I2YNFbTk_-2TaZmlc5jwT2lICKzh4-TJlKFv3T2e8gKgwgUaYu0qxahXmjJ1yiUDC0qg3Jcxmu-cVi9gd6n2LN7rcSf69McLaUcRttTHOIiHcR-nOBc8xFx00WlD6UAEvT8pZRahSiJkrhk1YaOEUib-s1Ez7oPmrW0n8zkXa3e9NoHlOMgIcu_yHGakAXPSDxTyDU_6S3yOlF67JkvYXxTH_Ne_-a-qNmPgpWoxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=InS1Pn51dZJBRq-F6fDnLdcIRwBybviXFd0v6LIrNz-JflfBAjxxvRNaM60LtmCm4bHf6_RzwPq0PPNmhPVBpGQ-3eGpfQONrGEgD0KUc820jR5AcPa0yNb_J8c3XhFNuvC_NEL_r_f2pb6nqFMqBE-HM3rREhw_l4J-NU_crRs2DNp7Sdwg97tmD--fhfODq6-DK68UiK6Dda3L1yx7xOxHmmfveHXL7NRTrgaWVYuvXITmL5qKWej9pwrAmldozqvAcwVrCUYjDsHplVMvePa91Qt2D32Y10c5qua8TDKceAqp5CuAJrCRb1egNm2in9jMhSwW6P1lSC6aySRFAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=InS1Pn51dZJBRq-F6fDnLdcIRwBybviXFd0v6LIrNz-JflfBAjxxvRNaM60LtmCm4bHf6_RzwPq0PPNmhPVBpGQ-3eGpfQONrGEgD0KUc820jR5AcPa0yNb_J8c3XhFNuvC_NEL_r_f2pb6nqFMqBE-HM3rREhw_l4J-NU_crRs2DNp7Sdwg97tmD--fhfODq6-DK68UiK6Dda3L1yx7xOxHmmfveHXL7NRTrgaWVYuvXITmL5qKWej9pwrAmldozqvAcwVrCUYjDsHplVMvePa91Qt2D32Y10c5qua8TDKceAqp5CuAJrCRb1egNm2in9jMhSwW6P1lSC6aySRFAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9Fp0JBpE02ih4kN7X-CI7MPMnQbzyRDvc5GiDaSF3md3LUlhRsPmvkIgqAVQDePV47oxEvTNLWd30JUloiYghHhixS69xosLVh7Ygq1lwwwrVORrazIrV0qG07pyoCYUH6jdRDZFrjqQ_x5cwtGC3wn7KYId3scVMLqQFLaesK2HcA0I4hWXYq_pE_EMcN00vauU1WDJJx46keYBnASrNIme2rlPvHSVKhonjbfQM4OaaA5C1H6xU-Fbhhnfe0dWiCB7JFJLCD3oas2gOTHdknOEbkeyRcWKaYGqJfcmJ3AcblVJnfcxOZVESiftt6rhuiLrkW0BgW2PaRvbpeZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvpBptinSQuNO-BnBe-RkceAZAbk8jfr8WMCB1--bh76jc96IxIqJvh3a-jn6jVvETyAZaWoDPo0Y8vLA62mN-DxzEvLczNVHxmTES6vIkev6WtRNWFlDOeSCu2wmsoMccGJ3WBkUXONgWnRJYONedEIn_8tokcvcBQwxS24UOhxC56HIDt_t-5ZHFuWLTOfpPhdX60Oaxbcsm-DWtG9i2UQeYQtDN417UNbhAAuox1XqHMD4JjfzU-zy0EHuvGsnQmc5_GTOQqs6EnG3th7zy1Sqk3IKlRJttuMLtS33AlJbbn86q2rgF8MayB2B_kL68y7iSr52gDidZdyH1eIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-MTjDvZLcRAx1JYMA1cCg7dWjsKy4B8hjUKvhSIl_5oCb3TgN6llNvl4bmo9GiY-89e02oujhrSMEXCW9qOPiPcRwTVaQ1Pm-nI6zdSGF5_20Ep4WFKfvQSgjQtzQ8UaaxuexIydyT6XaMLhq26iskmbbPZnFLJfaqohxzbKkKYUmZOkPrCM4c512SPECfAizkn5ZFm9fVppEuUHKmfdB05gAzFIchHyfmONxsR5B1DH8O8fCNfPVm7yHlVM1Ce1GZO0EAv7IVwhVf_RrirVRL-g1M06SW0nTjGLtos5vcHkTo37g_CQsTf2GGp4Gi0qvKapgXHw3G3ECwoeVadfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHQrch5HSrj8Y0mlH_yPeECh1x4ASvbeR-uJiJn3-o0tNHdfSCEZaKHyAh0snGrRq5ao2Sa4g0V2s3xHoGhro4hQaciHfNOD0TnW93821mIPTxf1j-9rdWi7adTp1I-rYP0K7XB5rEzS1qlYdZqz6MNCOu8Qh4juSKeiQU1x97kZHgYg2CDLD3CJsms7TzoIs3Oy_Tr3QMfZeDXeNNrRO8k28VWNbm9iuPMU-GUepMHnsh9aMlnJzLdDw-XltJiKEbmQqlOclgmjtYqKQ5Mh4LqlqcAFTgmJmrs6B_KUtTX90-9gLhyAIJp92UZgM74WAfa6VuCsvmya16x8mvqM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=X6YXsec-B34s7zuvdmgw-wW4MWVfGuOcLx3xtwWAymYbxzDwKHDZzH7p1V5Ig4Sub103Ia4VqJV9q1zA9_5yGmgsCOaCtI1Ky3i5hoRRMbptyqRp3PXigXtlHi8DO_8d_Ll2pyPXcxTtO2gjl3Ncb1miTQ1TMIF6n-BWYwry5JXwEJOgWTvxnmB3u6MhlY3WAcWImsR18zzTfR3ttc9PB1pE4Qqlh9X88MtBCGuZ5yWXo-j__FHaZixjh4EcPKU2pNZzY_C3MHpr5tPANI3BwkX_adwXAvd4svtLNphwCd_h-vK__j0ZLRsabo3d_dxFpqV2OGdPYYBVhPGhwCYvBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=X6YXsec-B34s7zuvdmgw-wW4MWVfGuOcLx3xtwWAymYbxzDwKHDZzH7p1V5Ig4Sub103Ia4VqJV9q1zA9_5yGmgsCOaCtI1Ky3i5hoRRMbptyqRp3PXigXtlHi8DO_8d_Ll2pyPXcxTtO2gjl3Ncb1miTQ1TMIF6n-BWYwry5JXwEJOgWTvxnmB3u6MhlY3WAcWImsR18zzTfR3ttc9PB1pE4Qqlh9X88MtBCGuZ5yWXo-j__FHaZixjh4EcPKU2pNZzY_C3MHpr5tPANI3BwkX_adwXAvd4svtLNphwCd_h-vK__j0ZLRsabo3d_dxFpqV2OGdPYYBVhPGhwCYvBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihPKEmsaUrMRnYL-7aEUH1IqeTfFIu3AdYIAv7DnurxWj2TiuCf5oatn4viywyFHhjZHW4hsKWcpSLlm76eZgYURJiA-acnRhrITXoKiuM50zOR7P4qIEMcNKMtqevjgZeWwBtVnncf5PL27efgBkKa6pR_lxRmedN6ZrWqNmU2futbtyrVw2AVvwdYgm0CdQ3jF2h_pYN6Kp5ksRNHNb3s9AD2lVmSgfb-HjQFaMMChK4280WLFoP3W8Ba2YKwfjTvnGIwok8Qq-wHrHh7R_ImZrAWrJT_p5-02UnFjZytAedTDZzT1bJdabiddA2CNfd08lcITNRAVXXNd4NM_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEdQSF0wuG90VeiOi36PHwiPkPtnR-09v0PIgrIO50bmJr2BWLS1r6bv1eZvvc664YSJ0BHswgRurFTbd4Nkw_n9pXgv9oHHwQeRAB7PGlQ1UjZtW_0fIr6EKgscZLhbRwnITBGQm6vuhCsx3A9jRjVJ987M-YjrIAGOkF-PuzzKzEK9KZPfBwY1iFXnXpSHnc9F-iqGVaQv5r1eP_nsiZ0pi8CY4MtwPtKPG56e60o5Py_8xrTcE8kadPbkN_ZJbDUfNn2Krs_IKiJDEx3J8LWO2jAvpdVIWVOwgE31AYIp7OBKYe_o59-BZDZRsaOdmxuyyZyPnCHtHmzBsPlnqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=GysgOnsiKwhOH6zuUrnulthcSOxNJqa8285ezYCje6SGLbzBiko-uOHiFOiYNzafuC4WuT9Jm-H_7s0TII7zIig8F-a4mWutoIeRgTUE_gWAvnTkXumd3W8TCg7kP-jPMZ39FiGIglEOiysdtNylPPUeyEw7942it567eyD0AaNhoCKOQNWq7Lo7e4ijRdWL8Xps7xIp7n5lvnIUIaLWbkjSVoQkks6gRW-UeqjgTjNdWEKrbpJrfkofSYf26ogYDzhxzS6wJZ1vJL29biHbq2rBGDwrATL0zuYEUSso-P8T7sGcDOf8Ub_w8bgoFKV0gIsJYvT96mYXv6abodv4TDjyyzVTIv4nVTy8CtjEfxMO-mMnB1jpF6YkZ83xlthh9wZaONg2LPAOJvoldgMCk9Jmop_U0A_8i3VxMaNIn-Tfz2k9O4Wfp2m2Amr_6616yZ2ONgdf9Tlo5haasqxw_BOp5QTdtWeERbhVjFJNY3acSU2IAEdL-B3ZAt6585O7qnNUleqWhQffAuAwwa_pnV_ZeldZuyLSLuDOznG4gzVRLLDVdiAtyulUHQYuKEevw86kfgPo7K4MG9y5IbxUw7Q-JZBPAxw9UaArlsyvtd9CkkTXJZ7tSenstamobmD8JZ-bZ8C4HzcUuG_6OPLC2ghbrEKuRgJmZP_dlWd7poA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=GysgOnsiKwhOH6zuUrnulthcSOxNJqa8285ezYCje6SGLbzBiko-uOHiFOiYNzafuC4WuT9Jm-H_7s0TII7zIig8F-a4mWutoIeRgTUE_gWAvnTkXumd3W8TCg7kP-jPMZ39FiGIglEOiysdtNylPPUeyEw7942it567eyD0AaNhoCKOQNWq7Lo7e4ijRdWL8Xps7xIp7n5lvnIUIaLWbkjSVoQkks6gRW-UeqjgTjNdWEKrbpJrfkofSYf26ogYDzhxzS6wJZ1vJL29biHbq2rBGDwrATL0zuYEUSso-P8T7sGcDOf8Ub_w8bgoFKV0gIsJYvT96mYXv6abodv4TDjyyzVTIv4nVTy8CtjEfxMO-mMnB1jpF6YkZ83xlthh9wZaONg2LPAOJvoldgMCk9Jmop_U0A_8i3VxMaNIn-Tfz2k9O4Wfp2m2Amr_6616yZ2ONgdf9Tlo5haasqxw_BOp5QTdtWeERbhVjFJNY3acSU2IAEdL-B3ZAt6585O7qnNUleqWhQffAuAwwa_pnV_ZeldZuyLSLuDOznG4gzVRLLDVdiAtyulUHQYuKEevw86kfgPo7K4MG9y5IbxUw7Q-JZBPAxw9UaArlsyvtd9CkkTXJZ7tSenstamobmD8JZ-bZ8C4HzcUuG_6OPLC2ghbrEKuRgJmZP_dlWd7poA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=ILzgeWwRZeMcU6taXnKcmLvxYGMmgFy6nOQkl2tXDso4-qeDTFGukpE8nnm6_QVYwTSMEY0yJML9t070b-PeOy2wTEAgW2LxUFUrkYPsBGBcYo9BZFmhdVZXE5ZmxX26fEkTpy1haoFtuxlHejgVMH71Gn_YVrrEeDoBu47OqrcMRCywfoon8TfwrD178MgeoNSz9TezyPqUqjNxFU8KqAZUWCPIzFYrOLKDX4dtZtmNkAmwkzSCRAtmA8IIUODEpkpXLa8naMpjozmRkYMJ1u0QPOMepZN_-_yriePhFnDVyH1K7pM8Fjy7Rot5YuzkaxjwN9pAsgQ7yt6gRPebCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=ILzgeWwRZeMcU6taXnKcmLvxYGMmgFy6nOQkl2tXDso4-qeDTFGukpE8nnm6_QVYwTSMEY0yJML9t070b-PeOy2wTEAgW2LxUFUrkYPsBGBcYo9BZFmhdVZXE5ZmxX26fEkTpy1haoFtuxlHejgVMH71Gn_YVrrEeDoBu47OqrcMRCywfoon8TfwrD178MgeoNSz9TezyPqUqjNxFU8KqAZUWCPIzFYrOLKDX4dtZtmNkAmwkzSCRAtmA8IIUODEpkpXLa8naMpjozmRkYMJ1u0QPOMepZN_-_yriePhFnDVyH1K7pM8Fjy7Rot5YuzkaxjwN9pAsgQ7yt6gRPebCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsSzSfVWF-h8DtBie3CNGkv38kAMPDsV2mAPjrLWxX-8GJTi2EREFzQRgIPnsKEawZJn9AgBVLA1sqXgH2pCbJQlv8smTiWaj-N90yMBsQQqlpByCGNnbw7t6lQSL0ept77TAPHGpOVrHsauhmMqNBDm_QpbxbQT1bP11qlIYtN3d_QxYjAY8hsSAUAOj1VvvNrXOWVpNwZjAiTjm4RzuHfX_nVGxk5WyO_dHyh42H2MhPKvg3srnSB1JQxpXB0YOfTr8hwfxdsbwiyzVTor8vH6dVfrrDdH0Rl_s3QBETc2Z2k7LKrAg6RKAe56CfBTKxWQCsIE6ME0jCl7fT9VcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=V4Zbt5VDv4yV1f4Xhjao4_V29GBmEnowqATuQP79hsJNoDds3jrLJF6bxUrvdMwf1-2TBDPBnAM3iaBQ4hA6h1QOK0MWR9nzl7MfgPPehrtbpkFnA6kJeJX9it7_6zRAs-GQjTd-CVY6EJVOVpnk-yim9ez5fgMpfUsi2raJYLFZEg843Sr_UV-FFq0NnRm0H5E78XizNGWbxSyIPkWpXyyWJndd2r4632ia77PhzG_9uKSeFtXUgR1mjl7K68XNF1Cvh2IhWldVogQmSzIWk8tzbz3dcDthXMNQVAsySvP4tCElcWD4W_FuB_H-2aSGDGWV1RCPN1-riLilGo24vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=V4Zbt5VDv4yV1f4Xhjao4_V29GBmEnowqATuQP79hsJNoDds3jrLJF6bxUrvdMwf1-2TBDPBnAM3iaBQ4hA6h1QOK0MWR9nzl7MfgPPehrtbpkFnA6kJeJX9it7_6zRAs-GQjTd-CVY6EJVOVpnk-yim9ez5fgMpfUsi2raJYLFZEg843Sr_UV-FFq0NnRm0H5E78XizNGWbxSyIPkWpXyyWJndd2r4632ia77PhzG_9uKSeFtXUgR1mjl7K68XNF1Cvh2IhWldVogQmSzIWk8tzbz3dcDthXMNQVAsySvP4tCElcWD4W_FuB_H-2aSGDGWV1RCPN1-riLilGo24vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiK5Kq81FByVwlnJ6zp-tN7oGKTfPxT6TKqmprFee6PEcLwDFNW0YqR8_mWLxnAV037825Ky0jru_Iu6RR07KwDyTTAqkR04doMCW8Ns1L-pemX7weuPBwWbREdgFcooco-sk9HdEOmCeV9nUa54Fo5QxK_f9PXeS7MvpcnU3pvdbnVAPQ8BBixbip1RPm645w9WDAsPb9KNnsC6pyIMLqQHmSW04cFd4sgcIc8RxIu3LOewYMHiNjigLGtlb6hG3qvxw9nPnk7Fe7EMz9Ye_Bk066BLUEzDjmCkdOqt1HBHOKaRCJiB7LkBKFEe4aZoKDyAJWyrSh-_3pOIz37-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=ICRHXxAAFHjlitzNJLNQKh_8GK4AfNGZeKh5bdRh3TD3E7-63uX8TQcT42mTqUuX3nJoXTI-jSonqPJIK-1ZU2NChqlyjIHKeCsvsGLmYGrR-3qsPfEuc8JGld7UItAxqtGi8kjqXdN0RNvBNcWKnVcTRHpEX3MtV1I5jeZs3NCbpdlGweN5sS5Il9vhmhtiQf1JhPk7TA8uI6Fx0gvvca9r_oZxjAGirN3fL6O_KJkD_GAbVn3nhcSpI-HYxjdDDr5_oLK_zP_o0A_Z_iHK2EcvOlqbsUeaCDp1sYcktcCEaoc43vhe6g-ErAntNmkNuMzLIntJ7VMi_HzQAxHjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=ICRHXxAAFHjlitzNJLNQKh_8GK4AfNGZeKh5bdRh3TD3E7-63uX8TQcT42mTqUuX3nJoXTI-jSonqPJIK-1ZU2NChqlyjIHKeCsvsGLmYGrR-3qsPfEuc8JGld7UItAxqtGi8kjqXdN0RNvBNcWKnVcTRHpEX3MtV1I5jeZs3NCbpdlGweN5sS5Il9vhmhtiQf1JhPk7TA8uI6Fx0gvvca9r_oZxjAGirN3fL6O_KJkD_GAbVn3nhcSpI-HYxjdDDr5_oLK_zP_o0A_Z_iHK2EcvOlqbsUeaCDp1sYcktcCEaoc43vhe6g-ErAntNmkNuMzLIntJ7VMi_HzQAxHjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=SP4DaJe-4mNipbKGHsK41zPYy4xl_v87d4OF83fce57lCRdlW5jnYllv7w8Cv_gM691oh7eAiFOgEumnaXK3xqxKcEZFsHwCNTZ2jlKSEw05D3G4vX4lvVG9iGiFvppkNIsFLi8dWboirX_EB-wHRiVicaFajN2X_ydStqy9TA4FAzKJT7LIJnNrRmYbsvGGO3Po4nD04v-YciwId0WM74frr6JXE3OHKfAWCjCiVbwv4SFTzhA_-1zj_uS_LiQ7JwFTAn_R4i60Mu4-CdNjRjLAQSSW4ZuBVPx6Dubvior_yYf_2VGvdnywxRMkBxpmpAzxZIeNBhxtRIpcQSn_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=SP4DaJe-4mNipbKGHsK41zPYy4xl_v87d4OF83fce57lCRdlW5jnYllv7w8Cv_gM691oh7eAiFOgEumnaXK3xqxKcEZFsHwCNTZ2jlKSEw05D3G4vX4lvVG9iGiFvppkNIsFLi8dWboirX_EB-wHRiVicaFajN2X_ydStqy9TA4FAzKJT7LIJnNrRmYbsvGGO3Po4nD04v-YciwId0WM74frr6JXE3OHKfAWCjCiVbwv4SFTzhA_-1zj_uS_LiQ7JwFTAn_R4i60Mu4-CdNjRjLAQSSW4ZuBVPx6Dubvior_yYf_2VGvdnywxRMkBxpmpAzxZIeNBhxtRIpcQSn_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2PSusYI6KgO386-FJlEhyuzOq6LBNn5vvcShBG_0iqDXepH4Kkg-uN9WqMyX-bBd00hgWx8d6fp8BkiaWq-2GRKk3XpCdb_Tzd4zKXph2FVnPm7XjBpxanRQ-MWx7DOC7wdzMdtjf6X30wGsIhlVPiiFRiVU-S0PnBKZ4kLCMCpk2aN9EIJUuyBwp01nW_DN6A55CNnNprQxTRoR_792LSIbPEhhZC0y3BSoQ6OAZfH9CwcLogBP1B7cAE9EPj2VnxGzCea5Zy4RRzLoaco3tOHytR-8qDsSDbkd478jg55MuMIryy9ifeYw6SeN7Jug8UG8kpL0qGVMnsRw8aL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=jgHeGkBf0Q_MtQuqE154u21lqChmVDuF30W7nsNCWvh-GgXZGnsecXC6zlLQCXjCGLL-cfFIn-rILygAqWNpqUlcXzvqPDxyfmGtg_kvr7CbwFgIE0RU40UBB0nTc2csdT01syKS4j9UPvSFrLPeykRuFldsNHaZL4sf6tsevfiCqOvpThFCyo_BEIVFuBOuYjqsuMCHbv-1QWYKbppF4x6YY-3iHOMaIbGi9-7Nh5HMxb7V8cGPTlMiwmGKj8LiW8a1992m6-Z_uLMHpizquFfHd52zi3IxuArOIXwN6WGjgfVIwTSuQZHjaIZVK-6o-ZGq_oH--lB5oASNhesQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=jgHeGkBf0Q_MtQuqE154u21lqChmVDuF30W7nsNCWvh-GgXZGnsecXC6zlLQCXjCGLL-cfFIn-rILygAqWNpqUlcXzvqPDxyfmGtg_kvr7CbwFgIE0RU40UBB0nTc2csdT01syKS4j9UPvSFrLPeykRuFldsNHaZL4sf6tsevfiCqOvpThFCyo_BEIVFuBOuYjqsuMCHbv-1QWYKbppF4x6YY-3iHOMaIbGi9-7Nh5HMxb7V8cGPTlMiwmGKj8LiW8a1992m6-Z_uLMHpizquFfHd52zi3IxuArOIXwN6WGjgfVIwTSuQZHjaIZVK-6o-ZGq_oH--lB5oASNhesQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhQttttRrAY-0MfjvbE-0Fn81hRLkeIH5rRFWHqwndciQx8R8_LG-VKGYDxcnFCB3VvH4N4DF8tyUnE6cVM5OFZLtRpzSMOkoPoX-onKcXYbkuOIRGamVkTSlJ7jqEcYEt2fJ8NGTpqKJ8NvGs5I9doRo5li3mbuhOVyvUy0ymKEN2pniaUrJzYQmv1OYZsY4ysQ3nhk3W9G3muYTI-AXRJ5GEYTmy9dQYwZNF4TUQ4hb6Hh2pkFsD10AfdgIk0N2drdfOBAyVhhXauftDpCt2PWLdDRK32TQwKyqxlLOfhIE4Xfqs6ovSQ_WClod2IFRIkM3MjXlD22ejYTVrI1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBcLEI5faU7wadZ24wLYqPsP0lp_EgFt7X9M-RfO7wR8KkzSINHGhOFcmlPw7-tnOZFfGGGlNogRU0fQZXXu-PSlUED21VQWnnzRQWskM0CbU1IMqxwItsuwJypM79U8EYqZZlu5nV-Gy_iLDSFIK3UgktuluuEAWIr4hJxUaXqcbBTpMu5s1p7T4T3jNwjqw5Dxf0i1vU8YgRM5CT9K85HjZJDWaKv6al5UNM2CtWqdh9u6920tNiu0zXYPY1IxhDqF3lN2OZdC0JArG0fHHWY1Q-Ol_CHdf7YrJlOAQbA5t8TRBjDWcwHRhZNeDix84BeEDNg2YULuDuACpaQtRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYIFbTJjGD6JrQwtb-8ZQS6IpLqbBrCWFsX1dZnu8MFpH2brbs9hjeB0JiGLHn6u4ENkrgIAnSu61dbLoeg1gYp9Typ9nLldumawespZC_D15-wYwEhqCXZw7l6SM5QnrqaEDc_ADbYxZ0mZrl7D1z_5_7HzSOWQeioTvwCllcs7j7ZBgZQyhD_GgxO6JiDD_Hq0uKSTkXCEpnnze9JbnxPo_hcTGkmWd2YzLaC05Bdx6RRAhz-JEWxjkXAmqIlCpxpQbS7gd784Kfa-DmFXkZ04zbxLD2KuVub3jKZKRLneXlsVMj1c5TFRQRHsSij3w7w-81wfoxM5vTqvZJQGgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlvn43sBnASVR_gH_gccGxjSZRhS6LIdJManIGbz--Q3Ra6TKi_Eckil039NszRNS15gG3zydbzAPtk4VXP6lwckDTEn4FOB3GPL8eGgs4rrSDa08HmAJEd537ekpqngl0vQqHQohCjwTBpSZEHL1fcwezZEMbcgZgPm2jyH_21T0UnBFejrSsY-sulXbrijhp3bKK9X5mHhvxxYA27DJnzqx0lIs-wfjjkDOQzjBF50dAM5RqpLz4BlttP4CXCbFXYL6HQjRSwFAzPBmwEun3v-7GdfwKgR0DHjXegjY_FhgZtgXTES4pRZdWsnO86dEtFOHYQQNT7ahdx3bLITNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRS-q6SU_zEYeacUXyGsccgaPjwNvAm6vAHja9yFeLoyn21kwdA0asPE7Z4Q1zUWDB1gfM4_glw_3JfWxuECLgAF3pJwPP1NxdLYR9S8mdyWovr6OaiOV3VxaN8eJjny_DGmKH8WJioyN-lJLfJoSbiEFARubT0bsG1nKwFi53lAM-h7J2vPFQyvY5v05EW18kstvH7lrDLmZ_E2dgo2OeWY0Ta0NrTeOw4fvQ-haC3_L_ob5Xgzbn_IMZa8ScpIE4MMZ3jGCcTC168efpIT-mKXh8_hh4FiTfAa1pgcQFlAjKjDY3sqilS0ZshdoMaoL7dOQTE4v--wp_Pev9Dtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtL0UiodQ14E_Wh4oeFewF6UowF-HAmeAYy0ffLwpvK4_wqXKOj6rZNwCKbCOhyRCHUEJhugYwVOKAIRRnYfBcZJvCvCnOaK9kfWbPGcqQFOEhoeExHCFGzibxh6yLNyNr2-N1Q179n_3yPV3hLM7oEGPDUUV9sVTs3SwXZ9yWwfsRQS4OEo7o5betl0sgzD28UQeeTpeSDgOeARzY6PvkdaWzzjQF6PldI14hvKDLenawjfZCLDwYPzQfnnueas66-MaYdrkKE4N_bfqutMfHSe58FT6gFsd2g1ZWVdjtil0QFZjkSrtRdfBo1Sjm-BNrfOUC2w1zAvTtrr18eOrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=MGuCSa0ArVfn84g1NLzN4AxxIm14CpjRYUcGr4OrjZuYYKqEToQVtcjo21ra6EhEyHnRqZDE5UZscdSfalBWE-zl_yBJj_0flqPSFb1hdvT01-RMaP9TKBXrEhqyGEqZmsQymbZfaz-7k5OYo0MAmeN9fLStGupo5mMVFOB28dWqJeR2Px2whiL72Ime33wiBklEsfgfbUzgGL7vE-sxZqDanEmRDn5dqo6LTO6feQgAjkC3TED-_bE2RPjz7N7lmhljuUcFnnZi0BZ0crdq3eE6aLxvQ8OOPakch0rX81zESQ8DFSmL7MJNnaFyQoBDJK2BF2FYpzeK3jMst4-cNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=MGuCSa0ArVfn84g1NLzN4AxxIm14CpjRYUcGr4OrjZuYYKqEToQVtcjo21ra6EhEyHnRqZDE5UZscdSfalBWE-zl_yBJj_0flqPSFb1hdvT01-RMaP9TKBXrEhqyGEqZmsQymbZfaz-7k5OYo0MAmeN9fLStGupo5mMVFOB28dWqJeR2Px2whiL72Ime33wiBklEsfgfbUzgGL7vE-sxZqDanEmRDn5dqo6LTO6feQgAjkC3TED-_bE2RPjz7N7lmhljuUcFnnZi0BZ0crdq3eE6aLxvQ8OOPakch0rX81zESQ8DFSmL7MJNnaFyQoBDJK2BF2FYpzeK3jMst4-cNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFKhgh7KF3B1ZfY6i4ZDywMmMcpW-ACXwHwZO_Jl1kHq5ST86RO0i3-1_kmJ7TxgwFk2mOyF2piSJjlnjZI784re8pYOsP8DfCwcgxNAmQhehzNdUvhzeRGjGQtj9FAS9HrlKs3k_bklD5rX8nu2zLjgdY4IzwufLSlujLebmDTe1tTOwET8qFW-ds7w7gc0BPhhNbipTCzK4mlAgDSVM-dw4o1UQXJPQMm-3T_9VqmveEb9g6D5-mguOpimkgQuIXLGxsE3EWVPfw6wC5l-8fzcl7KDUXOeX3g4jYu5aA3ZH4RhQ66jFf_WYbZoetv4HBStvSuqcSpswi5RhzL2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dekpp82LQo-a_4iV7OjTBupv3h4-N7Gxv5H7dgZ5Ewi5ItG-oQ-72pNe8rDex_lgE0vBODp40A_98lV2JBjzezGk-SPXrEtIQdhUZnX_6ZmYWoj7c0knG_vdRGDwbQY9x5Jh25tabjxfYD9onLDf5YFkUGNOp8oKQ2Ae9cHlWFfTJ6VptVvnjxXmNDmbMoqTnpVsSnanyWMXGNnu1zYeuQLYIDMUO7Hh2wRFKonLyqqe25SjPzxUFJa5Q57YE2VP-OPNYnXeaxQoWOMVMO3h94fs68B12FlwS37sGC6drOik9Ylk_gbCSK39oW8GWfFucrvSReQr1pP-xedzRO7a4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1JzLd-6PDRO_U4UrelPIcn5ZqbvDrli1e0cZC7B-dnrSbfGHu3WXQO0Pc1JwRlpdnfYFh2NkL-yDJQks1R1ujy2Kh9vu5h8yZaFIcT-sI_Egp9mqjQ9IHFCsxI5cuW2gED7CbXfyoxzNH_t6_5ZVdCIjhIZiSQS2j1SwbHSeAOJ1oDa5Exy9wso88u1P2YZu7JiK5TBqbdzDdfvZuZ4lEW_Sv6WIp-0O5VZNWkncnTKl2suPCB3kSupYc5FbZiq2r5emUs1I9KR4CwgyA2PjIs4EMyPjBGC_FyP4D_3QOH4deFeIsE6XLkX7Yv38EopxzQTlxOEo9060NPqEB94-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9HBfi9lghPHRN14X6Wlx4LBeIJOPR0Diiy6EqP1ul5Z4hvNGs1kIdj9Vc2iUAEOLrUsWkyEjQXgYACxSocZkkY5_4EbrjByrZxo-bi13RYb1yVbs0i162_FmvCfU5ae7ZTs0VV2rcnp-4fPAmMZrfIJ1ShzSnhpznbOAdOxvkqeoTL93QUypiOd9EKmn_aVSwcAaXX3rTjrJqMWjnlTjPomxOMfC8S4m_r0NSdxdHne3JUz5eHKSUNZoqmCkhImfuWPGxfWZUhHIy6ULksa1sa3W6e1Tat6FKXQFuShyJOQMcSEA-84suqpg5TtP-YiPDtQ66p1i-X39vO3qXJlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=l2qAEQijxXCUX9AyMXd4Sch8mX6WnrF5QVQKNlPx3ye3ozEccb4GwyZBoJxsFUxEQ1Xlg5z5GKfMvBNfYlQ4EXy3jw_jPQ_yb7NhVwa8y7WthkLhBUy6XrlNxdROWhl-GcWmwhMZZuYF0cejxp7ZCxjoEAJSRFa4RNx3aQZD-ZbxrFD0h-JCqc_Ef_vzlZBCkdQG03rPSWgIukk1HeaQ6rdXEcgKtXql6yBHAmcmd6ek2uPtvOjEg2V7GEy1vMIotzVOtSBTnM6y3KwoVChmGkSg8u5rnBnEGcI5CHqMF4-xa2UWsfuY_6yHtsKvLxeuSUMtG-5ILEaKIpWpGULvZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=l2qAEQijxXCUX9AyMXd4Sch8mX6WnrF5QVQKNlPx3ye3ozEccb4GwyZBoJxsFUxEQ1Xlg5z5GKfMvBNfYlQ4EXy3jw_jPQ_yb7NhVwa8y7WthkLhBUy6XrlNxdROWhl-GcWmwhMZZuYF0cejxp7ZCxjoEAJSRFa4RNx3aQZD-ZbxrFD0h-JCqc_Ef_vzlZBCkdQG03rPSWgIukk1HeaQ6rdXEcgKtXql6yBHAmcmd6ek2uPtvOjEg2V7GEy1vMIotzVOtSBTnM6y3KwoVChmGkSg8u5rnBnEGcI5CHqMF4-xa2UWsfuY_6yHtsKvLxeuSUMtG-5ILEaKIpWpGULvZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVCBCOHPiKt-c2XytkW_InPa2EwDvt4KOY5ANTojM37Pr_fUwYmCMZPY-yvDjdo13HU49doyadySGwg9hRQx_tdqF4737hRh-kCMxRRO7ENhU6DcLOdCEFbd8laVR-hzbg8z-a_PxxMM9vBbYG97LWPxhGkdUd6JAEoCB7dKCgCyssV3U5Q6bLQGwlrucoLfGlsb1TUkQ0QeBRBfI4EPabISJOghtkhRxgwNc9nnCNSljJQn-pSnVXY98RPUy0GYOT_iT4Y-fB3di_7y-Rp2H6Zk08QeU8gza-jCaXyiIPlYc7BT9JL7Vf10xAJB0Q2jVrOUJCpTwCwPCTbYho9TPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIrFF1rpfKHG2TN9A42B-biv1GA33yLxVVaebNwTFbySR-5cnvk8Lx0LOyo7ZvuDubkjPNbJb5vDws4Jr0uKusW_R8UD7Wo00-WHWSrqZoh_6R4Xafez3ftFtfApAhaomfWoHzE9B1n4jdvr-P6mdkSIcrvmzGvZ1ASpZ9ORE39ALF6ELrA5j-WbBFooqFaCBGhxl2fQef1KGTSHe5DlGkLtb9ud-ZF6J7_RTYcgRHWOtrvwp_CRhSJKZzitHhzuij23rVVpXejkD6WqDzhSucQuGY15f0FEGAo1zhAAZ0LSbPXPvwncontmWI5wNkSr9z26rwWuMu55xwfbEZudxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
