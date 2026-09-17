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
<img src="https://cdn4.telesco.pe/file/g20pT_YVNV4WUu4jZEcPrShFIrBvPBUCAatYEtI3CoVW7DusHQXChgg3yFuaD5AfLnZGJO6a6FkhycYfLW6z39lOJU7Wx6bnfuwzGfNCH12WrlhpuxqEIL6ApcNC9XbW6o7Jlck_UsC99v-4i_sANwG7SFvnl6Dc_eEtEghjdjTQATTL-2Ql24hddbb-1W22ZGIg1kTiXSon8YjVtY5M7y0o6trRW7Ls3XxEGkIebgsG5iYyPXgB5Gr_zd5UeOi-hyqwg4h6kkUGt_WX5s7AYIbS3Dq_EemKruKxDFkYtXwYoRoN7MuHrgWmg_Ocq8rKuDFB1RjwVHVmaKbG13fg8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 01:20:28</div>
<hr>

<div class="tg-post" id="msg-90843">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ee316d91.mp4?token=S2LQNJRc4u-UjtrYNHsa4qLW1k2WaGKGms3sbsvF9AB476pFEek1kE-hhlNjSkiLVD9oRcVxqJNdH3uW0kBmv59NEJwYQWHWpB71GWXv161WC61UcFXROZjtc26XAaHZJtbQT5TSeUO-EfmZsePLu1BjtzZ1gwIqDxIUsQQ4k4t6oVlhPNd15pW1nYxesmSfi0pAytkzaThtsvWtkwAvkLcZx1KQGP1bBWZUGfkooLnkEBahx-S-T7weaOtVy0yhVmE9oFETbegNJnVFE1X4OsD-u0mPdpFmaPXiXX0xLQ0U71B5pFEaNWvNpmDQ-7Y4cvnLzBGfn2Ij5jUnrD-PLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ee316d91.mp4?token=S2LQNJRc4u-UjtrYNHsa4qLW1k2WaGKGms3sbsvF9AB476pFEek1kE-hhlNjSkiLVD9oRcVxqJNdH3uW0kBmv59NEJwYQWHWpB71GWXv161WC61UcFXROZjtc26XAaHZJtbQT5TSeUO-EfmZsePLu1BjtzZ1gwIqDxIUsQQ4k4t6oVlhPNd15pW1nYxesmSfi0pAytkzaThtsvWtkwAvkLcZx1KQGP1bBWZUGfkooLnkEBahx-S-T7weaOtVy0yhVmE9oFETbegNJnVFE1X4OsD-u0mPdpFmaPXiXX0xLQ0U71B5pFEaNWvNpmDQ-7Y4cvnLzBGfn2Ij5jUnrD-PLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بين ياسر المالكي وقاسم عطا المكصوصي من سيختار تيار الحكمة الوطني وزيرا للداخلية العراقية ؟</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/naya_foriraq/90843" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90842">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزارة الدفاع الأمريكية : خلال فترة ترامب، تدرس خططًا لسحب الطائرات والسفن والأسلحة وأكثر من 25 ألف جندي أمريكي من أوروبا.</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/naya_foriraq/90842" target="_blank">📅 00:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90841">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un4ADKrh1gy715XKacikjVf0vPNoV_JBhAin09fEb4ohCciwD_B_jc1tjQlrIkK6v6n7BE9YFIUTiEP0dfbVDTtBdU5TAmZO9GfnQr_idESQZBzdMjPSahpFVDVHzPv7Jx0myDoKkcfwQ2oZWxeoJ2_p4U2H3SSIkrmxcomK2d774p4uNqMEwAgHqmzBMZ2CuwAJWdKKy4y_2l2MwnOX9zBmt9LjQ6J7gfSlNUncdbZEvsfJ9saRemHA58hvvNm6MQ6rFQiU9QSlca0usYXqzc7-cddOoqyaWyAwy4Bhq3Dfl8t1MHILjQ-__mzOi7UrSwq2YYVbeBRckCqdmE-WIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر صور الأقمار الصناعية لاندسات 8-9 الملتقطة اليوم أضرارًا إضافية محتملة في محطة أبها لتخزين النفط الخام جنوب غرب المملكة العربية السعودية، وذلك في أعقاب هجمات الحوثيين هذا الأسبوع. ويبدو أن ما تبقى من خزانات تخزين النفط في المحطة قد تعرض للهجوم والتدمير.</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/naya_foriraq/90841" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90840">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kByKmKegOk66liXDrcbXoMxKsIJjNmKtPzA6IdJmQ49kMVgEQxUz2Ripyf9-A0xNUBx-oDATYyavQfQOfev5ADsDmZE17OI-RlqgeL5ZceRS4rImmmEypOyqB8zpyac3DXano5qavXT0L_jUh9gaIhsE67_0AUHmk_kNWo8X37mnPHh_0_8MnYRXgz7S1vjCTaLStNLETGBL1aS0_wvBdy8GCr8ponjrW2une84e04VwbzPX0RsuvLHtICsgW1Y7H5N9MrcGcJPMXeikCPycD7WI4_aM0KHGg2uTGIMLt3PvA5y5mrExj2IZl3qbD8v5WnSP4FTaSgEOEDw5ldszEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر
استهداف سفينة في مضيق هرمز</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/90840" target="_blank">📅 23:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90839">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvnCW7WWFMX2D66MCLSNXIp-KoD5gFEDA9J2X_slYAp4ZCKT7p8Xo8Fats6lO7IAlCHJz8yPD-3aMHOgo8Lm8rkNGJ1ksvLygz0CSAAVYR2SgFJJzFvTxAU2eZSUO_NRGFwIB_ezBW_al_73Bh3EpvLFLECnX6FlmdYKEl_OIk-Pwynq6w28Nn8n-o2wkI2k5gb-R4wnBhb1ehe4LMBXhS9C7ad7bxgjnmodubHHpoDcfbQOoRmHcDBflUqVqNbajtzwrCt6Y41hsnVOMOcef2X4uuJn0LLfWwWWkOLnAU5oXAHIl_Gv3nbVhb3g5UaQG0PN3iBJbSqRF9qqPUQcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
: ‏انتهى النظام الأحادي القطب الذي ينتزع فيه طرف واحد التنازلات بالقوة والإكراه. وقد رفضت الصين وروسيا، باستخدام حق النقض (الفيتو)، الاستغلال السياسي لمجلس الأمن، وأكدتا سيادة القانون. يجب علينا الدفاع عن التعددية؛ فالأحادية لا تخدم مصالح أحد.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/90839" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90838">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/90838" target="_blank">📅 22:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90837">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/90837" target="_blank">📅 22:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90836">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu6MtomqVP3RaLE7qKzugu1-UpA2LvxU87CT9InPNF7YwscGPCyR0EJS-VdCtC56B9GMD_6fQkaSGk2OlZv_wmF49jYZ9ocU3ek2BgsEtWhHiTmQOYPp1GRAsMb-zCOzLuaKEm8U8HNu57jivuEyWocW5OfBOIUiaJNfkhTsY0QK5MUjhUgjsgAPWKyL6Zc8zSVSbmA42ZhU-FxNebSyUCmVRb24vSmMy7aL4lvS2bIs5NnVSqx5MUJRi6BErvtj29xmEUYD2tS6BtaaEfTrf7on6l1hlXR2cfic-ih8621xsfAac2gRIoU32kByiBh_3pvKf3vafIRVO18dXXTlow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
وردت أنباء أولية الآن عن تحطم طائرة من طراز إف-16 في مقاطعة بلير بولاية ميشيغان.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90836" target="_blank">📅 22:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90835">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
🇮🇷
الخارجية الاميركية:
واشنطن تمنح تأشيرات دخول لإيران لحضور اجتماعات الأمم المتحدة .</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/90835" target="_blank">📅 22:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90834">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
‏شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 37 غارة جوية بطائرات نوع "F15" أقلعت من قاعدة خميس مشيط الجوية واستهدفت محافظات تعز وحجة وخلفت شهداء وجرحى من المدنيين.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90834" target="_blank">📅 22:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90833">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
🇨🇳
حادث سير عنيف في محافظة ذي قار اصابة اكثر من ٨ افراد بينهم افراد من الجنسية الصينية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90833" target="_blank">📅 22:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90832">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇸🇦
🇾🇪
طيران العدو السعودي يغير على المدنيين في محافظة تعز.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90832" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90831">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇸🇦
المعارضة السعودية تنشر:
سَنْطِيح مَلْكُكُمْ وَكُلُّ حصونِكُمْ.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90831" target="_blank">📅 21:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90830">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امريكا تفرض عقوبات على منصة بتبانك للعملات الرقمية بتهمة العمل مع ايران
وعقوبات إضافية على كوبا</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90830" target="_blank">📅 21:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90829">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b77cfc018.mp4?token=JRYrIsZkhAMWelBmXRCg81gZDv7n6-NgezDED0y_8wQ-_F5wnFWhhX8ZBxWxeQx35-Dcv3u3Wphx1je5P3ly4LHUmFF-g2XqyP75X7MpyHz1h5g3f0ae3hJkDjbimr-AsQ0H5uWeu8tKA3Ri1AocKyMqm2oodaVYSmPQLYukm4HOhgSQ2hQVa8jY6GWZrJhxB5MjeMPptuAFHZC_2FYJztEiLigZUDr_llwE3jwwN3lXaCqlpJvblrb5BenwWKY_hvQiXVyvDHlvNVrQhb3P7e2hp5RdxUvVTiSqnM9XdMH6XCIFEB0FYEXDBV9GFR9vHy_3V28aWxzOcVkxf2ma-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b77cfc018.mp4?token=JRYrIsZkhAMWelBmXRCg81gZDv7n6-NgezDED0y_8wQ-_F5wnFWhhX8ZBxWxeQx35-Dcv3u3Wphx1je5P3ly4LHUmFF-g2XqyP75X7MpyHz1h5g3f0ae3hJkDjbimr-AsQ0H5uWeu8tKA3Ri1AocKyMqm2oodaVYSmPQLYukm4HOhgSQ2hQVa8jY6GWZrJhxB5MjeMPptuAFHZC_2FYJztEiLigZUDr_llwE3jwwN3lXaCqlpJvblrb5BenwWKY_hvQiXVyvDHlvNVrQhb3P7e2hp5RdxUvVTiSqnM9XdMH6XCIFEB0FYEXDBV9GFR9vHy_3V28aWxzOcVkxf2ma-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
‏الخارجية الأميركية: صفقة بيع مقاتلات إف 35 لايتنينغ 2 للسعودية تقدر بـ 24.3 مليار دولار</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90829" target="_blank">📅 21:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90828">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6c6c51e3.mp4?token=YeuSbIKA_OFwMPX7sbYg_TExl586L72q8fv0vDjkxM3aLg7w6u8UmATX9dPodnbbTAFpBIV4mM2UyD3ROV0ZVy2bcUfdUHuduIe31c8tpzyLDkZRlgvy5HS2MBUOmw3pPyyUtlCqeB8aj7gSlL-BExbTWUYAPl4O9v31uxGxor8ASgOYWHZCN7krNerOh3_bwAVOORxrICRcTXV6W_eIUVm4ChXrWoZoMV5VdyzomiirMEzbHc9cuv9sWmBCGHwDNu1ylTrP_4p7CeM1DbQTZqHNuRgb-pjVH2Hck41ErO8kv0fgMsDeLCRa3oYKTGzphHvkBwDZj7xC2OXKDZHbaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6c6c51e3.mp4?token=YeuSbIKA_OFwMPX7sbYg_TExl586L72q8fv0vDjkxM3aLg7w6u8UmATX9dPodnbbTAFpBIV4mM2UyD3ROV0ZVy2bcUfdUHuduIe31c8tpzyLDkZRlgvy5HS2MBUOmw3pPyyUtlCqeB8aj7gSlL-BExbTWUYAPl4O9v31uxGxor8ASgOYWHZCN7krNerOh3_bwAVOORxrICRcTXV6W_eIUVm4ChXrWoZoMV5VdyzomiirMEzbHc9cuv9sWmBCGHwDNu1ylTrP_4p7CeM1DbQTZqHNuRgb-pjVH2Hck41ErO8kv0fgMsDeLCRa3oYKTGzphHvkBwDZj7xC2OXKDZHbaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
إصابة سفينة الشحن التركية «ماريام إم» بمسيّرة روسية في قناة دلتا الدانوب داخل الأراضي الأوكرانية قرب الحدود الرومانية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90828" target="_blank">📅 20:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90827">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QII8cjcyWw-0S4SueRWL-iauJLqQQin_1m85Ga38QVBiXEW58eGFrhmEplex_WeWa5bDagpjhbJPn93jfyDwaT1e8Y2BXKXETOhJ2qscWu7K0VlMopAEG3JFvj6pZvqJIGvXfJWokNogWRWuzurAChAkwl0thIhAr1r3OmH_AAOR5NSWNlLxhsYpajbpXCSivTgpusWt5Vb4XcmcbtzBgxxgIHvTGd9WhIYXBIfSlpeD8FJj1dJEJAI1cm1WXvwHVWBR4YpbYNIQoieGATSwi2F52iZQZKxGb-QMNUSe3eKg76Hkyn4vNJGA9zNDXBsTDYnDO41Re6UYxFO6AZ_MiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
أخبار رائعة! بفضل القيادة الجريئة لصديقي كارول ناوروكي، رئيس بولندا، يتم إحراز تقدم كبير نحو إنشاء الولايات المتحدة.
قاعدة الجيش في بولندا. إذا حدث هذا، فسيتم الإعلان عن الموقع قريبا جدا. ستكون هذه خطوة تاريخية للولايات المتحدة العظمى. /التحالف البولندي.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90827" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90826">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
🇸🇦
‏
الخارجية الأميركية:
صفقة بيع مقاتلات إف 35 لايتنينغ 2 للسعودية تقدر بـ 24.3 مليار دولار</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/90826" target="_blank">📅 20:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90825">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gL1VHqpXEEWCRfJl8wzAROTZp40qAaTpLbqUs0HLN5k7eTVP0YAImNVjveWuP0zIEsyRxF7O433hJE7s9wU1k4cAKzqtkIhoxcxkFhEUbsVvbgry2cw8jToh4s-vpKrJFEBTXx0MBk5tXPw3z9TGIilpZb_zfU0ZydYUk4tlEH-b0j-dN791n3rXQ9-iwFWTgrzyhNQOcMvTJ8wb8kVHKGYA6yhUZT1kA40ohERYnISjTCpB7Ggq7azMqUJDDw3Cinb3TqcnlCAzBcqTXwnhw56mX8QRJqyZwdF-ZyVnKPkgt8z_SDUnZVNOdtzDYSXnirFHGJ3oUEx0IaWrUe4Yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
آیا ایمان لازم برای انجام این کار رو دارید؟
@Naya_Press</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/90825" target="_blank">📅 20:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90824">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
متحدث باسم الحكومة العراقية:
رئيس الوزراء سيذهب إلى الولايات المتحدة الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/90824" target="_blank">📅 20:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90823">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران: لدي قرار كبير قادم، أنا اقترب من منعطف كبير في الحرب مع إيران.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/90823" target="_blank">📅 20:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90822">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران:
لدي قرار كبير قادم، أنا اقترب من منعطف كبير في الحرب مع إيران.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/90822" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90821">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597f82b7a4.mp4?token=HdPPGsLR8lBsDjzIb3didhuw3e7sAUe31714lSjyWB2ngMqnF_ljlhcfcN_d0Jpwr6J8Knm3qURjxDj69PmtL5GpKat1tb5GYsKvxnrsvDQHaj1US-FvpowZ4uvKPaCFmW4Bx5GAKCmPSU5qeuD_kPc469RN9zjsYVxGWXzdZXVgK-0hUdD-RQEy3TovTEqAu9VwZReeuDZL44RPPHSzdKYUS-9HbJHZ4dUmi2tUoGROpiqF9JmbOv3R86_78_MwLxQ3MIpilwCh0EXzTmb8CtBEOLhJNWRYScsGbvoc87FD8YgWJHO9in0RgTpml7H0nYuuFp4yD1kO2DmbfF6k4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597f82b7a4.mp4?token=HdPPGsLR8lBsDjzIb3didhuw3e7sAUe31714lSjyWB2ngMqnF_ljlhcfcN_d0Jpwr6J8Knm3qURjxDj69PmtL5GpKat1tb5GYsKvxnrsvDQHaj1US-FvpowZ4uvKPaCFmW4Bx5GAKCmPSU5qeuD_kPc469RN9zjsYVxGWXzdZXVgK-0hUdD-RQEy3TovTEqAu9VwZReeuDZL44RPPHSzdKYUS-9HbJHZ4dUmi2tUoGROpiqF9JmbOv3R86_78_MwLxQ3MIpilwCh0EXzTmb8CtBEOLhJNWRYScsGbvoc87FD8YgWJHO9in0RgTpml7H0nYuuFp4yD1kO2DmbfF6k4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏المندوب السوري في مجلس الأمن: إسرائيل قابلت رغبتنا في السلام والدبلوماسية بالقصف والتوغلات
القدس تنتظرنا يا اخوان</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/90821" target="_blank">📅 20:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90820">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">إعلام صهيوني : إسقاط طائرة مسيرة تابعة لسلاح الجو الإسرائيلي في البحر قبالة شاطئ بالماتشيم</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/90820" target="_blank">📅 20:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اندلاع حريق داخل مبنى وزارة الداخلية العراقية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90819" target="_blank">📅 20:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90818">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">قوات عسكرية من عامة الشعب تبدأ مناوراتها في عدة مدن ايرانية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90818" target="_blank">📅 19:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90817">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQIjT3jByE-W3EKnrHIHhXTrQ4NtzKMTxTlOQ_AckAzsJymT5c-aR3fqD2BbF43xEl83id3Kzx9w55mW2V7J1B0KZfu-jQBd0pQBqamU0cszG0pu2RRbIr6rcRTMptHUrzWSOAwXPh3CM2jelLzYjjRuvsHGStQ4l7bMLAVdK-7kJFlTXU8EA6fQ9AZ1-2pOT5761Ls3emaGePOv-42uv5i-WJUv9a_nUIBhGipgoDQYc1IWmDf_I8fXV12d1Txnb9SjtD-fmmq5LpKbmbEMbuk4xqL3WyPgu4pXDEc3wPKx3A0BCdxN46dkMLWs7H8dFko6ZbYvWW3mUFPHi_FIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة معتدية قرب عدن</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90817" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90816">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90816" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90815">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇸🇦
الاعلام الغربي:
تضررت ثلاث محطات ضخ على طول خط أنابيب النفط الذي يمتد من الشرق إلى الغرب في المملكة العربية السعودية، في هجوم وقع الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90815" target="_blank">📅 19:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90814">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdAJ1kjoMjPPP1l_BUrtSzndrSZRQTV6_Jk3N2No0byvPeQ5JyTfJbcZrL_HIpPHPzGSUXcxM8gJjjkb1WIS5fADpZOp-AratD-3TxoPxHQIFssXebhNMAKEt-6_OR8nZRpkS7GIG_u7gb0fNFFej_6xhCPsTy4byhejkU60WkhzMG76zJArdc_M2gIOkroWTrR6jQ4sDegzVh7YIJRTONeU3HR5egFL8JcYVaCC7ffJ5Rbcr3W0hV7QHfhmiajcdkca4DbOs52HDLLTWUXNZYQgyBoFfNA5h6oLWTezUVhLqzxoXVfJ_4gnrQlaRPbIWscpAm6Vmr_Qdkn_TQYWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇮🇶
السفير الروسي يغادر العاصمة بغداد قريبا ..</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90814" target="_blank">📅 18:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90813">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">السيد الحوثي: لن نسكت على البهتان السعودي وادعو شعبنا للخروج يوم غد في صنعاء والمحافظات للدفاع عن شرفه الاسلامي</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90813" target="_blank">📅 18:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90812">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">السيد الحوثي: هناك تبعات شرعية وقانونية لهذا البهتان تجاه شعبنا ولذلك نحتفظ بحقنا في الرد على هذا الظلم والاساءة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90812" target="_blank">📅 18:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90811">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
استدعاء السفير الألماني في طهران على خلفية تصريحات مسؤولين ألمان ضد إيران.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90811" target="_blank">📅 18:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90810">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">السيد الحوثي: الانظمة التي تلقفت البهتان السعودي يتحملون مع السعودي جنبا الى جنب كامل المسؤولية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90810" target="_blank">📅 18:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90809">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">السيد الحوثي: كل من ادان البهتان السعودي باستهداف مكة المكرمة هو شريك في العار. انها اساءة لشعبنا</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90809" target="_blank">📅 18:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90807">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">السيد الحوثي: نحن كشعب يمني أنفسنا وأرواحنا وحياتنا وأموالنا وما نملك فداءً لمكة المكرمة فداءً للمقدسات الإسلامية بكلها.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90807" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90806">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">السيد الحوثي: قارون العصر السعودي المفتري يحمل راية هذا البهتان ضد شعبنا وهو قرن الشيطان ومنبع الزلازل والفتن.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90806" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90805">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">السيد الحوثي يدعو الشعوب الاسلامية لرفض استخدام مكة المكرمة من قبل ال سعود لخدمة عدوانهم الظالم على الشعب اليمني.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90805" target="_blank">📅 17:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90804">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">السيد الحوثي: العدو السعودي يسعى لحرب مباشرة تدخل فيها كل الاطراف الاقليمية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90804" target="_blank">📅 17:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90803">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مجلس الأمن الدولي يعقد اجتماعاً ويصوّت على فرض عقوبات على إيران.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/90803" target="_blank">📅 17:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90802">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">السيد الحوثي: استهداف مكة المكرمة كذبة كبرى وقبيحة وشنيعة للغاية كررها العدو السعودي عسى ان تلقى بعض الرواج.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90802" target="_blank">📅 17:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90801">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">السيد الحوثي: المعتدي السعودي استهدف في بلدنا كل شيء ولم يرع أي حرمة على الإطلاق</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/90801" target="_blank">📅 17:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90800">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انباء اولية عن انفجار دراجة مفخخة استهدفت مركزا أمنيا في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90800" target="_blank">📅 17:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90799">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مجلس الأمن الدولي يعقد اجتماعاً ويصوّت على فرض عقوبات على إيران.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90799" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">السيد الحوثي: شعبنا العزيز لم يقبل مصادرة حقوقه وتصدى للعدوان ولم يهاجم سوى القواعد العسكرية والثروة النفطية السعودية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90798" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90797">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">السيد الحوثي: العدو السعودي يتصور ان قوته واستقراره وتحقيقه لطموحاته يكون بوضع شعبنا ضعيف ومستعبد ومقهورا تصادر حريته ويصادر استقراره ومشتت ومتفرقا</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90797" target="_blank">📅 17:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90796">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">السيد الحوثي: العدو السعودي ينفذ عدوانه على اليمن بدعم امريكي واشراف اسرائيلي</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/90796" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90795">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">السيد الحوثي يبارك للشعب اليمني انتصاراته</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/90795" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90794">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بدأ كلمة المرگض ال سعود السيد الحوثي</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/90794" target="_blank">📅 17:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90793">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الكلمة بعد دقائق عند الساعة 4:45م</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/90793" target="_blank">📅 17:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90792">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">كلمة مرتقبة للسيد القائد عبدالملك بدرالدين الحوثي حول آخر التطورات والمستجدات</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90792" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90791">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90791" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90791" target="_blank">📅 16:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90790">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os1-A0eE2TE3Fqfm38TfMyLD5DLgIV21HfooET_oep_2GNNdICyc_wC-udtdC6hy6izLBFt-12N2DBDc86vXVZ4t2bN7X68FU5ejawAOswCY53FAgrn-Nm9JEhiiB_jPR5ooPbBnIdqWFOVMberRqESMjt2TFMQ0AJEVHIKXFq3fUTL_f_BsOjVTTquYb_ebvWPCaK_OoqXz3onmA2a00-LunaqeBGJSSqB_bOWVIAhpjq-VC1yFP4gP8ZDqxcEKD-OLyjjcuv5EuuWeqLwApC8C2Dd-yMylwWE5TK9895ibiFhacHC5JQ7TfJPUHxBH4Hl707-h7ftRTFasU4uLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صور الاقمار الصناعية: حفر انصار الله ما يقرب من 20 كيلومترًا من الخنادق حول منطقة باب المندب، على الأرجح استعدادًا للمرحلة التالية من الحرب</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90790" target="_blank">📅 16:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90789">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae63336bfe.mp4?token=surWPPykMQY70CfTkZ6FtMA8kTscqr2iTMSlYEDPxZkdZ9Cc3XU5u9xtqgkDbyyhwvuS0nZMB1wxM76Sfx3L0a_vb8Uu63MU8i8zqHaVdHj8bdIvpXusjxvFf2jNPI6Eh-B2Y-0ZNJHwmScKJhS9doGmwA3MLfFokOxD-6E8VSfpbFlGMsO6r6J5lm3mTUmXU1feaO4vbcj6lmsqVE0D_Sh3beB8_6By1t28D2uQqP13Av0sOndX_tJTALRizRNfsa8xFedWVMnYclb-AQZYO-225Q9mrpPYv5wqEc_MmimXArxYwyVYW2MGkEJwYSjNLYKJrOgsvPGji3NnCBQKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae63336bfe.mp4?token=surWPPykMQY70CfTkZ6FtMA8kTscqr2iTMSlYEDPxZkdZ9Cc3XU5u9xtqgkDbyyhwvuS0nZMB1wxM76Sfx3L0a_vb8Uu63MU8i8zqHaVdHj8bdIvpXusjxvFf2jNPI6Eh-B2Y-0ZNJHwmScKJhS9doGmwA3MLfFokOxD-6E8VSfpbFlGMsO6r6J5lm3mTUmXU1feaO4vbcj6lmsqVE0D_Sh3beB8_6By1t28D2uQqP13Av0sOndX_tJTALRizRNfsa8xFedWVMnYclb-AQZYO-225Q9mrpPYv5wqEc_MmimXArxYwyVYW2MGkEJwYSjNLYKJrOgsvPGji3NnCBQKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الاقمار الصناعية: حفر انصار الله ما يقرب من 20 كيلومترًا من الخنادق حول منطقة باب المندب، على الأرجح استعدادًا للمرحلة التالية من الحرب</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/90789" target="_blank">📅 16:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90788">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f88721f31.mp4?token=hoV6P2G86Y090cWschpR3r2BU1geHlJeOrsTIeWBbhpDayIu-Oo1z-HgzjH5E5N4EuRxdKsenQJIWfitKiJPEk8BgnTwqCUQUOG4A3vmQDjGS22VgiyHnqTZYGT6OuHWwyCw5VrKtZZahwjKvaS_pWdiuvMH7KaGT8BEfCLv2TIevRbQMW93sdFY4UjehioyJZ4lXFQv667DuOMEezyFzhZiDdwoFmjRUyyc-50JzzeIl_QT2sap3wRwFuT_jT4z9VYP3TWgnqveRuZ5peWB_MiKHELl4iDCsf57IGUG_Zh0VKYwNQlZIXS3KDbamMBsZ2GmiVsBRMt8gFY_4aPWwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f88721f31.mp4?token=hoV6P2G86Y090cWschpR3r2BU1geHlJeOrsTIeWBbhpDayIu-Oo1z-HgzjH5E5N4EuRxdKsenQJIWfitKiJPEk8BgnTwqCUQUOG4A3vmQDjGS22VgiyHnqTZYGT6OuHWwyCw5VrKtZZahwjKvaS_pWdiuvMH7KaGT8BEfCLv2TIevRbQMW93sdFY4UjehioyJZ4lXFQv667DuOMEezyFzhZiDdwoFmjRUyyc-50JzzeIl_QT2sap3wRwFuT_jT4z9VYP3TWgnqveRuZ5peWB_MiKHELl4iDCsf57IGUG_Zh0VKYwNQlZIXS3KDbamMBsZ2GmiVsBRMt8gFY_4aPWwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اسقاط الطائرة المسيرة السعودية في اجواء محافظة ذمار</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/90788" target="_blank">📅 16:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90787">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db63aa4992.mp4?token=S1GOJWiusTVGpoxFh2Z--ifTbT0xOyq7vNYfSra-aS9HCTQCDINF91IUNp-F9KWsOzM0R6fHRNMyw4ZCS7PVDvHTSKXqTkiwZYGSF8Kh76GjnVgMur4Zuas_e_H1HJyS4FUbRXIVcRSVr5qU9u3OxdQW43v3whdwQJGV1ixTffoQlpYzuLztH0lu9T0-LchMu1CjZuh5Yguk9zgowEcNNUdWfW1RIHfr890PSLTfYkXKmbxi7dQ2HNwloOu_6L7o1nan5ZDpt2FzwkLY2mCdKDrXVegfuEBZnrHhEy5axS8eRvN58xSXUFKlPoYMhZEmd6AtF2LOsh_sCh4ctN309mhxphDXwC-gwpCGqByN5fZ56L3HetEGmmipLQLf3mkOLkPKR1UxAu5iMwpy0BjGLWF4HiOPh0eZX-_IT7pZFfsiWpofRHAmJmrDWS6dNH3Ip7bfd-arXgMJwmXSwOsDqgTFNBmJxxGI8riI-WPbNUASLlclHS6wgeBWTdmDrqKwpxEjAVOPvedo2TV9oh3df23V5QDfhiL5iI9-wTQIUCEjm3DmMh2r3FTcSvXiMwwRrc-VcMDaq8__covb_b0fulTPlEUG8IWmJkwSkIHzJu1HIXxoe2EonQ0kow49wds9_kICFAGgecpl4zQphp8wTf5vQ09PvaLnCAA1KSMWW5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db63aa4992.mp4?token=S1GOJWiusTVGpoxFh2Z--ifTbT0xOyq7vNYfSra-aS9HCTQCDINF91IUNp-F9KWsOzM0R6fHRNMyw4ZCS7PVDvHTSKXqTkiwZYGSF8Kh76GjnVgMur4Zuas_e_H1HJyS4FUbRXIVcRSVr5qU9u3OxdQW43v3whdwQJGV1ixTffoQlpYzuLztH0lu9T0-LchMu1CjZuh5Yguk9zgowEcNNUdWfW1RIHfr890PSLTfYkXKmbxi7dQ2HNwloOu_6L7o1nan5ZDpt2FzwkLY2mCdKDrXVegfuEBZnrHhEy5axS8eRvN58xSXUFKlPoYMhZEmd6AtF2LOsh_sCh4ctN309mhxphDXwC-gwpCGqByN5fZ56L3HetEGmmipLQLf3mkOLkPKR1UxAu5iMwpy0BjGLWF4HiOPh0eZX-_IT7pZFfsiWpofRHAmJmrDWS6dNH3Ip7bfd-arXgMJwmXSwOsDqgTFNBmJxxGI8riI-WPbNUASLlclHS6wgeBWTdmDrqKwpxEjAVOPvedo2TV9oh3df23V5QDfhiL5iI9-wTQIUCEjm3DmMh2r3FTcSvXiMwwRrc-VcMDaq8__covb_b0fulTPlEUG8IWmJkwSkIHzJu1HIXxoe2EonQ0kow49wds9_kICFAGgecpl4zQphp8wTf5vQ09PvaLnCAA1KSMWW5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تسقط طائرة مسيرة سعودية في أجواء مديرية الحداء بمحافظة ذمار</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90787" target="_blank">📅 16:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90786">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18dcda2654.mp4?token=TbDdqtuDdwwoD9hl435PbiS2X7H6irzctQ2r83oXDu3BVP6bZI32A4H13Sn22qhB2QNrEtnDKOMVkCJnMWIe8VtSM8QYwtz_-1d1MXsDRJrysgBi-cCUYnayP_EYiytRGSVeeBho8YRDvoLDOkYQjPQtiuaqeXg4dYLk6CeYqLFMe9L0EdgJo-rLrwSAS694EH2h76rNrAq5EgBldKO9ntu46QTDt-4FHzyxBLaiy2LlxlQbhx64Ce8iDAixO0Aum1rYHEME4u7cUIjqSgNomkEQBVe2yml_-vgpkIX03qTVSfbri5rOx4o0uTAXPJSXs1J304sd4kcU-VcHcvqtLyMPK2zflfw8_59H5KdIrlYVQbQjvpPst3xbS14fqOX8-6cuBMX7iSAo44IFwPpBSCjxe5gwGElIPSRCXUFHrvwcLBMEXy8kQQaOMtab9HFTwYUP6wfP-R32eMJpMsGqNkk6j9Q8t4wW_-xjsJKiS_kUhuPvL5XRdiHIsp_kfaf56EVWTMMlWJq2gYJZ9tDlhC4cyyIuki73Ipo5EKcj_NU_mkuLb-mt6YVLsOZRVD-IiPU4jLffbn6586V7EPYTcSUn3k3Eg2gUhlsQ0fcqWaHKB08Tf8E9mMKuk0wU3jvjCbs5T7qtapIdnTT_thbjMyCYvk97ZbEQe8-KaB7ej1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18dcda2654.mp4?token=TbDdqtuDdwwoD9hl435PbiS2X7H6irzctQ2r83oXDu3BVP6bZI32A4H13Sn22qhB2QNrEtnDKOMVkCJnMWIe8VtSM8QYwtz_-1d1MXsDRJrysgBi-cCUYnayP_EYiytRGSVeeBho8YRDvoLDOkYQjPQtiuaqeXg4dYLk6CeYqLFMe9L0EdgJo-rLrwSAS694EH2h76rNrAq5EgBldKO9ntu46QTDt-4FHzyxBLaiy2LlxlQbhx64Ce8iDAixO0Aum1rYHEME4u7cUIjqSgNomkEQBVe2yml_-vgpkIX03qTVSfbri5rOx4o0uTAXPJSXs1J304sd4kcU-VcHcvqtLyMPK2zflfw8_59H5KdIrlYVQbQjvpPst3xbS14fqOX8-6cuBMX7iSAo44IFwPpBSCjxe5gwGElIPSRCXUFHrvwcLBMEXy8kQQaOMtab9HFTwYUP6wfP-R32eMJpMsGqNkk6j9Q8t4wW_-xjsJKiS_kUhuPvL5XRdiHIsp_kfaf56EVWTMMlWJq2gYJZ9tDlhC4cyyIuki73Ipo5EKcj_NU_mkuLb-mt6YVLsOZRVD-IiPU4jLffbn6586V7EPYTcSUn3k3Eg2gUhlsQ0fcqWaHKB08Tf8E9mMKuk0wU3jvjCbs5T7qtapIdnTT_thbjMyCYvk97ZbEQe8-KaB7ej1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تسقط طائرة مسيرة سعودية في أجواء مديرية الحداء بمحافظة ذمار</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90786" target="_blank">📅 16:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90785">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏الدفاع المدني السعودي: حالة وفاة وإصابتان بسقوط شظايا إثر اعتراض مسيّرة في محافظة الطائف</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/90785" target="_blank">📅 16:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90784">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1iSioW0NyDobVqhhq0eBbjnONcm_cfLaKx5jY49bRgHZCUg9e5vArJaFCoFo1xGzrRW_EOrr3ls4ajqH_F-h8lr7JX0GDSKf5l4GTLQ9xC8DThIupthR1_tjP1Z7-ScvyaCEswiVN5eerFxFMWatgWPUc2i2h43bZxyQeFY2wCxA3-t6_zizOqSdAe-9ioTrUi8dDU5ttt6xhI-7m08JXr_FCLPOX6l9wDFoYjstgHEr6iHpwufuNUxKCTKK_7m6DTaTL7G2rXSxmu2ZwkfIJMLaFPwTtCLDk7GmOuK5FWlvhkMnfTfsqCcg2_eRbUddlPDESL61pPbnVgOhVXBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏الدفاع المدني السعودي: حالة وفاة وإصابتان بسقوط شظايا إثر اعتراض مسيّرة في محافظة الطائف</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90784" target="_blank">📅 16:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90783">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
وزارة التربية العراقية تقرر بدء الدوام المدرسي في 1 تشرين الأول بعد استكمال استعداداتها لانطلاق العام الدراسي الجديد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/90783" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90782">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وسائل اعلام: السعودية تطلب من سلطنة عمان التوسط لدى أنصار الله لهدنة لمدة أسبوعين يبحث خلالها كافة المطالب الإنسانية وتنتهي بنهاية الأسبوع بإعلان اتفاق</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90782" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90781">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns3tWI5PhLi4sZVsdj26lsbVBnkSbVBva_NKdFj5CWch-c1yuqQZpChB8Fdj2jU7gcTJ2Tzt4C_cH-a6NLUK0S_iPAKD3c9af3nJ0SGbCPaS9hyn-smn3y8yl6S193sYf7720l5JA4qyJIe7hvcNltJX6FlL1Ib5UArPIyCFm0ypr30c3f1uLUQxrpVCxMzyI2lGgmNFsO8IjFGtyNbXGmOCwsqrLwflBedx135n90rO7Y4PczLONPn2WNKZLMRgGXSA7N4Y7y4ZFanJmY_Unjkclfh_iNdFCfe_C1yzT_dHczUfis51z199OY491iWtf_9OvKsA32eo_xCJVuycYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام امريكي: السعودية تلجأ للصين وتطلب منها الضغط على ايران لاحتواء انصار الله.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90781" target="_blank">📅 15:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90780">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اعلام امريكي: السعودية تلجأ للصين وتطلب منها الضغط على ايران لاحتواء انصار الله.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90780" target="_blank">📅 15:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90779">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تواصل تصاعد اعمدة الدخان في شمال الكيان بعد تسلل ناجح لطائرات مسيرة</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90779" target="_blank">📅 15:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90778">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKPKiPOSwf4NSwLCz2InmGUqJCjgoOzTUHc6kUxTI7xxJh0Ne2vKBcBdorp9hTGcUKpA6-9qh-DtOKh73kepCC8qCrG_QPahKyE3WOEzTobflDWW7TRlKYehfzXbnh191mPxEbxkCu27e4Y_O0sgjvbOIt47FF08pRUSpOr1Fbto6NbYgp5aJyTkCBHVcDch1KXpl5ewY_pYs6zMzY-CoVZWYZFM3hRQZxvolKDjLZLGnV2o4RTPqcfNlAAytSPuHsn1MDn6ecdhdmkEpdWUkgqwIm4jwzXQXFExsTyDr7YHNgJjIKHXEcdKWtep16WeHjocqWpkM_EoG14YqqDlUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من تفعيل الدفاعات الصهيونية في شمال الكيان</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90778" target="_blank">📅 15:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90777">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b3c39fe7.mp4?token=eaI4RG8T3Hb_PSVgH3xqpK58mNQQrlScEklLSgMJiHRPs1pcv35F2PYx7XpS3xPHAiouSeinYPndDJY1XVMzRodaa2WDXpK5D1QV3TgI41y5OUnkHhG-dMRjRxb4IqOX88J9GPqG626K67MjWI7TmljLVkpuWJ9PSifmN6QQQ_GV1XxCCavcUWv7_EY-M6rJuECVjaVuasTmZQ7gmcjguqYdC1g8tS7LvLFs11Dm6XQMc_9XOw_4II5Uk9PpV4PZoQqQcQTtrmrZ3YryeuKwJL84PerXbE3o8HXs4HaaZC3BsRAtqLryo43V7kw97AwQdG46RAqCJQPTaEKOBInM2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b3c39fe7.mp4?token=eaI4RG8T3Hb_PSVgH3xqpK58mNQQrlScEklLSgMJiHRPs1pcv35F2PYx7XpS3xPHAiouSeinYPndDJY1XVMzRodaa2WDXpK5D1QV3TgI41y5OUnkHhG-dMRjRxb4IqOX88J9GPqG626K67MjWI7TmljLVkpuWJ9PSifmN6QQQ_GV1XxCCavcUWv7_EY-M6rJuECVjaVuasTmZQ7gmcjguqYdC1g8tS7LvLFs11Dm6XQMc_9XOw_4II5Uk9PpV4PZoQqQcQTtrmrZ3YryeuKwJL84PerXbE3o8HXs4HaaZC3BsRAtqLryo43V7kw97AwQdG46RAqCJQPTaEKOBInM2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدخان يتصاعد من كيبوتس دان</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90777" target="_blank">📅 15:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90776">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اعمدة الدخان تتصاعد من شمال الكيان</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/90776" target="_blank">📅 15:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90775">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds_6LHKjsmSeSit4OG3u46rm1ZZzo6Yl8dNMxgL95ViFAv9gSaajKQFIGx8bl0VGLLe1ltJIyEeh4sippx61_MsCzIvVHuLYxE5raFCiZkBJW2GbbGZJBtS0M5oQ1WLCzgjTCRbx72fEuzAEW-uFoQsKwRB-jsrsqNqczXtlSkTFu2xFznXwv4nITeBhxBfnJpGg65fu4M5XhQHC0cwnMXirTqDAWLLo6dbw3w-TMDMFI7slbq7e1QOCTEBGQIsdgE6ZxUJp2DYWkWsoLV8JoFC2MvhVXb_bEzcLEls8RnK2PnGFx-1QKzkSo3VEymMkx3v6PYG0H_62P8zQakQ-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من شمال الكيان بعد تسلل طائرات مسيرة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90775" target="_blank">📅 15:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90774">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39633299af.mp4?token=m0ybt2m9dMI_fZEKGiD4LO6wWqj7jGaeuJs3HDjIOBRyVFTAXlK1IjVTcf57fkMbb9IUhIx9bZiQUuCPcUqs0AkTl8ZvHvq19ZbFMTn1D4rUd1czbloV8a54zwh-4jffbQlR7srHgagNDOHV-EzFzd6ONZxbOM0pPdJv6cMpAlnmwrEx8eaYDgghqgltfsR6oiY0Dn-2Pir_4Joryuu8TtfmJnzdQBAcZ4Q-7B5peWwnlR_8CkE0jvi22dXvsb9JQJuhbEFgZVpveqTBaKZ7W80gfekHn4gBMkGLG7AbmSehs297na7yy77kI9crPMMoJA2lICfYYQMpI7vM3fUa8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39633299af.mp4?token=m0ybt2m9dMI_fZEKGiD4LO6wWqj7jGaeuJs3HDjIOBRyVFTAXlK1IjVTcf57fkMbb9IUhIx9bZiQUuCPcUqs0AkTl8ZvHvq19ZbFMTn1D4rUd1czbloV8a54zwh-4jffbQlR7srHgagNDOHV-EzFzd6ONZxbOM0pPdJv6cMpAlnmwrEx8eaYDgghqgltfsR6oiY0Dn-2Pir_4Joryuu8TtfmJnzdQBAcZ4Q-7B5peWwnlR_8CkE0jvi22dXvsb9JQJuhbEFgZVpveqTBaKZ7W80gfekHn4gBMkGLG7AbmSehs297na7yy77kI9crPMMoJA2lICfYYQMpI7vM3fUa8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ضخمة تسمع شمال إصبع الجليل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/90774" target="_blank">📅 15:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90773">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">محاولات للتصدي في شمال الكيان</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/90773" target="_blank">📅 15:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90772">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWxkigrkil2DTmKoHbTZbYZG1DGEK5aK_APWxnpBhZJWnUh_zt9WI7lcV7ZtLghgBz3l1iIPGU6GirNTwXm52n2ojgjL1BAWxi2Zjblk2tgi6l1H5vex0ZZEpnNwzkiXEokYchB_ZQdCZ_bcN8Dy7hXWkerHut3zW6qcxn_JcVeO-7ZwUYMW7wmd4OR8ybEyewTOwk7RL9B3PDz23KPVt5bIkvHG1FnEpBbBW4aOMGwbTWiut5_qlJnLh9PVBuyWdlMQOV4TxTOzHqpv-dGv_07C_Se8T7UoVtKOIF4z3MfBqzJ2hnHHZCbvcJdYhpco-cd_prHowMAE9_QeHzsiWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل الدفاعات الصهيونية في المستوطنات الشمالية</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90772" target="_blank">📅 15:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90771">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تفعيل أنظمة الإنذار في منطقة منارة ومرجليوت</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90771" target="_blank">📅 15:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90770">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل طائرة مسيرة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90770" target="_blank">📅 15:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90769">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل طائرة مسيرة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90769" target="_blank">📅 15:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90768">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">كلمة مرتقبة للسيد القائد عبدالملك بدرالدين الحوثي حول آخر التطورات والمستجدات</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90768" target="_blank">📅 14:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90767">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b327d0501.mp4?token=nraUQuS-eYLpU_rTN_o3qgeTq9-GY0kd0cHEulFM4jyhW5BPXZ_ZosPs72ncfB2JdtljDX8iXrSsiTDuJ_-F62TvNFKr4tTKUESVv1tAVi_PL6QjDFK3Nf-il11ne2PhpK1fDDv2khjO48q5apIsjYWKkuwQA9VGHKW7SSTh2elYgGrHcY5NYQ5UdBXRpueN6GObd5RX2_bA4EWgMpHpNL_omupUSEUnMIWS0YAYP-btMWfVmqXshMQZK2aNadVF-tcoJCOq6nKoWdsHq3G43dOVWC0FS0_p81lRPOyOaxga_K89qZ077uqRoGpXKsFXsqiHqXtHYGmbG1T1-HpcYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b327d0501.mp4?token=nraUQuS-eYLpU_rTN_o3qgeTq9-GY0kd0cHEulFM4jyhW5BPXZ_ZosPs72ncfB2JdtljDX8iXrSsiTDuJ_-F62TvNFKr4tTKUESVv1tAVi_PL6QjDFK3Nf-il11ne2PhpK1fDDv2khjO48q5apIsjYWKkuwQA9VGHKW7SSTh2elYgGrHcY5NYQ5UdBXRpueN6GObd5RX2_bA4EWgMpHpNL_omupUSEUnMIWS0YAYP-btMWfVmqXshMQZK2aNadVF-tcoJCOq6nKoWdsHq3G43dOVWC0FS0_p81lRPOyOaxga_K89qZ077uqRoGpXKsFXsqiHqXtHYGmbG1T1-HpcYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان سعودي على منطقة الحوبان شرق تعز اليمنية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90767" target="_blank">📅 14:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90766">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇷🇺
سكرتير مجلس الأمن الروسي سيرغي شويغو:
الولايات المتحدة الأميركية وأوروبا معنيتان بإضعاف موقعي روسيا وإيران وفرض قواعدهما الخاصة في جنوب القوقاز، خطط الغرب تتضمن تقليص تعاون روسيا مع دول الجنوب العالمي وعزلها عن العمليات العالمية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90766" target="_blank">📅 14:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90765">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ab7a4269.mp4?token=FAlpYruXqZ5PgOdWGsyT9csAq1Wk4P9lQU4uz-2mVirg8m3q9b0CXIOno1x9naZqq4KyVKs3J_-L3NETjj5t_m9xQ3lzRhK9OLVLpdqxrSFpSr4jlIC934bMp5mGWVy0Xwfqgv17oW-kJYLrAzwZkROgEGsOXBZ5myHQ-OwbnozCvDz33MQo5NJOyL9BV_rloxtUma0Y807hI9F4aX5o7bwpIbi8qZBcr5vUSmN2o1AJKZlxEREkkcMNeKG2BXd8EeVJm-YUwT48TRXeDjTjXtNHjJxwZNpookDcGTP4qvUzLcNPdCP5VD13qLeyuu3ZMH3ibvXXMlPtNueG4fWtUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ab7a4269.mp4?token=FAlpYruXqZ5PgOdWGsyT9csAq1Wk4P9lQU4uz-2mVirg8m3q9b0CXIOno1x9naZqq4KyVKs3J_-L3NETjj5t_m9xQ3lzRhK9OLVLpdqxrSFpSr4jlIC934bMp5mGWVy0Xwfqgv17oW-kJYLrAzwZkROgEGsOXBZ5myHQ-OwbnozCvDz33MQo5NJOyL9BV_rloxtUma0Y807hI9F4aX5o7bwpIbi8qZBcr5vUSmN2o1AJKZlxEREkkcMNeKG2BXd8EeVJm-YUwT48TRXeDjTjXtNHjJxwZNpookDcGTP4qvUzLcNPdCP5VD13qLeyuu3ZMH3ibvXXMlPtNueG4fWtUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدأ موجة احتجاجات كبيرة جديدة في سوريا بسبب تعنت الجولاني وحكومته واصراراه على قرار رفع اسعار الوقود
اهم شي رجعت اصاله عالشام</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90765" target="_blank">📅 13:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90764">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
ندين قرار السويد منع أحد دبلوماسيينا من مواصلة مهامه في سفارتنا بستوكهولم وأبلغنا سفير السويد بأنه يتعين على أحد الدبلوماسيين السويديين مغادرة إيران خلال 48 ساعة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90764" target="_blank">📅 13:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90763">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇾🇪
🇾🇪
انصار الله يدعون لخروج جماهيري كبير يوم غد للشعب اليمني الابي في صنعاء والمحافظات اليمنية بعنوان (دعم القوات المسلحة ومعادلة الحصار بالحصار، وفضح أكذوبة استهداف مكة)</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90763" target="_blank">📅 12:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90762">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNYDoeCIS2bNkl_v_iskzzEfhq3LtJK0xbGoAMAenFA693DLcTK2631pMk8j3ABDOSBypKa24RmeVO46cXzCa3eNv8kWxA-ClelBx2ofajRN03XUIfmJSEhq8im-4gb5a_ov48OE4j90b5-tABC1PxBr0DQQUetfB5vMSJ4ZOAlJJ8Xy4uXLy5X8VatDRedhq16Evkvk7Bn-Lc7fMV6a2V38DbcyhF9oQoZ0WxY9Q2H0nSuuUZORWii0Xr4pCDu0UdE2Hh_3kJx6NTdZZrQ8UBDSId89RL9zJh4S692KOnNYU4MiOOaZ58c-6TJu8lP4EGOj78-vyHSVeZhhz9e6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر في الحكومة اليمنية لنايا
ندعو الشعب العراقي الكريم بأن يتريثوا هذا العام ولا يقدموا حجز او دفع مالي للحج عبر هيئة العمرة والحج العراقية فقد يكون هذا العام موسم الحج مجاني لكل المسلمين .</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90762" target="_blank">📅 12:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90761">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏴‍☠️
🇷🇺
زلينسكي : استهدفنا مصفاة ياروسلافل النفطية. و مطار عسكري في روستوف، وزعم زلينسكي عن أضرار لحقت بطائرة أنتونوف An-12 وطائرتين من طراز An-26 وثلاث مروحيات.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90761" target="_blank">📅 11:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90760">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏
🇸🇦
🇺🇸
🇨🇳
نييورك تايمز :
حذرت أجهزة الاستخبارات الأمريكية من أن بيع طائرات إف-35 المقاتلة للسعودية قد يُعرّض تكنولوجيا حساسة لخطر الاختراق من قِبل الصين، وقد تناول تقييمٌ أجراه البنتاغون قبل عدة أشهر إمكانية وصول الجيش الصيني إلى قواعد في السعودية، واستخدام الرياض للتكنولوجيا الصينية في بنيتها التحتية للاتصالات .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90760" target="_blank">📅 09:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90759">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94042c2176.mp4?token=uJypsnZXIsmFMI-tvXk8ZFprgW5W7ECNGiCgCnN0tomzV8LYtZd9PWrIoXrwx3rdivLuYpgN_dlglfG-3zm9ePs6vG7iMEn2VnY2oRbteE_dklPzDJXFp-wAWKlatOcjsj9tg2TyMn7b9hmtXUpMuWQk2sGtnkUHDDBExFU2TMRr4SClhRAdzRFDM9henCNVTULHkHzsu7fVF5szGxxA0BsAUtDKpm_jGnewDgJhRjgmego9vhWVq4whMuGteOMD5ewGBwZ56aeVDsmriIjP_-U4w0pXpNgSWKhuLfVY0e690HMdZoN5qPcj0Isz4odl5e0LHVlYTzESV85aHkpcgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94042c2176.mp4?token=uJypsnZXIsmFMI-tvXk8ZFprgW5W7ECNGiCgCnN0tomzV8LYtZd9PWrIoXrwx3rdivLuYpgN_dlglfG-3zm9ePs6vG7iMEn2VnY2oRbteE_dklPzDJXFp-wAWKlatOcjsj9tg2TyMn7b9hmtXUpMuWQk2sGtnkUHDDBExFU2TMRr4SClhRAdzRFDM9henCNVTULHkHzsu7fVF5szGxxA0BsAUtDKpm_jGnewDgJhRjgmego9vhWVq4whMuGteOMD5ewGBwZ56aeVDsmriIjP_-U4w0pXpNgSWKhuLfVY0e690HMdZoN5qPcj0Isz4odl5e0LHVlYTzESV85aHkpcgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
القيادي بالمعارضة السعودية
يكشف عن خطة " مبس " بعد فشل التحشيد حول فكرة قصف مكة، محمد بن سلمان قد يتسبب بعمل إرهابي في مكة أو المدينة ليلصقها بالحوثيين. على غرار محاولة ابو جهل بالاستعانة باليهود في الحديبية .</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90759" target="_blank">📅 09:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90758">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇸🇾
إندلاع إشتباكات مسلحة عنيفة بين عصابات الجولاني ومسلحين في مدينة الصنمين بريف محافظة درعا السورية؛ سقوط قتلى وجرحى من الطرفين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90758" target="_blank">📅 07:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5f30186f.mp4?token=eX_elRKiZrUF-B6BoNXUCztoUFuG71b7Sa31V77ArJYI4fttsn3aXamkP6BrFRoFuHjo0IBYINBsvNrnPfGV9sRPbLZSgEnu8jHUY8bBdj_udEYMmB3PRXvvj5Lb_JLtxz65WCGtaVj90YD1gWJXG7GvPb8Og5Rzdp9Rzp5DZhSjo2vkiiWQFEH0AW9Zgf8karemm3Bu2mQYtKdxwR_JQ2U5fIuHopJoYnioLPTKRFIbd4OCtbpQZJHR8VaKXFZp5-lj7tSjty7dnPMOag2yKXbGL88n7coUCInegKz5pSY1VuQ_p54n7LHEZbu8QQ0WOuCk7_ytQEtdsQGIH7s5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5f30186f.mp4?token=eX_elRKiZrUF-B6BoNXUCztoUFuG71b7Sa31V77ArJYI4fttsn3aXamkP6BrFRoFuHjo0IBYINBsvNrnPfGV9sRPbLZSgEnu8jHUY8bBdj_udEYMmB3PRXvvj5Lb_JLtxz65WCGtaVj90YD1gWJXG7GvPb8Og5Rzdp9Rzp5DZhSjo2vkiiWQFEH0AW9Zgf8karemm3Bu2mQYtKdxwR_JQ2U5fIuHopJoYnioLPTKRFIbd4OCtbpQZJHR8VaKXFZp5-lj7tSjty7dnPMOag2yKXbGL88n7coUCInegKz5pSY1VuQ_p54n7LHEZbu8QQ0WOuCk7_ytQEtdsQGIH7s5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب عن إيران: بصراحة، الأمر سينتهي قريبًا لأنهم لا يستطيعون الاستمرار. أمتهم مدمرة.  قد يكون هناك ارتفاع طفيف في أسعار الوقود. لكن هذا سعر زهيد للغاية مقارنة بما فعلناه.  قد يكون الأمر أكثر من ذلك. وبصراحة، حتى لو كان الأمر أكثر بكثير، إلا أن هذا كله…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90757" target="_blank">📅 04:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b525552494.mp4?token=HAsul6Zh2TnOSLM60bhbg3hRPs26zZ82H_EmgjNdmw-Z3XBFFijOHileVaoLar02gde1kKHBNfxSPo13MwbcI9ZX0qYh6LgyUZ00CIkPryZP0bChy1SU0_5QPBGUuzFhhSuxsI-Hw7RtO_VCLCxzKXtni-5DBBZDYKuqsOFLwxzdLwo6UOCnzI_RygBXTOS4fj_7xa-OYhdmZYk2-xXDxXuskHBCtNm5t9-nAAc5GQKpR8gdEaFujbXHw7-kStrTXfKYOCOZBZNW0u3K1KDdFI6wxDjDjUFmnpKzy_7MK6oz8kI-xn66KYMNkVyZKNzwzPCz4-ui3oMvhQTze-bzYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b525552494.mp4?token=HAsul6Zh2TnOSLM60bhbg3hRPs26zZ82H_EmgjNdmw-Z3XBFFijOHileVaoLar02gde1kKHBNfxSPo13MwbcI9ZX0qYh6LgyUZ00CIkPryZP0bChy1SU0_5QPBGUuzFhhSuxsI-Hw7RtO_VCLCxzKXtni-5DBBZDYKuqsOFLwxzdLwo6UOCnzI_RygBXTOS4fj_7xa-OYhdmZYk2-xXDxXuskHBCtNm5t9-nAAc5GQKpR8gdEaFujbXHw7-kStrTXfKYOCOZBZNW0u3K1KDdFI6wxDjDjUFmnpKzy_7MK6oz8kI-xn66KYMNkVyZKNzwzPCz4-ui3oMvhQTze-bzYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
بعد أيام من إستحواذ إيران على قواصة وإستهداف سفن حربية أمريكية.. ترامب: كل شيء دمر في إيران وسلاحها البحري يقبع في قاع الخليج.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90756" target="_blank">📅 03:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90755">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب:  الإيرانيون يتعرضون لخسائر فادحة ويريدون التوصل إلى اتفاق بشدة.  الحرب مع إيران ستنتهي قريبا جدا.  يمكننا التوصل إلى اتفاق بشأن إيران في أي وقت نريده.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90755" target="_blank">📅 03:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76ac567e2.mp4?token=iF1oYSY_pvlCzN8MapNEkLHakG_pLIni3IElpvqbfDPdL3iajhCfzoS0wMQWc2qfR538Vry_yBSPN5K0QytcWwISl3PQ_dyU0-S4s3Kzf8O3OdLxrr63PUSQTxp9xQjGw99jUcGdvK8iImdK5PFq45X-K2ksuoonV8AcRpTTp68JRlwKzWItpZyDeHTY76-NpvetennkE7mxq73xUjpLsvXqwoVryQ75a48x1PKf1Q-d8h7Ri42k4HNi1q2QQOV2vf7puqC02quGrdSH0ezZ1fMIi3Euxa7V41hLhL-tfwVynf7u-4TnVnIp_LLJeotcSuGQaG_A7q7hkHAsSjM5FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76ac567e2.mp4?token=iF1oYSY_pvlCzN8MapNEkLHakG_pLIni3IElpvqbfDPdL3iajhCfzoS0wMQWc2qfR538Vry_yBSPN5K0QytcWwISl3PQ_dyU0-S4s3Kzf8O3OdLxrr63PUSQTxp9xQjGw99jUcGdvK8iImdK5PFq45X-K2ksuoonV8AcRpTTp68JRlwKzWItpZyDeHTY76-NpvetennkE7mxq73xUjpLsvXqwoVryQ75a48x1PKf1Q-d8h7Ri42k4HNi1q2QQOV2vf7puqC02quGrdSH0ezZ1fMIi3Euxa7V41hLhL-tfwVynf7u-4TnVnIp_LLJeotcSuGQaG_A7q7hkHAsSjM5FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🔻
ترامب: لماذا يجب علينا أن نتحمل عبء الكثير من الدول في أوروبا؟ نحن نتحمل أعباء الدول الأوروبية. كل ما علينا فعله هو أن نقول: "هل تعلمون ماذا؟ لن نتعامل معكم بعد الآن." نحن لا نحتاج إلى أي شيء لديهم.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90754" target="_blank">📅 03:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455b367be5.mp4?token=jRbgQgZtQia88r9cSe_mRGNa4PWzlygyZ4AM82X5LvmLU9w_dfXl_00qRd2cHnAa01XaWDggyZB3VWqdT-IvnbfvziyzwyQ-S0k71OpA5NGf0NXvCOVpK3zxqZ09wjLP0LmNDSia-wnX0Q2qwYCRflhwvvxM_UEwc_FZTulKhgee2Jp0h_uH70F5Rl-CJIftsJSKbxkeOhUOyjr1fCZ-6eJ6WnG9jJIZw-0dTivJIxDtBPZXbkMJ5_Rn9ZyDSE-fkukYg84VU0rJVOHXU0PkUi3tDHKnNQTd6eMxZ4-Gs--bsjyQxzFrRzK31mDjq8vktLiPrYSWNf0lp-WBvPcImg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455b367be5.mp4?token=jRbgQgZtQia88r9cSe_mRGNa4PWzlygyZ4AM82X5LvmLU9w_dfXl_00qRd2cHnAa01XaWDggyZB3VWqdT-IvnbfvziyzwyQ-S0k71OpA5NGf0NXvCOVpK3zxqZ09wjLP0LmNDSia-wnX0Q2qwYCRflhwvvxM_UEwc_FZTulKhgee2Jp0h_uH70F5Rl-CJIftsJSKbxkeOhUOyjr1fCZ-6eJ6WnG9jJIZw-0dTivJIxDtBPZXbkMJ5_Rn9ZyDSE-fkukYg84VU0rJVOHXU0PkUi3tDHKnNQTd6eMxZ4-Gs--bsjyQxzFrRzK31mDjq8vktLiPrYSWNf0lp-WBvPcImg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب:  الإيرانيون يتعرضون لخسائر فادحة ويريدون التوصل إلى اتفاق بشدة.  الحرب مع إيران ستنتهي قريبا جدا.  يمكننا التوصل إلى اتفاق بشأن إيران في أي وقت نريده.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90753" target="_blank">📅 03:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a82a8098.mp4?token=gDP8B9Fvqeh3pimO8AXLVka8EL-XdNcP4UyW5rNvZEiARHyRi02bKsNjjZA6nK8EbFJeLldJ6OyDWdUIufYheDeKe2sjWWotxUbD1o3iKwsd6XNN9GnT1XO5o79txjd11y7-yZjh2CGKptvF0UDltOTDfS_eNGK2SZI4NJwpE3_NYKyG0GUZ3IsuWRf724dnZOFgxB122Mhe8M9WPuDSQE8S5QYAX4THiU-g-Mi0VI8HKc8eBH3Fti4xuzKdJrJOGAafU7NKMW16zbw2AsRDBv-5T9jvY5cbMo87FF1GcYV-r0qaCX5_fAoNnJoajFpDZ4sdnREU4ljHzGhQ8RbSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a82a8098.mp4?token=gDP8B9Fvqeh3pimO8AXLVka8EL-XdNcP4UyW5rNvZEiARHyRi02bKsNjjZA6nK8EbFJeLldJ6OyDWdUIufYheDeKe2sjWWotxUbD1o3iKwsd6XNN9GnT1XO5o79txjd11y7-yZjh2CGKptvF0UDltOTDfS_eNGK2SZI4NJwpE3_NYKyG0GUZ3IsuWRf724dnZOFgxB122Mhe8M9WPuDSQE8S5QYAX4THiU-g-Mi0VI8HKc8eBH3Fti4xuzKdJrJOGAafU7NKMW16zbw2AsRDBv-5T9jvY5cbMo87FF1GcYV-r0qaCX5_fAoNnJoajFpDZ4sdnREU4ljHzGhQ8RbSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المراسل: هل تعترف بأنهم يرفعون الأسعار بهدف خفض التكاليف بسبب الحرب في إيران؟
🇺🇸
ترامب: لا، إنهم يرفعون الأسعار لجعلني أسوأ ما يمكن. المشكلة التي يواجهونها هي أن لدينا أقوى اقتصاد في التاريخ.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90752" target="_blank">📅 03:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90750">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8zZTbqxWUmB-5DaLGmqL_smfKILwUm1rDcQ1BbHKm90CPJW54-zv_IqtCEDGCeVuaYVO2jaYFncWQLHR0SogQ8dJFFafqUs9DXwW1nI0XT8-K9Eoi3g5_qOHPXNBQjE_XE-t27OM3UcpRB9NUwvtO0zIBf1AC6V5RrMQXWAoiOdvzLBir59181Q_Db76D-Y-CUPXgk0cCMqCvQv15qRiRUYz-eijJlB_OKsHFtfomGhzzBxbm5-oWuBoiWcLx-tBRBkWsaF8fnOF3Bx_LVolK2RCdYezVMEbkU9agyN95rD1rGUbc74JApVne679IFIHRVzRca0q6YdqKfZsuXWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e0c180b1.mp4?token=ru7YPlhf59Lt4TdNZiVtgokJRgzxtPN4RDBHzhwx4pTSCL15ec9lR3ZE1YN3s7TtnZVgsuA6ZLZu0j4yeLjx_hInFvG1ap7ui21AR4gOVTjY9nswh4qezLwIwlE9dzVqLFLA0iiH3ZF3Z_mm1b2pFONgHEE5Ny9FJOTEkDlFGYauSktOmflVMO_8XNyR3nv5CWKv7Ogim8F78Ple-dTap2xAjT-JZBD6nj7okeZxvpxrOyAWOYQgG3GJktR53NNNnL6VDdXI9-5D1EFydI2vilXP2yxwc5dx5qOWv87ITcV9HThLgqfF18zzzUi6Bp7LROCrXUFCk5KQWdP1G-Sbig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e0c180b1.mp4?token=ru7YPlhf59Lt4TdNZiVtgokJRgzxtPN4RDBHzhwx4pTSCL15ec9lR3ZE1YN3s7TtnZVgsuA6ZLZu0j4yeLjx_hInFvG1ap7ui21AR4gOVTjY9nswh4qezLwIwlE9dzVqLFLA0iiH3ZF3Z_mm1b2pFONgHEE5Ny9FJOTEkDlFGYauSktOmflVMO_8XNyR3nv5CWKv7Ogim8F78Ple-dTap2xAjT-JZBD6nj7okeZxvpxrOyAWOYQgG3GJktR53NNNnL6VDdXI9-5D1EFydI2vilXP2yxwc5dx5qOWv87ITcV9HThLgqfF18zzzUi6Bp7LROCrXUFCk5KQWdP1G-Sbig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يستهدف العاصمة كييف ومدن أوكرانية أخرى.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90750" target="_blank">📅 03:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90749">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
‏
أكسيوس:
ترامب سيعقد مباحثات بشأن إيران مع قادة وفود دول الخليج بنيويورك الأسبوع المقبل.
‏ترامب سيطلع دول الخليج على أفكار لاستراتيجية ما بعد الحرب مع إيران.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90749" target="_blank">📅 03:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90748">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يستهدف العاصمة كييف ومدن أوكرانية أخرى.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90748" target="_blank">📅 02:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90747">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec03755b2.mp4?token=cYR0hVqvJ1yFRxLt36289asHhpwhG0nt1I8lEDQldoZmagJGbxX76xX7VIXKfQUpO3ppoThLYza6Gpn992q_rkpwWTPYrwCxa1xsTv8ImmiVZ0flhrzvqibAaqf347Af02nmaSbwzFnzlvC7Ip3wzwF3M5VAj609Na3mralYHl4Ad8zIO8li1DiWwFAuiNCRSrunRwU4HrUmPluOdNWAMEo31YvmpbzTqnVEKlSKdWBTMVhb0tlj6oUW4rSqgyTqSaykRDMSYp5rkrOWi6koTjCFKcBmj9yCSbxUGWDXNYHflywvgGuiC_8zZWLst9slIjm4ubw-aiH2CMUZQxEkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec03755b2.mp4?token=cYR0hVqvJ1yFRxLt36289asHhpwhG0nt1I8lEDQldoZmagJGbxX76xX7VIXKfQUpO3ppoThLYza6Gpn992q_rkpwWTPYrwCxa1xsTv8ImmiVZ0flhrzvqibAaqf347Af02nmaSbwzFnzlvC7Ip3wzwF3M5VAj609Na3mralYHl4Ad8zIO8li1DiWwFAuiNCRSrunRwU4HrUmPluOdNWAMEo31YvmpbzTqnVEKlSKdWBTMVhb0tlj6oUW4rSqgyTqSaykRDMSYp5rkrOWi6koTjCFKcBmj9yCSbxUGWDXNYHflywvgGuiC_8zZWLst9slIjm4ubw-aiH2CMUZQxEkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:  سعر الفائدة مرتفع للغاية ولا يعكس حقيقة الوضع الاقتصادي.  نحن في آخر مراحل الحرب مع إيران.  ‏قد نفرض تعريفات جمركية باهظة على أوروبا إذا اعتبرنا منح كندا صفة دولة مراقبة عملاً عدائياً.   إيران تريد بشدة التوصل إلى اتفاق.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90747" target="_blank">📅 02:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90746">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
دوي إنفجار في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90746" target="_blank">📅 02:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90745">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9188e09e6.mp4?token=EzUg4jkoEefMubrTL4cSLcfae4UEUr-NMLWxuBuewR46s9_AtwE5SrEjq24ymWmIoPAoiTeegLIfVc-0p4Xtho2AwF9c_bBMkPkXpkFsiOOs6rAXG99hbsbXXjeeHtXZ1_zk1kgFKZYKCZVplr-Snd6Ka4twphFFGRf_VM7kvRep_rOmoUna7TDK6j9qEQ6HXw70AfKzeE8IXprGAYa1Z1I1OQXFmf_B24k_joJkP59wnWMcf9bcNIPyABx0jxJILMMJOKYphy6NUGNXCdj_Ink1w0a_8HVQdvXnECn9noSvgvQvsZf6TpnQw0PkXdCmUq8Oaw44jSB7P7R4X6wC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9188e09e6.mp4?token=EzUg4jkoEefMubrTL4cSLcfae4UEUr-NMLWxuBuewR46s9_AtwE5SrEjq24ymWmIoPAoiTeegLIfVc-0p4Xtho2AwF9c_bBMkPkXpkFsiOOs6rAXG99hbsbXXjeeHtXZ1_zk1kgFKZYKCZVplr-Snd6Ka4twphFFGRf_VM7kvRep_rOmoUna7TDK6j9qEQ6HXw70AfKzeE8IXprGAYa1Z1I1OQXFmf_B24k_joJkP59wnWMcf9bcNIPyABx0jxJILMMJOKYphy6NUGNXCdj_Ink1w0a_8HVQdvXnECn9noSvgvQvsZf6TpnQw0PkXdCmUq8Oaw44jSB7P7R4X6wC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مجلس النواب الأميركي يصوت لصالح تشديد العقوبات وفرض رسوم على روسيا وإيران.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90745" target="_blank">📅 01:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90744">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
مجلس النواب الأميركي يصوت لصالح تشديد العقوبات وفرض رسوم على روسيا وإيران.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90744" target="_blank">📅 01:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90743">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f566eb691.mp4?token=dUdoirDbWVkxRUnX0miemt65Ji0jxuKbNMF9vj4NpPAu-X_0JBHaFX52TEOffzr6dhX1fTEGsqJAiNix2LxkvYVW8r-SZeVjTxaOdMYEfTIphazqaoyzYWarkJb9Dih0O7a4Rr6qg6OC_n1hAdAR9ik3qf_9W7wF11CzKMd3IidCqQxs5jIo4AGxfF2aLkJAvbnP-qo1qF7chyjlCqoN51illNWjhWNJKypGnkxYpgCAcP_n7vLdUOCipfzlSpk725tJ7zgg8Fvua7bZZ4iCmuQOMjO6pPHIPKzmb0GF0B8744voLcm6ogxQH8MqlMaelIRvn7fb32ba67603YjheA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f566eb691.mp4?token=dUdoirDbWVkxRUnX0miemt65Ji0jxuKbNMF9vj4NpPAu-X_0JBHaFX52TEOffzr6dhX1fTEGsqJAiNix2LxkvYVW8r-SZeVjTxaOdMYEfTIphazqaoyzYWarkJb9Dih0O7a4Rr6qg6OC_n1hAdAR9ik3qf_9W7wF11CzKMd3IidCqQxs5jIo4AGxfF2aLkJAvbnP-qo1qF7chyjlCqoN51illNWjhWNJKypGnkxYpgCAcP_n7vLdUOCipfzlSpk725tJ7zgg8Fvua7bZZ4iCmuQOMjO6pPHIPKzmb0GF0B8744voLcm6ogxQH8MqlMaelIRvn7fb32ba67603YjheA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:
سعر الفائدة مرتفع للغاية ولا يعكس حقيقة الوضع الاقتصادي.
نحن في آخر مراحل الحرب مع إيران.
‏قد نفرض تعريفات جمركية باهظة على أوروبا إذا اعتبرنا منح كندا صفة دولة مراقبة عملاً عدائياً.
إيران تريد بشدة التوصل إلى اتفاق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90743" target="_blank">📅 01:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90742">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6309a31e7c.mp4?token=iB9WhMtWiL5J07Ts15aionHe7bOA487NHg0x6p3HF1ds4I1qWEEG7NYI0msiOVcoYW8hjpk3F8Goy8-H-x81J_qyo8-Bl7p8fdpi-NbYsBEGEYlQyUetsz_Zhx6nEMsmtz6n7gmuSVvqcdmQrlhaW00qmzR1YG3libp-z3mA1zPHjZ3ZmFOvE8eo-NkL_3-P0k1j7DHs0pSG1-03gickDkx9xKXknwJdmXF9QtvHGRmcHb7Lmyk8s5Cyn9HW9IZbKYQnOiHBIq8xr1bhd6WTlyA4SrWj9m5Kjh22bU_tAbPYH3tCE9odhRhQ1k1qndcYejfjlvfCS3NkVBLPYws6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6309a31e7c.mp4?token=iB9WhMtWiL5J07Ts15aionHe7bOA487NHg0x6p3HF1ds4I1qWEEG7NYI0msiOVcoYW8hjpk3F8Goy8-H-x81J_qyo8-Bl7p8fdpi-NbYsBEGEYlQyUetsz_Zhx6nEMsmtz6n7gmuSVvqcdmQrlhaW00qmzR1YG3libp-z3mA1zPHjZ3ZmFOvE8eo-NkL_3-P0k1j7DHs0pSG1-03gickDkx9xKXknwJdmXF9QtvHGRmcHb7Lmyk8s5Cyn9HW9IZbKYQnOiHBIq8xr1bhd6WTlyA4SrWj9m5Kjh22bU_tAbPYH3tCE9odhRhQ1k1qndcYejfjlvfCS3NkVBLPYws6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إرتفاع أعمدة الدخان في شارع فلسطين بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90742" target="_blank">📅 01:57 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
