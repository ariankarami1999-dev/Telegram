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
<img src="https://cdn4.telesco.pe/file/O3VZugERr3gM7CQiSTcVqj89hixXkwZw9cpdU05JpmpRGBg-Y-60U8JyZs-qratoAIxlg-qVUYkA4iAv8nOZBIeboT950jFN-J1fH-GzRmlK77o0KtipIBru0WjsK_0tGJ1vMLXlza_2F0QXWj0LaiiMAm5DJGeayzoZgXaq4Rul0fukZua2VBNh9TUHiOe0mx5pLRbzU4eUEmkTI_WBv7h8A__92AXbaRZ3EHiIONdZejXNh25DdPisBjcPkR9j6Nb3F-NaFkCI_I5K5IPmu14IGY9cs3o3PDr3nk2gKgXtA7zbUP8kBtcEukYQEXXfTBqMnvOHicqtARUPpWIRaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تنويه…
🌟
سيصدر بعد قليل بيان المقاومة الاسلامية العراقية حركة النجباء
.</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/naya_foriraq/76884" target="_blank">📅 15:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
الدفاع الكويتية
: تعاملنا مع ١٣ بالستي و ١٧ مسيرة قادمة من ايران .</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/naya_foriraq/76883" target="_blank">📅 15:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76881">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad5f20ed9.mp4?token=RaFHHTRbAk01Gc_RHLJS3KF-z0OV9WDCgwQYeESe-6_9aBaFmfq2Eryb6jDzKP9BzrPXhibBAJ0kGq4bM06yBMW6pvaTgPFalfr-qZ0825OFlyNCT4eIN_fTl-PwVjA2mzQCYqAnuHYA7Fp8nIH6XD7ZPbZGe8O39G6_n1hLmTPkN1vtAZnCjEYvsCnLH2BgLlTKU-gbFajPaiwhzNgZ_RUAtMP-MBF465wRkjWbA-whbcTnzBu_rNOKm2VMdKLNbbR-vOuCnJnLbLIF4xZsQfTCVYDmm1reAhMqFcl36n0A7nu5wymdrWViYp6K9ooOx3DWCy8chgUBUpqIB444nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad5f20ed9.mp4?token=RaFHHTRbAk01Gc_RHLJS3KF-z0OV9WDCgwQYeESe-6_9aBaFmfq2Eryb6jDzKP9BzrPXhibBAJ0kGq4bM06yBMW6pvaTgPFalfr-qZ0825OFlyNCT4eIN_fTl-PwVjA2mzQCYqAnuHYA7Fp8nIH6XD7ZPbZGe8O39G6_n1hLmTPkN1vtAZnCjEYvsCnLH2BgLlTKU-gbFajPaiwhzNgZ_RUAtMP-MBF465wRkjWbA-whbcTnzBu_rNOKm2VMdKLNbbR-vOuCnJnLbLIF4xZsQfTCVYDmm1reAhMqFcl36n0A7nu5wymdrWViYp6K9ooOx3DWCy8chgUBUpqIB444nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
سُمِع دوي انفجار عنيف في قضاء جومان بمحافظة أربيل شمالي العراق، أعقبه تصاعد أعمدة الدخان من موقع الانفجار.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/naya_foriraq/76881" target="_blank">📅 15:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76880">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
🇮🇷
المجلس الأعلى الإسلامي العراقي يطالب بتشييع جثمان الإمام الخامنئي (قده) في العراق .</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/naya_foriraq/76880" target="_blank">📅 15:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3070c474.mp4?token=pUTntlF2arvm7bKFGTYSuFQWmdb8EG3EK6BuqhObFxQkdSZG6PhOTC-5AVULyB2p-aD2SXopAH5cAg_DrTJs8767nt0D2zReO41bfFBfhpIXW5-qcvXdc552wDrMo0xJGrDiLd6obkf-zcE9ZMAhE-J4TW9I9xoa6Iqn5H-o7FRz2f96R1PC-tol3c2LZoYZ4F6_ax6_6vv_3Km9kpi2vybzraLrQFfuTMyvLAQqeEW7Moz5s94v6OTYBMdg78-vDBk7Qox6hVcem9t1nMY198KGvEAXDSqT8_6AWgUkgqTecK159bLy-O7DHXQGYdUnNnDgorUHluAz9QdPCQlO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3070c474.mp4?token=pUTntlF2arvm7bKFGTYSuFQWmdb8EG3EK6BuqhObFxQkdSZG6PhOTC-5AVULyB2p-aD2SXopAH5cAg_DrTJs8767nt0D2zReO41bfFBfhpIXW5-qcvXdc552wDrMo0xJGrDiLd6obkf-zcE9ZMAhE-J4TW9I9xoa6Iqn5H-o7FRz2f96R1PC-tol3c2LZoYZ4F6_ax6_6vv_3Km9kpi2vybzraLrQFfuTMyvLAQqeEW7Moz5s94v6OTYBMdg78-vDBk7Qox6hVcem9t1nMY198KGvEAXDSqT8_6AWgUkgqTecK159bLy-O7DHXQGYdUnNnDgorUHluAz9QdPCQlO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
شرطة أربيل في شمال العراق تعتقل شخصاً بعد قيامه بنفخ بوق يُصدر صوتاً مشابهاً لصوت المسيّرات الإيرانية.
كاكا هاي صوت مسيرة من باب شرجي
😆</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/naya_foriraq/76879" target="_blank">📅 14:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76878">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDSKs7tlhM-KjVnGsOIjD_rpkeSEbsv39d5ELj0fYVpKb6i1yGE5DCqDdlY3CbhWgG1SzEteBqJxMqD1qsp_mjEh8izhDl9HlArbdoDCLlqu7igw7TGkGFIL253G7dfN8IvetI8G2shpohUsArNHNOmdWNitffoT6jb_ZNgnSWBjtqj7yHz98ZjNEMohqFitni2fYCSwUHVfF54dtAaDeTTiy9iaDLrqjgEvdkwZLHZ4LSEQrhpHeJ9iFvGDw3CQvg5aN8J60xPas9r-j9IFMd90xlSiyFTIX-FCcGFEH8bKUBp1011Z5V3ny2UrFt38phDfSptz8jRxiY3a-8U7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
الجيش البريطاني يعلن عن مقتل أحد أفراده  في شمال العراق خلال حادث تدريبي (حسب وصفهم).</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/naya_foriraq/76878" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏
الصحة الكويتية:
إجراء 7 عمليات جراحية كبرى عاجلة بعد الهجوم الإيراني، واستقبلنا 63 مصابا.
لا لا
يابة سنتكوم تعترضهن كلهن
😫</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76877" target="_blank">📅 14:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
الانفجار الذي سُمع دويه في جزيرة قشم الإيرانية ناتج عن تفجير ذخائر حربية غير منفجرة.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76875" target="_blank">📅 14:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1c8f3530.mp4?token=uOwrUvaekUYOcbciq7Ml13FNB1FvEb07rS-j7NFI23ys0ARPV9Gv5DkHtYPkwsMPpC_35Akva6_PD9YDgYnlh9u-QL6QEfrduB8sSiBIcQOpHzUxPz1FfK6x5FWt9szx2XuE_QB7-O92zukfoxI55NCIvsXtAeBw7rAZhXpkhVOGDgV0_XLFpL7pT7X2jyi-zfa-KA96eKUiMUp2VEx6J5b_5Uy7PxPktFV7IA4Eq7dY6OuDVInn7m1l7WMOXx5p22qwoaSuwiqNlC-Bvk7YmTdZU0k3xakXhmYkYPaHveaTo0IBX_7bAyZu6avmQSGR9VFSyju6Q4FHbH_lYWV_Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1c8f3530.mp4?token=uOwrUvaekUYOcbciq7Ml13FNB1FvEb07rS-j7NFI23ys0ARPV9Gv5DkHtYPkwsMPpC_35Akva6_PD9YDgYnlh9u-QL6QEfrduB8sSiBIcQOpHzUxPz1FfK6x5FWt9szx2XuE_QB7-O92zukfoxI55NCIvsXtAeBw7rAZhXpkhVOGDgV0_XLFpL7pT7X2jyi-zfa-KA96eKUiMUp2VEx6J5b_5Uy7PxPktFV7IA4Eq7dY6OuDVInn7m1l7WMOXx5p22qwoaSuwiqNlC-Bvk7YmTdZU0k3xakXhmYkYPaHveaTo0IBX_7bAyZu6avmQSGR9VFSyju6Q4FHbH_lYWV_Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
ترامب لنتنياهو في مكالمته الهاتفية:أنت مجنون تمامًا. كنت ستكون في السجن لولاي. أنا أنقذك من الكارثة. الجميع يكرهك الآن. الجميع يكره إسرائيل بسبب هذا.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/76874" target="_blank">📅 13:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76873">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2702a18eac.mp4?token=AnrTSN5t5fPoEiV6GX9y3T-EOLQJ5E3pRu9FSoAlBYpUnHMRqcdgdNDLTuTc8VHHO54gcsGhYd4Zwc8OiZ-psOkgG6XtlCjhgv-ERjz9-oZ_nHhrVZmCclUvhGh7M8Nl6F5hW000JBbbl99ahtcYvNdLwiOECqM2rGoxptZbDUzRrCn4gUNF-RTrJGSyllJ9HYO0EfBg1ZlMNp-_zbRsS5FqCd1LDhoQ1LZ2GqyNCHzU-Htdkc9I-AhMb0AKcADQFg_AfOHJKBZGznmYd7wkNDlyZNp9fiet95IpKa5qIH9r_MeS2TT9ghnbsNkT4IeEDlhWmefKTFontsIOAGhUAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2702a18eac.mp4?token=AnrTSN5t5fPoEiV6GX9y3T-EOLQJ5E3pRu9FSoAlBYpUnHMRqcdgdNDLTuTc8VHHO54gcsGhYd4Zwc8OiZ-psOkgG6XtlCjhgv-ERjz9-oZ_nHhrVZmCclUvhGh7M8Nl6F5hW000JBbbl99ahtcYvNdLwiOECqM2rGoxptZbDUzRrCn4gUNF-RTrJGSyllJ9HYO0EfBg1ZlMNp-_zbRsS5FqCd1LDhoQ1LZ2GqyNCHzU-Htdkc9I-AhMb0AKcADQFg_AfOHJKBZGznmYd7wkNDlyZNp9fiet95IpKa5qIH9r_MeS2TT9ghnbsNkT4IeEDlhWmefKTFontsIOAGhUAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏
ترمب
: مجتبى خامنئي منخرط بالمفاوضات معنا وقد ألتقيه في وقت ما، وإيران وافقت على عدم امتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76873" target="_blank">📅 13:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ie5bUmQTBNrqO7jF163CznR4vi7wv0RRQtAABXh23ZBD2IvpsU5-XNV-Cx6_lRQjgPgMedtqQqx_xFdEU51wRPqf8guKiLLTI3SWSss7aSJL0za2upODStETpgswlepE35X--n5U8v5ZSbhlCALCZPLGVKfodnYMSqRQ3xq7pGk0SQBUf47hEzVbTexgzbIGj4ejaGHfDptRVkcq57S6cFQjOX6ARd-Cp8fl3RAo6DoXFg6HYiZl3uycbtZwx0KvnRRaMk3wP3m8iQxrQvz_TwqqL8A16DqYR_wITT8dz3PRjKaK6cB2zgUCX50H-p_uGi16ZBo6kIKyZh51tt5x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
نفى المكتب الإعلامي للحاج هادي العامري بشكل قاطع الأنباء المتداولة بشأن تشكيل لجنة برئاسته لمتابعة ملف نزع السلاح.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76872" target="_blank">📅 13:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61caaee40f.mp4?token=GUtCBX1LCGxVwm0VkSh8ReVkaUfm4DRbK637K0u4c7u1k1RGtHdw4RjnvM42sHEWjudUbvZzsaxcxP2eneg7pxIh_b6K78TPt6mqgnf7cYVJ3Ft9FTAmiC2knUocrJ2Zyl1lfp24NtY62NWN--W02Ck1Tjnho2QzvLuIm26LuenmG0lJX70fnHc04c5LMaLGxDPRm-QAlibjswQv0ZMHBGQGM2i9TReyx2GXLIXAId-bUF0ME_eoqGUr-9BvrTZMVjuwjxxRtCY5TJHM7u7f9NTq-Hm3tCAQURlohC6IomjAy-8YhPq6b9Og3B5avyakUp-62Sdf08QSqQP-TpZ8-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61caaee40f.mp4?token=GUtCBX1LCGxVwm0VkSh8ReVkaUfm4DRbK637K0u4c7u1k1RGtHdw4RjnvM42sHEWjudUbvZzsaxcxP2eneg7pxIh_b6K78TPt6mqgnf7cYVJ3Ft9FTAmiC2knUocrJ2Zyl1lfp24NtY62NWN--W02Ck1Tjnho2QzvLuIm26LuenmG0lJX70fnHc04c5LMaLGxDPRm-QAlibjswQv0ZMHBGQGM2i9TReyx2GXLIXAId-bUF0ME_eoqGUr-9BvrTZMVjuwjxxRtCY5TJHM7u7f9NTq-Hm3tCAQURlohC6IomjAy-8YhPq6b9Og3B5avyakUp-62Sdf08QSqQP-TpZ8-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حالة من الهلع بين المستوطنين في كريات شمونة، عقب انقضاض مسيّرة تابعة لحزب الله على مواقع عسكرية قريبة من المنطقة.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/76871" target="_blank">📅 13:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76869">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951231e9f2.mp4?token=HBUacnbFBEVDYudBVqawVhcyVEDrincEcdpTu4cRlQNc1e15voGlkW3PyAO_YxpPrqjgQcFHxUQiohM9Yi9kCmxjeYc3_4dq4UugGf2NObxqM95-Rn7-4MeBo-y8d1BP4iFUcWib4TdDthXl70eu9NdzjVvjKAgvGit6j_RUJbJB5u_nRndDClwMAOuaHevLliJHNLu0-g8d-A3-E6R78Dr6PK63-AZo2I9Lu5f875peDjLG9FQR-2y-1aZg0udzx6wEsE7YNpJvwNLg3Uc3OUdPBpSHQ9OSO9KHfMmI00w7-_kbSpptMg1GVoCB0VKvuEB_XbbF6OUsFdcfaPQEDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951231e9f2.mp4?token=HBUacnbFBEVDYudBVqawVhcyVEDrincEcdpTu4cRlQNc1e15voGlkW3PyAO_YxpPrqjgQcFHxUQiohM9Yi9kCmxjeYc3_4dq4UugGf2NObxqM95-Rn7-4MeBo-y8d1BP4iFUcWib4TdDthXl70eu9NdzjVvjKAgvGit6j_RUJbJB5u_nRndDClwMAOuaHevLliJHNLu0-g8d-A3-E6R78Dr6PK63-AZo2I9Lu5f875peDjLG9FQR-2y-1aZg0udzx6wEsE7YNpJvwNLg3Uc3OUdPBpSHQ9OSO9KHfMmI00w7-_kbSpptMg1GVoCB0VKvuEB_XbbF6OUsFdcfaPQEDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجزت فرق الدفاع المدني من اطفاء الحرائق المندلعة في مطار الكويت بعد امطارهه بعدة مسيرات ايرانية ليلة البارحة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76869" target="_blank">📅 13:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇯🇴
حكومة البندورة الأردنية تعلن تضامنها مع الكويت والبحرين وتدين اعتداءات إيران
😆</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76868" target="_blank">📅 12:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇰🇼
هيئة الطيران المدني بالكويت: استهداف مبنى ركاب بمطار الكويت بمسيرات وصواريخ إيرانية وتفعيل خطة الطوارئ  استهداف مطار الكويت أسفر عن إصابات وأضرار جسيمة في عدد من مرافقه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76867" target="_blank">📅 12:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76866">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🌟
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 24-05-2026 تجمّعات لآليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بصلياتٍ صاروخية وقذائف المدفعية ومسيّراتٍ انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76866" target="_blank">📅 12:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76864">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇰🇼
الخارجية الكويتية: مقتل شخص وإصابة آخرين في استهداف مطار الكويت
‏اعتداء إيران أسفر عن أضرار بالمنشآت الحيوية بما فيها بعثات دبلوماسية</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76864" target="_blank">📅 12:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76863">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d40ecfec.mp4?token=WGNvv1-lNZHfVixgz4b-qvvY0gvNGCC_5CJlAlccxtTU-RQwaTQ6ieHPp1GfaBFJia0x6aOmjn6uO0gwi_AwGlobfhtkBO6txU_pQgp50gpUFlN-C8FZnsOxZ0xiqDpBzZYY4vi_EXzUGC9PygiCYy1rn-yv7yaIAusPHdRCN7T7yZHc4Kl4p6gZGqfIyam3JOeE4z7cSN4w14E5-BTEVRvnQ5NKWpAt_mcwsGogtFsXKb0YXmvtdufto9aFGJsA7B6xuKUqXKuoIp8jHs6L5Pz8UN4a1mvOxC2aA7m66b3b-tmHUxa-uqU9PSrccuQ0hH-QOt8xSQNZbmuAH1Ui_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d40ecfec.mp4?token=WGNvv1-lNZHfVixgz4b-qvvY0gvNGCC_5CJlAlccxtTU-RQwaTQ6ieHPp1GfaBFJia0x6aOmjn6uO0gwi_AwGlobfhtkBO6txU_pQgp50gpUFlN-C8FZnsOxZ0xiqDpBzZYY4vi_EXzUGC9PygiCYy1rn-yv7yaIAusPHdRCN7T7yZHc4Kl4p6gZGqfIyam3JOeE4z7cSN4w14E5-BTEVRvnQ5NKWpAt_mcwsGogtFsXKb0YXmvtdufto9aFGJsA7B6xuKUqXKuoIp8jHs6L5Pz8UN4a1mvOxC2aA7m66b3b-tmHUxa-uqU9PSrccuQ0hH-QOt8xSQNZbmuAH1Ui_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المتحدث باسم كتائب سيد الشهداء الشيخ كاظم الفرطوسي :
تسليم السلاح من اجل الحصول على وزارة هو خيانة .</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76863" target="_blank">📅 12:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0a748bed.mp4?token=IvIiiOpTTNZ37s7NQMKSe0CA928YSQAosOrjru3LOfPbaOgvlRPyAkoevp8wfzjdD2AOtOYIOh2XJGBGT99KQaiCGPleqENZ3HMbQfoNihz-qY9ExTZFp_2e2IN4CbyUZ3iomwa22PHiWmiFWjOQmZcAWIUaN8uMlSgG6eB3jWXc4BlDZ3lQkTsWy3vKJrpwf0l9VCB8DlsdwY9ABYJYuwSjShJ0_yOgDH7Idyjl-Jrs7BfjPsfVCCr6KniI8kp0ybIxuS3fYx5H2AAI2PaedJhqv8Z5OH7bTwV_KxaL1ic4EIndG3epTO2QDsqXD5cMNq4-OnCA-oZ3yXlyuegpew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0a748bed.mp4?token=IvIiiOpTTNZ37s7NQMKSe0CA928YSQAosOrjru3LOfPbaOgvlRPyAkoevp8wfzjdD2AOtOYIOh2XJGBGT99KQaiCGPleqENZ3HMbQfoNihz-qY9ExTZFp_2e2IN4CbyUZ3iomwa22PHiWmiFWjOQmZcAWIUaN8uMlSgG6eB3jWXc4BlDZ3lQkTsWy3vKJrpwf0l9VCB8DlsdwY9ABYJYuwSjShJ0_yOgDH7Idyjl-Jrs7BfjPsfVCCr6KniI8kp0ybIxuS3fYx5H2AAI2PaedJhqv8Z5OH7bTwV_KxaL1ic4EIndG3epTO2QDsqXD5cMNq4-OnCA-oZ3yXlyuegpew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مشاهد من انطلاق المستوطنين إلى الملاجئ بعد وصول مسيرات وصواريخ حزب الله إلى المطلة شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76862" target="_blank">📅 12:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76861">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن رئيس الأركان السابق: لقد أرسلوا جنودنا إلى لبنان كقطيع من البط إلى ميدان الرماية
😆</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76861" target="_blank">📅 11:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a04a5b1d9b.mp4?token=WkpmxzYmHOv4HMhBCSDzyuCQPUtTSdSlV1aBZGwbsE6LR8xP1DypD4T1LPB9zzqIgvnXSQ53Bh7-YBcooEFrQyHPSfvMJCvcFrl1QGSI6hLJsFmg33ElfmyCfOD3zjX06nm4T6hwV-nTaSW9jAY2qqUBWq91cSh6QI3HgW4luxzi2U5zPFM-8wE3Ger4oRK6z3hOekY9MjbIIhpGc2R49z9TACk1PwezpMaW8uhByDtrtkqzLXBktAr82gZHNkVXVxw3Cce0uar-emKjZ5j9mjsEnsLRYYe28jMfY-xtfoIRCkehPKSC8vHplTcE05iiHFDwN2_jKT9IyusSVsKYUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a04a5b1d9b.mp4?token=WkpmxzYmHOv4HMhBCSDzyuCQPUtTSdSlV1aBZGwbsE6LR8xP1DypD4T1LPB9zzqIgvnXSQ53Bh7-YBcooEFrQyHPSfvMJCvcFrl1QGSI6hLJsFmg33ElfmyCfOD3zjX06nm4T6hwV-nTaSW9jAY2qqUBWq91cSh6QI3HgW4luxzi2U5zPFM-8wE3Ger4oRK6z3hOekY9MjbIIhpGc2R49z9TACk1PwezpMaW8uhByDtrtkqzLXBktAr82gZHNkVXVxw3Cce0uar-emKjZ5j9mjsEnsLRYYe28jMfY-xtfoIRCkehPKSC8vHplTcE05iiHFDwN2_jKT9IyusSVsKYUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
استهداف صهيوني على طريق صيدا بيروت</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76860" target="_blank">📅 11:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇰🇼
مشاهد متداولة لمطار الكويت الدولي بعد دكه بالصواريخ والمسيرات الإيرانية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76859" target="_blank">📅 11:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76858">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2KAR5-bYX6Yj5pQ8HePEar-Q2qACedq6C7PXOwl9_SYbGv1n2rHHQLCO5XAayXP_ZG45EG5HzHXUb0uI50HPGvHfg_LrlscFcsOqEyyKv-kMk2y5FbXWEFmrkb2kbAV_KYAA89PAQxJDRJSW2DQZVXCPaAPdDuMuWMuna0G7mvX9VVAoSD-XdxK68_XJVRT3BEoFqjzGb_QFZBnwW0dSDPaXoM8pYPvqbyjxHq3gIDRbXNkijbk68mF-r6ZyC4uO5oLUNR0T02Y_NJdP6cg8MdHCQ26VfzFWSRr4clLTC3simTBFoUGzNo_wZsa7Nt7IZoyPnROWf885ZD7GtyAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
صورة تظهر الأضرار الكبيرة في مطار الكويت الدولي التي أُبلغ عنها بعد تعرضه لضربة من طائرات مسيرة إيرانية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76858" target="_blank">📅 10:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76855">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fu--B_8qOznzV0xwBCSyVkqFnwR3BOWcQOWD6lH8kvUZK-cjs_sSl3uamhNuaW2gjDayTMjx7FisOPoRA8U9ZBTqXpttJHOYJgKEqcbM3aA64d4gIVHPfYMXuUTqkI62u7nQWIl1res1xX0MVpLl2pMQeFKWOL9Y9PeBHrKgKRlt8UvAMMLH7FfpxNtkkZyXF1J4dWuyTUas8khEG9sxkLRZkbgw0VZfGRpeYt7s03ZmsyjlgdUVrq3Bq4KrVdV9fGFdq3L9LF4lgWySP5Sp4czBr--xzE4AQ9ae4HAT_7VIyupqjTMkfMLcKJN7z75JBXt6dto-XYSxLZWJL0rLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdEGF3YnFDHuksbL3mOIo_oI7NSfGAuc-jImAylCAjzHxQjbk9io2h0y-1pGwqu4c_94tlcXaApMDIaPPGJ9-PZKvF0jArNCqkHfttHRrwmDqvDn9K9alTwW1tr-fW5Cm6L4-n3fY6T73dpWtdS3m00JgHcVJUATyy69y-xt4QTEoOLNTT_XS95hfNNlMW_2sKsaZUCqxr4KfcRft-EM5Q3hOUWlJGSw2y8fMb3bHv3bey87ms9yKxusqK_fbn_RdGx5Ap36NwCP8L9Kynwp61bOIm7Svhla9osWXksF4ACv21EvPCHFejLJsSZXjAtQ2kC5XE6O3ifwraCh1BfaJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b244cd39.mp4?token=KtLIUs-Fq2rcmp0BcIPIm7gsvRSeroCNNupyzWp4lhjtZzgGEa1SyqC1PeeMlwoA47h_zDHSCFqONackRokSL-PGNJpJW66I5ifmMj5MuX2CncmDy8dlwtkdZ-Keh0n3yXE6ctpRSg5EXWMPxdcVAxS60whyS97wdl5FqWxlobm30cuzqkhsODwZxd88B04vr9RW_N_jzmkKp-mHgs8zpUnVnLsf3_vHCQcCUc4T61wFVpfrU72BQ_Ntaj6y4cbid5f4sRbAV3kQZ9m0yjw3bRbc2877lL5VsjgZHxn4HbXYhUoVb2iC23xMnoyk0bQpyrzoL_sQItG5RehaV3hdRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b244cd39.mp4?token=KtLIUs-Fq2rcmp0BcIPIm7gsvRSeroCNNupyzWp4lhjtZzgGEa1SyqC1PeeMlwoA47h_zDHSCFqONackRokSL-PGNJpJW66I5ifmMj5MuX2CncmDy8dlwtkdZ-Keh0n3yXE6ctpRSg5EXWMPxdcVAxS60whyS97wdl5FqWxlobm30cuzqkhsODwZxd88B04vr9RW_N_jzmkKp-mHgs8zpUnVnLsf3_vHCQcCUc4T61wFVpfrU72BQ_Ntaj6y4cbid5f4sRbAV3kQZ9m0yjw3bRbc2877lL5VsjgZHxn4HbXYhUoVb2iC23xMnoyk0bQpyrzoL_sQItG5RehaV3hdRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇼
هيئة الطيران المدني بالكويت: استهداف مبنى ركاب بمطار الكويت بمسيرات وصواريخ إيرانية وتفعيل خطة الطوارئ  استهداف مطار الكويت أسفر عن إصابات وأضرار جسيمة في عدد من مرافقه</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76855" target="_blank">📅 10:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76854">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇧🇭
قوة دفاع البحرين: استهدفنا ب 3 صواريخ وعدد من المسيرات الإيرانية</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76854" target="_blank">📅 10:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izc04tDLRLLfAvoAtrlEDsS51fe3hvAmCIDSBFDQusfiAfk6Yofvnw_C0nZ73IAm2GpGeF_QO81584ERXQOtrHqeGBxVt-F6iGL0DySyUfUw2_qaVLsOJCWM9MDe4G5-CvURY9muWPfaKoTAeetFkmxjQldP223cJnZLD3xt6_cvel5YDOk8tmZnpWlRju7M27xQvjjzw-lflMk-vbTOfBAxJ6RHLNwvf06_1wrJTddyoubYcx7ArXBn4ccdm3WvTQwUR86Sk9EwuugbCyweVevljRcG8Rl9bnnCqhWnqLy_Xzg1vbT1HgcYaQHwgsko5f4pi7uoNnNd-dtNLpvTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السلطات البحرينية تعتقل عدد من الشخصيات الشيعية في البحرين وذلك رداً على الهجوم الإيراني على المصالح الأمريكية على أراضي البحرين.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76853" target="_blank">📅 09:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw3_4JNt4vvZMZxV0vZESztk9MG4Pnp0eM0hAnYCtTl6vQZqcKUBau-QxGyL8OhNefcUwR77jtNXnoo29FInHcWGctHmD_fUpIu2Ezgp8koWhuul-ctHlSXQnOhOeHM7nfMhL-bVpRWeqbtz-pN-2qCqW_YeHoN46J9G9VXLxYs_vhDxpwEqDswnVAa1hVmkMcfV30EJyrRTSpqx8RFuAbg7mqQQaE5V0J5UgbuRjob5SjvcK0HQNsG_boVeVZp6Oci_dtnybqoPExfIH_SAWZiMUztWfbupmUI3rRCEE-9X-qrYXQOPPYEHWJ1cnbdqhXyN1296DoW1o1ox-9I7YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة أقلعت من تل أبيب تطلق نداء الاستغاثة وبدأت بالهبوط متجهةً نحو Belgrade.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76852" target="_blank">📅 09:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇰🇼
🇦🇪
الكويت والإمارات تغلق مجالها الجوي أمام حركة الطيران.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/76851" target="_blank">📅 09:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇰🇼
🇦🇪
الكويت والإمارات تغلق مجالها الجوي أمام حركة الطيران.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76850" target="_blank">📅 08:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5KsrGEb1MIwm8EUCIRVkMW9WPUmWWXoiOnCS09xGXqEv7QNt4gae_ziaXtseSfYboQkrdMgeCus9TsOPyGmF6w5gKpzUu0fNde4JteE6Zg14PW1NmVlvvmrJsM7WpbSJeDWg7Ug2mQUq4DmkU7kOBe4Ja_WIEKwA05LssLBF6dDRjuWx_F_cI_gevJDX--fOSpD1Veot7HLqB3TADvY0W_xvcAU75-184QRt6CstDQorKQEap-kKEHOKpjYOqlWLVC9yqkV9cdA8Dh-aLf1msQVNJHQmVc-skN5Vx1VI891VqyMT7nNjO4sK7UbJTcRftsRRzKple8s4GagbpubHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🏴‍☠️
طائرة التزويد بالوقود الأمريكية أقلعت من تل أبيب وتحلق الآن فوق الخليج الفارسي.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/76849" target="_blank">📅 08:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">إطلاق صفارات الإنذار في البحرين.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76848" target="_blank">📅 08:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">إطلاق صفارات الإنذار في البحرين.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/76847" target="_blank">📅 08:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76846">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b904ffec5.mp4?token=GC0OgVMNT2GKtrUR713tA9CQqIdhC4fp22MOGs2fLk66BNp7rHZpWYrd0bLCbSwa3zvMlGTN55IgZBgh9-skdyuh7Y-c3obVPe364xCV2X2mHZgmDPcNDBpr7EpOVnZ3eUaCNYwx50QOBRtvUTaffnp2FPPOX41aAY0xpRhkZ5R-boicK7dc9yfDBQaAO2-ZIkJuqr5nstYsLey7ucHL4SHCyUjZygauIDp0w6vpCQOhXkdKqlejHlo6MTyTBwkjoYvYrUx0WBgF-W-uznzYyPX1T8ejtssuVyIgdfHuQwAUr2Sn52QReCOoqKG8Iv9uc0y-SkOcnpqxeIcTc7wmOw0CPIKqNtcbmNAaFERUQq0s3sz06zWxoF2ciacseNRZcb6iTWnc2LHSNGq9StCwj_KeRCZNKbE_eTYiytViDRZ_U9lkFZSUA6cgHd721CiuLX1-nPVCdMOSlQuijWzvcC8KMi6dEVyWikncMq-238NZ-ipb7qh1v6NFBYVnuXGDa_4p9-Moi3ghkW8qAMSkNec18mkYkrNO2yeEDkCTBLdahL1Nri1NRhsZg1F9JtAa1RX7qE7NdE0I5XWG14hwgC6iXoMI2bSaQDuY-vf2mKrB-qvp_0cSG_Sdzbm-DNxIgwcphuVjkyBEvZVHDzT2i72ZrPDBmQYoaeJTfxwiGWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b904ffec5.mp4?token=GC0OgVMNT2GKtrUR713tA9CQqIdhC4fp22MOGs2fLk66BNp7rHZpWYrd0bLCbSwa3zvMlGTN55IgZBgh9-skdyuh7Y-c3obVPe364xCV2X2mHZgmDPcNDBpr7EpOVnZ3eUaCNYwx50QOBRtvUTaffnp2FPPOX41aAY0xpRhkZ5R-boicK7dc9yfDBQaAO2-ZIkJuqr5nstYsLey7ucHL4SHCyUjZygauIDp0w6vpCQOhXkdKqlejHlo6MTyTBwkjoYvYrUx0WBgF-W-uznzYyPX1T8ejtssuVyIgdfHuQwAUr2Sn52QReCOoqKG8Iv9uc0y-SkOcnpqxeIcTc7wmOw0CPIKqNtcbmNAaFERUQq0s3sz06zWxoF2ciacseNRZcb6iTWnc2LHSNGq9StCwj_KeRCZNKbE_eTYiytViDRZ_U9lkFZSUA6cgHd721CiuLX1-nPVCdMOSlQuijWzvcC8KMi6dEVyWikncMq-238NZ-ipb7qh1v6NFBYVnuXGDa_4p9-Moi3ghkW8qAMSkNec18mkYkrNO2yeEDkCTBLdahL1Nri1NRhsZg1F9JtAa1RX7qE7NdE0I5XWG14hwgC6iXoMI2bSaQDuY-vf2mKrB-qvp_0cSG_Sdzbm-DNxIgwcphuVjkyBEvZVHDzT2i72ZrPDBmQYoaeJTfxwiGWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
الإنفجار الذي سمع دويه في العاصمة الإيرانية طهران، ناتج عن انفجار "خزان غاز سيارة" بإحدى محطات الوقود ولايوجد هناك حادث أمني.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/76846" target="_blank">📅 07:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd089958f6.mp4?token=j_oRFWilZzM7jr_mwqqW10VaHEunhIGBTY0B7oYgafpEyNkLkUqIuA8HB_L8DkDlw9OrYrPWdAZuDmIO1G2IsMj_2AkIkUvBJikCUJeX3X8d0oXbxYd3qycr4prPB2qJiZLKVYeRpE1jlgRDJhearnQH7qfLbK2ynAlCCTifCltCJMgYWvI3eilkUmGEQP_0e6ZIAhhENMKMaG4k_t6Fma78pfU03Oqhm3MSHS5Nzeib7-KeCpPa5k1IJRJxn8aKdJzJto2zzRM6Sh8edBIh7FaObhSm-zQ6sfqahGi4AhJGc5ZBk_zkT61jW7YYyv2JP9_GDXW7zpdtSV6eOGf6Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd089958f6.mp4?token=j_oRFWilZzM7jr_mwqqW10VaHEunhIGBTY0B7oYgafpEyNkLkUqIuA8HB_L8DkDlw9OrYrPWdAZuDmIO1G2IsMj_2AkIkUvBJikCUJeX3X8d0oXbxYd3qycr4prPB2qJiZLKVYeRpE1jlgRDJhearnQH7qfLbK2ynAlCCTifCltCJMgYWvI3eilkUmGEQP_0e6ZIAhhENMKMaG4k_t6Fma78pfU03Oqhm3MSHS5Nzeib7-KeCpPa5k1IJRJxn8aKdJzJto2zzRM6Sh8edBIh7FaObhSm-zQ6sfqahGi4AhJGc5ZBk_zkT61jW7YYyv2JP9_GDXW7zpdtSV6eOGf6Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
هجوم أوكراني على مصافي النفط في مدينة سانت بطرسبرغ الروسية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/76845" target="_blank">📅 07:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76844">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇯🇵
‏
اليابان
: ميزانية إضافية بقيمة 19 مليار دولار لمواجهة تداعيات حرب إيران.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76844" target="_blank">📅 06:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf856cab38.mp4?token=ulXfkZZpwLJBYtlNq5sb6yT6NMGCmePmXUJs0AKDxePtIQS9w47unhWZjJOYyK7Qbyr1yBc1ghxIoQP2jKbH00XbULeYbUqDB21wfaEmwr9uyPhul37AEVic6zHn9KILpPmr6bhwWKVNxds6kkmzhq7EZgRPtnWbf7yQDuEBPzowxweuQO03outzTrKVmavVeX9LGZDYGC7CN09xQ-qFukZnYi8Gsnd8O09-zsBwM4EgG5H0Ud8qUMWxfuShcO67P6yoAW-VPVlERZACT4vSpaoGCXEEi6XziYEIFtUbzP6aLnoki0Png16e0_FIPO2AIqSkgtlFg__Oxen7INxpJL5uB2UlKd_Hx4YSuLIYV9g64AAcuF1CkVEVkqJxGrwsgpZFaovFOFp9YfaMX2MzBmaoUz3ICeh6lSGbfbhFydCR7YjX5lCXfaeb0JDmHBy-5wL563-a7G7owSG91cK8wiE89hROnaKHJnaYFJFGcu-L9qxYiP7l3BoZc5d9fh7cz9KZkTUeAGAhne_Y_Iozfn-erqKi4t6V3QIaDG6nw8zyX4vb9-cccfsohtjdPKK5lksLLrPK-UBJBm3HmBP45P7zgzyqdceu_NRTXUl_K93LjLKPiopfGdfak2BXPlwmGrBCypNshppwnhzHuETA7ZjSgjqqRD6P_iCOX0PdlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf856cab38.mp4?token=ulXfkZZpwLJBYtlNq5sb6yT6NMGCmePmXUJs0AKDxePtIQS9w47unhWZjJOYyK7Qbyr1yBc1ghxIoQP2jKbH00XbULeYbUqDB21wfaEmwr9uyPhul37AEVic6zHn9KILpPmr6bhwWKVNxds6kkmzhq7EZgRPtnWbf7yQDuEBPzowxweuQO03outzTrKVmavVeX9LGZDYGC7CN09xQ-qFukZnYi8Gsnd8O09-zsBwM4EgG5H0Ud8qUMWxfuShcO67P6yoAW-VPVlERZACT4vSpaoGCXEEi6XziYEIFtUbzP6aLnoki0Png16e0_FIPO2AIqSkgtlFg__Oxen7INxpJL5uB2UlKd_Hx4YSuLIYV9g64AAcuF1CkVEVkqJxGrwsgpZFaovFOFp9YfaMX2MzBmaoUz3ICeh6lSGbfbhFydCR7YjX5lCXfaeb0JDmHBy-5wL563-a7G7owSG91cK8wiE89hROnaKHJnaYFJFGcu-L9qxYiP7l3BoZc5d9fh7cz9KZkTUeAGAhne_Y_Iozfn-erqKi4t6V3QIaDG6nw8zyX4vb9-cccfsohtjdPKK5lksLLrPK-UBJBm3HmBP45P7zgzyqdceu_NRTXUl_K93LjLKPiopfGdfak2BXPlwmGrBCypNshppwnhzHuETA7ZjSgjqqRD6P_iCOX0PdlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد توثق لحظة إطلاق الصواريخ من قبل الجمهورية الإسلامية الإيرانية باتجاه القواعد الأميركية في دويلات الخليج الفارسي.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/76843" target="_blank">📅 05:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76842">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية تزعم:
فشل محاولة ثانية من المسيرات الإيرانية في مهاجمة قواتنا في الكويت.
الدفاعات الجوية التابعة لنا نجحت في إسقاط عدة مسيرات إيرانية ولم نتعرض لأي ضرر.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/76842" target="_blank">📅 05:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76841">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66acdfd3d4.mp4?token=k-EGt4sgPrt9Bydl6kIAa1g6PJ34TlUt3rHyTWcWa6WkXh0gTqdr0QNzo5fZfv1uOGgd-sfZmsfQgXMvMAonPiDQD_TcKKl9Gwt06xOBIVJWeA3cq4ZJFE5pezhVBbUui2RG9le3OTEd1bRkOkIS7Kwo25lVm4ffTAjC0hnqPCEVZYc-6epem4D3fjCs5G_ZRhdg5ui03EAyH5XLr2CpSeDsAQnqiQb29t0CcwlZZx9bpnNIMJZlgJa3HzX2fO5yi2SyKAPsCMiBNl31T-ChgZoSBZ61u6mDylFcTOE9nF5VD7pDY-rEk4QLIAPnaQQ-NroNk2MXSPjZnH7CbsC5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66acdfd3d4.mp4?token=k-EGt4sgPrt9Bydl6kIAa1g6PJ34TlUt3rHyTWcWa6WkXh0gTqdr0QNzo5fZfv1uOGgd-sfZmsfQgXMvMAonPiDQD_TcKKl9Gwt06xOBIVJWeA3cq4ZJFE5pezhVBbUui2RG9le3OTEd1bRkOkIS7Kwo25lVm4ffTAjC0hnqPCEVZYc-6epem4D3fjCs5G_ZRhdg5ui03EAyH5XLr2CpSeDsAQnqiQb29t0CcwlZZx9bpnNIMJZlgJa3HzX2fO5yi2SyKAPsCMiBNl31T-ChgZoSBZ61u6mDylFcTOE9nF5VD7pDY-rEk4QLIAPnaQQ-NroNk2MXSPjZnH7CbsC5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای انتحاری در حال حرکت به سمت کویت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/76841" target="_blank">📅 04:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76840">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241cbfcc80.mp4?token=iVxYIzhV6Clhq7ky9N9ic7fPcGTqmpvJFLq8nENvQTfrMy4AwrXU1TGK1kLgohj4mxZ-PuHs8_J3B_WJpukRkaoU-OWC-IJOg4YpokyrwRVxoarMMq0eR-8-4Ro33QNyiN5FtHIuRQINopWPIFkgs8q0gNViLvdHaQT2nYg4nYk14Wu_MGhkWMeBko1az_SH5CmXQ6rM3o9f7aHeMQVC9dq9TwLT7Lep-CO_lBHWC3Xuu7OORBs6Kd-Ii-DZ5ybW6Dkz2YFiHHzIbSTxIuOAAyqmavdXk6vdmd5FpO4x_0oZPPi1zDPXYewiHOT8MpttuQ5ZQ9tb0yvqHYQlSdzOiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241cbfcc80.mp4?token=iVxYIzhV6Clhq7ky9N9ic7fPcGTqmpvJFLq8nENvQTfrMy4AwrXU1TGK1kLgohj4mxZ-PuHs8_J3B_WJpukRkaoU-OWC-IJOg4YpokyrwRVxoarMMq0eR-8-4Ro33QNyiN5FtHIuRQINopWPIFkgs8q0gNViLvdHaQT2nYg4nYk14Wu_MGhkWMeBko1az_SH5CmXQ6rM3o9f7aHeMQVC9dq9TwLT7Lep-CO_lBHWC3Xuu7OORBs6Kd-Ii-DZ5ybW6Dkz2YFiHHzIbSTxIuOAAyqmavdXk6vdmd5FpO4x_0oZPPi1zDPXYewiHOT8MpttuQ5ZQ9tb0yvqHYQlSdzOiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏انفجارات تهزّ مقر الأسطول الخامس الأميركي في البحرين، عقب إطلاق رشقات صاروخية إيرانية باتجاهه.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/76840" target="_blank">📅 04:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76839">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82785218ec.mp4?token=Jqgvu4WBfW3Jdj_WuRFmVY7I4EOgRJGX6prlhozDN_bNDyiqkZmJmrQzGEkUKRtIJ8GuLeErlBj7J7FVpo1rFEfpr_p-KC9XlJamYhbYfvK74tC7hw0nWixTcCVZvqRBpocokfdvVuGUe1ysphRrGWtoTDmx8kDE5bdmUkIm16POD3fliiybDgOSnBWJWl7zLZ0NaCjS5E5RjASGg_wwev7r4epkm-Ge-cBqFaJPILFAk0q5aCK-4cYRmHYQqvVaNp1OeJ3RUl9J_A7gS57c_U-wgQQAYeOoxfQMhqoHKCA_pNhSGvOuB_XOQA5PTPk1BbkOO18qkOJ-CqbSBTrpig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82785218ec.mp4?token=Jqgvu4WBfW3Jdj_WuRFmVY7I4EOgRJGX6prlhozDN_bNDyiqkZmJmrQzGEkUKRtIJ8GuLeErlBj7J7FVpo1rFEfpr_p-KC9XlJamYhbYfvK74tC7hw0nWixTcCVZvqRBpocokfdvVuGUe1ysphRrGWtoTDmx8kDE5bdmUkIm16POD3fliiybDgOSnBWJWl7zLZ0NaCjS5E5RjASGg_wwev7r4epkm-Ge-cBqFaJPILFAk0q5aCK-4cYRmHYQqvVaNp1OeJ3RUl9J_A7gS57c_U-wgQQAYeOoxfQMhqoHKCA_pNhSGvOuB_XOQA5PTPk1BbkOO18qkOJ-CqbSBTrpig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای انتحاری در حال حرکت به سمت کویت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/76839" target="_blank">📅 04:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76838">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyOBVCV4r3XleeVeKe9rh68HcFIgseN4i8V5SfjUSYmygTBzZzGIrM_3M2yNSq6sX5FvxyNpRxvGJTbvza4KJsf8Sna6PDce9ovNwr2SPoH8gsEXD5fE-OPbyl9HMg85uCf7O9ZvCU_weIFzNBoNF51rQUrVBFmTuFsU_zzWw_1_vG0Ic8yaOLgd28sZqRoYo7xl7qf4mz_GgKSfyqBLnbj8h9nxJ-QGg4Pg3flQHNVaV3Zv7FsPpFyKoGYyY7L5ZkHANZ-JDKIuIhKy3G7q8_tj034QvlI5Qu-TU47reNBqJ5i0pliTuY4iENlgwZi1w4CkvzxSV92-NwR8uN0c2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط العالمي تتجاوز 97 دولار للبرميل الواحد بعد الهجمات الإيرانية على قواعد الأمريكان في دويلات الخليج الفارسي.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/76838" target="_blank">📅 03:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76837">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">من الطيران الحربي الذي يجوب سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/76837" target="_blank">📅 03:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76836">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8563b797f.mp4?token=UG86OfDRlhI0r1F8UTtmiZfodsJUKGZsJqD7baMAR35VvErBVu9exXQtw0RVOIV7U5Xotc82c6MdIjNebdmt-ifzPokz7NgECEELHe4PzvNqvdX0JJMRzvEXhJopmKsPGHd-oIMQBqA5YHymNNqcqx-zX-BN-RupnPHqzjG-buIUcj68k_PDGW5plkrEMsCByZieEnPielxK3yao3brVKBffj0-J3hOaj4_m3z7qzD8Xkwu0l1_7guXD3Ao_WQ14lM3RmV6tL5Rr3TfmH0W1yD34f6R9aAyG4Hz_u8VhNKeh-4NCxztks29gLnQBYF047uCbqapuZL5PYp6lOgPT0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8563b797f.mp4?token=UG86OfDRlhI0r1F8UTtmiZfodsJUKGZsJqD7baMAR35VvErBVu9exXQtw0RVOIV7U5Xotc82c6MdIjNebdmt-ifzPokz7NgECEELHe4PzvNqvdX0JJMRzvEXhJopmKsPGHd-oIMQBqA5YHymNNqcqx-zX-BN-RupnPHqzjG-buIUcj68k_PDGW5plkrEMsCByZieEnPielxK3yao3brVKBffj0-J3hOaj4_m3z7qzD8Xkwu0l1_7guXD3Ao_WQ14lM3RmV6tL5Rr3TfmH0W1yD34f6R9aAyG4Hz_u8VhNKeh-4NCxztks29gLnQBYF047uCbqapuZL5PYp6lOgPT0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي في سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/76836" target="_blank">📅 03:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76835">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/192564c0d1.mp4?token=CpC5BNgagnwpInP1PL77Y2wjMpKBIjB8alg1-FF8kR9vnTCwz2Qzx16sRUspObXo4Ibt_2LgAoR9pkeAhsOmu_lT22vxSUFmhPudtBnuPe4t_9gUiCrMsTf7faGzo3BkC5hc9MS-liYqFKPNADpOfi8CSV4hQ0UK_bPR6DNbXLcLqmBrtSZGavs7ug8XS-A90CH3VN4ka8A-vafVoG3bESXTWwDqN_p-aRR-TdTGFRkIk3lEqVW4vM-xP_aKiTxsl90plZvecakZypVQyPnW6fa2scid0YemVXWouedl04y8aD-lFOq8EO9NdKwwAl2g-MpxTKJ-3Z1Jejq2x2IKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/192564c0d1.mp4?token=CpC5BNgagnwpInP1PL77Y2wjMpKBIjB8alg1-FF8kR9vnTCwz2Qzx16sRUspObXo4Ibt_2LgAoR9pkeAhsOmu_lT22vxSUFmhPudtBnuPe4t_9gUiCrMsTf7faGzo3BkC5hc9MS-liYqFKPNADpOfi8CSV4hQ0UK_bPR6DNbXLcLqmBrtSZGavs7ug8XS-A90CH3VN4ka8A-vafVoG3bESXTWwDqN_p-aRR-TdTGFRkIk3lEqVW4vM-xP_aKiTxsl90plZvecakZypVQyPnW6fa2scid0YemVXWouedl04y8aD-lFOq8EO9NdKwwAl2g-MpxTKJ-3Z1Jejq2x2IKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ باتريوت أمريكي يفشل في اعتراض الصواريخ الإيرانية ويعود ليستهدف دويلة الكويت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76835" target="_blank">📅 03:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ecc2e200.mp4?token=jhEnPV8lNAaxX0XUCxY6oZNFLhHrHotnaciVMvB00S-Ste_GQ8VCKGYvdIzGg-Ty9G9WWA28hvRfQ0JlWUjmJGuxEyKNuNIVi-WzCSpFdaFuKGhTmGu0mg-dHt8IyVGk2EJXMWi5hjQpVcaofQZxUZ-dmQr-DMQf7d8DEZUlP7BG3YhW6D4iRshy8o_edVBjgNhPWEtt-RpWIxQs5oQyD5I-IRGiOYH0jw0LqTr7Zue8iozTJCW6hfBM6JwKJS5r-rJ08Xo1l4ehaLKRMruemVfBYNOVvtNgtgMWBIj0bPxTV1PJQi4y6FreZIhazqV9GSVJVBYbmEa8Hv8o15DRYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ecc2e200.mp4?token=jhEnPV8lNAaxX0XUCxY6oZNFLhHrHotnaciVMvB00S-Ste_GQ8VCKGYvdIzGg-Ty9G9WWA28hvRfQ0JlWUjmJGuxEyKNuNIVi-WzCSpFdaFuKGhTmGu0mg-dHt8IyVGk2EJXMWi5hjQpVcaofQZxUZ-dmQr-DMQf7d8DEZUlP7BG3YhW6D4iRshy8o_edVBjgNhPWEtt-RpWIxQs5oQyD5I-IRGiOYH0jw0LqTr7Zue8iozTJCW6hfBM6JwKJS5r-rJ08Xo1l4ehaLKRMruemVfBYNOVvtNgtgMWBIj0bPxTV1PJQi4y6FreZIhazqV9GSVJVBYbmEa8Hv8o15DRYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من الهجوم الذي طال دويلة الكويت</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/76833" target="_blank">📅 03:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سماع دوي انفجار قوي في مدينة قامشلي السورية.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/76832" target="_blank">📅 03:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76831">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">طيران حربي في سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/76831" target="_blank">📅 03:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">يبدو ان قطر والسعودية قد تعهدت لايران بعدم استخدام أراضيها بالهجمات على الجمهورية وهذا ما يفسر عدم استهدافهم بالجولة الأخيرة ..</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/76830" target="_blank">📅 03:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25fedd33a5.mp4?token=HxRV0uujCuiCp8vo07NV3GXWH05G35imel07bPhU-oBxbQkwTKvc3ipIDuzjlbEVfcNVZ6Cmk_70Bggk8Y1C427DhSR3q-ZBWSSyCv77By8_9WRimnTy-eL57T2G33VysAY5LdqUI3oJdneiWflC-ZIYKIe4fmW7xsAYTqmx5LMb_nL3H3K_aOj5tT2cJfxOQc59dxyan68zhg5jPZGaSax3KVb_kbsxvnkjpeiNstnBIKCboWcssmm0YlElgamGLY7F89x1Y0tRzqQcatvtiV5qKHibC-hpl_kU_inkT0VhizE54LhQGh5-A2CZeC5bwsvSlDPMA6SMqV1m2bwgmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25fedd33a5.mp4?token=HxRV0uujCuiCp8vo07NV3GXWH05G35imel07bPhU-oBxbQkwTKvc3ipIDuzjlbEVfcNVZ6Cmk_70Bggk8Y1C427DhSR3q-ZBWSSyCv77By8_9WRimnTy-eL57T2G33VysAY5LdqUI3oJdneiWflC-ZIYKIe4fmW7xsAYTqmx5LMb_nL3H3K_aOj5tT2cJfxOQc59dxyan68zhg5jPZGaSax3KVb_kbsxvnkjpeiNstnBIKCboWcssmm0YlElgamGLY7F89x1Y0tRzqQcatvtiV5qKHibC-hpl_kU_inkT0VhizE54LhQGh5-A2CZeC5bwsvSlDPMA6SMqV1m2bwgmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق لإطلاق الصواريخ من إيران نحو دويلات الخليج الفارسي</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/76829" target="_blank">📅 03:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXe0GpaqIvj92DkR9yBIZZJ0c0A2tYaBzkRG6VGgBdEOdLhDuDjrCeIuKXAsgx0vFWCD6EUmU6pji2MnJZjmNR1jkWIXVr4j4SJKCxaYBqgtRz2ZkYz8EHM9ldPww6BK9PcFENcuwSEvWd3crwg4yRf3pw-Ats3RoUHKiGCcbL6RIn5BMOLNe6sh8XnM7dtLfeSp-qSytMVlsupgHOyPgDEMQMh6S6ZKBvnZ7sdJkDkRYT0jSQwrKJsdn524XDDM1O6GI9y05BT4FCZnIdnOtd0r89IOANP3Z-7Ao9F3jzgPOHKVbaYKioggDjxlJpD3sglB-G9BZpXWysuoak8vnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها   بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/76828" target="_blank">📅 03:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/540734d971.mp4?token=AHy5JoTDBjKF0H-zUI4PmyRhL27caqeLo2R9e2BlYghj24adtqXF3FPrkVV7JewaXmNPo4j2V-VQZ597gnW46068yF1tmyXvxHsyeRymYySh79H7vNKwI48eD_4_fIHIMlT9MseTuOp0YYMt3YbgE-sfGkKdRAkMtkEkR8b7xXaNeOVkqmk5USPs1UD2IiXc-2N_8uePPd8aRppNdVikm3t0IjC70PO6BXDrHuNEhFDiLxdEScb2lHnjIPLp73bXPCKaTpiYHG0emHtwZL6eAQH764qVF-5kHreQR4srRuE7HH_MWD1fx-CGag2pbOS8abAC213tAP3_JqsGqZ4C9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/540734d971.mp4?token=AHy5JoTDBjKF0H-zUI4PmyRhL27caqeLo2R9e2BlYghj24adtqXF3FPrkVV7JewaXmNPo4j2V-VQZ597gnW46068yF1tmyXvxHsyeRymYySh79H7vNKwI48eD_4_fIHIMlT9MseTuOp0YYMt3YbgE-sfGkKdRAkMtkEkR8b7xXaNeOVkqmk5USPs1UD2IiXc-2N_8uePPd8aRppNdVikm3t0IjC70PO6BXDrHuNEhFDiLxdEScb2lHnjIPLp73bXPCKaTpiYHG0emHtwZL6eAQH764qVF-5kHreQR4srRuE7HH_MWD1fx-CGag2pbOS8abAC213tAP3_JqsGqZ4C9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عجلة في محافظة ميسان جنوبي العراق</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76826" target="_blank">📅 03:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76825">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
🇮🇷
بيان العلاقات العامة للحرس الثوري الإيراني:
بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
في وقت متأخر من الليلة الماضية، استهدف الجيش الأمريكي المعتدي ناقلة نفط إيرانية قرب مضيق هرمز بقذيفة جوية، مما أدى إلى إلحاق أضرار بغرفة المحركات.
ردًا على هذا العدوان وانتهاك لوائح مضيق هرمز، استهدفت صواريخ تابعة للحرس الثوري الإيراني سفينة تابعة للعدو الصهيوني الأمريكي، وهي سفينة "بانايا".
في عدوان متجدد، استهدف العدو الأمريكي برج اتصالات تابعًا للحرس الثوري الإيراني جنوب جزيرة قشم بقذائفه الجوية. وردًا على هذا العدوان، تعرضت قاعدته الجوية ومروحياته المتمركزة في إحدى دول المنطقة، بالإضافة إلى مقر قيادة الأسطول الخامس الأمريكي، لهجوم بصواريخ وطائرات مسيرة تابعة للقوات الجوية للحرس الثوري الإيراني.
لقد حذرنا سابقًا من أنه في حال وقوع عدوان، سيكون الرد مختلفًا وأشدّ، وقد تصرفنا وفقًا لذلك. كان ينبغي أن تكون هذه الردود درسًا لنا.
نؤكد مجددًا أن زعزعة أمن مضيق هرمز ستُكلّف الجيش الأمريكي المعتدي ثمنًا باهظًا.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76825" target="_blank">📅 03:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7f9af40f.mp4?token=cNFNTR75yJfd0TkW6VhyV4NtVwKoLTuWxcJb07YxHNC7yKCQ7Lu0EzG7RKGbHbp-vCpDnt2iSTJgUHKKxSAv1JOjgzQAnIetkJbB3_4ZOdKx5joRpChoV9EhNn1WbqqynyVz5bwJeJ2oIYn3dEWTS-0tElt00GHplDeIk76R2cQc6OxUehGxJ4ayiwWFYfpR7NmU04dopijk6-UP2Iu0I46EeSjpyj7H0zF1O8lJ8PNseOC_dpUAd9621_Hm9V2ILnQBGj6qgy2IEDzgxSHnJ7Mxbj6UEMpk3ilAug8vrxbOppHeFwOxk4V9IAp-4BsM5IDuALYPFEEoaaX9nTNBpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7f9af40f.mp4?token=cNFNTR75yJfd0TkW6VhyV4NtVwKoLTuWxcJb07YxHNC7yKCQ7Lu0EzG7RKGbHbp-vCpDnt2iSTJgUHKKxSAv1JOjgzQAnIetkJbB3_4ZOdKx5joRpChoV9EhNn1WbqqynyVz5bwJeJ2oIYn3dEWTS-0tElt00GHplDeIk76R2cQc6OxUehGxJ4ayiwWFYfpR7NmU04dopijk6-UP2Iu0I46EeSjpyj7H0zF1O8lJ8PNseOC_dpUAd9621_Hm9V2ILnQBGj6qgy2IEDzgxSHnJ7Mxbj6UEMpk3ilAug8vrxbOppHeFwOxk4V9IAp-4BsM5IDuALYPFEEoaaX9nTNBpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من الهجوم الذي طال دويلة الكويت</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76824" target="_blank">📅 03:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🌟
‏انفجارات تهزّ مقر الأسطول الخامس الأميركي في البحرين، عقب إطلاق رشقات صاروخية إيرانية باتجاهه.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76823" target="_blank">📅 03:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76822">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">القيادة المركزية الامريكية:
نجحت القوات الأمريكية في إسقاط عدة صواريخ باليستية وطائرات مسيرة إيرانية، ونفذت ضربات دفاعية على جزيرة قشم ردًا على محاولات إيران شن هجمات في أنحاء الشرق الأوسط.
أطلقت إيران عدة صواريخ باليستية باتجاه دول مجاورة، إلا أنها لم تصب أهدافها. وسقط صاروخان إيرانيان أُطلقا على الكويت قبل وصولهما إلى وجهتهما أو تحطما أثناء تحليقهما، بينما اعترضت قوات الدفاع الجوي الأمريكية والبحرينية على الفور ثلاثة صواريخ أُطلقت على البحرين.
وقبل ذلك بلحظات، أسقطت قوات القيادة المركزية الأمريكية (سنتكوم) ثلاث طائرات مسيرة هجومية أحادية الاتجاه أطلقتها إيران باتجاه بحارة مدنيين كانوا يعبرون المياه الإقليمية بشكل قانوني. كما نفذت القوات الأمريكية ضربات دفاعية على محطة تحكم أرضية عسكرية إيرانية في جزيرة قشم.
ولم يُصب أي من أفراد القوات الأمريكية بأذى. وتبقى قوات سنتكوم متأهبة وجاهزة للدفاع ضد أي عدوان إيراني غير مبرر خلال فترة وقف إطلاق النار الحالية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/76822" target="_blank">📅 03:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76821">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4ap6kmODTLCYolfMXZReEjKlJtuKl_2qPpPBjKoHnZYSYNGpwpv0cDOsLLaXeZANn8MEDkCrjAZJ4cZNsMhU38fMwtb9ZdjKNP9dsbSS86_rcBN3mHNVTtxDpNGx6t3V8dpZkBlLp14B1drC3510siX9-6sffAITZxeQ7UsSyRg8g1se54Ou-5Y3GLQIlRbSUSOSOF3c5_ERm1dgWMmB1TexlaEtfdqcUqacXlU3_ozzBrVQjVYoFMkSyTACtkaqnVN5r_8DmtzMziTdM8PCX17jYdPBTALFbps1KUqoA9lsPBpq6NiAi6fhXQGXF9mHJwrm6Z7j0BYsBQ_BZ0QVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إغلاق المجال الجوي كليا في الكويت</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/76821" target="_blank">📅 02:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76820">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/76820" target="_blank">📅 02:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76819">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/76819" target="_blank">📅 02:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76818">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">توقف صافرات الإنذار في البحرين
رفع التحذير من هجوم صاروخي</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/76818" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76817">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة قشم الايرانية</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/76817" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76816">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd6NSPq8v8Bp9gVKgOOi5FcCldhzhtfWmbPWqaVYuMqGQAGTgXhj1_xW-HuCg0wFsIB7nDGIG_HJnwfSJURKiFP7lXeyNgabiv8jLdwR-60hrvD023cPrnkz55n89tCKYJPfkCgV2gqAnwAjOnxaTOFkLeLoC-9SRgmMH2OxCvsegXupimL-seg1jINZmari15D9bs6ZjXdGaNpLxOfLmzwlUjhHWLAPWsF2e4eC2Jd7K8AP-27uLzSkD490eznQdzYOw70o_5_WupQSIOh2MmqQ07fU57C5FKjf_K7xibED3pg1viptOXfa3osXvs0CVwo0rwvaQLPwSPHAaiHkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تم إغلاق المجال الجوي للبحرين بالكامل أمام جميع حركة الطيران من الساعة 03:30 بالتوقيت العالمي المنسق حتى الساعة 16:00 بالتوقيت العالمي المنسق، مع السماح فقط بمغادرات محدودة معتمدة مسبقًا.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/76816" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76815">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/76815" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76814">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osyb60m6VqS3jibRbCDsMiQ9zIMwF21M6dP9CkYTOJ7RNsnJhzzU3iDOvre34W1HvJLOrqbkhyq6_TgeXWuHLZ7aI5HzabDSrO49_nYQPXIfu4s-gyfjFaN2IUtWEJXrwsZmBlwX-tfsYAkjJ918FGiBo19X3iuw59_MzP9u3XILa7Hfiyps9CECij36cOs0XL3FgkUdYOzslVuctt45FyKo086qaKhvjtSEpsq48RTbd9-RSD4t7nJPc7LNIO6IT6N-ymj1k1QntCzqCOIVUKFeLbG2wA0aBRNdsUER9dL8EpBiBhBcYzyfMGJGFx0EhhZz29JW8bv4XL4RJGYPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصف نحو مطار دبي</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/76814" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قصف نحو مطار دبي</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/76813" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/76812" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الإعلام الأمريكي : أفادت التقارير أن رجلاً يدّعي حمله قنبلة مربوطة بصدره قد احتجز رهينة واحدة على الأقل داخل فرع بنك تشيس في بيكرسفيلد، كاليفورنيا .</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76811" target="_blank">📅 02:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APs7MZFWNMQyroIKJwDUT5PCX5rdJquq4fYvRw0LMr9Ei3qA4eDVcToJ2jCcPJTIbNoAoVmCNC7PvmkTDuOj6awrsnBJ6vNgOvA8_nDiBTtManLUHzInjIHRxjsv-kCF2FP6J_SDu2hjpfJyefJk7ZAkgZGAiDJGYmv_h5wluIwvEUvusX5BDlms5kAOpsFc0Rt77ayiJot0azedZgcZhEtiWYNhvAoEGvhWABFXqR_sKaHqmV8nbMUUyZlW5pr2jKLDBMhfupjfm-ei9wxE8F_GFElZJ2FDwukrCEouYXC6XH0BPdXFa6_zGIqsmRdX4hJqe7GDTnLaIsRvmXRS2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف حركة الطيران في سماء البحرين</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/76810" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defe9d3c1f.mp4?token=neQTruuOub1bXBoA5m5XQolpspICgBQI9szqNEQS_QISlwQjL0HPFDGh_3hRsPdDLFjb8h83T45gxVLcwWo60YEoOmEujF85VLCwh9I3z8avral-6O1vQ_F4aIThLIQantYgaxaKhyOhzXERkJnHQj9nEbE_zbW03cwGJ3JPyCHplWgTDBPfYTcGBfFyFqX3eTQzxUMt2h3itPPRaiFVW3fBc-2GFtEmALk-V84OGy4x-L-db52DWqMWmhWEi895aEqHRQfO-MeYURCGe26ObHkpX0_6Qu2e6JY3j0YrGM5XiDfdCPSAW4xjmclmHjmHEK4t9DbErYZJLJIES4jtDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defe9d3c1f.mp4?token=neQTruuOub1bXBoA5m5XQolpspICgBQI9szqNEQS_QISlwQjL0HPFDGh_3hRsPdDLFjb8h83T45gxVLcwWo60YEoOmEujF85VLCwh9I3z8avral-6O1vQ_F4aIThLIQantYgaxaKhyOhzXERkJnHQj9nEbE_zbW03cwGJ3JPyCHplWgTDBPfYTcGBfFyFqX3eTQzxUMt2h3itPPRaiFVW3fBc-2GFtEmALk-V84OGy4x-L-db52DWqMWmhWEi895aEqHRQfO-MeYURCGe26ObHkpX0_6Qu2e6JY3j0YrGM5XiDfdCPSAW4xjmclmHjmHEK4t9DbErYZJLJIES4jtDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق صواريخ جديدة من إيران نحو دويلات الخليج الفارسي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76809" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4d84fc6b.mp4?token=RwHbFaqiRDUTMdNsErvI6WQqZhVeI3sA-voYeZ3LJtgi5-gmTj6DQvVTzy3Ozytyo0lZDkQ_O377_2kMnWwLgNcT7656XJtmXi2JnxspQIsbYFdgmqR3IixOEpPaxB3UPhRIPPBJ86FplcJW4nNkyzobf3wLfi3mkq_myIYbYYqz2xEDTsjQUymwKKH7hFyO-RO96HbUn1RsNAo3_-xaomRsYQZ7PTdvS9odnqRoYROFgoGk4FInVSK37a0sBqhH012ITlQwuuzCrJK3CwrXOZUQQQFLc1e9whoS1RZNHANyoN4BlzTitIcow6wKLjruKSUNqsgSxqIwxnaPvg4XPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4d84fc6b.mp4?token=RwHbFaqiRDUTMdNsErvI6WQqZhVeI3sA-voYeZ3LJtgi5-gmTj6DQvVTzy3Ozytyo0lZDkQ_O377_2kMnWwLgNcT7656XJtmXi2JnxspQIsbYFdgmqR3IixOEpPaxB3UPhRIPPBJ86FplcJW4nNkyzobf3wLfi3mkq_myIYbYYqz2xEDTsjQUymwKKH7hFyO-RO96HbUn1RsNAo3_-xaomRsYQZ7PTdvS9odnqRoYROFgoGk4FInVSK37a0sBqhH012ITlQwuuzCrJK3CwrXOZUQQQFLc1e9whoS1RZNHANyoN4BlzTitIcow6wKLjruKSUNqsgSxqIwxnaPvg4XPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القواعد الامريكية في الكويت تدك بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/76808" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">استهداف سفن عسكرية قبالة سواحل الإمارات</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76807" target="_blank">📅 02:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5327aa8b74.mp4?token=hCTdYxEdXZrOuDO0c4oTgnlz0fVo5mSuNKmAnbtntG9fsF5OHCYTiKU-mDCj4UBj-s2d39XmpXrAK-7ZvT8y0SpNXOpyhnTV2NwpaDYvdeP2AqiT8PGj8GOuHgOVB2pB_xfjqTqyNLsQ7fYW8HOYGdTBG4Z_IMX9p8D1n1Mqoklw3YPLKLnV692Yah8g2Kt_MEDAVCvknlFRvrO0oA3OzlT092TXujukrXdHfVxsRQN-So7XJx9Ly2qHBQHImEVXKDswfea7FWcOnB7xKyFKGc6FMCZq9EQP_3k34iAsVs5wugNjN_dTC5o2Lpcs_AJID6rr1xOopFnfE_Yx5uXTlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5327aa8b74.mp4?token=hCTdYxEdXZrOuDO0c4oTgnlz0fVo5mSuNKmAnbtntG9fsF5OHCYTiKU-mDCj4UBj-s2d39XmpXrAK-7ZvT8y0SpNXOpyhnTV2NwpaDYvdeP2AqiT8PGj8GOuHgOVB2pB_xfjqTqyNLsQ7fYW8HOYGdTBG4Z_IMX9p8D1n1Mqoklw3YPLKLnV692Yah8g2Kt_MEDAVCvknlFRvrO0oA3OzlT092TXujukrXdHfVxsRQN-So7XJx9Ly2qHBQHImEVXKDswfea7FWcOnB7xKyFKGc6FMCZq9EQP_3k34iAsVs5wugNjN_dTC5o2Lpcs_AJID6rr1xOopFnfE_Yx5uXTlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف قاعدة الجفري الأمريكية ومقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/76806" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات تهز أربيل شمال العراق الان مجددا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76805" target="_blank">📅 02:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74abf9487.mp4?token=TvjORGow1udcXsGYVX8c0TRgfc62gMna82y508IN_Dv7689ValgWWMBW9Al7UWUQ1Bc-XA-DJVGmpZOgqlFerEu1XmVrL9TqiaSY69_uMFjNh-PkF6et32p1jugpvDyNyZXrfcN91Mfz0NOTZh3GN7lv1lw5nFx164TK1XcqGBmKzNIK1QAMhjMAEtma4x0nFzB1Awqb69zNOYwGFZiHU-ksTm3ipd-pPpO5g72EFcKxHV7ymb9cF0rPkbsMvttS7khZwt-wFyLQQyXpItQj5vDUbwgLlO_Fdqmzl9-qBR3PQFLk4iw5md-YIfZzsB0VYNgz0mB0koZtpszt0CPVGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74abf9487.mp4?token=TvjORGow1udcXsGYVX8c0TRgfc62gMna82y508IN_Dv7689ValgWWMBW9Al7UWUQ1Bc-XA-DJVGmpZOgqlFerEu1XmVrL9TqiaSY69_uMFjNh-PkF6et32p1jugpvDyNyZXrfcN91Mfz0NOTZh3GN7lv1lw5nFx164TK1XcqGBmKzNIK1QAMhjMAEtma4x0nFzB1Awqb69zNOYwGFZiHU-ksTm3ipd-pPpO5g72EFcKxHV7ymb9cF0rPkbsMvttS7khZwt-wFyLQQyXpItQj5vDUbwgLlO_Fdqmzl9-qBR3PQFLk4iw5md-YIfZzsB0VYNgz0mB0koZtpszt0CPVGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي على الكويت الان مجددا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/76804" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cefcea39.mp4?token=Gq3ZwxtELhROqQ1iKsFS8NHaEU57bDyIFgP68ix9VhwDQf3rKa5F4YKnBUQqNAPeLiOLmj6Sf6jXhNfB1CO_-AaWOwQwO77x2Ph5cbk19QV1EgFOQkMOcJNISY8LPP8UVxEpoV3_rv4dCuLKWUPQeVkbaTHhkn38kQeJuwoCtVCC6-iIws6WzYyTQk8d_oSufBQxwcdZqmIF4EZMyAAIq1O-UZLczcsqxITJtS-VUyp56Ty8BNLkumobBswP8OjhrAWEv8BazG6npy1moRLRDdDzoZQ8bgdWhmQ1nHiNcSwqPx3uIaePrdU6kJS9bJrpbeSxsIAkzaqU1v3ze1IMPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cefcea39.mp4?token=Gq3ZwxtELhROqQ1iKsFS8NHaEU57bDyIFgP68ix9VhwDQf3rKa5F4YKnBUQqNAPeLiOLmj6Sf6jXhNfB1CO_-AaWOwQwO77x2Ph5cbk19QV1EgFOQkMOcJNISY8LPP8UVxEpoV3_rv4dCuLKWUPQeVkbaTHhkn38kQeJuwoCtVCC6-iIws6WzYyTQk8d_oSufBQxwcdZqmIF4EZMyAAIq1O-UZLczcsqxITJtS-VUyp56Ty8BNLkumobBswP8OjhrAWEv8BazG6npy1moRLRDdDzoZQ8bgdWhmQ1nHiNcSwqPx3uIaePrdU6kJS9bJrpbeSxsIAkzaqU1v3ze1IMPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي على الكويت الان مجددا</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76803" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هجوم صاروخي على الكويت الان مجددا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76802" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76801" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تجدد دوي صافرات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76800" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صافرات الانذار تدوي مجددا في البحرين</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76799" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c006192776.mp4?token=aGXitVGlzWpDUwZN3lRjT0fTazyTTGy4KqDVgSdiUHX-ZNI0KQKgSROTPXRCzfu9vXA-xDdWXH_3YXCjtHXRSRgB7qFe0t3fTcdATfxUIaUp5qBMi6aHfSTn_-gvvcL6PlewNnhZDMR-DMJaIX3KAimYOCtdFEswwTsZevH__p137di6AWNmvMQW8LMoOyyIS9yHmXhBhiqQB_I2EgSjznHntHSsHmjV8rVoIihXmnc3CxcASDhijsTg1_qEBs-s-Ztu-yL1JUL9gVmtZTfnIu1WgiH2_qVJKNoLRpF3vw3z5H5haD4Kw2_dD4tnjXdyVxBcv-diMBmqkyMqt-POrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c006192776.mp4?token=aGXitVGlzWpDUwZN3lRjT0fTazyTTGy4KqDVgSdiUHX-ZNI0KQKgSROTPXRCzfu9vXA-xDdWXH_3YXCjtHXRSRgB7qFe0t3fTcdATfxUIaUp5qBMi6aHfSTn_-gvvcL6PlewNnhZDMR-DMJaIX3KAimYOCtdFEswwTsZevH__p137di6AWNmvMQW8LMoOyyIS9yHmXhBhiqQB_I2EgSjznHntHSsHmjV8rVoIihXmnc3CxcASDhijsTg1_qEBs-s-Ztu-yL1JUL9gVmtZTfnIu1WgiH2_qVJKNoLRpF3vw3z5H5haD4Kw2_dD4tnjXdyVxBcv-diMBmqkyMqt-POrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجدد دوي صافرات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/76798" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTgNBw4V9Nzp-ufvcnxePJZHNyVYUKPo89e-6R4feongZktONhH75cDH13nQnbcneRBg_yJkaqO7hRQwR_yPAn4v1f1Mu4GNrKLmdKuX5ylwkIPF4X2A_h6INuEcXbqITBgGg9T2CICtYz4xqZUhwYTEPbIi2-wzahVSXHZ62d2jDXsS688yTLhFd_jP34TPkQjNMKbJhPIclkppx97ei1YqJr-f9wycDO_6qGmWYLHEfjQJFAFz1IR_BoRedSuftWZVckYB5xjrVkb7BX-IGgLyK5XeV0_Zq2MOar7NSxYiv18P3eXrz57FlOk3aav0Pdx328ObcDBw4C39AhaI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76797" target="_blank">📅 02:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95bbb3482d.mp4?token=PTcQBL06NzJk7t_u4yB-8xJ24G7tnYLP5e-Otj39e_jKz9mj_W0n0G0h7lerxk5tLAxinZfQIgD5nblHNWAxDmIa2EFl-i1gr1y-5DVMjGztC3WQLJnT44VV7MEWTCCaDO0Yiod0DIWelcONIkUYoJGE27serGs4JveiMrUaquaVLF52dn6ezjfm07eBR1cIs2aohkSjvHIizNAJrqkeC0Qbk0fv7KWKFO1leGABzvd81ZwUFROFNyY9iEoUvvFhr-K1Mdc0kahIby04tEal0QMVWRVjGpTLIgc9TyfLnTkxdOTV4HW9U2-mSUqLIDcuvxZCsYuN18ueyugZ-FMo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95bbb3482d.mp4?token=PTcQBL06NzJk7t_u4yB-8xJ24G7tnYLP5e-Otj39e_jKz9mj_W0n0G0h7lerxk5tLAxinZfQIgD5nblHNWAxDmIa2EFl-i1gr1y-5DVMjGztC3WQLJnT44VV7MEWTCCaDO0Yiod0DIWelcONIkUYoJGE27serGs4JveiMrUaquaVLF52dn6ezjfm07eBR1cIs2aohkSjvHIizNAJrqkeC0Qbk0fv7KWKFO1leGABzvd81ZwUFROFNyY9iEoUvvFhr-K1Mdc0kahIby04tEal0QMVWRVjGpTLIgc9TyfLnTkxdOTV4HW9U2-mSUqLIDcuvxZCsYuN18ueyugZ-FMo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الكويت</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76795" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76794" target="_blank">📅 02:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76793">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cc4a4ac1.mp4?token=gbxzTuO3i8RISWCYTq945_lRGJln8KUuA-Z-w2M7zmkS3rwJY-5026W6Qw1EagShs3cKTNKezkL2LfgpBOIvotmAWT_N4yaHOoqye1YMcl-a27a9OHzyx-AqzVoz4Eahq-0wuvINg7feBfzaL1M5xtMOtcQCq65ueAgsOWy-JpNxnfNfo41SGglgrL1Jh4gGET4oOqg0Ltu5qoBDTOSQdUDjCECjq-AXLOTFkTGCNMw7sS2oyZR8nvqE_z8hL_rzM7_B-KhmFK4eRZtK99uQacJkgOPV1mVncfpIKfgSObutvbiKu0LbYr9XGS2-rJazWWfQtldsU3JuNdvphLWGGG6ceTXg63U0W-qqRGq3aG6z8eEv-O2a3yRAuP--pK_KxaQKXm5NpcPFV7xwcYi3TbZfF99kP7URYZRBSRp4M0MmYd1uWmiP0vs--sdYN75GceT6JXZjI7MGX-jhtu2dW4fkh5Sith_RZkAXr152zafhAAZ7xTMv8ellKX2fsm7ENoFVYQVZm4YcOvJbO0_KqC-jdxzn0HBxpVF6aBP81SvdRuN7cZz3tjEhhtdVKtu43rSFqeyE7HYB9oQPdkdRXLAp6b3WH0p7WxiHf10fo8O7mWcf2-hExKbaXiPslPkcMYpjFlrnDxPx7Nf2a0DIsjafdMJ57hHEOwAa-K9krsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cc4a4ac1.mp4?token=gbxzTuO3i8RISWCYTq945_lRGJln8KUuA-Z-w2M7zmkS3rwJY-5026W6Qw1EagShs3cKTNKezkL2LfgpBOIvotmAWT_N4yaHOoqye1YMcl-a27a9OHzyx-AqzVoz4Eahq-0wuvINg7feBfzaL1M5xtMOtcQCq65ueAgsOWy-JpNxnfNfo41SGglgrL1Jh4gGET4oOqg0Ltu5qoBDTOSQdUDjCECjq-AXLOTFkTGCNMw7sS2oyZR8nvqE_z8hL_rzM7_B-KhmFK4eRZtK99uQacJkgOPV1mVncfpIKfgSObutvbiKu0LbYr9XGS2-rJazWWfQtldsU3JuNdvphLWGGG6ceTXg63U0W-qqRGq3aG6z8eEv-O2a3yRAuP--pK_KxaQKXm5NpcPFV7xwcYi3TbZfF99kP7URYZRBSRp4M0MmYd1uWmiP0vs--sdYN75GceT6JXZjI7MGX-jhtu2dW4fkh5Sith_RZkAXr152zafhAAZ7xTMv8ellKX2fsm7ENoFVYQVZm4YcOvJbO0_KqC-jdxzn0HBxpVF6aBP81SvdRuN7cZz3tjEhhtdVKtu43rSFqeyE7HYB9oQPdkdRXLAp6b3WH0p7WxiHf10fo8O7mWcf2-hExKbaXiPslPkcMYpjFlrnDxPx7Nf2a0DIsjafdMJ57hHEOwAa-K9krsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق اخر من الهجوم الصاروخي على القواعد الأمريكية في الكويت</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/76793" target="_blank">📅 02:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e1fda2c0.mp4?token=nZeIUAHnMijbCOE_ZIp96vCQpzoI7Lxjlh7nFJu43vjjcrCW9dMbgF31vlUTyD1vPgCD7_gzGT0ug6JjxgnCzzLz02PVloXHpaju9d9a5r90c9Jj4s0auNX5XAGrmc7Iflcp8ZE3K3TX2LMHMiOiOWZAYl-eqVcNEgL24TS9dQKrd4Ol6Mjp84HwOWrCt-F_PSMNjivgV-YOt0Wqz7eCK8bwplEbbyru0LUUCVBA0gyKPQpLXsrkYEx9LsZaaqYyhf684SE8PVwORaEBHpDZWXWltb0Rg03NdAMvop6v0lFNJpa4uaaCE6qMN_ginat4l7keHBIHHs7MqnTCCvryW0oKJYYcwF1acnE-bl1Fz8PJCASpr7NIMbx3K1Y6H0UMQ0OBSKeAc9ho9lj8C8R-OvqUSYefDCwY2TArIYcfaJVNd0TkjZnyClGhYZj7v-uIEcErLprC9HRTEg0MyQNg_r1RXRTLG8VCn4MZNuzQZSwhvcfElWkFTFrFNXAN4bGBhtNLJHO5phz0cOBBzNSDxCNALXl4PKoCsRRFcWkZQtkbQpyBFJ351t1YezxAgVBBAnFBd4cuz1Gupz9FJL9HVflRwjZMUYXR-kSHRF_Fj_kAhXaiozsiHxI4t4Nfwyn7dkcCWz1QGVC2NF1F9dH-D4tufo9BsjjWW_m8A9oXtJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e1fda2c0.mp4?token=nZeIUAHnMijbCOE_ZIp96vCQpzoI7Lxjlh7nFJu43vjjcrCW9dMbgF31vlUTyD1vPgCD7_gzGT0ug6JjxgnCzzLz02PVloXHpaju9d9a5r90c9Jj4s0auNX5XAGrmc7Iflcp8ZE3K3TX2LMHMiOiOWZAYl-eqVcNEgL24TS9dQKrd4Ol6Mjp84HwOWrCt-F_PSMNjivgV-YOt0Wqz7eCK8bwplEbbyru0LUUCVBA0gyKPQpLXsrkYEx9LsZaaqYyhf684SE8PVwORaEBHpDZWXWltb0Rg03NdAMvop6v0lFNJpa4uaaCE6qMN_ginat4l7keHBIHHs7MqnTCCvryW0oKJYYcwF1acnE-bl1Fz8PJCASpr7NIMbx3K1Y6H0UMQ0OBSKeAc9ho9lj8C8R-OvqUSYefDCwY2TArIYcfaJVNd0TkjZnyClGhYZj7v-uIEcErLprC9HRTEg0MyQNg_r1RXRTLG8VCn4MZNuzQZSwhvcfElWkFTFrFNXAN4bGBhtNLJHO5phz0cOBBzNSDxCNALXl4PKoCsRRFcWkZQtkbQpyBFJ351t1YezxAgVBBAnFBd4cuz1Gupz9FJL9HVflRwjZMUYXR-kSHRF_Fj_kAhXaiozsiHxI4t4Nfwyn7dkcCWz1QGVC2NF1F9dH-D4tufo9BsjjWW_m8A9oXtJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء البحرين تشهد هجوم صاروخي</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76792" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76791">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4c6cfc93.mp4?token=lCwjFhGcaH_aqZEOBB25bcoaBK7efHfvlwudz6v16QSQ2UMgJNnumCAd-1kkYUaVkQIZlU9Mib3W0zi0yrVzJ1mewgyxygrWOD-P6z0bip7oTpxaXAZ7izlI5JpsNthErokuYbhlrx-JZND_uCkDROyYGEpBORqfTDi9Wo6xUy093rIqH1cESOOHFdXL3PVvmmq95sA4aTxxV1UCwMAaG072bkCfMukFu4kodGAPy4xxqeIJPKj7jrAJV5XC3p_UK9STbHBWoN_IPngSsr4jmGSQ3QgmJbYjWy-k7FJqD_YMHWScB0o4_IVYlf9mS28-ZXFQPWEY9L3MDsS0NWtcpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4c6cfc93.mp4?token=lCwjFhGcaH_aqZEOBB25bcoaBK7efHfvlwudz6v16QSQ2UMgJNnumCAd-1kkYUaVkQIZlU9Mib3W0zi0yrVzJ1mewgyxygrWOD-P6z0bip7oTpxaXAZ7izlI5JpsNthErokuYbhlrx-JZND_uCkDROyYGEpBORqfTDi9Wo6xUy093rIqH1cESOOHFdXL3PVvmmq95sA4aTxxV1UCwMAaG072bkCfMukFu4kodGAPy4xxqeIJPKj7jrAJV5XC3p_UK9STbHBWoN_IPngSsr4jmGSQ3QgmJbYjWy-k7FJqD_YMHWScB0o4_IVYlf9mS28-ZXFQPWEY9L3MDsS0NWtcpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76791" target="_blank">📅 02:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS5yBW14WkUuQOODYIVBgUNcVQ4tvt8VtqLipoFiNaR6q0Gmk2KZt3JcMU9CjEaLZp6lGHPTWokrnDjH-WYzMPLlomCAOXh-w8kMLp04YCJBmsoKie68AJt_e15lwUVe_vyGI1KyDUaX2vcQ4lLd9smMVUl5f9ypSUm97l0KFjAUqsQnKKcghzp5PmMpeE0sW8r9yoLV_jou4fPpasDvKmUTITJFvuGwoR4yGnCIhz5BJwzUaembbB3x7kMsoG0U87aPYew9f6dNMA6KIQcfZncfEm6UnSy1LUA_kglJFizABV48dCNvt78HkcQua64K_5dvLaaF0C3EGIDnpXdK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ تنطلق من ايران</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76790" target="_blank">📅 02:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=LnC4gbDU20YtA9DuSacck-vDDbXwBwjgAbajPVaB0ZcpD4blemV-8XiKoZ7dap5se1empPZOJXPe4S16yoJhhQ4ePHUocOwOikTLF38BNu1PgzQ--e2iuMJfo0U_sl3Do462J0RTJvOsZ2Qxew_r4-B-hLbtORA6vYyeDW5IYHAyIbyHKTtQRCKpGZ8B9H54nUp0ZEupHNoA3L0z_Ux_7h39ks3jWCECbgChe9JAWYidLpILlpxGsVsuF-YZ0AFGkUg31MfmC-xsAxYI51caIqDJ3eyZ6_GRv2uYoYd38oYgrN9Nui4zh01a22_sdqww4W0FXd-jpr_mxtFfl2t4bix4u0HCJAX-u6TNGl9kJUHExFCif7JCC0arAF280mt3JfykAYyhzLKmUQhmZjXeKH3K4aAQOPQ9zmO92KegvGbqxtQ1iV6c4hZDsnq1Z460I4MJbg6aBN3JpVTOdXQsRzo6m7tPJsJojIXYjCbjl5k9cAOLGxitb3I4Oy9gks_1EK472-IAnBmHM2mnzKsivDYpoYH5efLnJ_Vo_O496hROHyLdFXB3nX6HB5-C-byho9a_9luceMr5HDykzKLz0k1HZqAe0cQsaQBOYDyG_2610BnsIWg1nMo841oz0JhrUTJlJFVic4lrynzaWdajTbp4Lweao8dR3EQG80cXMxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=LnC4gbDU20YtA9DuSacck-vDDbXwBwjgAbajPVaB0ZcpD4blemV-8XiKoZ7dap5se1empPZOJXPe4S16yoJhhQ4ePHUocOwOikTLF38BNu1PgzQ--e2iuMJfo0U_sl3Do462J0RTJvOsZ2Qxew_r4-B-hLbtORA6vYyeDW5IYHAyIbyHKTtQRCKpGZ8B9H54nUp0ZEupHNoA3L0z_Ux_7h39ks3jWCECbgChe9JAWYidLpILlpxGsVsuF-YZ0AFGkUg31MfmC-xsAxYI51caIqDJ3eyZ6_GRv2uYoYd38oYgrN9Nui4zh01a22_sdqww4W0FXd-jpr_mxtFfl2t4bix4u0HCJAX-u6TNGl9kJUHExFCif7JCC0arAF280mt3JfykAYyhzLKmUQhmZjXeKH3K4aAQOPQ9zmO92KegvGbqxtQ1iV6c4hZDsnq1Z460I4MJbg6aBN3JpVTOdXQsRzo6m7tPJsJojIXYjCbjl5k9cAOLGxitb3I4Oy9gks_1EK472-IAnBmHM2mnzKsivDYpoYH5efLnJ_Vo_O496hROHyLdFXB3nX6HB5-C-byho9a_9luceMr5HDykzKLz0k1HZqAe0cQsaQBOYDyG_2610BnsIWg1nMo841oz0JhrUTJlJFVic4lrynzaWdajTbp4Lweao8dR3EQG80cXMxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76789" target="_blank">📅 02:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ab10aec0.mp4?token=ORRoFEFQ8zENUaybyOW9HvWKrg8uD65EggTc_Rx8IOyc18CbDIidgoyIEp_D2uy9DE3fobxd8Et9zu3S8mfznjc8KprgW94Tbx_7mq61jUY-aOxO7Xq2tGX5BzuHqIyNzd6L6H-OFpduh2Qq8gZI0Y4a42hi6YTh4szO1H9Lk7B-4T0kqD5gVFNomVcXICzTmnLmbixz4EmR8wguszO7WlTweW49haqpy5o-8DgqdjGEBPRvNR3QX0dkUc0w2k05pCdOKjEA2vZIjrB0xA1CytpWVh5qT3tCffMy9bMJUrehni7Tese1sb5savHqZxt937lZ8XPUjA35BjqhEkNfCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ab10aec0.mp4?token=ORRoFEFQ8zENUaybyOW9HvWKrg8uD65EggTc_Rx8IOyc18CbDIidgoyIEp_D2uy9DE3fobxd8Et9zu3S8mfznjc8KprgW94Tbx_7mq61jUY-aOxO7Xq2tGX5BzuHqIyNzd6L6H-OFpduh2Qq8gZI0Y4a42hi6YTh4szO1H9Lk7B-4T0kqD5gVFNomVcXICzTmnLmbixz4EmR8wguszO7WlTweW49haqpy5o-8DgqdjGEBPRvNR3QX0dkUc0w2k05pCdOKjEA2vZIjrB0xA1CytpWVh5qT3tCffMy9bMJUrehni7Tese1sb5savHqZxt937lZ8XPUjA35BjqhEkNfCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ إيرانية تشعل سماء الكويت</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76787" target="_blank">📅 02:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ky21UBlxaf1RU-o84V84CYUNrp4sEjwO1-3TsfEunyaJRUkxF20jJv8FiMmgD-eh5lQG_Ll2Ns86iyLsR77luHrWWW2S1pDSMaauTs9wJNJ7yi2A4EOAHR957CgPORtfu8T8-uy-USy6_hKOxp4twhPCY2Ow9jFjKMj2MC3avylF8T0c9RpWbqzPQR9GJ0CM9ttcd__oNHaS_Iisc2bxYivh2DITMII5SLUttk7JSuXOg4EioyN33j4mJHKTECTsbSbdWGtdaqNUXY0yR0l10BSnSo-Y8CBPZs2Y7RflbeO4LD0jchhhIGYqBaos-X3_OzTPF5-rwqWcJPD_ElP5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئاسة اركان الجيش الكويتي: الدفاعات الجوية الكويتية تتصدى حاليًا لهجمات صاروخية وطائرات مسيرة معادية، ندعو الجميع إلى التقيد بتعليمات الأمن والسلامة الصادرة عن الجهات المختصة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76786" target="_blank">📅 02:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76785" target="_blank">📅 02:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76784" target="_blank">📅 02:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رئاسة اركان الجيش الكويتي:
الدفاعات الجوية الكويتية تتصدى حاليًا لهجمات صاروخية وطائرات مسيرة معادية، ندعو الجميع إلى التقيد بتعليمات الأمن والسلامة الصادرة عن الجهات المختصة.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/76783" target="_blank">📅 02:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صواريخ دفاع امريكية تتساقط على سكان الكويت بعد فشلها بالتصدي للهجوم المركب</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76782" target="_blank">📅 02:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76781">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5a837cee.mp4?token=Wbj3xJlv9JM53xB9crRrYgmSHy7hmX7vC1AN2ySt-8-DoUgVnBrSFktmh0oAI6oI-RWJ3kb1wlGa4yKxCEHycfrXnBq6m8BPMhfjFSobGTXN_L9LxPTfUrck33DTE6Ptuoc6ErSznks8zZ5OcdcgBLXZJq1-SALQlAJ-091IOLQNgQ0wlFLP9mhMV41MlgAPUNPMQOKmT6ObBwCGTwBlSAdz0-qsDBcQifbJd27VyXQkM3ptRYNzyJxXZJQrVc1BIigIyPudngdmuKizN53CiNZNwW7IvAWcqCsVY0-kJRfzLWc0ZSjDpOpTXPDLRTNyFxock0NqtnxeFWbN3rGFWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5a837cee.mp4?token=Wbj3xJlv9JM53xB9crRrYgmSHy7hmX7vC1AN2ySt-8-DoUgVnBrSFktmh0oAI6oI-RWJ3kb1wlGa4yKxCEHycfrXnBq6m8BPMhfjFSobGTXN_L9LxPTfUrck33DTE6Ptuoc6ErSznks8zZ5OcdcgBLXZJq1-SALQlAJ-091IOLQNgQ0wlFLP9mhMV41MlgAPUNPMQOKmT6ObBwCGTwBlSAdz0-qsDBcQifbJd27VyXQkM3ptRYNzyJxXZJQrVc1BIigIyPudngdmuKizN53CiNZNwW7IvAWcqCsVY0-kJRfzLWc0ZSjDpOpTXPDLRTNyFxock0NqtnxeFWbN3rGFWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الامريكية في الكويت تحاول التصدي للهجوم الصاروخي والمسير</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/76781" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76780">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4649ab83e9.mp4?token=iC6Z406rEQO9XdGgNXKusvUipjRA2Dij0XidZHBKgsEQmaC7HQ6kesv_32zn5uU-YpI_veteJRuvSfn678ZS1CmcRTxuMJM38xsk8BV8_vIm8le4qUW0ACpCA2kP8X2nD_6GGNhMahxdTRlGiTxsTsmmMs6z7qVa2XZ3nLfADGHQ9iEKBWIphjg_0PYk2pdFnAqXYOcnNDEBRQEd0YoXqN1rOI7Uc9mJtBUhO2G6kMJD8gX6tHGsCFMhNUwPjwy0VGj-MH33hDsRERDhj6Et1-VtUf726hMG4VIQHgZwBF_7s5vJmdR_mhTk5NYwjWeYMT-xFwPhg62K0a5Y1Eu_pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4649ab83e9.mp4?token=iC6Z406rEQO9XdGgNXKusvUipjRA2Dij0XidZHBKgsEQmaC7HQ6kesv_32zn5uU-YpI_veteJRuvSfn678ZS1CmcRTxuMJM38xsk8BV8_vIm8le4qUW0ACpCA2kP8X2nD_6GGNhMahxdTRlGiTxsTsmmMs6z7qVa2XZ3nLfADGHQ9iEKBWIphjg_0PYk2pdFnAqXYOcnNDEBRQEd0YoXqN1rOI7Uc9mJtBUhO2G6kMJD8gX6tHGsCFMhNUwPjwy0VGj-MH33hDsRERDhj6Et1-VtUf726hMG4VIQHgZwBF_7s5vJmdR_mhTk5NYwjWeYMT-xFwPhg62K0a5Y1Eu_pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من سماء الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/76780" target="_blank">📅 01:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76779">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3nizMuk33qBlbkh1Epf-lXjtc0IVhKJ4DqNlm1s8b4zz7OCNQA6zmBPZpciqnoFtrV8Zno3VkShF2saEmDu4O0lZ6SE6y25ggc_GSXmIaHKaKoyp43OBg9ZEsEzFmzVtMe3uCdmE7poCX7yQGH-38g1ifeCGIN-a41z-zGADMCgAsSnno8FSsaYzifTKDNh7s0MbX1kjg89P4FICz5_TkNi_J-f287h64KvD_8r5h5PeYdvGNAf7IyTiSSAHM-fgfzVg1UKz3Qr_ITNJeNYbed37j0kJ23N6oHeRBmStH1nwKSEp_p61nUIZ5hXlKdwJiRqhjf7nX5jsNRqvzqsoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهود عيان: انفجارات تهز منطقة جنوب السرة في الكويت</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/76779" target="_blank">📅 01:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزارة الدفاع الكويتية: نتعرض لهجمات صاروخية وطائرات مسيرة معادية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/76778" target="_blank">📅 01:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/76777" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b49a37c30.mp4?token=deXtTyY4_M6ZLbcd_KcyInlIHsqD58tis46VfGcVsDXjXDXm_X2c5H8k1Pw__bruai5VAd8l6ix-jrCErxJsyEE4JKuNW6uYELMPArJnxkSOLf6jhCYKOeL3O-diRGDnXuyKtwrRnqiIoXm5KH7mCe88yj4PA2JkVkNjytTOk4_eqUe0CaAWQxBvtEz6xJeOWYpcWTan8AALYJdjVnDq4cDCnxdruae2-bXLlnziSyx27v5bScb6ndHf3jbiBjgaKTO_CK323EcVzeLnjbgSmxg0X8e5FJoKax-q3NyvwtitG3UhOfgN6gOyWs7U5UlvGfJ2Um87vXkgcFTI_zv_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b49a37c30.mp4?token=deXtTyY4_M6ZLbcd_KcyInlIHsqD58tis46VfGcVsDXjXDXm_X2c5H8k1Pw__bruai5VAd8l6ix-jrCErxJsyEE4JKuNW6uYELMPArJnxkSOLf6jhCYKOeL3O-diRGDnXuyKtwrRnqiIoXm5KH7mCe88yj4PA2JkVkNjytTOk4_eqUe0CaAWQxBvtEz6xJeOWYpcWTan8AALYJdjVnDq4cDCnxdruae2-bXLlnziSyx27v5bScb6ndHf3jbiBjgaKTO_CK323EcVzeLnjbgSmxg0X8e5FJoKax-q3NyvwtitG3UhOfgN6gOyWs7U5UlvGfJ2Um87vXkgcFTI_zv_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/76776" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة قشم الايرانية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/76775" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
