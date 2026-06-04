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
<img src="https://cdn4.telesco.pe/file/mgwJw33Ft-kxdUStciiuPbVSoaMhWAqfTmJ6Lcrw7KO8d4VsYMV_hyr5QfpqLKW8rFR1kaXmPvQXYdKJGn19BJAR41v6E-JKYGKDb2C49jY4rGFxE93v04EYMqGWMT_tCsAkWW4p0b-QmpIkCg10nMHBIbrX24xcoOkHq4vcqFq1tonSctUb5x9YWcm46RFyFv6yNnhLdNoqgurqSPTJvgU6VIJZXHJNye95dgjypudTHNetaYAPTjBC94IARp7p2HqjaQfC-sPKyGx2nx_iLgIhMdn7sgnWTqSWo3ULh30ZyeSQAROHEMHJVG0rH5Plj6YFszCGrQDjgZxfXuvHqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 02:21:22</div>
<hr>

<div class="tg-post" id="msg-77056">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwLPvRrys84HQp8aI17VwBqZ35nIE4th-lT1V8IbG7FVRwK0WNV6FT9V0C3ZUQqvQCnjhWD62ZMa8Nb6YrsXn2hOKXH5UveBkPa1M1dz7U4LUqLwWReXNSHfbT3gis8jkuK5NT1AckV6xulMZBP7-QP-Gj-08nXwbMmGVVwdcp-l70U8waiCv5VDleq10gtLu8h_z6sYWwLxk4fV_YGNRZUL5Wvx0o8PfW10mcg1b1iG6jBrzp1Mlhr8Z55ohIXyeSQNRMb1alh7mL65cgkG2SEtDq2JvQhLEDR_Ic891Jn--PKLoSfI4CMzml3pmlJW9qqcS9MP1BrWWep51fBb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد المكصوصي : من
كنت مولاه فهذا علي مولاه ؛ تسليم ذو الفقار هو خيانة للبيعة ..</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/naya_foriraq/77056" target="_blank">📅 02:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77055">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">استهداف نحو هدف معادي الان قبالة جنوب ايران</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/naya_foriraq/77055" target="_blank">📅 01:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77054">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/naya_foriraq/77054" target="_blank">📅 01:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77053">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6-gcuOuzyqlPqAalFxmvw8J2Uinj0eer1MwcJwNLcr13wP7Z4hAQq7rNLvqfuNq3UAIadQKrsz0lUU5ej9SHbBnCGtpiZXlRV-ehMpM1cMtMS-jxDe8iEcf2lW9p9FuBeWSTc3q0AdANaaMheVk93HDtMR7LrdF_8Y0OFBBuSm_NNdfSs1dy41YBGSFu_GatZsVRpjIDBR8v_U4YcOoDM9rdA4KkCYfFXLSw2W4400DejITCbFkp1UiRV6xNjav9UUndUC4mj8D3rpdInDUQQpFIlOd0raFUZ-HmC38X1znqYkr_r53p6aNpiKDplNwsp01dd7SQxNAjPxJZkGr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأمين العام لحركة أنصار الله الأوفياء الشيخ حيدر الغراوي رافضا تسليم السلاح: بنادقنا هي الامتداد الطبيعي لـ"ذو الفقار".</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/naya_foriraq/77053" target="_blank">📅 01:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77052">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727569b896.mp4?token=GnDSRUyJtqGT9oDmldJCUUol1o5KmmRqfMhoSCj2Ntn0LB04_z1tS984Ajj9weRCESPvD_idKnQtj71Mm6S3ERHYPg8Rnrcbayo906PEdtgFSgKVNhqGaDFTC53GiSfwGhqgtgG7QkkwpFHASM2p7g6H-SybBugePTCtVzYR4mfM0ZF5OJbpActjIBp-lvJ9dmSrjcgIoh6bG-15n42SonJb3R9diPAf5SLIV2T378MasHn-NM6r7eEexjFDsrnspV6t32U8k0yhsmlRQRgZNbxgEBMDkfivVcJVRfDle1PdDn7QI-IhOSlRGTa_SXS2QagIbXuFj46vM1zaXbqZjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727569b896.mp4?token=GnDSRUyJtqGT9oDmldJCUUol1o5KmmRqfMhoSCj2Ntn0LB04_z1tS984Ajj9weRCESPvD_idKnQtj71Mm6S3ERHYPg8Rnrcbayo906PEdtgFSgKVNhqGaDFTC53GiSfwGhqgtgG7QkkwpFHASM2p7g6H-SybBugePTCtVzYR4mfM0ZF5OJbpActjIBp-lvJ9dmSrjcgIoh6bG-15n42SonJb3R9diPAf5SLIV2T378MasHn-NM6r7eEexjFDsrnspV6t32U8k0yhsmlRQRgZNbxgEBMDkfivVcJVRfDle1PdDn7QI-IhOSlRGTa_SXS2QagIbXuFj46vM1zaXbqZjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطنين يرصدون ظهور اجسام غريبة لليوم الثاني على التوالي في سماء ناحية النخيب غربي العراق حيث مقر القاعدة الاسرائيلية المكتشفة مؤخرا</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/naya_foriraq/77052" target="_blank">📅 01:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77051">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شبكة CNN: الحاملة كلفتها 13 مليار دولار</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/naya_foriraq/77051" target="_blank">📅 01:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77050">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شبكة CNN تبث مشاهد لحاملة الطائرات الامريكية "يو إس إس جيرالد آر فورد" وهي مدمرة بعد هجوم ايراني رغم النفي الامريكي</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/naya_foriraq/77050" target="_blank">📅 01:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77049">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cb994ab4.mp4?token=KWlYN2vkK7-uIYCwTFCxNgSL4Y9uIsJ0YBaT9iS4bH6RZusHrVN0VqoSp4QGg2KntuXFQxAfukBPseWPV12hPn97c65UziQlQAp-PCJHSHPYTUPZ9BgqttcJKm9lzqJzhJ6PqL8UeJb4GLa5IHXGB_AMizwSYMp8ki1bvmPubTE1joXXfQgMbRQ_F8RxbMWA4fXy8aGbVBkbgVEIb1NM4XXbmJ_AqdXPmlpGL19d3Iv-Xm7gav1fwyNeUfGaWInhLNAZT3G2sN70HF7cobiDzMFB_2DARsTZi_Qj_U7Ndho22OB0nVWWGq9qTHYRgZal6FAQjD0A9Pin77h_JBUGsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cb994ab4.mp4?token=KWlYN2vkK7-uIYCwTFCxNgSL4Y9uIsJ0YBaT9iS4bH6RZusHrVN0VqoSp4QGg2KntuXFQxAfukBPseWPV12hPn97c65UziQlQAp-PCJHSHPYTUPZ9BgqttcJKm9lzqJzhJ6PqL8UeJb4GLa5IHXGB_AMizwSYMp8ki1bvmPubTE1joXXfQgMbRQ_F8RxbMWA4fXy8aGbVBkbgVEIb1NM4XXbmJ_AqdXPmlpGL19d3Iv-Xm7gav1fwyNeUfGaWInhLNAZT3G2sN70HF7cobiDzMFB_2DARsTZi_Qj_U7Ndho22OB0nVWWGq9qTHYRgZal6FAQjD0A9Pin77h_JBUGsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبكة CNN تبث مشاهد لحاملة الطائرات الامريكية "يو إس إس جيرالد آر فورد" وهي مدمرة بعد هجوم ايراني رغم النفي الامريكي</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/naya_foriraq/77049" target="_blank">📅 01:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77047">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVJzHi4cZ9m89knXXHp27Yve4etDHg_WtFyxNHM95nonWjAR4IMRksCjZ-H1q19T3WtaL2KeakNl5AmoZxklMn0J1ZzYju-WO6rDDje1Z447b1IYfITT3E9h6m2dtsBXa309JBNYxgvQ-thtekZ1eAspHfYbpxn5_-uCYk6nDZQQ_QT8cLeSxFxugBQfkuxEYqhizad6HGV4-u8h7QtqKvd1TuHuFw3qDmHH0PDD6s5-kJvpOb_CDgH63wAxqoSrI5NxZRZoC7GJcDeJHdYPBqiM1Lz4DH6FbiTe8RLvDR9kTqMAbWx47VSmpOo4oWCSZaPiopwZDxem3Iz_y3LyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZycoF17onRuPylS_xIzuWlz7Wz6fjd7UfRgtI-SyauKuXi2kCb8C_I5yaKhx6Ca0G5bLieWyAq5Mr7GNN0g1qNSXeQCG1-Pi-IwiUiSn7pRHNsHEdjoA-2vrg1XKGHZ77NooYYcz6HLmrE6UIi_puIeqUvynbUGyd8RgbCkP7FZUW8tz4r71TAxe61I9vEG399lM5QzZjw3aoYdukuvWtbJ5stMIcPgeb90gfgkDh-I0ZW_8cxWmFho-3y7y8hP1Uvmo7rhfRHectGOnmkwUeauwBYXSbi8eHcyRmluEgjlRuOKBGI814h4rKvLkIWGSradB1SasxZJ1uo7QmaTNUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
شبكة CNN:  عندما اندلع حريق على متن حاملة الطائرات يو إس إس جيرالد آر فورد في مارس، أصدرت البحرية الأمريكية بيانًا مقتضبًا قالت فيه إن الحريق قد تم احتواؤه، وأن اثنين من البحارة قد تلقيا العلاج الطبي لإصابات "غير مهددة للحياة"، وأن حاملة الطائرات "جاهزة للعمل…</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/naya_foriraq/77047" target="_blank">📅 01:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77046">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0TE69xSMw-4sopYcYHC3y5uMPt1_XuLyaybka2cciEjVvIzfTMN8yfYIn6u2DXG7X880LV7I6X0EejBlRJVQsS4KSjzkf1QSMwBlUknhtc6LZpxAoFxARpthbLRupVNMK-sfJW2vM7diou4FaCWQPIvOpsoGqIaL_xB6NtiwbeYwSLmsxux2yeUzjsJVAtTxUbcXtd7m_jEpVQ3THjRXHqDym5UCnd-THHvt2NFe1udVCsJuRasPD8FAfwYfHbp8xyRRZRraaUmOs7haXVTcrtocTjDdwao7rxhwVhdqYFy0IohYQpF5QwBsllVCGRlnJdXLM3zha8Y3cXaZwhu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/naya_foriraq/77046" target="_blank">📅 01:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77045">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/naya_foriraq/77045" target="_blank">📅 01:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77044">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الاعلام الايراني:
‏تم رصد حريق بقوة تزيد عن 300 ميغاواط في جزيرة داس بالإمارات العربية المتحدة؛ ويبدو أن شيئاً ما قد تم استهدافه أو تفجيره. ‏تُعد جزيرة داس واحدة من أهم مراكز تصدير الغاز الطبيعي المسال في الإمارات العربية المتحدة. ‏الحريق عمره حوالي 12 ساعة، مما يعني أن الحادث أو الانفجار أو الهجوم المحتمل وقع خلال النهار، وليس في الليل.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77044" target="_blank">📅 00:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77043">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
مقتل أحد ابرز قادة العصابات الإجرامية في جنوب سيستان وبلوشستان والتفاصيل لاحقا.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/77043" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77042">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ترامب عن السيد مجتبى خامنئي: ‏في الواقع، يتمتع بسمعة طيبة للغاية في بعض الأوساط. ‏يقول البعض كلاماً سيئاً عني، لكن الكثيرين يقولون كلاماً سيئاً عني. هذا غير صحيح على الإطلاق، بالطبع.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/77042" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77041">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e18f8c0b54.mp4?token=hLET_7rT91fGWn8UDNp-jymxF1CjK2VsW8-hvu1cyT0Qrb5oHMsVgnoQJ3CM2Me1xlN9pNPs3DnyG7ZKCARh7CpdsJPL_MILaPK70Gev2rbad9aUOpJ9EeWosubS8qo74BknPVQPCGhE5KCjAkeqI30ZeeKJ462HevnAa3AZWggQS9455WCSul2cafOBdvZbUFHGK1bVukt8G9fLgSZEzKk-ePMzjXi6V29WcXcPvR-B0yH5Ta6t-TBkF2AMmXYp0l4MNkW6IrGjPJ_qOXLBvd91uYTr5cg8c8PIBegQD0j_9ZPstIsfgPSkpNzWQ04PtSFSAXFhtaAfPLNw9DTWwxp0l-WxgQxD6X3fRFEuIVgGtH9iWXrIHnugDyS3ZUy_HO41-Uv4ESV0NCdYHOqZX1D1Jb0LFniaHDDP-MY2vHofNAbBIOggTn3KAGbAv8A4HCF3MnT5RrpII0dmfR40L7MX8uv9vMnA7TJqNOOrAp3cCx8Rr0UCXsJ9n-WHVjMY-wIeYuAHQGBc9PR3A_p9DzK_v9esdz8m-IrWKoaTrUqnt66Zz-6q1PIC0xGmC5Gy8bJ0g2w1_UJvz2PYRojdyppOjqnUxFqG98BEYmVyRLRRaSfXeSSxAdb2h_x8OgFMuNGeSxq7QelZ4GPcps85SC5L0LwGFJiE9goF9vc6I64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e18f8c0b54.mp4?token=hLET_7rT91fGWn8UDNp-jymxF1CjK2VsW8-hvu1cyT0Qrb5oHMsVgnoQJ3CM2Me1xlN9pNPs3DnyG7ZKCARh7CpdsJPL_MILaPK70Gev2rbad9aUOpJ9EeWosubS8qo74BknPVQPCGhE5KCjAkeqI30ZeeKJ462HevnAa3AZWggQS9455WCSul2cafOBdvZbUFHGK1bVukt8G9fLgSZEzKk-ePMzjXi6V29WcXcPvR-B0yH5Ta6t-TBkF2AMmXYp0l4MNkW6IrGjPJ_qOXLBvd91uYTr5cg8c8PIBegQD0j_9ZPstIsfgPSkpNzWQ04PtSFSAXFhtaAfPLNw9DTWwxp0l-WxgQxD6X3fRFEuIVgGtH9iWXrIHnugDyS3ZUy_HO41-Uv4ESV0NCdYHOqZX1D1Jb0LFniaHDDP-MY2vHofNAbBIOggTn3KAGbAv8A4HCF3MnT5RrpII0dmfR40L7MX8uv9vMnA7TJqNOOrAp3cCx8Rr0UCXsJ9n-WHVjMY-wIeYuAHQGBc9PR3A_p9DzK_v9esdz8m-IrWKoaTrUqnt66Zz-6q1PIC0xGmC5Gy8bJ0g2w1_UJvz2PYRojdyppOjqnUxFqG98BEYmVyRLRRaSfXeSSxAdb2h_x8OgFMuNGeSxq7QelZ4GPcps85SC5L0LwGFJiE9goF9vc6I64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجنرال رضائي لوكالة فارس:
إذا انحازت الإمارات والكويت إلى جانب الصهاينة، فيجب منح أبو ظبي وبوبيان للسعودية والعراق.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/77041" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77040">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">المراسل: أسفرت عملية "الغضب الملحمي" عن مقتل والد مجتبى خامنئي وزوجته وطفله.  ترامب: لستُ الشخص المُفضّل لديه، لكنه على الأرجح مُحترف.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77040" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77039">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100efa8385.mp4?token=WkD7fDVWiNtykdIOzJWcsd_FxnnzciMoFniHAmP1GdBdY3YLqtS6CZt9zO6rl_I51pO1KgCUf44lnN4ooxoLGQpHDF7FYbVSn4JyAR5KOMb3J_P_qCDkUnaAgItzSEffDtVKvD6lFA_vgjf1P6Putf5kehPTTqpi0YkNLIJFUJKcvgS6G5ZZGwFQtrO8-VbWYjDlB4y_QUDt_pu6CFCw_Au2PzDLq8M8yzbMxiU5nbx5TVasxbnSMHG3e41zpM8LINOIs0BwdXXnttPIcrTDx4MfHQuDArQvi5iCFLR_gaCV75q8loFGwhKvf9hYm9guNeHoCqji6YNhyfGayCZNMIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100efa8385.mp4?token=WkD7fDVWiNtykdIOzJWcsd_FxnnzciMoFniHAmP1GdBdY3YLqtS6CZt9zO6rl_I51pO1KgCUf44lnN4ooxoLGQpHDF7FYbVSn4JyAR5KOMb3J_P_qCDkUnaAgItzSEffDtVKvD6lFA_vgjf1P6Putf5kehPTTqpi0YkNLIJFUJKcvgS6G5ZZGwFQtrO8-VbWYjDlB4y_QUDt_pu6CFCw_Au2PzDLq8M8yzbMxiU5nbx5TVasxbnSMHG3e41zpM8LINOIs0BwdXXnttPIcrTDx4MfHQuDArQvi5iCFLR_gaCV75q8loFGwhKvf9hYm9guNeHoCqji6YNhyfGayCZNMIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: إذا توصلنا إلى اتفاق مع ايران، فمن الممكن مقابلة المرشد الأعلى لإيران. سيكون من دواعي شرفي أن ألتقي به.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77039" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77038">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامب: الدولتان الوحيدتان القادرتان على الحصول على الغبار النووي الايراني هما الصين والولايات المتحدة.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77038" target="_blank">📅 23:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77037">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇨🇺
🇺🇸
وزارة الخزانة الامريكية تفرض عقوبات على الرئيس الكوبي ميغيل دياز</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77037" target="_blank">📅 23:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77036">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترفيهي اخر  ‏ترامب: ‏لم يرفض حزب الله أي شيء. اتصلوا بنا وقالوا: "ما رأيكم بالتوقف؟"  من تكثر شرب بالصالة الجديدة مال البيت الابيض
😄</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77036" target="_blank">📅 23:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77035">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#ترفيهي  ‏ترامب: لا تزال بعض الصواريخ موجودة في إيران، ولكن عددها قليل جداً.  من دمرنا كل شيء الى بعدها موجودة لكن عددها قليل
😄</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/77035" target="_blank">📅 23:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77034">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">#ترفيهي
‏ترامب: لا تزال بعض الصواريخ موجودة في إيران، ولكن عددها قليل جداً.
من دمرنا كل شيء الى بعدها موجودة لكن عددها قليل
😄</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/77034" target="_blank">📅 23:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77033">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇷🇺
‏الكرملين عن رسالة زيلينسكي التي طلب فيها لقاء بوتين: الرسالة وصلت، زيلينيسكي مرحب به للقاء بوتين في موسكو "في أي وقت".</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/77033" target="_blank">📅 23:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77032">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c38afa62c.mp4?token=KFk26EZmsNOz8Yc-vUx-21Z5HfipCvVPMhGgTkthGxkO1D4S8DkssAVA0y6fXMgOnnu6TLmHV4V4F96m13G6NKgTTokgQGMJtGRP8mL58hKt2jg-1EJ5vC8Bm7R9AgslsAvqL1214cUv1juDN78e3ri6RQgA7oe4Wlk9dscCQMOCTbRM8BWtQsdvid23sTkd_fFboGMJ2AgY2YePI6nj7cR3k2I1btM5HngqytdHE6R7OPHNRCq6jwQHOZw4cKw-lWPaTFzBisT7PrcaFSKBd0KQEd1OtJEVvMSst2ZqsrsjEaGkUmcdbnF93fnERKWlXXC3jCO-mJ15RBnzumEm8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c38afa62c.mp4?token=KFk26EZmsNOz8Yc-vUx-21Z5HfipCvVPMhGgTkthGxkO1D4S8DkssAVA0y6fXMgOnnu6TLmHV4V4F96m13G6NKgTTokgQGMJtGRP8mL58hKt2jg-1EJ5vC8Bm7R9AgslsAvqL1214cUv1juDN78e3ri6RQgA7oe4Wlk9dscCQMOCTbRM8BWtQsdvid23sTkd_fFboGMJ2AgY2YePI6nj7cR3k2I1btM5HngqytdHE6R7OPHNRCq6jwQHOZw4cKw-lWPaTFzBisT7PrcaFSKBd0KQEd1OtJEVvMSst2ZqsrsjEaGkUmcdbnF93fnERKWlXXC3jCO-mJ15RBnzumEm8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المنتخب الاسباني يسجل الهدف الاول على المنتخب العراقي ضمن المباراة الودية التحضيرية لكأس العالم 2026</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77032" target="_blank">📅 23:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77031">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇷🇺
‏الكرملين عن رسالة زيلينسكي التي طلب فيها لقاء بوتين: الرسالة وصلت، زيلينيسكي مرحب به للقاء بوتين
في موسكو
"في أي وقت".</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77031" target="_blank">📅 22:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77030">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
وكالة تسنيم الايرانية عن مصدر أمني:
- أحد أهم مستشاري رئيس الإمارات محمد بن زايد مرتبط بالعمل مع الاستخبارات الإسرائيلية منذ عام 2015
- مستشار بن زايد كان محل اهتمام الأجهزة الأمنية الإسرائيلية منذ عام 2007 بسبب طبيعة مواقفه
- المتابعة الإسرائيلية لمستشار رئيس دولة الإمارات دخلت مرحلة جديدة بدءاً من عام 2015
- اكتشاف أهمية مستشار رئيس الإمارات بالنسبة لـ"إسرائيل" تم في وزارة الخارجية الإسرائيلية
- الجهة التي اضطلعت بهذه المهمة كانت مؤسسة "ماماد" الأمنية التابعة لوزارة الخارجية الإسرائيلية
- مؤسسة "ماماد" لعبت دوراً أساسياً في اكتشاف مستشار رئيس الإمارات ثم توجيه مواقفه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/77030" target="_blank">📅 22:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77029">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حدث أمني صعب جديد جنوبي لبنان... التفاصيل لاحقًا.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77029" target="_blank">📅 22:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77028">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByXzMENXbtrWpXEdeKkizcchSsm5_xYyc-KT4j-ZN_bpEIMvQPGB8VMeTdqZuT8VDYea5vQr5nDxa4aEF8SUSbcg4qWv6pl04UqfACXVkbE2tcsYjCMtc75dXR1j5kiI0f_LwF5oEIwjz1_s6aUE0a_8dks8EM3YJ2OtfPk7bNj-eHR1ilDV2VAUQ3aaCqwDQLcDHrPb8EdjZX8RvWSNAYqeDZjpJPhLmP4Zapyk3pNs7wi_2zXrh2bSQ7h0hQnFYTG1tdfX1rjywoDrGeowi2bAq0oPSOBPxo-8M6MuusNuWkQuGHX43Y7EknXf4AyQxcQB5ReQ0QL678vgvde94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش العدو يعلن مقتل ضابط برتبة نقيب من الكتيبة 75 التابعة للواء السابع المدرع في جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77028" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77027">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الإيراني:
لا نعتبر أي ورقة مع أمريكا نهائية إلا إذا أخذت ملاحظاتنا ومصالحنا بعين الاعتبار. نصر على وضع 50% من أصولنا المجمدة تحت تصرفنا فور توقيع مذكرة التفاهم مع أمريكا</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/77027" target="_blank">📅 22:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77026">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇱🇧
بيان صادر عن حزب الله:
يمعن العدو الإسرائيلي في اختلاق الروايات الكاذبة وفبركة الاتهامات وإلصاقها بالمقاومة زورًا وبهتانًا، ضمن سياسة التضليل والأكاذيب الممنهجة للتغطية على جرائمه المتواصلة والتي باتت مكشوفة أمام العالم أجمع.
إن اتهام العدو المقاومة باستهداف مقر قوات اليونيفيل في بلدة دبين والتسبب بمقتل أحد جنودها، هو ادعاء باطل وكذب محض. لا سيما أن الاتهام يصدر عن العدو نفسه الذي لم يخفِ يومًا انزعاجه من وجود القوات الدولية في جنوب لبنان وسعيه الدائم إلى الحد من دورها، لأنها تشكّل شاهدًا حيًا على جرائمه واعتداءاته وخروقاته المتواصلة لسيادة لبنان.
إن حزب الله يؤكد حرصه الدائم على دور قوات اليونيفيل في جنوب لبنان ضمن المهام الموكلة إليها بموجب القرارات الدولية، ويتقدم بأحر التعازي إلى قيادة القوات الدولية وإلى عائلة الجندي، متمنيًا الشفاء العاجل للمصابين</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/77026" target="_blank">📅 22:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77025">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X574XYpuPWUvTfaaRdLFmihdGXThYyrKsdPpGqqF-o6t7qtlPkZ15VibipKodBe14iFM9RIoPtP8_heVs8iWxuN5LpCsQ2aIBXSXPzCeP79prIrIxak-9RXc-yQ4eEpAXA_TtRjP0u-hjH-a0e0kepxoXSNMF21JOlqOtuQe1Wxw7d8demwYXyW9213Uf7DJ2ALlm4CKaz8nGIs5ACRh9szSDAfbZ0uVm_X-MQf6DFATCBjHGJQGs86-WqVTLz9V0hp1AGAvk3vJkK4CX1-iMLsZaLyMOBi7vih2Z7Lw2wDEHzevSbH3RE0Cni6kfboe4UVA13YCaBWBzbdBAFU3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
أعتقد أن لدينا أكثر الانتخابات غير شريفة في أي بلد، في أي مكان في العالم!</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/77025" target="_blank">📅 22:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77024">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇷🇺
‏بوتين: الحرب على إيران صرفت اهتمام الولايات المتحدة عن أوكرانيا</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77024" target="_blank">📅 22:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77023">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الناطق باسم القائد العام للقوات المسلحة العراقية: تشكيل لجنة مركزية عليا تضم ممثلين عن الدفاع والداخلية والحشد الشعبي لحصر السلاح بيد الدولة</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/77023" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77022">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇷🇺
‏
بوتين:
الحرب على إيران صرفت اهتمام الولايات المتحدة عن أوكرانيا</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/77022" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77021">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 02-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/77021" target="_blank">📅 22:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77020">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:  - قطر دولة صديقة لنا ولطالما جمعتنا بها علاقات جيدة جدا  - يا للأسف استُخدمت في الحرب الأخيرة القاعدة الأميركية في قطر ضدنا كذلك استخدمت الأجواء القطرية  - لقد أبلغنا الأصدقاء القطريين باستخدام القواعد الاميركية على أرضهم…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/77020" target="_blank">📅 22:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77019">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
- قطر دولة صديقة لنا ولطالما جمعتنا بها علاقات جيدة جدا
- يا للأسف استُخدمت في الحرب الأخيرة القاعدة الأميركية في قطر ضدنا كذلك استخدمت الأجواء القطرية
- لقد أبلغنا الأصدقاء القطريين باستخدام القواعد الاميركية على أرضهم ضدنا
- نحن شاكرون للإخوة في قطر الذين بذلوا جهودا وساعدوا من أجل التوصل إلى حل عادل بين إيران وأميركا إلى جانب باكستان</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/77019" target="_blank">📅 22:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77018">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇸🇾
سماع دوي انفجارات في مدينة حلب السورية.</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/77018" target="_blank">📅 22:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77017">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌟
🏴‍☠️
مجدداً.. أستهداف دبابتي ميركافا في محيط قلعة الشقيف بجنوب لبنان من قبل أبطال حزب الله.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/77017" target="_blank">📅 22:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77016">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
🔥
بوتين: روسيا ترتبط بعلاقات وثيقة مع إيران ونحن قادرون على المساعدة في حل الأزمة .</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77016" target="_blank">📅 21:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77015">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c6ea7cab.mp4?token=bzT5ysBAE8PPE3iG_oxWD5zoJ-nNOTXlAiuRvAHwic90C7jFEuPbEmlDN7zKEK1IYFX3QG5ltQX6KJ3Cs-01i3VZElZTNdZAWj6g1CbiB2piPPFJANj7HFTKrc5HNNi4WO_bqCWsR7NsEBvgtUsnIBb_Aql0fT53Z6SSlvEc4CAflG49u12ISdDvIiHnixPcyr7K1Aa5voqb985LU9CHp0wh7q1voj7NHFVJTSp87KIrtTX3IkwbLK8PvOgoopD03Z_jipW_GAzxkHBRT_kfY7JqlZWVAcvHc9X3rDzaN-MYeQsNF3AgPpEz951Ue7zNVUzYOWCKNEvQXn7k7-Klag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c6ea7cab.mp4?token=bzT5ysBAE8PPE3iG_oxWD5zoJ-nNOTXlAiuRvAHwic90C7jFEuPbEmlDN7zKEK1IYFX3QG5ltQX6KJ3Cs-01i3VZElZTNdZAWj6g1CbiB2piPPFJANj7HFTKrc5HNNi4WO_bqCWsR7NsEBvgtUsnIBb_Aql0fT53Z6SSlvEc4CAflG49u12ISdDvIiHnixPcyr7K1Aa5voqb985LU9CHp0wh7q1voj7NHFVJTSp87KIrtTX3IkwbLK8PvOgoopD03Z_jipW_GAzxkHBRT_kfY7JqlZWVAcvHc9X3rDzaN-MYeQsNF3AgPpEz951Ue7zNVUzYOWCKNEvQXn7k7-Klag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إندلاع إشتباكات مسلحة في منطقة عائشة بكار بالعاصمة اللبنانية بيروت.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77015" target="_blank">📅 21:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77014">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
رئيس هيئة الحشد الشعبي العراقي:
الحشد الشعبي منح القوات الأمنية فرصة لإعادة بناء قدراتها بعد هجمة داعش الإرهابي.
الحشد الشعبي تشكل في الميدان استجابة لفتوى السيد السيستاني.
لا يزال العراق محاطاً بالتحديات.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/77014" target="_blank">📅 21:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77013">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402d45f5a9.mp4?token=W9XJSrawugCbVk0gwKqj_8OHP3qjTG8EEHCwPwBHR9HPnNzmyTmtsPdljisVQkSOYFe-y0mwGWTB2b4Yk5NqREc6coWlJaRDOz31tJD1bJfsmuzXBQaFuHl8rieFgSy6eIukbHYz3bhDQxPGE3tNqrr2PC6jEHuiWNMOFGWQkcXEaPrtVgQKQ-17_tCY4eIjltE0P3U1maoJrrcaCF5tnwe8MOrcaeVS-qdqXkMghHnLZt3wkJJXWFchVHD_BonvkqujEfKDsH0s4wcnNyk2qvGGvjz3PtbYfxgoLyoqUAcT5BcOvif1vkYJojl7n3cyeZX6kBazSSG2i2oZJETR5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402d45f5a9.mp4?token=W9XJSrawugCbVk0gwKqj_8OHP3qjTG8EEHCwPwBHR9HPnNzmyTmtsPdljisVQkSOYFe-y0mwGWTB2b4Yk5NqREc6coWlJaRDOz31tJD1bJfsmuzXBQaFuHl8rieFgSy6eIukbHYz3bhDQxPGE3tNqrr2PC6jEHuiWNMOFGWQkcXEaPrtVgQKQ-17_tCY4eIjltE0P3U1maoJrrcaCF5tnwe8MOrcaeVS-qdqXkMghHnLZt3wkJJXWFchVHD_BonvkqujEfKDsH0s4wcnNyk2qvGGvjz3PtbYfxgoLyoqUAcT5BcOvif1vkYJojl7n3cyeZX6kBazSSG2i2oZJETR5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إندلاع إشتباكات مسلحة في منطقة عائشة بكار بالعاصمة اللبنانية بيروت.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77013" target="_blank">📅 21:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77012">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LU-_cXvJUmcJKfM8-MNMheHyFcHnZiU-2Z49t8LrfMEBK79sAM39l3NG-WiYU5JsvXTQREiXPcUXTBjdkYnl_QUpPF8vcvM-SJd9Qj9h2_n6rn__LGI1WYlIpRdYfbtZS0aS_GQJcmBTOWn1Z6FMiN8CH3QRMJYjSTwkgr1p1UpbLALQXvRJ7CPwLfWIyYnlJllTr00pcYadWA9YHF27Yvma0spPwBxIV_9Z02c-sNo-wywmos9ojUV-U7JYqCmJ1DH6UiaNenpgwBLhHzZC-4E1F-omkdDmTkmgmWhRRtu-v-9N8rg4jnnYQTZ3qQ21QNsgLpZLugVcKN2a_qwXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: الرياضة الجامعية، وهي مؤسسة أمريكية عظيمة تنتج العديد من الرياضيين والقادة والهيمنة الأولمبية، هي "فوضى" كاملة، ويقول الجميع إنه يجب إصلاحها.  بعد الدعاوى القضائية التي لا تنتهي والأحكام المجنونة، لم تعد هناك حدود تقريبا، وسرعان ما لن يكون لدى معظم…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77012" target="_blank">📅 21:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77011">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909440813e.mp4?token=IG7d2qFDHD8RJdFIwCF5mhEDTl8Kcrh7ZVUQPy-xIYN6GTGUwBru9aia0cDOkB87KLf0ne_qwfqryF_K1WjxbdKAWXqQKDKpxuJJd6pPyI0sY3sk8RmjRCo66ZMOO1j7324ezudYPZiJHXeeQ1NPtQ4ESbw8vTTgqqOkk9Ri7tPK9OEZ-uFwfFyKWu6kLwd6r7iPv0t7GXfH9DNm_bp0PlMlMT-d4sC0qbAkbh3-zSHaC4c2G5A4gzmI9qWjgf3CvYFslOH6mvfqEqdn9r50cotT0cnClQLiHhs3unjuJEna9Re_Ts2WSiJKnHFIwwHqswHoMyeOwVmo3HFKIGF_3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909440813e.mp4?token=IG7d2qFDHD8RJdFIwCF5mhEDTl8Kcrh7ZVUQPy-xIYN6GTGUwBru9aia0cDOkB87KLf0ne_qwfqryF_K1WjxbdKAWXqQKDKpxuJJd6pPyI0sY3sk8RmjRCo66ZMOO1j7324ezudYPZiJHXeeQ1NPtQ4ESbw8vTTgqqOkk9Ri7tPK9OEZ-uFwfFyKWu6kLwd6r7iPv0t7GXfH9DNm_bp0PlMlMT-d4sC0qbAkbh3-zSHaC4c2G5A4gzmI9qWjgf3CvYFslOH6mvfqEqdn9r50cotT0cnClQLiHhs3unjuJEna9Re_Ts2WSiJKnHFIwwHqswHoMyeOwVmo3HFKIGF_3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
والد الجولاني يتحدث عن الدول الحليفة لابنه ويتهم السعودية باحتلال صحراء النفوذ وينسب مدناً تركية منها أضنة وماردين ومرسين وأورفا وطرسوس لسوريا ويتساءل ساخراً عن من يمكن إقناعهم بالتنازل عن هذه المدن.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77011" target="_blank">📅 21:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77010">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
🇱🇧
🇱🇧
ايران لا تترك حليف لها
رفعُ الرايةِ العملاقةِ لحزبِ الله، والبالغِ ارتفاعُها 500 متر، فوقَ برجِ آزادي في طهران .</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77010" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77009">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇷🇺
بوتين:
لا نستبعد في المستقبل اتخاذ قرارات بشأن الاستخدام الكامل لـ "Oreshnik" ضد أهداف، بما في ذلك في مناطق البناء الحضري.
نمتلك جميع الموارد اللازمة لتحقيق أهدافنا العسكرية والجيش الأوكراني يعاني من نقص كارثي في عدد ​​الأفراد.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77009" target="_blank">📅 20:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77008">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
واشنطن طالبت طهران بتسليم ردّها قبل نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77008" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77007">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔥
🇮🇶
سوالف الگهوة
رسالة رئيس مجلس الدوما الروسي السيد فياتشيسلاف فولودين إلى رئاسة مجلس النواب العراقي .</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77007" target="_blank">📅 20:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77006">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الصهيوني في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77006" target="_blank">📅 20:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77005">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv12KRLC-op5qTGE28Iu6cMBOagmIImJ9QCY2VzBznfonnp2LQgnm--CTz8LnhNzCbAsFeyTTpPxnlfgad4xnbEB2FxPA2O6sviuGdXBd1-tuA8yBWwNfotXsAJ_pUK59bv5vyWKeDHj6ml2VHN4znz8v3L7frdKwo6V7tQNyEYTRKYoU6L7gmPH7NKu_FkAp7yUrc_movuu9NBMtVK6Ton0FjwQ3sHUlav4Bu7fCJSYH-DeItvbyMVPNeCWqS44TGE9ORHSFAKTL7ka04LJlYpCXD84sgrGBHXFDhpaCw0EIaZk04cvVNFGj9PjWzTmNl4XVP9obx1JuYSNbd4LRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
الرياضة الجامعية، وهي مؤسسة أمريكية عظيمة تنتج العديد من الرياضيين والقادة والهيمنة الأولمبية، هي "فوضى" كاملة، ويقول الجميع إنه يجب إصلاحها.
بعد الدعاوى القضائية التي لا تنتهي والأحكام المجنونة، لم تعد هناك حدود تقريبا، وسرعان ما لن يكون لدى معظم الكليات رياضة لأن كل واحدة منها ستكون مفلسة، ولن يسمع عنها مرة أخرى. الرياضات النسائية، والألعاب الأولمبية نفسها، هي الأكثر خطورة من هذا الوضع الكارثي. تتحول الرياضات الجامعية إلى رياضات محترفة، إلا بدون قواعد على الإطلاق، وهي نتيجة لا يريدها أحد. اشتكى لي رؤساء الجامعات ومفوضو المؤتمرات والطلاب الرياضيين والمدربون والمديرون الرياضيون من أنها أصبحت كارثة، بعد سنوات من عدم اتخاذ أي إجراء، وأن المدارس كانت تخسر مئات الملايين من الدولارات سنويا. لقد قارنوه بقطار شحن لا يمكن إيقافه!
لهذا السبب، قبل بضعة أشهر، عقدت مائدة مستديرة جمع فريقا عالميا من أفضل المديرين التنفيذيين الرياضيين والطلاب الرياضيين والقادة السياسيين في بلدنا. كان الهدف هو إيجاد حل من الحزبين لحل المشكلة.
بناء على هذه الاجتماعات وخبرة السلطات الرائدة، وقعت أمرا تنفيذيا، لكنني قلت دائما إن الحل الأفضل هو الحصول على قانون الكونغرس من الحزبين إلى مكتبي من أجل إنقاذ طريق طويل ومحرج عبر الجحيم لهذه المؤسسات. أود أن أشكر أعضاء مجلس الشيوخ تيد كروز وإريك شميت وماريا كانتويل وكريس كونز، من بين آخرين، على تقديم قانون حماية الرياضة الجامعية. يحل هذا القانون العديد من القضايا الأكثر إلحاحا التي تتحدى جامعاتنا وطلابنا الرياضيين، ويوقف الفوضى، والأهم من ذلك، قد تكون الفرصة الأخيرة لإنقاذ الرياضات الجامعية، والكليات نفسها، قبل فوات الأوان.
لقد عمل مجلس النواب لفترة طويلة وبجد بشأن هذه القضية أيضا، وأنا ممتن جدا للمتحدث مايك جونسون والزعيم ستيف سكاليز على عملهما لحل هذه المشكلة الرئيسية للغاية.
أحث مجلس النواب ومجلس الشيوخ على الاجتماع معا لتمرير قانون نهائي من الحزبين، يمكنني التوقيع عليه هذا الصيف، يعكس آراء ومدخلات كلا المجلسين. علينا أن ننقذ الرياضات الجامعية! شكرا لك على اهتمامك بهذه المسألة.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/77005" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77004">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c605ae8ccf.mp4?token=Mq8l_KERObjiaEhfMy32_y6s65FpcIGvldHithLEN1XTu15UuFUHN9lTHrMKQoPBPEQ4xZVfAxmmIW7S7wf9cIicovX3pAezv0Y44WqHwIsiBhSCPRefZWj7OyNg_zn1ovCbk89xtk-rrjCn2C3cj99Q4WvvkhRsmwYpE9fldtk0MbBe2r2SD9rcoynQIOXY7UXCOWl8Rql9J1GR_x0cnkpLLKgiB32kTtoT3azVMCBlEwToi6qd-MbJkk8G-GCGFSlyIllxfO0nnfImliBs86DXqiBxyHEzvZQlQRvUINPhHewOaqK-adm4LJoyUAtssPgd5LN_e7Nfvrn923fppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c605ae8ccf.mp4?token=Mq8l_KERObjiaEhfMy32_y6s65FpcIGvldHithLEN1XTu15UuFUHN9lTHrMKQoPBPEQ4xZVfAxmmIW7S7wf9cIicovX3pAezv0Y44WqHwIsiBhSCPRefZWj7OyNg_zn1ovCbk89xtk-rrjCn2C3cj99Q4WvvkhRsmwYpE9fldtk0MbBe2r2SD9rcoynQIOXY7UXCOWl8Rql9J1GR_x0cnkpLLKgiB32kTtoT3azVMCBlEwToi6qd-MbJkk8G-GCGFSlyIllxfO0nnfImliBs86DXqiBxyHEzvZQlQRvUINPhHewOaqK-adm4LJoyUAtssPgd5LN_e7Nfvrn923fppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
غارة صهيونية على منطقة المساكن في مدينة صور بجنوب لبنان؛ إرتقاء 3 شهداء كحصيلة أولية.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/77004" target="_blank">📅 20:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77003">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4d0cbb1a.mp4?token=IiTcAAtvkkDAabl7jZId8yf_EVVYc8hx-lA9kGjnLiDqJWhJGa7tNV970Bq5dMqQicrhIMmT8C9p19uvyXb5gQ6KOMTeWeaIlythLLSubPhIWvp__HlDfVmSRskHurwFj6SF0FPH5JKZwzg43BujBVnvVU11SqI-d_1rtyNs6QEGTCGARixK8K_5lih8ZN3w5o7y-9qFzU0FgeTEZ0T-ygDAuaSlK2DYIkXwF6QQurUp9uWZO_NayEaVW5yW0M-mWjX9Yf4MmfzyjmJvLGKWLmrlow1LMu1K6jH1FWdBgXM5p0tNIbUFjCw76gc7z17Ry4b4fI1Q3OTE7o0SKZPOFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4d0cbb1a.mp4?token=IiTcAAtvkkDAabl7jZId8yf_EVVYc8hx-lA9kGjnLiDqJWhJGa7tNV970Bq5dMqQicrhIMmT8C9p19uvyXb5gQ6KOMTeWeaIlythLLSubPhIWvp__HlDfVmSRskHurwFj6SF0FPH5JKZwzg43BujBVnvVU11SqI-d_1rtyNs6QEGTCGARixK8K_5lih8ZN3w5o7y-9qFzU0FgeTEZ0T-ygDAuaSlK2DYIkXwF6QQurUp9uWZO_NayEaVW5yW0M-mWjX9Yf4MmfzyjmJvLGKWLmrlow1LMu1K6jH1FWdBgXM5p0tNIbUFjCw76gc7z17Ry4b4fI1Q3OTE7o0SKZPOFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
جيش الإحتلال التركي ينشئ نقطة عسكرية ومهبط للطيران المروحي على مرتفعات ناحية بادينان في محافظة دهوك شمالي العراق.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/77003" target="_blank">📅 19:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77002">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edbc444708.mp4?token=JamnYx_XDEkb_hNTxykcDxIaTDvTzLdV6_Dmktr6vOd6bmlnevC85Xr2zq2eX5VLOIGQT7D8CUVP1YixolySqLLjz8yh45pthRB-wycc6GhzM5YJiLExIW0O7YdF3ZgPI_ML9XLXHzmHk2DszyhBClufGpry2DMDBl60C5ZD1sjYfKw_dSN_F6BqgrUsh5rfF5-w4yBWHXUEc65Bn2T44ivh2P5G1r42Jr2QhupBp9-0EJmq_SYBMX51GiMgJsKQcwYmNyizLgrWIaX4DLQiWZ1uKZXiyW8L1zgOPBXnRJmxWHJwzTzZ2E75J10l555M7x1vyLIm0dQhzHGHBk5wrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edbc444708.mp4?token=JamnYx_XDEkb_hNTxykcDxIaTDvTzLdV6_Dmktr6vOd6bmlnevC85Xr2zq2eX5VLOIGQT7D8CUVP1YixolySqLLjz8yh45pthRB-wycc6GhzM5YJiLExIW0O7YdF3ZgPI_ML9XLXHzmHk2DszyhBClufGpry2DMDBl60C5ZD1sjYfKw_dSN_F6BqgrUsh5rfF5-w4yBWHXUEc65Bn2T44ivh2P5G1r42Jr2QhupBp9-0EJmq_SYBMX51GiMgJsKQcwYmNyizLgrWIaX4DLQiWZ1uKZXiyW8L1zgOPBXnRJmxWHJwzTzZ2E75J10l555M7x1vyLIm0dQhzHGHBk5wrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
الله أكبر.. تصاعد اعمدة الدخان من دبابات وآليات جيش الإحتلال في محيط قلعة الشقيف بجنوب لبنان بعد دكها بالصواريخ الموجهة والمسيرات الإنقضاضية من قبل أبناء نصرالله.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77002" target="_blank">📅 19:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77001">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581c1b2139.mp4?token=RpFda6vMiHrpRrZELaGZAso_aYw_qBpzbIHG8eBwnSy9T18LCG7WpOTXf1b-LyEuvlDkHgmIxFVrbiyUEWaK8aWoRk0--dAO0ioBmjfH0hD9j3q5EucGnBIVWTt5TOYEZ5xjKin8n89ls-qMATAe2Z2QLzB3c3QkfcJNF7zDgUGXPelXDPmSnbkARGfILBbF3-TlwfyM_jdKjf-DVbTLFHZ8eL0AQ-MZBqEHuNbjIoH4wsH7n7FwLzRpJhbzzYTqza0kE8tIXNt3EOi1BDrDpIYVNyuMT1a3ZT58G7dsjYKlkvGbxtMcW5ZMJe6UU7_ouBA23puRYLSMRoXOxs0nVKKHqpTfQkyZsSbqkuvYX09VK0LLEyDybtUl7luQG_oGlI9mDQqj9NHDVf_QoJE0fBs2qhJwoYbzajAUQWU4Tx5zQ9ob1DVVWtQ7Usi0AK1R_8YaNeJWxcgOUVp9mhESd5yyCIt2IYrUIc0Fd_ThCYNjlrFI6o1z0YeQKTRGtxIWYQo7pnKQf3D9M9L_-7D-4Fr-PEutPuIE53r6YsDRmdY9pRMZXuIkG2K5iScyqZComsCXVMEqhutkhbIFW827Ib8ZhqHGDsa91pI276ljnGDWPL8QibVi7MqyI08eMTODfTTlM8YwT6IlywPX7ohGRw7UHADEgOv48-L6P4U0-PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581c1b2139.mp4?token=RpFda6vMiHrpRrZELaGZAso_aYw_qBpzbIHG8eBwnSy9T18LCG7WpOTXf1b-LyEuvlDkHgmIxFVrbiyUEWaK8aWoRk0--dAO0ioBmjfH0hD9j3q5EucGnBIVWTt5TOYEZ5xjKin8n89ls-qMATAe2Z2QLzB3c3QkfcJNF7zDgUGXPelXDPmSnbkARGfILBbF3-TlwfyM_jdKjf-DVbTLFHZ8eL0AQ-MZBqEHuNbjIoH4wsH7n7FwLzRpJhbzzYTqza0kE8tIXNt3EOi1BDrDpIYVNyuMT1a3ZT58G7dsjYKlkvGbxtMcW5ZMJe6UU7_ouBA23puRYLSMRoXOxs0nVKKHqpTfQkyZsSbqkuvYX09VK0LLEyDybtUl7luQG_oGlI9mDQqj9NHDVf_QoJE0fBs2qhJwoYbzajAUQWU4Tx5zQ9ob1DVVWtQ7Usi0AK1R_8YaNeJWxcgOUVp9mhESd5yyCIt2IYrUIc0Fd_ThCYNjlrFI6o1z0YeQKTRGtxIWYQo7pnKQf3D9M9L_-7D-4Fr-PEutPuIE53r6YsDRmdY9pRMZXuIkG2K5iScyqZComsCXVMEqhutkhbIFW827Ib8ZhqHGDsa91pI276ljnGDWPL8QibVi7MqyI08eMTODfTTlM8YwT6IlywPX7ohGRw7UHADEgOv48-L6P4U0-PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الصهيوني في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77001" target="_blank">📅 19:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77000">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
🏴‍☠️
إصابة مباشرة لصواريخ حزب الله في وادي الحولة بشمال فلسطين المحتلة واعمدة الدخان تتصاعد.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77000" target="_blank">📅 19:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76999">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
🌟
جيش الاحتلال الاسرائيلي يعلن اصابة 3 جنود - أحدهم في حالة خطيرة، نتيجة لعملية لحزب الله ضد قواته في جنوب لبنان تم إبلاغ العائلات.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76999" target="_blank">📅 18:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76998">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAa07NFDK_zXets0Zi6NTfoE47eRNNmyj2RUKZ1q_JDzV6vFlYikoCoP-5CvN67GZRb7bWo1alpQoaPI7gF3UD8Oes4lrzmGOljFK4xhIhTJQyMAkBRkQrF1lkg9Jyw1JIDdJFPmRD3licInbFnYvGAh2UNc3-hw00GDBTHroIfASWlkYfsgTxKLM6-tI_1SP9bIBSRCJn2e98hTSAjGfi9dr0UNg0d_qzTLKub6iNNabGJQOXYnwItCC6cmI-iISc_UEFOsvTDxnP7Rbgq2KNDCYfMuvfsGFgtDvcxwVBbb6F314s3cH3Gq5mf2Dv3Tj2pxCroMhGD8_j4iuL8anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
لبيك ياشيخ نعيم.. حزب الله يدك الشمال المحتل برشقات صاروخية وصافرات الرعب تدوي في المطلة ومحيطها.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76998" target="_blank">📅 18:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76997">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ec8e09d4.mp4?token=V3uuXuDRdMz4coZTiCnVesHlNvEodPjpDEkx2GtrEIEdgwd0DoYu2GPsBn5M_g205CfwVaRM4iw7PC0jrrVmJLPdlvaFMhaoF0SkR-ZNddf-zoFxlALdioFtWa7Rtd5yW48FdfV3dNod5pcr0hwp3l-CHJoVwIThd2OycPsYI18Wixn0c1IlTwsAHYDjcQS2Ax9cTz7nUtAi2qp5eZETxp_sOAcyOSL6WkNjYXK8BFbR9ICiwj42550vBzPe76y_cVHAYu-neEHQgymyR7jWCN7mqJR7KZV4RXhVLVMcyHx4TGBwWMrIGZTowLvjgjSyod864nvwGxIyNfwsb7FbeXCw3AQ5znwdaSMjMrfSSdaBkzv0Jn81ln1fXm9CBUYz0AsZxFiDoldfod6WmE4AVcgTApi7SU1oKQzip2cgiM5NcTc4EpX8hV7jGlgUAadD2uXCc4TSuBqD7fjVFmoyRyI8UPFM6asIe4QBW4HIZAcYgYsCvtICnK5kThc7hMPeyhryw-7H0gdpTQRSD_-Lx0L75EhaLzpY9eW7HUHEbrmhVeeUsVibdo2OAvqAlUdaUksWcLh6KBuxncHuvgqv0YIvBH4zuFrng3JyLhag7NTdOm91xvjG21fx_E4l8ul-W0h1CJ1Gw3z4eDcEvzAuqr6Hfd39r_h9D3n0stJfYCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ec8e09d4.mp4?token=V3uuXuDRdMz4coZTiCnVesHlNvEodPjpDEkx2GtrEIEdgwd0DoYu2GPsBn5M_g205CfwVaRM4iw7PC0jrrVmJLPdlvaFMhaoF0SkR-ZNddf-zoFxlALdioFtWa7Rtd5yW48FdfV3dNod5pcr0hwp3l-CHJoVwIThd2OycPsYI18Wixn0c1IlTwsAHYDjcQS2Ax9cTz7nUtAi2qp5eZETxp_sOAcyOSL6WkNjYXK8BFbR9ICiwj42550vBzPe76y_cVHAYu-neEHQgymyR7jWCN7mqJR7KZV4RXhVLVMcyHx4TGBwWMrIGZTowLvjgjSyod864nvwGxIyNfwsb7FbeXCw3AQ5znwdaSMjMrfSSdaBkzv0Jn81ln1fXm9CBUYz0AsZxFiDoldfod6WmE4AVcgTApi7SU1oKQzip2cgiM5NcTc4EpX8hV7jGlgUAadD2uXCc4TSuBqD7fjVFmoyRyI8UPFM6asIe4QBW4HIZAcYgYsCvtICnK5kThc7hMPeyhryw-7H0gdpTQRSD_-Lx0L75EhaLzpY9eW7HUHEbrmhVeeUsVibdo2OAvqAlUdaUksWcLh6KBuxncHuvgqv0YIvBH4zuFrng3JyLhag7NTdOm91xvjG21fx_E4l8ul-W0h1CJ1Gw3z4eDcEvzAuqr6Hfd39r_h9D3n0stJfYCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله ينشر:
قبّة الطيور ...
כיפת הציפורים...</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/76997" target="_blank">📅 18:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76996">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5e868ae6.mp4?token=qMC90F6Nr550QZ3a4tnAx-zhSFl4CjwVYGvFBVHM8HXfu-BrIqkzjt9iaSI-TBumGynt8ZFwfFYeI71neNgBEIiEIF4SsNvLe-_eq1SU9iMnGFQYqCTJ0rdaOOk8Ow99LVbh-Etgey9F15xAYKQ1inkxuUhuTKhsXrk6lk5RCW6jsA369IR-ZJ8YXY0UtX9v_rbPs9arYKn6I_qtjdIH65EqXrdMEO04BngDij5BTsT4fuZtymDW9oITzMvdmme716wcOnQHImx-PnBTkizJC9Mo2Jc1eIg74RdqX8lE4ApDDBbb_PbuNX05HDPwxG7W5F3LYnV-Sqlp9DAmAe3AOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5e868ae6.mp4?token=qMC90F6Nr550QZ3a4tnAx-zhSFl4CjwVYGvFBVHM8HXfu-BrIqkzjt9iaSI-TBumGynt8ZFwfFYeI71neNgBEIiEIF4SsNvLe-_eq1SU9iMnGFQYqCTJ0rdaOOk8Ow99LVbh-Etgey9F15xAYKQ1inkxuUhuTKhsXrk6lk5RCW6jsA369IR-ZJ8YXY0UtX9v_rbPs9arYKn6I_qtjdIH65EqXrdMEO04BngDij5BTsT4fuZtymDW9oITzMvdmme716wcOnQHImx-PnBTkizJC9Mo2Jc1eIg74RdqX8lE4ApDDBbb_PbuNX05HDPwxG7W5F3LYnV-Sqlp9DAmAe3AOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
لبيك ياشيخ نعيم..
حزب الله يدك الشمال المحتل برشقات صاروخية وصافرات الرعب تدوي في المطلة ومحيطها.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76996" target="_blank">📅 18:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76995">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الصهيوني في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/76995" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76994">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
السيد عبدالملك بدرالدين الحوثي:
نؤكد على جهوزيتنا للتصدي للأعداء بمعونة الله وبالثقة به في أي جولة من جولات التصعيد أو أي تطورات في إطار الوضع الراهن.
نحن على تنسيق تام مع إخوتنا المجاهدين في محور الجهاد والمقاومة والقدس تجاه ما يحدث في لبنان وفلسطين وتجاه الإجراءات الأمريكية الظالمة والعدوانية وما يلزم تجاه ذلك.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76994" target="_blank">📅 17:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76993">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇨🇳
🇩🇪
الصين تحذر ألمانيا بشأن تايوان:
نأمل أن يتمسك الجانب الألماني بمبدأ "صين واحدة" وأن يمتنع عن استخدام قضية تايوان للتدخل في الشؤون الداخلية للصين.
سيكون هناك بالتأكيد ثمن لتجاوز الخط الأحمر في قضية تايوان.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/76993" target="_blank">📅 17:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
🇮🇶
رسالة من الشعب الإيرانية في مدينة الكورة جنوبي البلاد خلال الإحتفال بعيد الغدير الأغر إلى عراق المقاومة والشجاعة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76992" target="_blank">📅 17:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76991">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⭐️
تقرير الوكالة الدولية للطاقة الذرية:
لم تتلق الوكالة الدولية للطاقة الذرية أي معلومات من إيران بشأن حالة المواد النووية المعلنة أو منشآتها، كما لم تتمكن من الوصول إلى أي من تلك المنشآت لإجراء أنشطة التحقق الميداني، باستثناء محطة بوشهر.
في ضوء استمرار عدم رغبة إيران في معالجة قضايا الضمانات التي لم يتم حلها، فإن لدى الوكالة الدولية للطاقة الذرية مخاوف بالغة بشأن احتمال وجود مواد وأنشطة نووية غير معلنة في إيران.
أن عدم قدرة الوكالة على التحقق من مخزونات اليورانيوم المخصب المعلن عنها سابقاً، لمدة عام تقريباً - وهو أمر متأخر جداً وفقاً لممارسات الضمانات القياسية - يمثل مصدر قلق بشأن انتشار اليورانيوم.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/76991" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76990">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇷
🇮🇷
الحرس الثوري الإيراني:
لن يتحقق الهدوء في المنطقة دون انسحاب الصهاينة من الأراضي اللبنانية المحتلة.
لا تزال هذه الأرض ترزح تحت وطأة العدوان الوحشي للكيان الصهيوني الغاصب. لم تُجدِ معارضة المؤسسات الدولية ودول العالم وتعبيراتها عن الاستنكار نفعًا في ردع حكام تل أبيب المتعطشين للدماء، ولم تُسفر تدخلات النظام الأمريكي المتعجرف، الذي يدّعي إحلال السلام، إلا عن تفاقم الجريمة والإبادة الجماعية.
يُعوّض الجيش الصهيوني الجبان العاجز، بكل ما يملكه من عتاد، هزائمه على الجبهات بقتل المدنيين وتدمير المنازل والمستشفيات والمدارس. هذا النظام العنصري، رغم الدعم المتواصل من الولايات المتحدة والحكومات الأوروبية طوال تاريخه المخزي، لم يستطع حتى كسب قلوب سكان قرية محتلة، وفنّه هو حكم الأراضي المحروقة، ونشهد يوميًا تدمير منازل الشعبين الفلسطيني واللبناني المظلومين على يد هذا النظام المعتدي.
لن يسمح الشعب اللبناني للنظام الغاصب بتحقيق ما عجز عنه في الحرب بدعم من النظام الأمريكي القاتل للأطفال، وذلك عبر اتفاق مفروض.
كان شرطنا الأساسي لقبول وقف إطلاق النار في الحرب الإقليمية هو وقف إطلاق النار على جميع الجبهات، بما فيها لبنان. يجب على العدو أن يوقف هجماته على الشعب اللبناني فوراً، وأن ينسحب فوراً إلى ما وراء الحدود الدولية بإخلاء الأراضي اللبنانية المحتلة، وأن يعترف بوحدة الأراضي اللبنانية.
إن الشعب اللبناني فخر الأمة الإسلامية ورمز شرف شعوب المنطقة، وسندعمه جميعاً بكل قلوبنا، ولن يتحقق السلام في المنطقة دون الانسحاب من الأراضي اللبنانية المحتلة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76990" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76989">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وهذا يعني ان اي مواجهة مستقبلية على غرار حرب رمضان فان المقاومة العراقية المذكورة أعلاه سوف تكون بنفس الوتيرة السابقة ولن تتغير اي معادلة اخرى على المستوى الميداني ،، فلم تكن جبهة لبنان بعد البيجر صادمة وحدها ؛ بل كانت مسيرات الحميداوي والكعبي والولائي والغراوي…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76989" target="_blank">📅 17:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
🌟
ابو مجاهد العساف المسؤول الامني لكتائب حزب الله: ما يخص فصائل المقاومة الإسلامية الخمسة، بالإضافة إلى كتائب كربلاء، فإنها ستبقى على تماسكها، وستنجز مهامها ما دام هناك احتلال للأرض.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76988" target="_blank">📅 17:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtQfFVkUXhRjjYd5UfuHtVOxTnJ09i7L0Waj6Wx-kvgh1xEjX6IEpc6Nq6CB4pR6mQVQbMhOlaCDW-g6aB-9CI66pe1aO99PIDtFHR3Wtxor2anEpsfYn0OqBnUJUHxFYMZ22zFaTEltuFLAJwctMQWoWnGRiJ22_U8VoMTBb8R_GuaK51yumLuDK0R-CM1htEYRZ-BmJWoQaHzLWJ88G3tc8ojXWfCL4HEYwcPau_gPpklgRB0oWdri7Yyxg6mF-XzKifpX9hqlt7YFlV3O2LNqXPFK9tiJAKJTNqeR7aH8Wxge7u1fQIwzqjS7aL67Sa5N9sY1hDvzvS2d3H-nEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
ابو مجاهد العساف المسؤول الامني لكتائب حزب الله:
ما يخص فصائل المقاومة الإسلامية الخمسة، بالإضافة إلى كتائب كربلاء، فإنها ستبقى على تماسكها، وستنجز مهامها ما دام هناك احتلال للأرض.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/76987" target="_blank">📅 17:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76986">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dgbel5uKSPP6QwJ05WpzX3B2_IwygiG1L424tdDkcgvPd-cu_z0IIc5xRfB4hhaSCp3Jd8PeSVHVkxTCPPyFB4cu2FiyRhYzkbW3BhSDdLf3eiKeFoQp30J_owVOfBy7o1MZEh-njEMf037J2FP8i4UyJoXbPlDaPpo9ddbQMt0ZYOml-He4gEHfWFy-sBrZj1hn97RTT2JPsM0KHeiX8rb8xG1NOyWigpsXexaQrxHamSD79n7lV1Mx1rxnxt1evHbtsoyoYRCF9AZbXEq4xGbw0dzvKcezqFg5yVn4IkMB61z6-zVkAO9nPss3xBu_nSD36Wv6R1h99ImildYmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
سلطات آل خليفة في البحرين تعتقل عدداً من الأطفال من أبناء الطائفة الشيعية
1.سيد سجاد سيد فاضل الموسوي
2.سيد قاسم سيد ياسين الموسوي
3.سيد محمد سيد ياسين الموسوي
4.سيد حسن سيد ماجد سيد فاخر
5.سيد عباس سيد جعفر
6.سيد حسن سيد حيدر
7.سيد ماجد سيد هادي
8.سيد محمد علي سيد نجيب
9.علي حسين جميل المرزوق
10.محمد علي صالح
11.علي عيسى
12.علي حسين جارالله
13.امين الحواج</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76986" target="_blank">📅 17:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU8EALQqnNa2oHtYMZW7lTib-sGJg_uxtFuiakHAPH-tBA84CjhDJkRpK7sxhFPJX8dDenAiMw0Y87gvBicRvj_InEV_FZXq2f0d7w8uwBTeV0__m_SxplCqX7CmW2e2r7j3T9mC3Pgx44vZS3qoC5iZ5aKYngxlNC5z4r0x72OGoGO83M1IiVXYUxQQ6mkRm2egU9W1OWLHWMgquZEPqvK0chfhObTB4th3fumV25REZy1qArGyK8Zq_XaCcNiOpPg1r_e9w9XBLxWFMHrcPuPZm0PrbMFIIv7oe5-dSvDRkwp6-y9QkGDgpJ8rlNgZ3GuV6y_2vo1x3f7qyOxzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بزشكيان
:
لقد كان الحفاظ على الوحدة والتماسك والتضامن هو الإطار النظري والأساس للحكومة التوافقية.
‏استناداً إلى تعاليم الإمام الأعظم وقائد الثورة الشهيد، وفي ذكرى صعود الإمام إلى السماء، التي تتزامن مع عيد الإمامة والوصاية، نجدد عهدنا مع القائد الأعلى للثورة بحماية وصون هذا الكنز الثمين.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76985" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76984">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e658e4f43.mp4?token=kqOIWeJ4ktGBwJ9pcW_9eYoQp2JZKHA-KdSP9FzqvV1L5hAlXn2wjZY0kpDpV89FtTV40dnvudeHFs22jmTExtS_g76w5zcr09_Npbc7mi8ITubS8lCA5aMBHULQEjb1nmj39r1f1DC3P-40_S_JzJTP5sIOHp7DOLImK7BxPUa2DjMKk10TasYGM76ooyf2QJTk_ZCPDdJtQ_D9mo9fM71xAJRk_Mbc06s7SsVIAKloG_OqbmheG8Xi84yFcsdPm90g834AlTS4FxOfAk16USyVWxHAvcFeNe_u7Cy8s9kQvO6nJXEzDUKQZWoAgxNeC6ajszU2YHg0pCL-135QhJZ0HbAjl2rWSS4PDNLfrZv2fAXFVuIkdAEPqTGzP9PHgNdu27-Ixj7Kzu-Oc0ydImRQ_rrJGti9SXpYtuaP1TNWYythN4OaPC7NUCuA0xy_RGClv69Z81EvKdWlnLvA6MIPczcHcGi_xqqxfysFMJXZM9yltcx6HoMzyW04awEXLCdbhCWWbNoZJW7dMU5o-UodoCk3eK3w3n5pzw95tsIomJONxoy8YtDeOg7NOboAyCFj70mNYJc7z_vMsTwdZZIQhJU-nIfLwGanALLfvtyNrgvqgfqy6ENN-HdoclTJ19ZtNdTD1l6OdK_6dh2Umx4dskogeiq9YIE2T9etDL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e658e4f43.mp4?token=kqOIWeJ4ktGBwJ9pcW_9eYoQp2JZKHA-KdSP9FzqvV1L5hAlXn2wjZY0kpDpV89FtTV40dnvudeHFs22jmTExtS_g76w5zcr09_Npbc7mi8ITubS8lCA5aMBHULQEjb1nmj39r1f1DC3P-40_S_JzJTP5sIOHp7DOLImK7BxPUa2DjMKk10TasYGM76ooyf2QJTk_ZCPDdJtQ_D9mo9fM71xAJRk_Mbc06s7SsVIAKloG_OqbmheG8Xi84yFcsdPm90g834AlTS4FxOfAk16USyVWxHAvcFeNe_u7Cy8s9kQvO6nJXEzDUKQZWoAgxNeC6ajszU2YHg0pCL-135QhJZ0HbAjl2rWSS4PDNLfrZv2fAXFVuIkdAEPqTGzP9PHgNdu27-Ixj7Kzu-Oc0ydImRQ_rrJGti9SXpYtuaP1TNWYythN4OaPC7NUCuA0xy_RGClv69Z81EvKdWlnLvA6MIPczcHcGi_xqqxfysFMJXZM9yltcx6HoMzyW04awEXLCdbhCWWbNoZJW7dMU5o-UodoCk3eK3w3n5pzw95tsIomJONxoy8YtDeOg7NOboAyCFj70mNYJc7z_vMsTwdZZIQhJU-nIfLwGanALLfvtyNrgvqgfqy6ENN-HdoclTJ19ZtNdTD1l6OdK_6dh2Umx4dskogeiq9YIE2T9etDL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية
آلية هامر تابعة لجيش
العدو الإسرائيلي
في
محيط بلدة زوطر الشرقيّة
جنوبيّ لبنان
.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76984" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76983">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IF7WHre-C4vjo73kf1w2lvikGNJ6ecuemLUFW1jvgNU8siYxThikOp_-6W8GJEIA_mxSn1ilxr-ekIgXRIDw1xVMF2ssCC7TZxBSUNPF2MXCXq_rskqOY4RW95gabO4N5q6fjhBhjnYzxh3M4miYKwPSYD6g14sbuwYcZBxRkIF2yiaLUqJfn39zY31ArgtlY0oikJz7Au7bw-FQI7xlonDjFEv4Zt61eCChEGdc0BvViWTXnx-rE74jzXgCqkGMmBtQWeuT3vrVTK6VoeVtItkVCx4I39IArfuOehZKtiAzu9oTSewfhVwY4F9g4A4mU2ssuzklxVvRPxLX95I33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
بالتزامن مع زيارة نتنياهو والنائب سوخوت إلى شلومي، أطلق حزب الله صواريخ استهدفت المنطقة بشكل مباشر، ما أدى إلى تفعيل صفارات الإنذار ومغادرة المسؤولين الموقع قبل وقت قصير من القصف.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76983" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76982">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKhUjrzCpKxadJU-mexkOrYsFapdpfheAYR8qotA3Npxjc_3teK5qxb6PL5YjkgP6e2DhwB8nVMhXNchy0l1YwL1N7jqdb4m2ZFX-rnsNFggrRv_KTK-ahQhB6IckCnNbNuDB9blh14FthLlovjIPKwMeByD985jjKGpRy69i5yojucgcTK8XGNvz5caiGeDmHFQO1vwq8jK8wUfXjL_DSbjxTO6TLoU0Yvqz_k3Zf6DwR7wymq4qUyW2olBDci2WlVkGMbj4EZPgtfTlRf6rfUwcnC2EfkirirOfq0jnul4advOlK5muSIU9TclJOAj7csvHRGLklXE0HGpQp1h3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
بالتزامن مع زيارة نتنياهو والنائب سوخوت إلى شلومي، أطلق حزب الله صواريخ استهدفت المنطقة بشكل مباشر، ما أدى إلى تفعيل صفارات الإنذار ومغادرة المسؤولين الموقع قبل وقت قصير من القصف.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/76982" target="_blank">📅 16:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76981">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌟
🌟
جيش الاحتلال الاسرائيلي يعلن اصابة 3 جنود - أحدهم في حالة خطيرة، نتيجة لعملية لحزب الله ضد قواته في جنوب لبنان تم إبلاغ العائلات.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/76981" target="_blank">📅 16:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOh4xyk_KpzplPupFb0giY_GbL4oTKpcvR_mQ3ilEIUwoVnJ1up7nDzzX7548dfFworIqLwvMbEC7V3zKsHj5-EqKbea_cY0Uojx5UAw13315QRz6_wmHuXHdCu-Yfe4gQVeXwBq8yRJ4oSmxpqzkobY7SPgixgWq9Yx5xkVAhxzdcLpMov_VYkp6N5NDZCt166_roTnq_L2HMNCgYP0UyL2lJRwwaojM9DBVUEcdqDBQkhIpMlf6gxrf9MPc3WuQRNiaxghakAonkuhCALtmf83CtaHbbj6Ww11uOxgkM0fH_4TBufA5FAxY83rOpTVq80xgHCnRlxfUvvz8aH02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اعلام العبري: بعد أقل من ساعة من إعلان الشيخ نعيم قاسم: سلسلة من الإنذارات وعمليات التنصت في الجليل الغربي، بينما كان الأطفال في طريق عودتهم إلى منازلهم من المؤسسات التعليمية.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/76980" target="_blank">📅 16:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
دويلة الكويت تصدر حكماً بالسجن لمدة ثلاث سنوات بحق مواطنة، على خلفية تعاطفها مع القصف الإيراني الذي استهدف قواعد الاحتلال الأميركي.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/76979" target="_blank">📅 16:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76978">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الله اكبر...بعد بيان الشيخ نعيم قاسم حزب الله يطلق رشقة صاروخية مع سرب من المسيرات نحو المستوطنات الشمالية.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/76978" target="_blank">📅 16:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76977">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx2DPdM6ZWePnrzwK3Uoh1qfHkN4snEPATBC4W1_Ff-yzK0x2vxXxwh9bbeIgbeTbj1bLHTOxsRg_vKUQ4Mp9ETp2ksfW2FjXTvkBfzIZlJnL_NJ_alfYO3kzOscIJyxpawyCC54VylppfUrMj4j8TVe_ttu1IX-6qgjNwCQd-kSduPQ22jzyT-r4sthQBQ2c3S6Ed8gxSzo_dcGH5zvDw51mL4ewtv8FQs3TwdozrdSpWZDnL6w69SfpX0wCbtizrm1_uazRGPG693gmXWixy3a8CPgkvqXPfE_zs6pBwSRBI5zULzvah5KiakNfFr9NihQSNuDVP7o_mUBTB_TPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الامين العام لحزب الله الشيخ نعيم: الاعلان هو خارطة طريق لإبادة قسم من الشعب اللبناني واستبعاد الباقي. جاءت نتيجة المفاوضات المباشرة العبثية والمذلة والمخزية للبنان، وهي المرفوضة جملة وتفصيلًا من شرائح واسعة من الشعب اللبناني، بإعلان واشنطن الذي يرسم المبادىء…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76977" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:  بيان حجة الإسلام والمسلمين الأمين العام لحزب الله سماحة الشيخ نعيم قاسم في ذكرى رحيل الإمام الخميني (قدس سره) وحول الأوضاع السياسية:  بسم الله الرحمن الرحيم   الحمد لله الذي أرسل لنا الأنبياء وسيدهم رسول الله محمد(ص) بالهدى ودين الحق، وبعده…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76976" target="_blank">📅 15:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:
بيان حجة الإسلام والمسلمين الأمين العام لحزب الله سماحة الشيخ نعيم قاسم في ذكرى رحيل الإمام الخميني (قدس سره) وحول الأوضاع السياسية:
بسم الله الرحمن الرحيم
الحمد لله الذي أرسل لنا الأنبياء وسيدهم رسول الله محمد(ص) بالهدى ودين الحق، وبعده أئمة الهدى المعصومين الطيبين الطاهرين، وتابَعهم الصحابة الأخيار المنتجبين والعلماء الربانيين ليكونوا جميعًا مقياسًا للصلاح والاستقامة وقدوة للبشرية.
أولًا: تحية إجلالٍ وإكبار للإمام الراحل الخميني العظيم، محيي الدين، ومحطم جبروت المستكبرين.
لقد وفق الله تعالى البشرية بقيام نهضة الإمام الخميني(قده) وثورته الربَّانية في إيران، في ظروف كانت تسيطر فيه أميركا على إيران ومقدراتها وتستعمر الكثير من دول العالم وفي منطقتنا، طغيانًا وظلمًا. مقابل سيطرة الاتحاد السوفياتي على جزء آخر من العالم.
هذه الثورة انطلقت من خلفية إلهية إسلامية على مبادىء الحق، والعدالة، والاستقلال، وحرية الاختيار، والوحدة الإسلامية، واحترام الإنسان، ومقاومة الظلم والاحتلال، ودعم المستضعفين في العالم. أقامت نظام الجمهورية الإسلامية الإيرانية باستفتاء شعبي، ووضعت دستورها وقوانينها، وأعلنت بأنَّها لا شرقية ولا غربية.
الإمام الخميني(قده) ومن المنطلق الديني والخيار الفكري والثقافي هو من تجليات الخط الرباني لكلِّ البشرية، لمن أراد أن يختار منهج الحياة الإنسانية المستقيمة والعادلة، ولذا سارعت فئات شعبية كثيرة في العالم إلى تبني قيادته ورؤيته الإيمانية الربانية، وهذا حقٌّ مشروع، خصوصًا بالمقارنة مع خيارات فكرية أخرى أو مادية أو معادية.
لم يترك الغرب ولا الشرق لإيران أن ترتاح في خوض تجربتها السياسية بقيادة الإمام الخميني(قده)، فخاض المستكبرون حربًا ضد إيران لثماني سنوات بواجهة صدام العراق، وبحشد من قوى عالمية وإقليمية لإسقاط نظام الجمهورية الإسلامية الذي واجه الحرب بتضحيات مليونية، والحصار الاقتصادي والدولي، بصمود قيادته وشعبه وحرس ثورته وجيشه وقياداته ونُخبه. ومع كل الصعوبات والتحديات تقدَّمت إيران على جميع الصُّعد، ودعمت حركات التحرُّر وجبهة الحق، وهي لم تتدخل في شؤون أحد. وكانت درّة المواقف النبيلة العظيمة مساندتها للشعب الفلسطيني لتحرير أرضه والقدس، ومساندة حركات المقاومة ضد الاحتلال الإسرائيلي المجرم الذي يشكل خطرًا على كلِّ المنطقة بل كلّ العالم.
الإمام الخميني نموذجٌ للقائد الرباني المدافع عن الحق والكرامة الإنسانية. في المقابل نموذج الطغاة من أميركا وإسرائيل وغيرهما، و الذين أشاعوا الحروب والفوضى والإجرام والإبادة للأطفال والنساء والحرث والنسل على مستوى العالم، وهذه غزة نموذجٌ صارخ أمام مرأى العالم يوميًّا. من نختار للعزة والكرامة الإنسانية والاستقامة؟ لنا الفخر والشكر الذي لا ينقطع لله تعالى أن اقتدينا بالإمام الخميني في منهج حياتنا ودعمنا للاستقامة والحق.
لماذا حاربت أميركا والغرب والأذناب إيران لمدة سبع وأربعين سنة؟ لماذا يحاصرونها؟ لماذا يريدون منعها من امتلاك القوة الدفاعية وهو حق مشروع لكل الدول؟ لماذا يريدون منعها من تخصيب اليورانيوم السلمي المسموح بحسب القانون الدولي؟ الجواب: لا يقبلونها نموذجًا للاستقامة والعدالة والاستقلال، بل تابعة ومسخَّرة لمصالحهم وطغيانهم.
شنت أميركا والكيان الإسرائيلي حربين على إيران، واغتالوا القائد الرباني الإمام الخامنئي(قده) وعدد من القيادات العسكري والسياسية والنووية، وقتلوا المدنيين والأطفال في مدارسهم ودمروا منشآت مدنية .. ظلمًا وعدوانًا واضحًا أمام العالم، لإسقاط النظام والسيطرة على إيران. لكنَّهم لم ينجحوا ولن ينجحوا مع هذا الشعب الخميني العظيم الذي تربى على نهج الحسين والتضحية والفداء، ويتألق إن شاء الله بقيادة الخلف الصالح القائد أية الله مجتبى الخامنئي(دام ظله).
استلهمت المقاومة في لبنان من منهج وفكر الإمام الخميني(قده) لتحرير الأرض من العدو الغاصب في المنطقة، ولكننا نقاتل من أجل أرضنا وشعبنا من خلفية طاعتنا لربنا أن لا نكون عبيدًا لأحد، وأن يعيش أجيالنا حياتهم مستقلين في وطنهم مع أهل بلدهم. هذه المقاومة هي زرع الإمام موسى الصدر(أعاده الله سالمًا) ومسار سيد شهداء الأمة السيد حسن نصر الله(رض)، وهي متحالفة مع قوى سياسية ومن فئات مختلفة تؤمن بالمقاومة وتقدم التضحيات في سبيلها.
ثانيًا: في ذكرى رحيل الإمام الخميني(قده) ، الذي يُصادف عيد الغدير وولاية أمير المؤمنين علي(ع) رائد العدالة ونصرة الحق، نستعرض أوضاعنا السياسية المتأئرة بهذه المناسبات الجليلة، تثبيتًا لنهج الأصالة والحق.
الشكر لإيران أنها تساعدنا لاستعادة أرضنا وحقنا في مواجهة العدوان الإسرائيلي الأميركي رغم مواجهاتها الكبرى. وتتصدى لتثبيت وقف العدوان وإطلاق النار الشامل في لبنان كجزء من وقف العدوان على إيران.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76975" target="_blank">📅 15:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بيان_قائد_الثورة_الإسلامية_بمناسبة_عيد_الغدير،_والذكرى_السابعة_والثلاثين.pdf</div>
  <div class="tg-doc-extra">1.9 MB</div>
