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
<img src="https://cdn4.telesco.pe/file/k1Ysu6uzzdxB7ceUNoYWSFRoy-4nQhNg0kuMT4bYML-AIFchJUsO68ub7WaOEiUO2Nyf0OIzjgDJisezcvvPVY0cdf_zUH6nJ2BYCu8KsY7_Ay4fjPY2NlUgeZmDXN52mk3V5TYBr8Q9Vt8tp3dVK8mDFOSODR3A_H2Jqo6o6UGdFIR3CeGGnzVKLL6UyFR-xIII1coKtie7I66cjPT7EAvIfDj7E1giZtyE0fkm7oYzPfQYs7lsQNh9fCr_81J5TaaMZ26PkEOQ4pipV19Usro1w7btI5x96CL0N3ysJrb4Ys768g5USbBaeB_70I1rE0zRFv7USR4RYlN158P_iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.2M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 20:56:09</div>
<hr>

<div class="tg-post" id="msg-680929">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb3b61d3e.mp4?token=A_5_wFRJSxizRN0f4Pzq50GueujyJM-6jHxU0VzF81I9NHvaljvdABzgPF6HTdSXo7EbmaRAzFQyEOS2vF-E_ifpViiUC3qOizU9a5Xx6n3fxhbyMqTUyFIYEwFQUrLYL4FNr0wI17h7bLH_3049R4v5ANrhRec9J1hYUOE2AMOHUZ0Gimztspe_-T_DoBAI6fhtRuxXuNMx9r8KJq3tlZp1XgchZZNY-GVAaZQcR-Vi0XoiCkfodqOiduCiLjAAD-eKuBBsksh_qARBB6u-WHsiOmITS5DQRbPqFpw1j3AIKyQe4-Ea59xbAfY59E2MBdw6D7aaX60ce2C__3qYKz-aTWtubCEtKk-97VqIpGXMljToapWKxarZaPj5Po4zJ2t11XlVS6gRI47X9wKidKhgojPI430UTMZ-tMdkDMQi62dUDssT8XDtsKldoQXJ0rptZsLv9V3iT7__Yane_1YvE2sIsWSRZSZIW0sXkZV0DJ8su-En0YCW2pQDhQFg2BHepGn_DXuM7yS_L7R_h831c9RYD7hXrYFpy7-foX0gALEEL_r0LVhzbvvC_Wo05xp5kD1FFfvfV8xb8XH0RcqefGHLBGBTwwnVUjmGtFyiycKa_95ISF3wnRck6X8tMSpdfSNCSqwjzlFqf8C84bkHmzriuC0zj58aJ-LQfFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb3b61d3e.mp4?token=A_5_wFRJSxizRN0f4Pzq50GueujyJM-6jHxU0VzF81I9NHvaljvdABzgPF6HTdSXo7EbmaRAzFQyEOS2vF-E_ifpViiUC3qOizU9a5Xx6n3fxhbyMqTUyFIYEwFQUrLYL4FNr0wI17h7bLH_3049R4v5ANrhRec9J1hYUOE2AMOHUZ0Gimztspe_-T_DoBAI6fhtRuxXuNMx9r8KJq3tlZp1XgchZZNY-GVAaZQcR-Vi0XoiCkfodqOiduCiLjAAD-eKuBBsksh_qARBB6u-WHsiOmITS5DQRbPqFpw1j3AIKyQe4-Ea59xbAfY59E2MBdw6D7aaX60ce2C__3qYKz-aTWtubCEtKk-97VqIpGXMljToapWKxarZaPj5Po4zJ2t11XlVS6gRI47X9wKidKhgojPI430UTMZ-tMdkDMQi62dUDssT8XDtsKldoQXJ0rptZsLv9V3iT7__Yane_1YvE2sIsWSRZSZIW0sXkZV0DJ8su-En0YCW2pQDhQFg2BHepGn_DXuM7yS_L7R_h831c9RYD7hXrYFpy7-foX0gALEEL_r0LVhzbvvC_Wo05xp5kD1FFfvfV8xb8XH0RcqefGHLBGBTwwnVUjmGtFyiycKa_95ISF3wnRck6X8tMSpdfSNCSqwjzlFqf8C84bkHmzriuC0zj58aJ-LQfFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی منتشرنشده از دیدارهای صمیمانۀ خانواده‌های شهدا با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/680929" target="_blank">📅 20:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680928">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
اوباش صهیونیست قرآن را پاره و به آن اهانت‌ کردند
🔹
شهرک‌نشینان صهیونیست عصر امروز حین حمله و تخریب یکی از خانه‌ها در منطقه «بیر قوزا»، در شهرک «بیتا»، واقع در جنوب نابلس، قرآن کریم را پاره کردند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/akhbarefori/680928" target="_blank">📅 20:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PxEdaFlPCDzHspoMSgCnhthnpH_F1_yLTu216gbmF3z8EDRV7OiQ1ElQDz16cMhRq2LS5tDaIRFUE9uVhHrfja5mtMCv7pIfZOKYRDP6QtPMSIH7_EES95mXNN1Ez4bKLLpN8jRFhMjXX0doRyJEwOBaPoOwKirUGhpHNOpAZkIqPJRsFPvGbWCwSSyEoEZj_KsEK0INxlQZj32KJcv-B38SXW56ROhSMXL_gZaTKz90hL2ZmmTSJasFaci5Hf1BcYubxnfCHNqKF5SXeG79agZD7KZ6JyLsibmdHGXo2waMXPBR6YyfjHSezpfFumDF8WukR9PghcNpiseO2rbCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6YUtMZNMJYnlQtm62XjYzRFaXcwfW0qxF25Id3bDBQ1Z2PY5OxbNfu5UoIF1nkrlYBC-clfn1RppLElQ_x7EGY2jx6-WzYKTC6rx0VRvbKg6FSX0WNMjDLJ0yEPq6EctcU5f5pSzsqZyHRjnacQjiOBUmmzpJ486zalMU4pMJwHvSt9qNWJFm-fBMO1WRmhtTXdwc4cc1JDNa-62cvnQm0NHZI0Z0qCEd-1e6YGKfHty1P9DbyceXbI_ghuTlR_rylUDQ8_lsACzCo_v64mqdN7j7xo4ZXlDHGDysQmnw_3mdlYQQZx7cu6BFIwnRhH5mBc778Wsb5LBIpPVS6XAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه به مناسبت سالروز تصویب معاهدات چهارگانه ژنو ۱۹۴۹ درباره حقوق جنگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/680926" target="_blank">📅 20:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded454043a.mp4?token=ALkOm8IpPq79JoFHvYVHrdr3SdchdHU5h_xnxXESb9U4D3XgXerGGx6mWGRhOVE076coGr_hcQyaouMZ2xPThxv1pKopwSAFcqUJe4g_q0OfX-9vGRn3nbXoAoPL8b01M_uY4jjtL0wNGRqeTZm4LWriWVFeg4gq1fWI2VEl6ux5YUgn4EbdIz3za74pKZGqKYK7mHenmEN1NE_TUvnr0P0s2on0PxQecMR2rE0Nas73E9qoFXqOHHaNzUOu8GmOmCPL2HIZFu9LyjwNbuoGGCuNC1OrT7vE7yyPmuDrFtTtWXHdzilRruSzZzEZTiMeTAVTOR0uXIOre5nDDCba-2EF2xR7YVkCb2EqBtysVpycr16di-1r_7S-mcp6x2uJivMv6vDPcL2R7YjQ1FEQQEL8nXM4d2BMKfavlUvK2ToT183CCyGTmxF6T0CGQjrHNKBLC2_wgkUyCULL-CJKnRN_YcVNH_8gGXq8tXKXiQNxdaPxy92bvizg11Zs9QOtuTcZYWg9lJF_7ZsJWZ-YXRP3qofR8MLBYXjJ9Q589WGsS8Fgo03451qtqGKJtZh08NNbj7cXc3L_3uACs6mGJVIfJFCLBTQEJO2WAZdwunoMp0yGHS8CDaIrr0_SwDBpS2--9c8brfjqaqsgoePUp3YhzJUMjXmVkQmcIemh8ak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded454043a.mp4?token=ALkOm8IpPq79JoFHvYVHrdr3SdchdHU5h_xnxXESb9U4D3XgXerGGx6mWGRhOVE076coGr_hcQyaouMZ2xPThxv1pKopwSAFcqUJe4g_q0OfX-9vGRn3nbXoAoPL8b01M_uY4jjtL0wNGRqeTZm4LWriWVFeg4gq1fWI2VEl6ux5YUgn4EbdIz3za74pKZGqKYK7mHenmEN1NE_TUvnr0P0s2on0PxQecMR2rE0Nas73E9qoFXqOHHaNzUOu8GmOmCPL2HIZFu9LyjwNbuoGGCuNC1OrT7vE7yyPmuDrFtTtWXHdzilRruSzZzEZTiMeTAVTOR0uXIOre5nDDCba-2EF2xR7YVkCb2EqBtysVpycr16di-1r_7S-mcp6x2uJivMv6vDPcL2R7YjQ1FEQQEL8nXM4d2BMKfavlUvK2ToT183CCyGTmxF6T0CGQjrHNKBLC2_wgkUyCULL-CJKnRN_YcVNH_8gGXq8tXKXiQNxdaPxy92bvizg11Zs9QOtuTcZYWg9lJF_7ZsJWZ-YXRP3qofR8MLBYXjJ9Q589WGsS8Fgo03451qtqGKJtZh08NNbj7cXc3L_3uACs6mGJVIfJFCLBTQEJO2WAZdwunoMp0yGHS8CDaIrr0_SwDBpS2--9c8brfjqaqsgoePUp3YhzJUMjXmVkQmcIemh8ak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار وحشیانه پلیس آمریکا با دختر ۱۸ ساله‌ای که به دلیل تخلف رانندگی دستگیر شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/680925" target="_blank">📅 20:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgxqR4vgd-cxQMU6vZBkmQyAK1M7A5dBN9k2xx_Kpp7znwAXJgu613JN_mRR6_OM4iYpkOv08F7EaN9vJ2Nfh_uHFCiotPLU0bWVzhFMh_kZDHxOglUHXQCIKiHZewQp8H_SpgwtrJP45g8LHl4DymVQsedyWDZ_deugcqYbJmgLLI0Wab4xo5KnLvD2QZ32BzqvQcsFzbFFcCbC9koIXvgAtGQxYOwCRnvV6CrQjDHxTtboml125gYHxMKTI49M_4-Mfz2CiVj_L1_ndivlGdKumBNduzLoB-982MnI6ZHXIwJndUOp4dpMknT7MNLyqFLVnMKiQCyR4UuQOI4lDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش CNN از وضعیت بحرانی سربازان ارتش آمریکا در ناو آبراهام لینکلن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/680924" target="_blank">📅 20:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlvoIjX5M89bzqulgqx6FmYE5UssUDGga1fmtn83758YDVfyJHUsPwRLf0xr8rGlx3mToyI1CVzRUzWEneS-rlj8CmAkqsejhfxE-tzAsQAhyf0xKXaWhL4Uvgf_tMvR1P4sLzMFrX6nsJNkx452-D6DyS5AudUzHqVidAzoDITZ_9EWlM6krXGr5WMkHcf2BJUHaxTVEt3sf6W3r0_f6XBovqIdbxFplxfyhNqrOVlyRKPKGUlit-FhTiOuwgcKhpLF1KSikC3EoxxQ-tkIIg85rxx9dNGHv9eQ2Ev6ZicUUUh97SO_MXIMKP3emr519L3SpM8EyU1ZaUIFMusNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وحدت و انسجام، مسیر عزت و استقلال ملت ایران است
آیت‌الله مروی در مراسم خطبه‌خوانی شهادت امام رضا(ع):
🔹
وحدت، اتحاد و اعتماد به دست‌اندرکاران کشور، مسیر عزت، عظمت، شکوه و استقلال ملت ایران است.
🔹
ایجاد یأس، بدبینی و شبهه در ذهن مردم، جز خدمت به دشمن هیچ اثری ندارد؛ همان‌گونه که بزک کردن و بی‌خطر نشان دادن دشمن نیز مردود است.
🔹
ملت ایران در برابر سختی‌ها و جنایات دشمن نه‌تنها متزلزل نشدند، بلکه عزم و استقامتش بیشتر شد.
🔹
زائر امام رضا(ع) باید با افزایش معرفت و تبعیت از آموزه‌های حضرت، زیارت را به فرصتی برای اصلاح و تطبیق زندگی خود با سیره امام تبدیل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/680923" target="_blank">📅 20:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
حملات توپخانه‌ای عربستان به شمال یمن
🔹
خبرگزاری رسمی یمن (سبأ) گزارش داد در این حملات، روستاهای واقع در منطقه مرزی «غمر» در غرب استان «صعده» هدف قرار گرفته است، هنوز خبری از تلفات یا خسارات احتمالی منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/akhbarefori/680922" target="_blank">📅 20:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
چشم‌پوشی نماینده فرانسه بر محاصره ظالمانه یمن و هیاهو برای امنیت کشتی‌های غربی
نماینده فرانسه در نشست شورای امنیت سازمان ملل با موضوع یمن:
🔹
ایران با حمایت در این بحران و نادیده گرفتن تعهدات خود در چارچوب تحریم تسلیحاتی تعیین‌شده در قطعنامه ۲۲۱۶، به تداوم این وضعیت کمک می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/680921" target="_blank">📅 20:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680917">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2cb0d8e4.mp4?token=FIWdnu9GaIG_omq1gajsRSysDkrN1tD6cUEmoq0tKRe5kk7nCLG4CSxSnH-78hlBCZblONzwrCwAFZb-W2gBgsz0FIaAU0_1W3rXyWrvPFyIVCYxQDHWJk-bwT9RBf1q47QUE-1g6d-Jy0KDAhJbVJLb_llIHQ3p8u-IgCJ9EDAU8SJZd84QFCFvxKiRhz_kCWSDxBdGnJUd03_rkoYU5-kMX4-zMYyXpkbJGwNORN8KnsxQ55lLxYE8nffdraTdPpaqHEDQ7wJ3-9wH84r-Ro6EXD3Y52hFVZOdnAV8kPoiaf7RNLmeiY1PTx-n0rFUBBaJnD9mFfhcwA7NAhaCuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2cb0d8e4.mp4?token=FIWdnu9GaIG_omq1gajsRSysDkrN1tD6cUEmoq0tKRe5kk7nCLG4CSxSnH-78hlBCZblONzwrCwAFZb-W2gBgsz0FIaAU0_1W3rXyWrvPFyIVCYxQDHWJk-bwT9RBf1q47QUE-1g6d-Jy0KDAhJbVJLb_llIHQ3p8u-IgCJ9EDAU8SJZd84QFCFvxKiRhz_kCWSDxBdGnJUd03_rkoYU5-kMX4-zMYyXpkbJGwNORN8KnsxQ55lLxYE8nffdraTdPpaqHEDQ7wJ3-9wH84r-Ro6EXD3Y52hFVZOdnAV8kPoiaf7RNLmeiY1PTx-n0rFUBBaJnD9mFfhcwA7NAhaCuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
🥀
شب جمعه است هوایت نکنم میمیرم..
کلیپ های شب جمعه شب زیارتی امام حسین (ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/680917" target="_blank">📅 20:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680916">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
شهادت ماندگار است
🔹
رهبر شهید انقلاب درباره شهادت اینگونه بیان می کنند که خاصیّت شهادت، خاصیّت فداکاری در راه خدا این است که به طور طبیعی ماندنی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/680916" target="_blank">📅 20:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680915">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
احضار فرماندهان نظامی به پارلمان عراق در ارتباط با حملات به مقرهای حشدشعبی
🔹
کمیسیون تحقیق وابسته به پارلمان عراق شماری از فرماندهان و مسئولان امنیتی و نظامی را برای بررسی علت تخلیه نشدن مقرهای حشد شعبی پیش از حمله به این مقرها، احضار کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680915" target="_blank">📅 20:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680914">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjkERJFNtYS8fif_9uY_SMYN4d4iCDmy8eV73wuIXBl0S4MJA66T5YWSzALUQRwOOGDAshMk_W_b2NhvRumO4yX03cDYdk5I4EQCss-MW1onWRj8VCWgqs9Wz1wLdQ6RygSdzq9ycR5U2TMjxQYQGgcQIos1GmLxFWzyKhCe936SRC-HO8eMjTX97uvGoLQtSnErGK0zsJfw0mXjo5iYHlJ9Y5eRiWd4lK7SKTJuiXR3CYMEP0_Jiore0t4nUveQFHaEE3k7G5vOFqxGrs9j-TvrOTWakRBF8I8Jbl8Dtm2MvLskAhuevNNb89vPYMXjfrIKuEDa7zyxuaWbvAOjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌲
کلینیک دندان پزشکی سرو
🌲
👀
اگه فقط ۲ دقیقه وقت بذاری، شاید نظرت درباره کامپوزیت کاملاً عوض بشه!
🦷
✨
🦷
اینجا جاییه که سال‌هاست لبخندهای زیبا و موندگار ساخته می‌شن…
⁉️
چرا سرو انتخاب هزاران زیباجوست؟
🌟
تخصص و تجربه حرفه‌ای تیم سرو با سال‌ها تجربه و تجهیزات مدرن، بهترین نتایج در لمینت، کامپوزیت و ایمپلنت را ارائه می‌دهد
✔️
🌍
کلینیک سرو به عنوان بزرگ‌ترین مرکز تخصصی کامپوزیت و لمینت و ایمپلنت در خاورمیانه با بیش از  10شعبه فعال در ایران
🤩
🦷
✅
اقساط بلندمدت بدون سود و ضامن
✅
۱۰سال گارانتی بدون قید و شرط
✨
✅
سال پالیش رایگان
✨
💎
اگر به فکر کامپوزیت دندونتون هستید  و به هر دلیلی هنوز شرایطش رو نداشتید ،همین الان میتونید از شرایط ویژه (اقساط بلندمدت)
🌲
سرو
🌲
استفاده بکنید
💯
✅
📞
مشاوره و تعیین وقت:09337830160
📞
ارتباط با ادمین:
@mahya_sarvcip
پیج اینستگرام:sarvcip
برای دیدن نمونه کارهای بیشتروارد
👇🏻
شوید
✨
https://t.me/sarvcip_cllinic</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680914" target="_blank">📅 20:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680913">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680913" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680908">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ایران: بیانیه حقوق بشری فرانسه و شرکای غربی، فرافکنی منافقانه است
🔹
سرپرست اداره کل حقوق بشر وزارت امور خارجه اقدام فرانسه و تعدادی از کشورهای غربی در صدور بیانیه مشترک علیه جمهوری اسلامی ایران به بهانه حقوق بشر را محکوم کرد و آن را مصداق واضح فرافکنی منافقانه دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/680908" target="_blank">📅 19:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680907">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1c3df4c24.mp4?token=BjxoczEG2pApkk7ru9rmqxJjVX76wKvdat5o7ISI5FdkMOrKaO1zOrol7gZljbV77gsQooQ8ne9awMRz5rjQzTEaNbJzcJ-kXZgPg2b9YB-zGAymmUjdkqQDDdPL3jMoy_HKMl8WaNU6PPrxXD_86UZlb4tbK2D8BWsEshWQtZzTMVYJRRlKkY_E2oCDSWp6zssTsZ55kl5ZSx0K1VBe8Agdnmm3-5xBbE1nrZjKY1ItKIAFBe_R84AQCqA8IMrVevD1SSDw-J6EEFPNxzgyOFPUtlTAuwq-k8kMKxGDE4QsMTD23BN3c-wf5-rmSdR0Uyq5oE2K2PJ9yZXquIkAtxVnsQ0nuvnAzan-G_5UdTLnnXW6vYz5AZrmir0xTQ6vk9EbwUZ0Xsw1E0jxkjLxyndA_PbS3CK6YqlR5ZRzSuo8DRcCikdejfoPs8dtCdvXAggmzQen9g3Of1M5bJXBHM-xOM_peVWdsgwtw1TonY67F796iliWrMzXMxPtDcWWWlBULkfBD12g03LnbWI_SEiXDd6Qs0TjZJWRqWHYzSy0m8Ja5KhlA8vV2NZTuNXULApruYKtiw1yK9-wSsN3mjv7qUW4Jeih5ykONpgzcjDS0l1E7EHrzo14VT43N_qyXoyvCY9aIc2g0DzJ1LIjaP1Ft67BnpAP0NGWt5b5fLo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1c3df4c24.mp4?token=BjxoczEG2pApkk7ru9rmqxJjVX76wKvdat5o7ISI5FdkMOrKaO1zOrol7gZljbV77gsQooQ8ne9awMRz5rjQzTEaNbJzcJ-kXZgPg2b9YB-zGAymmUjdkqQDDdPL3jMoy_HKMl8WaNU6PPrxXD_86UZlb4tbK2D8BWsEshWQtZzTMVYJRRlKkY_E2oCDSWp6zssTsZ55kl5ZSx0K1VBe8Agdnmm3-5xBbE1nrZjKY1ItKIAFBe_R84AQCqA8IMrVevD1SSDw-J6EEFPNxzgyOFPUtlTAuwq-k8kMKxGDE4QsMTD23BN3c-wf5-rmSdR0Uyq5oE2K2PJ9yZXquIkAtxVnsQ0nuvnAzan-G_5UdTLnnXW6vYz5AZrmir0xTQ6vk9EbwUZ0Xsw1E0jxkjLxyndA_PbS3CK6YqlR5ZRzSuo8DRcCikdejfoPs8dtCdvXAggmzQen9g3Of1M5bJXBHM-xOM_peVWdsgwtw1TonY67F796iliWrMzXMxPtDcWWWlBULkfBD12g03LnbWI_SEiXDd6Qs0TjZJWRqWHYzSy0m8Ja5KhlA8vV2NZTuNXULApruYKtiw1yK9-wSsN3mjv7qUW4Jeih5ykONpgzcjDS0l1E7EHrzo14VT43N_qyXoyvCY9aIc2g0DzJ1LIjaP1Ft67BnpAP0NGWt5b5fLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد ایران برای کریدور مالی مستقل بریکس
🔹
رئیس‌ کل بانک مرکزی جمهوری اسلامی ایران در دومین روز نشست‌های مالی بریکس در هند بر ضرورت ایجاد کریدور مالی اختصاصی بریکس و اتصال شبکه‌های پرداخت ملی کشورهای عضو تأکید کرد.
🔹
وی گفت توسعه همکاری‌های مالی بریکس باید از گفت‌وگوهای کلی فراتر رفته و به ایجاد زیرساخت‌های عملیاتی، امن و پایدار برای پرداخت‌ها و تسویه‌های فرامرزی منجر شود.
🔹
به گفته عبدالناصر همتی، رئیس‌کل بانک مرکزی، اتصال شبکه‌های پرداخت و گسترش استفاده از ارزهای ملی، ضمن کاهش وابستگی به مسیرهای مالی خارج از بریکس، به افزایش سرعت، کاهش هزینه‌ها و ارتقای امنیت مبادلات تجاری اعضا کمک می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/680907" target="_blank">📅 19:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-text">امیدواریم با غروب خورشید ماه صفر، هرآنچه قلب نازنینتان را می‌آزارد غروب کند و شادی ربیع بر شما طلوع کند و هرگز پایانی بر آن نباشد
🌸
🌸
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/680905" target="_blank">📅 19:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680904">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ4jlzq1Ps-VSLpYsU2ZQlU7XBaDCQ2FvIErJTcZhluFWj3p7w17UHcnBBxRuoz1Re3xz3uT5GLjti5_qbiK4RpMFE6WZQfMy1LiKARrSH2HkZsx_GOz05K15dPr8W8VmN7myuRwiy_i6ps2TvpDaawpOMjRKBXVL1uHPfG8xxBDqecDFdHgL0kgd0u7Csq3ecbjNg8SRqdZ56HMHVSYu1kZT73kBZwtq3W6t3fqHrENKf1pUQbplKc-UEqles3L4MG4acf2iuDpXzCPGP2ZKaOavkTGHOy-QZHWtxrZNPRF6lqWQJoG9h7sBFLesW8pAZCGij4tesRBuuNxadJjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اجازه مادر سادات رخت عزای پسرش را
نه از جان بلکه از تن در می‌آوریم و می‌گوییم
ای حسین داغ تو تا ابد در سینه ما خواهد ماند...
🔹
حلولِ ماهِ ربیع الاول ماهِ شادی و شادمانیِ اهل بيت(ع) را تبریک عرض می‌نماییم
🌸
🌸
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/680904" target="_blank">📅 19:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680903">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fj-lHJ_Hz2ADq44wSLH4LYoULScrToAOIIu9SRPiF2_KUnXiC9sMDS63Al3WHnCyQP3LyekOXRi0gkRBCODSGJOd-t_ClCzPmrw8F1js2a99gB_eSDCPq2Cu80brATTRyHbHzU5eZcT58BfEe2WQ17ylQeZLW1ek4hxNfHWN2ahFX3rzh4HsIH9vuQFhtA7PAkEQLFMnT0wXuO19rux6-Adxq4elSRlusFbHSZ6wJ8f1WRCFNL90Q6ABz-Ng3ypved949NSyjEQ9tLtWL-j6s3xMRZ9kxbcNKGXGAvnTHS4HsnezkvwYejVtJTXtCm6MmoXg5aY3k8H2fFG7KRPndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام پس از یک دهه لوگوتایپ خود را تغییر داد
🔹
به گفته «آدام موسری»، مدیر اینستاگرام، این تغییر با هدف مدرن‌تر و ساده‌تر شدن هویت بصری برند و درعین‌حال حفظ ارتباط آن با طراحی اولیه انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/680903" target="_blank">📅 19:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680902">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
پولیتیکو: جنگ ایران می‌تواند ضربه‌ای بزرگ به اعتبار آمریکا باشد
پولیتیکو:
🔹
پیامدهای جنگ ایران می‌تواند بسیار فراتر از خاورمیانه باشد، به‌ویژه اگر تنگه هرمز درگیر بحران شود، اقتصاد جهانی با شوکی جدی روبه‌رو خواهد شد.
🔹
در شرایطی که نفوذ جهانی آمریکا کاهش یافته و چین در حال قدرت‌گرفتن است، تردیدهای مداوم دولت ترامپ درباره ایران می‌تواند به اعتبار واشنگتن آسیب بیشتری بزند.
🔹
تیم ترامپ در محاسبات خود درباره ایران دچار یک خطای اساسی شده؛ آنها تصور کرده‌اند فشار بیشتر می‌تواند به فروپاشی حکومت ایران منجر شود، اما آن حکومت فرو نخواهد پاشید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/680902" target="_blank">📅 19:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680901">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966d0062d6.mp4?token=B-89VCfQvOOp3V5IAFBM-nW9rWo3QWUc6FQ_2tegRjdRve0uqV3KyzLcvinNP84LrgXeVt4qms5otCBEHuls1tHGSVI_YS-zaYMxgJlEMzyC1p4ioMULdInSlfvcc06QhtoRfXThoUF48EqJfl4ceRVk2shOwPTP3qd32M_sA-u2n6ztmTMrMa4TIyr4FjecvBd63it4wMUtl0r8PHJyp7C08LvlVDa7IaAYgLYXlJ4Z8WyULsdxBEwv7DgV7ej48duZXxTMfBp4vjzae36KS3tvVydZoySU-ubN5C3kLuVHj39-aXmr5kvXo497twR57qcXvZxZ2TT2u9sr7ru86Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966d0062d6.mp4?token=B-89VCfQvOOp3V5IAFBM-nW9rWo3QWUc6FQ_2tegRjdRve0uqV3KyzLcvinNP84LrgXeVt4qms5otCBEHuls1tHGSVI_YS-zaYMxgJlEMzyC1p4ioMULdInSlfvcc06QhtoRfXThoUF48EqJfl4ceRVk2shOwPTP3qd32M_sA-u2n6ztmTMrMa4TIyr4FjecvBd63it4wMUtl0r8PHJyp7C08LvlVDa7IaAYgLYXlJ4Z8WyULsdxBEwv7DgV7ej48duZXxTMfBp4vjzae36KS3tvVydZoySU-ubN5C3kLuVHj39-aXmr5kvXo497twR57qcXvZxZ2TT2u9sr7ru86Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنها پادشاه ایران که اجازه نداد به او بگویند قبله‌ عالم یا سلطان!
ادامه‌ی ویدیو
👇
https://youtu.be/IPmkJyaMkF4?si=f58hxCuT9iH8RCT2
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/680901" target="_blank">📅 19:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680900">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سناریو دولت برای بنزین چیست؛ با قیمت نجومی مواجه خواهیم شد؟
🔹
یک اقتصاددان می‌گوید: با توجه به شرایطی که بعد از جنگ ۴۰ روزه ایجاد شده، بنابر اعلام دولت، تغییر در میزان سهمیه و حتی قیمت بنزین امری اجتناب‌ناپذیر است.
مشروح گفتگوی خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3237426</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/680900" target="_blank">📅 19:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680899">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
‏
یونیوز: تهران دمشق را به هدف‌گیری ۱۰۰ نقطه استراتژیک در صورت مداخله در لبنان تهدید کرد
رسانه لبنانی:
🔹
تهران با آگاه‌سازی پایتخت‌های منطقه‌ای (آنکارا، بغداد، دوحه و ریاض) اعلام کرد در صورت انجام هرگونه ماجراجویی نظامی سوریه در لبنان، یک رویارویی منطقه‌ای گسترده در جغرافیای سوریه شکل خواهد گرفت و پاسخ موشکی ایران شامل هدف قرار دادن بیش از ۱٠٠ هدف استراتژیک از جمله کاخ ریاست جمهوری سوریه خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/680899" target="_blank">📅 19:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680898">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
اوضاع در ناو آبراهام لینکلن قاراشمیش شد!
🔹
همزمان با حملات هوایی جنگنده‌ها به ایران از ناو هواپیمابر یو اس اس آبراهام لینکلن که اکنون در خاورمیانه فعالیت می‌کند، خانواده‌های نظامی به MS NOW گزارش می‌دهند که ۵۰۰۰ خدمه این ناو از کمبود آذوقه رنج می‌برند.
🔹
این…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/680898" target="_blank">📅 19:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680897">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c0f75f54.mp4?token=V0TSC4n5VYGfxpHkYZTKAk_CO-_IH4fhqxH_qkPn9CQgsKqmRsRPRBF1pgnZyDInA4viww8Vo6XPPyQ2bBniDE21hMCTn-L9J6tTSxfn-XBr2Iv423wFRmymOnjpqQPe70yrcsrEtYBU_Dnt8aub5Ql-gdSBudt1cOX3zNlxEjvnnjTshMVi-vPy_PmKciFwxcrbc3lD39j1c9Oi9YlR9UdnM-nCrRFvAPrc7SXlg2R9LNy7j9OkEKfJAalU_P-YGEXbg_S6DS7Bd8UNtkruGdW3MHQN-_m_Y4ea-wwszcTrk8OTTQQTEazQd3RcCcuqVumBlqkitEjgJ-hs5v3elw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c0f75f54.mp4?token=V0TSC4n5VYGfxpHkYZTKAk_CO-_IH4fhqxH_qkPn9CQgsKqmRsRPRBF1pgnZyDInA4viww8Vo6XPPyQ2bBniDE21hMCTn-L9J6tTSxfn-XBr2Iv423wFRmymOnjpqQPe70yrcsrEtYBU_Dnt8aub5Ql-gdSBudt1cOX3zNlxEjvnnjTshMVi-vPy_PmKciFwxcrbc3lD39j1c9Oi9YlR9UdnM-nCrRFvAPrc7SXlg2R9LNy7j9OkEKfJAalU_P-YGEXbg_S6DS7Bd8UNtkruGdW3MHQN-_m_Y4ea-wwszcTrk8OTTQQTEazQd3RcCcuqVumBlqkitEjgJ-hs5v3elw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلکسیونی از خاطرات و نوستالژی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/680897" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680896">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اطلاعاتی ناامیدکننده از بارورسازی ابرها در ایران
احد وظیفه، رئیس مرکز ملی اقلیم و مدیریت بحران خشکسالی سازمان هوش‌شناسی، در
#گفت‌وگو
با خبرفوری:
🔹
بارورسازی ابرها یک فناوری قدیمی با دو دیدگاه متضاد است.
🔹
شرکت‌های پیمانکار مدعی تأثیر ۱۰ تا ۲۰ درصدی هستند، اما جامعه علمی و آکادمیک این نتایج را مردود می‌داند.
🔹
بررسی‌های دقیق در آمریکا تأثیر واقعی را تنها حدود ۲ درصد نشان داده که از نظر اقتصادی به‌صرفه نیست.
🔹
اسرائیل نیز پس از دهه‌ها آزمایش، این پروژه‌ها را تعطیل کرد و به سراغ شیرین‌سازی آب رفت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/680896" target="_blank">📅 19:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680895">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
رسانه یمنی: پالایشگاه آرامکو در جیزان هدف حمله پهپادی ارتش یمن قرار گرفت
🔹
خبرگزاری سبأ یمن گزارش داد نیروهای مسلح یمن در تازه‌ترین عملیات نظامی خود، تأسیسات استراتژیک نفتی عربستان سعودی در منطقه جیزان را هدف قرار دادند
🔹
ارتش یمن با استفاده از دو فروند پهپاد، پالایشگاه شرکت آرامکو در منطقه جیزان را هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/680895" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680894">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd281a894.mp4?token=cN3cR1ul7w0HG_ZGi7vQsutgil1m8or-Z9pyjuranRot6QbZ1okOWJAmUCsmNoXwlrTphZfUiUM-x1y_CW_BJ0y5tZ-FMqfTq9XZipmudrMX8liPBMrYiT04d6tWogEysvok0aJq7jAZjW9-YKqUxDFtUj5Z4kccWLrOu0xMlgHUFtAtqQP3TBUwHbkPVmKdU92dbR9AaLy5w9LqgcDy2Qv4KCjc5ngLmhWrqtDJuZyuaeIgA0zwG6ioqsRH-XWVFAK5PPQ6CxdbIRF7kz4sUcjSlXLeyei2iIdqtkJaVFPwN_oHnv2YJbkH8t-RS9IMieEskvzLq92ol7wkEjb01A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd281a894.mp4?token=cN3cR1ul7w0HG_ZGi7vQsutgil1m8or-Z9pyjuranRot6QbZ1okOWJAmUCsmNoXwlrTphZfUiUM-x1y_CW_BJ0y5tZ-FMqfTq9XZipmudrMX8liPBMrYiT04d6tWogEysvok0aJq7jAZjW9-YKqUxDFtUj5Z4kccWLrOu0xMlgHUFtAtqQP3TBUwHbkPVmKdU92dbR9AaLy5w9LqgcDy2Qv4KCjc5ngLmhWrqtDJuZyuaeIgA0zwG6ioqsRH-XWVFAK5PPQ6CxdbIRF7kz4sUcjSlXLeyei2iIdqtkJaVFPwN_oHnv2YJbkH8t-RS9IMieEskvzLq92ol7wkEjb01A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب گسترده خانه‌ها و زیرساخت‌های مسکونی در جنوب لبنان ادامه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/680894" target="_blank">📅 18:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680893">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFqKPGjSK7_pRViJIG7r17ETSUQxQHX0FxtMkIwKcN9GgX1btja_AMh_W10mnxrCpfSQmcyAHY2Pf0y1Rip1cPDfsQQ9149L6u-YXJ1KKS2MOP67p7nSk2wmsnQ-53J2y6AP7M93zXcVM2bUrgDNgfRbcJBRi7BDIl5dh4gXmTGALPVB6hHHg2VNdfaQcZugnJnzDVj7Q2ANXC27w7YjsObl1aB_yAXXrwXvlwUDfujeqvOg1jYs-EA1g6Ze4XYQQh3cICMw2keNkrJyW6yF_HghM1V5V5-ZV8OaDyR491TumJaCCkaxf2eyQXJ4IzLUEOc1MHAW8AJIlAIx2KR-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد شرکت‌ها و محصولات نانوفناوری در ایران
🔹
بیشترین تعداد شرکت‌های فعال در حوزه فناوری نانو به بخش‌های عمران و ساختمان با ۶۸ شرکت  و سپس نساجی و پوشاک با ۴۱ شرکت تعلق دارد.
🔹
از طرفی دیگر، حوزه‌هایی مانند «انرژی‌های تجدیدپذیر» و «ورزش و سرگرمی» با وجود پتانسیل بالا، همچنان در ابتدای مسیر توسعه شرکت‌ها و محصولات نانویی قرار دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/680893" target="_blank">📅 18:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680891">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOsf4tmatH6q1egD_S9i61kGEXXRDIv7pvd834Hg-yFdMV-bYswQthuDieZ8tXfCGPXEMFkOI6HyHCA5puPjrlFzV6kBTvygLNoBGwVwKOsNzs8nPjngdnO987NsyulL2rGkz7u4DbyOqWaUjKcIe3MEzMf4pshTXQC_rU4AVH-mg90jwNuye5J97fSz7uNL417gxjPyfCl86W1fgTZroc0G7HMX3znU6VkopQvc5Lc091PIHKX2GRx6F9bbQ2WLSDjNIAYrXPWPDEQkNgYBM4yZh2MPSkbx5JFf3pCdpcN7CAxOO8C2PSepQAU5ZJ9uZYHD6gqiu1YpN291xtfO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41fc106a5.mp4?token=DRIyPbPDMoWsPHxnqgOV37t0HEIISoowCLw1DTUxzIvgMP-5_ADM9gIK1CjPvqqqdZ_pZQv9Y-bIwhw8aSMaLFGofrtKR2RSh-6DYxUbRszM8PE2KJ48jxz1hFmf6l5MOHDWrq_uHj5e43xKjpz016VKdqCSqg0xCuGW0cbQPzvxE0IJfp4nYgS0pNScZoh_o4PFECmFo4Mc3Cp6E46M40B6geplIDLR6nM5AsqgqXvcGUigU0TrxeNqz4JNIgahw9IRLKkVxluxy6qyWAnO7m_cuW-ZLM0dmHzf-H2NeJOS0L9iULPYQ9AEzcz0ZvoMfN_Eg83CKlSE2VavBEeukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41fc106a5.mp4?token=DRIyPbPDMoWsPHxnqgOV37t0HEIISoowCLw1DTUxzIvgMP-5_ADM9gIK1CjPvqqqdZ_pZQv9Y-bIwhw8aSMaLFGofrtKR2RSh-6DYxUbRszM8PE2KJ48jxz1hFmf6l5MOHDWrq_uHj5e43xKjpz016VKdqCSqg0xCuGW0cbQPzvxE0IJfp4nYgS0pNScZoh_o4PFECmFo4Mc3Cp6E46M40B6geplIDLR6nM5AsqgqXvcGUigU0TrxeNqz4JNIgahw9IRLKkVxluxy6qyWAnO7m_cuW-ZLM0dmHzf-H2NeJOS0L9iULPYQ9AEzcz0ZvoMfN_Eg83CKlSE2VavBEeukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خورشید گرفتگی زیبای دیروز در اروپا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/680891" target="_blank">📅 18:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680889">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYP0yJiHChMonrxdLQkZB4uCyqpSD4Jq-8ssGh7C_CkC_RdwrUBXq-J38CzLeI8JmOzH487asgOVwSN4OBVThnzGHhtIteZArg5_G4a13LeJ6vTBsUcewQWA1bPO_LHLzqT4ECDnBFbm1gGCMoIRkxUpH8VnMtaU_QBMl0qTQ389acmsVhcrTNpKjuoYwThRHwNiQljbtUkUvQqWoI9zcTWIlxN9LTtPmhyBZJCCawaA1KTb1iTpJPX_J3AdZ7kt89OaSu2vIdaeXpZbQ9KHd9MJPIu3-ez0QaotV9UYKh5wVKRYg0-Y9uwDrvQIbVr060y1SX2fbbnHnWZ0osdk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوضاع در ناو آبراهام لینکلن قاراشمیش شد!
🔹
همزمان با حملات هوایی جنگنده‌ها به ایران از ناو هواپیمابر یو اس اس آبراهام لینکلن که اکنون در خاورمیانه فعالیت می‌کند، خانواده‌های نظامی به MS NOW گزارش می‌دهند که ۵۰۰۰ خدمه این ناو از کمبود آذوقه رنج می‌برند.
🔹
این کمبودها در حالی رخ می‌دهد که یو اس اس لینکلن رکورد دریایی بیشترین روزهای مداوم در دریا را به نام خود ثبت کرده است.
🔹
طبق گزارش‌ها، اعضای سرویس در شیفت‌های ۱۲ تا ۱۶ ساعته، گاهی بدون هیچ روز مرخصی، کار می‌کنند و استقرار آنها برای دومین بار تمدید شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/680889" target="_blank">📅 18:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680888">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
رئیس سازمان حفاظت محیط‌زیست: آلودگی نفتی در سواحل جنوبی قشم و جزیره هنگام، بخشی از پیامدهای آشکار تجاوزات نظامی است که بر زیست‌بوم ساحلی و دریایی کشور ما تحمیل شده است  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/680888" target="_blank">📅 18:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680887">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXFYGAAFKk3aT8aMXcEJ3zM1PeWw-e7ax4dzsARw_ScVIAfclecSJawhCshEnEwaE52DEjGpmHCJ829hfT_3bSxE6cGUYbwGMJ93c3GG9mJktpfvzcZ52pjmfArLlXAGo2FX_wcOrIyj3NyGgN9TUSW2G4eW9VcktOQkcDGFePsSyCm92JT-NZSkVeJN3H-f9M7-1ZTthpsxKguvB5gspuFiD_RMFP0N1ZHYt2i-yYucphnCeWT7LZbCoLSoxf1eraKbvZ-K5UlcvtkNNn4A50_uvHvS3HGs6I1gbya7MNoyk2gYOcOnjKYETsk0H_FY12KaJYp832DJQb1VEPd89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس پلیس غزه ترور شد
🔹
رئیس پلیس استان غزه بر اثر حمله هوایی رژیم صهیونیستی به خودروی او به شهادت رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/680887" target="_blank">📅 18:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680886">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
تست سرعت‌گیر از خودروهای میلیاردی
🔹
با کمک هوش مصنوعی وضعیت خودروهای میلیاردی در مواجه با سرعت گیرهای غیرمعمول رو سنجیدن، که نتیجه خیلی جالبه!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/680886" target="_blank">📅 18:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680883">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
انفجار مهیب در کارخانه اسلحه سازی در رم
🔹
منابع محلی از وقوع یک انفجار سهمگین در یک کارخانه تولید مهمات و تجهیزات نظامی در نزدیکی پایتخت ایتالیا خبر دادند که موجب بروز وضعیت اضطراری در منطقه شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/680883" target="_blank">📅 17:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680882">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPrewRRh6j6U95uoT6OdSG7M-4w9BUTZ4ZbWsRml232dgmRsVzBJUEU2MsvAhDqtiYiKdpKZ_ZSHJzb3xrs3ZPSz-0emjtFDeYm_p41OmV5dDS-zoIZPYjvpTHwkKiy2my3JLXWj3Stuscb-Rm8SpdjildqZOokOgpmIZhxq1EFFv_mj7Oi--PHmAvvHBDUbYjiSUoeBp4D5quGi_Y29dU30HgH38jXzE-iDdGB6dvencRrlzOalKIvY8zMfGBsKNM4YGSuAdqbr_q7ZmvT88NGUblDexH3XTofKDD645u__XKl0UCoIHZ6EsNNXwFEP8DWbMPY-2N53IUI7QvCP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: راهبردِ تهاجمی‌شدن جنگ در صورت تحقق نیافتن شرایط ایران، بدون شک معادلات قدرت را در جهان دگرگون می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/680882" target="_blank">📅 17:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680881">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آ
یا ایران دریای خزر را به روسیه فروخته؟!
🔹
می‌گویند ایران خزر را فروخته و سهمش شده ۱۳ درصد! اما یک سؤال ساده همه‌چیز را به هم می‌ریزد: سند این ۱۳ درصد کجاست؟
چرا این عدد در کنوانسیون آکتائو وجود ندارد؟
🔹
اگر «فروش خزر» واقعیت ندارد، پس پشت این جنجال بزرگ چه چیزی پنهان شده؟
ماجرا را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/680881" target="_blank">📅 17:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680879">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f344cb7a.mp4?token=GxRF8A5p9Ad2xHSFBipD5f5RqZx5XPOxyNXpdWJBecxKfPfPtajUa-VR4HO3T1SdSN1bzXRpbn7Q6fa88pEDvAL-6UoXTxHkjJGfVUVdVYWW_1gaMElW0S8NwI6pqCYPnKwzP2HLv5BfW36yNWujbx3Yth9vzj3rAMppMA58Me0zt4QjRKddDYD06KdtY8wru0yONyv2GUB4Ez7ZpQEMP8sRcmSry8HtJZgp6vp3HYA0PQ4fSEQHFrEEG_ABr3fa_M7sNhq1mPnp1-qIPUrRsTyWHY-L8XBaDjSEDqPvqeNmwEm5xZ3E1whvBFIsXtOpDV8GApw3OjJDj1pj-vkWRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f344cb7a.mp4?token=GxRF8A5p9Ad2xHSFBipD5f5RqZx5XPOxyNXpdWJBecxKfPfPtajUa-VR4HO3T1SdSN1bzXRpbn7Q6fa88pEDvAL-6UoXTxHkjJGfVUVdVYWW_1gaMElW0S8NwI6pqCYPnKwzP2HLv5BfW36yNWujbx3Yth9vzj3rAMppMA58Me0zt4QjRKddDYD06KdtY8wru0yONyv2GUB4Ez7ZpQEMP8sRcmSry8HtJZgp6vp3HYA0PQ4fSEQHFrEEG_ABr3fa_M7sNhq1mPnp1-qIPUrRsTyWHY-L8XBaDjSEDqPvqeNmwEm5xZ3E1whvBFIsXtOpDV8GApw3OjJDj1pj-vkWRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در کشتی‌سازی چین
🔹
در پی آتش‌سوزی یک کشتی در کارخانه کشتی‌سازی شهر فوان در استان فوجیان چین، انفجار شدیدی رخ داد که تاکنون دست‌کم ۱۰ زخمی بر جای گذاشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/680879" target="_blank">📅 17:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680878">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCKm4tzWMbLwkS9UuJC3Re4LagbVfwpxa9M_TxKL75wW5gyjex2U3UeqOcKixDEgHpLQtFm6-zciQ-KcV8Tzksf8IuW3SZoybXLOmCWCXBKY3wJWwqB1ojwMoNWr1sSEYVimKbe2I7pkOXwkNfI6S1O3GCQvIeXI37bWN7oSr4jpn0QQJJwJUQZEPW9o1_uXsDfwPOFNoqydf0pMrC0S37js8Q-c6NDbJiAjfaYMe3L79rkvb4tBjDMfzJGtH5QvbAb_BiQYtTblXl0oRpSAUD433WcC9Y6FvgqS5SK2xOBZPTZOWTRznGeKjIex8FObXH0Aj9nb7Yjw-CZE6vaa9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طعمه کردن خبرنگاران در ماجرای فرار ترامپ از طریق کامیون آشغال غذا
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/680878" target="_blank">📅 17:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680876">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3517e5ff46.mp4?token=cMVBIvUrtVw6Jdrgb0OZiBy1SWZzLCysb_PLnudbu6RPz3roRNLvw-q4WUCdoPRFg_oo5O3DBFgmdp-HVL5OwbQzoxO24jFJK04pwsX4CbUsSVROr2MWxAd6x9pBNZUM3sQMM-j0laGwEtdLZP1uWwMXfjiUsEuhMXAPrx8lkyuC40Q-Bgj4BVDuNG_WvOmjMYRqKTQB2CFqfybDcMOzdk0h0rH0FdJAcSiAHgbUzty7gzneZxbPq51nJkOFasdItO0X3dztc-Mr9Lcf9I145PDsvItOuBhgVnvReSHhVGGIdwdivOPRFAo-rKmx0W3kN_hDvgsknfCFe9kWH_lXWCch23yXXX60N6hbdSQS0I9ynApEr7TWJ7pIx8CaTvydtlF6Dp6SXGUVOLdmx9c3sWLeg6h2OZqBh_DY80ctCglC0UpZ1Nq73cQ3uaY9lKxz84E_xT4RAGRDnkoqJxYyWdk61aV6hFHo_OejRmtFVWWHZIDYSMQe-6SKVDQud1qYyWdAkfd1e5AOA5FIe-fvFg5pqF6dedcFEZZ13E-lXu3adgQ-OFWqXUjxtLGr0CvcJbtZwfgbHlW0af92kdKb28nr2p7LOR2hf9FhDPHSzvo8_xY-hOAWi6PFIyvxxAud-6yl6XsKvSTsye6P9orsA9mAJ9_1I3BYUwtp6DWU_0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3517e5ff46.mp4?token=cMVBIvUrtVw6Jdrgb0OZiBy1SWZzLCysb_PLnudbu6RPz3roRNLvw-q4WUCdoPRFg_oo5O3DBFgmdp-HVL5OwbQzoxO24jFJK04pwsX4CbUsSVROr2MWxAd6x9pBNZUM3sQMM-j0laGwEtdLZP1uWwMXfjiUsEuhMXAPrx8lkyuC40Q-Bgj4BVDuNG_WvOmjMYRqKTQB2CFqfybDcMOzdk0h0rH0FdJAcSiAHgbUzty7gzneZxbPq51nJkOFasdItO0X3dztc-Mr9Lcf9I145PDsvItOuBhgVnvReSHhVGGIdwdivOPRFAo-rKmx0W3kN_hDvgsknfCFe9kWH_lXWCch23yXXX60N6hbdSQS0I9ynApEr7TWJ7pIx8CaTvydtlF6Dp6SXGUVOLdmx9c3sWLeg6h2OZqBh_DY80ctCglC0UpZ1Nq73cQ3uaY9lKxz84E_xT4RAGRDnkoqJxYyWdk61aV6hFHo_OejRmtFVWWHZIDYSMQe-6SKVDQud1qYyWdAkfd1e5AOA5FIe-fvFg5pqF6dedcFEZZ13E-lXu3adgQ-OFWqXUjxtLGr0CvcJbtZwfgbHlW0af92kdKb28nr2p7LOR2hf9FhDPHSzvo8_xY-hOAWi6PFIyvxxAud-6yl6XsKvSTsye6P9orsA9mAJ9_1I3BYUwtp6DWU_0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میمونی که بعد از دعوا با دوستش ساعت‌ها در فکر فرو رفت!
🔹
«کیوماسا» نام این میمون است که در باغ‌وحشی در ژاپن زندگی می‌کند.
🔹
پس از مشاجره با دوستش، ساعت‌ها گوشه‌ای نشست و در حالی که به نقطه‌ای خیره شده بود، به نظر می‌رسید عمیقاً در فکر فرو رفته است.
🐒
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/680876" target="_blank">📅 17:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680875">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYEZQbY4CFdQiPdy0BThyv0eIESI8oUjfiLavPoGM9vuCEccGLsNLkVssiUDjC6t9WeplSJ33nhViAWFY8Uk2UFh6pzRI5SFaDJOl8arGcicRikFJmKrQIknlenbMMe53lRtWZtgrGdQ7WqIaDE_RuT-ni93QlJZezICn-R7XS18zoTq3EhfzUuyT2D9sgTabQGYjidgMFJZNEV8Ehg8jbiORE9IHT79xCD3uOyEW3naRkI9kCZ_1V3UdJLyA4o9uM9uPRPChrnQtUSJxLcgX8D14jy1uXflqZDPds8MjZ_uttbCmIKxU-VrqJGdwoj1SY9ORCIr3HX43q_Rv-ma1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهرام رادان به «سیاوش» پیوست
🔹
همزمان با مراحل نهایی تولید کنسرت‌نمایش «سیاوش»، بهرام رادان به جمع بازیگران این اثر به کارگردانی حسین پارسایی و تهیه‌کنندگی سید محمود شبیری و جلیل کیا پیوست.
🔹
«سیاوش» با الهام از حماسه ماندگار شاهنامه فردوسی به صحنه می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/680875" target="_blank">📅 17:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680874">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
شیر اضافه مادران جمع‌آوری می‌شود؛ فعال شدن ۱۹ بانک شیر در کشور
رضا سعیدی، فوق‌تخصص نوزادان و مدیرکل جوانی جمعیت، سلامت خانواده و مدارس وزارت بهداشت، در
#گفت‌وگو
با خبرفوری:
🔹
در حال حاضر حدود ۱۹ بانک شیر در کشور فعال است و چند مرکز دیگر نیز در حال راه‌اندازی هستند.
🔹
بانک‌های شیر یکی از راهکارهای مؤثر برای کاهش مرگ‌ومیر و عوارض نوزادان نارس محسوب می‌شوند.
🔹
فعالیت بانک‌های شیر کاملا داوطلبانه و غیرتجاری است. این مراکز معمولا در بیمارستان‌هایی ایجاد می‌شوند که دارای بخش مراقبت‌های ویژه نوزادان هستند و شیر اهدایی پس از دریافت، بررسی سلامت، پاستوریزه شدن و نگهداری در شرایط استاندارد، در اختیار نوزادان نیازمند قرار می‌گیرد.
🔹
مادرانی که زایمان کرده‌اند و شیر اضافه دارند، به‌ویژه مادرانی که نوزادشان در بیمارستان بستری است و امکان تغذیه مستقیم ندارد، می‌توانند از اهداکنندگان شیر باشند.
🔹
مادران اهداکننده الزاما نیاز ندارند برای دوشیدن شیر به مرکز مراجعه کنند؛ آن‌ها می‌توانند در منزل با استفاده از بسته‌بندی‌های مخصوص شیر را آماده کرده و به بانک شیر تحویل دهند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/680874" target="_blank">📅 17:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680873">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
من جوجه کبابم مرا نکشید!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/680873" target="_blank">📅 17:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680872">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef213bb96.mp4?token=s2bWzcUV-VeUOw06196T0j4W0EHhH-a41GSu9p4bXCn2l-IwO06iiEgkiI8PWT3UjyjGbmnONomPi9wRvOfa4YYZOs6kczFh5GjOW7EBZ-2cMYUuOg3X9RmQvw1GiOFq8QZvxXKHD2wGvWtHMjV9uAoRWhw2jk-9_hEtB0jLCDf_C4J1asp-B9GPEDAZtHABdjrfktYVblehqiWFwPJX1CiZRsuC1izP2tdhw50ba86fAK42I1Qxawmz8wD6hA98gPmkhRuidy7Fcnp94D99ahKhDg9U7feoKQE4R5NEbq9trO3kVXcaeNSA5sm329cXzdzop16z_H2uRRYQTd8NoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef213bb96.mp4?token=s2bWzcUV-VeUOw06196T0j4W0EHhH-a41GSu9p4bXCn2l-IwO06iiEgkiI8PWT3UjyjGbmnONomPi9wRvOfa4YYZOs6kczFh5GjOW7EBZ-2cMYUuOg3X9RmQvw1GiOFq8QZvxXKHD2wGvWtHMjV9uAoRWhw2jk-9_hEtB0jLCDf_C4J1asp-B9GPEDAZtHABdjrfktYVblehqiWFwPJX1CiZRsuC1izP2tdhw50ba86fAK42I1Qxawmz8wD6hA98gPmkhRuidy7Fcnp94D99ahKhDg9U7feoKQE4R5NEbq9trO3kVXcaeNSA5sm329cXzdzop16z_H2uRRYQTd8NoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛑
مغازه‌دارا و فروشنده‌های پوشاک، مشتریات منتظرن...
✨
مدل‌های ترند و پرفروش
💰
قیمت عمده واقعی
🚛
ارسال سریع به سراسر کشور
📦
خرید مستقیم و بدون واسطه
اگه دنبال سود بیشتر و جنس پرفروش هستی،
همین الان وارد کانال شو و لیست مدل هارو ببین
👇
🔥
تولید و پخش نیکلین (منگو سابق)
https://t.me/nikleinn
https://t.me/nikleinn
https://t.me/nikleinn
https://t.me/nikleinn</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/680872" target="_blank">📅 17:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680871">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ff90e764.mp4?token=FXbhilTyq5MsqFy2jPn5rVMyGa0zCQSnBwvY49M9S7dm3Xp8u7WvhhRpw5I7PYKtkfVxcxGXFTMxUiUVvijv8Qgqv4DHHpjkFaOtzwCLDyvyiWta_oXvbsomLPzyZePGv1Wj3F78euCM5yPijz8_42etzRBUsNZtf4zNDWZEZBrkk8em7WQ5U2oocb6WNrw3EqaY9Zt_9X5krn2HfFWdgxIc4pagAnKDT4WVj3S-QHHg8P-lehUpkOkKBYwHmEJV0ISsZIOAQAID4osOzyNW41Rv_BM_mWlyH5Aj9w-BpD9pGfFngCA1JRR1uMsRvmaZv-fsfneVcQOy1wrOifD9cg1JEMVbiUj0DUmNFYB6cF61VNUtYTb4Id-IF70A1H4aATVMjOrG5MRtmb0P9J0xB14MS95pEAC9wQ7boJAi3YvUEQNmqtRjbFXfV19ArYBD57_uW9MDy8uCarFtJoR-TDGCb2DNDXbxqv8NY7Js6j49XqUoXdd_pfR_Za8vGd7mKrgOx9_wTyQVvEBYx8DoKUkc1m3IoZRR3fCIqcbyRRmt9qS5SH1wm34S0dYgN0E01ZSJwZRa67MyheQLyw5Z2B_8BBhS6DYSYzICOZ3-ISsgByfaSCx8ySgUDwH0fuNx0CD-dDobSdTVxFRJY4mWJJc7iUIZ6A5Xb6pk-Sqk5LM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ff90e764.mp4?token=FXbhilTyq5MsqFy2jPn5rVMyGa0zCQSnBwvY49M9S7dm3Xp8u7WvhhRpw5I7PYKtkfVxcxGXFTMxUiUVvijv8Qgqv4DHHpjkFaOtzwCLDyvyiWta_oXvbsomLPzyZePGv1Wj3F78euCM5yPijz8_42etzRBUsNZtf4zNDWZEZBrkk8em7WQ5U2oocb6WNrw3EqaY9Zt_9X5krn2HfFWdgxIc4pagAnKDT4WVj3S-QHHg8P-lehUpkOkKBYwHmEJV0ISsZIOAQAID4osOzyNW41Rv_BM_mWlyH5Aj9w-BpD9pGfFngCA1JRR1uMsRvmaZv-fsfneVcQOy1wrOifD9cg1JEMVbiUj0DUmNFYB6cF61VNUtYTb4Id-IF70A1H4aATVMjOrG5MRtmb0P9J0xB14MS95pEAC9wQ7boJAi3YvUEQNmqtRjbFXfV19ArYBD57_uW9MDy8uCarFtJoR-TDGCb2DNDXbxqv8NY7Js6j49XqUoXdd_pfR_Za8vGd7mKrgOx9_wTyQVvEBYx8DoKUkc1m3IoZRR3fCIqcbyRRmt9qS5SH1wm34S0dYgN0E01ZSJwZRa67MyheQLyw5Z2B_8BBhS6DYSYzICOZ3-ISsgByfaSCx8ySgUDwH0fuNx0CD-dDobSdTVxFRJY4mWJJc7iUIZ6A5Xb6pk-Sqk5LM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شله؛ غذای سنتی مشهدی‌ها برای پذیرایی از زائران امام رضا(ع)
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/680871" target="_blank">📅 16:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680869">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1ZYO37o07m5Visw80uuyUEtGGHXjZ2rjyUAuI9IWH4mZAGvNTn2-JvnJqEz9aA7IukZzOCiRMw6NuGmTbbnWAcftoNIGJpWvXMm4UhN1vNhuKjws6RJOj-RJ8qoz0NoKzqwvQPigtmdzOwD71l3gVbNj9CrlnSsFzTjxk4MptyfcYwZ3zwkjdSUIQyXY2A5lA7G15qZsoSYISWVtkbpkhbOtWeeiLXBudrBG_4uRGCHCLUtG94CPf0cVH-BpxqZVzjCv_TYoiuCY4fBtEhty-_iuG7GM9USfODC2nUX94q_WzCpUn5xNuCeLtcHj8pVsxVtphHyf16FJodN9WQbwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esqvzKrLRfCybh5k_GMMOud-fyNUMgSPxcE_kEeAlxBZE4ldmlzNxMr_lmockE463WWmqANWIQqZ7HZ_sjcQKzN2A1vPKtcD7-o005VHd3HwSKA_jDYw13SWaFPNwsLE6fxNl4agpRQsRCzcXzElxU7DeDx-RlW-Wb-6Jf7Af6VHoNQz5BQvrtgFIfqkBLOT-fcD2LS4792GDLhJKnA9FjOoH6K4dvgYRlufY4GZEEUlshSzNZEaMTOdahBaxdgFpHV0QwG-moVjl1ZH1jXpWHkAh5ctPQVxdi1hI68jEq7BPeK8kbX4NeoryIeuRlYnY2axo4DRMf_15xN2-KsLGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت عکاس نیویورک‌تایمز از پرواز فریب: ترامپ ما را طعمه کرد!
🔹
داگ میلز، عکاس روزنامه نیویورک‌تایمز که در جریان سفر دونالد ترامپ از ترکیه در هواپیمای ایر فورس وان حضور داشت، پس از افشای جابه‌جایی مخفیانه رئیس‌ دولت تروریستی آمریکا به یک هواپیمای دیگر، این…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/680869" target="_blank">📅 16:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680866">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fvz4hRlecKvGNQAHXpHqw3l99cVvaTZggm8a2B6VCZMBEAEhFrtJp_Hk8vBeMudESWN37xxYe8JHroGF3C14RwJCN6UaP5zdYez1cjZavdkgma3iTd1pJgGzO6b34rpEr2kO66RvmpHKA6h3293Psga2H6ExblEu7uUukcp8xXrMKhA5EfwO8Ng0Ah7CDEC83eG95_OXztvyYCQYpELEtzJjE5mIf6iJsN1dHY-GEUEvV0xWDNIRlkKcTJeO7E2p8p2fG-GTi_qqTRxbzCrRCTfhlqoItH6EDYGBc21Oc10q2dfH85rtFjBay0eDIilS7y2y-qDF7_ecQIy5H2sB3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXk9SzASTP4sr7EUZkmoVro_vwqQHtbOYVeBSnmSvwYaEgw-DMOmH3iDRIA3Z_zKi6mBE8cz30wWTt7MRZRDS4Hm6M_6Tf6QYIldlFVtl6JUP08y1jbujzh0tPB5Jv1A70kR8lCpUlU1yGph3IeG8C7_yQhu6IJjHMhOhTUI-es-RhtUQQRk460xxT4LHP4DpK_1mRyvdNGwH31Oj7NyMXDbA7tDP6QnqdES-7KEBgVY0m6PZqUku2p3HS33kRHSONLHNHmodR8kVGPM4xnoQWHHL4Kz4sSBPZ5udejWLugVUEmMJUJE3Vi0v-g-zVm5kICyt8E-BWTm8s4OqY0GDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCqyKEhFqjtLaARfKB_aByCKDQx8xuo6Q7wh8_rIvWTshg-qgSfHyE6xRsGyIn5fIryKgmmzXvMgUJskn77_jEyOCT67653FLCPCUcgzP6eL350vixm8w1h1NXzFm5-YwTIWhq4VKZzbqzWI7jgVFvg3ak1LBbqWvYxe-zLBDBJHYk47lCWvlo6X1pIhGlGCRNux_ruh_EVBqk3Qk7RgCCjj72M2UOa_TUfqDHBjFpsQO6020eTutAzdT_2JJ-uBPjXECgEr6lmdins6z-UVcP00xUsA-4YUbTPwPCmuVNV7W6keLxD5A2pmt5P7tbvsRbS55fnwQj_kBkzInRd-kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چند ساعت قبل از آخرین رانندگی جیمز دین
🔹
این تصویر، جیمز دین را کنار پورشه ۵۵۰ اسپایدر در یک پمپ‌بنزین در شرمن اوکس کالیفرنیا نشان می‌دهد؛ عکسی که ۳۰ سپتامبر ۱۹۵۵، ساعاتی قبل از تصادف مرگبار و پایان تراژیک زندگی این ستاره گرفته شده.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/680866" target="_blank">📅 16:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680865">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c802205578.mp4?token=QodrYrxnFFUQpLSUKWyJOIoIy7M6Gyf1V7LSSmv4RNJg2HqTnVW5yF_B1gA4cVVzBac3zkC18hm7l0fxu8ZrQ6RpZVNN1KKvYmlKl1VEi01FO2JVSy9QnTTH8UEYFON226vuyWM5QkLdgxzylu8_ej4LfvyZR5HWOoyChgKrayt-BxfnAIWqb-KaRfwdeAINZ3iaeRcbGJ9jUO7RZAgrRAi0C6a-cHR8Edq0nV88ooF01wB6vbZenEfJ6Ai0aWxBpDbRsNBiRgmHtxz1M_2znKAYmHFl3NaU_b3gw3_ALFMXKbUnC9BKuvEzCfllHG5LJCYmqQeBP_3ZiJQJAXNE6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c802205578.mp4?token=QodrYrxnFFUQpLSUKWyJOIoIy7M6Gyf1V7LSSmv4RNJg2HqTnVW5yF_B1gA4cVVzBac3zkC18hm7l0fxu8ZrQ6RpZVNN1KKvYmlKl1VEi01FO2JVSy9QnTTH8UEYFON226vuyWM5QkLdgxzylu8_ej4LfvyZR5HWOoyChgKrayt-BxfnAIWqb-KaRfwdeAINZ3iaeRcbGJ9jUO7RZAgrRAi0C6a-cHR8Edq0nV88ooF01wB6vbZenEfJ6Ai0aWxBpDbRsNBiRgmHtxz1M_2znKAYmHFl3NaU_b3gw3_ALFMXKbUnC9BKuvEzCfllHG5LJCYmqQeBP_3ZiJQJAXNE6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه بختیاری‌زاده به رامین رضائیان: برخی بیشتر از اینکه عاشق استقلال باشند، پول را دوست داشتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/680865" target="_blank">📅 16:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680864">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFmjzqOPUgMXGmDy5kTa-8v4V_p7gkevGLplzGM5uZ07ZiXtE3AFRKY7lD4xQv5vUyKDr0zMv5T3O3Txr1uMPmGmZJVFw596g9fHM1nFC6JUoCKqFjbqf9hPfoWETopVOE_5z_2Ro_c5WiwSU0XzcKMik74ZBv-hyqnGrTHc0ZPvJ5Ae1K1o7m38UZBcYwwLlYt5T7h-kreYgEodKvGteEDiZ-wR1zg3rKSIDaE-n7erk_DtFzrEeH-Fx6JejakLfXYwTc9pkUysvkBV-sZ1ToomtjCwm5c66V7sWs_1ODVd0UB9JT0q56HD6DF67nxxmfKCUlB0RIHj9mvHcH3UoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر حکم انتصاب رهبر شهید انقلاب به عنوان رئیس خدمه‌ی آستان قدس رضوی در سال ۱۳۵۸ توسط آیت‌الله واعظ طبسی تولیت وقت آستان قدس رضوی
🔹
بازنشر به مناسبت روز شهادت امام رضا(ع)
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/680864" target="_blank">📅 16:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680862">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Arj5eTrPP3HFnh0mM1h627WDjthMccDQaCVTtxNDKl0C616S0qdjGkSj-SYUeC0VF1GV4bdiltheJ1DYdfRelf2k_FVVnacGiETxQlkNjrbsGQL6n3KlWcQ6Fko3HZurGMuEPef5clZR00y8pRdfwQ-0O_2ZaruKqp_f9wEqJG-W16Hd8oswL3swSIIBm4RTEUuGLe7rZRZHMlXcgUqjSTMZECeK9Z8b08toe585WgczLUnXacgLai6dpZqVGJdXDBRRpoH9ou3AATfI7UjbB7jWiM-roSDgHFh6PP5l4B3F7gqDYR1dLJPsZrYQGy7ZzFGOXwDeAYdSmIjIzXRN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فورچون: دریافت عوارض در تنگه هرمز برای ایران ۲۵ میلیارد دلار درآمد دارد
ادعای فورچون:
🔹
درخواست سرسختانه ایران برای ایجاد سیستم عوارض در تنگه هرمز، سالانه تا ۲۵ میلیارد دلار درآمد ایجاد می‌کند.
🔹
بسته به قیمت دقیق نفت و حجم آن و کارمزد ۵ درصدی به ازای هر بشکه، سالانه چیزی بین ۱۸ تا ۲۵ میلیارد دلار برای ایران درآمد ایجاد می‌شود.
🔹
این موضوع باعث افزایش تورمی هزینه‌ها در سطح جهانی می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/680862" target="_blank">📅 16:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680861">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136871ba42.mp4?token=IeAguUWqnsNvqJZh8BPwAMvNVAwkLn9tt9yGhwKc-6OFY8EcJahrIUsSHAyK7w6G_gvw8NNZ2NsgJbDaTqDi568iSSNcCKZpwr4wYKsi604VdOYpPzNFzY5V14qrKcm-PNQIlphBqGLh0OHy3sPtFzD4Biw6p0gsq7_sfRQBauPC00syvD-TS0or_op3FqA0KW6RjPf2QT1B71wdtVAP8YaVG9UJXpCWjwrP9x5hhezaOfm7soYDsKLWd0ysLYxLHyeGic7Say-Ggtnlvpv66_Z-ymTfbd3oUnXw3zcx_cITxscfq3zSs_3oOmXLvqAlj_mxwVo2z9xoyeeQZR9TWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136871ba42.mp4?token=IeAguUWqnsNvqJZh8BPwAMvNVAwkLn9tt9yGhwKc-6OFY8EcJahrIUsSHAyK7w6G_gvw8NNZ2NsgJbDaTqDi568iSSNcCKZpwr4wYKsi604VdOYpPzNFzY5V14qrKcm-PNQIlphBqGLh0OHy3sPtFzD4Biw6p0gsq7_sfRQBauPC00syvD-TS0or_op3FqA0KW6RjPf2QT1B71wdtVAP8YaVG9UJXpCWjwrP9x5hhezaOfm7soYDsKLWd0ysLYxLHyeGic7Say-Ggtnlvpv66_Z-ymTfbd3oUnXw3zcx_cITxscfq3zSs_3oOmXLvqAlj_mxwVo2z9xoyeeQZR9TWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما را ببخش گریه ی سیری نکرده ایم
چشمانِ خشکِ ما خجل از این عزای تو
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/680861" target="_blank">📅 16:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680859">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
محیط زیست لرستان: ورود گردشگران به منطقه حفاظت‌شده اشترانکوه (دریاچه گهر) از تاریخ یکم شهریورماه ۱۴۰۵ تا اطلاع ثانوی ممنوع اعلام می‌شود
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/680859" target="_blank">📅 16:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680858">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ساحل شیب‌دراز قشم از آلودگی نفتی پاکسازی شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/680858" target="_blank">📅 16:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680857">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e9fda238.mp4?token=UDWEMbiCkko-gibnIyZV8QSLlqoRoDYf6b4HWI9eKG0efA5lxuJZ-_uWHzR__7NaKlMxJbg8mKmkdt6m_8jf3s9YFp4sKObGC7vWvErpqh3p4iyJToBqaVfac-y0D2vqa06uC6lCEqMec5qjxZ4ijBPH4MIasEewu6YUMo-TVzjSjwawC_x-rADO-oGchS3dsc8QMLtNplLnz7bsK36Bc4xr-wMhmpu7fIhq4lxP2H7U87k5K5b1ahCtBXWxJlZA4V-l-tHGFzdghF-CUhq5hhTWqPkUaRLO8mKC_RynZsB_22mv_ZXZUw1heh6cpYEyUpelyqgqAAOaZsKDWlDfiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e9fda238.mp4?token=UDWEMbiCkko-gibnIyZV8QSLlqoRoDYf6b4HWI9eKG0efA5lxuJZ-_uWHzR__7NaKlMxJbg8mKmkdt6m_8jf3s9YFp4sKObGC7vWvErpqh3p4iyJToBqaVfac-y0D2vqa06uC6lCEqMec5qjxZ4ijBPH4MIasEewu6YUMo-TVzjSjwawC_x-rADO-oGchS3dsc8QMLtNplLnz7bsK36Bc4xr-wMhmpu7fIhq4lxP2H7U87k5K5b1ahCtBXWxJlZA4V-l-tHGFzdghF-CUhq5hhTWqPkUaRLO8mKC_RynZsB_22mv_ZXZUw1heh6cpYEyUpelyqgqAAOaZsKDWlDfiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان وظیفهٔ فراجا: مهلت مشمولان فارغ‌التحصیل غیرغایب برای شرکت در آزمون سراسری تا پایان آبان تمدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/680857" target="_blank">📅 16:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680856">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
فصل بیست و ششم لیگ برتر و بررسی وضعیت چهار تیم مدعی/ استارت برای ماراتن ١٨ تیمی
🔹
لیگ بیست‌وششم با حضور چند مدعی جدی، می‌تواند یکی از فشرده‌ترین و غیرقابل‌پیش‌بینی‌ترین فصل‌های سال‌های اخیر باشد؛ جایی که فاصله بین مدعیان کم شده و کوچک‌ترین لغزش می‌تواند معادلات قهرمانی را تغییر دهد.
🔹
خبرفوری به بررسی وضعیت ۴ تیم مدعی این فصل پرداخته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/680856" target="_blank">📅 16:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680855">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwDoqtARWIQ_2Qpynk8s24r_57zLCNWzTA-JwyKB54Uq0GgeeAiKfv8OlBsOSCcKHQIfdtrG42yJK0RftOp4P7UIpYsQqvs2VvMo9cneguQseZBZ8mak_zvV3J6aS2Ae5IGQR5kDj4r34giA3nl7lPK6ifpI4xGt84lnAXBt1uUTLA38bk70YSEtD5xgyE_meJqq2KMgxRfAMg9TSl9k2UTQz5fxacGJmCGuZHOzb1jbGkZ7_U4O_B4ay7gia4UEkLqHi6_clA2ytTkAHVp_ukSLbUHJLjXQP5GxYkxRR_uSKUB3ZM4yvZ2QpmAzFk9qPmeCUVxsAjT1m2Pak7F8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای آمریکا درباره تهدیدی که ترامپ را در کامیون حمل اشغال غذا مخفی کرد  ادعای یک مقام ارشد آمریکایی بامداد پنجشنبه در مصاحبه با شبکه اِی‌بی‌سی نیوز:
🔹
نفوذ مخفیانه یک گروه ایرانی به ترکیه به همراه موشک‌های دوش‌پرتاب، رئیس جمهور آمریکا را مجبور به تغییر…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/680855" target="_blank">📅 16:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680854">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/276475a01a.mp4?token=fRtWPP0ZZg50ygR8ewJcPRPQeZmblKbO90-hZxsHKubCKoIsLnFBjUF0QNcOUwpwocZ09h3cz1UMvyDzPAlbxX7XLJSEPVIJRhMCGO4wt6hhd23JWzmo6GhAkELxhSVdZtQLr-DUSnkLpoRI49HWU1Ae-qkEe9u2NI8odfAYvKogR_MOd1vDXOQjR2ODTXOWqmWb6oiH4t4nd6QgYCASCrYCuc4dYADSXsOyKTrHhwGK_gRcP_QBeFCfDxnIbsDvzU__OpMjtVN8YjolVUP7VzggaHe1lomD5HYYNmJZTQFVoebqePg-obdvdcGS9aOJJKTb7ldiRnODmOVH5mkWoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/276475a01a.mp4?token=fRtWPP0ZZg50ygR8ewJcPRPQeZmblKbO90-hZxsHKubCKoIsLnFBjUF0QNcOUwpwocZ09h3cz1UMvyDzPAlbxX7XLJSEPVIJRhMCGO4wt6hhd23JWzmo6GhAkELxhSVdZtQLr-DUSnkLpoRI49HWU1Ae-qkEe9u2NI8odfAYvKogR_MOd1vDXOQjR2ODTXOWqmWb6oiH4t4nd6QgYCASCrYCuc4dYADSXsOyKTrHhwGK_gRcP_QBeFCfDxnIbsDvzU__OpMjtVN8YjolVUP7VzggaHe1lomD5HYYNmJZTQFVoebqePg-obdvdcGS9aOJJKTb7ldiRnODmOVH5mkWoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش‌های سیل‌آسا در ژاپن
🔹
بارش‌های شدید و رعدوبرق گسترده در منطقه توکیو و استان چیبا ژاپن، شرایط اضطراری ایجاد کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/680854" target="_blank">📅 16:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680853">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تحلیل الجزیره: ایران هدف خود را طولانی کردن جنگ قرار داده تا درد را برای ترامپ حادتر کند.
🔹
نروژ: جنگ علیه ایران نقض قوانین بین‌المللی است.
🔹
هیات امنیتی عراق برای بررسی مسایل امنیتی و موضوعات مشترک وارد ریاض، پایتخت عربستان شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/680853" target="_blank">📅 16:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680852">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY1ZieM27x3BOU2lgO1gUUW9xi1GvL_4zN73GGvguqx9UmUb61qKNFu3NdtPZj4-X7oE3a6FomlYakA_bazu-107hCeg_nqZK3nEWZkVeY6VcOy-ulugzCN1SMU7ZT6puVR4i7D3FmkU4LA28UFaNta7EanhkM293n1IKg89OuDn0giLrj51_gEYdGwvnkH1EoDil69onlWbDKewkic-arOmXPAKIJzxjcTQuDrG72M70C0wSXylhbB5BhrsCR7mEbMy6Zbymj9yY2D1dTaixr2QtVrC8HOmRDNixIK36acxONr1guw3l4ZtNbaoV2bjXv9ajPmumSOlHwq6Su93IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای توسل پسرم مجتبی به امام رضا(ع) برای آزادی من از زندان پهلوی
رهبر شهید انقلاب:
🔹
همسرم برایم نقل کرد که مادرش پسرم مجتبی را که کودکی بود سرشار از معصومیت و پاکی و سلامت روحی و عشق و عاطفه و پایبندی به برخی عبادات به حرم حضرت رضا (علیه‌السلام) می‌برده و به او می‌گفته: به وسیله‌ امام رضا به خدای متعال متوسل شو و از خدا بخواه که پدرت را از زندان آزاد کند.
🔹
کودک، معصومانه رو به امام رضا(علیه‌السلام) می‌کرده و به او توسل می‌جست. یک شب دیگر مجتبی با مادربزرگش به حرم رفته و صحنه تکرارشده؛ اما این بار نشانه‌های تأثری شدید در مجتبی ظاهر شده، گریه و زاری کرده و با لحنی که حاکی از لبریز شدن کاسه صبر کودک و سوز و گداز عمیق او بوده، با امام رضا صحبت می‌کرده و به شدت اشک می‌ریخته؛ به حدی که مادربزرگش از کرده خود پشیمان شده و تصمیم گرفته که دیگر این کار را از مجتبی نخواهد.
🔹
دو روز بعد، تلفن خانه به صدا در می‌آید تا صدای من را بشنوند؛ من آزاد شده بودم و از خانه برادرم در تهران با آن‌ها تماس گرفته بودم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/680852" target="_blank">📅 16:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680851">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مجلس برای حضور اتباع در ایران قانون جدید تدوین کرد
فداحسین مالکی، نائب رئیس دوم کمیسیون مهاجرت مجلس، در
#گفت‌وگو
با خبرفوری:
🔹
تدوین قانون جامع مهاجرت در دستور کار قرار گرفت.
🔹
در این رابطه کمیسیونی مشترک تشکیل شد که نهایتا کلیات آن در ماه‌های گذشته به تصویب رسید.
🔹
در حال حاضر، این قانون در اختیار معاونت قوانین مجلس است تا کارهای حقوقی و نگارشی نهایی آن انجام شود و سپس برای تأیید به شورای نگهبان فرستاده شود.
🔹
در این قانون، شرایط حضور موقت، دائم و اقامت به دقت تعریف شده است.
🔹
در قانون جدید برای پزشکان، متخصصان و کسانی که قصد سرمایه‌گذاری در ایران دارند، فرصت‌های ویژه‌ای دیده شده است.
🔹
جایگاه هر کدام متفاوت است و وزارت کار نیز بر اساس نیاز کشور برای نیروهای فنی و متخصص برنامه‌ریزی می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/680851" target="_blank">📅 16:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOXwWQ0_VtmixdeEBwwDKOoIPtJfzPpkfqOU5Ztu6lKopGEOZmwSue_i3t0gLj5yEfB6crkmYdg-7IpQZIPPbm2TsCSslcm0ELSzmHygxDSGNn1WIObfYb_bee5lN4z7T7qoY8VQfHaH4dNUHIKPu96cUNKwoe9MJNH44DDJkoraXVs355KPvgWAWMLrQAygtjsd70C3vT-QvQlACrbwQhkZ0Lald8gnNpyEDaptyMfeFvZKtjKvtp2O6NZhDcnytnhrIC9Poo6_5sqptzQwb5hIUnTIEVnFDL8OWSwj4a6yXIMQLjUVKS7bxiw2F57KWykm455yQOjAqr5IHqgcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مراسم عزاداری ایام پایانی ماه صفر
▪️
با
مرثیه سرایی: حاج باسم‌ کربلایی
⏰
پنجشنبه ۲۲ مرداد ماه - ساعت ۲۲
📍
حرم مطهر رضوی - رواق امام خمینی(ره)</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/680850" target="_blank">📅 16:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b68d8bf3c8.mp4?token=XOyIZXzajfy9C-wXDE-z448lfnZpgmOcUdHavon8E7CNK6ktYRP8UYmtYXkoG2X0RGneTPqVErBwnkCDV5tLF3zurQwDmWkypiehQ3bIBNokMVS32r1aqySUHaRQvKIGZMVy8VxB6DlYpMIdTu_n8nhvZMALB01jksacMQKOlJoPSCm5utEZIhzEeDnEmMTf-88MrL9ndIi1WShLp_J5AvekWEOoXUi9VHTZfAppvKMCIIMKWYeEwHVjpXfQdYT0c7GyZlTiN4UpkdI_9Pq-q5h_WwsT2ybTBfoRz3e7PIdm93WTXR-07_MP6zIwzQC1Z79fNU76vaFvi0NZvbjwQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b68d8bf3c8.mp4?token=XOyIZXzajfy9C-wXDE-z448lfnZpgmOcUdHavon8E7CNK6ktYRP8UYmtYXkoG2X0RGneTPqVErBwnkCDV5tLF3zurQwDmWkypiehQ3bIBNokMVS32r1aqySUHaRQvKIGZMVy8VxB6DlYpMIdTu_n8nhvZMALB01jksacMQKOlJoPSCm5utEZIhzEeDnEmMTf-88MrL9ndIi1WShLp_J5AvekWEOoXUi9VHTZfAppvKMCIIMKWYeEwHVjpXfQdYT0c7GyZlTiN4UpkdI_9Pq-q5h_WwsT2ybTBfoRz3e7PIdm93WTXR-07_MP6zIwzQC1Z79fNU76vaFvi0NZvbjwQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی قایق گردشگری در سواحل ترکیه
🔹
یک قایق گردشگری حامل ۱۱۵ مسافر و خدمه در سواحل فتحیه در استان موغلا ترکیه دچار آتش‌سوزی شد و با کمک نیروهای امدادی گردشگران نجات یافتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/680849" target="_blank">📅 15:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680848">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6566c5a5.mp4?token=MEGilkv_9uu_CtdgJYS38ZD7w1FiT5pFP3-E5Tvnxhzfo_UVynNZsHk-758LxLkYmfZPcJRNkIqVX2iRmp13Xt3BwrJL8UUKQgrcFzYzVQsurnLltR7Mh8je0pVgs0Z8i7E7wDdKdgKk9eLbAZEEUyaCiMfP7NLXqIMECMOaVYLRr6XnVXwbirBpuGbBarwL0imVcKXCkPaK4OJf7bQrVXoRiHS6e4KJyEp2-1Nu_QJehRCWTCJj-G_ooIMhUtP1CG7RuGoWX8m8eUAGqVQQp3rLlBC4usyOMr0ojvu-hmuEdF8vXArT1FOK7Ax6lfWtsKzgb1MEZifmOwHfvVK8og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6566c5a5.mp4?token=MEGilkv_9uu_CtdgJYS38ZD7w1FiT5pFP3-E5Tvnxhzfo_UVynNZsHk-758LxLkYmfZPcJRNkIqVX2iRmp13Xt3BwrJL8UUKQgrcFzYzVQsurnLltR7Mh8je0pVgs0Z8i7E7wDdKdgKk9eLbAZEEUyaCiMfP7NLXqIMECMOaVYLRr6XnVXwbirBpuGbBarwL0imVcKXCkPaK4OJf7bQrVXoRiHS6e4KJyEp2-1Nu_QJehRCWTCJj-G_ooIMhUtP1CG7RuGoWX8m8eUAGqVQQp3rLlBC4usyOMr0ojvu-hmuEdF8vXArT1FOK7Ax6lfWtsKzgb1MEZifmOwHfvVK8og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم قدیمی از تعویض ضریح مضجع شریف حضرت امام رضا علیه‌السلام با حضور رهبر شهید انقلاب در سال ۱۳۷۹
🔹
بازنشر به مناسبت روز شهادت امام رضا علیه‌السلام
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/680848" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0GHpUdGY08XJldWCF8qQhXT1AJ5uWSz0QKnq8sU5B8up3qGQ3tRzxZDs_AkRS2Joo1_HoBTQVVuA-qpMQT80OdWLlP-_oKHPK0Lz9h1gOX6hZ-HOv7MHw2DW2u0S1nObf9OA6PHSD4sfwrOeQ9tCMfrl4-QkrlKzH5b0VHS6dfNn4jPbPnG3e6Tz6pZhdyEbgPeMMYKH7Y2DLoPYPMgVDFuOtW9WB2CyI46SAzkR4qD2xM7Sxjqbkd5GqSFqJm1PidYOF9VFCfrvi-Y3-JuzPgUqf6EainmBslynynRMc8xiGgOElgE2Z5enthvxeZkYF33wxLc-etKbqA5kVc3Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دلنوشتهٔ خاص مهران غفوریان؛ خوشحالم زادهٔ خاکی هستم که امام رضا دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/680847" target="_blank">📅 15:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680846">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0n-Cf5dN3b85-XBud7miwdkT1_LvW9U7cC9-GU5CMA4qSlkz5DsbO_uvk2d6KaGauJg-gZBiHK6qdP8mJPQIU6RAH1veiPkMcKfjfdH_-rBkaVMZyZImyG7jxVHA98_mFXalNrftndQ5bJjllokg1DhSd7-h6_ukyjIS8DRtniJpcmOqAXjUYZtmeL_rKrz1KmQUKC85lo0MFXoReZJ_4sUb8gXxb9FDAWXkPP65oyhsMRP5nOVd3T608cF8MhBaSF2XSCl3GHfZa4jJ0JwBxZfJIvUpIUGRcZGZDV_qg5d1TUqUGMEnnek_VbtIesiEaKqJ9HfT8JOGr5O0Ws7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده یک تخریب سازمان‌یافته؛ چرا مافیای صنعت بیمه به سیم آخر زد؟
🔹
هشدار بی‌سابقه موسی رضایی، رئیس‌کل بیمه مرکزی، ریشه موج تازه تخریب‌ها را برملا کرد. او با بیان اینکه «با کسی تعارف ندارم و با شرکت‌های متخلف برخورد جدی می‌کنم»،
پرده از یک بدهی ۷۵ هزار میلیارد تومانی برداشت که تنها در دست تعداد اندکی کارگزار و‌نماینده خاص بلوکه شده
و ۱۴ شرکت بیمه را ناتراز کرده که تبعات آن دامن هموطنان را گرفته است و برای دریافت خسارت باید ماه ها در انتظار باشند.
🔹
رضایی با این قاطعیت، رسماً وارد «میدان مینی» شد که سال‌ها کسی جرات ورود به آن را نداشت.
🔹
علت شب‌نامه‌ها و سوژه‌های فیک چیست؟ دقیقاً از همان شبِ خط‌ونشان برای سودجویان، حملات کلید خورد. سودجویانی که منافع چندصد میلیاردی‌شان به خطر افتاده، چون جرات مواجهه علنی ندارند، پشت بیانیه‌های بی‌امضا، سوژه‌های ساختگی و اکانت‌های اجاره‌ای پنهان شده‌اند.
🔗
مشروح گزارش را در لینک زیر بخوانید
https://eghtesadsanj.ir/?p=161318
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/680846" target="_blank">📅 15:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680845">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
انهدام باند جعل گذرنامه در تهران
معاون گذرنامه تهران بزرگ:
🔹
یک باند حرفه‌ای جعل گذرنامه و کلاهبرداری در پایتخت منهدم شد. این باند با استفاده از مدارک و هویت‌های جعلی، اقدام به صدور گذرنامه‌های غیرقانونی برای متقاضیان می‌کرد و از آنان مبالغ هنگفتی دریافت می‌نمود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/680845" target="_blank">📅 15:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680844">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0c1537e0.mp4?token=qm0qY7QfI5L-uTIw0Lqcqfk4yeu6TxkMgNHYsiNOv27oVPWcQCm9eYRlD69LktKBY5opTcIfhPF41buFxkO0HA4vbcy-eB_mw4qe_ke-Pc6b7LEw2M5rEtmXytewa52fZxKLKkxKnhRhBXfaqyvWWXb0rusjEcNHc9I1vn3X8C3Jak5ib29C2LJJUB5Dncag7DSVs_pWakCQR6DaPUXfl-aFlepLWOISYpF4Dh56zhcjX2qcl6uxrCHzHn2JMbGt-KRc7Q1CqCuUKT8AjQGgnqOODVscfmD_o6CXco8XbjWFZgeZhXSmd7na4ig3qvAP8rg3vfY-EQ9PVsOc_7CNBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0c1537e0.mp4?token=qm0qY7QfI5L-uTIw0Lqcqfk4yeu6TxkMgNHYsiNOv27oVPWcQCm9eYRlD69LktKBY5opTcIfhPF41buFxkO0HA4vbcy-eB_mw4qe_ke-Pc6b7LEw2M5rEtmXytewa52fZxKLKkxKnhRhBXfaqyvWWXb0rusjEcNHc9I1vn3X8C3Jak5ib29C2LJJUB5Dncag7DSVs_pWakCQR6DaPUXfl-aFlepLWOISYpF4Dh56zhcjX2qcl6uxrCHzHn2JMbGt-KRc7Q1CqCuUKT8AjQGgnqOODVscfmD_o6CXco8XbjWFZgeZhXSmd7na4ig3qvAP8rg3vfY-EQ9PVsOc_7CNBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: هیچ کشتی بدون مجوز و نظارت ایران امکان تردد امن را از تنگه هرمز ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/680844" target="_blank">📅 15:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680843">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV3bB0lNLrRuO_L2veq7YA6xXSurfBlyric8HfVdT5K8Fj6UK8IcYKkzHGsb8siI6a1-FdDL6furvNjLhiySx8P-987L14kNS9HBtkJV_aFEL122qFQsSujUPsT2gDCs6F7O0E41yhi1zkUyVRHsFhP3sjLPN3dEqTunuUErQ3wjNTUbN6KwJKU6BWppygNSxYSwNBnG0ABzq1OONhmWieZOoXjADjuvv631m_hhg8Y1RDCiAGY4q9kLY2Ni6g2JJwxUuTwD15WoINeGXS9b-kCbfDMXlFB9aaDUfiCVVOHcyXgWRlhKDSem0tBxJuIF10RCctaFTJJvJNzIASteHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرج طهماسب و مرضیه برومند، پشت صحنه سریال عروسکی مدرسه موش‌ها در دهه شصت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/680843" target="_blank">📅 15:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680842">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
برگ برنده جدید سرمایه‌گذاران در بورس؛ اینجا سود ۲ برابری می‌دهد!
🔹
۳۵ صندوق بخشی که از سال ۱۳۹۵ راه‌اندازی شده‌اند، حالا بیش از ۱۰۲ هزار میلیارد تومان دارایی تحت مدیریت دارند.
🔹
یعنی نزدیک به یک‌سوم منابع صندوق‌های سهامی به این گروه اختصاص یافته است.
🔹
اما جذاب‌تر از حجم سرمایه، عملکرد برخی صنایع است؛ صنعت سیمان از ابتدای ۱۴۰۰ تاکنون ۵۸۴ درصد رشد کرده؛ بیش از دو برابر رشد ۲۷۳ درصدی شاخص کل بورس!
🔹
صندوق بخشی یک نوع صندوق سرمایه‌گذاری در بورس است که به‌جای اینکه در کل بازار پخش شود، تمرکزش را روی یک صنعت خاص می‌گذارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/680842" target="_blank">📅 15:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea9e72aa4.mp4?token=vyahl06QHvk5HauGut9JXuAZaNkLU6YNYemp_iXjO6Ujk1Ip0dmcIA1j-KWGZQMCRVU2iERLOH5yQ1-lhOdim2DO9qELvLJ4JjZnb0T4dC7kayp1l2T-XuaVra0MD5ORm-2k7Wb6UMc5T0KJJu4ojaKFNkLRUSJz_92oZZdR_ziy3oK2wLoaXSnGGQjN4W8qTw6RDx-RsRolVV8KDHyMeP98YqCCn77DqzYpCFir07Ksf4GvyahHPkLIpc1nWyXhsUUNtbNfU6JTCII_2GbYleC0BiJooS61iDN8mbzfjl1SfZOb8espag_hti5F-chsEqaXH9U1KEi9ii8VeSmw8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea9e72aa4.mp4?token=vyahl06QHvk5HauGut9JXuAZaNkLU6YNYemp_iXjO6Ujk1Ip0dmcIA1j-KWGZQMCRVU2iERLOH5yQ1-lhOdim2DO9qELvLJ4JjZnb0T4dC7kayp1l2T-XuaVra0MD5ORm-2k7Wb6UMc5T0KJJu4ojaKFNkLRUSJz_92oZZdR_ziy3oK2wLoaXSnGGQjN4W8qTw6RDx-RsRolVV8KDHyMeP98YqCCn77DqzYpCFir07Ksf4GvyahHPkLIpc1nWyXhsUUNtbNfU6JTCII_2GbYleC0BiJooS61iDN8mbzfjl1SfZOb8espag_hti5F-chsEqaXH9U1KEi9ii8VeSmw8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری جف مارکلی، سناتور آمریکایی: شمار نظامیان کشته یا مجروح آمریکا در «جنگ ترامپ» از ۶۰۰ نفر فراتر رفته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/680841" target="_blank">📅 15:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
روسیه: کسی تعلق جزایر کوریل به روسیه را زیر سوال ببرد، با عواقب وخیمی روبرو خواهد شد.
🔹
پلیس هلند از کشته شدن یک نفر و مجروح شدن چندین تن در پی وقوع انفجار در بندر روتردام خبر داد.
🔹
با دستور دادستان مرکز لرستان جرثقیل‌های خطرآفرین پروژه بلاتکلیف کیو جمع‌آوری شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/680840" target="_blank">📅 15:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
نتانیاهو: شاید بتوانید بریتانیا را «جمهوری اسلامی بریتانیا» بنامید
🔹
اولین جمهوری اسلامی دارای سلاح هسته‌ای، انگلیس خواهد بود./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/680839" target="_blank">📅 15:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVDapTJdqcSZC4nDyCoP4lulSHQ2I05eMifGBKBuaKFSu8mDBr9uRH846i-t8BusjdImRlB_olnDlrzGlSqMX7Y2eHG6M-YAzff6aixkiy1IJBZIvX_kNBs9jET21LLmGXAOhX7PpVsiiRprSn331_8qtI6-izkuPuC8HAZofutYjVymTFyLnpEllQes7GF-LToQ-rna2T9Hx6aGsh82R09SATWG-11JXN8T3ATWUQhlNOWViO6loOdojWoK_gOiNkez-oorUKcYnEe86CPsV_y3IQC_jv4ga2znqnNKaL_EvSialL5dBIoOR97eUi_aFXOpOru2AoZP4BkPiKE78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد بمب‌های اتمی جهان در سال ۲۰۲۶
🔹
روسیه با ۵۴۲۰ و آمریکا با ۵۰۴۲ کلاهک اتمی، بیشترین سهم از تسلیحات هسته‌ای جهان را به خود اختصاص داده‌اند.
🔹
چین با ۶۲۰ کلاهک در جایگاه سوم قرار دارد و فرانسه، انگلیس، هند، پاکستان، رژیم صهیونیستی و کره شمالی در رده‌های بعدی هستند.
🔹
همچنین رژیم صهیونیستی به عنوان تنها دارنده بمب اتمی در خاورمیانه، هرگز تحت نظارت و پاسخگویی بین‌المللی قرار نگرفته است.
@amarfact</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/680838" target="_blank">📅 15:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680837">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
هشدار اتحادیه اروپا به شهرک‌نشینان صهیونیست
🔹
خشونت، ارعاب، تخریب خانه‌ها و اموال به دست شهرک‌نشینان در کرانه باختری باید متوقف شود.
🔹
باید اقدامات ملموسی برای جلوگیری از خشونت شهرک‌نشینان و تضمین مجازات عاملان جرایم انجام شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/680837" target="_blank">📅 15:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680836">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh_p6rdoj2A5JJIAlD-ljnlH2jnP3ffywU3rsp2jVHBLTKyHGmFtnhAXihF38suI9y24XTxDNIxEjbMR9ZEHSpfD-l2sVCRvyZloGN7cFf5DI2M4eL3cFULC8npk4AoU_n4mHQx3Ncyhf6yAo-13Y0_nZzxBaBGh6D6VrlB36aFwvqWZkfwoNsnO4Ng0hTgAMTs6qPOvRS6SJ5QKY1ERQbDACEAet7t85lG2mMQqRO_ZA2QvI2BApluLEILUlcKuWN41r8X9NcK2V7eDhepXFTbM1cCHDUjtA-kq7F9obk1g1f6eROixI2Qnr-1LD_YClYpFlICquEKQNH8jWypR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقاله جنجالی اسرائیل هیوم: همه راه‌ها به تهران ختم می‌شود/ رسانه صهیونیست نتانیاهو را تشویق به حمله به ایران کرد؛ برای جبران سه شکست باید با ایران جنگید
🔹
اسرائیل هیوم می نویسد: جنگ اسرائیل با سه جبهه یعنی غزه، لبنان و سوریه همچنان در جریان است و علت این مساله این است که جنگ اسرائیل با ایران همچنان ادامه دارد و پایان نیافته است و تا این جدال پایان نیابد، هیچ امیدی وجود ندارد که سه جدال دیگر در سوریه، غزه و لبنان به نفع اسرائیل به پایان یابد.
ترجمه این گزارش را در وبسایت خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3237291</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/680836" target="_blank">📅 15:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680835">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca11fedaa.mp4?token=DqdFDmMaqXj1MeDzIAq5Bu9sKfNW8bniXVv_zYcpwFXUIUo9ujhCcn7RhEUooc_FuW6mAXJCyzEFDDUU_ffD7SyBXHCO5htlch9XZePdwfFOpP1qx0tsH7CDZM7ZoWI6WYaNbbxi0H1gu9jyOWNTohJIyUfN_2rf-diPcr5f_VwMfJIZlZCzm4HKH5v2kI21tg8wQym0MJSjROa_f36RJKrlUqi8gVKDj5-C2JHic5lHWl4tPLjJG9ZFYy4q5pSM7ti0fgB-U8CuOk7ZexlQC1qfBvGg3tRJ-uFA463fExcSCtNXMfoTtvicT50BcEPiwEBe1gWtexjuetnBeX1mpIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca11fedaa.mp4?token=DqdFDmMaqXj1MeDzIAq5Bu9sKfNW8bniXVv_zYcpwFXUIUo9ujhCcn7RhEUooc_FuW6mAXJCyzEFDDUU_ffD7SyBXHCO5htlch9XZePdwfFOpP1qx0tsH7CDZM7ZoWI6WYaNbbxi0H1gu9jyOWNTohJIyUfN_2rf-diPcr5f_VwMfJIZlZCzm4HKH5v2kI21tg8wQym0MJSjROa_f36RJKrlUqi8gVKDj5-C2JHic5lHWl4tPLjJG9ZFYy4q5pSM7ti0fgB-U8CuOk7ZexlQC1qfBvGg3tRJ-uFA463fExcSCtNXMfoTtvicT50BcEPiwEBe1gWtexjuetnBeX1mpIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هگست: اقدام نظامی آمریکا علیه کوبا همچنان روی میز است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/680835" target="_blank">📅 15:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680834">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بنزین؛ این‌بار فقط مردم نه!
🔹
در کشور ما معمولاً بحران باید به مرز انفجار برسد تا برای حل آن تصمیم بگیریم؛ آن‌هم در شرایطی که ترس از هزینه‌های کوچکِ امروز، ما را ناگزیر به پرداخت هزینه‌های بسیار بزرگ‌تر در فردا می‌کند.
🔹
گاهی تصمیم را آن‌قدر به تأخیر می‌اندازیم تا دیگر «انتخاب»ی باقی نماند و آنچه می‌توانست با تدبیر اصلاح شود، با اضطرار و هزینه‌ای چند برابر بر سرمان آوار شود.
🔹
داستان بنزین، یکی از روشن‌ترین روایت‌های این تعلل است. قیمت سوخت می‌توانست دو دهه پیش، آرام و تدریجی و با کمترین هزینه اجتماعی اصلاح شود؛ اما ملاحظات سیاسی و تصمیم‌های کوتاه‌مدت، امروز ما را به نقطه‌ای رسانده که اصلاح قیمت، بیش از آنکه یک انتخاب باشد، به ضرورتی اجتناب‌ناپذیر بدل شده است.
🔹
حالا اگر قرار است یارانه بنزین اصلاح شود، عدالت ایجاب می‌کند که بار این اصلاح تنها بر دوش مردم گذاشته نشود. همزمان با اینکه قیمت را بالا ببریم، باید به سراغ آنچه مصرف را بی‌دلیل بالا برده است برویم.
🔹
خودروسازی ناکارآمد، خودروهای پرمصرف، ناوگان فرسوده و سال‌ها سیاست‌گذاری نادرست بیشتر از مصرف مردم به این سرمایه آسیب زده است.
🔹
در کنار اصلاح این موارد باید یارانه سوخت به کارت بانکی متصل به کد ملی منتقل شود، مصرف شفاف شود، صورتحساب‌ها الکترونیکی شوند، سبد سوخت توسعه یابد و یارانه انرژی عادلانه‌تر توزیع شود.
🔹
مردم با تصمیم سخت همراه می‌شوند، اگر احساس کنند سختی، فقط سهم آنان نیست.
🔹
صیانت از سرمایه ملی یعنی همه در اصلاح شریک باشند؛ دولت، مجلس، خودروساز و مصرف‌کننده.
امروز اگر شجاعتِ اصلاح همراه با انصاف داشته باشیم، شاید هزینه‌ای بپردازیم؛ اما اگر باز هم تصمیم را به فردا حواله کنیم، فردا دیگر بهای اصلاح را نمی‌پردازیم، بهای یک بحران را خواهیم پرداخت.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/680834" target="_blank">📅 14:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680832">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/064ab06f45.mp4?token=jWK3b3lJ7FBWND9Fquh8QAp1A4DqecvD1h9XE13Ms6HHYAlr0rnfgUCYTYjRTm-a2XehnOLAngitINJi-U1rcAtRQbH3xuUS5_82PwXbgW2URSa8lJEnLUxBqCNZxaDyGtiQYXqfcRp9RfSmaYwwM9PrTqNLhttNzF5AwaEBwpiNch1VoUF1MeX9A-6kJP7uxBMYvyyXXomtMoo7m71zlW_oTCbLqyBNhqKR-El-j28WQPH7R9qhsFf1jYnawX5CM5tiw2GGt7c53fxhWt5Oqz4fWQ7slMEQE0XKKd6xRffIdv5DYtyRDM7vBiTTBIlcQXWvLmNAvuFP_DiHNn6_Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/064ab06f45.mp4?token=jWK3b3lJ7FBWND9Fquh8QAp1A4DqecvD1h9XE13Ms6HHYAlr0rnfgUCYTYjRTm-a2XehnOLAngitINJi-U1rcAtRQbH3xuUS5_82PwXbgW2URSa8lJEnLUxBqCNZxaDyGtiQYXqfcRp9RfSmaYwwM9PrTqNLhttNzF5AwaEBwpiNch1VoUF1MeX9A-6kJP7uxBMYvyyXXomtMoo7m71zlW_oTCbLqyBNhqKR-El-j28WQPH7R9qhsFf1jYnawX5CM5tiw2GGt7c53fxhWt5Oqz4fWQ7slMEQE0XKKd6xRffIdv5DYtyRDM7vBiTTBIlcQXWvLmNAvuFP_DiHNn6_Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ قانون مهم مدیریت پول
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/680832" target="_blank">📅 14:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680831">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
آیا تنگه هرمز به گران‌ترین مسیر جهان تبدیل می‌شود؟
🔹
بر اساس گزارش سازمان بین‌المللی دریانوردی، رویترز، گاردین، CMA CGM و Marsh، بحران تنگه هرمز هزینه‌های کشتیرانی را به‌شدت افزایش داده است؛ کرایه سفر سوپرتانکر از ۲ به ۲۵ میلیون دلار، اجاره روزانه نفتکش خارج از هرمز به ۱۹۰ هزار دلار و بیمه جنگی از ۰.۲۵ به ۳ درصد رسیده است. افزایش هزینه‌های کانتینری، تغییر مسیر کشتی‌ها و رشد هزینه بیمه، این شوک را به زنجیره تأمین، قیمت کالا، انرژی و تجارت جهانی منتقل کرده و تداوم آن می‌تواند فشار تورمی و هزینه‌های اقتصادی گسترده‌تری ایجاد کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/680831" target="_blank">📅 14:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680830">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf8b42ced.mp4?token=OfoQJz4P6i3xXasUWfBCVwsInw-Hz_0nbgkluItz_m6P3F1pxhd7Ls0LXFjFyXI4rc7L3Wv8VJ-aR7cf5hlq-VRgVdd44B8PUFPlDmh4kWTNKH-lv8uHMK-eHNQwkK82Zgm3Qn_qk1nP0Q1ymsVYO6B98sgOLLgeMj_y0hhalniwtUs_WGsV4CB-gjGmfZSHxZArWvn3IwzvE6DMKwjYQBq15OrQYaFWJ8_Avcw6fOrr3DaobhaanvJDIdDkSMpk8ApB6EnGVMmm0H7xpHatDXeD8aPtbRcij-PTfHq5UBy9IJenzXVECzIC3czzFEY2duGVnNixeorGG7AJhMiklA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf8b42ced.mp4?token=OfoQJz4P6i3xXasUWfBCVwsInw-Hz_0nbgkluItz_m6P3F1pxhd7Ls0LXFjFyXI4rc7L3Wv8VJ-aR7cf5hlq-VRgVdd44B8PUFPlDmh4kWTNKH-lv8uHMK-eHNQwkK82Zgm3Qn_qk1nP0Q1ymsVYO6B98sgOLLgeMj_y0hhalniwtUs_WGsV4CB-gjGmfZSHxZArWvn3IwzvE6DMKwjYQBq15OrQYaFWJ8_Avcw6fOrr3DaobhaanvJDIdDkSMpk8ApB6EnGVMmm0H7xpHatDXeD8aPtbRcij-PTfHq5UBy9IJenzXVECzIC3czzFEY2duGVnNixeorGG7AJhMiklA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط اسم قانون شفافیت به یک سازمان رسید، فیش های حقوقی شان اصلاح شد!/پس از آنکه مخبر قانون شفافیت را ابلاغ کرد، دیگر کسی پیگیر اجرای قانون نشد. چرا؟
/ تلویزیون اینترنتی مدار
این برنامه را در لینک زیر ببینید
👇
https://www.aparat.com/v/htjp67n
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/680830" target="_blank">📅 14:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680828">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada1abc8c0.mp4?token=DeEpPz-a-u8SJ7j1HQrYi6YloQ7yrJti-XbMQ2MiqqVMEcE4SpRkofEx1aBSgMpoQAesr7hcEPJzkKx1six2GBb7X8fye_PePBRX-GDaAdJ2UYDe1pHJPe8eQQPfeYmaxVXlm__axXARzPaoD4OpyzsQpRF8hJ_unURK_OI-k4Sp7SNT1r1SHONL6zGmoEcZyDep7k6OY_56D1d6Rso-w6i_mFEHXwNxRhMHPNQc4tnQBeZ0qV51AS4ApTkTTuglhFJxalNl4VVS1RYZeshWtVtAEK3sr9jwl8_995RoD8JGua6w14A-89z63PssYVSJtxM0icWAP1_CcnTMpaahWRzyBBYYPhWdoETOE087pGncrIzJ4YOkQn0-IjEtjS8cx-zLMpZ6U_ufWPRL07RYZC_fOPIMUDvHSm9iClPk-3T8O5yv0uvnRWubJgcbKv9GgcTT_SL-TjH0LnxZkmlDgrtkirb7FFp6T07TyQglYGdRI-sgKzn_VgohDFx0VgGIg0DtUd6_vVcmOKTfYSQmW6wTh7EdeesjlLeeyU15MpjZOo92TgKnWx5JB0aN2JraygkVKbdFEJuJdutsZs9HSytIUA1js9tuZA5dvNO1GYKQHJeqZSoZsTfR5VI733-74tddbsOorltxRLgsZeqDhbfXeZDQsx2AozZ8YXI2A1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada1abc8c0.mp4?token=DeEpPz-a-u8SJ7j1HQrYi6YloQ7yrJti-XbMQ2MiqqVMEcE4SpRkofEx1aBSgMpoQAesr7hcEPJzkKx1six2GBb7X8fye_PePBRX-GDaAdJ2UYDe1pHJPe8eQQPfeYmaxVXlm__axXARzPaoD4OpyzsQpRF8hJ_unURK_OI-k4Sp7SNT1r1SHONL6zGmoEcZyDep7k6OY_56D1d6Rso-w6i_mFEHXwNxRhMHPNQc4tnQBeZ0qV51AS4ApTkTTuglhFJxalNl4VVS1RYZeshWtVtAEK3sr9jwl8_995RoD8JGua6w14A-89z63PssYVSJtxM0icWAP1_CcnTMpaahWRzyBBYYPhWdoETOE087pGncrIzJ4YOkQn0-IjEtjS8cx-zLMpZ6U_ufWPRL07RYZC_fOPIMUDvHSm9iClPk-3T8O5yv0uvnRWubJgcbKv9GgcTT_SL-TjH0LnxZkmlDgrtkirb7FFp6T07TyQglYGdRI-sgKzn_VgohDFx0VgGIg0DtUd6_vVcmOKTfYSQmW6wTh7EdeesjlLeeyU15MpjZOo92TgKnWx5JB0aN2JraygkVKbdFEJuJdutsZs9HSytIUA1js9tuZA5dvNO1GYKQHJeqZSoZsTfR5VI733-74tddbsOorltxRLgsZeqDhbfXeZDQsx2AozZ8YXI2A1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ تا کجا جرائت پیشروی در ایران را دارد؟
🔹
ترامپ بارها از حمله به زیرساخت‌های حیاتی ایران گفته، اما چرا درست در لحظه‌ای که باید تصمیم بگیرد، عقب می‌کشد؟
🔹
آیا پای ترس از پاسخ ایران در میان است؟ یا واشنگتن می‌داند شلیک این «آخرین تیر» می‌تواند معادله جنگ را برای همیشه تغییر دهد؟
🔹
پاسخ، از چیزی که فکر می‌کنید پیچیده‌تر است. در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/680828" target="_blank">📅 14:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680826">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b554f9121.mp4?token=FEsuECATvlpUlZWLydbd1hvC4B88UWBhQmWUBOTf5awPW2JRiD_VNv3sqkH5s721nrYSYOy8J9lEqOtRgdhbH2wuYKroPfW6gKEpIumSbTs8tIhjCCla8K1nlCxVnU8Ym37lq9fjfqrGvuKYzrEWJOrIeoigJkyrJRYBG-MxIIw-VxxRhcYgwCUUq1X6YrKjCZ6qf_QTqLmhg0qb3gHwf8WOmW92UwXQHZoWfG3H0mGxcQnFS_HaAY0jZ4PbYILQhyo7X_p6RQ_ygvUfDgTIW3kWigCmO6EGYxpEgnU2G_pvXdioltYg2W5x_VAWdOumFUTxjtZikDyL7vATF-sFtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b554f9121.mp4?token=FEsuECATvlpUlZWLydbd1hvC4B88UWBhQmWUBOTf5awPW2JRiD_VNv3sqkH5s721nrYSYOy8J9lEqOtRgdhbH2wuYKroPfW6gKEpIumSbTs8tIhjCCla8K1nlCxVnU8Ym37lq9fjfqrGvuKYzrEWJOrIeoigJkyrJRYBG-MxIIw-VxxRhcYgwCUUq1X6YrKjCZ6qf_QTqLmhg0qb3gHwf8WOmW92UwXQHZoWfG3H0mGxcQnFS_HaAY0jZ4PbYILQhyo7X_p6RQ_ygvUfDgTIW3kWigCmO6EGYxpEgnU2G_pvXdioltYg2W5x_VAWdOumFUTxjtZikDyL7vATF-sFtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تصاویر به سقوط فضاپیمای استارشیپ در سال گذشته تعلق دارد و ارتباطی با بارش شهابی آسمان قزاقستان ندارد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/680826" target="_blank">📅 14:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680825">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403c0eb549.mp4?token=iD9940EiJdQOZ09YQTjnibSQJH90m26vpei_b1uUBg4panujrB_f_Ap2W7iuYyk-0UaSteVNPfb6UjL_45LyV6bzKRiQqmrF7oybaAtbM1ZSctIfVHzviy6HktzxyTK0c_aMHAu_jbCDrMFDPKbdvltMtrPqPJOgzPewVQo6Bl-1fyaL5SQcBjUdNJIjNin-iGVz9WCMAg-dME_AVWDFdXK9yQjIs1BbY81mlvnpLQI-cJCzagmale0raR05ry6nUO7S3r9Se0hOBQ05EZufDIH6U1MbmvpMx3IRSq4aiW2wKJU1mh88dlOdpz-UWl7m--Q9mN53FcdCZqzuNE0hyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403c0eb549.mp4?token=iD9940EiJdQOZ09YQTjnibSQJH90m26vpei_b1uUBg4panujrB_f_Ap2W7iuYyk-0UaSteVNPfb6UjL_45LyV6bzKRiQqmrF7oybaAtbM1ZSctIfVHzviy6HktzxyTK0c_aMHAu_jbCDrMFDPKbdvltMtrPqPJOgzPewVQo6Bl-1fyaL5SQcBjUdNJIjNin-iGVz9WCMAg-dME_AVWDFdXK9yQjIs1BbY81mlvnpLQI-cJCzagmale0raR05ry6nUO7S3r9Se0hOBQ05EZufDIH6U1MbmvpMx3IRSq4aiW2wKJU1mh88dlOdpz-UWl7m--Q9mN53FcdCZqzuNE0hyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای حرمت ملجأ درماندگان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/680825" target="_blank">📅 14:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680824">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2faa71b2fc.mp4?token=UvyMZQ2gcSLH9PRzxJtUjVqWnKZMf_OIquqn3h72VyniUhRRir5-ZeZtkIstmOkDHYdW26g-K01CU9197h5uXONnYo3mL6UAUCeYqhlkPUr_TX9AJUFNcP7MnNl9GShsWmt2vykZAA1kQtyQdWgjT6-C7liqgHmPjmoidgOxuW8TgzcN-jwaOJboF-e8tnjhuT3etb_43cE8ILGbk9aeUZZOMjBt_dxsi2YeyK68VJ_GotK2SKVfadBQUIlu5aGmlzSRpwUS_wXntYEUAuTsyK0NmKQ47jfPtjsJLxCXWmisSP-DuwKtyPbJFd-yM0hkiaiU8mME1JVhbZP2ClpUsnEhN9xaNF8c9Z-BxzJMavwuFkEtEY4hbwCf_-Z_m1p07hMNfvNItFSjSkLw8GD9fl0de-DAYi_m0wKygOCF5Nu6ufoInMT5TecZabc2Hr0VYjGKa18Jgtnlp-3LAVmkUJIeUPRJYwNGi-D70h83hoj6TZqwW_SpkD4kP1Oqlovlofml5dYJtsBIaPYRxwNawGG5cG5Pn8EGJyG6AooxDU4EoZ_5RoPeq7ibjW3c1gSHzDYtDmf9xtVnKexplLZwfVYlzpi7AZ5ua8PYcqatUtK8WqHBtoBVUQ5nhRPFoFFR4Vyd2XZGbyBkIEqFbL1dYUHmv2-mbf-RBV8elLoOXG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2faa71b2fc.mp4?token=UvyMZQ2gcSLH9PRzxJtUjVqWnKZMf_OIquqn3h72VyniUhRRir5-ZeZtkIstmOkDHYdW26g-K01CU9197h5uXONnYo3mL6UAUCeYqhlkPUr_TX9AJUFNcP7MnNl9GShsWmt2vykZAA1kQtyQdWgjT6-C7liqgHmPjmoidgOxuW8TgzcN-jwaOJboF-e8tnjhuT3etb_43cE8ILGbk9aeUZZOMjBt_dxsi2YeyK68VJ_GotK2SKVfadBQUIlu5aGmlzSRpwUS_wXntYEUAuTsyK0NmKQ47jfPtjsJLxCXWmisSP-DuwKtyPbJFd-yM0hkiaiU8mME1JVhbZP2ClpUsnEhN9xaNF8c9Z-BxzJMavwuFkEtEY4hbwCf_-Z_m1p07hMNfvNItFSjSkLw8GD9fl0de-DAYi_m0wKygOCF5Nu6ufoInMT5TecZabc2Hr0VYjGKa18Jgtnlp-3LAVmkUJIeUPRJYwNGi-D70h83hoj6TZqwW_SpkD4kP1Oqlovlofml5dYJtsBIaPYRxwNawGG5cG5Pn8EGJyG6AooxDU4EoZ_5RoPeq7ibjW3c1gSHzDYtDmf9xtVnKexplLZwfVYlzpi7AZ5ua8PYcqatUtK8WqHBtoBVUQ5nhRPFoFFR4Vyd2XZGbyBkIEqFbL1dYUHmv2-mbf-RBV8elLoOXG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت سی‌ام از فصل پنجم
🔹
سومین قسمت از تجربه‌ نزدیک به مرگ آقای سید محمد موسوی که به همراه دوستی که در دنیا خودکشی کرده بود به طبقه ۸ ام جهنم می‌رود و عذاب دردناک آنجا از جمله رها شدن در تاریکی مطلق که هیچ نگاهی از رحمت الهی در آن طبقه نمی‌باشد را درک می‌کند و به ترتیب طبقات را بالا آمده و در هر طبقه عذاب مربوط به هر گناه از جمله نگاه به نامحرم تا قسم‌های دروغ و ظلم به پدر و مادر و همسر را چشیده تا از آن طبقات عبور کند ولی بالاخره با لطف الهی اجازه بازگشت به دنیا برای جبران به او داده می‌شود را نظاره می‌کنید.
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید محمد موسوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/680824" target="_blank">📅 14:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680823">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تخلیه ساختمان‌های اطراف ایستگاه قطار بایرن به ظن وجود بمب
پلیس آلمان:
🔹
در پی کشف یک شیء مشکوک با ظن به وجود بمب در نزدیکی خطوط راه‌آهن در ایالت بایرن، ساختمان‌های اطراف منطقه به‌طور موقت تخلیه شدند.
🔹
نیروهای خنثی‌سازی بمب در محل حاضر شده و منطقه را محاصره کرده‌اند. پلیس از مردم خواسته تا اطلاع بعدی از نزدیک شدن به محل خودداری کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/680823" target="_blank">📅 14:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680822">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ka42dBKy4hVP9qzyrHIFYTVDorRXhUYfnDMYRgLM7qh0Jr-Id4FJA5x64oSrp4crZ4shsf8JN1elyj2W72GQIZjvl6Y8_UBRmgMBFC_ExFN1qu1XLu7rvlNuxNXIGlhBlNL1tGbLNOqynV2JBTtRe-68xIecZMYAKoV7wMDOBNy_7QvSy-Gy-pm0HPtL_4NNXn633iFRxJQ4gWgsGJn-IIOEHZmqTAopgKvbTRMwGgSVeMI7cDQsih6OAGTdb38yus5lw600ufS2pNN6r3t8ctfxUQWeQbAZGUyuqWXNEIGq1J7M0bt9tCuDdinwh_D1Z6XmX59jodKeUz56n6QDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ امریکا با ایران هر روز ۱ میلیارد دلار هزینه دارد
🔹
بر اساس داده‌های TheDataProject هزینه درگیری نظامی امریکا با ایران در ۶ روز نخست روزانه ۱.۸۸ میلیارد دلار بوده و پس از آن به حدود ۱ میلیارد دلار در روز رسیده است.
🔹
بر اساس همین داده‌ها، هزینه کل جنگ تاکنون از ۴۵.۳ میلیارد دلار عبور کرده؛ رقمی که پنتاگون آن را ۲۵ میلیارد دلار برآورد کرده است.
🔹
اگر این ارقام درست باشند، جنگ ایران از نظر هزینه روزانه، پرهزینه‌ترین جنگ آمریکا در تاریخ بوده و فاصله‌ای چشمگیر با جنگ عراق دارد؛ جنگی که روزانه حدود ۶۸۴ میلیون دلار هزینه داشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/680822" target="_blank">📅 14:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680821">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13df26e32b.mp4?token=eDYIsXyS5HHBp0RIGCfQ_P1QHubX35DbJCmIof57JLb5SjokBkFmNo4PXfgO5X7qHVubVunY3OlDYxGsYEWXJmXkERv7aRCREtMFpyowgXeLs_9m39Txm4HAYGPbuteNkdI0DcG3lOpauEU3sslCAlUbiygIj6sDKDc_5dGAV_lxBV-dHLolCQNArFk0fJDC8CtPedUZwk4H9rEfgVeUvPzcipr4-zFtc6l9sEKpgOIU2nSKYDMqu9cGQlSuO5o9sUtTNDuLUnln7TswGYjZej_CZEYkW5zJBmfUx3Vqr-3M7bA8WFyvaZmY_1X10A_MEnh_V49WjbhGRK-1vn9diW7uuxcGv7Ms1vMuqxYX3PxEaEIEE0zezIZDTvKIQa48iSFSQu-J6wJxL4oMpA0kqBOYzBxjYuECMd7VCJUy-g49aixzvDkQIY_HJomdC9lHOIXiL17c3ZwgC8xksuWxS55bM4hEIbnYra2Z4_a5lSU8XpM5oNoodd9J62tYJj128SQZ-qT3i7WNUkHyqKbOS39c0gTfPwubl2Uqgj6BbX0iatC57jHjQK3GO-818ZtUuO21W4m_ipQ1pVm1YlZIpAsLhN5N7zSj3f3NRZxjlToAcKo5J9oqGOWVmuKLiGWwGQURKPmIP-j7ji3-m9wGpgD2t29_2sUcmZTJVaYFYV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13df26e32b.mp4?token=eDYIsXyS5HHBp0RIGCfQ_P1QHubX35DbJCmIof57JLb5SjokBkFmNo4PXfgO5X7qHVubVunY3OlDYxGsYEWXJmXkERv7aRCREtMFpyowgXeLs_9m39Txm4HAYGPbuteNkdI0DcG3lOpauEU3sslCAlUbiygIj6sDKDc_5dGAV_lxBV-dHLolCQNArFk0fJDC8CtPedUZwk4H9rEfgVeUvPzcipr4-zFtc6l9sEKpgOIU2nSKYDMqu9cGQlSuO5o9sUtTNDuLUnln7TswGYjZej_CZEYkW5zJBmfUx3Vqr-3M7bA8WFyvaZmY_1X10A_MEnh_V49WjbhGRK-1vn9diW7uuxcGv7Ms1vMuqxYX3PxEaEIEE0zezIZDTvKIQa48iSFSQu-J6wJxL4oMpA0kqBOYzBxjYuECMd7VCJUy-g49aixzvDkQIY_HJomdC9lHOIXiL17c3ZwgC8xksuWxS55bM4hEIbnYra2Z4_a5lSU8XpM5oNoodd9J62tYJj128SQZ-qT3i7WNUkHyqKbOS39c0gTfPwubl2Uqgj6BbX0iatC57jHjQK3GO-818ZtUuO21W4m_ipQ1pVm1YlZIpAsLhN5N7zSj3f3NRZxjlToAcKo5J9oqGOWVmuKLiGWwGQURKPmIP-j7ji3-m9wGpgD2t29_2sUcmZTJVaYFYV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع مقابل شرکت نظامی «ترما» در دانمارک در اعتراض به حمایت از رژیم صهیونیستی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/680821" target="_blank">📅 13:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680820">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4a2cb90e.mp4?token=pf6g9vNzf98CJ0-lgc6rY8U8hmfQq62Gi_9jtrRIGfA_ACLD2-4rftF00IWgsyn5jT0oHcz-heHMfLqUSshGvZ_37nRBV2nCjffPHdzVfnYvKW7DHnP0kZLHe2MyrIqB-fQjFpCsvOYdUUZNkpGgMG2LmmHKsR-AHWnibtt2OX3DKZ8My11f45Xq1J9g_qYBhugQlNMl1W0FbN1bFKJI1y0jnhze9eTx6VVUrs_JzLybCdn4DESWJ2GG7zUWC8eAEBzTbRzk7Itqfluipy9OhZifna772WMSCcIxGUIgO7lZeOUOyxMynRlj9cWECUNWQgOMtN9q2F4NwmSIf1b6hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4a2cb90e.mp4?token=pf6g9vNzf98CJ0-lgc6rY8U8hmfQq62Gi_9jtrRIGfA_ACLD2-4rftF00IWgsyn5jT0oHcz-heHMfLqUSshGvZ_37nRBV2nCjffPHdzVfnYvKW7DHnP0kZLHe2MyrIqB-fQjFpCsvOYdUUZNkpGgMG2LmmHKsR-AHWnibtt2OX3DKZ8My11f45Xq1J9g_qYBhugQlNMl1W0FbN1bFKJI1y0jnhze9eTx6VVUrs_JzLybCdn4DESWJ2GG7zUWC8eAEBzTbRzk7Itqfluipy9OhZifna772WMSCcIxGUIgO7lZeOUOyxMynRlj9cWECUNWQgOMtN9q2F4NwmSIf1b6hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتی صندلی طبی؛ راحتی واقعی هنگام رانندگی و کار
😌
✅
پرکننده فضای خالی پشت کمر
✅
کمک به حالت صحیح ستون فقرات
🦴
✅
جلوگیری از تعریق با توری خنک
🌬
✅
نصب سریع و آسان روی صندلی
🚗
✨
مناسب خودرو و محل کار
💺
🏢
🔴
قیمت 1,098,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/36246/180124/</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/680820" target="_blank">📅 13:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680819">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d782dea63.mp4?token=dAX6WcV39tU78GHyPbnQwmBB0j7a1Az9giO87SFJXbh6XDB7YHXSFIGFtKKc0W15thu9wH9D8BctpHVgGHhOmLp6Vtk_b1Y81zGCob__vOkY7Rb2BCFXu4-EmyjmvqTZINl_Hjl4mfCsjIlYFBR2ALrUKtumCjzHlDZFdFiPBpe_B0Y3uNPVs_NEfnPUue5HhLoIeuMVrntZzZSB9pbWYuk5NXp7-VqG6qEtfmKDWLGaraOeytdIK_hNwWECRiHpOY_tSm47p9ZF7vAUfPDCC_CTajmUYmSC4C4AQPJA-zudx0rxfG8aUyJxceDZB71PuCaySBCo4nP8F-p1uBGyiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d782dea63.mp4?token=dAX6WcV39tU78GHyPbnQwmBB0j7a1Az9giO87SFJXbh6XDB7YHXSFIGFtKKc0W15thu9wH9D8BctpHVgGHhOmLp6Vtk_b1Y81zGCob__vOkY7Rb2BCFXu4-EmyjmvqTZINl_Hjl4mfCsjIlYFBR2ALrUKtumCjzHlDZFdFiPBpe_B0Y3uNPVs_NEfnPUue5HhLoIeuMVrntZzZSB9pbWYuk5NXp7-VqG6qEtfmKDWLGaraOeytdIK_hNwWECRiHpOY_tSm47p9ZF7vAUfPDCC_CTajmUYmSC4C4AQPJA-zudx0rxfG8aUyJxceDZB71PuCaySBCo4nP8F-p1uBGyiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام ۲ هسته‌ عملیاتی گروهک تروریستی-تکفیری  وزارت اطلاعات:
🔹
۲ هسته‌ سازمان‌یافته وابسته به سرویس‌های جاسوسی دشمن آمریکایی-صهیونیستی هنگام ورود به کشور در شهرستان خاش شناسایی و متلاشی شدند.
🔹
در این عملیات، ۴ تروریست بازداشت و ۲ تروریست دیگر در درگیری با…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/680819" target="_blank">📅 13:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680817">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پالایشگاه مسکو هدف قرار گرفت
🔹
پهپادهای اوکراینی به پالایشگاه نفت مسکو حمله کردند و در نتیجه آن، آتش‌سوزی در منطقه کاپوتنیا در جنوب شرقی پایتخت روسیه رخ داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/680817" target="_blank">📅 13:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680815">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b37ae36d.mp4?token=bkNslCkGG5R9DuPiJIqnjwpJexaKZUYBJeAu3VSELsClYxGTJNRFAVKnharEOfNEL-VqrmQsoJw6CdQDC4-0wdbWcvsawZcMPMSvGGGmFpYdEG-DKZmowxsta8smhc8lJFV_P_pTStBJAYtoOHC2v35b3lLD_VvLb-b9_Xcgmjjx5YHCR6iFjbPgFRs9WEEmEgn6rDJ505HrBfiq9TB4A1mS0QEQ27bTbAp8hqrWHivRZyIBeBB4Xu5YyWwp-XwwEZt_s1HyyX-sE6n0zEVyX0ZMIzr6G7LY7HDy4rN80Z4o63PC8DiSE4UCl6ggn49MSD-X5KVYpZ2anB21JyM3ValHNOiVcYuTlwpW3uSnAsGmxTBdFzaKXIMi6pebUYVX_xc7YzKWabFzKLxjTX74xuXgGmsT0dPbBslOjhDRpuYitBhryNPKKjGTldpz7g4kHEtEDKuhWxhlrF8LMfTkUMZSL2mhDwG1S4HMV40NilRYQTvqHSMrs4PRUXrzNknXgeCFu9vhr2MCrpl3oH-2spbeQsXTRhnaPb_Jkpa6AuTZSV3ls25alVIbP9ojhkQOE3P_gKviSBDe3uDWej3kNB4lKg1b2_IdhsqppcSkPXXRXkMz0XjBpyPMnsW3iHGhNZK19JFTi3KO-MvPpP2rnqIaFuBzJZ0KZrpQL7JsugY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b37ae36d.mp4?token=bkNslCkGG5R9DuPiJIqnjwpJexaKZUYBJeAu3VSELsClYxGTJNRFAVKnharEOfNEL-VqrmQsoJw6CdQDC4-0wdbWcvsawZcMPMSvGGGmFpYdEG-DKZmowxsta8smhc8lJFV_P_pTStBJAYtoOHC2v35b3lLD_VvLb-b9_Xcgmjjx5YHCR6iFjbPgFRs9WEEmEgn6rDJ505HrBfiq9TB4A1mS0QEQ27bTbAp8hqrWHivRZyIBeBB4Xu5YyWwp-XwwEZt_s1HyyX-sE6n0zEVyX0ZMIzr6G7LY7HDy4rN80Z4o63PC8DiSE4UCl6ggn49MSD-X5KVYpZ2anB21JyM3ValHNOiVcYuTlwpW3uSnAsGmxTBdFzaKXIMi6pebUYVX_xc7YzKWabFzKLxjTX74xuXgGmsT0dPbBslOjhDRpuYitBhryNPKKjGTldpz7g4kHEtEDKuhWxhlrF8LMfTkUMZSL2mhDwG1S4HMV40NilRYQTvqHSMrs4PRUXrzNknXgeCFu9vhr2MCrpl3oH-2spbeQsXTRhnaPb_Jkpa6AuTZSV3ls25alVIbP9ojhkQOE3P_gKviSBDe3uDWej3kNB4lKg1b2_IdhsqppcSkPXXRXkMz0XjBpyPMnsW3iHGhNZK19JFTi3KO-MvPpP2rnqIaFuBzJZ0KZrpQL7JsugY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش میوه خشک کردن به روش سنتی
🔹
برای تهیه میوه خشک باکیفیت، انتخاب میوه‌های تازه و سالم اهمیت زیادی دارد. میوه‌های مانده یا دارای زدگی، پس از خشک شدن کیفیت مطلوبی نخواهند داشت و ممکن است تغییر رنگ یا کپک‌زدگی ایجاد کنند.
🔹
ضخامت برش‌ها، نوع میوه و میزان…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/680815" target="_blank">📅 13:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680814">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117318c285.mp4?token=qdrcCz82iw-3MAi0o3vx0XHAuyQZXaCq9ACFuZLiP1D9EIFzPv9Wi01hJ1F2wLrHcQcPKd-avBbmDXyJnwrXGjVUQRzTXFnsmN-1trDNA_7Nhn6YKix-UNVbdoxTi4aq8osIFb7FVf5_CeJXaO3yc4vBFJfYJ8hUNVsRmZtRU7vRh3iwWlbGSsEu-Lh7q6M0s9h0_bChdwn84ERCkGSu4D9BZKc8r5-sSgtnCGm4t_vgU03zbpiNbAZn8QQ8II0yt9vtJRF5Ui30ASBM4jjxlWbRGewNwucas30ZsW6NKGYMAG-puXlD2FCDloouoHppswmlRLp5qQJwOstJ9SXEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117318c285.mp4?token=qdrcCz82iw-3MAi0o3vx0XHAuyQZXaCq9ACFuZLiP1D9EIFzPv9Wi01hJ1F2wLrHcQcPKd-avBbmDXyJnwrXGjVUQRzTXFnsmN-1trDNA_7Nhn6YKix-UNVbdoxTi4aq8osIFb7FVf5_CeJXaO3yc4vBFJfYJ8hUNVsRmZtRU7vRh3iwWlbGSsEu-Lh7q6M0s9h0_bChdwn84ERCkGSu4D9BZKc8r5-sSgtnCGm4t_vgU03zbpiNbAZn8QQ8II0yt9vtJRF5Ui30ASBM4jjxlWbRGewNwucas30ZsW6NKGYMAG-puXlD2FCDloouoHppswmlRLp5qQJwOstJ9SXEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کیفیت آموزش تا عدالت آموزشی؛ دو چالش اصلی آموزش و پرورش که روی زمین مانده
!/ تلویزیون اینترنتی مدار
این گفتگوی کامل و تحلیلی درباره آموزش و پرورش
را اینجا ببینید
👇
https://aparat.com/v/ayld6ud
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/680814" target="_blank">📅 13:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680813">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
گوشی اقتصادی هم از دسترس خارج شد
🔹
فاصله دستمزد و قیمت گوشی در ایران طی سال‌های اخیر به نقطه‌ای رسیده که حتی مدل‌های اقتصادی سامسونگ هم برای بسیاری از خانوارها دیگر واقعاً اقتصادی نیستند.
🔹
در سال ۱۴۰۰، گوشی A02 حدود ۸۳ درصد حقوق پایه قیمت داشت؛ اما در سال ۱۴۰۵، قیمت A07 به ۳۲.۴ میلیون تومان رسیده، در حالی که حداقل حقوق ۱۶.۶ میلیون تومان است؛ یعنی یک گوشی اقتصادی حالا تقریباً دو برابر کل حقوق ماهانه هزینه دارد.
🔹
یعنی در فاصله ۱۴۰۰ تا ۱۴۰۵، قیمت گوشی اقتصادی مورد اشاره حدود ۱۴.۷ برابر شده، در حالی که کف حقوق حدود ۶.۳ برابر رشد کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/680813" target="_blank">📅 13:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680812">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39451088de.mp4?token=oB73vQ09bvgftnRu7VT3zXYvsEMGGIIKBOg6fx84L1VcsMqxvj3Nf_RzMbVwdyvKEz4kg1aYMlTctix85KEM4wtl5EPXeR8gPdZ2b8GeNeH7dAXwIpudZOyIiSHKvYoLh2XIowirCD05V5l0EbFvD2uDey7aliXHBkUM00za64xp5jdPWOZWz9MZckXs5QnaRs9kiknWJwiuC2w-ZVUow_F5b336r6F6WcgPGuz9A7PM6P53G5LkQNC1ND23JjPVaxC9ep1okfmcynQTAN0xcDbbeaGWWZDgLgg0i8IBqhA4eUhS7pqzBOQnKUgSebK0AYqctU8If-bqQypOI40i6jQpsXgHP_USMYQiaQyifuOxKGfO8eXCBBSbCVpQBwFJGZikrRxAMibIptdP1NWA8jftFsUG83FoRQ7RBwyg6zC977Qhfm52aSFLK1lCj90tJoMgyf7rTyRcWTC80S4C_SKLUuhxSGgUaZ0GghkoGJk7AqedF0cSeZ0qqMW1R0PNgPpTVrN764jii1edDAc01ZLeG9KT8ce7Q12rRc6UWaaN1cUWQVJ6I2YS1nsjecj2mPvqXr8-G3Tl5IpGEsv6bpKzPIBSy3xad_rjrxf61WNYEo3YmNMTz31Ry5Nn6gq7Et6WIK439Bq1JWhf1HlsJciL_lDUAW6zRRE9axVSh7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39451088de.mp4?token=oB73vQ09bvgftnRu7VT3zXYvsEMGGIIKBOg6fx84L1VcsMqxvj3Nf_RzMbVwdyvKEz4kg1aYMlTctix85KEM4wtl5EPXeR8gPdZ2b8GeNeH7dAXwIpudZOyIiSHKvYoLh2XIowirCD05V5l0EbFvD2uDey7aliXHBkUM00za64xp5jdPWOZWz9MZckXs5QnaRs9kiknWJwiuC2w-ZVUow_F5b336r6F6WcgPGuz9A7PM6P53G5LkQNC1ND23JjPVaxC9ep1okfmcynQTAN0xcDbbeaGWWZDgLgg0i8IBqhA4eUhS7pqzBOQnKUgSebK0AYqctU8If-bqQypOI40i6jQpsXgHP_USMYQiaQyifuOxKGfO8eXCBBSbCVpQBwFJGZikrRxAMibIptdP1NWA8jftFsUG83FoRQ7RBwyg6zC977Qhfm52aSFLK1lCj90tJoMgyf7rTyRcWTC80S4C_SKLUuhxSGgUaZ0GghkoGJk7AqedF0cSeZ0qqMW1R0PNgPpTVrN764jii1edDAc01ZLeG9KT8ce7Q12rRc6UWaaN1cUWQVJ6I2YS1nsjecj2mPvqXr8-G3Tl5IpGEsv6bpKzPIBSy3xad_rjrxf61WNYEo3YmNMTz31Ry5Nn6gq7Et6WIK439Bq1JWhf1HlsJciL_lDUAW6zRRE9axVSh7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام ۲ هسته‌ عملیاتی گروهک تروریستی-تکفیری
وزارت اطلاعات:
🔹
۲ هسته‌ سازمان‌یافته وابسته به سرویس‌های جاسوسی دشمن آمریکایی-صهیونیستی هنگام ورود به کشور در شهرستان خاش شناسایی و متلاشی شدند.
🔹
در این عملیات، ۴ تروریست بازداشت و ۲ تروریست دیگر در درگیری با نیروهای حافظ امنیت به هلاکت رسیدند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/680812" target="_blank">📅 13:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680810">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a81e1bb14.mp4?token=FOmvzEt0PykwyzM9M1R4lKM1-CHSChI99VdPijM2WttSBt2R6quKxyBHoTkLEGWsCpKTAfdoybliTCSUImAm8rMdARcNHfJ4oav7us-FcXCFNBjfMphxFX-URY9c_isDxaBPCvAHSv_QJM-7nuWbW6d6mI4SFc4V3W21WarybIwQXeA5dPtr0HWraiHDykZmH8qu__dbTryEyhN9TBvYu7395pIQD-K6FXfjzqNppvxXCkmGKZfbS2gSBOTwH_hBuEbna45Eki01I1FXAh85GJfjU_S8FUFPYSZfggWXaqsHuIqtY9Hh9ightNbvI1FO_tFofMASj06s0pimHOfW1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a81e1bb14.mp4?token=FOmvzEt0PykwyzM9M1R4lKM1-CHSChI99VdPijM2WttSBt2R6quKxyBHoTkLEGWsCpKTAfdoybliTCSUImAm8rMdARcNHfJ4oav7us-FcXCFNBjfMphxFX-URY9c_isDxaBPCvAHSv_QJM-7nuWbW6d6mI4SFc4V3W21WarybIwQXeA5dPtr0HWraiHDykZmH8qu__dbTryEyhN9TBvYu7395pIQD-K6FXfjzqNppvxXCkmGKZfbS2gSBOTwH_hBuEbna45Eki01I1FXAh85GJfjU_S8FUFPYSZfggWXaqsHuIqtY9Hh9ightNbvI1FO_tFofMASj06s0pimHOfW1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ بهترین ماه زندگی…
‌
@Heyate_gharar</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/680810" target="_blank">📅 13:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680809">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔹
خبرهای متفاوت را هر روز در وبسایت خبرفوری کلیک کنید
🔹
🔹
ادعای آزادی میلیاردها دلار از دارایی های بلوکه شده ایران در امارات
👇
khabarfoori.com/fa/tiny/news-3237414
🔹
راز مرگ مارادونا فاش شد
👇
khabarfoori.com/fa/tiny/news-3237419
🔹
این صحنه عجیب هواداران سوپرجام را حیرت زده کرد/ عکس
👇
khabarfoori.com/fa/tiny/news-3237386
🔹
ازدواج چهارم خواننده مشهور در ۷۱ سالگی | عروس ۳۳ سال جوان‌تر است
👇
khabarfoori.com/fa/tiny/news-3237306
🔹
«چنگیز وثوقی» به خانه بازگشت
👇
khabarfoori.com/fa/tiny/news-3237397
🔹
برای مرور لحظه‌ای خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/680809" target="_blank">📅 13:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680806">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f319d54a1.mp4?token=fnuyY2hG6zY2ZVsxAixf5b80Vm_60omIbFygeV66yyqK3qLAFzaJ-d4X5l1_jedKM6_KRvXlAhhlGvRg83cjLdmOoiol7327TcznNqkLzHzVrV8AfmN0xEiVpfaAhFdtH_c2AFrUrCk8wu8PJXOHxmjUrQxSPkFx_RajNkto6rpp9ZhliAH4LgaOsakJS2D_DWQ68m5SAVBeg_uTGF3BrWIfNfHNwyape_0TFEzmFitPxero11xzmt3vrQ7ruC_et4x-fHObGf7KWDEwt80MicesTralIiiPrvJzpCWhD1TQKz5W6HpwdAG1L2gvidGpYhW1VgmMIfBlDrdQROKWNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f319d54a1.mp4?token=fnuyY2hG6zY2ZVsxAixf5b80Vm_60omIbFygeV66yyqK3qLAFzaJ-d4X5l1_jedKM6_KRvXlAhhlGvRg83cjLdmOoiol7327TcznNqkLzHzVrV8AfmN0xEiVpfaAhFdtH_c2AFrUrCk8wu8PJXOHxmjUrQxSPkFx_RajNkto6rpp9ZhliAH4LgaOsakJS2D_DWQ68m5SAVBeg_uTGF3BrWIfNfHNwyape_0TFEzmFitPxero11xzmt3vrQ7ruC_et4x-fHObGf7KWDEwt80MicesTralIiiPrvJzpCWhD1TQKz5W6HpwdAG1L2gvidGpYhW1VgmMIfBlDrdQROKWNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۹ سالگی دانشگاه را رها کرد و فیسبوک را تأسیس کرد؟ پس ماجرا به این سادگی‌ها نیست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/680806" target="_blank">📅 12:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680804">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
قیمت ارزی مسکن در تهران به ۱۳۰۰ دلار رسید
🔹
قیمت دلاری مسکن تهران در ماه‌های پساجنگ به حدود ۱۳۰۰ دلار در هر مترمربع رسیده است؛ سطحی که معادل دلار حدود ۲۲۰ هزار تومان در بازار ملک است.
🔹
اگر دلار به این محدوده برسد، مسکن همچنان ظرفیت رشد دارد؛ اما اگر دلار عقب بماند، رکود می‌تواند مهمان بعدی بازار ملک باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/680804" target="_blank">📅 12:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680801">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
توقف اجرای طرح عرضۀ بنزین با نرخ پالایشگاهی در کرمان  مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضۀ بنزین با نرخ آزاد پالایشگاهی در استان کرمان…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/680801" target="_blank">📅 12:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680800">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZz9v209agNHe3PCVw59Ek0t3waiuCag4kD5jwrzX0JYe9_uDHf7qhFFS6suH7nZrEUaymrPJSC77xsq7FgvdRwl5JdD2EAzvS-8pls1A27T3dzhzl1E7qT0ZgYH7YIPFlbdoJzr4_NTZYVShOG9LA95hQTuMi3r5rFYenJqOPSLItWhQhZtu71HYGQk3mzWaTIgGVtCIIgYZmsdkTaxl_k_Dc_ArbCkADVu3OgmREOBlFWWK8ZTiVXIcaE24VC2eLKpMfszU3HbJg7RTmUGcmAitKOvLh7XIjN882l1Homz6u2nPfzJlDaBt1Ze6mV2Hh11mlvv40NoyvOq17BWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه ۱۰۰ سال زلزله در ایران؛ کدام مناطق بیشتر لرزیده‌اند؟
🔹
نقشه زمین‌لرزه‌های ثبت‌شده در ایران طی یک قرن، از ۱۹۲۳ تا ۲۰۲۳، تصویری روشن از پراکندگی لرزه‌خیزی کشور ارائه می‌دهد.
🔹
بررسی این نقشه نشان می‌دهد بیشترین تمرکز زمین‌لرزه‌ها در امتداد زاگرس، البرز، مکران و خراسان قرار دارد. مناطقی که در امتداد گسل‌ها و رشته‌کوه‌های اصلی کشور واقع شده‌اند.
🔹
در مقابل، بخش‌های مرکزی و کویری ایران در این نقشه کم‌نورتر و آرام‌تر دیده می‌شوند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/680800" target="_blank">📅 12:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680798">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c3075fe50.mp4?token=uJw7Xwayccoma-u8eBN8HnYFVVaWjjsEkvv08Hh8XNPnscgBwiFVF21VoEQCcJiLmbM_R0GZTbAsOSXtOqr326RNU1_PX1KPRPB5dDZktkEvyIQWZ5s_PKHSmKdMF4ZOgX2qBtp_H9-Fyp7rchFk3V6SztnsbOTIBj2HVcAexrc768VhYo-PL1S6baXLL8YDfg4Sm-Z2dYuWyUAK0wFgwqpF1rdmg50raG1BKPxRM0cUsaVZhK9okTjEymfVkkucDAa5xV6DIk0TPMwk95G1ludrJN8J3I0G2cUuQJaulPLS6p8szWQIVMz5GnSklyWCJzygMyUSxHakcpmQujZigoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c3075fe50.mp4?token=uJw7Xwayccoma-u8eBN8HnYFVVaWjjsEkvv08Hh8XNPnscgBwiFVF21VoEQCcJiLmbM_R0GZTbAsOSXtOqr326RNU1_PX1KPRPB5dDZktkEvyIQWZ5s_PKHSmKdMF4ZOgX2qBtp_H9-Fyp7rchFk3V6SztnsbOTIBj2HVcAexrc768VhYo-PL1S6baXLL8YDfg4Sm-Z2dYuWyUAK0wFgwqpF1rdmg50raG1BKPxRM0cUsaVZhK9okTjEymfVkkucDAa5xV6DIk0TPMwk95G1ludrJN8J3I0G2cUuQJaulPLS6p8szWQIVMz5GnSklyWCJzygMyUSxHakcpmQujZigoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جغد عقابی با وجود ابهت و قدرت شکارچی‌بودنش، عاشق نوازش و محبت است و گاهی در آغوش انسان‌ها آرام می‌گیرد؛ ترکیبی عجیب از قدرت و لطافت
🦉
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/680798" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
