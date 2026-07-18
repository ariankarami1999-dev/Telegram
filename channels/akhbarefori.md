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
<img src="https://cdn4.telesco.pe/file/XsC6sW3Ug4EOkokJQpk_lMnxVg9_YQ0I4pzD-VZsv1pRr7dvE1TahgD4Brr_EZbxf47ZbsGbKd6K3AgHnImN6wUt4VZ8nGqlOmHEzKTUptt3oEB0AKU-HeL5Y3YLeB2LZFRCGsSul7ZKgIuELS1FMsDvFADoh8vOcBlxewx5omDIpF3zoCBX5L24X2lIlHRzrauF6-Oy_y-TaId4HRaV0aZ_BhaWIQFaZfbWE-ppm8oatz-G-iUXwNWAN2EOByoXic-e4iwxL3e4J-yaM24SeLM9YrsMiMBJ1oDPCdQG5FNx56XGii6V83gZKJ4CIEfKrnDOWIzqkTakku2YyHnuVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.29M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 19:15:34</div>
<hr>

<div class="tg-post" id="msg-672644">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPPVajg6KzFwSTfb22Lx5XG2IVhssoFHpw_eep_9VhX_1X_0bePnhSchWwwq2fct_ognTwNzwWxaSa6hvq-DN2dIifjsqf0BMweIiK5IeJYgB9y07vNwiVCMosRNms6yQytPrFpUHdTbQcNpy6kanNE6tj3ssICGmQYYUkc_BH3EcBawiRlkxBB1wtsTl3OH4Z22iWruKdCNrf5sC0ep90M9S_JUQMr_McoX0cExuaLJhu0xgtEGbJSsvYURAbz1xbNmNRPrV4bw8nRsBKGMiRsx8-6I3tgL24rGa5flo5skz1DB2oPqWlm9vVMM57lzKB0r0fHO6tvgTqvwkKy_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر لکه و خط روی ناخن یک هشدار است؛ معنی آن‌ها را بدانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/akhbarefori/672644" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672643">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2872367cbe.mp4?token=T7X-AuZiNqLLuqZ1bJkw-LkEqwS8oZ3H5AnnKy9evEDjZFLSp0SdBfe8ULBYuaViyAopgT9ePD85AzC8-uks3rJCzVIPNktIuuKPMbgG052hmn4C_cHZesP1AdgGTuC6Jv4oq-UVVuKlMSxbaY3kTATnX92KxE6dVb2HkoayCTLVHtMJJClxdKekOP9GzQdApTlVbO2YO-Z-hJS2KJKkejWIrv_REM10JxSdtXcGTMsFnLg4-dXVNO1z-D9rkaQXggfZCuHA6jMAQviTIAct1_d_TD5ogoL3V0EWR_pmFM1hrbP6LtrgNQq6O5yLb3N5yJXLoqjSri4lhOSMp8oUELiOmH_suUTrA1-C3M1t2H7hTdUuVNwMhAK2PrAb0EWH_8MUD-tLjYHhBy4D7TDx5Z1e5L0u8IAG7qqZURUKKzAZYDfg4gfAWihEf3QlFiVvkpwO6jFTRKhn-EbBsTIWCwq96DGgPN3qWZ6jF1WokqTOEUBJfjKVK8JRL4cEPT2qL4wEZcZWkj5D9TemWSsd1GTdU4PI6-nt5J-d1y3952c0ngDK2frQKmbB6SBLxrzUhVSm-BMLBmgSUkA-egs0G_R1dTyy5oFfoS85wFvB_rLMxjPg5Z9DmibrIsNoiFEr9-IswaizuCq_Yvn1cEJR_Xg7lnC_Mzua1AnY_QlZaN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2872367cbe.mp4?token=T7X-AuZiNqLLuqZ1bJkw-LkEqwS8oZ3H5AnnKy9evEDjZFLSp0SdBfe8ULBYuaViyAopgT9ePD85AzC8-uks3rJCzVIPNktIuuKPMbgG052hmn4C_cHZesP1AdgGTuC6Jv4oq-UVVuKlMSxbaY3kTATnX92KxE6dVb2HkoayCTLVHtMJJClxdKekOP9GzQdApTlVbO2YO-Z-hJS2KJKkejWIrv_REM10JxSdtXcGTMsFnLg4-dXVNO1z-D9rkaQXggfZCuHA6jMAQviTIAct1_d_TD5ogoL3V0EWR_pmFM1hrbP6LtrgNQq6O5yLb3N5yJXLoqjSri4lhOSMp8oUELiOmH_suUTrA1-C3M1t2H7hTdUuVNwMhAK2PrAb0EWH_8MUD-tLjYHhBy4D7TDx5Z1e5L0u8IAG7qqZURUKKzAZYDfg4gfAWihEf3QlFiVvkpwO6jFTRKhn-EbBsTIWCwq96DGgPN3qWZ6jF1WokqTOEUBJfjKVK8JRL4cEPT2qL4wEZcZWkj5D9TemWSsd1GTdU4PI6-nt5J-d1y3952c0ngDK2frQKmbB6SBLxrzUhVSm-BMLBmgSUkA-egs0G_R1dTyy5oFfoS85wFvB_rLMxjPg5Z9DmibrIsNoiFEr9-IswaizuCq_Yvn1cEJR_Xg7lnC_Mzua1AnY_QlZaN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احساساتی شدن داوران برنامه محفل ستاره‌ها با تلاوت فوق‌العاده خلبان کوچولو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/672643" target="_blank">📅 19:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672642">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d070710477.mp4?token=H4Evaj6DrdxDdwsT4oQjo9_-RQvghqMTqa41lYbozPPDjMArShpic2XHnqOWiDuwUUz2E3k5GvYeKlOsPVrNTzmEUcy85lHktHMXQqjkNeEQKZpkIG0j1u3pJb-5xd0PoS2XHmTLl-omOrU6SjTM9xerVu13i5Z_ziBS0Ti_PIDxPHtGtqrlUCs0Bn7s-0C2MesXrAZ-79PuAEmVsMSbOWv_wSZNj0PD0w04Yz4pKXljHosHpjM9OS6Sq8vP_cAoc1cc6nEsoCx7NynMVymqhAMZevjJfAvK9E5nY-2f0iMOZYlekFzi7-g0tNmeSICILSiOXc4iK37MnjcN2H9qLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d070710477.mp4?token=H4Evaj6DrdxDdwsT4oQjo9_-RQvghqMTqa41lYbozPPDjMArShpic2XHnqOWiDuwUUz2E3k5GvYeKlOsPVrNTzmEUcy85lHktHMXQqjkNeEQKZpkIG0j1u3pJb-5xd0PoS2XHmTLl-omOrU6SjTM9xerVu13i5Z_ziBS0Ti_PIDxPHtGtqrlUCs0Bn7s-0C2MesXrAZ-79PuAEmVsMSbOWv_wSZNj0PD0w04Yz4pKXljHosHpjM9OS6Sq8vP_cAoc1cc6nEsoCx7NynMVymqhAMZevjJfAvK9E5nY-2f0iMOZYlekFzi7-g0tNmeSICILSiOXc4iK37MnjcN2H9qLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارلسون: هیچ راه حل نظامی برای جنگ با ایران وجود ندارد چون ایران یک کشور بزرگ است
🔹
وقتی ترامپ در تنگنا قرار می‌گیرد واکنشش این است که نقش آدم دیوانه را بازی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/akhbarefori/672642" target="_blank">📅 19:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672641">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بقائی: آمریکا به دنبال کنترل بر تنگه هرمز است  سخنگوی وزارت امور خارجه:
🔹
ماده پنجم یادداشت تفاهم صراحتاً بر مدیریت تنگه هرمز با مشورت عمان و کشورهای منطقه تأکید دارد، اما آمریکا با نادیده گرفتن این توافق، قصد دارد کنترل این آبراه استراتژیک را در دست بگیرد.…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/akhbarefori/672641" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672640">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbMxORYlCHMEorHAIlI0Oow6_UFO1sIZ6nGxLx2P2ll_MY6AyRQaQfIkQFaHG2haiCGwPvQSTe8kD6Zan9elvkvzd-G0X-mzWm8W3pSHrpXZvTdWhT29gvqxW9dSQZgBjtl4cl9Qn-GBWJ9o8xCdGu4tJ8dZxtYgNjQ7spnJKJSb41jzd0RAsBOVLIECxOvWbo18aFxXHF6kGChPLcwqxnwkIgop7SBw0G2YV43uuPXNIX-idRQ0PpMg4v3ttoLSMSwvnMkWc3gmXylQkp74TWYtxy7YTd_RwUkNCEKukl26_kk5mhVx1_1iEmb4aiZ7qESth7VmeduuOO0YtzyQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عجیب‌ترین داستان ایران شاید مربوط به یک «گربه درباری» باشد!
🔹
در دوره ناصرالدین‌شاه قاجار، گربه‌ای به نام «ببری‌خان» آن‌قدر محبوب شاه بود که تقریبا مثل یک شخصیت سیاسی با او رفتار می‌شد. ببری‌خان فقط یک حیوان خانگی نبود؛ در دربار برایش جایگاه ویژه داشت، آزادانه رفت‌وآمد می‌کرد و حتی بعضی از درباریان سعی می‌کردند از علاقه شاه به او استفاده کنند.
🔹
می‌گویند بعضی افراد برای جلب توجه شاه، عریضه یا درخواست خود را به ببری‌خان می‌رساندند، چون می‌دانستند هر چیزی که به این گربه محبوب مربوط باشد، سریع‌تر به چشم ناصرالدین‌شاه می‌آید. همین موضوع باعث شده بود ببری‌خان در روایت‌های تاریخی و خاطرات آن دوره، به یکی از عجیب‌ترین نمادهای نفوذ غیررسمی دربار تبدیل شود.
🔹
سرانجام ببری خان به طرز مشکوکی ناپدید شد و گفته می‌شود زنان حرم‌سرا او را در چاه انداختند.
🔹
شهرت این گربه آن‌قدر زیاد شد که اسمش در خاطرات و روایت‌های متعدد دوره قاجار باقی ماند؛ گربه‌ای که شاید از خیلی از آدم‌های دربار، به شاه نزدیک‌تر بود.
🔹
منبع: خاطرات و نوشته‌های مربوط به دربار ناصرالدین‌شاه قاجار، از جمله روایت‌های محمدحسن‌خان اعتمادالسلطنه و پژوهش‌های تاریخی درباره زندگی روزمره دربار قاجار
#روایت_جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/akhbarefori/672640" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672639">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhFriBXZnTeIZ3Ha3cg6FbSTXfDJkyz5bvFEMsHlcYqt9iQ-3Q2Fmgx7IPcfRXo8Fr_Vrjwgil-VKrRcxZlMWhpLAhJsJ5FZnk_1KdPQ7heGr7RpVL0uZV70VNa_9LXnoeBvHJttHeTKe7sm1bgJZhPsc9e8zKXyFA4xEOmLjZXuCifJBGoHI1qFTGffCgYGwJ7hTZzSysEuWW8Pj0iQ3Gu6uJWqdhTaRxCFRe7CkhMp8iZfLGe-xMBJMfWxpbEFxmWHO0-aNhL5_pYHLCRgMuhwPWDWR_dcf7FXptpNEevJOP-7gYoJM8JFEX33gMzwWQwa3DGljSiI84M-vKRVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی: اگر ترامپ به هدف قرار دادن غیرنظامیان ادامه دهد، امارات متحده عربی هدف بعدی خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/akhbarefori/672639" target="_blank">📅 19:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672638">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gS0Zk6fX0SuqYQvXRoXvAnG_PLmJrANna-_LYNOZW7QBrFayIbpQ45v_FWQSXzpLTmyy5hHvcc6Uw35ubSnedNdeYQaH4XW81WYYQ3mVhqCflYveVn_zmct2JuS4LurfdHMbPyx7ndonn0HA5io3wQ08HFUIN_PKG7SMeF646St11BDfeh2lx_OCLdoXG-3RjReFxmmiUWbfKvv9h5yq8ybU8-dPVShcEyF3Lzstm15aZ2s8SBCh2sPJsVm4ox_FAznFmolZqden-AbuAOwDUAN3gtM-J2w7O4_2HilnPR__x3VXaYdhYspr5n2mHjYCNs6MQEUvX0TBkqE8O6lXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
https://khabarfoori.com/</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/akhbarefori/672638" target="_blank">📅 19:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
چت‌جی‌پی‌تی تخلفات نوجوانان را به والدین گزارش می‌دهد
🔹
اپن‌ای‌آی از گسترش قابلیت‌های نظارت والدین در چت‌جی‌پی‌تی خبر داد. بر اساس این تغییر، در صورت غیرفعال شدن حساب یک کاربر نوجوان به‌دلیل نقض سیاست‌های مربوط به تهدیدها یا اقدامات خشونت‌آمیز، والدین متصل به حساب فرزندشان یک اعلان دریافت خواهند کرد.
🔹
اعلان جدید فقط از غیرفعال شدن حساب به‌دلیل نقض قوانین خبر می‌دهد و دسترسی والدین به محتوای گفت‌وگوهای نوجوان را فراهم نمی‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/672637" target="_blank">📅 18:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672636">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11955b90e.mp4?token=LRFdxuXLOUzpOEPB2bNmgHDjoHWdfux0ieQiY7G754JEBHgm4kkwAmZ1EfQiJZ3ryarGCA7bAzq3rPR-KXph99mE5DYdiVB4Lm2fcC3vrRYTWblZqqtDqlZVDCMHxjbZhp6q3WfxFVxcmkNpYJceQ0TJV58_3ZztOPQ57StZYZsEJKDIOMpCmuqRMedkKOwgeaOgl146FWcWS2mUrFbKuHEe748e45hp_63J2XfsNWiAwWT5vQ797DhzhoO_F_tCKinbrqoFGl6xXcmf1Eey81wNJfmARC200A1U_5UoNB780P00DbvPabGEg5MuSbvdXGgTMhDdxGFzisJgZH29AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11955b90e.mp4?token=LRFdxuXLOUzpOEPB2bNmgHDjoHWdfux0ieQiY7G754JEBHgm4kkwAmZ1EfQiJZ3ryarGCA7bAzq3rPR-KXph99mE5DYdiVB4Lm2fcC3vrRYTWblZqqtDqlZVDCMHxjbZhp6q3WfxFVxcmkNpYJceQ0TJV58_3ZztOPQ57StZYZsEJKDIOMpCmuqRMedkKOwgeaOgl146FWcWS2mUrFbKuHEe748e45hp_63J2XfsNWiAwWT5vQ797DhzhoO_F_tCKinbrqoFGl6xXcmf1Eey81wNJfmARC200A1U_5UoNB780P00DbvPabGEg5MuSbvdXGgTMhDdxGFzisJgZH29AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده شمال اسپانیا را فرا گرفت
🔹
منطقه «آراگون» در شمال اسپانیا شاهد وقوع یک حریق مهیب است که نیروهای امدادی را برای مهار آن به حالت آماده‌باش درآورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/672636" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672635">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: کل روند توافقات به دلیل بدعهدی و حملات مجدد واشنگتن در وضعیت تعلیق قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/672635" target="_blank">📅 18:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672634">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5df86f50.mp4?token=oIMmISML40scqnRNLac5jsaWXMs-D-orgq-5sXwnaKlzfteX9mb7HHIUsnOKcHh7mnUTBOXYsWsXyKfY5QsPq9CM9VWFAe1FPMPuH7Io1HGUaZjS1FBdqcQI1uirRskbP0834OszBfqosWbIbTBckShh-IAhYH-wZDItIN0ZXm3LwDz79b-Zj_t3dRhiYL7ETw8fvuWqNtNhRSoEzX-HQBUGRI_3oLJW-IroFX6GllUYOofoY1uTTZ58WiBnLDHsKqrFmxAwuhgZfAe1UOMMdM_Adm3FWV0DeiBvWFE6-KCt_PZ6uFap0syfAeoWaM9NFMfThFjn_f34SqEWCg_vYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5df86f50.mp4?token=oIMmISML40scqnRNLac5jsaWXMs-D-orgq-5sXwnaKlzfteX9mb7HHIUsnOKcHh7mnUTBOXYsWsXyKfY5QsPq9CM9VWFAe1FPMPuH7Io1HGUaZjS1FBdqcQI1uirRskbP0834OszBfqosWbIbTBckShh-IAhYH-wZDItIN0ZXm3LwDz79b-Zj_t3dRhiYL7ETw8fvuWqNtNhRSoEzX-HQBUGRI_3oLJW-IroFX6GllUYOofoY1uTTZ58WiBnLDHsKqrFmxAwuhgZfAe1UOMMdM_Adm3FWV0DeiBvWFE6-KCt_PZ6uFap0syfAeoWaM9NFMfThFjn_f34SqEWCg_vYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین بخش از تجهیزات پزشکی هم به بندر ماهشهر رسید
🔹
در فاصله یک روز پس از ورود بخش اول، آخرین پارت از تجهیزات پزشکی مورد نیاز بیمارستان‌های بندر ماهشهر و بندر امام خمینی(ره) اهدایی پتروشیمی امیرکبیر وارد این شهر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/672634" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672633">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9lDxqb6iFCDQtveX_I2bcwDXqGzdsxfbC9xgzZazRtYb2l-jahMTlDRLAFR37jwX4TeSIPAtY8BuUyGXEATJvqX2EDUilJ_FFiCKycL6Qk3x2Xg2N8cBjQ38fkwk05A7AbI8xkCEomi0oPaKG-syHqUAXiNoHNyotkVulckwyf23MFPYY4vk9RH8utvSz_GE0hqBB8dvHZp6YLag9h7DnQxAVqNjGPx5nqXtcfK85uUeD1IES2LdTnMZ0Mxv945RcRaiT3vZRkTB0vCrnHnscmqb-bGLen8sZn2snciJrU9A8Lz8gpI2Jqfe0b80sbXeuGB_D27uap7hoUZQJtJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاعر تصنیف معروف (مرغ سحر ناله سر کن) رو می‌شناسید؟
🔹
محمدتقی بهار، مشهور به ملک‌الشعرای بهار از درخشان‌ترین چهره‌های ادبیات معاصر ایران است. او فقط شاعر نبود؛ سیاستمدار، روزنامه‌نگار، پژوهشگر و استاد دانشگاه نیز بود. بهار با شعرهای میهن‌دوستانه و آزادی‌خواهانه‌اش…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/672633" target="_blank">📅 18:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672632">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC4GzM69-m00fIUl828LWXs5MMUqceBHQtJ5tbx0KJPLWpB_xjZOm-oLzFGzC3Gvy4LTxmdGdFBar6BtO9kEzS-tGY4RpJ4gYgSbFvGzsWpvqzTywsQH1WbKGJM41CGCdN90C8ZKMZuko_Ywf2NabDDKC-RTmBtSmP3e53KuCSJ5pbTUSwDUlKgw9S5bA--1omfzxJAPkDUGJGdE1EhZ-HAV5iU2yt014_UIJj6GZk0WSJctyKsC_Ukhu6I4QCfH_c7BsfZGR0Vqq_FYJfJGi4vr7D5ukQtNNzolSdNvMd2p5hXXcxvajJ5xMErwFvRwkuKuLvNcRTfvtmZxoYnJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفات نظامیان آمریکا همچنان رو به افزایش
🔹
پنتاگون اعلام کرد در جریان پاسخ ایران به تجاوز نظامی آمریکا، ۱۳ نظامی دیگر این کشور شامل ۱۰ نیروی ارتش و ۳ ملوان نیروی دریایی مجروح شده‌اند.
🔹
بر اساس آمار جدید پنتاگون، شمار نظامیان مجروح آمریکایی در جنگ با ایران از ۴۱۴ به ۴۲۷ نفر افزایش یافته است.
@amarfact</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/672632" target="_blank">📅 18:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672631">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bef3aa902.mp4?token=PnfTwo7qJuV1dcDxFWfyg3IFPe4fobdapmPCqA9O_hrvSdN_N5xR2DPfzSFZOw5mygaXZwcxk5P5exhoimnkEdwR8BFYEcAPlXdcf1bfTOnHlfArq7RAJNUE5gL3EHFUku_K5tT9DNKCu-MsRgCHt2-895xZk7en-2SmkrA3q6yEqGOIKN4bmyKcp57u_iowJhdaH-7n2MEDeqYNW1PrRDnCR36VeoIYgFGRH3UiL2OxyYaLlIj2aczRmVKHl1lp652Ez1DTHAwfnU0RS9yrLiZyhh-bKs4JYvFAbNSQEHBtM783laDMcAL0ODXiIQV1H2vrluH2LlhuZUtnCgJCQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bef3aa902.mp4?token=PnfTwo7qJuV1dcDxFWfyg3IFPe4fobdapmPCqA9O_hrvSdN_N5xR2DPfzSFZOw5mygaXZwcxk5P5exhoimnkEdwR8BFYEcAPlXdcf1bfTOnHlfArq7RAJNUE5gL3EHFUku_K5tT9DNKCu-MsRgCHt2-895xZk7en-2SmkrA3q6yEqGOIKN4bmyKcp57u_iowJhdaH-7n2MEDeqYNW1PrRDnCR36VeoIYgFGRH3UiL2OxyYaLlIj2aczRmVKHl1lp652Ez1DTHAwfnU0RS9yrLiZyhh-bKs4JYvFAbNSQEHBtM783laDMcAL0ODXiIQV1H2vrluH2LlhuZUtnCgJCQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلای آسمانی بر سر آمریکایی‌ها؛ اعلام هشدار هوای آلوده در ده‌ها ایالت
فاکس‌نیوز:
🔹
این شعله‌های عظیم دود را به سمت جنوب می‌فرستند و باعث  صدور هشدارهای کیفیت هوا در بیش از ده‌ها ایالت آمریکا از جمله واشنگتن دی‌سی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/672631" target="_blank">📅 18:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672630">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
وزیر خارجه عراق: خروج نیروهای آمریکایی از عراق در پایان سپتامبر قطعی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/672630" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672629">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
حملات متعدد نظامی دشمن آمریکایی به حوالی سیریک
استانداری هرمزگان:
🔹
در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/672629" target="_blank">📅 18:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672628">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: کل روند توافقات به دلیل بدعهدی و حملات مجدد واشنگتن در وضعیت تعلیق قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/672628" target="_blank">📅 18:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672627">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae992943.mp4?token=BgkwWxq_uMdgCpT8HCt4E42f-BKNOKyYHWrowhqCESYQqzOHA4Kohx-ChPKXW2P5FdKJf9FO_t4Db0vuyqjZ3pOVA6gXRyFnk9JXGnDu8qD3Ff-1wiR8vFFVop_Lu-Hp8GIXEv9pnLlC3NwTPFCpAuZnU-89X4ow3XI9Xx2b_xq8x4JyO2bxS2dRNPBU5_7wZqBlaF9GKYk7zGBiNt3gjV0l4qWf70zAFyFaCcKmXVMdWs35bFfegUV6ULLIVaDFpgfAqN_7KACFNQ-7qhxgVUXeA68camSriDx7GAoKjkUzDFd01LLZXwLLf0IpfS6aOVxHKR2wcYXjWjc6HvASag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae992943.mp4?token=BgkwWxq_uMdgCpT8HCt4E42f-BKNOKyYHWrowhqCESYQqzOHA4Kohx-ChPKXW2P5FdKJf9FO_t4Db0vuyqjZ3pOVA6gXRyFnk9JXGnDu8qD3Ff-1wiR8vFFVop_Lu-Hp8GIXEv9pnLlC3NwTPFCpAuZnU-89X4ow3XI9Xx2b_xq8x4JyO2bxS2dRNPBU5_7wZqBlaF9GKYk7zGBiNt3gjV0l4qWf70zAFyFaCcKmXVMdWs35bFfegUV6ULLIVaDFpgfAqN_7KACFNQ-7qhxgVUXeA68camSriDx7GAoKjkUzDFd01LLZXwLLf0IpfS6aOVxHKR2wcYXjWjc6HvASag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از اصابت موشک‌های دشمن به تاسیسات آب‌شیرین‌کن جاسک
🔹
بامداد امروز، اتاق پمپ اسکله تاسیسات آب‌شیرین‌کن شهرستان جاسک هدف اصابت موشک‌های دشمن قرار گرفت و تاسیسات آب‌شیرین‌کن این اسکله، تخریب گردید.
🔹
در حال حاضر، آبرسانی به مناطق تحت پوشش این تأسیسات تنها از طریق تانکرهای سیار انجام می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/672627" target="_blank">📅 18:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672626">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بنیاد ملی گندم‌کاران: بخشی از مطالبات گندم‌کاران پرداخت شد.
🔹
تاس به نقل از یک منبع ایرانی: پزشکیان در اجلاس بریکس در هند شرکت خواهد کرد.
🔹
بلومبرگ: عراق مسیر زمینی سوریه را جایگزین تنگه هرمز کرد.
🔹
وزیر خارجه پاکستان بر پایبندی به تفاهم‌نامه اسلام آباد تأکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/672626" target="_blank">📅 18:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672625">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799874b1b5.mp4?token=Z4Pn8_wtaDqBNfnM1zehgFYdLa05AGzscTWM8PHYrmTIeh8rqAwKNS00QSh6PNLihIyGmBEw8LbidX8o1yeoUC8ZjtCGTHW-KX_8o02wGWEBox03QITt2mMd6kq54WsYw2qw8l0qhTHzoNYtC7T3_NO6If-6Y3PZ7FLEY_DKMq-rPozd19U2xX_AxTUWZhtIoIcEyBhIQozm-XgVJj91B0rtxr-UZhrBMCUdQY3CUGEQLV3rQ48nSaJeC9xp319jqx54M0TSZTDxWOBLtvDwT4cW_2zUVlj7aDm5NbD8X6y0tN6h03lyAXLWjGSNaKtz3Qj-YKebU399H51xihVDVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799874b1b5.mp4?token=Z4Pn8_wtaDqBNfnM1zehgFYdLa05AGzscTWM8PHYrmTIeh8rqAwKNS00QSh6PNLihIyGmBEw8LbidX8o1yeoUC8ZjtCGTHW-KX_8o02wGWEBox03QITt2mMd6kq54WsYw2qw8l0qhTHzoNYtC7T3_NO6If-6Y3PZ7FLEY_DKMq-rPozd19U2xX_AxTUWZhtIoIcEyBhIQozm-XgVJj91B0rtxr-UZhrBMCUdQY3CUGEQLV3rQ48nSaJeC9xp319jqx54M0TSZTDxWOBLtvDwT4cW_2zUVlj7aDm5NbD8X6y0tN6h03lyAXLWjGSNaKtz3Qj-YKebU399H51xihVDVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدئویی از عبور یک هواپیمای مسافربری بر فراز انبار در حال سوختن «وایلدبریز» در حومه مسکو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/672625" target="_blank">📅 18:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672624">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRg1daSD3GMrbUdpULREjJA0wO1lZtF4an3QEBUKGpZy06R7LKvvyQfuPbXj1DALnnPPBrrGveUGTK0kTKel5VuC5KGKnpGpH_KSMMTo0AjO3v0A5bqTOGCVA4RYajQt0ardUzEBDTPXTHoUr-YbZxdqMq9EHTMD3oaNsEpRG8PiqFlq9sbZS9bYADKU9vygbX8h9BiiqMqmuIVbcpXM3ND23nVVsXOa1d-uUHvLSLvKS6ZUAAKdAzeh7Xx6OyekgI_H0UiL2MqJsxlfhMfo2eA-kO5PIrENeiTOSSA9ErVUUZhy3EbVS5MmuXqgEKdwm-oPyyTpzTm2L5sKMdOxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این سلاح کوچک تعیین کننده نتیجه جنگ ایران و آمریکا خواهد بود
🔹
مهم‌ ترین کارایی شهپادها در جنگ های جدید، تغییر ماهیت تهدیدات دریایی از سطح به زیر سطح و ایجاد یک بحران "هزینه - اثربخشی" برای طرف مقابل است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3231295</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/672624" target="_blank">📅 18:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672623">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/li9g1pW5b2lECSjwhDbDlsueqq1nvkNMmeXD0U51y5AhwkneEOcCeFUtXvpqVoglxD520iljY4lAixiyIkLY3u-N0TaiW_vZ-dfSeSaC7-XeEXeM-J1a_3CuPnkRYSZXQfeOJ2o8EJcilelUqmoDF9mlCvE-CTOCqsvCJumijJ32tkbTcVDBu3V21krj8956gDcbbuJcggy3mpa_Zl9CHvuIdcjnhqt4Xs37QkLlgzpoD_LgxoCaIoUuEodCUdFVyWx6iKg0yX_uReQ8jkVGndTsVDJyy4uJdbaRIi6RuBcuO5l1ndTykDte2oHr2fzb6d9zQBTa64e04VijF8PtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در کنگو در واکنش به اظهارات وزیر جنگ آمریکا نوشت: تمدنی که با اصول خود مکر می‌کند، تمدنی در حال مرگ است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/672623" target="_blank">📅 18:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672622">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikCSPKe9UzpPEmJqnbLUKGU2ne-LuD93_xFweABn6iRm77tfHgGKB3NGj0Xz09A0obiCYgtq4EEatvejASpKmmZ2y1f2SPBkJ85tV8B9IDPMoNOHrqiEdcBs2HprPkYv6Bp_P0LFq04LCHE1JhF-zFMOfjZTK-anr4xvK1a4CbHS9Nr5C_KnWwXTaMwYNxdidHPhuZvNid0lzBw_Li3YyAFe2DJU4DYMG3_c8428gDV4yAY2htGBjfg9SyjOm_irZeV5rCfvM7BY3mkvE9Ki8abiuKIHjeXb_vniRYfIj-fO_Ae1YsHki5vX-ItNUOWFKEqO_k6kojvLWeA4qyb65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پسران والیبال ایران بر بام آسیا ایستادند
🔹
تیم ملی نوجوانان والیبال ایران در فینال قهرمانی آسیا، ۳-۱ ژاپن را شکست داد و بدون شکست قهرمان شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/672622" target="_blank">📅 17:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672621">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
منبع ایرانی به المیادین: منطقه برای نیروهای آمریکایی ناامن شده است.
🔹
بلژیک واردات کالا از اسرائیل را ممنوع کرد.
🔹
محمدحسین اسلامی قرارداد خود را به مدت دو فصل دیگر با تیم استقلال تمدید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/672621" target="_blank">📅 17:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672620">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7f6b7989.mp4?token=e2Nik0roMcSJ6awMEJdwDlndsGDUzYqWL60O-LIG7NSYglCqyIFfN29G3sAlroe42urUdfnSP8Y4SjBqR8bamtwO_EdPGYr2xnMdA8d4w2ibcJ-HGDA6hWq_NrhRbe5r8BxFyDyJ_sYFO8_atlqojeCkPMdAiJdfmTpYAkKJBJtKT2uloT0tTcXGkSLUu4kN1TfkYcwnBQZ93vRqiCpsCg1rZ8RevfHBfK75GIA24qT5KLZEDkTm509DslOnWo7rdhpQ9PYo34jcRuvbICeEEqegNy8vmWIDx2nsEF9OBusGqFGQoiZmGmv5IO11Tzxwmu0VtWnUxap6D3MmJ9iCUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7f6b7989.mp4?token=e2Nik0roMcSJ6awMEJdwDlndsGDUzYqWL60O-LIG7NSYglCqyIFfN29G3sAlroe42urUdfnSP8Y4SjBqR8bamtwO_EdPGYr2xnMdA8d4w2ibcJ-HGDA6hWq_NrhRbe5r8BxFyDyJ_sYFO8_atlqojeCkPMdAiJdfmTpYAkKJBJtKT2uloT0tTcXGkSLUu4kN1TfkYcwnBQZ93vRqiCpsCg1rZ8RevfHBfK75GIA24qT5KLZEDkTm509DslOnWo7rdhpQ9PYo34jcRuvbICeEEqegNy8vmWIDx2nsEF9OBusGqFGQoiZmGmv5IO11Tzxwmu0VtWnUxap6D3MmJ9iCUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صادق خرازی: روسیه و چین هم تصور می‌کردند ایران به‌زودی از هم خواهد پاشید!
سید محمدصادق خرازی دیپلمات پیشین کشورمان و فعال سیاسی:
🔹
یکی از مقامات بلندپایه روسیه این موضوع را با ما در میان گذاشت و چینی‌ها هم رسماً گفتند که در ده روز نخست تصور می‌کردند ایران به‌زودی از هم خواهد پاشید، اما وقتی از نزدیک شرایط منطقه را بررسی کردند، به این نتیجه رسیدند که ایران با استحکام ایستاده و در مقابل، طرف مقابل در حال فرسوده شدن است، همان‌جا دریافتند که
این نظام، نظامی خدشه‌ناپذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/672620" target="_blank">📅 17:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672618">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774abe36aa.mp4?token=SpaPqFlDLRmLgLUBhCkuZz4NnbFJKR0Zqdy6oUo22oimTPUw_GHdr-GCJX9ETrJp5lM4ONlcGH9id7HHGmlKJWxkrLyXNWRbou8rfvrv7OclqMqmCO0UXKx7v8E9M2lR_wlxsD8kSZ-lAgFzoShAbhw7koVUtEnrcH7J-aT4qPSbQjc-6fCyLnhl548VjLq1iaji_qCP3WECQmVIrkOjj8t5OSMHWPQz3aQg8ESPdBcs_Cj1HeBzHmDQZyV4kXdUl-nxY0puvoWq51ZB47wV-0Nq32leFwTXAmMJCn5zEHloi0iBpTM-55ShyV5HVdvU2-_qAB5IQZ5Vd-C0z2rPeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774abe36aa.mp4?token=SpaPqFlDLRmLgLUBhCkuZz4NnbFJKR0Zqdy6oUo22oimTPUw_GHdr-GCJX9ETrJp5lM4ONlcGH9id7HHGmlKJWxkrLyXNWRbou8rfvrv7OclqMqmCO0UXKx7v8E9M2lR_wlxsD8kSZ-lAgFzoShAbhw7koVUtEnrcH7J-aT4qPSbQjc-6fCyLnhl548VjLq1iaji_qCP3WECQmVIrkOjj8t5OSMHWPQz3aQg8ESPdBcs_Cj1HeBzHmDQZyV4kXdUl-nxY0puvoWq51ZB47wV-0Nq32leFwTXAmMJCn5zEHloi0iBpTM-55ShyV5HVdvU2-_qAB5IQZ5Vd-C0z2rPeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار جمعی مسافران از فرودگاه کویت؛ ازدحام بی‌سابقه در پی حملات کوبنده ایران
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/672618" target="_blank">📅 17:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672616">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bAJfWHzj4--ghh4FKrpxHALpFhv1-Bvp3_EpZfBiwYc8GM22tp3iDvsTAnSZ0Lea_s9cA_TCKbLKvvmRdGBUuNn0bY21rvKyPb-AzIguV62UU3VUrML9QDWobLSzxTddA1ibwUgZz6h_AYfIJH04X9d1F4zB94J9uoJKd8F9MJRF-fw8WrCmDogWrchrDbkVRn8fpeWcQo8-BQnL3KdmkJH2kvu_Nib57ZPRBr9RZgpzAJYww5XXU1iiyWb8g5KLq8JqR2ISSCTx2e6YwYj1_h0wLYefu0kRlvZJJTr5hiDIStPv8SgWmCe4aEz8kxDfy9IxrnXCA0dTIJGwIGx6LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDHb7VuuE86I3JvN91QqDWBrjuGIYRoFt7leqKBqvGLHFTpmFg-7iHDMGqrqgxOkn31TX3IJycvYLIZY_meqWL-U7-G_iQwcogJ4_lgW98QenjuhypM_fd3WfudavfuuTwsbC_6c5NUCbeydQsOkZrBdQVHTEt5CZPbRd8GqYn_D8G22zYkT0tCULNYXZS2Ja4WRFWbIEmkCvTdqnE1cg0Eqhn9o74H26gXMibUW9FhHQIcvyZY_hSkm3vHlFaujyVAqCwvpcfi5dI7xA-pxOVDLUxSq4UuIpwRoKWyVhcSF6r2Qx8VIpmkj9PVTLjzJ1F4uUNn8FV8S52gj6-IivA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمله به تروریست‌ها در سلیمانیه عراق
🔹
به گزارش منابع خبری، در این حملات، مقرهای تروریست‌های تجزیه‌طلب ضد ایرانی هدف قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/672616" target="_blank">📅 17:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672615">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
احتمال تعویق کنکور و امتحانات نهایی
🔹
طبق گفته یک منبع آگاه، با توجه به شرایط کشور، طی روزهای آینده جلسه‌ای با حضور وزیر آموزش‌و‌پرورش برگزار می‌شود و در خصوص تعویق و یا عدم تعویق کنکور و امتحانات نهایی در کل کشور تصمیم‌گیری خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/672615" target="_blank">📅 17:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672614">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0814504652.mp4?token=bkYMurmBpX2EtHalSbL7Rc5i_v11yyLIlMRHnp5KqGUEtk60zZrFI8F0yQ-vJjQcgT6RZbyoDWlf5oZJOD3GOZTGDnXb9G0ijrLnaQHFAmvVhmsHX_5vgVzhilJbpBVTbopYs2A3c8evLmxJoQKZZMGIjXILGB3DAcGttiP9cjIizZt8duy0l0K2ISShBZyILTKYVw5QfDHX0mmYjqvhCDx28Ts-yoTFz1KOOqHiBU7Q4xhZAoTCvieXJz14CVYdmEEm31byu5HbUDaj-z56H7EhAiTUDEt3RSM-4P2ho3yLjkzsLoLMDpv8SL603fL--QLokYF_fJ5Z4Fy5YaTGfjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0814504652.mp4?token=bkYMurmBpX2EtHalSbL7Rc5i_v11yyLIlMRHnp5KqGUEtk60zZrFI8F0yQ-vJjQcgT6RZbyoDWlf5oZJOD3GOZTGDnXb9G0ijrLnaQHFAmvVhmsHX_5vgVzhilJbpBVTbopYs2A3c8evLmxJoQKZZMGIjXILGB3DAcGttiP9cjIizZt8duy0l0K2ISShBZyILTKYVw5QfDHX0mmYjqvhCDx28Ts-yoTFz1KOOqHiBU7Q4xhZAoTCvieXJz14CVYdmEEm31byu5HbUDaj-z56H7EhAiTUDEt3RSM-4P2ho3yLjkzsLoLMDpv8SL603fL--QLokYF_fJ5Z4Fy5YaTGfjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی بزرگ در نروژ؛ تخلیه ۴٠٠ نفر و تخریب بیش از ۱٠٠ خانه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/672614" target="_blank">📅 17:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672613">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
شرکت برق تهران: برق بیش از ۵۰۰ اداره بدمصرف که از سقف مجاز مصرف عبور کرده بودند، قطع شد و این روند تا اصلاح الگوی مصرف ادامه خواهد داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/672613" target="_blank">📅 17:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672612">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e94e0d995f.mp4?token=bJIxM8rRk1ZgOay7QgdmSghR4l6UgR-qxkohxd4aXyc8QEWNvVfL6lBX0tGe9tMqVNq7qwwyM9Al4Et7b_JnwLFRmDR_vlv3hsHp80JsHw8Zv0XLVRDMs9EXmpawjUDSEr2ULif6YZseFgCBvUtlQ-QzwUJb24SNBK_FzCbkCRTcY0JS_CXcvY08aXqpN_bdGOPicK4nHijheOAfdHK_5PCnc9hyRyOwK3L_jN6Fqk87c4TFZgFlB9Hee8HGLAP_C5wNSnTbMcW5nNJTrT4QtOfwG1l-jPC4bQ6e5CGdUceYtEbJ2VqdjeNcDiSgxlzGYyWduN-4OESOaL2cYBXDBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e94e0d995f.mp4?token=bJIxM8rRk1ZgOay7QgdmSghR4l6UgR-qxkohxd4aXyc8QEWNvVfL6lBX0tGe9tMqVNq7qwwyM9Al4Et7b_JnwLFRmDR_vlv3hsHp80JsHw8Zv0XLVRDMs9EXmpawjUDSEr2ULif6YZseFgCBvUtlQ-QzwUJb24SNBK_FzCbkCRTcY0JS_CXcvY08aXqpN_bdGOPicK4nHijheOAfdHK_5PCnc9hyRyOwK3L_jN6Fqk87c4TFZgFlB9Hee8HGLAP_C5wNSnTbMcW5nNJTrT4QtOfwG1l-jPC4bQ6e5CGdUceYtEbJ2VqdjeNcDiSgxlzGYyWduN-4OESOaL2cYBXDBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک سیاره، دو فصل متفاوت
❄️
🌍
🔹
در حالی که ما در نیم‌کره شمالی زیر آفتاب تابستان از گرما کلافه شده‌ایم، در نیم‌کره جنوبی فصل زمستان جریان دارد؛ تا جایی که در بخش‌هایی از شیلی حدود ۲.۵ متر برف باریده است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/672612" target="_blank">📅 17:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672611">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcDaIht2Y76YF8hkzPGXcf4wUBCd6hFP2YYFdPo89zxjm_VhBjn_mYW8m3MbcS2SzWRHiXgMUthyS534gYioiavcn6NJwhkStJX7xLLteO1jbWpULJ_mnBuGKq2c5vTsG4Fj4M4PmAodQqaADlrSM-1ECa_6Eke8nFbaoTCZZyQ0XIJLyMQsAAhc7nc4dho1Y9-ywoz_0cKWjFT2VAb-Tvz1ETa7aa5wQKMbyCJEckxRcX4Xv7ZA5e0HoWyz8VgY4v2MomZhllawKQ_3-f6-mTbPYeB3sMa1KBG5QIhSRRW1pMiQfVqKsJvpOyOPHG-4g3W8q8fnz4VwRTK70Oxm-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/672611" target="_blank">📅 17:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672610">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb0_h5fIx45aMUFrwKpcofEXnYcUy_MPyshKmorERweoEJAdyTH_r-amdAy2BG3AsEQxzdKoRZwzWPafqrvtrN2fiLMWelb-9nZabQwA4pX0TGkWJQ5kYu51hteFLJrJZdC_I1uKe6XOtaajr9b9jgaNtn5p8yzoN7mkL-YEu-648ox0GhngVEpONLlsJ5-5IjrzmuiQGFt27e-sApuCCDKP9tCQhnuuHd47ITBMIDfQ1kP2UTytyA6rsypbxXkndML2NRJx33AwRYr5H-oVQJyUqCCfqe2RFWCtwDWe8xczxEwOQ52jYvXlIP-jRHMfYduDljEjEObdzIdQtxgD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاه کاربران به پلتفرم‌های خرید اقساطی چیست؟
🔸
در این نظرسنجی بیش از ۱۵ هزار نفر شرکت کردند که سهم تلگرام ۱۷٪، روبیکا ۵۴٪ و بله حدود ۲۹٪ بوده است.
🔸
بیش از ۳۸٪ شرکت‌کنندگان، پلتفرم‌های خرید اقساطی را به دلیل سود پنهان و کارمزدهایی که دریافت می‌کنند ترجیح نمی‌دهند.
🔸
حدود ۲۶٪ نیز معتقدند این پلتفرم‌ها بدهی‌های غیرضروری و مصرف‌گرایی را افزایش می‌دهند.
🔸
به نظر می‌رسد نگرانی‌های مالی، بیش از مزایای خرید اقساطی، بر ذهنیت کاربران نسبت به این پلتفرم‌ها اثر گذاشته است.
@amarfact</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/672610" target="_blank">📅 17:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672608">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3h6IPYG-aPdM-F_-x7Unp8Yrtm4SSFTJtww0I9aG_PW-rvIcK_64phd1wVoSNwzo3jDzZCBBK0lhgz9Evw4bQ6eQl_vd6vwIOYTSesDffVm4ReHCAr0snozqG_6E_Nu-yFs0mzMW6JY6DdSyBpunvxjmZSdYazq6TrTP8WyMY-x30zgQ_NKw3bcsEDOJkD2AJDGMMp4B70pLfsHjg3gwTH23FAmaEYvnp2uqKAAmwaq6Ju2R2mi0yjQJfndrb9dCCP59nG9cS3eZxG6UttXLPnoQpU8rgPHLGa9iYpqYibSkAm46nrZxXKjLXfChYz9y5u9BElXbBedXcpiPNKcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع انفجار مهیب در جنوب لبنان توسط رژیم صهیونیستی
🔹
گزارش‌های میدانی از وقوع یک انفجار بسیار بزرگ در شهرک زوطر شرقی در جنوب لبنان خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/672608" target="_blank">📅 17:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672607">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
پس از ناکامی سیستم پدافند هوایی پاتریوت آمریکایی در برابر موشک‌های ایرانی، کویت ممنوعیت تصویربرداری را اعلام کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/672607" target="_blank">📅 17:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672606">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
۱۳ نظامی آمریکایی در حملات ایران مجروح شده‌اند
شبکه خبری فاکس‌نیوز:
🔹
از آغاز حملات ایران به پایگاه‌های آمریکا در کویت، بحرین و اردن،‌ دست‌کم ۱۳ نظامی آمریکایی مجروح شده‌اند.
🔹
طی روزهای اخیر دست‌کم سه پرواز برای انتقال مجروحان آمریکایی از منطقه انجام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/672606" target="_blank">📅 17:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672605">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfGp99tXwiWqUdLMtHI_A3ZI_88oC_HN-4dWyjci-8VauLVYzTFh1kj76gMhUdnRF1JGX-iCQ0lhi9DybXIbylWdFY1ydmetNOjPjhlnueVKF17YSslEKFGyEVnbnhsw6Ka4eB1qZq46wTGJcnTmlYWfiu6UTvxldkE-LlO1ps_s-gJFBb9VnbKwf8AHY7ty5ua0ZAVmEdRVhnJebHvZATu-BPk4kn45Q0NtpJYkLttXZD7MgD9HmNMKgi6MCWgXq8EGdEgnITsHDNOxTunXr3NUhO08em59QcWr_PHbegXlHjbCgoYKcTTc8yY5zPtJoCwmlXfQKF-b7mjfKCy-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اسنپ‌بیمه قسطی هم بخری، تخفیف داری!
💰
برای خرید بیمۀ بدنه یا شخص ثالث تا ۲ میلیون تومان تخفیف بگیر و هزینه‌اش رو قسطی و بدون سود پرداخت کن.
✅
کد تخفیف: GT3F
برای استعلام و خرید به‌صرفه بیمه، اسنپ‌بیمه ۲۴ساعته کنارته
💙
برای خرید بیمه وارد لینک زیر شو:
👇
👇
https://l.snpy.ir/z0kq4
https://l.snpy.ir/z0kq4</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/672605" target="_blank">📅 17:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672604">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
در صورت حمله آمریکا به زیرساخت‌های ایران، فرودگاه‌ها و بنادر امارات باید فوراً تخلیه شوند
یک مقام نظامی:
🔹
اگر امشب آمریکا به زیرساخت‌های غیرنظامی کشور حمله کند برای حفظ جان شهروندان از حملات متقابل ایران، فرودگاه‌های دبی و ابوظبی و همچنین بنادر فجیره و جبل‌علی باید فوراً تخلیه شوند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/672604" target="_blank">📅 17:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672603">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SP9MsK7hFNC2qeY7tHdpx27IX_1_f4Zrrpv0RFV5uIVd7eW2MqjA99mT27PhmQtrLXowqqe3NunCgw8eSlhZ_RFYb9Ti1IxnVYoyd5zyvKHInHOZYyCVkASSeuSte7ZP6UHa-KcVF8eyZQU_7zNB_4JJALZnHLqZH2jngx_8NmHb_w0PaZA7RXQ5QNEZXJJGKDiuAHBU-Tqau2pFA7EkdgkWhOvNFPtjWXrZUEi4mX8g6p6XwcyOdKOLj26Mhq7kgpkyXNJnPMBjR-u_1h46dey4pztRY9JltYIPpQtRUossUsgacL3pN2jPFM1mAupkfVOneo7deiNKsnTIiWHkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروگاه شعیبه کویت منفجر شد
🔹
این نیروگاه با ظرفیت تولید ۸۷۶ مگاوات برق و ۴۵ میلیون گالن آب شیرین در روز به عنوان یکی از شش نیروگاه اصلی دولتی کویت، نقش حیاتی در تأمین برق و آب شرب این کشور ایفا می‌کند و از نوع تولید همزمان برق و آب محسوب می‌شود.
🔹
نیروگاه شعیبه بامداد امروز هدف قرار گرفت و به طور کامل منهدم شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/672603" target="_blank">📅 16:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672602">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
آکادمی امنیت کویت در پی حملات گزارش‌شده موشکی و پهپادی ایران در آتش می‌سوزد
🔹
این مرکز خسارت‌های گسترده‌ای متحمل شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/672602" target="_blank">📅 16:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672601">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-BgzSFVIPbxQ90qb4Z_CuaTapXfdapih4_onndx7l01UmLF55nXMYWl_eoGcaSHBeAt1IgJMP6OV9gc2K42d1U4eFRPpGrSIJppBuA3cUZcCmmECEU5rOL3NHnRrrcewdG78jD-V8rD6UOkJX7FHJh08yx2ax9a23XxhlpYwU78lheoFX6-tAGo96TtQJbRj0AvTuqHwNDMu5gUYP9cnpgm_1tAIp1jJQEso-z5hVIMjjfJxI4_CGwHzKuksRaz0OscBsigIGHmLULA4nnd9GadKU2RdQXVnjK4dUxiRVbgTu5uuS-XxbTJHcn7eG5soJNY0eyqz89XLEx2yAljMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه DD Geopolitics: جمهوری اسلامی امروز به طور کامل پادشاهی گوجه‌فرنگی را در هم می‌کوبد
🔹
ضربه‌های مستقیم به مجموعه‌ای از دارایی‌های آمریکایی در اردن.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672601" target="_blank">📅 16:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672600">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3655956b73.mp4?token=KLr13sYUUh01FjrDvesNvewHbuz4nte-5rKxyyNBe6U4X8_xr0QyK9ivsSWTOcOEvlqJEqk4n1IqSvr3Qbis14gzrMgnBzMUwEM2MmGaowoPQ96ufMKOlH4aB1spDGFENYw_wrvK6eowP_RG4aUdlth1IqLb174X1_WnlyGiVAWHNuwDjfbDnJxYHqtyZmf4kQKrp6d8f8L4G4C4zpmAFtMsPB0tBnZFdsA6KJMxlDjloSs_RbfUmQ7fZxI4eNpVH1QUNqRI_XFdyVpsJIzj5f-xnfiOjoaJFZSohrsmXFkffkDb6LorfTQ8smOin8HEZsVAOSmQ1_5_u91K7Bba3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3655956b73.mp4?token=KLr13sYUUh01FjrDvesNvewHbuz4nte-5rKxyyNBe6U4X8_xr0QyK9ivsSWTOcOEvlqJEqk4n1IqSvr3Qbis14gzrMgnBzMUwEM2MmGaowoPQ96ufMKOlH4aB1spDGFENYw_wrvK6eowP_RG4aUdlth1IqLb174X1_WnlyGiVAWHNuwDjfbDnJxYHqtyZmf4kQKrp6d8f8L4G4C4zpmAFtMsPB0tBnZFdsA6KJMxlDjloSs_RbfUmQ7fZxI4eNpVH1QUNqRI_XFdyVpsJIzj5f-xnfiOjoaJFZSohrsmXFkffkDb6LorfTQ8smOin8HEZsVAOSmQ1_5_u91K7Bba3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار جمعی مسافران از فرودگاه کویت؛ ازدحام بی‌سابقه در پی حملات کوبنده ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672600" target="_blank">📅 16:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672599">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hurRiBH9hV2VjBIZvSCzFjEQ2QatdZ0Vvv_vdnVmxd3RQ7bZM1skC3GFS24jn5Vq_tRId6ZccRRjz8ttLY5r3-XAgynz420HSCkUzAB7NsdpDlLhjthEywD1Yewur_CDmI7Ij6qgJ2ugXrK98ROwzXdv0CGFBIaE9tA7N9CAA-QoM41ZA-BoxCe3tx3R_1695ZTT7eI700d6aIqvUIiboq0B3GAwLgZV8qJPUoHxmfRc9hy8-IeemCekhKzx5WCX7BQwu7QfJBP7KmZi0yW9SYCojWmi8XGgtxx3g8xRYo0reIbcqoEgpq4e0mLfRiY1VWjhpXhujrxPshmH3oskJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیسان قشقایی؛ همراه همیشگی سفر
خرید با شرایط متنوع:
▪️
نقدی دو‌مرحله‌ای
▪️
اقساط ۶ ماهه بدون بهره
▪️
اقساط ۳۶ و ۶۰ ماهه با نرخ ۲۳٪
▪️
تحویل ۳۰ روز کاری
مشاهده بخشنامه و ثبت درخواست خرید:
🔗
https://arinadrive.com/qashqai_landing/
آرینا درایو؛ همیشه رو به راه</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/672599" target="_blank">📅 16:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672598">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
آسیب سخت به نظامیان آمریکایی در پی حملات ایران به اردن
شبکه ۱۲ اسرائیل:
🔹
ایران طی هفته جاری به دست‌کم دو پایگاه در اردن حمله کرده است که در پی هدف قرار گرفتن این تأسیسات، تعدادی از نظامیان آمریکایی زخمی شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/672598" target="_blank">📅 16:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672597">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس دادگستری هرمزگان: مردم هیچ نگرانی بابت ارسال کالاها و خدمات بندری نداشته باشند.
🔹
نشت گاز در محدوده بیمارستان دی بدون حادثه مهار شد
🔹
ستون دود در منطقه گیلاوند دماوند ناشی از آتش‌سوزی است
🔹
شهرک‌نشینان صهیونیستی: در صورت بازگشت دوباره نتانیاهو به قدرت، مهاجرت می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/672597" target="_blank">📅 16:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwuQnvUwZH_IIm0zRoQV98ROyT1_6-q0uMgA05z6QquqPXOXPHMQCmEQhjoHyU-L36pwp42dj3o7YTMq9heiGTEJuckJp1aaFqw4cgxaAM0wR1iaSuHAfmhcb-yyT1YT7av-Xf_hQL_YawIzh6fHM63VRdzPEw6XOWrWXx4VOH08UDjjJBDF_N81ZNyAlA2ReI7VkKdnuowODl7n9AClkFB8gDp5sOc8Rw10V3ci1g06zcocQF3eZYf_EO-en2nJhl7yxTVvxPxD7ENiSLEODEHaMccy_GhXBkM8EcHKM8aYxDeesTy3yRdwc0NfB7zEj8gVRsVzGrB9c_Hhp6f6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
العربیه: بار دیگر، آژیرهای خطر در بحرین به صدا درآمدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/672596" target="_blank">📅 16:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To7Y7gN4-T_Rjyqbo_KVNR8QhJ1oRAMzTSgmwsFlfyci4SAH0Rys3VLumDlwgjHVz4kkbo4LbV93TG-KD1TlYR1n3bH6YlmD8DmQAoPYwQjot5lJj5VKFJGj4gh5ZSflqCyZ7xi107DQYr00VIkGswE45PWMip1xHFnv0kZfE-XqqVfV3aeEFTU-XBWIl_zIPOUCwDbUIZYKmKSHV5UgsEgv8CpMNXeLxpj1HrUOJOZZniv8Db39m2APH4sslyupKj6dKZrilsmIVerh19kHMD2NrAgF_SBbDuwFQ8M1kCsBji7IpQqfXl0na0Pl_bK3ZKJ8dmVvs_mZlXe0LgULJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به تروریست‌ها در سلیمانیه عراق
🔹
به گزارش منابع خبری، در این حملات، مقرهای تروریست‌های تجزیه‌طلب ضد ایرانی هدف قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/672595" target="_blank">📅 16:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672594">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c37398e3f.mp4?token=lwcj-Be_jkKL33I0OTKH-aUo_c8FX-FgjPpmjZ-4hdoDWWzbEG7ND3WcW-0P0RXnE4wfaXBW6ADvx8LXy6QM_bq188neqs2yICF9JyXpVi6DPZ6fLEGDtsHscX5C6pMlYWs7BMPOxcByv3vU_QLj7fpffb66C-hMOE1Y1s6SxTFISjfHKe1pZS4r4weDxBcFSo75TO7th_IxzOXdyNfwOSDOIxHK8ZtngNtuXQZ7xOoLCRw1BDZ6B7KsxDgaKB54atYIAUFxApJD8p4Kz9nBizaJcd14-YCbBbNl8ZJiIG-HrLBAa63xUsJFr7b8nxlvq4xeGdOyw0msu9OYW46MjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c37398e3f.mp4?token=lwcj-Be_jkKL33I0OTKH-aUo_c8FX-FgjPpmjZ-4hdoDWWzbEG7ND3WcW-0P0RXnE4wfaXBW6ADvx8LXy6QM_bq188neqs2yICF9JyXpVi6DPZ6fLEGDtsHscX5C6pMlYWs7BMPOxcByv3vU_QLj7fpffb66C-hMOE1Y1s6SxTFISjfHKe1pZS4r4weDxBcFSo75TO7th_IxzOXdyNfwOSDOIxHK8ZtngNtuXQZ7xOoLCRw1BDZ6B7KsxDgaKB54atYIAUFxApJD8p4Kz9nBizaJcd14-YCbBbNl8ZJiIG-HrLBAa63xUsJFr7b8nxlvq4xeGdOyw0msu9OYW46MjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ضربات جدی ایران به پایگاه آمریکا در کویت
🔹
شدت آتش‌سوزی به حدی است که دود حاصل از آن از فاصله دور قابل مشاهده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/672594" target="_blank">📅 16:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672593">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOff3LgKtqXsNDhkKP9CiwsFzVKw5mF8Q74Xc_n-mMg3q_n63nlsZId_YZoDh_mHGMITvbvX15FbwY3toGfe-BakCN4timN83ptAsa22N6o-PjqpepAmQ8S_938foI5blHj_LY707UojhRb9yvBrO2JSvOpSVtLHyEBddRS8S9wMbHbjy306hyaPIctpf91vA5EdBAYi9_K-kG0Vx-ZuIHAQio926shhQ_hGot-OazescyN0aqdpJOlIEA0BwbIPEw_BAts7r7D1PP3asgpYGJD1XWm-HDlCnwqda5KzGQFwAzvHXCwR7Z2rwezP2sCo6YMbS7r-30PoxHhHmfo79g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل‌گر اسرائیلی: هیچ نیروی نظامی در تاریخ با چنین سطحی از دقت و اثربخشی به نیروهای آمریکایی ضربه نزده است
آلوهن میرزاحی:
🔹
آمریکایی‌ها حتی نمی‌دانند رویارویی با یک ارتش واقعی یعنی چه و آنها در حال نابودی هستند
🔹
ایران مانند یک ابرقدرت مدرن می‌جنگد، اما با روحیه یک نیروی نظامی مقدس و بومی اسلامی. چه صحنه دیوانه‌کننده‌ای.
🔹
ما شاهد بزرگ‌ترین و حماسی‌ترین نبرد از زمان شکست نازی‌ها توسط ارتش سرخ در جنگ جهانی دوم هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/672593" target="_blank">📅 16:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
♦️
منابع عربی از حمله به پایگاه هوایی شیخ عیسی در بحرین خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/672592" target="_blank">📅 16:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672591">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49795aeed3.mp4?token=cer86MjNba6wljQldpQFaLLuXPNl2ZsvWIYw7e2dNy82rhmgizSLUM1w6oUykVxBFu2YfDdlDwK5z_qu4xt-aW2pgJ5e8KESeIhQfgql1O1huBCsW5ZmleWi7NtMUC0NOOH3JpVqzKhNRovWJ_j0exRtQ3dyM0-sfyektqpuvQQwkgC9nSPDmF589xexZ0AAn0yOMg0vJbYFngCuZ-rjoxkmmDHGlz42kJS-rfmQVHjhIB6M4OkbtaWCDwJzwl1YW0dl5F2S-hVf6EpS_3rILlFcrJ0u5LrtIdJN6Ibv0-mFX7xXufJ8bNtX6oyK7vbE_M3wsiTtvouNDyjj7mFWuLlKrEPeZ4eCN0AKR3ZAR5JFgtfdfwIwNYPJuPAK8if_xRW50OLf8eriMu556-ymgtvCUERyoDRV9ZN8gqc_U445Pi9ncXTWU47QuRz5VwzmZRp2CGuOdz0NuYtIKv_c72KaKucTNqrfrji1zMiZBbTI01UPajxmQm4hGUEz_r_4sm9lM-AgJPliCn67YzQb4t2dNq9r-6Rax9y4G1ZXVr0leWEs1N_umxhL3U45PxezqUNz8GMmbAZgnylkDtoQm4FsC-ebNbt_dtX-_5vueQkK_yr_aQs81_XTutOXyh6OVbh-wkxbvBZak0Ej21vuF9zW2OohQp28dCPy9wreX7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49795aeed3.mp4?token=cer86MjNba6wljQldpQFaLLuXPNl2ZsvWIYw7e2dNy82rhmgizSLUM1w6oUykVxBFu2YfDdlDwK5z_qu4xt-aW2pgJ5e8KESeIhQfgql1O1huBCsW5ZmleWi7NtMUC0NOOH3JpVqzKhNRovWJ_j0exRtQ3dyM0-sfyektqpuvQQwkgC9nSPDmF589xexZ0AAn0yOMg0vJbYFngCuZ-rjoxkmmDHGlz42kJS-rfmQVHjhIB6M4OkbtaWCDwJzwl1YW0dl5F2S-hVf6EpS_3rILlFcrJ0u5LrtIdJN6Ibv0-mFX7xXufJ8bNtX6oyK7vbE_M3wsiTtvouNDyjj7mFWuLlKrEPeZ4eCN0AKR3ZAR5JFgtfdfwIwNYPJuPAK8if_xRW50OLf8eriMu556-ymgtvCUERyoDRV9ZN8gqc_U445Pi9ncXTWU47QuRz5VwzmZRp2CGuOdz0NuYtIKv_c72KaKucTNqrfrji1zMiZBbTI01UPajxmQm4hGUEz_r_4sm9lM-AgJPliCn67YzQb4t2dNq9r-6Rax9y4G1ZXVr0leWEs1N_umxhL3U45PxezqUNz8GMmbAZgnylkDtoQm4FsC-ebNbt_dtX-_5vueQkK_yr_aQs81_XTutOXyh6OVbh-wkxbvBZak0Ej21vuF9zW2OohQp28dCPy9wreX7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه طلایی بخریم که ارزش سرمایه‌گذاری داشته باشد؟  #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/672591" target="_blank">📅 16:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672590">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9rNFWn0FK5RQY7ps5cXsyw-qRGosoTmW4IO2j1beO5fwOVsEFd1Gi_rX9uYYyomn_-fPPTTtYFZMfE65gpk-8IaP7dVbLrdw0yeZ8INKDyF05rbuJ-AArdogqrvyBmIEM4u21K627b8sPsJId7QNlgzXssNeWrRIUGAv4Kxinl6aaeRcumIcv-9EDzv2tgGwHnZKckyPwdEPRYFIPfwuwyJlNwtwDT0DDO5HuODFr7KcLTwEvVDd0PApx3jQo0HFKAxCRL49_jOQRkoexs5LBWH5TYiA6msB_wZmrBEweb-wTl5QygSsBXPiy3ZcZEM1-mreIzqI-4wWGRQZqsP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش اردن: پهپادهای ایران را رهگیری کردیم و اصلا هم دردمون نیومد
🌟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/672590" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672589">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4acb113fd.mp4?token=b5zd9x6NLIkF2MqzuygsvF7fQ9y_G1I8gQl-DDPuThfsOxUHuS1FUpFFcTsfA1x8ToM8t3hiP8KySGEuHutUsMBUEr0ESv05PfYFTkvB5qnG_MDGsU1FgzVJWXQdQFA-qIaniKEa81aDBtvv9yeBu6Zl0ko5qrr3NtZqkZR8I1yGNFhpVzLF4cm2yusZefMnWk0M_phN28KlGwLMmtUKdz0F5nxUvQgJpP2nSiN71FuIIPbez4rHYLwv7nXU_sODA_KC_27-L-EfLsP9VE8ZYqUHAUkkOoQqiymoHPBiWa81ZoPnNB97vA7kM_qOWbSm6GjLPTAkL6n9haDJlZGl_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4acb113fd.mp4?token=b5zd9x6NLIkF2MqzuygsvF7fQ9y_G1I8gQl-DDPuThfsOxUHuS1FUpFFcTsfA1x8ToM8t3hiP8KySGEuHutUsMBUEr0ESv05PfYFTkvB5qnG_MDGsU1FgzVJWXQdQFA-qIaniKEa81aDBtvv9yeBu6Zl0ko5qrr3NtZqkZR8I1yGNFhpVzLF4cm2yusZefMnWk0M_phN28KlGwLMmtUKdz0F5nxUvQgJpP2nSiN71FuIIPbez4rHYLwv7nXU_sODA_KC_27-L-EfLsP9VE8ZYqUHAUkkOoQqiymoHPBiWa81ZoPnNB97vA7kM_qOWbSm6GjLPTAkL6n9haDJlZGl_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت مستقیم موشک‌های ایران به پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672589" target="_blank">📅 15:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672588">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIMSGOF1v10VKmw1xeYFSkbJa0KvYS-jZdPP3LePw0z3-dvLfm-T1N9NL84wX3nsAGbJc8-wn2P0-CSWR8aU4qE4ruN3RhxAVdYaDu1EaunT3ljR5jdhLpKkWVeC9hm_XH2cbIl59eqp8bs_NOYjOLIosMN-cqhVncPB8Zg7HO-W9nwFYK6APbcEYJaqbwKbsUjrY208pcfpZZ6g2adSRX6OTYUon0F5ccHrxMkbcla5XScOiQCkS9jXS3X-0lIEUWVtwK7ueYLa6vyy5A32VSVRIv2Qfq6W-xc9L_-DZnxV3e1rpiBr9WJTpQxXSGMGC9ScBlBqZvuYR6Ai_G-8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسرائیل هیوم: خوک هار تمایلی به دیدار با نتانیاهو ندارد
🔹
اختلافات جدیدی میان واشنگتن و تل‌آویو درباره نحوه برخورد با ایران پدید آمده و روابط دو طرف وارد مرحله‌ای از تنش شده است. این مسئله همچنین به کاهش سطح هماهنگی سیاسی میان دو طرف منجر خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/672588" target="_blank">📅 15:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672587">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
۱۱۶ دکل مخابراتی هرمزگان در حملات آمریکا از مدار خارج شد/تلفن ثابت، همراه و اینترنت ‌با قطعی مواجه است‌   مدیرکل ارتباطات و فناوری اطلاعات هرمزگان:
🔹
بر اثر حمله شب گذشته آمریکا، ۱۱۶ دکل مخابراتی در شمال بندرعباس و حاجی‌آباد از مدار خارج و تلفن و اینترنت…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/672587" target="_blank">📅 15:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672586">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
دانیا ظفر: تهران در حال ایجاد سطح بالایی از ترس در میان کشورهای خلیج فارس است
تحلیل‌گر عرب:
🔹
درگیری‌ها میان ایران و آمریکا از الگوی «چشم در برابر چشم» پیروی می‌کند؛ به‌ گونه‌ای که حمله به زیرساخت‌ها نشان‌دهنده تشدید تنش است، اما هنوز به معنای بازگشت به «جنگ تمام عیار» نیست
🔹
در اهمیت حمله به آب‌شیرین کویت، همین بس که این کشور بیش از ۹۰ درصد به آب شیرین‌ شده وابسته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/672586" target="_blank">📅 15:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672585">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
غریب‌آبادی: تعهداتمان در تفاهمنامه اسلام‌آباد را متوقف کرده‌ایم
معاون امور حقوقی و بین‌المللی وزارت امور خارجه:
🔹
آمریکا تمام تعهداتش در چارچوب یادداشت تفاهم اسلام‌آباد را زیر پا گذاشته و همه را متوقف کرده است،  ما نیز تعهدات خود را متوقف کرده‌ایم و در حال اجرای آنها نیستیم و مشغول دفاع از کشوریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/672585" target="_blank">📅 15:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672584">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
صدای آژیر خطر بار دیگر در کویت و بحرین به صدا درآمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/672584" target="_blank">📅 15:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672583">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
العربیه: بار دیگر، آژیرهای خطر در بحرین به صدا درآمدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/672583" target="_blank">📅 15:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672582">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
عراق به سوریه هشدار داد: از پرونده لبنان دوری کنید
🔹
یک رسانه لبنانی فاش کرد که دولت عراق در روزهای اخیر پیامی هشدارآمیز به رئیس دولت موقت سوریه ارسال کرده و از او خواسته است از هرگونه ورود به پرونده لبنان و همراهی با فشارهای آمریکا و عربستان علیه حزب‌الله خودداری کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/672582" target="_blank">📅 15:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672580">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9ILfuPW-A0-ks9eo-UMcwfwKbTgaSKC5371eal0yHvZFb95SttmzBp08qFzXpVxKHYxfdKTeaKBxb2w5q4Fr4HTr8czXoMUPVySiLZDhf5FoUxkZ7HiEOsurNvLCVHDpyXLiMY5teYfdHkvEFwvFIV_7TsDDr1mgzl3v59V4zRzLGUxHpQb0-Az8UdBD5qrm6UmjHKPs4w4aUusSRpJjjaL-VCRnv3BI1RsrXogrU5p7Ofr30QfDM68wDzwguZ7bEabJm1e-J3uDQ-g9p22zVpmtjv5zBta3-_k8fVPyQPWObVOgvgLxAkWz-YgUOq0s8P8Tgfq94cMU2zL6r9jOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممدانی: جای نتانیاهو در دادگاه لاهه است
🔹
شهردار نیویورک، زهران ممدانی در مصاحبه‌ای با روزنامه نیویورک‌تایمز گفت که درباره این موضوع که آیا اختیار قانونی برای بازداشت نخست‌وزیر اسرائیل را دارد یا نه، در حال «رایزنی و گفت‌وگویی فعال» با اداره حقوقی شهر نیویورک است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/672580" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672579">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5afb3ddfbf.mp4?token=XXyWZw5zL1OQJ5UqT3aYrF2rJKCG2xkLpvzGKcWlZBEBlCHLOR5EG6d0T3_YaNUY9WiFoJ5CdqQ4ri0GLxJF8Z_bjF4jcjdQa3oo0qaP1HXoO-S8f7MI2PY7HCxU-jCif2eGXlznCoZ0qgm1DIV1Hr3I24r99j5WJhF6Q9SfagNuqqZ0ImvmdeQSDtp9FmWI4KU8nB1WQeA7f7OuOV_EuY8DqWX0ppb_j0CJYgvnJGGVeCRxddpHbTGDt1HHTMY3FS-n5RLMdIjL68SVmOYFgOdgMqKyjK8YZFzXGfQOIiGu2IKu0PX6xRK0IcnIoFw-vMP51xfDdRUSwz1fJF4COg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5afb3ddfbf.mp4?token=XXyWZw5zL1OQJ5UqT3aYrF2rJKCG2xkLpvzGKcWlZBEBlCHLOR5EG6d0T3_YaNUY9WiFoJ5CdqQ4ri0GLxJF8Z_bjF4jcjdQa3oo0qaP1HXoO-S8f7MI2PY7HCxU-jCif2eGXlznCoZ0qgm1DIV1Hr3I24r99j5WJhF6Q9SfagNuqqZ0ImvmdeQSDtp9FmWI4KU8nB1WQeA7f7OuOV_EuY8DqWX0ppb_j0CJYgvnJGGVeCRxddpHbTGDt1HHTMY3FS-n5RLMdIjL68SVmOYFgOdgMqKyjK8YZFzXGfQOIiGu2IKu0PX6xRK0IcnIoFw-vMP51xfDdRUSwz1fJF4COg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار هرمزگان: با وجود تهاجم به آب‌شیرین‌کن‌ها در ۲۰ روستای شهرستان جاسک، اختلالی در روند آب‌رسانی به مردم وجود ندارد
🔹
در روزهای آینده آب‌شیرین‌کن‌ها وارد مدار می‌شوند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/672579" target="_blank">📅 15:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672578">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02387c752.mp4?token=GYaY4StNP-Mfn_nk-mxeRup7TzrOenShcPJEaGoizE2LpzLZSnriJZhgJK0JydYqctmjSaoeBjaHcdHvRheCofac1nHhhiQVQsHxqxkq3BYRzNqmB9NH5d5PokJ5KHK9pJm-nXZm9jmp3lTLfVpUaLnEqVxa7hUUKLAOQrDZCCtB6p4ZTBmfDCjKHvTU_fTZklPP8GhMRuRxmL5cIMJB7EoEYeikZk-ZM55zp997xdM2Fpx-Rbt9x3vItsqHgDRNNKdsbcszufX8Cg4oBBBQmr2dtIdgKWhhA1ZCu2q4Y8ZSIRtuS6z4ukP0mhdcL7ADvKPln9ZFnvlDqPj45ykNfJDEqpv0xMGi353hxOH7aSh5hlaOnXMAniJ_xQaJnhDiC4Hgum-nH3OyWfNGOsCCPsdUPzXqnbXhYX3uarzXyx-ao7APf-asZrLTaRdufi2aWu9oBpRWhA68hgYcaTYhAaLqpfFp7_17R8VWz-Mt-RIXeM1gnO6ukAl_2HHG1of_V40RYgjoGNBBepOqe4WSAYF97QqJLHQeJOcvTx6nA4eJDj08bfGzjchXdYrXtLh-ueedrEJ6KxG2aPd6cqep9VF58kGnGFrJskh1A3WBvznzYXP_ReB2KrpefJaKqWaY5O0M3cvehRzTsWEaDYZ4FzsGO9MPyRCCUPVthuRfnjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02387c752.mp4?token=GYaY4StNP-Mfn_nk-mxeRup7TzrOenShcPJEaGoizE2LpzLZSnriJZhgJK0JydYqctmjSaoeBjaHcdHvRheCofac1nHhhiQVQsHxqxkq3BYRzNqmB9NH5d5PokJ5KHK9pJm-nXZm9jmp3lTLfVpUaLnEqVxa7hUUKLAOQrDZCCtB6p4ZTBmfDCjKHvTU_fTZklPP8GhMRuRxmL5cIMJB7EoEYeikZk-ZM55zp997xdM2Fpx-Rbt9x3vItsqHgDRNNKdsbcszufX8Cg4oBBBQmr2dtIdgKWhhA1ZCu2q4Y8ZSIRtuS6z4ukP0mhdcL7ADvKPln9ZFnvlDqPj45ykNfJDEqpv0xMGi353hxOH7aSh5hlaOnXMAniJ_xQaJnhDiC4Hgum-nH3OyWfNGOsCCPsdUPzXqnbXhYX3uarzXyx-ao7APf-asZrLTaRdufi2aWu9oBpRWhA68hgYcaTYhAaLqpfFp7_17R8VWz-Mt-RIXeM1gnO6ukAl_2HHG1of_V40RYgjoGNBBepOqe4WSAYF97QqJLHQeJOcvTx6nA4eJDj08bfGzjchXdYrXtLh-ueedrEJ6KxG2aPd6cqep9VF58kGnGFrJskh1A3WBvznzYXP_ReB2KrpefJaKqWaY5O0M3cvehRzTsWEaDYZ4FzsGO9MPyRCCUPVthuRfnjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای آژیر خطر علاوه بر پایگاه پنجم نیروی دریایی آمریکا در بحرین ۱٠ هزار کیلومتر آنطرف تر در وال استریت نیز شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/672578" target="_blank">📅 15:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672577">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPWZPoM6PGjiZIBSR0p6hj74paQsW1y9KapTvjq4pwGNdRIwZLt3hVfm8OqaUEFdH6CvRsk682oeHiXktDtziZo14QDvSP9svCrvM9KK_TDqvA8eYXd8847mkwoUIlJzwfkvPVS5R2_nwfJYNDF6Z97QQ9KQKRkKmTzmTELLc3akOYOnpg6WzqXHugdUTQCiN82j6CsUFTAfktdFBMfD74rmuJ3699-n4xsmmCsRmj_GSc7qkIlfpxA7Wc4rqMVdQfSanXXq5y-fbr3_IBBrEsY1w_ydAh8v3Pb9n3Ch4tkQPVPnNK3N7gIqn58PKGSRbiuzHdkbdA6j7u0J7SS8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صندوق طلای رز ترنج
؛
یک رز و چند نشان
🟢
صندوق طلای رز ترنج امکان سرمایه‌گذاری در طلا را بدون پرداخت
مالیات
و
اجرت
ساخت فراهم می‌کند و دغدغه‌هایی مانند نگهداری، سرقت و تشخیص
اصالت
طلای فیزیکی را نیز کاهش می‌دهد.
🟢
ترکیب
بهینه
گواهی سپرده
شمش
و
سکه
طلا در کنار استفاده از ظرفیت بازار آپشن، به «
رز ترنج
» کمک می‌کند تا از فرصت‌های بازار برای بهبود بازدهی استفاده کند.
🟢
برای خرید با حداقل مبلغ ۱۰۰
هزار تومان
، کافی است از ساعت ۱۱:۴۵ تا ۱۷:۰۰ نماد «
رز ترنج
» را در سامانه معاملاتی تمام کارگزاری‌ها جستجو کنید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/672577" target="_blank">📅 15:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672576">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a571e5b933.mp4?token=tqwi_HhAEpXorGV_WMTQEMXFnGQV9XCpNtkK5RsVjyWGrdLCgC_64VN10lH3RAhqlIGD6ejFiKre6d19nCZVHO5QHhyNQ_7r7nPThcCbxeREY1EP_g4LTTz0lNFNVc5o6fj2G5xqdFWQuTti3uy-FPLYbk1Q16f3d2z_reGJoZgD3e5yvfvLWqD7iig2F7EW4zQt3OeuMdBIX9dt8HNm8kbXK98yW1QtzZB6Tezi2oQx_s01fTkXwqs017XCN30KWSU3Xp5_hLNfG3wRyuO86VjYmvvubFDe2cwIT2WYwUzPwQXDvoZ9VCy-rBQ2d0poS7dzS04UWot_dCz6GVNbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a571e5b933.mp4?token=tqwi_HhAEpXorGV_WMTQEMXFnGQV9XCpNtkK5RsVjyWGrdLCgC_64VN10lH3RAhqlIGD6ejFiKre6d19nCZVHO5QHhyNQ_7r7nPThcCbxeREY1EP_g4LTTz0lNFNVc5o6fj2G5xqdFWQuTti3uy-FPLYbk1Q16f3d2z_reGJoZgD3e5yvfvLWqD7iig2F7EW4zQt3OeuMdBIX9dt8HNm8kbXK98yW1QtzZB6Tezi2oQx_s01fTkXwqs017XCN30KWSU3Xp5_hLNfG3wRyuO86VjYmvvubFDe2cwIT2WYwUzPwQXDvoZ9VCy-rBQ2d0poS7dzS04UWot_dCz6GVNbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان اردن در تسخیر موشک‌ها و پهپادهای ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/672576" target="_blank">📅 14:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672575">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
♦️
وزارت دفاع کویت: یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/672575" target="_blank">📅 14:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672574">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efb89dac2.mp4?token=F7Jnb-HDHKYZ4Dc4-Sef-sWoEral27U9dThcJWScLQRhrN2VJR0UZbiEzt1Zw_-1164Gms7Ij3MQaaapWxx15hUHD2iAkabEpU6w8olTntU0pAgocQPb-A5JxIZwyK6yF-_gxGtEoiVWYch1VJKhEDwb5b2Q7ua7KkQQCdqrAywplNt6vkm9lmcoJMQzRUCJEGyg5DZ_jobX60jLbYAVGkxykegnvYS31rYXFDZ1nvFnNTOGO0Cz1rOJgwFEFisgqEhVHlHIr7RKtisVVVrYzyKjWw5ZygQhRFt6j4Vyaq_-Rfr4QtsNyIWAHMifJfVeuoUKZZ5cPvVp0c9BwC2IKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efb89dac2.mp4?token=F7Jnb-HDHKYZ4Dc4-Sef-sWoEral27U9dThcJWScLQRhrN2VJR0UZbiEzt1Zw_-1164Gms7Ij3MQaaapWxx15hUHD2iAkabEpU6w8olTntU0pAgocQPb-A5JxIZwyK6yF-_gxGtEoiVWYch1VJKhEDwb5b2Q7ua7KkQQCdqrAywplNt6vkm9lmcoJMQzRUCJEGyg5DZ_jobX60jLbYAVGkxykegnvYS31rYXFDZ1nvFnNTOGO0Cz1rOJgwFEFisgqEhVHlHIr7RKtisVVVrYzyKjWw5ZygQhRFt6j4Vyaq_-Rfr4QtsNyIWAHMifJfVeuoUKZZ5cPvVp0c9BwC2IKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان اردن در تسخیر موشک‌ها و پهپادهای ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/672574" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672573">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
وزارت بهداشت
:
در حملات هوایی ۶ تا ۲۷ تیرماه، بیش از ۵۰۰ نفر مصدوم و ۵۰ نفر شهید شدند
🔹
در میان شهدا، ۵ زن و ۲ کودک و نوجوان زیر ۱۸ سال و در میان مصدومان ۳۲ زن و ۱۸ کودک و نوجوان دیده می‌شوند.
🔹
تاکنون ۲۸ عمل جراحی انجام شده، ۴۶۰ نفر ترخیص و ۳۷ نفر همچنان بستری هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/672573" target="_blank">📅 14:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672572">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
۱۱۶ دکل مخابراتی هرمزگان در حملات آمریکا از مدار خارج شد
/
تلفن ثابت، همراه و اینترنت ‌با قطعی مواجه است‌
مدیرکل ارتباطات و فناوری اطلاعات هرمزگان:
🔹
بر اثر حمله شب گذشته آمریکا، ۱۱۶ دکل مخابراتی در شمال بندرعباس و حاجی‌آباد از مدار خارج و تلفن و اینترنت این مناطق قطع شد. عملیات بازسازی و اعزام تیم‌های تعمیراتی آغاز شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/672572" target="_blank">📅 14:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672571">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
فواد حسین، وزیر امور خارجه عراق: عراق نقش میانجی را بین ایالات متحده و ایران ایفا خواهد کرد و من به زودی به تهران سفر خواهم کرد
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/672571" target="_blank">📅 14:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672570">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd951247a.mp4?token=GUINbyAgM4As3mzGtgJCg7z-1b_LQFPDziMZK01Y8UvdH236iaap5UCcHyAdJsXkLWGwCL9L7_y9ujaGoeffGj56aPco92Z09o0h9vjUKaouhPHEOGNwP4x_KPgiURMhLlETTknSRALByhUvM8JwLMZyJBcEKekpfSDW27JnxJybpCvFuqPI8rqSu0AOUS_FE250ePtSHmAMP28yMhj-B5OvF9Rdqp57pnlIFZMbxvhMLgzPxoNrIH30gBqDsTDJyBmCczQj03zLeFYQ1DXfK9I3nkfXyy8wyAplAl-4U2TFsc3M3P_gnThxvH_Qaiq-zP7oNPmGRqykd7zzQIhH1Eu_lEf7iXo2kitZaMM3kssC7q3Zx6zx0vma__U3AgZMWH4Nh0DSoEmCWr4F2mP3f8Yjd2a2fRvkYYSdRjQ4xGGbSwTcLzz_9lcTaCp5v6Pn-9Ync6a1oiXeBodzz8ICqawAQMeeH8htwo1wnxf1AQY6f6zjimLWZtss63w9wpI9GFqptUhwUOamYvFZo2u5XJoHmfXVSUUGvkIo4FzZCN4kG2R4gG2arjiJYblTdbjNQ2MdkECe1oRPibd5SeIrcorNWEYGpLyE87JQFWiEOQS9EPl62grgN6r4gv0DAs0HyOrQnW8wSJLR57tzeC8viToof8JggiOFSrVoumd-FXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd951247a.mp4?token=GUINbyAgM4As3mzGtgJCg7z-1b_LQFPDziMZK01Y8UvdH236iaap5UCcHyAdJsXkLWGwCL9L7_y9ujaGoeffGj56aPco92Z09o0h9vjUKaouhPHEOGNwP4x_KPgiURMhLlETTknSRALByhUvM8JwLMZyJBcEKekpfSDW27JnxJybpCvFuqPI8rqSu0AOUS_FE250ePtSHmAMP28yMhj-B5OvF9Rdqp57pnlIFZMbxvhMLgzPxoNrIH30gBqDsTDJyBmCczQj03zLeFYQ1DXfK9I3nkfXyy8wyAplAl-4U2TFsc3M3P_gnThxvH_Qaiq-zP7oNPmGRqykd7zzQIhH1Eu_lEf7iXo2kitZaMM3kssC7q3Zx6zx0vma__U3AgZMWH4Nh0DSoEmCWr4F2mP3f8Yjd2a2fRvkYYSdRjQ4xGGbSwTcLzz_9lcTaCp5v6Pn-9Ync6a1oiXeBodzz8ICqawAQMeeH8htwo1wnxf1AQY6f6zjimLWZtss63w9wpI9GFqptUhwUOamYvFZo2u5XJoHmfXVSUUGvkIo4FzZCN4kG2R4gG2arjiJYblTdbjNQ2MdkECe1oRPibd5SeIrcorNWEYGpLyE87JQFWiEOQS9EPl62grgN6r4gv0DAs0HyOrQnW8wSJLR57tzeC8viToof8JggiOFSrVoumd-FXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت صحنه اکران ۷۰ میلیمتری فیلم اودیسه نولان در سینمای IMAX
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/672570" target="_blank">📅 14:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672569">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fafd5b944a.mp4?token=AWT8tAVT5-ARtss4D2DSLMNjBVDgmW_aGtWgzcRYD4aCS3gkC7EoeHqdq2HclV857HcRoj1AA-suP9I08c6HXzb9zXZ1QmogfrmaaF5QKN-8GM7eDYK2XYegExhNGvcknoCt5DV7sqQQlFoZmNg0ezgvC58dSf6fEDDh0TltVKkT3X5ju1vNw5YJNzM19ALXmzhS4oOakK6aHZhkV7g3551ni_PsxqhdQgHwOJmdVA2kkfYtAyu11ZCFKaFWtunwqv0JzcuBIHMuwGCtZRhyANrW5DeLJ-yaLdMwtJfGQscSQ_B9R5qeJIIE8S8U8lfa4liS2I0g8kBAfwOJE8l_e1k0sC3l1OOt_PZjgiqPu5GhDofl5BsHf9k95wp7SuWBz472tOWLzVxB2JHnNOAmcNoKcXAsgpI2CqDyRYRti4ciKY3JJJhTuvNrSkhNdNr0EBiKb_Fw9Nui3_4hf20Rq7NsYtdoikWfr0nO-lN5rVlaHAXm-i2fVG-TDxM-2Rkk9lXOJdQ59IWKZ09CB35Bqn-0TOOQdl_zZNEmEW-uwCl3clzuc5IE8kK--0PzYioSu1eSTEyhW0mzglteTWL_gReHmfQfE55pFcssH2qGAReeDLOGuxFluy_gulkekOcvlTxIuL-mw4d6SufnCqAvLLo6uK9RdHOa6obSVg2D7X8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fafd5b944a.mp4?token=AWT8tAVT5-ARtss4D2DSLMNjBVDgmW_aGtWgzcRYD4aCS3gkC7EoeHqdq2HclV857HcRoj1AA-suP9I08c6HXzb9zXZ1QmogfrmaaF5QKN-8GM7eDYK2XYegExhNGvcknoCt5DV7sqQQlFoZmNg0ezgvC58dSf6fEDDh0TltVKkT3X5ju1vNw5YJNzM19ALXmzhS4oOakK6aHZhkV7g3551ni_PsxqhdQgHwOJmdVA2kkfYtAyu11ZCFKaFWtunwqv0JzcuBIHMuwGCtZRhyANrW5DeLJ-yaLdMwtJfGQscSQ_B9R5qeJIIE8S8U8lfa4liS2I0g8kBAfwOJE8l_e1k0sC3l1OOt_PZjgiqPu5GhDofl5BsHf9k95wp7SuWBz472tOWLzVxB2JHnNOAmcNoKcXAsgpI2CqDyRYRti4ciKY3JJJhTuvNrSkhNdNr0EBiKb_Fw9Nui3_4hf20Rq7NsYtdoikWfr0nO-lN5rVlaHAXm-i2fVG-TDxM-2Rkk9lXOJdQ59IWKZ09CB35Bqn-0TOOQdl_zZNEmEW-uwCl3clzuc5IE8kK--0PzYioSu1eSTEyhW0mzglteTWL_gReHmfQfE55pFcssH2qGAReeDLOGuxFluy_gulkekOcvlTxIuL-mw4d6SufnCqAvLLo6uK9RdHOa6obSVg2D7X8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازسرگیری آمدوشد در محور رفت تونل ایستگاه شهیدمیرزایی
🔹
محور برگشت این تونل هم که به دلیل تجاوز هوایی دشمن مسدود شده بود، تا فردا زیر بار ترافیک می رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/672569" target="_blank">📅 14:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672567">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
پزشکیان: اژه‌ای و قالیباف با تمام توان، همراه ما در مسیر احقاق حقوق ایران هستند
رئیس‌جمهور:
🔹
امروز باید مراقب باشیم اقدامات ما از انسجام علمی و قابلیت استناد برخوردار باشد.
🔹
در تاریخ انقلاب، چنین انسجامی میان قوا برای پیگیری حقوق ملت ایران بی‌سابقه است.
🔹
اژه‌ای و قالیباف با تمام توان، همراه ما در مسیر احقاق حقوق ایران هستند، هرچند گاهی حتی با نقدهای غیرمنصفانه نیز مواجه می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/672567" target="_blank">📅 14:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672566">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
۹۵ حمله آمریکا به ۱۲ شهرستان خوزستان در ۱۰ روز
/
۸ شهروند شهید شدند
معاون امنیتی استانداری خوزستان:
🔹
در ۱۰ روز گذشته، متجاوزان آمریکایی به ۹۵ نقطه در ۱۲ شهرستان استان خوزستان حمله کردند که در این حملات متجاوزان تروریستی آمریکا، ۸ نفر از شهروندان خوزستانی به درجه رفیع شهادت نائل آمدند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/672566" target="_blank">📅 14:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672564">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8c90faa4.mp4?token=Xzgqnp_hJEu2Gxl-T4WnWgj6jkUYxNwjYGrJYj-dFy20yenqRMq_noOLeyqlzbFJagE8zFk8ftOJR29EWmpiQDLY1R08V-UvbLksRxWOWx4UrzGNIuxwPnj50yFqBRA2Z9zTfc5itEGvNHsVr8wzltzTxdAx68AhUCuQ_f3xHhRJ-mKmnz9r3jXszE6zWdNdLAGPeZE03Z1k4htaJNW5do-XPrhQ4hyWlLBxVeG3jn-GUPkl7_cwLnBEaIV9T0P1AJBCrv1SELlw9A97X1PFDj7KqFUq_bmW49kwskQJ_JJM8GlVKm6hbfaDCxt4wCSGcDXPAuaUX0KGdv3kq4p4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8c90faa4.mp4?token=Xzgqnp_hJEu2Gxl-T4WnWgj6jkUYxNwjYGrJYj-dFy20yenqRMq_noOLeyqlzbFJagE8zFk8ftOJR29EWmpiQDLY1R08V-UvbLksRxWOWx4UrzGNIuxwPnj50yFqBRA2Z9zTfc5itEGvNHsVr8wzltzTxdAx68AhUCuQ_f3xHhRJ-mKmnz9r3jXszE6zWdNdLAGPeZE03Z1k4htaJNW5do-XPrhQ4hyWlLBxVeG3jn-GUPkl7_cwLnBEaIV9T0P1AJBCrv1SELlw9A97X1PFDj7KqFUq_bmW49kwskQJ_JJM8GlVKm6hbfaDCxt4wCSGcDXPAuaUX0KGdv3kq4p4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر لحظهٔ پرتاب موشک‌های خیبرشکن، ذوالفقار، فاتح ۱۱۰، حاج قاسم و پهپادهای شاهد در موج‌های ۱۷ تا ۲۰ عملیات نصر ۲
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672564" target="_blank">📅 14:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff94ca366.mp4?token=PVIGXtCJYS9MenzFzD2ahQEnUI6bi1JQSavXdjtQFqyhyx0_UFGBAnArTZBJzsviyk2AxE_GcSalJA0RZVAud25IuINwoKV_BMw4oTghaNF1WtcR4JkqAexXX2suNSuiZ9j8PWljS8dDGP0CzKkfwVeBqD1eICNQx37IM8XZSDfzBPoEDDK2m8JSy7LB0g0XPQv1Fz2VHVKVzWjuIL858AZnDenIAI4XSsbeqshpj8-wiDiqJjJLVlqYDz89advm0ja74rWrwIeFly8XBgl0ZzPKSFrtfa0c-BkqEHHS6g8O1fbO7xPj34mDqkKlCGh0MLbPv1pX7tGTGa4NhSaU5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff94ca366.mp4?token=PVIGXtCJYS9MenzFzD2ahQEnUI6bi1JQSavXdjtQFqyhyx0_UFGBAnArTZBJzsviyk2AxE_GcSalJA0RZVAud25IuINwoKV_BMw4oTghaNF1WtcR4JkqAexXX2suNSuiZ9j8PWljS8dDGP0CzKkfwVeBqD1eICNQx37IM8XZSDfzBPoEDDK2m8JSy7LB0g0XPQv1Fz2VHVKVzWjuIL858AZnDenIAI4XSsbeqshpj8-wiDiqJjJLVlqYDz89advm0ja74rWrwIeFly8XBgl0ZzPKSFrtfa0c-BkqEHHS6g8O1fbO7xPj34mDqkKlCGh0MLbPv1pX7tGTGa4NhSaU5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتیجه نقص‌فنی و سقوط موشک پدافندی پاتریوت در کویت روی خانه‌ غیرنظامیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/672563" target="_blank">📅 14:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672562">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
تیزر قسمت پنجم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای طیب پیشداد که در حین عمل جراحی رخ می‌دهد و به دلیل یاد نام امام حسین (ع) هنگام خوردن آب از کودکی، با عروج به تمامی آسمان‌ها ، یاحسین را شنیده و با همراه شدن توسط روح پدر همسرشان، جهنمیان و چگونگی عذاب آنها را درک کرده و درنهایت با دیدن فرزند سقط شده‌شان که از عمد انجام شده، حال خوب ایشان دگرگون می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: طیب پیشداد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/672562" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672561">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6358d8ec15.mp4?token=VeEOSWpakurUPdEfaUD7N8H2iP9AxmPfkad-oEMeeByrMlvsRKsnwnKzFybwhIlQsXofR7K87AzhT838kKkMquvJM6SvCI-TN1SHmj7p-KDRxD3Z_gf40p3DOoZvzdTiYtltRVOhs809TcqnBaSRaakO3k58HWmolvDTL9o6g-Bd-wUzf-lbH2ib7yG8SQA0rm2RhudFG7c20apnB2VtfUeGi3_6Oh6xidSZ3ycLlmp77T0NttAHL1xe2VF50NIzKsoQy-V-XrCTWMm-Gcager7GkeGVt4Mtm-1V9egN667--TwPs3QQ5gnECL2yrZ8p7gaECJ6arQAVO-ZmtKIgqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6358d8ec15.mp4?token=VeEOSWpakurUPdEfaUD7N8H2iP9AxmPfkad-oEMeeByrMlvsRKsnwnKzFybwhIlQsXofR7K87AzhT838kKkMquvJM6SvCI-TN1SHmj7p-KDRxD3Z_gf40p3DOoZvzdTiYtltRVOhs809TcqnBaSRaakO3k58HWmolvDTL9o6g-Bd-wUzf-lbH2ib7yG8SQA0rm2RhudFG7c20apnB2VtfUeGi3_6Oh6xidSZ3ycLlmp77T0NttAHL1xe2VF50NIzKsoQy-V-XrCTWMm-Gcager7GkeGVt4Mtm-1V9egN667--TwPs3QQ5gnECL2yrZ8p7gaECJ6arQAVO-ZmtKIgqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩺
سلامتی رو به شانس نسپارید!
فشار خون بالا معمولاً هیچ علامتی ندارد، اما می‌تواند خطرات جدی برای سلامتی ایجاد کند. با یک دستگاه فشارسنج خانگی، هر زمان که بخواهید در کمتر از چند دقیقه فشار خونتان را اندازه‌گیری کنید.
✅
اندازه‌گیری سریع و دقیق
✅
قابلیت تشخیص آریتمی
✅
تشخیص فشار دیاستولیک / سیستولیک
✅
حافظه ذخیره نتایج : بله
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
💰
قیمت قبلی: 1,698,000 تومان
🔥
قیمت ویژه: 1,398,000 تومان
📦
همین حالا سفارش دهید و با خیال راحت سلامت خود و عزیزانتان را زیر نظر داشته باشید.
https://memarket24.ir/product/brief/37832/180124/</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672561" target="_blank">📅 14:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N67zYranmSAgQEW01D-FS437rO-RcrgvxDILi-f6MU6wGMRyubdY-__rex_0JG_bL6HzCzKErlNWVIH-ls0VloWJB5kiCXTtESv_1OJf1ZpbZwgf_cyNBDzW8SD66xsV3e-frRYfl-UbZ72wbY_oVFyj9Sr8m2C_0akaPs5sRvOZAv6Uf1vFbG48FLafrT3Y2Uphr8SOGND897sfHsQxGwKWZ4c6rjJL_-iuNIstbz3fVZArnBJZFUSAyi1ZHrfz8vdXxL39vutEyrNlT8Dts8CXvJ3L9lYH3gJ7ODaQkhjgGrPkQpYdFqjfp2y4GWJB8vq62MU6CvUAVBtq7JlGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا هرمز سفره ایرانی را نجات می‌دهد
؟
🔹
تاثیر اقتصادی مدیریت تنگه هرمز بر اقتصاد و معیشت ایرانی‌ها، از افزایش ثروت و افزایش درآمد نفتی تا بی اثر سازی تحریم‌ها
🔹
تنگه هرمز به عنوانی بخشی از سرزمین کهن ایران می‌توان به یک منبع ثروت برای مردم تبدیل شود که شرط آن حفظ مدیریت ایران بر آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/672560" target="_blank">📅 14:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672555">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pF8ZMQvsaFOAitPILtA3wWXGYqXBv54MnH3BCdzHhTSliEM15UREZmGukVRtwEi4p9OLDk-RQAMv8HQJwJufHLUhXRzMrfizjTjIpNFUeOnUAbZpqDte7o5ufD4Wo2XSQK4ZKDkEKEBVA0o5JczXb7ATrpwCCz7jp1Yk_Zxm5YtMSCttgL5L21DZ9ykM02Qz60816iSnVKqdt2vqpFBoS1efbY582VmbUr9CLHK1mADsMBfyDDc7rtb_8t8A9wuIepEPbD7MWizBuYmchSBDRyJF2pUVrFDmTiExrWfr5hoaETlSU2hS7Y1QZH8HfQvvBLXrsKoMoPqbEzfQiTkXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8vn03wVEApelMUcEXjTo4GoUipBjiXw9H9dh5khJwkGudCjSHdSReGRdu4PrcPgJhoAvnUM418IJ41_iDdh0wxUm4DFd-QtAzmLKrVpXb811flU1U5H85ZrIJCPyUyyXEwX3NTFdRiiJlA3J6mzBeGlHDkilpQ4o1nGJ_tgeoYn6Q-8ctkiQALRdh35BhXqImcG8w65l_9bXXplZO22Pxp2Ya3X9sRLZxSDfcBNHFKj5Y0C_UCdhTrEVXZlyaieCCIFHZbdo_8l_VZALtiBEhVPgtAdnfeFvG_uga88ytrcO6cI6g3isfDbJuPnB4EeRu8Cl3CTRx1CNVD7LX2ddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBa_XvHwPsq0biNdoqIoGHdlFTKJv6mcPOmP2bocgeOU0THIj3k7T2fcjtvm2Xw0RqODE25S6QSf3eJ_hJQ7Yt_PqAk4nRIRYYzEiwg214ayt2tCmbeK3BZqHUdcCKoqLTJr4gRBxnk0ebQbdGhj24710AFIASea-xrIwaaBjf3w_kX5443RJKUoYFu_flyjb6EKSSIf4RE_oNR2lujzC4maW1pMJMgtlI3D74uCp58LvIrMEaKtUUL_0HcJRZ5yiCouDxdfUzfBVV2qr_FVkB_4QL2ZRfH8wZkMbR3RYDxYN3g9xTsBhezYwI7UJFGGZV3KxIKEs5Ei0KkHwurVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7cNTtEV3bFWpkebFs26JB71Est4aa8HW2_ysQOAXnsu8bqEQB1cjBzNtj4efBkN0UXd1rpsLslk3XlQnHTC5e3tm66pXpBwIufL5l_SJ9ZRMF75L7X9a0Rn8pn1GTTq4g6PaYD5K8FKzc-5IFbP8ezEKkHCbo2KQYeZQhqJTohg_UU-2Kd0In9_8NjTDKDYtCE0ooQaY4FyTp4jjqjd6IqLTzsi7RNrKRvuFr5L98nxxCPa-sRE85901rGbKVaMROdjnJPOSynQcotlNCrCwGyloxUuHXMEVnBJYV1bdYAD20UliAZGIVRxu6Q9prkl09znzOybknglz8altRnM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAROHBSgBqI28yIQrjE37s9UqUpaPveOMp9h1QLKtUhP3nk1WdtLP9mO8ERoYbIl_eCjkK2Df3_4Ofnm9dFsKQEGijXecaswz0kHkXHt8zupkt1lRWu7HaJFxvOxB1lR5Ncek17OPQyDFiH8uEH6ovAMeGUsosKGyb_hzuyq6hTqntxWy37GBJkiwKXOuFgEUpV1814-SNV57FOJDj9picT8wSXi9jKmyVyF33EERD7t5dSJv2sihWfNGHa3pdJFlg4rZjyGiueUWaVvk96wWKT7q3FfG1Zjqlr_v8YdAnJDXv7yuCzXg6zAfD_J-ErdZA_7_jyZZWYh8S6sInRn2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کفش مناسب، رمز یک استایل جذاب و حرفه‌ای؛ این نکات را از دست ندهید
👠
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/672555" target="_blank">📅 14:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672552">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرفوری
pinned «
♦️
وضعیت امتحانات و کنکور در جنوب کشور چگونه است؟
🔹
سهمیه مناطق جنگی: برای داوطلبان کنکور کارشناسی ارشد استان‌های جنوبی، سهمیه مناطق جنگی در نظر گرفته شد.
🔹
تعویق امتحانات نهایی: امتحانات نهایی ۲۵ و ۲۷ تیر پایه دوازدهم در هرمزگان، بوشهر، خوزستان و سیستان‌ و…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/672552" target="_blank">📅 13:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672551">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
وضعیت امتحانات و کنکور در جنوب کشور چگونه است؟
🔹
سهمیه مناطق جنگی
: برای داوطلبان کنکور کارشناسی ارشد استان‌های جنوبی، سهمیه مناطق جنگی در نظر گرفته شد.
🔹
تعویق امتحانات نهایی
: امتحانات نهایی ۲۵ و ۲۷ تیر پایه دوازدهم در هرمزگان، بوشهر، خوزستان و سیستان‌ و بلوچستان به زمان دیگری موکول شد.
🔹
دانشگاه‌ها
: امتحانات دانشگاه‌های هرمزگان، بوشهر و نوار جنوبی سیستان‌ و بلوچستان به‌صورت مجازی برگزار می‌شود.
🔹
علوم پزشکی اهواز
: کلاس‌ها و امتحانات حضوری دانشگاه علوم پزشکی اهواز تا پایان تیرماه تعطیل است، اما آزمون‌های کشوری طبق برنامه برگزار می‌شود.
🔹
امتحانات معوق
: زمان جدید برگزاری امتحانات نهایی هنوز اعلام نشده و متعاقباً اطلاع‌رسانی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/672551" target="_blank">📅 13:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672549">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIYJctFCkXTbSL8_H0_8sVdxnAQ2uSHccrT9nB9RfdE2zvJrD-W5UCBiSmuz4FiUgAgeSRgVwibRHAIqwpebj0_PQT7n2Q4nTS6qAQdIs4TA6RHJprjuMTCDOTBKzUOp8t4z7ESoFe5nIHSgxX-69aBx72DD0IlhYgPd8_SBPhEwKhh-A7xwtorlblRF17xHO4wHiN2WLxuzRCk0LMQ4QuTar304HrqxoQZgj7IPxnhigvqUyOxj6GBjGoQPnAGyS_BmOuF_Xgcu_Cyj5YtP8CC8Ju6U81XpmU28f_8BZvLmTbwktL0F21Gorx7TR3bWtN236roIY4pejPJau6r7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با بسته شدن تنگه هرمز توسط ایران، میانگین قیمت هر گالن بنزین در ایالات متحده مجدداً در حال افزایش است و به زودی به ۴ دلار خواهد رسید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/672549" target="_blank">📅 13:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672545">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
حمله جنایتکارانه آمریکا به آب‌شیرین‌کن بونجی جاسک/ ۲۰ روستای ۱۰ هزار نفری بی‌آب شد  مدیرعامل شرکت آب و فاضلاب هرمزگان:
🔹
آمریکا در حمله تروریستی به آب‌شیرین‌کن بونجی در غرب جاسک، ایستگاه پمپاژ و ترانس برق آن را تخریب کرد. این تأسیسات روزانه ۳۱۵۰ مترمکعب آب…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/672545" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672543">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
منابع عربی: پایگاه «الازرق» متعلق به نظامیان تروریست آمریکا هدف حملات موشکی قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/672543" target="_blank">📅 13:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672540">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
امتحانات دانشگاه‌‌های ۳ استان جنوبی مجازی شد
وزارت علوم:
🔹
امتحانات دانشگاه‌های ۳ استان هرمزگان، بوشهر و نوار جنوبی سیستان‌وبلوچستان به‌صورت مجازی برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/672540" target="_blank">📅 13:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672539">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
رویترز: کویت یکی از بدترین شب‌های خود را در حملات تلافی‌جویانه ایران سپری کرد
رویترز:
🔹
کویت یکی از بدترین شب‌های خود را از زمان آغاز درگیری‌ها در خاورمیانه، در جریان حملات تلافی‌جویانه ایران سپری کرده است.
🔹
در جریان این حملات، دومین نیروگاه تولید برق در کویت طی دو روز گذشته هدف قرار گرفته و حریم هوایی این کشور نیز بسته شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/672539" target="_blank">📅 13:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672536">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF9G99nnS94uRXLsjmJ2J6OZyRxC_V94dHlu2B_9ov9z8YWB5qFRN5VKj_J9OMt7aF-xgqiQQYKuTF8g1AD_ZkcXlDWok6bqkXPREjOlwLz_uOGZa9IalxFgGpWdbYC_8bhFYtRr1fIs_t7E-BBmf2tTliEFOJ4931Kz_t50igJIfXtqjqXgdGZ0Dcaa7_I7pJG45elLEU1sWhLfHUmeIAP5tKhqC7395hDfu6tR1qZa5FkcuyZ0-rIEG3KtXZC23bw2pA43Q2tv4UZRI_hi9NhSIcCkiBRw8OoDBtzqmLA-hiotGp0Laor5WRiH8ux15IrUl88o8kg06675qHD18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام گروه سنی ایران بیشتر در بازار رمزارزها حضور دارند؟
🔹
آمارهای منتشر شده در گزارش دوسالانه نوبیتکس نشان می‌دهد که ۳۵ درصد جمعیت کاربران این صرافی در بازه سنی ۳۱ تا ۴۰ سال هستند.
🔹
آماری که نشان دهنده این است که حضور در بازارهای رمزارز عمدتا توسط افرادی انتخاب می‌شود که در دوره ثبات مالی و شغلی و اوج توان تصمیم‌گیری اقتصادی خود قرار دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/672536" target="_blank">📅 13:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672532">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
گوگل با هوش مصنوعی یکی از گل‌های خاطره‌انگیز پله را بازسازی کرد
🔹
هوش مصنوعی گوگل موفق شده تا یکی از خاطره‌انگیزترین گل‌های پله، اسطوره فوتبال برزیل که هیچ ویدیویی از آن وجود نداشت را فقط با توصیف افرادی که آن را دیده بودند بازسازی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/672532" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672531">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده جاسک: آمریکا‌یی‌ها زمینی بیایند با تابوت‌هایشان برمی‌گردند
عبدالکریم هاشمی، نماینده جاسک در مجلس در
#گفتگو
با خبرفوری:
🔹
زدن راه‌های ارتباطی بندرعباس، حمله زمینی نیست و دشمن می‌خواهد ارتباط بنادر و دریا را با مرکز قطع کنند. احتمال حمله زمینی را رد نمی‌کنم و اگر این‌ها پا به عرصه خاک ایران بگذارند، باید انشاالله تابوت‌ها را به آمریکا برگردانیم.
🔹
هر راهی که زده شود، راه‌های جایگزینی وجود دارد و انشاالله به مشکلی بر نمی‌خوریم و ترمیم خواهد شد. اصلا نیازی به خارج کردن مردم بندرعباس و اینگونه اقدامات وجود ندارد و راه‌های جایگزین برای خدمات، کمک و پشتیبانی وجود دارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/672531" target="_blank">📅 13:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672529">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj0jNGtZFprJJO3BlRNxRgDnNbnwTkzmxUFlNqUaXWHjIqhTCl72fLnfaOF0brzlqO0H8zz632IloaRHZjMQsCOYDJZ9BRnYpV7NsVhUqyFwQxErQUHcMk_aEM39siZdH757i67KJUiRZADAh77pGXJLAHoiEb2F0slgw9M-2Z_b4vL0a2lS6A4KFTtR5WOwkN1rRrktETNq-zScI4Eam40s1W_0qqb-4nzrY9rCvPjz5SXH0UVb-HU5o31kFFwHXcnI5TQpSR1OQibRCENL_DZcefGRejZGn8n2pcr9CTysv-xTXT_VbaV0_3zRA3DYjDacKTyAEJBaJECr9SgBRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه ۳۴۰ نفر در دوره مدیریت پیشین کیش‌ایر در این ایرلاین استخدام شده‌اند؟
🔹
پس از انتشار گزارش‌ها و نامه‌های سازمان حسابرسی که از ابهاماتی در مدیریت قراردادها، کنترل هزینه‌های مشاوره‌ای، اخذ تضامین، رعایت ضوابط معاملاتی و انضباط پرداخت‌ها در دوره پیشین حکایت دارد، اکنون موضوع استخدام گسترده بستگان، آشنایان و معرفی‌شدگان مدیران و برخی مسئولان در بخش‌های مختلف شرکت نیز مطرح شده است.
🔹
بررسی اسناد موجود نشان می‌دهد که در دوره مدیریت پیشین کیش‌ایر، هم‌زمان با خروج یا منفک‌شدن حدود ۳۶۰ نفر از کارکنان، نزدیک به ۳۴۰ نیروی جدید به مجموعه اضافه شده‌اند؛ جابه‌جایی گسترده‌ای که به گفته برخی کارشناسان، نیازمند توضیح درباره منطق مدیریتی، فرآیند تصمیم‌گیری و معیارهای استخدام است.
🔹
اکنون مهم‌ترین پرسش این است که آیا جذب نیروی انسانی در آن دوره بر اساس نیاز واقعی شرکت و معیارهای حرفه‌ای انجام شده، یا روابط و معرفی‌های غیرسازمانی در تصمیم‌گیری‌ها نقش پررنگ‌تری داشته‌اند؟
مشروح خبر
👇
https://B2n.ir/fd6213
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/672529" target="_blank">📅 13:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672520">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjRrW3KgiJLt6rzKz_IjQzB8LiXxbw0tq7HjZeWzTMLEXx4D6R8rU1-S9kbIhszEvfRw-O2vgCRwFECfkvKLi6lSWPMeiz7Xe5P3Ha-IdeFqvZXSVvMNPc19ejt7ds9nPXydYI-mngdVlDfSw6Bo5EH-6AQGRNVxwXm30DxdUo3KpxOerYRGkXzwuo3fekDULXC0Qe31RzN5mhhb1x-lXx-6ufyUcFS42I-IUW66xhVDMzLhXSIpS6G5Eu-T2MGu3www70yRetR79QWqLBbtoyVSot6kIqJ9zr5TUhjbJJ_Bj5KX4gvD5BUSGlM8jLA8sP4LVfLoBlhSJGdfR2gRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4U6_tIB0V98zzaunOKdYRgJTuzYZHXcw0mNSj4m-wHoWi8IcftvDfOEdZBJYzY1PwJ2KwI9t27p_ZXqi3EP1I6SsQ2ojbUIp-0cT_eGSGl-5IdT3S5RkV4AXEYsHtsyta9PzYVlfuLLfMTiJoR_biwAliC_xOfbvsPM9Eyepv7Pk8TGWTEPyVz6WQG_xbs2H8ZzpYGi9R6iEfkAZCJaadWjbXSglZQUQ5rxN2JmRFDGa4Zp4cdVKqBU0QTzZTXspidYCcw2Ich0xKM_c0C24_zGrjJ4lB7_CH2Jm4CXL0CN3E7NgZnCGDmZTSumSn3S5vYhoixxTcokZRnWWQ_nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kD1L-lb75V6qlOP2P-cpSjLSzGa9cFwYvk5Vp_GfTuNhVrQddMlRESUfvZwkrzm0Z6A78X7-5JO5wdVi3tRAQpbt2ZHHQZHxJXm-3wt_uYD2hqTN2JTuSMCpqaq_yJDZVn8oZQQXoEKa5u0jMJlxUA6gFS0n916r75Acs-tPqMyq2Uin3G7p1eSkmAwyde5bY6ay3XkXbDsx-q1KFww0qgMgFZkPR9s0soE6mdWBHodcSg5lfy4PI_GPDxmgxcLBaWEwFdx8UFCGJCqxwl5xqIjY1C0F9no30-tWagM8numJ6SIv2XTM69tUWO9NzIEUw3hp_gddhLtYJNz8hr2Bnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phZVUd5V9HGi3R3Qg4XLJoVTzakJVBovohpOyzoWuQqG2DPhBA5niUeImYrJJxIAQjI6vNWwhJoLP553GcG_coDL2ejnGVg7JjNp_tqq4LelJxfkmj8h7N3STfxf6PQCy-RY2jGPKIKtEbMWWWNtOXQU3mAsHrSoKSfbrp_qzAcRcgSQFDoAkVcWSm9Vs6IJoECHYdd4c7vvMV32lwouKJZh16u_uXIDskcXkAAJVVnlGPd3e6BnlIsRti0yjNjl7hhCmmVTyAaTi-w5Ev3NUSGhcM5U9L971EJg9XnsFVPk5oHEhvP0zwfuAc9c16tZuGkcPnW3SnhdTZ8-cwkPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBryRxvwHghYdIjHTTK2056VU1ZpCpO5f05A2bGV30VOZZzXIJOvgwNgoioRFphLRCpXEu54NCadGO0B0gxwy00Zu9tBO4oQkno2ad9r4-gLhF9KcpkjMQugYu-t-Af4BzwJQRCrgYfVh56vFExyd4IlLo70Hk84jgDk4gKZcobGWKLamJAUNAEKP2N-qsMv1vytq0_XhSzIxWIB16wJF0w4znc188o_AsU0Fn7QHZHKcrmjgD-D2QTxZOQrUXi_Vhnd6IQdkwZWLgVVdkJxcLoU20_MO5cvvcD-Y3AGRkGVWYGpWxjUrkcrrhEHyHStbW0tsl4k7v-x7I-gFq9GOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiBfiReZYPRvmr3bvm_hPHOXsGShe4oXoyUxfUIrl757JJ7wWeY4aeNoS6GSvHzfbQH9AQxZ3GlV8JoML8LueSlHXr5yT89azS8TElJsVgOTu1-3zqwMRk4QpFsv6KevKospJQwdTBqQ_NrMpUSTell1klgg0xBh1xPa-msrNfJIoeOeLqDePdfATMvxRIEwguZkg8qnWjnOmAeQ8AJjH_FSsJYspYxLEH1DZLbj8HW1KieiJi4c8t1qojYGdB1cbUK-AeqsDe6Ol7OpM2qfK7aBxkW3hzqAbUOIBp3nZjQMXyLj9JQn6kTOZ3nmUg9TBIsQ1DBNz3OP5S_wDJl5iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9pMiAbzv69hwHglLgkk1uC6uO9IFnoL31WYBMzADvBmkAMlhhYi-gsiiVOMCX_E0HY7uzXhvUwKhdkkaGandkr_HDo2WnUooc62GWgtvcmnZmlFTR-5GHa1fuFr6OE9k8meNHdW6HCgAtKFOVy_DLKIv7IBr6GQje401vl-lqh9rdfQjHTu5whjeAjMZMad297HZaNtqVvs3v_0-TH5c38IHu13omsAiOTn36HDGyNNI2rDu-b-qVY3uV4XB4DGlX8F88OaUI9EdooMG_EHsumLjZsp4VKF6hKyFMWmMqcuuCm-IB5c4wkVrFpbV95EWfkB3UAT6iRUjIhYtQ3zVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJTJX644fwwCfomfRM6UFjJ964nIA2tbKvSZsqH58FEjBlX0d-sIJftMG2_XR5RVSyl_qOerW7UhJv12UafpO-WQVy3ZTGz31169WBxsBtV8BUbDRr1ow5e9AR-KBp38L8srXC-dYT90O6eE2PDHGWDIIecUloJExOtCtJl9V_dYvDLoyETseBrVWua9ePvOSouj6PYLjcHnZlq9wFhYfJ6T69_uiR8LpEF9Do6V2OO2arzhHHcTOemHiLeQPdNSgrW-QSFDgFlIk2IIqclIaBooQtlKzHKyTiRKZ7R51jHbwSBWnMFkdlGkAn3th6BuTBK4r6Hy6g5A_Lbprm5YVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وضعیت پل محور بندرعباس به رودان بعد از حملات دشمن آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/672520" target="_blank">📅 12:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672519">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران؛ مشاور کسب‌وکارها در مدیریت نقدینگی و عبور از بحران
🔺
اتاق تهران با ارائه مشاوره تخصصی و رایگان در حوزه مدیریت مالی، به بنگاه‌های اقتصادی کمک می‌کند با مدیریت جریان نقدینگی و اولویت‌بندی هزینه‌ها، تاب‌آوری خود را در شرایط بحران و پسابحران افزایش دهند.
برگرفته از ویژه‌نامه آینده‌نگر «
نسخه سخت‌جانی بیشتر
»
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/672519" target="_blank">📅 12:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672517">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6dbe7790.mp4?token=MTdjaGjuIaRQfVcztzWGVGJpbiB5LkOjQeioE4QOAQ-YZl61yr80d5TbJ1ZYMqG5wXHiWVLTel7-MxWlX5Xldkp4obZtQYNB69ik5sTiFzvvybfiYr2jP8jBjUmG0llgDpkpDzTMECO1MEnw63e-9JREOv4uEOzbYvtA5FxRK2k8btgmJ8nIJwc3FGoNMHxnwzCuOxy6PV_19aZN4EmUBv18nvPcvDIG0_CMFGkxCJQ0p9dDPc0Ki-N7q-ud_aD7TiPkcQ05cNXKCoT3E5vS2UnHyZuIq72Rk7Gl1UBJWGXAUF3e4EsJWgrtaAMB2F_Wo0neIp9LhBJLJLxxE5tI9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6dbe7790.mp4?token=MTdjaGjuIaRQfVcztzWGVGJpbiB5LkOjQeioE4QOAQ-YZl61yr80d5TbJ1ZYMqG5wXHiWVLTel7-MxWlX5Xldkp4obZtQYNB69ik5sTiFzvvybfiYr2jP8jBjUmG0llgDpkpDzTMECO1MEnw63e-9JREOv4uEOzbYvtA5FxRK2k8btgmJ8nIJwc3FGoNMHxnwzCuOxy6PV_19aZN4EmUBv18nvPcvDIG0_CMFGkxCJQ0p9dDPc0Ki-N7q-ud_aD7TiPkcQ05cNXKCoT3E5vS2UnHyZuIq72Rk7Gl1UBJWGXAUF3e4EsJWgrtaAMB2F_Wo0neIp9LhBJLJLxxE5tI9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسمت چیه؟ احمد نادری
🔹
کلاس چندمی؟ دوم راهنمایی
🔹
کار تون چیه؟ دفاع از خلیج فارس‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/672517" target="_blank">📅 12:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672516">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKj4wkMRsyU5r5EYbpso_p5YlGisnv07oFUvT09R0Z1I5roiS6c78nh4QaJKG82P8PgckXzoMF0l7Rqjf7ztsz8HoZbHAnL9mCfhYfaVrgBKp3rLtpQr86qO7rLtWsI4ZyN9xKZhnj1_ms7nSAQlj6jSukPlxlq4Qe6m37RBCd56HeaO7ve5X6Ej5n58ohq37U2m4sdb7ZYCzYzDi-zEboAdQpxKH7RVQvc5MZxoM9G9_Ry5vT6bYZJnkMnC2lqDRFq8duq-XsX7DIgTQ7izpc5P2SAg_t2JxOAg-godyx7cXx_UppPwFF7EE1OmFLSfJs8KDT-jiSJL224XOfOXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۷ تیر ۱۴۰۵؛ ساعت ۱۲:۳۵
🔹
دلار امروز در بازار آزاد با جهش حدود ۵ هزار تومانی، معاملات هفته جدید را در سطح ۱۹۳ هزار و ۴۸۵ تومان آغاز کرد و همزمان، طلای ۱۸ عیار هم با رشد قیمت به ۱۸ میلیون و ۷۸۰ هزار تومان رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/672516" target="_blank">📅 12:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672513">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0935780bf5.mp4?token=G0vL1eUXvzMbFLbAtC94cE2PPDgsU4b-UuTIgtfRcSl63BAe2USWMvEG4b6NSkjKCHkFeaiCx44cRwFRpHR42Du2dZiCPB5GwgSiEIZLLTMqug2-D5NBOy6VOYCbLKSoJ_VDPkG2oGH7u_k-0vN5Q_cL4e3W_8tOJmyOXw2lS2g4ln5u-H41Qn1RbGtewmTiL1WIIxKCE7kOyIBxGmkmiecTOJlApYTaVLjFZVPHfeEAvzQkd74u1kpdfBpFFT1bkVbhIm_odMHImBHsxk1h1xZOekA2pokqyjWyBkH_5F3GAbxLJOrWW77a1EzJZKCta7Y0idzUMO2cpc_20VNfMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0935780bf5.mp4?token=G0vL1eUXvzMbFLbAtC94cE2PPDgsU4b-UuTIgtfRcSl63BAe2USWMvEG4b6NSkjKCHkFeaiCx44cRwFRpHR42Du2dZiCPB5GwgSiEIZLLTMqug2-D5NBOy6VOYCbLKSoJ_VDPkG2oGH7u_k-0vN5Q_cL4e3W_8tOJmyOXw2lS2g4ln5u-H41Qn1RbGtewmTiL1WIIxKCE7kOyIBxGmkmiecTOJlApYTaVLjFZVPHfeEAvzQkd74u1kpdfBpFFT1bkVbhIm_odMHImBHsxk1h1xZOekA2pokqyjWyBkH_5F3GAbxLJOrWW77a1EzJZKCta7Y0idzUMO2cpc_20VNfMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوستالژی موبایل؛ وقتی اریکسون با کیبورد و باتری غول‌پیکر پادشاه بود!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/672513" target="_blank">📅 12:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672511">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_IMP9jAGV67O6Yk_ofMTbxDv9T1ZfRgA34_T2OAJ6UxPUZyTH4LnwSl51Wu6qSUQ3TP4iyF-s7MmHrxoqIx9a_yB48gX6oP_J_XWgzeVQrKS3mPm2vgu_8FuDhmU-yIfs5NKnAH3xXFX_zxldxrw2UQOuuX2nCeeaYUeeOraFp_v818kNxtI7Rkx0ZLE_Wqw7xkTPiosRadLXkYzi9PCRcnNdWkA0dB0Qh0FKOzOHwl0KxpvmLilbndX58C0sFF4j1PlaRew_mOO9QAIFX9HiCHkAW6SrX-NsYnmBy-AYIhQyMjnH-GVWHurFEhYK4H0KCmD3qpLWyNoEW2Ve6PhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خانوارهای شهری در سال ۱۴۰۳ به نسبت سال ۱۴۰۲، تقریبا ۲۰ میلیون تومان بیشتر می‌توانستند پس‌انداز کنند!
🔹
طبق گزارش مرکز آمار، در سال ۱۴۰۲ هر خانوار شهری سالانه بطور متوسط ۲۵۶ میلیون تومان درآمد داشته و ۲۰۶ میلیون تومان هزینه زندگیش بوده اما در سال ۱۴۰۳ این آمار، ۳۴۳ میلیون تومان مربوط به درآمد و ۲۶۹ میلیون تومان مربوط به هزینه‌های زندگی گزارش شده است./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/672511" target="_blank">📅 12:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672503">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sG0XlMomey6oXJKBG1cLN5Oc2XxbITMISrakUXjhg-y8ycbB6SqYDRwe4QjRtlah6oxfDpwele7XpKYSSYREcQHf6jVIj7uqr3XY4mwnFgCT2HDmqsCDMOZKwuCQ3fz2GyGd74AJriBnaskzvCpabnCSB7nSd4ry9525-rP99lraWdaiWznpacBLnlPkpg-eZY2E643c3TYkoXkN5h7yJFqc4oRHbJYTQt4Ev4mruSRhgCfYqL43QU4bXNvEuYrwQav5fyEBjtt1YwtNf00WpL4d2QeFu8wXKz1l0k6DM6-38P9BMQEJorNOQms70Gwn05s27nXJQYoYnonQcdcCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lf2-DPRg3Gat5jSgYTe8oqCs9t7tfJjpOYoE8wWzGIz7EAfdfONWSlo4aCwkV4v7uMPCr0ziuLjAa_ylm_hDHrKly-SozyjP2ddomGHbS5ExeUAlncSq1q51YK_i6qI6a9cOscK-3OVke0rODb-HjprkI94EYR1AkS85Rjn9RRNFv6Axp40X7LfGGokd1-VSo2re-t82F22TQFPFVOMcWG6ytogfOU6-xrMnXoyrQ1ujdliKw4wn8NXAbUtY9bsbbgb7un-Syp57je3rhHMKboXOp8yc3I5jjVicbTAzZkaPmzuze2WLpVKSz4FzfjI-URGNixMztl1gjVwBiLEKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNaRXi6HeY7VqcVVHIklJ4ZV9j92mGL7aL8qSu6DrEqomcBQS8_R9F4uRhE-jkG0fCWssEZYhoiRPtxTCJbV42sXnr5qRYZOyfLAx-FLwPXIn_lZ_kvbfXSwQr6oVdLx6oUrI0KUvoA6govFPEeZ1WAic-dsDa6DpxrMs_PX8OulpLQgzwd3I_EwUCnYwgWUpTL1vE1l6skxAWqbhjRcAwHs2VVxgQQhiXoU0MDW5F_Td4x2WAjsQL00UOdCvGtyzOMtpBMyWbpuzSQmKrUgBYsnh64KIjVbyzMfIP-kWBgzL8tJMd3mnGHtzeT1MOWomr49uhANMlf1j6nhxwusnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvid42XnNkeJkTmyLhZVTBfeMP-ayry1qZ9c24UIu41T1HAV_d0dKIMd84pg8z_wniC1KszVQ_91zCw7JqlqdseOHwOf-RXeJP8CX2N_m38-UB5as7TbAJoGeD_P42Wtvz73jUHJTo-SDCdSbmlquBYh-ViPwrUmRaQDfRjo1z9fAWXWAAwIp0nVgjqwaFzNvBD9PKblgUdBngXuz-802HWakFPptsaNrzcRRbqfzeB8YGZzm-sTti5rGgWY6oRx-KdiMGPGEduGEdcOzPcZfe9WvfZMo7yxaCbo3ISHmGsGRUQOkGb0xoREuT3JRRLS-k94N3BjatGLIaW31aGftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CgXulAwc5Z16F9tMI_zP6hgFsVnbRh8h5nR-fRsnczQPySEqMWHfQ-aP_8oms5V1yKutaWdy8_YDBsaoyH7vLqo_h7GniEnzmR6ROgzlHCW7T0FtTIZxdf2IHcoRpwh4zcPSEFeRobbYNzhc7MCGPWZrcHHWTnxBbSFAHMJyjFZnM9fwmCgkvYdN-lXOfCcHhMIvhQkdqS-X_37Fsx_BebdENPfFTSO5Tbm3fMhhZN0TEHbSoWuGaO-ZssSz9oLNNiF9K0oLnML7UCb-Gy-pQ0fXkq1emVjvErkQFjWtHSLbPpUGCdxG0dhq3vN78AlCGIJTMOna9Ft8eRL311l79g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAw0E6Et0KaJ9r7quVygt8nL3eEFggbcB4rRLbQ1-epLefWkIVJi0qKECKQwzFUAy316Y9O7fXMxzNBF1bIqmcDS2xEtXvFC9I0RG6xElbKRUb8Tqz7-JsN5iZisxwGpjKEJKaDjVws-1Ds8dCAQgFK63z4sY_trKC6pNV3aShS6iOX71GgyiRhJzdR2vciwUPrdc4tdcRV2JU54JzkK3SVClm5AaRu-Z1DHSVaEK_5hcr9e2o5LgTHuu3Pf600F6yC7-ZdDigYebdAXx5BQ3ghd2fN6-AskPVI6wUhcGFEVQDPH1qVfarKh0X1GxnJ8xfeaBEicZWFvECb-5_mi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgC3FhryYXh3v4_SYUnv8ctA6_P9Mi66gmK_Cp7A0ywYVvF_wJbqiLxdtBMAjE8jU61m5g9Xcs3xjN95RC7Hs_U4_DtWQP9knUbMkxsuyhYgwmh3f2Z03EgeFn5pZ8t9MR8FhmW1eMyR5o-mZzKEltF-YY-9hCn9gYWXH6anBcEYA-d0i5lfd-JXEb8l-44IXziBaxLAeyvxi203wFuLiQaTh09f7dn8JzAAju_lTlw0fOMvOAMjrdXoVvU4g-BUh6zLKmItJmBxK5E67i5D2AWRZF9h8y0Q2lAb1A-kYnt7tUNwm0xPmH4jakfcWIgab0ZAMQ4QhgyoPNQuRWP0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcEabckDRa49xbH9puuaiE6MKdPwPrnm0QFEt0eEGI8q-q3RgTSCQUMvuLM5Arg2VI8gugrDLOquvVdlm6efh1d8gcB8raiCH0x5dk44IirjYrjcZCxFKGNAYluv2IJPXW_E6sjJ7quuhTaveQOy5CFY8HXcML5X1KEz9E2F9Gi-r0fR8dCGxMFbet3Iecq5CWZwURXu-CjyZoYbXJzFmKSYthBOkGxdlnq17svxnZDvBSzsp-pLCQFotMNHbSP6xZl5KM35ixswymV7uuddj9WD2RspU27K-HQb6BI2WLxDL0HbGRNdvfWqqPF9bdSaLq-NiwGOAZtksIk_NPTMdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌱
کمپین «نه به پلاستیک»
🔹
تغییر، از یک انتخاب ساده شروع می‌شود…
🔹
در ادامه کمپین «نه به پلاستیک»، تعدادی ساک پارچه‌ای از طرف خبرفوری میان مردم توزیع شد؛ با این هدف که استفاده از کیسه‌های پلاستیکی کمتر و یک انتخاب پایدارتر، جایگزین آن شود.
🔹
هر ساک پارچه‌ای، یعنی یک قدم کمتر برای مصرف پلاستیک؛
و یک قدم بیشتر برای حفظ طبیعت
🌱
شما هم با کنار گذاشتن کیسه‌های پلاستیکی، به کمپین
#نه_به_پلاستیک
بپیوندید.
#نه_به_پلاستیک
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/672503" target="_blank">📅 12:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672502">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
اسکای‌نیوز: آمریکا دروغ گفت، آنها به مدرسه میناب حمله کردند
اسکای نیوز:
🔹
تحقیقات تازه و بررسی‌های مستقل نشان می‌دهد که برخلاف ادعاهای دونالد ترامپ، شواهد موجود مسئولیت ایالات متحده را در این حمله تقویت می‌کند.
🔹
به گفته هفت کارشناس مستقل و سه منبع نظامی، حمله با موشک‌های کروز تاماهاک و بر اساس اطلاعات هدف‌گیری قدیمی و خطاهای اطلاعاتی انجام شده است.
🔹
همچنین مدل سه‌ بعدی تهیه‌ شده با همکاری Forensic Architecture نشان می‌دهد مدرسه هدف‌قرارگرفته دست‌کم یک دهه از محوطه مرتبط با نیروی دریایی ایران به‌صورت فیزیکی جدا بوده و حملات نیز کاملاً دقیق و هدفمند اجرا شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672502" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672500">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoyAJ-Qg5urryuRjSgILPvuaNWOCmN6eO2VGujINS6udnqjm0-X0ivOCfJetFIAhp1mOJUzax2o_FN0wX0tgj6CoyG29gQJCdhmEbUT0a6ICqa1rsdX7P4Xoi_pzx0Lh5A3PedE0wpvqyLR77vwUN4fSuLiPfaUmFUNemvgawXJH1yCXOTTY232n7maMYv4y-7DcPaKwiuKkDNjk76JHZi6rdl0_oDrpJA0PdWzwQ4MMPDDG1bcXLZJLz4QmfSSqXo8_Nz_2GdnbKbvteq0k16qOr28ymC6sZVwR44_lwoEixLn_Mpd-244uRJOCRH3XnzhRl_DWPJh9DTAcl_Q7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی جنایت جدید آمریکا، آب شرب ۱۰ هزار نفر قطع شد
🔹
در پی حمله وحشیانه آمریکا به آب‌شیرین‌کن بونجی در غرب شهرستان جاسک، تأمین آب آشامیدنی ۲۰ روستا با جمعیتی حدود ۱۰ هزار نفر به‌طور کامل مختل شد.
🔹
این آب‌شیرین‌کن با ظرفیت تولید روزانه ۳۱۵۰ مترمکعب آب، به‌طور کامل از مدار بهره‌برداری خارج شد.
@amarfact</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/672500" target="_blank">📅 12:14 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