</div>
<a href="https://t.me/naya_foriraq/76974" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇮🇷
بيان قائد الثورة الإسلامية، آیة الله السيد مجتبى الخامنئي، بمناسبة عيد الغدير، والذكرى السابعة والثلاثين لرحيل الإمام الخميني (قده)، وذكرى بدء قيادة الإمام الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76974" target="_blank">📅 15:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76973">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhJHyrxoRgPcwZ71nmbT1zoPR1fVHEcJtVMKPs_2WTXnBiVZkF5F29eJgonLLNjvxOSHIfOeHc1s-KNewL77DHGZ969I2uc3FbOxDo5qs1L3q4VO9h4fcmQGBR0GgqKcB4GUspEI8kmycH7_EbheXQsuA6_9MlFGiSMqEyVkx_dvE-r1G267Hh59oPmGsImuYWrc3_3C_OmwBs7cKnYweLuRnaDggdPjNJ00CRQXPvOul12Kr4np2aGHHD64E3TiOjuxR4J3uqWFouBQnPoX7NMQdQB7KURWZFTqr2C9Txh2gQIr9v_TvBo4yQ6u7mS7AKQMXSs6IbyXG2tcO9Fiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
:مجلس النواب صوت، بدعم جميع الديمقراطين وأربعة جمهورين، لتقييد صلاحياته العسكرية في وقت يقول إنه يقترب من إنهاء الحرب مع إيران، معتبراً الخطوة “غير وطنية” ومتهماً خصومه بالسعي لإفشال نجاحاته السياسية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76973" target="_blank">📅 14:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76972">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11fe7d926a.mp4?token=MM1mh5xEEmQBvV9E8LJaFWtmxzR0-f1wjsGqSVQpNMBr2tJZq8btcaIqFrADA00SDB6OjhwON2mpFpZSbDyP4PhRq_REHnCl-vMiD4SrxbhAV36Y9P7gft7JcWbYIeXQWncvTMryU7mM35Q1yFKQ__rfHBig1-KRY4hbg5eE08KUfaVewmv_moZAeA37GdvPRO-JbDMpDuZ8XsEcZ70Le2R4-ZfGG-1WdG8I_3HM7xaAgTn3XOSToRSyP0Pr1-EupgBEH4rLiUes1OkftzjEdl_lM7tyF6Wd3Wa_9MnfOPCnl9airMQByRxh4IAOT_cE5dqutAYR0Jjgea2sWaSRW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11fe7d926a.mp4?token=MM1mh5xEEmQBvV9E8LJaFWtmxzR0-f1wjsGqSVQpNMBr2tJZq8btcaIqFrADA00SDB6OjhwON2mpFpZSbDyP4PhRq_REHnCl-vMiD4SrxbhAV36Y9P7gft7JcWbYIeXQWncvTMryU7mM35Q1yFKQ__rfHBig1-KRY4hbg5eE08KUfaVewmv_moZAeA37GdvPRO-JbDMpDuZ8XsEcZ70Le2R4-ZfGG-1WdG8I_3HM7xaAgTn3XOSToRSyP0Pr1-EupgBEH4rLiUes1OkftzjEdl_lM7tyF6Wd3Wa_9MnfOPCnl9airMQByRxh4IAOT_cE5dqutAYR0Jjgea2sWaSRW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 30-05-2026
تجهيزات فنيّة تابعة لجيش العدو
الإسرائيلي في بلدة رشاف جنوبي لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76972" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76970">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdES7GaNisr55CLlKETCLPCjSj0vdSvN_QmieWyemYpIVXvjUE4Z4ZiOgrbM9bLsRHzZ7mlmSEIJD0JhrL7MwwqHBm3PG2YeJzCN9L1mESU5B3gnmaFj2tn81oVZgnY8Wsa2-1iBTWXAdfY7mG3m8-hdOixQdde6_CNznnQv6I79whb-OxHrqaiqRkgSyx0Xl9B3J24ILbnNPPEGOki03kvqBn0Ap0gpz9ZuH-oer_dQLjwUMFpH0bE7WS__KsrQuGxk7tWxtmwxenHjDdk1owsKQAIM0VWriJLhO2nHggBCQPqFbZ5EOEbQTjhJEndLJqgnA5FDgHiri2UtT3gDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس التابع للحرس الثوري الإيراني:
دعم المقاومة في لبنان واجبٌ علينا جميعًا، وإخراج إسرائيل من المنطقة هدفٌ قابلٌ للتحقيق للمسلمين. جوهر مطالب المقاومة هو انسحاب النظام الغاصب إلى ما قبل بدء حرب الأربعين يومًا. سيجني المجاهدون اللبنانيون قريبًا ثمار مقاومتهم الباسلة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76970" target="_blank">📅 13:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76969">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdC3ob9b8K6n33Eo5Ky0DnNnxriQdnzMWTuBW8LD6RpZgMf7z6MNaleoAkDHvk_VzBSHl15FpQzom3fdyQ4NEdhB_YO8VhS3IgvdTMp9EuKFz_Cc6xgHrDwSUAyXTOazJQASiPPyvnXBjrtlFIjTQm4YYawIceRXiZouwoGMhq7IA2j2WogUU6N27bD6x1ZmXXhwkIX24ftLfYm4ISs4kDpDXWHxkYX8AkutVIDZcDVk2UMEIQrfiVkZkJA5-p11FPRf7eh1EBAKYNI-49d91Q0XFt0kj1Ab3MygJZ_sY7zYv6kb2eVvy7od_hp_eG3-AnyVQrNkON1how_BujcgrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وفاة المرجع الديني آية الله العظمى الشيخ محمد إسحاق الفياض بعد تدهور حالته الصحية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76969" target="_blank">📅 13:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76968">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8d0ac34d.mp4?token=lVSmSGhTBG0DEUKIuRlpDBziLXsM1Gsf-iv3AuCReofombBpbP35JizdlmDRPnIMfejoZGKmxW1ULswkgbP20VbU4Vo6oJSma58PXEQ8LT9TxNq8PwrMTCDmFC64eJ1giSvbzZYvZ6qtmCrfzgXYvB4u89-vMpf8olA5pbnbmix0LpsR0ta0Yib_U6XLtc8NSYrCP8sMGwPH_9242TI20-5maFqTURQETZli5m1TuQbhqSL0U6krdE2LJpEEfcz9EUGoD3nU7unY2TcBCQxNQzrIZXW-tL_HPP9eGs1AhGd-w1ghzJ6MYCzHjRwKZDUk5u6-nomDoZd_JbVmxpUn6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8d0ac34d.mp4?token=lVSmSGhTBG0DEUKIuRlpDBziLXsM1Gsf-iv3AuCReofombBpbP35JizdlmDRPnIMfejoZGKmxW1ULswkgbP20VbU4Vo6oJSma58PXEQ8LT9TxNq8PwrMTCDmFC64eJ1giSvbzZYvZ6qtmCrfzgXYvB4u89-vMpf8olA5pbnbmix0LpsR0ta0Yib_U6XLtc8NSYrCP8sMGwPH_9242TI20-5maFqTURQETZli5m1TuQbhqSL0U6krdE2LJpEEfcz9EUGoD3nU7unY2TcBCQxNQzrIZXW-tL_HPP9eGs1AhGd-w1ghzJ6MYCzHjRwKZDUk5u6-nomDoZd_JbVmxpUn6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حديثة توثق لحظة العدوان الامريكي الذي استهدف جسر B1 في الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76968" target="_blank">📅 13:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEVKpe8jSdCUpm3e2tXSami6CGi2wtf56J1GWRxQHL9juYtyLemJTq3d4D2OV7dW7t1QQfwQP8KMqwQNIvsN5rCUSgv7wYPOB3mpQ4GJnII0MGhj6uvEosvUmxcR7r87Yqzf9UHvVc6aAe2Cwtdbh3na591aOs3IzskPEHYjjSVJtruSdO0nnZgvn2wHcMYQX35JqU0BIhr3IyghOCJMPMarHDbNzD9hQcIxPGE9mzQl4AlpdS3bVUotjW0_o0-AlnmHF0KvN0T0HxcCndXITbIZju-DR7fHIBNQcBIVq0urFSyQ4FKTwgwGNVpVmJIOw8V0Jlh8KrlZHC7RHuEp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتل جندي أمريكي في قاعدة الحرير اربيل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76967" target="_blank">📅 13:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🌟
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 31-05-2026 تجمّعات لآليات وجنود جيش العدو الإسرائيلي في بلدات القنطرة والطيبة وفي محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بصلياتٍ صاروخي</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76966" target="_blank">📅 12:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏اعلام خليجي عن مصادر: الاتفاق حول الإفراج عن الأموال الإيرانية المجمدة بمراحله النهائية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76965" target="_blank">📅 12:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇱🇧
اليونيفيل: وفاة جندي وجرح اثنين إثر سقوط قذائف على موقعنا قرب مرجعيون جنوبي لبنان</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76964" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76963">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 02-06-2026 آلية نميرا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76963" target="_blank">📅 11:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76962">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctLzCShIqKa6wMMvn3_w8-n1WdYvjHnVtUvj3-1Z5FfDvTGI438gHQxqVCsH4v9cyiM1jVK48m3XtFjaMo39NiL78t6TDsTISY_BhlXIJDMEHPkuVI3Sm3ft_NeQ-hajbLvWMAvqBYYBggkMiQwkuKyJwvL84hFlw9-CwPMGHLO1Y8_1LqUKMjpk0Uy_7tYuK5pF3Mvs9pRkTxmbCXu2O5higkvoXN4xilTrHvQ3N9imvvcZE2YtzLljUVr9Y5jIuH_asXiqArucKZ-bRYSp5QCrpjziKYyIv_Z0kMOWyAmdvYCDwWmp-qFhgugUgIfm4mbz5fYRPmXT2clYL7LHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇺🇸
نظرة من صور الأقمار الصناعية
على الأضرار المدمرة الناجمة عن هجمات الفصائل العراقية البطلة من معسكر فكتوريا التابع للجيش الأمريكي في العراق قرب مطار بغداد الدولي ؛ وقعت الهجمات في مارسو أبريل 2026 بواسطة مختلفة الأسلحة ..</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76962" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76961">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سرايا السلام تسلم ملفها إلى القوات الأمنية في مقر قيادة عمليات سامراء المقدسة</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76961" target="_blank">📅 11:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76959">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6b338b2a.mp4?token=YFDwTu9tup5euWXvi2dZJCQgdx8iZcfi1QfYszyr49Drz7tiWUJ17TfsQg5KgBR3InmYxgc3WIuO9tx0fQm9aUtHPDErD6FL_CGTLLMcG_CW4sqZySxCC6LwT5xdM_YW98_teX2LlBq0JPVIREh5gTi23WCc04SPQnQTpkXI3Md0cGgCKj_bZuOVHgSMKb8p-AyN7JfbtfJz1Ws8kkMsBhb6Yq9O9VHZjxQfaEbhR3bbCXBUuEM1ziPJmS9lNkjzT6XnfQdYGkHJJGulJsT4NmzvMng2T8U5P3EFqKNTx9xP2LiOqUB9P1DSpG4Y5HO95CpFZSKOnNIXvmraI1hNonLWlV62FdDkYP32m464ViLJ-_Igi2cKyeJBqugdRAZb7UEDoZjIHIK2vjk9hSPJ5Mf_e31PQLRQDlK1LAnAYcOGFAIo4WQnMaEg6bJB9NusqE930n2ytYXajeKaG6rgUOej5BIVvyjmIUDJCm4LNkQEB-jxVD3ClWGRjRE7WG9QL5RCKNlcBy1V1I343H4x0fb0BksT0tc4pTcQfq3wKtqLya4d7odKbQhnmv1XPPGOQovNUEGF8qs2oQe8EUMpQe8mym-LmCo0NzWiwR0wurVCC_aYUhn2NGYc2sX8xlb-jPCeCcZmTzrPdwyiZssw0Rv8chlzdqsgMK08TPje6oU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6b338b2a.mp4?token=YFDwTu9tup5euWXvi2dZJCQgdx8iZcfi1QfYszyr49Drz7tiWUJ17TfsQg5KgBR3InmYxgc3WIuO9tx0fQm9aUtHPDErD6FL_CGTLLMcG_CW4sqZySxCC6LwT5xdM_YW98_teX2LlBq0JPVIREh5gTi23WCc04SPQnQTpkXI3Md0cGgCKj_bZuOVHgSMKb8p-AyN7JfbtfJz1Ws8kkMsBhb6Yq9O9VHZjxQfaEbhR3bbCXBUuEM1ziPJmS9lNkjzT6XnfQdYGkHJJGulJsT4NmzvMng2T8U5P3EFqKNTx9xP2LiOqUB9P1DSpG4Y5HO95CpFZSKOnNIXvmraI1hNonLWlV62FdDkYP32m464ViLJ-_Igi2cKyeJBqugdRAZb7UEDoZjIHIK2vjk9hSPJ5Mf_e31PQLRQDlK1LAnAYcOGFAIo4WQnMaEg6bJB9NusqE930n2ytYXajeKaG6rgUOej5BIVvyjmIUDJCm4LNkQEB-jxVD3ClWGRjRE7WG9QL5RCKNlcBy1V1I343H4x0fb0BksT0tc4pTcQfq3wKtqLya4d7odKbQhnmv1XPPGOQovNUEGF8qs2oQe8EUMpQe8mym-LmCo0NzWiwR0wurVCC_aYUhn2NGYc2sX8xlb-jPCeCcZmTzrPdwyiZssw0Rv8chlzdqsgMK08TPje6oU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الضريح المقدس لمؤسس الثورة الإسلامية الإمام الخميني قدس سره خلال مراسم إحياء ذكرى رحيله.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76959" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76958">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وفاة المرجع الديني آية الله العظمى الشيخ محمد إسحاق الفياض بعد تدهور حالته الصحية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76958" target="_blank">📅 10:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76957">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f58636b4.mp4?token=HsJ7s-ZEY6Uu-sbGsrzQuslIi20zsvs69luLMdLUAHU-L1E5sPfgdvYm9LqkBROIWOZlRxZrhdOFibB2ICk_IXsjJAx0uGleoeKYcaQSY0YYdjaayWI-Ht5X5D_d5Jcqn5iRJ6Xec5hAbY3KH5hc_HrES6NYXwfz2ZW2ZX1ohqpA5swdl_Cala4OS4qumMCnCzsIGK_vJhSGDMa1S-11Ac2rPIcZlzK6DWC4JGUBJHo9UDR_802Ss9JGfAGhpfkCdvt8sm19SB0JzevkkoRGrz7sGGtncUY5-0QNlukxiR_9vNhqTkSlIzxeTQ7GwhzHrPKYQUevy9bXznpzSsEvsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f58636b4.mp4?token=HsJ7s-ZEY6Uu-sbGsrzQuslIi20zsvs69luLMdLUAHU-L1E5sPfgdvYm9LqkBROIWOZlRxZrhdOFibB2ICk_IXsjJAx0uGleoeKYcaQSY0YYdjaayWI-Ht5X5D_d5Jcqn5iRJ6Xec5hAbY3KH5hc_HrES6NYXwfz2ZW2ZX1ohqpA5swdl_Cala4OS4qumMCnCzsIGK_vJhSGDMa1S-11Ac2rPIcZlzK6DWC4JGUBJHo9UDR_802Ss9JGfAGhpfkCdvt8sm19SB0JzevkkoRGrz7sGGtncUY5-0QNlukxiR_9vNhqTkSlIzxeTQ7GwhzHrPKYQUevy9bXznpzSsEvsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
انفجار مركبة على الطريق 20 بين حولون وتل أبيب مقتل صهيوني وإصابات عديدة كحصيلة أولية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76957" target="_blank">📅 10:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76956">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: منذ إعلان وقف إطلاق النار، أطلق حزب الله 6 صواريخ باتجاه قواتنا العاملة في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76956" target="_blank">📅 09:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76955">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏴‍☠️
‏وزير الدفاع الإسرائيلي: الواقع الذي فرضناه بلبنان يقود لاتفاق يحقق أمن سكان الشمال لأول مرة منذ 50 عاماً</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76955" target="_blank">📅 09:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76954">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قناة CBS: مقتل شخص وإصابة 3 آخرين نتيجة إطلاق نار أثناء حفل تخرج مدرسي في مدينة فيرفيلد الأمريكية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76954" target="_blank">📅 09:14 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
