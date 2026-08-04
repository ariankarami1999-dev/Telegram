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
<img src="https://cdn4.telesco.pe/file/lQmKElPSULmpHHeL4dQ2886FPrYHWkcHZlpS9-N395y00kOqRIuZ88YhKMdEnJaM9SS05auC5HjMjYlNreXb2D1lhHpnPjVbDjRfGmoN1uz9D4NVvkgrCZTXVQpwDXgLUAlpGYz778DZXmIC5M6V81lLXo45oqWrn8pKaWNVj165ndzPRL_aZqaGQO4WB2Je1T2s0gTV-mIFYzgatpSiZEeUxN_FZhCsb9by3GWpuGVrWuSXcF0VD1mG93wu8CsrOTmJQFitT6Z9aR3uAH9XC4mFoqogFG4CHg56b1icocrFK8W_rgrSHRltEpsxuE2qDhL2F7Kr-bQJf8FAxwsekA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 15:06:30</div>
<hr>

<div class="tg-post" id="msg-86892">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇶🇦
قطر تقول ان هناك مشروع اتفاق محتمل يجري تداوله بين الأطراف وان التركيز حاليًا ينصب على إيجاد حلول قصيرة الأجل.</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/naya_foriraq/86892" target="_blank">📅 14:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86891">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e077c0ea7c.mp4?token=SUtdZjHPoZCx3cV5zaJinECFkAmQmEzRXECVqRU4wjRsMht1r_hUfp9ViXgTCoCIez4TPjhB25YboWiBV70E1DlEqZgQ6j9f4UFRuOcU8LIimIxd1uZQiHst_7b1B3f2os2pbfHTWCjLfmCPSu16O2Nag4JqXJVhZsmB0mJAlvZZJiB11Z5hHpnu1h0ot2lGf7pZneb_ZXTTSA8ZIq5i9TSxKzyO0DSnu8jBMyN78rAxrpe79mW2x1KDk2IYaeHwvMCXXs9NGUH8DRVNXAAXgx4V9CvH3m6TtF7AmP8p1fvXBD1ddZGEos3HqPjI4cpC2RS0nhdoQphJ1xYiHVi5cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e077c0ea7c.mp4?token=SUtdZjHPoZCx3cV5zaJinECFkAmQmEzRXECVqRU4wjRsMht1r_hUfp9ViXgTCoCIez4TPjhB25YboWiBV70E1DlEqZgQ6j9f4UFRuOcU8LIimIxd1uZQiHst_7b1B3f2os2pbfHTWCjLfmCPSu16O2Nag4JqXJVhZsmB0mJAlvZZJiB11Z5hHpnu1h0ot2lGf7pZneb_ZXTTSA8ZIq5i9TSxKzyO0DSnu8jBMyN78rAxrpe79mW2x1KDk2IYaeHwvMCXXs9NGUH8DRVNXAAXgx4V9CvH3m6TtF7AmP8p1fvXBD1ddZGEos3HqPjI4cpC2RS0nhdoQphJ1xYiHVi5cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجمهورية الاسلامية الايرانية تواصل نقل قوات ومعدات عسكرية على الحدود الايرانية العراقية الكويتية.</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/naya_foriraq/86891" target="_blank">📅 14:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86890">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇸🇾
سوريا الجولاني توافق على خفض واردات النفط الروسية خلال مفاوضات رفع العقوبات الأمريكية عنها.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/86890" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86889">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الدخان يتصاعد من معمل الالمنیوم في مدينة شمس آباد الصناعية والاسباب غير معروفة</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/86889" target="_blank">📅 13:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86888">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thn_c6yCN8xHdrw_OPi_ZQ5Fmj3BX91xlFbR8NN2aCE6VWjISXzkn5xCCmBUSahtTvho5A3jCZlm9mU7qPkgojS2ast9mZsm1ncZYswjLiQ5aJAXu3VOQS9PxsQKobW3iKWbd_WjbkuzuZ2eko1IG9elnjF5z014LqOkwSAymLiV754qIGv9AmLy4Ydfgpgn9G-hygZUVd8fJY60vkXUx_X7IgK3W7uDiplRvQwdDevJPlkaPRdFRBPhEFuJa99qVzs127Y8Qe3p-MdbCHl4ty6W3BNP78HRenWUweAGVoeTijuOQs__n77-5t7DEkdfupgv-UZnyBEEO0wJ_pac0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/86888" target="_blank">📅 13:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86887">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/86887" target="_blank">📅 13:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86886">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي: أكثر من 70 فوجاً انتشرت على حدود المحافظات خلال الزيارة الأربعينية.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/86886" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86885">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي:
أكثر من 70 فوجاً انتشرت على حدود المحافظات خلال الزيارة الأربعينية.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/86885" target="_blank">📅 13:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86884">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6l-2gtBspR_5uv0quNBiSZc3yU-cSOIWZNI7iaeGxqO6DcqXal90UdvNySZoJpKgd1kMnBAlaXE_cIslqlALd78CfM2EJpNfuE-iD-bRrqBnAA_PMjT2Ekh6EZzkrmClaiRDGcmv6GxpRuDDlD4CRP5yBghduNK01Qw4MxD73yeDN-s0O6lTF-k_hI3SGYJnhsoIl9Psu80xMyXHa6O1lOsXoYxkSZYb5dwBKr3Q0iQ2i67v1M5fppTChtQ4VmapvcSpBoY36lAjuVMqD1TiH7t_rclHt30wnXUsIyXdUEReWmuVdi_O-dIdMCJQhML5YHTcTHVS21_mKQ92Zjoww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد لاعمدة الدخان من جنوب طهران لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/86884" target="_blank">📅 13:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86883">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_tlfjCTl5a9Ra2mmOXDnmpv60UQitWNKHYREDPZWGbhh2QOEz8rPxADc_epdMjGl6nQk_mlQcnTYEpghGe0hISQQ8EsiGH4Vt1SGEYKrIXYyzQfIIIRGJmvdz8C2aHcwoRdLlQ3GWBvaJcmKC5PFpRCHlPzJX6Vg9dC2H2SbDFszNOBTFEoZUn_z7YRitp6JlFc5rcOGQhJak5qXnpTia22if2WfOroMFP-veGgi0oSK43k8nNzXzYiWyC1CC-2jXmTIfM4v77JcS3sZ4FkCn3i_rh95YNpX1_EUbsjgOO3mA94SEfJDqNdMn53cATrU-2fnn4LFSTrbJB-WRdtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد لاعمدة الدخان من جنوب طهران لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/86883" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86882">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مصدر ايراني رفيع المستوى: بالنسبة لمسار الملاحة الخارجة عبر مضيق هرمز، ستسمح سلطنة عُمان للسفن بالمغادرة بعد إبلاغ إيران بذلك</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/86882" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86881">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مصدر ايراني رفيع المستوى: ستتبع مساحة الملاحة البحرية الخارجة من هرمز مسارًا يربط بين إيران وعُمان.</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/86881" target="_blank">📅 13:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86880">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📰
مصدر ايراني رفيع المستوى لرويترز: خطة مؤقتة بشأن مضيق هرمز قيد المناقشة مع سلطنة عمان تمنح طهران السيطرة الكاملة على حركة السفن القادمة.</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/naya_foriraq/86880" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86879">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📰
مصدر ايراني رفيع المستوى لرويترز:
خطة مؤقتة بشأن مضيق هرمز قيد المناقشة مع سلطنة عمان تمنح طهران السيطرة الكاملة على حركة السفن القادمة.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/86879" target="_blank">📅 13:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86878">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e85d3110.mp4?token=tkMkWRh5bEKF96vzC5XRSK5f_CEvsEk0aAbaIZeyXcvdbUUB51tdoTaX4BGdXwYs4Dcm-r3-5a3iwjuA1MSRHL9KulqXWQqEGSViYpF_R1o3sWLKJ8yWROAb6mZMHakmG568HTqh9prlxcNveGGYT58NF-RIr09G9JIEeWaHswWGBJkwZeelqwvziVUWOTYgsPc5T2Kaz0EsU-hnahfEXokcQ7RRdYW0l5nv9EIe5bOdsnY26F7Qs6v0xRXUEl1ufswMV20et5BOCCT1jdvGFMgR58ycaqo5Vs33QJPWgWPwp9YLuE14SnfvFGVsXn1XjqiSvCB5TxwKriNO7Pp7SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e85d3110.mp4?token=tkMkWRh5bEKF96vzC5XRSK5f_CEvsEk0aAbaIZeyXcvdbUUB51tdoTaX4BGdXwYs4Dcm-r3-5a3iwjuA1MSRHL9KulqXWQqEGSViYpF_R1o3sWLKJ8yWROAb6mZMHakmG568HTqh9prlxcNveGGYT58NF-RIr09G9JIEeWaHswWGBJkwZeelqwvziVUWOTYgsPc5T2Kaz0EsU-hnahfEXokcQ7RRdYW0l5nv9EIe5bOdsnY26F7Qs6v0xRXUEl1ufswMV20et5BOCCT1jdvGFMgR58ycaqo5Vs33QJPWgWPwp9YLuE14SnfvFGVsXn1XjqiSvCB5TxwKriNO7Pp7SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطن سعودي يوثق نفسه وهو يحرض على الطائفية ويسيء إلى زائري الإمام الحسين (ع) من قلب العاصمة العراقية بغداد  إلى وزارة الداخلية ومديرية الإقامة والجوازات: كيف منح هذا الشخص تأشيرة دخول إلى العراق دون تدقيق في نشاطه ومحتواه رغم ما ينشره من خطاب تحريضي يثير…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/86878" target="_blank">📅 13:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86877">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية: عبور ناقلات محملة بالخام العراقي عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/86877" target="_blank">📅 12:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86876">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">السفينة خالفت توجيهات حرس الثورة الاسلامية</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/86876" target="_blank">📅 12:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86875">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏استهداف سفينة بضائع بمقذوف حربي</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/86875" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86874">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حدث امني قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/86874" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86873">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حدث امني قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/86873" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86870">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XW38rQN1H5ufrCQqdokh0uV9mITZ5r-KF61zqYfh9836BiwhSfnbYccDh6hh4Is2gGP_gig5oCRtcIULdXNNTJRiYdBQGmjMoaBtKgoptu6FkEK6Lc1TqIhZWOy86s1JtLkaWUPa7dQdGO01qs0RV2AeMOQVSISHd5kiZkFZoxkhg6ysH9T1B7koeryrXeGbHlyP7dKddTrHc4DzFPmGMnfnV_pJgxWy5rPMDwo0QiuBnWW9z97J9G2aaArZ2IRVNaMB16ds2PDtnOBZF-Dtr05LBcBeRr7mwWKAmp1u-MTgLi5TPwtxSj65THHCa8UnP3WyVS9hDtkw-6A3M2hnyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3NXc_GR6pqiiURN-M-ZbkQCHtl-rxi6wYM23XVWm0pZZxnnkdetpYuqe89PeGvO-GdnUVG5SevHYKgiQBU6SFj6dxd5TasG13EpVKlea_AxRno2vlmmCXRDxL25WPNkczAXu8gJSC8ro2i3_M0rzEbbTh0r_ir8Dnxunlw2ooyMzBMGbguAVHPbMHTc-w1y0R2NufMZU_BJlSaddZRyypFcLp9L2Ije9jHsQhChVQx8AaCGOhVDrzuYVikJWhG1Xb90Ol2d7o0CRWI7uP_8apJZJuYgMItgqyh50ACiwRaMFMN-thL4qq9r5ifvlSmVub8ZrGHGJjt44O7DKHP7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EO8-HRTmGfphlnMqGmGjFmZRUY_nNgw-uIasiuD28cEwCj2za1_yWnC2OWskwjqCxQz4QAvtIBn81o5rBaIVGfod7g3wBKiVcvcZ7uH-3D1PXxmwgUZuc6G6z7cZzOtqGAZ3Tw5PEzhJLscAFwWU_USFpsd56WagE22jHDRjKuhhWNTmrAt-2n7J4HCliT78xojGL076vGGIsFl75VZCpr32LeCdyvVOsdmN6ZvLSY5YWO-ihkM5hoGEhy9WhirIx8jbRf-5T1_iFsdPogAlFLUgdHsSXnQrv-7I5nhNUCn6_pme4BS6HFpfLhLMMQuthuHJKa2dRCaOgI1N7XDexA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇱🇧
الجيش اللبناني يدعي إحباط محاولة تهريب صواريخ غراد بقطر 122 ملم من الأراضي السورية إلى الأراضي اللبنانية كانت بطريقها إلى حزب الله.
تنويه للجيش اللبناني: الجنوب اللبناني بحاجة كمان لإحباط التوغل الإسرائيلي
🤷‍♀️</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/86870" target="_blank">📅 12:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86869">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afb1b6f848.mp4?token=j9xkO4M91OQgG7rb1MTP3duzgd6UgiMW71DrLCrptsza50-NvEUvaMLDz7A5qqesXGSbjae0xmiczOnLkSb-vLn7lncT6QVoou6A0mV__Ar6Ojpe8rT7NrvSftPYi9IkeCy9fWqjOyUx-jEd9KLVKwYnDU-ZPbLTQdXWU_uNC9Dh3BiUJYa4G1G4SSgJm85_gIKU2JSMHTNwyNrZNZKJlCV_ZrBuN0HLDB9zMxLwN8ZQLiyWi_z9mMNLpyYTAMGrABTgp4MI24l28Yg6-Flv3VWjxWIGUcbVwzP7F0hxNqtXdwEEKNK9ZhLTjgN5jgX2z3g0Jj6FqxiJ7ztaiYdbrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afb1b6f848.mp4?token=j9xkO4M91OQgG7rb1MTP3duzgd6UgiMW71DrLCrptsza50-NvEUvaMLDz7A5qqesXGSbjae0xmiczOnLkSb-vLn7lncT6QVoou6A0mV__Ar6Ojpe8rT7NrvSftPYi9IkeCy9fWqjOyUx-jEd9KLVKwYnDU-ZPbLTQdXWU_uNC9Dh3BiUJYa4G1G4SSgJm85_gIKU2JSMHTNwyNrZNZKJlCV_ZrBuN0HLDB9zMxLwN8ZQLiyWi_z9mMNLpyYTAMGrABTgp4MI24l28Yg6-Flv3VWjxWIGUcbVwzP7F0hxNqtXdwEEKNK9ZhLTjgN5jgX2z3g0Jj6FqxiJ7ztaiYdbrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
اندلاع حريق مفاجئ مجهول على متن سفينة أثناء إبحارها قبالة سواحل منطقة "الفاتح" في مدينة إسطنبول التركية وسط حالة استنفار كبيرة للسلطات البحرية وفرق الإنقاذ.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/86869" target="_blank">📅 12:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86867">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8d4da1cb4.mp4?token=uI3PqNkug24nbLbIhpK9Jn0O1BiHUmfQLp2Fjlcz_caG34CZd5ABzRdA6GYh25jfrqw4D3j8DPeVDsvk3HGq3PL_tOjcRpa0-YNN9NYUomeuTTPB80DKVbw8WxdrLiGTysnIHOxmj8UwbYRpuyw5DQCZ6PWAOu7Ho-mFV-XBll0UfSHkMA1yV2B81iHdB1lfhh_H2XHhTh8ovwhYq9lsNPUbQMaG380vSMc6cf2H7h_aNWbrZ0806DiQks2bVZqkoOeIumrhB-lJIdLdyszephXOJl0Rf3muI7eCzvyj2ilYWAWhR4HmYXHi7oG3lZcVMebfsele1BxrnSVCQq5RujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8d4da1cb4.mp4?token=uI3PqNkug24nbLbIhpK9Jn0O1BiHUmfQLp2Fjlcz_caG34CZd5ABzRdA6GYh25jfrqw4D3j8DPeVDsvk3HGq3PL_tOjcRpa0-YNN9NYUomeuTTPB80DKVbw8WxdrLiGTysnIHOxmj8UwbYRpuyw5DQCZ6PWAOu7Ho-mFV-XBll0UfSHkMA1yV2B81iHdB1lfhh_H2XHhTh8ovwhYq9lsNPUbQMaG380vSMc6cf2H7h_aNWbrZ0806DiQks2bVZqkoOeIumrhB-lJIdLdyszephXOJl0Rf3muI7eCzvyj2ilYWAWhR4HmYXHi7oG3lZcVMebfsele1BxrnSVCQq5RujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطن سعودي يوثق نفسه وهو يحرض على الطائفية ويسيء إلى زائري الإمام الحسين (ع) من قلب العاصمة العراقية بغداد
إلى وزارة الداخلية ومديرية الإقامة والجوازات: كيف منح هذا الشخص تأشيرة دخول إلى العراق دون تدقيق في نشاطه ومحتواه رغم ما ينشره من خطاب تحريضي يثير الفتنة ويسيء إلى شريحة واسعة من العراقيين؟!</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/86867" target="_blank">📅 12:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86864">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ec2bebd6.mp4?token=l8t5UIRV9Im9nvNOV2PMhnESubnAq6PB34HXLBt0VPb0mnJb8HDdFSYW2rfo7TKQr876pMee7QFGt9LN4NDwj3cGcco6wWk4vmQW7XUKQZL01sMtPav1X5uJPWtzdBMniB1YEGvYJHefLQFwfKcOix6XUrw8vMhq4k6a6Za0Qi-6MpEHihJe6g1K2L_Ot8rI-7wcmOZEFoqxgjRwfZFwb-khG0SVUD2Aau9wmIQVYulVFr6YiTca3cNgZxwym8kGWjF9JYeIC-Tz-Nds5tIqAfAt0sEE8iBrbJUsUxJ370szPV9zqsfO3kmOrKWJz-_EnXwcjnZZc44s5KoUhLG_fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ec2bebd6.mp4?token=l8t5UIRV9Im9nvNOV2PMhnESubnAq6PB34HXLBt0VPb0mnJb8HDdFSYW2rfo7TKQr876pMee7QFGt9LN4NDwj3cGcco6wWk4vmQW7XUKQZL01sMtPav1X5uJPWtzdBMniB1YEGvYJHefLQFwfKcOix6XUrw8vMhq4k6a6Za0Qi-6MpEHihJe6g1K2L_Ot8rI-7wcmOZEFoqxgjRwfZFwb-khG0SVUD2Aau9wmIQVYulVFr6YiTca3cNgZxwym8kGWjF9JYeIC-Tz-Nds5tIqAfAt0sEE8iBrbJUsUxJ370szPV9zqsfO3kmOrKWJz-_EnXwcjnZZc44s5KoUhLG_fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇺🇸
تأهب عسكري غير مسبوق في مطار رامون العسكري بالكيان الصهيوني.. حيث أظهرت مشاهد انتشار أسطول طائرات وقود أمريكية في قاعدة رامون لجوية وسط تصاعد التوترات الإقليمية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/86864" target="_blank">📅 11:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86863">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔻
الشيخ نعيم قاسم:
الجمهورية الإسلامية الإيرانية انتصرت ولم يعد هناك مجال للحديث عن من انتصر في المواجهة
إيران عملت على أن يكون لبنان في البند الأول من المذكرة واشترطت إيقاف العدوان والانسحاب الإسرائيلي
المفاوضات المباشرة لم تجلب للبنان إلا العار والذل والخيبة والتنازلات المتتالية
﻿
تحية إلى العراق واليمن على نصرة قضايانا في مواجهة العدو الواحد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/86863" target="_blank">📅 10:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86862">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات قوية في الكويت تسمع دويها في محافظة البصرة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86862" target="_blank">📅 08:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86861">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇬🇧
صحيفة تايمز: تسرب أسماء ومعلومات الاتصال بأكثر من 114 ألف موظف في الأجهزة الأمنية البريطانية إلى شبكة الظلام "دارك نت" نتيجة هجوم إلكتروني</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86861" target="_blank">📅 06:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86860">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCcfjwpj-hXP3DUYXRI7q3wckgn7k7cF_Qe15JMmPmED6a9T9pmDAOtW9fYJO5uYS3Bqj-m-cwwyOA4kBTV1ex2ryiBEKTIXEDr5A1_X1GEnUCnKTmYCVw-8CXy3Z9I0HUWPo-5IPpcm-Svtug9t0QSLXQKKNQEVaN36TAHOO7JZ_hH3eYM-QJEIbI9gemaU-cjJd63RHg4lUqSIxM7KMHjLpmJVWc3WqaMhiaUWURu3mTRKiwrw_cV1g75bM-At4XqaV9T89KlKyyoG7dJDJXMiV7CcX8uNRHTH8MzZnH9OLNeZm8wHuauYx8KjTW7fYLbRItIgoTWQBQyMQfaJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرض سفينة مخالفة لقوانين عبور الحرس الثوري لصاروخ مما ادى الى استهدافها بشكل مباشر عند سواحل عمان.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/86860" target="_blank">📅 03:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86859">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwrlW2Z9-Y59U8XK4142VFGH3D2zuTUeCJo0ZWULjYqQQBl0dYoxHAFEQJ-MFPZwlNNwGFlsAGQNzVTsYEPKPFE9GKlzQgMXBd_Og4tHU-yip6jbqKYWgEjQBNX4LxcQo1X1mXnbM68DGgJ1WadgZ6WpuL_LN-_YIp_lXGHEJYCN8_rhh6jTvO0uCQ2XgZXr-LQSFGBDTtMsTs-Hvrrv_DaDCahzgGN-wc1rIgvcsm4BhsOqUt5glt8tYJ3hVizBBeKsXC3xTneOfs4FWnl8UKhqsNciJFhdzH1Ilm8usjKJ8xg-np3JYxpWQjEfwiMRkQf5c9Mrceei3p_646v-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز شمال الكويت مجددا ؛ اصابة مباشرة لقاعدة أمريكية</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/86859" target="_blank">📅 02:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86858">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجارات قوية في الكويت تسمع دويها في محافظة البصرة.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/86858" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86857">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات قوية في الكويت تسمع دويها في محافظة البصرة.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/86857" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86856">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله اكبر... ارتفاع النيران من وسط الكويت لاسباب مجهولة.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/86856" target="_blank">📅 02:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86855">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=iswIkxGtX5OkEbSW1FHdbr0cSRfBxKZ2PRpu51knRK0xEeXEIa0ZOT4p7D7iiALEdw3jFG_PD_yxHlbpE9r9l9XHAiopJj9ObKD9zsC5YMUGBFI_TnSYx9BPj2mUZdKc3KCRtnBMp-UKSoajgSupCOWobPMuukMVG4SkmbvK6ybIDTOCJWkbx7ISj9XcvCvd78Ms6sjMt8BTPcx8YCcbFFWgIKOS93Ex28tu2f6azO2A-YiMi_ZSK9Etrzd7neeZIKRvPG6m4M8ypz2Dl9KKhO4rsGaqJESm0o6LAD9SfQKwNPClyJZKVJtNRLXeLbFN06I59f4ogcswhbZC1rhzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=iswIkxGtX5OkEbSW1FHdbr0cSRfBxKZ2PRpu51knRK0xEeXEIa0ZOT4p7D7iiALEdw3jFG_PD_yxHlbpE9r9l9XHAiopJj9ObKD9zsC5YMUGBFI_TnSYx9BPj2mUZdKc3KCRtnBMp-UKSoajgSupCOWobPMuukMVG4SkmbvK6ybIDTOCJWkbx7ISj9XcvCvd78Ms6sjMt8BTPcx8YCcbFFWgIKOS93Ex28tu2f6azO2A-YiMi_ZSK9Etrzd7neeZIKRvPG6m4M8ypz2Dl9KKhO4rsGaqJESm0o6LAD9SfQKwNPClyJZKVJtNRLXeLbFN06I59f4ogcswhbZC1rhzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات قوية في الكويت تسمع دويها في محافظة البصرة.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/86855" target="_blank">📅 02:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86854">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجارات قوية في الكويت تسمع دويها في محافظة البصرة.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86854" target="_blank">📅 02:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86853">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e0824f22.mp4?token=hTJFfwHGk4biEQ5wRbWOKyX_i2HfmwjPsrn0yIhlrdIfO-7UVfLUe5F0JMr2Tu5xuByE-NLrABAHd6U-30GGz8rnTFQevUFOFDBgnC8Stw7pHa5y-70MSnOXW0jalyfXe15OVJgjWlfxfjpSvddzmYDFLQds03aCxxaxUbw7lkfbFVAx3rb_paJ0ujFe2c9EoFZesD4KfhCBC5uzWYOwpUxYnrpkJTnFM5qLvdU-dxUxV8a4SJchnrrULPlnIXq1XrAX5k3HHVc0TPXf6DIvpQXFSG_bUC73Wd0HwA8qp5RlFNLoawfmH2PVzyXKU6yYD9oh7n5WqC45eGdfPZ9GHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e0824f22.mp4?token=hTJFfwHGk4biEQ5wRbWOKyX_i2HfmwjPsrn0yIhlrdIfO-7UVfLUe5F0JMr2Tu5xuByE-NLrABAHd6U-30GGz8rnTFQevUFOFDBgnC8Stw7pHa5y-70MSnOXW0jalyfXe15OVJgjWlfxfjpSvddzmYDFLQds03aCxxaxUbw7lkfbFVAx3rb_paJ0ujFe2c9EoFZesD4KfhCBC5uzWYOwpUxYnrpkJTnFM5qLvdU-dxUxV8a4SJchnrrULPlnIXq1XrAX5k3HHVc0TPXf6DIvpQXFSG_bUC73Wd0HwA8qp5RlFNLoawfmH2PVzyXKU6yYD9oh7n5WqC45eGdfPZ9GHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحاج أبو آلاء الولائي الأمين العام لكتائب سيد الشهداء، بين العتبتين المقدستين في محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/86853" target="_blank">📅 01:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86852">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e07b48363.mp4?token=Tv7t8ZX0m6lpn6DpXBI1NFaM-7-oq5kLijFdkwbRzutwcURJciaQUOpPiPi3F3XsxpnlX-_XS3jRK2PDXcgBy2zevS9iZQexMh8TXGgrkIkaFgl7V-GXiqo1deqm5eMDWzDFQuLjDf6XcbCkR89AyrgxrsQe1DGohoKHD2PmEgwsuhiycqowu_UH0L1xlzy_SeFEK4ryoJrOftqEp6fDt6qr8GjGNy3KNjMKy8Sj0PGOc3nMpbJGwldV7dLk9x_bpL48aXCfIegoRvhlO--pQgVnJIfCrCAWNB6YfAUkHSrzkJMS8fDIZf8zxOwVDuXS1hkCuAsnCRTbkC1CeCRt453_OqLYN-uBWk08VD2W_Qv4h3LlxswfQzJJkMVvXHaUa4vF9dlON4klFCy6kEwnP4ubcf6u7qR4A3Lze16lqTIzs2A3N5AFyARTxID-bgQd0ypv9N19nh19gKC7gcuC8LMhI4EpiDf_A6bMwollY3QP8IIaHiOVejyNHYXj_natSGcjgMGhx8VeJgYomoRLpBFraCTgw7nQtPfXF_nOVz7rOc8I1lOsat_SZmIfUBPN6RvauhN8jZ7JM3ivEByVQFWNj2rv0zeE7pen82zThBjpbWXwoDYzOKNQ6uYPamci0MJqOAusfVcYnKjkwA0fUEvXBSQASUhGZzUME-GT620" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e07b48363.mp4?token=Tv7t8ZX0m6lpn6DpXBI1NFaM-7-oq5kLijFdkwbRzutwcURJciaQUOpPiPi3F3XsxpnlX-_XS3jRK2PDXcgBy2zevS9iZQexMh8TXGgrkIkaFgl7V-GXiqo1deqm5eMDWzDFQuLjDf6XcbCkR89AyrgxrsQe1DGohoKHD2PmEgwsuhiycqowu_UH0L1xlzy_SeFEK4ryoJrOftqEp6fDt6qr8GjGNy3KNjMKy8Sj0PGOc3nMpbJGwldV7dLk9x_bpL48aXCfIegoRvhlO--pQgVnJIfCrCAWNB6YfAUkHSrzkJMS8fDIZf8zxOwVDuXS1hkCuAsnCRTbkC1CeCRt453_OqLYN-uBWk08VD2W_Qv4h3LlxswfQzJJkMVvXHaUa4vF9dlON4klFCy6kEwnP4ubcf6u7qR4A3Lze16lqTIzs2A3N5AFyARTxID-bgQd0ypv9N19nh19gKC7gcuC8LMhI4EpiDf_A6bMwollY3QP8IIaHiOVejyNHYXj_natSGcjgMGhx8VeJgYomoRLpBFraCTgw7nQtPfXF_nOVz7rOc8I1lOsat_SZmIfUBPN6RvauhN8jZ7JM3ivEByVQFWNj2rv0zeE7pen82zThBjpbWXwoDYzOKNQ6uYPamci0MJqOAusfVcYnKjkwA0fUEvXBSQASUhGZzUME-GT620" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
متابعات نايا...
آراء زوار الأربعين بشأن قضية تسليم سلاح المقاومة العراقية.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/86852" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86851">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
🇺🇸
طيران مسير مجهول يستطلع المنطقة الخضراء وسط العاصمة بغداد والقوات الامنية تحاول المعالجة بمنظومات EW .</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86851" target="_blank">📅 23:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86849">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a31c1f52.mp4?token=ZCbVN3N8BmVs5mFaM0-Sx4UAbeW0chR_PWymt1OQHL9oEcrJ9b3HooDlkNxuGbuc0Ujx9kk9Yx4A5HCIGNshq8gVs5OS7KngwE9qpgVS20pgjVHtLZIIMLhrWxLz3qhtvZ8jUEUf9Qtx6ov8Jhhth9MLlPI82-cDtIvBL0HTRqY5f0emVDfZX2FZpZnka704e9DwOAJrk_zCavc_cVgvWSo_M9Fy5iptdH-ng1UIfucXzrOwuKaBqMJPenB9GioAyHdL3FhwMqyNOW5LZqw9YyTEtzcVdIvIa5A0L4Aa6ENI-TQdlqnGUTG02wWLr4rEeHYxh3y5XNyZkSXGNMgkxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a31c1f52.mp4?token=ZCbVN3N8BmVs5mFaM0-Sx4UAbeW0chR_PWymt1OQHL9oEcrJ9b3HooDlkNxuGbuc0Ujx9kk9Yx4A5HCIGNshq8gVs5OS7KngwE9qpgVS20pgjVHtLZIIMLhrWxLz3qhtvZ8jUEUf9Qtx6ov8Jhhth9MLlPI82-cDtIvBL0HTRqY5f0emVDfZX2FZpZnka704e9DwOAJrk_zCavc_cVgvWSo_M9Fy5iptdH-ng1UIfucXzrOwuKaBqMJPenB9GioAyHdL3FhwMqyNOW5LZqw9YyTEtzcVdIvIa5A0L4Aa6ENI-TQdlqnGUTG02wWLr4rEeHYxh3y5XNyZkSXGNMgkxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
سفينة شحن تركية كانت متجهة إلى روسيا تتعرض لهجوم بطائرات مسيّرة في البحر الأسود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/86849" target="_blank">📅 23:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86848">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇧🇭
البحرين
:  ‏خفر السواحل تعلن عن تغيير منطقة العمل الخاصة بمشروع المسح البحري ثلاثي الأبعاد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86848" target="_blank">📅 22:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86847">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2LKTIsW70UdXZAONsfSXSWDM9FuUsv5SUwteA5FnbkbAsF1M0tzb8pXpL_T0aJHm9Nq1QkcbbkzxZmWIQnY92L6FhAOyOv180uRXb_pYrtwVhAkj_3NAkUX7DjMdLwRz4-clLzpdxRY7ZLYTA42MmBTKgdD3jK1dBYIn27Wr-oLlyRD54kWQp4TqYTEf6LufvDNwl7RuY872fxTE7nCq_Gwx-Lt_r15XnBcgHsfGHb__tPaIlyrI5FXhd7sl-1spmetKTrNnLAksGm68bEgcAZNzKa6RKzM1p12DQWwSKwvYub1JO8nfN4mL0ArejVTU8_VUAPz7OSBKZS1EZgV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇨🇳
تعزيزًا للعلاقات بين الشعبين العراقي والصيني، أطلقت شركة باورشينا (PowerChina) الصينية العاملة في العراق مواكب خدمية لتقديم الطعام والمياه والفواكه لزوّار الإمام الحسين (عليه السلام) خلال زيارة الأربعين.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86847" target="_blank">📅 22:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86846">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992b3aa52c.mp4?token=HMipZZ5Ycykw3td_rssG5yatDM0pV9PPQFUAZH605GUm2hi2ryqk90qos2zrxRs1DDZafHtNez0VJHt01U0NMFVvg_r7ftj_naqc7mSLzle0Le4ot9LXzLg3Uh5EZVoDWRayTv3JK5gVvo3UOJB387nvNNu5qeLD9uvp4pfjZDHNa3Tku0zG14exiSLjlfZI0IhzkFbr03eIVrDDELMRaHzfAvCGg4ZWSoX5ucZbeDroFjfgoSKMDf3EjbPpciFhy94H4-Cnxd_otTJ3h7BjahVBpAt2s7lcxjjEw-qnwDc3_VK8yF1n9i_VtsYLegy8ydvKNAgI2NKNFFBcOWKBqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992b3aa52c.mp4?token=HMipZZ5Ycykw3td_rssG5yatDM0pV9PPQFUAZH605GUm2hi2ryqk90qos2zrxRs1DDZafHtNez0VJHt01U0NMFVvg_r7ftj_naqc7mSLzle0Le4ot9LXzLg3Uh5EZVoDWRayTv3JK5gVvo3UOJB387nvNNu5qeLD9uvp4pfjZDHNa3Tku0zG14exiSLjlfZI0IhzkFbr03eIVrDDELMRaHzfAvCGg4ZWSoX5ucZbeDroFjfgoSKMDf3EjbPpciFhy94H4-Cnxd_otTJ3h7BjahVBpAt2s7lcxjjEw-qnwDc3_VK8yF1n9i_VtsYLegy8ydvKNAgI2NKNFFBcOWKBqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحاج أبو آلاء الولائي الأمين العام لكتائب سيد الشهداء، بين العتبتين المقدستين في محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86846" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86845">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98195db8f9.mp4?token=KRpLulGPYvaKNa_Py33ALIRzbgjV1sSUC8HXv_xJu2lZZgHh2I3TOBsJW_RMcFWYxfnRbHOIO7d6K7GJZYNQgKcNEyKWV8KwGzvlgnw4X-S2Vlo3RiU26QtRrfL1kABVYvTzp00b9GdjTqjVzRz2mKtagMrfznTQADdhdQAITBCDsGduHUebSoMnCX75N1m47sStIvhM5p4Oa_5fHSEwrGZO-_ainfJ5jix-VM590zVqzSHdPNDf_l5u3JFu9MILFMHar14iQQ4aSfjfXV04E9x7UDiRlFO39qrvl0PLGa1RDVbv5WwhbNPmOX8citYuQVf9AgQ55rs0XSCBxeEabIp05ACII1oUtr-DJmSd_2g1lhTvpWDiMGfaYTTAZ5xhprwxzjxUETZUqIdrgtMi0mQAbwyMekalyQ5qx1upItqR2mqwMWNswakq3Zxge2JAaM2CSB5jgOqHaxSy6NnrAmmOSE3I5pCcvbDf0or4sRyHtXQau3Nzt9TrkwoxehRta8h72mHpnEPD2cEmMEPt9OTZgwMI0P99haT5h6JKlIbMZzH5ASO9_xPS1HDbtb4KmUcmykF3Tiijl0y7AP5MtYcML01HEAPqQ8ZEoVOQ5GupKeQbYChwuudBXUGtrvo8Q3huVnm0rRWY8bnq6tbLzJDl88xUcaFLzpP1O-W8NGs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98195db8f9.mp4?token=KRpLulGPYvaKNa_Py33ALIRzbgjV1sSUC8HXv_xJu2lZZgHh2I3TOBsJW_RMcFWYxfnRbHOIO7d6K7GJZYNQgKcNEyKWV8KwGzvlgnw4X-S2Vlo3RiU26QtRrfL1kABVYvTzp00b9GdjTqjVzRz2mKtagMrfznTQADdhdQAITBCDsGduHUebSoMnCX75N1m47sStIvhM5p4Oa_5fHSEwrGZO-_ainfJ5jix-VM590zVqzSHdPNDf_l5u3JFu9MILFMHar14iQQ4aSfjfXV04E9x7UDiRlFO39qrvl0PLGa1RDVbv5WwhbNPmOX8citYuQVf9AgQ55rs0XSCBxeEabIp05ACII1oUtr-DJmSd_2g1lhTvpWDiMGfaYTTAZ5xhprwxzjxUETZUqIdrgtMi0mQAbwyMekalyQ5qx1upItqR2mqwMWNswakq3Zxge2JAaM2CSB5jgOqHaxSy6NnrAmmOSE3I5pCcvbDf0or4sRyHtXQau3Nzt9TrkwoxehRta8h72mHpnEPD2cEmMEPt9OTZgwMI0P99haT5h6JKlIbMZzH5ASO9_xPS1HDbtb4KmUcmykF3Tiijl0y7AP5MtYcML01HEAPqQ8ZEoVOQ5GupKeQbYChwuudBXUGtrvo8Q3huVnm0rRWY8bnq6tbLzJDl88xUcaFLzpP1O-W8NGs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أَعِرِ اللهَ جُمْجُمَتَكَ، وَاضْرِبِ القَوْمَ بِسَيْفِكَ، وَانْظُرْ إِلَى أَقْصَى القَوْمِ.
جمجمه‌ات را به خدا عاریه بده، با شمشیرت بر دشمن ضربه بزن و تا دورترین نقطهٔ لشكر دشمن را بنگر.
We ready to make one of the most biggest fire party in the world</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86845" target="_blank">📅 22:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86844">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
‏س: هذه هي المرة الخامسة على الأقل التي توقفون فيها الغارات الجوية على إيران منذ أبريل. ما هي رسالتكم للشعب الأمريكي بشأن ما تغير هذه المرة؟  ‏ترامب: حسناً، لا أعرف. أريد أن أمنحهم كل فرصة أخيرة قبل قطع رؤوسهم.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86844" target="_blank">📅 22:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86843">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA51KUn9QAGv6Nb7URt38u2ZEP-ZewOkJxyUJZrDkppW9J0uk-kYcrWQTsVrDm7gv0BZdRvDcHM7dKnNW4jJrNFhi-of__tHAXeTxi_EndlMlAtVnkuBfdWllO0ZzfckXq4AHsO0VECVmlFyi4fIvXllJRsy3gBFGDdcDNNZD8sOZ81qfsWl_WpQ-KdSkhsLS6GkLKtGNI4jUFL5uiatg4ysR54PoLmRmLLpD9wuwUj_rCPVIwJmYIFmanAhSL7aBe2uTDASOhTBetPC7ZzdOhNk2LLshYRQ-yYyM6q_Uqw0ehdHC2GqPzAs0RmuQi50uKtAY7AzJpBHBqwHiOCcHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏س: هذه هي المرة الخامسة على الأقل التي توقفون فيها الغارات الجوية على إيران منذ أبريل. ما هي رسالتكم للشعب الأمريكي بشأن ما تغير هذه المرة؟  ‏ترامب: حسناً، لا أعرف. أريد أن أمنحهم كل فرصة أخيرة قبل قطع رؤوسهم.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86843" target="_blank">📅 21:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86842">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
ترامب حول الرسوم المفروضة في مضيق هرمز: لن أسمح لإيران بتحصيل أي رسوم، إذا كان هناك من سيفرض رسومًا، فسوف نكون نحن، لدينا سيطرة كاملة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86842" target="_blank">📅 21:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86841">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇹🇷
سفينة شحن تركية كانت متجهة إلى روسيا تتعرض لهجوم بطائرات مسيّرة في البحر الأسود.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86841" target="_blank">📅 21:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86840">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b23deb7a.mp4?token=gou7lxQ3iARpVuhLwk1yzGqmXSKamtPUsj7LvsovnVQhjBey4YnOJAHN_pLH9PSWq8s_3OlnB6iHieSQV0C_G_upGNzghriJmnX5FFJbsdkcGZjwE_Olmrk4OR8m6ya71zh618v3QdyfMEsr3vULbOb8LRb2_NJp7gPW8PgenO_QIftxFmvmATktIxFQtqOYcxLDPG4mycZc8neQG3-xDfTpCSAJB3u2jITObKWw-aYwS7yvIClknCO2gY2MyQlBl3gQrE6_NkIuehMgl2KZqcGn7S383kNe1NApR7fJekui2QwFjaVkERlNxh04ccGV7uapIs6eaFCXQNt-UpLcyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b23deb7a.mp4?token=gou7lxQ3iARpVuhLwk1yzGqmXSKamtPUsj7LvsovnVQhjBey4YnOJAHN_pLH9PSWq8s_3OlnB6iHieSQV0C_G_upGNzghriJmnX5FFJbsdkcGZjwE_Olmrk4OR8m6ya71zh618v3QdyfMEsr3vULbOb8LRb2_NJp7gPW8PgenO_QIftxFmvmATktIxFQtqOYcxLDPG4mycZc8neQG3-xDfTpCSAJB3u2jITObKWw-aYwS7yvIClknCO2gY2MyQlBl3gQrE6_NkIuehMgl2KZqcGn7S383kNe1NApR7fJekui2QwFjaVkERlNxh04ccGV7uapIs6eaFCXQNt-UpLcyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
تضهر صور في الاقمار الصناعية تضرر محطات ومصفات في ينبع اثر الهجمات الاخيرة التي شنها انصار الله في اليمن.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86840" target="_blank">📅 21:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86839">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ab223602.mp4?token=PKYg8z8p2SstvK6_q7r1VmSCojHjAaEYSQYKYpxAEDEjFawqCQjHjvx46ymY9uv8ZIxKT-XBnyLPs-nsHjth6ALO2-FwiEkBUGCLjD64qMaLiFw9c2e8Ke7KNs7BqzwwELzdcPklLcJoteEKaIvBbBcUJb5fbrF1P8jvLrj0DyB9wJ4j_gUUgyeXr5YwvpC_Ynj3WeKVnro5wGV4s-kIbh5aUjUr2Due-A1pR8hvs-yTqrWxbGXCA9fD4qOS2cewAmYoWBJNclUGWYAvHteE1yVGxpF_0BYUqnqVv9kFh6HGMGuo9bhr-zSPKjAS46N2SY5lEzJR1Nqa0haJpuQcZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ab223602.mp4?token=PKYg8z8p2SstvK6_q7r1VmSCojHjAaEYSQYKYpxAEDEjFawqCQjHjvx46ymY9uv8ZIxKT-XBnyLPs-nsHjth6ALO2-FwiEkBUGCLjD64qMaLiFw9c2e8Ke7KNs7BqzwwELzdcPklLcJoteEKaIvBbBcUJb5fbrF1P8jvLrj0DyB9wJ4j_gUUgyeXr5YwvpC_Ynj3WeKVnro5wGV4s-kIbh5aUjUr2Due-A1pR8hvs-yTqrWxbGXCA9fD4qOS2cewAmYoWBJNclUGWYAvHteE1yVGxpF_0BYUqnqVv9kFh6HGMGuo9bhr-zSPKjAS46N2SY5lEzJR1Nqa0haJpuQcZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: نتحدث مع ايران لفتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/86839" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86838">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
ترامب: "كنا سنهاجمهم بقوة بالامس. بقوة كبيرة جدًا. بقوة أكبر من أي هجوم منذ الحرب العالمية الثانية."</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/86838" target="_blank">📅 21:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86837">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
ترامب: نتحدث مع ايران لفتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86837" target="_blank">📅 21:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86836">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad669497cf.mp4?token=jHYW9mGO-d6wUOkulJzW22J86TW1LgsnRGpumQd8NuPjOBuFmKlNGJT5boSzblTCmFcxblg39xUjbvC_b_sPf9R54JBwN52ohptsWfphyCEt2-Jt4SL5UNEaHN5CAmInoiqSC8Bd50BGw3PuqPKt4q0ksvHbtEpq__mGNT7o2dg_jStMJU9Vz3p7lAFomKxvgcmIxkRxNFqwEUgqiUeIPgSuDx4qE5d3YkPRyZ6kACJixhgNNbfCYUJno7az8uD_2jf15eNtqxljRnsYS9n6d7qk5nxQ7AFKtVNuX1Q1sCKdJgvgGARLeNWoIEIiT56p17vkjANeCXiKyHGvrDvv64wH9WrP-Clz5jpevqSiAZRoLj0LDxNq1wQ9PFIkwMYO0J_uQp-VpdBg5FbBTMXIjmzcneoIGfDfdKgHEMsxf-ZpgRB_2WS1HW9wek3uCKl2l2AJ379nTIWWpd5ZJBiIDItB481J1p0LN3AIA0gPKx51BVmK-ztI_pp4sTMzNeXz-6hb7bXtsPpN_mj60fMqU9aZYrYrREP3TSbxPPruZY0UQ2Ylmr_Ov71j-HlZrP0oapGh9nFnRt1RT3sPHXC18NgxdvXDx_8PjYQ4JvSQGPeUt1VRfM2l0i0rld_vM0t02uVkzuqGeEthzkEPY0cWkd3wLyZH1PVqRGjOnXP4i4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad669497cf.mp4?token=jHYW9mGO-d6wUOkulJzW22J86TW1LgsnRGpumQd8NuPjOBuFmKlNGJT5boSzblTCmFcxblg39xUjbvC_b_sPf9R54JBwN52ohptsWfphyCEt2-Jt4SL5UNEaHN5CAmInoiqSC8Bd50BGw3PuqPKt4q0ksvHbtEpq__mGNT7o2dg_jStMJU9Vz3p7lAFomKxvgcmIxkRxNFqwEUgqiUeIPgSuDx4qE5d3YkPRyZ6kACJixhgNNbfCYUJno7az8uD_2jf15eNtqxljRnsYS9n6d7qk5nxQ7AFKtVNuX1Q1sCKdJgvgGARLeNWoIEIiT56p17vkjANeCXiKyHGvrDvv64wH9WrP-Clz5jpevqSiAZRoLj0LDxNq1wQ9PFIkwMYO0J_uQp-VpdBg5FbBTMXIjmzcneoIGfDfdKgHEMsxf-ZpgRB_2WS1HW9wek3uCKl2l2AJ379nTIWWpd5ZJBiIDItB481J1p0LN3AIA0gPKx51BVmK-ztI_pp4sTMzNeXz-6hb7bXtsPpN_mj60fMqU9aZYrYrREP3TSbxPPruZY0UQ2Ylmr_Ov71j-HlZrP0oapGh9nFnRt1RT3sPHXC18NgxdvXDx_8PjYQ4JvSQGPeUt1VRfM2l0i0rld_vM0t02uVkzuqGeEthzkEPY0cWkd3wLyZH1PVqRGjOnXP4i4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حيث نتحدث حاليا عن فتح مضيق هرمز بالكامل.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86836" target="_blank">📅 21:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86835">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085519ec4b.mp4?token=elK-0IAqLCezzrDI8gZNP2nZaqfuB5uO6zcKPrpTa9zw2vzt13HsMcuLMbLUGXpgSY8gg6iMeeN7IFUVm6vM6vdqSfWyO30y_s-6-0Iz0VhCr8SRWvF4p57lDwabqBUJjjfyrtONO0r2HaBBfN3T11PnC2YnaVwKQmTBf6AZE62_hm-EPYl6LjjYtF3MxTMbKkDgA-8MvC7CEZ11XKxG6NW7gj7e50_lbbXUMucXCEhAeJj4-5Bg2H4k51rMAc47X5ZEm_o4ocpdEM-34kFA7chl2DUpJpIMXIVLLCoknjXDmrVCjITiQPP4wIv4cQDjY2aTvxWNs3-audsoBec7Vn1YFO5Teqmuog59yeIJ56ivlHy83tMIO9kTbqz7h7JR55ZADQz0OBPCMq6Hmop04D5ndZx34WJM4ZDEGoyKBO8MlG6WYiDIyEanO8OF44YZMPkMRR_FPPPUTMciD3l9M_LK7T2rGIJizdkni32mCHhgubWSEeoKoG7soiCocbRx9mc1nXFlwQxPLo-OGddqHuy4K7dd2fR84C_IDwOvQGQ3zvm8m_juREVz3tr3hZw7nBJa__UxMwxcF4k8hgEPexSZSyNE4R-cCwYw3qVAXANmer88xiLR6Unw4u_0hjRiDcsyu513RyntosEdZ6Unps5yQ2Bj_kJKvkq4fkUZLTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085519ec4b.mp4?token=elK-0IAqLCezzrDI8gZNP2nZaqfuB5uO6zcKPrpTa9zw2vzt13HsMcuLMbLUGXpgSY8gg6iMeeN7IFUVm6vM6vdqSfWyO30y_s-6-0Iz0VhCr8SRWvF4p57lDwabqBUJjjfyrtONO0r2HaBBfN3T11PnC2YnaVwKQmTBf6AZE62_hm-EPYl6LjjYtF3MxTMbKkDgA-8MvC7CEZ11XKxG6NW7gj7e50_lbbXUMucXCEhAeJj4-5Bg2H4k51rMAc47X5ZEm_o4ocpdEM-34kFA7chl2DUpJpIMXIVLLCoknjXDmrVCjITiQPP4wIv4cQDjY2aTvxWNs3-audsoBec7Vn1YFO5Teqmuog59yeIJ56ivlHy83tMIO9kTbqz7h7JR55ZADQz0OBPCMq6Hmop04D5ndZx34WJM4ZDEGoyKBO8MlG6WYiDIyEanO8OF44YZMPkMRR_FPPPUTMciD3l9M_LK7T2rGIJizdkni32mCHhgubWSEeoKoG7soiCocbRx9mc1nXFlwQxPLo-OGddqHuy4K7dd2fR84C_IDwOvQGQ3zvm8m_juREVz3tr3hZw7nBJa__UxMwxcF4k8hgEPexSZSyNE4R-cCwYw3qVAXANmer88xiLR6Unw4u_0hjRiDcsyu513RyntosEdZ6Unps5yQ2Bj_kJKvkq4fkUZLTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: الفرصة الأخيرة لإيران لتوقيع وثيقة جيدة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86835" target="_blank">📅 21:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86834">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323354d999.mp4?token=l8gAvDZbQwmOl0TcfLa7U-3vLdBIGTwkgzEpEOchN-a9BZD92dxYsNtAWE4lB7zAfoFdwyFZOlOIjKna2OqaGX8mtMz4V5BucJ92TJjDFt0soT_v0uCcV4smsAbGhZYr0nGoSykPdcqVT7V9iS7jQPOXs9zdkcf8ZhthI_6wC-VkkT-2bIdktUmYcKwkoh9WZoLeUOOvYWvZUcUSxU7ZDBnrDSv501OL6wtqKI4-C3TfkOikZNs9qCmF1-AMQ0w6iTlTxeQKP_TpLL-JkuC9enRJ59RyED0ru7LwPCwzChi6MwF_NF7XLUnC2NvbljJj3PKZ-RdIkDcO_rtVl_qfe14VyYuwiNptriLxVh6ZNvFp4I8AHro3zgNVR1s01kTvplo8L_pekznMEz-qU333UCfhHKyqkarevTN0N_ot0qToMtsZTRJtHE7bV-hTl642A_VIPrGuO6l_Iy2gAV-g9wBC1cM7HvSrstlX7vf2cIb-a7jFpG-PSNaSJ1nJ65GjX6EyZ-UtHVpLRD_ntQng_So9snP0nRObo53QZWR5pGPoNH_IGHcRCgH-QcCL9L1jiWq6A7gRU9gKJ5-L_nvv5cdJJZYU71Kwv7_Z7vxINow2pyA9Q0F6vYVlU07h2DIVLb2b7aH6ALRPQSG7d1UbI9PYgVqk9rRqVnwv4elDURg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323354d999.mp4?token=l8gAvDZbQwmOl0TcfLa7U-3vLdBIGTwkgzEpEOchN-a9BZD92dxYsNtAWE4lB7zAfoFdwyFZOlOIjKna2OqaGX8mtMz4V5BucJ92TJjDFt0soT_v0uCcV4smsAbGhZYr0nGoSykPdcqVT7V9iS7jQPOXs9zdkcf8ZhthI_6wC-VkkT-2bIdktUmYcKwkoh9WZoLeUOOvYWvZUcUSxU7ZDBnrDSv501OL6wtqKI4-C3TfkOikZNs9qCmF1-AMQ0w6iTlTxeQKP_TpLL-JkuC9enRJ59RyED0ru7LwPCwzChi6MwF_NF7XLUnC2NvbljJj3PKZ-RdIkDcO_rtVl_qfe14VyYuwiNptriLxVh6ZNvFp4I8AHro3zgNVR1s01kTvplo8L_pekznMEz-qU333UCfhHKyqkarevTN0N_ot0qToMtsZTRJtHE7bV-hTl642A_VIPrGuO6l_Iy2gAV-g9wBC1cM7HvSrstlX7vf2cIb-a7jFpG-PSNaSJ1nJ65GjX6EyZ-UtHVpLRD_ntQng_So9snP0nRObo53QZWR5pGPoNH_IGHcRCgH-QcCL9L1jiWq6A7gRU9gKJ5-L_nvv5cdJJZYU71Kwv7_Z7vxINow2pyA9Q0F6vYVlU07h2DIVLb2b7aH6ALRPQSG7d1UbI9PYgVqk9rRqVnwv4elDURg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏المراسل: المحادثات مع إيران توقفت الآن.
🇺🇸
‏ترامب: إنهم مستمرون الآن. إنه أمر مذهل.  ‏إنهم لا ينكرون ذلك هذه المرة.  ‏لكن لسبب ما، عندما يتحدثون، لا يحبون أن يقولوا إنهم يتحدثون.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/86834" target="_blank">📅 21:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86833">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167ef831e7.mp4?token=k067mk6MLyvX56cWoReJR_vS5gCcywa7j17Vqpq58ZJ0iBQbLNw9TTmNJhA70XVbHpJ3UP4Gi9c5LZnNu6jVpEnf1POd53Ds_JaLPMo4RTINZAhOega8k-afIJQx8nH0-0gtCK0o9GVABAM0snKbdP0Ho5IHO-go7vEaV1u31hgdGmeawgCzl4i_x1WfWq7T8B3AJrWNld34IdkY280Ohu3Z775zl_Bi0OrbQdBTsVxp22cdYEuitRnBNi2mabBL6U1oUGeHkjwG5F-JPiPhYiv9oQtgqG1K1YI1U_Ra0PFExpUcgLyWw7C335_V3KZRFpBkQEw9Xtj4oUt-uSDtiSyObkGdKVYNuTVjerq38FRidmPFW-0kxyslPeRQDvO4ipkTDKBDaBeoebHpNBZluK0MMBbIURfVZ0fLYVPkHXbNwpz1sl6PVzEUX8ARrIztXQqdQboP-LLNLrxkVhMaVkXGXj3bWp5vQKsZorsM9fRig5iRAabI-wnm7xjvJxugiDnVO_Xf7r4G5lCW67qKpQv1OHtWopP13XWgt4VX-JZEAXLdIEiZHUEw5IZvbNqeAGuDIOhGHR4AtydwjBDrzIJAQ3LunH_mbLgLoB8no2FAAnmS4MdHHXqTKC1PSVN3AO2IBVMqh0YUz2Zh53vaAGUNX7sP31wYN9mTBH2Oc98" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167ef831e7.mp4?token=k067mk6MLyvX56cWoReJR_vS5gCcywa7j17Vqpq58ZJ0iBQbLNw9TTmNJhA70XVbHpJ3UP4Gi9c5LZnNu6jVpEnf1POd53Ds_JaLPMo4RTINZAhOega8k-afIJQx8nH0-0gtCK0o9GVABAM0snKbdP0Ho5IHO-go7vEaV1u31hgdGmeawgCzl4i_x1WfWq7T8B3AJrWNld34IdkY280Ohu3Z775zl_Bi0OrbQdBTsVxp22cdYEuitRnBNi2mabBL6U1oUGeHkjwG5F-JPiPhYiv9oQtgqG1K1YI1U_Ra0PFExpUcgLyWw7C335_V3KZRFpBkQEw9Xtj4oUt-uSDtiSyObkGdKVYNuTVjerq38FRidmPFW-0kxyslPeRQDvO4ipkTDKBDaBeoebHpNBZluK0MMBbIURfVZ0fLYVPkHXbNwpz1sl6PVzEUX8ARrIztXQqdQboP-LLNLrxkVhMaVkXGXj3bWp5vQKsZorsM9fRig5iRAabI-wnm7xjvJxugiDnVO_Xf7r4G5lCW67qKpQv1OHtWopP13XWgt4VX-JZEAXLdIEiZHUEw5IZvbNqeAGuDIOhGHR4AtydwjBDrzIJAQ3LunH_mbLgLoB8no2FAAnmS4MdHHXqTKC1PSVN3AO2IBVMqh0YUz2Zh53vaAGUNX7sP31wYN9mTBH2Oc98" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: ‏عندما تتحدث إيران، فإنها لا تحب أن تقول ذلك، والمحادثات مع إيران جارية الآن، حيث نتحدث حاليا عن فتح مضيق هرمز بالكامل.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86833" target="_blank">📅 21:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86832">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
‏ترمب: الصراع مع إيران يسير على "نحو جيد للغاية"</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/86832" target="_blank">📅 21:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86831">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
‏
ترمب
: الصراع مع إيران يسير على "نحو جيد للغاية"</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86831" target="_blank">📅 21:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86830">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
رئيس شركة "سومو" العراقية:
تبلغ ضريبة الجمارك على نقل النفط الخام عبر تركيا 1.62 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86830" target="_blank">📅 21:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86827">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQnc3yLsNMCkPqUcMpaPYzBn-4i_asqtrzyCfC75Hw-QLEfAoBGZzA-h2esJ6bKNk0QUV3soOlMTmoePtzjVkgCLaUDNQPCwAbSR0lLnxW33K59-ip_TDUczFOoZ1qGyz5V26UdzUuk5yIGg_MgaVaowJuqBiwVdAOBSj-xIVd1EprQbXsjV_c_4-TL_ZSKLez8G2IUu3QKWkD59kCr23rwE-11vmp1xbS6XPMK2PA_xV6cDCC4JUmZluYH11UZVrN35hh5pZfJsSKM2xRS3QnovHJQ_rYn0s1Ssi7S6NhCE60fmCjqTI03nU93PF9-EPUdoS6bYUlmlJBRD587Kqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgOYE7MzOsaQKWtTdkmW2Q-wj8-_FMaeDFHaRFpHiWj91UL_WVphHm3Qtk5RJ59EEbMMhTWO4zTtDiCsgpf-_IEe0duUc88jyI-uSRsTbs2QQUzfKSVpD84hC4O8sgL1_qjlfGZVmkmkqMaFqcKhK2qKM5JY1SkPZrWsGch1L_HrvM7zFYdN92hdapNU0kiscgl1B2dX1_WDlBpTi8hekDH3GbqfyjDXaW5Nr-sm25c9NoYGGaUPWLEY8puoZd4NbCQL4I8T7yqas5w1jW_mpsk_i2Ex4Lh5NLi263RU5gf5tt7vxlBb6C0p-hNTb-Hh7a9P-V_e701uVEOSCnwBrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCHbM2nDM__aMi5CIOEDrH0AEgLkF9ze0GTCG3A_QykKsOr-atB83N0dwR73xB0EGczaJzFkSoKb4XJnIkndlfYJPwEZMI5JkDRDdpbOQMpwKQ-ApM7xJgxSVgA9EM8frMmC-mbuDTn23rpYuTz9EEd2MOB6ISjZ6WcrKCHtfYfpHPXe7aZSmM9ZjS8Dj442AUcpzK_U7IbJXEsMBrLLWbamQy3n0Rek1hL9rCAGyhTw_JMcXCKYodtMuxvhuCCoFDBT-xWbszwwYORTYdIRovxNfkn_q3dJgAjcc7AbhU-qbVXjUH4qptED8NWejPwcRGICrHtRKqTkJDc4mKHgsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">المواكب الحسينية التابعة للحشد الشعبي تستعرض بجرائم ال سعود اتجاه الشعب العراقي في محافظة كربلاء المقدسة
ال سعود ظلمة</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86827" target="_blank">📅 21:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86826">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqAVQTsp9wSs6sXwPve4W_5FfAZC6zENDe1zZ9b4XiP9zstbm6rszCvP6zlj1NG4f6ALeo1UM3D9KMS_Wexy7NxhllXMOexTco2AHae-9L-dGXRWOe-zWYLajDqoEFdrEV0tnoxn3AvaJqH8TwbWNT4N26Rm9HRPj5gJqTVvaE4TFhZhp9utgPHCUa8iktJCpxV_gp8np7oRZLHSftW4gBRD0KeEnRtlK3NqHWHtLO0-JlRgkqMerYiey28_QxLFbuIK0bUt72Hwz5pdfeT36RGssy8a8yAekbEhOmIoic6Hdd_w46DJxV3xmTetcFTOUyVr_ebWgV8aFt7HdehqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مروحي عراقي تحت إشراف أمريكي في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86826" target="_blank">📅 20:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86825">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
إعلام أمريكي : تم الإبلاغ عن أول حالتي وفاة في الولايات المتحدة لأشخاص أصيبوا بمرض داء السيكلوسبورا في ولاية ميشيغان.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86825" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86824">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdxKmCtb5QrGduiIlQQgJL792Brv6eiAJcda4KlSSU8lwf9rW5qvCvO4c_eUScGuWqrzvxQaD393Zmb-uDJPnYnB5zCx5HJQNTcBBaOXcNweWMLGxTAYjrN2R6ZCXaz-Cyncs4wM8PdYHTJQFEmLqWMm18agupjTscmSlUAZSQxNyfsyrtaXUen6qdX3y1barP_0MbtfwFwuO0GhNG9jWxM8qW5PZ0VtRizjDeKyxaIB43ZH2aEFziqpd4fYzq9oyPVVfVWomMcttUdES4k1LnwoCQyyIptI8vVgx52Stxh-oH0RUCNKKO9ne1l7YOxyEwrNE5Q5DAUuFwOPuZFcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فيلق بدر متمسكون بالسلاح ..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86824" target="_blank">📅 20:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86823">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXJulUB35TQ2a8rl1TAS2jLQ5Yepuwdz5HWmd9VVHi-Xke03eKvhVRr_yUrC_GZGz_2ihnW-4AMcbTSC48yfr_B0pRKLH5NolYc8CgRnMgUZYGrv3vjeSX-WXNuYuo7w34oydVtU9NdbbPZemajvYP5a_K_4-xse-rs6LW7pBxtcSRwtfE7H1xEFoaMJuHs4un7masSwLTZjeUKF7IYmy9w1aDkKPPACDq6o483qwOpxM90xC1f_y11iN9UJCid0ukOSBgduFtQYO9ukg2VzY7OE7CWciVSF0iBTZHb54h_NDlqfEsXCnK0XoN2ev8Ph32wTZcVW6sUapVP6tej0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
﴿وَلَيَنصُرَنَّ اللَّهُ مَنْ يَنْصُرُهُ ۚ إِنَّ اللَّهَ لَقَوِيٌّ عَزِيزٌ﴾
الأمانة العامة
للمقاومة الاسلامية في العراق
كتائب سيد الشهداء</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86823" target="_blank">📅 19:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86822">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
الأمين العام لكتائب حزب الله الحاج أبو حسين الحميداوي: بسم الله الرحمن الرحيم (ذَٰلِكَ وَمَن يُعَظِّمْ شَعَائِرَ اللَّهِ فَإِنَّهَا مِن تَقْوَى الْقُلُوبِ)  الحمد لله رب العالمين، والصلاة والسلام على قائدنا ونبينا محمد الأمين، وأهل بيته الطيبين الطاهرين،…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86822" target="_blank">📅 19:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86821">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇶
الأمين العام لكتائب حزب الله الحاج أبو حسين الحميداوي:
بسم الله الرحمن الرحيم
(ذَٰلِكَ وَمَن يُعَظِّمْ شَعَائِرَ اللَّهِ فَإِنَّهَا مِن تَقْوَى الْقُلُوبِ)
الحمد لله رب العالمين، والصلاة والسلام على قائدنا ونبينا محمد الأمين، وأهل بيته الطيبين الطاهرين، ورضي الله عن صحبه الأخيار المنتجبين، وعباده الصالحين والشهداء والمجاهدين.
السلام على الحسين، وعلى علي بن الحسين، وعلى أولاد الحسين، وعلى أصحاب الحسين، والسلام على الإمام الخميني المعظم، مؤسس محور المقاومة والكرامة والخير.
لقد انقضت سنة كاملة منذ أن عصفت بأمتنا أحداث جسام، حين شنت قوى الشر والظلام حروباً إجرامية على شعوب المنطقة، فسفكت الدماء، وروعت الآمنين، وخلفّت عشرات الآلاف من الشهداء والجرحى، ممن نحسبهم من خيرة المجاهدين وصفوة المؤمنين.
لقد جسد أولئك الكرام، ببأسهم الذي لا يلين، وثباتهم الراسخ، وذوبانهم في ذات الله تعالى، السيرة الخالدة للخُلّص من أصحاب رسول الله (صلى الله عليه وآله وسلم)، وأمير المؤمنين، والإمام الحسين (صلوات الله عليهم أجمعين)، فكانوا امتداداً حياً لمدرسة التضحية والفداء، ورمزاً للعزة والإباء.
وكان من أعظم ما أوجع قلوب أحرار العالم خلال تلك الأيام، ارتقاء إمام المجاهدين، السيد علي الخامنئي (طاب ثراه)، شهيداً، بعد أن أفنى عمره في نصرة الإسلام والدفاع عن المستضعفين وقضايا الأمة، فغدا دمه الطاهر عهداً متجدداً يبعث في النفوس روح الثبات والصمود، ويستنهض في الأمة معاني العزة والإباء. ولم يكن خروج عشرات الملايين لتشييعه مجرد وداع لهذا القائد العظيم، بل كان تجديداً للعهد والوفاء لنهج رسول الله وأهل بيته (صلوات الله عليهم أجمعين)، ومبايعة للنهج القويم، ومواصلة الجهاد في سبيل الله، وردع كل معتد، ليدفع أثمان اعتدائه مضاعفة، لا سيما ما ارتكبه العدو الأمريكي السعودي من جريمة بحق أبنائنا، في سابقة خطيرة تنذر بتداعيات قد تؤسس لمرحلة جديدة في المنطقة.
وإن ذلك مُدعاة إلى تمسكنا بسلاح المقاومة، وعدم التفريط به، بل تطويره وتعظيم ترسانته، والسعي لتنقية فضائنا الأمني، مع التشديد على ضرورة الالتزام التام بالإجراءات الأمنية وحفظ الأسرار، بما يتناسب وحجم التحديات، لردع كل من يريد بنا شراً في حروب هذه المرحلة؛ تلك الحروب التي لم تنفك عن مواءمة الجهاد العسكري مع الجهاد الإعلامي لمواجهة الأعداء وأذنابهم ببأس شديد وثبات لا يتزعزع.
ونحن على أعتاب ختام مراسم زيارة الأربعين، نكبر ونثمن الوعي الاستثنائي الذي تجسد في مسيرة زوار أبي عبد الله الحسين (عليه السلام) وحضورهم الكبير هذا العام؛ حيث تجلت قضايا الأمة الكبرى في وجدانهم وفي مقدمتها القضية الفلسطينية، معبرين عن سخطهم على أعداء الأمة والإنسانية من قوى الاستكبار الصهيوأمريكي وأذنابهم في المنطقة، وقد زادوا بفعالياتهم تراث الشهداء إثراءً وخلوداً، فشكراً لجحافل الزوار، وهنيئاً لهم هذا الحضور والارتباط النوراني، وعظم الله أجورهم وشكر سعيهم.
وفي الختام، نتقدم بعظيم الشكر والامتنان لإدارة العتبات المقدسة على الجهود الاستثنائية التي أذهلت المتابعين وأصحاب المواكب الحسينية، وكذلك لإدارة محافظة كربلاء على جهودهم الجليلة. كما نحيي باعتزاز سواعد المجاهدين، ويقظة الأجهزة الأمنية، وأبطال الحشد الشعبي، الذين كانوا حصناً منيعاً لتأمين الطرق وخدمة زوار أبي عبد الله (عليه السلام).
(سَلامٌ قَوْلا مِنْ رَبٍّ رَحِيمٍ)
الأمين العام لكتائب حزب الله
الحاج أبو حسين الحميداوي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86821" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86820">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9ffea580c.mp4?token=hjyD8GIjA32I0yLk5WL0R-fnYV_kQlWSZSKIKFD3t1aEA7Gle4Zk5OXtJFphBm7ea9GOoo02ulOSRBmiVcnWa0D1z7qyfv4BhRUOxpBiu2u_LR0fsQaI3cFlQmLxiVqKfXZjXBWlFsijDjs6enGCN4aOBkyQtRkYuqfnCEX-sucb9XM6onk7OTlQyzcR-0n9_IlZPYHZ2WMrI-hy3u8P-qoa8YNiF4Re8WjY4sWTmUut8enpsamZzSmS2o2YVwHysDXLgaY9TF4h5UxYAGPFzGNC9ZrdI4EnULlbbN76cdx5TxPFz-fl6sV7biHCUFOHctxvrf1SJywGpj0lxlL5NDMAv3KPqL_5KDpCCSS0bnZxpxe8Q6hOywt3RjaJRjUlJsI0S1WfK7i3Kd3sXs0H1n-BZ77h-pjcEQFWRr-xMK7MvFO6fVM2UaLhAJKShPUfAqJ9sLzl5lezNMGUujytJUeArqdliMJMoa7zQLzmfUnMuJp56zUh4JFzBPKD_lMXAAOpJ7DNCjyq-j-zK2llPtujLXLKJVqCBjXNPSKqBxDhG8Dul_upsHB1F_w4aVAm_ZpDB7g6jZ6pHMVwFVuJc2Aey5c9zXfMo8iWGxp6q4Y5IZhwBAWfFIONs5rGOuqBV018IGrYBKFtJLn86_nxxLomJ3dACnOy_3ZkDBS-aN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9ffea580c.mp4?token=hjyD8GIjA32I0yLk5WL0R-fnYV_kQlWSZSKIKFD3t1aEA7Gle4Zk5OXtJFphBm7ea9GOoo02ulOSRBmiVcnWa0D1z7qyfv4BhRUOxpBiu2u_LR0fsQaI3cFlQmLxiVqKfXZjXBWlFsijDjs6enGCN4aOBkyQtRkYuqfnCEX-sucb9XM6onk7OTlQyzcR-0n9_IlZPYHZ2WMrI-hy3u8P-qoa8YNiF4Re8WjY4sWTmUut8enpsamZzSmS2o2YVwHysDXLgaY9TF4h5UxYAGPFzGNC9ZrdI4EnULlbbN76cdx5TxPFz-fl6sV7biHCUFOHctxvrf1SJywGpj0lxlL5NDMAv3KPqL_5KDpCCSS0bnZxpxe8Q6hOywt3RjaJRjUlJsI0S1WfK7i3Kd3sXs0H1n-BZ77h-pjcEQFWRr-xMK7MvFO6fVM2UaLhAJKShPUfAqJ9sLzl5lezNMGUujytJUeArqdliMJMoa7zQLzmfUnMuJp56zUh4JFzBPKD_lMXAAOpJ7DNCjyq-j-zK2llPtujLXLKJVqCBjXNPSKqBxDhG8Dul_upsHB1F_w4aVAm_ZpDB7g6jZ6pHMVwFVuJc2Aey5c9zXfMo8iWGxp6q4Y5IZhwBAWfFIONs5rGOuqBV018IGrYBKFtJLn86_nxxLomJ3dACnOy_3ZkDBS-aN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🔻
عدسة نايا - تصوير درون
بين الحرمين " من سرباز قاسم سليماني "
19 صفر
#شاركها</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86820" target="_blank">📅 19:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86819">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏
رويترز
: مخزونات احتياطي النفط في أميركا عند أدنى مستوى منذ 1983.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86819" target="_blank">📅 18:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86818">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAd8OL2XBGrmskPROivFN4lsoteUU5xTm4_iFc6AgPu9dFXzJTpQsTXztoFfc9mjUgrNJmYPKKlxzQ1abBUY6pLvOaOeOTmOmRz1tM_pX22TRNc2nA79rXb5rj-w1g797-oqkkNpIpFwpjJflYKEUgIwYbV9QZtPN0awQ7BoM0BFjlXEIIlGETCl5grEY1esns6a9X-z2-Rabbfw8cGufh4pwRcfBEkFvfzSVANNd-M2TTZhOjJQyO0AB72I39F2e43vKMQNO6yRr64KpV6Z10kFJS5_jGvNhw2zrfQvfibGLVqsOQV6e8Ec5ycI1EZV5wq5XmLh2FFyP5FX71T_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
القيادة الإيرانية مخادعة بشكل لا يُصدق! يطلبون اجتماعًا، بل قد يقول البعض "يتوسلون"، وتبدأ المحادثات، مع تحديد مواعيد لمزيد منها في المستقبل القريب، ثم يقولون، بكل فخر واعتزاز، إنهم لا يُجرون أي مناقشات، ولا يُناقش أي شيء، وأنهم يتعاملون فقط مع "عُمان". ثم يُطلقون ثرثرتهم المعتادة قائلين إن مضيق هرمز سيُدار بقوة من قِبلهم، بينما هو بالفعل تحت سيطرة البحرية الأمريكية بالكامل و"حصارنا" أو كما يُسميه البعض "جدار الولايات المتحدة الفولاذي"! لا شيء يصل إلى إيران، إلا إذا أردنا ذلك، ولن يصل شيء إلا باتفاق أو استسلام كامل. سواء أرادت إيران الاعتراف بذلك أم لا، فنحن في الواقع نتحدث عن حل لمشكلة تسببت بها لعقود. الأمر بسيط للغاية، إيران لن تمتلك سلاحًا نوويًا أبدًا! شكرًا لاهتمامكم بهذا الأمر." الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86818" target="_blank">📅 18:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86817">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇶
رويترز:
ناقلة تحمل مليوني برميل من النفط العراقي تعبر مضيق هرمز متجهة إلى الصين</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86817" target="_blank">📅 17:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86816">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سماع دوي انفجار في دبي</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86816" target="_blank">📅 17:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86815">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجار يهز الامارات</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86815" target="_blank">📅 17:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86814">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجار يهز الامارات</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86814" target="_blank">📅 17:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86813">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📰
أكسيوس:
الممثل الأعلى لـ"مجلس السلام" ملادينوف التقى نتن ياهو وأبلغه بضرورة وقف الهجمات على قطاع غزة.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86813" target="_blank">📅 17:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86812">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
‏
ترامب:
شركات النفط.. واخفضوا أسعار النفط للمستهلكين، الآن!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86812" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86811">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
🔻
لوحةٌ عملاقة بمساحة 2500 متر مربع تتوسط المنطقة بين الحرمين الشريفين، يرفعها الحشد الشعبي حاملةً صور الشهداء، تخليدًا لذكراهم ووفاءً لتضحياتهم</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86811" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86810">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوي صافرات الإنذار داخل السفارة الأميركية في المنطقة الخضراء</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86810" target="_blank">📅 17:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86809">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HG5lklIwhn3QqHVumOXxwyi7rBKRKPFo5LCToIqj73wYDqEYmolxPWpo7tilOvuKChZgrf4OjAlCvvEvmluLJYJVD7SET-3Z45SKSrKaeuECzS0VXwf_m92azbmnixxC8pFfdOCTEMRKNnfwmw7M4BkDpQeeg1aPvKpQAgJvlooFxShkYaQsJ_fleSZebLp7DSJPrZ-4V2Qk3qObf1G23gCmhOdUAmKJb9tAgMC7S9nRRoiYedckB4hxap17uZ5f529eP7PH0vc3ZnOdweLyDaM-kSygMaz6IBmHNaCE9uH6MCB1e7t-WiGbti2qK2E6JBaljCvygmzoFwDb9X-c2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
بمساحةٍ تبلغ 2500 مترٍ مربع، هيئة الحشد الشعبي ترفع أكبر بوستر يوثّق صور الشهداء في منطقة مابين الحرمين الشريفين، تخليدًا لتضحياتهم، وتجديدًا للعهد على إحياء ذكراهم واستلهام قيمهم ومسيرتهم.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86809" target="_blank">📅 17:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86808">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAI8y9SCyEWsVGrW9zzAQXtz5tAT8Uprv5XSvjFhH8IwloB31OtfI-mSHAYV1WBtCBwLHSLtxBZulMWC3gTxQUKNW68hBYVtMcopjVNqtTfztfManeg0xWkxIavWFofAEsy_CxXoY1M896WxM33uFm-SBCmvkTPGkHk8AAEYI6tdCso6O-Hp-_tqCSzTAJ_yUwZyCsXPc2KPf7YnrgbvEMsRAJBP0dkdJdY_FCgYR14f5MWCzogNZrNhaP3ShWcC7rMuYF-NXOt0_Eyw8R6U_0AS6cRZD62l-0vCrXjJ5ovdQOhl47hTJFwHw2mfyFWles1N05Cs5FZ592G_NzLaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
بعد تراجع شعبيته كثيرا وفق الاستطلاعات بسبب الاثار الاقتصادية للحرب على الجمهورية الاسلامية.. ترامب:
إنّ استطلاعات الرأي الحقيقية التي أجريتها، وليست تلك التي تروج لها وسائل الإعلام المضللة، هي الأفضل على الإطلاق، فكيف لا وهي تشهد أكبر تخفيضات ضريبية وأعلى معدلات توظيف في التاريخ، وأكبر استثمار خارجي في أمريكا في تاريخ العالم، وحدود مؤمنة بالكامل، وانتصار ساحق في فنزويلا، ونزع السلاح النووي من إيران، واحترام ونجاح لا مثيل لهما في جميع أنحاء العالم، وغير ذلك الكثير؟ لا تصدقوا استطلاعات الرأي المزيفة التي يروج لها اليسار المتطرف. إنها فاسدة ومضللة، تمامًا كما أن الديمقراطيين الذين يدمرون البلاد فاسدون ومضللون. صوتوا للجمهوريين من أجل عظمة أمريكا!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86808" target="_blank">📅 17:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86807">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇵🇸
🇮🇷
رئيس حركة حماس خليل الحية للرئيس الايراني مسعود لبزشكيان:
نستحضر
الشهداء الذين ارتقوا منذ بدء طوفان الأقصى في مختلف الساحات على طريق تحرير فلسطين والأقصى ونعبر عن تقديرنا وشكرنا للمواقف الإيرانية ودعمها الثابت للشعب الفلسطيني، ونعرب عن املنا وتطلعنا إلى وقف العدوان على الجمهورية الإسلامية، وعودة الأمن والاستقرار إلى المنطقة برمتها.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86807" target="_blank">📅 16:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86806">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_5kicSvig-9lBvKlQhCFTHxom4WljcuMonrY4HidPje83YoNpj_yO95sO8cZz9eBfmebO1sIZRGsEb7zWk3gz6NS1FzisE_69GpKChB-ih3oWHhfvGPq8yLrRDBZZkLoVcDGmapo6e6uktjcUryJlgXkz2JgDHSODXA0KXHrym2P882tOrtP31jl1y5t-qM-QO_BQ4b6kfBUzrXQYv-fnFyWVa41Pqu0TIbe98JFDiMQ_QWJY_G-0TMm_Fm1Yg1IZo17OK_BGW_cedy5dQU6jOWr6vqZxD-HiAq3jM6TW1_cftVKhX70b-UOWxznXWf9dKo1kApGDYieb5KLmVWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
التهريب متواصل من سوريا
القوات الامنية العراقية تضبط كمية من الأدوية البشرية عددها (2,160) حبة من مخدر الأسنان مخبأة داخل عجلة قادمة من سوريا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86806" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86805">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الجيش الكويتي يعلن عن ‏تنظيمه تمرين للرماية بالرصاص الحي يومي الثلاثاء والأربعاء لاظهار قدرات الردع الكويتية وسط انباء عن قيام الحرس الثوري بتقديم اعتذاره للكويت والتعهد بعدم المساس بالكويت العظمى مستقبلا.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86805" target="_blank">📅 16:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86804">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc9490f89.mp4?token=E-gLzOlvXM8-P81sbhPMfsZkVBuxvYSlj2wXpYgEG7ezZf1cRsaX_sySrmWEL8ZYB43JoVuwW_JjT3Hz4nFD9ejBqQf6i2J0cO-VZkSl9shQzBxKQHNpGlzR5xqJm4aUm-lMCA3dkTEtAkOEkozoRbUwLGk57os1AM1pC49C9AsRZx4y4wIgGGAhMGPOJEa7jZB_sv01EAHD9fAwSDP1RE6P90r5QqCaHGZdxDVXjrkfTwjfKMkU0hzofNqv5xqgbz_3VGiHfQ56IFfszZaalz2uzdVVapyOiyk_dc6FrKIV3O74DWmiaEeBJPiWh7eeHSl-rANz_QqTHFenOV5Plg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc9490f89.mp4?token=E-gLzOlvXM8-P81sbhPMfsZkVBuxvYSlj2wXpYgEG7ezZf1cRsaX_sySrmWEL8ZYB43JoVuwW_JjT3Hz4nFD9ejBqQf6i2J0cO-VZkSl9shQzBxKQHNpGlzR5xqJm4aUm-lMCA3dkTEtAkOEkozoRbUwLGk57os1AM1pC49C9AsRZx4y4wIgGGAhMGPOJEa7jZB_sv01EAHD9fAwSDP1RE6P90r5QqCaHGZdxDVXjrkfTwjfKMkU0hzofNqv5xqgbz_3VGiHfQ56IFfszZaalz2uzdVVapyOiyk_dc6FrKIV3O74DWmiaEeBJPiWh7eeHSl-rANz_QqTHFenOV5Plg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اندلاع حرائق واسعة في الجليل الاعلى والكيان يستعين باعداد كبيرة من عجلات الاطفاء والطيران لاخمادها كما قرر الكيان اغلاق عدد من الطرق من بينها الطريق الرابط بين منارة ويفتح والطريق رقم 886 في كلا الاتجاهين.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86804" target="_blank">📅 16:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86803">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
🇮🇶
مشاهد من الحريق الذي طال مصفى بيجي بمحافظة صلاح الدين بعد انفجار داخل وحدة الهيدروجين.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86803" target="_blank">📅 15:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86802">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
🇮🇶
ممثل قائد الثورة في ‏حرس الثورة الاسلامية يصدر بيان بخصوص العدوان الامريكي السعودي على مجاهدي الحشد الشعبي:
.
لقد تعرضت قوات الحشد الشعبي الباسلة، التي لطالما اضطلعت بدور محوري لا مثيل له في تحقيق الأمن والاستقرار في العراق، والتي لا تزال تضحي بنفسها في ملاحقة فلول الجماعات الإرهابية التكفيرية التابعة لتنظيم داعش والقضاء عليها، لهذا الهجوم الظالم. ويُعدّ هذا العمل الإرهابي دليلاً على يأس وانحطاط أخلاق أولئك الذين يدّعون زوراً حماية حقوق الإنسان.
‏وكم نتذكر بجمالٍ أن هذه الأيام هي فترة الحداد على الأربعين، وقتٌ يسير فيه ملايين الحجاج على الأقدام بقلوبٍ تفيض حباً لكربلاء، ويهتفون بشعار "لبيك يا حسين"، وهم في الحقيقة يهتفون "الموت لأمريكا" ويعبرون عن كراهيتهم لجميع الظالمين في العالم. هذه الرابطة الوثيقة بين الأربعين والمقاومة هي رصيدٌ عظيم لن يستطيع أعداؤنا انتزاعه منا أبداً.
إنهم يعتقدون أنهم بهذه الهجمات الجبانة قادرون على كسر إرادة الشعب العراقي الراسخة، لكنهم مخطئون خطأً فادحاً.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86802" target="_blank">📅 15:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86801">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇵🇸
في ذكرى اغتيال إسماعيل هنية قامت مجموعة من الشباب في قطاع غزة برفع لافتتين كبيرتين في حي الرمال وسط غزة تحملان صورتي القائد الشهيد قاسم سليماني والشهيد إسماعيل هنية وقائد الثورة الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86801" target="_blank">📅 14:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86800">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
هزة ارضية جديدة في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86800" target="_blank">📅 14:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86799">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇬🇧
🫡
التلغراف البريطانية :
‏لا يزال شبح قاسم سليماني يطارد دونالد ترامب حيث تستخدم إيران شبكة الشيعة العراقية التي بناها سليماني لجر الولايات المتحدة والدول العربية إلى حرب أطول وأكثر تكلفة.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86799" target="_blank">📅 14:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86798">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFCq-6Y3y3cj12BzeQWywqlQVgcUGQDPh0B2ye0mxdRdVBxkJOhsmLC8ss94Rhj-uU84jbN2lL7ETAQbWN9A8tWDeqLl-HhYZ7uBfN3NFf4fdM3Ub2QrLh4HMPEk2gR2st0K2b_llWvdiBbXY2urHosuJtwWc2EEiV1m52L6ZeeupCY88o_pfHwmGb5u584X5aZUQ6QebLvf0W0kmSsiUGFgesBJkdSl680KArT4zGzc5ho_ASnB5xjnuyGjfESUkOZSPbWrVEMC9osZv3HczA8uyzgPmhFdnNaTY-YjExDhJhRKdDVc9J6lq2ZzlZ6jzmk2xbbTPxHcoA2BhV-sQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العلم العراقي وين ؟!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86798" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86797">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhB9yYMmRzdix8lyAJcPbwFxiDQMJhJQJyJNctZBOXwkLfMiQ_aaQaqH6pYyq7ePzG6XatUm2OGIDxhakhU9cfXANApCRxGqH_J9-DLjnozZApbkP4oimKUuCkq-2CEldYDVO8-0O0lYBv65X7MnvzqAbBw_lI1R0vIqUipX0Gpb7dPnPhWaYcBjYx29RJ7OuVAqZCGXSBWmTsGkTqqQQdKgYkNMvwpuTNo67BqpQnqmy18Si1V-CsXdjUcYE7oU9Xw0ejr_E37hh1Q-RAkGmHJfKiMIzXx58pDictVBCut4TDikD1d39BoHLzraWBNroA-FJhPX92Vaxgu6VGh1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
وصول وزير الخارجية الايراني عباس عراقجي الى محافظة النجف الاشرف.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86797" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86796">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وصول نيجيرفان بارزاني إلى دمشق</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86796" target="_blank">📅 14:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86795">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25f2d7dae.mp4?token=eXOxDd0m_s-QNYUMqLLbQw21J1bjRCdcBotCz9IJjGN6fcYXrO4W1616Qw7YcNCM0b6cY9OCrcur6IpCqfe-kxc2FbgyxE6k_rkEFD0Izv4b6UFReGgobzca5h4DzCkWXFI1Fj9yPQzS4VeRQNZtbXk4Yuxjg2K-P47dc0FXD26vpIBkJ36J7GoFIi7yNRf34ffjRfxRe6xNPUJvUPun4MdO6_MkYyKa5PRTdVnZH1UlQaIFJ45wEhDYL7s-LtXjD1H1N868IweTw6MntNXRJdFDV_7WwnoV8S2wt7LKTJc9a9y4X9xKQlfaZlYPjYx2rB97ETuBgoJXkuEQzIHTAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25f2d7dae.mp4?token=eXOxDd0m_s-QNYUMqLLbQw21J1bjRCdcBotCz9IJjGN6fcYXrO4W1616Qw7YcNCM0b6cY9OCrcur6IpCqfe-kxc2FbgyxE6k_rkEFD0Izv4b6UFReGgobzca5h4DzCkWXFI1Fj9yPQzS4VeRQNZtbXk4Yuxjg2K-P47dc0FXD26vpIBkJ36J7GoFIi7yNRf34ffjRfxRe6xNPUJvUPun4MdO6_MkYyKa5PRTdVnZH1UlQaIFJ45wEhDYL7s-LtXjD1H1N868IweTw6MntNXRJdFDV_7WwnoV8S2wt7LKTJc9a9y4X9xKQlfaZlYPjYx2rB97ETuBgoJXkuEQzIHTAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر لنايا: وزير الخارجية الايراني عباس عراقجي يصل النجف الاشرف يوم غد للمشاركة في اداء زيارة اربعينية سيد الشهداء (ع)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86795" target="_blank">📅 13:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86794">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
اعتراض طائرة مسيرة من طراز MQ9 وإصابتها بواسطة نظام دفاع جوي متطور حديث تابع لقوة الفضاء التابعة للحرس الثوري الإيراني وذلك في سماء مضيق هرمز.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/86794" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86793">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الاعلام السعودي: نيجيرفان بارزاني رئيس إقليم كردستان العراق سيلتقي الجولاني غدا في دمشق.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/86793" target="_blank">📅 12:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86791">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUpfTRndwM07jGHEU7G40vspOeE0GJjjkiU4gMWYwdMzUBzYFVqiot65vHZTdIQpS1fWHjr0rFDJ2jSfKRT-TBmqr4U5lQMY1wjtaTTmrFWMULEYFOAQw81-3-iKF2NvoupIVVSyxv9EVr87O_OcOGh4St3tXT0ZrP-X_wjufdhRlq-Iru4aWlvmLqR6PNuIzAERoHM_m6_L7XoSIBJ78fCchyzwQVk_zZh0TwMXUV2rnHbuV4_7myVweD5T61M66vZTUDQjlkpWykiHDwfY5hyFNI7cS8mfTfkBvHxOjRYaQN8yQapMVpSaRiU_TTAlu1euIPcZoVX_gAw2Rdck4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDUrEgRvTyDV5W3rKr0GDM6HZdyUdjnOcAtCJ2O9JsxlihbCMEpLyYNuFGtIYpe8Pm9PauA3n7hWH8kht-48B1WCoGpQ-JJrErTUnmaLwlkif-66Hrm27Rc3-SPC5vQubX9LypTCYlE_-dPjsfVEZTwSh_lCyEjS41-Nc8Joy4-s8gU8op18yuWAulCSHCCEyeFIRVHGAtIDCC3OuOpdMdPZQ7fgCSoe92nbNRTcqo_AmeHxassXtaO0fOd0Up6qTm0rpauoy4WesVUSb0vrpenYDl3kqTaZMzx6-qLf5Ui-S-vmiYyb_9eA19D_zON2vJdJ-SCd0ScdGg2ySBkTCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🇯🇴
🇦🇪
طائرة نقل عسكرية ثقيلة تابعة للقوات الجوية الأمريكية تغادر مطار العقبة في الأردن وتتجه إلى قاعدة سويحان الجوية في الإمارات.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86791" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86790">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33c71a96b.mp4?token=a0fdHCwDbEVYAMzS-fXyoOlJgyxpp1-Pd5t_ogbCfwiMUg8okGzxTKLp5LTWI59FcWeBcqrxHdLBuGKiyA1sBW7e0LoyEM-cQuaD5MuZV-JVkYOZY6qGBYqntA8JmqxLFMsaoP2EnjA-5bffRiQdpL2L6djcrO6cJtoWS0R3cCiSKCH-H0LBD_7XnAqPGkPnkCw_snFpJ2Ntp2nG3gCEC0lMbQ66aDvsCDTHSZRJWx24V_O020bPpP2_xSMYl1s_iIEIIyx-qTemKJ6_uWVYC5iG2-uFYu4QsN2feZwcLORM6GGoNULJ0qUGfQ3EyTnPOm1equMxhNuQ8eOlFRY-cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33c71a96b.mp4?token=a0fdHCwDbEVYAMzS-fXyoOlJgyxpp1-Pd5t_ogbCfwiMUg8okGzxTKLp5LTWI59FcWeBcqrxHdLBuGKiyA1sBW7e0LoyEM-cQuaD5MuZV-JVkYOZY6qGBYqntA8JmqxLFMsaoP2EnjA-5bffRiQdpL2L6djcrO6cJtoWS0R3cCiSKCH-H0LBD_7XnAqPGkPnkCw_snFpJ2Ntp2nG3gCEC0lMbQ66aDvsCDTHSZRJWx24V_O020bPpP2_xSMYl1s_iIEIIyx-qTemKJ6_uWVYC5iG2-uFYu4QsN2feZwcLORM6GGoNULJ0qUGfQ3EyTnPOm1equMxhNuQ8eOlFRY-cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
أبو محمد الجولاني: الاستنتاج الذي توصلت إليه من تجربة العراق هو أنه يجب ألا ننقل واقع العراق إلى سوريا. لكل دولة ظروفها الخاصة ومشاكلها الخاصة.  ما تعلمته من العراق هو أن الصراعات والانقسامات والنزاعات الطائفية التي استهلكت العراق يجب ألا تتكرر أبدًا في…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86790" target="_blank">📅 10:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86789">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e9f384c4.mp4?token=n3AsJq6uk4LX2AQpPNUdPR2vDolZOZ8St95yYt48woQW0BXS0LJ6V5h47BmeZUFuYhR1ZzoYTMoRFM6LBTWBbqHC_EOEa1vT7dV4hiwFWjrcod-2EwGXctZ-phU_MJxs0qydNH-Ho3J3AAZKVwUx--jSXS7Zw6hqGhtdfmcteRGPNQAllv82rDoOFVYrwgGIvRJBCZn6IkYh6aLFn8ckeeZW58ktXroPMmy2uInzLOhfzZv62VBvyXU6YuvIOig0R6vxeGvwMdmjIK_SXeseFyvgY0PwwnrnT5tu7O30_3XZ7kFPi0pdYrb5kJ93t0brz3uMvpfqn_E6Xk_5VeUiw4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e9f384c4.mp4?token=n3AsJq6uk4LX2AQpPNUdPR2vDolZOZ8St95yYt48woQW0BXS0LJ6V5h47BmeZUFuYhR1ZzoYTMoRFM6LBTWBbqHC_EOEa1vT7dV4hiwFWjrcod-2EwGXctZ-phU_MJxs0qydNH-Ho3J3AAZKVwUx--jSXS7Zw6hqGhtdfmcteRGPNQAllv82rDoOFVYrwgGIvRJBCZn6IkYh6aLFn8ckeeZW58ktXroPMmy2uInzLOhfzZv62VBvyXU6YuvIOig0R6vxeGvwMdmjIK_SXeseFyvgY0PwwnrnT5tu7O30_3XZ7kFPi0pdYrb5kJ93t0brz3uMvpfqn_E6Xk_5VeUiw4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
أبو محمد الجولاني: الاستنتاج الذي توصلت إليه من تجربة العراق هو أنه يجب ألا ننقل واقع العراق إلى سوريا. لكل دولة ظروفها الخاصة ومشاكلها الخاصة.
ما تعلمته من العراق هو أن الصراعات والانقسامات والنزاعات الطائفية التي استهلكت العراق يجب ألا تتكرر أبدًا في سوريا.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/86789" target="_blank">📅 10:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86788">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f8a7eb0b.mp4?token=hqpNEtND07Rxy-rxmXfIbHt3zBVZwP7E4ki7sEylOf6e0xKVJ5i5RgY_g2jSSYcfB86BIFjztZagbObHArt0Cj96_MhYgu6t8RwGfzUa2iNeumA_4QZQGc3i9cv9o-CBg0ox7h-3RDfQdUwDm1v6wQff7u9tfZ3XxbLQRvgaEBw4uKjRG119AW0Ui2ZHOAOoUz8GuDKcYJziVLKV4IBUjtrDsessn3AcPIlOHEE7bu0e-WnotNREbIkp-B8jPjfkjQZC2FxLHmHT4f1okR9lOM0YmK9VHBs_6tbTBWxn6FdElMqf_o3JtFjO4DyC-FNqGYbnvXXCz6E7R1PdQk0OdZCt3mmJRV2a4yrG_MbaBh3DSNZbN_oA-KScfkLhDpfCTbDsjaQzT4KYge9mUt0s6PnhxtQ5o567yaaXEIF6vZIB_evJS6SoNPJYPHUW9P0OEe9t4WK_C8OqJMBEN3jXwAH9eDmNYXGsNGEH20j63OeqGEp7nmUOn-fSJO90mHR4y8efilMryBsXej9NSZRoqTSBVcw1rlbpdp4cV4PfFiYdOzSob8DBbXNBHwe-H_ppOftr_0K_WKQodpHrT8mHUVr5ckQOvxieMvX6hY83c-K2413Pm9n4WgwjlKVo7OaWrV6NK-sUNDn2N_t0Fw_bd50osSGkkH3A4KRQ-H-xfQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f8a7eb0b.mp4?token=hqpNEtND07Rxy-rxmXfIbHt3zBVZwP7E4ki7sEylOf6e0xKVJ5i5RgY_g2jSSYcfB86BIFjztZagbObHArt0Cj96_MhYgu6t8RwGfzUa2iNeumA_4QZQGc3i9cv9o-CBg0ox7h-3RDfQdUwDm1v6wQff7u9tfZ3XxbLQRvgaEBw4uKjRG119AW0Ui2ZHOAOoUz8GuDKcYJziVLKV4IBUjtrDsessn3AcPIlOHEE7bu0e-WnotNREbIkp-B8jPjfkjQZC2FxLHmHT4f1okR9lOM0YmK9VHBs_6tbTBWxn6FdElMqf_o3JtFjO4DyC-FNqGYbnvXXCz6E7R1PdQk0OdZCt3mmJRV2a4yrG_MbaBh3DSNZbN_oA-KScfkLhDpfCTbDsjaQzT4KYge9mUt0s6PnhxtQ5o567yaaXEIF6vZIB_evJS6SoNPJYPHUW9P0OEe9t4WK_C8OqJMBEN3jXwAH9eDmNYXGsNGEH20j63OeqGEp7nmUOn-fSJO90mHR4y8efilMryBsXej9NSZRoqTSBVcw1rlbpdp4cV4PfFiYdOzSob8DBbXNBHwe-H_ppOftr_0K_WKQodpHrT8mHUVr5ckQOvxieMvX6hY83c-K2413Pm9n4WgwjlKVo7OaWrV6NK-sUNDn2N_t0Fw_bd50osSGkkH3A4KRQ-H-xfQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بعزيمة يملؤها الإيمان وقلوب تنبض بحب الحسين عليه السلام ؛ انطلق أبناء موكب بني عامر في مسيرهم إلى كربلاء المقدسة لإحياء زيارة الأربعين الخالدة وتجديد البيعة لسيد الشهداء حاملين راية الوفاء والخدمة على نهجه المبارك.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86788" target="_blank">📅 09:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86787">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔻
إعلام غربي: التكاليف الاقتصادية الناجمة عن الحرائق والموجة الحارة الشاذة في دول أوروبا خلال عام 2026 تجاوزت 3 مليارات يورو</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86787" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86786">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d50a4696d.mp4?token=uQFZqaUSoxGMg0wEeyQuxjHWNTeABFzPrhi5zG98b6jBWcmitoK9dyLeGTLJXJiv6IChOtiGJP_jf2MIBx6TqsNe7-OWiI7n7l9szaREbde4iXyoyQ0rcw7Z6ydI6SBtLjzyFwGoDgxZXOr0z1aAhYBRxJwFkIVizPxdBIBmW4TwHLnHt2onU1HQ1Jxt1bVjirAeVuNrDCtAoAEoiFVn_in7zBs0VogiqapZDRh6JaW0Vna-BW1eDijRsCbsIIDI57B3LoScCJ-hjbQJDpAUCF6RmYxwUhHtIa8ZZvH0Ibew-AtYvRTlu5B1b18sw5Nt5iqU0eEFmEaon5VYbF0bcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d50a4696d.mp4?token=uQFZqaUSoxGMg0wEeyQuxjHWNTeABFzPrhi5zG98b6jBWcmitoK9dyLeGTLJXJiv6IChOtiGJP_jf2MIBx6TqsNe7-OWiI7n7l9szaREbde4iXyoyQ0rcw7Z6ydI6SBtLjzyFwGoDgxZXOr0z1aAhYBRxJwFkIVizPxdBIBmW4TwHLnHt2onU1HQ1Jxt1bVjirAeVuNrDCtAoAEoiFVn_in7zBs0VogiqapZDRh6JaW0Vna-BW1eDijRsCbsIIDI57B3LoScCJ-hjbQJDpAUCF6RmYxwUhHtIa8ZZvH0Ibew-AtYvRTlu5B1b18sw5Nt5iqU0eEFmEaon5VYbF0bcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجار داخل مصفى بيجي وحدة الهيدروجين بمحافظة صلاح الدين نتيجة خلل فني.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/86786" target="_blank">📅 07:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86785">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d154890a98.mp4?token=TTqUa8Zg7BahTHpvjiXbQUVhbAol7M5vomTdaAjR9kjRU5t9xEHUYVeJYpxp63MlXQ-Nk8t4EnVTPnVlfjbUUJMu5d6v2oAa-OBCRvPGsU3VEAuNCf1yDk5yd7RJrFKQzLzms_8FWIAsVX2LLOuz94p6ZF2e1PoNdxnvwT9TTqRaaEsM9eiAZnCiSeuORczyvb9xqUy-tYkUXswZ7D2JOI5hh9nVnQl8fn2I_F5pTEENIGEI7pl5arq7qgJD-pvfYVX2xwQlaGjstpq7PIZO31fM1mnqUrG7bYPdxgbae-jvJ-eiWPXe6NrWgeArP8xHCh1snv0obEhjS-u7lU_KYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d154890a98.mp4?token=TTqUa8Zg7BahTHpvjiXbQUVhbAol7M5vomTdaAjR9kjRU5t9xEHUYVeJYpxp63MlXQ-Nk8t4EnVTPnVlfjbUUJMu5d6v2oAa-OBCRvPGsU3VEAuNCf1yDk5yd7RJrFKQzLzms_8FWIAsVX2LLOuz94p6ZF2e1PoNdxnvwT9TTqRaaEsM9eiAZnCiSeuORczyvb9xqUy-tYkUXswZ7D2JOI5hh9nVnQl8fn2I_F5pTEENIGEI7pl5arq7qgJD-pvfYVX2xwQlaGjstpq7PIZO31fM1mnqUrG7bYPdxgbae-jvJ-eiWPXe6NrWgeArP8xHCh1snv0obEhjS-u7lU_KYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة صلاح الدين العراقية.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/86785" target="_blank">📅 07:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86784">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة صلاح الدين العراقية.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/86784" target="_blank">📅 07:01 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
