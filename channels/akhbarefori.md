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
<img src="https://cdn4.telesco.pe/file/RRTaupuqDauoWbi9cfF3SbNaVVYm6TlIOdDsjHS4YI-ONRs3ioEeO4ZAisRTHCMpM-JUZ-RClLNoqXFjNF2dGWXjpNc3KTaKBRFSfWggJFlfrgRy6dM81fbfcfeZXrs4PzKQC9qpJx5nF7Tlm8pKXBfW-wttNP_x8hSUcc9-QLxP9YQWT9i8Q7A0tVmXGhoZE1w67xDKGEA498wGbQ7jzHQ-Wr2lL2p3H7yQNk2wj4RRJrXUrVs6h-bR2zA8s7PHZHLP4GFz1LpzMmDNorTU9LsInhWSSsCwpElx-Sq56kZUe3yVie2fpcmKqlU4-jiXGpM2TpBC6Npmq5_RP51_TA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 02:54:57</div>
<hr>

<div class="tg-post" id="msg-673234">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
صدای انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار در تبریز به گوش رسید، هنوز هیچ جزییاتی مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/673234" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673233">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای سنتکام: از ساعت ۷ عصر امروز به وقت شرق آمریکا (ET)، برای نهمین شب پیاپی موج جدیدی از حملات علیه ایران را آغاز کرده است./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/673233" target="_blank">📅 02:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673232">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f0d26c63.mp4?token=qA76QjU55SSwE1tgXgWYdsdZTn0Co-BcJN6gV3yVeFVhKSmG2APSQbarLmURXK4NbQ37lag5vVqLT6KL-050Q6tlVDSAg37LlgydkkIddXNbU-upxQlo8ZALDEXhjFpyCwF3GHAx4SOqBRmyZbdJNtI6-qNCxdDm1nPUDdZhDmVJwONilZI8JVGCeZc6aJyUqtuy8NXexjzJrVAdk0VumFosjpuSHYY1ewLHW7ZznF-grUVmNzybU7Rw_sYYQuB4m9L6OVD5Osp-GPlxBl3-hICZTHkMutapMmdWweRU9etG6aPaSfG8ExGahlGpLBR3-bFn7Ls9pp6_8WLJl51e1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f0d26c63.mp4?token=qA76QjU55SSwE1tgXgWYdsdZTn0Co-BcJN6gV3yVeFVhKSmG2APSQbarLmURXK4NbQ37lag5vVqLT6KL-050Q6tlVDSAg37LlgydkkIddXNbU-upxQlo8ZALDEXhjFpyCwF3GHAx4SOqBRmyZbdJNtI6-qNCxdDm1nPUDdZhDmVJwONilZI8JVGCeZc6aJyUqtuy8NXexjzJrVAdk0VumFosjpuSHYY1ewLHW7ZznF-grUVmNzybU7Rw_sYYQuB4m9L6OVD5Osp-GPlxBl3-hICZTHkMutapMmdWweRU9etG6aPaSfG8ExGahlGpLBR3-bFn7Ls9pp6_8WLJl51e1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون مقرهای تروریست‌ها تحت حملات شدید ایران
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/673232" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673230">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLNmTUVkfjVA5sur3frCwb9VppNZ0rDZrlhCpZ6lM6cn0N_edpto1cR2Yye7zJVwtJWultKRBMpIJ30iu6wGNTRjuwUqfpi0NIVWBV5ni6bu4mWsKnTxgpQvI1pSkK8U_dbfO0S3MxleGxMuEpgfnD5-fCVLiz5TASnYjeLwdoXf1rvDYUoK8ywE59zcUJ_BTuc0wNeY_boHGUTSYWybtadcgp_uDRoGY4_cFoLZRoMHXGgEMU1pupTfoFO1W9NfMzidu5ldgCkf2peQn_H2BwbYFwxLI1bmyg5Nb9zEIr35jzusfTF9KKgmKPRfY4injqIph9kbSIxYhQ3a5p-ptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-T0UgpED3zYEOWJ4jeF540GD8l94T1ONStQ6vY7WN3L5NO73SEdNN8GjTNA1z6A6HMdetrcSBVzxGgv0yAyrrqRgBsI8LhVmXbWxGFZiw1PW5_2YBJ0VVTFo48WZ7SzNf987GNhXG7AM4-bdLBsalFLUosy4awjXMtye2bY_5MhYeGu7DDZQmOI9D_CB5AGNPCuwa6rnbFC8Z4uoDznvYiyfhBlg0vGAyNj34Bsm9ccAUpyJNDyvvYFjaAxHOc6-IF9zZXEkLqog5ZLniCErm8QO20HPj_3zY61NC7LVd21ALnm5ch7j1n-UVyjWMmVbx4RPqZERTrNXpaCgLG6bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چشم‌های یامال احساس تنفر نسبت به ترامپ کودک‌کش را فریاد می‌زنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/673230" target="_blank">📅 02:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673229">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cdc7cef56.mp4?token=YAM_xG6gg1_O-BF4v6mvLwdooyQPk5ultOf6knKTBbQyLKnVnUieockMF-b1_c3eYaxB5E-p53GzUGwM9SvZ4_7zFmwViCjtPAWAQTGl9VhELbH7uCSH2N_Jiu1advtMPDLoqLjKzrT1609oRfgPRHCsQnWDEAeUZSoVKChZbaZv3YuZ8i-y5_PI0QTqd5bdfrGeD6IkkgLozijtAKItYm-3yS8QeN3hrVWWdXJ9Ux_rc0IEn7DHbC8me06i7akOn28TmLbQZaZSP721sv2mNNeFcmLZx79m0WKRU_DSmq937S9hCRPXleaxaP0P0sT3e-zHb1rgawnm8u5GLBNaTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cdc7cef56.mp4?token=YAM_xG6gg1_O-BF4v6mvLwdooyQPk5ultOf6knKTBbQyLKnVnUieockMF-b1_c3eYaxB5E-p53GzUGwM9SvZ4_7zFmwViCjtPAWAQTGl9VhELbH7uCSH2N_Jiu1advtMPDLoqLjKzrT1609oRfgPRHCsQnWDEAeUZSoVKChZbaZv3YuZ8i-y5_PI0QTqd5bdfrGeD6IkkgLozijtAKItYm-3yS8QeN3hrVWWdXJ9Ux_rc0IEn7DHbC8me06i7akOn28TmLbQZaZSP721sv2mNNeFcmLZx79m0WKRU_DSmq937S9hCRPXleaxaP0P0sT3e-zHb1rgawnm8u5GLBNaTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن در ضاحیه بیروت در پی قهرمانی اسپانیا و شکست آرژانتین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/673229" target="_blank">📅 02:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673228">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3bc53ff5.mp4?token=WLMCR776wHEusVC5ZAzlc0No_5j__pMkyBBAAFxBViBJ4K-Z-HWduIanqTcZYuYUgGFtrIPJOEn0dqUX_FLfYlr3L0uSrG02cb5k3Vlwc_apRhLx-Q2YgtdexgXOTxnbn7EcbNAL0J2vGV6R3s-tkZTZrcgvTOp7hEIMcM1BNIhw0Cm30hdrpatvwwB1lHe4s2qBj_Egk3LMWJl-WOH9gu3rECoowKe0hlKCfZ12kKO1DN5QufzPr_bM1Ktt2fjC26i-W3zlECYMPXiJpXRCPSbs99ciBUex2vAHLsQJdf4MBJqnFEH-ywD3uywDnfwM4lXwWZshSH4FX3uZ5Q9uzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3bc53ff5.mp4?token=WLMCR776wHEusVC5ZAzlc0No_5j__pMkyBBAAFxBViBJ4K-Z-HWduIanqTcZYuYUgGFtrIPJOEn0dqUX_FLfYlr3L0uSrG02cb5k3Vlwc_apRhLx-Q2YgtdexgXOTxnbn7EcbNAL0J2vGV6R3s-tkZTZrcgvTOp7hEIMcM1BNIhw0Cm30hdrpatvwwB1lHe4s2qBj_Egk3LMWJl-WOH9gu3rECoowKe0hlKCfZ12kKO1DN5QufzPr_bM1Ktt2fjC26i-W3zlECYMPXiJpXRCPSbs99ciBUex2vAHLsQJdf4MBJqnFEH-ywD3uywDnfwM4lXwWZshSH4FX3uZ5Q9uzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غزه درطول جام جهانی طرفدار اسپانیا بود ، همان طور که اسپانیا حامی فلسطین بود و معترض سرسخت به جنایات اسراییل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/673228" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
واکنش حماس به قهرمانی اسپانیا
باسم نعيم عضو دفتر سیاسی جنبش حماس:
🔹
ما پیروزی شایسته اسپانیا در جام جهانی فوتبال را تبریک می‌گوییم، این شادی را به فلسطین و حامیان آن هم تبریک می‌گوییم. «حتی اگر تنها فایده این پیروزی، آزار صهیونیست‌ها و همدستانشان باشد، همین کافی است.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/673226" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjDJZWxeqsqr6qTSdXAtk3MNifjIjc0nxoLEvXrUsLe4eYbQb8yUhQ0vl-BrlFKj16Q051gVUr4p4lUJuBw1ecQhedOnOi3tyixBtdnBVuHrGEcldoPbdNy81-uCs32OjKSMBtqKSbNgsAwB949UQmdV1F_aoKlPd4iaQ2xFfSYvpjO-FYiflE5ydvjVVmrmF-nBs9Q8Xy6TvboqyuaqvECQXYZTTfJWHrNrK7IlCCW_xYD-3t3wjUFEQ0sPeP6jikZhmdyB-udSjRClY3Pj9Iow9W1RgMx4gPYFTN4Rwh1SL_RFbXTEUezPUYH41gXUR_rbGeR4QDYNaQ91TpE7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
طرح علاء اللقطه هنرمند فلسطینی به مناسبت قهرمانی تیم فوتبال اسپانیا در جام جهانی
۲٠۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/673225" target="_blank">📅 02:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673224">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
اخبار اولیه برخی منابع، از هدف قرار گرفتن گروهی از تروریست‌های آمریکایی با حملۀ موشکی حکایت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/673224" target="_blank">📅 02:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673223">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1QIkqWdTBgkFTr-D50BG4ykEe1ujPrJfiLWhwBuhhbP-4btHS-a782kDAOOU33yB43X5ImPPm4TKjqncUZHQaG5pDxbtXNq2biEfwpE0UVsMsRjoKpSJ12nYa3HKXc6Ba1TBYR73l6R1A1PQi1bREXdaCIxeh8tAw5GUZKbA3HmsppM-UIjXPuvwUfmTKuImK5_nqPqW2q_Hsm2cTluCu073HSc_OFuV1ie8VcPphjq3CBdkTMZ-4U8hP6Pat8XZo2G3wE1NqbXHhwxrCy0-QOjnjlGEclMH4ptjt8s4KF2uJUbD3CT7x3lrle4gKACdMsIH8-lLeH4jWB0BQVAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کیلیان امباپه با ١٠ گل
،
کفش طلای جام جهانی ۲۰۲۶ رو به دست آورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/673223" target="_blank">📅 02:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارها این بار در سلیمانیه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/673222" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673221">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
منابع خبری: انفجارهایی پایگاه‌های اشغالگران آمریکایی در بحرین را به لرزه درآورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/673221" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673220">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702f41e938.mp4?token=LiLnHioXbC5n8o2_UcTDznADbppioLVSzT-_Y8WSHW01AI6rPTpOlR3zi04Fais_YHYroHX395m6GskIVtyx0K8YvFH3K2waL9Nel1AVVHAPPl5fChLVfdIUy_iM2edLszEJy9PV70HfzW1pANtsd-qxEWSnfP2432Ne_63Z3xsPG8XtKPD7xhwoNJbgVeE1lHfVuVDaY7Pl9X69lofGZnyvB96I5b2fEGtzF-nFr2Wo0kw4RZylwyy0kHTaUcylvl1qw9D0-M_9pxoQ7Idg9QkPZoPGX_KqrGRPt0Pnxl2GEJqHS9F7ydNstJdHIBSogYlEtO1i0-AVbkX2hGlxmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702f41e938.mp4?token=LiLnHioXbC5n8o2_UcTDznADbppioLVSzT-_Y8WSHW01AI6rPTpOlR3zi04Fais_YHYroHX395m6GskIVtyx0K8YvFH3K2waL9Nel1AVVHAPPl5fChLVfdIUy_iM2edLszEJy9PV70HfzW1pANtsd-qxEWSnfP2432Ne_63Z3xsPG8XtKPD7xhwoNJbgVeE1lHfVuVDaY7Pl9X69lofGZnyvB96I5b2fEGtzF-nFr2Wo0kw4RZylwyy0kHTaUcylvl1qw9D0-M_9pxoQ7Idg9QkPZoPGX_KqrGRPt0Pnxl2GEJqHS9F7ydNstJdHIBSogYlEtO1i0-AVbkX2hGlxmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه بالا بردن جام قهرمانی توسط رودری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/673220" target="_blank">📅 02:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3323f025d2.mp4?token=Zc01yGzMD4hlqplgMJRRlh6aY-zA_r8m5gIcEBhyrxoqCGOojG4Ote7y-0GsBrJ3_TkSn7HBzAMSPjd0N5U05ur2ZjeH_K-egmCk1MrQKlIO4UcJ6GkpcLZ2obj6rpLmzMHO3llqVaMKCL0CnzieOq7cvv0I-I_IY5RI-g2dac4ujNSfXrgxm0ZrW55-5a-Y3TSPIyZy5QAIhAvfNmXsKsW2vLu6K2YtDDTBPhByGfOJQPhYyxM3TyJFJ-fRDX_BMtAG1OF7p-ceLNZhRIGAvptfsRO67yLFz01FHTDFN2WcX1KeV7g6-ELeO57K0DzMzGUlaQcb8Qdj0WNvXV9S6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3323f025d2.mp4?token=Zc01yGzMD4hlqplgMJRRlh6aY-zA_r8m5gIcEBhyrxoqCGOojG4Ote7y-0GsBrJ3_TkSn7HBzAMSPjd0N5U05ur2ZjeH_K-egmCk1MrQKlIO4UcJ6GkpcLZ2obj6rpLmzMHO3llqVaMKCL0CnzieOq7cvv0I-I_IY5RI-g2dac4ujNSfXrgxm0ZrW55-5a-Y3TSPIyZy5QAIhAvfNmXsKsW2vLu6K2YtDDTBPhByGfOJQPhYyxM3TyJFJ-fRDX_BMtAG1OF7p-ceLNZhRIGAvptfsRO67yLFz01FHTDFN2WcX1KeV7g6-ELeO57K0DzMzGUlaQcb8Qdj0WNvXV9S6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اعضای تیم ملی اسپانیا مدال طلای جام جهانی را دریافت کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/673219" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe7c33843.mp4?token=amhhQ7WD-8s7Zz8L0_bB6C4Vnxc-CFttw54SnVt9RaJ5yrp4SXYbp7SHtrIimmqH2xEzkXfLDUwTsjR1Fe8VqXyqBrqblbDX9rFMENOR8REZmkNxbB1Yz5ZWpUoYDLkMCLKBJ7cADLJOz_zoN1lopSucd8lWsrlmXgpg14YnjetFG2my8R1ZuqZBDVMgFUAdbAn4XlApNFZGgIzPilhk2WIt2klF9yCxyd4gaQQzi1Y-p9H5ZG1vw_dT05booKp7rdD7JM1fXXx5TmAnkxgtI-ijhC2GSpxGdFtlMInQHMg109Ff4AjUmuWkJk0h9SMcVol9IkE5cevFAO-qD7WW6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe7c33843.mp4?token=amhhQ7WD-8s7Zz8L0_bB6C4Vnxc-CFttw54SnVt9RaJ5yrp4SXYbp7SHtrIimmqH2xEzkXfLDUwTsjR1Fe8VqXyqBrqblbDX9rFMENOR8REZmkNxbB1Yz5ZWpUoYDLkMCLKBJ7cADLJOz_zoN1lopSucd8lWsrlmXgpg14YnjetFG2my8R1ZuqZBDVMgFUAdbAn4XlApNFZGgIzPilhk2WIt2klF9yCxyd4gaQQzi1Y-p9H5ZG1vw_dT05booKp7rdD7JM1fXXx5TmAnkxgtI-ijhC2GSpxGdFtlMInQHMg109Ff4AjUmuWkJk0h9SMcVol9IkE5cevFAO-qD7WW6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رودری بهترین بازیکن جام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/673218" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc20bd9e05.mp4?token=b9rbSx-HKNzBBe1Cn4UNquG0mdEY6nXp4qcsa_Y-aitu6yTsXpDPb2yXCMxq1odBRDqO1Rm0iIDiwcPE3_qyKCYApw2MK-9ChYMfxUGG0lPJHGF-s-xJEXgDqxAeQ6wPrVPeHsvrwjDerUEX7KZZZqOGEIPgJHX7Mtohxf1dYymHQ3_vvXnMlaIePnagNgxTKGLAQUdbGSnDcWh437AKI9VqUOxljFQERlP-MYiCeaT3X8UhHX3C_PRIioNkEfw-DSNAO8xGucxWKM-V3UpI7i5CigBBCW-71RkUtSuAYQHHF1CBVHRgt440Syso55FNiQKlv5dwgxyB5KPvU4JFJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc20bd9e05.mp4?token=b9rbSx-HKNzBBe1Cn4UNquG0mdEY6nXp4qcsa_Y-aitu6yTsXpDPb2yXCMxq1odBRDqO1Rm0iIDiwcPE3_qyKCYApw2MK-9ChYMfxUGG0lPJHGF-s-xJEXgDqxAeQ6wPrVPeHsvrwjDerUEX7KZZZqOGEIPgJHX7Mtohxf1dYymHQ3_vvXnMlaIePnagNgxTKGLAQUdbGSnDcWh437AKI9VqUOxljFQERlP-MYiCeaT3X8UhHX3C_PRIioNkEfw-DSNAO8xGucxWKM-V3UpI7i5CigBBCW-71RkUtSuAYQHHF1CBVHRgt440Syso55FNiQKlv5dwgxyB5KPvU4JFJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مسی مدال نقره جام جهانی ۲٠۲۶ را گرفت و گریه کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/673217" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caeeP_BM-5sZ3ztxsYI2uGG0chWcdl9FwG9MPNQr6INF5nGtFUUAmSHIMECHmF4aWma5u8l5BpHK9cirQBGk4Dq_2UpLvOizyo_5-XyapTLA-ygelU6PHHDdHVV3YXjyRZ7vhjcSjdrUKFyIWFYkVgqF0uhsVdsQyTYp1FXmCZOp4B5ozldMIWVydH0UmW8Fuo6EGLYmWjCfU7CJp4LAPx5JBX8bT5zJFcc141vzO5lAelEMNbNvcR_0g7R269NIY4JnqlS0c4sPbtK2LpeV4WyWF-K9df6dOSSgzKIAKOB8Szhhv4wXPwL_xEHKuKIuSwLKEm7lO-WXJmYVeqEOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سیمون بهترین دروازه‌بان جام جهانی شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/673215" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmPSnDVifFKcYRNT2sMSAjkJ7bJaCEx1RcazPGKb1TaOGIrCLpv4DrIoPNVtrCFpKOp552yEj21mPNCDTkyctZPhIMS69hREyMfTSjUSn1Wlp8loJl61SfHwCfd7CWsZ2aXGhvJr9-MLLi28caG3Rf2gx32V7EYh7XMU_s4IBpglsNcibrtg4ormKtSJO5Vd38Aa7EKMBGvIO14MsC64eBBDnw0oPgMeqcHDSq1_ViE1mrn2Yjmvjv17T0xmRUSSr4jcC1bH1jaIqc8HD85UIvePBvKY-iCx54zuEW3soe8wNtVPvUQICtQh20FLwWFOyKWrlkD1ZYMSXWNEG9yong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کوبارسی بهترین بازیکن جوان جام جهانی شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/673214" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در قصاص خون سربازان شهید ایرانشهر
🔹
سپاه پاسدران انقلاب اسلامی در نوزدهمین اطلاعیه خود از حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهرخبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/673213" target="_blank">📅 02:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=Yf6MvUTUWcNUT3aYpB7wGK2D2imqCCr40OLdwCXSlsFjGbP1KVkctRy-8bLM2Lfu2uBoUtP5s4up0j3jbfxQp_gUjbVyNcbNYOYTxCmssgcil7taU50JeOjGT91E8Q-Q4ze30XCSprlF8g-WnUsI4Jq7Mr3xp2xY9YmtCm1mq1TQE8fFjQjKEyKnsFoioemqKcjEUXeKorcyXDU4TvynMZG4G8k5nhqKEJ5_JKYk8bLEso2tOBR4UWbIg-uIoSvBBEGrivrad9Do_jDZ-vsU76bYVRT6a-GURhJeM-o3UlozDnev7HF3-VeJ-aj7Bz3TcZ5fDR89l7WqAi4eR9BE3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=Yf6MvUTUWcNUT3aYpB7wGK2D2imqCCr40OLdwCXSlsFjGbP1KVkctRy-8bLM2Lfu2uBoUtP5s4up0j3jbfxQp_gUjbVyNcbNYOYTxCmssgcil7taU50JeOjGT91E8Q-Q4ze30XCSprlF8g-WnUsI4Jq7Mr3xp2xY9YmtCm1mq1TQE8fFjQjKEyKnsFoioemqKcjEUXeKorcyXDU4TvynMZG4G8k5nhqKEJ5_JKYk8bLEso2tOBR4UWbIg-uIoSvBBEGrivrad9Do_jDZ-vsU76bYVRT6a-GURhJeM-o3UlozDnev7HF3-VeJ-aj7Bz3TcZ5fDR89l7WqAi4eR9BE3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک هار به منظور اهدای جام قهرمانی به تیم ملی اسپانیا وارد زمین مسابقه شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/673212" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNecl-YMdpE6D0M_2kZ74U9M6HksQHzSEV0XxPut6BKlScG8I9yxxAkowENlMgHo-nOvFUR3PeFSCBxrbuDja5ai20JnAVEZ065Sn6Xd619R5l9I7P3ZsTZ_GsUYBw6Wc8j8yBt2d2wBE8OP9wBm4QInieT_jvr-6BNZXrwSM64Ko2XYX6UcvLP-4Gfts9lYWDUVLCnBWhD-2LADe72FZpF-61s4j2lj-akoG9SpF87ss-yG3OZdsvf9oeUpb1Ia8Vz2MV4TZ-aM1ZFQ7MyX2A6HEJqZSjXqFcR_r2UqQJqgRIIN0qJXSLrh_fe5iMVuOwqO3hnatsFed0TenF5BJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپانیا به جمع دو ستاره‌ها پیوست
🔹
با پیروزی ۱ بر ۰ مقابل آرژانتین در فینال، اسپانیا برای دومین بار در تاریخ خود قهرمان جام جهانی شد و پس از قهرمانی سال ۲۰۱۰، دومین ستاره را بر پیراهن خود نشاند.
🔹
پس از این قهرمانی، جدول پرافتخارترین تیم‌های تاریخ جام جهانی به این شکل است:
برزیل: ۵ قهرمانی
ایتالیا: ۴ قهرمانی
آلمان: ۴ قهرمانی
آرژانتین: ۳ قهرمانی
اسپانیا: ۲ قهرمانی
اروگوئه: ۲ قهرمانی
فرانسه: ۲ قهرمانی
انگلستان: ۱ قهرمانی
🔹
این قهرمانی، اسپانیا را در کنار اروگوئه و فرانسه به جمع تیم‌های دو قهرمانی جام جهانی رساند و فاصله این تیم با آرژانتین را به یک عنوان کاهش داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/673211" target="_blank">📅 02:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
برخی منابع از شنیده‌شدن صدای انفجارهایی در کویت خبر می‌دهند
🔹
وزارت کشور بحرین: آژیرهای هشدار در سراسر کشور فعال شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/673210" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3VBEQ5IxkLsa-3GbieF5DnppMig5JKPt7-reSXcVtT4CikgoHETgiN1wi-cae9AkHkPydsJrIOwA-AFu5PFu2MsowWGSg332l4BiXfxCmQRAP67nWBqA6KkJpiM6i3ejNJu1xIyoPmtF1wa2wCf0sZkwJ6sSFuXwLnFW98z1Vj8sbZ_Z8iKwnkVwSHV1BuJbiPQxijW7-8pJr-cDMhpt_mI-ed6L-xC4duoQLWzGOfdvFYtIcXMMj2GJPSVnatYM1axX86M_XgI5VcvCTdzZ2EoRI6u440BNeG5TFI8iEMH-srW6oDvUwGXrL1SZyLpcwuqTstrwkmN6L_DbgxTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به بالای ۹۰ دلار رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/673209" target="_blank">📅 02:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673208">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ارتش تروریست آمریکا همچنان مدعی تعرض به کشتی‌ها
سازمان تروریستی ستاد فرماندهی مرکزی ایالات متحده مدعی شد:
🔹
نیروهای ما به اجرای محاصره دریایی اعمال شده علیه ایران ادامه می‌دهند.
🔹
ما مسیر ۶ کشتی را تغییر دادیم و یک کشتی را تا ۱۹ ژوئیه غیرفعال کردیم تا از رعایت کامل محاصره اطمینان حاصل کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/673208" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcebb879a.mp4?token=B0_JDSdQwxDODUZ4Z6M4IzUjNUZMtCafiQEoMVT-hHCkug-QrKVxP_Xsmy_f4nWl2t1GXha5ORgd8_qg9YvgivDURTcvlgQGpLQb81enNkw2xeAp85DobH707JWJPOGDWqLIgDpBmgUeMbNeUq69WlUIGpBKh-r6g-WSg1VNGz4lbuHVwjTsoTDpfxGbaZvvd20nITIimobvlqB4yc17DtvZCBaaLDmjuDRi7pvdR237OI0u6FbLaViC45Jyd7LRnrezxcJchYzx9KcDJ6JvE36Uxwsle9LQdPFkwsUROkwDndcX7hLGy_VAxJkj-4nO7PNfhiUFDtrsXVfwbHTZ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcebb879a.mp4?token=B0_JDSdQwxDODUZ4Z6M4IzUjNUZMtCafiQEoMVT-hHCkug-QrKVxP_Xsmy_f4nWl2t1GXha5ORgd8_qg9YvgivDURTcvlgQGpLQb81enNkw2xeAp85DobH707JWJPOGDWqLIgDpBmgUeMbNeUq69WlUIGpBKh-r6g-WSg1VNGz4lbuHVwjTsoTDpfxGbaZvvd20nITIimobvlqB4yc17DtvZCBaaLDmjuDRi7pvdR237OI0u6FbLaViC45Jyd7LRnrezxcJchYzx9KcDJ6JvE36Uxwsle9LQdPFkwsUROkwDndcX7hLGy_VAxJkj-4nO7PNfhiUFDtrsXVfwbHTZ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دست در دست هم، با مهر، خرد و غیرت از ایران پاسداری می‌کنیم؛ ایران تنها یک سرزمین نیست، سرنوشت مشترک همه ماست #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/673206" target="_blank">📅 01:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaYdBPCrmzZ8f9TM3tvfHqmhk4edMhr1Ny5gQ_u7ItGkvGzt0umDo5U7tKdw4-qOCM5b8pxubKlvLnQWLsGlJBeP4bvukn1_4cjpLp8Yuna71QaXzPgwy9r8BQzKT51RNRFicS3eg_ssFI7D-SKv6xX1cYpD3f9QYO0JPGnbkhYbbEb9AGnOGUELLtx6leiEoKRGZCzNQyFZzjQXawrp4YDPf8U14XapJ6VH82el6Xjzw3-Yb8w_Z82zA1MHihtWSDV8K6ytU5aJDZpA4CVXzBd02J9jjVOwpeMUuOZCAS4JLFebfY9pCC5ve_WU25jnYriUhPgZaP9_gJhcdqNBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لامین یامال و نسل جدید اسپانیا نقش مهمی در قهرمانی داشتند و پس از پایان بازی، تصویری از در آغوش گرفتن مسی و یامال منتشر شد که مورد توجه رسانه‌ها قرار گرفت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/673205" target="_blank">📅 01:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
برخی منابع از شنیده‌شدن صدای انفجارهایی در کویت خبر می‌دهند
🔹
وزارت کشور بحرین: آژیرهای هشدار در سراسر کشور فعال شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/673204" target="_blank">📅 01:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_sSrmpb8MkpKwkGQoEIfpVBI3uGrD8kd8eLNhay_yg8gjWcK_aOWRfVaTEheGJgjwZfj0rA4mRoGBzzwrxKBHT9K6ySqPqivrH-BCqsGY6WWS5Roj_A5arwg_X-__4QOPHd471azSdDY7B6riO6-fKEXMuu74DktYzpbfsgM3av2GO9NIeJ62eeWaPaT1UsNuPYX1_i9GKX9dDAysHCu7keEBYvlhM7Jws9sdqJCzrfSenctWtjX7zrMJSGSGKxNm5yanNdgwZBVfB6kE3K3n1TN4loGgTusSkuGYpTjOBeTidh0IKWNJZgLGgsfr7op_1Ec0wPN9ZPSeYl5WNyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردداران قهرمانی در جام جهانی؛ اسپانیا به جمع فرانسه و اروگوئه ۲ ستاره ملحق شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/673203" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673202">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF6a1UvOhZKHwole1NGinpTKXF1rbKxor8dZOS9XRCNDj683VU0r8H1GUqWAVBSpDv8eo_7qqkWQpKIpq-14qNIEutZP-x8ShY9Rt8Oid8vw0P54WsVpH9JHvo1RwJYAIXO-7SskvlivKPDLK6QNHx5aO5xrW5IWwnE44Qx08zXmuEcd8CV8ZuFIiUswqHp-qmoNW7h4UlyczbROHlbvpP-FgZYFUfLV9MTJf-UNXzo1JY97cmFsv2IQI3w3xDrs8gZegad4iGcc49Ao7yM836pgqWOa7AH_I71OkG1M1PIqqPdERqcjL6_V7Wy3hpKVMD5FB08kBThCr6yEKyPQtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲٠۲۶ هم با همه خنده‌ها و گریه‌ها تموم شد
🇪🇸
قهرمان: اسپانیا
🇦🇷
نایب قهرمان: آرژانتین
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقام سومی: انگلیس
🇫🇷
آقای گل: امباپه
🇫🇷
آقای پاس‌گل: اولیسه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/673202" target="_blank">📅 01:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673201">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXQudn77JdUEVpjbQZLUr64b1LCIzfAxQDe22_JDrRvQz6A8HiUJtPjqZpZ0-_73V2Kc7vLl69q6lysuzp-LWUxAi2bXJPIc4UVZw9v6xuxFYrAtTYMrwTYrItIDy4KqUtp8jHjFnL7OFnzKJhRyJppYAyesBXJY6bdo3x-LgskzxH2G7Ijt_Q_l98ZrAhL2MPT7Mek40kPlylb7_Acz8GcqgrFWfDbU1--WkE3Itk_XJ1y1cKCBJ9HPoCPrlbkVg1Vslpaqz_l0qG2kaefnsxUtL_B3_2mG8TJkjbu0aP8LQCVrYxM_GZ_jjkS3n9oy9LOsIosohIyqzIua6_MtOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا برای قهرمانی اسپانیا در جام جهانی ۲
٠۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/673201" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673200">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWSyhKc5qjDafQrBeEGsSL2droSrPX4O1Mdgy2Wwzo1bMjl7TQriOnBaRSpYrcyZxp5O_glBM61cJlM8WTPmoYHLaHHHb8a6eR2VlexQ3TW0j_-bGFV5tJp0SrVe-T_N0gWgJCAfovSYsi5kJnrHpS61eTABDlRA_12Pxxi5ibIsltafi71eLnbkDv1ma9Ksp3VPAcl6iARs11gbHWDWepummYUr1cGK8wLwUHhFYeNgdDaCpKImK-rLK0dxtJ3Tmp8TptxCPIC1fODAlJ4FW3dQDysGhWMHcu1AGi1tIZ9M2rul9nuKMzNgthbISFVlSCDEJPREFC44Dmuq4hmCPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ماتادورها قهرمان جام‌جهانی ۲۰۲۶ شدند
اسپانیا با شایستگی برای دومین‌بار قهرمان جام جهانی شد
🇦🇷
0️⃣
🏆
1️⃣
🇪🇸
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/673200" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673198">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5911d00df6.mp4?token=ZV46WbXrB0SqPVdGuTtjbLJ--YQkPcy1lPv3HWquden6cQpITnvHfG1I2Rz1_6G70-XUquzlaWwcc1WbC0D0gzn8f4YECvcZ1AKoa9uGx84NYf6PwLO4xDyRMxwZYHYMq09Sz3rBF0bcYkaN-nh1-OAWcf2dSf-Ui-rhNbUX1urp2peHGhpmG04rIVVgwUWHJvycZCcsDnlaUyxzywfV528NqZ-BvxOam6v4u3oQPDnp8O4HwF9ONfQZ9avjDbLBPZolzWoFbY4dTUAe7wAXBwoIvbXdtd7QBKUFQuR-BnzDUfGwYvGRRcLewcb5WT7xQIcAJWMf54TSoX0oKe3fUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5911d00df6.mp4?token=ZV46WbXrB0SqPVdGuTtjbLJ--YQkPcy1lPv3HWquden6cQpITnvHfG1I2Rz1_6G70-XUquzlaWwcc1WbC0D0gzn8f4YECvcZ1AKoa9uGx84NYf6PwLO4xDyRMxwZYHYMq09Sz3rBF0bcYkaN-nh1-OAWcf2dSf-Ui-rhNbUX1urp2peHGhpmG04rIVVgwUWHJvycZCcsDnlaUyxzywfV528NqZ-BvxOam6v4u3oQPDnp8O4HwF9ONfQZ9avjDbLBPZolzWoFbY4dTUAe7wAXBwoIvbXdtd7QBKUFQuR-BnzDUfGwYvGRRcLewcb5WT7xQIcAJWMf54TSoX0oKe3fUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسرت و افسوس مسی بعد از گل اسپانیا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/673198" target="_blank">📅 01:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673197">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab996676b.mp4?token=mQ798ShwerRbLGeUxnBRVhCR2O2Q1cAtejAA8XEWY5CNNO8LGPRWGuOp_-hiWBUTJCcUaYjGS9HmdZU5v54GiHZgI0Y8R0y0_YwzCRePmWaMzDRMTrajRVn1YDrM6WI8jQ4JdIFdA7C6tHRCTN2l05lPFZ3P1ggXDuSPH1OajxYc5Lb-ru50zatiE_PXvLhZCLthfogVG4JIDGipdcz3M_KIsU6kPBQWYgXnaQlJeZXAYCqm2ln6IPRvv96pUocQ5Y8iqBXzqz8dwmDTGXWQL529g8oeyFkHKPF-mLKWdhsmBW662UkFYYFwHWqp9sZQGq4lcikAwnpfLy-ms4IQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab996676b.mp4?token=mQ798ShwerRbLGeUxnBRVhCR2O2Q1cAtejAA8XEWY5CNNO8LGPRWGuOp_-hiWBUTJCcUaYjGS9HmdZU5v54GiHZgI0Y8R0y0_YwzCRePmWaMzDRMTrajRVn1YDrM6WI8jQ4JdIFdA7C6tHRCTN2l05lPFZ3P1ggXDuSPH1OajxYc5Lb-ru50zatiE_PXvLhZCLthfogVG4JIDGipdcz3M_KIsU6kPBQWYgXnaQlJeZXAYCqm2ln6IPRvv96pUocQ5Y8iqBXzqz8dwmDTGXWQL529g8oeyFkHKPF-mLKWdhsmBW662UkFYYFwHWqp9sZQGq4lcikAwnpfLy-ms4IQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل اول اسپانیا به آرژانتین توسط فران تورس
🇦🇷
0️⃣
🏆
1️⃣
🇪🇸
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/673197" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673196">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
منابع عراقی: آژیرهای خطر در کنسولگری آمریکا در اربیل به‌صدا درآمد
/فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/673196" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673195">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELZR3rW-QVEY5YxSjhX4Wev10xVccOUlY_2x9SqXFhB4z9V-NmpgCOoGCLNPcGc_XyKBPn6qwo3VFqelpEaNUlPBGb1dK_TihKFMiZinLP4UHmgfQutvKcOtFvbNTIMEiELyLSGMa1wh73_M0xcNFXQSBuOfK0p_TfbBjA1aN5CKvW4sYt_Kq0nwqTmTUz2q8ToONMr08KHMlzX_2XtNmgAXKd_nCxnqWZaVDwEDxrLM6D4gKmPRWCy7qXutE_D5Xw1r9t98DBnOdEQshBwwzDTV9UM_xDVrw3gqUaic3y34nDKKoQeWz8SBsASk-gSteI76Z6Cy5nmanfJeCxO1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یزیدزاده
🔹
بامداد امروز، رژیم جنایتکار آمریکا، تأسیسات آب‌شیرین‌کن بونجی در شهرستان جاسک را مورد هدف حمله قرار داد. این حمله تنها یک زیرساخت را هدف نگرفت، بلکه جریان زندگی در ده‌ها روستا را نشانه رفت. با تخریب ایستگاه پمپاژ و ترانس برق این مجموعه، آب آشامیدنی حدود ۲۰ روستا با جمعیتی نزدیک به ۱۰ هزار نفر قطع شد و ساکنان منطقه با بحران تأمین آب روبه‌رو شدند. در گرمای طاقت‌فرسای تابستان، محروم شدن هزاران نفر از ابتدایی‌ترین نیاز زندگی، ابعاد انسانی این حادثه را پررنگ‌تر کرده است؛ رخدادی که علاوه بر خسارت به زیرساخت‌ها، زندگی روزمره مردم را نیز تحت تأثیر قرار داده است.
🔹
هشتصدوسیزدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/673195" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673194">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90474a79f.mp4?token=qX_yzyc1Qbc-bDusWAWfkscVXZE3ZbDm-qI16JwP3BhDnixedSH6JB4h0vikNmBvlfXsS-Ax7zW06r3uz6xPaouEcglkwb95hMVPdYdP11-DxBfFLRVnsNPYveogkcru5EaiCuYc9h_Za9lizZYsq9qOvp3VOGC90HHvrpUxLNPnJFJn_p9_g8sS7mnXZp-9EOFmBPFE6oVFxsvFDsqkxFD5Fft1TsTAXAjGBerfAO5U5n3Xpg17GOqYbH-O1UnzwoMhOWbv6huXnCxbLfLWnFsA6FqVO9m8dhVHLo0Vri1GUdPse32hKMvaKI-Vz29lTg6WqNdxFQPUg9i4138GeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90474a79f.mp4?token=qX_yzyc1Qbc-bDusWAWfkscVXZE3ZbDm-qI16JwP3BhDnixedSH6JB4h0vikNmBvlfXsS-Ax7zW06r3uz6xPaouEcglkwb95hMVPdYdP11-DxBfFLRVnsNPYveogkcru5EaiCuYc9h_Za9lizZYsq9qOvp3VOGC90HHvrpUxLNPnJFJn_p9_g8sS7mnXZp-9EOFmBPFE6oVFxsvFDsqkxFD5Fft1TsTAXAjGBerfAO5U5n3Xpg17GOqYbH-O1UnzwoMhOWbv6huXnCxbLfLWnFsA6FqVO9m8dhVHLo0Vri1GUdPse32hKMvaKI-Vz29lTg6WqNdxFQPUg9i4138GeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل اول اسپانیا به آرژانتین توسط فران تورس
🇦🇷
0️⃣
🏆
1️⃣
🇪🇸
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/673194" target="_blank">📅 01:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673191">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سازمان تروریستی سنتکام: بامداد امروز بقایای جسد ناشناسی را در محل حملهٔ موشکی ایران به اردن پیدا کردیم
🔹
در این حمله ۲ نیروهای نظامی آمریکا کشته‌ شدند و یک نفر مفقود شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/673191" target="_blank">📅 01:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673190">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nyd9Y1XFRc4l3UGE5LfnjFp_aaSnE5xft1zZ5aETjnC_CW_FWeEcyrVJXqJkE1VFIqLo__7WW8I03qC-HEn8ZtdFMs-L5UM_je0iYPzypKE8GeXpvJaFVIb98KiQM_fKq3o13BpVW1R0bTtlSJncqa_7W8SKaMgWotREdVQm3E_c6IphRXmOwAUS9raUXaz3Qb8UbvHJ2z8JqV61dHVTAAzYF1GWvU3eu5v76-NO4hyROm3mkO-LyMDuNDwi22hO_rqaJ2NxHLxmo7qTlhAPv24EbqCQNK3jKPFVfeqVPZF6K2PCwTyvT6uj11kU0wUn_FkE2lp9rw1Eex8TwKd9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملکرد عجیب آرژانتین در ۹۰ دقیقه فینال جام جهانی ۲۰۲۶
🔹
حتی یک شوت هم به اسپانیا نزدند، حتی یک شوت در خارج چارچوب! هیچ موقعیت گلی هم ایجاد نکردند. هیچ!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/673190" target="_blank">📅 01:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673189">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802f158a8c.mp4?token=HNmk3ZOuh2mbAOzBjvjIthQD6kxDiFpOLufHKTwMEH0lJMGD2FxlduUAkNhowBC_zPP4JjUsI0KGifJ5jwDrWH8_8IMAfTeH5RGdyhfPMYFBcRaLcquQKtWzAUcesAXzxP28Z5c1LFHuwBsVmu5VQ_44XNqh8dXzwxtU8pp6FQJCIOk5qzrKW9V1xoV9WJQGfktEP5giLdVAp9lDAjOWfOyi6Vb8t-LD3evH3yXnAFOstM6VGJt81S6fNjMGevsk1GKa4rGbf1JA4W-KyN2uygi7vmlXbFu4V9bb6yzaFtBLq_1Ej8TfDig6flI8XHw0ppW3Rn-q25JpZzcCmyLjyk7lihpwGzXSCwMC937_mva6k6bY7IeFkyQP5zI2mXdTQctDY2799xKwNykI8xqMr0sAzkuZq_94UuJC_7wqoOIaGHjgoM4UUVjPN-4_aVzmdLDeYyXrXoj_ketoVNjhE-EcXl2YzvaZprHVaWna77JPLzNj4phfEQGBdx5BQIBUaxOArd7-Clafr_EaAZAjmCM__2vRw1U2Ykc_OuORb-gVpkYVzEPXfnCCb_56rlCRpInG7iIVeEyFhvQiWpaHROefUDhWRPcupqohx6Pd0JHcpDZtv_nVGZrn33PeEucJFbl5EACDSiOceLPP8-v6ek4Zmp28HaJpJTFD6PCFeu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802f158a8c.mp4?token=HNmk3ZOuh2mbAOzBjvjIthQD6kxDiFpOLufHKTwMEH0lJMGD2FxlduUAkNhowBC_zPP4JjUsI0KGifJ5jwDrWH8_8IMAfTeH5RGdyhfPMYFBcRaLcquQKtWzAUcesAXzxP28Z5c1LFHuwBsVmu5VQ_44XNqh8dXzwxtU8pp6FQJCIOk5qzrKW9V1xoV9WJQGfktEP5giLdVAp9lDAjOWfOyi6Vb8t-LD3evH3yXnAFOstM6VGJt81S6fNjMGevsk1GKa4rGbf1JA4W-KyN2uygi7vmlXbFu4V9bb6yzaFtBLq_1Ej8TfDig6flI8XHw0ppW3Rn-q25JpZzcCmyLjyk7lihpwGzXSCwMC937_mva6k6bY7IeFkyQP5zI2mXdTQctDY2799xKwNykI8xqMr0sAzkuZq_94UuJC_7wqoOIaGHjgoM4UUVjPN-4_aVzmdLDeYyXrXoj_ketoVNjhE-EcXl2YzvaZprHVaWna77JPLzNj4phfEQGBdx5BQIBUaxOArd7-Clafr_EaAZAjmCM__2vRw1U2Ykc_OuORb-gVpkYVzEPXfnCCb_56rlCRpInG7iIVeEyFhvQiWpaHROefUDhWRPcupqohx6Pd0JHcpDZtv_nVGZrn33PeEucJFbl5EACDSiOceLPP8-v6ek4Zmp28HaJpJTFD6PCFeu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به آرژانتین توسط ویلیامز که مردود شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/673189" target="_blank">📅 01:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673186">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fg9_EzhOd00HXaSpfLXMsMflhUicgPxLKeZJW-hjkUVdmyyHszBKcWZDKlOftqT9FCDjdO02Mriyl3cq1Xlu_Cc6hawSETBjEP_PH2MdDHV9ab_rYmlNl0AXY-Uj3iGHeyg9D8mx7XtHOiJTWBXJBhhJ7CvmDhyx-E8raqBHG2vqYV8sGguCV87XFbd6GgT1ZKY9zUo610t0RExe6XyVVB-taVuLrKMvlw9D1De0eShDU0xcFvrZtNZyW-_OQ-kxQQKvjhaQY-XV7cc7Sfwz0vhKzzLHW4c_kzDypmSl3Nvx8bQvNV1kZXmMscWj6g-7__s1m5m1GI-4j9e1A4qAng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2oRNEymNCr60BnCy5AP_3_wa5nmJFkiI1frknjV2tbxLRhutc_9WJl96U98hqG027WOb62euJIvLQ84dU1K_ZWBkr-MHmFRv1Mi7NOg2gvOsqcwSQamSwKnkqwCtM3hAihZcq3gnRUijlX34yRcne0RKyjDhPIQQIlukrSRVY3bCk5QNtxM0xsEgBcju9dpj94gURGunNVd_GB0Dr_QGdEgZc10ZdzOsSKLAXEpjuYCTUvpsMD7yYoDHSAC7_3rpj5deI8Opp9dFrifIDa_wM4EPbxsfnezl1HICEW4ILMxCb5cYgq0Jalb_brF5sipgWenEDE9atDtbBBByz0JyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e88f1b708c.mp4?token=caDvJMtcO27Kbn-cHiLcSMCDDhB9dIb41ir-yp-NeCwAKepxk55scQSg3bDfg-f1yLVjrxz3TZWjFtREWC4j5vpDQ3nnVtoxy0PcrlOMIpyJo4q-G1Wo63GeDpRXspr_HRuV6DiEZykHUSciGEx0yC5maM1bZcCDgPWGZnzDmp8woi8Y_5hDoplSRrAM_FKi711bshpgnGibR5UhHLZSfgo0UYvTPFLYxB3n7a7uxdIKsn3oemLOPhkZedUyB3j3C1_YIES4utI94NjhSCQsT3RJzVC3yIPxNnFE0XxbBmyckwWh4NTb86DhElu7173SpNPVcHfiAAYL-lHLdwGnkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e88f1b708c.mp4?token=caDvJMtcO27Kbn-cHiLcSMCDDhB9dIb41ir-yp-NeCwAKepxk55scQSg3bDfg-f1yLVjrxz3TZWjFtREWC4j5vpDQ3nnVtoxy0PcrlOMIpyJo4q-G1Wo63GeDpRXspr_HRuV6DiEZykHUSciGEx0yC5maM1bZcCDgPWGZnzDmp8woi8Y_5hDoplSRrAM_FKi711bshpgnGibR5UhHLZSfgo0UYvTPFLYxB3n7a7uxdIKsn3oemLOPhkZedUyB3j3C1_YIES4utI94NjhSCQsT3RJzVC3yIPxNnFE0XxbBmyckwWh4NTb86DhElu7173SpNPVcHfiAAYL-lHLdwGnkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری دیگر از خوک زرد در قفس شیشه‌ای
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/673186" target="_blank">📅 01:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673185">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای شدید در اربیل در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/673185" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
مقاومت اسلامی عراق: در صورت اصرار دشمن آمریکایی بر گسترش حملات خود به ایران، مستقیماً وارد نبرد خواهیم شد و با تمام قدرت و قاطعیت، تمامی منافع و پایگاه‌های آمریکا را در عراق و منطقه هدف قرار خواهیم داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/673184" target="_blank">📅 00:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673183">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-VkHbCSQs1EdgkH_fS2kRcFLmnuogD70W1osFczHkz5YxxpSVrWV-aeeSEucc7cHhQJrZzHn4MIdUk3S51e8iEed7dclVGQfXVwpZmgh94CAr0IaB4jR7KVU-NuUpklYx691LjrDPJpzFh4ZFB_DlQF1RSddaso5TNYNmdLjwKKXaKntX9tAZUpr--Wry_UDEjxon3tei4OYQNcZ_Yb1sZO2wCrGjNn0F61FLrVy_oRg1xp5YOm7IOA2GcRTccF2NGmI2Nv4fcMlHjPdHVJLOnBxXebJRP4tbpyjSgz_mr9ClHnw9Wq2vM-nCeqRrAJpyEDzw5Z_KpdE14iRaIs3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انزو اخراج شد/ آرژانتین ده نفره شد
🤩
🤩
🤩
🤩
🤩
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/673183" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673181">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwzBD1OYm1nAkWpf_Cok-OHF7VG2-q3C4T4w-N59jEng8JbH7aXIShUFYkkEzv0xB1oh7hZEBXJ4lBwV5blT1xtpAn-BbHJAr9UN31jT-NK1D5Qz84KvhMh-vbcRxr8-8DaeT5i1gjvGdOkuZnf3e4NZVLxZOAHhUUM6y2UJomhutkQFaqe4rxk1YedtZngPyxSGq1Ik9sBO2yx2fUcTiKiId52nzghilB4rIMod0Uz4YsyH2-ePhBbDPJYrDUQx4AHYZza-_AaoZ1cQIjKC4vBGzE08mDu9DmilHEAINBy9fwr7wgKfMljiyEqE7q8Of40vWCRBhCbn6WJrqldlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انزو اخراج شد/ آرژانتین ده نفره شد
🤩
🤩
🤩
🤩
🤩
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/673181" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673180">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای شدید در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/673180" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673179">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
شلیک موشک از نقاط مختلف کشور به سمت اهداف دشمن متخاصم آغاز شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/673179" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673178">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای شدید در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/673178" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673177">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
منابع عربی: انفجارها پایگاه اشغالگران آمریکا در کویت را لرزاند
🔹
منابع خبری گزارش دادند که انفجارهایی پایگاه‌های اشغالگران آمریکایی در کویت را به لرزه درآورد که صدای آن در آن سوی مرزهای این کشور با عراق شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/673177" target="_blank">📅 00:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673176">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/673176" target="_blank">📅 00:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673175">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9b75580c.mp4?token=ZTOeT3WZxhrMNuFHofDDsRK4v7aeUTlDMg5xxXrd8fxQ5yRkUlFWuEZU3u0Rkh2g4eh5s9MEzxh-6ZjianNBTcAJrmCstx3a-TKATXXqRmnZzeuEx5nL4SS_GzV8613cWlva1KccTe272Q4rRL1JGpAJ9--4KkTuYCGjui41wCV-W7AWViEmdk77AVSadOB-l6hjUNaPzfrkF6h0A8gOSyRLG_z0X4ONwnG-xpGB6HPS9HN8YOPq3ZFh0rwG4F1MD9YDsqhW6xZyzhKy6rq-sf2i-YNj47jU8h83Mez0rduIATIvVb7p_AcuOG1Wj_ppt_LctK_tm-2N7TQl3D8u7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9b75580c.mp4?token=ZTOeT3WZxhrMNuFHofDDsRK4v7aeUTlDMg5xxXrd8fxQ5yRkUlFWuEZU3u0Rkh2g4eh5s9MEzxh-6ZjianNBTcAJrmCstx3a-TKATXXqRmnZzeuEx5nL4SS_GzV8613cWlva1KccTe272Q4rRL1JGpAJ9--4KkTuYCGjui41wCV-W7AWViEmdk77AVSadOB-l6hjUNaPzfrkF6h0A8gOSyRLG_z0X4ONwnG-xpGB6HPS9HN8YOPq3ZFh0rwG4F1MD9YDsqhW6xZyzhKy6rq-sf2i-YNj47jU8h83Mez0rduIATIvVb7p_AcuOG1Wj_ppt_LctK_tm-2N7TQl3D8u7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
وینچیچ داور مسابقه به طور تصادفی دکمه اسپری‌ خود را در حالیکه بازیکنان اسپانیا پشت او بودند؛ فشار داد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/673175" target="_blank">📅 00:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673172">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fn7m8bQIiGyRTF4u1VjcZ_tqITaJjmcQTj1NI0vvqkFwncTM_nlJy2OeM1aFnDqVkf2FzCD_hxLwpDtxixVMPKRheFkwZfj27xltVUEifDmPWxJ1w1rvc2yhDR-Bn9bix38_7IsWCQG89iITlWHTlqYXPDbT4RI3RQFvESICkBieJxRw46JnDxPNghYlHGe6uAor1qtLAPi6bl3tv7pkAZrHwYb06YsW_JW1i-ruz_7aXOzoIMg_VWLg0a7Nip13dwjIxqk9wNaROBBd90v0qERa5cmcRZma0eZsVZKsxJYTpEPrLaGgcKNdpN9pZL8806n7ZZuC2egQeNw7V43eFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_PgHEpLRk_ibJULpfjaHfCZXlCvgXGBdhzQIsrN98FFdIBOdDUHQyFUnvi-4UiUq2ZhYI8gPMQ3Ink7HxhKJridNcRbhPXEULtfAyYHhSUblus47LDhM_bRzIaF4IpJVw1KdjD_CQl25acmkPD-YjyK9Ttpkev2I-gNkdDAlj_mtPFjghVcJYLNr4Dn-TsWAbY-Yqownde0wH4Tavn78pTn5LuPcgqwbRjA8_EmXDJbAWlyJKOTr6NiSd2WFcPGwrgWm33K_E7U9Lp8eBIHJzyrikH-OhD5Rf1G6OwKaZBufNXTE2Yd8ai1lEyJYBOl7boBOrl5LzK7aDYxWsvEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fyowF4EMX43PSp3G-bKwS7-FyT45mbp-AHXNHCO3E8P4gw47n7z41HNTqjurYq-sDuPN9FCMaX5pukMT4PBE4n8bdd62qtBRD6TJznkH_VaGAlVsKpAqg6Aq_iYQtNRgfmT-wSXNTchkMMeCVPXMLOnWmBa2rxkeG0jnDZqIfcQ1GOFcf59zYo-QoUaNkvLvwtQt5SXEMCVu_Kuj8vtEynaG21i3OyrUU5gRCbQPe02xqLUFIJCgXB7qjU6oF14Su7IprSSBKPkif2Kj2WXs8MQGk_h8263lwEouwlJvtx5fgh72b9068FgoWVKxFk9-_2hyVtUo5ZdjwjC40AZVQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جایگاه ویژه در استادیوم با مبل و کلاه آفتابی و ویوی فوق‌العاده نزدیکه به زمین
🔹
قیمت: ۱ میلیون یورو ناقابل (تقریبا ۲۰۰ میلیارد تومن)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/673172" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673171">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
واشنگتن‌پست مدعی شد آمریکا برای جنگ گسترده‌تر با ایران آماده می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/673171" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673170">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای شدید در اربیل در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/673170" target="_blank">📅 00:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673169">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaFlzJxElw-5FgC6biVIIB8kdsYTUyekpzv-Z8mh6ywJbkl7mALlqGBEEEdRPNu7pjLS4h0U9HAdB0DweNBcES0CE0jhWRBNc6JjScqYaZvWnu1iiL6tHPXdMzbUvQflhx4BBMB4tIl2JmBQhXVgRFsucKoFCghgg3IbTbO0x9ma7i-CQabOBW13HYs07Yi7wKooMrFZT3rDq3Xer6fJ3twOhOo46-vkHhFwJBPhI-EvdUyNyXwKhxOT_pmjWccCKG_3ZCexmjlsh-jfAD3Wxlb_yEipFU8dlpUoNGd7CrCBPPfUfO98NuKi_Z5gvK5bqLOB1U8i-k7yGgQA0RPR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارقام نجومی برای بلیط فینال
🔹
ارزونترین بلیط فینال: ۹۵۹۶ دلار (۱ میلیارد و ۸۳۵ میلیون تومن)
🔹
گرونترین بلیط فینال: ۴۹۳۸۴ دلار (۹ میلیارد و ۴۴۷ میلیون تومن)
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/673169" target="_blank">📅 00:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673168">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
منابع سوری از حمله توپخانه‌ای ارتش رژیم صهیونیستی به جنوب سوریه خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/673168" target="_blank">📅 00:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673167">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
معاون استاندار مرکزی: صدای انفجار لحظات پیش در اراک مربوط به اقدامات آفندی بوده و جای هیچ نگرانی نیست
#اخبار_مرکزی‌
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/673167" target="_blank">📅 00:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673166">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ac438237.mp4?token=PwKo-MK0NW_TSf-fbqybyTVo_TmSDafEpl-Wc8Vip1HULpgPU2Dy-IN4UkfM0gb1QjcQMp_g4Od9301QC9qvZW3vV7Iv-9RXPKtOKak_9_KcJTueAaYChnI_dWHvehowOhWBxNek_hRWndynlWIerzPyf66b4BkjYm9xv6Naw0Qrs3YXoq36NogMv17EG0Rhionyccy5a-EN_F-GGZoOCYUEJ-6M63H23Lk2OkpYAshGvcFsAy_3jwlueSPaRdRv4odeIJJbT59IhVUIZFQKZhq6w0QrjMY6mP3joEEN3kvWVeVPvwYwYDlqWCaDc70kBA3wRu8KW64r_i4eFl8uJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ac438237.mp4?token=PwKo-MK0NW_TSf-fbqybyTVo_TmSDafEpl-Wc8Vip1HULpgPU2Dy-IN4UkfM0gb1QjcQMp_g4Od9301QC9qvZW3vV7Iv-9RXPKtOKak_9_KcJTueAaYChnI_dWHvehowOhWBxNek_hRWndynlWIerzPyf66b4BkjYm9xv6Naw0Qrs3YXoq36NogMv17EG0Rhionyccy5a-EN_F-GGZoOCYUEJ-6M63H23Lk2OkpYAshGvcFsAy_3jwlueSPaRdRv4odeIJJbT59IhVUIZFQKZhq6w0QrjMY6mP3joEEN3kvWVeVPvwYwYDlqWCaDc70kBA3wRu8KW64r_i4eFl8uJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری عراقچی از ماجرای تماس یکی از کشورهای منطقه و تهدید ایران: ۴ صبح زنگ زد و گفت ساعت ۸ ما شما را می‌زنیم شما هم پاسخ ندهید
🔹
گفتم بزنید ما دیگر پایگاه آمریکایی در کشور شما را نمی‌زنیم خود شما را می‌زنیم
🔹
منطقه باورش نمی‌شد که ما آنها را بزنیم و آنها نتوانند حتی یکبار جواب دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/673166" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673165">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVzizbgYW8jZ4NeJSuIYPf_0H_TKQ8JGQS983SMYe39LHuN9MedcfmMl5jpS-m17eWHB3wZKsjXwAuX0CnVz4JYBpXTTp0vLmBc9OOpX9bO_DA9yEfWZua0C75-A2sKLTpaZhoR1qVymDrPQTC5cu_61v1USyNJQbmczJb2duY49rCrJ6ILg_gaqBity2ksOTm2uQc99gXjLyIRJfJiNaWZP91AUdOBhUNuaf-a-_rElogZSTyn-k8h9QehXgUosmdxe1lXC_C-eex5xgapCi8Mf4nSraueYPyvWQVQbe0J7_dFWd0a1FHFILeqT11aBsBRp4scpZLZAlyzQ34a2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/673165" target="_blank">📅 00:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673164">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a341f37b.mp4?token=su1Oyz5tuqxge2kyqLL5aBOkss_0XupkeBxz8L2Tg-gdzMW8cEcnXAi-LUZWkVec8w_sw9YVGJ64FIe23H96ch5AE2fOF4KuAGoufktpokcWgNQwKDu13U7TMQTOd54glRu7dZYdfFvSZg97Uqu8u92SG1hqHi7YczeVQ2G-VwH2Y7qy2kastnO3LynE_1Ad_DhyW6J9Qe02HXpSHS8Euzg70GVPPgTVW3HoDHtk7oarna1uv4fz5CfvttWfvpiM5pCrl8dDsZwYEZOopfHcitUxb7EHU2eUZ4a7P62n3vK0cLcZitnlYjUFfNR25aYJjY6oOnybw2qE2HtNymV2Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a341f37b.mp4?token=su1Oyz5tuqxge2kyqLL5aBOkss_0XupkeBxz8L2Tg-gdzMW8cEcnXAi-LUZWkVec8w_sw9YVGJ64FIe23H96ch5AE2fOF4KuAGoufktpokcWgNQwKDu13U7TMQTOd54glRu7dZYdfFvSZg97Uqu8u92SG1hqHi7YczeVQ2G-VwH2Y7qy2kastnO3LynE_1Ad_DhyW6J9Qe02HXpSHS8Euzg70GVPPgTVW3HoDHtk7oarna1uv4fz5CfvttWfvpiM5pCrl8dDsZwYEZOopfHcitUxb7EHU2eUZ4a7P62n3vK0cLcZitnlYjUFfNR25aYJjY6oOnybw2qE2HtNymV2Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای بیژن مرتضوی، موسیقی‌دان مازندرانی بین دو نیمه فینال
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/673164" target="_blank">📅 23:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673163">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39ab21c56.mp4?token=ccg--tpKZADsWAdAB3AGjFp_ANT-LcNKWMk0aV9t1OA4RCCTqm0FzqkA--ZEsst9pIbCmpUolc4xpOw4hohZrc3Yr9nKT-WLmj7qKLDSE_6CllukTPfsWC7A2cXMIGaXPtQzpgL5rVXGk_fXjBtSpueeBCTKGUr2DU0SYWuROfkALR7xbQ-1rcrlyNSDQ-0ydR7eloikmTw7RIQS63Y2Z7yG6lZSFOu0FI3WYG7cQ4jWI5o8Ce4IskCFjiHLyclucyAOuxXjdHKt5n461bfNjso_nlh0C0r30OSuBfwYr9E0tre6Xkqn66T6AOsamOPt6-jzs5wK4c7mDzc2ZZSD4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39ab21c56.mp4?token=ccg--tpKZADsWAdAB3AGjFp_ANT-LcNKWMk0aV9t1OA4RCCTqm0FzqkA--ZEsst9pIbCmpUolc4xpOw4hohZrc3Yr9nKT-WLmj7qKLDSE_6CllukTPfsWC7A2cXMIGaXPtQzpgL5rVXGk_fXjBtSpueeBCTKGUr2DU0SYWuROfkALR7xbQ-1rcrlyNSDQ-0ydR7eloikmTw7RIQS63Y2Z7yG6lZSFOu0FI3WYG7cQ4jWI5o8Ce4IskCFjiHLyclucyAOuxXjdHKt5n461bfNjso_nlh0C0r30OSuBfwYr9E0tre6Xkqn66T6AOsamOPt6-jzs5wK4c7mDzc2ZZSD4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی ۲۰۲۶؛ تدلاسو و دستیارش بین دو نیمه بخشی از برنامه اختتامیه را اجرا کردند
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/673163" target="_blank">📅 23:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673162">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYnQDZpEJx-EiclHOTw8PuPmLIKXtpVRpb5fHJnwZBli6e6ly_OcXYijj3R7Sw8Epa6lsnkv-VyJ7_lgo5QSLufpqXYhz4QY3vPlQa4T_t_UWO-QeiXZB71HJ58jZB56htsWzJbb91VMt0PjgCu8sYqrPVzU0_zmhJYDwPzaY0NDxKn9X01EIfZ10xISfQB3I7lHfBEcINVwjKN1sZoQFp1vlQbm5LgHNFxgYLXmmQ2Gd_ru26wqKSWR_uJa7IVSZC4Cjwd2dYHNVZA0lO_mKY-90nTF3Kbewf8KX8WVtaWopa8J_Unu0HXn1bOqwWHJkFfvNbiWxOwQcwvmviMU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی زیبا از لحظه پایان اجرای بین‌ دونیمه بازی فینال جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/673162" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673161">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgd4rBKh-qki0MXoufYE-RESKi1JpqeFrTe_ioStudUHj5Lb99T5U8Qik8sgirCN0N7X_6_MDE9nzQSjlA9i4DlFmtgYka7wRNy17lWTP_h3WxFWS9Hv-9BEnvgRoN4skLOZ8BpSynUG0GgI7HSIBAf8TLUxbUUXfV4H8uMJy9eqzYPE9e1W3PJaWHL3TnxZznMtBEI-hfbdbyAEfSG3bpnsLwDOhkinlReGUgDY_cOSIMiKd1w6coLgFwaEnfs6P4h9NinFTMvpLnekW3lKu85PTfu_C-phZd8zd2UR0YSQDjQF86TK_3mWWD8V9tCNCOTvNZK-FgXTXIQHTNNpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اجرای گروه  BTS بین دو نیمه فینال جام جهانی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/673161" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673160">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pscYnQLIu6BG5qR6knmQKx2KUeHLtDFdNaMhhgZnZNEKYOFINeGYFox3TE4cFNj5VT_hn0voNmL5wtHo3vToJtlnaxsEkq4HaFA6GvuJaj3Vr4YOhYxhMzL3gzH76f3XewaXrPW4tm7inavKbq8n0Y26NYGyWL4qpCYlHVMTfLS5a3dJy18XAXBdffz189cGuBBvx15eBpl8jGTFqb5VuxMGNNnVmhRBbF4HmuoFEVGVdb98jxHgFFexwx21rk7sH4eyMRN1ikjuD-IUA_MJap5OwQK49ta1t1mIDZmsBr1Xg5HO0SmsbbwKoKflgj6OtFjIXIjzAl-N6u1vfycAeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر خارجه: ایران ضمن محکومیت قاطع تجاوز آمریکا به دارخوین، اقدام مقتضی را برای دفاع از منافع و امنیت ملی خود اتخاذ می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/673160" target="_blank">📅 23:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673159">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyqtBgXWsmBWwxTE9HveYYomuDrzUbgSgVVToprZsBDjFbFhtKv740uMLDauvco0QDg3jOMTxBhN3TZGZwQe-se8rQxmtkEyC8sAPWgRJbvOKClVdOKjhpe2Ygu1o3Xdq-s4Rt9vnuZH9eMzA75OBjXjkZOpNe6SNVqCJWuoeVz_GUmjxiLw0Kl5nfIToDDhH7JMyX7xb6rSIdQjcfCGmS_UCUUB2sDWGRGvVMZmvZ1YW7W2KIhoY7OJaH4FYeSnIt0e0VJEMcLLJbGSF6WasSIUdjcCumSj1mBk3FggSbldVAjBJwQoqze5uajsh2E-VHFrKk2VQJbPQFFAvilOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی، حین اجرای ویالون در بین دو نیمه فینال جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/673159" target="_blank">📅 23:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673158">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
اسرائیل هیوم: سفر نتانیاهو به آمریکا برای شرکت در مراسم خاکسپاری «لیندسی گراهام» در هاله‌ای از ابهام قرار دارد
🔹
مقامات اسرائیلی نسبت به احتمال هدف قرار گرفتن چهره‌های بلندپایه این رژیم توسط ایران به‌ شدت ابراز نگرانی کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/673158" target="_blank">📅 23:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673157">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
گزارشی از هشتمین روز حمله آمریکا به ایران و تهدید دوباره ترامپ
👇
khabarfoori.com/fa/tiny/news-3231372
🔹
مصاحبه جنجالی عراقچی؛ هنوز آقا مجتبی را از نزدیک ندیده‌ام
👇
khabarfoori.com/fa/tiny/news-3231467
🔹
پاکستان هم شاید به جنگ آمریکا و ایران کشیده شود/ میانجی تهران و واشنگتن یا متحد نظامی عربستان؟
👇
khabarfoori.com/fa/tiny/news-3231570
🔹
سعید حدادیان: آنها که می‌گفتند «نه غزه نه لبنان، جانم فدای ایران» بروند جنوب/ می‌خواهند ما میدان‌های شهر را رها کنیم؟
khabarfoori.com/fa/tiny/news-3231482
🔹
آتش بس در دل آتش بس / طرح عجیب قطر برای توقف درگیری‌ها در جنوب ایران / پایان حملات در ازای گشایش ۱۰ روزه تنگه هرمز
👇
khabarfoori.com/fa/tiny/news-3231634
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/673157" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673156">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0wSxH287Yg6GHeL9v8omKSbWLbP9y5A2_9PPUtbDFplTo3iyflbnCCLGpWLCrvxoQDewgLskU4ymFl1cx7hvDiZGCFSi2aBwBSlAPC4adg0Mfb4WIKtS60z3tMfVcxGzD6_QkSLM7xBPvA4VY-i13tHlZr2R_3Dmpw1GWih6-NliTPxKNerifI_DOEVMHZ04sEbVzxcJM1UnQ1AH4CPlUZ8FWQ9b9vQD9-Xv1vFlFADfXz0AoAPxZTJ0D3TwlHayRwMp7QSghL_qoSDcMrT2t2_fZOrP5VsljCj1578jz0L8YRXwXi8ht3ryi3cASWYpLj2CV7oGe2LkqdTOO1iZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسی، اولین بازیکنی که در ۳ فینال جام جهانی از ابتدا به میدان رفت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/673156" target="_blank">📅 23:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673155">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
حجت‌الاسلام کرمی: مردم ما در اوج فتنه‌ها، چراغ اربعین را روشن نگه داشته‌اند
واعظ برجسته کشور:
🔹
این مردم، با وجود پشت سر گذاشتن بیش از ۱۵۰ روز حضور در صحنه‌های مختلف اجتماعی، هیچ هراسی به دل راه نداده و همچنان با اشتیاق، چشم‌انتظار پیاده‌روی حرم اباعبدالله (ع) هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/673155" target="_blank">📅 23:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673154">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIjeo5yioSHSN-U-ahw2GwefubZfotMoYEJvCq2XKTdxtPRd-JP-69V_dD7UEU53Adlctde2_qshtz5Oix3RD0YzoSjjodko0jEl9F9L-bf4dr242Jq_7LrCz9vqgx_Qqaapz1mzPSf24RGL1TGQGzOcEE6fK7Uy05GyXadM9baXiEcmgZUg5yJzevRlq_ePWoD4dMOkL8dahdU7Nk3BPqzp7FnYkH4fVmAWelFAFwtLbbWRZKn2uTysN7w3eBjvqQCOS77GEMNzJCTbHUiq8RNX6HOOHcoCzbFy2nI4GO2BGpBR8UDdrZDmiw8lbo4KKKZBTzZ_3MEEEXkFfEHu6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو هیات رییسه کمیسیون صنایع و معادن مجلس: اولویت نخست ترمیم کابینه، وزارت نفت است
قیصری، رئیس فراکسیون نظارت بر صنعت نفت، گاز و پتروشیمی مجلس:
🔹
در شرایط کنونی، اولویت نخست اصلاح کابینه، وزارت نفت است
🔹
آقای پاک‌نژاد نه به برنامه‌هایی که در زمان اخذ رأی اعتماد به مجلس ارائه کرد، عمل کرده و نه تکالیف قانونی وزارت نفت در برنامه هفتم پیشرفت را به‌درستی به سرانجام رسانده است. همچنین در حوزه ارزآوری و بازگشت منابع ارزی ناشی از صادرات نفت و فرآورده‌ها نیز عملکرد قابل قبولی نداشته و این تعلل‌ها در بروز نوسانات ارزی و اتفاقات دی‌ماه بی‌تأثیر نبوده است.
🔹
اگرچه در برخی وزارتخانه‌های دیگر نیز ضعف‌ها و کاستی‌های جدی وجود دارد، اما وزارت نفت به دلیل نقش مستقیم در اقتصاد کشور، معیشت مردم و مدیریت شرایط جنگی، از جایگاه ویژه‌ای برخوردار است. کوتاهی در این وزارتخانه آثار گسترده‌تری نسبت به سایر دستگاه‌ها بر زندگی مردم و اقتصاد ملی بر جای می‌گذارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/673154" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673153">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65067a3a3.mp4?token=NR3_dqcXTiueIZqBfHNkYVMidakINuZnZqAc3kvU-f6Je472Pwc2GucjchfBz1fa6KZ32WyEBBKZyw2sSoGK_Z7WXosG1lgSrfl5IIEqIaEfFKiMcMAKjPV9qfl48u-QxWeJkMzQ0KZO5rgv8e_pTyAwYyRyRt19Ni1KxNZYRstUj3LfsPYEOkTnsXPzQV4uehbsQ8y-OBIH2U8utSGWVd5kWxJhV6LVCQ1X6QYDrR8HkuwBumiNCf_ssTYcXz3f6U0c1Kco2eqMqWJQMukADmUyztiSo7AZkkJzMiKPMDjaoXmRpnOzAsECDsN8ySDcMmgTv9MtE6qrd-Yljg76Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65067a3a3.mp4?token=NR3_dqcXTiueIZqBfHNkYVMidakINuZnZqAc3kvU-f6Je472Pwc2GucjchfBz1fa6KZ32WyEBBKZyw2sSoGK_Z7WXosG1lgSrfl5IIEqIaEfFKiMcMAKjPV9qfl48u-QxWeJkMzQ0KZO5rgv8e_pTyAwYyRyRt19Ni1KxNZYRstUj3LfsPYEOkTnsXPzQV4uehbsQ8y-OBIH2U8utSGWVd5kWxJhV6LVCQ1X6QYDrR8HkuwBumiNCf_ssTYcXz3f6U0c1Kco2eqMqWJQMukADmUyztiSo7AZkkJzMiKPMDjaoXmRpnOzAsECDsN8ySDcMmgTv9MtE6qrd-Yljg76Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: در بازی فینال جام‌جهانی هیچ تصویری از رئیس‌جمهور جانی آمریکا نمایش نمی‌دهیم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/673153" target="_blank">📅 23:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673152">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb30f9faa.mp4?token=dDdzzw-TknjzdoMxyGNSGjNNdPLmlLLNjG2OshD1hA4WEuyyWXvVOtotO_CcCzyd6OeZ3XgHJ5CY40g7cDB58ZdS-j_M3iopxfQRYYl2MuK3EecwmzfY4eP8qs3jJph6V7ArT4PjVgimUgAB4fSXbqKzOq3DCeWUM0xNLQ1yypYZl5YPFVqemYByID0l1oc0ZCeLyHYdfreo3-IHjQZVpOAcK6tFfNp5SRXlj2h0MGSmt4gihnV3b5JlNF9F9wbYtiPm-TwRKq33zfOCx6XFGYZN9SqB5xTnQ25mYKFE1jxdRJDMxy6TWuFLlHDjJSElvm7htAcMcBLCIuSshUJnmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb30f9faa.mp4?token=dDdzzw-TknjzdoMxyGNSGjNNdPLmlLLNjG2OshD1hA4WEuyyWXvVOtotO_CcCzyd6OeZ3XgHJ5CY40g7cDB58ZdS-j_M3iopxfQRYYl2MuK3EecwmzfY4eP8qs3jJph6V7ArT4PjVgimUgAB4fSXbqKzOq3DCeWUM0xNLQ1yypYZl5YPFVqemYByID0l1oc0ZCeLyHYdfreo3-IHjQZVpOAcK6tFfNp5SRXlj2h0MGSmt4gihnV3b5JlNF9F9wbYtiPm-TwRKq33zfOCx6XFGYZN9SqB5xTnQ25mYKFE1jxdRJDMxy6TWuFLlHDjJSElvm7htAcMcBLCIuSshUJnmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میرمهنا بندری چطور کشتی‌های خارجی غول‌پیکر را در خلیج فارس متوقف کرد؟!
داستان قهرمان جنوب ایران
👇
https://youtu.be/PkNQz2D9nTY?si=pgrF1QTSxQdPUYkL
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/673152" target="_blank">📅 23:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673151">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dec6e7bf.mp4?token=McZx8eXFy7YHT4meU7qiA5_V_STz03UG4cUu-jTXTra69QFdV0ZktB-iX1ByH0jsPqeqfWMDkScE0eOBEOfKIJJheY2OJEW3DXbR-MMQuF2s-9zPJcgWUfGT35FwCbMP9AR5H8_FaXtc3txpg6yCO68Y4CNQx71qFAd2a4T0V-7qUAmgsc0LA6rHZVq5FZoOiXDzLDRlU5w4bXtqN2RO8hJNuCYxNRHendNGUtU-9U1udLpuBRd0GNMJuSyudJIbI75NFX7cx0JEhlPdNbeE9fmkfmw-zTJPI4tDIkF6dzxs_NP6x9ZIWGrUJjqkL7K3r7GlqAJQSXMJkY9OrqIS6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dec6e7bf.mp4?token=McZx8eXFy7YHT4meU7qiA5_V_STz03UG4cUu-jTXTra69QFdV0ZktB-iX1ByH0jsPqeqfWMDkScE0eOBEOfKIJJheY2OJEW3DXbR-MMQuF2s-9zPJcgWUfGT35FwCbMP9AR5H8_FaXtc3txpg6yCO68Y4CNQx71qFAd2a4T0V-7qUAmgsc0LA6rHZVq5FZoOiXDzLDRlU5w4bXtqN2RO8hJNuCYxNRHendNGUtU-9U1udLpuBRd0GNMJuSyudJIbI75NFX7cx0JEhlPdNbeE9fmkfmw-zTJPI4tDIkF6dzxs_NP6x9ZIWGrUJjqkL7K3r7GlqAJQSXMJkY9OrqIS6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا در تهاجمات اخیر آمریکا به ایران، خبری از اسرائیل نیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/673151" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673150">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKF9SfVAzuF7CSukuPl9IgNou5AiI085mr-gC3HaI2QLebxTJ_v4ldnrENrcOaEYDIwt1Ca_3nEkW4MuwkIJq5wdkQag3O62h1yICm5QF8bKMmKJKtQ4K3LmRbXSQGQ4nePHU_Yyp3XKEeqr91QIN0mEd3So966Y8pW7iaHHuUGTLAZd_Qu091yefSVlRl5f5rSLNxIkPoUGM43AvhKyrD7SsJQBc2o_kDNPxjCaWkjZ3ae0oM8_IHS6V2wzEWMxZdmC56fJ4VydgOo8mLIVYnWaCFoRZnyFO20Vh-C0D-miqpCLErCNkunkZ48JdZ3kdA-e9rKNt33C-qeVhkog2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری اکانت اینستاگرامی مربوط به پادشاهی کویت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/673150" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673149">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a749daded.mp4?token=ZQz0hubwSm2crLu1aJ2_EXSThv_p9euzO05TMs_qzrWEcoqoT6BhejOJ-EvUgMkTKynS5JJVteG1H09q2AEEsaQAdBkQkDYZmhEW5hiFdw1BDLC_3sBetnE4QD_VdwA_3FFZg6ayEEmSAAGTpn0xWI7Z_61j8S7TlFDXBQYo6R_aZ9sfF3ZbGQ2KS_Q_qflNVN5QGwMaP6u7-eI95GOBkMemUKYcc-F9Z2TmPD50ZirnmGDuPL3Cy5hQWPMmBKUTRIlyWwMBr9ubP2lt0FDnTDQIRMbvDSD4De4-XvSM8NeDM-yYv1TDPOoCuBYTsAYtCCBkOMSMzV6QR7oyKif7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a749daded.mp4?token=ZQz0hubwSm2crLu1aJ2_EXSThv_p9euzO05TMs_qzrWEcoqoT6BhejOJ-EvUgMkTKynS5JJVteG1H09q2AEEsaQAdBkQkDYZmhEW5hiFdw1BDLC_3sBetnE4QD_VdwA_3FFZg6ayEEmSAAGTpn0xWI7Z_61j8S7TlFDXBQYo6R_aZ9sfF3ZbGQ2KS_Q_qflNVN5QGwMaP6u7-eI95GOBkMemUKYcc-F9Z2TmPD50ZirnmGDuPL3Cy5hQWPMmBKUTRIlyWwMBr9ubP2lt0FDnTDQIRMbvDSD4De4-XvSM8NeDM-yYv1TDPOoCuBYTsAYtCCBkOMSMzV6QR7oyKif7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از آشیانه F15 و F16 آمریکایی‌ها که در حملات ایران به پایگاه آنها در اردن منهدم شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/673149" target="_blank">📅 23:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673148">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHCMcIp7LyEsdYnpeWFnmMWBKgqkUl4tYP-rlLsOy5_UB9Lc9gnCIjzFMLJiHroIXFYTzPQCYWYGO4k3k2em574tFIsMjAzOYZR1ZOFhbKpXfMqxP-7P5ldHom7EhlQCx8si6GeomkaQ7B9z9vddZwC-Y-cfYsPmtGrzmFrsGUBWj8FzaAfAMgRX3Hmg3zYmbHk9tUzkKD35K7rVywYMlnn5VHeiEc3JuGcIr9tl6-2-aoDnlTa-z31Aia1nWT3n3jYZ2wm3coinQPyzzwI1HnZJ7EcowfcF_sg5_HRLJZdS-zARTdYy7TMPHbsirq7j5q85BsB1PCjSGy8ELoQ8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر ژئوپلیتیک: یک حسی بهم میگه که انگار قراره از اردن یک گروه مقاومت وابسته به ایران، بیرون بیاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/673148" target="_blank">📅 23:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673147">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN4bg_o2gg-ivuNxqoOoQB7djOV9QQNxmPNj4HTr2ZkT1rQ8jFzwjZsufRDciY8CU5Dn8ojFs5-l_6zoM8MAPg99HCS67Z2NnKmeI9KktxL-HLDFlnN8zBQYv5o2l8onR0kbKfXIwp6HTTx21Mi5I72qVm6-3or6U5r6-9ntge5GDc3pNHEbvJ5dXSxKltNLgOr7qsTjmB8T5DaSS5ExoPTw8Y777jbxL3FnG3iMyrRdIdjdJDCwpJSDxJihnLzNIPyygvLw30hxnZcJoN_Q28cHXUXfei88FZyd9yCKNG_MWwjVPCnfHkmHuO51S0y7ctV_jkxHqiUNHdizbfrpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستیار بلوند مرموز ترامپ جایگزین دختر ترامپ در فینال جام جهانی شد!
🔹
حضور مداوم ناتالی هارپ، دستیار ۳۴ ساله دونالد ترامپ، در کنار رئیس‌جمهور آمریکا بار دیگر توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3231469</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/673147" target="_blank">📅 23:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673146">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
المیادین: صدای انفجار در اطراف شهر اربیل، مرکز اقلیم کردستان عراق، شنیده می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/673146" target="_blank">📅 23:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673145">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaKMIXckjHSrGWuzg_SQqhfBPSfhS0IaBGsewrh3bCG2ZyZAHGwWU8LqwJJWOm4uDegH3PobCeaOm9xe1NfEoAMrBhh6dss_mr-iBNXVYrFKYD815MOzfYyYNaq33_z5O6wXFWJPeffOEaSDQtSoBvlXK5upilQaOSIqehVANKuZWm0QvRc-yf1Vw0mq5Mo7GduBeLxz8ho_rumKklNGv-bByOV4XUv970PLhRNLgCL9zaXP6ULOGSdkQwZvo4UzL939QqjNdsaM80aDJPIw-Q3wRaJksy3hcNKLCnhtyTSVkluZD0EUQB6MqnM6xx6O1_xJ5vM9-CpdA1Ej863JEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر نظامی و ژئوپلیتیک: وقتی ایران کار پایگاه‌های آمریکا در اردن را یکسره کند، نوبت پایگاه‌های نیروی هوایی اسرائیل می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/673145" target="_blank">📅 23:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673144">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: کویت بدونه وضعیتش در پایان این جنگ عادی نخواهد بود؛ کویت درس عبرت بقیه می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/673144" target="_blank">📅 22:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673143">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7evvyw3b_jT7cWKo80YQL8CLR_zpwib5A3lWohsZat89k-VIVVZLeqXeaWGHlOqkIFMCLRjQ3feOVSIgIm6uaNLyEZ6rPi7W8b36FZ98FB9TXDz9L8EH7UZOqVgdoCyXCgangr_WylK3lwP1Oym_7AiiQnkO4myBEf5lTRWAk_HEzxk3-qEDY10JiGjcPkqHgxArDR1Ub3Z8sboohdG8sg7E2nxA2ebGeWyN5nZ--bzI57XaXaPm8ZxH5KoWlNE4Rhfl63ffqp5Qha4_SfV6MadomXx87ord9Vdc-2SmD-669GOzU5Sivpsy4-OghTa3_ewD6VH0o6Ko4GbUzMJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کیم آیورسن، مجری سیاسی آمریکایی: بزرگ‌ترین ترسم اینه که ایران با زدن تأسیسات آب‌شیرین‌کن اسرائیل، شبکه‌های برق و زیرساخت‌ها تلافی کنه؛ بعدش اسرائیلی‌ها فرار کنن، خب حدس بزنید کجا قراره برن؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/673143" target="_blank">📅 22:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673141">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZS81E7lAKtUhsEUUk1a_KmU4nvSngMA9PxxaO9aoeZhUz0ozyRW4lKhipsJi6HwKADjYvRGwbdK8dhrYHubuIVC54dqU5RZuuHKOGaeA_bMvUKPScaK9L-3H72LKL_u6OasgP2QjVQNyqulFv6sPgdRl8HS5oBviBN0f0mfPT7ob9ALCVPYAOtxgcOrTEPjdbJE_DsFx12rFRZz3uIJDzaMylXa8x-NAtuATw0g2hq33Sp1_LGrMN1itYXI-tTzkJnOABvavU44zW7TcyLo5pN6zq079nRYfiZltP7aWyboEZ67KrAX8ZKguZGPIrUQlxLfKppTjnbAR8iLNEIP7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUR7ncnbAEOeBpTudkrjuUxIimnDm3iOI5f1ShHkPgSR36GvCf-VzWjRSoLJlNesR03mHHMCxYwCXxQDATHY9RRUl5gkgjc7lhy7YK6JU3569yOb7QKPs8xOtPYTf3LFTNHrqRBMHrKShdsXIfaNDeJVlLaomBOEHUKzJMz9EN5n4LPe4q9ryuQBkeG62O9mXTQDPMAdDGoEfFr9IOa3t8Lw0pJ0EYMd6EVN7iskkPpKyGon4veNeaynDbaG8eFaOGl7Z7KUZqvkdaGElbrQmX93cNG7JNwDPaBDfBR0siW7ubTh4uj0ZYdLCdIfRZddnZfk1IE_JiC_lJtorbK9Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سرنوشت عجیب پهپاد آمریکایی در عسلویه
🔹
پهپاد آمریکایی MQ-9 که بامداد جمعه توسط پدافند در کوه‌های عسلویه سرنگون شده بود، با کمک یک الاغ به پایین کوه منتقل شد.
🔹
تصاویر منتشر شده از منطقه نشان می‌دهد که لاشه این پهپاد ۳۰ میلیون دلاری به قطعات کوچک‌تر تقسیم شده و با استفاده از یک الاغ از مسیرهای صعب‌العبور کوهستانی به پایین حمل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/673141" target="_blank">📅 22:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673140">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سازمان تروریستی سنتکام: بامداد امروز بقایای جسد ناشناسی را در محل حملهٔ موشکی ایران به اردن پیدا کردیم
🔹
در این حمله ۲ نیروهای نظامی آمریکا کشته‌ شدند و یک نفر مفقود شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/673140" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673136">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQhTIBISBcm_t3xxrmts88ZImApD3vpmZ4HqjDIZzfTZs3z6e1G9QqMvmKlEzEJDBHFL0Smnll1sHzzlBlpZz7lUtaq6eO_zn_ijKzUEFwelaHQvRiJpEtZGN0PjDMgIqLuL7HNANaoHf8i4vPHafuJVtuTq3KJidlOs-qvkil3M6uKRAY9D0nUC2j4yc2bAwZcNynNwCmz7MU8FtxXbbq1al0wSRcMOvVa87aZBbqxGLPc7z7uXyS4fj2rMwMsyioE4c_KjrCJrw3Z97kauKdjGIMdVZTraj2yhPtUhKAn-7BCZAuErYVLhDKqqxV91FwMwI7kQ-nip7ZldY1QCfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpxFiPHEAzlBrdKl1zyOquk7F1Xs5O8q-mq5MhbQHpH66dOWzLLKOABs-lq5_5rsN-jiOOCWeYOTZkm9Pox4LLAqbp4NyQdLlw_SqdGP273kM4abmGQZyp4byRO2ae7zWwVsQYNLjlem2LR-HGEFE5w7ZToNE0OTnbO8UZ8MhbeEoPyYsjvyST2CLOStdo_dmJdCUXw_KXuybXckIvtj52aSnYj8c067hGM457FhQz8NFe2EthB3qqVui-rf01Bs3nbTIps5k8stCziP_DV07L9RF7-ll2b-A_qiCDwLI0dNqRb1-tHV6aOPzyM8GN8lwuEivh2qXejNjr5NqEx9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcPn48FLsoBewg8pZr2O6Jis1k95Ih8xCldYV_dBRoACBeF0GwPBMRJnWGjas4QW-aLG5W2100I7RkQ8ytEVFj--Ibks5ZqaA7oIlDbZGd4O4TK-OeqniTZxk1u5I9uFrEt7ke3ERRRxeX_qNVn4kMQqYcQFMGdzjOpcapiElEnYz_nvpG22DgdVfw6bWNK4oJ0ehKmlTPU6BUCjz9gLEiaJFZCYSWwEvb0Gts7JXl3QNlAbq9ubPAsPXkBE7vB5CmRDW5w2EJVHFUCdvsq97RlAmR2JjXyXA8IXxQaZm7jxNTVf1SjW36VpRB7KZ20YJkGDQQ--H0nWTCnyU-z24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aAmoOiXwZ2emPSqKng5bLCB8jJx6pKI-2SrTgXykjnL2tZ2kjDGOhR--M63nGrWG6AM9Sb3AZqKcGKumibkIF8zdJmgz2ayI4oDWiCwNs-OcrQ4mXZig1q-2DJAifMOPzb9rscPgIVeXT630wYRPowZgAyC1nPj4YcjeeXC2jhD5SydPdbtzimGXooQZzrDR0DiWkT4VsW-pIyNh7qxlELVSFmYsAmOy_TikcBd6H3eGuiFDPwBMWpshQkIhQqEs6RXfjUxiL1BY28sVSVyhef03-4h0tQ3aDPkbvVvRkf1ZkigF5JUHrlSOom7FYXJgmIHDSxfVsyWZ_Txn-NJhHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درخشش ایران در رقابت‌های جهانی ربوکاپ
🔹
ایران در سه رشته فوتبالیست سایز کوچک (SSL)، شبیه‌ساز امدادگر و امدادگر واقعی (Rescue) طی سال‌های اخیر بارها روی سکوی مسابقات جهانی ربوکاپ ایستاده است.
🔹
در رشته شبیه‌ساز امدادگر، ایران ۶ قهرمانی جهان را کسب کرده و در رشته‌های SSL و Rescue نیز چندین عنوان قهرمانی، نایب‌قهرمانی و سومی در کارنامه دارد.
🔹
این نتایج، ایران را در میان کشورهای پرافتخار و تأثیرگذار ربوکاپ جهان قرار داده است.
@amarfact</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/673136" target="_blank">📅 22:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673135">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سنتکام: یک نظامی آمریکایی در شمال عراق کشته شد
🔹
فرماندهی مرکزی آمریکا اعلام کرد هنگام خنثی‌سازی مهمات منفجر نشده یک پهپاد ایرانی که در شمال عراق سرنگون شده بود، یک نظامی آمریکایی کشته و نظامی دیگری زخمی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/673135" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673134">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3YhOhRk2tEujV36MMUTRbwnrhLeEBY6YRND0tGWrGehynnOMJR9OXdcPIW3Z6Fw8t3tOZ-0UlaMplIr-HM9oLjT2SCau_nqSYijBG7xV4r05H1aPJQBqtztIBdMJ9UlEO6Z_k8n06D527UVTZMRNAxcNdFTZgJo4_BknC2S5BoLGNuW8bCXO7I9pc6S7BSlKR1iipqgo_vHH4BOEtlF2ZWyPoSa2JukRRSMedX9R1eaEua_dMAGgzHvSkKBBQJRJ4gQlL-hZi6dMs5VqcCP6TsozO4pFKO26JEhgJozs8rijI2U1yQzwgKkeaGC5r2SmLJrW0mkJTdtFfVXn7pFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای آخرین‌بار در جام جهانی
🇮🇷
نمایش پرچم تمام تیم‌های حاضر با حضور پرچم سه‌رنگ ایران
در مقابل چشمان سگ زرد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/673134" target="_blank">📅 22:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673133">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b5e4e960.mp4?token=rdXSBz7zwVLbEDn9o1WETaN6Tw8a4C_jhTj41l7ctMmCDCxHYy5dCgZ-7CV641NfiTVMtV7ar0zgMDImqLf-_qZmNJAAbK68h-g3pWrb8DcU-LOuaxAAwmclJvNqveGPpma9Zm8o6DjytILDYCnEL_iwB-1TgFuG52G_AYa3ltld_9UNh7A698GAKLzz6Y_USwFIlJ5CXFTOzWyZNjVFJKPudS2upROSqg1oLbu8x-VeimfpIdHnJf8yryOkh2vN8QO5Qpg8Z1vR8ofB3kefAGSbgqT3wbe7sRiLjzBmHFNgclJUj3sNecEs0pBV_qRyXa9whSu_DsUUKgJAMGfQTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b5e4e960.mp4?token=rdXSBz7zwVLbEDn9o1WETaN6Tw8a4C_jhTj41l7ctMmCDCxHYy5dCgZ-7CV641NfiTVMtV7ar0zgMDImqLf-_qZmNJAAbK68h-g3pWrb8DcU-LOuaxAAwmclJvNqveGPpma9Zm8o6DjytILDYCnEL_iwB-1TgFuG52G_AYa3ltld_9UNh7A698GAKLzz6Y_USwFIlJ5CXFTOzWyZNjVFJKPudS2upROSqg1oLbu8x-VeimfpIdHnJf8yryOkh2vN8QO5Qpg8Z1vR8ofB3kefAGSbgqT3wbe7sRiLjzBmHFNgclJUj3sNecEs0pBV_qRyXa9whSu_DsUUKgJAMGfQTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندوه را با هم تحمل می‌کنیم، سختی را با هم پشت سر می‌گذاریم و امید را با هم زنده نگه می‌داریم؛ کنار جنوب، کنار ایران #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/673133" target="_blank">📅 22:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea4ba715d.mp4?token=WF8aPJqOC5sjZS9M2AlBMdwv9usY5pAuqx0PNLvcJEFlfndlNuyVvaz1HvqSZGGX9NDMj-yvT4ZcqLzomCK7DhoxuTul1e00Qc106arXgmVr_54UBf0KodVJuC_dJPuvrEJ4yH15vv5MB4Wra92dxJ84FtLRJcbQRJEuaVB-Htr6RltML89xsDxSIXz7PTNptfb-pc7LbkGXtRBNaMGgErGECSnCgxx_4MX7pj-xtky6pzF5KKFGgW9SMxmM3_cUOlhaP46YCYrK0udSgmZjI_iMhjD9aY2YMTWlDE0m8CCX4ZZI58c2ids3mv8xL16dk5yShNydzF2GLrhpZC-LUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea4ba715d.mp4?token=WF8aPJqOC5sjZS9M2AlBMdwv9usY5pAuqx0PNLvcJEFlfndlNuyVvaz1HvqSZGGX9NDMj-yvT4ZcqLzomCK7DhoxuTul1e00Qc106arXgmVr_54UBf0KodVJuC_dJPuvrEJ4yH15vv5MB4Wra92dxJ84FtLRJcbQRJEuaVB-Htr6RltML89xsDxSIXz7PTNptfb-pc7LbkGXtRBNaMGgErGECSnCgxx_4MX7pj-xtky6pzF5KKFGgW9SMxmM3_cUOlhaP46YCYrK0udSgmZjI_iMhjD9aY2YMTWlDE0m8CCX4ZZI58c2ids3mv8xL16dk5yShNydzF2GLrhpZC-LUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحید شمسایی: در طول تاریخ، خاک وطن را قهرمان‌های گمنام اما شریف حفظ کرده‌اند، مثل همین مرزداران جنوبی؛ ایستادن کنار شما بزرگتر از هر‌ جام و مدالی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/673132" target="_blank">📅 22:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
صدای انفجارها در سلیمانیه عراق
🔹
منابع عراقی از حمله پهپادی به مواضع تروریست‌های کُرد ضد ایرانی در استان سلیمانیه عراق خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/673131" target="_blank">📅 22:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUz1f8lrrbLtu3sWXpwMC5k0svAjLw8_Qy5RipJyK9SEvsOKBzsM7zXJy_UczgrqKDLLhIFLwyo4gcDh5N_pfhWx9wAbGQgu75vBcZAma2DfD45T47IMyUBsnNXgudA2SdcKJPcvyLsXfHhsBmv8OQDVdlczSRBS8-MzUHr-fZYuY-XNmO4k8FE3rITQAZr7GpWBbHAD4GLaG4-wPvqkY5ni5TclZFi3sh3obZFHsn-HHH6KZYqPlNVL-7bnLHbh1vue1TRux1czqP1RTrFr0su9Fh84UzJ9qV1vdd1f15g0GRvbZ4sgoxPjPiRDAVAlpya2TYIMCN5dySG3gUe7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه طور بیشتر صبور باشیم؟
🔹
صبر و شكيبايى گاه در مقابل شهوت و در مسير اطاعت خدا، گاه در مقام پرهيز از گناهان، گاه در مقابل درد و رنج‌هاى دنيوى است و گاه در مقابل پايان عمر و مرگ است.
🔹
براى اين‌كه انسان بتواند در برابر این مسائل صبر پیشه کند باید عقیده قوی…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/673130" target="_blank">📅 22:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd7bbfb25.mp4?token=oVznsjg0HJAJNSiFQF7wjKCyvJtotpWyMBduDOIMV4wT0vdNEe-FwFLwnP0FQjqOAPVzZH3i9MmmMUfUwOK7Bq7ZzZpv4797FQj8U48VKhjq9_MNhjE8xqVBOQJSx81PFgcGdrAirj9rnCj_CQNsiTDkwBRQ14p1R8_hxZO0tS0ChGfH0RKx6avfJHsGpyzlQOcJkw_bkeN7XWjhk9zyKCMc1-0_zRkIuJqw5Pm6ctU-HXWEgEkvfbGrgZaTF7m_6v8EnE3rFBtiEpEde4bOlz0SVTNPDZMtykRjvTA7ujFMQNzftpQl5m-3vC81ESX_ZBxh-lWnQRwqUjU8iBxbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd7bbfb25.mp4?token=oVznsjg0HJAJNSiFQF7wjKCyvJtotpWyMBduDOIMV4wT0vdNEe-FwFLwnP0FQjqOAPVzZH3i9MmmMUfUwOK7Bq7ZzZpv4797FQj8U48VKhjq9_MNhjE8xqVBOQJSx81PFgcGdrAirj9rnCj_CQNsiTDkwBRQ14p1R8_hxZO0tS0ChGfH0RKx6avfJHsGpyzlQOcJkw_bkeN7XWjhk9zyKCMc1-0_zRkIuJqw5Pm6ctU-HXWEgEkvfbGrgZaTF7m_6v8EnE3rFBtiEpEde4bOlz0SVTNPDZMtykRjvTA7ujFMQNzftpQl5m-3vC81ESX_ZBxh-lWnQRwqUjU8iBxbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امتحانات نهایی تمام دانش‌آموزان حداکثر تا ۱۵ شهریور برگزار خواهد شد
فرهادی، سخنگوی وزارت آموزش و پرورش:
🔹
امتحانات نهایی پایهٔ دوازدهم روز سه‌شنبه ۳۰ تیرماه مطابق برنامه در تمامی استان‌های کشور به‌جز هرمزگان برگزار خواهد شد.
🔹
هرگونه تأخیر در برگزاری امتحانات نهایی، علاوه بر فشار زمانی، روند شروع سال تحصیلی دانشگاه‌ها را مختل کرده و اثرات زنجیره‌ای بر سایر برنامه‌های آموزشی خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/673129" target="_blank">📅 22:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBank Maskan | بانک مسکن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2887ed15fa.mp4?token=T6jsFZenoIr2mN1XL6RlpdlDKrsWVgr6C84HL51afz6UgyeFGmCs-XGtxCjCejYnpjuSsDCCxUZGyonZpsfNyg4SNZW4o1Iy0xxXLMDU5o7ECAI7ocjJkQHd4FVEfdKhtSpe4lZRkdfH6F3J4C8zPf-74q6kKqe9JY3w8bCHt_iMgJ18L9dC2d1hUk1hCpNSq1S4CqBtNLyrFjzjkXKk2qA2TIP2EbVPAS-Aeq7_WsFua9rwdS74c7b-V5v5DSVnwFeZLwOKNzT0BJLiAZMUeTZplR22XWG_MbVs6i_1G7N04YMmiEdOaNRx08laC7osvSAtoKGYjOD6WoDZ9Ju0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2887ed15fa.mp4?token=T6jsFZenoIr2mN1XL6RlpdlDKrsWVgr6C84HL51afz6UgyeFGmCs-XGtxCjCejYnpjuSsDCCxUZGyonZpsfNyg4SNZW4o1Iy0xxXLMDU5o7ECAI7ocjJkQHd4FVEfdKhtSpe4lZRkdfH6F3J4C8zPf-74q6kKqe9JY3w8bCHt_iMgJ18L9dC2d1hUk1hCpNSq1S4CqBtNLyrFjzjkXKk2qA2TIP2EbVPAS-Aeq7_WsFua9rwdS74c7b-V5v5DSVnwFeZLwOKNzT0BJLiAZMUeTZplR22XWG_MbVs6i_1G7N04YMmiEdOaNRx08laC7osvSAtoKGYjOD6WoDZ9Ju0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاهی یک جمله، آغاز یک تغییر است...
«زندگی در دستان ماست، اگر...»
ادامه این جمله را بنویسید و در مسابقه بانک مسکن شرکت کنید.
1️⃣
کانال تلگرام بانک مسکن را دنبال کنید:
https://t.me/bankmaskan
2️⃣
جمله خود را ارسال کنید:
https://bank-maskan.ir/j1405
🎁
به ۱۰ نفر از شرکت‌کنندگان، به قید قرعه جوایز ویژه مسابقه اهدا می‌شود.
⏳
مهلت شرکت: ۵ مرداد ۱۴۰۵
⭐
همچنین با افتتاح یا تکمیل موجودی حساب قرض‌الحسنه پس‌انداز بانک مسکن تا پایان تیرماه، می‌توانید در قرعه‌کشی هزاران جایزه حساب‌های قرض‌الحسنه پس‌انداز بانک مسکن نیز شرکت کنید.
ℹ️
اطلاعات بیشتر:
https://bank-maskan.ir/g1405</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/673128" target="_blank">📅 22:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673126">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6dpgD-RwsuvqNIw2vWCye3WMb9Y7eI3FZ_2PAJFVnGzy2Y3R1ZLdAmuSSkXSGBus0R2rmuAm6V7hytH2nsuibDHkFFge04xiJ4wG7sUuWwk4rfmFm_4tcZzc6HNVeLFmUlQjjI_-SOELeG731Iox-VI86_f8o6_kYVQW35fo1pYL04C25jPUb6DIGNfWjtBsjY3N7uL15BF6eLU1AQ2gU0wiBIaQEchYnWEX8FN-cxZBBAjSj3aXbxVJ0YP8PQj-N6h519JVNftbXn9_PdOI2U0uOKNEamQQE9KlyjbhsCp0US_RLZN9sY2twmtc3rQ8IxfL_XWtnbXSkUnTEY_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3jxvKwt-R-OGHiUzNeXR0cGE3cW7YDfYo3EuId16-DRdePgbALGGrPT6wpkfX90YdU-j342gQZbhF-6rPDdzLw6Bzy7bE6ABN_BbP_bEocPKqO1MEBlIQuxH3_wFNaCk_QfLYjiF2mLDO0xZIdAWaTE2E0Ftxw6m-E6yAVTDIKY7KNAIP2JBgsc38zVXQ1tVNMxieTGHF35eD185Ixa198OURs5NeVVmDZY-zGOJjW57F22VPO1NgrpGH5IjV3CXc2qE2Ts--pScqCE0BpwIvBV-HbiiRWdZ3Hb976k5aMruwGFqLizbPtwpmsEFzgvXvzNqNlv7dBk0CVojknepA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمایی از ورزشگاه پیش از آغاز بازی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/673126" target="_blank">📅 22:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673125">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc6300f6c.mp4?token=rXPpaS-2sdMmrCvcn9NRnKPwpX9I1t_bdCYlPHOCC3Eagy2BiuSZ894A8VpWlPbPuCU160pKNr9Qj2I2j_m8S4z95aENy74S1gI0N6rw-_rQgzWRVN35T0slpsAuK6nm0Xxo4T9cm7Dcxj2nKaRlooAKH-KMApqEstDxHtmoPC99pf6r-07Ycf9-hCpy8tF4kt9REj9xbfYEGsSt4p7A87RvvBa3awMAHRkyglgWjLoWs8le7RXv3pG1Slma9CfYjKs45y9KPJQ-kdfpGpcKdq9sxGfgtm8yC1cyhytd7CNrJTs0akCHqVFmCtJRDL8g-gQtDjjGNQCHY-CByPDrTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc6300f6c.mp4?token=rXPpaS-2sdMmrCvcn9NRnKPwpX9I1t_bdCYlPHOCC3Eagy2BiuSZ894A8VpWlPbPuCU160pKNr9Qj2I2j_m8S4z95aENy74S1gI0N6rw-_rQgzWRVN35T0slpsAuK6nm0Xxo4T9cm7Dcxj2nKaRlooAKH-KMApqEstDxHtmoPC99pf6r-07Ycf9-hCpy8tF4kt9REj9xbfYEGsSt4p7A87RvvBa3awMAHRkyglgWjLoWs8le7RXv3pG1Slma9CfYjKs45y9KPJQ-kdfpGpcKdq9sxGfgtm8yC1cyhytd7CNrJTs0akCHqVFmCtJRDL8g-gQtDjjGNQCHY-CByPDrTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود کاپ جام جهانی به ورزشگاه مت لایف با حضور آندرس اینیستا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/673125" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673124">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fabc038fb.mp4?token=lLWfDGouS1xHyhnX8lAHy6Mm1QH-ZQqODZ0L_hevVPKROe933Nd1EhEVuOiwa4OlGt5C34DER67QhstlOPjZL4hmyM-QgMPUlgjVRZKqbqOsf_4AYf-gpPGO9GEGc7R8pVBuLzOX0xiVHW0Vb5ipELDMxR5Fy7jPVgjfzK_LXtVL4CcvCz2J9IQg-_P-ptqZo5lXuJbOS1Q2ySRXLjUpvEQ_Fb9mmvAkdWqJWZ_S9vl-pshWIfTZiPXpQHsgNyAkryhvxwPzLaY1diBw7-0X44G_VLRkyWniksVDQSke-dZRngzIIlLXRnI_n9vgY3QfVLGOa89EiaDCj1LoYO7mOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fabc038fb.mp4?token=lLWfDGouS1xHyhnX8lAHy6Mm1QH-ZQqODZ0L_hevVPKROe933Nd1EhEVuOiwa4OlGt5C34DER67QhstlOPjZL4hmyM-QgMPUlgjVRZKqbqOsf_4AYf-gpPGO9GEGc7R8pVBuLzOX0xiVHW0Vb5ipELDMxR5Fy7jPVgjfzK_LXtVL4CcvCz2J9IQg-_P-ptqZo5lXuJbOS1Q2ySRXLjUpvEQ_Fb9mmvAkdWqJWZ_S9vl-pshWIfTZiPXpQHsgNyAkryhvxwPzLaY1diBw7-0X44G_VLRkyWniksVDQSke-dZRngzIIlLXRnI_n9vgY3QfVLGOa89EiaDCj1LoYO7mOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینفانتینو و ترامپ در ورزشگاه مت لایف ورزشگاه محل برگزاری فینال جام جهانی
🔹
خوک هار از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/673124" target="_blank">📅 22:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673123">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعاها درباره توافق بر سر خروج کامل نظامیان صهیونیست از جنوب لبنان
🔹
روزنامه «معاریو» به نقل از یک منبع لبنانی مدعی شد ژوزف عون رئیس‌جمهور لبنان و روبیو وزیر خارجه آمریکا، به توافقی درباره خروج کامل نظامیان صهیونیست از جنوب لبنان دست یافته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/673123" target="_blank">📅 22:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673122">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9ad63557.mp4?token=Xm3XzzaC6N9-ZxzRDt90vhdLPnD2cZVxhEHdGvO99c3NwAXURdZYpko9AXJNM60I8GDDO5KMbr6dCpvuEGEQoNN9e9QgmH5YH9bHEgC-wgIT2ui1YbplpmndbgzeWDFtaEZWzLlA9D_b3Z2KY9pPk_mm-tu9Nvz2sL7fWTXescroAQnZuU2wJOdNV0wHICPvQ7yOBT53-fZeBqBPmJQyUrG5pWoi2NF9zEaq09poeb_HDMwa79q8tLQPqO-ZR62tO6JQ2cOtOWdbOopU2-ByiBPScx-qmbIFj0sc6qS5tbK4gvPZQUUs66q31l90VcagTqxGnoeMc390EcJG6zGbVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9ad63557.mp4?token=Xm3XzzaC6N9-ZxzRDt90vhdLPnD2cZVxhEHdGvO99c3NwAXURdZYpko9AXJNM60I8GDDO5KMbr6dCpvuEGEQoNN9e9QgmH5YH9bHEgC-wgIT2ui1YbplpmndbgzeWDFtaEZWzLlA9D_b3Z2KY9pPk_mm-tu9Nvz2sL7fWTXescroAQnZuU2wJOdNV0wHICPvQ7yOBT53-fZeBqBPmJQyUrG5pWoi2NF9zEaq09poeb_HDMwa79q8tLQPqO-ZR62tO6JQ2cOtOWdbOopU2-ByiBPScx-qmbIFj0sc6qS5tbK4gvPZQUUs66q31l90VcagTqxGnoeMc390EcJG6zGbVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از لحظات برگزاری مراسم اختتامیه جام‌جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/673122" target="_blank">📅 22:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673119">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRUPfbkBciu3U_kPkb9QQeULg6Ne3K0HfurT0eCtrluT4GqGQsSfwUJqXm9B-Oy4YjliA8sLOwxTTwAyVhN0sSE2uN9gr8DNQJCpv3xR-S3MDM9ScijLtIzWiNlnewvSiP5nMXVwljRt-5JHsJ_AJWmRxvPD3IrqzATekFMrzydHN4yLbDXGT-izdRXS_bxKq_JxBpScSHLfaX3rKice9x9wVuZNlUy3BVgnVoveV5I15dv0RWU50AUvPwLOQqpCQ5PO8ofEXlR5lcxvv-R3RHBJFMIzFMAWPVb-VWs13m5phVGhdmzfhr9C2OgHcJNHuh0mimvPA26dcCS2vpmF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyY0YZOW0KCI4qTb93bQRK5x_WcczQVMhHAG7ISETs60PQAsW_pBC146cleNEqU_7lYLHDmsLK6mQ_XYgSkuhcE7ivA2WzjiUfg5EXhbq0gq8A7t3yBgankpVBQfP1sv-XyFFLA9Qs0eadJn4Nj5pjg2RQKfw202AcR65JMb8qLyOgnjkRh7io3cE-vyxDf1Mtjw0k4bmLgR8O8IhtEIw-znJ9a9nIHramSV9VxZQbhpRQue5Kd7hcpp1KIgO2hykYEGD3TfzfpTvnx_rgR8zaihC2O7zOd0dVijcJvxxNGcmt4sKDgQM5V8t56VrA7JIIGOZolaF2uoD8sWQHhJjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پادشاه، ملکه و نخست‌وزیر اسپانیا تماشاگران ویژه فینال
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/673119" target="_blank">📅 22:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673114">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای
کانال ۱۳ اسرائیل: قطر طرح جدیدی برای کاهش تنش میان ایران و آمریکا ارائه کرد
کانال ۱۳ اسرائیل:
🔹
برای نخستین بار گزارش شده است که قطر پیشنهاد جدیدی برای کاهش تنش‌ها میان ایران و آمریکا ارائه کرده است. بر اساس این طرح آمریکا حملات خود را متوقف می‌کند، در مقابل، ایران متعهد می‌شود به مدت ۱۰ روز دو مسیر کشتیرانی در تنگه هرمز را باز کند./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/673114" target="_blank">📅 22:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673113">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9016aa38ae.mp4?token=CbQIn9hVSjETcAQ0HoK9xiYk6n3o3naSuGayt9WlIM__FopLd_iJuFS-ofhm4foP90rxqorM1TA0H4M-kKcXqcR8Sgt9KHwUUc61sdo8sg9db8QRRKETnvMjl15Ot7GS5hjzFQS8hm3RpLBkZ4N5eQi0zlsv0uJSOWvyIUs4CFe5Hcx43M4XVxruWQdOC2NZKfImB9oW2BKgGkb09AXM7HvFkio69a6FiQhhyMe1pZjKS6BblyQq8QICVk36uo5OUpoF7utVK5PQx_XNk4PIv_fgQrQDyIxPtRxfI_L6Y8pmeh0MD8qNuPE7qHbTxWREpVf3G_kS5jKYy1Pe2USZcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9016aa38ae.mp4?token=CbQIn9hVSjETcAQ0HoK9xiYk6n3o3naSuGayt9WlIM__FopLd_iJuFS-ofhm4foP90rxqorM1TA0H4M-kKcXqcR8Sgt9KHwUUc61sdo8sg9db8QRRKETnvMjl15Ot7GS5hjzFQS8hm3RpLBkZ4N5eQi0zlsv0uJSOWvyIUs4CFe5Hcx43M4XVxruWQdOC2NZKfImB9oW2BKgGkb09AXM7HvFkio69a6FiQhhyMe1pZjKS6BblyQq8QICVk36uo5OUpoF7utVK5PQx_XNk4PIv_fgQrQDyIxPtRxfI_L6Y8pmeh0MD8qNuPE7qHbTxWREpVf3G_kS5jKYy1Pe2USZcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هرج‌و‌مرج در ورودی ورزشگاه مت‌لایف
🔹
مشکلات فنی در گیت‌های گردان، بررسی‌های امنیتی اضافی و دستورالعمل‌های نادرست از سوی مسئولین برگزاری، باعث ایجاد صف‌های طولانی قبل از رویارویی اسپانیا با آرژانتین شده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/673113" target="_blank">📅 22:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673112">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
خوک هار کشته شدن نظامیان آمریکایی در جنگ با ایران را توجیه کرد
ترامپ در  مصاحبه‌ای با روزنامه نیویورک‌پست در دفاع از جنگ با ایران:
🔹
آیا تا به حال از خود پرسیده‌اید که چند نفر در ویتنام جان خود را از دست دادند؟ آیا تا به حال از خود پرسیده‌اید که چند نفر در یک روز در افغانستان جان خود را از دست دادند؟ در یک روز، تحت رهبری جو بایدن.
🔹
ما در مورد دو جنگ صحبت می‌کنیم: ونزوئلا و این جنگ با ایران. این موضوع شرم‌آور است، اما در این مورد، آن‌ها جان خود را از دست دادند زیرا نمی‌خواهند ایران سلاح هسته‌ای داشته باشد و نمی‌خواهند شاهد نابودی خاورمیانه باشند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/673112" target="_blank">📅 22:10 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
