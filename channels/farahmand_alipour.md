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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 03:12:55</div>
<hr>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=sqxOdFoSRfU1xFWOj9H2KGu56nSOTGj4NJJhhrGDUTFsfv68ApkuWMnx6VAev5vFF3VBEejt-Lh8Lty0Pl0qaOGegfscxRnVOFmBiyzu52o_DtQ0bfbM0RKtHvRyoQPmOLwUE8lSYCO3rGXgtq4s6Txxmd1GBk0Q8mN0EzUC4OGUVKByu8skUuiaH-v440cXNeuWcH-pw6AZSyPiZ2zFUivOrIMJ3PoK9VK-By_ZtlkvcJ1b9ml7rudSmoSzo_vNL1Hq5-RyEgAFkQYrbb90PGmF_mfjW4qTgAKEs_M0ORNPkzusmBqIHZr02g59BrwS2ON4RQLkqZcTjR-5ZcXpxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=sqxOdFoSRfU1xFWOj9H2KGu56nSOTGj4NJJhhrGDUTFsfv68ApkuWMnx6VAev5vFF3VBEejt-Lh8Lty0Pl0qaOGegfscxRnVOFmBiyzu52o_DtQ0bfbM0RKtHvRyoQPmOLwUE8lSYCO3rGXgtq4s6Txxmd1GBk0Q8mN0EzUC4OGUVKByu8skUuiaH-v440cXNeuWcH-pw6AZSyPiZ2zFUivOrIMJ3PoK9VK-By_ZtlkvcJ1b9ml7rudSmoSzo_vNL1Hq5-RyEgAFkQYrbb90PGmF_mfjW4qTgAKEs_M0ORNPkzusmBqIHZr02g59BrwS2ON4RQLkqZcTjR-5ZcXpxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-thAneT0i8IHfFu9t72fBzz4_Gcp3Lj7pfjP774Kf-5Y_GzT_DhK_Wotra5h4YfY6uejTQZQkb1tmo85wphu_oz-R4rbDRACJDgWHl0swkVvebHQcsl9vzt6NFsyzV7Xi9gR8pfMw_tuvHmyrmEtutIoZfYkxiYfHWfCmjTiDrQoeFZT7f7iWPdmN200ctEfmOtc2bKLxggSJ6uSlUcyhEL7g4mmYVKJDAVFZzfyOd-Yi9lz0QS5GbJxnw3-uJY2qOT2f9ioNhWATHwYhhAQq15PgBDm6KaAJsrdo96ToNBrAfQwyipWxVPfqgRk5ZdsBmXPbG_0ptHd_37y2YeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4mVibPBw0eTr1gRTGNQb3XRCfny3Oz-uh82TwTsV3xvMGClyO5fmI6shvbZpKO3XEey5XidRloasQiHdbrALRSFQZAnisgoaRceVWlI4CTKNGoB00Ghe5CNX0baKLelkuhdT_iQQYC6R1cKSkDT-QdKb7xG2HyJeYdTcbpNYQfJF62EvT2qREMpgg72uID-BgYQXRuufpMUEYKXaIsoR98w56qi5eDOPV31uMsOMUmdiiJb3ba9oX6hVb9z63MOK-DUDfFC5X88bAtLXs62907JLlWfcpIy_lhoy1aIlLLZEMtLoo-fdn5qg5ppozUDL6y7ocXanJeMU1m4OJcOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcTQKFWjSocS4SiURLk0QU8VKDJbJ3ZvZtIoL1Zdd7eIdtMnINUgw_suDMlRPq4xhGD6J0PnZxqPoF66wOX4C7WEz7hxwOOClopXQsFYYRzQ0iSzd5ABJrz437HPxBx0YWK0hyDfctCvoXwczBiCZzg44nk6rzxYvTAjNM2AsjA1-Gu_tKcPl-ZJbe9q7JOx3vxoA0dF-I65tgvlGG5qEwDNrXnq6GzmjAM46MEgTuG-sFna2fqwyqIHoaSs1ui2EUXCQTR0oDJ54xGuHn6N3KV6NA2eOQm9L9KpxbkaOOEH4_SwYp1Oq8c-x-6GbqfdkzYgSTAkeGhAnpkk7K8MYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCih9Wib4QqmE-nmlaYMaTAww_1_BKpyJYTVv2ZOMd-hrWF-Vp44dbm9FbzDE9N4HtLIm5Ub1jnCNU4X5D1fHdGmw05wH6Dr2vU3CObOS4VpKgmktmRRGIpaV1PlGOgUTuovF6m78HtxKYgvobyT-yj91baQgxlHG6Ipd6qnnqWyqyM30J82m1cc1RLEPag1GodvEYB6jsqQF21Y8lUllGZz7SLtKkzRt-pTpAXbv90MDW_tzZIUSG4TiIkY6j118Li1QiqjEj4v-2pSQpsjmiOuB_MZG4JxeKK35Uk09rehQc54HMbegpsgIqf6zDnajP2DQ1gq6toc7KwLss85OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=EUs3O-rcTBxN1b6Ro-k8V1OqRxa6_ArXvwScd-uOTNGRZMkGDIWfIUIHznB3h_stfVZQGwf1_qKxLT_MUTwKy0-KOjvg34mezm4rRgSJrZnsxv_HE3s7-K7FF2dDW4BR67q3diDjrBgeC61Xv7V1eiiqUXaqRj8KwmHSdtXethZYTCwBjFlCPt7yOU7BAFrh4cgzdMt2kdA6YKFlHjAn4zZQezx6alg5-6fUxUiJAUnrIRJRY_md0J98fMAnRoGT1iMIonhFx-FMmh5a01p8wzsYBeu1DnRqX0-rd1lgSjiY2T5ZyFUqTdnSPFBKGYma9wrYJJNqcxYglgB9Prtn3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=EUs3O-rcTBxN1b6Ro-k8V1OqRxa6_ArXvwScd-uOTNGRZMkGDIWfIUIHznB3h_stfVZQGwf1_qKxLT_MUTwKy0-KOjvg34mezm4rRgSJrZnsxv_HE3s7-K7FF2dDW4BR67q3diDjrBgeC61Xv7V1eiiqUXaqRj8KwmHSdtXethZYTCwBjFlCPt7yOU7BAFrh4cgzdMt2kdA6YKFlHjAn4zZQezx6alg5-6fUxUiJAUnrIRJRY_md0J98fMAnRoGT1iMIonhFx-FMmh5a01p8wzsYBeu1DnRqX0-rd1lgSjiY2T5ZyFUqTdnSPFBKGYma9wrYJJNqcxYglgB9Prtn3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=sRtWqlRc8mKZFT2ycHcA0sBtiuQK6Nb_m1vQQmSXQo4UC-y5j2D9Yv_0UuYwrIedRL_ZLqxX8H7MiCnz53tHV51Y60AsWuui8eu-he5odGwHNl9SLfbnyfKPGz2VhIcKNUNA6iP-dpyiHq7k7srNmF8s66wEw8jf7LyMhQKXPSQOmqGTMhzT_AuTI4s_sZGcloXTxii4ylK93GOrSoHXMyGrQj_7hOiOZd9MLwmaOaNhUNdGClZmwovCvfucEtCUL4lp0eN5mkCMYCbnX0BU-KlnZiNUQA5T05puhCDaN9-CV-RoiP4bJDM1T05brc0RKI2pdC29cjjQbQOSY0Kx6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=sRtWqlRc8mKZFT2ycHcA0sBtiuQK6Nb_m1vQQmSXQo4UC-y5j2D9Yv_0UuYwrIedRL_ZLqxX8H7MiCnz53tHV51Y60AsWuui8eu-he5odGwHNl9SLfbnyfKPGz2VhIcKNUNA6iP-dpyiHq7k7srNmF8s66wEw8jf7LyMhQKXPSQOmqGTMhzT_AuTI4s_sZGcloXTxii4ylK93GOrSoHXMyGrQj_7hOiOZd9MLwmaOaNhUNdGClZmwovCvfucEtCUL4lp0eN5mkCMYCbnX0BU-KlnZiNUQA5T05puhCDaN9-CV-RoiP4bJDM1T05brc0RKI2pdC29cjjQbQOSY0Kx6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=PpNkWh-LYhcXKzi--__peYv4BM1NW_YOstqn6UkdDmJaqptAg0HsW2UslKaoshBioVMYTDWyyrp7JJC9Hh78PimgGNu6cYN_tQDZbXhKLpckvqW_RnFiq2e--bjJcNQ3nKUGxYnxzy8Cx0WJSEM4F1dYwlJ0Ozth_WgGv02ffoUBskUB2wZqHvtj2mPmwWUaM5lVklkIGgWF0w2uF-X9TIGRjrSD8sOSjlDj14AVu16c33DNFwuHmoa7WiBojQdn3TTX1kFRBhLaYUnpJeZNXqhNAQDoUHTMVLpD7LL7q9T6fxSvfDPLHiwBbfzCq12avdVCxWl4bioahIQACzPWDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=PpNkWh-LYhcXKzi--__peYv4BM1NW_YOstqn6UkdDmJaqptAg0HsW2UslKaoshBioVMYTDWyyrp7JJC9Hh78PimgGNu6cYN_tQDZbXhKLpckvqW_RnFiq2e--bjJcNQ3nKUGxYnxzy8Cx0WJSEM4F1dYwlJ0Ozth_WgGv02ffoUBskUB2wZqHvtj2mPmwWUaM5lVklkIGgWF0w2uF-X9TIGRjrSD8sOSjlDj14AVu16c33DNFwuHmoa7WiBojQdn3TTX1kFRBhLaYUnpJeZNXqhNAQDoUHTMVLpD7LL7q9T6fxSvfDPLHiwBbfzCq12avdVCxWl4bioahIQACzPWDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=ncXGbYG5jnvquXnzH_EVjiQdu0sAGnBV7PsEbOFGkK4ufRIn2-xK7ji44X3zv1S0TeGpm44gTFZ--HBlImOSIjHN0iVksRcOovMVBCr09FZgVRJlSB84DvBAlc0hebmP0I5BQJuBx2V4kOTa_DI8_bd74sOOm6Ug1nbShEWrhpQ9YHQxn8WjdQaw5ej2SVLIda8y1ZcqoBHH9x_q-2-R40yqkoqnKgWFQqohoLKIyMo_yhjnneOC0hMjl50ZLyXt_rm7vfQ0tXuJGDEYeIStmufzkz12cevN1fvTLnSLRGWHeHa29qLzd4Gbm6gVdijAHqJ4uirLokRslmbjVlsSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=ncXGbYG5jnvquXnzH_EVjiQdu0sAGnBV7PsEbOFGkK4ufRIn2-xK7ji44X3zv1S0TeGpm44gTFZ--HBlImOSIjHN0iVksRcOovMVBCr09FZgVRJlSB84DvBAlc0hebmP0I5BQJuBx2V4kOTa_DI8_bd74sOOm6Ug1nbShEWrhpQ9YHQxn8WjdQaw5ej2SVLIda8y1ZcqoBHH9x_q-2-R40yqkoqnKgWFQqohoLKIyMo_yhjnneOC0hMjl50ZLyXt_rm7vfQ0tXuJGDEYeIStmufzkz12cevN1fvTLnSLRGWHeHa29qLzd4Gbm6gVdijAHqJ4uirLokRslmbjVlsSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=He85OZZysVkYkjQ5ck07q1Yqpz85YdkTOB067hHEIOnBAgis2CcAvxxSjuJhst0bbuJCm76gDQK6A59_l0Hn8Nrq1xatkfnp7MK725bYi4apVbLm3kpUXdNIfVSffLX3b_QQqXOk-no3ikYn9bHTRt4cc4nvVLFEyjfid0YbKEFa6P7yofbpMNawkJKscEg_dqfoMqrxkf2zxhu8zmdvTK9tu0b9fRCjftBhQYTCzX8vV27rly6UfUb1NrWuEpA8m3fKDGKnaWVdJ9Uf1f5a82Sljr6_VUNYLcsc2ezhbBQ43dtJapSsAoT_decvbUU4kL5eDvEYg9RGGNghYEL3qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=He85OZZysVkYkjQ5ck07q1Yqpz85YdkTOB067hHEIOnBAgis2CcAvxxSjuJhst0bbuJCm76gDQK6A59_l0Hn8Nrq1xatkfnp7MK725bYi4apVbLm3kpUXdNIfVSffLX3b_QQqXOk-no3ikYn9bHTRt4cc4nvVLFEyjfid0YbKEFa6P7yofbpMNawkJKscEg_dqfoMqrxkf2zxhu8zmdvTK9tu0b9fRCjftBhQYTCzX8vV27rly6UfUb1NrWuEpA8m3fKDGKnaWVdJ9Uf1f5a82Sljr6_VUNYLcsc2ezhbBQ43dtJapSsAoT_decvbUU4kL5eDvEYg9RGGNghYEL3qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO96Q9pyGLorWgwfbJEMSxyxxJt7jfbiBAHdEDCcraVKKtpBpnO9Civ-co84YDVqEHpZWnITsx65wEutVNOVbRl6zrVEZ9TNClwhJpqbv7mAHxeuw0JBR_LWwPnQ1cPpxCh5e_KphgY3q09eo53qk8Xq3x85GdMsKzG7bet1vxfw9JVJLeWHccQQBjz4IYU0-7b6TkRO14zf3dW5-LEhoay5v8ajn6O7woORmpWOFLL1k34VI7RMjItgvqirLmKYbgaJhlGZGO3Hg_qKd_I4d2Y3j4AbF7M31Cn4qB2UADI9M7hGa4k-1EfkesJCSaEy5Ua745Lqu2XMRZz9LB5fFD8yc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO96Q9pyGLorWgwfbJEMSxyxxJt7jfbiBAHdEDCcraVKKtpBpnO9Civ-co84YDVqEHpZWnITsx65wEutVNOVbRl6zrVEZ9TNClwhJpqbv7mAHxeuw0JBR_LWwPnQ1cPpxCh5e_KphgY3q09eo53qk8Xq3x85GdMsKzG7bet1vxfw9JVJLeWHccQQBjz4IYU0-7b6TkRO14zf3dW5-LEhoay5v8ajn6O7woORmpWOFLL1k34VI7RMjItgvqirLmKYbgaJhlGZGO3Hg_qKd_I4d2Y3j4AbF7M31Cn4qB2UADI9M7hGa4k-1EfkesJCSaEy5Ua745Lqu2XMRZz9LB5fFD8yc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pkh2FZVDN5nCIkYfiFK4LTRcmlRaSePFecd1d1aX-_yjbxK0pwxAQXhrYeDa34qTCS8Sk0LLpb5qutU2cS1j6ShBSD11J4DNpKVefqqoF6K58SlaQLGViJLzHg7PO5HZBDL6m5DFZebKFPczVaTQjmr0vCFvtmIYjT8KXaflsYhmVPAeTLfRko0Pvpt0nMvud3qBWzIu6FH_SogVHLymL-LiTxxcCfYfTxQ3onUC6w-kTWKutDSVAvqEF2nFRZmh9rf5kvTXegymTVuHcDI7Zc4EZi0IB_zWMjB_WbeD5MT0XUGVyy1hF-UjU7jbS4jtZVSUTxd5IVxRTwP-t9oDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=CQAVgiT4URJFtRo7mVMn1n8DJ1TQm2b_TVufF33JkO1xh2i7JT-3R6tJ7zT5ChRZsW7XRbZ1u9-yNuHLt8IEdLjhlDxx0dLr_OaQ-wJdKgLTIIX6qDeoQOvLbS0PqG4RtCI4LmYMevRPGeGcjH7C77O74FNe6FQVDqMT01U8lm2J2ZYpVjwsSAB52o4AtHhss33vRSBZoWjiLmyH53907ZnA55UOINcoRbivxtJM4qDAo28bH5q7KIpmV1dftGAu1cTvb0x7-oBBzC-FAFet8MouBB5xswgWeL4NJOYZ-qzbxBj_ZgjEXLNPSzDYJfHmZMTbesoL7Um2ZfxIszuVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=CQAVgiT4URJFtRo7mVMn1n8DJ1TQm2b_TVufF33JkO1xh2i7JT-3R6tJ7zT5ChRZsW7XRbZ1u9-yNuHLt8IEdLjhlDxx0dLr_OaQ-wJdKgLTIIX6qDeoQOvLbS0PqG4RtCI4LmYMevRPGeGcjH7C77O74FNe6FQVDqMT01U8lm2J2ZYpVjwsSAB52o4AtHhss33vRSBZoWjiLmyH53907ZnA55UOINcoRbivxtJM4qDAo28bH5q7KIpmV1dftGAu1cTvb0x7-oBBzC-FAFet8MouBB5xswgWeL4NJOYZ-qzbxBj_ZgjEXLNPSzDYJfHmZMTbesoL7Um2ZfxIszuVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSFbb3dfi5m6VppYUvOA1ZJoVWG4WAEAjUcjAa3ZZ8tN_kzppFNtbhHyhgVcSUm-4dDwyKBBIy28vBjpSGxRKhhqd5RNTepPn1yQppufcd7grwrX-Z2wOE3FgCMgd6F4Uh5g4oG02fu8x8rfh-CGMNI25AR33tI0QoBVmMPLSF_TEmogMHzyw8uKopXqtU8ZfxvXpjiGPzXuzm1dDfOlwtAFggVEDU0JqwZhxKlQLRVP9_OyHnF0zlAmlkvE5EVpCErzzZEYElYma4c9x-IR0JWB5R2z4tnBJOpCztwLaGfZ2mOSiUKFodr7ggaVBgqmiWEVYSnZ9zRcdqKXOVow-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3On4CliEzMDco_oI-tghFhubnwpSWZbL-OcmLuW5mkK7Z4ACE3gCUUVY_8AVDAIw1T6vI4TsJv82NNUKIjDpG0Q-d2IhP2n9iL2_FwAD1WM51VaKkBifzy-uMU_H0rshddk-_d0MuLxnMPCaeDXxQ_gz5aIrIiE87D2rBe1JNW9YXyZr3k9eP8yFRIiQH5vwYFLMrPHlsu0bttXjp_FcU2Fuamd4NRpEyt7QwRDUE6my79PJ5NQOVNb4kk8Mham5fKnV5VW-4AaPmg6pEwAOTm64Sr6URB-_tuWd6_LsIIvjkmq_a1oOPdhgqK2Ka-7YXfjzsAHIqK7JbWfJgKOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjiYLzVb6FLQzWzAZAHUwYyICjiLUJX9rsHn0LtGLXF3ROsd5kGL_ASHdvisdA-l4JbV9NBJldHywKJQTPeUWlnxK2-36Q0buFLrMzvaBF0u0b0SQnDLxs7q7sIBsuX2mRuqEKCf8H-JSc9X32BELPgFbv68zQj6VIGxkal_kE7ja1qq-G0ZEWlXEdgZdVO9C1FvZaY7C1veKmF29I3SErKofKcZv8-GE2TU-m5obxBk6C-8RMXv_x1E37dAOzqNj-864-xnAgh2jvNsJv33AcOKF-mN1Nbv7XzhAw19Xln56TLQR2f159s2NY89QHZU9sZrh-jOa7fZzLns9aRf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=PkRaC0QIUiGOmylPE2N5UVKFFrD-i-264jS0bygn17I0GawDlacnJidWaOqEQ9EfgdGA_CbDYJ4z1Pyr3WdIBlG4MPtUHhad1PhOM5MTKbHW4pFljiGPtSv-af4rtmX42ADjUk-3uMm0nuK90At-6wWX2ghF4UzoohDn0uSQRsDWzC3yu3g6nnSlET0_adPEnQqW3qtGICjxoL9rOtWA1NI1BB7QCH14xvLdZk3iwyLau3hGPLaRDGUXwRV-imNI0DmOymKpsuoKr2YSkMaqW3QpPV1UMb101DDWtgezpf5Re1GOj1Ut9FRLize5U9GSW7Cpmv9Ws3OHzcVYpvz--w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=PkRaC0QIUiGOmylPE2N5UVKFFrD-i-264jS0bygn17I0GawDlacnJidWaOqEQ9EfgdGA_CbDYJ4z1Pyr3WdIBlG4MPtUHhad1PhOM5MTKbHW4pFljiGPtSv-af4rtmX42ADjUk-3uMm0nuK90At-6wWX2ghF4UzoohDn0uSQRsDWzC3yu3g6nnSlET0_adPEnQqW3qtGICjxoL9rOtWA1NI1BB7QCH14xvLdZk3iwyLau3hGPLaRDGUXwRV-imNI0DmOymKpsuoKr2YSkMaqW3QpPV1UMb101DDWtgezpf5Re1GOj1Ut9FRLize5U9GSW7Cpmv9Ws3OHzcVYpvz--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv-q38zDJtQr1nptmS4F6rQN_27UgC_7pLUjgFNWC4lLg2oi9KOBPopMS4oZSAb1mhFu9sNlBOGWaDUvpyZdHU7-cPWnjEp4tH6eigkCIcrPWbCZS3Z4Fy_pMOoGshGD72YsynhJk00w4M4FO7sJYac1CsA95dqhQvGTlmBHIRkpaXN65G5m4TZ1ZOS_S-BWuuXebQAX-Au6ovxwk_c7ZyHcHi_FcA02gjkWPJgguUso3zJ_Fy6vtZC4KIxKBnaG8xFx4mDFy8gSKMr_3JQlBLXzKyLoxElaiPz7RpZwk5NNHJ16sjh4oRHpJ9L7dV1ddLiXWOtTehVWK57eLmRaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJlkylajHRRRw2O2QGeetO9X2kMOcUvmLpbPM9uXw9ogQS5PbFTo4cfUx6TUbDX4I3xmVT42WtMhcUC3TmmuxKkqD96AvCxlDwVzCW6XlVM3Wy4Ig1n2il5U5sc94Z0fGBERKceJzoxth8azCLI3o4B9PFNe_dhZwIiOLqzOfezY5qLNPVJmEl_pGLOCPFAO6U4395OBlNgt_GXFtFbsiXb-8jnQXOLHbzW3Z1rD-yxRT5i0Z1a5Ko5qIVGEwdNPi4Taq_A89ocq3iSIHTUsdkS-Qk5jWjmd8R_S9m9dn89WX5zVpCxOBKu1cyo4cimEBQ4vWlOlyVprSeSEd-LrJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGxlkeIHMcQpO8cYodYO3R2xc4cAS0lF5U9uRJUiTTMgWlypjwe2MU2UpDSE-mzogjCnJINqs7Qi-Ff3E2KFFTCd3FrrfcOParOXNOwtFJLG1wBzWw5LovN-GDSQQVLOrBFoSq4HDZ3o9MXCWknXHXCrDwGQZEtoSsnEhxKDdRcGSjPjCX7NR61-w2yme1iQOIk9uwcG51Xe4mBoFCIz-DBOH-jr6Xh5WbIuDn_fEh17Nkh0rfWJ3rQdmctIYMMkX0GnA8H29-r0BxHPRPULfMjHTXSlP6cPcRobmIzeUyIOQprSTeTMEekvVG9Lod6w7EBQe1dH_OoNZABJw0aMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vieDyFa2Bz9VviR1DSc8VGBvRKp9CYPtW6O6xLgL51ebiCsH4M4JQO760Tcx9stgh3uH-Efcs7_zEMTmNrS1EBV6k-TncQwYzwcnghiYEO6DAAbJ2YznbzGoiQrWilny5WVUzl0RAyZROuSfKayyz4WBWVpTdKb_9JHiAO3ziM3iBg4deKY2D3R5GZwFwn_ww7GAcXk1-TI7yBN702uEPacxsf3BV6XVgc6u3A35dQ2Y_Vsrie3ensXWZKIcAj9HiFGo1dPivqE0lvj50GoRemtOyXeOVyrr5NkbfFvuhKaIXcQSDnuhPJXJ22H5K0X3paTMVIjefAwa2jJMoDSJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=wCSuElKkumM5sIoBeQhpkgRGFvEn-OnIEFvSKZTngKfe6odOQLEznNGrNON9K1H0g-wLRKsrCIN51UwIKCwB497fzRuraN3cY3OEyOGt5ALK_5tgc0EMEWCMAtRUhoAWXvjvWM5cykGmnpJQUv8gyrtPlGGV7CJp6X4xQnoWpOZuSIE0cwF9rUkSZdtf28YkMehTxaiZFHcQnnpFrM8UDHRZxtk12HZeSKHdlsftrVlKB7JO1ag0o82mSJ8q_1--kZlz43mWDx16QhNCJcKunla950wR9rPGOs__tkqiOssHkz6CNjnMwEuheAMpOs55_JtKcZi0uWcIfYdsUytuEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=wCSuElKkumM5sIoBeQhpkgRGFvEn-OnIEFvSKZTngKfe6odOQLEznNGrNON9K1H0g-wLRKsrCIN51UwIKCwB497fzRuraN3cY3OEyOGt5ALK_5tgc0EMEWCMAtRUhoAWXvjvWM5cykGmnpJQUv8gyrtPlGGV7CJp6X4xQnoWpOZuSIE0cwF9rUkSZdtf28YkMehTxaiZFHcQnnpFrM8UDHRZxtk12HZeSKHdlsftrVlKB7JO1ag0o82mSJ8q_1--kZlz43mWDx16QhNCJcKunla950wR9rPGOs__tkqiOssHkz6CNjnMwEuheAMpOs55_JtKcZi0uWcIfYdsUytuEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cua5lpEW7DZMHuRGSiN9ltxtCc-BeUSrhDHa0hdjZ2MDmzgaCOroxdxAzMLyx4JvPMzShVdNiq8zeL9cgk6_kVz4AiAoLVUWC0ygzj8c6VjhnZo8i8UqZed9KdHPh-Ge4-xgje8nOs9EOtRQOdNg2ViSJxwt3YL5ue81IjOzTHNwOCdqNk9u5dsoBZrr3GInWLHmusJYU97DBB2lCB-iJoHU_qa6darqEQ0mZZVDEeXLVEnUvXtRnYc9Yt5wu5dQLx0mfxtdSYTI-2HmI0UHk7jwHwNErkOw54HZ2iaEjDaCIC5jT37ACWcMA28VFuM--EkTdCU9WQ0xmEU--AbYDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnAzJWJl4RVcSyG3VU6fmegq5fSnBJvTpqQxAw00-SH9EWwaINbJxHj9-QP-SXKdPMVnOREfK0G0icQjfSbdJp2OuV_0iMRPnQcJhG_-Uo_vVQij6hujqcJ8G29C2MRQSrmCKztQHyl-zEcxhWApgdD470CYwnQBtH2b8ofLifhg5WSfahuDZnGsy1Fdbw415vzPz1jnAwQY42Z_aNboGRD14Wm2kW8Wycv7xh4UqgSsQ13BO1z0pEBuJ_tQtVKNHvSn-8j2iRXf-1rFZf6WzU4Db37u5leKbvBczTTlYXM3BIE1K8U5NwwX9SXqAMoGBephDK7JAGZzNNIE9tmzRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=VIl-okdbHk40ZU5ipvPKae-5ViW8tDV7xqmULYzKpm-gb7POTUOKoWHPX5CrIKTDh9Rr-TMpx7v7MCGCIsYCLf7oeUyT-cMxz6gutbgNHbCQM3d_1W0ikpE7WSdht1pcogLSiM7yJGpvVnEV35RnGolGMpoHWmS8SPbA6TnD1dIO08-pZr4J_FZubwb3z9MgInYuI3nQouqMtbjhoL3q96K1SIXBjdPHBYMvAZJeTDj9AnWTi-G-b-Ziywh3j93tJSLvyhghQ4lTSxGLoolVb2vSNexG3EKTMdzFaaSYgiJwiUn2pYAk26osdwYZ_zGhQfTi5sO28kN64ecHsPV2aA3Za4_OdaMoA-zIqbfV9JPaAf4dFffxs-xe01yfIkJb_R9bwuGccUEMydc1NYGybJwjh8KKO__tqGjhV6agwF6XO2wh5kd949eENG4GGo39Oo6wS-K9rY1GhYkdgsA0XWAOdP8tLUi1Ibt9PVvajVBAgmue4oxvwPDT7vyd9Wtk5C_t0EBFL_ApdaUJoIyHjOF061ylh4aQMDA1nDUlK2vyJgIe9qJNujJjYZYVrNxUQgYxqATLcb2wIWxVP-umsk89X_kxv-xcokigsptmmdiN8AFLVkQzmrjWZarpngZFXc7s4Ye6IPzXaGyauHj555Fa35OK-HpMy0H17OH_Q6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=VIl-okdbHk40ZU5ipvPKae-5ViW8tDV7xqmULYzKpm-gb7POTUOKoWHPX5CrIKTDh9Rr-TMpx7v7MCGCIsYCLf7oeUyT-cMxz6gutbgNHbCQM3d_1W0ikpE7WSdht1pcogLSiM7yJGpvVnEV35RnGolGMpoHWmS8SPbA6TnD1dIO08-pZr4J_FZubwb3z9MgInYuI3nQouqMtbjhoL3q96K1SIXBjdPHBYMvAZJeTDj9AnWTi-G-b-Ziywh3j93tJSLvyhghQ4lTSxGLoolVb2vSNexG3EKTMdzFaaSYgiJwiUn2pYAk26osdwYZ_zGhQfTi5sO28kN64ecHsPV2aA3Za4_OdaMoA-zIqbfV9JPaAf4dFffxs-xe01yfIkJb_R9bwuGccUEMydc1NYGybJwjh8KKO__tqGjhV6agwF6XO2wh5kd949eENG4GGo39Oo6wS-K9rY1GhYkdgsA0XWAOdP8tLUi1Ibt9PVvajVBAgmue4oxvwPDT7vyd9Wtk5C_t0EBFL_ApdaUJoIyHjOF061ylh4aQMDA1nDUlK2vyJgIe9qJNujJjYZYVrNxUQgYxqATLcb2wIWxVP-umsk89X_kxv-xcokigsptmmdiN8AFLVkQzmrjWZarpngZFXc7s4Ye6IPzXaGyauHj555Fa35OK-HpMy0H17OH_Q6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=C0lKQxOQ-7V4BLYddWQAmZDI-TAivid5MRApq8JfZRGBlUUDWXnjiu5CnBSVnyVkE6IBw6F8_Fm66wHNcFR9GWnDzbL1XVeV8yOzECzk2rTPdFGa6x8wghOV8kKgXJvoH6Kj2hIv8mBMyRnjPsA8moAD3_S_FPprlPkBr0h7qoJrLlS7TzRSaF7d-O42FlFNPlcw7D82Dm0h1S8MepCqySK1M8yWiFsim5PSfa0kgAKfW21srCrlzBy8TR2gGqtKJ2Sv_2BqJMPk51Y55y4LFxePaZY6nOCO-ruUy4BJNXfbPM8bnANVttyNWrEc-7VPuuCPVA7aCtvXHvTIXdOxRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=C0lKQxOQ-7V4BLYddWQAmZDI-TAivid5MRApq8JfZRGBlUUDWXnjiu5CnBSVnyVkE6IBw6F8_Fm66wHNcFR9GWnDzbL1XVeV8yOzECzk2rTPdFGa6x8wghOV8kKgXJvoH6Kj2hIv8mBMyRnjPsA8moAD3_S_FPprlPkBr0h7qoJrLlS7TzRSaF7d-O42FlFNPlcw7D82Dm0h1S8MepCqySK1M8yWiFsim5PSfa0kgAKfW21srCrlzBy8TR2gGqtKJ2Sv_2BqJMPk51Y55y4LFxePaZY6nOCO-ruUy4BJNXfbPM8bnANVttyNWrEc-7VPuuCPVA7aCtvXHvTIXdOxRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVjbu662i5TA8uVGhm4HddbsUanKJL5BZe5dsnFSM2seJAvxaQxgSYIPt6fH2MZeFf4AxzcyxGnEZsRMCfRLbNrGl9n9tJwb5tHM4eFqB1N0BPixfWD0Hncnn_8NgDnF7-ITJyIp5if0SwsPJcMo0yB78gEBRpcb41sVXP27yG_iD326uutl4uB6Vv10lHtk_ilDcthPqx1h_BQLHcpWb5XdlsNWDsezrCekl15xZnzvy4T6e_LQzRXHRFrmyBmyg1bPX2hx1pN82bM6-bg7IRAE4UqOtrc0WyrABketW3W-bYLmVEbfp3-4VefEwwX_g9-84LkVEcr_s7ObdrXYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=DvbyfoJ930OBDfXdfvaZ8hTnCqjqC_sck1dsOXGcMG6R-T9NPHt_58Dj4rm-ZDfFmaO1jLjLp48gCcGs9TQjwdeTHKzOK3Aq3gXunlLZhs-KyQ4GV1EQQT77Zj7YPH8sjdEnimdj0hEWlD0AunZx6Bi8qJTVIsROr98K91ODJFEmwPnBFIc1UNm3zR9fEZ3K1JoINDsP7-ttUjkixt7XeGpbTPdAkBWcBVKruQrxPjR5-_2kdgz9fGEhD82DE2Ig_1LI20ygnRagPmvkm5TwfR6Vb49oGMrHFj6YyX1D9kfCWoieZMm_qZ_GlJFCjQOHk5pD9cF7x-m9bT3GFd9maA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=DvbyfoJ930OBDfXdfvaZ8hTnCqjqC_sck1dsOXGcMG6R-T9NPHt_58Dj4rm-ZDfFmaO1jLjLp48gCcGs9TQjwdeTHKzOK3Aq3gXunlLZhs-KyQ4GV1EQQT77Zj7YPH8sjdEnimdj0hEWlD0AunZx6Bi8qJTVIsROr98K91ODJFEmwPnBFIc1UNm3zR9fEZ3K1JoINDsP7-ttUjkixt7XeGpbTPdAkBWcBVKruQrxPjR5-_2kdgz9fGEhD82DE2Ig_1LI20ygnRagPmvkm5TwfR6Vb49oGMrHFj6YyX1D9kfCWoieZMm_qZ_GlJFCjQOHk5pD9cF7x-m9bT3GFd9maA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjCdAEE4ZC64qg4oxWNTxuxP8SKYslcCIo6drdv9Ac01pGWpxfKd3sWqHOK6N61u3C0QzcV4d7wWaLL9cBW4qaa0ibTi1XRtczENMArPEHZP5nkdPl57ZojOdhPzUTnI4qzkPp2AxKgiaPhqVuH4K5thKRVKXtNM091yB7R8ends4BmbqqhfN7Y0qsMnR1vw0fI9H6hZbnHcLUvFcEEnxh8rFonjqqD_gBGJSATM77lWYkQ2he9R9BKS1nQ2ieleijjGMjzeS5dv02_A3KEqNTbwm3RGc2G7QjJZPkpJ6jeauS4W2tRWgZY69Zkb3R6BMc9HNwmIdRSpwayYPIpONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=rzhMOpVscK0K1g_X8kLhybYWvZzLshKozQA0znl9bH7K0J4ZyGBuY7xW21zaB8mI69c3TE9HZnIbl2p95zwdBy0qWhLEi_S-8n-jzeyH12q9qpWjEjQy1leeF1J9Hq9mgGsQ6E2NfJaUeTtuw5tGMQH8c4baIK3lga5n06m0XEYH6MSIbEqqmuuYlAmQ3mZK535gLNYolX7L7O1tB7wWXEQM5uIqP9pHdLWtp5GD8YCh2aNSop3islk7lg-_iKhBLSywTSwPjZTWqjOIT-KLdq1nDmkAHQGfT884gLbBuSozV1_r3-JLurrbnTPDFYiGLfuHEUzMidUrSiiSGjArWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=rzhMOpVscK0K1g_X8kLhybYWvZzLshKozQA0znl9bH7K0J4ZyGBuY7xW21zaB8mI69c3TE9HZnIbl2p95zwdBy0qWhLEi_S-8n-jzeyH12q9qpWjEjQy1leeF1J9Hq9mgGsQ6E2NfJaUeTtuw5tGMQH8c4baIK3lga5n06m0XEYH6MSIbEqqmuuYlAmQ3mZK535gLNYolX7L7O1tB7wWXEQM5uIqP9pHdLWtp5GD8YCh2aNSop3islk7lg-_iKhBLSywTSwPjZTWqjOIT-KLdq1nDmkAHQGfT884gLbBuSozV1_r3-JLurrbnTPDFYiGLfuHEUzMidUrSiiSGjArWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=nThHHz42sGDoQ8K489s5yxTP_NfBYMkrcs7_iPsakniRVaqFYu8NU4YQtBFfrDauw0AnNzWstxsWBxC29mR1S4hmOBdoxnEKisZ4Tv8YGKn-Xki9aKdX8f47nNQvFLvrE1GDGhV7BXHiW9oZWGX98cZ-2ujCPCGL7gnk4k45q8iZs4_FTbiWuQBzvEBpkVxFfN4dBdD493kP72dIoQvT0tIEz29PX16v8jfPisJALtULb9j1F8g0ULSdsRzavh6r2vHvAa7orohgpWZdREoxwlCL3CLTTrSdFwt2mnTs3KpMfzLWriB2asAgO-to1voJc7c7tB0kq6uZ0PPSO6RN5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=nThHHz42sGDoQ8K489s5yxTP_NfBYMkrcs7_iPsakniRVaqFYu8NU4YQtBFfrDauw0AnNzWstxsWBxC29mR1S4hmOBdoxnEKisZ4Tv8YGKn-Xki9aKdX8f47nNQvFLvrE1GDGhV7BXHiW9oZWGX98cZ-2ujCPCGL7gnk4k45q8iZs4_FTbiWuQBzvEBpkVxFfN4dBdD493kP72dIoQvT0tIEz29PX16v8jfPisJALtULb9j1F8g0ULSdsRzavh6r2vHvAa7orohgpWZdREoxwlCL3CLTTrSdFwt2mnTs3KpMfzLWriB2asAgO-to1voJc7c7tB0kq6uZ0PPSO6RN5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUioEQhPcdoiL3FePRDSvuJ-tnXDz_3Vpe5uNGIAbUUA6h8wvz0bXDxjNUUq9CwJQV9aYnoGjDOPnGWmZysoYZWU8NldHJf_H_8RjN0eKSJI5g_iG6I3qIVovMZKjEjMNjP_ivgyQ3CEoNOqCFraoZlmd8hJ5kAH9xMjJDoApOB9frxgqfZkvYCUdvbrLj1aEyu6PL6TQsFoAmnydHsI7nCcSme3i43IlwxWfbV1Z1ckUiNkQutVyFa3qY6bemYxz-IrqipYiF_JS7e4-Caborc6s-Rf9diAubZl0DYXje6Xj4jbV3xyCB5AxWIAi2xNqzOwbfQSI_cd73CXaKeMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=d8moeuhjTQRNto6eSHy9QtEM1_kpXkNoZtGjSo_9A8mRJ_pxIMRjBeJnr0mvRS9awAh7gZSSSwd_EeyAIzIk8B3JuPBEDHfIH_D8YorUfJQ859djvT4zn8DuAdWdmlQD4YLzzHlVJF4-3fkNKisatCqP6Xe9-oKO346s-OKwR57HrGMVfZ0IMuSD3MGJZN0Z-OfehnGChsCd5Y_6NhAxudStxSgmgO-QCp-B2s2l6dGAOGSshbK5PJRWvXwSnbBIwNeRy8vymLK3iSlIUJsgoiDargtKMMRBVKjpS9DLnOVB9btbUYTYgGZEIIX4weXetaovtq1ul0540kcI9PcE8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=d8moeuhjTQRNto6eSHy9QtEM1_kpXkNoZtGjSo_9A8mRJ_pxIMRjBeJnr0mvRS9awAh7gZSSSwd_EeyAIzIk8B3JuPBEDHfIH_D8YorUfJQ859djvT4zn8DuAdWdmlQD4YLzzHlVJF4-3fkNKisatCqP6Xe9-oKO346s-OKwR57HrGMVfZ0IMuSD3MGJZN0Z-OfehnGChsCd5Y_6NhAxudStxSgmgO-QCp-B2s2l6dGAOGSshbK5PJRWvXwSnbBIwNeRy8vymLK3iSlIUJsgoiDargtKMMRBVKjpS9DLnOVB9btbUYTYgGZEIIX4weXetaovtq1ul0540kcI9PcE8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDdYR7lVFnks-7t-h8Fs9KuSOtOiPknIfJ-sl5thMy8SvxlOKX0EdPo-EOlqWTeWyf5T9XsMHUenb-N0hR6rzPge09UsrK49zmTmmZC844363or73KTfVLrnXvhRnc8UQOypssfn2hsvBjpSKlI7AInOYpzw8S_zKa7kwGKoVEHfq3nWyT8gwpWUOCp2lL71s-ZhEr_NdBX9kYBQqv53-jAdDVsSIOT7mYGHocSDaYkgPudWZUVMiTswMUCZjQcD-UarUWTExuSwb709gZgb8O8xW3d3vTtT0U2Qb5fqH2vJIBns2ZaOfX3yB5cVZh6IKP5KDcRrIMC20DuQCjMtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCrvcNRaWNOe5rZwoCMoAJZgjo7-Z0_IUfq9b2VPyUoEsvC29Ep7s7X1GClnAtEOXeKRQ4OFou9juLa5TTpnLyTclNMuEeuymhaQD9toUJmzoBwfpeY_wqrxRYd3XUpWumwUZhbALXj-tqrXNfMbZqIbjEjvFMnTIB1ScMwLPfPXq35WR4Lj8YIVEsIa_Ql6Fky2gMuqiPNFwDvMfoHEV9DCpJoXXZPkqDnXwMkOsFYXpote7P7lfcdARlbYbS271TjweXsXl4sUXzPs7i5k4jG3snNP2dJ6UzC6_7gMNl8DD2Sgx6q0k0o1rB5ze8daF3MSh3o7PMC7wRIEDxP0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8u5wILAgI85SuzKrqa-EehJSRpf_jcMd_3tEU21tCNcQE1yNsxzMJm7uxKyJe2p8WOaaNFLWAmFQ12sW_0YgvQOCWbH4iSCIED1_jsunziqJgxWR1qPLfm-1spf_q-SczHu2SseyBZOdxQ6Xn0hgNIyKFfPeqLGemCcy2HOaVxzwrf7T6I661tWZfXZjXhn5HUU7cAC1zjGFswqr7s6UjlJy6HUPvWtouzwpS6C2tEyRLQWAFPdcT-HuElqwmsLXYDnbXqVRu2MT_wHntG52LqqHYWuRafKNW_sIdpffYoAe8Arp0UGsJa9RAN8B0UdyGv6-cNb1U4MPai-SyF6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fO2KRa5ZRrl_SPQf2dKrRAAvDRk6_QMFUtIpFuEE0gpEbY9hAW_cq8EZ522bAYyPASesSjNyvRy5uAWZXOi4es-8rfSTV2a-INZhoG266WTayWZmIs2nLLKkTtqmHeagwTAsWIkEmWb1XpRVAHigKt2jgQ8so4dQ3lX699WVdPGj24VCXqpJ8mfPYkFBOQNZcyv1LFy5Yu25WpqOsXL5kTk91FbetvD0p5f_ETEl9RWgwWddulSehoVrdqOGf6Z2K7jSJUJzl5jxsRzlt0x3IMrsfm8Rx7HMJc9NCsHw6O-A6qyp6TmlIK_lskIbOGrIaBvTP-PCiaF1RMejM2ZM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4-bZtDMFQ9G1Lc6FLSRhOmP-Ur52MEgqnNZZ3sojwmnUss6WNX50AxkaYyhgDCsCLShKXw4oEzNXymXNtBIOaA-2Ji_exeCpCRKvdepuGx3f_iiGp8hUdlTUlmStwMQiD49u_6HXLUoT3P721BC5ZmFvedrT-nrdoHj5UetKcH9kFGF8knD7y3xlytSiz1nfUEg8AyCec4QOfJGnm3msi3ZlEJd1jV-z2cBgnyCUT0ETJMDnVidLpI8n4YOzcYJFJUmOuPwjTU45-M7y9rsZozO0t8BmvaikK3IkLTpPRlR-uzg5X1VoDRXcygSC3b2l4Te4LWGo9zIWgu7x1Wt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8lfXzx73vaMGU19N3796VJDTZO-WvoyKihhk7o8-Nc71rERKN36dEN6q7fqwFvyat2QXHm4llgUrnUZcSO7BLBzoeK3CaEkxSE64pQjWxH_CAa5a2682-rctGdFXxN_OWv1bWzLq1VLSw_zCvGAHQciRUTmDgRuJ_8Oh7Gd65uUH3EKVwOESw9eMfG-F4ObrT4Xi5EVbH3gEtsPk8QIUIeYXKd6kYS6qCEj4YjllO5Aa14BO5jis_ash23VGHZinAKDYgR5PvHQvcC5ZisQtSA_00n2y8OOwXPwSQh07LQFFQUJwRhA7qqz3Q_DQ8G8v0JHwAOd7-8CCifRw1LfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=PXMy8_ppwO50LjuzCwBQDF--sEfvVt3u7aE7_pIc9MducfvPp27R9JvusJ3EmG0prOsngCd1zg0h7G9GmVPUai0VwsOsWmAOtKbHQ6AwkM68xXo2vQqeSh2nNc54YgL9Rx-1r-Q4pLd7pL6qqGGIM-qs_UADKlCJzIVDYRabT4ePiDdZTccPmSivof8zB-xw4oQhgQC_vN53kLnjs89xB-t1cICDD6WhRtAyV2_jT3JZceWenrvDhZv6ocsZVynKzYvS0Cyt0sgGOc6sSoLFcgZTJsh6dewByBeabamkJAae6wr1wNPS06smZR8hUIZLIHJO9Hz-vMLwq1YT0NQXGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=PXMy8_ppwO50LjuzCwBQDF--sEfvVt3u7aE7_pIc9MducfvPp27R9JvusJ3EmG0prOsngCd1zg0h7G9GmVPUai0VwsOsWmAOtKbHQ6AwkM68xXo2vQqeSh2nNc54YgL9Rx-1r-Q4pLd7pL6qqGGIM-qs_UADKlCJzIVDYRabT4ePiDdZTccPmSivof8zB-xw4oQhgQC_vN53kLnjs89xB-t1cICDD6WhRtAyV2_jT3JZceWenrvDhZv6ocsZVynKzYvS0Cyt0sgGOc6sSoLFcgZTJsh6dewByBeabamkJAae6wr1wNPS06smZR8hUIZLIHJO9Hz-vMLwq1YT0NQXGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ3F480LDNFW0LU-HOYZHTPZYzhtfQRtQDyod9-aCHetIWjAaNDF2vm_tjALaFnnj_AJGOQSC3yfwS84KN2SJ0rxGDL53ycyM79mI99XXwAhEafKR86euzrs4F4vZ1uVuJkYwPubWZveZSnKx0tzRwLlH2G5ZcsRtBtZYvS5_D8jfhLKp-S-qY_HxycVWDZiNZxVGba1OT9st-AmWkPXl7j3v15A0UG7bb4iR_LUB3lgHC0Wb2_s_iKIfqpbNeRgFsciX2cEYfFzxpsimBWhU6A5344AuHywylWN3E2_mpdu6QIOJP7WsjNDYjbu7Ybq_evK8nJR6DiUvxoskoeeqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaCyowNT_ajjAH5zFhHK3dqmwkWKatuGVfTEAHINUUKIG4_rXCMsivR6ZWi9YJupjiBzZRBkeadh4HrmWQd5jxYxJI-9OKwL19aajntR4_CjNs1etzIsM3q-KsUxP_-GMwh-_nBC8QrxTE6BFUsNAGBBVbVoX37zdU0DrNlvDYIXUU62kI0zqrSF04BnuEXPMlsDIpAaIf8UmsghPA0FcSTwRyNbQa7sYXCNvf30ReADAM9i_8BvcBw-Z9D5PcOHcPfbuhKsWs29kvLtxDl0HGc5O4Olf15tnypaYt4XwJFeOLhgg0E7NTz_pYuHYM0lZdxqXETpJGLofaElO3wO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er6J78RaRI79piaZZRO8vg1E8SYsOXDb75U_I52Bb_0rUx4xY7rI-0YOlnsHIAaKHQV8GVXiDKE1tISgtQkc2z8jhgOBD2Hg45D0J6DA_40DTWT3_xP2ZiIIk7bGWqjl5PBFoNShr9MIZ9-MHYBEqGO5vIKPScuR6hcRFUPLmA6EwJF7WfYfHhFwRKUcQ-q17HjU4dkGKulXHQPlON2S0O7rdiJWEMNA_XWej5Zx0Js6bB05Tu8YladKhnyKPbYZbDRPfQNsh3qXXLmR99g3sd5DKrowvad-S4sNnlMULJHxhgbjxOOJzEjIr3VNWQ40SS4Kmyov9cN5n4BknhCICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmk8FzW53-qu2aXbgPeAxNCCgLUfR7mMtWgzFv0DfbHOruPge-xJtqu9sW6xy60dCZgAwWd0QvaCvu3A7h5DXAp7UuTXRzbJ5Ufhfct2U-PVLqA6KVwkBuxniqc323tfMjhYqksr83sok1z5_fGk1H1DmMvMylNeM-J0eL59VFG1hl2EyjH-BRjoW2uClc--BoxQjG3Oj21HO-LHif4BY-Kz1zPNifgn6Z3wzq2MkJ0g_aAnX8f5DC7_G1BOhl9OHlysBrJGQPYwsSJORFpARXGcnTWH1GFUCEAdh1fDZC6Z2uHJhP0EAz7QGnCKZRrnsPPBde0BuazhKRTXsGQAuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=ZGWo2ErV-Ix_QPl-KfvUQGkEnQ7sQRP1_ZdjLIGmw5oNvCZ9riJTe2SJ2mAqA3lImyL9ZSbBZlyrQyKJ_hgKt96r4sn7K3WletgbHjNArmjajxUon0H2b7KybwqBEIk992PNa0-apw4gh2Ww7SHDKWtJ2cuFelLN3AiVV0nVwlu5_IPN3w5edvvkMTarpPqEZSRIiFueHbBNivRmHq81XjIsYSfyLj0MPInYzqTO6SR4acCpOl3qGWLSbF-p6qB98qfzpTIeaksCOWp6chFaSlnkT6-mwT-egyMaTatgOOu1rehEzjmIILjFQpt8vpFQm9hDoKPaficH2PmtWs6f3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=ZGWo2ErV-Ix_QPl-KfvUQGkEnQ7sQRP1_ZdjLIGmw5oNvCZ9riJTe2SJ2mAqA3lImyL9ZSbBZlyrQyKJ_hgKt96r4sn7K3WletgbHjNArmjajxUon0H2b7KybwqBEIk992PNa0-apw4gh2Ww7SHDKWtJ2cuFelLN3AiVV0nVwlu5_IPN3w5edvvkMTarpPqEZSRIiFueHbBNivRmHq81XjIsYSfyLj0MPInYzqTO6SR4acCpOl3qGWLSbF-p6qB98qfzpTIeaksCOWp6chFaSlnkT6-mwT-egyMaTatgOOu1rehEzjmIILjFQpt8vpFQm9hDoKPaficH2PmtWs6f3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dyq3p7nl_-UlTNyf8L0eZsiodWSh3rswI6qWON6sqwOAD7x2wPEHMxaaD0TgWsmcHpa1DqOoeCGZ4zK4FA3rxbiZ4kI7SpGUjTcieDeDvY7pUd14gP3nRVO8eVZdAUoon4hcpVyMEN6uvmwPNxJkUtJ7Y-xJxxEMdG3_hza6axqS_-mIidkK8xANtZd63yCxrnvEFnYNqRYejW2vsE96bSP3t1YdM27OiDDCjIqvvP5WiN_KbBm9lBLFpjwLoGAiUJe-_yFbqQaKefdilQ3F8tMmzRo607CNWIYJk55-2XpnlsKi6o4UhtNqdayuG1ZYNlPIaXAOIJmPM55AQorfQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiO8l9bWhbwUVMOYs6dmB9ECwubZg0jMj09_isvuT-s1KI_VqBS6fpsMq1lzF3xGoW5aEqcn7-1m0TKvn7_X9i5NbSeJGI5EJw4xm0sqiU7vO6v2bB2p-ywEUgvrP8izNSpx1ElKf_04ucgfc60FrTvmTrwotXtlHldJpVfIlUCiPjO1zOZLHnYM8p90KaI2B51FyHzudIO7pUuFEDt1oSep4FlWWUjQTnXsf3VJ-mn7ir6ryAGMmfKP8kHFftG3ui9_VcTJOWvns4eBrbB39V-EBGo8MT4jy7Pv5s7AaVCWVLrQObtLgrTfZkE0v-29-LvFqMz6XF6c-_nBFdc-BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRz4JDtXqQ86FjflMkw3sJhARjKg3CcPyq3iZTbvhHGUpiFfH3XJIE-ID8tU2ScMWtlm8Nq3pB6a9bFxIQVLGaq1by8wi019XMCZMwEG-K3ue4gjy91VHo4oz4ShmhEjTno3mBrwgbaISWVLZrLklnVKUXOkXiCSaOpUsetBTB5Ez1YiY7KRhxcVJC_YXkOBb2AB4Ey109vh_BKVn-_NA50z-zDD-tVJoXI052WSWovFQ4DCuWeU9JJWxV-MofNwOMjTSl0mA-H7BQGvBH3z_JYFfGuZjH2Z_zUYBi3myZJ4qibIpH5d4jQutCL5qDVZGx0tV2JLEaqdDR_zIzF-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d985nXUSICQr06KJMCcu4WfoA3b5z1Qoawy5WSU6oV2CWzf87ta5JJVUvRT4yPDw27yTUTXrCpKbLUmDXSZIGJuSyY8DkdrCibwjQkOz1NoP7H00v7Wy3fRgaL7Ex155UyIuRUb3wfvJPI7luWT67UfOA2GDBa2Lcq7jm-BunAR-D6zlY9HqwoiIY8eA2tadbmg-tFCBsYcuEHBzGD5KQZ95T5F2W-5HxsF4EU5Rvz5R29c7jWyFQlQRpsEMH17tVhxLaazgYXod1TfVqJ0U-Mgx01Pb0fGWVrNMhe1bd52mJMV9HeyxnURLdEW_QHxyXPGWoy7iA3fImpskF26_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDKHgIok9lwvFVZGyWk4G-PWVp5PUMHuGnI8cM8IlRl1GKWCBbeQZCg0E4hlUfMDRXW-6hS3r2cVuCuwUt9RUCWM2BLlKh9YHXo2ZRlPDUm-h6AGkiqYQl8rbcZxX-yNeFO0u6B9S6oXMmX-ByugrSXTwZiCeZW7IpL1WrQmnRs-zkoRbM6J83JRa3Zf8K-YuR90nlOYey8nSbYhtER3_8eCfoWBIO2S7S5W199ei1gal4GjdkZpvcF-zyvKlz31E5hOfohiPJcygEQJdbn3WzytZQz8CRgd5XH-SqUcXzk-oJ0mtv7770TtLZlXbWE6VMfakTK8PBnZZzxRwW7wqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMj78CN1oYCVXMR4yRFKDlSDespPzkeYQ6Zr7Phgavwn6EkdZyqqpEAA6re5NnEwReY3pg58Bbris-aeEPdODmosscTKv3odQQMa8_FYsyZM9lonPE0a4i6JHhBuHf3BNCOm3Hcl75Rkh0UuF4gC0RyCpOvxh-BTeOhRlP8lpgohrOeg5VHBo2VTSdTIji-Alt1s_H3KzAnUMYJGWRKbAUjJ6vC11q4uz3wwQi_4l927HDbSA7ieC_0bGTGZWjEJFSweBxbNv9zcGxvtkJvXxqBWI0M8KCzl_z7V3K80YwGdKabyXHKlTN7eDmLlfkpPp9nZyQSQ969EJWjpf3UYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
