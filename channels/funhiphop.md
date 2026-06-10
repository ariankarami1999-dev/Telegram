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
<img src="https://cdn4.telesco.pe/file/Wnddt4d1UHGbXjSYSQL33owErkEaAUxMdSx03aFpSPMjgVIN0J-8sPQTfo_y7Yxw9BmqaaUaVnTIhEyGtaj5qtaKUjQFMu9bnj6Vqtu-bqYhqjeNrNO1aE_OFf5Uo21W4KfavVRiDrgoZsS5vLV3TtXQO7mbjCrvKvlLgqXaHa9aRW3pXLrZnGVsGMrQClxITzoXAc1_kfm1a1cVoOy2-a7Ilj6M6OWoPPD8HlaYnQm3Np4mq_vCqMn6DLv1Gcvx6d0qCUvFT7gxndjr0k4f-1y0gBfLmYeN55wSkF2gzjPRyjNTcJvdSuCUdvLedpp1riLKOigX4dee9dPySGELrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 06:07:11</div>
<hr>

<div class="tg-post" id="msg-77440">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آژیرها در کویت فعال شدند.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 498 · <a href="https://t.me/funhiphop/77440" target="_blank">📅 06:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77439">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آژیرها در کویت فعال شدند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/funhiphop/77439" target="_blank">📅 05:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی: بسم الله قاصم الجبارین فمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن ۲۱ هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط…</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/funhiphop/77437" target="_blank">📅 05:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=DSbG5dPjpmtJoky6oCThT0GKfG45jVwJUvLS93UUfbfCic5gR19Ftv5bPYDrRZ7V2nNnM97VmkobfYSlT-p7V7tRkKmfwN_TUXQZOmgnKaLE-Vh1QU22cpU_z5zRPUrP2ZXfxITb6h1iKdsvBTcg0xhviOo62qGQJFsVGRFgU8CLPMZ4BUbuYonKBiG8F9uiO3AvZ6LCyD7u_bNu7Rc5HUm63_LGRTy9fGp7Ce1M0y_ojCR445UFpDcARsjoq1eyH_FBR_XDI03hsctDZPFaIjNV2R4tCNkfWVG59N925Ngfi2dui-wgeaIBUf9r3NHMRSMwwC4DN7nxwMV-a56orw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=DSbG5dPjpmtJoky6oCThT0GKfG45jVwJUvLS93UUfbfCic5gR19Ftv5bPYDrRZ7V2nNnM97VmkobfYSlT-p7V7tRkKmfwN_TUXQZOmgnKaLE-Vh1QU22cpU_z5zRPUrP2ZXfxITb6h1iKdsvBTcg0xhviOo62qGQJFsVGRFgU8CLPMZ4BUbuYonKBiG8F9uiO3AvZ6LCyD7u_bNu7Rc5HUm63_LGRTy9fGp7Ce1M0y_ojCR445UFpDcARsjoq1eyH_FBR_XDI03hsctDZPFaIjNV2R4tCNkfWVG59N925Ngfi2dui-wgeaIBUf9r3NHMRSMwwC4DN7nxwMV-a56orw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
فمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ
به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن ۲۱ هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط کردن یک فروند پهپاد MQ9 در آسمان شهرستان جم، با توجه به تداوم شرارتهای دشمن در تکمیل عملیات مقابله به مثل، قوای اسلام و رزمندگان شجاع هوافضای سپاه توسط موشک های سوخت جامد دور برد خود ۴ هدف مهم از جمله آشیانه های جنگنده های F35 در پایگاه هوایی و مرکز فرمانده کنترل ارتش کودک‌کش آمریکا در الازرق اردن را مورد هدف قرار داده و منهدم کردند.
نیروهای ما آماده پاسخ کوبنده و قاطع به هرگونه تجاوز مجدد دشمن هستند و عواقب هر تجاوز مجدد بر عهده دشمن آمریکایی میباشد.
و ما النصر الا من عندالله العزیز الحکیم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/funhiphop/77436" target="_blank">📅 05:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یه موشک بالستیک دیگه از اصفهان شلیک شد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/funhiphop/77435" target="_blank">📅 05:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77433">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه موشک بالستیک دیگه از اصفهان شلیک شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/funhiphop/77433" target="_blank">📅 05:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77432">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزارت دفاع بحرین: تمام موشک های ارسال شده رهگیری شدن.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/funhiphop/77432" target="_blank">📅 05:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77431">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزارت دفاع بحرین:
تمام موشک های ارسال شده رهگیری شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/funhiphop/77431" target="_blank">📅 05:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77430">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">احتمالش بالاست که موشکا وسط راه فیل شده باشن. چون ما تا الان باید گزارش برخورد می‌داشتیم درحالیکه هیچ کشوری تو خاورمیانه هنوز آژیر هشدار هم نزده.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/funhiphop/77430" target="_blank">📅 05:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77429">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجار تو بحرین گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/funhiphop/77429" target="_blank">📅 05:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77428">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poKWBJ3Lf-v2fiBsFAmhvhbd814qqO-9cbe7geCdTTTH7FDdweVnjoVHEqfzU8ZyjPl_nuZT5nMu9T62EX2U696E9Gv7CqP3w9JOo0lPARK18xsTDanlJImxfPoDAxsjzVUmORjUJCfYZbttRVPkJijUYtELsa9Z0DuVhBzg71di17RKT8l9Om1xMVMan4Ps14uphPPkLVUHXxR9m3ymYUOtt5n166b5mkPChUQKnYcI0LntGovPQvnDRQxxA73_K-pqrmkZOGjTGzehIVcwwGXAS2xAmum6-3hA1qnsS0NTx3G3Ec3RKH9eBP6lj648YnkB2fD7t95GoaAdbBSwiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحرین به شهرونداش هشدار داد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/funhiphop/77428" target="_blank">📅 05:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77427">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اوه اوه سپاه جدی جواب داد.
گزارش‌های اولیه از حمله‌ی پهپادی سپاه پاسداران انقلاب اسلامی به مقر کردهای منطقه‌ی اربیل عراق.
🔥
🔥
🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/funhiphop/77427" target="_blank">📅 04:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">احتمالش بالاست که موشکا وسط راه فیل شده باشن. چون ما تا الان باید گزارش برخورد می‌داشتیم درحالیکه هیچ کشوری تو خاورمیانه هنوز آژیر هشدار هم نزده.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/funhiphop/77426" target="_blank">📅 04:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77425">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نخوابید که سلطان بیدار شده  ۳ موشک بالستیک شلیک شده  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/funhiphop/77425" target="_blank">📅 04:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77424">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=Ipi2jFSpyHhMukXOAqoSSPB5ffvsw-peStPOhi_9dKfmpCkMizM_5tetdAf3WCTj80B4ovxEXrASWslRB1bfh9OkfgDcPAN2wS-WaU8m_yzVvvuH1wVeCNwGUyS-nIkxujPgLTY3bOXJhS2LpSIY-o4QPfn1y_7sXCzey8YIGsgTuLcHqYXJg_VwWhjRjtsK0aZsMlO5bv-C_Ii5e4SeW-ECgXVb_GVhuep1BasSsqjmczCT_uzyl6wMWSCnZi_owSvNL4CmfMRnO_7ko4wb2tQo7NdI439RuinGWmmN-JhjWchdBk27l3QWqJdzq-6909UqPBkl7faghrmvj-9yyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=Ipi2jFSpyHhMukXOAqoSSPB5ffvsw-peStPOhi_9dKfmpCkMizM_5tetdAf3WCTj80B4ovxEXrASWslRB1bfh9OkfgDcPAN2wS-WaU8m_yzVvvuH1wVeCNwGUyS-nIkxujPgLTY3bOXJhS2LpSIY-o4QPfn1y_7sXCzey8YIGsgTuLcHqYXJg_VwWhjRjtsK0aZsMlO5bv-C_Ii5e4SeW-ECgXVb_GVhuep1BasSsqjmczCT_uzyl6wMWSCnZi_owSvNL4CmfMRnO_7ko4wb2tQo7NdI439RuinGWmmN-JhjWchdBk27l3QWqJdzq-6909UqPBkl7faghrmvj-9yyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا همش برنامه امریکا واس جام جهانی هست ساعت خواب ها با امریکا تنظیم شده دیگ میشه راحت بازی هارو نگاه کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/funhiphop/77424" target="_blank">📅 04:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77423">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نخوابید که سلطان بیدار شده  ۳ موشک بالستیک شلیک شده  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/funhiphop/77423" target="_blank">📅 04:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77422">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بزارید سید مجید نقطه زن بیدار بشه تلافی میکنه امشبو</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/funhiphop/77422" target="_blank">📅 04:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77421">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حملات هوایی امریکا تکمیل شد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/funhiphop/77421" target="_blank">📅 04:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77420">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حملات هوایی امریکا تکمیل شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/funhiphop/77420" target="_blank">📅 04:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77419">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا می‌گه ما پاسخمون دادیم تموم شده رفته شما داغ بودید نفهمیدید: در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانه واهی سقوط بالگرد خود، برخی از پایگاه های آمریکا که در منطقه که نام نمی‌بریم هدف هجوم قدرتمند ارتش قهرمان…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/funhiphop/77419" target="_blank">📅 04:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77418">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا می‌گه ما پاسخمون دادیم تموم شده رفته شما داغ بودید نفهمیدید:
در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانه واهی سقوط بالگرد خود، برخی از پایگاه های آمریکا که در منطقه که نام نمی‌بریم هدف هجوم قدرتمند ارتش قهرمان جمهوری اسلامی و دلاورمردان سپاه پاسداران انقلاب اسلامی قرار گرفت.
ارتش جنایتکار آمریکا بداند در صورت تکرار تعرض به جمهوری اسلامی ایران، حملات سهمگین و گسترده تر علیه بانک اهداف تعیین شده در منطقه انجام خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/funhiphop/77418" target="_blank">📅 04:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77417">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f906ee6c6a.mp4?token=g2zpWsTpa44Ch2Eq5fOARHLAWsHhySyYPPy-roYEdvgVF4DRK2kzSbvyPDE4YhanebZ8rHMmW_W8ZxK0NDp6Z6RW9SUwApdnoqup8MYeFc66Vv5hokXJ4luJQmzFFgaB-4d8QvwEGnWkBVb_EBrmvuNEJ217ar7qX6EbfE3Zh2mS9gC8NQfPld-O9YtZ-3DaVG0PAV4wL2XiY2abudMTa7jqg7M06zRrjYzzj3Y_RnP_8-hEW4LALLdGNiGqAMQkQm7Jch8WgicibNiCmCOwwKtINjiYWgvMw_WEYubrVOVWp0UFwJi1WbwyXH_I12RrKAwK3qmHvSCWKp7AuAXTKQ0HfLcfodeZ_mcBwZO2Yw-aFQZF_TCuWMdE61UWW7y-8s5DZqteVPsb2AS6L4IpzRYC5uyzY7YPAQ3bahMTLdQIBEUJIOL6RQrMRGorLDlhG2g1_KZwoG4XRb2KR_N9eOBd4dFgZvVEjXhM3pyNb94YxJdeWvF8Mevxf9RVHsYDhHUnDsYvgpC2rMBOIty8W4zIQGA0cXEtRNIi6BAqMW9nAi7fsPOZFo8MN_674IUjP6oOa1tGzVmynvThkSxU46pM36934ZArCFrmsFAB-5mBTE9i-9EMeB6B05TDspEUjGQOyUamaAJb8yw06mT8d4btDP-HUsyP50Yw959sr_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f906ee6c6a.mp4?token=g2zpWsTpa44Ch2Eq5fOARHLAWsHhySyYPPy-roYEdvgVF4DRK2kzSbvyPDE4YhanebZ8rHMmW_W8ZxK0NDp6Z6RW9SUwApdnoqup8MYeFc66Vv5hokXJ4luJQmzFFgaB-4d8QvwEGnWkBVb_EBrmvuNEJ217ar7qX6EbfE3Zh2mS9gC8NQfPld-O9YtZ-3DaVG0PAV4wL2XiY2abudMTa7jqg7M06zRrjYzzj3Y_RnP_8-hEW4LALLdGNiGqAMQkQm7Jch8WgicibNiCmCOwwKtINjiYWgvMw_WEYubrVOVWp0UFwJi1WbwyXH_I12RrKAwK3qmHvSCWKp7AuAXTKQ0HfLcfodeZ_mcBwZO2Yw-aFQZF_TCuWMdE61UWW7y-8s5DZqteVPsb2AS6L4IpzRYC5uyzY7YPAQ3bahMTLdQIBEUJIOL6RQrMRGorLDlhG2g1_KZwoG4XRb2KR_N9eOBd4dFgZvVEjXhM3pyNb94YxJdeWvF8Mevxf9RVHsYDhHUnDsYvgpC2rMBOIty8W4zIQGA0cXEtRNIi6BAqMW9nAi7fsPOZFo8MN_674IUjP6oOa1tGzVmynvThkSxU46pM36934ZArCFrmsFAB-5mBTE9i-9EMeB6B05TDspEUjGQOyUamaAJb8yw06mT8d4btDP-HUsyP50Yw959sr_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیکرها با استناد به منابع معتبر سیزن آخر ایران رو اسپویل و یه فیلم از شبیه سازی انفجار یه بمب اتم تو شهر وسط اخبار صدا سیما پخش کردن.
🙏
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/funhiphop/77417" target="_blank">📅 04:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77416">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اهواز رو هم زدن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/funhiphop/77416" target="_blank">📅 04:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77415">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اهواز رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/funhiphop/77415" target="_blank">📅 03:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77414">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">صدای انفجار تو برازجان گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/funhiphop/77414" target="_blank">📅 03:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77413">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش‌های اولیه از پرتاب موشک‌های کروز ضد کشتی ایرانی از بندرعباس به سمت ناوهای آمریکا.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/funhiphop/77413" target="_blank">📅 03:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77412">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شین: سه موشک شلیک شده  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/funhiphop/77412" target="_blank">📅 03:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77411">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
آتش پرقدرت پدافند مقتدر و یک پارچه‌ی نیروهای مسلح، یک فروند پهپاد متجاوز و متخاصم دشمنان جنیاتکار را بر فراز آسمان امن جم در استان بوشهر ساقط کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/funhiphop/77411" target="_blank">📅 03:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77410">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صدای انفجار تو زاهدان گزارش شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/funhiphop/77410" target="_blank">📅 03:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77409">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ایران بالستیک شلیک کرد   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/funhiphop/77409" target="_blank">📅 03:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77408">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ایران بالستیک شلیک کرد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/funhiphop/77408" target="_blank">📅 03:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77407">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بندرعباسو دارن بد میزنن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/funhiphop/77407" target="_blank">📅 03:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77406">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جم تو استان بوشهر رو زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/funhiphop/77406" target="_blank">📅 03:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77405">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک مقام ارشد آمریکایی به کانال ۱۲ اسرائیل گفت که موج سوم حملات به ایران اکنون در حال وقوع است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/77405" target="_blank">📅 03:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77404">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بندرعباسو دارن بد میزنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/77404" target="_blank">📅 03:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77402">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدا سیما:
حملات امشب آمریکا تو سیریک به دوتا مخزن آب بوده.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/77402" target="_blank">📅 02:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77401">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWNJ_hmcuwLnqI1EtU8zNdrexv8HTPnpLB_QQ2tLLs9Hs_cpRFMBfbJQaJIjYCgsE7gHfLzvAEmXVl8Wicqq9zVgTFhJuRIr2yHQm7rmfffFMjHuW__d9xD2U_y_4-D4pAwhcNNQPwmDpbCuhOzp0-q4y9uS7rwxUsXDkQpVukbZbAZ9NzmyrQAwsCHx80HA8VssLVGOKwPjaXqhxbz_VEnWA574D6BrMd09H03yYk0imscfY2rebsrydgKwbHJGYxzZm8vyw0QpnqExHvJGPLJ6MBdKzQjaa3ZZTTZZbSoGW01kSPBd-7gKUBBKtHmApqLWosoNJTH8_tHadPfo8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور عراقچی می‌گه جواب می‌دیم و تنها راه در امان موندن سربازای آمریکایی اینه که از خاورمیانه فرار کنن:
با وجود شکست‌های آمریکا در میدان نبرد، آمریکا تصمیم گرفت عزم ما را آزمایش کند.
نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نخواهند گذاشت.
اگر می‌خواهید در امان باشید، منطقه ما را ترک کنید.
تاریخ خلیج فارس فصل‌های زیادی درباره سرنوشت‌های تلخ متجاوزان خارجی دارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/funhiphop/77401" target="_blank">📅 02:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77400">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رئیس مجلس نمایندگان آمریکا درباره ایران:
یک حمله دفاعی انجام شده است — این حمله متناسب و محدود است.
این حملات هدفمند به سایت‌های رادار، موشک و فرماندهی و کنترل بود — ماهیت آن دفاعی است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/funhiphop/77400" target="_blank">📅 02:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77399">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اسرائیل هیوم:
ارزیابی مقامات اسرائیلی این است که حملات آمریکا آنقدر حجم زیادی نداشته که سپاه برای تلافی به اسرائیل حمله کند.
احتمالا حملات تلافی جویانه ایران محدود به کشورهای عربی خواهد بود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/funhiphop/77399" target="_blank">📅 02:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77398">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یک مقام ارشد کاخ سفید به پولیتیکو:
ترامپ همچنان معتقد است توافق صلح با ایران نزدیک است، حتی در حالی که ایالات متحده امشب حملات تلافی‌جویانه‌ای علیه ایران انجام داد.
این مقام گفت: «هیچ چیز وضعیت کنونی توافق را تغییر نمی‌دهد.»
این مقام تأکید کرد که توافق با تهران «هنوز نزدیک است.»
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/funhiphop/77398" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77396">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ای مو موردوم سپاه هم داره کردا رو میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/funhiphop/77396" target="_blank">📅 01:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77395">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">روسیه 6 تا اسکندر زد اوکراین
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/funhiphop/77395" target="_blank">📅 01:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77394">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عربستان ----» یمن
پاکستان -----» افغانستان
ترکیه ------» کردستان عراق
آمریکا -----» ایران
اسرائیل -----» لبنان
یک شب عادی در خاورمیانه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/funhiphop/77394" target="_blank">📅 01:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77391">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هیچگونه انفجار یا حمله‌ی جدیدی در بحرین یا هرمزگان یا لبنان گزارش نشده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/funhiphop/77391" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77390">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">CNN:
یک مقام آمریکایی گفت که حملات اخیر به عنوان یک هشدار به ایران در نظر گرفته شده‌اند و انتظار نمی‌رود که تلاش‌ها برای مذاکره به منظور پایان دادن به درگیری را مختل کنند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/funhiphop/77390" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77389">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجار هرمزگان
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/funhiphop/77389" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77388">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صدای انفجار در بحرین
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/funhiphop/77388" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77387">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مقام آمریکایی به فاکس:
حملات هوایی علیه ایران «در حال انجام است» و اهداف شامل سامانه‌های پدافند هوایی و تأسیسات راداریه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/77387" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77386">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سپاه: بزودی تاسیسات نظامی بیکینی باتم را مورد حمله قرار خواهیم داد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/funhiphop/77386" target="_blank">📅 01:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77385">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این تو بمیری دقیقا از همون تو بمیریاس
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/funhiphop/77385" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77384">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه: بزودی تاسیسات نظامی بیکینی باتم را مورد حمله قرار خواهیم داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/77384" target="_blank">📅 01:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77383">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پاکستان هم افغانستانو زد
🤣
🤣
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/funhiphop/77383" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77382">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جنگنده ها از فرودگاه مهراباد برخواستند
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/funhiphop/77382" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77381">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سد مجید :
و ما النصر الا من عند الله العزیز الحکیم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/funhiphop/77381" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77380">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR5sGEKqDkaahMzAhoVeztCb02hOVGEJfTdrvYtiaz4fDiywuabqdxkSLq-YWRH-rzZXAZ-UBO0Vrvrg7EOsmHbTkLW0xf5XjUEjGpQ57IW4Jojndwvr8lztPyjnwToa4eU8QjxJxKfe8F9Z_lo_2yExysDgcTi_xPQNkbaSwU6Xe1UoTKZFH2kzdcwqoaQh_RAmQOAyJUFBJsRGs8INxzOX2X4LQmDdbX0lHXHVjHk_HV2iZX8C7ukM572j5FXmBiGQaTXIuCMRyzixRoAw_g-1wHtBFu2dcJg_wkuTScME2MwPtanyk5dloJ-3cgzbwSe9I9YxxCiI-hVc-nsCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمون ایران سوریه و لبنان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/funhiphop/77380" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77379">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تو این هیروویری اسرائیل بیروت رو زد که ایران به جفتشون پاسخ بده تا شاید آتش بس نقض شه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/funhiphop/77379" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77378">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قطر و کویت حریم هوایی خودشون رو بستن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/77378" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77377">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">لبنان رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/77377" target="_blank">📅 01:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77376">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هگست الان زیر بغلش تموم شده داره بارفیکس خلبانی میزنه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/funhiphop/77376" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77374">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حوثی ها: مالک گپ مگام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/funhiphop/77374" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77373">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تسنیم:
ایران همچنان که ساعاتی پیش نیز هشدار داده، پاسخ قطعی به تجاوز آمریکا که به بهانه سقوط هلیکوپتر آپاچی انجام می‌شود، خواهد داد.
@FuunHipHop
| Nima﻿</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/funhiphop/77373" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77372">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صدا و سیما:
پاسخ های ما تا دقایقی دیگر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/funhiphop/77372" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77371">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فوری از علیرضا تنگسیری، فرمانده نیروی دریایی سپاه:
سریعا به تجاوز آمریکا پاسخ خواهیم داد!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/77371" target="_blank">📅 01:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77370">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ به آ‌ب‌ث نیوز:
فکر می‌کنم پاسخ دادن بسیار مهم است. آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم.
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، و من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد، و این همان چیزی است که این پاسخ نمایانگر آن است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/funhiphop/77370" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77369">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجار تو میناب گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/77369" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77368">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هم اکنون جلسه اضطراری شورای دفاع به ریاست علی شمخانی در حال برگزاری است
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/77368" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77367">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ارتش امریکا از شلیک چندین موشک کروز به سمت ایران گزارش داد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/77367" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77366">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الان ترامپ زنگ میزنه به خودش میگه حمله رو متوقف کن چون توافق نزدیکه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77366" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77365">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سنتکام اعلام کرد که حملاتی را در قالب دفاع از خود علیه ایران آغاز کرده است؛ این اقدام در پاسخ به سرنگونی یک بالگرد آپاچی آمریکایی در روز گذشته صورت گرفت. این مأموریت، پاسخی متناسب به تجاوزات غیرموجه ایران است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/77365" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77364">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">درود بر فرید جان عزیز بندر عباس یه صداهایی میاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/77364" target="_blank">📅 00:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77363">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرگزاری دولتی مهر:
شنیده شدن صدای انفجار در منطقه سیریک، استان هرمزگان. ساکنان محلی از وقوع چندین انفجار خبر می‌دهند. مقامات رژیم اسلامی هنوز درباره علت آن اظهار نظری نکرده‌اند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/77363" target="_blank">📅 00:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77362">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دیس جدید شایع به اسم عصبانی 2 ریلیز شد    Youtube  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77362" target="_blank">📅 00:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77361">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دیس جدید شایع به اسم عصبانی 2 ریلیز شد    Youtube  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77361" target="_blank">📅 00:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77360">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiy1FaM6bxA-1FgJzVI4N93R8yaaSGRxPm4jK3rW0xL78SNPIpY7ZAG12PV636_0mjS_-f7WZwuxbtq2sYOirTEvRiwKKGCIFK-I_sEYxL_3xAC9LsIbLqYcm0i1pzPatf15mf0oT3KxYMx8QRhtZJeSdEAsmoHFIJrwM-b8iNyiy0luAcIl5Ur9yk--kzKFYGVBv9jx1npGy4DGQOvuYAFO5BUnZAeTltTc6KfPVfmD_GS6RKnqb-wbl7OcWqsJ5MhRC66oCFibimAEj3YdjDaQaLq-g8pmtiUcEOUrR6e70TNqRKe4u9sK1d4t9zGVpVQjWxPKltA_joQdiAIBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس جدید شایع به اسم
عصبانی 2
ریلیز شد
Youtube
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77360" target="_blank">📅 00:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77359">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntkYhm3oX3apqL3xfJK4M56MvjIXnLvkIsU4nNePnpXhqu50OmONBD7Sw4u3_hXT8Lh3dsLfizVOKFg6U6y-qGG5AueoOu865f7CsvPFY3w8Jtk2xJdp-lLen5OZeJCI5z06vNsIrGeUN3XUwS8cu6iW2Rx-qR3EMOP8DntqinxOOGpacHVXO7cQEoKPPFyt8Sf-SNBpNo7n4v4bkZ9kqGuMoY0k7U1NTizEeHnH2pxmDYEtr8D8sdvBuaVMpzK6HEznTwYA9kgevwAAoh9hRSEOuMprIMOkZtrF3dgp1jfoPFwLO3jnw9y0nOVsTHrxMoNf-IScsfeYVZmpmJAl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاشیدم به در و دیوار
معاون دکتر عراقچی در مصاحبه با الجزیره:  ایران پشت حمله به بالگرد آمریکایی آپاچی در بالای تنگه هرمز نیست.  این احتمال وجود دارد که چنین حوادثی به دلیل فضای پرتنش در تنگه هرمز به صورت غیرعمد رخ دهند.  هیچ هدفگیری عمدی از سوی ایران علیه…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77359" target="_blank">📅 00:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77357">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNhgNiu6rc5xjIdn2_vAjPqx6tJtLdN12-KNnNXnpadZJs-U5RQRk40c9i0aUnysaz--eLMEoJce-o0OvLNA9ifW9VcbdvTt8V5qiqkLltx_luPTxzmSZ7CG7PizKIFMEn4CtLRCFzTrAR0cEZcJwMwhuBbeuQpeF_7zNBf39H1QhhIzFhyLrFYnhBXcWmDSK19TgfF8KJ4-0kL6oZQ13gYhvaqT7v_RNnI8gqPNDWYioIniZup64vSttIdyQxlvgqXGzot2uUEFlBCf_UOhQtdclmHLxcCfhSHj7zjYnvloUJTqCDiHxKOv_vpcSURLPxz_raheM-y-4BvDq8Q_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ورزش:
به قلعه نویی دستور دادیم اگه وسط بازیای جام جهانی کسی پرچم های غیر رسمی (مثل شیر و خورشید) رو بیاره یا شعاری داده بشه سریع بازی رو متوقف کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77357" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77356">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ به وال استریت ژورنال:
حادثه هلیکوپتر آپاچی موضوع بزرگی نیست و خلبان حالش خوب است و مادر بنده هم جند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77356" target="_blank">📅 23:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77355">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پاشیدم به در و دیوار
معاون دکتر عراقچی در مصاحبه با الجزیره:
ایران پشت حمله به بالگرد آمریکایی آپاچی در بالای تنگه هرمز نیست.
این احتمال وجود دارد که چنین حوادثی به دلیل فضای پرتنش در تنگه هرمز به صورت غیرعمد رخ دهند.
هیچ هدفگیری عمدی از سوی ایران علیه بالگرد آمریکایی در بالای تنگه هرمز صورت نگرفته است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77355" target="_blank">📅 23:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77354">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLRDkD2OqbTZ2v6tCHBVLlVxa_XNvkYsTKHrO5xu_o-zIqLivllCY0QDPV1cygmXiuELYtFd5pm1Roa0ld3b4LHjlzuB1GjEiXgeqHmxP-H0f-DmD7LtXHdBboSrzXIrDeW1qfrTjBefUW6uA3CLUAEyuWqN7_tXq5HgEJlEtVxxJ-d6_M6yXtGqJb_gYnO34NKB0KRuztor0f0U-Y647QGaHYlRWKaGaruY69UoILrncjZA4KscYbF-Gj3qqU8LlcXqZXF6QsaI_IeEQsEBR72LMxwV9c0EaZEJdA0WYAwQ1-nseaQHHY4YoBqGlC7E-9edWbMU7e6fN5PlQsGDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77354" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77353">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF1-91u8vwDRGJrvUlEbqtXkq5eGsk7CIlNaBgSueRcnnLnvqBTm3W_5pCrB8skDeeUqHQnuDx6VB79qxjBc1_9jSy-yb3d97SzweIA-E6XlSx4L2mIoavpQFyXLCAuZudJkLg75xvcNOfMkcrum4bjjbio_zz44dfGvHsG7GZXySh2wjoarc7LvkeIvx6uLQbPXbqYfAm2j8M04V9ZysaYbnyjIGYJ0WbXPoPidIysPrSsiG5Kjs_QWyL5uRyAPpGxwvaAmoTecJfG4Rp1jmsfbiBErRZDnHD9nM0alMOe5Iw9exFv5ECMPwjBhGF_8Ly3eqarY5-CzmquMGlvU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلایه ی پزشکیان در توییتر از نحوه ی مدیریت جمهوری اسلامی و سلطه ی سپاه بر کشور.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77353" target="_blank">📅 23:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77352">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxd6rrP4zKmVCHjNe0LZg0YxULbIyMXqg4GgEgiTXoAQUxoHoWetgwAhRmqi4JO9uOBviIYrdvj2VaMbyWdrA4WdXXeX_lU0k4p0z-CG4S8gsDNlqpXrOQYW8QO15tKe0OZvxysMP369UUOwutmDKFcbeR4LZyEyPLAM_GAI4MSYMRMidS_ZBLykEL8rxSN3fvn7k8W2Wfsv0tNK8qfLvtlL_14dpr4gu89nZFwuM-C74r5-y3iUeRAhpbaeJ32DUAWI7jbbgODZ2JBKP4gsMedS9VLa0kF4zUPj_I-sCKnAnIe-vXljtnj0p5ja6HqQFjAjV92v3bkEQII9OaWUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلایه ی پزشکیان در توییتر از نحوه ی مدیریت جمهوری اسلامی و سلطه ی سپاه بر کشور.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77352" target="_blank">📅 23:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77351">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">داش بمولا این سری، این سری دیگه میزنن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77351" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77349">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خب امریکا میخواد بزنه ولی ازونجایی که ترامپ دالگخیزه تبادل اتشی بیش نیس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77349" target="_blank">📅 22:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77348">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNCPU1IdRxZgdD6DpUTDCYAa8R4OxYCxGQ8Bn-wBGg7zxs9VZOlibbJs1gnlYr-OZx5i0KPlwIERb2chiVLSYNFmEuzKFbe39fPYEaxFfILnTHckZ3-OfbHA19iG3-Rm2E1J2niaaHExDeM6RPvzvVwOY66-dIyogfxu4VDflWxOQ9n74nGPXhQMfYrpummNHQ_Sa3IKHeLhu2pN_RnHqTaZNe4EyAgmUxMt0UsTgSe8xcoxBMJus2BgJBVitMqtEve08d0HHo9Qwps_288XoKdLA0tyMYs7aIs6Vv5fEA-RFsE-gL6Hh-YHERf53yKK7639k0A7tbPa6UGpURUe-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77348" target="_blank">📅 22:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپارس شو</strong></div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77347" target="_blank">📅 22:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77346">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRCjKE4ttkBZu1lBUUggswgBB5Q3r5KoepfZsWUDV7rQOLWfV_mBzZ10QKmUN_wkcm_MfhH4K5XsEx3ncocEkz7joubgq836phUdM1Plf-3S1lE47kZRKrieiwffyKMwfaxo3Az7gVvcOmEAsdNEBhGVLKm7kGoy_GT7hVjqnlhkWsa35S5jnBxi-bYAIq646Tagb-WM1P_RQ8dxlcv7d0jvhAE2qEaVS4DA2ViQTbmsF5c6L2LWDOa-eA7MvOxyW1RR3vP-dXHjXK7Htl6-C1pDY-qZ83OVzhXUIAkpkQjSEog2n0kI9uzYQ-BSZSXvAJ3GuLSDP2yjkI9JGF85TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرت مذاکره:
نیروهای خارجی در نزدیکی قلمرو ما به دلیل اشتباهات انسانی خود، حوادث ساده یا احتمال گرفتار شدن در آتش متقابل، همواره در معرض خطر هستند.
برای کاهش خطر، بهترین راه حل این است که آنها منطقه را ترک کنند.
ما زبان دیپلماسی را ترجیح می‌دهیم اما به زبان‌های دیگر نیز صحبت می‌کنیم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77346" target="_blank">📅 22:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77345">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ به ABC : اگه یه عده بخوان احمقانه رفتار کنن
ممکنه کار به جایی بکشه که مجبور بشیم کل زیرساخت‌های یه کشور رو نابود کنیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77345" target="_blank">📅 22:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77344">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوسی خبرنگار فاکس نیوز: «او در دفتر بیضی شکل بود و از او پرسیده شد که آیا خط قرمزی برای از سرگیری یک جنگ داغ علیه ایران، کشته شدن نیروهای آمریکایی خواهد بود یا خیر. و او گفت که این دلیل خوبی برای از سرگیری عملیات نظامی خواهد بود.»
«در اینجا هیچ نیروی آمریکایی کشته نشد، اما به نظر می‌رسد ایران واقعاً، واقعاً تلاش می‌کرد نیروهای آمریکایی را بکشد چون یک هلیکوپتر آپاچی را سرنگون کردند.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77344" target="_blank">📅 21:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77343">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آکسیوس کاملا روانی شده:
نتانیاهو پس از سقوط هلیکوپتر با ترامپ تماس گرفت و از او خواست به این اقدام ایران پاسخ ندهد و حمله نکند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77343" target="_blank">📅 21:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77342">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرنگار فاکس نیوز گفته رئیس‌جمهور آمریکا در آستانه دستور دادن به یک انفجار بزرگ در ایران است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77342" target="_blank">📅 21:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77340">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پرز برا آلوارز پیشنهاد ۱۵۰ میلیون یورویی فرستاده</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77340" target="_blank">📅 20:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77339">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پرز برا آلوارز پیشنهاد ۱۵۰ میلیون یورویی فرستاده</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77339" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77338">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69d28ab16.mp4?token=NgmxtmB1Y2BrQFuRafTNr9RtNuDKeJiaE3quZHVsmA1hA3lv4OuRAuabhsS-UGi4TS7tbf86yb3GfkyoZZ7b_NHJScsnSMFvC3faJnqNqqjnxOETXUfzUvmmjwrr9PATZbN3dMLqInW-M9n0RdvodEYMTNTeZ-qjVSzZ0ryIFRXuNcWJhCm3_ICFPVtOZiHFWpxgeuWrER2f8pLe_GBvY3Akf3RMd-E9fh2Eax_LDhbZfbGf_X3gmwG-67F9WHlRQ7ikD2WzW41HtGycub4JY50_943-bW8U3FiWhXAm7JcrJ-grD3SZEvJoAMd4SpMjGuEAolNiikk_d-bJHFCPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69d28ab16.mp4?token=NgmxtmB1Y2BrQFuRafTNr9RtNuDKeJiaE3quZHVsmA1hA3lv4OuRAuabhsS-UGi4TS7tbf86yb3GfkyoZZ7b_NHJScsnSMFvC3faJnqNqqjnxOETXUfzUvmmjwrr9PATZbN3dMLqInW-M9n0RdvodEYMTNTeZ-qjVSzZ0ryIFRXuNcWJhCm3_ICFPVtOZiHFWpxgeuWrER2f8pLe_GBvY3Akf3RMd-E9fh2Eax_LDhbZfbGf_X3gmwG-67F9WHlRQ7ikD2WzW41HtGycub4JY50_943-bW8U3FiWhXAm7JcrJ-grD3SZEvJoAMd4SpMjGuEAolNiikk_d-bJHFCPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دالگخیز ۳۷ بار توافق با ایران رو «قریب‌الوقوع» اعلام کرده، اما هنوز هیچ توافقی حاصل نشده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77338" target="_blank">📅 20:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77337">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JC6g0YvhfFNAvCzv6ccFCU2hU8cNcOpSkuiyig9V26oFy0TUb9MOeZHVTKldalu60NX5ffeKsHo8-ycc3QW3E1S_ofnu9pYJ9xhv4KeETo51S448n4DBjmbFX65sddwn9zUd25qcHRo3hlcqUNxjXnPqZ6RqfFZNLo_npLtJUsLIxj2fEs3wak1C6EvIYzwP0oBQSX0cHdgFeI-L692sRZ4MbZYjeAWjhj5sHSUBXk9cII8CjnhX9eSlCas__EOI76YZSeipWgn2HSJl1NiFU-GpgOkpZD_KSvpPlEgokrYQpYcVgp_rLNTi6cCpmG6Ot8xZrYRU_0dFZKahz6iTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالگخیز:
ارتش بزرگ ما به من اطلاع داده است که دیشب ایرانی‌ها یکی از هلیکوپترهای آپاچی بسیار پیشرفته ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند. دو خلبان در این حادثه دخیل بودند که هر دو سالم و بدون آسیب هستند. با این وجود، ایالات متحده، لزوماً، باید به این حمله پاسخ دهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77337" target="_blank">📅 20:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77335">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kzit9HgOsUGaNqB8e5ZNH7bwUTvioR5G8L5yXsD0lnggsWBofGBR4GfhBXLWbjEYY_2U4ohSYaOB6SPteUa4VhTwU58JVmTC0CakJJmtAkSAq0QrCYU9q_xU6fNPJNyWZGh-XvOwCRL3VuJNuN_5aoAyHElhBBAvEm0R3D09LeYVA2_Ix7-uZ7hqx-FvH-0J0P-eNNV7nQZeMmlDlvHSpNcUbYzigWumkvx7JmMODoCrPfzuXVvtRaCHamg10sHXLpDh-lymc5TtWO-IU1SmnVZLOps8HM4vZZAswDCMSSPV-s2uMhssy3Raw6kfjFgJVj0BxT6BoyBufNYocoi2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپر تخفیف گیگی ۸/۵ رو از دست ندید
❤️
🚨
0️⃣
1️⃣
گیگ 100 تومان
0️⃣
2️⃣
گیگ 200 تومان
0️⃣
3️⃣
گیگ 300 تومان
0️⃣
4️⃣
گیگ 400 تومان
0️⃣
5️⃣
گیگ 500 تومان
تخفیف ویژه
0️⃣
0️⃣
1️⃣
گیگ ۸۵۰ تومان
مدت محدود
🦋
سرعت عالی
🫶
بدون قطعی
🫶
با لینک ساب
❤️
📩
همین الان پیام بده
@wevpn_admin
🦄</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77335" target="_blank">📅 20:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77333">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کان نیوز:
تو درگیری اخیر آمریکا به ایران ۳ میلیارد دلار از طریق یه پرواز از مبدا قطر که تو تهران فرو اومد پول داد تا دیگه به اسرائیل موشک شلیک نکنه و آتش‌بس کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77333" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77332">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه این پیام بماند به یادگار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77332" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77331">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه
این پیام بماند به یادگار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77331" target="_blank">📅 18:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77330">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMnkKRzTyiQA2_VkEcJtDZUER5CT-11Q9oNvHIsAKAqdWQ1wEyATHq9-Lbc3q5Mtudd-DZv3s-8Wj1KC495_XsKocSuo-RHxoKUcK4Y1Ve--fG1DC8keBii3qXy07_ZOwSyN-XYWonCNe7Gyygq2Vv-XmiWJOUkc-w3JDDk_GOehve9RIH2rypdv-QrUfaN_9a7GdbRFDM64QbVfF2zERaZUoIgEUGwi2RMTA0nK-Ig5btzja-8vFcuy9JWQK_4s4NS2ar0nh5opAft4BItT_NsKRlYKX_o3nGUfhNGzAXA-6mPcKMDRYmeIQbVVx22-zMFqjSOT1dwklq08Asn7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد مهدی طارمی و رونالدو توی جام‌جهانی 2022 :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77330" target="_blank">📅 17:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77329">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77329" target="_blank">📅 17:53 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
