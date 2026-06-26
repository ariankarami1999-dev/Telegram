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
<img src="https://cdn4.telesco.pe/file/uTaIMdr-YgfQFrpbEsWQClbZ-9T7MzWhbMPkrZ21uNNbmEsn5zwmaCM_Ezgv24m6qICRXvAhAa7nxXR1f3ypexwniP4w3h33b7q7FgpsVbKBpPlyJp_J8EWpNWmbodwKsEECjj68v8jEg7NuSxTPZXu1FF4_7UnGmwpsRX3YY0s1UP8yQkTWq_jvX4FndsgB_nyTKu5hxqjQlY-OQSNNJx2BvrwQx6_NqzvlorHJUl1VztGjNNMjJWbf5dV1DkuiN4VCfZC9m8etrI9bl1ygNdil9iAgbNJoZSfQnvF8oxwBvqs_LkFEtTau8a1ytZJSlxzyvuCw0407_w7BVGlxKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 00:32:49</div>
<hr>

<div class="tg-post" id="msg-80016">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4eea0f59.mp4?token=NgkeHUAW8OilXRM1vsUCZEcCsNtTTRJLXd2OC-wF6dP8mQdEC4Fo9YHz7NdAwIAk4Ph6u6Qa0el1PXWFItOGcsPOhhHUVlYn6bQlg_pkB8GgEEGDbrsYcnH5_WjoEJRt70yojQJaegUsKRR23OCKiMQTTIl-4KhfvaabEYjrvvDfbA_ARLmJb1aSooatE14t0_cBPrvToM7cIowlFntoBVbl7_eU9iqBnS73Ipswahbiy_NhQPfPNsD7M1py-SDKPNOsRi68N--3njytdjN1KCPahTyV6PHtkiBoxsg1Ld4EgOjHkrjagVItXtuBlnJga7LxhITkFPC-quJcI3wsww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4eea0f59.mp4?token=NgkeHUAW8OilXRM1vsUCZEcCsNtTTRJLXd2OC-wF6dP8mQdEC4Fo9YHz7NdAwIAk4Ph6u6Qa0el1PXWFItOGcsPOhhHUVlYn6bQlg_pkB8GgEEGDbrsYcnH5_WjoEJRt70yojQJaegUsKRR23OCKiMQTTIl-4KhfvaabEYjrvvDfbA_ARLmJb1aSooatE14t0_cBPrvToM7cIowlFntoBVbl7_eU9iqBnS73Ipswahbiy_NhQPfPNsD7M1py-SDKPNOsRi68N--3njytdjN1KCPahTyV6PHtkiBoxsg1Ld4EgOjHkrjagVItXtuBlnJga7LxhITkFPC-quJcI3wsww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
الغضب يعم لبنان بعد توقيع النظام اللبناني اتفاقية مع الكيان الصهيوني</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/naya_foriraq/80016" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80015">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
اعفاء مدير المخدرات في محافظة النجف من منصبه واعتقال عدد من الضباط والمنتسبين و ارسالهم لبغداد بعد عملية قبض كيدية بحق مواطن نجفي</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/naya_foriraq/80015" target="_blank">📅 00:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80014">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6017431c96.mp4?token=KA324WwRA5KtZKhn0nbAL8Cpb-UlNaK-DL4xj9iavlPRKF3K4rTGZ9fOYumo_qZzyuZlRvAyzRZVyVEVwBD5HH0xqCKEn_zB-AZOmwcXJaqdITQAv_DtXVl9My45bX6fYPyjKCS4OawA-f9Qwpy3zCUZ-f54tKdVpjGatKtJwwNJnx8MgInd5njDccfOkjYUhjWYHaU3MkrD7AuPQ2w4EH9E-pzPRuFUxH6dNxuakoXSHVbCdNyUbkU4LlevedZTRoY8ZJo6OahZ2OL_LmwuAAF4wtNYp8709hujY0CgTKVmUPtSACT8jnmeCgcVCwF2pV3cL0AyT7VPe4zI2g5STg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6017431c96.mp4?token=KA324WwRA5KtZKhn0nbAL8Cpb-UlNaK-DL4xj9iavlPRKF3K4rTGZ9fOYumo_qZzyuZlRvAyzRZVyVEVwBD5HH0xqCKEn_zB-AZOmwcXJaqdITQAv_DtXVl9My45bX6fYPyjKCS4OawA-f9Qwpy3zCUZ-f54tKdVpjGatKtJwwNJnx8MgInd5njDccfOkjYUhjWYHaU3MkrD7AuPQ2w4EH9E-pzPRuFUxH6dNxuakoXSHVbCdNyUbkU4LlevedZTRoY8ZJo6OahZ2OL_LmwuAAF4wtNYp8709hujY0CgTKVmUPtSACT8jnmeCgcVCwF2pV3cL0AyT7VPe4zI2g5STg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مشاهد للغضب الشعبي اللبناني في محيط السراي الحكومي في بيروت بعد الاتفاقية مع الكيان</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/naya_foriraq/80014" target="_blank">📅 00:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80013">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e30e9777d.mp4?token=uTKVSOTtCVL5-q0mI-vJTdcSnVCMK0bzWgXt3Ixip0kBl63Ry4Q40_42K0TNmhiVyCETYA8Wkfp94d6MWY889FeUQYAK4YjNxryp6T4Sz6HsmSB6ugr8G05GzEQhkWE5UxGAT2j9Frhn3Sic6IWPAwJhh6cYXNm1ZuP5-0QVTMqSzuYvooGo911MaAlnsin2swEdurt1Q5Yq8kPJyo-Lejr7SSYCgLZXweG8rqftWyzWntEAOD8aQT9Be0b1IfdlEmJ8vyu0IrBW4Lwiv2ceh9HxUHWFcI1Qfx-N9ieAZRqauzSbdrmZ28kDDjUccsluWPck_TY7vMIXHCNDeyImNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e30e9777d.mp4?token=uTKVSOTtCVL5-q0mI-vJTdcSnVCMK0bzWgXt3Ixip0kBl63Ry4Q40_42K0TNmhiVyCETYA8Wkfp94d6MWY889FeUQYAK4YjNxryp6T4Sz6HsmSB6ugr8G05GzEQhkWE5UxGAT2j9Frhn3Sic6IWPAwJhh6cYXNm1ZuP5-0QVTMqSzuYvooGo911MaAlnsin2swEdurt1Q5Yq8kPJyo-Lejr7SSYCgLZXweG8rqftWyzWntEAOD8aQT9Be0b1IfdlEmJ8vyu0IrBW4Lwiv2ceh9HxUHWFcI1Qfx-N9ieAZRqauzSbdrmZ28kDDjUccsluWPck_TY7vMIXHCNDeyImNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاصرة السراي الحكومي في بيروت بعد الاتفاقية بين النظام اللبناني والكيان الصهيوني</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/naya_foriraq/80013" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80012">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
امريكا تشن غارات على ايران.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/naya_foriraq/80012" target="_blank">📅 00:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80011">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">السنغال تسجل الهدف الرابع في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/naya_foriraq/80011" target="_blank">📅 00:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P11gr6GBpl_g1YmRKvVUSPu-AzSAeUfZKcQmEL-OJKU30KTYVnKfPDA1qvGdDNxQSNtk7YxLWmhbdBVB1Dg-fwzF6gYVFYqhp7k3ZXA_3ilk0hJVWZWjHuuvR_qfss4V6B6pfeBx4YQKMO16jAUs0m_fL2Fwaju63yc1aocWmpfPN-883ZnDmjFsrlQMe3xIsDMPRDXIx7jfnR0Gcwx-09_MQk4pm7MhvR6_Yl2UGzHLLdZAdOmUwn1UuGpVPeNK4k5CP5QwIhzmVH09d0Chss97jWi0iFe2og2RgSF-rctkgqBd3_8yIUKB8FhALC7jfwFXqzeef-8vXhTY5gnzPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzuSqSXIbLxDdKp-xW4hPFW9LElqhpQTHtYv9ARy7qVgnis93y6d-C8W0LKiTihkQxUyOcZm9eR4gkRKhS26UPLHwn_IUhhyhm3VXWWwuVykiaT9AqRbhhxsyULg2YDkeZsocHTAmcYndmPS03SFrg2JYhDMEJ8FYa1CWPrN9d--Sc1pW1VJhxE-OpjrTNhc_WXr1Kp677beHC1O7oCLAZsxqz_lopDuUHAStaluYY8Me4EKxd89KWFWqqmXU7S_64diEdkJmzdToh6Uc4FTzca_gL152c5suAeCc90subrv3MVIZQv2EMBDeN7mNFaMLF_UX8gfQ2qnrYQZApEXDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">النص المبدئي للإتفاق بين لبنان والكيان:  ‎ تؤكد إسرائيل ولبنان حق كل دولة في الوجود بسلام، ورغبتهما المتبادلة في العيش بأمن كدولتين ذاتي سيادة ومتجاورتين. وتعلن إسرائيل ولبنان بموجب هذا الإطار نيتهما إنهاء النزاع بينهما بشكل نهائي، ومعالجة أسبابه الجذرية،…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/naya_foriraq/80009" target="_blank">📅 00:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">السنغال تسجل الهدف الرابع في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/naya_foriraq/80008" target="_blank">📅 00:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">السنغال تسجل الهدف الثالث في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/80007" target="_blank">📅 00:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80006">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">القيادة المركزية الامريكية: قمنا بشن ضربات ضد إيران في 26 يونيو كرد فعل قوي على هجوم الأمس على سفينة تجارية كانت تمر عبر مضيق هرمز. أصابت الطائرات الأمريكية مواقع تخزين الصواريخ والطائرات بدون طيار الإيرانية ومواقع الرادار الساحلية.</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/naya_foriraq/80006" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80005">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
امريكا تشن غارات على ايران.</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/80005" target="_blank">📅 00:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80004">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو يعلن عن توصل لبنان وإسرائيل إلى اتفاقية إطارية</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/naya_foriraq/80004" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80003">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو يعلن عن توصل لبنان وإسرائيل إلى اتفاقية إطارية</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/naya_foriraq/80003" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80002">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
امريكا تشن غارات على ايران.</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/naya_foriraq/80002" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80001">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تصاعد اعمدة الدخان من سيريك بعد انفجارات مجهولة.</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/naya_foriraq/80001" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80000">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">السنغال تسجل الهدف الثاني في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/naya_foriraq/80000" target="_blank">📅 23:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79999">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">السنغال تسجل الهدف الاول في مرمى منتخبنا الوطني</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/naya_foriraq/79999" target="_blank">📅 23:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79998">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RptwyaIdaBk0c2HloTd9_Ejm_wCZfRbyrXGfgwN21AcNud8qrCaeDLBiL3I507O5w8y2v0sasyl4gnKSW7-NF1cU7R1638j9oUxkcpirGD_RqPg835MkeS4z4PoShAig46uRVAL-wvftWK5n3MX5yKMPHRNz9CLGXBOxU0oi8EalXShvB189xS65r2L7WWWDo0LZVKSwu3PIMwXWOOK2xKouRNvqvyUoHCqqKw77dvJ4pKarNN6a64w71htdX_c-hN4js9B9VNCfMY0Is7fdNLYF-NHciS00VyOd_9o3ZhIVSSYTWcGJX05gYinTd8MVRFZUQKypAeCTaIt9v5lqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماع دوي 3 انفجارات في جزيرة سيريك، مقاطعة هرمزغان في إيران</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79998" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79997">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامب: انتهاك ايران لوقف اطلاق النار لم يعجبني</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79997" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79996">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سماع دوي 3 انفجارات في جزيرة سيريك، مقاطعة هرمزغان في إيران</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79996" target="_blank">📅 23:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79995">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
ترامب يغط في النوم خلال كلمة لنائب حاكم ولاية تكساس.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79995" target="_blank">📅 23:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79994">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1696a6fb43.mp4?token=U5gDFyw8flCiNuKn94JH7nEIYPdDoyTbqiIgVdplR7FwPZPUdl8IGVTYBEtDQTrkBG5x7pGcqMwaAerkyBL8mjN-dkRrAxs70_NHvUJkz94KmjlmivksxdszwJiKj7FVHoPUuqTNOz32pfLKyG3JsPVnR4DzIc7oBT8t-ZgYaLnRxAmZfvRXwDnihTqaJtNxTeFE7dnxMBINlss7Hkc0PDGa4a8Nxapr9oV02ULVfeiFw4oQibsLnnd3HwG89QV23lTZRjhKh7CqDObJ1IcwVggLHYx_o72WqtthTp3s70sGfu_-5CfusPxLQcKvtmhYhDnQ6iCaoWXYYOrdy2g3Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1696a6fb43.mp4?token=U5gDFyw8flCiNuKn94JH7nEIYPdDoyTbqiIgVdplR7FwPZPUdl8IGVTYBEtDQTrkBG5x7pGcqMwaAerkyBL8mjN-dkRrAxs70_NHvUJkz94KmjlmivksxdszwJiKj7FVHoPUuqTNOz32pfLKyG3JsPVnR4DzIc7oBT8t-ZgYaLnRxAmZfvRXwDnihTqaJtNxTeFE7dnxMBINlss7Hkc0PDGa4a8Nxapr9oV02ULVfeiFw4oQibsLnnd3HwG89QV23lTZRjhKh7CqDObJ1IcwVggLHYx_o72WqtthTp3s70sGfu_-5CfusPxLQcKvtmhYhDnQ6iCaoWXYYOrdy2g3Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب يغط في النوم خلال كلمة لنائب حاكم ولاية تكساس.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79994" target="_blank">📅 23:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79993">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">السنغال تسجل الهدف الاول في مرمى منتخبنا الوطني</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79993" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79991">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">السنغال تسجل الهدف الاول في مرمى منتخبنا الوطني</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79991" target="_blank">📅 22:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79990">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2d55dce0.mp4?token=gsmH8uunb-lnIun2XhsdNqnBAtR8ftEN8E_ga5qPBruxs8l0wpf-gP_1UPa1BWhwoeHVblHLe1mlweQD4hbiviu_lMtBU0LxKEqgieWZU_NmZevcJx-dtWDMCnJfqh50VPh-M83xY1D3HA2NPUvs6my1sPXyd4mYAuSEpeom2yJebDqrWcGR4f5YAQLnUR5Uzez9_GBadC_WVZkLFppPoCBoN23L4c58HfD_uFdhAMEACCqcG9Mb74tHNO1CxphRz0dzMalEMasOq7WVAWNDr8PcDjrsCzehlFo8hpAXrpgLpYv4lWseP4akzNOErc2EAZ4k6rN7SP1kmoFtaC2cKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2d55dce0.mp4?token=gsmH8uunb-lnIun2XhsdNqnBAtR8ftEN8E_ga5qPBruxs8l0wpf-gP_1UPa1BWhwoeHVblHLe1mlweQD4hbiviu_lMtBU0LxKEqgieWZU_NmZevcJx-dtWDMCnJfqh50VPh-M83xY1D3HA2NPUvs6my1sPXyd4mYAuSEpeom2yJebDqrWcGR4f5YAQLnUR5Uzez9_GBadC_WVZkLFppPoCBoN23L4c58HfD_uFdhAMEACCqcG9Mb74tHNO1CxphRz0dzMalEMasOq7WVAWNDr8PcDjrsCzehlFo8hpAXrpgLpYv4lWseP4akzNOErc2EAZ4k6rN7SP1kmoFtaC2cKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في ليلة الوحشة.. انطلاق مسيرة الشموع في منطقة الكرادة الشرقية وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79990" target="_blank">📅 22:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX8R-o56-wBxnBWpcZz3GYvnJ9k4DCg0ZFtirw1R7rfEKvlWjCzHefmqXsl-i3n8PVmcaOicnbRY5X90nsgfZ5mGH2Yq8Nxqv1ezDis0xi1FKB4Vfz5Pl9rBt19autWHxbx2ztTllicZaFPmFjdkjOR_2PxHrXCceHS2p2--vrzhrOf-wAPsxn5ybxeEwTX695MQjpkrU7F7FthMlIH8oP35oL4D0XrxCDw6DiWkFevHij5_q-zGMWSUKpQXf4-9ipj972YnvgXiE6lguU7fRMMHJ3ZM8UAjh3yy2fikd6PxA2RF7J5_SZIJelvU8mOWBaNPKSzxbRg5wNEFZO9sxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🇮🇶
🇮🇷
النائب عن حركة حقوق حسين الدراجي :
اليوم ببركات الإمام الحسين "عليه السلام" تم ضخ الغاز من الجانب الإيراني بكمية 5 مليون متر مكعب باليوم علماً أن معدل إنتاج الكهرباء في البصرة تجاوز معدل الاستهلاك وإن التشغيل الحالي افضل بكثير من الشهر الماضي، وسنبقى نتابع الموقف كما وعدناكم أولاً بأول، ومن الله التوفيق.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79989" target="_blank">📅 22:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">استخبارات قيادة عمليات نينوى للحشد الشعبي تعتقل شبكة مكونة من ثلاثة متهمين (اثنين من الجنسية العراقية وآخر سوري الجنسية) ​ضبط بحوزتهم مادة (اوكسيد الزئبق) شديدة الخطورة والمحظورة دولياً</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/79988" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامب: لا تزال إيران تمتلك بعض القدرات، ولكن ليس الكثير.</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/naya_foriraq/79987" target="_blank">📅 22:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏ترامب يهاجم وسائل الاعلام الامريكية التي فضحت كذبه: ‏زعمت الأخبار الكاذبة أن إيران أقوى بكثير اليوم مما كانت عليه قبل أربعة أشهر. ‏إنهم يتوقون لإبرام صفقة.</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/79986" target="_blank">📅 22:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
🏴‍☠️
ترامب: ‏إسرائيل رفضت المشاركة في عملية اغتيال قاسم سليماني.</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/79985" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">#ترفيهي
🌟
‏ترامب: سأكون صريحاً -- أعتقد أنني سأكون أعظم شيوعي في التاريخ.</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/79984" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
التغطية الإعلامية ليوم عاشوراء
:
شهدت التغطية الاعلامية مشاركة واسعة، تمثلت بوجود (7) عجلات للبث المباشر، و(84) جهاز بث مباشر (LiveU)، و(676) كاميرا صحفية، فيما بلغ عدد الإعلاميين والصحفيين المشاركين (1011)، بينهم (102) إعلامي اجنبي
(12) إذاعات محلية و(82) قناة تلفزيونية شاركت في تغطية مراسم الزيارة، إلى جانب (26) وكالة أنباء عربية وأجنبية، فيما بلغ مجموع ساعات البث المباشر (1006) ساعات خلال عشرة أيام، كما نقلت (87) قناة محلية وأجنبية البث المباشر عبر خدمة (Feed Clean).</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/79983" target="_blank">📅 21:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180ec771cc.mp4?token=SuMuZR9xa7ADmFeN9gyiRk-yLBqcdXxyxtFUqf0oJV-kHRtm8LHGQ5aRxOlcE6cREl4sGAwG6oQB8Thdj-VyTxT-L88m5bp0I6AWwtwMnpQG7MmenU7zMyrZE2R-VwN26YAQtghCuqLZAYjgVezK8aRfgsk-vW2PgeUHzRMXUiGtSP0XTRx_r_pYc7-oIWvnBh_veyiD-nc9r10TovMtZsMrdQOG-VBhQJ1QjHJEJ5vz9wVF9VYC4wMkQ_5SUV6Y2hkauieSvHCY_O-bSpSyIInJQVgo_8gz95ujbS01ipBwIzbWi-dZWlsVeYoJJxxqyCVf74-_k2YlghN13TF3WE33_Kd0TI-iFwrXdAcYHFH1Wqw_y1OlvxrsH65yfMeLnsykpwdsjhcs8ULcADKPzsEqAT8rW_2gUHDnekTKcrnoAHKlgvVQOi3I9I9uVKi02X0bR421ypY3XtLQJ5TK_APuxXk9e3RrUhG9LA5_xESwg03f59dTPm6KEX7ylkLDogBO_wRRDSKs_HNMA__94CMfC1o8cXaPH-7Y4jgmIlEmYM4OlwdKFiI5z_7lQbG8V4xlHDSUUuui_acXgh6O9gJ4H0F4X972uYUKbU5fz13QjLqnH21M_0L7_ja-hQOshOcMllp2w-HSxw1Qc4rjt1vMXSxAxnh6YIW--c54pSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180ec771cc.mp4?token=SuMuZR9xa7ADmFeN9gyiRk-yLBqcdXxyxtFUqf0oJV-kHRtm8LHGQ5aRxOlcE6cREl4sGAwG6oQB8Thdj-VyTxT-L88m5bp0I6AWwtwMnpQG7MmenU7zMyrZE2R-VwN26YAQtghCuqLZAYjgVezK8aRfgsk-vW2PgeUHzRMXUiGtSP0XTRx_r_pYc7-oIWvnBh_veyiD-nc9r10TovMtZsMrdQOG-VBhQJ1QjHJEJ5vz9wVF9VYC4wMkQ_5SUV6Y2hkauieSvHCY_O-bSpSyIInJQVgo_8gz95ujbS01ipBwIzbWi-dZWlsVeYoJJxxqyCVf74-_k2YlghN13TF3WE33_Kd0TI-iFwrXdAcYHFH1Wqw_y1OlvxrsH65yfMeLnsykpwdsjhcs8ULcADKPzsEqAT8rW_2gUHDnekTKcrnoAHKlgvVQOi3I9I9uVKi02X0bR421ypY3XtLQJ5TK_APuxXk9e3RrUhG9LA5_xESwg03f59dTPm6KEX7ylkLDogBO_wRRDSKs_HNMA__94CMfC1o8cXaPH-7Y4jgmIlEmYM4OlwdKFiI5z_7lQbG8V4xlHDSUUuui_acXgh6O9gJ4H0F4X972uYUKbU5fz13QjLqnH21M_0L7_ja-hQOshOcMllp2w-HSxw1Qc4rjt1vMXSxAxnh6YIW--c54pSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🌟
بالتزامن مع ترويجها لسردية فصل الدين عن الدولة في بلداننا.. رئيس الولايات المتحدة ترامب في خطاب ديني: ‏ لكي تكون أمة عظيمة، يجب أن يكون لديك دين وإله. ‏إذا لم يكن لديك ذلك، فلن ينجح الأمر، أليس كذلك؟ الدين عاد بقوة. الدين في ازدهار ملحوظ. لو كان سهماً،…</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/79982" target="_blank">📅 21:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
🌟
بالتزامن مع ترويجها لسردية فصل الدين عن الدولة في بلداننا.. رئيس الولايات المتحدة ترامب في خطاب ديني:
‏
لكي تكون أمة عظيمة، يجب أن يكون لديك دين وإله. ‏إذا لم يكن لديك ذلك، فلن ينجح الأمر، أليس كذلك؟ الدين عاد بقوة. الدين في ازدهار ملحوظ. لو كان سهماً، لكنا أثرياء جداً. عندما بدأتُ العمل في عام ٢٠١٦، كانوا يريدون تجريد عيد الميلاد من روحه. لقد استشهد مؤسسو بلادنا بالخالق أربع مرات في إعلان الاستقلال. أربع مرات. ولم يُذكر اسمي ولو لمرة واحدة. أنا مستاء للغاية. ولا مرة واحدة، ‏في ظل حكم الديمقراطيين، استُهدف الكاثوليك من قبل مكتب التحقيقات الفيدرالي. ‏سُجنت الجدات المؤيدات للحياة بسبب الصلاة. ‏تم طرد أفراد من جيشنا من القوات المسلحة بسبب معتقداتهم الدينية. منذ فجر تأسيس بلادنا، بُنيت عظمة أمريكا على أيدي المؤمنين. أول المستوطنين الذين وطأت أقدامهم أرض هذا العالم الجديد في جيمستاون، نزلوا من سفينتهم، ورفعوا صليبًا، وسجدوا للرب في الصلاة. كان الإيمان هو الذي قوّى رجال الميليشيا الذين صمدوا في ليكسينغتون غرين وجسر كونكورد. ‏في فيلادلفيا، قبل 250 عامًا الأسبوع المقبل، استحضر مؤسسونا الخالق أربع مرات في إعلان الاستقلال... الإيمان دفع الرواد إلى السفر غربًا، والإيمان قاد الأمريكيين إلى إلغاء العبودية، والإيمان بنى هذا البلد ليصبح أكثر الدول تميزًا في تاريخ العالم.</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/79981" target="_blank">📅 21:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1cc7c8a5.mp4?token=kpD5XQbnhaCXkyQ4dGlM_mwHFi-hv_HzF542HdOM0_KKWOcLNpA9bbuXmNTmPdRgGwyf7_OafQ40Edk-NyqMp_8oPHTzM93Dot0F9rEU62FNai_DWGFKeFpxNKPn_4MXpIeyDPHdlHo1sGCK9a7HC191p9fThB8tIypOztGaBLMUFvw9x80w5BfxjegAUW17GWvcz7CTuTzwGnO2HHAT1PleXhP_lhnAXyxu3HZU3QKV_6Y6awwiRgp325iaGkHa3q_iC78QrBsOYvu75HiMtfevYcbuEQDmj3wUUBuXlNeuMe6H_V7eidLiuoy_OXfanncQamg8_4WkPpY0CEsgoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1cc7c8a5.mp4?token=kpD5XQbnhaCXkyQ4dGlM_mwHFi-hv_HzF542HdOM0_KKWOcLNpA9bbuXmNTmPdRgGwyf7_OafQ40Edk-NyqMp_8oPHTzM93Dot0F9rEU62FNai_DWGFKeFpxNKPn_4MXpIeyDPHdlHo1sGCK9a7HC191p9fThB8tIypOztGaBLMUFvw9x80w5BfxjegAUW17GWvcz7CTuTzwGnO2HHAT1PleXhP_lhnAXyxu3HZU3QKV_6Y6awwiRgp325iaGkHa3q_iC78QrBsOYvu75HiMtfevYcbuEQDmj3wUUBuXlNeuMe6H_V7eidLiuoy_OXfanncQamg8_4WkPpY0CEsgoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في ليلة الوحشة..
انطلاق مسيرة الشموع في منطقة الكرادة الشرقية وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/79980" target="_blank">📅 21:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏مسؤول إسرائيلي: سنحافظ على الشريط الأمني على طول الحدود داخل الخط الأصفر بلبنان.</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/naya_foriraq/79979" target="_blank">📅 21:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWpeii3eRLidLZbbZLxEgJ5__AGtA0kDZDtqhSFOa6Igu9S5k6q4nFpWawnrQJ_m5iBdS01vTRvTE_4jWhSzHh8Smhdox6Mo8ELhxjo0NUlW-cKNRLLmP_tGBg7g6H5LJnhEhKwcm_gCTnCaJecNi8THodjJli-zmU-k1KrN2qyomkTeBBY0zWWwf2Ebk6YCJmDAg75IFAKDg9OfBxjIFAwnwT2yT2eC0rXfC20FD5a3-CuCldkdj_5RGBU9cI1J_6Y0FGtKh4IklBDiTjw2y4F3RyzzX4NDZ9ioFRT2ZwKoFvV9z22Wj77U_drEeWNzepRIi4SgSpr_y_chWFdMzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
رئيس الوزراء الباكستاني:
مع اقتراب يوم عاشوراء من نهايته، نُعرب عن أعمق مشاعر الاحترام والتقدير للتضحية الخالدة للإمام الحسين (رضي الله عنه) وشهداء كربلاء. إن ثباتهم الراسخ في سبيل الحق والعدل والكرامة الإنسانية يبقى مصدر إلهام خالد. ‏الحمد لله! لقد أُحيي هذا اليوم المبارك في جميع أنحاء باكستان بتفانٍ وصبر ووئام. نسأل الله أن تبقى روح كربلاء نهتدي بها نحو الوحدة والرحمة والعدل. ‏نسأل الله العلي القدير أن يبارك باكستان والأمة الإسلامية بالسلام والرخاء الدائمين. ‏آمين.</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/naya_foriraq/79978" target="_blank">📅 21:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79977">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_-BHztCNi48_-IIc2J4Ut9L4rn4V7xB8lhVB8AnKYB469Gu-5Lj89UNPb1CMJkoOH6D0R3PCy8SxJ-yTcibk1qkN2pV848ss_Ar3ptpePtSbPEsmIzXMSf6GaZt640LyrE6nFMl_PqBqiKa9n5LvWv_Xny9DerfODHBfhyTuUzfDEXonevmmkmxijacrIkTGrZe3vUUijUOTumdZneK94nIFgZnImBat6KHfReHQCFdPUoslHQK0zNIjX9847W6GXMhpUBLgWuVYuiwPG27jRP54GZG201NnjL1CK5nip0y6W4xYFUrJviYoZrZIwmpgngOPC1y-dfWrhkAZ7yU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرطة محافظة كركوك شمالي العراق تغلق الشوارع في محيط جامع صالح بهاء الدين في الحي العسكري بعد انباء عن وجود سيارة مفخخة</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/naya_foriraq/79977" target="_blank">📅 21:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79976">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏴‍☠️
🌟
لبنان وإسرائيل يوقعان على ما يسمى بـ "الاتفاق إلاطاري" برعاية أمريكية.</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/naya_foriraq/79976" target="_blank">📅 21:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79975">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw9Qa1Vxo22JYiUsoW6GE6V5Omg941knvcKnPdCGxZI03Yn_Da94M7WDQhadcME8yotZUwDe4RAh-WD8FplsY4wQ6TQ-CCG0Xd2BpiTUmRmIig_1T-aP_9Am1gCPCURWWP0zUL0Umhso5LlwtajJkPv_SSt1kAYRCal-P14gF6f9azzHldYka1n4GEtTnFOFvcGHuVFTr-7OgHYA8XjJQzWxE5rrsn5UTiUV7C3YDfaQiPfByiJsyqxiLQ8b7g1guyfi5jGZmNicJrQ1ILrW1036Twgs31aAdpa6w0Ee238PpC4C7cEB0sE008ezXbtmLNgGvZIV947YE42ljp1yuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو يعلن عن توصل لبنان وإسرائيل إلى اتفاقية إطارية</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/79975" target="_blank">📅 21:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79974">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3m1jpZZfb2I8-N_DIFs-xzXFIfqE4eyei7ktqZ2qCkdyluyrBMKCbZgBvbShhCv_3_M2oo1YhRNFfF5Ra6kZI487Ia5q01tDhjSJMLMBkBYwwKp94HdHGf4ae9Xrp4Z-mwRsBzo1kQoxfbL5n5hFP8V3OWObHC4v2fELkofykpkHFrf-ZtdORZRYtJRg4Q4hyLm_-ekEiZGUEScwoPEPYVIoe1vbyGmv5nJjuw3JyizwUyybV0CEWj5ckPHQ4CyXN75oDzm5580WeCWYf0XoqlV5Ndbt9TktnTl_mCgXkUqp1NnQaE5Qfohdkjat0ws3le-Hmc1WOFlhIjBVu5RDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
سأتحدث في الساعة 1:30 مساء إلى تحالف الإيمان والحرية، وأحد البيانات التي سأدلي بها، ربما أهمها جميعا، يتعلق بالانتخابات الأخيرة للشيوعيين في بلدنا. من السهل جدا بيع الشيوعية. سأكون أعظم شيوعي في التاريخ. سأعطي إيجارا مجانيا، ومنازل مجانية، وطعاما مجانيا، كل شيء مجاني. لسوء الحظ، بعد عامين أو ثلاثة أعوام، سيفشل البلد الذي يحدث فيه ذلك. إنه يفعل ذلك دائما، ثم ستبدأ في العيش في البؤس. لن يكون هناك طعام، ولن يكون هناك سكن، ولن يكون هناك جيش، ولن يكون هناك شيء. ستكون العالم الثالث بكل الطرق، وسيعاني الجميع أو يموتون. يؤسفني أن أقول، لكن اغتيالات أولئك الذين يعارضونهم هي عنصر مهم جدا في أيديولوجيتهم.
إنهم حيوانات! في كثير من الحالات، ليسوا أذكياء، ولكن في بعض الحالات، هم كذلك. من السهل عليهم الحصول على متابعين لأنهم يقدمون وعودا يعرفون أنهم لا يستطيعون الوفاء بها، والدوموقراطيون لا يقاومون. من نواح كثيرة، يسمحون لهم بالسير في طريقهم الخاص. إنهم يخشون أن يخسروا انتخاباتهم، إنهم يخشون الصراع. إنهم ليسوا أذكياء بما فيه الكفاية أو أقوياء بما يكفي لمحاربة هذا الطاعون. إذا قاتلوهم بالطريقة التي يقاتلون بها الجمهوريين، أو أنا، فسيكونون منتصرين، ولكن ليس لديهم الشجاعة للقيام بذلك. هؤلاء ليسوا دوموقراطيين اجتماعيين، هؤلاء شيوعيون صلبون بلا إله. هذا هو أخطر تهديد لبلدنا منذ وجوده قبل 250 عاما. أليس من السخرية أننا نحتفل بعيد ميلاد مهم جدا، وبدلا من الحديث عن المسيح والحرية والانتصارات من جميع الأنواع المختلفة، نتحدث عن تهديد آخر لأسس أمريكا.
سيهاجم هؤلاء الشيوعيون الذين لا يرحمون جميع الأديان ولكن، على وجه الخصوص، المسيحية - يفعلون ذلك دائما. جميع الدول الشيوعية تهاجم الأديان بعنف. كما تعلمون، لقد ضربنا نيجيريا مؤخرا، وأنهينا إلى حد كبير ذبح سكانها المسيحيين العظماء. إنهم يعرفون أنه إذا ذهبوا إلى أبعد من ذلك، فسيكون الهجوم أكبر بكثير، وفي ذلك، لا يريدون التورط. أنا أنقذ المسيحيين في جميع أنحاء العالم، على الرغم من أننا لسنا في تلك البلدان المختلفة، من خلال ضرب هؤلاء الإرهابيين بعنف وقوة. سيغلقون كنائسك، وسيقتلون شعبك. هذا ما يدورون حوله. هذا هو أكبر تهديد لبلدنا منذ تأسيسه قبل 250 عاما!</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/naya_foriraq/79974" target="_blank">📅 21:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79973">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو يعلن عن توصل لبنان وإسرائيل إلى اتفاقية إطارية</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/naya_foriraq/79973" target="_blank">📅 21:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79972">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">في ميادين الجهاد وميادين الشعائر حاضرون
انهم رجال المهمات الخاصة
#كتائب_سيد_الشهداء
#لن_نساوم</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/naya_foriraq/79972" target="_blank">📅 21:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79971">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1sOUSXDHEhk8ghneA5zhbFyUwwF4WvP6L4_kEV43U2UrNbFHHnaIKGUTcX7LpJTZGw6L5wqHobEoG3qAQckdYJDrKH-jBkot8RrWaVHjR1yybKj4YTTGsGkMuu4W0d9-t-vKWQ_pfIDERhsUzPElyms9b6bf9IozapnowFC583FNGmQWI2upP-d9ciOEt3L_lC2Qc319fu2g_UepRrXXnrNBPtEAnmAzKjGbFey14pYVU2A_3POCOjvlbU7nn484N33kAZAQ_ztfUOlD85DLP3ynmb0vmETgRae3GPI-8DCFnCIs_Izq1MCAyYn52kPIS8X0ZhcLdN8cfNg4TSLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
تشكيلة المنتخب العراقي في مواجهة السنغال ضمن الجولة الأخيرة لدور المجموعات في كأس العالم 2026</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/naya_foriraq/79971" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPOJDnFidkQ2_0XNNiqDofGpFiJdHWLPHLFmTyNm3JhvgRguci659ASbmMY1MaQ2_q_cLJhpYqXz-8ICDQzby32aZ2N3shUG_P87YsyfT8XHwWX9HhLuosVNCNd-PArc3bXC8gJe5eccdy_lghGXvIFzO-hRuaiUG9I0UNrGnHiNIxRgMwEmdfrxp03K4RpymwUF7nlcMosNlQTagvVE4K9PJ-fHntw5AaW9jckIcMUTs74kXIlYLNND9yBedByw5_2EwqIOHkNIvtK_3jMS9bfEqUuaN6waYdtLnDJ3CCooaT7Qg9MYZp2xH0mMaw806I94uYxkiTzUGcPuZVM3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي
:
-
في العاصمة بغداد نفذت مفارز الجهاز عمليتين منفصلتين حيث تمكنت في الأولى من تحديد هوية أحد الأشخاص في قضاء أبي غريب بعد رصده ينشر محتوى عبر منصة "تيك توك" يتضمن الترويج للفكر الداعشي المتطرف، وإثارة النعرات الطائفية، والإساءة إلى الرموز الدينية، فضلاً عن تمجيد الجرائم الإرهابية، وقد ضُبطت بحوزته ثلاثة هواتف نقالة وعدد من الكتب التي تدعو إلى الخطاب المتطرف.
- العملية الثانية، أسفرت عن إلقاء القبض على متهم أقدم على تمزيق راية خاصة بالشعائر الحسينية في منطقة حي الجهاد، في محاولة تهدف إلى الإخلال بالسلم المجتمعي.
- في محافظة كربلاء المقدسة، وبالتنسيق مع العتبة الحسينية المقدسة، تمكنت مفارز الجهاز من معالجة حادثة تجاوز وقعت بالقرب من مرقد الإمام الحسين (عليه السلام)، بعدما أقدمت مجموعة مكونة من (١٤) شخصاً من حملة الجنسية الأجنبية على الاعتداء على زائرين آخرين، في حادثة كادت أن تتسبب بإثارة فتنة بين الحشود الكبيرة في منطقة بين الحرمين.</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/79970" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79969">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
حزب الله:
تنفي المقاومة الإسلاميّة نفيًا قاطعًا ما نشرته جهات رسميّة تتبع لجيش العدو الإسرائيلي حول سيطرته على تلّة علي الطاهر عند الأطراف الشرقيّة لمدينة النبطية.</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/79969" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79968">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
‏الإعلام السعودي: إعلان عن اتفاقٍ إطاري بين لبنان والكيان الصهيوني بعد قليل.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79968" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79967">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qvelegl8DLp-9z0ECZ_njRY5sIpgCyxpjpemfnzEWRJ0QwgCWsgUqgCr28buz65BEEaCt5aTVUX0HulnsbpFTswmbbCy6vhoenCJdhQEdHxvMZjvF2d_mLsG6ZQ9S9SliYaAb3rmpEJI_ODopKs1rVzTQ9n-3LXBNP-QWmFkGs23q5l_-hWeGFIH4UdA2EOoNT-zKV_-hRMnh7C6uJ6CD56di3Dj6a2HbpyzddFgrIbK_023r8zgh81IRlR9StjsDR8Pm0MmGPenKmY0aychHAtLuHxPdVGE2BsptYAlweblj16lsyDjWPP7t8_rHS7U1Yirsdyk-Y2hiVjuzc9Cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب:  أطلقت إيران أربع طائرات بدون طيار من نوع One Way Attack على سفن في مضيق هرمز.   ضربت إحداها بقوة السطح العلوي لسفينة شحن كبيرة ومكلفة. لحقت أضرار، لكن السفينة استمرت في طريقها.   وقد أسقطنا الثلاثة الأخرى.   من الواضح أن هذا انتهاك غبيًا لاتفاق وقف…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79967" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79966">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvBp5kdY1-Yn0aVph24_1UjkZyGvbHXJ-469oLiZrJKtVLnh2eSvYSD4B66bbwM8631vvQ3jL-TijNhEtcSa7ixcP363QnGpvDZSr81NxmAHUcsylmodgOW47RTrhazOhGCSls0R3AyzgvHCEMAIHGR5cSjdAK9H_glzJA3GsDiTzDQ0zFIsQ9EiMv6t19xWJ0ouVhPcqCZljaj9vLejce7Buc8aRrEie_2xP16q7PjKkhyFjdaI49_ypr-o27HDRl0c7SIMXeBuPE8zQzNV3yqFEBlW-pQFpNRaRbhwLSnt8WfVF2vTyd-ZIgQgaDoKBozUKs2dJlMuQU9G2J537g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
أطلقت إيران أربع طائرات بدون طيار من نوع One Way Attack على سفن في مضيق هرمز.
ضربت إحداها بقوة السطح العلوي لسفينة شحن كبيرة ومكلفة. لحقت أضرار، لكن السفينة استمرت في طريقها.
وقد أسقطنا الثلاثة الأخرى.
من الواضح أن هذا انتهاك غبيًا لاتفاق وقف إطلاق النار بيننا.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79966" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79965">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نايا - NAYA
pinned «
🇮🇶
🔻
Dear brothers and sisters, in light of the reports regarding the presence of the martyred leader Immam Sayyid Khamenei in Iraq during the funeral procession, Naya Channel has launched a dedicated channel for designs related to this occasion. Please join…
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79965" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79964">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
🔻
Dear brothers and sisters,
in light of the reports regarding the presence of the martyred leader Immam Sayyid Khamenei in Iraq during the funeral procession, Naya Channel has launched a dedicated channel for designs related to this occasion. Please join via the link below.
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/79964" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79963">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭐️
مدير عام الوكالة الدولية للطاقة الذرية، حول ما إذا سيُسمح للمفتشين بدخول إيران:
من أجل الإشراف، نحن بحاجة إلى التفتيش. لا توجد طريقة أخرى.
هناك اتفاق، وللامتثال لهذا الاتفاق، سيتعين على الوكالة الدولية للطاقة الذرية أن تتمكن من الوصول والتفتيش.
أنا مستعد لمواصلة العمل الفني وأن أكون هناك في أقرب وقت ممكن.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79963" target="_blank">📅 19:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79962">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-4-JJnSGNh8Tur3cRz0Qt5ylxjksqfoyrROSMMfUeoRV-LkgXM4h7XnVjVXERBtsqGFFBJgefNkyqWQpNHUucufYl5agHVlJQzSVy2HFhn5FlZDOtw_pTDoCXzU6bDshojm5sG_OzIG7-0Pu7MQfLxLzzi3pjpyitgkQhUblCXNr_NG6l_oDapWfGIOCnPbbkgCRlYEhFovdvXZLfLILgVTL6t_9vvhxqmONfY9UuTjQpEo79xZf6cttqv2I1N9Fyo1_xzmHNsHuCchtC69BZzB6kggPYbOy1E0gUXnfGxofdH9ufFcU7JMX2GWYz4bDluRw6EoUCCafrpuKqVe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هناك شخصيات لا تختصرها الكلمات، ولا تكفي السطور لوصف أثرها. ومع اقتراب يوم التشييع، يستعيد الجميع ما تركته من حضور في وجدان الأمة..
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79962" target="_blank">📅 19:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79961">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭐️
مصدر لنايا:
توجيه بخفض إنتاج حقل الرميلة في محافظة البصرة جنوبي العراق، بسبب استمرار الظروف القاهرة وتذبذب وصول الناقلات.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79961" target="_blank">📅 18:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79960">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7f73f33d.mp4?token=nJYOXcXn3CeMlyKHRxp6H4pcX1XPwjempwki40n9AoBCYdnEjuo0mdr4KK0JjJrixCpmqbZjJgEWYaJLPFet79oAZpvi1YUY0uZaFsOuI6C_Pzr5IaBNKpXbApbxD4-3bnW4v0IGcFz8nhyJDMUbyxe4e1Uxb7kVaFZv4BE30y7eIdpSf2EK5-O9p_ayM6dGOvCXJsHmPRWjUpZeNqSyno1Q9_FyY5wEM6IH6gQiv3apKg07QBbcfGckcTwlHY5_xI-W58cvCkn3zvGtxbhLfTe8ZYsnyCRVYE1ll_Y6b1AQuh6w4rHJyPSOmQqn43Nf3nDuJCDI5a31dM74tfi5DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7f73f33d.mp4?token=nJYOXcXn3CeMlyKHRxp6H4pcX1XPwjempwki40n9AoBCYdnEjuo0mdr4KK0JjJrixCpmqbZjJgEWYaJLPFet79oAZpvi1YUY0uZaFsOuI6C_Pzr5IaBNKpXbApbxD4-3bnW4v0IGcFz8nhyJDMUbyxe4e1Uxb7kVaFZv4BE30y7eIdpSf2EK5-O9p_ayM6dGOvCXJsHmPRWjUpZeNqSyno1Q9_FyY5wEM6IH6gQiv3apKg07QBbcfGckcTwlHY5_xI-W58cvCkn3zvGtxbhLfTe8ZYsnyCRVYE1ll_Y6b1AQuh6w4rHJyPSOmQqn43Nf3nDuJCDI5a31dM74tfi5DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
وزارة الدفاع الروسية تنشر مشاهد لإستهداف محطة توليد الطاقة الحرارية في سلافيانسك الأوكرانية.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79960" target="_blank">📅 18:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79959">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
بلومبرج:
أخبرت عُمان حلفاءها الأوروبيين أن السفن التي تعبر مضيق هرمز قد تضطر إلى دفع رسوم مقابل خدمات مثل المساعدة في الملاحة ومكافحة التلوث.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79959" target="_blank">📅 18:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⭐️
المنظمة البحرية الدولية:
14 بحارا قتلوا منذ بداية الأزمة الحالية في مضيق هرمز.
نحقق في استهداف سفينة أمس بعد عبورها مضيق هرمز من المسار الجنوبي.
أغلب السفن تستخدم المسار الشمالي الذي تسيطر عليه إيران بمضيق هرمز.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79958" target="_blank">📅 18:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79957">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">إعلام اماراتي : انتهاء حالة الخطر !</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79957" target="_blank">📅 17:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79956">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭐️
استمرار الزلازل القوية في الكرة الأرضية.. هزة أرضية بقوة 6.5 ريختر تضرب الفلبين وأخرى بقوة 5.2 تهز باكستان و ثالثة بقوة 5.5 ريختر تضرب جمهورية نيكاراغوا، خلال أقل من ساعة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79956" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79955">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79955" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79954">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79954" target="_blank">📅 16:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79953">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVuZkTOOyOq_qe2gfubXohjlVGhQzC4ZSvk260D11NEWIf_VKlXtJr91QVZlBwn234x64kGXwLMNaxBFfppmR7giRZeJ3Wtx6T605tbbm8bRvo53JMk1rUr63qvzwTBqJb-7TgHDiP2lvPV1gfdesrXt_1EhFZMBjQvX3OYBm483Tc49UP5v5Ac9_Z3ZJBieVnQcO2CZbnVwORckNf-FJ0gG39USmxjhp6Bi1Nanudm8ympihYbKNbNY_5wRMafEiNPmLVl8SQLL2bfq9ff6tlXjTVXuxLpo2PUJburAZFSqZtpi9T9LaqPmZRylktudmiYE34YO5h3Z00jRJH62GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79953" target="_blank">📅 16:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79952">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79952" target="_blank">📅 16:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79951">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79951" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79950">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇷🇺
🇮🇷
‏
رئيس شركة روساتوم الروسية:
روساتوم ستعيد موظفيها إلى محطة بوشهر النووية الإيرانية في الأسابيع المقبلة إذا بقي الوضع مستقراً.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79950" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79949">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56c90f612f.mp4?token=D9Qc4_Lyg44waNShA-8yLov_ShZ2TOO6B1J3XJX2M3e2ldtQWPHjgWsjdyt7mdgcAMxZHFCvKrID7Laxk4x62vBYAnUtsfbU2Sc4q-Mid_jTZb3lzsmAvfgAzkc--qhSkVgwHw6VTRjpUiqtoedQ5SiLuqmd5XoLkrsJwoZ_dXVcbV7p29faUTw6xOHKB8HoBQR1x-86lURiiFLjzF07r1OZpE2cInUnJfUb5VpqfO7LTe1jgqvbJLTtwDfPVaJAuvGy0Z2xWodlsJFN-0Cy0zVBpWff3SopZdLVtRCzjxvMcckFfwegbVIwZ5Kwtjt-6ymOtR2FKG46J1DtrmmwtEXEDEUQdq4CjwDwlX3mdq3xdtw2bxdWUWQB8AFAOw8kMTGO_7tEdL_x_Z3c3_i4TEVBi_Tz_UVo0weeFdjFvwmZ-yFa_TWi-O2QlwOh4O0SAw7BHgiy2bsfoVPvtyK4K5QU_JiVSyG7XwOdOt_vmc42tms-DL8_kvGu5ksCiSbiPVdWOP8fF_vtuHoBR52OFm-ZEFez9JgBjB0rZ31PJ6Dc6HFEpja1ehj_7Nihwq6U4COrqB1krZ4l7GyWVGwmdSAI849ksr7cTY4deRPi8eptTrsqU4C0-qwgo_xgUeDsQOrSQGv2NjHFtlfdfa4r4-XAhqw3bkOWqRg2Vv9DmvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56c90f612f.mp4?token=D9Qc4_Lyg44waNShA-8yLov_ShZ2TOO6B1J3XJX2M3e2ldtQWPHjgWsjdyt7mdgcAMxZHFCvKrID7Laxk4x62vBYAnUtsfbU2Sc4q-Mid_jTZb3lzsmAvfgAzkc--qhSkVgwHw6VTRjpUiqtoedQ5SiLuqmd5XoLkrsJwoZ_dXVcbV7p29faUTw6xOHKB8HoBQR1x-86lURiiFLjzF07r1OZpE2cInUnJfUb5VpqfO7LTe1jgqvbJLTtwDfPVaJAuvGy0Z2xWodlsJFN-0Cy0zVBpWff3SopZdLVtRCzjxvMcckFfwegbVIwZ5Kwtjt-6ymOtR2FKG46J1DtrmmwtEXEDEUQdq4CjwDwlX3mdq3xdtw2bxdWUWQB8AFAOw8kMTGO_7tEdL_x_Z3c3_i4TEVBi_Tz_UVo0weeFdjFvwmZ-yFa_TWi-O2QlwOh4O0SAw7BHgiy2bsfoVPvtyK4K5QU_JiVSyG7XwOdOt_vmc42tms-DL8_kvGu5ksCiSbiPVdWOP8fF_vtuHoBR52OFm-ZEFez9JgBjB0rZ31PJ6Dc6HFEpja1ehj_7Nihwq6U4COrqB1krZ4l7GyWVGwmdSAI849ksr7cTY4deRPi8eptTrsqU4C0-qwgo_xgUeDsQOrSQGv2NjHFtlfdfa4r4-XAhqw3bkOWqRg2Vv9DmvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الصهيوني ينشر مشاهد يزعم أنها لغارة إستهدفت النبطية الفوقا بجنوب لبنان صباح اليوم.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79949" target="_blank">📅 16:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79948">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني:
قائد قوة القدس الإيرانية قاآني يكثر مؤخرًا من إرسال التهديدات تجاه إسرائيل.
إذا هاجمت إيران إسرائيل فستكون هذه أكبر خطأ ارتكبته حتى الآن.
هنا لن تساعدها أي هرمز أو إطلاق نار على السكان. لا شيء سيوقفنا.
قواتنا مستعدة لإكمال المهمة.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79948" target="_blank">📅 16:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79947">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
🇮🇷
وسائل إعلام خليجية:
أميركا تسلّم باكستان 22 إيرانياً من طاقم ناقلة نفط احتجزتها خلال عملية قرصنة في وقت سابق.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79947" target="_blank">📅 15:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79946">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKZUABDCXiTGkxJoNkmdiMR-XBwqw9Yy6sch9RGofw5sfq9m9L0x1evs2c-czo0N89ej3mKa3n_fEsYRQnw7-8SIvoweTzjkZ-OLUpN2Kewk18L8lgVVNYSbz_DYVaXbd6a7tMiesUAq4QfgdXboNznEXKofx9p7b6TIBj7pSeOwDHZuM14j_Gmakz187uPP2qp5WM32Es0xc_iwYbgE_eR2_H1VmwXFaxQENxOZpZ3ofsV_JkeAItKdCKpExtx9QdELkV6k_TM4Zw45z8ZcixePENnke_JVQoQwg5yijZEXPXo645LB0VTuTwcOeJcviNGtdOzJ0Tw4YIRPEz2VVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متحديا الموت مثل اصحاب الحسين   مشاركة الحاج الامين ابو الاء الولائي في مراسم ( ركضة طويريج ) على الرغم من الملاحقات الامريكية</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79946" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79945">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c558cbf6e9.mp4?token=ZkNRHSM2rr5PqhEzaotSOf6LCTFDpg_U_0gZVmSPkuCL-PRYmAv94hFyfub0J8a94CdhmNyLyOQCpqo-ZvBjENLCM0B5zb0J757KnE2iRoNjRfTdpxhspZ_i8GM_cybAKcqQm8ZDJLtoQfSd_bxQ5chaodE8QuN7YNn3RsPPiaX030BAYDZQ31Y8HIWV1DcIwQeZh1MaZTQ6VSChLoGI2WPOVUWE8jJW4mfLWEPiHMrZkdyf7IJcntHjyKt7lCeMihY29Wv2B8zUB_fczpCNHFCzTu2jA5YWtqM5cig33AKugjHZbdcDYaMLx3t31zair7mIxNQ1hewQ__uKztf7aopUrNiwuj5lEHLVaciyKRIRZ8jFLvUtXaUHm97nZFquYfgyXDAYt1qW1qKFdnt1yqEbm0ykSxiyzw8D27ZAMxWNe0txq9js5yDV_KaLuhyevSjXRxx5xSPQ5twqVJGW54pgfLrH8JGFUIo9eFmRovrQrpUDhbT3VifqXADe0exKHDxIB2fqceT8WPSTJr5oI-wrxCBvlQuJ-fjx72_W0lvhYDy-uVqfn8ILluZWpaGas5gjqfqxAplYCdv67sxXgh7BvsFW_bKUAUiSx_rj6D3_iXMfvgKLXaLcAZftFnecGsL6An0c6aOsKcTRZkQlnLndPNuAO2LO_59IGR2WFjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c558cbf6e9.mp4?token=ZkNRHSM2rr5PqhEzaotSOf6LCTFDpg_U_0gZVmSPkuCL-PRYmAv94hFyfub0J8a94CdhmNyLyOQCpqo-ZvBjENLCM0B5zb0J757KnE2iRoNjRfTdpxhspZ_i8GM_cybAKcqQm8ZDJLtoQfSd_bxQ5chaodE8QuN7YNn3RsPPiaX030BAYDZQ31Y8HIWV1DcIwQeZh1MaZTQ6VSChLoGI2WPOVUWE8jJW4mfLWEPiHMrZkdyf7IJcntHjyKt7lCeMihY29Wv2B8zUB_fczpCNHFCzTu2jA5YWtqM5cig33AKugjHZbdcDYaMLx3t31zair7mIxNQ1hewQ__uKztf7aopUrNiwuj5lEHLVaciyKRIRZ8jFLvUtXaUHm97nZFquYfgyXDAYt1qW1qKFdnt1yqEbm0ykSxiyzw8D27ZAMxWNe0txq9js5yDV_KaLuhyevSjXRxx5xSPQ5twqVJGW54pgfLrH8JGFUIo9eFmRovrQrpUDhbT3VifqXADe0exKHDxIB2fqceT8WPSTJr5oI-wrxCBvlQuJ-fjx72_W0lvhYDy-uVqfn8ILluZWpaGas5gjqfqxAplYCdv67sxXgh7BvsFW_bKUAUiSx_rj6D3_iXMfvgKLXaLcAZftFnecGsL6An0c6aOsKcTRZkQlnLndPNuAO2LO_59IGR2WFjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متحديا الموت مثل اصحاب الحسين
مشاركة الحاج الامين ابو الاء الولائي في مراسم ( ركضة طويريج ) على الرغم من الملاحقات الامريكية</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79945" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79944">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭐️
استمرار الزلازل القوية في الكرة الأرضية..
هزة أرضية بقوة 6.5 ريختر تضرب الفلبين وأخرى بقوة 5.2 تهز باكستان و ثالثة بقوة 5.5 ريختر تضرب جمهورية نيكاراغوا، خلال أقل من ساعة.</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/79944" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79938">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_ixa7o7fo_OsDrwbXf3VP4P_8khOrKh2goxFef_mTh0EHbc9ZOLzeQ9MGLMRvFHoxE7xS__HWp6IjlHeXlm85fUOw9XnkognSGd0vbWzdAfY3GLNpPK4dRGGXCD4gfDBZ48oesyULPZgdG4Ehpv8wFt8xbZMGcpBX-QOrHt_4QdHvPbP4hBTbvx8uxVsQQbLVtbUim2x2DVG2dm7n4qCyTYY4_mBSsWDmjXkk4bnop7bnJjCIVefQLycwu1BaoB6bBtJpxcHskSi1JLKkdnC7De3Snid1lUu4mHkKNBnVIJLFptUZRoF5uzewtro7-nD2Y-G5YGET8olBguVCz6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4tqdv4v6kveyt6IPA3QRO9bWnEKW1wjSKspFmbfU5psyy15-Sw6vBrkOkWrZtE-H3oqbPqc7Yc7Cvgn4gkxEJ5FMmn6z0pXHB4qeKxnxKs0uquejnx5LNZK3Dq-VPHj9kTUny9V_EPNFgaBafFrF4-yTjHZJ-u5JeLeuwTEKdC_ygplUyYuRCLQzduh40h7xSgqca0aumEYomPI7QFZ0Buzl90QtAioUMLBuf5NoivvNS3UayykA8I8Xx0rgSGEiR0z0q5gKZA_Ldr69WlD7zspaqadGWM4FdO-YAFN9pGaryHt5_MgdYPYGP4nN_D1x4b6Lr2HxTVgnON_i419ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nnccruw24B75b-VZcaoetXqJrYHJl11z3ArhRqIA_8HQpFKGjRSHiNw7J01PLeqvf66S6RH0WrQRzjUZJxrecL7qBw7SKRNzHd5Zan7xb1wLfDpJMa7mztRinPVuT6YcCx6VruLS39m2NPYJZXAqVoKgPrpgEmriUCxHZPcu2sbwff9byO1zrOi9s0ShjrYzVNl4KbzV6iOcpigpoI1uJuxQ4qjWcz47maarvdAomZ_sd_apz01Zc4Suv0q0lC7J3IdMDa0L_p2JTpY97GB3nVBZxs3JRQ1yNe83rXMrlQviul1MSKXBvpU250dIKausNZp1NsCwjmHO4liGv9Z3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCCtSmdkpb_s7axGNv49wpZKNRmnyt5C3j4kvXcjFWmxu_qsi-cWlOAHBwalPusyI3pUFF6mH7WS63EQUTqbCfCrQQXlZjx804X_Qmcj3VATY56tmLR8Ap4BhwwQ-Sl1MgJZNGBNolaAC_ZlB78o9ZbF_wthjE1bE2k68iXN7c4S4ZBib4MGYBqntjTVtfMUB8NRb2q22GGDw770d8mURclwylSdnOdWSrvYYvH4hUClIkoRPQinoysHHWopxOndoYEHzJ9dhHdfMAtYseMQvhPh9ItFvzk3rVr1ws4i62616ot9sZLigbZatWYpBNHlnsxxIiF6GEDX6B0M8jRcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWFgqtudkJmhjH7Lotl0MiXrvQLUcUeKPXV4AfSKeL9PJadhYiDv_PbGcAVS9v5wpjlHSVriE4AoNf7F6QCaSgh1EHepOOaPSyDNKR9V2nyieuej-TUAVfyqGUX53WdPd1Hb5xvqv3FEd3MrI0VEJ2KSDZN-0zL2lhfAgriEowKE3XtENeLwQxyRc3gv8rJfXFbTya0SjJkFV_dJV3uPD3fOJ3PZ5hZ2dQmbam9asDVBEk5CR-WuvRH_TAySqv0DhRf8DCxYG9O-Goevt21-KgGunPq4lSQSH58WBLLg9YJhOQMVacwI2vptlszBuxyBWvC6XaMS8QikBDYFUsD4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxVdw5DBLaFQuAaB33LdB64UbvYO3cmPUDbsLGHU75I7YEem4MtwB2-lqjCG3oY7Enc4Eo-t1ia3Rdu3XOHWaHF9gF-3chcEE6YGZXyJ5lGh0N5vQyEVwiMI9lCIN29xLx27hpCUCjwkMS3J7lHg7dcBRhjehK9aED2E-MsKOl2f8iDqkbdsDGXh3JYa3fw7KcHCV_AU0D771b4sQNiSkSnnVQNSiPITM5HpIHJmmuB4FxE6li8V68Ylo9FZbSifXEMgnTCsSYjahJiH79QX7BmI7rICVFXfLB42xuf9WfeoMidvQmGwTD5j7O9A4j4vC1cTNHVXRHYtf1qw6LveeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴
تصاویر رهبر شهید امت در مراسم طویریج در بین الحرمین
#قوموا_لله</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79938" target="_blank">📅 15:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79937">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔻
أعداد هائلة من المعزين العراقيين في مدينة الناصرية يحيون يوم العاشر من محرم الحرام.</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/naya_foriraq/79937" target="_blank">📅 15:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79936">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
🔻
تشارك سفارات الدول الأجنبية في العراق بتوزيع الطعام مجاناً ضمن نشاطات موكب خيمة الانصار في منطقة الجادرية بالعاصمة بغداد ؛ العراق هو الدولة الوحيدة بالعالم الذي يشارك مواطنون من مختلف الطبقات ؛ الطعام مجانا منذ بداية شهر محرم إلى يوم ١٠ من شهر صفر اي بمعدل ٤٠ يوم كصورة للبذل والعطاء وتضامنا مع الإمام الحسين الذي أعطى دمه من اجل القيم الإنسانية والاجتماعية ..</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/naya_foriraq/79936" target="_blank">📅 15:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79935">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
🇮🇷
مردم عزیز ایران، ای مایه افتخار جهان اسلام..  محرم امسال با سال‌های گذشته بسیار متفاوت است؛ زیرا بسیاری از هیئت‌های حسینی در عراق، یاد و خاطره شهادت امام حسین بن علی (ع) را با یاد و خاطره شهادت رهبر، سید علی خامنه‌ای، پیوند می‌زنند؛ در حالی که روزه بود…</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/79935" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79934">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
ثلاث ناقلات نفط أجنبية حاولت عبور مضيق هرمز "بصورة غير مصرح بها" قد أُجبرت على العودة بعد تحذير من البحرية التابعة للحرس الثوري الإيراني.
يمكن عبور مضيق هرمز فقط من خلال المسارات التي أعلنتها طهران.</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/79934" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79933">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBu32qB22K55epT-WeSPkMeMmxo-dLvLH11vc_8yNn0QVA0xaKRpBtCthbF_nuLzkWNi842ztiJfd1GUKzuoIcrUu-etaR1y4wOKErDuVzO-7cI2tEQWJDn16lm6821kUzuN9cvG33HPqFC9iY-lVPpjd756zvoUvnd33X7QqpdwEP2NfTRnd8rouG-oZXSmalEXEnkPmNvP7NArA-rksjcWz1IXCMIPUFryTmamlsLmO1WWLiighm7k7hDRLAaE2-66eChiSQiE58mRcRH9GvQyo8mVsJ7DaUjAckiAfzHRl5E14nFUSpUrO5VnGLcqj7FSMASfl1vr8eGIZuTI2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أمين عام المقاومة الإسلامية كتائب سيد الشهداء "الحاج أبو ألاء الولائي" مغرداً
: ما العدوان على الجمهورية الإسلامية في إيران ومحور المقاومة، إلا امتداد لذلك الصراع التاريخي، وإن اختلفت الوسائل وتبدلت العناوين.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79933" target="_blank">📅 14:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79932">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">#عاجـــــــــــــل
⭐️
إنفجار عبوة ناسفة في جزيرة راوة غربي محافظة الأنبار العراقية؛ إرتقاء 2 كحصيلة أولية.</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/naya_foriraq/79932" target="_blank">📅 14:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79931">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9afd66d9.mp4?token=CeOpAKQ3ST56It6or1BgKi-z2HUzCjy-M6zUQgL6oW03uFWpMkLgm0c2ZJO0WSemh6TOF2zXHl_NYH2EMYuivX7MLIjcSy00uPJucxlAtKlvMqTKYplqVahdO5lAHisHzEZJ7XJU88oubHOGijzAqjQLSW5b0saxJVDRQfTvFRLdanCe4U6L_BdnAmsU6upcBfRwrlD2OREymnd1z3tYnzgrD1e2RweOSF6VL7NM9Ez0CpMuxGfhEGdaR99L1AedFR01MuNhW3h5dx1drfe7lYk8gt2ZcsEV1S_oGvz52utrLrcq78uOTAPE2gY38Nr56PzHoWUQaSIPtfK3avxFrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9afd66d9.mp4?token=CeOpAKQ3ST56It6or1BgKi-z2HUzCjy-M6zUQgL6oW03uFWpMkLgm0c2ZJO0WSemh6TOF2zXHl_NYH2EMYuivX7MLIjcSy00uPJucxlAtKlvMqTKYplqVahdO5lAHisHzEZJ7XJU88oubHOGijzAqjQLSW5b0saxJVDRQfTvFRLdanCe4U6L_BdnAmsU6upcBfRwrlD2OREymnd1z3tYnzgrD1e2RweOSF6VL7NM9Ez0CpMuxGfhEGdaR99L1AedFR01MuNhW3h5dx1drfe7lYk8gt2ZcsEV1S_oGvz52utrLrcq78uOTAPE2gY38Nr56PzHoWUQaSIPtfK3avxFrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
هاليوم هاليوم نعزي فاطمة.. جانب أخر من شعيرة "ركضة طويريج" في منطقة بين الحرمين بمحافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79931" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79930">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70fc449821.mp4?token=a9j95MXAl6GcZNEmJhbZfC5DTGfAf2baWN0lWiOYhtXOayMGa7agZ79OxEqqDiYVpbivK6LHTjHhA-ZyfFbn3erwJm3kUyFanZvyN7Z1IqVCLKMXd20KH8M6o99H3K8cznzkY05ABz4WCROzOrg0gnrmSlx8ZsUlRkFggCDKo0k0hFzpHAJTDEoNHP6RtEnIJLFeH7XhIKQAKQ01uFJddxmX8wyrgTQHyGXhRafOWrhpmW-VWf4xdvq3WpifTtnwwDw45rQDSBq_iPL5t_oLF5wPIxlEw74h86_RqBgvxhP0K9hoe2c-Nd-OD2IgPLAH0GOVHX4uskwL6eOH6v_a7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70fc449821.mp4?token=a9j95MXAl6GcZNEmJhbZfC5DTGfAf2baWN0lWiOYhtXOayMGa7agZ79OxEqqDiYVpbivK6LHTjHhA-ZyfFbn3erwJm3kUyFanZvyN7Z1IqVCLKMXd20KH8M6o99H3K8cznzkY05ABz4WCROzOrg0gnrmSlx8ZsUlRkFggCDKo0k0hFzpHAJTDEoNHP6RtEnIJLFeH7XhIKQAKQ01uFJddxmX8wyrgTQHyGXhRafOWrhpmW-VWf4xdvq3WpifTtnwwDw45rQDSBq_iPL5t_oLF5wPIxlEw74h86_RqBgvxhP0K9hoe2c-Nd-OD2IgPLAH0GOVHX4uskwL6eOH6v_a7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من شعيرة "ركضة طويريج" الحسينية في حرم الإمام الحسين عليه السلام بكربلاء المقدسة، الرمز لنصرة الحق وعدم الحياد عند مواجهة الباطل ويزيد العصر.</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/79930" target="_blank">📅 13:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79929">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1329577.mp4?token=ZdSnlZmAsFgPGAV4LH2WJ1sgwkuvIlazBYyd-M7kjGqdnlaubKjb7HxWr2kdtWTd5FKWVbKorx4A7kezfIDZlFWFR_y3ZUP_NBOM_emXYz59D_PEf49cpyOM2iSClpnp33NE0JbEn5CoxdZPwooWElt_Xz0W-z7nhxryEEBbLmtxM6-Oyyzu7HAWWFy3XM-cg1q2yAjeDNqHQ2aw0mXrgHsuxvTaReP7HFw2s-iEQShlGOGDvz9ZNt8Ku-t9yOM9brOdwUXS-AJX2HzR4f5UaPuuyG94_YX9YPeHT70iRYbEQn9LCpaMMe6rswh4tLXObKI8pJA3uyRZ7rkZ8-vrfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1329577.mp4?token=ZdSnlZmAsFgPGAV4LH2WJ1sgwkuvIlazBYyd-M7kjGqdnlaubKjb7HxWr2kdtWTd5FKWVbKorx4A7kezfIDZlFWFR_y3ZUP_NBOM_emXYz59D_PEf49cpyOM2iSClpnp33NE0JbEn5CoxdZPwooWElt_Xz0W-z7nhxryEEBbLmtxM6-Oyyzu7HAWWFy3XM-cg1q2yAjeDNqHQ2aw0mXrgHsuxvTaReP7HFw2s-iEQShlGOGDvz9ZNt8Ku-t9yOM9brOdwUXS-AJX2HzR4f5UaPuuyG94_YX9YPeHT70iRYbEQn9LCpaMMe6rswh4tLXObKI8pJA3uyRZ7rkZ8-vrfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رايةُ الحشد الشعبي تتصدّر حشودَ المعزّين خلال مراسم ركضة طويريج، في مشهدٍ مهيبٍ احتضنته كربلاء المقدسة .</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/79929" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79928">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
من كعبة الأحرار.. رايات محور الحق ترفرف في حرم سيد الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/79928" target="_blank">📅 13:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79927">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2776bed0c7.mp4?token=LNORqgTahIZTlP_Zts9J2MaDhyQR8amx7LujSYzmBP_wa48wKt9G_CbCAgk2IiUT3OqKHJSaFGs2LF7qEEOtGW8ABAF-6wqbPU_ZM8coR1z3aSkOw8fKKCtHmT-MjcpUzkb9ahfvYKstyD0oL50D05ZJ2JuUSYeFBoIBdgR6OhIduHNlZj4WZkGu-OFC8pssVrafqS-4gNsB36yhUBPYk8O_7vO9XxbYIcIbhVWAf43gGpGGOlRtOI2rvoeq_aEXjwPMjbZvPTLpPe5nvu8a7T6JeiRotmhgV3XdEifuRIZXSGm9K3T_lcgARp-mC7O5G_WpndUbnbGok5vyfQjRuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2776bed0c7.mp4?token=LNORqgTahIZTlP_Zts9J2MaDhyQR8amx7LujSYzmBP_wa48wKt9G_CbCAgk2IiUT3OqKHJSaFGs2LF7qEEOtGW8ABAF-6wqbPU_ZM8coR1z3aSkOw8fKKCtHmT-MjcpUzkb9ahfvYKstyD0oL50D05ZJ2JuUSYeFBoIBdgR6OhIduHNlZj4WZkGu-OFC8pssVrafqS-4gNsB36yhUBPYk8O_7vO9XxbYIcIbhVWAf43gGpGGOlRtOI2rvoeq_aEXjwPMjbZvPTLpPe5nvu8a7T6JeiRotmhgV3XdEifuRIZXSGm9K3T_lcgARp-mC7O5G_WpndUbnbGok5vyfQjRuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من كعبة الأحرار.. رايات محور الحق ترفرف في حرم سيد الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/naya_foriraq/79927" target="_blank">📅 13:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79925">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46bd0c99a.mp4?token=OaOe3KSxzUgoJyEX_rsdnfJM-Q9jGIs9b0BXvGc8WFbBxNYlJ61o_Ws_SfPfTGXpfU1L-y-qxdMMUfksPjaF20MfDbZqeRZY-10z1zI4VvSvQtwv7cdN-55fU_c5WcEsXaiW76qhV5ui60vmsPSRKOg_Y1j4dr8HTQBhiqCBTgFXDtY1Vd2Rt5YGF7984nE87nVPqfos08wNXiA9Uy7K1hxBgvNFPKXmCJ9rZR016L4xNMBnTKkW_OG9eh4lKEyVGR-0ZvLaLykUc2kfOGDaZVDmvLOhNAJogrI48IfB-rAsa5hs1LFWHLGfMdIMk2WwHc9fMciLuMS9oeZuUFMXHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46bd0c99a.mp4?token=OaOe3KSxzUgoJyEX_rsdnfJM-Q9jGIs9b0BXvGc8WFbBxNYlJ61o_Ws_SfPfTGXpfU1L-y-qxdMMUfksPjaF20MfDbZqeRZY-10z1zI4VvSvQtwv7cdN-55fU_c5WcEsXaiW76qhV5ui60vmsPSRKOg_Y1j4dr8HTQBhiqCBTgFXDtY1Vd2Rt5YGF7984nE87nVPqfos08wNXiA9Uy7K1hxBgvNFPKXmCJ9rZR016L4xNMBnTKkW_OG9eh4lKEyVGR-0ZvLaLykUc2kfOGDaZVDmvLOhNAJogrI48IfB-rAsa5hs1LFWHLGfMdIMk2WwHc9fMciLuMS9oeZuUFMXHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
حشود من الاف المعزين تشارك في إحياء شعائر سید الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/79925" target="_blank">📅 13:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79924">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e68c8ab7b.mp4?token=CNJQoJSfe_bVtj6tuP0H2qxc2lbEVYl7p3s_EuLdjO3EcjL-JRrosqc3eVsB2tLh2AiSmb3KbpXvJWkn159uh9m9Qo1vfrXt3n7lZ9R1UZWPJBdqsp85RdHWYcEZPx2a8oxsR8fHFyLc4Saai_iAulqbk0CgFeWQkY4F_hAMh766z81YlqYVCs9wEJeYQjTGZrsqw6EDpdJUPYPZY2Wph2RwKe0FOGEW3pK9qsD2PmCjZyr2NLjGoWhveYP72Z6la-nYI18NAFTBq7_pGKrLLhrMbehCNqllVNRGD3nI3wcnikcOumeiR2YJ1zTIdxH-ZsCYOq7F66fwnGl7DHTXrjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e68c8ab7b.mp4?token=CNJQoJSfe_bVtj6tuP0H2qxc2lbEVYl7p3s_EuLdjO3EcjL-JRrosqc3eVsB2tLh2AiSmb3KbpXvJWkn159uh9m9Qo1vfrXt3n7lZ9R1UZWPJBdqsp85RdHWYcEZPx2a8oxsR8fHFyLc4Saai_iAulqbk0CgFeWQkY4F_hAMh766z81YlqYVCs9wEJeYQjTGZrsqw6EDpdJUPYPZY2Wph2RwKe0FOGEW3pK9qsD2PmCjZyr2NLjGoWhveYP72Z6la-nYI18NAFTBq7_pGKrLLhrMbehCNqllVNRGD3nI3wcnikcOumeiR2YJ1zTIdxH-ZsCYOq7F66fwnGl7DHTXrjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انطلاق شعيرة ركضة طويريج من كربلاء المقدسة بمشاركة جموع المعزين.</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/naya_foriraq/79924" target="_blank">📅 13:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79923">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c00048c27b.mp4?token=CKHGsWNmpWdlDLb6fjEUkRpbyODv1UF-7NuCKQSDe8xERmcQ1su_2fnUP6-eBc9X5xFd9nciLNHZIyWkzTcbirjguw08IkyZHNJKkb-BXd_Uh1rMU3ArrxZxnjiDLOMrUebdnqzxTxs6E1GlFnmmt5jutlJypUd76OSsJg6dU-_USOnPWdOJheZmxT1j9LWElKqdTlxChpdJIqQ4fiKCE4xafwsq-3KSTjEvUlCpGXPgmkE6BKPwR8rnYIryrXTnKB9LPdgumBOlh-IeMfg8tfEdUBhqsUTl3QUHp0CerCMmRLhFwIy6h-wPoSDO1LrJAskw1DGOTUAqv4p-c2Y4fA3VuBOtVefdAoFj-EiRsuQXp5Ibyy455UZBHE9OzEJX5SJh_xdlTB1LJHIyL2Axar5Qucxgpi3aBqOkyk6dYZtaOG97uyUS5JGcqymA0EQw-JRVF8gJYT7wRZ6BbHzrzRpa7cu-DvBaOzGSKnEV3u59gwJpIx2ui-Md1YsAsYOgcHxok-EImYdvlm2m1Hn3LO6nV1yybV1cp4RG8MNfzfWhNtCNzDoskkNZM2_WS-XPPEsUulhuGq5tF3Q42g3QbkUDpFfxwsyTF3TURTdxbOSqPkIygWnAGnrMF60idV6MLWsj0xFxfdUvf-OO9hut5QpDi-yTJgrAbwIG0jnDIFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c00048c27b.mp4?token=CKHGsWNmpWdlDLb6fjEUkRpbyODv1UF-7NuCKQSDe8xERmcQ1su_2fnUP6-eBc9X5xFd9nciLNHZIyWkzTcbirjguw08IkyZHNJKkb-BXd_Uh1rMU3ArrxZxnjiDLOMrUebdnqzxTxs6E1GlFnmmt5jutlJypUd76OSsJg6dU-_USOnPWdOJheZmxT1j9LWElKqdTlxChpdJIqQ4fiKCE4xafwsq-3KSTjEvUlCpGXPgmkE6BKPwR8rnYIryrXTnKB9LPdgumBOlh-IeMfg8tfEdUBhqsUTl3QUHp0CerCMmRLhFwIy6h-wPoSDO1LrJAskw1DGOTUAqv4p-c2Y4fA3VuBOtVefdAoFj-EiRsuQXp5Ibyy455UZBHE9OzEJX5SJh_xdlTB1LJHIyL2Axar5Qucxgpi3aBqOkyk6dYZtaOG97uyUS5JGcqymA0EQw-JRVF8gJYT7wRZ6BbHzrzRpa7cu-DvBaOzGSKnEV3u59gwJpIx2ui-Md1YsAsYOgcHxok-EImYdvlm2m1Hn3LO6nV1yybV1cp4RG8MNfzfWhNtCNzDoskkNZM2_WS-XPPEsUulhuGq5tF3Q42g3QbkUDpFfxwsyTF3TURTdxbOSqPkIygWnAGnrMF60idV6MLWsj0xFxfdUvf-OO9hut5QpDi-yTJgrAbwIG0jnDIFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انطلاق مراسم ركضة طويريج في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/naya_foriraq/79923" target="_blank">📅 12:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79922">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ5VnZC-YwYsiV8tYwD3DmRMMMhVG9Iho7x8-y6d3VWPyNKKOGXXD5LoPnoFx1OYx3AOGM7IyYiQv0Mh2juuPO074QMqjbSxjDrNZkEf0oigxxTE9TxIzzvUXgCQxxESFW7NRqE8djw7Wqdnnk-UMX0lQoIU_3z_9LwSgrDxinUXh3c4kXm8wv3nKLXspb7IAp0puq3tWClOTzMC82YNIHKXdZYDFbAmP9r3xHRokHE8n3zIdTjIkg8a3nCDSxT4j-BVJBqvbgQj7oXy2QdDLW3bEYJlqWhCaAHSxgrxfLvdFI4nZX8ggk3jY5P4KEqSo8vNy_-6HYhcDdBoLAH_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
انطلاق مراسم ركضة طويريج في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/naya_foriraq/79922" target="_blank">📅 12:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79921">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79921" target="_blank">📅 12:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79920">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym-iL1monVZaUQb6BWEk3GEB0O2GEW1i2nsAyPUrgC8DAVLNvox1_wy-9C58VGUycS-V_yvtkfH-QVRCgXDY8jLFHk3F8X-g-kOIWQoh7YCdYDmTBGFa6DDcLbTavfOaEGXvyzefWCHsgdHwLo9z5uPw-mYgnyXRBgwH4Lwr2K-5mhZCDS1GRWb0ans3YKYxjVptH1xg4v3RYnAX3w10VognzBq5_qGH__g4DufX7bfo0-ZomYdPL5jv9fIq6ssRiOOA_gIXnGJbEYAuMMRw-TpGfmU1J5l72W7ViboJawH0LzfxVRi7tzHytsVnl0Klh8Za45oqTsj0L_xGmb-Y7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم ؛؛
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم ، كن انت المراسل وانضم الى فريقنا
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/79920" target="_blank">📅 12:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79916">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aa1hBXM-xUN3CJSeoAwYAv96OniKLVoua0dm2WYfr9FdmcsHBQ966-It51NAj1a-d9CNEeTWVz7gmZMDYjSimLQZITlIrGYAhCk7dsTIl6seGiE64V5Hp2pUsiHXMIGKmCCf-v3zpFEq0ynCXE14DqkIxKMMs_siOSrf1jlY-ZAX3O5s92bqVBt0gU7HsWFxWHZeC-Uz2W5CdFBDic4Y8LsOvBZ-_sLUhByh9Cd_Xdu2ZoVEsO3mcphwGTmxK7Gxcxgcki9K6-lWRMvd0-AE4KQaFp_K0l_9fVwPieE-LTPFESzmh5aKuP83myN5p8PErwEJIiCQpnhaGbkRq4CLSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OK7sAmUVDmwEqdmuojrgUtDgyc-udx4lzqAAgAjsI4astzAaNtC5TELOR6FSGRs9_w28EQttkB3lFl0aMdh_Hy7aEoQTJQ4l27WsUmop6VZO_NizzBMFLlHiWrm4iOXbDfEarpEMdq-attyhLTrRaZPAXzumkdxk9eAsfq0z7NdS0vDdI4x1fE4v1ilECAVgBLfDcnaSc2owNm-Kn_YRuQ69MNgUr3hqhZtp7gl9f9oJRj_RRX3_ew7G7b-mkaprov5pUDR42JJBKNJJmo8U-Hny3RE6fS537r8ztenhkVeDBSIVNb9ebuyoSO-eaojwon_noByGFDXErZPYeLtU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tz1CptEo-ykbEUloZCmuo0_9ieaaEJ10WQXCL5ip5qCpN5ts-g291DXeRS0RsW_mjMfA2BNDTlA01lvZNOAkfO526Bp_UUpqux67UvCto0v-CMfu7cqBijMFYfy_va27rzzZqaYyrUydHjAwTSjTxIExZ4wj-gKePLyNOZ98gxrncYntW9ujzSYxFxm8JTf1wyVGYTW2u3IAT8vVzYnM3H1LNjvMznsIWVnqDZFmfzaqGH5lLT8zo4x_nOD3EMWSSUtt7lnXpC839yuYX1Bf9zEv-vAdilk6svZjUpDjCSPzpyPQoDLxi6_0N9VoI0j-0I80KzuQIutY8cQYScuQ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVVBuBMtXltgtPV5x_HQV4P49ZNakGwZxM6omjg9uw4V8gV4DuKZWn3yPpVaOh0VWlAtE7KQZZMT4q-rQalYwVvcMqVboq1hsu7yfd515PTBStfF_xcC-kgMYD371Cz-rinGZm0qJVI3k8P7biogP-1exaEZd90hXnvr_bYPyNzDxYJBKqbmWNJwR06deAe5SUo_48oOZfU_U8ifA9KtsquiE0unuAM2xSE2pQe80GeAPMb_VHp8DgrolD-OoV3p_mC1hDnTaoKO8-0kUoLZc07QbuQo0HNwzGgB41_SawX8R1vNcVJaLwPifYEHEhdldPxoRhnO83pilJK5nuXASw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد إيمانية من داخل العتبتين المقدستين، تزامنا مع اقتراب انطلاق شعيرة ركضة طويريج.</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/79916" target="_blank">📅 12:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79915">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1beabe075.mp4?token=X9QOtxmowVHMtNSPXZCBgXPx5nL4KCTD24hklqfLoJDkjgncGEfHKjcKdrPK0mBwKkamdcDwcjaSnkuehb8I3AmB7tsCC12ilr0oEwaX0_0fGFREhRkwf22gkGMazawQ0x-99xhzQsi8VAUA0YzHakY3G-IaBxcBCSwqthbH94oUpTcBmyIrwTqJe2HF2ZVk0J4fGeIKUDIKXrlOz6cS6bAn04qmSFvddG-WnAaHUc3hCa0ejNHOcjUZ-ea1a2uwsxQo5YbUNvG7IJ-T6A-bDAYd2HtCRDLIu86rqQpz9qED1v8izz5XrcyAXgeLwrI5yyx4zDRVI2h9KHs3PuIojU03_PGBMtY_KcQCqzkYJ16feFLAsi-UehwsDiAZusiiJoVrBFrCFCi6-jyXTqbi1PqP3LjtPGpapxc5iTK-WZ8Cr0ibMH4tOhvi8G1tI63wASgqMi0rvltZUNkvkf1K9IWzfIcKnl1bBaTMVe3RbLP57LO6EyZXQZvWmQ12du7KYIKqbFVvgXIDsIXfZMt0IdXnf7IDNDh2fpw3IOewNBrz0ch2N8V05Bx7sbfHJUZqeuELhSYfxPE26hjlul49EtBb6XoNXVca-BP0j1DWJKm0YN-iGblSoJuBW4Swm_gU3MP6FduMPz0hFsBN6L0PPoXSFA4IFJK_y1pB_-qghYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1beabe075.mp4?token=X9QOtxmowVHMtNSPXZCBgXPx5nL4KCTD24hklqfLoJDkjgncGEfHKjcKdrPK0mBwKkamdcDwcjaSnkuehb8I3AmB7tsCC12ilr0oEwaX0_0fGFREhRkwf22gkGMazawQ0x-99xhzQsi8VAUA0YzHakY3G-IaBxcBCSwqthbH94oUpTcBmyIrwTqJe2HF2ZVk0J4fGeIKUDIKXrlOz6cS6bAn04qmSFvddG-WnAaHUc3hCa0ejNHOcjUZ-ea1a2uwsxQo5YbUNvG7IJ-T6A-bDAYd2HtCRDLIu86rqQpz9qED1v8izz5XrcyAXgeLwrI5yyx4zDRVI2h9KHs3PuIojU03_PGBMtY_KcQCqzkYJ16feFLAsi-UehwsDiAZusiiJoVrBFrCFCi6-jyXTqbi1PqP3LjtPGpapxc5iTK-WZ8Cr0ibMH4tOhvi8G1tI63wASgqMi0rvltZUNkvkf1K9IWzfIcKnl1bBaTMVe3RbLP57LO6EyZXQZvWmQ12du7KYIKqbFVvgXIDsIXfZMt0IdXnf7IDNDh2fpw3IOewNBrz0ch2N8V05Bx7sbfHJUZqeuELhSYfxPE26hjlul49EtBb6XoNXVca-BP0j1DWJKm0YN-iGblSoJuBW4Swm_gU3MP6FduMPz0hFsBN6L0PPoXSFA4IFJK_y1pB_-qghYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الآلاف من المعزين يبدأون بالتوافد إلى منطقة انطلاق ركضة طويريج، بانتظار الموعد الرسمي لانطلاق إحدى أكبر الشعائر الحسينية.</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/naya_foriraq/79915" target="_blank">📅 12:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79914">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b196168a39.mp4?token=fllE2-Fb6DkAmbkp4Ep-R8Q5PCqkiZ9H111mYfwqxrVSXkFgXhgHfk1GrWP8ZGCICLYizj8Mo3qqtOetkZ7CCQudzP1xI4A3wG5ncFM-q33mNks6rEm-4gTK3LhAFKWm_DOgATKGAO9M3T99fOAgLVF9FNVECzAPLkr-ZEVFrVirF4K2SQDMKxLVBSinBxzUY7uUnBrfgiG6AbB1wGYKmSkiWS_lsw3U4-xeDtREfgtC1zqtC2dtYq1T1d3dJxVgn3rt1QZYr3GZTUiz9-CMhWE5mdCL2VteHxbe6PXUZzCmgdJv-No11sdVXLdxxXiciMXi3oJaMXyZy63HvvjoZyxdg4xKUeEoK2G4awogyyeWalbIApIfBIq5LfzdsmnX7bp7qhQQFPSKylksFNTMYbyhmzaF3R4H66PpwmA5TyOV5v76-vYKeDwAzH9p-tXeuAQUC6z8t-qhaW9Gyz3rWHWhTtaa57nOiGfXTNGqmMUQtT-VzrpVJpNuSLUFhwLcjJE4-YlDmyRfGjpY9l5TX4RwnQJmPFw4J4S1k8ojpCIAse6TuGoBMXXI_OVHNx4gDGY0IaRsIlImq_m7ZP2al5ytJ4vBU-JKQ4U8_1XPSxXODcY3MgfLvG1tQ-SfW9aRGltbat04ssnu8sulvl40ZAm56P_Q8SsM2EH08Q5NJE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b196168a39.mp4?token=fllE2-Fb6DkAmbkp4Ep-R8Q5PCqkiZ9H111mYfwqxrVSXkFgXhgHfk1GrWP8ZGCICLYizj8Mo3qqtOetkZ7CCQudzP1xI4A3wG5ncFM-q33mNks6rEm-4gTK3LhAFKWm_DOgATKGAO9M3T99fOAgLVF9FNVECzAPLkr-ZEVFrVirF4K2SQDMKxLVBSinBxzUY7uUnBrfgiG6AbB1wGYKmSkiWS_lsw3U4-xeDtREfgtC1zqtC2dtYq1T1d3dJxVgn3rt1QZYr3GZTUiz9-CMhWE5mdCL2VteHxbe6PXUZzCmgdJv-No11sdVXLdxxXiciMXi3oJaMXyZy63HvvjoZyxdg4xKUeEoK2G4awogyyeWalbIApIfBIq5LfzdsmnX7bp7qhQQFPSKylksFNTMYbyhmzaF3R4H66PpwmA5TyOV5v76-vYKeDwAzH9p-tXeuAQUC6z8t-qhaW9Gyz3rWHWhTtaa57nOiGfXTNGqmMUQtT-VzrpVJpNuSLUFhwLcjJE4-YlDmyRfGjpY9l5TX4RwnQJmPFw4J4S1k8ojpCIAse6TuGoBMXXI_OVHNx4gDGY0IaRsIlImq_m7ZP2al5ytJ4vBU-JKQ4U8_1XPSxXODcY3MgfLvG1tQ-SfW9aRGltbat04ssnu8sulvl40ZAm56P_Q8SsM2EH08Q5NJE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الآلاف من المعزين يبدأون بالتوافد إلى منطقة انطلاق ركضة طويريج، بانتظار الموعد الرسمي لانطلاق إحدى أكبر الشعائر الحسينية.</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/79914" target="_blank">📅 11:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79913">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJBsgb_itLq9ETnyl8DvjjZS4yd-knC8VvbVZwOfNmrWYdi8T82yWR7glU2DFmTpxmSAWypabpC-VXf6jEPR8SKwSccupLLn-_zl_YgYSIzUGuBPbc6atbSPPEha72Djz2pUDBxSST36luyQKa4pamjgRbz9uRiNagRjnDCmTSuPsrqeQw4SgKXWu9BN9Oa-Ut62mRfAfqifrgGWPqd0cxuwF0Ut76jUAvMx4C9yqLI21uD63GFzeGstfBw265hR2rZ6WGBqKAtYbQ1GjVSRI7RVmzOAcY2G2RwtZfc6LvVriKZfVyzkpYHvX8Vz1O898Gk0yP2I-N25g1s6Nq-N8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية بشأن البيان التدخلي لروبيو ومجلس التعاون الخليجي
تعتبر وزارة الخارجية لجمهورية إيران الإسلامية المواقف الواردة في البيان المشترك لوزير الخارجية الأمريكي ووزراء خارجية مجلس التعاون الخليجي - بتاريخ 25 يونيو 2026 - تدخلاً غير مسؤول واستفزازياً، وتحذر من استمرار السلوكيات العدائية والتدخلية في المنطقة.
إن الادعاء بـ «الالتزام الدائم لأمريكا بأمن دول مجلس التعاون الخليجي» ليس سوى كلام فارغ وتحريف للواقع. لقد أصبح واضحاً للجميع الآن أكثر من أي وقت مضى أن الوجود العسكري الأمريكي في دول المنطقة هو عبء على شعوب المنطقة وعامل لعدم الأمن والتفرقة في المنطقة.
إن استخدام أمريكا للقواعد والمرافق العسكرية الموجودة في دول المنطقة لارتكاب جريمة عدوان ضد جمهورية إيران الإسلامية خلال الفترة من 9 اسفند 1405 إلى 19 فروردين 1406 أظهر بوضوح أن أمريكا لا تعير أي قيمة لأمن دول المنطقة وللعلاقات فيما بينها.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79913" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79912">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔻
أبرز ما جاء في كلمة الامين العام لحزب الله سماحة الشيخ نعيم قاسم: - تعاونّا مع إيران في فترة العدوان وكسرنا المشروع معًا.  - عملنا كمحور وشكرًا لإيران حتى يدخل الشكر الى النفوس المريضة.  - سنبقى مع إيران ونريد أن نكون وحدة حال لأنه تبيّن أن قوتكم مع قوة المقاومين…</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/79912" target="_blank">📅 11:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79911">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
أبرز ما جاء في كلمة الامين العام لحزب الله سماحة الشيخ نعيم قاسم
:
- تعاونّا مع إيران في فترة العدوان وكسرنا المشروع معًا.
- عملنا كمحور وشكرًا لإيران حتى يدخل الشكر الى النفوس المريضة.
- سنبقى مع إيران ونريد أن نكون وحدة حال لأنه تبيّن أن قوتكم مع قوة المقاومين في الميدان تساعد في إيجاد التوازن المناسب لكسر "اسرائيل" وطردها من أرضنا.
- لا خيار أمام "اسرائيل" إلّا الانسحاب الكامل من كلّ شبر وأرض لبنانية وإيقاف العدوان الذي فشل في تحقيق الأهداف التوسعية.
- أيّ التزام ضدّ سيادة لبنان لن يمرّ.
- سقف السيادة يمكن تحقيقه بأن نبقى في إطار اتفاق 27/11/2024، على قاعدة جنوب نهر الليطاني حصرًا.
- المقاومة مستمرة بوجودها، وحضورها، وقرارها.
- المقاومة هي عماد استقلال لبنان وتحريره.
- لا تستطيع السلطة أن تعادي أكثر من نصف الشعب اللبناني.
- على السلطة السياسية أن تعيد النظر في مسارها، وأن تعمل على جمع الكلمة، ووحدة الصف والموقف في مواجهة العدو الإسرائيلي، وأن تتوقف عن تنفيذ إملاءاته.
- نحن جاهزون ونمدّ اليد، فانتهزوا الفرصة، فالمقاومة قوية.
- هناك ضرورة لشحذ الهمم، وسدّ الفجوة الاجتماعية، وإعادة الإعمار.
- لضرورة الاستفادة من مسار التفاهم بين ايران وأميركا كداعم أساسي للسيادة اللبنانية أرسلها الله كهبة.
- لقد ثبت أن إيران طريق الخلاص.
- كفّوا أيدي الدول العربية والأجنبية التي تضغط عليكم للفتنة ولمصالح "اسرائيل"</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79911" target="_blank">📅 11:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79910">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe1d0acb8.mp4?token=KXosUQ5gxdK159cgCoG9SNreYjDkFQGGt_ExzwdaN7DGXTSVQKRH7CvEHV_RZNvuMyuuUd6H5BcfWfD4UomKx3Qc_27BMgrFs4GhA6qPF028O5FU5iNBf5P6IewObqcM4OxtTXmDptsMIYo0wM2LAoQXr99bU0jAfckvwCCR1VkuWYIzCLx0VUE59HcfuSzRZp5FL-ivWXBsaBieeqLndxGenRgBjensVtdptS1nUHNIN-QVSts2p6eqhOtwiQlOs5Id4lAM2nPfsBBmEcIRruehOJnyrA1-rVq7PDkXpV72Gv4vU8DeELqlAGaGh7GKQmctXNyU0Db07OUh-pQeQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe1d0acb8.mp4?token=KXosUQ5gxdK159cgCoG9SNreYjDkFQGGt_ExzwdaN7DGXTSVQKRH7CvEHV_RZNvuMyuuUd6H5BcfWfD4UomKx3Qc_27BMgrFs4GhA6qPF028O5FU5iNBf5P6IewObqcM4OxtTXmDptsMIYo0wM2LAoQXr99bU0jAfckvwCCR1VkuWYIzCLx0VUE59HcfuSzRZp5FL-ivWXBsaBieeqLndxGenRgBjensVtdptS1nUHNIN-QVSts2p6eqhOtwiQlOs5Id4lAM2nPfsBBmEcIRruehOJnyrA1-rVq7PDkXpV72Gv4vU8DeELqlAGaGh7GKQmctXNyU0Db07OUh-pQeQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ازدواجية المعايير في ابهى صورة لها:
في الوقت الذي تُنبش فيه قبور الدروز والعلويين في سوريا تسارع جهات سورية تابعة للجولاني إلى ترميم قبور اليهود خشيةً من رد فعل نتنياهو.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79910" target="_blank">📅 10:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79909">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء:
نعتبر تحركات ووجود الطائرات العسكرية التابعة للكيان الصهيوني الإرهابي في سماء بعض الدول المجاورة باتجاه إيران عملاً خطيراً وتهديداً للجمهورية الإسلامية الإيرانية.
نعلن أنه إذا عجزت الولايات المتحدة عن احتواء الكيان الصهيوني والسيطرة عليه، فإن الجمهورية الإسلامية الإيرانية لن تتسامح مع أي تهديد يطالها، وتعتبر من حقها الرد على هذه الأعمال الخطيرة.</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/naya_foriraq/79909" target="_blank">📅 10:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79908">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
مرقد السيد حسن نصر الله قرب مطار بيروت يعج بالمعزين في يوم استشهاد الإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79908" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79905">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plAUrU1MUQXpEyE-GM-jwCpPINMUyCjPnYxIs18vtNowpLjGEPH-YfbTY1nDWSVJPai4XumAhD7wVxuFurzyt513kvxcJ-Ys9IWQzoQiDCWG9jkryHyOJoRxQKrhkEOTHxKjOLqn4yaV2vMVsIQIUR5SpfIIjYh6MF2Puf0nJg-AnbPybRJcRKeIq6sPydaSRfkDhCGDu5YSi409_gtrER_8es471hiy7CvlNYE7-3Ldgy7JcpHUphBJzc_3yUJRdHBNpnBjKd_3UOKGxksRb9DVY9QVKIGOpPvjzB-E8KY0YQo4uYwe2ccOGDNec23kOqNCLYOnxIhbwDSYCXuALg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2K1uT-ugm6wWaH8wfTDuY9XX1pPRFsbiqrPP0RoacvLaKtF1VyYWbjf5gTNfHws8n_h3wTb0GrBZGU-xmf-ay9gEl1QgaQIxFAGW_tWg8QJ2kU79cHvGulcJcG49Dp6ktXMqGIiPx6hYbp4suySmcMTTq4blXOSeV-CVtfyogRGaZqtyeyiYB-bu63NLFE3iiu4un6Ixnz2xAZXdBfxRqzdhc1SSsnVcy-XOuXiw8uLf796nbRVinyPwAQT1bydaoB8CxieWxZ74pPhCbet6Re_RmEoZLLKXlquX9e-avbH0TGA3shIIPblW_-BxtzHIF7596H4ahaxyzovQIsIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWm3Um_pFBTFUwnI3I2ROzCIt6MqWwYv8n4Cd8b4rrXwyMKMQnewmYVPx88O_FUOk26pqaXPDJK1c_f8RKX4V1bJbE9cGkuAWjK16nZWm9nHvfQZFU5ThLfSN1tWwSdLxWXrP6je0BG4crM4M-IEehfYZKOvEvjJGA451yY_cuUCQKrJZEX-Pm32u80Wo0F6-IrzIguQaDySvYSZ6KZcVAu5u486PRcWq-BvIgJXvFhtnxFkGJtc3FWRRgFBRHtUDdy53AOzUGpfYMf9ak2o0I8dvu82P2XUNKxgQBpfWW2_SXtyo2szeSUmGQrl-_AlgNkkatrU9zKF71ioPLlRDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
جموع المعزين في الصحن الحسيني الشريف بمحافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79905" target="_blank">📅 10:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79904">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okjIQmnIe6_fv5CEa2pMwWWpy0rmLgC9hS_1f0wR_ezgoNF2XkILP4q-DiQFNhXA5wSynzKHnDen4LJOHSW8e37V6o0GJdVS9t3K7Ws2x6CTtv84QBRjJq7Q4Y6jqPpMXcaOhhNlWh4zmW2vl_ZwdN4OnME2_oYRpJ86pRj07PTh4CjI1jMgyngan-dXxRAGrEvkmMw0LugqeOiDipTK-hcbTKuqrsvC3pUVyKjvYLaDg2Ha9mym2prffTHomuujypAvxY6tqjdfjL6gKwISxWW5vipcQtKJHfdGRnf1B3_YDPxsUil-VJd_OrEMEUiRumSR-WGGASuraBnWcKUGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
أربع هزات أرضية تضرب الحدود العراقية الإيرانية منذ صباح اليوم.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79904" target="_blank">📅 09:43 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
