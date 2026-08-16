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
<img src="https://cdn4.telesco.pe/file/OHCKsSt6yC4Y-hRuM4em7Us2bCvHpQgNjo1PzWZXt71eMBMXLbyuYdauQs-XgFTuOptif2oUfOly7waytxTeTxZKE0Nm-Cxbd5KKJqLHJYUozgDE4ZCpX3PlRzSFQZQ5WBgAwzAH6DOvHFI2thDKduKSie5LNAIXLw2J5qyYqmoU9cElCaqSmR-2PKO1hRX6sxgG1p4EMs-2E7Bm0pEcGg2nccIj7ImaG1YHyYhvJYCVe4XidzHsYOgwhjdVTvLHjomB8tqxY_1Lf5QxupLvMvb-qpp-dgiLxu2XLf9CWkxdB2B-Qh_r0p8NmpPak1MTnYcqQjpDz1bY4zNJn3Y5CQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 12:24:01</div>
<hr>

<div class="tg-post" id="msg-87890">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
حاكم مدينة مهران الإيرانية:
صوت الانفجار الذي سمع قبل قليل في مهران ناتج عن عمليات تدمير الذخائر المتبقية من الحرب في الأراضي العراقية، ولا يوجد أي حدث أمني.</div>
<div class="tg-footer">👁️ 501 · <a href="https://t.me/naya_foriraq/87890" target="_blank">📅 12:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87889">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
القائد العام للجيش الإيراني:
بمشاركة الشعب، إذا تمكن أي جندي إيراني من القبض على أو قتل جندي أمريكي متجاوز، فسوف يحصل على جائزة قدرها 30 ألف دولار من الشعب الإيراني.</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/naya_foriraq/87889" target="_blank">📅 12:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87887">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NReLswzqkJl8Nk2iKH8q0b7jpATWROTaXyAqs5A_plAi3S9d2kUeljw9gvzfo585NMJyPyfYd9V2ZOSrRTCftsdMHTh9U3KHgBDbJbdNCznzQCp-M-j7J-axM4M_dB5c4C591gkm04m6jpBeskrjqUK0s4HimhhJtYA6MMPNWftQ_vWIT29AMqCIbuDIit_oitK54kWKwzLB__2ZU1pbvpCqTM8cp1O3j9JxSJKmIMVwKTbPmBtFQ-YfVKJIRtOnxfEdQ3Il4yqvZa4M2tlvYAp3knmnBIxVUOCreLbc-xw1aXXDXh7WDxUVZETnGeFxafs4tVu60R2WXQZ8gJRv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c305e2b0ee.mp4?token=IicCBFZ0vJIpW7sSAVEWYs5x5NHSN6ymz5RPs2FtD-AG3xchR9NwLsBTmzDhq2B2tmufNbwOrQOUPivJOIl4l_H3B4--pH5Yum_vUAsp-rwLi2nv2Onmeez6P56SLm33kXl8M8Y4AjRtdkMKk9u3OmuL2Stl49FcXnUa55ItjU9bHeeIbvDoCAJkHFqU_km1GDoDLnktnrBp3llfQOOVSqkY54aRrRIu-Le5djKj_DSc2WrjnPlEgK-mjGtb-gXRDr61qIJgAjbml_ixd8Hf6Std-Ibfj9CDOxA83v_GTfa4yok-VdecctItI-dsrg5IhwWH9nKvj9Tj7fEQtj4IQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c305e2b0ee.mp4?token=IicCBFZ0vJIpW7sSAVEWYs5x5NHSN6ymz5RPs2FtD-AG3xchR9NwLsBTmzDhq2B2tmufNbwOrQOUPivJOIl4l_H3B4--pH5Yum_vUAsp-rwLi2nv2Onmeez6P56SLm33kXl8M8Y4AjRtdkMKk9u3OmuL2Stl49FcXnUa55ItjU9bHeeIbvDoCAJkHFqU_km1GDoDLnktnrBp3llfQOOVSqkY54aRrRIu-Le5djKj_DSc2WrjnPlEgK-mjGtb-gXRDr61qIJgAjbml_ixd8Hf6Std-Ibfj9CDOxA83v_GTfa4yok-VdecctItI-dsrg5IhwWH9nKvj9Tj7fEQtj4IQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إصابات في صفوف المتظاهرين من خريجي المجموعة الطبية جراء إطلاق قنابل صوتية ومسيلة للدوع من قبل القوات الحكومية.</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/naya_foriraq/87887" target="_blank">📅 12:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87886">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇷🇺
🇬🇧
ذا صن دي تايمز:
استُخدمت طائرات بدون طيار بريطانية لأول مرة لشن هجمات داخل روسيا.</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/naya_foriraq/87886" target="_blank">📅 12:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87885">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
نتائج الحرب مع إيران.. وزارة الطاقة الأمريكية:
تراجع مخزون الاحتياطي النفطي الاستراتيجي إلى أقل من 300 مليون برميل.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/naya_foriraq/87885" target="_blank">📅 11:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87884">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇦
زيلينسكي:
13 منطقة أوكرانية تعرضت للهجوم هذا الأسبوع وأطلق الروس أكثر من 1550 طائرة مسيّرة هجومية ونحو 1560 قنبلة جوية موجهة و62 صاروخًا على مدننا.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/naya_foriraq/87884" target="_blank">📅 11:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87883">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴
مَرَّ أربعينَ يومًا…
چهل روز گذشت…</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/naya_foriraq/87883" target="_blank">📅 10:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87882">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
هيئة أركان القوات المسلحة الإيرانية:
نؤكد أننا لن نتراجع حتى تحقيق الهزيمة الكاملة للأعداء الأمريكيين والصهاينة في المنطقة، وتحقيق الحقوق للشعب الإيراني البطل، وخضوع العدو. ولن نتنازل عن المطالب المشروعة للشعب وتطلعات قائدنا العزيز، في وجه أمريكا المعتدية.</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/87882" target="_blank">📅 10:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87881">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
‏
الحرس الثوري:
على قطر السماح بتواجد فريق من خبرائنا بدلاء من إنكار قضية احتجاز الطيارين.
‏خبراؤنا ينتظرون دخول قطر منذ عدة أشهر لإجراء تحقيق ميداني بشأن مصير الطيارين.‏
قطر ترفض إدخال لجنة خبراء وتقصي حقائق إيرانية للتحقيق بمصير طيارين إيرانيين.</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/87881" target="_blank">📅 10:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87880">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇾🇪
🇸🇦
إنفجارات عنيفة في مدينة المخا اليمنية جراء هجوم لأنصار الله على مواقع مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/87880" target="_blank">📅 10:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87879">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0696943056.mp4?token=JCT-mfRO86mJCpHxe1a53MPN5lro10QtMJ_9O4RH51szH8OdlyJkl-FEMpsoO3eN4G5ENMLN6HDmdzd-v_8mz8zGKl74FB7-5yrqYzG3NiX5ftJVA8-cs3uT6L9pdkoJsNfhrHy9d7IXiCTJN8y0xsgzj3xJPIolv6dkgm9lexLd8AdsJkEBOAWUIQ8Ub5P9BHU2pfXvk4lPK2AkpGT53ABOxKaXkWvn-YA7mHDnN0HWRFmypqU2lmAnfAN1JhTdpT_8f6AzEYDIhM126pWTWo_ZV5GfQjy82x_-hw9Wy-VJeEVt24U_zrA-fxm-boxP_RbjCbpjcXGbsdrjlakG7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0696943056.mp4?token=JCT-mfRO86mJCpHxe1a53MPN5lro10QtMJ_9O4RH51szH8OdlyJkl-FEMpsoO3eN4G5ENMLN6HDmdzd-v_8mz8zGKl74FB7-5yrqYzG3NiX5ftJVA8-cs3uT6L9pdkoJsNfhrHy9d7IXiCTJN8y0xsgzj3xJPIolv6dkgm9lexLd8AdsJkEBOAWUIQ8Ub5P9BHU2pfXvk4lPK2AkpGT53ABOxKaXkWvn-YA7mHDnN0HWRFmypqU2lmAnfAN1JhTdpT_8f6AzEYDIhM126pWTWo_ZV5GfQjy82x_-hw9Wy-VJeEVt24U_zrA-fxm-boxP_RbjCbpjcXGbsdrjlakG7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر امني   اصوات الانفجارات ناجمة عن استخدام قنابل صوتية من قوات مكافحة الشغب تجاه المتظاهرين السلميين من خريجي المجموعة الطبية المطالبين بالتعين .</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/87879" target="_blank">📅 09:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87878">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/87878" target="_blank">📅 09:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87877">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/87877" target="_blank">📅 09:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87876">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/naya_foriraq/87876" target="_blank">📅 09:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87875">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏
🏴‍☠️
🇷🇺
بلدية موسكو:
تعرض المدينة لهجوم بـ 600 طائرة مسيرة ليلا وإصابة ثلاثة أشخاص</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/87875" target="_blank">📅 07:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87873">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29dd6be136.mp4?token=P73iUCTNzZes_aJRm2HMn8vgY2IFuf_kTcGyIdzNsBVHXMDs1kbN7ZxuKS1oK5QbytWETPRa9NsfW5sAVrnC53v1bkmi1f19H0cc9pOW3SpT3MinV_l64-5arMsjAxs3_dHvPz8fHs9KV46r6yK5NWzIGgVKVlPcICyCI4gssH4lt_iT7uL9E0ipSTxRXP7H3JuLtUoFWLH5KJWRjim4MbEgcYE9h4BgVHoqTTla7jvmZ2gM3QYhpLp4j1pQoRh1mDsUcJ38ef5PHMkHBnBAmwDbfxpwbsSz0RXwcF3YOQZQb9Drao1apBN96kaB1nJ_MWaOqS0bG9V83HpHzrghNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29dd6be136.mp4?token=P73iUCTNzZes_aJRm2HMn8vgY2IFuf_kTcGyIdzNsBVHXMDs1kbN7ZxuKS1oK5QbytWETPRa9NsfW5sAVrnC53v1bkmi1f19H0cc9pOW3SpT3MinV_l64-5arMsjAxs3_dHvPz8fHs9KV46r6yK5NWzIGgVKVlPcICyCI4gssH4lt_iT7uL9E0ipSTxRXP7H3JuLtUoFWLH5KJWRjim4MbEgcYE9h4BgVHoqTTla7jvmZ2gM3QYhpLp4j1pQoRh1mDsUcJ38ef5PHMkHBnBAmwDbfxpwbsSz0RXwcF3YOQZQb9Drao1apBN96kaB1nJ_MWaOqS0bG9V83HpHzrghNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇶
🇺🇸
فضيحة عنوانها منظمات المجتمع المدني المدعومة من السفارة الأمريكية في بغداد USAID
تداول ناشطون على مواقع التواصل الاجتماعي مقاطع فديو لناشطة معارضة لقانون الزواج الجعفري المقر موخراً بمظاهرة قرب المنطقة الخضراء وسط العاصمة بغداد ادعت انها شيعية وان القانون جعل الشيعة مضحكة امام العالم لتكشف صفحتها على الفيس بوك و مقاطع فديو سابقة تتحدث بها على انها مصرية ومن السليمانية فمن نصدق الفديو الأول ام الفديو الثاني ؟ فيما تسأل ناشطون عن الدور الحقيقي لجهاز الامن الوطني وجهاز المخابرات العراقي وتفعيل دورهم المطلوب والرادع عن طبيعة هكذا تجمعات وشخصيات ذات هويات متعددة !</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87873" target="_blank">📅 06:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87872">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrhYXpqKrrvRn3R2Omae2FClA-sjgDfm_FQ1HrHfWwmIzb65yl_jnmKLWXkpvVlI71S_x8wFbgxdaFuTwhplPca8Yn-4K5IzvA5oPJhXccV6ru05c5MZ63ef2yiCRLCcBe4YZPUpeGCNbol2eNUHw7QFnFW6IlzRj-4uzfJ6zFUvQ8JmrIT4iO7XpweThWYjlX0FUKjGzdpy-WenwwpHpZN5Y0fdBOzE9PzWLSMHbThAkTFKs8fNDzzjtEZQksIAMJuGn6gGmtx79-8rnfAjrzjhsrRFqRVaabUtrprjxvX4IMOM9EqjWAIB9NP8v3C7q4evpjtrBbW3Ah4t5FMOpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إنّ من أوضح أوجه السيادة المنقوصة للعراق هو هيمنة امريكا عليه اقتصاديًا واحتلالها وسيطرتها على امواله حرفيًا وتحكمها بثرواته كُليًّا.
فهل يرتضي الأحرار للعراق العزيز أن يتعامل مع ثروته وكأنها منحةٌ تُسلَّم له، لا حقٌّ سياديٌّ أصيلٌ لشعبه؟
وهل نطلب كثيرًا إذا أردنا التحرر من الهيمنة المالية والاقتصادية الأمريكية، وتنويع أسواق التصدير وشبكة العلاقات المصرفية، وبناء اقتصادٍ يملك قراره وثروته ومسارات تجارته؟
فالسيادة لا تكتمل بالسيطرة على الأرض وحدها، بل بامتلاك القرار السياسي والاقتصادي والمالي بعيدًا عن هيمنة ايِّ قوةٍ خارجية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87872" target="_blank">📅 01:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87871">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRyPbEhjljPDj9SOp-xxE9dBOq7FsXsHpWjEmMhawkxzCC7UAeemhJdroXZXToQbH2ayw6AO__IOctbMeYZcOXOA9b6zy1q-bB1KvkE1oyLS3Fj8mTCxVVvNCratPifQDW-R-JDTQMFnpz4M5JPnLD8eXqfCBv7aRwLWAgutQftg3F161UHtKc6POdqhNIX2TCIW1gR2XEvYnYJAFIP_BUO24Pc5vp4UVkv7x1BGoaXpGHJXI_7CcTrkkycX0SH2mqwdGmJosOq5h9_beNl6wn94nel7G0-lQuU_KfeJECtKYETUlA4Yt8DtOaKKs1SlAAfxiSDCVBvFIf_iniefMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
سنتنصر.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87871" target="_blank">📅 00:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87870">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb4c61f98.mp4?token=Uj09Li-_Jpm2q3lDrefmqo-EOtXxZhKbLZ6HLV2TvE7Ru57GoRMGIsjhTNc3dX-sWksFjUzi56anviTJ8YAKXbIxaBoEcSVG7mfeZNKOQjWNfuFRE_Gxw1hSSvsT8HZ67hoXihZnJDY5dVSSyke49B637P4Qy4hQxXWDs3igfyGit2kRBa2CUsmXvQVvXggU4P-6x7LjRyYlPWhMBR0VeWh1pDp4RwdBkZjzHP0Obs448GrdKhILBqi2uvo4t1OrWeJUowJofUgyKbL_pg0x4xxCtgF58qfEQMcnlvJDqXHM5wPAfCBJsKGMCChtrL53M0-lRXu6Tcw-jc2il2rCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb4c61f98.mp4?token=Uj09Li-_Jpm2q3lDrefmqo-EOtXxZhKbLZ6HLV2TvE7Ru57GoRMGIsjhTNc3dX-sWksFjUzi56anviTJ8YAKXbIxaBoEcSVG7mfeZNKOQjWNfuFRE_Gxw1hSSvsT8HZ67hoXihZnJDY5dVSSyke49B637P4Qy4hQxXWDs3igfyGit2kRBa2CUsmXvQVvXggU4P-6x7LjRyYlPWhMBR0VeWh1pDp4RwdBkZjzHP0Obs448GrdKhILBqi2uvo4t1OrWeJUowJofUgyKbL_pg0x4xxCtgF58qfEQMcnlvJDqXHM5wPAfCBJsKGMCChtrL53M0-lRXu6Tcw-jc2il2rCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
انفجار في محطة كهرباء الحرشة في الزاوية بليبيا اثر استهدافه بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87870" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87869">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd380ae70b.mp4?token=Re_ByfCtgJGlIN1DUWWdMW83edNFzn7LJolTegGa9BUsNEjonly-oNRhd5zTuT3130nt2VuD1rWPcjtqWlKolhR1Hn7oebEBA8_WL0wxnFmRkqL5IAflkXzXnWoln0QlB75iJBtbzHUuh08n21p4G3e9AR-dlmoWDJkyp_ZIKaJWqHWyLdgsfxzIcijrFtfozvVZurcXFAxgakwAIBGT1W2WveGGhvZ3x6LbRY6vZGWOa-5foMom6JS-js-07CzfTHvMCTAtfUTolv8PUfuBc796FRhj8b1Kws2Hr034yVSSqOw2qRnf1DKs0IzADYdg0hCHsMWWD3kY-3C0nXx6qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd380ae70b.mp4?token=Re_ByfCtgJGlIN1DUWWdMW83edNFzn7LJolTegGa9BUsNEjonly-oNRhd5zTuT3130nt2VuD1rWPcjtqWlKolhR1Hn7oebEBA8_WL0wxnFmRkqL5IAflkXzXnWoln0QlB75iJBtbzHUuh08n21p4G3e9AR-dlmoWDJkyp_ZIKaJWqHWyLdgsfxzIcijrFtfozvVZurcXFAxgakwAIBGT1W2WveGGhvZ3x6LbRY6vZGWOa-5foMom6JS-js-07CzfTHvMCTAtfUTolv8PUfuBc796FRhj8b1Kws2Hr034yVSSqOw2qRnf1DKs0IzADYdg0hCHsMWWD3kY-3C0nXx6qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
اكثر من اربع انفجارات سمعت في مدينة مأرب</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87869" target="_blank">📅 22:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87868">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇶🇦
‏
الخارجية القطرية:
ننفي ادعاءات احتجاز طيارين إيرانيين، فرق البحث بحثت عن رفات الطيارين الإيرانيين وتواصلنا مع إيران للتنسيق.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87868" target="_blank">📅 22:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87867">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
رئيس خلية الإعلام الأمني العراقية :
موعد 30-9 ليس بعبع وهناك مفاوضات تجري عبر هيئة الحشد الشعبي كونها المؤسسة الدستورية والقانونية لهذا الملف .</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87867" target="_blank">📅 21:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87866">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇾🇪
انفجارات متتالية تسمع في صنعاء ناتجة عن اطلاقات صاروخية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87866" target="_blank">📅 21:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87865">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
انفجارات متتالية تسمع في صنعاء ناتجة عن اطلاقات صاروخية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87865" target="_blank">📅 21:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87864">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUlVkBF0GuTOqIX3vDyKL9LQ3Y-JtMoaXSnR_mD6yjOfMBuoUh_TrJ9IirVqfNrGyMyol2N0lgofFSzl-BkrL0hi44avR5ScGUo97Eo6BCK7q6Dw3M3SmQ0ou3rrb1NZPQ0jpZ4Y-cNxMfof4uIS1nuWCl30ECUGH_CJ1ICYnCCEyJOqOnhyP9h0ZjGWrTCBj91_2-aX7GuuUGXNGsanuzlKsSLwimPZAKT0KLaGARNqmNpKnwq6OqKheIcEPCBjxsFSPDOfW4X30YAz48X2KdvBFMUVMZx26iIfQwz68W2ZPWT4GeI_8j13dQq9OOd7-gr_WVU_Jx9XkgokOMVumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
ثلاثة انفجارات قوية تهز مدينة مأرب.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87864" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87863">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الله اكبر اصابات مباشرة تطال المليشيات الموالية للسعودية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87863" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87862">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇾🇪
مشاهد متداولة لمدينة مأرب يعتقد انها ناتجة عن قصف لانصار الله.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87862" target="_blank">📅 20:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87861">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_YWiraQxzbqqlmFKkxzfgMHx7yoFi6Pea8cAUpa9roRIkAmomBKpSBQ1eozihNiFA34xFf4-wywkKSsE-kcd05yLNWiwgYBWe9QzHf_2Xu-Eh-kdZKkxBV6Aa1pJkyh0bU9wYt52TgAKtV3M4cDsgPTGTnZejv_79bus-5uxClzQZyun8FtefJ-FGEI9oMODYvJcmpsHGRjQb-KL9zeYvQlkL8osbtKC0dDiCG01reBrGXDXhdGuVvPIsNfwCaE3XGmIv4cQMMst3oP1-QcV6Fg2el-rIscYYQeC-BC1Bq93rTWp-Ejf-j9oNeajl-rZAdmdwkcobinuiwjiWE9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
مشاهد متداولة لمدينة مأرب يعتقد انها ناتجة عن قصف لانصار الله.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87861" target="_blank">📅 20:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87860">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTRPcs1nVRf1NyLlR8Ks1YlVHBC1LSuVLgmV0arOHR8EbEUzV5paaULYBZ5rSuPCgN7CVupiazVfG7Q_kqznIRFixktBktqWiAHUKRp7ifiMekgE0p7TulaMuJr_x5VPU3YGW263XTQTbjBxQkkll1PQnXQb2Q3zeZKATyhNTcu6aqi3S-BjWDTQhSvEKbE7RVFXom_AXXHuwi_4KfSuypyCe9Kzpiab-J-5ghVeOoDJA_mDbJ1tck4eo3RYLbinEprDgQy9G7H1SOMuMIKhD3DrqZqgar7d_QU-ZWqtOaLcy-nDMYwo3G4gnaQaWWk-I-Z7i9iczH0lzhZ1q89l2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هل العالم بوضعه الحالي قادر على فقدان أربع مليون برميل من العراق في حال اندلاع الفوضى ؟!  هل يعلم الإطار التنسيقي ان حجم ضربة لوبيات الطاقة العالمية للعراق الأخيرة الهجوم الأكبر" ضربة السعودية للعراق " كان بسبب فقدانهم نصف مليون برميل فقط من بقيق !   هل لا…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87860" target="_blank">📅 20:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87859">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇱
إعلام العدو:
تعرض دبابة لهجوم في قطاع غزة نتيجة لغم تابع لحماس.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87859" target="_blank">📅 20:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87858">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هل العالم بوضعه الحالي قادر على فقدان أربع مليون برميل من العراق في حال اندلاع الفوضى ؟!
هل يعلم الإطار التنسيقي ان حجم ضربة لوبيات الطاقة العالمية للعراق الأخيرة الهجوم الأكبر" ضربة السعودية للعراق " كان بسبب فقدانهم نصف مليون برميل فقط من بقيق !
هل لا يرى ساسة العراق افول امريكا بهرمز و وضع قواعدها بدويلات خليج فارس ؟! وبروز نظام الدفع المسبق للسفن المارة بخليج فارس  ؟!
هل ستقطع علينا امريكا الدولار الذي هو منقطع أصلا على العراق منذ ثلاثة اشهر ؟! وتمنع علينا بيع السندات ؟!
ام ستقطع الكهرباء التي هي أصلا مقطوعة منذ ٢٠٠٣ ؟! ويومية هزي تمر يا نخلة اجه جنرال الكترك راحت سيمنز ؟!
متى يعرف قادة الإطار التنسيقي ان مصلحتهم لا ترتبط بامريكا ولا البرتقالي وان مصالحهم الاقتصادية مع احزابهم وخوفهم من المجهول لا يجب ان يكون على حساب سيادة وتاريخ شعب العراق …
كل مشاكل العراق وبروز نظام بشكله الحالي القريب من امريكا وتحت سيطرة الحاكم في العراق والشام " توم باراك " بصورة مذلة يتحملها قادة الإطار التنسيقي ال 11 …. وعليهم اما ان يتولى مسؤوليتهم التاريخية او ينكفوا عن إدارة البلد …</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87858" target="_blank">📅 20:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87857">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM5rR1yTuP5ohMS9MFiprEBlhyQAIxRujCWHlijwGQUBHYGGLBF2IVq4l4ZLumrbNCDLz-hSWQIdIvl-nRzCEP6zp9u_7LI581U_zTHitYQnnmU1yUwAbUKy3GhPBcPHqIjY-WzUnOBVJvxC1WwJeeker4kV3dofjZDyompc7IlxGeUFfxI_VHwpSIvnpBBuUbXF4nu7hysxg13Q_w3yix-btXv7r-i6rzDSxBujlnSnP95uMQBzvoafgsxZ_ZgXA7_N-piGyVadyF7nW60KOG_4PfwuHr3MTOCPU693g8T5a2aA9XV2TQD3lV0rkVRmC567s30gCmoq5xkeFmT5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اول تعليق للبرلمان العراقي
زحمة قناة رسمية تثير الفتنة</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87857" target="_blank">📅 19:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87856">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huDrGgN4Gvczpj6-f5V0B9hQJ2YtjUlgUqmpj7ybXSqiMSlybYCtffovgR3KzB7T5FUTjDTmsNua4LY7m7W6egD7oplS9B-2LGhRIEvYnBjjagRGAr5Be4LnH6vlpzqRMAxzRJ5JUJCRjujYr2RlpDFFuAARLvWFcf4IsszSDqr-XcrZLtlmBme2LK_PGQ3-qxMtj6kyB8VkBJzpNhAA3Ih-Zx_wlIQLeQOyH2ueReBh5dAqqA6A9K-qNgP1hBmtP2UOzcPHx8etGz_tL5Hyl9agTIlEcB52tuKgbB15hzGOCwXT1GfnFMyVQI6mxegIfNPKO3ZMTiwwvII_gau7-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: على الرغم من المظهر غير الودود في هذه الصورة بالتحديد، إلا أن هناك العديد من الصور التي نبتسم فيها، وأنا و Kim Jong Un نتفق تمامًا.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87856" target="_blank">📅 19:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87855">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
أعلن المتحدث باسم كتائب سيد الشهداء،
أن الفصائل المسلحة لم تكن وراء الهجوم بالطائرات المسيرة الذي استهدف مدينة أربيل فجر الجمعة.  كما يوجد "شبه اتفاق" لوقف العمليات وتأجيل الرد على الهجمات السعودية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87855" target="_blank">📅 18:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87853">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇾🇪
مدير ميناء المخا اليمني يوقف العمليات بعد هجمات الحوثيين.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87853" target="_blank">📅 18:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87852">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
رئيس مجلس امناء شبكة الاعلام العراقي: تقرر ان تخضع جميع الفواصل الاعلانية اياً كان مصدرها للفحص والمراجعة من قبل الادارة العليا للشبكة ولجان الفحص المختصة فيها.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87852" target="_blank">📅 18:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87851">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇱
مكتب نتن ياهو:
هجوم لحزب الله في "منطقة الأمن" اللبنانية يؤدي إلى إصابة ثلاثة جنود والجيش رد بقصف مقر أصدر أوامر الهجوم ولم نعلم الا لاحقا ان بداخله مدنيين.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87851" target="_blank">📅 18:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87850">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRzCl4aOVJxMu2EaQnzDIpbOvY5p3auF4hpbK1shFU54pfjgZN0m5hDYMIrItMzARrAkTn1OWkgntRK9opTptKQ8RxLRtrcm1BInEGupiM-4eeJY8_4361944HzDJ9NboIG3NNp1Ner_2Sy2JlwZT1h0zp2ytdePuIhbE2PcbJMWR0uREaFGLlUqfD-KVc8nXvGzQZC9kPWOVpA7woY7EaxvX4AWunrnB2j42YN3LODPk1Zq_LMHtVb3aQkNyOcQWXtiPL6IHAbEC40XhTildRR4iyPHz4Ol5nVR1cqoWbkdUzOG0WGeq7pSlTEaCSjgcsOMgB0t4i5CCKSdX8dM7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
رئيس مجلس امناء شبكة الاعلام العراقي:
تقرر ان تخضع جميع الفواصل الاعلانية اياً كان مصدرها للفحص والمراجعة من قبل الادارة العليا للشبكة ولجان الفحص المختصة فيها.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87850" target="_blank">📅 18:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87849">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عشرات الآلاف يقررون التظاهر ليوم غد ايضا احتجاجاً على الدعوات الطائفية في محافظة بابل وسط العراق   المواطنون يطالبون بمحاكمة عدنان الجنابي و شيوخ الفتنة والتحريض .</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87849" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87848">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇶
مصادر خاصة بنايا   حراك برلماني لاستجواب رئيس شبكة الإعلام العراقي تمهيدا لاقالته وذلك لدفعه وترويجه الاقتتالات والحروب الداخلية في العراق .</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87848" target="_blank">📅 17:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87847">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b7ffa1c5.mp4?token=QCdBzcUaLCDVIjF8_taG8ikUBi2F0T0Rh_ZzZWjsz3npRnjr8Z-sdbvzoHSTQYekq5FACQ9grPxdzlVGT1e6h8XfMbGfvGApJdKOe49c5KIXjF8mFfDKPQKTbUrtDMW2PrzZPyNj2kePQgSHe-t5bD-uXCMxxPRIvWK9QvqYnIk9aAuHwZsVPvEm8xS5PXLW7sfHtBEoh-8YNg94gcntgh0u_hqyoc8wq5hDlxV2DjORsxcR1m-R-CjCUA4-qy9PSk_YCQ3DfBUWGeyJ-7yVrnQI6pq0eTH_6PVGozMjHnINnuTPrKKcuyGx_0rO38xMzRRRSCg_N8g7NyakZPtYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b7ffa1c5.mp4?token=QCdBzcUaLCDVIjF8_taG8ikUBi2F0T0Rh_ZzZWjsz3npRnjr8Z-sdbvzoHSTQYekq5FACQ9grPxdzlVGT1e6h8XfMbGfvGApJdKOe49c5KIXjF8mFfDKPQKTbUrtDMW2PrzZPyNj2kePQgSHe-t5bD-uXCMxxPRIvWK9QvqYnIk9aAuHwZsVPvEm8xS5PXLW7sfHtBEoh-8YNg94gcntgh0u_hqyoc8wq5hDlxV2DjORsxcR1m-R-CjCUA4-qy9PSk_YCQ3DfBUWGeyJ-7yVrnQI6pq0eTH_6PVGozMjHnINnuTPrKKcuyGx_0rO38xMzRRRSCg_N8g7NyakZPtYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🔻
الموضوع هو اكبر من المقاومة وسلاحها ، الهدف هو الشيعة وعقيدتهم التي تقف اما المخطط الصهيوني الابستيني ومشاهد ملايين الزوار من الشيعة حول العالم في الأربعينية هي مشاهد مرعبة لأمريكا وإسرائيل ودول الخليج والهدف القضاء على هذه المظاهر لأنها شعلة الحق الوحيدة المتبقية في العالم ..</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87847" target="_blank">📅 17:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87846">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الرئيس التركي: استمرار الهجمات الإسرائيلية على لبنان يشكل مصدر قلق كبير لنا</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/87846" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87845">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سلاح ما نسلم   مثل ابو حميد ما نصير</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/87845" target="_blank">📅 17:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87844">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c189e3c62.mp4?token=HFPTUmGHU54PhH4_l0Rvprtb41L4BHGeH5xQihJvCqZGFu1j49k-uxBF1yLvM44e78xj_gY4UhG38VXmcCDKXJPoahKcqxdJx7MWE1OXLY3yM7jxXZUoyZaNZ07MxaITrVNXzSkHV78VrRxuwnylXz2gbtFlepAnUbfBs7ykclj-fdN8C100KA3t0ujfZaYzYRLvIdG_we-1v_PK42G_iQe3EwNC7a3TcJwwRRCyeVBuy27G_R3q5pYEYCR5tSoaxa3iPBtAA4i6B6RWljnKMVbPx9cPeK6OS18eXIamTErrP70OlAAThwEWmDyqfgoNsbD5vzs4XAhV9wM0seebOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c189e3c62.mp4?token=HFPTUmGHU54PhH4_l0Rvprtb41L4BHGeH5xQihJvCqZGFu1j49k-uxBF1yLvM44e78xj_gY4UhG38VXmcCDKXJPoahKcqxdJx7MWE1OXLY3yM7jxXZUoyZaNZ07MxaITrVNXzSkHV78VrRxuwnylXz2gbtFlepAnUbfBs7ykclj-fdN8C100KA3t0ujfZaYzYRLvIdG_we-1v_PK42G_iQe3EwNC7a3TcJwwRRCyeVBuy27G_R3q5pYEYCR5tSoaxa3iPBtAA4i6B6RWljnKMVbPx9cPeK6OS18eXIamTErrP70OlAAThwEWmDyqfgoNsbD5vzs4XAhV9wM0seebOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشرات الآلاف يقررون التظاهر ليوم غد ايضا احتجاجاً على الدعوات الطائفية في محافظة بابل وسط العراق
المواطنون يطالبون بمحاكمة عدنان الجنابي و شيوخ الفتنة والتحريض .</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87844" target="_blank">📅 17:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87843">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyVJUdg6uv1Ivup652Y80FqohDMY5FSNHZZtNsqgFAYYVi5cmE-y1h4QZROVsB8T8LqmE27NDC-o2B4X8TGsDdb2Hfp4XYgH43n_60M2qpE27xzuf-anaypHnH4majgui84UhkJk2NXGy9YFxA9vmKWkqqaKhdwSwlQaOweGUraZ4EZzpBJ0JVpiCNpT7Mv4uIbr38jckUV0AvXY5ejWa4g47F2H21YgCPMvnbqlP0IIWrnA106JPMYpQvMFcGhJZFb6UE6ikbLwoJnEwzj4qanW4t5p9_oBHteR_WRORHaOviHh7g-hdDMXKWnqimyXep-8t8gr9HP08dAxGCHEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
منصات التتبع:
تواصل أكثر من خمس ناقلات نفط عملاقة عمليات نقل النفط من سفينة إلى أخرى قبالة سواحل الفجيرة، مما يشير إلى أن صادرات النفط الخام من العراق والإمارات والكويت لا تزال تعبر مضيق هرمز. وتدفع بعض السفن رسوم العبور الإيرانية، بينما لا تدفعها الأغلبية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/87843" target="_blank">📅 17:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87842">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb7dc434c.mp4?token=g0Pjm4Tc58bQX2qQtLKMM0DXONrRiNz7lUvj9KH4jxWn_pZeSMLVk1dID18kvwsyFkHfF8zkibQ5KYK7Je47BAKiGsHaNwR-c4uM8B-kFaE68QAwT8pza_I0kBnil8qzlpyFO82t3QKH9VtibQstR6r7Y138O69pmsqM9I_9q4GA5geCY1_xUk7iHoWmdwD5Hr09bWy2h7qQoS9uuz8uR0KLPYhtQnBNfOuZ5c3k4aDu_ZqRhwCr9Mb-CjHggwkOCI0g64PpN7UQR7zzHe9c7R_0rGBj3Dpu2ozlnfNDY-hcuXfZnt0RVUhCUn-UNcGEeci7T5lNjevRf2bj_myZKKylRpnw29EsilUIjAS1dcJ6_BXAZ8tkZuF-I6Y6p7rXc5W1RZ5c5iATWK0f-S1p1tfbGgrW81lFdfNTsTbfq7IIOmS7YCjWYFnSMW5hsEj9PpADePC3fr2TwE8sE3dzGihTHdfCBxXyKUrWonn7rRYpO7_XDAnTmQMFsWJFIdBTbEmoRkO9kBs04PsVaomjEjrzE_XRR89msj18S4sSEd3KHvc80_zmXRyfcholYrTV89djpBkyjZzbhpOaEe8Rjk_tFoaffPqwLYrhhN6NKaW9FNWGGJMMPuXjmJD4j0bLySX1Mx7PTTJdAzI7COcdL-HKH58hx-fyRUQ9ggRgs1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb7dc434c.mp4?token=g0Pjm4Tc58bQX2qQtLKMM0DXONrRiNz7lUvj9KH4jxWn_pZeSMLVk1dID18kvwsyFkHfF8zkibQ5KYK7Je47BAKiGsHaNwR-c4uM8B-kFaE68QAwT8pza_I0kBnil8qzlpyFO82t3QKH9VtibQstR6r7Y138O69pmsqM9I_9q4GA5geCY1_xUk7iHoWmdwD5Hr09bWy2h7qQoS9uuz8uR0KLPYhtQnBNfOuZ5c3k4aDu_ZqRhwCr9Mb-CjHggwkOCI0g64PpN7UQR7zzHe9c7R_0rGBj3Dpu2ozlnfNDY-hcuXfZnt0RVUhCUn-UNcGEeci7T5lNjevRf2bj_myZKKylRpnw29EsilUIjAS1dcJ6_BXAZ8tkZuF-I6Y6p7rXc5W1RZ5c5iATWK0f-S1p1tfbGgrW81lFdfNTsTbfq7IIOmS7YCjWYFnSMW5hsEj9PpADePC3fr2TwE8sE3dzGihTHdfCBxXyKUrWonn7rRYpO7_XDAnTmQMFsWJFIdBTbEmoRkO9kBs04PsVaomjEjrzE_XRR89msj18S4sSEd3KHvc80_zmXRyfcholYrTV89djpBkyjZzbhpOaEe8Rjk_tFoaffPqwLYrhhN6NKaW9FNWGGJMMPuXjmJD4j0bLySX1Mx7PTTJdAzI7COcdL-HKH58hx-fyRUQ9ggRgs1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توافد حاشد لموقع التظاهرة في محافظة بابل</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/87842" target="_blank">📅 17:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87841">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">المتحدث باسم الخارجية الايرانية بقائي: لقد تم التوصل إلى اتفاق بشأن خريطة حركة الملاحة بين ايران وسلطنة عمان</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87841" target="_blank">📅 16:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87840">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da068288c4.mp4?token=UZrr2Go-jUnRVxOReWhG4QlrdLdELCVltk0AwQJt13CAxirOzKbU0D2c7C7KzsCIsZMygX778thdK4NdDs09UcWW4FXm0GXja_iOx5qzjd_jvA_Gn58ztNHBfdjCa-ZfsgDhWnD8lkNTAUid0DNISM_kid5lhp1nwR45yVdW5U7XV57mhcJn7jvm-i4X-VNq3x97tCn1HVb7v-exAjR1VM-D9ydhdan-rmzvlv1gKX2fJVSAXmQ08L-44EiJwqN-mMNR37wUlsSFovzq6LntIG2ZqZi66OzHV7oynNc5bYJttFirTVSDCBprbnXq2N7rJgwJXEbLqYuyPznIuYv66Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da068288c4.mp4?token=UZrr2Go-jUnRVxOReWhG4QlrdLdELCVltk0AwQJt13CAxirOzKbU0D2c7C7KzsCIsZMygX778thdK4NdDs09UcWW4FXm0GXja_iOx5qzjd_jvA_Gn58ztNHBfdjCa-ZfsgDhWnD8lkNTAUid0DNISM_kid5lhp1nwR45yVdW5U7XV57mhcJn7jvm-i4X-VNq3x97tCn1HVb7v-exAjR1VM-D9ydhdan-rmzvlv1gKX2fJVSAXmQ08L-44EiJwqN-mMNR37wUlsSFovzq6LntIG2ZqZi66OzHV7oynNc5bYJttFirTVSDCBprbnXq2N7rJgwJXEbLqYuyPznIuYv66Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلاح ما نسلم
مثل ابو حميد ما نصير</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87840" target="_blank">📅 16:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87839">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d027dce5.mp4?token=O_7tyolrFmdWZcyRDl1MkHtHxCQ9flF5jwY1w9wDtUqMJENv6C6bji_M4v9XUkAJL8a1-IJ1DzUmj2zWW5QS1_j1RZjDt0rkM2o_m266xgZDD7WXv1HnbCcl8IQymT7JX3e79Ak78VRIeTa-r7uINBMP_0UPlQVIPp1iMHUKmA-D7HnItQzYJMdNDyrb1pYWT1kukVlnGJWZtS4qCCjgUwopADXCSoNqpV-I96ADeyguP2mcu4Np1hEdrm66EKg3Gj7XefepLA0d3bgahkdUlHJKEcwtQZqvI3YxWknsgeOD263Mz_McK3INmRP8JqejyhaMwikpB-mJa8un4VEYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d027dce5.mp4?token=O_7tyolrFmdWZcyRDl1MkHtHxCQ9flF5jwY1w9wDtUqMJENv6C6bji_M4v9XUkAJL8a1-IJ1DzUmj2zWW5QS1_j1RZjDt0rkM2o_m266xgZDD7WXv1HnbCcl8IQymT7JX3e79Ak78VRIeTa-r7uINBMP_0UPlQVIPp1iMHUKmA-D7HnItQzYJMdNDyrb1pYWT1kukVlnGJWZtS4qCCjgUwopADXCSoNqpV-I96ADeyguP2mcu4Np1hEdrm66EKg3Gj7XefepLA0d3bgahkdUlHJKEcwtQZqvI3YxWknsgeOD263Mz_McK3INmRP8JqejyhaMwikpB-mJa8un4VEYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطنين يتوافدون الى موقع الوقفة الجماهيرية في محافظة بابل لادانة عودة الارهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87839" target="_blank">📅 16:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87838">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏وزارة الخارجية الروسية: شحنات الأسلحة الأمريكية التركية المحتملة إلى كييف ستضر بعلاقات موسكو مع واشنطن وأنقرة، طلبنا من واشنطن وأنقرة توضيحات بشأن مزاعم وجود خطط لتزويد كييف بالأسلحة</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87838" target="_blank">📅 16:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87837">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بدأ وقفة جماهيرية في محافظة بابل للتأكيد على رفض عودة الإرهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87837" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87836">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
اللواء 52 بالحشد الشعبي يتسلم قاطع بسطاملي في آمرلي من الجيش ضمن تنظيم توزيع القطاعات والمسؤوليات الأمنية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/87836" target="_blank">📅 16:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87835">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa80e2a4e.mp4?token=Qoi8nY5ElJMSPQGks95S9C9JdUbNhkYfh4Ae2LiHNA-mDRZOGHj_rHKoZFTyydBrlOtPkPpPD1b5hL2grC2C0kr29WWza4cchyW8cXqsQ8lGbYYI3SO3gMUUR0l6gcOnWeqGj2DGNtYWA2ZXa2iM5oOVpUzagrhCINkuvJP7T1y1fFb2V8vXXHa0DrzrTg590r-tOSsgmQCUieJA8HQQR4dstZ2ESFujCdf8lO5R4qI_3kWrb21fCzm439lgJQbmuLiPr8LOw1mCeMM9UpgI6X3N3erTsmQ9_f1L6nVE-UsIn90Hr18NeC7wf9kTOpHyd7ddtXrJOntb5sE8DvcxrZBLSNmAbBen60E0fo12_0V-jFCrq202tqvVzBjeNntvOOWj0AxgXWVxWfNdBVGZOYM_7KDsHxDipw0aNAKi0faBoavZBDIwy4UHumRpXdxxamZcOH3ozH6QLPaA3uoRzA3biKzC7ODZwrjDhxxHcr56J1v5rDb5tYA0xPjtVuMediGuRvIripjsEafEujnompKIseuEUGN4hC-_2BpZUXyjWX4cpv0c73YPZ-dw-T8JWbhMZNuukePQDzF5xU1Lol5VFVSOfYIgzI7UTN4XCVg4z0oBGFwOfvJ3sGgT-i5Z3pMyEO-5Icw8WICCms8Pnmy_XtRqKu4V7kOu7toi0wo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa80e2a4e.mp4?token=Qoi8nY5ElJMSPQGks95S9C9JdUbNhkYfh4Ae2LiHNA-mDRZOGHj_rHKoZFTyydBrlOtPkPpPD1b5hL2grC2C0kr29WWza4cchyW8cXqsQ8lGbYYI3SO3gMUUR0l6gcOnWeqGj2DGNtYWA2ZXa2iM5oOVpUzagrhCINkuvJP7T1y1fFb2V8vXXHa0DrzrTg590r-tOSsgmQCUieJA8HQQR4dstZ2ESFujCdf8lO5R4qI_3kWrb21fCzm439lgJQbmuLiPr8LOw1mCeMM9UpgI6X3N3erTsmQ9_f1L6nVE-UsIn90Hr18NeC7wf9kTOpHyd7ddtXrJOntb5sE8DvcxrZBLSNmAbBen60E0fo12_0V-jFCrq202tqvVzBjeNntvOOWj0AxgXWVxWfNdBVGZOYM_7KDsHxDipw0aNAKi0faBoavZBDIwy4UHumRpXdxxamZcOH3ozH6QLPaA3uoRzA3biKzC7ODZwrjDhxxHcr56J1v5rDb5tYA0xPjtVuMediGuRvIripjsEafEujnompKIseuEUGN4hC-_2BpZUXyjWX4cpv0c73YPZ-dw-T8JWbhMZNuukePQDzF5xU1Lol5VFVSOfYIgzI7UTN4XCVg4z0oBGFwOfvJ3sGgT-i5Z3pMyEO-5Icw8WICCms8Pnmy_XtRqKu4V7kOu7toi0wo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام امريكي: المنفذ ليس واحد بل عدة مسلحين</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/87835" target="_blank">📅 16:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87834">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxSwK-rYwOBgjBfnvQe-93nAiL6EM6jQaXszOzFrNi3gzTKht5w9jopn0IZ1Q-AJgnLFZdiDPRk8tVc8EXCzDifoL4hH5ufbyvHgD4kPEHuHeDMstu6SAaU--5zWNOCNTKwHN3phdsJQrLnCapSFc__qiSSALAbKXEMfcBTlcxr0lf0tZGE_obVw0BEvYtDQ-B_SusbryA8v4GQHLhrfOzP89iLM3skj12eZXhXsI6yt6w5TRuOnSvE7MDqHyRB5E1ytEBWk44LktsPSNqc9o0BWdNzGyUk0mqWYFMe9ouW5zo3-CZTUawJcc1HYZCsxfxkQP-vHkktIjOLvFFLmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مصادر لنايا
شبكة الإعلام العراقي بصدد انتاج الجزء الثاني عن تسليم السلاح لكن شخصية حميد ستصبح كاكا حمه في اشارة لسلاح مليشيات البيشمرگة ..</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87834" target="_blank">📅 16:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87833">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اغلاق جامعة ولاية فرجينيا بعد الهجوم المسلح</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/87833" target="_blank">📅 16:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87832">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اطلاق نار داخل جامعة فرجينيا ومقتل واصابة عدة اشخاص كحصيلة اولية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87832" target="_blank">📅 16:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87831">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حدث امني في ولاية فرجينيا الأميركية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87831" target="_blank">📅 16:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87830">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حدث امني في ولاية فرجينيا الأميركية</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87830" target="_blank">📅 16:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87829">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
بيان صادر عن حزب الله:
استيقظ اللبنانيون فجر اليوم على وقع تصعيد عدواني ومجزرة وحشية ارتكبها العدو الصهيوني المجرم بحق المدنيين الآمنين في الجنوب، من خلال استهداف منزل في أطراف بلدة أنصار الجنوبية ومبنى في دير الزهراني، ما أدى إلى ارتقاء إحدى عشر شهيدًا من بينهم أطفال ونساء وسقوط اثني عشر جريحًا، في جريمة موصوفة تضاف إلى سجل العدو الحافل بالمجازر والجرائم وسفك دماء اللبنانيين وتفجير منازلهم وجرف حقولهم ومحو معالم قراهم.
إن هذا التصعيد الإسرائيلي، باستهداف المدنيين وتوسيع دائرة المناطق المستهدفة، يعبر عن رغبة وإرادة رئيس وزراء العدو المجرم نتنياهو  بتصعيد الحرب تعزيزاً لواقعه السياسي الداخلي، وخدمة لأهدافه الانتخابية وإرضاءً لليمين المتطرف. وإن هذا التمادي في العدوان وانتهاك سيادة لبنان تتحمل مسؤوليته حكومة العدو  والولايات المتحدة التي تؤمن الدعم والغطاء لها، فيما يجب على  السلطة اللبنانية أن تبحث عن السبل المتاحة لوقف هذا العدوان وأن لا تصر على الاستمرار في مسار المفاوضات المباشرة المذلة وتقديم الهدايا المجانية للعدو، رغم كل ما يرتكبه من جرائم واعتداءات، وما يعلنه من نوايا عدوانية وتوسعية تجاه لبنان.
لقد آن للسلطة أن تراجع حساباتها مراجعة شاملة بما يحفظ سيادة لبنان وحقوقه، بدل الاستمرار في سياسات تأكّد عجزها عن حماية لبنان وشعبه، وأن تقف موقفًا وطنيًا وشجاعًا ومسؤولًا، وأن تتوقف عن اللهاث خلف المفاوضات التي يجرّها إليها الأميركي، وأن تدرك أن الرهان على الضمانة والوساطة الأميركية هو رهان خائب، فالأميركي شريك للعدو الإسرائيلي في جرائمه ومجازره بحق لبنان. وما التصريح الأخير والوقح والابتزازي للسفير الأميركي في لبنان الذي دعا فيه إلى تسليم سلاح المقاومة، فيما المطلوب منه أن يضغط على العدو الإسرائيلي للانسحاب من المناطق التي يحتلها، إلا تأكيد على أن ما يبحث عنه الأميركي هو مصلحة العدو الإسرائيلي وأمنه على حساب سيادة لبنان وشعبه.
إن على اللبنانيين جميعًا، بكل مكوناتهم، أن يدركوا خطورة النهج الذي تنتهجه هذه السلطة على لبنان ووحدته وأمنه واستقلاله. وإن على العدو الإسرائيلي أن يفهم جيدًا أن اعتداءاته وتجاوزاته ومحاولاته فرض أمر واقع لا يمكن أن تستمر، وستقابل بما يناسبها، دفاعًا عن لبنان وشعبه وسيادته وكرامته الوطنية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87829" target="_blank">📅 16:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87828">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX78VDFaS_hykjcjZNBdZJ2Ri62S2Eq7M08ubXLLMVed_Dz4HkUI95jzSxqUneGd6aYc8vpWJr5PpMTI5pKl6a_We-_7vfQpM1dEbOQKYS7P29ggA1Xq0vmuUP2KAWCVYoEMsf7y5fe3jztHy3e5aXoLSsCTYJnrxpneGhqN_5uPiXQkGRuURTtKiFMeAnuc7-yL7qStquYaszFeqpHFrTC77TM2ctrC1TAOOKWJbMKaLxs_jRDUd_PpSlsMwxajeW0AGas67fD7jhdICHN7AVUl-Hpp18wYxsx4z0rFzdkJYvlvkdCElpv7NoIfRW7Y4Vr2-5vq1mOBaf78f6-tzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشوراء الفرقة الخاصة
نار على أعداء العراق</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87828" target="_blank">📅 15:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87827">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بدأ وقفة جماهيرية في محافظة بابل للتأكيد على رفض عودة الإرهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87827" target="_blank">📅 15:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87826">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLQzhhAV-7LULPFn97kq2S8qcs8gyyP9w23aKOSc-7tFvJ_iX7a_afFA8hcf6cJPOvhJmZXTcug1XdDy3bz-ePBdpK9038zz1X-NZ_DU1pe4Hzn7Gwz7ZtfJh6uNwLCuCWyqgDOWtTns0J_gSfBoy5TuzMSd8TdFpifyIHl07TKuCa5lxKlxYQ63_BFvO6jBnWglAkcVbDgtcBGavYPh4mQIR7mRfWGdG1hFcJ1op1g_gcI_2QbJu0h_TaVkuOl2bLM2Xz0jHeY_hsxpv-I-_PbPhoZ0Zc8p-lDKMYwAuht95OpVWW9JYcbvgiQI0DZdsdGX8bP2wBW1C16i4MfI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لولا دماء بلال الوحيلي و شيخ ياسر عاتي الكعبي
لكانت الجرف الان ولاية ارهابية داعشية سلفية ..
شكرا حميد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87826" target="_blank">📅 15:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87825">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏قصف مدفعي متبادل بين مرتزقة السعودية وانصار الله على جبهة كرش شمالي لحج</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87825" target="_blank">📅 15:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87824">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">زلزال بقوة 6.9 درجة يضرب إندونيسيا، وهو الثاني في يوم واحد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87824" target="_blank">📅 14:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87823">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
الامريكيين ينتجون فيديوهات دعائية بعد ساعات من تداول اخبار عن تعطل مراحيض حاملة الطائرات الأمريكية "لينكولن" واضطرار البحارة للسير في مياه الصرف الصحي على متنها وكيف كانوا يحصلون على طعام رديء. كل هذا دفع البعض إلى القفز من السفينة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87823" target="_blank">📅 14:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87822">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">السفير التركي في سوريا: اردوغان مغرم بدمشق وسيزور سوريا نهاية العام ومتشوق للصلاة في الجامع الأموي</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87822" target="_blank">📅 14:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87821">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
الإعلام الأمني العراقي:
الحشد الشعبي جزء من القوات المسلحة وحصر السلاح يشمل الجهات غير المرتبطة بالمؤسسات الأمنية</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87821" target="_blank">📅 14:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87820">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: تمكنت القوات المسلحة _بفضل الله_ من استهداف تحشيدات وأسلحة تابعة  للعدو السعودي وزوارق حربية تابعة لأدواته ومرتزقته في منطقة المخا، وذلك بعدد كبير من الصواريخ  البالستية وكانت الإصابة دقيقة بفضل الله وقد أدت العملية إلى تدمير الزوارق…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87820" target="_blank">📅 13:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87819">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roeWsZJkOEJbka4BS0DyCohzhQiVvHlXyRVSFBaPp3mQ6qnV-z-oHK-t76O9CuhdWxqTtmdQd9zpf-IIwt3JfPA-koy2MffcPP021ZgYhT9XWbTPO5n1FaLyts23MKPzkyRMnIIGCTyKzzlN0ya3tFBoEA601JYoNnLZA8JBKDCekLn1e9gW4GZPIu9iOI39xKntEcgJOJKcMEqaOqeAaHkixh8IuhvWPxotoXmXeALDRzEdrNbhU4L8qwZ4hAuJZYylEaBHX1wZ0ddX-NXcF1uGk1_kE1-burln_3sUin6NmnXyLpqj8Lksr05bT1GXKbsHHIs-a_3WCG0ICj2I-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مراقبون لنايا
تحويل الإعلام الرسمي إلى منصة تهديد ليس هيبة دولة بل عبث بالسلم الأهلي .. إذا كان المطلوب تطبيق القانون، فليُطبّق بالقانون لا بالوعيد من شاشة الدولة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87819" target="_blank">📅 12:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87818">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-ixGvD_6WmNBeiYTO9KfIcG_Del_74QFnTDo5HYUUjntA8339p4VihXdd_5_TSRmPUB_P7uF2SsH2jWhex5Hrft6KMkuIIxUNTjxQfn55-EA3yrwIPKPJTeKXL06uWVKZb1IIH_AI9RrlKO-Bn0mcN2ATCDQEMROEgNDMwpdxE_WmAhk0TcOXIraaMaKwFlW_TxeNcIgtVP_Uxlv_YdAVBBWPqvnQkQONCBKBw6cgn4BBGwuqAjeO1xQngzQjSFEGgKDa6Xm14SuUuE9efLosUAktB4DwEU2g4GDpH_k_pW3IYw_EUz4sPK_kvmld-yaw0EJzjAORYqGVnCCwVWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
🇮🇱
إلى أنظار جوزف عون و نواف سلام..
عائلة كاملة إرتقت فجر اليوم جراء عدوان صهيوني غاشم على بلدة أنصار جنوبي لبنان.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87818" target="_blank">📅 12:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87817">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4aa482a54.mp4?token=QeQotM5usC_GCP9CQ_mEC3XJ9UjU9PnG_aO_i53eB0BRwZ9m-NO1GhOYYDNm9s9ChqXnZ8ucZEmOdzSJ5oem6N7_WJpyVDuRiLz2A6eqV5ZhenizjTMFj92i5pTspNoI__s7BjovRtPqBdFfwyVCwhnYxLWTBucl_mttE8XHkhfeV1Evvq9qTaAgOexNRQsnlrCEpFQ-q-r1mBoOkzGjj53QFOukb5aZftNwtZw3SaCEtRf7UgI2Y6RghHQlwM7OaJahmBhb0IU0W4JTpLT4GGwLMg9uoxHjU6ajKyo3Y9EfWVhDdfm85jA4BuCNoG3OEdzq_ZkkRWLvuxomJPtjlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4aa482a54.mp4?token=QeQotM5usC_GCP9CQ_mEC3XJ9UjU9PnG_aO_i53eB0BRwZ9m-NO1GhOYYDNm9s9ChqXnZ8ucZEmOdzSJ5oem6N7_WJpyVDuRiLz2A6eqV5ZhenizjTMFj92i5pTspNoI__s7BjovRtPqBdFfwyVCwhnYxLWTBucl_mttE8XHkhfeV1Evvq9qTaAgOexNRQsnlrCEpFQ-q-r1mBoOkzGjj53QFOukb5aZftNwtZw3SaCEtRf7UgI2Y6RghHQlwM7OaJahmBhb0IU0W4JTpLT4GGwLMg9uoxHjU6ajKyo3Y9EfWVhDdfm85jA4BuCNoG3OEdzq_ZkkRWLvuxomJPtjlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇮🇱
إرتقاء شهداء وعدة إصابات جراء غارة وحشية من الطيران الصهيوني على منطقة مأهولة بالسكان في بلدة دير الزهراني جنوبي لبنان.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87817" target="_blank">📅 12:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87815">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
رئيس السلطة القضائية الإيرانية:
لقد أثبتنا لترامب وتابعيه في الساحة العسكرية أن مضيق هرمز جزء لا يتجزأ من المياه الإقليمية والحدود الإيرانية، وأن أي مغامرة فيه ستقضي على أي قوة متجاوزة ومغامرة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87815" target="_blank">📅 11:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87814">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عدوان سعودي على محافظة صعدة اليمنية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87814" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87813">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7000ddea94.mp4?token=WRxd_X4Qket1lmea07APlO9oB_0DbspvEa1GDvul5qtlwxyt083Ixl4d15n-dfzZNu-o6O292ec2P6vfRLBjBsC6LWQd_es9rKN4qYXzwHlXN4LDm46-fpFjG1QonOOKdR1lTrBsg7ahPai5Q2z0DDyiF2UAO6Xji2YZrWhK4HJP7zsbXvNS6E1026PaWOCYWjEKgOYaz5gM9maVudfG6oiBsPk96nKBCp3qZ8G-KzsceSm9DrPB4TPBykly51iFYbHM-hmJBgEbleCCW4Nb_W2DziMgeL7l8AYvXnncJI6eNIMP5au5zZSrrVf9Tm50COhTBEXNFfQuJrmO0Qw_oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7000ddea94.mp4?token=WRxd_X4Qket1lmea07APlO9oB_0DbspvEa1GDvul5qtlwxyt083Ixl4d15n-dfzZNu-o6O292ec2P6vfRLBjBsC6LWQd_es9rKN4qYXzwHlXN4LDm46-fpFjG1QonOOKdR1lTrBsg7ahPai5Q2z0DDyiF2UAO6Xji2YZrWhK4HJP7zsbXvNS6E1026PaWOCYWjEKgOYaz5gM9maVudfG6oiBsPk96nKBCp3qZ8G-KzsceSm9DrPB4TPBykly51iFYbHM-hmJBgEbleCCW4Nb_W2DziMgeL7l8AYvXnncJI6eNIMP5au5zZSrrVf9Tm50COhTBEXNFfQuJrmO0Qw_oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مروحي يحلق بإستمرار في سماء محافظتي أربيل والسليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87813" target="_blank">📅 10:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87812">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نيويورك تايمز:
هاجمت إيران في بداية الحرب القاعدة البحرية الأمريكية في البحرين، مما أدى إلى تعطيل مركز لوجستي رئيسي، وأجبر البحرية الأمريكية على الحصول على الإمدادات من جزيرة دييغو غارسيا، التي تبعد حوالي 3500 كيلومتر عن حاملات الطائرات العاملة بالقرب من إيران.
ساهمت مسار الإمداد الأطول في حدوث نقص وضغوط على متن السفينة الحربية الأمريكية "أبراهام لينكولن"، حيث قضى طاقمها المكون من 5000 بحار ما يقرب من تسعة أشهر في البحر دون توقف في أي ميناء.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87812" target="_blank">📅 10:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87811">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇶
🇺🇸
القناة الحكومية العراقية تهدد فصائل المقاومة العراقية   نشرت قناة العراقية الممولة من الحكومة العراقية فديو دعائي لاول مرة منذ عام ٢٠٠٣ تضمن لغة تهديد للفصائل المسلحة بالتزامن مع نهاية المهلة التي اطلقها توم بارك بخروج المزعوم للقوات الأميركية في العراق…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87811" target="_blank">📅 10:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87810">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX1uticxx9ni670T5fqK1uaDe5CoOhKg1BLqqTuQoT4roW_FVA6-gL6aGod-siBZfz62aARqs1IzIcnLJBQCHlXrlwF-eQMRT5iVJX54HpjbTD0kk37X4MvO0fNDsOHDzGs7h3z-K7-Z221J3ZmYtjCx1b32vu9JPfXVpZi1aUEWBGHNCTVq-Sj0tJmMwqXu8O3QFCidlGkqY33CX85ljafDxPEkgQ9yh6YvWX1GWwceBP_nn_0n5AplbsyKjMvDWAYFN92MT6BatqXhMlnSeoNvvp7ANNxSMOd0kQukeBRwMRtVQlPcX41x9uf_xJ-rxkv8SkAMF-iUfdyRtgyH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇺🇸
القناة الحكومية العراقية تهدد فصائل المقاومة العراقية
نشرت قناة العراقية الممولة من الحكومة العراقية فديو دعائي لاول مرة منذ عام ٢٠٠٣ تضمن لغة تهديد للفصائل المسلحة بالتزامن مع نهاية المهلة التي اطلقها توم بارك بخروج المزعوم للقوات الأميركية في العراق ومهلة الحكومة العراقية ايضا للفصائل بنزع السلاح ؛ المضحك ان القناة الحكومية استخدمت في الفديو طائرة MG 29 الروسية والتي تخضع للعقوبات وتفرض امريكا على العراق قرار بعدم اعادة تأهليها مع ٣٥٠ طائرة اخرى روسية الصنع تحولت لكتلة حديد بمطار التاجي بسبب الوصاية الأمريكية على العراق</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87810" target="_blank">📅 10:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87809">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMUswe8zVGQUuQu5vl6hPfnI8Eokb4cxxEy8pzZfAHOsiBT__0IrHGBDgqGjQEJzokIh5WOAGw75C-o9xwa5CZiXhbfgoDbYtZJzBRglSS5chRPslrt2wfF3QLY76QlYdiS3Qa4FYcf0mEziFqgAnmV1aKv5zftMwNZ6xG4SIb2wPhIbOE8-1IQYkMUDNQImzYBITu3xOGr-fl4UhoKDhSUA5P9NgwhzP7y3x49fyOwd9KA7QVtx0l2UGq8bxmTn8oT4Ae2Z3yYTXRLj6lKv-2z0c_1oOYPvvsRupU8Ylik-JJWPVuCeAGRYiBjVdCtXzwr2K4IH5dhhqmlpYTqaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87809" target="_blank">📅 09:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87808">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87808" target="_blank">📅 09:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87807">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
القائم بأعمال وزير البحرية الأمريكي:
عالجنا عددا من حالات الصحة النفسية على الحاملة لينكولن.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/87807" target="_blank">📅 01:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87806">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579ffff276.mp4?token=XWuCypXzzh724fBLQ-X0kfbfCxJ65S3nhuRh6HoFZ7scyElPAtPNSGCvCbOabPh7o6IaTsKTdSh6iwMFLwa3Wf8e8UGjBTGLuqHd7Ins5MdwOQjvbjGiTynqrQLGQJtHH4Qoc0G8jIKgeYhk_CKU3ud_22ITxUAfcCdWJno22CTYZrVO71JIfn3VSLW94eDrvrsdugmqTL5wzrxX_IJrmWet0eCz1CyYE2n_bZH_Np4iRvPPizEolRhEkydI0sPKeRdouraStWsQ4wTl92b3nP4q8JvIzLbvCGWySRnGtxnzqmP2fwrwTNn0VKZn0YUpEdqKv7zoIWZkDKgdVNXf-VKi6lLAmhZ6f7O5a3XW-A_Xkdz1d8Fx_c8nh6IT2xRowFAdnVV1nWG8UMdQpoLPBImnQrv1kFKbScrIF0fvK6RoKKW6sgC1G0dYdR9jffISBi-5gcDFetc-4iz0-wITTHSeq82r5F53eeiIUoq1XECC1A_S2rH-wBAyYt8Y7o-MR9TObp3Jd4z_WxazesVSWDX7ILYwX6CfnZhT3r85LjSFXGfM09nMzqnip4bXGxy2NfW6Y7-HqkzMYQMw6iuYcOEy_hjZGHkiLOa8PcGaz6d9bixCQzI99-h2CxBUXRI9G8X0EfqoBmxJwPHnZErKxup7UU_5IWTKFQXzCsmNDm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579ffff276.mp4?token=XWuCypXzzh724fBLQ-X0kfbfCxJ65S3nhuRh6HoFZ7scyElPAtPNSGCvCbOabPh7o6IaTsKTdSh6iwMFLwa3Wf8e8UGjBTGLuqHd7Ins5MdwOQjvbjGiTynqrQLGQJtHH4Qoc0G8jIKgeYhk_CKU3ud_22ITxUAfcCdWJno22CTYZrVO71JIfn3VSLW94eDrvrsdugmqTL5wzrxX_IJrmWet0eCz1CyYE2n_bZH_Np4iRvPPizEolRhEkydI0sPKeRdouraStWsQ4wTl92b3nP4q8JvIzLbvCGWySRnGtxnzqmP2fwrwTNn0VKZn0YUpEdqKv7zoIWZkDKgdVNXf-VKi6lLAmhZ6f7O5a3XW-A_Xkdz1d8Fx_c8nh6IT2xRowFAdnVV1nWG8UMdQpoLPBImnQrv1kFKbScrIF0fvK6RoKKW6sgC1G0dYdR9jffISBi-5gcDFetc-4iz0-wITTHSeq82r5F53eeiIUoq1XECC1A_S2rH-wBAyYt8Y7o-MR9TObp3Jd4z_WxazesVSWDX7ILYwX6CfnZhT3r85LjSFXGfM09nMzqnip4bXGxy2NfW6Y7-HqkzMYQMw6iuYcOEy_hjZGHkiLOa8PcGaz6d9bixCQzI99-h2CxBUXRI9G8X0EfqoBmxJwPHnZErKxup7UU_5IWTKFQXzCsmNDm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب عن إيران: كان لديهم 212 طائرة جميلة جدًا، بعضها تم شراؤها من الولايات المتحدة، وبشكل ذكي، في عهد أوباما. جميع طائراتهم اختفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/87806" target="_blank">📅 23:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87805">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6da41714.mp4?token=p7_154eaAXQOa9z-gNEAd54LcYpBW22w4g-2exjcG8uPlAI1QUyxuEkfAqSv7qRlXVNHeg6pVTc8CQTmH9Nx6I0mrWop9av-PXvkc8m61PIo2mWZr89KJwoaMhjLnfj1gqD9QpgKC2regmDidpQKrhP6b1bF9E2pqKYla3N4b6pBfPhsNRhIZIgd2PZsp8KVtqp55fdoD8EtTO9Z-ep1OmRT7-R9dzODSMvj6mItPODhIiEuoj1Yrbu9kwtYWzJnBezTUbR-1pZ6DMHJTdJrDUlwdyR3X_fF3q9IRmWM2Cl6eVsTDt3OK5UacMcJ1VYsMBVteEQ1YzjfpKr7MHhnkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6da41714.mp4?token=p7_154eaAXQOa9z-gNEAd54LcYpBW22w4g-2exjcG8uPlAI1QUyxuEkfAqSv7qRlXVNHeg6pVTc8CQTmH9Nx6I0mrWop9av-PXvkc8m61PIo2mWZr89KJwoaMhjLnfj1gqD9QpgKC2regmDidpQKrhP6b1bF9E2pqKYla3N4b6pBfPhsNRhIZIgd2PZsp8KVtqp55fdoD8EtTO9Z-ep1OmRT7-R9dzODSMvj6mItPODhIiEuoj1Yrbu9kwtYWzJnBezTUbR-1pZ6DMHJTdJrDUlwdyR3X_fF3q9IRmWM2Cl6eVsTDt3OK5UacMcJ1VYsMBVteEQ1YzjfpKr7MHhnkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/87805" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87804">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
الوضع بين الولايات المتحدة وإيران مستقر.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87804" target="_blank">📅 23:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87803">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/87803" target="_blank">📅 23:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87802">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba96a06df0.mp4?token=M5P0fRWwEq80Qozd77taeeIbJWQbfnlXAu-CLm0zBBWOkV73FDHqB1fYKDX8hlk_0D8gW9LYJuhpLr94-JuqRiAzmvRFkwpQMsgMAmmSP8vnxxlQUVRNY1nHj_B91vi3L6cvpBttjVcFK_xdcZo4QnARBjTozC-gmaFTWdAh_TcUIQrZN5tssEeEYp7CvmNnrLp8AM7eD0veYlVD8nL1Z3dp2LKDSkDuSfIXXlsIeklz4qiV7qQYNzCdSxaI7lQ5xZgCnlNgvSiySdtVUzXrsoambaUInzfGxvIkjpqhDXBwJI7WZF3TG0SH1_s0L2rJohGOhUlB80Y1ENpfBkjz5ClJDrhNuqP4mHqN4eFpvYxj-oB4mRWt8vbp-9QEme0ZlNBnJCHRP975C3vn-XoNVdYw8cqlgp-KObwUIRQRImzoyrynxdvBDmOV_6IRxGl-bqOejMGePgFlzkEBHBYC2Y_On-KmbzuJfLtCB1FyoKPmUYN5PYiGagJp9IC3DHuStQrHvuwX39fpkHGt4TBNz0ay6VdwfErsx3VpvoI92RPd_kubHsRSJfjtfsfOV6VYrVvR6spDth38X9C4B3bZtFsJE_gBFRUFngNDqojZfApyLTWN8DCsKI7kXCIMALL1CvMyRVDCeIVhvjmtcchg83bCWnpijUVezYPstTbADw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba96a06df0.mp4?token=M5P0fRWwEq80Qozd77taeeIbJWQbfnlXAu-CLm0zBBWOkV73FDHqB1fYKDX8hlk_0D8gW9LYJuhpLr94-JuqRiAzmvRFkwpQMsgMAmmSP8vnxxlQUVRNY1nHj_B91vi3L6cvpBttjVcFK_xdcZo4QnARBjTozC-gmaFTWdAh_TcUIQrZN5tssEeEYp7CvmNnrLp8AM7eD0veYlVD8nL1Z3dp2LKDSkDuSfIXXlsIeklz4qiV7qQYNzCdSxaI7lQ5xZgCnlNgvSiySdtVUzXrsoambaUInzfGxvIkjpqhDXBwJI7WZF3TG0SH1_s0L2rJohGOhUlB80Y1ENpfBkjz5ClJDrhNuqP4mHqN4eFpvYxj-oB4mRWt8vbp-9QEme0ZlNBnJCHRP975C3vn-XoNVdYw8cqlgp-KObwUIRQRImzoyrynxdvBDmOV_6IRxGl-bqOejMGePgFlzkEBHBYC2Y_On-KmbzuJfLtCB1FyoKPmUYN5PYiGagJp9IC3DHuStQrHvuwX39fpkHGt4TBNz0ay6VdwfErsx3VpvoI92RPd_kubHsRSJfjtfsfOV6VYrVvR6spDth38X9C4B3bZtFsJE_gBFRUFngNDqojZfApyLTWN8DCsKI7kXCIMALL1CvMyRVDCeIVhvjmtcchg83bCWnpijUVezYPstTbADw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران
: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/87802" target="_blank">📅 23:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87801">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ca3fdb17.mp4?token=D4fZIzBCqU9Cdz6nTUrUkTXiz-gWAiGxQlU7zFZnHKxVs8pQulMI-YnyacQ-XpPg6uq-1Cus_dsn-2DEU3aBJQOXICMwQlAlI2PcVKnxzQYQb20rxNyuLa-YfEikCQegx_LOmUsgmCZMV5DHTRFuA5HxcLdxtgvxus4jfhhlK4JuhRiBl7vpVjwPMi2EkgugbRQNWQu2xh_EBpBZCCyQ1-lrRdvMnkwsxUjh_eGICfPNNHhx_22UPTh6Y7jmPJQzjw__kcZM1ktpSiBlQRlfGOVuWuJ9WbsDR9WiuTqYGu7OCYy0oA_PFfRvVgXVXDj7ZnHp5e9YMRBrxUn7wkhmxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ca3fdb17.mp4?token=D4fZIzBCqU9Cdz6nTUrUkTXiz-gWAiGxQlU7zFZnHKxVs8pQulMI-YnyacQ-XpPg6uq-1Cus_dsn-2DEU3aBJQOXICMwQlAlI2PcVKnxzQYQb20rxNyuLa-YfEikCQegx_LOmUsgmCZMV5DHTRFuA5HxcLdxtgvxus4jfhhlK4JuhRiBl7vpVjwPMi2EkgugbRQNWQu2xh_EBpBZCCyQ1-lrRdvMnkwsxUjh_eGICfPNNHhx_22UPTh6Y7jmPJQzjw__kcZM1ktpSiBlQRlfGOVuWuJ9WbsDR9WiuTqYGu7OCYy0oA_PFfRvVgXVXDj7ZnHp5e9YMRBrxUn7wkhmxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
We are the king of Hormuz</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/87801" target="_blank">📅 23:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87800">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
ترامب
: سأضرب إيران اقتصادياً بقوة .</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87800" target="_blank">📅 22:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87799">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇾🇪
مشاهد من احتراق السفينتين في المخا، بعدما تم استهدافهما من قبل أنصار الله.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87799" target="_blank">📅 22:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87798">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e601d104f1.mp4?token=LGimF4MkABcn4lPsR6Pta9zKyehNhTCapOI2FiiU3VRj1sxUw8wvH9DKZVCaTRP9L8U_u44Z_FO2YO9DG-UtL41h2gEzamGM6ONNdVvED5s4aC4Wtqgwj-GrpoP4nwvS2mBu7kKpKbR8EdcWdJ8THWAxm07zJyzYW4L7VUeBi7dhv3N7Na11hz24YrxqNAUYwW3e4patBVnRaLNDyBsgk9Qi1eUpgLMkf2qxuBkkWYVoHQBoU_KIjcprf45jsl-oWURnecJaUOUttsxDTTqEe16UVmzLVzyoIfm4x9xJMc8uvs4VMNtcR2rh6fdgsoqnXTuxGdUMhAhN10WMXB03zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e601d104f1.mp4?token=LGimF4MkABcn4lPsR6Pta9zKyehNhTCapOI2FiiU3VRj1sxUw8wvH9DKZVCaTRP9L8U_u44Z_FO2YO9DG-UtL41h2gEzamGM6ONNdVvED5s4aC4Wtqgwj-GrpoP4nwvS2mBu7kKpKbR8EdcWdJ8THWAxm07zJyzYW4L7VUeBi7dhv3N7Na11hz24YrxqNAUYwW3e4patBVnRaLNDyBsgk9Qi1eUpgLMkf2qxuBkkWYVoHQBoU_KIjcprf45jsl-oWURnecJaUOUttsxDTTqEe16UVmzLVzyoIfm4x9xJMc8uvs4VMNtcR2rh6fdgsoqnXTuxGdUMhAhN10WMXB03zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية استهدفت سفينتين كانتا راسيتين في ميناء المخا.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87798" target="_blank">📅 22:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87797">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تستهدف ميناء المخا من جديد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87797" target="_blank">📅 21:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87796">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789a1d80f8.mp4?token=Xc5Y0azYcsymKwsBjNNKT5eM2rzgIBxnyhIdGcRpz27CilIbOJhsN5pn9gNo-K54CwLuIFPicb1oUkKre2vqfgVZuRXc5Ua8ZWGrOoiWf1bjP0mFkQJ4CR5gKp2ZTS-0lO46dpyaQDiGJhL5KRRs1JFDVxvDDLoObhi696YL1qg9heT6NuwIGaYkF-p8zVVlXp1E3toSoRc-h3Z1BNNZ6n_i8sFK6wSyrDNWP8h7Hfvir8FTfVol1_HoYSAhjWWZaZdANS8MH2Z3-apHgQeBQ9le_exR4zKH6Wr7PjjGV3bfQZng6lKxsb3cES0aDvgx91wlK8LEb1hZV8FUXbRJ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789a1d80f8.mp4?token=Xc5Y0azYcsymKwsBjNNKT5eM2rzgIBxnyhIdGcRpz27CilIbOJhsN5pn9gNo-K54CwLuIFPicb1oUkKre2vqfgVZuRXc5Ua8ZWGrOoiWf1bjP0mFkQJ4CR5gKp2ZTS-0lO46dpyaQDiGJhL5KRRs1JFDVxvDDLoObhi696YL1qg9heT6NuwIGaYkF-p8zVVlXp1E3toSoRc-h3Z1BNNZ6n_i8sFK6wSyrDNWP8h7Hfvir8FTfVol1_HoYSAhjWWZaZdANS8MH2Z3-apHgQeBQ9le_exR4zKH6Wr7PjjGV3bfQZng6lKxsb3cES0aDvgx91wlK8LEb1hZV8FUXbRJ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل
: أفراد عائلات أفراد الخدمة العسكريين قلقون بشأن الظروف على متن السفينة الحربية "لينكولن".
ترامب
: لا، هم ليسوا قلقين.
المراسل
: هل استمرت مهمة الانتشار لفترة طويلة جدًا؟
ترامب
: لا. لا. لا. لم تكن طويلة بما يكفي على الإطلاق.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87796" target="_blank">📅 20:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87795">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇾🇪
انصار الله اطلقو خمسة صواريخ  على ميناء المخا.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87795" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87794">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇱
الاعلام العبري
: أميركا وضعت فيتو على طلب إسرائيلي بقصف أهداف في سوريا.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87794" target="_blank">📅 20:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87793">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇾🇪
انصار الله اطلقو خمسة صواريخ  على ميناء المخا.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87793" target="_blank">📅 20:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87792">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇾🇪
مشاهد جديدة لميناء المخا وهو يشتعل بفعل الصواريخ انصار الله.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87792" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87791">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1341d9e0.mp4?token=r85eFjenPPODnFQ1Pl5fzYFSZO2QD169bT0jEHKf5Irx9kJsEAhEHawHz_tdIGnsOt-mP6y6UvXJ0eNHpfHYQw3JPYiGf63iQP3aDI79uAVmXVhxEtvtDyJE09Z3yz7HfIHY3YxfoJs2j4W-B9siBGogTTgivwsy_7_8yetCtPdZjQghZdqtsWT_JnU6rSkmC1iPdVSxgy63UHyWnYw4S8T4zye0wXdqdvJ__Ff8yYv5Y6wcoP3uE4BXepdwvnBGWkTbEpIFPxGhzEkUhnvUWteBuNZ83x5BwMrDaywIkLMeNws83rwVCkC28jXu5VYxs4SzDRE3KCl7yra3E66f1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1341d9e0.mp4?token=r85eFjenPPODnFQ1Pl5fzYFSZO2QD169bT0jEHKf5Irx9kJsEAhEHawHz_tdIGnsOt-mP6y6UvXJ0eNHpfHYQw3JPYiGf63iQP3aDI79uAVmXVhxEtvtDyJE09Z3yz7HfIHY3YxfoJs2j4W-B9siBGogTTgivwsy_7_8yetCtPdZjQghZdqtsWT_JnU6rSkmC1iPdVSxgy63UHyWnYw4S8T4zye0wXdqdvJ__Ff8yYv5Y6wcoP3uE4BXepdwvnBGWkTbEpIFPxGhzEkUhnvUWteBuNZ83x5BwMrDaywIkLMeNws83rwVCkC28jXu5VYxs4SzDRE3KCl7yra3E66f1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
قصف صاروخي من انصار الله جديد يستهدف ميناء المخا</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87791" target="_blank">📅 20:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87790">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇾🇪
استهداف مباشر لميناء المخا معقل تمركز العصابات المنفلتة الغير شرعية في اليمن .</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87790" target="_blank">📅 20:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87789">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefbba7708.mp4?token=XZge0-vf2XOxxUUZSMcGVKfncYrHdu8t5tHft7ue7-lJWZ9Xz0JIuPbhXGmiE5mctRpvaNGsPfslXVrFTKw84R9ZAx9cip1ujXXdGuJJ3D0beMKmB05_w7NNzB6rYch1mFDcuFV2oih1lzlsD-kepsTHaqGwarIgUJ4rXRRWLZkSJbi0-pXqFh1axITwA091Ipb9fIbJjLxeWYfFa3EcGYBc3Vvyc0CuNFAiCCktVpot0Rad4U7pDvZCoQt3Gcf_a-kkPlz3gOQ4dBvvF62_TOW4VBNNsoZ7uhXCnoBf3K5_3TPIgiZMRc_eKseI_rt3Ac8fnAcRWbiOLaHOuS2qpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefbba7708.mp4?token=XZge0-vf2XOxxUUZSMcGVKfncYrHdu8t5tHft7ue7-lJWZ9Xz0JIuPbhXGmiE5mctRpvaNGsPfslXVrFTKw84R9ZAx9cip1ujXXdGuJJ3D0beMKmB05_w7NNzB6rYch1mFDcuFV2oih1lzlsD-kepsTHaqGwarIgUJ4rXRRWLZkSJbi0-pXqFh1axITwA091Ipb9fIbJjLxeWYfFa3EcGYBc3Vvyc0CuNFAiCCktVpot0Rad4U7pDvZCoQt3Gcf_a-kkPlz3gOQ4dBvvF62_TOW4VBNNsoZ7uhXCnoBf3K5_3TPIgiZMRc_eKseI_rt3Ac8fnAcRWbiOLaHOuS2qpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
استهداف مباشر لميناء المخا معقل تمركز العصابات المنفلتة الغير شرعية في اليمن .</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87789" target="_blank">📅 19:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الشيخ نعيم قاسم:  - من يراهن على الاستسلام إنما يراهن على سراب ولا يعرف المقاومة جيداً بأنها تتحمل وتصبر هي وأهل المقاومة  - اتفاق الإطار الذي ذهبت إليه السلطة اللبنانية ليس لا اتفاقاً ولا إطاراً  - اتفاق الإطار هو إملاءات إسرائيلية بالحبر الإسرائيلي تُوقّع…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87788" target="_blank">📅 19:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔻
كلمة مرتقبة للأمين العام لحزب الله الشيخ نعيم قاسم اليوم الجمعة عند الساعة 18:30 بمناسبة ذكرى الانتصار يتناول فيها آخر التطورات.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87787" target="_blank">📅 19:16 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
